---
title: "Streaming Protocol Spezifikation"
description: "Spezifikation für das I2P-Streaming-Protokoll, das eine TCP-ähnliche zuverlässige Übertragung bereitstellt"
slug: "streaming"
category: "Protokolle"
lastUpdated: "2023-10"
accurateFor: "0.9.59"
---

## Überblick

Siehe [Streaming Library](/docs/api/streaming) für einen Überblick über das Streaming-Protokoll.

## Protokollversionen

Das Streaming-Protokoll enthält kein Versionsfeld. Die unten aufgeführten Versionen gelten für Java I2P. Implementierungen und tatsächliche Krypto-Unterstützung können variieren. Es gibt keine Möglichkeit zu bestimmen, ob das entfernte Ende eine bestimmte Version oder Funktion unterstützt. Die untenstehende Tabelle dient als allgemeine Orientierung bezüglich der Veröffentlichungsdaten für verschiedene Funktionen.

Die unten aufgeführten Funktionen beziehen sich auf das Protokoll selbst. Verschiedene Konfigurationsoptionen sind in der [Streaming Library](/docs/api/streaming) zusammen mit der Java I2P-Version dokumentiert, in der sie implementiert wurden.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Router Version</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Streaming Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Bob's hash in NACKs field of SYN packet</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE option</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">I2CP protocol number enforced</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED no longer required in RESET</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PINGs and PONGs may include a payload</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA Ed25519 sig type</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA P-256, P-384, and P-521 sig types</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Variable-length signatures</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.7.1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Protocol numbers defined in I2CP</td>
    </tr>
  </tbody>
</table>
## Protokoll-Spezifikation

### Paketformat

Das Format eines einzelnen Pakets im Streaming-Protokoll wird unten gezeigt. Die minimale Header-Größe, ohne NACKs oder Optionsdaten, beträgt 22 Bytes.

Es gibt kein Längenfeld im Streaming-Protokoll. Die Rahmenbildung wird von den unteren Schichten bereitgestellt - I2CP und I2NP.

```
+----+----+----+----+----+----+----+----+
| send Stream ID    | rcv Stream ID     |
+----+----+----+----+----+----+----+----+
| sequence  Num     | ack Through       |
+----+----+----+----+----+----+----+----+
| nc |  nc*4 bytes of NACKs (optional)
+----+----+----+----+----+----+----+----+
     | rd |  flags  | opt size| opt data
+----+----+----+----+----+----+----+----+
   ...  (optional, see below)           |
+----+----+----+----+----+----+----+----+
|   payload ...
+----+----+----+-//
```
**sendStreamId** :: 4 byte [Integer](/docs/specs/common-structures#integer) : Zufallszahl, die vom Paketempfänger vor dem Senden des ersten SYN-Antwortpakets ausgewählt wird und für die Lebensdauer der Verbindung konstant bleibt, größer als null. 0 in der SYN-Nachricht, die vom Verbindungsinitiator gesendet wird, und in nachfolgenden Nachrichten, bis eine SYN-Antwort empfangen wird, die die Stream-ID des Peers enthält.

**receiveStreamId** :: 4 Byte [Integer](/docs/specs/common-structures#integer) : Zufallszahl, die vom Paket-Urheber vor dem Senden des ersten SYN-Pakets ausgewählt und für die Lebensdauer der Verbindung konstant ist, größer als null. Kann 0 sein, falls unbekannt, zum Beispiel in einem RESET-Paket.

**sequenceNum** :: 4 Byte [Integer](/docs/specs/common-structures#integer) : Die Sequenznummer für diese Nachricht, beginnend bei 0 in der SYN-Nachricht und um 1 in jeder Nachricht erhöht, außer bei einfachen ACKs und Neuübertragungen. Wenn die sequenceNum 0 ist und das SYN-Flag nicht gesetzt ist, handelt es sich um ein einfaches ACK-Paket, das nicht bestätigt werden sollte.

**ackThrough** :: 4 Byte [Integer](/docs/specs/common-structures#integer) : Die höchste Paket-Sequenznummer, die auf der receiveStreamId empfangen wurde. Dieses Feld wird beim ersten Verbindungspaket ignoriert (wo receiveStreamId die unbekannte ID ist) oder wenn das NO_ACK-Flag gesetzt ist. Alle Pakete bis einschließlich dieser Sequenznummer werden mit ACK bestätigt, AUSSER denen, die in den NACKs unten aufgelistet sind.

**NACK-Anzahl** :: 1 Byte [Integer](/docs/specs/common-structures#integer) : Die Anzahl der 4-Byte-NACKs im nächsten Feld, oder 8 wenn zusammen mit SYNCHRONIZE für Replay-Schutz ab 0.9.58 verwendet; siehe unten.

**NACKs** :: nc * 4 Byte [Integer](/docs/specs/common-structures#integer)s : Sequenznummern kleiner als ackThrough, die noch nicht empfangen wurden. Zwei NACKs eines Pakets sind eine Anfrage für eine 'schnelle Wiederübertragung' dieses Pakets. Wird seit 0.9.58 auch zusammen mit SYNCHRONIZE zur Replay-Verhinderung verwendet; siehe unten.

**resendDelay** :: 1 Byte [Integer](/docs/specs/common-structures#integer) : Wie lange wird der Ersteller dieses Pakets warten, bevor er dieses Paket erneut sendet (falls es noch nicht bestätigt wurde). Der Wert sind Sekunden seit der Paketerstellung. Wird derzeit beim Empfang ignoriert.

**flags** :: 2-Byte-Wert : Siehe unten.

**option size** :: 2 Byte [Integer](/docs/specs/common-structures#integer) : Die Anzahl der Bytes im nächsten Feld

**option data** :: 0 oder mehr Bytes : Wie durch die Flags spezifiziert. Siehe unten.

**payload** :: verbleibende Paketgröße

### Flags und Optionsdatenfelder

Das Flags-Feld oben spezifiziert einige Metadaten über das Paket und kann wiederum erfordern, dass bestimmte zusätzliche Daten eingeschlossen werden. Die Flags sind wie folgt. Alle spezifizierten Datenstrukturen müssen dem Optionsbereich in der angegebenen Reihenfolge hinzugefügt werden.

Bit-Reihenfolge: 15....0 (15 ist MSB)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Flag</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Order</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SYNCHRONIZE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP SYN. Set in the initial packet and in the first response. FROM_INCLUDED and SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">CLOSE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP FIN. If the response to a SYNCHRONIZE fits in a single message, the response will contain both SYNCHRONIZE and CLOSE. SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RESET</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Abnormal close. SIGNATURE_INCLUDED must also be set. Prior to release 0.9.20, due to a bug, FROM_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#signature">Signature</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, CLOSE, and RESET, where it is required, and with ECHO, where it is required for a ping. The signature uses the Destination's <a href="/docs/specs/common-structures#signingprivatekey">SigningPrivateKey</a> to sign the entire header and payload with the space in the option data field for the signature being set to all zeroes. Prior to release 0.9.11, the signature was always 40 bytes. As of release 0.9.11, the signature may be variable-length, see below for details.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused. Requests every packet in the other direction to have SIGNATURE_INCLUDED</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">387+ byte <a href="/docs/specs/common-structures#destination">Destination</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, where it is required, and with ECHO, where it is required for a ping. Prior to release 0.9.20, due to a bug, must also be sent with RESET.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DELAY_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Optional delay. How many milliseconds the sender of this packet wants the recipient to wait before sending any more data. A value greater than 60000 indicates choking. A value of 0 requests an immediate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MAX_PACKET_SIZE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum length of the payload. Send with SYNCHRONIZE.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PROFILE_INTERACTIVE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused or ignored; the interactive profile is unimplemented.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECHO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused except by ping programs. If set, most other options are ignored. See the <a href="/docs/api/streaming">streaming docs</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">NO_ACK</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">This flag simply tells the recipient to ignore the ackThrough field in the header. Currently set in the initial SYN packet, otherwise the ackThrough field is always valid. Note that this does not save any space, the ackThrough field is before the flags and is always present.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#offlinesignature">OfflineSig</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Contains the offline signature section from LS2. See proposal 123 and the common structures specification. FROM_INCLUDED must also be set. Contains an OfflineSig: 1) Expires timestamp (4 bytes, seconds since epoch, rolls over in 2106) 2) Transient sig type (2 bytes) 3) Transient <a href="/docs/specs/common-structures#signingpublickey">SigningPublicKey</a> (length as implied by sig type) 4) <a href="/docs/specs/common-structures#signature">Signature</a> of expires timestamp, transient sig type, and public key, by the destination public key. Length of sig as implied by the destination public key sig type.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12-15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">unused</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Set to zero for compatibility with future uses.</td>
    </tr>
  </tbody>
</table>
### Hinweise zu Signaturen mit variabler Länge

Vor Release 0.9.11 war die Signatur im Optionsfeld immer 40 Bytes lang.

Ab Version 0.9.11 ist die Signatur von variabler Länge. Der Signatur-Typ und die Länge werden aus dem Schlüsseltyp abgeleitet, der in der FROM_INCLUDED-Option verwendet wird, und aus der [Signature](/docs/specs/common-structures#signature)-Dokumentation.

Ab Release 0.9.39 wird die OFFLINE_SIGNATURE-Option unterstützt. Wenn diese Option vorhanden ist, wird der transiente [SigningPublicKey](/docs/specs/common-structures#signingpublickey) verwendet, um alle signierten Pakete zu verifizieren, und die Signaturlänge und der Typ werden aus dem transienten SigningPublicKey in der Option abgeleitet.

- Wenn ein Paket sowohl FROM_INCLUDED als auch SIGNATURE_INCLUDED enthält (wie bei SYNCHRONIZE), kann die Schlussfolgerung direkt gezogen werden.

- Wenn ein Paket kein FROM_INCLUDED enthält, muss die Ableitung aus einem vorherigen SYNCHRONIZE-Paket erfolgen.

- Wenn ein Paket kein FROM_INCLUDED enthält und es kein vorheriges SYNCHRONIZE-Paket gab (zum Beispiel ein verirrtes CLOSE- oder RESET-Paket), kann die Schlussfolgerung aus der Länge der verbleibenden Optionen gezogen werden (da SIGNATURE_INCLUDED die letzte Option ist), aber das Paket wird wahrscheinlich trotzdem verworfen, da kein FROM verfügbar ist, um die Signatur zu validieren. Falls in Zukunft weitere Optionsfelder definiert werden, müssen diese berücksichtigt werden.

### Replay-Schutz

Um zu verhindern, dass Bob einen Replay-Angriff durchführt, indem er ein gültiges signiertes SYNCHRONIZE-Paket von Alice speichert und es später an ein Opfer Charlie sendet, muss Alice Bobs Destination-Hash wie folgt in das SYNCHRONIZE-Paket einbinden:

```
Set NACK count field to 8
Set the NACKs field to Bob's 32-byte destination hash
```
Nach dem Empfang einer SYNCHRONIZE muss Bob, wenn das NACK-Anzahl-Feld 8 ist, das NACKs-Feld als einen 32-Byte-Destination-Hash interpretieren und überprüfen, dass dieser mit seinem Destination-Hash übereinstimmt. Er muss auch wie üblich die Signatur des Pakets verifizieren, da diese das gesamte Paket einschließlich der NACK-Anzahl- und NACKs-Felder abdeckt. Wenn die NACK-Anzahl 8 ist und das NACKs-Feld nicht übereinstimmt, muss Bob das Paket verwerfen.

Dies ist für Versionen 0.9.58 und höher erforderlich. Dies ist rückwärtskompatibel mit älteren Versionen, da NACKs in einem SYNCHRONIZE-Paket nicht erwartet werden. Destinations wissen nicht und können nicht wissen, welche Version am anderen Ende läuft.

Für das SYNCHRONIZE ACK-Paket, das von Bob an Alice gesendet wird, ist keine Änderung erforderlich; NACKs dürfen nicht in diesem Paket enthalten sein.

## Referenzen

- **[Destination]** [Destination](/docs/specs/common-structures#destination)
- **[Integer]** [Integer](/docs/specs/common-structures#integer)
- **[OfflineSig]** [OfflineSignature](/docs/specs/common-structures#offlinesignature)
- **[Signature]** [Signature](/docs/specs/common-structures#signature)
- **[SigningPrivateKey]** [SigningPrivateKey](/docs/specs/common-structures#signingprivatekey)
- **[SigningPublicKey]** [SigningPublicKey](/docs/specs/common-structures#signingpublickey)
- **[STREAMING]** [Streaming-Bibliothek](/docs/api/streaming)
