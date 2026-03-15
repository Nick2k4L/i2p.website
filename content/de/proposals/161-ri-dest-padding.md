---
title: "RI und Ziel Padding"
number: "161"
author: "zzz"
created: "2022-09-28"
lastupdated: "2023-01-02"
status: "Offen"
thread: "http://zzz.i2p/topics/3279"
target: "0.9.57"
toc: true
---
## Status

In Version 0.9.57 implementiert.  
Dieser Vorschlag bleibt offen, damit wir die Ideen im Abschnitt „Zukunftsplanung“ weiter verbessern und diskutieren können.


## Übersicht


### Zusammenfassung

Der ElGamal-Public-Key in Destinationen wird seit Release 0.6 (2005) nicht mehr verwendet.  
Obwohl unsere Spezifikationen angeben, dass er ungenutzt ist, sagen sie NICHT aus, dass Implementierungen darauf verzichten können, ein ElGamal-Schlüsselpaar zu generieren, und das Feld einfach mit zufälligen Daten füllen dürfen.

Wir schlagen vor, die Spezifikationen dahingehend zu ändern, dass  
das Feld ignoriert wird und Implementierungen das Feld mit zufälligen Daten füllen DÜRFEN.  
Diese Änderung ist abwärtskompatibel. Es ist keine Implementierung bekannt, die den ElGamal-Public-Key validiert.

Zusätzlich bietet dieser Vorschlag Implementierern Empfehlungen, wie die  
zufälligen Daten für die Padding-Felder in Destinationen UND Router-Identitäten generiert werden sollten,  
damit sie komprimierbar sind, gleichzeitig aber sicher bleiben und ihre Base64-Darstellungen nicht korrupt oder unsicher erscheinen.  
Dies bietet die meisten Vorteile des Entfernens der Padding-Felder, ohne disruptive Protokolländerungen vorzunehmen.  
Komprimierbare Destinationen reduzieren die Größe von Streaming-SYN und repliable Datagrammen;  
komprimierbare Router-Identitäten reduzieren Database-Store-Nachrichten, SSU2-Session-Confirmed-Nachrichten und reseed-su3-Dateien.

Schließlich diskutiert der Vorschlag Möglichkeiten für neue Formate von Destinationen und Router-Identitäten,  
die das Padding vollständig eliminieren würden. Es gibt auch eine kurze Diskussion über Post-Quanten-Kryptografie und deren mögliche Auswirkungen auf zukünftige Planungen.



### Ziele

- Entfernen der Notwendigkeit, ein ElGamal-Schlüsselpaar für Destinationen zu generieren
- Empfehlung bewährter Verfahren, damit Destinationen und Router-Identitäten stark komprimierbar sind,  
  aber keine offensichtlichen Muster in ihren Base64-Darstellungen aufweisen
- Förderung der Übernahme bewährter Verfahren durch alle Implementierungen, sodass die Felder nicht unterscheidbar sind
- Reduzierung der Streaming-SYN-Größe
- Reduzierung der repliable-Datagramm-Größe
- Reduzierung der SSU2-RI-Blockgröße
- Reduzierung der SSU2-Session-Confirmed-Größe und der Fragmentierungshäufigkeit
- Reduzierung der Database-Store-Nachricht (mit RI)-Größe
- Reduzierung der Größe von Reseed-Dateien
- Beibehaltung der Kompatibilität in allen Protokollen und APIs
- Aktualisierung der Spezifikationen
- Diskussion alternativer Formate für neue Destinationen und Router-Identitäten

Durch das Entfallen der Notwendigkeit, ElGamal-Schlüssel zu generieren, könnten Implementierungen möglicherweise den ElGamal-Code vollständig entfernen,  
vorbehaltlich der Abwärtskompatibilitätsüberlegungen in anderen Protokollen.



## Design

Streng genommen reicht allein der 32-Byte lange Signatur-Public-Key (sowohl in Destinationen als auch in Router-Identitäten)  
und der 32-Byte lange Verschlüsselungs-Public-Key (nur in Router-Identitäten) als Zufallszahl aus,  
um sicherzustellen, dass die SHA-256-Hashes dieser Strukturen kryptografisch stark sind und im Netzwerkdatenbank-DHT zufällig verteilt werden.

Aus übermäßiger Vorsicht empfehlen wir jedoch, mindestens 32 Bytes zufälliger Daten  
im ElG-Public-Key-Feld und im Padding zu verwenden. Außerdem würden Destinationen mit ausschließlich Nullen in den Feldern  
lange Sequenzen von AAAA-Zeichen in ihrer Base64-Darstellung enthalten, was bei Benutzern Besorgnis oder Verwirrung auslösen könnte.

Für den Ed25519-Signaturtyp und den X25519-Verschlüsselungstyp:  
Destinationen enthalten 11 Kopien (352 Bytes) der zufälligen Daten.  
Router-Identitäten enthalten 10 Kopien (320 Bytes) der zufälligen Daten.



### Geschätzte Einsparungen

Destinationen sind in jeder Streaming-SYN  
und jedem repliable Datagramm enthalten.  
Router-Infos (mit Router-Identitäten) sind in Database-Store-Nachrichten  
und in den Session-Confirmed-Nachrichten von NTCP2 und SSU2 enthalten.

NTCP2 komprimiert die Router-Info nicht.  
RIs in Database-Store-Nachrichten und SSU2-Session-Confirmed-Nachrichten werden mit gzip komprimiert.  
Router-Infos werden in reseed-SU3-Dateien mit zip komprimiert.

Destinationen in Database-Store-Nachrichten werden nicht komprimiert.  
Streaming-SYN-Nachrichten werden auf der I2CP-Ebene mit gzip komprimiert.

Für den Ed25519-Signaturtyp und den X25519-Verschlüsselungstyp  
geschätzte Einsparungen:

| Datentyp | Gesamtgröße | Schlüssel und Zertifikat | Unkomprimiertes Padding | Komprimiertes Padding | Größe | Einsparung |
|-----------|------------|---------------|----------------------|--------------------|------|---------|
| Destination | 391 | 39 | 352 | 32 | 71 | 320 Bytes (82 %) |
| Router-Identität | 391 | 71 | 320 | 32 | 103 | 288 Bytes (74 %) |
| Router-Info | 1000 typ. | 71 | 320 | 32 | 722 typ. | 288 Bytes (29 %) |

Anmerkungen: Geht davon aus, dass ein 7-Byte-Zertifikat nicht komprimierbar ist, ohne zusätzlichen gzip-Overhead.  
Beides ist nicht zutreffend, aber die Effekte sind gering.  
Ignoriert andere komprimierbare Teile der Router-Info.



## Spezifikation

Vorgeschlagene Änderungen an unseren aktuellen Spezifikationen sind unten dokumentiert.


### Gemeinsame Strukturen
Ändern Sie die Spezifikation für gemeinsame Strukturen dahingehend,  
dass das 256-Byte große Public-Key-Feld der Destination ignoriert wird und zufällige Daten enthalten darf.

Fügen Sie einen Abschnitt zur Spezifikation für gemeinsame Strukturen hinzu,  
der bewährte Verfahren für das Public-Key-Feld der Destination und die  
Padding-Felder in Destination und Router-Identität wie folgt empfiehlt:

Generieren Sie 32 Bytes zufälliger Daten mithilfe eines kryptografisch starken Pseudozufallszahlengenerators (PRNG)  
und wiederholen Sie diese 32 Bytes nach Bedarf, um das Public-Key-Feld (für Destinationen)  
und das Padding-Feld (für Destinationen und Router-Identitäten) zu füllen.

### Private-Key-Datei
Das Format der privaten Schlüsseldatei (eepPriv.dat) ist kein offizieller Bestandteil unserer Spezifikationen,  
wird aber in den [Java-I2P-Javadocs](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html) dokumentiert,  
und andere Implementierungen unterstützen es ebenfalls.  
Dies ermöglicht die Portabilität privater Schlüssel zwischen verschiedenen Implementierungen.  
Fügen Sie in diesen Javadocs einen Hinweis hinzu, dass der Verschlüsselungs-Public-Key aus zufälligem Padding bestehen darf  
und der Verschlüsselungs-Private-Key aus lauter Nullen oder zufälligen Daten bestehen darf.

### SAM
Hinweis in der SAM-Spezifikation: Der Verschlüsselungs-Private-Key wird nicht verwendet und kann ignoriert werden.  
Der Client kann beliebige zufällige Daten zurückgeben.  
Die SAM-Brücke kann bei der Erstellung (mit DEST GENERATE oder SESSION CREATE DESTINATION=TRANSIENT) zufällige Daten anstelle von Nullen senden,  
damit die Base64-Darstellung keine Zeichenfolge aus AAAA-Zeichen enthält und nicht defekt wirkt.


### I2CP
Keine Änderungen an I2CP erforderlich. Der Private Key zum Verschlüsselungs-Public-Key in der Destination  
wird nicht an den Router gesendet.


## Zukunftsplanung


### Protokolländerungen

Auf Kosten von Protokolländerungen und fehlender Abwärtskompatibilität könnten wir  
unsere Protokolle und Spezifikationen so ändern, dass das Padding-Feld in  
der Destination, der Router-Identität oder beiden entfällt.

Dieser Vorschlag ähnelt in gewisser Weise dem „b33“-Format für verschlüsselte Leasesets,  
das nur ein Schlüsselfeld und ein Typfeld enthält.

Zur Beibehaltung einiger Kompatibilität könnten bestimmte Protokollschichten das Padding-Feld  
mit Nullen „erweitern“, um es anderen Protokollschichten darzustellen.

Für Destinationen könnten wir auch das Verschlüsselungstyp-Feld im Schlüsselzertifikat entfernen,  
was eine Einsparung von zwei Bytes bedeutet.  
Alternativ könnte die Destination einen neuen Verschlüsselungstyp im Schlüsselzertifikat erhalten,  
der einen Null-Public-Key (und Padding) anzeigt.

Falls keine Kompatibilitätskonvertierung zwischen alten und neuen Formaten auf einer Protokollschicht vorgesehen ist,  
wären folgende Spezifikationen, APIs, Protokolle und Anwendungen betroffen:

- Common-structures-Spezifikation
- I2NP
- I2CP
- NTCP2
- SSU2
- Ratchet
- Streaming
- SAM
- Bittorrent
- Reseeding
- Private-Key-Datei
- Java-Core und Router-API
- i2pd-API
- Drittanbieter-SAM-Bibliotheken
- Eingebettete und Drittanbieter-Tools
- Mehrere Java-Plugins
- Benutzeroberflächen
- P2P-Anwendungen, z. B. MuWire, Bitcoin, Monero
- hosts.txt, Adressbuch und Abonnements

Falls die Konvertierung auf einer Schicht spezifiziert wird, wäre die Liste kürzer.

Die Kosten und Nutzen dieser Änderungen sind unklar.

Konkrete Vorschläge noch offen:





### PQ-Schlüssel

Post-Quantum (PQ)-Verschlüsselungs-Public-Keys sind für jeden erwarteten Algorithmus  
größer als 256 Bytes. Dies würde jegliches Padding und jegliche Einsparungen durch die oben vorgeschlagenen Änderungen  
für Router-Identitäten eliminieren.

Bei einem „hybriden“ PQ-Ansatz, wie er auch in SSL verwendet wird, wären die PQ-Schlüssel nur ephemeral  
und würden nicht in der Router-Identität erscheinen.

PQ-Signaturschlüssel sind nicht praktikabel,  
und Destinationen enthalten keine Verschlüsselungs-Public-Keys.  
Statische Schlüssel für Ratchet befinden sich im Lease Set, nicht in der Destination.  
Daher können wir Destinationen aus der folgenden Diskussion ausschließen.

PQ betrifft also nur Router-Infos, und nur bei PQ-statischen (nicht ephemeralen) Schlüsseln, nicht bei hybriden PQ-Schlüsseln.  
Dies wäre für einen neuen Verschlüsselungstyp und würde NTCP2, SSU2 sowie  
verschlüsselte Database-Lookup-Nachrichten und Antworten betreffen.  
Der geschätzte Zeitrahmen für Design, Entwicklung und Einführung wäre ????????  
Aber erst nach hybriden oder Ratchet-????????????

Zur weiteren Diskussion siehe [dieses Thema](http://zzz.i2p/topics/3294).




## Probleme

Es könnte wünschenswert sein, das Netzwerk langsam neu zu schlüsseln, um neuen Routern Deckung zu geben.  
„Neu schlüsseln“ könnte einfach bedeuten, das Padding zu ändern, ohne die eigentlichen Schlüssel zu ändern.

Ein Neuschlüsseln bestehender Destinationen ist nicht möglich.

Sollten Router-Identitäten mit Padding im Public-Key-Feld durch einen anderen  
Verschlüsselungstyp im Schlüsselzertifikat gekennzeichnet werden? Dies würde Kompatibilitätsprobleme verursachen.




## Migration

Keine Abwärtskompatibilitätsprobleme beim Ersetzen des ElGamal-Schlüssels durch Padding.

Ein Neuschlüsseln, falls implementiert, wäre vergleichbar mit den drei vorherigen Übergängen bei Router-Identitäten:  
Von DSA-SHA1 zu ECDSA-Signaturen, dann zu  
EdDSA-Signaturen, dann zu X25519-Verschlüsselung.

Vorbehaltlich der Abwärtskompatibilitätsprobleme und nach Deaktivierung von SSU  
könnten Implementierungen den ElGamal-Code vollständig entfernen.  
Etwa 14 % der Router im Netzwerk verwenden den ElGamal-Verschlüsselungstyp, darunter viele Floodfills.

Ein Entwurf für einen Merge Request für Java I2P befindet sich unter [git.idk.i2p](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66).


## Referenzen

* [Common](/docs/specs/common-structures/)
* [Datagram](/docs/api/datagrams/)
* [I2CP](/docs/specs/i2cp/)
* [I2NP](/docs/specs/i2np/)
* [MR](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66)
* [NTCP2](/docs/specs/ntcp2/)
* [PKF](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html)
* [PQ](http://zzz.i2p/topics/3294)
* [SAM](/docs/api/samv3/)
* [SSU2](/docs/specs/ssu2/)
* [Streaming](/docs/specs/streaming/)
