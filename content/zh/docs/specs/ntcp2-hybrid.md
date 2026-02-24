---
title: "PQ 混合 NTCP2"
description: "使用 ML-KEM 的 NTCP2 传输协议的后量子混合变体"
slug: "ntcp2-hybrid"
lastupdated: "2026-02"
category: "传输协议"
accurateFor: "0.9.69"
---

### 状态

Beta版 2026年第一季度，正式发布 2026年第二季度

## 概述

这是 NTCP2 传输协议的混合后量子变体，如提案 169 中设计的那样。有关更多背景信息，请参阅该提案。

PQ混合NTCP2只能在与标准NTCP2相同的地址和端口上定义。不允许在不同端口上运行，或者在没有标准NTCP2支持的情况下运行，在标准NTCP2被弃用之前的几年内都不会允许这样做。

本规范仅记录标准 NTCP2 支持 PQ Hybrid 所需的更改。有关基线实现细节，请参阅 NTCP2 规范。

## 设计

我们支持基于CRYSTALS-Kyber和CRYSTALS-Dilithium（版本3.1、3及更早版本）但与其不兼容的NIST FIPS 203和204标准[FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)。

### 密钥交换

PQ KEM 仅提供临时密钥，不直接支持静态密钥握手，如 Noise XK 和 IK。加密类型与 PQ Hybrid Ratchet 中使用的相同，并在通用结构文档 [/docs/specs/common-structures/](/docs/specs/common-structures/) 中定义，如 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) 所述，混合类型仅与 X25519 结合定义。

加密类型包括：

| 类型 | 代码 |
|------|------|
| MLKEM512_X25519 | 5 |
| MLKEM768_X25519 | 6 |
| MLKEM1024_X25519 | 7 |
### 合法组合

新的加密类型在 RouterAddresses 中指示。密钥证书中的加密类型将继续为类型 4。

## 规范

### 握手模式

握手使用 [Noise Protocol](https://noiseprotocol.org/noise.html) 握手模式。

使用以下字母映射：

- e = 一次性临时密钥
- s = 静态密钥
- p = 消息载荷
- e1 = 一次性临时PQ密钥，从Alice发送到Bob
- ekem1 = KEM密文，从Bob发送到Alice

以下对 XK 和 IK 的混合前向保密 (hfs) 修改，按照 [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) 第 5 节的规定：

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
e1 模式定义如下，如 [Noise HFS 规范](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) 第 4 节所述：

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
ekem1 模式定义如下，如 [Noise HFS 规范](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) 第 4 节所述：

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
### Noise 握手密钥派生函数

#### 概述

混合握手在 [Noise HFS 规范](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) 中定义。第一个消息，从 Alice 到 Bob，在消息载荷之前包含 e1，即封装密钥。这被视为一个额外的静态密钥；对其调用 EncryptAndHash()（作为 Alice）或 DecryptAndHash()（作为 Bob）。然后像往常一样处理消息载荷。

第二条消息，从 Bob 发送到 Alice，在消息负载之前包含 ekem1 密文。这被视为额外的静态密钥；对其调用 EncryptAndHash()（作为 Bob）或 DecryptAndHash()（作为 Alice）。然后，计算 kem_shared_key 并调用 MixKey(kem_shared_key)。然后按常规方式处理消息负载。

#### 定义的 ML-KEM 操作

我们定义以下函数，对应于 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) 中定义的密码学构建块。

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

注意，encap_key 和密文都在 Noise 握手消息 1 和 2 的 ChaCha/Poly 块内进行了加密。它们将作为握手过程的一部分被解密。

kem_shared_key 通过 MixHash() 混合到链式密钥中。详细信息请参见下文。

#### Alice KDF 用于消息 1

在 'es' 消息模式之后和载荷之前，添加：

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
#### 消息 1 的 Bob KDF

在 'es' 消息模式之后、载荷之前，添加：

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
#### 消息 2 的 Bob KDF

对于 XK：在 'ee' 消息模式之后、载荷之前，添加：

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
#### Alice KDF用于消息2

在 'ee' 消息模式之后，添加：

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
#### 消息 3 的 KDF（仅限 XK）

未更改

#### 用于 split() 的 KDF

未更改

### 握手详情

#### Noise 标识符

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

变更：当前的 NTCP2 只包含 ChaCha 部分中的选项。使用 ML-KEM 后，ChaCha 部分还将包含加密的 PQ 公钥。

为了让 PQ 和非 PQ NTCP2 能够在同一个路由器地址和端口上支持，我们使用 X 值（X25519 临时公钥）的最高位来标记这是一个 PQ 连接。对于非 PQ 连接，这个位总是未设置的。

对于 Alice，在消息被 Noise 加密后，但在对 X 进行 AES 混淆之前，设置 X[31] |= 0x7f。

对于Bob，在对X进行AES去混淆后，测试X[31] & 0x80。如果该位被设置，则用X[31] &= 0x7f清除它，并通过Noise作为PQ连接进行解密。如果该位未设置，则像往常一样通过Noise作为非PQ连接进行解密。

对于在不同 router 地址和端口上广播的 PQ NTCP2，这不是必需的。

更多信息请参见下文的已发布地址部分。

原始内容：

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
未加密数据（未显示 Poly1305 认证标签）：

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
注意：消息1选项块中的版本字段必须设置为2，即使是PQ连接也是如此。

大小：

| 类型 | 类型代码 | X 长度 | 消息 1 长度 | 消息 1 加密长度 | 消息 1 解密长度 | PQ 密钥长度 | 可选长度 |
|------|-----------|-------|-----------|---------------|---------------|------------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 880+pad | 848 | 816 | 800 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1264+pad | 1232 | 1200 | 1184 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1648+pad | 1616 | 1584 | 1568 | 16 |
注意：类型代码仅供内部使用。Router 将保持类型 4，支持情况将在 router 地址中表示。

#### 2) SessionCreated

原始内容：

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
未加密数据（未显示 Poly1305 认证标签）：

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
大小：

| 类型 | 类型代码 | Y 长度 | 消息 2 长度 | 消息 2 加密长度 | 消息 2 解密长度 | PQ CT 长度 | 可选长度 |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 848+pad | 816 | 784 | 768 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1136+pad | 1104 | 1104 | 1088 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1616+pad | 1584 | 1584 | 1568 | 16 |
注意：类型代码仅供内部使用。router 将保持类型 4，支持情况将在 router 地址中指示。

#### 3) SessionConfirmed

未更改

#### 密钥派生函数 (KDF)（用于数据阶段）

未更改

#### 发布地址

在所有情况下，请照常使用 NTCP2 传输名称。

使用与非PQ、非防火墙相同的地址/端口。仅支持一种PQ变体。在router地址中，发布v=2（如常）和新参数pq=[3|4|5]以指示MLKEM 512/768/1024。Alice在会话请求中设置临时密钥的MSB（key[31] & 0x80）以指示这是混合连接。见上文。较旧的router将忽略pq参数并照常进行非pq连接。

不同地址/端口作为非PQ，或仅PQ、非防火墙配置不受支持。这将不会实现，直到非PQ NTCP2被禁用，这要等到几年后。当非PQ被禁用时，可能支持多个PQ变体，但每个地址只能有一个。当它被支持时，在router地址中，发布v=[3|4|5]来表示MLKEM 512/768/1024。Alice不设置临时密钥的MSB。旧版router将检查v参数并跳过此地址，因为它不受支持。

防火墙地址（不发布IP）：在router地址中，发布v=2（照常）。无需发布pq参数。

Alice可以使用Bob发布的PQ变体连接到PQ Bob，无论Alice是否在她的router信息中宣传pq支持，或者她是否宣传相同的变体。

#### 最大填充

在当前规范中，消息 1 和消息 2 被定义为具有"合理"数量的填充，建议范围为 0-31 字节，且未指定最大值。

Java I2P 为非 PQ 连接实现了最多 256 字节的填充，但这在之前的文档中没有记录。

使用定义的消息大小作为最大填充，即最大填充将使消息大小翻倍，如下所示：

| 消息最大填充 | MLKEM-512 | MLKEM-768 | MLKEM-1024 |
|---------------------|-----------|-----------|------------|
| Session Request  |       880   |     1264   |    1648  |
| Session Created  |       848   |     1136   |    1616	 |
## 开销分析

### 密钥交换

大小增加（字节）：

| 类型 | 公钥 (消息 1) | 密文 (消息 2) |
|------|----------------|-------------------|
| MLKEM512_X25519 | +816 | +784 |
| MLKEM768_X25519 | +1200 | +1104 |
| MLKEM1024_X25519 | +1584 | +1584 |
## 安全性分析

NIST 安全类别在 [NIST 演示文稿](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) 第 10 页中有总结。初步标准：对于混合协议，我们的最低 NIST 安全类别应为 2，对于纯 PQ 协议应为 3。

| 类别 | 安全等级相当于 |
|----------|--------------|
| 1 | AES128 |
| 2 | SHA256 |
| 3 | AES192 |
| 4 | SHA384 |
| 5 | AES256 |
### 握手

这些都是混合协议。实现应该优先选择 MLKEM768；MLKEM512 不够安全。

NIST 安全类别 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)：

| 算法 | 安全类别 |
|-----------|-------------------|
| MLKEM512 | 1 |
| MLKEM768 | 3 |
| MLKEM1024 | 5 |
## 实现说明

### 库支持

Bouncycastle、BoringSSL 和 WolfSSL 库现在支持 MLKEM 和 MLDSA。OpenSSL 的支持将在其 2025 年 4 月 8 日发布的 3.5 版本中提供 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/)。

### 入站流量识别

我们在会话请求中设置临时密钥的最高有效位（key[31] & 0x80）来表明这是一个混合连接。这使我们能够在同一端口上运行标准 NTCP 和混合 NTCP。入站连接只支持一种混合变体，并在 router 地址中进行广播。例如，pq=3 或 pq=4。

#### 混淆

作为 Alice，对于 PQ 连接，在混淆之前，设置 X[31] |= 0x80。这使得 X 成为一个无效的 X25519 公钥。混淆之后，AES-CBC 会将其随机化。混淆后 X 的最高有效位将是随机的。

作为 Bob，在去混淆后测试 (X[31] & 0x80) != 0。如果是，则这是一个 PQ 连接。

NTCP2-PQ 所需的最低 router 版本待定。

注意：类型代码仅供内部使用。Router 将保持类型 4，支持情况将在 router 地址中指示。

## Router兼容性

### 传输名称

在所有情况下，像往常一样使用 NTCP2 传输名称。较旧的 router 将忽略 pq 参数，并像往常一样使用标准 NTCP2 进行连接。

## 参考资料

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
