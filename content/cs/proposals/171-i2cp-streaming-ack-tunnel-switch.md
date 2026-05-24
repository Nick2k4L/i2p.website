---
title: "Příznak I2CP pro přepínání odchozích tunelů"
number: "171"
author: "onon, eyedeekay"
created: "2026-05-19"
lastupdated: "2026-05-23"
status: "Návrh"
toc: true
---

## Přehled

Připojení streamovacího klienta se mohou zaseknout, pokud jsou potvrzení doručení ztracena beze zbytku. Odesílatel znovu přenáší data, dokud nedostane potvrzení nebo dokud není připojení ukončeno, přičemž neexistuje spolehlivý způsob, jak ověřit, že potvrzení dosahují druhé strany. Tento návrh přidává jeden nový příznakový bit do pole příznaků [SendMessageExpiresMessage](/docs/specs/i2cp/), aby klient mohl směrovači přikázat, aby pro následující zprávy na stejný cíl zvolil jiný odchozí tunel. Streamovací protokol tento bit využívá k aktivaci přepnutí tunelu při detekci zaseklého připojení.

## Spouštěče

Dvě podmínky by měly vést k tomu, že klient nastaví příznak u další odchozí zprávy. Tyto podmínky jsou vyhodnocovány na úrovni streamovací vrstvy.

**Strana odesílatele**

V rámci aktuálního časového limitu opakovaného přenosu klienta nebylo přijato žádné potvrzení.

**Strana příjemce**

Přijímač zaznamenal, že vzdálená strana více než jednou znovu přenáší stejná data, což naznačuje, že jeho potvrzení nedosahují k vzdálené straně. Přijímač by měl tuto příznakovou bitu nastavit ve své další odchozí zprávě I2CP, aby potvrzení dorazila k vzdálené straně po jiné cestě. Přijímač MUSÍ počkat, dokud: (1) nedostane duplicitní data, (2) neodeslal alespoň jedno potvrzení a (3) vzdálená strana znovu znovu nepřenese data, než bitu nastaví.

Aby se omezily útoky na základě korelace časování, klient NESMÍ nastavit příznak více než jednou za 10sekundové okno na jedno spojení. Klient by měl také zpozdit nastavení příznaku o náhodnou dobu vybranou rovnoměrně z intervalu `[0, min(T/4, 2000ms)]`, kde T je aktuální časový limit opakovaného přenosu klienta v milisekundách, po detekci stavu zácpy, čímž se sníží přesnost korelace časování.

## Specifikace

Pole příznaků zprávy [SendMessageExpiresMessage](/docs/specs/i2cp/) zabírá horní 2 byty po poli Datum (předefinováno od verze 0.8.4) a je přenášeno v big-endian formátu. Bit 15 je aktuálně nepoužíván; tento návrh jej definuje.

Pořadí bitů: 15...0

| Bit | Název | Popis |
|-----|------|-------------|
| 15 | SWITCH_OUTBOUND_TUNNEL | Pokud je nastaven na 1, měl by router vybrat jiný odchozí tunel ze své skupiny pro následující zprávy určené tomuto cíli. Pokud není k dispozici žádný alternativní tunel, je tento příznak ignorován. Router NESMÍ uzavřít ani vyřadit dříve použitý tunel pouze proto, že byl tento příznak nastaven. |
Tento příznak má výchozí hodnotu 0. Směrovače, které jej neimplementují, jej musí bez chyby ignorovat.

## Poznámky k implementaci

Když je nastaveno `SWITCH_OUTBOUND_TUNNEL`, měl by směrovač náhodně a rovnoměrně vybrat tunel z výstupního fondu, s výjimkou:

- tunel aktuálně používaný pro tuto relaci a
- jeden nejnověji selhalý tunel v poolu, pokud existuje.

Všechny ostatní metriky výkonnosti tunelu, doby sestavení nebo historie výběru NESMĚJÍ ovlivňovat výběr, protože vážený výběr by mohl upřednostňovat sybil útočníky. Pokud po těchto vyloučeních neobsahuje fond žádný způsobilý tunel, příznak je beze slova ignorován.

Tento příznak nezpůsobuje žádné další zprávy tunelů; přepínání tunelů může změnit zdánlivou latenci. Časový limit 10 sekund na připojení (viz Spouštěče) brání nadměrnému přepínání.

## Úvahy o anonymitě

Příznaky v [SendMessageExpiresMessage](/docs/specs/i2cp/) jsou přenášeny přes I2CP, což je místní rozhraní mezi klientem a jeho vlastním směrovačem. Nejsou viditelné pro pozorovatele sítě.

Riziko anonymity je založeno na vzorcích provozu: útočník s viditelností napříč více koncovými body tunelu může pozorovat, *kdy* dochází ke změnám využití tunelu.

Přepínání odchozích tunelů jako přímá reakce na zastavení na straně klienta vytváří detekovatelný chovací vzor. Existují dva konkrétní vektory pozorování:

**Sybilův útok na první skoky odchozích tunelů**

První skok každé odchozí tunely vidí veškerý provoz vstupující do této tunely z routeru odesílatele. Útočník, který ovládá první skok více než jedné tunely v sadě odesílatele, může pozorovat, že provoz na jednom prvním skoku ustává a na jiném začíná téměř současně, čímž obě tunely propojí se stejným odesílatelem. Při sadě N tunelů má útočník ovládající K prvních skoků pravděpodobnost K/N, že pozoruje libovolnou konkrétní událost přepnutí tunelu.

**Časování mezery v provozu**

Během zácpy klient neposílá nová data, takže starý odchozí tunel ztichne. Když dojde ke přepnutí, provoz pokračuje po jiné cestě. Útočník, který má výhodnou pozici u směrovače odesílatele – například poskytovatel sítě odesílatele nebo samotný první uzel cesty – může pozorovat vzorec ticha následovaného obnovením provozu. Délka přestávky navíc prozrazuje přibližnou hodnotu časového limitu opakovaného přenosu klienta.

Klienti MUSÍ dodržovat požadavky na omezení rychlosti a rozptyl definované v Triggers.

## Odkazy

- [Specifikace I2CP](/docs/specs/i2cp/)
