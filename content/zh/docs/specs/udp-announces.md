---
title: "UDP Tracker"
description: "I2P 中 UDP BitTorrent 宣告的协议规范"
slug: "udp-announces"
aliases:
  - "/zh/docs/specs/udp-bittorrent-announces"
  - "/zh/docs/specs/udp-bittorrent-announces/"
category: "协议"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

## 概述

本规范记录了 I2P 中 UDP bittorrent 公告的协议。有关 I2P 中 bittorrent 的整体规范，请参阅 [BitTorrent over I2P](/docs/applications/bittorrent)。有关本规范开发的背景和其他信息，请参阅 [Proposal 160](/proposals/160-udp-trackers)。

## 设计

该提案使用可回复数据报2、可回复数据报3和原始数据报，如[数据报](/docs/specs/datagrams)中定义。数据报2和数据报3是可回复数据报的新变体，在[提案163](/proposals/163-datagram2-datagram3)中定义。数据报2增加了重放抵抗和离线签名支持。数据报3比旧的数据报格式更小，但没有身份验证。

### BEP 15

作为参考，[BEP 15](http://www.bittorrent.org/beps/bep_0015.html) 中定义的消息流程如下：

```
Client                        Tracker
    Connect Req. ------------->
      <-------------- Connect Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
```
连接阶段是防止IP地址欺骗所必需的。tracker返回一个连接ID，客户端在后续的公告中使用该连接ID。这个连接ID默认在客户端一分钟后过期，在tracker两分钟后过期。

I2P将使用与BEP 15相同的消息流，以便在现有支持UDP的客户端代码库中易于采用：为了效率，以及出于下面讨论的安全原因：

```
Client                        Tracker
    Connect Req. ------------->       (Repliable Datagram2)
      <-------------- Connect Resp.   (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
             ...
```
相比流式传输（TCP）公告，这可能提供大量的带宽节省。虽然 Datagram2 的大小与流式传输 SYN 大致相同，但原始响应比流式传输 SYN ACK 要小得多。后续请求使用 Datagram3，后续响应都是原始格式。

announce 请求使用 Datagram3，这样 tracker 就无需维护一个将连接 ID 映射到 announce 目标或哈希值的大型映射表。相反，tracker 可以通过发送方哈希值、当前时间戳（基于某个时间间隔）和一个密钥值来加密生成连接 ID。当收到 announce 请求时，tracker 验证连接 ID，然后使用 Datagram3 发送方哈希值作为发送目标。

### 连接生命周期

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html) 规定连接 ID 在客户端一分钟后过期，在 tracker 两分钟后过期。这是不可配置的。这限制了潜在的效率提升，除非客户端批量处理 announce 请求，在一分钟窗口内完成所有操作。i2psnark 目前不会批量处理 announce 请求；它会将这些请求分散开来，以避免流量突发。据报告，高级用户会同时运行数千个 torrent，将如此多的 announce 请求突发到一分钟内是不现实的。

在此，我们建议扩展连接响应以添加一个可选的连接生存时间字段。如果不存在，默认值为一分钟。否则，客户端应使用以秒为单位指定的生存时间，tracker 将多维持连接 ID 一分钟。

### 与 BEP 15 的兼容性

此设计尽可能保持与 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) 的兼容性，以限制现有客户端和 tracker 所需的更改。

唯一必需的更改是在公告响应中对等节点信息的格式。在连接响应中添加生命周期字段不是必需的，但为了提高效率强烈建议添加，如上所述。

### 安全分析

UDP 宣告协议的一个重要目标是防止地址欺骗。客户端必须真实存在并捆绑一个真实的 leaseset。它必须拥有入站 tunnel 来接收连接响应。这些 tunnel 可以是零跳并即时构建，但这会暴露创建者。此协议实现了这一目标。

### 问题

- 此协议不支持盲化目标，但可以扩展以支持该功能。请参见下文。

## 规范

### 协议和端口

可回复的 Datagram2 使用 I2CP 协议 19；可回复的 Datagram3 使用 I2CP 协议 20；原始数据报使用 I2CP 协议 18。请求可以是 Datagram2 或 Datagram3。响应始终是原始格式。使用 I2CP 协议 17 的旧版可回复数据报（"Datagram1"）格式不得用于请求或回复；如果在请求/回复端口上接收到这些数据报，必须丢弃。请注意，Datagram1 协议 17 仍然用于 DHT 协议。

请求使用来自公告 URL 的 I2CP "to port"；详见下文。请求的 "from port" 由客户端选择，但应该非零，并且与 DHT 使用的端口不同，以便响应可以轻松分类。tracker 应该拒绝在错误端口上收到的请求。

响应使用来自请求的I2CP"目标端口"。请求的"源端口"就是请求的"目标端口"。

### 公告 URL

announce URL格式在[BEP 15](http://www.bittorrent.org/beps/bep_0015.html)中没有规定，但与明网一样，UDP announce URL的格式为`udp://host:port/path`。路径被忽略，可以为空，但在明网上通常为`/announce`。`:port`部分应该始终存在，但是，如果省略了`:port`部分，则使用默认的I2CP端口6969，因为这是明网上的常见端口。还可能附加cgi参数`&a=b&c=d`，这些参数可能会被处理并在announce请求中提供，参见[BEP 41](http://www.bittorrent.org/beps/bep_0041.html)。如果没有参数或路径，尾随的`/`也可以省略，如[BEP 41](http://www.bittorrent.org/beps/bep_0041.html)中所暗示的。

### 数据报格式

所有数值都以网络字节序（大端序）发送。不要期望数据包具有确切的特定大小。未来的扩展可能会增加数据包的大小。

#### 连接请求

客户端到 tracker。16 字节。必须是可回复的 Datagram2。与 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) 中相同。无变化。

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">protocol_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0x41727101980 // magic constant</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
#### 连接响应

Tracker 到客户端。16 或 18 字节。必须是原始数据。与 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) 相同，除了以下说明的部分。

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">lifetime</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // Change from BEP 15</td>
    </tr>
  </tbody>
</table>
响应必须发送到接收请求时的"from port"所对应的I2CP"to port"。

lifetime 字段是可选的，表示 connection_id 客户端生存时间（以秒为单位）。默认值为 60，如果指定的话最小值为 60。最大值为 65535 或大约 18 小时。tracker 应该维护 connection_id 的时间比客户端生存时间多 60 秒。

#### 宣告请求

客户端到 tracker。最小 98 字节。必须是可回复的 Datagram3。与 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) 相同，除了以下说明的部分。

connection_id 是在连接响应中收到的。

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">info_hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">peer_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">56</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">downloaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">left</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">uploaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">80</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">event</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // 0: none; 1: completed; 2: started; 3: stopped</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">84</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">IP address</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // default, unused in I2P</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">88</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">92</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">num_want</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1 // default</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">port</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// must be same as I2CP from port</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">98</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">options</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // As specified in BEP 41</td>
    </tr>
  </tbody>
</table>
与 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) 的变更:

- key 被忽略
- IP 地址未使用
- port 可能被忽略，但必须与 I2CP from port 相同
- options 部分（如果存在）的定义参见 [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)

响应必须发送到作为请求"from port"接收到的I2CP"to port"。不要使用来自announce请求的端口。

#### 公告响应

Tracker 到客户端。最少 20 字节。必须是原始数据。与 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) 相同，除非下文另有说明。

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">interval</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">leechers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">seeders</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32 * n 32-byte hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">binary hashes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// Change from BEP 15</td>
    </tr>
  </tbody>
</table>
与 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) 的变更：

- 不同于 6 字节的 IPv4+端口或 18 字节的 IPv6+端口，我们返回 32 字节的倍数"紧凑响应"，其中包含 SHA-256 二进制 peer 哈希值。与 TCP 紧凑响应一样，我们不包含端口。

响应必须发送到作为请求"from port"接收到的I2CP"to port"。不要使用来自通告请求的端口。

I2P 数据报的最大尺寸很大，约为 64 KB；但是，为了可靠传输，应避免使用大于 4 KB 的数据报。为了提高带宽效率，tracker 应该将最大节点数限制在大约 50 个，这对应于各层开销之前约 1600 字节的数据包，并且在分片后应在双 tunnel 消息负载限制内。

与 BEP 15 中一样，这里没有包含要跟随的对等节点地址数量的计数（BEP 15 中为 IP/端口，这里为哈希值）。虽然 BEP 15 中没有考虑到这一点，但可以定义一个全零的对等节点结束标记来表示对等节点信息已完整，后面跟随一些扩展数据。

为了未来扩展的可能性，客户端应该忽略32字节全零hash以及其后的任何数据。tracker应该拒绝来自全零hash的announce，尽管该hash已经被Java router禁止。

#### 抓取

本规范不要求实现来自 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) 的 Scrape 请求/响应，但如果需要可以实现，无需更改。客户端必须首先获取连接 ID。scrape 请求始终是可回复的 Datagram3。scrape 响应始终是原始数据。

#### 错误响应

Tracker 到客户端。最少 8 字节（如果消息为空）。必须是原始格式。与 [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) 中相同。无变化。

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3 // error</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">message</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
## 扩展

不包含扩展位或版本字段。客户端和 tracker 不应假定数据包具有特定大小。这样，可以在不破坏兼容性的情况下添加额外字段。如果需要，建议使用 [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) 中定义的扩展格式。

连接响应被修改以添加一个可选的连接ID生存期。

如果需要支持盲化目标，我们可以将盲化的35字节地址添加到announce请求的末尾，或者使用[BEP 41](http://www.bittorrent.org/beps/bep_0041.html)格式在响应中请求盲化哈希（参数待定）。盲化的35字节对等体地址集合可以添加到announce回复的末尾，在一个全零的32字节哈希之后。

## 实现指南

有关非集成、非I2CP客户端和tracker面临的挑战的讨论，请参见上述设计部分。

### 客户端

对于给定的 tracker 主机名，客户端应该优先使用 UDP 而非 HTTP URL，并且不应该同时向两者发起通告。

已支持 BEP 15 的客户端应该只需要进行少量修改。

如果客户端支持DHT或其他数据报协议，它应该选择不同的端口作为请求的"源端口"，这样回复就会返回到该端口，不会与DHT消息混淆。客户端只接收原始数据报作为回复。Tracker永远不会向客户端发送可回复的datagram2。

拥有默认开放tracker列表的客户端应在已知开放tracker支持UDP后，更新列表以添加UDP URL。

客户端可以实现或不实现请求的重传。如果实现了重传，初始超时时间应至少为15秒，并且每次重传时将超时时间翻倍（指数退避）。

客户端在收到错误响应后必须退避。

### Tracker

支持现有 BEP 15 的 tracker 应该只需要进行小幅修改。此规范与 2014 年的提案不同，tracker 必须支持在同一端口上接收可回复的 datagram2 和 datagram3。

为了最小化 tracker 资源需求，此协议旨在消除 tracker 存储客户端哈希到连接 ID 映射以供后续验证的任何要求。这是可能的，因为公告请求数据包是一个可回复的 Datagram3 数据包，所以它包含发送者的哈希。

推荐的实现方式是：

- 将当前 epoch 定义为具有连接生存期分辨率的当前时间，`epoch = now / lifetime`。
- 定义一个密码学哈希函数 `H(secret, clienthash, epoch)`，它生成 8 字节输出。
- 生成用于所有连接的随机常量 secret。
- 对于连接响应，生成 `connection_id = H(secret, clienthash, epoch)`
- 对于宣告请求，通过验证 `connection_id == H(secret, clienthash, epoch) || connection_id == H(secret, clienthash, epoch - 1)` 来验证当前 epoch 中接收到的连接 ID

## 参考资料

- **[BEP15]** [BEP 15 - UDP Tracker Protocol](http://www.bittorrent.org/beps/bep_0015.html)
- **[BEP41]** [BEP 41 - UDP Tracker Protocol Extensions](http://www.bittorrent.org/beps/bep_0041.html)
- **[DATAGRAMS]** [数据报规范](/docs/specs/datagrams)
- **[Prop160]** [提案 160 - UDP Trackers](/proposals/160-udp-trackers)
- **[Prop163]** [提案 163 - Datagram2/Datagram3](/proposals/163-datagram2-datagram3)
- **[SAMv3]** [SAMv3 API](/docs/api/samv3)
- **[SPEC]** [BitTorrent over I2P](/docs/applications/bittorrent)
