---
title: "Расширение I2PControl"
number: "170"
author: "Nick2k4"
created: "2026-05-20"
lastupdated: "2026-05-20"
status: "Открыть"
toc: true
---

## Обзор

Данное предложение добавляет новую информацию в API i2pcontrol, обеспечивая большую гибкость. Эта информация включает: добавление, удаление, получение и изменение записей в адресных книгах и скрытых сервисах. Также в рамках данного предложения предоставляется дополнительная информация о вашем маршрутизаторе, например, о пирах, новостях, netDb и другое.

## Мотивация

Область применения данного предложения — создание унифицированной и упрощённой консоли маршрутизатора, которую можно использовать во всех реализациях маршрутизаторов со стандартным набором туннелей i2p. По сути, это предложение позволяет обеспечить более интуитивно понятный и удобный пользовательский интерфейс для пользователей по всей сети I2P.

Это предложение также обеспечит большую гибкость в API I2P для реализации и управления административным интерфейсом I2P в приложениях. Предоставление такой информации через i2pcontrol позволяет пользователям создавать более сложные приложения и улучшает поддержку удалённого управления.

## Дизайн

Когда пользователи взаимодействуют с API i2pcontrol, они смогут получать доступ к новым конечным точкам, предоставляющим информацию, упомянутую выше. Например, API i2pcontrol предоставит новые методы `TunnelManager` и `AddressBook`, которые позволят пользователям вводить параметры для создания, удаления, получения и изменения туннелей и адресных книг. Кроме того, у уже существующего метода `RouterInfo` появятся новые параметры для предоставления информации о маршрутизаторе.

## Последствия для безопасности

У данного предложения не ожидается дополнительных последствий для безопасности, поскольку информация, которая становится доступной, уже может быть получена другими способами. Однако важно обеспечить наличие надлежащих механизмов аутентификации и авторизации для доступа к API i2pcontrol, с целью предотвращения несанкционированного доступа к конфиденциальной информации или управления маршрутизатором.

## Спецификация API и методы

Все запросы следуют структуре JSON-RPC 2.0:

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
### Метод - RouterInfo (GETTERS)

Ниже приведены новые параметры для метода `RouterInfo` и возвращаемые ими значения:

- `i2p.router.news` - возвращает все записи новостей маршрутизатора. Тип возвращаемого значения — `String`
- `i2p.router.id` - возвращает хэш маршрутизатора в виде строки Base64 или `null`. Тип возвращаемого значения — `String`
- `i2p.router.clockskew` - возвращает среднее отклонение часов пира или `null`. Тип возвращаемого значения — `long`
- `i2p.router.info` - возвращает сериализованный RouterInfo в виде строки Base64 или `null`. Тип возвращаемого значения — `String`
- `i2p.router.logs` - возвращает последние сообщения журнала маршрутизатора. Тип возвращаемого значения — `List<String>`
- `i2p.router.logs.clear` - очищает буфер журнала маршрутизатора и возвращает `"success"`. Тип возвращаемого значения — `String`

- `i2p.router.net.total.received.bytes` — возвращает общее количество принятых байтов с момента запуска. *(взято из i2pd)* Тип возвращаемого значения — `long`
- `i2p.router.net.total.sent.bytes` — возвращает общее количество отправленных байтов с момента запуска. *(взято из i2pd)* Тип возвращаемого значения — `long`
- `i2p.router.net.total.transit.bytes` — возвращает общее количество транзитных байтов, пересланных с момента запуска. *(взято из i2pd)* Тип возвращаемого значения — `long`
- `i2p.router.net.bw.transit.15s` — возвращает среднюю пропускную способность транзита за 15 секунд (байт/сек). *(взято из i2pd)* Тип возвращаемого значения — `long`

- `i2p.router.net.tunnels.shareratio` - возвращает коэффициент обмена туннеля. Тип возвращаемого значения — `double`
- `i2p.router.net.tunnels.participating.info` - возвращает информацию об участвующих туннелях. Тип возвращаемого значения — `List<Map<String, Object>>`
- `i2p.router.net.tunnels.i2ptunnel` - возвращает информацию о настроенных контроллерах I2PTunnel (краткая статистика по всем). Тип возвращаемого значения — `List<Map<String, Object>>`
- `i2p.router.net.tunnels.exploratory.inbound` - возвращает количество исследовательских входящих туннелей. Тип возвращаемого значения — `int`
- `i2p.router.net.tunnels.exploratory.outbound` - возвращает количество исследовательских исходящих туннелей. Тип возвращаемого значения — `int`
- `i2p.router.net.tunnels.exploratory.info.list` - возвращает список информации об исследовательских туннелях. Тип возвращаемого значения — `List<Map<String, Object>>`
- `i2p.router.net.tunnels.client.inbound` - возвращает количество клиентских входящих туннелей. Тип возвращаемого значения — `int`
- `i2p.router.net.tunnels.client.outbound` - возвращает количество клиентских исходящих туннелей. Тип возвращаемого значения — `int`
- `i2p.router.net.tunnels.client.info.list` - возвращает список информации о клиентских туннелях. Тип возвращаемого значения — `List<Map<String, Object>>`

- `i2p.router.net.status.v6` - возвращает код состояния сети IPv6. *(заимствовано из i2pd)* Тип возвращаемого значения — `int`
- `i2p.router.net.error` - возвращает код ошибки сети IPv4. *(заимствовано из i2pd)* Тип возвращаемого значения — `int`
- `i2p.router.net.error.v6` - возвращает код ошибки сети IPv6. *(заимствовано из i2pd)* Тип возвращаемого значения — `int`
- `i2p.router.net.testing` - возвращает, находится ли сеть IPv4 в состоянии тестирования (0 или 1). *(заимствовано из i2pd)* Тип возвращаемого значения — `int`
- `i2p.router.net.testing.v6` - возвращает, находится ли сеть IPv6 в состоянии тестирования (0 или 1). *(заимствовано из i2pd)* Тип возвращаемого значения — `int`

- `i2p.router.net.tunnels.successrate` - возвращает недавний процент успешного создания туннелей (%). *(заимствовано из i2pd)* Тип возвращаемого значения — `double`
- `i2p.router.net.tunnels.totalsuccessrate` - возвращает общий процент успешного создания туннелей с момента запуска (%). *(заимствовано из i2pd)* Тип возвращаемого значения — `double`
- `i2p.router.net.tunnels.queue` - возвращает размер очереди запросов на создание туннелей. *(заимствовано из i2pd)* Тип возвращаемого значения — `int`
- `i2p.router.net.tunnels.tbmqueue` - возвращает размер очереди сообщений создания туннелей (Tunnel Build Message). *(заимствовано из i2pd)* Тип возвращаемого значения — `int`

- `i2p.router.netdb.peers` - возвращает список известных хэшей пиров. Тип возвращаемого значения — `List<String>`
- `i2p.router.netdb.activepeers.info` - возвращает сериализованные данные RouterInfo для активных пиров. Тип возвращаемого значения — `List<String>`
- `i2p.router.netdb.ntcp.limit` - возвращает лимит подключений NTCP. Тип возвращаемого значения — `int`
- `i2p.router.netdb.ssu.limit` - возвращает лимит подключений SSU. Тип возвращаемого значения — `int`
- `i2p.router.netdb.bannedpeers` - возвращает список забаненных пиров с деталями бана. Тип возвращаемого значения — `Map<String, Map<String, Object>>`
- `i2p.router.netdb.activepeers.list` - возвращает хэши активных пиров. Тип возвращаемого значения — `List<String>`
- `i2p.router.netdb.peers.list` - возвращает хэши известных пиров. Тип возвращаемого значения — `List<String>`
- `i2p.router.netdb.peers.info` - возвращает сериализованные данные RouterInfo для известных пиров. Тип возвращаемого значения — `List<String>`
- `i2p.router.netdb.activepeers.stats` - возвращает статистику по активным пирам. Тип возвращаемого значения — `List<Map<String, Object>>`

- `i2p.router.addressbook.private.list` - возвращает записи из приватной адресной книги. Тип возвращаемого значения — `List<Map<String, String>>`
- `i2p.router.addressbook.local.list` - возвращает записи из локальной адресной книги. Тип возвращаемого значения — `List<Map<String, String>>`
- `i2p.router.addressbook.router.list` - возвращает записи из адресной книги роутера. Тип возвращаемого значения — `List<Map<String, String>>`
- `i2p.router.addressbook.published.list` - возвращает опубликованные записи адресной книги. Тип возвращаемого значения — `List<Map<String, String>>`
- `i2p.router.addressbook.subscriptions` - возвращает путь к файлу подписок и его записи. Тип возвращаемого значения — `Map<String, Object>`
- `i2p.router.addressbook.config` - возвращает путь к конфигурационному файлу адресной книги и его записи. Тип возвращаемого значения — `Map<String, Object>`

Пример:

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
Возврат:

```json
{
    "jsonrpc": "2.0",
    "result": "{ data }",
    "id": 1
}
```
### Метод - Адресная книга (SETTERS)

Для метода `AddressBook` требуется три параметра/аргумента для удаления и добавления записей в адресную книгу:

- `Type` — соответствует типу адресной книги:
  - `private`
  - `local`
  - `router`
  - `published`
- `Hostname` — соответствует имени хоста или доменному имени, связанному с записью в адресной книге.
- `Destination` — соответствует назначению, связанному с записью в адресной книге.
- `Delete` — этот параметр является необязательным и используется для удаления записи из адресной книги. Если параметр не указан, метод добавит новую запись в адресную книгу.

Пример:

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
Возврат:

```json
{
  "jsonrpc": "2.0",
  "success": true or false,        
  "message": "Deleted/Added (hostname) in (address book type) address book" OR "Failed to delete/add (hostname) to (address book type) address book",
  "id": 1
}
```
Для редактирования AddressBookSubscriptions:

- `SetSubscriptions` - этот параметр используется для установки подписок для записи в адресной книге. В качестве аргумента он принимает список строк.

Пример:

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
Возврат:

```json
{
  "jsonrpc": "2.0",
  "success": true,
  "message": "Successfully modified: /path/to/subscriptions.txt"
}
```
Для редактирования AddressBookConfig:

- `SetConfig` — этот параметр используется для установки конфигурации записи в адресной книге.

Принимает в качестве аргумента объект JSON, содержащий параметры конфигурации.

Доступные/распространённые параметры конфигурации:

- `subscriptions` — файл, содержащий список URL-адресов подписок.
- `update_delay` — интервал обновления в часах.
- `published_addressbook` — путь к опубликованной адресной книге.
- `router_addressbook` — путь к адресной книге маршрутизатора.
- `local_addressbook` — путь к локальной адресной книге.
- `private_addressbook` — путь к приватной адресной книге.
- `proxy_port` — порт eepProxy.
- `proxy_host` — имя хоста eepProxy.
- `should_publish` — следует ли обновлять опубликованную адресную книгу.
- `etags` — файл, содержащий etag-идентификаторы URL-адресов подписок.
- `last_modified` — файл, содержащий временные метки последнего изменения URL-адресов подписок.
- `log` — путь к файлу журнала.
- `theme` — тема оформления.

Пример:

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
Возврат:

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
### Метод - TunnelManager (1 МЕТОД ДЛЯ ПОЛУЧЕНИЯ ОТМЕЧЕННЫХ, ОСТАЛЬНЫЕ ДЛЯ УСТАНОВКИ)

Метод `TunnelManager` используется для создания, редактирования, получения, запуска, остановки, перезапуска и удаления контроллеров I2PTunnel.

Обязательные параметры:

- `Name` - имя туннеля. Это идентификатор туннеля.
- `Action` - действие, которое необходимо выполнить:
  - `create`.
  - `edit`
  - `get`
  - `start`
  - `stop`
  - `restart`
  - `delete`

Дополнительные параметры:

- `All` - булево значение, указывает, нужно ли применить действие ко всем туннелям. Допустимо только для действий `start`, `stop` и `restart`.

Поддерживаемые типы туннелей для `create`:

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

Общие параметры для создания/редактирования туннелей:

- `Type` - тип туннеля. Обязателен для `create`.
- `NewName` - необязательное новое имя при редактировании.
- `Port` - локальный порт прослушивания.
- `TargetHost` или `Host` - целевой хост для серверных туннелей.
- `TargetPort` - целевой порт для серверных туннелей.
- `TargetDestination` или `Destination` - назначение для клиентских туннелей, которым оно требуется.
- `StartOnLoad` - булево значение, должен ли туннель запускаться при загрузке.
- `Description` - описание туннеля.
- `ReachableBy` - интерфейс/адрес, на котором прослушивает туннель.
- `Shared` - булево значение, должен ли быть клиентский туннель общим.
- `UseSSL` - булево значение, включить SSL, где поддерживается.
- `TunnelLength` - длина туннеля, от `0` до `3`.
- `TunnelVariance` - вариативность туннеля, от `-2` до `2`.
- `TunnelQuantity` - количество туннелей, от `1` до `6`.
- `TunnelBackupQuantity` - количество резервных туннелей, от `0` до `3`.
- `SigType` - тип ключа подписи.
- `EncType` - тип шифрования.
- `CustomOptions` - пользовательские параметры туннеля.

Параметры клиентского прокси:

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

Параметры управления клиентом:

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

Параметры фильтрации HTTP-клиента:

- `AllowUserAgent`
- `AllowReferer`
- `AllowAccept`
- `AllowInternalSSL`

Параметры сервера:

- `WebsiteHostname` или `SpoofedHost`
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

Параметры LeaseSet:

- `EncryptLeaseSet` - один из:
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

Пример создания:

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
Возврат:

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
Пример редактирования:

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
Возврат:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - edited tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
Получить пример (ТОЛЬКО ГЕТТЕР) Возвращает - `Map<String, Object>` (информация) и `String` (статус):

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
Возврат:

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
Примеры запуска, остановки, перезапуска и удаления. Они имеют одинаковую структуру, просто с разными параметрами `Action`:

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
Возврат:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - starting tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
### Method - ClientServicesInfo *(адаптировано из i2pd)*

Метод `ClientServicesInfo` возвращает информацию о состоянии клиентских служб, работающих на маршрутизаторе. Включите нужные ключи служб (с любыми значениями) в параметр `params`, чтобы запросить состояние каждой службы.

Поддерживаемые параметры:

- `I2PTunnel` - возвращает отображение настроенных имён туннелей на их адреса, разделённое на подобъекты `client` и `server`.
- `HTTPProxy` - возвращает состояние включённости HTTP-прокси и его адрес.
- `SOCKS` - возвращает состояние включённости SOCKS-прокси и его адрес.
- `SAM` - возвращает состояние включённости моста SAM и информацию об активных сессиях.
- `BOB` - возвращает состояние включённости моста BOB. (Устарело в Java I2P; всегда возвращает `false`.)
- `I2CP` - возвращает состояние включённости сервера I2CP.

Пример:

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
Возврат:

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
## Совместимость

Совместимость с существующим API i2pcontrol должна быть сохранена, поскольку новые методы и параметры добавляются таким образом, что не мешают существующей функциональности. Приложения, уже использующие API i2pcontrol, должны продолжать работать без изменений, в то время как новые приложения смогут воспользоваться дополнительной информацией и возможностями, предусмотренными в данном предложении.

## Реализация

### Java I2P

Это предложение еще не реализовано в Java I2P, однако код доступен в репозитории [i2p.plugins.i2pcontrol](https://github.com/i2p/i2p.plugins.i2pcontrol) в рамках запроса на слияние [#6](https://github.com/i2p/i2p.plugins.i2pcontrol/pull/6). Это сделано для того, чтобы разрешить тестирование и разработку новых методов без влияния на существующий код. После готовности кода к использованию в продакшене он будет включен в основной репозиторий I2P в каталог i2pcontrol.

### i2pd

Методы и параметры, помеченные как «(заимствовано из i2pd)», реализованы в i2pd и не изменяются в данном предложении. Расширения i2pd не потребуют модификации в рамках данного предложения. Части, не отмеченные таким образом, в i2pd не реализованы.

### Go-I2P

go-i2p стремится реализовать это предложение, чтобы включить и улучшить своё приложение консоли маршрутизатора. В будущем оно примет и реализует данное предложение.

### emissary

Вероятность внедрения в Emissary на данный момент неизвестна, однако Emissary, вероятно, получит выгоду от данного предложения теми же способами, что и go-i2p.

## Производительность

Ожидается отсутствие влияния на производительность.
