---
title: "Nová šablona návrhu šifrování"
aliases:
  - "/cs/proposals/142-ecies-template"
  - "/cs/proposals/142-ecies-template/"
number: "142"
author: "zzz"
created: "2018-01-11"
lastupdated: "2018-01-20"
status: "Meta"
thread: "http://zzz.i2p/topics/2499"
toc: true
---
## Přehled

Tento dokument popisuje důležité otázky, které je třeba zvážit při navrhování
náhrady nebo doplnění naší asymetrické šifry ElGamal.

Toto je dokument informačního charakteru.


## Motivace

ElGamal je starý a pomalý, a existují lepší alternativy.
Existuje však několik problémů, které je nutné vyřešit, než budeme moci přidat nebo přejít na jakýkoli nový algoritmus.
Tento dokument tyto nevyřešené otázky zdůrazňuje.



## Předběžný výzkum

Každý, kdo navrhuje novou kryptografii, musí být nejprve obeznámen s následujícími dokumenty:

- [Návrh 111 NTCP2](/proposals/111-ntcp-2/)
- [Návrh 123 LS2](/proposals/123-new-netdb-entries/)
- [Návrh 136 experimentální typy podpisů](/proposals/136-experimental-sigtypes/)
- [Návrh 137 volitelné typy podpisů](/proposals/137-optional-sigtypes/)
- Diskusní vlákna zde pro každý z výše uvedených návrhů, odkazovaná uvnitř
- [Priority návrhů z roku 2018](http://zzz.i2p/topics/2494)
- [Návrh ECIES](http://zzz.i2p/topics/2418)
- [Přehled nové asymetrické kryptografie](http://zzz.i2p/topics/1768)
- [Přehled nízkoúrovňové kryptografie](/docs/specs/common-structures/)


## Použití asymetrické kryptografie

Pro připomenutí, ElGamal používáme pro:

1) Zprávy pro stavbu tunelu (klíč je v RouterIdentity)

2) Šifrování mezi směrovači pro netDb a další I2NP zprávy (Klíč je v RouterIdentity)

3) End-to-end ElGamal+AES/SessionTag na straně klienta (klíč je v LeaseSet, klíč Destination se nepoužívá)

4) Dočasné DH pro NTCP a SSU


## Návrh

Každý návrh na nahrazení ElGamalu jiným algoritmem musí obsahovat následující podrobnosti.



## Specifikace

Každý návrh nové asymetrické kryptografie musí plně specifikovat následující položky.



### 1. Obecné

Ve svém návrhu odpovězte na následující otázky. Vezměte v úvahu, že to může být nutné zpracovat jako samostatný návrh oddělený od konkrétních bodů v části 2) níže, protože by mohl kolidovat s existujícími návrhy 111, 123, 136, 137 nebo jinými.

- Pro které z výše uvedených případů 1–4 navrhujete použití nové kryptografie?
- Pokud pro 1) nebo 2) (směrovač), kam bude veřejný klíč umístěn – do RouterIdentity nebo do vlastností RouterInfo? Máte v úmyslu použít typ kryptografie v certifikátu klíče? Plně specifikujte. Oba případy zdůvodněte.
- Pokud pro 3) (klient), máte v úmyslu uložit veřejný klíč v cíli a použít typ kryptografie v certifikátu klíče (jako v návrhu ECIES), nebo jej uložit v LS2 (jako v návrhu 123), nebo něco jiného? Plně specifikujte a své rozhodnutí zdůvodněte.
- Pro všechna použití – jak bude podpora inzerovala? Pokud pro 3), bude to v LS2 nebo jinde? Pokud pro 1) a 2), bude to podobné jako v návrzích 136 a/nebo 137? Plně specifikujte a svá rozhodnutí zdůvodněte. Pravděpodobně bude potřeba samostatný návrh pro tuto část.
- Plně specifikujte, jak a proč je toto zpětně kompatibilní, a podrobně popište plán migrace.
- Které nerealizované návrhy jsou předpoklady pro váš návrh?


### 2. Konkrétní typ kryptografie

Ve svém návrhu odpovězte na následující otázky:

- Obecné informace o kryptografii, konkrétní křivky/parametry, plně zdůvodněte svou volbu. Uveďte odkazy na specifikace a další informace.
- Výsledky testů rychlosti ve srovnání s ElGamalem a dalšími alternativami, pokud jsou k dispozici. Zahrňte šifrování, dešifrování a generování klíčů.
- Dostupnost knihoven v C++ a Javě (OpenJDK, BouncyCastle i třetí strany)
  Pro třetí strany nebo ne-Java knihovny uveďte odkazy a licence
- Navrhované číslo(a) kryptografického typu (v experimentálním rozsahu nebo nikoli)




## Poznámky
