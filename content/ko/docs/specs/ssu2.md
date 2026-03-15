---
title: "SSU2 사양"
description: "보안 준신뢰성 UDP 전송 프로토콜 버전 2"
slug: "ssu2"
category: "전송 계층"
lastUpdated: "2026-03"
accurateFor: "0.9.69"
---

## 상태

실질적으로 완료되었습니다. 보안 분석, 위협 모델, SSU 1 보안 및 문제점 검토, QUIC 사양 발췌를 포함한 추가 배경 및 목표에 대해서는 [Prop159](/proposals/159-ssu2)를 참조하십시오.

출시 계획:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Feature</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Testing (not default)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Enabled by default</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Local test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-03</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test in-net</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze basic protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Basic Session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address Validation (Retry)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Fragmented RI in handshake</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze extended protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Enable for random 2%</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Validation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Connection Migration</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Immediate ACK flag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Key Rotation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2023-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (i2pd)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (Java I2P)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.61 2023-12</td></tr>
  </tbody>
</table>
기본 세션은 핸드셰이크와 데이터 단계를 포함합니다. 확장 프로토콜은 릴레이와 피어 테스트를 포함합니다.

## 개요

이 사양은 [SSU](/docs/transport/ssu)가 다양한 형태의 자동화된 식별 및 공격에 대한 저항성을 개선하기 위한 인증된 키 합의 프로토콜을 정의합니다.

다른 I2P transport와 마찬가지로 SSU2는 I2NP 메시지의 지점 간 (router-to-router) 전송을 위해 정의됩니다. 이것은 범용 데이터 파이프가 아닙니다. [SSU](/docs/transport/ssu)와 마찬가지로 두 가지 추가 서비스를 제공합니다: NAT 통과를 위한 릴레이와 인바운드 접근 가능성 판단을 위한 피어 테스팅입니다. 또한 SSU에는 없는 세 번째 서비스로, 피어가 IP나 포트를 변경할 때 연결 마이그레이션 기능을 제공합니다.

## 설계 개요

### 요약

우리는 영감, 지침, 그리고 코드 재사용을 위해 I2P 내부와 외부 표준의 여러 기존 프로토콜에 의존합니다:

- 위협 모델: NTCP2 [NTCP2](/docs/specs/ntcp2)에서 가져온 것으로, QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001)에서 분석된 UDP 전송과 관련된 중요한 추가 위협을 포함합니다.
- 암호화 선택: [NTCP2](/docs/specs/ntcp2)에서 가져왔습니다.
- 핸드셰이크: [NTCP2](/docs/specs/ntcp2)와 [NOISE](https://noiseprotocol.org/noise.html)의 Noise XK입니다. UDP가 제공하는 캡슐화(고유한 메시지 경계)로 인해 NTCP2에 대한 상당한 단순화가 가능합니다.
- 핸드셰이크 임시 키 난독화: [NTCP2](/docs/specs/ntcp2)에서 적응되었지만 AES 대신 [ECIES](/docs/specs/ecies)의 ChaCha20을 사용합니다.
- 패킷 헤더: WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf)와 QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001)에서 적응되었습니다.
- 패킷 헤더 난독화: [NTCP2](/docs/specs/ntcp2)에서 적응되었지만 AES 대신 [ECIES](/docs/specs/ecies)의 ChaCha20을 사용합니다.
- 패킷 헤더 보호: QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001)와 [Nonces](https://eprint.iacr.org/2019/624.pdf)에서 적응되었습니다.
- [ECIES](/docs/specs/ecies)에서와 같이 AEAD 연관 데이터로 사용되는 헤더입니다.
- 패킷 번호 매기기: WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf)와 QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001)에서 적응되었습니다.
- 메시지: [SSU](/docs/transport/ssu)에서 적응되었습니다.
- I2NP 단편화: [SSU](/docs/transport/ssu)에서 적응되었습니다.
- 릴레이 및 피어 테스팅: [SSU](/docs/transport/ssu)에서 적응되었습니다.
- 릴레이 및 피어 테스트 데이터의 서명: 공통 구조 사양 [Common](/docs/specs/common-structures)에서 가져왔습니다.
- 블록 형식: [NTCP2](/docs/specs/ntcp2)와 [ECIES](/docs/specs/ecies)에서 가져왔습니다.
- 패딩 및 옵션: [NTCP2](/docs/specs/ntcp2)와 [ECIES](/docs/specs/ecies)에서 가져왔습니다.
- Acks, nacks: QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000)에서 적응되었습니다.
- 흐름 제어: 미정

I2P에서 이전에 사용되지 않은 새로운 암호화 프리미티브는 없습니다.

### 전송 보장

다른 I2P transport인 NTCP, NTCP2, SSU 1과 마찬가지로, 이 transport는 순서가 보장된 바이트 스트림 전달을 위한 범용 기능이 아닙니다. I2NP 메시지 전송을 위해 설계되었습니다. "스트림" 추상화는 제공되지 않습니다.

또한 SSU의 경우, 피어가 지원하는 NAT 통과 및 도달 가능성(인바운드 연결) 테스트를 위한 추가 기능을 포함하고 있습니다.

SSU 1의 경우, I2NP 메시지의 순차적 전달을 제공하지 않습니다. 또한 I2NP 메시지의 전달 보장도 제공하지 않습니다. 효율성을 위해, 또는 UDP 데이터그램의 순서가 바뀌어 전달되거나 데이터그램이 손실되기 때문에, I2NP 메시지는 원격 끝단에 순서가 바뀌어 전달되거나 아예 전달되지 않을 수 있습니다. I2NP 메시지는 필요시 여러 번 재전송될 수 있지만, 전체 연결이 끊어지지 않더라도 최종적으로 전달이 실패할 수 있습니다. 또한, 다른 I2NP 메시지들에 대해 재전송(손실 복구)이 발생하고 있는 동안에도 새로운 I2NP 메시지들이 계속 전송될 수 있습니다.

이 프로토콜은 I2NP 메시지의 중복 전송을 완전히 방지하지 않습니다. router는 I2NP 만료를 강제하고 I2NP 메시지 ID를 기반으로 블룸 필터 또는 기타 메커니즘을 사용해야 합니다. 아래 I2NP 메시지 중복 섹션을 참조하세요.

### Noise Protocol Framework

이 명세서는 Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (개정판 33, 2017-10-04)를 기반으로 한 요구사항을 제공합니다. Noise는 [SSU](/docs/transport/ssu) 프로토콜의 기반이 되는 Station-To-Station 프로토콜 [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol)와 유사한 특성을 가지고 있습니다. Noise 용어에서 Alice는 개시자(initiator)이고, Bob은 응답자(responder)입니다.

SSU2는 Noise 프로토콜 Noise_XK_25519_ChaChaPoly_SHA256을 기반으로 합니다. (초기 키 유도 함수의 실제 식별자는 I2P 확장을 나타내기 위해 "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256"입니다 - 아래 KDF 1 섹션 참조)

참고: 이 식별자는 NTCP2에서 사용되는 것과 다릅니다. 세 개의 핸드셰이크 메시지 모두 헤더를 연관 데이터로 사용하기 때문입니다.

이 Noise 프로토콜은 다음과 같은 기본 요소들을 사용합니다:

- Handshake Pattern: XK Alice가 자신의 키를 Bob에게 전송 (X) Alice는 이미 Bob의 정적 키를 알고 있음 (K)
- DH Function: X25519 [RFC-7748](https://tools.ietf.org/html/rfc7748)에 명시된 32바이트 키 길이를 가진 X25519 DH.
- Cipher Function: ChaChaPoly [RFC-7539](https://tools.ietf.org/html/rfc7539) 섹션 2.8에 명시된 AEAD_CHACHA20_POLY1305. 12바이트 nonce, 처음 4바이트는 0으로 설정.
- Hash Function: SHA256 I2P에서 이미 광범위하게 사용되는 표준 32바이트 해시.

### 프레임워크에 대한 추가 사항

이 명세서는 Noise_XK_25519_ChaChaPoly_SHA256에 대한 다음과 같은 향상 사항들을 정의합니다. 이들은 일반적으로 [NOISE](https://noiseprotocol.org/noise.html) 섹션 13의 가이드라인을 따릅니다.

1) 핸드셰이크 메시지(Session Request, Created, Confirmed)는 16바이트 또는 32바이트 헤더를 포함합니다. 2) 핸드셰이크 메시지(Session Request, Created, Confirmed)의 헤더는 암호화/복호화 전에 mixHash()의 입력으로 사용되어 헤더를 메시지에 바인딩합니다. 3) 헤더는 암호화되고 보호됩니다. 4) 평문 임시 키는 알려진 키와 IV를 사용하는 ChaCha20 암호화로 난독화됩니다. 이는 elligator2보다 더 빠릅니다. 5) 페이로드 형식은 메시지 1, 2 및 데이터 단계에 대해 정의됩니다. 물론 이는 Noise에서 정의되지 않습니다.

데이터 단계는 Noise 데이터 단계와 유사하지만 호환되지 않는 암호화를 사용합니다.

### 세션 구성

사용된 암호학적 구성 요소들에 해당하는 다음 함수들을 정의합니다.

#### 긴 헤더

ZEROLEN

#### 짧은 헤더

:   길이가 0인 바이트 배열

#### 연결 ID 번호 매기기

H(p, d)

#### 패킷 번호 매기기

:   개인화 문자열 p와 데이터 d를 입력받아 32바이트 길이의 출력을 생성하는 SHA-256 해시 함수입니다. [NOISE](https://noiseprotocol.org/noise.html)에서 정의된 대로입니다. 아래 ||는 추가를 의미합니다.

## 정의

MixHash(d)

:   이전 해시 h와 새로운 데이터 d를 입력받아 32바이트 길이의 출력을 생성하는 SHA-256 해시 함수입니다. 아래의 ||는 추가(append)를 의미합니다.

STREAM

:   [RFC-7539](https://tools.ietf.org/html/rfc7539)에서 명시된 ChaCha20/Poly1305 AEAD. S_KEY_LEN = 32이고 S_IV_LEN = 12.

DH

    Use SHA-256 as follows:

        H(p, d) := SHA-256(p || d)

:   X25519 공개 키 합의 시스템. 32바이트의 개인 키, 32바이트의 공개 키, 32바이트의 출력을 생성합니다. 다음과 같은 기능이 있습니다:

HKDF(salt, ikm, info, n)

    Use SHA-256 as follows:

        MixHash(d) := h = SHA-256(h || d)

:   입력 키 자료 ikm(좋은 엔트로피를 가져야 하지만 균등하게 무작위인 문자열일 필요는 없음), 32바이트 길이의 솔트, 그리고 컨텍스트별 'info' 값을 받아서 키 자료로 사용하기에 적합한 n바이트의 출력을 생성하는 암호학적 키 도출 함수입니다.

MixKey(d)

    ENCRYPT(k, n, plaintext, ad)

    :   Encrypts plaintext using the cipher key k, and nonce n which MUST be unique for the key k. Associated data ad is optional. Returns a ciphertext that is the size of the plaintext + 16 bytes for the HMAC.

        The entire ciphertext must be indistinguishable from random if the key is secret.

    DECRYPT(k, n, ciphertext, ad)

    :   Decrypts ciphertext using the cipher key k, and nonce n. Associated data ad is optional. Returns the plaintext.

:   이전 chainKey와 새로운 데이터 d로 HKDF()를 사용하고, 새로운 chainKey와 k를 설정합니다. [NOISE](https://noiseprotocol.org/noise.html)에서 정의된 대로입니다.

각 UDP datagram은 정확히 하나의 메시지를 포함합니다. datagram의 길이(IP 및 UDP 헤더 이후)는 메시지의 길이입니다. 패딩이 있는 경우, 메시지 내부의 패딩 블록에 포함됩니다. 이 문서에서는 "datagram"과 "packet"이라는 용어를 대부분 상호 교환적으로 사용합니다. 각 datagram(또는 packet)은 단일 메시지를 포함합니다(하나의 datagram이 여러 QUIC packet을 포함할 수 있는 QUIC와는 다름). "packet header"는 IP/UDP 헤더 이후 부분입니다.

    GENERATE_PRIVATE()

    :   Generates a new private key.

    DERIVE_PUBLIC(privkey)

    :   Returns the public key corresponding to the given private key.

    DH(privkey, pubkey)

    :   Generates a shared secret from the given private and public keys.

예외: Session Confirmed 메시지는 여러 패킷에 걸쳐 분할될 수 있다는 점에서 고유합니다. 자세한 정보는 아래의 Session Confirmed 분할 섹션을 참조하세요.

모든 SSU2 메시지는 최소 40바이트 길이입니다. 1-39바이트 길이의 메시지는 유효하지 않습니다. 모든 SSU2 메시지는 1472바이트(IPv4) 또는 1452바이트(IPv6) 이하의 길이입니다. 메시지 형식은 Noise 메시지를 기반으로 하되, 프레이밍과 구별 불가능성을 위한 수정 사항이 있습니다. 표준 Noise 라이브러리를 사용하는 구현체는 수신된 메시지를 표준 Noise 메시지 형식으로 전처리해야 합니다. 모든 암호화된 필드는 AEAD 암호문입니다.

    Use HKDF as specified in [RFC-5869](https://tools.ietf.org/html/rfc5869), using the HMAC hash function SHA-256 as specified in [RFC-2104](https://tools.ietf.org/html/rfc2104). This means that SALT_LEN is 32 bytes max.

다음 메시지들이 정의되어 있습니다:

Alice가 이전에 Bob으로부터 받은 유효한 토큰을 가지고 있을 때의 표준 연결 설정 순서는 다음과 같습니다:

    Use HKDF as follows:

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]

## 메시지

Alice가 유효한 토큰을 가지고 있지 않은 경우, 설정 순서는 다음과 같습니다:

Alice가 유효한 토큰을 가지고 있다고 생각하지만 Bob이 이를 거부하는 경우(아마도 Bob이 재시작했기 때문에), 설정 순서는 다음과 같습니다:

Bob은 이유 코드가 포함된 Termination 블록을 담은 Retry 메시지로 응답하여 Session 또는 Token Request를 거부할 수 있습니다. 이유 코드에 따라 Alice는 일정 시간 동안 다른 요청을 시도하지 않아야 합니다:

Noise 용어를 사용하면, 연결 설정 및 데이터 시퀀스는 다음과 같습니다: (페이로드 보안 속성)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Encr. Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionRequest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionCreated</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionConfirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">PeerTest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">HolePunch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
  </tbody>
</table>
### 패킷 헤더

세션이 설정되면 Alice와 Bob은 Data 메시지를 교환할 수 있습니다.

```
Alice                           Bob

SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
모든 패킷은 난독화된(암호화된) 헤더로 시작합니다. 헤더 타입에는 긴 헤더와 짧은 헤더 두 가지가 있습니다. 처음 13바이트(Destination Connection ID, 패킷 번호, 타입)는 모든 헤더에서 동일합니다.

```
Alice                           Bob

TokenRequest --------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
긴 헤더는 32바이트입니다. 세션이 생성되기 전에 Token Request, SessionRequest, SessionCreated, Retry에 사용됩니다. 또한 세션 외부의 Peer Test 및 Hole Punch 메시지에도 사용됩니다.

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
헤더 암호화 이전:

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry containing a Termination block

or

TokenRequest --------------------->
<---------------------------  Retry containing a Termination block
```
짧은 헤더는 16바이트입니다. Session Created 메시지와 Data 메시지에 사용됩니다. Session Request, Retry, Peer Test와 같은 인증되지 않은 메시지는 항상 긴 헤더를 사용합니다.

```
XK(s, rs):           Authentication   Confidentiality
  <- s
  ...
  -> e, es                  0                2
  <- e, ee                  2                1
  -> s, se                  2                5
  <-                        2                5
```
16바이트가 필요한 이유는 수신자가 메시지 유형을 얻기 위해 처음 16바이트를 복호화해야 하고, 메시지 유형에서 나타내는 바와 같이 실제로 긴 헤더인 경우 추가로 16바이트를 더 복호화해야 하기 때문입니다.

### 패킷 무결성

Session Confirmed의 경우, 헤더 암호화 이전:

#### 헤더 바인딩

frag 필드에 대한 자세한 정보는 아래의 세션 확인된 단편화 섹션을 참조하세요.

Data 메시지의 경우, 헤더 암호화 이전에:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 0, 1, 7, 9, 10, or 11

ver :: The protocol version, equal to 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: 8 bytes, unsigned big endian integer

Token :: 8 bytes, unsigned big endian integer
```
#### 헤더 암호화

Connection ID는 무작위로 생성되어야 합니다. Source와 Destination ID는 동일하면 안 되며, 이는 경로상의 공격자가 패킷을 캡처하여 유효해 보이는 패킷을 발신자에게 다시 보낼 수 없도록 하기 위함입니다. Connection ID 생성에 카운터를 사용하지 마십시오. 경로상의 공격자가 유효해 보이는 패킷을 생성할 수 없도록 하기 위함입니다.

QUIC와 달리, 우리는 핸드셰이크 중이나 후에, 심지어 Retry 메시지 후에도 connection ID를 변경하지 않습니다. ID는 첫 번째 메시지(Token Request 또는 Session Request)부터 마지막 메시지(Termination이 포함된 Data)까지 일정하게 유지됩니다. 또한 connection ID는 path challenge나 connection migration 중이나 후에도 변경되지 않습니다.

또한 QUIC과 다른 점은 헤더의 연결 ID가 항상 헤더 암호화되어 있다는 것입니다. 아래를 참조하세요.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, all zeros

type :: The message type = 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility
```
핸드셰이크에서 First Packet Number 블록이 전송되지 않으면, 패킷은 각 방향에 대해 단일 세션 내에서 0부터 시작하여 최대 (2**32 -1)까지 번호가 매겨집니다. 최대 패킷 수가 전송되기 훨씬 전에 세션을 종료하고 새 세션을 생성해야 합니다.

First Packet Number 블록이 핸드셰이크에서 전송되면, 패킷들은 해당 방향에 대해 단일 세션 내에서 그 패킷 번호부터 시작하여 번호가 매겨집니다. 패킷 번호는 세션 중에 순환할 수 있습니다. 최대 2**32개의 패킷이 전송되어 패킷 번호가 첫 번째 패킷 번호로 되돌아가면, 해당 세션은 더 이상 유효하지 않습니다. 최대 패킷 수가 전송되기 훨씬 전에 세션을 종료하고 새 세션을 생성해야 합니다.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|flag|moreflags|
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 6

flag :: 1 byte flags:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-1: unused, set to 0 for future compatibility
       bits 0: when set to 1, immediate ack requested

moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### 헤더 암호화 KDF

TODO 키 로테이션, 최대 패킷 번호 줄이기?

손실된 것으로 판단되는 핸드셰이크 패킷은 패킷 번호를 포함한 동일한 헤더와 함께 전체가 재전송됩니다. 핸드셰이크 메시지인 Session Request, Session Created, Session Confirmed는 동일한 패킷 번호와 동일한 암호화된 내용으로 재전송되어야 하며, 이는 응답을 암호화하는 데 동일한 연쇄 해시가 사용되도록 하기 위함입니다. Retry 메시지는 전송되지 않습니다.

손실된 것으로 판단되는 데이터 단계 패킷은 전체적으로 재전송되지 않습니다(종료 제외, 아래 참조). 손실된 패킷에 포함된 블록에도 동일하게 적용됩니다. 대신, 블록에 포함될 수 있는 정보는 필요에 따라 새로운 패킷으로 다시 전송됩니다. 데이터 패킷은 동일한 패킷 번호로 재전송되지 않습니다. 패킷 내용의 재전송(내용이 동일하게 유지되는지 여부와 관계없이)은 반드시 다음 사용되지 않은 패킷 번호를 사용해야 합니다.

#### 헤더 검증

동일한 패킷 번호로 변경되지 않은 전체 패킷을 그대로 재전송하는 것은 여러 이유로 허용되지 않습니다. 배경 정보는 QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) 섹션 12.3을 참조하세요.

새로운 패킷은 손실된 것으로 판단된 정보를 전송하는 데 사용됩니다. 일반적으로 해당 정보가 포함된 패킷이 손실된 것으로 판단되면 정보가 다시 전송되고, 해당 정보가 포함된 패킷이 확인응답되면 전송이 중단됩니다.

예외: Termination 블록을 포함하는 데이터 단계 패킷은 전체를 그대로 재전송할 수 있지만 필수는 아닙니다. 아래의 세션 종료 섹션을 참조하십시오.

다음 패킷들은 무시되는 임의의 패킷 번호를 포함합니다:

Alice의 경우, 아웃바운드 패킷 번호는 Session Confirmed부터 0으로 시작됩니다. Bob의 경우, 아웃바운드 패킷 번호는 첫 번째 Data 패킷부터 0으로 시작되며, 이는 Session Confirmed의 ACK여야 합니다. 표준 핸드셰이크 예시에서 패킷 번호는 다음과 같습니다:

handshake 메시지(SessionRequest, SessionCreated 또는 SessionConfirmed)를 재전송할 때는 동일한 패킷 번호로 변경 없이 재전송해야 합니다. 이러한 메시지를 재전송할 때 다른 임시 키를 사용하거나 페이로드를 변경하지 마십시오.

- 재전송을 위해 패킷을 저장하는 것은 비효율적입니다
- 새로운 패킷 데이터는 경로상의 관찰자에게 다르게 보이므로, 재전송된 것인지 알 수 없습니다
- 새로운 패킷에는 이전 ack 블록이 아닌 업데이트된 ack 블록이 함께 전송됩니다
- 필요한 것만 재전송합니다. 일부 프래그먼트는 이미 한 번 재전송되어 ack를 받았을 수 있습니다
- 더 많은 데이터가 대기 중이라면 각 재전송 패킷에 필요한 만큼 담을 수 있습니다
- 중복 탐지 목적으로 모든 개별 패킷을 추적하는 엔드포인트는 과도한 상태 정보를 축적할 위험이 있습니다. 중복 탐지에 필요한 데이터는 최소 패킷 번호를 유지하여 해당 번호 미만의 모든 패킷을 즉시 삭제함으로써 제한할 수 있습니다.
- 이 방식은 훨씬 더 유연합니다

헤더(난독화 및 보호 이전의)는 헤더를 데이터에 암호학적으로 바인딩하기 위해 AEAD 함수의 연관 데이터에 항상 포함됩니다.

헤더 암호화는 여러 목표를 가지고 있습니다. 배경과 가정은 위의 "추가 DPI 논의" 섹션을 참조하십시오.

헤더는 네트워크 데이터베이스에 게시된 알려진 키나 나중에 계산된 키로 암호화됩니다. 핸드셰이크 단계에서는 키가 공개되어 있고 키와 논스가 재사용되므로 DPI 저항용으로만 사용되며, 실제로는 단순한 난독화에 불과합니다. 헤더 암호화는 임시 키 X(Session Request에서)와 Y(Session Created에서)를 난독화하는 데도 사용됩니다.

- Session Request
- Session Created
- Token Request
- Retry
- Peer Test
- Hole Punch

추가 지침은 아래의 인바운드 패킷 처리 섹션을 참조하세요.

```
Alice                           Bob

SessionRequest (r)    ------------>
<-------------   SessionCreated (r)
SessionConfirmed (0)  ------------>
<-------------             Data (0) (Ack-only)
Data (1)              ------------> (May be sent before Ack is received)
<-------------             Data (1)
Data (2)              ------------>
Data (3)              ------------>
Data (4)              ------------>
<-------------             Data (2)

r = random packet number (ignored)
Token Request, Retry, and Peer Test
also have random packet numbers.
```
모든 헤더의 0-15바이트는 QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) 및 [Nonces](https://eprint.iacr.org/2019/624.pdf)와 유사하게 ChaCha20을 사용하여 알려진 키로부터 계산된 데이터와 XOR 연산을 통해 헤더 보호 방식으로 암호화됩니다. 이는 암호화된 짧은 헤더와 긴 헤더의 첫 번째 부분이 무작위로 보이도록 보장합니다.

#### ChaCha20/Poly1305

Session Request와 Session Created의 경우, 긴 헤더의 16-31바이트와 32바이트 Noise ephemeral key는 ChaCha20을 사용하여 암호화됩니다. 암호화되지 않은 데이터는 랜덤하므로, 암호화된 데이터도 랜덤하게 보일 것입니다.

#### 참고 사항

Retry의 경우, long header의 16-31번째 바이트는 ChaCha20을 사용하여 암호화됩니다. 암호화되지 않은 데이터는 임의의 값이므로, 암호화된 데이터도 임의의 값처럼 보일 것입니다.

- 온라인 DPI가 프로토콜을 식별하는 것을 방지
- 핸드셰이크 재전송을 제외하고 동일한 연결에서 일련의 메시지 패턴을 방지
- 서로 다른 연결에서 동일한 유형의 메시지 패턴을 방지
- netDb에서 발견되는 introduction key에 대한 지식 없이 핸드셰이크 헤더의 복호화를 방지
- netDb에서 발견되는 introduction key에 대한 지식 없이 X25519 임시 키의 식별을 방지
- 온라인 또는 오프라인 공격자에 의한 데이터 단계 패킷 번호 및 유형의 복호화를 방지
- netDb에서 발견되는 introduction key에 대한 지식 없이 경로상 또는 경로외 관찰자에 의한 유효한 핸드셰이크 패킷 주입을 방지
- 경로상 또는 경로외 관찰자에 의한 유효한 데이터 패킷 주입을 방지
- 들어오는 패킷의 빠르고 효율적인 분류를 허용
- 잘못된 Session Request에 대한 응답이 없거나, Retry 응답이 있더라도 netDb에서 발견되는 introduction key에 대한 지식 없이는 해당 응답이 I2P로 식별되지 않도록 하는 "프로빙" 저항성을 제공
- Destination Connection ID는 중요한 데이터가 아니며, netDb에서 발견되는 introduction key에 대한 지식을 가진 관찰자가 복호화할 수 있어도 문제없음
- 데이터 단계 패킷의 패킷 번호는 AEAD nonce이며 중요한 데이터입니다. netDb에서 발견되는 introduction key에 대한 지식을 가진 관찰자라도 복호화할 수 없어야 합니다. [Nonces](https://eprint.iacr.org/2019/624.pdf)를 참조하십시오.

QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) 헤더 보호 방식과 달리, 목적지 및 소스 connection ID를 포함한 모든 헤더의 모든 부분이 암호화됩니다. QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001)과 [Nonces](https://eprint.iacr.org/2019/624.pdf)는 주로 헤더의 "중요한" 부분, 즉 패킷 번호(ChaCha20 nonce)를 암호화하는 데 중점을 둡니다. session ID를 암호화하면 들어오는 패킷 분류가 약간 더 복잡해지지만, 일부 공격을 더 어렵게 만듭니다. QUIC는 서로 다른 단계와 경로 챌린지 및 연결 마이그레이션을 위해 서로 다른 connection ID를 정의합니다. 여기서는 connection ID가 암호화되므로 전체에 걸쳐 동일한 connection ID를 사용합니다.

헤더 보호 키 단계는 7개가 있습니다:

헤더 암호화는 복잡한 휴리스틱이나 대체 방법 없이 인바운드 패킷의 신속한 분류를 허용하도록 설계되었습니다. 이는 거의 모든 인바운드 메시지에 동일한 k_header_1 키를 사용함으로써 달성됩니다. 실제 IP 변경이나 NAT 동작으로 인해 연결의 소스 IP나 포트가 변경되더라도, 연결 ID의 단일 조회로 패킷을 세션에 신속하게 매핑할 수 있습니다.

Session Created와 Retry는 송신자(Bob)의 intro key를 사용하기 때문에 Connection ID를 복호화하기 위해 k_header_1에 대한 대체 처리가 필요한 유일한 메시지입니다. 다른 모든 메시지는 k_header_1에 대해 수신자의 intro key를 사용합니다. 대체 처리는 소스 IP/포트별로 대기 중인 아웃바운드 연결만 조회하면 됩니다.

소스 IP/포트에 의한 대체 처리가 대기 중인 아웃바운드 연결을 찾지 못하는 경우, 여러 원인이 있을 수 있습니다:

대기 중인 아웃바운드 연결을 찾고 해당 연결에 대한 k_header_1을 사용하여 연결 ID를 복호화하는 추가적인 폴백 처리가 가능하지만, 아마도 필요하지 않을 것입니다. Bob이 NAT 또는 패킷 라우팅에 문제가 있다면, 연결이 실패하도록 두는 것이 더 나을 것입니다. 이 설계는 엔드포인트가 핸드셰이크 기간 동안 안정적인 주소를 유지한다는 것에 의존합니다.

추가 가이드라인은 아래의 Inbound Packet Handling 섹션을 참조하세요.

- Session Request and Token Request
- Session Created
- 재시도
- Session Confirmed
- Data Phase
- Peer Test
- Hole Punch

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_1</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_2</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Request KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Created KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice/Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See data phase KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 5,7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Hole Punch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
  </tbody>
</table>
해당 단계의 헤더 암호화 키 유도에 대해서는 아래의 개별 KDF 섹션을 참조하세요.

이 KDF는 패킷의 마지막 24바이트를 두 ChaCha20 연산의 IV로 사용합니다. 모든 패킷이 16바이트 MAC으로 끝나므로, 모든 패킷 페이로드는 최소 8바이트여야 합니다. 이 요구사항은 아래 메시지 섹션에서 추가로 문서화되어 있습니다.

헤더의 처음 8바이트를 복호화한 후, 수신자는 Destination Connection ID를 알게 됩니다. 그 시점부터 수신자는 세션의 키 단계를 기반으로 헤더의 나머지 부분에 사용할 헤더 암호화 키를 알 수 있습니다.

- SSU2 메시지가 아님
- 손상된 SSU2 메시지
- 응답이 공격자에 의해 스푸핑되거나 수정됨
- Bob이 대칭 NAT를 사용함
- Bob이 메시지 처리 중에 IP 또는 포트를 변경함
- Bob이 다른 인터페이스로 응답을 전송함

헤더의 다음 8바이트를 복호화하면 메시지 타입이 드러나고 짧은 헤더인지 긴 헤더인지 판단할 수 있습니다. 긴 헤더인 경우, 수신자는 버전과 netid 필드를 검증해야 합니다. 버전이 2가 아니거나 netid가 예상 값(일반적으로 2, 테스트 네트워크 제외)이 아닌 경우, 수신자는 메시지를 삭제해야 합니다.

모든 메시지는 3개 또는 4개의 부분을 포함합니다:

모든 경우에 헤더(그리고 존재하는 경우 ephemeral key)는 전체 메시지가 온전함을 보장하기 위해 인증 MAC에 바인딩됩니다.

#### AEAD 오류 처리

```
// incoming encrypted packet
packet = incoming encrypted packet
len = packet.length

// take the next-to-last 12 bytes of the packet
iv = packet[len-24:len-13]
k_header_1 = header encryption key 1
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_1, iv, data)

// encrypt the first part of the header by XORing with the mask
packet[0:7] ^= mask[0:7]

// take the last 12 bytes of the packet
iv = packet[len-12:len-1]
k_header_2 = header encryption key 2
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_2, iv, data)

// encrypt the second part of the header by XORing with the mask
packet[8:15] ^= mask[0:7]


// For Session Request and Session Created only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header and the ephemeral key
packet[16:63] = ChaCha20.encrypt(k_header_2, iv, packet[16:63])


// For Retry, Token Request, Peer Test, and Hole Punch only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header
packet[16:31] = ChaCha20.encrypt(k_header_2, iv, packet[16:31])
```
인바운드 패킷 핸들러는 메시지를 처리하기 전에 항상 ChaCha20 페이로드를 복호화하고 MAC을 검증해야 하지만, 한 가지 예외가 있습니다: 유효하지 않은 토큰을 포함한 Session Request 메시지로 보이는 주소 스푸핑된 패킷으로부터의 DoS 공격을 완화하기 위해, 핸들러는 전체 메시지를 복호화하고 검증하려고 시도할 필요가 없습니다(ChaCha20/Poly1305 복호화에 더해 비용이 많이 드는 DH 연산이 필요함). 핸들러는 Session Request 메시지의 헤더에서 찾은 값들을 사용하여 Retry 메시지로 응답할 수 있습니다.

#### 초기 ChainKey를 위한 KDF

세 개의 별도 인증 암호화 인스턴스(CipherStates)가 있습니다. 하나는 핸드셰이크 단계에서 사용되고, 두 개(송신 및 수신)는 데이터 단계에서 사용됩니다. 각각은 KDF에서 파생된 고유한 키를 가집니다.

암호화/인증된 데이터는 다음과 같이 표현됩니다

### 인증된 암호화

암호화되고 인증된 데이터 형식.

- 메시지 헤더
- Session Request와 Session Created에만 해당하는 임시 키
- ChaCha20으로 암호화된 페이로드
- Poly1305 MAC

암호화/복호화 함수의 입력값:

- 핸드셰이크 메시지인 Session Request, Session Created, Session Confirmed의 경우, 메시지 헤더는 Noise 처리 단계 이전에 mixHash()됩니다
- ephemeral key가 존재하는 경우, 표준 Noise misHash()로 보호됩니다
- Noise 핸드셰이크 외부의 메시지의 경우, 헤더는 ChaCha20/Poly1305 암호화를 위한 Associated Data로 사용됩니다.

암호화 함수의 출력, 복호화 함수의 입력:

### Session Request를 위한 KDF

ChaCha20의 경우, 여기에 설명된 내용은 [RFC-7539](https://tools.ietf.org/html/rfc7539)에 해당하며, 이는 TLS [RFC-7905](https://tools.ietf.org/html/rfc7905)에서도 유사하게 사용됩니다.

Key Derivation Function (KDF)는 [RFC-2104](https://tools.ietf.org/html/rfc2104)에서 정의된 HMAC-SHA256(key, data)를 사용하여 DH 결과로부터 핸드셰이크 단계 암호 키 k를 생성합니다. 이는 Noise 사양에서 정의된 것과 정확히 동일한 InitializeSymmetric(), MixHash(), MixKey() 함수들입니다.

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   Encrypted and authenticated data    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
```
#### Session Request를 위한 KDF

Alice가 Bob에게 보내는 메시지로, 핸드셰이크의 첫 번째 메시지이거나 Retry 메시지에 대한 응답입니다. Bob은 Session Created 메시지로 응답합니다. 크기: 80 + 페이로드 크기. 최소 크기: 88

Alice가 유효한 토큰을 가지고 있지 않다면, Session Request 생성 시 비대칭 암호화 오버헤드를 피하기 위해 Session Request 대신 Token Request 메시지를 보내야 합니다.

```
k :: 32 byte cipher key, as generated from KDF

nonce :: Counter-based nonce, 12 bytes.
         Starts at 0 and incremented for each message.
         First four bytes are always zero.
         Last eight bytes are the counter, little-endian encoded.
         Maximum value is 2**64 - 2.
         Connection must be dropped and restarted after
         it reaches that value.
         The value 2**64 - 1 must never be sent.

ad :: In handshake phase:
      Associated data, 32 bytes.
      The SHA256 hash of all preceding data.
      In data phase:
      The packet header, 16 bytes.

data :: Plaintext data, 0 or more bytes
```
긴 헤더. Noise 내용: Alice의 임시 키 X Noise 페이로드: DateTime 및 기타 블록 최대 페이로드 크기: MTU - 108 (IPv4) 또는 MTU - 128 (IPv6). 1280 MTU의 경우: 최대 페이로드는 1172 (IPv4) 또는 1152 (IPv6). 1500 MTU의 경우: 최대 페이로드는 1392 (IPv4) 또는 1372 (IPv6).

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|       ChaCha20 encrypted data         |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|  Poly1305 Message Authentication Code |
+              (MAC)                    +
|             16 bytes                  |
+----+----+----+----+----+----+----+----+

encrypted data :: Same size as plaintext data, 0 - 65519 bytes

MAC :: Poly1305 message authentication code, 16 bytes
```
페이로드 보안 속성:

#### 페이로드

- ChaCha20는 스트림 암호이므로 평문을 패딩할 필요가 없습니다. 추가 키스트림 바이트는 폐기됩니다.
- 암호의 키(256비트)는 SHA256 KDF를 통해 합의됩니다. 각 메시지에 대한 KDF의 세부 사항은 아래의 별도 섹션에 있습니다.

#### 참고 사항

- 모든 메시지에서 AEAD 메시지 크기는 미리 알 수 있습니다. AEAD 인증 실패 시, 수신자는 추가 메시지 처리를 중단하고 메시지를 폐기해야 합니다.
- Bob은 반복적인 실패가 발생한 IP들의 블랙리스트를 유지해야 합니다.

### SessionRequest (타입 0)

X 값은 페이로드 구별 불가능성과 고유성을 보장하기 위해 암호화되며, 이는 필수적인 DPI 대응책입니다. 이를 위해 elligator2와 같은 더 복잡하고 느린 대안보다는 ChaCha20 암호화를 사용합니다. Bob의 router 공개 키로 비대칭 암호화를 하기에는 너무 느릴 것입니다. ChaCha20 암호화는 netDb에 게시된 Bob의 intro 키를 사용합니다.

#### 페이로드

```
// Define protocol_name.
Set protocol_name = "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256"
 (52 bytes, US-ASCII encoded, no NULL termination).

// Define Hash h = 32 bytes
h = SHA256(protocol_name);

Define ck = 32 byte chaining key. Copy the h data to ck.
Set ck = h

// MixHash(null prologue)
h = SHA256(h);

// up until here, can all be precalculated by Alice for all outgoing connections

// Bob's X25519 static keys
// bpk is published in routerinfo
bsk = GENERATE_PRIVATE()
bpk = DERIVE_PUBLIC(bsk)

// Bob static key
// MixHash(bpk)
// || below means append
h = SHA256(h || bpk);

// Bob introduction key
// bik is published in routerinfo
bik = RANDOM(32)

// up until here, can all be precalculated by Bob for all incoming connections
```
#### 참고사항

```
// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Alice's X25519 ephemeral keys
aesk = GENERATE_PRIVATE()
aepk = DERIVE_PUBLIC(aesk)

// Alice ephemeral key X
// MixHash(aepk)
h = SHA256(h || aepk);

// h is used as the associated data for the AEAD in Session Request
// Retain the Hash h for the Session Created KDF


End of "e" message pattern.

This is the "es" message pattern:

// DH(e, rs) == DH(s, re)
sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
// ChaChaPoly parameters to encrypt/decrypt
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chainKey for Session Created KDF


End of "es" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2 = bik

// Header encryption keys for next message (Session Created)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessCreateHeader", 32)

// Header encryption keys for next message (Retry)
k_header_1 = bik
k_header_2 = bik
```
### Session Created 및 Session Confirmed part 1을 위한 KDF

ChaCha20 암호화는 DPI 저항성을 위해서만 사용됩니다. 네트워크 데이터베이스에 공개된 Bob의 소개 키를 알고 있는 모든 당사자는 이 메시지의 헤더와 X 값을 복호화할 수 있습니다.

원시 내용:

암호화되지 않은 데이터 (Poly1305 인증 태그는 표시되지 않음):

최소 페이로드 크기는 8바이트입니다. DateTime 블록은 7바이트에 불과하므로, 최소한 하나의 다른 블록이 존재해야 합니다.

```
XK(s, rs):           Authentication   Confidentiality
  -> e, es                  0                2

  Authentication: None (0).
  This payload may have been sent by any party, including an active attacker.

  Confidentiality: 2.
  Encryption to a known recipient, forward secrecy for sender compromise
  only, vulnerable to replay.  This payload is encrypted based only on DHs
  involving the recipient's static key pair.  If the recipient's static
  private key is compromised, even at a later date, this payload can be
  decrypted.  This message can also be replayed, since there's no ephemeral
  contribution from the recipient.

  "e": Alice generates a new ephemeral key pair and stores it in the e
       variable, writes the ephemeral public key as cleartext into the
       message buffer, and hashes the public key along with the old h to
       derive a new h.

  "es": A DH is performed between the Alice's ephemeral key pair and the
        Bob's static key pair.  The result is hashed along with the old ck to
        derive a new ck and k, and n is set to zero.
```
Bob이 Session Request 메시지에 대한 응답으로 Alice에게 보냅니다. Alice는 Session Confirmed 메시지로 응답합니다. 크기: 80 + 페이로드 크기. 최소 크기: 88

Noise 내용: Bob의 임시 키 Y Noise 페이로드: DateTime, Address 및 기타 블록들 최대 페이로드 크기: MTU - 108 (IPv4) 또는 MTU - 128 (IPv6). 1280 MTU의 경우: 최대 페이로드는 1172 (IPv4) 또는 1152 (IPv6). 1500 MTU의 경우: 최대 페이로드는 1392 (IPv4) 또는 1372 (IPv6).

페이로드 보안 속성:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|    See Header Encryption KDF          |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key n=0     +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+       X, ChaCha20 encrypted           +
|       with Bob intro key n=0          |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|  k defined in KDF for Session Request |
+  n = 0                                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

X :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted X)
```
Y 값은 페이로드의 구별 불가능성과 고유성을 보장하기 위해 암호화되며, 이는 필요한 DPI 대응 조치입니다. 이를 위해 elligator2와 같은 더 복잡하고 느린 대안보다는 ChaCha20 암호화를 사용합니다. Alice의 router 공개 키에 대한 비대칭 암호화는 너무 느릴 것입니다. ChaCha20 암호화는 네트워크 데이터베이스에 게시된 Bob의 intro 키를 사용합니다.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                   X                   |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|     see below for allowed blocks      |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 0

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Alice, ignored

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: 0 if not previously received from Bob

X :: 32 bytes, X25519 ephemeral key, little endian
```
#### 문제

- DateTime 블록
- Options 블록 (선택사항)
- Relay Tag Request 블록 (선택사항)
- Padding 블록 (선택사항)

ChaCha20 암호화는 DPI 저항용으로만 사용됩니다. Bob의 intro key를 알고 있는 당사자(이는 네트워크 데이터베이스에 공개됨)가 Session Request의 첫 32바이트를 캡처한 경우, 이 메시지의 Y 값을 복호화할 수 있습니다.

#### 페이로드

- 초기 ChaCha20 블록의 고유한 X 값은 모든 세션에 대해 암호문이 다르도록 보장합니다.
- 탐지 저항성을 제공하기 위해, Bob은 Session Request 메시지의 메시지 타입, 프로토콜 버전, 네트워크 ID 필드가 유효하지 않은 경우 Session Request 메시지에 대한 응답으로 Retry 메시지를 보내서는 안 됩니다.
- Bob은 타임스탬프 값이 현재 시간과 너무 멀리 떨어진 연결을 거부해야 합니다. 최대 델타 시간을 "D"라고 합니다. Bob은 이전에 사용된 핸드셰이크 값의 로컬 캐시를 유지하고 재생 공격을 방지하기 위해 중복을 거부해야 합니다. 캐시의 값들은 최소 2*D의 수명을 가져야 합니다. 캐시 값은 구현에 따라 다르지만, 32바이트 X 값(또는 그 암호화된 동등물)을 사용할 수 있습니다. 제로 토큰과 종료 블록이 포함된 Retry 메시지를 보내어 거부합니다.
- Diffie-Hellman 임시 키는 암호학적 공격을 방지하기 위해 재사용되어서는 안 되며, 재사용은 재생 공격으로 거부됩니다.
- "KE"와 "auth" 옵션은 호환되어야 하며, 즉 공유 비밀 K는 적절한 크기여야 합니다. 더 많은 "auth" 옵션이 추가되면, 이는 "KE" 플래그의 의미를 다른 KDF 또는 다른 절단 크기를 사용하도록 암시적으로 변경할 수 있습니다.
- Bob은 Alice의 임시 키가 여기서 곡선상의 유효한 점인지 검증해야 합니다.
- 패딩은 합리적인 양으로 제한되어야 합니다. Bob은 과도한 패딩이 있는 연결을 거부할 수 있습니다. Bob은 Session Created에서 자신의 패딩 옵션을 지정합니다. 최소/최대 가이드라인은 결정 예정입니다. 최소 0에서 31바이트까지의 임의 크기? (분포는 결정될 예정, 부록 A 참조.)
- AEAD, DH, 명백한 재생, 또는 키 검증 실패를 포함한 대부분의 오류에서, Bob은 추가 메시지 처리를 중단하고 응답하지 않고 메시지를 삭제해야 합니다.
- Bob은 DateTime 블록의 타임스탬프가 너무 많이 기울어진 경우 제로 토큰과 클록 스큐 이유 코드가 있는 Termination 블록을 포함한 Retry 메시지를 보낼 수 있습니다.
- DoS 완화: DH는 상대적으로 비용이 많이 드는 연산입니다. 이전 NTCP 프로토콜과 마찬가지로, router들은 CPU 또는 연결 고갈을 방지하기 위해 모든 필요한 조치를 취해야 합니다. 최대 활성 연결 수와 진행 중인 최대 연결 설정 수에 제한을 두십시오. 읽기 타임아웃을 강제하십시오(읽기당 및 "slowloris"에 대한 총계 모두). 동일한 소스에서의 반복적이거나 동시 연결을 제한하십시오. 반복적으로 실패하는 소스에 대한 블랙리스트를 유지하십시오. AEAD 실패에 응답하지 마십시오. 또는 DH 연산 및 AEAD 검증 전에 Retry 메시지로 응답하십시오.
- "ver" 필드: SSU2를 나타내는 전체 Noise 프로토콜, 확장 및 페이로드 사양을 포함한 SSU2 프로토콜. 이 필드는 향후 변경 사항에 대한 지원을 나타내는 데 사용될 수 있습니다.
- 네트워크 ID 필드는 교차 네트워크 연결을 빠르게 식별하는 데 사용됩니다. 이 필드가 Bob의 네트워크 ID와 일치하지 않으면, Bob은 연결을 끊고 향후 연결을 차단해야 합니다.
- Source Connection ID가 Destination Connection ID와 같으면 Bob은 메시지를 삭제해야 합니다.

### SessionCreated (타입 1)

```
// take h saved from Session Request KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Request)

// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Bob's X25519 ephemeral keys
besk = GENERATE_PRIVATE()
bepk = DERIVE_PUBLIC(besk)

// h is from KDF for Session Request
// Bob ephemeral key Y
// MixHash(bepk)
h = SHA256(h || bepk);

// h is used as the associated data for the AEAD in Session Created
// Retain the Hash h for the Session Confirmed KDF

End of "e" message pattern.

This is the "ee" message pattern:

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chaining key ck for Session Confirmed KDF

End of "ee" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Request KDF above

// Header protection keys for next message (Session Confirmed)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessionConfirmed", 32)
```
### Session Confirmed 파트 1을 위한 KDF, Session Created KDF 사용

원시 내용:

암호화되지 않은 데이터 (Poly1305 인증 태그는 표시되지 않음):

최소 페이로드 크기는 8바이트입니다. DateTime과 Address 블록의 총합이 이보다 크므로, 이 두 블록만으로도 요구 사항을 충족합니다.

```
XK(s, rs):           Authentication   Confidentiality
  <- e, ee                  2                1

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 1.
  Encryption to an ephemeral recipient.
  This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee").
  However, the sender has not authenticated the recipient,
  so this payload might be sent to any party, including an active attacker.


  "e": Bob generates a new ephemeral key pair and stores it in the e variable,
  writes the ephemeral public key as cleartext into the message buffer,
  and hashes the public key along with the old h to derive a new h.

  "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair.
  The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Alice가 Session Created 메시지에 대한 응답으로 Bob에게 보냅니다. Bob은 ACK 블록을 포함한 Data 메시지로 즉시 응답합니다. 크기: 80 + 페이로드 크기. 최소 크기: 약 500 (최소 router info 블록 크기는 약 420바이트)

Noise 내용: Alice의 정적 키 Noise payload 파트 1: 없음 Noise payload 파트 2: Alice의 RouterInfo 및 기타 블록 최대 payload 크기: MTU - 108 (IPv4) 또는 MTU - 128 (IPv6). 1280 MTU의 경우: 최대 payload는 1172 (IPv4) 또는 1152 (IPv6). 1500 MTU의 경우: 최대 payload는 1392 (IPv4) 또는 1372 (IPv6).

페이로드 보안 속성:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with derived key n=0       +
|  See Header Encryption KDF            |
+----+----+----+----+----+----+----+----+
|                                       |
+       Y, ChaCha20 encrypted           +
|       with derived key n=0            |
+              (32 bytes)               +
|       See Header Encryption KDF       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in KDF for Session Created +
|  n = 0; see KDF for associated data   |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

Y :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted Y)
```
이것은 두 개의 ChaChaPoly 프레임을 포함합니다. 첫 번째는 Alice의 암호화된 정적 공개 키입니다. 두 번째는 Noise 페이로드: Alice의 암호화된 RouterInfo, 선택적 옵션들, 그리고 선택적 패딩입니다. 이들은 서로 다른 키를 사용하는데, 그 사이에 MixKey() 함수가 호출되기 때문입니다.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                  Y                    |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|      see below for allowed blocks     |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: The Source Connection ID
                             received from Alice in Session Request

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 1

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Bob, ignored

Source Connection ID :: The Destination Connection ID
                        received from Alice in Session Request

Token :: 0 (unused)

Y :: 32 bytes, X25519 ephemeral key, little endian
```
#### 참고사항

- DateTime 블록
- Address 블록
- Relay Tag 블록 (선택사항)
- New Token 블록 (권장하지 않음, 참고사항 참조)
- First Packet Number 블록 (선택사항)
- Options 블록 (선택사항)
- Termination 블록 (권장하지 않음, 대신 재시도 메시지로 전송)
- Padding 블록 (선택사항)

원본 내용:

#### 세션 확인 단편화

- Alice는 여기서 Bob의 ephemeral 키가 curve 상의 유효한 점인지 검증해야 합니다.
- 패딩은 합리적인 양으로 제한되어야 합니다. Alice는 과도한 패딩이 있는 연결을 거부할 수 있습니다. Alice는 Session Confirmed에서 자신의 패딩 옵션을 지정합니다. 최소/최대 가이드라인은 미정입니다. 최소 0에서 31바이트까지의 랜덤 크기? (분포는 결정될 예정, 부록 A 참조.)
- AEAD, DH, 타임스탬프, 명백한 재생, 또는 키 검증 실패를 포함한 모든 오류 시, Alice는 추가 메시지 처리를 중단하고 응답 없이 연결을 닫아야 합니다.
- Alice는 타임스탬프 값이 현재 시간과 너무 멀리 떨어진 연결을 거부해야 합니다. 최대 델타 시간을 "D"라고 합니다. Alice는 이전에 사용된 핸드셰이크 값의 로컬 캐시를 유지하고 중복을 거부하여 재생 공격을 방지해야 합니다. 캐시의 값들은 최소 2*D의 수명을 가져야 합니다. 캐시 값은 구현에 의존적이지만, 32바이트 Y 값(또는 그 암호화된 등가물)을 사용할 수 있습니다.
- 소스 IP와 포트가 Session Request의 목적지 IP와 포트와 일치하지 않으면 Alice는 메시지를 삭제해야 합니다.
- Destination과 Source Connection ID가 Session Request의 Source와 Destination Connection ID와 일치하지 않으면 Alice는 메시지를 삭제해야 합니다.
- Bob은 Session Request에서 Alice가 요청한 경우 relay tag 블록을 전송합니다.
- Bob이 먼저 Session Confirmed의 검증을 수행해야 하므로 Session Created에서 New Token 블록은 권장되지 않습니다. 아래 Tokens 섹션을 참조하세요.

#### 참고 사항

- 여기에 최소/최대 패딩 옵션을 포함할까요?

### Session Confirmed part 2를 위한 KDF

```
// take h saved from Session Created KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Created)

// MixHash(header)
h = SHA256(h || header)
// h is used as the associated data for the AEAD in Session Confirmed part 1, below

This is the "s" message pattern:

// Alice's X25519 static keys
ask = GENERATE_PRIVATE()
apk = DERIVE_PUBLIC(ask)

// AEAD parameters
// k is from Session Request
n = 1
ad = h
ciphertext = ENCRYPT(k, n++, apk, ad)

// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// h is used as the associated data for the AEAD in Session Confirmed part 2

End of "s" message pattern.

// Header encryption keys for this message
See Session Confirmed part 2 below
```
### SessionConfirmed (타입 2)

```
This is the "se" message pattern:

// DH(ask, bepk) == DH(besk, apk)
sharedSecret = DH(ask, bepk) = DH(besk, apk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// h from Session Confirmed part 1 is used as the associated data for the AEAD in Session Confirmed part 2
// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF
// retain the hash h for the data phase KDF

End of "se" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Created KDF above

// Header protection keys for data phase
See data phase KDF below
```
### 데이터 단계를 위한 KDF

암호화되지 않은 데이터 (Poly1305 인증 태그는 표시되지 않음):

최소 페이로드 크기는 8바이트입니다. RouterInfo 블록이 그보다 훨씬 클 것이므로, 해당 블록만으로도 요구사항이 충족됩니다.

1)  Alice의 Router Info 블록 (필수)   2)  옵션 블록 (선택사항)   3)  I2NP 블록 (선택사항)

```
XK(s, rs):           Authentication   Confidentiality
  -> s, se                  2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).  The
  sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key
  pair.  Assuming the corresponding private keys are secure, this
  authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.  This payload is
  encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static
  DH with the recipient's static key pair.  Assuming the ephemeral private
  keys are secure, and the recipient is not being actively impersonated by an
  attacker that has stolen its static private key, this payload cannot be
  decrypted.

  "s": Alice writes her static public key from the s variable into the
  message buffer, encrypting it, and hashes the output along with the old h
  to derive a new h.

  "se": A DH is performed between the Alice's static key pair and the Bob's
  ephemeral key pair.  The result is hashed along with the old ck to derive a
  new ck and k, and n is set to zero.
```
4\) 패딩 블록 (선택사항) 이 프레임은 다른 블록 타입을 포함해서는 안 됩니다. TODO: relay와 peer test는 어떻게 할까요?

Session Confirmed 메시지는 Bob이 여러 필수 검사를 수행할 수 있도록 Alice의 완전한 서명된 Router Info를 포함해야 합니다:

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|   ChaCha20 encrypted data (32 bytes)  |
+   Encrypted and authenticated data    +
+   Alice static key S                  +
| k defined in KDF for Session Created  |
+     n = 1                             +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+ Length varies (remainder of packet)   +
|                                       |
+   ChaCha20 encrypted data             +
|   see below for allowed blocks        |
+     k defined in KDF for              +
|     Session Confirmed part 2          |
+     n = 0                             +
|     see KDF for associated data       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, ChaCha20 encrypted Alice's X25519 static key, little endian
     inside 48 byte ChaChaPoly frame
```
안타깝게도 Router Info는 RI 블록에서 gzip 압축되었을 때조차 MTU를 초과할 수 있습니다. 따라서 Session Confirmed는 두 개 이상의 패킷으로 분할될 수 있습니다. 이는 SSU2 프로토콜에서 AEAD로 보호된 페이로드가 두 개 이상의 패킷으로 분할되는 유일한 경우입니다.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|              S                        |
+       Alice static key                +
|          (32 bytes)                   |
+                                       +
|                                       |
+                                       +
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|        Noise Payload                  |
+        (length varies)                +
|        see below for allowed blocks   |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As sent in Session Request,
                             or one received in Session Confirmed?

Packet Number :: 0 always, for all fragments, even if retransmitted

type :: 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility

S :: 32 bytes, Alice's X25519 static key, little endian
```
#### 참고사항

- RouterInfo 블록 (첫 번째 블록이어야 함)
- Options 블록 (선택사항)
- New Token 블록 (선택사항)
- Relay Request 블록 (선택사항)
- Peer Test 블록 (선택사항)
- First Packet Number 블록 (선택사항)
- I2NP, First Fragment, 또는 Follow-on Fragment 블록 (선택사항이지만 공간이 부족할 수 있음)
- Padding 블록 (선택사항)

각 패킷의 헤더는 다음과 같이 구성됩니다:

#### 페이로드

- Bob은 일반적인 Router Info 검증을 수행해야 합니다. 서명 타입이 지원되는지 확인하고, 서명을 검증하며, 타임스탬프가 허용 범위 내에 있는지 확인하고, 필요한 기타 검사를 수행해야 합니다. 분할된 Router Info 처리에 대한 참고사항은 아래를 참조하세요.

- Bob은 첫 번째 프레임에서 받은 Alice의 정적 키가 Router Info의 정적 키와 일치하는지 확인해야 합니다. Bob은 먼저 Router Info에서 일치하는 버전(v) 옵션을 가진 NTCP 또는 SSU2 Router Address를 검색해야 합니다. 아래의 Published Router Info 및 Unpublished Router Info 섹션을 참조하세요. 단편화된 Router Info 처리에 대한 참고사항은 아래를 참조하세요.

- Bob이 자신의 netdb에 Alice의 RouterInfo의 이전 버전을 가지고 있다면, router info의 정적 키가 둘 다에서 동일한지 확인하고(존재하는 경우), 이전 버전이 XXX보다 오래되지 않았는지 확인합니다(아래 키 회전 시간 참조)

- Bob은 여기서 Alice의 정적 키가 곡선 상의 유효한 점인지 검증해야 합니다.

- 패딩 매개변수를 지정하기 위한 옵션이 포함되어야 합니다.

- AEAD, RI, DH, 타임스탬프 또는 키 검증 실패를 포함한 모든 오류 시, Bob은 추가 메시지 처리를 중단하고 응답 없이 연결을 종료해야 합니다.

- 메시지 3 파트 2 프레임 내용: 이 프레임의 형식은 데이터 단계 프레임의 형식과 동일하지만, 프레임의 길이는 Alice가 Session Request에서 전송합니다. 데이터 단계 프레임 형식은 아래를 참조하세요. 프레임은 다음 순서로 1~4개의 블록을 포함해야 합니다:

다음과 같이 패킷 시리즈를 구성합니다:

재조립 과정:

- Message 3 part 2 패딩 블록이 권장됩니다.

- MTU와 Router Info 크기에 따라 I2NP 블록을 위한 공간이 없거나 매우 적을 수 있습니다. Router Info가 분할된 경우 I2NP 블록을 포함하지 마십시오. 가장 간단한 구현은 Session Confirmed 메시지에 I2NP 블록을 절대 포함하지 않고, 모든 I2NP 블록을 후속 Data 메시지에서 전송하는 것입니다. 최대 블록 크기는 아래 Router Info 블록 섹션을 참조하십시오.

#### 페이로드

Bob이 Session Confirmed 메시지를 받으면, 그는 헤더를 복호화하고 frag 필드를 검사하여 Session Confirmed가 분할되어 있는지 확인합니다. 그는 모든 분할된 부분이 수신되고 재조립될 때까지 메시지를 복호화하지 않습니다(그리고 할 수도 없습니다).

- RI의 정적 키 "s"가 핸드셰이크의 정적 키와 일치함
- RI의 소개 키 "i"는 추출되어 유효해야 하며, 데이터 단계에서 사용됨
- RI 서명이 유효함

Bob이 개별 fragment들을 ack할 메커니즘은 없습니다. Bob이 모든 fragment들을 수신하고, 재조립하고, 복호화하고, 내용을 검증하면, Bob은 평소와 같이 split()을 수행하고, 데이터 단계에 진입하여 패킷 번호 0의 ACK를 전송합니다.

Alice가 패킷 번호 0에 대한 ACK를 받지 못하면, 그녀는 모든 세션 확인 패킷들을 그대로 재전송해야 합니다.

- 모든 헤더는 동일한 패킷 번호 0을 가진 짧은 헤더입니다
- 모든 헤더는 조각 번호와 총 조각 수를 포함하는 "frag" 필드를 포함합니다
- 조각 0의 암호화되지 않은 헤더는 "jumbo" 메시지의 관련 데이터(AD)입니다
- 각 헤더는 해당 패킷의 데이터 마지막 24바이트를 사용하여 암호화됩니다

예제:

- 단일 RI 블록 생성 (RI 블록 frag 필드에서 1개 중 fragment 0). RI 블록 단편화는 사용하지 않으며, 이는 동일한 문제를 해결하는 대안적 방법을 위한 것이었습니다.
- RI 블록과 포함될 다른 블록들로 "jumbo" 페이로드 생성
- 총 데이터 크기 계산 (헤더 제외), 이는 페이로드 크기 + 정적 키와 두 MAC을 위한 64바이트입니다
- 각 패킷에서 사용 가능한 공간 계산, 이는 MTU에서 IP 헤더(20 또는 40), UDP 헤더(8), SSU2 short 헤더(16)를 뺀 값입니다. 패킷당 총 오버헤드는 44바이트(IPv4) 또는 64바이트(IPv6)입니다.
- 패킷 수 계산
- 마지막 패킷의 데이터 크기 계산. 헤더 암호화가 작동하도록 24바이트 이상이어야 합니다. 너무 작으면 패딩 블록을 추가하거나, 이미 있는 경우 패딩 블록 크기를 늘리거나, 마지막 패킷이 충분히 커지도록 다른 패킷 중 하나의 크기를 줄입니다.
- 첫 번째 패킷의 암호화되지 않은 헤더 생성, frag 필드에 총 fragment 수를 넣고, 평소와 같이 헤더를 AD로 사용하여 Noise로 "jumbo" 페이로드를 암호화합니다.
- 암호화된 jumbo 패킷을 fragment로 분할
- 각 fragment 1-n에 암호화되지 않은 헤더 추가
- 각 fragment 0-n의 헤더 암호화. 각 헤더는 위의 Session Confirmed KDF에서 정의된 동일한 k_header_1과 k_header_2를 사용합니다.
- 모든 fragment 전송

IPv6에서 1500 MTU의 경우, 최대 페이로드는 1372이고, RI 블록 오버헤드는 5이므로, 최대 (gzip 압축된) RI 데이터 크기는 1367입니다 (다른 블록이 없다고 가정). 두 개의 패킷을 사용하면, 두 번째 패킷의 오버헤드는 64이므로 추가로 1436바이트의 페이로드를 담을 수 있습니다. 따라서 두 개의 패킷으로 최대 2803바이트의 압축된 RI를 처리할 수 있습니다.

현재 네트워크에서 확인된 가장 큰 압축된 RI는 약 1400바이트입니다. 따라서 실제로는 최소 1280 MTU로도 두 개의 조각으로 충분해야 합니다. 프로토콜은 최대 15개의 조각을 허용합니다.

- fragment 0의 헤더는 Noise AD로 사용되므로 보존
- 재조립 전에 다른 fragment들의 헤더는 폐기
- fragment 0의 헤더를 AD로 사용하여 "jumbo" 페이로드를 재조립하고 Noise로 복호화
- 평소와 같이 RI 블록 검증
- 데이터 단계로 진행하여 평소와 같이 ACK 0 전송

보안 분석:

단편화된 Session Confirmed의 무결성과 보안은 단편화되지 않은 것과 동일합니다. 어떤 단편이라도 변경되면 재조립 후 Noise AEAD가 실패하게 됩니다. 단편 0 이후 단편들의 헤더는 오직 단편을 식별하는 용도로만 사용됩니다. 경로상의 공격자가 헤더 암호화에 사용되는 k_header_2 키를 가지고 있다 하더라도(핸드셰이크에서 파생되므로 가능성은 낮음), 이것이 공격자로 하여금 유효한 단편을 대체할 수 있게 해주지는 않습니다.

데이터 단계에서는 연관 데이터로 헤더를 사용합니다.

KDF는 [RFC-2104](https://tools.ietf.org/html/rfc2104)에서 정의된 HMAC-SHA256(key, data)를 사용하여 chaining key ck에서 두 개의 cipher key k_ab와 k_ba를 생성합니다. 이는 Noise 스펙에서 정의된 것과 정확히 동일한 split() 함수입니다.

Noise 페이로드: 모든 블록 타입이 허용됩니다. 최대 페이로드 크기: MTU - 60 (IPv4) 또는 MTU - 80 (IPv6). 1500 MTU의 경우: 최대 페이로드는 1440 (IPv4) 또는 1420 (IPv6)입니다.

Session Confirmed의 2번째 부분부터 시작하여, 모든 메시지는 인증되고 암호화된 ChaChaPoly 페이로드 내부에 있습니다. 모든 패딩은 메시지 내부에 있습니다. 페이로드 내부에는 0개 이상의 "블록"을 가진 표준 형식이 있습니다. 각 블록은 1바이트 타입과 2바이트 길이를 가집니다. 타입에는 날짜/시간, I2NP 메시지, 옵션, 종료, 패딩이 포함됩니다.

참고: Bob은 데이터 단계에서 Alice에게 보내는 첫 번째 메시지로 자신의 RouterInfo를 보낼 수 있지만 필수는 아닙니다.

### 데이터 메시지 (타입 6)

페이로드 보안 속성:

암호화되지 않은 데이터 (Poly1305 인증 태그는 표시되지 않음):

```
// split()
// chainKey = from handshake phase
keydata = HKDF(chainKey, ZEROLEN, "", 64)
k_ab = keydata[0:31]
k_ba = keydata[32:63]

// key is k_ab for Alice to Bob
// key is k_ba for Bob to Alice

keydata = HKDF(key, ZEROLEN, "HKDFSSU2DataKeys", 64)
k_data = keydata[0:31]
k_header_2 = keydata[32:63]


// AEAD parameters
k = k_data
n = 4 byte packet number from header
ad = 16 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for data phase
// aik = Alice's intro key
// bik = Bob's intro key
k_header_1 = Receiver's intro key (aik or bik)
k_header_2: from above
```
### Peer Test용 KDF

Charlie는 Alice에게 전송하고, Alice는 Charlie에게 전송하며, 이는 Peer Test 단계 5-7에만 해당됩니다. Peer Test 단계 1-4는 Data 메시지의 Peer Test 블록을 사용하여 세션 내에서 전송되어야 합니다. 자세한 정보는 아래의 Peer Test Block 및 Peer Test Process 섹션을 참조하세요.

크기: 48 + 페이로드 크기.

Noise payload: 아래 참조.

원본 내용:

```
XK(s, rs):           Authentication   Confidentiality
  <-                        2                5
  ->                        2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.
  This payload is encrypted based on an ephemeral-ephemeral DH as well as
  an ephemeral-static DH with the recipient's static key pair.
  Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated
  by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### 참고 사항

- router는 AEAD 오류가 있는 메시지를 삭제해야 합니다.

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with intro key and         +
|  derived key, see Data Phase KDF      |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in Data Phase KDF          +
|  n = packet number from header        |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
암호화되지 않은 데이터 (Poly1305 인증 태그는 표시되지 않음):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|flag|moreflags|
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|                                       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: As specified in session setup

Packet Number :: 4 byte big endian integer

type :: 6

flag :: 1 byte flags:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-1: unused, set to 0 for future compatibility
       bits 0: when set to 1, immediate ack requested

moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### 페이로드

- 최소 페이로드 크기는 8바이트입니다. 이 요구사항은 ACK, I2NP, First Fragment, 또는 Follow-on Fragment 블록에 의해 충족될 것입니다. 요구사항이 충족되지 않으면 Padding 블록을 포함해야 합니다.
- 각 패킷 번호는 한 번만 사용될 수 있습니다. I2NP 메시지나 fragment를 재전송할 때는 새로운 패킷 번호를 사용해야 합니다.

### 피어 테스트 (타입 7)

```
// AEAD parameters
// aik = Alice's intro key
k = aik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = aik
k_header_2 = aik
```
### 재시도를 위한 KDF

최소 페이로드 크기는 8바이트입니다. Peer Test 블록의 총 크기가 이보다 크므로, 이 블록만으로도 요구사항이 충족됩니다.

메시지 5와 7에서, Peer Test 블록은 Charlie가 서명한 합의를 포함하는 세션 내 메시지 3과 4의 블록과 동일할 수도 있고, 재생성될 수도 있습니다. 서명은 선택사항입니다.

메시지 6에서 Peer Test 블록은 Alice가 서명한 요청을 포함하여 세션 내 메시지 1과 2의 블록과 동일할 수도 있고, 새로 생성될 수도 있습니다. 서명은 선택 사항입니다.

Connection ID들: 두 connection ID는 테스트 nonce에서 파생됩니다. Charlie에서 Alice로 전송되는 메시지 5와 7의 경우, Destination Connection ID는 4바이트 빅엔디안 테스트 nonce의 두 복사본입니다. 즉, ((nonce << 32) | nonce)입니다. Source Connection ID는 Destination Connection ID의 역(inverse)입니다. 즉, ~((nonce << 32) | nonce)입니다. Alice에서 Charlie로 전송되는 메시지 6의 경우, 두 connection ID를 교체합니다.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
주소 블록 내용:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

Packet Number :: Random number generated by Alice

type :: 10

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: zero
```
#### 참고사항

- DateTime 블록
- Address 블록 (메시지 6과 7에 필수, 아래 참고사항 참조)
- Peer Test 블록
- Padding 블록 (선택사항)

Retry 메시지에 대한 요구사항은 Bob이 응답으로 Retry 메시지를 생성하기 위해 Session Request 메시지를 복호화할 필요가 없다는 것입니다. 또한, 이 메시지는 대칭 암호화만을 사용하여 빠르게 생성되어야 합니다.

Bob이 Session Request 또는 Token Request 메시지에 대한 응답으로 Alice에게 보냅니다. Alice는 새로운 Session Request로 응답합니다. 크기: 48 + 페이로드 크기.

Termination 블록이 포함된 경우 종료 메시지(즉, "재시도하지 않음")로도 사용됩니다.

Noise 페이로드: 아래를 참조하세요.

원시 내용:

- 메시지 5에서: 필요하지 않음.
- 메시지 6에서: Charlie의 RI에서 선택된 Charlie의 IP와 포트.
- 메시지 7에서: 메시지 6을 받은 Alice의 실제 IP와 포트.

### 재시도 (타입 9)

암호화되지 않은 데이터 (Poly1305 인증 태그는 표시되지 않음):

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### 토큰 요청을 위한 KDF

최소 페이로드 크기는 8바이트입니다. DateTime과 Address 블록의 총합이 그보다 크므로, 이 두 블록만으로도 요구사항이 충족됩니다.

이 메시지는 대칭 암호화만을 사용하여 빠르게 생성되어야 합니다.

Alice가 Bob에게 전송합니다. Bob이 Retry 메시지로 응답합니다. 크기: 48 + 페이로드 크기.

Alice가 유효한 토큰을 가지고 있지 않다면, Session Request 생성 시 비대칭 암호화 오버헤드를 피하기 위해 Session Request 대신 이 메시지를 보내야 합니다.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Noise 페이로드: 아래를 참조하세요.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: The Source Connection ID
                             received from Alice in Token Request
                             or Session Request

Packet Number :: Random number generated by Bob

type :: 9

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: The Destination Connection ID
                        received from Alice in Token Request
                        or Session Request

Token :: 8 byte unsigned integer, randomly generated by Bob, nonzero,
         or zero if session is rejected and a termination block is included
```
#### 페이로드

- DateTime 블록
- Address 블록
- Options 블록 (선택사항)
- Termination 블록 (선택사항, 세션이 거부된 경우)
- Padding 블록 (선택사항)

원본 내용:

#### DateTime

- 탐지 저항성을 제공하기 위해, router는 Request 메시지의 메시지 타입, 프로토콜 버전, 네트워크 ID 필드가 유효하지 않은 경우 Session Request 또는 Token Request 메시지에 대한 응답으로 Retry 메시지를 전송해서는 안 됩니다.
- 위조된 소스 주소를 사용하여 실행될 수 있는 증폭 공격의 규모를 제한하기 위해, Retry 메시지는 대용량의 패딩을 포함해서는 안 됩니다. Retry 메시지는 응답하는 메시지 크기의 3배를 초과하지 않는 것이 권장됩니다. 또는 1-64바이트 범위에서 임의의 패딩을 추가하는 것과 같은 간단한 방법을 사용하십시오.

### 토큰 요청 (타입 10)

암호화되지 않은 데이터 (Poly1305 인증 태그는 표시되지 않음):

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Hole Punch용 KDF

최소 페이로드 크기는 8바이트입니다.

이 메시지는 대칭 암호화만을 사용하여 빠르게 생성되어야 합니다.

Charlie는 Bob으로부터 받은 Relay Intro에 대한 응답으로 Alice에게 보냅니다. Alice는 새로운 Session Request로 응답합니다. 크기: 48 + 페이로드 크기.

Noise payload: 아래를 참조하세요.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
원본 내용:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|    flags     |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As specified in session setup

Packet Number :: 4 byte big endian integer

type :: 6

flags :: 3 bytes, unused, set to 0 for future compatibility
```
#### 옵션

- DateTime 블록
- Padding 블록

암호화되지 않은 데이터 (Poly1305 인증 태그는 표시되지 않음):

#### RouterInfo

- 프로빙 저항성을 제공하기 위해, router는 Token Request 메시지의 메시지 타입, 프로토콜 버전, 네트워크 ID 필드가 유효하지 않은 경우 Token Request 메시지에 대한 응답으로 Retry 메시지를 보내지 않아야 합니다.
- 이것은 표준 Noise 메시지가 아니며 핸드셰이크의 일부가 아닙니다. 연결 ID 이외의 방법으로는 Session Request 메시지와 연결되지 않습니다.
- AEAD 또는 명백한 재생 공격을 포함한 대부분의 오류에서, Bob은 추가 메시지 처리를 중단하고 응답하지 않고 메시지를 삭제해야 합니다.
- Bob은 타임스탬프 값이 현재 시간과 너무 많이 차이나는 연결을 거부해야 합니다. 최대 델타 시간을 "D"라고 합니다. Bob은 이전에 사용된 핸드셰이크 값들의 로컬 캐시를 유지하고 재생 공격을 방지하기 위해 중복을 거부해야 합니다. 캐시의 값들은 최소 2*D의 수명을 가져야 합니다. 캐시 값들은 구현에 따라 다르지만, 32바이트 X 값(또는 그 암호화된 동등물)을 사용할 수 있습니다.
- Bob은 DateTime 블록의 타임스탬프가 너무 많이 치우쳐 있는 경우, 0 토큰과 클럭 스큐 이유 코드가 포함된 Termination 블록을 포함하는 Retry 메시지를 보낼 수 있습니다.
- 최소 크기: TBD, Session Created와 동일한 규칙?

### Hole Punch (Type 11)

최소 페이로드 크기는 8바이트입니다. DateTime과 Address 블록의 총 크기가 그보다 크므로, 이 두 블록만으로도 요구사항을 충족합니다.

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### 페이로드 형식

Connection ID들: 두 connection ID는 relay nonce에서 파생됩니다. Destination Connection ID는 4바이트 빅엔디안 relay nonce의 두 개 복사본입니다. 즉, ((nonce << 32) | nonce)입니다. Source Connection ID는 Destination Connection ID의 역수입니다. 즉, ~((nonce << 32) | nonce)입니다.

Alice는 헤더의 토큰을 무시해야 합니다. Session Request에서 사용될 토큰은 Relay Response 블록에 있습니다.

각 Noise 페이로드는 0개 이상의 "블록"을 포함합니다.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
이는 [NTCP2](/docs/specs/ntcp2)와 [ECIES](/docs/specs/ecies) 사양에서 정의된 것과 동일한 블록 형식을 사용합니다. 개별 블록 유형은 다르게 정의됩니다. QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000)에서 이에 해당하는 용어는 "프레임"입니다.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: See below

type :: 7

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random number generated by Alice or Charlie

Source Connection ID :: See below

Token :: Randomly generated by Alice or Charlie, ignored
```
#### I2NP 메시지

- DateTime 블록
- Address 블록
- Relay Response 블록
- Padding 블록 (선택사항)

구현자들이 코드를 공유하도록 장려하는 것이 파싱 문제로 이어질 수 있다는 우려가 있습니다. 구현자들은 코드 공유의 이점과 위험을 신중하게 고려하고, 두 컨텍스트에서 순서 및 유효한 블록 규칙이 다르도록 보장해야 합니다.

암호화된 페이로드에는 하나 이상의 블록이 있습니다. 블록은 간단한 Tag-Length-Value (TLV) 형식입니다. 각 블록은 1바이트 식별자, 2바이트 길이, 그리고 0개 이상의 데이터 바이트를 포함합니다. 이 형식은 [NTCP2](/docs/specs/ntcp2)와 [ECIES](/docs/specs/ecies)의 형식과 동일하지만, 블록 정의는 다릅니다.

확장성을 위해, 수신자는 알 수 없는 식별자를 가진 블록을 무시하고 패딩으로 처리해야 합니다.

## Noise 페이로드

(Poly1305 인증 태그는 표시되지 않음):

헤더 암호화는 두 개의 ChaCha20 연산을 위한 IV로 패킷의 마지막 24바이트를 사용합니다. 모든 패킷은 16바이트 MAC으로 끝나므로, 모든 패킷 페이로드는 최소 8바이트여야 합니다. 페이로드가 이 요구사항을 충족하지 않는 경우, Padding 블록을 포함해야 합니다.

최대 ChaChaPoly 페이로드는 메시지 유형, MTU, IPv4 또는 IPv6 주소 유형에 따라 달라집니다. 최대 페이로드는 IPv4의 경우 MTU - 60이고 IPv6의 경우 MTU - 80입니다. 최대 페이로드 데이터는 IPv4의 경우 MTU - 63이고 IPv6의 경우 MTU - 83입니다. 상한은 IPv4, 1500 MTU, Data 메시지의 경우 약 1440바이트입니다. 최대 총 블록 크기는 최대 페이로드 크기입니다. 최대 단일 블록 크기는 최대 총 블록 크기입니다. 블록 유형은 1바이트입니다. 블록 길이는 2바이트입니다. 최대 단일 블록 데이터 크기는 최대 단일 블록 크기에서 3을 뺀 값입니다.

### 블록 순서 규칙

참고 사항:

블록 유형:

Session Confirmed에서 Router Info는 첫 번째 블록이어야 합니다.

```
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
~               .   .   .               ~

blk :: 1 byte, see below
size :: 2 bytes, big endian, size of data to follow, 0 - TBD
data :: the data
```
다른 모든 메시지에서는 순서가 지정되지 않지만, 다음 요구사항은 예외입니다: Padding이 있는 경우 마지막 블록이어야 합니다. Termination이 있는 경우 Padding을 제외하고 마지막 블록이어야 합니다. 단일 페이로드에서 여러 개의 Padding 블록은 허용되지 않습니다.

시간 동기화를 위해:

참고사항:

- 구현자는 블록을 읽을 때 잘못된 형식이거나 악의적인 데이터로 인해 다음 블록이나 페이로드 경계를 넘어서 읽기가 발생하지 않도록 보장해야 합니다.
- 구현체는 향후 호환성을 위해 알려지지 않은 블록 유형을 무시해야 합니다.

업데이트된 옵션을 전달합니다. 옵션에는 최소 및 최대 패딩이 포함됩니다.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Block Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Number</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Block Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Options</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15+</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Router Info</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">I2NP Message</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Follow-on Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Termination</td><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 typ.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">8</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Intro</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Next Nonce</td><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">ACK</td><td style="border:1px solid var(--color-border); padding:0.6rem;">12</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 or 21</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;">--</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">17</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Challenge</td><td style="border:1px solid var(--color-border); padding:0.6rem;">18</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">19</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Packet Number</td><td style="border:1px solid var(--color-border); padding:0.6rem;">20</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Congestion</td><td style="border:1px solid var(--color-border); padding:0.6rem;">21</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for experimental features</td><td style="border:1px solid var(--color-border); padding:0.6rem;">224-253</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Padding</td><td style="border:1px solid var(--color-border); padding:0.6rem;">254</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for future extension</td><td style="border:1px solid var(--color-border); padding:0.6rem;">255</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>           
### 블록 사양

Options 블록은 가변 길이입니다.

옵션 문제:

### 세션 요청

#### 첫 번째 조각

Alice의 RouterInfo를 Bob에게 전달합니다. Session Confirmed part 2 페이로드에서만 사용됩니다. 데이터 단계에서는 사용하지 말고 대신 I2NP DatabaseStore 메시지를 사용하세요.

```
+----+----+----+----+----+----+----+
| 0  |    4    |     timestamp     |
+----+----+----+----+----+----+----+

blk :: 0
size :: 2 bytes, big endian, value = 4
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
```
최소 크기: 약 420바이트. 단, router info의 router identity와 서명이 압축 가능한 경우는 예외이나, 이는 가능성이 낮습니다.

- SSU 1과 달리, SSU 2에서는 데이터 단계의 패킷 헤더에 타임스탬프가 없습니다.
- 구현체는 데이터 단계에서 주기적으로 DateTime 블록을 보내야 합니다.
- 구현체는 네트워크에서 클럭 편향을 방지하기 위해 가장 가까운 초로 반올림해야 합니다.

#### 후속 Fragment

참고: Router Info 블록은 절대 분할되지 않습니다. frag 필드는 항상 0/1입니다. 자세한 내용은 위의 Session Confirmed 분할 섹션을 참조하세요.

참고:

```
+----+----+----+----+----+----+----+----+
| 1  |  size   |tmin|tmax|rmin|rmax|tdmy|
+----+----+----+----+----+----+----+----+
|tdmy|  rdmy   |  tdelay |  rdelay |    |
~----+----+----+----+----+----+----+    ~
|              more_options             |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 1
size :: 2 bytes, big endian, size of options to follow, 12 bytes minimum

tmin, tmax, rmin, rmax :: requested padding limits
    tmin and rmin are for desired resistance to traffic analysis.
    tmax and rmax are for bandwidth limits.
    tmin and tmax are the transmit limits for the router sending this options block.
    rmin and rmax are the receive limits for the router sending this options block.
    Each is a 4.4 fixed-point float representing 0 to 15.9375
    (or think of it as an unsigned 8-bit integer divided by 16.0).
    This is the ratio of padding to data. Examples:
    Value of 0x00 means no padding
    Value of 0x01 means add 6 percent padding
    Value of 0x10 means add 100 percent padding
    Value of 0x80 means add 800 percent (8x) padding
    Alice and Bob will negotiate the minimum and maximum in each direction.
    These are guidelines, there is no enforcement.
    Sender should honor receiver's maximum.
    Sender may or may not honor receiver's minimum, within bandwidth constraints.

tdmy: Max dummy traffic willing to send, 2 bytes big endian, bytes/sec average
rdmy: Requested dummy traffic, 2 bytes big endian, bytes/sec average
tdelay: Max intra-message delay willing to insert, 2 bytes big endian, msec average
rdelay: Requested intra-message delay, 2 bytes big endian, msec average

Padding distribution specified as additional parameters?
Random delay specified as additional parameters?

more_options :: Format TBD
```
수정된 헤더가 포함된 완전한 I2NP 메시지.

- 옵션 협상은 TBD입니다.

#### 종료

이는 [NTCP2](/docs/specs/ntcp2)에서와 동일한 9바이트를 I2NP 헤더에 사용합니다 (타입, 메시지 ID, 짧은 만료시간).

참고:

수정된 헤더를 가진 I2NP 메시지의 첫 번째 조각(fragment #0).

```
+----+----+----+----+----+----+----+----+
| 2  |  size   |flag|frag|              |
+----+----+----+----+----+              +
|                                       |
+       Router Info fragment            +
| (Alice RI in Session Confirmed)       |
+ (Alice, Bob, or third-party           +
|  RI in data phase)                    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 2
size :: 2 bytes, big endian, 2 + fragment size
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 0 for local store, 1 for flood request
       bit 1: 0 for uncompressed, 1 for gzip compressed
       bits 7-2: Unused, set to 0 for future compatibility
frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number, always 0
       bits 3-0: total fragments, always 1, big endian

routerinfo :: Alice's or Bob's RouterInfo
```
이는 [NTCP2](/docs/specs/ntcp2)에서와 동일한 9바이트의 I2NP 헤더를 사용합니다 (타입, 메시지 ID, 짧은 만료 시간).

- Router Info는 플래그 비트 1로 표시되는 바와 같이 선택적으로 gzip으로 압축됩니다. 이는 절대 압축되지 않는 NTCP2나 항상 압축되는 DatabaseStore Message와는 다릅니다. 압축은 선택사항인데, 압축 가능한 콘텐츠가 거의 없는 작은 Router Info에서는 보통 거의 도움이 되지 않지만, 여러 압축 가능한 Router Address가 있는 큰 Router Info에서는 매우 유용하기 때문입니다. Router Info가 단편화 없이 단일 Session Confirmed 패킷에 맞도록 할 수 있다면 압축이 권장됩니다.
- Session Confirmed 메시지에서 첫 번째 또는 유일한 단편의 최대 크기: IPv4의 경우 MTU - 113 또는 IPv6의 경우 MTU - 133입니다. 1500바이트 기본 MTU를 가정하고 메시지에 다른 블록이 없다면, IPv4의 경우 1387 또는 IPv6의 경우 1367입니다. 현재 router info의 97%는 gzip 없이 1367보다 작습니다. 현재 router info의 99.9%는 gzip 적용 시 1367보다 작습니다. 1280바이트 최소 MTU를 가정하고 메시지에 다른 블록이 없다면, IPv4의 경우 1167 또는 IPv6의 경우 1147입니다. 현재 router info의 94%는 gzip 없이 1147보다 작습니다. 현재 router info의 97%는 gzip 적용 시 1147보다 작습니다.
- frag 바이트는 이제 사용되지 않으며, Router Info 블록은 절대 단편화되지 않습니다. frag 바이트는 단편 0, 전체 단편 1로 설정되어야 합니다. 자세한 내용은 위의 Session Confirmed Fragmentation 섹션을 참조하세요.
- RouterInfo에 게시된 RouterAddress가 있지 않으면 플러딩을 요청해서는 안 됩니다. 수신 router는 RouterInfo에 게시된 RouterAddress가 없으면 RouterInfo를 플러딩해서는 안 됩니다.
- 이 프로토콜은 RouterInfo가 저장되거나 플러딩되었다는 확인 응답을 제공하지 않습니다. 확인 응답이 필요하고 수신자가 floodfill인 경우, 발신자는 대신 응답 토큰과 함께 표준 I2NP DatabaseStoreMessage를 보내야 합니다.

#### RelayRequest

총 프래그먼트 수가 지정되지 않았습니다.

참고:

```
+----+----+----+----+----+----+----+----+
| 3  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |     message       |
+----+----+----+----+                   +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 3
size :: 2 bytes, big endian, size of type + msg id + exp + message to follow
        I2NP message body size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: I2NP message body
```
I2NP 메시지의 추가 조각 (0보다 큰 조각 번호).

- 이는 NTCP2에서 사용되는 것과 동일한 9바이트 I2NP 헤더 형식입니다.
- 이는 First Fragment 블록과 정확히 동일한 형식이지만, 블록 타입이 이것이 완전한 메시지임을 나타냅니다.
- 9바이트 I2NP 헤더를 포함한 최대 크기는 IPv4의 경우 MTU - 63이고 IPv6의 경우 MTU - 83입니다.

#### RelayResponse

참고사항:

연결을 끊습니다. 이것은 페이로드에서 패딩이 아닌 마지막 블록이어야 합니다.

주의사항:

```
+----+----+----+----+----+----+----+----+
| 4  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |                   |
+----+----+----+----+                   +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 4
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: Partial I2NP message body, bytes 0 - (size - 10)
```
세션 내에서 Alice에서 Bob으로 Data 메시지로 전송됩니다. 아래의 Relay Process 섹션을 참조하세요.

- 이것은 NTCP2에서 사용되는 것과 동일한 9바이트 I2NP 헤더 형식입니다.
- 이것은 I2NP Message 블록과 정확히 동일한 형식이지만, 블록 타입은 이것이 메시지의 첫 번째 fragment임을 나타냅니다.
- 부분 메시지 길이는 0보다 커야 합니다.
- SSU 1에서와 같이, 마지막 fragment를 먼저 보내는 것이 권장됩니다. 이렇게 하면 수신자가 전체 fragment 수를 알고 수신 버퍼를 효율적으로 할당할 수 있습니다.
- 9바이트 I2NP 헤더를 포함한 최대 크기는 IPv4의 경우 MTU - 63, IPv6의 경우 MTU - 83입니다.

#### RelayIntro

참고사항:

```
+----+----+----+----+----+----+----+----+
| 5  |  size   |frag|    msg id         |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 5
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 5).
frag :: Fragment info:
        Bit order: 76543210 (bit 7 is MSB)
        bits 7-1: fragment number 1 - 127 (0 not allowed)
        bit 0: isLast (1 = true)
msg id :: 4 bytes, big endian, I2NP message ID
message :: Partial I2NP message body
```
서명:

- 부분 메시지 길이는 0보다 커야 합니다.
- SSU 1에서와 같이, 수신자가 전체 fragment 수를 알고 수신 버퍼를 효율적으로 할당할 수 있도록 마지막 fragment를 먼저 보내는 것이 권장됩니다.
- SSU 1에서와 같이, 최대 fragment 번호는 127이지만, 실용적인 한계는 63 이하입니다. 구현체는 약 64 KB의 최대 I2NP 메시지 크기에 대해 실용적인 수준으로 최대값을 제한할 수 있으며, 이는 1280 최소 MTU에서 약 55개의 fragment입니다. 아래의 Max I2NP Message Size 섹션을 참조하세요.
- 최대 부분 메시지 크기(fragment 및 메시지 ID 제외)는 IPv4의 경우 MTU - 68, IPv6의 경우 MTU - 88입니다.

#### PeerTest

Alice는 요청에 서명하고 이를 이 블록에 포함합니다; Bob은 이를 Relay Intro 블록에서 Charlie에게 전달합니다. 서명 알고리즘: Alice의 router 서명 키로 다음 데이터에 서명합니다:

```
+----+----+----+----+----+----+----+----+
| 6  |  size   |    valid data packets  |
+----+----+----+----+----+----+----+----+
    received   | rsn|     addl data     |
+----+----+----+----+                   +
~               .   .   .               ~
+----+----+----+----+----+----+----+----+

blk :: 6
size :: 2 bytes, big endian, value = 9 or more
valid data packets received :: The number of valid packets received
                              (current receive nonce value)
                              0 if error occurs in handshake phase
                              8 bytes, big endian
rsn :: reason, 1 byte:
       0: normal close or unspecified
       1: termination received
       2: idle timeout
       3: router shutdown
       4: data phase AEAD failure
       5: incompatible options
       6: incompatible signature type
       7: clock skew
       8: padding violation
       9: AEAD framing error
       10: payload format error
       11: Session Request error
       12: Session Created error
       13: Session Confirmed error
       14: Timeout
       15: RI signature verification fail
       16: s parameter missing, invalid, or mismatched in RouterInfo
       17: banned
       18: bad token
       19: connection limits
       20: incompatible version
       21: wrong net ID
       22: replaced by new session
addl data :: optional, 0 or more bytes, for future expansion, debugging,
             or reason text.
             Format unspecified and may vary based on reason code.
```
세션 내에서 Charlie에서 Bob으로 또는 Bob에서 Alice로 Data 메시지로 전송되며, Charlie에서 Alice로의 Hole Punch 메시지에서도 전송됩니다. 아래 Relay Process 섹션을 참조하세요.

- 모든 이유가 실제로 사용되는 것은 아니며, 구현에 따라 달라집니다. 대부분의 실패는 일반적으로 연결 종료가 아닌 메시지가 삭제되는 결과를 가져옵니다. 위의 handshake 메시지 섹션의 참고사항을 참조하세요. 나열된 추가 이유들은 일관성, 로깅, 디버깅 또는 정책 변경을 위한 것입니다.
- Termination 블록과 함께 ACK 블록을 포함하는 것을 권장합니다.
- 데이터 단계에서 "termination received" 이외의 다른 이유에 대해서는 피어가 "termination received" 이유와 함께 termination 블록으로 응답해야 합니다.

#### NextNonce

참고사항:

```
+----+----+----+----+----+----+----+----+
|  7 |  size   |flag|       nonce       |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 7
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility

The data below here is covered
by the signature, and Bob forwards it unmodified.

nonce :: 4 bytes, randomly generated by Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
토큰은 Alice가 세션 요청에서 즉시 사용해야 합니다.

- IP 주소는 항상 포함되며(SSU 1과 달리) 세션에 사용된 IP와 다를 수 있습니다.

서명:

Charlie가 동의하거나(응답 코드 0) 거부하면(응답 코드 64 이상), Charlie는 응답에 서명하여 이 블록에 포함시킵니다; Bob은 이를 Relay Response 블록에서 Alice에게 전달합니다. 서명 알고리즘: Charlie의 router 서명 키로 다음 데이터에 서명합니다:

- prologue: 16바이트 "RelayRequestData", null로 종료되지 않음 (메시지에 포함되지 않음)
- bhash: Bob의 32바이트 router 해시 (메시지에 포함되지 않음)
- chash: Charlie의 32바이트 router 해시 (메시지에 포함되지 않음)
- nonce: 4바이트 nonce
- relay tag: 4바이트 relay tag
- timestamp: 4바이트 timestamp (초 단위)
- ver: 1바이트 SSU 버전
- asz: 1바이트 endpoint (포트 + IP) 크기 (6 또는 18)
- AlicePort: 2바이트 Alice의 포트 번호
- Alice IP: (asz - 2)바이트 Alice IP 주소

#### 확인

Bob이 거부하는 경우 (응답 코드 1-63), Bob은 응답에 서명하고 이를 이 블록에 포함합니다. 서명 알고리즘: Bob의 router 서명 키로 다음 데이터에 서명합니다:

```
+----+----+----+----+----+----+----+----+
|  8 |  size   |flag|code|    nonce
+----+----+----+----+----+----+----+----+
     |     timestamp     | ver| csz|Char
+----+----+----+----+----+----+----+----+
 Port|   Charlie IP addr |              |
+----+----+----+----+----+              +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

blk :: 8
size :: 2 bytes, 6
flag :: 1 byte flags, Unused, set to 0 for future compatibility
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, Charlie is banned
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, relay tag not found
       6: rejected by Bob, Alice RI not found
       7-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       71-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD

The data below is covered by the signature if the code is 0 (accept).
Bob forwards it unmodified.

nonce :: 4 bytes, as received from Bob or Alice

The data below is present only if the code is 0 (accept).

timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
csz :: 1 byte endpoint (port + IP) size (0 or 6 or 18)
       may be 0 for some rejection codes
CharliePort :: 2 byte Charlie's port number, big endian
               not present if csz is 0
Charlie IP :: (csz - 2) byte representation of Charlie's IP address,
              network byte order
              not present if csz is 0
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Charlie.
             Not present if rejected by Bob.
token :: Token generated by Charlie for Alice to use
         in the Session Request.
         Only present if code is 0 (accept)
```
세션 내에서 Bob에서 Charlie로 Data 메시지로 전송됩니다. 아래 Relay Process 섹션을 참조하세요.

RouterInfo 블록 또는 Alice의 Router Info를 포함하는 I2NP DatabaseStore 메시지 블록(또는 조각)이 앞서 와야 하며, 이는 동일한 페이로드 내에(공간이 있는 경우) 또는 이전 메시지에 있어야 합니다.

참고사항:

서명:

- prologue: 16바이트 "RelayAgreementOK", null로 종료되지 않음 (메시지에 포함되지 않음)
- bhash: Bob의 32바이트 router 해시 (메시지에 포함되지 않음)
- nonce: 4바이트 nonce
- timestamp: 4바이트 타임스탬프 (초)
- ver: 1바이트 SSU 버전
- csz: 1바이트 엔드포인트 (포트 + IP) 크기 (0 또는 6 또는 18)
- CharliePort: 2바이트 Charlie의 포트 번호 (csz가 0이면 존재하지 않음)
- Charlie IP: (csz - 2)바이트 Charlie IP 주소 (csz가 0이면 존재하지 않음)

Alice가 요청에 서명하고 Bob이 이를 이 블록에서 Charlie에게 전달합니다. 검증 알고리즘: Alice의 router 서명 키로 다음 데이터를 검증합니다:

- prologue: 16바이트 "RelayAgreementOK", null로 종료되지 않음 (메시지에 포함되지 않음)
- bhash: Bob의 32바이트 router 해시 (메시지에 포함되지 않음)
- nonce: 4바이트 nonce
- timestamp: 4바이트 timestamp (초)
- ver: 1바이트 SSU 버전
- csz: 1바이트 = 0

#### 주소

세션 내에서 Data 메시지로 보내지거나, 세션 외에서 Peer Test 메시지로 보내집니다. 아래의 Peer Test Process 섹션을 참조하세요.

메시지 2의 경우, 동일한 페이로드 내에(공간이 있는 경우) 또는 이전 메시지에서 Alice의 Router Info가 포함된 RouterInfo 블록 또는 I2NP DatabaseStore 메시지 블록(또는 단편)이 앞에 와야 합니다.

```
+----+----+----+----+----+----+----+----+
|  9 |  size   |flag|                   |
+----+----+----+----+                   +
|                                       |
+                                       +
|         Alice Router Hash             |
+             32 bytes                  +
|                                       |
+                   +----+----+----+----+
|                   |      nonce        |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 9
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's 32-byte router hash,

The data below here is covered
by the signature, as received from Alice in the Relay Request,
and Bob forwards it unmodified.

nonce :: 4 bytes, as received from Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
메시지 4의 경우, relay가 수락되면 (reason code 0), Charlie의 Router Info를 포함하는 RouterInfo 블록 또는 I2NP DatabaseStore 메시지 블록 (또는 fragment)이 앞에 와야 합니다. 이는 동일한 페이로드 내에 (공간이 있는 경우) 또는 이전 메시지에 포함될 수 있습니다.

- IPv4의 경우, Alice의 IP 주소는 항상 4바이트입니다. Alice가 IPv4를 통해 Charlie에게 연결을 시도하기 때문입니다. IPv6도 지원되며, Alice의 IP 주소는 16바이트일 수 있습니다.
- IPv4의 경우, 이 메시지는 확립된 IPv4 연결을 통해 전송되어야 합니다. 이것이 Bob이 [RelayResponse](#relayresponse)에서 Alice에게 돌려줄 Charlie의 IPv4 주소를 알 수 있는 유일한 방법이기 때문입니다. IPv6도 지원되며, 이 메시지는 확립된 IPv6 연결을 통해 전송될 수 있습니다.
- introducer와 함께 게시되는 모든 SSU 주소는 "caps" 옵션에 "4" 또는 "6"을 포함해야 합니다.

참고사항:

Alice는 테스트하고자 하는 전송 계층(IPv4 또는 IPv6)을 통해 기존 세션을 사용하여 Bob에게 요청을 보냅니다. Bob이 IPv4를 통해 Alice로부터 요청을 받으면, Bob은 IPv4 주소를 광고하는 Charlie를 선택해야 합니다. Bob이 IPv6을 통해 Alice로부터 요청을 받으면, Bob은 IPv6 주소를 광고하는 Charlie를 선택해야 합니다. 실제 Bob-Charlie 통신은 IPv4 또는 IPv6를 통해 이루어질 수 있습니다(즉, Alice의 주소 유형과는 독립적입니다).

- prologue: 16바이트 "RelayRequestData", null로 끝나지 않음 (메시지에 포함되지 않음)
- bhash: Bob의 32바이트 router 해시 (메시지에 포함되지 않음)
- chash: Charlie의 32바이트 router 해시 (메시지에 포함되지 않음)
- nonce: 4바이트 nonce
- relay tag: 4바이트 relay tag
- timestamp: 4바이트 timestamp (초 단위)
- ver: 1바이트 SSU 버전
- asz: 1바이트 엔드포인트 (포트 + IP) 크기 (6 또는 18)
- AlicePort: 2바이트 Alice의 포트 번호
- Alice IP: (asz - 2)바이트 Alice IP 주소

#### Relay Tag 요청

서명:

Alice는 요청에 서명하고 이를 메시지 1에 포함합니다. Bob은 이를 메시지 2에서 Charlie에게 전달합니다. Charlie는 응답에 서명하고 이를 메시지 3에 포함합니다. Bob은 이를 메시지 4에서 Alice에게 전달합니다. 서명 알고리즘: Alice 또는 Charlie의 서명 키로 다음 데이터를 서명하거나 검증합니다:

TODO 키를 순환할 때만

```
+----+----+----+----+----+----+----+----+
| 10 |  size   | msg|code|flag|         |
+----+----+----+----+----+----+         +
| Alice router hash (message 2 only)    |
+             or                        +
| Charlie router hash (message 4 only)  |
+ or all zeros if rejected by Bob       +
| Not present in messages 1,3,5,6,7     |
+                             +----+----+
|                             | ver|
+----+----+----+----+----+----+----+----+
   nonce       |     timestamp     | asz|
+----+----+----+----+----+----+----+----+
|AlicePort|  Alice IP address |         |
+----+----+----+----+----+----+         +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 10
size :: 2 bytes, big endian, size of data to follow
msg :: 1 byte message number 1-7
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, no Charlie available
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, address unsupported
       6-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       70-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD
       reject codes only allowed in messages 3 and 4
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's or Charlie's 32-byte router hash,
        only present in messages 2 and 4.
        All zeros (fake hash) in message 4 if rejected by Bob.

For messages 1-4, the data below here is covered
by the signature, if present, and Bob forwards it unmodified.

ver :: 1 byte SSU version:
       1: SSU 1 (not supported)
       2: SSU 2 (required)
nonce :: 4 byte test nonce, big endian
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice or Charlie.
             Only present for messages 1-4.
             Optional in message 5-7.
```
4바이트 ack through, 그 다음에 ack count와 0개 이상의 nack/ack 범위가 따라옴.

- SSU 1과 달리, 메시지 1에는 Alice의 IP 주소와 포트가 포함되어야 합니다.

- IPv6 주소 테스팅이 지원되며, Bob과 Charlie가 게시된 IPv6 주소에서 'B' capability로 지원을 표시하는 경우 Alice-Bob 및 Alice-Charlie 통신이 IPv6를 통해 이루어질 수 있습니다. 자세한 내용은 Proposal 126을 참조하세요.

이 설계는 QUIC에서 적응되고 단순화되었습니다. 설계 목표는 다음과 같습니다:

- 메시지 1-4는 기존 세션의 Data 메시지에 포함되어야 합니다.

- Bob은 메시지 2를 보내기 전에 Alice의 RI를 Charlie에게 전송해야 합니다.

- Bob은 수락된 경우(이유 코드 0) 메시지 4를 보내기 전에 Charlie의 RI를 Alice에게 보내야 합니다.

- 메시지 5-7은 세션 외부의 Peer Test 메시지에 포함되어야 합니다.

- 메시지 5와 7은 메시지 3과 4에서 전송된 것과 동일한 서명된 데이터를 포함할 수 있거나, 새로운 타임스탬프로 재생성될 수 있습니다. 서명은 선택사항입니다.

- 메시지 6은 메시지 1과 2에서 전송된 것과 동일한 서명된 데이터를 포함할 수 있거나, 새로운 타임스탬프로 재생성될 수 있습니다. 서명은 선택사항입니다.

아래에 명시된 인코딩은 1로 설정된 가장 높은 비트의 번호를 그보다 낮은 연속된 1로 설정된 추가 비트들과 함께 전송함으로써 이러한 설계 목표를 달성합니다. 그 후, 공간이 있다면 연속된 0 비트와 그보다 낮은 연속된 1 비트의 수를 지정하는 하나 이상의 "범위"가 포함됩니다. 더 자세한 배경 정보는 QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) 섹션 13.2.3을 참조하세요.

예시:

- prologue: 16바이트 "PeerTestValidate", null로 종료되지 않음 (메시지에 포함되지 않음)
- bhash: Bob의 32바이트 router 해시 (메시지에 포함되지 않음)
- ahash: Alice의 32바이트 router 해시 (메시지 3과 4의 서명에서만 사용됨; 메시지 3 또는 4에는 포함되지 않음)
- ver: 1바이트 SSU 버전
- nonce: 4바이트 테스트 논스
- timestamp: 4바이트 타임스탬프 (초)
- asz: 1바이트 엔드포인트 (포트 + IP) 크기 (6 또는 18)
- AlicePort: 2바이트 Alice의 포트 번호
- Alice IP: (asz - 2)바이트 Alice IP 주소

#### Relay Tag

패킷 10만 ACK하려고 합니다:

```
+----+----+----+----+----+----+----+----+
| 11 |  size   |      TBD               |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 11
size :: 2 bytes, big endian, size of data to follow
```
#### 새 토큰

패킷 8-10만 ACK하려고 합니다:

우리는 10 9 8 6 5 2 1 0을 ACK하고, 7 4 3을 NACK하려고 합니다. ACK Block의 인코딩은 다음과 같습니다:

- 승인된 패킷을 나타내는 비트 시퀀스인 "bitfield"를 효율적으로 인코딩하고자 합니다.
- bitfield는 대부분 1로 구성됩니다. 1과 0 모두 일반적으로 순차적인 "덩어리"로 나타납니다.
- 패킷에서 승인에 사용할 수 있는 공간의 양은 다양합니다.
- 가장 중요한 비트는 가장 높은 번호의 비트입니다. 낮은 번호의 비트들은 덜 중요합니다. 가장 높은 비트에서 일정 거리 이하의 가장 오래된 비트들은 "잊혀져서" 다시는 전송되지 않습니다.

참고 사항:

```
+----+----+----+----+----+----+----+----+
| 12 |  size   |    Ack Through    |acnt|
+----+----+----+----+----+----+----+----+
|  range  |  range  |     .   .   .     |
+----+----+----+----+                   +
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 12
size :: 2 bytes, big endian, size of data to follow,
        5 minimum
ack through :: highest packet number acked
acnt :: number of acks lower than ack through also acked,
        0-255
range :: If present,
         1 byte nack count followed by 1 byte ack count,
         0-255 each
```
2바이트 포트와 4바이트 또는 16바이트 IP 주소. Bob이 Alice에게 보내는 Alice의 주소, 또는 Alice가 Bob에게 보내는 Bob의 주소.

이는 Alice가 Session Request, Session Confirmed, 또는 Data 메시지에서 보낼 수 있습니다. Session Created 메시지에서는 지원되지 않는데, 이는 Bob이 아직 Alice의 RI를 가지고 있지 않으며, Alice가 relay를 지원하는지 알지 못하기 때문입니다. 또한, Bob이 들어오는 연결을 받고 있다면, 그는 아마도 introducer가 필요하지 않을 것입니다 (다른 유형인 ipv4/ipv6의 경우는 제외).

- Ack Through: 10
- acnt: 0
- 범위가 포함되지 않음

Session Request에서 전송될 때, Bob은 Session Created 메시지에서 Relay Tag로 응답할 수 있거나, Session Confirmed에서 Alice의 RouterInfo를 받아 Alice의 신원을 검증한 후 Data 메시지로 응답하기까지 기다리도록 선택할 수 있습니다. Bob이 Alice를 위해 릴레이하고 싶지 않다면, Relay Tag 블록을 전송하지 않습니다.

- Ack Through: 10
- acnt: 2
- 범위가 포함되지 않음

이것은 Alice의 Relay Tag Request에 대한 응답으로 Bob이 Session Confirmed 또는 Data 메시지로 보낼 수 있습니다.

- Ack Through: 10
- acnt: 2 (ack 9 8)
- range: 1 2 (nack 7, ack 6 5)
- range: 2 3 (nack 4 3, ack 2 1 0)

Relay Tag Request가 Session Request에서 전송되면, Bob은 Session Created 메시지에서 Relay Tag로 응답하거나, Session Confirmed에서 Alice의 RouterInfo를 받아 Alice의 신원을 검증한 후 Data 메시지로 응답하기를 선택할 수 있습니다. Bob이 Alice를 위해 릴레이하고 싶지 않다면, Relay Tag 블록을 전송하지 않습니다.

- 범위가 없을 수도 있습니다. 범위의 최대 개수는 지정되지 않으며, 패킷에 들어갈 수 있는 만큼 많을 수 있습니다.
- 255개 이상의 연속 패킷을 ack하는 경우 Range nack가 0일 수 있습니다.
- 255개 이상의 연속 패킷을 nack하는 경우 Range ack가 0일 수 있습니다.
- Range nack와 ack 모두 0일 수는 없습니다.
- 마지막 범위 이후의 패킷들은 ack되지도 nack되지도 않습니다. ack 블록의 길이와 오래된 ack/nack 처리 방법은 ack 블록을 보내는 측에 달려 있습니다. 논의는 아래 ack 섹션을 참조하십시오.
- ack through는 수신된 가장 높은 패킷 번호여야 하며, 더 높은 패킷들은 수신되지 않았습니다. 그러나 제한적인 상황에서는 "구멍을 메우는" 단일 패킷을 ack하거나 모든 수신된 패킷의 상태를 유지하지 않는 단순화된 구현과 같은 경우에는 더 낮을 수 있습니다. 최고 수신 패킷 위의 패킷들은 ack되지도 nack되지도 않지만, 여러 ack 블록 이후에는 빠른 재전송 모드로 들어가는 것이 적절할 수 있습니다.
- 이 형식은 QUIC의 단순화된 버전입니다. 대량의 ACK와 버스트 형태의 NACK를 효율적으로 인코딩하도록 설계되었습니다.
- ACK 블록은 데이터 단계 패킷을 acknowledge하는 데 사용됩니다. 세션 내 데이터 단계 패킷에 대해서만 포함되어야 합니다.

#### 경로 챌린지

후속 연결을 위한 것입니다. 일반적으로 Session Created 및 Session Confirmed 메시지에 포함됩니다. 이전 토큰이 만료된 경우 장기간 지속되는 세션의 Data 메시지에서 다시 전송될 수도 있습니다.

```
+----+----+----+----+----+----+----+----+
| 13 | 6 or 18 |   Port  | IP Address    
+----+----+----+----+----+----+----+----+
     |
+----+

blk :: 13
size :: 2 bytes, big endian, 6 or 18
port :: 2 bytes, big endian
ip :: 4 byte IPv4 or 16 byte IPv6 address,
      big endian (network byte order)
```
#### 경로 응답

Path Response에서 반환될 임의 데이터가 포함된 Ping으로, 연결 유지 또는 IP/포트 변경 검증에 사용됩니다.

참고 사항:

```
+----+----+----+
| 15 |    0    |
+----+----+----+

blk :: 15
size :: 2 bytes, big endian, value = 0
```
#### 첫 번째 패킷 번호

Path Challenge에서 받은 데이터와 함께 Path Challenge에 대한 응답으로 보내는 Pong으로, keep-alive 또는 IP/Port 변경 검증에 사용됩니다.

각 방향의 핸드셰이크에 선택적으로 포함되며, 전송될 첫 번째 패킷 번호를 지정합니다. 이는 TCP와 유사하게 헤더 암호화에 더 많은 보안을 제공합니다.

```
+----+----+----+----+----+----+----+
| 16 |    4    |    relay tag      |
+----+----+----+----+----+----+----+

blk :: 16
size :: 2 bytes, big endian, value = 4
relay tag :: 4 bytes, big endian, nonzero
```
#### 혼잡

완전히 명세되지 않았으며, 현재 지원되지 않습니다.

```
+----+----+----+----+----+----+----+----+
| 17 |   12    |     expires       |
+----+----+----+----+----+----+----+----+
                token              |
+----+----+----+----+----+----+----+

blk :: 17
size :: 2 bytes, big endian, value = 12
expires :: Unix timestamp, unsigned seconds.
           Wraps around in 2106
token :: 8 bytes, big endian
```
#### 패딩

이 블록은 혼잡 제어 정보를 교환하기 위한 확장 가능한 방법으로 설계되었습니다. 혼잡 제어는 복잡할 수 있으며, 실시간 테스트에서 프로토콜에 대한 더 많은 경험을 쌓거나 전면 배포 후에 발전할 수 있습니다.

```
+----+----+----+----+----+----+----+----+
| 18 |  size   |    Arbitrary Data      |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 18
size :: 2 bytes, big endian, size of data to follow
data :: Arbitrary data to be returned in a Path Response
        length as selected by sender
```
이는 플래그가 할당될 공간이 없는 고사용량 I2NP, First Fragment, Followon Fragment, ACK 블록에서 혼잡 정보를 제외시킵니다. Data 패킷 헤더에 3바이트의 미사용 플래그가 있지만, 이 역시 확장성을 위한 제한된 공간을 제공하며 암호화 보호 기능이 약합니다.

- 무작위 데이터를 포함하는 최소 8바이트의 데이터 크기가 권장되지만 필수는 아닙니다.
- 최대 크기는 명시되지 않았지만, 경로 검증 단계에서 PMTU가 1280이므로 1280보다 훨씬 작아야 합니다.
- 큰 challenge 크기는 패킷 증폭 공격의 벡터가 될 수 있으므로 권장되지 않습니다.

#### 피어 주소 스푸핑

2비트 정보를 위해 4바이트 블록을 사용하는 것은 다소 낭비적이지만, 이를 별도의 블록에 두면 현재 윈도우 크기, 측정된 RTT, 또는 기타 플래그와 같은 추가 데이터로 쉽게 확장할 수 있습니다. 경험에 따르면 플래그 비트만으로는 고급 혼잡 제어 방식의 구현에 종종 불충분하고 어색합니다. 예를 들어 ACK 블록에서 가능한 모든 혼잡 제어 기능에 대한 지원을 추가하려고 하면 공간이 낭비되고 해당 블록의 파싱에 복잡성이 추가됩니다.

```
+----+----+----+----+----+----+----+----+
| 19 |  size   |                        |
+----+----+----+                        +
|    Data received in Path Challenge    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 19
size :: 2 bytes, big endian, size of data to follow
data :: As received in a Path Challenge
```
#### 경로상 주소 스푸핑

구현체들은 이 사양의 향후 버전에서 구현이 요구되지 않는 한, 다른 router가 여기에 포함된 특정 플래그 비트나 기능을 지원한다고 가정해서는 안 됩니다.

이 블록은 아마도 페이로드에서 패딩이 아닌 마지막 블록이어야 합니다.

```
+----+----+----+----+----+----+----+
| 20 |  size   |  First pkt number |
+----+----+----+----+----+----+----+

blk :: 20
size :: 4
pkt num :: The first packet number to be sent in the data phase
```
#### 오프패스 패킷 포워딩

이는 AEAD 페이로드 내부의 패딩을 위한 것입니다. 모든 메시지의 패딩은 AEAD 페이로드 내부에 있습니다.

패딩은 협상된 매개변수를 대략적으로 준수해야 합니다. Bob은 Session Created에서 요청된 tx/rx 최소/최대 매개변수를 보냈습니다. Alice는 Session Confirmed에서 요청된 tx/rx 최소/최대 매개변수를 보냈습니다. 업데이트된 옵션은 데이터 단계 중에 전송될 수 있습니다. 위의 옵션 블록 정보를 참조하세요.

존재할 경우, 이는 페이로드의 마지막 블록이어야 합니다.

참고사항:

SSU2는 공격자가 재생하는 메시지의 영향을 최소화하도록 설계되었습니다.

```
+----+----+----+----+
| 21 |  size   |flag|
+----+----+----+----+

blk :: 21
size :: 1 (or more if extended)
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 1 to request immediate ack
       bit 1: 1 for explicit congestion notification (ECN)
       bits 7-2: Unused, set to 0 for future compatibility
```
#### 프라이버시 영향

Token Request, Retry, Session Request, Session Created, Hole Punch, 그리고 out-of-session Peer Test 메시지는 DateTime 블록을 포함해야 합니다.

Alice와 Bob 모두 이러한 메시지의 시간이 유효한 편차 범위 내에 있는지 검증합니다(권장 사항: +/- 2분). "probing resistance"를 위해 Bob은 편차가 유효하지 않은 경우 Token Request 또는 Session Request 메시지에 응답하지 않아야 합니다. 이러한 메시지들은 재전송 공격이나 probing 공격일 수 있기 때문입니다.

Bob은 skew가 유효하더라도 Bloom filter나 다른 메커니즘을 통해 중복된 Token Request 및 Retry 메시지를 거부하도록 선택할 수 있습니다. 하지만 이러한 메시지에 응답하는 데 필요한 크기와 CPU 비용은 낮습니다. 최악의 경우, 재생된 Token Request 메시지가 이전에 전송된 토큰을 무효화할 수 있습니다.

```
+----+----+----+----+----+----+----+----+
|254 |  size   |      padding           |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 254
size :: 2 bytes, big endian, size of padding to follow
padding :: random data
```
토큰 시스템은 재전송된 Session Request 메시지의 영향을 크게 최소화합니다. 토큰은 한 번만 사용할 수 있으므로, 재전송된 Session Request 메시지는 절대 유효한 토큰을 가질 수 없습니다. Bob은 skew가 유효하더라도 Bloom filter나 기타 메커니즘을 통해 중복된 Session Request 메시지를 거부하도록 선택할 수 있습니다. 그러나 Retry 메시지로 응답하는 데 드는 크기와 CPU 비용은 낮습니다. 최악의 경우, Retry 메시지를 보내는 것이 이전에 전송된 토큰을 무효화할 수 있습니다.

- Size = 0은 허용됩니다.
- 패딩 전략은 TBD입니다.
- 최소 패딩은 TBD입니다.
- 패딩 전용 페이로드가 허용됩니다.
- 패딩 기본값은 TBD입니다.
- 패딩 매개변수 협상은 옵션 블록을 참조하세요
- 최소/최대 패딩 매개변수는 옵션 블록을 참조하세요
- MTU를 초과하지 마세요. 더 많은 패딩이 필요한 경우 여러 메시지를 전송하세요.
- 협상된 패딩 위반에 대한 router 응답은 구현에 따라 달라집니다.
- 패딩 길이는 메시지별로 결정되고 길이 분포 추정에 따라 결정되거나, 랜덤 지연이 추가되어야 합니다. 이러한 대응책은 DPI에 저항하기 위해 포함되어야 하며, 그렇지 않으면 메시지 크기가 전송 프로토콜에서 I2P 트래픽이 전달되고 있음을 드러낼 수 있습니다. 정확한 패딩 방식은 향후 작업 영역이며, [NTCP2](/docs/specs/ntcp2)의 부록 A에서 이 주제에 대한 자세한 정보를 제공합니다.

## 재생 공격 방지

중복된 Session Created 및 Session Confirmed 메시지는 Noise handshake 상태가 이를 복호화할 올바른 상태에 있지 않기 때문에 검증되지 않습니다. 최악의 경우, 피어는 명백한 중복 Session Created에 대한 응답으로 Session Confirmed를 재전송할 수 있습니다.

재전송된 Hole Punch 및 Peer Test 메시지는 거의 또는 전혀 영향을 미치지 않아야 합니다.

Router는 데이터 메시지 패킷 번호를 사용하여 중복된 데이터 단계 메시지를 감지하고 폐기해야 합니다. 각 패킷 번호는 한 번만 사용되어야 합니다. 재생된 메시지는 무시되어야 합니다.

Alice가 Session Created 또는 Retry를 받지 못한 경우:

동일한 소스 및 연결 ID, 임시 키, 그리고 패킷 번호 0을 유지하세요. 또는 동일한 암호화된 패킷을 유지하고 재전송하세요. 패킷 번호는 증가시키면 안 됩니다. 이는 Session Created 메시지를 암호화하는 데 사용되는 체인 해시 값을 변경하기 때문입니다.

권장 재전송 간격: 1.25, 2.5, 5초 (첫 전송 후 1.25, 3.75, 8.75초). 권장 타임아웃: 총 15초

Bob이 Session Confirmed를 받지 못한 경우:

동일한 소스 및 연결 ID, 임시 키, 그리고 패킷 번호 0을 유지하세요. 또는 암호화된 패킷을 그대로 보관하세요. 패킷 번호는 증가시키면 안 됩니다. 왜냐하면 이는 Session Confirmed 메시지를 암호화하는 데 사용되는 연쇄 해시 값을 변경하기 때문입니다.

## 핸드셰이크 재전송

### 세션 생성됨

권장 재전송 간격: 1, 2, 4초 (첫 전송 후 1, 3, 7초). 권장 타임아웃: 총 12초

SSU 1에서 Alice는 Bob으로부터 첫 번째 데이터 패킷을 받을 때까지 데이터 단계로 전환하지 않습니다. 이로 인해 SSU 1은 2라운드 트립 설정이 됩니다.

SSU 2의 경우, 권장되는 Session Confirmed 재전송 간격: 1.25초, 2.5초, 5초 (첫 전송 후 1.25초, 3.75초, 8.75초).

### 세션 확인됨

몇 가지 대안이 있습니다. 모두 1 RTT입니다:

1) Alice는 Session Confirmed가 수신되었다고 가정하고, 데이터 메시지를 즉시 전송하며, Session Confirmed를 재전송하지 않습니다. 순서가 맞지 않게 수신된 데이터 패킷(Session Confirmed 이전에 수신된)은 복호화할 수 없지만, 재전송됩니다. Session Confirmed가 손실되면 전송된 모든 데이터 메시지가 드롭됩니다. 2) 1)과 같이 데이터 메시지를 즉시 전송하지만, 데이터 메시지가 수신될 때까지 Session Confirmed도 재전송합니다. 3) 핸드셰이크에서 2개의 메시지만 사용하는 IK를 XK 대신 사용할 수 있지만, 추가 DH(3개 대신 4개)를 사용합니다.

권장되는 구현은 옵션 2)입니다. Alice는 Session Confirmed 메시지를 재전송하는 데 필요한 정보를 보유해야 합니다. Alice는 또한 Session Confirmed 메시지가 재전송된 후 모든 Data 메시지를 재전송해야 합니다.

### 토큰 요청

Session Confirmed를 재전송할 때는 동일한 소스 및 연결 ID, ephemeral key, 패킷 번호 1을 유지하세요. 또는 암호화된 패킷을 그대로 보관하세요. 패킷 번호는 증가시키면 안 됩니다. 이는 split() 함수의 입력값인 체인 해시 값을 변경하기 때문입니다.

Bob은 Session Confirmed 메시지를 받기 전에 수신된 데이터 메시지를 보관(큐잉)할 수 있습니다. Session Confirmed 메시지를 받기 전까지는 헤더 보호 키와 복호화 키를 모두 사용할 수 없으므로, Bob은 그것들이 데이터 메시지라는 것을 알 수 없지만 추정할 수는 있습니다. Session Confirmed 메시지를 받은 후, Bob은 큐에 저장된 데이터 메시지를 복호화하고 처리할 수 있습니다. 이것이 너무 복잡하다면, Bob은 복호화할 수 없는 데이터 메시지를 그냥 드롭할 수 있습니다. Alice가 이를 재전송할 것이기 때문입니다.

참고: 세션 확인 패킷이 손실되면, Bob은 session created를 재전송합니다. session created 헤더는 Bob의 intro key로 설정되므로 Alice의 intro key로는 복호화할 수 없습니다 (Bob의 intro key로 fallback 복호화를 수행하지 않는 한). Bob은 이전에 ack되지 않았고 복호화할 수 없는 패킷이 수신된 경우, session confirmed 패킷을 즉시 재전송할 수 있습니다.

Alice가 Retry를 받지 못한 경우:

동일한 소스 및 연결 ID를 유지합니다. 구현체는 새로운 랜덤 패킷 번호를 생성하고 새 패킷을 암호화할 수 있습니다. 또는 동일한 패킷 번호를 재사용하거나 단순히 동일한 암호화된 패킷을 보관하고 재전송할 수 있습니다. 패킷 번호는 증가시키면 안 됩니다. 이는 Session Created 메시지를 암호화하는 데 사용되는 연쇄 해시 값을 변경하게 되기 때문입니다.

권장 재전송 간격: 3초 및 6초 (첫 전송 후 3초 및 9초). 권장 타임아웃: 총 15초

Bob이 Session Confirmed를 받지 못한 경우:

Retry 메시지는 타임아웃 시 재전송되지 않으며, 이는 스푸핑된 소스 주소의 영향을 줄이기 위함입니다.

### 다시 시도

그러나 Retry 메시지는 원래의 (유효하지 않은) 토큰과 함께 반복된 Session Request 메시지가 수신되거나, 반복된 Token Request 메시지에 대한 응답으로 재전송될 수 있습니다. 두 경우 모두 Retry 메시지가 손실되었음을 나타냅니다.

다른 토큰이지만 여전히 유효하지 않은 토큰을 가진 두 번째 Session Request 메시지가 수신되면, 대기 중인 세션을 삭제하고 응답하지 않습니다.

Retry 메시지를 재전송하는 경우: 동일한 소스 및 연결 ID와 토큰을 유지합니다. 구현체는 새로운 랜덤 패킷 번호를 생성하고 새 패킷을 암호화할 수 있습니다. 또는 동일한 패킷 번호를 재사용하거나 동일한 암호화된 패킷을 그대로 유지하고 재전송할 수 있습니다.

### 전체 타임아웃

handshake에 대한 권장 총 타임아웃은 20초입니다.

세 개의 Noise 핸드셰이크 메시지인 Session Request, Session Created, Session Confirmed의 중복은 헤더의 MixHash() 이전에 감지되어야 합니다. 그 이후에 Noise AEAD 처리가 실패할 것으로 예상되지만, 핸드셰이크 해시는 이미 손상되었을 것입니다.

세 개의 메시지 중 하나라도 손상되어 AEAD가 실패하면, 손상된 메시지에 대해 이미 MixHash()가 호출되었기 때문에 재전송을 하더라도 핸드셰이크를 복구할 수 없습니다.

Session Request 헤더의 토큰은 DoS 완화, 소스 주소 스푸핑 방지, 그리고 재전송 공격에 대한 저항성을 위해 사용됩니다.

Bob이 Session Request 메시지의 토큰을 받아들이지 않으면, Bob은 메시지를 복호화하지 않습니다. 이는 비용이 많이 드는 DH 연산이 필요하기 때문입니다. Bob은 단순히 새로운 토큰과 함께 Retry 메시지를 보냅니다.

### 중복 및 오류 처리

해당 토큰과 함께 후속 Session Request 메시지가 수신되면, Bob은 해당 메시지를 복호화하고 핸드셰이크를 진행합니다.

### 패킷 번호

토큰은 토큰 생성기가 값들과 관련된 IP 및 포트를 저장하는 경우(메모리 또는 영구적으로), 무작위로 생성된 8바이트 값이어야 합니다. 생성기는 불투명한 값을 생성해서는 안 됩니다. 예를 들어, IP, 포트, 현재 시간 또는 일의 SipHash(비밀 시드 K0, K1 사용)를 사용하여 메모리에 저장할 필요가 없는 토큰을 생성하는 것은, 이 방법이 재사용된 토큰과 재생 공격을 거부하기 어렵게 만들기 때문입니다. 그러나 [WireGuard](https://www.wireguard.com/papers/wireguard.pdf)가 서버 비밀과 IP 주소의 16바이트 HMAC를 사용하는 것처럼, 그러한 방식으로 마이그레이션할 수 있는지는 추가 연구가 필요한 주제입니다.

토큰은 한 번만 사용할 수 있습니다. Retry 메시지에서 Bob이 Alice에게 보낸 토큰은 즉시 사용되어야 하며, 몇 초 후에 만료됩니다. 설정된 세션에서 New Token 블록으로 전송된 토큰은 후속 연결에서 사용할 수 있으며, 해당 블록에서 지정된 시간에 만료됩니다. 만료 시간은 송신자가 지정하며, 저장된 토큰의 원하는 최대 오버헤드에 따라 최소 몇 분에서 최대 1시간 이상의 값을 권장합니다.

## 토큰

router의 IP 또는 포트가 변경되면, 이전 IP 또는 포트에 대해 저장된 모든 토큰(인바운드 및 아웃바운드 모두)을 삭제해야 합니다. 이는 더 이상 유효하지 않기 때문입니다. 토큰은 구현에 따라 router 재시작 시에도 선택적으로 유지될 수 있습니다. 만료되지 않은 토큰의 수락이 보장되지는 않습니다. Bob이 저장된 토큰을 잊어버리거나 삭제했다면, Alice에게 Retry를 보낼 것입니다. router는 토큰 저장 용량을 제한하기로 선택할 수 있으며, 만료되지 않았더라도 가장 오래된 저장된 토큰을 제거할 수 있습니다.

새로운 토큰 블록은 Alice에서 Bob으로 또는 Bob에서 Alice로 전송될 수 있습니다. 일반적으로 세션 설정 중이나 직후에 최소 한 번은 전송됩니다. Session Confirmed 메시지에서 RouterInfo의 유효성 검사로 인해 Bob은 Session Created 메시지에서 New Token 블록을 전송해서는 안 되며, Session Confirmed가 수신되고 검증된 후 ACK 0 및 Router Info와 함께 전송될 수 있습니다.

세션 수명이 토큰 만료보다 종종 더 길기 때문에, 새로운 만료 시간과 함께 만료 전후에 토큰을 다시 전송하거나 새로운 토큰을 전송해야 합니다. Router들은 마지막으로 받은 토큰만 유효하다고 가정해야 합니다. 동일한 IP/포트에 대해 여러 개의 인바운드 또는 아웃바운드 토큰을 저장할 필요는 없습니다.

토큰은 소스 IP/포트와 목적지 IP/포트의 조합에 바인딩됩니다. IPv4에서 수신된 토큰은 IPv6에서 사용될 수 없으며, 그 반대의 경우도 마찬가지입니다.

세션 중에 어느 한 peer가 새로운 IP나 포트로 마이그레이션하는 경우(Connection Migration 섹션 참조), 이전에 교환된 모든 토큰은 무효화되며, 새로운 토큰을 교환해야 합니다.

구현체는 토큰을 디스크에 저장하고 재시작 시 다시 로드할 수 있지만 필수는 아닙니다. 지속적으로 저장하는 경우, 구현체는 토큰을 다시 로드하기 전에 종료 이후 IP와 포트가 변경되지 않았는지 확인해야 합니다.

SSU 1과의 차이점

참고: SSU 1에서와 같이, 초기 fragment는 전체 fragment 수나 전체 길이에 대한 정보를 포함하지 않습니다. 후속 fragment들은 자신의 오프셋에 대한 정보를 포함하지 않습니다. 이는 송신자에게 패킷 내 사용 가능한 공간에 따라 "즉석에서" fragment하는 유연성을 제공합니다. (Java I2P는 이렇게 하지 않으며, 첫 번째 fragment가 전송되기 전에 "사전 fragment"를 수행합니다) 하지만 이는 수신자에게 순서가 맞지 않게 수신된 fragment들을 저장하고 모든 fragment가 수신될 때까지 재조립을 지연시켜야 하는 부담을 줍니다.

SSU 1에서와 마찬가지로, 프래그먼트의 재전송은 이전 전송에서의 프래그먼트 길이(및 암시적 오프셋)를 보존해야 합니다.

SSU 2는 처리 효율성을 향상시키기 위해 세 가지 경우(전체 메시지, 초기 fragment, 후속 fragment)를 세 개의 서로 다른 블록 유형으로 분리합니다.

이 프로토콜은 I2NP 메시지의 중복 전달을 완전히 방지하지는 않습니다. IP 계층의 중복이나 재전송 공격은 SSU2 계층에서 감지될 것입니다. 각 패킷 번호는 한 번만 사용될 수 있기 때문입니다.

## I2NP 메시지 단편화

하지만 I2NP 메시지나 조각들이 새로운 패킷으로 재전송될 때는 SSU2 계층에서 이를 감지할 수 없습니다. router는 I2NP 만료 시간(너무 오래된 것과 너무 미래의 것 모두)을 강제해야 하고, I2NP 메시지 ID를 기반으로 한 Bloom 필터나 다른 메커니즘을 사용해야 합니다.

router나 SSU2 구현에서는 중복을 탐지하기 위해 추가적인 메커니즘을 사용할 수 있습니다. 예를 들어, SSU2는 최근에 수신된 메시지 ID의 캐시를 유지할 수 있습니다. 이는 구현에 따라 달라집니다.

이 규격은 패킷 번호 매기기와 ACK 블록에 대한 프로토콜을 명시합니다. 이는 송신자가 효율적이고 반응성 있는 혼잡 제어 알고리즘을 구현할 수 있도록 충분한 실시간 정보를 제공하는 동시에, 해당 구현에서 유연성과 혁신을 허용합니다. 이 섹션에서는 구현 목표를 논의하고 제안사항을 제공합니다. 일반적인 지침은 [RFC-9002](https://tools.ietf.org/html/rfc9002)에서 찾을 수 있습니다. 재전송 타이머에 대한 지침은 [RFC-6298](https://tools.ietf.org/html/rfc6298)도 참조하시기 바랍니다.

ACK 전용 데이터 패킷은 전송 중인 바이트나 패킷 수에 포함되어서는 안 되며 혼잡 제어를 받지 않습니다. TCP와 달리 SSU2는 이러한 패킷의 손실을 감지할 수 있으며, 이 정보는 혼잡 상태를 조정하는 데 사용될 수 있습니다. 하지만 이 문서는 그러한 메커니즘을 명시하지 않습니다.

## I2NP 메시지 중복

일부 다른 비데이터 블록을 포함하는 패킷들도 원하는 경우 혼잡 제어에서 제외될 수 있으며, 이는 구현에 따라 달라집니다. 예를 들어:

혼잡 제어는 TCP RFC와 QUIC [RFC-9002](https://tools.ietf.org/html/rfc9002)의 지침에 따라 패킷 수가 아닌 바이트 수를 기반으로 하는 것이 권장됩니다. 구현에 따라 커널이나 중간 장비에서 버퍼 오버플로우를 방지하기 위해 추가적인 패킷 수 제한이 유용할 수도 있지만, 이는 상당한 복잡성을 추가할 수 있습니다. 세션별 및/또는 전체 패킷 출력이 대역폭 제한 및/또는 속도 조절되는 경우, 패킷 수 제한의 필요성을 완화할 수 있습니다.

SSU 1에서는 ACK와 NACK가 I2NP 메시지 번호와 프래그먼트 비트마스크를 포함했습니다. 전송자는 아웃바운드 메시지(및 해당 프래그먼트)의 ACK 상태를 추적하고 필요에 따라 프래그먼트를 재전송했습니다.

## 혼잡 제어

SSU 2에서 ACK와 NACK은 패킷 번호를 포함합니다. 송신자는 패킷 번호와 그 내용의 매핑을 가진 데이터 구조를 유지해야 합니다. 패킷이 ACK되거나 NACK될 때, 송신자는 해당 패킷에 어떤 I2NP 메시지와 프래그먼트가 있었는지 확인하여 무엇을 재전송할지 결정해야 합니다.

Bob은 패킷 0의 ACK를 전송하여 Session Confirmed 메시지를 확인하고 Alice가 데이터 단계로 진행할 수 있도록 하며, 재전송 가능성을 위해 저장되어 있던 큰 Session Confirmed 메시지를 폐기할 수 있게 합니다. 이는 SSU 1에서 Bob이 전송했던 DeliveryStatusMessage를 대체합니다.

Bob은 Session Confirmed 메시지를 수신한 후 가능한 한 빨리 ACK를 보내야 합니다. 작은 지연(50ms 이하)은 허용되는데, 이는 Session Confirmed 메시지 직후 거의 즉시 적어도 하나의 Data 메시지가 도착해야 하므로 ACK가 Session Confirmed와 Data 메시지를 모두 확인응답할 수 있기 때문입니다. 이렇게 하면 Bob이 Session Confirmed 메시지를 재전송하지 않아도 됩니다.

- Peer Test
- 릴레이 요청/소개/응답
- 경로 챌린지/응답

정의: Ack-eliciting 패킷: ack-eliciting 블록을 포함하는 패킷은 최대 확인응답 지연 시간 내에 수신자로부터 ACK를 유도하며, 이러한 패킷을 ack-eliciting 패킷이라고 합니다.

### 세션 확인 ACK

Router들은 수신하고 처리하는 모든 패킷을 확인응답합니다. 그러나 ack-eliciting 패킷만이 최대 ack 지연 시간 내에 ACK 블록이 전송되도록 합니다. Ack-eliciting이 아닌 패킷들은 다른 이유로 ACK 블록이 전송될 때만 확인응답됩니다.

어떤 이유로든 패킷을 전송할 때, 엔드포인트는 최근에 전송되지 않았다면 ACK 블록을 포함하도록 시도해야 합니다. 이렇게 하면 피어에서 적시에 손실을 감지하는 데 도움이 됩니다.

### ACK 생성하기

일반적으로 수신자로부터의 빈번한 피드백은 손실 및 혼잡 응답을 개선하지만, 이는 모든 ack-eliciting 패킷에 대해 ACK 블록을 보내는 수신자가 생성하는 과도한 부하와 균형을 맞춰야 합니다. 아래에서 제공하는 지침은 이러한 균형을 맞추고자 합니다.

다음을 제외한 모든 블록을 포함하는 세션 내 데이터 패킷은 ack를 유발합니다:

### 핸드셰이크 ACK

핸드셰이크 메시지와 피어 테스트 메시지 5-7을 포함한 세션 외 패킷들은 자체적인 승인 메커니즘을 가지고 있습니다. 아래를 참조하세요.

다음은 특수한 경우들입니다:

ACK 블록은 데이터 단계 패킷을 확인응답하는 데 사용됩니다. 세션 내 데이터 단계 패킷에 대해서만 포함되어야 합니다.

모든 패킷은 적어도 한 번은 확인응답을 받아야 하며, ack-eliciting 패킷은 최대 지연 시간 내에 적어도 한 번은 확인응답을 받아야 합니다.

엔드포인트는 다음 예외를 제외하고 모든 ack-eliciting 핸드셰이크 패킷을 최대 지연 시간 내에 즉시 확인응답해야 합니다. 핸드셰이크 확인 이전에는 엔드포인트가 패킷을 수신할 때 패킷을 복호화하는 데 필요한 패킷 헤더 암호화 키를 가지고 있지 않을 수 있습니다. 따라서 패킷을 버퍼링하고 필요한 키를 사용할 수 있게 되면 확인응답할 수 있습니다.

- ACK 블록
- 주소 블록
- DateTime 블록
- 패딩 블록
- 종료 블록
- 기타?

ACK 블록만 포함된 패킷은 혼잡 제어되지 않으므로, 엔드포인트는 ack-eliciting 패킷을 수신하는 것에 대한 응답으로 그러한 패킷을 두 개 이상 전송해서는 안 됩니다.

### ACK 블록 전송

endpoint는 수신된 패킷 이전에 패킷 간격이 있더라도 non-ack-eliciting 패킷에 대한 응답으로 non-ack-eliciting 패킷을 보내서는 안 됩니다. 이는 연결이 유휴 상태가 되는 것을 방해할 수 있는 확인응답의 무한 피드백 루프를 방지합니다. Non-ack-eliciting 패킷들은 endpoint가 다른 이벤트에 응답하여 ACK 블록을 보낼 때 결국 확인응답됩니다.

- Token Request는 Retry에 의해 암묵적으로 확인됨
- Session Request는 Session Created 또는 Retry에 의해 암묵적으로 확인됨
- Retry는 Session Request에 의해 암묵적으로 확인됨
- Session Created는 Session Confirmed에 의해 암묵적으로 확인됨
- Session Confirmed는 즉시 확인되어야 함

### ACK 빈도

ACK 블록만 전송하는 endpoint는 해당 확인응답이 ack-eliciting 블록을 포함한 패킷에 포함되지 않는 한 피어로부터 확인응답을 받지 못합니다. endpoint는 확인응답해야 할 새로운 ack-eliciting 패킷이 있을 때 다른 블록과 함께 ACK 블록을 전송해야 합니다. non-ack-eliciting 패킷만 확인응답해야 하는 경우, endpoint는 ack-eliciting 패킷을 받을 때까지 나가는 블록과 함께 ACK 블록을 전송하지 않을 수 있습니다.

ack-eliciting이 아닌 패킷만을 전송하는 엔드포인트는 확인 응답을 받을 수 있도록 해당 패킷에 ack-eliciting 블록을 가끔 추가하는 것을 선택할 수 있습니다. 이 경우, 확인 응답의 무한 피드백 루프를 방지하기 위해 엔드포인트는 원래 non-ack-eliciting이었을 모든 패킷에 ack-eliciting 블록을 전송해서는 안 됩니다(MUST NOT).

송신자의 손실 감지를 돕기 위해, 엔드포인트는 다음 중 어느 경우에서든 ACK 유발 패킷을 수신했을 때 지연 없이 ACK 블록을 생성하고 전송해야 합니다:

알고리즘들은 위에서 제시된 지침을 따르지 않는 수신자들에 대해서도 복원력을 가질 것으로 예상됩니다. 그러나 구현체는 엔드포인트가 만드는 연결과 네트워크의 다른 사용자들에 대한 변경의 성능 영향을 신중히 고려한 후에만 이러한 요구사항에서 벗어나야 합니다.

수신자는 ack-eliciting 패킷에 대한 응답으로 확인응답을 얼마나 자주 보낼지 결정합니다. 이러한 결정에는 상충관계가 포함됩니다.

엔드포인트는 손실을 감지하기 위해 적시에 수신확인에 의존합니다. 윈도우 기반 혼잡 제어기는 혼잡 윈도우를 관리하기 위해 수신확인에 의존합니다. 두 경우 모두 수신확인을 지연시키면 성능에 악영향을 미칠 수 있습니다.

반면에 확인응답만 전달하는 패킷의 빈도를 줄이면 양쪽 엔드포인트에서 패킷 전송 및 처리 비용이 감소합니다. 이는 심각하게 비대칭인 링크에서 연결 처리량을 개선할 수 있고, 역방향 경로 용량을 사용하는 확인응답 트래픽의 양을 줄일 수 있습니다. [RFC-3449](https://tools.ietf.org/html/rfc3449)의 섹션 3을 참조하세요.

수신자는 최소 두 개의 ACK 유발 패킷을 받은 후 ACK 블록을 전송해야 합니다. 이 권장사항은 일반적인 성격을 가지며 TCP 엔드포인트 동작에 대한 권장사항 [RFC-5681](https://tools.ietf.org/html/rfc5681)과 일치합니다. 네트워크 상황에 대한 지식, 피어의 혼잡 제어기에 대한 지식, 또는 추가 연구 및 실험을 통해 더 나은 성능 특성을 가진 대안적인 확인응답 전략이 제안될 수 있습니다.

- 수신된 패킷의 패킷 번호가 이미 수신된 다른 ack-eliciting 패킷보다 작을 때
- 패킷의 패킷 번호가 수신된 가장 높은 번호의 ack-eliciting 패킷보다 클 때 그리고 해당 패킷과 이 패킷 사이에 누락된 패킷들이 있을 때
- 패킷 헤더의 ack-immediate 플래그가 설정되었을 때

수신자는 응답으로 ACK 블록을 보낼지 결정하기 전에 사용 가능한 여러 패킷을 처리할 수 있습니다. 일반적으로 수신자는 ACK를 RTT / 6 또는 최대 150ms 이상 지연시키지 않아야 합니다.

### 즉시 ACK 플래그

데이터 패킷 헤더의 ack-immediate 플래그는 수신자가 수신 후 곧바로, 아마도 몇 ms 이내에 ack를 보내달라는 요청입니다. 일반적으로 수신자는 즉시 ACK를 RTT / 16 또는 최대 5ms를 초과하여 지연시켜서는 안 됩니다.

수신자는 송신자의 전송 윈도우 크기를 알지 못하므로, ACK를 전송하기 전에 얼마나 지연시켜야 하는지 알 수 없습니다. 데이터 패킷 헤더의 즉시 ACK 플래그는 효과적인 RTT를 최소화하여 최대 처리량을 유지하는 중요한 방법입니다. 즉시 ACK 플래그는 헤더 바이트 13, 비트 0, 즉 (header[13] & 0x01)입니다. 설정되면 즉시 ACK가 요청됩니다. 자세한 내용은 위의 짧은 헤더 섹션을 참조하세요.

발신자가 immediate-ack 플래그를 설정할 시점을 결정하는 데 사용할 수 있는 몇 가지 가능한 전략이 있습니다:

즉시 ACK 플래그는 I2NP 메시지나 메시지 조각을 포함하는 데이터 패킷에서만 필요해야 합니다.

ACK 블록이 전송될 때, 확인응답된 패킷의 하나 이상의 범위가 포함됩니다. 이전 패킷에 대한 확인응답을 포함하면 이전에 전송된 ACK 블록의 손실로 인한 불필요한 재전송 가능성을 줄일 수 있지만, ACK 블록의 크기가 커지는 단점이 있습니다.

ACK 블록은 항상 가장 최근에 수신된 패킷들을 확인응답해야 하며, 패킷들이 더 많이 순서에서 벗어날수록 업데이트된 ACK 블록을 빠르게 전송하는 것이 더욱 중요합니다. 이는 상대방이 패킷을 손실된 것으로 판단하고 그 안에 포함된 블록들을 잘못 재전송하는 것을 방지하기 위함입니다. ACK 블록은 단일 패킷 내에 맞아야 합니다. 만약 맞지 않는다면, 더 오래된 범위들(가장 작은 패킷 번호를 가진 것들)이 생략됩니다.

### ACK 블록 크기

수신자는 ACK 블록의 크기를 제한하고 리소스 고갈을 방지하기 위해 기억하고 ACK 블록으로 전송하는 ACK 범위의 수를 제한합니다. ACK 블록에 대한 확인응답을 받은 후, 수신자는 해당 확인응답된 ACK 범위를 추적하는 것을 중단해야 합니다. 송신자는 대부분의 패킷에 대한 확인응답을 기대할 수 있지만, 이 프로토콜은 수신자가 처리하는 모든 패킷에 대한 확인응답의 수신을 보장하지는 않습니다.

많은 ACK 범위를 유지하는 것이 ACK 블록이 너무 커지게 만들 수 있습니다. 수신자는 ACK 블록 크기를 제한하기 위해 확인응답되지 않은 ACK 범위를 삭제할 수 있지만, 이는 송신자로부터의 재전송 증가라는 비용을 수반합니다. 이는 ACK 블록이 패킷에 들어가기에 너무 클 경우 필요합니다. 수신자는 또한 다른 블록을 위한 공간을 보존하거나 확인응답이 소비하는 대역폭을 제한하기 위해 ACK 블록 크기를 더욱 제한할 수 있습니다.

- 작은 N 값에 대해 N개 패킷마다 한 번씩 설정
- 패킷 버스트의 마지막에 설정
- 송신 윈도우가 거의 가득 찰 때 설정, 예를 들어 2/3 이상 찰 때
- 재전송된 fragment가 포함된 모든 패킷에 설정

수신자는 해당 범위의 번호를 가진 패킷을 이후에 수락하지 않을 것임을 보장할 수 없는 한 ACK 범위를 유지해야 합니다. 범위가 폐기됨에 따라 증가하는 최소 패킷 번호를 유지하는 것은 최소한의 상태로 이를 달성하는 한 가지 방법입니다.

### ACK 블록 추적을 통한 범위 제한

수신자는 모든 ACK 범위를 폐기할 수 있지만, 성공적으로 처리된 가장 큰 패킷 번호는 보관해야 합니다. 이는 후속 패킷에서 패킷 번호를 복구하는 데 사용되기 때문입니다.

다음 섹션에서는 각 ACK 블록에서 승인할 패킷을 결정하는 예시적인 접근 방법을 설명합니다. 이 알고리즘의 목표는 처리되는 모든 패킷에 대해 승인을 생성하는 것이지만, 승인이 손실될 가능성은 여전히 존재합니다.

ACK 블록을 포함한 패킷이 전송될 때, 해당 블록의 Ack Through 필드를 저장할 수 있습니다. ACK 블록을 포함한 패킷이 확인응답을 받으면, 수신자는 전송된 ACK 블록의 Ack Through 필드보다 작거나 같은 패킷들에 대한 확인응답을 중단할 수 있습니다.

ACK 블록과 같이 ack-eliciting이 아닌 패킷만을 전송하는 수신자는 장시간 동안 확인응답을 받지 못할 수 있습니다. 이로 인해 수신자가 많은 수의 ACK 블록에 대한 상태를 장시간 유지해야 하며, 전송하는 ACK 블록이 불필요하게 클 수 있습니다. 이러한 경우, 수신자는 피어로부터 ACK를 유도하기 위해 라운드트립당 한 번과 같이 가끔씩 PING이나 기타 작은 ack-eliciting 블록을 전송할 수 있습니다.

ACK 블록 손실이 없는 경우, 이 알고리즘은 최소 1 RTT의 재정렬을 허용합니다. ACK 블록 손실과 재정렬이 있는 경우, 이 접근 방식은 모든 확인응답이 더 이상 ACK 블록에 포함되지 않기 전에 송신자가 이를 확인한다는 것을 보장하지 않습니다. 패킷이 순서대로 수신되지 않을 수 있으며, 이를 포함하는 모든 후속 ACK 블록이 손실될 수 있습니다. 이 경우 손실 복구 알고리즘이 잘못된 재전송을 야기할 수 있지만, 송신자는 계속해서 전진하는 진행을 유지할 것입니다.

I2P transport는 I2NP 메시지의 순서대로 전달을 보장하지 않습니다. 따라서 하나 이상의 I2NP 메시지나 fragment를 포함한 Data 메시지의 손실이 다른 I2NP 메시지의 전달을 방해하지 않으며, head-of-line blocking이 발생하지 않습니다. 구현체는 송신 윈도우가 허용하는 경우 손실 복구 단계 중에도 새로운 메시지를 계속 전송해야 합니다.

송신자는 메시지의 전체 내용을 보관하여 동일하게 재전송해서는 안 됩니다 (handshake 메시지는 예외, 위 참조). 송신자는 메시지를 보낼 때마다 최신 정보(ACK, NACK, 확인되지 않은 데이터)가 포함된 메시지를 조립해야 합니다. 송신자는 메시지가 한 번 확인되면 해당 메시지의 정보를 재전송하지 않아야 합니다. 여기에는 손실로 선언된 후 확인된 메시지도 포함되며, 이는 네트워크 순서 변경이 있을 때 발생할 수 있습니다.

### 혼잡

TBD. 일반적인 지침은 [RFC-9002](https://tools.ietf.org/html/rfc9002)에서 찾을 수 있습니다.

세션의 수명 동안 피어의 IP 또는 포트가 변경될 수 있습니다. IP 변경은 IPv6 임시 주소 순환, ISP 주도의 주기적 IP 변경, WiFi와 셀룰러 IP 간 전환하는 모바일 클라이언트, 또는 기타 로컬 네트워크 변경으로 인해 발생할 수 있습니다. 포트 변경은 이전 바인딩이 시간 초과된 후 NAT 재바인딩으로 인해 발생할 수 있습니다.

피어의 IP나 포트는 패킷 수정이나 주입을 포함한 다양한 경로상 및 경로외 공격으로 인해 변경된 것처럼 보일 수 있습니다.

### 재전송

연결 마이그레이션은 새로운 소스 엔드포인트(IP+포트)를 검증하는 과정이며, 동시에 검증되지 않은 변경사항을 방지합니다. 이 과정은 QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000)에서 정의된 것의 단순화된 버전입니다. 이 과정은 세션의 데이터 단계에서만 정의됩니다. 핸드셰이크 중에는 마이그레이션이 허용되지 않습니다. 모든 핸드셰이크 패킷은 이전에 송수신된 패킷과 동일한 IP 및 포트에서 온 것임이 검증되어야 합니다. 즉, 핸드셰이크 동안 피어의 IP와 포트는 일정해야 합니다.

### 윈도우

(QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000)에서 각색)

### 위협 모델

피어는 소스 주소를 스푸핑하여 엔드포인트가 원하지 않는 호스트에게 과도한 양의 데이터를 전송하도록 할 수 있습니다. 엔드포인트가 스푸핑하는 피어보다 훨씬 많은 데이터를 전송하는 경우, 연결 마이그레이션이 공격자가 피해자에게 생성할 수 있는 데이터 볼륨을 증폭시키는 데 사용될 수 있습니다.

## 연결 마이그레이션

경로상 공격자는 스푸핑된 주소로 패킷을 복사하고 전달하여 원본 패킷보다 먼저 도착하도록 함으로써 가짜 연결 마이그레이션을 유발할 수 있습니다. 스푸핑된 주소를 가진 패킷은 마이그레이션하는 연결에서 온 것으로 보이고, 원본 패킷은 중복으로 간주되어 드롭됩니다. 가짜 마이그레이션 후에는 소스 주소의 검증이 실패하게 되는데, 이는 소스 주소에 있는 엔티티가 설령 원한다고 하더라도 전송된 Path Challenge를 읽거나 응답하는 데 필요한 암호화 키를 가지고 있지 않기 때문입니다.

패킷을 관찰할 수 있는 경로 외부 공격자는 진짜 패킷의 복사본을 엔드포인트로 전달할 수 있습니다. 복사된 패킷이 진짜 패킷보다 먼저 도착하면, 이는 NAT 재바인딩으로 나타날 것입니다. 진짜 패킷은 중복으로 간주되어 폐기됩니다. 공격자가 계속해서 패킷을 전달할 수 있다면, 공격자를 통한 경로로의 마이그레이션을 유발할 수 있을 것입니다. 이는 공격자를 경로상에 위치시켜, 모든 후속 패킷을 관찰하거나 차단할 수 있는 능력을 제공합니다.

QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000)은 네트워크 경로를 변경할 때 연결 ID를 변경하도록 명시했습니다. 여러 네트워크 경로에서 안정적인 연결 ID를 사용하면 수동적 관찰자가 해당 경로들 간의 활동을 연관짓는 것을 허용할 수 있습니다. 네트워크 간을 이동하는 엔드포인트는 상대방이 아닌 다른 개체가 자신의 활동을 연관짓는 것을 원하지 않을 수 있습니다. 그러나 QUIC은 헤더의 연결 ID를 암호화하지 않습니다. SSU2는 이를 암호화하므로, 프라이버시 누출이 발생하려면 수동적 관찰자가 연결 ID를 해독하는 데 필요한 introduction key를 얻기 위해 네트워크 데이터베이스에도 접근해야 합니다. introduction key가 있더라도 이는 강력한 공격이 아니며, 상당한 복잡성을 야기할 수 있으므로 SSU2에서는 마이그레이션 후 연결 ID를 변경하지 않습니다.

### 경로 검증 시작

데이터 단계에서 peer들은 수신된 각 데이터 패킷의 소스 IP와 포트를 확인해야 합니다. IP 또는 포트가 이전에 수신된 것과 다르고, 패킷이 중복 패킷 번호가 아니며, 패킷이 성공적으로 복호화되면 세션은 경로 검증 단계로 진입합니다.

#### Introducer 선택

또한, peer는 새로운 IP와 포트가 로컬 검증 규칙에 따라 유효한지 확인해야 합니다(차단되지 않았는지, 불법 포트가 아닌지 등). Peer는 IPv4와 IPv6 간의 마이그레이션을 지원할 의무가 없으며, 다른 주소 체계의 새로운 IP를 무효한 것으로 취급할 수 있습니다. 이는 예상되는 동작이 아니고 구현 복잡성을 크게 증가시킬 수 있기 때문입니다. 무효한 IP/포트에서 패킷을 수신했을 때, 구현체는 단순히 이를 드롭하거나 기존 IP/포트로 경로 검증을 시작할 수 있습니다.

#### 응답 처리

경로 검증 단계에 진입하면 다음 단계를 수행하세요:

#### 소개자

경로 검증 단계에서 세션은 수신되는 패킷을 계속 처리할 수 있습니다. 기존 IP/포트든 새로운 IP/포트든 관계없이 말입니다. 세션은 또한 데이터 패킷을 계속 전송하고 확인응답할 수 있습니다. 그러나 혼잡 윈도우와 PMTU는 경로 검증 단계 동안 최소값을 유지해야 하며, 이는 스푸핑된 주소로 대량의 트래픽을 전송하여 서비스 거부 공격에 악용되는 것을 방지하기 위함입니다.

#### 신원 숨김

구현체는 여러 경로를 동시에 검증하려고 시도할 수 있지만 필수는 아닙니다. 이는 복잡성에 비해 가치가 없을 것 같습니다. 이전 IP/포트가 이미 검증되었다는 것을 기억할 수 있고, 피어가 이전 IP/포트로 돌아오는 경우 경로 검증을 건너뛸 수 있지만 필수는 아닙니다.

### 메시지 내용

Path Challenge에서 전송된 것과 동일한 데이터를 포함하는 Path Response가 수신되면 Path Validation이 성공한 것입니다. Path Response 메시지의 소스 IP/포트는 Path Challenge가 전송된 곳과 동일할 필요가 없습니다.

Path Response 타이머가 만료되기 전에 Path Response를 받지 못하면, 다른 Path Challenge를 보내고 Path Response 타이머를 두 배로 늘립니다.

Path Validation 타이머가 만료되기 전에 Path Response를 받지 못하면 Path Validation이 실패합니다.

- 몇 초 또는 현재 RTO의 몇 배에 해당하는 경로 검증 타임아웃 타이머를 시작합니다 (TBD)
- 혼잡 윈도우를 최소값으로 줄입니다
- PMTU를 최소값(1280)으로 줄입니다
- 새로운 IP와 포트로 Path Challenge 블록, Address 블록(새로운 IP/포트 포함), 그리고 일반적으로 ACK 블록을 포함하는 데이터 패킷을 전송합니다. 이 패킷은 현재 세션과 동일한 connection ID와 암호화 키를 사용합니다. Path Challenge 블록 데이터는 스푸핑될 수 없도록 충분한 엔트로피(최소 8바이트)를 포함해야 합니다.
- 선택적으로, 다른 블록 데이터를 사용하여 기존 IP/포트로도 Path Challenge를 전송합니다. 아래를 참조하세요.
- 현재 RTO를 기반으로 Path Response 타임아웃 타이머를 시작합니다 (일반적으로 RTT + RTTdev의 배수)

Data 메시지는 다음 블록들을 포함해야 합니다. Padding이 마지막이어야 한다는 점을 제외하고는 순서가 지정되지 않습니다:

메시지에 다른 블록(예: I2NP)을 포함하는 것은 권장되지 않습니다.

Path Response를 포함하는 메시지에 Path Challenge 블록을 포함하여 반대 방향의 검증을 시작하는 것이 허용됩니다.

Path Challenge와 Path Response 블록은 ACK-eliciting입니다. Path Challenge는 Path Response와 ACK 블록을 포함하는 Data 메시지에 의해 ACK됩니다. Path Response는 ACK 블록을 포함하는 Data 메시지에 의해 ACK되어야 합니다.

QUIC 사양은 경로 검증 중에 데이터 패킷을 어디로 보낼지 - 기존 IP/포트인지 새로운 IP/포트인지에 대해 명확하지 않습니다. IP/포트 변경에 신속하게 응답하는 것과 스푸핑된 주소로 트래픽을 보내지 않는 것 사이에는 균형이 필요합니다. 또한 스푸핑된 패킷이 기존 세션에 실질적인 영향을 미치도록 허용해서는 안 됩니다. 포트만 변경되는 경우는 유휴 기간 후 NAT 리바인딩에 의해 발생할 가능성이 높으며, IP 변경은 한쪽 또는 양쪽 방향으로 높은 트래픽이 발생하는 단계에서 일어날 수 있습니다.

### 경로 검증 중 라우팅

전략은 연구와 개선의 대상입니다. 가능성은 다음과 같습니다:

- Path Challenge 또는 Path Response 블록. Path Challenge는 불투명한 데이터를 포함하며, 최소 8바이트를 권장합니다. Path Response는 Path Challenge의 데이터를 포함합니다.
- 수신자의 명시적 IP를 포함하는 Address 블록
- DateTime 블록
- ACK 블록
- Padding 블록

Path Challenge를 받으면, 피어는 Path Challenge의 데이터를 포함한 Path Response가 담긴 데이터 패킷으로 응답해야 합니다.

Path Response는 Path Challenge가 수신된 IP/포트로 전송되어야 합니다. 이는 이전에 피어에 대해 설정된 IP/포트와 반드시 같지 않을 수 있습니다. 이를 통해 피어에 의한 경로 검증이 경로가 양방향으로 기능할 때만 성공하도록 보장합니다. 아래의 로컬 변경 후 검증 섹션을 참조하세요.

IP/포트가 해당 피어에 대해 이전에 알려진 IP/포트와 다르지 않다면, Path Challenge를 단순한 핑으로 처리하고 무조건적으로 Path Response로 응답합니다. 수신자는 수신된 Path Challenge를 기반으로 어떤 상태도 유지하거나 변경하지 않습니다. IP/포트가 다른 경우, 피어는 새로운 IP와 포트가 로컬 검증 규칙에 따라 유효한지(차단되지 않았는지, 불법 포트가 아닌지 등) 확인해야 합니다. 피어는 IPv4와 IPv6 간의 주소 패밀리 간 응답을 지원할 필요가 없으며, 다른 주소 패밀리의 새로운 IP를 무효한 것으로 처리할 수 있습니다. 이는 예상되는 동작이 아니기 때문입니다.

### 경로 도전에 응답하기

혼잡 제어로 인한 제약이 없다면, Path Response는 즉시 전송되어야 합니다. 구현체들은 필요시 Path Response의 전송률을 제한하거나 사용되는 대역폭을 제한하는 조치를 취해야 합니다.

Path Challenge 블록은 일반적으로 같은 메시지 내의 Address 블록과 함께 제공됩니다. Address 블록에 새로운 IP/포트가 포함되어 있다면, peer는 해당 IP/포트를 검증하고 세션 peer 또는 다른 peer와 함께 새로운 IP/포트에 대한 peer 테스트를 시작할 수 있습니다. peer가 자신이 방화벽 뒤에 있다고 생각하고 포트만 변경된 경우, 이 변경은 아마도 NAT 리바인딩으로 인한 것이며 추가적인 peer 테스트는 필요하지 않을 것입니다.

- 검증될 때까지 새로운 IP/포트로 데이터 패킷을 전송하지 않음
- 새로운 IP/포트가 검증될 때까지 이전 IP/포트로 데이터 패킷을 계속 전송
- 이전 IP/포트를 동시에 재검증
- 이전 또는 새로운 IP/포트 중 하나가 검증될 때까지 데이터를 전송하지 않음
- IP 변경과 포트만 변경되는 경우에 대한 서로 다른 전략
- 임시 주소 순환으로 인해 발생할 가능성이 높은 동일한 /32 내에서의 IPv6 변경에 대한 서로 다른 전략

### 성공적인 경로 검증

성공적인 경로 검증 시, 연결이 새로운 IP/포트로 완전히 마이그레이션됩니다. 성공 시:

경로 검증 단계에서 이전 IP/포트로부터 수신된 유효하고 중복되지 않은 패킷이 성공적으로 복호화되면 경로 검증이 취소됩니다. 스푸핑된 패킷으로 인해 취소된 경로 검증이 유효한 세션을 종료하거나 심각하게 중단시키지 않도록 하는 것이 중요합니다.

취소된 경로 검증에서:

스푸핑된 패킷으로 인한 경로 검증 실패가 유효한 세션을 종료시키거나 심각하게 방해하지 않도록 하는 것이 중요합니다.

경로 검증 실패 시:

### 경로 검증 취소

위의 과정은 변경된 IP/포트로부터 패킷을 수신한 peer들을 위해 정의되었습니다. 하지만 이 과정은 반대 방향으로도, 즉 자신의 IP나 포트가 변경되었음을 감지한 peer에 의해 시작될 수도 있습니다. peer는 자신의 로컬 IP가 변경되었음을 감지할 수 있을지도 모르지만, NAT rebinding으로 인해 자신의 포트가 변경되었음을 감지할 가능성은 훨씬 낮습니다. 따라서 이는 선택사항입니다.

- 경로 검증 단계를 종료합니다
- 모든 패킷이 새로운 IP와 포트로 전송됩니다.
- 혼잡 윈도우와 PMTU에 대한 제한이 제거되고, 증가가 허용됩니다. 새로운 경로는 다른 특성을 가질 수 있으므로 단순히 이전 값으로 복원하지 마세요.
- IP가 변경된 경우, 계산된 RTT와 RTO를 초기값으로 설정합니다. 포트만 변경되는 경우는 일반적으로 NAT 리바인딩이나 기타 미들박스 활동의 결과이므로, 피어는 초기값으로 되돌리는 대신 혼잡 제어 상태와 왕복 시간 추정치를 유지할 수 있습니다.
- 이전 IP/포트에 대해 전송되거나 수신된 모든 토큰을 삭제(무효화)합니다 (선택사항)
- 새로운 IP/포트에 대한 새 토큰 블록을 전송합니다 (선택사항)

### 경로 검증 실패

IP 또는 포트가 변경된 피어로부터 경로 챌린지를 받으면, 상대방 피어는 반대 방향으로 경로 챌린지를 시작해야 합니다.

Path Challenge와 Path Response 블록은 언제든지 Ping/Pong 패킷으로 사용될 수 있습니다. Path Challenge 블록의 수신은 다른 IP/포트에서 수신되지 않는 한 수신자의 상태를 변경하지 않습니다.

- 경로 검증 단계 종료
- 모든 패킷이 이전 IP와 포트로 전송됩니다.
- 혼잡 윈도우와 PMTU에 대한 제한이 제거되고, 증가가 허용되거나 선택적으로 이전 값으로 복원됩니다.
- 이전에 새로운 IP/포트로 전송되었던 모든 데이터 패킷을 이전 IP/포트로 재전송합니다.

### 로컬 변경 후 검증

피어는 동일한 피어와 여러 세션을 설정해서는 안 되며, 이는 SSU 1 또는 2와 관계없이, 또한 동일하거나 다른 IP 주소와 관계없이 적용됩니다. 그러나 버그, 이전 세션 종료 메시지가 손실된 경우, 또는 종료 메시지가 아직 도착하지 않은 경쟁 상황으로 인해 이러한 상황이 발생할 수 있습니다.

Bob이 Alice와 기존 세션을 가지고 있는 상태에서, Bob이 Alice로부터 Session Confirmed를 받아 핸드셰이크를 완료하고 새 세션을 설정할 때, Bob은 다음을 수행해야 합니다:

- 경로 유효성 검사 단계를 종료합니다
- 모든 패킷이 기존 IP와 포트로 전송됩니다.
- 혼잡 윈도우와 PMTU에 대한 제한이 제거되고, 증가할 수 있습니다.
- 선택적으로, 기존 IP와 포트에서 경로 유효성 검사를 시작합니다. 실패하면 세션을 종료합니다.
- 그렇지 않으면, 표준 세션 타임아웃 및 종료 규칙을 따릅니다.
- 이전에 새 IP/포트로 전송되었던 모든 데이터 패킷을 기존 IP/포트로 재전송합니다.

### Ping/Pong으로 사용

핸드셰이크 단계의 세션은 일반적으로 단순히 시간 초과되거나 더 이상 응답하지 않음으로써 종료됩니다. 선택적으로, 응답에 Termination 블록을 포함하여 종료할 수 있지만, 암호화 키의 부족으로 인해 대부분의 오류에는 응답할 수 없습니다. 종료 블록을 포함한 응답을 위한 키가 사용 가능하더라도, 응답을 위해 DH를 수행하는 것은 일반적으로 CPU 비용에 비해 가치가 없습니다. 예외적으로 재시도 메시지의 Termination 블록은 생성 비용이 저렴하므로 허용될 수 있습니다.

데이터 단계의 세션은 Termination 블록을 포함하는 데이터 메시지를 전송하여 종료됩니다. 이 메시지에는 ACK 블록도 포함되어야 합니다. 세션이 충분히 오래 지속되어 이전에 전송된 토큰이 만료되었거나 만료될 예정인 경우, New Token 블록이 포함될 수 있습니다. 이 메시지는 ack를 요구하지 않습니다. "Termination Received"를 제외한 모든 이유로 Termination 블록을 수신하면, 피어는 "Termination Received" 이유가 포함된 Termination 블록을 담은 데이터 메시지로 응답합니다.

### 핸드셰이크 단계

Termination 블록을 송신하거나 수신한 후, 세션은 TBD로 정해질 최대 기간 동안 종료 단계에 진입해야 합니다. 종료 상태는 Termination 블록을 포함한 패킷이 손실되거나 반대 방향으로 전송 중인 패킷들로부터 보호하기 위해 필요합니다. 종료 단계에 있는 동안에는 추가로 수신되는 패킷들을 처리할 요구사항이 없습니다. 종료 상태의 세션은 해당 세션에 속한다고 판단되는 모든 수신 패킷에 대해 Termination 블록을 포함한 패킷으로 응답합니다. 세션은 종료 상태에서 패킷을 생성하는 속도를 제한해야 합니다. 예를 들어, 세션은 수신된 패킷에 응답하기 전에 점진적으로 증가하는 수의 수신 패킷이나 시간을 기다릴 수 있습니다.

## 다중 세션

종료되는 세션에 대해 router가 유지해야 하는 상태를 최소화하기 위해, 세션은 수신된 패킷에 대한 응답으로 동일한 패킷 번호를 가진 정확히 같은 패킷을 그대로 전송할 수 있지만 반드시 그래야 하는 것은 아닙니다. 참고: 종료 패킷의 재전송을 허용하는 것은 각 패킷에 새로운 패킷 번호를 사용해야 한다는 요구사항에 대한 예외입니다. 새로운 패킷 번호를 전송하는 것은 주로 손실 복구와 혼잡 제어에 유리한데, 이는 종료된 연결에서는 관련이 없을 것으로 예상됩니다. 최종 패킷을 재전송하는 것은 더 적은 상태를 요구합니다.

"Termination Received" 사유로 Termination 블록을 받은 후, 세션은 종료 단계를 벗어날 수 있습니다.

- 이전 세션에서 새 세션으로 전송되지 않았거나 확인되지 않은 아웃바운드 I2NP 메시지를 마이그레이션
- 이전 세션에서 이유 코드 22로 종료 신호 전송
- 이전 세션을 제거하고 새 세션으로 교체

## 세션 종료

### 데이터 단계

정상적이거나 비정상적인 종료 시, router들은 handshake 임시 키, 대칭 암호화 키 및 관련 정보를 포함하여 메모리 내의 모든 임시 데이터를 제로화해야 합니다.

### 정리

요구사항은 게시된 주소가 SSU 1과 공유되는지 여부에 따라 달라집니다. 현재 SSU 1 IPv4 최소값은 620이며, 이는 확실히 너무 작습니다.

최소 SSU2 MTU는 IPv4와 IPv6 모두에서 1280이며, 이는 [RFC-9000](https://tools.ietf.org/html/rfc9000)에서 지정된 것과 동일합니다. 아래를 참조하세요. 최소 MTU를 증가시킴으로써 1 KB tunnel 메시지와 짧은 tunnel 빌드 메시지가 하나의 데이터그램에 맞게 되어, 일반적인 fragmentation 양이 크게 줄어듭니다. 이는 또한 최대 I2NP 메시지 크기의 증가를 허용합니다. 1820바이트 스트리밍 메시지는 두 개의 데이터그램에 맞아야 합니다.

router는 해당 주소의 MTU가 최소 1280 이상이 아닌 한 SSU2를 활성화하거나 SSU2 주소를 게시해서는 안 됩니다.

라우터는 각 SSU 또는 SSU2 router 주소에서 기본값이 아닌 MTU를 게시해야 합니다.

### SSU 주소

SSU 1과 주소를 공유하므로 SSU 1 규칙을 따라야 합니다. IPv4: 기본값과 최대값은 1484입니다. 최소값은 1292입니다. (IPv4 MTU + 4)는 16의 배수여야 합니다. IPv6: 반드시 게시되어야 하며, 최소값은 1280이고 최대값은 1488입니다. IPv6 MTU는 16의 배수여야 합니다.

## MTU

IPv4: 기본값과 최대값은 1500입니다. 최소값은 1280입니다. IPv6: 기본값과 최대값은 1500입니다. 최소값은 1280입니다. 16의 배수 규칙은 없지만, 최소한 2의 배수여야 합니다.

SSU 1의 경우, 현재 Java I2P는 작은 패킷으로 시작하여 점진적으로 크기를 늘리거나 수신된 패킷 크기에 따라 증가시키는 방식으로 PMTU 탐지를 수행합니다. 이는 조잡하며 효율성을 크게 떨어뜨립니다. SSU 2에서 이 기능을 계속 사용할지는 미정입니다.

최근 [PMTU](https://en.wikipedia.org/wiki/Path_MTU_Discovery) 연구에 따르면 IPv4의 최소값을 1200 이상으로 설정하면 99% 이상의 연결에서 작동할 것으로 나타났습니다. QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000)는 최소 IP 패킷 크기를 1280바이트로 요구합니다.

[RFC-9000](https://tools.ietf.org/html/rfc9000) 인용:

### SSU2 주소

최대 데이터그램 크기는 단일 UDP 데이터그램을 사용하여 네트워크 경로를 통해 전송할 수 있는 UDP 페이로드의 최대 크기로 정의됩니다. 네트워크 경로가 최소 1200바이트의 최대 데이터그램 크기를 지원할 수 없는 경우 QUIC을 사용해서는 안 됩니다.

### PMTU 검색

QUIC은 최소 1280바이트의 IP 패킷 크기를 가정합니다. 이는 IPv6 최소 크기 [IPv6]이며 대부분의 현대적인 IPv4 네트워크에서도 지원됩니다. IPv6의 최소 IP 헤더 크기 40바이트와 IPv4의 20바이트, 그리고 UDP 헤더 크기 8바이트를 가정하면, IPv6에서는 최대 데이터그램 크기가 1232바이트, IPv4에서는 1252바이트가 됩니다. 따라서 현대적인 IPv4와 모든 IPv6 네트워크 경로는 QUIC을 지원할 수 있을 것으로 예상됩니다.

### 핸드셰이크 최소 크기

참고: 1200바이트의 UDP 페이로드를 지원해야 한다는 이 요구사항은 경로가 IPv6 최소 MTU인 1280바이트만 지원하는 경우 IPv6 확장 헤더에 사용할 수 있는 공간을 32바이트로, IPv4 옵션에 사용할 수 있는 공간을 52바이트로 제한합니다. 이는 Initial 패킷과 경로 검증에 영향을 미칩니다.

인용 끝

QUIC는 증폭 공격을 방지하고 양방향으로 PMTU가 이를 지원함을 보장하기 위해 양방향의 Initial 데이터그램이 최소 1200바이트 이상이어야 한다고 요구합니다.

Session Request와 Session Created에 대해 이를 요구할 수 있지만, 대역폭 측면에서 상당한 비용이 발생합니다. 토큰이 없는 경우나 Retry 메시지를 받은 후에만 이를 수행할 수도 있습니다. 추후 결정 예정

QUIC는 Bob이 클라이언트 주소가 검증될 때까지 수신한 데이터량의 3배를 초과하여 전송하지 않도록 요구합니다. SSU2는 본질적으로 이 요구사항을 충족합니다. 왜냐하면 Retry 메시지가 Token Request 메시지와 거의 같은 크기이고 Session Request 메시지보다 작기 때문입니다. 또한 Retry 메시지는 한 번만 전송됩니다.

QUIC은 증폭 공격을 방지하고 양방향으로 PMTU가 이를 지원하는지 확인하기 위해 PATH_CHALLENGE 또는 PATH_RESPONSE 블록을 포함하는 메시지가 최소 1200바이트 이상이어야 한다고 요구합니다.

이 역시 대역폭의 상당한 비용을 들여 요구할 수 있습니다. 하지만 이러한 경우는 드물 것입니다. TBD

### 경로 메시지 최소 크기

IPv4: IP 단편화는 없다고 가정합니다. IP + 데이터그램 헤더는 28바이트입니다. 이는 IPv4 옵션이 없다고 가정합니다. 최대 메시지 크기는 MTU - 28입니다. 데이터 단계 헤더는 16바이트이고 MAC은 16바이트로 총 32바이트입니다. 페이로드 크기는 MTU - 60입니다. 최대 1500 MTU에서 최대 데이터 단계 페이로드는 1440입니다. 최소 1280 MTU에서 최대 데이터 단계 페이로드는 1220입니다.

IPv6: IP 단편화는 허용되지 않습니다. IP + 데이터그램 헤더는 48바이트입니다. 이는 IPv6 확장 헤더가 없다고 가정합니다. 최대 메시지 크기는 MTU - 48입니다. 데이터 단계 헤더는 16바이트이고 MAC은 16바이트로, 총 32바이트입니다. 페이로드 크기는 MTU - 80입니다. 최대 1500 MTU에서 최대 데이터 단계 페이로드는 1420입니다. 최소 1280 MTU에서 최대 데이터 단계 페이로드는 1200입니다.

SSU 1에서는 최대 64개 fragment와 620 최소 MTU를 기반으로 I2NP 메시지에 대해 약 32KB의 엄격한 최대값이 가이드라인이었습니다. 번들된 LeaseSet과 세션 키의 오버헤드로 인해 애플리케이션 레벨에서의 실제 한계는 약 6KB 낮은 약 26KB였습니다. SSU 1 프로토콜은 128개 fragment를 허용하지만 현재 구현에서는 64개 fragment로 제한합니다.

### 최대 I2NP 메시지 크기

최소 MTU를 1280으로 높이고 데이터 단계 페이로드를 약 1200으로 설정하면, 64개 조각으로 약 76KB의 SSU 2 메시지가 가능하고 128개 조각으로 152KB가 가능합니다. 이렇게 하면 최대 64KB를 쉽게 허용할 수 있습니다.

tunnel에서의 단편화와 SSU 2에서의 단편화로 인해 메시지 손실 확률이 메시지 크기에 따라 기하급수적으로 증가합니다. I2NP 데이터그램의 경우 애플리케이션 계층에서 약 10KB의 실용적인 제한을 계속 권장합니다.

### 버전

SSU1 Peer Test와 SSU2 Peer Test의 목표에 대한 분석은 위의 Peer Test Security를 참조하세요.

Bob에 의해 거부될 때:

Charlie에 의해 거부될 때:

참고: RI는 I2NP 블록 내의 I2NP Database Store 메시지로 전송되거나, (충분히 작은 경우) RI 블록으로 전송될 수 있습니다. 이들은 충분히 작은 경우 peer test 블록과 동일한 패킷에 포함될 수 있습니다.

메시지 1-4는 Data 메시지의 Peer Test 블록을 사용하는 세션 내 메시지입니다. 메시지 5-7은 Peer Test 메시지의 Peer Test 블록을 사용하는 세션 외 메시지입니다.

## 피어 테스트 프로세스

참고: SSU 1에서와 같이, 메시지 4와 5는 어떤 순서로든 도착할 수 있습니다. Alice가 방화벽으로 보호되어 있다면 메시지 5 및/또는 7이 전혀 수신되지 않을 수 있습니다. 메시지 5가 메시지 4보다 먼저 도착하면, Alice는 헤더를 암호화할 Charlie의 intro key가 아직 없기 때문에 즉시 메시지 6을 보낼 수 없습니다. 메시지 4가 메시지 5보다 먼저 도착하면, Alice는 메시지 6으로 방화벽을 열지 않고 메시지 5가 도착하는지 기다려야 하므로 즉시 메시지 6을 보내서는 안 됩니다.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest
        <---------------- Charlie RI
4.      <------------------ PeerTest

5.      <----------------------------------------- PeerTest
6. PeerTest ----------------------------------------->
7.      <----------------------------------------- PeerTest
```
크로스 버전 피어 테스팅은 지원되지 않습니다. 유일하게 허용되는 버전 조합은 모든 피어가 버전 2인 경우입니다.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
4.      <------------------ PeerTest (reject)
```
메시지 1-4는 세션 내에 있으며 데이터 단계 ACK 및 재전송 프로세스에 의해 처리됩니다. Peer Test 블록은 ack를 요구합니다.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest (reject)
                      (optional: Bob could try another Charlie here)
4.      <------------------ PeerTest (reject)
```
메시지 5-7은 변경 없이 재전송될 수 있습니다.

SSU 1에서와 같이 IPv6 주소 테스트가 지원되며, Bob과 Charlie가 게시된 IPv6 주소에서 'B' capability로 지원을 표시하는 경우 Alice-Bob 및 Alice-Charlie 통신이 IPv6를 통해 이루어질 수 있습니다. 자세한 내용은 Proposal 126을 참조하세요.

0.9.50 이전의 SSU 1에서와 같이, Alice는 테스트하고자 하는 전송 계층(IPv4 또는 IPv6)을 통해 기존 세션을 사용하여 Bob에게 요청을 보냅니다. Bob이 IPv4를 통해 Alice로부터 요청을 받으면, Bob은 IPv4 주소를 광고하는 Charlie를 선택해야 합니다. Bob이 IPv6을 통해 Alice로부터 요청을 받으면, Bob은 IPv6 주소를 광고하는 Charlie를 선택해야 합니다. 실제 Bob-Charlie 통신은 IPv4 또는 IPv6을 통해 이루어질 수 있습니다(즉, Alice의 주소 타입과 무관함). 이는 IPv4/v6 혼합 요청이 허용되는 0.9.50부터의 SSU 1 동작과는 다릅니다.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Path</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Intro Key</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->C session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->A session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->C</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
  </tbody>
</table>
### 재전송

SSU 1과 달리, Alice는 메시지 1에서 요청된 테스트 IP와 포트를 지정합니다. Bob은 이 IP와 포트를 검증해야 하며, 유효하지 않을 경우 코드 5로 거부해야 합니다. 권장되는 IP 검증은 IPv4의 경우 Alice의 IP와 일치해야 하고, IPv6의 경우 최소한 IP의 첫 8바이트가 일치해야 합니다. 포트 검증은 특권 포트와 잘 알려진 프로토콜의 포트를 거부해야 합니다.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### IPv6 참고 사항

여기서는 Alice가 수신된 메시지를 기반으로 피어 테스트 결과를 어떻게 결정할 수 있는지 문서화합니다. SSU2의 향상된 기능을 통해 [SSU](/docs/transport/ssu)의 피어 테스트 결과 상태 머신과 비교하여 이를 수정하고 개선하며 더 잘 문서화할 수 있는 기회를 얻었습니다.

테스트된 각 주소 유형(IPv4 또는 IPv6)에 대해, 결과는 UNKNOWN, OK, FIREWALLED, 또는 SYMNAT 중 하나가 될 수 있습니다. 또한 IP나 포트 변경을 감지하거나 내부 포트와 다른 외부 포트를 감지하기 위해 추가적인 처리가 수행될 수 있습니다.

### Bob에 의한 처리

문서화된 SSU 상태 머신의 문제점:

따라서 SSU와 달리, 메시지 4를 받은 후 몇 초간 기다린 다음, 메시지 5를 받지 못했더라도 메시지 6을 보내는 것을 권장합니다.

### 결과 상태 머신

메시지 4, 5, 7이 수신되었는지 여부(예 또는 아니오)를 기반으로 한 상태 머신의 요약은 다음과 같습니다:

### 재전송

메시지 7의 주소 블록에서 수신된 IP/포트를 확인하는 더 자세한 상태 머신은 아래와 같습니다. 한 가지 과제는 당신(Alice)이 대칭 NAT 상태인지, 아니면 Charlie가 대칭 NAT 상태인지를 결정하는 것입니다.

동일한 결과를 두 개 이상의 피어 테스트에서 요구하여 상태 전환을 확인하는 후처리 또는 추가 로직을 사용하는 것이 권장됩니다.

두 개 이상의 테스트에 의한 IP/포트 검증 및 확인 수신, 또는 Session Created 메시지의 주소 블록을 통한 검증도 권장되지만, 이는 본 명세의 범위를 벗어납니다.

- 메시지 5를 받지 않으면 메시지 6을 보내지 않으므로, 우리가 SYMNAT인지 알 수 없습니다
- 메시지 4와 7을 받았다면, 어떻게 SYMNAT일 수 있겠습니까
- IP는 일치하지 않지만 포트가 일치한다면, 우리는 SYMNAT이 아니라 단지 IP가 변경된 것입니다

SSU1 Relay의 분석과 SSU2 Relay의 목표에 대해서는 위의 Relay Security를 참조하세요.

Bob에 의해 거부되었을 때:

```
4 5 7  Result             Notes
-----  ------             -----
n n n  UNKNOWN
y n n  FIREWALLED           (unless currently SYMNAT)
n y n  OK                   (unless currently SYMNAT, which is unlikely)
y y n  OK                   (unless currently SYMNAT, which is unlikely)
n n y  n/a                  (can't send msg 6)
y n y  FIREWALLED or SYMNAT (requires sending msg 6 w/o rcv msg 5)
n y y  n/a                  (can't send msg 6)
y y y  OK
```
Charlie에 의해 거부될 때:

참고: RI는 I2NP 블록 내의 I2NP Database Store 메시지로 전송되거나, (충분히 작은 경우) RI 블록으로 전송될 수 있습니다. 이들은 충분히 작은 경우 relay 블록과 동일한 패킷에 포함될 수 있습니다.

SSU 1에서 Charlie의 router 정보는 각 introducer의 IP, 포트, intro 키, relay 태그, 만료 시간을 포함합니다.

```
If Alice does not get msg 5:
   If Alice does not get msg 4: -> UNKNOWN
   If Alice does not get msg 7: -> UNKNOWN
   If Alice gets msgs 4/7 and IP/port match: -> FIREWALLED
   If Alice gets msgs 4/7 and IP matches, port does not match:
      -> SYMNAT, but needs confirmation with 2nd test
   If Alice gets msgs 4/7 and IP does not match, port matches:
      -> FIREWALLED, address change?
   If Alice gets msgs 4/7 and both IP and port do not match:
      -> SYMNAT, address change?

If Alice gets msg 5:
   If Alice does not get msg 4: -> OK unless currently SYMNAT, else UNKNOWN
                                   (in SSU2 have to stop here)
   If Alice does not get msg 7: -> OK unless currently SYMNAT, else UNKNOWN
   If Alice gets msgs 4/5/7 and IP/port match: -> OK
   If Alice gets msgs 4/5/7 and IP matches, port does not match:
      -> OK, charlie is probably sym. natted
   If Alice gets msgs 4/5/7 and IP does not match, port matches:
      -> OK, address change?
   If Alice gets msgs 4/5/7 and both IP and port do not match:
      -> OK, address change?
```
## 릴레이 프로세스

SSU 2에서 Charlie의 router 정보에는 각 introducer의 router hash, relay tag, 그리고 만료 시간이 포함됩니다.

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse

5.      <-------------------------------------------- HolePunch
6. SessionRequest -------------------------------------------->
7.      <-------------------------------------------- SessionCreated
8. SessionConfirmed ------------------------------------------>
```
Alice는 먼저 이미 연결되어 있는 introducer(Bob)를 선택하여 필요한 라운드 트립 수를 줄여야 합니다. 두 번째로, 그런 것이 없다면 이미 router 정보를 가지고 있는 introducer를 선택해야 합니다.

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
4.      <-------------- RelayResponse
```
가능한 경우 버전 간 릴레이도 지원되어야 합니다. 이는 SSU 1에서 SSU 2로의 점진적 전환을 촉진할 것입니다. 허용되는 버전 조합은 다음과 같습니다 (TODO):

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse
```
Relay Request, Relay Intro, Relay Response는 모두 세션 내에서 처리되며 데이터 단계의 ACK 및 재전송 프로세스에 의해 보호됩니다. Relay Request, Relay Intro, Relay Response 블록은 ack-eliciting입니다.

일반적으로 Charlie는 Relay Intro에 대해 ACK 블록이 포함된 Relay Response로 즉시 응답한다는 점에 유의하세요. 이 경우 ACK 블록이 포함된 별도의 메시지는 필요하지 않습니다.

Hole punch는 SSU 1에서와 같이 재전송될 수 있습니다.

I2NP 메시지와 달리, Relay 메시지는 고유 식별자가 없으므로 중복은 nonce를 사용하여 relay 상태 머신에서 감지되어야 합니다. 구현체들은 또한 최근에 사용된 nonce들의 캐시를 유지해야 할 수도 있습니다. 이를 통해 해당 nonce에 대한 상태 머신이 완료된 후에도 수신된 중복을 감지할 수 있습니다.

[Prop158](/proposals/158-ipv6-transport-enhancements)에 문서화되어 0.9.50부터 지원되는 기능들을 포함하여 SSU 1 relay의 모든 기능이 지원됩니다. IPv4와 IPv6 소개가 지원됩니다. IPv6 소개를 위해 IPv4 세션을 통해 Relay Request를 보낼 수 있으며, IPv4 소개를 위해 IPv6 세션을 통해 Relay Request를 보낼 수 있습니다.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/2/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### IPv4/v6

다음은 SSU 1과의 차이점과 SSU 2 구현을 위한 권장사항입니다.

SSU 1에서는 introduction이 상대적으로 저렴하며, Alice는 일반적으로 모든 introducer에게 Relay Request를 보냅니다. SSU 2에서는 introducer와 먼저 연결을 설정해야 하므로 introduction이 더 비쌉니다. introduction 지연 시간과 오버헤드를 최소화하기 위해 권장되는 처리 단계는 다음과 같습니다:

SSU 1과 SSU 2 모두에서 Relay Response와 Hole Punch는 어떤 순서로든 수신될 수 있으며, 전혀 수신되지 않을 수도 있습니다.

SSU 1에서 Alice는 일반적으로 Hole Punch (1 1/2 RTT)보다 Relay Response (1 RTT)를 먼저 받습니다. 해당 명세서에 잘 문서화되어 있지 않을 수 있지만, Alice는 Charlie의 IP를 받기 위해 계속 진행하기 전에 Bob으로부터 Relay Response를 받아야 합니다. Hole Punch가 먼저 수신되면, Alice는 이를 인식하지 못할 것입니다. 왜냐하면 데이터가 포함되어 있지 않고 소스 IP가 인식되지 않기 때문입니다. Relay Response를 받은 후, Alice는 Charlie로부터 Hole Punch를 받거나, Charlie와의 핸드셰이크를 시작하기 전에 짧은 지연(권장 500ms) 중 하나를 기다려야 합니다.

### Alice의 처리

SSU 2에서 Alice는 보통 Relay Response(2 RTT)보다 Hole Punch(1 1/2 RTT)를 먼저 받게 됩니다. SSU 2 Hole Punch는 정의된 connection ID(relay nonce에서 파생됨)와 Charlie의 IP를 포함한 내용을 가진 완전한 메시지이기 때문에 SSU 1보다 처리하기 쉽습니다. Relay Response(Data 메시지)와 Hole Punch 메시지는 동일한 서명된 Relay Response 블록을 포함합니다. 따라서 Alice는 Charlie로부터 Hole Punch를 받거나 Bob으로부터 Relay Response를 받은 후에 Charlie와 핸드셰이크를 시작할 수 있습니다.

### Bob의 태그 요청

Hole Punch의 서명 검증에는 소개자(Bob)의 router 해시가 포함됩니다. Relay Request가 둘 이상의 소개자에게 전송된 경우, 서명을 검증하기 위한 몇 가지 옵션이 있습니다:

#### 요약

Charlie가 대칭 NAT 뒤에 있는 경우, Relay Response와 Hole Punch에서 보고된 그의 포트가 정확하지 않을 수 있습니다. 따라서 Alice는 Hole Punch 메시지의 UDP 소스 포트를 확인하고, 보고된 포트와 다른 경우 해당 포트를 사용해야 합니다.

- 주소의 iexp 값을 기반으로 만료된 introducer는 무시합니다
- 하나 이상의 introducer에 SSU2 연결이 이미 설정되어 있는 경우, 하나를 선택하여 해당 introducer에만 Relay Request를 전송합니다.
- 그렇지 않고, 하나 이상의 introducer에 대한 Router Info가 로컬에 알려져 있는 경우, 하나를 선택하여 해당 introducer에만 연결합니다.
- 그렇지 않으면, 모든 introducer의 Router Info를 조회하고, Router Info를 가장 먼저 받은 introducer에 연결합니다.

#### 세부사항

SSU 1에서는 Alice만이 Session Request에서 tag를 요청할 수 있었습니다. Bob은 절대 tag를 요청할 수 없었고, Alice는 Bob을 위해 릴레이할 수 없었습니다.

SSU2에서 Alice는 일반적으로 Session Request에서 태그를 요청하지만, Alice 또는 Bob 모두 데이터 단계에서 태그를 요청할 수도 있습니다. Bob은 일반적으로 인바운드 요청을 받은 후에는 방화벽에 막히지 않지만, 릴레이 후에 막힐 수 있거나, Bob의 상태가 변경되거나, 다른 주소 유형(IPv4/v6)에 대한 introducer를 요청할 수 있습니다. 따라서 SSU2에서는 Alice와 Bob이 동시에 상대방의 릴레이가 되는 것이 가능합니다.

다음 주소 속성들은 SSU 1에서 변경되지 않은 상태로 게시될 수 있으며, API 0.9.50부터 지원되는 [Prop158](/proposals/158-ipv6-transport-enhancements)의 변경사항을 포함합니다:

게시된 RouterAddress(RouterInfo의 일부)는 "SSU" 또는 "SSU2"의 프로토콜 식별자를 가집니다.

- 요청이 전송된 각 해시를 시도합니다
- 각 introducer에 대해 서로 다른 nonce를 사용하고, 이를 통해 이 Hole Punch가 어떤 introducer에 대한 응답인지 판단합니다
- 이미 수신된 Relay Response의 내용과 동일한 경우 서명을 재검증하지 않습니다
- 서명을 전혀 검증하지 않습니다

RouterAddress는 SSU2 지원을 나타내기 위해 세 가지 옵션을 포함해야 합니다:

### 주소 속성

Alice는 SSU2 프로토콜을 사용하여 연결하기 전에 세 가지 옵션이 모두 존재하고 유효한지 확인해야 합니다.

"s", "i", "v" 옵션과 "host", "port" 옵션을 사용하여 "SSU"로 게시될 때, router는 해당 호스트와 포트에서 SSU 및 SSU2 프로토콜 모두에 대한 들어오는 연결을 수락해야 하며, 프로토콜 버전을 자동으로 감지해야 합니다.

## 게시된 Router 정보

### 공개된 주소

"s", "i", "v" 옵션과 "host", "port" 옵션을 포함하여 "SSU2"로 게시될 때, router는 해당 호스트와 포트에서 SSU2 프로토콜 전용 수신 연결을 허용합니다.

- caps: [B,C,4,6] capabilities
- host: IP (IPv4 또는 IPv6). 축약된 IPv6 주소 ("::" 포함)가 허용됩니다. 방화벽이 있는 경우 존재할 수도 있고 없을 수도 있습니다. 호스트 이름은 허용되지 않습니다.
- iexp[0-2]: 이 introducer의 만료 시간. ASCII 숫자, epoch 이후 초 단위. 방화벽이 있고 introducer가 필요한 경우에만 존재합니다. 선택사항 (이 introducer의 다른 속성이 존재하더라도).
- ihost[0-2]: Introducer의 IP (IPv4 또는 IPv6). 축약된 IPv6 주소 ("::" 포함)가 허용됩니다. 방화벽이 있고 introducer가 필요한 경우에만 존재합니다. 호스트 이름은 허용되지 않습니다. SSU 주소에만 해당.
- ikey[0-2]: Introducer의 Base 64 introduction key. 방화벽이 있고 introducer가 필요한 경우에만 존재합니다. SSU 주소에만 해당.
- iport[0-2]: Introducer의 포트 1024 - 65535. 방화벽이 있고 introducer가 필요한 경우에만 존재합니다. SSU 주소에만 해당.
- itag[0-2]: Introducer의 태그 1 - (2**32 - 1) ASCII 숫자. 방화벽이 있고 introducer가 필요한 경우에만 존재합니다.
- key: Base 64 introduction key.
- mtu: 선택사항. 위의 MTU 섹션을 참조하세요.
- port: 1024 - 65535 방화벽이 있는 경우 존재할 수도 있고 없을 수도 있습니다.

### 게시되지 않은 SSU2 주소

router가 SSU1과 SSU2 연결을 모두 지원하지만 들어오는 연결에 대한 자동 버전 감지를 구현하지 않는 경우, "SSU"와 "SSU2" 주소를 모두 광고해야 하며, SSU2 옵션은 "SSU2" 주소에만 포함해야 합니다. router는 SSU2가 우선되도록 "SSU2" 주소에 "SSU" 주소보다 낮은 비용 값(높은 우선순위)을 설정해야 합니다.

만약 여러 개의 SSU2 RouterAddress들이 (SSU 또는 SSU2로) 동일한 RouterInfo에 게시되는 경우 (추가 IP 주소나 포트를 위해), 동일한 포트를 지정하는 모든 주소는 동일한 SSU2 옵션과 값을 포함해야 합니다. 특히, 모든 주소는 동일한 정적 키 "s"와 소개 키 "i"를 포함해야 합니다.

- s=(Base64 키) 이 RouterAddress에 대한 현재 Noise static 공개 키(s). 표준 I2P Base 64 알파벳을 사용하여 Base 64로 인코딩됨. 바이너리로 32바이트, Base 64 인코딩으로 44바이트, little-endian X25519 공개 키.
- i=(Base64 키) 이 RouterAddress에 대한 헤더 암호화를 위한 현재 introduction 키. 표준 I2P Base 64 알파벳을 사용하여 Base 64로 인코딩됨. 바이너리로 32바이트, Base 64 인코딩으로 44바이트, big-endian ChaCha20 키.
- v=2 현재 버전(2). "SSU"로 게시될 때 버전 1에 대한 추가 지원이 암시됨. 향후 버전에 대한 지원은 쉼표로 구분된 값으로 제공됨 (예: v=2,3). 구현체는 쉼표가 있을 경우 여러 버전을 포함하여 호환성을 확인해야 함. 쉼표로 구분된 버전은 숫자 순서로 배열되어야 함.

introducer와 함께 SSU 또는 SSU2로 게시될 때, 다음 옵션들이 존재합니다:

다음 옵션들은 SSU 전용이며 SSU2에서는 사용되지 않습니다. SSU2에서는 Alice가 Charlie의 RI에서 이 정보를 대신 가져옵니다.

router는 introducer를 게시할 때 주소에 호스트나 포트를 게시해서는 안 됩니다. router는 IPv4 및/또는 IPv6 지원을 나타내기 위해 introducer를 게시할 때 주소에 4 및/또는 6 caps를 게시해야 합니다. 이는 최근 SSU 1 주소에 대한 현재 관행과 동일합니다.

참고: SSU로 게시되고 SSU 1과 SSU2 introducer가 혼재되어 있는 경우, 구형 router와의 호환성을 위해 SSU 1 introducer는 낮은 인덱스에, SSU2 introducer는 높은 인덱스에 위치해야 합니다.

Alice가 수신 연결을 위해 자신의 SSU2 주소를("SSU" 또는 "SSU2"로) 게시하지 않는 경우, Bob이 Session Confirmed part 2에서 Alice의 RouterInfo를 받은 후 키를 검증할 수 있도록 정적 키와 SSU2 버전만 포함하는 "SSU2" router 주소를 게시해야 합니다.

#### 오류 처리

이 router 주소는 아웃바운드 SSU2 연결에는 필요하지 않으므로 "host"나 "port" 옵션을 포함하지 않습니다. 이 주소에 대한 공개된 비용은 인바운드 전용이므로 엄격하게 중요하지 않습니다. 하지만 다른 주소보다 비용을 더 높게(우선순위를 낮게) 설정하면 다른 router들에게 도움이 될 수 있습니다. 권장값은 14입니다.

- ih[0-2]=(Base64 hash) introducer의 router hash. 표준 I2P Base 64 알파벳을 사용하여 Base 64로 인코딩됨. 바이너리로 32바이트, Base 64 인코딩으로 44바이트
- iexp[0-2]: 이 introducer의 만료 시간. SSU 1에서 변경되지 않음.
- itag[0-2]: Introducer의 태그 1 - (2**32 - 1) SSU 1에서 변경되지 않음.

Alice는 기존에 게시된 "SSU" 주소에 "i", "s", "v" 옵션을 간단히 추가할 수도 있습니다.

- ihost[0-2]
- ikey[0-2]
- itag[0-2]

NTCP2와 SSU2에 동일한 정적 키를 사용하는 것은 허용되지만 권장되지 않습니다.

RouterInfo의 캐싱으로 인해, router는 실행 중일 때 정적 공개 키나 IV를 순환시켜서는 안 됩니다. 이는 게시된 주소에 있든 없든 마찬가지입니다. Router는 즉시 재시작 후 재사용을 위해 이 키와 IV를 지속적으로 저장해야 하므로, 들어오는 연결이 계속 작동하고 재시작 시간이 노출되지 않습니다. Router는 시작 시 이전 다운타임을 계산할 수 있도록 마지막 종료 시간을 지속적으로 저장하거나 달리 결정해야 합니다.

### 공개 키 및 IV 순환

재시작 시간 노출에 대한 우려를 고려하여, router가 이전에 상당한 시간(최소 며칠) 동안 중단되었던 경우 시작 시 이 키 또는 IV를 회전할 수 있습니다.

- s=(Base64 key) 게시된 주소에 대해 위에서 정의된 대로.
- i=(Base64 key) 게시된 주소에 대해 위에서 정의된 대로.
- v=2 게시된 주소에 대해 위에서 정의된 대로.

router가 게시된 SSU2 RouterAddress를 가지고 있다면 (SSU 또는 SSU2로), 로컬 IP 주소가 변경되었거나 router가 "rekeys"를 수행하지 않는 한, 순환 전 최소 다운타임은 훨씬 길어야 하며, 예를 들어 한 달 정도가 적절합니다.

router가 SSU RouterAddress를 게시했지만 SSU2(SSU 또는 SSU2로)는 없는 경우, 로컬 IP 주소가 변경되었거나 router가 "rekeys"하지 않는 한, 순환 전 최소 다운타임은 더 길어야 하며, 예를 들어 하루 정도가 적절합니다. 이는 게시된 SSU 주소에 introducer가 있는 경우에도 적용됩니다.

### 아웃바운드 패킷 생성

router가 게시된 RouterAddress(SSU, SSU2, 또는 SSU)를 갖지 않는 경우, router가 "rekey"하지 않는 한 IP 주소가 변경되더라도 순환 전 최소 다운타임은 2시간 정도로 짧을 수 있습니다.

router가 다른 Router Hash로 "rekey"하는 경우, 새로운 noise key와 intro key도 생성해야 합니다.

구현체들은 정적 공개 키나 IV를 변경하면 이전 RouterInfo를 캐시한 router들로부터의 SSU2 연결 수신이 차단된다는 점을 인지해야 합니다. RouterInfo 게시, tunnel 피어 선택(OBGW와 IB closest hop 모두 포함), zero-hop tunnel 선택, 전송 선택, 그리고 기타 구현 전략들은 이 점을 고려해야 합니다.

Intro key rotation은 key rotation과 동일한 규칙을 따릅니다.

참고: 네트워크 상태를 보장하고 적당한 시간 동안 다운된 router가 reseeding하는 것을 방지하기 위해 rekeying 전 최소 다운타임이 수정될 수 있습니다.

부인 가능성(Deniability)은 목표가 아닙니다. 위의 개요를 참조하세요.

각 패턴에는 개시자의 정적 공개 키와 응답자의 정적 공개 키에 제공되는 기밀성을 설명하는 속성이 할당됩니다. 기본 가정은 임시 개인 키가 안전하며, 당사자들이 신뢰하지 않는 정적 공개 키를 상대방으로부터 받으면 핸드셰이크를 중단한다는 것입니다.

이 섹션은 핸드셰이크의 정적 공개 키 필드를 통한 신원 누출만을 고려합니다. 물론 Noise 참가자의 신원은 페이로드 필드, 트래픽 분석, 또는 IP 주소와 같은 메타데이터를 포함한 다른 수단을 통해 노출될 수 있습니다.

Alice: (8) 인증된 당사자에게 전진 보안(forward secrecy)으로 암호화됨.

Bob: (3) 전송되지 않지만, 수동적 공격자가 응답자의 개인 키 후보들을 확인하여 해당 후보가 올바른지 판단할 수 있습니다.

#### 익명성 보호

Bob은 자신의 정적 공개 키를 netDb에 게시합니다. Alice는 그럴 필요가 없지만, Bob에게 보내는 RI에 이를 포함해야 합니다.

Handshake 메시지 (Session Request/Created/Confirmed, Retry) 기본 단계, 순서대로:

데이터 단계 메시지 기본 단계들, 순서대로:

모든 인바운드 메시지의 초기 처리:

핸드셰이크 메시지 (Session Request/Created/Confirmed, Retry, Token Request) 및 기타 세션 외 메시지 (Peer Test, Hole Punch) 처리:

데이터 단계 메시지 처리:

## 패킷 가이드라인

### 인바운드 패킷 처리

SSU 1에서는 세션 번호를 나타내는 헤더가 없기 때문에 인바운드 패킷 분류가 어렵습니다. router는 먼저 소스 IP와 포트를 기존 피어 상태와 매칭해야 하고, 찾지 못할 경우 적절한 피어 상태를 찾거나 새로운 상태를 시작하기 위해 다른 키들로 여러 번의 복호화를 시도해야 합니다. NAT 동작 등으로 인해 기존 세션의 소스 IP나 포트가 변경되는 경우, router는 패킷을 기존 세션과 매칭하고 내용을 복구하기 위해 비용이 많이 드는 휴리스틱을 사용할 수 있습니다.

- 16 또는 32바이트 헤더 생성
- 페이로드 생성
- 헤더에 대해 mixHash() 수행 (Retry 제외)
- Noise를 사용하여 페이로드 암호화 (Retry 제외, 헤더를 AD로 사용하여 ChaChaPoly 사용)
- 헤더 암호화, Session Request/Created의 경우 ephemeral key도 함께 암호화

SSU 2는 DPI 저항성과 기타 경로상 위협을 유지하면서 인바운드 패킷 분류 작업을 최소화하도록 설계되었습니다. Connection ID 번호는 모든 메시지 유형의 헤더에 포함되며, 알려진 키와 nonce를 사용하여 ChaCha20으로 암호화(난독화)됩니다. 또한 메시지 유형도 헤더에 포함되며(알려진 키에 대한 헤더 보호로 암호화된 후 ChaCha20으로 난독화됨) 추가 분류를 위해 사용될 수 있습니다. 어떤 경우에도 패킷을 분류하기 위해 시행착오 DH나 기타 비대칭 암호화 연산이 필요하지 않습니다.

- 16바이트 헤더 생성
- 페이로드 생성
- 헤더를 AD로 사용하여 ChaChaPoly로 페이로드 암호화
- 헤더 암호화

### 참고사항

#### 요약

거의 모든 피어로부터 오는 모든 메시지에 대해, Connection ID 암호화를 위한 ChaCha20 키는 netDb에 게시된 목적지 router의 introduction key입니다.

- intro key로 헤더의 첫 8바이트(Destination Connection ID)를 복호화
- Destination Connection ID로 연결을 조회
- 연결이 발견되고 데이터 단계에 있으면, 데이터 단계 섹션으로 이동
- 연결이 발견되지 않으면, handshake 섹션으로 이동
- 참고: Peer Test 및 Hole Punch 메시지도 테스트 또는 릴레이 nonce에서 생성된 Destination Connection ID로 조회될 수 있음.

유일한 예외는 Bob이 Alice에게 보내는 첫 번째 메시지들(Session Created 또는 Retry)로, 이때 Alice의 introduction key가 Bob에게 아직 알려지지 않은 경우입니다. 이러한 경우에는 Bob의 introduction key가 키로 사용됩니다.

- intro key로 헤더의 8-15바이트(패킷 유형, 버전, net ID)를 복호화합니다. 유효한 Session Request, Token Request, Peer Test 또는 Hole Punch인 경우 계속 진행
- 유효한 메시지가 아닌 경우, 패킷 소스 IP/포트로 보류 중인 아웃바운드 연결을 조회하고, 패킷을 Session Created 또는 Retry로 처리합니다. 올바른 키로 헤더의 첫 8바이트와 헤더의 8-15바이트(패킷 유형, 버전, net ID)를 다시 복호화합니다. 유효한 Session Created 또는 Retry인 경우 계속 진행
- 유효한 메시지가 아닌 경우 실패하거나, 순서가 맞지 않을 수 있는 데이터 단계 패킷으로 대기열에 추가
- Session Request/Created, Retry, Token Request, Peer Test, Hole Punch의 경우 헤더의 16-31바이트를 복호화
- Session Request/Created의 경우 임시 키를 복호화
- 모든 헤더 필드를 검증하고, 유효하지 않으면 중단
- 헤더를 mixHash()
- Session Request/Created/Confirmed의 경우 Noise를 사용하여 페이로드 복호화
- Retry 및 데이터 단계의 경우 ChaChaPoly를 사용하여 페이로드 복호화
- 헤더와 페이로드 처리

이 프로토콜은 여러 폴백 단계에서 추가적인 암호화 작업이나 복잡한 휴리스틱이 필요할 수 있는 패킷 분류 처리를 최소화하도록 설계되었습니다. 또한, 수신된 패킷의 대부분은 소스 IP/포트에 의한 (비용이 많이 들 수 있는) 폴백 조회와 두 번째 헤더 복호화가 필요하지 않습니다. Session Created와 Retry (그리고 향후 결정될 기타 유형들)만 폴백 처리가 필요합니다. 세션 생성 후 엔드포인트가 IP나 포트를 변경하더라도, 연결 ID는 여전히 세션을 찾는 데 사용됩니다. 예를 들어 같은 IP를 가지지만 다른 포트를 가진 다른 세션을 찾는 것과 같은 휴리스틱을 사용하여 세션을 찾을 필요는 전혀 없습니다.

- 올바른 키를 사용하여 헤더의 8-15번째 바이트(패킷 타입, 버전, net ID)를 복호화합니다
- 헤더를 AD로 사용하여 ChaChaPoly로 페이로드를 복호화합니다
- 헤더와 페이로드를 처리합니다

#### 세부 정보

따라서 수신기 루프 로직에서 권장되는 처리 단계는 다음과 같습니다:

1) 로컬 introduction key를 사용하여 ChaCha20으로 처음 8바이트를 복호화하여 Destination Connection ID를 복구합니다. Connection ID가 현재 또는 대기 중인 인바운드 세션과 일치하는 경우:

2) 연결 ID가 현재 세션과 일치하지 않는 경우: 8-15 바이트의 평문 헤더가 유효한지 확인합니다 (헤더 보호 작업을 수행하지 않고). net ID와 프로토콜 버전이 유효한지 확인하고, 메시지 유형이 Session Request이거나 세션 외부에서 허용되는 다른 메시지 유형인지 확인합니다 (TBD).

3) 패킷의 소스 IP/포트로 대기 중인 아웃바운드 세션을 찾아보세요.

4) 같은 포트에서 SSU 1을 실행 중인 경우, 메시지를 SSU 1 패킷으로 처리하려고 시도합니다.

일반적으로 세션(핸드셰이크 또는 데이터 단계)은 예상치 못한 메시지 타입의 패킷을 수신한 후에 절대 파기되어서는 안 됩니다. 이는 패킷 주입 공격을 방지합니다. 이러한 패킷들은 또한 핸드셰이크 패킷의 재전송 후에, 헤더 복호화 키가 더 이상 유효하지 않을 때 흔히 수신됩니다.

대부분의 경우, 단순히 패킷을 드롭합니다. 구현체는 응답으로 이전에 전송된 패킷(handshake 메시지 또는 ACK 0)을 재전송할 수 있지만 필수는 아닙니다.

    a)  Using the appropriate key, decrypt the header bytes 8-15 to recover the version, net ID, and message type.
    b)  If the message type is Session Confirmed, it is a long header. Verify the net ID and protocol version are valid. Decrypt the bytes 15-31 of the header with ChaCha20 using the local intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise.
    c)  If the message type is valid but not Session Confirmed, it is a short header. Verify the net ID and protocol version are valid. decrypt the rest of the message with ChaCha20/Poly1305 using the session key, using the decrypted 16-byte header as the AD.
    d)  (optional) If connection ID is a pending inbound session awaiting a Session Confirmed message, but the net ID, protocol, or message type is not valid, it could be a Data message received out-of-order before the Session Confirmed, so the data phase header protection keys are not yet known, and the header bytes 8-15 were incorrectly decrypted. Queue the message, and attempt to decrypt it once the Session Confirmed message is received.
    e)  If b) or c) fails, drop the message.

Bob으로서 Session Created를 전송한 후, 예상치 못한 패킷들은 일반적으로 Session Confirmed 패킷들이 손실되거나 순서가 바뀌어서 복호화할 수 없는 Data 패킷들입니다. 패킷들을 큐에 저장하고 Session Confirmed 패킷들을 받은 후에 복호화를 시도하세요.

    a)  If all is valid and the message type is Session Request, decrypt bytes 16-31 of the header and the 32-byte X value with ChaCha20 using the local intro key.

    - If the token at header bytes 24-31 is accepted, then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Created in response.
    - If the token is not accepted, send a Retry message to the source IP/port with a token. Do not attempt to decrypt the message with Noise to avoid DDoS attacks.

    b)  If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.
    c)  If a) or b) fails, go to step 3)

Bob으로서 Session Confirmed를 받은 후, 예상치 못한 패킷들은 일반적으로 재전송된 Session Confirmed 패킷들입니다. 이는 Session Confirmed의 ACK 0이 손실되었기 때문입니다. 예상치 못한 패킷들은 드롭될 수 있습니다. 구현체는 응답으로 ACK 블록을 포함하는 Data 패킷을 전송할 수 있지만, 필수는 아닙니다.

    a)  If found, re-decrypt the first 8 bytes with ChaCha20 using Bob's introduction key to recover the Destination Connection ID.
    b)  If the connection ID matches the pending session: Using the correct key, decrypt bytes 8-15 of the header to recover the version, net ID, and message type. Verify the net ID and protocol version are valid, and the message type is Session Created or Retry, or other message type allowed out-of-session (TBD).

    - If all is valid and the message type is Session Created, decrypt the next 16 bytes of the header and the 32-byte Y value with ChaCha20 using Bob's intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Confirmed in response.
    - If all is valid and the message type is Retry, decrypt bytes 16-31 of the header with ChaCha20 using Bob's intro key. Decrypt and validate the message using ChaCha20/Poly1305 using TBD as the key and TBD as the nonce and the decrypted 32-byte header as the AD. Resend a Session Request with the received token in response.
    - If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.

    > c)  If a pending outbound session is not found, or the connection ID does not match the pending session, drop the message, unless the port is shared with SSU 1.

Session Created와 Session Confirmed의 경우, 구현체는 헤더에서 mixHash()를 호출하고 Noise AEAD로 페이로드를 복호화하려고 시도하기 전에 모든 복호화된 헤더 필드(Connection ID, 패킷 번호, 패킷 유형, 버전, id, frag, 플래그)를 주의 깊게 검증해야 합니다. Noise AEAD 복호화가 실패하면, 구현체가 해시 상태를 저장하고 "되돌리지" 않는 한, mixHash()가 핸드셰이크 상태를 손상시킬 것이므로 더 이상의 처리를 수행할 수 없습니다.

#### 오류 처리

동일한 인바운드 포트에서 들어오는 패킷이 버전 1인지 2인지 효율적으로 감지하는 것이 불가능할 수 있습니다. 위의 단계들은 두 프로토콜 버전을 모두 사용한 시행착오 DH 연산을 시도하는 것을 피하기 위해 SSU 1 처리 전에 수행하는 것이 합리적일 수 있습니다.

필요 시 추후 결정.

IPv4를 가정하며, 추가 패딩은 포함하지 않고, IP 및 UDP 헤더 크기는 포함하지 않습니다. 패딩은 SSU 1에서만 mod-16 패딩입니다.

**SSU 1**

### 버전 감지

**SSU 2**

### 토큰

위에서 토큰은 랜덤으로 생성된 8바이트 값이어야 하며, 재사용 공격으로 인해 서버 비밀과 IP, 포트의 해시나 HMAC과 같은 불투명한 값을 생성하지 않아야 한다고 명시했습니다. 하지만 이는 전달된 토큰의 임시적이고 (선택적으로) 영구적인 저장을 필요로 합니다. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf)는 서버 비밀과 IP 주소의 16바이트 HMAC을 사용하며, 서버 비밀은 2분마다 순환됩니다. 더 긴 서버 비밀 수명을 가진 유사한 방법을 조사해야 합니다. 토큰에 타임스탬프를 포함시킨다면 해결책이 될 수 있지만, 8바이트 토큰은 그런 용도로는 충분하지 않을 수 있습니다.

필요한지 아직 결정되지 않음.

## 권장 상수

- 아웃바운드 핸드셰이크 재전송 타임아웃: 1.25초, 지수적 백오프 적용 (1.25초, 3.75초, 8.75초에 재전송)
- 총 아웃바운드 핸드셰이크 타임아웃: 15초
- 인바운드 핸드셰이크 재전송 타임아웃: 1초, 지수적 백오프 적용 (1초, 3초, 7초에 재전송)
- 총 인바운드 핸드셰이크 타임아웃: 12초
- 재시도 전송 후 타임아웃: 9초
- ACK 지연: max(10, min(rtt/6, 150)) ms
- 즉시 ACK 지연: min(rtt/16, 5) ms
- 최대 ACK 범위: 256?
- 최대 ACK 깊이: 512?
- 패딩 분포: 0-15 바이트, 또는 그 이상
- 데이터 단계 최소 재전송 타임아웃: 1초, [RFC-6298](https://tools.ietf.org/html/rfc6298)에 따름
- 데이터 단계의 재전송 타이머에 대한 추가 지침은 [RFC-6298](https://tools.ietf.org/html/rfc6298)도 참조하세요.

## 패킷 오버헤드 분석

IPv4을 가정하며, 추가 패딩은 포함하지 않고, IP 및 UDP 헤더 크기도 포함하지 않습니다. 패딩은 SSU 1에서만 모드-16 패딩입니다.

**SSU 1**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MAC</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">40</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">304</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. extended options</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">79</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">336</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 64 byte Ed25519 sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">462</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">512</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 391 byte ident and 64 byte sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (RI)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1014</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1051</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header, 1000 byte RI</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">51</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">2254</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>
**SSU 2**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MACs</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">87</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">96</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime, Address blocks</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1005</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1085</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1000 byte compressed RI block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">46</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1314</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>    
## 문제점 및 향후 작업

### 토큰

위에서 언급했듯이, 재사용 공격을 방지하기 위해 토큰은 서버 비밀값과 IP, 포트의 해시 또는 HMAC처럼 불투명한 값을 생성하는 것이 아니라, 무작위로 생성된 8바이트 값이어야 한다고 명시합니다. 그러나 이 방식은 전달된 토큰의 일시적 저장뿐 아니라 (선택적으로) 영구 저장도 필요로 합니다. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf)는 서버 비밀값과 IP 주소를 기반으로 16바이트 HMAC을 사용하며, 서버 비밀값은 2분마다 교체됩니다. 우리는 비슷한 방식을 조사해볼 필요가 있으며, 서버 비밀값의 수명을 더 길게 설정하는 것이 좋을 수 있습니다. 토큰 내에 타임스탬프를 포함시킨다면 그 자체로 해결책이 될 수 있지만, 8바이트 토큰은 그 용량이 충분하지 않을 수 있습니다.

## 참고 자료

- **[Common]** [공통 구조 명세](/docs/specs/common-structures)
- **[ECIES]** [ECIES-X25519-AEAD-Ratchet 명세](/docs/specs/ecies)
- **[netDb]** [네트워크 데이터베이스](/docs/overview/network-database)
- **[NOISE]** [Noise Protocol Framework](https://noiseprotocol.org/noise.html)
- **[Nonces]** [Nonce-Disrespecting Adversaries](https://eprint.iacr.org/2019/624.pdf)
- **[NTCP]** [NTCP 전송](/docs/transport/ntcp)
- **[NTCP2]** [NTCP2 명세](/docs/specs/ntcp2)
- **[PMTU]** [Path MTU Discovery](https://en.wikipedia.org/wiki/Path_MTU_Discovery)
- **[Prop104]** [제안서 104: TLS 전송](/proposals/104-tls-transport)
- **[Prop109]** [제안서 109: 플러그 가능 전송](/proposals/109-pt-transport)
- **[Prop158]** [제안서 158: IPv6 전송 향상](/proposals/158-ipv6-transport-enhancements)
- **[Prop159]** [제안서 159: SSU2](/proposals/159-ssu2)
- **[RFC-2104]** [RFC 2104: HMAC](https://tools.ietf.org/html/rfc2104)
- **[RFC-3449]** [RFC 3449: TCP 성능 영향](https://tools.ietf.org/html/rfc3449)
- **[RFC-3526]** [RFC 3526: MODP Groups](https://tools.ietf.org/html/rfc3526)
- **[RFC-5681]** [RFC 5681: TCP 혼잡 제어](https://tools.ietf.org/html/rfc5681)
- **[RFC-5869]** [RFC 5869: HKDF](https://tools.ietf.org/html/rfc5869)
- **[RFC-6151]** [RFC 6151: MD5 보안 고려사항](https://tools.ietf.org/html/rfc6151)
- **[RFC-6298]** [RFC 6298: TCP 재전송 타이머](https://tools.ietf.org/html/rfc6298)
- **[RFC-6437]** [RFC 6437: IPv6 플로우 레이블](https://tools.ietf.org/html/rfc6437)
- **[RFC-7539]** [RFC 7539: ChaCha20/Poly1305](https://tools.ietf.org/html/rfc7539)
- **[RFC-7748]** [RFC 7748: 보안용 타원곡선](https://tools.ietf.org/html/rfc7748)
- **[RFC-7905]** [RFC 7905: TLS용 ChaCha20-Poly1305 암호 스위트](https://tools.ietf.org/html/rfc7905)
- **[RFC-9000]** [RFC 9000: QUIC 전송 프로토콜](https://datatracker.ietf.org/doc/html/rfc9000)
- **[RFC-9001]** [RFC 9001: TLS를 사용한 QUIC 보안](https://datatracker.ietf.org/doc/html/rfc9001)
- **[RFC-9002]** [RFC 9002: QUIC 손실 탐지 및 혼잡 제어](https://datatracker.ietf.org/doc/html/rfc9002)
- **[RouterAddress]** [RouterAddress 구조](/docs/specs/common-structures#struct-routeraddress)
- **[RouterIdentity]** [RouterIdentity 구조](/docs/specs/common-structures#struct-routeridentity)
- **[SigningPublicKey]** [SigningPublicKey 타입](/docs/specs/common-structures#type-signingpublickey)
- **[SSU]** [SSU 전송](/docs/transport/ssu)
- **[STS]** [Station-to-Station Protocol](https://en.wikipedia.org/wiki/Station-to-Station_protocol)
- **[Ticket1112]** [I2P 티켓 1112](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1112)
- **[Ticket1849]** [I2P 티켓 1849](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1849)
- **[WireGuard]** [WireGuard Protocol](https://www.wireguard.com/papers/wireguard.pdf)
