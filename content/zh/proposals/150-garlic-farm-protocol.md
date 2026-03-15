---
title: "大蒜农场协议"
number: "150"
author: "zzz"
created: "2019-05-02"
lastupdated: "2019-05-20"
status: "开放"
thread: "http://zzz.i2p/topics/2234"
toc: true
---
## 概述

这是 Garlic Farm 有线协议的规范，  
基于 JRaft、其用于 TCP 上实现的“exts”代码，  
以及其“dmprinter”示例应用 [JRAFT](https://github.com/datatechnology/jraft)。

我们未能找到任何具有文档化有线协议的实现。  
然而，JRaft 的实现足够简单，我们可以  
检查其代码并随后记录其协议。  
本提案即为此工作的成果。

这将成为路由器发布 Meta LeaseSet 条目时协调的后端。参见提案 123。


## 目标

- 小代码体积
- 基于现有实现
- 不使用序列化的 Java 对象或任何 Java 特有功能或编码
- 引导过程不在本协议范围内。假定至少有一个其他服务器是硬编码的，或通过本协议之外的方式配置
- 支持带外和 I2P 内使用场景


## 设计

Raft 协议不是一个具体的协议；它仅定义了一个状态机。  
因此我们记录 JRaft 的具体协议并基于其构建我们的协议。  
除了添加身份验证握手外，对 JRaft 协议没有其他更改。

Raft 选举一个 Leader，其职责是发布日志。  
日志包含 Raft 配置数据和应用数据。  
应用数据包含每个服务器路由器的状态以及 Meta LS2 集群的目的地。  
服务器使用共同算法确定 Meta LS2 的发布者和内容。  
Meta LS2 的发布者不一定是 Raft Leader。


## 规范

有线协议通过 SSL 套接字或非 SSL I2P 套接字进行。  
I2P 套接字通过 HTTP 代理进行代理。  
不支持明文非 SSL 套接字。

### 握手与认证

JRaft 未定义此部分。

目标：

- 用户/密码认证方式
- 版本标识符
- 集群标识符
- 可扩展
- 在用于 I2P 套接字时易于代理
- 不必要地暴露服务器为 Garlic Farm 服务器
- 简单协议，因此不需要完整的 Web 服务器实现
- 兼容常见标准，以便实现可选择使用标准库

我们将使用类似 WebSocket 的握手和  
HTTP Digest 认证 [RFC 2617](https://tools.ietf.org/html/rfc2617)。  
不支持 RFC 2617 Basic 认证。  
通过 HTTP 代理代理时，按 [RFC 2616](https://tools.ietf.org/html/rfc2616) 中指定的方式与代理通信。

#### 凭据

用户名和密码是按集群还是按服务器，取决于具体实现。


#### HTTP 请求 1

发起方将发送以下内容。

所有行均以 CRLF 结尾，符合 HTTP 要求。

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: close
  (any other headers ignored)
  (blank line)

  CLUSTER 是集群名称（默认为 "farm"）
  VERSION 是 Garlic Farm 版本（当前为 "1"）

```


#### HTTP 响应 1

如果路径不正确，接收方将发送标准的 "HTTP/1.1 404 Not Found" 响应，  
如 [RFC 2616](https://tools.ietf.org/html/rfc2616) 所述。

如果路径正确，接收方将发送标准的 "HTTP/1.1 401 Unauthorized" 响应，  
包含 WWW-Authenticate HTTP digest 认证头，  
如 [RFC 2617](https://tools.ietf.org/html/rfc2617) 所述。

双方随后将关闭套接字。


#### HTTP 请求 2

发起方将发送以下内容，  
如 [RFC 2617](https://tools.ietf.org/html/rfc2617) 所述。

所有行均以 CRLF 结尾，符合 HTTP 要求。

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: keep-alive, Upgrade
  Upgrade: websocket
  (Sec-Websocket-* headers if proxied)
  Authorization: (HTTP digest authorization header as in RFC 2617)
  (any other headers ignored)
  (blank line)

  CLUSTER 是集群名称（默认为 "farm"）
  VERSION 是 Garlic Farm 版本（当前为 "1"）

```


#### HTTP 响应 2

如果认证不正确，接收方将再次发送标准的 "HTTP/1.1 401 Unauthorized" 响应，  
如 [RFC 2617](https://tools.ietf.org/html/rfc2617) 所述。

如果认证正确，接收方将发送以下响应，  
如 WebSocket 协议所述。

所有行均以 CRLF 结尾，符合 HTTP 要求。

```text

HTTP/1.1 101 Switching Protocols
  Connection: Upgrade
  Upgrade: websocket
  (Sec-Websocket-* headers)
  (any other headers ignored)
  (blank line)

```

收到此响应后，套接字保持打开状态。  
下方定义的 Raft 协议在同一套接字上开始。


#### 缓存

凭据应至少缓存一小时，以便后续连接可直接跳转到  
上述“HTTP 请求 2”。


### 消息类型

有两种消息类型：请求和响应。  
请求可能包含日志条目，大小可变；  
响应不包含日志条目，大小固定。

消息类型 1-4 是 Raft 定义的标准 RPC 消息。  
这是核心 Raft 协议。

消息类型 5-15 是 JRaft 定义的扩展 RPC 消息，  
用于支持客户端、动态服务器变更和高效日志同步。

消息类型 16-17 是 Raft 第 7 节中定义的日志压缩 RPC 消息。


| 消息 | 编号 | 发送方 | 接收方 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| RequestVoteRequest | 1 | Candidate | Follower | 标准 Raft RPC；不得包含日志条目 |
| RequestVoteResponse | 2 | Follower | Candidate | 标准 Raft RPC |
| AppendEntriesRequest | 3 | Leader | Follower | 标准 Raft RPC |
| AppendEntriesResponse | 4 | Follower | Leader / Client | 标准 Raft RPC |
| ClientRequest | 5 | Client | Leader / Follower | 响应为 AppendEntriesResponse；必须仅包含应用日志条目 |
| AddServerRequest | 6 | Client | Leader | 必须仅包含单个 ClusterServer 日志条目 |
| AddServerResponse | 7 | Leader | Client | Leader 还将发送 JoinClusterRequest |
| RemoveServerRequest | 8 | Follower | Leader | 必须仅包含单个 ClusterServer 日志条目 |
| RemoveServerResponse | 9 | Leader | Follower | |
| SyncLogRequest | 10 | Leader | Follower | 必须仅包含单个 LogPack 日志条目 |
| SyncLogResponse | 11 | Follower | Leader | |
| JoinClusterRequest | 12 | Leader | New Server | 邀请加入；必须仅包含单个配置日志条目 |
| JoinClusterResponse | 13 | New Server | Leader | |
| LeaveClusterRequest | 14 | Leader | Follower | 离开命令 |
| LeaveClusterResponse | 15 | Follower | Leader | |
| InstallSnapshotRequest | 16 | Leader | Follower | Raft 第 7 节；必须仅包含单个 SnapshotSyncRequest 日志条目 |
| InstallSnapshotResponse | 17 | Follower | Leader | Raft 第 7 节 |


### 建立

HTTP 握手后，建立序列为：

```text

新服务器 Alice              随机 Follower Bob

  ClientRequest   ------->
          <---------   AppendEntriesResponse

  如果 Bob 表示它是 Leader，则继续如下。
  否则，Alice 必须断开与 Bob 的连接并连接到 Leader。


  新服务器 Alice              Leader Charlie

  ClientRequest   ------->
          <---------   AppendEntriesResponse
  AddServerRequest   ------->
          <---------   AddServerResponse
          <---------   JoinClusterRequest
  JoinClusterResponse  ------->
          <---------   SyncLogRequest
                       OR InstallSnapshotRequest
  SyncLogResponse  ------->
  OR InstallSnapshotResponse

```

断开序列：

```text

Follower Alice              Leader Charlie

  RemoveServerRequest   ------->
          <---------   RemoveServerResponse
          <---------   LeaveClusterRequest
  LeaveClusterResponse  ------->

```

选举序列：

```text

Candidate Alice               Follower Bob

  RequestVoteRequest   ------->
          <---------   RequestVoteResponse

  如果 Alice 赢得选举：

  Leader Alice                Follower Bob

  AppendEntriesRequest   ------->
  (heartbeat)
          <---------   AppendEntriesResponse

```


### 定义

- 源（Source）：标识消息的发起者
- 目标（Destination）：标识消息的接收者
- Term：参见 Raft。初始化为 0，单调递增
- Index：参见 Raft。初始化为 0，单调递增


### 请求

请求包含一个头部和零个或多个日志条目。  
请求包含固定大小的头部和可变大小的可选日志条目。


#### 请求头部

请求头部为 45 字节，如下所示。  
所有值均为无符号大端序。

```text

消息类型：      1 字节
  源：            ID，4 字节整数
  目标：          ID，4 字节整数
  Term：          当前 Term（见注释），8 字节整数
  上一个日志 Term： 8 字节整数
  上一个日志 Index：8 字节整数
  提交 Index：     8 字节整数
  日志条目大小：   总字节数，4 字节整数
  日志条目：       见下文，总长度按指定

```


#### 注释

在 RequestVoteRequest 中，Term 是候选者的 Term。  
否则，它是 Leader 的当前 Term。

在 AppendEntriesRequest 中，当日志条目大小为零时，  
此消息为心跳（保活）消息。


#### 日志条目

日志包含零个或多个日志条目。  
每个日志条目如下所示。  
所有值均为无符号大端序。

```text

Term：           8 字节整数
  值类型：         1 字节
  条目大小：       字节数，4 字节整数
  条目：           指定长度

```


#### 日志内容

所有值均为无符号大端序。

| 日志值类型 | 编号 |
| :--- | :--- |
| Application | 1 |
| Configuration | 2 |
| ClusterServer | 3 |
| LogPack | 4 |
| SnapshotSyncRequest | 5 |


#### Application

应用内容为 UTF-8 编码的 [JSON](https://www.json.org/)。  
参见下方应用层部分。


#### Configuration

用于 Leader 序列化新集群配置并复制到对等节点。  
包含零个或多个 ClusterServer 配置。

```text

日志 Index：  8 字节整数
  上一个日志 Index：  8 字节整数
  每个服务器的 ClusterServer 数据：
    ID：                4 字节整数
    端点数据长度： 字节数，4 字节整数
    端点数据：     形如 "tcp://localhost:9001" 的 ASCII 字符串，长度按指定

```


#### ClusterServer

集群中服务器的配置信息。  
仅包含在 AddServerRequest 或 RemoveServerRequest 消息中。

在 AddServerRequest 消息中使用时：

```text

ID：                4 字节整数
  端点数据长度： 字节数，4 字节整数
  端点数据：     形如 "tcp://localhost:9001" 的 ASCII 字符串，长度按指定

```


在 RemoveServerRequest 消息中使用时：

```text

ID：                4 字节整数

```


#### LogPack

仅包含在 SyncLogRequest 消息中。

传输前进行 gzip 压缩：

```text

索引数据长度： 字节数，4 字节整数
  日志数据长度：   字节数，4 字节整数
  索引数据：     每个索引 8 字节，长度按指定
  日志数据：       长度按指定

```


#### SnapshotSyncRequest

仅包含在 InstallSnapshotRequest 消息中。

```text

上一个日志 Index：  8 字节整数
  上一个日志 Term：   8 字节整数
  配置数据长度： 字节数，4 字节整数
  配置数据：     长度按指定
  偏移量：          数据库中数据的偏移量（字节），8 字节整数
  数据长度：        字节数，4 字节整数
  数据：            长度按指定
  是否完成：         完成为 1，未完成为 0（1 字节）

```


### 响应

所有响应均为 26 字节，如下所示。  
所有值均为无符号大端序。

```text

消息类型：   1 字节
  源：         ID，4 字节整数
  目标：       通常为实际目标 ID（见注释），4 字节整数
  Term：       当前 Term，8 字节整数
  下一个 Index： 初始化为 Leader 最后日志 Index + 1，8 字节整数
  是否接受：     接受为 1，否则为 0（见注释），1 字节

```


#### 注释

目标 ID 通常是此消息的实际目标。  
但对于 AppendEntriesResponse、AddServerResponse 和 RemoveServerResponse，  
它是当前 Leader 的 ID。

在 RequestVoteResponse 中，Is Accepted 为 1 表示投票给候选者（请求者），  
为 0 表示不投票。


## 应用层

每个服务器定期在 ClientRequest 中向日志发布应用数据。  
应用数据包含每个服务器路由器的状态以及 Meta LS2 集群的目的地。  
服务器使用共同算法确定 Meta LS2 的发布者和内容。  
日志中“最佳”近期状态的服务器是 Meta LS2 发布者。  
Meta LS2 的发布者不一定是 Raft Leader。


### 应用数据内容

应用内容为 UTF-8 编码的 [JSON](https://json.org/)，  
以简化和扩展性。  
完整规范待定。  
目标是提供足够数据以编写算法确定“最佳”  
路由器来发布 Meta LS2，并使发布者拥有足够信息  
以对 Meta LS2 中的目的地进行加权。  
数据将包含路由器和目的地的统计信息。

数据可选择性包含关于其他服务器健康状况的远程感知数据，  
以及获取 Meta LS 的能力。  
这些数据在第一版中不支持。

数据可选择性包含管理员客户端发布的配置信息。  
这些数据在第一版中不支持。

如果列出“name: value”，则指定 JSON 映射键和值。  
否则，规范待定。

集群数据（顶层）：

- cluster: 集群名称
- date: 此数据的日期（long，自纪元以来的毫秒数）
- id: Raft ID（整数）

配置数据（config）：

- 任何配置参数

MetaLS 发布状态（meta）：

- destination: metals 目的地，base64
- lastPublishedLS: 如果存在，上次发布的 metals 的 base64 编码
- lastPublishedTime: 毫秒，或从未发布为 0
- publishConfig: 发布者配置状态 off/on/auto
- publishing: metals 发布者状态布尔值 true/false

路由器数据（router）：

- lastPublishedRI: 如果存在，上次发布的路由器信息的 base64 编码
- uptime: 运行时间（毫秒）
- Job lag
- 探索性隧道
- 参与的隧道
- 配置带宽
- 当前带宽

目的地（destinations）：
列表

目的地数据：

- destination: 目的地，base64
- uptime: 运行时间（毫秒）
- 配置隧道数
- 当前隧道数
- 配置带宽
- 当前带宽
- 配置连接数
- 当前连接数
- 黑名单数据

远程路由器感知数据：

- 最近看到的 RI 版本
- LS 获取时间
- 连接测试数据
- 最近的 floodfill 档案数据
  针对昨天、今天和明天的时间段

远程目的地感知数据：

- 最近看到的 LS 版本
- LS 获取时间
- 连接测试数据
- 最近的 floodfill 档案数据
  针对昨天、今天和明天的时间段

Meta LS 感知数据：

- 最近看到的版本
- 获取时间
- 最近的 floodfill 档案数据
  针对昨天、今天和明天的时间段


## 管理接口

待定，可能为单独提案。  
第一版不需要。  

管理接口需求：

- 支持多个主目的地，即多个虚拟集群（farms）
- 提供共享集群状态的全面视图 —— 所有成员发布的统计信息、当前 Leader 是谁等
- 能够强制从集群中移除参与者或 Leader
- 能够强制发布 metaLS（如果当前节点是发布者）
- 能够排除 metaLS 中的哈希（如果当前节点是发布者）
- 支持批量部署的配置导入/导出功能


## 路由器接口

待定，可能为单独提案。  
i2pcontrol 不是第一版必需的，详细变更将包含在单独提案中。

Garlic Farm 到路由器 API 的需求（JVM 内 Java 或 i2pcontrol）

- getLocalRouterStatus()
- getLocalLeafHash(Hash masterHash)
- getLocalLeafStatus(Hash leaf)
- getRemoteMeasuredStatus(Hash masterOrLeaf) // 可能不在 MVP 中
- publishMetaLS(Hash masterHash, List<MetaLease> contents) // 或签名的 MetaLeaseSet？谁签名？
- stopPublishingMetaLS(Hash masterHash)
- 认证待定？


## 理由

Atomix 过于庞大，且不允许我们自定义以将协议路由到 I2P。  
此外，其有线格式未文档化，且依赖 Java 序列化。


## 注释



## 问题

- 客户端无法发现并连接到未知的 Leader。  
  稍微修改即可让 Follower 在 AppendEntriesResponse 中以日志条目形式发送配置。


## 迁移

无向后兼容性问题。


## 参考文献

* [JRAFT](https://github.com/datatechnology/jraft)
* [JSON](https://json.org/)
* [RAFT](/docs/research/ongaro2014-raft.pdf)
* [RFC-2616](https://tools.ietf.org/html/rfc2616)
* [RFC-2617](https://tools.ietf.org/html/rfc2617)
* [WEBSOCKET](https://en.wikipedia.org/wiki/WebSocket)
