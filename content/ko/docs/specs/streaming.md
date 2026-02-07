---
title: "스트리밍 프로토콜 명세서"
description: "TCP와 유사한 신뢰할 수 있는 전송을 제공하는 I2P streaming protocol 명세"
slug: "streaming"
category: "프로토콜"
lastUpdated: "2023-10"
accurateFor: "0.9.59"
---

## 개요

Streaming 프로토콜에 대한 개요는 [Streaming Library](/docs/api/streaming)를 참조하세요.

## 프로토콜 버전

스트리밍 프로토콜에는 버전 필드가 포함되어 있지 않습니다. 아래 나열된 버전들은 Java I2P용입니다. 구현 및 실제 암호화 지원은 다를 수 있습니다. 원격 끝점이 특정 버전이나 기능을 지원하는지 확인할 방법은 없습니다. 아래 표는 다양한 기능의 릴리스 날짜에 대한 일반적인 안내를 위한 것입니다.

아래 나열된 기능들은 프로토콜 자체에 대한 것입니다. 다양한 구성 옵션들은 해당 기능들이 구현된 Java I2P 버전과 함께 [Streaming Library](/docs/api/streaming)에 문서화되어 있습니다.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Router Version</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Streaming Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Bob's hash in NACKs field of SYN packet</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE option</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">I2CP protocol number enforced</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED no longer required in RESET</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PINGs and PONGs may include a payload</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA Ed25519 sig type</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA P-256, P-384, and P-521 sig types</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Variable-length signatures</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.7.1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Protocol numbers defined in I2CP</td>
    </tr>
  </tbody>
</table>
## 프로토콜 사양

### 패킷 형식

스트리밍 프로토콜에서 단일 패킷의 형식은 아래와 같습니다. NACK나 옵션 데이터 없이 최소 헤더 크기는 22바이트입니다.

스트리밍 프로토콜에는 길이 필드가 없습니다. 프레이밍은 하위 레이어인 I2CP와 I2NP에서 제공됩니다.

```
+----+----+----+----+----+----+----+----+
| send Stream ID    | rcv Stream ID     |
+----+----+----+----+----+----+----+----+
| sequence  Num     | ack Through       |
+----+----+----+----+----+----+----+----+
| nc |  nc*4 bytes of NACKs (optional)
+----+----+----+----+----+----+----+----+
     | rd |  flags  | opt size| opt data
+----+----+----+----+----+----+----+----+
   ...  (optional, see below)           |
+----+----+----+----+----+----+----+----+
|   payload ...
+----+----+----+-//
```
**sendStreamId** :: 4바이트 [Integer](/docs/specs/common-structures#integer) : 첫 번째 SYN 응답 패킷을 보내기 전에 패킷 수신자가 선택한 임의의 숫자로, 연결 수명 동안 상수이며 0보다 큰 값입니다. 연결 시작자가 보낸 SYN 메시지에서는 0이며, 상대방의 stream ID가 포함된 SYN 응답을 받을 때까지 후속 메시지에서도 0입니다.

**receiveStreamId** :: 4 바이트 [Integer](/docs/specs/common-structures#integer) : 첫 번째 SYN 패킷을 보내기 전에 패킷 발신자가 선택한 난수이며 연결이 지속되는 동안 일정하고, 0보다 큰 값. RESET 패킷과 같이 알 수 없는 경우에는 0일 수 있음.

**sequenceNum** :: 4 byte [Integer](/docs/specs/common-structures#integer) : 이 메시지의 시퀀스 번호로, SYN 메시지에서 0부터 시작하며, 일반 ACK와 재전송을 제외한 각 메시지에서 1씩 증가합니다. sequenceNum이 0이고 SYN 플래그가 설정되지 않은 경우, 이는 ACK를 받을 필요가 없는 일반 ACK 패킷입니다.

**ackThrough** :: 4 바이트 [Integer](/docs/specs/common-structures#integer) : receiveStreamId에서 수신된 가장 높은 패킷 시퀀스 번호입니다. 이 필드는 초기 연결 패킷(receiveStreamId가 알 수 없는 ID인 경우) 또는 NO_ACK 플래그가 설정된 경우 무시됩니다. 이 시퀀스 번호까지의 모든 패킷(포함)이 ACK됩니다. 단, 아래 NACK에 나열된 패킷들은 예외입니다.

**NACK count** :: 1바이트 [Integer](/docs/specs/common-structures#integer) : 다음 필드에 있는 4바이트 NACK의 개수, 또는 0.9.58부터 재생 방지를 위해 SYNCHRONIZE와 함께 사용될 때는 8; 아래 참조.

**NACKs** :: nc * 4바이트 [Integer](/docs/specs/common-structures#integer) : ackThrough보다 작지만 아직 수신되지 않은 시퀀스 번호들. 패킷에 대한 두 번의 NACK는 해당 패킷의 '빠른 재전송' 요청입니다. 또한 0.9.58부터 SYNCHRONIZE와 함께 재생 공격 방지를 위해 사용됩니다. 아래 참조.

**resendDelay** :: 1 byte [Integer](/docs/specs/common-structures#integer) : 이 패킷의 생성자가 이 패킷을 재전송하기 전에 기다릴 시간 (아직 ACK되지 않은 경우). 값은 패킷이 생성된 이후의 초 단위입니다. 현재 수신 시 무시됩니다.

**flags** :: 2바이트 값 : 아래 참조.

**option size** :: 2 바이트 [Integer](/docs/specs/common-structures#integer) : 다음 필드의 바이트 수

**option data** :: 0바이트 이상 : 플래그에 의해 지정됨. 아래 참조.

**payload** :: 남은 패킷 크기

### 플래그 및 옵션 데이터 필드

위의 플래그 필드는 패킷에 대한 일부 메타데이터를 지정하며, 이에 따라 특정 추가 데이터가 포함되어야 할 수 있습니다. 플래그는 다음과 같습니다. 지정된 모든 데이터 구조는 주어진 순서대로 옵션 영역에 추가되어야 합니다.

비트 순서: 15....0 (15는 MSB)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Flag</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Order</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SYNCHRONIZE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP SYN. Set in the initial packet and in the first response. FROM_INCLUDED and SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">CLOSE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP FIN. If the response to a SYNCHRONIZE fits in a single message, the response will contain both SYNCHRONIZE and CLOSE. SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RESET</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Abnormal close. SIGNATURE_INCLUDED must also be set. Prior to release 0.9.20, due to a bug, FROM_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#signature">Signature</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, CLOSE, and RESET, where it is required, and with ECHO, where it is required for a ping. The signature uses the Destination's <a href="/docs/specs/common-structures#signingprivatekey">SigningPrivateKey</a> to sign the entire header and payload with the space in the option data field for the signature being set to all zeroes. Prior to release 0.9.11, the signature was always 40 bytes. As of release 0.9.11, the signature may be variable-length, see below for details.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused. Requests every packet in the other direction to have SIGNATURE_INCLUDED</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">387+ byte <a href="/docs/specs/common-structures#destination">Destination</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, where it is required, and with ECHO, where it is required for a ping. Prior to release 0.9.20, due to a bug, must also be sent with RESET.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DELAY_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Optional delay. How many milliseconds the sender of this packet wants the recipient to wait before sending any more data. A value greater than 60000 indicates choking. A value of 0 requests an immediate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MAX_PACKET_SIZE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum length of the payload. Send with SYNCHRONIZE.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PROFILE_INTERACTIVE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused or ignored; the interactive profile is unimplemented.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECHO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused except by ping programs. If set, most other options are ignored. See the <a href="/docs/api/streaming">streaming docs</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">NO_ACK</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">This flag simply tells the recipient to ignore the ackThrough field in the header. Currently set in the initial SYN packet, otherwise the ackThrough field is always valid. Note that this does not save any space, the ackThrough field is before the flags and is always present.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#offlinesignature">OfflineSig</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Contains the offline signature section from LS2. See proposal 123 and the common structures specification. FROM_INCLUDED must also be set. Contains an OfflineSig: 1) Expires timestamp (4 bytes, seconds since epoch, rolls over in 2106) 2) Transient sig type (2 bytes) 3) Transient <a href="/docs/specs/common-structures#signingpublickey">SigningPublicKey</a> (length as implied by sig type) 4) <a href="/docs/specs/common-structures#signature">Signature</a> of expires timestamp, transient sig type, and public key, by the destination public key. Length of sig as implied by the destination public key sig type.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12-15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">unused</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Set to zero for compatibility with future uses.</td>
    </tr>
  </tbody>
</table>
### 가변 길이 서명 참고사항

릴리스 0.9.11 이전에는 옵션 필드의 서명이 항상 40바이트였습니다.

릴리스 0.9.11부터 signature는 가변 길이입니다. Signature 타입과 길이는 FROM_INCLUDED 옵션에서 사용된 키 타입과 [Signature](/docs/specs/common-structures#signature) 문서로부터 추론됩니다.

릴리스 0.9.39부터 OFFLINE_SIGNATURE 옵션이 지원됩니다. 이 옵션이 있으면 임시 [SigningPublicKey](/docs/specs/common-structures#signingpublickey)가 서명된 패킷을 검증하는 데 사용되며, 서명 길이와 유형은 옵션의 임시 SigningPublicKey에서 추론됩니다.

- 패킷이 FROM_INCLUDED와 SIGNATURE_INCLUDED를 모두 포함하는 경우 (SYNCHRONIZE에서처럼), 추론을 직접적으로 수행할 수 있습니다.

- 패킷에 FROM_INCLUDED가 포함되어 있지 않을 때, 이전 SYNCHRONIZE 패킷으로부터 추론해야 합니다.

- 패킷이 FROM_INCLUDED를 포함하지 않고, 이전 SYNCHRONIZE 패킷이 없었던 경우(예: 떠돌아다니는 CLOSE 또는 RESET 패킷), 남은 옵션의 길이로부터 추론할 수 있습니다(SIGNATURE_INCLUDED가 마지막 옵션이므로). 하지만 서명을 검증할 FROM이 없기 때문에 패킷은 아마 폐기될 것입니다. 향후 더 많은 옵션 필드가 정의되면 이를 고려해야 합니다.

### 재생 공격 방지

Bob이 Alice로부터 받은 유효한 서명된 SYNCHRONIZE 패킷을 저장해두고 나중에 피해자 Charlie에게 보내는 재전송 공격을 사용하는 것을 방지하기 위해, Alice는 다음과 같이 SYNCHRONIZE 패킷에 Bob의 목적지 해시를 포함해야 합니다:

```
Set NACK count field to 8
Set the NACKs field to Bob's 32-byte destination hash
```
SYNCHRONIZE를 수신하면, NACK 카운트 필드가 8인 경우, Bob은 NACKs 필드를 32바이트 destination 해시로 해석해야 하며, 이것이 자신의 destination 해시와 일치하는지 확인해야 합니다. 또한 평소와 같이 패킷의 서명을 검증해야 하는데, 이는 NACK 카운트와 NACKs 필드를 포함한 전체 패킷을 포괄합니다. NACK 카운트가 8이고 NACKs 필드가 일치하지 않으면, Bob은 패킷을 폐기해야 합니다.

이는 버전 0.9.58 이상에서 필수입니다. SYNCHRONIZE 패킷에서는 NACK가 예상되지 않기 때문에 이전 버전과 역호환됩니다. Destination은 상대방이 실행 중인 버전을 알 수 없고 알 수도 없습니다.

Bob에서 Alice로 전송되는 SYNCHRONIZE ACK 패킷에는 변경이 필요하지 않습니다. 해당 패킷에 NACK을 포함하지 마십시오.

## 참고 자료

- **[Destination]** [Destination](/docs/specs/common-structures#destination)
- **[Integer]** [Integer](/docs/specs/common-structures#integer)
- **[OfflineSig]** [OfflineSignature](/docs/specs/common-structures#offlinesignature)
- **[Signature]** [Signature](/docs/specs/common-structures#signature)
- **[SigningPrivateKey]** [SigningPrivateKey](/docs/specs/common-structures#signingprivatekey)
- **[SigningPublicKey]** [SigningPublicKey](/docs/specs/common-structures#signingpublickey)
- **[STREAMING]** [Streaming 라이브러리](/docs/api/streaming)
