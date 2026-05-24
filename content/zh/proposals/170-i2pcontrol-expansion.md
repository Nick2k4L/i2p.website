---
title: "I2PControl 扩展"
number: "170"
author: "Nick2k4"
created: "2026-05-20"
lastupdated: "2026-05-20"
status: "打开"
toc: true
---

## 概述

该提案向 i2pcontrol API 暴露了新的信息，从而提供了更大的灵活性。这些信息包括：添加、删除、检索和修改地址簿及隐藏服务（hidden services）。该提案还暴露了有关您的路由器的更多信息，例如对等节点（peers）、新闻（news）、网络数据库（netdb）等。

## 动机

此提案的使用场景是创建一个统一且简化的路由器控制台，该控制台可被所有路由器实现共享，并与标准的i2p隧道套件配合使用。本质上，该提案旨在为I2P网络中的用户带来更直观、更友好的使用体验。

该提案还将为 I2P API 提供更大的灵活性，使应用程序能够实现和管理 I2P 管理界面。将此类信息暴露给 i2pcontrol 可使用户开发更高级的应用程序，并为远程管理提供更好的支持。

## 设计

当用户与 i2pcontrol API 交互时，他们将能够访问提供上述信息的新端点。例如，i2pcontrol API 将提供新的方法 `TunnelManager` 和 `AddressBook`，允许用户输入参数来创建、删除、检索和修改隧道及地址簿。此外，已有的 `RouterInfo` 方法将新增参数，以暴露有关路由器的信息。

## 安全影响

此提案不会带来预期的额外安全影响，因为所暴露的信息已可通过其他方式访问。然而，必须确保为访问 i2pcontrol API 配备了适当的认证和授权机制，以防止未授权访问敏感信息或对路由器的控制。

## API 规范与方法

所有请求都遵循 JSON-RPC 2.0 结构：

```json
{
  "jsonrpc": "2.0",
  "method": "MethodName",
  "params": {
    // method-specific parameters
  },
  "id": 1
}
```
### 方法 - RouterInfo（获取器）

以下包含 `RouterInfo` 方法的新参数及其返回值：

- `i2p.router.news` - 返回所有路由器新闻条目。返回类型 - `String`
- `i2p.router.id` - 以 Base64 字符串形式返回路由器哈希，或 `null`。返回类型 - `String`
- `i2p.router.clockskew` - 返回平均对等体时钟偏差，或 `null`。返回类型 - `long`
- `i2p.router.info` - 以 Base64 字符串形式返回序列化的 RouterInfo，或 `null`。返回类型 - `String`
- `i2p.router.logs` - 返回最近的路由器日志消息。返回类型 - `List<String>`
- `i2p.router.logs.clear` - 清空路由器日志缓冲区并返回 `"success"`。返回类型 - `String`

- `i2p.router.net.total.received.bytes` - 返回自启动以来接收的总字节数。*(源自 i2pd)* 返回类型 - `long`
- `i2p.router.net.total.sent.bytes` - 返回自启动以来发送的总字节数。*(源自 i2pd)* 返回类型 - `long`
- `i2p.router.net.total.transit.bytes` - 返回自启动以来中转转发的总字节数。*(源自 i2pd)* 返回类型 - `long`
- `i2p.router.net.bw.transit.15s` - 返回15秒内的平均中转带宽（字节/秒）。*(源自 i2pd)* 返回类型 - `long`

- `i2p.router.net.tunnels.shareratio` - 返回隧道共享比率。返回类型 - `double`
- `i2p.router.net.tunnels.participating.info` - 返回参与隧道的信息。返回类型 - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.i2ptunnel` - 返回已配置的 I2PTunnel 控制器信息（所有内容的快速统计）。返回类型 - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.exploratory.inbound` - 返回探索性入站隧道数量。返回类型 - `int`
- `i2p.router.net.tunnels.exploratory.outbound` - 返回探索性出站隧道数量。返回类型 - `int`
- `i2p.router.net.tunnels.exploratory.info.list` - 返回探索性隧道信息列表。返回类型 - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.client.inbound` - 返回客户端入站隧道数量。返回类型 - `int`
- `i2p.router.net.tunnels.client.outbound` - 返回客户端出站隧道数量。返回类型 - `int`
- `i2p.router.net.tunnels.client.info.list` - 返回客户端隧道信息列表。返回类型 - `List<Map<String, Object>>`

- `i2p.router.net.status.v6` - 返回 IPv6 网络状态码。*(源自 i2pd)* 返回类型 - `int`
- `i2p.router.net.error` - 返回 IPv4 网络错误码。*(源自 i2pd)* 返回类型 - `int`
- `i2p.router.net.error.v6` - 返回 IPv6 网络错误码。*(源自 i2pd)* 返回类型 - `int`
- `i2p.router.net.testing` - 返回 IPv4 网络是否处于测试状态（0 或 1）。*(源自 i2pd)* 返回类型 - `int`
- `i2p.router.net.testing.v6` - 返回 IPv6 网络是否处于测试状态（0 或 1）。*(源自 i2pd)* 返回类型 - `int`

- `i2p.router.net.tunnels.successrate` - 返回最近的隧道构建成功率（%）。（*采用自 i2pd*）返回类型 - `double`
- `i2p.router.net.tunnels.totalsuccessrate` - 返回自启动以来的隧道构建总成功率（%）。（*采用自 i2pd*）返回类型 - `double`
- `i2p.router.net.tunnels.queue` - 返回隧道构建请求队列大小。（*采用自 i2pd*）返回类型 - `int`
- `i2p.router.net.tunnels.tbmqueue` - 返回隧道构建消息队列大小。（*采用自 i2pd*）返回类型 - `int`

- `i2p.router.netdb.peers` - 返回已知对等体哈希的列表。返回类型 - `List<String>`
- `i2p.router.netdb.activepeers.info` - 返回活动对等体的序列化 RouterInfo 数据。返回类型 - `List<String>`
- `i2p.router.netdb.ntcp.limit` - 返回 NTCP 连接限制。返回类型 - `int`
- `i2p.router.netdb.ssu.limit` - 返回 SSU 连接限制。返回类型 - `int`
- `i2p.router.netdb.bannedpeers` - 返回被封禁的对等体及其封禁详情。返回类型 - `Map<String, Map<String, Object>>`
- `i2p.router.netdb.activepeers.list` - 返回活动对等体的哈希列表。返回类型 - `List<String>`
- `i2p.router.netdb.peers.list` - 返回已知对等体的哈希列表。返回类型 - `List<String>`
- `i2p.router.netdb.peers.info` - 返回已知对等体的序列化 RouterInfo 数据。返回类型 - `List<String>`
- `i2p.router.netdb.activepeers.stats` - 返回活动对等体的统计信息。返回类型 - `List<Map<String, Object>>`

- `i2p.router.addressbook.private.list` - 返回私有地址簿条目。返回类型 - `List<Map<String, String>>`
- `i2p.router.addressbook.local.list` - 返回本地地址簿条目。返回类型 - `List<Map<String, String>>`
- `i2p.router.addressbook.router.list` - 返回路由器地址簿条目。返回类型 - `List<Map<String, String>>`
- `i2p.router.addressbook.published.list` - 返回已发布的地址簿条目。返回类型 - `List<Map<String, String>>`
- `i2p.router.addressbook.subscriptions` - 返回订阅文件路径和条目。返回类型 - `Map<String, Object>`
- `i2p.router.addressbook.config` - 返回地址簿配置路径和条目。返回类型 - `Map<String, Object>`

示例：

```json
{
    "jsonrpc": "2.0",
    "method": "RouterInfo",
    "params": {
        "i2p.router.id": "",
    },
    "id": 1
}
```
返回：

```json
{
    "jsonrpc": "2.0",
    "result": "{ data }",
    "id": 1
}
```
### 方法 - 地址簿（设置器）

对于 `AddressBook` 方法，向地址簿删除和添加条目需要三个参数：

- `Type` - 对应地址簿类型：
  - `private`
  - `local`
  - `router`
  - `published`
- `Hostname` - 对应地址簿条目关联的主机名或域名。
- `Destination` - 对应地址簿条目关联的目标地址。
- `Delete` - 此参数为可选，用于删除地址簿条目。如果未提供此参数，该方法将向地址簿添加新条目。

示例：

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "Type": "private",
    "Hostname": "example.i2p",
    "Destination": "exampleDestinationString",
    "Delete": "" <--- this parameter is optional
  },
  "id": 1
}
```
返回：

```json
{
  "jsonrpc": "2.0",
  "success": true or false,        
  "message": "Deleted/Added (hostname) in (address book type) address book" OR "Failed to delete/add (hostname) to (address book type) address book",
  "id": 1
}
```
用于编辑 AddressBookSubscriptions：

- `SetSubscriptions` - 此参数用于为地址簿条目设置订阅。它接受一个字符串列表作为参数。

示例：

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetSubscriptions": ["notbob.i2p", "helloworld.i2p", ...]
  },
  "id": 1
}
```
返回：

```json
{
  "jsonrpc": "2.0",
  "success": true,
  "message": "Successfully modified: /path/to/subscriptions.txt"
}
```
用于编辑 AddressBookConfig：

- `SetConfig` - 此参数用于设置地址簿条目的配置。

它接受一个 JSON 对象作为参数，该对象包含配置设置。

可用/常见的配置参数：

- `subscriptions` - 包含订阅URL列表的文件。
- `update_delay` - 更新间隔（小时）。
- `published_addressbook` - 已发布地址簿的路径。
- `router_addressbook` - 路由器地址簿的路径。
- `local_addressbook` - 本地地址簿的路径。
- `private_addressbook` - 私有地址簿的路径。
- `proxy_port` - eepProxy 端口。
- `proxy_host` - eepProxy 主机名。
- `should_publish` - 是否更新已发布的地址簿。
- `etags` - 包含订阅URL的etag的文件。
- `last_modified` - 包含订阅URL最后修改时间戳的文件。
- `log` - 日志文件路径。
- `theme` - 主题。

示例：

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetConfig": {
      "subscriptions": "subscriptions.txt",
      "update_delay": "12",
      "published_addressbook": "../eepsite/docroot/hosts.txt",
      "router_addressbook": "hosts.txt",
      "local_addressbook": "../userhosts.txt",
      "private_addressbook": "../privatehosts.txt",
      "proxy_port": "4444",
      "proxy_host": "127.0.0.1",
      "should_publish": "true",
      "etags": "etags.txt",
      "last_modified": "last_modified.txt",
      "log": "log.txt",
      "theme": "light"
    }
  },
  "id": 1
}
```
返回：

```json
{
  "jsonrpc": "2.0",
  "result": {
    "success": true,
    "message": "Successfully modified: /path/to/config.txt"
  },
  "id": 1
}
```
### 方法 - TunnelManager（1 个标记的 getter，其余为 setter）

`TunnelManager` 方法用于创建、编辑、获取、启动、停止、重启和删除 I2PTunnel 控制器。

必需参数：

- `Name` - 隧道的名称。这是隧道的标识符。
- `Action` - 要执行的操作：
  - `create`（创建）
  - `edit`（编辑）
  - `get`（获取）
  - `start`（启动）
  - `stop`（停止）
  - `restart`（重启）
  - `delete`（删除）

可选参数：

- `All` - 布尔值，表示是否将操作应用于所有隧道。仅对 `start`、`stop` 和 `restart` 操作有效。

`create` 支持的隧道类型：

- `client`（客户端）
- `httpclient`（HTTP 客户端）
- `ircclient`（IRC 客户端）
- `socks`（SOCKS 代理）
- `socksirc`（SOCKS + IRC 组合客户端）
- `connectclient`（连接客户端）
- `streamrclient`（流媒体客户端）

- `server`
- `httpserver`
- `httpbidirserver`
- `ircserver`
- `streamrserver`

创建/编辑隧道的常用参数：

- `Type` - 隧道类型。`create` 时必需。
- `NewName` - 编辑时可选的新名称。
- `Port` - 本地监听端口。
- `TargetHost` 或 `Host` - 服务端隧道的目标主机。
- `TargetPort` - 服务端隧道的目标端口。
- `TargetDestination` 或 `Destination` - 需要目标的客户端隧道的目的地址。
- `StartOnLoad` - 布尔值，表示隧道加载后是否应自动启动。
- `Description` - 隧道描述。
- `ReachableBy` - 隧道监听的接口/地址。
- `Shared` - 布尔值，表示客户端隧道是否应被共享。
- `UseSSL` - 布尔值，在支持的地方启用 SSL。
- `TunnelLength` - 隧道长度，`0` 到 `3`。
- `TunnelVariance` - 隧道长度变化值，`-2` 到 `2`。
- `TunnelQuantity` - 隧道数量，`1` 到 `6`。
- `TunnelBackupQuantity` - 备用隧道数量，`0` 到 `3`。
- `SigType` - 签名密钥类型。
- `EncType` - 加密类型。
- `CustomOptions` - 自定义隧道选项。

客户端代理选项：

- `ProxyList`
- `UseOutproxyPlugin`
- `ProxyAuth`
- `ProxyUsername`
- `ProxyPassword`
- `OutproxyAuth`
- `OutproxyUsername`
- `OutproxyPassword`
- `OutproxyType`
- `SSLProxies`
- `JumpList`

客户端管理选项：

- `ConnectDelay`
- `Profile`
- `DelayOpen`
- `Reduce`
- `ReduceCount`
- `ReduceTime`
- `Close`
- `CloseTime`
- `NewDest`
- `PersistentClientKey`
- `PrivKeyFile`

HTTP 客户端过滤选项：

- `AllowUserAgent`
- `AllowReferer`
- `AllowAccept`
- `AllowInternalSSL`

服务器选项：

- `WebsiteHostname` 或 `SpoofedHost`
- `BlockAccessInProxies`
- `BlockUserAgents`
- `UserAgents`
- `UniqueLocalAddressPerClient`
- `BlockReferers`
- `MultiHoming`
- `AccessOption`
- `AccessList`
- `FilterFilePath`
- `MaxConcurrentConns`
- `ClientPerMinute`
- `ClientPerHour`
- `ClientPerDay`
- `TotalInPerMinute`
- `TotalInPerHour`
- `TotalInPerDay`
- `PostLimit`
- `PostLimitTime`
- `PerClientPeriod`
- `TotalPeriod`
- `TotalBanTime`

LeaseSet 选项：

- `EncryptLeaseSet` - 以下之一：
  - `disable`
  - `encrypted (aes)`
  - `blinded`
  - `blinded with lookup password`
  - `encrypted (psk)`
  - `encrypted with lookup password (psk)`
  - `encrypted with per-user key (psk)`
  - `encrypted with lookup password and per-user key (psk)`
  - `encrypted with per-user key (dh)`
  - `encrypted with lookup password and per-user key (dh)`
- `OptionalLookup`
- `LeaseSetClientAuths`

创建示例：

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "create",
    "Type": "client",
    "Port": 7656,
    "TargetDestination": "exampleDestinationString",
    "StartOnLoad": false,
    ....
  },
  "id": 1
}
```
返回：

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - created tunnel example-client" OR "error - { error message }",
    "results": [ {/* information about where persistent keys are stored */} ]
  },
  "id": 1
}
```
编辑示例：

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "edit",
    "NewName": "renamed-client",
    "Port": 7657,
    "TargetDestination": "newDestinationString",
    "StartOnLoad": true
  },
  "id": 1
}
```
返回：

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - edited tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
获取示例（仅限 GETTER）返回 - `Map<String, Object>`（信息）和 `String`（状态）：

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "get"
  },
  "id": 1
}
```
返回：

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - options for example-client" OR "error - { error message }",
    "info": {
      "client": true,
      "status": "running",
      "persistentClientKey": false,
      "offlineKeys": false,
      "targetDestination": "exampleDestinationString",
      "localDestination": "exampleBase64Destination",
      "destination": "exampleBase64Destination",
      "destinationB32": "example.b32.i2p",
      "rawConfig": {
        "name": "example-client",
        "type": "client"
      }
    }
  },
  "id": 1
}
```
启动、停止、重启、删除示例，它们遵循相同的结构，只是使用了不同的 `Action` 参数：

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "start"
  },
  "id": 1
}
```
返回：

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - starting tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
### 方法 - ClientServicesInfo *（采用自 i2pd）*

`ClientServicesInfo` 方法返回路由器上运行的客户端服务的状态信息。在 `params` 中包含所需的服务键（值任意）以请求每个服务的状态。

支持的参数：

- `I2PTunnel` - 返回配置的隧道名称到其地址的映射，分为 `client` 和 `server` 两个子对象。
- `HTTPProxy` - 返回 HTTP 代理的启用状态和地址。
- `SOCKS` - 返回 SOCKS 代理的启用状态和地址。
- `SAM` - 返回 SAM 桥接的启用状态以及活动会话信息。
- `BOB` - 返回 BOB 桥接的启用状态。（在 Java I2P 中已弃用；始终返回 `false`。）
- `I2CP` - 返回 I2CP 服务器的启用状态。

示例：

```json
{
  "jsonrpc": "2.0",
  "method": "ClientServicesInfo",
  "params": {
    "I2PTunnel": "",
    "SAM": ""
  },
  "id": 1
}
```
返回：

```json
{
  "jsonrpc": "2.0",
  "result": {
    "I2PTunnel": {
      "client": {"my-client": {"address": "example.b32.i2p"}},
      "server": {"my-server": {"address": "example.b32.i2p", "port": 8080}}
    },
    "SAM": {
      "enabled": true,
      "sessions": {}
    }
  },
  "id": 1
}
```
## 兼容性

应保持与现有 i2pcontrol API 的兼容性，因为新增的方法和参数不会干扰现有功能。使用 i2pcontrol API 的现有应用程序应无需修改即可继续正常运行，同时新应用程序可利用本提案提供的额外信息和功能。

## 实现

### Java I2P

该提案尚未在 Java I2P 中实现，但相关代码已存在于 [i2p.plugins.i2pcontrol](https://github.com/i2p/i2p.plugins.i2pcontrol) 仓库的拉取请求 [#6](https://github.com/i2p/i2p.plugins.i2pcontrol/pull/6) 中。这样做是为了在不影响现有代码的前提下，允许对新方法进行测试和开发。一旦代码准备好用于生产环境，将会被合并到主 I2P 仓库的 i2pcontrol 目录中。

### i2pd

标记为“（采用自 i2pd）”的方法和参数已在 i2pd 中实现，并且在本提案中保持不变。i2pd 的扩展部分无需因本提案而进行修改。本提案中未标记的部分在 i2pd 中尚未实现。

### Go-I2P

go-i2p 致力于推进此提案，以实现并增强其路由器控制台应用。未来将采用并实施该提案。

### Emissary

目前尚不清楚 Emissary 采用此提案的可能性，但 Emissary 很可能会像 go-i2p 一样从此提案中受益。

## 性能

预计不会影响性能。
