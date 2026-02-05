---
title: "Verschlüsselte LeaseSet-Spezifikation"
description: "Blinding, Verschlüsselung und Entschlüsselung von verschlüsselten leaseSets"
slug: "encryptedleaseset"
category: "Protokolle"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Übersicht

Dieses Dokument spezifiziert das Blinding, die Verschlüsselung und die Entschlüsselung von verschlüsselten leaseSets. Für die Struktur des verschlüsselten leaseSet siehe die [Common Structures Spezifikation](/docs/specs/common-structures). Für Hintergrundinformationen zu verschlüsselten leaseSets siehe [Proposal 123](/proposals/123-new-netdb-entries). Für die Verwendung in der netDb siehe die netdb-Dokumentation.

### Definitionen

Wir definieren die folgenden Funktionen, die den kryptographischen Bausteinen entsprechen, die für verschlüsselte LS2 verwendet werden:

**CSRNG(n)** : n-Byte-Ausgabe von einem kryptographisch sicheren Zufallszahlengenerator.

Zusätzlich zu der Anforderung, dass CSRNG kryptographisch sicher sein muss (und somit für die Generierung von Schlüsselmaterial geeignet ist), MUSS es sicher sein, dass eine n-Byte-Ausgabe für Schlüsselmaterial verwendet werden kann, wenn die Byte-Sequenzen unmittelbar davor und danach im Netzwerk preisgegeben werden (wie z.B. in einem Salt oder verschlüsseltem Padding). Implementierungen, die auf eine möglicherweise nicht vertrauenswürdige Quelle angewiesen sind, sollten jede Ausgabe, die im Netzwerk preisgegeben werden soll, hashen [PRNG-REFS](http://projectbullrun.org/dual-ec/ext-rand.html).

**H(p, d)**: SHA-256 Hash-Funktion, die eine Personalisierungszeichenkette p und Daten d entgegennimmt und eine Ausgabe von 32 Bytes Länge erzeugt.

Verwende SHA-256 wie folgt:

```
H(p, d) := SHA-256(p || d)
```
**STREAM** : Die ChaCha20-Stromchiffre wie in [RFC-7539-S2.4](https://tools.ietf.org/html/rfc7539#section-2.4) spezifiziert, mit dem anfänglichen Zähler auf 1 gesetzt. S_KEY_LEN = 32 und S_IV_LEN = 12.

- **ENCRYPT(k, iv, plaintext)** : Verschlüsselt plaintext mit dem Chiffrierschlüssel k und der Nonce iv, die für den Schlüssel k eindeutig sein MUSS. Gibt einen Chiffretext zurück, der die gleiche Größe wie der plaintext hat. Der gesamte Chiffretext muss von Zufallsdaten nicht zu unterscheiden sein, wenn der Schlüssel geheim ist.

- **DECRYPT(k, iv, ciphertext)** : Entschlüsselt den Chiffretext unter Verwendung des Chiffrierschlüssels k und der Nonce iv. Gibt den Klartext zurück.

**SIG** : Das Red25519-Signaturschema (entsprechend SigType 11) mit key blinding. Es hat die folgenden Funktionen:

- **DERIVE_PUBLIC(privkey)** : Gibt den öffentlichen Schlüssel zurück, der dem gegebenen privaten Schlüssel entspricht.

- **SIGN(privkey, m)** : Gibt eine Signatur mit dem privaten Schlüssel privkey über die gegebene Nachricht m zurück.

- **VERIFY(pubkey, m, sig)** : Verifiziert die Signatur sig gegen den öffentlichen Schlüssel pubkey und die Nachricht m. Gibt true zurück, wenn die Signatur gültig ist, andernfalls false.

Es muss auch die folgenden Key-Blinding-Operationen unterstützen:

- **GENERATE_ALPHA(data, secret)** : Generiert alpha für diejenigen, die die Daten und ein optionales Geheimnis kennen. Das Ergebnis muss identisch verteilt sein wie die privaten Schlüssel.

- **BLIND_PRIVKEY(privkey, alpha)** : Blendet einen privaten Schlüssel unter Verwendung eines geheimen Alpha.

- **BLIND_PUBKEY(pubkey, alpha)** : Blendet einen öffentlichen Schlüssel mit einem geheimen Alpha. Für ein gegebenes Schlüsselpaar (privkey, pubkey) gilt folgende Beziehung:

```
BLIND_PUBKEY(pubkey, alpha) ==
DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))
```
**DH** : X25519 Public-Key-Vereinbarungssystem. Private Schlüssel von 32 Bytes, öffentliche Schlüssel von 32 Bytes, erzeugt Ausgaben von 32 Bytes. Es hat die folgenden Funktionen:

- **GENERATE_PRIVATE()** : Generiert einen neuen privaten Schlüssel.

- **DERIVE_PUBLIC(privkey)** : Gibt den öffentlichen Schlüssel zurück, der dem gegebenen privaten Schlüssel entspricht.

- **DH(privkey, pubkey)** : Erzeugt ein gemeinsames Geheimnis aus den gegebenen privaten und öffentlichen Schlüsseln.

**HKDF(salt, ikm, info, n)** : Eine kryptographische Schlüsselableitungsfunktion, die etwas Eingabeschlüsselmaterial ikm (welches gute Entropie haben sollte, aber nicht zwingend eine gleichmäßig zufällige Zeichenkette sein muss), ein Salt der Länge 32 Bytes und einen kontextspezifischen 'info'-Wert nimmt und eine Ausgabe von n Bytes erzeugt, die zur Verwendung als Schlüsselmaterial geeignet ist.

Verwenden Sie HKDF wie in [RFC-5869](https://tools.ietf.org/html/rfc5869) spezifiziert, unter Verwendung der HMAC-Hash-Funktion SHA-256 wie in [RFC-2104](https://tools.ietf.org/html/rfc2104) spezifiziert. Das bedeutet, dass SALT_LEN maximal 32 Bytes beträgt.

### Format

Das verschlüsselte LS2-Format besteht aus drei verschachtelten Ebenen:

- Eine äußere Schicht, die die notwendigen Klartextinformationen für Speicherung und Abruf enthält.
- Eine mittlere Schicht, die die Client-Authentifizierung verwaltet.
- Eine innere Schicht, die die eigentlichen LS2-Daten enthält.

Das Gesamtformat sieht folgendermaßen aus:

```
Layer 0 data + Enc(layer 1 data + Enc(layer 2 data)) + Signature
```
Beachte, dass verschlüsselte LS2 verblendet sind. Das Ziel ist nicht im Header enthalten. Der DHT-Speicherort ist SHA-256(sig type || verblendeter öffentlicher Schlüssel) und wird täglich rotiert.

Verwendet NICHT den oben spezifizierten Standard-LS2-Header.

#### Schicht 0 (äußere)

**Typ** : 1 Byte

Nicht tatsächlich im Header, sondern Teil der von der Signatur abgedeckten Daten. Aus dem Feld in der Database Store Message entnehmen.

**Blinded Public Key Sig Type** : 2 Bytes, Big Endian

Dies wird immer Typ 11 sein und identifiziert einen Red25519 blinded key.

**Blinded Public Key** : Länge wie durch Signaturtyp impliziert

**Veröffentlichungszeitstempel** : 4 Bytes, Big Endian

Sekunden seit der Epoche, läuft 2106 über

**Expires** : 2 Bytes, Big Endian

Abweichung vom veröffentlichten Zeitstempel in Sekunden, maximal 18,2 Stunden

**Flags** : 2 Bytes

Bit-Reihenfolge: 15 14 ... 3 2 1 0

- Bit 0: Wenn 0, keine Offline-Schlüssel; wenn 1, Offline-Schlüssel
- Andere Bits: auf 0 setzen für Kompatibilität mit zukünftigen Verwendungen

**Transiente Schlüsseldaten** : Vorhanden, wenn Flag Offline-Schlüssel anzeigt

- **Expires timestamp** : 4 Bytes, Big Endian. Sekunden seit Epoch, läuft 2106 über
- **Transient sig type** : 2 Bytes, Big Endian
- **Transient signing public key** : Länge wie durch sig type impliziert
- **Signature** : Länge wie durch blinded public key sig type impliziert. Über expires timestamp, transient sig type und transient public key. Verifiziert mit dem blinded public key.

**lenOuterCiphertext** : 2 Bytes, Big Endian

**outerCiphertext** : lenOuterCiphertext Bytes

Verschlüsselte Layer-1-Daten. Siehe unten für Schlüsselableitung und Verschlüsselungsalgorithmen.

**Signature** : Länge wie durch den Signaturtyp des verwendeten Signaturschlüssels impliziert

Die Signatur umfasst alles oben Stehende. Wenn das Flag Offline-Schlüssel anzeigt, wird die Signatur mit dem temporären öffentlichen Schlüssel verifiziert. Andernfalls wird die Signatur mit dem verblendeten öffentlichen Schlüssel verifiziert.

#### Schicht 1 (mittlere)

**Flags** : 1 Byte

Bit-Reihenfolge: 76543210

- Bit 0: 0 für alle, 1 für pro-Client, Authentifizierungsbereich folgt
- Bits 3-1: Authentifizierungsschema, nur wenn Bit 0 auf 1 für pro-Client gesetzt ist, andernfalls 000
  - 000: DH-Client-Authentifizierung (oder keine pro-Client-Authentifizierung)
  - 001: PSK-Client-Authentifizierung
- Bits 7-4: Unbenutzt, auf 0 setzen für zukünftige Kompatibilität

**DH Client-Auth-Daten** : Vorhanden, wenn Flag-Bit 0 auf 1 gesetzt ist und Flag-Bits 3-1 auf 000 gesetzt sind.

- **ephemeralPublicKey** : 32 Bytes
- **clients** : 2 Bytes, Big Endian. Anzahl der nachfolgenden authClient-Einträge, jeweils 40 Bytes
- **authClient** : Autorisierungsdaten für einen einzelnen Client. Siehe unten für den clientspezifischen Autorisierungsalgorithmus.
  - **clientID_i** : 8 Bytes
  - **clientCookie_i** : 32 Bytes

**PSK Client-Authentifizierungsdaten** : Vorhanden wenn Flag-Bit 0 auf 1 gesetzt ist und Flag-Bits 3-1 auf 001 gesetzt sind.

- **authSalt** : 32 Bytes
- **clients** : 2 Bytes, Big Endian. Anzahl der folgenden authClient-Einträge, je 40 Bytes
- **authClient** : Autorisierungsdaten für einen einzelnen Client. Siehe unten für den clientspezifischen Autorisierungsalgorithmus.
  - **clientID_i** : 8 Bytes
  - **clientCookie_i** : 32 Bytes

**innerCiphertext** : Länge impliziert durch lenOuterCiphertext (alle verbleibenden Daten)

Verschlüsselte Layer-2-Daten. Siehe unten für Schlüsselableitung und Verschlüsselungsalgorithmen.

#### Schicht 2 (innen)

**Typ** : 1 Byte

Entweder 3 (LS2) oder 7 (Meta LS2)

**Daten** : LeaseSet2-Daten für den angegebenen Typ.

Enthält den Header und die Signatur.

### Blinding Key Ableitung

Wir verwenden das folgende Schema für Key Blinding, basierend auf Ed25519 und ZCash RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf). Die Red25519-Signaturen verwenden die Ed25519-Kurve mit SHA-512 für den Hash.

Wir verwenden nicht Tors rend-spec-v3.txt Anhang A.2 [TOR-REND-SPEC-V3](https://spec.torproject.org/rend-spec-v3), das ähnliche Designziele hat, da seine verblindeten öffentlichen Schlüssel möglicherweise außerhalb der Primordnungsuntergruppe liegen, mit unbekannten Sicherheitsauswirkungen.

#### Ziele

- Der öffentliche Signaturschlüssel im ungeblindeten Ziel muss Ed25519 (sig type 7) oder Red25519 (sig type 11) sein; keine anderen sig types werden unterstützt
- Wenn der öffentliche Signaturschlüssel offline ist, muss der transiente öffentliche Signaturschlüssel ebenfalls Ed25519 sein
- Blinding ist rechnerisch einfach
- Verwendung bestehender kryptographischer Primitive
- Geblindete öffentliche Schlüssel können nicht entblindet werden
- Geblindete öffentliche Schlüssel müssen auf der Ed25519-Kurve und der prime-order Untergruppe liegen
- Der öffentliche Signaturschlüssel des Ziels muss bekannt sein (vollständiges Ziel nicht erforderlich), um den geblindeten öffentlichen Schlüssel abzuleiten
- Optional kann ein zusätzliches Geheimnis erforderlich sein, um den geblindeten öffentlichen Schlüssel abzuleiten

#### Sicherheit

Die Sicherheit eines Blinding-Schemas erfordert, dass die Verteilung von Alpha dieselbe ist wie die der ungeblindeten privaten Schlüssel. Wenn wir jedoch einen Ed25519 privaten Schlüssel (sig type 7) zu einem Red25519 privaten Schlüssel (sig type 11) blinden, ist die Verteilung unterschiedlich. Um die Anforderungen von zcash Abschnitt 4.1.6.1 [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) zu erfüllen, sollte Red25519 (sig type 11) auch für die ungeblindeten Schlüssel verwendet werden, damit "die Kombination aus einem re-randomisierten öffentlichen Schlüssel und Signatur(en) unter diesem Schlüssel nicht den Schlüssel preisgeben, von dem aus er re-randomisiert wurde." Wir erlauben Typ 7 für bestehende Ziele, empfehlen aber Typ 11 für neue Ziele, die verschlüsselt werden sollen.

#### Definitionen

**B** : Der Ed25519 Basispunkt (Generator) 2^255 - 19 wie in [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)

**L** : Die Ed25519-Ordnung 2^252 + 27742317777372353535851937790883648493 wie in [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)

**DERIVE_PUBLIC(a)** : Konvertiert einen privaten Schlüssel zu einem öffentlichen, wie in Ed25519 (Multiplikation mit G)

**alpha** : Eine 32-Byte-Zufallszahl, die denjenigen bekannt ist, die das Ziel kennen.

**GENERATE_ALPHA(destination, date, secret)** : Generiert alpha für das aktuelle Datum, für diejenigen, die das Ziel und das Geheimnis kennen. Das Ergebnis muss identisch verteilt sein wie Ed25519 private keys.

**a** : Der nicht verblindete 32-Byte EdDSA- oder RedDSA-Signatur-Private-Key, der zum Signieren des Ziels verwendet wird

**A** : Der ungeblendete 32-Byte EdDSA oder RedDSA Signatur-Public-Key im Ziel, = DERIVE_PUBLIC(a), wie in Ed25519

**a'** : Der geblendete 32-Byte EdDSA-Signatur-Private-Key, der zum Signieren des verschlüsselten leaseSet verwendet wird. Dies ist ein gültiger EdDSA-Private-Key.

**A'** : Der geblendete 32-Byte EdDSA-Signatur-öffentliche Schlüssel im Destination, kann mit DERIVE_PUBLIC(a') generiert werden, oder aus A und alpha. Dies ist ein gültiger EdDSA-öffentlicher Schlüssel, auf der Kurve und in der Untergruppe primärer Ordnung.

**LEOS2IP(x)** : Die Reihenfolge der Eingabebytes zu Little-Endian umkehren

**H\*(x)** : 32 Bytes = (LEOS2IP(SHA512(x))) mod B, gleich wie bei Ed25519 Hash-and-Reduce

#### Blinding-Berechnungen

Ein neuer geheimer Alpha- und Blinded-Schlüssel muss jeden Tag (UTC) generiert werden.

Das geheime Alpha und die geblendeten Schlüssel werden wie folgt berechnet:

GENERATE_ALPHA(destination, date, secret), für alle Parteien:

```
// secret is optional, else zero-length
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of blinded public key A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
datestring = 8 bytes ASCII YYYYMMDD from the current date UTC
secret = UTF-8 encoded string
seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || secret, "i2pblinding1", 64)
// treat seed as a 64 byte little-endian value
alpha = seed mod L
```
BLIND_PRIVKEY(), für den Besitzer, der das leaseSet veröffentlicht:

```
alpha = GENERATE_ALPHA(destination, date, secret)
// If for a Ed25519 private key (type 7)
seed = destination's signing private key
a = left half of SHA512(seed) and clamped as usual for Ed25519
// else for a Red25519 private key (type 11)
a = destination's signing private key
// Addition using scalar arithmetic
blinded signing private key = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
blinded signing public key = A' = DERIVE_PUBLIC(a')
```
BLIND_PUBKEY(), für die Clients, die das leaseSet abrufen:

```
alpha = GENERATE_ALPHA(destination, date, secret)
A = destination's signing public key
// Addition using group elements (points on the curve)
blinded public key = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```
Beide Methoden zur Berechnung von A' ergeben das gleiche Ergebnis, wie erforderlich.

#### Signierung

Das unblinded leaseSet wird mit dem unblinded Ed25519 oder Red25519 Signing-Private-Key signiert und wie üblich mit dem unblinded Ed25519 oder Red25519 Signing-Public-Key (sig types 7 oder 11) verifiziert.

Wenn der öffentliche Signaturschlüssel offline ist, wird das unblinded leaseset vom unblinded transient Ed25519 oder Red25519 privaten Signaturschlüssel signiert und mit dem unblinded Ed25519 oder Red25519 transient öffentlichen Signaturschlüssel (Signaturtypen 7 oder 11) wie üblich verifiziert. Siehe unten für zusätzliche Hinweise zu Offline-Schlüsseln für verschlüsselte leasesets.

Für die Signierung des verschlüsselten leaseset verwenden wir Red25519 basierend auf RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf), um mit geblendeten Schlüsseln zu signieren und zu verifizieren. Die Red25519-Signaturen basieren auf der Ed25519-Kurve und verwenden SHA-512 für den Hash.

Red25519 ist ähnlich dem Standard Ed25519, außer in den unten spezifizierten Punkten.

#### Signatur/Verifizierungs-Berechnungen

Der äußere Teil des verschlüsselten leaseSet verwendet Red25519-Schlüssel und -Signaturen.

Red25519 ist ähnlich zu Ed25519. Es gibt zwei Unterschiede:

Red25519 private keys werden aus Zufallszahlen generiert und müssen dann mod L reduziert werden, wobei L oben definiert ist. Ed25519 private keys werden aus Zufallszahlen generiert und dann mittels bitweiser Maskierung auf die Bytes 0 und 31 "geklammert". Dies wird bei Red25519 nicht durchgeführt. Die oben definierten Funktionen GENERATE_ALPHA() und BLIND_PRIVKEY() generieren ordnungsgemäße Red25519 private keys unter Verwendung von mod L.

In Red25519 verwendet die Berechnung von r für die Signierung zusätzliche Zufallsdaten und nutzt den öffentlichen Schlüsselwert anstelle des Hashes des privaten Schlüssels. Aufgrund der Zufallsdaten ist jede Red25519-Signatur unterschiedlich, selbst beim Signieren derselben Daten mit demselben Schlüssel.

```
Signing:
  T = 80 random bytes
  r = H*(T || publickey || message)
  (rest is the same as in Ed25519)

Verification:
  Same as for Ed25519
```
### Verschlüsselung und Verarbeitung

#### Ableitung von Subzertifikaten

Als Teil des Blinding-Prozesses müssen wir sicherstellen, dass ein verschlüsseltes LS2 nur von jemandem entschlüsselt werden kann, der den entsprechenden öffentlichen Signaturschlüssel der Destination kennt. Die vollständige Destination ist nicht erforderlich. Um dies zu erreichen, leiten wir eine Berechtigung vom öffentlichen Signaturschlüssel ab:

```
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
credential = H("credential", keydata)
```
Der Personalisierungsstring stellt sicher, dass die Berechtigung nicht mit einem Hash kollidiert, der als DHT-Lookup-Schlüssel verwendet wird, wie beispielsweise der einfache Destination-Hash.

Für einen gegebenen blinded key können wir dann eine Subcredential ableiten:

```
subcredential = H("subcredential", credential || blindedPublicKey)
```
Das subcredential wird in die unten beschriebenen Schlüsselableitungsprozesse einbezogen, wodurch diese Schlüssel an die Kenntnis des öffentlichen Signaturschlüssels des Destination gebunden werden.

#### Layer 1 Verschlüsselung

Zunächst wird die Eingabe für den Schlüsselableitungsprozess vorbereitet:

```
outerInput = subcredential || publishedTimestamp
```
Als nächstes wird ein zufälliges Salt generiert:

```
outerSalt = CSRNG(32)
```
Dann wird der Schlüssel zur Verschlüsselung von Schicht 1 abgeleitet:

```
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Schließlich wird der Layer-1-Klartext verschlüsselt und serialisiert:

```
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```
#### Layer 1 Entschlüsselung

Das Salt wird aus dem Layer-1-Chiffretext geparst:

```
outerSalt = outerCiphertext[0:31]
```
Dann wird der Schlüssel abgeleitet, der zur Verschlüsselung von Schicht 1 verwendet wird:

```
outerInput = subcredential || publishedTimestamp
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Schließlich wird der Schichttext der Ebene 1 entschlüsselt:

```
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```
#### Layer-2-Verschlüsselung

Wenn die Client-Autorisierung aktiviert ist, wird `authCookie` wie unten beschrieben berechnet. Wenn die Client-Autorisierung deaktiviert ist, ist `authCookie` das Byte-Array der Länge null.

Die Verschlüsselung erfolgt in ähnlicher Weise wie bei Schicht 1:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = CSRNG(32)
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```
#### Layer 2 Entschlüsselung

Wenn die Client-Autorisierung aktiviert ist, wird `authCookie` wie unten beschrieben berechnet. Wenn die Client-Autorisierung deaktiviert ist, ist `authCookie` das Byte-Array mit der Länge null.

Die Entschlüsselung läuft ähnlich wie bei Schicht 1 ab:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = innerCiphertext[0:31]
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```
### Pro-Client-Autorisierung

Wenn Client-Autorisierung für eine Destination aktiviert ist, verwaltet der Server eine Liste von Clients, die er autorisiert, die verschlüsselten LS2-Daten zu entschlüsseln. Die pro Client gespeicherten Daten hängen vom Autorisierungsmechanismus ab und umfassen eine Form von Schlüsselmaterial, das jeder Client generiert und über einen sicheren Out-of-Band-Mechanismus an den Server sendet.

Es gibt zwei Alternativen für die Implementierung der clientbezogenen Autorisierung:

#### DH-Client-Autorisierung

Jeder Client generiert ein DH-Schlüsselpaar `[csk_i, cpk_i]` und sendet den öffentlichen Schlüssel `cpk_i` an den Server.

##### Server-Verarbeitung

Der Server generiert ein neues `authCookie` und ein ephemeres DH-Schlüsselpaar:

```
authCookie = CSRNG(32)
esk = GENERATE_PRIVATE()
epk = DERIVE_PUBLIC(esk)
```
Dann verschlüsselt der Server für jeden autorisierten Client das `authCookie` mit dessen öffentlichem Schlüssel:

```
sharedSecret = DH(esk, cpk_i)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
Der Server platziert jedes `[clientID_i, clientCookie_i]` Tupel in Schicht 1 des verschlüsselten LS2, zusammen mit `epk`.

##### Client-Verarbeitung

Der Client verwendet seinen privaten Schlüssel, um seine erwartete Client-Kennung `clientID_i`, den Verschlüsselungsschlüssel `clientKey_i` und den Verschlüsselungs-IV `clientIV_i` abzuleiten:

```
sharedSecret = DH(csk_i, epk)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Dann durchsucht der Client die Layer-1-Autorisierungsdaten nach einem Eintrag, der `clientID_i` enthält. Wenn ein passender Eintrag existiert, entschlüsselt der Client ihn, um `authCookie` zu erhalten:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Pre-shared Key Client-Autorisierung

Jeder Client generiert einen geheimen 32-Byte-Schlüssel `psk_i` und sendet ihn an den Server. Alternativ kann der Server den geheimen Schlüssel generieren und ihn an einen oder mehrere Clients senden.

##### Serververarbeitung

Der Server generiert ein neues `authCookie` und Salt:

```
authCookie = CSRNG(32)
authSalt = CSRNG(32)
```
Dann verschlüsselt der Server für jeden autorisierten Client das `authCookie` mit dessen vorab geteiltem Schlüssel:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
Der Server platziert jedes `[clientID_i, clientCookie_i]`-Tupel in Schicht 1 des verschlüsselten LS2, zusammen mit `authSalt`.

##### Client-Verarbeitung

Der Client verwendet seinen vorab geteilten Schlüssel, um seine erwartete Client-Kennung `clientID_i`, seinen Verschlüsselungsschlüssel `clientKey_i` und seinen Verschlüsselungs-IV `clientIV_i` abzuleiten:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Dann durchsucht der Client die Layer-1-Autorisierungsdaten nach einem Eintrag, der `clientID_i` enthält. Falls ein passender Eintrag existiert, entschlüsselt der Client ihn, um `authCookie` zu erhalten:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Sicherheitsüberlegungen

Beide oben genannten Client-Autorisierungsmechanismen bieten Privatsphäre für die Client-Mitgliedschaft. Eine Entität, die nur das Destination kennt, kann sehen, wie viele Clients zu einem beliebigen Zeitpunkt abonniert sind, aber kann nicht nachverfolgen, welche Clients hinzugefügt oder widerrufen werden.

Server SOLLTEN die Reihenfolge der Clients jedes Mal randomisieren, wenn sie ein verschlüsseltes LS2 generieren, um zu verhindern, dass Clients ihre Position in der Liste erfahren und ableiten können, wann andere Clients hinzugefügt oder widerrufen wurden.

Ein Server KANN sich dafür entscheiden, die Anzahl der abonnierten Clients zu verbergen, indem er zufällige Einträge in die Liste der Autorisierungsdaten einfügt.

##### Vorteile der DH-Client-Autorisierung

- Die Sicherheit des Schemas hängt nicht ausschließlich vom Out-of-Band-Austausch des Client-Schlüsselmaterials ab. Der private Schlüssel des Clients muss niemals sein Gerät verlassen, sodass ein Angreifer, der den Out-of-Band-Austausch abfangen kann, aber den DH-Algorithmus nicht brechen kann, weder das verschlüsselte LS2 entschlüsseln noch bestimmen kann, wie lange dem Client Zugang gewährt wird.

##### Nachteile der DH-Client-Autorisierung

- Erfordert N + 1 DH-Operationen auf der Serverseite für N Clients.
- Erfordert eine DH-Operation auf der Client-Seite.
- Erfordert, dass der Client den geheimen Schlüssel generiert.

##### Vorteile der PSK-Client-Autorisierung

- Erfordert keine DH-Operationen.
- Ermöglicht es dem Server, den geheimen Schlüssel zu generieren.
- Ermöglicht es dem Server, denselben Schlüssel mit mehreren Clients zu teilen, falls gewünscht.

##### Nachteile der PSK-Client-Autorisierung

- Die Sicherheit des Schemas hängt kritisch vom Out-of-Band-Austausch des Client-Schlüsselmaterials ab. Ein Angreifer, der den Austausch für einen bestimmten Client abfängt, kann alle nachfolgenden verschlüsselten LS2 entschlüsseln, für die dieser Client autorisiert ist, sowie bestimmen, wann der Zugang des Clients widerrufen wird.

### Verschlüsselte LS mit Base 32 Adressen

Du kannst keine traditionelle Base-32-Adresse für ein verschlüsseltes LS2 verwenden, da sie nur den Hash des Ziels enthält. Sie stellt den nicht-geblendeten öffentlichen Schlüssel nicht zur Verfügung. Daher ist eine Base-32-Adresse allein unzureichend. Der Client benötigt entweder das vollständige Ziel (das den öffentlichen Schlüssel enthält) oder den öffentlichen Schlüssel selbst. Wenn der Client das vollständige Ziel in einem Adressbuch hat und das Adressbuch die Rückwärtssuche nach Hash unterstützt, dann kann der öffentliche Schlüssel abgerufen werden.

Daher benötigen wir ein neues Format, das den public key anstelle des Hashes in eine base32-Adresse einfügt. Dieses Format muss auch den signature type des public key und den signature type des blinding scheme enthalten. Die Gesamtanforderungen betragen 32 + 3 = 35 Bytes, was 56 Zeichen in base 32 erfordert, oder mehr für längere public key-Typen.

```
data = ((1 byte flags || 1 byte unblinded sigtype || 1 byte blinded sigtype) XOR checksum) || 32 byte pubkey
address = Base32Encode(data) || ".b32.i2p"
```
Wir verwenden das gleiche ".b32.i2p" Suffix wie für traditionelle base 32 Adressen. Adressen für verschlüsselte leaseSets werden durch die 56 kodierten Zeichen (35 dekodierte Bytes) identifiziert, im Vergleich zu 52 Zeichen (32 Bytes) für traditionelle base 32 Adressen. Die fünf ungenutzten Bits am Ende von b32 müssen 0 sein.

Du kannst kein verschlüsseltes LS2 für BitTorrent verwenden, wegen der kompakten Announce-Antworten, die 32 Bytes groß sind. Die 32 Bytes enthalten nur den Hash. Es gibt keinen Platz für eine Angabe, dass das leaseSet verschlüsselt ist, oder für die Signaturtypen.

Siehe die [Namensgebungsspezifikation](/docs/specs/naming) oder [Vorschlag 149](/proposals/149-b32-encrypted-ls2) für weitere Informationen zum neuen Format.

### Verschlüsselte LS mit Offline-Schlüsseln

Für verschlüsselte leaseSets mit Offline-Schlüsseln müssen die geblendeten privaten Schlüssel ebenfalls offline generiert werden, einen für jeden Tag.

Da der optionale Offline-Signaturblock im Klartext-Teil des verschlüsselten leaseSets liegt, könnte jeder, der die floodfills durchsucht, dies verwenden, um das leaseSet (aber nicht es zu entschlüsseln) über mehrere Tage zu verfolgen. Um dies zu verhindern, sollte der Besitzer der Schlüssel auch für jeden Tag neue temporäre Schlüssel generieren. Sowohl die temporären als auch die geblendeten Schlüssel können im Voraus generiert und dem router in einem Batch geliefert werden.

Es ist kein Dateiformat definiert, um mehrere temporäre und geblindete Schlüssel zu bündeln und diese dem Client oder router bereitzustellen. Es ist keine I2CP-Protokollerweiterung definiert, um verschlüsselte leaseSets mit Offline-Schlüsseln zu unterstützen.

### Notizen

- Ein Dienst, der verschlüsselte leasesets verwendet, würde die verschlüsselte Version an die floodfills veröffentlichen. Für die Effizienz würde er jedoch unverschlüsselte leasesets an Clients in der umhüllten garlic-Nachricht senden, sobald diese authentifiziert sind (z.B. über eine Whitelist).
- Floodfills können die maximale Größe auf einen angemessenen Wert begrenzen, um Missbrauch zu verhindern.
- Nach der Entschlüsselung sollten mehrere Prüfungen durchgeführt werden, einschließlich der Überprüfung, dass der innere Zeitstempel und das Ablaufdatum mit denen auf der obersten Ebene übereinstimmen.
- ChaCha20 wurde gegenüber AES ausgewählt. Während die Geschwindigkeiten ähnlich sind, wenn AES-Hardware-Unterstützung verfügbar ist, ist ChaCha20 2,5-3x schneller, wenn keine AES-Hardware-Unterstützung verfügbar ist, wie z.B. bei ARM-Geräten der unteren Preisklasse.

## Referenzen

- **[ED25519-REFS]** "High-speed high-security signatures" von Daniel J. Bernstein, Niels Duif, Tanja Lange, Peter Schwabe, und Bo-Yin Yang. [http://cr.yp.to/papers.html#ed25519](http://cr.yp.to/papers.html#ed25519)
- **[KEYBLIND-PROOF]** [https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html](https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html)
- **[KEYBLIND-REFS]** [https://trac.torproject.org/projects/tor/ticket/8106](https://trac.torproject.org/projects/tor/ticket/8106) und [https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html](https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html)
- **[PRNG-REFS]** [http://projectbullrun.org/dual-ec/ext-rand.html](http://projectbullrun.org/dual-ec/ext-rand.html) und [https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html)
- **[RFC-2104]** [https://tools.ietf.org/html/rfc2104](https://tools.ietf.org/html/rfc2104)
- **[RFC-4880-S5.1]** [https://tools.ietf.org/html/rfc4880#section-5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
- **[RFC-5869]** [https://tools.ietf.org/html/rfc5869](https://tools.ietf.org/html/rfc5869)
- **[RFC-7539-S2.4]** [https://tools.ietf.org/html/rfc7539#section-2.4](https://tools.ietf.org/html/rfc7539#section-2.4)
- **[TOR-REND-SPEC-V3]** [https://spec.torproject.org/rend-spec-v3](https://spec.torproject.org/rend-spec-v3)
- **[ZCASH]** [https://github.com/zcash/zips/tree/master/protocol/protocol.pdf](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)
