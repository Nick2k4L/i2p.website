---
title: "OBEP传输到1-of-N或N-of-N隧道"
number: "125"
author: "zzz, str4d"
created: "2016-03-10"
lastupdated: "2017-04-07"
status: "开放"
thread: "http://zzz.i2p/topics/2099"
toc: true
---
## 概述

本提案涵盖两项用于提升网络性能的改进：

- 通过向 OBEP 提供一组备选方案而非单一选项，将 IBGW 的选择权委托给 OBEP。

- 在 OBEP 上启用多播数据包路由。


## 动机

在直接连接的情况下，其理念是通过赋予 OBEP 更灵活地连接 IBGW 的能力来减少连接拥塞。能够指定多个隧道也使我们可以在 OBEP 上实现多播（通过将消息发送到所有指定的隧道）。

作为本提案中“委托”部分的替代方案，可以发送 LeaseSet 哈希，类似于现有机制中指定目标 [RouterIdentity](/docs/specs/common-structures/#common-structure-specification) 哈希的能力。这将导致消息更小，并可能获取更新的 LeaseSet。然而：

1. 这会迫使 OBEP 执行一次查找。

2. LeaseSet 可能未发布到 floodfill 节点，因此查找会失败。

3. LeaseSet 可能是加密的，因此 OBEP 无法获取其中的 leases。

4. 指定 LeaseSet 会向 OBEP 泄露消息的 [Destination](/docs/specs/common-structures/#destination)，而否则 OBEP 只能通过遍历网络中所有 LeaseSet 并查找 Lease 匹配项才能发现该信息。


## 设计

发起方（OBGW）将把部分（或全部）目标 [Leases](/docs/specs/common-structures/#lease) 放入交付指令 [TUNNEL-DELIVERY](/docs/specs/i2np/#tunnel-message-delivery-instructions) 中，而不是仅选择一个。

OBEP 将从这些 Lease 中选择一个进行交付。如果可用，OBEP 会优先选择它已经连接或已知的 Lease。这将使 OBEP 到 IBGW 的路径更快、更可靠，并减少整个网络的连接数。

我们在 TUNNEL-DELIVERY 的交付类型中有一个未使用的类型（0x03），以及标志位中的两个剩余位（位 0 和 1），可用于实现这些功能。


## 安全影响

本提案不会改变关于 OBGW 目标 Destination 或其对 NetDB 视图的信息泄露量：

- 控制 OBEP 并从 NetDB 抓取 LeaseSet 的攻击者，已经可以通过搜索 TunnelId / RouterIdentity 对来确定消息是否发送给特定 Destination。最坏情况下，TMDI 中包含多个 Lease 可能会加快攻击者在其数据库中找到匹配项的速度。

- 运营恶意 Destination 的攻击者已经可以通过向不同 floodfill 发布包含不同入站隧道的 LeaseSet，并观察 OBGW 通过哪些隧道连接，来获取连接受害者对 NetDB 视图的信息。从他们的角度来看，OBEP 选择使用哪个隧道在功能上与 OBGW 自行选择是等同的。

多播标志会向 OBEP 泄露 OBGW 正在执行多播的事实。这在实现高层协议时会产生性能与隐私之间的权衡。由于这是一个可选标志，用户可以根据其应用做出适当决策。不过，对于兼容的应用程序，默认启用此行为可能带来好处，因为多种应用程序广泛使用该功能将减少关于某条消息具体来自哪个应用的信息泄露。


## 规范

首片段交付指令将修改如下：

```
+----+----+----+----+----+----+----+----+
  |flag|  Tunnel ID (opt)  |              |
  +----+----+----+----+----+              +
  |                                       |
  +                                       +
  |         To Hash (optional)            |
  +                                       +
  |                                       |
  +                        +----+----+----+
  |                        |dly | Message
  +----+----+----+----+----+----+----+----+
   ID (opt) |extended opts (opt)|cnt | (o)
  +----+----+----+----+----+----+----+----+
   Tunnel ID N   |                        |
  +----+----+----+                        +
  |                                       |
  +                                       +
  |         To Hash N (optional)          |
  +                                       +
  |                                       |
  +              +----+----+----+----+----+
  |              | Tunnel ID N+1 (o) |    |
  +----+----+----+----+----+----+----+    +
  |                                       |
  +                                       +
  |         To Hash N+1 (optional)        |
  +                                       +
  |                                       |
  +                                  +----+
  |                                  | sz
  +----+----+----+----+----+----+----+----+
       |
  +----+

flag ::
       1 字节
       位顺序：76543210
       位 6-5：交付类型
                 0x03 = TUNNELS
       位 0：是否多播？若为 0，交付到其中一个隧道
                         若为 1，交付到所有隧道
                         若交付类型不是 TUNNELS，则应设为 0 以兼容未来用途

Count ::
       1 字节
       可选，仅当交付类型为 TUNNELS 时存在
       2-255 - 后续 id/hash 对的数量

Tunnel ID :: TunnelId
To Hash ::
       每个 36 字节
       可选，仅当交付类型为 TUNNELS 时存在
       id/hash 对

总长度：典型长度为：
       75 字节用于计数为 2 的 TUNNELS 交付（未分片的隧道消息）；
       79 字节用于计数为 2 的 TUNNELS 交付（首片段）

其余交付指令保持不变
```


## 兼容性

只有 OBGW 和 OBEP 需要理解新规范。因此，我们可以通过将新功能的使用条件设置为目标 I2P 版本来使此更改与现有网络兼容：

* OBGW 在构建出站隧道时必须根据对端在 [RouterInfo](/docs/specs/common-structures/#routerinfo) 中声明的 I2P 版本选择兼容的 OBEP。

* 声明目标版本的节点必须支持解析新标志，并且不得将指令视为无效而拒绝。


## 参考资料

* [Destination](/docs/specs/common-structures/#destination)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [RouterIdentity](/docs/specs/common-structures/#routeridentity)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TUNNEL-DELIVERY](/docs/specs/common-structures/#tunnelmessagedeliveryinstructions)
* [TunnelId](/docs/specs/common-structures/#tunnelid)
* [VERSIONS](/docs/specs/i2np/#protocol-versions)
