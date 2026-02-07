---
title: "데이터그램 사양"
description: "raw, repliable, authenticated 타입을 포함한 I2P 데이터그램 메시지 형식 사양"
slug: "datagrams"
category: "프로토콜"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

## 개요

Datagrams API의 개요는 [Datagrams API 문서](/docs/api/datagrams/)를 참조하세요.

다음 타입들이 정의되어 있습니다. 표준 프로토콜 번호들이 나열되어 있지만, 스트리밍 프로토콜 번호(6)를 제외하고는 애플리케이션별로 다른 프로토콜 번호들을 사용할 수 있습니다.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Protocol</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Repliable?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Authenticated?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Replay Prevention?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">As Of</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Raw</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
  </tbody>
</table>
다양한 router 및 라이브러리 구현에서 Datagram2와 Datagram3에 대한 지원은 미정입니다. 해당 구현의 문서를 확인하세요.

### 데이터그램 유형 식별

네 가지 datagram 유형은 동일한 위치에 프로토콜 버전이 있는 공통 헤더를 공유하지 않습니다. 패킷은 내용을 기반으로 유형을 식별할 수 없습니다. 동일한 세션에서 여러 유형을 사용하거나 단일 유형을 스트리밍과 함께 사용할 때, 애플리케이션은 프로토콜 번호 및/또는 I2CP/SAM 포트를 사용하여 들어오는 패킷을 올바른 위치로 라우팅해야 합니다. 표준 프로토콜 번호를 사용하면 이 작업이 더 쉬워집니다. datagram 전용 애플리케이션이라도 프로토콜 번호를 설정하지 않는 것(0 또는 PROTO_ANY)은 라우팅 오류 가능성을 높이고 다중 프로토콜 애플리케이션으로의 업그레이드를 어렵게 만들기 때문에 권장되지 않습니다. Datagram 2와 3의 버전 필드는 라우팅 오류와 향후 변경사항에 대한 추가 검사용으로만 제공됩니다.

### 애플리케이션 설계

모든 datagram 사용은 애플리케이션별로 다릅니다.

인증된 데이터그램은 상당한 오버헤드를 가지므로, 일반적인 애플리케이션은 인증된 데이터그램과 인증되지 않은 데이터그램을 모두 사용합니다. 일반적인 설계는 클라이언트에서 서버로 토큰이 포함된 단일 인증된 데이터그램을 보내는 것입니다. 서버는 동일한 토큰이 포함된 인증되지 않은 데이터그램으로 응답합니다. 토큰 타임아웃 전까지의 모든 후속 통신에서는 원시 데이터그램을 사용합니다.

애플리케이션들은 [I2CP](/docs/specs/i2cp/) API 또는 [SAMv3](/docs/api/samv3/)를 통해 프로토콜과 포트 번호를 사용하여 데이터그램을 송수신합니다.

데이터그램은 당연히 신뢰할 수 없습니다. 애플리케이션은 신뢰할 수 없는 전달을 고려하여 설계해야 합니다. I2P 내에서는 NTCP2와 SSU2 전송 방식이 신뢰성을 제공하므로, 다음 홉이 도달 가능한 경우 홉 간 전달은 신뢰할 수 있습니다. 하지만 I2NP 메시지가 큐 제한, 만료, 타임아웃, 대역폭 제한 또는 도달할 수 없는 다음 홉으로 인해 모든 홉에서 삭제될 수 있으므로, 종단 간 전달은 신뢰할 수 없습니다.

### 데이터그램 크기

데이터그램을 포함한 I2NP 메시지의 명목상 크기 제한은 64 KB입니다. Garlic encryption과 tunnel 메시지 오버헤드로 인해 실제 크기는 이보다 다소 줄어듭니다.

그러나 모든 I2NP 메시지는 1KB tunnel 메시지로 분할되어야 합니다. n KB I2NP 메시지의 드롭 확률은 단일 tunnel 메시지의 드롭 확률의 지수 함수인 p ** n입니다. 분할로 인해 tunnel 메시지가 폭증하므로, router 구현의 큐 제한과 능동적 큐 관리(AQM, CoDel 또는 유사한 기술) 때문에 실제 드롭 확률은 지수 함수가 시사하는 것보다 훨씬 높습니다.

신뢰할 수 있는 전송을 보장하기 위한 권장 일반 최대 크기는 몇 KB이며, 최대 10 KB입니다. (전송 계층을 제외한) 모든 프로토콜 계층에서 오버헤드 크기를 신중히 분석하여, 개발자는 하나, 둘 또는 세 개의 tunnel 메시지에 정확히 맞는 최대 페이로드 크기를 설정해야 합니다. 이렇게 하면 효율성과 신뢰성을 극대화할 수 있습니다. 다양한 계층의 오버헤드에는 gzip 헤더, I2NP 헤더, garlic 메시지 헤더, garlic encryption, tunnel 메시지 헤더, tunnel 메시지 단편화 헤더 등이 포함됩니다. 예시는 [Proposal 144](/proposals/144-ecies-x25519-aead-ratchet/)의 스트리밍 MTU 계산과 Java I2P 소스의 ConnectionOptions.java를 참조하세요.

### SAM 고려사항

애플리케이션은 I2CP API 또는 SAM을 통해 프로토콜 및 포트 번호를 사용하여 데이터그램을 송수신합니다. SAM을 통한 프로토콜 및 포트 번호 지정은 SAM v3.2 이상이 필요합니다. 동일한 SAM 세션(tunnel)에서 데이터그램과 스트리밍(UDP 및 TCP)을 모두 사용하려면 SAM v3.3 이상이 필요합니다. 동일한 SAM 세션(tunnel)에서 여러 데이터그램 유형을 사용하려면 SAM v3.3 이상이 필요합니다. SAM v3.3은 현재 Java I2P router에서만 지원됩니다.

다양한 router 및 라이브러리 구현체에서 Datagram2 및 Datagram3에 대한 SAM 지원은 미정입니다. 해당 구현체의 문서를 확인하세요.

일반적인 1500바이트 네트워크 MTU를 초과하는 크기는 애플리케이션과 서버가 별도의 컴퓨터에 있을 경우 SAM 애플리케이션이 SAM 서버로부터/서버로 분할되지 않은 패킷을 전송하는 것을 방해한다는 점에 유의하세요. 일반적으로 이런 경우는 없으며, 둘 다 MTU가 65536 이상인 localhost에 있습니다. SAM 애플리케이션이 서버와 다른 컴퓨터에 분리되어 있을 것으로 예상되는 경우, 응답 가능한 데이터그램의 최대 페이로드는 1KB보다 약간 작습니다.

### PQ 고려사항

Post-Quantum [Proposal 169](/proposals/169-pq-crypto/)의 MLDSA 부분이 구현되면 오버헤드가 상당히 증가할 것입니다. destination + signature의 크기는 391 + 64 = 455바이트에서 MLDSA44의 경우 최소 3739바이트, MLDSA87의 경우 최대 7226바이트로 증가합니다. 이것의 실질적인 영향은 아직 확인되지 않았습니다. router가 제공하는 인증을 사용하는 Datagram3이 해결책이 될 수 있습니다.

## Raw (응답 불가능한) 데이터그램 {#raw}

응답할 수 없는 데이터그램은 'from' 주소가 없으며 인증되지 않습니다. 이들은 "raw" 데이터그램이라고도 불립니다. 엄밀히 말하면, 이들은 전혀 "데이터그램"이 아니며, 단지 원시 데이터입니다. 이들은 datagram API에 의해 처리되지 않습니다. 그러나 SAM과 I2PTunnel 클래스는 "raw datagrams"를 지원합니다.

원시 데이터그램에 대한 표준 I2CP 프로토콜 번호는 PROTO_DATAGRAM_RAW (18)입니다.

형식은 여기에서 지정되지 않으며, 애플리케이션에 의해 정의됩니다. 완전성을 위해 아래에 형식의 그림을 포함합니다.

### 형식

```
+----+----+----+----+----//
| payload...
+----+----+----+----+----//

length: 0 - about 64 KB (see notes)
```
### 참고 사항

실용적인 길이는 다양한 계층에서의 오버헤드와 신뢰성에 의해 제한됩니다.

## Datagram1 (응답 가능) {#repliable}

응답 가능한 데이터그램은 'from' 주소와 서명을 포함합니다. 이는 최소 427바이트의 오버헤드를 추가합니다.

응답 가능한 데이터그램에 대한 표준 I2CP 프로토콜 번호는 PROTO_DATAGRAM (17)입니다.

### 형식

```
+----+----+----+----+----+----+----+----+
| from                                  |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+                                       +
|                                       |
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
| payload...
+----+----+----+----//

from :: a Destination
        length: 387+ bytes
        The originator and signer of the datagram

signature :: a Signature
             Signature type must match the signing public key type of $from
             length: 40+ bytes, as implied by the Signature type.
             For the default DSA_SHA1 key type:
                The DSA Signature of the SHA-256 hash of the payload.
             For other key types:
                The Signature of the payload.
             The signature may be verified by the signing public key of $from

payload :: The data
           Length: 0 to about 63 KB (see notes)

Total length: Payload length + 427+
```
### 참고 사항

- 실제 길이는 다양한 계층의 오버헤드와 신뢰성에 의해 제한됩니다.
- 대용량 datagram의 신뢰성에 대한 중요한 참고사항은 [Datagrams API 문서](/docs/api/datagrams/)를 참조하세요. 최상의 결과를 위해서는 페이로드를 약 10 KB 이하로 제한하세요.
- DSA_SHA1 이외의 타입에 대한 서명은 릴리스 0.9.14에서 재정의되었습니다.
- 이 형식은 LS2에 대한 오프라인 서명 블록 포함을 지원하지 않습니다 (제안서 123). 이를 위해서는 플래그가 있는 새로운 프로토콜이 정의되어야 합니다.

## Datagram2 {#datagram2}

Datagram2 형식은 [Proposal 163](/proposals/163-datagram2/)에 명시된 대로입니다. Datagram2의 I2CP 프로토콜 번호는 19입니다.

Datagram2는 Datagram1을 대체하기 위해 만들어졌습니다. Datagram1에 다음 기능들을 추가합니다:

- 재생 공격 방지
- 오프라인 서명 지원
- 확장성을 위한 플래그 및 옵션 필드

Datagram2의 서명 계산 알고리즘은 Datagram1과 상당히 다르다는 점에 유의하세요.

### 형식

```
+----+----+----+----+----+----+----+----+
|                                       |
~            from                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~     offline_signature (optional)      ~
~   expires, sigtype, pubkey, offsig    ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            signature                  ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

from :: a Destination
        length: 387+ bytes
        The originator and (unless offline signed) signer of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x02 (0 0 1 0)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bit 5: If 0, no offline sig; if 1, offline signed
         Bits 15-6: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

offline_signature ::
             If flag indicates offline keys, the offline signature section,
             as specified in the Common Structures Specification,
             with the following 4 fields. Length: varies by online and offline
             sig types, typically 102 bytes for Ed25519
             This section can, and should, be generated offline.

  expires :: Expires timestamp
             (4 bytes, big endian, seconds since epoch, rolls over in 2106)

  sigtype :: Transient sig type (2 bytes, big endian)

  pubkey :: Transient signing public key (length as implied by sig type),
            typically 32 bytes for Ed25519 sig type.

  offsig :: a Signature
            Signature of expires timestamp, transient sig type,
            and public key, by the destination public key,
            length: 40+ bytes, as implied by the Signature type, typically
            64 bytes for Ed25519 sig type.

payload :: The data
           Length: 0 to about 61 KB (see notes)

signature :: a Signature
             Signature type must match the signing public key type of $from
             (if no offline signature) or the transient sigtype
             (if offline signed)
             length: 40+ bytes, as implied by the Signature type, typically
             64 bytes for Ed25519 sig type.
             The Signature of the payload and other fields as specified below.
             The signature is verified by the signing public key of $from
             (if no offline signature) or the transient pubkey
             (if offline signed)
```
총 길이: 최소 433 + 페이로드 길이; X25519 발신자이고 오프라인 서명이 없는 경우의 일반적인 길이: 457 + 페이로드 길이. 메시지는 일반적으로 I2CP 계층에서 gzip으로 압축되므로, from destination이 압축 가능한 경우 상당한 절약 효과가 있습니다.

참고: 오프라인 서명 형식은 [공통 구조 사양](/docs/specs/common-structures/)과 [스트리밍 사양](/docs/specs/streaming/)에서와 동일합니다.

### 서명

서명은 다음 필드들에 대해 적용됩니다:

- Prelude: 대상 목적지의 32바이트 해시 (데이터그램에 포함되지 않음)
- flags
- options (존재하는 경우)
- offline_signature (존재하는 경우)
- payload

응답 가능한 데이터그램에서 DSA_SHA1 키 타입의 경우, 서명은 페이로드 자체가 아닌 페이로드의 SHA-256 해시에 대한 것이었습니다. 여기서는 키 타입에 관계없이 서명이 항상 위의 필드들에 대한 것입니다(해시가 아님).

### ToHash 검증

수신자는 서명을 검증해야 하며 (목적지 해시 사용), 재전송 공격 방지를 위해 실패 시 데이터그램을 폐기해야 합니다.

## Datagram3 {#datagram3}

Datagram3 형식은 [Proposal 163](/proposals/163-datagram2/)에 명시된 대로입니다. Datagram3의 I2CP 프로토콜 번호는 20입니다.

Datagram3는 raw datagram의 향상된 버전으로 설계되었습니다. raw datagram에 다음과 같은 기능을 추가합니다:

- 복제 가능성
- 확장성을 위한 플래그 및 옵션 필드

Datagram3은 인증되지 않습니다. 향후 제안에서는 router의 ratchet 계층에 의해 인증이 제공될 수 있으며, 인증 상태가 클라이언트에 전달될 것입니다.

### 형식

```
+----+----+----+----+----+----+----+----+
|                                       |
~            fromhash                   ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

fromhash :: a Hash
            length: 32 bytes
            The originator of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x03 (0 0 1 1)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bits 15-5: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

payload :: The data
           Length: 0 to about 61 KB (see notes)
```
전체 길이: 최소 34 + 페이로드 길이.

## 참고 자료

- [Common](/docs/specs/common-structures/) - 공통 구조 사양
- [DATAGRAMS](/docs/api/datagrams/) - Datagrams API 개요
- [I2CP](/docs/specs/i2cp/) - I2CP 사양
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet/) - ECIES-X25519-AEAD-Ratchet 제안
- [Prop163](/proposals/163-datagram2/) - Datagram2 및 Datagram3 제안
- [Prop169](/proposals/169-pq-crypto/) - 포스트 양자 암호화 제안
- [SAMv3](/docs/api/samv3/) - SAM v3 사양
- [Streaming](/docs/specs/streaming/) - 스트리밍 사양
- [TRANSPORT](/docs/overview/transport/) - 전송 개요
- [TUNMSG](/docs/specs/tunnel-message/#notes) - Tunnel 메시지 사양
