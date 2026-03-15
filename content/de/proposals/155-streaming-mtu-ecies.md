---
title: "Streaming MTU für ECIES-Ziele"
number: "155"
author: "zzz"
created: "2020-05-06"
lastupdated: "2020-05-30"
status: "Geschlossen"
thread: "http://zzz.i2p/topics/2886"
target: "0.9.47"
implementedin: "0.9.47"
toc: true
---
## Hinweis
Netzwerk-Deployment und Tests sind im Gange.
Vorbehaltlich geringfügiger Änderungen.


## Übersicht


### Zusammenfassung

ECIES reduziert den Overhead bestehender Sitzungsnachrichten (ES) um etwa 90 Byte.
Daher können wir die MTU für ECIES-Verbindungen um etwa 90 Byte erhöhen.
Siehe die [ECIES-Spezifikation](/docs/specs/ecies/#overhead), [Streaming-Spezifikation](/docs/specs/streaming/#flags-and-option-data-fields) und [Streaming-API-Dokumentation](/docs/api/streaming/).

Ohne Erhöhung der MTU werden die Overhead-Einsparungen in vielen Fällen nicht wirklich „eingespart“,
da die Nachrichten ohnehin auf zwei volle Tunnelnachrichten aufgefüllt werden.

Dieser Vorschlag erfordert keine Änderung der Spezifikationen.
Er wird lediglich als Vorschlag veröffentlicht, um Diskussion und Konsensbildung
über den empfohlenen Wert und die Implementierungsdetails zu erleichtern.


### Ziele

- Erhöhung der verhandelten MTU
- Maximale Nutzung von 1-KB-Tunnelnachrichten
- Keine Änderung des Streaming-Protokolls


## Entwurf

Verwenden Sie die vorhandene Option MAX_PACKET_SIZE_INCLUDED und die MTU-Verhandlung.
Streaming verwendet weiterhin das Minimum aus gesendeter und empfangener MTU.
Der Standardwert bleibt für alle Verbindungen 1730, unabhängig davon, welche Schlüssel verwendet werden.

Implementierungen werden dazu ermutigt, die Option MAX_PACKET_SIZE_INCLUDED in alle SYN-Pakete in beide Richtungen aufzunehmen,
obwohl dies keine Anforderung ist.

Wenn ein Ziel ausschließlich ECIES verwendet, wird der höhere Wert verwendet (egal ob als Alice oder Bob).
Wenn ein Ziel Dual-Key-fähig ist, kann sich das Verhalten unterscheiden:

Wenn der Dual-Key-Client außerhalb des Routers ist (in einer externen Anwendung),
kann er möglicherweise nicht „wissen“, welcher Schlüssel am entfernten Ende verwendet wird, und Alice kann
einen höheren Wert im SYN anfordern, während die maximale Datenmenge im SYN weiterhin 1730 beträgt.

Wenn der Dual-Key-Client innerhalb des Routers ist, kann die Information darüber, welcher Schlüssel
verwendet wird, dem Client möglicherweise bekannt sein oder auch nicht.
Das Leaseset wurde möglicherweise noch nicht abgerufen, oder die internen API-Schnittstellen
stellen diese Information dem Client nicht leicht zur Verfügung.
Falls die Information verfügbar ist, kann Alice den höheren Wert verwenden;
andernfalls muss Alice den Standardwert von 1730 verwenden, bis eine Verhandlung erfolgt.

Ein Dual-Key-Client als Bob kann den höheren Wert in der Antwort senden,
auch wenn kein Wert oder ein Wert von 1730 von Alice empfangen wurde;
es gibt jedoch keine Möglichkeit, in Streaming nach oben zu verhandeln,
daher sollte die MTU bei 1730 bleiben.


Wie in der [Streaming-API-Dokumentation](/docs/api/streaming/) erwähnt,
kann die Datenmenge in den SYN-Paketen, die von Alice an Bob gesendet werden, Bobs MTU überschreiten.
Dies ist eine Schwachstelle im Streaming-Protokoll.
Daher müssen Dual-Key-Clients die Daten in den gesendeten SYN-Paketen
auf 1730 Bytes begrenzen, während sie einen höheren MTU-Wert angeben.
Sobald der höhere MTU-Wert von Bob empfangen wurde, kann Alice die tatsächlich gesendete maximale Nutzlast erhöhen.


### Analyse

Wie in der [ECIES-Spezifikation](/docs/specs/ecies/#overhead) beschrieben, beträgt der ElGamal-Overhead für bestehende Sitzungsnachrichten
151 Bytes, und der Ratchet-Overhead beträgt 69 Bytes.
Daher können wir die MTU für Ratchet-Verbindungen um (151 - 69) = 82 Bytes erhöhen,
von 1730 auf 1812.


## Spezifikation

Fügen Sie die folgenden Änderungen und Klarstellungen zum Abschnitt „MTU Selection and Negotiation“ der [Streaming-API-Dokumentation](/docs/api/streaming/) hinzu.
Keine Änderungen an der [Streaming-Spezifikation](/docs/specs/streaming/).

Der Standardwert der Option i2p.streaming.maxMessageSize bleibt für alle Verbindungen 1730, unabhängig davon, welche Schlüssel verwendet werden.
Clients müssen wie üblich das Minimum aus gesendeter und empfangener MTU verwenden.

Es gibt vier verwandte MTU-Konstanten und -Variablen:

- DEFAULT_MTU: 1730, unverändert, für alle Verbindungen
- i2cp.streaming.maxMessageSize: Standard 1730 oder 1812, kann durch Konfiguration geändert werden
- ALICE_SYN_MAX_DATA: Die maximale Datenmenge, die Alice in ein SYN-Paket einfügen darf
- negotiated_mtu: Das Minimum aus Alices und Bobs MTU, wird als maximale Datengröße
  im SYN-ACK von Bob an Alice und in allen nachfolgenden Paketen in beide Richtungen verwendet


Es gibt fünf Fälle zu berücksichtigen:


### 1) Alice nur ElGamal
Keine Änderung, 1730 MTU in allen Paketen.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize Standardwert: 1730
- Alice kann MAX_PACKET_SIZE_INCLUDED im SYN senden, nicht erforderlich, es sei denn, der Wert ist != 1730


### 2) Alice nur ECIES
1812 MTU in allen Paketen.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize Standardwert: 1812
- Alice muss MAX_PACKET_SIZE_INCLUDED im SYN senden


### 3) Alice Dual-Key und weiß, dass Bob ElGamal verwendet
1730 MTU in allen Paketen.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize Standardwert: 1812
- Alice kann MAX_PACKET_SIZE_INCLUDED im SYN senden, nicht erforderlich, es sei denn, der Wert ist != 1730


### 4) Alice Dual-Key und weiß, dass Bob ECIES verwendet
1812 MTU in allen Paketen.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize Standardwert: 1812
- Alice muss MAX_PACKET_SIZE_INCLUDED im SYN senden


### 5) Alice Dual-Key und Bobs Schlüssel ist unbekannt
Sende 1812 als MAX_PACKET_SIZE_INCLUDED im SYN-Paket, beschränke aber die Daten im SYN-Paket auf 1730.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize Standardwert: 1812
- Alice muss MAX_PACKET_SIZE_INCLUDED im SYN senden


### Für alle Fälle

Alice und Bob berechnen
negotiated_mtu, das Minimum aus Alices und Bobs MTU, das als maximale Datengröße
im SYN-ACK von Bob an Alice und in allen nachfolgenden Paketen in beide Richtungen verwendet wird.


## Begründung

Siehe den [Java-I2P-Quellcode](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220) dafür, warum der aktuelle Wert 1730 ist.
Siehe die [ECIES-Spezifikation](/docs/specs/ecies/#overhead), warum der ECIES-Overhead 82 Bytes geringer ist als ElGamal.


## Implementierungshinweise

Wenn Streaming Nachrichten optimaler Größe erzeugt, ist es sehr wichtig, dass
die ECIES-Ratchet-Schicht nicht über diese Größe hinaus auffüllt.

Die empfohlene Größe einer Garlic-Nachricht, um in zwei Tunnelnachrichten zu passen,
einschließlich des 16-Byte-Garlic-Nachrichten-I2NP-Headers, 4-Byte-Garlic-Nachrichtenlänge,
8-Byte-ES-Tag und 16-Byte-MAC, beträgt 1956 Bytes.

Ein empfohlener Auffüllalgorithmus in ECIES ist wie folgt:

- Wenn die Gesamtlänge der Garlic-Nachricht 1954–1956 Bytes betragen würde,
  füge keinen Auffüllblock hinzu (kein Platz)
- Wenn die Gesamtlänge der Garlic-Nachricht 1938–1953 Bytes betragen würde,
  füge einen Auffüllblock hinzu, um genau auf 1956 Bytes aufzufüllen.
- Andernfalls wie üblich auffüllen, z. B. mit einer zufälligen Menge von 0–15 Bytes.

Ähnliche Strategien könnten bei der optimalen Ein-Tunnel-Nachrichten-Größe (964)
und Drei-Tunnel-Nachrichten-Größe (2952) verwendet werden, obwohl diese Größen in der Praxis selten sein sollten.


## Probleme

Der Wert 1812 ist vorläufig. Muss bestätigt und ggf. angepasst werden.


## Migration

Keine Abwärtskompatibilitätsprobleme.
Dies ist eine bestehende Option, und die MTU-Verhandlung ist bereits Teil der Spezifikation.

Ältere ECIES-Ziele unterstützen 1730.
Jeder Client, der einen höheren Wert empfängt, wird mit 1730 antworten, und das entfernte Ende
wird wie üblich nach unten verhandeln.


## Referenzen

* [CALCULATION](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220)
* [ECIES](/docs/specs/ecies/#overhead)
* [STREAMING-OPTIONS](/docs/api/streaming/)
* [STREAMING-SPEC](/docs/specs/streaming/#flags-and-option-data-fields)
