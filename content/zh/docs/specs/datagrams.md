---
title: "数据报规范"
description: "I2P 数据报消息格式规范，包括原始、可回复和认证类型"
slug: "datagrams"
category: "协议"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

## 概述

参阅 [Datagrams API 文档](/docs/api/datagrams/) 了解 Datagrams API 的概述。

定义了以下类型。列出了标准协议号，但是除了流协议号 (6) 之外，可以使用任何其他协议号，具体取决于应用程序。

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
各种 router 和库实现中对 Datagram2 和 Datagram3 的支持情况待定。请查看这些实现的相关文档。

### 数据报类型识别

四种数据报类型在协议版本字段的位置上没有共同的头部格式。无法根据数据包内容识别其类型。当在同一会话中使用多种类型，或将单一类型与流式传输一起使用时，应用程序必须使用协议号和/或I2CP/SAM端口将传入数据包路由到正确位置。使用标准协议号将使此过程更加容易。不建议不设置协议号（0或PROTO_ANY），即使是仅使用数据报的应用程序，因为这会增加路由错误的可能性，并使升级到多协议应用程序变得更加困难。数据报2和数据报3中的版本字段仅作为路由错误的附加检查和未来变更的准备。

### 应用程序设计

所有数据报的使用都是特定于应用程序的。

由于认证数据报带有相当大的开销，典型的应用程序会同时使用认证和非认证数据报。一个典型的设计是从客户端向服务器发送一个包含令牌的认证数据报。服务器用包含相同令牌的非认证数据报进行回复。在令牌超时之前的任何后续通信都使用原始数据报。

应用程序通过 [I2CP](/docs/specs/i2cp/) API 或 [SAMv3](/docs/api/samv3/) 使用协议和端口号发送和接收数据报。

当然，数据报是不可靠的。应用程序必须为不可靠传输进行设计。在I2P内部，如果下一跳可达，逐跳传输是可靠的，因为NTCP2和SSU2传输协议提供了可靠性。然而，端到端传输并不可靠，因为I2NP消息可能会在任何跳内因队列限制、过期、超时、带宽限制或下一跳不可达而被丢弃。

### 数据报大小

I2NP消息（包括数据报）的标称大小限制为64 KB。Garlic和tunnel消息开销会在一定程度上减少这个限制。

然而，所有I2NP消息都必须分片为1 KB的tunnel消息。一个n KB的I2NP消息的丢失概率是单个tunnel消息丢失概率的指数函数，即p ** n。由于分片会导致tunnel消息的突发传输，实际的丢失概率要比指数函数所暗示的高得多，这是由于router实现中的队列限制和主动队列管理（AQM、CoDel或类似技术）造成的。

为确保可靠传输，建议的典型最大大小为几KB，最多10KB。通过仔细分析所有协议层（传输层除外）的开销大小，开发者应该设置一个最大负载大小，使其能够精确地适配到一个、两个或三个 tunnel 消息中。这将最大化效率和可靠性。各层的开销包括gzip头、I2NP头、garlic消息头、garlic encryption、tunnel消息头、tunnel消息分片头等。请参见[提案144](/proposals/144-ecies-x25519-aead-ratchet/)中的流式传输MTU计算和Java I2P源码中的ConnectionOptions.java以获取示例。

### SAM 注意事项

应用程序通过 I2CP API 或 SAM 使用协议和端口号发送和接收数据报。通过 SAM 指定协议和端口号需要 SAM v3.2 或更高版本。在同一个 SAM 会话（tunnel）上同时使用数据报和流传输（UDP 和 TCP）需要 SAM v3.3 或更高版本。在同一个 SAM 会话（tunnel）上使用多种数据报类型需要 SAM v3.3 或更高版本。目前只有 Java I2P router 支持 SAM v3.3。

各种 router 和库实现中对 Datagram2 和 Datagram3 的 SAM 支持待定。请查看这些实现的文档。

请注意，如果大小超过典型的1500字节网络MTU，将阻止SAM应用程序在应用程序和服务器位于不同计算机时向/从SAM服务器传输未分片的数据包。通常情况下并非如此，它们都在localhost上，其中MTU为65536或更高。如果SAM应用程序预期与服务器分离在不同的计算机上，可回复数据报的最大载荷略低于1KB。

### PQ 考虑因素

如果实现了后量子[提案 169](/proposals/169-pq-crypto/)的 MLDSA 部分，开销将大幅增加。目的地 + 签名的大小将从 391 + 64 = 455 字节增加到 MLDSA44 的最小值 3739 字节和 MLDSA87 的最大值 7226 字节。这种变化的实际影响有待确定。由 router 提供身份验证的 Datagram3 可能是一个解决方案。

## 原始（不可回复）数据报 {#raw}

不可回复的数据报没有"发送方"地址且未经身份验证。它们也被称为"原始"数据报。严格来说，它们根本不是"数据报"，只是原始数据。它们不由数据报API处理。然而，SAM和I2PTunnel类支持"原始数据报"。

原始数据报的标准 I2CP 协议号是 PROTO_DATAGRAM_RAW (18)。

格式在这里没有指定，它是由应用程序定义的。为了完整性，我们在下面包含了格式的图片。

### 格式

```
+----+----+----+----+----//
| payload...
+----+----+----+----+----//

length: 0 - about 64 KB (see notes)
```
### 注释

实际长度受到各层开销和可靠性的限制。

## Datagram1 (可回复) {#repliable}

可回复数据报包含"from"地址和签名。这些至少增加427字节的开销。

可回复数据报的标准 I2CP 协议编号是 PROTO_DATAGRAM (17)。

### 格式

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
### 注释

- 实际长度受到各层开销和可靠性的限制。
- 请参阅 [Datagrams API 文档](/docs/api/datagrams/) 中关于大数据报可靠性的重要说明。为获得最佳效果，请将负载限制在约 10 KB 或更少。
- DSA_SHA1 以外类型的签名在 0.9.14 版本中被重新定义。
- 该格式不支持为 LS2 包含离线签名块（提案 123）。必须为此定义一个带有标志的新协议。

## Datagram2 {#datagram2}

Datagram2 格式按照 [提案 163](/proposals/163-datagram2/) 中的规范。Datagram2 的 I2CP 协议号是 19。

Datagram2 旨在作为 Datagram1 的替代方案。它在 Datagram1 的基础上增加了以下功能：

- 重放攻击防护
- 离线签名支持
- 用于扩展性的标志和选项字段

请注意，Datagram2 的签名计算算法与 Datagram1 有本质区别。

### 格式

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
总长度：最小 433 + 载荷长度；X25519 发送方且无离线签名的典型长度：457 + 载荷长度。注意消息通常会在 I2CP 层使用 gzip 压缩，如果发送方目标地址可压缩，这将显著节省空间。

注意：离线签名格式与[通用结构规范](/docs/specs/common-structures/)和[流式传输规范](/docs/specs/streaming/)中的格式相同。

### 签名

签名覆盖以下字段：

- Prelude: 目标目的地的32字节哈希值（不包含在数据报中）
- flags
- options（如果存在）
- offline_signature（如果存在）
- payload

在可回复数据报中，对于 DSA_SHA1 密钥类型，签名是基于载荷的 SHA-256 哈希值，而不是载荷本身；在这里，签名始终基于上述字段（不是哈希值），无论密钥类型如何。

### ToHash 验证

接收方必须验证签名（使用其目标哈希）并在失败时丢弃数据报，以防止重放攻击。

## Datagram3 {#datagram3}

Datagram3 格式如 [Proposal 163](/proposals/163-datagram2/) 中所规定。Datagram3 的 I2CP 协议号为 20。

Datagram3 旨在作为原始数据报的增强版本。它为原始数据报添加了以下功能：

- 可重复性
- 用于扩展性的标志和选项字段

Datagram3 没有经过身份验证。在未来的提案中，身份验证可能由 router 的棘轮层提供，身份验证状态将传递给客户端。

### 格式

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
总长度：最小34 + 有效载荷长度。

## 参考资料

- [Common](/docs/specs/common-structures/) - 通用结构规范
- [DATAGRAMS](/docs/api/datagrams/) - Datagrams API 概述
- [I2CP](/docs/specs/i2cp/) - I2CP 规范
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet/) - ECIES-X25519-AEAD-Ratchet 提案
- [Prop163](/proposals/163-datagram2/) - Datagram2 和 Datagram3 提案
- [Prop169](/proposals/169-pq-crypto/) - 后量子密码学提案
- [SAMv3](/docs/api/samv3/) - SAM v3 规范
- [Streaming](/docs/specs/streaming/) - 流传输规范
- [TRANSPORT](/docs/overview/transport/) - 传输概述
- [TUNMSG](/docs/specs/tunnel-message/#notes) - tunnel 消息规范
