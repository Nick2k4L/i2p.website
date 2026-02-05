---
title: "SSU2 Spezifikation"
description: "Secure Semi-Reliable UDP Transport Protocol Version 2"
slug: "ssu2"
category: "Transports"
lastUpdated: "2025-04"
accurateFor: "0.9.65"
---

## Status

Im Wesentlichen vollständig. Siehe [Prop159](/proposals/159-ssu2) für zusätzliche Hintergrundinformationen und Ziele, einschließlich Sicherheitsanalyse, Bedrohungsmodelle, eine Überprüfung der SSU 1 Sicherheit und Probleme sowie Auszüge aus den QUIC-Spezifikationen.

Rollout-Plan:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Feature</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Testing (not default)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Enabled by default</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Local test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-03</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test in-net</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze basic protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Basic Session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address Validation (Retry)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Fragmented RI in handshake</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze extended protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Enable for random 2%</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Validation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Connection Migration</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Immediate ACK flag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Key Rotation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2023-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (i2pd)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (Java I2P)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.61 2023-12</td></tr>
  </tbody>
</table>
Die Basis-Session umfasst die Handshake- und Datenphase. Das erweiterte Protokoll umfasst Relay und Peer-Test.

## Überblick

Diese Spezifikation definiert ein authentifiziertes Schlüsselvereinbarungsprotokoll zur Verbesserung der Widerstandsfähigkeit von [SSU](/docs/transport/ssu) gegen verschiedene Formen automatisierter Identifizierung und Angriffe.

Wie bei anderen I2P-Transportprotokollen ist SSU2 für den Punkt-zu-Punkt-Transport (router-zu-router) von I2NP-Nachrichten definiert. Es ist keine Allzweck-Datenleitung. Wie [SSU](/docs/transport/ssu) bietet es auch zwei zusätzliche Dienste: Weiterleitung für NAT-Traversierung und Peer Testing zur Bestimmung der eingehenden Erreichbarkeit. Es bietet außerdem einen dritten Dienst, der nicht in SSU vorhanden ist, für Verbindungsmigration, wenn ein Peer die IP-Adresse oder den Port wechselt.

## Design-Übersicht

### Zusammenfassung

Wir stützen uns auf mehrere bestehende Protokolle, sowohl innerhalb von I2P als auch auf externe Standards, für Inspiration, Anleitung und Code-Wiederverwendung:

- Bedrohungsmodelle: Aus NTCP2 [NTCP2](/docs/specs/ntcp2), mit zusätzlichen erheblichen Bedrohungen, die für UDP-Transport relevant sind, wie von QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001) analysiert.
- Kryptographische Auswahl: Aus [NTCP2](/docs/specs/ntcp2).
- Handshake: Noise XK aus [NTCP2](/docs/specs/ntcp2) und [NOISE](https://noiseprotocol.org/noise.html). Erhebliche Vereinfachungen zu NTCP2 sind aufgrund der von UDP bereitgestellten Kapselung (inhärente Nachrichtengrenzen) möglich.
- Handshake Ephemeral Key Obfuscation: Angepasst von [NTCP2](/docs/specs/ntcp2), aber mit ChaCha20 aus [ECIES](/docs/specs/ecies) anstelle von AES.
- Paket-Header: Angepasst von WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) und QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Paket-Header-Verschleierung: Angepasst von [NTCP2](/docs/specs/ntcp2), aber mit ChaCha20 aus [ECIES](/docs/specs/ecies) anstelle von AES.
- Paket-Header-Schutz: Angepasst von QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) und [Nonces](https://eprint.iacr.org/2019/624.pdf)
- Header als AEAD-zugehörige Daten verwendet wie in [ECIES](/docs/specs/ecies).
- Paketnummerierung: Angepasst von WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) und QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Nachrichten: Angepasst von [SSU](/docs/transport/ssu)
- I2NP-Fragmentierung: Angepasst von [SSU](/docs/transport/ssu)
- Relay und Peer-Tests: Angepasst von [SSU](/docs/transport/ssu)
- Signaturen von Relay- und Peer-Test-Daten: Aus der allgemeinen Strukturspezifikation [Common](/docs/specs/common-structures)
- Block-Format: Aus [NTCP2](/docs/specs/ntcp2) und [ECIES](/docs/specs/ecies).
- Padding und Optionen: Aus [NTCP2](/docs/specs/ntcp2) und [ECIES](/docs/specs/ecies).
- Acks, Nacks: Angepasst von QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000).
- Flusskontrolle: Noch zu bestimmen

Es gibt keine neuen kryptographischen Primitive, die nicht bereits zuvor in I2P verwendet wurden.

### Zustellungsgarantien

Wie bei anderen I2P-Transportprotokollen NTCP, NTCP2 und SSU 1 ist auch dieser Transport keine allgemeine Einrichtung für die Übertragung eines geordneten Byte-Streams. Er ist für den Transport von I2NP-Nachrichten konzipiert. Es wird keine "Stream"-Abstraktion bereitgestellt.

Darüber hinaus enthält es, wie bei SSU, zusätzliche Funktionen für peer-unterstützte NAT-Durchquerung und Tests der Erreichbarkeit (eingehende Verbindungen).

Wie bei SSU 1 bietet es KEINE geordnete Zustellung von I2NP-Nachrichten. Es bietet auch keine garantierte Zustellung von I2NP-Nachrichten. Aus Effizienzgründen oder aufgrund der ungeordneten Zustellung von UDP-Datagrammen oder dem Verlust dieser Datagramme können I2NP-Nachrichten am Zielort ungeordnet zugestellt werden oder überhaupt nicht ankommen. Eine I2NP-Nachricht kann bei Bedarf mehrfach erneut übertragen werden, aber die Zustellung kann letztendlich fehlschlagen, ohne dass die gesamte Verbindung getrennt wird. Außerdem können neue I2NP-Nachrichten weiterhin gesendet werden, auch während für andere I2NP-Nachrichten eine erneute Übertragung (Verlustwiederherstellung) stattfindet.

Dieses Protokoll verhindert NICHT vollständig die doppelte Zustellung von I2NP-Nachrichten. Der router sollte die I2NP-Ablaufzeit durchsetzen und einen Bloom-Filter oder einen anderen Mechanismus verwenden, der auf der I2NP-Nachrichten-ID basiert. Siehe den Abschnitt "I2NP Message Duplication" unten.

### Noise Protocol Framework

Diese Spezifikation stellt die Anforderungen basierend auf dem Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (Revision 33, 2017-10-04) bereit. Noise hat ähnliche Eigenschaften wie das Station-To-Station-Protokoll [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol), welches die Grundlage für das [SSU](/docs/transport/ssu)-Protokoll bildet. In der Noise-Terminologie ist Alice der Initiator und Bob der Responder.

SSU2 basiert auf dem Noise-Protokoll Noise_XK_25519_ChaChaPoly_SHA256. (Der tatsächliche Bezeichner für die anfängliche Schlüsselableitungsfunktion ist "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256" um I2P-Erweiterungen anzuzeigen - siehe KDF 1 Abschnitt unten)

HINWEIS: Diese Kennung unterscheidet sich von der für NTCP2 verwendeten, da alle drei Handshake-Nachrichten den Header als zugehörige Daten verwenden.

Dieses Noise-Protokoll verwendet die folgenden Primitive:

- Handshake Pattern: XK Alice übermittelt ihren Schlüssel an Bob (X) Alice kennt bereits Bobs statischen Schlüssel (K)
- DH Function: X25519 X25519 DH mit einer Schlüssellänge von 32 Bytes wie in [RFC-7748](https://tools.ietf.org/html/rfc7748) spezifiziert.
- Cipher Function: ChaChaPoly AEAD_CHACHA20_POLY1305 wie in [RFC-7539](https://tools.ietf.org/html/rfc7539) Abschnitt 2.8 spezifiziert. 12-Byte-Nonce, wobei die ersten 4 Bytes auf null gesetzt sind.
- Hash Function: SHA256 Standard-32-Byte-Hash, bereits umfangreich in I2P verwendet.

### Ergänzungen zum Framework

Diese Spezifikation definiert die folgenden Verbesserungen für Noise_XK_25519_ChaChaPoly_SHA256. Diese folgen im Allgemeinen den Richtlinien in [NOISE](https://noiseprotocol.org/noise.html) Abschnitt 13.

1) Handshake-Nachrichten (Session Request, Created, Confirmed) enthalten einen 16 oder 32 Byte Header. 2) Die Header für die Handshake-Nachrichten (Session Request, Created, Confirmed) werden als Eingabe für mixHash() vor der Verschlüsselung/Entschlüsselung verwendet, um die Header an die Nachricht zu binden. 3) Header werden verschlüsselt und geschützt. 4) Klartext-ephemerale Schlüssel werden mit ChaCha20-Verschlüsselung unter Verwendung eines bekannten Schlüssels und IV verschleiert. Dies ist schneller als elligator2. 5) Das Payload-Format ist für Nachrichten 1, 2 und die Datenphase definiert. Dies ist natürlich nicht in Noise definiert.

Die Datenphase verwendet eine Verschlüsselung, die ähnlich, aber nicht kompatibel mit der Noise-Datenphase ist.

## Definitionen

Wir definieren die folgenden Funktionen, die den verwendeten kryptographischen Bausteinen entsprechen.

ZEROLEN

:   Byte-Array der Länge null

H(p, d)

:   SHA-256 Hash-Funktion, die eine Personalisierungszeichenfolge p und Daten d entgegennimmt und eine Ausgabe der Länge 32 Bytes erzeugt. Wie definiert in [NOISE](https://noiseprotocol.org/noise.html). || unten bedeutet anhängen.

    Use SHA-256 as follows:

        H(p, d) := SHA-256(p || d)

MixHash(d)

:   SHA-256 Hash-Funktion, die einen vorherigen Hash h und neue Daten d nimmt und eine Ausgabe von 32 Bytes Länge produziert. || bedeutet unten anhängen.

    Use SHA-256 as follows:

        MixHash(d) := h = SHA-256(h || d)

STREAM

:   Das ChaCha20/Poly1305 AEAD wie in [RFC-7539](https://tools.ietf.org/html/rfc7539) spezifiziert. S_KEY_LEN = 32 und S_IV_LEN = 12.

    ENCRYPT(k, n, plaintext, ad)

    :   Encrypts plaintext using the cipher key k, and nonce n which MUST be unique for the key k. Associated data ad is optional. Returns a ciphertext that is the size of the plaintext + 16 bytes for the HMAC.

        The entire ciphertext must be indistinguishable from random if the key is secret.

    DECRYPT(k, n, ciphertext, ad)

    :   Decrypts ciphertext using the cipher key k, and nonce n. Associated data ad is optional. Returns the plaintext.

DH

:   X25519 Public-Key-Vereinbarungssystem. Private Schlüssel von 32 Bytes, öffentliche Schlüssel von 32 Bytes, erzeugt Ausgaben von 32 Bytes. Es hat die folgenden Funktionen:

    GENERATE_PRIVATE()

    :   Generates a new private key.

    DERIVE_PUBLIC(privkey)

    :   Returns the public key corresponding to the given private key.

    DH(privkey, pubkey)

    :   Generates a shared secret from the given private and public keys.

HKDF(salt, ikm, info, n)

:   Eine kryptographische Schlüsselableitungsfunktion, die Eingabeschlüsselmaterial ikm (das eine gute Entropie haben sollte, aber nicht zwingend eine gleichmäßig zufällige Zeichenkette sein muss), ein Salt mit einer Länge von 32 Bytes und einen kontextspezifischen 'info'-Wert entgegennimmt und eine Ausgabe von n Bytes erzeugt, die als Schlüsselmaterial geeignet ist.

    Use HKDF as specified in [RFC-5869](https://tools.ietf.org/html/rfc5869), using the HMAC hash function SHA-256 as specified in [RFC-2104](https://tools.ietf.org/html/rfc2104). This means that SALT_LEN is 32 bytes max.

MixKey(d)

:   Verwende HKDF() mit einem vorherigen chainKey und neuen Daten d, und setze den neuen chainKey und k. Wie in [NOISE](https://noiseprotocol.org/noise.html) definiert.

    Use HKDF as follows:

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]

## Nachrichten

Jedes UDP-Datagramm enthält genau eine Nachricht. Die Länge des Datagramms (nach den IP- und UDP-Headern) entspricht der Länge der Nachricht. Padding, falls vorhanden, ist in einem Padding-Block innerhalb der Nachricht enthalten. In diesem Dokument verwenden wir die Begriffe "Datagramm" und "Paket" größtenteils synonym. Jedes Datagramm (oder Paket) enthält eine einzelne Nachricht (im Gegensatz zu QUIC, wo ein Datagramm mehrere QUIC-Pakete enthalten kann). Der "Paket-Header" ist der Teil nach dem IP/UDP-Header.

Ausnahme: Die Session Confirmed-Nachricht ist insofern einzigartig, als sie über mehrere Pakete fragmentiert werden kann. Weitere Informationen finden Sie im Abschnitt Session Confirmed Fragmentation weiter unten.

Alle SSU2-Nachrichten sind mindestens 40 Bytes lang. Jede Nachricht mit einer Länge von 1-39 Bytes ist ungültig. Alle SSU2-Nachrichten sind kleiner oder gleich 1472 (IPv4) oder 1452 (IPv6) Bytes lang. Das Nachrichtenformat basiert auf Noise-Nachrichten, mit Modifikationen für Framing und Ununterscheidbarkeit. Implementierungen, die Standard-Noise-Bibliotheken verwenden, müssen empfangene Nachrichten zum Standard-Noise-Nachrichtenformat vorverarbeiten. Alle verschlüsselten Felder sind AEAD-Chiffretexte.

Die folgenden Nachrichten sind definiert:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Encr. Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionRequest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionCreated</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionConfirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">PeerTest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">HolePunch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
  </tbody>
</table>
### Session-Erstellung

Die Standard-Aufbausequenz, wenn Alice ein gültiges Token besitzt, das sie zuvor von Bob erhalten hat, ist wie folgt:

```
Alice Bob

SessionRequest -------------------> <------------------- SessionCreated SessionConfirmed ----------------->
```
Wenn Alice kein gültiges Token hat, ist die Einrichtungssequenz wie folgt:

```
Alice Bob

TokenRequest ---------------------> <--------------------------- Retry SessionRequest -------------------> <------------------- SessionCreated SessionConfirmed ----------------->
```
Wenn Alice denkt, dass sie einen gültigen Token hat, aber Bob ihn ablehnt (vielleicht weil Bob neu gestartet wurde), ist die Verbindungsaufbau-Sequenz wie folgt:

```
Alice Bob

SessionRequest -------------------> <--------------------------- Retry SessionRequest -------------------> <------------------- SessionCreated SessionConfirmed ----------------->
```
Bob kann eine Session- oder Token-Anfrage ablehnen, indem er mit einer Retry-Nachricht antwortet, die einen Termination-Block mit einem Grund-Code enthält. Basierend auf dem Grund-Code sollte Alice für eine gewisse Zeit keine weitere Anfrage versuchen:

```
Alice Bob

SessionRequest -------------------> <--------------------------- Retry containing a Termination block

or

TokenRequest ---------------------> <--------------------------- Retry containing a Termination block
```
Mit der Noise-Terminologie ist die Aufbau- und Datensequenz wie folgt: (Payload Security Properties)

```
XK(s, rs): Authentication Confidentiality

<- s \... -> e, es 0 2 <- e, ee 2 1 -> s, se 2 5 <- 2 5
```
Sobald eine Sitzung etabliert wurde, können Alice und Bob Data-Nachrichten austauschen.

### Paket-Header

Alle Pakete beginnen mit einem verschleierten (verschlüsselten) Header. Es gibt zwei Header-Typen, lang und kurz. Beachten Sie, dass die ersten 13 Bytes (Destination Connection ID, Paketnummer und Typ) für alle Header gleich sind.

#### Langer Header

Der lange Header ist 32 Bytes groß. Er wird vor der Erstellung einer Sitzung verwendet, für Token Request, SessionRequest, SessionCreated und Retry. Er wird auch für sitzungslose Peer Test und Hole Punch Nachrichten verwendet.

Vor der Header-Verschlüsselung:

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-------------------------------------------+----------+----------+----------+----------+
    | > Packet Number                           | type     | ver      | id       | flag     |
    +-------------------------------------------+----------+----------+----------+----------+
    | > Source Connection ID                                                                |
    +---------------------------------------------------------------------------------------+
    | > Token                                                                               |
    +---------------------------------------------------------------------------------------+

    Destination Connection ID :: 8 bytes, unsigned big endian integer

    Packet Number :: 4 bytes, unsigned big endian integer

    type :: The message type = 0, 1, 7, 9, 10, or 11

    ver :: The protocol version, equal to 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Source Connection ID :: 8 bytes, unsigned big endian integer

    Token :: 8 bytes, unsigned big endian integer
```
#### Kurzer Header

Der kurze Header ist 16 Bytes lang. Er wird für Session Created und für Data-Nachrichten verwendet. Nicht authentifizierte Nachrichten wie Session Request, Retry und Peer Test verwenden immer den langen Header.

16 Bytes sind erforderlich, da der Empfänger die ersten 16 Bytes entschlüsseln muss, um den Nachrichtentyp zu erhalten, und dann weitere 16 Bytes entschlüsseln muss, wenn es sich tatsächlich um einen langen Header handelt, wie durch den Nachrichtentyp angezeigt.

Für Session Confirmed, vor der Header-Verschlüsselung:

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-----------------------------------+------+------+-------------+
    | > Packet Number                   | type | frag | > flags     |
    +-----------------------------------+------+------+-------------+

    Destination Connection ID :: 8 bytes, unsigned big endian integer

    Packet Number :: 4 bytes, all zeros

    type :: The message type = 2

    frag :: 1 byte fragment info:

    :   bit order: 76543210 (bit 7 is MSB) bits 7-4: fragment number 0-14, big endian bits 3-0: total fragments 1-15, big endian

    flags :: 2 bytes, unused, set to 0 for future compatibility
```
Siehe den Abschnitt "Session Confirmed Fragmentation" weiter unten für weitere Informationen über das frag-Feld.

Für Data-Nachrichten, vor der Header-Verschlüsselung:

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-----------------------------------+------+------+---------------+
    | > Packet Number                   | type | flag | moreflags     |
    +-----------------------------------+------+------+---------------+

    Destination Connection ID :: 8 bytes, unsigned big endian integer

    Packet Number :: 4 bytes, unsigned big endian integer

    type :: The message type = 6

    flag :: 1 byte flags:

    :   bit order: 76543210 (bit 7 is MSB) bits 7-1: unused, set to 0 for future compatibility bits 0: when set to 1, immediate ack requested

    moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### Verbindungs-ID-Nummerierung

Verbindungs-IDs müssen zufällig generiert werden. Quell- und Ziel-IDs dürfen NICHT identisch sein, damit ein Angreifer im Übertragungsweg kein Paket abfangen und an den Absender zurücksenden kann, das gültig aussieht. Verwenden Sie KEINEN Zähler zur Generierung von Verbindungs-IDs, damit ein Angreifer im Übertragungsweg kein Paket generieren kann, das gültig aussieht.

Anders als bei QUIC ändern wir die Verbindungs-IDs weder während noch nach dem Handshake, auch nicht nach einer Retry-Nachricht. Die IDs bleiben konstant von der ersten Nachricht (Token Request oder Session Request) bis zur letzten Nachricht (Data with Termination). Zusätzlich ändern sich die Verbindungs-IDs nicht während oder nach einer Path Challenge oder Connection Migration.

Auch anders als bei QUIC ist, dass Verbindungs-IDs in den Headern immer header-verschlüsselt sind. Siehe unten.

#### Paketnummerierung

Wenn kein First Packet Number Block im Handshake gesendet wird, werden Pakete innerhalb einer einzelnen Sitzung für jede Richtung nummeriert, beginnend bei 0 bis zu einem Maximum von (2**32 -1). Eine Sitzung muss beendet und eine neue Sitzung erstellt werden, deutlich bevor die maximale Anzahl von Paketen gesendet wird.

Wenn ein First Packet Number Block während des Handshakes gesendet wird, werden Pakete innerhalb einer einzelnen Session für diese Richtung ab dieser Paketnummer nummeriert. Die Paketnummer kann während der Session umlaufen. Wenn maximal 2**32 Pakete gesendet wurden und die Paketnummer wieder zur ersten Paketnummer zurückspringt, ist diese Session nicht mehr gültig. Eine Session muss beendet und eine neue Session erstellt werden, deutlich bevor die maximale Anzahl von Paketen gesendet wird.

TODO Schlüsselrotation, maximale Paketnummer reduzieren?

Handshake-Pakete, die als verloren erkannt werden, werden vollständig retransmittiert, mit dem identischen Header einschließlich der Paketnummer. Die Handshake-Nachrichten Session Request, Session Created und Session Confirmed MÜSSEN mit derselben Paketnummer und identischem verschlüsselten Inhalt retransmittiert werden, damit derselbe verkettete Hash zur Verschlüsselung der Antwort verwendet wird. Die Retry-Nachricht wird niemals übertragen.

Datenphasenpakete, die als verloren eingestuft werden, werden niemals vollständig erneut übertragen (außer bei Beendigung, siehe unten). Das Gleiche gilt für die Blöcke, die in verlorenen Paketen enthalten sind. Stattdessen werden die Informationen, die möglicherweise in Blöcken enthalten sind, bei Bedarf erneut in neuen Paketen gesendet. Datenpakete werden niemals mit derselben Paketnummer erneut übertragen. Jede erneute Übertragung von Paketinhalten (unabhängig davon, ob der Inhalt gleich bleibt oder nicht) muss die nächste unbenutzte Paketnummer verwenden.

Das unveränderte Weiterleiten eines ganzen Pakets in unveränderter Form mit derselben Paketnummer ist aus mehreren Gründen nicht erlaubt. Für Hintergrundinformationen siehe QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) Abschnitt 12.3.

- Es ist ineffizient, Pakete für die Neuübertragung zu speichern
- Ein neues Paket sieht für einen Beobachter im Übertragungsweg anders aus, kann nicht erkennen, dass es erneut übertragen wurde
- Ein neues Paket erhält einen aktualisierten ack-Block, nicht den alten ack-Block
- Sie übertragen nur das Nötige erneut. Einige Fragmente könnten bereits einmal erneut übertragen und bestätigt worden sein
- Sie können so viel wie nötig in jedes erneut übertragene Paket packen, wenn mehr aussteht
- Endpunkte, die alle einzelnen Pakete zum Zweck der Duplikatserkennung verfolgen, riskieren eine übermäßige Zustandsanhäufung. Die für die Duplikatserkennung erforderlichen Daten können begrenzt werden, indem eine minimale Paketnummer aufrechterhalten wird, unter der alle Pakete sofort verworfen werden.
- Dieses Schema ist viel flexibler

Neue Pakete werden verwendet, um Informationen zu übertragen, die als verloren gegangen bestimmt wurden. Im Allgemeinen werden Informationen erneut gesendet, wenn ein Paket mit diesen Informationen als verloren bestimmt wird, und das Senden wird beendet, wenn ein Paket mit diesen Informationen bestätigt wird.

Ausnahme: Ein Datenphase-Paket, das einen Termination-Block enthält, kann, muss aber nicht, vollständig und unverändert erneut übertragen werden. Siehe den Abschnitt "Session Termination" unten.

Die folgenden Pakete enthalten eine zufällige Paketnummer, die ignoriert wird:

- Session Request
- Session Created
- Token Request
- Retry
- Peer Test
- Hole Punch

Für Alice beginnt die ausgehende Paketnummerierung bei 0 mit Session Confirmed. Für Bob beginnt die ausgehende Paketnummerierung bei 0 mit dem ersten Data-Paket, welches eine ACK der Session Confirmed sein sollte. Die Paketnummern in einem beispielhaften Standard-Handshake werden sein:

```
Alice Bob

SessionRequest (r) ------------> <------------- SessionCreated (r) SessionConfirmed (0) ------------> <------------- Data (0) (Ack-only) Data (1) ------------> (May be sent before Ack is received) <------------- Data (1) Data (2) ------------> Data (3) ------------> Data (4) ------------> <------------- Data (2)

r = random packet number (ignored) Token Request, Retry, and Peer Test also have random packet numbers.
```
Jede Neuübertragung von Handshake-Nachrichten (SessionRequest, SessionCreated oder SessionConfirmed) muss unverändert mit derselben Paketnummer erneut gesendet werden. Verwenden Sie keine anderen ephemeren Schlüssel und ändern Sie nicht die Nutzdaten beim erneuten Senden dieser Nachrichten.

#### Header-Bindung

Der Header (vor Verschleierung und Schutz) ist immer in den zugehörigen Daten für die AEAD-Funktion enthalten, um den Header kryptographisch an die Daten zu binden.

#### Header-Verschlüsselung

Header-Verschlüsselung hat mehrere Ziele. Siehe den Abschnitt "Zusätzliche DPI-Diskussion" oben für Hintergrund und Annahmen.

- Online-DPI daran hindern, das Protokoll zu identifizieren
- Muster in einer Serie von Nachrichten in derselben Verbindung verhindern, außer bei Handshake-Wiederübertragungen
- Muster in Nachrichten desselben Typs in verschiedenen Verbindungen verhindern
- Entschlüsselung von Handshake-Headern ohne Kenntnis des introduction key aus der netDb verhindern
- Identifizierung von X25519 ephemeral keys ohne Kenntnis des introduction key aus der netDb verhindern
- Entschlüsselung der Paketnummer und des Typs von Data-Phase-Paketen durch jeden Online- oder Offline-Angreifer verhindern
- Einschleusung gültiger Handshake-Pakete durch einen On-Path- oder Off-Path-Beobachter ohne Kenntnis des introduction key aus der netDb verhindern
- Einschleusung gültiger Datenpakete durch einen On-Path- oder Off-Path-Beobachter verhindern
- Schnelle und effiziente Klassifizierung eingehender Pakete ermöglichen
- "Probing"-Resistenz bieten, sodass es keine Antwort auf eine schlechte Session Request gibt, oder falls es eine Retry-Antwort gibt, die Antwort ohne Kenntnis des introduction key aus der netDb nicht als I2P identifizierbar ist
- Die Destination Connection ID sind keine kritischen Daten, und es ist in Ordnung, wenn sie von einem Beobachter mit Kenntnis des introduction key aus der netDb entschlüsselt werden können
- Die Paketnummer eines Data-Phase-Pakets ist eine AEAD-Nonce und stellt kritische Daten dar. Sie darf nicht von einem Beobachter entschlüsselbar sein, selbst nicht mit Kenntnis des introduction key aus der netDb. Siehe [Nonces](https://eprint.iacr.org/2019/624.pdf).

Header werden mit bekannten Schlüsseln verschlüsselt, die in der netDb veröffentlicht oder später berechnet werden. In der Handshake-Phase dient dies nur der DPI-Resistenz, da der Schlüssel öffentlich ist und Schlüssel und Nonces wiederverwendet werden, sodass es effektiv nur Verschleierung ist. Beachten Sie, dass die Header-Verschlüsselung auch verwendet wird, um die ephemeren Schlüssel X (in Session Request) und Y (in Session Created) zu verschleiern.

Siehe den Abschnitt "Inbound Packet Handling" unten für weitere Anleitungen.

Die Bytes 0-15 aller Header werden mit einem Header-Schutzschema verschlüsselt, indem sie mit Daten XOR-verknüpft werden, die aus bekannten Schlüsseln berechnet wurden, unter Verwendung von ChaCha20, ähnlich wie bei QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) und [Nonces](https://eprint.iacr.org/2019/624.pdf). Dies stellt sicher, dass der verschlüsselte kurze Header und der erste Teil des langen Headers zufällig erscheinen.

Für Session Request und Session Created werden die Bytes 16-31 des langen Headers und der 32-Byte Noise ephemeral key mit ChaCha20 verschlüsselt. Die unverschlüsselten Daten sind zufällig, daher erscheinen die verschlüsselten Daten ebenfalls zufällig.

Für Retry werden die Bytes 16-31 des langen Headers mit ChaCha20 verschlüsselt. Die unverschlüsselten Daten sind zufällig, daher erscheinen die verschlüsselten Daten ebenfalls zufällig.

Im Gegensatz zum QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) Header-Schutzschema werden ALLE Teile aller Header, einschließlich Ziel- und Quell-Verbindungs-IDs, verschlüsselt. QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) und [Nonces](https://eprint.iacr.org/2019/624.pdf) konzentrieren sich hauptsächlich auf die Verschlüsselung des "kritischen" Teils des Headers, d.h. der Paketnummer (ChaCha20 nonce). Obwohl die Verschlüsselung der Session-ID die Klassifizierung eingehender Pakete etwas komplexer macht, erschwert sie bestimmte Angriffe. QUIC definiert verschiedene Verbindungs-IDs für verschiedene Phasen und für Path-Challenge und Verbindungsmigration. Hier verwenden wir durchgehend dieselben Verbindungs-IDs, da sie verschlüsselt sind.

Es gibt sieben Header-Schutzschlüssel-Phasen:

- Session Request und Token Request
- Session Created
- Retry
- Session Confirmed
- Data Phase
- Peer Test
- Hole Punch

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_1</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_2</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Request KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Created KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice/Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See data phase KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 5,7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Hole Punch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
  </tbody>
</table>
Header-Verschlüsselung ist darauf ausgelegt, eine schnelle Klassifizierung eingehender Pakete zu ermöglichen, ohne komplexe Heuristiken oder Fallback-Mechanismen. Dies wird erreicht, indem derselbe k_header_1 Schlüssel für fast alle eingehenden Nachrichten verwendet wird. Selbst wenn sich die Quell-IP oder der Port einer Verbindung aufgrund einer tatsächlichen IP-Änderung oder NAT-Verhaltens ändert, kann das Paket schnell einer Session zugeordnet werden durch eine einzige Suche der Verbindungs-ID.

Beachten Sie, dass Session Created und Retry die EINZIGEN Nachrichten sind, die eine Fallback-Verarbeitung für k_header_1 benötigen, um die Connection ID zu entschlüsseln, da sie den intro key des Absenders (Bob) verwenden. ALLE anderen Nachrichten verwenden den intro key des Empfängers für k_header_1. Die Fallback-Verarbeitung muss nur ausstehende ausgehende Verbindungen anhand der Quell-IP/Port nachschlagen.

Wenn die Fallback-Verarbeitung nach Quell-IP/Port keine ausstehende ausgehende Verbindung finden kann, könnte es mehrere Ursachen geben:

- Keine SSU2-Nachricht
- Eine beschädigte SSU2-Nachricht
- Die Antwort ist gefälscht oder von einem Angreifer modifiziert
- Bob hat ein symmetrisches NAT
- Bob hat während der Verarbeitung der Nachricht die IP oder den Port gewechselt
- Bob hat die Antwort über eine andere Schnittstelle gesendet

Während zusätzliche Fallback-Verarbeitung möglich ist, um zu versuchen, die ausstehende ausgehende Verbindung zu finden und die Verbindungs-ID mit dem k_header_1 für diese Verbindung zu entschlüsseln, ist dies wahrscheinlich nicht notwendig. Wenn Bob Probleme mit seinem NAT oder Paket-Routing hat, ist es wahrscheinlich besser, die Verbindung fehlschlagen zu lassen. Dieses Design setzt darauf, dass Endpunkte eine stabile Adresse für die Dauer des Handshakes beibehalten.

Siehe den Abschnitt zur Behandlung eingehender Pakete unten für weitere Richtlinien.

Siehe die einzelnen KDF-Abschnitte unten für die Ableitung der Header-Verschlüsselungsschlüssel für diese Phase.

#### Header-Verschlüsselung KDF

```
// incoming encrypted packet

packet = incoming encrypted packet len = packet.length

    // take the next-to-last 12 bytes of the packet iv = packet[len-24:len-13] k_header_1 = header encryption key 1 data = {0, 0, 0, 0, 0, 0, 0, 0} mask = ChaCha20.encrypt(k_header_1, iv, data)

    // encrypt the first part of the header by XORing with the mask packet[0:7] \^= mask[0:7]

    // take the last 12 bytes of the packet iv = packet[len-12:len-1] k_header_2 = header encryption key 2 data = {0, 0, 0, 0, 0, 0, 0, 0} mask = ChaCha20.encrypt(k_header_2, iv, data)

    // encrypt the second part of the header by XORing with the mask packet[8:15] \^= mask[0:7]

    // For Session Request and Session Created only: iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

    // encrypt the third part of the header and the ephemeral key packet[16:63] = ChaCha20.encrypt(k_header_2, iv, packet[16:63])

    // For Retry, Token Request, Peer Test, and Hole Punch only: iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

    // encrypt the third part of the header packet[16:31] = ChaCha20.encrypt(k_header_2, iv, packet[16:31])
```
Diese KDF verwendet die letzten 24 Bytes des Pakets als IV für die beiden ChaCha20-Operationen. Da alle Pakete mit einem 16-Byte-MAC enden, erfordert dies, dass alle Paket-Payloads mindestens 8 Bytes groß sind. Diese Anforderung ist zusätzlich in den nachfolgenden Nachrichtensektionen dokumentiert.

#### Header-Validierung

Nach der Entschlüsselung der ersten 8 Bytes des Headers kennt der Empfänger die Destination Connection ID. Von da an weiß der Empfänger, welchen Header-Verschlüsselungsschlüssel er für den Rest des Headers verwenden muss, basierend auf der Schlüsselphase der Sitzung.

Die Entschlüsselung der nächsten 8 Bytes des Headers wird dann den Nachrichtentyp preisgeben und es ermöglichen zu bestimmen, ob es sich um einen kurzen oder langen Header handelt. Wenn es ein langer Header ist, muss der Empfänger die Versions- und netid-Felder validieren. Wenn die Version != 2 ist oder die netid != dem erwarteten Wert entspricht (normalerweise 2, außer in Testnetzwerken), sollte der Empfänger die Nachricht verwerfen.

### Paketintegrität

Alle Nachrichten enthalten entweder drei oder vier Teile:

- Der Nachrichten-Header
- Nur für Session Request und Session Created, ein ephemerer Schlüssel
- Eine ChaCha20-verschlüsselte Nutzlast
- Ein Poly1305 MAC

In allen Fällen ist der Header (und falls vorhanden, der ephemeral key) an den Authentifizierungs-MAC gebunden, um sicherzustellen, dass die gesamte Nachricht unversehrt ist.

- Für Handshake-Nachrichten Session Request, Session Created und Session Confirmed wird der Nachrichten-Header vor der Noise-Verarbeitungsphase mixHash()ed
- Der ephemere Schlüssel, falls vorhanden, wird von einem Standard-Noise mixHash() abgedeckt
- Für Nachrichten außerhalb des Noise-Handshakes wird der Header als Associated Data für die ChaCha20/Poly1305-Verschlüsselung verwendet.

Eingehende Paket-Handler müssen immer die ChaCha20-Nutzlast entschlüsseln und den MAC validieren, bevor sie die Nachricht verarbeiten, mit einer Ausnahme: Um DoS-Angriffe von adress-gespoften Paketen abzumildern, die scheinbare Session Request-Nachrichten mit einem ungültigen Token enthalten, muss ein Handler NICHT versuchen, die vollständige Nachricht zu entschlüsseln und zu validieren (was zusätzlich zur ChaCha20/Poly1305-Entschlüsselung eine teure DH-Operation erfordert). Der Handler kann mit einer Retry-Nachricht antworten, wobei er die im Header der Session Request-Nachricht gefundenen Werte verwendet.

### Authentifizierte Verschlüsselung

Es gibt drei separate authentifizierte Verschlüsselungsinstanzen (CipherStates). Eine während der Handshake-Phase und zwei (Senden und Empfangen) für die Datenphase. Jede hat ihren eigenen Schlüssel aus einer KDF.

Verschlüsselte/authentifizierte Daten werden dargestellt als

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | Encrypted and authenticated data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+
```
#### ChaCha20/Poly1305

Verschlüsseltes und authentifiziertes Datenformat.

Eingaben für die Verschlüsselungs-/Entschlüsselungsfunktionen:

```
k :: 32 byte cipher key, as generated from KDF


nonce :: Counter-based nonce, 12 bytes.

Starts at 0 and incremented for each message. First four bytes are always zero. Last eight bytes are the counter, little-endian encoded. Maximum value is 2**64 - 2. Connection must be dropped and restarted after it reaches that value. The value 2**64 - 1 must never be sent.

ad :: In handshake phase:

Associated data, 32 bytes. The SHA256 hash of all preceding data. In data phase: The packet header, 16 bytes.

data :: Plaintext data, 0 or more bytes
```
Ausgabe der Verschlüsselungsfunktion, Eingabe der Entschlüsselungsfunktion:

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | ChaCha20 encrypted data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | Poly1305 Message Authentication Code | + (MAC) + | 16 bytes | +----+----+----+----+----+----+----+----+

    encrypted data :: Same size as plaintext data, 0 - 65519 bytes

    MAC :: Poly1305 message authentication code, 16 bytes
```
Für ChaCha20 entspricht das hier Beschriebene [RFC-7539](https://tools.ietf.org/html/rfc7539), welches auch ähnlich in TLS [RFC-7905](https://tools.ietf.org/html/rfc7905) verwendet wird.

#### Notizen

- Da ChaCha20 ein Stream-Cipher ist, müssen Klartexte nicht aufgefüllt werden. Zusätzliche Keystream-Bytes werden verworfen.
- Der Schlüssel für die Verschlüsselung (256 Bits) wird mittels der SHA256 KDF vereinbart. Die Details der KDF für jede Nachricht sind in separaten Abschnitten unten aufgeführt.

#### AEAD-Fehlerbehandlung

- Bei allen Nachrichten ist die AEAD-Nachrichtengröße im Voraus bekannt. Bei einem AEAD-Authentifizierungsfehler muss der Empfänger die weitere Nachrichtenverarbeitung stoppen und die Nachricht verwerfen.
- Bob sollte eine Blacklist von IPs mit wiederholten Fehlern führen.

### KDF für Session Request

Die Key Derivation Function (KDF) generiert einen handshake-Phasen-Chiffrierschlüssel k aus dem DH-Ergebnis, unter Verwendung von HMAC-SHA256(key, data) wie in [RFC-2104](https://tools.ietf.org/html/rfc2104) definiert. Dies sind die Funktionen InitializeSymmetric(), MixHash() und MixKey(), genau wie in der Noise-Spezifikation definiert.

#### KDF für initialen ChainKey

```
// Define protocol_name.


    Set protocol_name = "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256"

    :   (52 bytes, US-ASCII encoded, no NULL termination).

    // Define Hash h = 32 bytes h = SHA256(protocol_name);

    Define ck = 32 byte chaining key. Copy the h data to ck. Set ck = h

    // MixHash(null prologue) h = SHA256(h);

    // up until here, can all be precalculated by Alice for all outgoing connections

    // Bob's X25519 static keys // bpk is published in routerinfo bsk = GENERATE_PRIVATE() bpk = DERIVE_PUBLIC(bsk)

    // Bob static key // MixHash(bpk) // || below means append h = SHA256(h || bpk);

    // Bob introduction key // bik is published in routerinfo bik = RANDOM(32)

    // up until here, can all be precalculated by Bob for all incoming connections
```
#### KDF für Session Request

```
// MixHash(header)

h = SHA256(h || header)

    This is the "e" message pattern:

    // Alice's X25519 ephemeral keys aesk = GENERATE_PRIVATE() aepk = DERIVE_PUBLIC(aesk)

    // Alice ephemeral key X // MixHash(aepk) h = SHA256(h || aepk);

    // h is used as the associated data for the AEAD in Session Request // Retain the Hash h for the Session Created KDF

    End of "e" message pattern.

    This is the "es" message pattern:

    // DH(e, rs) == DH(s, re) sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

    // MixKey(DH()) //[chainKey, k] = MixKey(sharedSecret) // ChaChaPoly parameters to encrypt/decrypt keydata = HKDF(chainKey, sharedSecret, "", 64) chainKey = keydata[0:31]

    // AEAD parameters k = keydata[32:63] n = 0 ad = h ciphertext = ENCRYPT(k, n, payload, ad)

    // retain the chainKey for Session Created KDF

    End of "es" message pattern.

    // Header encryption keys for this message // bik = Bob's intro key k_header_1 = bik k_header_2 = bik

    // Header encryption keys for next message (Session Created) k_header_1 = bik k_header_2 = HKDF(chainKey, ZEROLEN, "SessCreateHeader", 32)

    // Header encryption keys for next message (Retry) k_header_1 = bik k_header_2 = bik
```
### SessionRequest (Typ 0)

Alice sendet an Bob, entweder als erste Nachricht im Handshake oder als Antwort auf eine Retry-Nachricht. Bob antwortet mit einer Session Created-Nachricht. Größe: 80 + Payload-Größe. Mindestgröße: 88

Wenn Alice kein gültiges Token besitzt, sollte Alice eine Token Request-Nachricht anstelle einer Session Request senden, um den Overhead der asymmetrischen Verschlüsselung bei der Generierung einer Session Request zu vermeiden.

Langer Header. Noise-Inhalt: Alices ephemerer Schlüssel X Noise-Nutzlast: DateTime und andere Blöcke Maximale Nutzlastgröße: MTU - 108 (IPv4) oder MTU - 128 (IPv6). Für 1280 MTU: Maximale Nutzlast ist 1172 (IPv4) oder 1152 (IPv6). Für 1500 MTU: Maximale Nutzlast ist 1392 (IPv4) oder 1372 (IPv6).

Payload-Sicherheitseigenschaften:

```
XK(s, rs): Authentication Confidentiality

-> e, es 0 2

    Authentication: None (0). This payload may have been sent by any party, including an active attacker.

    Confidentiality: 2. Encryption to a known recipient, forward secrecy for sender compromise only, vulnerable to replay. This payload is encrypted based only on DHs involving the recipient's static key pair. If the recipient's static private key is compromised, even at a later date, this payload can be decrypted. This message can also be replayed, since there's no ephemeral contribution from the recipient.

    "e": Alice generates a new ephemeral key pair and stores it in the e

    :   variable, writes the ephemeral public key as cleartext into the message buffer, and hashes the public key along with the old h to derive a new h.

    "es": A DH is performed between the Alice's ephemeral key pair and the

    :   Bob's static key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Der X-Wert wird verschlüsselt, um Payload-Ununterscheidbarkeit und Eindeutigkeit sicherzustellen, welche notwendige DPI-Gegenmaßnahmen sind. Wir verwenden ChaCha20-Verschlüsselung, um dies zu erreichen, anstatt komplexerer und langsamerer Alternativen wie elligator2. Asymmetrische Verschlüsselung mit Bobs router-öffentlichem Schlüssel wäre viel zu langsam. ChaCha20-Verschlüsselung verwendet Bobs Intro-Schlüssel, wie er in der netDb veröffentlicht ist.

ChaCha20-Verschlüsselung dient nur der DPI-Resistenz. Jede Partei, die Bobs introduction key kennt, welcher in der Netzwerkdatenbank veröffentlicht ist, kann den Header und X-Wert in dieser Nachricht entschlüsseln.

Rohe Inhalte:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Bob intro key + | See Header Encryption KDF | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Bob intro key n=0 + | | +----+----+----+----+----+----+----+----+ | | + X, ChaCha20 encrypted + | with Bob intro key n=0 | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | k defined in KDF for Session Request | + n = 0 + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+

    X :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian

    :   key: Bob's intro key n: 1 data: 48 bytes (bytes 16-31 of the header, followed by encrypted X)
```
Unverschlüsselte Daten (Poly1305-Authentifizierungs-Tag nicht angezeigt):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-----------------------------------------------+-----------+-----------+-----------+-----------+
    | > Packet Number                               | type      | ver       | id        | flag      |
    +-----------------------------------------------+-----------+-----------+-----------+-----------+
    | > Source Connection ID                                                                        |
    +-----------------------------------------------------------------------------------------------+
    | > Token                                                                                       |
    +-----------------------------------------------------------------------------------------------+
    | > X (32 bytes)                                                                                |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    +-----------------------------------------------------------------------------------------------+
    | >                                                                                             |
    | >                                                                                             |
    | > Noise payload (block data)                                                                  |
    | >                                                                                             |
    | > :   (length varies)                                                                         |
    | >                                                                                             |
    | > see below for allowed blocks                                                                |
    |                                                                                               |
    |                                                                                               |
    +-----------------------------------------------------------------------------------------------+

    Destination Connection ID :: Randomly generated by Alice

    id :: 1 byte, the network ID (currently 2, except for test networks)

    ver :: 2

    type :: 0

    flag :: 1 byte, unused, set to 0 for future compatibility

    Packet Number :: Random 4 byte number generated by Alice, ignored

    Source Connection ID :: Randomly generated by Alice,

    :   must not be equal to Destination Connection ID

    Token :: 0 if not previously received from Bob

    X :: 32 bytes, X25519 ephemeral key, little endian
```
#### Nutzlast

- DateTime Block
- Options Block (optional)
- Relay Tag Request Block (optional)
- Padding Block (optional)

Die minimale Payload-Größe beträgt 8 Bytes. Da der DateTime-Block nur 7 Bytes groß ist, muss mindestens ein weiterer Block vorhanden sein.

#### Hinweise

- Der eindeutige X-Wert im anfänglichen ChaCha20-Block stellt sicher, dass der verschlüsselte Text für jede Sitzung unterschiedlich ist.
- Um Widerstand gegen Probing zu bieten, sollte Bob keine Retry-Nachricht als Antwort auf eine Session Request-Nachricht senden, es sei denn, die Felder für Nachrichtentyp, Protokollversion und Netzwerk-ID in der Session Request-Nachricht sind gültig.
- Bob muss Verbindungen ablehnen, bei denen der Zeitstempel-Wert zu weit von der aktuellen Zeit abweicht. Nennen wir die maximale Delta-Zeit "D". Bob muss einen lokalen Cache von zuvor verwendeten Handshake-Werten führen und Duplikate ablehnen, um Replay-Angriffe zu verhindern. Werte im Cache müssen eine Lebensdauer von mindestens 2*D haben. Die Cache-Werte sind implementierungsabhängig, jedoch kann der 32-Byte X-Wert (oder sein verschlüsseltes Äquivalent) verwendet werden. Ablehnung durch Senden einer Retry-Nachricht mit einem Null-Token und einem Termination-Block.
- Diffie-Hellman-Ephemeral-Schlüssel dürfen niemals wiederverwendet werden, um kryptographische Angriffe zu verhindern, und eine Wiederverwendung wird als Replay-Angriff abgelehnt.
- Die "KE"- und "auth"-Optionen müssen kompatibel sein, d.h. das geteilte Geheimnis K muss die angemessene Größe haben. Wenn weitere "auth"-Optionen hinzugefügt werden, könnte dies implizit die Bedeutung des "KE"-Flags ändern, um eine andere KDF oder eine andere Abschneidungsgröße zu verwenden.
- Bob muss validieren, dass Alices Ephemeral-Schlüssel ein gültiger Punkt auf der Kurve ist.
- Padding sollte auf eine vernünftige Menge begrenzt werden. Bob kann Verbindungen mit exzessivem Padding ablehnen. Bob wird seine Padding-Optionen in Session Created angeben. Min/Max-Richtlinien noch zu bestimmen. Zufällige Größe von 0 bis 31 Bytes mindestens? (Verteilung noch zu bestimmen, siehe Anhang A.)
- Bei den meisten Fehlern, einschließlich AEAD, DH, scheinbarem Replay oder Schlüsselvalidierungsfehlern, sollte Bob die weitere Nachrichtenverarbeitung stoppen und die Nachricht ohne Antwort verwerfen.
- Bob KANN eine Retry-Nachricht mit einem Null-Token und einem Termination-Block mit einem Clock Skew-Grund-Code senden, wenn der Zeitstempel im DateTime-Block zu stark abweicht.
- DoS-Minderung: DH ist eine relativ teure Operation. Wie beim vorherigen NTCP-Protokoll sollten router alle notwendigen Maßnahmen ergreifen, um CPU- oder Verbindungserschöpfung zu verhindern. Grenzen für maximale aktive Verbindungen und maximale laufende Verbindungsaufbauten festlegen. Lese-Timeouts durchsetzen (sowohl pro Lesevorgang als auch insgesamt für "Slowloris"). Wiederholte oder gleichzeitige Verbindungen von derselben Quelle begrenzen. Blacklists für Quellen führen, die wiederholt fehlschlagen. Nicht auf AEAD-Fehler antworten. Alternativ mit einer Retry-Nachricht vor der DH-Operation und AEAD-Validierung antworten.
- "ver"-Feld: Das gesamte Noise-Protokoll, Erweiterungen und SSU2-Protokoll einschließlich Payload-Spezifikationen, die SSU2 anzeigen. Dieses Feld kann verwendet werden, um Unterstützung für zukünftige Änderungen anzuzeigen.
- Das Netzwerk-ID-Feld wird verwendet, um netzwerkübergreifende Verbindungen schnell zu identifizieren. Wenn dieses Feld nicht mit Bobs Netzwerk-ID übereinstimmt, sollte Bob die Verbindung trennen und zukünftige Verbindungen blockieren.
- Bob muss die Nachricht verwerfen, wenn die Source Connection ID der Destination Connection ID entspricht.

### KDF für Session Created und Session Confirmed Teil 1

```
// take h saved from Session Request KDF

// MixHash(ciphertext) h = SHA256(h || encrypted Noise payload from Session Request)

    // MixHash(header) h = SHA256(h || header)

    This is the "e" message pattern:

    // Bob's X25519 ephemeral keys besk = GENERATE_PRIVATE() bepk = DERIVE_PUBLIC(besk)

    // h is from KDF for Session Request // Bob ephemeral key Y // MixHash(bepk) h = SHA256(h || bepk);

    // h is used as the associated data for the AEAD in Session Created // Retain the Hash h for the Session Confirmed KDF

    End of "e" message pattern.

    This is the "ee" message pattern:

    // MixKey(DH()) //[chainKey, k] = MixKey(sharedSecret) sharedSecret = DH(aesk, bepk) = DH(besk, aepk) keydata = HKDF(chainKey, sharedSecret, "", 64) chainKey = keydata[0:31]

    // AEAD parameters k = keydata[32:63] n = 0 ad = h ciphertext = ENCRYPT(k, n, payload, ad)

    // retain the chaining key ck for Session Confirmed KDF

    End of "ee" message pattern.

    // Header encryption keys for this message // bik = Bob's intro key k_header_1 = bik k_header_2: See Session Request KDF above

    // Header protection keys for next message (Session Confirmed) k_header_1 = bik k_header_2 = HKDF(chainKey, ZEROLEN, "SessionConfirmed", 32)
```
### SessionCreated (Typ 1)

Bob sendet an Alice, als Antwort auf eine Session Request Nachricht. Alice antwortet mit einer Session Confirmed Nachricht. Größe: 80 + Payload-Größe. Mindestgröße: 88

Noise-Inhalt: Bobs ephemerer Schlüssel Y Noise-Payload: DateTime, Address und andere Blöcke Maximale Payload-Größe: MTU - 108 (IPv4) oder MTU - 128 (IPv6). Für 1280 MTU: Maximaler Payload ist 1172 (IPv4) oder 1152 (IPv6). Für 1500 MTU: Maximaler Payload ist 1392 (IPv4) oder 1372 (IPv6).

Payload-Sicherheitseigenschaften:

```
XK(s, rs): Authentication Confidentiality

<- e, ee 2 1

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 1. Encryption to an ephemeral recipient. This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee"). However, the sender has not authenticated the recipient, so this payload might be sent to any party, including an active attacker.

    "e": Bob generates a new ephemeral key pair and stores it in the e variable, writes the ephemeral public key as cleartext into the message buffer, and hashes the public key along with the old h to derive a new h.

    "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Der Y-Wert wird verschlüsselt, um die Ununterscheidbarkeit und Einzigartigkeit der Payload zu gewährleisten, was notwendige DPI-Gegenmaßnahmen sind. Wir verwenden ChaCha20-Verschlüsselung, um dies zu erreichen, anstatt komplexerer und langsamerer Alternativen wie elligator2. Asymmetrische Verschlüsselung mit Alice's router public key wäre viel zu langsam. Die ChaCha20-Verschlüsselung verwendet Bob's Intro-Schlüssel, wie er in der netDb veröffentlicht ist.

ChaCha20-Verschlüsselung dient nur der DPI-Resistenz. Jede Partei, die Bobs Intro-Schlüssel kennt, der in der Netzwerkdatenbank veröffentlicht ist, und die ersten 32 Bytes der Session Request erfasst hat, kann den Y-Wert in dieser Nachricht entschlüsseln.

Raw-Inhalte:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Bob intro key and + | derived key, see Header Encryption KDF| +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with derived key n=0 + | See Header Encryption KDF | +----+----+----+----+----+----+----+----+ | | + Y, ChaCha20 encrypted + | with derived key n=0 | + (32 bytes) + | See Header Encryption KDF | + + | | +----+----+----+----+----+----+----+----+ | ChaCha20 data | + Encrypted and authenticated data + | length varies | + k defined in KDF for Session Created + | n = 0; see KDF for associated data | + + | | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+

    Y :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian

    :   key: Bob's intro key n: 1 data: 48 bytes (bytes 16-31 of the header, followed by encrypted Y)
```
Unverschlüsselte Daten (Poly1305 Auth-Tag nicht gezeigt):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-------------------------------------------+----------+----------+----------+----------+
    | > Packet Number                           | type     | ver      | id       | flag     |
    +-------------------------------------------+----------+----------+----------+----------+
    | > Source Connection ID                                                                |
    +---------------------------------------------------------------------------------------+
    | > Token                                                                               |
    +---------------------------------------------------------------------------------------+
    | > Y (32 bytes)                                                                        |
    |                                                                                       |
    |                                                                                       |
    |                                                                                       |
    |                                                                                       |
    |                                                                                       |
    |                                                                                       |
    +---------------------------------------------------------------------------------------+
    | >                                                                                     |
    | >                                                                                     |
    | > Noise payload (block data)                                                          |
    | >                                                                                     |
    | > :   (length varies) see below for allowed blocks                                    |
    |                                                                                       |
    |                                                                                       |
    +---------------------------------------------------------------------------------------+

    Destination Connection ID :: The Source Connection ID

    :   received from Alice in Session Request

    id :: 1 byte, the network ID (currently 2, except for test networks)

    ver :: 2

    type :: 0

    flag :: 1 byte, unused, set to 0 for future compatibility

    Packet Number :: Random 4 byte number generated by Bob, ignored

    Source Connection ID :: The Destination Connection ID

    :   received from Alice in Session Request

    Token :: 0 (unused)

    Y :: 32 bytes, X25519 ephemeral key, little endian
```
#### Nutzlast

- DateTime-Block
- Address-Block
- Relay Tag-Block (optional)
- New Token-Block (nicht empfohlen, siehe Hinweis)
- First Packet Number-Block (optional)
- Options-Block (optional)
- Termination-Block (nicht empfohlen, stattdessen in einer Wiederholungsnachricht senden)
- Padding-Block (optional)

Die minimale Payload-Größe beträgt 8 Bytes. Da die DateTime- und Address-Blöcke zusammen mehr als das ausmachen, wird die Anforderung bereits mit diesen beiden Blöcken erfüllt.

#### Hinweise

- Alice muss hier validieren, dass Bobs ephemerer Schlüssel ein gültiger Punkt auf der Kurve ist.
- Padding sollte auf einen vernünftigen Umfang begrenzt werden. Alice kann Verbindungen mit übermäßigem Padding ablehnen. Alice wird ihre Padding-Optionen in Session Confirmed angeben. Min/Max-Richtlinien noch zu bestimmen. Zufällige Größe von 0 bis 31 Bytes mindestens? (Verteilung noch zu bestimmen, siehe Anhang A.)
- Bei jedem Fehler, einschließlich AEAD, DH, Zeitstempel, offensichtlicher Wiederholung oder Schlüsselvalidierungsfehlern, muss Alice die weitere Nachrichtenverarbeitung stoppen und die Verbindung ohne Antwort schließen.
- Alice muss Verbindungen ablehnen, bei denen der Zeitstempelwert zu weit von der aktuellen Zeit abweicht. Nennen wir die maximale Zeitdifferenz "D". Alice muss einen lokalen Cache von zuvor verwendeten Handshake-Werten pflegen und Duplikate ablehnen, um Replay-Angriffe zu verhindern. Werte im Cache müssen eine Lebensdauer von mindestens 2*D haben. Die Cache-Werte sind implementierungsabhängig, jedoch kann der 32-Byte Y-Wert (oder sein verschlüsseltes Äquivalent) verwendet werden.
- Alice muss die Nachricht verwerfen, wenn die Quell-IP und der Port nicht mit der Ziel-IP und dem Port der Session Request übereinstimmen.
- Alice muss die Nachricht verwerfen, wenn die Destination und Source Connection IDs nicht mit den Source und Destination Connection IDs der Session Request übereinstimmen.
- Bob sendet einen Relay-Tag-Block, falls von Alice in der Session Request angefordert.
- New Token Block wird nicht in Session Created empfohlen, da Bob zuerst die Validierung der Session Confirmed durchführen sollte. Siehe Tokens-Abschnitt unten.

#### Probleme

- Min/Max-Padding-Optionen hier einschließen?

### KDF für Session Confirmed Teil 1, unter Verwendung der Session Created KDF

```
// take h saved from Session Created KDF

// MixHash(ciphertext) h = SHA256(h || encrypted Noise payload from Session Created)

    // MixHash(header) h = SHA256(h || header) // h is used as the associated data for the AEAD in Session Confirmed part 1, below

    This is the "s" message pattern:

    // Alice's X25519 static keys ask = GENERATE_PRIVATE() apk = DERIVE_PUBLIC(ask)

    // AEAD parameters // k is from Session Request n = 1 ad = h ciphertext = ENCRYPT(k, n++, apk, ad)

    // MixHash(ciphertext) h = SHA256(h || ciphertext);

    // h is used as the associated data for the AEAD in Session Confirmed part 2

    End of "s" message pattern.

    // Header encryption keys for this message See Session Confirmed part 2 below
```
### KDF für Session Confirmed Teil 2

```
This is the "se" message pattern:

// DH(ask, bepk) == DH(besk, apk) sharedSecret = DH(ask, bepk) = DH(besk, apk)

// MixKey(DH()) //[chainKey, k] = MixKey(sharedSecret) keydata = HKDF(chainKey, sharedSecret, "", 64) chainKey = keydata[0:31]

// AEAD parameters k = keydata[32:63] n = 0 ad = h ciphertext = ENCRYPT(k, n, payload, ad)

// h from Session Confirmed part 1 is used as the associated data for the AEAD in Session Confirmed part 2 // MixHash(ciphertext) h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF // retain the hash h for the data phase KDF

End of "se" message pattern.

// Header encryption keys for this message // bik = Bob's intro key k_header_1 = bik k_header_2: See Session Created KDF above

// Header protection keys for data phase See data phase KDF below
```
### SessionConfirmed (Typ 2)

Alice sendet an Bob, als Antwort auf eine Session Created-Nachricht. Bob antwortet sofort mit einer Data-Nachricht, die einen ACK-Block enthält. Größe: 80 + Payload-Größe. Mindestgröße: Etwa 500 (minimale Router-Info-Blockgröße beträgt etwa 420 Bytes)

Noise-Inhalt: Alices statischer Schlüssel Noise-Payload Teil 1: Keine Noise-Payload Teil 2: Alices RouterInfo und andere Blöcke Maximale Payload-Größe: MTU - 108 (IPv4) oder MTU - 128 (IPv6). Für 1280 MTU: Maximale Payload ist 1172 (IPv4) oder 1152 (IPv6). Für 1500 MTU: Maximale Payload ist 1392 (IPv4) oder 1372 (IPv6).

Payload-Sicherheitseigenschaften:

```
XK(s, rs): Authentication Confidentiality

-> s, se 2 5

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 5. Encryption to a known recipient, strong forward secrecy. This payload is encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static DH with the recipient's static key pair. Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated by an attacker that has stolen its static private key, this payload cannot be decrypted.

    "s": Alice writes her static public key from the s variable into the message buffer, encrypting it, and hashes the output along with the old h to derive a new h.

    "se": A DH is performed between the Alice's static key pair and the Bob's ephemeral key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Dies enthält zwei ChaChaPoly-Frames. Der erste ist Alices verschlüsselter statischer öffentlicher Schlüssel. Der zweite ist die Noise-Payload: Alices verschlüsselte RouterInfo, optionale Optionen und optionales Padding. Sie verwenden unterschiedliche Schlüssel, da die MixKey()-Funktion dazwischen aufgerufen wird.

Rohe Inhalte:

```
+----+----+----+----+----+----+----+----+

|  Short Header 16 bytes, ChaCha20 |

    + encrypted with Bob intro key and + | derived key, see Header Encryption KDF| +----+----+----+----+----+----+----+----+ | ChaCha20 frame (32 bytes) | + Encrypted and authenticated data + + Alice static key S + | k defined in KDF for Session Created | + n = 1 + | | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+ | | + Length varies (remainder of packet) + | | + ChaChaPoly frame + | Encrypted and authenticated | + see below for allowed blocks + | | + k defined in KDF for + | Session Confirmed part 2 | + n = 0 + | see KDF for associated data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+

    S :: 32 bytes, ChaChaPoly encrypted Alice's X25519 static key, little endian

    :   inside 48 byte ChaChaPoly frame
```
Unverschlüsselte Daten (Poly1305-Authentifizierungstags nicht angezeigt):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+-------------------------+
    | > Packet Number                                   | type       | frag       | > flags                 |
    +---------------------------------------------------+------------+------------+-------------------------+
    | > S Alice static key (32 bytes)                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    Destination Connection ID :: As sent in Session Request,

    :   or one received in Session Confirmed?

    Packet Number :: 0 always, for all fragments, even if retransmitted

    type :: 2

    frag :: 1 byte fragment info:

    :   bit order: 76543210 (bit 7 is MSB) bits 7-4: fragment number 0-14, big endian bits 3-0: total fragments 1-15, big endian

    flags :: 2 bytes, unused, set to 0 for future compatibility

    S :: 32 bytes, Alice's X25519 static key, little endian
```
#### Nutzlast

- RouterInfo-Block (muss der erste Block sein)
- Options-Block (optional)
- New Token-Block (optional)
- Relay Request-Block (optional)
- Peer Test-Block (optional)
- First Packet Number-Block (optional)
- I2NP-, First Fragment- oder Follow-on Fragment-Blöcke (optional, aber wahrscheinlich kein Platz)
- Padding-Block (optional)

Die minimale Payload-Größe beträgt 8 Bytes. Da der RouterInfo-Block deutlich mehr als das sein wird, ist die Anforderung bereits mit diesem Block allein erfüllt.

#### Notizen

- Bob muss die übliche Router Info-Validierung durchführen. Sicherstellen, dass der Signaturtyp unterstützt wird, die Signatur verifizieren, prüfen, dass der Zeitstempel innerhalb der Grenzen liegt, und alle anderen notwendigen Überprüfungen durchführen. Siehe unten für Hinweise zum Umgang mit fragmentierten Router Infos.

- Bob muss überprüfen, dass Alices statischer Schlüssel, der im ersten Frame empfangen wurde, mit dem statischen Schlüssel in der Router Info übereinstimmt. Bob muss zuerst in der Router Info nach einer NTCP- oder SSU2-Router-Adresse mit einer passenden Versions-(v)-Option suchen. Siehe die Abschnitte zu veröffentlichten Router Infos und unveröffentlichten Router Infos unten. Siehe unten für Hinweise zum Umgang mit fragmentierten Router Infos.

- Wenn Bob eine ältere Version von Alices RouterInfo in seiner netDb hat, überprüfe, dass der statische Schlüssel in der router info in beiden gleich ist, falls vorhanden, und falls die ältere Version weniger als XXX alt ist (siehe Schlüsselrotationszeit unten)

- Bob muss hier validieren, dass Alices statischer Schlüssel ein gültiger Punkt auf der Kurve ist.

- Optionen sollten enthalten sein, um Padding-Parameter zu spezifizieren.

- Bei jedem Fehler, einschließlich AEAD-, RI-, DH-, Zeitstempel- oder Schlüsselvalidierungsfehlern, muss Bob die weitere Nachrichtenverarbeitung stoppen und die Verbindung ohne Antwort schließen.

- Message 3 Teil 2 Frame-Inhalt: Das Format dieses Frames ist das gleiche wie das Format der Datenphase-Frames, außer dass die Länge des Frames von Alice in der Session Request gesendet wird. Siehe unten für das Datenphase-Frame-Format. Der Frame muss 1 bis 4 Blöcke in der folgenden Reihenfolge enthalten:

1)  Alice's Router Info Block (erforderlich)   2)  Options Block (optional)   3)  I2NP Blocks (optional)

4\) Padding-Block (optional) Dieser Frame darf niemals einen anderen Block-Typ enthalten. TODO: was ist mit Relay und Peer-Test?

- Message 3 Teil 2 Padding-Block wird empfohlen.

- Es kann keinen Platz oder nur wenig Platz für I2NP-Blöcke geben, abhängig von der MTU und der Router Info-Größe. Fügen Sie KEINE I2NP-Blöcke hinzu, wenn die Router Info fragmentiert ist. Die einfachste Implementierung könnte sein, niemals I2NP-Blöcke in der Session Confirmed-Nachricht einzuschließen und alle I2NP-Blöcke in nachfolgenden Data-Nachrichten zu senden. Siehe Router Info-Block-Abschnitt unten für die maximale Blockgröße.

#### Session Confirmed Fragmentierung

Die Session Confirmed Nachricht muss die vollständige signierte Router Info von Alice enthalten, damit Bob mehrere erforderliche Überprüfungen durchführen kann:

- Der statische Schlüssel "s" im RI stimmt mit dem statischen Schlüssel im Handshake überein
- Der Einführungsschlüssel "i" im RI muss extrahiert und gültig sein, um in der Datenphase verwendet zu werden
- Die RI-Signatur ist gültig

Leider kann die Router Info, selbst wenn sie im RI-Block gzip-komprimiert ist, die MTU überschreiten. Daher kann die Session Confirmed über zwei oder mehr Pakete fragmentiert werden. Dies ist der EINZIGE Fall im SSU2-Protokoll, bei dem eine AEAD-geschützte Nutzlast über zwei oder mehr Pakete fragmentiert wird.

Die Header für jedes Paket werden wie folgt konstruiert:

- ALLE Header sind kurze Header mit derselben Paketnummer 0
- ALLE Header enthalten ein "frag"-Feld mit der Fragmentnummer und der Gesamtzahl der Fragmente
- Der unverschlüsselte Header von Fragment 0 ist die zugehörigen Daten (AD) für die "Jumbo"-Nachricht
- Jeder Header wird mit den letzten 24 Bytes der Daten in DIESEM Paket verschlüsselt

Erstellen Sie die Paketreihe wie folgt:

- Erstelle einen einzelnen RI-Block (Fragment 0 von 1 im RI-Block-Frag-Feld). Wir verwenden keine RI-Block-Fragmentierung, das war für eine alternative Methode zur Lösung desselben Problems.
- Erstelle eine "Jumbo"-Payload mit dem RI-Block und allen anderen einzuschließenden Blöcken
- Berechne die Gesamtdatengröße (ohne Header), die der Payload-Größe + 64 Bytes für den statischen Schlüssel und zwei MACs entspricht
- Berechne den verfügbaren Platz in jedem Paket, das ist die MTU minus IP-Header (20 oder 40), minus UDP-Header (8), minus SSU2-Short-Header (16). Gesamter Overhead pro Paket beträgt 44 (IPv4) oder 64 (IPv6).
- Berechne die Anzahl der Pakete.
- Berechne die Größe der Daten im letzten Paket. Sie muss größer oder gleich 24 Bytes sein, damit die Header-Verschlüsselung funktioniert. Wenn sie zu klein ist, entweder einen Padding-Block hinzufügen, ODER die Größe des Padding-Blocks vergrößern falls bereits vorhanden, ODER die Größe eines der anderen Pakete reduzieren, sodass das letzte Paket groß genug wird.
- Erstelle den unverschlüsselten Header für das erste Paket, mit der Gesamtzahl der Fragmente im Frag-Feld, und verschlüssle die "Jumbo"-Payload mit Noise, wobei der Header als AD verwendet wird, wie üblich.
- Teile das verschlüsselte Jumbo-Paket in Fragmente auf
- Füge einen unverschlüsselten Header für jedes Fragment 1-n hinzu
- Verschlüssle den Header für jedes Fragment 0-n. Jeder Header verwendet dieselben k_header_1 und k_header_2 wie oben in der Session Confirmed KDF definiert.
- Übertrage alle Fragmente

Reassemblierungsprozess:

Wenn Bob eine Session Confirmed Nachricht erhält, entschlüsselt er den Header, überprüft das frag-Feld und stellt fest, dass die Session Confirmed fragmentiert ist. Er entschlüsselt die Nachricht nicht (und kann sie nicht entschlüsseln), bis alle Fragmente empfangen und wieder zusammengesetzt wurden.

- Den Header für Fragment 0 beibehalten, da er als Noise AD verwendet wird
- Die Header für andere Fragmente vor der Wiederzusammensetzung verwerfen
- Die "Jumbo"-Nutzlast wiederzusammensetzen, mit dem Header für Fragment 0 als AD, und mit Noise entschlüsseln
- Den RI-Block wie gewohnt validieren
- Zur Datenphase übergehen und ACK 0 senden, wie gewohnt

Es gibt keinen Mechanismus für Bob, einzelne Fragmente zu bestätigen. Wenn Bob alle Fragmente empfangen, zusammengesetzt, entschlüsselt und den Inhalt validiert hat, führt Bob wie gewöhnlich einen split() durch, tritt in die Datenphase ein und sendet eine ACK für Paketnummer 0.

Wenn Alice keine ACK für Paketnummer 0 erhält, muss sie alle session confirmed Pakete unverändert erneut übertragen.

Beispiele:

Für 1500 MTU über IPv6 beträgt die maximale Payload 1372, der RI-Block-Overhead ist 5, die maximale (gzip-komprimierte) RI-Datengröße beträgt 1367 (vorausgesetzt, es gibt keine anderen Blöcke). Mit zwei Paketen beträgt der Overhead des 2. Pakets 64, sodass es weitere 1436 Bytes Payload aufnehmen kann. Zwei Pakete reichen also für eine komprimierte RI bis zu 2803 Bytes aus.

Die größte komprimierte RI, die im aktuellen Netzwerk beobachtet wurde, ist etwa 1400 Bytes groß; daher sollten in der Praxis zwei Fragmente ausreichen, selbst bei einer minimalen MTU von 1280. Das Protokoll erlaubt maximal 15 Fragmente.

Sicherheitsanalyse:

Die Integrität und Sicherheit einer fragmentierten Session Confirmed ist dieselbe wie die einer nicht fragmentierten. Jede Änderung an einem Fragment führt dazu, dass die Noise AEAD nach der Wiederzusammensetzung fehlschlägt. Die Header der Fragmente nach Fragment 0 werden nur zur Identifikation des Fragments verwendet. Selbst wenn ein Angreifer im Übertragungsweg den k_header_2-Schlüssel zur Header-Verschlüsselung hätte (unwahrscheinlich, da aus dem Handshake abgeleitet), würde dies dem Angreifer nicht ermöglichen, ein gültiges Fragment zu ersetzen.

### KDF für Datenphase

Die Datenphase verwendet den Header für zugehörige Daten.

Die KDF generiert zwei Chiffrierschlüssel k_ab und k_ba aus dem Verkettungsschlüssel ck, wobei HMAC-SHA256(key, data) wie in [RFC-2104](https://tools.ietf.org/html/rfc2104) definiert verwendet wird. Dies ist die split()-Funktion, genau wie in der Noise-Spezifikation definiert.

```
// split()

// chainKey = from handshake phase keydata = HKDF(chainKey, ZEROLEN, "", 64) k_ab = keydata[0:31] k_ba = keydata[32:63]

    // key is k_ab for Alice to Bob // key is k_ba for Bob to Alice

    keydata = HKDF(key, ZEROLEN, "HKDFSSU2DataKeys", 64) k_data = keydata[0:31] k_header_2 = keydata[32:63]

    // AEAD parameters k = k_data n = 4 byte packet number from header ad = 16 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for data phase // aik = Alice's intro key // bik = Bob's intro key k_header_1 = Receiver's intro key (aik or bik) k_header_2: from above
```
### Datennachricht (Typ 6)

Noise-Nutzlast: Alle Blocktypen sind erlaubt. Maximale Nutzlastgröße: MTU - 60 (IPv4) oder MTU - 80 (IPv6). Für 1500 MTU: Maximale Nutzlast ist 1440 (IPv4) oder 1420 (IPv6).

Beginnend mit dem 2. Teil von Session Confirmed befinden sich alle Nachrichten innerhalb einer authentifizierten und verschlüsselten ChaChaPoly-Nutzlast. Alle Polsterung befindet sich innerhalb der Nachricht. Innerhalb der Nutzlast befindet sich ein Standardformat mit null oder mehr "Blöcken". Jeder Block hat einen Ein-Byte-Typ und eine Zwei-Byte-Länge. Die Typen umfassen Datum/Zeit, I2NP-Nachricht, Optionen, Beendigung und Polsterung.

Hinweis: Bob kann, ist aber nicht verpflichtet, seine RouterInfo als erste Nachricht an Alice in der Datenphase zu senden.

Payload-Sicherheitseigenschaften:

```
XK(s, rs): Authentication Confidentiality

<- 2 5 -> 2 5

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 5. Encryption to a known recipient, strong forward secrecy. This payload is encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static DH with the recipient's static key pair. Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### Hinweise

- Der router muss eine Nachricht mit einem AEAD-Fehler verwerfen.

```
+----+----+----+----+----+----+----+----+

|  Short Header 16 bytes, ChaCha20 |

    + encrypted with intro key and + | derived key, see Data Phase KDF | +----+----+----+----+----+----+----+----+ | ChaCha20 data | + Encrypted and authenticated data + | length varies | + k defined in Data Phase KDF + | n = packet number from header | + + | | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
Unverschlüsselte Daten (Poly1305 Auth-Tag nicht gezeigt):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-------------------------------------------+----------+--------------------------------+
    | > Packet Number                           | type     | > flags                        |
    +-------------------------------------------+----------+--------------------------------+
    | >                                                                                     |
    | >                                                                                     |
    | > Noise payload (block data)                                                          |
    | >                                                                                     |
    | > :   (length varies)                                                                 |
    |                                                                                       |
    |                                                                                       |
    +---------------------------------------------------------------------------------------+

    Destination Connection ID :: As specified in session setup

    Packet Number :: 4 byte big endian integer

    type :: 6

    flags :: 3 bytes, unused, set to 0 for future compatibility
```
#### Notizen

- Die minimale Payload-Größe beträgt 8 Bytes. Diese Anforderung wird von jedem ACK-, I2NP-, First Fragment- oder Follow-on Fragment-Block erfüllt. Wenn die Anforderung nicht erfüllt wird, muss ein Padding-Block eingefügt werden.
- Jede Paketnummer darf nur einmal verwendet werden. Bei der Neuübertragung von I2NP-Nachrichten oder Fragmenten muss eine neue Paketnummer verwendet werden.

### KDF für Peer Test

```
// AEAD parameters

// bik = Bob's intro key k = bik n = 4 byte packet number from header ad = 32 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for this message k_header_1 = bik k_header_2 = bik
```
### Peer Test (Typ 7)

Charlie sendet an Alice, und Alice sendet an Charlie, nur für Peer Test Phasen 5-7. Peer Test Phasen 1-4 müssen in-session mit einem Peer Test Block in einer Data-Nachricht gesendet werden. Siehe die Abschnitte Peer Test Block und Peer Test Process unten für weitere Informationen.

Größe: 48 + Nutzlastgröße.

Noise-Nutzlast: Siehe unten.

Rohe Inhalte:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Alice or Charlie + | intro key | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Alice or Charlie + | intro key | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | | + see KDF for key and n + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
Unverschlüsselte Daten (Poly1305-Authentifizierungs-Tag nicht dargestellt):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+------------+------------+
    | > Packet Number                                   | type       | ver        | id         | flag       |
    +---------------------------------------------------+------------+------------+------------+------------+
    | > Source Connection ID                                                                                |
    +-------------------------------------------------------------------------------------------------------+
    | > Token                                                                                               |
    +-------------------------------------------------------------------------------------------------------+
    | >                                                                                                     |
    | >                                                                                                     |
    | > ChaCha20 payload (block data)                                                                       |
    | >                                                                                                     |
    | > :   (length varies)                                                                                 |
    | >                                                                                                     |
    | > see below for allowed blocks                                                                        |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    Destination Connection ID :: See below

    type :: 7

    ver :: 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Packet Number :: Random number generated by Alice or Charlie

    Source Connection ID :: See below

    Token :: Randomly generated by Alice or Charlie, ignored
```
#### Nutzlast

- DateTime-Block
- Address-Block (erforderlich für Nachrichten 6 und 7, siehe Hinweis unten)
- Peer Test-Block
- Padding-Block (optional)

Die minimale Nutzlastgröße beträgt 8 Bytes. Da der Peer Test Block insgesamt mehr als das umfasst, ist die Anforderung bereits mit diesem Block allein erfüllt.

In den Nachrichten 5 und 7 kann der Peer Test Block identisch mit dem Block aus den In-Session-Nachrichten 3 und 4 sein, der die von Charlie signierte Vereinbarung enthält, oder er kann neu generiert werden. Die Signatur ist optional.

In Nachricht 6 kann der Peer Test Block identisch mit dem Block aus den In-Session-Nachrichten 1 und 2 sein, der die von Alice signierte Anfrage enthält, oder er kann neu generiert werden. Die Signatur ist optional.

Verbindungs-IDs: Die beiden Verbindungs-IDs werden aus der Test-Nonce abgeleitet. Für die Nachrichten 5 und 7, die von Charlie an Alice gesendet werden, ist die Ziel-Verbindungs-ID zwei Kopien der 4-Byte-Big-Endian-Test-Nonce, d.h. ((nonce << 32) | nonce). Die Quell-Verbindungs-ID ist die Umkehrung der Ziel-Verbindungs-ID, d.h. ~((nonce << 32) | nonce). Für Nachricht 6, die von Alice an Charlie gesendet wird, werden die beiden Verbindungs-IDs vertauscht.

Inhalte des Adressblocks:

- In Nachricht 5: Nicht erforderlich.
- In Nachricht 6: Charlies IP und Port wie aus Charlies RI ausgewählt.
- In Nachricht 7: Alices tatsächliche IP und Port, von der Nachricht 6 empfangen wurde.

### KDF für Wiederholung

Die Anforderung für die Retry-Nachricht ist, dass Bob nicht verpflichtet ist, die Session Request-Nachricht zu entschlüsseln, um eine Retry-Nachricht als Antwort zu generieren. Außerdem muss diese Nachricht schnell zu generieren sein und nur symmetrische Verschlüsselung verwenden.

```
// AEAD parameters

// bik = Bob's intro key k = bik n = 4 byte packet number from header ad = 32 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for this message k_header_1 = bik k_header_2 = bik
```
### Wiederholung (Typ 9)

Bob sendet an Alice als Antwort auf eine Session Request- oder Token Request-Nachricht. Alice antwortet mit einer neuen Session Request. Größe: 48 + Payload-Größe.

Dient auch als Beendigungsnachricht (d.h. "Nicht wiederholen"), wenn ein Beendigungsblock enthalten ist.

Noise-Payload: Siehe unten.

Rohe Inhalte:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Bob intro key + | | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Bob intro key + | | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | | + see KDF for key and n + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
Unverschlüsselte Daten (Poly1305-Authentifizierungs-Tag nicht angezeigt):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+------------+------------+
    | > Packet Number                                   | type       | ver        | id         | flag       |
    +---------------------------------------------------+------------+------------+------------+------------+
    | > Source Connection ID                                                                                |
    +-------------------------------------------------------------------------------------------------------+
    | > Token                                                                                               |
    +-------------------------------------------------------------------------------------------------------+
    | >                                                                                                     |
    | >                                                                                                     |
    | > ChaCha20 payload (block data)                                                                       |
    | >                                                                                                     |
    | > :   (length varies)                                                                                 |
    | >                                                                                                     |
    | > see below for allowed blocks                                                                        |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    Destination Connection ID :: The Source Connection ID

    :   received from Alice in Token Request or Session Request

    Packet Number :: Random number generated by Bob

    type :: 9

    ver :: 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Source Connection ID :: The Destination Connection ID

    :   received from Alice in Token Request or Session Request

    Token :: 8 byte unsigned integer, randomly generated by Bob, nonzero,

    :   or zero if session is rejected and a termination block is included
```
#### Nutzlast

- DateTime-Block
- Adress-Block
- Options-Block (optional)
- Termination-Block (optional, wenn Session abgelehnt wird)
- Padding-Block (optional)

Die minimale Payload-Größe beträgt 8 Bytes. Da die DateTime- und Address-Blöcke zusammen mehr als das ausmachen, wird die Anforderung bereits mit diesen beiden Blöcken erfüllt.

#### Hinweise

- Um Widerstandsfähigkeit gegen Probing zu bieten, sollte ein router keine Retry-Nachricht als Antwort auf eine Session Request- oder Token Request-Nachricht senden, es sei denn, die Felder für Nachrichtentyp, Protokollversion und Netzwerk-ID in der Request-Nachricht sind gültig.
- Um das Ausmaß jedes Amplification-Angriffs zu begrenzen, der mit gefälschten Quelladressen durchgeführt werden kann, darf die Retry-Nachricht keine großen Mengen an Padding enthalten. Es wird empfohlen, dass die Retry-Nachricht nicht größer als dreimal so groß wie die Nachricht ist, auf die sie antwortet. Alternativ kann eine einfache Methode verwendet werden, wie das Hinzufügen einer zufälligen Menge an Padding im Bereich von 1-64 Bytes.

### KDF für Token-Anfrage

Diese Nachricht muss schnell zu generieren sein und nur symmetrische Verschlüsselung verwenden.

```
// AEAD parameters

// bik = Bob's intro key k = bik n = 4 byte packet number from header ad = 32 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for this message k_header_1 = bik k_header_2 = bik
```
### Token-Anfrage (Typ 10)

Alice sendet an Bob. Bob antwortet mit einer Retry-Nachricht. Größe: 48 + Payload-Größe.

Wenn Alice kein gültiges Token hat, sollte Alice diese Nachricht anstelle einer Session Request senden, um den asymmetrischen Verschlüsselungsaufwand bei der Generierung einer Session Request zu vermeiden.

Noise-Payload: Siehe unten.

Rohe Inhalte:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Bob intro key + | | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Bob intro key + | | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | | + see KDF for key and n + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
Unverschlüsselte Daten (Poly1305-Authentifizierungs-Tag nicht dargestellt):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+------------+------------+
    | > Packet Number                                   | type       | ver        | id         | flag       |
    +---------------------------------------------------+------------+------------+------------+------------+
    | > Source Connection ID                                                                                |
    +-------------------------------------------------------------------------------------------------------+
    | > Token                                                                                               |
    +-------------------------------------------------------------------------------------------------------+
    | >                                                                                                     |
    | >                                                                                                     |
    | > ChaCha20 payload (block data)                                                                       |
    | >                                                                                                     |
    | > :   (length varies)                                                                                 |
    | >                                                                                                     |
    | > see below for allowed blocks                                                                        |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    Destination Connection ID :: Randomly generated by Alice

    Packet Number :: Random number generated by Alice

    type :: 10

    ver :: 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Source Connection ID :: Randomly generated by Alice,

    :   must not be equal to Destination Connection ID

    Token :: zero
```
#### Nutzlast

- DateTime-Block
- Padding-Block

Die minimale Payload-Größe beträgt 8 Bytes.

#### Anmerkungen

- Um Widerstand gegen Probing zu bieten, sollte ein router keine Retry-Nachricht als Antwort auf eine Token Request-Nachricht senden, es sei denn, die Felder für Nachrichtentyp, Protokollversion und Netzwerk-ID in der Token Request-Nachricht sind gültig.
- Dies ist KEINE Standard-Noise-Nachricht und ist nicht Teil des Handshakes. Sie ist nicht mit der Session Request-Nachricht verbunden, außer durch Verbindungs-IDs.
- Bei den meisten Fehlern, einschließlich AEAD oder offensichtlichem Replay, sollte Bob die weitere Nachrichtenverarbeitung stoppen und die Nachricht ohne Antwort verwerfen.
- Bob muss Verbindungen ablehnen, bei denen der Zeitstempelwert zu weit von der aktuellen Zeit abweicht. Nennen wir die maximale Delta-Zeit "D". Bob muss einen lokalen Cache von zuvor verwendeten Handshake-Werten pflegen und Duplikate ablehnen, um Replay-Angriffe zu verhindern. Werte im Cache müssen eine Lebensdauer von mindestens 2*D haben. Die Cache-Werte sind implementierungsabhängig, jedoch kann der 32-Byte X-Wert (oder sein verschlüsseltes Äquivalent) verwendet werden.
- Bob KANN eine Retry-Nachricht mit einem Null-Token und einem Termination-Block mit einem Clock-Skew-Reason-Code senden, wenn der Zeitstempel im DateTime-Block zu stark verzerrt ist.
- Mindestgröße: TBD, gleiche Regeln wie für Session Created?

### KDF für Hole Punch

Diese Nachricht muss schnell zu generieren sein und nur symmetrische Verschlüsselung verwenden.

```
// AEAD parameters

// aik = Alice's intro key k = aik n = 4 byte packet number from header ad = 32 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for this message k_header_1 = aik k_header_2 = aik
```
### Hole Punch (Typ 11)

Charlie sendet an Alice, als Antwort auf ein Relay Intro, das von Bob empfangen wurde. Alice antwortet mit einer neuen Session Request. Größe: 48 + Payload-Größe.

Noise-Nutzlast: Siehe unten.

Roher Inhalt:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Alice intro key + | | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Alice intro key + | | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | | + see KDF for key and n + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
Unverschlüsselte Daten (Poly1305-Authentifizierungs-Tag nicht gezeigt):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+------------+------------+
    | > Packet Number                                   | type       | ver        | id         | flag       |
    +---------------------------------------------------+------------+------------+------------+------------+
    | > Source Connection ID                                                                                |
    +-------------------------------------------------------------------------------------------------------+
    | > Token                                                                                               |
    +-------------------------------------------------------------------------------------------------------+
    | >                                                                                                     |
    | >                                                                                                     |
    | > ChaCha20 payload (block data)                                                                       |
    | >                                                                                                     |
    | > :   (length varies)                                                                                 |
    | >                                                                                                     |
    | > see below for allowed blocks                                                                        |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    Destination Connection ID :: See below

    Packet Number :: Random number generated by Charlie

    type :: 11

    ver :: 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Source Connection ID :: See below

    Token :: 8 byte unsigned integer, randomly generated by Charlie, nonzero.
```
#### Payload

- DateTime-Block
- Adress-Block
- Relay Response-Block
- Padding-Block (optional)

Die minimale Payload-Größe beträgt 8 Bytes. Da die DateTime- und Address-Blöcke zusammen mehr als das ergeben, ist die Anforderung bereits mit nur diesen beiden Blöcken erfüllt.

Connection IDs: Die beiden Connection IDs werden von der Relay-Nonce abgeleitet. Die Destination Connection ID besteht aus zwei Kopien der 4-Byte Big-Endian Relay-Nonce, d.h. ((nonce << 32) | nonce). Die Source Connection ID ist die Umkehrung der Destination Connection ID, d.h. ~((nonce << 32) | nonce).

Alice sollte das Token im Header ignorieren. Das Token, das in der Session Request verwendet werden soll, befindet sich im Relay Response Block.

## Noise Payload

Jede Noise-Nutzlast enthält null oder mehr "Blöcke".

Dies verwendet das gleiche Block-Format wie in den [NTCP2](/docs/specs/ntcp2) und [ECIES](/docs/specs/ecies) Spezifikationen definiert. Einzelne Block-Typen sind unterschiedlich definiert. Der entsprechende Begriff in QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) ist "frames".

Es gibt Bedenken, dass die Ermutigung von Implementierern, Code zu teilen, zu Parsing-Problemen führen könnte. Implementierer sollten die Vorteile und Risiken der Code-Teilung sorgfältig abwägen und sicherstellen, dass die Reihenfolge und gültigen Block-Regeln für die beiden Kontexte unterschiedlich sind.

### Payload-Format

Es gibt einen oder mehrere Blöcke in der verschlüsselten Nutzlast. Ein Block ist ein einfaches Tag-Length-Value (TLV) Format. Jeder Block enthält eine Ein-Byte-Kennung, eine Zwei-Byte-Länge und null oder mehr Datenbytes. Dieses Format ist identisch mit dem in [NTCP2](/docs/specs/ntcp2) und [ECIES](/docs/specs/ecies), jedoch sind die Blockdefinitionen unterschiedlich.

Zur Erweiterbarkeit müssen Empfänger Blöcke mit unbekannten Identifikatoren ignorieren und sie als Padding behandeln.

(Poly1305 Authentifizierungs-Tag nicht angezeigt):

```
+----+----+----+----+----+----+----+----+

[|blk |](##SUBST##|blk |) size | data | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ [|blk |](##SUBST##|blk |) size | data | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ ~ . . . ~

    blk :: 1 byte, see below size :: 2 bytes, big endian, size of data to follow, 0 - TBD data :: the data
```
Die Header-Verschlüsselung verwendet die letzten 24 Bytes des Pakets als IV für die beiden ChaCha20-Operationen. Da alle Pakete mit einem 16-Byte-MAC enden, ist erforderlich, dass alle Paket-Payloads mindestens 8 Bytes groß sind. Wenn ein Payload diese Anforderung andernfalls nicht erfüllen würde, muss ein Padding-Block eingefügt werden.

Die maximale ChaChaPoly-Nutzlast variiert je nach Nachrichtentyp, MTU und IPv4- oder IPv6-Adresstyp. Die maximale Nutzlast beträgt MTU - 60 für IPv4 und MTU - 80 für IPv6. Die maximalen Nutzlastdaten betragen MTU - 63 für IPv4 und MTU - 83 für IPv6. Die Obergrenze liegt bei etwa 1440 Bytes für IPv4, 1500 MTU, Data-Nachricht. Die maximale Gesamtblockgröße entspricht der maximalen Nutzlastgröße. Die maximale Einzelblockgröße entspricht der maximalen Gesamtblockgröße. Der Blocktyp umfasst 1 Byte. Die Blocklänge umfasst 2 Bytes. Die maximale Einzelblock-Datengröße ist die maximale Einzelblockgröße minus 3.

Hinweise:

- Implementierer müssen sicherstellen, dass beim Lesen eines Blocks fehlerhafte oder bösartige Daten nicht dazu führen, dass Lesevorgänge in den nächsten Block oder über die Payload-Grenze hinaus übergreifen.
- Implementierungen sollten unbekannte Block-Typen für Vorwärtskompatibilität ignorieren.

Blocktypen:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Block Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Number</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Block Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Options</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15+</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Router Info</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">I2NP Message</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Follow-on Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Termination</td><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 typ.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">8</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Intro</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Next Nonce</td><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">ACK</td><td style="border:1px solid var(--color-border); padding:0.6rem;">12</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 or 21</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;">--</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">17</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Challenge</td><td style="border:1px solid var(--color-border); padding:0.6rem;">18</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">19</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Packet Number</td><td style="border:1px solid var(--color-border); padding:0.6rem;">20</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Congestion</td><td style="border:1px solid var(--color-border); padding:0.6rem;">21</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for experimental features</td><td style="border:1px solid var(--color-border); padding:0.6rem;">224-253</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Padding</td><td style="border:1px solid var(--color-border); padding:0.6rem;">254</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for future extension</td><td style="border:1px solid var(--color-border); padding:0.6rem;">255</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>           
### Regeln für die Block-Reihenfolge

In der Session Confirmed muss Router Info der erste Block sein.

In allen anderen Nachrichten ist die Reihenfolge nicht spezifiziert, außer für die folgenden Anforderungen: Padding, falls vorhanden, muss der letzte Block sein. Termination, falls vorhanden, muss der letzte Block außer Padding sein. Mehrere Padding-Blöcke sind in einer einzigen Payload nicht erlaubt.

### Block-Spezifikationen

#### DateTime

Für Zeitsynchronisation:

```
+----+----+----+----+----+----+----+

| 0 | 4 | timestamp |

    +----+----+----+----+----+----+----+

    blk :: 0 size :: 2 bytes, big endian, value = 4 timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106
```
Hinweise:

- Im Gegensatz zu SSU 1 gibt es in SSU 2 keinen Zeitstempel im Paket-Header für die Datenphase.
- Implementierungen sollten regelmäßig DateTime-Blöcke in der Datenphase senden.
- Implementierungen müssen auf die nächste Sekunde runden, um Uhrenabweichungen im Netzwerk zu verhindern.

#### Optionen

Übergebe aktualisierte Optionen. Optionen umfassen: Minimale und maximale Polsterung.

Der Optionen-Block wird eine variable Länge haben.

```
+----+----+----+----+----+----+----+----+

| 1 | size [|tmin|](##SUBST##|tmin|)tmax[|rmin|](##SUBST##|rmin|)rmax[|tdmy|](##SUBST##|tdmy|)

    +----+----+----+----+----+----+----+----+ [|tdmy|](##SUBST##|tdmy|) rdmy | tdelay | rdelay | | ~----+----+----+----+----+----+----+ ~ | more_options | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 1 size :: 2 bytes, big endian, size of options to follow, 12 bytes minimum

    tmin, tmax, rmin, rmax :: requested padding limits

    :   tmin and rmin are for desired resistance to traffic analysis. tmax and rmax are for bandwidth limits. tmin and tmax are the transmit limits for the router sending this options block. rmin and rmax are the receive limits for the router sending this options block. Each is a 4.4 fixed-point float representing 0 to 15.9375 (or think of it as an unsigned 8-bit integer divided by 16.0). This is the ratio of padding to data. Examples: Value of 0x00 means no padding Value of 0x01 means add 6 percent padding Value of 0x10 means add 100 percent padding Value of 0x80 means add 800 percent (8x) padding Alice and Bob will negotiate the minimum and maximum in each direction. These are guidelines, there is no enforcement. Sender should honor receiver's maximum. Sender may or may not honor receiver's minimum, within bandwidth constraints.

    tdmy: Max dummy traffic willing to send, 2 bytes big endian, bytes/sec average rdmy: Requested dummy traffic, 2 bytes big endian, bytes/sec average tdelay: Max intra-message delay willing to insert, 2 bytes big endian, msec average rdelay: Requested intra-message delay, 2 bytes big endian, msec average

    Padding distribution specified as additional parameters? Random delay specified as additional parameters?

    more_options :: Format TBD
```
Optionen-Probleme:

- Options-Verhandlung ist noch zu bestimmen.

#### RouterInfo

Übertrage Alices RouterInfo an Bob. Wird nur in der Session Confirmed Teil 2 Nutzlast verwendet. Nicht in der Datenphase zu verwenden; verwende stattdessen eine I2NP DatabaseStore Message.

Mindestgröße: Etwa 420 Bytes, es sei denn, die router-Identität und Signatur in den router-Informationen sind komprimierbar, was unwahrscheinlich ist.

HINWEIS: Der Router Info Block wird niemals fragmentiert. Das frag-Feld ist immer 0/1. Siehe den Abschnitt Session Confirmed Fragmentation oben für weitere Informationen.

```
+----+----+----+----+----+----+----+----+

| 2 | size [|flag|](##SUBST##|flag|)frag| |

    +----+----+----+----+----+ + | | + Router Info fragment + | (Alice RI in Session Confirmed) | + (Alice, Bob, or third-party + | RI in data phase) | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 2 size :: 2 bytes, big endian, 2 + fragment size flag :: 1 byte flags bit order: 76543210 (bit 7 is MSB) bit 0: 0 for local store, 1 for flood request bit 1: 0 for uncompressed, 1 for gzip compressed bits 7-2: Unused, set to 0 for future compatibility frag :: 1 byte fragment info: bit order: 76543210 (bit 7 is MSB) bits 7-4: fragment number, always 0 bits 3-0: total fragments, always 1, big endian

    routerinfo :: Alice's or Bob's RouterInfo
```
Hinweise:

- Die Router Info ist optional mit gzip komprimiert, wie durch Flag-Bit 1 angezeigt. Dies unterscheidet sich von NTCP2, wo sie niemals komprimiert wird, und von einer DatabaseStore Message, wo sie immer komprimiert wird. Kompression ist optional, da sie normalerweise bei kleinen Router Infos mit wenig komprimierbarem Inhalt von geringem Nutzen ist, aber bei großen Router Infos mit mehreren komprimierbaren Router Addresses sehr vorteilhaft ist. Kompression wird empfohlen, wenn sie es ermöglicht, dass eine Router Info in ein einzelnes Session Confirmed Paket ohne Fragmentierung passt.
- Maximale Größe des ersten oder einzigen Fragments in der Session Confirmed Nachricht: MTU - 113 für IPv4 oder MTU - 133 für IPv6. Bei einer angenommenen Standard-MTU von 1500 Bytes und ohne andere Blöcke in der Nachricht: 1387 für IPv4 oder 1367 für IPv6. 97% der aktuellen router infos sind ohne gzipping kleiner als 1367. 99,9% der aktuellen router infos sind mit gzipping kleiner als 1367. Bei einer angenommenen Mindest-MTU von 1280 Bytes und ohne andere Blöcke in der Nachricht: 1167 für IPv4 oder 1147 für IPv6. 94% der aktuellen router infos sind ohne gzipping kleiner als 1147. 97% der aktuellen router infos sind mit gzipping kleiner als 1147.
- Das frag-Byte wird nun nicht mehr verwendet, der Router Info Block wird niemals fragmentiert. Das frag-Byte muss auf Fragment 0, Gesamtfragmente 1 gesetzt werden. Siehe den Abschnitt Session Confirmed Fragmentation oben für weitere Informationen.
- Flooding darf nur angefordert werden, wenn veröffentlichte RouterAddresses in der RouterInfo vorhanden sind. Der empfangende router darf die RouterInfo nur dann flooden, wenn veröffentlichte RouterAddresses in ihr enthalten sind.
- Dieses Protokoll bietet keine Bestätigung, dass die RouterInfo gespeichert oder geflutet wurde. Falls eine Bestätigung gewünscht wird und der Empfänger floodfill ist, sollte der Sender stattdessen eine Standard-I2NP DatabaseStoreMessage mit einem Reply-Token senden.

#### I2NP Message

Eine vollständige I2NP-Nachricht mit einem modifizierten Header.

Dies verwendet die gleichen 9 Bytes für den I2NP-Header wie in [NTCP2](/docs/specs/ntcp2) (Typ, Nachrichten-ID, kurze Ablaufzeit).

```
+----+----+----+----+----+----+----+----+

| 3 | size [|type|](##SUBST##|type|) msg id |

    +-------------------------------+
    | > short exp                   |
    +-------------------------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 3 size :: 2 bytes, big endian, size of type + msg id + exp + message to follow I2NP message body size is (size - 9). type :: 1 byte, I2NP msg type, see I2NP spec msg id :: 4 bytes, big endian, I2NP message ID short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds. Wraps around in 2106 message :: I2NP message body
```
Hinweise:

- Dies ist das gleiche 9-Byte I2NP Header-Format, das in NTCP2 verwendet wird.
- Dies ist genau das gleiche Format wie der First Fragment-Block, aber der Block-Typ zeigt an, dass dies eine vollständige Nachricht ist.
- Die maximale Größe einschließlich des 9-Byte I2NP Headers beträgt MTU - 63 für IPv4 und MTU - 83 für IPv6.

#### Erstes Fragment

Das erste Fragment (Fragment #0) einer I2NP-Nachricht mit einem modifizierten Header.

Dies verwendet die gleichen 9 Bytes für den I2NP-Header wie in [NTCP2](/docs/specs/ntcp2) (Typ, Nachrichten-ID, kurze Ablaufzeit).

Die Gesamtanzahl der Fragmente ist nicht angegeben.

```
+----+----+----+----+----+----+----+----+

| 4 | size [|type|](##SUBST##|type|) msg id |

    +-------------------------------+
    | > short exp                   |
    +-------------------------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 4 size :: 2 bytes, big endian, size of data to follow Fragment size is (size - 9). type :: 1 byte, I2NP msg type, see I2NP spec msg id :: 4 bytes, big endian, I2NP message ID short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds. Wraps around in 2106 message :: Partial I2NP message body, bytes 0 - (size - 10)
```
Hinweise:

- Dies ist das gleiche 9-Byte I2NP Header-Format, das in NTCP2 verwendet wird.
- Dies ist exakt das gleiche Format wie der I2NP Message Block, aber der Block-Typ zeigt an, dass dies das erste Fragment einer Nachricht ist.
- Die partielle Nachrichtenlänge muss größer als null sein.
- Wie in SSU 1 wird empfohlen, das letzte Fragment zuerst zu senden, damit der Empfänger die Gesamtanzahl der Fragmente kennt und Empfangspuffer effizient zuweisen kann.
- Die maximale Größe einschließlich des 9-Byte I2NP Headers beträgt MTU - 63 für IPv4 und MTU - 83 für IPv6.

#### Nachfolge-Fragment

Ein zusätzliches Fragment (Fragmentnummer größer als null) einer I2NP-Nachricht.

```
+----+----+----+----+----+----+----+----+

| 5 | size [|frag|](##SUBST##|frag|) msg id |

    +----+----+----+----+----+----+----+----+ | | + + | partial message | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 5 size :: 2 bytes, big endian, size of data to follow Fragment size is (size - 5). frag :: Fragment info: Bit order: 76543210 (bit 7 is MSB) bits 7-1: fragment number 1 - 127 (0 not allowed) bit 0: isLast (1 = true) msg id :: 4 bytes, big endian, I2NP message ID message :: Partial I2NP message body
```
Hinweise:

- Die Teilnachrichtenlänge muss größer als null sein.
- Wie in SSU 1 wird empfohlen, das letzte Fragment zuerst zu senden, damit der Empfänger die Gesamtanzahl der Fragmente kennt und effizient Empfangspuffer zuweisen kann.
- Wie in SSU 1 beträgt die maximale Fragmentnummer 127, aber die praktische Grenze liegt bei 63 oder weniger. Implementierungen können das Maximum auf das begrenzen, was für eine maximale I2NP-Nachrichtengröße von etwa 64 KB praktisch ist, was etwa 55 Fragmente bei einer minimalen MTU von 1280 entspricht. Siehe den Abschnitt "Max I2NP Message Size" unten.
- Die maximale Teilnachrichtengröße (ohne frag und message id) beträgt MTU - 68 für IPv4 und MTU - 88 für IPv6.

#### Beendigung

Verbindung trennen. Dies muss der letzte Nicht-Padding-Block in der Nutzlast sein.

```
+----+----+----+----+----+----+----+----+

| 6 | size | valid data packets |

    +----+----+----+----+----+----+----+----+

    :   received | rsn| addl data |

    +----+----+----+----+ + ~ . . . ~ +----+----+----+----+----+----+----+----+

    blk :: 6 size :: 2 bytes, big endian, value = 9 or more valid data packets received :: The number of valid packets received (current receive nonce value) 0 if error occurs in handshake phase 8 bytes, big endian rsn :: reason, 1 byte: 0: normal close or unspecified 1: termination received 2: idle timeout 3: router shutdown 4: data phase AEAD failure 5: incompatible options 6: incompatible signature type 7: clock skew 8: padding violation 9: AEAD framing error 10: payload format error 11: Session Request error 12: Session Created error 13: Session Confirmed error 14: Timeout 15: RI signature verification fail 16: s parameter missing, invalid, or mismatched in RouterInfo 17: banned 18: bad token 19: connection limits 20: incompatible version 21: wrong net ID 22: replaced by new session addl data :: optional, 0 or more bytes, for future expansion, debugging, or reason text. Format unspecified and may vary based on reason code.
```
Hinweise:

- Nicht alle Gründe werden möglicherweise tatsächlich verwendet, implementierungsabhängig. Die meisten Fehler führen in der Regel dazu, dass die Nachricht verworfen wird, nicht zu einer Beendigung. Siehe Hinweise in den Handshake-Nachrichtensektionen oben. Zusätzlich aufgeführte Gründe dienen der Konsistenz, Protokollierung, Fehlerbehebung oder falls sich die Richtlinien ändern.
- Es wird empfohlen, einen ACK-Block zusammen mit dem Termination-Block einzubinden.
- In der Datenphase sollte der Peer für jeden anderen Grund als "termination received" mit einem Termination-Block mit dem Grund "termination received" antworten.

#### RelayRequest

Gesendet in einer Data-Nachricht innerhalb der Sitzung, von Alice zu Bob. Siehe Abschnitt Relay Process unten.

```
+----+----+----+----+----+----+----+----+

|  7 | size [|flag|](##SUBST##|flag|) nonce |

    +-------+-------+---------------+-----------------------------------+
    | > relay tag                   | > timestamp                       |
    +-------+-------+---------------+-----------------------------------+
    | ver   | asz   | AlicePort     | > Alice IP address                |
    +-------+-------+---------------+-----------------------------------+

    ~ ~ | . . . | +----+----+----+----+----+----+----+----+

    blk :: 7 size :: 2 bytes, big endian, size of data to follow flag :: 1 byte flags, Unused, set to 0 for future compatibility

    The data below here is covered by the signature, and Bob forwards it unmodified.

    nonce :: 4 bytes, randomly generated by Alice relay tag :: 4 bytes, the itag from Charlie's RI timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106 ver :: 1 byte SSU version to be used for the introduction: 1: SSU 1 2: SSU 2 asz :: 1 byte endpoint (port + IP) size (6 or 18) AlicePort :: 2 byte Alice's port number, big endian Alice IP :: (asz - 2) byte representation of Alice's IP address, network byte order signature :: length varies, 64 bytes for Ed25519. Signature of prologue, Bob's hash, and signed data above, as signed by Alice.
```
Hinweise:

- Die IP-Adresse ist immer enthalten (im Gegensatz zu SSU 1) und kann sich von der für die Sitzung verwendeten IP unterscheiden.

Signatur:

Alice signiert die Anfrage und fügt sie in diesen Block ein; Bob leitet sie im Relay Intro Block an Charlie weiter. Signaturalgorithmus: Signiere die folgenden Daten mit Alices router signing key:

- prologue: 16 Bytes "RelayRequestData", nicht null-terminiert (nicht in der Nachricht enthalten)
- bhash: Bobs 32-Byte router Hash (nicht in der Nachricht enthalten)
- chash: Charlies 32-Byte router Hash (nicht in der Nachricht enthalten)
- nonce: 4 Byte nonce
- relay tag: 4 Byte relay tag
- timestamp: 4 Byte Zeitstempel (Sekunden)
- ver: 1 Byte SSU Version
- asz: 1 Byte Endpunkt (Port + IP) Größe (6 oder 18)
- AlicePort: 2 Byte Alices Portnummer
- Alice IP: (asz - 2) Byte Alice IP-Adresse

#### RelayResponse

Gesendet in einer Data-Nachricht innerhalb der Sitzung, von Charlie an Bob oder von Bob an Alice, UND in der Hole Punch-Nachricht von Charlie an Alice. Siehe Abschnitt Relay Process unten.

```
+----+----+----+----+----+----+----+----+

|  8 | size [|flag|](##SUBST##|flag|)code| nonce

    +----+----+----+----+----+----+----+----+

    :   |     timestamp | ver| csz|Char

    +----+----+----+----+----+----+----+----+

    :   Port| Charlie IP addr | |

    +----+----+----+----+----+ + | signature | + length varies + | 64 bytes for Ed25519 | ~ ~ | . . . | +----+----+----+----+----+----+----+----+ | Token | +----+----+----+----+----+----+----+----+

    blk :: 8 size :: 2 bytes, 6 flag :: 1 byte flags, Unused, set to 0 for future compatibility code :: 1 byte status code: 0: accept 1: rejected by Bob, reason unspecified 2: rejected by Bob, Charlie is banned 3: rejected by Bob, limit exceeded 4: rejected by Bob, signature failure 5: rejected by Bob, relay tag not found 6: rejected by Bob, Alice RI not found 7-63: other rejected by Bob codes TBD 64: rejected by Charlie, reason unspecified 65: rejected by Charlie, unsupported address 66: rejected by Charlie, limit exceeded 67: rejected by Charlie, signature failure 68: rejected by Charlie, Alice is already connected 69: rejected by Charlie, Alice is banned 70: rejected by Charlie, Alice is unknown 71-127: other rejected by Charlie codes TBD 128: reject, source and reason unspecified 129-255: other reject codes TBD

    The data below is covered by the signature if the code is 0 (accept). Bob forwards it unmodified.

    nonce :: 4 bytes, as received from Bob or Alice

    The data below is present only if the code is 0 (accept).

    timestamp :: Unix timestamp, unsigned seconds.

    :   Wraps around in 2106

    ver :: 1 byte SSU version to be used for the introduction:

    :   1: SSU 1 2: SSU 2

    csz :: 1 byte endpoint (port + IP) size (0 or 6 or 18)

    :   may be 0 for some rejection codes

    CharliePort :: 2 byte Charlie's port number, big endian

    :   not present if csz is 0

    Charlie IP :: (csz - 2) byte representation of Charlie's IP address,

    :   network byte order not present if csz is 0

    signature :: length varies, 64 bytes for Ed25519.

    :   Signature of prologue, Bob's hash, and signed data above, as signed by Charlie. Not present if rejected by Bob.

    token :: Token generated by Charlie for Alice to use

    :   in the Session Request. Only present if code is 0 (accept)
```
Hinweise:

Das Token muss von Alice sofort in der Session Request verwendet werden.

Signatur:

Wenn Charlie zustimmt (Antwortcode 0) oder ablehnt (Antwortcode 64 oder höher), signiert Charlie die Antwort und fügt sie in diesen Block ein; Bob leitet sie im Relay Response Block an Alice weiter. Signaturalgorithmus: Signiere die folgenden Daten mit Charlies router Signaturschlüssel:

- prologue: 16 Bytes "RelayAgreementOK", nicht null-terminiert (nicht in der Nachricht enthalten)
- bhash: Bobs 32-Byte router Hash (nicht in der Nachricht enthalten)
- nonce: 4 Byte nonce
- timestamp: 4 Byte Zeitstempel (Sekunden)
- ver: 1 Byte SSU Version
- csz: 1 Byte Endpunkt (Port + IP) Größe (0 oder 6 oder 18)
- CharliePort: 2 Byte Charlies Portnummer (nicht vorhanden wenn csz 0 ist)
- Charlie IP: (csz - 2) Byte Charlie IP-Adresse (nicht vorhanden wenn csz 0 ist)

Wenn Bob ablehnt (Antwortcode 1-63), signiert Bob die Antwort und fügt sie in diesen Block ein. Signaturalgorithmus: Signiere die folgenden Daten mit Bobs router-Signaturschlüssel:

- prologue: 16 Bytes "RelayAgreementOK", nicht null-terminiert (nicht in der Nachricht enthalten)
- bhash: Bobs 32-Byte router hash (nicht in der Nachricht enthalten)
- nonce: 4 Byte nonce
- timestamp: 4 Byte Zeitstempel (Sekunden)
- ver: 1 Byte SSU Version
- csz: 1 Byte = 0

#### RelayIntro

Gesendet in einer Data-Nachricht innerhalb der Sitzung, von Bob zu Charlie. Siehe Abschnitt Relay Process unten.

Muss von einem RouterInfo-Block oder I2NP DatabaseStore-Nachrichtenblock (oder -fragment) vorangestellt werden, der Alices Router-Info enthält, entweder in derselben Nutzlast (falls Platz vorhanden ist) oder in einer vorherigen Nachricht.

```
+----+----+----+----+----+----+----+----+

|  9 | size [|flag|](##SUBST##|flag|) |

    +----+----+----+----+ + | | + + | Alice Router Hash | + 32 bytes + | | + +----+----+----+----+ | | nonce | +----+----+----+----+----+----+----+----+ | relay tag | timestamp | +----+----+----+----+----+----+----+----+ | ver| asz[|AlicePort|](##SUBST##|AlicePort|) Alice IP address | +----+----+----+----+----+----+----+----+ | signature | + length varies + | 64 bytes for Ed25519 | ~ ~ | . . . | +----+----+----+----+----+----+----+----+

    blk :: 9 size :: 2 bytes, big endian, size of data to follow flag :: 1 byte flags, Unused, set to 0 for future compatibility hash :: Alice's 32-byte router hash,

    The data below here is covered by the signature, as received from Alice in the Relay Request, and Bob forwards it unmodified.

    nonce :: 4 bytes, as received from Alice relay tag :: 4 bytes, the itag from Charlie's RI timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106 ver :: 1 byte SSU version to be used for the introduction: 1: SSU 1 2: SSU 2 asz :: 1 byte endpoint (port + IP) size (6 or 18) AlicePort :: 2 byte Alice's port number, big endian Alice IP :: (asz - 2) byte representation of Alice's IP address, network byte order signature :: length varies, 64 bytes for Ed25519. Signature of prologue, Bob's hash, and signed data above, as signed by Alice.
```
Anmerkungen:

- Für IPv4 ist Alice's IP-Adresse immer 4 Bytes lang, da Alice versucht, sich über IPv4 mit Charlie zu verbinden. IPv6 wird unterstützt, und Alice's IP-Adresse kann 16 Bytes lang sein.
- Für IPv4 muss diese Nachricht über eine etablierte IPv4-Verbindung gesendet werden, da dies die einzige Möglichkeit ist, wie Bob Charlie's IPv4-Adresse kennt, um sie in der [RelayResponse](#relayresponse) an Alice zurückzusenden. IPv6 wird unterstützt, und diese Nachricht kann über eine etablierte IPv6-Verbindung gesendet werden.
- Jede SSU-Adresse, die mit introducers veröffentlicht wird, muss "4" oder "6" in der "caps"-Option enthalten.

Signatur:

Alice signiert die Anfrage und Bob leitet sie in diesem Block an Charlie weiter. Verifizierungsalgorithmus: Verifiziere die folgenden Daten mit Alices router-Signaturschlüssel:

- prologue: 16 Bytes "RelayRequestData", nicht null-terminiert (nicht in der Nachricht enthalten)
- bhash: Bobs 32-Byte router Hash (nicht in der Nachricht enthalten)
- chash: Charlies 32-Byte router Hash (nicht in der Nachricht enthalten)
- nonce: 4 Byte Nonce
- relay tag: 4 Byte relay Tag
- timestamp: 4 Byte Zeitstempel (Sekunden)
- ver: 1 Byte SSU Version
- asz: 1 Byte Endpunkt (Port + IP) Größe (6 oder 18)
- AlicePort: 2 Byte Alices Portnummer
- Alice IP: (asz - 2) Byte Alice IP-Adresse

#### PeerTest

Wird entweder in einer Data-Nachricht während der Sitzung oder in einer Peer Test-Nachricht außerhalb der Sitzung gesendet. Siehe Abschnitt Peer Test Process unten.

Für Nachricht 2 muss ein RouterInfo-Block oder ein I2NP DatabaseStore-Nachrichtenblock (oder Fragment) vorangehen, der Alices Router Info enthält, entweder in derselben Payload (falls Platz vorhanden ist) oder in einer vorherigen Nachricht.

Für Nachricht 4, wenn das Relay akzeptiert wird (Grund-Code 0), muss ein RouterInfo-Block oder I2NP DatabaseStore-Nachrichtenblock (oder Fragment) vorangestellt werden, der Charlies Router Info enthält, entweder in derselben Nutzlast (falls Platz vorhanden ist) oder in einer vorherigen Nachricht.

```
+----+----+----+----+----+----+----+----+

| 10 | size | msg[|code|](##SUBST##|code|)flag| |

    +----+----+----+----+----+----+ + | Alice router hash (message 2 only) | + or + | Charlie router hash (message 4 only) | + or all zeros if rejected by Bob + | Not present in messages 1,3,5,6,7 | + +----+----+ | | ver| +----+----+----+----+----+----+----+----+ nonce | timestamp | asz| +----+----+----+----+----+----+----+----+ [|AlicePort|](##SUBST##|AlicePort|) Alice IP address | | +----+----+----+----+----+----+ + | signature | + length varies + | 64 bytes for Ed25519 | ~ ~ | . . . | +----+----+----+----+----+----+----+----+

    blk :: 10 size :: 2 bytes, big endian, size of data to follow msg :: 1 byte message number 1-7 code :: 1 byte status code: 0: accept 1: rejected by Bob, reason unspecified 2: rejected by Bob, no Charlie available 3: rejected by Bob, limit exceeded 4: rejected by Bob, signature failure 5: rejected by Bob, address unsupported 6-63: other rejected by Bob codes TBD 64: rejected by Charlie, reason unspecified 65: rejected by Charlie, unsupported address 66: rejected by Charlie, limit exceeded 67: rejected by Charlie, signature failure 68: rejected by Charlie, Alice is already connected 69: rejected by Charlie, Alice is banned 70: rejected by Charlie, Alice is unknown 70-127: other rejected by Charlie codes TBD 128: reject, source and reason unspecified 129-255: other reject codes TBD reject codes only allowed in messages 3 and 4 flag :: 1 byte flags, Unused, set to 0 for future compatibility hash :: Alice's or Charlie's 32-byte router hash, only present in messages 2 and 4. All zeros (fake hash) in message 4 if rejected by Bob.

    For messages 1-4, the data below here is covered by the signature, if present, and Bob forwards it unmodified.

    ver :: 1 byte SSU version:

    :   1: SSU 1 (not supported) 2: SSU 2 (required)

    nonce :: 4 byte test nonce, big endian timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106 asz :: 1 byte endpoint (port + IP) size (6 or 18) AlicePort :: 2 byte Alice's port number, big endian Alice IP :: (asz - 2) byte representation of Alice's IP address, network byte order signature :: length varies, 64 bytes for Ed25519. Signature of prologue, Bob's hash, and signed data above, as signed by Alice or Charlie. Only present for messages 1-4. Optional in message 5-7.
```
Hinweise:

- Anders als bei SSU 1 muss Nachricht 1 Alices IP-Adresse und Port enthalten.

- Das Testen von IPv6-Adressen wird unterstützt, und die Kommunikation zwischen Alice-Bob und Alice-Charlie kann über IPv6 erfolgen, wenn Bob und Charlie ihre Unterstützung mit einer 'B'-Fähigkeit in ihrer veröffentlichten IPv6-Adresse anzeigen. Siehe Proposal 126 für Details.

Alice sendet die Anfrage an Bob über eine bestehende Sitzung über das Transport-Protokoll (IPv4 oder IPv6), das sie testen möchte. Wenn Bob eine Anfrage von Alice über IPv4 erhält, muss Bob einen Charlie auswählen, der eine IPv4-Adresse bewirbt. Wenn Bob eine Anfrage von Alice über IPv6 erhält, muss Bob einen Charlie auswählen, der eine IPv6-Adresse bewirbt. Die tatsächliche Bob-Charlie-Kommunikation kann über IPv4 oder IPv6 erfolgen (d.h. unabhängig von Alices Adresstyp).

- Die Nachrichten 1-4 müssen in einer Data-Nachricht in einer bestehenden Sitzung enthalten sein.

- Bob muss Alices RI an Charlie senden, bevor er Nachricht 2 sendet.

- Bob muss Charlie's RI an Alice senden, bevor er Nachricht 4 sendet, falls akzeptiert (Ursachencode 0).

- Die Nachrichten 5-7 müssen in einer Peer Test-Nachricht außerhalb der Sitzung enthalten sein.

- Nachrichten 5 und 7 können dieselben signierten Daten enthalten, die in Nachrichten 3 und 4 gesendet wurden, oder sie können mit einem neuen Zeitstempel neu generiert werden. Signatur ist optional.

- Nachricht 6 kann dieselben signierten Daten enthalten, die in Nachrichten 1 und 2 gesendet wurden, oder sie kann mit einem neuen Zeitstempel neu generiert werden. Die Signatur ist optional.

Signaturen:

Alice signiert die Anfrage und fügt sie in Nachricht 1 ein; Bob leitet sie in Nachricht 2 an Charlie weiter. Charlie signiert die Antwort und fügt sie in Nachricht 3 ein; Bob leitet sie in Nachricht 4 an Alice weiter. Signatur-Algorithmus: Signieren oder verifizieren Sie die folgenden Daten mit dem Signaturschlüssel von Alice oder Charlie:

- prologue: 16 Bytes "PeerTestValidate", nicht null-terminiert (nicht in der Nachricht enthalten)
- bhash: Bobs 32-Byte router Hash (nicht in der Nachricht enthalten)
- ahash: Alices 32-Byte router Hash (Nur in der Signatur für Nachrichten 3 und 4 verwendet; nicht in Nachricht 3 oder 4 enthalten)
- ver: 1 Byte SSU Version
- nonce: 4 Byte Test-Nonce
- timestamp: 4 Byte Zeitstempel (Sekunden)
- asz: 1 Byte Endpunkt (Port + IP) Größe (6 oder 18)
- AlicePort: 2 Byte Alices Portnummer
- Alice IP: (asz - 2) Byte Alice IP-Adresse

#### NextNonce

TODO nur wenn wir Schlüssel rotieren

```
+----+----+----+----+----+----+----+----+

| 11 | size | TBD |

    +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 11 size :: 2 bytes, big endian, size of data to follow
```
#### Bestätigung

4 Byte ack through, gefolgt von einer ack-Anzahl und null oder mehr nack/ack-Bereichen.

Dieses Design ist von QUIC adaptiert und vereinfacht. Die Designziele sind wie folgt:

- Wir möchten ein "Bitfeld" effizient codieren, das eine Sequenz von Bits darstellt, die bestätigte Pakete repräsentiert.
- Das Bitfeld besteht hauptsächlich aus 1en. Sowohl die 1en als auch die 0en kommen im Allgemeinen in aufeinanderfolgenden "Klumpen" vor.
- Der verfügbare Platz im Paket für Bestätigungen variiert.
- Das wichtigste Bit ist das mit der höchsten Nummer. Bits mit niedrigeren Nummern sind weniger wichtig. Unterhalb einer bestimmten Entfernung vom höchsten Bit werden die ältesten Bits "vergessen" und nie wieder gesendet.

Die unten spezifizierte Kodierung erreicht diese Designziele, indem sie die Nummer des höchsten Bits sendet, das auf 1 gesetzt ist, zusammen mit zusätzlichen aufeinanderfolgenden Bits darunter, die ebenfalls auf 1 gesetzt sind. Danach, falls Platz vorhanden ist, einen oder mehrere "Bereiche", die die Anzahl der aufeinanderfolgenden 0-Bits und aufeinanderfolgenden 1-Bits darunter spezifizieren. Siehe QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) Abschnitt 13.2.3 für weitere Hintergrundinformationen.

```
+----+----+----+----+----+----+----+----+

| 12 | size | Ack Through [|acnt|](##SUBST##|acnt|)

    +-------------+-------------+
    | > range     | > range     |
    +-------------+-------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 12 size :: 2 bytes, big endian, size of data to follow, 5 minimum ack through :: highest packet number acked acnt :: number of acks lower than ack through also acked, 0-255 range :: If present, 1 byte nack count followed by 1 byte ack count, 0-255 each
```
Beispiele:

Wir möchten nur Paket 10 bestätigen:

- Ack Through: 10
- acnt: 0
- keine Bereiche sind enthalten

Wir möchten nur die Pakete 8-10 bestätigen:

- Ack Through: 10
- acnt: 2
- keine Bereiche sind enthalten

Wir möchten 10 9 8 6 5 2 1 0 bestätigen (ACK) und 7 4 3 nicht bestätigen (NACK). Die Kodierung des ACK-Blocks ist:

- Ack Through: 10
- acnt: 2 (ack 9 8)
- range: 1 2 (nack 7, ack 6 5)
- range: 2 3 (nack 4 3, ack 2 1 0)

Hinweise:

- Bereiche müssen nicht vorhanden sein. Die maximale Anzahl von Bereichen ist nicht spezifiziert, es können so viele sein, wie in das Paket passen.
- Range nack kann null sein, wenn mehr als 255 aufeinanderfolgende Pakete bestätigt werden.
- Range ack kann null sein, wenn mehr als 255 aufeinanderfolgende Pakete nicht bestätigt werden.
- Range nack und ack dürfen nicht beide null sein.
- Nach dem letzten Bereich werden Pakete weder bestätigt noch nicht bestätigt. Die Länge des ack-Blocks und wie alte acks/nacks behandelt werden, liegt beim Sender des ack-Blocks. Siehe ack-Abschnitte unten für weitere Diskussion.
- Das ack through sollte die höchste empfangene Paketnummer sein, und alle höheren Pakete wurden nicht empfangen. In begrenzten Situationen könnte es jedoch niedriger sein, wie etwa bei der Bestätigung eines einzelnen Pakets, das "eine Lücke füllt", oder einer vereinfachten Implementierung, die den Zustand aller empfangenen Pakete nicht verwaltet. Über dem höchsten empfangenen Paket werden Pakete weder bestätigt noch nicht bestätigt, aber nach mehreren ack-Blöcken kann es angebracht sein, in den schnellen Wiederübertragungsmodus zu wechseln.
- Dieses Format ist eine vereinfachte Version des in QUIC verwendeten. Es ist darauf ausgelegt, eine große Anzahl von ACKs zusammen mit Bursts von NACKs effizient zu kodieren.
- ACK-Blöcke werden verwendet, um Datenphase-Pakete zu bestätigen. Sie sollen nur für Datenphase-Pakete innerhalb der Sitzung einbezogen werden.

#### Adresse

2-Byte-Port und 4- oder 16-Byte-IP-Adresse. Alices Adresse, von Bob an Alice gesendet, oder Bobs Adresse, von Alice an Bob gesendet.

```
+----+----+----+----+----+----+----+----+

| 13 | 6 or 18 | Port | IP Address

    +----+----+----+----+----+----+----+----+

    :   | 

    +----+

    blk :: 13 size :: 2 bytes, big endian, 6 or 18 port :: 2 bytes, big endian ip :: 4 byte IPv4 or 16 byte IPv6 address, big endian (network byte order)
```
#### Relay Tag Anfrage

Dies kann von Alice in einer Session Request, Session Confirmed oder Data-Nachricht gesendet werden. Wird in der Session Created-Nachricht nicht unterstützt, da Bob noch keine RI von Alice hat und nicht weiß, ob Alice relay unterstützt. Außerdem benötigt Bob wahrscheinlich keine Introducer, wenn er eine eingehende Verbindung erhält (außer vielleicht für den anderen Typ ipv4/ipv6).

Wenn es in der Session Request gesendet wird, kann Bob mit einem Relay Tag in der Session Created Nachricht antworten, oder er kann warten, bis er Alices RouterInfo in der Session Confirmed erhält, um Alices Identität zu validieren, bevor er in einer Data Nachricht antwortet. Wenn Bob nicht für Alice weiterleiten möchte, sendet er keinen Relay Tag Block.

```
+----+----+----+

| 15 | 0 |

    +----+----+----+

    blk :: 15 size :: 2 bytes, big endian, value = 0
```
#### Relay Tag

Dies kann von Bob in einer Session Confirmed oder Data-Nachricht gesendet werden, als Antwort auf eine Relay Tag Request von Alice.

Wenn die Relay Tag Request in der Session Request gesendet wird, kann Bob mit einem Relay Tag in der Session Created Nachricht antworten, oder er kann warten, bis er Alices RouterInfo in der Session Confirmed erhält, um Alices Identität zu validieren, bevor er in einer Data-Nachricht antwortet. Wenn Bob nicht für Alice weiterleiten möchte, sendet er keinen Relay Tag Block.

```
+----+----+----+----+----+----+----+

| 16 | 4 | relay tag |

    +----+----+----+----+----+----+----+

    blk :: 16 size :: 2 bytes, big endian, value = 4 relay tag :: 4 bytes, big endian, nonzero
```
#### Neuer Token

Für eine nachfolgende Verbindung. Normalerweise in den Session Created und Session Confirmed Nachrichten enthalten. Kann auch erneut in der Data-Nachricht einer langlebigen Session gesendet werden, wenn das vorherige Token abläuft.

```
+----+----+----+----+----+----+----+----+

| 17 | 12 | expires |

    +----+----+----+----+----+----+----+----+

    :   token |

    +----+----+----+----+----+----+----+

    blk :: 17 size :: 2 bytes, big endian, value = 12 expires :: Unix timestamp, unsigned seconds. Wraps around in 2106 token :: 8 bytes, big endian
```
#### Pfad-Herausforderung

Ein Ping mit beliebigen Daten, die in einer Path Response zurückgegeben werden sollen, verwendet als Keep-Alive oder zur Validierung einer IP/Port-Änderung.

```
+----+----+----+----+----+----+----+----+

| 18 | size | Arbitrary Data |

    +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 18 size :: 2 bytes, big endian, size of data to follow data :: Arbitrary data to be returned in a Path Response length as selected by sender
```
Hinweise:

- Eine minimale Datengröße von 8 Bytes, die zufällige Daten enthält, wird empfohlen, ist aber nicht erforderlich.
- Die maximale Größe ist nicht spezifiziert, sollte aber deutlich unter 1280 liegen, da die PMTU während der Pfadvalidierungsphase 1280 beträgt.
- Große Challenge-Größen werden nicht empfohlen, da sie einen Vektor für Paketverstärkungsangriffe darstellen könnten.

#### Pfad-Antwort

Ein Pong mit den im Path Challenge empfangenen Daten, als Antwort auf die Path Challenge, verwendet als Keep-Alive oder zur Validierung einer IP/Port-Änderung.

```
+----+----+----+----+----+----+----+----+

| 19 | size | |

    +----+----+----+ + | Data received in Path Challenge | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 19 size :: 2 bytes, big endian, size of data to follow data :: As received in a Path Challenge
```
#### Erste Paketnummer

Optional im Handshake in jede Richtung enthalten, um die erste Paketnummer anzugeben, die gesendet wird. Dies bietet mehr Sicherheit für die Header-Verschlüsselung, ähnlich wie bei TCP.

Nicht vollständig spezifiziert, derzeit nicht unterstützt.

```
+----+----+----+----+----+----+----+

| 20 | size | First pkt number |

    +----+----+----+----+----+----+----+

    blk :: 20 size :: 4 pkt num :: The first packet number to be sent in the data phase
```
#### Überlastung

Dieser Block ist als erweiterbare Methode zum Austausch von Congestion-Control-Informationen konzipiert. Congestion Control kann komplex sein und sich weiterentwickeln, während wir mehr Erfahrungen mit dem Protokoll in Live-Tests sammeln oder nach der vollständigen Einführung.

Dies hält alle Stauinformationen aus den stark genutzten I2NP-, First Fragment-, Followon Fragment- und ACK-Blöcken heraus, wo kein Platz für Flags vorgesehen ist. Obwohl es drei Bytes ungenutzter Flags im Data-Paket-Header gibt, bietet dies auch nur begrenzten Raum für Erweiterbarkeit und schwächeren Verschlüsselungsschutz.

Obwohl es etwas verschwenderisch ist, einen 4-Byte-Block für zwei Informationsbits zu verwenden, können wir ihn durch die Verwendung eines separaten Blocks einfach mit zusätzlichen Daten wie aktuellen Fenstergrößen, gemessener RTT oder anderen Flags erweitern. Die Erfahrung hat gezeigt, dass Flag-Bits allein oft unzureichend und unhandlich für die Implementierung fortgeschrittener Congestion-Control-Schemata sind. Der Versuch, Unterstützung für jede mögliche Congestion-Control-Funktion beispielsweise in den ACK-Block einzubauen, würde Platz verschwenden und die Komplexität beim Parsing dieses Blocks erhöhen.

Implementierungen sollten nicht davon ausgehen, dass der andere Router ein bestimmtes Flag-Bit oder eine hier enthaltene Funktion unterstützt, es sei denn, die Implementierung wird durch eine zukünftige Version dieser Spezifikation gefordert.

Dieser Block sollte wahrscheinlich der letzte Nicht-Padding-Block in der Nutzlast sein.

```
+----+----+----+----+

| 21 | size [|flag|](##SUBST##|flag|)

    +----+----+----+----+

    blk :: 21 size :: 1 (or more if extended) flag :: 1 byte flags bit order: 76543210 (bit 7 is MSB) bit 0: 1 to request immediate ack bit 1: 1 for explicit congestion notification (ECN) bits 7-2: Unused, set to 0 for future compatibility
```
#### Padding

Dies dient zum Padding innerhalb von AEAD-Payloads. Padding für alle Nachrichten befindet sich innerhalb von AEAD-Payloads.

Das Padding sollte ungefähr den ausgehandelten Parametern entsprechen. Bob sendete seine angeforderten tx/rx min/max Parameter in Session Created. Alice sendete ihre angeforderten tx/rx min/max Parameter in Session Confirmed. Aktualisierte Optionen können während der Datenphase gesendet werden. Siehe Informationen zum Optionsblock oben.

Falls vorhanden, muss dies der letzte Block in der Nutzlast sein.

```
+----+----+----+----+----+----+----+----+

[|254 |](##SUBST##|254 |) size | padding | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 254 size :: 2 bytes, big endian, size of padding to follow padding :: random data
```
Hinweise:

- Size = 0 ist erlaubt.
- Padding-Strategien sind noch zu bestimmen.
- Minimales Padding ist noch zu bestimmen.
- Payloads, die nur aus Padding bestehen, sind erlaubt.
- Standard-Padding-Werte sind noch zu bestimmen.
- Siehe Optionsblock für die Aushandlung von Padding-Parametern
- Siehe Optionsblock für min/max Padding-Parameter
- Die MTU darf nicht überschritten werden. Falls mehr Padding erforderlich ist, senden Sie mehrere Nachrichten.
- Die Router-Antwort bei Verletzung von ausgehandelten Padding-Regeln ist implementierungsabhängig.
- Die Padding-Länge sollte entweder pro Nachricht basierend auf Schätzungen der Längenverteilung bestimmt werden, oder es sollten zufällige Verzögerungen hinzugefügt werden. Diese Gegenmaßnahmen sollen zur Resistenz gegen DPI (Deep Packet Inspection) beitragen, da Nachrichtengrößen andernfalls verraten würden, dass I2P-Traffic über das Transportprotokoll übertragen wird. Das genaue Padding-Schema ist ein Bereich zukünftiger Arbeit, Anhang A von [NTCP2](/docs/specs/ntcp2) bietet weitere Informationen zu diesem Thema.

## Replay-Schutz

SSU2 ist darauf ausgelegt, die Auswirkungen von Nachrichten zu minimieren, die von einem Angreifer wiederholt werden.

Token Request, Retry, Session Request, Session Created, Hole Punch und out-of-session Peer Test Nachrichten müssen DateTime-Blöcke enthalten.

Sowohl Alice als auch Bob validieren, dass die Zeit für diese Nachrichten innerhalb einer gültigen Abweichung liegt (empfohlen +/- 2 Minuten). Für "probing resistance" sollte Bob nicht auf Token Request oder Session Request Nachrichten antworten, wenn die Abweichung ungültig ist, da diese Nachrichten möglicherweise ein Replay- oder Probing-Angriff sind.

Bob kann sich dafür entscheiden, doppelte Token Request- und Retry-Nachrichten abzulehnen, selbst wenn die Abweichung gültig ist, über einen Bloom-Filter oder einen anderen Mechanismus. Die Größe und CPU-Kosten für die Beantwortung dieser Nachrichten sind jedoch gering. Im schlimmsten Fall kann eine wiedergesendete Token Request-Nachricht ein zuvor gesendetes Token ungültig machen.

Das Token-System minimiert die Auswirkungen von wiederholten Session Request-Nachrichten erheblich. Da Tokens nur einmal verwendet werden können, wird eine wiederholte Session Request-Nachricht niemals ein gültiges Token haben. Bob kann sich dafür entscheiden, doppelte Session Request-Nachrichten abzulehnen, selbst wenn der Skew gültig ist, über einen Bloom-Filter oder einen anderen Mechanismus. Die Größe und CPU-Kosten für die Antwort mit einer Retry-Nachricht sind jedoch gering. Im schlimmsten Fall kann das Senden einer Retry-Nachricht ein zuvor gesendetes Token ungültig machen.

Doppelte Session Created und Session Confirmed Nachrichten werden nicht validiert, da der Noise-Handshake-Status nicht im korrekten Zustand sein wird, um sie zu entschlüsseln. Im schlimmsten Fall kann ein Peer eine Session Confirmed als Antwort auf eine scheinbar doppelte Session Created erneut übertragen.

Wiederholte Hole Punch und Peer Test Nachrichten sollten wenig bis gar keine Auswirkungen haben.

Router müssen die Paketnummer der Datennachricht verwenden, um doppelte Datenphase-Nachrichten zu erkennen und zu verwerfen. Jede Paketnummer sollte nur einmal verwendet werden. Wiederholte Nachrichten müssen ignoriert werden.

## Handshake-Neuübertragung

### Sitzungsanfrage

Wenn Alice keine Session Created oder Retry erhält:

Behalten Sie dieselben Quell- und Verbindungs-IDs, ephemeren Schlüssel und Paketnummer 0 bei. Oder behalten und übertragen Sie einfach dasselbe verschlüsselte Paket erneut. Die Paketnummer darf nicht erhöht werden, da dies den verketteten Hash-Wert ändern würde, der zur Verschlüsselung der Session Created-Nachricht verwendet wird.

Empfohlene Wiederübertragungsintervalle: 1,25, 2,5 und 5 Sekunden (1,25, 3,75 und 8,75 Sekunden nach dem ersten Senden). Empfohlener Timeout: 15 Sekunden insgesamt

### Session erstellt

Wenn Bob keine Session Confirmed erhält:

Behalte dieselben Quell- und Verbindungs-IDs, ephemeren Schlüssel und Paketnummer 0 bei. Oder behalte einfach das verschlüsselte Paket. Die Paketnummer darf nicht erhöht werden, da dies den verketteten Hash-Wert ändern würde, der zur Verschlüsselung der Session Confirmed Nachricht verwendet wird.

Empfohlene Übertragungswiederholungsintervalle: 1, 2 und 4 Sekunden (1, 3 und 7 Sekunden nach dem ersten Senden). Empfohlenes Timeout: 12 Sekunden insgesamt

### Sitzung bestätigt

In SSU 1 wechselt Alice nicht in die Datenphase, bis das erste Datenpaket von Bob empfangen wird. Dies macht SSU 1 zu einem Setup mit zwei Roundtrips.

Für SSU 2, empfohlene Session Confirmed Wiederübertragungsintervalle: 1,25, 2,5 und 5 Sekunden (1,25, 3,75 und 8,75 Sekunden nach dem ersten Senden).

Es gibt mehrere Alternativen. Alle haben 1 RTT:

1) Alice nimmt an, dass Session Confirmed empfangen wurde, sendet Datennachrichten sofort und überträgt Session Confirmed niemals erneut. Datenpakete, die außerhalb der Reihenfolge empfangen werden (vor Session Confirmed), sind nicht entschlüsselbar, werden aber erneut übertragen. Wenn Session Confirmed verloren geht, werden alle gesendeten Datennachrichten verworfen. 2) Wie in 1), sende Datennachrichten sofort, aber übertrage auch Session Confirmed erneut, bis eine Datennachricht empfangen wird. 3) Wir könnten IK anstelle von XK verwenden, da es nur zwei Nachrichten im Handshake hat, aber es verwendet einen zusätzlichen DH (4 statt 3).

Die empfohlene Implementierung ist Option 2). Alice muss die Informationen behalten, die für die Neuübertragung der Session Confirmed Nachricht erforderlich sind. Alice sollte auch alle Data-Nachrichten nach der Neuübertragung der Session Confirmed Nachricht erneut übertragen.

Beim erneuten Senden von Session Confirmed müssen dieselben Quell- und Verbindungs-IDs, der ephemeral key und die Paketnummer 1 beibehalten werden. Oder bewahren Sie einfach das verschlüsselte Paket auf. Die Paketnummer darf nicht erhöht werden, da dies den verketteten Hash-Wert ändern würde, der ein Eingabeparameter für die split()-Funktion ist.

Bob kann die Datennachrichten, die vor der Session Confirmed-Nachricht empfangen wurden, behalten (in die Warteschlange einreihen). Weder die Header-Schutzschlüssel noch die Entschlüsselungsschlüssel sind verfügbar, bevor die Session Confirmed-Nachricht empfangen wird, daher weiß Bob nicht, dass es sich um Datennachrichten handelt, aber das kann angenommen werden. Nachdem die Session Confirmed-Nachricht empfangen wurde, ist Bob in der Lage, die in der Warteschlange befindlichen Datennachrichten zu entschlüsseln und zu verarbeiten. Falls dies zu komplex ist, kann Bob die nicht entschlüsselbaren Datennachrichten einfach verwerfen, da Alice sie erneut übertragen wird.

Hinweis: Wenn die session confirmed Pakete verloren gehen, wird Bob session created erneut übertragen. Der session created Header wird nicht mit Alices intro key entschlüsselbar sein, da er mit Bobs intro key gesetzt ist (es sei denn, eine Fallback-Entschlüsselung wird mit Bobs intro key durchgeführt). Bob kann die session confirmed Pakete sofort erneut übertragen, falls sie zuvor nicht bestätigt wurden und ein nicht entschlüsselbares Paket empfangen wird.

### Token-Anfrage

Wenn Alice keine Retry erhält:

Dieselben Quell- und Verbindungs-IDs beibehalten. Eine Implementierung kann eine neue zufällige Paketnummer generieren und ein neues Paket verschlüsseln; oder sie kann dieselbe Paketnummer wiederverwenden oder einfach dasselbe verschlüsselte Paket beibehalten und erneut übertragen. Die Paketnummer darf nicht erhöht werden, da dies den verketteten Hash-Wert ändern würde, der zur Verschlüsselung der Session Created Nachricht verwendet wird.

Empfohlene Übertragungswiederholungsintervalle: 3 und 6 Sekunden (3 und 9 Sekunden nach dem ersten Senden). Empfohlene Zeitüberschreitung: 15 Sekunden insgesamt

### Wiederholen

Wenn Bob keine Session Confirmed erhält:

Eine Retry-Nachricht wird bei einem Timeout nicht erneut übertragen, um die Auswirkungen gefälschter Quelladressen zu reduzieren.

Eine Retry-Nachricht kann jedoch als Antwort auf eine wiederholte Session Request-Nachricht, die mit dem ursprünglichen (ungültigen) Token empfangen wurde, oder als Antwort auf eine wiederholte Token Request-Nachricht erneut übertragen werden. In beiden Fällen deutet dies darauf hin, dass die Retry-Nachricht verloren gegangen ist.

Wenn eine zweite Session Request-Nachricht mit einem anderen, aber immer noch ungültigen Token empfangen wird, verwerfe die ausstehende Session und antworte nicht.

Beim erneuten Senden der Retry-Nachricht: Behalten Sie dieselben Quell- und Verbindungs-IDs sowie das Token bei. Eine Implementierung kann eine neue zufällige Paketnummer generieren und ein neues Paket verschlüsseln; oder sie kann dieselbe Paketnummer wiederverwenden oder einfach dasselbe verschlüsselte Paket beibehalten und erneut übertragen.

### Gesamtzeit-Timeout

Die empfohlene Gesamtzeit für das Timeout beim Handshake beträgt 20 Sekunden.

### Duplikate und Fehlerbehandlung

Duplikate der drei Noise-Handshake-Nachrichten Session Request, Session Created und Session Confirmed müssen vor MixHash() des Headers erkannt werden. Während die Noise AEAD-Verarbeitung danach vermutlich fehlschlagen wird, wäre der Handshake-Hash bereits beschädigt.

Wenn eine der drei Nachrichten beschädigt ist und AEAD fehlschlägt, kann der Handshake anschließend nicht wiederhergestellt werden, selbst bei einer erneuten Übertragung, da MixHash() bereits auf die beschädigte Nachricht angewendet wurde.

## Tokens

Das Token im Session Request Header wird zur DoS-Abwehr, zur Verhinderung von Quelladress-Spoofing und als Schutz vor Replay-Angriffen verwendet.

Wenn Bob das Token in der Session Request-Nachricht nicht akzeptiert, entschlüsselt Bob die Nachricht NICHT, da dies eine aufwändige DH-Operation erfordert. Bob sendet einfach eine Retry-Nachricht mit einem neuen Token.

Wenn dann eine nachfolgende Session Request-Nachricht mit diesem Token empfangen wird, entschlüsselt Bob diese Nachricht und setzt den Handshake fort.

Das Token muss ein zufällig generierter 8-Byte-Wert sein, wenn der Generator des Tokens die Werte und die zugehörige IP-Adresse und den Port speichert (im Arbeitsspeicher oder dauerhaft). Der Generator darf keinen opaken Wert generieren, beispielsweise durch Verwendung des SipHash (mit einem geheimen Seed K0, K1) der IP-Adresse, des Ports und der aktuellen Stunde oder des aktuellen Tags, um Tokens zu erstellen, die nicht im Arbeitsspeicher gespeichert werden müssen, da diese Methode es schwierig macht, wiederverwendete Tokens und Replay-Angriffe abzulehnen. Es ist jedoch ein Thema für weitere Studien, ob wir zu einem solchen Schema migrieren können, wie es [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) macht, unter Verwendung eines 16-Byte-HMAC eines Servergeheimnisses und einer IP-Adresse.

Tokens dürfen nur einmal verwendet werden. Ein Token, das von Bob an Alice in einer Retry-Nachricht gesendet wird, muss sofort verwendet werden und läuft nach wenigen Sekunden ab. Ein Token, das in einem New Token-Block in einer etablierten Sitzung gesendet wird, kann in einer nachfolgenden Verbindung verwendet werden und läuft zu dem in diesem Block angegebenen Zeitpunkt ab. Das Ablaufdatum wird vom Sender festgelegt; empfohlene Werte sind mindestens mehrere Minuten, maximal eine oder mehrere Stunden, je nach gewünschtem maximalen Overhead der gespeicherten Tokens.

Wenn sich die IP-Adresse oder der Port eines routers ändert, muss er alle gespeicherten Tokens (sowohl eingehende als auch ausgehende) für die alte IP-Adresse oder den alten Port löschen, da sie nicht mehr gültig sind. Tokens können optional über router-Neustarts hinweg gespeichert werden, abhängig von der Implementierung. Die Annahme eines nicht abgelaufenen Tokens ist nicht garantiert; wenn Bob seine gespeicherten Tokens vergessen oder gelöscht hat, wird er einen Retry an Alice senden. Ein router kann wählen, die Token-Speicherung zu begrenzen und die ältesten gespeicherten Tokens zu entfernen, auch wenn sie noch nicht abgelaufen sind.

New Token-Blöcke können von Alice zu Bob oder von Bob zu Alice gesendet werden. Sie werden typischerweise mindestens einmal gesendet, während oder kurz nach der Sitzungserrichtung. Aufgrund der Validierungsüberprüfungen der RouterInfo in der Session Confirmed-Nachricht sollte Bob keinen New Token-Block in der Session Created-Nachricht senden. Er kann mit dem ACK 0 und der Router Info gesendet werden, nachdem die Session Confirmed empfangen und validiert wurde.

Da die Lebensdauer von Sessions oft länger ist als die Token-Ablaufzeit, sollte das Token vor oder nach dem Ablauf mit einer neuen Ablaufzeit erneut gesendet werden, oder ein neues Token sollte gesendet werden. Router sollten davon ausgehen, dass nur das zuletzt empfangene Token gültig ist; es gibt keine Anforderung, mehrere eingehende oder ausgehende Token für dieselbe IP/Port zu speichern.

Ein Token ist an die Kombination aus Quell-IP/Port und Ziel-IP/Port gebunden. Ein Token, das über IPv4 empfangen wurde, darf nicht für IPv6 verwendet werden oder umgekehrt.

Wenn einer der beiden Peers während der Sitzung zu einer neuen IP oder einem neuen Port migriert (siehe Abschnitt Connection Migration), werden alle zuvor ausgetauschten Token ungültig und neue Token müssen ausgetauscht werden.

Implementierungen können Token auf der Festplatte speichern und beim Neustart wieder laden, sind dazu aber nicht verpflichtet. Falls sie gespeichert werden, muss die Implementierung sicherstellen, dass sich IP und Port seit dem Herunterfahren nicht geändert haben, bevor sie wieder geladen werden.

## I2NP-Nachrichtenfragmentierung

Unterschiede zu SSU 1

Hinweis: Wie bei SSU 1 enthält das erste Fragment keine Informationen über die Gesamtanzahl der Fragmente oder die Gesamtlänge. Nachfolgende Fragmente enthalten keine Informationen über ihren Versatz. Dies gibt dem Sender die Flexibilität, "on the fly" zu fragmentieren, basierend auf dem verfügbaren Platz im Paket. (Java I2P macht dies nicht; es "pre-fragmentiert" bevor das erste Fragment gesendet wird) Allerdings belastet es den Empfänger, Fragmente zu speichern, die in falscher Reihenfolge empfangen werden, und die Reassemblierung zu verzögern, bis alle Fragmente empfangen wurden.

Wie in SSU 1 muss jede Neuübertragung von Fragmenten die Länge (und den impliziten Offset) der vorherigen Übertragung des Fragments beibehalten.

SSU 2 trennt die drei Fälle (vollständige Nachricht, erstes Fragment und Folge-Fragment) in drei verschiedene Blocktypen, um die Verarbeitungseffizienz zu verbessern.

## I2NP Nachrichten-Duplizierung

Dieses Protokoll verhindert NICHT vollständig die doppelte Zustellung von I2NP-Nachrichten. IP-Layer-Duplikate oder Replay-Angriffe werden auf der SSU2-Ebene erkannt, da jede Paketnummer nur einmal verwendet werden darf.

Wenn I2NP-Nachrichten oder -Fragmente jedoch in neuen Paketen erneut übertragen werden, ist dies auf der SSU2-Schicht nicht erkennbar. Der Router sollte die I2NP-Ablaufzeit durchsetzen (sowohl zu alt als auch zu weit in der Zukunft) und einen Bloom-Filter oder einen anderen Mechanismus verwenden, der auf der I2NP-Nachrichten-ID basiert.

Zusätzliche Mechanismen können vom router oder in der SSU2-Implementierung verwendet werden, um Duplikate zu erkennen. Beispielsweise könnte SSU2 einen Cache kürzlich empfangener Nachrichten-IDs verwalten. Dies ist implementierungsabhängig.

## Überlastungskontrolle

Diese Spezifikation definiert das Protokoll für Paketnummerierung und ACK-Blöcke. Dies bietet ausreichende Echtzeitinformationen für einen Sender, um einen effizienten und reaktionsfähigen Congestion-Control-Algorithmus zu implementieren, während Flexibilität und Innovation bei dieser Implementierung ermöglicht wird. Dieser Abschnitt behandelt Implementierungsziele und bietet Vorschläge. Allgemeine Anleitung findet sich in [RFC-9002](https://tools.ietf.org/html/rfc9002). Siehe auch [RFC-6298](https://tools.ietf.org/html/rfc6298) für Anleitung zu Retransmission-Timern.

Reine ACK-Datenpakete sollten nicht für Bytes oder Pakete im Flug zählen und sind nicht staukontrolliert. Anders als bei TCP kann SSU2 den Verlust dieser Pakete erkennen und diese Information kann zur Anpassung des Staukontrollzustands verwendet werden. Dieses Dokument spezifiziert jedoch keinen Mechanismus dafür.

Pakete, die andere Nicht-Daten-Blöcke enthalten, können bei Bedarf auch von der Staukontrolle ausgeschlossen werden, implementierungsabhängig. Zum Beispiel:

- Peer Test
- Relay-Anfrage/Intro/Antwort
- Pfad-Challenge/Antwort

Es wird empfohlen, dass die Überlastungskontrolle auf der Byte-Anzahl basiert, nicht auf der Paket-Anzahl, entsprechend den Richtlinien in den TCP RFCs und QUIC [RFC-9002](https://tools.ietf.org/html/rfc9002). Ein zusätzliches Paket-Anzahl-Limit kann ebenfalls nützlich sein, um Pufferüberläufe im Kernel oder in Middleboxes zu verhindern, implementierungsabhängig, obwohl dies erhebliche Komplexität hinzufügen kann. Wenn die Paketausgabe pro Session und/oder insgesamt bandbreitenbegrenzt und/oder zeitgesteuert ist, kann dies die Notwendigkeit einer Paket-Anzahl-Begrenzung verringern.

### Paketnummern

In SSU 1 enthielten ACKs und NACKs I2NP-Nachrichtennummern und Fragment-Bitmasken. Sender verfolgten den ACK-Status ausgehender Nachrichten (und ihrer Fragmente) und übertrugen Fragmente bei Bedarf erneut.

In SSU 2 enthalten ACKs und NACKs Paketnummern. Sender müssen eine Datenstruktur mit einer Zuordnung von Paketnummern zu deren Inhalten verwalten. Wenn ein Paket ACKed oder NACKed wird, muss der Sender bestimmen, welche I2NP-Nachrichten und Fragmente in diesem Paket waren, um zu entscheiden, was erneut übertragen werden soll.

### Session Confirmed ACK

Bob sendet eine ACK für Paket 0, die die Session Confirmed-Nachricht bestätigt und es Alice erlaubt, zur Datenphase überzugehen und die große Session Confirmed-Nachricht zu verwerfen, die für eine mögliche Wiederübertragung gespeichert wurde. Dies ersetzt die DeliveryStatusMessage, die Bob in SSU 1 gesendet hat.

Bob sollte eine ACK so schnell wie möglich nach Erhalt der Session Confirmed-Nachricht senden. Eine kleine Verzögerung (nicht mehr als 50 ms) ist akzeptabel, da mindestens eine Data-Nachricht fast unmittelbar nach der Session Confirmed-Nachricht eintreffen sollte, so dass die ACK sowohl die Session Confirmed- als auch die Data-Nachricht bestätigen kann. Dies verhindert, dass Bob die Session Confirmed-Nachricht erneut übertragen muss.

### ACKs generieren

Definition: Bestätigungs-auslösende Pakete: Pakete, die bestätigungs-auslösende Blöcke enthalten, lösen eine Bestätigung (ACK) vom Empfänger innerhalb der maximalen Bestätigungsverzögerung aus und werden bestätigungs-auslösende Pakete genannt.

Router bestätigen alle Pakete, die sie empfangen und verarbeiten. Jedoch verursachen nur bestätigungspflichtige Pakete, dass ein ACK-Block innerhalb der maximalen Bestätigungsverzögerung gesendet wird. Pakete, die nicht bestätigungspflichtig sind, werden nur bestätigt, wenn ein ACK-Block aus anderen Gründen gesendet wird.

Beim Senden eines Pakets aus beliebigem Grund sollte ein Endpunkt versuchen, einen ACK-Block einzuschließen, falls kürzlich keiner gesendet wurde. Dies hilft bei der rechtzeitigen Verlusterkennung beim Peer.

Im Allgemeinen verbessert häufiges Feedback von einem Empfänger die Reaktion auf Verluste und Überlastung, aber dies muss gegen die übermäßige Last abgewogen werden, die durch einen Empfänger entsteht, der als Antwort auf jedes bestätigungspflichtige Paket einen ACK-Block sendet. Die unten angebotene Anleitung versucht, dieses Gleichgewicht zu finden.

In-Session-Datenpakete, die einen beliebigen Block enthalten, AUSSER den folgenden, lösen eine Bestätigung aus:

- ACK-Block
- Adress-Block
- DateTime-Block
- Padding-Block
- Termination-Block
- Andere?

Out-of-session-Pakete, einschließlich Handshake-Nachrichten und Peer-Test-Nachrichten 5-7, haben ihre eigenen Bestätigungsmechanismen. Siehe unten.

### Handshake-Bestätigungen

Dies sind Sonderfälle:

- Token Request wird implizit durch Retry bestätigt
- Session Request wird implizit durch Session Created oder Retry bestätigt
- Retry wird implizit durch Session Request bestätigt
- Session Created wird implizit durch Session Confirmed bestätigt
- Session Confirmed sollte sofort bestätigt werden

### Senden von ACK-Blöcken

ACK-Blöcke werden verwendet, um Datenphase-Pakete zu bestätigen. Sie sollen nur für Datenphase-Pakete innerhalb einer Sitzung eingefügt werden.

Jedes Paket sollte mindestens einmal bestätigt werden, und Pakete, die eine Bestätigung erfordern, müssen mindestens einmal innerhalb einer maximalen Verzögerung bestätigt werden.

Ein Endpunkt muss alle bestätigungsanforderenden Handshake-Pakete sofort innerhalb seiner maximalen Verzögerung bestätigen, mit folgender Ausnahme. Vor der Handshake-Bestätigung verfügt ein Endpunkt möglicherweise nicht über die Paketkopf-Verschlüsselungsschlüssel zum Entschlüsseln der Pakete beim Empfang. Er kann sie daher puffern und bestätigen, wenn die erforderlichen Schlüssel verfügbar werden.

Da Pakete, die nur ACK-Blöcke enthalten, nicht überlastungskontrolliert sind, darf ein Endpunkt nicht mehr als ein solches Paket als Antwort auf den Empfang eines ACK-auslösenden Pakets senden.

Ein Endpunkt darf kein non-ack-eliciting Paket als Antwort auf ein non-ack-eliciting Paket senden, auch wenn Paketlücken vor dem empfangenen Paket vorhanden sind. Dies vermeidet eine unendliche Rückkopplungsschleife von Bestätigungen, die verhindern könnte, dass die Verbindung jemals inaktiv wird. Non-ack-eliciting Pakete werden schließlich bestätigt, wenn der Endpunkt einen ACK-Block als Antwort auf andere Ereignisse sendet.

Ein Endpunkt, der nur ACK-Blöcke sendet, wird keine Bestätigungen von seinem Peer erhalten, es sei denn, diese Bestätigungen sind in Paketen mit ack-auslösenden Blöcken enthalten. Ein Endpunkt sollte einen ACK-Block mit anderen Blöcken senden, wenn neue ack-auslösende Pakete zu bestätigen sind. Wenn nur nicht-ack-auslösende Pakete bestätigt werden müssen, KANN ein Endpunkt wählen, keinen ACK-Block mit ausgehenden Blöcken zu senden, bis ein ack-auslösendes Paket empfangen wurde.

Ein Endpunkt, der nur Pakete sendet, die keine Bestätigung erfordern, könnte gelegentlich einen bestätigungspflichtigen Block zu diesen Paketen hinzufügen, um sicherzustellen, dass er eine Bestätigung erhält. In diesem Fall DARF ein Endpunkt NICHT in allen Paketen, die andernfalls keine Bestätigung erfordern würden, einen bestätigungspflichtigen Block senden, um eine unendliche Rückkopplungsschleife von Bestätigungen zu vermeiden.

Um die Verlustertkennung beim Sender zu unterstützen, sollte ein Endpunkt unverzüglich einen ACK-Block generieren und senden, wenn er ein ACK-auslösendes Paket in einem der folgenden Fälle empfängt:

- Wenn das empfangene Paket eine Paketnummer hat, die kleiner ist als die eines anderen ack-eliciting Pakets, das empfangen wurde
- Wenn das Paket eine Paketnummer hat, die größer ist als die höchste Nummer eines empfangenen ack-eliciting Pakets und es fehlende Pakete zwischen diesem Paket und jenem Paket gibt.
- Wenn das ack-immediate Flag im Paketkopf gesetzt ist

Es wird erwartet, dass die Algorithmen widerstandsfähig gegenüber Empfängern sind, die den oben angebotenen Leitlinien nicht folgen. Eine Implementierung sollte jedoch nur nach sorgfältiger Abwägung der Leistungsauswirkungen einer Änderung von diesen Anforderungen abweichen, sowohl für Verbindungen des Endpunkts als auch für andere Nutzer des Netzwerks.

### ACK-Häufigkeit

Ein Empfänger bestimmt, wie häufig Bestätigungen als Antwort auf bestätigungspflichtige Pakete gesendet werden sollen. Diese Bestimmung beinhaltet einen Kompromiss.

Endpunkte sind auf rechtzeitige Bestätigungen angewiesen, um Verluste zu erkennen. Fensterbasierte Überlastungscontroller sind auf Bestätigungen angewiesen, um ihr Überlastungsfenster zu verwalten. In beiden Fällen kann das Verzögern von Bestätigungen die Leistung beeinträchtigen.

Andererseits reduziert die Verringerung der Häufigkeit von Paketen, die nur Bestätigungen enthalten, die Kosten für Paketübertragung und -verarbeitung an beiden Endpunkten. Dies kann den Verbindungsdurchsatz bei stark asymmetrischen Verbindungen verbessern und das Volumen des Bestätigungsverkehrs reduzieren, der die Kapazität des Rückpfads nutzt; siehe Abschnitt 3 von [RFC-3449](https://tools.ietf.org/html/rfc3449).

Ein Empfänger sollte einen ACK-Block senden, nachdem er mindestens zwei bestätigungspflichtige Pakete erhalten hat. Diese Empfehlung ist allgemeiner Natur und steht im Einklang mit den Empfehlungen für das Verhalten von TCP-Endpunkten [RFC-5681](https://tools.ietf.org/html/rfc5681). Kenntnisse über Netzwerkbedingungen, Kenntnisse über den Überlastungsregler des Peers oder weitere Forschung und Experimente könnten alternative Bestätigungsstrategien mit besseren Leistungsmerkmalen nahelegen.

Ein Empfänger kann mehrere verfügbare Pakete verarbeiten, bevor er entscheidet, ob er einen ACK-Block als Antwort senden soll. Im Allgemeinen sollte der Empfänger ein ACK nicht um mehr als RTT / 6 oder maximal 150 ms verzögern.

Das ack-immediate Flag im Datenpaket-Header ist eine Anfrage, dass der Empfänger bald nach dem Empfang eine Bestätigung sendet, wahrscheinlich innerhalb weniger ms. Grundsätzlich sollte der Empfänger eine sofortige ACK nicht um mehr als RTT / 16 oder maximal 5 ms verzögern.

### Immediate ACK Flag

Der Empfänger kennt die Sendepuffergröße des Senders nicht und weiß daher nicht, wie lange er warten soll, bevor er eine ACK sendet. Das Immediate-ACK-Flag im Datenpaket-Header ist ein wichtiger Weg, um maximalen Durchsatz zu erhalten, indem die effektive RTT minimiert wird. Das Immediate-ACK-Flag befindet sich in Header-Byte 13, Bit 0, d.h. (header[13] & 0x01). Wenn gesetzt, wird eine sofortige ACK angefordert. Siehe den Abschnitt über kurze Header oben für Details.

Es gibt verschiedene mögliche Strategien, die ein Sender verwenden kann, um zu bestimmen, wann das immediate-ack Flag gesetzt werden soll:

- Wird einmal alle N Pakete gesetzt, für ein kleines N
- Wird beim letzten Paket in einem Burst gesetzt
- Wird gesetzt, wenn das Sendefenster fast voll ist, zum Beispiel über 2/3 voll
- Wird bei allen Paketen mit retransmittierten Fragmenten gesetzt

Immediate ACK-Flags sollten nur bei Datenpaketen notwendig sein, die I2NP-Nachrichten oder Nachrichtenfragmente enthalten.

### ACK-Blockgröße

Wenn ein ACK-Block gesendet wird, sind ein oder mehrere Bereiche von bestätigten Paketen enthalten. Die Einbeziehung von Bestätigungen für ältere Pakete reduziert die Wahrscheinlichkeit von fälschlichen Neuübertragungen, die durch den Verlust zuvor gesendeter ACK-Blöcke verursacht werden, auf Kosten größerer ACK-Blöcke.

ACK-Blöcke sollten immer die zuletzt empfangenen Pakete bestätigen, und je mehr die Pakete außerhalb der Reihenfolge sind, desto wichtiger ist es, schnell einen aktualisierten ACK-Block zu senden, um zu verhindern, dass der Peer ein Paket als verloren erklärt und die darin enthaltenen Blöcke fälschlicherweise erneut überträgt. Ein ACK-Block muss in ein einzelnes Paket passen. Wenn dies nicht der Fall ist, werden ältere Bereiche (die mit den kleinsten Paketnummern) weggelassen.

Ein Empfänger begrenzt die Anzahl der ACK-Bereiche, die er sich merkt und in ACK-Blöcken sendet, sowohl um die Größe der ACK-Blöcke zu begrenzen als auch um Ressourcenerschöpfung zu vermeiden. Nach dem Erhalt von Bestätigungen für einen ACK-Block sollte der Empfänger aufhören, diese bestätigten ACK-Bereiche zu verfolgen. Sender können Bestätigungen für die meisten Pakete erwarten, aber dieses Protokoll garantiert nicht den Erhalt einer Bestätigung für jedes Paket, das der Empfänger verarbeitet.

Es ist möglich, dass das Beibehalten vieler ACK-Bereiche dazu führen könnte, dass ein ACK-Block zu groß wird. Ein Empfänger kann unbestätigte ACK-Bereiche verwerfen, um die ACK-Block-Größe zu begrenzen, auf Kosten erhöhter Neuübertragungen vom Sender. Dies ist notwendig, wenn ein ACK-Block zu groß wäre, um in ein Paket zu passen. Empfänger können die ACK-Block-Größe auch weiter begrenzen, um Platz für andere Blöcke zu bewahren oder um die Bandbreite zu begrenzen, die Bestätigungen verbrauchen.

Ein Empfänger muss einen ACK-Bereich beibehalten, es sei denn, er kann sicherstellen, dass er nachfolgend keine Pakete mit Nummern in diesem Bereich akzeptiert. Die Aufrechterhaltung einer minimalen Paketnummer, die ansteigt, wenn Bereiche verworfen werden, ist eine Möglichkeit, dies mit minimalem Zustand zu erreichen.

Empfänger können alle ACK-Bereiche verwerfen, müssen jedoch die größte Paketnummer beibehalten, die erfolgreich verarbeitet wurde, da diese zur Wiederherstellung von Paketnummern aus nachfolgenden Paketen verwendet wird.

Der folgende Abschnitt beschreibt einen beispielhaften Ansatz zur Bestimmung, welche Pakete in jedem ACK-Block bestätigt werden sollen. Obwohl das Ziel dieses Algorithmus darin besteht, eine Bestätigung für jedes verarbeitete Paket zu generieren, ist es dennoch möglich, dass Bestätigungen verloren gehen.

### Bereiche durch Verfolgung von ACK-Blöcken begrenzen

Wenn ein Paket mit einem ACK-Block gesendet wird, kann das Ack Through-Feld in diesem Block gespeichert werden. Wenn ein Paket mit einem ACK-Block bestätigt wird, kann der Empfänger aufhören, Pakete zu bestätigen, die kleiner oder gleich dem Ack Through-Feld im gesendeten ACK-Block sind.

Ein Empfänger, der nur Pakete sendet, die keine Bestätigung erfordern, wie z.B. ACK-Blöcke, könnte über einen längeren Zeitraum keine Bestätigung erhalten. Dies könnte dazu führen, dass der Empfänger den Zustand für eine große Anzahl von ACK-Blöcken über einen längeren Zeitraum aufrechterhält, und die von ihm gesendeten ACK-Blöcke könnten unnötig groß werden. In einem solchen Fall könnte ein Empfänger gelegentlich einen PING oder anderen kleinen bestätigungserfordernden Block senden, etwa einmal pro Rundlaufzeit, um eine ACK-Bestätigung vom Peer zu erhalten.

In Fällen ohne ACK-Block-Verlust ermöglicht dieser Algorithmus eine minimale Neuordnung von 1 RTT. In Fällen mit ACK-Block-Verlust und Neuordnung garantiert dieser Ansatz nicht, dass jede Bestätigung vom Sender gesehen wird, bevor sie nicht mehr im ACK-Block enthalten ist. Pakete könnten außer der Reihe empfangen werden, und alle nachfolgenden ACK-Blöcke, die sie enthalten, könnten verloren gehen. In diesem Fall könnte der Verlustwiederherstellungsalgorithmus falsche Übertragungen verursachen, aber der Sender wird weiterhin vorwärts fortschreiten.

### Überlastung

I2P-Transporte garantieren keine geordnete Zustellung von I2NP-Nachrichten. Daher verhindert der Verlust einer Data-Nachricht, die eine oder mehrere I2NP-Nachrichten oder Fragmente enthält, NICHT die Zustellung anderer I2NP-Nachrichten; es gibt keine Head-of-Line-Blockierung. Implementierungen sollten während der Verlustwiederherstellungsphase weiterhin neue Nachrichten senden, wenn das Sendefenster dies zulässt.

### Neuübertragung

Ein Sender sollte nicht den vollständigen Inhalt einer Nachricht speichern, um sie identisch erneut zu übertragen (außer bei Handshake-Nachrichten, siehe oben). Ein Sender muss jedes Mal, wenn er eine Nachricht sendet, Nachrichten mit aktuellen Informationen (ACKs, NACKs und unbestätigte Daten) zusammenstellen. Ein Sender sollte vermeiden, Informationen aus Nachrichten erneut zu übertragen, sobald diese bestätigt wurden. Dies schließt Nachrichten ein, die nach ihrer Verlusterklärung bestätigt werden, was bei Netzwerk-Neuordnung auftreten kann.

### Fenster

TBD. Allgemeine Richtlinien finden sich in [RFC-9002](https://tools.ietf.org/html/rfc9002).

## Verbindungsmigration

Die IP-Adresse oder der Port eines Peers kann sich während der Lebensdauer einer Sitzung ändern. Eine IP-Änderung kann durch IPv6-Rotation temporärer Adressen, ISP-gesteuerte periodische IP-Änderungen, einen mobilen Client, der zwischen WiFi und Mobilfunk-IPs wechselt, oder andere lokale Netzwerkänderungen verursacht werden. Eine Port-Änderung kann durch eine NAT-Neubindung verursacht werden, nachdem die vorherige Bindung abgelaufen ist.

Die IP-Adresse oder der Port eines Peers kann sich aufgrund verschiedener On-Path- und Off-Path-Angriffe zu ändern scheinen, einschließlich der Modifikation oder Einschleusung von Paketen.

Connection Migration ist der Prozess, durch den ein neuer Quell-Endpunkt (IP+Port) validiert wird, während Änderungen verhindert werden, die nicht validiert sind. Dieser Prozess ist eine vereinfachte Version dessen, was in QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) definiert ist. Dieser Prozess ist nur für die Datenphase einer Sitzung definiert. Migration ist während des Handshakes nicht erlaubt. Alle Handshake-Pakete müssen verifiziert werden, dass sie von derselben IP und demselben Port stammen wie zuvor gesendete und empfangene Pakete. Mit anderen Worten, die IP und der Port eines Peers müssen während des Handshakes konstant bleiben.

### Bedrohungsmodell

(Adaptiert von QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000))

#### Peer-Adress-Spoofing

Ein Peer kann seine Quelladresse fälschen, um einen Endpunkt dazu zu bringen, übermäßige Datenmengen an einen unwilligen Host zu senden. Wenn der Endpunkt deutlich mehr Daten sendet als der fälschende Peer, könnte Connection Migration verwendet werden, um das Datenvolumen zu verstärken, das ein Angreifer gegen ein Opfer erzeugen kann.

#### On-Path-Adress-Spoofing

Ein Angreifer, der sich im Übertragungsweg befindet, könnte eine unechte Verbindungsmigration verursachen, indem er ein Paket mit einer gefälschten Adresse kopiert und weiterleitet, sodass es vor dem ursprünglichen Paket ankommt. Das Paket mit der gefälschten Adresse wird als von einer migrierenden Verbindung stammend betrachtet, und das ursprüngliche Paket wird als Duplikat angesehen und verworfen. Nach einer unechten Migration wird die Validierung der Quelladresse fehlschlagen, da die Entität an der Quelladresse nicht über die notwendigen kryptographischen Schlüssel verfügt, um die Path Challenge zu lesen oder darauf zu antworten, die an sie gesendet wird, selbst wenn sie es wollte.

#### Off-Path-Paketweiterleitung

Ein Off-Path-Angreifer, der Pakete beobachten kann, könnte Kopien echter Pakete an Endpunkte weiterleiten. Wenn das kopierte Paket vor dem echten Paket ankommt, wird dies als NAT-Rebinding erscheinen. Jedes echte Paket wird als Duplikat verworfen. Wenn der Angreifer in der Lage ist, weiterhin Pakete weiterzuleiten, könnte er eine Migration zu einem Pfad über den Angreifer verursachen. Dies bringt den Angreifer auf den Pfad und gibt ihm die Möglichkeit, alle nachfolgenden Pakete zu beobachten oder zu verwerfen.

#### Datenschutz-Auswirkungen

QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) spezifiziert das Ändern von Verbindungs-IDs beim Wechsel von Netzwerkpfaden. Die Verwendung einer stabilen Verbindungs-ID auf mehreren Netzwerkpfaden würde es einem passiven Beobachter ermöglichen, Aktivitäten zwischen diesen Pfaden zu korrelieren. Ein Endpunkt, der zwischen Netzwerken wechselt, möchte möglicherweise nicht, dass seine Aktivität von einer anderen Entität als seinem Peer korreliert wird. QUIC verschlüsselt jedoch nicht die Verbindungs-IDs im Header. SSU2 macht das, sodass das Datenschutzleck erfordern würde, dass der passive Beobachter auch Zugang zur network database hat, um den introduction key zu erhalten, der zum Entschlüsseln der Verbindungs-ID erforderlich ist. Selbst mit dem introduction key ist dies kein starker Angriff, und wir ändern Verbindungs-IDs nach Migration in SSU2 nicht, da dies eine erhebliche Komplikation wäre.

### Einleitung der Pfadvalidierung

Während der Datenphase müssen Peers die Quell-IP und den Port jedes empfangenen Datenpakets überprüfen. Wenn sich die IP oder der Port von zuvor empfangenen unterscheidet UND das Paket keine doppelte Paketnummer hat UND das Paket erfolgreich entschlüsselt wird, wechselt die Session in die Pfadvalidierungsphase.

Zusätzlich muss ein Peer verifizieren, dass die neue IP und der Port gemäß den lokalen Validierungsregeln gültig sind (nicht blockiert, keine illegalen Ports usw.). Peers sind NICHT verpflichtet, Migration zwischen IPv4 und IPv6 zu unterstützen, und können eine neue IP in der anderen Adressfamilie als ungültig betrachten, da dies kein erwartetes Verhalten ist und erhebliche Implementierungskomplexität hinzufügen kann. Beim Empfang eines Pakets von einer ungültigen IP/Port kann eine Implementierung es einfach verwerfen oder eine Pfadvalidierung mit der alten IP/Port initiieren.

Beim Eintritt in die Pfadvalidierungsphase führen Sie die folgenden Schritte aus:

- Starten Sie einen Pfadvalidierungs-Timeout-Timer von mehreren Sekunden oder mehrmals dem aktuellen RTO (TBD)
- Reduzieren Sie das Congestion Window auf das Minimum
- Reduzieren Sie die PMTU auf das Minimum (1280)
- Senden Sie ein Datenpaket mit einem Path Challenge Block, einem Address Block (mit der neuen IP/Port) und typischerweise einem ACK Block an die neue IP und den neuen Port. Dieses Paket verwendet dieselbe Verbindungs-ID und Verschlüsselungsschlüssel wie die aktuelle Session. Die Path Challenge Block-Daten müssen ausreichend Entropie enthalten (mindestens 8 Bytes), damit sie nicht gefälscht werden können.
- Optional können Sie auch einen Path Challenge an die alte IP/Port mit anderen Block-Daten senden. Siehe unten.
- Starten Sie einen Path Response-Timeout-Timer basierend auf dem aktuellen RTO (typischerweise RTT + ein Vielfaches von RTTdev)

Während der Pfadvalidierungsphase kann die Sitzung weiterhin eingehende Pakete verarbeiten. Sowohl von der alten als auch von der neuen IP/Port. Die Sitzung kann auch weiterhin Datenpakete senden und bestätigen. Allerdings müssen das Staufenster und die PMTU während der Pfadvalidierungsphase bei den Minimalwerten bleiben, um zu verhindern, dass sie für Denial-of-Service-Angriffe missbraucht werden, indem große Mengen an Datenverkehr an eine gefälschte Adresse gesendet werden.

Eine Implementierung kann, ist aber nicht verpflichtet, versuchen, mehrere Pfade gleichzeitig zu validieren. Dies ist wahrscheinlich die Komplexität nicht wert. Sie kann, ist aber nicht verpflichtet, sich an eine vorherige IP/Port-Adresse als bereits validiert zu erinnern und die Pfadvalidierung zu überspringen, wenn ein Peer zu seiner vorherigen IP/Port-Adresse zurückkehrt.

Wenn eine Path Response empfangen wird, die identische Daten enthält wie sie in der Path Challenge gesendet wurden, war die Path Validation erfolgreich. Die Quell-IP/Port der Path Response Nachricht muss nicht dieselbe sein, an die die Path Challenge gesendet wurde.

Wenn keine Path Response empfangen wird, bevor der Path Response Timer abläuft, sende eine weitere Path Challenge und verdopple den Path Response Timer.

Wenn keine Path Response empfangen wird, bevor der Path Validation Timer abläuft, ist die Path Validation fehlgeschlagen.

### Nachrichteninhalt

Die Data-Nachrichten sollten die folgenden Blöcke enthalten. Die Reihenfolge ist nicht spezifiziert, außer dass Padding als letztes stehen muss:

- Path Challenge oder Path Response Block. Path Challenge enthält opake Daten, empfohlen mindestens 8 Bytes. Path Response enthält die Daten aus dem Path Challenge.
- Address Block mit der scheinbaren IP des Empfängers
- DateTime Block
- ACK Block
- Padding Block

Es wird nicht empfohlen, andere Blöcke (zum Beispiel I2NP) in die Nachricht einzufügen.

Es ist erlaubt, einen Path Challenge Block in die Nachricht einzuschließen, die die Path Response enthält, um eine Validierung in die andere Richtung zu initiieren.

Path Challenge und Path Response Blöcke lösen ACKs aus. Der Path Challenge wird durch eine Data-Nachricht mit Path Response und ACK-Blöcken bestätigt. Der Path Response sollte durch eine Data-Nachricht mit einem ACK-Block bestätigt werden.

### Routing während der Pfadvalidierung

Die QUIC-Spezifikation ist nicht eindeutig darüber, wohin Datenpakete während der Pfadvalidierung gesendet werden sollen - an die alte oder neue IP/Port-Kombination? Es muss ein Gleichgewicht gefunden werden zwischen der schnellen Reaktion auf IP/Port-Änderungen und dem Vermeiden des Sendens von Datenverkehr an gefälschte Adressen. Außerdem dürfen gefälschte Pakete keine erheblichen Auswirkungen auf eine bestehende Sitzung haben. Reine Port-Änderungen werden wahrscheinlich durch NAT-Rebinding nach einer Leerlaufperiode verursacht; IP-Änderungen könnten während Phasen mit hohem Datenverkehr in eine oder beide Richtungen auftreten.

Strategien unterliegen der Forschung und Verfeinerung. Möglichkeiten umfassen:

- Keine Datenpakete an die neue IP/Port senden, bis diese validiert wurde
- Weiterhin Datenpakete an die alte IP/Port senden, bis die neue IP/Port validiert ist
- Gleichzeitige Revalidierung der alten IP/Port
- Keine Daten senden, bis entweder die alte oder neue IP/Port validiert ist
- Unterschiedliche Strategien für reine Port-Änderungen im Vergleich zu IP-Änderungen
- Unterschiedliche Strategien für eine IPv6-Änderung innerhalb desselben /32, wahrscheinlich verursacht durch temporäre Adressrotation

### Antworten auf Path Challenge

Beim Empfang einer Path Challenge muss der Peer mit einem Datenpaket antworten, das eine Path Response mit den Daten aus der Path Challenge enthält.

Die Path Response muss an die IP/den Port gesendet werden, von dem die Path Challenge empfangen wurde. Dies ist NICHT ZWANGSLÄUFIG die IP/der Port, die zuvor für den Peer etabliert wurde. Dies stellt sicher, dass die Pfadvalidierung durch einen Peer nur erfolgreich ist, wenn der Pfad in beide Richtungen funktionsfähig ist. Siehe den Abschnitt "Validierung nach lokaler Änderung" unten.

Sofern sich die IP/Port nicht von der zuvor bekannten IP/Port für den Peer unterscheidet, behandle eine Path Challenge als einfachen Ping und antworte bedingungslos mit einer Path Response. Der Empfänger behält oder ändert keinen Zustand basierend auf einer empfangenen Path Challenge. Falls sich die IP/Port unterscheidet, muss ein Peer verifizieren, dass die neue IP und der Port gemäß lokalen Validierungsregeln gültig sind (nicht blockiert, keine illegalen Ports, etc.). Peers sind NICHT verpflichtet, adressfamilien-übergreifende Antworten zwischen IPv4 und IPv6 zu unterstützen, und dürfen eine neue IP in der anderen Adressfamilie als ungültig behandeln, da dies kein erwartetes Verhalten ist.

Sofern nicht durch Congestion Control eingeschränkt, sollte die Path Response sofort gesendet werden. Implementierungen sollten Maßnahmen ergreifen, um Path Responses oder die verwendete Bandbreite bei Bedarf zu begrenzen.

Ein Path Challenge-Block wird in der Regel von einem Address-Block in derselben Nachricht begleitet. Wenn der Address-Block eine neue IP/Port enthält, kann ein Peer diese IP/Port validieren und Peer-Tests dieser neuen IP/Port initiieren, entweder mit dem Session-Peer oder einem anderen Peer. Wenn der Peer denkt, dass er hinter einer Firewall ist und sich nur der Port geändert hat, ist diese Änderung wahrscheinlich auf NAT-Rebinding zurückzuführen, und weitere Peer-Tests sind vermutlich nicht erforderlich.

### Erfolgreiche Pfadvalidierung

Bei erfolgreicher Pfadvalidierung wird die Verbindung vollständig zur neuen IP/Port migriert. Bei Erfolg:

- Die Pfadvalidierungsphase verlassen
- Alle Pakete werden an die neue IP und den neuen Port gesendet.
- Die Beschränkungen für das Überlastungsfenster und PMTU werden aufgehoben und dürfen wieder ansteigen. Stellen Sie sie nicht einfach auf die alten Werte zurück, da der neue Pfad andere Eigenschaften haben könnte.
- Wenn sich die IP geändert hat, setzen Sie die berechnete RTT und RTO auf Anfangswerte zurück. Da Änderungen nur am Port häufig das Ergebnis von NAT-Rebinding oder anderen Middlebox-Aktivitäten sind, kann der Peer stattdessen seinen Überlastungskontrollstatus und die Rundlaufzeitschätzung in diesen Fällen beibehalten, anstatt auf Anfangswerte zurückzukehren.
- Alle Token löschen (ungültig machen), die für die alte IP/Port gesendet oder empfangen wurden (optional)
- Einen neuen Token-Block für die neue IP/Port senden (optional)

### Pfadvalidierung abbrechen

Während der Pfadvalidierungsphase führen alle gültigen, nicht-doppelten Pakete, die von der alten IP/Port empfangen und erfolgreich entschlüsselt werden, zur Abbruch der Pfadvalidierung. Es ist wichtig, dass eine abgebrochene Pfadvalidierung, die durch ein gefälschtes Paket verursacht wurde, nicht dazu führt, dass eine gültige Sitzung beendet oder erheblich gestört wird.

Bei abgebrochener Pfadvalidierung:

- Die Pfadvalidierungsphase verlassen
- Alle Pakete werden an die alte IP und den alten Port gesendet.
- Die Beschränkungen für das Congestion Window und PMTU werden aufgehoben, und sie dürfen ansteigen oder optional die vorherigen Werte wiederherstellen
- Alle Datenpakete, die zuvor an die neue IP/den neuen Port gesendet wurden, werden an die alte IP/den alten Port neu übertragen.

### Fehlgeschlagene Pfadvalidierung

Es ist wichtig, dass eine fehlgeschlagene Pfadvalidierung, die durch ein gefälschtes Paket verursacht wurde, nicht dazu führt, dass eine gültige Sitzung beendet oder erheblich gestört wird.

Bei fehlgeschlagener Pfadvalidierung:

- Die Pfadvalidierungsphase verlassen
- Alle Pakete werden an die alte IP und den alten Port gesendet.
- Die Beschränkungen für das Congestion Window und PMTU werden aufgehoben und dürfen wieder steigen.
- Optional eine Pfadvalidierung für die alte IP und den alten Port starten. Falls diese fehlschlägt, die Sitzung beenden.
- Andernfalls den Standard-Regeln für Sitzungs-Timeout und -Beendigung folgen.
- Alle Datenpakete, die zuvor an die neue IP/den neuen Port gesendet wurden, an die alte IP/den alten Port erneut übertragen.

### Validierung nach lokaler Änderung

Der oben beschriebene Prozess ist für Peers definiert, die ein Paket von einer geänderten IP/Port erhalten. Er kann jedoch auch in die andere Richtung initiiert werden, von einem Peer, der erkennt, dass sich seine IP oder sein Port geändert hat. Ein Peer kann möglicherweise erkennen, dass sich seine lokale IP geändert hat; es ist jedoch viel unwahrscheinlicher, dass er erkennt, dass sich sein Port aufgrund einer NAT-Neubindung geändert hat. Daher ist dies optional.

Beim Empfang einer Path Challenge von einem Peer, dessen IP oder Port sich geändert hat, sollte der andere Peer eine Path Challenge in die andere Richtung initiieren.

### Als Ping/Pong verwenden

Path Challenge und Path Response Blöcke können jederzeit als Ping/Pong-Pakete verwendet werden. Der Empfang eines Path Challenge Blocks ändert keinen Zustand beim Empfänger, es sei denn, er wird von einer anderen IP/einem anderen Port empfangen.

## Mehrere Sitzungen

Peers sollten nicht mehrere Sitzungen mit demselben Peer aufbauen, weder SSU 1 oder 2, noch mit derselben oder verschiedenen IP-Adressen. Dies könnte jedoch passieren, entweder aufgrund von Fehlern, oder weil eine vorherige Sitzungsbeendigungsnachricht verloren ging, oder in einer Race-Condition, bei der die Beendigungsnachricht noch nicht angekommen ist.

Falls Bob eine bestehende Sitzung mit Alice hat, sollte Bob, wenn er die Session Confirmed von Alice erhält und dadurch den Handshake abschließt und eine neue Sitzung etabliert, folgendes tun:

- Migriere alle ungesendeten oder unbestätigten ausgehenden I2NP-Nachrichten von der alten Session zur neuen
- Sende eine Beendigung mit Reason-Code 22 auf der alten Session
- Entferne die alte Session und ersetze sie durch die neue

## Session-Beendigung

### Handshake-Phase

Sessions in der Handshake-Phase werden im Allgemeinen einfach durch Timeout beendet oder indem nicht weiter geantwortet wird. Optional können sie durch Einbeziehung eines Termination-Blocks in die Antwort beendet werden, aber auf die meisten Fehler kann aufgrund fehlender kryptographischer Schlüssel nicht geantwortet werden. Selbst wenn Schlüssel für eine Antwort mit einem Termination-Block verfügbar sind, ist es normalerweise die CPU-Zeit nicht wert, den DH für die Antwort durchzuführen. Eine Ausnahme KANN ein Termination-Block in einer Retry-Nachricht sein, der kostengünstig zu generieren ist.

### Datenphase

Sessions in der Datenphase werden beendet, indem eine Datennachricht gesendet wird, die einen Termination-Block enthält. Diese Nachricht sollte auch einen ACK-Block enthalten. Sie kann, falls die Session lange genug aktiv war, dass ein zuvor gesendeter Token abgelaufen ist oder kurz vor dem Ablauf steht, einen New Token-Block enthalten. Diese Nachricht löst keine Bestätigung aus. Beim Empfang eines Termination-Blocks mit einem anderen Grund als "Termination Received" antwortet der Peer mit einer Datennachricht, die einen Termination-Block mit dem Grund "Termination Received" enthält.

Nach dem Senden oder Empfangen eines Termination-Blocks sollte die Session für eine noch zu bestimmende maximale Zeitdauer in die Schließungsphase eintreten. Der Schließungszustand ist notwendig, um vor dem Verlust des Pakets mit dem Termination-Block und vor Paketen zu schützen, die in der anderen Richtung noch übertragen werden. Während der Schließungsphase besteht keine Anforderung, zusätzlich empfangene Pakete zu verarbeiten. Eine Session im Schließungszustand sendet als Antwort auf jedes eingehende Paket, das sie der Session zuordnet, ein Paket mit einem Termination-Block. Eine Session sollte die Rate begrenzen, mit der sie Pakete im Schließungszustand erzeugt. Beispielsweise könnte eine Session auf eine progressiv steigende Anzahl empfangener Pakete oder Zeitdauer warten, bevor sie auf empfangene Pakete antwortet.

Um den Zustand zu minimieren, den ein router für eine schließende Sitzung aufrechterhält, können Sitzungen als Antwort auf jedes empfangene Paket dasselbe Paket mit derselben Paketnummer unverändert senden, sind aber nicht dazu verpflichtet. Hinweis: Die Erlaubnis zur Neuübertragung eines Beendigungspakets ist eine Ausnahme von der Anforderung, dass für jedes Paket eine neue Paketnummer verwendet werden muss. Das Senden neuer Paketnummern ist hauptsächlich für die Verlustwiederherstellung und Staukontrolle von Vorteil, die bei einer geschlossenen Verbindung nicht relevant sein sollten. Die Neuübertragung des letzten Pakets erfordert weniger Zustand.

Nach Erhalt eines Termination-Blocks mit dem Grund "Termination Received" kann die Sitzung die Schließungsphase verlassen.

### Bereinigung

Bei jeder normalen oder abnormalen Beendigung sollten router alle flüchtigen Daten im Speicher löschen, einschließlich ephemerer Handshake-Schlüssel, symmetrischer Kryptoschlüssel und verwandter Informationen.

## MTU

Die Anforderungen variieren je nachdem, ob die veröffentlichte Adresse mit SSU 1 geteilt wird. Das aktuelle SSU 1 IPv4-Minimum beträgt 620, was definitiv zu klein ist.

Die minimale SSU2 MTU beträgt 1280 für sowohl IPv4 als auch IPv6, was der Spezifikation in [RFC-9000](https://tools.ietf.org/html/rfc9000) entspricht. Siehe unten. Durch die Erhöhung der minimalen MTU passen 1 KB tunnel-Nachrichten und kurze tunnel-Build-Nachrichten in ein Datagramm, was die typische Fragmentierung erheblich reduziert. Dies ermöglicht auch eine Erhöhung der maximalen I2NP-Nachrichtengröße. 1820-Byte-Streaming-Nachrichten sollten in zwei Datagramme passen.

Ein router darf SSU2 nicht aktivieren oder eine SSU2-Adresse veröffentlichen, es sei denn, die MTU für diese Adresse beträgt mindestens 1280.

Router müssen eine nicht standardmäßige MTU in jeder SSU- oder SSU2-router-Adresse veröffentlichen.

### SSU-Adresse

Geteilte Adresse mit SSU 1, muss SSU 1 Regeln befolgen. IPv4: Standard und Maximum ist 1484. Minimum ist 1292. (IPv4 MTU + 4) muss ein Vielfaches von 16 sein. IPv6: Muss veröffentlicht werden, Minimum ist 1280 und Maximum ist 1488. IPv6 MTU muss ein Vielfaches von 16 sein.

### SSU2-Adresse

IPv4: Standard und Maximum ist 1500. Minimum ist 1280. IPv6: Standard und Maximum ist 1500. Minimum ist 1280. Keine Vielfache-von-16-Regeln, sollte aber wahrscheinlich mindestens ein Vielfaches von 2 sein.

### PMTU-Erkennung

Für SSU 1 führt das aktuelle Java I2P eine PMTU-Erkennung durch, indem es mit kleinen Paketen beginnt und die Größe schrittweise erhöht oder basierend auf der empfangenen Paketgröße vergrößert. Dies ist primitiv und reduziert die Effizienz erheblich. Die Fortsetzung dieser Funktion in SSU 2 ist noch zu klären.

Neuere Studien zu [PMTU](https://en.wikipedia.org/wiki/Path_MTU_Discovery) legen nahe, dass ein Minimum für IPv4 von 1200 oder mehr für über 99% der Verbindungen funktionieren würde. QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) erfordert eine minimale IP-Paketgröße von 1280 Bytes.

Zitat [RFC-9000](https://tools.ietf.org/html/rfc9000):

Die maximale Datagramm-Größe ist definiert als die größte Größe einer UDP-Nutzlast, die über einen Netzwerkpfad mit einem einzigen UDP-Datagramm gesendet werden kann. QUIC DARF NICHT verwendet werden, wenn der Netzwerkpfad keine maximale Datagramm-Größe von mindestens 1200 Bytes unterstützen kann.

QUIC geht von einer minimalen IP-Paketgröße von mindestens 1280 Bytes aus. Dies ist die IPv6-Mindestgröße [IPv6] und wird auch von den meisten modernen IPv4-Netzwerken unterstützt. Unter der Annahme einer minimalen IP-Header-Größe von 40 Bytes für IPv6 und 20 Bytes für IPv4 sowie einer UDP-Header-Größe von 8 Bytes ergibt sich eine maximale Datagramm-Größe von 1232 Bytes für IPv6 und 1252 Bytes für IPv4. Daher wird erwartet, dass moderne IPv4- und alle IPv6-Netzwerkpfade QUIC unterstützen können.

Hinweis: Diese Anforderung zur Unterstützung einer UDP-Nutzlast von 1200 Bytes begrenzt den verfügbaren Platz für IPv6-Erweiterungsheader auf 32 Bytes oder IPv4-Optionen auf 52 Bytes, wenn der Pfad nur die IPv6-Mindest-MTU von 1280 Bytes unterstützt. Dies betrifft Initial-Pakete und Pfadvalidierung.

Ende des Zitats

### Handshake Mindestgröße

QUIC erfordert, dass Initial-Datagramme in beide Richtungen mindestens 1200 Bytes groß sind, um Verstärkungsangriffe zu verhindern und sicherzustellen, dass die PMTU dies in beide Richtungen unterstützt.

Wir könnten dies für Session Request und Session Created verlangen, was erhebliche Bandbreitenkosten verursachen würde. Vielleicht könnten wir dies nur tun, wenn wir kein Token haben oder nachdem eine Retry-Nachricht empfangen wurde. Noch zu entscheiden

QUIC erfordert, dass Bob nicht mehr als dreimal die Menge der empfangenen Daten sendet, bis die Client-Adresse validiert ist. SSU2 erfüllt diese Anforderung von Natur aus, da die Retry-Nachricht etwa die gleiche Größe wie die Token Request-Nachricht hat und kleiner als die Session Request-Nachricht ist. Außerdem wird die Retry-Nachricht nur einmal gesendet.

### Pfad-Nachricht Mindestgröße

QUIC erfordert, dass Nachrichten, die PATH_CHALLENGE- oder PATH_RESPONSE-Blöcke enthalten, mindestens 1200 Bytes groß sind, um Verstärkungsangriffe zu verhindern und sicherzustellen, dass die PMTU dies in beide Richtungen unterstützt.

Wir könnten dies ebenfalls verlangen, allerdings mit erheblichen Kosten bei der Bandbreite. Diese Fälle sollten jedoch selten auftreten. TBD

### Maximale I2NP-Nachrichtengröße

IPv4: Es wird keine IP-Fragmentierung angenommen. IP + Datagramm-Header sind 28 Bytes. Dies setzt voraus, dass keine IPv4-Optionen vorhanden sind. Die maximale Nachrichtengröße ist MTU - 28. Der Datenphase-Header ist 16 Bytes und MAC ist 16 Bytes, insgesamt 32 Bytes. Die Payload-Größe ist MTU - 60. Die maximale Datenphase-Payload ist 1440 für eine maximale MTU von 1500. Die maximale Datenphase-Payload ist 1220 für eine minimale MTU von 1280.

IPv6: Keine IP-Fragmentierung ist erlaubt. IP + Datagramm-Header sind 48 Bytes. Dies setzt voraus, dass keine IPv6-Erweiterungsheader vorhanden sind. Maximale Nachrichtengröße ist MTU - 48. Datenphasen-Header sind 16 Bytes und MAC sind 16 Bytes, insgesamt 32 Bytes. Payload-Größe ist MTU - 80. Maximale Datenphasen-Payload sind 1420 bei einer maximalen MTU von 1500. Maximale Datenphasen-Payload sind 1200 bei einer minimalen MTU von 1280.

In SSU 1 waren die Richtlinien ein striktes Maximum von etwa 32 KB für eine I2NP-Nachricht, basierend auf 64 maximalen Fragmenten und einer minimalen MTU von 620. Aufgrund des Overheads für gebündelte LeaseSets und Session-Schlüssel lag das praktische Limit auf Anwendungsebene etwa 6KB niedriger, also bei etwa 26KB. Das SSU 1-Protokoll erlaubt 128 Fragmente, aber aktuelle Implementierungen beschränken es auf 64 Fragmente.

Durch die Erhöhung der minimalen MTU auf 1280, mit einer Datenphase-Nutzlast von etwa 1200, ist eine SSU 2-Nachricht von etwa 76 KB in 64 Fragmenten und 152 KB in 128 Fragmenten möglich. Dies ermöglicht problemlos ein Maximum von 64 KB.

Aufgrund der Fragmentierung in Tunneln und der Fragmentierung in SSU 2 steigt die Wahrscheinlichkeit von Nachrichtenverlusten exponentiell mit der Nachrichtengröße. Wir empfehlen weiterhin eine praktische Grenze von etwa 10 KB auf der Anwendungsebene für I2NP-Datagramme.

## Peer-Test-Prozess

Siehe Peer Test-Sicherheit oben für eine Analyse des SSU1 Peer Tests und die Ziele für den SSU2 Peer Test.

```
Alice Bob Charlie

1.  

        PeerTest ------------------->

        :   Alice RI ------------------->

    2.  PeerTest ------------------->

    3\. <------------------ PeerTest

    :   <---------------- Charlie RI

    4.  <------------------ PeerTest
    5.  <----------------------------------------- PeerTest
    6.  PeerTest ----------------------------------------->
    7.  <----------------------------------------- PeerTest
```
Wenn von Bob abgelehnt:

```
Alice Bob Charlie

1.  PeerTest ------------------->
    2.  <------------------ PeerTest (reject)
```
Wenn von Charlie abgelehnt:

```
Alice Bob Charlie

1.  

        PeerTest ------------------->

        :   Alice RI ------------------->

    2.  PeerTest ------------------->

    3\. <------------------ PeerTest (reject)

    :   (optional: Bob could try another Charlie here)

    4.  <------------------ PeerTest (reject)
```
HINWEIS: RI können entweder als I2NP Database Store-Nachrichten in I2NP-Blöcken oder als RI-Blöcke (falls klein genug) gesendet werden. Diese können in denselben Paketen wie die Peer-Test-Blöcke enthalten sein, falls sie klein genug sind.

Nachrichten 1-4 sind in-session und verwenden Peer Test-Blöcke in einer Data-Nachricht. Nachrichten 5-7 sind out-of-session und verwenden Peer Test-Blöcke in einer Peer Test-Nachricht.

HINWEIS: Wie in SSU 1 können die Nachrichten 4 und 5 in beliebiger Reihenfolge ankommen. Nachricht 5 und/oder 7 werden möglicherweise überhaupt nicht empfangen, wenn Alice hinter einer Firewall ist. Wenn Nachricht 5 vor Nachricht 4 ankommt, kann Alice nicht sofort Nachricht 6 senden, da sie noch nicht Charlies Intro-Schlüssel hat, um den Header zu verschlüsseln. Wenn Nachricht 4 vor Nachricht 5 ankommt, sollte Alice nicht sofort Nachricht 6 senden, da sie abwarten sollte, ob Nachricht 5 ankommt, ohne die Firewall mit Nachricht 6 zu öffnen.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Path</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Intro Key</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->C session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->A session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->C</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
  </tbody>
</table>
### Versionen

Versionsübergreifende Peer-Tests werden nicht unterstützt. Die einzige zulässige Versionskombination ist, wenn alle Peers Version 2 verwenden.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### Wiederholungsübertragungen

Nachrichten 1-4 befinden sich in der Sitzung und werden von den ACK- und Retransmission-Prozessen der Datenphase abgedeckt. Peer Test-Blöcke erfordern eine Bestätigung.

Nachrichten 5-7 können unverändert erneut übertragen werden.

### IPv6-Hinweise

Wie in SSU 1 wird das Testen von IPv6-Adressen unterstützt, und die Kommunikation zwischen Alice-Bob und Alice-Charlie kann über IPv6 erfolgen, wenn Bob und Charlie ihre Unterstützung durch eine 'B'-Fähigkeit in ihrer veröffentlichten IPv6-Adresse anzeigen. Siehe Proposal 126 für Details.

Wie in SSU 1 vor Version 0.9.50 sendet Alice die Anfrage an Bob über eine bestehende Session über den Transport (IPv4 oder IPv6), den sie testen möchte. Wenn Bob eine Anfrage von Alice über IPv4 erhält, muss Bob einen Charlie auswählen, der eine IPv4-Adresse bewirbt. Wenn Bob eine Anfrage von Alice über IPv6 erhält, muss Bob einen Charlie auswählen, der eine IPv6-Adresse bewirbt. Die tatsächliche Bob-Charlie-Kommunikation kann über IPv4 oder IPv6 erfolgen (d.h. unabhängig von Alices Adresstyp). Dies ist NICHT das Verhalten von SSU 1 ab Version 0.9.50, wo gemischte IPv4/v6-Anfragen erlaubt sind.

### Verarbeitung durch Bob

Anders als in SSU 1 gibt Alice die angeforderte Test-IP und den Port in Nachricht 1 an. Bob sollte diese IP und den Port validieren und mit Code 5 ablehnen, wenn sie ungültig sind. Die empfohlene IP-Validierung ist, dass bei IPv4 die IP mit Alices IP übereinstimmt und bei IPv6 mindestens die ersten 8 Bytes der IP übereinstimmen. Die Port-Validierung sollte privilegierte Ports und Ports für bekannte Protokolle ablehnen.

### Ergebnisse-Zustandsmaschine

Hier dokumentieren wir, wie Alice die Ergebnisse eines Peer-Tests bestimmen kann, basierend darauf, welche Nachrichten empfangen werden. Die Verbesserungen von SSU2 bieten uns die Gelegenheit, die Zustandsmaschine für Peer-Test-Ergebnisse im Vergleich zu der in [SSU](/docs/transport/ssu) zu reparieren, zu verbessern und besser zu dokumentieren.

Für jeden getesteten Adresstyp (IPv4 oder IPv6) kann das Ergebnis UNKNOWN, OK, FIREWALLED oder SYMNAT sein. Zusätzlich können andere Verarbeitungsschritte durchgeführt werden, um IP- oder Port-Änderungen oder einen externen Port zu erkennen, der sich vom internen Port unterscheidet.

Probleme mit der dokumentierten SSU-Zustandsmaschine:

- Wir senden niemals Nachricht 6, es sei denn, wir haben Nachricht 5 erhalten, daher wissen wir nie, ob wir SYMNAT sind
- Wenn wir die Nachrichten 4 und 7 erhalten HABEN, wie könnten wir möglicherweise SYMNAT sein
- Wenn die IP nicht übereinstimmte, aber der Port schon, sind wir nicht SYMNAT, wir haben nur unsere IP geändert

Im Gegensatz zu SSU empfehlen wir daher, mehrere Sekunden nach Erhalt von Nachricht 4 zu warten und dann Nachricht 6 zu senden, auch wenn Nachricht 5 nicht empfangen wurde.

Eine Zusammenfassung der Zustandsmaschine, basierend darauf, ob die Nachrichten 4, 5 und 7 empfangen werden (ja oder nein), ist wie folgt:

```
4 5 7 Result Notes

----- ------ -----n n n UNKNOWN y n n FIREWALLED (unless currently SYMNAT) n y n OK (unless currently SYMNAT, which is unlikely) y y n OK (unless currently SYMNAT, which is unlikely) n n y n/a (can't send msg 6) y n y FIREWALLED or SYMNAT (requires sending msg 6 w/o rcv msg 5) n y y n/a (can't send msg 6) y y y OK
```
Eine detailliertere Zustandsmaschine mit Überprüfungen der IP/Port, die im Adressblock von Nachricht 7 empfangen wurden, ist unten dargestellt. Eine Herausforderung besteht darin zu bestimmen, ob Sie (Alice) derjenige mit symmetrischem NAT sind oder Charlie.

Eine Nachbearbeitung oder zusätzliche Logik zur Bestätigung von Zustandsübergängen durch das Erfordernis derselben Ergebnisse bei zwei oder mehr Peer-Tests wird empfohlen.

Die Validierung und Bestätigung der empfangenen IP/Port durch zwei oder mehr Tests oder mit dem Adressblock in Session Created-Nachrichten wird ebenfalls empfohlen, liegt jedoch außerhalb des Umfangs dieser Spezifikation.

```
If Alice does not get msg 5:

If Alice does not get msg 4: -> UNKNOWN If Alice does not get msg 7: -> UNKNOWN If Alice gets msgs 4/7 and IP/port match: -> FIREWALLED If Alice gets msgs 4/7 and IP matches, port does not match: -> SYMNAT, but needs confirmation with 2nd test If Alice gets msgs 4/7 and IP does not match, port matches: -> FIREWALLED, address change? If Alice gets msgs 4/7 and both IP and port do not match: -> SYMNAT, address change?

    If Alice gets msg 5: If Alice does not get msg 4: -> OK unless currently SYMNAT, else UNKNOWN (in SSU2 have to stop here) If Alice does not get msg 7: -> OK unless currently SYMNAT, else UNKNOWN If Alice gets msgs 4/5/7 and IP/port match: -> OK If Alice gets msgs 4/5/7 and IP matches, port does not match: -> OK, charlie is probably sym. natted If Alice gets msgs 4/5/7 and IP does not match, port matches: -> OK, address change? If Alice gets msgs 4/5/7 and both IP and port do not match: -> OK, address change?
```
## Relay-Prozess

Siehe Relay-Sicherheit oben für eine Analyse des SSU1 Relay und die Ziele für SSU2 Relay.

```
Alice Bob Charlie

lookup Bob RI

    SessionRequest -------------------->

    :   <------------ SessionCreated

    SessionConfirmed ----------------->

    1.  

        RelayRequest ---------------------->

        :   Alice RI ------------>

    2.  RelayIntro ----------->

    3.  <-------------- RelayResponse

    4.  <-------------- RelayResponse

    5.  <-------------------------------------------- HolePunch

    6.  SessionRequest -------------------------------------------->

    7.  <-------------------------------------------- SessionCreated

    8.  SessionConfirmed ------------------------------------------>
```
Wenn von Bob abgelehnt:

```
Alice Bob Charlie

lookup Bob RI

    SessionRequest -------------------->

    :   <------------ SessionCreated

    SessionConfirmed ----------------->

    1.  RelayRequest ---------------------->
    2.  <-------------- RelayResponse
```
Wenn von Charlie abgelehnt:

```
Alice Bob Charlie

lookup Bob RI

    SessionRequest -------------------->

    :   <------------ SessionCreated

    SessionConfirmed ----------------->

    1.  

        RelayRequest ---------------------->

        :   Alice RI ------------>

    2.  RelayIntro ----------->

    3.  <-------------- RelayResponse

    4.  <-------------- RelayResponse
```
HINWEIS: RI können entweder als I2NP Database Store Nachrichten in I2NP-Blöcken oder als RI-Blöcke gesendet werden (falls klein genug). Diese können in denselben Paketen wie die Relay-Blöcke enthalten sein, falls sie klein genug sind.

In SSU 1 enthält Charlies router info die IP, den Port, den intro key, das relay tag und die Ablaufzeit jedes introducers.

In SSU 2 enthält Charlies router info den router hash, relay tag und Ablaufzeit jedes introducers.

Alice sollte die Anzahl der erforderlichen Round Trips reduzieren, indem sie zuerst einen Introducer (Bob) auswählt, zu dem sie bereits eine Verbindung hat. Zweitens, falls keiner vorhanden ist, sollte sie einen Introducer auswählen, für den sie bereits die Router-Informationen hat.

Cross-Version-Relaying sollte ebenfalls unterstützt werden, wenn möglich. Dies wird einen schrittweisen Übergang von SSU 1 zu SSU 2 erleichtern. Die erlaubten Versionskombinationen sind (TODO):

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/2/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### Neuübertragungen

Relay Request, Relay Intro und Relay Response sind alle in-session und werden von den ACK- und Neuübertragungsprozessen der Datenphase abgedeckt. Relay Request, Relay Intro und Relay Response Blöcke lösen ACKs aus.

Beachten Sie, dass Charlie normalerweise sofort auf eine Relay Intro mit einer Relay Response antwortet, die einen ACK-Block enthalten sollte. In diesem Fall ist keine separate Nachricht mit einem ACK-Block erforderlich.

Hole Punch kann erneut übertragen werden, wie in SSU 1.

Im Gegensatz zu I2NP-Nachrichten haben Relay-Nachrichten keine eindeutigen Identifikatoren, daher müssen Duplikate von der Relay-Zustandsmaschine unter Verwendung der Nonce erkannt werden. Implementierungen müssen möglicherweise auch einen Cache der kürzlich verwendeten Nonces verwalten, damit empfangene Duplikate auch dann erkannt werden können, nachdem die Zustandsmaschine für diese Nonce abgeschlossen wurde.

### IPv4/v6

Alle Funktionen des SSU 1 Relay werden unterstützt, einschließlich derjenigen, die in [Prop158](/proposals/158-ipv6-transport-enhancements) dokumentiert und ab Version 0.9.50 unterstützt werden. IPv4- und IPv6-Einführungen werden unterstützt. Eine Relay-Anfrage kann über eine IPv4-Sitzung für eine IPv6-Einführung gesendet werden, und eine Relay-Anfrage kann über eine IPv6-Sitzung für eine IPv4-Einführung gesendet werden.

### Verarbeitung durch Alice

Im Folgenden sind die Unterschiede zu SSU 1 und Empfehlungen für die SSU 2 Implementierung aufgeführt.

#### Introducer-Auswahl

In SSU 1 ist die Einführung relativ kostengünstig, und Alice sendet im Allgemeinen Relay Requests an alle Introducer. In SSU 2 ist die Einführung kostspieliger, da zuerst eine Verbindung mit einem Introducer aufgebaut werden muss. Um die Einführungslatenz und den Overhead zu minimieren, sind die empfohlenen Verarbeitungsschritte wie folgt:

- Ignoriere alle introducer, die basierend auf dem iexp-Wert in der Adresse abgelaufen sind
- Falls bereits eine SSU2-Verbindung zu einem oder mehreren introducern besteht, wähle einen aus und sende die Relay Request nur an diesen introducer.
- Andernfalls, falls eine Router Info für einen oder mehrere introducer lokal bekannt ist, wähle einen aus und verbinde dich nur mit diesem introducer.
- Andernfalls suche die Router Infos für alle introducer, verbinde dich mit dem introducer, dessen Router Info zuerst empfangen wird.

#### Antwortverarbeitung

In sowohl SSU 1 als auch SSU 2 können die Relay Response und Hole Punch in beliebiger Reihenfolge empfangen werden oder möglicherweise gar nicht empfangen werden.

In SSU 1 erhält Alice normalerweise die Relay Response (1 RTT) vor dem Hole Punch (1 1/2 RTT). Es mag in diesen Spezifikationen nicht gut dokumentiert sein, aber Alice muss die Relay Response von Bob erhalten, bevor sie fortfährt, um Charlies IP zu erhalten. Wenn der Hole Punch zuerst empfangen wird, wird Alice ihn nicht erkennen, da er keine Daten enthält und die Quell-IP nicht erkannt wird. Nach Erhalt der Relay Response sollte Alice ENTWEDER auf den Empfang des Hole Punch von Charlie warten ODER eine kurze Verzögerung (empfohlene 500 ms) abwarten, bevor sie den Handshake mit Charlie initiiert.

In SSU 2 wird Alice normalerweise den Hole Punch (1 1/2 RTT) vor der Relay Response (2 RTT) erhalten. Der SSU 2 Hole Punch ist einfacher zu verarbeiten als in SSU 1, da es sich um eine vollständige Nachricht mit definierten Verbindungs-IDs (abgeleitet von der Relay-Nonce) und Inhalten einschließlich Charlies IP handelt. Die Relay Response (Data-Nachricht) und die Hole Punch-Nachricht enthalten den identischen signierten Relay Response-Block. Daher kann Alice den Handshake mit Charlie initiieren, nachdem sie ENTWEDER den Hole Punch von Charlie ODER die Relay Response von Bob erhalten hat.

Die Signaturverifikation des Hole Punch enthält den router hash des Vermittlers (Bob). Wenn Relay Requests an mehr als einen Vermittler gesendet wurden, gibt es mehrere Optionen zur Validierung der Signatur:

- Versuche jeden Hash, an den eine Anfrage gesendet wurde
- Verwende verschiedene Nonces für jeden introducer und nutze das, um zu bestimmen, von welchem introducer dieser Hole Punch als Antwort kam
- Validiere die Signatur nicht erneut, wenn der Inhalt identisch mit dem in der Relay Response ist, falls bereits empfangen
- Validiere die Signatur überhaupt nicht

Wenn Charlie sich hinter einem symmetrischen NAT befindet, ist sein gemeldeter Port in der Relay Response und dem Hole Punch möglicherweise nicht korrekt. Daher sollte Alice den UDP-Quellport der Hole Punch-Nachricht überprüfen und diesen verwenden, falls er sich vom gemeldeten Port unterscheidet.

### Tag-Anfragen von Bob

In SSU 1 konnte nur Alice ein Tag anfordern, und zwar im Session Request. Bob konnte niemals ein Tag anfordern, und Alice konnte nicht für Bob weiterleiten.

In SSU2 fordert Alice normalerweise einen Tag in der Session Request an, aber sowohl Alice als auch Bob können einen Tag in der Datenphase anfordern. Bob ist normalerweise nicht durch eine Firewall geschützt, nachdem er eine eingehende Anfrage erhalten hat, aber es könnte nach einem Relay der Fall sein, oder Bobs Zustand könnte sich ändern, oder er könnte einen Introducer für den anderen Adresstyp (IPv4/v6) anfordern. Daher ist es in SSU2 möglich, dass sowohl Alice als auch Bob gleichzeitig als Relays für die andere Partei fungieren.

## Veröffentlichte Router Info

### Adresseigenschaften

Die folgenden Adresseigenschaften können veröffentlicht werden, unverändert von SSU 1, einschließlich Änderungen in [Prop158](/proposals/158-ipv6-transport-enhancements), die ab API 0.9.50 unterstützt werden:

- caps: [B,C,4,6] Fähigkeiten
- host: IP (IPv4 oder IPv6). Gekürzte IPv6-Adresse (mit "::") ist erlaubt. Kann vorhanden sein oder nicht, wenn firewalled. Hostnamen sind nicht erlaubt.
- iexp[0-2]: Ablauf dieses introducers. ASCII-Ziffern, in Sekunden seit der Epoche. Nur vorhanden wenn firewalled und introducer erforderlich sind. Optional (auch wenn andere Eigenschaften für diesen introducer vorhanden sind).
- ihost[0-2]: IP des Introducers (IPv4 oder IPv6). Gekürzte IPv6-Adresse (mit "::") ist erlaubt. Nur vorhanden wenn firewalled und introducer erforderlich sind. Hostnamen sind nicht erlaubt. Nur SSU-Adresse.
- ikey[0-2]: Base 64 introduction key des Introducers. Nur vorhanden wenn firewalled und introducer erforderlich sind. Nur SSU-Adresse.
- iport[0-2]: Port des Introducers 1024 - 65535. Nur vorhanden wenn firewalled und introducer erforderlich sind. Nur SSU-Adresse.
- itag[0-2]: Tag des Introducers 1 - (2**32 - 1) ASCII-Ziffern. Nur vorhanden wenn firewalled und introducer erforderlich sind.
- key: Base 64 introduction key.
- mtu: Optional. Siehe MTU-Abschnitt oben.
- port: 1024 - 65535 Kann vorhanden sein oder nicht, wenn firewalled.

### Veröffentlichte Adressen

Die veröffentlichte RouterAddress (Teil der RouterInfo) wird eine Protokoll-Kennung von entweder "SSU" oder "SSU2" haben.

Die RouterAddress muss drei Optionen enthalten, um SSU2-Unterstützung anzuzeigen:

- s=(Base64 Schlüssel) Der aktuelle Noise static public key (s) für diese RouterAddress. Base 64 kodiert mit dem Standard I2P Base 64 Alphabet. 32 Bytes binär, 44 Bytes als Base 64 kodiert, little-endian X25519 public key.
- i=(Base64 Schlüssel) Der aktuelle introduction key zum Verschlüsseln der Header für diese RouterAddress. Base 64 kodiert mit dem Standard I2P Base 64 Alphabet. 32 Bytes binär, 44 Bytes als Base 64 kodiert, big-endian ChaCha20 Schlüssel.
- v=2 Die aktuelle Version (2). Wenn als "SSU" veröffentlicht, ist zusätzliche Unterstützung für Version 1 impliziert. Unterstützung für zukünftige Versionen erfolgt mit kommagetrennten Werten, z.B. v=2,3 Die Implementierung sollte die Kompatibilität überprüfen, einschließlich mehrerer Versionen falls ein Komma vorhanden ist. Kommagetrennte Versionen müssen in numerischer Reihenfolge stehen.

Alice muss überprüfen, dass alle drei Optionen vorhanden und gültig sind, bevor sie sich über das SSU2-Protokoll verbindet.

Wenn als "SSU" mit den Optionen "s", "i" und "v" und mit den Optionen "host" und "port" veröffentlicht, muss der router eingehende Verbindungen auf diesem Host und Port sowohl für SSU- als auch SSU2-Protokolle akzeptieren und die Protokollversion automatisch erkennen.

Wenn als "SSU2" mit den Optionen "s", "i" und "v" und mit den Optionen "host" und "port" veröffentlicht, akzeptiert der router eingehende Verbindungen auf diesem Host und Port nur für das SSU2-Protokoll.

Wenn ein router sowohl SSU1- als auch SSU2-Verbindungen unterstützt, aber keine automatische Versionserkennung für eingehende Verbindungen implementiert, muss er sowohl "SSU"- als auch "SSU2"-Adressen bekanntgeben und die SSU2-Optionen nur in der "SSU2"-Adresse einschließen. Der router sollte einen niedrigeren Kostenwert (höhere Priorität) in der "SSU2"-Adresse als in der "SSU"-Adresse setzen, damit SSU2 bevorzugt wird.

Wenn mehrere SSU2 RouterAddresses (entweder als "SSU" oder "SSU2") in derselben RouterInfo veröffentlicht werden (für zusätzliche IP-Adressen oder Ports), müssen alle Adressen, die denselben Port angeben, identische SSU2-Optionen und -Werte enthalten. Insbesondere müssen alle denselben statischen Schlüssel "s" und Einführungsschlüssel "i" enthalten.

#### Einführer

Wenn als SSU oder SSU2 mit Introducern veröffentlicht, sind die folgenden Optionen vorhanden:

- ih[0-2]=(Base64 hash) Ein router Hash für einen Introducer. Base 64 kodiert mit dem Standard I2P Base 64 Alphabet. 32 Bytes binär, 44 Bytes als Base 64 kodiert
- iexp[0-2]: Ablaufzeit dieses Introducers. Unverändert von SSU 1.
- itag[0-2]: Tag des Introducers 1 - (2**32 - 1) Unverändert von SSU 1.

Die folgenden Optionen gelten nur für SSU und werden nicht für SSU2 verwendet. In SSU2 erhält Alice diese Informationen stattdessen aus Charlies RI.

- ihost[0-2]
- ikey[0-2]
- itag[0-2]

Ein router darf keine Host- oder Port-Angaben in der Adresse veröffentlichen, wenn er introducers veröffentlicht. Ein router muss 4 und/oder 6 caps in der Adresse veröffentlichen, wenn er introducers veröffentlicht, um die Unterstützung für IPv4 und/oder IPv6 anzuzeigen. Dies entspricht der aktuellen Praxis für aktuelle SSU 1-Adressen.

Hinweis: Wenn als SSU veröffentlicht und es eine Mischung aus SSU 1 und SSU2 introducers gibt, sollten die SSU 1 introducers bei den niedrigeren Indizes und die SSU2 introducers bei den höheren Indizes stehen, um die Kompatibilität mit älteren routern zu gewährleisten.

### Unveröffentlichte SSU2-Adresse

Wenn Alice ihre SSU2-Adresse (als "SSU" oder "SSU2") für eingehende Verbindungen nicht veröffentlicht, muss sie eine "SSU2" router-Adresse veröffentlichen, die nur ihren statischen Schlüssel und die SSU2-Version enthält, damit Bob den Schlüssel validieren kann, nachdem er Alices RouterInfo in Session Confirmed Teil 2 erhalten hat.

- s=(Base64 key) Wie oben für veröffentlichte Adressen definiert.
- i=(Base64 key) Wie oben für veröffentlichte Adressen definiert.
- v=2 Wie oben für veröffentlichte Adressen definiert.

Diese Router-Adresse wird keine "host"- oder "port"-Optionen enthalten, da diese für ausgehende SSU2-Verbindungen nicht erforderlich sind. Die veröffentlichten Kosten für diese Adresse sind nicht strikt relevant, da sie nur eingehend ist; jedoch kann es für andere Router hilfreich sein, wenn die Kosten höher (niedrigere Priorität) als bei anderen Adressen gesetzt werden. Der empfohlene Wert ist 14.

Alice kann auch einfach die Optionen "i", "s" und "v" zu einer bestehenden veröffentlichten "SSU"-Adresse hinzufügen.

### Rotation von öffentlichen Schlüsseln und IV

Die Verwendung derselben statischen Schlüssel für NTCP2 und SSU2 ist erlaubt, aber nicht empfohlen.

Aufgrund der Zwischenspeicherung von RouterInfos dürfen router den statischen öffentlichen Schlüssel oder IV nicht rotieren, während der router läuft, unabhängig davon, ob sie in einer veröffentlichten Adresse stehen oder nicht. Router müssen diesen Schlüssel und IV dauerhaft speichern, um sie nach einem sofortigen Neustart wiederzuverwenden, damit eingehende Verbindungen weiterhin funktionieren und Neustartzeiten nicht preisgegeben werden. Router müssen die Zeit des letzten Herunterfahrens dauerhaft speichern oder anderweitig bestimmen, damit die vorherige Ausfallzeit beim Start berechnet werden kann.

Unter Berücksichtigung von Bedenken bezüglich der Preisgabe von Neustartzeiten können router diesen Schlüssel oder IV beim Start rotieren, wenn der router zuvor für längere Zeit (mindestens mehrere Tage) offline war.

Wenn der Router veröffentlichte SSU2 RouterAddresses (als SSU oder SSU2) hat, sollte die minimale Ausfallzeit vor der Rotation viel länger sein, zum Beispiel einen Monat, es sei denn, die lokale IP-Adresse hat sich geändert oder der Router führt ein "rekeys" durch.

Wenn der router veröffentlichte SSU RouterAddresses hat, aber nicht SSU2 (als SSU oder SSU2), sollte die minimale Ausfallzeit vor der Rotation länger sein, zum Beispiel ein Tag, es sei denn, die lokale IP-Adresse hat sich geändert oder der router führt ein "rekeys" durch. Dies gilt auch wenn die veröffentlichte SSU-Adresse introducers hat.

Wenn der router keine veröffentlichten RouterAddresses (SSU, SSU2 oder NTCP2) hat, kann die minimale Ausfallzeit vor der Rotation nur zwei Stunden betragen, selbst wenn sich die IP-Adresse ändert, es sei denn, der router führt ein "rekeys" durch.

Wenn der router sich zu einem anderen Router Hash "umschlüsselt", sollte er auch einen neuen Noise-Schlüssel und Intro-Schlüssel generieren.

Implementierungen müssen sich bewusst sein, dass eine Änderung des statischen öffentlichen Schlüssels oder IV eingehende SSU2-Verbindungen von Routern verhindert, die eine ältere RouterInfo zwischengespeichert haben. RouterInfo-Veröffentlichung, Tunnel-Peer-Auswahl (einschließlich sowohl OBGW als auch IB nächster Hop), Zero-Hop-Tunnel-Auswahl, Transport-Auswahl und andere Implementierungsstrategien müssen dies berücksichtigen.

Die Intro-Schlüsselrotation unterliegt denselben Regeln wie die Schlüsselrotation.

Hinweis: Die minimale Ausfallzeit vor dem Rekeying kann angepasst werden, um die Netzwerkgesundheit zu gewährleisten und ein Reseeding durch einen router zu verhindern, der für eine moderate Zeit ausgefallen war.

#### Identität verbergen

Abstreitbarkeit ist kein Ziel. Siehe Übersicht oben.

Jedem Muster werden Eigenschaften zugewiesen, die die Vertraulichkeit beschreiben, die für den statischen öffentlichen Schlüssel des Initiators und für den statischen öffentlichen Schlüssel des Responders bereitgestellt wird. Die zugrundeliegenden Annahmen sind, dass ephemere private Schlüssel sicher sind und dass die Parteien den Handshake abbrechen, wenn sie einen statischen öffentlichen Schlüssel von der anderen Partei erhalten, dem sie nicht vertrauen.

Dieser Abschnitt betrachtet nur die Preisgabe von Identitäten durch statische öffentliche Schlüsselfelder in Handshakes. Natürlich könnten die Identitäten von Noise-Teilnehmern auch durch andere Mittel preisgegeben werden, einschließlich Payload-Feldern, Verkehrsanalyse oder Metadaten wie IP-Adressen.

Alice: (8) Verschlüsselt mit Forward Secrecy zu einer authentifizierten Partei.

Bob: (3) Nicht übertragen, aber ein passiver Angreifer kann Kandidaten für den privaten Schlüssel des Responders überprüfen und bestimmen, ob der Kandidat korrekt ist.

Bob veröffentlicht seinen statischen öffentlichen Schlüssel in der netDb. Alice muss dies möglicherweise nicht tun, aber muss ihn in die an Bob gesendete RI einschließen.

## Paket-Richtlinien

### Erstellung ausgehender Pakete

Handshake-Nachrichten (Session Request/Created/Confirmed, Retry) grundlegende Schritte, in der Reihenfolge:

- 16 oder 32 Byte Header erstellen
- Payload erstellen
- mixHash() des Headers (außer bei Retry)
- Payload mit Noise verschlüsseln (außer bei Retry, verwende ChaChaPoly mit dem Header als AD)
- Header verschlüsseln, und bei Session Request/Created den ephemeral key

Grundlegende Schritte der Datenphasen-Nachrichten, in der Reihenfolge:

- 16-Byte-Header erstellen
- Payload erstellen
- Payload mit ChaChaPoly verschlüsseln, wobei der Header als AD verwendet wird
- Header verschlüsseln

### Verarbeitung eingehender Pakete

#### Zusammenfassung

Erste Verarbeitung aller eingehenden Nachrichten:

- Entschlüssele die ersten 8 Bytes des Headers (die Destination Connection ID) mit dem intro key
- Suche die Verbindung anhand der Destination Connection ID
- Wenn die Verbindung gefunden wird und sich in der Datenphase befindet, gehe zum Datenphase-Abschnitt
- Wenn die Verbindung nicht gefunden wird, gehe zum Handshake-Abschnitt
- Hinweis: Peer Test und Hole Punch Nachrichten können ebenfalls über die Destination Connection ID gesucht werden, die aus der test oder relay nonce erstellt wurde.

Verarbeitung von Handshake-Nachrichten (Session Request/Created/Confirmed, Retry, Token Request) und anderen sitzungsunabhängigen Nachrichten (Peer Test, Hole Punch):

- Entschlüssele Bytes 8-15 des Headers (der Pakettyp, Version und Netz-ID) mit dem intro key. Wenn es eine gültige Session Request, Token Request, Peer Test oder Hole Punch ist, fortfahren
- Wenn keine gültige Nachricht, suche eine ausstehende ausgehende Verbindung anhand der Paket-Quell-IP/Port, behandle das Paket als Session Created oder Retry. Entschlüssele erneut die ersten 8 Bytes des Headers mit dem korrekten Schlüssel und die Bytes 8-15 des Headers (der Pakettyp, Version und Netz-ID). Wenn es eine gültige Session Created oder Retry ist, fortfahren
- Wenn keine gültige Nachricht, fehlschlagen oder als mögliches Datenphase-Paket außer der Reihenfolge einreihen
- Für Session Request/Created, Retry, Token Request, Peer Test und Hole Punch, entschlüssele Bytes 16-31 des Headers
- Für Session Request/Created, entschlüssele den ephemeral key
- Validiere alle Header-Felder, stoppen wenn nicht gültig
- mixHash() den Header
- Für Session Request/Created/Confirmed, entschlüssele die Payload mit Noise
- Für Retry und Datenphase, entschlüssele die Payload mit ChaChaPoly
- Verarbeite den Header und die Payload

Verarbeitung von Datenphasennachrichten:

- Entschlüssele Bytes 8-15 des Headers (Pakettyp, Version und Netz-ID) mit dem korrekten Schlüssel
- Entschlüssele die Nutzdaten mit ChaChaPoly unter Verwendung des Headers als AD
- Verarbeite den Header und die Nutzdaten

#### Details

In SSU 1 ist die eingehende Paketklassifizierung schwierig, da es keinen Header gibt, der die Sitzungsnummer angibt. Router müssen zunächst die Quell-IP und den Port mit einem bestehenden Peer-Status abgleichen, und wenn nichts gefunden wird, mehrere Entschlüsselungen mit verschiedenen Schlüsseln versuchen, um den entsprechenden Peer-Status zu finden oder einen neuen zu starten. Falls sich die Quell-IP oder der Port für eine bestehende Sitzung ändert, möglicherweise aufgrund von NAT-Verhalten, kann der Router teure Heuristiken verwenden, um zu versuchen, das Paket einer bestehenden Sitzung zuzuordnen und den Inhalt wiederherzustellen.

SSU 2 ist darauf ausgelegt, den Aufwand für die eingehende Paketklassifizierung zu minimieren, während gleichzeitig DPI-Resistenz und andere Bedrohungen auf dem Übertragungsweg aufrechterhalten werden. Die Connection ID-Nummer ist im Header für alle Nachrichtentypen enthalten und mit ChaCha20 unter Verwendung eines bekannten Schlüssels und einer bekannten Nonce verschlüsselt (verschleiert). Zusätzlich ist auch der Nachrichtentyp im Header enthalten (verschlüsselt mit Header-Schutz zu einem bekannten Schlüssel und dann mit ChaCha20 verschleiert) und kann für zusätzliche Klassifizierung verwendet werden. In keinem Fall ist eine Probe-DH oder eine andere asymmetrische Krypto-Operation zur Klassifizierung eines Pakets erforderlich.

Für fast alle Nachrichten von allen Peers ist der ChaCha20-Schlüssel für die Connection ID-Verschlüsselung der Introduction Key des Ziel-Routers, wie er in der netDb veröffentlicht wurde.

Die einzigen Ausnahmen sind die ersten Nachrichten, die von Bob an Alice gesendet werden (Session Created oder Retry), bei denen Alices introduction key Bob noch nicht bekannt ist. In diesen Fällen wird Bobs introduction key als Schlüssel verwendet.

Das Protokoll ist darauf ausgelegt, die Paketklassifizierungsverarbeitung zu minimieren, die möglicherweise zusätzliche Kryptographie-Operationen in mehreren Fallback-Schritten oder komplexe Heuristiken erfordern könnte. Darüber hinaus wird die große Mehrheit der empfangenen Pakete keine (möglicherweise teure) Fallback-Suche nach Quell-IP/Port und eine zweite Header-Entschlüsselung erfordern. Nur Session Created und Retry (und möglicherweise andere noch festzulegende) werden die Fallback-Verarbeitung benötigen. Wenn ein Endpunkt nach der Session-Erstellung die IP oder den Port ändert, wird die Verbindungs-ID weiterhin für die Session-Suche verwendet. Es ist niemals notwendig, Heuristiken zu verwenden, um die Session zu finden, beispielsweise durch die Suche nach einer anderen Session mit derselben IP aber einem anderen Port.

Daher sind die empfohlenen Verarbeitungsschritte in der Empfänger-Loop-Logik:

1) Entschlüsseln Sie die ersten 8 Bytes mit ChaCha20 unter Verwendung des lokalen Einführungsschlüssels, um die Ziel-Verbindungs-ID wiederherzustellen. Wenn die Verbindungs-ID mit einer aktuellen oder ausstehenden eingehenden Sitzung übereinstimmt:

    a)  Using the appropriate key, decrypt the header bytes 8-15 to recover the version, net ID, and message type.
    b)  If the message type is Session Confirmed, it is a long header. Verify the net ID and protocol version are valid. Decrypt the bytes 15-31 of the header with ChaCha20 using the local intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise.
    c)  If the message type is valid but not Session Confirmed, it is a short header. Verify the net ID and protocol version are valid. decrypt the rest of the message with ChaCha20/Poly1305 using the session key, using the decrypted 16-byte header as the AD.
    d)  (optional) If connection ID is a pending inbound session awaiting a Session Confirmed message, but the net ID, protocol, or message type is not valid, it could be a Data message received out-of-order before the Session Confirmed, so the data phase header protection keys are not yet known, and the header bytes 8-15 were incorrectly decrypted. Queue the message, and attempt to decrypt it once the Session Confirmed message is received.
    e)  If b) or c) fails, drop the message.

2)  Wenn die Verbindungs-ID mit keiner aktuellen Sitzung übereinstimmt: Prüfen Sie, ob der Klartext-Header bei Bytes 8-15 gültig ist (ohne eine Header-Schutz-Operation durchzuführen). Verifizieren Sie, dass die Netzwerk-ID und Protokollversion gültig sind und der Nachrichtentyp Session Request oder ein anderer außerhalb der Sitzung erlaubter Nachrichtentyp ist (TBD).

    a)  If all is valid and the message type is Session Request, decrypt bytes 16-31 of the header and the 32-byte X value with ChaCha20 using the local intro key.

    - If the token at header bytes 24-31 is accepted, then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Created in response.
    - If the token is not accepted, send a Retry message to the source IP/port with a token. Do not attempt to decrypt the message with Noise to avoid DDoS attacks.

    b)  If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.
    c)  If a) or b) fails, go to step 3)

3)  Suche eine ausstehende ausgehende Sitzung anhand der Quell-IP/Port des Pakets.

    a)  If found, re-decrypt the first 8 bytes with ChaCha20 using Bob's introduction key to recover the Destination Connection ID.
    b)  If the connection ID matches the pending session: Using the correct key, decrypt bytes 8-15 of the header to recover the version, net ID, and message type. Verify the net ID and protocol version are valid, and the message type is Session Created or Retry, or other message type allowed out-of-session (TBD).

    - If all is valid and the message type is Session Created, decrypt the next 16 bytes of the header and the 32-byte Y value with ChaCha20 using Bob's intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Confirmed in response.
    - If all is valid and the message type is Retry, decrypt bytes 16-31 of the header with ChaCha20 using Bob's intro key. Decrypt and validate the message using ChaCha20/Poly1305 using TBD as the key and TBD as the nonce and the decrypted 32-byte header as the AD. Resend a Session Request with the received token in response.
    - If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.

    > c)  If a pending outbound session is not found, or the connection ID does not match the pending session, drop the message, unless the port is shared with SSU 1.

4)  Falls SSU 1 auf demselben Port läuft, versuchen Sie, die Nachricht als SSU 1-Paket zu verarbeiten.

#### Fehlerbehandlung

Im Allgemeinen sollte eine Sitzung (in der Handshake- oder Datenphase) niemals nach dem Empfang eines Pakets mit einem unerwarteten Nachrichtentyp zerstört werden. Dies verhindert Paket-Injektions-Angriffe. Diese Pakete werden auch häufig nach der Neuübertragung eines Handshake-Pakets empfangen, wenn die Header-Entschlüsselungsschlüssel nicht mehr gültig sind.

In den meisten Fällen wird das Paket einfach verworfen. Eine Implementierung kann als Antwort das zuvor gesendete Paket (Handshake-Nachricht oder ACK 0) erneut übertragen, ist aber nicht dazu verpflichtet.

Nach dem Senden von Session Created als Bob sind unerwartete Pakete häufig Data-Pakete, die nicht entschlüsselt werden können, weil die Session Confirmed-Pakete verloren gegangen oder nicht in der richtigen Reihenfolge angekommen sind. Stellen Sie die Pakete in eine Warteschlange und versuchen Sie, sie nach dem Empfang der Session Confirmed-Pakete zu entschlüsseln.

Nachdem Session Confirmed als Bob empfangen wurde, sind unerwartete Pakete häufig erneut übertragene Session Confirmed-Pakete, weil das ACK 0 des Session Confirmed verloren ging. Die unerwarteten Pakete können verworfen werden. Eine Implementierung kann, ist aber nicht verpflichtet, ein Data-Paket mit einem ACK-Block als Antwort zu senden.

### Notizen

Für Session Created und Session Confirmed müssen Implementierungen alle entschlüsselten Header-Felder (Connection IDs, Paketnummer, Pakettyp, Version, ID, Frag und Flags) sorgfältig validieren, BEVOR sie mixHash() auf den Header anwenden und versuchen, die Payload mit Noise AEAD zu entschlüsseln. Wenn die Noise AEAD-Entschlüsselung fehlschlägt, darf keine weitere Verarbeitung durchgeführt werden, da mixHash() den Handshake-Zustand korrumpiert haben wird, es sei denn, eine Implementierung speichert den Hash-Zustand und macht ihn "rückgängig".

### Versionserkennung

Es ist möglicherweise nicht effizient möglich zu erkennen, ob eingehende Pakete Version 1 oder 2 auf demselben eingehenden Port sind. Die oben genannten Schritte sollten sinnvollerweise vor der SSU 1-Verarbeitung durchgeführt werden, um zu vermeiden, dass Trial-DH-Operationen mit beiden Protokollversionen versucht werden.

TBD falls erforderlich.

## Empfohlene Konstanten

- Ausgehender Handshake-Wiederübertragungstimeout: 1,25 Sekunden, mit exponentieller Rückstufung (Wiederübertragungen bei 1,25, 3,75 und 8,75 Sekunden)
- Gesamter ausgehender Handshake-Timeout: 15 Sekunden
- Eingehender Handshake-Wiederübertragungstimeout: 1 Sekunde, mit exponentieller Rückstufung (Wiederübertragungen bei 1, 3 und 7 Sekunden)
- Gesamter eingehender Handshake-Timeout: 12 Sekunden
- Timeout nach Senden eines Wiederholungsversuchs: 9 Sekunden
- ACK-Verzögerung: max(10, min(rtt/6, 150)) ms
- Sofortige ACK-Verzögerung: min(rtt/16, 5) ms
- Maximale ACK-Bereiche: 256?
- Maximale ACK-Tiefe: 512?
- Padding-Verteilung: 0-15 Bytes oder mehr
- Datenphase minimaler Wiederübertragungstimeout: 1 Sekunde, wie in [RFC-6298](https://tools.ietf.org/html/rfc6298)
- Siehe auch [RFC-6298](https://tools.ietf.org/html/rfc6298) für zusätzliche Hinweise zu Wiederübertragungszeitmessern für die Datenphase.

## Paket-Overhead-Analyse

Geht von IPv4 aus, ohne zusätzliche Auffüllung, ohne IP- und UDP-Header-Größen. Auffüllung ist mod-16 Auffüllung nur für SSU 1.

**SSU 1**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MAC</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">40</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">304</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. extended options</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">79</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">336</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 64 byte Ed25519 sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">462</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">512</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 391 byte ident and 64 byte sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (RI)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1014</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1051</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header, 1000 byte RI</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">51</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">2254</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>
**SSU 2**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MACs</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">87</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">96</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime, Address blocks</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1005</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1085</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1000 byte compressed RI block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">46</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1314</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>    
## Probleme und zukünftige Arbeiten

### Token

Wir spezifizieren oben, dass das Token ein zufällig generierter 8-Byte-Wert sein muss und nicht ein undurchsichtiger Wert wie ein Hash oder HMAC eines Server-Geheimnisses und der IP, Port, aufgrund von Wiederverwendungsangriffen. Dies erfordert jedoch temporäre und (optional) dauerhafte Speicherung von zugestellten Tokens. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) verwendet einen 16-Byte-HMAC eines Server-Geheimnisses und einer IP-Adresse, und das Server-Geheimnis rotiert alle zwei Minuten. Wir sollten etwas Ähnliches untersuchen, mit einer längeren Lebensdauer des Server-Geheimnisses. Wenn wir einen Zeitstempel in das Token einbetten, könnte das eine Lösung sein, aber ein 8-Byte-Token ist möglicherweise nicht groß genug dafür.

## Referenzen

- **[Common]** [Spezifikation gemeinsamer Strukturen](/docs/specs/common-structures)
- **[ECIES]** [ECIES-X25519-AEAD-Ratchet Spezifikation](/docs/specs/ecies)
- **[NetDB]** [Netzwerkdatenbank](/docs/overview/network-database)
- **[NOISE]** [Noise Protocol Framework](https://noiseprotocol.org/noise.html)
- **[Nonces]** [Nonce-Disrespecting Adversaries](https://eprint.iacr.org/2019/624.pdf)
- **[NTCP]** [NTCP Transport](/docs/transport/ntcp)
- **[NTCP2]** [NTCP2 Spezifikation](/docs/specs/ntcp2)
- **[PMTU]** [Path MTU Discovery](https://en.wikipedia.org/wiki/Path_MTU_Discovery)
- **[Prop104]** [Vorschlag 104: TLS Transport](/proposals/104-tls-transport)
- **[Prop109]** [Vorschlag 109: Pluggable Transport](/proposals/109-pt-transport)
- **[Prop158]** [Vorschlag 158: IPv6 Transport Erweiterungen](/proposals/158-ipv6-transport-enhancements)
- **[Prop159]** [Vorschlag 159: SSU2](/proposals/159-ssu2)
- **[RFC-2104]** [RFC 2104: HMAC](https://tools.ietf.org/html/rfc2104)
- **[RFC-3449]** [RFC 3449: TCP Performance Auswirkungen](https://tools.ietf.org/html/rfc3449)
- **[RFC-3526]** [RFC 3526: MODP Gruppen](https://tools.ietf.org/html/rfc3526)
- **[RFC-5681]** [RFC 5681: TCP Staukontrolle](https://tools.ietf.org/html/rfc5681)
- **[RFC-5869]** [RFC 5869: HKDF](https://tools.ietf.org/html/rfc5869)
- **[RFC-6151]** [RFC 6151: MD5 Sicherheitsüberlegungen](https://tools.ietf.org/html/rfc6151)
- **[RFC-6298]** [RFC 6298: TCP Wiederübertragungszeittakt](https://tools.ietf.org/html/rfc6298)
- **[RFC-6437]** [RFC 6437: IPv6 Flow Label](https://tools.ietf.org/html/rfc6437)
- **[RFC-7539]** [RFC 7539: ChaCha20/Poly1305](https://tools.ietf.org/html/rfc7539)
- **[RFC-7748]** [RFC 7748: Elliptische Kurven für Sicherheit](https://tools.ietf.org/html/rfc7748)
- **[RFC-7905]** [RFC 7905: ChaCha20-Poly1305 Cipher Suites für TLS](https://tools.ietf.org/html/rfc7905)
- **[RFC-9000]** [RFC 9000: QUIC Transport Protokoll](https://datatracker.ietf.org/doc/html/rfc9000)
- **[RFC-9001]** [RFC 9001: TLS zur Sicherung von QUIC verwenden](https://datatracker.ietf.org/doc/html/rfc9001)
- **[RFC-9002]** [RFC 9002: QUIC Verlusterkennung und Staukontrolle](https://datatracker.ietf.org/doc/html/rfc9002)
- **[RouterAddress]** [RouterAddress Struktur](/docs/specs/common-structures#struct-routeraddress)
- **[RouterIdentity]** [RouterIdentity Struktur](/docs/specs/common-structures#struct-routeridentity)
- **[SigningPublicKey]** [SigningPublicKey Typ](/docs/specs/common-structures#type-signingpublickey)
- **[SSU]** [SSU Transport](/docs/transport/ssu)
- **[STS]** [Station-to-Station Protokoll](https://en.wikipedia.org/wiki/Station-to-Station_protocol)
- **[Ticket1112]** [I2P Ticket 1112](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1112)
- **[Ticket1849]** [I2P Ticket 1849](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1849)
- **[WireGuard]** [WireGuard Protokoll](https://www.wireguard.com/papers/wireguard.pdf)
