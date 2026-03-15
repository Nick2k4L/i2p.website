---
title: "SSU2 规范"
description: "安全半可靠 UDP 传输协议版本 2"
slug: "ssu2"
category: "传输协议"
lastUpdated: "2026-03"
accurateFor: "0.9.69"
---

## 状态

基本完成。请参阅 [Prop159](/proposals/159-ssu2) 了解更多背景和目标，包括安全分析、威胁模型、SSU 1 安全性和问题的回顾，以及 QUIC 规范摘录。

推出计划：

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
基本会话包括握手和数据阶段。扩展协议包括中继和对等体测试。

## 概述

本规范定义了一个经过身份验证的密钥协商协议，以提高 [SSU](/docs/transport/ssu) 对各种形式的自动识别和攻击的抵抗能力。

与其他 I2P 传输协议一样，SSU2 用于点对点（router 到 router）传输 I2NP 消息。它不是通用的数据管道。与 [SSU](/docs/transport/ssu) 一样，它还提供两个额外的服务：用于 NAT 穿越的中继，以及用于确定入站可达性的对等测试。它还提供了第三个服务（SSU 中没有），即当对等节点更改 IP 或端口时的连接迁移。

## 设计概述

### 摘要

我们依赖多个现有协议，包括 I2P 内部协议和外部标准，以获得启发、指导和代码重用：

- 威胁模型：来自 NTCP2 [NTCP2](/docs/specs/ntcp2)，以及 QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001) 分析的与 UDP 传输相关的重要附加威胁。
- 密码学选择：来自 [NTCP2](/docs/specs/ntcp2)。
- 握手：来自 [NTCP2](/docs/specs/ntcp2) 和 [NOISE](https://noiseprotocol.org/noise.html) 的 Noise XK。由于 UDP 提供的封装（固有的消息边界），可以对 NTCP2 进行重大简化。
- 握手临时密钥混淆：改编自 [NTCP2](/docs/specs/ntcp2)，但使用来自 [ECIES](/docs/specs/ecies) 的 ChaCha20 而不是 AES。
- 数据包头：改编自 WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) 和 QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001)。
- 数据包头混淆：改编自 [NTCP2](/docs/specs/ntcp2)，但使用来自 [ECIES](/docs/specs/ecies) 的 ChaCha20 而不是 AES。
- 数据包头保护：改编自 QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) 和 [Nonces](https://eprint.iacr.org/2019/624.pdf)
- 头部用作 AEAD 关联数据，如 [ECIES](/docs/specs/ecies) 中所示。
- 数据包编号：改编自 WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) 和 QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001)。
- 消息：改编自 [SSU](/docs/transport/ssu)
- I2NP 分片：改编自 [SSU](/docs/transport/ssu)
- 中继和对等测试：改编自 [SSU](/docs/transport/ssu)
- 中继和对等测试数据的签名：来自通用结构规范 [Common](/docs/specs/common-structures)
- 块格式：来自 [NTCP2](/docs/specs/ntcp2) 和 [ECIES](/docs/specs/ecies)。
- 填充和选项：来自 [NTCP2](/docs/specs/ntcp2) 和 [ECIES](/docs/specs/ecies)。
- 确认，否定确认：改编自 QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000)。
- 流量控制：待定

没有使用I2P之前未曾使用过的新加密原语。

### 传输保证

与其他I2P传输协议NTCP、NTCP2和SSU 1一样，该传输协议并非用于传输有序字节流的通用设施。它专为传输I2NP消息而设计。不提供"流"抽象。

此外，对于 SSU，它包含额外的功能，用于对等体协助的 NAT 穿越和可达性测试（入站连接）。

对于 SSU 1，它不提供 I2NP 消息的有序传递。也不提供 I2NP 消息的可靠传递保证。由于效率考虑，或者因为 UDP 数据报的乱序传递或丢失，I2NP 消息可能会乱序传递到远端，或者可能根本无法传递。如有必要，I2NP 消息可能会被多次重传，但传递最终可能会失败，而不会导致整个连接断开。此外，即使在为其他 I2NP 消息进行重传（丢失恢复）时，新的 I2NP 消息也可能继续发送。

此协议并不能完全防止 I2NP 消息的重复传递。router 应该强制执行 I2NP 过期机制，并使用布隆过滤器或其他基于 I2NP 消息 ID 的机制。请参见下面的 I2NP 消息重复部分。

### Noise Protocol Framework

本规范基于 Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html)（修订版 33，2017-10-04）提供要求。Noise 具有与 Station-To-Station 协议 [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol) 类似的属性，后者是 [SSU](/docs/transport/ssu) 协议的基础。在 Noise 术语中，Alice 是发起者，Bob 是响应者。

SSU2 基于 Noise 协议 Noise_XK_25519_ChaChaPoly_SHA256。（初始密钥派生函数的实际标识符是 "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256" 以表示 I2P 扩展 - 请参见下面的 KDF 1 部分）

注意：此标识符与用于 NTCP2 的标识符不同，因为所有三个握手消息都将头部用作关联数据。

此 Noise 协议使用以下原语：

- Handshake Pattern：XK Alice 向 Bob 传输她的密钥 (X) Alice 已经知道 Bob 的静态密钥 (K)
- DH Function：X25519 使用密钥长度为 32 字节的 X25519 DH，如 [RFC-7748](https://tools.ietf.org/html/rfc7748) 中所规定。
- Cipher Function：ChaChaPoly AEAD_CHACHA20_POLY1305，如 [RFC-7539](https://tools.ietf.org/html/rfc7539) 第 2.8 节所规定。12 字节 nonce，前 4 字节设置为零。
- Hash Function：SHA256 标准 32 字节哈希，已在 I2P 中广泛使用。

### 框架的补充

本规范定义了对 Noise_XK_25519_ChaChaPoly_SHA256 的以下增强。这些增强通常遵循 [NOISE](https://noiseprotocol.org/noise.html) 第 13 节中的指导原则。

1) 握手消息（Session Request、Created、Confirmed）包含一个16或32字节的头部。2) 握手消息（Session Request、Created、Confirmed）的头部在加密/解密之前用作mixHash()的输入，以将头部绑定到消息。3) 头部经过加密和保护。4) 明文临时密钥使用已知密钥和IV通过ChaCha20加密进行混淆。这比elligator2更快。5) 为消息1、消息2和数据阶段定义了载荷格式。当然，这在Noise中是未定义的。

数据阶段使用类似于但与 Noise 数据阶段不兼容的加密方式。

### 会话建立

我们定义以下对应于所使用的密码学构建块的函数。

#### 长标头

ZEROLEN

#### 短标题

:   零长度字节数组

#### 连接 ID 编号

H(p, d)

#### 数据包编号

:   SHA-256 哈希函数，接受个性化字符串 p 和数据 d，产生长度为 32 字节的输出。如 [NOISE](https://noiseprotocol.org/noise.html) 中所定义。下面的 || 表示追加。

## 定义

MixHash(d)

:   SHA-256 哈希函数，接受前一个哈希值 h 和新数据 d，产生长度为 32 字节的输出。下面的 || 表示追加。

STREAM

:   如 [RFC-7539](https://tools.ietf.org/html/rfc7539) 中规定的 ChaCha20/Poly1305 AEAD。S_KEY_LEN = 32 且 S_IV_LEN = 12。

DH

    Use SHA-256 as follows:

        H(p, d) := SHA-256(p || d)

:   X25519公钥协商系统。32字节的私钥，32字节的公钥，产生32字节的输出。它具有以下功能：

HKDF(salt, ikm, info, n)

    Use SHA-256 as follows:

        MixHash(d) := h = SHA-256(h || d)

:   一种密码学密钥派生函数，它接受一些输入密钥材料 ikm（应该具有良好的熵值，但不要求是均匀随机字符串）、长度为32字节的盐值，以及特定上下文的'info'值，并产生适合用作密钥材料的n字节输出。

MixKey(d)

    ENCRYPT(k, n, plaintext, ad)

    :   Encrypts plaintext using the cipher key k, and nonce n which MUST be unique for the key k. Associated data ad is optional. Returns a ciphertext that is the size of the plaintext + 16 bytes for the HMAC.

        The entire ciphertext must be indistinguishable from random if the key is secret.

    DECRYPT(k, n, ciphertext, ad)

    :   Decrypts ciphertext using the cipher key k, and nonce n. Associated data ad is optional. Returns the plaintext.

:   使用 HKDF() 与之前的 chainKey 和新数据 d，并设置新的 chainKey 和 k。如 [NOISE](https://noiseprotocol.org/noise.html) 中定义。

每个UDP数据报恰好包含一条消息。数据报的长度（在IP和UDP头部之后）就是消息的长度。填充（如果有的话）包含在消息内部的填充块中。在本文档中，我们大多数情况下可以互换使用"数据报"和"数据包"这两个术语。每个数据报（或数据包）包含单个消息（不像QUIC，其中一个数据报可能包含多个QUIC数据包）。"数据包头部"是指IP/UDP头部之后的部分。

    GENERATE_PRIVATE()

    :   Generates a new private key.

    DERIVE_PUBLIC(privkey)

    :   Returns the public key corresponding to the given private key.

    DH(privkey, pubkey)

    :   Generates a shared secret from the given private and public keys.

例外：Session Confirmed 消息的独特之处在于它可能会被分片到多个数据包中。更多信息请参见下面的 Session Confirmed 分片部分。

所有SSU2消息长度至少为40字节。任何长度为1-39字节的消息都是无效的。所有SSU2消息的长度小于或等于1472字节（IPv4）或1452字节（IPv6）。消息格式基于Noise消息，并针对帧结构和不可区分性进行了修改。使用标准Noise库的实现必须将接收到的消息预处理为标准Noise消息格式。所有加密字段都是AEAD密文。

    Use HKDF as specified in [RFC-5869](https://tools.ietf.org/html/rfc5869), using the HMAC hash function SHA-256 as specified in [RFC-2104](https://tools.ietf.org/html/rfc2104). This means that SALT_LEN is 32 bytes max.

定义了以下消息：

当Alice拥有之前从Bob接收到的有效令牌时，标准建立序列如下：

    Use HKDF as follows:

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]

## 消息

当 Alice 没有有效的令牌时，建立序列如下：

当 Alice 认为她拥有一个有效的令牌，但 Bob 拒绝了它时（可能是因为 Bob 重启了），建立序列如下：

Bob 可以通过回复包含带有原因代码的 Termination 块的 Retry 消息来拒绝 Session 或 Token Request。基于原因代码，Alice 在一段时间内不应尝试另一个请求：

使用 Noise 术语，建立和数据序列如下：（有效载荷安全属性）

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
### 数据包头部

一旦会话建立完成，Alice 和 Bob 就可以交换数据消息。

```
Alice                           Bob

SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
所有数据包都以混淆（加密）的报头开始。有两种报头类型：长报头和短报头。请注意，前13个字节（目标连接ID、数据包编号和类型）在所有报头中都是相同的。

```
Alice                           Bob

TokenRequest --------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
长报头为32字节。它在会话创建之前使用，用于令牌请求、SessionRequest、SessionCreated和重试。它也用于会话外的对等测试和打洞消息。

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
在头部加密之前：

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry containing a Termination block

or

TokenRequest --------------------->
<---------------------------  Retry containing a Termination block
```
短头部长度为 16 字节。它用于 Session Created 和 Data 消息。未经身份验证的消息（如 Session Request、Retry 和 Peer Test）将始终使用长头部。

```
XK(s, rs):           Authentication   Confidentiality
  <- s
  ...
  -> e, es                  0                2
  <- e, ee                  2                1
  -> s, se                  2                5
  <-                        2                5
```
需要16字节，因为接收方必须解密前16字节以获取消息类型，然后如果消息类型表明这实际上是一个长头部，则必须额外解密16字节。

### 数据包完整性

对于 Session Confirmed，在头部加密之前：

#### 头部绑定

有关 frag 字段的更多信息，请参见下面的会话确认分片部分。

对于数据消息，在头部加密之前：

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
#### 头部加密

连接ID必须随机生成。源ID和目标ID不得相同，这样路径上的攻击者就无法捕获数据包并将其发送回发起者，使其看起来有效。不要使用计数器来生成连接ID，这样路径上的攻击者就无法生成看起来有效的数据包。

与QUIC不同，我们不会在握手过程中或握手完成后更改连接ID，即使在Retry消息之后也不会更改。ID从第一条消息（Token Request或Session Request）到最后一条消息（带Termination的Data）始终保持不变。此外，连接ID在路径质询或连接迁移期间或之后也不会更改。

另外与QUIC不同的是，头部中的连接ID总是经过头部加密的。请参见下文。

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
如果握手过程中没有发送First Packet Number块，数据包在单个会话内编号，每个方向分别从0开始，最大到(2**32 -1)。必须在发送的数据包数量接近最大值之前终止会话并创建新会话。

如果在握手过程中发送了首个数据包编号块，则在该会话中，对于该方向的数据包将从该数据包编号开始进行编号。数据包编号可能在会话期间回绕。当发送的数据包数量达到最大值 2**32 时，数据包编号会回绕到首个数据包编号，此时该会话不再有效。必须在发送最大数量的数据包之前终止会话并创建新会话。

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
#### 头部加密 KDF

TODO 密钥轮换，减少最大数据包数量？

确定丢失的握手数据包将整体重传，包括数据包编号在内的相同头部。握手消息 Session Request、Session Created 和 Session Confirmed 必须使用相同的数据包编号和相同的加密内容进行重传，以便使用相同的链式哈希来加密响应。Retry 消息永远不会被传输。

被确定为丢失的数据阶段数据包从不进行整包重传（除了终止包，见下文）。这同样适用于丢失数据包中包含的数据块。相反，数据块中可能携带的信息会根据需要在新数据包中重新发送。数据包从不使用相同的数据包编号进行重传。任何数据包内容的重传（无论内容是否保持相同）都必须使用下一个未使用的数据包编号。

#### 头部验证

不允许使用相同的数据包编号原样重传未更改的完整数据包，原因有几个。背景信息请参见 QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) 第 12.3 节。

新数据包用于传输被确定已丢失的信息。通常情况下，当包含某信息的数据包被确定丢失时，该信息会被重新发送，而当包含该信息的数据包被确认收到时，发送就会停止。

例外：包含终止块的数据阶段数据包可以（但不是必须）完整地按原样重传。请参见下面的会话终止部分。

以下数据包包含一个被忽略的随机数据包编号：

对于 Alice，出站数据包编号从 Session Confirmed 开始为 0。对于 Bob，出站数据包编号从第一个 Data 数据包开始为 0，该数据包应该是对 Session Confirmed 的 ACK。在标准握手示例中，数据包编号如下：

任何握手消息（SessionRequest、SessionCreated 或 SessionConfirmed）的重传都必须保持不变地重发，使用相同的数据包编号。重传这些消息时不要使用不同的临时密钥或更改载荷。

- 存储数据包用于重传是低效的
- 新数据包对路径上的观察者来说看起来不同，无法判断这是重传的
- 新数据包会携带更新的确认块，而不是旧的确认块
- 你只重传必要的部分。某些片段可能已经被重传过一次并得到确认
- 如果有更多数据待发送，你可以在每个重传数据包中放入尽可能多的内容
- 为了检测重复而跟踪所有单个数据包的端点面临累积过多状态的风险。通过维护一个最小数据包编号来限制检测重复所需的数据，低于此编号的所有数据包都会被立即丢弃。
- 这种方案更加灵活

头部（在混淆和保护之前）始终包含在AEAD函数的关联数据中，以加密方式将头部绑定到数据。

Header 加密有几个目标。请参阅上面的"额外 DPI 讨论"部分了解背景和假设。

头部使用在网络数据库中发布的已知密钥或稍后计算的密钥进行加密。在握手阶段，这仅用于抗DPI（深度包检测）目的，因为密钥是公开的且密钥和随机数会被重复使用，所以这实际上只是混淆。请注意，头部加密还用于混淆临时密钥X（在Session Request中）和Y（在Session Created中）。

- 会话请求
- 会话已创建
- 令牌请求
- 重试
- 对等测试
- 打洞

请参见下面的入站数据包处理部分以获取更多指导。

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
所有头部的字节0-15都使用头部保护方案进行加密，通过与从已知密钥计算出的数据进行异或运算，使用ChaCha20，类似于QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001)和[Nonces](https://eprint.iacr.org/2019/624.pdf)。这确保了加密的短头部和长头部的第一部分看起来是随机的。

#### ChaCha20/Poly1305

对于 Session Request 和 Session Created，长头部的第16-31字节和32字节的 Noise 临时密钥使用 ChaCha20 加密。未加密的数据是随机的，因此加密后的数据看起来也是随机的。

#### 注意事项

对于重试包，长头部的第16-31字节使用ChaCha20加密。未加密的数据是随机的，因此加密后的数据看起来也是随机的。

- 防止在线DPI识别协议
- 防止同一连接中一系列消息的模式，握手重传除外
- 防止不同连接中相同类型消息的模式
- 在不知道netDb中介绍密钥的情况下，防止握手头部被解密
- 在不知道netDb中介绍密钥的情况下，防止X25519临时密钥被识别
- 防止任何在线或离线攻击者解密数据阶段数据包编号和类型
- 防止在不知道netDb中介绍密钥的情况下，路径上或路径外观察者注入有效的握手数据包
- 防止路径上或路径外观察者注入有效的数据包
- 允许对传入数据包进行快速高效分类
- 提供"探测"抗性，使得对错误的会话请求没有响应，或者如果有重试响应，在不知道netDb中介绍密钥的情况下，响应不能被识别为I2P
- 目标连接ID不是关键数据，如果知道netDb中介绍密钥的观察者能够解密它是可以接受的
- 数据阶段数据包的数据包编号是AEAD随机数，属于关键数据。即使观察者知道netDb中的介绍密钥，也不能解密它。参见[Nonces](https://eprint.iacr.org/2019/624.pdf)。

与 QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) 头部保护方案不同，所有头部的所有部分，包括目标和源连接 ID，都被加密。QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) 和 [Nonces](https://eprint.iacr.org/2019/624.pdf) 主要专注于加密头部的"关键"部分，即包号（ChaCha20 随机数）。虽然加密会话 ID 会使传入包分类稍微复杂一些，但它使某些攻击变得更加困难。QUIC 为不同阶段定义了不同的连接 ID，用于路径挑战和连接迁移。而在这里，由于连接 ID 被加密，我们在整个过程中使用相同的连接 ID。

有七个头部保护密钥阶段：

Header encryption 旨在允许快速分类入站数据包，无需复杂的启发式算法或回退机制。这是通过对几乎所有入站消息使用相同的 k_header_1 密钥来实现的。即使当连接的源 IP 或端口由于实际 IP 变化或 NAT 行为而改变时，数据包也可以通过连接 ID 的单次查找快速映射到会话。

请注意，Session Created 和 Retry 是唯一需要对 k_header_1 进行回退处理以解密 Connection ID 的消息，因为它们使用发送方（Bob）的 intro key。所有其他消息都使用接收方的 intro key 来处理 k_header_1。回退处理只需要通过源 IP/端口查找待处理的出站连接。

如果基于源IP/端口的回退处理未能找到待处理的出站连接，可能有几种原因：

虽然可以进行额外的后备处理来尝试找到待处理的出站连接并使用该连接的 k_header_1 来解密连接 ID，但这可能并非必要。如果 Bob 的 NAT 或数据包路由出现问题，最好让连接失败。此设计依赖于端点在握手期间保持稳定的地址。

请参阅下面的入站数据包处理部分以获取更多指导原则。

- 会话请求和令牌请求
- 会话已创建
- 重试
- 会话已确认
- 数据阶段
- 对等测试
- 打洞

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
请参阅下面各个KDF部分，了解该阶段标头加密密钥的推导。

这个KDF使用数据包的最后24字节作为两个ChaCha20操作的IV。由于所有数据包都以16字节MAC结尾，这要求所有数据包载荷最少为8字节。这个要求在下面的消息部分中也有额外说明。

在解密报头的前8个字节后，接收方将知道目标连接ID。从那时起，接收方根据会话的密钥阶段知道对报头其余部分使用什么报头加密密钥。

- 不是 SSU2 消息
- 损坏的 SSU2 消息
- 回复被攻击者伪造或修改
- Bob 有对称 NAT
- Bob 在处理消息期间更改了 IP 或端口
- Bob 通过不同的接口发送回复

解密头部的下8个字节将揭示消息类型，并能够确定这是短头部还是长头部。如果是长头部，接收方必须验证版本和netid字段。如果版本不等于2，或者netid不等于期望值（通常为2，测试网络除外），接收方应该丢弃该消息。

所有消息包含三个或四个部分：

在所有情况下，头部（如果存在的话，还包括临时密钥）都与认证MAC绑定，以确保整个消息的完整性。

#### AEAD 错误处理

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
入站数据包处理程序必须始终解密ChaCha20负载并在处理消息之前验证MAC，但有一个例外：为了缓解来自地址欺骗数据包的DoS攻击（这些数据包包含带有无效token的明显Session Request消息），处理程序无需尝试解密和验证完整消息（除了ChaCha20/Poly1305解密之外还需要昂贵的DH操作）。处理程序可以使用在Session Request消息头部中找到的值来响应Retry消息。

#### 初始 ChainKey 的 KDF

有三个独立的认证加密实例（CipherStates）。一个在握手阶段，两个（传输和接收）在数据阶段。每个实例都有自己从 KDF 派生的密钥。

加密/认证数据将表示为

### 认证加密

加密和认证的数据格式。

- 消息头
- 仅用于会话请求和会话创建，一个临时密钥
- ChaCha20加密的载荷
- Poly1305 MAC

加密/解密函数的输入：

- 对于握手消息 Session Request、Session Created 和 Session Confirmed，消息头在 Noise 处理阶段之前进行 mixHash() 操作
- 临时密钥（如果存在）由标准的 Noise misHash() 覆盖
- 对于 Noise 握手之外的消息，消息头用作 ChaCha20/Poly1305 加密的关联数据

加密函数的输出，解密函数的输入：

### 会话请求的 KDF

对于 ChaCha20，这里描述的内容对应于 [RFC-7539](https://tools.ietf.org/html/rfc7539)，在 TLS [RFC-7905](https://tools.ietf.org/html/rfc7905) 中也有类似的使用。

密钥派生函数(KDF)使用HMAC-SHA256(key, data)从DH结果生成握手阶段的加密密钥k，该函数定义在[RFC-2104](https://tools.ietf.org/html/rfc2104)中。这些是InitializeSymmetric()、MixHash()和MixKey()函数，完全按照Noise规范中的定义。

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   Encrypted and authenticated data    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
```
#### 会话请求的密钥派生函数

Alice发送给Bob，可以是握手中的第一条消息，也可以是对Retry消息的响应。Bob用Session Created消息回应。大小：80 + 载荷大小。最小大小：88

如果 Alice 没有有效的令牌，Alice 应该发送令牌请求消息而不是会话请求消息，以避免生成会话请求时非对称加密的开销。

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
长头部。Noise 内容：Alice 的临时密钥 X Noise 载荷：DateTime 和其他块 最大载荷大小：MTU - 108 (IPv4) 或 MTU - 128 (IPv6)。对于 1280 MTU：最大载荷为 1172 (IPv4) 或 1152 (IPv6)。对于 1500 MTU：最大载荷为 1392 (IPv4) 或 1372 (IPv6)。

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
负载安全属性：

#### 载荷

- 由于 ChaCha20 是流密码，明文无需填充。多余的密钥流字节将被丢弃。
- 密码的密钥（256位）通过 SHA256 KDF 协商确定。每个消息的 KDF 详细信息在下面的单独章节中说明。

#### 注释

- 在所有消息中，AEAD 消息大小是预先已知的。在 AEAD 认证失败时，接收方必须停止进一步的消息处理并丢弃该消息。
- Bob 应该维护一个重复失败的 IP 黑名单。

### SessionRequest（类型 0）

X 值经过加密以确保载荷的不可区分性和唯一性，这些是必要的 DPI 对抗措施。我们使用 ChaCha20 加密来实现这一点，而不是使用更复杂和更慢的替代方案，如 elligator2。使用 Bob 的 router 公钥进行非对称加密会太慢。ChaCha20 加密使用 Bob 在 netDb 中发布的 intro 密钥。

#### 载荷

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
#### 注释

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
### 用于 Session Created 和 Session Confirmed 第一部分的 KDF

ChaCha20 加密仅用于抵抗 DPI（深度包检测）。任何知道 Bob 的介绍密钥的一方（该密钥发布在网络数据库中）都可以解密此消息中的头部和 X 值。

原始内容：

未加密数据（未显示 Poly1305 认证标签）：

最小载荷大小为8字节。由于DateTime块只有7字节，因此必须至少存在另一个块。

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
Bob 发送给 Alice，作为对 Session Request 消息的响应。Alice 用 Session Confirmed 消息回应。大小：80 + 负载大小。最小大小：88

Noise 内容：Bob 的临时密钥 Y Noise 载荷：DateTime、Address 和其他块 最大载荷大小：MTU - 108 (IPv4) 或 MTU - 128 (IPv6)。对于 1280 MTU：最大载荷为 1172 (IPv4) 或 1152 (IPv6)。对于 1500 MTU：最大载荷为 1392 (IPv4) 或 1372 (IPv6)。

载荷安全属性：

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
Y 值被加密以确保载荷的不可区分性和唯一性，这些是必要的 DPI 对抗措施。我们使用 ChaCha20 加密来实现这一点，而不是使用更复杂和更慢的替代方案，如 elligator2。使用 Alice router 公钥的非对称加密会太慢。ChaCha20 加密使用 Bob 的介绍密钥，该密钥发布在 netDb 中。

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
#### 问题

- DateTime 块
- Options 块（可选）
- Relay Tag Request 块（可选）
- Padding 块（可选）

ChaCha20 加密仅用于抵抗 DPI（深度包检测）。任何知道 Bob 的 intro key（发布在网络数据库中）并捕获了 Session Request 前 32 字节的一方，都可以解密此消息中的 Y 值。

#### 载荷

- 初始 ChaCha20 块中的唯一 X 值确保每个会话的密文都不相同。
- 为了提供探测抗性，Bob 不应该对 Session Request 消息发送 Retry 消息，除非 Session Request 消息中的消息类型、协议版本和网络 ID 字段都有效。
- Bob 必须拒绝时间戳值与当前时间相差过远的连接。将最大时间差称为"D"。Bob 必须维护一个之前使用过的握手值的本地缓存并拒绝重复值，以防止重放攻击。缓存中的值必须至少有 2*D 的生存期。缓存值是实现相关的，但可以使用 32 字节的 X 值（或其加密等价物）。通过发送包含零令牌和终止块的 Retry 消息来拒绝。
- Diffie-Hellman 临时密钥绝不能重复使用，以防止加密攻击，重复使用将被作为重放攻击拒绝。
- "KE" 和 "auth" 选项必须兼容，即共享密钥 K 必须具有适当的大小。如果添加更多 "auth" 选项，这可能会隐式地改变 "KE" 标志的含义，以使用不同的 KDF 或不同的截断大小。
- Bob 必须验证 Alice 的临时密钥是曲线上的有效点。
- 填充应该限制在合理的数量内。Bob 可以拒绝具有过度填充的连接。Bob 将在 Session Created 中指定他的填充选项。最小/最大指导方针待定。从 0 到 31 字节的随机大小最少？（分布待确定，见附录 A。）
- 在大多数错误情况下，包括 AEAD、DH、明显的重放或密钥验证失败，Bob 应该停止进一步的消息处理并丢弃消息而不响应。
- 如果 DateTime 块中的时间戳偏差过大，Bob 可以发送包含零令牌和带有时钟偏差原因代码的 Termination 块的 Retry 消息。
- DoS 缓解：DH 是一个相对昂贵的操作。与之前的 NTCP 协议一样，router 应该采取所有必要措施防止 CPU 或连接耗尽。对最大活跃连接数和正在进行的最大连接设置数设置限制。强制执行读取超时（每次读取和"slowloris"的总超时）。限制来自同一源的重复或同时连接。为重复失败的源维护黑名单。不响应 AEAD 失败。或者，在 DH 操作和 AEAD 验证之前用 Retry 消息响应。
- "ver" 字段：整体的 Noise 协议、扩展和包括有效载荷规范在内的 SSU2 协议，表示 SSU2。此字段可用于表示对未来变更的支持。
- 网络 ID 字段用于快速识别跨网络连接。如果此字段与 Bob 的网络 ID 不匹配，Bob 应该断开连接并阻止未来的连接。
- 如果源连接 ID 等于目标连接 ID，Bob 必须丢弃该消息。

### SessionCreated (类型 1)

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
### 会话确认第1部分的密钥派生函数，使用会话创建的密钥派生函数

原始内容：

未加密数据（Poly1305 认证标签未显示）：

最小载荷大小为8字节。由于DateTime和Address块的总大小超过了这个要求，仅有这两个块就能满足要求。

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
Alice 发送给 Bob，作为对 Session Created 消息的响应。Bob 立即回应一个包含 ACK 块的 Data 消息。大小：80 + 载荷大小。最小大小：约 500 字节（最小 router info 块大小约为 420 字节）

Noise 内容：Alice 的静态密钥 Noise 载荷部分 1：无 Noise 载荷部分 2：Alice 的 RouterInfo 和其他块 最大载荷大小：MTU - 108 (IPv4) 或 MTU - 128 (IPv6)。对于 1280 MTU：最大载荷为 1172 (IPv4) 或 1152 (IPv6)。对于 1500 MTU：最大载荷为 1392 (IPv4) 或 1372 (IPv6)。

负载安全属性：

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
这包含两个 ChaChaPoly 帧。第一个是 Alice 的加密静态公钥。第二个是 Noise 负载：Alice 的加密 RouterInfo、可选选项和可选填充。它们使用不同的密钥，因为在两者之间调用了 MixKey() 函数。

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
#### 注意事项

- DateTime 块
- Address 块
- Relay Tag 块（可选）
- New Token 块（不推荐，见注释）
- First Packet Number 块（可选）
- Options 块（可选）
- Termination 块（不推荐，应在重试消息中发送）
- Padding 块（可选）

原始内容：

#### 会话确认分片

- Alice 必须在此验证 Bob 的临时密钥是曲线上的有效点。
- 填充应限制在合理范围内。Alice 可以拒绝填充过多的连接。Alice 将在 Session Confirmed 中指定她的填充选项。最小/最大指导原则待定。最小随机大小从 0 到 31 字节？（分布待确定，见附录 A。）
- 在任何错误（包括 AEAD、DH、时间戳、明显重放或密钥验证失败）时，Alice 必须停止进一步的消息处理并关闭连接，不作响应。
- Alice 必须拒绝时间戳值与当前时间相差过大的连接。将最大时间差称为"D"。Alice 必须维护一个之前使用过的握手值的本地缓存并拒绝重复值，以防止重放攻击。缓存中的值必须至少有 2*D 的生存期。缓存值取决于实现，但可以使用 32 字节的 Y 值（或其加密等效值）。
- 如果源 IP 和端口与 Session Request 的目标 IP 和端口不匹配，Alice 必须丢弃该消息。
- 如果目标和源连接 ID 与 Session Request 的源和目标连接 ID 不匹配，Alice 必须丢弃该消息。
- 如果 Alice 在 Session Request 中请求，Bob 发送一个中继标签块。
- 不建议在 Session Created 中使用 New Token 块，因为 Bob 应该首先验证 Session Confirmed。请参见下面的 Tokens 部分。

#### 注意事项

- 在这里包含最小/最大填充选项？

### 会话确认第2部分的KDF

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
### SessionConfirmed（类型 2）

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
### 数据阶段的 KDF

未加密数据（未显示 Poly1305 认证标签）：

最小载荷大小为8字节。由于RouterInfo块远大于这个要求，仅仅该块就能满足要求。

1)  Alice的Router Info块（必需）   2)  选项块（可选）   3)  I2NP块（可选）

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
4\) 填充块（可选）此帧绝不能包含任何其他块类型。TODO：relay 和 peer test 如何处理？

Session Confirmed 消息必须包含来自 Alice 的完整签名 Router Info，以便 Bob 可以执行几项必要的检查：

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
不幸的是，router Info 即使在 RI 块中进行 gzip 压缩后，仍可能超过 MTU。因此，Session Confirmed 可能会被分片到两个或更多数据包中。这是 SSU2 协议中唯一一种 AEAD 保护的载荷被分片到两个或更多数据包的情况。

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
#### 注释

- RouterInfo 块（必须是第一个块）
- Options 块（可选）
- New Token 块（可选）
- Relay Request 块（可选）
- Peer Test 块（可选）
- First Packet Number 块（可选）
- I2NP、First Fragment 或 Follow-on Fragment 块（可选，但可能没有空间）
- Padding 块（可选）

每个数据包的头部构造如下：

#### 负载

- Bob必须执行通常的Router Info验证。确保签名类型受支持，验证签名，验证时间戳在范围内，以及任何其他必要的检查。有关处理分片Router Info的说明，请参见下文。

- Bob必须验证在第一帧中收到的Alice静态密钥与Router Info中的静态密钥匹配。Bob必须首先在Router Info中搜索具有匹配版本(v)选项的NTCP或SSU2 Router地址。请参见下面的已发布Router Info和未发布Router Info部分。有关处理分片Router Info的注意事项，请参见下文。

- 如果Bob在他的netDb中有Alice的RouterInfo的较旧版本，请验证router info中的静态密钥在两个版本中是否相同（如果存在），以及较旧版本是否少于XXX时间（参见下面的密钥轮换时间）

- Bob 必须在此验证 Alice 的静态密钥是曲线上的有效点。

- 应包含选项，以指定填充参数。

- 在任何错误情况下，包括 AEAD、RI、DH、时间戳或密钥验证失败，Bob 必须停止进一步的消息处理并关闭连接，不做任何响应。

- 消息3第2部分帧内容：此帧的格式与数据阶段帧的格式相同，除了帧的长度由Alice在会话请求中发送。数据阶段帧格式见下文。该帧必须按以下顺序包含1到4个块：

按如下方式构造数据包序列：

重组过程：

- 建议使用消息3第2部分填充块。

- 根据 MTU 和 Router Info 大小，可能没有空间或只有很小的空间可用于 I2NP 块。如果 Router Info 被分片，请不要包含 I2NP 块。最简单的实现可能是永远不在 Session Confirmed 消息中包含 I2NP 块，而是在后续的 Data 消息中发送所有 I2NP 块。关于最大块大小，请参见下面的 Router Info 块部分。

#### 有效载荷

当 Bob 收到任何 Session Confirmed 消息时，他解密消息头，检查 frag 字段，并确定 Session Confirmed 消息是分片的。在收到并重新组装所有分片之前，他不会（也不能）解密消息。

- RI 中的静态密钥 "s" 与握手中的静态密钥匹配
- RI 中的介绍密钥 "i" 必须被提取且有效，以便在数据阶段使用
- RI 签名有效

Bob没有机制来确认单个片段。当Bob接收到所有片段、重新组装、解密并验证内容后，Bob像往常一样执行split()，进入数据阶段，并发送数据包编号0的ACK。

如果 Alice 没有收到数据包编号 0 的 ACK，她必须原样重传所有会话确认数据包。

- 所有头部都是具有相同数据包编号0的短头部
- 所有头部都包含一个"frag"字段，包含片段编号和片段总数
- 片段0的未加密头部是"jumbo"消息的关联数据（AD）
- 每个头部都使用该数据包中最后24字节的数据进行加密

示例：

- 创建单个 RI 区块（在 RI 区块片段字段中为片段 0/1）。我们不使用 RI 区块分片，那是解决同一问题的替代方法。
- 创建包含 RI 区块和任何其他要包含的区块的"jumbo"负载
- 计算总数据大小（不包括头部），即负载大小 + 64 字节用于静态密钥和两个 MAC
- 计算每个数据包中的可用空间，即 MTU 减去 IP 头部（20 或 40），减去 UDP 头部（8），减去 SSU2 短头部（16）。每个数据包的总开销为 44（IPv4）或 64（IPv6）。
- 计算数据包数量。
- 计算最后一个数据包中的数据大小。必须大于或等于 24 字节，以便头部加密能够工作。如果太小，要么添加填充区块，要么增加已存在的填充区块的大小，要么减少其他数据包中某一个的大小，使最后一个数据包足够大。
- 为第一个数据包创建未加密的头部，在片段字段中包含总片段数，并像往常一样使用 Noise 加密"jumbo"负载，将头部作为 AD。
- 将加密的 jumbo 数据包分割成片段
- 为每个片段 1-n 添加未加密的头部
- 加密每个片段 0-n 的头部。每个头部使用上述 Session Confirmed KDF 中定义的相同 k_header_1 和 k_header_2。
- 传输所有片段

对于IPv6上的1500 MTU，最大载荷为1372字节，RI块开销为5字节，最大（gzip压缩）RI数据大小为1367字节（假设没有其他块）。使用两个数据包时，第二个数据包的开销为64字节，因此可以容纳另外1436字节的载荷。所以两个数据包足以容纳最大2803字节的压缩RI。

当前网络中看到的最大压缩 RI 大小约为 1400 字节；因此在实际情况下，即使在最小 1280 MTU 的情况下，两个片段应该就足够了。协议允许最多 15 个片段。

- 保留片段 0 的头部，因为它用作 Noise AD
- 在重组前丢弃其他片段的头部
- 重组"jumbo"载荷，使用片段 0 的头部作为 AD，并用 Noise 解密
- 照常验证 RI 块
- 进入数据阶段并发送 ACK 0，照常进行

安全性分析：

分片Session Confirmed的完整性和安全性与未分片的相同。对任何分片的任何修改都会导致重新组装后Noise AEAD失败。除了分片0之外的分片头部仅用于标识分片。即使路径上的攻击者拥有用于加密头部的k_header_2密钥（不太可能，从握手中派生），这也不允许攻击者替换有效的分片。

数据阶段使用头部作为关联数据。

KDF 从链接密钥 ck 生成两个密码密钥 k_ab 和 k_ba，使用 [RFC-2104](https://tools.ietf.org/html/rfc2104) 中定义的 HMAC-SHA256(key, data)。这是 split() 函数，与 Noise 规范中定义的完全一致。

Noise 负载：允许所有区块类型 最大负载大小：MTU - 60（IPv4）或 MTU - 80（IPv6）。对于 1500 MTU：最大负载为 1440（IPv4）或 1420（IPv6）。

从Session Confirmed的第2部分开始，所有消息都在经过身份验证和加密的ChaChaPoly载荷内。所有填充都在消息内部。载荷内部是包含零个或多个"块"的标准格式。每个块都有一个字节的类型和两个字节的长度。类型包括日期/时间、I2NP消息、选项、终止和填充。

注意：Bob 可以（但不是必须的）在数据阶段向 Alice 发送的第一条消息中包含他的 RouterInfo。

### 数据消息（类型 6）

载荷安全属性：

未加密数据（未显示 Poly1305 认证标签）：

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
### 用于对等测试的KDF

Charlie 发送给 Alice，Alice 发送给 Charlie，仅适用于 Peer Test 阶段 5-7。Peer Test 阶段 1-4 必须在会话中使用 Data 消息中的 Peer Test 块发送。更多信息请参见下面的 Peer Test 块和 Peer Test 过程部分。

大小：48 + 载荷大小。

Noise 载荷：见下文。

原始内容：

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
#### 注释

- router必须丢弃出现AEAD错误的消息。

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
未加密数据（未显示 Poly1305 认证标签）：

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
#### 负载

- 最小负载大小为8字节。任何ACK、I2NP、First Fragment或Follow-on Fragment块都能满足此要求。如果不满足要求，必须包含一个Padding块。
- 每个数据包编号只能使用一次。重传I2NP消息或片段时，必须使用新的数据包编号。

### 对等测试 (类型 7)

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
### 重试的密钥派生函数

最小载荷大小为 8 字节。由于 Peer Test 块的总大小超过了这个要求，仅使用该块就能满足要求。

在消息 5 和 7 中，Peer Test 块可能与会话内消息 3 和 4 中的块相同，包含由 Charlie 签名的协议，或者可能重新生成。签名是可选的。

在消息6中，Peer Test块可能与会话内消息1和2中的块相同，包含由Alice签名的请求，或者可能重新生成。签名是可选的。

连接ID：两个连接ID都从测试nonce中派生。对于从Charlie发送给Alice的消息5和7，目标连接ID是4字节大端序测试nonce的两个副本，即((nonce << 32) | nonce)。源连接ID是目标连接ID的反码，即~((nonce << 32) | nonce)。对于从Alice发送给Charlie的消息6，交换这两个连接ID。

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
地址块内容：

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
#### 注释

- DateTime 块
- Address 块（消息 6 和 7 需要，见下文注释）
- Peer Test 块
- Padding 块（可选）

Retry 消息的要求是 Bob 不需要解密 Session Request 消息就能生成 Retry 消息作为响应。同时，这个消息必须能够快速生成，仅使用对称加密。

Bob 向 Alice 发送，作为对 Session Request 或 Token Request 消息的响应。Alice 用新的 Session Request 进行回应。大小：48 + 载荷大小。

如果包含终止块，也可作为终止消息（即"不要重试"）。

Noise 载荷：见下文。

原始内容：

- 在消息 5 中：不需要。
- 在消息 6 中：从 Charlie 的 RI 中选择的 Charlie 的 IP 和端口。
- 在消息 7 中：接收消息 6 的 Alice 的实际 IP 和端口。

### 重试 (类型 9)

未加密数据（未显示 Poly1305 认证标签）：

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
### Token 请求的 KDF

最小载荷大小为8字节。由于DateTime和Address块的总大小已超过该要求，仅凭这两个块就能满足要求。

此消息必须快速生成，仅使用对称加密。

Alice 发送给 Bob。Bob 用 Retry 消息响应。大小：48 + 载荷大小。

如果 Alice 没有有效的令牌，Alice 应该发送此消息而不是会话请求，以避免生成会话请求时的非对称加密开销。

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
Noise 载荷：见下文。

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
#### 有效载荷

- DateTime 块
- Address 块
- Options 块（可选）
- Termination 块（可选，如果会话被拒绝）
- Padding 块（可选）

原始内容：

#### 日期时间

- 为了提供探测抗性，router 不应该发送 Retry 消息来响应 Session Request 或 Token Request 消息，除非请求消息中的消息类型、协议版本和网络 ID 字段是有效的。
- 为了限制使用伪造源地址发起的任何放大攻击的规模，Retry 消息不得包含大量填充。建议 Retry 消息的大小不超过其响应消息大小的三倍。或者，使用简单的方法，例如添加 1-64 字节范围内的随机填充量。

### 令牌请求（类型 10）

未加密数据（未显示 Poly1305 认证标签）：

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
### Hole Punch 的 KDF

最小负载大小为 8 字节。

此消息必须快速生成，仅使用对称加密。

Charlie 发送给 Alice，作为对从 Bob 收到的 Relay Intro 的响应。Alice 用新的 Session Request 进行回应。大小：48 + 负载大小。

Noise 载荷：见下文。

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
原始内容：

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
#### 选项

- DateTime 块
- Padding 块

未加密数据（未显示 Poly1305 认证标签）：

#### RouterInfo

- 为了提供探测抗性，router 不应该响应 Token Request 消息发送 Retry 消息，除非 Token Request 消息中的消息类型、协议版本和网络 ID 字段都是有效的。
- 这不是标准的 Noise 消息，也不是握手的一部分。除了通过连接 ID，它与 Session Request 消息没有绑定关系。
- 在大多数错误情况下，包括 AEAD 错误或明显的重放攻击，Bob 应该停止进一步的消息处理并丢弃消息而不响应。
- Bob 必须拒绝时间戳值与当前时间偏差过大的连接。将最大时间差称为"D"。Bob 必须维护一个本地缓存来存储之前使用过的握手值并拒绝重复值，以防止重放攻击。缓存中的值必须至少有 2*D 的生存期。缓存值依赖于实现，不过可以使用 32 字节的 X 值（或其加密等价物）。
- 如果 DateTime 块中的时间戳偏差过大，Bob 可以发送包含零 token 和带有时钟偏差原因码的 Termination 块的 Retry 消息。
- 最小大小：待定，与 Session Created 相同的规则？

### 打洞 (类型 11)

最小载荷大小为8字节。由于DateTime和Address块的总和超过了这个要求，仅凭这两个块就能满足要求。

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
### 载荷格式

连接ID：两个连接ID都从中继随机数派生而来。目标连接ID是4字节大端序中继随机数的两个副本，即 ((nonce << 32) | nonce)。源连接ID是目标连接ID的反码，即 ~((nonce << 32) | nonce)。

Alice 应该忽略头部中的令牌。要在 Session Request 中使用的令牌位于 Relay Response 块中。

每个 Noise 载荷包含零个或多个"块"。

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
这使用与 [NTCP2](/docs/specs/ntcp2) 和 [ECIES](/docs/specs/ecies) 规范中定义的相同块格式。各个块类型的定义有所不同。在 QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) 中的等效术语是"帧"。

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
#### I2NP 消息

- DateTime 块
- Address 块
- Relay Response 块
- Padding 块（可选）

有人担心鼓励实现者共享代码可能会导致解析问题。实现者应该仔细考虑共享代码的好处和风险，并确保在两种上下文中排序和有效块规则是不同的。

加密载荷中有一个或多个块。块是简单的标签-长度-值（TLV）格式。每个块包含一个字节的标识符、两个字节的长度和零个或多个字节的数据。这种格式与 [NTCP2](/docs/specs/ntcp2) 和 [ECIES](/docs/specs/ecies) 中的格式相同，但是块定义是不同的。

为了可扩展性，接收方必须忽略具有未知标识符的块，并将它们视为填充。

## Noise 载荷

（未显示 Poly1305 认证标签）：

头部加密使用数据包的最后 24 字节作为两个 ChaCha20 操作的 IV。由于所有数据包都以 16 字节 MAC 结尾，这要求所有数据包载荷最少为 8 字节。如果载荷本身不满足此要求，则必须包含一个填充块。

最大 ChaChaPoly 负载根据消息类型、MTU 和 IPv4 或 IPv6 地址类型而变化。最大负载为 MTU - 60（IPv4）和 MTU - 80（IPv6）。最大负载数据为 MTU - 63（IPv4）和 MTU - 83（IPv6）。上限约为 1440 字节（IPv4，1500 MTU，Data 消息）。最大总块大小为最大负载大小。最大单块大小为最大总块大小。块类型为 1 字节。块长度为 2 字节。最大单块数据大小为最大单块大小减去 3。

### 区块排序规则

注意事项：

区块类型：

在 Session Confirmed 中，Router Info 必须是第一个块。

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
在所有其他消息中，顺序是未指定的，除了以下要求：如果存在填充（Padding），必须是最后一个块。如果存在终止（Termination），必须是除填充之外的最后一个块。单个载荷中不允许有多个填充块。

用于时间同步：

注意：

- 实现者必须确保在读取块时，格式错误或恶意数据不会导致读取越界到下一个块或超出有效载荷边界。
- 实现应该忽略未知的块类型以保持向前兼容性。

传递更新的选项。选项包括：最小和最大填充。

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
### 区块规范

Options 块的长度是可变的。

选项问题：

### 会话请求

#### 第一个片段

将Alice的RouterInfo传递给Bob。仅用于Session Confirmed第2部分的载荷中。不应在数据阶段使用；应使用I2NP DatabaseStore消息代替。

```
+----+----+----+----+----+----+----+
| 0  |    4    |     timestamp     |
+----+----+----+----+----+----+----+

blk :: 0
size :: 2 bytes, big endian, value = 4
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
```
最小大小：约 420 字节，除非 router info 中的 router identity 和签名是可压缩的，但这种情况不太可能发生。

- 与 SSU 1 不同，SSU 2 在数据阶段的数据包头部没有时间戳。
- 实现应该定期在数据阶段发送 DateTime 块。
- 实现必须四舍五入到最近的秒，以防止网络中的时钟偏差。

#### 后续片段

注意：Router Info 块永远不会被分片。frag 字段始终为 0/1。有关更多信息，请参见上面的 Session Confirmed 分片部分。

注意事项：

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
一个带有修改头部的完整 I2NP 消息。

- 选项协商待定。

#### 终止

这使用与 [NTCP2](/docs/specs/ntcp2) 中相同的 9 字节 I2NP 头部（类型、消息 ID、短期到期时间）。

注意事项：

带有修改头部的 I2NP 消息的第一个片段（片段 #0）。

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
这使用与 [NTCP2](/docs/specs/ntcp2) 相同的 9 字节作为 I2NP 头部（类型、消息 ID、短期过期时间）。

- Router Info 可选择使用 gzip 压缩，由标志位 1 表示。这与 NTCP2 不同（从不压缩），也与 DatabaseStore 消息不同（总是压缩）。压缩是可选的，因为对于内容较少、可压缩内容较少的小型 Router Info，压缩通常收益不大，但对于具有多个可压缩 Router Address 的大型 Router Info 则非常有益。如果压缩能够让 Router Info 在单个 Session Confirmed 数据包中传输而无需分片，则建议使用压缩。
- Session Confirmed 消息中第一个或唯一分片的最大大小：IPv4 为 MTU - 113 或 IPv6 为 MTU - 133。假设默认 MTU 为 1500 字节，且消息中没有其他块，IPv4 为 1387 或 IPv6 为 1367。当前 97% 的 router info 在不使用 gzip 压缩时小于 1367。当前 99.9% 的 router info 在使用 gzip 压缩时小于 1367。假设最小 MTU 为 1280 字节，且消息中没有其他块，IPv4 为 1167 或 IPv6 为 1147。当前 94% 的 router info 在不使用 gzip 压缩时小于 1147。当前 97% 的 router info 在使用 gzip 压缩时小于 1147。
- frag 字节现在未使用，Router Info 块从不分片。frag 字节必须设置为分片 0，总分片数 1。更多信息请参见上面的 Session Confirmed 分片部分。
- 除非 RouterInfo 中有已发布的 RouterAddress，否则不得请求泛洪。接收 router 只有在 RouterInfo 中包含已发布的 RouterAddress 时才能泛洪该 RouterInfo。
- 此协议不提供 RouterInfo 已存储或泛洪的确认。如果需要确认，且接收方是 floodfill，发送方应改为发送带有回复令牌的标准 I2NP DatabaseStoreMessage。

#### RelayRequest

未指定碎片总数。

注意：

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
I2NP 消息的附加片段（片段编号大于零）。

- 这与 NTCP2 中使用的 9 字节 I2NP 头部格式相同。
- 这与第一个分片块的格式完全相同，但块类型表明这是一个完整的消息。
- 包括 9 字节 I2NP 头部在内的最大大小为 IPv4 的 MTU - 63 和 IPv6 的 MTU - 83。

#### RelayResponse

注意事项：

断开连接。这必须是负载中最后一个非填充块。

注意事项：

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
在会话中通过数据消息从 Alice 发送到 Bob。请参见下面的中继处理部分。

- 这与 NTCP2 中使用的 9 字节 I2NP 头部格式相同。
- 这与 I2NP 消息块的格式完全相同，但块类型表示这是消息的第一个分片。
- 部分消息长度必须大于零。
- 与 SSU 1 中一样，建议首先发送最后一个分片，这样接收方就能知道分片总数并可以高效地分配接收缓冲区。
- 包括 9 字节 I2NP 头部在内的最大大小对于 IPv4 是 MTU - 63，对于 IPv6 是 MTU - 83。

#### RelayIntro

注意：

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
签名：

- 部分消息长度必须大于零。
- 与 SSU 1 中一样，建议先发送最后一个片段，这样接收方就知道片段的总数，可以有效地分配接收缓冲区。
- 与 SSU 1 中一样，最大片段编号是 127，但实际限制是 63 或更少。实现可能会将最大值限制为对于约 64 KB 的最大 I2NP 消息大小实际可行的值，在 1280 最小 MTU 下约为 55 个片段。请参见下面的最大 I2NP 消息大小部分。
- 最大部分消息大小（不包括片段和消息 id）对于 IPv4 是 MTU - 68，对于 IPv6 是 MTU - 88。

#### PeerTest

Alice 签名该请求并将其包含在此块中；Bob 在 Relay Intro 块中将其转发给 Charlie。签名算法：使用 Alice 的 router 签名密钥对以下数据进行签名：

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
在会话中通过数据消息发送，从 Charlie 到 Bob 或从 Bob 到 Alice，并且在从 Charlie 到 Alice 的打洞消息中发送。请参见下面的中继过程部分。

- 并非所有原因都可能实际使用，这取决于实现。大多数失败通常会导致消息被丢弃，而不是终止连接。请参阅上述握手消息部分的注释。列出的其他原因是为了一致性、日志记录、调试或政策变更。
- 建议在终止块中包含一个 ACK 块。
- 在数据阶段，对于除"收到终止"之外的任何原因，对等节点应该响应一个原因为"收到终止"的终止块。

#### NextNonce

注意事项：

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
该令牌必须立即由Alice在会话请求中使用。

- IP地址始终包含在内（与SSU 1不同），可能与用于会话的IP不同。

签名：

如果Charlie同意（响应代码0）或拒绝（响应代码64或更高），Charlie对响应进行签名并将其包含在此块中；Bob在中继响应块中将其转发给Alice。签名算法：使用Charlie的router签名密钥对以下数据进行签名：

- prologue: 16 字节 "RelayRequestData"，非空终止（不包含在消息中）
- bhash: Bob 的 32 字节 router 哈希（不包含在消息中）
- chash: Charlie 的 32 字节 router 哈希（不包含在消息中）
- nonce: 4 字节随机数
- relay tag: 4 字节中继标签
- timestamp: 4 字节时间戳（秒）
- ver: 1 字节 SSU 版本
- asz: 1 字节端点（端口 + IP）大小（6 或 18）
- AlicePort: 2 字节 Alice 的端口号
- Alice IP: (asz - 2) 字节 Alice IP 地址

#### 确认

如果 Bob 拒绝（响应代码 1-63），Bob 对响应进行签名并将其包含在此块中。签名算法：使用 Bob 的 router 签名密钥对以下数据进行签名：

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
在会话中通过Data消息发送，从Bob到Charlie。请参见下面的中继过程部分。

必须在前面有一个 RouterInfo 块，或包含 Alice 的 Router Info 的 I2NP DatabaseStore 消息块（或片段），要么在同一个载荷中（如果有空间），要么在之前的消息中。

注意事项：

签名：

- prologue: 16 字节 "RelayAgreementOK"，非空终止（不包含在消息中）
- bhash: Bob 的 32 字节 router 哈希值（不包含在消息中）
- nonce: 4 字节随机数
- timestamp: 4 字节时间戳（秒）
- ver: 1 字节 SSU 版本
- csz: 1 字节端点（端口 + IP）大小（0 或 6 或 18）
- CharliePort: 2 字节 Charlie 的端口号（如果 csz 为 0 则不存在）
- Charlie IP: (csz - 2) 字节 Charlie IP 地址（如果 csz 为 0 则不存在）

Alice 对请求进行签名，Bob 将其转发到这个区块中给 Charlie。验证算法：使用 Alice 的 router 签名密钥验证以下数据：

- prologue: 16 字节 "RelayAgreementOK"，非空终止（不包含在消息中）
- bhash: Bob 的 32 字节 router 哈希（不包含在消息中）
- nonce: 4 字节随机数
- timestamp: 4 字节时间戳（秒）
- ver: 1 字节 SSU 版本
- csz: 1 字节 = 0

#### 地址

在会话中通过数据消息发送，或在会话外通过对等测试消息发送。请参见下面的对等测试过程部分。

对于消息2，必须在前面有一个RouterInfo块，或包含Alice的Router Info的I2NP DatabaseStore消息块（或片段），要么在同一个载荷中（如果有空间），要么在之前的消息中。

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
对于消息4，如果relay被接受（原因代码0），必须前面有一个RouterInfo块，或I2NP DatabaseStore消息块（或片段），包含Charlie的Router Info，要么在同一个payload中（如果有空间），要么在之前的消息中。

- 对于 IPv4，Alice 的 IP 地址总是 4 字节，因为 Alice 试图通过 IPv4 连接到 Charlie。支持 IPv6，Alice 的 IP 地址可能是 16 字节。
- 对于 IPv4，此消息必须通过已建立的 IPv4 连接发送，因为只有这样 Bob 才能知道 Charlie 的 IPv4 地址，以便在 [RelayResponse](#relayresponse) 中返回给 Alice。支持 IPv6，此消息可以通过已建立的 IPv6 连接发送。
- 任何使用 introducers 发布的 SSU 地址都必须在 "caps" 选项中包含 "4" 或 "6"。

注意事项：

Alice 使用现有会话通过传输层（IPv4 或 IPv6）向 Bob 发送请求，这是她希望测试的传输层。当 Bob 通过 IPv4 收到来自 Alice 的请求时，Bob 必须选择一个公布 IPv4 地址的 Charlie。当 Bob 通过 IPv6 收到来自 Alice 的请求时，Bob 必须选择一个公布 IPv6 地址的 Charlie。实际的 Bob-Charlie 通信可能通过 IPv4 或 IPv6 进行（即，独立于 Alice 的地址类型）。

- prologue: 16 字节 "RelayRequestData"，不以空字符结尾（不包含在消息中）
- bhash: Bob 的 32 字节 router 哈希值（不包含在消息中）
- chash: Charlie 的 32 字节 router 哈希值（不包含在消息中）
- nonce: 4 字节随机数
- relay tag: 4 字节中继标签
- timestamp: 4 字节时间戳（秒）
- ver: 1 字节 SSU 版本
- asz: 1 字节端点（端口 + IP）大小（6 或 18）
- AlicePort: 2 字节 Alice 的端口号
- Alice IP: (asz - 2) 字节 Alice IP 地址

#### 中继标签请求

签名：

Alice 对请求进行签名并将其包含在消息1中；Bob 在消息2中将其转发给 Charlie。Charlie 对响应进行签名并将其包含在消息3中；Bob 在消息4中将其转发给 Alice。签名算法：使用 Alice 或 Charlie 的签名密钥对以下数据进行签名或验证：

TODO 仅在我们轮换密钥时

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
4字节确认通过，后跟确认计数和零个或多个否定确认/确认范围。

- 与 SSU 1 不同，消息 1 必须包含 Alice 的 IP 地址和端口。

- 支持IPv6地址测试，如果Bob和Charlie在其发布的IPv6地址中用'B'能力标识表示支持，那么Alice-Bob和Alice-Charlie通信可以通过IPv6进行。详情请参见提案126。

此设计改编并简化自 QUIC。设计目标如下：

- 消息 1-4 必须包含在现有会话的数据消息中。

- Bob 必须在发送消息 2 之前将 Alice 的 RI 发送给 Charlie。

- 如果接受（原因代码 0），Bob 必须在发送消息 4 之前将 Charlie 的 RI 发送给 Alice。

- 消息 5-7 必须包含在会话外的 Peer Test 消息中。

- 消息 5 和 7 可能包含与消息 3 和 4 中发送的相同签名数据，或者可以用新的时间戳重新生成。签名是可选的。

- 消息 6 可能包含与消息 1 和 2 中发送的相同签名数据，或者可能使用新时间戳重新生成。签名是可选的。

下面指定的编码通过发送设置为1的最高位的编号，以及低于该位且同样设置为1的额外连续位，来实现这些设计目标。之后，如果有空间，会有一个或多个"范围"，指定低于该位的连续0位和连续1位的数量。更多背景信息请参见QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000)第13.2.3节。

示例：

- prologue: 16 字节 "PeerTestValidate"，不以 null 结尾（不包含在消息中）
- bhash: Bob 的 32 字节 router 哈希（不包含在消息中）
- ahash: Alice 的 32 字节 router 哈希（仅用于消息 3 和 4 的签名；不包含在消息 3 或 4 中）
- ver: 1 字节 SSU 版本
- nonce: 4 字节测试随机数
- timestamp: 4 字节时间戳（秒）
- asz: 1 字节端点（端口 + IP）大小（6 或 18）
- AlicePort: 2 字节 Alice 的端口号
- Alice IP: (asz - 2) 字节 Alice IP 地址

#### Relay Tag

我们只想对数据包 10 进行 ACK 确认：

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
#### 新令牌

我们只想确认数据包 8-10：

我们想要 ACK 10 9 8 6 5 2 1 0，并且 NACK 7 4 3。ACK Block 的编码是：

- 我们希望高效地编码一个"位字段"，它是表示已确认数据包的位序列。
- 位字段主要由 1 组成。1 和 0 通常都以连续的"块"形式出现。
- 数据包中可用于确认的空间大小会变化。
- 最重要的位是编号最高的那个。编号较低的位不那么重要。在距离最高位一定距离以下，最旧的位将被"遗忘"且不再发送。

注意事项：

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
2字节端口和4或16字节IP地址。Alice的地址，由Bob发送给Alice，或Bob的地址，由Alice发送给Bob。

这可能由 Alice 在 Session Request、Session Confirmed 或 Data 消息中发送。在 Session Created 消息中不支持，因为 Bob 还没有 Alice 的 RI，也不知道 Alice 是否支持中继。另外，如果 Bob 正在接收传入连接，他可能不需要介绍者（除非可能是为了其他类型 ipv4/ipv6）。

- Ack Through: 10
- acnt: 0
- 不包含范围

当在会话请求中发送时，Bob可以在会话创建消息中回复一个中继标签，或者可以选择等到在会话确认中接收到Alice的RouterInfo来验证Alice的身份后再在数据消息中回复。如果Bob不希望为Alice进行中继，他不会发送中继标签块。

- Ack Through: 10
- acnt: 2
- 不包含范围

这可能由 Bob 在 Session Confirmed 或 Data 消息中发送，作为对 Alice 发送的 Relay Tag Request 的响应。

- Ack Through: 10
- acnt: 2 (ack 9 8)
- range: 1 2 (nack 7, ack 6 5)
- range: 2 3 (nack 4 3, ack 2 1 0)

当在 Session Request 中发送 Relay Tag Request 时，Bob 可以在 Session Created 消息中回复一个 Relay Tag，或者可以选择等到在 Session Confirmed 中收到 Alice 的 RouterInfo 来验证 Alice 的身份后再在 Data 消息中回复。如果 Bob 不希望为 Alice 进行中继，他就不发送 Relay Tag 块。

- 范围可能不存在。范围的最大数量未指定，可能有数据包能容纳的数量。
- 如果确认超过 255 个连续数据包，范围 nack 可能为零。
- 如果否定确认超过 255 个连续数据包，范围 ack 可能为零。
- 范围 nack 和 ack 不能同时为零。
- 在最后一个范围之后，数据包既不被确认也不被否定确认。ack 块的长度以及如何处理旧的 acks/nacks 由 ack 块的发送方决定。有关讨论，请参阅下面的 ack 部分。
- ack through 应该是接收到的最高数据包编号，任何更高的数据包都没有被接收到。但是，在有限的情况下，它可能更低，例如确认一个"填补空缺"的单个数据包，或者不维护所有已接收数据包状态的简化实现。在最高接收数据包之上，数据包既不被确认也不被否定确认，但在几个 ack 块之后，可能适合进入快速重传模式。
- 这种格式是 QUIC 中格式的简化版本。它旨在高效编码大量 ACK，以及 NACK 的突发。
- ACK 块用于确认数据阶段数据包。它们只能包含在会话内数据阶段数据包中。

#### 路径挑战

用于后续连接。通常包含在 Session Created 和 Session Confirmed 消息中。如果之前的令牌过期，也可能在长期会话的 Data 消息中再次发送。

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
#### 路径响应

一个携带任意数据的 Ping，数据会在 Path Response 中返回，用作保活机制或验证 IP/端口变更。

注意事项：

```
+----+----+----+
| 15 |    0    |
+----+----+----+

blk :: 15
size :: 2 bytes, big endian, value = 0
```
#### 第一个数据包编号

一个包含从路径挑战中接收到的数据的Pong消息，作为对路径挑战的回复，用于保持连接活跃或验证IP/端口变更。

可选地包含在每个方向的握手中，用于指定将要发送的第一个数据包编号。这为头部加密提供了更多安全性，类似于TCP。

```
+----+----+----+----+----+----+----+
| 16 |    4    |    relay tag      |
+----+----+----+----+----+----+----+

blk :: 16
size :: 2 bytes, big endian, value = 4
relay tag :: 4 bytes, big endian, nonzero
```
#### 拥塞

未完全指定，当前不支持。

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
#### 填充

这个块被设计为一种可扩展的方法来交换拥塞控制信息。拥塞控制可能很复杂，并且可能会随着我们在实时测试中获得更多协议经验，或在完全部署后而不断发展。

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
这样可以避免将任何拥塞信息放入高使用率的 I2NP、First Fragment、Followon Fragment 和 ACK 块中，因为这些块没有分配标志位的空间。虽然 Data 数据包头中有三个字节的未使用标志位，但这也为扩展性提供了有限的空间，并且加密保护较弱。

- 建议但不要求最小数据大小为8字节，包含随机数据。
- 最大大小未指定，但应远小于1280，因为路径验证阶段的PMTU为1280。
- 不建议使用大的挑战大小，因为它们可能成为数据包放大攻击的载体。

#### 对等节点地址欺骗

虽然使用4字节块来存储两位信息有些浪费，但通过将其放在单独的块中，我们可以轻松地用其他数据扩展它，如当前窗口大小、测量的RTT或其他标志。经验表明，仅使用标志位通常不足以满足需求，并且对于实现高级拥塞控制方案来说很笨拙。试图在例如ACK块中添加对任何可能的拥塞控制功能的支持，会浪费空间并增加该块解析的复杂性。

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
#### 路径上地址欺骗

实现不应假设其他 router 支持此处包含的任何特定标志位或功能，除非未来版本的此规范要求实现。

这个块应该是载荷中最后一个非填充块。

```
+----+----+----+----+----+----+----+
| 20 |  size   |  First pkt number |
+----+----+----+----+----+----+----+

blk :: 20
size :: 4
pkt num :: The first packet number to be sent in the data phase
```
#### 离路径数据包转发

这用于AEAD载荷内部的填充。所有消息的填充都在AEAD载荷内部。

填充应大致遵循协商的参数。Bob 在 Session Created 中发送了他请求的 tx/rx 最小/最大参数。Alice 在 Session Confirmed 中发送了她请求的 tx/rx 最小/最大参数。更新的选项可能在数据阶段发送。请参阅上面的选项块信息。

如果存在，这必须是载荷中的最后一个块。

注意事项：

SSU2 旨在最小化攻击者重放消息的影响。

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
#### 隐私影响

Token Request、Retry、Session Request、Session Created、Hole Punch 和 out-of-session Peer Test 消息必须包含 DateTime 块。

Alice和Bob都验证这些消息的时间是否在有效的偏差范围内（建议±2分钟）。为了"探测抵抗"，如果偏差无效，Bob不应回复Token Request或Session Request消息，因为这些消息可能是重放攻击或探测攻击。

Bob 可以选择通过 Bloom 过滤器或其他机制拒绝重复的 Token Request 和 Retry 消息，即使时间偏差是有效的。但是，回复这些消息的大小和 CPU 成本都很低。在最坏情况下，重放的 Token Request 消息可能会使之前发送的 token 失效。

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
token系统极大地减少了重放Session Request消息的影响。由于token只能使用一次，重放的Session Request消息永远不会有有效的token。Bob可以选择拒绝重复的Session Request消息，即使时间偏移是有效的，可通过布隆过滤器或其他机制实现。然而，回复Retry消息的大小和CPU开销都很低。最坏情况下，发送Retry消息可能会使之前发送的token失效。

- 大小 = 0 是允许的。
- 填充策略待定。
- 最小填充待定。
- 允许仅填充的载荷。
- 默认填充待定。
- 参见选项块中的填充参数协商
- 参见选项块中的最小/最大填充参数
- 不要超过 MTU。如果需要更多填充，发送多条消息。
- router 对违反协商填充的响应取决于具体实现。
- 填充长度要么基于每条消息决定并估算长度分布，要么应该添加随机延迟。这些对策应该被包括进来以抵抗 DPI（深度包检测），因为消息大小否则会暴露传输协议正在承载 I2P 流量。确切的填充方案是未来工作的一个领域，[NTCP2](/docs/specs/ntcp2) 的附录 A 提供了关于该主题的更多信息。

## 重放攻击防护

重复的 Session Created 和 Session Confirmed 消息将无法验证，因为 Noise 握手状态不会处于正确状态来解密它们。最坏的情况下，对等节点可能会响应明显重复的 Session Created 而重传 Session Confirmed。

重放的打洞和对等测试消息应该几乎没有影响。

Router 必须使用数据消息包编号来检测和丢弃重复的数据阶段消息。每个包编号只能使用一次。重放的消息必须被忽略。

如果Alice没有收到Session Created或Retry消息：

保持相同的源ID和连接ID、临时密钥和数据包编号0。或者，只需保留并重传相同的加密数据包。数据包编号不得递增，因为这会改变用于加密Session Created消息的链式哈希值。

推荐的重传间隔：1.25、2.5 和 5 秒（首次发送后的 1.25、3.75 和 8.75 秒）。推荐超时：总共 15 秒

如果 Bob 没有收到 Session Confirmed：

保持相同的源ID和连接ID、临时密钥以及数据包编号0。或者，只保留加密的数据包。数据包编号不能递增，因为这会改变用于加密Session Confirmed消息的链式哈希值。

## 握手重传

### 会话已创建

推荐的重传间隔：1、2 和 4 秒（首次发送后的 1、3 和 7 秒）。推荐超时时间：总共 12 秒

在 SSU 1 中，Alice 在收到 Bob 的第一个数据包之前不会切换到数据阶段。这使得 SSU 1 成为一个两轮往返的设置过程。

对于 SSU 2，推荐的会话确认重传间隔为：1.25、2.5 和 5 秒（首次发送后的 1.25、3.75 和 8.75 秒）。

### 会话已确认

有几种替代方案。所有这些都是1个RTT：

1) Alice假设已收到Session Confirmed，立即发送数据消息，从不重传Session Confirmed。乱序接收的数据包（在Session Confirmed之前）将无法解密，但会被重传。如果Session Confirmed丢失，所有已发送的数据消息都将被丢弃。2) 如1)中所述，立即发送数据消息，但同时重传Session Confirmed直到收到数据消息。3) 我们可以使用IK而不是XK，因为它在握手中只有两条消息，但它使用额外的DH（4个而不是3个）。

推荐的实现方式是选项 2）。Alice 必须保留重传 Session Confirmed 消息所需的信息。Alice 还应该在重传 Session Confirmed 消息后重传所有数据消息。

### 令牌请求

重传 Session Confirmed 时，保持相同的源 ID 和连接 ID、临时密钥和数据包编号 1。或者，仅保留加密数据包。数据包编号不得递增，因为这会改变链式哈希值，而该值是 split() 函数的输入。

Bob 可以保留（排队）在收到 Session Confirmed 消息之前接收到的数据消息。在收到 Session Confirmed 消息之前，头部保护密钥和解密密钥都不可用，所以 Bob 不知道它们是数据消息，但可以推测它们是。在收到 Session Confirmed 消息后，Bob 能够解密和处理排队的数据消息。如果这太复杂，Bob 可以直接丢弃无法解密的数据消息，因为 Alice 会重新传输它们。

注意：如果session confirmed数据包丢失，Bob将重新传输session created。由于session created头部是用Bob的intro key设置的，因此无法用Alice的intro key解密（除非使用Bob的intro key执行回退解密）。如果之前未收到确认且收到了无法解密的数据包，Bob可能会立即重新传输session confirmed数据包。

如果Alice没有收到Retry：

保持相同的源ID和连接ID。实现可以生成新的随机包号并加密新包；或者可以重用相同的包号，或者只是保留并重传相同的加密包。包号不得递增，因为这会改变用于加密Session Created消息的链式哈希值。

推荐的重传间隔：3秒和6秒（首次发送后3秒和9秒）。推荐超时时间：总计15秒

如果 Bob 没有收到 Session Confirmed：

Retry 消息在超时时不会重新传输，以减少伪造源地址的影响。

### 重试

然而，重试消息可能会重新传输，以响应收到的带有原始（无效）token 的重复会话请求消息，或者响应重复的 Token 请求消息。在任一情况下，这表明重试消息已丢失。

如果接收到第二个Session Request消息，其中包含不同但仍然无效的令牌，则丢弃待处理的会话且不响应。

如果重新发送 Retry 消息：保持相同的源和连接 ID 以及 token。实现可以生成新的随机数据包编号并加密新数据包；或者可以重用相同的数据包编号或仅保留并重新传输相同的加密数据包。

### 总超时时间

建议的握手总超时时间为 20 秒。

在对头部进行 MixHash() 之前，必须检测三个 Noise 握手消息 Session Request、Session Created 和 Session Confirmed 的重复消息。虽然在此之后 Noise AEAD 处理可能会失败，但握手哈希已经被破坏了。

如果三条消息中的任何一条被损坏并导致 AEAD 失败，即使重新传输，握手也无法恢复，因为 MixHash() 已经在损坏的消息上被调用了。

Session Request 头部中的 Token 用于 DoS 缓解、防止源地址欺骗，以及抵御重放攻击。

如果Bob在Session Request消息中不接受该token，Bob不会解密消息，因为这需要昂贵的DH操作。Bob只是发送一个带有新token的Retry消息。

### 重复项和错误处理

如果随后收到带有该令牌的会话请求消息，Bob会继续解密该消息并进行握手。

### 数据包编号

如果token生成器存储这些值以及相关联的IP和端口（在内存中或持久存储），那么token必须是一个随机生成的8字节值。生成器不能生成不透明值，例如，使用IP、端口和当前小时或天的SipHash（带有密钥种子K0、K1）来创建无需保存在内存中的token，因为这种方法使得拒绝重复使用的token和重放攻击变得困难。然而，正如[WireGuard](https://www.wireguard.com/papers/wireguard.pdf)所做的那样，使用服务器密钥和IP地址的16字节HMAC，我们是否可以迁移到这样的方案还有待进一步研究。

Token只能使用一次。Bob在重试消息中发送给Alice的token必须立即使用，并在几秒钟内过期。在已建立会话中通过New Token块发送的token可以在后续连接中使用，并在该块指定的时间过期。过期时间由发送方指定；推荐值为最少几分钟，最多一小时或更长，具体取决于存储token的期望最大开销。

## 令牌

如果router的IP或端口发生变化，它必须删除旧IP或端口对应的所有已保存令牌（包括入站和出站），因为这些令牌不再有效。令牌可以选择性地在router重启后持久保存，这取决于具体实现。不保证接受未过期的令牌；如果Bob忘记或删除了他保存的令牌，他将向Alice发送重试请求。router可以选择限制令牌存储，并移除最旧的已存储令牌，即使它们尚未过期。

新的 Token 块可以从 Alice 发送到 Bob，也可以从 Bob 发送到 Alice。它们通常在会话建立期间或之后不久至少发送一次。由于在 Session Confirmed 消息中对 RouterInfo 进行验证检查，Bob 不应在 Session Created 消息中发送新的 Token 块，它可以在收到并验证 Session Confirmed 后与 ACK 0 和 Router Info 一起发送。

由于会话生命周期通常比令牌过期时间更长，应该在过期前或过期后重新发送带有新过期时间的令牌，或者发送新令牌。Router 应该假设只有最后收到的令牌有效；没有要求为同一个 IP/端口存储多个入站或出站令牌。

令牌绑定到源IP/端口和目标IP/端口的组合。在IPv4上接收的令牌不能用于IPv6，反之亦然。

如果会话期间任一对等节点迁移到新的IP或端口（参见连接迁移部分），则之前交换的所有令牌都将失效，必须交换新的令牌。

实现可以（但不是必须的）将令牌保存到磁盘并在重启时重新加载它们。如果持久化保存，实现必须确保IP地址和端口自关闭以来没有发生变化，然后才能重新加载它们。

与 SSU 1 的区别

注意：与 SSU 1 一样，初始分片不包含关于分片总数或总长度的信息。后续分片不包含关于其偏移量的信息。这为发送方提供了根据数据包中可用空间"动态"分片的灵活性。（Java I2P 不会这样做；它在发送第一个分片之前进行"预分片"）然而，这确实给接收方带来了负担，需要存储乱序接收的分片，并延迟重组直到接收到所有分片。

与 SSU 1 中一样，任何片段的重传都必须保持片段之前传输的长度（和隐含的偏移量）。

SSU 2确实将三种情况（完整消息、初始片段和后续片段）分离为三种不同的块类型，以提高处理效率。

此协议并不能完全防止 I2NP 消息的重复传递。IP 层的重复或重放攻击将在 SSU2 层被检测到，因为每个数据包编号只能使用一次。

## I2NP 消息分片

然而，当 I2NP 消息或片段在新数据包中重传时，这在 SSU2 层是无法检测到的。路由器应该强制执行 I2NP 过期检查（包括太旧和太远的未来时间），并使用基于 I2NP 消息 ID 的布隆过滤器或其他机制。

router 或 SSU2 实现中可能使用其他机制来检测重复消息。例如，SSU2 可以维护一个最近接收到的消息 ID 缓存。这取决于具体实现。

本规范指定了数据包编号和ACK块的协议。这为发送方提供了足够的实时信息来实现高效且响应迅速的拥塞控制算法，同时在实现中允许灵活性和创新。本节讨论实现目标并提供建议。一般指导可以在[RFC-9002](https://tools.ietf.org/html/rfc9002)中找到。有关重传定时器的指导，另请参阅[RFC-6298](https://tools.ietf.org/html/rfc6298)。

仅包含ACK的数据包不应计入传输中的字节数或包数，也不受拥塞控制。与TCP不同，SSU2可以检测到这些包的丢失，该信息可用于调整拥塞状态。但是，本文档未指定执行此操作的机制。

## I2NP 消息重复

如果需要，包含其他一些非数据块的数据包也可以从拥塞控制中排除，这取决于具体实现。例如：

建议拥塞控制基于字节计数而非数据包计数，遵循 TCP RFC 和 QUIC [RFC-9002](https://tools.ietf.org/html/rfc9002) 中的指导原则。额外的数据包计数限制也可能有用，以防止内核或中间件中的缓冲区溢出，这取决于具体实现，尽管这可能会增加显著的复杂性。如果按会话和/或总数据包输出受到带宽限制和/或节奏控制，这可能会减轻对数据包计数限制的需求。

在 SSU 1 中，ACK 和 NACK 包含 I2NP 消息编号和片段位掩码。发送方跟踪出站消息（及其片段）的 ACK 状态，并根据需要重传片段。

## 拥塞控制

在 SSU 2 中，ACK 和 NACK 包含数据包编号。发送方必须维护一个数据结构，将数据包编号映射到其内容。当数据包被 ACK 或 NACK 时，发送方必须确定该数据包中包含哪些 I2NP 消息和片段，以决定需要重传什么内容。

Bob 发送数据包 0 的 ACK，确认会话确认消息并允许 Alice 进入数据阶段，同时丢弃为可能的重传而保存的大型会话确认消息。这取代了 Bob 在 SSU 1 中发送的 DeliveryStatusMessage。

Bob 应该在收到 Session Confirmed 消息后尽快发送 ACK。小的延迟（不超过 50 毫秒）是可以接受的，因为至少一个 Data 消息应该会在 Session Confirmed 消息之后几乎立即到达，这样 ACK 可以同时确认 Session Confirmed 和 Data 消息。这将防止 Bob 必须重传 Session Confirmed 消息。

- 对等测试
- 中继请求/介绍/响应
- 路径质询/响应

定义：引发确认的数据包：包含引发确认块的数据包会在最大确认延迟时间内从接收方引发一个 ACK，这些数据包被称为引发确认的数据包。

### 会话确认 ACK

Router 会确认它们接收和处理的所有数据包。但是，只有需要确认的数据包会在最大确认延迟内触发发送 ACK 块。不需要确认的数据包只有在因其他原因发送 ACK 块时才会被确认。

当出于任何原因发送数据包时，如果最近没有发送过，端点应尝试包含一个ACK块。这样做有助于对端及时检测丢包。

### 生成 ACK

一般来说，接收方的频繁反馈能够改善丢包和拥塞响应，但这需要与接收方对每个需要确认的数据包都发送ACK块所产生的过度负载进行平衡。下面提供的指导旨在实现这种平衡。

包含除以下块之外任何块的会话内数据包都会引发确认：

### 握手 ACK

会话外数据包，包括握手消息和对等测试消息5-7，有自己的确认机制。见下文。

这些是特殊情况：

ACK 块用于确认数据阶段数据包。它们仅用于会话内的数据阶段数据包。

每个数据包都应该至少被确认一次，而引发确认的数据包必须在最大延迟时间内至少被确认一次。

端点必须在其最大延迟时间内立即确认所有需要确认的握手数据包，但有以下例外。在握手确认之前，端点可能没有用于解密接收到的数据包的包头加密密钥。因此它可能会缓存这些数据包，并在获得必需的密钥后对其进行确认。

- ACK 块
- 地址块
- 日期时间块
- 填充块
- 终止块
- 其他？

由于仅包含 ACK 块的数据包不受拥塞控制，端点在收到引发确认的数据包时，不得发送超过一个此类数据包作为响应。

### 发送 ACK 块

端点不得发送非确认引发数据包来响应非确认引发数据包，即使在接收到的数据包之前存在数据包间隙。这避免了确认的无限反馈循环，否则可能导致连接永远无法变为空闲状态。当端点因其他事件发送ACK块时，非确认引发数据包最终会被确认。

- Token Request 由 Retry 隐式确认
- Session Request 由 Session Created 或 Retry 隐式确认
- Retry 由 Session Request 隐式确认
- Session Created 由 Session Confirmed 隐式确认
- Session Confirmed 应立即确认

### ACK 频率

仅发送 ACK 块的端点不会从其对等方收到确认，除非这些确认包含在带有需要确认块的数据包中。当有新的需要确认的数据包需要确认时，端点应该与其他块一起发送 ACK 块。当只有非需要确认的数据包需要确认时，端点可以选择不与传出块一起发送 ACK 块，直到收到需要确认的数据包。

只发送非请求确认数据包的端点可能会选择偶尔向这些数据包添加请求确认块，以确保它能收到确认。在这种情况下，端点不得在所有本来是非请求确认的数据包中都发送请求确认块，以避免确认的无限反馈循环。

为了协助发送端进行丢包检测，当端点在以下任何情况下接收到需要确认的数据包时，应该立即生成并发送ACK块，不应延迟：

这些算法预期能够抵御不遵循上述指导原则的接收方。但是，实现应该仅在仔细考虑了变更对端点建立的连接以及网络其他用户的性能影响之后，才可偏离这些要求。

接收方决定多久发送一次确认消息来响应需要确认的数据包。这个决定涉及权衡取舍。

端点依赖及时的确认来检测丢失。基于窗口的拥塞控制器依赖确认来管理其拥塞窗口。在这两种情况下，延迟确认都可能对性能产生不利影响。

另一方面，减少仅携带确认信息的数据包频率可以降低两端的数据包传输和处理成本。这可以改善严重不对称链路上的连接吞吐量，并减少使用返回路径容量的确认流量；请参见 [RFC-3449](https://tools.ietf.org/html/rfc3449) 的第 3 节。

接收方应在收到至少两个需要确认的数据包后发送ACK块。此建议具有通用性质，并与TCP端点行为建议[RFC-5681](https://tools.ietf.org/html/rfc5681)保持一致。对网络条件的了解、对对等方拥塞控制器的了解，或进一步的研究和实验可能会建议采用具有更好性能特征的替代确认策略。

- 当接收到的数据包的包号小于已接收到的另一个需要确认的数据包时
- 当数据包的包号大于已接收到的编号最高的需要确认的数据包，且在该数据包与当前数据包之间存在丢失的数据包时
- 当数据包头中设置了立即确认标志时

接收方可以在决定是否发送ACK块作为响应之前处理多个可用数据包。一般来说，接收方延迟ACK的时间不应超过RTT / 6，或最多150毫秒。

### 立即 ACK 标志

数据包头中的ack-immediate标志是一个请求，要求接收方在接收后尽快发送ack，通常在几毫秒内。一般来说，接收方延迟立即ACK的时间不应超过RTT / 16，或最多5毫秒。

接收方不知道发送方的发送窗口大小，因此不知道在发送ACK之前应该延迟多长时间。数据包头中的立即ACK标志是通过最小化有效RTT来维持最大吞吐量的重要方式。立即ACK标志位于头部字节13的第0位，即(header[13] & 0x01)。当设置时，请求立即ACK。详细信息请参见上面的短头部章节。

发送方可以使用几种可能的策略来确定何时设置立即确认标志：

即时 ACK 标志应该只在包含 I2NP 消息或消息片段的数据包上才有必要。

当发送ACK块时，会包含一个或多个已确认数据包的范围。包含对较旧数据包的确认可以减少因丢失先前发送的ACK块而导致的虚假重传的可能性，但代价是ACK块变得更大。

ACK 块应该始终确认最近接收到的数据包，数据包越乱序，就越需要快速发送更新的 ACK 块，以防止对等方将数据包声明为丢失并错误地重传其包含的块。ACK 块必须适合单个数据包。如果不适合，则会省略较旧的范围（具有最小数据包号的范围）。

### ACK 块大小

接收方限制其记住和在ACK块中发送的ACK范围数量，既是为了限制ACK块的大小，也是为了避免资源耗尽。在收到ACK块的确认后，接收方应该停止跟踪那些已确认的ACK范围。发送方可以期望大多数数据包得到确认，但此协议不保证接收方处理的每个数据包都会收到确认。

保留许多 ACK 范围可能会导致 ACK 块变得过大。接收方可以丢弃未确认的 ACK 范围来限制 ACK 块大小，代价是发送方会增加重传。如果 ACK 块过大而无法放入数据包中，这种做法是必要的。接收方也可以进一步限制 ACK 块大小，以便为其他块保留空间或限制确认消息消耗的带宽。

- 每N个数据包设置一次，N为较小值
- 在数据包突发的最后一个包上设置
- 当发送窗口接近满载时设置，例如超过2/3满
- 在所有包含重传片段的数据包上设置

接收方必须保留ACK范围，除非它能确保不会随后接受该范围内的数据包。维护一个随着范围被丢弃而递增的最小数据包编号是以最小状态实现这一点的方法之一。

### 通过跟踪 ACK 块来限制范围

接收方可以丢弃所有 ACK 范围，但必须保留已成功处理的最大数据包编号，因为这用于从后续数据包中恢复数据包编号。

下面的章节描述了一种用于确定在每个 ACK 块中应该确认哪些数据包的示例方法。尽管该算法的目标是为每个处理的数据包生成确认，但确认消息仍然可能丢失。

当发送包含ACK块的数据包时，可以保存该块中的Ack Through字段。当包含ACK块的数据包被确认时，接收方可以停止确认小于或等于已发送ACK块中Ack Through字段的数据包。

仅发送非需确认数据包（如 ACK 块）的接收方可能在很长时间内都收不到确认。这可能导致接收方长时间维护大量 ACK 块的状态，并且它发送的 ACK 块可能会变得不必要地庞大。在这种情况下，接收方可以偶尔发送 PING 或其他小的需确认块，比如每轮往返发送一次，以引发对等方的 ACK 响应。

在没有 ACK 块丢失的情况下，此算法允许最小 1 RTT 的重排序。在存在 ACK 块丢失和重排序的情况下，此方法不能保证发送方在确认不再包含在 ACK 块中之前看到每个确认。数据包可能会乱序接收，并且包含这些数据包的所有后续 ACK 块都可能丢失。在这种情况下，丢失恢复算法可能会导致虚假重传，但发送方将继续取得前进进展。

I2P 传输不保证 I2NP 消息的按序传递。因此，包含一个或多个 I2NP 消息或片段的数据消息丢失不会阻止其他 I2NP 消息的传递；不存在队头阻塞。如果发送窗口允许，实现应该在丢失恢复阶段继续发送新消息。

发送方不应保留消息的完整内容以进行相同的重传（握手消息除外，见上文）。发送方必须在每次发送消息时组装包含最新信息（ACK、NACK 和未确认数据）的消息。发送方应避免重传已被确认的消息中的信息。这包括在被声明丢失后才被确认的消息，这种情况可能在网络重排序的情况下发生。

### 拥塞

待定。一般指导可参考 [RFC-9002](https://tools.ietf.org/html/rfc9002)。

在会话生命周期内，对等节点的IP或端口可能会发生变化。IP变化可能由IPv6临时地址轮换、ISP驱动的定期IP变更、移动客户端在WiFi和蜂窝网络IP之间切换，或其他本地网络变化引起。端口变化可能由于之前绑定超时后NAT重新绑定引起。

由于各种路径上和路径外攻击，包括修改或注入数据包，对等节点的IP或端口可能看起来发生了变化。

### 重传

连接迁移是一个验证新源端点（IP+端口）的过程，同时防止未经验证的更改。此过程是 QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) 中定义过程的简化版本。此过程仅针对会话的数据阶段定义。在握手期间不允许迁移。所有握手数据包都必须经过验证，确保来自与之前发送和接收数据包相同的 IP 和端口。换句话说，对等方的 IP 和端口在握手期间必须保持不变。

### 窗口

（改编自 QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000)）

### 威胁模型

对等节点可能伪造其源地址，导致端点向不愿意的主机发送大量数据。如果端点发送的数据明显多于伪造的对等节点，连接迁移可能被用来放大攻击者能够向受害者生成的数据量。

## 连接迁移

路径上的攻击者可能通过复制并转发带有伪造地址的数据包来引起虚假连接迁移，使其在原始数据包之前到达。带有伪造地址的数据包将被视为来自迁移连接，而原始数据包将被视为重复数据包并被丢弃。在虚假迁移之后，源地址验证将失败，因为源地址处的实体没有必要的加密密钥来读取或响应发送给它的 Path Challenge，即使它想要响应也无法做到。

能够观察数据包的路径外攻击者可能会将真实数据包的副本转发到端点。如果复制的数据包在真实数据包之前到达，这将表现为NAT重新绑定。任何真实数据包都会被丢弃，因为它是重复的。如果攻击者能够继续转发数据包，它可能能够导致迁移到经过攻击者的路径。这将攻击者置于路径上，使其能够观察或丢弃所有后续数据包。

QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) 规定在更改网络路径时要更改连接 ID。在多个网络路径上使用稳定的连接 ID 会允许被动观察者关联这些路径之间的活动。在网络间移动的端点可能不希望除了对等方之外的任何实体关联他们的活动。然而，QUIC 不会加密头部中的连接 ID。SSU2 确实会这样做，因此隐私泄露需要被动观察者还要能够访问 netDb 来获取解密连接 ID 所需的介绍密钥。即使有了介绍密钥，这也不是一个强有力的攻击，我们在 SSU2 迁移后不会更改连接 ID，因为这会是一个重大的复杂化问题。

### 启动路径验证

在数据阶段，节点必须检查每个接收到的数据包的源IP和端口。如果IP或端口与之前接收到的不同，并且该数据包不是重复的包编号，并且数据包成功解密，则会话进入路径验证阶段。

#### Introducer 选择

此外，peer 必须验证新的 IP 和端口根据本地验证规则是有效的（未被阻止、非非法端口等）。Peer 不需要支持 IPv4 和 IPv6 之间的迁移，并且可以将其他地址族中的新 IP 视为无效，因为这不是预期行为并且可能增加显著的实现复杂性。在从无效的 IP/端口接收到数据包时，实现可以简单地丢弃它，或者可以使用旧的 IP/端口启动路径验证。

#### 响应处理

进入路径验证阶段后，请按照以下步骤操作：

#### 介绍人

在路径验证阶段，会话可能会继续处理传入的数据包，无论是来自旧的还是新的IP/端口。会话也可能继续发送和确认数据包。然而，在路径验证阶段，拥塞窗口和PMTU必须保持在最小值，以防止通过向伪造地址发送大量流量来进行拒绝服务攻击。

#### 身份隐藏

实现可以（但不是必需的）尝试同时验证多个路径。这可能不值得增加复杂性。实现也可以（但不是必需的）记住之前已验证的IP/端口，并且如果对等节点返回到其之前的IP/端口时跳过路径验证。

### 消息内容

如果接收到包含与 Path Challenge 中发送的相同数据的 Path Response，则路径验证成功。Path Response 消息的源 IP/端口不需要与发送 Path Challenge 的目标相同。

如果在路径响应计时器过期之前未收到路径响应，则发送另一个路径质疑并将路径响应计时器时间加倍。

如果在路径验证计时器过期之前未收到路径响应，则路径验证失败。

- 启动一个几秒钟的路径验证超时计时器，或当前 RTO 的几倍（待定）
- 将拥塞窗口减少到最小值
- 将 PMTU 减少到最小值（1280）
- 发送一个数据包，包含 Path Challenge 块、Address 块（包含新的 IP/端口）以及通常的 ACK 块，发送到新的 IP 和端口。此数据包使用与当前会话相同的连接 ID 和加密密钥。Path Challenge 块数据必须包含足够的熵（至少 8 字节），以便无法被伪造。
- 可选地，也向旧的 IP/端口发送 Path Challenge，使用不同的块数据。见下文。
- 基于当前 RTO 启动 Path Response 超时计时器（通常为 RTT + RTTdev 的倍数）

Data 消息应该包含以下数据块。除了填充必须在最后之外，顺序没有特定要求：

不建议在消息中包含任何其他块（例如，I2NP）。

允许在包含 Path Response 的消息中包含 Path Challenge 块，以启动另一个方向的验证。

Path Challenge 和 Path Response 块是需要确认的。Path Challenge 将通过包含 Path Response 和 ACK 块的 Data 消息进行确认。Path Response 应该通过包含 ACK 块的 Data 消息进行确认。

QUIC 规范对于在路径验证期间将数据包发送到何处（旧的或新的 IP/端口）并不明确。需要在快速响应 IP/端口变更和不向伪造地址发送流量之间取得平衡。此外，不能允许伪造的数据包对现有会话产生实质性影响。仅端口变更可能是由于空闲期后 NAT 重新绑定导致的；IP 变更可能在单向或双向高流量阶段发生。

### 路径验证期间的路由

策略需要研究和改进。可能的方案包括：

- Path Challenge 或 Path Response 块。Path Challenge 包含不透明数据，建议最少8字节。Path Response 包含来自 Path Challenge 的数据。
- 包含接收者表面IP的地址块
- DateTime 块
- ACK 块
- 填充块

收到路径挑战后，对等节点必须用包含路径响应的数据包进行响应，其中包含来自路径挑战的数据。

Path Response 必须发送到接收 Path Challenge 的 IP/端口。这并不一定是之前为对等节点建立的 IP/端口。这确保了只有在路径在两个方向上都正常工作时，对等节点的路径验证才能成功。请参见下面的本地更改后验证部分。

除非IP/端口与该peer之前已知的IP/端口不同，否则将Path Challenge视为简单的ping，并无条件地用Path Response进行响应。接收方不会基于收到的Path Challenge保持或更改任何状态。如果IP/端口不同，peer必须根据本地验证规则验证新的IP和端口是否有效（未被阻止、不是非法端口等）。peer不需要支持IPv4和IPv6之间的跨地址族响应，并且可以将另一个地址族中的新IP视为无效，因为这不是预期的行为。

### 响应路径挑战

除非受到拥塞控制的约束，否则应该立即发送路径响应。如有必要，实现应该采取措施对路径响应进行速率限制或限制所使用的带宽。

Path Challenge 块通常会在同一消息中伴随一个 Address 块。如果地址块包含新的 IP/端口，对等节点可以验证该 IP/端口，并与会话对等节点或任何其他对等节点一起启动对该新 IP/端口的对等节点测试。如果对等节点认为自己处于防火墙后面，且仅端口发生了变化，这种变化可能是由于 NAT 重新绑定造成的，进一步的对等节点测试可能不需要。

- 在验证之前不向新的 IP/端口发送数据包
- 继续向旧的 IP/端口发送数据包，直到新的 IP/端口得到验证
- 同时重新验证旧的 IP/端口
- 在旧的或新的 IP/端口任一得到验证之前不发送任何数据
- 仅端口变更与 IP 变更采用不同的策略
- 对于同一个 /32 内的 IPv6 变更采用不同的策略，这种变更可能由临时地址轮换引起

### 成功的路径验证

路径验证成功后，连接将完全迁移到新的IP/端口。成功时：

在路径验证阶段，任何从旧IP/端口接收到的有效、非重复数据包，如果成功解密，都会导致路径验证被取消。重要的是，由伪造数据包引起的路径验证取消不应导致有效会话被终止或显著中断。

关于取消的路径验证：

重要的是，由伪造数据包导致的路径验证失败不应导致有效会话被终止或受到严重干扰。

在路径验证失败时：

### 取消路径验证

上述过程是为接收到来自已更改IP/端口的数据包的对等节点而定义的。然而，它也可以从另一个方向启动，即由检测到自己IP或端口已更改的对等节点发起。对等节点可能能够检测到其本地IP已更改；但是，由于NAT重新绑定，检测到其端口更改的可能性要小得多。因此，这是可选的。

- 退出路径验证阶段
- 所有数据包都发送到新的IP和端口。
- 移除对拥塞窗口和PMTU的限制，允许它们增加。不要简单地将它们恢复到旧值，因为新路径可能具有不同的特征。
- 如果IP发生变化，将计算的RTT和RTO设置为初始值。因为仅端口变化通常是NAT重新绑定或其他中间设备活动的结果，在这些情况下，对等节点可以保留其拥塞控制状态和往返时间估计，而不是恢复到初始值。
- 删除（使无效）为旧IP/端口发送或接收的任何令牌（可选）
- 为新IP/端口发送新的令牌块（可选）

### 路径验证失败

在收到IP或端口已更改的对等节点发送的路径挑战时，另一个对等节点应该在相反方向发起路径挑战。

Path Challenge 和 Path Response 块可以随时用作 Ping/Pong 数据包。接收到 Path Challenge 块不会改变接收方的任何状态，除非是从不同的 IP/端口接收到的。

- 退出路径验证阶段
- 所有数据包都发送到旧的IP和端口
- 移除对拥塞窗口和PMTU的限制，允许它们增加，或者可选地恢复之前的值
- 将之前发送到新IP/端口的任何数据包重传到旧IP/端口

### 本地更改后的验证

节点不应与同一对等节点建立多个会话，无论是 SSU 1 还是 2，或者使用相同或不同的 IP 地址。但是，这种情况可能会发生，可能是由于程序错误，或者之前的会话终止消息丢失，或者在终止消息尚未到达的竞态条件下。

如果Bob与Alice已有一个现有会话，当Bob从Alice接收到会话确认消息，完成握手并建立新会话时，Bob应该：

- 退出路径验证阶段
- 所有数据包都发送到旧的IP和端口。
- 移除对拥塞窗口和PMTU的限制，允许它们增加。
- 可选择在旧的IP和端口上启动路径验证。如果失败，则终止会话。
- 否则，遵循标准的会话超时和终止规则。
- 将之前发送到新IP/端口的任何数据包重传到旧的IP/端口。

### 用作 Ping/Pong

处于握手阶段的会话通常通过超时或不再响应来简单地终止。可选地，它们也可以通过在响应中包含终止块来终止，但由于缺乏加密密钥，大多数错误都无法响应。即使有密钥可用于包含终止块的响应，通常也不值得消耗CPU来执行DH运算以生成响应。一个例外可能是重试消息中的终止块，因为这种终止块生成成本很低。

数据阶段的会话通过发送包含终止块的数据消息来终止。此消息还应包含 ACK 块。如果会话已运行足够长时间，以至于先前发送的令牌已过期或即将过期，则可能包含新令牌块。此消息不会引发确认。当接收到终止块且原因不是"已接收终止"时，对等方会响应一个包含终止块的数据消息，原因为"已接收终止"。

### 握手阶段

在发送或接收终止块后，会话应进入关闭阶段，持续时间为待定的最大时间段。关闭状态是必要的，以防包含终止块的数据包丢失，以及处理另一个方向上正在传输的数据包。在关闭阶段，无需处理任何额外接收到的数据包。处于关闭状态的会话会发送包含终止块的数据包，以响应任何归属于该会话的传入数据包。会话应限制其在关闭状态下生成数据包的速率。例如，会话可以等待逐渐增加的接收数据包数量或时间长度，然后再响应接收到的数据包。

## 多会话

为了最小化router在关闭会话时需要维护的状态，会话可以（但不是必须）发送完全相同的数据包，使用相同的包号来响应任何接收到的数据包。注意：允许重传终止数据包是对每个数据包必须使用新包号这一要求的例外。发送新包号主要有利于丢包恢复和拥塞控制，而对于已关闭的连接，这些功能预计不会相关。重传最终数据包需要更少的状态维护。

在接收到原因为"Termination Received"的终止块后，会话可以退出关闭阶段。

- 将旧会话中任何未发送或未确认的出站 I2NP 消息迁移到新会话
- 在旧会话上发送带有原因代码 22 的终止消息
- 移除旧会话并用新会话替换

## 会话终止

### 数据阶段

在任何正常或异常终止时，router 应清零所有内存中的临时数据，包括握手临时密钥、对称加密密钥以及相关信息。

### 清理

需求因发布地址是否与 SSU 1 共享而有所不同。当前 SSU 1 IPv4 最小值为 620，这显然太小了。

IPv4 和 IPv6 的最小 SSU2 MTU 都是 1280，这与 [RFC-9000](https://tools.ietf.org/html/rfc9000) 中规定的相同。见下文。通过增加最小 MTU，1 KB tunnel 消息和短 tunnel 构建消息将适合在一个数据报中，大大减少了典型的分片数量。这也允许增加最大 I2NP 消息大小。1820 字节的流消息应该能适合在两个数据报中。

除非该地址的MTU至少为1280，否则router不得启用SSU2或发布SSU2地址。

路由器必须在每个 SSU 或 SSU2 router 地址中发布非默认的 MTU。

### SSU 地址

与 SSU 1 共享地址，必须遵循 SSU 1 规则。IPv4：默认和最大值为 1484。最小值为 1292。(IPv4 MTU + 4) 必须是 16 的倍数。IPv6：必须发布，最小值为 1280，最大值为 1488。IPv6 MTU 必须是 16 的倍数。

## MTU

IPv4：默认值和最大值为1500。最小值为1280。IPv6：默认值和最大值为1500。最小值为1280。没有16的倍数规则，但应该至少是2的倍数。

对于 SSU 1，当前的 Java I2P 通过从小数据包开始并逐渐增加大小，或基于接收到的数据包大小来增加，从而执行 PMTU 发现。这种方法很粗糙，大大降低了效率。在 SSU 2 中是否继续这个功能还待定。

最近的研究 [PMTU](https://en.wikipedia.org/wiki/Path_MTU_Discovery) 表明，IPv4 的最小值为 1200 或更高将适用于超过 99% 的连接。QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) 要求最小 IP 数据包大小为 1280 字节。

引用 [RFC-9000](https://tools.ietf.org/html/rfc9000)：

### SSU2 地址

最大数据报大小被定义为可以使用单个UDP数据报通过网络路径发送的UDP负载的最大尺寸。如果网络路径无法支持至少1200字节的最大数据报大小，则不得使用QUIC。

### PMTU 发现

QUIC假设IP数据包的最小大小至少为1280字节。这是IPv6的最小大小[IPv6]，也得到了大多数现代IPv4网络的支持。假设IPv6的最小IP头大小为40字节，IPv4为20字节，UDP头大小为8字节，这导致IPv6的最大数据报大小为1232字节，IPv4为1252字节。因此，现代IPv4和所有IPv6网络路径都应该能够支持QUIC。

### 握手最小尺寸

注意：支持1200字节UDP载荷的这一要求限制了IPv6扩展头的可用空间为32字节，或IPv4选项的可用空间为52字节，前提是路径仅支持IPv6最小MTU 1280字节。这会影响Initial数据包和路径验证。

引用结束

QUIC 要求双向的初始数据报至少为 1200 字节，以防止放大攻击并确保 PMTU 在两个方向上都支持它。

我们可以为 Session Request 和 Session Created 要求这个功能，但会显著增加带宽成本。也许我们可以只在没有令牌时，或在收到 Retry 消息后才这样做。待定

QUIC要求Bob在客户端地址验证之前发送的数据不超过接收数据量的三倍。SSU2天然满足这个要求，因为Retry消息与Token Request消息大小相当，并且小于Session Request消息。此外，Retry消息只发送一次。

QUIC要求包含PATH_CHALLENGE或PATH_RESPONSE块的消息至少为1200字节，以防止放大攻击，并确保PMTU在两个方向上都支持它。

我们也可以要求这样做，但会大幅增加带宽成本。不过，这些情况应该很少见。待定

### 路径消息最小大小

IPv4：假设不进行 IP 分片。IP + 数据报头部为 28 字节。这假设没有 IPv4 选项。最大消息大小为 MTU - 28。数据阶段头部为 16 字节，MAC 为 16 字节，总计 32 字节。有效载荷大小为 MTU - 60。对于最大 1500 MTU，最大数据阶段有效载荷为 1440。对于最小 1280 MTU，最大数据阶段有效载荷为 1220。

IPv6：不允许IP分片。IP + 数据报头部为48字节。这假设没有IPv6扩展头部。最大消息大小为MTU - 48。数据阶段头部为16字节，MAC为16字节，总计32字节。载荷大小为MTU - 80。对于最大1500 MTU，最大数据阶段载荷为1420。对于最小1280 MTU，最大数据阶段载荷为1200。

在 SSU 1 中，基于最多 64 个分片和 620 字节最小 MTU，I2NP 消息的严格最大限制约为 32 KB。由于捆绑的 LeaseSet 和会话密钥的开销，应用层的实际限制约低 6KB，即约 26KB。SSU 1 协议允许 128 个分片，但当前实现将其限制为 64 个分片。

### 最大 I2NP 消息大小

通过将最小MTU提高到1280，数据阶段载荷约为1200字节，一个SSU 2消息在64个分片中可达到约76 KB，在128个分片中可达到152 KB。这很容易支持最大64 KB的消息大小。

由于tunnel中的分片以及SSU 2中的分片，消息丢失的概率会随着消息大小呈指数级增长。我们仍然建议在应用层对I2NP数据报保持约10 KB的实际限制。

### 版本

请参阅上述对等测试安全性部分，了解对 SSU1 对等测试的分析以及 SSU2 对等测试的目标。

当被 Bob 拒绝时：

当被Charlie拒绝时：

注意：RI 可能以 I2NP Database Store 消息的形式在 I2NP 块中发送，或者作为 RI 块发送（如果足够小的话）。如果足够小，这些可能包含在与对等测试块相同的数据包中。

消息 1-4 是会话内的，使用数据消息中的对等测试块。消息 5-7 是会话外的，使用对等测试消息中的对等测试块。

## 对等节点测试流程

注意：与SSU 1一样，消息4和5可能以任意顺序到达。如果Alice处于防火墙后面，消息5和/或7可能根本不会被接收到。当消息5在消息4之前到达时，Alice无法立即发送消息6，因为她还没有Charlie的intro key来加密头部。当消息4在消息5之前到达时，Alice不应立即发送消息6，因为她应该等待看消息5是否到达，而不是通过发送消息6来打开防火墙。

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
不支持跨版本节点测试。唯一允许的版本组合是所有节点都使用版本2。

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
4.      <------------------ PeerTest (reject)
```
消息1-4在会话中，由数据阶段的ACK和重传过程覆盖。Peer Test块需要确认应答。

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest (reject)
                      (optional: Bob could try another Charlie here)
4.      <------------------ PeerTest (reject)
```
消息 5-7 可能会被重传，内容不变。

与 SSU 1 中一样，支持 IPv6 地址测试，如果 Bob 和 Charlie 在其发布的 IPv6 地址中用 'B' 能力标识表示支持，那么 Alice-Bob 和 Alice-Charlie 通信可以通过 IPv6 进行。详情请参阅提案 126。

与 0.9.50 版本之前的 SSU 1 一样，Alice 使用现有会话通过她希望测试的传输协议（IPv4 或 IPv6）向 Bob 发送请求。当 Bob 通过 IPv4 收到来自 Alice 的请求时，Bob 必须选择一个公布 IPv4 地址的 Charlie。当 Bob 通过 IPv6 收到来自 Alice 的请求时，Bob 必须选择一个公布 IPv6 地址的 Charlie。实际的 Bob-Charlie 通信可以通过 IPv4 或 IPv6 进行（即，独立于 Alice 的地址类型）。这与 0.9.50 版本的 SSU 1 的行为不同，后者允许混合 IPv4/v6 请求。

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
### 重传

与 SSU 1 不同，Alice 在消息 1 中指定了请求的测试 IP 和端口。Bob 应该验证这个 IP 和端口，如果无效则使用代码 5 拒绝。推荐的 IP 验证是：对于 IPv4，它应该匹配 Alice 的 IP；对于 IPv6，IP 的至少前 8 个字节应该匹配。端口验证应该拒绝特权端口和知名协议端口。

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
### IPv6 注意事项

在这里，我们记录了 Alice 如何根据接收到的消息来确定对等测试的结果。SSU2 的增强功能为我们提供了机会来修复、改进和更好地记录对等测试结果状态机，相比于 [SSU](/docs/transport/ssu) 中的状态机。

对于测试的每种地址类型（IPv4 或 IPv6），结果可以是 UNKNOWN、OK、FIREWALLED 或 SYMNAT 中的一种。此外，还可能执行其他处理来检测 IP 或端口变化，或者外部端口与内部端口不同的情况。

### 由 Bob 处理

已记录的 SSU 状态机存在的问题：

因此，与 SSU 不同的是，我们建议在收到消息 4 后等待几秒钟，然后即使未收到消息 5 也要发送消息 6。

### 结果状态机

基于是否接收到消息4、5和7（是或否），状态机的摘要如下：

### 重传

下面是一个更详细的状态机，其中包含对消息7地址块中接收到的IP/端口的检查。一个挑战是确定是你（Alice）还是Charlie处于对称NAT后面。

建议进行后处理或额外的逻辑处理，通过要求在两个或更多对等测试中获得相同结果来确认状态转换。

建议通过两个或多个测试进行IP/端口验证和确认，或者在Session Created消息中使用地址块，但这超出了本规范的范围。

- 我们永远不会发送消息 6，除非我们收到了消息 5，所以我们永远不知道自己是否是 SYMNAT
- 如果我们确实收到了消息 4 和 7，我们怎么可能是 SYMNAT
- 如果 IP 不匹配但端口匹配，我们就不是 SYMNAT，我们只是改变了 IP

请参见上述中继安全性部分，了解对 SSU1 Relay 的分析以及 SSU2 Relay 的目标。

当被 Bob 拒绝时：

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
当被 Charlie 拒绝时：

注意：RI 可以通过 I2NP 块中的 I2NP Database Store 消息发送，或者作为 RI 块发送（如果足够小）。如果足够小，这些可以包含在与中继块相同的数据包中。

在 SSU 1 中，Charlie 的 router 信息包含每个引入者的 IP、端口、intro key、relay tag 和过期时间。

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
## 中继过程

在 SSU 2 中，Charlie 的 router 信息包含每个引介者的 router 哈希、中继标签和过期时间。

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
Alice应该通过首先选择她已经连接的introducer（Bob）来减少所需的往返次数。其次，如果没有已连接的，则选择她已经拥有router信息的introducer。

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
4.      <-------------- RelayResponse
```
如果可能的话，还应该支持跨版本中继。这将有助于从 SSU 1 到 SSU 2 的渐进式过渡。允许的版本组合包括（待定）：

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
注意：路由信息（RI）可以作为I2NP块中的I2NP数据库存储消息发送，也可以作为RI块发送（如果足够小）。如果足够小，这些可以与中继块包含在同一个数据包中。

请注意，通常情况下，Charlie 会立即对 Relay Intro 响应一个 Relay Response，其中应包含一个 ACK 块。在这种情况下，不需要单独的包含 ACK 块的消息。

Hole punch 可能会被重传，就像在 SSU 1 中一样。

与 I2NP 消息不同，Relay 消息没有唯一标识符，因此必须由 relay 状态机使用 nonce 来检测重复消息。实现可能还需要维护最近使用的 nonce 缓存，以便即使在该 nonce 的状态机完成后也能检测到收到的重复消息。

支持 SSU 1 relay 的所有功能，包括在 [Prop158](/proposals/158-ipv6-transport-enhancements) 中记录的功能，并从 0.9.50 版本开始支持。支持 IPv4 和 IPv6 介绍。可以通过 IPv4 会话发送中继请求以进行 IPv6 介绍，也可以通过 IPv6 会话发送中继请求以进行 IPv4 介绍。

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

以下是与 SSU 1 的差异以及 SSU 2 实现的建议。

在SSU 1中，介绍相对便宜，Alice通常会向所有介绍者发送中继请求。在SSU 2中，介绍更加昂贵，因为必须首先与介绍者建立连接。为了最小化介绍延迟和开销，建议的处理步骤如下：

在 SSU 1 和 SSU 2 中，中继响应和打洞消息可能以任意顺序接收，或者可能根本不会收到。

在 SSU 1 中，Alice 通常会在 Hole Punch（1 1/2 RTT）之前收到 Relay Response（1 RTT）。虽然这些规范中可能没有很好地记录，但 Alice 必须先从 Bob 收到 Relay Response 才能继续，以获得 Charlie 的 IP。如果先收到 Hole Punch，Alice 将无法识别它，因为它不包含数据且源 IP 无法识别。在收到 Relay Response 后，Alice 应该等待从 Charlie 收到 Hole Punch，或者等待一个短暂的延迟（建议 500 毫秒），然后再与 Charlie 开始握手。

### 由 Alice 处理

在 SSU 2 中，Alice 通常会在收到中继响应（2 RTT）之前先收到打洞数据包（1 1/2 RTT）。SSU 2 的打洞数据包比 SSU 1 中的更容易处理，因为它是一个完整的消息，具有定义的连接 ID（从中继随机数派生）和包含 Charlie 的 IP 等内容。中继响应（数据消息）和打洞消息包含相同的已签名中继响应块。因此，Alice 可以在收到来自 Charlie 的打洞数据包或收到来自 Bob 的中继响应中的任一个后，就与 Charlie 发起握手。

### Bob 的标签请求

Hole Punch 的签名验证包含介绍者（Bob）的 router 哈希。如果 Relay 请求已发送给多个介绍者，有几个选项来验证签名：

#### 摘要

如果Charlie位于对称NAT后面，他在中继响应和打洞消息中报告的端口可能不准确。因此，Alice应该检查打洞消息的UDP源端口，如果与报告的端口不同，则使用该端口。

- 根据地址中的 iexp 值忽略任何已过期的引荐者
- 如果已经与一个或多个引荐者建立了 SSU2 连接，选择其中一个并仅向该引荐者发送中继请求。
- 否则，如果本地已知一个或多个引荐者的 Router Info，选择其中一个并仅连接到该引荐者。
- 否则，查找所有引荐者的 Router Info，连接到第一个收到 Router Info 的引荐者。

#### 详细信息

在 SSU 1 中，只有 Alice 可以请求标签，在会话请求中。Bob 永远不能请求标签，Alice 也不能为 Bob 中继。

在 SSU2 中，Alice 通常在会话请求中请求一个标签，但 Alice 或 Bob 也可能在数据阶段请求标签。Bob 在收到入站请求后通常不会被防火墙阻挡，但在中继之后可能会被阻挡，或者 Bob 的状态可能发生变化，或者他可能为其他地址类型（IPv4/v6）请求引导者。因此，在 SSU2 中，Alice 和 Bob 可能同时充当对方的中继。

以下地址属性可能会被发布，与 SSU 1 保持不变，包括自 API 0.9.50 起支持的 [Prop158](/proposals/158-ipv6-transport-enhancements) 中的更改：

已发布的 RouterAddress（RouterInfo 的一部分）将具有 "SSU" 或 "SSU2" 的协议标识符。

- 尝试每个发送请求的哈希值
- 为每个介绍者使用不同的随机数，并利用此来确定这个 Hole Punch 是响应哪个介绍者的
- 如果内容与已收到的 Relay Response 中的内容完全相同，则不要重新验证签名
- 完全不验证签名

RouterAddress 必须包含三个选项来指示 SSU2 支持：

### 地址属性

Alice 必须验证所有三个选项都存在且有效，然后才能使用 SSU2 协议进行连接。

当以"SSU"发布并带有"s"、"i"和"v"选项，以及"host"和"port"选项时，router必须在该主机和端口上接受SSU和SSU2协议的传入连接，并自动检测协议版本。

## 已发布的 Router 信息

### 发布地址

当以"SSU2"发布，带有"s"、"i"和"v"选项，以及"host"和"port"选项时，router仅在该主机和端口上接受SSU2协议的传入连接。

- caps: [B,C,4,6] 能力
- host: IP (IPv4 或 IPv6)。允许缩写的 IPv6 地址（带有 "::"）。如果有防火墙可能存在也可能不存在。不允许主机名。
- iexp[0-2]: 此 introducer 的过期时间。ASCII 数字，自纪元以来的秒数。仅在有防火墙且需要 introducer 时存在。可选（即使此 introducer 的其他属性存在）。
- ihost[0-2]: Introducer 的 IP (IPv4 或 IPv6)。允许缩写的 IPv6 地址（带有 "::"）。仅在有防火墙且需要 introducer 时存在。不允许主机名。仅限 SSU 地址。
- ikey[0-2]: Introducer 的 Base 64 introduction key。仅在有防火墙且需要 introducer 时存在。仅限 SSU 地址。
- iport[0-2]: Introducer 的端口 1024 - 65535。仅在有防火墙且需要 introducer 时存在。仅限 SSU 地址。
- itag[0-2]: Introducer 的标签 1 - (2**32 - 1) ASCII 数字。仅在有防火墙且需要 introducer 时存在。
- key: Base 64 introduction key。
- mtu: 可选。见上面的 MTU 部分。
- port: 1024 - 65535 如果有防火墙可能存在也可能不存在。

### 未发布的 SSU2 地址

如果一个 router 同时支持 SSU1 和 SSU2 连接，但没有实现传入连接的自动版本检测，则必须同时发布 "SSU" 和 "SSU2" 地址，并且只在 "SSU2" 地址中包含 SSU2 选项。router 应该在 "SSU2" 地址中设置较低的成本值（更高的优先级），而不是在 "SSU" 地址中，以便优先选择 SSU2。

如果在同一个 RouterInfo 中发布了多个 SSU2 RouterAddress（无论是"SSU"还是"SSU2"）（用于额外的 IP 地址或端口），所有指定相同端口的地址必须包含相同的 SSU2 选项和值。特别是，所有地址都必须包含相同的静态密钥"s"和介绍密钥"i"。

- s=（Base64 密钥）此 RouterAddress 的当前 Noise 静态公钥 (s)。使用标准 I2P Base 64 字母表进行 Base 64 编码。二进制格式为 32 字节，Base 64 编码格式为 44 字节，小端序 X25519 公钥。
- i=（Base64 密钥）用于加密此 RouterAddress 头部的当前介绍密钥。使用标准 I2P Base 64 字母表进行 Base 64 编码。二进制格式为 32 字节，Base 64 编码格式为 44 字节，大端序 ChaCha20 密钥。
- v=2 当前版本 (2)。当以 "SSU" 发布时，暗示对版本 1 的额外支持。对未来版本的支持将使用逗号分隔的值，例如 v=2,3。实现应验证兼容性，如果存在逗号则包括多个版本。逗号分隔的版本必须按数字顺序排列。

当发布为带有introducers的SSU或SSU2时，存在以下选项：

以下选项仅适用于SSU，不用于SSU2。在SSU2中，Alice从Charlie的RI中获取此信息。

router在发布introducers时不得在地址中发布主机或端口。router在发布introducers时必须在地址中发布4和/或6 caps，以表明对IPv4和/或IPv6的支持。这与当前SSU 1地址的实践相同。

注意：如果以SSU方式发布，且存在SSU 1和SSU2 introducers的混合情况，为了与旧版router兼容，SSU 1 introducers应该位于较低的索引位置，而SSU2 introducers应该位于较高的索引位置。

如果Alice没有发布她的SSU2地址（作为"SSU"或"SSU2"）用于接收连接，她必须发布一个"SSU2" router地址，该地址仅包含她的静态密钥和SSU2版本，以便Bob在Session Confirmed第2部分中收到Alice的RouterInfo后可以验证该密钥。

#### 错误处理

此router地址将不包含"host"或"port"选项，因为出站SSU2连接不需要这些选项。此地址的发布成本并不严格重要，因为它仅用于入站连接；但是，如果将成本设置得比其他地址更高（优先级更低），可能对其他router有帮助。建议值为14。

- ih[0-2]=(Base64 hash) 一个引荐者的 router 哈希。使用标准 I2P Base 64 字母表进行 Base 64 编码。二进制格式为 32 字节，Base 64 编码格式为 44 字节
- iexp[0-2]: 此引荐者的过期时间。与 SSU 1 保持不变。
- itag[0-2]: 引荐者的标签 1 - (2**32 - 1) 与 SSU 1 保持不变。

Alice也可以简单地在现有已发布的"SSU"地址中添加"i"、"s"和"v"选项。

- ihost[0-2]
- ikey[0-2]
- itag[0-2]

允许为 NTCP2 和 SSU2 使用相同的静态密钥，但不推荐这样做。

由于 RouterInfo 的缓存机制，router 在运行期间不得轮换静态公钥或 IV，无论是否在已发布的地址中。Router 必须持久化存储此密钥和 IV 以便在立即重启后重用，这样传入连接将继续工作，且重启时间不会被暴露。Router 必须持久化存储或以其他方式确定上次关闭时间，以便在启动时计算先前的停机时间。

### 公钥和初始化向量轮换

考虑到暴露重启时间的担忧，如果 router 之前已经下线了一段时间（至少几天），router 可以在启动时轮换此密钥或 IV。

- s=(Base64 key) 如上所述，用于已发布地址。
- i=(Base64 key) 如上所述，用于已发布地址。
- v=2 如上所述，用于已发布地址。

如果 router 有任何已发布的 SSU2 RouterAddresses（作为 SSU 或 SSU2），则轮换前的最小停机时间应该更长，例如一个月，除非本地 IP 地址已更改或 router "重新生成密钥"。

如果router发布了任何SSU RouterAddresses，但没有SSU2（作为SSU或SSU2），则轮换前的最小停机时间应该更长，例如一天，除非本地IP地址已更改或router"重新生成密钥"。即使发布的SSU地址有介绍者，这一点也适用。

### 出站数据包创建

如果 router 没有任何已发布的 RouterAddresses（SSU、SSU2 或 SSU），那么轮换前的最短停机时间可能只需两小时，即使 IP 地址发生变化，除非 router 执行"rekeys"操作。

如果 router "重新生成密钥" 到不同的 Router Hash，它也应该生成新的噪声密钥和介绍密钥。

实现必须意识到，更改静态公钥或初始化向量(IV)将阻止来自缓存了较旧RouterInfo的router的传入SSU2连接。RouterInfo发布、tunnel对等体选择（包括OBGW和IB最近跳）、零跳tunnel选择、传输选择以及其他实现策略都必须考虑到这一点。

Intro 密钥轮换遵循与密钥轮换相同的规则。

注意：重新生成密钥前的最短停机时间可能会被修改，以确保网络健康，并防止因适度停机时间而导致的 router 重新获取种子。

否认性不是一个目标。请参见上述概述。

每个模式都被分配了属性，描述了为发起者的静态公钥和响应者的静态公钥提供的机密性。基本假设是临时私钥是安全的，并且如果各方从对方收到他们不信任的静态公钥，他们会中止握手。

本节仅考虑通过握手中静态公钥字段导致的身份泄露。当然，Noise 参与者的身份可能通过其他方式暴露，包括载荷字段、流量分析或如 IP 地址等元数据。

Alice：(8) 使用前向保密加密到已认证方。

Bob: (3) 不会传输，但被动攻击者可以检查响应者私钥的候选值并确定候选值是否正确。

#### 身份隐藏

Bob 在 netDb 中发布他的静态公钥。Alice 可能不会这样做，但必须将其包含在发送给 Bob 的 RI 中。

握手消息（会话请求/已创建/已确认、重试）基本步骤，按顺序：

数据阶段消息基本步骤，按顺序：

所有入站消息的初始处理：

握手消息（Session Request/Created/Confirmed、Retry、Token Request）和其他会话外消息（Peer Test、Hole Punch）处理：

数据阶段消息处理：

## 数据包指南

### 入站数据包处理

在 SSU 1 中，入站数据包分类很困难，因为没有头部来指示会话编号。router 必须首先将源 IP 和端口与现有的对等节点状态进行匹配，如果找不到，则尝试使用不同密钥进行多次解密，以找到合适的对等节点状态或启动新的会话。如果现有会话的源 IP 或端口发生变化（可能由于 NAT 行为），router 可能会使用昂贵的启发式算法来尝试将数据包与现有会话匹配并恢复内容。

- 创建 16 或 32 字节头部
- 创建载荷
- mixHash() 头部（Retry 除外）
- 使用 Noise 加密载荷（Retry 除外，使用 ChaChaPoly 并以头部作为 AD）
- 加密头部，对于 Session Request/Created，还要加密临时密钥

SSU 2 设计旨在最小化入站数据包分类工作，同时保持 DPI 抗性和其他路径威胁防护。连接 ID 号码包含在所有消息类型的头部中，并使用 ChaCha20 以已知密钥和随机数进行加密（混淆）。此外，消息类型也包含在头部中（使用头部保护加密到已知密钥，然后用 ChaCha20 混淆），可用于额外分类。在任何情况下都不需要试验性 DH 或其他非对称加密操作来分类数据包。

- 创建16字节头部
- 创建负载
- 使用ChaChaPoly加密负载，将头部作为AD
- 加密头部

### 注释

#### 摘要

对于来自所有对等节点的几乎所有消息，用于连接 ID 加密的 ChaCha20 密钥是目标 router 在 netDb 中发布的介绍密钥。

- 使用 intro key 解密头部的前 8 字节（目标连接 ID）
- 通过目标连接 ID 查找连接
- 如果找到连接且处于数据阶段，则进入数据阶段部分
- 如果未找到连接，则进入握手部分
- 注意：Peer Test 和 Hole Punch 消息也可能通过从测试或中继 nonce 创建的目标连接 ID 进行查找。

唯一的例外是 Bob 发送给 Alice 的第一条消息（Session Created 或 Retry），此时 Bob 还不知道 Alice 的 introduction key。在这些情况下，使用 Bob 的 introduction key 作为密钥。

- 使用 intro key 解密头部的字节 8-15（包类型、版本和网络 ID）。如果是有效的 Session Request、Token Request、Peer Test 或 Hole Punch，继续
- 如果不是有效消息，通过数据包源 IP/端口查找待处理的出站连接，将数据包视为 Session Created 或 Retry。使用正确的密钥重新解密头部的前 8 个字节，以及头部的字节 8-15（包类型、版本和网络 ID）。如果是有效的 Session Created 或 Retry，继续
- 如果不是有效消息，失败，或将其排队作为可能的乱序数据阶段数据包
- 对于 Session Request/Created、Retry、Token Request、Peer Test 和 Hole Punch，解密头部的字节 16-31
- 对于 Session Request/Created，解密临时密钥
- 验证所有头部字段，如果无效则停止
- mixHash() 头部
- 对于 Session Request/Created/Confirmed，使用 Noise 解密载荷
- 对于 Retry 和数据阶段，使用 ChaChaPoly 解密载荷
- 处理头部和载荷

该协议旨在最小化可能需要在多个回退步骤中进行额外加密操作或复杂启发式处理的数据包分类处理。此外，绝大多数接收到的数据包不需要通过源IP/端口进行（可能昂贵的）回退查找和二次报头解密。只有Session Created和Retry（以及可能其他待定的）才需要回退处理。如果端点在会话创建后改变IP或端口，连接ID仍然用于查找会话。永远不需要使用启发式方法来查找会话，例如通过寻找相同IP但不同端口的不同会话。

- 使用正确的密钥解密报头的第8-15字节（数据包类型、版本和网络ID）
- 使用ChaChaPoly解密载荷，将报头作为AD（附加数据）
- 处理报头和载荷

#### 详细信息

因此，接收器循环逻辑中推荐的处理步骤如下：

1) 使用本地引入密钥通过 ChaCha20 解密前 8 个字节，以恢复目标连接 ID。如果连接 ID 与当前或待处理的入站会话匹配：

2) 如果连接ID与当前会话不匹配：检查字节8-15处的明文头部是否有效（无需执行任何头部保护操作）。验证网络ID和协议版本是否有效，以及消息类型是否为Session Request或其他允许在会话外使用的消息类型（待定）。

3) 通过数据包的源 IP/端口查找待处理的出站会话。

4) 如果在同一端口上运行 SSU 1，尝试将消息作为 SSU 1 数据包进行处理。

一般来说，会话（无论是在握手阶段还是数据阶段）都不应该在接收到包含意外消息类型的数据包后被销毁。这可以防止数据包注入攻击。当头部解密密钥不再有效时，重传握手数据包后也经常会收到这些数据包。

在大多数情况下，简单地丢弃数据包。实现可以（但不是必须）重新传输之前发送的数据包（握手消息或 ACK 0）作为响应。

    a)  Using the appropriate key, decrypt the header bytes 8-15 to recover the version, net ID, and message type.
    b)  If the message type is Session Confirmed, it is a long header. Verify the net ID and protocol version are valid. Decrypt the bytes 15-31 of the header with ChaCha20 using the local intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise.
    c)  If the message type is valid but not Session Confirmed, it is a short header. Verify the net ID and protocol version are valid. decrypt the rest of the message with ChaCha20/Poly1305 using the session key, using the decrypted 16-byte header as the AD.
    d)  (optional) If connection ID is a pending inbound session awaiting a Session Confirmed message, but the net ID, protocol, or message type is not valid, it could be a Data message received out-of-order before the Session Confirmed, so the data phase header protection keys are not yet known, and the header bytes 8-15 were incorrectly decrypted. Queue the message, and attempt to decrypt it once the Session Confirmed message is received.
    e)  If b) or c) fails, drop the message.

作为Bob发送Session Created后，意外的数据包通常是由于Session Confirmed数据包丢失或乱序而无法解密的Data数据包。将这些数据包排队，并在收到Session Confirmed数据包后尝试解密它们。

    a)  If all is valid and the message type is Session Request, decrypt bytes 16-31 of the header and the 32-byte X value with ChaCha20 using the local intro key.

    - If the token at header bytes 24-31 is accepted, then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Created in response.
    - If the token is not accepted, send a Retry message to the source IP/port with a token. Do not attempt to decrypt the message with Noise to avoid DDoS attacks.

    b)  If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.
    c)  If a) or b) fails, go to step 3)

作为Bob接收到Session Confirmed后，意外的数据包通常是重传的Session Confirmed数据包，这是因为Session Confirmed的ACK 0丢失了。这些意外的数据包可能会被丢弃。实现可以（但不是必须）发送包含ACK块的Data数据包作为响应。

    a)  If found, re-decrypt the first 8 bytes with ChaCha20 using Bob's introduction key to recover the Destination Connection ID.
    b)  If the connection ID matches the pending session: Using the correct key, decrypt bytes 8-15 of the header to recover the version, net ID, and message type. Verify the net ID and protocol version are valid, and the message type is Session Created or Retry, or other message type allowed out-of-session (TBD).

    - If all is valid and the message type is Session Created, decrypt the next 16 bytes of the header and the 32-byte Y value with ChaCha20 using Bob's intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Confirmed in response.
    - If all is valid and the message type is Retry, decrypt bytes 16-31 of the header with ChaCha20 using Bob's intro key. Decrypt and validate the message using ChaCha20/Poly1305 using TBD as the key and TBD as the nonce and the decrypted 32-byte header as the AD. Resend a Session Request with the received token in response.
    - If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.

    > c)  If a pending outbound session is not found, or the connection ID does not match the pending session, drop the message, unless the port is shared with SSU 1.

对于 Session Created 和 Session Confirmed，实现必须仔细验证所有解密的头部字段（Connection ID、数据包编号、数据包类型、版本、id、frag 和 flags），然后再对头部调用 mixHash() 并尝试使用 Noise AEAD 解密负载。如果 Noise AEAD 解密失败，则不得进行进一步处理，因为 mixHash() 会损坏握手状态，除非实现存储并"回退"哈希状态。

#### 错误处理

可能无法在同一入站端口上有效检测传入数据包是版本1还是版本2。上述步骤可能需要在SSU 1处理之前执行，以避免尝试使用两种协议版本进行试验性DH操作。

如有需要将待定。

假设使用IPv4，不包括额外填充，不包括IP和UDP头部大小。填充是仅适用于SSU 1的mod-16填充。

**SSU 1**

### 版本检测

**SSU 2**

### 令牌

我们在上面指定 token 必须是一个随机生成的 8 字节值，而不是生成不透明的值（如服务器密钥和 IP、端口的哈希值或 HMAC），这是为了避免重用攻击。然而，这需要临时存储（以及可选的持久存储）已交付的 token。[WireGuard](https://www.wireguard.com/papers/wireguard.pdf) 使用服务器密钥和 IP 地址的 16 字节 HMAC，服务器密钥每两分钟轮换一次。我们应该研究类似的方案，但使用更长的服务器密钥生命周期。如果我们在 token 中嵌入时间戳，这可能是一个解决方案，但 8 字节的 token 可能不够大来容纳这些信息。

待定是否需要。

## 推荐常量

- 出站握手重传超时：1.25秒，采用指数退避算法（重传时间点为1.25、3.75和8.75秒）
- 出站握手总超时：15秒
- 入站握手重传超时：1秒，采用指数退避算法（重传时间点为1、3和7秒）
- 入站握手总超时：12秒
- 发送重试后超时：9秒
- ACK延迟：max(10, min(rtt/6, 150)) 毫秒
- 立即ACK延迟：min(rtt/16, 5) 毫秒
- 最大ACK范围：256？
- 最大ACK深度：512？
- 填充分布：0-15字节，或更多
- 数据阶段最小重传超时：1秒，如[RFC-6298](https://tools.ietf.org/html/rfc6298)所述
- 另请参阅[RFC-6298](https://tools.ietf.org/html/rfc6298)获取数据阶段重传定时器的额外指导。

## 数据包开销分析

假设为 IPv4，不包括额外填充，不包括 IP 和 UDP 头部大小。填充仅针对 SSU 1 采用模 16 填充。

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
## 问题和未来工作

### 令牌

我们上述规定，该令牌必须是一个随机生成的 8 字节值，而不应生成诸如服务器密钥与 IP、端口的哈希或 HMAC 这类不透明的值，以防止重放攻击。然而，这种方法需要临时（以及可选地）持久存储已发放的令牌。[WireGuard](https://www.wireguard.com/papers/wireguard.pdf) 使用一个 16 字节的 HMAC，其基于服务器密钥和 IP 地址生成，并且服务器密钥每两分钟轮换一次。我们应该研究类似的方法，但采用更长的服务器密钥有效期。如果我们在令牌中嵌入时间戳，这可能是一种解决方案，但 8 字节的令牌可能不足以容纳时间戳信息。

## 参考文献

- **[Common]** [通用结构规范](/docs/specs/common-structures)
- **[ECIES]** [ECIES-X25519-AEAD-Ratchet 规范](/docs/specs/ecies)
- **[NetDB]** [网络数据库](/docs/overview/network-database)
- **[NOISE]** [Noise 协议框架](https://noiseprotocol.org/noise.html)
- **[Nonces]** [无视 Nonce 的对手](https://eprint.iacr.org/2019/624.pdf)
- **[NTCP]** [NTCP 传输](/docs/transport/ntcp)
- **[NTCP2]** [NTCP2 规范](/docs/specs/ntcp2)
- **[PMTU]** [路径 MTU 发现](https://en.wikipedia.org/wiki/Path_MTU_Discovery)
- **[Prop104]** [提案 104: TLS 传输](/proposals/104-tls-transport)
- **[Prop109]** [提案 109: 可插拔传输](/proposals/109-pt-transport)
- **[Prop158]** [提案 158: IPv6 传输增强](/proposals/158-ipv6-transport-enhancements)
- **[Prop159]** [提案 159: SSU2](/proposals/159-ssu2)
- **[RFC-2104]** [RFC 2104: HMAC](https://tools.ietf.org/html/rfc2104)
- **[RFC-3449]** [RFC 3449: TCP 性能影响](https://tools.ietf.org/html/rfc3449)
- **[RFC-3526]** [RFC 3526: MODP 组](https://tools.ietf.org/html/rfc3526)
- **[RFC-5681]** [RFC 5681: TCP 拥塞控制](https://tools.ietf.org/html/rfc5681)
- **[RFC-5869]** [RFC 5869: HKDF](https://tools.ietf.org/html/rfc5869)
- **[RFC-6151]** [RFC 6151: MD5 安全注意事项](https://tools.ietf.org/html/rfc6151)
- **[RFC-6298]** [RFC 6298: TCP 重传定时器](https://tools.ietf.org/html/rfc6298)
- **[RFC-6437]** [RFC 6437: IPv6 流标签](https://tools.ietf.org/html/rfc6437)
- **[RFC-7539]** [RFC 7539: ChaCha20/Poly1305](https://tools.ietf.org/html/rfc7539)
- **[RFC-7748]** [RFC 7748: 安全椭圆曲线](https://tools.ietf.org/html/rfc7748)
- **[RFC-7905]** [RFC 7905: TLS 的 ChaCha20-Poly1305 密码套件](https://tools.ietf.org/html/rfc7905)
- **[RFC-9000]** [RFC 9000: QUIC 传输协议](https://datatracker.ietf.org/doc/html/rfc9000)
- **[RFC-9001]** [RFC 9001: 使用 TLS 保护 QUIC](https://datatracker.ietf.org/doc/html/rfc9001)
- **[RFC-9002]** [RFC 9002: QUIC 丢包检测和拥塞控制](https://datatracker.ietf.org/doc/html/rfc9002)
- **[RouterAddress]** [RouterAddress 结构](/docs/specs/common-structures#struct-routeraddress)
- **[RouterIdentity]** [RouterIdentity 结构](/docs/specs/common-structures#struct-routeridentity)
- **[SigningPublicKey]** [SigningPublicKey 类型](/docs/specs/common-structures#type-signingpublickey)
- **[SSU]** [SSU 传输](/docs/transport/ssu)
- **[STS]** [站对站协议](https://en.wikipedia.org/wiki/Station-to-Station_protocol)
- **[Ticket1112]** [I2P 工单 1112](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1112)
- **[Ticket1849]** [I2P 工单 1849](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1849)
- **[WireGuard]** [WireGuard 协议](https://www.wireguard.com/papers/wireguard.pdf)
