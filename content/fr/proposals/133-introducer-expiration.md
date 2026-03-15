---
title: "Expiration de l'Introcuteur"
number: "133"
author: "zzz"
created: "2017-02-05"
lastupdated: "2017-08-09"
status: "Closed"
thread: "http://zzz.i2p/topics/2230"
target: "0.9.30"
implementedin: "0.9.30"
toc: true
---
## Aperçu

Cette proposition vise à améliorer le taux de réussite des introductions.


## Motivation

Les introducteurs expirent après une certaine durée, mais cette information n'est pas publiée dans les informations du routeur (Router Info). Les routeurs doivent actuellement utiliser des heuristiques pour estimer quand un introducteur n'est plus valide.


## Conception

Dans une adresse de routeur SSU contenant des introducteurs, l'éditeur peut optionnellement inclure des horodateurs d'expiration pour chaque introducteur.


## Spécification

```
iexp{X}={nnnnnnnnnn}

X :: Le numéro de l'introducteur (0-2)

nnnnnnnnnn :: Le temps en secondes (pas en ms) depuis l'époque.
```

### Notes

* Chaque expiration doit être supérieure à la date de publication des informations du routeur (Router Info), et inférieure à 6 heures après cette date.

* Les routeurs éditeurs et les introducteurs devraient s'efforcer de maintenir la validité de l'introducteur jusqu'à son expiration, mais ils ne peuvent pas garantir cela.

* Les routeurs ne devraient pas utiliser un introducteur publié après son expiration.

* Les expirations des introducteurs se trouvent dans le mappage de l'adresse du routeur (Router Address).  
  Elles ne correspondent pas au champ d'expiration de 8 octets (actuellement inutilisé) dans l'adresse du routeur.

**Exemple :** `iexp0=1486309470`


## Migration

Aucun problème. La mise en œuvre est facultative.  
La compatibilité ascendante est assurée, car les anciens routeurs ignoreront les paramètres inconnus.


## Références

* [RouterAddress](/docs/specs/common-structures/#routeraddress)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TRAC-TICKET](http://trac.i2p2.i2p/ticket/1352)
