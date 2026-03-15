---
title: "LeaseSet Chiffré"
number: "121"
author: "zzz"
created: "2016-01-11"
lastupdated: "2016-01-12"
status: "Rejeté"
thread: "http://zzz.i2p/topics/2047"
supercededby: "123"
toc: true
---
## Vue d'ensemble

Cette proposition concerne la refonte du mécanisme de chiffrement des LeaseSets.


## Motivation

Le LS chiffré actuel est horrible et peu sécurisé. Je peux le dire, je l'ai conçu et
implémenté.

Raisons :

- Chiffrement AES CBC
- Une seule clé AES pour tout le monde
- Les expirations de bail sont toujours exposées
- La clé de chiffrement publique est toujours exposée


## Conception

### Objectifs

- Rendre l'ensemble opaque
- Clés pour chaque destinataire


### Stratégie

Faire comme GPG/OpenPGP. Chiffrer de manière asymétrique une clé symétrique pour chaque
destinataire. Les données sont déchiffrées avec cette clé asymétrique. Voir par exemple [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
SI nous pouvons trouver un algorithme qui est petit et rapide.

L'astuce consiste à trouver un chiffrement asymétrique qui est petit et rapide. ElGamal à 514
octets est un peu douloureux ici. Nous pouvons faire mieux.

Voir par exemple http://security.stackexchange.com/questions/824...

Cela fonctionne pour de petits nombres de destinataires (ou en fait, de clés ; vous pouvez toujours
distribuer des clés à plusieurs personnes si vous le souhaitez).


## Spécification

- Destination
- Horodatage publié
- Expiration
- Indicateurs
- Longueur des données
- Données chiffrées
- Signature

Les données chiffrées pourraient être précédées d'un spécificateur de type de chiffrement, ou non.


## Références

* [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
