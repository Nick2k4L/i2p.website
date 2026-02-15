---
title: "B32 für verschlüsselte LeaseSet"
description: "Base 32 Adressformat für verschlüsselte LS2 leaseSets"
slug: "b32encrypted"
aliases:
  - "/de/docs/specs/b32-for-encrypted-leasesets"
  - "/de/docs/specs/b32-for-encrypted-leasesets/"
category: "Design"
lastUpdated: "2020-08"
accurateFor: "0.9.47"
---

## Überblick

Standard Base 32 ("b32") Adressen enthalten den Hash des Ziels. Dies funktioniert nicht für verschlüsselte ls2 (Vorschlag 123).

Wir können keine traditionelle Base-32-Adresse für ein verschlüsseltes LS2 (Vorschlag 123) verwenden, da sie nur den Hash des Ziels enthält. Sie stellt den nicht-geblindeten öffentlichen Schlüssel nicht zur Verfügung. Clients müssen den öffentlichen Schlüssel des Ziels, den Signaturtyp, den geblindeten Signaturtyp und einen optionalen geheimen oder privaten Schlüssel kennen, um das leaseSet abzurufen und zu entschlüsseln. Daher ist eine Base-32-Adresse allein unzureichend. Der Client benötigt entweder das vollständige Ziel (welches den öffentlichen Schlüssel enthält) oder den öffentlichen Schlüssel selbst. Wenn der Client das vollständige Ziel in einem Adressbuch hat und das Adressbuch die Rückwärtssuche nach Hash unterstützt, kann der öffentliche Schlüssel abgerufen werden.

Dieses Format fügt den öffentlichen Schlüssel anstelle des Hash-Werts in eine base32-Adresse ein. Dieses Format muss auch den Signaturtyp des öffentlichen Schlüssels und den Signaturtyp des Blinding-Schemas enthalten.

Dieses Dokument spezifiziert ein b32-Format für diese Adressen. Obwohl wir während Diskussionen auf dieses neue Format als "b33"-Adresse verwiesen haben, behält das tatsächliche neue Format das übliche ".b32.i2p"-Suffix bei.

## Design

- Das neue Format wird den ungeblendeten öffentlichen Schlüssel, den ungeblendeten Signaturtyp und den geblendeten Signaturtyp enthalten.
- Optional einen geheimen und/oder privaten Schlüssel enthalten, nur für private Links
- Das bestehende ".b32.i2p"-Suffix verwenden, aber mit längerer Länge.
- Eine Prüfsumme hinzufügen.
- Adressen für verschlüsselte leasesets werden durch 56 oder mehr kodierte Zeichen (35 oder mehr dekodierte Bytes) identifiziert, im Vergleich zu 52 Zeichen (32 Bytes) für traditionelle Base-32-Adressen.

## Spezifikation

### Erstellung und Kodierung

Erstellen Sie einen Hostname von {56+ Zeichen}.b32.i2p (35+ Zeichen in Binärform) wie folgt:

```
flag (1 byte)
    bit 0: 0 for one-byte sigtypes, 1 for two-byte sigtypes
    bit 1: 0 for no secret, 1 if secret is required
    bit 2: 0 for no per-client auth, 1 if client private key is required
    bits 7-3: Unused, set to 0

public key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

blinded key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

public key
    Number of bytes as implied by sigtype
```
Nachbearbeitung und Prüfsumme:

```
Construct the binary data as above.
Treat checksum as little-endian.
Calculate checksum = CRC-32(data[3:end])
data[0] ^= (byte) checksum
data[1] ^= (byte) (checksum >> 8)
data[2] ^= (byte) (checksum >> 16)

hostname = Base32.encode(data) || ".b32.i2p"
```
Alle ungenutzten Bits am Ende der b32 müssen 0 sein. Es gibt keine ungenutzten Bits für eine Standard-56-Zeichen (35 Byte) Adresse.

### Dekodierung und Verifikation

```
strip the ".b32.i2p" from the hostname
data = Base32.decode(hostname)
Calculate checksum = CRC-32(data[3:end])
Treat checksum as little-endian.
flags = data[0] ^ (byte) checksum
if 1 byte sigtypes:
    pubkey sigtype = data[1] ^ (byte) (checksum >> 8)
    blinded sigtype = data[2] ^ (byte) (checksum >> 16)
else (2 byte sigtypes):
    pubkey sigtype = data[1] ^ ((byte) (checksum >> 8)) || data[2] ^ ((byte) (checksum >> 16))
    blinded sigtype = data[3] || data[4]
parse the remainder based on the flags to get the public key
```
### Secret und Private Key Bits

Die secret- und private-key-Bits werden verwendet, um Clients, Proxies oder anderem clientseitigen Code anzuzeigen, dass der secret- und/oder private-key benötigt wird, um das leaseSet zu entschlüsseln. Bestimmte Implementierungen können den Benutzer auffordern, die erforderlichen Daten bereitzustellen, oder Verbindungsversuche ablehnen, wenn die erforderlichen Daten fehlen.

## Zwischenspeicherung

Obwohl dies außerhalb des Geltungsbereichs dieser Spezifikation liegt, müssen router und/oder Clients die Zuordnung von öffentlichem Schlüssel zu Ziel und umgekehrt speichern und zwischenspeichern (wahrscheinlich persistent).

## Hinweise

- Unterscheide alte von neuen Varianten anhand der Länge. Alte b32-Adressen haben
  immer {52 Zeichen}.b32.i2p. Neue haben {56+ Zeichen}.b32.i2p
- Tor-Diskussionsthread:
  https://lists.torproject.org/pipermail/tor-dev/2017-January/011816.html
- Erwarte nicht, dass 2-Byte-sigtypes jemals auftreten, wir sind erst bei 13. Keine
  Notwendigkeit, das jetzt zu implementieren.
- Das neue Format kann in Jump-Links (und von Jump-Servern bereitgestellt) verwendet werden,
  falls gewünscht, genau wie b32.

## Referenzen

- [CRC-32](https://en.wikipedia.org/wiki/CRC-32) - siehe auch [RFC 3309](https://tools.ietf.org/html/rfc3309)
