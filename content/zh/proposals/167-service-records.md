---
title: "LS2中的服务记录"
number: "167"
author: "zzz, orignal, eyedeekay"
created: "2024-06-22"
lastupdated: "2025-04-03"
status: "已关闭"
thread: "http://zzz.i2p/topics/3641"
target: "0.9.66"
toc: true
---
## 状态
2025-04-01 第二次审查通过；规范已更新；尚未实现。


## 概述

I2P 缺乏集中式的 DNS 系统。  
然而，地址簿结合 b32 主机名系统，允许路由器查找完整目的地并获取包含网关列表和密钥的租赁集（leaseSet），以便客户端可以连接到该目的地。

因此，leaseset 在某种程度上类似于 DNS 记录。但目前尚无机制可查询某个主机是否支持任何服务（无论是在该目的地还是其他目的地），类似于 [RFC 2782](https://datatracker.ietf.org/doc/html/rfc2782) 中定义的 DNS [SRV 记录](https://en.wikipedia.org/wiki/SRV_record)。

此功能的首个应用可能是点对点电子邮件。  
其他可能的应用包括：DNS、GNS、密钥服务器、证书颁发机构、时间服务器、BitTorrent、加密货币以及其他点对点应用。


## 相关提案与替代方案

### 服务列表

LS2 [提案 123](/proposals/123-new-netdb-entries/) 定义了“服务记录”，表明某个目的地正在参与全局服务。洪泛填充节点（floodfills）会将这些记录聚合为全局“服务列表”。  
由于复杂性、缺乏认证、安全性和垃圾信息等问题，该提案从未实现。

本提案的不同之处在于，它提供针对特定目的地的服务查找，而不是为某个全局服务提供全局目的地池。

### GNS

GNS 提议每个人运行自己的 DNS 服务器。  
本提案是互补的，我们可以使用服务记录来指定支持 GNS（或 DNS），标准服务名称为 "domain"，端口为 53。

### Dot well-known

曾有 [提议](http://i2pforum.i2p/viewtopic.php?p=3102) 通过 HTTP 请求 / .well-known/i2pmail.key 来查找服务。这要求每个服务都必须有一个相关网站来托管密钥。大多数用户并不运行网站。

一种变通方法是，我们可以假定 b32 地址的服务实际上运行在该 b32 地址上。因此，查找 example.i2p 的服务需要从 http://example.i2p/.well-known/i2pmail.key 获取 HTTP 内容，但查找 aaa...aaa.b32.i2p 的服务则不需要此查找，可直接连接。

但这里存在歧义，因为 example.i2p 也可以通过其 b32 地址寻址。

### MX 记录

SRV 记录只是针对任意服务的通用版 MX 记录。  
"_smtp._tcp" 就是 "MX" 记录。  
如果我们已有 SRV 记录，则无需 MX 记录，而仅靠 MX 记录无法为任意服务提供通用记录。


## 设计

服务记录放置在 [LS2](/docs/specs/common-structures/) 的选项部分中。  
LS2 的选项部分当前未使用。  
不支持 LS1。  
这类似于 [隧道带宽提案](/proposals/168-tunnel-bandwidth/)，后者为隧道构建记录定义了选项。

要查找特定主机名或 b32 的服务地址，路由器会获取 leaseset 并在属性中查找服务记录。

该服务可能托管在与 LS 相同的目的地，也可能引用不同的主机名/b32。

如果服务的目标目的地不同，则目标 LS 也必须包含一个指向自身的服务记录，表明其支持该服务。

该设计不需要洪泛填充节点的特殊支持、缓存或任何更改。  
仅 leaseset 发布者和查找服务记录的客户端需要支持这些更改。

建议对 I2CP 和 SAM 进行小幅扩展，以方便客户端检索服务记录。


## 规范

### LS2 选项规范

LS2 选项必须按键排序，以确保签名不变。

定义如下：

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := 所需服务的符号名称。必须小写。示例："smtp"。  
  允许字符为 [a-z0-9-]，且不能以 '-' 开头或结尾。  
  如果已在 [DNS-SD 服务类型注册表](http://www.dns-sd.org/ServiceTypes.html) 或 Linux /etc/services 中定义，则必须使用其中的标准标识符。
- proto := 所需服务的传输协议。必须小写，为 "tcp" 或 "udp"。  
  "tcp" 表示流式传输，"udp" 表示可回复的数据报。  
  原始数据报和 datagram2 的协议指示符可稍后定义。  
  允许字符为 [a-z0-9-]，且不能以 '-' 开头或结尾。
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := 生存时间，单位为秒的整数。正整数。示例："86400"。  
  建议最小值为 86400（一天），详见下文“建议”部分。
- priority := 目标主机的优先级，数值越低越优先。非负整数。示例："0"  
  仅在多条记录时有用，但即使只有一条记录也必须包含。
- weight := 具有相同优先级的记录的相对权重。数值越高越可能被选中。非负整数。示例："0"  
  仅在多条记录时有用，但即使只有一条记录也必须包含。
- port := 服务所在的 I2CP 端口。非负整数。示例："25"  
  支持端口 0，但不推荐。
- target := 提供服务的目的地的主机名或 b32。有效的 [主机名](/docs/overview/naming/)。必须小写。  
  示例："aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" 或 "example.i2p"。  
  除非主机名“众所周知”（即在官方或默认地址簿中），否则推荐使用 b32。
- appoptions := 应用程序特定的任意文本，不得包含 " " 或 ","。编码为 UTF-8。

### 示例

在 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p 的 LS2 中，指向一个 SMTP 服务器：

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

在 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p 的 LS2 中，指向两个 SMTP 服务器：

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

在 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p 的 LS2 中，指向自身作为 SMTP 服务器：

    "_smtp._tcp" "0 999999 25"

重定向邮件的可能格式（见下文）：

    "_smtp._tcp" "1 86400 0 0 25 smtp.postman.i2p example@mail.i2p"


### 限制

LS2 选项使用的映射数据结构格式限制键和值最多 255 字节（非字符）。  
使用 b32 目标时，optionvalue 约为 67 字节，因此仅能容纳 3 条记录。  
若 appoptions 字段较长，可能只能容纳一两条；若主机名较短，最多可容纳四到五条。  
这应已足够；多条记录的情况应属罕见。


### 与 RFC 2782 的差异

- 无尾随点
- proto 后无名称
- 必须小写
- 文本格式中记录以逗号分隔，非二进制 DNS 格式
- 不同的记录类型指示符
- 新增 appoptions 字段


### 注释

不允许使用通配符，如 (星号)、(星号)._tcp 或 _tcp。  
每个支持的服务必须拥有自己的记录。


### 服务名称注册表

未在 [DNS-SD 服务类型注册表](http://www.dns-sd.org/ServiceTypes.html) 或 Linux /etc/services 中列出的非标准标识符  
可申请并添加至 [通用结构规范](/docs/specs/common-structures/)。

特定服务的 appoptions 格式也可添加于此处。


### I2CP 规范

[I2CP 协议](/docs/specs/i2cp/) 必须扩展以支持服务查找。  
需要新增与服务查找相关的 MessageStatusMessage 和/或 HostReplyMessage 错误码。  
为使查找功能通用而不仅限于服务记录，设计为支持检索所有 LS2 选项。

实现：扩展 HostLookupMessage 以添加对哈希、主机名和目的地的 LS2 选项请求（请求类型 2-4）。  
扩展 HostReplyMessage 以在请求时包含选项映射。  
扩展 HostReplyMessage 以添加额外错误码。

选项映射可在客户端或路由器端短暂缓存或负缓存，具体取决于实现。  
建议最大时间为一小时，除非服务记录 TTL 更短。  
服务记录可由应用程序、客户端或路由器根据指定的 TTL 缓存。

按如下方式扩展规范：

#### 配置选项

向 [I2CP 配置选项](/docs/specs/i2cp/) 添加以下内容

i2cp.leaseSetOption.nnn

要放入 leaseset 的选项。仅适用于 LS2。  
nnn 从 0 开始。选项值包含 "key=value"。  
（不要包含引号）

示例：
i2cp.leaseSetOption.0=_smtp._tcp=1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p


#### HostLookup 消息

- 查找类型 2：哈希查找，请求选项映射
- 查找类型 3：主机名查找，请求选项映射
- 查找类型 4：目的地查找，请求选项映射

对于查找类型 4，第 5 项为 Destination。


#### HostReply 消息

对于查找类型 2-4，路由器必须获取 leaseset，即使查找键在地址簿中。

若成功，HostReply 将包含来自 leaseset 的选项映射，并作为第 5 项跟在目的地之后。  
如果映射中无选项，或 leaseset 为版本 1，则仍包含为空映射（两个字节：0 0）。  
将包含 leaseset 中的所有选项，而不仅是服务记录选项。  
例如，未来定义的参数选项可能存在。

若 leaseset 查找失败，回复将包含新错误码 6（Leaseset 查找失败），且不包含映射。  
当返回错误码 6 时，Destination 字段可能存在也可能不存在。  
若地址簿中的主机名查找成功，或之前的查找成功且结果已缓存，或查找消息中包含 Destination（查找类型 4），则该字段存在。

若查找类型不受支持，回复将包含新错误码 7（查找类型不受支持）。


### SAM 规范

[SAMv3 协议](/docs/api/samv3/) 必须扩展以支持服务查找。

按如下方式扩展 NAMING LOOKUP：

NAMING LOOKUP NAME=example.i2p OPTIONS=true 请求在回复中包含选项映射。

当 OPTIONS=true 时，NAME 可以是完整的 base64 目的地。

若目的地查找成功且 leaseset 中存在选项，则在回复中，目的地之后将包含一个或多个形如 OPTION:key=value 的选项。  
每个选项都有独立的 OPTION: 前缀。  
将包含 leaseset 中的所有选项，而不仅是服务记录选项。  
例如，未来定义的参数选项可能存在。  
示例：

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

包含 '=' 的键，以及包含换行符的键或值，被视为无效，键值对将从回复中移除。

若在 leaseset 中未找到选项，或 leaseset 为版本 1，则响应不包含任何选项。

若查找中包含 OPTIONS=true 且未找到 leaseset，则返回新结果值 LEASESET_NOT_FOUND。


## 命名查找替代方案

曾考虑另一种设计，通过更新 [命名规范](/docs/overview/naming/) 以处理以 '_' 开头的主机名，支持以完整主机名查找服务，例如 _smtp._tcp.example.i2p。  
该方案因两个原因被拒绝：

- 仍需对 I2CP 和 SAM 进行更改，以将 TTL 和端口信息传递给客户端。
- 它不会成为通用设施，无法用于检索未来可能定义的其他 LS2 选项。


## 建议

服务器应指定至少 86400 的 TTL，以及应用程序的标准端口。


## 高级功能

### 递归查找

可能需要支持递归查找，即依次检查每个 leaseset 是否包含指向另一个 leaseset 的服务记录，类似 DNS 方式。  
这在初始实现中可能并非必要。

待办


### 应用程序特定字段

可能需要在服务记录中包含应用程序特定数据。  
例如，example.i2p 的运营者可能希望指示邮件应转发至 example@mail.i2p。"example@" 部分需要位于服务记录的单独字段中，或从目标中剥离。

即使运营者运行自己的邮件服务，他可能也希望指示邮件应发送至 example@example.i2p。大多数 I2P 服务由单个人运行。  
因此，单独字段在此也可能有帮助。

待办：如何以通用方式实现


### 邮件所需更改

超出本提案范围。详见 [i2pforum 上的讨论](http://i2pforum.i2p/viewtopic.php?p=3102) 以获取更多细节。


## 实现说明

路由器或应用程序可选择性地根据 TTL 缓存服务记录，具体取决于实现。是否持久缓存也取决于实现。

查找时还必须查找目标 leaseset 并验证其包含 "self" 记录，然后才能将目标目的地返回给客户端。


## 安全分析

由于 leaseset 经过签名，其中的任何服务记录均由目的地的签名密钥认证。

服务记录是公开的，洪泛填充节点可见，除非 leaseset 被加密。  
任何请求 leaseset 的路由器都将能看到服务记录。

指向不同主机名/b32 目标的 SRV 记录（即非 "self"）不需要目标主机名/b32 的同意。  
尚不清楚将服务重定向到任意目的地是否可能促成某种攻击，或此类攻击的目的为何。  
然而，本提案通过要求目标也发布 "self" SRV 记录来缓解此类攻击。实现者必须检查目标 leaseset 中的 "self" 记录。


## 兼容性

LS2：无问题。所有已知实现目前忽略 LS2 中的选项字段，并能正确跳过非空选项字段。  
在 LS2 开发期间，Java I2P 和 i2pd 均已通过测试验证。  
LS2 于 2016 年在 0.9.38 版本中实现，所有路由器实现均支持良好。  
该设计不需要洪泛填充节点的特殊支持、缓存或任何更改。

命名：'_' 不是 i2p 主机名中的有效字符。

I2CP：低于支持该功能的最低 API 版本（待定）的路由器不应发送查找类型 2-4。

SAM：Java SAM 服务器忽略 OPTIONS=true 等附加键值。  
i2pd 也应如此，待验证。  
SAM 客户端除非使用 OPTIONS=true 请求，否则不会在回复中获得附加值。  
无需版本升级。


## 迁移

实现可随时添加支持，无需协调，  
除了需就 I2CP 更改的有效 API 版本达成一致。  
各实现的 SAM 兼容版本将在 SAM 规范中记录。


## 参考文献

* [DOTWELLKNOWN](http://i2pforum.i2p/viewtopic.php?p=3102)
* [I2CP](/docs/specs/i2cp/)
* [I2CP-OPTIONS](/docs/specs/i2cp/)
* [LS2](/docs/specs/common-structures/)
* [GNS](http://zzz.i2p/topcs/1545)
* [NAMING](/docs/overview/naming/)
* [Prop123](/proposals/123-new-netdb-entries/)
* [Prop168](/proposals/168-tunnel-bandwidth/)
* [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
* [RFC2782](https://datatracker.ietf.org/doc/html/rfc2782)
* [SAMv3](/docs/api/samv3/)
* [SRV](https://en.wikipedia.org/wiki/SRV_record)
