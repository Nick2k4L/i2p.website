---
title: "ECIES-X25519 Router Nachrichten"
description: "Spezifikation für Garlic-Nachrichtenverschlüsselung an ECIES-Router mit X25519"
slug: "ecies-routers"
category: "Protokolle"
lastUpdated: "2025-03"
accurateFor: "0.9.65"
---

## Hinweis

Unterstützt seit Version 0.9.49. Netzwerk-Deployment und Tests laufen. Kleinere Änderungen vorbehalten. Siehe [Vorschlag 156](/proposals/156-ecies-routers).

## Übersicht

Dieses Dokument spezifiziert garlic encryption für Nachrichten an ECIES router, unter Verwendung kryptographischer Primitive, die von [ECIES-X25519](/docs/specs/ecies) eingeführt wurden. Es ist ein Teil des gesamten [Vorschlags 156](/proposals/156-ecies-routers) zur Umstellung von routern von ElGamal- auf ECIES-X25519-Schlüssel. Diese Spezifikation ist ab Release 0.9.49 implementiert.

Für einen Überblick über alle erforderlichen Änderungen für ECIES router, siehe [Vorschlag 156](/proposals/156-ecies-routers). Für Garlic Messages an ECIES-X25519 Ziele, siehe [ECIES-X25519](/docs/specs/ecies).

### Kryptografische Grundelemente

Die zur Implementierung dieser Spezifikation erforderlichen Primitive sind:

- AES-256-CBC wie in [Cryptography](/docs/specs/cryptography)
- STREAM ChaCha20/Poly1305-Funktionen: ENCRYPT(k, n, plaintext, ad) und DECRYPT(k, n, ciphertext, ad) - wie in [NTCP2](/docs/specs/ntcp2), [ECIES-X25519](/docs/specs/ecies), und [RFC-7539](https://tools.ietf.org/html/rfc7539)
- X25519 DH-Funktionen - wie in [NTCP2](/docs/specs/ntcp2) und [ECIES-X25519](/docs/specs/ecies)
- HKDF(salt, ikm, info, n) - wie in [NTCP2](/docs/specs/ntcp2) und [ECIES-X25519](/docs/specs/ecies)

Andere Noise-Funktionen, die an anderer Stelle definiert sind:

- MixHash(d) - wie in [NTCP2](/docs/specs/ntcp2) und [ECIES-X25519](/docs/specs/ecies)
- MixKey(d) - wie in [NTCP2](/docs/specs/ntcp2) und [ECIES-X25519](/docs/specs/ecies)

## Design

Der ECIES Router SKM benötigt kein vollständiges Ratchet SKM, wie es in [ECIES](/docs/specs/ecies) für Destinations spezifiziert ist. Es gibt keine Anforderung für nicht-anonyme Nachrichten unter Verwendung des IK-Musters. Das Bedrohungsmodell erfordert keine Elligator2-kodierten ephemeren Schlüssel.

Daher wird der router SKM das Noise "N" Pattern verwenden, wie es in [Prop152](/proposals/152-ecies-tunnels) für tunnel building spezifiziert ist. Es wird das gleiche Payload-Format verwenden, wie es in [ECIES](/docs/specs/ecies) für Destinations spezifiziert ist. Der Zero-Static-Key-Modus (keine Bindung oder Session) von IK, der in [ECIES](/docs/specs/ecies) spezifiziert ist, wird nicht verwendet.

Antworten auf Lookups werden mit einem Ratchet-Tag verschlüsselt, falls dies im Lookup angefordert wurde. Dies ist wie in [Prop154](/proposals/154-ecies-lookups) dokumentiert und nun in [I2NP](/docs/specs/i2np) spezifiziert.

Das Design ermöglicht es dem Router, einen einzigen ECIES Session Key Manager zu haben. Es ist nicht notwendig, "dual key" Session Key Manager zu betreiben, wie in [ECIES](/docs/specs/ecies) für Destinations beschrieben. Router haben nur einen öffentlichen Schlüssel.

Ein ECIES router hat keinen statischen ElGamal-Schlüssel. Der router benötigt dennoch eine ElGamal-Implementierung, um tunnel durch ElGamal router zu erstellen und verschlüsselte Nachrichten an ElGamal router zu senden.

Ein ECIES router KANN einen partiellen ElGamal Session Key Manager benötigen, um ElGamal-getaggte Nachrichten zu empfangen, die als Antworten auf NetDB-Lookups von floodfill routern vor Version 0.9.46 empfangen werden, da diese router keine Implementierung von ECIES-getaggten Antworten haben, wie sie in [Prop152](/proposals/152-ecies-tunnels) spezifiziert sind. Falls nicht, darf ein ECIES router möglicherweise keine verschlüsselte Antwort von einem floodfill router vor Version 0.9.46 anfordern.

Dies ist optional. Die Entscheidung kann in verschiedenen I2P-Implementierungen variieren und hängt möglicherweise davon ab, wie viel des Netzwerks auf 0.9.46 oder höher aktualisiert wurde. Zum jetzigen Zeitpunkt sind etwa 85% des Netzwerks auf 0.9.46 oder höher.

### Noise Protocol Framework

Diese Spezifikation stellt die Anforderungen basierend auf dem [Noise Protocol Framework](https://noiseprotocol.org/noise.html) (Revision 34, 2018-07-11) bereit. In der Noise-Terminologie ist Alice die Initiatorin und Bob der Responder.

Es basiert auf dem Noise-Protokoll Noise_N_25519_ChaChaPoly_SHA256. Dieses Noise-Protokoll verwendet die folgenden Grundbausteine:

- **Einseitiges Handshake-Muster: N** - Alice überträgt ihren statischen Schlüssel nicht an Bob (N)
- **DH-Funktion: X25519** - X25519 DH mit einer Schlüssellänge von 32 Bytes wie in [RFC-7748](https://tools.ietf.org/html/rfc7748) spezifiziert.
- **Verschlüsselungsfunktion: ChaChaPoly** - AEAD_CHACHA20_POLY1305 wie in [RFC-7539](https://tools.ietf.org/html/rfc7539) Abschnitt 2.8 spezifiziert. 12-Byte-Nonce, wobei die ersten 4 Bytes auf null gesetzt sind. Identisch mit dem in [NTCP2](/docs/specs/ntcp2).
- **Hash-Funktion: SHA256** - Standard-32-Byte-Hash, bereits umfassend in I2P verwendet.

### Handshake-Muster

Handshakes verwenden [Noise](https://noiseprotocol.org/noise.html) Handshake-Muster.

Die folgende Buchstabenzuordnung wird verwendet:

- e = einmaliger ephemerer Schlüssel
- s = statischer Schlüssel
- p = Nachrichten-Payload

Die Build-Anfrage ist identisch mit dem Noise N-Muster. Dies ist auch identisch mit der ersten (Session Request) Nachricht im XK-Muster, das in [NTCP2](/docs/specs/ntcp2) verwendet wird.

```
<- s
  ...
  e es p ->
```
### Nachrichtenverschlüsselung

Nachrichten werden erstellt und asymmetrisch zum Ziel-router verschlüsselt. Diese asymmetrische Verschlüsselung von Nachrichten ist derzeit ElGamal, wie in [Cryptography](/docs/specs/cryptography) definiert, und enthält eine SHA-256-Prüfsumme. Dieses Design bietet keine Forward Secrecy.

Das ECIES-Design verwendet das unidirektionale Noise-Muster "N" mit ECIES-X25519 ephemeral-static DH, mit einem HKDF und ChaCha20/Poly1305 AEAD für Forward Secrecy, Integrität und Authentifizierung. Alice ist die anonyme Nachrichtenabsenderin, ein router oder eine Destination. Der Ziel-ECIES-router ist Bob.

### Antwort-Verschlüsselung

Antworten sind nicht Teil dieses Protokolls, da Alice anonym ist. Die Antwortschlüssel, falls vorhanden, sind in der Anfragenachricht gebündelt. Siehe die [I2NP-Spezifikation](/docs/specs/i2np) für Database Lookup Messages.

Antworten auf Database Lookup Nachrichten sind Database Store oder Database Search Reply Nachrichten. Sie werden als Existing Session Nachrichten mit dem 32-Byte Reply-Schlüssel und 8-Byte Reply-Tag verschlüsselt, wie in [I2NP](/docs/specs/i2np) und [Prop154](/proposals/154-ecies-lookups) spezifiziert.

Es gibt keine expliziten Antworten auf Database Store-Nachrichten. Der Absender kann seine eigene Antwort als Garlic Message an sich selbst bündeln, die eine Delivery Status-Nachricht enthält.

## Spezifikation

X25519: Siehe [ECIES](/docs/specs/ecies).

Router-Identität und Schlüsselzertifikat: Siehe [Gemeinsame Strukturen](/docs/specs/common-structures).

### Anfragenverschlüsselung

Die Anfragenverschlüsselung ist dieselbe wie in [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) und [Prop152](/proposals/152-ecies-tunnels) spezifiziert, unter Verwendung des Noise "N" Musters.

Antworten auf Lookups werden mit einem Ratchet-Tag verschlüsselt, falls dies im Lookup angefordert wurde. Database Lookup-Anfragenachrichten enthalten den 32-Byte-Antwortschlüssel und das 8-Byte-Antwort-Tag wie in [I2NP](/docs/specs/i2np) und [Prop154](/proposals/154-ecies-lookups) spezifiziert. Der Schlüssel und das Tag werden verwendet, um die Antwort zu verschlüsseln.

Tag-Sets werden nicht erstellt. Das Zero-Static-Key-Schema, das in ECIES-X25519-AEAD-Ratchet [Prop144](/proposals/144-ecies-x25519-aead-ratchet) und [ECIES](/docs/specs/ecies) spezifiziert ist, wird nicht verwendet. Ephemerale Schlüssel werden nicht mit Elligator2 kodiert.

Im Allgemeinen handelt es sich dabei um New Session-Nachrichten, die mit einem Null-Static-Key (keine Bindung oder Session) gesendet werden, da der Absender der Nachricht anonym ist.

#### KDF für anfängliches ck und h

Dies ist das Standard-[Noise](https://noiseprotocol.org/noise.html) für Muster "N" mit einem Standard-Protokollnamen. Dies ist dasselbe wie in [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) und [Prop152](/proposals/152-ecies-tunnels) für tunnel Build-Nachrichten spezifiziert.

```
This is the "e" message pattern:

  // Define protocol_name.
  Set protocol_name = "Noise_N_25519_ChaChaPoly_SHA256"
  (31 bytes, US-ASCII encoded, no NULL termination).

  // Define Hash h = 32 bytes
  // Pad to 32 bytes. Do NOT hash it, because it is not more than 32 bytes.
  h = protocol_name || 0

  Define ck = 32 byte chaining key. Copy the h data to ck.
  Set chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // up until here, can all be precalculated by all routers.
```
#### KDF für Nachricht

Nachrichtenersteller generieren ein ephemeres X25519-Schlüsselpaar für jede Nachricht. Ephemere Schlüssel müssen für jede Nachricht eindeutig sein. Dies entspricht den Spezifikationen in [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) und [Prop152](/proposals/152-ecies-tunnels) für Tunnel-Build-Nachrichten.

```
  // Target router's X25519 static keypair (hesk, hepk) from the Router Identity
  hesk = GENERATE_PRIVATE()
  hepk = DERIVE_PUBLIC(hesk)

  // MixHash(hepk)
  // || below means append
  h = SHA256(h || hepk);

  // up until here, can all be precalculated by each router
  // for all incoming messages

  // Sender generates an X25519 ephemeral keypair
  sesk = GENERATE_PRIVATE()
  sepk = DERIVE_PUBLIC(sesk)

  // MixHash(sepk)
  h = SHA256(h || sepk);

  End of "e" message pattern.

  This is the "es" message pattern:

  // Noise es
  // Sender performs an X25519 DH with receiver's static public key.
  // The target router
  // extracts the sender's ephemeral key preceding the encrypted record.
  sharedSecret = DH(sesk, hepk) = DH(hesk, sepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // ChaChaPoly parameters to encrypt/decrypt
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  // Chain key is not used
  //chainKey = keydata[0:31]

  // AEAD parameters
  k = keydata[32:63]
  n = 0
  plaintext = 464 byte build request record
  ad = h
  ciphertext = ENCRYPT(k, n, plaintext, ad)

  End of "es" message pattern.

  // MixHash(ciphertext) is not required
  //h = SHA256(h || ciphertext)
```
#### Nutzlast

Die Payload verwendet das gleiche Blockformat wie in [ECIES](/docs/specs/ecies) und [Prop144](/proposals/144-ecies-x25519-aead-ratchet) definiert. Alle Nachrichten müssen einen DateTime-Block zur Verhinderung von Replay-Angriffen enthalten.

## Implementierungshinweise

- Ältere Router überprüfen nicht den Verschlüsselungstyp des Routers und senden ElGamal-verschlüsselte Nachrichten. Einige neuere Router sind fehlerhaft und senden verschiedene Arten von fehlerhaften Nachrichten. Implementierer sollten diese Datensätze vor der DH-Operation erkennen und ablehnen, wenn möglich, um die CPU-Nutzung zu reduzieren.

## Referenzen

- [Gemeinsame Strukturen](/docs/specs/common-structures)
- [Kryptographie](/docs/specs/cryptography)
- [ECIES](/docs/specs/ecies)
- [I2NP](/docs/specs/i2np)
- [Noise Protocol Framework](https://noiseprotocol.org/noise.html)
- [NTCP2](/docs/specs/ntcp2)
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet)
- [Prop152](/proposals/152-ecies-tunnels)
- [Prop154](/proposals/154-ecies-lookups)
- [Prop156](/proposals/156-ecies-routers)
- [RFC-7539](https://tools.ietf.org/html/rfc7539)
- [RFC-7748](https://tools.ietf.org/html/rfc7748)
- [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies)
