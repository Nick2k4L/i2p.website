---
title: "Specifikace běžných struktur"
description: "Datové typy společné pro všechny I2P protokoly"
slug: "common-structures"
category: "Návrh"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

Tento dokument popisuje některé datové typy společné pro všechny I2P protokoly, jako jsou [I2NP](/docs/specs/i2np/), [I2CP](/docs/specs/i2cp/), [SSU](/docs/legacy/ssu/) atd.

## Specifikace společného typu

### Celé číslo

#### Popis

Představuje nezáporné celé číslo.

#### Obsah

1 až 8 bajtů v síťovém pořadí bajtů (big endian) reprezentujících unsigned integer.

### Datum

#### Popis

Počet milisekund od půlnoci 1. ledna 1970 v časovém pásmu GMT. Pokud je číslo 0, datum je nedefinované nebo null.

#### Obsah

8 byte [Integer](#integer)

### Řetězec

#### Popis

Představuje řetězec kódovaný v UTF-8.

#### Obsah

1 nebo více bajtů, kde první bajt je počet bajtů (ne znaků!) v řetězci a zbývajících 0-255 bajtů je pole znaků kódovaných v UTF-8 bez nulového ukončení. Limit délky je 255 bajtů (ne znaků). Délka může být 0.

### PublicKey

#### Popis

Tato struktura se používá v ElGamal nebo jiném asymetrickém šifrování a představuje pouze exponent, nikoli prvočísla, která jsou konstantní a definovaná ve specifikaci kryptografie [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy). Další schémata šifrování jsou v procesu definování, viz tabulka níže.

#### Obsah

Typ a délka klíče jsou odvozeny z kontextu nebo jsou specifikovány v Key Certificate destinace nebo RouterInfo, nebo v polích [LeaseSet2](#leaseset2) nebo jiné datové struktury. Výchozí typ je ElGamal. Od verze 0.9.38 mohou být podporovány další typy v závislosti na kontextu. Klíče jsou big-endian, pokud není uvedeno jinak.

X25519 klíče jsou podporovány v Destinations a LeaseSet2 od vydání 0.9.44. X25519 klíče jsou podporovány v RouterIdentities od vydání 0.9.48.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there; discouraged for leasesets</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Little-endian. See <a href="/docs/specs/ecies/">ECIES</a> and <a href="/docs/specs/ecies-routers/">ECIES-ROUTERS</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">800</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1184</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1568</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1088</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1568</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/PublicKey.html

### PrivateKey

#### Popis

Tato struktura se používá v ElGamal nebo jiném asymetrickém dešifrování a představuje pouze exponent, nikoli prvočísla, která jsou konstantní a definována ve specifikaci kryptografie [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy). Další šifrovací schémata jsou v procesu definování, viz tabulka níže.

#### Obsah

Typ a délka klíče jsou odvozeny z kontextu nebo jsou uloženy samostatně v datové struktuře nebo v souboru privátního klíče. Výchozí typ je ElGamal. Od verze 0.9.38 mohou být v závislosti na kontextu podporovány i jiné typy. Klíče jsou v big-endian formátu, pokud není uvedeno jinak.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there; discouraged for leasesets</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">48</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">66</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Little-endian. See <a href="/docs/specs/ecies/">ECIES</a> and <a href="/docs/specs/ecies-routers/">ECIES-ROUTERS</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1632</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2400</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3168</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/PrivateKey.html

### SessionKey

#### Popis

Tato struktura se používá pro symetrické šifrování a dešifrování AES256.

#### Obsah

32 bytů

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionKey.html

### SigningPublicKey

#### Popis

Tato struktura se používá k ověřování podpisů.

#### Obsah

Typ a délka klíče jsou odvozeny z kontextu nebo jsou specifikovány v Key Certificate cíle (Destination). Výchozí typ je DSA_SHA1. Od verze 0.9.12 mohou být podporovány další typy v závislosti na kontextu.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### Poznámky

* Když je klíč složen ze dvou prvků (například body X,Y), je
  serializován tak, že se každý prvek doplní na délku/2 vedoucími nulami
  v případě potřeby.

* Všechny typy jsou Big Endian, kromě EdDSA a RedDSA, které jsou uloženy a přenášeny ve formátu Little Endian.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPublicKey.html

### SigningPrivateKey

#### Popis

Tato struktura se používá pro vytváření podpisů.

#### Obsah

Typ a délka klíče jsou specifikovány při vytvoření. Výchozí typ je DSA_SHA1. Od verze 0.9.12 mohou být podporovány další typy v závislosti na kontextu.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">48</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">66</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### Poznámky

* Když je klíč složen ze dvou elementů (například body X,Y), je
  serializován tak, že každý element je doplněn na délku/2 s počátečními nulami,
  pokud je to nutné.

* Všechny typy jsou Big Endian, kromě EdDSA a RedDSA, které jsou ukládány a přenášeny
  ve formátu Little Endian.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPrivateKey.html

### Podpis

#### Popis

Tato struktura představuje podpis nějakých dat.

#### Obsah

Typ a délka podpisu se odvozují z typu použitého klíče. Výchozím typem je DSA_SHA1. Od verze 0.9.12 mohou být podporovány další typy v závislosti na kontextu.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">40</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### Poznámky

* Když se podpis skládá ze dvou elementů (například hodnoty R,S), je serializován tak, že se každý element doplní na délku/2 úvodními nulami, pokud je to nutné.

* Všechny typy jsou Big Endian, kromě EdDSA a RedDSA, které jsou ukládány a přenášeny
  ve formátu Little Endian.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Signature.html

### Hash

#### Popis

Představuje SHA256 některých dat.

#### Obsah

32 bytů

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Hash.html

### Session Tag

Poznámka: Session Tags pro ECIES-X25519 cíle (ratchet) a ECIES-X25519 routery mají 8 bajtů. Viz [ECIES](/docs/specs/ecies/) a [ECIES-ROUTERS](/docs/specs/ecies-routers/).

#### Popis

Náhodné číslo

#### Obsah

32 bajtů

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionTag.html

### TunnelId

#### Popis

Definuje identifikátor, který je jedinečný pro každý router v tunelu. Tunnel ID je obecně větší než nula; nepoužívejte hodnotu nula kromě speciálních případů.

#### Obsah

4 byte [Integer](#integer)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/TunnelId.html

### Certifikát

#### Popis

Certifikát je kontejner pro různé potvrzení nebo důkazy prací používané v síti I2P.

#### Obsah

1 bajt [Integer](#integer) určující typ certifikátu, následovaný 2 bajty [Integer](#integer) určujícími velikost dat certifikátu, poté tolik bajtů.

```
+----+----+----+----+----+-/
|type| length  | payload
+----+----+----+----+----+-/

type :: `Integer`
        length -> 1 byte

        case 0 -> NULL
        case 1 -> HASHCASH
        case 2 -> HIDDEN
        case 3 -> SIGNED
        case 4 -> MULTIPLE
        case 5 -> KEY

length :: `Integer`
          length -> 2 bytes

payload :: data
           length -> $length bytes
```
#### Poznámky

* Pro [Router Identities](#routeridentity) je Certificate vždy NULL až do verze
  0.9.15. Od verze 0.9.16 se používá Key Certificate pro specifikaci
  typů klíčů. Od verze 0.9.48 jsou povoleny typy X25519 encryption public key.
  Viz níže.

* Pro [Garlic Cloves](/docs/specs/i2np/#struct-garlicclove) je Certificate vždy NULL, žádné další nejsou v současnosti
  implementovány.

* Pro [Garlic Messages](/docs/specs/i2np/#msg-garlic) je Certificate vždy NULL, žádné další nejsou v současnosti implementovány.

* Pro [Destinations](#destination) může být Certificate nenulový. Od verze 0.9.12 může být Key Certificate použit pro specifikaci typu veřejného klíče pro podepisování. Viz níže.

* Implementátoři jsou upozorněni, aby zakázali nadbytečná data v Certificates.
  Odpovídající délka pro každý typ certifikátu by měla být vynucena.

#### Typy certifikátů

Následující typy certifikátů jsou definovány:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">HashCash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains an ASCII colon-separated hashcash string.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Hidden</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Hidden routers generally do not announce that they are hidden.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Signed</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">40 or 72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">43 or 75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains a 40-byte DSA signature, optionally followed by the 32-byte Hash of the signing Destination.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Multiple</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains multiple certificates.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4+</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7+</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Since 0.9.12. See below for details.</td>
    </tr>
  </tbody>
</table>
#### Certifikáty klíčů

Klíčové certifikáty byly představeny ve verzi 0.9.12. Před touto verzí byly všechny PublicKeys 256-bytové ElGamal klíče a všechny SigningPublicKeys byly 128-bytové DSA-SHA1 klíče. Klíčový certifikát poskytuje mechanismus pro označení typu PublicKey a SigningPublicKey v Destination nebo RouterIdentity a pro zabalení jakýchkoli klíčových dat přesahujících standardní délky.

Udržováním přesně 384 bajtů před certifikátem a umístěním všech přebytečných klíčových dat do certifikátu zachováváme kompatibilitu pro jakýkoli software, který parsuje Destinations a Router Identities.

Payload klíčového certifikátu obsahuje:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Signing Public Key Type (<a href="#integer">Integer</a>)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Crypto Public Key Type (<a href="#integer">Integer</a>)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Excess Signing Public Key Data</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0+</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Excess Crypto Public Key Data</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0+</td>
    </tr>
  </tbody>
</table>
Varování: Pořadí typů klíčů je opačné, než byste mohli očekávat; Signing Public Key Type je na prvním místě.

Definované typy veřejných klíčů pro podepisování jsou:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Public Key Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely if ever used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely if ever used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (GOST)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/134-gost/">Prop134</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (GOST)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/134-gost/">Prop134</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only; never used for Router Identities</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">13</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">14</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65280-65534</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for experimental use</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65535</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for future expansion</td>
    </tr>
  </tbody>
</table>
Definované typy Crypto Public Key jsou:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Public Key Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies/">ECIES</a> and proposal 156</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (NONE)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">255</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65280-65534</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for experimental use</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65535</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for future expansion</td>
    </tr>
  </tbody>
</table>
Když Key Certificate není přítomen, předchozích 384 bytů v Destination nebo RouterIdentity je definováno jako 256-bytový ElGamal PublicKey následovaný 128-bytovým DSA-SHA1 SigningPublicKey. Když je Key Certificate přítomen, předchozích 384 bytů je předefinováno následovně:

* Kompletní nebo první část kryptografického veřejného klíče

* Náhodné vyplnění, pokud je celková délka obou klíčů menší než 384 bajtů

* Kompletní nebo první část Signing Public Key

Crypto Public Key je zarovnán na začátku a Signing Public Key je zarovnán na konci. Výplň (pokud existuje) je uprostřed. Délky a hranice počátečních klíčových dat, výplně a nadbytečných klíčových dat v certifikátech nejsou explicitně specifikovány, ale jsou odvozeny z délek specifikovaných typů klíčů. Pokud celková délka Crypto a Signing Public Keys překročí 384 bajtů, zbytek bude obsažen v Key Certificate. Pokud délka Crypto Public Key není 256 bajtů, metoda pro určení hranice mezi oběma klíči bude specifikována v budoucí revizi tohoto dokumentu.

Příklady rozložení používající ElGamal Crypto Public Key a uvedený typ Signing Public Key:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Signing Key Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Excess Signing Key Data in Cert</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Certificate.html

#### Poznámky

* Implementátorům se doporučuje zakázat nadměrná data v Key Certificates.
  Měla by být vynucena odpovídající délka pro každý typ certifikátu.

* KEY certifikát s typy 0,0 (ElGamal,DSA_SHA1) je povolen, ale nedoporučuje se.
  Není dobře otestován a může způsobit problémy v některých implementacích.
  Použijte NULL certifikát v kanonické reprezentaci
  (ElGamal,DSA_SHA1) Destination nebo RouterIdentity, který bude o 4 bajty kratší
  než použití KEY certifikátu.

### Mapování

#### Popis

Sada mapování klíč/hodnota nebo vlastností

#### Obsah

2-bajtové celé číslo velikosti následované řadou párů String=String;.

VAROVÁNÍ: Většina použití Mapping je ve podepsaných strukturách, kde musí být položky Mapping seřazeny podle klíče, aby byl podpis neměnný. Neseřazení podle klíče povede k selhání podpisu!

```
+----+----+----+----+----+----+----+----+
|  size   | key_string (len + data)| =  |
+----+----+----+----+----+----+----+----+
| val_string (len + data)     | ;  | ...
+----+----+----+----+----+----+----+
size :: `Integer`
        length -> 2 bytes
        Total number of bytes that follow

key_string :: `String`
              A string (one byte length followed by UTF-8 encoded characters)

= :: A single byte containing '='

val_string :: `String`
              A string (one byte length followed by UTF-8 encoded characters)

; :: A single byte containing ';'
```
#### Poznámky

* Kódování není optimální - potřebujeme buď znaky '=' a ';', nebo
  délky řetězců, ale ne obojí

* Některá dokumentace uvádí, že řetězce nesmí obsahovat '=' nebo ';', ale toto kódování je podporuje

* Řetězce jsou definovány jako UTF-8, ale v současné implementaci I2CP používá
  UTF-8, ale I2NP nikoli. Například UTF-8 řetězce v mapování možností RouterInfo
  v I2NP Database Store Message budou poškozeny.

* Kódování umožňuje duplicitní klíče, avšak při jakémkoli použití, kde je mapování
  podepsáno, mohou duplicity způsobit selhání podpisu.

* Mapování obsažená v I2NP zprávách (např. v RouterAddress nebo RouterInfo)
  musí být seřazena podle klíče, aby byl podpis neměnný. Duplicitní klíče
  nejsou povoleny.

* Mapování obsažená v [I2CP SessionConfig](/docs/specs/i2cp/#struct-sessionconfig) musí být seřazena podle klíče tak, aby
  podpis byl invariantní. Duplicitní klíče nejsou povoleny.

* Metoda řazení je definována stejně jako v Java String.compareTo(), používající Unicode hodnoty znaků.

* Ačkoli je to závislé na aplikaci, klíče a hodnoty jsou obecně
  citlivé na velikost písmen.

* Limity délky řetězců klíče a hodnoty jsou 255 bajtů (nikoli znaků) každý, plus
  bajt délky. Bajt délky může být 0.

* Celkový limit délky je 65535 bajtů, plus 2bajtové pole velikosti, nebo celkem 65537.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/DataHelper.html

## Specifikace společné struktury

### KeysAndCert

#### Popis

Veřejný šifrovací klíč, veřejný podepisovací klíč a certifikát, používané buď jako RouterIdentity nebo Destination.

#### Obsah

[PublicKey](#publickey) následovaný [SigningPublicKey](#signingpublickey) a poté [Certificate](#certificate).

```
+----+----+----+----+----+----+----+----+
| public_key                            |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| padding (optional)                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signing_key                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| certificate                           |
+----+----+----+-/

public_key :: `PublicKey` (partial or full)
              length -> 256 bytes or as specified in key certificate

padding :: random data
           length -> 0 bytes or as specified in key certificate
           public_key length + padding length + signing_key length == 384 bytes

signing__key :: `SigningPublicKey` (partial or full)
                length -> 128 bytes or as specified in key certificate

certificate :: `Certificate`
               length -> >= 3 bytes

total length: 387+ bytes
```
#### Pokyny pro generování výplně

Tyto pokyny byly navrženy v Návrhu 161 a implementovány v API verzi 0.9.57. Tyto pokyny jsou zpětně kompatibilní se všemi verzemi od 0.6 (2005). Viz Návrh 161 pro další informace a pozadí.

Pro jakoukoli aktuálně používanou kombinaci typů klíčů jinou než ElGamal + DSA-SHA1 bude přítomno vyplnění. Navíc pro destinace je pole veřejného klíče o velikosti 256 bajtů nepoužívané od verze 0.6 (2005).

Implementátoři by měli generovat náhodná data pro veřejné klíče Destination a pro padding v Destination a Router Identity tak, aby byla komprimovatelná v různých I2P protokolech, přičemž zůstanou bezpečná a jejich Base 64 reprezentace nebudou vypadat jako poškozené nebo nebezpečné. Toto poskytuje většinu výhod odebrání padding polí bez jakýchkoli rušivých změn protokolu.

Přísně vzato, samotný 32bajtový veřejný klíč pro podepisování (jak v Destinations, tak v Router Identities) a 32bajtový veřejný klíč pro šifrování (pouze v Router Identities) je náhodné číslo, které poskytuje veškerou entropii potřebnou k tomu, aby byly SHA-256 hashe těchto struktur kryptograficky silné a náhodně distribuované v DHT síťové databáze.

Nicméně z důvodu maximální opatrnosti doporučujeme použít minimálně 32 bajtů náhodných dat v poli ElG veřejného klíče a paddingu. Navíc, pokud by všechna pole byla nulová, Base 64 destinace by obsahovaly dlouhé řady znaků AAAA, což by mohlo uživatele znepokojit nebo zmást.

Opakujte 32 bajtů náhodných dat podle potřeby tak, aby byla celá struktura KeysAndCert vysoce kompresibilní v I2P protokolech jako je I2NP Database Store Message, Streaming SYN, SSU2 handshake a repliable Datagrams.

Příklady:

* Router Identity s typem šifrování X25519 a typem podpisu Ed25519
  bude obsahovat 10 kopií (320 bajtů) náhodných dat, což při kompresi ušetří přibližně 288 bajtů.

* Destination se signaturním typem Ed25519
  bude obsahovat 11 kopií (352 bajtů) náhodných dat, což při kompresi ušetří přibližně 320 bajtů.

Implementace musí samozřejmě ukládat celou strukturu o 387+ bajtech, protože SHA-256 hash této struktury pokrývá celý obsah.

#### Poznámky

* Nepředpokládejte, že tyto jsou vždy 387 bajtů! Jsou to 387 bajtů plus délka certifikátu specifikovaná na bajtech 385-386, která může být nenulová.

* Od verze 0.9.12, pokud je certifikát Key Certificate, hranice polí klíčů se mohou lišit. Podrobnosti naleznete v sekci Key Certificate výše.

* Kryptografický veřejný klíč je zarovnán na začátku a podepisovací veřejný klíč je zarovnán na konci. Výplň (pokud existuje) je uprostřed.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/KeysAndCert.html

### RouterIdentity

#### Popis

Definuje způsob, jak jednoznačně identifikovat konkrétní router

#### Obsah

Identické s KeysAndCert.

Viz [KeysAndCert](#keysandcert) pro pokyny k generování náhodných dat pro pole padding.

#### Poznámky

* Certifikát pro RouterIdentity byl vždy NULL až do vydání 0.9.12.

* Nepředpokládejte, že mají vždy 387 bytů! Mají 387 bytů plus délku certifikátu specifikovanou na bytech 385-386, která může být nenulová.

* Od verze 0.9.12, pokud je certifikát Key Certificate, hranice polí klíče se mohou lišit. Podrobnosti naleznete v části Key Certificate výše.

* Crypto Public Key je zarovnán na začátku a Signing Public Key je
  zarovnán na konci. Výplň (pokud existuje) je uprostřed.

* RouterIdentities s klíčovým certifikátem a veřejným klíčem ECIES_X25519
  jsou podporovány od vydání 0.9.48.
  Před tím byly všechny RouterIdentities ElGamal.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterIdentity.html

### Cíl

#### Popis

Destination definuje konkrétní koncový bod, na který mohou být zprávy směrovány pro bezpečné doručení.

#### Obsah

Identické s [KeysAndCert](#keysandcert), kromě toho, že veřejný klíč se nikdy nepoužívá a může obsahovat náhodná data namísto platného ElGamal veřejného klíče.

Viz [KeysAndCert](#keysandcert) pro pokyny k generování náhodných dat pro pole veřejného klíče a výplně.

#### Poznámky

* Veřejný klíč destinace byl použit pro staré i2cp-to-i2cp
  šifrování, které bylo zakázáno ve verzi 0.6 (2005), v současnosti se nepoužívá kromě
  IV pro LeaseSet šifrování, které je zastaralé. Místo toho se používá veřejný klíč v
  LeaseSet.

* Nepředpokládejte, že jsou vždy dlouhé 387 bajtů! Jsou dlouhé 387 bajtů plus délka certifikátu uvedená na bajtech 385-386, která může být nenulová.

* Od vydání 0.9.12, pokud je certifikát Key Certificate, hranice polí klíče se mohou lišit. Podrobnosti najdete v sekci Key Certificate výše.

* Kryptografický veřejný klíč je zarovnán na začátku a podepisující veřejný klíč je
  zarovnán na konci. Výplň (pokud existuje) je uprostřed.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Destination.html

### Lease

#### Popis

Definuje autorizaci pro konkrétní tunnel k přijímání zpráv směřujících k [Destination](#destination).

#### Obsah

SHA256 [Hash](#hash) [RouterIdentity](#routeridentity) gateway routeru, poté [TunnelId](#tunnelid) a nakonec konečné [Date](#date).

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     tunnel_id     |      end_date
+----+----+----+----+----+----+----+----+
                    |
+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway
             length -> 32 bytes

tunnel_id :: `TunnelId`
             length -> 4 bytes

end_date :: `Date`
            length -> 8 bytes
```
#### Poznámky

* Celková velikost: 44 bajtů

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease.html

### LeaseSet

#### Popis

Obsahuje všechny aktuálně autorizované [Leases](#lease) pro konkrétní [Destination](#destination), [PublicKey](#publickey) do kterého mohou být zašifrovány garlic zprávy, a poté [SigningPublicKey](#signingpublickey) který může být použit k odvolání této konkrétní verze struktury. LeaseSet je jedna ze dvou struktur uložených v síťové databázi (druhou je [RouterInfo](#routerinfo)) a je indexována pod SHA256 obsaženého [Destination](#destination).

#### Obsah

[Destination](#destination), následovaný [PublicKey](#publickey) pro šifrování, poté [SigningPublicKey](#signingpublickey), který lze použít k odvolání této verze LeaseSet, poté 1 byte [Integer](#integer) specifikující kolik struktur [Lease](#lease) je v sadě, následovaný skutečnými strukturami [Lease](#lease) a nakonec [Signature](#signature) předchozích bytů podepsaný [SigningPrivateKey](#signingprivatekey) [Destination](#destination).

```
+----+----+----+----+----+----+----+----+
| destination                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| encryption_key                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signing_key                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| Lease 0                          |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease 1                               |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease ($num-1)                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+

destination :: `Destination`
               length -> >= 387+ bytes

encryption_key :: `PublicKey`
                  length -> 256 bytes

signing_key :: `SigningPublicKey`
               length -> 128 bytes or as specified in destination's key
                         certificate

num :: `Integer`
       length -> 1 byte
       Number of leases to follow
       value: 0 <= num <= 16

leases :: [`Lease`]
          length -> $num*44 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate
```
#### Poznámky

* Veřejný klíč destinace byl použit pro staré I2CP-to-I2CP šifrování, které bylo zakázáno ve verzi 0.6, v současnosti se nepoužívá.

* Šifrovací klíč se používá pro end-to-end ElGamal/AES+SessionTag šifrování
  [ELGAMAL-AES](/docs/specs/elgamal-aes/). V současnosti se generuje znovu při každém spuštění routeru, není
  trvalý.

* Podpis může být ověřen pomocí veřejného podepisovacího klíče cíle.

* LeaseSet s nulovými Lease je povolený, ale nepoužívá se.
  Byl zamýšlen pro odvolání LeaseSet, což není implementováno.
  Všechny varianty LeaseSet2 vyžadují alespoň jeden Lease.

* signing_key se v současnosti nepoužívá. Byl určen pro odvolání LeaseSet,
  což není implementováno. V současnosti se generuje znovu při každém spuštění routeru,
  není trvalý. Typ signing key je vždy stejný jako typ signing key destinace.

* Nejdřívější vypršení ze všech Lease je považováno za časové razítko nebo
  verzi LeaseSet. Routery obecně neakceptují uložení LeaseSet, pokud není
  "novější" než současný. Buďte opatrní při publikování nového LeaseSet,
  kde nejstarší Lease je stejný jako nejstarší Lease v předchozím LeaseSet.
  Publikující router by měl obecně zvýšit vypršení nejstaršího Lease
  nejméně o 1 ms v takovém případě.

* Před vydáním verze 0.9.7, když byl zahrnut ve zprávě DatabaseStore odeslané původním routerem, router nastavil všechna zveřejněná lease vypršení na stejnou hodnotu, a to hodnotu nejdříve vypršujícího lease. Od vydání verze 0.9.7 router publikuje skutečné vypršení lease pro každý lease. Toto je implementační detail a není součástí specifikace struktur.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet.html

### Lease2

#### Popis

Definuje autorizaci pro konkrétní tunnel pro příjem zpráv cílených na [Destination](#destination). Stejné jako [Lease](#lease), ale s 4-bytovým end_date. Používá [LeaseSet2](#leaseset2). Podporováno od verze 0.9.38; více informací viz návrh 123.

#### Obsah

SHA256 [Hash](#hash) [RouterIdentity](#routeridentity) gateway routeru, poté [TunnelId](#tunnelid) a nakonec 4bajtové datum ukončení.

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     tunnel_id     |      end_date     |
+----+----+----+----+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway
             length -> 32 bytes

tunnel_id :: `TunnelId`
             length -> 4 bytes

end_date :: 4 byte date
            length -> 4 bytes
            Seconds since the epoch, rolls over in 2106.

```
#### Poznámky

* Celková velikost: 40 bajtů

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease2.html

### OfflineSignature

#### Popis

Toto je volitelná část [LeaseSet2Header](#leaseset2header). Také se používá ve streaming a I2CP. Podporováno od verze 0.9.38; další informace viz návrh 123.

#### Obsah

Obsahuje expiraci, sigtype a přechodný [SigningPublicKey](#signingpublickey) a [Signature](#signature).

```
+----+----+----+----+----+----+----+----+
|     expires       | sigtype |         |
+----+----+----+----+----+----+         +
|       transient_public_key            |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|           signature                   |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

expires :: 4 byte date
           length -> 4 bytes
           Seconds since the epoch, rolls over in 2106.

sigtype :: 2 byte type of the transient_public_key
           length -> 2 bytes

transient_public_key :: `SigningPublicKey`
                        length -> As inferred from the sigtype

signature :: `Signature`
             length -> As inferred from the sigtype of the signing public key
                       in the `Destination` that preceded this offline signature.
             Signature of expires timestamp, transient sig type, and public key,
             by the destination public key.

```
#### Poznámky

* Tato sekce může být a měla by být generována offline.

### LeaseSet2Header

#### Popis

Toto je společná část [LeaseSet2](#leaseset2) a [MetaLeaseSet](#metaleaseset). Podporováno od verze 0.9.38; více informací najdete v návrhu 123.

#### Obsah

Obsahuje [Destination](#destination), dva časové razítka a volitelný [OfflineSignature](#offlinesignature).

```
+----+----+----+----+----+----+----+----+
| destination                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|     published     | expires |  flags  |
+----+----+----+----+----+----+----+----+
| offline_signature (optional)          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

destination :: `Destination`
               length -> >= 387+ bytes

published :: 4 byte date
             length -> 4 bytes
             Seconds since the epoch, rolls over in 2106.

expires :: 2 byte time
           length -> 2 bytes
           Offset from published timestamp in seconds, 18.2 hours max

flags :: 2 bytes
  Bit order: 15 14 ... 3 2 1 0
  Bit 0: If 0, no offline keys; if 1, offline keys
  Bit 1: If 0, a standard published leaseset.
         If 1, an unpublished leaseset. Should not be flooded, published, or
         sent in response to a query. If this leaseset expires, do not query the
         netdb for a new one, unless bit 2 is set.
  Bit 2: If 0, a standard published leaseset.
         If 1, this unencrypted leaseset will be blinded and encrypted when published.
         If this leaseset expires, query the blinded location in the netdb for a new one.
         If this bit is set to 1, set bit 1 to 1 also.
         As of release 0.9.42.
  Bits 15-3: set to 0 for compatibility with future uses

offline_signature :: `OfflineSignature`
                     length -> varies
                     Optional, only present if bit 0 is set in the flags.

```
#### Poznámky

* Celková velikost: minimálně 395 bajtů

* Maximální skutečný čas vypršení je přibližně 660 (11 minut) pro
  [LeaseSet2](#leaseset2) a 65535 (plných 18,2 hodin) pro [MetaLeaseSet](#metaleaseset).

* [LeaseSet](#leaseset) (1) neměl pole 'published', takže verzování vyžadovalo
  hledání nejstaršího lease. LeaseSet2 přidává pole 'published'
  s rozlišením jedné sekundy. Routery by měly omezovat rychlost odesílání
  nových leasesetů do floodfillů na rychlost mnohem pomalejší než jednou za sekundu (na destinaci).
  Pokud toto není implementováno, pak kód musí zajistit, že každý nový leaseset
  má čas 'published' alespoň o sekundu později než ten předchozí, jinak
  floodfilly nebudou ukládat nebo šířit nový leaseset.

### LeaseSet2

#### Popis

Obsaženo ve zprávě I2NP DatabaseStore typu 3. Podporováno od verze 0.9.38; více informací viz návrh 123.

Obsahuje všechny aktuálně autorizované [Lease2](#lease2) pro konkrétní [Destination](#destination) a [PublicKey](#publickey), kterým lze šifrovat garlic zprávy. LeaseSet je jedna ze dvou struktur uložených v síťové databázi (druhou je [RouterInfo](#routerinfo)) a je indexován pod SHA256 hashem obsaženého [Destination](#destination).

#### Obsah

[LeaseSet2Header](#leaseset2header), následovaný možnostmi, poté jeden nebo více [PublicKey](#publickey) pro šifrování, [Integer](#integer) specifikující kolik [Lease2](#lease2) struktur je v sadě, následované skutečnými [Lease2](#lease2) strukturami a konečně [Signature](#signature) předchozích bajtů podepsaná [SigningPrivateKey](#signingprivatekey) [Destination](#destination) nebo přechodným klíčem.

```
+----+----+----+----+----+----+----+----+
|         ls2_header                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          options                      |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|numk| keytype0| keylen0 |              |
+----+----+----+----+----+              +
|          encryption_key_0             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| keytypen| keylenn |                   |
+----+----+----+----+                   +
|          encryption_key_n             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| Lease2 0                         |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease2($num-1)                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

ls2header :: `LeaseSet2Header`
             length -> varies

options :: `Mapping`
           length -> varies, 2 bytes minimum

numk :: `Integer`
        length -> 1 byte
        Number of key types, key lengths, and `PublicKey`s to follow
        value: 1 <= numk <= max TBD

keytype :: The encryption type of the `PublicKey` to follow.
           length -> 2 bytes

keylen :: The length of the `PublicKey` to follow.
          Must match the specified length of the encryption type.
          length -> 2 bytes

encryption_key :: `PublicKey`
                  length -> keylen bytes

num :: `Integer`
       length -> 1 byte
       Number of `Lease2`s to follow
       value: 0 <= num <= 16

leases :: [`Lease2`]
          length -> $num*40 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate, or by the sigtype of the transient public key,
                       if present in the header

```
#### Preference šifrovacího klíče

U publikovaných (serverových) leaseSets jsou šifrovací klíče seřazeny podle preferencí serveru, nejvíce preferované jsou první. Pokud klienti podporují více než jeden typ šifrování, doporučuje se, aby respektovali preference serveru a vybrali první podporovaný typ jako metodu šifrování pro připojení k serveru. Obecně jsou novější (s vyšším číslem) typy klíčů bezpečnější nebo efektivnější a jsou preferované, takže klíče by měly být uvedeny v opačném pořadí podle typu klíče.

Klienti však mohou, v závislosti na implementaci, místo toho vybírat na základě svých preferencí nebo použít nějakou metodu k určení "kombinované" preference. To může být užitečné jako konfigurační možnost nebo pro ladění.

Pořadí klíčů v nepublikovaných (klientských) leaseStech ve skutečnosti nezáleží, protože připojení k nepublikovaným klientům obvykle nebude navazováno. Pokud se toto pořadí nepoužívá k určení kombinované preference, jak je popsáno výše.

#### Možnosti

Od API 0.9.66 je definován standardní formát pro možnosti záznamů služeb. Podrobnosti naleznete v návrhu 167. V budoucnu mohou být definovány další možnosti jiné než záznamy služeb, používající jiný formát.

Možnosti LS2 MUSÍ být seřazeny podle klíče, aby byl podpis neměnný.

Možnosti záznamů služeb jsou definovány následovně:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := Symbolické jméno požadované služby. Musí být psané malými písmeny. Příklad: "smtp".
  Povolené znaky jsou [a-z0-9-] a nesmí začínat ani končit znakem '-'.
  Pokud jsou definovány, musí být použity standardní identifikátory z [REGISTRY](http://www.dns-sd.org/ServiceTypes.html) nebo Linux /etc/services.
- proto := Transportní protokol požadované služby. Musí být psán malými písmeny, buď "tcp" nebo "udp".
  "tcp" znamená streamování a "udp" znamená odpověditelné datagramy.
  Indikátory protokolu pro surové datagramy a datagram2 mohou být definovány později.
  Povolené znaky jsou [a-z0-9-] a nesmí začínat ani končit znakem '-'.
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := doba života, celočíselné sekundy. Kladné celé číslo. Příklad: "86400".
  Doporučuje se minimum 86400 (jeden den), viz sekce Doporučení níže pro podrobnosti.
- priority := Priorita cílového hostitele, nižší hodnota znamená větší preference. Nezáporné celé číslo. Příklad: "0"
  Užitečné pouze pokud je více než jeden záznam, ale vyžadováno i v případě jediného záznamu.
- weight := Relativní váha pro záznamy se stejnou prioritou. Vyšší hodnota znamená větší pravděpodobnost výběru. Nezáporné celé číslo. Příklad: "0"
  Užitečné pouze pokud je více než jeden záznam, ale vyžadováno i v případě jediného záznamu.
- port := I2CP port na kterém má být služba nalezena. Nezáporné celé číslo. Příklad: "25"
  Port 0 je podporován, ale nedoporučuje se.
- target := Hostname nebo b32 cíle poskytujícího službu. Platný hostname jak v [NAMING](/docs/overview/naming/). Musí být psán malými písmeny.
  Příklad: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" nebo "example.i2p".
  b32 je doporučeno, pokud hostname není "dobře známý", tj. v oficiálních nebo výchozích adresářích.
- appoptions := libovolný text specifický pro aplikaci, nesmí obsahovat " " nebo ",". Kódování je UTF-8.

Příklady:

V LS2 pro aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, odkazující na jeden SMTP server:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

V LS2 pro aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, ukazující na dva SMTP servery:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

V LS2 pro bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p, ukazující na sebe jako SMTP server:

"_smtp._tcp" "0 999999 25"

#### Poznámky

* Veřejný klíč destinace byl použit pro staré I2CP-to-I2CP šifrování, které bylo zakázáno ve verzi 0.6, v současnosti se nepoužívá.

* Šifrovací klíče jsou používány pro end-to-end ElGamal/AES+SessionTag šifrování
  [ELGAMAL-AES](/docs/specs/elgamal-aes/) (typ 0) nebo jiná end-to-end šifrovací schémata.
  Viz [ECIES](/docs/specs/ecies/) a návrhy 145 a 156.
  Mohou být generovány znovu při každém spuštění routeru
  nebo mohou být trvalé.
  X25519 (typ 4, viz [ECIES](/docs/specs/ecies/)) je podporováno od vydání 0.9.44.

* Podpis je nad daty výše, PŘEDŘAZENÝMI jediným bytem
  obsahujícím typ DatabaseStore (3).

* Podpis může být ověřen pomocí veřejného podpisového klíče destinace nebo přechodného podpisového veřejného klíče, pokud je offline podpis zahrnut v hlavičce leaseset2.

* Délka klíče je uvedena pro každý klíč, takže floodfilly a klienti
  mohou analyzovat strukturu i v případě, že nejsou všechny typy šifrování známé nebo podporované.

* Viz poznámku k poli 'published' v [LeaseSet2Header](#leaseset2header)

* Mapování možností, pokud je velikost větší než jedna, musí být seřazeno podle klíče, takže podpis je neměnný.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet2.html

### MetaLease

#### Popis

Definuje autorizaci pro konkrétní tunel pro přijímání zpráv cílených na [Destination](#destination). Stejné jako [Lease2](#lease2), ale s příznaky a náklady namísto tunnel id. Používá se v [MetaLeaseSet](#metaleaseset). Obsaženo ve zprávě I2NP DatabaseStore typu 7. Podporováno od verze 0.9.38; viz návrh 123 pro více informací.

#### Obsah

SHA256 [Hash](#hash) [RouterIdentity](#routeridentity) gateway routeru, pak příznaky a náklady, a nakonec 4bytové koncové datum.

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|    flags     |cost|      end_date     |
+----+----+----+----+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway,
             or the hash of another `MetaLeaseSet`.
             length -> 32 bytes

flags :: 3 bytes of flags
         Bit order: 23 22 ... 3 2 1 0
         Bits 3-0: Type of the entry.
         If 0, unknown.
         If 1, a `LeaseSet`.
         If 3, a `LeaseSet2`.
         If 5, a `MetaLeaseSet`.
         Bits 23-4: set to 0 for compatibility with future uses
         length -> 3 bytes

cost :: 1 byte, 0-255. Lower value is higher priority.
        length -> 1 byte

end_date :: 4 byte date
            length -> 4 bytes
            Seconds since the epoch, rolls over in 2106.

```
#### Poznámky

* Celková velikost: 40 bajtů

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLease.html

### MetaLeaseSet

#### Popis

Obsaženo v I2NP DatabaseStore zprávě typu 7. Definováno od verze 0.9.38; naplánováno jako funkční od verze 0.9.40; více informací viz návrh 123.

Obsahuje všechny aktuálně autorizované [MetaLease](#metalease) pro konkrétní [Destination](#destination) a [PublicKey](#publickey), kterým mohou být garlic zprávy šifrovány. LeaseSet je jedna ze dvou struktur uložených v síťové databázi (druhou je [RouterInfo](#routerinfo)) a je indexována pod SHA256 obsaženého [Destination](#destination).

#### Obsah

[LeaseSet2Header](#leaseset2header), následovaný možnostmi, [Integer](#integer) specifikující kolik struktur [Lease2](#lease2) je v sadě, následované skutečnými strukturami [Lease2](#lease2) a nakonec [Signature](#signature) předchozích bajtů podepsaných [SigningPrivateKey](#signingprivatekey) [Destination](#destination) nebo přechodným klíčem.

```
+----+----+----+----+----+----+----+----+
|         ls2_header                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          options                      |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| MetaLease 0                      |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| MetaLease($num-1)                     |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|numr|                                  |
+----+                                  +
|          revocation_0                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          revocation_n                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

ls2header :: `LeaseSet2Header`
             length -> varies

options :: `Mapping`
           length -> varies, 2 bytes minimum

num :: `Integer`
        length -> 1 byte
        Number of `MetaLease`s to follow
        value: 1 <= num <= max TBD

leases :: `MetaLease`s
          length -> $numr*40 bytes

numr :: `Integer`
        length -> 1 byte
        Number of `Hash`es to follow
        value: 0 <= numr <= max TBD

revocations :: [`Hash`]
               length -> $numr*32 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate, or by the sigtype of the transient public key,
                       if present in the header

```
#### Poznámky

* Veřejný klíč cíle byl používán pro staré I2CP-to-I2CP šifrování, které bylo vypnuto ve verzi 0.6, v současnosti se nepoužívá.

* Podpis je nad daty výše, PŘEDŘAZENÝ jedním bytem
  obsahujícím typ DatabaseStore (7).

* Podpis může být ověřen pomocí veřejného podepisovacího klíče
  destinace, nebo dočasného veřejného podepisovacího klíče, pokud je
  offline podpis zahrnut v hlavičce leaseset2.

* Viz poznámka k poli 'published' v [LeaseSet2Header](#leaseset2header)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLeaseSet.html

### EncryptedLeaseSet

#### Popis

Obsaženo ve zprávě I2NP DatabaseStore typu 5. Definováno od verze 0.9.38; funkční od verze 0.9.39; více informací v návrhu 123.

Pouze blinded klíč a vypršení jsou viditelné v čistém textu. Skutečný leaseSet je šifrovaný.

#### Obsah

Dvoubytový typ podpisu, oslepený [SigningPrivateKey](#signingprivatekey), čas publikování, vypršení a příznaky. Poté dvoubytová délka následovaná šifrovanými daty. Nakonec [Signature](#signature) předchozích bytů podepsaný oslepeným [SigningPrivateKey](#signingprivatekey) nebo přechodným klíčem.

```
+----+----+----+----+----+----+----+----+
| sigtype |                             |
+----+----+                             +
|        blinded_public_key             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|     published     | expires |  flags  |
+----+----+----+----+----+----+----+----+
| offline_signature (optional)          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  len    |                             |
+----+----+                             +
|         encrypted_data                |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

sigtype :: A two byte signature type of the public key to follow
           length -> 2 bytes

blinded_public_key :: `SigningPublicKey`
                      length -> As inferred from the sigtype

published :: 4 byte date
             length -> 4 bytes
             Seconds since the epoch, rolls over in 2106.

expires :: 2 byte time
           length -> 2 bytes
           Offset from published timestamp in seconds, 18.2 hours max

flags :: 2 bytes
  Bit order: 15 14 ... 3 2 1 0
  Bit 0: If 0, no offline keys; if 1, offline keys
  Bit 1: If 0, a standard published leaseset.
         If 1, an unpublished leaseset. Should not be flooded, published, or
         sent in response to a query. If this leaseset expires, do not query the
         netdb for a new one.
  Bits 15-2: set to 0 for compatibility with future uses

offline_signature :: `OfflineSignature`
                     length -> varies
                     Optional, only present if bit 0 is set in the flags.

len :: `Integer`
        length -> 2 bytes
        length of encrypted_data to follow
        value: 1 <= num <= max TBD

encrypted_data :: Data encrypted
                  length -> len bytes

signature :: `Signature`
             length -> As specified by the sigtype of the blinded pubic key,
                       or by the sigtype of the transient public key,
                       if present in the header

```
#### Poznámky

* Veřejný klíč destinace byl používán pro staré I2CP-to-I2CP šifrování, které bylo zakázáno ve verzi 0.6, aktuálně se nepoužívá.

* Podpis je nad daty výše, PŘEDŘAZENÝMI s jediným bajtem
  obsahujícím typ DatabaseStore (5).

* Podpis může být ověřen pomocí veřejného podpisového klíče cíle, nebo přechodného podpisového veřejného klíče, pokud je offline podpis zahrnut v hlavičce leaseset2.

* Blinding a šifrování jsou specifikovány v [EncryptedLeaseSet](/docs/specs/encryptedleaseset/)

* Tato struktura nepoužívá [LeaseSet2Header](#leaseset2header).

* Maximální skutečný čas vypršení je přibližně 660 (11 minut), pokud
  se nejedná o šifrovaný [MetaLeaseSet](#metaleaseset).

* Viz návrh 123 pro poznámky k používání offline podpisů
  s šifrovanými leaseSety.

* Viz poznámka k poli 'published' v [LeaseSet2Header](#leaseset2header)
  (stejný problém, i když zde nepoužíváme formát LeaseSet2Header)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/EncryptedLeaseSet.html

### RouterAddress

#### Popis

Tato struktura definuje způsob, jak kontaktovat router prostřednictvím transportního protokolu.

#### Obsah

1 byte [Integer](#integer) definující relativní náklady na použití adresy, kde 0 je zdarma a 255 je drahé, následované datem expirace [Date](#date), po kterém by se adresa neměla používat, nebo pokud je null, adresa nikdy nevyprší. Poté následuje [String](#string) definující transportní protokol, který tato router adresa používá. Nakonec je zde [Mapping](#mapping) obsahující všechny transportně specifické možnosti nezbytné pro navázání spojení, jako je IP adresa, číslo portu, emailová adresa, URL atd.

```
+----+----+----+----+----+----+----+----+
|cost|           expiration
+----+----+----+----+----+----+----+----+
     |        transport_style           |
+----+----+----+----+-/-+----+----+----+
|                                       |
+                                       +
|               options                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

cost :: `Integer`
        length -> 1 byte

        case 0 -> free
        case 255 -> expensive

expiration :: `Date` (must be all zeros, see notes below)
              length -> 8 bytes

              case null -> never expires

transport_style :: `String`
                   length -> 1-256 bytes

options :: `Mapping`
```
#### Poznámky

* Náklady jsou typicky 5 nebo 6 pro SSU a 10 nebo 11 pro NTCP.

* Expiration je v současnosti nepoužíváno, vždy null (samé nuly). Od verze 0.9.3 se předpokládá, že expiration je nulová a neukládá se, takže jakákoli nenulová expiration selže při ověřování podpisu RouterInfo. Implementace expiration (nebo jiné použití těchto bajtů) bude změna nekompatibilní se staršími verzemi. Routery MUSÍ nastavit toto pole na samé nuly. Od verze 0.9.12 je nenulové expiration pole opět rozpoznáváno, musíme však počkat několik verzí, než začneme toto pole používat, dokud ho nebude rozpoznávat naprostá většina sítě.

* Následující možnosti, ačkoli nejsou vyžadovány, jsou standardní a očekává se, že budou přítomny ve většině router adres: "host" (IPv4 nebo IPv6 adresa nebo název hostitele) a "port".

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterAddress.html

### RouterInfo

#### Popis

Definuje všechna data, která chce router publikovat tak, aby je síť mohla vidět. [RouterInfo](#routerinfo) je jedna ze dvou struktur uložených v síťové databázi (druhou je [LeaseSet](#leaseset)) a je indexována pod SHA256 hash obsažené [RouterIdentity](#routeridentity).

#### Obsah

[RouterIdentity](#routeridentity) následovaná [Date](#date), kdy byla položka publikována

```
+----+----+----+----+----+----+----+----+
| router_ident                          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| published                             |
+----+----+----+----+----+----+----+----+
|size| RouterAddress 0                  |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| RouterAddress 1                       |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| RouterAddress ($size-1)               |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+-/-+----+----+----+
|psiz| options                          |
+----+----+----+----+-/-+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+

router_ident :: `RouterIdentity`
                length -> >= 387+ bytes

published :: `Date`
             length -> 8 bytes

size :: `Integer`
        length -> 1 byte
        The number of `RouterAddress`es to follow, 0-255

addresses :: [`RouterAddress`]
             length -> varies

peer_size :: `Integer`
             length -> 1 byte
             The number of peer `Hash`es to follow, 0-255, unused, always zero
             value -> 0

options :: `Mapping`

signature :: `Signature`
             length -> 40 bytes or as specified in router_ident's key
                       certificate
```
#### Poznámky

* Hodnota peer_size [Integer](#integer) může být následována seznamem tolika router hashů.
  Toto se v současnosti nepoužívá. Bylo určeno pro formu omezených tras,
  která není implementována.
  Určité implementace mohou vyžadovat, aby byl seznam seřazen, aby byl podpis invariantní.
  Je třeba to prozkoumat před povolením této funkce.

* Podpis může být ověřen pomocí veřejného klíče pro podepisování z router_ident.

* Viz stránku síťové databáze [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo) pro standardní možnosti, které
  se očekává, že budou přítomny ve všech router infos.

* Velmi staré routery vyžadovaly, aby byly adresy seřazeny podle SHA256 jejich dat,
  takže podpis je invariantní.
  Toto již není vyžadováno a není to hodné implementace kvůli zpětné kompatibilitě.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterInfo.html

### Instrukce pro doručení

Instrukce pro doručení zpráv tunelu jsou definovány ve specifikaci zpráv tunelu [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions).

Instrukce pro doručování Garlic zpráv jsou definovány ve specifikaci I2NP zpráv [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions).

## Reference

- [ECIES](/docs/specs/ecies/)
- [ECIES-HYBRID](/docs/specs/ecies-hybrid/)
- [ECIES-ROUTERS](/docs/specs/ecies-routers/)
- [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy)
- [ELGAMAL-AES](/docs/specs/elgamal-aes/)
- [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions)
- [I2CP](/docs/specs/i2cp/)
- [I2NP](/docs/specs/i2np/)
- [NAMING](/docs/overview/naming/)
- [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo)
- [Prop134](/proposals/134-gost/)
- [Prop169](/proposals/169-pq-crypto/)
- [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
- [SSU](/docs/legacy/ssu/)
- [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions)
