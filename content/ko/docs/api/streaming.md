---
title: "스트리밍 프로토콜"
description: "대부분의 I2P 애플리케이션에서 사용하는 TCP와 유사한 전송 방식"
slug: "streaming"
lastUpdated: "2025-07"
accurateFor: "0.9.67"
---

## 개요 {#overview}

streaming 라이브러리는 핵심 router 기능이 아니기 때문에 기술적으로는 "애플리케이션" 계층의 일부입니다. 하지만 실제로는 I2P를 통해 TCP와 유사한 스트림을 제공하고 기존 앱을 I2P로 쉽게 포팅할 수 있게 해주어, 거의 모든 기존 I2P 애플리케이션에 필수적인 기능을 제공합니다. 클라이언트 통신을 위한 다른 종단 간 전송 라이브러리는 [datagram library](/docs/specs/datagrams)입니다.

스트리밍 라이브러리는 핵심 [I2CP API](/docs/specs/i2cp) 위에 구축된 계층으로, 신뢰할 수 없고 순서가 보장되지 않으며 인증되지 않은 메시지 계층 위에서 신뢰할 수 있고 순서가 보장되며 인증된 메시지 스트림이 작동할 수 있도록 합니다. TCP와 IP의 관계와 마찬가지로, 이 스트리밍 기능에는 다양한 절충점과 최적화 옵션이 있지만, 이러한 기능을 기본 I2P 코드에 포함시키지 않고 별도의 라이브러리로 분리하여 TCP와 유사한 복잡성을 분리하고 대안적인 최적화된 구현을 가능하게 했습니다.

메시지의 상대적으로 높은 비용을 고려하여, streaming 라이브러리의 메시지 스케줄링 및 전달 프로토콜은 개별 메시지가 가능한 한 많은 정보를 담을 수 있도록 최적화되었습니다. 예를 들어, streaming 라이브러리를 통해 프록시되는 소규모 HTTP 트랜잭션은 단일 왕복으로 완료될 수 있습니다 - 첫 번째 메시지는 SYN, FIN, 그리고 소규모 HTTP 요청 페이로드를 묶고, 응답은 SYN, FIN, ACK, 그리고 HTTP 응답 페이로드를 묶습니다. SYN/FIN/ACK가 수신되었음을 HTTP 서버에 알리기 위해 추가 ACK가 전송되어야 하지만, 로컬 HTTP 프록시는 종종 전체 응답을 브라우저에 즉시 전달할 수 있습니다.

streaming 라이브러리는 슬라이딩 윈도우, 혼잡 제어 알고리즘(slow start와 congestion avoidance 모두), 그리고 일반적인 패킷 동작(ACK, SYN, FIN, RST, rto 계산 등)을 갖춘 TCP의 추상화와 매우 유사합니다.

스트리밍 라이브러리는 I2P 상에서의 동작에 최적화된 견고한 라이브러리입니다. 이는 1단계 설정을 가지고 있으며, 완전한 윈도우잉 구현을 포함하고 있습니다.

## API {#api}

스트리밍 라이브러리 API는 Java 애플리케이션에 표준 소켓 패러다임을 제공합니다. 하위 레벨의 [I2CP](/docs/specs/i2cp) API는 완전히 숨겨져 있지만, 애플리케이션은 스트리밍 라이브러리를 통해 [I2CP 매개변수](/docs/specs/i2cp#options)를 전달하여 I2CP가 해석하도록 할 수 있습니다.

streaming lib의 표준 인터페이스는 애플리케이션이 I2PSocketManagerFactory를 사용하여 I2PSocketManager를 생성하는 것입니다. 그러면 애플리케이션은 socket manager에게 I2PSession을 요청하며, 이는 [I2CP](/docs/specs/i2cp)를 통해 router와의 연결을 발생시킵니다. 그 후 애플리케이션은 I2PSocket으로 연결을 설정하거나 I2PServerSocket으로 연결을 수신할 수 있습니다.

사용법의 좋은 예시를 보려면 i2psnark 코드를 참조하세요.

### 옵션과 기본값 {#options}

옵션들과 현재 기본값들이 아래에 나열되어 있습니다. 옵션들은 대소문자를 구분하며 전체 router에 대해, 특정 클라이언트에 대해, 또는 연결별로 개별 소켓에 대해 설정할 수 있습니다. 많은 값들이 일반적인 I2P 조건에서 HTTP 성능을 위해 조정되어 있습니다. P2P 서비스와 같은 다른 애플리케이션들은 I2PSocketManagerFactory.createManager(_i2cpHost, _i2cpPort, opts) 호출을 통해 옵션을 설정하고 전달하여 필요에 따라 수정할 것을 강력히 권장합니다. 시간 값들은 ms 단위입니다.

[SAM](/docs/api/samv3), [BOB](/docs/legacy/bob), [I2PTunnel](/docs/api/i2ptunnel)과 같은 상위 계층 API는 자체 기본값으로 이러한 기본값을 재정의할 수 있다는 점에 유의하세요. 또한 많은 옵션이 들어오는 연결을 수신하는 서버에만 적용된다는 점도 참고하시기 바랍니다.

릴리스 0.9.1부터, 활성 소켓 관리자나 세션에서 대부분의 옵션을 변경할 수 있지만 모든 옵션이 가능한 것은 아닙니다. 자세한 내용은 javadocs를 참조하세요.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Default</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.accessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes used for either access list or blacklist. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.destination.sigType</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The name or number of the signature type for a transient destination. As of release 0.9.12.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableAccessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a whitelist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableBlackList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a blacklist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.answerPings</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to respond to incoming pings</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.blacklist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes to be blacklisted for incoming connections to ALL destinations in the context. This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.3.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.bufferSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64K</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How much transmit data (in bytes) will be accepted that hasn't been written out yet.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.congestionAvoidanceGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in congestion avoidance, we grow the window size at the rate of <code>1/(windowSize*factor)</code>. In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to wait after instantiating a new con before actually attempting to connect. If this is &lt;= 0, connect immediately with no initial data. If greater than 0, wait until the output stream is flushed, the buffer fills, or that many milliseconds pass, and include any initial data with the SYN.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5*60*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on connect, in milliseconds. Negative means indefinitely. Default is 5 minutes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.disableRejectLogging</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to disable warnings in the logs when an incoming connection is rejected due to connection limits. As of release 0.9.4.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.dsalist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes or host names to be contacted using an alternate DSA destination. Only applies if multisession is enabled and the primary session is non-DSA (generally for shared clients only). This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.21.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.enforceProtocol</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to listen only for the streaming protocol. Setting to true will prohibit communication with Destinations earlier than release 0.7.1 (released March 2009). Set to true if running multiple protocols on this Destination. As of release 0.9.1. Default true as of release 0.9.36.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 (send)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0=noop, 1=disconnect) What to do on an inactivity timeout - do nothing, disconnect, or send a duplicate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">90*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Idle time before sending a keepalive</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialAckDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">750</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Delay before sending an ack</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialResendDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The initial value of the resend delay field in the packet header, times 1000. Not fully implemented; see below.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial timeout (if no <a href="#sharing">sharing data</a> available). As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial round trip time estimate (if no <a href="#sharing">sharing data</a> available). Disabled as of release 0.9.8; uses actual RTT.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(if no <a href="#sharing">sharing data</a> available) In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.limitAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reset</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">What action to take when an incoming connection exceeds limits. Valid values are: reset (reset the connection); drop (drop the connection); or http (send a hardcoded HTTP 429 response). Any other value is a custom response to be sent. backslash-r and backslash-n will be replaced with CR and LF. As of release 0.9.34.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConcurrentStreams</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0 or negative value means unlimited) This is a total limit for incoming and outgoing combined.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxMessageSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1730</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum size of the payload, i.e. the MTU in bytes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxResends</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Maximum number of retransmissions before failure.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (all peers; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.profile</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 (bulk)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1=bulk; 2=interactive; see important notes <a href="#profile">below</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.readTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on read, in milliseconds. Negative means indefinitely.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.slowStartGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in slow start, we grow the window size at the rate of 1/(factor). In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttdevDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.wdwDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.writeTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on write/flush, in milliseconds. Negative means indefinitely.</td>
    </tr>
  </tbody>
</table>
## 프로토콜 사양 {#spec}

[Streaming Library 사양 페이지를 참조하세요.](/docs/specs/streaming)

## 구현 세부사항 {#implementation}

### 설정 {#setup}

개시자는 SYNCHRONIZE 플래그가 설정된 패킷을 보냅니다. 이 패킷에는 초기 데이터도 포함될 수 있습니다. 상대방은 SYNCHRONIZE 플래그가 설정된 패킷으로 응답합니다. 이 패킷에는 초기 응답 데이터도 포함될 수 있습니다.

개시자는 SYNCHRONIZE 응답을 받기 전에 초기 윈도우 크기까지 추가 데이터 패킷을 보낼 수 있습니다. 이러한 패킷들도 송신 Stream ID 필드가 0으로 설정됩니다. 수신자는 SYNCHRONIZE 패킷보다 먼저 도착하여 순서가 바뀔 수 있으므로, 알려지지 않은 스트림에서 받은 패킷들을 짧은 시간 동안 버퍼링해야 합니다.

### MTU 선택 및 협상 {#mtu}

최대 메시지 크기(MTU / MRU라고도 함)는 두 피어가 지원하는 더 낮은 값으로 협상됩니다. tunnel 메시지는 1KB로 패딩되므로, 잘못된 MTU 선택은 많은 오버헤드를 초래합니다. MTU는 i2p.streaming.maxMessageSize 옵션으로 지정됩니다. 현재 기본 MTU인 1730은 일반적인 경우의 오버헤드를 포함하여 두 개의 1K I2NP tunnel 메시지에 정확히 맞도록 선택되었습니다.

참고: 이는 헤더를 제외한 페이로드만의 최대 크기입니다.

참고: 오버헤드가 줄어든 ECIES 연결의 경우, 권장 MTU는 1812입니다. 기본 MTU는 사용되는 키 유형에 관계없이 모든 연결에서 1730으로 유지됩니다. 클라이언트는 평소와 같이 송신 및 수신 MTU 중 최솟값을 사용해야 합니다. proposal 155를 참조하세요.

연결의 첫 번째 메시지에는 streaming 계층에서 추가하는 387바이트(일반적) Destination과, 보통 898바이트(일반적) LeaseSet, 그리고 router에 의해 garlic 메시지에 번들링된 Session 키들이 포함됩니다. (ElGamal Session이 이전에 설정된 경우 LeaseSet과 Session Keys는 번들링되지 않습니다). 따라서 완전한 HTTP 요청을 단일 1KB I2NP 메시지에 맞추는 목표가 항상 달성 가능한 것은 아닙니다. 그러나 MTU의 선택과 tunnel 게이트웨이 프로세서에서 조각화 및 배치 전략의 신중한 구현은 네트워크 대역폭, 지연시간, 안정성, 효율성에서 중요한 요소이며, 특히 오래 지속되는 연결의 경우 더욱 그렇습니다.

### 데이터 무결성 {#integrity}

데이터 무결성은 [I2CP 계층](/docs/specs/i2cp#format)에서 구현된 gzip CRC-32 체크섬으로 보장됩니다. 스트리밍 프로토콜에는 체크섬 필드가 없습니다.

### 패킷 캡슐화 {#encapsulation}

각 패킷은 단일 메시지로(또는 [Garlic Message](/docs/overview/garlic-routing)의 개별 clove로) I2P를 통해 전송됩니다. 메시지 캡슐화는 기본 [I2CP](/docs/specs/i2cp), [I2NP](/docs/specs/i2np), 그리고 [tunnel message](/docs/specs/tunnel-message) 계층에서 구현됩니다. 스트리밍 프로토콜에는 패킷 구분 메커니즘이나 페이로드 길이 필드가 없습니다.

### 선택적 지연 {#delay}

데이터 패킷에는 수신자가 패킷을 ack하기 전에 요청된 지연 시간을 ms 단위로 지정하는 선택적 지연 필드가 포함될 수 있습니다. 유효한 값은 0부터 60000까지입니다. 0 값은 즉시 ack를 요청합니다. 이는 권고사항일 뿐이며, 수신자는 추가 패킷들을 단일 ack로 승인할 수 있도록 약간 지연해야 합니다. 일부 구현에서는 이 필드에 (측정된 RTT / 2)의 권고 값을 포함할 수 있습니다. 0이 아닌 선택적 지연 값의 경우, 수신자는 ack를 보내기 전의 최대 지연 시간을 최대 몇 초로 제한해야 합니다. 60000보다 큰 선택적 지연 값은 choking을 나타내며, 아래를 참조하십시오.

### 전송/수신 윈도우와 Choking {#windows}

TCP 헤더는 수신 윈도우를 바이트 단위로 포함하지만, 스트리밍 프로토콜은 최대 수신 윈도우 크기를 바이트나 패킷 단위로 교환하는 방법을 제공하지 않습니다. 수신 버퍼가 가득 찼음을 나타내는 단순한 choke/unchoke 표시만 있을 뿐입니다. 각 엔드포인트는 원격 엔드의 수신 윈도우에 대한 자체 추정치를 바이트 또는 패킷 단위로 유지해야 합니다. 클라이언트 애플리케이션이 버퍼를 비우는 속도가 느리면 어떤 윈도우 크기에서든 수신 버퍼가 오버플로될 수 있다는 점에 주의하십시오.

Java 구현에서 기본 최대 전송 및 수신 윈도우 크기는 128개 패킷입니다. 최대 전송 윈도우 크기를 128보다 높게 설정하는 구현체는 다음 문제들을 고려해야 합니다:

- 수신 버퍼 오버플로로 인한 Java router의 CHOKE 응답이 훨씬 더 발생하기 쉽습니다.
- 반복적인 오버플로를 완화하기 위해 원격 수신기 버퍼 크기 추정이 구현되어야 합니다 (위 참조)
- CHOKE는 올바르게 처리되어야 합니다 (아래 참조)
- 256을 초과하는 최대 윈도우 크기는 더욱 오류가 발생하기 쉽습니다. nack count 옵션 필드 길이가 1바이트이므로 최대 NACK 수가 255개로 제한되기 때문입니다. 이 사양은 255개를 초과하는 NACK가 있을 때 어떻게 해야 하는지 다루지 않습니다. 256을 초과하는 최대 윈도우 크기는 권장되지 않습니다.

수신자 구현에 권장되는 최소 버퍼 크기는 128개 패킷 또는 232KB(약 128 * 1812)입니다. I2P 네트워크 지연, 패킷 손실, 그리고 그로 인한 혼잡 제어로 인해 이 크기의 버퍼가 가득 찰 일은 거의 없습니다. 하지만 고대역폭 "로컬 루프백"(같은 router) 연결이나 로컬 테스트에서는 오버플로가 발생할 가능성이 훨씬 높습니다.

오버플로우 상황을 빠르게 표시하고 원활하게 복구하기 위해, 스트리밍 프로토콜에는 pushback을 위한 간단한 메커니즘이 있습니다. 선택적 지연 필드 값이 60001 이상인 패킷이 수신되면, 이는 "choking" 또는 수신 윈도우가 0임을 나타냅니다. 선택적 지연 필드 값이 60000 이하인 패킷은 "unchoking"을 나타냅니다. 선택적 지연 필드가 없는 패킷은 choke/unchoke 상태에 영향을 주지 않습니다.

choke된 후에는, 손실된 unchoke 패킷들을 보상하기 위한 occasional한 "probe" 데이터 패킷들을 제외하고는 transmitter가 unchoke될 때까지 데이터가 포함된 더 이상의 패킷을 보내지 않아야 합니다. choke된 endpoint는 TCP에서처럼 probing을 제어하기 위해 "persist timer"를 시작해야 합니다. unchoking endpoint는 이 필드가 설정된 여러 패킷을 보내거나, 데이터 패킷이 다시 수신될 때까지 주기적으로 계속 보내야 합니다. unchoking을 기다리는 최대 시간은 구현에 따라 다릅니다. unchoke된 후의 transmitter 윈도우 크기와 congestion control 전략은 구현에 따라 다릅니다.

### 혼잡 제어 {#congestion}

스트리밍 라이브러리는 지수적 백오프와 함께 표준 슬로우 스타트(지수적 윈도우 증가)와 혼잡 회피(선형 윈도우 증가) 단계를 사용합니다. 윈도잉과 확인응답은 바이트 수가 아닌 패킷 수를 사용합니다.

### 닫기 {#close}

SYNCHRONIZE 플래그가 설정된 패킷을 포함하여 모든 패킷은 CLOSE 플래그도 함께 전송할 수 있습니다. 연결은 피어가 CLOSE 플래그로 응답할 때까지 닫히지 않습니다. CLOSE 패킷에도 데이터가 포함될 수 있습니다.

### Ping / Pong {#ping}

I2CP 계층(ICMP echo에 해당)이나 데이터그램에는 ping 기능이 없습니다. 이 기능은 스트리밍에서 제공됩니다. ping과 pong은 표준 스트리밍 패킷과 결합될 수 없습니다. ECHO 옵션이 설정되면 대부분의 다른 플래그, 옵션, ackThrough, sequenceNum, NACK 등이 무시됩니다.

ping 패킷은 ECHO, SIGNATURE_INCLUDED, FROM_INCLUDED 플래그가 설정되어야 합니다. sendStreamId는 0보다 커야 하며, receiveStreamId는 무시됩니다. sendStreamId는 기존 연결과 일치할 수도 있고 그렇지 않을 수도 있습니다.

pong 패킷은 ECHO 플래그가 설정되어야 합니다. sendStreamId는 0이어야 하고, receiveStreamId는 ping의 sendStreamId입니다. 릴리스 0.9.18 이전에는 pong 패킷이 ping에 포함된 페이로드를 포함하지 않습니다.

릴리스 0.9.18부터 ping과 pong은 페이로드를 포함할 수 있습니다. ping에 포함된 페이로드는 최대 32바이트까지 가능하며, pong에서 그대로 반환됩니다.

스트리밍은 `i2p.streaming.answerPings=false` 설정으로 pong 전송을 비활성화하도록 구성할 수 있습니다.

### i2p.streaming.profile 참고사항 {#profile}

이 옵션은 두 가지 값을 지원합니다; 1=bulk, 2=interactive. 이 옵션은 예상되는 트래픽 패턴에 대해 스트리밍 라이브러리 및/또는 router에 힌트를 제공합니다.

"Bulk"는 지연 시간을 희생하더라도 높은 대역폭에 최적화한다는 의미입니다. 이것이 기본값입니다. "Interactive"는 대역폭이나 효율성을 희생하더라도 낮은 지연 시간에 최적화한다는 의미입니다. 최적화 전략이 있다면 구현에 따라 달라지며, 스트리밍 프로토콜 외부의 변경 사항을 포함할 수 있습니다.

API 버전 0.9.63까지, Java I2P는 1 (bulk) 이외의 모든 값에 대해 오류를 반환하고 tunnel이 시작에 실패했습니다. API 0.9.64부터 Java I2P는 이 값을 무시합니다. API 버전 0.9.63까지 i2pd는 이 옵션을 무시했으나, API 0.9.64부터 i2pd에서 구현되었습니다.

스트리밍 프로토콜에는 프로필 설정을 상대방에게 전달하는 플래그 필드가 포함되어 있지만, 이는 알려진 어떤 router에서도 구현되지 않았습니다.

### Control Block 공유 {#sharing}

streaming lib은 "TCP" Control Block 공유를 지원합니다. 이는 동일한 원격 피어에 대한 연결 간에 세 가지 중요한 streaming lib 매개변수(윈도우 크기, 왕복 시간, 왕복 시간 분산)를 공유합니다. 이는 연결 중 "ensemble" 공유가 아닌 연결 열기/닫기 시점의 "temporal" 공유에 사용됩니다([RFC 2140](http://www.ietf.org/rfc/rfc2140.txt) 참조). 동일한 router의 다른 Destination에 정보 누출이 없도록 ConnectionManager(즉, 로컬 Destination)마다 별도의 공유가 있습니다. 특정 피어에 대한 공유 데이터는 몇 분 후 만료됩니다. 다음 Control Block 공유 매개변수들을 router별로 설정할 수 있습니다:

- RTT_DAMPENING = 0.75
- RTTDEV_DAMPENING = 0.75
- WINDOW_DAMPENING = 0.75

### 기타 매개변수 {#other}

다음 매개변수들은 권장되는 기본값입니다. 기본값은 구현에 따라 다를 수 있습니다:

- MIN_RESEND_DELAY = 100 ms (최소 RTO)
- MAX_RESEND_DELAY = 45 sec (최대 RTO)
- MIN_WINDOW_SIZE = 1
- MAX_WINDOW_SIZE = 128
- TREND_COUNT = 3
- MIN_MESSAGE_SIZE = 512 (최소 MTU)
- INBOUND_BUFFER_SIZE = maxMessageSize * (maxWindowSize + 2)
- INITIAL_TIMEOUT (RTT가 샘플링되기 전에만 유효) = 9 sec
- "alpha" ( RFC 6298에 따른 RTT 감쇠 인수 ) = 0.125
- "beta" ( RFC 6298에 따른 RTTDEV 감쇠 인수 ) = 0.25
- "K" ( RFC 6298에 따른 RTDEV 승수 ) = 4
- PASSIVE_FLUSH_DELAY = 175 ms
- 최대 RTT 추정값: 60 sec

### 역사 {#history}

streaming 라이브러리는 I2P를 위해 유기적으로 성장해왔습니다 - 처음에 mihi가 I2PTunnel의 일부로 "mini streaming library"를 구현했는데, 이는 1개 메시지의 윈도우 크기로 제한되어 있었습니다 (다음 메시지를 보내기 전에 ACK를 요구). 그 후 이것은 일반적인 streaming 인터페이스(TCP 소켓을 모방)로 리팩토링되었고, 슬라이딩 윈도우 프로토콜과 높은 대역폭 x 지연 곱을 고려한 최적화를 포함한 완전한 streaming 구현이 배포되었습니다. 개별 스트림은 최대 패킷 크기와 기타 옵션을 조정할 수 있습니다. 기본 메시지 크기는 두 개의 1K I2NP tunnel 메시지에 정확히 맞도록 선택되었으며, 손실된 메시지를 재전송하는 대역폭 비용과 여러 메시지의 지연 시간 및 오버헤드 사이의 합리적인 절충안입니다.

## 향후 작업 {#future}

스트리밍 라이브러리의 동작은 애플리케이션 수준의 성능에 심대한 영향을 미치므로, 추가 분석이 필요한 중요한 영역입니다.

- streaming lib 매개변수의 추가 튜닝이 필요할 수 있습니다.
- 연구가 필요한 또 다른 영역은 streaming lib와 NTCP 및 SSU 전송 계층 간의 상호작용입니다. 자세한 내용은 [NTCP 토론 페이지](/docs/historical/ntcp-discussion)를 참조하세요.
- 라우팅 알고리즘과 streaming lib의 상호작용은 성능에 큰 영향을 미칩니다. 특히, 풀 내 여러 tunnel로 메시지를 무작위 배포하면 순서가 뒤바뀐 전달이 많이 발생하여 그렇지 않았다면 가능했을 것보다 작은 윈도우 크기가 됩니다. router는 현재 단일 송신자/수신자 목적지 쌍에 대한 메시지를 일관된 tunnel 세트를 통해 라우팅하며, tunnel 만료나 전달 실패가 발생할 때까지 유지됩니다. router의 실패 및 tunnel 선택 알고리즘을 개선 가능성에 대해 검토해야 합니다.
- 첫 번째 SYN 패킷의 데이터가 수신자의 MTU를 초과할 수 있습니다.
- DELAY_REQUESTED 필드를 더 많이 활용할 수 있습니다.
- 단기간 스트림에서 중복된 초기 SYNCHRONIZE 패킷이 인식되지 않고 제거되지 않을 수 있습니다.
- 재전송에서 MTU를 전송하지 마세요.
- 아웃바운드 윈도우가 가득 찬 경우가 아니면 데이터가 전송됩니다. (즉, no-Nagle 또는 TCP_NODELAY) 이에 대한 구성 옵션이 있어야 할 것 같습니다.
- zzz가 streaming library에 wireshark 호환(pcap) 형식으로 패킷을 로그하는 디버그 코드를 추가했습니다. 이를 사용하여 성능을 추가 분석하세요. 더 많은 streaming lib 매개변수를 TCP 필드에 매핑하기 위해 형식을 개선해야 할 수 있습니다.
- streaming lib를 표준 TCP(또는 raw socket과 함께 null 계층)로 교체하는 제안들이 있습니다. 이는 불행히도 streaming lib와 호환되지 않지만 두 방식의 성능을 비교하는 것은 좋을 것입니다.
