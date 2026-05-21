---
title: "i2pcontrol-expansion"
number: "170"
author: "Nick2k4"
created: "2026-05-20"
lastupdated: "2026-05-20"
status: "Otevřít"
toc: true
---

Přehled ========

Tento návrh zpřístupňuje nové informace přes API i2pcontrol, čímž umožňuje větší flexibilitu. Tyto informace zahrnují: přidávání, mazání, načítání a úpravu addressbooků (adresářů) a skrytých služeb. Návrh také zpřístupňuje další informace o vašem routeru, jako jsou peerové, novinky, netDb a další.

Motivace ==========

Důvodem tohoto návrhu je umožnit větší flexibilitu v I2P API pro aplikace, které implementují a spravují správcovské rozhraní I2P. Zpřístupnění takových informací prostřednictvím i2pcontrol umožňuje uživatelům vytvářet pokročilejší aplikace a poskytovat lepší podporu pro vzdálenou správu.

Návrh ======

Když uživatelé budou komunikovat s rozhraním i2pcontrol API, budou mít přístup k novým koncovým bodům, které poskytují výše zmíněné informace. Například rozhraní i2pcontrol API zpřístupní nové metody `TunnelManager` a `AddressBook`, které uživatelům umožní zadávat parametry pro vytváření, mazání, načítání a úpravu tunelů a adresářů. Kromě toho bude mít předem existující metoda `RouterInfo` nové parametry pro zobrazení informací o směrovači.

Důsledky pro zabezpečení =====================

Tento návrh nepřináší žádné další očekávané bezpečnostní důsledky, protože informace, které jsou zpřístupněny, jsou již dostupné jinými prostředky. Je však důležité zajistit, aby byly pro přístup k rozhraní i2pcontrol API implementovány vhodné mechanismy ověřování a autorizace, aby se zabránilo neoprávněnému přístupu k citlivým informacím nebo ovládání směrovače.

Specifikace API a metody ===========================

Všechny požadavky následují strukturu JSON-RPC 2.0:

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
Metoda - RouterInfo -------------------

Níže jsou uvedeny nové parametry metody `RouterInfo` a to, co vrací:

- `i2p.router.news` - vrací všechny záznamy novinek směrovače.
- `i2p.router.id` - vrací otisk směrovače jako Base64 řetězec nebo `null`.
- `i2p.router.clockskew` - vrací průměrnou odchylku hodin protějšků, nebo `null`.
- `i2p.router.info` - vrací serializované RouterInfo jako Base64 řetězec, nebo `null`.
- `i2p.router.logs` - vrací poslední zprávy z protokolu směrovače.
- `i2p.router.logs.clear` - vymaže vyrovnávací paměť protokolu směrovače a vrací `"success"`.

- `i2p.router.net.total.received.bytes` - vrátí celkový počet přijatých bajtů od spuštění. *(převzato z i2pd)*
- `i2p.router.net.total.sent.bytes` - vrátí celkový počet odeslaných bajtů od spuštění. *(převzato z i2pd)*
- `i2p.router.net.total.transit.bytes` - vrátí celkový počet přeposlaných transit bajtů od spuštění. *(převzato z i2pd)*
- `i2p.router.net.bw.transit.15s` - vrátí průměrnou transit šířku pásma za 15 sekund (bajty/sek). *(převzato z i2pd)*

- `i2p.router.net.tunnels.shareratio` - vrátí poměr sdílení tunelů.
- `i2p.router.net.tunnels.participating.info` - vrátí informace o účastnících se tunelech.
- `i2p.router.net.tunnels.i2ptunnel` - vrátí informace o nakonfigurovaném ovladači I2PTunnel (rychlé statistiky všech).
- `i2p.router.net.tunnels.exploratory.inbound` - vrátí počet průzkumných příchozích tunelů.
- `i2p.router.net.tunnels.exploratory.outbound` - vrátí počet průzkumných odchozích tunelů.
- `i2p.router.net.tunnels.exploratory.info.list` - vrátí seznam informací o průzkumných tunelech.
- `i2p.router.net.tunnels.client.inbound` - vrátí počet příchozích klientových tunelů.
- `i2p.router.net.tunnels.client.outbound` - vrátí počet odchozích klientových tunelů.
- `i2p.router.net.tunnels.client.info.list` - vrátí seznam informací o klientových tunelech.

- `i2p.router.net.status.v6` - vrací kód stavu IPv6 sítě. *(převzato z i2pd)*
- `i2p.router.net.error` - vrací kód chyby IPv4 sítě. *(převzato z i2pd)*
- `i2p.router.net.error.v6` - vrací kód chyby IPv6 sítě. *(převzato z i2pd)*
- `i2p.router.net.testing` - vrací, zda je IPv4 síť ve stavu testování (0 nebo 1). *(převzato z i2pd)*
- `i2p.router.net.testing.v6` - vrací, zda je IPv6 síť ve stavu testování (0 nebo 1). *(převzato z i2pd)*

- `i2p.router.net.tunnels.successrate` - vrací aktuální úspěšnost vytváření tunelů (%). *(převzato z i2pd)*
- `i2p.router.net.tunnels.totalsuccessrate` - vrací celkovou úspěšnost vytváření tunelů od spuštění (%). *(převzato z i2pd)*
- `i2p.router.net.tunnels.queue` - vrací velikost fronty požadavků na vytvoření tunelů. *(převzato z i2pd)*
- `i2p.router.net.tunnels.tbmqueue` - vrací velikost fronty zpráv pro vytvoření tunelů (Tunnel Build Message). *(převzato z i2pd)*

- `i2p.router.netdb.peers` - vrací seznam známých hashů peerů.
- `i2p.router.netdb.activepeers.info` - vrací serializovaná data RouterInfo pro aktivní peery.
- `i2p.router.netdb.ntcp.limit` - vrací limit spojení NTCP.
- `i2p.router.netdb.ssu.limit` - vrací limit spojení SSU.
- `i2p.router.netdb.bannedpeers` - vrací seznam zablokovaných peerů s detaily blokování.
- `i2p.router.netdb.activepeers.list` - vrací seznam hashů aktivních peerů.
- `i2p.router.netdb.peers.list` - vrací seznam hashů známých peerů.
- `i2p.router.netdb.peers.info` - vrací serializovaná data RouterInfo pro známé peery.
- `i2p.router.netdb.activepeers.stats` - vrací statistiky aktivních peerů.

- `i2p.router.addressbook.private.list` – vrací položky soukromé adresářové knihy.
- `i2p.router.addressbook.local.list` – vrací položky místní adresářové knihy.
- `i2p.router.addressbook.router.list` – vrací položky adresářové knihy směrovače.
- `i2p.router.addressbook.published.list` – vrací publikované položky adresářové knihy.
- `i2p.router.addressbook.subscriptions` – vrací cestu k souboru odběrů a jeho položky.
- `i2p.router.addressbook.config` – vrací cestu ke konfiguračnímu souboru adresářové knihy a její položky.

Příklad:

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
Návrat:

```json
{
    "jsonrpc": "2.0",
    "result": "{ data }",
    "id": 1
}
```
Metoda - AddressBook --------------------

Pro metodu `AddressBook` jsou pro mazání a přidávání záznamů do adresáře vyžadovány tři parametry:

- `Type` - odpovídá typu adresáře:
  - `private`
  - `local`
  - `router`
  - `published`
- `Hostname` - odpovídá názvu hostitele nebo doménovému názvu spojenému se záznamem v adresáři.
- `Destination` - odpovídá cíli spojenému se záznamem v adresáři.
- `Delete` - tento parametr je volitelný a slouží k odstranění záznamu z adresáře. Pokud není tento parametr uveden, metoda přidá nový záznam do adresáře.

Příklad:

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
Návrat:

```json
{
  "jsonrpc": "2.0",
  "success": true or false,        
  "message": "Deleted/Added (hostname) in (address book type) address book" OR "Failed to delete/add (hostname) to (address book type) address book",
  "id": 1
}
```
Pro úpravu AddressBookSubscriptions:

- `SetSubscriptions` – tento parametr slouží k nastavení odběrů pro záznam v adresáři. Jako argument přijímá seznam řetězců.

Příklad:

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
Návrat:

```json
{
  "jsonrpc": "2.0",
  "success": true,
  "message": "Successfully modified: /path/to/subscriptions.txt"
}
```
Pro úpravu AddressBookConfig:

- `SetConfig` - tento parametr se používá k nastavení konfigurace záznamu v adresáři.

Jako argument přijímá objekt JSON, který obsahuje nastavení konfigurace.

Dostupné/běžné konfigurační parametry:

- `subscriptions` – soubor obsahující seznam URL odběrů.
- `update_delay` – interval aktualizace v hodinách.
- `published_addressbook` – cesta k publikované adresářové knize.
- `router_addressbook` – cesta k adresářové knize směrovače.
- `local_addressbook` – cesta k místní adresářové knize.
- `private_addressbook` – cesta k soukromé adresářové knize.
- `proxy_port` – port eepProxy.
- `proxy_host` – název hostitele eepProxy.
- `should_publish` – určuje, zda se má aktualizovat publikovaná adresářová kniha.
- `etags` – soubor obsahující etagy URL odběrů.
- `last_modified` – soubor obsahující časová razítka poslední změny URL odběrů.
- `log` – cesta k souboru protokolu.
- `theme` – motiv vzhledu.

Příklad:

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
Návrat:

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
Metoda - Správce tunelů --------

Metoda `TunnelManager` se používá k vytváření, úpravě, získávání, spouštění, zastavování, restartování a mazání kontrolérů I2PTunnel.

Požadované parametry:

- `Name` – název tunelu. Jedná se o identifikátor tunelu.
- `Action` – akce, která se má provést:
  - `create`
  - `edit`
  - `get`
  - `start`
  - `stop`
  - `restart`
  - `delete`

Volitelné parametry:

- `All` - boolean, zda použít akci na všechny tunely. Platí pouze pro akce `start`, `stop` a `restart`.

Podporované typy tunelů pro `create`:

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

Běžné parametry pro vytváření/upravování tunelů:

- `Type` - typ tunelu. Vyžadováno pro `create`.
- `NewName` - volitelný nový název při úpravě.
- `Port` - místní naslouchající port.
- `TargetHost` nebo `Host` - cílový hostitel pro serverové tunely.
- `TargetPort` - cílový port pro serverové tunely.
- `TargetDestination` nebo `Destination` - cíl pro klientské tunely, které jej vyžadují.
- `StartOnLoad` - logická hodnota, zda by měl být tunel spuštěn po načtení.
- `Description` - popis tunelu.
- `ReachableBy` - rozhraní/adresa, na které tunel naslouchá.
- `Shared` - logická hodnota, zda by měl být klientský tunel sdílen.
- `UseSSL` - logická hodnota, zapne SSL tam, kde je podporováno.
- `TunnelLength` - délka tunelu, `0` až `3`.
- `TunnelVariance` - variabilita tunelu, `-2` až `2`.
- `TunnelQuantity` - počet tunelů, `1` až `6`.
- `TunnelBackupQuantity` - počet záložních tunelů, `0` až `3`.
- `SigType` - typ podpisového klíče.
- `EncType` - typ šifrování.
- `CustomOptions` - vlastní nastavení tunelu.

Možnosti klientské proxy:

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

Možnosti správy klienta:

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

Možnosti filtrování HTTP klienta:

- `AllowUserAgent`
- `AllowReferer`
- `AllowAccept`
- `AllowInternalSSL`

Možnosti serveru:

- `WebsiteHostname` nebo `SpoofedHost`
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

Možnosti LeaseSet:

- `EncryptLeaseSet` - jedna z možností:
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

Vytvořit příklad:

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
Návrat:

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
Upravit příklad:

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
Návrat:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - edited tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
Získat příklad:

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
Návrat:

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
Příklad pro spuštění, zastavení, restartování a odstranění. Mají stejnou strukturu, liší se pouze parametry `Action`:

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
Návrat:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - starting tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
Metoda - ClientServicesInfo *(převzato z i2pd)* -------------------------------------------------

Metoda `ClientServicesInfo` vrací informace o stavu klientských služeb běžících na routeru. Zahrňte požadované klíče služeb (s libovolnou hodnotou) do `params`, abyste vyžádali stav jednotlivých služeb.

Podporované parametry:

- `I2PTunnel` – vrací mapu nakonfigurovaných názvů tunelů na jejich adresy, rozdělenou do podobjektů `client` a `server`.
- `HTTPProxy` – vrací stav povolení HTTP proxy a její adresu.
- `SOCKS` – vrací stav povolení SOCKS proxy a její adresu.
- `SAM` – vrací stav povolení SAM mostu a informace o aktivních sezeních.
- `BOB` – vrací stav povolení BOB mostu. (Zastaralé v Java I2P; vždy vrací `false`.)
- `I2CP` – vrací stav povolení I2CP serveru.

Příklad:

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
Návrat:

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
Kompatibilita =============

Kompatibilita se stávajícím i2pcontrol API by měla být zachována, protože nové metody a parametry jsou přidávány způsobem, který neovlivňuje stávající funkčnost. Stávající aplikace využívající i2pcontrol API by měly nadále fungovat bez úprav, zatímco nové aplikace si mohou využít dodatečné informace a možnosti poskytované tímto návrhem.

Implementace ==============

Java I2P --------

Tento návrh zatím není implementován v Java I2P, avšak kód je dostupný v repozitáři [i2p.plugins.i2pcontrol](https://github.com/i2p/i2p.plugins.i2pcontrol) pod žádostí o sloučení [#6](https://github.com/i2p/i2p.plugins.i2pcontrol/pull/6). Toto bylo provedeno, aby bylo možné testovat a vyvíjet nové metody, aniž by to ovlivnilo stávající kód. Po připravenosti kódu pro produkční použití bude sloučen do hlavního repozitáře I2P do adresáře i2pcontrol.

i2pd ----

Metody a parametry označené jako „(převzato z i2pd)“ jsou implementovány v i2pd a v tomto návrhu nejsou změněny. Rozšíření i2pd nebudou v rámci tohoto návrhu vyžadovat úpravy. Části tohoto návrhu, které nejsou označeny, nejsou v i2pd implementovány.

go-i2p ------

go-i2p má motivaci prosazovat tuto návrh, aby umožnilo a vylepšilo svou aplikaci řídicí konzole. V budoucnu návrh přijme a implementuje.

emissary --------

Pravděpodobnost přijetí v Emissary je v současné době neznámá, avšak Emissary bude pravděpodobně profitovat z této navržené změny stejnými způsoby jako go-i2p.

Výkon ===========

Nelze očekávat žádný dopad na výkon.
