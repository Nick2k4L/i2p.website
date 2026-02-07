---
title: "加密 LeaseSet 规范"
description: "加密 leaseSet 的盲化、加密和解密"
slug: "encryptedleaseset"
category: "协议"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## 概述

本文档规定了加密 leaseset 的致盲、加密和解密。关于加密 leaseset 的结构，请参见[通用结构规范](/docs/specs/common-structures)。关于加密 leaseset 的背景信息，请参见[提案 123](/proposals/123-new-netdb-entries)。关于在 netdb 中的使用，请参见 netdb 文档。

### 定义

我们定义以下与加密 LS2 所使用的加密构建块相对应的函数：

**CSRNG(n)** : 密码学安全随机数生成器输出的 n 字节数据。

除了要求CSRNG在密码学上安全（因此适合生成密钥材料）之外，当紧接在某些n字节输出之前和之后的字节序列在网络上暴露时（例如在盐值或加密填充中），该输出必须能够安全地用作密钥材料。依赖于潜在不可信源的实现应该对任何将在网络上暴露的输出进行哈希处理 [PRNG-REFS](http://projectbullrun.org/dual-ec/ext-rand.html)。

**H(p, d)** : SHA-256 哈希函数，接受个性化字符串 p 和数据 d，产生长度为 32 字节的输出。

使用 SHA-256 如下：

```
H(p, d) := SHA-256(p || d)
```
**STREAM** : 按照 [RFC-7539-S2.4](https://tools.ietf.org/html/rfc7539#section-2.4) 规范的 ChaCha20 流密码，初始计数器设置为 1。S_KEY_LEN = 32 和 S_IV_LEN = 12。

- **ENCRYPT(k, iv, plaintext)** : 使用密码密钥 k 和随机数 iv 加密明文，其中 iv 对于密钥 k 必须是唯一的。返回与明文大小相同的密文。如果密钥是保密的，整个密文必须与随机数据无法区分。

- **DECRYPT(k, iv, ciphertext)** : 使用密钥 k 和随机数 iv 解密密文。返回明文。

**SIG**：Red25519 签名方案（对应 SigType 11）具有密钥致盲功能。它具有以下函数：

- **DERIVE_PUBLIC(privkey)** : 返回与给定私钥对应的公钥。

- **SIGN(privkey, m)** : 使用私钥 privkey 对给定消息 m 返回一个签名。

- **VERIFY(pubkey, m, sig)** : 验证签名 sig 对公钥 pubkey 和消息 m 的有效性。如果签名有效则返回 true，否则返回 false。

它还必须支持以下密钥盲化操作：

- **GENERATE_ALPHA(data, secret)** : 为那些知道数据和可选密钥的人生成 alpha。结果必须与私钥具有相同的分布。

- **BLIND_PRIVKEY(privkey, alpha)** : 使用秘密值 alpha 对私钥进行盲化处理。

- **BLIND_PUBKEY(pubkey, alpha)** : 使用秘密值 alpha 对公钥进行盲化。对于给定的密钥对 (privkey, pubkey)，以下关系成立：

```
BLIND_PUBKEY(pubkey, alpha) ==
DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))
```
**DH** : X25519 公钥协商系统。私钥 32 字节，公钥 32 字节，输出 32 字节。它具有以下功能：

- **GENERATE_PRIVATE()** : 生成新的私钥。

- **DERIVE_PUBLIC(privkey)** : 返回与给定私钥对应的公钥。

- **DH(privkey, pubkey)** : 从给定的私钥和公钥生成共享密钥。

**HKDF(salt, ikm, info, n)** : 一种密码学密钥派生函数，接受一些输入密钥材料 ikm（应具有良好的熵值但不要求是均匀随机字符串）、长度为 32 字节的盐值，以及特定于上下文的 'info' 值，产生 n 字节的输出，适合用作密钥材料。

使用 [RFC-5869](https://tools.ietf.org/html/rfc5869) 中指定的 HKDF，采用 [RFC-2104](https://tools.ietf.org/html/rfc2104) 中指定的 HMAC 哈希函数 SHA-256。这意味着 SALT_LEN 最大为 32 字节。

### 格式

加密的 LS2 格式由三个嵌套层组成：

- 包含存储和检索所需明文信息的外层。
- 处理客户端身份验证的中间层。
- 包含实际 LS2 数据的内层。

整体格式如下：

```
Layer 0 data + Enc(layer 1 data + Enc(layer 2 data)) + Signature
```
注意加密的 LS2 是盲化的。Destination 不在头部中。DHT 存储位置是 SHA-256(sig type || blinded public key)，并且每日轮换。

不使用上述指定的标准 LS2 头部。

#### 层 0（外层）

**类型** : 1 字节

实际上不在头部中，但属于签名覆盖的数据部分。从 Database Store Message 中的字段获取。

**Blinded Public Key Sig Type** : 2 字节，大端序

这将始终是类型 11，标识一个 Red25519 盲化密钥。

**盲化公钥** : 长度由签名类型隐含确定

**发布时间戳** : 4 字节，大端序

从纪元开始的秒数，将在2106年回滚

**Expires** : 2 字节，大端序

从发布时间戳开始的偏移量（秒），最大18.2小时

**标志** : 2 字节

位顺序：15 14 ... 3 2 1 0

- 位 0：如果为 0，无离线密钥；如果为 1，有离线密钥
- 其他位：设置为 0 以便与未来用途兼容

**临时密钥数据** : 如果标志指示离线密钥则存在

- **过期时间戳**：4字节，大端序。自纪元以来的秒数，2106年溢出
- **临时签名类型**：2字节，大端序
- **临时签名公钥**：长度由签名类型决定
- **签名**：长度由盲化公钥签名类型决定。覆盖过期时间戳、临时签名类型和临时公钥。使用盲化公钥进行验证。

**lenOuterCiphertext** : 2 字节，大端序

**outerCiphertext** : lenOuterCiphertext 字节

加密的第1层数据。密钥派生和加密算法请见下文。

**签名**：长度由所用签名密钥的签名类型决定

签名覆盖上述所有内容。如果标志指示离线密钥，则使用临时公钥验证签名。否则，使用盲化公钥验证签名。

#### 第一层（中间层）

**标志** : 1 字节

位顺序：76543210

- 位 0：0 表示所有人，1 表示每客户端，后跟认证部分
- 位 3-1：认证方案，仅当位 0 设置为 1（每客户端）时使用，否则为 000
  - 000：DH 客户端认证（或无每客户端认证）
  - 001：PSK 客户端认证
- 位 7-4：未使用，设置为 0 以保持未来兼容性

**DH 客户端认证数据**：当标志位 0 设置为 1 且标志位 3-1 设置为 000 时存在。

- **ephemeralPublicKey** : 32 字节
- **clients** : 2 字节，大端序。后续 authClient 条目的数量，每个 40 字节
- **authClient** : 单个客户端的授权数据。请参阅下面的每客户端授权算法。
  - **clientID_i** : 8 字节
  - **clientCookie_i** : 32 字节

**PSK 客户端认证数据**：当标志位 0 设置为 1 且标志位 3-1 设置为 001 时存在。

- **authSalt** : 32 字节
- **clients** : 2 字节，大端序。后续 authClient 条目的数量，每个条目 40 字节
- **authClient** : 单个客户端的授权数据。请参见下方的每客户端授权算法。
  - **clientID_i** : 8 字节
  - **clientCookie_i** : 32 字节

**innerCiphertext** : 长度由 lenOuterCiphertext 隐含（剩余的任何数据）

加密的第2层数据。密钥派生和加密算法请参见下文。

#### 第二层（内层）

**类型** : 1 字节

3（LS2）或 7（Meta LS2）

**数据** : 给定类型的 LeaseSet2 数据。

包括头部和签名。

### 盲化密钥推导

我们使用以下基于 Ed25519 和 ZCash RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) 的密钥盲化方案。Red25519 签名在 Ed25519 曲线上进行，使用 SHA-512 作为哈希函数。

我们不使用 Tor 的 rend-spec-v3.txt 附录 A.2 [TOR-REND-SPEC-V3](https://spec.torproject.org/rend-spec-v3)，虽然它有类似的设计目标，但是因为其盲化公钥可能偏离素数阶子群，存在未知的安全隐患。

#### 目标

- 未盲化目标中的签名公钥必须是 Ed25519（签名类型 7）或 Red25519（签名类型 11）；不支持其他签名类型
- 如果签名公钥离线，临时签名公钥也必须是 Ed25519
- 盲化在计算上很简单
- 使用现有的密码学原语
- 盲化公钥无法取消盲化
- 盲化公钥必须在 Ed25519 曲线和素数阶子群上
- 必须知道目标的签名公钥（不需要完整目标）来推导盲化公钥
- 可选地提供推导盲化公钥所需的额外密钥

#### 安全

盲化方案的安全性要求alpha的分布与未盲化私钥的分布相同。然而，当我们将Ed25519私钥（sig type 7）盲化为Red25519私钥（sig type 11）时，分布是不同的。为了满足zcash第4.1.6.1节 [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) 的要求，Red25519（sig type 11）也应该用于未盲化密钥，这样"重新随机化公钥和该密钥下的签名的组合不会泄露其被重新随机化的原始密钥"。我们允许现有目标使用type 7，但建议将要加密的新目标使用type 11。

#### 定义

**B** : Ed25519基点（生成元）2^255 - 19，如[ED25519-REFS](http://cr.yp.to/papers.html#ed25519)中所述

**L** : Ed25519 阶数 2^252 + 27742317777372353535851937790883648493，如 [ED25519-REFS](http://cr.yp.to/papers.html#ed25519) 中所述

**DERIVE_PUBLIC(a)** : 将私钥转换为公钥，如 Ed25519 中的操作（乘以 G）

**alpha** : 一个 32 字节的随机数，只有知道目标地址的人才知道。

**GENERATE_ALPHA(destination, date, secret)** : 为知道目标地址和密钥的用户生成当前日期的alpha值。结果必须与Ed25519私钥具有相同的分布。

**a** : 用于签署目标的未盲化32字节EdDSA或RedDSA签名私钥

**A** : 目标中未盲化的32字节EdDSA或RedDSA签名公钥，= DERIVE_PUBLIC(a)，如Ed25519中所示

**a'** : 用于签名加密 leaseset 的盲化 32 字节 EdDSA 签名私钥。这是一个有效的 EdDSA 私钥。

**A'** : Destination中的盲化32字节EdDSA签名公钥，可以通过DERIVE_PUBLIC(a')生成，或者从A和alpha生成。这是一个有效的EdDSA公钥，位于曲线上和素数阶子群中。

**LEOS2IP(x)** : 将输入字节的顺序翻转为小端序

**H\*(x)** : 32字节 = (LEOS2IP(SHA512(x))) mod B，与Ed25519哈希和约简中相同

#### 盲化计算

必须每天（UTC时间）生成新的密钥 alpha 和致盲密钥。

秘密 alpha 和盲化密钥的计算方法如下：

GENERATE_ALPHA(destination, date, secret)，对于所有参与方：

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
BLIND_PRIVKEY()，用于发布 leaseSet 的所有者：

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
BLIND_PUBKEY()，用于客户端检索 leaseset：

```
alpha = GENERATE_ALPHA(destination, date, secret)
A = destination's signing public key
// Addition using group elements (points on the curve)
blinded public key = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```
两种计算 A' 的方法都产生相同的结果，符合要求。

#### 签名

未屏蔽的 leaseset 由未屏蔽的 Ed25519 或 Red25519 签名私钥签名，并使用未屏蔽的 Ed25519 或 Red25519 签名公钥（签名类型 7 或 11）进行验证，这与常规方式相同。

如果签名公钥离线，未盲化的leaseset由未盲化的临时Ed25519或Red25519签名私钥签名，并使用未盲化的Ed25519或Red25519临时签名公钥（签名类型7或11）进行验证，这与通常情况相同。有关加密leasesets的离线密钥的其他说明，请参见下文。

对于加密 leaseset 的签名，我们使用基于 RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) 的 Red25519 来使用盲化密钥进行签名和验证。Red25519 签名基于 Ed25519 曲线，使用 SHA-512 作为哈希函数。

Red25519与标准Ed25519类似，除了以下所述的差异。

#### 签名/验证计算

加密 leaseset 的外层部分使用 Red25519 密钥和签名。

Red25519 与 Ed25519 类似。有两个区别：

Red25519 私钥是从随机数生成的，然后必须对 L 取模，其中 L 在上面已定义。Ed25519 私钥是从随机数生成的，然后通过对字节 0 和 31 进行按位掩码操作来"钳制"。这在 Red25519 中不会执行。上面定义的函数 GENERATE_ALPHA() 和 BLIND_PRIVKEY() 使用模 L 生成正确的 Red25519 私钥。

在 Red25519 中，签名时 r 的计算使用了额外的随机数据，并使用公钥值而不是私钥的哈希值。由于随机数据的存在，每个 Red25519 签名都是不同的，即使使用相同的密钥对相同的数据进行签名也是如此。

```
Signing:
  T = 80 random bytes
  r = H*(T || publickey || message)
  (rest is the same as in Ed25519)

Verification:
  Same as for Ed25519
```
### 加密和处理

#### 子凭证的派生

作为盲化过程的一部分，我们需要确保加密的 LS2 只能被知道相应 Destination 签名公钥的人解密。不需要完整的 Destination。为了实现这一点，我们从签名公钥派生一个凭证：

```
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
credential = H("credential", keydata)
```
个性化字符串确保凭证不会与任何用作 DHT 查找键的哈希发生冲突，例如普通的目标哈希。

对于给定的盲化密钥，我们可以派生出一个子凭证：

```
subcredential = H("subcredential", credential || blindedPublicKey)
```
subcredential 包含在下面的密钥派生过程中，这将这些密钥绑定到对 Destination 签名公钥的知识。

#### 第一层加密

首先，准备密钥派生过程的输入：

```
outerInput = subcredential || publishedTimestamp
```
接下来，生成一个随机salt：

```
outerSalt = CSRNG(32)
```
然后推导出用于加密第1层的密钥：

```
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
最后，第一层明文被加密并序列化：

```
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```
#### 第一层解密

salt 是从第 1 层密文中解析出来的：

```
outerSalt = outerCiphertext[0:31]
```
然后推导出用于加密第1层的密钥：

```
outerInput = subcredential || publishedTimestamp
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
最后，第1层密文被解密：

```
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```
#### 第二层加密

当启用客户端授权时，`authCookie` 按以下方式计算。当禁用客户端授权时，`authCookie` 是零长度字节数组。

加密过程与第1层类似：

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = CSRNG(32)
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```
#### 第二层解密

当启用客户端授权时，`authCookie` 按如下所述计算。当禁用客户端授权时，`authCookie` 是零长度字节数组。

解密过程与第 1 层类似：

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = innerCiphertext[0:31]
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```
### 客户端授权

当为目标启用客户端授权时，服务器维护一个客户端列表，这些客户端被授权解密加密的 LS2 数据。每个客户端存储的数据取决于授权机制，包括每个客户端生成并通过安全的带外机制发送给服务器的某种形式的密钥材料。

有两种实现每客户端授权的替代方案：

#### DH 客户端授权

每个客户端生成一个 DH 密钥对 `[csk_i, cpk_i]`，并将公钥 `cpk_i` 发送给服务器。

##### 服务器处理

服务器生成一个新的 `authCookie` 和一个临时的 DH 密钥对：

```
authCookie = CSRNG(32)
esk = GENERATE_PRIVATE()
epk = DERIVE_PUBLIC(esk)
```
然后对于每个授权的客户端，服务器使用其公钥加密 `authCookie`：

```
sharedSecret = DH(esk, cpk_i)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
服务器将每个 `[clientID_i, clientCookie_i]` 元组与 `epk` 一起放入加密 LS2 的第 1 层中。

##### 客户端处理

客户端使用其私钥来推导出预期的客户端标识符 `clientID_i`、加密密钥 `clientKey_i` 和加密初始化向量 `clientIV_i`：

```
sharedSecret = DH(csk_i, epk)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
然后客户端在第1层授权数据中搜索包含 `clientID_i` 的条目。如果存在匹配的条目，客户端解密它以获得 `authCookie`：

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### 预共享密钥客户端授权

每个客户端生成一个32字节的密钥`psk_i`，并将其发送给服务器。或者，服务器可以生成密钥，并将其发送给一个或多个客户端。

##### 服务器处理

服务器生成新的 `authCookie` 和盐值：

```
authCookie = CSRNG(32)
authSalt = CSRNG(32)
```
然后对于每个授权的客户端，服务器使用其预共享密钥加密 `authCookie`：

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
服务器将每个 `[clientID_i, clientCookie_i]` 元组与 `authSalt` 一起放入加密 LS2 的第 1 层中。

##### 客户端处理

客户端使用其预共享密钥来派生其预期的客户端标识符 `clientID_i`、加密密钥 `clientKey_i` 和加密初始化向量 `clientIV_i`：

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
然后客户端搜索第1层授权数据中包含 `clientID_i` 的条目。如果存在匹配的条目，客户端将解密它以获取 `authCookie`：

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### 安全考虑

上述两种客户端授权机制都为客户端成员身份提供隐私保护。仅知道 Destination 的实体可以看到任何时候有多少客户端订阅，但无法跟踪哪些客户端被添加或撤销。

服务器在每次生成加密的 LS2 时应该随机化客户端的顺序，以防止客户端了解自己在列表中的位置并推断其他客户端何时被添加或撤销。

服务器可以选择通过在授权数据列表中插入随机条目来隐藏订阅的客户端数量。

##### DH 客户端授权的优势

- 该方案的安全性并不完全依赖于客户端密钥材料的带外交换。客户端的私钥永远不需要离开其设备，因此能够拦截带外交换但无法破解 DH 算法的攻击者，既无法解密加密的 LS2，也无法确定客户端被授予访问权限的时长。

##### DH 客户端授权的缺点

- 服务器端需要对 N 个客户端执行 N + 1 次 DH 操作。
- 客户端需要执行一次 DH 操作。
- 需要客户端生成密钥。

##### PSK 客户端授权的优势

- 不需要 DH 操作。
- 允许服务器生成密钥。
- 如果需要，允许服务器与多个客户端共享同一密钥。

##### PSK 客户端授权的缺点

- 该方案的安全性严重依赖于客户端密钥材料的带外交换。如果攻击者截获了特定客户端的交换信息，就可以解密该客户端有权访问的任何后续加密 LS2，并且还能确定该客户端的访问权限何时被撤销。

### 使用 Base 32 地址的加密 LS

你不能为加密的 LS2 使用传统的 base 32 地址，因为它只包含目标的哈希值。它不提供非盲化的公钥。因此，仅有 base 32 地址是不够的。客户端需要完整的目标（包含公钥），或者单独的公钥。如果客户端在地址簿中有完整的目标，并且地址簿支持通过哈希值进行反向查找，那么可以获取公钥。

所以我们需要一种新的格式，将公钥而不是哈希值放入base32地址中。这种格式还必须包含公钥的签名类型，以及盲化方案的签名类型。总的要求是32 + 3 = 35字节，在base 32中需要56个字符，对于更长的公钥类型则需要更多字符。

```
data = ((1 byte flags || 1 byte unblinded sigtype || 1 byte blinded sigtype) XOR checksum) || 32 byte pubkey
address = Base32Encode(data) || ".b32.i2p"
```
我们使用与传统base 32地址相同的".b32.i2p"后缀。加密leaseSet的地址由56个编码字符（35个解码字节）标识，而传统base 32地址为52个字符（32字节）。b32末尾的5个未使用位必须为0。

你不能将加密的 LS2 用于 bittorrent，因为紧凑宣告回复只有 32 字节。这 32 字节只包含哈希值。没有空间来指示 leaseset 是否加密，或者签名类型。

查看[命名规范](/docs/specs/naming)或[提案 149](/proposals/149-b32-encrypted-ls2)了解新格式的更多信息。

### 使用离线密钥的加密 LS

对于使用离线密钥的加密 leaseSet，盲化私钥也必须离线生成，每天生成一个。

由于可选的离线签名块位于加密 leaseSet 的明文部分，任何抓取 floodfill 的人都可以利用这一点在几天内跟踪 leaseSet（但无法解密）。为了防止这种情况，密钥所有者也应该每天生成新的临时密钥。临时密钥和盲化密钥都可以提前生成，并批量交付给 router。

目前没有定义用于打包多个临时和盲化密钥并将其提供给客户端或router的文件格式。也没有定义I2CP协议增强来支持使用离线密钥的加密leaseSet。

### 注释

- 使用加密 leaseSet 的服务会将加密版本发布到 floodfill。但是，为了提高效率，一旦通过身份验证（例如通过白名单），它会在包装的 garlic 消息中向客户端发送未加密的 leaseSet。
- Floodfill 可能会将最大大小限制为合理值以防止滥用。
- 解密后，应该进行多项检查，包括验证内部时间戳和过期时间与顶层的时间戳和过期时间匹配。
- 选择 ChaCha20 而不是 AES。虽然在有 AES 硬件支持时速度相似，但在没有 AES 硬件支持时（如低端 ARM 设备），ChaCha20 的速度要快 2.5-3 倍。

## 参考资料

- **[ED25519-REFS]** "高速高安全性签名" 由 Daniel J. Bernstein、Niels Duif、Tanja Lange、Peter Schwabe 和 Bo-Yin Yang 撰写。[http://cr.yp.to/papers.html#ed25519](http://cr.yp.to/papers.html#ed25519)
- **[KEYBLIND-PROOF]** [https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html](https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html)
- **[KEYBLIND-REFS]** [https://trac.torproject.org/projects/tor/ticket/8106](https://trac.torproject.org/projects/tor/ticket/8106) 和 [https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html](https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html)
- **[PRNG-REFS]** [http://projectbullrun.org/dual-ec/ext-rand.html](http://projectbullrun.org/dual-ec/ext-rand.html) 和 [https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html)
- **[RFC-2104]** [https://tools.ietf.org/html/rfc2104](https://tools.ietf.org/html/rfc2104)
- **[RFC-4880-S5.1]** [https://tools.ietf.org/html/rfc4880#section-5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
- **[RFC-5869]** [https://tools.ietf.org/html/rfc5869](https://tools.ietf.org/html/rfc5869)
- **[RFC-7539-S2.4]** [https://tools.ietf.org/html/rfc7539#section-2.4](https://tools.ietf.org/html/rfc7539#section-2.4)
- **[TOR-REND-SPEC-V3]** [https://spec.torproject.org/rend-spec-v3](https://spec.torproject.org/rend-spec-v3)
- **[ZCASH]** [https://github.com/zcash/zips/tree/master/protocol/protocol.pdf](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)
