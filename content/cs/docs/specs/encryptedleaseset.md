---
title: "Specifikace šifrovaného LeaseSet"
description: "Blinding, šifrování a dešifrování šifrovaných leaseSet"
slug: "encryptedleaseset"
category: "Protokoly"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Přehled

Tento dokument specifikuje zaslepování, šifrování a dešifrování šifrovaných leaseSets. Pro strukturu šifrovaného leaseSet viz [specifikaci běžných struktur](/docs/specs/common-structures). Pro pozadí k šifrovaným leaseSets viz [návrh 123](/proposals/123-new-netdb-entries). Pro použití v netDb viz dokumentaci netdb.

### Definice

Definujeme následující funkce odpovídající kryptografickým stavebním blokům používaným pro šifrované LS2:

**CSRNG(n)** : n-bytový výstup z kryptograficky bezpečného generátoru náhodných čísel.

Kromě požadavku, aby CSRNG byl kryptograficky bezpečný (a tedy vhodný pro generování klíčového materiálu), MUSÍ být bezpečný pro použití n-bajtového výstupu jako klíčový materiál, když jsou bajtové sekvence bezprostředně předcházející a následující vystaveny v síti (například v salti nebo šifrovaném paddingu). Implementace, které se spoléhají na potenciálně nedůvěryhodný zdroj, by měly hashovat jakýkoli výstup, který má být vystaven v síti [PRNG-REFS](http://projectbullrun.org/dual-ec/ext-rand.html).

**H(p, d)** : Hashovací funkce SHA-256, která přijímá personalizační řetězec p a data d a produkuje výstup o délce 32 bajtů.

Použijte SHA-256 následovně:

```
H(p, d) := SHA-256(p || d)
```
**STREAM** : Proudová šifra ChaCha20 jak je specifikována v [RFC-7539-S2.4](https://tools.ietf.org/html/rfc7539#section-2.4), s počátečním čítačem nastaveným na 1. S_KEY_LEN = 32 a S_IV_LEN = 12.

- **ENCRYPT(k, iv, plaintext)** : Šifruje prostý text pomocí šifrovacího klíče k a nonce iv, které MUSÍ být jedinečné pro klíč k. Vrací šifrovaný text, který má stejnou velikost jako prostý text. Celý šifrovaný text musí být nerozlišitelný od náhodného, pokud je klíč tajný.

- **DECRYPT(k, iv, ciphertext)** : Dešifruje šifrovaný text pomocí šifrovacího klíče k a nonce iv. Vrací prostý text.

**SIG** : Schéma podpisu Red25519 (odpovídá SigType 11) s oslepením klíčů. Má následující funkce:

- **DERIVE_PUBLIC(privkey)** : Vrací veřejný klíč odpovídající danému soukromému klíči.

- **SIGN(privkey, m)** : Vrací podpis privátním klíčem privkey pro danou zprávu m.

- **VERIFY(pubkey, m, sig)** : Ověřuje podpis sig proti veřejnému klíči pubkey a zprávě m. Vrací true, pokud je podpis platný, jinak false.

Musí také podporovat následující operace zaslepení klíčů:

- **GENERATE_ALPHA(data, secret)** : Vygeneruje alpha pro ty, kteří znají data a volitelné tajemství. Výsledek musí být identicky distribuován jako soukromé klíče.

- **BLIND_PRIVKEY(privkey, alpha)** : Zaslepuje soukromý klíč pomocí tajného alpha.

- **BLIND_PUBKEY(pubkey, alpha)** : Zaslepí veřejný klíč pomocí tajného alfa. Pro daný pár klíčů (privkey, pubkey) platí následující vztah:

```
BLIND_PUBKEY(pubkey, alpha) ==
DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))
```
**DH** : Systém dohody veřejných klíčů X25519. Soukromé klíče o 32 bytech, veřejné klíče o 32 bytech, produkuje výstupy o 32 bytech. Má následující funkce:

- **GENERATE_PRIVATE()** : Generuje nový privátní klíč.

- **DERIVE_PUBLIC(privkey)** : Vrací veřejný klíč odpovídající danému soukromému klíči.

- **DH(privkey, pubkey)** : Generuje sdílené tajemství z daných soukromých a veřejných klíčů.

**HKDF(salt, ikm, info, n)** : Kryptografická funkce pro derivaci klíčů, která bere vstupní klíčový materiál ikm (který by měl mít dobrou entropii, ale nemusí být uniformně náhodný řetězec), salt o délce 32 bajtů a kontextově specifickou hodnotu 'info', a produkuje výstup n bajtů vhodný pro použití jako klíčový materiál.

Použijte HKDF podle specifikace v [RFC-5869](https://tools.ietf.org/html/rfc5869), s použitím HMAC hash funkce SHA-256 podle specifikace v [RFC-2104](https://tools.ietf.org/html/rfc2104). To znamená, že SALT_LEN je maximálně 32 bajtů.

### Formát

Šifrovaný formát LS2 se skládá ze tří vnořených vrstev:

- Vnější vrstva obsahující nezbytné informace v otevřeném textu pro ukládání a získávání.
- Střední vrstva, která zpracovává autentifikaci klienta.
- Vnitřní vrstva obsahující skutečná LS2 data.

Celkový formát vypadá takto:

```
Layer 0 data + Enc(layer 1 data + Enc(layer 2 data)) + Signature
```
Všimněte si, že šifrovaný LS2 je zaslepený. Destination není v hlavičce. Umístění úložiště DHT je SHA-256(typ podpisu || zaslepený veřejný klíč) a denně se rotuje.

NEPOUŽÍVÁ standardní LS2 hlavičku specifikovanou výše.

#### Vrstva 0 (vnější)

**Typ** : 1 byte

Není skutečně v hlavičce, ale je součástí dat pokrytých podpisem. Převzato z pole v Database Store Message.

**Typ podpisu zaslepného veřejného klíče** : 2 bajty, big endian

Toto bude vždy typ 11, identifikující Red25519 blinded klíč.

**Blinded Public Key** : Délka podle typu podpisu

**Časová značka publikování** : 4 bajty, big endian

Sekundy od epochy, přetečení v roce 2106

**Expires** : 2 bajty, big endian

Posun od publikovaného časového razítka v sekundách, maximálně 18,2 hodiny

**Příznaky** : 2 bajty

Pořadí bitů: 15 14 ... 3 2 1 0

- Bit 0: Pokud 0, žádné offline klíče; pokud 1, offline klíče
- Ostatní bity: nastavit na 0 pro kompatibilitu s budoucím použitím

**Přechodná klíčová data** : Přítomna, pokud příznak označuje offline klíče

- **Časová značka vypršení** : 4 bajty, big endian. Sekundy od epochy, přetečení v roce 2106
- **Typ přechodového podpisu** : 2 bajty, big endian
- **Přechodový veřejný klíč pro podepisování** : Délka odvozená od typu podpisu
- **Podpis** : Délka odvozená od typu podpisu zaslepeného veřejného klíče. Nad časovou značkou vypršení, typem přechodového podpisu a přechodovým veřejným klíčem. Ověřeno pomocí zaslepeného veřejného klíče.

**lenOuterCiphertext** : 2 bajty, big endian

**outerCiphertext** : lenOuterCiphertext bajtů

Zašifrovaná data vrstvy 1. Viz níže pro algoritmy derivace klíčů a šifrování.

**Signature** : Délka podle typu podpisu použitého podpisového klíče

Podpis je ze všeho výše uvedeného. Pokud příznak označuje offline klíče, podpis se ověřuje s dočasným veřejným klíčem. Jinak se podpis ověřuje s maskovaným veřejným klíčem.

#### Vrstva 1 (střední)

**Příznaky** : 1 bajt

Pořadí bitů: 76543210

- Bit 0: 0 pro všechny, 1 pro jednotlivé klienty, následuje sekce autentizace
- Bity 3-1: Schéma autentizace, pouze pokud je bit 0 nastaven na 1 pro jednotlivé klienty, jinak 000
  - 000: DH autentizace klienta (nebo žádná autentizace jednotlivých klientů)
  - 001: PSK autentizace klienta
- Bity 7-4: Nepoužité, nastavit na 0 pro budoucí kompatibilitu

**DH client auth data** : Přítomno, pokud je flag bit 0 nastaven na 1 a flag bity 3-1 jsou nastaveny na 000.

- **ephemeralPublicKey** : 32 bytů
- **clients** : 2 byty, big endian. Počet authClient záznamů následujících, každý 40 bytů
- **authClient** : Autorizační data pro jednoho klienta. Viz níže pro algoritmus autorizace pro jednotlivé klienty.
  - **clientID_i** : 8 bytů
  - **clientCookie_i** : 32 bytů

**PSK client auth data** : Přítomno, pokud je flag bit 0 nastaven na 1 a flag bity 3-1 jsou nastaveny na 001.

- **authSalt** : 32 bajtů
- **clients** : 2 bajty, big endian. Počet authClient záznamů následujících dále, každý 40 bajtů
- **authClient** : Autorizační data pro jednoho klienta. Viz níže pro autorizační algoritmus pro jednotlivé klienty.
  - **clientID_i** : 8 bajtů
  - **clientCookie_i** : 32 bajtů

**innerCiphertext** : Délka implicitně určená pomocí lenOuterCiphertext (jakákoliv zbývající data)

Šifrovaná data vrstvy 2. Pro algoritmy odvození klíčů a šifrování viz níže.

#### Vrstva 2 (vnitřní)

**Typ** : 1 byte

Buď 3 (LS2) nebo 7 (Meta LS2)

**Data** : LeaseSet2 data pro daný typ.

Zahrnuje hlavičku a podpis.

### Odvození Blinding Key

Pro utajování klíčů používáme následující schéma založené na Ed25519 a ZCash RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf). Red25519 podpisy jsou nad křivkou Ed25519, používající SHA-512 pro hash.

Nepoužíváme Tor's rend-spec-v3.txt přílohu A.2 [TOR-REND-SPEC-V3](https://spec.torproject.org/rend-spec-v3), která má podobné konstrukční cíle, protože její zaslepené veřejné klíče mohou být mimo podgrupu primárního řádu s neznámými bezpečnostními důsledky.

#### Cíle

- Podpisový veřejný klíč v neoslepeném destination musí být Ed25519 (typ podpisu 7) nebo Red25519 (typ podpisu 11); žádné další typy podpisů nejsou podporovány
- Pokud je podpisový veřejný klíč offline, přechodný podpisový veřejný klíč musí být také Ed25519
- Blinding je výpočetně jednoduché
- Používá existující kryptografické primitiva
- Oslepené veřejné klíče nelze odoslepit
- Oslepené veřejné klíče musí být na křivce Ed25519 a v podgrupě prvočíselného řádu
- Pro odvození oslepeného veřejného klíče je nutné znát podpisový veřejný klíč destination (úplné destination není vyžadováno)
- Volitelně poskytuje dodatečné tajemství vyžadované pro odvození oslepeného veřejného klíče

#### Bezpečnost

Bezpečnost schématu blinding vyžaduje, aby distribuce alfa byla stejná jako u neoslepených soukromých klíčů. Nicméně, když oslepíme Ed25519 soukromý klíč (sig type 7) na Red25519 soukromý klíč (sig type 11), distribuce je odlišná. Pro splnění požadavků zcash sekce 4.1.6.1 [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf), Red25519 (sig type 11) by měl být použit i pro neoslepené klíče, tak aby "kombinace re-randomizovaného veřejného klíče a podpisu(ů) pod tímto klíčem neodhalila klíč, ze kterého byl re-randomizován." Pro existující destinace povolujeme type 7, ale pro nové destinace, které budou šifrovány, doporučujeme type 11.

#### Definice

**B** : Ed25519 základní bod (generátor) 2^255 - 19 jako v [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)

**L** : Řád Ed25519 2^252 + 27742317777372353535851937790883648493 jak je uvedeno v [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)

**DERIVE_PUBLIC(a)** : Převést soukromý klíč na veřejný, jako v Ed25519 (násobení G)

**alpha** : 32bajtové náhodné číslo známé těm, kteří znají cíl.

**GENERATE_ALPHA(destination, date, secret)** : Vygenerovat alfa pro aktuální datum, pro ty kteří znají cíl a tajemství. Výsledek musí být identicky distribuován jako Ed25519 privátní klíče.

**a** : Neoslepený 32bajtový EdDSA nebo RedDSA podepisovací soukromý klíč použitý k podepsání destinace

**A** : Nezastřený 32-bajtový veřejný klíč pro podepisování EdDSA nebo RedDSA v cíli, = DERIVE_PUBLIC(a), stejně jako u Ed25519

**a'** : Zaslepený 32-bajtový soukromý klíč EdDSA pro podepisování použitý k podepsání šifrovaného leaseSetu. Toto je platný soukromý klíč EdDSA.

**A'** : Zaslepený 32-bajtový veřejný klíč EdDSA pro podepisování v Destination, může být vygenerován pomocí DERIVE_PUBLIC(a'), nebo z A a alpha. Toto je platný veřejný klíč EdDSA, na křivce a v podgrupě prvočíselného řádu.

**LEOS2IP(x)** : Obrátit pořadí vstupních bajtů na little-endian

**H\*(x)** : 32 bajtů = (LEOS2IP(SHA512(x))) mod B, stejně jako v Ed25519 hash-and-reduce

#### Výpočty oslnění

Nový tajný alfa a zaslepené klíče musí být generovány každý den (UTC).

Tajný alfa a zaslepené klíče se vypočítají následovně:

GENERATE_ALPHA(destination, date, secret), pro všechny strany:

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
BLIND_PRIVKEY(), pro vlastníka publikujícího leaseSet:

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
BLIND_PUBKEY(), pro klienty načítající leaseSet:

```
alpha = GENERATE_ALPHA(destination, date, secret)
A = destination's signing public key
// Addition using group elements (points on the curve)
blinded public key = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```
Obě metody výpočtu A' dávají stejný výsledek, jak je požadováno.

#### Podepisování

Neoslepený leaseSet je podepsán neoslepeným Ed25519 nebo Red25519 podepisovacím soukromým klíčem a ověřen neoslepeným Ed25519 nebo Red25519 podepisovacím veřejným klíčem (typy podpisů 7 nebo 11) jako obvykle.

Pokud je podepisovací veřejný klíč offline, neoslepený leaseset je podepsán neoslepeným přechodným Ed25519 nebo Red25519 podepisovacím soukromým klíčem a ověřen neoslepeným Ed25519 nebo Red25519 přechodným podepisovacím veřejným klíčem (typy podpisů 7 nebo 11) jako obvykle. Viz níže pro další poznámky k offline klíčům pro šifrované leasesety.

Pro podpisování šifrovaného leaseSetu používáme Red25519 založený na RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) k podpisování a ověřování pomocí zaslepených klíčů. Podpisy Red25519 jsou nad křivkou Ed25519, používají SHA-512 pro hash.

Red25519 je podobný standardnímu Ed25519 kromě níže uvedených specifikací.

#### Výpočty podpisu/ověření

Vnější část šifrovaného leaseset používá Red25519 klíče a podpisy.

Red25519 je podobný Ed25519. Existují dva rozdíly:

Red25519 privátní klíče jsou generovány z náhodných čísel a poté musí být redukovány mod L, kde L je definováno výše. Ed25519 privátní klíče jsou generovány z náhodných čísel a poté "ořezány" pomocí bitového maskování na byty 0 a 31. Toto se pro Red25519 neprovádí. Funkce GENERATE_ALPHA() a BLIND_PRIVKEY() definované výše generují správné Red25519 privátní klíče pomocí mod L.

V Red25519 používá výpočet r pro podepisování dodatečná náhodná data a používá hodnotu veřejného klíče namísto hashe soukromého klíče. Kvůli náhodným datům je každý Red25519 podpis odlišný, i při podepisování stejných dat se stejným klíčem.

```
Signing:
  T = 80 random bytes
  r = H*(T || publickey || message)
  (rest is the same as in Ed25519)

Verification:
  Same as for Ed25519
```
### Šifrování a zpracování

#### Odvození podpověření

V rámci procesu oslепování musíme zajistit, že zašifrovaný LS2 může být dešifrován pouze někým, kdo zná odpovídající podpisový veřejný klíč Destination. Úplná Destination není vyžadována. Abychom toho dosáhli, odvodíme pověření z podpisového veřejného klíče:

```
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
credential = H("credential", keydata)
```
Personalizační řetězec zajišťuje, že pověření nekoliduje s žádným hashem používaným jako vyhledávací klíč DHT, jako je například obyčejný hash Destination.

Pro daný zaslepený klíč pak můžeme odvodit subpověření:

```
subcredential = H("subcredential", credential || blindedPublicKey)
```
Subcredential je zahrnut v níže uvedených procesech derivace klíčů, což váže tyto klíče k znalosti veřejného podpisového klíče Destination.

#### Šifrování vrstvy 1

Nejprve se připraví vstup pro proces odvození klíče:

```
outerInput = subcredential || publishedTimestamp
```
Dále se vygeneruje náhodný salt:

```
outerSalt = CSRNG(32)
```
Poté je odvozen klíč použitý k šifrování vrstvy 1:

```
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Nakonec je prostý text vrstvy 1 zašifrován a serializován:

```
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```
#### Dešifrování 1. vrstvy

Sůl je analyzována z šifrovaného textu vrstvy 1:

```
outerSalt = outerCiphertext[0:31]
```
Poté je odvozen klíč použitý k šifrování vrstvy 1:

```
outerInput = subcredential || publishedTimestamp
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Nakonec je dešifrován šifrovaný text vrstvy 1:

```
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```
#### Šifrování vrstvy 2

Když je povolena autorizace klienta, `authCookie` se vypočítá jak je popsáno níže. Když je autorizace klienta zakázána, `authCookie` je bajtové pole nulové délky.

Šifrování probíhá podobným způsobem jako u vrstvy 1:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = CSRNG(32)
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```
#### Dešifrování vrstvy 2

Když je povolena autorizace klienta, `authCookie` se vypočítá jak je popsáno níže. Když je autorizace klienta zakázána, `authCookie` je bajtové pole nulové délky.

Dešifrování probíhá podobným způsobem jako u vrstvy 1:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = innerCiphertext[0:31]
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```
### Autorizace pro jednotlivé klienty

Když je pro Destination povolena autorizace klienta, server udržuje seznam klientů, které autorizuje k dešifrování šifrovaných LS2 dat. Data uložená pro každého klienta závisí na autorizačním mechanismu a zahrnují nějakou formu klíčového materiálu, který každý klient generuje a posílá serveru prostřednictvím bezpečného out-of-band mechanismu.

Existují dvě alternativy pro implementaci autorizace podle klientů:

#### DH autorizace klienta

Každý klient generuje DH pár klíčů `[csk_i, cpk_i]` a odesílá veřejný klíč `cpk_i` na server.

##### Zpracování serveru

Server vygeneruje nový `authCookie` a dočasný DH klíčový pár:

```
authCookie = CSRNG(32)
esk = GENERATE_PRIVATE()
epk = DERIVE_PUBLIC(esk)
```
Poté pro každého autorizovaného klienta server zašifruje `authCookie` jeho veřejným klíčem:

```
sharedSecret = DH(esk, cpk_i)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
Server umístí každou n-tici `[clientID_i, clientCookie_i]` do vrstvy 1 šifrovaného LS2 spolu s `epk`.

##### Zpracování klienta

Klient používá svůj privátní klíč k odvození svého očekávaného identifikátoru klienta `clientID_i`, šifrovacího klíče `clientKey_i` a šifrovacího IV `clientIV_i`:

```
sharedSecret = DH(csk_i, epk)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Poté klient prohledává autorizační data vrstvy 1 pro záznam, který obsahuje `clientID_i`. Pokud odpovídající záznam existuje, klient ho dešifruje, aby získal `authCookie`:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Autorizace klienta pomocí předsdíleného klíče

Každý klient vygeneruje tajný 32-bytový klíč `psk_i` a pošle ho serveru. Alternativně může server vygenerovat tajný klíč a poslat ho jednomu nebo více klientům.

##### Zpracování serveru

Server vygeneruje nový `authCookie` a salt:

```
authCookie = CSRNG(32)
authSalt = CSRNG(32)
```
Pak pro každého autorizovaného klienta server zašifruje `authCookie` pomocí jeho předem sdíleného klíče:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
Server umístí každou dvojici `[clientID_i, clientCookie_i]` do vrstvy 1 šifrovaného LS2 spolu s `authSalt`.

##### Zpracování klienta

Klient používá svůj předem sdílený klíč k odvození svého očekávaného identifikátoru klienta `clientID_i`, šifrovacího klíče `clientKey_i` a šifrovacího IV `clientIV_i`:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Poté klient prohledá autorizační data vrstvy 1 pro záznam, který obsahuje `clientID_i`. Pokud odpovídající záznam existuje, klient jej dešifruje a získá `authCookie`:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Bezpečnostní aspekty

Oba výše uvedené mechanismy autorizace klientů poskytují soukromí pro členství klientů. Entita, která zná pouze Destination, může vidět, kolik klientů je kdykoli přihlášeno, ale nemůže sledovat, kteří klienti jsou přidáváni nebo odvoláváni.

Servery BY MĚLY randomizovat pořadí klientů pokaždé, když generují šifrovaný LS2, aby zabránily klientům zjistit jejich pozici v seznamu a odvodit, kdy byli jiní klienti přidáni nebo odvoláni.

Server MŮŽE zvolit skrytí počtu přihlášených klientů vložením náhodných záznamů do seznamu autorizačních dat.

##### Výhody DH autorizace klienta

- Bezpečnost schématu není závislá výhradně na out-of-band výměně klíčového materiálu klienta. Soukromý klíč klienta nikdy nepotřebuje opustit jeho zařízení, takže útočník, který je schopen zachytit out-of-band výměnu, ale nemůže prolomit DH algoritmus, nemůže dešifrovat zašifrovaný LS2 ani určit, jak dlouho má klient přístup.

##### Nevýhody DH klientské autorizace

- Vyžaduje N + 1 DH operací na straně serveru pro N klientů.
- Vyžaduje jednu DH operaci na straně klienta.
- Vyžaduje, aby klient vygeneroval tajný klíč.

##### Výhody PSK autorizace klienta

- Nevyžaduje žádné DH operace.
- Umožňuje serveru generovat tajný klíč.
- Umožňuje serveru sdílet stejný klíč s více klienty, pokud je to žádoucí.

##### Nevýhody PSK klientské autorizace

- Bezpečnost schématu je kriticky závislá na out-of-band výměně klíčového materiálu klienta. Protivník, který zachytí výměnu pro konkrétního klienta, může dešifrovat jakékoli následné šifrované LS2, pro které je tento klient autorizován, a také určit, kdy je přístup klienta odvolán.

### Šifrované LS s Base 32 adresami

Nemůžete použít tradiční base 32 adresu pro šifrovaný LS2, protože obsahuje pouze hash destinace. Neposkytuje nezastřený veřejný klíč. Proto samotná base 32 adresa není dostatečná. Klient potřebuje buď úplnou destinaci (která obsahuje veřejný klíč), nebo samotný veřejný klíč. Pokud má klient úplnou destinaci v adresáři a adresář podporuje reverzní vyhledávání podle hash, pak může být veřejný klíč získán.

Potřebujeme tedy nový formát, který vloží veřejný klíč místo hashe do base32 adresy. Tento formát musí také obsahovat typ podpisu veřejného klíče a typ podpisu schématu zaslepování. Celkové požadavky jsou 32 + 3 = 35 bajtů, což vyžaduje 56 znaků v base 32, nebo více pro delší typy veřejných klíčů.

```
data = ((1 byte flags || 1 byte unblinded sigtype || 1 byte blinded sigtype) XOR checksum) || 32 byte pubkey
address = Base32Encode(data) || ".b32.i2p"
```
Používáme stejnou příponu ".b32.i2p" jako pro tradiční base 32 adresy. Adresy pro šifrované leaseSet jsou identifikovány 56 kódovanými znaky (35 dekódovaných bajtů) ve srovnání s 52 znaky (32 bajty) pro tradiční base 32 adresy. Pět nepoužitých bitů na konci b32 musí být 0.

Nemůžete použít šifrovaný LS2 pro bittorrent kvůli kompaktním odpovědím announce, které mají 32 bajtů. Těch 32 bajtů obsahuje pouze hash. Není zde místo pro označení, že leaseSet je šifrovaný, nebo pro typy podpisů.

Více informací o novém formátu naleznete ve [specifikaci pojmenování](/docs/specs/naming) nebo v [návrhu 149](/proposals/149-b32-encrypted-ls2).

### Šifrovaný LS s offline klíči

Pro šifrované leaseSety s offline klíči musí být také offline generovány zaslepené soukromé klíče, jeden pro každý den.

Jelikož volitelný blok offline podpisu se nachází v nešifrované části zašifrovaného leaseSetu, kdokoli procházející floodfilly by to mohl použít ke sledování leaseSetu (ale ne k jeho dešifrování) po několik dní. Aby se tomu zabránilo, měl by vlastník klíčů také generovat nové přechodné klíče pro každý den. Jak přechodné, tak blinded klíče mohou být generovány předem a doručeny do routeru v dávce.

Neexistuje definovaný formát souboru pro balení více přechodných a zaslepených klíčů a jejich poskytování klientovi nebo routeru. Neexistuje definované vylepšení protokolu I2CP pro podporu šifrovaných leaseSets s offline klíči.

### Poznámky

- Služba používající šifrované leasesets by publikovala šifrovanou verzi do floodfills. Pro efektivitu by však posílala nešifrované leasesets klientům v zabaleném garlic message, jakmile by byly autentizovány (například pomocí whitelistu).
- Floodfills mohou omezit maximální velikost na rozumnou hodnotu, aby předešly zneužití.
- Po dešifrování by mělo být provedeno několik kontrol, včetně toho, že vnitřní časové razítko a expirace odpovídají těm na nejvyšší úrovni.
- ChaCha20 byl vybrán před AES. Zatímco rychlosti jsou podobné, pokud je k dispozici hardwarová podpora AES, ChaCha20 je 2,5-3x rychlejší, když hardwarová podpora AES není k dispozici, například na slabších ARM zařízeních.

## Reference

- **[ED25519-REFS]** "High-speed high-security signatures" od Daniel J. Bernstein, Niels Duif, Tanja Lange, Peter Schwabe a Bo-Yin Yang. [http://cr.yp.to/papers.html#ed25519](http://cr.yp.to/papers.html#ed25519)
- **[KEYBLIND-PROOF]** [https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html](https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html)
- **[KEYBLIND-REFS]** [https://trac.torproject.org/projects/tor/ticket/8106](https://trac.torproject.org/projects/tor/ticket/8106) a [https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html](https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html)
- **[PRNG-REFS]** [http://projectbullrun.org/dual-ec/ext-rand.html](http://projectbullrun.org/dual-ec/ext-rand.html) a [https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html)
- **[RFC-2104]** [https://tools.ietf.org/html/rfc2104](https://tools.ietf.org/html/rfc2104)
- **[RFC-4880-S5.1]** [https://tools.ietf.org/html/rfc4880#section-5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
- **[RFC-5869]** [https://tools.ietf.org/html/rfc5869](https://tools.ietf.org/html/rfc5869)
- **[RFC-7539-S2.4]** [https://tools.ietf.org/html/rfc7539#section-2.4](https://tools.ietf.org/html/rfc7539#section-2.4)
- **[TOR-REND-SPEC-V3]** [https://spec.torproject.org/rend-spec-v3](https://spec.torproject.org/rend-spec-v3)
- **[ZCASH]** [https://github.com/zcash/zips/tree/master/protocol/protocol.pdf](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)
