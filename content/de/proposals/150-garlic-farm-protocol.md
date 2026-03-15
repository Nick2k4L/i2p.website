---
title: "Garlic Farm-Protokoll"
number: "150"
author: "zzz"
created: "2019-05-02"
lastupdated: "2019-05-20"
status: "Offen"
thread: "http://zzz.i2p/topics/2234"
toc: true
---
## Übersicht

Dies ist die Spezifikation für das Garlic-Farm-Übertragungsprotokoll,
basierend auf JRaft, dessen „exts“-Code zur Implementierung über TCP
und seiner „dmprinter“-Beispielanwendung [JRAFT](https://github.com/datatechnology/jraft).


Wir konnten keine Implementierung mit dokumentiertem Übertragungsprotokoll finden.
Allerdings ist die JRaft-Implementierung einfach genug, sodass wir
den Code analysieren und anschließend dessen Protokoll dokumentieren konnten.
Dieser Vorschlag ist das Ergebnis dieser Bemühung.

Dies wird die Backend-Koordinierung für Router sein, die
Einträge in einem Meta-LeaseSet veröffentlichen. Siehe Vorschlag 123.


## Ziele

- Geringe Codegröße
- Basierend auf bestehender Implementierung
- Keine serialisierten Java-Objekte oder Java-spezifischen Funktionen oder Kodierungen
- Bootstrapping ist außerhalb des Anwendungsbereichs. Es wird angenommen,
  dass mindestens ein anderer Server hartcodiert ist oder außerhalb dieses Protokolls konfiguriert wurde.
- Unterstützung sowohl von außerhalb des Bandes als auch von innerhalb-I2P-Anwendungsfällen.


## Entwurf

Das Raft-Protokoll ist kein konkretes Protokoll; es definiert lediglich eine Zustandsmaschine.
Daher dokumentieren wir das konkrete Protokoll von JRaft und basieren unser Protokoll darauf.
Es gibt keine Änderungen am JRaft-Protokoll, außer der Hinzufügung
eines Authentifizierungs-Handshakes.

Raft wählt einen Leader, dessen Aufgabe es ist, ein Protokoll (Log) zu veröffentlichen.
Das Protokoll enthält Raft-Konfigurationsdaten und Anwendungsdaten.
Anwendungsdaten enthalten den Status jedes Servers-Routers und das Ziel
für den Meta-LS2-Cluster.
Die Server verwenden einen gemeinsamen Algorithmus, um den Veröffentlicher und Inhalt
des Meta-LS2 zu bestimmen.
Der Veröffentlicher des Meta-LS2 ist NICHT notwendigerweise der Raft-Leader.



## Spezifikation

Das Übertragungsprotokoll erfolgt über SSL-Sockets oder nicht-SSL-I2P-Sockets.
I2P-Sockets werden über den HTTP-Proxy weitergeleitet.
Es gibt keine Unterstützung für Clearnet-Non-SSL-Sockets.

### Handshake und Authentifizierung

Nicht durch JRaft definiert.

Ziele:

- Benutzer/Passwort-Authentifizierungsmethode
- Versionskennung
- Cluster-Kennung
- Erweiterbar
- Einfache Weiterleitung bei Verwendung für I2P-Sockets
- Server nicht unnötig als Garlic-Farm-Server offenlegen
- Einfaches Protokoll, sodass keine vollständige Webserver-Implementierung erforderlich ist
- Kompatibel mit gängigen Standards, sodass Implementierungen ggf. Standardbibliotheken verwenden können

Wir verwenden einen websocket-ähnlichen Handshake und
HTTP-Digest-Authentifizierung [RFC 2617](https://tools.ietf.org/html/rfc2617).
RFC 2617 Basic-Authentifizierung wird NICHT unterstützt.
Bei der Weiterleitung über den HTTP-Proxy kommunizieren Sie mit
dem Proxy wie in [RFC 2616](https://tools.ietf.org/html/rfc2616) spezifiziert.

#### Anmeldeinformationen

Ob Benutzernamen und Passwörter pro Cluster oder
pro Server sind, ist implementierungsabhängig.


#### HTTP-Anfrage 1

Der Initiator sendet Folgendes.

Alle Zeilen werden mit CRLF abgeschlossen, wie von HTTP gefordert.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: close
  (alle weiteren Header werden ignoriert)
  (leere Zeile)

  CLUSTER ist der Name des Clusters (Standard „farm“)
  VERSION ist die Garlic-Farm-Version (derzeit „1“)

```


#### HTTP-Antwort 1

Wenn der Pfad nicht korrekt ist, sendet der Empfänger eine Standardantwort „HTTP/1.1 404 Not Found“,
wie in [RFC 2616](https://tools.ietf.org/html/rfc2616).

Wenn der Pfad korrekt ist, sendet der Empfänger eine Standardantwort „HTTP/1.1 401 Unauthorized“,
einschließlich des WWW-Authenticate-HTTP-Digest-Authentifizierungs-Headers,
wie in [RFC 2617](https://tools.ietf.org/html/rfc2617).

Beide Parteien schließen dann den Socket.


#### HTTP-Anfrage 2

Der Initiator sendet Folgendes,
wie in [RFC 2617](https://tools.ietf.org/html/rfc2617).

Alle Zeilen werden mit CRLF abgeschlossen, wie von HTTP gefordert.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: keep-alive, Upgrade
  Upgrade: websocket
  (Sec-Websocket-* Header, falls weitergeleitet)
  Authorization: (HTTP-Digest-Authorisierungs-Header gemäß RFC 2617)
  (alle weiteren Header werden ignoriert)
  (leere Zeile)

  CLUSTER ist der Name des Clusters (Standard „farm“)
  VERSION ist die Garlic-Farm-Version (derzeit „1“)

```


#### HTTP-Antwort 2

Wenn die Authentifizierung nicht korrekt ist, sendet der Empfänger eine weitere Standardantwort „HTTP/1.1 401 Unauthorized“,
wie in [RFC 2617](https://tools.ietf.org/html/rfc2617).

Wenn die Authentifizierung korrekt ist, sendet der Empfänger die folgende Antwort,
wie im WebSocket-Protokoll.

Alle Zeilen werden mit CRLF abgeschlossen, wie von HTTP gefordert.

```text

HTTP/1.1 101 Switching Protocols
  Connection: Upgrade
  Upgrade: websocket
  (Sec-Websocket-* Header)
  (alle weiteren Header werden ignoriert)
  (leere Zeile)

```

Nach Empfang bleibt der Socket geöffnet.
Das unten definierte Raft-Protokoll beginnt auf demselben Socket.


#### Zwischenspeicherung

Anmeldeinformationen müssen mindestens eine Stunde lang zwischengespeichert werden, sodass
nachfolgende Verbindungen direkt zu
„HTTP-Anfrage 2“ oben springen können.



### Nachrichtentypen

Es gibt zwei Arten von Nachrichten: Anfragen und Antworten.
Anfragen können Protokolleinträge (Log Entries) enthalten und sind variabel groß;
Antworten enthalten keine Protokolleinträge und sind fest groß.

Nachrichtentypen 1–4 sind die standardmäßigen RPC-Nachrichten, die von Raft definiert werden.
Dies ist das Kern-Raft-Protokoll.

Nachrichtentypen 5–15 sind die erweiterten RPC-Nachrichten, die von
JRaft definiert werden, um Clients, dynamische Serveränderungen und
effiziente Protokollsynchronisierung zu unterstützen.

Nachrichtentypen 16–17 sind die Protokollkomprimierungs-RPC-Nachrichten, die
im Raft-Abschnitt 7 definiert sind.


| Nachricht | Nummer | Gesendet von | Gesendet an | Hinweise |
| :--- | :--- | :--- | :--- | :--- |
| RequestVoteRequest | 1 | Kandidat | Follower | Standard-Raft-RPC; darf keine Protokolleinträge enthalten |
| RequestVoteResponse | 2 | Follower | Kandidat | Standard-Raft-RPC |
| AppendEntriesRequest | 3 | Leader | Follower | Standard-Raft-RPC |
| AppendEntriesResponse | 4 | Follower | Leader / Client | Standard-Raft-RPC |
| ClientRequest | 5 | Client | Leader / Follower | Antwort ist AppendEntriesResponse; darf nur Anwendungs-Protokolleinträge enthalten |
| AddServerRequest | 6 | Client | Leader | Darf nur einen einzigen ClusterServer-Protokolleintrag enthalten |
| AddServerResponse | 7 | Leader | Client | Leader sendet auch eine JoinClusterRequest |
| RemoveServerRequest | 8 | Follower | Leader | Darf nur einen einzigen ClusterServer-Protokolleintrag enthalten |
| RemoveServerResponse | 9 | Leader | Follower | |
| SyncLogRequest | 10 | Leader | Follower | Darf nur einen einzigen LogPack-Protokolleintrag enthalten |
| SyncLogResponse | 11 | Follower | Leader | |
| JoinClusterRequest | 12 | Leader | Neuer Server | Einladung zum Beitritt; darf nur einen einzigen Konfigurations-Protokolleintrag enthalten |
| JoinClusterResponse | 13 | Neuer Server | Leader | |
| LeaveClusterRequest | 14 | Leader | Follower | Befehl zum Verlassen |
| LeaveClusterResponse | 15 | Follower | Leader | |
| InstallSnapshotRequest | 16 | Leader | Follower | Raft Abschnitt 7; Darf nur einen einzigen SnapshotSyncRequest-Protokolleintrag enthalten |
| InstallSnapshotResponse | 17 | Follower | Leader | Raft Abschnitt 7 |


### Aufbau

Nach dem HTTP-Handshake ist die Aufbau-Sequenz wie folgt:

```text

Neuer Server Alice              Zufälliger Follower Bob

  ClientRequest   ------->
          <---------   AppendEntriesResponse

  Wenn Bob sagt, er sei der Leader, weiter unten fortfahren.
  Andernfalls muss Alice sich von Bob trennen und mit dem Leader verbinden.


  Neuer Server Alice              Leader Charlie

  ClientRequest   ------->
          <---------   AppendEntriesResponse
  AddServerRequest   ------->
          <---------   AddServerResponse
          <---------   JoinClusterRequest
  JoinClusterResponse  ------->
          <---------   SyncLogRequest
                       ODER InstallSnapshotRequest
  SyncLogResponse  ------->
  ODER InstallSnapshotResponse

```

Trennungs-Sequenz:

```text

Follower Alice              Leader Charlie

  RemoveServerRequest   ------->
          <---------   RemoveServerResponse
          <---------   LeaveClusterRequest
  LeaveClusterResponse  ------->

```

Wahl-Sequenz:

```text

Kandidat Alice               Follower Bob

  RequestVoteRequest   ------->
          <---------   RequestVoteResponse

  wenn Alice die Wahl gewinnt:

  Leader Alice                Follower Bob

  AppendEntriesRequest   ------->
  (Heartbeat)
          <---------   AppendEntriesResponse

```


### Definitionen

- Quelle (Source): Identifiziert den Ursprung der Nachricht
- Ziel (Destination): Identifiziert den Empfänger der Nachricht
- Begriffe (Terms): Siehe Raft. Initialisiert auf 0, monoton steigend
- Indizes (Indexes): Siehe Raft. Initialisiert auf 0, monoton steigend



### Anfragen

Anfragen enthalten einen Header und null oder mehr Protokolleinträge.
Anfragen enthalten einen Header fester Größe und optionale Protokolleinträge variabler Größe.


#### Anfrage-Header

Der Anfrage-Header ist 45 Bytes groß, wie folgt.
Alle Werte sind vorzeichenlose Big-Endian-Werte.

```text

Nachrichtentyp:      1 Byte
  Quelle:              ID, 4-Byte-Ganzzahl
  Ziel:                ID, 4-Byte-Ganzzahl
  Begriff (Term):      Aktueller Begriff (siehe Hinweise), 8-Byte-Ganzzahl
  Letzter Protokollbegriff:     8-Byte-Ganzzahl
  Letzter Protokollindex:    8-Byte-Ganzzahl
  Commit-Index:      8-Byte-Ganzzahl
  Protokolleinträge-Größe:  Gesamtgröße in Bytes, 4-Byte-Ganzzahl
  Protokolleinträge:       siehe unten, Gesamtlänge wie angegeben

```


#### Hinweise

In der RequestVoteRequest ist „Term“ der Begriff des Kandidaten.
Ansonsten ist es der aktuelle Begriff des Leaders.

In der AppendEntriesRequest ist diese Nachricht eine Heartbeat-Nachricht (Keepalive),
wenn die Größe der Protokolleinträge null ist.



#### Protokolleinträge

Das Protokoll enthält null oder mehr Protokolleinträge.
Jeder Protokolleintrag ist wie folgt.
Alle Werte sind vorzeichenlose Big-Endian-Werte.

```text

Begriff (Term):           8-Byte-Ganzzahl
  Werttyp:     1 Byte
  Eintragsgröße:     In Bytes, 4-Byte-Ganzzahl
  Eintrag:          Länge wie angegeben

```


#### Protokollinhalte

Alle Werte sind vorzeichenlose Big-Endian-Werte.

| Protokoll-Werttyp | Nummer |
| :--- | :--- |
| Anwendung | 1 |
| Konfiguration | 2 |
| ClusterServer | 3 |
| LogPack | 4 |
| SnapshotSyncRequest | 5 |


#### Anwendung

Anwendungsinhalte sind UTF-8-kodiertes [JSON](https://www.json.org/).
Siehe Abschnitt Anwendungsschicht unten.


#### Konfiguration

Wird vom Leader verwendet, um eine neue Clusterkonfiguration zu serialisieren und an Peers zu replizieren.
Enthält null oder mehr ClusterServer-Konfigurationen.


```text

Protokollindex:  8-Byte-Ganzzahl
  Letzter Protokollindex:  8-Byte-Ganzzahl
  ClusterServer-Daten für jeden Server:
    ID:                4-Byte-Ganzzahl
    Endpunkt-Datenlänge: In Bytes, 4-Byte-Ganzzahl
    Endpunkt-Daten:     ASCII-Zeichenkette der Form „tcp://localhost:9001“, Länge wie angegeben

```


#### ClusterServer

Die Konfigurationsinformationen für einen Server in einem Cluster.
Wird nur in einer AddServerRequest- oder RemoveServerRequest-Nachricht enthalten.

Wenn in einer AddServerRequest-Nachricht verwendet:

```text

ID:                4-Byte-Ganzzahl
  Endpunkt-Datenlänge: In Bytes, 4-Byte-Ganzzahl
  Endpunkt-Daten:     ASCII-Zeichenkette der Form „tcp://localhost:9001“, Länge wie angegeben

```


Wenn in einer RemoveServerRequest-Nachricht verwendet:

```text

ID:                4-Byte-Ganzzahl

```


#### LogPack

Wird nur in einer SyncLogRequest-Nachricht enthalten.

Folgendes wird vor der Übertragung gzipped:

```text

Indexdatenlänge: In Bytes, 4-Byte-Ganzzahl
  Protokolldatenlänge:   In Bytes, 4-Byte-Ganzzahl
  Indexdaten:     8 Bytes für jeden Index, Länge wie angegeben
  Protokolldaten:       Länge wie angegeben

```



#### SnapshotSyncRequest

Wird nur in einer InstallSnapshotRequest-Nachricht enthalten.

```text

Letzter Protokollindex:  8-Byte-Ganzzahl
  Letzter Protokollbegriff:   8-Byte-Ganzzahl
  Konfigurationsdatenlänge: In Bytes, 4-Byte-Ganzzahl
  Konfigurationsdaten:     Länge wie angegeben
  Offset:          Der Offset der Daten in der Datenbank, in Bytes, 8-Byte-Ganzzahl
  Datenlänge:        In Bytes, 4-Byte-Ganzzahl
  Daten:            Länge wie angegeben
  Ist abgeschlossen:         1 wenn abgeschlossen, 0 wenn nicht (1 Byte)

```




### Antworten

Alle Antworten sind 26 Bytes groß, wie folgt.
Alle Werte sind vorzeichenlose Big-Endian-Werte.

```text

Nachrichtentyp:   1 Byte
  Quelle:         ID, 4-Byte-Ganzzahl
  Ziel:           Normalerweise die tatsächliche Ziel-ID (siehe Hinweise), 4-Byte-Ganzzahl
  Begriff (Term):           Aktueller Begriff, 8-Byte-Ganzzahl
  Nächster Index:     Initialisiert auf letzter Protokollindex des Leaders + 1, 8-Byte-Ganzzahl
  Wird akzeptiert:    1 wenn akzeptiert, 0 wenn nicht (siehe Hinweise), 1 Byte

```


#### Hinweise

Die Ziel-ID ist normalerweise die tatsächliche Ziel-ID für diese Nachricht.
Allerdings ist sie bei AppendEntriesResponse, AddServerResponse und RemoveServerResponse
die ID des aktuellen Leaders.

In der RequestVoteResponse ist „Wird akzeptiert“ 1 für eine Stimme für den Kandidaten (Anfragenden),
und 0 für keine Stimme.


## Anwendungsschicht

Jeder Server veröffentlicht regelmäßig Anwendungsdaten im Protokoll über eine ClientRequest.
Anwendungsdaten enthalten den Status jedes Server-Routers und das Ziel
für den Meta-LS2-Cluster.
Die Server verwenden einen gemeinsamen Algorithmus, um den Veröffentlicher und Inhalt
des Meta-LS2 zu bestimmen.
Der Server mit dem „besten“ aktuellen Status im Protokoll ist der Meta-LS2-Veröffentlicher.
Der Veröffentlicher des Meta-LS2 ist NICHT notwendigerweise der Raft-Leader.


### Anwendungsinhalte

Anwendungsinhalte sind aus Gründen der Einfachheit und Erweiterbarkeit UTF-8-kodiertes [JSON](https://json.org/).
Die vollständige Spezifikation steht noch aus.
Ziel ist es, genügend Daten bereitzustellen, um einen Algorithmus zu schreiben, der den „besten“
Router zur Veröffentlichung des Meta-LS2 bestimmt, und damit der Veröffentlicher ausreichend Informationen hat,
um die Ziele im Meta-LS2 gewichten zu können.
Die Daten enthalten sowohl Router- als auch Ziel-Statistiken.

Die Daten können optional Fernmessdaten über die Gesundheit der
anderen Server und die Fähigkeit zum Abrufen des Meta-LS enthalten.
Diese Daten würden in der ersten Version nicht unterstützt.

Die Daten können optional Konfigurationsinformationen enthalten, die
von einem Administrator-Client gepostet wurden.
Diese Daten würden in der ersten Version nicht unterstützt.

Wenn „name: Wert“ aufgelistet ist, gibt dies den JSON-Map-Schlüssel und -Wert an.
Andernfalls steht die Spezifikation noch aus.


Clusterdaten (oberste Ebene):

- cluster: Clustername
- date: Datum dieser Daten (lang, ms seit Epoche)
- id: Raft-ID (Ganzzahl)

Konfigurationsdaten (config):

- Alle Konfigurationsparameter

MetaLS-Veröffentlichungsstatus (meta):

- destination: das metals-Ziel, base64
- lastPublishedLS: falls vorhanden, base64-Kodierung des zuletzt veröffentlichten metals
- lastPublishedTime: in ms, oder 0 wenn nie
- publishConfig: Publisher-Konfigurationsstatus aus/ein/auto
- publishing: metals-Publisher-Status boolean true/false

Routerdaten (router):

- lastPublishedRI: falls vorhanden, base64-Kodierung der zuletzt veröffentlichten Router-Info
- uptime: Betriebszeit in ms
- Job-Lag
- Exploratorische Tunnel
- Teilnehmende Tunnel
- Konfigurierte Bandbreite
- Aktuelle Bandbreite

Ziele (destinations):
Liste

Zieldaten:

- destination: das Ziel, base64
- uptime: Betriebszeit in ms
- Konfigurierte Tunnel
- Aktuelle Tunnel
- Konfigurierte Bandbreite
- Aktuelle Bandbreite
- Konfigurierte Verbindungen
- Aktuelle Verbindungen
- Blacklist-Daten

Fernmessdaten des Remote-Routers:

- Letzte gesehene RI-Version
- LS-Abrufzeit
- Verbindungstestdaten
- Profildaten der nächstgelegenen Floodfills
  für die Zeiträume gestern, heute und morgen

Fernmessdaten des Remote-Ziels:

- Letzte gesehene LS-Version
- LS-Abrufzeit
- Verbindungstestdaten
- Profildaten der nächstgelegenen Floodfills
  für die Zeiträume gestern, heute und morgen

Meta-LS-Fernmessdaten:

- Letzte gesehene Version
- Abrufzeit
- Profildaten der nächstgelegenen Floodfills
  für die Zeiträume gestern, heute und morgen


## Administrations-Schnittstelle

Steht noch aus, möglicherweise ein separater Vorschlag.
Für die erste Version nicht erforderlich.

Anforderungen an eine Admin-Schnittstelle:

- Unterstützung mehrerer Master-Ziele, d.h. mehrerer virtueller Cluster (Farms)
- Umfassende Ansicht des gemeinsamen Clusterzustands – alle von Mitgliedern veröffentlichten Statistiken, wer der aktuelle Leader ist, usw.
- Möglichkeit, einen Teilnehmer oder Leader aus dem Cluster zu entfernen
- Möglichkeit, MetaLS manuell zu veröffentlichen (wenn der aktuelle Knoten der Veröffentlicher ist)
- Möglichkeit, Hashes vom MetaLS auszuschließen (wenn der aktuelle Knoten der Veröffentlicher ist)
- Import-/Export-Funktion für Konfigurationen für Massendeployments



## Router-Schnittstelle

Steht noch aus, möglicherweise ein separater Vorschlag.
i2pcontrol ist für die erste Version nicht erforderlich, detaillierte Änderungen werden in einem separaten Vorschlag enthalten sein.

Anforderungen an die Garlic-Farm-zu-Router-API (in-JVM Java oder i2pcontrol)

- getLocalRouterStatus()
- getLocalLeafHash(Hash masterHash)
- getLocalLeafStatus(Hash leaf)
- getRemoteMeasuredStatus(Hash masterOrLeaf) // wahrscheinlich nicht im MVP
- publishMetaLS(Hash masterHash, List<MetaLease> contents) // oder signiertes MetaLeaseSet? Wer signiert?
- stopPublishingMetaLS(Hash masterHash)
- Authentifizierung noch offen?


## Begründung

Atomix ist zu groß und erlaubt keine Anpassung, um
das Protokoll über I2P weiterzuleiten. Außerdem ist sein Übertragungsformat ungedokumentiert und hängt
von Java-Serialisierung ab.


## Hinweise



## Probleme

- Es gibt keine Möglichkeit, dass ein Client den unbekannten Leader erkennt und sich mit ihm verbindet.
  Es wäre eine geringfügige Änderung, damit ein Follower die Konfiguration als Protokolleintrag in der AppendEntriesResponse sendet.



## Migration

Keine Abwärtskompatibilitätsprobleme.


## Referenzen

* [JRAFT](https://github.com/datatechnology/jraft)
* [JSON](https://json.org/)
* [RAFT](/docs/research/ongaro2014-raft.pdf)
* [RFC-2616](https://tools.ietf.org/html/rfc2616)
* [RFC-2617](https://tools.ietf.org/html/rfc2617)
* [WEBSOCKET](https://en.wikipedia.org/wiki/WebSocket)
