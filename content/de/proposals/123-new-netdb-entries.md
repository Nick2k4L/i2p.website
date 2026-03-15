---
title: "Neue netDB-Einträge"
number: "123"
author: "zzz, str4d, orignal"
created: "2016-01-16"
lastupdated: "2020-07-18"
status: "Öffnen"
thread: "http://zzz.i2p/topics/2051"
supercedes: "110, 120, 121, 122"
toc: true
---
## Status

Teile dieses Vorschlags sind abgeschlossen und in Version 0.9.38 und 0.9.39 implementiert.  
Die Spezifikationen für gemeinsame Strukturen, I2CP, I2NP und andere  
sind nun aktualisiert, um die jetzt unterstützten Änderungen widerzuspiegeln.

Die abgeschlossenen Teile unterliegen weiterhin geringfügigen Überarbeitungen.  
Andere Teile dieses Vorschlags befinden sich noch in Entwicklung  
und unterliegen erheblichen Änderungen.

Die Dienstsuche (Typen 9 und 11) hat niedrige Priorität,  
ist nicht terminiert und könnte in einen separaten Vorschlag ausgelagert werden.


## Übersicht

Dies ist eine Aktualisierung und Zusammenfassung der folgenden 4 Vorschläge:

- 110 LS2
- 120 Meta LS2 für massives Multihoming
- 121 Verschlüsseltes LS2
- 122 Unauthentifizierte Dienstsuche (Anycasting)

Diese Vorschläge sind größtenteils unabhängig, aber aus Gründen der Konsistenz definieren wir und verwenden ein gemeinsames Format für mehrere davon.

Die folgenden Vorschläge sind teilweise verwandt:

- 140 Unsichtbares Multihoming (inkompatibel mit diesem Vorschlag)
- 142 Neues Kryptovorlage (für neue symmetrische Kryptografie)
- 144 ECIES-X25519-AEAD-Ratchet
- 145 ECIES-P256
- 146 Red25519
- 148 EdDSA-BLAKE2b-Ed25519
- 149 B32 für verschlüsseltes LS2
- 150 Garlic-Farm-Protokoll
- 151 ECDSA-Blinding


## Vorschlag

Dieser Vorschlag definiert 5 neue DatabaseEntry-Typen und den Prozess zum  
Speichern und Abrufen aus der Netzwerkdatenbank,  
sowie die Methode zum Signieren und Verifizieren dieser Signaturen.

### Ziele

- Rückwärtskompatibel
- LS2 verwendbar mit altem Multihoming
- Keine neuen Kryptoverfahren oder Primitiva erforderlich
- Beibehaltung der Entkopplung von Kryptografie und Signatur; Unterstützung aller aktuellen und zukünftigen Versionen
- Unterstützung optionaler Offline-Signaturschlüssel
- Reduzierung der Zeitstempelgenauigkeit zur Verringerung von Fingerprinting
- Aktivierung neuer Kryptoverfahren für Ziele
- Massive Multihoming-Fähigkeit
- Behebung mehrerer Probleme mit bestehenden verschlüsselten LS
- Optionales Blinding zur Verringerung der Sichtbarkeit durch Floodfills
- Verschlüsselung unterstützt sowohl Einzelschlüssel als auch mehrere widerrufbare Schlüssel
- Dienstsuche für einfachere Suche nach Outproxies, Anwendung-DHT-Bootstrap und andere Anwendungen
- Nichts brechen, was auf 32-Byte-binären Ziel-Hashes basiert, z. B. BitTorrent
- Flexibilität in Leasesets durch Eigenschaften, wie wir sie in Routerinfos haben
- Veröffentlichungszeitstempel und variable Ablaufzeit im Header, damit es auch funktioniert, wenn Inhalte verschlüsselt sind (nicht Zeitstempel aus frühester Lease ableiten)
- Alle neuen Typen befinden sich im selben DHT-Bereich und an denselben Orten wie bestehende Leasesets, sodass Benutzer vom alten LS zu LS2 migrieren oder zwischen LS2, Meta und Verschlüsselt wechseln können, ohne Ziel oder Hash zu ändern
- Ein vorhandenes Ziel kann zur Verwendung von Offline-Schlüsseln konvertiert werden oder zurück zu Online-Schlüsseln, ohne Ziel oder Hash zu ändern

### Nicht-Ziele / Außerhalb des Umfangs

- Neuer DHT-Rotationsalgorithmus oder gemeinsame Zufallszahlengenerierung
- Der spezifische neue Verschlüsselungstyp und das Ende-zu-Ende-Verschlüsselungsschema, um diesen neuen Typ zu verwenden, wären Gegenstand eines separaten Vorschlags. Hier wird keine neue Kryptografie spezifiziert oder diskutiert.
- Neue Verschlüsselung für RIs oder Tunnelaufbau. Das wäre Gegenstand eines separaten Vorschlags.
- Methoden zur Verschlüsselung, Übertragung und Empfang von I2NP DLM / DSM / DSRM-Nachrichten. Bleibt unverändert.
- Wie Meta generiert und unterstützt wird, einschließlich Backend-Inter-Router-Kommunikation, Management, Failover und Koordination. Unterstützung könnte I2CP, i2pcontrol oder ein neues Protokoll hinzugefügt werden. Dies könnte standardisiert werden oder auch nicht.
- Wie tatsächlich länger laufende Tunnel implementiert und verwaltet oder bestehende Tunnel abgebrochen werden. Das ist extrem schwierig, und ohne dies kann kein vernünftiger, sanfter Herunterfahren erfolgen.
- Änderungen am Bedrohungsmodell
- Offline-Speicherformat oder Methoden zum Speichern/Abrufen/Teilen der Daten
- Implementierungsdetails werden hier nicht diskutiert und bleiben jedem Projekt überlassen


### Begründung

LS2 fügt Felder für die Änderung des Verschlüsselungstyps und zukünftige Protokolländerungen hinzu.

Verschlüsseltes LS2 behebt mehrere Sicherheitsprobleme mit dem bestehenden verschlüsselten LS, indem die gesamte Menge von Leases asymmetrisch verschlüsselt wird.

Meta LS2 bietet flexibles, effizientes, effektives und großskaliges Multihoming.

Dienst-Eintrag und Dienst-Liste bieten Anycast-Dienste wie Namenssuche und DHT-Bootstrap.


### NetDB-Datentypen

Die Typnummern werden in den I2NP Database Lookup/Store-Nachrichten verwendet.

Die Spalte „Ende-zu-Ende“ bezieht sich darauf, ob Abfragen/Antworten an ein Ziel in einer Garlic-Nachricht gesendet werden.

Bestehende Typen:

| NetDB-Daten | Lookup-Typ | Store-Typ |
|------------|-------------|------------|
| beliebig   | 0           | beliebig   |
| LS         | 1           | 1          |
| RI         | 2           | 0          |
| explorativ | 3           | DSRM       |

Neue Typen:

| NetDB-Daten     | Lookup-Typ | Store-Typ | Standard-LS2-Header? | Ende-zu-Ende gesendet? |
|----------------|-------------|------------|------------------|------------------|
| LS2            | 1           | 3          | ja               | ja               |
| Verschlüsseltes LS2  | 1           | 5          | nein             | nein             |
| Meta LS2       | 1           | 7          | ja               | nein             |
| Dienst-Eintrag | n/a         | 9          | ja               | nein             |
| Dienst-Liste   | 4           | 11         | nein             | nein             |


### Hinweise

- Lookup-Typen verwenden derzeit die Bits 3-2 in der Database Lookup-Nachricht.  
  Zusätzliche Typen würden die Verwendung von Bit 4 erfordern.

- Alle Store-Typen sind ungerade, da die oberen Bits im Typfeld der Database Store-Nachricht von alten Routern ignoriert werden.  
  Wir bevorzugen, dass das Parsen als LS fehlschlägt, nicht als komprimiertes RI.

- Sollte der Typ explizit, implizit oder gar nicht in den durch die Signatur abgedeckten Daten sein?


### Lookup/Store-Prozess

Typen 3, 5 und 7 können als Antwort auf eine Standard-Leaseset-Abfrage (Typ 1) zurückgegeben werden.  
Typ 9 wird niemals als Antwort auf eine Abfrage zurückgegeben.  
Typ 11 wird als Antwort auf einen neuen Dienstsuchtyp (Typ 11) zurückgegeben.

Nur Typ 3 kann in einer Garlic-Nachricht von Client zu Client gesendet werden.


### Format

Typen 3, 7 und 9 haben ein gemeinsames Format::

  Standard-LS2-Header
  - wie unten definiert

  Typspezifischer Teil
  - wie unten in jedem Teil definiert

  Standard-LS2-Signatur:
  - Länge wie durch Sig-Typ des Signaturschlüssels impliziert

Typ 5 (verschlüsselt) beginnt nicht mit einem Ziel und hat ein anderes Format. Siehe unten.

Typ 11 (Dienst-Liste) ist eine Aggregation mehrerer Dienst-Einträge und hat ein anderes Format. Siehe unten.


### Datenschutz-/Sicherheitsüberlegungen

TBD


## Standard-LS2-Header

Typen 3, 7 und 9 verwenden den Standard-LS2-Header, wie unten spezifiziert:


### Format

```
Standard-LS2-Header:
  - Typ (1 Byte)
    Nicht tatsächlich im Header, aber Teil der durch die Signatur abgedeckten Daten.
    Aus Feld in Database Store-Nachricht entnehmen.
  - Ziel (387+ Bytes)
  - Veröffentlichungszeitstempel (4 Bytes, Big Endian, Sekunden seit Epoche, Überlauf im Jahr 2106)
  - Ablauf (2 Bytes, Big Endian) (Offset vom Veröffentlichungszeitstempel in Sekunden, max. 18,2 Stunden)
  - Flags (2 Bytes)
    Bitreihenfolge: 15 14 ... 3 2 1 0
    Bit 0: Wenn 0, keine Offline-Schlüssel; wenn 1, Offline-Schlüssel
    Bit 1: Wenn 0, ein Standard-veröffentlichtes Leaseset.
           Wenn 1, ein nicht veröffentlichtes Leaseset. Sollte nicht geflutet, veröffentlicht oder
           als Antwort auf eine Abfrage gesendet werden. Wenn dieses Leaseset abläuft, nicht im
           NetDB nach einem neuen suchen, es sei denn, Bit 2 ist gesetzt.
    Bit 2: Wenn 0, ein Standard-veröffentlichtes Leaseset.
           Wenn 1, wird dieses unverschlüsselte Leaseset beim Veröffentlichen verblendet und verschlüsselt.
           Wenn dieses Leaseset abläuft, im NetDB nach der verblendeten Position nach einem neuen suchen.
           Wenn dieses Bit auf 1 gesetzt ist, muss auch Bit 1 auf 1 gesetzt sein.
           Ab Version 0.9.42.
    Bits 3-15: Zur Kompatibilität mit zukünftigen Verwendungen auf 0 setzen
  - Wenn Flag Offline-Schlüssel anzeigt, folgt der Offline-Signaturabschnitt:
    Ablaufzeitstempel (4 Bytes, Big Endian, Sekunden seit Epoche, Überlauf im Jahr 2106)
    Transienter Sig-Typ (2 Bytes, Big Endian)
    Transienter öffentlicher Signaturschlüssel (Länge wie durch Sig-Typ impliziert)
    Signatur des Ablaufzeitstempels, transienten Sig-Typs und öffentlichen Schlüssels,
    durch den öffentlichen Ziel-Schlüssel,
    Länge wie durch Sig-Typ des öffentlichen Ziel-Schlüssels impliziert.
    Dieser Abschnitt kann und sollte offline generiert werden.
```

### Begründung

- Nicht veröffentlicht/veröffentlicht: Zur Verwendung beim Senden einer Datenbank-Speicherung Ende-zu-Ende,
  kann der sendende Router angeben, dass dieses Leaseset nicht an andere gesendet werden soll. Derzeit verwenden wir Heuristiken, um diesen Zustand beizubehalten.

- Veröffentlicht: Ersetzt die komplexe Logik zur Bestimmung der „Version“ des Leasesets. Derzeit ist die Version das Ablaufdatum der am längsten laufenden Lease, und ein Router, der ein Leaseset veröffentlicht, das nur eine ältere Lease entfernt, muss dieses Ablaufdatum um mindestens 1 ms erhöhen.

- Ablauf: Ermöglicht, dass das Ablaufdatum eines NetDB-Eintrags früher ist als das der am längsten laufenden Leaseset. Für LS2 möglicherweise nicht nützlich, wo Leasesets mit maximal 11 Minuten Ablauf erwartet werden, aber für andere neue Typen notwendig (siehe Meta LS und Dienst-Eintrag unten).

- Offline-Schlüssel sind optional, um die anfängliche/erforderliche Implementierungskomplexität zu reduzieren.


### Probleme

- Die Zeitstempelgenauigkeit könnte noch weiter reduziert werden (10 Minuten?), aber dann müsste eine Versionsnummer hinzugefügt werden. Dies könnte Multihoming brechen, es sei denn, wir haben ordnungserhaltende Verschlüsselung? Ohne Zeitstempel wahrscheinlich nicht machbar.

- Alternative: 3-Byte-Zeitstempel (Epoche / 10 Minuten), 1-Byte-Version, 2-Byte-Ablauf

- Ist der Typ explizit oder implizit in Daten/Signatur? „Domain“-Konstanten für Signatur?


### Hinweise

- Router sollten ein LS nicht öfter als einmal pro Sekunde veröffentlichen.  
  Wenn doch, müssen sie den Veröffentlichungszeitstempel künstlich um 1 gegenüber dem zuvor veröffentlichten LS erhöhen.

- Router-Implementierungen könnten die transienten Schlüssel und Signaturen zwischenspeichern,  
  um die Verifizierung bei jedem Zugriff zu vermeiden. Insbesondere Floodfills und Router an beiden Enden langlebiger Verbindungen könnten davon profitieren.

- Offline-Schlüssel und -signatur sind nur für langlebige Ziele geeignet,  
  d. h. Server, nicht Clients.


## Neue DatabaseEntry-Typen


### LeaseSet 2

Änderungen gegenüber bestehendem LeaseSet:

- Hinzufügen von Veröffentlichungszeitstempel, Ablaufzeitstempel, Flags und Eigenschaften
- Hinzufügen des Verschlüsselungstyps
- Entfernen des Widerrufschlüssels

Abfrage mit  
    Standard-LS-Flag (1)  
Speichern mit  
    Standard-LS2-Typ (3)  
Speichern unter  
    Hash des Ziels  
    Dieser Hash wird dann verwendet, um den täglichen „Routing-Key“ zu generieren, wie bei LS1  
Typischer Ablauf  
    10 Minuten, wie bei einem regulären LS.  
Veröffentlicht von  
    Ziel

### Format

```
Standard-LS2-Header wie oben spezifiziert

  Standard-LS2-Typspezifischer Teil
  - Eigenschaften (Mapping wie in der Spezifikation gemeinsamer Strukturen, 2 Null-Bytes, wenn keine)
  - Anzahl der folgenden Schlüsselabschnitte (1 Byte, max. TBD)
  - Schlüsselabschnitte:
    - Verschlüsselungstyp (2 Bytes, Big Endian)
    - Länge des Verschlüsselungsschlüssels (2 Bytes, Big Endian)
      Dies ist explizit, damit Floodfills LS2 mit unbekannten Verschlüsselungstypen parsen können.
    - Verschlüsselungsschlüssel (angegebene Anzahl Bytes)
  - Anzahl der Lease2s (1 Byte)
  - Lease2s (jeweils 40 Bytes)
    Dies sind Leases, aber mit 4-Byte statt 8-Byte-Ablauf,
    Sekunden seit Epoche (Überlauf im Jahr 2106)

  Standard-LS2-Signatur:
  - Signatur
    Wenn Flag Offline-Schlüssel anzeigt, wird dies durch den transienten öffentlichen Schlüssel signiert,
    andernfalls durch den öffentlichen Ziel-Schlüssel
    Länge wie durch Sig-Typ des Signaturschlüssels impliziert
    Die Signatur bezieht sich auf alles oben.
```


### Begründung

- Eigenschaften: Zukünftige Erweiterbarkeit und Flexibilität.  
  Zuerst platziert, falls zur Analyse der restlichen Daten erforderlich.

- Mehrere Verschlüsselungstyp-/öffentliche Schlüsselpaare  
  erleichtern den Übergang zu neuen Verschlüsselungstypen. Die andere Möglichkeit ist,  
  mehrere Leasesets zu veröffentlichen, möglicherweise mit denselben Tunneln,  
  wie wir es derzeit für DSA- und EdDSA-Ziele tun.  
  Die Identifizierung des eingehenden Verschlüsselungstyps auf einem Tunnel  
  kann mit dem bestehenden Session-Tag-Mechanismus erfolgen  
  und/oder durch Testentschlüsselung mit jedem Schlüssel. Die Länge der eingehenden  
  Nachrichten kann ebenfalls Hinweise geben.

### Diskussion

Dieser Vorschlag verwendet weiterhin den öffentlichen Schlüssel im Leaseset als Ende-zu-Ende-Verschlüsselungsschlüssel und lässt das öffentliche Schlüsselfeld im Ziel ungenutzt, wie es derzeit ist. Der Verschlüsselungstyp ist nicht im Zertifikat des Ziel-Schlüssels angegeben, bleibt 0.

Eine abgelehnte Alternative ist, den Verschlüsselungstyp im Zertifikat des Ziel-Schlüssels anzugeben, den öffentlichen Schlüssel im Ziel zu verwenden und den öffentlichen Schlüssel im Leaseset nicht zu verwenden. Dies ist nicht geplant.

Vorteile von LS2:

- Der Ort des tatsächlichen öffentlichen Schlüssels ändert sich nicht.
- Verschlüsselungstyp oder öffentlicher Schlüssel können sich ändern, ohne das Ziel zu ändern.
- Entfernt das ungenutzte Widerruffeld
- Grundlegende Kompatibilität mit anderen DatabaseEntry-Typen in diesem Vorschlag
- Erlaubt mehrere Verschlüsselungstypen

Nachteile von LS2:

- Der Ort des öffentlichen Schlüssels und des Verschlüsselungstyps unterscheidet sich von RouterInfo
- Behält den ungenutzten öffentlichen Schlüssel im Leaseset bei
- Erfordert Implementierung im gesamten Netzwerk; alternativ könnten experimentelle Verschlüsselungstypen verwendet werden, wenn von Floodfills erlaubt (siehe aber verwandte Vorschläge 136 und 137 zur Unterstützung experimenteller Sig-Typen). Der alternative Vorschlag könnte einfacher zu implementieren und testen sein für experimentelle Verschlüsselungstypen.


### Neue Verschlüsselungsprobleme

Einiges davon ist für diesen Vorschlag außerhalb des Umfangs,  
aber hier werden vorläufige Notizen gesammelt, da wir noch  
keinen separaten Verschlüsselungsvorschlag haben.  
Siehe auch die ECIES-Vorschläge 144 und 145.

- Der Verschlüsselungstyp repräsentiert die Kombination  
  aus Kurve, Schlüssellänge und Ende-zu-Ende-Schema,  
  einschließlich KDF und MAC, falls vorhanden.

- Wir haben ein Schlüssellängenfeld eingefügt, damit das LS2  
  vom Floodfill auch für unbekannte Verschlüsselungstypen  
  analysierbar und verifizierbar ist.

- Der erste neue Verschlüsselungstyp, der vorgeschlagen wird, wird  
  wahrscheinlich ECIES/X25519 sein. Wie es Ende-zu-Ende verwendet wird  
  (entweder eine leicht modifizierte Version von ElGamal/AES+SessionTag  
  oder etwas völlig Neues, z. B. ChaCha/Poly) wird in einem oder mehreren separaten Vorschlägen spezifiziert.  
  Siehe auch die ECIES-Vorschläge 144 und 145.


### Hinweise

- 8-Byte-Ablauf in Leases geändert zu 4 Bytes.

- Falls wir jemals Widerruf implementieren, können wir dies mit einem Ablaufwert von Null tun, oder mit Null Leases, oder beidem. Kein separater Widerrufschlüssel erforderlich.

- Verschlüsselungsschlüssel sind in der Reihenfolge der Serverpräferenz, am liebsten zuerst.  
  Standardverhalten des Clients ist, den ersten Schlüssel mit unterstütztem Verschlüsselungstyp auszuwählen.  
  Clients können andere Auswahlalgorithmen basierend auf Verschlüsselungsunterstützung, relativer Leistung und anderen Faktoren verwenden.


### Verschlüsseltes LS2

Ziele:

- Hinzufügen von Blinding
- Erlauben mehrerer Sig-Typen
- Keine neuen Kryptoprimitiva erforderlich
- Optional an jeden Empfänger verschlüsseln, widerrufbar
- Unterstützung der Verschlüsselung von Standard-LS2 und Meta-LS2 nur

Verschlüsseltes LS2 wird niemals in einer Ende-zu-Ende-Garlic-Nachricht gesendet.  
Verwenden Sie stattdessen das Standard-LS2 wie oben.


Änderungen gegenüber bestehendem verschlüsseltem LeaseSet:

- Alles aus Sicherheitsgründen verschlüsseln
- Sicher verschlüsseln, nicht nur mit AES
- An jeden Empfänger verschlüsseln

Abfrage mit  
    Standard-LS-Flag (1)  
Speichern mit  
    Verschlüsseltes LS2-Typ (5)  
Speichern unter  
    Hash des verblendeten Sig-Typs und des verblendeten öffentlichen Schlüssels  
    Zweibytiger Sig-Typ (Big Endian, z. B. 0x000b) || verblendeter öffentlicher Schlüssel  
    Dieser Hash wird dann verwendet, um den täglichen „Routing-Key“ zu generieren, wie bei LS1  
Typischer Ablauf  
    10 Minuten, wie bei einem regulären LS, oder Stunden, wie bei einem Meta-LS.  
Veröffentlicht von  
    Ziel


### Definitionen

Wir definieren die folgenden Funktionen entsprechend den kryptografischen Bausteinen, die für verschlüsseltes LS2 verwendet werden:

CSRNG(n)  
    n-Byte-Ausgabe aus einem kryptografisch sicheren Zufallszahlengenerator.

    Zusätzlich zur Anforderung, dass CSRNG kryptografisch sicher ist (und daher geeignet für die Generierung von Schlüsselmaterial), muss es sicher sein, dass eine n-Byte-Ausgabe als Schlüsselmaterial verwendet werden kann, wenn die unmittelbar vorhergehenden und nachfolgenden Bytefolgen im Netzwerk sichtbar sind (z. B. in einem Salt oder verschlüsseltem Padding). Implementierungen, die auf einer potenziell unsicheren Quelle basieren, sollten jede Ausgabe, die im Netzwerk sichtbar ist, hashen. Siehe [PRNG-Referenzen](http://projectbullrun.org/dual-ec/ext-rand.html) und [Tor-Entwicklerdiskussion](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html).

H(p, d)  
    SHA-256-Hashfunktion, die eine Personalisierungszeichenfolge p und Daten d nimmt und eine Ausgabe der Länge 32 Bytes erzeugt.

    Verwenden Sie SHA-256 wie folgt::

        H(p, d) := SHA-256(p || d)

STREAM  
    Der ChaCha20-Streamchiffre wie in [RFC 7539 Abschnitt 2.4](https://tools.ietf.org/html/rfc7539#section-2.4) spezifiziert, mit dem Anfangszähler auf 1 gesetzt. S_KEY_LEN = 32 und S_IV_LEN = 12.

    ENCRYPT(k, iv, plaintext)  
        Verschlüsselt den Klartext mit dem Chiffrierschlüssel k und dem Nonce iv, das für den Schlüssel k eindeutig sein muss. Gibt einen Geheimtext zurück, der dieselbe Größe wie der Klartext hat.

        Der gesamte Geheimtext muss ununterscheidbar von Zufall sein, wenn der Schlüssel geheim ist.

    DECRYPT(k, iv, ciphertext)  
        Entschlüsselt den Geheimtext mit dem Chiffrierschlüssel k und dem Nonce iv. Gibt den Klartext zurück.

SIG  
    Das RedDSA-Signaturschema (entsprechend Sig-Typ 11) mit Schlüssel-Blinding.  
    Es hat die folgenden Funktionen:

    DERIVE_PUBLIC(privkey)  
        Gibt den öffentlichen Schlüssel zurück, der zum gegebenen privaten Schlüssel gehört.

    SIGN(privkey, m)  
        Gibt eine Signatur des privaten Schlüssels privkey über die gegebene Nachricht m zurück.

    VERIFY(pubkey, m, sig)  
        Verifiziert die Signatur sig gegenüber dem öffentlichen Schlüssel pubkey und der Nachricht m. Gibt true zurück, wenn die Signatur gültig ist, andernfalls false.

    Es muss auch die folgenden Schlüssel-Blinding-Operationen unterstützen:

    GENERATE_ALPHA(data, secret)  
        Generiert alpha für diejenigen, die die Daten und ein optionales Geheimnis kennen.  
        Das Ergebnis muss identisch verteilt sein wie die privaten Schlüssel.

    BLIND_PRIVKEY(privkey, alpha)  
        Verblendet einen privaten Schlüssel unter Verwendung eines geheimen alpha.

    BLIND_PUBKEY(pubkey, alpha)  
        Verblendet einen öffentlichen Schlüssel unter Verwendung eines geheimen alpha.  
        Für ein gegebenes Schlüsselpaar (privkey, pubkey) gilt folgende Beziehung::

            BLIND_PUBKEY(pubkey, alpha) ==
            DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))

DH  
    X25519-System zur öffentlichen Schlüsselvereinbarung. Private Schlüssel mit 32 Bytes, öffentliche Schlüssel mit 32 Bytes, erzeugt Ausgaben mit 32 Bytes. Es hat die folgenden Funktionen:

    GENERATE_PRIVATE()  
        Generiert einen neuen privaten Schlüssel.

    DERIVE_PUBLIC(privkey)  
        Gibt den öffentlichen Schlüssel zurück, der zum gegebenen privaten Schlüssel gehört.

    DH(privkey, pubkey)  
        Generiert einen gemeinsamen geheimen Schlüssel aus den gegebenen privaten und öffentlichen Schlüsseln.

HKDF(salt, ikm, info, n)  
    Eine kryptografische Schlüsselableitungsfunktion, die einige Eingabeschlüsselmaterial ikm (das gute Entropie haben sollte, aber nicht eine gleichmäßig zufällige Zeichenfolge sein muss), ein Salt der Länge 32 Bytes und einen kontextspezifischen „info“-Wert nimmt und eine Ausgabe von n Bytes erzeugt, die als Schlüsselmaterial geeignet ist.

    Verwenden Sie HKDF wie in [RFC 5869](https://tools.ietf.org/html/rfc5869) spezifiziert, unter Verwendung der HMAC-Hashfunktion SHA-256 wie in [RFC 2104](https://tools.ietf.org/html/rfc2104) spezifiziert. Das bedeutet, dass SALT_LEN maximal 32 Bytes beträgt.


### Format

Das verschlüsselte LS2-Format besteht aus drei verschachtelten Schichten:

- Eine äußere Schicht, die die notwendigen Klartextinformationen für Speicherung und Abruf enthält.
- Eine mittlere Schicht, die die Client-Authentifizierung behandelt.
- Eine innere Schicht, die die eigentlichen LS2-Daten enthält.

Das Gesamtformat sieht wie folgt aus::

    Schicht-0-Daten + Enc(Schicht-1-Daten + Enc(Schicht-2-Daten)) + Signatur

Beachten Sie, dass verschlüsseltes LS2 verblendet ist. Das Ziel ist nicht im Header enthalten.  
Der DHT-Speicherort ist SHA-256(Sig-Typ || verblendeter öffentlicher Schlüssel) und wird täglich rotiert.

Verwendet NICHT den oben spezifizierten Standard-LS2-Header.

#### Schicht 0 (äußerste)
Typ  
    1 Byte

    Nicht tatsächlich im Header, aber Teil der durch die Signatur abgedeckten Daten.  
    Aus Feld in Database Store-Nachricht entnehmen.

Verblendeter öffentlicher Schlüssel-Sig-Typ  
    2 Bytes, Big Endian  
    Dies wird immer Typ 11 sein, identifiziert einen verblendeten Red25519-Schlüssel.

Verblendeter öffentlicher Schlüssel  
    Länge wie durch Sig-Typ impliziert

Veröffentlichungszeitstempel  
    4 Bytes, Big Endian

    Sekunden seit Epoche, Überlauf im Jahr 2106

Ablauf  
    2 Bytes, Big Endian

    Offset vom Veröffentlichungszeitstempel in Sekunden, max. 18,2 Stunden

Flags  
    2 Bytes

    Bitreihenfolge: 15 14 ... 3 2 1 0

    Bit 0: Wenn 0, keine Offline-Schlüssel; wenn 1, Offline-Schlüssel

    Andere Bits: Zur Kompatibilität mit zukünftigen Verwendungen auf 0 setzen

Transienter Schlüsseldaten  
    Vorhanden, wenn Flag Offline-Schlüssel anzeigt

    Ablaufzeitstempel  
        4 Bytes, Big Endian

        Sekunden seit Epoche, Überlauf im Jahr 2106

    Transienter Sig-Typ  
        2 Bytes, Big Endian

    Transienter öffentlicher Signaturschlüssel  
        Länge wie durch Sig-Typ impliziert

    Signatur  
        Länge wie durch Sig-Typ des verblendeten öffentlichen Schlüssels impliziert

        Über Ablaufzeitstempel, transienten Sig-Typ und transienten öffentlichen Schlüssel.

        Mit dem verblendeten öffentlichen Schlüssel verifiziert.

lenOuterCiphertext  
    2 Bytes, Big Endian

outerCiphertext  
    lenOuterCiphertext Bytes

    Verschlüsselte Schicht-1-Daten. Siehe unten für Schlüsselableitung und Verschlüsselungsalgorithmen.

Signatur  
    Länge wie durch Sig-Typ des verwendeten Signaturschlüssels impliziert

    Die Signatur bezieht sich auf alles oben.

    Wenn das Flag Offline-Schlüssel anzeigt, wird die Signatur mit dem transienten öffentlichen Schlüssel verifiziert. Andernfalls wird sie mit dem verblendeten öffentlichen Schlüssel verifiziert.


#### Schicht 1 (mittlere)
Flags  
    1 Byte
    
    Bitreihenfolge: 76543210

    Bit 0: 0 für alle, 1 für pro-Client, Auth-Abschnitt folgt

    Bits 3-1: Authentifizierungsschema, nur wenn Bit 0 auf 1 für pro-Client gesetzt ist, sonst 000  
              000: DH-Client-Authentifizierung (oder keine pro-Client-Authentifizierung)  
              001: PSK-Client-Authentifizierung

    Bits 7-4: Unbenutzt, zur zukünftigen Kompatibilität auf 0 setzen

DH-Client-Auth-Daten  
    Vorhanden, wenn Flag-Bit 0 auf 1 gesetzt ist und Flag-Bits 3-1 auf 000 gesetzt sind.

    ephemeralPublicKey  
        32 Bytes

    clients  
        2 Bytes, Big Endian

        Anzahl der folgenden authClient-Einträge, jeweils 40 Bytes

    authClient  
        Autorisierungsdaten für einen einzelnen Client.  
        Siehe unten für den pro-Client-Autorisierungsalgorithmus.

        clientID_i  
            8 Bytes

        clientCookie_i  
            32 Bytes

PSK-Client-Auth-Daten  
    Vorhanden, wenn Flag-Bit 0 auf 1 gesetzt ist und Flag-Bits 3-1 auf 001 gesetzt sind.

    authSalt  
        32 Bytes

    clients  
        2 Bytes, Big Endian

        Anzahl der folgenden authClient-Einträge, jeweils 40 Bytes

    authClient  
        Autorisierungsdaten für einen einzelnen Client.  
        Siehe unten für den pro-Client-Autorisierungsalgorithmus.

        clientID_i  
            8 Bytes

        clientCookie_i  
            32 Bytes


innerCiphertext  
    Länge impliziert durch lenOuterCiphertext (verbleibende Daten)

    Verschlüsselte Schicht-2-Daten. Siehe unten für Schlüsselableitung und Verschlüsselungsalgorithmen.


#### Schicht 2 (innere)
Typ  
    1 Byte

    Entweder 3 (LS2) oder 7 (Meta LS2)

Daten  
    LeaseSet2-Daten für den gegebenen Typ.

    Enthält Header und Signatur.


### Blinding-Schlüsselableitung

Wir verwenden das folgende Schema für die Schlüsselverblendung,  
basierend auf Ed25519 und [ZCash RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf).  
Die Re25519-Signaturen erfolgen über die Ed25519-Kurve, unter Verwendung von SHA-512 für den Hash.

Wir verwenden NICHT [Tor's rend-spec-v3.txt Anhang A.2](https://spec.torproject.org/rend-spec-v3),  
das ähnliche Designziele hat, weil seine verblendeten öffentlichen Schlüssel  
außerhalb der prim-Ordnungs-Untergruppe liegen könnten, mit unbekannten Sicherheitsimplikationen.


#### Ziele

- Der Signierungs-öffentliche Schlüssel im unverblendeten Ziel muss  
  Ed25519 (Sig-Typ 7) oder Red25519 (Sig-Typ 11) sein;  
  keine anderen Sig-Typen werden unterstützt
- Wenn der Signierungs-öffentliche Schlüssel offline ist, muss auch der transiente öffentliche Signaturschlüssel Ed25519 sein
- Verblendung ist rechnerisch einfach
- Verwendung bestehender kryptografischer Primitiva
- Verblendete öffentliche Schlüssel können nicht entblendet werden
- Verblendete öffentliche Schlüssel müssen auf der Ed25519-Kurve und der prim-Ordnungs-Untergruppe liegen
- Es muss der Signierungs-öffentliche Schlüssel des Ziels bekannt sein  
  (vollständiges Ziel nicht erforderlich), um den verblendeten öffentlichen Schlüssel abzuleiten
- Optional kann ein zusätzliches Geheimnis bereitgestellt werden, das zum Ableiten des verblendeten öffentlichen Schlüssels erforderlich ist


#### Sicherheit

Die Sicherheit eines Verblendungsschemas erfordert, dass die  
Verteilung von alpha identisch mit der der unverblendeten privaten Schlüssel ist.  
Wenn wir jedoch einen Ed25519-privaten Schlüssel (Sig-Typ 7)  
zu einem Red25519-privaten Schlüssel (Sig-Typ 11) verblenden,  
ist die Verteilung unterschiedlich. Um die Anforderungen von [zcash Abschnitt 4.1.6.1](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) zu erfüllen,  
sollte Red25519 (Sig-Typ 11) auch für die unverblendeten Schlüssel verwendet werden,  
damit „die Kombination aus einem neu randomisierten öffentlichen Schlüssel und Signatur(en)  
unter diesem Schlüssel den Schlüssel, von dem er neu randomisiert wurde, nicht offenbart“.  
Wir erlauben Typ 7 für bestehende Ziele, empfehlen aber  
Typ 11 für neue Ziele, die verschlüsselt werden sollen.


#### Definitionen

B  
    Der Ed25519-Basispunkt (Generator) 2^255 - 19 wie in [Ed25519](http://cr.yp.to/papers.html#ed25519)

L  
    Die Ed25519-Ordnung 2^252 + 27742317777372353535851937790883648493  
    wie in [Ed25519](http://cr.yp.to/papers.html#ed25519)

DERIVE_PUBLIC(a)  
    Konvertiert einen privaten Schlüssel in öffentlich, wie in Ed25519 (Multiplikation mit G)

alpha  
    Eine 32-Byte-Zufallszahl, bekannt für diejenigen, die das Ziel kennen.

GENERATE_ALPHA(destination, date, secret)  
    Generiert alpha für das aktuelle Datum, für diejenigen, die das Ziel und das Geheimnis kennen.  
    Das Ergebnis muss identisch verteilt sein wie Ed25519-private Schlüssel.

a  
    Der unverblendete 32-Byte-EdDSA- oder RedDSA-Signatur-privatschlüssel, der zum Signieren des Ziels verwendet wird

A  
    Der unverblendete 32-Byte-EdDSA- oder RedDSA-Signatur-öffentliche Schlüssel im Ziel,  
    = DERIVE_PUBLIC(a), wie in Ed25519

a'  
    Der verblendete 32-Byte-EdDSA-Signatur-privatschlüssel, der zum Signieren des verschlüsselten Leasesets verwendet wird  
    Dies ist ein gültiger EdDSA-privater Schlüssel.

A'  
    Der verblendete 32-Byte-EdDSA-Signatur-öffentliche Schlüssel im Ziel,  
    kann mit DERIVE_PUBLIC(a') generiert werden oder aus A und alpha.  
    Dies ist ein gültiger EdDSA-öffentlicher Schlüssel, auf der Kurve und auf der prim-Ordnungs-Untergruppe.

LEOS2IP(x)  
    Kehrt die Reihenfolge der Eingabebits in Little-Endian um

H*(x)  
    32 Bytes = (LEOS2IP(SHA512(x))) mod B, wie in Ed25519 Hash-and-reduce


#### Verblendungsberechnungen

Ein neues Geheimnis alpha und verblendete Schlüssel müssen täglich (UTC) neu generiert werden.  
Das Geheimnis alpha und die verblendeten Schlüssel werden wie folgt berechnet.

GENERATE_ALPHA(destination, date, secret), für alle Parteien:

```text
// GENERATE_ALPHA(destination, date, secret)

  // secret ist optional, sonst null-längig
  A = Signatur-öffentlicher Schlüssel des Ziels
  stA = Sig-Typ von A, 2 Bytes Big Endian (0x0007 oder 0x000b)
  stA' = Sig-Typ des verblendeten öffentlichen Schlüssels A', 2 Bytes Big Endian (0x000b)
  keydata = A || stA || stA'
  datestring = 8 Bytes ASCII YYYYMMDD aus dem aktuellen Datum UTC
  secret = UTF-8-kodierter String
  seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || secret, "i2pblinding1", 64)
  // seed als 64-Byte-Little-Endian-Wert behandeln
  alpha = seed mod L
```

BLIND_PRIVKEY(), für den Eigentümer, der das Leaseset veröffentlicht:

```text
// BLIND_PRIVKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  // Wenn für einen Ed25519-privaten Schlüssel (Typ 7)
  seed = privater Signaturschlüssel des Ziels
  a = linke Hälfte von SHA512(seed) und wie üblich für Ed25519 geklemmt
  // sonst, für einen Red25519-privaten Schlüssel (Typ 11)
  a = privater Signaturschlüssel des Ziels
  // Addition mit Skalararithmetik
  verblendeter Signatur-privater Schlüssel = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
  verblendeter Signatur-öffentlicher Schlüssel = A' = DERIVE_PUBLIC(a')
```

BLIND_PUBKEY(), für die Clients, die das Leaseset abrufen:

```text
// BLIND_PUBKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  A = Signatur-öffentlicher Schlüssel des Ziels
  // Addition mit Gruppenelementen (Punkte auf der Kurve)
  verblendeter öffentlicher Schlüssel = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```

Beide Methoden zur Berechnung von A' liefern das gleiche Ergebnis, wie erforderlich.


#### Signieren

Das unverblendete Leaseset wird vom unverblendeten Ed25519- oder Red25519-Signatur-privaten Schlüssel signiert und mit dem unverblendeten Ed25519- oder Red25519-Signatur-öffentlichen Schlüssel (Sig-Typen 7 oder 11) wie üblich verifiziert.

Wenn der Signatur-öffentliche Schlüssel offline ist,  
wird das unverblendete Leaseset vom unverblendeten transienten Ed25519- oder Red25519-Signatur-privaten Schlüssel signiert  
und mit dem unverblendeten Ed25519- oder Red25519-transienten öffentlichen Signaturschlüssel (Sig-Typen 7 oder 11) wie üblich verifiziert.  
Siehe unten für zusätzliche Hinweise zu Offline-Schlüsseln für verschlüsselte Leasesets.

Zum Signieren des verschlüsselten Leasesets verwenden wir Red25519, basierend auf [RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf),  
um mit verblendeten Schlüsseln zu signieren und zu verifizieren.  
Die Red25519-Signaturen erfolgen über die Ed25519-Kurve, unter Verwendung von SHA-512 für den Hash.

Red25519 ist identisch mit Standard-Ed25519, außer wie unten spezifiziert.


#### Signier-/Verifizierungsberechnungen

Der äußere Teil des verschlüsselten Leasesets verwendet Red25519-Schlüssel und -Signaturen.

Red25519 ist fast identisch mit Ed25519. Es gibt zwei Unterschiede:

Red25519-privatschlüssel werden aus Zufallszahlen generiert und müssen dann mod L reduziert werden, wobei L wie oben definiert ist.  
Ed25519-privatschlüssel werden aus Zufallszahlen generiert und dann „geklemmt“ unter Verwendung von  
bitweiser Maskierung für Bytes 0 und 31. Dies wird für Red25519 nicht gemacht.  
Die Funktionen GENERATE_ALPHA() und BLIND_PRIVKEY() oben generieren korrekte  
Red25519-privatschlüssel unter Verwendung von mod L.

In Red25519 verwendet die Berechnung von r für die Signatur zusätzliche Zufallsdaten  
und verwendet den öffentlichen Schlüsselwert statt des Hashes des privaten Schlüssels.  
Aufgrund der Zufallsdaten ist jede Red25519-Signatur unterschiedlich, selbst  
wenn dieselben Daten mit demselben Schlüssel signiert werden.

Signieren:

```text
T = 80 Zufallsbytes
  r = H*(T || publickey || message)
  // Rest ist identisch mit Ed25519
```

Verifizieren:

```text
// identisch mit Ed25519
```


### Verschlüsselung und Verarbeitung

#### Ableitung von Subcredentials
Als Teil des Verblendungsprozesses müssen wir sicherstellen, dass ein verschlüsseltes LS2 nur von jemandem entschlüsselt werden kann, der den entsprechenden Signatur-öffentlichen Schlüssel des Ziels kennt. Das vollständige Ziel ist nicht erforderlich.  
Um dies zu erreichen, leiten wir ein Credential vom Signatur-öffentlichen Schlüssel ab:

```text
A = Signatur-öffentlicher Schlüssel des Ziels
  stA = Sig-Typ von A, 2 Bytes Big Endian (0x0007 oder 0x000b)
  stA' = Sig-Typ von A', 2 Bytes Big Endian (0x000b)
  keydata = A || stA || stA'
  credential = H("credential", keydata)
```

Die Personalisierungszeichenfolge stellt sicher, dass das Credential nicht mit einem Hash kollidiert, der als DHT-Suchschlüssel verwendet wird, wie z. B. der reine Ziel-Hash.

Für einen gegebenen verblendeten Schlüssel können wir dann ein Subcredential ableiten:

```text
subcredential = H("subcredential", credential || blindedPublicKey)
```

Das Subcredential ist in den unten beschriebenen Schlüsselableitungsprozessen enthalten, was diese Schlüssel an das Wissen des Signatur-öffentlichen Schlüssels des Ziels bindet.

#### Verschlüsselung der Schicht 1
Zuerst wird die Eingabe für den Schlüsselableitungsprozess vorbereitet:

```text
outerInput = subcredential || publishedTimestamp
```

Als Nächstes wird ein zufälliger Salt generiert:

```text
outerSalt = CSRNG(32)
```

Dann wird der Schlüssel abgeleitet, der zum Verschlüsseln der Schicht 1 verwendet wird:

```text
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
  outerKey = keys[0:31]
  outerIV = keys[32:43]
```

Schließlich wird der Klartext der Schicht 1 verschlüsselt und serialisiert:

```text
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```

#### Entschlüsselung der Schicht 1
Der Salt wird aus dem Geheimtext der Schicht 1 geparst:

```text
outerSalt = outerCiphertext[0:31]
```

Dann wird der Schlüssel abgeleitet, der zum Verschlüsseln der Schicht 1 verwendet wurde:

```text
outerInput = subcredential || publishedTimestamp
  keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
  outerKey = keys[0:31]
  outerIV = keys[32:43]
```

Schließlich wird der Geheimtext der Schicht 1 entschlüsselt:

```text
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```

#### Verschlüsselung der Schicht 2
Wenn Client-Autorisierung aktiviert ist, wird ``authCookie`` wie unten beschrieben berechnet.  
Wenn Client-Autorisierung deaktiviert ist, ist ``authCookie`` das null-längige Byte-Array.

Die Verschlüsselung erfolgt ähnlich wie bei Schicht 1:

```text
innerInput = authCookie || subcredential || publishedTimestamp
  innerSalt = CSRNG(32)
  keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
  innerKey = keys[0:31]
  innerIV = keys[32:43]
  innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```

#### Entschlüsselung der Schicht 2
Wenn Client-Autorisierung aktiviert ist, wird ``authCookie`` wie unten beschrieben berechnet.  
Wenn Client-Autorisierung deaktiviert ist, ist ``authCookie`` das null-längige Byte-Array.

Die Entschlüsselung erfolgt ähnlich wie bei Schicht 1:

```text
innerInput = authCookie || subcredential || publishedTimestamp
  innerSalt = innerCiphertext[0:31]
  keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
  innerKey = keys[0:31]
  innerIV = keys[32:43]
  innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```


### Pro-Client-Autorisierung

Wenn Client-Autorisierung für ein Ziel aktiviert ist, verwaltet der Server eine Liste von Clients, die autorisiert sind, die verschlüsselten LS2-Daten zu entschlüsseln. Die pro Client gespeicherten Daten hängen vom Autorisierungsmechanismus ab und enthalten eine Form von Schlüsselmaterial, das jeder Client generiert und über einen sicheren Out-of-Band-Mechanismus an den Server sendet.

Es gibt zwei Alternativen zur Implementierung der pro-Client-Autorisierung:

#### DH-Client-Autorisierung
Jeder Client generiert ein DH-Schlüsselpaar ``[csk_i, cpk_i]`` und sendet den öffentlichen Schlüssel ``cpk_i`` an den Server.

Serververarbeitung
^^^^^^^^^^^^^^^^^
Der Server generiert ein neues ``authCookie`` und ein temporäres DH-Schlüsselpaar:

```text
authCookie = CSRNG(32)
  esk = GENERATE_PRIVATE()
  epk = DERIVE_PUBLIC(esk)
```

Dann verschlüsselt der Server für jeden autorisierten Client das ``authCookie`` mit dessen öffentlichem Schlüssel:

```text
sharedSecret = DH(esk, cpk_i)
  authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
  okm = HKDF(epk, authInput, "ELS2_XCA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
  clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```

Der Server platziert jedes ``[clientID_i, clientCookie_i]``-Tupel in Schicht 1 des verschlüsselten LS2 zusammen mit ``epk``.

Clientverarbeitung
^^^^^^^^^^^^^^^^^
Der Client verwendet seinen privaten Schlüssel, um seinen erwarteten Client-Bezeichner ``clientID_i``, Verschlüsselungsschlüssel ``clientKey_i`` und Verschlüsselungs-IV ``clientIV_i`` abzuleiten:

```text
sharedSecret = DH(csk_i, epk)
  authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
  okm = HKDF(epk, authInput, "ELS2_XCA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
```

Dann sucht der Client in den Autorisierungsdaten der Schicht 1 nach einem Eintrag, der ``clientID_i`` enthält. Wenn ein passender Eintrag existiert, entschlüsselt der Client ihn, um ``authCookie`` zu erhalten:

```text
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```

#### Vorabgeteilter-Schlüssel-Client-Autorisierung
Jeder Client generiert einen geheimen 32-Byte-Schlüssel ``psk_i`` und sendet ihn an den Server. Alternativ kann der Server den geheimen Schlüssel generieren und an einen oder mehrere Clients senden.

Serververarbeitung
^^^^^^^^^^^^^^^^^
Der Server generiert ein neues ``authCookie`` und einen Salt:

```text
authCookie = CSRNG(32)
  authSalt = CSRNG(32)
```

Dann verschlüsselt der Server für jeden autorisierten Client das ``authCookie`` mit dessen vorabgeteiltem Schlüssel:

```text
authInput = psk_i || subcredential || publishedTimestamp
  okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
  clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```

Der Server platziert jedes ``[clientID_i, clientCookie_i]``-Tupel in Schicht 1 des verschlüsselten LS2 zusammen mit ``authSalt``.

Clientverarbeitung
^^^^^^^^^^^^^^^^^
Der Client verwendet seinen vorabgeteilten Schlüssel, um seinen erwarteten Client-Bezeichner ``clientID_i``, Verschlüsselungsschlüssel ``clientKey_i`` und Verschlüsselungs-IV ``clientIV_i`` abzuleiten:

```text
authInput = psk_i || subcredential || publishedTimestamp
  okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
```

Dann sucht der Client in den Autorisierungsdaten der Schicht 1 nach einem Eintrag, der ``clientID_i`` enthält. Wenn ein passender Eintrag existiert, entschlüsselt der Client ihn, um ``authCookie`` zu erhalten:

```text
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```

#### Sicherheitsüberlegungen
Beide oben genannten Client-Autorisierungsmechanismen bieten Privatsphäre für die Client-Mitgliedschaft. Eine Entität, die nur das Ziel kennt, kann sehen, wie viele Clients zu einem Zeitpunkt abonniert sind, kann aber nicht verfolgen, welche Clients hinzugefügt oder widerrufen werden.

Server SOLLTEN die Reihenfolge der Clients bei jeder Generierung eines verschlüsselten LS2 zufällig machen, um zu verhindern, dass Clients ihre Position in der Liste erfahren und ableiten, wann andere Clients hinzugefügt oder widerrufen wurden.

Ein Server KANN wählen, die Anzahl der abonnierten Clients zu verbergen, indem er zufällige Einträge in die Liste der Autorisierungsdaten einfügt.

Vorteile der DH-Client-Autorisierung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Die Sicherheit des Schemas hängt nicht ausschließlich vom Out-of-Band-Austausch des Client-Schlüsselmaterials ab. Der private Schlüssel des Clients muss niemals sein Gerät verlassen, und daher kann ein Angreifer, der den Out-of-Band-Austausch abfangen kann, aber den DH-Algorithmus nicht brechen kann, das verschlüsselte LS2 nicht entschlüsseln oder bestimmen, wie lange dem Client Zugriff gewährt wird.

Nachteile der DH-Client-Autorisierung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Erfordert N + 1 DH-Operationen auf der Serverseite für N Clients.
- Erfordert eine DH-Operation auf der Clientseite.
- Erfordert, dass der Client den geheimen Schlüssel generiert.

Vorteile der PSK-Client-Autorisierung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Erfordert keine DH-Operationen.
- Ermöglicht dem Server, den geheimen Schlüssel zu generieren.
- Ermöglicht dem Server, denselben Schlüssel mit mehreren Clients zu teilen, wenn gewünscht.

Nachteile der PSK-Client-Autorisierung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Die Sicherheit des Schemas hängt kritisch vom Out-of-Band-Austausch des Client-Schlüsselmaterials ab. Ein Angreifer, der den Austausch für einen bestimmten Client abfängt, kann jedes nachfolgende verschlüsselte LS2 entschlüsseln, für das dieser Client autorisiert ist, sowie bestimmen, wann der Zugriff des Clients widerrufen wird.


### Verschlüsseltes LS mit Base 32-Adressen

Siehe Vorschlag 149.

Sie können kein verschlüsseltes LS2 für BitTorrent verwenden, wegen der kompakten Ankündigung-Antworten, die 32 Bytes sind.  
Die 32 Bytes enthalten nur den Hash. Es ist kein Platz für eine Angabe, dass das Leaseset verschlüsselt ist, oder für die Signaturtypen.


### Verschlüsseltes LS mit Offline-Schlüsseln

Für verschlüsselte Leasesets mit Offline-Schlüsseln müssen auch die verblendeten privaten Schlüssel offline generiert werden, einer für jeden Tag.

Da der optionale Offline-Signaturblock im Klartextteil des verschlüsselten Leasesets ist, könnte jemand, der Floodfills durchsucht, dies verwenden, um das Leaseset (aber nicht zu entschlüsseln) über mehrere Tage zu verfolgen.  
Um dies zu verhindern, sollte der Eigentümer der Schlüssel auch neue transiente Schlüssel für jeden Tag generieren.  
Sowohl die transienten als auch die verblendeten Schlüssel können im Voraus generiert und dem Router in einem Batch zur Verfügung gestellt werden.

Es ist in diesem Vorschlag kein Dateiformat definiert, um mehrere transiente und verblendete Schlüssel zu verpacken und dem Client oder Router zur Verfügung zu stellen.  
Es ist in diesem Vorschlag keine I2CP-Protokollerweiterung definiert, um verschlüsselte Leasesets mit Offline-Schlüsseln zu unterstützen.


### Hinweise

- Ein Dienst, der verschlüsselte Leasesets verwendet, würde die verschlüsselte Version an die Floodfills veröffentlichen. Aus Effizienzgründen würde er jedoch unverschlüsselte Leasesets an Clients in der umhüllten Garlic-Nachricht senden, sobald authentifiziert (z. B. über eine Whitelist).

- Floodfills können die maximale Größe auf einen vernünftigen Wert begrenzen, um Missbrauch zu verhindern.

- Nach der Entschlüsselung sollten mehrere Prüfungen durchgeführt werden, einschließlich, dass der innere Zeitstempel und Ablauf mit denen auf der obersten Ebene übereinstimmen.

- ChaCha20 wurde gegenüber AES ausgewählt. Während die Geschwindigkeiten ähnlich sind, wenn AES-Hardwareunterstützung verfügbar ist, ist ChaCha20 2,5-3x schneller, wenn keine AES-Hardwareunterstützung verfügbar ist, wie z. B. auf Low-End-ARM-Geräten.

- Wir kümmern uns nicht genug um Geschwindigkeit, um BLAKE2b mit Schlüssel zu verwenden. Es hat eine Ausgabegröße, die groß genug ist, um die größte n zu akkommodieren, die wir benötigen (oder wir können es einmal pro gewünschten Schlüssel mit einem Zählerargument aufrufen). BLAKE2b ist viel schneller als SHA-256, und BLAKE2b mit Schlüssel würde die Gesamtanzahl der Hashfunktionsaufrufe reduzieren. Allerdings siehe Vorschlag 148, wo vorgeschlagen wird, dass wir aus anderen Gründen zu BLAKE2b wechseln. Siehe [Secure key derivation performance](https://www.lvh.io/posts/secure-key-derivation-performance.html).


### Meta LS2

Dies wird verwendet, um Multihoming zu ersetzen. Wie jedes Leaseset wird dies vom Ersteller signiert. Dies ist eine authentifizierte Liste von Ziel-Hashes.

Das Meta LS2 ist die Spitze und möglicherweise Zwischenknoten einer Baumstruktur.  
Es enthält eine Anzahl von Einträgen, die jeweils auf ein LS, LS2 oder ein anderes Meta LS2 verweisen, um massives Multihoming zu unterstützen.  
Ein Meta LS2 kann eine Mischung aus LS-, LS2- und Meta-LS2-Einträgen enthalten.  
Die Blätter des Baums sind immer ein LS oder LS2.  
Der Baum ist ein DAG; Schleifen sind verboten; Clients, die Suchen durchführen, müssen Schleifen erkennen und deren Folge verweigern.

Ein Meta LS2 kann eine viel längere Ablaufzeit als ein Standard-LS oder LS2 haben.  
Die oberste Ebene kann eine Ablaufzeit mehrere Stunden nach dem Veröffentlichungsdatum haben.  
Die maximale Ablaufzeit wird von Floodfills und Clients durchgesetzt und ist TBD.

Der Anwendungsfall für Meta LS2 ist massives Multihoming, aber ohne mehr Schutz vor Korrelation von Routern zu Leasesets (beim Neustart des Routers) als derzeit mit LS oder LS2 bereitgestellt wird.  
Dies entspricht dem „Facebook“-Anwendungsfall, der wahrscheinlich keinen Korrelationsschutz benötigt. Dieser Anwendungsfall benötigt wahrscheinlich Offline-Schlüssel, die im Standard-Header an jedem Knoten des Baums bereitgestellt werden.

Das Backend-Protokoll zur Koordination zwischen den Blattroutern, Zwischen- und Master-Meta-LS-Unterzeichnern ist hier nicht spezifiziert. Die Anforderungen sind extrem einfach – nur prüfen, ob der Peer online ist, und alle paar Stunden ein neues LS veröffentlichen. Die einzige Komplexität besteht darin, neue Publisher für die Meta-LS auf oberster oder Zwischenebene bei Ausfall auszuwählen.

Misch-und-Match-Leasesets, bei denen Leases von mehreren Routern kombiniert, signiert und in einem einzigen Leaseset veröffentlicht werden, sind im Vorschlag 140, „unsichtbares Multihoming“, dokumentiert.  
Dieser Vorschlag ist so, wie er geschrieben ist, nicht durchführbar, weil Streaming-Verbindungen nicht „sticky“ zu einem einzelnen Router wären, siehe http://zzz.i2p/topics/2335 .

Das Backend-Protokoll und die Interaktion mit Router- und Client-Internas wäre für unsichtbares Multihoming sehr komplex.

Um Überlastung des Floodfills für das Meta-LS auf oberster Ebene zu vermeiden, sollte die Ablaufzeit mindestens mehrere Stunden betragen. Clients müssen das Meta-LS auf oberster Ebene zwischenspeichern und es bei Nichtablauf über Neustarts hinweg beibehalten.

Wir müssen einen Algorithmus definieren, damit Clients den Baum durchlaufen, einschließlich Fallbacks, damit die Nutzung verteilt ist. Eine Funktion von Hash-Abstand, Kosten und Zufälligkeit. Wenn ein Knoten sowohl LS oder LS2 als auch Meta LS hat, müssen wir wissen, wann diese Leasesets verwendet werden dürfen und wann der Baum weiter durchlaufen werden muss.

Abfrage mit  
    Standard-LS-Flag (1)  
Speichern mit  
    Meta LS2-Typ (7)  
Speichern unter  
    Hash des Ziels  
    Dieser Hash wird dann verwendet, um den täglichen „Routing-Key“ zu generieren, wie bei LS1  
Typischer Ablauf  
    Stunden. Max. 18,2 Stunden (65535 Sekunden)  
Veröffentlicht von  
    „Master“-Ziel oder Koordinator oder Zwischenkoordinatoren

### Format

```
Standard-LS2-Header wie oben spezifiziert

  Meta-LS2-Typspezifischer Teil
  - Eigenschaften (Mapping wie in der Spezifikation gemeinsamer Strukturen, 2 Null-Bytes, wenn keine)
  - Anzahl der Einträge (1 Byte) Maximum TBD
  - Einträge. Jeder Eintrag enthält: (40 Bytes)
    - Hash (32 Bytes)
    - Flags (2 Bytes)
      TBD. Zur Kompatibilität mit zukünftigen Verwendungen alle auf Null setzen.
    - Typ (1 Byte) Der Typ des LS, auf das verwiesen wird;
      1 für LS, 3 für LS2, 5 für verschlüsselt, 7 für Meta, 0 für unbekannt.
    - Kosten (Priorität) (1 Byte)
    - Ablauf (4 Bytes) (4 Bytes, Big Endian, Sekunden seit Epoche, Überlauf im Jahr 2106)
  - Anzahl der Widerrufe (1 Byte) Maximum TBD
  - Widerrufe: Jeder Widerruf enthält: (32 Bytes)
    - Hash (32 Bytes)

  Standard-LS2-Signatur:
  - Signatur (40+ Bytes)
    Die Signatur bezieht sich auf alles oben.
```

Flags und Eigenschaften: für zukünftige Verwendung


### Hinweise

- Ein verteilter Dienst, der dies verwendet, hätte einen oder mehrere „Master“ mit dem privaten Schlüssel des Dienstziels. Sie würden (außerhalb des Bandes) die aktuelle Liste der aktiven Ziele bestimmen und das Meta LS2 veröffentlichen. Zur Redundanz könnten mehrere Master das Meta LS2 multihomen (d. h. gleichzeitig veröffentlichen).

- Ein verteilter Dienst könnte mit einem einzelnen Ziel beginnen oder altes Multihoming verwenden und dann zu einem Meta LS2 übergehen. Eine Standard-LS-Abfrage könnte jedes der LS, LS2 oder Meta LS2 zurückgeben.

- Wenn ein Dienst ein Meta LS2 verwendet, hat er keine Tunnel (Leases).


### Dienst-Eintrag

Dies ist ein einzelner Eintrag, der besagt, dass ein Ziel an einem Dienst teilnimmt. Er wird vom Teilnehmer an den Floodfill gesendet. Er wird niemals einzeln von einem Floodfill gesendet, sondern nur als Teil einer Dienst-Liste. Der Dienst-Eintrag wird auch verwendet, um die Teilnahme an einem Dienst zu widerrufen, indem der Ablauf auf Null gesetzt wird.

Dies ist kein LS2, aber es verwendet das Standard-LS2-Header- und Signaturformat.

Abfrage mit  
    n/a, siehe Dienst-Liste  
Speichern mit  
    Dienst-Eintrag-Typ (9)  
Speichern unter  
    Hash des Dienstnamens  
    Dieser Hash wird dann verwendet, um den täglichen „Routing-Key“ zu generieren, wie bei LS1  
Typischer Ablauf  
    Stunden. Max. 18,2 Stunden (65535 Sekunden)  
Veröffentlicht von  
    Ziel

### Format

```
Standard-LS2-Header wie oben spezifiziert

  Dienst-Eintrag-Typspezifischer Teil
  - Port (2 Bytes, Big Endian) (0, wenn nicht angegeben)
  - Hash des Dienstnamens (32 Bytes)

  Standard-LS2-Signatur:
  - Signatur (40+ Bytes)
    Die Signatur bezieht sich auf alles oben.
```

### Hinweise

- Wenn Ablauf alle Nullen ist, sollte der Floodfill den Eintrag widerrufen und ihn nicht länger in der Dienst-Liste enthalten.

- Speicherung: Der Floodfill kann die Speicherung dieser Einträge streng drosseln und die Anzahl der gespeicherten Einträge pro Hash und deren Ablauf begrenzen. Eine Whitelist von Hashes kann ebenfalls verwendet werden.

- Jeder andere NetDB-Typ am selben Hash hat Priorität, daher kann ein Dienst-Eintrag niemals ein LS/RI überschreiben, aber ein LS/RI wird alle Dienst-Einträge an diesem Hash überschreiben.


### Dienst-Liste

Dies ähnelt keinem LS2 und verwendet ein anderes Format.

Die Dienst-Liste wird vom Floodfill erstellt und signiert. Sie ist nicht authentifiziert, da jeder durch Veröffentlichung eines Dienst-Eintr
