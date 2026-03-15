---
title: "RI 和目标填充"
number: "161"
author: "zzz"
created: "2022-09-28"
lastupdated: "2023-01-02"
status: "开放"
thread: "http://zzz.i2p/topics/3279"
target: "0.9.57"
toc: true
---
## 状态

已在 0.9.57 版本中实现。  
保留本提案开放，以便我们进一步增强并讨论“未来规划”部分中的想法。

## 概述

### 摘要

自 0.6 版本（2005 年）以来，Destination 中的 ElGamal 公钥一直未被使用。  
虽然我们的规范确实说明该字段未被使用，但**并未说明**实现可以避免生成 ElGamal 密钥对，而仅用随机数据填充该字段。

我们提议修改规范，明确指出该字段将被忽略，且实现**可以**用随机数据填充该字段。  
此更改是向后兼容的。目前没有已知的实现会验证 ElGamal 公钥。

此外，本提案为实现者提供指导，说明如何生成 Destination 和路由器身份（Router Identity）的填充数据，使其在保持安全性的同时具备良好的可压缩性，并避免 Base64 表示形式看起来像是损坏或不安全的。  
这在不进行破坏性协议变更的前提下，提供了移除填充字段的大部分好处。  
可压缩的 Destination 可减少流式 SYN 和可回复数据报的大小；可压缩的 Router Identity 可减少数据库存储消息、SSU2 Session Confirmed 消息以及 reseed su3 文件的大小。

最后，本提案讨论了新的 Destination 和 Router Identity 格式可能性，这些格式将彻底消除填充字段。同时也简要讨论了后量子密码学（post-quantum crypto）及其对未来规划的潜在影响。

### 目标

- 消除为 Destination 生成 ElGamal 密钥对的要求  
- 推荐最佳实践，使 Destination 和 Router Identity 高度可压缩，同时在 Base64 表示中不显示明显模式  
- 鼓励所有实现采用最佳实践，使这些字段无法被区分  
- 减少流式 SYN 大小  
- 减少可回复数据报大小  
- 减少 SSU2 RI 块大小  
- 减少 SSU2 Session Confirmed 大小和分片频率  
- 减少包含 RI 的数据库存储消息大小  
- 减少 reseed 文件大小  
- 在所有协议和 API 中保持兼容性  
- 更新规范  
- 讨论新的 Destination 和 Router Identity 格式的替代方案  

通过消除生成 ElGamal 密钥的要求，实现可能能够完全移除 ElGamal 代码，具体取决于其他协议中的向后兼容性考虑。

## 设计

严格来说，32 字节的签名公钥（在 Destination 和 Router Identity 中均有）以及 32 字节的加密公钥（仅在 Router Identity 中）本身就是提供足够熵的随机数，足以确保这些结构的 SHA-256 哈希在网络数据库 DHT 中具有密码学强度和随机分布。

然而，出于谨慎考虑，我们建议在 ElG 公钥字段和填充字段中至少使用 32 字节的随机数据。此外，如果这些字段全为零，则 Base64 表示的 Destination 将包含大量连续的 AAAA 字符，可能引起用户警觉或困惑。

对于 Ed25519 签名类型和 X25519 加密类型：  
Destination 将包含该随机数据的 11 份副本（352 字节）。  
Router Identity 将包含该随机数据的 10 份副本（320 字节）。

### 预计节省

Destination 包含在每个流式 SYN 和可回复数据报中。  
Router Info（包含 Router Identity）包含在数据库存储消息以及 NTCP2 和 SSU2 的 Session Confirmed 消息中。

NTCP2 不压缩 Router Info。  
数据库存储消息和 SSU2 Session Confirmed 消息中的 RIs 会被 gzip 压缩。  
reseed SU3 文件中的 Router Infos 被 zip 压缩。

数据库存储消息中的 Destination 不被压缩。  
流式 SYN 消息在 I2CP 层被 gzip 压缩。

对于 Ed25519 签名类型和 X25519 加密类型，预计节省如下：

| 数据类型 | 总大小 | 密钥和证书 | 未压缩填充 | 压缩后填充 | 大小 | 节省 |
|-----------|------------|---------------|----------------------|--------------------|------|---------|
| Destination | 391 | 39 | 352 | 32 | 71 | 320 字节 (82%) |
| Router Identity | 391 | 71 | 320 | 32 | 103 | 288 字节 (74%) |
| Router Info | 1000 典型 | 71 | 320 | 32 | 722 典型 | 288 字节 (29%) |

注：假设 7 字节证书不可压缩，且无额外 gzip 开销。  
这两点均不完全准确，但影响很小。  
忽略 Router Info 中其他可压缩部分。

## 规范

以下是我们当前规范的建议变更。

### 通用结构
修改通用结构规范，明确指出 256 字节的 Destination 公钥字段将被忽略，且可包含随机数据。

在通用结构规范中新增一节，推荐 Destination 公钥字段以及 Destination 和 Router Identity 中填充字段的最佳实践，如下所示：

使用强加密伪随机数生成器（PRNG）生成 32 字节的随机数据，并将这 32 字节重复填充至公钥字段（用于 Destination）和填充字段（用于 Destination 和 Router Identity）。

### 私钥文件
私钥文件格式（eepPriv.dat）并非我们规范的正式部分，但它在 [Java I2P javadocs](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html) 中有文档记录，其他实现也支持该格式。  
这使得私钥可在不同实现之间移植。  
在该 javadoc 中添加注释：加密公钥可以是随机填充，加密私钥可以是全零或随机数据。

### SAM
在 SAM 规范中注明：加密私钥未被使用，可被忽略。  
客户端可返回任意随机数据。  
SAM Bridge 在创建时（使用 DEST GENERATE 或 SESSION CREATE DESTINATION=TRANSIENT）可发送随机数据而非全零，以避免 Base64 表示中出现 AAAA 字符串而显得异常。

### I2CP
I2CP 无需更改。Destination 中加密公钥对应的私钥不会发送给路由器。

## 未来规划

### 协议变更

以协议变更和失去向后兼容性为代价，我们可以更改协议和规范，彻底移除 Destination、Router Identity 或两者中的填充字段。

该提案与“b33”加密 leaseset 格式有相似之处，仅包含密钥和类型字段。

为保持一定兼容性，某些协议层可在传递给其他协议层前“扩展”填充字段为全零。

对于 Destination，我们还可以从密钥证书中移除加密类型字段，节省 2 字节。  
或者，Destination 可获得一个新的加密类型，表示公钥为零（及填充）。

如果在某协议层未包含新旧格式之间的兼容转换，则以下规范、API、协议和应用将受到影响：

- 通用结构规范  
- I2NP  
- I2CP  
- NTCP2  
- SSU2  
- Ratchet  
- 流式传输  
- SAM  
- BitTorrent  
- 重种子（Reseeding）  
- 私钥文件  
- Java 核心和路由器 API  
- i2pd API  
- 第三方 SAM 库  
- 捆绑和第三方工具  
- 多个 Java 插件  
- 用户界面  
- P2P 应用（如 MuWire、bitcoin、monero）  
- hosts.txt、地址簿和订阅  

如果在某一层指定了转换机制，则受影响列表将缩短。

这些变更的成本和收益尚不明确。

具体提案待定：

### PQ 密钥

对于任何预期算法，后量子（PQ）加密公钥都大于 256 字节。这将消除 Router Identity 中的所有填充以及上述变更带来的任何节省。

在 SSL 所采用的“混合”PQ 方法中，PQ 密钥仅为临时密钥，不会出现在 Router Identity 中。

PQ 签名密钥目前不可行，且 Destination 不包含加密公钥。  
Ratchet 的静态密钥位于 Lease Set 中，而非 Destination。  
因此，我们可以将 Destination 排除在以下讨论之外。

因此，PQ 仅影响 Router Info，且仅针对 PQ 静态（非临时）密钥，不适用于 PQ 混合模式。  
这将需要新的加密类型，并影响 NTCP2、SSU2 以及加密的数据库查找消息及其回复。  
其设计、开发和部署的预计时间框架为 ????????  
但将在混合或 Ratchet ???????????? 之后

进一步讨论见 [此主题](http://zzz.i2p/topics/3294)。

## 问题

可能希望以较慢速率对网络进行“重密钥”（rekey），以为新路由器提供掩护。  
“重密钥”可能仅意味着更改填充，而非真正更改密钥。

现有 Destination 无法重密钥。

是否应通过密钥证书中的不同加密类型来标识公钥字段中带有填充的 Router Identity？这将导致兼容性问题。

## 迁移

用填充替换 ElGamal 密钥不存在向后兼容性问题。

如果实现重密钥，其过程将类似于之前三次路由器身份转换：  
从 DSA-SHA1 到 ECDSA 签名，再到 EdDSA 签名，再到 X25519 加密。

在考虑向后兼容性并禁用 SSU 后，实现可能能够完全移除 ElGamal 代码。  
目前网络中约有 14% 的路由器使用 ElGamal 加密类型，包括许多 floodfill 节点。

Java I2P 的草案合并请求位于 [git.idk.i2p](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66)。

## 参考资料

* [Common](/docs/specs/common-structures/)
* [Datagram](/docs/api/datagrams/)
* [I2CP](/docs/specs/i2cp/)
* [I2NP](/docs/specs/i2np/)
* [MR](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66)
* [NTCP2](/docs/specs/ntcp2/)
* [PKF](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html)
* [PQ](http://zzz.i2p/topics/3294)
* [SAM](/docs/api/samv3/)
* [SSU2](/docs/specs/ssu2/)
* [Streaming](/docs/specs/streaming/)
