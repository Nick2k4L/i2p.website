---
title: "ECIES-X25519 Router Zprávy"
description: "Specifikace pro šifrování garlic zpráv pro ECIES routery pomocí X25519"
slug: "ecies-routers"
category: "Protokoly"
lastUpdated: "2025-03"
accurateFor: "0.9.65"
---

## Poznámka

Podporováno od verze 0.9.49. Nasazení a testování v síti probíhá. Může podléhat menším revizím. Viz [návrh 156](/proposals/156-ecies-routers).

## Přehled

Tento dokument specifikuje šifrování garlic zpráv pro ECIES routery, používající kryptografické primitiva zavedená v [ECIES-X25519](/docs/specs/ecies). Je součástí celkového [návrhu 156](/proposals/156-ecies-routers) pro převod routerů z ElGamal na ECIES-X25519 klíče. Tato specifikace je implementována od verze 0.9.49.

Pro přehled všech změn požadovaných pro ECIES routery viz [návrh 156](/proposals/156-ecies-routers). Pro Garlic Messages do ECIES-X25519 destinací viz [ECIES-X25519](/docs/specs/ecies).

### Kryptografické primitiva

Primitiva potřebná k implementaci této specifikace jsou:

- AES-256-CBC jak v [Cryptography](/docs/specs/cryptography)
- STREAM ChaCha20/Poly1305 funkce: ENCRYPT(k, n, plaintext, ad) a DECRYPT(k, n, ciphertext, ad) - jak v [NTCP2](/docs/specs/ntcp2), [ECIES-X25519](/docs/specs/ecies), a [RFC-7539](https://tools.ietf.org/html/rfc7539)
- X25519 DH funkce - jak v [NTCP2](/docs/specs/ntcp2) a [ECIES-X25519](/docs/specs/ecies)
- HKDF(salt, ikm, info, n) - jak v [NTCP2](/docs/specs/ntcp2) a [ECIES-X25519](/docs/specs/ecies)

Další Noise funkce definované jinde:

- MixHash(d) - jako v [NTCP2](/docs/specs/ntcp2) a [ECIES-X25519](/docs/specs/ecies)
- MixKey(d) - jako v [NTCP2](/docs/specs/ntcp2) a [ECIES-X25519](/docs/specs/ecies)

## Návrh

ECIES Router SKM nepotřebuje plný Ratchet SKM jak je specifikováno v [ECIES](/docs/specs/ecies) pro Destinations. Neexistuje požadavek na neanonymní zprávy používající IK pattern. Model hrozeb nevyžaduje Elligator2-kódované ephemeral klíče.

Proto router SKM bude používat Noise "N" vzor, stejně jako je specifikováno v [Prop152](/proposals/152-ecies-tunnels) pro budování tunnelů. Bude používat stejný formát payload jako je specifikován v [ECIES](/docs/specs/ecies) pro Destinations. Režim nulového statického klíče (bez vazby nebo relace) IK specifikovaný v [ECIES](/docs/specs/ecies) nebude používán.

Odpovědi na vyhledávání budou šifrovány pomocí ratchet tagu, pokud je to požadováno ve vyhledávání. To je zdokumentováno v [Prop154](/proposals/154-ecies-lookups), nyní specifikováno v [I2NP](/docs/specs/i2np).

Návrh umožňuje routeru mít jediného ECIES Session Key Managera. Není třeba provozovat "dual key" Session Key Managery, jak je popsáno v [ECIES](/docs/specs/ecies) pro Destinations. Routery mají pouze jeden veřejný klíč.

ECIES router nemá statický ElGamal klíč. Router stále potřebuje implementaci ElGamal pro vytváření tunnelů přes ElGamal routery a odesílání šifrovaných zpráv do ElGamal routerů.

ECIES router MŮŽE vyžadovat částečný ElGamal Session Key Manager pro příjem ElGamal-tagovaných zpráv přijatých jako odpovědi na NetDB vyhledávání od floodfill routerů před verzí 0.9.46, protože tyto routery nemají implementaci ECIES-tagovaných odpovědí jak je specifikováno v [Prop152](/proposals/152-ecies-tunnels). Pokud ne, ECIES router nemusí požadovat šifrovanou odpověď od floodfill routeru před verzí 0.9.46.

Toto je volitelné. Rozhodnutí se může lišit v různých implementacích I2P a může záviset na množství sítě, která byla upgradována na verzi 0.9.46 nebo vyšší. K tomuto datu je přibližně 85% sítě na verzi 0.9.46 nebo vyšší.

### Noise Protocol Framework

Tato specifikace poskytuje požadavky založené na [Noise Protocol Framework](https://noiseprotocol.org/noise.html) (Revize 34, 2018-07-11). V terminologii Noise je Alice iniciátor a Bob odpovídající strana.

Je založen na Noise protokolu Noise_N_25519_ChaChaPoly_SHA256. Tento Noise protokol používá následující primitiva:

- **Jednosměrný handshake vzor: N** - Alice nepřenáší svůj statický klíč Bobovi (N)
- **DH funkce: X25519** - X25519 DH s délkou klíče 32 bajtů jak je specifikováno v [RFC-7748](https://tools.ietf.org/html/rfc7748).
- **Šifrovací funkce: ChaChaPoly** - AEAD_CHACHA20_POLY1305 jak je specifikováno v [RFC-7539](https://tools.ietf.org/html/rfc7539) sekce 2.8. 12 bajtový nonce, s prvními 4 bajty nastavenými na nulu. Identické s tím v [NTCP2](/docs/specs/ntcp2).
- **Hash funkce: SHA256** - Standardní 32-bajtový hash, již hojně používaný v I2P.

### Vzory handshake

Handshakes používají [Noise](https://noiseprotocol.org/noise.html) handshake vzory.

Používá se následující mapování písmen:

- e = jednorázový dočasný klíč
- s = statický klíč
- p = obsah zprávy

Požadavek na sestavení je identický se vzorem Noise N. To je také identické s první zprávou (Session Request) ve vzoru XK používaném v [NTCP2](/docs/specs/ntcp2).

```
<- s
  ...
  e es p ->
```
### Šifrování zpráv

Zprávy jsou vytvořeny a asymetricky šifrovány pro cílový router. Toto asymetrické šifrování zpráv je v současnosti ElGamal, jak je definováno v [Cryptography](/docs/specs/cryptography) a obsahuje SHA-256 kontrolní součet. Tento návrh není forward-secret (nezaručuje dopřednou bezpečnost).

Návrh ECIES používá jednosměrný Noise vzor "N" s ECIES-X25519 ephemeral-static DH, s HKDF a ChaCha20/Poly1305 AEAD pro forward secrecy (dopřednou bezpečnost), integritu a autentizaci. Alice je anonymní odesílatel zprávy, router nebo cíl. Cílový ECIES router je Bob.

### Šifrování odpovědí

Odpovědi nejsou součástí tohoto protokolu, protože Alice je anonymní. Klíče pro odpovědi, pokud existují, jsou zabaleny ve zprávě požadavku. Viz [specifikace I2NP](/docs/specs/i2np) pro Database Lookup Messages.

Odpovědi na zprávy Database Lookup jsou zprávy Database Store nebo Database Search Reply. Jsou šifrovány jako zprávy Existing Session s 32-bytovým reply key a 8-bytovým reply tag jak je specifikováno v [I2NP](/docs/specs/i2np) a [Prop154](/proposals/154-ecies-lookups).

Neexistují žádné explicitní odpovědi na zprávy Database Store. Odesílatel může přibalit svou vlastní odpověď jako Garlic Message sám sobě, obsahující zprávu Delivery Status.

## Specifikace

X25519: Viz [ECIES](/docs/specs/ecies).

Identita routeru a klíčový certifikát: Viz [Běžné struktury](/docs/specs/common-structures).

### Šifrování požadavků

Šifrování požadavku je stejné jako je specifikováno v [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) a [Prop152](/proposals/152-ecies-tunnels), používající Noise "N" vzor.

Odpovědi na vyhledávání budou zašifrovány pomocí ratchet tagu, pokud je to požadováno ve vyhledávání. Zprávy Database Lookup obsahují 32-bytový reply key a 8-bytový reply tag podle specifikace v [I2NP](/docs/specs/i2np) a [Prop154](/proposals/154-ecies-lookups). Klíč a tag se používají k šifrování odpovědi.

Sady tagů nejsou vytvořeny. Schéma nulového statického klíče specifikované v ECIES-X25519-AEAD-Ratchet [Prop144](/proposals/144-ecies-x25519-aead-ratchet) a [ECIES](/docs/specs/ecies) nebude použito. Dočasné klíče nebudou kódovány pomocí Elligator2.

Obecně se bude jednat o zprávy New Session a budou odeslány s nulovým statickým klíčem (žádné propojení nebo relace), protože odesílatel zprávy je anonymní.

#### KDF pro počáteční ck a h

Toto je standardní [Noise](https://noiseprotocol.org/noise.html) pro vzor "N" se standardním názvem protokolu. Jedná se o totéž, co je specifikováno v [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) a [Prop152](/proposals/152-ecies-tunnels) pro zprávy budování tunelů.

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
#### KDF pro zprávu

Tvůrci zpráv generují pro každou zprávu dočasný X25519 klíčový pár. Dočasné klíče musí být jedinečné pro každou zprávu. Toto je stejné jako specifikováno v [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) a [Prop152](/proposals/152-ecies-tunnels) pro zprávy výstavby tunelů.

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
#### Datová část

Payload má stejný formát bloku jako je definován v [ECIES](/docs/specs/ecies) a [Prop144](/proposals/144-ecies-x25519-aead-ratchet). Všechny zprávy musí obsahovat blok DateTime pro prevenci opakovaného přehrání.

## Poznámky k implementaci

- Starší routery nekontrolují typ šifrování routeru a budou posílat ElGamal-šifrované zprávy. Některé nedávné routery obsahují chyby a budou posílat různé typy poškozených zpráv. Implementátoři by měli tyto záznamy detekovat a odmítnout před DH operací, pokud je to možné, aby se snížilo využití CPU.

## Reference

- [Běžné struktury](/docs/specs/common-structures)
- [Kryptografie](/docs/specs/cryptography)
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
