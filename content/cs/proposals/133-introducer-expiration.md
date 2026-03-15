---
title: "Vypršení platnosti zaváděče"
number: "133"
author: "zzz"
created: "2017-02-05"
lastupdated: "2017-08-09"
status: "Uzavřeno"
thread: "http://zzz.i2p/topics/2230"
target: "0.9.30"
implementedin: "0.9.30"
toc: true
---
## Přehled

Tento návrh se týká zlepšení úspěšnosti úvodů.


## Motivace

Úvodci po určité době vyprší, ale tato informace není zveřejněna v informacích o směrovači (Router Info). Směrovače aktuálně musí používat heuristiku k odhadu, kdy již úvodce není platný.


## Návrh

Ve směrovačové adrese SSU obsahující úvodce může vydavatel volitelně uvést čas vypršení platnosti pro každého úvodce.


## Specifikace

```
iexp{X}={nnnnnnnnnn}

X :: Číslo úvodce (0-2)

nnnnnnnnnn :: Čas v sekundách (nikoli ms) od počátku epochy.
```

### Poznámky

* Každé vypršení musí být větší než datum publikování informací o směrovači (Router Info) a menší než 6 hodin po datu publikování informací o směrovači.

* Směrovače a úvodci by měli usilovat o udržení platnosti úvodce až do vypršení, avšak nemají způsob, jak to zaručit.

* Směrovače by neměly používat publikovaného úvodce po uplynutí jeho platnosti.

* Vypršení platnosti úvodců je součástí mapování směrovačové adresy (Router Address). Nejedná se o (nyní nepoužívané) 8bytové pole vypršení v rámci směrovačové adresy.

**Příklad:** `iexp0=1486309470`


## Migrace

Žádné problémy. Implementace je volitelná.
Zpětná kompatibilita je zajištěna, protože starší směrovače budou ignorovat neznámé parametry.


## Reference

* [RouterAddress](/docs/specs/common-structures/#routeraddress)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TRAC-TICKET](http://trac.i2p2.i2p/ticket/1352)
