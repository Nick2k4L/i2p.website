---
title: "UDP Tracker"
description: "Protokollspezifikation für UDP-BitTorrent-Ankündigungen in I2P"
slug: "udp-announces"
aliases:
  - "/de/docs/specs/udp-bittorrent-announces"
  - "/de/docs/specs/udp-bittorrent-announces/"
category: "Protokolle"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

## Überblick

Diese Spezifikation dokumentiert das Protokoll für UDP-BitTorrent-Announces in I2P. Für die Gesamtspezifikation von BitTorrent in I2P siehe [BitTorrent over I2P](/docs/applications/bittorrent). Für Hintergrundinformationen und zusätzliche Details zur Entwicklung dieser Spezifikation siehe [Proposal 160](/proposals/160-udp-trackers).

## Design

Dieser Vorschlag verwendet repliable datagram2, repliable datagram3 und raw datagrams, wie in [Datagrams](/docs/specs/datagrams) definiert. Datagram2 und Datagram3 sind neue Varianten von repliable datagrams, die in [Proposal 163](/proposals/163-datagram2-datagram3) definiert sind. Datagram2 fügt Replay-Resistenz und Offline-Signatur-Unterstützung hinzu. Datagram3 ist kleiner als das alte Datagramm-Format, aber ohne Authentifizierung.

### BEP 15

Zur Referenz ist der in [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) definierte Nachrichtenfluss wie folgt:

```
Client                        Tracker
    Connect Req. ------------->
      <-------------- Connect Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
```
Die Verbindungsphase ist erforderlich, um IP-Adress-Spoofing zu verhindern. Der Tracker gibt eine Verbindungs-ID zurück, die der Client in nachfolgenden Ankündigungen verwendet. Diese Verbindungs-ID läuft standardmäßig nach einer Minute beim Client und nach zwei Minuten beim Tracker ab.

I2P wird denselben Nachrichtenfluss wie BEP 15 verwenden, um die Einführung in bestehende UDP-fähige Client-Codebasen zu erleichtern: aus Effizienzgründen und aus Sicherheitsgründen, die unten diskutiert werden:

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
Dies bietet potentiell erhebliche Bandbreiteneinsparungen gegenüber Streaming-(TCP)-Ankündigungen. Während das Datagram2 etwa die gleiche Größe wie ein Streaming-SYN hat, ist die rohe Antwort viel kleiner als das Streaming-SYN-ACK. Nachfolgende Anfragen verwenden Datagram3, und die nachfolgenden Antworten sind roh.

Die Announce-Anfragen sind Datagram3, sodass der Tracker keine große Zuordnungstabelle von Verbindungs-IDs zu Announce-Zielen oder Hashes verwalten muss. Stattdessen kann der Tracker Verbindungs-IDs kryptographisch aus dem Sender-Hash, dem aktuellen Zeitstempel (basierend auf einem bestimmten Intervall) und einem geheimen Wert generieren. Wenn eine Announce-Anfrage empfangen wird, validiert der Tracker die Verbindungs-ID und verwendet dann den Datagram3-Sender-Hash als Sendeziel.

### Verbindungslebensdauer

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html) spezifiziert, dass die Verbindungs-ID beim Client nach einer Minute abläuft und beim Tracker nach zwei Minuten. Dies ist nicht konfigurierbar. Das begrenzt die potenziellen Effizienzgewinne, es sei denn, Clients würden Ankündigungen stapeln, um sie alle innerhalb eines einminütigen Zeitfensters abzuarbeiten. i2psnark stapelt derzeit keine Ankündigungen; es verteilt sie zeitlich, um Traffic-Spitzen zu vermeiden. Power-User betreiben berichten zufolge tausende von Torrents gleichzeitig, und so viele Ankündigungen in eine Minute zu pressen ist nicht realistisch.

Hier schlagen wir vor, die Verbindungsantwort um ein optionales Feld für die Verbindungslebensdauer zu erweitern. Der Standardwert, falls nicht vorhanden, beträgt eine Minute. Andernfalls soll die in Sekunden angegebene Lebensdauer vom Client verwendet werden, und der Tracker wird die Verbindungs-ID für eine weitere Minute aufrechterhalten.

### Kompatibilität mit BEP 15

Dieses Design behält die Kompatibilität mit [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) so weit wie möglich bei, um die erforderlichen Änderungen in bestehenden Clients und Trackern zu begrenzen.

Die einzige erforderliche Änderung ist das Format der Peer-Informationen in der Announce-Antwort. Das Hinzufügen des Lifetime-Feldes in der Connect-Antwort ist nicht erforderlich, wird aber aus Effizienzgründen dringend empfohlen, wie oben erklärt.

### Sicherheitsanalyse

Ein wichtiges Ziel eines UDP-Announce-Protokolls ist es, Address-Spoofing zu verhindern. Der Client muss tatsächlich existieren und ein echtes leaseSet bündeln. Er muss über eingehende Tunnel verfügen, um die Connect Response zu empfangen. Diese Tunnel könnten Zero-Hop sein und sofort aufgebaut werden, aber das würde den Ersteller preisgeben. Dieses Protokoll erreicht dieses Ziel.

### Probleme

- Dieses Protokoll unterstützt keine blinded destinations, kann aber entsprechend erweitert werden. Siehe unten.

## Spezifikation

### Protokolle und Ports

Repliable Datagram2 verwendet I2CP-Protokoll 19; repliable Datagram3 verwendet I2CP-Protokoll 20; rohe Datagramme verwenden I2CP-Protokoll 18. Anfragen können Datagram2 oder Datagram3 sein. Antworten sind immer roh. Das ältere repliable datagram ("Datagram1") Format mit I2CP-Protokoll 17 darf NICHT für Anfragen oder Antworten verwendet werden; diese müssen verworfen werden, wenn sie auf den Anfrage-/Antwort-Ports empfangen werden. Beachten Sie, dass Datagram1-Protokoll 17 weiterhin für das DHT-Protokoll verwendet wird.

Anfragen verwenden den I2CP "to port" aus der Ankündigungs-URL; siehe unten. Der Anfrage-"from port" wird vom Client gewählt, sollte aber ungleich null sein und ein anderer Port als die vom DHT verwendeten, damit Antworten einfach klassifiziert werden können. Tracker sollten Anfragen ablehnen, die am falschen Port empfangen werden.

Antworten verwenden den I2CP "to port" aus der Anfrage. Der "from port" der Anfrage ist der "to port" aus der Anfrage.

### Ankündigungs-URL

Das Announce-URL-Format ist nicht in [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) spezifiziert, aber wie im Clearnet haben UDP-Announce-URLs die Form `udp://host:port/path`. Der Pfad wird ignoriert und kann leer sein, ist aber typischerweise `/announce` im Clearnet. Der `:port`-Teil sollte immer vorhanden sein, jedoch, wenn der `:port`-Teil weggelassen wird, verwende einen Standard-I2CP-Port von 6969, da das der übliche Port im Clearnet ist. Es können auch CGI-Parameter `&a=b&c=d` angehängt werden, diese können verarbeitet und in der Announce-Anfrage bereitgestellt werden, siehe [BEP 41](http://www.bittorrent.org/beps/bep_0041.html). Wenn es keine Parameter oder Pfad gibt, kann der abschließende `/` auch weggelassen werden, wie in [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) impliziert.

### Datagramm-Formate

Alle Werte werden in Netzwerk-Byte-Reihenfolge (Big-Endian) gesendet. Erwarten Sie nicht, dass Pakete genau eine bestimmte Größe haben. Zukünftige Erweiterungen könnten die Größe von Paketen erhöhen.

#### Verbindungsanfrage

Client zu Tracker. 16 Bytes. Muss ein beantwortbares Datagram2 sein. Wie in [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Keine Änderungen.

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
#### Connect-Antwort

Tracker zu Client. 16 oder 18 Bytes. Muss roh sein. Gleich wie in [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) außer wie unten angegeben.

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
Die Antwort MUSS an den I2CP "to port" gesendet werden, der als "from port" der Anfrage empfangen wurde.

Das Feld lifetime ist optional und gibt die Lebensdauer der connection_id des Clients in Sekunden an. Der Standardwert ist 60, und das Minimum, falls angegeben, ist 60. Das Maximum ist 65535 oder etwa 18 Stunden. Der Tracker sollte die connection_id 60 Sekunden länger als die Client-Lebensdauer aufrechterhalten.

#### Ankündigungsanfrage

Client zum Tracker. 98 Bytes mindestens. Muss ein antwortbares Datagram3 sein. Wie in [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) beschrieben, außer den unten angegebenen Abweichungen.

Die connection_id ist wie in der Verbindungsantwort empfangen.

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
Änderungen gegenüber [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- key wird ignoriert
- IP-Adresse wird nicht verwendet
- Port wird wahrscheinlich ignoriert, muss aber derselbe sein wie der I2CP from Port
- Der Options-Abschnitt, falls vorhanden, ist definiert wie in [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)

Die Antwort MUSS an den I2CP "to port" gesendet werden, der als "from port" der Anfrage empfangen wurde. Verwenden Sie nicht den Port aus der Ankündigungsanfrage.

#### Announce Response

Tracker an Client. Mindestens 20 Bytes. Muss raw sein. Wie in [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) außer wie unten vermerkt.

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
Änderungen von [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- Anstelle von 6-Byte IPv4+Port oder 18-Byte IPv6+Port geben wir ein Vielfaches von 32-Byte "kompakte Antworten" mit den SHA-256-Binär-Peer-Hashes zurück. Wie bei TCP-kompakten Antworten schließen wir keinen Port ein.

Die Antwort MUSS an den I2CP "to port" gesendet werden, der als "from port" der Anfrage empfangen wurde. Verwenden Sie nicht den Port aus der Announce-Anfrage.

I2P-Datagramme haben eine sehr große maximale Größe von etwa 64 KB; für zuverlässige Übertragung sollten jedoch Datagramme größer als 4 KB vermieden werden. Für Bandbreiteneffizienz sollten Tracker wahrscheinlich die maximale Anzahl von Peers auf etwa 50 begrenzen, was etwa einem 1600-Byte-Paket vor Overhead auf verschiedenen Schichten entspricht und nach Fragmentierung innerhalb der Nutzlastbegrenzung von zwei tunnel-Nachrichten liegen sollte.

Wie in BEP 15 ist keine Anzahl der folgenden Peer-Adressen (IP/Port für BEP 15, hier Hashes) enthalten. Obwohl in BEP 15 nicht vorgesehen, könnte ein End-of-Peers-Marker aus lauter Nullen definiert werden, um anzuzeigen, dass die Peer-Informationen vollständig sind und einige Erweiterungsdaten folgen.

Damit eine Erweiterung in der Zukunft möglich ist, sollten Clients einen 32-Byte-Hash aus lauter Nullen und alle darauf folgenden Daten ignorieren. Tracker sollten Ankündigungen von einem Hash aus lauter Nullen ablehnen, obwohl dieser Hash bereits von Java-Routern gesperrt wird.

#### Scrapen

Scrape-Anfrage/Antwort aus [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) ist von dieser Spezifikation nicht gefordert, kann aber bei Bedarf implementiert werden, keine Änderungen erforderlich. Der Client muss zuerst eine Verbindungs-ID erhalten. Die Scrape-Anfrage ist immer repliable Datagram3. Die Scrape-Antwort ist immer raw.

#### Fehlerantwort

Tracker zu Client. Mindestens 8 Bytes (wenn die Nachricht leer ist). Muss roh sein. Wie in [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Keine Änderungen.

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
## Erweiterungen

Erweiterungsbits oder ein Versionsfeld sind nicht enthalten. Clients und Tracker sollten nicht davon ausgehen, dass Pakete eine bestimmte Größe haben. Auf diese Weise können zusätzliche Felder hinzugefügt werden, ohne die Kompatibilität zu beeinträchtigen. Das in [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) definierte Erweiterungsformat wird bei Bedarf empfohlen.

Die Connect-Antwort wird modifiziert, um eine optionale Lebensdauer der Verbindungs-ID hinzuzufügen.

Falls Unterstützung für blinded destinations erforderlich ist, können wir entweder die blinded 35-Byte-Adresse am Ende der Announce-Anfrage hinzufügen oder blinded Hashes in den Antworten anfordern, unter Verwendung des [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) Formats (Parameter noch festzulegen). Die Menge der blinded 35-Byte-Peer-Adressen könnte am Ende der Announce-Antwort hinzugefügt werden, nach einem 32-Byte-Hash aus Nullen.

## Implementierungsrichtlinien

Siehe den Designabschnitt oben für eine Diskussion der Herausforderungen für nicht-integrierte, nicht-I2CP-Clients und Tracker.

### Clients

Für einen gegebenen Tracker-Hostnamen sollte ein Client UDP gegenüber HTTP-URLs bevorzugen und nicht an beide senden.

Clients mit bestehender BEP 15-Unterstützung sollten nur kleine Änderungen erfordern.

Wenn ein Client DHT oder andere Datagramm-Protokolle unterstützt, sollte er wahrscheinlich einen anderen Port als "Absender-Port" für die Anfrage wählen, damit die Antworten an diesen Port zurückkommen und nicht mit DHT-Nachrichten vermischt werden. Der Client empfängt nur reine Datagramme als Antworten. Tracker werden niemals ein beantwortbares datagram2 an den Client senden.

Clients mit einer Standard-Liste von Opentrackers sollten die Liste aktualisieren, um UDP-URLs hinzuzufügen, nachdem bekannt ist, dass die bekannten Opentracker UDP unterstützen.

Clients können Wiederholungsübertragungen von Anfragen implementieren oder auch nicht. Wiederholungsübertragungen sollten, falls implementiert, einen anfänglichen Timeout von mindestens 15 Sekunden verwenden und den Timeout für jede Wiederholungsübertragung verdoppeln (exponentieller Backoff).

Clients müssen nach dem Erhalt einer Fehlermeldung eine Pause einlegen.

### Tracker

Tracker mit vorhandener BEP 15-Unterstützung sollten nur kleine Änderungen erfordern. Diese Spezifikation unterscheidet sich vom Vorschlag von 2014 dahingehend, dass der Tracker den Empfang von repliable datagram2 und datagram3 auf demselben Port unterstützen muss.

Um die Ressourcenanforderungen des Trackers zu minimieren, ist dieses Protokoll darauf ausgelegt, jede Anforderung zu eliminieren, dass der Tracker Zuordnungen von Client-Hashes zu Verbindungs-IDs für spätere Validierung speichert. Dies ist möglich, weil das Announce-Request-Paket ein beantwortbares Datagram3-Paket ist und somit den Hash des Absenders enthält.

Eine empfohlene Implementierung ist:

- Definiere die aktuelle Epoche als die aktuelle Zeit mit einer Auflösung der Verbindungslebensdauer, `epoch = now / lifetime`.
- Definiere eine kryptographische Hash-Funktion `H(secret, clienthash, epoch)`, die eine 8-Byte-Ausgabe erzeugt.
- Erzeuge die zufällige Konstante secret, die für alle Verbindungen verwendet wird.
- Für Connect-Antworten erzeuge `connection_id = H(secret, clienthash, epoch)`
- Für Announce-Anfragen validiere die empfangene Verbindungs-ID in der aktuellen Epoche durch Verifikation von `connection_id == H(secret, clienthash, epoch) || connection_id == H(secret, clienthash, epoch - 1)`

## Referenzen

- **[BEP15]** [BEP 15 - UDP Tracker Protocol](http://www.bittorrent.org/beps/bep_0015.html)
- **[BEP41]** [BEP 41 - UDP Tracker Protocol Extensions](http://www.bittorrent.org/beps/bep_0041.html)
- **[DATAGRAMS]** [Datagrams Spezifikation](/docs/specs/datagrams)
- **[Prop160]** [Vorschlag 160 - UDP Tracker](/proposals/160-udp-trackers)
- **[Prop163]** [Vorschlag 163 - Datagram2/Datagram3](/proposals/163-datagram2-datagram3)
- **[SAMv3]** [SAM v3 API](/docs/api/samv3)
- **[SPEC]** [BitTorrent über I2P](/docs/applications/bittorrent)
