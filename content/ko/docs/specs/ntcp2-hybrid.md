---
title: "PQ Hybrid NTCP2"
description: "ML-KEM을 사용하는 NTCP2 전송 프로토콜의 포스트 양자 하이브리드 변형"
slug: "ntcp2-hybrid"
lastupdated: "2026-02"
category: "전송 계층"
accurateFor: "0.9.69"
---

### 상태

베타 2026년 1분기, 릴리스 2026년 2분기

## 개요

이는 Proposal 169에서 설계된 NTCP2 전송 프로토콜의 하이브리드 양자 후 변형입니다. 추가 배경 정보는 해당 제안서를 참조하세요.

PQ 하이브리드 NTCP2는 표준 NTCP2와 동일한 주소와 포트에서만 정의됩니다. 다른 포트에서의 작동이나 표준 NTCP2 지원 없이는 허용되지 않으며, 표준 NTCP2가 폐지되는 몇 년 후까지는 허용되지 않을 것입니다.

이 명세서는 PQ Hybrid를 지원하기 위해 표준 NTCP2에 필요한 변경사항만을 문서화합니다. 기본 구현 세부사항은 NTCP2 명세서를 참조하십시오.

## 설계

우리는 NIST FIPS 203 및 204 표준 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)을 지원합니다. 이 표준들은 CRYSTALS-Kyber와 CRYSTALS-Dilithium (버전 3.1, 3 및 이전 버전)을 기반으로 하지만 호환되지 않습니다.

### 키 교환

PQ KEM은 임시 키만 제공하며, Noise XK 및 IK와 같은 정적 키 핸드셰이크를 직접 지원하지 않습니다. 암호화 유형은 PQ Hybrid Ratchet에서 사용되는 것과 동일하며, [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)에서와 같이 공통 구조 문서 [/docs/specs/common-structures/](/docs/specs/common-structures/)에 정의되어 있습니다. 하이브리드 유형은 X25519와의 조합으로만 정의됩니다.

암호화 유형은 다음과 같습니다:

| 유형 | 코드 |
|------|------|
| MLKEM512_X25519 | 5 |
| MLKEM768_X25519 | 6 |
| MLKEM1024_X25519 | 7 |
### 유효한 조합

새로운 암호화 유형은 RouterAddresses에 표시됩니다. 키 인증서의 암호화 유형은 계속해서 type 4가 됩니다.

## 명세서

### 핸드셰이크 패턴

핸드셰이크는 [Noise Protocol](https://noiseprotocol.org/noise.html) 핸드셰이크 패턴을 사용합니다.

다음 문자 매핑이 사용됩니다:

- e = 일회용 임시 키
- s = 정적 키
- p = 메시지 페이로드
- e1 = Alice에서 Bob으로 전송되는 일회용 임시 PQ 키
- ekem1 = Bob에서 Alice로 전송되는 KEM 암호문

하이브리드 전방향 보안(hfs)을 위한 XK 및 IK에 대한 다음 수정사항들은 [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) 섹션 5에 명시된 바와 같습니다:

```
XK:                       XKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, p               -> e, es, e1, p
  <- e, ee, p               <- e, ee, ekem1, p
  -> s, se                  -> s, se
  <- p                      <- p
  p ->                      p ->


  e1 and ekem1 are encrypted. See pattern definitions below.
  NOTE: e1 and ekem1 are different sizes (unlike X25519)
```
e1 패턴은 [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) 섹션 4에 명시된 바와 같이 다음과 같이 정의됩니다:

```
For Alice:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++
  MixHash(ciphertext)

  For Bob:

  // DecryptAndHash(ciphertext)
  encap_key = DECRYPT(k, n, ciphertext, ad)
  n++
  MixHash(ciphertext)
```
ekem1 패턴은 [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) 섹션 4에 명시된 바와 같이 다음과 같이 정의됩니다:

```
For Bob:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  MixKey(kem_shared_key)


  For Alice:

  // DecryptAndHash(ciphertext)
  kem_ciphertext = DECRYPT(k, n, ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  MixKey(kem_shared_key)
```
### Noise Handshake KDF

#### 개요

하이브리드 핸드셰이크는 [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf)에 정의되어 있습니다. Alice에서 Bob으로의 첫 번째 메시지는 메시지 페이로드 앞에 캡슐화 키인 e1을 포함합니다. 이는 추가 정적 키로 처리됩니다. (Alice로서) EncryptAndHash()를 호출하거나 (Bob으로서) DecryptAndHash()를 호출하세요. 그런 다음 메시지 페이로드를 평소와 같이 처리합니다.

Bob에서 Alice로의 두 번째 메시지는 메시지 페이로드 앞에 ekem1, 암호문을 포함합니다. 이것은 추가 정적 키로 처리됩니다; (Bob으로서) EncryptAndHash()를 호출하거나 (Alice로서) DecryptAndHash()를 호출합니다. 그런 다음 kem_shared_key를 계산하고 MixKey(kem_shared_key)를 호출합니다. 그 후 평소와 같이 메시지 페이로드를 처리합니다.

#### 정의된 ML-KEM 작업

[FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)에서 정의된 암호화 구성 요소에 해당하는 다음 함수들을 정의합니다.

(encap_key, decap_key) = PQ_KEYGEN()

    Alice creates the encapsulation and decapsulation keys
    The encapsulation key is sent in message 1.
    encap_key and decap_key sizes vary based on ML-KEM variant.

(ciphertext, kem_shared_key) = ENCAPS(encap_key)

    Bob calculates the ciphertext and shared key,
    using the ciphertext received in message 1.
    The ciphertext is sent in message 2.
    ciphertext size varies based on ML-KEM variant.
    The kem_shared_key is always 32 bytes.

kem_shared_key = DECAPS(ciphertext, decap_key)

    Alice calculates the shared key,
    using the ciphertext received in message 2.
    The kem_shared_key is always 32 bytes.

encap_key와 ciphertext 모두 Noise 핸드셰이크 메시지 1과 2의 ChaCha/Poly 블록 내부에서 암호화된다는 점에 유의하세요. 이들은 핸드셰이크 과정의 일부로 복호화됩니다.

kem_shared_key는 MixHash()를 사용하여 chaining key에 혼합됩니다. 자세한 내용은 아래를 참조하세요.

#### 메시지 1을 위한 Alice KDF

'es' 메시지 패턴 다음과 페이로드 이전에 다음을 추가하세요:

```
This is the "e1" message pattern:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)


  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### 메시지 1에 대한 Bob KDF

'es' 메시지 패턴 이후와 페이로드 이전에 다음을 추가하세요:

```
This is the "e1" message pattern:

  // DecryptAndHash(encap_key_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  encap_key = DECRYPT(k, n, encap_key_section, ad)
  n++

  // MixHash(encap_key_section)
  h = SHA256(h || encap_key_section)

  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### Message 2를 위한 Bob KDF

XK의 경우: 'ee' 메시지 패턴 이후와 페이로드 이전에 다음을 추가합니다:

```
This is the "ekem1" message pattern:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  // MixKey(kem_shared_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### Message 2를 위한 Alice KDF

'ee' 메시지 패턴 다음에 추가하세요:

```
This is the "ekem1" message pattern:

  // DecryptAndHash(kem_ciphertext_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  kem_ciphertext = DECRYPT(k, n, kem_ciphertext_section, ad)

  // MixHash(kem_ciphertext_section)
  h = SHA256(h || kem_ciphertext_section)

  // MixKey(kem_shared_key)
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### 메시지 3에 대한 KDF (XK만 해당)

변경되지 않음

#### split()용 KDF

변경되지 않음

### 핸드셰이크 세부사항

#### Noise 식별자

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

변경사항: 현재 NTCP2는 ChaCha 섹션의 옵션만을 포함합니다. ML-KEM을 사용하면 ChaCha 섹션에는 암호화된 PQ 공개 키도 포함됩니다.

PQ와 비PQ NTCP2가 동일한 router 주소와 포트에서 지원될 수 있도록, X 값(X25519 임시 공개 키)의 최상위 비트를 사용하여 PQ 연결임을 표시합니다. 이 비트는 비PQ 연결에서는 항상 설정되지 않습니다.

Alice의 경우, 메시지가 Noise에 의해 암호화된 후 X의 AES 난독화 이전에 X[31] |= 0x7f를 설정합니다.

Bob의 경우, X의 AES 난독화 해제 후 X[31] & 0x80을 테스트합니다. 비트가 설정되어 있으면 X[31] &= 0x7f로 클리어하고 PQ 연결로 Noise를 통해 복호화합니다. 비트가 클리어되어 있으면 평소와 같이 non-PQ 연결로 Noise를 통해 복호화합니다.

다른 router 주소와 포트에서 광고되는 PQ NTCP2의 경우, 이는 필수가 아닙니다.

추가 정보는 아래의 게시된 주소 섹션을 참조하세요.

원본 내용:

```
  +----+----+----+----+----+----+----+----+
  |        MS bit set to 1 and then       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted X         |
  +             (32 bytes)                +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +      (see table below for length)     +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  ~   n = 0                               ~
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaChaPoly frame (options)          |
  +         32 bytes                      +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  ~         padding (optional)            ~
  |     length defined in options block   |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
암호화되지 않은 데이터 (Poly1305 인증 태그는 표시되지 않음):

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                   X                   |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM encap_key            |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
참고: 메시지 1 옵션 블록의 버전 필드는 PQ 연결에서도 2로 설정되어야 합니다.

크기:

| 타입 | 타입 코드 | X 길이 | 메시지 1 길이 | 메시지 1 암호화 길이 | 메시지 1 복호화 길이 | PQ 키 길이 | 옵션 길이 |
|------|-----------|-------|-----------|---------------|---------------|------------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 880+pad | 848 | 816 | 800 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1264+pad | 1232 | 1200 | 1184 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1648+pad | 1616 | 1584 | 1568 | 16 |
참고: 타입 코드는 내부 사용 전용입니다. Router는 타입 4로 유지되며, 지원 여부는 router 주소에서 표시됩니다.

#### 2) SessionCreated

원시 내용:

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted Y         |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +   Encrypted and authenticated data    +
  -      (see table below for length)     -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (options)          |
  +   Encrypted and authenticated data    +
  -           32 bytes                    -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
암호화되지 않은 데이터 (Poly1305 인증 태그는 표시되지 않음):

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                  Y                    |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
크기:

| Type | Type Code | Y len | Msg 2 len | Msg 2 Enc len | Msg 2 Dec len | PQ CT len | opt len |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 848+pad | 816 | 784 | 768 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1136+pad | 1104 | 1104 | 1088 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1616+pad | 1584 | 1584 | 1568 | 16 |
참고: 타입 코드는 내부 용도로만 사용됩니다. Router는 타입 4로 유지되며, 지원 여부는 router 주소에 표시됩니다.

#### 3) SessionConfirmed

변경되지 않음

#### 키 유도 함수 (KDF) (데이터 단계용)

변경되지 않음

#### 게시된 주소

모든 경우에 평상시와 같이 NTCP2 transport 이름을 사용하세요.

비PQ, 비방화벽과 동일한 주소/포트를 사용합니다. 하나의 PQ 변형만 지원됩니다. router 주소에서 v=2 (평소와 같이)와 새로운 매개변수 pq=[3|4|5]를 게시하여 MLKEM 512/768/1024를 표시합니다. Alice는 세션 요청에서 임시 키의 MSB (key[31] & 0x80)를 설정하여 이것이 하이브리드 연결임을 나타냅니다. 위를 참조하세요. 이전 router들은 pq 매개변수를 무시하고 평소와 같이 비PQ로 연결합니다.

PQ가 아닌 것과 다른 주소/포트, 또는 PQ 전용, 방화벽이 없는 환경은 지원되지 않습니다. 이는 PQ가 아닌 NTCP2가 비활성화되기 전까지는 구현되지 않을 예정이며, 이는 지금으로부터 몇 년 후입니다. PQ가 아닌 것이 비활성화되면 여러 PQ 변형이 지원될 수 있지만, 주소당 하나씩만 가능합니다. 지원되면 router 주소에서 MLKEM 512/768/1024를 나타내기 위해 v=[3|4|5]를 게시합니다. Alice는 임시 키의 MSB를 설정하지 않습니다. 이전 버전의 router들은 v 매개변수를 확인하고 이 주소를 지원되지 않는 것으로 건너뜁니다.

방화벽 주소 (IP가 공개되지 않음): router 주소에서 v=2를 게시합니다 (평소와 같이). pq 매개변수를 게시할 필요는 없습니다.

Alice는 자신의 router 정보에서 pq 지원을 광고하는지 여부나 같은 변형을 광고하는지 여부와 관계없이, Bob이 게시하는 PQ 변형을 사용하여 PQ Bob에 연결할 수 있습니다.

#### 최대 패딩

현재 명세에서 메시지 1과 2는 "합리적인" 양의 패딩을 갖도록 정의되어 있으며, 0-31바이트 범위가 권장되고 최대값은 지정되지 않았습니다.

Java I2P는 non-PQ 연결에 대해 최대 256바이트 패딩을 구현하지만, 이는 이전에 문서화되지 않았습니다.

정의된 메시지 크기를 최대 패딩으로 사용합니다. 즉, 최대 패딩은 다음과 같이 메시지 크기를 두 배로 늘립니다:

| Message Max Padding | MLKEM-512 | MLKEM-768 | MLKEM-1024 |
|---------------------|-----------|-----------|------------|
| Session Request  |       880   |     1264   |    1648  |
| Session Created  |       848   |     1136   |    1616	 |
## 오버헤드 분석

### 키 교환

크기 증가 (바이트):

| Type | Pubkey (Msg 1) | Cipertext (Msg 2) |
|------|----------------|-------------------|
| MLKEM512_X25519 | +816 | +784 |
| MLKEM768_X25519 | +1200 | +1104 |
| MLKEM1024_X25519 | +1584 | +1584 |
## 보안 분석

NIST 보안 카테고리는 [NIST 발표자료](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) 10번째 슬라이드에 요약되어 있습니다. 예비 기준: 하이브리드 프로토콜의 경우 최소 NIST 보안 카테고리 2, PQ 전용의 경우 3이어야 합니다.

| 카테고리 | 보안 수준 |
|----------|--------------|
| 1 | AES128 |
| 2 | SHA256 |
| 3 | AES192 |
| 4 | SHA384 |
| 5 | AES256 |
### 핸드셰이크

이들은 모두 하이브리드 프로토콜입니다. 구현체들은 MLKEM768을 선호해야 합니다. MLKEM512는 충분히 안전하지 않습니다.

NIST 보안 범주 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf):

| 알고리즘 | 보안 카테고리 |
|-----------|-------------------|
| MLKEM512 | 1 |
| MLKEM768 | 3 |
| MLKEM1024 | 5 |
## 구현 노트

### 라이브러리 지원

Bouncycastle, BoringSSL, WolfSSL 라이브러리들이 이제 MLKEM과 MLDSA를 지원합니다. OpenSSL 지원은 2025년 4월 8일 3.5 릴리스에 포함될 예정입니다 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

### 인바운드 트래픽 식별

세션 요청에서 임시 키의 MSB(key[31] & 0x80)를 설정하여 이것이 하이브리드 연결임을 나타냅니다. 이를 통해 동일한 포트에서 표준 NTCP와 하이브리드 NTCP를 모두 실행할 수 있습니다. 인바운드의 경우 하나의 하이브리드 변형만 지원되며, router 주소에 광고됩니다. 예를 들어, pq=3 또는 pq=4입니다.

#### 난독화

Alice로서, PQ 연결의 경우, 난독화 이전에 X[31] |= 0x80을 설정합니다. 이렇게 하면 X가 유효하지 않은 X25519 공개 키가 됩니다. 난독화 후에는 AES-CBC가 이를 무작위화합니다. 난독화 후 X의 MSB는 무작위가 됩니다.

Bob으로서, 난독화 해제 후 (X[31] & 0x80) != 0인지 테스트합니다. 만약 그렇다면, 이는 PQ 연결입니다.

NTCP2-PQ에 필요한 최소 router 버전은 미정입니다.

참고: 타입 코드는 내부 사용 전용입니다. Router는 타입 4로 유지되며, 지원은 router 주소에서 표시됩니다.

## Router 호환성

### 전송 이름

모든 경우에 평소와 같이 NTCP2 transport 이름을 사용하세요. 구버전 router들은 pq 매개변수를 무시하고 평소와 같이 표준 NTCP2로 연결합니다.

## 참고 자료

* [CABFORUM](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/)
* [Choosing-Hash](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3)
* [CLOUDFLARE](https://blog.cloudflare.com/pq-2024/)
* [COMMON](/docs/specs/common-structures/)
* [COMPOSITE-SIGS](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)
* [ECIES](/docs/specs/ecies/)
* [FORUM](http://zzz.i2p/topics/3294)
* [FIPS202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
* [FIPS203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
* [FIPS204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
* [FIPS205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf)
* [MLDSA-OIDS](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/)
* [NIST-PQ](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)
* [NIST-PQ-UPDATE](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf)
* [NIST-PQ-END](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf)
* [NIST-VECTORS](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values)
* [Noise](https://noiseprotocol.org/noise.html)
* [Noise-Hybrid](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf)
* [NSA-PQ](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF)
* [NTCP2](/docs/specs/ntcp2/)
* [OPENSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/)
* [Prop165](/docs/proposals/165/)
* [PQ-WIREGUARD](https://eprint.iacr.org/2020/379.pdf)
* [RFC-2104](https://tools.ietf.org/html/rfc2104)
* [Rosenpass](https://rosenpass.eu/)
* [Rosenpass-Whitepaper](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf)
* [SSH-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/)
* [SSU2](/docs/specs/ssu2/)
* [TLS-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/)
