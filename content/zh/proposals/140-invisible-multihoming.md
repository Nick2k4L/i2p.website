---
title: "不可见多重宿主"
number: "140"
author: "str4d"
created: "2017-05-22"
lastupdated: "2017-07-04"
status: "打开"
thread: "http://zzz.i2p/topics/2335"
toc: true
---
## 概述

本提案概述了一种协议设计，旨在使 I2P 客户端、服务或外部负载均衡器进程能够透明地管理多个路由器，这些路由器共同托管一个单一的 [Destination](/docs/specs/common-structures/#destination)。

该提案目前并未指定具体实现。它可以作为 [I2CP](/docs/specs/i2cp/) 的扩展来实现，也可以作为一个新协议实现。


## 动机

多宿主（Multihoming）是指使用多个路由器托管同一个 Destination。当前在 I2P 中实现多宿主的方式是将相同的 Destination 独立运行在每个路由器上；客户端在任意时刻所使用的路由器，是最后一个发布 LeaseSet 的那个。

这是一种权宜之计，且显然无法在大规模网站场景下有效工作。假设我们有 100 个用于多宿主的路由器，每个拥有 16 条隧道。这意味着每 10 分钟就有 1600 次 LeaseSet 发布，即几乎每秒 3 次。这将使 floodfill 节点不堪重负，并触发限流机制。而这还尚未计入查找流量的影响。

提案 123 通过引入“元 LeaseSet”（meta-LeaseSet）解决了这个问题，该结构列出了 100 个真实 LeaseSet 的哈希值。一次查找变为两阶段过程：首先查找元 LeaseSet，然后查找其中一个命名的 LeaseSet。这很好地解决了查找流量问题，但单独使用时会带来显著的隐私泄露风险：通过监控发布的元 LeaseSet，可以确定哪些多宿主路由器在线，因为每个真实的 LeaseSet 都对应唯一的路由器。

我们需要一种方法，使得 I2P 客户端或服务能将单个 Destination 分布到多个路由器上，且从 LeaseSet 本身的角度来看，其行为与使用单个路由器无法区分。


## 设计

### 定义

    User
        希望为其 Destination 实现多宿主的个人或组织。此处以单个 Destination 为例进行说明，不失一般性（WLOG）。

    Client
        运行在 Destination 后面的应用程序或服务。它可以是客户端、服务器端或点对点应用；我们称之为“客户端”，意指其连接到 I2P 路由器。

        客户端由三个部分组成，这三个部分可能位于同一进程中，也可能分布在多个进程或机器上（在多客户端设置中）：

        Balancer
            客户端中负责管理对等体选择和隧道构建的部分。任一时刻只有一个 Balancer，它与所有 I2P 路由器通信。可能存在故障转移用的备用 Balancer。

        Frontend
            客户端中可并行运行的部分。每个 Frontend 与单个 I2P 路由器通信。

        Backend
            在所有 Frontend 之间共享的客户端部分。它不直接与任何 I2P 路由器通信。

    Router
        由用户运行的 I2P 路由器，位于 I2P 网络与用户网络之间的边界（类似于企业网络中的边缘设备）。它在 Balancer 的指令下建立隧道，并为客户端或 Frontend 路由数据包。

### 高层次概述

设想以下期望的配置：

- 一个具有单一 Destination 的客户端应用。
- 四个路由器，每个管理三条入站隧道。
- 所有十二条隧道应发布在一个 LeaseSet 中。

### 单客户端模式

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]-----
                 |-{ [Tunnel 3]===/               \
                 |                                 \
                 |-{ [Tunnel 4]===\                 \
  [Destination]  |-{ [Tunnel 5]====[Router 2]-----   \
    \            |-{ [Tunnel 6]===/               \   \
     [LeaseSet]--|                               [Client]
                 |-{ [Tunnel 7]===\               /   /
                 |-{ [Tunnel 8]====[Router 3]-----   /
                 |-{ [Tunnel 9]===/                 /
                 |                                 /
                 |-{ [Tunnel 10]==\               /
                 |-{ [Tunnel 11]===[Router 4]-----
                  -{ [Tunnel 12]==/
```

### 多客户端模式

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]---------[Frontend 1]
                 |-{ [Tunnel 3]===/          \                    \
                 |                            \                    \
                 |-{ [Tunnel 4]===\            \                    \
  [Destination]  |-{ [Tunnel 5]====[Router 2]---\-----[Frontend 2]   \
    \            |-{ [Tunnel 6]===/          \   \                \   \
     [LeaseSet]--|                         [Balancer]            [Backend]
                 |-{ [Tunnel 7]===\          /   /                /   /
                 |-{ [Tunnel 8]====[Router 3]---/-----[Frontend 3]   /
                 |-{ [Tunnel 9]===/            /                    /
                 |                            /                    /
                 |-{ [Tunnel 10]==\          /                    /
                 |-{ [Tunnel 11]===[Router 4]---------[Frontend 4]
                  -{ [Tunnel 12]==/
```

### 客户端通用流程

- 加载或生成一个 Destination。

- 为每个路由器打开一个与该 Destination 关联的会话。

- 定期（大约每十分钟一次，具体频率可根据隧道存活状态调整）：

  - 从每个路由器获取其快速节点层（fast tier）。

  - 使用所有路由器的快速节点并集，为每个路由器构建出入站隧道。

    - 默认情况下，通往特定路由器的隧道将使用该路由器快速节点层中的节点，但协议本身不强制执行此规则。

  - 收集所有活动路由器上的活跃入站隧道集合，并创建一个 LeaseSet。

  - 通过一个或多个路由器发布该 LeaseSet。

### 与 I2CP 的差异

为了创建和管理此配置，客户端需要具备超出当前 [I2CP](/docs/specs/i2cp/) 所提供功能的新功能：

- 告诉路由器构建隧道，但不为其创建 LeaseSet。
- 获取当前入站隧道池中的隧道列表。

此外，以下功能将显著提升客户端管理隧道的灵活性：

- 获取路由器快速节点层的内容。
- 告诉路由器使用指定的节点列表构建入站或出站隧道。

### 协议概要

```
         Client                           Router

                    --------------------->  Create Session
   Session Status  <---------------------
                    --------------------->  Get Fast Tier
        Peer List  <---------------------
                    --------------------->  Create Tunnel
    Tunnel Status  <---------------------
                    --------------------->  Get Tunnel Pool
      Tunnel List  <---------------------
                    --------------------->  Publish LeaseSet
                    --------------------->  Send Packet
      Send Status  <---------------------
  Packet Received  <---------------------
```

### 消息

**Create Session**  
- 为给定的 Destination 创建一个会话。

**Session Status**  
- 确认会话已建立，客户端现在可以开始构建隧道。

**Get Fast Tier**  
- 请求路由器当前考虑用于构建隧道的节点列表。

**Peer List**  
- 路由器已知的节点列表。

**Create Tunnel**  
- 请求路由器通过指定节点构建一条新隧道。

**Tunnel Status**  
- 特定隧道构建的结果，一旦可用即返回。

**Get Tunnel Pool**  
- 请求获取 Destination 的入站或出站隧道池中的当前隧道列表。

**Tunnel List**  
- 所请求隧道池的隧道列表。

**Publish LeaseSet**  
- 请求路由器通过 Destination 的一条出站隧道发布提供的 LeaseSet。无需回复状态；路由器应持续重试，直到确认 LeaseSet 已成功发布。

**Send Packet**  
- 来自客户端的出站数据包。可选地指定必须（或应该？）通过哪条出站隧道发送该数据包。

**Send Status**  
- 通知客户端发送数据包的成功或失败状态。

**Packet Received**  
- 发送给客户端的入站数据包。可选地指定数据包是通过哪条入站隧道接收的（？）


## 安全影响

从路由器的角度来看，此设计在功能上等同于现状。路由器仍然负责构建所有隧道，维护自身的节点画像，并强制隔离路由器与客户端操作。在默认配置下完全相同，因为针对该路由器的隧道是从其自身的快速节点层中构建的。

从 netDb 的角度来看，通过此协议创建的单个 LeaseSet 与现状无异，因为它利用了已有的功能。然而，对于接近 16 个 Lease 的大型 LeaseSet，观察者可能能够判断该 LeaseSet 是否为多宿主：

- 当前快速节点层的最大大小为 75 个节点。入站网关（IBGW，即 Lease 中公布的节点）从该层的一部分中选择（按哈希随机分区，非按数量）：

      1 跳
          整个快速节点层

      2 跳
          快速节点层的一半
          （直到 2014 年中期的默认值）

      3+ 跳
          快速节点层的四分之一
          （3 跳为当前默认值）

  这意味着平均而言，IBGW 将来自 20-30 个节点的集合。

- 在单宿主设置中，完整的 16 隧道 LeaseSet 将从最多（例如）20 个节点的集合中随机选择 16 个 IBGW。

- 在使用默认配置的 4 路由器多宿主设置中，完整的 16 隧道 LeaseSet 将从最多 80 个节点的集合中随机选择 16 个 IBGW，尽管路由器之间可能存在部分共用节点。

因此，在默认配置下，可能通过统计分析推断出 LeaseSet 是由本协议生成的。甚至可能推断出路由器的数量，尽管快速节点层的节点更替（churn）会削弱此类分析的有效性。

由于客户端完全控制所选节点，因此可通过从更小的节点集合中选择 IBGW 来减少或消除此类信息泄露。


## 兼容性

此设计与网络完全向后兼容，因为 LeaseSet 格式没有任何更改。所有路由器都需要知晓新协议，但这不是问题，因为它们均由同一实体控制。


## 性能与可扩展性说明

本提案未改变每个 LeaseSet 最多 16 个 Lease 的上限。对于需要超过此数量隧道的 Destination，有两种可能的网络修改方案：

- 增加 LeaseSet 大小的上限。这是最简单的实现方式（尽管在广泛使用前仍需全网支持），但可能导致查找速度变慢，因为数据包更大。最大可行的 LeaseSet 大小由底层传输的 MTU 决定，因此约为 16kB。

- 实现提案 123 的分层 LeaseSet。结合本提案，子 LeaseSet 的 Destination 可分布于多个路由器上，实际上类似于明网服务的多个 IP 地址。


## 致谢

感谢 psi 的讨论促成了本提案。


## 参考文献

* [Destination](/docs/specs/common-structures/#destination)
* [I2CP](/docs/specs/i2cp/)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [Prop123](/proposals/123-new-netdb-entries/)
