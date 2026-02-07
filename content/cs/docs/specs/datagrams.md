---
title: "Specifikace datagramu"
description: "Specifikace formátů I2P datagram zpráv včetně raw, repliable a authenticated typů"
slug: "datagrams"
category: "Protokoly"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

## Přehled

Viz [dokumentaci Datagrams API](/docs/api/datagrams/) pro přehled Datagrams API.

Jsou definovány následující typy. Jsou uvedena standardní čísla protokolů, avšak mohou být použita jakákoli jiná čísla protokolů kromě čísla streaming protokolu (6), které je specifické pro aplikaci.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Protocol</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Repliable?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Authenticated?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Replay Prevention?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">As Of</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Raw</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
  </tbody>
</table>
Podpora pro Datagram2 a Datagram3 v různých implementacích routerů a knihoven bude teprve určena. Zkontrolujte dokumentaci těchto implementací.

### Identifikace typu datagramu

Čtyři typy datagramů nesdílejí společné záhlaví s verzí protokolu na stejném místě. Pakety nelze identifikovat podle typu na základě jejich obsahu. Při používání více typů na stejné relaci nebo jednoho typu společně se streamováním musí aplikace používat čísla protokolů a/nebo I2CP/SAM porty k směrování příchozích paketů na správné místo. Použití standardních čísel protokolů to usnadní. Ponechání čísla protokolu nenastavené (0 nebo PROTO_ANY), dokonce i pro aplikaci používající pouze datagramy, se nedoporučuje, protože to zvyšuje pravděpodobnost chyb při směrování a ztěžuje to upgrade na multi-protokolovou aplikaci. Pole verzí v Datagram 2 a 3 jsou poskytována pouze jako dodatečná kontrola chyb směrování a budoucích změn.

### Design aplikace

Všechna použití datagramů jsou specifická pro aplikaci.

Protože autentizované datagramy nesou značnou režii, typická aplikace používá jak autentizované, tak neautentizované datagramy. Typický návrh spočívá v odeslání jediného autentizovaného datagramu obsahujícího token z klienta na server. Server odpovídá neautentizovaným datagramem obsahujícím stejný token. Veškerá následná komunikace před vypršením tokenu používá surové datagramy.

Aplikace odesílají a přijímají datagramy pomocí protokolových a portových čísel přes [I2CP](/docs/specs/i2cp/) API nebo [SAMv3](/docs/api/samv3/).

Datagramy jsou samozřejmě nespolehlivé. Aplikace musí počítat s nespolehlivým doručením. V rámci I2P je doručení spolehlivé mezi jednotlivými uzly, pokud je další uzel dosažitelný, protože transporty NTCP2 a SSU2 poskytují spolehlivost. Nicméně end-to-end doručení není spolehlivé, protože I2NP zprávy mohou být zahozeny v kterémkoli uzlu kvůli limitům front, vypršení platnosti, timeoutům, omezením šířky pásma nebo nedostupným dalším uzlům.

### Velikost datagramu

Nominální limit velikosti pro I2NP zprávy, včetně datagramů, je 64 KB. Režie garlic encryption a tunnel zpráv toto omezení poněkud snižuje.

Všechny I2NP zprávy však musí být fragmentovány do 1 KB tunnel zpráv. Pravděpodobnost zahození n KB I2NP zprávy je exponenciální funkcí pravděpodobnosti zahození jediné tunnel zprávy, p ** n. Protože fragmentace má za následek burst tunnel zpráv, skutečná pravděpodobnost zahození je mnohem vyšší, než by implikovala exponenciální funkce, kvůli limitům front a aktivnímu řízení front (AQM, CoDel nebo podobné) v implementacích routerů.

Doporučená typická maximální velikost pro zajištění spolehlivého doručení je několik KB, nebo maximálně 10 KB. S pečlivou analýzou velikostí režie na všech protokolových vrstvách (kromě transportní) by vývojáři měli nastavit maximální velikost payload, která přesně zapadne do jedné, dvou nebo tří tunnel zpráv. To maximalizuje efektivitu a spolehlivost. Režie na různých vrstvách zahrnuje gzip hlavičku, I2NP hlavičku, garlic message hlavičku, garlic encryption, tunnel message hlavičku, hlavičky fragmentace tunnel message a další. Viz výpočty streaming MTU v [Proposal 144](/proposals/144-ecies-x25519-aead-ratchet/) a ConnectionOptions.java ve zdrojovém kódu Java I2P pro příklady.

### Úvahy o SAM

Aplikace odesílají a přijímají datagramy pomocí čísel protokolů a portů přes I2CP API nebo SAM. Specifikace čísel protokolů a portů přes SAM vyžaduje SAM v3.2 nebo vyšší. Používání datagramů i streamingu (UDP a TCP) ve stejné SAM session (tunnelech) vyžaduje SAM v3.3 nebo vyšší. Používání více typů datagramů ve stejné SAM session (tunnelech) vyžaduje SAM v3.3 nebo vyšší. SAM v3.3 je v současné době podporováno pouze Java I2P routerem.

Podpora SAM pro Datagram2 a Datagram3 v různých implementacích routerů a knihoven není zatím určena. Zkontrolujte dokumentaci těchto implementací.

Všimněte si, že velikosti přes typické síťové MTU 1500 bajtů zabrání SAM aplikacím přenášet nefragmentované pakety do/ze SAM serveru, pokud jsou aplikace a server na samostatných počítačích. Typicky to tak není, obě jsou na localhost, kde je MTU 65536 nebo vyšší. Pokud se očekává, že SAM aplikace bude oddělena na jiném počítači od serveru, maximální payload pro odpovědný datagram je mírně pod 1 KB.

### Úvahy o PQ

Pokud bude implementována MLDSA část Post-Quantum [Proposal 169](/proposals/169-pq-crypto/), režie se podstatně zvýší. Velikost destination + podpisu se zvýší z 391 + 64 = 455 bajtů na minimum 3739 pro MLDSA44 a maximum 7226 pro MLDSA87. Praktické dopady toho je třeba ještě určit. Datagram3 s autentizací poskytovanou routerem může být řešením.

## Surové (neodpověditelné) datagramy {#raw}

Neopakovatelné datagramy nemají žádnou adresu 'from' a nejsou autentizované. Nazývají se také "raw" datagramy. Přísně vzato, nejsou to vůbec "datagramy", jsou to jen surová data. Nejsou zpracovávány datagram API. Nicméně SAM a třídy I2PTunnel podporují "raw datagramy".

Standardní číslo I2CP protokolu pro surové datagramy je PROTO_DATAGRAM_RAW (18).

Formát zde není specifikován, je definován aplikací. Pro úplnost níže uvádíme obrázek formátu.

### Formát

```
+----+----+----+----+----//
| payload...
+----+----+----+----+----//

length: 0 - about 64 KB (see notes)
```
### Poznámky

Praktická délka je omezena jak režií na různých vrstvách, tak spolehlivostí.

## Datagram1 (Zodpověditelný) {#repliable}

Repliable datagramy obsahují adresu 'from' a podpis. Tyto přidávají nejméně 427 bajtů režie.

Standardní číslo I2CP protokolu pro odpověditelné datagramy je PROTO_DATAGRAM (17).

### Formát

```
+----+----+----+----+----+----+----+----+
| from                                  |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+                                       +
|                                       |
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
| payload...
+----+----+----+----//

from :: a Destination
        length: 387+ bytes
        The originator and signer of the datagram

signature :: a Signature
             Signature type must match the signing public key type of $from
             length: 40+ bytes, as implied by the Signature type.
             For the default DSA_SHA1 key type:
                The DSA Signature of the SHA-256 hash of the payload.
             For other key types:
                The Signature of the payload.
             The signature may be verified by the signing public key of $from

payload :: The data
           Length: 0 to about 63 KB (see notes)

Total length: Payload length + 427+
```
### Poznámky

- Praktická délka je omezena jak režií na různých vrstvách, tak spolehlivostí.
- Podívejte se na důležité poznámky o spolehlivosti velkých datagramů v [dokumentaci Datagrams API](/docs/api/datagrams/). Pro nejlepší výsledky omezte payload na přibližně 10 KB nebo méně.
- Podpisy pro typy jiné než DSA_SHA1 byly předefinovány ve verzi 0.9.14.
- Formát nepodporuje zahrnutí offline signature bloku pro LS2 (návrh 123). Pro to musí být definován nový protokol s příznaky.

## Datagram2 {#datagram2}

Formát Datagram2 je specifikován v [Návrhu 163](/proposals/163-datagram2/). Číslo protokolu I2CP pro Datagram2 je 19.

Datagram2 je zamýšlen jako náhrada za Datagram1. Přidává k Datagram1 následující funkce:

- Prevence opakování útoků
- Podpora offline podpisů
- Pole příznaků a možností pro rozšiřitelnost

Všimněte si, že algoritmus výpočtu podpisu pro Datagram2 se podstatně liší od algoritmu pro Datagram1.

### Formát

```
+----+----+----+----+----+----+----+----+
|                                       |
~            from                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~     offline_signature (optional)      ~
~   expires, sigtype, pubkey, offsig    ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            signature                  ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

from :: a Destination
        length: 387+ bytes
        The originator and (unless offline signed) signer of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x02 (0 0 1 0)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bit 5: If 0, no offline sig; if 1, offline signed
         Bits 15-6: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

offline_signature ::
             If flag indicates offline keys, the offline signature section,
             as specified in the Common Structures Specification,
             with the following 4 fields. Length: varies by online and offline
             sig types, typically 102 bytes for Ed25519
             This section can, and should, be generated offline.

  expires :: Expires timestamp
             (4 bytes, big endian, seconds since epoch, rolls over in 2106)

  sigtype :: Transient sig type (2 bytes, big endian)

  pubkey :: Transient signing public key (length as implied by sig type),
            typically 32 bytes for Ed25519 sig type.

  offsig :: a Signature
            Signature of expires timestamp, transient sig type,
            and public key, by the destination public key,
            length: 40+ bytes, as implied by the Signature type, typically
            64 bytes for Ed25519 sig type.

payload :: The data
           Length: 0 to about 61 KB (see notes)

signature :: a Signature
             Signature type must match the signing public key type of $from
             (if no offline signature) or the transient sigtype
             (if offline signed)
             length: 40+ bytes, as implied by the Signature type, typically
             64 bytes for Ed25519 sig type.
             The Signature of the payload and other fields as specified below.
             The signature is verified by the signing public key of $from
             (if no offline signature) or the transient pubkey
             (if offline signed)
```
Celková délka: minimálně 433 + délka payloadu; typická délka pro X25519 odesílatele a bez offline podpisů: 457 + délka payloadu. Všimněte si, že zpráva bude typicky komprimována pomocí gzip na I2CP vrstvě, což povede k významným úsporám, pokud je zdrojová destinace komprimovatelná.

Poznámka: Formát offline podpisu je stejný jako ve [Specifikaci společných struktur](/docs/specs/common-structures/) a [Specifikaci streamování](/docs/specs/streaming/).

### Podpisy

Podpis se vztahuje na následující pole:

- Prelude: 32-bajtový hash cílové destinace (není zahrnut v datagramu)
- flags
- options (pokud jsou přítomny)
- offline_signature (pokud je přítomen)
- payload

V odpověditelném datagramu bylo u typu klíče DSA_SHA1 podepsán SHA-256 hash užitečného obsahu, nikoli užitečný obsah samotný; zde je podpis vždy nad výše uvedenými poli (NIKOLI nad hashem), bez ohledu na typ klíče.

### Ověření ToHash

Příjemci musí ověřit podpis (pomocí svého destination hash) a při selhání datagram zahodit, aby se zabránilo replay útokům.

## Datagram3 {#datagram3}

Formát Datagram3 je specifikován podle [Návrhu 163](/proposals/163-datagram2/). Číslo protokolu I2CP pro Datagram3 je 20.

Datagram3 je zamýšlen jako vylepšená verze raw datagramů. Přidává následující funkce k raw datagramům:

- Replikovatelnost
- Pole pro příznaky a možnosti pro rozšiřitelnost

Datagram3 NENÍ ověřen. V budoucím návrhu může být ověření poskytováno ratchet vrstvou routeru a stav ověření by byl předán klientovi.

### Formát

```
+----+----+----+----+----+----+----+----+
|                                       |
~            fromhash                   ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

fromhash :: a Hash
            length: 32 bytes
            The originator of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x03 (0 0 1 1)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bits 15-5: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

payload :: The data
           Length: 0 to about 61 KB (see notes)
```
Celková délka: minimálně 34 + délka dat.

## Reference

- [Common](/docs/specs/common-structures/) - Specifikace společných struktur
- [DATAGRAMS](/docs/api/datagrams/) - Přehled API datagramů
- [I2CP](/docs/specs/i2cp/) - Specifikace I2CP
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet/) - Návrh ECIES-X25519-AEAD-Ratchet
- [Prop163](/proposals/163-datagram2/) - Návrh Datagram2 a Datagram3
- [Prop169](/proposals/169-pq-crypto/) - Návrh post-kvantové kryptografie
- [SAMv3](/docs/api/samv3/) - Specifikace SAM v3
- [Streaming](/docs/specs/streaming/) - Specifikace streamování
- [TRANSPORT](/docs/overview/transport/) - Přehled transportu
- [TUNMSG](/docs/specs/tunnel-message/#notes) - Specifikace tunnel zpráv
