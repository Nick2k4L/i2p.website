---
title: "i2pcontrol-expansion"
number: "170"
author: "Nick2k4"
created: "2026-05-20"
lastupdated: "2026-05-20"
status: "열기"
toc: true
---

개요 ========

이 제안은 i2pcontrol API에 새로운 정보를 공개하여 더 큰 유연성을 제공합니다. 여기에는 addressbook 및 숨겨진 서비스의 추가, 삭제, 검색, 수정이 포함됩니다. 또한 이 제안은 피어, 뉴스, netdb 등 라우터에 대한 더 많은 정보를 공개합니다.

동기 부여 ==========

이 제안의 이유는 애플리케이션이 I2P API를 통해 보다 유연하게 I2P 관리 인터페이스를 구현하고 관리할 수 있도록 하기 위한 것입니다. i2pcontrol에 이러한 정보를 노출함으로써 사용자는 보다 고급 기능의 애플리케이션을 개발하고 원격 관리를 위한 더 나은 지원을 제공할 수 있게 됩니다.

디자인 ======

사용자가 i2pcontrol API와 상호작용할 때 위에서 언급한 정보를 제공하는 새로운 엔드포인트에 접근할 수 있게 됩니다. 예를 들어, i2pcontrol API는 사용자가 매개변수를 입력하여 터널과 주소록을 생성, 삭제, 조회 및 수정할 수 있도록 해주는 새로운 메서드인 `TunnelManager`와 `AddressBook`을 공개할 것입니다. 또한 기존의 `RouterInfo` 메서드는 라우터에 대한 정보를 제공하기 위해 새로운 매개변수를 갖게 됩니다.

보안상의 영향
=====================

이 제안으로부터 예상되는 추가적인 보안 영향은 없습니다. 왜냐하면 노출되는 정보는 이미 다른 수단을 통해 접근이 가능하기 때문입니다. 그러나 민감한 정보에 대한 무단 접근이나 라우터 제어를 방지하기 위해, i2pcontrol API에 대한 적절한 인증 및 권한 부여 메커니즘이 마련되어 있는지 확인하는 것이 중요합니다.

API 사양 및 메서드 ===========================

모든 요청은 JSON-RPC 2.0 구조를 따릅니다:

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
방법 - RouterInfo -------------------

아래에는 `RouterInfo` 메서드의 새로운 매개변수와 그 반환값이 나와 있습니다:

- `i2p.router.news` - 라우터 뉴스 항목을 모두 반환합니다.
- `i2p.router.id` - 라우터 해시를 Base64 문자열로 반환하거나, `null`을 반환합니다.
- `i2p.router.clockskew` - 평균 피어 시계 편차를 반환하거나, `null`을 반환합니다.
- `i2p.router.info` - 직렬화된 RouterInfo를 Base64 문자열로 반환하거나, `null`을 반환합니다.
- `i2p.router.logs` - 최근 라우터 로그 메시지를 반환합니다.
- `i2p.router.logs.clear` - 라우터 로그 버퍼를 지우고 `"success"`를 반환합니다.

- `i2p.router.net.total.received.bytes` - 시작 이후 총 수신된 바이트 수를 반환합니다. *(i2pd에서 채택됨)*
- `i2p.router.net.total.sent.bytes` - 시작 이후 총 전송된 바이트 수를 반환합니다. *(i2pd에서 채택됨)*
- `i2p.router.net.total.transit.bytes` - 시작 이후 총 전달된 트랜짓 바이트 수를 반환합니다. *(i2pd에서 채택됨)*
- `i2p.router.net.bw.transit.15s` - 15초 평균 트랜짓 대역폭(바이트/초)을 반환합니다. *(i2pd에서 채택됨)*

- `i2p.router.net.tunnels.shareratio` - 터널 공유 비율을 반환합니다.
- `i2p.router.net.tunnels.participating.info` - 참여 중인 터널 정보를 반환합니다.
- `i2p.router.net.tunnels.i2ptunnel` - 구성된 I2PTunnel 컨트롤러 정보를 반환합니다(전체에 대한 빠른 통계).
- `i2p.router.net.tunnels.exploratory.inbound` - 탐색용 수신 터널 수를 반환합니다.
- `i2p.router.net.tunnels.exploratory.outbound` - 탐색용 발신 터널 수를 반환합니다.
- `i2p.router.net.tunnels.exploratory.info.list` - 탐색용 터널 정보 목록을 반환합니다.
- `i2p.router.net.tunnels.client.inbound` - 클라이언트 수신 터널 수를 반환합니다.
- `i2p.router.net.tunnels.client.outbound` - 클라이언트 발신 터널 수를 반환합니다.
- `i2p.router.net.tunnels.client.info.list` - 클라이언트 터널 정보 목록을 반환합니다.

- `i2p.router.net.status.v6` - IPv6 네트워크 상태 코드를 반환합니다. *(i2pd에서 채택함)*
- `i2p.router.net.error` - IPv4 네트워크 오류 코드를 반환합니다. *(i2pd에서 채택함)*
- `i2p.router.net.error.v6` - IPv6 네트워크 오류 코드를 반환합니다. *(i2pd에서 채택함)*
- `i2p.router.net.testing` - IPv4 네트워크가 테스트 상태인지 여부를 반환합니다(0 또는 1). *(i2pd에서 채택함)*
- `i2p.router.net.testing.v6` - IPv6 네트워크가 테스트 상태인지 여부를 반환합니다(0 또는 1). *(i2pd에서 채택함)*

- `i2p.router.net.tunnels.successrate` - 최근 터널 생성 성공률(%)을 반환합니다. *(i2pd에서 채택됨)*
- `i2p.router.net.tunnels.totalsuccessrate` - 시작 이후 총 터널 생성 성공률(%)을 반환합니다. *(i2pd에서 채택됨)*
- `i2p.router.net.tunnels.queue` - 터널 생성 요청 큐 크기를 반환합니다. *(i2pd에서 채택됨)*
- `i2p.router.net.tunnels.tbmqueue` - 터널 생성 메시지(Tunnel Build Message) 큐 크기를 반환합니다. *(i2pd에서 채택됨)*

- `i2p.router.netdb.peers` - 알려진 피어 해시 목록을 반환합니다.
- `i2p.router.netdb.activepeers.info` - 활성 피어의 직렬화된 RouterInfo 데이터를 반환합니다.
- `i2p.router.netdb.ntcp.limit` - NTCP 연결 제한 수를 반환합니다.
- `i2p.router.netdb.ssu.limit` - SSU 연결 제한 수를 반환합니다.
- `i2p.router.netdb.bannedpeers` - 차단된 피어와 차단 세부 정보를 반환합니다.
- `i2p.router.netdb.activepeers.list` - 활성 피어 해시를 반환합니다.
- `i2p.router.netdb.peers.list` - 알려진 피어 해시를 반환합니다.
- `i2p.router.netdb.peers.info` - 알려진 피어의 직렬화된 RouterInfo 데이터를 반환합니다.
- `i2p.router.netdb.activepeers.stats` - 활성 피어 통계를 반환합니다.

- `i2p.router.addressbook.private.list` - 개인 주소록 항목을 반환합니다.
- `i2p.router.addressbook.local.list` - 로컬 주소록 항목을 반환합니다.
- `i2p.router.addressbook.router.list` - 라우터 주소록 항목을 반환합니다.
- `i2p.router.addressbook.published.list` - 공개된 주소록 항목을 반환합니다.
- `i2p.router.addressbook.subscriptions` - 구독 파일 경로와 항목을 반환합니다.
- `i2p.router.addressbook.config` - 주소록 설정 파일 경로와 항목을 반환합니다.

예시:

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
반환:

```json
{
    "jsonrpc": "2.0",
    "result": "{ data }",
    "id": 1
}
```
방법 - 주소록 --------------------

`AddressBook` 메서드의 경우 주소록에 항목을 추가하거나 삭제하기 위해 세 가지 매개변수/인수가 필요합니다:

- `Type` - 주소록 유형에 해당:
  - `private`
  - `local`
  - `router`
  - `published`
- `Hostname` - 주소록 항목과 연결된 호스트명 또는 도메인명에 해당.
- `Destination` - 주소록 항목과 연결된 대상에 해당.
- `Delete` - 이 매개변수는 선택 사항이며, 주소록 항목을 삭제할 때 사용됨. 이 매개변수가 제공되지 않으면 해당 메서드는 주소록에 새 항목을 추가함.

예시:

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
반환:

```json
{
  "jsonrpc": "2.0",
  "success": true or false,        
  "message": "Deleted/Added (hostname) in (address book type) address book" OR "Failed to delete/add (hostname) to (address book type) address book",
  "id": 1
}
```
주소록 구독 편집 시:

- `SetSubscriptions` - 이 매개변수는 주소록 항목의 구독을 설정하는 데 사용됩니다. 문자열 목록을 인수로 받습니다.

예시:

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
반환:

```json
{
  "jsonrpc": "2.0",
  "success": true,
  "message": "Successfully modified: /path/to/subscriptions.txt"
}
```
AddressBookConfig 편집을 위해:

- `SetConfig` - 이 매개변수는 주소록 항목의 설정을 지정하는 데 사용됩니다.

구성 설정을 포함하는 JSON 객체를 인수로 받는다.

사용 가능한/일반적인 구성 매개변수:

- `subscriptions` - 구독 URL 목록을 포함하는 파일.
- `update_delay` - 시간 단위의 업데이트 간격.
- `published_addressbook` - 공개 주소록의 경로.
- `router_addressbook` - 라우터 주소록의 경로.
- `local_addressbook` - 로컬 주소록의 경로.
- `private_addressbook` - 개인 주소록의 경로.
- `proxy_port` - eepProxy 포트.
- `proxy_host` - eepProxy 호스트명.
- `should_publish` - 공개 주소록을 업데이트할지 여부.
- `etags` - 구독 URL의 ETag를 포함하는 파일.
- `last_modified` - 구독 URL의 마지막 수정 타임스탬프를 포함하는 파일.
- `log` - 로그 파일 경로.
- `theme` - 테마.

예시:

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
반환:

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
방법 - TunnelManager --------

`TunnelManager` 메서드는 I2PTunnel 컨트롤러를 생성, 편집, 조회, 시작, 중지, 재시작 및 삭제하는 데 사용됩니다.

필수 매개변수:

- `Name` - 터널의 이름. 이는 터널의 식별자입니다.
- `Action` - 수행할 동작:
  - `create`
  - `edit`
  - `get`
  - `start`
  - `stop`
  - `restart`
  - `delete`

선택적 매개변수:

- `All` - 불리언 값으로, 모든 튜널에 대해 해당 동작을 적용할지 여부를 나타냅니다. 이는 `start`, `stop`, `restart` 동작에만 유효합니다.

`create`에 지원되는 터널 유형:

- `client`
- `httpclient`
- `ircclient`
- `socks`
- `socksirc`
- `connectclient`
- `streamrclient`

- `server`
- `httpserver`
- `httpbidirserver`
- `ircserver`
- `streamrserver`

터널 생성/편집을 위한 일반 매개변수:

- `Type` - 터널 유형. `create` 시 필수.
- `NewName` - 편집 시 선택적으로 지정할 수 있는 새 이름.
- `Port` - 로컬 수신 포트.
- `TargetHost` 또는 `Host` - 서버 터널의 대상 호스트.
- `TargetPort` - 서버 터널의 대상 포트.
- `TargetDestination` 또는 `Destination` - 목적지를 요구하는 클라이언트 터널의 목적지.
- `StartOnLoad` - 부울 값. 터널이 로드될 때 시작되어야 하는지 여부.
- `Description` - 터널 설명.
- `ReachableBy` - 터널이 수신 대기하는 인터페이스/주소.
- `Shared` - 부울 값. 클라이언트 터널을 공유할지 여부.
- `UseSSL` - 부울 값. 지원되는 경우 SSL 활성화.
- `TunnelLength` - 터널 길이, `0`부터 `3`까지.
- `TunnelVariance` - 터널 변동 값, `-2`부터 `2`까지.
- `TunnelQuantity` - 터널 수, `1`부터 `6`까지.
- `TunnelBackupQuantity` - 백업 터널 수, `0`부터 `3`까지.
- `SigType` - 서명 키 유형.
- `EncType` - 암호화 유형.
- `CustomOptions` - 사용자 정의 터널 옵션.

클라이언트 프록시 옵션:

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

클라이언트 관리 옵션:

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

HTTP 클라이언트 필터링 옵션:

- `AllowUserAgent`
- `AllowReferer`
- `AllowAccept`
- `AllowInternalSSL`

서버 옵션:

- `WebsiteHostname` 또는 `SpoofedHost`
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

LeaseSet 옵션:

- `EncryptLeaseSet` - 다음 중 하나:
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

예제 생성:

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
반환:

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
편집 예시:

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
반환:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - edited tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
예제 가져오기:

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
반환:

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
시작, 중지, 재시작, 삭제 예제들은 동일한 구조를 따르며, 단지 `Action` 매개변수가 다를 뿐입니다:

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
반환:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - starting tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
방법 - ClientServicesInfo *(i2pd에서 채택됨)* -------------------------------------------------

`ClientServicesInfo` 메서드는 라우터에서 실행 중인 클라이언트 서비스에 대한 상태 정보를 반환합니다. 각 서비스의 상태를 요청하려면 원하는 서비스 키를 `params`에 (임의의 값과 함께) 포함하세요.

지원되는 매개변수:

- `I2PTunnel` - 구성된 터널 이름을 해당 주소에 매핑하여 `client`와 `server` 하위 객체로 나누어 반환합니다.
- `HTTPProxy` - HTTP 프록시의 활성화 상태 및 주소를 반환합니다.
- `SOCKS` - SOCKS 프록시의 활성화 상태 및 주소를 반환합니다.
- `SAM` - SAM 브리지의 활성화 상태 및 활성 세션 정보를 반환합니다.
- `BOB` - BOB 브리지의 활성화 상태를 반환합니다. (Java I2P에서 더 이상 사용되지 않음; 항상 `false`를 반환합니다.)
- `I2CP` - I2CP 서버의 활성화 상태를 반환합니다.

예시:

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
반환:

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
호환성 =============

기존 i2pcontrol API와의 호환성은 유지되어야 하며, 새로운 메서드와 매개변수는 기존 기능에 간섭하지 않는 방식으로 추가되어야 합니다. 이 제안을 사용하는 새로운 애플리케이션은 추가된 정보와 기능을 활용할 수 있는 반면, 기존의 i2pcontrol API를 사용하는 애플리케이션은 수정 없이 계속 정상 작동해야 합니다.

구현 ==============

Java I2P --------

이 제안은 아직 Java I2P에 구현되어 있지 않지만, 코드는 [i2p.plugins.i2pcontrol](https://github.com/i2p/i2p.plugins.i2pcontrol) 저장소의 풀 리퀘스트 [#6](https://github.com/i2p/i2p.plugins.i2pcontrol/pull/6)에서 확인할 수 있습니다. 기존 코드에 영향을 주지 않으면서도 새로운 메서드의 테스트와 개발을 가능하게 하기 위해 이렇게 진행되었습니다. 코드가 실용화 준비가 완료되는 대로, i2pcontrol 디렉터리 아래의 주요 I2P 저장소에 통합될 예정입니다.

i2pd ----

"(i2pd에서 채택됨)"으로 표시된 메서드와 매개변수는 i2pd에서 구현되어 있으며 본 제안에서 변경되지 않습니다. i2pd의 확장 기능은 본 제안의 일환으로 수정이 필요하지 않습니다. 별도의 표시가 없는 본 제안의 부분들은 i2pd에서 구현되지 않았습니다.

go-i2p ------

go-i2p는 라우터 콘솔 애플리케이션을 가능하게 하고 향상시키기 위해 이 제안을 추진하고자 한다. 향후 이 제안을 채택하고 구현할 예정이다.

emissary --------

에미서리(Emissary)에서의 채택 가능성은 현재로서는 불확실하지만, 에미서리는 go-i2p와 동일한 방식으로 이 제안으로부터 혜택을 받을 가능성이 높다.

성능 ===========

성능에 영향을 미칠 것으로 예상되지 않습니다.
