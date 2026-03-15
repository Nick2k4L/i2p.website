---
title: "RI a výplň cíle"
number: "161"
author: "zzz"
created: "2022-09-28"
lastupdated: "2023-01-02"
status: "Otevřeno"
thread: "http://zzz.i2p/topics/3279"
target: "0.9.57"
toc: true
---
## Stav

Implementováno ve verzi 0.9.57.  
Ponecháváme tuto navrženou změnu otevřenou, abychom mohli rozvíjet a diskutovat nápady v části „Plánování do budoucna“.


## Přehled


### Shrnutí

Veřejný klíč ElGamal v Destinacích se nepoužívá od verze 0.6 (2005).  
I když naše specifikace uvádějí, že se nevyužívá, NEuvádějí, že implementace mohou vynechat generování dvojice klíčů ElGamal a pole jednoduše naplnit náhodnými daty.

Navrhujeme změnit specifikace tak, aby bylo uvedeno, že pole je ignorováno a implementace MOHOU pole naplnit náhodnými daty.  
Tato změna je zpětně kompatibilní. Neznáme žádnou implementaci, která by ověřovala veřejný klíč ElGamal.

Navíc tato navržená změna poskytuje implementátorům doporučení, jak generovat náhodná data pro doplňování (padding) v Destinacích a Identitách směrovače (Router Identity), aby byla dobře komprimovatelná, zároveň bezpečná a jejich Base64 reprezentace nevypadala poškozeně nebo nezabezpečeně.  
Tím získáme většinu výhod odstranění polí s doplňováním, aniž bychom museli provádět rušivé změny protokolu.  
Komprimovatelné Destinace snižují velikost streamovacích SYN a replikovatelných datagramů; komprimovatelné Identity směrovače snižují velikost zpráv Database Store, zpráv SSU2 Session Confirmed a souborů reseed su3.

Nakonec navrhovaná změna diskutuje možnosti nových formátů Destinací a Identit směrovače, které by doplňování úplně odstranily.  
Obsahuje také krátkou diskuzi o post-kvantové kryptografii a o tom, jak by to mohlo ovlivnit budoucí plánování.



### Cíle

- Zrušit požadavek na generování dvojice klíčů ElGamal pro Destinace
- Doporučit osvědčené postupy, aby Destinace a Identity směrovače byly vysoce komprimovatelné, ale přitom nevykazovaly zjevné vzory v Base64 reprezentaci
- Podpořit přijetí osvědčených postupů všemi implementacemi, aby byla pole nerozlišitelná
- Snížit velikost streamovacích SYN
- Snížit velikost replikovatelných datagramů
- Snížit velikost bloku RI v SSU2
- Snížit velikost a četnost fragmentace zpráv SSU2 Session Confirmed
- Snížit velikost zpráv Database Store (s RI)
- Snížit velikost souborů reseed
- Zachovat kompatibilitu ve všech protokolech a rozhraních API
- Aktualizovat specifikace
- Diskutovat alternativy pro nové formáty Destinací a Identit směrovače

Zrušením požadavku na generování klíčů ElGamal mohou implementace být schopny kód pro ElGamal úplně odstranit, s ohledem na požadavky na zpětnou kompatibilitu v jiných protokolech.



## Návrh

Přísně vzato, pouze 32bitový veřejný podpisový klíč (v Destinacích i v Identitách směrovače) a 32bitový veřejný šifrovací klíč (pouze v Identitách směrovače) je náhodné číslo, které poskytuje veškerou entropii potřebnou k tomu, aby byly SHA-256 otisky těchto struktur kryptograficky silné a náhodně distribuované v DHT síťové databázi.

Nicméně z důvodu opatrnosti doporučujeme použít minimálně 32 bajtů náhodných dat v poli veřejného klíče ElGamal a v doplňování. Navíc, pokud by byla pole plná nul, Base64 reprezentace Destinací by obsahovala dlouhé sekvence znaků AAAA, což by mohlo uživatelům vyvolat poplach nebo zmatek.

Pro podpisový typ Ed25519 a šifrovací typ X25519:  
Destinace budou obsahovat 11 kopií (352 bajtů) náhodných dat.  
Identity směrovače budou obsahovat 10 kopií (320 bajtů) náhodných dat.



### Odhadované úspory

Destinace jsou zahrnuty ve všech streamovacích SYN a replikovatelných datagramech.  
Informace o směrovači (RI, obsahující Identity směrovače) jsou zahrnuty ve zprávách Database Store a ve zprávách Session Confirmed v NTCP2 a SSU2.

NTCP2 nekomprimuje informace o směrovači.  
RI ve zprávách Database Store a ve zprávách SSU2 Session Confirmed jsou gzipnuty.  
Informace o směrovači jsou zipovány v reseed SU3 souborech.

Destinace ve zprávách Database Store nejsou komprimovány.  
Zprávy streamovacích SYN jsou gzipovány na úrovni I2CP.

Pro podpisový typ Ed25519 a šifrovací typ X25519 odhadované úspory:

| Typ dat | Celková velikost | Klíče a certifikáty | Nekomprimované doplňování | Komprimované doplňování | Velikost | Úspora |
|---------|------------------|---------------------|---------------------------|-------------------------|--------|--------|
| Destinace | 391 | 39 | 352 | 32 | 71 | 320 bajtů (82 %) |
| Identita směrovače | 391 | 71 | 320 | 32 | 103 | 288 bajtů (74 %) |
| Informace o směrovači | 1000 typ. | 71 | 320 | 32 | 722 typ. | 288 bajtů (29 %) |

Poznámky: Předpokládá, že 7bajtový certifikát není komprimovatelný, nulové dodatečné režie gzipu.  
Ani jedno není pravda, ale vliv bude malý.  
Ignoruje ostatní komprimovatelné části informací o směrovači.



## Specifikace

Navrhované změny našich současných specifikací jsou zdokumentovány níže.


### Společné struktury
Změnit specifikaci společných struktur tak, aby bylo uvedeno, že 256bajtové pole veřejného klíče Destinace je ignorováno a může obsahovat náhodná data.

Přidat sekci do specifikace společných struktur s doporučením osvědčeného postupu pro pole veřejného klíče Destinace a pole doplňování v Destinaci a Identitě směrovače, a to následovně:

Vygenerujte 32 bajty náhodných dat pomocí silného kryptografického generátoru pseudonáhodných čísel (PRNG) a opakujte těchto 32 bajtů podle potřeby, aby bylo pole veřejného klíče (pro Destinace) a pole doplňování (pro Destinace a Identity směrovače) naplněno.


### Soubor soukromého klíče
Formát souboru soukromého klíče (eepPriv.dat) není oficiální součástí našich specifikací, ale je zdokumentován v [Java I2P javadoc](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html) a další implementace jej podporují.  
To umožňuje přenositelnost soukromých klíčů mezi různými implementacemi.  
Přidat poznámku do tohoto javadocu, že veřejný šifrovací klíč může být náhodné doplňování a soukromý šifrovací klíč může být plný nul nebo náhodná data.


### SAM
Poznamenat ve specifikaci SAM, že soukromý šifrovací klíč se nepoužívá a může být ignorován.  
Klient může vrátit jakákoli náhodná data.  
SAM Bridge může při vytváření (s DEST GENERATE nebo SESSION CREATE DESTINATION=TRANSIENT) poslat náhodná data místo nul, aby Base64 reprezentace neobsahovala řetězec znaků AAAA a nevypadala poškozeně.


### I2CP
Žádné změny nejsou vyžadovány pro I2CP. Soukromý klíč pro veřejný šifrovací klíč v Destinaci se směrovači neodesílá.


## Plánování do budoucna


### Změny protokolu

Za cenu změn protokolu a ztráty zpětné kompatibility bychom mohli změnit naše protokoly a specifikace tak, aby odstranily pole doplňování v Destinaci, Identitě směrovače, nebo v obou.

Tato navržená změna má určitou podobnost s formátem šifrovaného leasesetu „b33“, který obsahuje pouze klíč a typové pole.

Pro zachování určité kompatibility by některé vrstvy protokolu mohly „rozšířit“ pole doplňování nulami pro prezentaci jiným vrstvám protokolu.

U Destinací bychom mohli také odstranit pole typu šifrování v klíčovém certifikátu, čímž bychom ušetřili dva bajty.  
Alternativně by Destinace mohly získat nový typ šifrování v klíčovém certifikátu, který by indikoval nulový veřejný klíč (a doplňování).

Pokud by konverze mezi starými a novými formáty nebyla zahrnuta na některé vrstvě protokolu, byly by ovlivněny následující specifikace, API, protokoly a aplikace:

- Specifikace společných struktur
- I2NP
- I2CP
- NTCP2
- SSU2
- Ratchet
- Streaming
- SAM
- Bittorrent
- Reseeding
- Soubor soukromého klíče
- Java jádro a směrovačové API
- i2pd API
- Knihovny třetích stran pro SAM
- Balené a třetí strany nástroje
- Několik Java pluginů
- Uživatelská rozhraní
- P2P aplikace např. MuWire, bitcoin, monero
- hosts.txt, addressbook a odběry

Pokud by byla konverze specifikována na některé vrstvě, byl by seznam zkrácen.

Náklady a výhody těchto změn nejsou jasné.

Konkrétní návrhy jsou zatím nedefinovány:





### PQ klíče

Veřejné klíče pro post-kvantové (PQ) šifrování, pro jakýkoli očekávaný algoritmus, jsou větší než 256 bajtů. To by eliminovatlo jakékoli doplňování a jakékoli úspory z navrhovaných změn výše, alespoň pro Identity směrovače.

V „hybridním“ PQ přístupu, jako používá SSL, by PQ klíče byly pouze efemérní a neobjevily by se v Identitě směrovače.

PQ podpisové klíče nejsou životaschopné a Destinace neobsahují veřejné šifrovací klíče.  
Statické klíče pro ratchet jsou v Lease Set, ne v Destinaci.  
Proto můžeme z následující diskuse vyloučit Destinace.

Takže PQ ovlivňuje pouze Informace o směrovači a pouze pro statické (nikoli efemérní) PQ klíče, ne pro hybridní PQ.  
To by bylo pro nový typ šifrování a ovlivnilo by NTCP2, SSU2 a šifrované zprávy Database Lookup a odpovědi.  
Odhadovaný časový rámec pro návrh, vývoj a nasazení by byl ????????  
Ale byl by po hybridním nebo ratchet ????????????

Pro další diskuzi viz [toto téma](http://zzz.i2p/topics/3294).




## Problémy

Může být žádoucí postupně měnit klíče v síti, aby poskytovaly krytí novým směrovačům.  
„Změna klíčů“ by mohla znamenat jednoduše změnu doplňování, ne skutečnou změnu klíčů.

Není možné změnit klíče u stávajících Destinací.

Měly by být Identity směrovače s doplňováním ve veřejném klíčovém poli identifikovány jiným typem šifrování v klíčovém certifikátu? To by způsobilo problémy s kompatibilitou.




## Migrace

Žádné problémy se zpětnou kompatibilitou při nahrazování klíče ElGamal doplňováním.

Změna klíčů, pokud bude implementována, by byla podobná té, která byla provedena při třech předchozích přechodech identit směrovače:  
Od DSA-SHA1 k podpisům ECDSA, poté k podpisům EdDSA a poté k šifrování X25519.

S ohledem na problémy se zpětnou kompatibilitou a po vypnutí SSU mohou implementace kód ElGamal úplně odstranit.  
Přibližně 14 % směrovačů v síti používá šifrovací typ ElGamal, včetně mnoha floodfillů.

Návrh merge requestu pro Java I2P je k dispozici na [git.idk.i2p](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66).


## Reference

* [Common](/docs/specs/common-structures/)
* [Datagram](/docs/api/datagrams/)
* [I2CP](/docs/specs/i2cp/)
* [I2NP](/docs/specs/i2np/)
* [MR](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66)
* [NTCP2](/docs/specs/ntcp2/)
* [PKF](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html)
* [PQ](http://zzz.i2p/topics/3294)
* [SAM](/docs/api/samv3/)
* [SSU2](/docs/specs/ssu2/)
* [Streaming](/docs/specs/streaming/)
