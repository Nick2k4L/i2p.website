---
title: "Nové záznamy netDB"
number: "123"
author: "zzz, str4d, orignal"
created: "2016-01-16"
lastupdated: "2020-07-18"
status: "Otevřít"
thread: "http://zzz.i2p/topics/2051"
supercedes: "110, 120, 121, 122"
toc: true
---
## Stav

Části tohoto návrhu jsou dokončeny a implementovány ve verzích 0.9.38 a 0.9.39.  
Společné struktury, I2CP, I2NP a další specifikace  
jsou nyní aktualizovány, aby odrážely změny, které jsou nyní podporovány.

Dokončené části jsou stále předmětem drobných revizí.  
Další části tohoto návrhu jsou stále ve vývoji  
a podléhají významným revizím.

Vyhledávání služeb (typy 9 a 11) má nízkou prioritu,  
není naplánováno a může být přesunuto do samostatného návrhu.


## Přehled

Toto je aktualizace a agregace následujících 4 návrhů:

- 110 LS2
- 120 Meta LS2 pro masivní multihoming
- 121 Šifrovaný LS2
- 122 Neověřené vyhledávání služeb (anycasting)

Tyto návrhy jsou většinou nezávislé, ale pro přehlednost definujeme a používáme  
společný formát pro několik z nich.

Následující návrhy jsou nějakým způsobem související:

- 140 Neviditelný multihoming (nekompatibilní s tímto návrhem)
- 142 Nová šablona kryptografie (pro novou symetrickou kryptografii)
- 144 ECIES-X25519-AEAD-Ratchet
- 145 ECIES-P256
- 146 Red25519
- 148 EdDSA-BLAKE2b-Ed25519
- 149 B32 pro Šifrovaný LS2
- 150 Protokol Garlic Farm
- 151 ECDSA Blinding


## Návrh

Tento návrh definuje 5 nových typů DatabaseEntry a proces pro  
jejich ukládání do a načítání z databáze sítě,  
stejně jako metodu pro jejich podepisování a ověřování těchto podpisů.

### Cíle

- Zpětná kompatibilita
- LS2 použitelný se starším stylem multihomingu
- Pro podporu nejsou vyžadovány nové kryptografické algoritmy ani primitiva
- Zachování oddělení kryptografie a podepisování; podpora všech současných a budoucích verzí
- Povolení volitelných offline podepisovacích klíčů
- Snížení přesnosti časových razítek za účelem snížení možnosti fingerprintingu
- Povolení nové kryptografie pro cíle
- Povolení masivního multihomingu
- Oprava více problémů s existujícím šifrovaným LS
- Volitelné skrývání za účelem snížení viditelnosti pro floodfill uzly
- Šifrování podporuje jak jediný klíč, tak více odvolatelných klíčů
- Vyhledávání služeb pro snadnější vyhledávání outproxy, bootstrap aplikace DHT,  
  a další použití
- Neporušovat nic, co závisí na 32bitových binárních hashích cílů, např. bittorrent
- Přidání flexibility do leasesetů prostřednictvím vlastností, jako máme u routerinfos.
- Umístění časového razítka publikování a proměnné expirace do hlavičky, aby to fungovalo i  
  v případě, že obsah je šifrovaný (nepočítat časové razítko z nejstaršího lease)
- Všechny nové typy žijí ve stejném DHT prostoru a stejných umístěních jako stávající leasesety,  
  takže uživatelé mohou migrovat ze starého LS na LS2,  
  nebo přepínat mezi LS2, Meta a Šifrovaným,  
  aniž by měnili Cíl nebo hash.
- Stávající Cíl může být převeden na použití offline klíčů,  
  nebo zpět na online klíče, aniž by se měnil Cíl nebo hash.


### Není cílem / Mimo rozsah

- Nový algoritmus rotace DHT nebo generování sdíleného náhodného čísla
- Konkrétní nový typ šifrování a end-to-end šifrovací schéma  
  pro použití tohoto nového typu by bylo v samostatném návrhu.  
  Žádná nová kryptografie není zde specifikována ani diskutována.
- Nové šifrování pro RIs nebo stavbu tunelů.  
  To by bylo v samostatném návrhu.
- Metody šifrování, přenosu a příjmu zpráv I2NP DLM / DSM / DSRM.  
  Nebudou měněny.
- Jak generovat a podporovat Meta, včetně komunikace mezi backendovými směrovači, správy, převzetí a koordinace.  
  Podpora může být přidána do I2CP, nebo i2pcontrol, nebo nového protokolu.  
  To může být nebo nemusí být standardizováno.
- Jak skutečně implementovat a spravovat delší expirující tunely, nebo zrušit stávající tunely.  
  To je extrémně obtížné a bez toho nemůžete mít rozumné postupné vypnutí.
- Změny modelu hrozeb
- Formát offline úložiště, nebo metody pro ukládání/načítání/sdílení dat.
- Podrobnosti implementace nejsou zde diskutovány a jsou ponechány na každém projektu.



### Odůvodnění

LS2 přidává pole pro změnu typu šifrování a pro budoucí změny protokolu.

Šifrovaný LS2 opravuje několik bezpečnostních problémů stávajícího šifrovaného LS tím,  
že používá asymetrické šifrování celé sady lease.

Meta LS2 poskytuje flexibilní, efektivní, účinné a škálovatelné řešení multihomingu.

Záznam služby a Seznam služeb poskytují anycast služby jako vyhledávání jmen  
a bootstrapování DHT.


### Typy dat NetDB

Čísla typů jsou použita ve zprávách I2NP Database Lookup/Store.

Sloupec end-to-end označuje, zda jsou dotazy/odpovědi odesílány do Cíle ve zprávě Garlic.


Stávající typy:

| NetDB Data | Typ vyhledávání | Typ ukládání |
|------------|-------------|------------|
| jakýkoli        | 0           | jakýkoli        |
| LS         | 1           | 1          |
| RI         | 2           | 0          |
| exploratory| 3           | DSRM       |

Nové typy:

| NetDB Data     | Typ vyhledávání | Typ ukládání | Standardní hlavička LS2? | Odesíláno end-to-end? |
|----------------|-------------|------------|------------------|------------------|
| LS2            | 1           | 3          | ano              | ano              |
| Šifrovaný LS2  | 1           | 5          | ne               | ne               |
| Meta LS2       | 1           | 7          | ano              | ne               |
| Záznam služby | n/a         | 9          | ano              | ne               |
| Seznam služeb   | 4           | 11         | ne               | ne               |



### Poznámky

- Typy vyhledávání jsou aktuálně bity 3-2 ve zprávě Database Lookup.  
  Jakékoli další typy by vyžadovaly použití bitu 4.

- Všechny typy ukládání jsou liché, protože horní bity ve zprávě Database Store  
  jsou staršími směrovači ignorovány.  
  Raději bychom chtěli, aby se analýza nezdařila jako LS než jako komprimovaný RI.

- Měl by být typ explicitní, implicitní nebo ani jedno v datech pokrytých podpisem?



### Proces vyhledávání/ukládání

Typy 3, 5 a 7 mohou být vráceny jako odpověď na standardní vyhledávání leasesetu (typ 1).  
Typ 9 nikdy není vrácen jako odpověď na vyhledávání.  
Typ 11 je vrácen jako odpověď na nový typ vyhledávání služby (typ 11).

Pouze typ 3 může být odeslán ve zprávě Garlic mezi klienty.



### Formát

Typy 3, 7 a 9 mají společný formát::

  Standardní hlavička LS2
  - jak je definováno níže

  Část specifická pro typ
  - jak je definováno níže pro každou část

  Standardní podpis LS2:
  - Délka podle typu podpisu podepisovacího klíče

Typ 5 (Šifrovaný) nezačíná Cílem a má  
jiný formát. Viz níže.

Typ 11 (Seznam služeb) je agregací několika Záznamů služeb a má  
jiný formát. Viz níže.


### Úvahy o soukromí/bezpečnosti

TBD



## Standardní hlavička LS2

Typy 3, 7 a 9 používají standardní hlavičku LS2, specifikovanou níže:


### Formát

```
Standardní hlavička LS2:
  - Typ (1 bajt)
    Ve skutečnosti není v hlavičce, ale je součástí dat pokrytých podpisem.
    Vezměte z pole ve zprávě Database Store.
  - Cíl (387+ bajtů)
  - Časové razítko publikování (4 bajty, big endian, sekundy od epochy, přeteče v roce 2106)
  - Expire (2 bajty, big endian) (offset od časového razítka publikování v sekundách, max 18,2 hodiny)
  - Příznaky (2 bajty)
    Bitové pořadí: 15 14 ... 3 2 1 0
    Bit 0: Pokud 0, žádné offline klíče; pokud 1, offline klíče
    Bit 1: Pokud 0, standardní publikovaný leaseset.
           Pokud 1, nepublikovaný leaseset. Neměl by být šířen, publikován nebo
           odeslán jako odpověď na dotaz. Pokud tento leaseset expiruje, nevyhledávejte
           v netdb nový, pokud není nastaven bit 2.
    Bit 2: Pokud 0, standardní publikovaný leaseset.
           Pokud 1, tento nešifrovaný leaseset bude při publikování zaslepen a zašifrován.
           Pokud tento leaseset expiruje, vyhledejte zaslepené umístění v netdb pro nový.
           Pokud je tento bit nastaven na 1, nastavte také bit 1 na 1.
           Od verze 0.9.42.
    Bity 3-15: nastavte na 0 pro kompatibilitu s budoucím použitím
  - Pokud příznak označuje offline klíče, sekce offline podpisu:
    Časové razítko expirace (4 bajty, big endian, sekundy od epochy, přeteče v roce 2106)
    Přechodný typ podpisu (2 bajty, big endian)
    Přechodný veřejný podepisovací klíč (délka podle typu podpisu)
    Podpis časového razítka expirace, přechodného typu podpisu a veřejného klíče,
    pomocí veřejného klíče cíle,
    délka podle typu podpisu veřejného klíče cíle.
    Tato sekce může být a měla by být generována offline.
```

### Odůvodnění

- Nepublikovaný/publikovaný: Pro použití při odesílání databáze uložit end-to-end,
  odesílající směrovač může chtít označit, že tento leaseset by neměl být
  odesílán ostatním. Aktuálně používáme heuristiku k udržování tohoto stavu.

- Publikovaný: Nahrazuje složitou logiku potřebnou k určení 'verze' leasesetu.
  Aktuálně je verzí expirace posledního expirujícího lease,
  a směrovač publikující leaseset, který pouze odstraňuje starší lease, musí tuto expiraci zvýšit alespoň o 1ms.

- Expire: Umožňuje, aby expirace záznamu v netdb byla dřívější než expirace
  jeho posledního leasesetu. Možná nebude užitečný pro LS2, kde se očekává, že leasesety
  budou mít maximální expiraci 11 minut, ale
  pro jiné nové typy je to nezbytné (viz Meta LS a Záznam služby níže).

- Offline klíče jsou volitelné, aby se snížila počáteční/požadovaná složitost implementace.


### Problémy

- Můžeme snížit přesnost časového razítka ještě více (10 minut?), ale museli bychom přidat
  číslo verze. To by mohlo porušit multihoming, pokud nemáme šifrování zachovávající pořadí?
  Pravděpodobně nemůžeme bez časových razítek vůbec.

- Alternativa: 3 bajtové časové razítko (epocha / 10 minut), 1-bajtová verze, 2-bajtové expirace

- Je typ explicitní nebo implicitní v datech / podpisu? "Doménové" konstanty pro podpis?


### Poznámky

- Směrovače by neměly publikovat LS více než jednou za sekundu.
  Pokud ano, musí uměle zvýšit časové razítko publikování o 1
  oproti dříve publikovanému LS.

- Implementace směrovačů by mohly ukládat přechodné klíče a podpis do mezipaměti, aby
  se vyhnuly ověřování pokaždé. Zejména floodfill uzly a směrovače na
  obou koncích dlouhodobých spojení by mohly z toho těžit.

- Offline klíče a podpis jsou vhodné pouze pro dlouhodobé cíle,
  tj. servery, ne klienty.



## Nové typy DatabaseEntry


### LeaseSet 2

Změny oproti stávajícímu LeaseSet:

- Přidání časového razítka publikování, časového razítka expirace, příznaků a vlastností
- Přidání typu šifrování
- Odstranění klíče pro odvolání

Vyhledávání s
    Standardní příznak LS (1)
Ukládání s
    Standardní typ LS2 (3)
Ukládání na
    Hash cíle
    Tento hash je pak použit k vygenerování denního "směrovacího klíče", jako u LS1
Typická expirace
    10 minut, jako u běžného LS.
Publikováno
    Cílem

### Formát

```
Standardní hlavička LS2 jak je specifikována výše

  Standardní část specifická pro typ LS2
  - Vlastnosti (Mapování jak je specifikováno ve specifikaci společných struktur, 2 nulové bajty pokud žádné)
  - Počet sekcí klíčů, které následují (1 bajt, max TBD)
  - Sekce klíčů:
    - Typ šifrování (2 bajty, big endian)
    - Délka šifrovacího klíče (2 bajty, big endian)
      Toto je explicitní, aby floodfill uzly mohly analyzovat LS2 s neznámými typy šifrování.
    - Šifrovací klíč (počet bajtů specifikovaný)
  - Počet lease2 (1 bajt)
  - Lease2 (40 bajtů každý)
    To jsou lease, ale s 4-bajtovým místo 8-bajtovým expiračním časem,
    sekundy od epochy (přeteče v roce 2106)

  Standardní podpis LS2:
  - Podpis
    Pokud příznak označuje offline klíče, je podepsán přechodným veřejným klíčem,
    jinak veřejným klíčem cíle
    Délka podle typu podpisu podepisovacího klíče
    Podpis všeho výše.
```


### Odůvodnění

- Vlastnosti: Budoucí rozšiřitelnost a flexibilita.
  Umístěny na začátek pro případ, že jsou potřeba pro analýzu zbývajících dat.

- Více párů typ šifrování/veřejný klíč jsou
  pro usnadnění přechodu na nové typy šifrování. Jiná možnost je
  publikovat více leasesetů, možná pomocí stejných tunelů,
  jak to děláme nyní pro DSA a EdDSA cíle.
  Identifikace příchozího typu šifrování na tunelu
  může být provedena pomocí stávajícího mechanismu značky relace,
  a/nebo zkoušením dešifrování pomocí každého klíče. Délky příchozích
  zpráv mohou také poskytnout nápovědu.

### Diskuze

Tento návrh nadále používá veřejný klíč v leasesetu pro
end-to-end šifrovací klíč a ponechává pole veřejného klíče v
Cíli nevyužité, jak je to nyní. Typ šifrování není specifikován
v certifikátu klíče Cíle, zůstane 0.

Zamítnutá alternativa je specifikovat typ šifrování v certifikátu klíče Cíle,
použít veřejný klíč v Cíli a nepoužívat veřejný klíč
v leasesetu. Toto neplánujeme dělat.

Výhody LS2:

- Umístění skutečného veřejného klíče se nemění.
- Typ šifrování nebo veřejný klíč se může změnit bez změny Cíle.
- Odstraňuje nepoužívané pole pro odvolání
- Základní kompatibilita s jinými typy DatabaseEntry v tomto návrhu
- Umožňuje více typů šifrování

Nevýhody LS2:

- Umístění veřejného klíče a typu šifrování se liší od RouterInfo
- Zachovává nepoužívaný veřejný klíč v leasesetu
- Vyžaduje implementaci napříč sítí; v alternativě mohou být použity experimentální
  typy šifrování, pokud jsou povoleny floodfill uzly
  (ale viz související návrhy 136 a 137 o podpoře experimentálních typů podpisů).
  Alternativní návrh by mohl být jednodušší na implementaci a testování pro experimentální typy šifrování.


### Nové problémy šifrování

Některé z toho je mimo rozsah tohoto návrhu,
ale zatím zde zanecháváme poznámky, protože nemáme
zatím samostatný návrh na šifrování.
Viz také návrhy ECIES 144 a 145.

- Typ šifrování představuje kombinaci
  křivky, délky klíče a end-to-end schématu,
  včetně KDF a MAC, pokud existují.

- Zahrnuli jsme pole délky klíče, aby LS2 byl
  analyzovatelný a ověřitelný floodfillem i pro neznámé typy šifrování.

- První nový typ šifrování, který bude navržen,
  bude pravděpodobně ECIES/X25519. Jak se používá end-to-end
  (buď mírně upravená verze ElGamal/AES+SessionTag
  nebo něco úplně nového, např. ChaCha/Poly) bude specifikováno
  v jednom nebo více samostatných návrzích.
  Viz také návrhy ECIES 144 a 145.


### Poznámky

- 8-bajtová expirace v lease byla změněna na 4 bajty.

- Pokud bychom kdy implementovali odvolání, mohli bychom to udělat s polem expirace na nule,
  nebo nulovými lease, nebo obojím. Není potřeba samostatný klíč pro odvolání.

- Šifrovací klíče jsou v pořadí podle preference serveru, nejpreferovanější první.
  Výchozí chování klienta je vybrat první klíč s
  podporovaným typem šifrování. Klienti mohou používat jiné algoritmy výběru
  na základě podpory šifrování, relativního výkonu a dalších faktorů.


### Šifrovaný LS2

Cíle:

- Přidání zaslepení
- Povolení více typů podpisů
- Nevyžadovat žádné nové kryptografické primitivy
- Volitelně šifrovat každému příjemci, odvolatelné
- Podpora šifrování Standardního LS2 a Meta LS2 pouze

Šifrovaný LS2 nikdy není odesílán ve zprávě Garlic end-to-end.
Použijte standardní LS2 výše.


Změny oproti stávajícímu šifrovanému LeaseSet:

- Šifrovat celou věc pro zabezpečení
- Bezpečně šifrovat, ne jen pomocí AES.
- Šifrovat každému příjemci

Vyhledávání s
    Standardní příznak LS (1)
Ukládání s
    Typ Šifrovaného LS2 (5)
Ukládání na
    Hash zaslepeného typu podpisu a zaslepeného veřejného klíče
    Dvoubajtový typ podpisu (big endian, např. 0x000b) || zaslepený veřejný klíč
    Tento hash je pak použit k vygenerování denního "směrovacího klíče", jako u LS1
Typická expirace
    10 minut, jako u běžného LS, nebo hodiny, jako u meta LS.
Publikováno
    Cílem


### Definice

Definujeme následující funkce odpovídající kryptografickým stavebním blokům použitým
pro šifrovaný LS2:

CSRNG(n)
    n-bajtový výstup z kryptograficky bezpečného generátoru náhodných čísel.

    Kromě požadavku, že CSRNG je kryptograficky bezpečný (a tedy
    vhodný pro generování materiálu klíčů), MUSÍ být bezpečné
    pro použití nějakého n-bajtového výstupu jako materiálu klíče, když jsou byteové sekvence bezprostředně
    před a po něm vystaveny na síti (např. jako sůl nebo zašifrované odsazení). Implementace, které spoléhají na potenciálně nedůvěryhodný zdroj, by měly hashovat
    jakýkoli výstup, který bude vystaven na síti. Viz [PRNG references](http://projectbullrun.org/dual-ec/ext-rand.html) a [Tor dev discussion](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html).

H(p, d)
    Funkce hash SHA-256, která bere osobní řetězec p a data d a
    vytváří výstup o délce 32 bajtů.

    Použijte SHA-256 následovně::

        H(p, d) := SHA-256(p || d)

STREAM
    Proudová šifra ChaCha20 jak je specifikována v [RFC 7539 Section 2.4](https://tools.ietf.org/html/rfc7539#section-2.4), s počátečním čítačem
    nastaveným na 1. S_KEY_LEN = 32 a S_IV_LEN = 12.

    ENCRYPT(k, iv, plaintext)
        Šifruje plaintext pomocí šifrovacího klíče k a nonce iv, která MUSÍ být jedinečná pro
        klíč k. Vrací šifrový text stejné velikosti jako plaintext.

        Celý šifrový text musí být nerozlišitelný od náhodného, pokud je klíč tajný.

    DECRYPT(k, iv, ciphertext)
        Dešifruje šifrový text pomocí šifrovacího klíče k a nonce iv. Vrací plaintext.


SIG
    Schéma podpisu RedDSA (odpovídající SigType 11) s klíčovým zaslepením.
    Má následující funkce:

    DERIVE_PUBLIC(privkey)
        Vrací veřejný klíč odpovídající danému soukromému klíči.

    SIGN(privkey, m)
        Vrací podpis soukromým klíčem privkey nad danou zprávou m.

    VERIFY(pubkey, m, sig)
        Ověřuje podpis sig proti veřejnému klíči pubkey a zprávě m. Vrací
        true, pokud je podpis platný, jinak false.

    Musí také podporovat následující operace klíčového zaslepení:

    GENERATE_ALPHA(data, secret)
        Vygeneruje alfa pro ty, kteří znají data a volitelné tajemství.
        Výsledek musí mít identické rozdělení jako soukromé klíče.

    BLIND_PRIVKEY(privkey, alpha)
        Zaslepí soukromý klíč pomocí tajného alfa.

    BLIND_PUBKEY(pubkey, alpha)
        Zaslepí veřejný klíč pomocí tajného alfa.
        Pro daný pár klíčů (privkey, pubkey) platí následující vztah::

            BLIND_PUBKEY(pubkey, alpha) ==
            DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))

DH
    Systém veřejného klíčového dohody X25519. Soukromé klíče o délce 32 bajtů, veřejné klíče o délce 32
    bajtů, vytváří výstupy o délce 32 bajtů. Má následující
    funkce:

    GENERATE_PRIVATE()
        Vygeneruje nový soukromý klíč.

    DERIVE_PUBLIC(privkey)
        Vrací veřejný klíč odpovídající danému soukromému klíči.

    DH(privkey, pubkey)
        Vygeneruje sdílené tajemství z daného soukromého a veřejného klíče.

HKDF(salt, ikm, info, n)
    Kryptografická funkce odvození klíče, která bere vstupní materiál klíče ikm (který
    by měl mít dobrý entropii, ale není vyžadováno, aby byl rovnoměrně náhodný řetězec), sůl
    o délce 32 bajtů a kontextově specifickou hodnotu 'info' a vytváří výstup
    o n bajtech vhodný pro použití jako materiál klíče.

    Použijte HKDF jak je specifikováno v [RFC 5869](https://tools.ietf.org/html/rfc5869), pomocí HMAC hash funkce SHA-256
    jak je specifikováno v [RFC 2104](https://tools.ietf.org/html/rfc2104). To znamená, že SALT_LEN je maximálně 32 bajtů.


### Formát

Formát šifrovaného LS2 se skládá ze tří vnořených vrstev:

- Vnější vrstva obsahující nezbytné prosté informace pro ukládání a načítání.
- Střední vrstva, která zpracovává ověřování klienta.
- Vnitřní vrstva, která obsahuje skutečná data LS2.

Celkový formát vypadá takto::

    Data vrstvy 0 + Enc(data vrstvy 1 + Enc(data vrstvy 2)) + Podpis

Všimněte si, že šifrovaný LS2 je zaslepený. Cíl není v hlavičce.
Umístění úložiště DHT je SHA-256(typ podpisu || zaslepený veřejný klíč) a rotuje se denně.

Nepoužívá standardní hlavičku LS2 specifikovanou výše.

#### Vrstva 0 (vnější)
Typ
    1 bajt

    Ve skutečnosti není v hlavičce, ale je součástí dat pokrytých podpisem.
    Vezměte z pole ve zprávě Database Store.

Typ zaslepeného veřejného klíče
    2 bajty, big endian
    Toto bude vždy typ 11, identifikující zaslepený klíč Red25519.

Zaslepený veřejný klíč
    Délka podle typu podpisu

Časové razítko publikování
    4 bajty, big endian

    Sekundy od epochy, přeteče v roce 2106

Expire
    2 bajty, big endian

    Offset od časového razítka publikování v sekundách, max 18,2 hodiny

Příznaky
    2 bajty

    Bitové pořadí: 15 14 ... 3 2 1 0

    Bit 0: Pokud 0, žádné offline klíče; pokud 1, offline klíče

    Ostatní bity: nastavte na 0 pro kompatibilitu s budoucím použitím

Data přechodného klíče
    Přítomna, pokud příznak označuje offline klíče

    Časové razítko expirace
        4 bajty, big endian

        Sekundy od epochy, přeteče v roce 2106

    Přechodný typ podpisu
        2 bajty, big endian

    Přechodný veřejný podepisovací klíč
        Délka podle typu podpisu

    Podpis
        Délka podle typu podpisu zaslepeného veřejného klíče

        Nad časovým razítkem expirace, přechodným typem podpisu a přechodným veřejným klíčem.

        Ověřeno pomocí zaslepeného veřejného klíče.

lenOuterCiphertext
    2 bajty, big endian

outerCiphertext
    lenOuterCiphertext bajtů

    Šifrovaná data vrstvy 1. Viz níže pro algoritmy odvození klíče a šifrování.

Podpis
    Délka podle typu podpisu použitého podepisovacího klíče

    Podpis všeho výše.

    Pokud příznak označuje offline klíče, je podpis ověřen pomocí přechodného
    veřejného klíče. Jinak je podpis ověřen pomocí zaslepeného veřejného klíče.


#### Vrstva 1 (střední)
Příznaky
    1 bajt
    
    Bitové pořadí: 76543210

    Bit 0: 0 pro všechny, 1 pro konkrétního klienta, následuje sekce ověření

    Bity 3-1: Schéma ověření, pouze pokud je bit 0 nastaven na 1 pro konkrétního klienta, jinak 000
              000: Ověření klienta DH (nebo žádné ověření pro konkrétního klienta)
              001: Ověření klienta PSK

    Bity 7-4: Nepoužito, nastavte na 0 pro budoucí kompatibilitu

Data ověření klienta DH
    Přítomna, pokud je bit příznaku 0 nastaven na 1 a bity příznaku 3-1 jsou nastaveny na 000.

    ephemeralPublicKey
        32 bajtů

    clients
        2 bajty, big endian

        Počet položek authClient, které následují, 40 bajtů každá

    authClient
        Autorizační data pro jednoho klienta.
        Viz níže pro algoritmus autorizace pro konkrétního klienta.

        clientID_i
            8 bajtů

        clientCookie_i
            32 bajtů

Data ověření klienta PSK
    Přítomna, pokud je bit příznaku 0 nastaven na 1 a bity příznaku 3-1 jsou nastaveny na 001.

    authSalt
        32 bajtů

    clients
        2 bajty, big endian

        Počet položek authClient, které následují, 40 bajtů každá

    authClient
        Autorizační data pro jednoho klienta.
        Viz níže pro algoritmus autorizace pro konkrétního klienta.

        clientID_i
            8 bajtů

        clientCookie_i
            32 bajtů


innerCiphertext
    Délka podle lenOuterCiphertext (cokoli zbývajících dat)

    Šifrovaná data vrstvy 2. Viz níže pro algoritmy odvození klíče a šifrování.


#### Vrstva 2 (vnitřní)
Typ
    1 bajt

    Buď 3 (LS2) nebo 7 (Meta LS2)

Data
    Data LeaseSet2 pro daný typ.

    Zahrnuje hlavičku a podpis.


### Odvození klíče zaslepení

Používáme následující schéma pro zaslepení klíče,
založené na Ed25519 a [ZCash RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf).
Podpisy Re25519 jsou nad křivkou Ed25519, pomocí SHA-512 pro hash.

Nepoužíváme [Tor's rend-spec-v3.txt appendix A.2](https://spec.torproject.org/rend-spec-v3),
který má podobné cíle návrhu, protože jeho zaslepené veřejné klíče
mohou být mimo prvočíselnou podskupinu, s neznámými bezpečnostními důsledky.


#### Cíle

- Veřejný klíč pro podepisování v nezaslepeném cíli musí být
  Ed25519 (typ podpisu 7) nebo Red25519 (typ podpisu 11);
  žádné jiné typy podpisů nejsou podporovány
- Pokud je veřejný klíč pro podepisování offline, musí být přechodný veřejný klíč pro podepisování také Ed25519
- Zaslepení je výpočetně jednoduché
- Použití stávajících kryptografických primitiv
- Zaslepené veřejné klíče nelze odzaslepit
- Zaslepené veřejné klíče musí být na křivce Ed25519 a v prvočíselné podskupině
- Musí být znám veřejný klíč pro podepisování cíle
  (plný cíl není vyžadován) pro odvození zaslepeného veřejného klíče
- Volitelně poskytnout další tajemství vyžadované pro odvození zaslepeného veřejného klíče


#### Bezpečnost

Bezpečnost schématu zaslepení vyžaduje, aby
distribuce alfa byla stejná jako u nezaslepených soukromých klíčů.
Avšak když zaslepíme soukromý klíč Ed25519 (typ podpisu 7)
na soukromý klíč Red25519 (typ podpisu 11), distribuce je jiná.
Pro splnění požadavků [zcash section 4.1.6.1](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf),
měl by být pro nezaslepené klíče použit také Red25519 (typ podpisu 11), aby
"kombinace znovu náhodně generovaného veřejného klíče a podpisů
pod tímto klíčem neodhalila klíč, ze kterého byl znovu náhodně generován."
Umožňujeme typ 7 pro stávající cíle, ale doporučujeme
typ 11 pro nové cíle, které budou šifrované.



#### Definice

B
    Základní bod (generátor) Ed25519 2^255 - 19 jak je v [Ed25519](http://cr.yp.to/papers.html#ed25519)

L
    Řád Ed25519 2^252 + 27742317777372353535851937790883648493
    jak je v [Ed25519](http://cr.yp.to/papers.html#ed25519)

DERIVE_PUBLIC(a)
    Převod soukromého klíče na veřejný, jak je v Ed25519 (násobení G)

alpha
    32bajtové náhodné číslo známé těm, kteří znají cíl.

GENERATE_ALPHA(destination, date, secret)
    Vygeneruje alfa pro aktuální datum, pro ty, kteří znají cíl a tajemství.
    Výsledek musí mít identické rozdělení jako soukromé klíče Ed25519.

a
    Nezaslepený 32bajtový soukromý klíč EdDSA nebo RedDSA použitý k podepsání cíle

A
    Nezaslepený 32bajtový veřejný klíč EdDSA nebo RedDSA v cíli,
    = DERIVE_PUBLIC(a), jak je v Ed25519

a'
    Zaslepený 32bajtový soukromý klíč EdDSA použitý k podepsání šifrovaného leasesetu
    Toto je platný soukromý klíč EdDSA.

A'
    Zaslepený 32bajtový veřejný klíč EdDSA v Cíli,
    může být generován pomocí DERIVE_PUBLIC(a'), nebo z A a alfa.
    Toto je platný veřejný klíč EdDSA, na křivce a v prvočíselné podskupině.

LEOS2IP(x)
    Převrátí pořadí vstupních bajtů na little-endian

H*(x)
    32 bajtů = (LEOS2IP(SHA512(x))) mod B, stejné jako v Ed25519 hash-and-reduce


#### Výpočty zaslepení

Nové tajemství alfa a zaslepené klíče musí být generovány každý den (UTC).
Tajemství alfa a zaslepené klíče jsou vypočítány následovně.

GENERATE_ALPHA(destination, date, secret), pro všechny strany:

```text
// GENERATE_ALPHA(destination, date, secret)

  // tajemství je volitelné, jinak nulové délky
  A = veřejný klíč pro podepisování cíle
  stA = typ podpisu A, 2 bajty big endian (0x0007 nebo 0x000b)
  stA' = typ podpisu zaslepeného veřejného klíče A', 2 bajty big endian (0x000b)
  keydata = A || stA || stA'
  datestring = 8 bajtů ASCII YYYYMMDD z aktuálního data UTC
  secret = řetězec kódovaný UTF-8
  seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || secret, "i2pblinding1", 64)
  // považujte seed za 64bajtovou hodnotu little-endian
  alpha = seed mod L
```

BLIND_PRIVKEY(), pro vlastníka publikujícího leaseset:

```text
// BLIND_PRIVKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  // Pokud pro soukromý klíč Ed25519 (typ 7)
  seed = soukromý klíč pro podepisování cíle
  a = levá polovina SHA512(seed) a upravena jako obvykle pro Ed25519
  // jinak, pro soukromý klíč Red25519 (typ 11)
  a = soukromý klíč pro podepisování cíle
  // Sčítání pomocí skalární aritmetiky
  zaslepený soukromý klíč pro podepisování = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
  zaslepený veřejný klíč pro podepisování = A' = DERIVE_PUBLIC(a')
```

BLIND_PUBKEY(), pro klienty načítající leaseset:

```text
// BLIND_PUBKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  A = veřejný klíč pro podepisování cíle
  // Sčítání pomocí prvků skupiny (bodů na křivce)
  zaslepený veřejný klíč = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```

Obě metody výpočtu A' dávají stejný výsledek, jak je vyžadováno.



#### Podepisování

Nezaslepený leaseset je podepsán nezaslepeným soukromým klíčem pro podepisování Ed25519 nebo Red25519
a ověřen pomocí nezaslepeného veřejného klíče pro podepisování Ed25519 nebo Red25519 (typy podpisu 7 nebo 11) jako obvykle.

Pokud je veřejný klíč pro podepisování offline,
je nezaslepený leaseset podepsán nezaslepeným přechodným soukromým klíčem pro podepisování Ed25519 nebo Red25519
a ověřen pomocí nezaslepeného veřejného klíče pro podepisování Ed25519 nebo Red25519 (typy podpisu 7 nebo 11) jako obvykle.
Viz níže pro další poznámky k offline klíčům pro šifrované leasesety.

Pro podepisování šifrovaného leasesetu používáme Red25519, založené na [RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)
k podepisování a ověřování pomocí zaslepených klíčů.
Podpisy Red25519 jsou nad křivkou Ed25519, pomocí SHA-512 pro hash.

Red25519 je identické se standardním Ed25519 s výjimkou níže uvedeného.


#### Výpočty podepisování/ověřování

Vnější část šifrovaného leasesetu používá klíče a podpisy Red25519.

Red25519 je téměř identické s Ed25519. Jsou dvě rozdíly:

Soukromé klíče Red25519 jsou generovány z náhodných čísel a pak musí být redukovány mod L, kde L je definováno výše.
Soukromé klíče Ed25519 jsou generovány z náhodných čísel a pak "upraveny" pomocí
bitové masky na bajty 0 a 31. To se u Red25519 nedělá.
Funkce GENERATE_ALPHA() a BLIND_PRIVKEY() definované výše generují správné
soukromé klíče Red25519 pomocí mod L.

V Red25519 se výpočet r pro podepisování používá další náhodná data,
a používá hodnotu veřejného klíče místo hashu soukromého klíče.
Kvůli náhodným datům je každý podpis Red25519 jiný, i když
podepisuje stejná data stejným klíčem.

Podepisování:

```text
T = 80 náhodných bajtů
  r = H*(T || publickey || message)
  // zbytek je stejný jako v Ed25519
```

Ověřování:

```text
// stejné jako v Ed25519
```



### Šifrování a zpracování

#### Odvození podpověření
Jako součást procesu zaslepení musíme zajistit, že šifrovaný LS2 může být
dešifrován pouze někým, kdo zná odpovídající veřejný klíč pro podepisování Cíle.
Plný Cíl není vyžadován.
Pro dosažení tohoto cíle odvozujeme pověření z veřejného klíče pro podepisování:

```text
A = veřejný klíč pro podepisování cíle
  stA = typ podpisu A, 2 bajty big endian (0x0007 nebo 0x000b)
  stA' = typ podpisu A', 2 bajty big endian (0x000b)
  keydata = A || stA || stA'
  credential = H("credential", keydata)
```

Osobní řetězec zajišťuje, že pověření se nesrazí s žádným hashem použitým
jako klíč vyhledávání DHT, jako je prostý hash Cíle.

Pro daný zaslepený klíč pak můžeme odvodit podpověření:

```text
subcredential = H("subcredential", credential || blindedPublicKey)
```

Podpověření je zahrnuto do procesů odvození klíčů níže, což váže tyto
klíče ke znalosti veřejného klíče pro podepisování Cíle.

#### Šifrování vrstvy 1
Nejprve je připraven vstup do procesu odvození klíče:

```text
outerInput = subcredential || publishedTimestamp
```

Dále je generována náhodná sůl:

```text
outerSalt = CSRNG(32)
```

Poté je odvozen klíč použitý k zašifrování vrstvy 1:

```text
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
  outerKey = keys[0:31]
  outerIV = keys[32:43]
```

Nakonec je prostý text vrstvy 1 zašifrován a serializován:

```text
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```

#### Dešifrování vrstvy 1
Sůl je analyzována z šifrového textu vrstvy 1:

```text
outerSalt = outerCiphertext[0:31]
```

Poté je odvozen klíč použitý k zašifrování vrstvy 1:

```text
outerInput = subcredential || publishedTimestamp
  keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
  outerKey = keys[0:31]
  outerIV = keys[32:43]
```

Nakonec je šifrový text vrstvy 1 dešifrován:

```text
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```

#### Šifrování vrstvy 2
Když je povoleno ověřování klienta, ``authCookie`` je vypočítáno jak je popsáno níže.
Když je ověřování klienta zakázáno, ``authCookie`` je prázdné pole bajtů.

Šifrování pokračuje podobně jako u vrstvy 1:

```text
innerInput = authCookie || subcredential || publishedTimestamp
  innerSalt = CSRNG(32)
  keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
  innerKey = keys[0:31]
  innerIV = keys[32:43]
  innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```

#### Dešifrování vrstvy 2
Když je povoleno ověřování klienta, ``authCookie`` je vypočítáno jak je popsáno níže.
Když je ověřování klienta zakázáno, ``authCookie`` je prázdné pole bajtů.

Dešifrování pokračuje podobně jako u vrstvy 1:

```text
innerInput = authCookie || subcredential || publishedTimestamp
  innerSalt = innerCiphertext[0:31]
  keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
  innerKey = keys[0:31]
  innerIV = keys[32:43]
  innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```


### Autorizace pro konkrétního klienta

Když je pro Cíl povolena autorizace klienta, server udržuje seznam
klientů, které opravňuje k dešifrování dat šifrovaného LS2. Data uložená pro každého klienta
závisí na mechanismu autorizace a zahrnují nějaký druh materiálu klíče, který každý
klient generuje a posílá serveru prostřednictvím bezpečného out-of-band mechanismu.

Existují dvě alternativy pro implementaci autorizace pro konkrétního klienta:

#### Autorizace klienta DH
Každý klient generuje pár klíčů DH ``[csk_i, cpk_i]`` a pošle veřejný klíč ``cpk_i``
serveru.

Zpracování serveru
^^^^^^^^^^^^^^^^^
Server generuje nové ``authCookie`` a dočasný pár klíčů DH:

```text
authCookie = CSRNG(32)
  esk = GENERATE_PRIVATE()
  epk = DERIVE_PUBLIC(esk)
```

Pak pro každého oprávněného klienta server zašifruje ``authCookie`` na jeho veřejný klíč:

```text
sharedSecret = DH(esk, cpk_i)
  authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
  okm = HKDF(epk, authInput, "ELS2_XCA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
  clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```

Server umístí každou dvojici ``[clientID_i, clientCookie_i]`` do vrstvy 1
šifrovaného LS2, spolu s ``epk``.

Zpracování klienta
^^^^^^^^^^^^^^^^^
Klient použije svůj soukromý klíč k odvození očekávaného identifikátoru klienta ``clientID_i``,
šifrovacího klíče ``clientKey_i`` a IV šifrování ``clientIV_i``:

```text
sharedSecret = DH(csk_i, epk)
  authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
  okm = HKDF(epk, authInput, "ELS2_XCA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
```

Pak klient vyhledá v datech autorizace vrstvy 1 položku obsahující
``clientID_i``. Pokud existuje shodná položka, klient ji dešifruje a získá
``authCookie``:

```text
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```

#### Autorizace klienta s předem sdíleným klíčem
Každý klient generuje tajný 32bajtový klíč ``psk_i`` a pošle ho serveru.
Alternativně může server vygenerovat tajný klíč a poslat ho jednomu nebo více klientům.


Zpracování serveru
^^^^^^^^^^^^^^^^^
Server generuje nové ``authCookie`` a sůl:

```text
authCookie = CSRNG(32)
  authSalt = CSRNG(32)
```

Pak pro každého oprávněného klienta server zašifruje ``authCookie`` na jeho předem sdílený klíč:

```text
authInput = psk_i || subcredential || publishedTimestamp
  okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
  clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```

Server umístí každou dvojici ``[clientID_i, clientCookie_i]`` do vrstvy 1
šifrovaného LS2, spolu s ``authSalt``.

Zpracování klienta
^^^^^^^^^^^^^^^^^
Klient použije svůj předem sdílený klíč k odvození očekávaného identifikátoru klienta ``clientID_i``,
šifrovacího klíče ``clientKey_i`` a IV šifrování ``clientIV_i``:

```text
authInput = psk_i || subcredential || publishedTimestamp
  okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
```

Pak klient vyhledá v datech autorizace vrstvy 1 položku obsahující
``clientID_i``. Pokud existuje shodná položka, klient ji dešifruje a získá
``authCookie``:

```text
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```

#### Bezpečnostní úvahy
Oba výše uvedené mechanismy autorizace klienta poskytují soukromí pro členství klientů.
Entita, která zná pouze Cíl, může vidět, kolik klientů je přihlášeno v daném okamžiku, ale nemůže sledovat, kteří klienti jsou přidáváni nebo odvoláváni.

Servery by měly každým generováním šifrovaného LS2 náhodně změnit pořadí klientů, aby
zabránily klientům zjistit jejich pozici v seznamu a odvodit, kdy byli přidáni nebo odvoláni jiní klienti.

Server může zvolit skrytí počtu přihlášených klientů vložením náhodných položek do seznamu autorizačních dat.

Výhody autorizace klienta DH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Bezpečnost schématu nezávisí výhradně na out-of-band výměně materiálu klíče klienta. Soukromý klíč klienta nikdy nemusí opustit jejich zařízení, a tak protivník, který může zachytit out-of-band výměnu, ale nemůže prolomit algoritmus DH, nemůže dešifrovat šifrovaný LS2, ani určit, jak dlouho má klient přístup.

Nevýhody autorizace klienta DH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Vyžaduje N + 1 operací DH na straně serveru pro N klientů.
- Vyžaduje jednu operaci DH na straně klienta.
- Vyžaduje, aby klient vygeneroval tajný klíč.

Výhody autorizace klienta PSK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Nevyžaduje žádné operace DH.
- Umožňuje serveru generovat tajný klíč.
- Umožňuje serveru sdílet stejný klíč s více klienty, pokud je to žádoucí.

Nevýhody autorizace klienta PSK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Bezpečnost schématu je kriticky závislá na out-of-band výměně materiálu klíče klienta. Protivník, který zachytí výměnu pro konkrétního klienta, může dešifrovat jakýkoli následný šifrovaný LS2, pro který je klient oprávněn, stejně jako určit, kdy je přístup klienta odvolán.


### Šifrovaný LS s adresami Base 32

Viz ná
