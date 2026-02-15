---
title: "UDP Tracker"
description: "I2P에서 UDP BitTorrent 공지를 위한 프로토콜 사양"
slug: "udp-announces"
aliases:
  - "/ko/docs/specs/udp-bittorrent-announces"
  - "/ko/docs/specs/udp-bittorrent-announces/"
category: "프로토콜"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

## 개요

이 사양서는 I2P에서 UDP bittorrent 공지를 위한 프로토콜을 문서화합니다. I2P에서 bittorrent의 전체 사양에 대해서는 [BitTorrent over I2P](/docs/applications/bittorrent)를 참조하십시오. 이 사양의 개발 배경 및 추가 정보는 [Proposal 160](/proposals/160-udp-trackers)을 참조하십시오.

## 설계

이 제안서는 [Datagrams](/docs/specs/datagrams)에서 정의된 repliable datagram2, repliable datagram3, 그리고 raw datagrams을 사용합니다. Datagram2와 Datagram3는 [Proposal 163](/proposals/163-datagram2-datagram3)에서 정의된 repliable datagrams의 새로운 변형입니다. Datagram2는 재생 공격 저항성과 오프라인 서명 지원을 추가합니다. Datagram3는 기존 datagram 형식보다 작지만 인증 기능은 없습니다.

### BEP 15

참고로, [BEP 15](http://www.bittorrent.org/beps/bep_0015.html)에 정의된 메시지 플로우는 다음과 같습니다:

```
Client                        Tracker
    Connect Req. ------------->
      <-------------- Connect Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
```
연결 단계는 IP 주소 스푸핑을 방지하기 위해 필요합니다. tracker는 클라이언트가 후속 announce에서 사용하는 연결 ID를 반환합니다. 이 연결 ID는 클라이언트에서 기본적으로 1분 후에 만료되고, tracker에서는 2분 후에 만료됩니다.

I2P는 기존 UDP 지원 클라이언트 코드베이스에서의 채택 용이성, 효율성, 그리고 아래에서 논의할 보안상의 이유로 BEP 15와 동일한 메시지 플로우를 사용할 것입니다:

```
Client                        Tracker
    Connect Req. ------------->       (Repliable Datagram2)
      <-------------- Connect Resp.   (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
             ...
```
이는 스트리밍(TCP) 공지에 비해 잠재적으로 큰 대역폭 절약을 제공합니다. Datagram2는 스트리밍 SYN과 거의 같은 크기이지만, raw 응답은 스트리밍 SYN ACK보다 훨씬 작습니다. 후속 요청은 Datagram3을 사용하며, 후속 응답은 raw입니다.

announce 요청은 Datagram3를 사용하므로 tracker가 connection ID에서 announce 대상이나 해시로의 대규모 매핑 테이블을 유지할 필요가 없습니다. 대신 tracker는 sender 해시, 현재 타임스탬프(특정 간격 기반), 그리고 비밀 값으로부터 암호화 방식으로 connection ID를 생성할 수 있습니다. announce 요청이 수신되면 tracker는 connection ID를 검증한 후 Datagram3 sender 해시를 전송 대상으로 사용합니다.

### 연결 수명

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html)는 연결 ID가 클라이언트에서는 1분, 트래커에서는 2분 후에 만료되도록 명시하고 있습니다. 이는 구성할 수 없습니다. 클라이언트가 모든 announce를 1분 내에 일괄 처리하지 않는 한, 이는 잠재적인 효율성 향상을 제한합니다. i2psnark는 현재 announce를 일괄 처리하지 않으며, 트래픽 버스트를 피하기 위해 분산시킵니다. 파워 유저들은 한 번에 수천 개의 torrent를 실행하는 것으로 알려져 있으며, 그 많은 announce를 1분 안에 버스트로 처리하는 것은 현실적이지 않습니다.

여기서, 선택적인 연결 수명 필드를 추가하기 위해 연결 응답을 확장할 것을 제안합니다. 존재하지 않는 경우 기본값은 1분입니다. 그렇지 않으면, 초 단위로 지정된 수명이 클라이언트에 의해 사용되며, tracker는 연결 ID를 1분 더 유지합니다.

### BEP 15와의 호환성

이 설계는 기존 클라이언트와 tracker에서 필요한 변경 사항을 최소화하기 위해 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html)와 가능한 한 호환성을 유지합니다.

유일하게 필요한 변경사항은 announce 응답에서 피어 정보의 형식입니다. connect 응답에서 lifetime 필드를 추가하는 것은 필수가 아니지만 위에서 설명한 바와 같이 효율성을 위해 강력히 권장됩니다.

### 보안 분석

UDP announce 프로토콜의 중요한 목표는 주소 스푸핑을 방지하는 것입니다. 클라이언트는 실제로 존재해야 하며 실제 leaseset을 번들로 포함해야 합니다. Connect Response를 받기 위한 인바운드 tunnel이 있어야 합니다. 이러한 tunnel은 zero-hop이며 즉시 구축될 수 있지만, 이는 생성자를 노출시킬 수 있습니다. 이 프로토콜은 그 목표를 달성합니다.

### 문제점

- 이 프로토콜은 블라인드 대상을 지원하지 않지만, 지원하도록 확장될 수 있습니다. 아래를 참조하세요.

## 명세서

### 프로토콜과 포트

Repliable Datagram2는 I2CP protocol 19를 사용하고, repliable Datagram3는 I2CP protocol 20을 사용하며, raw datagram은 I2CP protocol 18을 사용합니다. 요청은 Datagram2 또는 Datagram3일 수 있습니다. 응답은 항상 raw입니다. I2CP protocol 17을 사용하는 구형 repliable datagram("Datagram1") 형식은 요청이나 응답에 사용되어서는 안 되며, 요청/응답 포트에서 수신될 경우 드롭되어야 합니다. Datagram1 protocol 17은 여전히 DHT protocol에 사용됩니다.

요청은 announce URL의 I2CP "to port"를 사용합니다. 아래를 참조하세요. 요청의 "from port"는 클라이언트에서 선택하지만, 0이 아닌 값이어야 하고 DHT에서 사용하는 포트와 다른 포트여야 응답을 쉽게 분류할 수 있습니다. 트래커는 잘못된 포트로 수신된 요청을 거부해야 합니다.

응답은 요청의 I2CP "to port"를 사용합니다. 요청의 "from port"는 요청의 "to port"입니다.

### 공지 URL

announce URL 형식은 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html)에서 명시되지 않았지만, clearnet에서와 같이 UDP announce URL은 `udp://host:port/path` 형태입니다. 경로는 무시되며 비어있을 수 있지만, clearnet에서는 일반적으로 `/announce`입니다. `:port` 부분은 항상 존재해야 하지만, `:port` 부분이 생략된 경우 기본 I2CP 포트인 6969를 사용하는데, 이는 clearnet에서의 일반적인 포트이기 때문입니다. CGI 매개변수 `&a=b&c=d`가 추가될 수도 있으며, 이들은 처리되어 announce 요청에 제공될 수 있습니다. [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)을 참조하세요. 매개변수나 경로가 없는 경우, [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)에 암시된 바와 같이 뒤의 `/`도 생략될 수 있습니다.

### 데이터그램 형식

모든 값은 네트워크 바이트 순서(big endian)로 전송됩니다. 패킷이 정확히 특정 크기일 것으로 기대하지 마십시오. 향후 확장으로 인해 패킷의 크기가 증가할 수 있습니다.

#### 연결 요청

클라이언트에서 tracker로. 16바이트. 응답 가능한 Datagram2여야 함. [BEP 15](http://www.bittorrent.org/beps/bep_0015.html)와 동일. 변경사항 없음.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">protocol_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0x41727101980 // magic constant</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
#### 연결 응답

Tracker에서 클라이언트로. 16 또는 18바이트. 반드시 원시 데이터여야 함. 아래 명시된 부분을 제외하고는 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html)와 동일.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">lifetime</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // Change from BEP 15</td>
    </tr>
  </tbody>
</table>
응답은 요청의 "from port"로 받은 I2CP "to port"로 반드시 전송되어야 합니다.

lifetime 필드는 선택 사항이며 connection_id 클라이언트 수명을 초 단위로 나타냅니다. 기본값은 60이고, 지정된 경우 최소값은 60입니다. 최대값은 65535 또는 약 18시간입니다. tracker는 클라이언트 수명보다 60초 더 오래 connection_id를 유지해야 합니다.

#### 요청 공지

클라이언트에서 트래커로. 최소 98바이트. 응답 가능한 Datagram3이어야 함. 아래에 명시된 사항을 제외하고는 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html)와 동일.

connection_id는 연결 응답에서 수신된 값입니다.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">info_hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">peer_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">56</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">downloaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">left</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">uploaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">80</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">event</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // 0: none; 1: completed; 2: started; 3: stopped</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">84</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">IP address</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // default, unused in I2P</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">88</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">92</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">num_want</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1 // default</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">port</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// must be same as I2CP from port</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">98</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">options</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // As specified in BEP 41</td>
    </tr>
  </tbody>
</table>
[BEP 15](http://www.bittorrent.org/beps/bep_0015.html)에서의 변경사항:

- key는 무시됨
- IP 주소는 사용되지 않음
- port는 아마도 무시되지만 I2CP from port와 동일해야 함
- options 섹션이 있는 경우 [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)에 정의된 대로 사용

응답은 요청의 "from port"로 받은 I2CP "to port"로 반드시 전송되어야 합니다. announce 요청의 포트를 사용하지 마세요.

#### 발표 응답

Tracker에서 클라이언트로. 최소 20바이트. 원시 데이터여야 함. 아래에 명시된 경우를 제외하고는 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html)와 동일함.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">interval</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">leechers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">seeders</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32 * n 32-byte hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">binary hashes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// Change from BEP 15</td>
    </tr>
  </tbody>
</table>
[BEP 15](http://www.bittorrent.org/beps/bep_0015.html)에서의 변경사항:

- 6바이트 IPv4+port 또는 18바이트 IPv6+port 대신, SHA-256 바이너리 peer 해시가 포함된 32바이트의 배수인 "compact responses"를 반환합니다. TCP compact responses와 마찬가지로 port는 포함하지 않습니다.

응답은 요청의 "from port"로 수신된 I2CP "to port"로 전송되어야 합니다. announce 요청의 포트를 사용하지 마세요.

I2P 데이터그램은 약 64KB의 매우 큰 최대 크기를 가지고 있습니다. 하지만 신뢰할 수 있는 전송을 위해서는 4KB보다 큰 데이터그램은 피해야 합니다. 대역폭 효율성을 위해, tracker는 최대 peer 수를 약 50개 정도로 제한해야 하는데, 이는 다양한 계층의 오버헤드를 제외하고 약 1600바이트 패킷에 해당하며, 분할 후 two-tunnel-message 페이로드 한계 내에 있어야 합니다.

BEP 15에서와 같이, 뒤따르는 피어 주소의 수(BEP 15에서는 IP/포트, 여기서는 해시)에 대한 카운트는 포함되지 않습니다. BEP 15에서는 고려되지 않았지만, 피어 정보가 완료되었고 일부 확장 데이터가 뒤따른다는 것을 나타내기 위해 모두 0으로 된 피어 종료 마커를 정의할 수 있습니다.

향후 확장이 가능하도록, 클라이언트는 32바이트 전체가 0인 해시와 그 뒤에 따라오는 모든 데이터를 무시해야 합니다. 트래커는 전체가 0인 해시로부터의 announce를 거부해야 하며, 비록 해당 해시는 이미 Java router에 의해 금지되어 있습니다.

#### 스크래핑

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html)의 스크래핑 요청/응답은 이 사양에서 필수가 아니지만, 원한다면 구현할 수 있으며 변경사항은 필요하지 않습니다. 클라이언트는 먼저 연결 ID를 획득해야 합니다. 스크래핑 요청은 항상 응답 가능한 Datagram3입니다. 스크래핑 응답은 항상 원시(raw) 형태입니다.

#### 오류 응답

Tracker에서 클라이언트로. 최소 8바이트 (메시지가 비어있는 경우). 반드시 raw여야 함. [BEP 15](http://www.bittorrent.org/beps/bep_0015.html)와 동일. 변경사항 없음.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3 // error</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">message</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
## 확장

확장 비트나 버전 필드는 포함되지 않습니다. 클라이언트와 트래커는 패킷이 특정 크기라고 가정해서는 안 됩니다. 이렇게 하면 호환성을 깨뜨리지 않고 추가 필드를 추가할 수 있습니다. 필요한 경우 [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)에 정의된 확장 형식을 사용하는 것이 권장됩니다.

연결 응답이 선택적인 연결 ID 수명을 추가하도록 수정되었습니다.

blinded destination 지원이 필요한 경우, announce 요청 끝에 blinded 35바이트 주소를 추가하거나, [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) 형식을 사용하여 응답에서 blinded 해시를 요청할 수 있습니다(매개변수는 추후 결정). blinded 35바이트 피어 주소 집합은 모든 값이 0인 32바이트 해시 뒤에 announce 응답 끝에 추가될 수 있습니다.

## 구현 가이드라인

비통합형, 비I2CP 클라이언트와 tracker들의 문제점에 대한 논의는 위의 설계 섹션을 참조하십시오.

### 클라이언트

특정 tracker 호스트명에 대해, 클라이언트는 HTTP URL보다 UDP를 선호해야 하며, 둘 다에 announce해서는 안 됩니다.

기존의 BEP 15 지원을 가진 클라이언트는 작은 수정만 필요합니다.

클라이언트가 DHT 또는 기타 datagram 프로토콜을 지원하는 경우, 응답이 해당 포트로 돌아와서 DHT 메시지와 섞이지 않도록 요청 "from port"로 다른 포트를 선택해야 합니다. 클라이언트는 응답으로 원시 datagram만 수신합니다. 트래커는 클라이언트에게 repliable datagram2를 보내지 않습니다.

기본 opentracker 목록을 가진 클라이언트는 알려진 opentracker들이 UDP를 지원하는 것이 확인된 후 UDP URL을 추가하도록 목록을 업데이트해야 합니다.

클라이언트는 요청의 재전송을 구현할 수도 있고 구현하지 않을 수도 있습니다. 재전송이 구현된 경우, 최소 15초의 초기 타임아웃을 사용해야 하며, 각 재전송마다 타임아웃을 두 배로 늘려야 합니다(지수 백오프).

클라이언트는 오류 응답을 받은 후 백오프해야 합니다.

### 트래커

기존 BEP 15 지원을 하는 tracker들은 작은 수정만 필요할 것입니다. 이 명세는 2014년 제안과 다른 점이 있는데, tracker가 동일한 포트에서 repliable datagram2와 datagram3의 수신을 지원해야 한다는 것입니다.

tracker 리소스 요구사항을 최소화하기 위해, 이 프로토콜은 tracker가 나중에 검증을 위해 클라이언트 해시와 연결 ID의 매핑을 저장해야 하는 요구사항을 제거하도록 설계되었습니다. 이는 announce 요청 패킷이 응답 가능한 Datagram3 패킷이므로 발신자의 해시를 포함하기 때문에 가능합니다.

권장되는 구현은 다음과 같습니다:

- 현재 epoch를 연결 수명의 해상도를 가진 현재 시간으로 정의합니다. `epoch = now / lifetime`.
- 8바이트 출력을 생성하는 암호화 해시 함수 `H(secret, clienthash, epoch)`를 정의합니다.
- 모든 연결에 사용되는 랜덤 상수 secret을 생성합니다.
- 연결 응답의 경우, `connection_id = H(secret, clienthash, epoch)`를 생성합니다.
- announce 요청의 경우, `connection_id == H(secret, clienthash, epoch) || connection_id == H(secret, clienthash, epoch - 1)`를 검증하여 현재 epoch에서 수신된 connection ID를 검증합니다.

## 참고 자료

- **[BEP15]** [BEP 15 - UDP Tracker Protocol](http://www.bittorrent.org/beps/bep_0015.html)
- **[BEP41]** [BEP 41 - UDP Tracker Protocol Extensions](http://www.bittorrent.org/beps/bep_0041.html)
- **[DATAGRAMS]** [데이터그램 사양](/docs/specs/datagrams)
- **[Prop160]** [제안 160 - UDP Trackers](/proposals/160-udp-trackers)
- **[Prop163]** [제안 163 - Datagram2/Datagram3](/proposals/163-datagram2-datagram3)
- **[SAMv3]** [SAM v3 API](/docs/api/samv3)
- **[SPEC]** [BitTorrent over I2P](/docs/applications/bittorrent)
