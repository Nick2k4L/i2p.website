---
title: "Neviditelný Multihoming"
number: "140"
author: "str4d"
created: "2017-05-22"
lastupdated: "2017-07-04"
status: "Otevřít"
thread: "http://zzz.i2p/topics/2335"
toc: true
---
## Přehled

Tento návrh popisuje návrh protokolu umožňujícího klientovi I2P, službě
nebo externímu procesu vyrovnávání zatížení spravovat více směrovačů transparentně hostujících jedinou [Destination](/docs/specs/common-structures/#destination).

Návrh aktuálně nespecifikuje konkrétní implementaci. Může být
implementován jako rozšíření [I2CP](/docs/specs/i2cp/), nebo jako nový protokol.


## Motivace

Multihoming znamená použití více směrovačů k hostování stejné Destination.
Současný způsob multihomingu s I2P spočívá v běhu stejné Destination na každém
směrovači nezávisle; směrovač, který je v daném okamžiku používán klienty, je ten,
který naposledy publikoval LeaseSet.

Toto je hack a pravděpodobně nebude fungovat pro velké weby ve velkém měřítku. Řekněme, že máme
100 multihomingových směrovačů, každý s 16 tunely. To je 1600 publikací LeaseSetu
každých 10 minut, tedy téměř 3 za sekundu. Floodfill uzly by byly zahlceny
a zapnuly by se omezení. A to ještě ani nebyla zmíněna provoz spojený s vyhledáváním.

Návrh 123 tento problém řeší pomocí meta-LeaseSetu, který obsahuje seznam 100 reálných
hashů LeaseSetu. Vyhledání se stává dvoustupňovým procesem: nejprve vyhledání meta-LeaseSetu a poté jednoho z pojmenovaných LeaseSetů. Toto je dobré řešení problému s provozem při vyhledávání, ale samo o sobě vytváří významnou díru v soukromí:
Je možné zjistit, které multihomingové směrovače jsou online sledováním publikovaného meta-LeaseSetu, protože každý reálný LeaseSet odpovídá jedinému směrovači.

Potřebujeme způsob, jak umožnit klientovi nebo službě I2P rozprostřít jednu Destination přes
více směrovačů tak, aby to bylo z hlediska LeaseSetu nerozeznatelné od použití jediného směrovače.


## Návrh

### Definice

    Uživatel
        Osoba nebo organizace, která chce provozovat multihoming svých Destination. Zde je uvažována jediná Destination obecně (WLOG).

    Klient
        Aplikace nebo služba běžící za Destination. Může se jednat o klientskou, serverovou nebo peer-to-peer aplikaci; označujeme ji jako
        klienta ve smyslu, že se připojuje ke směrovačům I2P.

        Klient se skládá ze tří částí, které mohou být všechny ve stejném procesu
        nebo mohou být rozděleny mezi procesy či stroje (v multi-klientském nastavení):

        Vyvažovač (Balancer)
            Část klienta, která spravuje výběr peerů a stavbu tunelů. V daném okamžiku existuje pouze jeden vyvažovač a komunikuje se všemi směrovači I2P. Může existovat záložní vyvažovač.

        Frontend
            Část klienta, která může být provozována paralelně. Každý frontend komunikuje s jedním směrovačem I2P.

        Backend
            Část klienta, která je sdílena mezi všemi frontendy. Nemá přímou komunikaci se žádným směrovačem I2P.

    Směrovač (Router)
        Směrovač I2P provozovaný uživatelem, který se nachází na hranici mezi sítí I2P a sítí uživatele (podobně jako hraniční zařízení v firemních
        sítích). Staví tunely na základě příkazů vyvažovače a směruje pakety pro klienta nebo frontend.

### Celkový přehled

Představme si následující požadovanou konfiguraci:

- Klientská aplikace s jednou Destination.
- Čtyři směrovače, každý spravující tři příchozí tunely.
- Všech dvanáct tunelů by mělo být publikováno v jednom LeaseSetu.

### Single-client

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]-----
                 |-{ [Tunnel 3]===/               \
                 |                                 \
                 |-{ [Tunnel 4]===\                 \
  [Destination]  |-{ [Tunnel 5]====[Router 2]-----   \
    \            |-{ [Tunnel 6]===/               \   \
     [LeaseSet]--|                               [Client]
                 |-{ [Tunnel 7]===\               /   /
                 |-{ [Tunnel 8]====[Router 3]-----   /
                 |-{ [Tunnel 9]===/                 /
                 |                                 /
                 |-{ [Tunnel 10]==\               /
                 |-{ [Tunnel 11]===[Router 4]-----
                  -{ [Tunnel 12]==/
```

### Multi-client

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]---------[Frontend 1]
                 |-{ [Tunnel 3]===/          \                    \
                 |                            \                    \
                 |-{ [Tunnel 4]===\            \                    \
  [Destination]  |-{ [Tunnel 5]====[Router 2]---\-----[Frontend 2]   \
    \            |-{ [Tunnel 6]===/          \   \                \   \
     [LeaseSet]--|                         [Balancer]            [Backend]
                 |-{ [Tunnel 7]===\          /   /                /   /
                 |-{ [Tunnel 8]====[Router 3]---/-----[Frontend 3]   /
                 |-{ [Tunnel 9]===/            /                    /
                 |                            /                    /
                 |-{ [Tunnel 10]==\          /                    /
                 |-{ [Tunnel 11]===[Router 4]---------[Frontend 4]
                  -{ [Tunnel 12]==/
```

### Obecný proces klienta

- Načíst nebo vygenerovat Destination.

- Otevřít relaci s každým směrovačem, vázanou k této Destination.

- Pravidelně (asi každých deset minut, ale více či méně podle životnosti tunelů):

  - Získat rychlou úroveň (fast tier) od každého směrovače.

  - Použít nadmnožinu peerů k vytvoření tunelů do/ze každého směrovače.

    - Ve výchozím nastavení budou tunely do/ze směrovače používat peery z
      rychlé úrovně tohoto směrovače, ale protokol to nevynucuje.

  - Shromáždit množinu aktivních příchozích tunelů ze všech aktivních směrovačů a vytvořit LeaseSet.

  - Publikovat LeaseSet přes jeden nebo více směrovačů.

### Rozdíly oproti I2CP

Pro vytvoření a správu této konfigurace potřebuje klient následující nové
funkce nad rámec toho, co je aktuálně poskytováno [I2CP](/docs/specs/i2cp/):

- Říct směrovači, aby postavil tunely, aniž by pro ně vytvářel LeaseSet.
- Získat seznam aktuálních tunelů v příchozím fondu.

Dále by následující funkce umožnily významnou flexibilitu v tom, jak klient spravuje své tunely:

- Získat obsah rychlé úrovně směrovače.
- Říct směrovači, aby postavil příchozí nebo odchozí tunel pomocí daného seznamu
  peerů.

### Náčrt protokolu

```
         Klient                           Směrovač

                    --------------------->  Vytvořit relaci (Create Session)
   Stav relace  <---------------------
                    --------------------->  Získat rychlou úroveň (Get Fast Tier)
        Seznam peerů  <---------------------
                    --------------------->  Vytvořit tunel (Create Tunnel)
    Stav tunelu  <---------------------
                    --------------------->  Získat fond tunelů (Get Tunnel Pool)
      Seznam tunelů  <---------------------
                    --------------------->  Publikovat LeaseSet (Publish LeaseSet)
                    --------------------->  Odeslat paket (Send Packet)
      Stav odeslání  <---------------------
  Přijatý paket  <---------------------
```

### Zprávy

**Create Session**
- Vytvořit relaci pro danou Destination.

**Session Status**
- Potvrzení, že relace byla nastavena a klient může začít stavět tunely.

**Get Fast Tier**
- Požadavek na seznam peerů, které směrovač aktuálně zvažuje pro stavbu tunelů.

**Peer List**
- Seznam peerů známých směrovači.

**Create Tunnel**
- Požadavek, aby směrovač postavil nový tunel přes zadané peery.

**Tunnel Status**
- Výsledek konkrétní stavby tunelu, jakmile je k dispozici.

**Get Tunnel Pool**
- Požadavek na seznam aktuálních tunelů v příchozím nebo odchozím fondu pro tuto Destination.

**Tunnel List**
- Seznam tunelů pro požadovaný fond.

**Publish LeaseSet**
- Požadavek, aby směrovač publikoval poskytnutý LeaseSet přes jeden z odchozích tunelů pro tuto Destination. Není potřeba žádný stav odpovědi; směrovač by měl pokračovat v opakovaném pokusu, dokud nebude spokojen, že LeaseSet byl publikován.

**Send Packet**
- Odchozí paket od klienta. Volitelně určuje odchozí tunel, přes který musí (měl?) být paket odeslán.

**Send Status**
- Informuje klienta o úspěchu či neúspěchu odeslání paketu.

**Packet Received**
- Příchozí paket pro klienta. Volitelně určuje příchozí tunel, přes který byl paket přijat(?)


## Bezpečnostní důsledky

Z pohledu směrovačů je tento návrh funkčně ekvivalentní současnému stavu. Směrovač stále staví všechny tunely, udržuje své vlastní profily peerů a vynucuje oddělení mezi operacemi směrovače a klienta. Ve výchozím nastavení je zcela identický, protože tunely pro daný směrovač jsou stavěny z jeho vlastní rychlé úrovně.

Z pohledu netDB je jeden LeaseSet vytvořený tímto protokolem identický se současným stavem, protože využívá již existující funkce. U větších LeaseSetů se blížících 16 Leaseům však může pozorovatel dozvědět, že LeaseSet je multihomed:

- Současná maximální velikost rychlé úrovně je 75 peerů. Inbound Gateway (IBGW, uzel publikovaný v Lease) je vybírán z části této úrovně (rozdělené náhodně podle hash per fond tunelů, nikoli podle počtu):

      1 skok
          Celá rychlá úroveň

      2 skoky
          Polovina rychlé úrovně
          (výchozí až do poloviny roku 2014)

      3+ skoky
          Čtvrtina rychlé úrovně
          (3 je aktuální výchozí hodnota)

  To znamená, že průměrně budou IBGWy pocházet ze sady 20–30 peerů.

- V jednoduchém nastavení bude plný 16-tunelový LeaseSet mít 16 IBGWů náhodně vybraných ze sady až (řekněme) 20 peerů.

- V 4-směrovačovém multihomed nastavení s výchozím nastavením bude plný
  16-tunelový LeaseSet mít 16 IBGWů náhodně vybraných ze sady maximálně 80 peerů, i když mezi směrovači pravděpodobně bude část společných peerů.

Takže ve výchozím nastavení může být možné statistickou analýzou zjistit, že LeaseSet je generován tímto protokolem. Může být také možné zjistit, kolik směrovačů je použito, i když efekt rotace na rychlých úrovních by snížil účinnost této analýzy.

Protože klient má plnou kontrolu nad tím, které peery vybírá, může být tento únik informací snížen nebo eliminován výběrem IBGWů z omezené sady peerů.


## Kompatibilita

Tento návrh je zcela zpětně kompatibilní se sítí, protože nejsou provedeny žádné změny ve formátu LeaseSetu. Všichni směrovači by museli znát nový protokol, ale to není problém, protože by všichni byli řízeni stejnou entitou.


## Poznámky k výkonu a škálovatelnosti

Horní limit 16 Leaseů na LeaseSet tímto návrhem zůstává nezměněn. Pro Destination, které vyžadují více tunelů, existují dvě možné síťové úpravy:

- Zvýšit horní limit velikosti LeaseSetů. To by bylo nejjednodušší na implementaci (i když by stále vyžadovalo rozsáhlou podporu sítě, než by mohlo být široce použito), ale mohlo by vést ke zpomalení vyhledávání kvůli větším velikostem paketů. Maximální realizovatelná velikost LeaseSetu je určena MTU podkladových přenosových prostředků a je tedy kolem 16 kB.

- Implementovat Návrh 123 pro hierarchické LeaseSety. V kombinaci s tímto návrhem by mohly být Destination pro dílčí LeaseSety rozprostřeny přes více směrovačů, čímž by efektivně fungovaly jako více IP adres pro clearnetovou službu.


## Poděkování

Děkujeme psi za diskuzi, která vedla k tomuto návrhu.


## Reference

* [Destination](/docs/specs/common-structures/#destination)
* [I2CP](/docs/specs/i2cp/)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [Prop123](/proposals/123-new-netdb-entries/)
