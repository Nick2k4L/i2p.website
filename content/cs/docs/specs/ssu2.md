---
title: "Specifikace SSU2"
description: "Secure Semi-Reliable UDP Transport Protocol Version 2"
slug: "ssu2"
category: "Transporty"
lastUpdated: "2026-03"
accurateFor: "0.9.69"
---

## Stav

Podstatně dokončeno. Viz [Prop159](/proposals/159-ssu2) pro další pozadí a cíle, včetně bezpečnostní analýzy, modelů hrozeb, přehledu bezpečnosti a problémů SSU 1 a úryvků ze specifikací QUIC.

Plán zavádění:

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
Základní relace zahrnuje handshake a datovou fázi. Rozšířený protokol zahrnuje relay a peer test.

## Přehled

Tato specifikace definuje protokol pro autentizované dohodnutí klíčů za účelem zlepšení odolnosti [SSU](/docs/transport/ssu) vůči různým formám automatizované identifikace a útoků.

Stejně jako u jiných I2P transportů je SSU2 definován pro point-to-point (router-to-router) přenos I2NP zpráv. Není to univerzální datová roura. Stejně jako [SSU](/docs/transport/ssu) také poskytuje dvě dodatečné služby: Relaying pro průchod NAT a Peer Testing pro zjištění příchozí dostupnosti. Poskytuje také třetí službu, která není v SSU, pro migraci spojení, když peer změní IP nebo port.

## Přehled designu

### Shrnutí

Spoléháme se na několik existujících protokolů, jak v rámci I2P, tak na vnější standardy, pro inspiraci, směrování a opětovné použití kódu:

- Modely hrozeb: Z NTCP2 [NTCP2](/docs/specs/ntcp2), s významnými dodatečnými hrozbami relevantními pro UDP transport jak analyzuje QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Kryptografické volby: Z [NTCP2](/docs/specs/ntcp2).
- Handshake: Noise XK z [NTCP2](/docs/specs/ntcp2) a [NOISE](https://noiseprotocol.org/noise.html). Významná zjednodušení NTCP2 jsou možná díky zapouzdření (inherentní hranice zpráv) poskytovanému UDP.
- Obfuskace dočasného klíče handshake: Adaptováno z [NTCP2](/docs/specs/ntcp2), ale používá ChaCha20 z [ECIES](/docs/specs/ecies) místo AES.
- Hlavičky paketů: Adaptováno z WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) a QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Obfuskace hlaviček paketů: Adaptováno z [NTCP2](/docs/specs/ntcp2), ale používá ChaCha20 z [ECIES](/docs/specs/ecies) místo AES.
- Ochrana hlaviček paketů: Adaptováno z QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) a [Nonces](https://eprint.iacr.org/2019/624.pdf)
- Hlavičky používané jako AEAD přidružená data jako v [ECIES](/docs/specs/ecies).
- Číslování paketů: Adaptováno z WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) a QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Zprávy: Adaptováno z [SSU](/docs/transport/ssu)
- Fragmentace I2NP: Adaptováno z [SSU](/docs/transport/ssu)
- Přenos a testování peerů: Adaptováno z [SSU](/docs/transport/ssu)
- Podpisy dat přenosu a testu peerů: Ze specifikace společných struktur [Common](/docs/specs/common-structures)
- Formát bloku: Z [NTCP2](/docs/specs/ntcp2) a [ECIES](/docs/specs/ecies).
- Doplnění a možnosti: Z [NTCP2](/docs/specs/ntcp2) a [ECIES](/docs/specs/ecies).
- Acks, nacks: Adaptováno z QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000).
- Řízení toku: TBD

Neexistují žádné nové kryptografické primitiva, která by nebyla dříve použita v I2P.

### Záruky doručení

Stejně jako u jiných I2P transportů NTCP, NTCP2 a SSU 1, tento transport není univerzální zařízení pro doručování uspořádaného toku bajtů. Je navržen pro transport I2NP zpráv. Není poskytována žádná abstrakce "proudu".

Navíc, stejně jako u SSU, obsahuje dodatečné možnosti pro NAT traversal zprostředkovaný partnery a testování dosažitelnosti (příchozí spojení).

Pokud jde o SSU 1, NEPOSKYTUJE doručování I2NP zpráv v pořadí. Ani nezaručuje doručení I2NP zpráv. Kvůli efektivitě, nebo z důvodu doručování UDP datagramů mimo pořadí nebo ztráty těchto datagramů, mohou být I2NP zprávy doručeny na vzdálený konec mimo pořadí, nebo nemusí být doručeny vůbec. I2NP zpráva může být v případě potřeby přenesena vícekrát, ale doručení může nakonec selhat, aniž by došlo k odpojení celého spojení. Také nové I2NP zprávy mohou být nadále odesílány, i když probíhá retransmise (obnova ze ztráty) pro jiné I2NP zprávy.

Tento protokol NEZABRAŇUJE úplně duplicitnímu doručování I2NP zpráv. Router by měl vynucovat expiraci I2NP zpráv a používat Bloom filtr nebo jiný mechanismus založený na ID I2NP zprávy. Viz sekce Duplikace I2NP zpráv níže.

### Noise Protocol Framework

Tato specifikace poskytuje požadavky založené na Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (Revize 33, 2017-10-04). Noise má podobné vlastnosti jako protokol Station-To-Station [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol), který je základem pro protokol [SSU](/docs/transport/ssu). V terminologii Noise je Alice iniciátor a Bob je respondent.

SSU2 je založeno na protokolu Noise s označením Noise_XK_25519_ChaChaPoly_SHA256. (Skutečný identifikátor pro počáteční funkci odvození klíče je "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256" k označení rozšíření I2P - viz sekce KDF 1 níže)

POZNÁMKA: Tento identifikátor je odlišný od toho, který se používá pro NTCP2, protože všechny tři handshake zprávy používají hlavičku jako přidružená data.

Tento protokol Noise používá následující primitiva:

- Handshake Pattern: XK Alice přenáší svůj klíč Bobovi (X) Alice již zná Bobův statický klíč (K)
- DH Function: X25519 X25519 DH s délkou klíče 32 bajtů jak je specifikováno v [RFC-7748](https://tools.ietf.org/html/rfc7748).
- Cipher Function: ChaChaPoly AEAD_CHACHA20_POLY1305 jak je specifikováno v [RFC-7539](https://tools.ietf.org/html/rfc7539) sekce 2.8. 12 bajtový nonce, s prvními 4 bajty nastavenými na nulu.
- Hash Function: SHA256 Standardní 32-bajtový hash, již hojně používaný v I2P.

### Dodatky k Framework

Tato specifikace definuje následující vylepšení pro Noise_XK_25519_ChaChaPoly_SHA256. Obecně následují pokyny v [NOISE](https://noiseprotocol.org/noise.html) sekci 13.

1) Zprávy handshake (Session Request, Created, Confirmed) obsahují 16 nebo 32 bajtovou hlavičku. 2) Hlavičky pro zprávy handshake (Session Request, Created, Confirmed) se používají jako vstup do mixHash() před šifrováním/dešifrováním k navázání hlaviček na zprávu. 3) Hlavičky jsou šifrovány a chráněny. 4) Cleartext dočasné klíče jsou obfuskovány pomocí ChaCha20 šifrování s použitím známého klíče a IV. To je rychlejší než elligator2. 5) Formát payload je definován pro zprávy 1, 2 a datovou fázi. To samozřejmě není definováno v Noise.

Datová fáze používá šifrování podobné datové fázi Noise, ale není s ní kompatibilní.

### Navázání relace

Definujeme následující funkce odpovídající používaným kryptografickým stavebním blokům.

#### Dlouhá hlavička

ZEROLEN

#### Krátká hlavička

:   bajtové pole nulové délky

#### Číslování ID připojení

H(p, d)

#### Číslování paketů

:   SHA-256 hash funkce, která přijímá personalizační řetězec p a data d, a produkuje výstup o délce 32 bytů. Jak je definováno v [NOISE](https://noiseprotocol.org/noise.html). || níže znamená připojit.

## Definice

MixHash(d)

:   SHA-256 hash funkce, která přijímá předchozí hash h a nová data d a produkuje výstup o délce 32 bytů. || níže znamená připojit.

STREAM

:   ChaCha20/Poly1305 AEAD jak je specifikováno v [RFC-7539](https://tools.ietf.org/html/rfc7539). S_KEY_LEN = 32 a S_IV_LEN = 12.

DH

    Use SHA-256 as follows:

        H(p, d) := SHA-256(p || d)

:   Systém pro dohodu o veřejných klíčích X25519. Soukromé klíče o délce 32 bajtů, veřejné klíče o délce 32 bajtů, produkuje výstupy o délce 32 bajtů. Má následující funkce:

HKDF(salt, ikm, info, n)

    Use SHA-256 as follows:

        MixHash(d) := h = SHA-256(h || d)

:   Kryptografická funkce pro odvození klíčů, která bere vstupní klíčový materiál ikm (který by měl mít dobrou entropii, ale nemusí být uniformně náhodný řetězec), salt o délce 32 bajtů a kontextově specifickou hodnotu 'info', a produkuje výstup o délce n bajtů vhodný pro použití jako klíčový materiál.

MixKey(d)

    ENCRYPT(k, n, plaintext, ad)

    :   Encrypts plaintext using the cipher key k, and nonce n which MUST be unique for the key k. Associated data ad is optional. Returns a ciphertext that is the size of the plaintext + 16 bytes for the HMAC.

        The entire ciphertext must be indistinguishable from random if the key is secret.

    DECRYPT(k, n, ciphertext, ad)

    :   Decrypts ciphertext using the cipher key k, and nonce n. Associated data ad is optional. Returns the plaintext.

:   Použije HKDF() s předchozím chainKey a novými daty d, a nastaví nový chainKey a k. Jak je definováno v [NOISE](https://noiseprotocol.org/noise.html).

Každý UDP datagram obsahuje přesně jednu zprávu. Délka datagramu (po IP a UDP hlavičkách) je délka zprávy. Výplň, pokud existuje, je obsažena v bloku výplně uvnitř zprávy. V tomto dokumentu používáme termíny "datagram" a "paket" většinou zaměnitelně. Každý datagram (nebo paket) obsahuje jednu zprávu (na rozdíl od QUIC, kde datagram může obsahovat více QUIC paketů). "Hlavička paketu" je část po IP/UDP hlavičce.

    GENERATE_PRIVATE()

    :   Generates a new private key.

    DERIVE_PUBLIC(privkey)

    :   Returns the public key corresponding to the given private key.

    DH(privkey, pubkey)

    :   Generates a shared secret from the given private and public keys.

Výjimka: Zpráva Session Confirmed je jedinečná v tom, že může být rozdělena na více paketů. Více informací najdete v sekci Session Confirmed Fragmentation níže.

Všechny SSU2 zprávy mají délku alespoň 40 bajtů. Jakákoli zpráva o délce 1-39 bajtů je neplatná. Všechny SSU2 zprávy mají délku menší nebo rovnou 1472 (IPv4) nebo 1452 (IPv6) bajtů. Formát zprávy je založen na Noise zprávách, s úpravami pro rámování a nerozeznatelnost. Implementace používající standardní Noise knihovny musí předem zpracovat přijaté zprávy do standardního formátu Noise zpráv. Všechna šifrovaná pole jsou AEAD šifrotexty.

    Use HKDF as specified in [RFC-5869](https://tools.ietf.org/html/rfc5869), using the HMAC hash function SHA-256 as specified in [RFC-2104](https://tools.ietf.org/html/rfc2104). This means that SALT_LEN is 32 bytes max.

Jsou definovány následující zprávy:

Standardní sekvence navázání spojení, když Alice má platný token dříve obdržený od Boba, probíhá následovně:

    Use HKDF as follows:

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]

## Zprávy

Když Alice nemá platný token, sekvence navázání spojení probíhá následovně:

Když si Alice myslí, že má platný token, ale Bob ho odmítne (možná proto, že Bob restartoval), sekvence navázání spojení je následující:

Bob může odmítnout požadavek Session nebo Token tím, že odpoví zprávou Retry obsahující blok Termination s kódem důvodu. Na základě kódu důvodu by Alice neměla po určitou dobu pokoušet o další požadavek:

Pomocí terminologie Noise je sekvence navázání spojení a dat následující: (Vlastnosti zabezpečení datové části)

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
### Hlavička paketu

Jakmile je relace navázána, Alice a Bob si mohou vyměňovat datové zprávy.

```
Alice                           Bob

SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Všechny pakety začínají zamlženou (zašifrovanou) hlavičkou. Existují dva typy hlaviček, dlouhá a krátká. Všimněte si, že prvních 13 bytů (Destination Connection ID, číslo paketu a typ) je stejných pro všechny hlavičky.

```
Alice                           Bob

TokenRequest --------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Dlouhá hlavička má 32 bajtů. Používá se před vytvořením relace, pro Token Request, SessionRequest, SessionCreated a Retry. Používá se také pro zprávy Peer Test a Hole Punch mimo relaci.

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Před šifrováním hlavičky:

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry containing a Termination block

or

TokenRequest --------------------->
<---------------------------  Retry containing a Termination block
```
Krátká hlavička má 16 bajtů. Používá se pro zprávy Session Created a Data. Neautentizované zprávy jako Session Request, Retry a Peer Test budou vždy používat dlouhou hlavičku.

```
XK(s, rs):           Authentication   Confidentiality
  <- s
  ...
  -> e, es                  0                2
  <- e, ee                  2                1
  -> s, se                  2                5
  <-                        2                5
```
16 bajtů je vyžadováno, protože příjemce musí dešifrovat prvních 16 bajtů, aby získal typ zprávy, a poté musí dešifrovat dalších 16 bajtů, pokud se skutečně jedná o dlouhou hlavičku, jak naznačuje typ zprávy.

### Integrita paketů

Pro Session Confirmed, před šifrováním hlavičky:

#### Vazba hlavičky

Další informace o poli frag najdete v sekci Session Confirmed Fragmentation níže.

Pro Data zprávy, před šifrováním hlavičky:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 0, 1, 7, 9, 10, or 11

ver :: The protocol version, equal to 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: 8 bytes, unsigned big endian integer

Token :: 8 bytes, unsigned big endian integer
```
#### Šifrování hlaviček

ID připojení musí být generována náhodně. Zdrojové a cílové ID nesmí být identické, aby útočník na cestě nemohl zachytit a odeslat paket zpět původci, který by vypadal platně. NEPOUŽÍVEJTE čítač pro generování ID připojení, aby útočník na cestě nemohl vygenerovat paket, který by vypadal platně.

Na rozdíl od QUIC neměníme identifikátory připojení během nebo po handshaku, ani po zprávě Retry. Identifikátory zůstávají konstantní od první zprávy (Token Request nebo Session Request) až po poslední zprávu (Data s ukončením). Navíc se identifikátory připojení nemění během nebo po path challenge nebo migraci připojení.

Na rozdíl od QUIC také platí, že ID připojení v hlavičkách jsou vždy šifrována na úrovni hlaviček. Viz níže.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, all zeros

type :: The message type = 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility
```
Pokud není v handshake odeslán žádný blok First Packet Number, pakety jsou číslovány v rámci jedné relace, pro každý směr, počínaje od 0, až do maxima (2**32 -1). Relace musí být ukončena a vytvořena nová relace výrazně dříve, než je odeslán maximální počet paketů.

Pokud je blok First Packet Number odeslán v handshake, pakety jsou číslovány v rámci jedné relace, pro daný směr, začínaje od tohoto čísla paketu. Číslo paketu se může během relace přetočit. Když je odesláno maximálně 2**32 paketů, přetočením čísla paketu zpět na první číslo paketu, tato relace už není platná. Relace musí být ukončena a vytvořena nová relace výrazně před odesláním maximálního počtu paketů.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|flag|moreflags|
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 6

flag :: 1 byte flags:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-1: unused, set to 0 for future compatibility
       bits 0: when set to 1, immediate ack requested

moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### KDF šifrování hlavičky

TODO rotace klíčů, snížit maximální číslo paketu?

Handshake pakety, které jsou určeny jako ztracené, jsou retransmitovány celé, se stejnou hlavičkou včetně čísla paketu. Handshake zprávy Session Request, Session Created a Session Confirmed MUSÍ být retransmitovány se stejným číslem paketu a identickým šifrovaným obsahem, aby byl použit stejný zřetězený hash pro šifrování odpovědi. Zpráva Retry není nikdy přenášena.

Pakety datové fáze, které jsou určeny jako ztracené, nejsou nikdy retransmitovány celé (kromě ukončení, viz níže). Totéž platí pro bloky, které jsou obsaženy ve ztracených paketech. Místo toho jsou informace, které mohou být přenášeny v blocích, odeslány znovu v nových paketech podle potřeby. Datové pakety nejsou nikdy retransmitovány se stejným číslem paketu. Jakákoli retransmise obsahu paketu (bez ohledu na to, zda obsah zůstává stejný) musí použít další nepoužité číslo paketu.

#### Validace hlavičky

Opětovné odeslání nezměněného celého paketu tak, jak je, se stejným číslem paketu, není povoleno z několika důvodů. Pro kontext viz QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) sekce 12.3.

Nové pakety se používají k přenosu informací, u kterých bylo určeno, že byly ztraceny. Obecně se informace odesílají znovu, když je paket obsahující tyto informace určen jako ztracený, a odesílání se ukončí, když je paket obsahující tyto informace potvrzen.

Výjimka: Paket datové fáze obsahující blok ukončení může, ale nemusí být retransmitován celý, jak je. Viz sekce Ukončení relace níže.

Následující pakety obsahují náhodné číslo paketu, které je ignorováno:

Pro Alici začíná číslování odchozích paketů na 0 se Session Confirmed. Pro Boba začíná číslování odchozích paketů na 0 s prvním Data paketem, který by měl být ACK pro Session Confirmed. Čísla paketů v příkladu standardního handshake budou:

Jakákoliv retransmise handshake zpráv (SessionRequest, SessionCreated nebo SessionConfirmed) musí být odeslána znovu beze změny, se stejným číslem paketu. Nepoužívejte různé dočasné klíče ani neměňte payload při retransmisi těchto zpráv.

- Je neefektivní ukládat pakety pro retransmisi
- Nový paket vypadá pro pozorovatele na cestě jinak, nelze poznat, že je retransmitovaný
- Nový paket má s sebou aktualizovaný ack blok, ne starý ack blok
- Retransmitujete pouze to, co je nutné. některé fragmenty mohly být již jednou retransmitovány a potvrzeny
- Do každého retransmitovaného paketu můžete vejít tolik, kolik potřebujete, pokud čeká více dat
- Koncové body, které sledují všechny jednotlivé pakety za účelem detekce duplikátů, riskují hromadění nadměrného stavu. Data potřebná pro detekci duplikátů lze omezit udržováním minimálního čísla paketu, pod kterým jsou všechny pakety okamžitě zahozeny.
- Toto schéma je mnohem flexibilnější

Hlavička (před obfuskací a ochranou) je vždy zahrnuta v přidružených datech pro AEAD funkci, aby se kryptograficky spojila hlavička s daty.

Šifrování hlaviček má několik cílů. Pro kontext a předpoklady viz sekci "Dodatečná diskuse o DPI" výše.

Hlavičky jsou šifrovány pomocí známých klíčů publikovaných v network database nebo vypočítaných později. Ve fázi handshake je to pouze pro odolnost proti DPI, protože klíč je veřejný a klíč i nonces jsou znovu použity, takže to je prakticky jen obfuskace. Všimněte si, že šifrování hlaviček se také používá k obfuskaci dočasných klíčů X (v Session Request) a Y (v Session Created).

- Žádost o relaci
- Relace vytvořena
- Žádost o token
- Opakování
- Test peer
- Hole Punch

Další pokyny najdete v sekci Zpracování příchozích paketů níže.

```
Alice                           Bob

SessionRequest (r)    ------------>
<-------------   SessionCreated (r)
SessionConfirmed (0)  ------------>
<-------------             Data (0) (Ack-only)
Data (1)              ------------> (May be sent before Ack is received)
<-------------             Data (1)
Data (2)              ------------>
Data (3)              ------------>
Data (4)              ------------>
<-------------             Data (2)

r = random packet number (ignored)
Token Request, Retry, and Peer Test
also have random packet numbers.
```
Bajty 0-15 všech hlaviček jsou šifrovány pomocí schématu ochrany hlaviček XORováním s daty vypočítanými ze známých klíčů, pomocí ChaCha20, podobně jako QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) a [Nonces](https://eprint.iacr.org/2019/624.pdf). To zajišťuje, že šifrovaná krátká hlavička a první část dlouhé hlavičky se budou jevit jako náhodné.

#### ChaCha20/Poly1305

Pro Session Request a Session Created jsou bajty 16-31 dlouhé hlavičky a 32-bajtový Noise dočasný klíč šifrovány pomocí ChaCha20. Nešifrovaná data jsou náhodná, takže šifrovaná data budou vypadat náhodně.

#### Poznámky

Pro Retry jsou bajty 16-31 dlouhé hlavičky šifrovány pomocí ChaCha20. Nešifrovaná data jsou náhodná, takže šifrovaná data budou vypadat náhodně.

- Zabránit online DPI v identifikaci protokolu
- Zabránit vzorům v sérii zpráv ve stejném spojení, kromě opětovných přenosů handshake
- Zabránit vzorům ve zprávách stejného typu v různých spojeních
- Zabránit dešifrování záhlaví handshake bez znalosti introduction key nalezené v netDb
- Zabránit identifikaci X25519 ephemeral keys bez znalosti introduction key nalezené v netDb
- Zabránit dešifrování čísla a typu paketu datové fáze jakýmkoli online nebo offline útočníkem
- Zabránit injekci platných handshake paketů pozorovatelem na cestě nebo mimo cestu bez znalosti introduction key nalezené v netDb
- Zabránit injekci platných datových paketů pozorovatelem na cestě nebo mimo cestu
- Umožnit rychlou a efektivní klasifikaci příchozích paketů
- Poskytovat odolnost proti "sondování", takže nedojde k žádné odpovědi na chybný Session Request, nebo pokud existuje Retry odpověď, odpověď není identifikovatelná jako I2P bez znalosti introduction key nalezené v netDb
- Destination Connection ID není kritická data a je v pořádku, pokud mohou být dešifrována pozorovatelem se znalostí introduction key nalezené v netDb
- Číslo paketu datové fáze je AEAD nonce a jsou to kritická data. Nesmí být dešifrovatelné pozorovatelem ani se znalostí introduction key nalezené v netDb. Viz [Nonces](https://eprint.iacr.org/2019/624.pdf).

Na rozdíl od schématu ochrany hlavičky QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) jsou šifrovány VŠECHNY části všech hlaviček, včetně cílových a zdrojových ID připojení. QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) a [Nonces](https://eprint.iacr.org/2019/624.pdf) se primárně zaměřují na šifrování "kritické" části hlavičky, tj. čísla paketu (ChaCha20 nonce). Zatímco šifrování ID relace činí klasifikaci příchozích paketů o něco složitější, znesnadňuje některé útoky. QUIC definuje různá ID připojení pro různé fáze a pro path challenge a migraci připojení. Zde používáme stejná ID připojení průběžně, protože jsou šifrována.

Existuje sedm fází klíčů ochrany hlaviček:

Šifrování hlaviček je navrženo tak, aby umožnilo rychlou klasifikaci příchozích paketů bez složitých heuristik nebo záložních řešení. To je dosaženo použitím stejného klíče k_header_1 pro téměř všechny příchozí zprávy. I když se zdrojová IP adresa nebo port připojení změní kvůli skutečné změně IP adresy nebo chování NAT, paket může být rychle namapován na relaci pomocí jediného vyhledání ID připojení.

Všimněte si, že Session Created a Retry jsou JEDINÉ zprávy, které vyžadují záložní zpracování pro k_header_1 k dešifrování Connection ID, protože používají intro klíč odesílatele (Boba). VŠECHNY ostatní zprávy používají intro klíč příjemce pro k_header_1. Záložní zpracování potřebuje pouze vyhledat čekající odchozí spojení podle zdrojové IP/portu.

Pokud záložní zpracování podle zdrojové IP/portu nenajde čekající odchozí spojení, může mít několik příčin:

Zatímco je možné provést dodatečné záložní zpracování pro pokus o nalezení čekajícího odchozího spojení a dešifrování ID spojení pomocí k_header_1 pro dané spojení, pravděpodobně to není nutné. Pokud má Bob problémy se svým NAT nebo směrováním paketů, je pravděpodobně lepší nechat spojení selhat. Tento návrh spoléhá na to, že koncové body si zachovají stabilní adresu po dobu trvání handshake.

Viz níže sekci Zpracování příchozích paketů pro další pokyny.

- Požadavek na relaci a požadavek na token
- Relace vytvořena
- Opakování
- Relace potvrzena
- Fáze dat
- Test peer
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
Viz jednotlivé sekce KDF níže pro odvození šifrovacích klíčů hlavičky pro danou fázi.

Tento KDF používá posledních 24 bajtů paketu jako IV pro dvě operace ChaCha20. Protože všechny pakety končí 16bajtovým MAC, vyžaduje to, aby všechny datové části paketů měly minimálně 8 bajtů. Tento požadavek je dodatečně dokumentován v sekcích zpráv níže.

Po dešifrování prvních 8 bajtů hlavičky bude příjemce znát Destination Connection ID. Odtud příjemce ví, jaký šifrovací klíč hlavičky použít pro zbytek hlavičky, na základě fáze klíče relace.

- Není to SSU2 zpráva
- Poškozená SSU2 zpráva
- Odpověď je podvržená nebo upravená útočníkem
- Bob má symetrický NAT
- Bob změnil IP nebo port během zpracování zprávy
- Bob odeslal odpověď přes jiné rozhraní

Dešifrování dalších 8 bajtů hlavičky pak odhalí typ zprávy a umožní určit, zda se jedná o krátkou nebo dlouhou hlavičku. Pokud se jedná o dlouhou hlavičku, příjemce musí ověřit pole version a netid. Pokud je version != 2 nebo netid != očekávané hodnotě (obecně 2, kromě testovacích sítí), příjemce by měl zprávu zahodit.

Všechny zprávy obsahují buď tři nebo čtyři části:

Ve všech případech je hlavička (a pokud je přítomen, také efemérní klíč) vázána na autentizační MAC, aby bylo zajištěno, že celá zpráva je neporušená.

#### Zpracování chyb AEAD

```
// incoming encrypted packet
packet = incoming encrypted packet
len = packet.length

// take the next-to-last 12 bytes of the packet
iv = packet[len-24:len-13]
k_header_1 = header encryption key 1
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_1, iv, data)

// encrypt the first part of the header by XORing with the mask
packet[0:7] ^= mask[0:7]

// take the last 12 bytes of the packet
iv = packet[len-12:len-1]
k_header_2 = header encryption key 2
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_2, iv, data)

// encrypt the second part of the header by XORing with the mask
packet[8:15] ^= mask[0:7]


// For Session Request and Session Created only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header and the ephemeral key
packet[16:63] = ChaCha20.encrypt(k_header_2, iv, packet[16:63])


// For Retry, Token Request, Peer Test, and Hole Punch only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header
packet[16:31] = ChaCha20.encrypt(k_header_2, iv, packet[16:31])
```
Handlery příchozích paketů musí vždy dešifrovat ChaCha20 payload a validovat MAC před zpracováním zprávy, s jednou výjimkou: Pro zmírnění DoS útoků z paketů s podvrženou adresou obsahujících zdánlivé Session Request zprávy s neplatným tokenem, handler NEMUSÍ pokoušet dešifrovat a validovat celou zprávu (což vyžaduje nákladnou DH operaci navíc k ChaCha20/Poly1305 dešifrování). Handler může odpovědět zprávou Retry s použitím hodnot nalezených v hlavičce Session Request zprávy.

#### KDF pro počáteční ChainKey

Existují tři samostatné instance autentizovaného šifrování (CipherStates). Jedna během fáze handshake a dvě (pro odesílání a přijímání) pro datovou fázi. Každá má svůj vlastní klíč z KDF.

Šifrovaná/autentizovaná data budou reprezentována jako

### Autentizované šifrování

Šifrovaný a ověřený formát dat.

- Hlavička zprávy
- Pouze pro Session Request a Session Created, dočasný klíč
- ChaCha20-šifrovaný payload
- Poly1305 MAC

Vstupy pro funkce šifrování/dešifrování:

- Pro handshake zprávy Session Request, Session Created a Session Confirmed se hlavička zprávy zpracuje pomocí mixHash() před fází zpracování Noise
- Dočasný klíč, pokud je přítomen, je pokryt standardním Noise mixHash()
- Pro zprávy mimo Noise handshake se hlavička používá jako Associated Data pro ChaCha20/Poly1305 šifrování.

Výstup šifrovací funkce, vstup dešifrovací funkce:

### KDF pro žádost o relaci

Pro ChaCha20 odpovídá to, co je zde popsáno, [RFC-7539](https://tools.ietf.org/html/rfc7539), který je také podobně používán v TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).

Funkce derivace klíčů (KDF) generuje šifrovací klíč k pro fázi handshake z výsledku DH pomocí HMAC-SHA256(key, data) jak je definováno v [RFC-2104](https://tools.ietf.org/html/rfc2104). Jedná se o funkce InitializeSymmetric(), MixHash() a MixKey(), přesně jak jsou definovány ve specifikaci Noise.

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   Encrypted and authenticated data    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
```
#### KDF pro Session Request

Alice odesílá Bobovi, buď jako první zprávu v handshake, nebo v odpovědi na zprávu Retry. Bob odpovídá zprávou Session Created. Velikost: 80 + velikost payload. Minimální velikost: 88

Pokud Alice nemá platný token, měla by místo Session Request odeslat zprávu Token Request, aby se vyhnula režii asymetrického šifrování při generování Session Request.

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
      The packet header, 16 bytes.

data :: Plaintext data, 0 or more bytes
```
Dlouhá hlavička. Noise obsah: Alicin dočasný klíč X Noise užitečné zatížení: DateTime a další bloky Maximální velikost užitečného zatížení: MTU - 108 (IPv4) nebo MTU - 128 (IPv6). Pro MTU 1280: Maximální užitečné zatížení je 1172 (IPv4) nebo 1152 (IPv6). Pro MTU 1500: Maximální užitečné zatížení je 1392 (IPv4) nebo 1372 (IPv6).

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|       ChaCha20 encrypted data         |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|  Poly1305 Message Authentication Code |
+              (MAC)                    +
|             16 bytes                  |
+----+----+----+----+----+----+----+----+

encrypted data :: Same size as plaintext data, 0 - 65519 bytes

MAC :: Poly1305 message authentication code, 16 bytes
```
Vlastnosti zabezpečení datové části:

#### Užitečná zátěž

- Protože ChaCha20 je proudová šifra, plaintexty nemusí být vyplňovány. Dodatečné bajty keystream jsou zahozeny.
- Klíč pro šifru (256 bitů) je dohodnut prostřednictvím SHA256 KDF. Podrobnosti KDF pro každou zprávu jsou v oddílech níže.

#### Poznámky

- Ve všech zprávách je velikost AEAD zprávy známa předem. Při selhání AEAD autentifikace musí příjemce zastavit další zpracování zprávy a zprávu zahodit.
- Bob by měl udržovat černou listinu IP adres s opakovanými selháními.

### SessionRequest (Typ 0)

Hodnota X je zašifrována, aby byla zajištěna nerozlišitelnost a jedinečnost payload, které jsou nezbytné jako protiopatření proti DPI (Deep Packet Inspection). K dosažení tohoto cíle používáme šifrování ChaCha20 místo složitějších a pomalejších alternativ, jako je elligator2. Asymetrické šifrování pomocí veřejného klíče Bobova routeru by bylo příliš pomalé. Šifrování ChaCha20 používá Bobův intro klíč publikovaný v síťové databázi netDb.

#### Užitečná data

```
// Define protocol_name.
Set protocol_name = "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256"
 (52 bytes, US-ASCII encoded, no NULL termination).

// Define Hash h = 32 bytes
h = SHA256(protocol_name);

Define ck = 32 byte chaining key. Copy the h data to ck.
Set ck = h

// MixHash(null prologue)
h = SHA256(h);

// up until here, can all be precalculated by Alice for all outgoing connections

// Bob's X25519 static keys
// bpk is published in routerinfo
bsk = GENERATE_PRIVATE()
bpk = DERIVE_PUBLIC(bsk)

// Bob static key
// MixHash(bpk)
// || below means append
h = SHA256(h || bpk);

// Bob introduction key
// bik is published in routerinfo
bik = RANDOM(32)

// up until here, can all be precalculated by Bob for all incoming connections
```
#### Poznámky

```
// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Alice's X25519 ephemeral keys
aesk = GENERATE_PRIVATE()
aepk = DERIVE_PUBLIC(aesk)

// Alice ephemeral key X
// MixHash(aepk)
h = SHA256(h || aepk);

// h is used as the associated data for the AEAD in Session Request
// Retain the Hash h for the Session Created KDF


End of "e" message pattern.

This is the "es" message pattern:

// DH(e, rs) == DH(s, re)
sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
// ChaChaPoly parameters to encrypt/decrypt
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chainKey for Session Created KDF


End of "es" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2 = bik

// Header encryption keys for next message (Session Created)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessCreateHeader", 32)

// Header encryption keys for next message (Retry)
k_header_1 = bik
k_header_2 = bik
```
### KDF pro Session Created a Session Confirmed část 1

Šifrování ChaCha20 je pouze pro odolnost proti DPI. Jakákoli strana znající Bobův úvodní klíč, který je publikován v síťové databázi, může dešifrovat hlavičku a hodnotu X v této zprávě.

Nezpracovaný obsah:

Nešifrovaná data (autentizační tag Poly1305 není zobrazen):

Minimální velikost payload je 8 bytů. Protože blok DateTime má pouze 7 bytů, musí být přítomen alespoň jeden další blok.

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
Bob posílá Alici v odpovědi na zprávu Session Request. Alice odpovídá zprávou Session Confirmed. Velikost: 80 + velikost datové části. Minimální velikost: 88

Noise obsah: Bobův dočasný klíč Y Noise payload: DateTime, Address a další bloky Maximální velikost payload: MTU - 108 (IPv4) nebo MTU - 128 (IPv6). Pro 1280 MTU: Maximální payload je 1172 (IPv4) nebo 1152 (IPv6). Pro 1500 MTU: Maximální payload je 1392 (IPv4) nebo 1372 (IPv6).

Bezpečnostní vlastnosti datové části:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|    See Header Encryption KDF          |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key n=0     +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+       X, ChaCha20 encrypted           +
|       with Bob intro key n=0          |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|  k defined in KDF for Session Request |
+  n = 0                                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

X :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted X)
```
Hodnota Y je zašifrována, aby byla zajištěna nerozlišitelnost a jedinečnost payload, což jsou nezbytná opatření proti DPI. K dosažení tohoto cíle používáme šifrování ChaCha20, spíše než složitější a pomalejší alternativy jako elligator2. Asymetrické šifrování na veřejný klíč Alice router by bylo příliš pomalé. Šifrování ChaCha20 používá Bob's intro key, jak je publikován v network database.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                   X                   |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|     see below for allowed blocks      |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 0

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Alice, ignored

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: 0 if not previously received from Bob

X :: 32 bytes, X25519 ephemeral key, little endian
```
#### Problémy

- DateTime blok
- Options blok (volitelný)
- Relay Tag Request blok (volitelný)
- Padding blok (volitelný)

ChaCha20 šifrování slouží pouze k odolnosti proti DPI. Jakákoliv strana znající Bobův intro key, který je publikován v síťové databázi, a zachytí prvních 32 bajtů Session Request, může dešifrovat hodnotu Y v této zprávě.

#### Datová část

- Jedinečná hodnota X v počátečním bloku ChaCha20 zajišťuje, že šifrovaný text je pro každou relaci odlišný.
- Pro poskytnutí odolnosti proti sondování by Bob neměl posílat zprávu Retry jako odpověď na zprávu Session Request, pokud nejsou pole typu zprávy, verze protokolu a ID sítě ve zprávě Session Request platná.
- Bob musí odmítnout spojení, kde je hodnota časového razítka příliš vzdálená od aktuálního času. Označme maximální časovou odchylku jako "D". Bob musí udržovat místní cache dříve použitých handshake hodnot a odmítat duplikáty, aby zabránil replay útokům. Hodnoty v cache musí mít životnost nejméně 2*D. Hodnoty cache jsou závislé na implementaci, nicméně lze použít 32-bytovou hodnotu X (nebo její šifrovaný ekvivalent). Odmítnutí proveďte odesláním zprávy Retry obsahující nulový token a blok ukončení.
- Diffie-Hellman dočasné klíče se nesmí nikdy znovu použít, aby se zabránilo kryptografickým útokům, a opětovné použití bude odmítnuto jako replay útok.
- Možnosti "KE" a "auth" musí být kompatibilní, tj. sdílené tajemství K musí mít odpovídající velikost. Pokud budou přidány další možnosti "auth", mohlo by to implicitně změnit význam příznaku "KE" k použití jiné KDF nebo jiné velikosti zkrácení.
- Bob musí ověřit, že Alicin dočasný klíč je platným bodem na křivce.
- Padding by měl být omezen na rozumné množství. Bob může odmítnout spojení s nadměrným paddingem. Bob specifikuje své možnosti paddingu v Session Created. Minimální/maximální směrnice TBD. Náhodná velikost od 0 do 31 bytů minimálně? (Distribuce bude určena, viz Příloha A.)
- Při většině chyb, včetně AEAD, DH, zjevného replay nebo selhání validace klíče, by Bob měl zastavit další zpracování zpráv a zahodit zprávu bez odpovědi.
- Bob MŮŽE poslat zprávu Retry obsahující nulový token a blok Termination s kódem důvodu časového posunu, pokud je časové razítko v bloku DateTime příliš posunuté.
- Zmírnění DoS: DH je relativně nákladná operace. Stejně jako u předchozího protokolu NTCP by routery měly přijmout všechna nezbytná opatření k zabránění vyčerpání CPU nebo spojení. Nastavte limity na maximální aktivní spojení a maximální probíhající nastavení spojení. Vynuťte časové limity čtení (jak per-read, tak celkové pro "slowloris"). Omezte opakovaná nebo současná spojení ze stejného zdroje. Udržujte blacklisty pro zdroje, které opakovaně selžou. Neodpovídejte na selhání AEAD. Alternativně odpovězte zprávou Retry před operací DH a validací AEAD.
- Pole "ver": Celkový protokol Noise, rozšíření a protokol SSU2 včetně specifikací payload, indikující SSU2. Toto pole může být použito k indikaci podpory budoucích změn.
- Pole ID sítě se používá k rychlé identifikaci spojení mezi sítěmi. Pokud toto pole neodpovídá Bobovu ID sítě, Bob by se měl odpojit a blokovat budoucí spojení.
- Bob musí zahodit zprávu, pokud se ID zdrojového spojení rovná ID cílového spojení.

### SessionCreated (Typ 1)

```
// take h saved from Session Request KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Request)

// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Bob's X25519 ephemeral keys
besk = GENERATE_PRIVATE()
bepk = DERIVE_PUBLIC(besk)

// h is from KDF for Session Request
// Bob ephemeral key Y
// MixHash(bepk)
h = SHA256(h || bepk);

// h is used as the associated data for the AEAD in Session Created
// Retain the Hash h for the Session Confirmed KDF

End of "e" message pattern.

This is the "ee" message pattern:

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chaining key ck for Session Confirmed KDF

End of "ee" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Request KDF above

// Header protection keys for next message (Session Confirmed)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessionConfirmed", 32)
```
### KDF pro Session Confirmed část 1, používající Session Created KDF

Nezpracovaný obsah:

Nešifrovaná data (Poly1305 auth tag není zobrazen):

Minimální velikost payload je 8 bajtů. Protože bloky DateTime a Address mají celkem více než tolik, požadavek je splněn pouze těmito dvěma bloky.

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
Alice posílá Bobovi v odpovědi na zprávu Session Created. Bob okamžitě odpovídá zprávou Data obsahující ACK blok. Velikost: 80 + velikost užitečného obsahu. Minimální velikost: Přibližně 500 (minimální velikost bloku router info je přibližně 420 bajtů)

Obsah Noise: Statický klíč Alice Noise payload část 1: Žádná Noise payload část 2: RouterInfo Alice a další bloky Maximální velikost payload: MTU - 108 (IPv4) nebo MTU - 128 (IPv6). Pro 1280 MTU: Maximální payload je 1172 (IPv4) nebo 1152 (IPv6). Pro 1500 MTU: Maximální payload je 1392 (IPv4) nebo 1372 (IPv6).

Bezpečnostní vlastnosti datové části:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with derived key n=0       +
|  See Header Encryption KDF            |
+----+----+----+----+----+----+----+----+
|                                       |
+       Y, ChaCha20 encrypted           +
|       with derived key n=0            |
+              (32 bytes)               +
|       See Header Encryption KDF       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in KDF for Session Created +
|  n = 0; see KDF for associated data   |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

Y :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted Y)
```
Toto obsahuje dva ChaChaPoly rámce. První je Alicin šifrovaný statický veřejný klíč. Druhý je Noise payload: Alicin šifrovaný RouterInfo, volitelné možnosti a volitelné vyplnění. Používají různé klíče, protože mezi nimi se volá funkce MixKey().

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                  Y                    |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|      see below for allowed blocks     |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: The Source Connection ID
                             received from Alice in Session Request

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 1

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Bob, ignored

Source Connection ID :: The Destination Connection ID
                        received from Alice in Session Request

Token :: 0 (unused)

Y :: 32 bytes, X25519 ephemeral key, little endian
```
#### Poznámky

- DateTime blok
- Address blok
- Relay Tag blok (volitelný)
- New Token blok (nedoporučuje se, viz poznámka)
- First Packet Number blok (volitelný)
- Options blok (volitelný)
- Termination blok (nedoporučuje se, místo toho odeslat v retry zprávě)
- Padding blok (volitelný)

Nezpracovaný obsah:

#### Fragmentace potvrzené relace

- Alice musí validovat, že Bobův efemérní klíč je platný bod na křivce.
- Padding by měl být omezen na rozumné množství. Alice může odmítnout připojení s nadměrným paddingem. Alice specifikuje své možnosti paddingu v Session Confirmed. Minimální/maximální směrnice budou teprve určeny. Náhodná velikost od 0 do 31 bajtů minimálně? (Distribuce bude určena, viz Příloha A.)
- Při jakékoli chybě, včetně AEAD, DH, časové značky, zdánlivého replay útoku nebo selhání validace klíče, musí Alice zastavit další zpracování zpráv a uzavřít připojení bez odpovědi.
- Alice musí odmítnout připojení, kde je hodnota časové značky příliš vzdálená od aktuálního času. Nazvěme maximální delta čas "D". Alice musí udržovat místní cache dříve použitých handshake hodnot a odmítat duplikáty, aby zabránila replay útokům. Hodnoty v cache musí mít životnost alespoň 2*D. Hodnoty cache jsou závislé na implementaci, nicméně lze použít 32-bajtovou Y hodnotu (nebo její šifrovaný ekvivalent).
- Alice musí zahodit zprávu, pokud zdrojová IP a port neodpovídají cílové IP a portu Session Request.
- Alice musí zahodit zprávu, pokud Destination a Source Connection ID neodpovídají Source a Destination Connection ID z Session Request.
- Bob pošle relay tag blok, pokud o to Alice požádala v Session Request.
- New Token blok není doporučen v Session Created, protože Bob by měl nejprve provést validaci Session Confirmed. Viz sekce Tokens níže.

#### Poznámky

- Zahrnout zde možnosti min/max padding?

### KDF pro Session Confirmed část 2

```
// take h saved from Session Created KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Created)

// MixHash(header)
h = SHA256(h || header)
// h is used as the associated data for the AEAD in Session Confirmed part 1, below

This is the "s" message pattern:

// Alice's X25519 static keys
ask = GENERATE_PRIVATE()
apk = DERIVE_PUBLIC(ask)

// AEAD parameters
// k is from Session Request
n = 1
ad = h
ciphertext = ENCRYPT(k, n++, apk, ad)

// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// h is used as the associated data for the AEAD in Session Confirmed part 2

End of "s" message pattern.

// Header encryption keys for this message
See Session Confirmed part 2 below
```
### SessionConfirmed (Typ 2)

```
This is the "se" message pattern:

// DH(ask, bepk) == DH(besk, apk)
sharedSecret = DH(ask, bepk) = DH(besk, apk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// h from Session Confirmed part 1 is used as the associated data for the AEAD in Session Confirmed part 2
// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF
// retain the hash h for the data phase KDF

End of "se" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Created KDF above

// Header protection keys for data phase
See data phase KDF below
```
### KDF pro datovou fázi

Nezašifrovaná data (Poly1305 autentizační značky nejsou zobrazeny):

Minimální velikost payload je 8 bajtů. Protože blok RouterInfo bude značně větší než toto množství, požadavek je splněn pouze tímto blokem.

1)  Blok Router Info Alice (povinný)   2)  Blok možností (volitelný)   3)  I2NP bloky (volitelné)

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
4\) Padding blok (volitelný) Tento rámec nesmí nikdy obsahovat žádný jiný typ bloku. TODO: co relay a peer test?

Zpráva Session Confirmed musí obsahovat úplné podepsané Router Info od Alice, aby Bob mohl provést několik požadovaných kontrol:

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|   ChaCha20 encrypted data (32 bytes)  |
+   Encrypted and authenticated data    +
+   Alice static key S                  +
| k defined in KDF for Session Created  |
+     n = 1                             +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+ Length varies (remainder of packet)   +
|                                       |
+   ChaCha20 encrypted data             +
|   see below for allowed blocks        |
+     k defined in KDF for              +
|     Session Confirmed part 2          |
+     n = 0                             +
|     see KDF for associated data       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, ChaCha20 encrypted Alice's X25519 static key, little endian
     inside 48 byte ChaChaPoly frame
```
Bohužel Router Info, i když je gzip komprimované v RI bloku, může překročit MTU. Proto může být Session Confirmed fragmentováno napříč dvěma nebo více pakety. Toto je JEDINÝ případ v SSU2 protokolu, kdy je AEAD-chráněný payload fragmentován napříč dvěma nebo více pakety.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
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
|        Noise Payload                  |
+        (length varies)                +
|        see below for allowed blocks   |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As sent in Session Request,
                             or one received in Session Confirmed?

Packet Number :: 0 always, for all fragments, even if retransmitted

type :: 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility

S :: 32 bytes, Alice's X25519 static key, little endian
```
#### Poznámky

- RouterInfo blok (musí být první blok)
- Options blok (volitelný)
- New Token blok (volitelný)
- Relay Request blok (volitelný)
- Peer Test blok (volitelný)
- First Packet Number blok (volitelný)
- I2NP, First Fragment nebo Follow-on Fragment bloky (volitelné, ale pravděpodobně není místo)
- Padding blok (volitelný)

Hlavičky každého paketu jsou konstruovány následovně:

#### Datová část

- Bob musí provést obvyklou validaci Router Info. Ujistit se, že typ podpisu je podporován, ověřit podpis, ověřit, že časové razítko je v mezích, a jakékoliv další potřebné kontroly. Viz níže poznámky k manipulaci s fragmentovanými Router Info.

- Bob musí ověřit, že Alice's statický klíč přijatý v prvním rámci se shoduje se statickým klíčem v Router Info. Bob musí nejprve vyhledat v Router Info adresu NTCP nebo SSU2 Router Address s odpovídající verzí (v). Viz níže části Published Router Info a Unpublished Router Info. Níže najdete poznámky k manipulaci s fragmentovanými Router Infos.

- Pokud má Bob starší verzi Alice RouterInfo ve své netdb, ověř, že statický klíč v router info je stejný v obou verzích, pokud je přítomen, a pokud je starší verze méně než XXX stará (viz čas rotace klíčů níže)

- Bob musí zde ověřit, že Alicein statický klíč je platným bodem na křivce.

- Měly by být zahrnuty možnosti pro specifikaci parametrů paddingu.

- Při jakékoli chybě, včetně selhání AEAD, RI, DH, časového razítka nebo validace klíče, musí Bob zastavit další zpracování zpráv a uzavřít spojení bez odpovědi.

- Obsah rámce části 2 zprávy 3: Formát tohoto rámce je stejný jako formát rámců datové fáze, s výjimkou toho, že délku rámce posílá Alice v Session Request. Viz níže pro formát rámce datové fáze. Rámec musí obsahovat 1 až 4 bloky v následujícím pořadí:

Sestavte sérii paketů následujícím způsobem:

Proces sestavení:

- Doporučuje se padding blok pro část 2 zprávy 3.

- Pro I2NP bloky může být k dispozici žádné místo nebo pouze malé množství místa, v závislosti na MTU a velikosti Router Info. NEZAHRNUJTE I2NP bloky, pokud je Router Info fragmentovaná. Nejjednodušší implementace může být nikdy nezahrnovat I2NP bloky ve zprávě Session Confirmed a poslat všechny I2NP bloky v následujících Data zprávách. Viz sekce Router Info bloku níže pro maximální velikost bloku.

#### Datová část

Když Bob obdrží jakoukoli Session Confirmed zprávu, dešifruje hlavičku, zkontroluje pole frag a zjistí, že Session Confirmed je fragmentována. Nedešifruje (a nemůže dešifrovat) zprávu, dokud nejsou obdrženy a znovu sestaveny všechny fragmenty.

- Statický klíč "s" v RI se shoduje se statickým klíčem v handshake
- Klíč pro představení "i" v RI musí být extrahován a platný, aby mohl být použit ve fázi dat
- Podpis RI je platný

Neexistuje mechanismus pro Boba k potvrzení jednotlivých fragmentů. Když Bob obdrží všechny fragmenty, znovu je sestaví, dešifruje a ověří obsah, Bob provede split() jako obvykle, vstoupí do datové fáze a pošle ACK paketu číslo 0.

Pokud Alice neobdrží ACK paketu číslo 0, musí znovu odeslat všechny session confirmed pakety beze změny.

- VŠECHNY hlavičky jsou krátké hlavičky se stejným číslem paketu 0
- VŠECHNY hlavičky obsahují pole "frag" s číslem fragmentu a celkovým počtem fragmentů
- Nešifrovaná hlavička fragmentu 0 je přidružená data (AD) pro "jumbo" zprávu
- Každá hlavička je šifrována pomocí posledních 24 bajtů dat v TOMTO paketu

Příklady:

- Vytvořte jeden blok RI (fragment 0 z 1 v poli frag bloku RI). Nepoužíváme fragmentaci bloku RI, to bylo pro alternativní metodu řešení stejného problému.
- Vytvořte "jumbo" payload s blokem RI a všemi ostatními bloky, které mají být zahrnuty
- Vypočítejte celkovou velikost dat (nezahrnuje hlavičku), což je velikost payload + 64 bajtů pro statický klíč a dva MAC
- Vypočítejte dostupné místo v každém paketu, což je MTU minus IP hlavička (20 nebo 40), minus UDP hlavička (8), minus SSU2 krátká hlavička (16). Celková režie na paket je 44 (IPv4) nebo 64 (IPv6).
- Vypočítejte počet paketů.
- Vypočítejte velikost dat v posledním paketu. Musí být větší nebo rovna 24 bajtům, aby šifrování hlavičky fungovalo. Pokud je příliš malá, buď přidejte padding blok, NEBO zvyšte velikost padding bloku, pokud již existuje, NEBO zmenšete velikost jednoho z ostatních paketů tak, aby poslední paket byl dostatečně velký.
- Vytvořte nešifrovanou hlavičku pro první paket, s celkovým počtem fragmentů v poli frag, a zašifrujte "jumbo" payload pomocí Noise, používajíce hlavičku jako AD, jako obvykle.
- Rozdělte zašifrovaný jumbo paket na fragmenty
- Přidejte nešifrovanou hlavičku pro každý fragment 1-n
- Zašifrujte hlavičku pro každý fragment 0-n. Každá hlavička používá STEJNÉ k_header_1 a k_header_2 jak je definováno výše v Session Confirmed KDF.
- Odešlete všechny fragmenty

Pro 1500 MTU přes IPv6 je maximální payload 1372, režie RI bloku je 5, maximální velikost (gzip komprimovaných) RI dat je 1367 (za předpokladu žádných dalších bloků). Se dvěma pakety je režie 2. paketu 64, takže může obsahovat dalších 1436 bajtů payload. Takže dva pakety stačí pro komprimované RI až do velikosti 2803 bajtů.

Největší komprimovaný RI viděný v současné síti má přibližně 1400 bajtů; proto by v praxi měly stačit dva fragmenty, i při minimální MTU 1280. Protokol umožňuje maximálně 15 fragmentů.

- Zachovat hlavičku pro fragment 0, protože se používá jako Noise AD
- Před sestavením zahodit hlavičky ostatních fragmentů
- Sestavit "jumbo" payload s hlavičkou fragmentu 0 jako AD a dešifrovat pomocí Noise
- Validovat RI blok obvyklým způsobem
- Pokračovat do datové fáze a poslat ACK 0, obvyklým způsobem

Analýza bezpečnosti:

Integrita a bezpečnost fragmentované Session Confirmed je stejná jako u nefragmentované. Jakákoliv změna jakéhokoliv fragmentu způsobí selhání Noise AEAD po opětovném sestavení. Hlavičky fragmentů po fragmentu 0 se používají pouze k identifikaci fragmentu. I kdyby útočník na cestě měl klíč k_header_2 používaný k šifrování hlavičky (nepravděpodobné, odvozený z handshake), neumožnilo by mu to nahradit platný fragment.

Fáze dat používá hlavičku pro přidružená data.

KDF generuje dva šifrovací klíče k_ab a k_ba z řetězového klíče ck, používá HMAC-SHA256(key, data) jak je definováno v [RFC-2104](https://tools.ietf.org/html/rfc2104). Toto je funkce split(), přesně jak je definována ve specifikaci Noise.

Noise payload: Všechny typy bloků jsou povoleny. Maximální velikost payload: MTU - 60 (IPv4) nebo MTU - 80 (IPv6). Pro MTU 1500: Maximální payload je 1440 (IPv4) nebo 1420 (IPv6).

Počínaje 2. částí Session Confirmed jsou všechny zprávy uvnitř autentizované a šifrované ChaChaPoly užitečné zátěže. Veškeré vyplnění je uvnitř zprávy. Uvnitř užitečné zátěže je standardní formát s nulovými nebo více "bloky". Každý blok má jednobytový typ a dvoubytovou délku. Typy zahrnují datum/čas, I2NP zprávu, možnosti, ukončení a vyplnění.

Poznámka: Bob může, ale není povinen, poslat své RouterInfo Alici jako svou první zprávu Alici ve fázi dat.

### Datová zpráva (Typ 6)

Bezpečnostní vlastnosti datové části:

Nezašifrovaná data (Poly1305 auth tag nezobrazeno):

```
// split()
// chainKey = from handshake phase
keydata = HKDF(chainKey, ZEROLEN, "", 64)
k_ab = keydata[0:31]
k_ba = keydata[32:63]

// key is k_ab for Alice to Bob
// key is k_ba for Bob to Alice

keydata = HKDF(key, ZEROLEN, "HKDFSSU2DataKeys", 64)
k_data = keydata[0:31]
k_header_2 = keydata[32:63]


// AEAD parameters
k = k_data
n = 4 byte packet number from header
ad = 16 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for data phase
// aik = Alice's intro key
// bik = Bob's intro key
k_header_1 = Receiver's intro key (aik or bik)
k_header_2: from above
```
### KDF pro Peer Test

Charlie posílá Alice a Alice posílá Charlie, pouze pro fáze 5-7 Peer Test. Fáze 1-4 Peer Test musí být odeslány v rámci relace pomocí bloku Peer Test v Data zprávě. Více informací naleznete v sekcích Blok Peer Test a Proces Peer Test níže.

Velikost: 48 + velikost užitečných dat.

Noise payload: Viz níže.

Nezpracovaný obsah:

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

- Router musí zahodit zprávu s chybou AEAD.

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with intro key and         +
|  derived key, see Data Phase KDF      |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in Data Phase KDF          +
|  n = packet number from header        |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Nešifrovaná data (Poly1305 autentizační tag není zobrazen):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|flag|moreflags|
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|                                       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: As specified in session setup

Packet Number :: 4 byte big endian integer

type :: 6

flag :: 1 byte flags:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-1: unused, set to 0 for future compatibility
       bits 0: when set to 1, immediate ack requested

moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### Datová část

- Minimální velikost payload je 8 bajtů. Tento požadavek bude splněn jakýmkoliv ACK, I2NP, First Fragment nebo Follow-on Fragment blokem. Pokud požadavek není splněn, musí být zahrnut Padding blok.
- Každé číslo packetu může být použito pouze jednou. Při opětovném přenosu I2NP zpráv nebo fragmentů musí být použito nové číslo packetu.

### Test protějšku (Typ 7)

```
// AEAD parameters
// aik = Alice's intro key
k = aik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = aik
k_header_2 = aik
```
### KDF pro opakování

Minimální velikost payload je 8 bajtů. Protože blok Peer Test má celkem více než tolik, požadavek je splněn pouze tímto blokem.

Ve zprávách 5 a 7 může být blok Peer Test identický s blokem ze zpráv 3 a 4 v rámci relace, obsahující dohodu podepsanou Charliem, nebo může být znovu vygenerován. Podpis je volitelný.

Ve zprávě 6 může být blok Peer Test identický s blokem ze zpráv 1 a 2 v rámci relace, obsahující požadavek podepsaný Alicí, nebo může být znovu vygenerován. Podpis je volitelný.

Connection ID: Obě connection ID jsou odvozena z test nonce. Pro zprávy 5 a 7 poslané od Charlieho Alici je Destination Connection ID tvořeno dvěma kopiemi 4-bajtového big-endian test nonce, tj. ((nonce << 32) | nonce). Source Connection ID je inverzí Destination Connection ID, tj. ~((nonce << 32) | nonce). Pro zprávu 6 poslanou od Alice Charliemu se obě connection ID prohodí.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Obsah bloku adres:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

Packet Number :: Random number generated by Alice

type :: 10

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: zero
```
#### Poznámky

- DateTime blok
- Address blok (vyžadován pro zprávy 6 a 7, viz poznámka níže)
- Peer Test blok
- Padding blok (volitelný)

Požadavkem pro zprávu Retry je, že Bob nemusí dešifrovat zprávu Session Request, aby vygeneroval zprávu Retry jako odpověď. Také tato zpráva musí být rychlá na vygenerování a používat pouze symetrické šifrování.

Bob posílá Alici jako odpověď na zprávu Session Request nebo Token Request. Alice odpovídá novou zprávou Session Request. Velikost: 48 + velikost payload.

Také slouží jako zpráva ukončení (tj. "Neopakovat pokus"), pokud je zahrnut blok ukončení.

Noise payload: Viz níže.

Nezpracovaný obsah:

- Ve zprávě 5: Není vyžadováno.
- Ve zprávě 6: Charlie's IP a port vybraný z Charlie's RI.
- Ve zprávě 7: Alice's skutečná IP a port, ze kterých byla zpráva 6 přijata.

### Opakovat (Typ 9)

Nešifrovaná data (Poly1305 autentizační značka není zobrazena):

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### KDF pro Token Request

Minimální velikost payload je 8 bajtů. Protože bloky DateTime a Address dohromady mají více než tolik, požadavek je splněn pouze těmito dvěma bloky.

Tato zpráva musí být rychle vygenerována, používá pouze symetrické šifrování.

Alice odešle Bobovi. Bob odpoví zprávou Retry. Velikost: 48 + velikost payload.

Pokud Alice nemá platný token, měla by poslat tuto zprávu místo Session Request, aby se vyhnula režii asymetrického šifrování při generování Session Request.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Noise payload: Viz níže.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: The Source Connection ID
                             received from Alice in Token Request
                             or Session Request

Packet Number :: Random number generated by Bob

type :: 9

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: The Destination Connection ID
                        received from Alice in Token Request
                        or Session Request

Token :: 8 byte unsigned integer, randomly generated by Bob, nonzero,
         or zero if session is rejected and a termination block is included
```
#### Datová část

- DateTime blok
- Address blok
- Options blok (volitelný)
- Termination blok (volitelný, pokud je relace odmítnuta)
- Padding blok (volitelný)

Nezpracovaný obsah:

#### DateTime

- Pro zajištění odolnosti proti sondování by router neměl poslat zprávu Retry jako odpověď na zprávu Session Request nebo Token Request, pokud nejsou pole typu zprávy, verze protokolu a ID sítě ve zprávě Request platná.
- Pro omezení rozsahu jakéhokoliv amplifikačního útoku, který může být proveden pomocí falešných zdrojových adres, nesmí zpráva Retry obsahovat velké množství výplně. Doporučuje se, aby zpráva Retry nebyla větší než trojnásobek velikosti zprávy, na kterou odpovídá. Alternativně použijte jednoduchou metodu, jako je přidání náhodného množství výplně v rozsahu 1-64 bajtů.

### Požadavek na Token (Typ 10)

Nešifrovaná data (Poly1305 autentizační značka není zobrazena):

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### KDF pro Hole Punch

Minimální velikost payload je 8 bajtů.

Tato zpráva musí být rychle generována, používá pouze symetrické šifrování.

Charlie posílá Alici v odpovědi na Relay Intro přijatou od Boba. Alice odpovídá novým Session Request. Velikost: 48 + velikost payload.

Noise payload: Viz níže.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Nezpracovaný obsah:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|    flags     |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As specified in session setup

Packet Number :: 4 byte big endian integer

type :: 6

flags :: 3 bytes, unused, set to 0 for future compatibility
```
#### Možnosti

- DateTime blok
- Padding blok

Nešifrovaná data (Poly1305 autentizační tag není zobrazen):

#### RouterInfo

- Pro poskytnutí odolnosti proti zkoumání by router neměl posílat zprávu Retry jako odpověď na zprávu Token Request, pokud pole typu zprávy, verze protokolu a síťového ID ve zprávě Token Request nejsou platná.
- Toto NENÍ standardní Noise zpráva a není součástí handshake. Není vázána ke zprávě Session Request jinak než prostřednictvím ID připojení.
- Při většině chyb, včetně AEAD nebo zjevného replay útoku by Bob měl zastavit další zpracování zprávy a zahodit zprávu bez odpovědi.
- Bob musí odmítnout připojení, kde je hodnota časového razítka příliš vzdálená od aktuálního času. Nazovme maximální delta čas "D". Bob musí udržovat místní cache dříve použitých handshake hodnot a odmítat duplikáty, aby zabránil replay útokům. Hodnoty v cache musí mít životnost alespoň 2*D. Hodnoty cache jsou závislé na implementaci, nicméně lze použít 32-bajtovou hodnotu X (nebo její šifrovaný ekvivalent).
- Bob MŮŽE poslat zprávu Retry obsahující nulový token a blok Termination s kódem důvodu pro časový posun, pokud je časové razítko v bloku DateTime příliš posunuté.
- Minimální velikost: TBD, stejná pravidla jako pro Session Created?

### Hole Punch (Typ 11)

Minimální velikost datové části je 8 bajtů. Protože bloky DateTime a Address dohromady přesahují tuto hodnotu, požadavek je splněn pouze těmito dvěma bloky.

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Formát datové části

ID připojení: Obě ID připojení jsou odvozena z relay nonce. ID cílového připojení jsou dvě kopie 4-bajtového relay nonce v big-endian formátu, tj. ((nonce << 32) | nonce). ID zdrojového připojení je inverzí ID cílového připojení, tj. ~((nonce << 32) | nonce).

Alice by měla ignorovat token v hlavičce. Token, který má být použit v Session Request, se nachází v bloku Relay Response.

Každý Noise payload obsahuje nula nebo více "bloků".

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Toto používá stejný formát bloků jako je definován ve specifikacích [NTCP2](/docs/specs/ntcp2) a [ECIES](/docs/specs/ecies). Jednotlivé typy bloků jsou definovány odlišně. Ekvivalentní termín v QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) je "rámce".

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: See below

type :: 7

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random number generated by Alice or Charlie

Source Connection ID :: See below

Token :: Randomly generated by Alice or Charlie, ignored
```
#### I2NP Message

- Blok DateTime
- Blok Address
- Blok Relay Response
- Blok Padding (volitelný)

Existují obavy, že povzbuzování implementátorů ke sdílení kódu může vést k problémům s parsováním. Implementátoři by měli pečlivě zvážit výhody a rizika sdílení kódu a zajistit, že pravidla pro řazení a platné bloky jsou pro tyto dva kontexty odlišná.

V šifrované datové části je jeden nebo více bloků. Blok má jednoduchý formát Tag-Length-Value (TLV). Každý blok obsahuje jednobytový identifikátor, dvoubajtovou délku a nula nebo více bajtů dat. Tento formát je identický s tím v [NTCP2](/docs/specs/ntcp2) a [ECIES](/docs/specs/ecies), avšak definice bloků se liší.

Pro rozšiřitelnost musí příjemci ignorovat bloky s neznámými identifikátory a zacházet s nimi jako s výplní.

## Noise Payload

(Poly1305 auth tag není zobrazen):

Šifrování hlavičky používá posledních 24 bajtů paketu jako IV pro dvě operace ChaCha20. Jelikož všechny pakety končí 16bajtovým MAC, je vyžadováno, aby všechny datové části paketů měly minimálně 8 bajtů. Pokud datová část nesplňuje tento požadavek, musí být zahrnut blok Padding.

Maximální ChaChaPoly payload se liší podle typu zprávy, MTU a typu IPv4 nebo IPv6 adresy. Maximální payload je MTU - 60 pro IPv4 a MTU - 80 pro IPv6. Maximální payload data jsou MTU - 63 pro IPv4 a MTU - 83 pro IPv6. Horní limit je přibližně 1440 bajtů pro IPv4, 1500 MTU, Data zpráva. Maximální celková velikost bloku je maximální velikost payload. Maximální velikost jednoho bloku je maximální celková velikost bloku. Typ bloku má 1 bajt. Délka bloku má 2 bajty. Maximální velikost dat jednoho bloku je maximální velikost jednoho bloku minus 3.

### Pravidla uspořádání bloků

Poznámky:

Typy bloků:

V Session Confirmed musí být Router Info první blok.

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

blk :: 1 byte, see below
size :: 2 bytes, big endian, size of data to follow, 0 - TBD
data :: the data
```
Ve všech ostatních zprávách je pořadí nespecifikované, kromě následujících požadavků: Padding, pokud je přítomen, musí být posledním blokem. Termination, pokud je přítomen, musí být posledním blokem kromě Padding. Více bloků Padding není povoleno v jednom payload.

Pro synchronizaci času:

Poznámky:

- Implementátoři musí zajistit, že při čtení bloku nebudou poškozená nebo škodlivá data způsobovat čtení přesahující do dalšího bloku nebo za hranice payload.
- Implementace by měly ignorovat neznámé typy bloků pro dopřednou kompatibilitu.

Předat aktualizované možnosti. Možnosti zahrnují: Minimální a maximální padding.

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
### Specifikace bloků

Blok možností bude mít proměnnou délku.

Problémy s možnostmi:

### Požadavek relace

#### První Fragment

Předej Alicin RouterInfo Bobovi. Používá se pouze v payload části 2 Session Confirmed. Nepoužívat ve fázi dat; místo toho použij I2NP DatabaseStore Message.

```
+----+----+----+----+----+----+----+
| 0  |    4    |     timestamp     |
+----+----+----+----+----+----+----+

blk :: 0
size :: 2 bytes, big endian, value = 4
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
```
Minimální velikost: Přibližně 420 bajtů, pokud identita routeru a podpis v router info nejsou kompresovatelné, což je nepravděpodobné.

- Na rozdíl od SSU 1 není v SSU 2 v hlavičce paketu během datové fáze žádný časový údaj.
- Implementace by měly periodicky posílat DateTime bloky během datové fáze.
- Implementace musí zaokrouhlovat na nejbližší sekundu, aby předešly časovému zkreslení v síti.

#### Následující fragment

POZNÁMKA: Blok Router Info není nikdy fragmentován. Pole frag je vždy 0/1. Viz sekce Session Confirmed Fragmentation výše pro více informací.

Poznámky:

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
Kompletní I2NP zpráva s upraveným hlavičkou.

- Vyjednávání možností je zatím neurčeno.

#### Ukončení

Toto používá stejných 9 bajtů pro I2NP hlavičku jako v [NTCP2](/docs/specs/ntcp2) (typ, ID zprávy, krátká doba vypršení).

Poznámky:

První fragment (fragment #0) I2NP zprávy s upravenou hlavičkou.

```
+----+----+----+----+----+----+----+----+
| 2  |  size   |flag|frag|              |
+----+----+----+----+----+              +
|                                       |
+       Router Info fragment            +
| (Alice RI in Session Confirmed)       |
+ (Alice, Bob, or third-party           +
|  RI in data phase)                    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 2
size :: 2 bytes, big endian, 2 + fragment size
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 0 for local store, 1 for flood request
       bit 1: 0 for uncompressed, 1 for gzip compressed
       bits 7-2: Unused, set to 0 for future compatibility
frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number, always 0
       bits 3-0: total fragments, always 1, big endian

routerinfo :: Alice's or Bob's RouterInfo
```
Toto používá stejných 9 bajtů pro I2NP hlavičku jako v [NTCP2](/docs/specs/ntcp2) (typ, ID zprávy, krátká expirace).

- Router Info je volitelně komprimováno pomocí gzip, jak naznačuje flag bit 1. Toto se liší od NTCP2, kde nikdy není komprimováno, a od DatabaseStore Message, kde je vždy komprimováno. Komprese je volitelná, protože obvykle poskytuje malý přínos pro malé Router Info, kde je málo komprimovatelného obsahu, ale je velmi užitečná pro velké Router Info s několika komprimovatelnými Router Address. Komprese se doporučuje, pokud umožní Router Info vejít se do jediného Session Confirmed paketu bez fragmentace.
- Maximální velikost prvního nebo jediného fragmentu v Session Confirmed zprávě: MTU - 113 pro IPv4 nebo MTU - 133 pro IPv6. Za předpokladu výchozího MTU 1500 bytů a žádných dalších bloků ve zprávě, 1387 pro IPv4 nebo 1367 pro IPv6. 97% současných router info je menších než 1367 bez gzippingu. 99,9% současných router info je menších než 1367 při gzippingu. Za předpokladu minimálního MTU 1280 bytů a žádných dalších bloků ve zprávě, 1167 pro IPv4 nebo 1147 pro IPv6. 94% současných router info je menších než 1147 bez gzippingu. 97% současných router info je menších než 1147 při gzippingu.
- Frag byte je nyní nepoužitý, Router Info blok není nikdy fragmentován. Frag byte musí být nastaven na fragment 0, celkový počet fragmentů 1. Viz sekce Session Confirmed Fragmentation výše pro více informací.
- Flooding nesmí být požadován, pokud nejsou v RouterInfo publikované RouterAddress. Přijímající router nesmí Router Info zaplavit, pokud v něm nejsou publikované RouterAddress.
- Tento protokol neposkytuje potvrzení, že Router Info bylo uloženo nebo zaplaveno. Pokud je potvrzení požadováno a příjemce je floodfill, odesílatel by měl místo toho poslat standardní I2NP DatabaseStoreMessage s reply tokenem.

#### RelayRequest

Celkový počet fragmentů není specifikován.

Poznámky:

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
Další fragment (číslo fragmentu větší než nula) I2NP zprávy.

- Toto je stejný 9-bajtový formát I2NP hlavičky používaný v NTCP2.
- Toto je přesně stejný formát jako blok First Fragment, ale typ bloku označuje, že se jedná o kompletní zprávu.
- Maximální velikost včetně 9-bajtové I2NP hlavičky je MTU - 63 pro IPv4 a MTU - 83 pro IPv6.

#### RelayResponse

Poznámky:

Ukončit spojení. Toto musí být poslední nepadovací blok v datové části.

Poznámky:

```
+----+----+----+----+----+----+----+----+
| 4  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |                   |
+----+----+----+----+                   +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 4
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: Partial I2NP message body, bytes 0 - (size - 10)
```
Odesláno ve zprávě Data v rámci relace, od Alice k Bobovi. Viz sekce Relay Process níže.

- Toto je stejný 9-bajtový formát I2NP hlavičky používaný v NTCP2.
- Toto je přesně stejný formát jako blok I2NP zprávy, ale typ bloku označuje, že se jedná o první fragment zprávy.
- Délka částečné zprávy musí být větší než nula.
- Stejně jako v SSU 1 se doporučuje poslat poslední fragment jako první, aby příjemce znal celkový počet fragmentů a mohl efektivně alokovat přijímací buffery.
- Maximální velikost včetně 9-bajtové I2NP hlavičky je MTU - 63 pro IPv4 a MTU - 83 pro IPv6.

#### RelayIntro

Poznámky:

```
+----+----+----+----+----+----+----+----+
| 5  |  size   |frag|    msg id         |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 5
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 5).
frag :: Fragment info:
        Bit order: 76543210 (bit 7 is MSB)
        bits 7-1: fragment number 1 - 127 (0 not allowed)
        bit 0: isLast (1 = true)
msg id :: 4 bytes, big endian, I2NP message ID
message :: Partial I2NP message body
```
Podpis:

- Délka částečné zprávy musí být větší než nula.
- Stejně jako v SSU 1 se doporučuje poslat poslední fragment jako první, aby příjemce znal celkový počet fragmentů a mohl efektivně alokovat přijímací buffery.
- Stejně jako v SSU 1 je maximální číslo fragmentu 127, ale praktický limit je 63 nebo méně. Implementace mohou omezit maximum na to, co je praktické pro maximální velikost I2NP zprávy okolo 64 KB, což je přibližně 55 fragmentů s minimálním MTU 1280. Viz sekce Maximální velikost I2NP zprávy níže.
- Maximální velikost částečné zprávy (nezahrnuje frag a message id) je MTU - 68 pro IPv4 a MTU - 88 pro IPv6.

#### PeerTest

Alice podepíše požadavek a zahrne ho do tohoto bloku; Bob ho předá v bloku Relay Intro Charlie. Algoritmus podpisu: Podepište následující data pomocí podpisového klíče routeru Alice:

```
+----+----+----+----+----+----+----+----+
| 6  |  size   |    valid data packets  |
+----+----+----+----+----+----+----+----+
    received   | rsn|     addl data     |
+----+----+----+----+                   +
~               .   .   .               ~
+----+----+----+----+----+----+----+----+

blk :: 6
size :: 2 bytes, big endian, value = 9 or more
valid data packets received :: The number of valid packets received
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
       11: Session Request error
       12: Session Created error
       13: Session Confirmed error
       14: Timeout
       15: RI signature verification fail
       16: s parameter missing, invalid, or mismatched in RouterInfo
       17: banned
       18: bad token
       19: connection limits
       20: incompatible version
       21: wrong net ID
       22: replaced by new session
addl data :: optional, 0 or more bytes, for future expansion, debugging,
             or reason text.
             Format unspecified and may vary based on reason code.
```
Odesláno ve zprávě Data v rámci relace, od Charlieho k Bobovi nebo od Boba k Alici, A TAKÉ ve zprávě Hole Punch od Charlieho k Alici. Viz sekce Relay Process níže.

- Ne všechny důvody mohou být skutečně použity, závisí na implementaci. Většina selhání obecně povede k zahození zprávy, nikoli k ukončení. Viz poznámky v sekcích handshake zpráv výše. Další uvedené důvody slouží pro konzistenci, logování, ladění, nebo pokud se změní pravidla.
- Doporučuje se zahrnout ACK blok spolu s Termination blokem.
- Ve fázi dat, z jakéhokoli důvodu jiného než "termination received", by peer měl odpovědět termination blokem s důvodem "termination received".

#### NextNonce

Poznámky:

```
+----+----+----+----+----+----+----+----+
|  7 |  size   |flag|       nonce       |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 7
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility

The data below here is covered
by the signature, and Bob forwards it unmodified.

nonce :: 4 bytes, randomly generated by Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
Token musí být okamžitě použit Alicí v Session Request.

- IP adresa je vždy zahrnuta (na rozdíl od SSU 1) a může se lišit od IP adresy použité pro relaci.

Podpis:

Pokud Charlie souhlasí (kód odpovědi 0) nebo odmítne (kód odpovědi 64 nebo vyšší), Charlie podepíše odpověď a zahrne ji do tohoto bloku; Bob ji předá v bloku Relay Response Alici. Algoritmus podpisu: Podepište následující data pomocí Charlie's router signing key:

- prologue: 16 bajtů "RelayRequestData", bez null ukončení (není zahrnuto ve zprávě)
- bhash: Bobův 32-bajtový hash routeru (není zahrnuto ve zprávě)
- chash: Charlieho 32-bajtový hash routeru (není zahrnuto ve zprávě)
- nonce: 4-bajtové nonce
- relay tag: 4-bajtový relay tag
- timestamp: 4-bajtové časové razítko (sekundy)
- ver: 1-bajtová verze SSU
- asz: 1-bajtová velikost koncového bodu (port + IP) (6 nebo 18)
- AlicePort: 2-bajtové číslo portu Alice
- Alice IP: (asz - 2) bajtová IP adresa Alice

#### Potvrzení

Pokud Bob odmítne (kód odpovědi 1-63), Bob podepíše odpověď a zahrne ji do tohoto bloku. Algoritmus podpisu: Podepsat následující data s Bobovým podpisovým klíčem routeru:

```
+----+----+----+----+----+----+----+----+
|  8 |  size   |flag|code|    nonce
+----+----+----+----+----+----+----+----+
     |     timestamp     | ver| csz|Char
+----+----+----+----+----+----+----+----+
 Port|   Charlie IP addr |              |
+----+----+----+----+----+              +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

blk :: 8
size :: 2 bytes, 6
flag :: 1 byte flags, Unused, set to 0 for future compatibility
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, Charlie is banned
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, relay tag not found
       6: rejected by Bob, Alice RI not found
       7-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       71-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD

The data below is covered by the signature if the code is 0 (accept).
Bob forwards it unmodified.

nonce :: 4 bytes, as received from Bob or Alice

The data below is present only if the code is 0 (accept).

timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
csz :: 1 byte endpoint (port + IP) size (0 or 6 or 18)
       may be 0 for some rejection codes
CharliePort :: 2 byte Charlie's port number, big endian
               not present if csz is 0
Charlie IP :: (csz - 2) byte representation of Charlie's IP address,
              network byte order
              not present if csz is 0
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Charlie.
             Not present if rejected by Bob.
token :: Token generated by Charlie for Alice to use
         in the Session Request.
         Only present if code is 0 (accept)
```
Odesláno ve zprávě Data v rámci relace, od Boba k Charliemu. Viz sekce Proces předávání níže.

Musí předcházet blok RouterInfo nebo blok I2NP DatabaseStore zprávy (nebo fragment) obsahující Router Info Alice, buď ve stejném payload (pokud je místo), nebo v předchozí zprávě.

Poznámky:

Podpis:

- prologue: 16 bytů "RelayAgreementOK", neukončeno nulou (není zahrnuto ve zprávě)
- bhash: Bobův 32-bytový hash routeru (není zahrnuto ve zprávě)
- nonce: 4-bytový nonce
- timestamp: 4-bytový časový údaj (sekundy)
- ver: 1-bytová verze SSU
- csz: 1-bytová velikost koncového bodu (port + IP) (0 nebo 6 nebo 18)
- CharliePort: 2-bytové číslo portu Charlie (nepřítomno pokud je csz 0)
- Charlie IP: (csz - 2) bytová IP adresa Charlie (nepřítomno pokud je csz 0)

Alice podepíše požadavek a Bob jej v tomto bloku předá Charliemu. Algoritmus ověření: Ověřte následující data pomocí podpisového klíče routeru Alice:

- prolog: 16 bajtů "RelayAgreementOK", není ukončeno null (není zahrnuto ve zprávě)
- bhash: 32-bajtový hash routeru Boba (není zahrnuto ve zprávě)
- nonce: 4-bajtový nonce
- timestamp: 4-bajtový timestamp (sekundy)
- ver: 1 bajt verze SSU
- csz: 1 bajt = 0

#### Adresa

Odesláno buď ve zprávě Data v rámci relace, nebo ve zprávě Peer Test mimo relaci. Viz sekce Proces Peer Test níže.

Pro zprávu 2 musí být předcházena blokem RouterInfo, nebo blokem I2NP DatabaseStore zprávy (nebo fragmentem), obsahujícím Router Info Alice, buď ve stejném payload (pokud je místo), nebo v předchozí zprávě.

```
+----+----+----+----+----+----+----+----+
|  9 |  size   |flag|                   |
+----+----+----+----+                   +
|                                       |
+                                       +
|         Alice Router Hash             |
+             32 bytes                  +
|                                       |
+                   +----+----+----+----+
|                   |      nonce        |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 9
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's 32-byte router hash,

The data below here is covered
by the signature, as received from Alice in the Relay Request,
and Bob forwards it unmodified.

nonce :: 4 bytes, as received from Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
Pro zprávu 4, pokud je relay přijato (kód důvodu 0), musí mu předcházet blok RouterInfo, nebo blok I2NP DatabaseStore zprávy (nebo fragment), obsahující Router Info Charlieho, buď ve stejném payload (pokud je místo), nebo v předchozí zprávě.

- Pro IPv4 je IP adresa Alice vždy 4 bajty, protože se Alice pokouší připojit k Charlie přes IPv4. IPv6 je podporováno a IP adresa Alice může být 16 bajtů.
- Pro IPv4 musí být tato zpráva odeslána přes navázané IPv4 spojení, protože to je jediný způsob, jak Bob zná IPv4 adresu Charlie, kterou může vrátit Alice v [RelayResponse](#relayresponse). IPv6 je podporováno a tato zpráva může být odeslána přes navázané IPv6 spojení.
- Každá SSU adresa publikovaná s introducery musí obsahovat "4" nebo "6" v možnosti "caps".

Poznámky:

Alice pošle požadavek Bobovi pomocí existující relace přes transport (IPv4 nebo IPv6), který chce testovat. Když Bob obdrží požadavek od Alice přes IPv4, Bob musí vybrat Charlie, který inzeruje IPv4 adresu. Když Bob obdrží požadavek od Alice přes IPv6, Bob musí vybrat Charlie, který inzeruje IPv6 adresu. Skutečná komunikace Bob-Charlie může být přes IPv4 nebo IPv6 (tj. nezávisle na typu adresy Alice).

- prolog: 16 bajtů "RelayRequestData", nekončí null znakem (není zahrnuto ve zprávě)
- bhash: Bobův 32-bajtový hash routeru (není zahrnuto ve zprávě)
- chash: Charlieho 32-bajtový hash routeru (není zahrnuto ve zprávě)
- nonce: 4-bajtový nonce
- relay tag: 4-bajtový relay tag
- timestamp: 4-bajtový časový údaj (sekundy)
- ver: 1-bajtová verze SSU
- asz: 1-bajtová velikost koncového bodu (port + IP) (6 nebo 18)
- AlicePort: 2-bajtové číslo portu Alice
- Alice IP: (asz - 2) bajtová IP adresa Alice

#### Požadavek na Relay Tag

Podpisy:

Alice podepíše požadavek a zahrne jej do zprávy 1; Bob jej přepošle ve zprávě 2 Charliemu. Charlie podepíše odpověď a zahrne ji do zprávy 3; Bob ji přepošle ve zprávě 4 Alici. Algoritmus podpisu: Podepsat nebo ověřit následující data pomocí podpisového klíče Alice nebo Charlieho:

TODO pouze pokud rotujeme klíče

```
+----+----+----+----+----+----+----+----+
| 10 |  size   | msg|code|flag|         |
+----+----+----+----+----+----+         +
| Alice router hash (message 2 only)    |
+             or                        +
| Charlie router hash (message 4 only)  |
+ or all zeros if rejected by Bob       +
| Not present in messages 1,3,5,6,7     |
+                             +----+----+
|                             | ver|
+----+----+----+----+----+----+----+----+
   nonce       |     timestamp     | asz|
+----+----+----+----+----+----+----+----+
|AlicePort|  Alice IP address |         |
+----+----+----+----+----+----+         +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 10
size :: 2 bytes, big endian, size of data to follow
msg :: 1 byte message number 1-7
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, no Charlie available
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, address unsupported
       6-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       70-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD
       reject codes only allowed in messages 3 and 4
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's or Charlie's 32-byte router hash,
        only present in messages 2 and 4.
        All zeros (fake hash) in message 4 if rejected by Bob.

For messages 1-4, the data below here is covered
by the signature, if present, and Bob forwards it unmodified.

ver :: 1 byte SSU version:
       1: SSU 1 (not supported)
       2: SSU 2 (required)
nonce :: 4 byte test nonce, big endian
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice or Charlie.
             Only present for messages 1-4.
             Optional in message 5-7.
```
4 byte ack through, následovaný počtem ack a nula nebo více nack/ack rozsahů.

- Na rozdíl od SSU 1 musí zpráva 1 obsahovat IP adresu a port Alice.

- Testování IPv6 adres je podporováno a komunikace Alice-Bob a Alice-Charlie může probíhat přes IPv6, pokud Bob a Charlie indikují podporu pomocí 'B' capability ve své publikované IPv6 adrese. Podrobnosti viz Proposal 126.

Tento návrh je adaptován a zjednodušen z protokolu QUIC. Cíle návrhu jsou následující:

- Zprávy 1-4 musí být obsaženy ve zprávě Data v existující relaci.

- Bob musí poslat Alice RI Charliemu před odesláním zprávy 2.

- Bob musí poslat Charlieho RI (router info) Alice před odesláním zprávy 4, pokud je přijata (kód důvodu 0).

- Zprávy 5-7 musí být obsaženy ve zprávě Peer Test mimo relaci.

- Zprávy 5 a 7 mohou obsahovat stejná podepsaná data jako byla odeslána ve zprávách 3 a 4, nebo mohou být regenerována s novým časovým razítkem. Podpis je volitelný.

- Zpráva 6 může obsahovat stejná podepsaná data jako byla odeslána ve zprávách 1 a 2, nebo může být znovu vygenerována s novým časovým razítkem. Podpis je volitelný.

Níže uvedené kódování dosahuje těchto designových cílů tím, že posílá číslo nejvyššího bitu, který je nastaven na 1, spolu s dalšími po sobě jdoucími bity níže, které jsou také nastaveny na 1. Poté, pokud je místo, jeden nebo více "rozsahů" specifikujících počet po sobě jdoucích 0 bitů a po sobě jdoucích 1 bitů níže. Viz QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) sekce 13.2.3 pro další pozadí.

Příklady:

- prologue: 16 bajtů "PeerTestValidate", nezakončené null (není zahrnuto ve zprávě)
- bhash: Bobův 32-bajtový hash routeru (není zahrnuto ve zprávě)
- ahash: Alicin 32-bajtový hash routeru (Používá se pouze v podpisu pro zprávy 3 a 4; není zahrnuto ve zprávě 3 nebo 4)
- ver: 1 bajt verze SSU
- nonce: 4 bajtový testovací nonce
- timestamp: 4 bajtový časový razítko (sekundy)
- asz: 1 bajt velikost koncového bodu (port + IP) (6 nebo 18)
- AlicePort: 2 bajtové číslo portu Alice
- Alice IP: (asz - 2) bajtová IP adresa Alice

#### Relay Tag

Chceme potvrdit pouze paket 10:

```
+----+----+----+----+----+----+----+----+
| 11 |  size   |      TBD               |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 11
size :: 2 bytes, big endian, size of data to follow
```
#### Nový Token

Chceme potvrdit pouze pakety 8-10:

Chceme ACK 10 9 8 6 5 2 1 0 a NACK 7 4 3. Kódování ACK bloku je:

- Chceme efektivně kódovat "bitfield", což je sekvence bitů reprezentující potvrzené pakety.
- Bitfield se skládá převážně z 1. Jak 1, tak 0 se obecně vyskytují v sekvenčních "shlucích".
- Množství místa v paketu dostupného pro potvrzení se liší.
- Nejdůležitější bit je ten s nejvyšším číslem. Bity s nižšími čísly jsou méně důležité. Pod určitou vzdáleností od nejvyššího bitu budou nejstarší bity "zapomenuty" a nikdy znovu odeslány.

Poznámky:

```
+----+----+----+----+----+----+----+----+
| 12 |  size   |    Ack Through    |acnt|
+----+----+----+----+----+----+----+----+
|  range  |  range  |     .   .   .     |
+----+----+----+----+                   +
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 12
size :: 2 bytes, big endian, size of data to follow,
        5 minimum
ack through :: highest packet number acked
acnt :: number of acks lower than ack through also acked,
        0-255
range :: If present,
         1 byte nack count followed by 1 byte ack count,
         0-255 each
```
2bajtový port a 4 nebo 16bajtová IP adresa. Adresa Alice, zaslaná Alice od Boba, nebo adresa Boba, zaslaná Bobovi od Alice.

Toto může být odesláno Alice ve zprávě Session Request, Session Confirmed nebo Data. Není podporováno ve zprávě Session Created, protože Bob ještě nemá Alice RI a neví, zda Alice podporuje relay. Také pokud Bob dostává příchozí spojení, pravděpodobně nepotřebuje introducers (kromě možná pro jiný typ ipv4/ipv6).

- Ack Through: 10
- acnt: 0
- žádné rozsahy nejsou zahrnuty

Když je odeslán v Session Request, Bob může odpovědět s Relay Tag v Session Created zprávě, nebo se může rozhodnout počkat na přijetí Alice RouterInfo v Session Confirmed pro ověření Alice identity před odpovědí v Data zprávě. Pokud Bob nechce pro Alice relay, neodešle Relay Tag blok.

- Ack Through: 10
- acnt: 2
- žádné rozsahy nejsou zahrnuty

Toto může být odesláno Bobem ve zprávě Session Confirmed nebo Data, jako odpověď na Relay Tag Request od Alice.

- Ack Through: 10
- acnt: 2 (ack 9 8)
- range: 1 2 (nack 7, ack 6 5)
- range: 2 3 (nack 4 3, ack 2 1 0)

Když je Relay Tag Request odeslán v Session Request, Bob může odpovědět s Relay Tag v Session Created zprávě, nebo se může rozhodnout počkat na přijetí Alice RouterInfo v Session Confirmed pro ověření Alice identity před odpovědí v Data zprávě. Pokud Bob nechce pro Alice přenášet, neposílá Relay Tag blok.

- Rozsahy nemusí být přítomny. Maximální počet rozsahů není specifikován, může jich být tolik, kolik se vejde do paketu.
- Range nack může být nula při potvrzování více než 255 po sobě jdoucích paketů.
- Range ack může být nula při odmítání více než 255 po sobě jdoucích paketů.
- Range nack a ack nemohou být oba nula.
- Po posledním rozsahu nejsou pakety ani potvrzeny ani odmítnuty. Délka ack bloku a způsob zpracování starých ack/nack záleží na odesílateli ack bloku. Viz diskuse v sekcích ack níže.
- Ack through by mělo být nejvyšší číslo přijatého paketu a všechny pakety s vyšším číslem nebyly přijaty. V omezených situacích však může být nižší, například při potvrzování jediného paketu, který "zaplní díru", nebo u zjednodušené implementace, která neudržuje stav všech přijatých paketů. Nad nejvyšším přijatým paketem nejsou pakety ani potvrzeny ani odmítnuty, ale po několika ack blocích může být vhodné přejít do režimu rychlého opakovaného odesílání.
- Tento formát je zjednodušenou verzí toho v QUIC. Je navržen pro efektivní kódování velkého počtu ACK společně se sériemi NACK.
- ACK bloky se používají k potvrzování paketů datové fáze. Mají být zahrnuty pouze pro pakety datové fáze v rámci relace.

#### Výzva cesty

Pro následující připojení. Obecně zahrnuto ve zprávách Session Created a Session Confirmed. Může být také znovu odesláno ve zprávě Data dlouhodobé relace, pokud předchozí token vyprší.

```
+----+----+----+----+----+----+----+----+
| 13 | 6 or 18 |   Port  | IP Address    
+----+----+----+----+----+----+----+----+
     |
+----+

blk :: 13
size :: 2 bytes, big endian, 6 or 18
port :: 2 bytes, big endian
ip :: 4 byte IPv4 or 16 byte IPv6 address,
      big endian (network byte order)
```
#### Odpověď cesty

Ping s libovolnými daty, která mají být vrácena v Path Response, používaný jako keep-alive nebo k validaci změny IP/Portu.

Poznámky:

```
+----+----+----+
| 15 |    0    |
+----+----+----+

blk :: 15
size :: 2 bytes, big endian, value = 0
```
#### Číslo prvního paketu

Pong s daty přijatými v Path Challenge, jako odpověď na Path Challenge, používaný jako keep-alive nebo k validaci změny IP/portu.

Volitelně zahrnuto v handshake v každém směru, pro specifikaci čísla prvního paketu, který bude odeslán. Toto poskytuje více bezpečnosti pro šifrování hlaviček, podobně jako u TCP.

```
+----+----+----+----+----+----+----+
| 16 |    4    |    relay tag      |
+----+----+----+----+----+----+----+

blk :: 16
size :: 2 bytes, big endian, value = 4
relay tag :: 4 bytes, big endian, nonzero
```
#### Přetížení

Není plně specifikováno, v současnosti není podporováno.

```
+----+----+----+----+----+----+----+----+
| 17 |   12    |     expires       |
+----+----+----+----+----+----+----+----+
                token              |
+----+----+----+----+----+----+----+

blk :: 17
size :: 2 bytes, big endian, value = 12
expires :: Unix timestamp, unsigned seconds.
           Wraps around in 2106
token :: 8 bytes, big endian
```
#### Výplň

Tento blok je navržen jako rozšiřitelná metoda pro výměnu informací o řízení zahlcení. Řízení zahlcení může být složité a může se vyvíjet, jak získáváme více zkušeností s protokolem při živém testování, nebo po úplném nasazení.

```
+----+----+----+----+----+----+----+----+
| 18 |  size   |    Arbitrary Data      |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 18
size :: 2 bytes, big endian, size of data to follow
data :: Arbitrary data to be returned in a Path Response
        length as selected by sender
```
Toto udržuje jakékoli informace o přetížení mimo vysoce používané I2NP, First Fragment, Followon Fragment a ACK bloky, kde není alokován prostor pro příznaky. Ačkoli jsou v hlavičce Data paketu tři bajty nevyužitých příznaků, i to poskytuje omezený prostor pro rozšiřitelnost a slabší ochranu šifrování.

- Doporučuje se minimální velikost dat 8 bajtů obsahující náhodná data, ale není vyžadována.
- Maximální velikost není specifikována, ale měla by být výrazně pod 1280, protože PMTU během fáze validace cesty je 1280.
- Velké velikosti výzev se nedoporučují, protože by mohly být vektorem pro útoky zesílení paketů.

#### Falšování adres peerů

Ačkoli je poněkud plýtvavé používat 4-bajtový blok pro dva bity informací, umístěním do samostatného bloku jej můžeme snadno rozšířit o další data, jako jsou aktuální velikosti oken, naměřené RTT nebo jiné příznaky. Zkušenosti ukázaly, že samotné bity příznaků jsou často nedostatečné a nepraktické pro implementaci pokročilých schémat řízení přetížení. Pokus o přidání podpory pro jakoukoliv možnou funkci řízení přetížení například do ACK bloku by plýtval místem a zvýšil složitost parsování tohoto bloku.

```
+----+----+----+----+----+----+----+----+
| 19 |  size   |                        |
+----+----+----+                        +
|    Data received in Path Challenge    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 19
size :: 2 bytes, big endian, size of data to follow
data :: As received in a Path Challenge
```
#### Podvržení adresy na trase

Implementace by neměly předpokládat, že druhý router podporuje jakýkoli konkrétní flag bit nebo funkci zde uvedenou, pokud implementace není vyžadována budoucí verzí této specifikace.

Tento blok by pravděpodobně měl být posledním blokem v datové části, který není výplňový.

```
+----+----+----+----+----+----+----+
| 20 |  size   |  First pkt number |
+----+----+----+----+----+----+----+

blk :: 20
size :: 4
pkt num :: The first packet number to be sent in the data phase
```
#### Předávání paketů mimo cestu

Toto je pro vyplnění uvnitř AEAD payloadů. Vyplnění pro všechny zprávy jsou uvnitř AEAD payloadů.

Padding by mělo přibližně dodržovat dohodnuté parametry. Bob poslal své požadované tx/rx min/max parametry v Session Created. Alice poslala své požadované tx/rx min/max parametry v Session Confirmed. Aktualizované možnosti mohou být odeslány během datové fáze. Viz informace o bloku možností výše.

Pokud je přítomen, musí to být poslední blok v datové části.

Poznámky:

SSU2 je navrženo tak, aby minimalizovalo dopad zpráv přehraných útočníkem.

```
+----+----+----+----+
| 21 |  size   |flag|
+----+----+----+----+

blk :: 21
size :: 1 (or more if extended)
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 1 to request immediate ack
       bit 1: 1 for explicit congestion notification (ECN)
       bits 7-2: Unused, set to 0 for future compatibility
```
#### Důsledky pro soukromí

Zprávy Token Request, Retry, Session Request, Session Created, Hole Punch a out-of-session Peer Test musí obsahovat bloky DateTime.

Alice i Bob ověřují, že čas těchto zpráv je v rámci platného odchýlení (doporučeno +/- 2 minuty). Pro "odolnost proti sondování" by Bob neměl odpovídat na Token Request nebo Session Request zprávy, pokud je odchýlení neplatné, protože tyto zprávy mohou být útokem typu replay nebo sondovacím útokem.

Bob si může zvolit zamítnutí duplicitních Token Request a Retry zpráv, i když je skew platný, pomocí Bloom filtru nebo jiného mechanismu. Nicméně velikost a CPU náklady na odpovědi na tyto zprávy jsou nízké. V nejhorším případě může přehraná Token Request zpráva zneplatnit dříve odeslaný token.

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
Systém tokenů výrazně minimalizuje dopad opakovaně přehrávaných Session Request zpráv. Jelikož tokeny mohou být použity pouze jednou, opakovaně přehrávaná Session Request zpráva nikdy nebude mít platný token. Bob si může zvolit odmítnutí duplikátních Session Request zpráv, i když je skew platný, prostřednictvím Bloom filtru nebo jiného mechanismu. Nicméně velikost a náklady na CPU pro odpověď s Retry zprávou jsou nízké. V nejhorším případě může odeslání Retry zprávy zneplatnit dříve odeslaný token.

- Velikost = 0 je povolena.
- Strategie paddingu TBD.
- Minimální padding TBD.
- Payloady obsahující pouze padding jsou povoleny.
- Výchozí hodnoty paddingu TBD.
- Viz blok options pro vyjednání parametrů paddingu
- Viz blok options pro parametry min/max paddingu
- Nepřekračujte MTU. Pokud je nutný více padding, pošlete více zpráv.
- Odpověď routeru na porušení vyjednaného paddingu závisí na implementaci.
- Délka paddingu má být buď rozhodována na základě jednotlivých zpráv a odhadů distribuce délky, nebo by měla být přidána náhodná zpoždění. Tato protiopatření mají být zahrnuta pro odolnost proti DPI, protože velikosti zpráv by jinak prozradily, že I2P provoz je přenášen transportním protokolem. Přesné schéma paddingu je oblastí budoucí práce, Příloha A dokumentu [NTCP2](/docs/specs/ntcp2) poskytuje více informací k tomuto tématu.

## Prevence opakování

Duplicitní zprávy Session Created a Session Confirmed se nebudou validovat, protože stav Noise handshake nebude ve správném stavu pro jejich dešifrování. V nejhorším případě může peer znovu odeslat Session Confirmed jako odpověď na zdánlivě duplicitní Session Created.

Opakované zprávy Hole Punch a Peer Test by měly mít malý nebo žádný dopad.

Routery musí používat číslo paketu datové zprávy k detekci a zahození duplicitních zpráv datové fáze. Každé číslo paketu by mělo být použito pouze jednou. Opakované zprávy musí být ignorovány.

Pokud Alice neobdrží Session Created nebo Retry:

Zachovejte stejné ID zdroje a připojení, dočasný klíč a číslo paketu 0. Nebo jednoduše podržte a znovu odešlete stejný zašifrovaný paket. Číslo paketu nesmí být zvýšeno, protože by to změnilo hodnotu zřetězeného hashe použitou k zašifrování zprávy Session Created.

Doporučené intervaly pro opětovné odesílání: 1,25, 2,5 a 5 sekund (1,25, 3,75 a 8,75 sekundy po prvním odeslání). Doporučený timeout: celkem 15 sekund

Pokud Bob neobdrží žádné Session Confirmed:

Zachovejte stejné zdrojové a spojovací ID, dočasný klíč a číslo paketu 0. Nebo jednoduše zachovejte zašifrovaný paket. Číslo paketu nesmí být zvýšeno, protože by to změnilo hodnotu zřetězeného hash použitého k šifrování zprávy Session Confirmed.

## Opětovné odeslání handshake

### Relace vytvořena

Doporučené intervaly pro opakované přenosy: 1, 2 a 4 sekundy (1, 3 a 7 sekund po prvním odeslání). Doporučený timeout: celkem 12 sekund

V SSU 1 Alice nepřechází do datové fáze, dokud neobdrží první datový paket od Boba. To činí z SSU 1 nastavení se dvěma zpáteční cestami.

Pro SSU 2, doporučené intervaly pro opakované přenosy Session Confirmed: 1,25, 2,5 a 5 sekund (1,25, 3,75 a 8,75 sekund po prvním odeslání).

### Relace potvrzena

Existuje několik alternativ. Všechny jsou 1 RTT:

1) Alice předpokládá, že Session Confirmed bylo přijato, posílá datové zprávy okamžitě, nikdy neretransmituje Session Confirmed. Datové pakety přijaté mimo pořadí (před Session Confirmed) budou nedešifrovatelné, ale budou retransmitovány. Pokud se Session Confirmed ztratí, všechny odeslané datové zprávy budou zahozeny. 2) Stejně jako v 1), posílat datové zprávy okamžitě, ale také retransmitovat Session Confirmed, dokud není přijata datová zpráva. 3) Mohli bychom použít IK místo XK, protože má pouze dvě zprávy v handshaku, ale používá extra DH (4 místo 3).

Doporučenou implementací je možnost 2). Alice musí zachovat informace potřebné k opětovnému odeslání zprávy Session Confirmed. Alice by také měla znovu odeslat všechny zprávy Data poté, co je zpráva Session Confirmed znovu odeslána.

### Požadavek na token

Při retransmisi Session Confirmed zachovejte stejné zdrojové a spojovací ID, dočasný klíč a číslo paketu 1. Nebo jednoduše podržte zašifrovaný paket. Číslo paketu nesmí být zvýšeno, protože by to změnilo hodnotu zřetězené hash, která je vstupem pro funkci split().

Bob může uchovat (zařadit do fronty) datové zprávy přijaté před zprávou Session Confirmed. Ani klíče pro ochranu hlavičky, ani dešifrovací klíče nejsou dostupné před přijetím zprávy Session Confirmed, takže Bob neví, že se jedná o datové zprávy, ale to lze předpokládat. Po přijetí zprávy Session Confirmed je Bob schopen dešifrovat a zpracovat datové zprávy ve frontě. Pokud je to příliš složité, Bob může nedešifrovatelné datové zprávy jednoduše zahodit, protože je Alice znovu odešle.

Poznámka: Pokud jsou pakety session confirmed ztraceny, Bob znovu odešle session created. Hlavička session created nebude rozšifrovatelná pomocí Alice's intro key, protože je nastavena s Bob's intro key (pokud není provedeno fallback dešifrování s Bob's intro key). Bob může okamžitě znovu odeslat pakety session confirmed, pokud nebyly dříve potvrzeny, a je přijat nešifrovatelný paket.

Pokud Alice neobdrží žádný Retry:

Udržujte stejné zdrojové a spojovací ID. Implementace může vygenerovat nové náhodné číslo paketu a zašifrovat nový paket; nebo může znovu použít stejné číslo paketu nebo pouze zachovat a znovu odeslat stejný zašifrovaný paket. Číslo paketu nesmí být zvýšeno, protože by to změnilo hodnotu zřetězeného hashe používanou k šifrování zprávy Session Created.

Doporučené intervaly pro opětovné odeslání: 3 a 6 sekund (3 a 9 sekund po prvním odeslání). Doporučený timeout: celkem 15 sekund

Pokud Bob neobdrží žádné Session Confirmed:

Zpráva Retry není při vypršení časového limitu retransmitována, aby se snížily dopady falešných zdrojových adres.

### Zkusit znovu

Nicméně zpráva Retry může být znovu odeslána v reakci na opakovanou zprávu Session Request přijatou s původním (neplatným) tokenem, nebo v reakci na opakovanou zprávu Token Request. V obou případech to znamená, že zpráva Retry byla ztracena.

Pokud je přijata druhá zpráva Session Request s odlišným, ale stále neplatným tokenem, zrušte čekající relaci a neodpovídejte.

Při opětovném odeslání zprávy Retry: Zachovejte stejné zdrojové a připojovací ID a token. Implementace může vygenerovat nové náhodné číslo paketu a zašifrovat nový paket; Nebo může znovu použít stejné číslo paketu nebo jen zachovat a znovu odeslat stejný zašifrovaný paket.

### Celkový timeout

Doporučený celkový časový limit pro handshake je 20 sekund.

Duplikáty tří zpráv Noise handshake Session Request, Session Created a Session Confirmed musí být detekovány před MixHash() hlavičky. Zatímco zpracování Noise AEAD pravděpodobně selže poté, handshake hash by již byl poškozen.

Pokud je kterákoli ze tří zpráv poškozena a selže AEAD, handshake již nelze následně obnovit ani pomocí opakovaného přenosu, protože MixHash() již byla volána na poškozenou zprávu.

Token v hlavičce Session Request se používá pro zmírnění DoS útoků, k zabránění falšování zdrojové adresy a jako ochrana proti replay útokům.

Pokud Bob nepřijme token ve zprávě Session Request, Bob NEDEŠIFRUJE zprávu, protože to vyžaduje nákladnou DH operaci. Bob jednoduše pošle zprávu Retry s novým tokenem.

### Duplikáty a zpracování chyb

Pokud je následně přijata zpráva Session Request s tímto tokenem, Bob pokračuje dešifrováním této zprávy a pokračuje v handshake.

### Čísla paketů

Token musí být náhodně generovaná 8bajtová hodnota, pokud generátor tokenu ukládá hodnoty a související IP a port (v paměti nebo trvale). Generátor nesmí generovat neprůhlednou hodnotu, například pomocí SipHash (s tajným seedem K0, K1) IP, portu a aktuální hodiny nebo dne, pro vytváření tokenů, které nemusí být uloženy v paměti, protože tato metoda ztěžuje odmítání znovu použitých tokenů a replay útoky. Je to však téma pro další studium, zda můžeme migrovat na takové schéma, jak to dělá [WireGuard](https://www.wireguard.com/papers/wireguard.pdf), používající 16bajtový HMAC serverového tajemství a IP adresy.

Tokeny mohou být použity pouze jednou. Token poslaný od Boba Alici ve zprávě Retry musí být použit okamžitě a vyprší během několika sekund. Token poslaný v bloku New Token v navázaném spojení může být použit v následujícím připojení a vyprší v čase specifikovaném v tomto bloku. Vypršení je specifikováno odesílatelem; doporučené hodnoty jsou několik minut minimálně, jedna nebo více hodin maximálně, v závislosti na požadované maximální režii uložených tokenů.

## Tokeny

Pokud se změní IP adresa nebo port routeru, musí smazat všechny uložené tokeny (jak příchozí, tak odchozí) pro starou IP adresu nebo port, protože již nejsou platné. Tokeny mohou být volitelně zachovány při restartech routeru, závisí to na implementaci. Přijetí nevypršelého tokenu není zaručeno; pokud Bob zapomněl nebo smazal své uložené tokeny, pošle Alice zprávu Retry. Router si může zvolit omezení úložiště tokenů a odebrat nejstarší uložené tokeny, i když nevypršely.

Nové bloky Token mohou být zasílány z Alice k Bobovi nebo z Boba k Alice. Obvykle by měly být zaslány alespoň jednou během navazování relace nebo krátce po něm. Kvůli validačním kontrolám RouterInfo ve zprávě Session Confirmed by Bob neměl zasílat blok New Token ve zprávě Session Created - může být zaslán s ACK 0 a Router Info poté, co je zpráva Session Confirmed přijata a validována.

Jelikož životnost relací je často delší než vypršení tokenů, token by měl být znovu odeslán před nebo po vypršení s novým časem vypršení, nebo by měl být odeslán nový token. Routery by měly předpokládat, že pouze poslední přijatý token je platný; neexistuje požadavek ukládat více příchozích nebo odchozích tokenů pro stejnou IP/port.

Token je vázán na kombinaci zdrojové IP/portu a cílové IP/portu. Token přijatý na IPv4 nesmí být použit pro IPv6 nebo naopak.

Pokud některý z peerů migruje na novou IP nebo port během relace (viz sekce Migrace připojení), všechny dříve vyměněné tokeny jsou zneplatněny a musí být vyměněny nové tokeny.

Implementace mohou, ale nemusí, ukládat tokeny na disk a znovu je načíst po restartu. Pokud jsou zachovány, implementace musí před jejich opětovným načtením zajistit, že se IP adresa a port nezměnily od vypnutí.

Rozdíly od SSU 1

Poznámka: Stejně jako u SSU 1, počáteční fragment neobsahuje informace o celkovém počtu fragmentů nebo celkové délce. Následující fragmenty neobsahují informace o svém offsetu. To poskytuje odesílateli flexibilitu fragmentovat "za běhu" na základě dostupného místa v paketu. (Java I2P to nedělá; "pre-fragmentuje" před odesláním prvního fragmentu) Nicméně to zatěžuje příjemce tím, že musí ukládat fragmenty přijaté mimo pořadí a odložit skládání, dokud nejsou přijaty všechny fragmenty.

Stejně jako v SSU 1, jakékoli opětovné odeslání fragmentů musí zachovat délku (a implicitní offset) předchozího přenosu fragmentu.

SSU 2 odděluje tři případy (úplnou zprávu, počáteční fragment a následující fragment) do tří různých typů bloků, aby se zlepšila efektivita zpracování.

Tento protokol NEUMOŽŇUJE úplnou ochranu před duplikovaným doručením I2NP zpráv. Duplikáty na IP vrstvě nebo replay útoky budou detekovány na SSU2 vrstvě, protože každé číslo paketu smí být použito pouze jednou.

## Fragmentace zpráv I2NP

Když jsou však I2NP zprávy nebo fragmenty znovu přeneseny v nových paketech, není to detekovatelné na vrstvě SSU2. Router by měl vynucovat expiraci I2NP (jak příliš staré, tak příliš daleko v budoucnosti) a použít Bloom filtr nebo jiný mechanismus založený na ID I2NP zprávy.

Router, nebo v implementaci SSU2, může používat dodatečné mechanismy pro detekci duplikátů. Například SSU2 by mohl udržovat cache nedávno přijatých ID zpráv. To závisí na implementaci.

Tato specifikace definuje protokol pro číslování paketů a ACK bloky. To poskytuje dostatečné informace v reálném čase pro vysílač k implementaci efektivního a responzivního algoritmu řízení zahlcení, přičemž umožňuje flexibilitu a inovace v této implementaci. Tato sekce diskutuje implementační cíle a poskytuje návrhy. Obecné pokyny lze nalézt v [RFC-9002](https://tools.ietf.org/html/rfc9002). Viz také [RFC-6298](https://tools.ietf.org/html/rfc6298) pro pokyny k časovačům retransmise.

Datové pakety typu ACK-only by se neměly započítávat do bajtů nebo paketů v přenosu a nepodléhají řízení přetížení. Na rozdíl od TCP může SSU2 detekovat ztrátu těchto paketů a tato informace může být použita k úpravě stavu přetížení. Tento dokument však nespecifikuje mechanismus pro takový postup.

## Duplikace I2NP zpráv

Pakety obsahující některé jiné nedatové bloky mohou být také vyloučeny z řízení zahlcení podle potřeby, závisí na implementaci. Například:

Doporučuje se, aby řízení zahlcení bylo založeno na počtu bajtů, nikoli na počtu paketů, podle pokynů v TCP RFC a QUIC [RFC-9002](https://tools.ietf.org/html/rfc9002). Dodatečný limit počtu paketů může být také užitečný pro předcházení přetečení bufferu v jádře nebo v middleboxech, v závislosti na implementaci, ačkoli to může přidat značnou složitost. Pokud je výstup paketů na relaci a/nebo celkový omezen šířkou pásma a/nebo řízen tempem, může to snížit potřebu omezování počtu paketů.

V SSU 1 obsahovaly ACK a NACK čísla I2NP zpráv a bitové masky fragmentů. Vysílače sledovaly stav ACK odchozích zpráv (a jejich fragmentů) a podle potřeby znovu přenášely fragmenty.

## Řízení přetížení

V SSU 2 obsahují ACK a NACK čísla paketů. Vysílače musí udržovat datovou strukturu s mapováním čísel paketů na jejich obsah. Když je paket potvrzen (ACK) nebo odmítnut (NACK), musí vysílač určit, které I2NP zprávy a fragmenty byly v daném paketu, aby se rozhodl, co znovu přenést.

Bob odesílá ACK paketu 0, které potvrzuje zprávu Session Confirmed a umožňuje Alice přejít do datové fáze a zahodit velkou zprávu Session Confirmed uloženou pro možné opětovné odeslání. Toto nahrazuje DeliveryStatusMessage odesílanou Bobem v SSU 1.

Bob by měl odeslat ACK co nejdříve po obdržení zprávy Session Confirmed. Malé zpoždění (ne více než 50 ms) je přijatelné, protože alespoň jedna Data zpráva by měla dorazit téměř okamžitě po zprávě Session Confirmed, takže ACK může potvrdit jak Session Confirmed, tak Data zprávu. Tím se zabrání tomu, aby Bob musel znovu odeslat zprávu Session Confirmed.

- Test peer
- Požadavek/úvod/odpověď relay
- Výzva/odpověď cesty

Definice: Pakety vyžadující potvrzení: Pakety, které obsahují bloky vyžadující potvrzení, vyvolají ACK od příjemce v rámci maximálního zpoždění potvrzení a nazývají se pakety vyžadující potvrzení.

### Potvrzení relace ACK

Routery potvrzují všechny pakety, které přijmou a zpracují. Pouze pakety vyžadující potvrzení však způsobí odeslání ACK bloku v rámci maximálního zpoždění potvrzení. Pakety, které nevyžadují potvrzení, jsou potvrzeny pouze tehdy, když je ACK blok odeslán z jiných důvodů.

Při odesílání paketu z jakéhokoli důvodu by se koncový bod měl pokusit zahrnout ACK blok, pokud nebyl nedávno odeslán. Tím se pomáhá s včasnou detekcí ztrát u protějšku.

### Generování ACK

Obecně platí, že častá zpětná vazba od příjemce zlepšuje reakci na ztráty a přetížení, ale toto je třeba vyvážit proti nadměrné zátěži generované příjemcem, který posílá ACK blok v reakci na každý packet vyžadující potvrzení. Níže uvedené pokyny se snaží nalézt tuto rovnováhu.

Datové pakety v rámci relace obsahující jakýkoliv blok KROMĚ následujících vyžadují potvrzení:

### Potvrzení handshake

Pakety mimo relaci, včetně handshake zpráv a peer test zpráv 5-7, mají své vlastní mechanismy potvrzování. Viz níže.

Toto jsou speciální případy:

ACK bloky se používají k potvrzování paketů datové fáze. Mají být zahrnuty pouze pro pakety datové fáze v rámci relace.

Každý paket by měl být potvrzen alespoň jednou a pakety vyžadující potvrzení musí být potvrzeny alespoň jednou v rámci maximálního zpoždění.

Koncový bod musí okamžitě potvrdit všechny handshake pakety vyžadující potvrzení v rámci svého maximálního zpoždění, s následující výjimkou. Před potvrzením handshake nemusí mít koncový bod šifrovací klíče hlavičky paketu pro dešifrování paketů při jejich přijetí. Proto je může ukládat do vyrovnávací paměti a potvrdit je až když budou k dispozici požadované klíče.

- ACK blok
- Adresní blok
- DateTime blok
- Padding blok
- Ukončovací blok
- Další?

Protože pakety obsahující pouze ACK bloky nepodléhají řízení zahlcení, nesmí koncový bod odeslat více než jeden takový paket jako odpověď na přijetí paketu vyžadujícího potvrzení.

### Odesílání ACK bloků

Koncový bod nesmí odeslat non-ack-eliciting paket v reakci na non-ack-eliciting paket, i když existují mezery v paketech, které předcházejí přijatému paketu. Tím se zabrání nekonečné zpětnovazební smyčce potvrzení, která by mohla zabránit tomu, aby se spojení kdy stalo nečinným. Non-ack-eliciting pakety jsou nakonec potvrzeny, když koncový bod odešle ACK blok v reakci na jiné události.

- Token Request je implicitně potvrzena pomocí Retry
- Session Request je implicitně potvrzena pomocí Session Created nebo Retry
- Retry je implicitně potvrzena pomocí Session Request
- Session Created je implicitně potvrzena pomocí Session Confirmed
- Session Confirmed by měla být potvrzena okamžitě

### Frekvence ACK

Koncový bod, který posílá pouze ACK bloky, neobdrží potvrzení od svého protějšku, pokud nejsou tato potvrzení zahrnuta v paketech s bloky vyžadujícími potvrzení. Koncový bod by měl poslat ACK blok s ostatními bloky, když existují nové pakety vyžadující potvrzení, které je třeba potvrdit. Když je třeba potvrdit pouze pakety nevyžadující potvrzení, koncový bod MŮŽE zvolit neposílání ACK bloku s odchozími bloky, dokud neobdrží paket vyžadující potvrzení.

Koncový bod, který odesílá pouze pakety nevyžadující potvrzení, se může rozhodnout občas přidat do těchto paketů blok vyžadující potvrzení, aby zajistil, že obdrží potvrzení. V takovém případě NESMÍ koncový bod poslat blok vyžadující potvrzení ve všech paketech, které by jinak nevyžadovaly potvrzení, aby se předešlo nekonečné smyčce potvrzování.

Aby se pomohlo detekci ztráty na straně odesílatele, měl by koncový bod generovat a odeslat ACK blok bez prodlení, když obdrží paket vyžadující potvrzení v kterémkoli z těchto případů:

Očekává se, že algoritmy budou odolné vůči příjemcům, kteří nebudou dodržovat výše uvedené pokyny. Implementace by se však měla odchýlit od těchto požadavků pouze po pečlivém zvážení dopadů změny na výkon, a to jak pro připojení vytvořená koncovým bodem, tak pro ostatní uživatele sítě.

Příjemce určuje, jak často odesílat potvrzení v reakci na pakety vyžadující potvrzení. Toto rozhodování zahrnuje kompromis.

Koncové body spoléhají na včasné potvrzení pro detekci ztráty. Řadiče zahlcení založené na oknech spoléhají na potvrzení pro správu svého okna zahlcení. V obou případech může zpožďování potvrzení negativně ovlivnit výkon.

Na druhé straně snížení frekvence paketů, které nesou pouze potvrzení, snižuje náklady na přenos a zpracování paketů na obou koncových bodech. Může to zlepšit propustnost připojení na silně asymetrických linkách a snížit objem potvrzovacího provozu využívajícího kapacitu zpětné cesty; viz Sekce 3 v [RFC-3449](https://tools.ietf.org/html/rfc3449).

Příjemce by měl odeslat ACK blok po přijetí alespoň dvou paketů vyžadujících potvrzení. Toto doporučení má obecnou povahu a je v souladu s doporučeními pro chování TCP koncového bodu [RFC-5681](https://tools.ietf.org/html/rfc5681). Znalost síťových podmínek, znalost kontroléru přetížení protějšku nebo další výzkum a experimentování může navrhnout alternativní strategie potvrzování s lepšími výkonnostními charakteristikami.

- Když má přijatý paket číslo paketu menší než jiný paket vyžadující potvrzení, který byl přijat
- Když má paket číslo paketu větší než paket s nejvyšším číslem vyžadující potvrzení, který byl přijat, a mezi tímto paketem a daným paketem chybí pakety.
- Když je v hlavičce paketu nastaven příznak ack-immediate

Příjemce může zpracovat více dostupných paketů před rozhodnutím, zda v odpovědi odeslat ACK blok. Obecně by příjemce neměl zdržovat ACK o více než RTT / 6, nebo maximálně 150 ms.

### Příznak okamžitého ACK

Příznak ack-immediate v hlavičce datového paketu je požadavek, aby příjemce odeslal potvrzení brzy po přijetí, pravděpodobně během několika ms. Obecně by příjemce neměl zpozdit okamžité ACK o více než RTT / 16, nebo maximálně 5 ms.

Příjemce nezná velikost odesílacího okna odesílatele, a proto neví, jak dlouho má čekat před odesláním ACK. Příznak okamžitého ACK v hlavičce datového paketu je důležitým způsobem, jak udržet maximální propustnost minimalizací efektivního RTT. Příznak okamžitého ACK je bajt 13 hlavičky, bit 0, tj. (header[13] & 0x01). Když je nastaven, je požadováno okamžité ACK. Podrobnosti viz sekce krátké hlavičky výše.

Existuje několik možných strategií, které může odesílatel použít k určení, kdy nastavit příznak immediate-ack:

Příznaky okamžitého ACK by měly být nutné pouze u datových paketů obsahujících I2NP zprávy nebo fragmenty zpráv.

Když je odeslán ACK blok, je zahrnuto jedno nebo více rozsahů potvrzených paketů. Zahrnutí potvrzení pro starší pakety snižuje pravděpodobnost falešných retransmisí způsobených ztrátou dříve odeslaných ACK bloků, za cenu větších ACK bloků.

ACK bloky by měly vždy potvrdit nejnověji přijaté pakety, a čím více jsou pakety mimo pořadí, tím důležitější je rychle odeslat aktualizovaný ACK blok, aby se zabránilo tomu, že protistrana prohlásí paket za ztracený a zbytečně znovu přenese bloky, které obsahuje. ACK blok se musí vejít do jediného paketu. Pokud se nevejde, pak jsou starší rozsahy (ty s nejmenšími čísly paketů) vynechány.

### Velikost bloku ACK

Příjemce omezuje počet ACK rozsahů, které si pamatuje a posílá v ACK blocích, jak pro omezení velikosti ACK bloků, tak pro předejití vyčerpání zdrojů. Po obdržení potvrzení pro ACK blok by měl příjemce přestat sledovat tyto potvrzené ACK rozsahy. Odesílatelé mohou očekávat potvrzení pro většinu paketů, ale tento protokol nezaručuje obdržení potvrzení pro každý paket, který příjemce zpracuje.

Je možné, že uchovávání mnoha ACK rozsahů by mohlo způsobit, že ACK blok se stane příliš velkým. Příjemce může zahodit nepotvrzené ACK rozsahy, aby omezil velikost ACK bloku, za cenu zvýšených opakovaných přenosů od odesílatele. To je nutné, pokud by ACK blok byl příliš velký na to, aby se vešel do paketu. Příjemci mohou také dále omezit velikost ACK bloku, aby zachovali místo pro další bloky nebo aby omezili šířku pásma, kterou potvrzení spotřebovávají.

- Nastavit jednou každých N paketů, pro malé N
- Nastavit na posledním paketu v sérii paketů
- Nastavit kdykoliv je odesílací okno téměř plné, například přes 2/3 plné
- Nastavit na všech paketech s retransmitovanými fragmenty

Příjemce musí zachovat rozsah ACK, pokud nemůže zajistit, že následně nepřijme pakety s čísly v tomto rozsahu. Udržování minimálního čísla paketu, které se zvyšuje při zahazování rozsahů, je jedním ze způsobů, jak toho dosáhnout s minimálním stavem.

### Omezování rozsahů sledováním ACK bloků

Příjemci mohou zahodit všechny ACK rozsahy, ale musí si ponechat největší číslo paketu, které bylo úspěšně zpracováno, protože se používá k obnovení čísel paketů z následujících paketů.

Následující sekce popisuje příkladný přístup k určování, které pakety potvrdit v každém ACK bloku. Ačkoli cílem tohoto algoritmu je vygenerovat potvrzení pro každý paket, který je zpracován, stále je možné, že se potvrzení ztratí.

Když je odeslán paket obsahující ACK blok, pole Ack Through v tomto bloku může být uloženo. Když je paket obsahující ACK blok potvrzen, příjemce může přestat potvrzovat pakety menší nebo rovné poli Ack Through v odeslaném ACK bloku.

Příjemce, který odesílá pouze pakety nevyžadující potvrzení, jako jsou bloky ACK, nemusí dlouhou dobu obdržet žádné potvrzení. To by mohlo způsobit, že si příjemce bude dlouhou dobu udržovat stav pro velký počet bloků ACK a bloky ACK, které odesílá, by mohly být zbytečně velké. V takovém případě by mohl příjemce příležitostně odeslat PING nebo jiný malý blok vyžadující potvrzení, například jednou za jeden round trip, aby vyžádal ACK od protějšku.

V případech bez ztráty ACK bloků tento algoritmus umožňuje minimálně 1 RTT přeuspořádání. V případech se ztrátou ACK bloků a přeuspořádáním tento přístup nezaručuje, že každé potvrzení bude odesílatelem viděno předtím, než již nebude zahrnuto v ACK bloku. Pakety mohou být přijaty mimo pořadí a všechny následující ACK bloky je obsahující mohou být ztraceny. V tomto případě může algoritmus obnovy po ztrátě způsobit falešné přenosy, ale odesílatel bude pokračovat v postupu vpřed.

I2P transporty nezaručují doručení I2NP zpráv ve správném pořadí. Proto ztráta Data zprávy obsahující jednu nebo více I2NP zpráv či fragmentů NEZABRÁNÍ doručení ostatních I2NP zpráv; nedochází k blokování na začátku fronty. Implementace by měly pokračovat v odesílání nových zpráv během fáze obnovy ztracených dat, pokud to odesílací okno umožňuje.

Odesílatel by neměl uchovávat úplný obsah zprávy pro identické opětovné odeslání (kromě handshake zpráv, viz výše). Odesílatel musí při každém odesílání sestavit zprávy obsahující aktuální informace (ACK, NACK a nepotvrzená data). Odesílatel by se měl vyhnout opětovnému odesílání informací ze zpráv, jakmile jsou potvrzeny. To zahrnuje zprávy, které jsou potvrzeny poté, co byly prohlášeny za ztracené, což se může stát při přeuspořádání v síti.

### Zahlcení

TBD. Obecné pokyny lze nalézt v [RFC-9002](https://tools.ietf.org/html/rfc9002).

IP adresa nebo port peera se může během životnosti relace změnit. Změna IP adresy může být způsobena rotací dočasných IPv6 adres, periodickou změnou IP adresy řízenou poskytovatelem internetových služeb, mobilním klientem přecházejícím mezi WiFi a mobilními IP adresami nebo jinými změnami v místní síti. Změna portu může být způsobena opětovným navázáním NAT poté, co předchozí navázání vypršelo.

IP adresa nebo port peer může vypadat, že se změnila kvůli různým útokům na cestě i mimo cestu, včetně modifikování nebo vkládání paketů.

### Opětovný přenos

Migrace připojení je proces, při kterém je validován nový zdrojový endpoint (IP+port), zatímco se zabraňuje změnám, které nejsou validovány. Tento proces je zjednodušenou verzí procesu definovaného v QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000). Tento proces je definován pouze pro datovou fázi relace. Migrace není povolena během handshake. Všechny handshake pakety musí být ověřeny, že pocházejí ze stejné IP a portu jako dříve odeslané a přijaté pakety. Jinými slovy, IP a port protějšku musí být konstantní během handshake.

### Okno

(Adaptováno z QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000))

### Model hrozeb

Peer může falšovat svou zdrojovou adresu, aby způsobil, že endpoint pošle nadměrné množství dat neochotnému hostiteli. Pokud endpoint pošle výrazně více dat než falšující peer, migrace připojení může být použita k zesílení objemu dat, který může útočník generovat směrem k oběti.

## Migrace připojení

Útočník na cestě by mohl způsobit falešnou migraci spojení zkopírováním a přeposláním paketu s falešnou adresou tak, aby dorazil před původním paketem. Paket s falešnou adresou bude vypadat, jako by pocházel z migrujícího spojení, a původní paket bude považován za duplikát a bude zahozen. Po falešné migraci se ověření zdrojové adresy nezdaří, protože entita na zdrojové adrese nemá potřebné kryptografické klíče ke čtení nebo odpovědi na Path Challenge, který jí byl zaslán, i kdyby chtěla.

Útočník mimo cestu, který může pozorovat pakety, může předávat kopie skutečných paketů koncovým bodům. Pokud kopírovaný paket dorazí před skutečným paketem, bude to vypadat jako NAT rebinding. Jakýkoli skutečný paket bude zahozen jako duplikát. Pokud je útočník schopen pokračovat v předávání paketů, může být schopen způsobit migraci na cestu přes útočníka. To umístí útočníka na cestu, což mu dává schopnost pozorovat nebo zahazovat všechny následující pakety.

QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) specifikuje změnu connection ID při změně síťových cest. Použití stabilního connection ID na více síťových cestách by umožnilo pasivnímu pozorovateli korelovat aktivitu mezi těmito cestami. Endpoint, který se pohybuje mezi sítěmi, si nemusí přát, aby jejich aktivita byla korelována jakoukoli entitou jinou než jejich protistrana. QUIC však nešifruje connection ID v hlavičce. SSU2 to dělá, takže únik soukromí by vyžadoval, aby pasivní pozorovatel měl také přístup k síťové databázi, aby získal introduction key potřebný k dešifrování connection ID. I s introduction key se nejedná o silný útok a v SSU2 neměníme connection ID po migraci, protože by to představovalo významnou komplikaci.

### Zahajování validace cesty

Během datové fáze musí uzly kontrolovat zdrojovou IP adresu a port každého přijatého datového paketu. Pokud se IP adresa nebo port liší od dříve přijatých, A paket není duplikátním číslem paketu, A paket se úspěšně dešifruje, relace vstoupí do fáze validace cesty.

#### Výběr introducer

Navíc musí peer ověřit, že nová IP adresa a port jsou platné podle místních validačních pravidel (nejsou blokované, nejedná se o zakázané porty, atd.). Peery NEJSOU povinni podporovat migraci mezi IPv4 a IPv6 a mohou považovat novou IP adresu v jiné adresní rodině za neplatnou, jelikož se nejedná o očekávané chování a může to přidat značnou implementační složitost. Po obdržení paketu z neplatné IP adresy/portu může implementace paket jednoduše zahodit nebo může zahájit validaci cesty se starou IP adresou/portem.

#### Zpracování odpovědi

Po vstupu do fáze validace cesty proveďte následující kroky:

#### Introducers

Během fáze validace cesty může relace pokračovat ve zpracování příchozích paketů. Ať už ze staré nebo nové IP/portu. Relace může také pokračovat v odesílání a potvrzování datových paketů. Okno zahlcení a PMTU však musí během fáze validace cesty zůstat na minimálních hodnotách, aby se zabránilo jejich využití pro útoky odmítnutí služby zasíláním velkého množství provozu na falešnou adresu.

#### Skrývání identity

Implementace může, ale není vyžadováno, aby se pokusila validovat více cest současně. To pravděpodobně nestojí za složitost. Může, ale není vyžadováno, aby si pamatovala předchozí IP/port jako již validovaný a přeskočila validaci cesty, pokud se peer vrátí na svou předchozí IP/port.

### Obsah zprávy

Pokud je přijata Path Response obsahující identická data odeslaná v Path Challenge, ověření cesty bylo úspěšné. Zdrojová IP adresa/port zprávy Path Response nemusí být stejná jako ta, na kterou byla odeslána Path Challenge.

Pokud není Path Response přijata před vypršením časovače Path Response, odešlete další Path Challenge a zdvojnásobte časovač Path Response.

Pokud není Path Response přijata před vypršením časovače Path Validation, Path Validation selhala.

- Spustit časovač pro timeout validace cesty na několik sekund, nebo několikanásobek aktuálního RTO (TBD)
- Snížit congestion window na minimum
- Snížit PMTU na minimum (1280)
- Poslat datový paket obsahující blok Path Challenge, blok Address (obsahující novou IP/port) a typicky blok ACK, na novou IP a port. Tento paket používá stejné connection ID a šifrovací klíče jako aktuální session. Data bloku Path Challenge musí obsahovat dostatečnou entropii (alespoň 8 bajtů), aby nemohla být falšována.
- Volitelně také poslat Path Challenge na starou IP/port s jinými daty bloku. Viz níže.
- Spustit časovač pro timeout Path Response založený na aktuálním RTO (typicky RTT + násobek RTTdev)

Zprávy Data by měly obsahovat následující bloky. Pořadí není specifikováno s výjimkou toho, že Padding musí být poslední:

Nedoporučuje se zahrnovat do zprávy žádné další bloky (například I2NP).

Je povoleno zahrnout blok Path Challenge do zprávy obsahující Path Response, aby se iniciovala validace v opačném směru.

Bloky Path Challenge a Path Response vyvolávají ACK. Path Challenge bude potvrzen Data zprávou obsahující bloky Path Response a ACK. Path Response by měl být potvrzen Data zprávou obsahující blok ACK.

Specifikace QUIC není jasná ohledně toho, kam posílat datové pakety během validace cesty - na starou nebo novou IP/port? Je třeba najít rovnováhu mezi rychlou reakcí na změny IP/port a neposíláním provozu na falešné adresy. Také falešné pakety nesmí být dovoleny podstatně ovlivnit existující relaci. Změny pouze portu jsou pravděpodobně způsobeny přenavázáním NAT po období nečinnosti; změny IP se mohou stát během fází s vysokým provozem v jednom nebo obou směrech.

### Směrování během ověřování cesty

Strategie podléhají výzkumu a zdokonalování. Mezi možnosti patří:

- Path Challenge nebo Path Response blok. Path Challenge obsahuje neprůhledná data, doporučuje se minimálně 8 bajtů. Path Response obsahuje data z Path Challenge.
- Address blok obsahující zdánlivou IP adresu příjemce
- DateTime blok
- ACK blok
- Padding blok

Po obdržení Path Challenge musí peer odpovědět datovým paketem obsahujícím Path Response s daty z Path Challenge.

Path Response musí být odeslána na IP/port, ze kterého byla přijata Path Challenge. Toto NEMUSÍ BÝT nutně IP/port, který byl dříve navázán pro protějšek. Tím se zajistí, že validace cesty protějškem uspěje pouze tehdy, pokud je cesta funkční v obou směrech. Viz sekci Validace po lokální změně níže.

Pokud se IP/port neliší od dříve známé IP/portu pro peer, považujte Path Challenge za jednoduchý ping a jednoduše odpovězte bezpodmínečně pomocí Path Response. Příjemce si neuchová ani nezmění žádný stav na základě přijaté Path Challenge. Pokud se IP/port liší, peer musí ověřit, že nová IP a port jsou platné podle místních validačních pravidel (nejsou blokované, nejsou nepovolené porty atd.). Peery NEJSOU povinny podporovat odpovědi napříč rodinami adres mezi IPv4 a IPv6 a mohou považovat novou IP v jiné rodině adres za neplatnou, protože se nejedná o očekávané chování.

### Odpověď na Path Challenge

Pokud není omezena řízením zahlcení, měla by být Path Response odeslána okamžitě. Implementace by měly přijmout opatření k omezení rychlosti Path Response nebo využité šířky pásma, pokud je to nutné.

Blok Path Challenge je obecně doprovázen blokem Address ve stejné zprávě. Pokud blok adresy obsahuje novou IP/port, peer může validovat tuto IP/port a zahájit peer testování této nové IP/port, se session peerem nebo jakýmkoli jiným peerem. Pokud si peer myslí, že je za firewallem, a změnil se pouze port, tato změna je pravděpodobně způsobena NAT rebindingem a další peer testování pravděpodobně není potřeba.

- Neposílání datových paketů na novou IP/port dokud není ověřena
- Pokračování v posílání datových paketů na starou IP/port dokud není nová IP/port ověřena
- Současné opětovné ověřování staré IP/port
- Neposílání žádných dat dokud není ověřena buď stará nebo nová IP/port
- Různé strategie pro změnu pouze portu oproti změně IP
- Různé strategie pro IPv6 změnu ve stejném /32, pravděpodobně způsobenou rotací dočasných adres

### Úspěšná validace cesty

Po úspěšné validaci cesty je spojení plně migrováno na novou IP/port. Po úspěchu:

Během fáze validace cesty způsobí jakékoli platné, neduplikátní pakety přijaté ze staré IP/portu, které jsou úspěšně dešifrovány, zrušení validace cesty. Je důležité, aby zrušená validace cesty způsobená podvrženým paketem nezpůsobila ukončení nebo výrazné narušení platné relace.

Při zrušené validaci cesty:

Je důležité, aby neúspěšné ověření cesty, způsobené padělaným paketem, nezpůsobilo ukončení nebo významné narušení platné relace.

Při neúspěšném ověření cesty:

### Zrušení validace cesty

Výše uvedený proces je definován pro peer-y, kteří obdrží paket ze změněné IP/portu. Nicméně může být také zahájen v opačném směru, peer-em, který zjistí, že se změnila jeho IP nebo port. Peer může být schopen zjistit, že se změnila jeho lokální IP; je však mnohem méně pravděpodobné, že zjistí změnu svého portu z důvodu NAT rebindingu. Proto je toto volitelné.

- Ukončit fázi validace cesty
- Všechny pakety jsou odesílány na novou IP a port.
- Omezení na congestion window a PMTU jsou odstraněna a je jim umožněno zvyšovat se. Jednoduše je neobnovujte na staré hodnoty, protože nová cesta může mít odlišné charakteristiky.
- Pokud se IP změnila, nastavte vypočítané RTT a RTO na počáteční hodnoty. Protože změny pouze portu jsou běžně výsledkem NAT rebinding nebo jiné middlebox aktivity, peer může místo toho zachovat svůj stav congestion control a odhad round-trip v těchto případech namísto návratu k počátečním hodnotám.
- Smazat (invalidovat) jakékoli tokeny odeslané nebo přijaté pro starou IP/port (volitelné)
- Odeslat nový token block pro novou IP/port (volitelné)

### Neúspěšné ověření cesty

Při obdržení path challenge od protějšku, jehož IP nebo port se změnil, by měl druhý protějšek zahájit path challenge v opačném směru.

Bloky Path Challenge a Path Response mohou být použity kdykoli jako pakety Ping/Pong. Příjem bloku Path Challenge nemění žádný stav na straně příjemce, pokud není přijat z jiné IP/portu.

- Ukončit fázi validace cesty
- Všechny pakety jsou odesílány na starou IP a port.
- Omezení na congestion window a PMTU jsou odstraněna a je jim povoleno se zvýšit, nebo volitelně obnovit předchozí hodnoty
- Znovu odeslat všechny datové pakety, které byly dříve odeslány na novou IP/port, na starou IP/port.

### Ověření po lokální změně

Uzly by neměly navazovat více relací se stejným uzlem, ať už SSU 1 nebo 2, nebo se stejnými či různými IP adresami. To se však může stát buď kvůli chybám, nebo kvůli ztrátě předchozí zprávy o ukončení relace, nebo v situaci, kdy zpráva o ukončení ještě nedorazila.

Pokud má Bob existující relaci s Alicí, když Bob obdrží Session Confirmed od Alice, čímž dokončí handshake a vytvoří novou relaci, Bob by měl:

- Ukončit fázi validace cesty
- Všechny pakety jsou odesílány na starou IP a port.
- Omezení na okno zahlcení a PMTU jsou odstraněna a je jim umožněno se zvyšovat.
- Volitelně spustit validaci cesty na staré IP a portu. Pokud selže, ukončit relaci.
- Jinak následovat standardní pravidla pro vypršení času relace a ukončení.
- Znovu odeslat všechny datové pakety, které byly dříve odeslány na novou IP/port, na starou IP/port.

### Použití jako Ping/Pong

Relace ve fázi handshake jsou obecně ukončovány jednoduše vypršením časového limitu nebo dalším neodpovídáním. Volitelně mohou být ukončeny zahrnutím Termination bloku v odpovědi, ale na většinu chyb není možné odpovědět kvůli nedostupnosti kryptografických klíčů. I když jsou klíče pro odpověď včetně termination bloku dostupné, obvykle se nevyplatí spotřebovávat CPU na provedení DH pro odpověď. Výjimkou MŮŽE být Termination blok ve zprávě o opakování pokusu, který je levný na vygenerování.

Relace ve fázi dat jsou ukončeny odesláním datové zprávy, která obsahuje blok Termination. Tato zpráva by měla také obsahovat blok ACK. Může, pokud relace byla aktivní dostatečně dlouho, že dříve odeslaný token vypršel nebo brzy vyprší, obsahovat blok New Token. Tato zpráva nevyžaduje potvrzení. Při přijetí bloku Termination s jakýmkoli důvodem kromě "Termination Received" protějšek odpovídá datovou zprávou obsahující blok Termination s důvodem "Termination Received".

### Fáze handshake

Po odeslání nebo přijetí Termination bloku by relace měla přejít do uzavírací fáze na určité maximální časové období, které bude ještě určeno. Uzavírací stav je nezbytný pro ochranu proti ztrátě paketu obsahujícího Termination blok a paketů cestujících opačným směrem. Během uzavírací fáze není požadavek zpracovávat další přijaté pakety. Relace v uzavíracím stavu odešle paket obsahující Termination blok v odpovědi na jakýkoliv příchozí paket, který přiřadí k dané relaci. Relace by měla omezit rychlost, s jakou generuje pakety v uzavíracím stavu. Například relace může čekat na postupně se zvyšující počet přijatých paketů nebo dobu před odpovídáním na přijaté pakety.

## Více relací

Pro minimalizaci stavu, který router udržuje pro ukončovanou relaci, mohou relace (ale nejsou povinny) poslat přesně stejný paket se stejným číslem paketu tak, jak je, jako odpověď na jakýkoli přijatý paket. Poznámka: Povolení retransmise ukončovacího paketu je výjimkou z požadavku, aby bylo pro každý paket použito nové číslo paketu. Posílání nových čísel paketů je primárně výhodné pro obnovu ztracených paketů a řízení zahlcení, což se u uzavřeného spojení nepředpokládá jako relevantní. Retransmise finálního paketu vyžaduje méně stavu.

Po obdržení Termination bloku s důvodem "Termination Received" může relace ukončit zavírací fázi.

- Migrovat všechny neodeslané nebo nepotvrzené odchozí I2NP zprávy ze staré relace do nové
- Odeslat ukončení s kódem důvodu 22 na staré relaci
- Odstranit starou relaci a nahradit ji novou

## Ukončení relace

### Datová fáze

Při jakémkoliv normálním nebo abnormálním ukončení by routery měly vynulovat veškerá dočasná data v paměti, včetně dočasných klíčů pro handshake, symetrických kryptografických klíčů a souvisejících informací.

### Vyčištění

Požadavky se liší podle toho, zda je publikovaná adresa sdílena s SSU 1. Současné minimum pro SSU 1 IPv4 je 620, což je rozhodně příliš málo.

Minimální SSU2 MTU je 1280 jak pro IPv4, tak pro IPv6, což je stejné jako specifikováno v [RFC-9000](https://tools.ietf.org/html/rfc9000). Viz níže. Zvýšením minimálního MTU se 1 KB tunnel zprávy a krátké tunnel build zprávy vejdou do jednoho datagramu, což značně sníží typické množství fragmentace. To také umožňuje zvýšení maximální velikosti I2NP zpráv. 1820-bajtové streaming zprávy by se měly vejít do dvou datagramů.

Router nesmí povolit SSU2 nebo publikovat SSU2 adresu, pokud není MTU pro danou adresu alespoň 1280.

Routery musí publikovat nevýchozí MTU v každé SSU nebo SSU2 router adrese.

### SSU adresa

Sdílená adresa s SSU 1, musí dodržovat pravidla SSU 1. IPv4: Výchozí a maximální hodnota je 1484. Minimální je 1292. (IPv4 MTU + 4) musí být násobkem 16. IPv6: Musí být publikováno, minimální hodnota je 1280 a maximální je 1488. IPv6 MTU musí být násobkem 16.

## MTU

IPv4: Výchozí a maximum je 1500. Minimum je 1280. IPv6: Výchozí a maximum je 1500. Minimum je 1280. Žádná pravidla násobků 16, ale mělo by to být pravděpodobně alespoň násobek 2.

Pro SSU 1 současná Java I2P provádí PMTU discovery tím, že začíná s malými pakety a postupně zvětšuje velikost, nebo zvětšuje na základě velikosti přijatých paketů. Toto je hrubý přístup a výrazně snižuje efektivitu. Pokračování této funkce v SSU 2 je TBD.

Nedávné studie [PMTU](https://en.wikipedia.org/wiki/Path_MTU_Discovery) naznačují, že minimum pro IPv4 ve výši 1200 nebo více by fungovalo pro více než 99% připojení. QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) vyžaduje minimální velikost IP paketu 1280 bajtů.

citace [RFC-9000](https://tools.ietf.org/html/rfc9000):

### SSU2 Address

Maximální velikost datagramu je definována jako největší velikost UDP payload, která může být odeslána přes síťovou cestu pomocí jediného UDP datagramu. QUIC NESMÍ být použit, pokud síťová cesta nepodporuje maximální velikost datagramu alespoň 1200 bajtů.

### Zjišťování PMTU

QUIC předpokládá minimální velikost IP paketu alespoň 1280 bajtů. To je minimální velikost IPv6 [IPv6] a je také podporována většinou moderních IPv4 sítí. Za předpokladu minimální velikosti IP hlavičky 40 bajtů pro IPv6 a 20 bajtů pro IPv4 a velikosti UDP hlavičky 8 bajtů, to má za následek maximální velikost datagramu 1232 bajtů pro IPv6 a 1252 bajtů pro IPv4. Proto se očekává, že moderní IPv4 a všechny IPv6 síťové cesty budou schopny podporovat QUIC.

### Minimální velikost handshake

Poznámka: Tento požadavek na podporu UDP payload o velikosti 1200 bajtů omezuje prostor dostupný pro IPv6 rozšiřující hlavičky na 32 bajtů nebo IPv4 volby na 52 bajtů, pokud cesta podporuje pouze minimální IPv6 MTU 1280 bajtů. To ovlivňuje počáteční pakety a validaci cesty.

konec citace

QUIC vyžaduje, aby počáteční datagramy v obou směrech měly alespoň 1200 bajtů, aby se předešlo zesilovacím útokům a zajistilo se, že PMTU to podporuje v obou směrech.

Mohli bychom to vyžadovat pro Session Request a Session Created, za významných nákladů na šířku pásma. Možná bychom to mohli dělat pouze pokud nemáme token, nebo poté, co je přijata zpráva Retry. TBD

QUIC vyžaduje, aby Bob neposílal více než trojnásobek množství dat přijatých, dokud není adresa klienta ověřena. SSU2 tento požadavek splňuje inherentně, protože zpráva Retry má přibližně stejnou velikost jako zpráva Token Request a je menší než zpráva Session Request. Zpráva Retry se také posílá pouze jednou.

QUIC vyžaduje, aby zprávy obsahující bloky PATH_CHALLENGE nebo PATH_RESPONSE měly alespoň 1200 bajtů, aby se předešlo zesilovacím útokům a zajistilo se, že PMTU to podporuje v obou směrech.

Mohli bychom to také vyžadovat, za cenu značného nárůstu spotřeby šířky pásma. Tyto případy by však měly být vzácné. TBD

### Minimální velikost zprávy cesty

IPv4: Nepředpokládá se fragmentace IP. IP + hlavička datagramu je 28 bajtů. Toto předpokládá žádné IPv4 volby. Maximální velikost zprávy je MTU - 28. Hlavička datové fáze je 16 bajtů a MAC je 16 bajtů, celkem 32 bajtů. Velikost payloadu je MTU - 60. Maximální payload datové fáze je 1440 pro maximální MTU 1500. Maximální payload datové fáze je 1220 pro minimální MTU 1280.

IPv6: Fragmentace IP není povolena. IP + hlavička datagramu má 48 bajtů. To předpokládá žádné rozšiřující hlavičky IPv6. Maximální velikost zprávy je MTU - 48. Hlavička datové fáze má 16 bajtů a MAC má 16 bajtů, celkem 32 bajtů. Velikost užitečného zatížení je MTU - 80. Maximální užitečné zatížení datové fáze je 1420 pro maximální MTU 1500. Maximální užitečné zatížení datové fáze je 1200 pro minimální MTU 1280.

V SSU 1 byly směrnice striktním maximem přibližně 32 KB pro I2NP zprávu založenou na 64 maximálních fragmentech a 620 minimálním MTU. Kvůli režii pro sdružené LeaseSet a klíče relací byl praktický limit na aplikační úrovni přibližně o 6KB nižší, tedy kolem 26KB. Protokol SSU 1 umožňuje 128 fragmentů, ale současné implementace to omezují na 64 fragmentů.

### Maximální velikost I2NP zprávy

Zvýšením minimální MTU na 1280, s datovou fází o velikosti přibližně 1200, je možná SSU 2 zpráva o velikosti asi 76 KB v 64 fragmentech a 152 KB ve 128 fragmentech. To snadno umožňuje maximum 64 KB.

Kvůli fragmentaci v tunelech a fragmentaci v SSU 2 se pravděpodobnost ztráty zpráv exponenciálně zvyšuje s velikostí zprávy. Nadále doporučujeme praktický limit přibližně 10 KB na aplikační vrstvě pro I2NP datagramy.

### Verze

Viz Bezpečnost Peer Test výše pro analýzu SSU1 Peer Test a cíle pro SSU2 Peer Test.

Když je odmítnut Bobem:

Když je odmítnut Charliem:

POZNÁMKA: RI mohou být odeslány buď jako I2NP Database Store zprávy v I2NP blocích, nebo jako RI bloky (pokud jsou dostatečně malé). Ty mohou být obsaženy ve stejných paketech jako peer test bloky, pokud jsou dostatečně malé.

Zprávy 1-4 jsou v rámci relace pomocí Peer Test bloků ve zprávě Data. Zprávy 5-7 jsou mimo relaci pomocí Peer Test bloků ve zprávě Peer Test.

## Proces testování peerů

POZNÁMKA: Stejně jako v SSU 1 mohou zprávy 4 a 5 dorazit v libovolném pořadí. Zprávy 5 a/nebo 7 nemusí být vůbec přijaty, pokud je Alice za firewallem. Když zpráva 5 dorazí před zprávou 4, Alice nemůže okamžitě odeslat zprávu 6, protože ještě nemá Charlie's intro key pro zašifrování hlavičky. Když zpráva 4 dorazí před zprávou 5, Alice by neměla okamžitě poslat zprávu 6, protože by měla počkat, zda zpráva 5 dorazí, aniž by otevřela firewall zprávou 6.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest
        <---------------- Charlie RI
4.      <------------------ PeerTest

5.      <----------------------------------------- PeerTest
6. PeerTest ----------------------------------------->
7.      <----------------------------------------- PeerTest
```
Testování mezi různými verzemi není podporováno. Jediná povolená kombinace verzí je, kdy všichni peerové používají verzi 2.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
4.      <------------------ PeerTest (reject)
```
Zprávy 1-4 jsou v rámci relace a jsou pokryty procesy ACK a opakovaného přenosu datové fáze. Bloky Peer Test vyžadují potvrzení.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest (reject)
                      (optional: Bob could try another Charlie here)
4.      <------------------ PeerTest (reject)
```
Zprávy 5-7 mohou být znovu odeslány, beze změny.

Stejně jako v SSU 1 je podporováno testování IPv6 adres a komunikace Alice-Bob a Alice-Charlie může probíhat přes IPv6, pokud Bob a Charlie označí podporu pomocí capability 'B' ve své publikované IPv6 adrese. Podrobnosti viz Proposal 126.

Stejně jako v SSU 1 před verzí 0.9.50, Alice pošle požadavek Bobovi pomocí existující relace přes transport (IPv4 nebo IPv6), který chce testovat. Když Bob obdrží požadavek od Alice přes IPv4, Bob musí vybrat Charlieho, který inzeruje IPv4 adresu. Když Bob obdrží požadavek od Alice přes IPv6, Bob musí vybrat Charlieho, který inzeruje IPv6 adresu. Skutečná komunikace Bob-Charlie může probíhat přes IPv4 nebo IPv6 (tj. nezávisle na typu adresy Alice). Toto NENÍ chování SSU 1 od verze 0.9.50, kde jsou povoleny smíšené IPv4/v6 požadavky.

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
### Opakované přenosy

Na rozdíl od SSU 1 Alice specifikuje požadovanou testovací IP adresu a port ve zprávě 1. Bob by měl ověřit tuto IP adresu a port a odmítnout s kódem 5, pokud jsou neplatné. Doporučené ověření IP adresy je, že pro IPv4 se shoduje s Alice IP adresou a pro IPv6 se shoduje alespoň prvních 8 bajtů IP adresy. Ověření portu by mělo odmítnout privilegované porty a porty pro známé protokoly.

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
### Poznámky k IPv6

Zde dokumentujeme, jak může Alice určit výsledky peer testu na základě toho, které zprávy jsou přijaty. Vylepšení SSU2 nám poskytují příležitost opravit, zlepšit a lépe zdokumentovat stavový automat výsledků peer testu ve srovnání s tím v [SSU](/docs/transport/ssu).

Pro každý testovaný typ adresy (IPv4 nebo IPv6) může být výsledek jeden z UNKNOWN, OK, FIREWALLED nebo SYMNAT. Navíc může být provedeno další zpracování pro detekci změny IP nebo portu, nebo externí port odlišný od interního portu.

### Zpracování Bobem

Problémy s dokumentovaným stavovým automatem SSU:

Takže na rozdíl od SSU doporučujeme počkat několik sekund po obdržení zprávy 4, poté odeslat zprávu 6, i když zpráva 5 nebyla přijata.

### Stavový automat výsledků

Shrnutí stavového automatu, založené na tom, zda jsou zprávy 4, 5 a 7 přijaty (ano nebo ne), je následující:

### Opětovné přenosy

Podrobnější stavový automat s kontrolami IP/portu přijatého v adresním bloku zprávy 7 je níže. Jednou výzvou je určit, zda jste to vy (Alice), kdo má symetrický NAT, nebo Charlie.

Doporučuje se následné zpracování nebo dodatečná logika pro potvrzení přechodů stavu vyžadováním stejných výsledků na dvou nebo více testech peer uzlů.

Doporučuje se také ověření a potvrzení IP/portu dvěma nebo více testy, nebo s blokem adres ve zprávách Session Created, ale to je mimo rozsah této specifikace.

- Nikdy neposíláme zprávu 6, pokud jsme nedostali zprávu 5, takže nikdy nevíme, jestli jsme SYMNAT
- Pokud jsme dostali zprávy 4 a 7, jak bychom mohli být SYMNAT
- Pokud se IP neshodovala, ale port ano, nejsme SYMNAT, pouze jsme si změnili IP

Viz Relay Security výše pro analýzu SSU1 Relay a cíle pro SSU2 Relay.

Když je odmítnut Bobem:

```
4 5 7  Result             Notes
-----  ------             -----
n n n  UNKNOWN
y n n  FIREWALLED           (unless currently SYMNAT)
n y n  OK                   (unless currently SYMNAT, which is unlikely)
y y n  OK                   (unless currently SYMNAT, which is unlikely)
n n y  n/a                  (can't send msg 6)
y n y  FIREWALLED or SYMNAT (requires sending msg 6 w/o rcv msg 5)
n y y  n/a                  (can't send msg 6)
y y y  OK
```
Když je odmítnut Charlie:

POZNÁMKA: RI může být zasláno buď jako I2NP Database Store zprávy v I2NP blocích, nebo jako RI bloky (pokud jsou dostatečně malé). Tyto mohou být obsaženy ve stejných paketech jako relay bloky, pokud jsou dostatečně malé.

V SSU 1 obsahují informace o Charlieho routeru IP, port, intro klíč, relay tag a expiraci každého introducera.

```
If Alice does not get msg 5:
   If Alice does not get msg 4: -> UNKNOWN
   If Alice does not get msg 7: -> UNKNOWN
   If Alice gets msgs 4/7 and IP/port match: -> FIREWALLED
   If Alice gets msgs 4/7 and IP matches, port does not match:
      -> SYMNAT, but needs confirmation with 2nd test
   If Alice gets msgs 4/7 and IP does not match, port matches:
      -> FIREWALLED, address change?
   If Alice gets msgs 4/7 and both IP and port do not match:
      -> SYMNAT, address change?

If Alice gets msg 5:
   If Alice does not get msg 4: -> OK unless currently SYMNAT, else UNKNOWN
                                   (in SSU2 have to stop here)
   If Alice does not get msg 7: -> OK unless currently SYMNAT, else UNKNOWN
   If Alice gets msgs 4/5/7 and IP/port match: -> OK
   If Alice gets msgs 4/5/7 and IP matches, port does not match:
      -> OK, charlie is probably sym. natted
   If Alice gets msgs 4/5/7 and IP does not match, port matches:
      -> OK, address change?
   If Alice gets msgs 4/5/7 and both IP and port do not match:
      -> OK, address change?
```
## Proces předávání

V SSU 2 obsahují informace o Charlieho routeru hash routeru, relay tag a expiraci každého introducera.

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse

5.      <-------------------------------------------- HolePunch
6. SessionRequest -------------------------------------------->
7.      <-------------------------------------------- SessionCreated
8. SessionConfirmed ------------------------------------------>
```
Alice by měla snížit počet potřebných round tripů tak, že nejprve vybere introducer (Boba), ke kterému už má připojení. Za druhé, pokud žádný takový není, vybere introducer, pro kterého už má router info.

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
4.      <-------------- RelayResponse
```
Přenos mezi verzemi by měl být také podporován, pokud je to možné. To usnadní postupný přechod ze SSU 1 na SSU 2. Povolené kombinace verzí jsou (TODO):

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse
```
Relay Request, Relay Intro a Relay Response jsou všechny v rámci relace a jsou pokryty procesy potvrzování a opětovného odesílání datové fáze. Bloky Relay Request, Relay Intro a Relay Response vyžadují potvrzení.

Všimněte si, že obvykle Charlie okamžitě odpoví na Relay Intro pomocí Relay Response, která by měla obsahovat ACK blok. V takovém případě není potřeba samostatná zpráva s ACK blokem.

Hole punch může být znovu odeslán, jako v SSU 1.

Na rozdíl od I2NP zpráv nemají Relay zprávy jedinečné identifikátory, takže duplikáty musí být detekovány pomocí relay stavového automatu s použitím nonce. Implementace mohou také potřebovat udržovat cache nedávno použitých nonce, aby mohly být duplikáty detekovány i poté, co stavový automat pro daný nonce dokončil svou činnost.

Všechny funkce SSU 1 relay jsou podporovány, včetně těch zdokumentovaných v [Prop158](/proposals/158-ipv6-transport-enhancements) a podporovaných od verze 0.9.50. IPv4 a IPv6 úvody jsou podporovány. Relay Request může být odeslán přes IPv4 relaci pro IPv6 úvod a Relay Request může být odeslán přes IPv6 relaci pro IPv4 úvod.

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
### IPv4/v6

Následují rozdíly oproti SSU 1 a doporučení pro implementaci SSU 2.

V SSU 1 je představení relativně levné a Alice obecně posílá Relay Requests všem introducer. V SSU 2 je představení nákladnější, protože nejprve musí být navázáno spojení s introducer. Pro minimalizaci latence a režie při představení se doporučuje následující postup zpracování:

V obou SSU 1 i SSU 2 mohou být Relay Response a Hole Punch přijaty v libovolném pořadí, nebo nemusí být přijaty vůbec.

V SSU 1 Alice obvykle obdrží Relay Response (1 RTT) před Hole Punch (1 1/2 RTT). I když to nemusí být v těchto specifikacích dobře zdokumentováno, Alice musí obdržet Relay Response od Boba před pokračováním, aby obdržela IP adresu Charlieho. Pokud je Hole Punch obdržen jako první, Alice ho nerozpozná, protože neobsahuje žádná data a zdrojová IP adresa není rozpoznána. Po obdržení Relay Response by Alice měla čekat BUĎTO na obdržení Hole Punch od Charlieho, NEBO krátké zpoždění (doporučeno 500 ms) před zahájením handshake s Charliem.

### Zpracováno Alicí

V SSU 2 Alice obvykle obdrží Hole Punch (1 1/2 RTT) před Relay Response (2 RTT). SSU 2 Hole Punch je snazší zpracovat než v SSU 1, protože se jedná o úplnou zprávu s definovanými ID připojení (odvozené z relay nonce) a obsahem včetně Charlie's IP. Relay Response (Data zpráva) a Hole Punch zpráva obsahují identický podepsaný Relay Response blok. Alice proto může zahájit handshake s Charliem poté, co BUĎTO obdrží Hole Punch od Charlieho, NEBO obdrží Relay Response od Boba.

### Požadavky na tagy od Boba

Ověření podpisu Hole Punch zahrnuje hash routeru představitele (Boba). Pokud byly Relay Requests odeslány více než jednomu představiteli, existuje několik možností, jak ověřit podpis:

#### Shrnutí

Pokud je Charlie za symetrickým NAT, jeho hlášený port v Relay Response a Hole Punch nemusí být přesný. Proto by Alice měla zkontrolovat zdrojový UDP port zprávy Hole Punch a použít ten, pokud se liší od hlášeného portu.

- Ignorovat všechny introducery, které jsou prošlé na základě hodnoty iexp v adrese
- Pokud je již navázáno SSU2 spojení k jednomu nebo více introducerům, vybrat jeden a poslat Relay Request pouze tomuto introduceru.
- Jinak, pokud je Router Info lokálně známo pro jeden nebo více introducerů, vybrat jeden a připojit se pouze k tomuto introduceru.
- Jinak vyhledat Router Info pro všechny introducery, připojit se k introduceru, jehož Router Info je přijato jako první.

#### Podrobnosti

V SSU 1 mohla pouze Alice požádat o tag v Session Request. Bob nemohl nikdy požádat o tag a Alice nemohla přenášet pro Boba.

V SSU2 Alice obecně požaduje tag v Session Request, ale buď Alice nebo Bob mohou také požádat o tag ve fázi dat. Bob obecně není za firewallem po obdržení příchozího požadavku, ale mohl by být po relay, nebo se Bobův stav může změnit, nebo může požádat o introducer pro jiný typ adresy (IPv4/v6). Takže v SSU2 je možné, aby Alice i Bob současně sloužili jako relay pro druhou stranu.

Následující vlastnosti adres mohou být publikovány, nezměněné z SSU 1, včetně změn v [Prop158](/proposals/158-ipv6-transport-enhancements) podporovaných od API 0.9.50:

Publikovaná RouterAddress (část RouterInfo) bude mít identifikátor protokolu buď "SSU" nebo "SSU2".

- Vyzkoušet každý hash, na který byl odeslán požadavek
- Použít různé nonces pro každý introducer a použít to k určení, kterému introducer tento Hole Punch odpovídal
- Znovu nevalidovat podpis, pokud je obsah identický s tím v Relay Response, pokud již byl přijat
- Nevalidovat podpis vůbec

RouterAddress musí obsahovat tři možnosti pro indikaci podpory SSU2:

### Vlastnosti adresy

Alice musí ověřit, že všechny tři možnosti jsou přítomny a platné před připojením pomocí SSU2 protokolu.

Když je publikován jako "SSU" s možnostmi "s", "i" a "v" a s možnostmi "host" a "port", router musí přijímat příchozí připojení na daném hostiteli a portu pro oba protokoly SSU a SSU2 a automaticky detekovat verzi protokolu.

## Publikované informace o router

### Publikované adresy

Když je publikován jako "SSU2" s možnostmi "s", "i" a "v" a s možnostmi "host" a "port", router přijímá příchozí spojení na daném hostiteli a portu pouze pro protokol SSU2.

- caps: schopnosti [B,C,4,6]
- host: IP (IPv4 nebo IPv6). Zkrácená IPv6 adresa (s "::") je povolena. Může nebo nemusí být přítomna, pokud je za firewallem. Názvy hostů nejsou povoleny.
- iexp[0-2]: Vypršení tohoto introduceru. ASCII číslice, v sekundách od epochy. Přítomno pouze pokud je za firewallem a introducery jsou vyžadovány. Volitelné (i když jsou přítomny další vlastnosti pro tento introducer).
- ihost[0-2]: IP introduceru (IPv4 nebo IPv6). Zkrácená IPv6 adresa (s "::") je povolena. Přítomno pouze pokud je za firewallem a introducery jsou vyžadovány. Názvy hostů nejsou povoleny. Pouze SSU adresa.
- ikey[0-2]: Base 64 introdukční klíč introduceru. Přítomno pouze pokud je za firewallem a introducery jsou vyžadovány. Pouze SSU adresa.
- iport[0-2]: Port introduceru 1024 - 65535. Přítomno pouze pokud je za firewallem a introducery jsou vyžadovány. Pouze SSU adresa.
- itag[0-2]: Tag introduceru 1 - (2**32 - 1) ASCII číslice. Přítomno pouze pokud je za firewallem a introducery jsou vyžadovány.
- key: Base 64 introdukční klíč.
- mtu: Volitelné. Viz sekce MTU výše.
- port: 1024 - 65535 Může nebo nemusí být přítomen, pokud je za firewallem.

### Nepublikovaná SSU2 adresa

Pokud router podporuje jak SSU1, tak SSU2 připojení, ale neimplementuje automatickou detekci verze pro příchozí připojení, musí inzerovat jak "SSU", tak "SSU2" adresy a zahrnout SSU2 možnosti pouze v "SSU2" adrese. Router by měl nastavit nižší hodnotu nákladů (vyšší prioritu) v "SSU2" adrese než v "SSU" adrese, takže SSU2 je preferováno.

Pokud je v jednom RouterInfo publikováno více SSU2 RouterAddresses (buď jako "SSU" nebo "SSU2") pro dodatečné IP adresy nebo porty, všechny adresy specifikující stejný port musí obsahovat identické SSU2 možnosti a hodnoty. Zejména všechny musí obsahovat stejný statický klíč "s" a introduction klíč "i".

- s=(Base64 klíč) Aktuální Noise statický veřejný klíč (s) pro tuto RouterAddress. Kódováno v Base 64 pomocí standardní I2P Base 64 abecedy. 32 bytů v binárním formátu, 44 bytů jako Base 64 kódováno, little-endian X25519 veřejný klíč.
- i=(Base64 klíč) Aktuální klíč pro představení pro šifrování hlaviček této RouterAddress. Kódováno v Base 64 pomocí standardní I2P Base 64 abecedy. 32 bytů v binárním formátu, 44 bytů jako Base 64 kódováno, big-endian ChaCha20 klíč.
- v=2 Aktuální verze (2). Když je publikováno jako "SSU", je implicitně zahrnuta dodatečná podpora pro verzi 1. Podpora pro budoucí verze bude s hodnotami oddělenými čárkami, např. v=2,3 Implementace by měla ověřit kompatibilitu, včetně více verzí pokud je přítomna čárka. Verze oddělené čárkami musí být v číselném pořadí.

Když je publikováno jako SSU nebo SSU2 s introducery, jsou přítomny následující možnosti:

Následující možnosti jsou pouze pro SSU a nepoužívají se pro SSU2. V SSU2 Alice získává tyto informace z Charlie's RI místo toho.

Router nesmí publikovat host nebo port v adrese při publikování introducers. Router musí publikovat 4 a/nebo 6 caps v adrese při publikování introducers pro indikaci podpory IPv4 a/nebo IPv6. To je stejné jako současná praxe pro nejnovější SSU 1 adresy.

Poznámka: Pokud je publikováno jako SSU a je zde kombinace SSU 1 a SSU2 introducers, SSU 1 introducers by měli být na nižších indexech a SSU2 introducers by měli být na vyšších indexech, kvůli kompatibilitě se staršími routery.

Pokud Alice nezveřejní svou SSU2 adresu (jako "SSU" nebo "SSU2") pro příchozí připojení, musí zveřejnit router adresu "SSU2" obsahující pouze svůj statický klíč a SSU2 verzi, aby Bob mohl ověřit klíč po obdržení Alice RouterInfo v Session Confirmed části 2.

#### Zpracování chyb

Tato adresa routeru nebude obsahovat možnosti "host" nebo "port", protože tyto nejsou vyžadovány pro odchozí SSU2 spojení. Publikovaná cena pro tuto adresu přísně nevzato nezáleží, protože je pouze příchozí; nicméně může to být užitečné pro ostatní routery, pokud je cena nastavena vyšší (nižší priorita) než u jiných adres. Navrhovaná hodnota je 14.

- ih[0-2]=(Base64 hash) Hash routeru pro introducer. Base 64 kódovaný pomocí standardní I2P Base 64 abecedy. 32 bajtů v binárním formátu, 44 bajtů jako Base 64 kódovaný
- iexp[0-2]: Vypršení platnosti tohoto introducera. Nezměněno z SSU 1.
- itag[0-2]: Tag introducera 1 - (2**32 - 1) Nezměněno z SSU 1.

Alice může také jednoduše přidat možnosti "i", "s" a "v" k existující publikované "SSU" adrese.

- ihost[0-2]
- ikey[0-2]
- itag[0-2]

Používání stejných statických klíčů pro NTCP2 a SSU2 je povoleno, ale nedoporučuje se.

Kvůli ukládání RouterInfo do cache nesmí routery rotovat statický veřejný klíč nebo IV, dokud je router spuštěný, ať už je v publikované adrese nebo ne. Routery musí tento klíč a IV perzistentně ukládat pro opětovné použití po okamžitém restartu, aby příchozí připojení nadále fungovala a časy restartů nebyly odhaleny. Routery musí perzistentně ukládat nebo jinak určit čas posledního vypnutí, aby mohl být při spuštění vypočítán předchozí čas nefunkčnosti.

### Rotace veřejného klíče a IV

Kvůli obavám ohledně odhalení časů restartů mohou routery rotovat tento klíč nebo IV při spuštění, pokud byl router předtím nějakou dobu vypnutý (alespoň několik dní).

- s=(Base64 klíč) Jak definováno výše pro publikované adresy.
- i=(Base64 klíč) Jak definováno výše pro publikované adresy.
- v=2 Jak definováno výše pro publikované adresy.

Pokud má router jakékoli publikované SSU2 RouterAddresses (jako SSU nebo SSU2), minimální doba nečinnosti před rotací by měla být mnohem delší, například jeden měsíc, pokud se nezměnila místní IP adresa nebo router neprovede "rekeys".

Pokud má router nějaké publikované SSU RouterAddresses, ale ne SSU2 (jako SSU nebo SSU2), minimální doba výpadku před rotací by měla být delší, například jeden den, pokud se nezměnila místní IP adresa nebo router neprovede "rekeys". To platí i v případě, že publikovaná SSU adresa má introducers.

### Vytváření odchozích paketů

Pokud router nemá žádné publikované RouterAddresses (SSU, SSU2, nebo SSU), může být minimální výpadek před rotací tak krátký jako dvě hodiny, i když se IP adresa změní, pokud router neprovede "rekeys".

Pokud router "rekeys" na jiný Router Hash, měl by také vygenerovat nový noise key a intro key.

Implementace si musí být vědomy toho, že změna statického veřejného klíče nebo IV znemožní příchozí SSU2 spojení od routerů, které mají v cache starší RouterInfo. Publikování RouterInfo, výběr tunnel peerů (včetně jak OBGW, tak IB nejbližšího hopu), výběr zero-hop tunnelů, výběr transportu a další implementační strategie musí toto brát v úvahu.

Rotace intro klíčů podléhá stejným pravidlům jako rotace klíčů.

Poznámka: Minimální doba výpadku před rekeying může být upravena pro zajištění zdraví sítě a pro zabránění reseeding router, který je vypnutý po střední dobu.

Popiratelnost není cílem. Viz přehled výše.

Každému vzoru jsou přiřazeny vlastnosti popisující důvernost poskytovanou statickému veřejnému klíči iniciátora a statickému veřejnému klíči odpovídajícího. Základní předpoklady jsou, že dočasné privátní klíče jsou bezpečné a že strany přeruší handshake, pokud obdrží statický veřejný klíč od druhé strany, které nevěří.

Tato sekce se zabývá pouze únikem identity prostřednictvím statických polí veřejných klíčů v handshakes. Identity účastníků Noise protokolu mohou být samozřejmě odhaleny i jinými způsoby, včetně polí v datech, analýzy provozu nebo metadat, jako jsou IP adresy.

Alice: (8) Šifrováno s forward secrecy pro autentifikovanou stranu.

Bob: (3) Nepřenášeno, ale pasivní útočník může kontrolovat kandidáty pro soukromý klíč respondenta a určit, zda je kandidát správný.

#### Skrytí identity

Bob publikuje svůj statický veřejný klíč v netDb. Alice nemusí, ale musí ho zahrnout do RI odeslaného Bobovi.

Zprávy handshake (Session Request/Created/Confirmed, Retry) základní kroky, v pořadí:

Základní kroky zpráv fáze dat, v pořadí:

Počáteční zpracování všech příchozích zpráv:

Zpracování handshake zpráv (Session Request/Created/Confirmed, Retry, Token Request) a dalších mimosezónních zpráv (Peer Test, Hole Punch):

Zpracování zpráv datové fáze:

## Pravidla pro pakety

### Zpracování příchozích paketů

V SSU 1 je klasifikace příchozích paketů obtížná, protože neexistuje hlavička indikující číslo relace. Routery musí nejprve porovnat zdrojovou IP adresu a port s existujícím stavem partnera, a pokud není nalezen, pokusit se o několik dešifrování s různými klíči, aby našly příslušný stav partnera nebo založily nový. V případě, že se zdrojová IP adresa nebo port pro existující relaci změní, možná kvůli chování NAT, může router použít nákladnou heuristiku, aby se pokusil přiřadit paket k existující relaci a obnovit obsah.

- Vytvořit 16 nebo 32 bajtovou hlavičku
- Vytvořit payload
- mixHash() hlavičku (kromě Retry)
- Zašifrovat payload pomocí Noise (kromě Retry, použít ChaChaPoly s hlavičkou jako AD)
- Zašifrovat hlavičku a pro Session Request/Created ephemeral klíč

SSU 2 je navrženo tak, aby minimalizovalo úsilí při klasifikaci příchozích paketů při zachování odolnosti proti DPI a dalším hrozbám na cestě. Číslo Connection ID je zahrnuto v hlavičce pro všechny typy zpráv a šifrováno (obfuskováno) pomocí ChaCha20 se známým klíčem a nonce. Navíc je typ zprávy také zahrnut v hlavičce (šifrován s ochranou hlavičky známým klíčem a poté obfuskován pomocí ChaCha20) a může být použit pro dodatečnou klasifikaci. V žádném případě není nutná zkušební DH nebo jiná asymetrická kryptografická operace pro klasifikaci paketu.

- Vytvořit 16-bajtové záhlaví
- Vytvořit datovou část
- Zašifrovat datovou část pomocí ChaChaPoly s použitím záhlaví jako AD
- Zašifrovat záhlaví

### Poznámky

#### Shrnutí

Pro téměř všechny zprávy od všech uzlů je ChaCha20 klíč pro šifrování Connection ID úvodní klíč cílového routeru tak, jak je publikován v netDb.

- Dešifrovat prvních 8 bajtů hlavičky (Destination Connection ID) s intro klíčem
- Vyhledat spojení podle Destination Connection ID
- Pokud je spojení nalezeno a je ve fázi dat, přejít na sekci fáze dat
- Pokud spojení není nalezeno, přejít na sekci handshake
- Poznámka: Zprávy Peer Test a Hole Punch mohou být také vyhledány podle Destination Connection ID vytvořeného z test nebo relay nonce.

Jedinými výjimkami jsou první zprávy odeslané od Boba k Alici (Session Created nebo Retry), kde Bobovi ještě není znám Alicin introduction key. V těchto případech se jako klíč používá Bobův introduction key.

- Dešifrovat bajty 8-15 hlavičky (typ paketu, verze a net ID) pomocí intro klíče. Pokud se jedná o platný Session Request, Token Request, Peer Test nebo Hole Punch, pokračovat
- Pokud se nejedná o platnou zprávu, vyhledat čekající odchozí spojení podle zdrojové IP/portu paketu, zacházet s paketem jako se Session Created nebo Retry. Znovu dešifrovat prvních 8 bajtů hlavičky správným klíčem a bajty 8-15 hlavičky (typ paketu, verze a net ID). Pokud se jedná o platný Session Created nebo Retry, pokračovat
- Pokud se nejedná o platnou zprávu, selhat, nebo zařadit do fronty jako možný paket datové fáze mimo pořadí
- Pro Session Request/Created, Retry, Token Request, Peer Test a Hole Punch dešifrovat bajty 16-31 hlavičky
- Pro Session Request/Created dešifrovat dočasný klíč
- Ověřit všechna pole hlavičky, zastavit pokud nejsou platná
- mixHash() hlavičku
- Pro Session Request/Created/Confirmed dešifrovat payload pomocí Noise
- Pro Retry a datovou fázi dešifrovat payload pomocí ChaChaPoly
- Zpracovat hlavičku a payload

Protokol je navržen tak, aby minimalizoval zpracování klasifikace paketů, které by mohlo vyžadovat dodatečné kryptografické operace v několika záložních krocích nebo složité heuristiky. Navíc většina přijatých paketů nebude vyžadovat (případně nákladné) záložní vyhledávání podle zdrojové IP/portu a druhé dešifrování hlavičky. Pouze Session Created a Retry (a případně další TBD) budou vyžadovat záložní zpracování. Pokud se koncový bod po vytvoření relace změní IP nebo port, ID připojení se stále používá k vyhledání relace. Nikdy není nutné používat heuristiky k nalezení relace, například hledáním jiné relace se stejnou IP, ale jiným portem.

- Dešifrovat bajty 8-15 hlavičky (typ paketu, verze a síťové ID) se správným klíčem
- Dešifrovat payload pomocí ChaChaPoly s použitím hlavičky jako AD
- Zpracovat hlavičku a payload

#### Podrobnosti

Proto jsou doporučené kroky zpracování v logice smyčky příjemce:

1) Dešifrujte prvních 8 bajtů pomocí ChaCha20 s použitím lokálního introduction klíče, abyste obnovili Destination Connection ID. Pokud se Connection ID shoduje se současnou nebo čekající příchozí relací:

2) Pokud ID připojení neodpovídá aktuální relaci: Zkontrolujte, že hlavička v plaintextu na bytech 8-15 je platná (bez provádění jakékoli operace ochrany hlavičky). Ověřte, že net ID a verze protokolu jsou platné, a že typ zprávy je Session Request, nebo jiný typ zprávy povolený mimo relaci (TBD).

3) Vyhledat čekající odchozí relaci podle zdrojové IP/portu paketu.

4)  Pokud běží SSU 1 na stejném portu, pokusit se zpracovat zprávu jako SSU 1 paket.

Obecně by relace (ve fázi handshake nebo dat) nikdy neměla být zrušena po přijetí paketu s neočekávaným typem zprávy. Toto zabraňuje útokům injektáže paketů. Tyto pakety budou také běžně přijímány po retransmisi handshake paketu, kdy klíče pro dešifrování hlavičky již nejsou platné.

Ve většině případů jednoduše zahoďte paket. Implementace může, ale není povinna, znovu odeslat dříve odeslaný paket (handshake zprávu nebo ACK 0) jako odpověď.

    a)  Using the appropriate key, decrypt the header bytes 8-15 to recover the version, net ID, and message type.
    b)  If the message type is Session Confirmed, it is a long header. Verify the net ID and protocol version are valid. Decrypt the bytes 15-31 of the header with ChaCha20 using the local intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise.
    c)  If the message type is valid but not Session Confirmed, it is a short header. Verify the net ID and protocol version are valid. decrypt the rest of the message with ChaCha20/Poly1305 using the session key, using the decrypted 16-byte header as the AD.
    d)  (optional) If connection ID is a pending inbound session awaiting a Session Confirmed message, but the net ID, protocol, or message type is not valid, it could be a Data message received out-of-order before the Session Confirmed, so the data phase header protection keys are not yet known, and the header bytes 8-15 were incorrectly decrypted. Queue the message, and attempt to decrypt it once the Session Confirmed message is received.
    e)  If b) or c) fails, drop the message.

Po odeslání Session Created jako Bob jsou neočekávané pakety běžně Data pakety, které nelze dešifrovat, protože Session Confirmed pakety byly ztraceny nebo dorazily mimo pořadí. Zařaďte pakety do fronty a pokuste se je dešifrovat po obdržení Session Confirmed paketů.

    a)  If all is valid and the message type is Session Request, decrypt bytes 16-31 of the header and the 32-byte X value with ChaCha20 using the local intro key.

    - If the token at header bytes 24-31 is accepted, then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Created in response.
    - If the token is not accepted, send a Retry message to the source IP/port with a token. Do not attempt to decrypt the message with Noise to avoid DDoS attacks.

    b)  If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.
    c)  If a) or b) fails, go to step 3)

Po obdržení Session Confirmed jako Bob jsou neočekávané pakety běžně retransmitované Session Confirmed pakety, protože ACK 0 Session Confirmed bylo ztraceno. Neočekávané pakety mohou být zahozeny. Implementace může, ale není povinná, poslat Data paket obsahující ACK blok jako odpověď.

    a)  If found, re-decrypt the first 8 bytes with ChaCha20 using Bob's introduction key to recover the Destination Connection ID.
    b)  If the connection ID matches the pending session: Using the correct key, decrypt bytes 8-15 of the header to recover the version, net ID, and message type. Verify the net ID and protocol version are valid, and the message type is Session Created or Retry, or other message type allowed out-of-session (TBD).

    - If all is valid and the message type is Session Created, decrypt the next 16 bytes of the header and the 32-byte Y value with ChaCha20 using Bob's intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Confirmed in response.
    - If all is valid and the message type is Retry, decrypt bytes 16-31 of the header with ChaCha20 using Bob's intro key. Decrypt and validate the message using ChaCha20/Poly1305 using TBD as the key and TBD as the nonce and the decrypted 32-byte header as the AD. Resend a Session Request with the received token in response.
    - If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.

    > c)  If a pending outbound session is not found, or the connection ID does not match the pending session, drop the message, unless the port is shared with SSU 1.

Pro Session Created a Session Confirmed musí implementace pečlivě validovat všechna dešifrovaná pole hlavičky (Connection IDs, číslo paketu, typ paketu, verzi, id, frag a příznaky) PŘED voláním mixHash() na hlavičce a pokusem o dešifrování obsahu pomocí Noise AEAD. Pokud dešifrování Noise AEAD selže, nesmí se provádět žádné další zpracování, protože mixHash() by poškodil stav handshake, pokud implementace neuloží a "nevrátí zpět" stav hashe.

#### Zpracování chyb

Možná nebude možné efektivně detekovat, zda jsou příchozí pakety verze 1 nebo 2 na stejném příchozím portu. Výše uvedené kroky může mít smysl provést před zpracováním SSU 1, aby se zabránilo pokusům o zkušební DH operace pomocí obou verzí protokolu.

Bude určeno v případě potřeby.

Předpokládá IPv4, nezahrnuje dodatečné vyplnění, nezahrnuje velikosti IP a UDP hlaviček. Vyplnění je mod-16 vyplnění pouze pro SSU 1.

**SSU 1**

### Detekce verze

**SSU 2**

### Tokeny

Výše specifikujeme, že token musí být náhodně generovaná 8bajtová hodnota, nikoli generovat neprůhlednou hodnotu jako je hash nebo HMAC serverového tajemství a IP, portu, kvůli útokům znovupoužití. To však vyžaduje dočasné a (volitelně) trvalé uložení doručených tokenů. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) používá 16bajtový HMAC serverového tajemství a IP adresy, přičemž serverové tajemství se obnovuje každé dvě minuty. Měli bychom prozkoumat něco podobného s delší životností serverového tajemství. Pokud do tokenu vložíme časové razítko, může to být řešením, ale 8bajtový token nemusí být dostatečně velký pro takový účel.

Doplní se podle potřeby.

## Doporučené konstanty

- Timeout pro opětovné odeslání odchozího handshaku: 1,25 sekundy, s exponenciálním zpožděním (opětovná odeslání po 1,25, 3,75 a 8,75 sekundách)
- Celkový timeout odchozího handshaku: 15 sekund
- Timeout pro opětovné odeslání příchozího handshaku: 1 sekunda, s exponenciálním zpožděním (opětovná odeslání po 1, 3 a 7 sekundách)
- Celkový timeout příchozího handshaku: 12 sekund
- Timeout po odeslání opakování: 9 sekund
- Zpoždění ACK: max(10, min(rtt/6, 150)) ms
- Okamžité zpoždění ACK: min(rtt/16, 5) ms
- Max rozsahů ACK: 256?
- Max hloubka ACK: 512?
- Distribuce paddingu: 0-15 bajtů, nebo více
- Minimální timeout pro opětovné odeslání v datové fázi: 1 sekunda, podle [RFC-6298](https://tools.ietf.org/html/rfc6298)
- Viz také [RFC-6298](https://tools.ietf.org/html/rfc6298) pro další pokyny k časovačům opětovného odeslání pro datovou fázi.

## Analýza režie paketů

Předpokládá IPv4, bez dodatečného doplňování, bez velikostí hlaviček IP a UDP. Doplňování je mod-16 pouze pro SSU 1.

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
## Problémy a budoucí práce

### Tokeny

Výše jsme uvedli, že token musí být náhodně generovaná hodnota o délce 8 bajtů, nikoli neprůhledná hodnota jako hash nebo HMAC tajného klíče serveru a IP adresy či portu, kvůli útokům spojeným s opakovaným použitím. To však vyžaduje dočasné a (volitelně) trvalé ukládání doručených tokenů. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) používá 16bajtový HMAC tajného klíče serveru a IP adresy, přičemž tajný klíč serveru se mění každé dva minuty. Měli bychom prozkoumat něco podobného s delší dobou platnosti tajného klíče serveru. Pokud bychom do tokenu vložili časovou značku, mohlo by to být řešením, ale 8bajtový token nemusí být pro tento účel dostatečně velký.

## Reference

- **[Common]** [Specifikace běžných struktur](/docs/specs/common-structures)
- **[ECIES]** [Specifikace ECIES-X25519-AEAD-Ratchet](/docs/specs/ecies)
- **[NetDB]** [Síťová databáze](/docs/overview/network-database)
- **[NOISE]** [Noise Protocol Framework](https://noiseprotocol.org/noise.html)
- **[Nonces]** [Nonce-Disrespecting Adversaries](https://eprint.iacr.org/2019/624.pdf)
- **[NTCP]** [NTCP Transport](/docs/transport/ntcp)
- **[NTCP2]** [Specifikace NTCP2](/docs/specs/ntcp2)
- **[PMTU]** [Path MTU Discovery](https://en.wikipedia.org/wiki/Path_MTU_Discovery)
- **[Prop104]** [Návrh 104: TLS Transport](/proposals/104-tls-transport)
- **[Prop109]** [Návrh 109: Pluggable Transport](/proposals/109-pt-transport)
- **[Prop158]** [Návrh 158: Vylepšení IPv6 transportu](/proposals/158-ipv6-transport-enhancements)
- **[Prop159]** [Návrh 159: SSU2](/proposals/159-ssu2)
- **[RFC-2104]** [RFC 2104: HMAC](https://tools.ietf.org/html/rfc2104)
- **[RFC-3449]** [RFC 3449: TCP Performance Implications](https://tools.ietf.org/html/rfc3449)
- **[RFC-3526]** [RFC 3526: MODP Groups](https://tools.ietf.org/html/rfc3526)
- **[RFC-5681]** [RFC 5681: TCP Congestion Control](https://tools.ietf.org/html/rfc5681)
- **[RFC-5869]** [RFC 5869: HKDF](https://tools.ietf.org/html/rfc5869)
- **[RFC-6151]** [RFC 6151: MD5 Security Considerations](https://tools.ietf.org/html/rfc6151)
- **[RFC-6298]** [RFC 6298: TCP Retransmission Timer](https://tools.ietf.org/html/rfc6298)
- **[RFC-6437]** [RFC 6437: IPv6 Flow Label](https://tools.ietf.org/html/rfc6437)
- **[RFC-7539]** [RFC 7539: ChaCha20/Poly1305](https://tools.ietf.org/html/rfc7539)
- **[RFC-7748]** [RFC 7748: Elliptic Curves for Security](https://tools.ietf.org/html/rfc7748)
- **[RFC-7905]** [RFC 7905: ChaCha20-Poly1305 Cipher Suites for TLS](https://tools.ietf.org/html/rfc7905)
- **[RFC-9000]** [RFC 9000: QUIC Transport Protocol](https://datatracker.ietf.org/doc/html/rfc9000)
- **[RFC-9001]** [RFC 9001: Using TLS to Secure QUIC](https://datatracker.ietf.org/doc/html/rfc9001)
- **[RFC-9002]** [RFC 9002: QUIC Loss Detection and Congestion Control](https://datatracker.ietf.org/doc/html/rfc9002)
- **[RouterAddress]** [Struktura RouterAddress](/docs/specs/common-structures#struct-routeraddress)
- **[RouterIdentity]** [Struktura RouterIdentity](/docs/specs/common-structures#struct-routeridentity)
- **[SigningPublicKey]** [Typ SigningPublicKey](/docs/specs/common-structures#type-signingpublickey)
- **[SSU]** [SSU Transport](/docs/transport/ssu)
- **[STS]** [Station-to-Station Protocol](https://en.wikipedia.org/wiki/Station-to-Station_protocol)
- **[Ticket1112]** [I2P Ticket 1112](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1112)
- **[Ticket1849]** [I2P Ticket 1849](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1849)
- **[WireGuard]** [WireGuard Protocol](https://www.wireguard.com/papers/wireguard.pdf)
