---
title: "ECIES 目标的流式 MTU"
number: "155"
author: "zzz"
created: "2020-05-06"
lastupdated: "2020-05-30"
status: "已关闭"
thread: "http://zzz.i2p/topics/2886"
target: "0.9.47"
implementedin: "0.9.47"
toc: true
---
## 说明
网络部署和测试正在进行中。  
可能会有少量修订。


## 概述


### 摘要

ECIES 将现有会话（ES）消息开销减少了约 90 字节。  
因此，我们可以为 ECIES 连接将 MTU 增加大约 90 字节。  
参见 [ECIES 规范](/docs/specs/ecies/#overhead)、[流规范](/docs/specs/streaming/#flags-and-option-data-fields) 和 [流 API 文档](/docs/api/streaming/)。

如果不增加 MTU，在许多情况下节省的开销实际上并未真正“节省”，  
因为消息仍会被填充以使用两个完整的隧道消息。

本提案不需要对规范进行任何更改。  
发布为提案仅是为了促进对推荐值和实现细节的讨论与共识建立。


### 目标

- 增加协商的 MTU
- 最大化利用 1 KB 隧道消息
- 不更改流协议


## 设计

使用现有的 MAX_PACKET_SIZE_INCLUDED 选项和 MTU 协商机制。  
流协议继续使用发送和接收 MTU 的最小值。  
默认值对所有连接仍为 1730，无论使用何种密钥。

鼓励实现在所有 SYN 数据包中（双向）包含 MAX_PACKET_SIZE_INCLUDED 选项，  
尽管这不是强制要求。

如果目标仅支持 ECIES，则使用更高的值（无论是作为 Alice 还是 Bob）。  
如果目标支持双密钥，行为可能有所不同：

如果双密钥客户端位于路由器外部（在外部应用程序中），  
它可能不知道远端使用的密钥，Alice 可能在 SYN 中请求更高的值，  
而 SYN 中的最大数据量仍为 1730。

如果双密钥客户端位于路由器内部，客户端可能知道也可能不知道正在使用的密钥。  
leaseset 可能尚未获取，或者内部 API 接口可能无法轻松向客户端提供该信息。  
如果信息可用，Alice 可使用更高的值；  
否则，Alice 必须使用标准值 1730，直到完成协商。

作为 Bob 的双密钥客户端可以在响应中发送更高的值，  
即使从 Alice 收到的值为空或为 1730；  
但流协议中没有向上协商的机制，因此 MTU 应保持在 1730。

如 [流 API 文档](/docs/api/streaming/) 中所述，  
从 Alice 发送到 Bob 的 SYN 数据包中的数据可能超过 Bob 的 MTU。  
这是流协议的一个弱点。  
因此，双密钥客户端必须将发送的 SYN 数据包中的数据限制为 1730 字节，  
同时发送更高的 MTU 选项。  
一旦从 Bob 收到更高的 MTU，Alice 可以增加实际发送的最大有效载荷。


### 分析

如 [ECIES 规范](/docs/specs/ecies/#overhead) 所述，现有会话消息的 ElGamal 开销为  
151 字节，Ratchet 开销为 69 字节。  
因此，我们可以将 Ratchet 连接的 MTU 增加 (151 - 69) = 82 字节，  
从 1730 增加到 1812。


## 规范

向 [流 API 文档](/docs/api/streaming/) 中的 MTU 选择与协商部分添加以下更改和说明。  
[流规范](/docs/specs/streaming/) 无需更改。

选项 i2p.streaming.maxMessageSize 的默认值对所有连接仍为 1730，无论使用何种密钥。  
客户端必须像往常一样使用发送和接收 MTU 的最小值。

有四个相关的 MTU 常量和变量：

- DEFAULT_MTU: 1730，保持不变，适用于所有连接
- i2cp.streaming.maxMessageSize: 默认 1730 或 1812，可通过配置更改
- ALICE_SYN_MAX_DATA: Alice 在 SYN 数据包中可包含的最大数据量
- negotiated_mtu: Alice 和 Bob MTU 的最小值，用作 Bob 到 Alice 的 SYN ACK 中以及后续双向发送的所有数据包中的最大数据大小

需要考虑五种情况：


### 1) Alice 仅使用 ElGamal
无变化，所有数据包中 MTU 为 1730。

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize 默认值：1730
- Alice 可在 SYN 中发送 MAX_PACKET_SIZE_INCLUDED，除非 != 1730 否则非必需


### 2) Alice 仅使用 ECIES
所有数据包中 MTU 为 1812。

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize 默认值：1812
- Alice 必须在 SYN 中发送 MAX_PACKET_SIZE_INCLUDED


### 3) Alice 使用双密钥且知道 Bob 使用 ElGamal
所有数据包中 MTU 为 1730。

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize 默认值：1812
- Alice 可在 SYN 中发送 MAX_PACKET_SIZE_INCLUDED，除非 != 1730 否则非必需


### 4) Alice 使用双密钥且知道 Bob 使用 ECIES
所有数据包中 MTU 为 1812。

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize 默认值：1812
- Alice 必须在 SYN 中发送 MAX_PACKET_SIZE_INCLUDED


### 5) Alice 使用双密钥且 Bob 密钥未知
在 SYN 数据包中发送 1812 作为 MAX_PACKET_SIZE_INCLUDED，但将 SYN 数据包数据限制为 1730。

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize 默认值：1812
- Alice 必须在 SYN 中发送 MAX_PACKET_SIZE_INCLUDED


### 所有情况

Alice 和 Bob 计算 negotiated_mtu，即 Alice 和 Bob MTU 的最小值，  
用作 Bob 到 Alice 的 SYN ACK 中以及后续双向发送的所有数据包中的最大数据大小。


## 理由

参见 [Java I2P 源代码](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220) 了解当前值为何为 1730。  
参见 [ECIES 规范](/docs/specs/ecies/#overhead) 了解为何 ECIES 开销比 ElGamal 少 82 字节。


## 实现说明

如果流正在创建最优大小的消息，则 ECIES-Ratchet 层不应对超出该大小的数据进行填充至关重要。

适合放入两个隧道消息的最优 Garlic 消息大小（包括 16 字节 Garlic 消息 I2NP 头、4 字节 Garlic 消息长度、8 字节 ES 标签和 16 字节 MAC）为 1956 字节。

ECIES 中推荐的填充算法如下：

- 如果 Garlic 消息的总长度为 1954-1956 字节，  
  不添加填充块（无空间）
- 如果 Garlic 消息的总长度为 1938-1953 字节，  
  添加一个填充块以恰好填充到 1956 字节。
- 否则，照常填充，例如随机填充 0-15 字节。

类似策略可用于最优单隧道消息大小（964）和三隧道消息大小（2952），尽管这些大小在实践中应较为罕见。


## 问题

1812 的值是初步的。需确认并可能调整。


## 迁移

无向后兼容性问题。  
这是一个已有选项，MTU 协商已是规范的一部分。

较旧的 ECIES 目标将支持 1730。  
任何接收到更高值的客户端将以 1730 响应，远端将像往常一样向下协商。


## 参考资料

* [CALCULATION](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220)
* [ECIES](/docs/specs/ecies/#overhead)
* [STREAMING-OPTIONS](/docs/api/streaming/)
* [STREAMING-SPEC](/docs/specs/streaming/#flags-and-option-data-fields)
