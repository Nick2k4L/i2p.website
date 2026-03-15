---
title: "IPv6传输增强"
aliases:
  - "/zh/spec/proposals/158"
  - "/zh/spec/proposals/158/"
number: "158"
author: "zzz, 原作者"
created: "2021-03-19"
lastupdated: "2021-04-26"
status: "Closed"
thread: "http://zzz.i2p/topics/3060"
target: "0.9.50"
toc: true
---
## 说明
网络部署和测试正在进行中。  
可能会有小幅修订。


## 概述

本提案旨在为 SSU 和 NTCP2 传输协议实现对 IPv6 的增强支持。


## 动机

随着全球 IPv6 的普及以及 IPv6-only 配置（尤其是在移动设备上）变得越来越普遍，  
我们需要改进对 IPv6 的支持，并消除“所有路由器都具备 IPv4 能力”这一假设。


### 连通性检查

在为隧道选择对等体，或为消息路由选择 OBEP/IBGW 路径时，  
判断路由器 A 是否能连接到路由器 B 是有帮助的。  
通常这意味着要确定 A 是否具备某种传输方式和地址类型（IPv4/v6）的出站能力，  
该类型需与 B 所公布的入站地址之一匹配。

然而，在许多情况下我们并不知道 A 的能力，只能做出假设。  
如果 A 是隐藏的或处于防火墙之后，其地址不会被发布，我们也无法直接获知其能力——  
因此我们默认它具备 IPv4 能力，但不具备 IPv6 能力。  
解决方案是在路由器信息（Router Info）中添加两个新的“能力”（caps），用于指示 IPv4 和 IPv6 的出站能力。


### IPv6 引荐者（Introducers）

我们关于 SSU 的规范在是否支持通过 IPv6 引荐者进行 IPv4 引荐方面存在错误和不一致。  
无论如何，Java I2P 和 i2pd 都从未实现过此功能。  
这一点需要修正。


### IPv6 引荐（Introductions）

我们关于 SSU 的规范明确指出：  
不支持 IPv6 引荐。  
这是基于“IPv6 永远不会被防火墙阻挡”的假设。  
这显然不成立，我们需要改进对处于防火墙后的 IPv6 路由器的支持。


### 引荐示意图

图例：----- 表示 IPv4，====== 表示 IPv6

**当前仅支持 IPv4：**

```
        Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**IPv4 引荐，IPv6 引荐者：**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**IPv6 引荐，IPv6 引荐者：**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```

**IPv6 引荐，IPv4 引荐者：**

```
Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```


## 设计

需要实现以下三项变更：

- 在路由器地址（Router Address）的能力中添加 "4" 和 "6"，以表示支持 IPv4 和 IPv6 出站
- 支持通过 IPv6 引荐者进行 IPv4 引荐
- 支持通过 IPv4 和 IPv6 引荐者进行 IPv6 引荐


## 规范

### 4/6 能力（Caps）

该功能最初在没有正式提案的情况下实现，但由于它是 IPv6 引荐所必需的，因此在此一并说明。

定义两个新能力 "4" 和 "6"。  
这些新能力将被添加到路由器地址（Router Address）的 "caps" 属性中，而不是路由器信息（Router Info）的 caps 中。  
目前我们尚未为 NTCP2 定义 "caps" 属性。  
当前，带有引荐者的 SSU 地址默认是 IPv4 的。我们完全不支持 IPv6 引荐。  
不过，本提案与 IPv6 引荐兼容。见下文。

此外，某些路由器可能通过 Yggdrasil 等覆盖网络（overlay network）实现连接，  
但不希望公布地址，或其地址不具备标准的 IPv4 或 IPv6 格式。  
新的能力系统应足够灵活，以支持此类网络。

定义以下变更：

NTCP2：添加 "caps" 属性

SSU：支持没有 host 或引荐者的路由器地址，以表示支持 IPv4、IPv6 或两者皆可的出站连接。

两种传输方式均需定义以下 caps 值：

- "4"：支持 IPv4
- "6"：支持 IPv6

单个地址可支持多个值。见下文。  
若路由器地址中未包含 "host" 值，则至少需要一个上述 caps。  
若路由器地址中包含 "host" 值，则最多可选一个上述 caps。  
未来可定义额外的传输 caps，以表示对覆盖网络或其他连接方式的支持。


#### 使用场景和示例

SSU：

带 host 的 SSU：4/6 可选，最多只能有一个。  
示例：SSU caps="4" host="1.2.3.4" key=... port="1234"

仅支持一种协议出站，另一种已发布：仅使用 caps，4 或 6。  
示例：SSU caps="6"

带引荐者的 SSU：从不组合使用。必须包含 4 或 6。  
示例：SSU caps="4" iexp0=... ihost0=... iport0=... itag0=... key=...

隐藏 SSU：仅使用 caps，可为 4、6 或 46。允许多个值。  
无需分别使用一个带 4 和一个带 6 的地址。  
示例：SSU caps="46"

NTCP2：

带 host 的 NTCP2：4/6 可选，最多只能有一个。  
示例：NTCP2 caps="4" host="1.2.3.4" i=... port="1234" s=... v="2"

仅支持一种协议出站，另一种已发布：仅使用 caps、s、v，支持 4/6/y，允许多个值。  
示例：NTCP2 caps="6" i=... s=... v="2"

隐藏 NTCP2：仅使用 caps、s、v，支持 4/6，允许多个值。无需分别使用一个带 4 和一个带 6 的地址。  
示例：NTCP2 caps="46" i=... s=... v="2"



### IPv6 引荐者用于 IPv4

需要进行以下更改以修正规范中的错误和不一致。  
我们也称此为提案的“第 1 部分”。

#### 规范变更

SSU 规范当前说明（IPv6 注释）：

自版本 0.9.8 起支持 IPv6。发布的中继地址可以是 IPv4 或 IPv6，Alice 与 Bob 的通信可通过 IPv4 或 IPv6 进行。

添加以下内容：

尽管规范自 0.9.8 版本起已更改，但 Alice 与 Bob 之间通过 IPv6 的通信实际上直到 0.9.50 版本才真正支持。  
早期版本的 Java 路由器错误地为 IPv6 地址发布了 'C' 能力，  
即使它们实际上并未通过 IPv6 充当引荐者。  
因此，路由器仅应在路由器版本为 0.9.50 或更高时，才信任 IPv6 地址上的 'C' 能力。


SSU 规范当前说明（中继请求 Relay Request）：

仅当 IP 地址与数据包源地址和端口不同时才包含该 IP 地址。  
在当前实现中，IP 长度始终为 0，端口始终为 0，  
接收方应使用数据包的源地址和端口。  
此消息可通过 IPv4 或 IPv6 发送。如果是 IPv6，Alice 必须包含她的 IPv4 地址和端口。

添加以下内容：

当通过 IPv6 发送此消息以引荐 IPv4 地址时，必须包含 IP 和端口。  
此功能自 0.9.50 版本起支持。


### IPv6 引荐（Introductions）

所有三个 SSU 中继消息（RelayRequest、RelayResponse 和 RelayIntro）都包含 IP 长度字段，  
用于指示（Alice、Bob 或 Charlie）后续 IP 地址的长度。

因此，无需更改消息格式。  
只需对规范进行文本修改，说明允许使用 16 字节的 IP 地址。

需要对规范进行以下更改。  
我们也称此为提案的“第 2 部分”。


#### 规范变更

SSU 规范当前说明（IPv6 注释）：

Bob 与 Charlie 以及 Alice 与 Charlie 的通信仅通过 IPv4 进行。

SSU 规范当前说明（中继请求 Relay Request）：

目前没有计划实现 IPv6 的中继功能。

更改为：

自 0.9.xx 版本起支持 IPv6 中继功能。


SSU 规范当前说明（中继响应 Relay Response）：

Charlie 的 IP 地址必须是 IPv4，因为 Alice 在打洞（Hole Punch）后将向该地址发送 SessionRequest。  
目前没有计划实现 IPv6 中继。

更改为：

Charlie 的 IP 地址可以是 IPv4，或自 0.9.xx 版本起支持 IPv6。  
该地址是 Alice 在打洞后将发送 SessionRequest 的目标地址。  
自 0.9.xx 版本起支持 IPv6 中继。


SSU 规范当前说明（中继引荐 Relay Intro）：

在当前实现中，Alice 的 IP 地址始终为 4 字节，因为 Alice 试图通过 IPv4 连接到 Charlie。  
此消息必须通过已建立的 IPv4 连接发送，  
因为这是 Bob 将 Charlie 的 IPv4 地址返回给 Alice 的唯一方式（在 RelayResponse 中）。

更改为：

对于 IPv4，Alice 的 IP 地址始终为 4 字节，因为 Alice 试图通过 IPv4 连接到 Charlie。  
自 0.9.xx 版本起支持 IPv6，Alice 的 IP 地址可以是 16 字节。

对于 IPv4，此消息必须通过已建立的 IPv4 连接发送，  
因为这是 Bob 将 Charlie 的 IPv4 地址返回给 Alice 的唯一方式（在 RelayResponse 中）。  
自 0.9.xx 版本起支持 IPv6，此消息也可通过已建立的 IPv6 连接发送。

同时添加：

自 0.9.xx 版本起，任何发布带有引荐者的 SSU 地址都必须在 "caps" 选项中包含 "4" 或 "6"。


## 迁移

所有旧版路由器应忽略 NTCP2 中的 caps 属性，以及 SSU caps 属性中未知的能力字符。

任何带有引荐者但未包含 "4" 或 "6" 能力的 SSU 地址，均默认用于 IPv4 引荐。


## 参考资料

* [CAPS](http://zzz.i2p/topics/3050)
* [NTCP2](/docs/specs/ntcp2/)
* [SSU](/docs/specs/ssu2/)
* [SSU-SPEC](/docs/legacy/ssu/)
