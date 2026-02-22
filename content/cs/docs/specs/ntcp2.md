---
title: "NTCP2 Transport"
description: "TCP transport založený na Noise pro spojení mezi routery"
slug: "ntcp2"
category: "Transporty"
lastUpdated: "2026-01"
accurateFor: "0.9.66"
---

## Přehled

NTCP2 je autentifikovaný protokol pro dohodnutí klíčů, který zlepšuje odolnost [NTCP](/docs/transport/ntcp) proti různým formám automatické identifikace a útokům.

NTCP2 je navržen pro flexibilitu a koexistenci s NTCP. Může být podporován na stejném portu jako NTCP, nebo na jiném portu, nebo zcela bez současné podpory NTCP. Podrobnosti najdete v sekci Publikované informace o routeru níže.

Stejně jako u ostatních I2P transportů je NTCP2 definován výhradně pro point-to-point (router-to-router) přenos I2NP zpráv. Nejedná se o datové roury obecného účelu.

NTCP2 je podporován od verze 0.9.36. Viz [Prop111](/proposals/111-ntcp-2) pro původní návrh, včetně diskuze na pozadí a dalších informací.

## Noise Protocol Framework

NTCP2 používá Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (Revize 33, 2017-10-04). Noise má podobné vlastnosti jako protokol Station-To-Station [STS](#references), který je základem pro protokol [SSU](/docs/transport/ssu). V terminologii Noise je Alice iniciátor a Bob je respondent.

NTCP2 je založeno na protokolu Noise Noise_XK_25519_ChaChaPoly_SHA256. (Skutečný identifikátor pro počáteční funkci odvození klíčů je "Noise_XKaesobfse+hs2+hs3_25519_ChaChaPoly_SHA256" pro označení rozšíření I2P - viz sekce KDF 1 níže) Tento protokol Noise používá následující primitiva:

- Handshake Pattern: XK Alice přenáší svůj klíč Bobovi (X) Alice už zná Bobův statický klíč (K)
- DH Function: X25519 X25519 DH s délkou klíče 32 bajtů jak je specifikováno v [RFC-7748](https://tools.ietf.org/html/rfc7748).
- Cipher Function: ChaChaPoly AEAD_CHACHA20_POLY1305 jak je specifikováno v [RFC-7539](https://tools.ietf.org/html/rfc7539) sekce 2.8. 12 bajtový nonce, s prvními 4 bajty nastavenými na nulu.
- Hash Function: SHA256 Standardní 32-bajtový hash, již rozsáhle používaný v I2P.

## Doplňky k frameworku

NTCP2 definuje následující vylepšení pro Noise_XK_25519_ChaChaPoly_SHA256. Tato obecně následují pokyny v [NOISE](https://noiseprotocol.org/noise.html) sekci 13.

1) Efemérní klíče v otevřeném textu jsou zamaskované pomocí AES šifrování s použitím známého klíče a IV. 2) Do zpráv 1 a 2 je přidáno náhodné výplňové pole v otevřeném textu. Výplňové pole v otevřeném textu je zahrnuto do výpočtu hashe handshaku (MixHash). Viz sekce KDF níže pro zprávu 2 a zprávu 3 část 1. Do zprávy 3 a zpráv datové fáze je přidáno náhodné AEAD výplňové pole. 3) Je přidáno dvoubytové pole délky rámce, jak je vyžadováno pro Noise přes TCP a stejně jako v obfs4. Toto se používá pouze ve zprávách datové fáze. AEAD rámce zpráv 1 a 2 mají pevnou délku. AEAD rámec zprávy 3 část 1 má pevnou délku. Délka AEAD rámce zprávy 3 část 2 je specifikována ve zprávě 1. 4) Dvoubytové pole délky rámce je zamaskované pomocí SipHash-2-4, stejně jako v obfs4. 5) Formát užitečného obsahu je definován pro zprávy 1, 2, 3 a datovou fázi. Tyto samozřejmě nejsou definovány v rámci frameworku.

## Zprávy

Všechny NTCP2 zprávy mají délku menší nebo rovnou 65537 bajtů. Formát zpráv je založen na Noise zprávách, s úpravami pro rámcování a nerozlišitelnost. Implementace používající standardní Noise knihovny mohou potřebovat předpracovat přijaté zprávy do/z formátu Noise zpráv. Všechna zašifrovaná pole jsou AEAD šifrotexty.

Sekvence navázání spojení je následující:

```
Alice                           Bob

SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Pomocí terminologie Noise je sekvence ustanovení a dat následující: (Vlastnosti zabezpečení datové části z [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs):           Authentication   Confidentiality
  <- s
  ...
  -> e, es                  0                2
  <- e, ee                  2                1
  -> s, se                  2                5
  <-                        2                5
```
Jakmile je relace navázána, Alice a Bob si mohou vyměňovat Data zprávy.

Všechny typy zpráv (SessionRequest, SessionCreated, SessionConfirmed, Data a TimeSync) jsou specifikovány v této sekci.

Některé označení:

    - RH_A = Router Hash for Alice (32 bytes)
    - RH_B = Router Hash for Bob (32 bytes)

### Autentizované šifrování

Existují tři oddělené instance autentizovaného šifrování (CipherStates). Jedna během fáze handshake a dvě (odesílání a příjem) pro datovou fáze. Každá má svůj vlastní klíč z KDF.

Šifrovaná/ověřená data budou reprezentována jako

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   Encrypted and authenticated data    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
```
#### ChaCha20/Poly1305

Šifrovaný a ověřený formát dat.

Vstupy pro funkce šifrování/dešifrování:

```
k :: 32 byte cipher key, as generated from KDF

nonce :: Counter-based nonce, 12 bytes.
         Starts at 0 and incremented for each message.
         First four bytes are always zero.
         Last eight bytes are the counter, little-endian encoded.
         Maximum value is 2**64 - 2.
         Connection must be dropped and restarted after
         it reaches that value.
         The value 2**64 - 1 must never be sent.

ad :: In handshake phase:
      Associated data, 32 bytes.
      The SHA256 hash of all preceding data.
      In data phase:
      Zero bytes

data :: Plaintext data, 0 or more bytes
```
Výstup šifrovací funkce, vstup dešifrovací funkce:

```
+----+----+----+----+----+----+----+----+
|Obfs Len |                             |
+----+----+                             +
|       ChaCha20 encrypted data         |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|  Poly1305 Message Authentication Code |
+              (MAC)                    +
|             16 bytes                  |
+----+----+----+----+----+----+----+----+

Obfs Len :: Length of (encrypted data + MAC) to follow, 16 - 65535
            Obfuscation using SipHash (see below)
            Not used in message 1 or 2, or message 3 part 1, where the length is fixed
            Not used in message 3 part 1, as the length is specified in message 1

encrypted data :: Same size as plaintext data, 0 - 65519 bytes

MAC :: Poly1305 message authentication code, 16 bytes
```
Pro ChaCha20 to, co je zde popsáno, odpovídá [RFC-7539](https://tools.ietf.org/html/rfc7539), které se také podobně používá v TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).

#### Poznámky

- Jelikož ChaCha20 je proudová šifra, plaintexty nemusí být doplněny. Dodatečné bajty keystream jsou zahozeny.
- Klíč pro šifru (256 bitů) je dohodnut pomocí SHA256 KDF. Podrobnosti KDF pro každou zprávu jsou uvedeny v samostatných sekcích níže.
- ChaChaPoly rámce pro zprávy 1, 2 a první část zprávy 3 mají známou velikost. Počínaje druhou částí zprávy 3 mají rámce proměnnou velikost. Velikost části 1 zprávy 3 je specifikována ve zprávě 1. Od datové fáze jsou rámce předloženy dvoubajtovou délkou zastřenou pomocí SipHash jako v obfs4.
- Padding je mimo autentizovaný datový rámec pro zprávy 1 a 2. Padding je použit v KDF pro následující zprávu, takže manipulace bude detekována. Počínaje zprávou 3 je padding uvnitř autentizovaného datového rámce.

#### Zpracování chyb AEAD

- Ve zprávách 1, 2 a ve zprávě 3 částech 1 a 2 je velikost AEAD zprávy známa předem. Při selhání AEAD autentifikace musí příjemce zastavit další zpracování zpráv a zavřít spojení bez odpovědi. Toto by mělo být abnormální ukončení (TCP RST).
- Pro odolnost proti sondování by měl Bob ve zprávě 1 po selhání AEAD nastavit náhodný timeout (rozsah TBD) a poté načíst náhodný počet bajtů (rozsah TBD) před zavřením socketu. Bob by měl udržovat černou listinu IP adres s opakovanými selháními.
- Ve fázi dat je velikost AEAD zprávy "zašifrována" (obfuskována) pomocí SipHash. Je třeba dbát na to, aby nevznikl dešifrovací oracle. Při selhání AEAD autentifikace ve fázi dat by měl příjemce nastavit náhodný timeout (rozsah TBD) a poté načíst náhodný počet bajtů (rozsah TBD). Po načtení nebo při timeoutu čtení by měl příjemce odeslat payload s ukončovacím blokem obsahujícím kód důvodu "AEAD selhání" a zavřít spojení.
- Provést stejnou akci při chybě pro neplatnou hodnotu pole délky ve fázi dat.

### Funkce pro derivaci klíčů (KDF) (pro handshake zprávu 1)

KDF generuje šifrovací klíč k pro fázi handshake z výsledku DH, používající HMAC-SHA256(key, data) jak je definováno v [RFC-2104](https://tools.ietf.org/html/rfc2104). Jedná se o funkce InitializeSymmetric(), MixHash() a MixKey(), přesně tak jak jsou definovány ve specifikaci Noise.

```
This is the "e" message pattern:

// Define protocol_name.
Set protocol_name = "Noise_XKaesobfse+hs2+hs3_25519_ChaChaPoly_SHA256"
 (48 bytes, US-ASCII encoded, no NULL termination).

// Define Hash h = 32 bytes
h = SHA256(protocol_name);

Define ck = 32 byte chaining key. Copy the h data to ck.
Set ck = h

Define rs = Bob's 32-byte static key as published in the RouterInfo

// MixHash(null prologue)
h = SHA256(h);

// up until here, can all be precalculated by Alice for all outgoing connections

// Alice must validate that Bob's static key is a valid point on the curve here.

// Bob static key
// MixHash(rs)
// || below means append
h = SHA256(h || rs);

// up until here, can all be precalculated by Bob for all incoming connections

This is the "e" message pattern:

Alice generates her ephemeral DH key pair e.

// Alice ephemeral key X
// MixHash(e.pubkey)
// || below means append
h = SHA256(h || e.pubkey);

// h is used as the associated data for the AEAD in message 1
// Retain the Hash h for the message 2 KDF


End of "e" message pattern.

This is the "es" message pattern:

// DH(e, rs) == DH(s, re)
Define input_key_material = 32 byte DH result of Alice's ephemeral key and Bob's static key
Set input_key_material = X25519 DH result

// MixKey(DH())

Define temp_key = 32 bytes
Define HMAC-SHA256(key, data) as in [RFC-2104]_
// Generate a temp key from the chaining key and DH result
// ck is the chaining key, defined above
temp_key = HMAC-SHA256(ck, input_key_material)
// overwrite the DH result in memory, no longer needed
input_key_material = (all zeros)

// Output 1
// Set a new chaining key from the temp key
// byte() below means a single byte
ck =       HMAC-SHA256(temp_key, byte(0x01)).

// Output 2
// Generate the cipher key k
Define k = 32 bytes
// || below means append
// byte() below means a single byte
k =        HMAC-SHA256(temp_key, ck || byte(0x02)).
// overwrite the temp_key in memory, no longer needed
temp_key = (all zeros)

// retain the chaining key ck for message 2 KDF


End of "es" message pattern.
```
### 1) SessionRequest

Alice posílá Bobovi.

Noise obsah: Alice's ephemeral key X Noise payload: 16 bajtový blok možností Non-noise payload: Náhodné vyplnění

(Vlastnosti zabezpečení payload z [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs):           Authentication   Confidentiality
  -> e, es                  0                2

  Authentication: None (0).
  This payload may have been sent by any party, including an active attacker.

  Confidentiality: 2.
  Encryption to a known recipient, forward secrecy for sender compromise
  only, vulnerable to replay.  This payload is encrypted based only on DHs
  involving the recipient's static key pair.  If the recipient's static
  private key is compromised, even at a later date, this payload can be
  decrypted.  This message can also be replayed, since there's no ephemeral
  contribution from the recipient.

  "e": Alice generates a new ephemeral key pair and stores it in the e
       variable, writes the ephemeral public key as cleartext into the
       message buffer, and hashes the public key along with the old h to
       derive a new h.

  "es": A DH is performed between the Alice's ephemeral key pair and the
        Bob's static key pair.  The result is hashed along with the old ck to
        derive a new ck and k, and n is set to zero.
```
Hodnota X je šifrována pro zajištění nerozlišitelnosti a jedinečnosti payload, což jsou nezbytná protiopatření proti DPI. K dosažení tohoto cíle používáme šifrování AES místo složitějších a pomalejších alternativ jako je elligator2. Asymetrické šifrování veřejným klíčem Bobova routeru by bylo příliš pomalé. Šifrování AES používá hash Bobova routeru jako klíč a Bobovo IV publikované v síťové databázi.

Šifrování AES slouží pouze k odolnosti proti DPI. Každá strana znající hash Bobova routeru a IV, které jsou publikovány v síťové databázi, může dešifrovat hodnotu X v této zprávě.

Výplň není šifrována Alicí. Může být nutné, aby Bob výplň dešifroval, aby se zabránilo časovým útokům.

Nezpracovaný obsah:

```
+----+----+----+----+----+----+----+----+
|                                       |
+        obfuscated with RH_B           +
|       AES-CBC-256 encrypted X         |
+             (32 bytes)                +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaChaPoly frame                    |
+             (32 bytes)                +
|   k defined in KDF for message 1      |
+   n = 0                               +
|   see KDF for associated data         |
+----+----+----+----+----+----+----+----+
|     unencrypted authenticated         |
~         padding (optional)            ~
|     length defined in options block   |
+----+----+----+----+----+----+----+----+

X :: 32 bytes, AES-256-CBC encrypted X25519 ephemeral key, little endian
        key: RH_B
        iv: As published in Bobs network database entry

padding :: Random data, 0 or more bytes.
           Total message length must be 65535 bytes or less.
           Total message length must be 287 bytes or less if
           Bob is publishing his address as NTCP
           (see Version Detection section below).
           Alice and Bob will use the padding data in the KDF for message 2.
           It is authenticated so that any tampering will cause the
           next message to fail.
```
Nešifrovaná data (Poly1305 autentifikační tag není zobrazen):

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

X :: 32 bytes, X25519 ephemeral key, little endian

options :: options block, 16 bytes, see below

padding :: Random data, 0 or more bytes.
           Total message length must be 65535 bytes or less.
           Total message length must be 287 bytes or less if
           Bob is publishing his address as "NTCP"
           (see Version Detection section below)
           Alice and Bob will use the padding data in the KDF for message 2.
           It is authenticated so that any tampering will cause the
           next message to fail.
```
Blok možností: Poznámka: Všechna pole jsou v big-endian pořadí.

```
+----+----+----+----+----+----+----+----+
| id | ver|  padLen | m3p2len | Rsvd(0) |
+----+----+----+----+----+----+----+----+
|        tsA        |   Reserved (0)    |
+----+----+----+----+----+----+----+----+

id :: 1 byte, the network ID (currently 2, except for test networks)
      As of 0.9.42. See proposal 147.

ver :: 1 byte, protocol version (currently 2)

padLen :: 2 bytes, length of the padding, 0 or more
          Min/max guidelines TBD. Random size from 0 to 31 bytes minimum?
          (Distribution is implementation-dependent)

m3p2Len :: 2 bytes, length of the the second AEAD frame in SessionConfirmed
           (message 3 part 2) See notes below

Rsvd :: 2 bytes, set to 0 for compatibility with future options

tsA :: 4 bytes, Unix timestamp, unsigned seconds.
       Wraps around in 2106

Reserved :: 4 bytes, set to 0 for compatibility with future options
```
#### Poznámky

- Když je publikovaná adresa "NTCP", Bob podporuje jak NTCP, tak NTCP2 na stejném portu. Z důvodu kompatibility musí Alice při navazování spojení na adresu publikovanou jako "NTCP" omezit maximální velikost této zprávy včetně paddingu na 287 bajtů nebo méně. To umožňuje automatickou identifikaci protokolu ze strany Boba. Když je publikována jako "NTCP2", neexistuje žádné omezení velikosti. Viz sekce Published Addresses a Version Detection níže.

- Jedinečná hodnota X v počátečním AES bloku zajišťuje, že šifrovaný text je pro každou relaci odlišný.

- Bob musí odmítnout spojení, kde je hodnota časové značky příliš vzdálená od aktuálního času. Označme maximální časový rozdíl jako "D". Bob musí udržovat místní cache dříve použitých handshake hodnot a odmítnout duplikáty, aby zabránil replay útokům. Hodnoty v cache musí mít životnost alespoň 2*D. Hodnoty cache jsou závislé na implementaci, nicméně lze použít 32-bajtovou hodnotu X (nebo její šifrovaný ekvivalent).

- Diffie-Hellman dočasné klíče nesmí být nikdy znovu použity, aby se zabránilo kryptografickým útokům, a opětovné použití bude odmítnuto jako replay útok.

- Možnosti "KE" a "auth" musí být kompatibilní, tj. sdílené tajemství K musí mít odpovídající velikost. Pokud budou přidány další možnosti "auth", mohlo by to implicitně změnit význam příznaku "KE" pro použití jiného KDF nebo jiné velikosti ořezání.

- Bob musí ověřit, že Alicein ephemeral klíč je platný bod na křivce zde.

- Padding by měl být omezen na rozumné množství. Bob může odmítnout spojení s nadměrným paddingem. Bob specifikuje své možnosti paddingu ve zprávě 2. Směrnice pro min/max zatím nejsou stanoveny. Náhodná velikost od 0 do minimálně 31 bajtů? (Distribuce závisí na implementaci) Java implementace aktuálně omezují padding na maximálně 256 bajtů.

- Při jakékoli chybě, včetně AEAD, DH, časové značky, zjevného replay útoku nebo selhání validace klíče, musí Bob zastavit další zpracování zpráv a zavřít připojení bez odpovědi. Toto by mělo být abnormální uzavření (TCP RST). Pro odolnost proti sondování by měl Bob po selhání AEAD nastavit náhodný timeout (rozsah TBD) a poté přečíst náhodný počet bajtů (rozsah TBD), před zavřením socketu.

- Bob může provést rychlou MSB kontrolu pro platný klíč (X[31] & 0x80 == 0) před pokusem o dešifrování. Pokud je vysoký bit nastaven, implementujte odolnost proti sondování jako u selhání AEAD.

- Zmírnění DoS: DH je relativně nákladná operace. Stejně jako u předchozího NTCP protokolu by routery měly přijmout všechna nezbytná opatření k zabránění vyčerpání CPU nebo připojení. Stanovte limity na maximální aktivní připojení a maximální počet probíhajících nastavování připojení. Vynuťte časové limity čtení (jak per čtení, tak celkové pro "slowloris"). Omezte opakovaná nebo současná připojení ze stejného zdroje. Udržujte černé listiny zdrojů, které opakovaně selhávají. Neodpovídejte na selhání AEAD.

- Pro usnadnění rychlé detekce verze a handshaking musí implementace zajistit, že Alice uloží do bufferu a poté vyprázdní celý obsah první zprávy najednou, včetně paddingu. To zvyšuje pravděpodobnost, že data budou obsažena v jediném TCP paketu (pokud nejsou segmentována OS nebo middleboxy) a Bob je obdrží najednou. Navíc musí implementace zajistit, že Bob uloží do bufferu a poté vyprázdní celý obsah druhé zprávy najednou, včetně paddingu, a že Bob uloží do bufferu a poté vyprázdní celý obsah třetí zprávy najednou. To je také kvůli efektivitě a pro zajištění účinnosti náhodného paddingu.

- pole "ver": Celkový protokol Noise, rozšíření a NTCP protokol včetně specifikací payload, indikující NTCP2. Toto pole může být použito k indikaci podpory pro budoucí změny.

- Délka části 2 zprávy 3: Toto je velikost druhého AEAD rámce (včetně 16-bajtového MAC) obsahujícího Router Info Alice a volitelné vyplnění, které bude odesláno ve zprávě SessionConfirmed. Jelikož routery periodicky regenerují a znovu publikují své Router Info, velikost aktuálního Router Info se může změnit před odesláním zprávy 3. Implementace musí zvolit jednu ze dvou strategií:

a\) uložit aktuální Router Info, které bude odesláno ve zprávě 3, takže je známa velikost, a volitelně přidat místo pro padding;

b\) zvýšit specifikovanou velikost dostatečně, aby umožnila možný nárůst velikosti Router Info, a vždy přidat padding při skutečném odeslání zprávy 3. V obou případech musí délka "m3p2len" obsažená ve zprávě 1 být přesně velikostí tohoto rámce při odeslání ve zprávě 3.

- Bob musí ukončit spojení, pokud po validaci zprávy 1 a načtení paddingu zůstanou nějaká příchozí data. Neměla by existovat žádná další data od Alice, protože Bob ještě neodpověděl zprávou 2.

- Pole network ID se používá k rychlé identifikaci spojení napříč sítěmi. Pokud je toto pole nenulové a neodpovídá network ID Boba, Bob by se měl odpojit a blokovat budoucí spojení. Jakékoli spojení z testovacích sítí by mělo mít jiné ID a test selže. Od verze 0.9.42. Více informací najdete v návrhu 147.

### Funkce derivace klíče (KDF) (pro handshake zprávu 2 a zprávu 3 část 1)

```
// take h saved from message 1 KDF
// MixHash(ciphertext)
h = SHA256(h || 32 byte encrypted payload from message 1)

// MixHash(padding)
// Only if padding length is nonzero
h = SHA256(h || random padding from message 1)

This is the "e" message pattern:

Bob generates his ephemeral DH key pair e.

// h is from KDF for handshake message 1
// Bob ephemeral key Y
// MixHash(e.pubkey)
// || below means append
h = SHA256(h || e.pubkey);

// h is used as the associated data for the AEAD in message 2
// Retain the Hash h for the message 3 KDF

End of "e" message pattern.

This is the "ee" message pattern:

// DH(e, re)
Define input_key_material = 32 byte DH result of Alice's ephemeral key and Bob's ephemeral key
Set input_key_material = X25519 DH result
// overwrite Alice's ephemeral key in memory, no longer needed
// Alice:
e(public and private) = (all zeros)
// Bob:
re = (all zeros)

// MixKey(DH())

Define temp_key = 32 bytes
Define HMAC-SHA256(key, data) as in [RFC-2104]_
// Generate a temp key from the chaining key and DH result
// ck is the chaining key, from the KDF for handshake message 1
temp_key = HMAC-SHA256(ck, input_key_material)
// overwrite the DH result in memory, no longer needed
input_key_material = (all zeros)

// Output 1
// Set a new chaining key from the temp key
// byte() below means a single byte
ck =       HMAC-SHA256(temp_key, byte(0x01)).

// Output 2
// Generate the cipher key k
Define k = 32 bytes
// || below means append
// byte() below means a single byte
k =        HMAC-SHA256(temp_key, ck || byte(0x02)).
// overwrite the temp_key in memory, no longer needed
temp_key = (all zeros)

// retain the chaining key ck for message 3 KDF

End of "ee" message pattern.
```
### 2) SessionCreated

Bob posílá Alici.

Noise obsah: Bobův dočasný klíč Y Noise payload: 16 bajtový blok možností Non-noise payload: Náhodné vyplnění

(Vlastnosti zabezpečení datové části z [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs):           Authentication   Confidentiality
  <- e, ee                  2                1

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 1.
  Encryption to an ephemeral recipient.
  This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee").
  However, the sender has not authenticated the recipient,
  so this payload might be sent to any party, including an active attacker.


  "e": Bob generates a new ephemeral key pair and stores it in the e variable,
  writes the ephemeral public key as cleartext into the message buffer,
  and hashes the public key along with the old h to derive a new h.

  "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair.
  The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Hodnota Y je šifrována pro zajištění nerozlišitelnosti a jedinečnosti payload, které jsou nezbytné jako protiopatření proti DPI. K dosažení tohoto cíle používáme šifrování AES namísto složitějších a pomalejších alternativ, jako je elligator2. Asymetrické šifrování veřejným klíčem Alice routeru by bylo příliš pomalé. Šifrování AES používá hash Bob's routeru jako klíč a AES stav ze zprávy 1 (který byl inicializován s Bob's IV publikovaným v network database).

AES šifrování slouží pouze k odolnosti proti DPI. Jakákoli strana znající Bobův router hash a IV, které jsou publikovány v síťové databázi, a zachytí prvních 32 bajtů zprávy 1, může dešifrovat hodnotu Y v této zprávě.

Nezpracovaný obsah:

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
|   ChaChaPoly frame                    |
+   Encrypted and authenticated data    +
|   32 bytes                            |
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

Y :: 32 bytes, AES-256-CBC encrypted X25519 ephemeral key, little endian
        key: RH_B
        iv: Using AES state from message 1
```
Nešifrovaná data (Poly1305 auth tag není zobrazen):

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

Y :: 32 bytes, X25519 ephemeral key, little endian

options :: options block, 16 bytes, see below

padding :: Random data, 0 or more bytes.
           Total message length must be 65535 bytes or less.
           Alice and Bob will use the padding data in the KDF for message 3 part 1.
           It is authenticated so that any tampering will cause the
           next message to fail.
```
#### Poznámky

- Alice musí ověřit, že Bobův ephemeral klíč je platný bod na křivce.
- Padding by měl být omezen na rozumné množství. Alice může odmítnout spojení s nadměrným paddingem. Alice specifikuje své možnosti paddingu ve zprávě 3. Min/max pokyny budou stanoveny později. Náhodná velikost od 0 do minimálně 31 bajtů? (Distribuce závisí na implementaci)
- Při jakékoli chybě, včetně AEAD, DH, časového razítka, zjevného přehrání nebo selhání validace klíče, musí Alice zastavit další zpracování zpráv a uzavřít spojení bez odpovědi. Toto by mělo být abnormální ukončení (TCP RST).
- Pro usnadnění rychlého handshaku musí implementace zajistit, že Bob ukládá do bufferu a poté vyprázdní celý obsah první zprávy najednou, včetně paddingu. To zvyšuje pravděpodobnost, že data budou obsažena v jediném TCP paketu (pokud nejsou segmentována OS nebo middleboxy) a Alice je obdrží najednou. Toto je také pro efektivitu a k zajištění účinnosti náhodného paddingu.
- Alice musí ukončit spojení neúspěšně, pokud po validaci zprávy 2 a načtení paddingu zůstanou jakákoli příchozí data. Neměla by být žádná další data od Boba, protože Alice ještě neodpověděla zprávou 3.

Blok možností: Poznámka: Všechna pole jsou v big-endian formátu.

```
+----+----+----+----+----+----+----+----+
| Rsvd(0) | padLen  |   Reserved (0)    |
+----+----+----+----+----+----+----+----+
|        tsB        |   Reserved (0)    |
+----+----+----+----+----+----+----+----+

Reserved :: 10 bytes total, set to 0 for compatibility with future options

padLen :: 2 bytes, big endian, length of the padding, 0 or more
          Min/max guidelines TBD. Random size from 0 to 31 bytes minimum?
          (Distribution is implementation-dependent)

tsB :: 4 bytes, big endian, Unix timestamp, unsigned seconds.
       Wraps around in 2106
```
#### Poznámky

- Alice musí odmítnout připojení, kde je hodnota časového razítka příliš vzdálená od aktuálního času. Nazývejme maximální časovou odchylku "D". Alice musí udržovat lokální cache dříve použitých handshake hodnot a odmítnout duplicity, aby zabránila replay útokům. Hodnoty v cache musí mít životnost alespoň 2*D. Hodnoty cache jsou závislé na implementaci, nicméně může být použita 32-bajtová hodnota Y (nebo její zašifrovaný ekvivalent).

#### Problémy

- Zahrnout zde možnosti min/max paddingu?

### Šifrování pro část 1 handshake zprávy 3, pomocí KDF zprávy 2)

```
// take h saved from message 2 KDF
// MixHash(ciphertext)
h = SHA256(h || 24 byte encrypted payload from message 2)

// MixHash(padding)
// Only if padding length is nonzero
h = SHA256(h || random padding from message 2)
// h is used as the associated data for the AEAD in message 3 part 1, below

This is the "s" message pattern:

Define s = Alice's static public key, 32 bytes

// EncryptAndHash(s.publickey)
// EncryptWithAd(h, s.publickey)
// AEAD_ChaCha20_Poly1305(key, nonce, associatedData, data)
// k is from handshake message 1
// n is 1
ciphertext = AEAD_ChaCha20_Poly1305(k, n++, h, s.publickey)
// MixHash(ciphertext)
// || below means append
h = SHA256(h || ciphertext);

// h is used as the associated data for the AEAD in message 3 part 2

End of "s" message pattern.
```
### Funkce pro odvození klíče (KDF) (pro handshake zprávu 3 část 2)

```
This is the "se" message pattern:

// DH(s, re) == DH(e, rs)
Define input_key_material = 32 byte DH result of Alice's static key and Bob's ephemeral key
Set input_key_material = X25519 DH result
// overwrite Bob's ephemeral key in memory, no longer needed
// Alice:
re = (all zeros)
// Bob:
e(public and private) = (all zeros)

// MixKey(DH())

Define temp_key = 32 bytes
Define HMAC-SHA256(key, data) as in [RFC-2104]_
// Generate a temp key from the chaining key and DH result
// ck is the chaining key, from the KDF for handshake message 1
temp_key = HMAC-SHA256(ck, input_key_material)
// overwrite the DH result in memory, no longer needed
input_key_material = (all zeros)

// Output 1
// Set a new chaining key from the temp key
// byte() below means a single byte
ck =       HMAC-SHA256(temp_key, byte(0x01)).

// Output 2
// Generate the cipher key k
Define k = 32 bytes
// || below means append
// byte() below means a single byte
k =        HMAC-SHA256(temp_key, ck || byte(0x02)).

// h from message 3 part 1 is used as the associated data for the AEAD in message 3 part 2

// EncryptAndHash(payload)
// EncryptWithAd(h, payload)
// AEAD_ChaCha20_Poly1305(key, nonce, associatedData, data)
// n is 0
ciphertext = AEAD_ChaCha20_Poly1305(k, n++, h, payload)
// MixHash(ciphertext)
// || below means append
h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF
// retain the hash h for the data phase Additional Symmetric Key (SipHash) KDF

End of "se" message pattern.

// overwrite the temp_key in memory, no longer needed
temp_key = (all zeros)
```
### 3) SessionConfirmed

Alice posílá Bobovi.

Noise obsah: Alice's static key Noise payload: Alice's RouterInfo a náhodné vyplnění Non-noise payload: žádný

(Bezpečnostní vlastnosti užitečného zatížení z [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs):           Authentication   Confidentiality
  -> s, se                  2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).  The
  sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key
  pair.  Assuming the corresponding private keys are secure, this
  authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.  This payload is
  encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static
  DH with the recipient's static key pair.  Assuming the ephemeral private
  keys are secure, and the recipient is not being actively impersonated by an
  attacker that has stolen its static private key, this payload cannot be
  decrypted.

  "s": Alice writes her static public key from the s variable into the
  message buffer, encrypting it, and hashes the output along with the old h
  to derive a new h.

  "se": A DH is performed between the Alice's static key pair and the Bob's
  ephemeral key pair.  The result is hashed along with the old ck to derive a
  new ck and k, and n is set to zero.
```
Toto obsahuje dva ChaChaPoly rámce. První je Alicin zašifrovaný statický veřejný klíč. Druhý je Noise payload: Alicina zašifrovaná RouterInfo, volitelné možnosti a volitelné odsazení. Používají různé klíče, protože funkce MixKey() je volána mezi nimi.

Nezpracovaný obsah:

```
+----+----+----+----+----+----+----+----+
|                                       |
+   ChaChaPoly frame (48 bytes)         +
|   Encrypted and authenticated         |
+   Alice static key S                  +
|      (32 bytes)                       |
+                                       +
|     k defined in KDF for message 2    |
+     n = 1                             +
|     see KDF for associated data       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+     Length specified in message 1     +
|                                       |
+   ChaChaPoly frame                    +
|   Encrypted and authenticated         |
+                                       +
|       Alice RouterInfo                |
+       using block format 2            +
|       Alice Options (optional)        |
+       using block format 1            +
|       Arbitrary padding               |
+       using block format 254          +
|                                       |
+                                       +
| k defined in KDF for message 3 part 2 |
+     n = 0                             +
|     see KDF for associated data       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, ChaChaPoly encrypted Alice's X25519 static key, little endian
     inside 48 byte ChaChaPoly frame
```
Nešifrovaná data (Poly1305 autentifikační značky nejsou zobrazeny):

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|              S                        |
+       Alice static key                +
|          (32 bytes)                   |
+                                       +
|                                       |
+                                       +
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                                       |
+                                       +
|       Alice RouterInfo block          |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+       Optional Options block          +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+       Optional Padding block          +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, Alice's X25519 static key, little endian
```
#### Poznámky

- Bob musí provést obvyklou validaci Router Info. Ujistit se, že typ podpisu je podporován, ověřit podpis, ověřit, že časové razítko je v mezích, a jakékoli další potřebné kontroly.

- Bob musí ověřit, že Alicin statický klíč přijatý v prvním rámci odpovídá statickému klíči v Router Info. Bob musí nejprve vyhledat v Router Info adresu NTCP nebo NTCP2 Router Address s odpovídající volbou verze (v). Viz sekce Published Router Info a Unpublished Router Info níže.

- Pokud má Bob starší verzi RouterInfo Alice ve své netdb, ověř, že statický klíč v router info je stejný v obou verzích, pokud je přítomen, a pokud je starší verze méně než XXX stará (viz čas rotace klíčů níže)

- Bob musí zde ověřit, že statický klíč Alice je platný bod na křivce.

- Měly by být zahrnuty možnosti pro specifikaci parametrů paddingu.

- Při jakékoli chybě, včetně selhání validace AEAD, RI, DH, časové známky nebo klíče, musí Bob zastavit další zpracování zpráv a uzavřít spojení bez odpovědi. Mělo by se jednat o abnormální uzavření (TCP RST).

- Pro usnadnění rychlého handshake musí implementace zajistit, že Alice uloží do bufferu a poté odešle celý obsah třetí zprávy najednou, včetně obou AEAD rámců. To zvyšuje pravděpodobnost, že data budou obsažena v jediném TCP paketu (pokud nebudou segmentována OS nebo middleboxy) a Bob je přijme všechna najednou. Toto je také z důvodu efektivity a pro zajištění účinnosti náhodného paddingu.

- Délka rámce části 2 zprávy 3: Délku tohoto rámce (včetně MAC) posílá Alice ve zprávě 1. Viz tato zpráva pro důležité poznámky o poskytnutí dostatečného prostoru pro padding.

- Obsah rámce části 2 zprávy 3: Formát tohoto rámce je stejný jako formát rámců datové fáze, s výjimkou toho, že délku rámce posílá Alice ve zprávě 1. Viz níže pro formát rámce datové fáze. Rámec musí obsahovat 1 až 3 bloky v následujícím pořadí:

1)  Blok Router Info Alice (povinný)   2)  Blok možností (volitelný)

3\) Blok výplně (volitelný) Tento rámec nesmí nikdy obsahovat žádný jiný typ bloku.

- Odsazení části 2 zprávy 3 není vyžadováno, pokud Alice připojí rámec datové fáze (volitelně obsahující odsazení) na konec zprávy 3 a odešle oboje najednou, protože pozorovateli se to bude jevit jako jeden velký proud bajtů. Jelikož Alice obecně, ale ne vždy, má I2NP zprávu k odeslání Bobovi (proto se k němu připojila), je toto doporučená implementace z důvodu efektivity a k zajištění účinnosti náhodného odsazení.

- Celková délka obou AEAD rámců zprávy 3 (část 1 a 2) je 65535 bajtů; část 1 má 48 bajtů, takže maximální délka rámce části 2 je 65487; maximální délka prostého textu části 2 bez MAC je 65471.

### Funkce odvození klíčů (KDF) (pro fázi dat)

Fáze dat používá vstup asociovaných dat nulové délky.

KDF generuje dva šifrovací klíče k_ab a k_ba z řetězového klíče ck, pomocí HMAC-SHA256(key, data) jak je definováno v [RFC-2104](https://tools.ietf.org/html/rfc2104). Toto je funkce Split(), přesně jak je definována ve specifikaci Noise.

```
ck = from handshake phase

// k_ab, k_ba = HKDF(ck, zerolen)
// ask_master = HKDF(ck, zerolen, info="ask")

// zerolen is a zero-length byte array
temp_key = HMAC-SHA256(ck, zerolen)
// overwrite the chaining key in memory, no longer needed
ck = (all zeros)

// Output 1
// cipher key, for Alice transmits to Bob (Noise doesn't make clear which is which, but Java code does)
k_ab =   HMAC-SHA256(temp_key, byte(0x01)).

// Output 2
// cipher key, for Bob transmits to Alice (Noise doesn't make clear which is which, but Java code does)
k_ba =   HMAC-SHA256(temp_key, k_ab || byte(0x02)).


KDF for SipHash for length field:
Generate an Additional Symmetric Key (ask) for SipHash
SipHash uses two 8-byte keys (big endian) and 8 byte IV for first data.

// "ask" is 3 bytes, US-ASCII, no null termination
ask_master = HMAC-SHA256(temp_key, "ask" || byte(0x01))
// sip_master = HKDF(ask_master, h || "siphash")
// "siphash" is 7 bytes, US-ASCII, no null termination
// overwrite previous temp_key in memory
// h is from KDF for message 3 part 2
temp_key = HMAC-SHA256(ask_master, h || "siphash")
// overwrite ask_master in memory, no longer needed
ask_master = (all zeros)
sip_master = HMAC-SHA256(temp_key, byte(0x01))

Alice to Bob SipHash k1, k2, IV:
// sipkeys_ab, sipkeys_ba = HKDF(sip_master, zerolen)
// overwrite previous temp_key in memory
temp_key = HMAC-SHA256(sip_master, zerolen)
// overwrite sip_master in memory, no longer needed
sip_master = (all zeros)

sipkeys_ab = HMAC-SHA256(temp_key, byte(0x01)).
sipk1_ab = sipkeys_ab[0:7], little endian
sipk2_ab = sipkeys_ab[8:15], little endian
sipiv_ab = sipkeys_ab[16:23]

Bob to Alice SipHash k1, k2, IV:

sipkeys_ba = HMAC-SHA256(temp_key, sipkeys_ab || byte(0x02)).
sipk1_ba = sipkeys_ba[0:7], little endian
sipk2_ba = sipkeys_ba[8:15], little endian
sipiv_ba = sipkeys_ba[16:23]

// overwrite the temp_key in memory, no longer needed
temp_key = (all zeros)
```
### 4) Fáze dat

Noise payload: Jak je definován níže, včetně náhodného paddingu Non-noise payload: žádný

Počínaje 2. částí zprávy 3 jsou všechny zprávy uvnitř autentizovaného a šifrovaného ChaChaPoly "rámce" s předřazenou dvoubajtovou zastřenou délkou. Veškeré vyplnění je uvnitř rámce. Uvnitř rámce je standardní formát s nulovými nebo více "bloky". Každý blok má jednobajtový typ a dvoubajtovou délku. Typy zahrnují datum/čas, I2NP zprávu, možnosti, ukončení a vyplnění.

Poznámka: Bob může, ale není povinen, poslat své RouterInfo Alici jako svou první zprávu Alici ve fázi dat.

(Vlastnosti zabezpečení užitečného zatížení z [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs):           Authentication   Confidentiality
  <-                        2                5
  ->                        2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.
  This payload is encrypted based on an ephemeral-ephemeral DH as well as
  an ephemeral-static DH with the recipient's static key pair.
  Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated
  by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### Poznámky

- Pro efektivitu a k minimalizaci identifikace pole délky musí implementace zajistit, že odesílatel ukládá do vyrovnávací paměti a poté vyprazdňuje celý obsah datových zpráv najednou, včetně pole délky a AEAD rámce. To zvyšuje pravděpodobnost, že data budou obsažena v jediném TCP paketu (pokud nejsou segmentována OS nebo middlewarovými zařízeními) a budou přijata najednou druhou stranou. To je také pro efektivitu a k zajištění účinnosti náhodného doplňování.
- Router může zvolit ukončení relace při AEAD chybě, nebo může pokračovat v pokusech o komunikaci. Pokud pokračuje, router by měl ukončit po opakovaných chybách.

#### SipHash zamaskovaná délka

Reference: [SipHash](https://www.131002.net/siphash/)

Jakmile obě strany dokončí handshake, přenášejí datové části, které jsou poté šifrovány a autentizovány v ChaChaPoly "rámcích".

Každý rámec je předcházen dvoubajtovou délkou v pořadí big endian. Tato délka specifikuje počet následujících šifrovaných bajtů rámce, včetně MAC. Aby se zabránilo přenosu identifikovatelných polí délky v datovém toku, délka rámce je obfuskována pomocí XOR s maskou odvozenou ze SipHash, inicializovanou z KDF datové fáze. Všimněte si, že oba směry mají jedinečné SipHash klíče a IV z KDF.

```
    sipk1, sipk2 = The SipHash keys from the KDF.  (two 8-byte long integers)
    IV[0] = sipiv = The SipHash IV from the KDF. (8 bytes)
    length is big endian.
    For each frame:
      IV[n] = SipHash-2-4(sipk1, sipk2, IV[n-1])
      Mask[n] = First 2 bytes of IV[n]
      obfuscatedLength = length ^ Mask[n]

    The first length output will be XORed with with IV[1].
```
Příjemce má identické SipHash klíče a IV. Dekódování délky se provádí odvozením masky použité k maskování délky a XOR operací s zkráceným digestem k získání délky rámce. Délka rámce je celková délka šifrovaného rámce včetně MAC.

#### Poznámky

- Pokud používáte funkci knihovny SipHash, která vrací unsigned long integer, použijte dva nejméně významné bajty jako Mask. Převeďte long integer na další IV jako little endian.

#### Surový obsah

```
+----+----+----+----+----+----+----+----+
|obf size |                             |
+----+----+                             +
|                                       |
+   ChaChaPoly frame                    +
|   Encrypted and authenticated         |
+   key is k_ab for Alice to Bob        +
|   key is k_ba for Bob to Alice        |
+   as defined in KDF for data phase    +
|   n starts at 0 and increments        |
+   for each frame in that direction    +
|   no associated data                  |
+   16 bytes minimum                    +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

obf size :: 2 bytes length obfuscated with SipHash
            when de-obfuscated: 16 - 65535

Minimum size including length field is 18 bytes.
Maximum size including length field is 65537 bytes.
Obfuscated length is 2 bytes.
Maximum ChaChaPoly frame is 65535 bytes.
```
#### Poznámky

- Jelikož příjemce musí získat celý rámec pro kontrolu MAC, doporučuje se, aby odesílatel omezil rámce na několik KB spíše než maximalizoval velikost rámce. To minimalizuje latenci u příjemce.

#### Nešifrovaná data

V šifrovaném rámci je nula nebo více bloků. Každý blok obsahuje jednobytový identifikátor, dvoubajtovou délku a nula nebo více bajtů dat.

Pro rozšiřitelnost musí příjemci ignorovat bloky s neznámými identifikátory a zacházet s nimi jako s výplní.

Šifrovaná data mají maximálně 65535 bytů, včetně 16-bytové ověřovací hlavičky, takže maximální nešifrovaná data jsou 65519 bytů.

(Poly1305 autentizační tag není zobrazen):

```
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
~               .   .   .               ~

blk :: 1 byte
       0 for datetime
       1 for options
       2 for RouterInfo
       3 for I2NP message
       4 for termination
       224-253 reserved for experimental features
       254 for padding
       255 reserved for future extension
size :: 2 bytes, big endian, size of data to follow, 0 - 65516
data :: the data

Maximum ChaChaPoly frame is 65535 bytes.
Poly1305 tag is 16 bytes
Maximum total block size is 65519 bytes
Maximum single block size is 65519 bytes
Block type is 1 byte
Block length is 2 bytes
Maximum single block data size is 65516 bytes.
```
#### Pravidla řazení bloků

V handshake zprávě 3 část 2 musí být pořadí: RouterInfo, následované Options pokud jsou přítomny, následované Padding pokud je přítomno. Žádné jiné bloky nejsou povoleny.

Ve fázi dat není pořadí specifikováno, kromě následujících požadavků: Padding, je-li přítomen, musí být posledním blokem. Termination, je-li přítomen, musí být posledním blokem kromě Padding.

V jednom rámci může být více I2NP bloků. Více Padding bloků není v jednom rámci povoleno. Ostatní typy bloků pravděpodobně nebudou mít více bloků v jednom rámci, ale není to zakázáno.

#### DatumČas

Speciální případ pro synchronizaci času:

```
+----+----+----+----+----+----+----+
| 0  |    4    |     timestamp     |
+----+----+----+----+----+----+----+

blk :: 0
size :: 2 bytes, big endian, value = 4
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
```
POZNÁMKA: Implementace musí zaokrouhlovat na nejbližší sekundu, aby se zabránilo časovému posunu v síti.

#### Možnosti

Předat aktualizované možnosti. Možnosti zahrnují: Minimální a maximální padding.

Blok opcí bude mít proměnnou délku.

```
+----+----+----+----+----+----+----+----+
| 1  |  size   |tmin|tmax|rmin|rmax|tdmy|
+----+----+----+----+----+----+----+----+
|tdmy|  rdmy   |  tdelay |  rdelay |    |
~----+----+----+----+----+----+----+    ~
|              more_options             |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 1
size :: 2 bytes, big endian, size of options to follow, 12 bytes minimum

tmin, tmax, rmin, rmax :: requested padding limits
    tmin and rmin are for desired resistance to traffic analysis.
    tmax and rmax are for bandwidth limits.
    tmin and tmax are the transmit limits for the router sending this options block.
    rmin and rmax are the receive limits for the router sending this options block.
    Each is a 4.4 fixed-point float representing 0 to 15.9375
    (or think of it as an unsigned 8-bit integer divided by 16.0).
    This is the ratio of padding to data. Examples:
    Value of 0x00 means no padding
    Value of 0x01 means add 6 percent padding
    Value of 0x10 means add 100 percent padding
    Value of 0x80 means add 800 percent (8x) padding
    Alice and Bob will negotiate the minimum and maximum in each direction.
    These are guidelines, there is no enforcement.
    Sender should honor receiver's maximum.
    Sender may or may not honor receiver's minimum, within bandwidth constraints.

tdmy: Max dummy traffic willing to send, 2 bytes big endian, bytes/sec average
rdmy: Requested dummy traffic, 2 bytes big endian, bytes/sec average
tdelay: Max intra-message delay willing to insert, 2 bytes big endian, msec average
rdelay: Requested intra-message delay, 2 bytes big endian, msec average

Padding distribution specified as additional parameters?
Random delay specified as additional parameters?

more_options :: Format TBD
```
#### Problémy s možnostmi

- Formát opcí je dosud neurčen (TBD).
- Vyjednávání opcí je dosud neurčeno (TBD).

#### RouterInfo

Předat Alice RouterInfo Bobovi. Používá se ve zprávě handshake 3 část 2. Předat Alice RouterInfo Bobovi, nebo Bobovo Alice. Používá se volitelně ve fázi dat.

```
+----+----+----+----+----+----+----+----+
| 2  |  size   |flg |    RouterInfo     |
+----+----+----+----+                   +
| (Alice RI in handshake msg 3 part 2)  |
~ (Alice, Bob, or third-party           ~
|  RI in data phase)                    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 2
size :: 2 bytes, big endian, size of flag + router info to follow
flg :: 1 byte flags
       bit order: 76543210
       bit 0: 0 for local store, 1 for flood request
       bits 7-1: Unused, set to 0 for future compatibility
routerinfo :: Alice's or Bob's RouterInfo
```
#### Poznámky

- Při použití ve fázi dat musí příjemce (Alice nebo Bob) ověřit, že se jedná o stejný Router Hash jako původně odeslaný (pro Alice) nebo odeslaný k (pro Bob). Poté s ním nakládat jako s lokální I2NP DatabaseStore Message. Ověřit podpis, ověřit novější časové razítko a uložit do lokální netDb. Pokud je flag bit 0 roven 1 a přijímající strana je floodfill, nakládat s ním jako s DatabaseStore Message s nenulovým reply tokenem a zaplavit ho do nejbližších floodfillů.
- Router Info NENÍ komprimován pomocí gzip (na rozdíl od DatabaseStore Message, kde je)
- Flooding nesmí být požadován, pokud v RouterInfo nejsou publikované RouterAddresses. Přijímající router nesmí zaplavit RouterInfo, pokud v něm nejsou publikované RouterAddresses.
- Implementátoři musí zajistit, že při čtení bloku nezpůsobí poškozená nebo škodlivá data přečtení za hranice následujícího bloku.
- Tento protokol neposkytuje potvrzení, že RouterInfo byl přijat, uložen nebo zaplavený (ani ve fázi handshake, ani ve fázi dat). Pokud je potvrzení žádoucí a příjemce je floodfill, měl by odesílatel místo toho poslat standardní I2NP DatabaseStoreMessage s reply tokenem.

#### Problémy

- Mohlo by být také použito ve fázi dat, namísto I2NP DatabaseStoreMessage. Například Bob by ji mohl použít k zahájení fáze dat.
- Je povoleno, aby tato zpráva obsahovala RI pro routery jiné než původce, jako obecná náhrada za DatabaseStoreMessages, např. pro flooding pomocí floodfills?

#### I2NP zpráva

Jediná I2NP zpráva s upravenou hlavičkou. I2NP zprávy nesmí být fragmentovány napříč bloky nebo napříč ChaChaPoly rámci.

Toto používá prvních 9 bytů ze standardní NTCP I2NP hlavičky a odstraňuje posledních 7 bytů hlavičky následovně: zkrátí expiraci z 8 na 4 byty (sekundy místo milisekund, stejně jako u SSU), odstraní 2-bytovou délku (použije velikost bloku - 9) a odstraní jednobytový SHA256 kontrolní součet.

```
+----+----+----+----+----+----+----+----+
| 3  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |     message       |
+----+----+----+----+                   +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 3
size :: 2 bytes, big endian, size of type + msg id + exp + message to follow
        I2NP message body size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: I2NP message body
```
#### Poznámky

- Implementátoři musí zajistit, že při čtení bloku nebudou poškozená nebo škodlivá data způsobovat, že čtení přesáhne do následujícího bloku.

#### Ukončení

Noise doporučuje explicitní zprávu o ukončení. Původní NTCP ji nemá. Ukončit spojení. Toto musí být posledním ne-výplňovým blokem v rámci.

```
+----+----+----+----+----+----+----+----+
| 4  |  size   |    valid data frames   |
+----+----+----+----+----+----+----+----+
    received   | rsn|     addl data     |
+----+----+----+----+                   +
~               .   .   .               ~
+----+----+----+----+----+----+----+----+

blk :: 4
size :: 2 bytes, big endian, value = 9 or more
valid data frames received :: The number of valid AEAD data phase frames received
                              (current receive nonce value)
                              0 if error occurs in handshake phase
                              8 bytes, big endian
rsn :: reason, 1 byte:
       0: normal close or unspecified
       1: termination received
       2: idle timeout
       3: router shutdown
       4: data phase AEAD failure
       5: incompatible options
       6: incompatible signature type
       7: clock skew
       8: padding violation
       9: AEAD framing error
       10: payload format error
       11: message 1 error
       12: message 2 error
       13: message 3 error
       14: intra-frame read timeout
       15: RI signature verification fail
       16: s parameter missing, invalid, or mismatched in RouterInfo
       17: banned
addl data :: optional, 0 or more bytes, for future expansion, debugging,
             or reason text.
             Format unspecified and may vary based on reason code.
```
#### Poznámky

Ne všechny důvody mohou být skutečně použity, závisí na implementaci. Selhání handshake obecně povede k uzavření s TCP RST namísto toho. Viz poznámky v sekcích handshake zpráv výše. Další uvedené důvody jsou pro konzistenci, logování, ladění, nebo pokud se změní zásady.

#### Výplň

Toto je pro výplň uvnitř AEAD rámců. Výplň pro zprávy 1 a 2 je mimo AEAD rámce. Veškerá výplň pro zprávu 3 a datovou fázi je uvnitř AEAD rámců.

Padding uvnitř AEAD by měl zhruba odpovídat vyjednaným parametrům. Bob odeslal své požadované tx/rx min/max parametry ve zprávě 2. Alice odeslala své požadované tx/rx min/max parametry ve zprávě 3. Aktualizované možnosti mohou být odeslány během datové fáze. Viz informace o bloku možností výše.

Pokud je přítomen, musí být posledním blokem v rámci.

```
+----+----+----+----+----+----+----+----+
|254 |  size   |      padding           |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 254
size :: 2 bytes, big endian, size of padding to follow
padding :: random data
```
#### Poznámky

- Velikost = 0 je povolena.
- Strategie paddingu TBD.
- Minimální padding TBD.
- Rámce pouze s paddingem jsou povoleny.
- Výchozí hodnoty paddingu TBD.
- Viz blok options pro vyjednání parametrů paddingu
- Viz blok options pro parametry min/max paddingu
- Noise omezuje zprávy na 64KB. Pokud je nutný větší padding, pošlete více rámců.
- Odpověď routeru na porušení vyjednaného paddingu je závislá na implementaci.

#### Ostatní typy bloků

Implementace by měly neznámé typy bloků ignorovat kvůli dopředné kompatibilitě, kromě zprávy 3 část 2, kde neznámé bloky nejsou povoleny.

#### Budoucí práce

- Délka paddingu má být rozhodována buď na základě jednotlivých zpráv a odhadů distribuce délky, nebo by měly být přidány náhodné zpoždění. Tato protiopatření mají být zahrnuta pro odolnost proti DPI, protože velikosti zpráv by jinak prozradily, že I2P provoz je přenášen transportním protokolem. Přesné schéma paddingu je oblastí budoucí práce.

### 5) Ukončení

Spojení mohou být ukončena pomocí normálního nebo abnormálního uzavření TCP socketu, nebo, jak Noise doporučuje, explicitní ukončovací zprávou. Explicitní ukončovací zpráva je definována ve fázi dat výše.

Při jakémkoliv normálním nebo abnormálním ukončení by routery měly vynulovat veškerá dočasná data v paměti, včetně dočasných klíčů handshake, symetrických kryptografických klíčů a souvisejících informací.

## Publikované informace o routeru

### Možnosti

Od verze 0.9.50 je v NTCP2 adresách podporována možnost "caps", podobně jako u SSU. V možnosti "caps" může být publikována jedna nebo více schopností. Schopnosti mohou být v libovolném pořadí, ale "46" je doporučené pořadí pro konzistenci napříč implementacemi. Existují dvě definované schopnosti:

4: Označuje schopnost odchozího IPv4. Pokud je IP adresa publikována v poli host, tato schopnost není nutná. Pokud je router skrytý, nebo NTCP2 je pouze odchozí, '4' a '6' mohou být kombinovány v jedné adrese.

6: Označuje schopnost odchozího IPv6. Pokud je IP adresa publikována v poli host, tato schopnost není nutná. Pokud je router skrytý nebo NTCP2 funguje pouze pro odchozí spojení, '4' a '6' mohou být kombinovány v jedné adrese.

### Publikované adresy

Publikovaná RouterAddress (část RouterInfo) bude mít identifikátor protokolu buď "NTCP" nebo "NTCP2".

RouterAddress musí obsahovat možnosti "host" a "port", stejně jako v současném NTCP protokolu.

RouterAddress musí obsahovat tři možnosti pro indikaci podpory NTCP2:

- s=(Base64 klíč) Aktuální Noise statický veřejný klíč (s) pro tuto RouterAddress. Kódován v Base 64 pomocí standardní I2P Base 64 abecedy. 32 bytů v binární podobě, 44 bytů jako Base 64 kódovaný, little-endian X25519 veřejný klíč.
- i=(Base64 IV) Aktuální IV pro šifrování hodnoty X ve zprávě 1 pro tuto RouterAddress. Kódován v Base 64 pomocí standardní I2P Base 64 abecedy. 16 bytů v binární podobě, 24 bytů jako Base 64 kódovaný, big-endian.
- v=2 Aktuální verze (2). Když je publikována jako "NTCP", je implicitně podporována také verze 1. Podpora budoucích verzí bude pomocí hodnot oddělených čárkami, např. v=2,3 Implementace by měla ověřit kompatibilitu, včetně více verzí, pokud je přítomna čárka. Verze oddělené čárkami musí být v číselném pořadí.

Alice musí ověřit, že jsou všechny tři možnosti přítomny a platné před připojením pomocí protokolu NTCP2.

Když je publikován jako "NTCP" s možnostmi "s", "i" a "v", router musí přijímat příchozí spojení na daném hostiteli a portu pro protokoly NTCP i NTCP2 a automaticky detekovat verzi protokolu.

Když je publikováno jako "NTCP2" s možnostmi "s", "i" a "v", router přijímá příchozí spojení na daném hostiteli a portu pouze pro protokol NTCP2.

Pokud router podporuje jak NTCP1, tak NTCP2 připojení, ale neimplementuje automatickou detekci verze pro příchozí připojení, musí inzerovat jak "NTCP", tak "NTCP2" adresy a zahrnout NTCP2 možnosti pouze do "NTCP2" adresy. Router by měl nastavit nižší hodnotu nákladů (vyšší prioritu) v "NTCP2" adrese než v "NTCP" adrese, takže NTCP2 je upřednostňováno.

Pokud je v rámci stejného RouterInfo publikováno více NTCP2 RouterAddresses (buď jako "NTCP" nebo "NTCP2") pro dodatečné IP adresy nebo porty, všechny adresy specifikující stejný port musí obsahovat identické NTCP2 možnosti a hodnoty. Zejména všechny musí obsahovat stejný statický klíč a iv.

### Nepublikovaná NTCP2 adresa

Pokud Alice nepublikuje svou NTCP2 adresu (jako "NTCP" nebo "NTCP2") pro příchozí spojení, musí publikovat "NTCP2" router adresu obsahující pouze její statický klíč a NTCP2 verzi, aby Bob mohl validovat klíč poté, co obdrží Alice RouterInfo ve zprávě 3 část 2.

- s=(Base64 klíč) Jak je definováno výše pro publikované adresy.
- v=2 Jak je definováno výše pro publikované adresy.

Tato router adresa nebude obsahovat možnosti "i", "host" nebo "port", protože tyto nejsou vyžadovány pro odchozí NTCP2 připojení. Publikované náklady pro tuto adresu nejsou striktně důležité, jelikož je pouze příchozí; může však být užitečné pro ostatní routery, pokud jsou náklady nastaveny výše (nižší priorita) než u ostatních adres. Navrhovaná hodnota je 14.

Alice může také jednoduše přidat možnosti "s" a "v" k existující publikované "NTCP" adrese.

### Rotace veřejného klíče a IV

Kvůli ukládání RouterInfo do cache nesmí routery rotovat statický veřejný klíč nebo IV, dokud je router v provozu, ať už je v publikované adrese nebo ne. Routery musí tento klíč a IV trvale uložit pro opětovné použití po okamžitém restartu, aby příchozí spojení nadále fungovala a časy restartů nebyly odhaleny. Routery musí trvale uložit nebo jinak určit čas posledního vypnutí, aby mohl být při spuštění vypočítán předchozí čas nečinnosti.

V závislosti na obavách ohledně odhalení časů restartů mohou routery rotovat tento klíč nebo IV při spuštění, pokud byl router předtím vypnutý po nějakou dobu (alespoň pár hodin).

Pokud má router jakékoliv publikované NTCP2 RouterAddresses (jako NTCP nebo NTCP2), minimální doba výpadku před rotací by měla být mnohem delší, například jeden měsíc, pokud se nezměnila místní IP adresa nebo router neprovádí "rekeys".

Pokud má router jakékoli publikované SSU RouterAddresses, ale ne NTCP2 (jako NTCP nebo NTCP2), měla by být minimální doba nečinnosti před rotací delší, například jeden den, pokud se nezměnila místní IP adresa nebo router neprovedl "rekeys". To platí i v případě, že publikovaná SSU adresa má introducery.

Pokud router nemá žádné publikované RouterAddresses (NTCP, NTCP2, nebo SSU), minimální doba výpadku před rotací může být pouhé dvě hodiny, i když se IP adresa změní, pokud router neprovedl "rekeys" (obnovu klíčů).

Pokud router provede "rekeys" na jiný Router Hash, měl by také vygenerovat nový noise key a IV.

Implementace si musí být vědomy toho, že změna statického veřejného klíče nebo IV znemožní příchozí NTCP2 spojení od routerů, které mají v cache starší RouterInfo. Publikování RouterInfo, výběr tunnel peerů (včetně OBGW i IB nejbližšího hopu), výběr zero-hop tunnelů, výběr transportu a další implementační strategie to musí zohlednit.

Rotace IV podléhá stejným pravidlům jako rotace klíčů, s výjimkou toho, že IV nejsou přítomny kromě publikovaných RouterAddresses, takže neexistuje žádné IV pro skryté nebo firewallované routery. Pokud se něco změní (verze, klíč, možnosti?), doporučuje se, aby se IV také změnilo.

Poznámka: Minimální doba výpadku před rekeying může být upravena pro zajištění zdraví sítě a pro zabránění reseeding routerem, který je vypnutý po středně dlouhou dobu.

## Detekce verze

Když je publikován jako "NTCP", router musí automaticky detekovat verzi protokolu pro příchozí spojení.

Tato detekce závisí na implementaci, ale zde je obecné vodítko.

Pro detekci verze příchozího NTCP spojení postupuje Bob následovně:

- Počkejte na alespoň 64 bajtů (minimální velikost NTCP2 zprávy 1)

- Pokud jsou počáteční přijatá data 288 nebo více bajtů, příchozí spojení je verze 1.

- Pokud méně než 288 bytů, buď

> - Počkejte krátkou dobu na více dat (dobrá strategie před širokou adopcí NTCP2), pokud je celkem přijato alespoň 288 bajtů, je to NTCP 1.   >   > - Zkuste první fáze dekódování jako verze 2, pokud selže, počkejte krátkou dobu na více dat (dobrá strategie po široké adopci NTCP2)   >   >   > - Dešifrujte prvních 32 bajtů (klíč X) paketu SessionRequest pomocí AES-256 s klíčem RH_B.   >   > - Ověřte platný bod na křivce. Pokud selže, počkejte krátkou dobu na více dat pro NTCP 1   >   > - Ověřte AEAD rámec. Pokud selže, počkejte krátkou dobu na více dat pro NTCP 1

Upozorňujeme, že změny nebo dodatečné strategie mohou být doporučeny, pokud detekujeme aktivní útoky TCP segmentace na NTCP 1.

Pro usnadnění rychlé detekce verze a handshake musí implementace zajistit, aby Alice uložila do bufferu a poté najednou vyprázdnila celý obsah první zprávy včetně paddingu. Tím se zvyšuje pravděpodobnost, že data budou obsažena v jediném TCP paketu (pokud nebudou segmentována OS nebo middleboxy) a Bob je obdrží najednou. Toto je také kvůli efektivitě a k zajištění účinnosti náhodného paddingu. Toto platí jak pro NTCP, tak pro NTCP2 handshake.

## Varianty, záložní řešení a obecné problémy

- Pokud Alice i Bob podporují NTCP2, Alice by se měla připojit pomocí NTCP2.
- Pokud se Alice nepodaří připojit k Bobovi pomocí NTCP2 z jakéhokoli důvodu, připojení selže. Alice nesmí opakovat pokus pomocí NTCP 1.

## Pokyny pro zkosení hodin

Časové značky peerů jsou zahrnuty v prvních dvou handshake zprávách, Session Request a Session Created. Časový posun mezi dvěma peery větší než +/- 60 sekund je obecně fatální. Pokud si Bob myslí, že jeho místní hodiny jsou špatné, může upravit své hodiny pomocí vypočítaného posunu nebo nějakého externího zdroje. Jinak by Bob měl odpovědět s Session Created i když je maximální posun překročen, spíše než jednoduše ukončit spojení. To umožňuje Alice získat Bobovu časovou značku a vypočítat posun, a pokud je to nutné, podniknout akci. Bob v tomto bodě nemá identitu Alice routeru, ale kvůli úspoře zdrojů může být žádoucí, aby Bob na určitou dobu zakázal příchozí spojení z Alice IP adresy, nebo po opakovaných pokusech o spojení s nadměrným posunem.

Alice by měla upravit vypočítaný posun hodin odečtením poloviny RTT. Pokud si Alice myslí, že její lokální hodiny jsou špatné, může upravit své hodiny pomocí vypočítaného posunu nebo nějakého externího zdroje. Pokud si Alice myslí, že Bobovy hodiny jsou špatné, může Boba zakázat na určité časové období. V obou případech by Alice měla spojení ukončit.

Pokud Alice odpoví s Session Confirmed (pravděpodobně proto, že skew je velmi blízko k limitu 60s a výpočty Alice a Boba nejsou úplně stejné kvůli RTT), Bob by měl upravit vypočítaný clock skew odečtením poloviny RTT. Pokud upravený clock skew překročí maximum, Bob by měl poté odpovědět zprávou Disconnect obsahující důvodový kód clock skew a uzavřít spojení. V tomto bodě má Bob identitu routeru Alice a může Alice zakázat na určité časové období.

## Reference

- [Společné struktury](/docs/specs/common-structures)
- [I2NP](/docs/specs/i2np)
- [Síťová databáze](/docs/overview/network-database)
- [NOISE - Noise Protocol Framework](https://noiseprotocol.org/noise.html)
- [NTCP](/docs/transport/ntcp)
- [Prop104](/proposals/104-tls-transport)
- [Prop109](/proposals/109-pt-transport)
- [Prop111](/proposals/111-ntcp-2)
- [RFC-2104 - HMAC](https://tools.ietf.org/html/rfc2104)
- [RFC-3526 - DH Groups](https://tools.ietf.org/html/rfc3526)
- [RFC-6151](https://tools.ietf.org/html/rfc6151)
- [RFC-7539 - ChaCha20-Poly1305](https://tools.ietf.org/html/rfc7539)
- [RFC-7748 - X25519](https://tools.ietf.org/html/rfc7748)
- [RFC-7905](https://tools.ietf.org/html/rfc7905)
- [SipHash](https://www.131002.net/siphash/)
- [SSU](/docs/transport/ssu)
- **[STS]** Diffie, W.; van Oorschot P. C.; Wiener M. J., Autentizace a autentizované výměny klíčů
