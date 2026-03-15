---
title: "ECIES-X25519-AEAD-Ratchet"
aliases:
  - "/de/proposals/144-ecies-x25519"
  - "/de/proposals/144-ecies-x25519/"
number: "144"
author: "zzz, chisana, orignal"
created: "2018-11-22"
lastupdated: "2025-03-05"
status: "Geschlossen"
thread: "http://zzz.i2p/topics/2639"
target: "0.9.46"
implementedin: "0.9.46"
toc: true
---
## Hinweis
Netzwerkbereitstellung und Tests laufen.
Kann geringfügigen Änderungen unterliegen.
Siehe [SPEC](/docs/specs/ecies/) für die offizielle Spezifikation.

Die folgenden Funktionen sind ab Version 0.9.46 noch nicht implementiert:

- MessageNumbers-, Options- und Termination-Blöcke
- Protokollschicht-Antworten
- Null-Static-Key
- Multicast


## Übersicht

Dies ist ein Vorschlag für den ersten neuen Ende-zu-Ende-Verschlüsselungstyp
seit Beginn von I2P, um ElGamal/AES+SessionTags [Elg-AES](/docs/specs/elgamal-aes/) zu ersetzen.

Er baut auf vorheriger Arbeit auf wie folgt:

- Gemeinsame Strukturen Spezifikation [Common Structures](/docs/specs/common-structures/)
- [I2NP](/docs/specs/i2np/) Spezifikation inklusive LS2
- ElGamal/AES+Session Tags [Elg-AES](/docs/specs/elgamal-aes/)
- [http://zzz.i2p/topics/1768](http://zzz.i2p/topics/1768) Übersicht über neue asymmetrische Kryptografie
- Übersicht über Low-Level-Kryptografie [CRYPTO-ELG](/docs/specs/cryptography/)
- ECIES [http://zzz.i2p/topics/2418](http://zzz.i2p/topics/2418)
- [NTCP2](/docs/specs/ntcp2/) [Proposal 111](/proposals/111-ntcp-2/)
- 123 Neue netDB-Einträge
- 142 Neues Krypto-Template
- [Noise](https://noiseprotocol.org/noise.html) Protokoll
- [Signal](https://signal.org/docs/) Double-Ratchet-Algorithmus

Ziel ist es, neue Verschlüsselung für Ende-zu-Ende-Kommunikation
von Ziel zu Ziel zu unterstützen.

Das Design verwendet einen Noise-Handshake und eine Datenphase, die den Double-Ratchet von Signal integriert.

Alle Referenzen auf Signal und Noise in diesem Vorschlag dienen nur als Hintergrundinformation.
Kenntnis der Signal- und Noise-Protokolle ist nicht erforderlich, um
diesen Vorschlag zu verstehen oder zu implementieren.


### Aktuelle ElGamal-Nutzung

Zur Erinnerung:
ElGamal 256-Byte öffentliche Schlüssel finden sich in folgenden Datenstrukturen.
Siehe die Spezifikation für gemeinsame Strukturen.

- In einer Router-Identität
  Dies ist der Verschlüsselungsschlüssel des Routers.

- In einem Ziel
  Der öffentliche Schlüssel des Ziels wurde für die alte i2cp-to-i2cp-Verschlüsselung verwendet,
  die in Version 0.6 deaktiviert wurde; er ist derzeit ungenutzt, außer für
  den IV zur LeaseSet-Verschlüsselung, was veraltet ist.
  Stattdessen wird der öffentliche Schlüssel im LeaseSet verwendet.

- In einem LeaseSet
  Dies ist der Verschlüsselungsschlüssel des Ziels.

- In einem LS2
  Dies ist der Verschlüsselungsschlüssel des Ziels.



### EncTypes in Key Certs

Zur Erinnerung:
Wir fügten Unterstützung für Verschlüsselungstypen hinzu, als wir Unterstützung für Signaturtypen hinzufügten.
Das Feld für den Verschlüsselungstyp ist immer Null, sowohl in Zielen als auch in Router-Identitäten.
Ob dies jemals geändert werden soll, steht noch aus.
Siehe die Spezifikation für gemeinsame Strukturen [Common Structures](/docs/specs/common-structures/).




### Asymmetrische Krypto-Nutzung

Zur Erinnerung verwenden wir ElGamal für:

1) Tunnel-Build-Nachrichten (Schlüssel ist in RouterIdentity)
   Ersatz ist in diesem Vorschlag nicht enthalten.
   Siehe Vorschlag 152 [Proposal 152](/proposals/152-ecies-tunnels).

2) Router-zu-Router-Verschlüsselung von netdb und anderen I2NP-Nachrichten (Schlüssel ist in RouterIdentity)
   Hängt von diesem Vorschlag ab.
   Erfordert einen Vorschlag für 1) oder das Eintragen des Schlüssels in die RI-Optionen.

3) Client Ende-zu-Ende ElGamal+AES/SessionTag (Schlüssel ist im LeaseSet, der Zielschlüssel ist ungenutzt)
   Ersatz IST in diesem Vorschlag enthalten.

4) Ephemeres DH für NTCP1 und SSU
   Ersatz ist in diesem Vorschlag nicht enthalten.
   Siehe Vorschlag 111 für NTCP2.
   Kein aktueller Vorschlag für SSU2.


### Ziele

- Rückwärtskompatibel
- Erfordert und baut auf LS2 (Vorschlag 123) auf
- Nutzt neue Kryptografie oder Primitive, die für NTCP2 (Vorschlag 111) hinzugefügt wurden
- Keine neuen Kryptografie oder Primitive erforderlich
- Beibehaltung der Entkopplung von Kryptografie und Signatur; Unterstützung aller aktuellen und zukünftigen Versionen
- Aktivierung neuer Kryptografie für Ziele
- Aktivierung neuer Kryptografie für Router, aber nur für Garlic-Nachrichten – Tunnel-Building wäre
  ein separater Vorschlag
- Nichts brechen, das auf 32-Byte binären Ziel-Hashes basiert, z.B. BitTorrent
- Beibehaltung der 0-RTT-Nachrichtenübermittlung mittels ephemeral-static DH
- Kein Puffern/Warten von Nachrichten auf dieser Protokollschicht erforderlich;
  weiterhin uneingeschränkte Nachrichtenübermittlung in beide Richtungen ohne Warten auf Antwort
- Upgrade auf ephemeral-ephemeral DH nach 1 RTT
- Beibehaltung der Verarbeitung von Nachrichten in falscher Reihenfolge
- Beibehaltung der 256-Bit-Sicherheit
- Hinzufügen von Vorwärtsgeheimhaltung
- Hinzufügen von Authentifizierung (AEAD)
- Deutlich CPU-effizienter als ElGamal
- Nicht auf Java jbigi angewiesen, um DH effizient zu machen
- Minimierung der DH-Operationen
- Deutlich bandbreiteneffizienter als ElGamal (514-Byte ElGamal-Block)
- Unterstützung von neuer und alter Kryptografie im selben Tunnel, falls gewünscht
- Empfänger kann effizient neue von alter Kryptografie unterscheiden, die im selben Tunnel ankommt
- Andere können neue von alter oder zukünftiger Kryptografie nicht unterscheiden
- Beseitigung der Unterscheidung zwischen neuer und bestehender Session-Länge (Unterstützung von Padding)
- Keine neuen I2NP-Nachrichten erforderlich
- Ersetzung der SHA-256-Prüfsumme im AES-Payload durch AEAD
- Unterstützung der Bindung von Senden- und Empfangssessions, sodass
  Bestätigungen innerhalb des Protokolls erfolgen können, nicht nur out-of-band.
  Dies ermöglicht auch, dass Antworten sofort Vorwärtsgeheimhaltung haben.
- Aktivierung der Ende-zu-Ende-Verschlüsselung bestimmter Nachrichten (RouterInfo-Speicher),
  die wir derzeit aufgrund der CPU-Last nicht verwenden.
- Keine Änderung der I2NP Garlic Message
  oder des Garlic Message Delivery Instructions-Formats.
- Beseitigung ungenutzter oder redundanter Felder in den Garlic Clove Set- und Clove-Formaten.

Beseitigung mehrerer Probleme mit Session-Tags, einschließlich:

- Unfähigkeit, AES zu verwenden, bis die erste Antwort eintrifft
- Unzuverlässigkeit und Staus, wenn Tag-Übermittlung angenommen wird
- Bandbreitenineffizienz, besonders bei erster Übermittlung
- Enorme Speicherineffizienz zum Speichern von Tags
- Enorme Bandbreitenbelastung zur Übermittlung von Tags
- Hochkomplex, schwer zu implementieren
- Schwierig zu optimieren für verschiedene Anwendungsfälle
  (Streaming vs. Datagramme, Server vs. Client, hohe vs. niedrige Bandbreite)
- Speichererschöpfungsanfälligkeiten durch Tag-Übermittlung


### Nicht-Ziele / Außerhalb des Rahmens

- Änderungen am LS2-Format (Vorschlag 123 ist abgeschlossen)
- Neuer DHT-Rotationsalgorithmus oder gemeinsame Zufallszahlengenerierung
- Neue Verschlüsselung für Tunnel-Building.
  Siehe Vorschlag 152 [Proposal 152](/proposals/152-ecies-tunnels).
- Neue Verschlüsselung für die Tunnel-Schichtverschlüsselung.
  Siehe Vorschlag 153 [Proposal 153](/proposals/153-chacha20-layer-encryption).
- Methoden der Verschlüsselung, Übertragung und Empfang von I2NP DLM / DSM / DSRM-Nachrichten.
  Wird nicht geändert.
- Keine LS1-zu-LS2- oder ElGamal/AES-zu-diesem-Vorschlag-Kommunikation wird unterstützt.
  Dieser Vorschlag ist ein bidirektionales Protokoll.
  Ziele können Rückwärtskompatibilität durch Veröffentlichung zweier Leasesets
  mit denselben Tunneln bewältigen oder beide Verschlüsselungstypen im LS2 platzieren.
- Änderungen am Bedrohungsmodell
- Implementierungsdetails werden hier nicht diskutiert und bleiben jedem Projekt überlassen.
- (Optimistisch) Hinzufügen von Erweiterungen oder Hooks zur Unterstützung von Multicast



### Begründung

ElGamal/AES+SessionTag war über etwa 15 Jahre unser einziges Ende-zu-Ende-Protokoll,
im Wesentlichen ohne Änderungen am Protokoll.
Es gibt nun kryptografische Primitive, die schneller sind.
Wir müssen die Sicherheit des Protokolls verbessern.
Wir haben auch heuristische Strategien und Workarounds entwickelt, um den
Speicher- und Bandbreitenbedarf des Protokolls zu minimieren, aber diese Strategien
sind fragil, schwer zu optimieren und machen das Protokoll noch anfälliger
für Fehler, was zum Abbruch der Sitzung führt.

Über denselben Zeitraum hat die ElGamal/AES+SessionTag-Spezifikation und verwandte
Dokumentation beschrieben, wie bandbreitenintensiv die Übermittlung von Session-Tags ist,
und vorgeschlagen, die Übermittlung von Session-Tags durch einen "synchronisierten PRNG" zu ersetzen.
Ein synchronisierter PRNG generiert deterministisch dieselben Tags an beiden Enden,
abgeleitet von einem gemeinsamen Seed.
Ein synchronisierter PRNG kann auch als "Ratchet" bezeichnet werden.
Dieser Vorschlag (endlich) spezifiziert diesen Ratchet-Mechanismus und beseitigt die Tag-Übermittlung.

Durch die Verwendung eines Ratchet (eines synchronisierten PRNG) zur Generierung der
Session-Tags wird der Overhead der Übermittlung von Session-Tags
in der New-Session-Nachricht und nachfolgenden Nachrichten beseitigt.
Für einen typischen Tag-Satz von 32 Tags sind das 1 KB.
Dies beseitigt auch die Speicherung von Session-Tags auf der Senderseite,
wodurch die Speicheranforderungen halbiert werden.

Ein vollständiger bidirektionaler Handshake, ähnlich dem Noise-IK-Muster, ist erforderlich, um Key Compromise Impersonation (KCI)-Angriffe zu vermeiden.
Siehe die Noise "Payload Security Properties"-Tabelle in [NOISE](https://noiseprotocol.org/noise.html).
Weitere Informationen zu KCI finden Sie im Paper https://www.usenix.org/system/files/conference/woot15/woot15-paper-hlauschek.pdf



### Bedrohungsmodell

Das Bedrohungsmodell unterscheidet sich etwas von NTCP2 (Vorschlag 111).
Die MitM-Knoten sind die OBEP und IBGW und werden davon ausgegangen, dass sie volle Sicht auf
die aktuelle oder historische globale NetDB haben, durch Zusammenarbeit mit Floodfills.

Ziel ist es, diese MitMs daran zu hindern, Datenverkehr als
neue und bestehende Session-Nachrichten oder als neue vs. alte Kryptografie zu klassifizieren.



## Detaillierter Vorschlag

Dieser Vorschlag definiert ein neues Ende-zu-Ende-Protokoll zur Ersetzung von ElGamal/AES+SessionTags.
Das Design verwendet einen Noise-Handshake und eine Datenphase, die den Double-Ratchet von Signal integriert.


### Zusammenfassung des kryptografischen Designs

Es gibt fünf Teile des Protokolls, die neu gestaltet werden müssen:


- 1) Die neuen und bestehenden Session-Containerformate
  werden durch neue Formate ersetzt.
- 2) ElGamal (256-Byte öffentliche Schlüssel, 128-Byte private Schlüssel) wird ersetzt durch
  ECIES-X25519 (32-Byte öffentliche und private Schlüssel)
- 3) AES wird ersetzt durch
  AEAD_ChaCha20_Poly1305 (im Folgenden als ChaChaPoly abgekürzt)
- 4) SessionTags werden ersetzt durch Ratchets,
  was im Wesentlichen ein kryptografischer, synchronisierter PRNG ist.
- 5) Der AES-Payload, wie in der ElGamal/AES+SessionTags-Spezifikation definiert,
  wird durch ein Blockformat ersetzt, ähnlich dem in NTCP2.

Jede der fünf Änderungen hat ihren eigenen Abschnitt unten.


### Neue kryptografische Primitive für I2P

Bestehende I2P-Router-Implementierungen erfordern Implementierungen für
die folgenden Standardkryptografie-Primitive,
die für aktuelle I2P-Protokolle nicht erforderlich sind:

- ECIES (aber dies ist im Wesentlichen X25519)
- Elligator2

Bestehende I2P-Router-Implementierungen, die [NTCP2](/docs/specs/ntcp2/) ([Proposal 111](/proposals/111-ntcp-2/))
noch nicht implementiert haben, erfordern ebenfalls Implementierungen für:

- X25519 Schlüsselgenerierung und DH
- AEAD_ChaCha20_Poly1305 (im Folgenden als ChaChaPoly abgekürzt)
- HKDF


### Krypto-Typ

Der Krypto-Typ (verwendet im LS2) ist 4.
Dies zeigt einen little-endian 32-Byte X25519 öffentlichen Schlüssel an
und das hier spezifizierte Ende-zu-Ende-Protokoll.

Krypto-Typ 0 ist ElGamal.
Krypto-Typen 1-3 sind reserviert für ECIES-ECDH-AES-SessionTag, siehe Vorschlag 145 [Proposal 145](/proposals/145-ecies).


### Noise-Protokoll-Framework

Dieser Vorschlag stellt die Anforderungen basierend auf dem Noise-Protokoll-Framework bereit
[NOISE](https://noiseprotocol.org/noise.html) (Revision 34, 2018-07-11).
Noise hat ähnliche Eigenschaften wie das Station-To-Station-Protokoll
[STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol), das die Grundlage für das [SSU](/docs/legacy/ssu/) Protokoll bildet. In Noise-Jargon ist Alice
der Initiator und Bob der Responder.

Dieser Vorschlag basiert auf dem Noise-Protokoll Noise_IK_25519_ChaChaPoly_SHA256.
(Die eigentliche Kennung für die anfängliche Schlüsselableitungsfunktion
ist "Noise_IKelg2_25519_ChaChaPoly_SHA256",
um I2P-Erweiterungen anzuzeigen – siehe Abschnitt KDF 1 unten)
Dieses Noise-Protokoll verwendet die folgenden Primitive:

- Interaktives Handshake-Muster: IK
  Alice sendet sofort ihren statischen Schlüssel an Bob (I)
  Alice kennt bereits Bobs statischen Schlüssel (K)

- Einweg-Handshake-Muster: N
  Alice sendet ihren statischen Schlüssel nicht an Bob (N)

- DH-Funktion: X25519
  X25519 DH mit einer Schlüssellänge von 32 Bytes, wie in [RFC-7748](https://tools.ietf.org/html/rfc7748) spezifiziert.

- Chiffrierfunktion: ChaChaPoly
  AEAD_CHACHA20_POLY1305 wie in [RFC-7539](https://tools.ietf.org/html/rfc7539) Abschnitt 2.8 spezifiziert.
  12-Byte Nonce, wobei die ersten 4 Bytes auf Null gesetzt sind.
  Identisch zu dem in [NTCP2](/docs/specs/ntcp2/).

- Hash-Funktion: SHA256
  Standard 32-Byte Hash, bereits umfassend in I2P verwendet.


### Erweiterungen zum Framework

Dieser Vorschlag definiert die folgenden Verbesserungen zu
Noise_IK_25519_ChaChaPoly_SHA256. Diese folgen im Allgemeinen den Richtlinien in
[NOISE](https://noiseprotocol.org/noise.html) Abschnitt 13.

1) Klartext-ephemere Schlüssel werden mit [Elligator2](https://elligator.cr.yp.to/) kodiert.

2) Die Antwort wird mit einem Klartext-Tag präfixiert.

3) Das Payload-Format ist für Nachrichten 1, 2 und die Datenphase definiert.
   Natürlich ist dies in Noise nicht definiert.

Alle Nachrichten enthalten einen [I2NP](/docs/specs/i2np/) Garlic Message-Header.
Die Datenphase verwendet eine Verschlüsselung, die der von Noise ähnelt, aber nicht kompatibel ist.


### Handshake-Muster

Handshakes verwenden [Noise](https://noiseprotocol.org/noise.html) Handshake-Muster.

Die folgende Buchstabenzuordnung wird verwendet:

- e = einmaliger ephemeraler Schlüssel
- s = statischer Schlüssel
- p = Nachrichten-Payload

Einmalige und ungebundene Sitzungen ähneln dem Noise-N-Muster.

```

<- s
  ...
  e es p ->

```

Gebundene Sitzungen ähneln dem Noise-IK-Muster.

```

<- s
  ...
  e es s ss p ->
  <- tag e ee se
  <- p
  p ->

```


### Sitzungen

Das aktuelle ElGamal/AES+SessionTag-Protokoll ist unidirektional.
Auf dieser Ebene weiß der Empfänger nicht, woher eine Nachricht stammt.
Ausgehende und eingehende Sitzungen sind nicht assoziiert.
Bestätigungen erfolgen out-of-band über eine DeliveryStatusMessage
(gepackt in eine GarlicMessage) im Clove.

Es gibt erhebliche Ineffizienz in einem unidirektionalen Protokoll.
Jede Antwort muss ebenfalls eine teure 'New Session'-Nachricht verwenden.
Dies verursacht höhere Bandbreite-, CPU- und Speichernutzung.

Es gibt auch Sicherheitsschwächen in einem unidirektionalen Protokoll.
Alle Sitzungen basieren auf ephemeral-static DH.
Ohne Rückweg kann Bob seinen statischen Schlüssel nicht auf einen ephemeralen Schlüssel "ratcheten".
Ohne zu wissen, woher eine Nachricht stammt, kann der empfangene ephemere Schlüssel nicht für ausgehende Nachrichten verwendet werden,
daher verwendet auch die anfängliche Antwort ephemeral-static DH.

Für diesen Vorschlag definieren wir zwei Mechanismen, um ein bidirektionales Protokoll zu erstellen –
"Paarung" und "Bindung".
Diese Mechanismen bieten erhöhte Effizienz und Sicherheit.


### Sitzungskontext

Wie bei ElGamal/AES+SessionTags müssen alle eingehenden und ausgehenden Sitzungen
in einem bestimmten Kontext erfolgen, entweder im Router-Kontext oder
im Kontext für ein bestimmtes lokales Ziel.
In Java I2P wird dieser Kontext Session Key Manager genannt.

Sitzungen dürfen nicht zwischen Kontexten geteilt werden, da dies
eine Korrelation zwischen den verschiedenen lokalen Zielen ermöglichen würde,
oder zwischen einem lokalen Ziel und einem Router.

Wenn ein bestimmtes Ziel sowohl ElGamal/AES+SessionTags
als auch diesen Vorschlag unterstützt, können beide Sitzungstypen einen Kontext teilen.
Siehe Abschnitt 1c) unten.



### Paarung von eingehenden und ausgehenden Sitzungen

Wenn eine ausgehende Sitzung beim Initiator (Alice) erstellt wird,
wird eine neue eingehende Sitzung erstellt und mit der ausgehenden Sitzung gepaart,
es sei denn, keine Antwort wird erwartet (z.B. rohe Datagramme).

Eine neue eingehende Sitzung wird immer mit einer neuen ausgehenden Sitzung gepaart,
es sei denn, keine Antwort wird angefordert (z.B. rohe Datagramme).

Wenn eine Antwort angefordert und an ein fernes Ziel oder einen Router gebunden ist,
wird diese neue ausgehende Sitzung an dieses Ziel oder diesen Router gebunden
und ersetzt jede vorherige ausgehende Sitzung zu diesem Ziel oder Router.

Durch die Paarung von eingehenden und ausgehenden Sitzungen wird ein bidirektionales Protokoll
mit der Fähigkeit zum Ratcheten der DH-Schlüssel bereitgestellt.



### Bindung von Sitzungen und Zielen

Es gibt nur eine ausgehende Sitzung zu einem bestimmten Ziel oder Router.
Es kann mehrere aktuelle eingehende Sitzungen von einem bestimmten Ziel oder Router geben.
Im Allgemeinen, wenn eine neue eingehende Sitzung erstellt wird und Datenverkehr auf dieser Sitzung empfangen wird
(was als ACK dient), werden alle anderen relativ schnell zum Ablaufen markiert, innerhalb einer Minute oder so.
Der vorherige gesendete (PN)-Wert wird überprüft, und wenn keine
nicht empfangenen Nachrichten (innerhalb der Fenstergröße) in der vorherigen eingehenden Sitzung vorhanden sind,
kann die vorherige Sitzung sofort gelöscht werden.


Wenn eine ausgehende Sitzung beim Initiator (Alice) erstellt wird,
wird sie an das fernes Ziel (Bob) gebunden,
und jede gepaarte eingehende Sitzung wird ebenfalls an das fernes Ziel gebunden.
Während die Sitzungen ratcheten, bleiben sie an das fernes Ziel gebunden.

Wenn eine eingehende Sitzung beim Empfänger (Bob) erstellt wird,
kann sie an das fernes Ziel (Alice) gebunden werden, nach Alices Wahl.
Wenn Alice Bindungsinformationen (ihren statischen Schlüssel) in die New-Session-Nachricht einfügt,
wird die Sitzung an dieses Ziel gebunden,
und eine ausgehende Sitzung wird erstellt und an dasselbe Ziel gebunden.
Während die Sitzungen ratcheten, bleiben sie an das fernes Ziel gebunden.


### Vorteile von Bindung und Paarung

Für den üblichen Streaming-Fall erwarten wir, dass Alice und Bob das Protokoll wie folgt verwenden:

- Alice paart ihre neue ausgehende Sitzung mit einer neuen eingehenden Sitzung, beide an das fernes Ziel (Bob) gebunden.
- Alice fügt die Bindungsinformationen und Signatur sowie eine Antwortanfrage in die
  New-Session-Nachricht ein, die an Bob gesendet wird.
- Bob paart seine neue eingehende Sitzung mit einer neuen ausgehenden Sitzung, beide an das fernes Ziel (Alice) gebunden.
- Bob sendet eine Antwort (Ack) an Alice in der gepaarten Sitzung, mit einem Ratchet auf einen neuen DH-Schlüssel.
- Alice ratcheted auf eine neue ausgehende Sitzung mit Bobs neuem Schlüssel, gepaart mit der bestehenden eingehenden Sitzung.

Durch die Bindung einer eingehenden Sitzung an ein fernes Ziel und die Paarung der eingehenden Sitzung
mit einer ausgehenden Sitzung, die an dasselbe Ziel gebunden ist, erreichen wir zwei große Vorteile:

1) Die anfängliche Antwort von Bob an Alice verwendet ephemeral-ephemeral DH

2) Nachdem Alice Bobs Antwort empfangen und geratcheted hat, verwenden alle nachfolgenden Nachrichten von Alice an Bob
ephemeral-ephemeral DH.


### Nachrichten-ACKs

In ElGamal/AES+SessionTags, wenn ein LeaseSet als Garlic-Clove gebündelt wird,
oder Tags übermittelt werden, fordert der sendende Router ein ACK an.
Dies ist ein separater Garlic-Clove, der eine DeliveryStatus-Nachricht enthält.
Zusätzliche Sicherheit bietet die Verpackung der DeliveryStatus-Nachricht in eine Garlic-Nachricht.
Dieser Mechanismus ist aus Sicht des Protokolls out-of-band.

Im neuen Protokoll, da eingehende und ausgehende Sitzungen gepaart sind,
können wir ACKs in-band haben. Kein separater Clove ist erforderlich.

Ein explizites ACK ist einfach eine Existing-Session-Nachricht ohne I2NP-Block.
Allerdings kann in den meisten Fällen ein explizites ACK vermieden werden, da Rückverkehr vorhanden ist.
Es kann wünschenswert sein, dass Implementierungen eine kurze Zeit (vielleicht hundert ms)
warten, bevor ein explizites ACK gesendet wird, um der Streaming- oder Anwendungsschicht Zeit zur Antwort zu geben.

Implementierungen müssen auch das Senden von ACKs verzögern, bis nach der
Verarbeitung des I2NP-Blocks, da die Garlic-Nachricht eine Database-Store-Nachricht
mit einem LeaseSet enthalten kann. Ein aktuelles LeaseSet wird benötigt, um das ACK zu routen,
und das fernes Ziel (enthalten im LeaseSet) wird benötigt, um
den Bindungs-Static-Key zu verifizieren.


### Sitzungs-Timeouts

Ausgehende Sitzungen sollten immer vor eingehenden Sitzungen ablaufen.
Sobald eine ausgehende Sitzung abläuft und eine neue erstellt wird, wird auch eine neue gepaarte eingehende
Sitzung erstellt. Wenn eine alte eingehende Sitzung vorhanden war,
wird ihr Ablauf zugelassen.


### Multicast

TBD


### Definitionen
Wir definieren die folgenden Funktionen, die den verwendeten kryptografischen Bausteinen entsprechen.

ZEROLEN
    Null-Länge-Byte-Array

CSRNG(n)
    n-Byte-Ausgabe aus einem kryptografisch sicheren Zufallszahlengenerator.

H(p, d)
    SHA-256-Hash-Funktion, die eine Personalisierungszeichenkette p und Daten d nimmt und
    eine Ausgabe der Länge 32 Bytes erzeugt.
    Wie in [NOISE](https://noiseprotocol.org/noise.html) definiert.
    || unten bedeutet Anhängen.

    Verwenden Sie SHA-256 wie folgt::

        H(p, d) := SHA-256(p || d)

MixHash(d)
    SHA-256-Hash-Funktion, die einen vorherigen Hash h und neue Daten d nimmt,
    und eine Ausgabe der Länge 32 Bytes erzeugt.
    || unten bedeutet Anhängen.

    Verwenden Sie SHA-256 wie folgt::

        MixHash(d) := h = SHA-256(h || d)

STREAM
    Das ChaCha20/Poly1305 AEAD wie in [RFC-7539](https://tools.ietf.org/html/rfc7539) spezifiziert.
    S_KEY_LEN = 32 und S_IV_LEN = 12.

    ENCRYPT(k, n, plaintext, ad)
        Verschlüsselt plaintext mit dem Chiffrierschlüssel k und Nonce n, der für
        den Schlüssel k eindeutig sein muss.
        Assoziierte Daten ad sind optional.
        Gibt einen Ciphertext zurück, der die Größe des Plaintexts + 16 Bytes für den HMAC hat.

        Der gesamte Ciphertext muss von Zufallsdaten ununterscheidbar sein, wenn der Schlüssel geheim ist.

    DECRYPT(k, n, ciphertext, ad)
        Entschlüsselt ciphertext mit dem Chiffrierschlüssel k und Nonce n.
        Assoziierte Daten ad sind optional.
        Gibt den Plaintext zurück.

DH
    X25519 Public-Key-Agreement-System. Private Schlüssel von 32 Bytes, öffentliche Schlüssel von 32
    Bytes, erzeugt Ausgaben von 32 Bytes. Es hat die folgenden
    Funktionen:

    GENERATE_PRIVATE()
        Generiert einen neuen privaten Schlüssel.

    DERIVE_PUBLIC(privkey)
        Gibt den öffentlichen Schlüssel zurück, der zum gegebenen privaten Schlüssel gehört.

    GENERATE_PRIVATE_ELG2()
        Generiert einen neuen privaten Schlüssel, der zu einem öffentlichen Schlüssel passt, der für die Elligator2-Kodierung geeignet ist.
        Beachten Sie, dass die Hälfte der zufällig generierten privaten Schlüssel nicht geeignet ist und verworfen werden muss.

    ENCODE_ELG2(pubkey)
        Gibt den Elligator2-kodierten öffentlichen Schlüssel zurück, der zum gegebenen öffentlichen Schlüssel gehört (inverse Abbildung).
        Kodierte Schlüssel sind little-endian.
        Kodierter Schlüssel muss 256 Bit sein, ununterscheidbar von zufälligen Daten.
        Siehe Elligator2-Abschnitt unten für Spezifikation.

    DECODE_ELG2(pubkey)
        Gibt den öffentlichen Schlüssel zurück, der zum gegebenen Elligator2-kodierten öffentlichen Schlüssel gehört.
        Siehe Elligator2-Abschnitt unten für Spezifikation.

    DH(privkey, pubkey)
        Generiert einen gemeinsamen geheimen Schlüssel aus den gegebenen privaten und öffentlichen Schlüsseln.

HKDF(salt, ikm, info, n)
    Eine kryptografische Schlüsselableitungsfunktion, die einige Eingabeschlüsselmaterial ikm (das
    gute Entropie haben sollte, aber nicht erforderlich ist, eine gleichmäßig zufällige Zeichenkette zu sein), ein Salz
    der Länge 32 Bytes und einen kontextspezifischen 'info'-Wert nimmt und eine Ausgabe
    von n Bytes erzeugt, geeignet als Schlüsselmaterial.

    Verwenden Sie HKDF wie in [RFC-5869](https://tools.ietf.org/html/rfc5869) spezifiziert, unter Verwendung der HMAC-Hash-Funktion SHA-256
    wie in [RFC-2104](https://tools.ietf.org/html/rfc2104) spezifiziert. Dies bedeutet, dass SALT_LEN maximal 32 Bytes ist.

MixKey(d)
    Verwendet HKDF() mit einem vorherigen chainKey und neuen Daten d und
    setzt den neuen chainKey und k.
    Wie in [NOISE](https://noiseprotocol.org/noise.html) definiert.

    Verwenden Sie HKDF wie folgt::

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]



### 1) Nachrichtenformat


### Überprüfung des aktuellen Nachrichtenformats

Die Garlic-Nachricht wie in [I2NP](/docs/specs/i2np/) spezifiziert ist wie folgt.
Da ein Entwurfsziel ist, dass Zwischenhops neue von alter Kryptografie nicht unterscheiden können,
darf dieses Format nicht geändert werden, auch wenn das Längenfeld redundant ist.
Das Format wird mit dem vollen 16-Byte-Header gezeigt, obwohl der
tatsächliche Header je nach Transport verwendetem Format unterschiedlich sein kann.

Nach der Entschlüsselung enthält die Daten eine Reihe von Garlic-Cloves und zusätzlichen
Daten, auch bekannt als Clove-Set.

Siehe [I2NP](/docs/specs/i2np/) für Details und eine vollständige Spezifikation.


```

+----+----+----+----+----+----+----+----+
  |type|      msg_id       |  expiration
  +----+----+----+----+----+----+----+----+
                           |  size   |chks|
  +----+----+----+----+----+----+----+----+
  |      length       |                   |
  +----+----+----+----+                   +
  |          encrypted data               |
  ~                                       ~
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

```


### Überprüfung des verschlüsselten Datenformats

Das aktuelle Nachrichtenformat, das seit über 15 Jahren verwendet wird,
ist ElGamal/AES+SessionTags.
In ElGamal/AES+SessionTags gibt es zwei Nachrichtenformate:

1) Neue Sitzung:
- 514-Byte ElGamal-Block
- AES-Block (mindestens 128 Bytes, Vielfaches von 16)

2) Bestehende Sitzung:
- 32-Byte Session-Tag
- AES-Block (mindestens 128 Bytes, Vielfaches von 16)

Die minimale Auffüllung auf 128 ist wie in Java I2P implementiert, aber nicht bei Empfang erzwungen.

Diese Nachrichten sind in einer I2NP-Garlic-Nachricht verpackt, die
ein Längenfeld enthält, sodass die Länge bekannt ist.

Beachten Sie, dass keine Auffüllung auf eine nicht-mod-16-Länge definiert ist,
daher ist die Neue Sitzung immer (mod 16 == 2),
und eine bestehende Sitzung ist immer (mod 16 == 0).
Wir müssen dies beheben.

Der Empfänger versucht zuerst, die ersten 32 Bytes als Session-Tag nachzuschlagen.
Wenn gefunden, entschlüsselt er den AES-Block.
Wenn nicht gefunden und die Daten mindestens (514+16) lang sind, versucht er, den ElGamal-Block zu entschlüsseln,
und wenn erfolgreich, entschlüsselt er den AES-Block.


### Neue Session-Tags und Vergleich mit Signal

In Signal Double Ratchet enthält der Header:

- DH: Aktueller Ratchet-öffentlicher Schlüssel
- PN: Vorherige Kettennachrichtenlänge
- N: Nachrichtennummer

Signals "sending chains" sind grob äquivalent zu unseren Tag-Sets.
Durch die Verwendung eines Session-Tags können wir das meiste davon eliminieren.

In New Session setzen wir nur den öffentlichen Schlüssel in den unverschlüsselten Header.

In Existing Session verwenden wir ein Session-Tag für den Header.
Das Session-Tag ist mit dem aktuellen Ratchet-öffentlichen Schlüssel
und der Nachrichtennummer assoziiert.

In beiden neuen und bestehenden Sitzungen sind PN und N im verschlüsselten Körper.

In Signal ratcheten Dinge ständig. Ein neuer DH-öffentlicher Schlüssel erfordert, dass der
Empfänger ratcheted und einen neuen öffentlichen Schlüssel zurücksendet, was auch als
Ack für den empfangenen öffentlichen Schlüssel dient.
Das wäre für uns viel zu viele DH-Operationen.
Daher trennen wir das Ack des empfangenen Schlüssels und die Übertragung eines neuen öffentlichen Schlüssels.
Jede Nachricht, die ein Session-Tag verwendet, das aus dem neuen DH-öffentlichen Schlüssel generiert wurde, stellt ein ACK dar.
Wir übertragen nur einen neuen öffentlichen Schlüssel, wenn wir neu schlüsseln möchten.

Die maximale Anzahl von Nachrichten, bevor DH ratcheten muss, ist 65535.

Beim Liefern eines Sitzungsschlüssels leiten wir das "Tag Set" davon ab,
anstatt zusätzlich Session-Tags liefern zu müssen.
Ein Tag Set kann bis zu 65536 Tags haben.
Allerdings sollten Empfänger eine "Look-ahead"-Strategie implementieren,
anstatt alle möglichen Tags auf einmal zu generieren.
Generieren Sie höchstens N Tags nach dem letzten guten empfangenen Tag.
N könnte höchstens 128 sein, aber 32 oder sogar weniger könnte eine bessere Wahl sein.



### 1a) Neues Sitzungsformat

Neue Sitzung Einmaliger öffentlicher Schlüssel (32 Bytes)
Verschlüsselte Daten und MAC (verbleibende Bytes)

Die New-Session-Nachricht kann den statischen öffentlichen Schlüssel des Senders enthalten oder nicht.
Wenn er enthalten ist, ist die Rückwärts-Sitzung an diesen Schlüssel gebunden.
Der statische Schlüssel sollte enthalten sein, wenn Antworten erwartet werden,
d.h. für Streaming und replizierbare Datagramme.
Er sollte nicht für rohe Datagramme enthalten sein.

Die New-Session-Nachricht ähnelt dem einwegigen Noise [NOISE](https://noiseprotocol.org/noise.html) Muster
"N" (wenn der statische Schlüssel nicht gesendet wird),
oder dem zweiwegigen Muster "IK" (wenn der statische Schlüssel gesendet wird).



### 1b) Neues Sitzungsformat (mit Bindung)

Länge ist 96 + Payload-Länge.
Verschlüsseltes Format:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   New Session Ephemeral Public Key    |
  +             32 bytes                  +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +         Static Key                    +
  |       ChaCha20 encrypted data         |
  +            32 bytes                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +    (MAC) for Static Key Section       +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Public Key :: 32 bytes, little endian, Elligator2, cleartext

  Static Key encrypted data :: 32 bytes

  Payload Section encrypted data :: remaining data minus 16 bytes

  MAC :: Poly1305 message authentication code, 16 bytes

```


### Neuer Sitzungs-ephemeraler Schlüssel

Der ephemere Schlüssel ist 32 Bytes, mit Elligator2 kodiert.
Dieser Schlüssel wird niemals wiederverwendet; ein neuer Schlüssel wird mit
jeder Nachricht generiert, einschließlich Wiederholungen.

### Statischer Schlüssel

Nach der Entschlüsselung Alices X25519 statischer Schlüssel, 32 Bytes.


### Payload

Verschlüsselte Länge ist der Rest der Daten.
Entschlüsselte Länge ist 16 weniger als die verschlüsselte Länge.
Payload muss einen DateTime-Block enthalten und enthält in der Regel einen oder mehrere Garlic-Clove-Blöcke.
Siehe den Payload-Abschnitt unten für Format und zusätzliche Anforderungen.



### 1c) Neues Sitzungsformat (ohne Bindung)

Wenn keine Antwort erforderlich ist, wird kein statischer Schlüssel gesendet.


Länge ist 96 + Payload-Länge.
Verschlüsseltes Format:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   New Session Ephemeral Public Key    |
  +             32 bytes                  +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Flags Section               +
  |       ChaCha20 encrypted data         |
  +            32 bytes                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for above section       +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Public Key :: 32 bytes, little endian, Elligator2, cleartext

  Flags Section encrypted data :: 32 bytes

  Payload Section encrypted data :: remaining data minus 16 bytes

  MAC :: Poly1305 message authentication code, 16 bytes

```

### Neuer Sitzungs-ephemeraler Schlüssel

Alices ephemeraler Schlüssel.
Der ephemere Schlüssel ist 32 Bytes, mit Elligator2 kodiert, little-endian.
Dieser Schlüssel wird niemals wiederverwendet; ein neuer Schlüssel wird mit
jeder Nachricht generiert, einschließlich Wiederholungen.


### Flags Section entschlüsselte Daten

Der Flags-Abschnitt enthält nichts.
Er ist immer 32 Bytes lang, da er dieselbe Länge
wie der statische Schlüssel für New-Session-Nachrichten mit Bindung haben muss.
Bob bestimmt, ob es sich um einen statischen Schlüssel oder einen Flags-Abschnitt handelt,
indem er prüft, ob die 32 Bytes alle Null sind.

TODO irgendwelche Flags hier erforderlich?

### Payload

Verschlüsselte Länge ist der Rest der Daten.
Entschlüsselte Länge ist 16 weniger als die verschlüsselte Länge.
Payload muss einen DateTime-Block enthalten und enthält in der Regel einen oder mehrere Garlic-Clove-Blöcke.
Siehe den Payload-Abschnitt unten für Format und zusätzliche Anforderungen.




### 1d) Einmaliges Format (keine Bindung oder Sitzung)

Wenn nur eine einzelne Nachricht gesendet werden soll,
ist kein Sitzungsaufbau oder statischer Schlüssel erforderlich.


Länge ist 96 + Payload-Länge.
Verschlüsseltes Format:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |       Ephemeral Public Key            |
  +             32 bytes                  +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Flags Section               +
  |       ChaCha20 encrypted data         |
  +            32 bytes                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for above section       +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Public Key :: 32 bytes, little endian, Elligator2, cleartext

  Flags Section encrypted data :: 32 bytes

  Payload Section encrypted data :: remaining data minus 16 bytes

  MAC :: Poly1305 message authentication code, 16 bytes

```


### Neuer Sitzungs-Einmal-Schlüssel

Der Einmal-Schlüssel ist 32 Bytes, mit Elligator2 kodiert, little-endian.
Dieser Schlüssel wird niemals wiederverwendet; ein neuer Schlüssel wird mit
jeder Nachricht generiert, einschließlich Wiederholungen.


### Flags Section entschlüsselte Daten

Der Flags-Abschnitt enthält nichts.
Er ist immer 32 Bytes lang, da er dieselbe Länge
wie der statische Schlüssel für New-Session-Nachrichten mit Bindung haben muss.
Bob bestimmt, ob es sich um einen statischen Schlüssel oder einen Flags-Abschnitt handelt,
indem er prüft, ob die 32 Bytes alle Null sind.

TODO irgendwelche Flags hier erforderlich?

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                                       |
  +             All zeros                 +
  |              32 bytes                 |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+

  zeros:: All zeros, 32 bytes.

```


### Payload

Verschlüsselte Länge ist der Rest der Daten.
Entschlüsselte Länge ist 16 weniger als die verschlüsselte Länge.
Payload muss einen DateTime-Block enthalten und enthält in der Regel einen oder mehrere Garlic-Clove-Blöcke.
Siehe den Payload-Abschnitt unten für Format und zusätzliche Anforderungen.



### 1f) KDFs für New-Session-Nachricht

### KDF für anfänglichen ChainKey

Dies ist standard [NOISE](https://noiseprotocol.org/noise.html) für IK mit einem modifizierten Protokollnamen.
Beachten Sie, dass wir denselben Initialisierer für das IK-Muster (gebundene Sitzungen)
und für das N-Muster (ungebundene Sitzungen) verwenden.

Der Protokollname ist aus zwei Gründen modifiziert.
Erstens, um anzugeben, dass die ephemeren Schlüssel mit Elligator2 kodiert sind,
und zweitens, um anzugeben, dass MixHash() vor der zweiten Nachricht
aufgerufen wird, um den Tag-Wert einzumischen.

```

Dies ist das "e" Nachrichtenmuster:

  // Define protocol_name.
  Set protocol_name = "Noise_IKelg2+hs2_25519_ChaChaPoly_SHA256"
   (40 bytes, US-ASCII encoded, no NULL termination).

  // Define Hash h = 32 bytes
  h = SHA256(protocol_name);

  Define ck = 32 byte chaining key. Copy the h data to ck.
  Set chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // up until here, can all be precalculated by Alice for all outgoing connections

```


### KDF für Flags/Static Key Section verschlüsselte Inhalte

```

Dies ist das "e" Nachrichtenmuster:

  // Bob's X25519 static keys
  // bpk is published in leaseset
  bsk = GENERATE_PRIVATE()
  bpk = DERIVE_PUBLIC(bsk)

  // Bob static public key
  // MixHash(bpk)
  // || below means append
  h = SHA256(h || bpk);

  // up until here, can all be precalculated by Bob for all incoming connections

  // Alice's X25519 ephemeral keys
  aesk = GENERATE_PRIVATE_ELG2()
  aepk = DERIVE_PUBLIC(aesk)

  // Alice ephemeral public key
  // MixHash(aepk)
  // || below means append
  h = SHA256(h || aepk);

  // h is used as the associated data for the AEAD in the New Session Message
  // Retain the Hash h for the New Session Reply KDF
  // eapk is sent in cleartext in the
  // beginning of the New Session message
  elg2_aepk = ENCODE_ELG2(aepk)
  // As decoded by Bob
  aepk = DECODE_ELG2(elg2_aepk)

  End of "e" message pattern.

  This is the "es" message pattern:

  // Noise es
  sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // ChaChaPoly parameters to encrypt/decrypt
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, flags/static key section, ad)

  End of "es" message pattern.

  This is the "s" message pattern:

  // MixHash(ciphertext)
  // Save for Payload section KDF
  h = SHA256(h || ciphertext)

  // Alice's X25519 static keys
  ask = GENERATE_PRIVATE()
  apk = DERIVE_PUBLIC(ask)

  End of "s" message pattern.


```



### KDF für Payload Section (mit Alice statischem Schlüssel)

```

Dies ist das "ss" Nachrichtenmuster:

  // Noise ss
  sharedSecret = DH(ask, bpk) = DH(bsk, apk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // ChaChaPoly parameters to encrypt/decrypt
  // chainKey from Static Key Section
  Set sharedSecret = X25519 DH result
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, payload, ad)

  End of "ss" message pattern.

  // MixHash(ciphertext)
  // Save for New Session Reply KDF
  h = SHA256(h || ciphertext)

```


### KDF für Payload Section (ohne Alice statischen Schlüssel)

Beachten Sie, dass dies ein Noise "N" Muster ist, aber wir verwenden denselben "IK" Initialisierer
wie für gebundene Sitzungen.

New-Session-Nachrichten können nicht identifiziert werden, ob sie Alices statischen Schlüssel enthalten oder nicht,
bis der statische Schlüssel entschlüsselt und überprüft wird, ob er alle Nullen enthält.
Daher muss der Empfänger die "IK"-Zustandsmaschine für alle
New-Session-Nachrichten verwenden.
Wenn der statische Schlüssel alle Nullen ist, muss das "ss"-Nachrichtenmuster übersprungen werden.



```

chainKey = from Flags/Static key section
  k = from Flags/Static key section
  n = 1
  ad = h from Flags/Static key section
  ciphertext = ENCRYPT(k, n, payload, ad)

```



### 1g) New-Session-Reply-Format

Eine oder mehrere New-Session-Replies können als Antwort auf eine einzelne New-Session-Nachricht gesendet werden.
Jede Antwort wird mit einem Tag präfixiert, das aus einem TagSet für die Sitzung generiert wird.

Die New-Session-Reply besteht aus zwei Teilen.
Der erste Teil ist der Abschluss des Noise-IK-Handshakes mit einem präfixierten Tag.
Die Länge des ersten Teils beträgt 56 Bytes.
Der zweite Teil ist die Payload der Datenphase.
Die Länge des zweiten Teils beträgt 16 + Payload-Länge.

Gesamtlänge beträgt 72 + Payload-Länge.
Verschlüsseltes Format:

```

+----+----+----+----+----+----+----+----+
  |       Session Tag   8 bytes           |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Ephemeral Public Key           +
  |                                       |
  +            32 bytes                   +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +  (MAC) for Key Section (no data)      +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Tag :: 8 bytes, cleartext

  Public Key :: 32 bytes, little endian, Elligator2, cleartext

  MAC :: Poly1305 message authentication code, 16 bytes
         Note: The ChaCha20 plaintext data is empty (ZEROLEN)

  Payload Section encrypted data :: remaining data minus 16 bytes

  MAC :: Poly1305 message authentication code, 16 bytes

```

### Session-Tag
Das Tag wird im Session-Tags-KDF generiert, wie in der DH-Initialisierungs-KDF unten initialisiert.
Dies korreliert die Antwort mit der Sitzung.
Der Session-Key aus der DH-Initialisierung wird nicht verwendet.


### New-Session-Reply-ephemeraler Schlüssel

Bobs ephemeraler Schlüssel.
Der ephemere Schlüssel ist 32 Bytes, mit Elligator2 kodiert, little-endian.
Dieser Schlüssel wird niemals wiederverwendet; ein neuer Schlüssel wird mit
jeder Nachricht generiert, einschließlich Wiederholungen.


### Payload
Verschlüsselte Länge ist der Rest der Daten.
Entschlüsselte Länge ist 16 weniger als die verschlüsselte Länge.
Payload enthält in der Regel einen oder mehrere Garlic-Clove-Blöcke.
Siehe den Payload-Abschnitt unten für Format und zusätzliche Anforderungen.


### KDF für Reply-TagSet

Ein oder mehrere Tags werden aus dem TagSet erstellt, das mit
der unten angegebenen KDF initialisiert wird, unter Verwendung des chainKey aus der New-Session-Nachricht.

```

// Generate tagset
  tagsetKey = HKDF(chainKey, ZEROLEN, "SessionReplyTags", 32)
  tagset_nsr = DH_INITIALIZE(chainKey, tagsetKey)

```


### KDF für Reply-Key-Section verschlüsselte Inhalte

```

// Keys from the New Session message
  // Alice's X25519 keys
  // apk and aepk are sent in original New Session message
  // ask = Alice private static key
  // apk = Alice public static key
  // aesk = Alice ephemeral private key
  // aepk = Alice ephemeral public key
  // Bob's X25519 static keys
  // bsk = Bob private static key
  // bpk = Bob public static key

  // Generate the tag
  tagsetEntry = tagset_nsr.GET_NEXT_ENTRY()
  tag = tagsetEntry.SESSION_TAG

  // MixHash(tag)
  h = SHA256(h || tag)

  Dies ist das "e" Nachrichtenmuster:

  // Bob's X25519 ephemeral keys
  besk = GENERATE_PRIVATE_ELG2()
  bepk = DERIVE_PUBLIC(besk)

  // Bob's ephemeral public key
  // MixHash(bepk)
  // || below means append
  h = SHA256(h || bepk);

  // elg2_bepk is sent in cleartext in the
  // beginning of the New Session message
  elg2_bepk = ENCODE_ELG2(bepk)
  // As decoded by Bob
  bepk = DECODE_ELG2(elg2_bepk)

  End of "e" message pattern.

  This is the "ee" message pattern:

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // ChaChaPoly parameters to encrypt/decrypt
  // chainKey from original New Session Payload Section
  sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
  keydata = HKDF(chainKey, sharedSecret, "", 32)
  chainKey = keydata[0:31]

  End of "ee" message pattern.

  This is the "se" message pattern:

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  sharedSecret = DH(ask, bepk) = DH(besk, apk)
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, ZEROLEN, ad)

  End of "se" message pattern.

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  chainKey is used in the ratchet below.

```


### KDF für Payload Section verschlüsselte Inhalte

Dies ist wie die erste Existing-Session-Nachricht,
nach Split, aber ohne separaten Tag.
Zusätzlich verwenden wir den Hash von oben, um die
Payload an die NSR-Nachricht zu binden.


```

// split()
  keydata = HKDF(chainKey, ZEROLEN, "", 64)
  k_ab = keydata[0:31]
  k_ba = keydata[32:63]
  tagset_ab = DH_INITIALIZE(chainKey, k_ab)
  tagset_ba = DH_INITIALIZE(chainKey, k_ba)

  // AEAD parameters for New Session Reply payload
  k = HKDF(k_ba, ZEROLEN, "AttachPayloadKDF", 32)
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, payload, ad)
```


### Hinweise

Mehrere NSR-Nachrichten können als Antwort gesendet werden, jede mit eindeutigen ephemeren Schlüsseln, abhängig von der Größe der Antwort.

Alice und Bob müssen für jede NS- und NSR-Nachricht neue ephemere Schlüssel verwenden.

Alice muss eine von Bobs NSR-Nachrichten empfangen, bevor sie Existing-Session-(ES)-Nachrichten sendet,
und Bob muss eine ES-Nachricht von Alice empfangen, bevor er ES-Nachrichten sendet.

Der ``chainKey`` und ``k`` aus Bobs NSR-Payload-Section werden als Eingaben für die anfänglichen ES-DH-Ratchets verwendet (beide Richtungen, siehe DH-Ratchet-KDF).

Bob darf nur Existing-Sessions für die ES-Nachrichten behalten, die er von Alice empfängt.
Alle anderen erstellten eingehenden und ausgehenden Sitzungen (für mehrere NSRs) sollten sofort nach dem Empfang von Alices erster ES-Nachricht für eine bestimmte Sitzung
zerstört werden.



### 1h) Existing-Session-Format

Session-Tag (8 Bytes)
Verschlüsselte Daten und MAC (siehe Abschnitt 3 unten)


### Format
Verschlüsselt:

```

+----+----+----+----+----+----+----+----+
  |       Session Tag                     |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +              (MAC)                    +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Session Tag :: 8 bytes, cleartext

  Payload Section encrypted data :: remaining data minus 16 bytes

  MAC :: Poly1305 message authentication code, 16 bytes

```


### Payload
Verschlüsselte Länge ist der Rest der Daten.
Entschlüsselte Länge ist 16 weniger als die verschlüsselte Länge.
Siehe den Payload-Abschnitt unten für Format und Anforderungen.


KDF

```
Siehe AEAD-Abschnitt unten.

  // AEAD parameters for Existing Session payload
  k = The 32-byte session key associated with this session tag
  n = The message number N in the current chain, as retrieved from the associated Session Tag.
  ad = The session tag, 8 bytes
  ciphertext = ENCRYPT(k, n, payload, ad)
```



### 2) ECIES-X25519


Format: 32-Byte öffentliche und private Schlüssel, little-endian.

Begründung: Wird in [NTCP2](/docs/specs/ntcp2/) verwendet.



### 2a) Elligator2

In standardmäßigen Noise-Handshakes beginnen die anfänglichen Handshake-Nachrichten in jeder Richtung mit
ephemeren Schlüsseln, die im Klartext übertragen werden.
Da gültige X25519-Schlüssel von Zufallsdaten unterscheidbar sind, kann ein Man-in-the-Middle diese Nachrichten von Existing-Session-Nachrichten unterscheiden, die mit zufälligen Session-Tags beginnen.
In [NTCP2](/docs/specs/ntcp2/) ([Proposal 111](/proposals/111-ntcp-2/)) verwendeten wir eine Low-Overhead-XOR-Funktion mit dem out-of-band statischen Schlüssel, um den Schlüssel zu verschleiern.
Allerdings ist das Bedrohungsmodell hier anders; wir möchten nicht zulassen, dass irgendein MitM
irgendein Mittel verwendet, um das Ziel des Datenverkehrs zu bestätigen oder die
anfänglichen Handshake-Nachrichten von Existing-Session-Nachrichten zu unterscheiden.

Daher wird [Elligator2](https://elligator.cr.yp.to/) verwendet, um die ephemeren Schlüssel in den New-Session- und New-Session-Reply-Nachrichten so zu transformieren,
dass sie von gleichmäßigen zufälligen Zeichenketten ununterscheidbar sind.



### Format

32-Byte öffentliche und private Schlüssel.
Kodierte Schlüssel sind little-endian.

Wie in [Elligator2](https://elligator.cr.yp.to/) definiert, sind die kodierte Schlüssel von 254 zufälligen Bits ununterscheidbar.
Wir benötigen 256 zufällige Bits (32 Bytes). Daher sind die Kodierung und Dekodierung
wie folgt definiert:

Kodierung:

```

ENCODE_ELG2() Definition

  // Encode as defined in Elligator2 specification
  encodedKey = encode(pubkey)
  // OR in 2 random bits to MSB
  randomByte = CSRNG(1)
  encodedKey[31] |= (randomByte & 0xc0)
```


Dekodierung:

```

DECODE_ELG2() Definition

  // Mask out 2 random bits from MSB
  encodedKey[31] &= 0x3f
  // Decode as defined in Elligator2 specification
  pubkey = decode(encodedKey)
```




### Begründung

Erforderlich, um zu verhindern, dass OBEP und IBGW den Datenverkehr klassifizieren.


### Hinweise

Elligator2 verdoppelt im Durchschnitt die Schlüsselgenerierungszeit, da die Hälfte der privaten Schlüssel
öffentliche Schlüssel erzeugt, die für die Kodierung mit Elligator2 ungeeignet sind.
Außerdem ist die Schlüsselgenerierungszeit mit einer exponentiellen Verteilung unbeschränkt,
da der Generator weiter versuchen muss, bis ein geeignetes Schlüsselpaar gefunden wird.

Dieser Overhead kann durch vorherige Schlüsselgenerierung
in einem separaten Thread verwaltet werden, um einen Pool geeigneter Schlüssel zu halten.

Der Generator führt die ENCODE_ELG2()-Funktion durch, um die Eignung zu bestimmen.
Daher sollte der Generator das Ergebnis von ENCODE_ELG2()
speichern, damit es nicht erneut berechnet werden muss.

Zusätzlich können die ungeeigneten Schlüssel dem Pool von Schlüsseln hinzugefügt werden,
die für [NTCP2](/docs/specs/ntcp2/) verwendet werden, wo Elligator2 nicht verwendet wird.
Die Sicherheitsfragen dabei sind TBD.




### 3) AEAD (ChaChaPoly)

AEAD mit ChaCha20 und Poly1305, gleich wie in [NTCP2](/docs/specs/ntcp2/).
Dies entspricht [RFC-7539](https://tools.ietf.org/html/rfc7539), das auch
ähnlich in TLS [RFC-7905](https://tools.ietf.org/html/rfc7905) verwendet wird.



### New-Session- und New-Session-Reply-Eingaben

Eingaben für die Verschlüsselungs-/Entschlüsselungsfunktionen
für einen AEAD-Block in einer New-Session-Nachricht:

```

k :: 32 byte cipher key
       See New Session and New Session Reply KDFs above.

  n :: Counter-based nonce, 12 bytes.
       n = 0

  ad :: Associated data, 32 bytes.
        The SHA256 hash of the preceding data, as output from mixHash()

  data :: Plaintext data, 0 or more bytes

```


### Existing-Session-Eingaben

Eingaben für die Verschlüsselungs-/Entschlüsselungsfunktionen
für einen AEAD-Block in einer Existing-Session-Nachricht:

```

k :: 32 byte session key
       As looked up from the accompanying session tag.

  n :: Counter-based nonce, 12 bytes.
       Starts at 0 and incremented for each message when transmitting.
       For the receiver, the value
       as looked up from the accompanying session tag.
       First four bytes are always zero.
       Last eight bytes are the message number (n), little-endian encoded.
       Maximum value is 65535.
       Session must be ratcheted when N reaches that value.
       Higher values must never be used.

  ad :: Associated data
        The session tag

  data :: Plaintext data, 0 or more bytes

```


### Verschlüsseltes Format

Ausgabe der Verschlüss
