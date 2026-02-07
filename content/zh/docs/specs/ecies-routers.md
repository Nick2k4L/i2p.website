---
title: "ECIES-X25519 Router消息"
description: "使用 X25519 向 ECIES router 进行 Garlic message encryption 的规范"
slug: "ecies-routers"
category: "协议"
lastUpdated: "2025-03"
accurateFor: "0.9.65"
---

## 注意

从0.9.49版本开始支持。网络部署和测试正在进行中。可能会有小幅修订。请参见[提案156](/proposals/156-ecies-routers)。

## 概述

本文档规定了向 ECIES router 发送 garlic message encryption 的方法，使用了 [ECIES-X25519](/docs/specs/ecies) 引入的加密原语。这是将 router 从 ElGamal 转换为 ECIES-X25519 密钥的整体 [提案 156](/proposals/156-ecies-routers) 的一部分。此规范从 0.9.49 版本开始实施。

有关 ECIES router 所需的所有更改概述，请参阅[提案 156](/proposals/156-ecies-routers)。有关发往 ECIES-X25519 目标的 Garlic Messages，请参阅 [ECIES-X25519](/docs/specs/ecies)。

### 密码学原语

实现此规范所需的原语包括：

- AES-256-CBC 如 [密码学](/docs/specs/cryptography) 中所述
- STREAM ChaCha20/Poly1305 函数：ENCRYPT(k, n, plaintext, ad) 和 DECRYPT(k, n, ciphertext, ad) - 如 [NTCP2](/docs/specs/ntcp2)、[ECIES-X25519](/docs/specs/ecies) 和 [RFC-7539](https://tools.ietf.org/html/rfc7539) 中所述
- X25519 DH 函数 - 如 [NTCP2](/docs/specs/ntcp2) 和 [ECIES-X25519](/docs/specs/ecies) 中所述
- HKDF(salt, ikm, info, n) - 如 [NTCP2](/docs/specs/ntcp2) 和 [ECIES-X25519](/docs/specs/ecies) 中所述

其他在别处定义的 Noise 函数：

- MixHash(d) - 如 [NTCP2](/docs/specs/ntcp2) 和 [ECIES-X25519](/docs/specs/ecies) 中所述
- MixKey(d) - 如 [NTCP2](/docs/specs/ntcp2) 和 [ECIES-X25519](/docs/specs/ecies) 中所述

## 设计

ECIES Router SKM 不需要像 [ECIES](/docs/specs/ecies) 中为 Destinations 指定的完整 Ratchet SKM。没有使用 IK 模式进行非匿名消息的要求。威胁模型不需要 Elligator2 编码的临时密钥。

因此，router SKM 将使用 Noise "N" 模式，与 [Prop152](/proposals/152-ecies-tunnels) 中为 tunnel 构建指定的相同。它将使用与 [ECIES](/docs/specs/ecies) 中为 Destinations 指定的相同载荷格式。[ECIES](/docs/specs/ecies) 中指定的零静态密钥（无绑定或会话）IK 模式将不会被使用。

如果在查找请求中要求，查找的回复将使用棘轮标签进行加密。这在 [Prop154](/proposals/154-ecies-lookups) 中有文档说明，现在在 [I2NP](/docs/specs/i2np) 中进行了规定。

这种设计使得router只需要一个ECIES会话密钥管理器。无需像[ECIES](/docs/specs/ecies)中为Destination描述的那样运行"双密钥"会话密钥管理器。Router只有一个公钥。

ECIES router没有ElGamal静态密钥。router仍然需要ElGamal的实现来通过ElGamal router构建tunnel，并向ElGamal router发送加密消息。

ECIES router 可能需要部分 ElGamal Session Key Manager 来接收从 0.9.46 版本之前的 floodfill router 收到的作为 NetDB 查询回复的 ElGamal 标记消息，因为这些 router 没有实现 [Prop152](/proposals/152-ecies-tunnels) 中指定的 ECIES 标记回复。如果没有这个功能，ECIES router 可能无法从 0.9.46 版本之前的 floodfill router 请求加密回复。

这是可选的。决策可能在不同的I2P实现中有所不同，并且可能取决于已升级到0.9.46或更高版本的网络数量。截至目前，大约85%的网络已升级到0.9.46或更高版本。

### Noise 协议框架

本规范基于 [Noise Protocol Framework](https://noiseprotocol.org/noise.html)（修订版 34，2018-07-11）提供要求。在 Noise 术语中，Alice 是发起者，Bob 是响应者。

它基于 Noise protocol Noise_N_25519_ChaChaPoly_SHA256。这个 Noise protocol 使用以下原语：

- **单向握手模式：N** - Alice 不向 Bob 传输她的静态密钥 (N)
- **DH 函数：X25519** - X25519 DH，密钥长度为 32 字节，如 [RFC-7748](https://tools.ietf.org/html/rfc7748) 中规定。
- **加密函数：ChaChaPoly** - AEAD_CHACHA20_POLY1305，如 [RFC-7539](https://tools.ietf.org/html/rfc7539) 第 2.8 节中规定。12 字节 nonce，前 4 字节设置为零。与 [NTCP2](/docs/specs/ntcp2) 中的相同。
- **哈希函数：SHA256** - 标准 32 字节哈希，在 I2P 中已广泛使用。

### 握手模式

握手使用 [Noise](https://noiseprotocol.org/noise.html) 握手模式。

使用以下字母映射：

- e = 一次性临时密钥
- s = 静态密钥
- p = 消息载荷

构建请求与 Noise N 模式相同。这也与 [NTCP2](/docs/specs/ntcp2) 中使用的 XK 模式的第一条消息（会话请求）相同。

```
<- s
  ...
  e es p ->
```
### 消息加密

消息被创建并使用非对称加密方式加密到目标 router。消息的非对称加密目前使用 ElGamal 算法，如 [Cryptography](/docs/specs/cryptography) 中所定义，并包含 SHA-256 校验和。这种设计不具备前向保密性。

ECIES设计使用单向Noise模式"N"，采用ECIES-X25519临时-静态DH，结合HKDF和ChaCha20/Poly1305 AEAD，以提供前向保密性、完整性和身份验证。Alice是匿名消息发送者，可以是一个router或目标。目标ECIES router是Bob。

### 回复加密

回复不是此协议的一部分，因为Alice是匿名的。如果有回复密钥，会被打包在请求消息中。有关数据库查找消息，请参见[I2NP规范](/docs/specs/i2np)。

对数据库查找消息的回复是数据库存储或数据库搜索回复消息。它们作为现有会话消息进行加密，使用32字节回复密钥和8字节回复标签，如[I2NP](/docs/specs/i2np)和[Prop154](/proposals/154-ecies-lookups)中所指定。

对于数据库存储消息没有明确的回复。发送方可以将自己的回复作为garlic消息捆绑给自己，其中包含一个传递状态消息。

## 规范

X25519: 参见 [ECIES](/docs/specs/ecies)。

Router 身份和密钥证书：参见[通用结构](/docs/specs/common-structures)。

### 请求加密

请求加密与 [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) 和 [Prop152](/proposals/152-ecies-tunnels) 中指定的相同，使用 Noise "N" 模式。

如果在查找中请求，对查找的回复将使用棘轮标签进行加密。数据库查找请求消息包含32字节的回复密钥和8字节的回复标签，如[I2NP](/docs/specs/i2np)和[Prop154](/proposals/154-ecies-lookups)中所指定的。该密钥和标签用于加密回复。

不创建标签集。在 ECIES-X25519-AEAD-Ratchet [Prop144](/proposals/144-ecies-x25519-aead-ratchet) 和 [ECIES](/docs/specs/ecies) 中指定的零静态密钥方案将不会被使用。临时密钥不会进行 Elligator2 编码。

通常，这些将是新会话消息，并且会使用零静态密钥发送（无绑定或会话），因为消息的发送者是匿名的。

#### 初始 ck 和 h 的 KDF

这是标准的 [Noise](https://noiseprotocol.org/noise.html) 协议，使用模式 "N" 和标准协议名称。这与 [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) 和 [Prop152](/proposals/152-ecies-tunnels) 中为 tunnel 构建消息指定的内容相同。

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
#### 消息的密钥派生函数

消息创建者为每个消息生成一个临时的 X25519 密钥对。每个消息的临时密钥必须是唯一的。这与 [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) 和 [Prop152](/proposals/152-ecies-tunnels) 中为 tunnel 构建消息指定的要求相同。

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
#### 负载

负载使用与 [ECIES](/docs/specs/ecies) 和 [Prop144](/proposals/144-ecies-x25519-aead-ratchet) 中定义的相同块格式。所有消息必须包含 DateTime 块以防止重放攻击。

## 实现说明

- 较旧的 router 不会检查 router 的加密类型，会发送 ElGamal 加密的消息。一些最新的 router 存在错误，会发送各种类型的格式错误的消息。实现者应该在可能的情况下在 DH 操作之前检测并拒绝这些记录，以减少 CPU 使用率。

## 参考文献

- [Common Structures](/docs/specs/common-structures)
- [密码学](/docs/specs/cryptography)
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
