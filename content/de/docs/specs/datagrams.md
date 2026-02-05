---
title: "Datagramm-Spezifikation"
description: "Spezifikation der I2P-Datagramm-Nachrichtenformate einschließlich Raw-, Antwortbare- und Authentifizierte-Typen"
slug: "datagrams"
category: "Protokolle"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

## Übersicht

Siehe die [Datagrams API-Dokumentation](/docs/api/datagrams/) für einen Überblick über die Datagrams API.

Die folgenden Typen sind definiert. Die Standard-Protokollnummern sind aufgelistet, jedoch können alle anderen Protokollnummern außer der Streaming-Protokollnummer (6) anwendungsspezifisch verwendet werden.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Protocol</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Repliable?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Authenticated?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Replay Prevention?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">As Of</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Raw</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
  </tbody>
</table>
Die Unterstützung für Datagram2 und Datagram3 in verschiedenen Router- und Bibliotheksimplementierungen ist noch zu bestimmen. Prüfen Sie die Dokumentation für diese Implementierungen.

### Datagram-Typ-Identifikation

Die vier Datagrammtypen teilen keinen gemeinsamen Header mit der Protokollversion an derselben Stelle. Pakete können nicht anhand ihres Inhalts nach Typ identifiziert werden. Bei der Verwendung mehrerer Typen in derselben Sitzung oder eines einzelnen Typs zusammen mit Streaming müssen Anwendungen Protokollnummern und/oder I2CP/SAM-Ports verwenden, um eingehende Pakete an die richtige Stelle zu leiten. Die Verwendung von Standardprotokollnummern wird dies erleichtern. Die Protokollnummer ungesetzt zu lassen (0 oder PROTO_ANY), selbst für eine reine Datagramm-Anwendung, wird nicht empfohlen, da dies die Wahrscheinlichkeit von Routing-Fehlern erhöht und Upgrades auf eine Multi-Protokoll-Anwendung erschwert. Versionsfelder in Datagram 2 und 3 werden nur als zusätzliche Prüfung für Routing-Fehler und zukünftige Änderungen bereitgestellt.

### Anwendungsdesign

Alle Verwendungen von Datagrammen sind anwendungsspezifisch.

Da authentifizierte Datagramme erheblichen Overhead verursachen, verwendet eine typische Anwendung sowohl authentifizierte als auch nicht-authentifizierte Datagramme. Ein typisches Design besteht darin, ein einzelnes authentifiziertes Datagramm mit einem Token vom Client an den Server zu senden. Der Server antwortet mit einem nicht-authentifizierten Datagramm, das dasselbe Token enthält. Jegliche weitere Kommunikation vor dem Token-Timeout verwendet rohe Datagramme.

Anwendungen senden und empfangen Datagramme mit Protokoll- und Portnummern über die [I2CP](/docs/specs/i2cp/) API oder [SAMv3](/docs/api/samv3/).

Datagramme sind natürlich unzuverlässig. Anwendungen müssen für unzuverlässige Zustellung entwickelt werden. Innerhalb von I2P ist die Zustellung von Hop zu Hop zuverlässig, wenn der nächste Hop erreichbar ist, da die NTCP2- und SSU2-Transporte Zuverlässigkeit bieten. Die Ende-zu-Ende-Zustellung ist jedoch nicht zuverlässig, da I2NP-Nachrichten innerhalb jedes Hops aufgrund von Warteschlangenlimits, Ablaufzeiten, Timeouts, Bandbreitenbeschränkungen oder nicht erreichbaren nächsten Hops verworfen werden können.

### Datagramm-Größe

Das nominelle Größenlimit für I2NP-Nachrichten, einschließlich Datagramme, beträgt 64 KB. Garlic- und Tunnel-Nachrichten-Overhead reduzieren dies etwas.

Allerdings müssen alle I2NP-Nachrichten in 1 KB tunnel-Nachrichten fragmentiert werden. Die Ausfallwahrscheinlichkeit einer n KB I2NP-Nachricht ist die Exponentialfunktion der Ausfallwahrscheinlichkeit einer einzelnen tunnel-Nachricht, p ** n. Da die Fragmentierung zu einem Burst von tunnel-Nachrichten führt, ist die tatsächliche Ausfallwahrscheinlichkeit viel höher als die Exponentialfunktion vermuten lassen würde, aufgrund von Warteschlangenlimits und aktivem Warteschlangenmanagement (AQM, CoDel oder ähnlich) in router-Implementierungen.

Die empfohlene typische Maximalgröße zur Gewährleistung zuverlässiger Zustellung beträgt einige KB oder höchstens 10 KB. Durch sorgfältige Analyse der Overhead-Größen auf allen Protokollebenen (außer Transport) sollten Entwickler eine maximale Payload-Größe festlegen, die genau in eine, zwei oder drei tunnel messages passt. Dies maximiert Effizienz und Zuverlässigkeit. Der Overhead auf verschiedenen Ebenen umfasst den gzip-Header, I2NP-Header, garlic message-Header, garlic encryption, tunnel message-Header, tunnel message-Fragmentierungs-Header und andere. Siehe Streaming-MTU-Berechnungen in [Proposal 144](/proposals/144-ecies-x25519-aead-ratchet/) und ConnectionOptions.java im Java I2P-Quellcode für Beispiele.

### SAM Überlegungen

Anwendungen senden und empfangen Datagramme unter Verwendung von Protokoll- und Portnummern über die I2CP API oder SAM. Die Angabe von Protokoll- und Portnummern über SAM erfordert SAM v3.2 oder höher. Die Verwendung sowohl von Datagrammen als auch von Streaming (UDP und TCP) in derselben SAM-Sitzung (tunnels) erfordert SAM v3.3 oder höher. Die Verwendung mehrerer Datagrammtypen in derselben SAM-Sitzung (tunnels) erfordert SAM v3.3 oder höher. SAM v3.3 wird derzeit nur vom Java I2P router unterstützt.

SAM-Unterstützung für Datagram2 und Datagram3 in verschiedenen Router- und Bibliotheksimplementierungen ist noch zu bestimmen. Überprüfen Sie die Dokumentation für diese Implementierungen.

Beachten Sie, dass Größen über eine typische 1500-Byte-Netzwerk-MTU SAM-Anwendungen daran hindern, unfragmentierte Pakete zum/vom SAM-Server zu transportieren, wenn sich Anwendung und Server auf verschiedenen Computern befinden. Normalerweise ist dies nicht der Fall, da sich beide auf localhost befinden, wo die MTU 65536 oder höher ist. Falls erwartet wird, dass eine SAM-Anwendung auf einem anderen Computer als der Server getrennt wird, liegt die maximale Payload für ein beantwortbares Datagramm knapp unter 1 KB.

### PQ-Überlegungen

Wenn der MLDSA-Teil des Post-Quantum [Proposal 169](/proposals/169-pq-crypto/) implementiert wird, wird der Overhead erheblich zunehmen. Die Größe einer Destination + Signatur wird von 391 + 64 = 455 Bytes auf mindestens 3739 für MLDSA44 und maximal 7226 für MLDSA87 ansteigen. Die praktischen Auswirkungen davon sind noch zu bestimmen. Datagram3 mit Authentifizierung durch den Router könnte eine Lösung sein.

## Rohe (Nicht-Beantwortbare) Datagramme {#raw}

Nicht-antwortbare Datagramme haben keine 'from'-Adresse und sind nicht authentifiziert. Sie werden auch "raw" Datagramme genannt. Streng genommen sind sie überhaupt keine "Datagramme", sondern nur rohe Daten. Sie werden nicht von der Datagramm-API verarbeitet. Jedoch unterstützen SAM und die I2PTunnel-Klassen "raw datagrams".

Die Standard-I2CP-Protokollnummer für raw datagrams ist PROTO_DATAGRAM_RAW (18).

Das Format wird hier nicht spezifiziert, es wird von der Anwendung definiert. Der Vollständigkeit halber fügen wir unten ein Bild des Formats bei.

### Format

```
+----+----+----+----+----//
| payload...
+----+----+----+----+----//

length: 0 - about 64 KB (see notes)
```
### Notizen

Die praktische Länge ist sowohl durch den Overhead auf verschiedenen Schichten als auch durch die Zuverlässigkeit begrenzt.

## Datagram1 (Antwortfähig) {#repliable}

Beantwortbare Datagramme enthalten eine 'from'-Adresse und eine Signatur. Diese fügen mindestens 427 Bytes an Overhead hinzu.

Die Standard-I2CP-Protokollnummer für beantwortbare Datagramme ist PROTO_DATAGRAM (17).

### Format

```
+----+----+----+----+----+----+----+----+
| from                                  |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+                                       +
|                                       |
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
| payload...
+----+----+----+----//

from :: a Destination
        length: 387+ bytes
        The originator and signer of the datagram

signature :: a Signature
             Signature type must match the signing public key type of $from
             length: 40+ bytes, as implied by the Signature type.
             For the default DSA_SHA1 key type:
                The DSA Signature of the SHA-256 hash of the payload.
             For other key types:
                The Signature of the payload.
             The signature may be verified by the signing public key of $from

payload :: The data
           Length: 0 to about 63 KB (see notes)

Total length: Payload length + 427+
```
### Notizen

- Die praktische Länge ist sowohl durch Overhead auf verschiedenen Schichten als auch durch Zuverlässigkeit begrenzt.
- Siehe wichtige Hinweise zur Zuverlässigkeit großer Datagramme in der [Datagrams API-Dokumentation](/docs/api/datagrams/). Für beste Ergebnisse begrenzen Sie die Nutzdaten auf etwa 10 KB oder weniger.
- Signaturen für andere Typen als DSA_SHA1 wurden in Version 0.9.14 neu definiert.
- Das Format unterstützt nicht die Einbindung eines Offline-Signaturblocks für LS2 (Vorschlag 123). Ein neues Protokoll mit Flags muss dafür definiert werden.

## Datagram2 {#datagram2}

Das Datagram2-Format ist wie in [Proposal 163](/proposals/163-datagram2/) spezifiziert. Die I2CP-Protokollnummer für Datagram2 ist 19.

Datagram2 ist als Ersatz für Datagram1 vorgesehen. Es fügt Datagram1 die folgenden Funktionen hinzu:

- Replay-Verhinderung
- Offline-Signatur-Unterstützung
- Flags- und Optionsfelder für Erweiterbarkeit

Beachten Sie, dass der Signaturberechnungsalgorithmus für Datagram2 sich erheblich von dem für Datagram1 unterscheidet.

### Format

```
+----+----+----+----+----+----+----+----+
|                                       |
~            from                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~     offline_signature (optional)      ~
~   expires, sigtype, pubkey, offsig    ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            signature                  ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

from :: a Destination
        length: 387+ bytes
        The originator and (unless offline signed) signer of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x02 (0 0 1 0)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bit 5: If 0, no offline sig; if 1, offline signed
         Bits 15-6: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

offline_signature ::
             If flag indicates offline keys, the offline signature section,
             as specified in the Common Structures Specification,
             with the following 4 fields. Length: varies by online and offline
             sig types, typically 102 bytes for Ed25519
             This section can, and should, be generated offline.

  expires :: Expires timestamp
             (4 bytes, big endian, seconds since epoch, rolls over in 2106)

  sigtype :: Transient sig type (2 bytes, big endian)

  pubkey :: Transient signing public key (length as implied by sig type),
            typically 32 bytes for Ed25519 sig type.

  offsig :: a Signature
            Signature of expires timestamp, transient sig type,
            and public key, by the destination public key,
            length: 40+ bytes, as implied by the Signature type, typically
            64 bytes for Ed25519 sig type.

payload :: The data
           Length: 0 to about 61 KB (see notes)

signature :: a Signature
             Signature type must match the signing public key type of $from
             (if no offline signature) or the transient sigtype
             (if offline signed)
             length: 40+ bytes, as implied by the Signature type, typically
             64 bytes for Ed25519 sig type.
             The Signature of the payload and other fields as specified below.
             The signature is verified by the signing public key of $from
             (if no offline signature) or the transient pubkey
             (if offline signed)
```
Gesamtlänge: mindestens 433 + Nutzlastlänge; typische Länge für X25519-Absender und ohne Offline-Signaturen: 457 + Nutzlastlänge. Beachten Sie, dass die Nachricht normalerweise mit gzip auf der I2CP-Ebene komprimiert wird, was zu erheblichen Einsparungen führt, wenn das Absenderziel komprimierbar ist.

Hinweis: Das Offline-Signaturformat ist dasselbe wie in der [Common Structures Specification](/docs/specs/common-structures/) und [Streaming Specification](/docs/specs/streaming/).

### Signaturen

Die Signatur erstreckt sich über die folgenden Felder:

- Prelude: Der 32-Byte-Hash des Zielziels (nicht im Datagramm enthalten)
- flags
- options (falls vorhanden)
- offline_signature (falls vorhanden)
- payload

Bei repliable datagram war die Signatur für den DSA_SHA1-Schlüsseltyp über den SHA-256-Hash der Nutzdaten, nicht über die Nutzdaten selbst; hier ist die Signatur immer über die oben genannten Felder (NICHT den Hash), unabhängig vom Schlüsseltyp.

### ToHash-Verifikation

Empfänger müssen die Signatur (unter Verwendung ihres Destination-Hash) verifizieren und das Datagramm bei einem Fehler verwerfen, um Replay-Angriffe zu verhindern.

## Datagram3 {#datagram3}

Das Datagram3-Format ist wie in [Proposal 163](/proposals/163-datagram2/) spezifiziert. Die I2CP-Protokollnummer für Datagram3 ist 20.

Datagram3 ist als erweiterte Version von rohen Datagrammen gedacht. Es fügt den rohen Datagrammen folgende Funktionen hinzu:

- Replizierbarkeit
- Flags und Optionsfelder für Erweiterbarkeit

Datagram3 ist NICHT authentifiziert. In einem zukünftigen Vorschlag könnte die Authentifizierung durch die ratchet-Schicht des routers bereitgestellt werden, und der Authentifizierungsstatus würde an den Client weitergegeben werden.

### Format

```
+----+----+----+----+----+----+----+----+
|                                       |
~            fromhash                   ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

fromhash :: a Hash
            length: 32 bytes
            The originator of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x03 (0 0 1 1)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bits 15-5: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

payload :: The data
           Length: 0 to about 61 KB (see notes)
```
Gesamtlänge: mindestens 34 + Nutzdatenlänge.

## Referenzen

- [Common](/docs/specs/common-structures/) - Common Structures Spezifikation
- [DATAGRAMS](/docs/api/datagrams/) - Datagrams API Übersicht
- [I2CP](/docs/specs/i2cp/) - I2CP Spezifikation
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet/) - ECIES-X25519-AEAD-Ratchet Vorschlag
- [Prop163](/proposals/163-datagram2/) - Datagram2 und Datagram3 Vorschlag
- [Prop169](/proposals/169-pq-crypto/) - Post-Quantum Kryptographie Vorschlag
- [SAMv3](/docs/api/samv3/) - SAM v3 Spezifikation
- [Streaming](/docs/specs/streaming/) - Streaming Spezifikation
- [TRANSPORT](/docs/overview/transport/) - Transport Übersicht
- [TUNMSG](/docs/specs/tunnel-message/#notes) - Tunnel Message Spezifikation
