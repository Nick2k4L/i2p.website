---
title: "ECIES-X25519-AEAD-Ratchet"
aliases:
  - "/cs/proposals/144-ecies-x25519"
  - "/cs/proposals/144-ecies-x25519/"
number: "144"
author: "zzz, chisana, orignal"
created: "2018-11-22"
lastupdated: "2025-03-05"
status: "Zavřeno"
thread: "http://zzz.i2p/topics/2639"
target: "0.9.46"
implementedin: "0.9.46"
toc: true
---
## Poznámka
Nasazení sítě a testování probíhají.
Předmět menších revizí.
Viz [SPEC](/docs/specs/ecies/) pro oficiální specifikaci.

Následující funkce nejsou implementovány ve verzi 0.9.46:

- Bloky MessageNumbers, Options a Termination
- Odpovědi na úrovni protokolu
- Nulový statický klíč
- Multicast


## Přehled

Toto je návrh prvního nového typu end-to-end šifrování
od počátku I2P, který nahradí ElGamal/AES+SessionTags [Elg-AES](/docs/specs/elgamal-aes/).

Spoléhá na předchozí práci následovně:

- Společné struktury spec [Common Structures](/docs/specs/common-structures/)
- [I2NP](/docs/specs/i2np/) spec včetně LS2
- ElGamal/AES+Session Tags [Elg-AES](/docs/specs/elgamal-aes/)
- [http://zzz.i2p/topics/1768](http://zzz.i2p/topics/1768) přehled nové asymetrické kryptografie
- Přehled nízkoúrovňové kryptografie [CRYPTO-ELG](/docs/specs/cryptography/)
- ECIES [http://zzz.i2p/topics/2418](http://zzz.i2p/topics/2418)
- [NTCP2](/docs/specs/ntcp2/) [Proposal 111](/proposals/111-ntcp-2/)
- 123 Nové záznamy v netDB
- 142 Nová šablona kryptografie
- [Noise](https://noiseprotocol.org/noise.html) protokol
- [Signal](https://signal.org/docs/) algoritmus dvojitého klikačky

Cílem je podpora nového šifrování pro end-to-end,
komunikaci z cíle do cíle.

Návrh použije handshake a datovou fázi Noise s využitím dvojitého klikačky z Signal.

Všechny odkazy na Signal a Noise v tomto návrhu jsou pouze pro informační účely.
K pochopení nebo implementaci tohoto návrhu není nutné znát protokoly Signal a Noise.


### Současné použití ElGamalu

Jako připomenutí,
veřejné klíče ElGamal o délce 256 bajtů lze nalézt v následujících datových strukturách.
Viz specifikace společných struktur.

- V identitě směrovače
  Toto je šifrovací klíč směrovače.

- V cíli
  Veřejný klíč cíle byl použit pro staré šifrování i2cp-to-i2cp,
  které bylo zakázáno ve verzi 0.6, aktuálně se nepoužívá kromě
  IV pro šifrování LeaseSet, což je zastaralé.
  Místo toho se používá veřejný klíč v LeaseSet.

- V LeaseSet
  Toto je šifrovací klíč cíle.

- V LS2
  Toto je šifrovací klíč cíle.



### EncTypes v klíčových certifikátech

Jako připomenutí,
přidali jsme podporu pro typy šifrování, když jsme přidali podporu pro typy podpisů.
Pole typu šifrování je vždy nula, jak v Cílech, tak v RouterIdentities.
Zda to někdy změnit, je zatím nevyřízeno.
Viz specifikace společných struktur [Common Structures](/docs/specs/common-structures/).




### Použití asymetrické kryptografie

Jako připomenutí, používáme ElGamal pro:

1) Zprávy pro stavbu tunelu (klíč je v RouterIdentity)
   Nahrazení není pokryto tímto návrhem.
   Viz návrh 152 [Proposal 152](/proposals/152-ecies-tunnels).

2) Šifrování mezi směrovači pro netdb a další zprávy I2NP (Klíč je v RouterIdentity)
   Závisí na tomto návrhu.
   Vyžaduje návrh pro 1) nebo vložení klíče do možností RI.

3) Klientské End-to-end ElGamal+AES/SessionTag (klíč je v LeaseSet, klíč Cíle se nepoužívá)
   Nahrazení JE pokryto tímto návrhem.

4) Dočasné DH pro NTCP1 a SSU
   Nahrazení není pokryto tímto návrhem.
   Viz návrh 111 pro NTCP2.
   Pro SSU2 zatím neexistuje žádný návrh.


### Cíle

- Zpětná kompatibilita
- Vyžaduje a staví na LS2 (návrh 123)
- Využívá novou kryptografii nebo primitiva přidaná pro NTCP2 (návrh 111)
- Nevyžaduje žádnou novou kryptografii nebo primitiva pro podporu
- Zachovává oddělení kryptografie a podepisování; podpora všech současných a budoucích verzí
- Povolí novou kryptografii pro cíle
- Povolí novou kryptografii pro směrovače, ale pouze pro česnekové zprávy - stavba tunelu by
  byla samostatným návrhem
- Neporušuje nic, co závisí na 32bitových binárních hashích cílů, např. bittorrent
- Zachovává doručování zpráv 0-RTT pomocí dočasné-statické DH
- Nevyžaduje ukládání/zálohování zpráv na této úrovni protokolu;
  pokračuje v podpoře neomezeného doručování zpráv v obou směrech bez čekání na odpověď
- Upgrade na dočasnou-dočasnou DH po 1 RTT
- Zachovává zpracování zpráv mimo pořadí
- Zachovává 256bitovou bezpečnost
- Přidává forward secrecy
- Přidává autentizaci (AEAD)
- Mnohem efektivnější CPU než ElGamal
- Nezávisí na Java jbigi pro efektivní DH
- Minimalizuje operace DH
- Mnohem efektivnější šířka pásma než ElGamal (514 bajtový blok ElGamal)
- Podpora nové a staré kryptografie na stejném tunelu, pokud je to žádoucí
- Příjemce je schopen efektivně rozlišit novou od staré kryptografie přicházející
  stejným tunelem
- Ostatní nemohou rozlišit novou od staré nebo budoucí kryptografie
- Odstraní klasifikaci délky nové vs. existující relace (podpora paddingu)
- Nevyžaduje žádné nové zprávy I2NP
- Nahradí kontrolní součet SHA-256 v datové části AES za AEAD
- Podpora vazby přenosových a přijímacích relací, aby
  potvrzení mohla probíhat v rámci protokolu, nikoli pouze mimo pásmo.
  To také umožní, aby odpovědi měly okamžitou forward secrecy.
- Povolí end-to-end šifrování určitých zpráv (ukládání RouterInfo),
  které aktuálně nešifrujeme kvůli výpočetnímu výkonu.
- Nezmění I2NP Garlic Message
  ani formát Garlic Message Delivery Instructions.
- Odstraní nepoužívaná nebo redundantní pole ve formátech Garlic Clove Set a Clove.

Odstraňuje několik problémů se session tagy, včetně:

- Nelze použít AES, dokud nepřijde první odpověď
- Nespolehlivost a zasekávání, pokud se předpokládá doručení tagu
- Neefektivní šířka pásma, zejména při prvním doručení
- Obrovská neefektivita prostoru pro ukládání tagů
- Obrovský režijní výdaj šířky pásma pro doručení tagů
- Vysoce složité, obtížné implementovat
- Obtížné ladit pro různé případy použití
  (streaming vs. datagramy, server vs. klient, vysoká vs. nízká šířka pásma)
- Zranitelnosti vyčerpání paměti kvůli doručování tagů


### Není cílem / mimo rozsah

- Změny formátu LS2 (návrh 123 je hotov)
- Nový algoritmus rotace DHT nebo generování sdíleného náhodného čísla
- Nové šifrování pro stavbu tunelu.
  Viz návrh 152 [Proposal 152](/proposals/152-ecies-tunnels).
- Nové šifrování pro šifrování vrstvy tunelu.
  Viz návrh 153 [Proposal 153](/proposals/153-chacha20-layer-encryption).
- Metody šifrování, přenosu a příjmu zpráv I2NP DLM / DSM / DSRM.
  Nezmění se.
- Komunikace LS1-to-LS2 nebo ElGamal/AES-to-tento-návrh není podporována.
  Tento návrh je obousměrný protokol.
  Cíle mohou zpracovat zpětnou kompatibilitu publikováním dvou leasesetů
  pomocí stejných tunelů, nebo vložením obou typů šifrování do LS2.
- Změny modelu hrozeb
- Podrobnosti implementace zde nejsou diskutovány a jsou ponechány každému projektu.
- (Optimistické) Přidání rozšíření nebo háků pro podporu multicastu



### Odůvodnění

ElGamal/AES+SessionTag byl naším jediným end-to-end protokolem po dobu asi 15 let,
v podstatě bez úprav protokolu.
Nyní existují kryptografické primitiva, která jsou rychlejší.
Musíme zvýšit bezpečnost protokolu.
Vyvinuli jsme také heuristické strategie a workarounds pro minimalizaci
výdajů paměti a šířky pásma protokolu, ale tyto strategie
jsou křehké, obtížné ladit a činí protokol ještě náchylnějším
k selhání, což způsobuje odpojení relace.

Po stejné období specifikace ElGamal/AES+SessionTag a související
dokumentace popisují, jak nákladné je doručování session tagů,
a navrhují nahradit doručování session tagů „synchronizovaným PRNG“.
Synchronizovaný PRNG deterministicky generuje stejné tagy na obou koncích,
odvozené z běžného semínka.
Synchronizovaný PRNG lze také označit jako „klikačku“.
Tento návrh (konečně) specifikuje tento mechanismus klikačky a eliminuje doručování tagů.

Použitím klikačky (synchronizovaného PRNG) k generování
session tagů eliminujeme režii odesílání session tagů
ve zprávě New Session a následných zprávách, když je to potřeba.
Pro typickou sadu tagů 32 tagů je to 1 KB.
To také eliminuje ukládání session tagů na odesílací straně,
čímž se nároky na úložiště sníží na polovinu.

Plný obousměrný handshake, podobný vzoru Noise IK, je potřeba k vyhnutí se útokům Key Compromise Impersonation (KCI).
Viz tabulka „Vlastnosti zabezpečení datové části“ v [NOISE](https://noiseprotocol.org/noise.html).
Další informace o KCI naleznete v článku https://www.usenix.org/system/files/conference/woot15/woot15-paper-hlauschek.pdf



### Model hrozeb

Model hrozeb je poněkud odlišný než pro NTCP2 (návrh 111).
Uzly MitM jsou OBEP a IBGW a předpokládá se, že mají plný přehled o
současném nebo historickém globálním NetDB, spolupracující s floodfill uzly.

Cílem je zabránit těmto MitM v klasifikaci provozu jako
nové a existující zprávy relace, nebo jako nová kryptografie vs. stará kryptografie.



## Podrobný návrh

Tento návrh definuje nový end-to-end protokol k nahrazení ElGamal/AES+SessionTags.
Návrh použije handshake a datovou fázi Noise s využitím dvojitého klikačky z Signal.


### Shrnutí kryptografického návrhu

Existuje pět částí protokolu, které mají být přepracovány:


- 1) Formáty kontejneru nové a existující relace
  jsou nahrazeny novými formáty.
- 2) ElGamal (256 bajtové veřejné klíče, 128 bajtové soukromé klíče) bude nahrazen
  ECIES-X25519 (32 bajtové veřejné a soukromé klíče)
- 3) AES bude nahrazeno
  AEAD_ChaCha20_Poly1305 (dále označováno jako ChaChaPoly)
- 4) SessionTags budou nahrazeny klikačkami,
  což je v podstatě kryptografický, synchronizovaný PRNG.
- 5) Datová část AES, jak je definována ve specifikaci ElGamal/AES+SessionTags,
  je nahrazena blokovým formátem podobným tomu v NTCP2.

Každá z pěti změn má svou vlastní sekci níže.


### Nové kryptografické primitiva pro I2P

Existující implementace směrovače I2P budou vyžadovat implementace
následujících standardních kryptografických primitiv,
která nejsou vyžadována pro současné protokoly I2P:

- ECIES (ale to je v podstatě X25519)
- Elligator2

Existující implementace směrovače I2P, které ještě neimplementovaly [NTCP2](/docs/specs/ntcp2/) ([Proposal 111](/proposals/111-ntcp-2/))
budou také vyžadovat implementace pro:

- Generování klíčů X25519 a DH
- AEAD_ChaCha20_Poly1305 (dále označováno jako ChaChaPoly)
- HKDF


### Typ kryptografie

Typ kryptografie (používaný v LS2) je 4.
To označuje little-endian 32bajtový veřejný klíč X25519,
a end-to-end protokol zde specifikovaný.

Typ kryptografie 0 je ElGamal.
Typy kryptografie 1-3 jsou vyhrazeny pro ECIES-ECDH-AES-SessionTag, viz návrh 145 [Proposal 145](/proposals/145-ecies).


### Rámec protokolu Noise

Tento návrh poskytuje požadavky založené na Rámci protokolu Noise
[NOISE](https://noiseprotocol.org/noise.html) (Revize 34, 2018-07-11).
Noise má podobné vlastnosti jako protokol Station-To-Station
[STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol), který je základem pro protokol [SSU](/docs/legacy/ssu/).  V terminologii Noise
je Alice iniciátor a Bob odpovídač.

Tento návrh je založen na protokolu Noise Noise_IK_25519_ChaChaPoly_SHA256.
(Skutečný identifikátor pro počáteční funkci odvození klíče
je „Noise_IKelg2_25519_ChaChaPoly_SHA256“
k označení rozšíření I2P - viz sekce KDF 1 níže)
Tento protokol Noise používá následující primitiva:

- Interaktivní vzor handshake: IK
  Alice okamžitě přenáší svůj statický klíč Bobovi (I)
  Alice již zná Bobův statický klíč (K)

- Jednosměrný vzor handshake: N
  Alice nepřenáší svůj statický klíč Bobovi (N)

- Funkce DH: X25519
  X25519 DH s délkou klíče 32 bajtů, jak je specifikováno v [RFC-7748](https://tools.ietf.org/html/rfc7748).

- Funkce šifry: ChaChaPoly
  AEAD_CHACHA20_POLY1305 jak je specifikováno v [RFC-7539](https://tools.ietf.org/html/rfc7539) sekce 2.8.
  12 bajtový nonce, s prvními 4 bajty nastavenými na nulu.
  Identické s tím v [NTCP2](/docs/specs/ntcp2/).

- Funkce hash: SHA256
  Standardní 32bajtový hash, již široce používaný v I2P.


### Přídavky k rámci

Tento návrh definuje následující vylepšení pro
Noise_IK_25519_ChaChaPoly_SHA256.  Ty obecně následují pokyny v
[NOISE](https://noiseprotocol.org/noise.html) sekce 13.

1) Veřejné dočasné klíče jsou kódovány pomocí [Elligator2](https://elligator.cr.yp.to/).

2) Odpověď je předřazena čitelným tagem.

3) Formát datové části je definován pro zprávy 1, 2 a datovou fázi.
   Samozřejmě, to není definováno v Noise.

Všechny zprávy zahrnují hlavičku [I2NP](/docs/specs/i2np/) Garlic Message.
Datová fáze používá šifrování podobné, ale nekompatibilní s datovou fází Noise.


### Vzory handshake

Handshake používají [Noise](https://noiseprotocol.org/noise.html) vzory handshake.

Používá se následující mapování písmen:

- e = jednorázový dočasný klíč
- s = statický klíč
- p = datová část zprávy

Jednorázové a nevázané relace jsou podobné vzoru Noise N.

```

<- s
  ...
  e es p ->

```

Vázané relace jsou podobné vzoru Noise IK.

```

<- s
  ...
  e es s ss p ->
  <- tag e ee se
  <- p
  p ->

```


### Relace

Současný protokol ElGamal/AES+SessionTag je jednosměrný.
Na této úrovni příjemce neví, odkud zpráva pochází.
Odchozí a příchozí relace nejsou spojeny.
Potvrzení jsou mimo pásmo pomocí DeliveryStatusMessage
(zabalené v GarlicMessage) v kloboučku.

Existuje významná neefektivita jednosměrného protokolu.
Jakákoli odpověď musí také použít nákladnou zprávu 'New Session'.
To způsobuje vyšší šířku pásma, CPU a využití paměti.

Existují také bezpečnostní slabiny jednosměrného protokolu.
Všechny relace jsou založeny na dočasné-statické DH.
Bez návratové cesty nemá Bob žádný způsob, jak „kliknout“ svůj statický klíč
na dočasný klíč.
Bez vědomí, odkud zpráva pochází, není způsob, jak použít
přijatý dočasný klíč pro odchozí zprávy,
takže počáteční odpověď také používá dočasnou-statickou DH.

Pro tento návrh definujeme dva mechanismy pro vytvoření obousměrného protokolu -
„spárování“ a „vázání“.
Tyto mechanismy poskytují zvýšenou efektivitu a bezpečnost.


### Kontext relace

Stejně jako u ElGamal/AES+SessionTags, všechny příchozí a odchozí relace
musí být v daném kontextu, buď v kontextu směrovače nebo
v kontextu pro konkrétní místní cíl.
V Java I2P se tento kontext nazývá Session Key Manager.

Relace nesmí být sdíleny mezi kontexty, protože by to
umožnilo korelaci mezi různými místními cíli,
nebo mezi místním cílem a směrovačem.

Když daný cíl podporuje jak ElGamal/AES+SessionTags,
tak tento návrh, mohou oba typy relací sdílet kontext.
Viz sekce 1c) níže.



### Spárování příchozích a odchozích relací

Když je vytvořena odchozí relace u iniciátora (Alice),
je vytvořena nová příchozí relace a spárována s odchozí relací,
pokud není očekávána odpověď (např. raw datagramy).

Nová příchozí relace je vždy spárována s novou odchozí relací,
pokud není požadována odpověď (např. raw datagramy).

Pokud je požadována odpověď a vázána na vzdálený cíl nebo směrovač,
tato nová odchozí relace je vázána na tento cíl nebo směrovač,
a nahrazuje všechny předchozí odchozí relace k tomuto cíli nebo směrovači.

Spárování příchozích a odchozích relací poskytuje obousměrný protokol
s možností klikání klíčů DH.



### Vázání relací a cílů

K danému cíli nebo směrovači existuje pouze jedna odchozí relace.
Může existovat několik aktuálních příchozích relací od daného cíle nebo směrovače.
Obecně, když je vytvořena nová příchozí relace a přijata je na ní
doprava (což slouží jako potvrzení), ostatní budou označeny
k vypršení relativně rychle, během minuty nebo tak.
Hodnota předchozích odeslaných (PN) je zkontrolována a pokud nejsou
neodebrané zprávy (v rámci velikosti okna) v předchozí příchozí relaci,
předchozí relace může být okamžitě smazána.


Když je vytvořena odchozí relace u iniciátora (Alice),
je vázána na vzdálený cíl (Bob),
a jakákoli spárovaná příchozí relace bude také vázána na vzdálený cíl.
Jak relace klikají, zůstávají vázány na vzdálený cíl.

Když je vytvořena příchozí relace u příjemce (Bob),
může být vázána na vzdálený cíl (Alice), na Alicinu volbu.
Pokud Alice zahrne informace o vazbě (její statický klíč) ve zprávě New Session,
relace bude vázána na tento cíl,
a bude vytvořena odchozí relace a vázána na stejný cíl.
Jak relace klikají, zůstávají vázány na vzdálený cíl.


### Výhody vazby a spárování

Pro běžný, streamovací případ očekáváme, že Alice a Bob použijí protokol následovně:

- Alice spáruje svou novou odchozí relaci s novou příchozí relací, obě vázané na vzdálený cíl (Bob).
- Alice zahrne informace o vazbě a podpis, a požadavek na odpověď, ve
  zprávě New Session odeslané Bobovi.
- Bob spáruje svou novou příchozí relaci s novou odchozí relací, obě vázané na vzdálený cíl (Alice).
- Bob pošle odpověď (potvrzení) Alici ve spárované relaci, s kliknutím na nový klíč DH.
- Alice klikne na novou odchozí relaci s Bobovým novým klíčem, spárovanou s existující příchozí relací.

Vazbou příchozí relace na vzdálený cíl a spárováním příchozí relace
s odchozí relací vázanou na stejný cíl dosáhneme dvou hlavních výhod:

1) Počáteční odpověď od Boba k Alici používá dočasnou-dočasnou DH

2) Po přijetí odpovědi Boba a kliknutí Alicí, všechny následující zprávy od Alice k Bobovi
používají dočasnou-dočasnou DH.


### Potvrzení zpráv

V ElGamal/AES+SessionTags, když je LeaseSet zabalen jako česnekový klobouček,
nebo jsou doručeny tagy, požaduje odesílací směrovač potvrzení.
Toto je samostatný česnekový klobouček obsahující zprávu DeliveryStatus Message.
Pro další bezpečnost je zpráva DeliveryStatus Message zabalená v Garlic Message.
Tento mechanismus je mimo pásmo z pohledu protokolu.

V novém protokolu, protože jsou příchozí a odchozí relace spárovány,
můžeme mít potvrzení v pásmu. Samostatný klobouček není vyžadován.

Explicitní potvrzení je jednoduše zpráva Existing Session bez bloku I2NP.
Nicméně, ve většině případů lze explicitní potvrzení vyhnout, protože existuje zpětný provoz.
Může být žádoucí, aby implementace počkala krátkou dobu (možná stovku ms)
před odesláním explicitního potvrzení, aby dala čas vrstvě streamování nebo aplikace na reakci.

Implementace budou také muset odložit jakékoli odesílání potvrzení až po
zpracování bloku I2NP, protože Garlic Message může obsahovat zprávu Database Store Message
s leasesetem. Nedávný leaseset bude nutný k směrování potvrzení,
a vzdálený cíl (obsažený v leasesetu) bude nutný k
ověření vazby statického klíče.


### Časové limity relace

Odchozí relace by měly vždy vypršet před příchozími relacemi.
Jakmile vyprší odchozí relace a je vytvořena nová, bude vytvořena také nová spárovaná příchozí
relace. Pokud existovala stará příchozí relace,
bude jí umožněno vypršet.


### Multicast

TBD


### Definice
Definujeme následující funkce odpovídající použitým kryptografickým stavebním blokům.

ZEROLEN
    pole bajtů nulové délky

CSRNG(n)
    výstup n bajtů z kryptograficky bezpečného generátoru náhodných čísel.

H(p, d)
    funkce hash SHA-256, která bere osobní řetězec p a data d a
    vytváří výstup o délce 32 bajtů.
    Jak je definováno v [NOISE](https://noiseprotocol.org/noise.html).
    || níže znamená připojení.

    Použijte SHA-256 následovně::

        H(p, d) := SHA-256(p || d)

MixHash(d)
    funkce hash SHA-256, která bere předchozí hash h a nová data d,
    a vytváří výstup o délce 32 bajtů.
    || níže znamená připojení.

    Použijte SHA-256 následovně::

        MixHash(d) := h = SHA-256(h || d)

STREAM
    ChaCha20/Poly1305 AEAD jak je specifikováno v [RFC-7539](https://tools.ietf.org/html/rfc7539).
    S_KEY_LEN = 32 a S_IV_LEN = 12.

    ENCRYPT(k, n, plaintext, ad)
        Šifruje plaintext pomocí šifrovacího klíče k a nonce n, který MUSÍ být jedinečný pro
        klíč k.
        Přidružená data ad jsou volitelná.
        Vrací šifrovou text o velikosti plaintext + 16 bajtů pro HMAC.

        Celý šifrový text musí být nerozlišitelný od náhodného, pokud je klíč tajný.

    DECRYPT(k, n, ciphertext, ad)
        Dešifruje šifrový text pomocí šifrovacího klíče k a nonce n.
        Přidružená data ad jsou volitelná.
        Vrací plaintext.

DH
    X25519 systém dohody o veřejném klíči. Soukromé klíče o délce 32 bajtů, veřejné klíče o délce 32
    bajtů, vytváří výstupy o délce 32 bajtů. Má následující
    funkce:

    GENERATE_PRIVATE()
        Generuje nový soukromý klíč.

    DERIVE_PUBLIC(privkey)
        Vrací veřejný klíč odpovídající danému soukromému klíči.

    GENERATE_PRIVATE_ELG2()
        Generuje nový soukromý klíč, který se mapuje na veřejný klíč vhodný pro kódování Elligator2.
        Všimněte si, že polovina náhodně generovaných soukromých klíčů nebude vhodná a musí být zahozena.

    ENCODE_ELG2(pubkey)
        Vrací veřejný klíč kódovaný Elligator2 odpovídající danému veřejnému klíči (inverzní mapování).
        Zakódované klíče jsou little endian.
        Zakódovaný klíč musí být 256 bitů nerozlišitelných od náhodných dat.
        Viz sekce Elligator2 níže pro specifikaci.

    DECODE_ELG2(pubkey)
        Vrací veřejný klíč odpovídající danému veřejnému klíči zakódovanému Elligator2.
        Viz sekce Elligator2 níže pro specifikaci.

    DH(privkey, pubkey)
        Generuje sdílený tajný klíč z daného soukromého a veřejného klíče.

HKDF(salt, ikm, info, n)
    Kryptografická funkce odvození klíče, která bere vstupní materiál klíče ikm (který
    by měl mít dobrý entropii, ale není vyžadováno, aby byl rovnoměrně náhodný řetězec), sůl
    o délce 32 bajtů a kontextově specifickou hodnotu 'info' a vytváří výstup
    o n bajtech vhodných pro použití jako materiál klíče.

    Použijte HKDF jak je specifikováno v [RFC-5869](https://tools.ietf.org/html/rfc5869), použitím funkce hash HMAC SHA-256
    jak je specifikováno v [RFC-2104](https://tools.ietf.org/html/rfc2104). To znamená, že SALT_LEN je maximálně 32 bajtů.

MixKey(d)
    Použijte HKDF() s předchozím chainKey a novými daty d a
    nastavte nový chainKey a k.
    Jak je definováno v [NOISE](https://noiseprotocol.org/noise.html).

    Použijte HKDF následovně::

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]



### 1) Formát zprávy


### Přehled současného formátu zprávy

Garlic Message jak je specifikováno v [I2NP](/docs/specs/i2np/) je následující.
Jako cíl návrhu je, že mezilehlé skoky nemohou rozlišit novou od staré kryptografie,
tento formát se nemůže změnit, i když je pole délky redundantní.
Formát je zobrazen s plnou 16bajtovou hlavičkou, i když
skutečná hlavička může být v jiném formátu, v závislosti na použitém přenosu.

Po dešifrování obsahuje data sérii Garlic Cloves a dalších
dat, také známých jako Clove Set.

Viz [I2NP](/docs/specs/i2np/) pro podrobnosti a úplnou specifikaci.


```

+----+----+----+----+----+----+----+----+
  |type|      msg_id       |  expiration
  +----+----+----+----+----+----+----+----+
                           |  size   |chks|
  +----+----+----+----+----+----+----+----+
  |      length       |                   |
  +----+----+----+----+                   +
  |          encrypted data               |
  ~                                       ~
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

```


### Přehled formátu šifrovaných dat

Současný formát zprávy, používaný více než 15 let,
je ElGamal/AES+SessionTags.
V ElGamal/AES+SessionTags existují dva formáty zpráv:

1) Nová relace:
- 514 bajtový blok ElGamal
- Blok AES (minimálně 128 bajtů, násobek 16)

2) Existující relace:
- 32 bajtový Session Tag
- Blok AES (minimálně 128 bajtů, násobek 16)

Minimální doplnění na 128 je implementováno v Java I2P, ale není vynuceno při příjmu.

Tyto zprávy jsou zabalené v I2NP česnekové zprávě, která obsahuje
pole délky, takže délka je známá.

Všimněte si, že není definováno doplnění na délku, která není mod 16,
takže Nová relace je vždy (mod 16 == 2),
a Existující relace je vždy (mod 16 == 0).
Musíme to opravit.

Příjemce nejprve pokusí vyhledat prvních 32 bajtů jako Session Tag.
Pokud nalezeno, dešifruje blok AES.
Pokud nenalezeno a data jsou alespoň (514+16) dlouhá, pokusí se dešifrovat blok ElGamal,
a pokud úspěšné, dešifruje blok AES.


### Nové Session Tags a srovnání se Signal

V Signal Double Ratchet obsahuje hlavička:

- DH: Aktuální veřejný klíč klikačky
- PN: Délka předchozího řetězce zpráv
- N: Číslo zprávy

„Odesílací řetězce“ Signal jsou hrubě ekvivalentní našim sadám tagů.
Použitím session tagu můžeme eliminovat většinu toho.

V Nové relaci vkládáme pouze veřejný klíč do nešifrované hlavičky.

V Existující relaci používáme session tag pro hlavičku.
Session tag je spojen s aktuálním veřejným klíčem klikačky,
a číslem zprávy.

V obou nových a existujících relacích jsou PN a N v šifrovaném těle.

V Signal se věci neustále kličkují. Nový veřejný klíč DH vyžaduje, aby příjemce klikl a poslal zpět nový veřejný klíč, což také slouží
jako potvrzení přijatého veřejného klíče.
To by pro nás bylo příliš mnoho operací DH.
Takže oddělujeme potvrzení přijatého klíče a přenos nového veřejného klíče.
Jakákoli zpráva používající session tag generovaný z nového veřejného klíče DH tvoří potvrzení.
Nový veřejný klíč posíláme pouze, když chceme změnit klíč.

Maximální počet zpráv před tím, než musí DH kliknout, je 65535.

Při doručování session klíče odvozujeme „Tag Set“ z něj,
místo toho, aby bylo nutné doručovat session tagy také.
Sada tagů může mít až 65536 tagů.
Příjemci by však měli implementovat „strategii náskoku“,
místo generování všech možných tagů najednou.
Vygenerujte maximálně N tagů za posledním dobrým přijatým tagem.
N může být maximálně 128, ale 32 nebo dokonce méně může být lepší volbou.



### 1a) Formát nové relace

Nový jednorázový veřejný klíč relace (32 bajtů)
Šifrovaná data a MAC (zbývající bajty)

Zpráva Nové relace může nebo nemusí obsahovat veřejný klíč odesílatele.
Pokud je zahrnut, je zpětná relace vázána na tento klíč.
Statický klíč by měl být zahrnut, pokud se očekává odpověď,
tj. pro streamování a odpovědné datagramy.
Neměl by být zahrnut pro raw datagramy.

Zpráva Nové relace je podobná jednosměrnému vzoru Noise [NOISE](https://noiseprotocol.org/noise.html)
„N“ (pokud není odeslán statický klíč),
nebo dvousměrnému vzoru „IK“ (pokud je statický klíč odeslán).



### 1b) Formát nové relace (s vazbou)

Délka je 96 + délka datové části.
Šifrovaný formát:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   Nový dočasný veřejný klíč relace    |
  +             32 bajtů                  +
  |     Zakódovaný pomocí Elligator2      |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +         Statický klíč                 +
  |       Šifrovaná data ChaCha20         |
  +            32 bajtů                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 kód ověření zprávy (MAC)    |
  +    pro sekci statického klíče         +
  |             16 bajtů                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Sekce datové části         +
  |       Šifrovaná data ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 kód ověření zprávy (MAC)    |
  +         pro sekci datové části        +
  |             16 bajtů                  |
  +----+----+----+----+----+----+----+----+

  Veřejný klíč :: 32 bajtů, little endian, Elligator2, čitelný

  Šifrovaná data statického klíče :: 32 bajtů

  Šifrovaná data sekce datové části :: zbývající data mínus 16 bajtů

  MAC :: Poly1305 kód ověření zprávy, 16 bajtů

```


### Nový dočasný klíč relace

Dočasný klíč je 32 bajtů, zakódovaný pomocí Elligator2.
Tento klíč se nikdy neopakuje; nový klíč je generován s
každou zprávou, včetně opakovaných přenosů.

### Statický klíč

Po dešifrování, Alicin X25519 statický klíč, 32 bajtů.


### Datová část

Šifrovaná délka je zbytek dat.
Dešifrovaná délka je o 16 bajtů menší než šifrovaná délka.
Datová část musí obsahovat blok DateTime a obvykle bude obsahovat jeden nebo více bloků Garlic Clove.
Viz sekce datové části níže pro formát a další požadavky.



### 1c) Formát nové relace (bez vazby)

Pokud není vyžadována žádná odpověď, není odeslán žádný statický klíč.


Délka je 96 + délka datové části.
Šifrovaný formát:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   Nový dočasný veřejný klíč relace    |
  +             32 bajtů                  +
  |     Zakódovaný pomocí Elligator2      |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Sekce příznaků              +
  |       Šifrovaná data ChaCha20         |
  +            32 bajtů                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 kód ověření zprávy (MAC)    |
  +         pro výše uvedenou sekci       +
  |             16 bajtů                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Sekce datové části         +
  |       Šifrovaná data ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 kód ověření zprávy (MAC)    |
  +         pro sekci datové části        +
  |             16 bajtů                  |
  +----+----+----+----+----+----+----+----+

  Veřejný klíč :: 32 bajtů, little endian, Elligator2, čitelný

  Šifrovaná data sekce příznaků :: 32 bajtů

  Šifrovaná data sekce datové části :: zbývající data mínus 16 bajtů

  MAC :: Poly1305 kód ověření zprávy, 16 bajtů

```

### Nový dočasný klíč relace

Alicin dočasný klíč.
Dočasný klíč je 32 bajtů, zakódovaný pomocí Elligator2, little endian.
Tento klíč se nikdy neopakuje; nový klíč je generován s
každou zprávou, včetně opakovaných přenosů.


### Dešifrovaná data sekce příznaků

Sekce příznaků neobsahuje nic.
Je vždy 32 bajtů, protože musí mít stejnou délku
jako statický klíč pro zprávy Nové relace s vazbou.
Bob určuje, zda jde o statický klíč nebo sekci příznaků
testováním, zda jsou 32 bajtů všechny nuly.

TODO jsou zde potřeba nějaké příznaky?

### Datová část

Šifrovaná délka je zbytek dat.
Dešifrovaná délka je o 16 bajtů menší než šifrovaná délka.
Datová část musí obsahovat blok DateTime a obvykle bude obsahovat jeden nebo více bloků Garlic Clove.
Viz sekce datové části níže pro formát a další požadavky.




### 1d) Jednorázový formát (bez vazby nebo relace)

Pokud se očekává odeslání pouze jedné zprávy,
není vyžadováno nastavení relace ani statický klíč.


Délka je 96 + délka datové části.
Šifrovaný formát:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |       Dočasný veřejný klíč           |
  +             32 bajtů                  +
  |     Zakódovaný pomocí Elligator2      |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Sekce příznaků              +
  |       Šifrovaná data ChaCha20         |
  +            32 bajtů                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 kód ověření zprávy (MAC)    |
  +         pro výše uvedenou sekci       +
  |             16 bajtů                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Sekce datové části         +
  |       Šifrovaná data ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 kód ověření zprávy (MAC)    |
  +         pro sekci datové části        +
  |             16 bajtů                  |
  +----+----+----+----+----+----+----+----+

  Veřejný klíč :: 32 bajtů, little endian, Elligator2, čitelný

  Šifrovaná data sekce příznaků :: 32 bajtů

  Šifrovaná data sekce datové části :: zbývající data mínus 16 bajtů

  MAC :: Poly1305 kód ověření zprávy, 16 bajtů

```


### Nový jednorázový klíč relace

Jednorázový klíč je 32 bajtů, zakódovaný pomocí Elligator2, little endian.
Tento klíč se nikdy neopakuje; nový klíč je generován s
každou zprávou, včetně opakovaných přenosů.


### Dešifrovaná data sekce příznaků

Sekce příznaků neobsahuje nic.
Je vždy 32 bajtů, protože musí mít stejnou délku
jako statický klíč pro zprávy Nové relace s vazbou.
Bob určuje, zda jde o statický klíč nebo sekci příznaků
testováním, zda jsou 32 bajtů všechny nuly.

TODO jsou zde potřeba nějaké příznaky?

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                                       |
  +             Všechny nuly              +
  |              32 bajtů                 |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+

  nuly:: Všechny nuly, 32 bajtů.

```


### Datová část

Šifrovaná délka je zbytek dat.
Dešifrovaná délka je o 16 bajtů menší než šifrovaná délka.
Datová část musí obsahovat blok DateTime a obvykle bude obsahovat jeden nebo více bloků Garlic Clove.
Viz sekce datové části níže pro formát a další požadavky.



### 1f) KDF pro zprávu Nové relace

### KDF pro počáteční ChainKey

Toto je standardní [NOISE](https://noiseprotocol.org/noise.html) pro IK s upraveným názvem protokolu.
Všimněte si, že používáme stejný inicializátor pro oba vzory IK (vázané relace)
a pro vzor N (nevázané relace).

Název protokolu je upraven z důvodu dvou důvodů.
Za prvé, aby označil, že dočasné klíče jsou kódovány pomocí Elligator2,
a za druhé, aby označil, že je volána funkce MixHash() před druhou zprávou
pro smíchání hodnoty tagu.

```

Toto je vzor „e“:

  // Definujte protocol_name.
  Nastavte protocol_name = "Noise_IKelg2+hs2_25519_ChaChaPoly_SHA256"
   (40 bajtů, kódování US-ASCII, bez ukončení NULL).

  // Definujte Hash h = 32 bajtů
  h = SHA256(protocol_name);

  Definujte ck = 32 bajtový řetězový klíč. Zkopírujte data h do ck.
  Nastavte chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // až sem, může být předpočítáno Alicí pro všechna odchozí spojení

```


### KDF pro šifrovaný obsah sekce příznaků/statického klíče

```

Toto je vzor „e“:

  // Bobovy X25519 statické klíče
  // bpk je publikován v leasesetu
  bsk = GENERATE_PRIVATE()
  bpk = DERIVE_PUBLIC(bsk)

  // Bobův statický veřejný klíč
  // MixHash(bpk)
  // || níže znamená připojení
  h = SHA256(h || bpk);

  // až sem, může být předpočítáno Bobem pro všechna příchozí spojení

  // Aliciny X25519 dočasné klíče
  aesk = GENERATE_PRIVATE_ELG2()
  aepk = DERIVE_PUBLIC(aesk)

  // Alicin dočasný veřejný klíč
  // MixHash(aepk)
  // || níže znamená připojení
  h = SHA256(h || aepk);

  // h je použito jako přidružená data pro AEAD ve zprávě Nové relace
  // Zachovat Hash h pro KDF odpovědi Nové relace
  // eapk je odeslán v čitelném textu na začátku
  // zprávy Nové relace
  elg2_aepk = ENCODE_ELG2(aepk)
  // Jak je dekódováno Bobem
  aepk = DECODE_ELG2(elg2_aepk)

  Konec vzoru „e“.

  Toto je vzor „es“:

  // Noise es
  sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Parametry ChaChaPoly pro šifrování/dešifrování
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Parametry AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, sekce příznaků/statického klíče, ad)

  Konec vzoru „es“.

  Toto je vzor „s“:

  // MixHash(ciphertext)
  // Uložit pro KDF sekce datové části
  h = SHA256(h || ciphertext)

  // Aliciny X25519 statické klíče
  ask = GENERATE_PRIVATE()
  apk = DERIVE_PUBLIC(ask)

  Konec vzoru „s“.


```



### KDF pro sekci datové části (s Aliciným statickým klíčem)

```

Toto je vzor „ss“:

  // Noise ss
  sharedSecret = DH(ask, bpk) = DH(bsk, apk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Parametry ChaChaPoly pro šifrování/dešifrování
  // chainKey z sekce statického klíče
  Nastavte sharedSecret = výsledek X25519 DH
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Parametry AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, datová část, ad)

  Konec vzoru „ss“.

  // MixHash(ciphertext)
  // Uložit pro KDF odpovědi Nové relace
  h = SHA256(h || ciphertext)

```


### KDF pro sekci datové části (bez Alicina statického klíče)

Všimněte si, že toto je vzor Noise „N“, ale používáme stejný inicializátor „IK“
jako pro vázané relace.

Zprávy Nové relace nelze identifikovat jako obsahující Alicin statický klíč nebo ne,
dokud není statický klíč dešifrován a zkontrolován, zda obsahuje všechny nuly.
Proto musí příjemce použít stavový stroj „IK“ pro všechny
zprávy Nové relace.
Pokud je statický klíč všechny nuly, musí být vzor „ss“ přeskočen.



```

chainKey = z sekce příznaků/statického klíče
  k = z sekce příznaků/statického klíče
  n = 1
  ad = h z sekce příznaků/statického klíče
  ciphertext = ENCRYPT(k, n, datová část, ad)

```



### 1g) Formát odpovědi Nové relace

Jedna nebo více odpovědí Nové relace mohou být odeslány jako odpověď na jednu zprávu Nové relace.
Každá odpověď je předřazena tagem, který je generován ze sady tagů pro relaci.

Odpověď Nové relace se skládá ze dvou částí.
První část je dokončení handshake Noise IK s předřazeným tagem.
Délka první části je 56 bajtů.
Druhá část je datová část fáze dat.
Délka druhé části je 16 + délka datové části.

Celková délka je 72 + délka datové části.
Šifrovaný formát:

```

+----+----+----+----+----+----+----+----+
  |       Session Tag   8 bajtů           |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Dočasný veřejný klíč           +
  |                                       |
  +            32 bajtů                   +
  |     Zakódovaný pomocí Elligator2      |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 kód ověření zprávy (MAC)    |
  +  (MAC) pro sekci klíče (žádná data)   +
  |             16 bajtů                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Sekce datové části         +
  |       Šifrovaná data ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 kód ověření zprávy (MAC)    |
  +         pro sekci datové části        +
  |             16 bajtů                  |
  +----+----+----+----+----+----+----+----+

  Tag :: 8 bajtů, čitelný text

  Veřejný klíč :: 32 bajtů, little endian, Elligator2, čitelný text

  MAC :: Poly1305 kód ověření zprávy, 16 bajtů
         Poznámka: Šifrovaný text ChaCha20 je prázdný (ZEROLEN)

  Šifrovaná data sekce datové části :: zbývající data mínus 16 bajtů

  MAC :: Poly1305 kód ověření zprávy, 16 bajtů

```

### Session Tag
Tag je generován v KDF Session Tags, jak je inicializováno
v KDF inicializace DH níže.
To
