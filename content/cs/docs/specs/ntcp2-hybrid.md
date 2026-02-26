---
title: "PQ Hybrid NTCP2"
description: "Post-kvantová hybridní varianta transportního protokolu NTCP2 používající ML-KEM"
slug: "ntcp2-hybrid"
lastupdated: "2026-02"
category: "Transporty"
accurateFor: "0.9.69"
---

### Stav

Beta Q1 2026, vydání Q2 2026

## Přehled

Toto je hybridní post-kvantová varianta transportního protokolu NTCP2, jak je navržena v Návrhu 169. Pro další informace viz tento návrh.

PQ Hybrid NTCP2 je definováno pouze na stejné adrese a portu jako standardní NTCP2. Provoz na jiném portu nebo bez podpory standardního NTCP2 není povolen a nebude několik let, dokud nebude standardní NTCP2 zastaralé.

Tato specifikace dokumentuje pouze změny potřebné pro standardní NTCP2 pro podporu PQ Hybrid. Pro podrobnosti základní implementace viz specifikaci NTCP2.

## Design

Podporujeme standardy NIST FIPS 203 a 204 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf), které jsou založeny na CRYSTALS-Kyber a CRYSTALS-Dilithium (verze 3.1, 3 a starší), ale NEJSOU s nimi kompatibilní.

### Výměna klíčů

PQ KEM poskytuje pouze dočasné klíče a nepodporuje přímo handshaky se statickými klíči jako jsou Noise XK a IK. Typy šifrování jsou stejné jako ty používané v PQ Hybrid Ratchet a jsou definovány v dokumentu společných struktur [/docs/specs/common-structures/](/docs/specs/common-structures/), stejně jako v [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf). Hybridní typy jsou definovány pouze v kombinaci s X25519.

Typy šifrování jsou:

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Type</th>
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

### Právní kombinace

Nové typy šifrování jsou uvedeny v RouterAddresses. Typ šifrování v certifikátu klíče bude nadále typu 4.

## Specifikace

### Vzory handshake

Handshaky používají vzory handshaku z [Noise Protocol](https://noiseprotocol.org/noise.html).

Používá se následující mapování písmen:

- e = jednorázový dočasný klíč
- s = statický klíč
- p = užitečné zatížení zprávy
- e1 = jednorázový dočasný PQ klíč, odeslaný od Alice k Bobovi
- ekem1 = šifrový text KEM, odeslaný od Boba k Alici

Následující úpravy XK a IK pro hybridní dopřednou bezpečnost (hfs) jsou specifikovány v [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) sekce 5:

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
Vzor e1 je definován následovně, jak je specifikováno v [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) sekci 4:

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
Vzor ekem1 je definován následovně, jak je specifikováno v [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) sekci 4:

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

#### Přehled

Hybridní handshake je definován v [Noise HFS specifikaci](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf). První zpráva, od Alice k Bobovi, obsahuje e1, enkapsulační klíč, před obsahem zprávy. Tento je považován za dodatečný statický klíč; zavolejte EncryptAndHash() na něj (jako Alice) nebo DecryptAndHash() (jako Bob). Poté zpracujte obsah zprávy obvyklým způsobem.

Druhá zpráva, od Boba k Alice, obsahuje ekem1, šifrovaný text, před samotným obsahem zprávy. S tímto se zachází jako s dalším statickým klíčem; zavolejte na něj EncryptAndHash() (jako Bob) nebo DecryptAndHash() (jako Alice). Poté vypočítejte kem_shared_key a zavolejte MixKey(kem_shared_key). Poté zpracujte obsah zprávy jako obvykle.

#### Definované ML-KEM operace

Definujeme následující funkce odpovídající kryptografickým stavebním blokům používaným podle definice v [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

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

Všimněte si, že jak encap_key, tak ciphertext jsou šifrovány uvnitř ChaCha/Poly bloků ve zprávách 1 a 2 Noise handshake. Budou dešifrovány jako součást procesu handshake.

Parametr kem_shared_key je smíchán do chaining key pomocí MixHash(). Podrobnosti naleznete níže.

#### Alice KDF pro Zprávu 1

Po vzoru zprávy 'es' a před užitečným nákladem přidejte:

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
#### Bob KDF pro zprávu 1

Po vzoru zprávy 'es' a před užitečným nákladem přidejte:

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
#### Bob KDF pro Zprávu 2

Pro XK: Po vzoru zprávy 'ee' a před payload, přidej:

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
#### Alice KDF pro Zprávu 2

Po vzoru zprávy 'ee' přidejte:

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
#### KDF pro Zprávu 3 (pouze XK)

beze změny

#### KDF pro split()

nezměněno

### Podrobnosti handshake

#### Identifikátory Noise

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

Změny: Současný NTCP2 obsahuje pouze možnosti v sekci ChaCha. S ML-KEM bude sekce ChaCha také obsahovat šifrovaný PQ veřejný klíč.

Aby bylo možné podporovat PQ i non-PQ NTCP2 na stejné router adrese a portu, používáme nejvýznamnější bit hodnoty X (X25519 ephemeral public key) k označení, že se jedná o PQ spojení. Tento bit je vždy nevyplněn pro non-PQ spojení.

Pro Alice, poté co je zpráva zašifrována pomocí Noise, ale před AES obfuskací X, nastavte X[31] |= 0x7f.

Pro Boba, po AES de-obfuskaci X, otestovat X[31] & 0x80. Pokud je bit nastaven, vynulovat ho pomocí X[31] &= 0x7f a dešifrovat přes Noise jako PQ připojení. Pokud je bit vynulován, dešifrovat přes Noise jako běžné non-PQ připojení jako obvykle.

Pro PQ NTCP2 inzerovaný na jiné adrese routeru a portu to není vyžadováno.

Další informace naleznete v sekci Publikované adresy níže.

Surový obsah:

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
Nezašifrovaná data (Poly1305 autentifikační tag není zobrazen):

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
Poznámka: pole verze v bloku možností zprávy 1 musí být nastaveno na 2, a to i pro PQ připojení.

Velikosti:

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Typ</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Kód typu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">X délka</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Délka zprávy 1</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Délka šifrované zprávy 1</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Délka dešifrované zprávy 1</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Délka PQ klíče</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">opt délka</th>
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

Poznámka: Kódy typů jsou určeny pouze pro interní použití. Routery zůstanou typu 4 a podpora bude označena v adresách routeru.

#### 2) SessionCreated

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
Nešifrovaná data (Poly1305 auth tag nezobrazena):

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
Velikosti:

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Typ</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Kód typu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Délka Y</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Délka Msg 2</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Délka Msg 2 Enc</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Délka Msg 2 Dec</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Délka PQ CT</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Délka opt</th>
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

Poznámka: Kódy typů jsou určeny pouze pro interní použití. Routery zůstanou typu 4 a podpora bude označena v adresách routerů.

#### 3) SessionConfirmed

Nezměněno

#### Funkce pro odvození klíčů (KDF) (pro datovou fázi)

Nezměněno

#### Publikované adresy

Ve všech případech použijte název NTCP2 transportu jako obvykle.

Použijte stejnou adresu/port jako non-PQ, non-firewalled. Je podporována pouze jedna PQ varianta. V adrese routeru publikujte v=2 (jako obvykle) a nový parametr pq=[3|4|5] pro označení MLKEM 512/768/1024. Alice nastaví MSB dočasného klíče (key[31] & 0x80) v požadavku relace pro označení, že se jedná o hybridní spojení. Viz výše. Starší routery budou parametr pq ignorovat a připojí se non-pq jako obvykle.

Různá adresa/port jako non-PQ, nebo pouze PQ, bez firewallu NENÍ podporováno. Toto nebude implementováno, dokud nebude zakázáno non-PQ NTCP2, což bude za několik let. Když bude non-PQ zakázáno, může být podporováno více PQ variant, ale pouze jedna na adresu. Když bude podporováno, v router adrese publikuj v=[3|4|5] pro označení MLKEM 512/768/1024. Alice nenastavuje MSB ephemeral klíče. Starší routery zkontrolují parametr v a přeskočí tuto adresu jako nepodporovanou.

Adresy za firewallem (žádná IP zveřejněna): V adrese routeru zveřejněte v=2 (jako obvykle). Není potřeba zveřejňovat parametr pq.

Alice se může připojit k PQ Bobovi pomocí PQ varianty, kterou Bob publikuje, bez ohledu na to, zda Alice inzeruje podporu pq ve svých informacích routeru, nebo zda inzeruje stejnou variantu.

#### Maximální výplň

V současné specifikaci jsou zprávy 1 a 2 definovány tak, aby měly "rozumné" množství paddingu, s doporučeným rozsahem 0-31 bajtů a bez specifikovaného maxima.

Do API 0.9.68 (vydání 2.11.0) implementovala Java I2P maximum 256 bajtů padding pro non-PQ připojení, avšak toto nebylo dříve zdokumentováno. Od API 0.9.69 (vydání 2.12.0) implementuje Java I2P stejné maximální padding pro non-PQ připojení jako pro MLKEM-512. Viz tabulka níže.

Použijte definovanou velikost zprávy jako maximální padding, to znamená, že maximální padding zdvojnásobí velikost zprávy pro PQ připojení, a to následovně:

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Message Max Padding</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">non-PQ (do 0.9.68)</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">non-PQ (od 0.9.69)</th>
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

## Analýza režie

### Výměna klíčů

Nárůst velikosti (bajtů):

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Typ</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Pubkey (Msg 1)</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Cipertext (Msg 2)</th>
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

## Analýza bezpečnosti

Bezpečnostní kategorie NIST jsou shrnuty v [NIST prezentaci](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) na snímku 10. Předběžná kritéria: Naše minimální bezpečnostní kategorie NIST by měla být 2 pro hybridní protokoly a 3 pro PQ-only.

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Kategorie</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Tak bezpečná jako</th>
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

Všechny tyto protokoly jsou hybridní. Implementace by měly preferovat MLKEM768; MLKEM512 není dostatečně bezpečný.

Bezpečnostní kategorie NIST [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf):

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Algoritmus</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Kategorie zabezpečení</th>
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

## Poznámky k implementaci

### Podpora knihoven

Knihovny Bouncycastle, BoringSSL a WolfSSL nyní podporují MLKEM a MLDSA. Podpora OpenSSL bude v jejich vydání 3.5 dne 8. dubna 2025 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

### Identifikace příchozího provozu

Nastavujeme MSB dočasného klíče (key[31] & 0x80) v session request, abychom označili, že se jedná o hybridní spojení. To nám umožňuje provozovat standardní NTCP i hybridní NTCP na stejném portu. Pro příchozí spojení je podporována pouze jedna hybridní varianta, která je inzerována v router address. Například pq=3 nebo pq=4.

#### Obfuskace

Jako Alice, pro PQ spojení, před obfuskací nastav X[31] |= 0x80. Tím se X stane neplatným X25519 veřejným klíčem. Po obfuskaci ho AES-CBC randomizuje. MSB z X bude po obfuskaci náhodný.

Jako Bob testujte, zda (X[31] & 0x80) != 0 po de-obfuskaci. Pokud ano, jedná se o PQ připojení.

Minimální verze routeru vyžadovaná pro NTCP2-PQ bude určena později.

Poznámka: Kódy typů jsou pouze pro interní použití. Routery zůstanou typu 4 a podpora bude uvedena v adresách routerů.

## Kompatibilita routeru

### Názvy transportů

Ve všech případech použijte název transportu NTCP2 jako obvykle. Starší routery budou ignorovat parametr pq a připojí se pomocí standardního NTCP2 jako obvykle.

## Reference

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
