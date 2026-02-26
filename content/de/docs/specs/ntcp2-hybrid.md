---
title: "PQ Hybrid NTCP2"
description: "Post-Quanten-Hybrid-Variante des NTCP2 Transportprotokolls unter Verwendung von ML-KEM"
slug: "ntcp2-hybrid"
lastupdated: "2026-02"
category: "Transports"
accurateFor: "0.9.69"
---

### Status

Beta Q1 2026, Veröffentlichung Q2 2026

## Übersicht

Dies ist die hybride Post-Quantum-Variante des NTCP2-Transportprotokolls, wie in Vorschlag 169 entworfen. Siehe diesen Vorschlag für zusätzliche Hintergrundinformationen.

PQ Hybrid NTCP2 ist nur auf derselben Adresse und demselben Port wie Standard-NTCP2 definiert. Der Betrieb auf einem anderen Port oder ohne Standard-NTCP2-Unterstützung ist nicht erlaubt und wird es auch für mehrere Jahre nicht sein, bis Standard-NTCP2 als veraltet eingestuft wird.

Diese Spezifikation dokumentiert nur die Änderungen, die am Standard-NTCP2 erforderlich sind, um PQ Hybrid zu unterstützen. Siehe die NTCP2-Spezifikation für die grundlegenden Implementierungsdetails.

## Design

Wir unterstützen die NIST FIPS 203 und 204 Standards [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf), die auf CRYSTALS-Kyber und CRYSTALS-Dilithium basieren, aber NICHT kompatibel sind mit den Versionen 3.1, 3 und älteren.

### Schlüsselaustausch

PQ KEM stellt nur ephemerale Schlüssel zur Verfügung und unterstützt nicht direkt Static-Key-Handshakes wie Noise XK und IK. Die Verschlüsselungstypen sind die gleichen wie in PQ Hybrid Ratchet verwendet und sind im Dokument für gemeinsame Strukturen [/docs/specs/common-structures/](/docs/specs/common-structures/) definiert, wie in [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf). Hybride Typen sind nur in Kombination mit X25519 definiert.

Die Verschlüsselungstypen sind:

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Typ</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Code</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">6</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">7</td>
</tr>
</table>

### Zulässige Kombinationen

Die neuen Verschlüsselungstypen werden in den RouterAddresses angegeben. Der Verschlüsselungstyp im Schlüsselzertifikat wird weiterhin Typ 4 sein.

## Spezifikation

### Handshake-Muster

Handshakes verwenden [Noise Protocol](https://noiseprotocol.org/noise.html) Handshake-Muster.

Die folgende Buchstabenzuordnung wird verwendet:

- e = einmaliger ephemerer Schlüssel
- s = statischer Schlüssel
- p = Nachrichten-Payload
- e1 = einmaliger ephemerer PQ-Schlüssel, von Alice an Bob gesendet
- ekem1 = der KEM-Chiffretext, von Bob an Alice gesendet

Die folgenden Änderungen an XK und IK für hybride Forward Secrecy (hfs) sind wie in der [Noise HFS Spezifikation](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) Abschnitt 5 spezifiziert:

```
XK:                       XKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, p               -> e, es, e1, p
  <- e, ee, p               <- e, ee, ekem1, p
  -> s, se                  -> s, se
  <- p                      <- p
  p ->                      p ->


  e1 and ekem1 are encrypted. See pattern definitions below.
  NOTE: e1 and ekem1 are different sizes (unlike X25519)
```
Das e1-Muster ist wie folgt definiert, wie in der [Noise HFS-Spezifikation](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) Abschnitt 4 angegeben:

```
For Alice:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++
  MixHash(ciphertext)

  For Bob:

  // DecryptAndHash(ciphertext)
  encap_key = DECRYPT(k, n, ciphertext, ad)
  n++
  MixHash(ciphertext)
```
Das ekem1-Muster ist wie folgt definiert, wie in der [Noise HFS-Spezifikation](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) Abschnitt 4 spezifiziert:

```
For Bob:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  MixKey(kem_shared_key)


  For Alice:

  // DecryptAndHash(ciphertext)
  kem_ciphertext = DECRYPT(k, n, ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  MixKey(kem_shared_key)
```
### Noise Handshake KDF

#### Überblick

Der Hybrid-Handshake ist in der [Noise HFS Spezifikation](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) definiert. Die erste Nachricht von Alice an Bob enthält e1, den Encapsulation-Schlüssel, vor der Nachrichtenutzlast. Dieser wird als zusätzlicher statischer Schlüssel behandelt; rufen Sie EncryptAndHash() darauf auf (als Alice) oder DecryptAndHash() (als Bob). Verarbeiten Sie dann die Nachrichtenutzlast wie üblich.

Die zweite Nachricht, von Bob an Alice, enthält ekem1, den Chiffretext, vor der Nachrichten-Payload. Dies wird als zusätzlicher statischer Schlüssel behandelt; rufe EncryptAndHash() darauf auf (als Bob) oder DecryptAndHash() (als Alice). Berechne dann den kem_shared_key und rufe MixKey(kem_shared_key) auf. Verarbeite dann die Nachrichten-Payload wie üblich.

#### Definierte ML-KEM-Operationen

Wir definieren die folgenden Funktionen entsprechend den kryptographischen Bausteinen, die wie in [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) definiert verwendet werden.

(encap_key, decap_key) = PQ_KEYGEN()

    Alice creates the encapsulation and decapsulation keys
    The encapsulation key is sent in message 1.
    encap_key and decap_key sizes vary based on ML-KEM variant.

(ciphertext, kem_shared_key) = ENCAPS(encap_key)

    Bob calculates the ciphertext and shared key,
    using the ciphertext received in message 1.
    The ciphertext is sent in message 2.
    ciphertext size varies based on ML-KEM variant.
    The kem_shared_key is always 32 bytes.

kem_shared_key = DECAPS(ciphertext, decap_key)

    Alice calculates the shared key,
    using the ciphertext received in message 2.
    The kem_shared_key is always 32 bytes.

Beachten Sie, dass sowohl der encap_key als auch der ciphertext innerhalb von ChaCha/Poly-Blöcken in den Noise-Handshake-Nachrichten 1 und 2 verschlüsselt sind. Sie werden als Teil des Handshake-Prozesses entschlüsselt.

Der kem_shared_key wird mit MixHash() in den chaining key eingemischt. Siehe unten für Details.

#### Alice KDF für Nachricht 1

Nach dem 'es' Nachrichtenmuster und vor der Nutzdaten, füge hinzu:

```
This is the "e1" message pattern:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)


  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### Bob KDF für Nachricht 1

Nach dem 'es' Nachrichtenmuster und vor der Nutzlast, fügen Sie hinzu:

```
This is the "e1" message pattern:

  // DecryptAndHash(encap_key_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  encap_key = DECRYPT(k, n, encap_key_section, ad)
  n++

  // MixHash(encap_key_section)
  h = SHA256(h || encap_key_section)

  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### Bob KDF für Nachricht 2

Für XK: Nach dem 'ee' Nachrichtenmuster und vor der Payload, hinzufügen:

```
This is the "ekem1" message pattern:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  // MixKey(kem_shared_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### Alice KDF für Nachricht 2

Nach dem 'ee' Nachrichtenmuster hinzufügen:

```
This is the "ekem1" message pattern:

  // DecryptAndHash(kem_ciphertext_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  kem_ciphertext = DECRYPT(k, n, kem_ciphertext_section, ad)

  // MixHash(kem_ciphertext_section)
  h = SHA256(h || kem_ciphertext_section)

  // MixKey(kem_shared_key)
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### KDF für Nachricht 3 (nur XK)

unverändert

#### KDF für split()

unverändert

### Handshake-Details

#### Noise-Kennungen

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

Änderungen: Das aktuelle NTCP2 enthält nur die Optionen im ChaCha-Abschnitt. Mit ML-KEM wird der ChaCha-Abschnitt auch den verschlüsselten PQ-Public-Key enthalten.

Damit PQ und Nicht-PQ NTCP2 auf derselben router-Adresse und demselben Port unterstützt werden können, verwenden wir das höchstwertige Bit des X-Werts (X25519 ephemeral public key), um zu kennzeichnen, dass es sich um eine PQ-Verbindung handelt. Dieses Bit ist bei Nicht-PQ-Verbindungen immer nicht gesetzt.

Für Alice wird nach der Verschlüsselung der Nachricht durch Noise, aber vor der AES-Verschleierung von X, X[31] |= 0x7f gesetzt.

Für Bob, nach der AES-Entschleierung von X, teste X[31] & 0x80. Wenn das Bit gesetzt ist, lösche es mit X[31] &= 0x7f und entschlüssele über Noise als PQ-Verbindung. Wenn das Bit nicht gesetzt ist, entschlüssele über Noise als Nicht-PQ-Verbindung wie gewohnt.

Für PQ NTCP2, das auf einer anderen router-Adresse und einem anderen Port angekündigt wird, ist dies nicht erforderlich.

Für weitere Informationen siehe den Abschnitt "Published Addresses" unten.

Rohinhalte:

```
  +----+----+----+----+----+----+----+----+
  |        MS bit set to 1 and then       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted X         |
  +             (32 bytes)                +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +      (see table below for length)     +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  ~   n = 0                               ~
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaChaPoly frame (options)          |
  +         32 bytes                      +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  ~         padding (optional)            ~
  |     length defined in options block   |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
Unverschlüsselte Daten (Poly1305-Authentifizierungs-Tag nicht angezeigt):

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                   X                   |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM encap_key            |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Hinweis: Das Versionsfeld im Optionsblock von Nachricht 1 muss auf 2 gesetzt werden, auch für PQ-Verbindungen.

Größen:

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Typ</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Typ Code</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">X Länge</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 1 Länge</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 1 Verschl Länge</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 1 Entschl Länge</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">PQ Schlüssel Länge</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">opt Länge</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">4</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">64+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">--</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">880+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">848</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">816</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">800</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">6</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1264+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1232</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1200</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1184</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">7</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1648+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1616</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1584</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1568</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
</table>

Hinweis: Typencodes sind nur für den internen Gebrauch bestimmt. Router bleiben Typ 4, und die Unterstützung wird in den router-Adressen angezeigt.

#### 2) SessionCreated

Roher Inhalt:

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted Y         |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +   Encrypted and authenticated data    +
  -      (see table below for length)     -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (options)          |
  +   Encrypted and authenticated data    +
  -           32 bytes                    -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
Unverschlüsselte Daten (Poly1305 Auth-Tag nicht gezeigt):

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                  Y                    |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Größen:

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Typ</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Typ Code</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Y len</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 2 len</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 2 Enc len</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 2 Dec len</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">PQ CT len</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">opt len</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">4</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">64+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">--</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">848+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">816</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">784</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">768</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">6</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1136+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1104</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1104</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1088</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">7</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1616+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1584</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1584</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1568</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
</table>

Hinweis: Typcodes sind nur für den internen Gebrauch bestimmt. Router bleiben Typ 4, und die Unterstützung wird in den Router-Adressen angezeigt.

#### 3) SessionConfirmed

Unverändert

#### Schlüsselableitungsfunktion (KDF) (für die Datenphase)

Unverändert

#### Veröffentlichte Adressen

In allen Fällen verwenden Sie wie gewohnt den NTCP2-Transportnamen.

Verwende dieselbe Adresse/Port wie non-PQ, non-firewalled. Nur eine PQ-Variante wird unterstützt. In der Router-Adresse veröffentliche v=2 (wie üblich) und den neuen Parameter pq=[3|4|5] um MLKEM 512/768/1024 anzuzeigen. Alice setzt das MSB des ephemeral key (key[31] & 0x80) in der Session-Anfrage, um anzuzeigen, dass dies eine Hybrid-Verbindung ist. Siehe oben. Ältere Router ignorieren den pq-Parameter und verbinden sich non-pq wie üblich.

Unterschiedliche Adresse/Port als Nicht-PQ, oder nur-PQ, nicht-firewalled wird NICHT unterstützt. Dies wird nicht implementiert werden, bis Nicht-PQ NTCP2 deaktiviert wird, was erst in einigen Jahren der Fall sein wird. Wenn Nicht-PQ deaktiviert ist, können mehrere PQ-Varianten unterstützt werden, aber nur eine pro Adresse. Wenn es unterstützt wird, veröffentliche in der router-Adresse v=[3|4|5] um MLKEM 512/768/1024 anzugeben. Alice setzt nicht das MSB des ephemeral key. Ältere router werden den v-Parameter prüfen und diese Adresse als nicht unterstützt überspringen.

Firewall-geschützte Adressen (keine IP veröffentlicht): In der router-Adresse v=2 veröffentlichen (wie gewöhnlich). Es ist nicht erforderlich, einen pq-Parameter zu veröffentlichen.

Alice kann sich mit einem PQ Bob über die PQ-Variante verbinden, die Bob veröffentlicht, unabhängig davon, ob Alice pq-Unterstützung in ihren router-Informationen bewirbt oder ob sie dieselbe Variante bewirbt.

#### Maximale Polsterung

In der aktuellen Spezifikation sind die Nachrichten 1 und 2 definiert, um eine "angemessene" Menge an Padding zu haben, mit einem empfohlenen Bereich von 0-31 Bytes und ohne spezifiziertes Maximum.

Bis API 0.9.68 (Release 2.11.0) implementierte Java I2P maximal 256 Bytes Padding für Nicht-PQ-Verbindungen, dies war jedoch zuvor nicht dokumentiert. Ab API 0.9.69 (Release 2.12.0) implementiert Java I2P das gleiche maximale Padding für Nicht-PQ-Verbindungen wie für MLKEM-512. Siehe Tabelle unten.

Verwende die definierte Nachrichtengröße als maximales Padding, das heißt, das maximale Padding wird die Nachrichtengröße für PQ-Verbindungen verdoppeln, wie folgt:

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Nachrichten Max Padding</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">non-PQ (bis 0.9.68)</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">non-PQ (ab 0.9.69)</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">MLKEM-512</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">MLKEM-768</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">MLKEM-1024</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">Session Request</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">256</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">880</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">880</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1264</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1648</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">Session Created</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">256</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">848</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">848</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1136</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1616</td>
</tr>
</table>

## Overhead-Analyse

### Schlüsselaustausch

Größenzunahme (Bytes):

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Typ</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Pubkey (Msg 1)</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Chiffretext (Msg 2)</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+816</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+784</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+1200</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+1104</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+1584</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+1584</td>
</tr>
</table>

## Sicherheitsanalyse

NIST-Sicherheitskategorien sind in der [NIST-Präsentation](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) auf Folie 10 zusammengefasst. Vorläufige Kriterien: Unsere minimale NIST-Sicherheitskategorie sollte 2 für hybride Protokolle und 3 für reine PQ-Protokolle sein.

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Kategorie</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">So sicher wie</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">1</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">AES128</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">2</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">SHA256</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">3</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">AES192</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">4</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">SHA384</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">AES256</td>
</tr>
</table>

### Handshakes

Dies sind alles Hybrid-Protokolle. Implementierungen sollten MLKEM768 bevorzugen; MLKEM512 ist nicht sicher genug.

NIST-Sicherheitskategorien [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf):

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Algorithmus</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Sicherheitskategorie</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">3</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
</tr>
</table>

## Implementierungshinweise

### Bibliotheksunterstützung

Bouncycastle, BoringSSL und WolfSSL Bibliotheken unterstützen jetzt MLKEM und MLDSA. OpenSSL Unterstützung wird in ihrer 3.5 Version am 8. April 2025 verfügbar sein [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

### Identifikation des eingehenden Datenverkehrs

Wir setzen das MSB des ephemeren Schlüssels (key[31] & 0x80) in der Session-Anfrage, um anzuzeigen, dass dies eine Hybrid-Verbindung ist. Dies ermöglicht es uns, sowohl Standard-NTCP als auch Hybrid-NTCP auf demselben Port zu betreiben. Nur eine Hybrid-Variante wird für eingehende Verbindungen unterstützt und in der Router-Adresse angekündigt. Zum Beispiel pq=3 oder pq=4.

#### Verschleierung

Als Alice, für eine PQ-Verbindung, vor der Verschleierung, setze X[31] |= 0x80. Dies macht X zu einem ungültigen X25519 öffentlichen Schlüssel. Nach der Verschleierung wird AES-CBC ihn randomisieren. Das MSB von X wird nach der Verschleierung zufällig sein.

Als Bob testen, ob (X[31] & 0x80) != 0 nach der Entschleierung. Wenn ja, ist es eine PQ-Verbindung.

Die mindestens erforderliche Router-Version für NTCP2-PQ ist noch zu bestimmen.

Hinweis: Typ-Codes sind nur für den internen Gebrauch bestimmt. Router bleiben Typ 4, und die Unterstützung wird in den Router-Adressen angezeigt.

## Router-Kompatibilität

### Transport-Namen

Verwenden Sie in allen Fällen den NTCP2-Transportnamen wie gewohnt. Ältere Router werden den pq-Parameter ignorieren und sich wie gewohnt mit Standard-NTCP2 verbinden.

## Referenzen

* [CABFORUM](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/)
* [Choosing-Hash](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3)
* [CLOUDFLARE](https://blog.cloudflare.com/pq-2024/)
* [COMMON](/docs/specs/common-structures/)
* [COMPOSITE-SIGS](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)
* [ECIES](/docs/specs/ecies/)
* [FORUM](http://zzz.i2p/topics/3294)
* [FIPS202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
* [FIPS203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
* [FIPS204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
* [FIPS205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf)
* [MLDSA-OIDS](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/)
* [NIST-PQ](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)
* [NIST-PQ-UPDATE](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf)
* [NIST-PQ-END](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf)
* [NIST-VECTORS](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values)
* [Noise](https://noiseprotocol.org/noise.html)
* [Noise-Hybrid](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf)
* [NSA-PQ](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF)
* [NTCP2](/docs/specs/ntcp2/)
* [OPENSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/)
* [Prop165](/docs/proposals/165/)
* [PQ-WIREGUARD](https://eprint.iacr.org/2020/379.pdf)
* [RFC-2104](https://tools.ietf.org/html/rfc2104)
* [Rosenpass](https://rosenpass.eu/)
* [Rosenpass-Whitepaper](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf)
* [SSH-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/)
* [SSU2](/docs/specs/ssu2/)
* [TLS-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/)
