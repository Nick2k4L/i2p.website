---
title: "ECIES-X25519-AEAD-Ratchet"
aliases:
  - "/zh/proposals/144-ecies-x25519"
  - "/zh/proposals/144-ecies-x25519/"
number: "144"
author: "zzz, chisana, orignal"
created: "2018-11-22"
lastupdated: "2025-03-05"
status: "已关闭"
thread: "http://zzz.i2p/topics/2639"
target: "0.9.46"
implementedin: "0.9.46"
toc: true
---
## 说明
网络部署和测试正在进行中。
可能会有小的修订。
请参阅 [SPEC](/docs/specs/ecies/) 获取官方规范。

截至 0.9.46 版本，以下功能尚未实现：

- MessageNumbers、Options 和 Termination 块
- 协议层响应
- 零静态密钥
- 多播


## 概述

这是自 I2P 诞生以来首个新的端到端加密类型提案，
用于替代 ElGamal/AES+SessionTags [Elg-AES](/docs/specs/elgamal-aes/)。

它依赖于先前的工作，如下所示：

- 通用结构规范 [Common Structures](/docs/specs/common-structures/)
- [I2NP](/docs/specs/i2np/) 规范，包括 LS2
- ElGamal/AES+Session Tags [Elg-AES](/docs/specs/elgamal-aes/)
- [http://zzz.i2p/topics/1768](http://zzz.i2p/topics/1768) 新的非对称加密概述
- 低层加密概述 [CRYPTO-ELG](/docs/specs/cryptography/)
- ECIES [http://zzz.i2p/topics/2418](http://zzz.i2p/topics/2418)
- [NTCP2](/docs/specs/ntcp2/) [Proposal 111](/proposals/111-ntcp-2/)
- 123 新的 netDB 条目
- 142 新的加密模板
- [Noise](https://noiseprotocol.org/noise.html) 协议
- [Signal](https://signal.org/docs/) 双棘轮算法

目标是支持端到端、目的地到目的地通信的新加密方式。

设计将使用 Noise 握手和数据阶段，并结合 Signal 的双棘轮机制。

本提案中所有对 Signal 和 Noise 的引用仅用于背景信息。
理解或实现本提案不需要了解 Signal 和 Noise 协议。


### 当前 ElGamal 的用途

作为回顾，
ElGamal 256 字节公钥可能出现在以下数据结构中。
请参考通用结构规范。

- 在路由器身份（Router Identity）中
  这是路由器的加密密钥。

- 在目标（Destination）中
  目标的公钥曾用于旧的 i2cp 到 i2cp 加密，
  该功能在 0.6 版本中已禁用，目前除用于 LeaseSet 加密的 IV 外未使用，
  而该 IV 已被弃用。
  LeaseSet 中的公钥被使用。

- 在 LeaseSet 中
  这是目标的加密密钥。

- 在 LS2 中
  这是目标的加密密钥。



### 密钥证书中的 EncTypes

作为回顾，
我们在添加签名类型支持时也添加了加密类型支持。
加密类型字段始终为零，无论是在目标还是路由器身份中。
是否更改该字段尚待决定。
请参考通用结构规范 [Common Structures](/docs/specs/common-structures/)。




### 非对称加密的用途

作为回顾，我们使用 ElGamal 用于：

1) 隧道构建消息（密钥位于 RouterIdentity 中）
   本提案不涵盖其替换。
   请参见提案 152 [Proposal 152](/proposals/152-ecies-tunnels)。

2) 路由器之间的 netdb 和其他 I2NP 消息的加密（密钥位于 RouterIdentity 中）
   依赖于本提案。
   需要一个关于 1) 的提案，或将密钥放入 RI 选项中。

3) 客户端端到端 ElGamal+AES/SessionTag（密钥位于 LeaseSet 中，目标密钥未使用）
   本提案涵盖其替换。

4) NTCP1 和 SSU 的临时 DH
   本提案不涵盖其替换。
   请参见提案 111 的 NTCP2。
   SSU2 当前无提案。


### 目标

- 向后兼容
- 需要并基于 LS2（提案 123）
- 利用为 NTCP2（提案 111）添加的新加密或原语
- 支持无需新的加密或原语
- 维持加密与签名的解耦；支持所有当前和未来的版本
- 为目标启用新加密
- 为路由器启用新加密，但仅限于大蒜消息——隧道构建将是单独的提案
- 不破坏任何依赖 32 字节二进制目标哈希的功能，例如 bittorrent
- 使用临时-静态 DH 维持 0-RTT 消息传递
- 不要求在此协议层缓冲/排队消息；继续支持双向无限消息传递而无需等待响应
- 在 1 RTT 后升级到临时-临时 DH
- 维持对乱序消息的处理
- 维持 256 位安全性
- 添加前向保密
- 添加认证（AEAD）
- 比 ElGamal 更高效的 CPU 使用
- 不依赖 Java jbigi 来使 DH 高效
- 最小化 DH 操作
- 比 ElGamal 更高效的带宽使用（514 字节 ElGamal 块）
- 支持在同一隧道上同时使用新旧加密
- 接收方能够高效地区分来自同一隧道的新旧加密
- 其他人无法区分新旧或未来加密
- 消除新与现有会话长度分类（支持填充）
- 无需新的 I2NP 消息
- 用 AEAD 替换 AES 载荷中的 SHA-256 校验和
- 支持绑定传输和接收会话，以便确认可以在协议内发生，而不仅仅是带外。
  这也将允许回复立即具有前向保密。
- 启用某些消息（如 RouterInfo 存储）的端到端加密，
  我们目前由于 CPU 开销而未这样做。
- 不更改 I2NP 大蒜消息或大蒜消息传递指令格式。
- 消除大蒜 cloveset 和 clove 格式中的未使用或冗余字段。

消除 session tags 的若干问题，包括：

- 在首次回复之前无法使用 AES
- 假设 tag 传递时的不可靠性和停滞
- 带宽效率低下，尤其是在首次传递时
- 存储 tags 的空间效率极低
- 传递 tags 的带宽开销巨大
- 极其复杂，难以实现
- 难以为各种用例调优
  （流式 vs. 数据报，服务器 vs. 客户端，高 vs. 低带宽）
- 由于 tag 传递导致的内存耗尽漏洞


### 非目标 / 范围之外

- LS2 格式更改（提案 123 已完成）
- 新的 DHT 轮换算法或共享随机生成
- 隧道构建的新加密。
  请参见提案 152 [Proposal 152](/proposals/152-ecies-tunnels)。
- 隧道层加密的新加密。
  请参见提案 153 [Proposal 153](/proposals/153-chacha20-layer-encryption)。
- I2NP DLM / DSM / DSRM 消息的加密、传输和接收方法。
  不更改。
- 不支持 LS1 到 LS2 或 ElGamal/AES 到本提案的通信。
  本提案是双向协议。
  目标可通过使用相同隧道发布两个 leasesets 或在 LS2 中放入两种加密类型来处理向后兼容性。
- 威胁模型更改
- 实现细节未在此讨论，由各项目自行决定。
- （乐观）添加扩展或钩子以支持多播



### 理由

ElGamal/AES+SessionTag 作为我们唯一的端到端协议已有约 15 年，
协议本身几乎没有修改。
现在已有更快的加密原语。
我们需要增强协议的安全性。
我们还开发了启发式策略和变通方法以最小化协议的内存和带宽开销，
但这些策略脆弱、难以调优，并使协议更容易出错，导致会话中断。

大约在同一时期，ElGamal/AES+SessionTag 规范及相关文档描述了传递 session tags 的带宽开销，
并提议用“同步 PRNG”替换 session tag 传递。
同步 PRNG 从共同种子确定性地生成相同的 tags。
同步 PRNG 也可称为“棘轮”。
本提案（终于）指定了该棘轮机制，并消除了 tag 传递。

通过使用棘轮（同步 PRNG）生成 session tags，
我们消除了在新会话消息和需要时后续消息中发送 session tags 的开销。
对于典型的 32 个 tag 的 tag set，这节省了 1KB。
这也消除了发送方存储 session tags 的需求，从而将存储需求减半。

需要一个完整的双向握手，类似于 Noise IK 模式，以避免密钥妥协冒充（KCI）攻击。
参见 [NOISE](https://noiseprotocol.org/noise.html) 中的“有效载荷安全属性”表。
有关 KCI 的更多信息，请参见论文 https://www.usenix.org/system/files/conference/woot15/woot15-paper-hlauschek.pdf



### 威胁模型

威胁模型与 NTCP2（提案 111）有所不同。
MitM 节点是 OBEP 和 IBGW，并假设它们通过与 floodfill 协作，
拥有当前或历史全局 NetDB 的完整视图。

目标是防止这些 MitM 将流量分类为
新会话和现有会话消息，或新旧加密。


## 详细提案

本提案定义了一个新的端到端协议以替代 ElGamal/AES+SessionTags。
设计将使用 Noise 握手和数据阶段，并结合 Signal 的双棘轮机制。


### 加密设计摘要

协议中有五个部分需要重新设计：


- 1) 新会话和现有会话容器格式
  被新格式替换。
- 2) ElGamal（256 字节公钥，128 字节私钥）被替换为
  ECIES-X25519（32 字节公钥和私钥）
- 3) AES 被替换为
  AEAD_ChaCha20_Poly1305（下文简称为 ChaChaPoly）
- 4) SessionTags 将被棘轮替换，
  这本质上是一种加密的同步 PRNG。
- 5) ElGamal/AES+SessionTags 规范中定义的 AES 载荷，
  被类似于 NTCP2 中的块格式替换。

这五项更改每项都有其独立的章节。


### I2P 的新加密原语

现有的 I2P 路由器实现将需要实现以下标准加密原语，
这些原语在当前 I2P 协议中不需要：

- ECIES（但这本质上是 X25519）
- Elligator2

尚未实现 [NTCP2](/docs/specs/ntcp2/) ([Proposal 111](/proposals/111-ntcp-2/)) 的现有 I2P 路由器实现
还需要实现：

- X25519 密钥生成和 DH
- AEAD_ChaCha20_Poly1305（下文简称为 ChaChaPoly）
- HKDF


### 加密类型

加密类型（用于 LS2）为 4。
这表示小端序 32 字节 X25519 公钥，
以及此处指定的端到端协议。

加密类型 0 是 ElGamal。
加密类型 1-3 保留给 ECIES-ECDH-AES-SessionTag，参见提案 145 [Proposal 145](/proposals/145-ecies)。


### Noise 协议框架

本提案基于 Noise 协议框架
[NOISE](https://noiseprotocol.org/noise.html)（修订版 34，2018-07-11）提供要求。
Noise 与站对站协议 [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol) 具有相似的属性，
后者是 [SSU](/docs/legacy/ssu/) 协议的基础。在 Noise 术语中，Alice 是发起者，Bob 是响应者。

本提案基于 Noise 协议 Noise_IK_25519_ChaChaPoly_SHA256。
（初始密钥派生函数的实际标识符为 "Noise_IKelg2_25519_ChaChaPoly_SHA256"
以表示 I2P 扩展——见下文 KDF 1 部分）
该 Noise 协议使用以下原语：

- 交互式握手模式：IK
  Alice 立即将她的静态密钥传输给 Bob（I）
  Alice 已经知道 Bob 的静态密钥（K）

- 单向握手模式：N
  Alice 不将她的静态密钥传输给 Bob（N）

- DH 函数：X25519
  X25519 DH，密钥长度为 32 字节，如 [RFC-7748](https://tools.ietf.org/html/rfc7748) 所述。

- 密码函数：ChaChaPoly
  AEAD_CHACHA20_POLY1305，如 [RFC-7539](https://tools.ietf.org/html/rfc7539) 第 2.8 节所述。
  12 字节 nonce，前 4 字节设为零。
  与 [NTCP2](/docs/specs/ntcp2/) 中的相同。

- 哈希函数：SHA256
  标准 32 字节哈希，已在 I2P 中广泛使用。


### 框架的补充

本提案定义了对
Noise_IK_25519_ChaChaPoly_SHA256 的以下增强。这些通常遵循
[NOISE](https://noiseprotocol.org/noise.html) 第 13 节中的指南。

1) 明文临时密钥使用 [Elligator2](https://elligator.cr.yp.to/) 编码。

2) 回复前缀为明文标签。

3) 定义了消息 1、2 和数据阶段的有效载荷格式。
   当然，Noise 中未定义此格式。

所有消息都包含一个 [I2NP](/docs/specs/i2np/) 大蒜消息头。
数据阶段使用类似于但不兼容于 Noise 数据阶段的加密。


### 握手模式

握手使用 [Noise](https://noiseprotocol.org/noise.html) 握手模式。

使用以下字母映射：

- e = 一次性临时密钥
- s = 静态密钥
- p = 消息有效载荷

一次性会话和无绑定会话类似于 Noise N 模式。

```

<- s
  ...
  e es p ->

```

绑定会话类似于 Noise IK 模式。

```

<- s
  ...
  e es s ss p ->
  <- tag e ee se
  <- p
  p ->

```


### 会话

当前的 ElGamal/AES+SessionTag 协议是单向的。
在此层，接收方不知道消息来源。
出站和入站会话未关联。
确认通过带外的 DeliveryStatusMessage
（包装在 GarlicMessage 中）在 clove 中进行。

单向协议存在显著的低效率。
任何回复也必须使用昂贵的“新会话”消息。
这导致更高的带宽、CPU 和内存使用。

单向协议也存在安全弱点。
所有会话都基于临时-静态 DH。
由于没有返回路径，Bob 无法将其静态密钥“棘轮”到临时密钥。
由于不知道消息来源，无法使用
接收到的临时密钥用于出站消息，
因此初始回复也使用临时-静态 DH。

对于本提案，我们定义了两种机制来创建双向协议——
“配对”和“绑定”。
这些机制提供了更高的效率和安全性。


### 会话上下文

与 ElGamal/AES+SessionTags 一样，所有入站和出站会话
必须在给定上下文中，要么是路由器的上下文，
要么是特定本地目标上下文。
在 Java I2P 中，此上下文称为会话密钥管理器（Session Key Manager）。

会话不得在上下文之间共享，因为这会
允许在各种本地目标之间，或在本地目标和路由器之间进行关联。

当给定目标同时支持 ElGamal/AES+SessionTags
和本提案时，两种类型的会话可共享一个上下文。
参见下文第 1c) 节。


### 配对入站和出站会话

当在发起方（Alice）创建出站会话时，
除非不需要回复（例如原始数据报），
否则会创建一个新的入站会话并与出站会话配对。

新的入站会话总是与新的出站会话配对，
除非未请求回复（例如原始数据报）。

如果请求回复并绑定到远端目标或路由器，
则该新的出站会话将绑定到该目标或路由器，
并替换到该目标或路由器的任何先前出站会话。

配对入站和出站会话提供了具有棘轮 DH 密钥能力的双向协议。


### 绑定会话和目标

到给定目标或路由器只有一个出站会话。
从给定目标或路由器可能有多个当前入站会话。
通常，当创建新的入站会话并接收到该会话上的流量时
（这作为 ACK），其他会话将在大约一分钟内被标记为过期。
检查先前消息发送（PN）值，如果在先前入站会话中没有
未接收的消息（在窗口大小内），先前会话可立即删除。


当在发起方（Alice）创建出站会话时，
它绑定到远端目标（Bob），
并且任何配对的入站会话也将绑定到远端目标。
随着会话棘轮，它们继续绑定到远端目标。

当在接收方（Bob）创建入站会话时，
它可能在 Alice 的选择下绑定到远端目标（Alice）。
如果 Alice 在新会话消息中包含绑定信息（她的静态密钥），
会话将绑定到该目标，
并创建出站会话并绑定到同一目标。
随着会话棘轮，它们继续绑定到远端目标。


### 绑定和配对的好处

对于常见的流式情况，我们期望 Alice 和 Bob 如下使用协议：

- Alice 将她的新出站会话与一个新入站会话配对，两者都绑定到远端目标（Bob）。
- Alice 在发送给 Bob 的新会话消息中包含绑定信息和签名，以及回复请求。
- Bob 将他的新入站会话与一个新出站会话配对，两者都绑定到远端目标（Alice）。
- Bob 在配对会话中向 Alice 发送回复（ack），并使用新 DH 密钥进行棘轮。
- Alice 使用 Bob 的新密钥进行棘轮，创建与现有入站会话配对的新出站会话。

通过将入站会话绑定到远端目标，并将入站会话
与绑定到同一目标的出站会话配对，我们实现了两个主要好处：

1) Bob 到 Alice 的初始回复使用临时-临时 DH

2) 在 Alice 接收 Bob 的回复并棘轮后，Alice 到 Bob 的所有后续消息
使用临时-临时 DH。


### 消息 ACKs

在 ElGamal/AES+SessionTags 中，当 LeaseSet 作为大蒜 clove 捆绑，
或传递 tags 时，发送路由器请求 ACK。
这是一个包含 DeliveryStatus Message 的单独大蒜 clove。
为了额外的安全性，DeliveryStatus Message 被包装在 Garlic Message 中。
此机制从协议角度看是带外的。

在新协议中，由于入站和出站会话已配对，
我们可以在带内进行 ACK。不需要单独的 clove。

显式 ACK 只是一个没有 I2NP 块的现有会话消息。
然而，在大多数情况下，可以避免显式 ACK，因为存在反向流量。
实现可能希望在发送显式 ACK 前等待很短时间（可能一百毫秒），
以给流式或应用层时间响应。

实现还需要在处理 I2NP 块后延迟任何 ACK 发送，
因为 Garlic Message 可能包含带有 lease set 的 Database Store Message。
需要最近的 lease set 来路由 ACK，
并且需要远端目标（包含在 lease set 中）来
验证绑定静态密钥。


### 会话超时

出站会话应在入站会话之前过期。
一旦出站会话过期并创建了新的会话，也会创建新的配对入站会话。
如果有旧的入站会话，将允许其过期。


### 多播

待定


### 定义
我们定义了以下函数，对应于使用的加密构建块。

ZEROLEN
    零长度字节数组

CSRNG(n)
    密码学安全随机数生成器的 n 字节输出。

H(p, d)
    SHA-256 哈希函数，接受个性化字符串 p 和数据 d，并
    产生 32 字节长度的输出。
    如 [NOISE](https://noiseprotocol.org/noise.html) 所定义。
    || 以下表示追加。

    使用 SHA-256 如下::

        H(p, d) := SHA-256(p || d)

MixHash(d)
    SHA-256 哈希函数，接受先前的哈希 h 和新数据 d，
    并产生 32 字节长度的输出。
    || 以下表示追加。

    使用 SHA-256 如下::

        MixHash(d) := h = SHA-256(h || d)

STREAM
    如 [RFC-7539](https://tools.ietf.org/html/rfc7539) 所述的 ChaCha20/Poly1305 AEAD。
    S_KEY_LEN = 32 且 S_IV_LEN = 12。

    ENCRYPT(k, n, plaintext, ad)
        使用密钥 k 和必须对密钥 k 唯一的 nonce n 加密明文。
        关联数据 ad 是可选的。
        返回大小为明文 + 16 字节 HMAC 的密文。

        如果密钥保密，整个密文必须与随机数据无法区分。

    DECRYPT(k, n, ciphertext, ad)
        使用密钥 k 和 nonce n 解密密文。
        关联数据 ad 是可选的。
        返回明文。

DH
    X25519 公钥协商系统。私钥 32 字节，公钥 32 字节，产生 32 字节输出。具有以下
    函数：

    GENERATE_PRIVATE()
        生成新的私钥。

    DERIVE_PUBLIC(privkey)
        返回与给定私钥对应的公钥。

    GENERATE_PRIVATE_ELG2()
        生成一个新私钥，该私钥映射到适合 Elligator2 编码的公钥。
        注意，一半随机生成的私钥不适合，必须丢弃。

    ENCODE_ELG2(pubkey)
        返回与给定公钥对应的 Elligator2 编码公钥（逆映射）。
        编码密钥为小端序。
        编码密钥必须是 256 位与随机数据无法区分。
        规范见下文 Elligator2 部分。

    DECODE_ELG2(pubkey)
        返回与给定 Elligator2 编码公钥对应的公钥。
        规范见下文 Elligator2 部分。

    DH(privkey, pubkey)
        使用给定的私钥和公钥生成共享密钥。

HKDF(salt, ikm, info, n)
    一种加密密钥派生函数，接受一些输入密钥材料 ikm（应具有良好的熵但不要求是均匀随机字符串）、
    长度为 32 字节的盐，以及特定于上下文的 'info' 值，并产生适合用作密钥材料的 n 字节输出。

    使用 [RFC-5869](https://tools.ietf.org/html/rfc5869) 中指定的 HKDF，使用 [RFC-2104](https://tools.ietf.org/html/rfc2104) 中指定的 HMAC 哈希函数 SHA-256。
    这意味着 SALT_LEN 最大为 32 字节。

MixKey(d)
    使用先前的 chainKey 和新数据 d 调用 HKDF()，
    并设置新的 chainKey 和 k。
    如 [NOISE](https://noiseprotocol.org/noise.html) 所定义。

    使用 HKDF 如下::

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]



### 1) 消息格式


### 当前消息格式回顾

如 [I2NP](/docs/specs/i2np/) 所述的大蒜消息如下。
由于设计目标是中间跳无法区分新旧加密，
此格式不能更改，即使长度字段是冗余的。
格式显示为完整的 16 字节头，尽管
实际头可能采用不同格式，取决于所用传输。

解密后，数据包含一系列大蒜 cloves 和附加数据，也称为 clove set。

详见 [I2NP](/docs/specs/i2np/) 及其完整规范。


```

+----+----+----+----+----+----+----+----+
  |type|      msg_id       |  expiration
  +----+----+----+----+----+----+----+----+
                           |  size   |chks|
  +----+----+----+----+----+----+----+----+
  |      length       |                   |
  +----+----+----+----+                   +
  |          encrypted data               |
  ~                                       ~
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

```


### 加密数据格式回顾

当前消息格式，已使用超过 15 年，
是 ElGamal/AES+SessionTags。
在 ElGamal/AES+SessionTags 中，有两种消息格式：

1) 新会话：
- 514 字节 ElGamal 块
- AES 块（最小 128 字节，16 的倍数）

2) 现有会话：
- 32 字节 Session Tag
- AES 块（最小 128 字节，16 的倍数）

最小填充到 128 是 Java I2P 中的实现方式，但接收时不强制执行。

这些消息被封装在 I2NP 大蒜消息中，其中包含
长度字段，因此长度已知。

注意，未定义填充到非模 16 长度，
因此新会话总是（模 16 == 2），
而现有会话总是（模 16 == 0）。
我们需要修复此问题。

接收方首先尝试将前 32 字节作为 Session Tag 查找。
如果找到，则解密 AES 块。
如果未找到，且数据至少为 (514+16) 字节长，则尝试解密 ElGamal 块，
如果成功，则解密 AES 块。


### 新 Session Tags 及与 Signal 的比较

在 Signal 双棘轮中，头包含：

- DH：当前棘轮公钥
- PN：前一链消息长度
- N：消息编号

Signal 的“发送链”大致相当于我们的 tag sets。
通过使用 session tag，我们可以消除大部分这些。

在新会话中，我们仅在未加密头中放入公钥。

在现有会话中，我们使用 session tag 作为头。
session tag 与当前棘轮公钥和消息编号相关联。

在新会话和现有会话中，PN 和 N 都在加密体中。

在 Signal 中，事物不断棘轮。新的 DH 公钥要求
接收方棘轮并发送新的公钥作为回复，这也作为
接收到的公钥的 ack。
这对我们来说会产生太多 DH 操作。
因此，我们分离接收到的密钥的 ack 和新公钥的传输。
任何使用从新 DH 公钥生成的 session tag 的消息都构成 ACK。
我们仅在希望重新密钥时才传输新公钥。

在 DH 必须棘轮之前的最大消息数为 65535。

在传递会话密钥时，我们从中派生“Tag Set”，
而不是必须同时传递 session tags。
Tag Set 最多可包含 65536 个 tags。
然而，接收方应实现“前瞻”策略，
而不是一次性生成所有可能的 tags。
最多生成 N 个 tags 超过最后接收到的良好 tag。
N 最多为 128，但 32 甚至更少可能是更好的选择。


### 1a) 新会话格式

新会话一次性公钥（32 字节）
加密数据和 MAC（剩余字节）

新会话消息可能包含也可能不包含发送方的静态公钥。
如果包含，反向会话将绑定到该密钥。
如果期望回复，
即用于流式和可回复数据报，则应包含静态密钥。
对于原始数据报则不应包含。

新会话消息类似于单向 Noise [NOISE](https://noiseprotocol.org/noise.html) 模式
“N”（如果未发送静态密钥），
或双向模式“IK”（如果发送了静态密钥）。


### 1b) 新会话格式（带绑定）

长度为 96 + 载荷长度。
加密格式：

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   新会话临时公钥                     |
  +             32 字节                   +
  |     使用 Elligator2 编码              |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +         静态密钥                     +
  |       ChaCha20 加密数据               |
  +            32 字节                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 消息认证码                  |
  +    (MAC) 静态密钥部分                 +
  |             16 字节                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            载荷部分                  +
  |       ChaCha20 加密数据               |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 消息认证码                  |
  +         (MAC) 载荷部分               +
  |             16 字节                  |
  +----+----+----+----+----+----+----+----+

  公钥 :: 32 字节，小端序，Elligator2，明文

  静态密钥加密数据 :: 32 字节

  载荷部分加密数据 :: 剩余数据减去 16 字节

  MAC :: Poly1305 消息认证码，16 字节

```


### 新会话临时密钥

临时密钥为 32 字节，使用 Elligator2 编码。
此密钥永不重用；每次消息（包括重传）都会生成新密钥。

### 静态密钥

解密后，Alice 的 X25519 静态密钥，32 字节。


### 载荷

加密长度为数据的剩余部分。
解密长度比加密长度少 16 字节。
载荷必须包含 DateTime 块，通常包含一个或多个 Garlic Clove 块。
见下文载荷部分的格式和附加要求。


### 1c) 新会话格式（无绑定）

如果不需要回复，则不发送静态密钥。


长度为 96 + 载荷长度。
加密格式：

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   新会话临时公钥                     |
  +             32 字节                   +
  |     使用 Elligator2 编码              |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           标志部分                   +
  |       ChaCha20 加密数据               |
  +            32 字节                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 消息认证码                  |
  +         (MAC) 上述部分               +
  |             16 字节                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            载荷部分                  +
  |       ChaCha20 加密数据               |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 消息认证码                  |
  +         (MAC) 载荷部分               +
  |             16 字节                  |
  +----+----+----+----+----+----+----+----+

  公钥 :: 32 字节，小端序，Elligator2，明文

  标志部分加密数据 :: 32 字节

  载荷部分加密数据 :: 剩余数据减去 16 字节

  MAC :: Poly1305 消息认证码，16 字节

```

### 新会话临时密钥

Alice 的临时密钥。
临时密钥为 32 字节，使用 Elligator2 编码，小端序。
此密钥永不重用；每次消息（包括重传）都会生成新密钥。


### 标志部分解密数据

标志部分不包含任何内容。
它始终为 32 字节，因为必须与带绑定的新会话消息中的静态密钥长度相同。
Bob 通过测试 32 字节是否全为零来确定是静态密钥还是标志部分。

TODO 此处是否需要任何标志？


### 载荷

加密长度为数据的剩余部分。
解密长度比加密长度少 16 字节。
载荷必须包含 DateTime 块，通常包含一个或多个 Garlic Clove 块。
见下文载荷部分的格式和附加要求。


### 1d) 一次性格式（无绑定或会话）

如果仅预期发送单条消息，
则不需要会话设置或静态密钥。


长度为 96 + 载荷长度。
加密格式：

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |       临时公钥                       |
  +             32 字节                   +
  |     使用 Elligator2 编码              |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           标志部分                   +
  |       ChaCha20 加密数据               |
  +            32 字节                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 消息认证码                  |
  +         (MAC) 上述部分               +
  |             16 字节                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            载荷部分                  +
  |       ChaCha20 加密数据               |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 消息认证码                  |
  +         (MAC) 载荷部分               +
  |             16 字节                  |
  +----+----+----+----+----+----+----+----+

  公钥 :: 32 字节，小端序，Elligator2，明文

  标志部分加密数据 :: 32 字节

  载荷部分加密数据 :: 剩余数据减去 16 字节

  MAC :: Poly1305 消息认证码，16 字节

```


### 新会话一次性密钥

一次性密钥为 32 字节，使用 Elligator2 编码，小端序。
此密钥永不重用；每次消息（包括重传）都会生成新密钥。


### 标志部分解密数据

标志部分不包含任何内容。
它始终为 32 字节，因为必须与带绑定的新会话消息中的静态密钥长度相同。
Bob 通过测试 32 字节是否全为零来确定是静态密钥还是标志部分。

TODO 此处是否需要任何标志？

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                                       |
  +             全为零                   +
  |              32 字节                 |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+

  零:: 全为零，32 字节。

```


### 载荷

加密长度为数据的剩余部分。
解密长度比加密长度少 16 字节。
载荷必须包含 DateTime 块，通常包含一个或多个 Garlic Clove 块。
见下文载荷部分的格式和附加要求。


### 1f) 新会话消息的 KDF

### 初始 ChainKey 的 KDF

这是标准 [NOISE](https://noiseprotocol.org/noise.html) 的 IK 模式，带有修改的协议名称。
注意，我们对 IK 模式（绑定会话）和 N 模式（无绑定会话）使用相同的初始化器。

协议名称修改有两个原因。
首先，表示临时密钥使用 Elligator2 编码，
其次，表示在第二条消息前调用 MixHash() 以混合标签值。

```

这是“e”消息模式：

  // 定义 protocol_name。
  Set protocol_name = "Noise_IKelg2+hs2_25519_ChaChaPoly_SHA256"
   (40 字节，US-ASCII 编码，无 NULL 终止)。

  // 定义 Hash h = 32 字节
  h = SHA256(protocol_name);

  定义 ck = 32 字节链式密钥。将 h 数据复制到 ck。
  Set chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // 到此为止，Alice 可为所有出站连接预先计算

```


### 标志/静态密钥部分加密内容的 KDF

```

这是“e”消息模式：

  // Bob 的 X25519 静态密钥
  // bpk 在 leaseset 中发布
  bsk = GENERATE_PRIVATE()
  bpk = DERIVE_PUBLIC(bsk)

  // Bob 静态公钥
  // MixHash(bpk)
  // || 以下表示追加
  h = SHA256(h || bpk);

  // 到此为止，Bob 可为所有入站连接预先计算

  // Alice 的 X25519 临时密钥
  aesk = GENERATE_PRIVATE_ELG2()
  aepk = DERIVE_PUBLIC(aesk)

  // Alice 临时公钥
  // MixHash(aepk)
  // || 以下表示追加
  h = SHA256(h || aepk);

  // h 用作新会话消息中 AEAD 的关联数据
  // 保留 Hash h 用于新会话回复 KDF
  // eapk 在新会话消息开头以明文发送
  elg2_aepk = ENCODE_ELG2(aepk)
  // Bob 解码后
  aepk = DECODE_ELG2(elg2_aepk)

  “e”消息模式结束。

  这是“es”消息模式：

  // Noise es
  sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // ChaChaPoly 参数用于加密/解密
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // AEAD 参数
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, flags/static key section, ad)

  “es”消息模式结束。

  这是“s”消息模式：

  // MixHash(ciphertext)
  // 保存用于载荷部分 KDF
  h = SHA256(h || ciphertext)

  // Alice 的 X25519 静态密钥
  ask = GENERATE_PRIVATE()
  apk = DERIVE_PUBLIC(ask)

  “s”消息模式结束。

```


### 载荷部分的 KDF（含 Alice 静态密钥）

```

这是“ss”消息模式：

  // Noise ss
  sharedSecret = DH(ask, bpk) = DH(bsk, apk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // ChaChaPoly 参数用于加密/解密
  // chainKey 来自静态密钥部分
  Set sharedSecret = X25519 DH 结果
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // AEAD 参数
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, payload, ad)

  “ss”消息模式结束。

  // MixHash(ciphertext)
  // 保存用于新会话回复 KDF
  h = SHA256(h || ciphertext)

```


### 载荷部分的 KDF（不含 Alice 静态密钥）

注意，这是 Noise “N”模式，但我们使用与绑定会话相同的“IK”初始化器。

新会话消息在静态密钥解密并检查是否全为零之前，
无法识别是否包含 Alice 的静态密钥。
因此，接收方必须对所有新会话消息使用“IK”状态机。
如果静态密钥全为零，则必须跳过“ss”消息模式。


```

chainKey = 来自标志/静态密钥部分
  k = 来自标志/静态密钥部分
  n = 1
  ad = h 来自标志/静态密钥部分
  ciphertext = ENCRYPT(k, n, payload, ad)

```


### 1g) 新会话回复格式

可发送一个或多个新会话回复以响应单个新会话消息。
每个回复前缀为一个标签，该标签从会话的 TagSet 生成。

新会话回复分为两部分。
第一部分是完成带前缀标签的 Noise IK 握手。
第一部分长度为 56 字节。
第二部分是数据阶段载荷。
第二部分长度为 16 + 载荷长度。

总长度为 72 + 载荷长度。
加密格式：

```

+----+----+----+----+----+----+----+----+
  |       会话标签   8 字节               |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        临时公钥                       +
  |                                       |
  +            32 字节                   +
  |     使用 Elligator2 编码              |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 消息认证码                  |
  +  (MAC) 密钥部分（无数据）             +
  |             16 字节                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            载荷部分                  +
  |       ChaCha20 加密数据               |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 消息认证码                  |
  +         (MAC) 载荷部分               +
  |             16 字节                  |
  +----+----+----+----+----+----+----+----+

  标签 :: 8 字节，明文

  公钥 :: 32 字节，小端序，Elligator2，明文

  MAC :: Poly1305 消息认证码，16 字节
         注意：ChaCha20 明文数据为空（ZEROLEN）

  载荷部分加密数据 :: 剩余数据减去 16 字节

  MAC :: Poly1305 消息认证码，16 字节

```

### 会话标签
标签在会话标签 KDF 中生成，如
下文 DH 初始化 KDF 所初始化。
这将回复与会话关联。
DH 初始化中的会话密钥未使用。


### 新会话回复临时密钥

Bob 的临时密钥。
临时密钥为 32 字节，使用 Elligator2 编码，小端序。
此密钥永不重用；每次消息（包括重传）都会生成新密钥。


### 载荷
加密长度为数据的剩余部分。
解密长度比加密长度少 16 字节。
载荷通常包含一个或多个 Garlic Clove 块。
见下文载荷部分的格式和附加要求。


### 回复 TagSet 的 KDF

从 TagSet 创建一个或多个标签，TagSet 使用
下文 KDF 初始化，使用新会话消息中的 chainKey。

```

// 生成 tagset
  tagsetKey = HKDF(chainKey, ZEROLEN, "SessionReplyTags", 32)
  tagset_nsr = DH_INITIALIZE(chainKey, tagsetKey)

```


### 回复密钥部分加密内容的 KDF

```

// 新会话消息中的密钥
  // Alice 的 X25519 密钥
  // apk 和 aepk 在原始新会话消息中发送
  // ask = Alice 私有静态密钥
  // apk = Alice 公有静态密钥
  // aesk = Alice 临时私有密钥
  // aepk = Alice 临时公有密钥
  // Bob 的 X25519 静态密钥
  // bsk = Bob 私有静态密钥
  // bpk = Bob 公有静态密钥

  // 生成标签
  tagsetEntry = tagset_nsr.GET_NEXT_ENTRY()
  tag = tagsetEntry.SESSION_TAG

  // MixHash(tag)
  h = SHA256(h || tag)

  这是“e”消息模式：

  // Bob 的 X25519 临时密钥
  besk = GENERATE_PRIVATE_ELG2()
  bepk = DERIVE_PUBLIC(besk)

  // Bob 的临时公钥
  // MixHash(bepk)
  // || 以下表示追加
  h = SHA256(h || bepk);

  // elg2_bepk 在新会话消息开头以明文发送
  elg2_bepk = ENCODE_ELG2(bepk)
  // Bob 解码后
  bepk = DECODE_ELG2(elg2_bepk)

  “e”消息模式结束。

  这是“ee”消息模式：

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // ChaChaPoly 参数用于加密/解密
  // chainKey 来自原始新会话载荷部分
  sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
  keydata = HKDF(chainKey, sharedSecret, "", 32)
  chainKey = keydata[0:31]

  “ee”消息模式结束。

  这是“se”消息模式：

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  sharedSecret = DH(ask, bepk) = DH(besk, apk)
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // AEAD 参数
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, ZEROLEN, ad)

  “se”消息模式结束。

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  chainKey 用于下文的棘轮。

```


### 载荷部分加密内容的 KDF

这类似于第一个现有会话消息，
后分割，但无单独标签。
此外，我们使用上述哈希将
载荷绑定到 NSR 消息。


```

// split()
  keydata = HKDF(chainKey, ZEROLEN, "", 64)
  k_ab = keydata[0:31]
  k_ba = keydata[32:63]
  tagset_ab = DH_INITIALIZE(chainKey, k_ab)
  tagset_ba = DH_INITIALIZE(chainKey, k_ba)

  // 新会话回复载荷的 AEAD 参数
  k = HKDF(k_ba, ZEROLEN, "AttachPayloadKDF", 32)
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, payload, ad)
```


### 注释

根据响应大小，可发送多个 NSR 消息，每个具有唯一临时密钥。

Alice 和 Bob 必须为每个 NS 和 NSR 消息使用新的临时密钥。

Alice 必须在发送现有会话（ES）消息前接收 Bob 的一个 NSR 消息，
Bob 必须在发送 ES 消息前接收 Alice 的 ES 消息。

Bob 的 NSR 载荷部分的 ``chainKey`` 和 ``k`` 用作
初始 ES DH 棘轮的输入（双向，见 DH 棘轮 KDF）。

Bob 必须仅保留从 Alice 接收到的 ES 消息的现有会话。
任何其他创建的入站和出站会话（用于多个 NSR）应在
接收到 Alice 的第一个 ES 消息后立即销毁。


### 1h) 现有会话格式

会话标签（8 字节）
加密数据和 MAC（见下文第 3 节）


### 格式
加密：

```

+----+----+----+----+----+----+----+----+
  |       会话标签                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            载荷部分                  +
  |       ChaCha20 加密数据               |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 消息认证码                  |
  +              (MAC)                   +
  |             16 字节                  |
  +----+----+----+----+----+----+----+----+

  会话标签 :: 8 字节，明文

  载荷部分加密数据 :: 剩余数据减去 16 字节

  MAC :: Poly1305 消息认证码，16 字节

```


### 载荷
加密长度为数据的剩余部分。
解密长度比加密长度少 16 字节。
见下文载荷部分的格式和要求。


KDF

```
见下文 AEAD 部分。

  // 现有会话载荷的 AEAD 参数
  k = 与此会话标签关联的 32 字节会话密钥
  n = 当前链中的消息编号 N，从关联的会话标签中检索。
  ad = 会话标签，8 字节
  ciphertext = ENCRYPT(k, n, payload, ad)
```


### 2) ECIES-X25519


格式：32 字节公钥和私钥，小端序。

理由：在 [NTCP2](/docs/specs/ntcp2/) 中使用。


### 2a) Elligator2

在标准 Noise 握手中，每个方向的初始握手消息以
以明文传输的临时密钥开始。
由于有效的 X25519 密钥可与随机数据区分，中间人可能区分
这些消息与以随机会话标签开始的现有会话消息。
在 [NTCP2](/docs/specs/ntcp2/) ([Proposal 111](/proposals/111-ntcp-2/)) 中，我们使用了低开销的 XOR 函数，利用带外静态密钥来混淆
密钥。然而，此处的威胁模型不同；我们不希望允许任何中间人
使用任何手段确认流量的目的地，或区分
初始握手消息与现有会话消息。

因此，[Elligator2](https://elligator.cr.yp.to/) 用于转换新会话和新会话回复消息中的临时密钥，
使其与均匀随机字符串无法区分。


### 格式

32 字节公钥和私钥。
编码密钥为小端序。

如 [Elligator2](https://elligator.cr.yp.to/) 所定义，编码密钥与 254 个随机位无法区分。
我们需要 256 个随机位（32 字节）。因此，编码和解码定义如下：

编码：

```

ENCODE_ELG2() 定义

  // 按 Elligator2 规范编码
  encodedKey = encode(pubkey)
  // 对 MSB 的 2 个随机位进行 OR 运算
  randomByte = CSRNG(1)
  encodedKey[31] |= (randomByte & 0xc0)
```


解码：

```

DECODE_ELG2() 定义

  // 从 MSB 屏蔽出 2 个随机位
  encodedKey[31] &= 0x3f
  // 按 Elligator2 规范解码
  pubkey = decode(encodedKey)
```


### 理由

防止 OBEP 和 IBGW 对流量进行分类所必需。


### 注释

Elligator2 使平均密钥生成时间加倍，因为一半的私钥
产生的公钥不适合用 Elligator2 编码。
此外，密钥生成时间具有指数分布且无界，
因为生成器必须不断重试直到找到合适的密钥对。

此开销可通过提前在单独线程中生成密钥来管理，
以保持合适的密钥池。

生成器执行 ENCODE_ELG2() 函数以确定适用性。
因此，生成器应存储 ENCODE_ELG2() 的结果，
以免再次计算。

此外，不合适的密钥可添加到用于 [NTCP2](/docs/specs/ntcp2/) 的密钥池中，
其中不使用 Elligator2。
这样做的安全问题尚待确定。


### 3) AEAD (ChaChaPoly)

使用 ChaCha20 和 Poly1305 的 AEAD，与 [NTCP2](/docs/specs/ntcp2/) 相同。
这对应于 [RFC-7539](https://tools.ietf.org/html/rfc7539)，也类似地用于 TLS [RFC-7905](https://tools.ietf.org/html/rfc7905)。


### 新会话和新会话回复输入

新会话消息中 AEAD 块的加密/解密函数输入：

```

k :: 32 字节密码密钥
       见上文新会话和新会话回复 KDF。

  n :: 基于计数器的 nonce，12 字节。
       n = 0

  ad :: 关联数据，32 字节。
        前续数据的 SHA256 哈希，作为 mixHash() 的输出。

  data :: 明文数据，0 或更多字节

```


### 现有会话输入

现有会话消息中 AEAD 块的加密/解密函数输入：

```

k :: 32 字节会话密钥
       从伴随的会话标签中查找。

  n :: 基于计数器的 nonce，12 字节。
       传输时从 0 开始并为每条消息递增。
       对于接收方，值
       从伴随的会话标签中查找。
       前四个字节始终为零。
       后八个字节是消息编号（n），小端序编码。
       最大值为 65535。
       当 N 达到该值时，会话必须棘轮。
       永远不要使用更高值。

  ad :: 关联数据
        会话标签

  data :: 明文数据，0 或更多字节

```


### 加密格式

加密函数的输出，解密函数的输入：

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |       ChaCha20 加密数据               |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 消息认证码                  |
  +              (MAC)                   +
  |             16 字节                  |
  +----+----+----+----+----+----+----+----+

  加密数据 :: 与明文数据大小相同，0 - 65519 字节

  MAC :: Poly1305 消息认证码，16 字节

```

### 注释
- 由于 ChaCha20 是流密码，明文无需填充。
  额外的密钥流字节被丢弃。

- 密码的密钥（256 位）通过 SHA256 KDF 协商。
  每条消息的 KDF 详细信息在下文各节中。

- ChaChaPoly 帧的大小已知，因为它们被封装在 I2NP 数据消息中。

- 对于所有消息，
  填充在认证数据帧内部。


### AEAD 错误处理

所有失败 AEAD 验证的接收数据必须丢弃。
不返回响应。


### 理由

在 [NTCP2](/docs/specs/ntcp2/) 中使用。


### 4) 棘轮

我们仍然使用会话标签，但使用棘轮生成它们。
会话标签也有一个我们从未实现的重新密钥选项。
所以它像双棘轮，但我们从未做第二个。

这里我们定义了类似于 Signal 双棘轮的东西。
会话标签在接收方和发送方确定性且相同地生成。

通过使用对称密钥/标签棘轮，我们消除了发送方存储会话标签的内存使用。
我们也消除了发送标签集的带宽消耗。
接收方使用仍然显著，但我们可以进一步减少，
因为我们会将会话标签从 32 字节缩小到 8 字节。

我们不使用 Signal 中指定（和可选）的头加密，
而是使用会话标签。

通过使用 DH 棘轮，我们实现了前向保密，这在 ElGamal/AES+SessionTags 中从未实现。

注意：新会话一次性公钥不是棘轮的一部分，其唯一功能
是加密 Alice 的初始 DH 棘轮密钥。


### 消息编号

双棘轮通过在每条消息头中包含标签来处理丢失或乱序消息。
接收方查找标签的索引，即消息编号 N。
如果消息包含带有 PN 值的消息编号块，
接收方可删除前一个标签集中的更高标签，
同时保留前一个标签集中的跳过标签，
以防稍后到达跳过消息。


### 示例实现

我们定义以下数据结构和函数来实现这些棘轮。

TAGSET_ENTRY
    TAGSET 中的单个条目。

    INDEX
        整数索引，从 0 开始

    SESSION_TAG
        在线上传输的标识符，8 字节

    SESSION_KEY
        对称密钥，永不在线上传输，32 字节

TAGSET
    TAGSET_ENTRIES 的集合。

    CREATE(key, n)
        使用 32 字节的初始加密密钥材料生成新 TAGSET。
        提供关联的会话标识符。
        指定要创建的初始标签数；对于出站会话通常为 0 或 1。
        LAST_INDEX = -1
        调用 EXTEND(n)。

    EXTEND(n)
        通过调用 EXTEND() n 次生成 n 个更多 TAGSET_ENTRIES。

    EXTEND()
        生成一个更多 TAGSET_ENTRY，除非已生成最大数量的 SESSION_TAGS。
        如果 LAST_INDEX 大于或等于 65535，则返回。
        ++ LAST_INDEX
        使用 LAST_INDEX 值和计算的 SESSION_TAG 创建新 TAGSET_ENTRY。
        调用 RATCHET_TAG() 和（可选）RATCHET_KEY()。
        对于入站会话，SESSION_KEY 的计算
        可延迟并在 GET_SESSION_KEY() 中计算。
        调用 EXPIRE()

    EXPIRE()
        删除过旧的标签和密钥，或如果 TAGSET 大小超过某个限制。

    RATCHET_TAG()
        基于最后一个 SESSION_TAG 计算下一个 SESSION_TAG。

    RATCHET_KEY()
        基于最后一个 SESSION_KEY 计算下一个 SESSION_KEY。

    SESSION
        关联的会话。

    CREATION_TIME
        创建 TAGSET 的时间。

    LAST_INDEX
        EXTEND() 生成的最后一个 TAGSET_ENTRY 索引。

    GET_NEXT_ENTRY()
        仅用于出站会话。
        如果没有剩余 TAGSET_ENTRIES，则调用 EXTEND(1)。
        如果 EXTEND(1) 无操作，则已使用最大 65535 个 TAGSETS，返回错误。
        返回下一个未使用的 TAGSET_ENTRY。

    GET_SESSION_KEY(sessionTag)
        仅用于入站会话。
        返回包含 sessionTag 的 TAGSET_ENTRY。
        如果找到，则删除 TAGSET_ENTRY。
        如果延迟了 SESSION_KEY 计算，则现在计算。
        如果剩余 TAGSET_ENTRIES 较少，则调用 EXTEND(n)。


### 4a) DH 棘轮

棘轮但不像 Signal 那样快。
我们分离接收到的密钥的 ack 和生成新密钥。
在典型使用中，Alice 和 Bob 将在新会话中立即各棘轮（两次），
但之后不再棘轮。

注意，棘轮是单向的，并为该方向生成新会话标签/消息密钥棘轮链。
要为双向生成密钥，必须棘轮两次。

每次生成并发送新密钥时，你都会棘轮。
每次接收到新密钥时，你都会棘轮。

Alice 在创建无绑定出站会话时棘轮一次，她不创建入站会话
（无绑定是不可回复的）。

Bob 在创建无绑定入站会话时棘轮一次，且不创建相应的出站会话
（无绑定是不可回复的）。

Alice 继续向 Bob 发送新会话（NS）消息，直到接收到 Bob 的一个新会话回复（NSR）消息。
然后她使用 NSR 的载荷部分 KDF 结果作为会话棘轮的输入（见 DH 棘轮 KDF），
并开始发送现有会话（ES）消息。

对于每个接收到的 NS 消息，Bob 创建一个新入站会话，使用回复载荷部分的 KDF 结果
作为新入站和出站 ES DH 棘轮的输入。

对于每个需要的回复，Bob 向 Alice 发送一个 NSR 消息，载荷中包含回复。
要求 Bob 为每个 NSR 使用新的临时密钥。

Bob 必须在创建和发送 ES 消息到相应出站会话前，
在其中一个入站会话上从 Alice 接收到 ES 消息。

Alice 应使用计时器接收 Bob 的 NSR 消息。如果计时器超时，
应移除会话。

为避免 KCI 和/或资源耗尽攻击，攻击者可能丢弃 Bob 的 NSR 回复以使 Alice 继续发送 NS 消息，
Alice 应避免在因计时器超时而重试一定次数后，
再次向 Bob 启动新会话。

Alice 和 Bob 各自
为接收到的每个 NextKey 块进行 DH 棘轮。

Alice 和 Bob 各自在每次
DH 棘轮后生成新的标签集棘轮和两个对称密钥棘轮。对于给定方向的每个新 ES 消息，Alice 和 Bob 推进会话
标签和对称密钥棘轮。

初始握手后的 DH 棘轮频率取决于实现。
虽然协议规定在棘轮前最多 65535 条消息，
但更频繁的棘轮（基于消息计数、经过时间或两者）
可能提供额外的安全性。

在绑定会话的最终握手 KDF 后，Bob 和 Alice 必须在
结果的 CipherState 上运行 Noise Split() 函数，以创建独立的对称和标签链密钥用于入站和出站会话。


#### 密钥和标签集 ID

密钥和标签集 ID 号用于标识密钥和标签集。
密钥 ID 用于 NextKey 块中标识发送或使用的密钥。
标签集 ID 用于（与消息编号一起）在 ACK 块中标识被确认的消息。
密钥和标签集 ID 均适用于单个方向的标签集。
密钥和标签集 ID 号必须是连续的。

在每个方向会话中使用的第一个标签集中，标签集 ID 为 0。
尚未发送 NextKey 块，因此没有密钥 ID。

要开始 DH 棘轮，发送方传输一个密钥 ID 为 0 的新 NextKey 块。
接收方回复一个密钥 ID 为 0 的新 NextKey 块。
然后发送方开始使用标签集 ID 为 1 的新标签集。

后续标签集类似生成。
对于在 NextKey 交换后使用的所有标签集，标签集编号为 (1 + Alice 的密钥 ID + Bob 的密钥 ID)。

密钥和标签集 ID 从 0 开始并连续递增。
最大标签集 ID 为 65535。
最大密钥 ID 为 32767。
当标签集即将耗尽时，标签集发送方必须启动 NextKey 交换。
当标签集 65535 即将耗尽时，标签集发送方必须通过发送新会话消息启动新会话。

假设最大流式消息大小为 1730，且无重传，
使用单个标签集的理论最大数据传输量为 1730 * 65536 ~= 108 MB。
实际最大值会因重传而更低。

在所有 65536 个可用标签集上使用所有标签集的理论最大数据传输量，
在会话必须被丢弃和替换之前，
为 64K * 108 MB ~= 6.9 TB。


#### DH 棘轮消息流

标签集的下一个密钥交换必须由
这些标签的发送方（出站标签集的所有者）启动。
接收方（入站标签集的所有者）将响应。
对于典型的应用层 HTTP GET 流量，Bob 将发送更多消息并首先棘轮
通过启动密钥交换；下图显示了这一点。
当 Alice 棘轮时，同样的事情反向发生。

NS/NSR 握手后使用的第一个标签集是标签集 0。
当标签集 0 即将耗尽时，必须在两个方向交换新密钥以创建标签集 1。
之后，仅在一个方向发送新密钥。

要创建标签集 2，标签发送方发送新密钥，标签接收方发送其旧密钥 ID 作为确认。
双方都进行 DH。

要创建标签集 3，标签发送方发送其旧密钥 ID 并请求标签接收方的新密钥。
双方都进行 DH。

后续标签集的生成方式与标签集 2 和 3 相同。
标签集编号为 (1 + 发送方密钥 ID + 接收方密钥 ID)。


```

标签发送方                    标签接收方

                   ... 使用标签集 #0 ...


  (标签集 #0 即将为空)
  (生成新密钥 #0)

  下一密钥，前向，请求反向，带密钥 #0  -------->
  (重复直到接收到下一密钥)

                              (生成新密钥 #0，进行 DH，创建 IB 标签集 #1)

          <-------------      下一密钥，反向，带密钥 #0
                              (重复直到在新标签集上接收到标签)

  (进行 DH，创建 OB 标签集 #1)


                   ... 使用标签集 #1 ...


  (标签集 #1 即将为空)
  (生成新密钥 #1)

  下一密钥，前向，带密钥 #1        -------->
  (重复直到接收到下一密钥)

                              (重用密钥 #0，进行 DH，创建 IB 标签集 #2)

          <--------------     下一密钥，反向，ID 0
                              (重复直到在新标签集上接收到标签)

  (进行 DH，创建 OB 标签集 #2)


                   ... 使用标签集 #2 ...


  (标签集 #2 即将为空)
  (重用密钥 #1)

  下一密钥，前向，请求反向，ID 1
