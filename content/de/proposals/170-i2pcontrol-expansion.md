---
title: "I2PControl-Erweiterung"
number: "170"
author: "Nick2k4"
created: "2026-05-20"
lastupdated: "2026-05-20"
status: "Öffnen"
toc: true
---

## Übersicht

Dieser Vorschlag macht neue Informationen über die i2pcontrol-API verfügbar und ermöglicht dadurch eine größere Flexibilität. Zu diesen Informationen gehören das Hinzufügen, Löschen, Abrufen und Ändern von Adressbüchern und versteckten Diensten. Der Vorschlag macht außerdem weitere Informationen über Ihren Router verfügbar, wie beispielsweise Peers, Nachrichten, netDb und mehr.

## Motivation

Der Anwendungsfall für diesen Vorschlag ist die Erstellung einer einheitlichen und vereinfachten Router-Konsole, die zwischen allen Router-Implementierungen mit der Standard-Suite an I2P-Tunneln gemeinsam genutzt werden kann. Im Wesentlichen ermöglicht dieser Vorschlag ein intuitiveres und benutzerfreundlicheres Erlebnis für Nutzer im gesamten I2P-Netzwerk.

Dieser Vorschlag wird außerdem eine größere Flexibilität in der I2P-API ermöglichen, sodass Anwendungen eine I2P-Verwaltungsschnittstelle implementieren und verwalten können. Die Bereitstellung solcher Informationen für i2pcontrol erlaubt es Benutzern, fortschrittlichere Anwendungen zu erstellen und eine bessere Unterstützung für die Fernverwaltung bereitzustellen.

## Design

Wenn Benutzer mit der i2pcontrol-API interagieren, können sie auf neue Endpunkte zugreifen, die die oben genannten Informationen bereitstellen. Beispielsweise wird die i2pcontrol-API neue Methoden `TunnelManager` und `AddressBook` bereitstellen, die es Benutzern ermöglichen, Parameter einzugeben, um Tunnel und Adressbücher zu erstellen, zu löschen, abzurufen und zu bearbeiten. Zusätzlich erhält die bereits vorhandene Methode `RouterInfo` neue Parameter, um Informationen über den Router offenzulegen.

## Sicherheitsimplikationen

Es gibt keine erwarteten zusätzlichen Sicherheitsimplikationen durch diesen Vorschlag, da die offengelegten Informationen bereits auf andere Weise zugänglich sind. Es ist jedoch wichtig sicherzustellen, dass ordnungsgemäße Authentifizierungs- und Autorisierungsmechanismen für den Zugriff auf die i2pcontrol-API vorhanden sind, um unbefugten Zugriff auf sensible Informationen oder die Kontrolle über den Router zu verhindern.

## API-Spezifikation und Methoden

Alle Anfragen folgen der JSON-RPC-2.0-Struktur:

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
### Methode - RouterInfo (GETTER)

Im Folgenden sind die neuen Parameter für die `RouterInfo`-Methode und deren Rückgabewerte aufgeführt:

- `i2p.router.news` - gibt alle News-Einträge des Routers zurück. Rückgabetyp - `String`
- `i2p.router.id` - gibt den Router-Hash als Base64-Zeichenfolge zurück oder `null`. Rückgabetyp - `String`
- `i2p.router.clockskew` - gibt die durchschnittliche Uhrabweichung zu Peers zurück oder `null`. Rückgabetyp - `long`
- `i2p.router.info` - gibt die serialisierte RouterInfo als Base64-Zeichenfolge zurück oder `null`. Rückgabetyp - `String`
- `i2p.router.logs` - gibt aktuelle Protokollnachrichten des Routers zurück. Rückgabetyp - `List<String>`
- `i2p.router.logs.clear` - löscht den Protokollpuffer des Routers und gibt `"success"` zurück. Rückgabetyp - `String`

- `i2p.router.net.total.received.bytes` - gibt die seit dem Start insgesamt empfangenen Bytes zurück. *(übernommen aus i2pd)* Rückgabetyp - `long`
- `i2p.router.net.total.sent.bytes` - gibt die seit dem Start insgesamt gesendeten Bytes zurück. *(übernommen aus i2pd)* Rückgabetyp - `long`
- `i2p.router.net.total.transit.bytes` - gibt die seit dem Start insgesamt weitergeleiteten Transit-Bytes zurück. *(übernommen aus i2pd)* Rückgabetyp - `long`
- `i2p.router.net.bw.transit.15s` - gibt die durchschnittliche Transit-Bandbreite über 15 Sekunden (Bytes/Sek) zurück. *(übernommen aus i2pd)* Rückgabetyp - `long`

- `i2p.router.net.tunnels.shareratio` - gibt das Tunnel-Share-Verhältnis zurück. Rückgabetyp - `double`
- `i2p.router.net.tunnels.participating.info` - gibt Informationen zu den aktiven Tunneln zurück. Rückgabetyp - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.i2ptunnel` - gibt die konfigurierten I2PTunnel-Controller-Informationen zurück (Schnellstatistiken aller). Rückgabetyp - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.exploratory.inbound` - gibt die Anzahl der eingehenden explorativen Tunnel zurück. Rückgabetyp - `int`
- `i2p.router.net.tunnels.exploratory.outbound` - gibt die Anzahl der ausgehenden explorativen Tunnel zurück. Rückgabetyp - `int`
- `i2p.router.net.tunnels.exploratory.info.list` - gibt die Liste der Informationen zu explorativen Tunneln zurück. Rückgabetyp - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.client.inbound` - gibt die Anzahl der eingehenden Client-Tunnel zurück. Rückgabetyp - `int`
- `i2p.router.net.tunnels.client.outbound` - gibt die Anzahl der ausgehenden Client-Tunnel zurück. Rückgabetyp - `int`
- `i2p.router.net.tunnels.client.info.list` - gibt die Liste der Client-Tunnel-Informationen zurück. Rückgabetyp - `List<Map<String, Object>>`

- `i2p.router.net.status.v6` - gibt den IPv6-Netzwerkstatuscode zurück. *(übernommen aus i2pd)* Rückgabetyp - `int`
- `i2p.router.net.error` - gibt den IPv4-Netzwerkfehlercode zurück. *(übernommen aus i2pd)* Rückgabetyp - `int`
- `i2p.router.net.error.v6` - gibt den IPv6-Netzwerkfehlercode zurück. *(übernommen aus i2pd)* Rückgabetyp - `int`
- `i2p.router.net.testing` - gibt zurück, ob sich das IPv4-Netzwerk im Testzustand befindet (0 oder 1). *(übernommen aus i2pd)* Rückgabetyp - `int`
- `i2p.router.net.testing.v6` - gibt zurück, ob sich das IPv6-Netzwerk im Testzustand befindet (0 oder 1). *(übernommen aus i2pd)* Rückgabetyp - `int`

- `i2p.router.net.tunnels.successrate` - gibt die aktuelle Erfolgsquote für den Aufbau von Tunneln (%) zurück. *(übernommen aus i2pd)* Rückgabetyp - `double`
- `i2p.router.net.tunnels.totalsuccessrate` - gibt die gesamte Erfolgsquote für den Aufbau von Tunneln seit dem Start (%) zurück. *(übernommen aus i2pd)* Rückgabetyp - `double`
- `i2p.router.net.tunnels.queue` - gibt die Größe der Warteschlange für Tunnelaufbauanfragen zurück. *(übernommen aus i2pd)* Rückgabetyp - `int`
- `i2p.router.net.tunnels.tbmqueue` - gibt die Größe der Tunnel-Build-Nachrichten-Warteschlange zurück. *(übernommen aus i2pd)* Rückgabetyp - `int`

- `i2p.router.netdb.peers` - gibt eine Liste bekannter Peer-Hashes zurück. Rückgabetyp - `List<String>`
- `i2p.router.netdb.activepeers.info` - gibt serialisierte RouterInfo-Daten für aktive Peers zurück. Rückgabetyp - `List<String>`
- `i2p.router.netdb.ntcp.limit` - gibt das NTCP-Verbindungslimit zurück. Rückgabetyp - `int`
- `i2p.router.netdb.ssu.limit` - gibt das SSU-Verbindungslimit zurück. Rückgabetyp - `int`
- `i2p.router.netdb.bannedpeers` - gibt gesperrte Peers mit Sperrdetails zurück. Rückgabetyp - `Map<String, Map<String, Object>>`
- `i2p.router.netdb.activepeers.list` - gibt Hashes aktiver Peers zurück. Rückgabetyp - `List<String>`
- `i2p.router.netdb.peers.list` - gibt Hashes bekannter Peers zurück. Rückgabetyp - `List<String>`
- `i2p.router.netdb.peers.info` - gibt serialisierte RouterInfo-Daten für bekannte Peers zurück. Rückgabetyp - `List<String>`
- `i2p.router.netdb.activepeers.stats` - gibt Statistiken aktiver Peers zurück. Rückgabetyp - `List<Map<String, Object>>`

- `i2p.router.addressbook.private.list` - gibt Einträge aus dem privaten Adressbuch zurück. Rückgabetyp - `List<Map<String, String>>`
- `i2p.router.addressbook.local.list` - gibt Einträge aus dem lokalen Adressbuch zurück. Rückgabetyp - `List<Map<String, String>>`
- `i2p.router.addressbook.router.list` - gibt Einträge aus dem Router-Adressbuch zurück. Rückgabetyp - `List<Map<String, String>>`
- `i2p.router.addressbook.published.list` - gibt veröffentlichte Adressbucheinträge zurück. Rückgabetyp - `List<Map<String, String>>`
- `i2p.router.addressbook.subscriptions` - gibt den Pfad zur Abonnementdatei und deren Einträge zurück. Rückgabetyp - `Map<String, Object>`
- `i2p.router.addressbook.config` - gibt den Pfad zur Adressbuch-Konfiguration und deren Einträge zurück. Rückgabetyp - `Map<String, Object>`

Beispiel:

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
Rückgabe:

```json
{
    "jsonrpc": "2.0",
    "result": "{ data }",
    "id": 1
}
```
### Methode - Adressbuch (SETTER)

Für die `AddressBook`-Methode sind drei Parameter/Argumente erforderlich, um Einträge in das Adressbuch hinzuzufügen oder daraus zu löschen:

- `Type` – entspricht dem Adressbuch-Typ:
  - `private`
  - `local`
  - `router`
  - `published`
- `Hostname` – entspricht dem Hostnamen oder Domainnamen, der mit dem Adressbucheintrag verknüpft ist.
- `Destination` – entspricht der Zieladresse, die mit dem Adressbucheintrag verknüpft ist.
- `Delete` – dieser Parameter ist optional und dient zum Löschen eines Adressbucheintrags. Wenn dieser Parameter nicht angegeben wird, fügt die Methode einen neuen Eintrag zum Adressbuch hinzu.

Beispiel:

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
Rückgabe:

```json
{
  "jsonrpc": "2.0",
  "success": true or false,        
  "message": "Deleted/Added (hostname) in (address book type) address book" OR "Failed to delete/add (hostname) to (address book type) address book",
  "id": 1
}
```
Zum Bearbeiten von AddressBookSubscriptions:

- `SetSubscriptions` – Dieser Parameter wird verwendet, um die Abonnements für einen Adressbucheintrag festzulegen. Er erwartet eine Liste von Zeichenketten als Argument.

Beispiel:

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
Rückgabe:

```json
{
  "jsonrpc": "2.0",
  "success": true,
  "message": "Successfully modified: /path/to/subscriptions.txt"
}
```
Zum Bearbeiten der AddressBookConfig:

- `SetConfig` - Dieser Parameter wird verwendet, um die Konfiguration für einen Adressbucheintrag festzulegen.

Es nimmt ein JSON-Objekt als Argument entgegen, das die Konfigurationseinstellungen enthält.

Verfügbare/häufige Konfigurationsparameter:

- `subscriptions` - Datei, die die Liste der Abonnement-URLs enthält.
- `update_delay` - Aktualisierungsintervall in Stunden.
- `published_addressbook` - Pfad zur veröffentlichten Adressbuchdatei.
- `router_addressbook` - Pfad zur Router-Adressbuchdatei.
- `local_addressbook` - Pfad zur lokalen Adressbuchdatei.
- `private_addressbook` - Pfad zur privaten Adressbuchdatei.
- `proxy_port` - eepProxy-Port.
- `proxy_host` - eepProxy-Hostname.
- `should_publish` - Gibt an, ob das veröffentlichte Adressbuch aktualisiert werden soll.
- `etags` - Datei, die die ETags der Abonnement-URLs enthält.
- `last_modified` - Datei, die die „Last-Modified“-Zeitstempel der Abonnement-URLs enthält.
- `log` - Pfad zur Protokolldatei.
- `theme` - Thema.

Beispiel:

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
Rückgabe:

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
### Methode - TunnelManager (1 MARKIERTER GETTER, RESTLICHE SETTER)

Die `TunnelManager`-Methode wird verwendet, um I2PTunnel-Controller zu erstellen, bearbeiten, abrufen, starten, stoppen, neu starten und zu löschen.

Erforderliche Parameter:

- `Name` - Name des Tunnels. Dies ist die Kennung des Tunnels.
- `Action` - durchzuführende Aktion:
  - `create`.
  - `edit`
  - `get`
  - `start`
  - `stop`
  - `restart`
  - `delete`

Optionale Parameter:

- `All` - boolean, ob die Aktion auf alle Tunnel angewendet werden soll. Dies ist nur für die Aktionen `start`, `stop` und `restart` gültig.

Unterstützte Tunneltypen für `create`:

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

Allgemeine Parameter zum Erstellen/Bearbeiten von Tunnels:

- `Type` - Tunnel-Typ. Erforderlich für `create`.
- `NewName` - optionaler neuer Name beim Bearbeiten.
- `Port` - lokaler Port, an dem gelauscht wird.
- `TargetHost` oder `Host` - Zielhost für Server-Tunnel.
- `TargetPort` - Zielport für Server-Tunnel.
- `TargetDestination` oder `Destination` - Ziel für Client-Tunnel, die eines benötigen.
- `StartOnLoad` - boolescher Wert, ob der Tunnel beim Laden gestartet werden soll.
- `Description` - Tunnel-Beschreibung.
- `ReachableBy` - Interface/Adresse, an dem der Tunnel lauscht.
- `Shared` - boolescher Wert, ob der Client-Tunnel geteilt werden soll.
- `UseSSL` - boolescher Wert, SSL aktivieren, wo unterstützt.
- `TunnelLength` - Tunnel-Länge, von `0` bis `3`.
- `TunnelVariance` - Tunnel-Streuung, von `-2` bis `2`.
- `TunnelQuantity` - Anzahl der Tunnel, von `1` bis `6`.
- `TunnelBackupQuantity` - Anzahl der Sicherungs-Tunnel, von `0` bis `3`.
- `SigType` - Typ des Signaturschlüssels.
- `EncType` - Verschlüsselungstyp.
- `CustomOptions` - benutzerdefinierte Tunnel-Optionen.

Optionen für den Client-Proxy:

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

Optionen zur Clientverwaltung:

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

HTTP-Client-Filteroptionen:

- `AllowUserAgent`
- `AllowReferer`
- `AllowAccept`
- `AllowInternalSSL`

Serveroptionen:

- `WebsiteHostname` oder `SpoofedHost`
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

LeaseSet-Optionen:

- `EncryptLeaseSet` - einer der folgenden Werte:
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

Beispiel erstellen:

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
Rückgabe:

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
Beispiel bearbeiten:

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
Rückgabe:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - edited tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
Abrufen-Beispiel (NUR GETTER) Gibt zurück – `Map<String, Object>` (Informationen) und `String` (Status):

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
Rückgabe:

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
Starten, Stoppen, Neustarten, Löschen Beispiel: Sie folgen der gleichen Struktur, unterscheiden sich jedoch nur in den `Action`-Parametern:

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
Rückgabe:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - starting tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
### Methode - ClientServicesInfo *(übernommen von i2pd)*

Die Methode `ClientServicesInfo` gibt Statusinformationen über auf dem Router laufende Clientservices zurück. Fügen Sie die gewünschten Service-Schlüssel (mit einem beliebigen Wert) in `params` ein, um den Status jedes Dienstes anzufordern.

Unterstützte Parameter:

- `I2PTunnel` - gibt eine Zuordnung von konfigurierten Tunnelnamen zu deren Adressen zurück, aufgeteilt in die Unterobjekte `client` und `server`.
- `HTTPProxy` - gibt den Aktivierungsstatus und die Adresse des HTTP-Proxys zurück.
- `SOCKS` - gibt den Aktivierungsstatus und die Adresse des SOCKS-Proxys zurück.
- `SAM` - gibt den Aktivierungsstatus des SAM-Bridges sowie Informationen zu aktiven Sitzungen zurück.
- `BOB` - gibt den Aktivierungsstatus des BOB-Bridges zurück. (In Java I2P veraltet; gibt immer `false` zurück.)
- `I2CP` - gibt den Aktivierungsstatus des I2CP-Servers zurück.

Beispiel:

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
Rückgabe:

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
## Kompatibilität

Die Kompatibilität mit der bestehenden i2pcontrol-API sollte erhalten bleiben, da die neuen Methoden und Parameter auf eine Weise hinzugefügt werden, die die bestehende Funktionalität nicht beeinträchtigt. Bestehende Anwendungen, die die i2pcontrol-API nutzen, sollten weiterhin ohne Änderungen funktionieren, während neue Anwendungen die zusätzlichen Informationen und Funktionen nutzen können, die in diesem Vorschlag bereitgestellt werden.

## Implementierung

### Java I2P

Dieser Vorschlag ist noch nicht in Java I2P implementiert, der Code ist jedoch im [i2p.plugins.i2pcontrol](https://github.com/i2p/i2p.plugins.i2pcontrol)-Repository unter dem Pull Request [#6](https://github.com/i2p/i2p.plugins.i2pcontrol/pull/6) verfügbar. Dies geschah, um das Testen und die Entwicklung der neuen Methoden zu ermöglichen, ohne den bestehenden Code zu beeinträchtigen. Sobald der Code für den Produktiveinsatz bereit ist, wird er in das Haupt-I2P-Repository im i2pcontrol-Verzeichnis übernommen.

### i2pd

Methoden und Parameter, die als „(übernommen aus i2pd)“ gekennzeichnet sind, sind in i2pd implementiert und in diesem Vorschlag unverändert. Die Erweiterungen von i2pd müssen im Rahmen dieses Vorschlags nicht geändert werden. Teile dieses Vorschlags, die nicht gekennzeichnet sind, sind in i2pd nicht implementiert.

### go-i2p

go-i2p verfolgt diesen Vorschlag mit der Motivation, seine Router-Konsolenanwendung zu ermöglichen und zu verbessern. Es wird den Vorschlag in Zukunft übernehmen und umsetzen.

### Emissary

Die Wahrscheinlichkeit der Einführung in Emissary ist derzeit unbekannt, jedoch wird Emissary voraussichtlich in gleicher Weise von diesem Vorschlag profitieren wie go-i2p.

## Leistung

Keine Auswirkungen auf die Leistung erwartet.
