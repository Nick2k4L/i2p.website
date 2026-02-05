---
title: "ECIES-X25519 라우터 메시지"
description: "X25519를 사용하는 ECIES router에 대한 Garlic 메시지 암호화 명세"
slug: "ecies-routers"
category: "프로토콜"
lastUpdated: "2025-03"
accurateFor: "0.9.65"
---

## 참고

릴리스 0.9.49부터 지원됩니다. 네트워크 배포 및 테스트가 진행 중입니다. 사소한 수정이 있을 수 있습니다. [제안서 156](/proposals/156-ecies-routers)을 참조하세요.

## 개요

이 문서는 [ECIES-X25519](/docs/specs/ecies)에서 도입된 암호화 기본 요소를 사용하여 ECIES router에 대한 Garlic message encryption을 명시합니다. 이는 router를 ElGamal에서 ECIES-X25519 키로 변환하기 위한 전체 [proposal 156](/proposals/156-ecies-routers)의 일부입니다. 이 명세는 0.9.49 릴리스부터 구현되었습니다.

ECIES router에 필요한 모든 변경 사항의 개요는 [proposal 156](/proposals/156-ecies-routers)을 참조하세요. ECIES-X25519 대상으로의 Garlic Messages에 대해서는 [ECIES-X25519](/docs/specs/ecies)를 참조하세요.

### 암호화 기본 요소

이 명세를 구현하는 데 필요한 기본 요소들은 다음과 같습니다:

- [암호화](/docs/specs/cryptography)에서와 같은 AES-256-CBC
- STREAM ChaCha20/Poly1305 함수: ENCRYPT(k, n, plaintext, ad) 및 DECRYPT(k, n, ciphertext, ad) - [NTCP2](/docs/specs/ntcp2), [ECIES-X25519](/docs/specs/ecies), 및 [RFC-7539](https://tools.ietf.org/html/rfc7539)에서와 같음
- X25519 DH 함수 - [NTCP2](/docs/specs/ntcp2) 및 [ECIES-X25519](/docs/specs/ecies)에서와 같음
- HKDF(salt, ikm, info, n) - [NTCP2](/docs/specs/ntcp2) 및 [ECIES-X25519](/docs/specs/ecies)에서와 같음

다른 곳에서 정의된 기타 Noise 함수들:

- MixHash(d) - [NTCP2](/docs/specs/ntcp2) 및 [ECIES-X25519](/docs/specs/ecies)에서와 같이
- MixKey(d) - [NTCP2](/docs/specs/ntcp2) 및 [ECIES-X25519](/docs/specs/ecies)에서와 같이

## 설계

ECIES Router SKM은 Destination용으로 [ECIES](/docs/specs/ecies)에서 명시된 완전한 Ratchet SKM이 필요하지 않습니다. IK 패턴을 사용하는 비익명 메시지에 대한 요구사항이 없습니다. 위협 모델은 Elligator2로 인코딩된 ephemeral 키를 요구하지 않습니다.

따라서 router SKM은 터널 구축을 위해 [Prop152](/proposals/152-ecies-tunnels)에서 지정된 것과 동일한 Noise "N" 패턴을 사용할 것입니다. Destination용으로 [ECIES](/docs/specs/ecies)에서 지정된 것과 동일한 페이로드 형식을 사용할 것입니다. [ECIES](/docs/specs/ecies)에서 지정된 IK의 zero static key (바인딩 또는 세션 없음) 모드는 사용되지 않을 것입니다.

조회에 대한 응답은 조회에서 요청된 경우 ratchet tag로 암호화됩니다. 이는 [Prop154](/proposals/154-ecies-lookups)에 문서화되어 있으며, 현재 [I2NP](/docs/specs/i2np)에 명시되어 있습니다.

이 설계를 통해 router는 단일 ECIES Session Key Manager를 가질 수 있습니다. Destination에 대해 [ECIES](/docs/specs/ecies)에서 설명된 "이중 키" Session Key Manager를 실행할 필요가 없습니다. Router는 하나의 공개 키만 가집니다.

ECIES router는 ElGamal 정적 키를 가지고 있지 않습니다. 그러나 router는 ElGamal router를 통해 tunnel을 구축하고 ElGamal router에 암호화된 메시지를 보내기 위해 여전히 ElGamal 구현이 필요합니다.

ECIES router는 0.9.46 이전 버전의 floodfill router로부터 NetDB 조회에 대한 응답으로 수신되는 ElGamal 태그 메시지를 받기 위해 부분적인 ElGamal Session Key Manager가 필요할 수 있습니다. 이는 해당 router들이 [Prop152](/proposals/152-ecies-tunnels)에 명시된 ECIES 태그 응답의 구현을 갖고 있지 않기 때문입니다. 그렇지 않으면, ECIES router는 0.9.46 이전 버전의 floodfill router로부터 암호화된 응답을 요청하지 못할 수 있습니다.

이는 선택사항입니다. 결정은 다양한 I2P 구현에 따라 달라질 수 있으며 0.9.46 이상으로 업그레이드된 네트워크의 비율에 따라 달라질 수 있습니다. 현재 기준으로 네트워크의 약 85%가 0.9.46 이상입니다.

### Noise Protocol Framework

이 명세는 [Noise Protocol Framework](https://noiseprotocol.org/noise.html) (개정판 34, 2018-07-11)를 기반으로 한 요구사항을 제공합니다. Noise 용어에서 Alice는 개시자이고, Bob은 응답자입니다.

이는 Noise 프로토콜 Noise_N_25519_ChaChaPoly_SHA256을 기반으로 합니다. 이 Noise 프로토콜은 다음과 같은 기본 요소들을 사용합니다:

- **단방향 핸드셰이크 패턴: N** - Alice는 자신의 정적 키를 Bob에게 전송하지 않음 (N)
- **DH 함수: X25519** - [RFC-7748](https://tools.ietf.org/html/rfc7748)에서 명시된 32바이트 키 길이를 가진 X25519 DH.
- **암호화 함수: ChaChaPoly** - [RFC-7539](https://tools.ietf.org/html/rfc7539) 섹션 2.8에서 명시된 AEAD_CHACHA20_POLY1305. 12바이트 nonce이며, 처음 4바이트는 0으로 설정. [NTCP2](/docs/specs/ntcp2)와 동일함.
- **해시 함수: SHA256** - 표준 32바이트 해시, I2P에서 이미 광범위하게 사용됨.

### 핸드셰이크 패턴

핸드셰이크는 [Noise](https://noiseprotocol.org/noise.html) 핸드셰이크 패턴을 사용합니다.

다음 문자 매핑이 사용됩니다:

- e = 일회성 임시 키
- s = 정적 키
- p = 메시지 페이로드

빌드 요청은 Noise N 패턴과 동일합니다. 이것은 또한 [NTCP2](/docs/specs/ntcp2)에서 사용되는 XK 패턴의 첫 번째(세션 요청) 메시지와도 동일합니다.

```
<- s
  ...
  e es p ->
```
### 메시지 암호화

메시지는 대상 router에 대해 생성되고 비대칭적으로 암호화됩니다. 메시지의 이러한 비대칭 암호화는 현재 [Cryptography](/docs/specs/cryptography)에서 정의된 ElGamal을 사용하며 SHA-256 체크섬을 포함합니다. 이 설계는 전방향 보안(forward-secret)을 제공하지 않습니다.

ECIES 설계는 ECIES-X25519 ephemeral-static DH를 사용하는 단방향 Noise 패턴 "N"을 사용하며, HKDF와 ChaCha20/Poly1305 AEAD를 통해 전진 보안성, 무결성, 인증을 제공합니다. Alice는 익명 메시지 발신자로서 router 또는 목적지입니다. 대상 ECIES router는 Bob입니다.

### 응답 암호화

Alice는 익명이므로 응답은 이 프로토콜의 일부가 아닙니다. 응답 키가 있다면 요청 메시지에 포함됩니다. Database Lookup 메시지에 대한 자세한 내용은 [I2NP 사양서](/docs/specs/i2np)를 참조하세요.

Database Lookup 메시지에 대한 응답은 Database Store 또는 Database Search Reply 메시지입니다. 이들은 [I2NP](/docs/specs/i2np) 및 [Prop154](/proposals/154-ecies-lookups)에서 명시된 32바이트 응답 키와 8바이트 응답 태그를 사용하여 Existing Session 메시지로 암호화됩니다.

Database Store 메시지에 대한 명시적인 응답은 없습니다. 송신자는 Delivery Status 메시지를 포함하는 Garlic Message를 자기 자신에게 번들로 묶어서 자체적인 응답을 만들 수 있습니다.

## 명세서

X25519: [ECIES](/docs/specs/ecies)를 참조하세요.

Router Identity와 Key Certificate: [Common Structures](/docs/specs/common-structures)를 참조하십시오.

### 요청 암호화

요청 암호화는 Noise "N" 패턴을 사용하여 [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) 및 [Prop152](/proposals/152-ecies-tunnels)에서 지정된 것과 동일합니다.

lookup에서 요청된 경우 lookup에 대한 응답은 ratchet tag로 암호화됩니다. Database Lookup 요청 메시지는 [I2NP](/docs/specs/i2np)와 [Prop154](/proposals/154-ecies-lookups)에 명시된 대로 32바이트 응답 키와 8바이트 응답 태그를 포함합니다. 이 키와 태그는 응답을 암호화하는 데 사용됩니다.

태그 세트는 생성되지 않습니다. ECIES-X25519-AEAD-Ratchet [Prop144](/proposals/144-ecies-x25519-aead-ratchet)와 [ECIES](/docs/specs/ecies)에서 명시된 제로 정적 키 방식은 사용되지 않습니다. 임시 키는 Elligator2로 인코딩되지 않습니다.

일반적으로 이들은 New Session 메시지이며, 메시지 발신자가 익명이므로 제로 정적 키(바인딩 또는 세션 없음)와 함께 전송됩니다.

#### 초기 ck와 h를 위한 KDF

이는 "N" 패턴을 위한 표준 [Noise](https://noiseprotocol.org/noise.html)이며 표준 프로토콜 명을 사용합니다. 이는 tunnel 빌드 메시지를 위한 [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies)와 [Prop152](/proposals/152-ecies-tunnels)에서 명시된 것과 동일합니다.

```
This is the "e" message pattern:

  // Define protocol_name.
  Set protocol_name = "Noise_N_25519_ChaChaPoly_SHA256"
  (31 bytes, US-ASCII encoded, no NULL termination).

  // Define Hash h = 32 bytes
  // Pad to 32 bytes. Do NOT hash it, because it is not more than 32 bytes.
  h = protocol_name || 0

  Define ck = 32 byte chaining key. Copy the h data to ck.
  Set chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // up until here, can all be precalculated by all routers.
```
#### 메시지용 KDF

메시지 생성자는 각 메시지마다 임시 X25519 키페어를 생성합니다. 임시 키는 메시지별로 고유해야 합니다. 이는 터널 빌드 메시지에 대한 [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) 및 [Prop152](/proposals/152-ecies-tunnels)에서 명시된 것과 동일합니다.

```
  // Target router's X25519 static keypair (hesk, hepk) from the Router Identity
  hesk = GENERATE_PRIVATE()
  hepk = DERIVE_PUBLIC(hesk)

  // MixHash(hepk)
  // || below means append
  h = SHA256(h || hepk);

  // up until here, can all be precalculated by each router
  // for all incoming messages

  // Sender generates an X25519 ephemeral keypair
  sesk = GENERATE_PRIVATE()
  sepk = DERIVE_PUBLIC(sesk)

  // MixHash(sepk)
  h = SHA256(h || sepk);

  End of "e" message pattern.

  This is the "es" message pattern:

  // Noise es
  // Sender performs an X25519 DH with receiver's static public key.
  // The target router
  // extracts the sender's ephemeral key preceding the encrypted record.
  sharedSecret = DH(sesk, hepk) = DH(hesk, sepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // ChaChaPoly parameters to encrypt/decrypt
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  // Chain key is not used
  //chainKey = keydata[0:31]

  // AEAD parameters
  k = keydata[32:63]
  n = 0
  plaintext = 464 byte build request record
  ad = h
  ciphertext = ENCRYPT(k, n, plaintext, ad)

  End of "es" message pattern.

  // MixHash(ciphertext) is not required
  //h = SHA256(h || ciphertext)
```
#### 페이로드

페이로드는 [ECIES](/docs/specs/ecies)와 [Prop144](/proposals/144-ecies-x25519-aead-ratchet)에서 정의된 것과 동일한 블록 형식입니다. 모든 메시지는 재전송 공격 방지를 위해 DateTime 블록을 포함해야 합니다.

## 구현 참고사항

- 구형 router들은 router의 암호화 타입을 확인하지 않고 ElGamal로 암호화된 메시지를 전송합니다. 일부 최근 router들에는 버그가 있어 다양한 형태의 잘못된 메시지를 전송할 수 있습니다. 구현자들은 가능하다면 DH 연산 전에 이러한 레코드들을 탐지하고 거부하여 CPU 사용량을 줄여야 합니다.

## 참고 문헌

- [공통 구조](/docs/specs/common-structures)
- [암호화](/docs/specs/cryptography)
- [ECIES](/docs/specs/ecies)
- [I2NP](/docs/specs/i2np)
- [Noise Protocol Framework](https://noiseprotocol.org/noise.html)
- [NTCP2](/docs/specs/ntcp2)
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet)
- [Prop152](/proposals/152-ecies-tunnels)
- [Prop154](/proposals/154-ecies-lookups)
- [Prop156](/proposals/156-ecies-routers)
- [RFC-7539](https://tools.ietf.org/html/rfc7539)
- [RFC-7748](https://tools.ietf.org/html/rfc7748)
- [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies)
