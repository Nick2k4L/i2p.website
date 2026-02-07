---
title: "암호화된 LeaseSet 명세서"
description: "암호화된 leaseSet의 블라인딩, 암호화 및 복호화"
slug: "encryptedleaseset"
category: "프로토콜"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## 개요

이 문서는 암호화된 leaseset의 블라인딩, 암호화, 복호화를 명시합니다. 암호화된 leaseset의 구조에 대해서는 [공통 구조 명세](/docs/specs/common-structures)를 참조하세요. 암호화된 leaseset의 배경 정보는 [제안서 123](/proposals/123-new-netdb-entries)을 참조하세요. netDb에서의 사용법은 netDb 문서를 참조하세요.

### 정의

암호화된 LS2에 사용되는 암호화 구성 요소에 해당하는 다음 함수들을 정의합니다:

**CSRNG(n)** : 암호학적으로 안전한 난수 생성기에서 출력되는 n바이트.

CSRNG가 암호학적으로 안전해야 한다는 요구사항(따라서 키 자료 생성에 적합함)에 더하여, n바이트 출력이 키 자료로 사용될 때 그 직전과 직후의 바이트 시퀀스가 네트워크에 노출되더라도(salt나 암호화된 패딩 등에서처럼) 안전해야 합니다. 잠재적으로 신뢰할 수 없는 소스에 의존하는 구현은 네트워크에 노출될 모든 출력을 해시해야 합니다 [PRNG-REFS](http://projectbullrun.org/dual-ec/ext-rand.html).

**H(p, d)** : 개인화 문자열 p와 데이터 d를 입력받아 32바이트 길이의 출력을 생성하는 SHA-256 해시 함수.

SHA-256을 다음과 같이 사용하세요:

```
H(p, d) := SHA-256(p || d)
```
**STREAM** : [RFC-7539-S2.4](https://tools.ietf.org/html/rfc7539#section-2.4)에 명시된 ChaCha20 스트림 암호화 방식으로, 초기 카운터는 1로 설정됩니다. S_KEY_LEN = 32이고 S_IV_LEN = 12입니다.

- **ENCRYPT(k, iv, plaintext)** : 암호화 키 k와 논스 iv를 사용하여 평문을 암호화합니다. 논스 iv는 키 k에 대해 반드시 고유해야 합니다. 평문과 동일한 크기의 암호문을 반환합니다. 키가 비밀로 유지되는 경우 전체 암호문은 랜덤 데이터와 구별할 수 없어야 합니다.

- **DECRYPT(k, iv, ciphertext)** : 암호화 키 k와 nonce iv를 사용하여 ciphertext를 복호화합니다. 평문을 반환합니다.

**SIG** : 키 블라인딩(key blinding)을 사용하는 Red25519 서명 방식 (SigType 11에 해당). 다음과 같은 기능을 가집니다:

- **DERIVE_PUBLIC(privkey)** : 주어진 개인 키에 해당하는 공개 키를 반환합니다.

- **SIGN(privkey, m)** : 주어진 메시지 m에 대해 개인키 privkey로 서명을 반환합니다.

- **VERIFY(pubkey, m, sig)** : 공개 키 pubkey와 메시지 m에 대해 서명 sig를 검증합니다. 서명이 유효하면 true를, 그렇지 않으면 false를 반환합니다.

또한 다음과 같은 키 블라인딩 연산을 지원해야 합니다:

- **GENERATE_ALPHA(data, secret)** : 데이터와 선택적 비밀을 알고 있는 사람들을 위한 알파를 생성합니다. 결과는 개인 키와 동일하게 분산되어야 합니다.

- **BLIND_PRIVKEY(privkey, alpha)** : 비밀 alpha를 사용하여 개인 키를 블라인드합니다.

- **BLIND_PUBKEY(pubkey, alpha)** : 비밀 alpha를 사용하여 공개 키를 블라인드합니다. 주어진 키 쌍 (privkey, pubkey)에 대해 다음 관계가 성립합니다:

```
BLIND_PUBKEY(pubkey, alpha) ==
DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))
```
**DH** : X25519 공개 키 합의 시스템. 32바이트의 개인 키, 32바이트의 공개 키, 32바이트의 출력을 생성합니다. 다음과 같은 기능들을 가지고 있습니다:

- **GENERATE_PRIVATE()** : 새로운 개인 키를 생성합니다.

- **DERIVE_PUBLIC(privkey)** : 주어진 개인 키에 해당하는 공개 키를 반환합니다.

- **DH(privkey, pubkey)** : 주어진 개인키와 공개키로부터 공유 비밀을 생성합니다.

**HKDF(salt, ikm, info, n)** : 일부 입력 키 자료 ikm (좋은 엔트로피를 가져야 하지만 균등하게 무작위인 문자열일 필요는 없음), 32바이트 길이의 salt, 그리고 컨텍스트별 'info' 값을 받아서 키 자료로 사용하기에 적합한 n바이트의 출력을 생성하는 암호화 키 유도 함수입니다.

[RFC-5869](https://tools.ietf.org/html/rfc5869)에 명시된 대로 HKDF를 사용하되, [RFC-2104](https://tools.ietf.org/html/rfc2104)에 명시된 HMAC 해시 함수 SHA-256을 사용합니다. 이는 SALT_LEN이 최대 32바이트임을 의미합니다.

### 형식

암호화된 LS2 형식은 세 개의 중첩된 레이어로 구성됩니다:

- 저장 및 검색에 필요한 평문 정보를 포함하는 외부 계층.
- 클라이언트 인증을 처리하는 중간 계층.
- 실제 LS2 데이터를 포함하는 내부 계층.

전체적인 형식은 다음과 같습니다:

```
Layer 0 data + Enc(layer 1 data + Enc(layer 2 data)) + Signature
```
암호화된 LS2는 블라인드(blinded) 처리됩니다. Destination은 헤더에 포함되지 않습니다. DHT 저장 위치는 SHA-256(sig type || blinded public key)이며, 매일 순환됩니다.

위에 명시된 표준 LS2 헤더를 사용하지 않습니다.

#### 레이어 0 (외부)

**Type** : 1바이트

실제로는 헤더에 있지 않지만, 서명으로 보호되는 데이터의 일부입니다. Database Store Message의 필드에서 가져옵니다.

**Blinded Public Key Sig Type** : 2바이트, 빅 엔디언

이것은 항상 타입 11이며, Red25519 블라인드 키를 식별합니다.

**Blinded Public Key** : sig type에 의해 암시되는 길이

**Published timestamp** : 4바이트, 빅 엔디언

epoch 이후의 초, 2106년에 롤오버됨

**Expires** : 2바이트, 빅 엔디안

게시된 타임스탬프로부터의 초 단위 오프셋, 최대 18.2시간

**플래그** : 2바이트

비트 순서: 15 14 ... 3 2 1 0

- 비트 0: 0이면 오프라인 키 없음; 1이면 오프라인 키 있음
- 다른 비트들: 향후 사용과의 호환성을 위해 0으로 설정

**임시 키 데이터** : 플래그가 오프라인 키를 나타내는 경우 존재

- **Expires timestamp** : 4바이트, 빅 엔디안. 에포크 이후 초 단위, 2106년에 롤오버됨
- **Transient sig type** : 2바이트, 빅 엔디안
- **Transient signing public key** : sig type에 의해 암시되는 길이
- **Signature** : blinded public key sig type에 의해 암시되는 길이. expires timestamp, transient sig type, transient public key에 대한 서명. blinded public key로 검증됨.

**lenOuterCiphertext** : 2바이트, 빅 엔디안

**outerCiphertext** : lenOuterCiphertext 바이트

암호화된 레이어 1 데이터. 키 유도 및 암호화 알고리즘은 아래를 참조하십시오.

**서명** : 사용된 서명 키의 sig type에 따라 결정되는 길이

서명은 위의 모든 내용에 대한 것입니다. 플래그가 오프라인 키를 나타내는 경우, 서명은 임시 공개 키로 검증됩니다. 그렇지 않으면, 서명은 블라인드된 공개 키로 검증됩니다.

#### 레이어 1 (중간)

**플래그** : 1바이트

비트 순서: 76543210

- 비트 0: 모든 사용자는 0, 클라이언트별은 1, 인증 섹션이 뒤따름
- 비트 3-1: 인증 방식, 비트 0이 클라이언트별로 1로 설정된 경우에만 해당, 그렇지 않으면 000
  - 000: DH 클라이언트 인증 (또는 클라이언트별 인증 없음)
  - 001: PSK 클라이언트 인증
- 비트 7-4: 사용되지 않음, 향후 호환성을 위해 0으로 설정

**DH 클라이언트 인증 데이터** : 플래그 비트 0이 1로 설정되고 플래그 비트 3-1이 000으로 설정된 경우 존재합니다.

- **ephemeralPublicKey** : 32바이트
- **clients** : 2바이트, 빅 엔디안. 뒤따를 authClient 항목 수, 각각 40바이트
- **authClient** : 단일 클라이언트에 대한 인증 데이터. 클라이언트별 인증 알고리즘은 아래를 참조하세요.
  - **clientID_i** : 8바이트
  - **clientCookie_i** : 32바이트

**PSK 클라이언트 인증 데이터** : 플래그 비트 0이 1로 설정되고 플래그 비트 3-1이 001로 설정된 경우 존재합니다.

- **authSalt** : 32바이트
- **clients** : 2바이트, 빅 엔디안. 뒤따를 authClient 항목의 개수, 각각 40바이트
- **authClient** : 단일 클라이언트에 대한 인증 데이터. 클라이언트별 인증 알고리즘은 아래를 참조하세요.
  - **clientID_i** : 8바이트
  - **clientCookie_i** : 32바이트

**innerCiphertext** : lenOuterCiphertext에 의해 암시된 길이 (남은 모든 데이터)

암호화된 레이어 2 데이터입니다. 키 유도 및 암호화 알고리즘은 아래를 참조하세요.

#### 레이어 2 (내부)

**타입** : 1바이트

3 (LS2) 또는 7 (Meta LS2)

**Data** : 주어진 타입에 대한 LeaseSet2 데이터.

헤더와 서명을 포함합니다.

### 블라인딩 키 유도

우리는 Ed25519와 ZCash RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)를 기반으로 하는 다음 키 블라인딩 방식을 사용합니다. Red25519 서명은 해시에 SHA-512를 사용하여 Ed25519 곡선 위에서 이루어집니다.

유사한 설계 목표를 가진 Tor의 rend-spec-v3.txt 부록 A.2 [TOR-REND-SPEC-V3](https://spec.torproject.org/rend-spec-v3)는 사용하지 않습니다. 왜냐하면 해당 방식의 blinded public key가 prime-order subgroup에서 벗어날 수 있어 보안상 알려지지 않은 문제점이 있을 수 있기 때문입니다.

#### 목표

- 언블라인드된 destination의 서명 공개 키는 Ed25519 (sig type 7) 또는 Red25519 (sig type 11)이어야 함; 다른 sig type은 지원되지 않음
- 서명 공개 키가 오프라인인 경우, 임시 서명 공개 키 또한 Ed25519이어야 함
- 블라인딩은 계산적으로 단순함
- 기존 암호화 프리미티브 사용
- 블라인드된 공개 키는 언블라인드될 수 없음
- 블라인드된 공개 키는 Ed25519 곡선과 소수 차수 부분군에 있어야 함
- 블라인드된 공개 키를 도출하려면 destination의 서명 공개 키를 알아야 함 (전체 destination은 필요하지 않음)
- 선택적으로 블라인드된 공개 키를 도출하는 데 필요한 추가 비밀을 제공

#### 보안

블라인딩 스키마의 보안을 위해서는 알파의 분포가 블라인드되지 않은 개인키와 동일해야 합니다. 그러나 Ed25519 개인키(sig type 7)를 Red25519 개인키(sig type 11)로 블라인드할 때, 분포가 다릅니다. zcash section 4.1.6.1 [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)의 요구사항을 충족하기 위해, Red25519(sig type 11)가 블라인드되지 않은 키에도 사용되어야 합니다. 이는 "재무작위화된 공개키와 해당 키 하에서의 서명(들)의 조합이 재무작위화된 원본 키를 드러내지 않도록" 하기 위함입니다. 기존 destination에 대해서는 type 7을 허용하지만, 암호화될 새로운 destination에는 type 11을 권장합니다.

#### 정의

**B** : [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)에서와 같은 Ed25519 기준점(생성자) 2^255 - 19

**L** : [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)에서와 같은 Ed25519 차수 2^252 + 27742317777372353535851937790883648493

**DERIVE_PUBLIC(a)** : Ed25519에서와 같이 개인 키를 공개 키로 변환 (G로 곱하기)

**alpha** : 목적지를 아는 사람들에게 알려진 32바이트 랜덤 숫자입니다.

**GENERATE_ALPHA(destination, date, secret)** : destination과 secret을 알고 있는 사람들을 위해 현재 날짜에 대한 알파를 생성합니다. 결과는 Ed25519 private key와 동일하게 분포되어야 합니다.

**a** : destination에 서명하는 데 사용되는 블라인딩 해제된 32바이트 EdDSA 또는 RedDSA 서명 개인키

**A** : destination에서 블라인딩 해제된 32바이트 EdDSA 또는 RedDSA 서명 공개 키, = DERIVE_PUBLIC(a), Ed25519에서와 같음

**a'** : 암호화된 leaseset에 서명하는 데 사용되는 블라인드된 32바이트 EdDSA 서명 개인 키입니다. 이는 유효한 EdDSA 개인 키입니다.

**A'** : Destination의 블라인드된 32바이트 EdDSA 서명 공개 키로, DERIVE_PUBLIC(a')로 생성되거나 A와 alpha로부터 생성될 수 있습니다. 이것은 곡선상에 있고 소수 차수 부분군에 속하는 유효한 EdDSA 공개 키입니다.

**LEOS2IP(x)** : 입력 바이트의 순서를 리틀 엔디안으로 뒤집기

**H\*(x)** : 32바이트 = (LEOS2IP(SHA512(x))) mod B, Ed25519 해시-앤-리듀스와 동일

#### Blinding 계산

새로운 비밀 알파와 블라인디드 키는 매일(UTC) 생성되어야 합니다.

비밀 알파와 블라인드된 키들은 다음과 같이 계산됩니다:

GENERATE_ALPHA(destination, date, secret), 모든 당사자에 대해:

```
// secret is optional, else zero-length
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of blinded public key A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
datestring = 8 bytes ASCII YYYYMMDD from the current date UTC
secret = UTF-8 encoded string
seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || secret, "i2pblinding1", 64)
// treat seed as a 64 byte little-endian value
alpha = seed mod L
```
BLIND_PRIVKEY(), leaseSet을 게시하는 소유자용:

```
alpha = GENERATE_ALPHA(destination, date, secret)
// If for a Ed25519 private key (type 7)
seed = destination's signing private key
a = left half of SHA512(seed) and clamped as usual for Ed25519
// else for a Red25519 private key (type 11)
a = destination's signing private key
// Addition using scalar arithmetic
blinded signing private key = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
blinded signing public key = A' = DERIVE_PUBLIC(a')
```
BLIND_PUBKEY(), leaseset을 검색하는 클라이언트들을 위한:

```
alpha = GENERATE_ALPHA(destination, date, secret)
A = destination's signing public key
// Addition using group elements (points on the curve)
blinded public key = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```
A'을 계산하는 두 방법 모두 요구된 대로 동일한 결과를 산출합니다.

#### 서명

언블라인드된 leaseset은 언블라인드된 Ed25519 또는 Red25519 서명 개인키로 서명되고, 평소와 같이 언블라인드된 Ed25519 또는 Red25519 서명 공개키(서명 타입 7 또는 11)로 검증됩니다.

서명 공개 키가 오프라인 상태인 경우, 블라인드되지 않은 leaseset은 블라인드되지 않은 임시 Ed25519 또는 Red25519 서명 개인 키로 서명되고, 평상시와 같이 블라인드되지 않은 Ed25519 또는 Red25519 임시 서명 공개 키(서명 타입 7 또는 11)로 검증됩니다. 암호화된 leaseset에 대한 오프라인 키에 대한 추가 참고 사항은 아래를 참조하세요.

암호화된 leaseset의 서명을 위해, 블라인드 키로 서명하고 검증하기 위해 RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)를 기반으로 한 Red25519를 사용합니다. Red25519 서명은 Ed25519 곡선을 사용하며, 해시로는 SHA-512를 사용합니다.

Red25519는 아래에 명시된 사항을 제외하고는 표준 Ed25519와 유사합니다.

#### 서명/검증 계산

암호화된 leaseset의 외부 부분은 Red25519 키와 서명을 사용합니다.

Red25519는 Ed25519와 유사합니다. 두 가지 차이점이 있습니다:

Red25519 개인 키는 난수로부터 생성된 후 위에서 정의된 L을 법으로 하는 모듈로 연산으로 축소되어야 합니다. Ed25519 개인 키는 난수로부터 생성된 후 바이트 0과 31에 비트별 마스킹을 사용하여 "클램핑"됩니다. 이는 Red25519에서는 수행되지 않습니다. 위에서 정의된 GENERATE_ALPHA() 및 BLIND_PRIVKEY() 함수들은 mod L을 사용하여 적절한 Red25519 개인 키를 생성합니다.

Red25519에서는 서명을 위한 r 계산에 추가적인 랜덤 데이터를 사용하고, 개인키의 해시가 아닌 공개키 값을 사용합니다. 랜덤 데이터 때문에 동일한 키로 동일한 데이터에 서명하더라도 모든 Red25519 서명은 다릅니다.

```
Signing:
  T = 80 random bytes
  r = H*(T || publickey || message)
  (rest is the same as in Ed25519)

Verification:
  Same as for Ed25519
```
### 암호화 및 처리

#### 하위 자격 증명의 파생

블라인딩 과정의 일환으로, 암호화된 LS2가 해당 Destination의 서명 공개 키를 아는 사람만이 복호화할 수 있도록 보장해야 합니다. 전체 Destination은 필요하지 않습니다. 이를 달성하기 위해 서명 공개 키에서 자격 증명을 도출합니다:

```
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
credential = H("credential", keydata)
```
개인화 문자열은 자격 증명이 일반 Destination 해시와 같은 DHT 조회 키로 사용되는 해시와 충돌하지 않도록 보장합니다.

주어진 블라인드 키에 대해, 우리는 서브크리덴셜을 도출할 수 있습니다:

```
subcredential = H("subcredential", credential || blindedPublicKey)
```
subcredential은 아래의 키 유도 과정에 포함되며, 이는 해당 키들을 Destination의 서명 공개 키에 대한 지식과 결합시킵니다.

#### 레이어 1 암호화

먼저, 키 유도 과정에 대한 입력이 준비됩니다:

```
outerInput = subcredential || publishedTimestamp
```
다음으로, 무작위 솔트가 생성됩니다:

```
outerSalt = CSRNG(32)
```
그런 다음 레이어 1을 암호화하는 데 사용되는 키가 도출됩니다:

```
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
마지막으로, 레이어 1 평문이 암호화되고 직렬화됩니다:

```
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```
#### 레이어 1 복호화

salt는 레이어 1 암호문에서 파싱됩니다:

```
outerSalt = outerCiphertext[0:31]
```
그런 다음 레이어 1을 암호화하는 데 사용되는 키가 도출됩니다:

```
outerInput = subcredential || publishedTimestamp
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
마지막으로, 레이어 1 암호문이 복호화됩니다:

```
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```
#### 레이어 2 암호화

클라이언트 인증이 활성화되면 `authCookie`는 아래 설명된 대로 계산됩니다. 클라이언트 인증이 비활성화되면 `authCookie`는 길이가 0인 바이트 배열입니다.

암호화는 레이어 1과 유사한 방식으로 진행됩니다:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = CSRNG(32)
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```
#### 레이어 2 복호화

클라이언트 인증이 활성화되면 `authCookie`는 아래 설명된 대로 계산됩니다. 클라이언트 인증이 비활성화되면 `authCookie`는 길이가 0인 바이트 배열입니다.

복호화는 레이어 1과 유사한 방식으로 진행됩니다:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = innerCiphertext[0:31]
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```
### 클라이언트별 인증

Destination에 대해 클라이언트 인증이 활성화되면, 서버는 암호화된 LS2 데이터를 복호화할 권한을 부여받은 클라이언트 목록을 유지합니다. 클라이언트별로 저장되는 데이터는 인증 메커니즘에 따라 달라지며, 각 클라이언트가 생성하여 보안 대역 외 메커니즘을 통해 서버에 전송하는 키 자료의 형태를 포함합니다.

클라이언트별 인증을 구현하는 두 가지 대안이 있습니다:

#### DH 클라이언트 인증

각 클라이언트는 DH 키 쌍 `[csk_i, cpk_i]`를 생성하고, 공개 키 `cpk_i`를 서버로 전송합니다.

##### 서버 처리

서버는 새로운 `authCookie`와 임시 DH 키쌍을 생성합니다:

```
authCookie = CSRNG(32)
esk = GENERATE_PRIVATE()
epk = DERIVE_PUBLIC(esk)
```
그런 다음 각 인증된 클라이언트에 대해 서버는 `authCookie`를 해당 클라이언트의 공개 키로 암호화합니다:

```
sharedSecret = DH(esk, cpk_i)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
서버는 각 `[clientID_i, clientCookie_i]` 튜플을 `epk`와 함께 암호화된 LS2의 레이어 1에 배치합니다.

##### 클라이언트 처리

클라이언트는 자신의 개인 키를 사용하여 예상되는 클라이언트 식별자 `clientID_i`, 암호화 키 `clientKey_i`, 그리고 암호화 IV `clientIV_i`를 도출합니다:

```
sharedSecret = DH(csk_i, epk)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
그런 다음 클라이언트는 레이어 1 인증 데이터에서 `clientID_i`를 포함하는 항목을 검색합니다. 일치하는 항목이 존재하면, 클라이언트는 이를 복호화하여 `authCookie`를 얻습니다:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### 사전 공유 키 클라이언트 인증

각 클라이언트는 32바이트 비밀 키 `psk_i`를 생성하고, 이를 서버에 전송합니다. 또는 서버가 비밀 키를 생성하여 하나 이상의 클라이언트에게 전송할 수도 있습니다.

##### 서버 처리

서버는 새로운 `authCookie`와 salt를 생성합니다:

```
authCookie = CSRNG(32)
authSalt = CSRNG(32)
```
그런 다음 각 승인된 클라이언트에 대해 서버는 사전 공유 키를 사용하여 `authCookie`를 암호화합니다:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
서버는 각 `[clientID_i, clientCookie_i]` 튜플을 `authSalt`와 함께 암호화된 LS2의 레이어 1에 배치합니다.

##### 클라이언트 처리

클라이언트는 사전 공유 키를 사용하여 예상되는 클라이언트 식별자 `clientID_i`, 암호화 키 `clientKey_i`, 그리고 암호화 IV `clientIV_i`를 도출합니다:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
그런 다음 클라이언트는 `clientID_i`를 포함하는 항목에 대해 레이어 1 인증 데이터를 검색합니다. 일치하는 항목이 존재하면 클라이언트는 이를 복호화하여 `authCookie`를 얻습니다:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### 보안 고려사항

위의 두 클라이언트 인증 메커니즘은 모두 클라이언트 멤버십에 대한 프라이버시를 제공합니다. Destination만 알고 있는 개체는 언제든지 구독된 클라이언트 수를 볼 수 있지만, 어떤 클라이언트가 추가되거나 취소되고 있는지는 추적할 수 없습니다.

서버는 암호화된 LS2를 생성할 때마다 클라이언트의 순서를 무작위화해야 하며, 이는 클라이언트가 목록에서 자신의 위치를 알아내고 다른 클라이언트가 추가되거나 제거된 시점을 추론하는 것을 방지하기 위함입니다.

서버는 인증 데이터 목록에 무작위 항목을 삽입하여 구독 중인 클라이언트 수를 숨기도록 선택할 수 있습니다.

##### DH 클라이언트 인증의 장점

- 스킴의 보안은 클라이언트 키 자료의 대역 외 교환에만 의존하지 않습니다. 클라이언트의 개인 키는 해당 기기를 벗어날 필요가 없으므로, 대역 외 교환을 가로챌 수 있지만 DH 알고리즘을 깨뜨릴 수 없는 공격자는 암호화된 LS2를 복호화하거나 클라이언트에게 얼마나 오랫동안 액세스가 허용되는지 알 수 없습니다.

##### DH 클라이언트 인증의 단점

- N개의 클라이언트에 대해 서버 측에서 N + 1번의 DH 연산이 필요합니다.
- 클라이언트 측에서 한 번의 DH 연산이 필요합니다.
- 클라이언트가 비밀 키를 생성해야 합니다.

##### PSK 클라이언트 인증의 장점

- DH 연산이 필요하지 않습니다.
- 서버가 비밀 키를 생성할 수 있습니다.
- 원하는 경우 서버가 여러 클라이언트와 동일한 키를 공유할 수 있습니다.

##### PSK 클라이언트 인증의 단점

- 이 방식의 보안은 클라이언트 키 자료의 대역 외 교환에 결정적으로 의존합니다. 특정 클라이언트에 대한 교환을 가로채는 공격자는 해당 클라이언트가 권한을 가진 모든 후속 암호화된 LS2를 복호화할 수 있으며, 클라이언트의 접근 권한이 언제 취소되는지도 확인할 수 있습니다.

### Base 32 주소를 사용한 암호화된 LS

암호화된 LS2에는 기존의 base 32 주소를 사용할 수 없습니다. 이는 destination의 해시만 포함하고 있기 때문입니다. 블라인드되지 않은 공개 키를 제공하지 않습니다. 따라서 base 32 주소만으로는 충분하지 않습니다. 클라이언트는 전체 destination(공개 키를 포함)이나 공개 키 자체가 필요합니다. 클라이언트가 주소록에 전체 destination을 가지고 있고, 주소록이 해시로 역방향 검색을 지원한다면, 공개 키를 검색할 수 있습니다.

따라서 해시 대신 공개키를 base32 주소에 넣는 새로운 형식이 필요합니다. 이 형식은 공개키의 서명 타입과 블라인딩 방식의 서명 타입도 포함해야 합니다. 총 요구사항은 32 + 3 = 35바이트이며, base32에서 56문자가 필요하거나 더 긴 공개키 타입의 경우 더 많은 문자가 필요합니다.

```
data = ((1 byte flags || 1 byte unblinded sigtype || 1 byte blinded sigtype) XOR checksum) || 32 byte pubkey
address = Base32Encode(data) || ".b32.i2p"
```
전통적인 base 32 주소와 동일한 ".b32.i2p" 접미사를 사용합니다. 암호화된 leaseSet의 주소는 56개의 인코딩된 문자(디코딩된 35바이트)로 식별되며, 이는 전통적인 base 32 주소의 52개 문자(32바이트)와 비교됩니다. b32 끝의 사용되지 않은 5비트는 반드시 0이어야 합니다.

BitTorrent에는 암호화된 LS2를 사용할 수 없습니다. 이는 32바이트인 compact announce 응답 때문입니다. 32바이트에는 해시만 포함됩니다. leaseSet이 암호화되어 있다는 표시나 서명 타입을 위한 공간이 없습니다.

새로운 형식에 대한 자세한 정보는 [명명 규격](/docs/specs/naming) 또는 [제안서 149](/proposals/149-b32-encrypted-ls2)를 참조하십시오.

### 오프라인 키를 사용한 암호화된 LS

오프라인 키를 사용하는 암호화된 leaseSet의 경우, 블라인드된 개인 키도 오프라인에서 생성되어야 하며, 매일 하나씩 생성해야 합니다.

선택적 오프라인 서명 블록이 암호화된 leaseSet의 평문 부분에 있기 때문에, floodfill을 스크래핑하는 누구든지 이를 사용하여 며칠에 걸쳐 leaseSet을 추적할 수 있습니다 (하지만 해독할 수는 없습니다). 이를 방지하기 위해 키의 소유자는 매일 새로운 임시 키도 생성해야 합니다. 임시 키와 블라인드 키 모두 미리 생성하여 router에 일괄적으로 전달할 수 있습니다.

여러 개의 임시 키와 블라인드 키를 패키징하여 클라이언트나 router에 제공하기 위한 파일 형식이 정의되지 않았습니다. 오프라인 키를 사용한 암호화된 leaseSet을 지원하기 위한 I2CP 프로토콜 확장도 정의되지 않았습니다.

### 참고사항

- 암호화된 leaseSet을 사용하는 서비스는 암호화된 버전을 floodfill에 게시합니다. 하지만 효율성을 위해, 인증된 후(예: 화이트리스트를 통해)에는 래핑된 garlic 메시지에서 클라이언트에게 암호화되지 않은 leaseSet을 보냅니다.
- Floodfill은 남용을 방지하기 위해 최대 크기를 합리적인 값으로 제한할 수 있습니다.
- 복호화 후에는 내부 타임스탬프와 만료 시간이 최상위 레벨의 것과 일치하는지 확인하는 등 여러 검사가 수행되어야 합니다.
- AES 대신 ChaCha20이 선택되었습니다. AES 하드웨어 지원이 가능한 경우 속도는 비슷하지만, 저급형 ARM 장치와 같이 AES 하드웨어 지원이 없는 경우 ChaCha20이 2.5-3배 더 빠릅니다.

## 참고 자료

- **[ED25519-REFS]** Daniel J. Bernstein, Niels Duif, Tanja Lange, Peter Schwabe, Bo-Yin Yang의 "High-speed high-security signatures". [http://cr.yp.to/papers.html#ed25519](http://cr.yp.to/papers.html#ed25519)
- **[KEYBLIND-PROOF]** [https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html](https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html)
- **[KEYBLIND-REFS]** [https://trac.torproject.org/projects/tor/ticket/8106](https://trac.torproject.org/projects/tor/ticket/8106) 및 [https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html](https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html)
- **[PRNG-REFS]** [http://projectbullrun.org/dual-ec/ext-rand.html](http://projectbullrun.org/dual-ec/ext-rand.html) 및 [https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html)
- **[RFC-2104]** [https://tools.ietf.org/html/rfc2104](https://tools.ietf.org/html/rfc2104)
- **[RFC-4880-S5.1]** [https://tools.ietf.org/html/rfc4880#section-5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
- **[RFC-5869]** [https://tools.ietf.org/html/rfc5869](https://tools.ietf.org/html/rfc5869)
- **[RFC-7539-S2.4]** [https://tools.ietf.org/html/rfc7539#section-2.4](https://tools.ietf.org/html/rfc7539#section-2.4)
- **[TOR-REND-SPEC-V3]** [https://spec.torproject.org/rend-spec-v3](https://spec.torproject.org/rend-spec-v3)
- **[ZCASH]** [https://github.com/zcash/zips/tree/master/protocol/protocol.pdf](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)
