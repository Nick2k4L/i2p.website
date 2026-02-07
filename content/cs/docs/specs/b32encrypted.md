---
title: "B32 pro šifrované LeaseSet"
description: "Formát Base 32 adres pro šifrované LS2 leaseSet"
slug: "b32encrypted"
category: "Návrh"
lastUpdated: "2020-08"
accurateFor: "0.9.47"
---

## Přehled

Standardní Base 32 ("b32") adresy obsahují hash cíle. To nebude fungovat pro šifrované ls2 (návrh 123).

Nemůžeme použít tradiční base 32 adresu pro šifrovaný LS2 (návrh 123), protože obsahuje pouze hash cíle. Neposkytuje nezaslepený veřejný klíč. Klienti musí znát veřejný klíč cíle, typ podpisu, zaslepený typ podpisu a volitelný tajný nebo soukromý klíč pro získání a dešifrování leaseset. Proto samotná base 32 adresa není dostatečná. Klient potřebuje buď úplný cíl (který obsahuje veřejný klíč), nebo veřejný klíč samostatně. Pokud má klient úplný cíl v adresáři a adresář podporuje zpětné vyhledávání podle hash, pak může být veřejný klíč získán.

Tento formát vkládá do base32 adresy veřejný klíč namísto hash. Tento formát musí také obsahovat typ podpisu veřejného klíče a typ podpisu schématu zaslepování.

Tento dokument specifikuje formát b32 pro tyto adresy. Ačkoli jsme během diskusí odkazovali na tento nový formát jako na adresu "b33", skutečný nový formát si zachovává obvyklou příponu ".b32.i2p".

## Návrh

- Nový formát bude obsahovat neoslepený veřejný klíč, typ neoslepené signaturky
  a typ oslepené signaturky.
- Volitelně obsahuje tajný a/nebo soukromý klíč, pouze pro soukromé odkazy
- Používá existující příponu ".b32.i2p", ale s větší délkou.
- Přidává kontrolní součet.
- Adresy pro šifrované leaseSety jsou identifikovány 56 nebo více kódovanými
  znaky (35 nebo více dekódovaných bajtů), oproti 52 znakům (32
  bajtů) u tradičních base 32 adres.

## Specifikace

### Vytvoření a kódování

Sestavte hostname {56+ znaků}.b32.i2p (35+ znaků v binárním formátu) následovně:

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
Následné zpracování a kontrolní součet:

```
Construct the binary data as above.
Treat checksum as little-endian.
Calculate checksum = CRC-32(data[3:end])
data[0] ^= (byte) checksum
data[1] ^= (byte) (checksum >> 8)
data[2] ^= (byte) (checksum >> 16)

hostname = Base32.encode(data) || ".b32.i2p"
```
Všechny nepoužité bity na konci b32 musí být 0. Pro standardní 56znakovou (35bajtovou) adresu nejsou žádné nepoužité bity.

### Dekódování a ověření

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
### Bity tajného a soukromého klíče

Bity secret a private key se používají k indikaci klientům, proxy serverům nebo jinému kódu na straně klienta, že secret a/nebo private key budou potřeba k dešifrování leaseSetu. Konkrétní implementace mohou vyzvat uživatele k poskytnutí požadovaných dat nebo odmítnout pokusy o připojení, pokud požadovaná data chybí.

## Ukládání do mezipaměti

Ačkoli je to mimo rozsah této specifikace, routery a/nebo klienti si musí pamatovat a ukládat do mezipaměti (pravděpodobně trvale) mapování veřejného klíče na destination a naopak.

## Poznámky

- Rozlište staré od nových variant podle délky. Staré b32 adresy jsou
  vždy {52 znaků}.b32.i2p. Nové jsou {56+ znaků}.b32.i2p
- Diskuzní vlákno Tor:
  https://lists.torproject.org/pipermail/tor-dev/2017-January/011816.html
- Neočekávejte, že se někdy objeví 2-bajtové sigtypes, jsme teprve na 13. Není
  potřeba to teď implementovat.
- Nový formát lze použít v jump odkazech (a obsluhovat jump servery), pokud
  je to žádoucí, stejně jako b32.

## Reference

- [CRC-32](https://en.wikipedia.org/wiki/CRC-32) - viz také [RFC 3309](https://tools.ietf.org/html/rfc3309)
