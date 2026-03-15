---
title: "Šifrovaný LeaseSet"
number: "121"
author: "zzz"
created: "2016-01-11"
lastupdated: "2016-01-12"
status: "Zamítnuto"
thread: "http://zzz.i2p/topics/2047"
supercededby: "123"
toc: true
---
## Přehled

Tato návrh se zabývá přepracováním mechanismu pro šifrování LeaseSets.


## Motivace

Současné šifrované LS jsou hrozné a nebezpečné. Mohu to říct, protože jsem je navrhl a implementoval.

Důvody:

- Šifrováno pomocí AES CBC
- Jeden AES klíč pro všechny
- Časové expirace Lease jsou stále přístupné
- Šifrovací pubkey jsou stále přístupné


## Návrh

### Cíle

- Zcela zakrýt celý proces
- Klíče pro každého příjemce


### Strategie

Postupujme stejně jako GPG/OpenPGP. Asymetricky šifrujeme symetrický klíč pro každého příjemce. Data jsou dešifrována pomocí toho asymetrického klíče. Viz např. [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
Pokud můžeme najít algoritmus, který je malý a rychlý.

Trikem je najít asymetrickou šifru, která je malá a rychlá. ElGamal s 514 bajty je zde trochu bolestivý. Můžeme to udělat lépe.

Viz např. http://security.stackexchange.com/questions/824...

Toto funguje pro malé počty příjemců (nebo vlastně, klíčů; můžete stále distribuovat klíče více lidem, pokud chcete).


## Specifikace

- Cílový router
- Publikovaný timestamp
- Expirace
- Flagy
- Délka dat
- Šifrovaná data
- Podpis

Šifrovaná data mohou být předřazena nějakým specifikátorem enctype, nebo ne.


## Reference

* [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
