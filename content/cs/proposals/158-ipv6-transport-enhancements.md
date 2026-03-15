---
title: "Vylepšení přenosu IPv6"
aliases:
  - "/cs/spec/proposals/158"
  - "/cs/spec/proposals/158/"
number: "158"
author: "zzz, původní"
created: "2021-03-19"
lastupdated: "2021-04-26"
status: "Uzavřeno"
thread: "http://zzz.i2p/topics/3060"
target: "0.9.50"
toc: true
---
## Poznámka
Nasazení sítě a testování probíhá.
Předmět malých revizí.


## Přehled

Tento návrh má za cíl implementovat vylepšení přenosů SSU a NTCP2 pro IPv6.


## Motivace

Jak roste využití IPv6 po celém světě a nastavení pouze s IPv6 (zejména na mobilních zařízeních) se stávají běžnějšími,
musíme zlepšit podporu IPv6 a odstranit předpoklady, že
všechny směrovače jsou schopné IPv4.



### Kontrola připojení

Při výběru peerů pro tunely nebo při výběru cest OBEP/IBGW pro směrování zpráv
je užitečné zjistit, zda směrovač A dokáže navázat spojení se směrovačem B.
Obecně to znamená určit, zda A má výstupní schopnost pro přenos a typ adresy (IPv4/v6),
který odpovídá jedné z příchozích adres inzerovaných B.

V mnoha případech však neznáme schopnosti A a musíme dělat předpoklady.
Pokud je A skrytý nebo za firewallem, adresy nejsou zveřejněny a nemáme přímé znalosti –
tak předpokládáme, že je schopný IPv4, ale ne IPv6.
Řešením je přidání dvou nových „schopností“ (caps) do informací o směrovači, které označí výstupní schopnost pro IPv4 a IPv6.


### IPv6 Introduktoři

Naše specifikace pro SSU obsahují chyby a nesrovnalosti ohledně toho, zda
jsou pro IPv4 úvodky podporovány IPv6 introduktoři.
V každém případě to nikdy nebylo implementováno ani v Java I2P, ani v i2pd.
To je třeba napravit.


### IPv6 Úvodky

Naše specifikace pro SSU jasně uvádějí, že
IPv6 úvodky nejsou podporovány.
To bylo založeno na předpokladu, že IPv6 nikdy není za firewallem.
To zjevně není pravda a potřebujeme zlepšit podporu směrovačů IPv6 za firewallem.


### Diagramy úvodků

Legenda: ----- je IPv4, ====== je IPv6

**Aktuální pouze IPv4:**

```
        Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**IPv4 úvodka, IPv6 introduktor:**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**IPv6 úvodka, IPv6 introduktor:**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```

**IPv6 úvodka, IPv4 introduktor:**

```
Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```


## Návrh

Budou implementovány tři změny.

- Přidání schopností „4“ a „6“ do schopností adresy směrovače pro indikaci výstupní podpory IPv4 a IPv6
- Přidání podpory pro IPv4 úvodky přes IPv6 introduktory
- Přidání podpory pro IPv6 úvodky přes IPv4 a IPv6 introduktory



## Specifikace

### Schopnosti 4/6

Toto bylo původně implementováno bez formálního návrhu, ale je to vyžadováno pro
IPv6 úvodky, proto to zde zahrnujeme.

Jsou definovány dvě nové schopnosti „4“ a „6“.
Tyto nové schopnosti budou přidány do vlastnosti „caps“ v adrese směrovače, nikoli do schopností v informacích o směrovači.
Momentálně nemáme pro NTCP2 definovanou vlastnost „caps“.
Adresa SSU s introduktory je aktuálně podle definice ipv4. Podporu ipv6 úvodků vůbec nemáme.
Tento návrh je však kompatibilní s IPv6 úvodkami. Viz níže.

Navíc směrovač může podporovat připojení přes overlay síť, jako je I2P-přes-Yggdrasil,
ale nemá zájem zveřejnit adresu, nebo tato adresa nemá standardní formát IPv4 nebo IPv6.
Nový systém schopností by měl být dostatečně flexibilní, aby podporoval i tyto sítě.

Definujeme následující změny:

NTCP2: Přidání vlastnosti „caps“

SSU: Přidání podpory pro adresu směrovače bez hostitele nebo introduktorů, pro indikaci výstupní podpory
pro IPv4, IPv6, nebo obojí.

Oba přenosy: Definujeme následující hodnoty schopností:

- „4“: podpora IPv4
- „6“: podpora IPv6

V jedné adrese může být podporováno více hodnot. Viz níže.
Alespoň jedna z těchto schopností je povinná, pokud není v adrese směrovače zahrnuta hodnota „host“.
Nejvýše jedna z těchto schopností je volitelná, pokud je v adrese směrovače zahrnuta hodnota „host“.
V budoucnu mohou být definovány další schopnosti přenosu pro indikaci podpory overlay sítí nebo jiné konektivity.


#### Případy použití a příklady

SSU:

SSU s hostitelem: 4/6 volitelné, nikdy více než jedno.
Příklad: SSU caps="4" host="1.2.3.4" key=... port="1234"

SSU pouze výstupní pro jedno, druhé je zveřejněno: Pouze schopnosti, 4/6.
Příklad: SSU caps="6"

SSU s introduktory: nikdy kombinováno. Vyžadováno 4 nebo 6.
Příklad: SSU caps="4" iexp0=... ihost0=... iport0=... itag0=... key=...

SSU skrytý: Pouze schopnosti, 4, 6, nebo 46. Více je povoleno.
Není potřeba dvou adres, jedné s 4 a jedné s 6.
Příklad: SSU caps="46"

NTCP2:

NTCP2 s hostitelem: 4/6 volitelné, nikdy více než jedno.
Příklad: NTCP2 caps="4" host="1.2.3.4" i=... port="1234" s=... v="2"

NTCP2 pouze výstupní pro jedno, druhé je zveřejněno: Pouze caps, s, v, 4/6/y, více je povoleno.
Příklad: NTCP2 caps="6" i=... s=... v="2"

NTCP2 skrytý: Pouze caps, s, v, 4/6, více je povoleno. Není potřeba dvou adres, jedné s 4 a jedné s 6.
Příklad: NTCP2 caps="46" i=... s=... v="2"



### IPv6 Introduktoři pro IPv4

Následující změny jsou vyžadovány k opravě chyb a nesrovnalostí ve specifikacích.
Toto jsme také popsali jako „část 1“ návrhu.

#### Změny specifikace

SSU specifikace aktuálně uvádí (poznámky k IPv6):

IPv6 je podporováno od verze 0.9.8. Zveřejněné relé adresy mohou být IPv4 nebo IPv6 a komunikace Alice-Bob může probíhat přes IPv4 nebo IPv6.

Přidejte následující:

I když byla specifikace změněna od verze 0.9.8, komunikace Alice-Bob přes IPv6 nebyla ve skutečnosti podporována až do verze 0.9.50.
Starší verze Java směrovačů chybně zveřejňovaly schopnost 'C' pro IPv6 adresy,
i když ve skutečnosti jako introduktor přes IPv6 nesloužily.
Proto by směrovače měly důvěřovat schopnosti 'C' na IPv6 adrese pouze v případě, že verze směrovače je 0.9.50 nebo vyšší.



SSU specifikace aktuálně uvádí (Relay Request):

IP adresa je zahrnuta pouze v případě, že se liší od zdrojové adresy a portu paketu.
V aktuální implementaci je délka IP vždy 0 a port je vždy 0,
a příjemce by měl použít zdrojovou adresu a port paketu.
Tato zpráva může být odeslána přes IPv4 nebo IPv6. Pokud IPv6, Alice musí zahrnout svou IPv4 adresu a port.

Přidejte následující:

IP adresa a port musí být zahrnuty pro úvod IPv4 adresy při odesílání této zprávy přes IPv6.
Toto je podporováno od verze 0.9.50.



### IPv6 Úvodky

Všechny tři SSU relé zprávy (RelayRequest, RelayResponse a RelayIntro) obsahují pole délky IP
pro indikaci délky (Alice, Bob nebo Charlie) IP adresy, která následuje.

Proto není vyžadována žádná změna formátu zpráv.
Vyžadují se pouze textové změny ve specifikacích, které uvádějí, že jsou povoleny 16bytové IP adresy.

Následující změny jsou vyžadovány ve specifikacích.
Toto jsme také popsali jako „část 2“ návrhu.


#### Změny specifikace

SSU specifikace aktuálně uvádí (poznámky k IPv6):

Komunikace Bob-Charlie a Alice-Charlie probíhá pouze přes IPv4.

SSU specifikace aktuálně uvádí (Relay Request):

Nejsou plánovány žádné implementace relé pro IPv6.

Změňte na:

Relé pro IPv6 je podporováno od verze 0.9.xx

SSU specifikace aktuálně uvádí (Relay Response):

IP adresa Charlieho musí být IPv4, protože to je adresa, na kterou Alice po Hole Punch pošle SessionRequest.
Nejsou plánovány žádné implementace relé pro IPv6.

Změňte na:

IP adresa Charlieho může být IPv4 nebo, od verze 0.9.xx, IPv6.
To je adresa, na kterou Alice po Hole Punch pošle SessionRequest.
Relé pro IPv6 je podporováno od verze 0.9.xx

SSU specifikace aktuálně uvádí (Relay Intro):

IP adresa Alice je v aktuální implementaci vždy 4 byty, protože Alice se snaží připojit k Charliemu přes IPv4.
Tato zpráva musí být odeslána přes navázané IPv4 spojení,
protože to je jediný způsob, jak Bob získá IPv4 adresu Charlieho, kterou vrátí Alici v RelayResponse.

Změňte na:

Pro IPv4 je IP adresa Alice vždy 4 byty, protože Alice se snaží připojit k Charliemu přes IPv4.
Od verze 0.9.xx je podporováno IPv6 a IP adresa Alice může být 16 bytů.

Pro IPv4 musí být tato zpráva odeslána přes navázané IPv4 spojení,
protože to je jediný způsob, jak Bob získá IPv4 adresu Charlieho, kterou vrátí Alici v RelayResponse.
Od verze 0.9.xx je podporováno IPv6 a tato zpráva může být odeslána přes navázané IPv6 spojení.

Přidejte také:

Od verze 0.9.xx musí být každá SSU adresa zveřejněná s introduktory obsahovat „4“ nebo „6“ ve volbě „caps“.


## Migrace

Všechny staré směrovače by měly ignorovat vlastnost caps v NTCP2 a neznámé znaky schopností ve vlastnosti caps SSU.

Každá SSU adresa s introduktory, která neobsahuje schopnost „4“ nebo „6“, se považuje za úvodku pro IPv4.


## Reference

* [CAPS](http://zzz.i2p/topics/3050)
* [NTCP2](/docs/specs/ntcp2/)
* [SSU](/docs/specs/ssu2/)
* [SSU-SPEC](/docs/legacy/ssu/)
