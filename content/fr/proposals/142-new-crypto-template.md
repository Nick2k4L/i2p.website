---
title: "Nouveau Modèle de Proposition de Chiffrement"
aliases:
  - "/fr/proposals/142-ecies-template"
  - "/fr/proposals/142-ecies-template/"
number: "142"
author: "zzz"
created: "2018-01-11"
lastupdated: "2018-01-20"
status: "Meta"
thread: "http://zzz.i2p/topics/2499"
toc: true
---
## Aperçu

Ce document décrit des problèmes importants à prendre en compte lorsqu'on propose
un remplacement ou une extension de notre chiffrement asymétrique ElGamal.

Il s'agit d'un document informatif.


## Motivation

ElGamal est ancien et lent, et de meilleures alternatives existent.
Cependant, plusieurs problèmes doivent être résolus avant de pouvoir ajouter ou changer d'algorithme.
Ce document met en lumière ces problèmes non résolus.



## Recherches préalables

Toute personne proposant une nouvelle cryptographie doit d'abord connaître les documents suivants :

- [Proposal 111 NTCP2](/proposals/111-ntcp-2/)
- [Proposal 123 LS2](/proposals/123-new-netdb-entries/)
- [Proposal 136 experimental sig types](/proposals/136-experimental-sigtypes/)
- [Proposal 137 optional sig types](/proposals/137-optional-sigtypes/)
- Les fils de discussion associés à chacune des propositions ci-dessus, disponibles via les liens internes
- [2018 proposal priorities](http://zzz.i2p/topics/2494)
- [ECIES proposal](http://zzz.i2p/topics/2418)
- [New asymmetric crypto overview](http://zzz.i2p/topics/1768)
- [Low-level crypto overview](/docs/specs/common-structures/)


## Utilisations du chiffrement asymétrique

Pour rappel, nous utilisons ElGamal pour :

1) Les messages de création de tunnel (la clé se trouve dans RouterIdentity)

2) Le chiffrement entre routeurs des messages netdb et autres messages I2NP (la clé se trouve dans RouterIdentity)

3) Le chiffrement de bout en bout client utilisant ElGamal+AES/SessionTag (la clé se trouve dans LeaseSet, la clé Destination n'est pas utilisée)

4) L'échange éphémère DH pour NTCP et SSU


## Conception

Toute proposition visant à remplacer ElGamal par un autre algorithme doit fournir les détails suivants.



## Spécification

Toute proposition de chiffrement asymétrique doit entièrement spécifier les éléments suivants.



### 1. Généralités

Répondez aux questions suivantes dans votre proposition. Notez que cela pourrait nécessiter une proposition distincte des détails spécifiques du point 2) ci-dessous, car cela pourrait entrer en conflit avec les propositions existantes 111, 123, 136, 137 ou d'autres.

- Pour quels cas parmi les cas 1 à 4 ci-dessus proposez-vous d'utiliser la nouvelle cryptographie ?
- Si pour les cas 1) ou 2) (routeur), où la clé publique sera-t-elle stockée, dans RouterIdentity ou dans les propriétés RouterInfo ? Avez-vous l'intention d'utiliser le type de chiffrement dans le certificat de clé ? Spécifiez entièrement. Justifiez votre choix dans tous les cas.
- Si pour le cas 3) (client), avez-vous l'intention de stocker la clé publique dans la destination et d'utiliser le type de chiffrement dans le certificat de clé (comme dans la proposition ECIES), ou de la stocker dans LS2 (comme dans la proposition 123), ou autre chose ? Spécifiez entièrement et justifiez votre choix.
- Pour toutes les utilisations, comment le support sera-t-il annoncé ? S'il s'agit du cas 3), cela ira-t-il dans LS2 ou ailleurs ? S'il s'agit des cas 1) et 2), cela ressemblera-t-il aux propositions 136 et/ou 137 ? Spécifiez entièrement et justifiez vos choix. Une proposition distincte sera probablement nécessaire pour cela.
- Spécifiez entièrement comment et pourquoi cela reste compatible avec les anciennes versions, et décrivez complètement un plan de migration.
- Quelles propositions non implémentées sont des prérequis à votre proposition ?


### 2. Type de chiffrement spécifique

Répondez aux questions suivantes dans votre proposition :

- Informations générales sur la cryptographie, courbes/paramètres spécifiques, justifiez entièrement votre choix. Fournissez des liens vers les spécifications et autres informations.
- Résultats de tests de vitesse comparés à ElG et à d'autres alternatives si applicables. Incluez chiffrement, déchiffrement et génération de clés.
- Disponibilité des bibliothèques en C++ et en Java (OpenJDK, BouncyCastle, et tiers)
  Pour les bibliothèques tierces ou non-Java, fournissez les liens et les licences
- Numéro(s) de type de chiffrement proposés (dans la plage expérimentale ou non)




## Notes
