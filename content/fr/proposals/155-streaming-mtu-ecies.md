---
title: "MTU de Streaming pour Destinations ECIES"
number: "155"
author: "zzz"
created: "2020-05-06"
lastupdated: "2020-05-30"
status: "Fermé"
thread: "http://zzz.i2p/topics/2886"
target: "0.9.47"
implementedin: "0.9.47"
toc: true
---
## Note
Déploiement et tests réseau en cours.  
Sous réserve de révisions mineures.


## Aperçu


### Résumé

ECIES réduit la surcharge des messages de session existante (ES) d'environ 90 octets.  
Par conséquent, nous pouvons augmenter le MTU d'environ 90 octets pour les connexions ECIES.  
Voir la [spécification ECIES](/docs/specs/ecies/#overhead), la [spécification Streaming](/docs/specs/streaming/#flags-and-option-data-fields) et la [documentation de l'API Streaming](/docs/api/streaming/).

Sans augmentation du MTU, dans de nombreux cas, les économies de surcharge ne sont pas vraiment « économisées »,  
car les messages seront de toute façon complétés pour occuper deux messages de tunnel complets.

Cette proposition ne nécessite aucun changement aux spécifications.  
Elle est publiée uniquement afin de faciliter la discussion et la construction d'un consensus  
sur la valeur recommandée et sur les détails d'implémentation.


### Objectifs

- Augmenter le MTU négocié
- Maximiser l'utilisation des messages de tunnel de 1 Ko
- Ne pas modifier le protocole de streaming


## Conception

Utiliser l'option existante MAX_PACKET_SIZE_INCLUDED et la négociation de MTU.  
Le streaming continue d'utiliser le minimum entre le MTU envoyé et le MTU reçu.  
La valeur par défaut reste 1730 pour toutes les connexions, quelles que soient les clés utilisées.

Les implémentations sont encouragées à inclure l'option MAX_PACKET_SIZE_INCLUDED dans tous les paquets SYN, dans les deux sens,  
bien que cela ne soit pas une obligation.

Si une destination est uniquement ECIES, utiliser la valeur plus élevée (en tant qu'Alice ou Bob).  
Si une destination est à clés doubles, le comportement peut varier :

Si le client à clés doubles est en dehors du routeur (dans une application externe),  
il peut ne pas « savoir » quelle clé est utilisée à l'extrémité distante, et Alice peut demander  
une valeur plus élevée dans le SYN, tandis que le max data dans le SYN reste à 1730.

Si le client à clés doubles est à l'intérieur du routeur, l'information sur la clé utilisée  
peut ou non être connue du client.  
Le leaseset peut ne pas avoir encore été récupéré, ou les interfaces d'API internes  
peuvent ne pas rendre facilement cette information disponible au client.  
Si l'information est disponible, Alice peut utiliser la valeur plus élevée ;  
sinon, Alice doit utiliser la valeur standard de 1730 jusqu'à la négociation.

Un client à clés doubles en tant que Bob peut envoyer la valeur plus élevée en réponse,  
même si aucune valeur ou une valeur de 1730 a été reçue d'Alice ;  
toutefois, il n'existe aucune possibilité de négocier une augmentation dans le streaming,  
donc le MTU doit rester à 1730.


Comme indiqué dans la [documentation de l'API Streaming](/docs/api/streaming/),  
les données dans les paquets SYN envoyés d'Alice vers Bob peuvent dépasser le MTU de Bob.  
C'est une faiblesse du protocole de streaming.  
Par conséquent, les clients à clés doubles doivent limiter les données dans les paquets SYN envoyés  
à 1730 octets, tout en envoyant une option de MTU plus élevée.  
Une fois que le MTU plus élevé est reçu de Bob, Alice peut augmenter la charge utile maximale envoyée.


### Analyse

Tel que décrit dans la [spécification ECIES](/docs/specs/ecies/#overhead), la surcharge ElGamal pour les messages de session existante est  
de 151 octets, et la surcharge Ratchet est de 69 octets.  
Par conséquent, nous pouvons augmenter le MTU pour les connexions ratchet de (151 - 69) = 82 octets,  
passant de 1730 à 1812.


## Spécification

Ajouter les modifications et clarifications suivantes à la section MTU Selection and Negotiation de la [documentation de l'API Streaming](/docs/api/streaming/).  
Aucun changement à la [spécification Streaming](/docs/specs/streaming/).


La valeur par défaut de l'option i2p.streaming.maxMessageSize reste 1730 pour toutes les connexions, quelles que soient les clés utilisées.  
Les clients doivent utiliser le minimum entre le MTU envoyé et reçu, comme d'habitude.

Il existe quatre constantes et variables MTU liées :

- DEFAULT_MTU : 1730, inchangé, pour toutes les connexions
- i2cp.streaming.maxMessageSize : par défaut 1730 ou 1812, peut être modifié par configuration
- ALICE_SYN_MAX_DATA : la taille maximale des données qu'Alice peut inclure dans un paquet SYN
- negotiated_mtu : le minimum entre le MTU d'Alice et celui de Bob, utilisé comme taille maximale des données  
  dans le SYN ACK envoyé de Bob vers Alice, et dans tous les paquets ultérieurs envoyés dans les deux sens


Cinq cas doivent être pris en compte :


### 1) Alice uniquement ElGamal
Aucun changement, MTU de 1730 dans tous les paquets.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize par défaut : 1730
- Alice peut envoyer MAX_PACKET_SIZE_INCLUDED dans le SYN, non requis sauf si ≠ 1730


### 2) Alice uniquement ECIES
MTU de 1812 dans tous les paquets.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize par défaut : 1812
- Alice doit envoyer MAX_PACKET_SIZE_INCLUDED dans le SYN


### 3) Alice à clés doubles et sait que Bob est ElGamal
MTU de 1730 dans tous les paquets.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize par défaut : 1812
- Alice peut envoyer MAX_PACKET_SIZE_INCLUDED dans le SYN, non requis sauf si ≠ 1730


### 4) Alice à clés doubles et sait que Bob est ECIES
MTU de 1812 dans tous les paquets.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize par défaut : 1812
- Alice doit envoyer MAX_PACKET_SIZE_INCLUDED dans le SYN


### 5) Alice à clés doubles et clé de Bob inconnue
Envoyer 1812 comme MAX_PACKET_SIZE_INCLUDED dans le paquet SYN mais limiter les données du paquet SYN à 1730.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize par défaut : 1812
- Alice doit envoyer MAX_PACKET_SIZE_INCLUDED dans le SYN


### Pour tous les cas

Alice et Bob calculent  
negotiated_mtu, le minimum entre le MTU d'Alice et celui de Bob, utilisé comme taille maximale des données  
dans le SYN ACK envoyé de Bob vers Alice, et dans tous les paquets ultérieurs envoyés dans les deux sens.


## Justification

Voir le [code source Java I2P](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220) pour comprendre pourquoi la valeur actuelle est 1730.  
Voir la [spécification ECIES](/docs/specs/ecies/#overhead) pour comprendre pourquoi la surcharge ECIES est inférieure de 82 octets à celle d'ElGamal.


## Notes d'implémentation

Si le streaming crée des messages de taille optimale, il est très important que  
la couche ECIES-Ratchet n'ajoute pas de remplissage au-delà de cette taille.

La taille optimale d'un message Garlic pour tenir dans deux messages de tunnel,  
incluant l'en-tête I2NP de 16 octets du message Garlic, 4 octets pour la longueur du message Garlic,  
8 octets pour le tag ES, et 16 octets pour le MAC, est de 1956 octets.

Un algorithme de remplissage recommandé dans ECIES est le suivant :

- Si la longueur totale du message Garlic serait de 1954 à 1956 octets,  
  ne pas ajouter de bloc de remplissage (pas de place)
- Si la longueur totale du message Garlic serait de 1938 à 1953 octets,  
  ajouter un bloc de remplissage pour atteindre exactement 1956 octets.
- Sinon, remplir comme d'habitude, par exemple avec une quantité aléatoire de 0 à 15 octets.

Des stratégies similaires pourraient être utilisées pour les tailles optimales d'un message de tunnel (964)  
et de trois messages de tunnel (2952), bien que ces tailles devraient être rares en pratique.


## Problèmes

La valeur 1812 est provisoire. À confirmer et éventuellement ajuster.


## Migration

Aucun problème de compatibilité ascendante.  
Il s'agit d'une option existante et la négociation de MTU fait déjà partie de la spécification.

Les anciennes destinations ECIES supporteront 1730.  
Tout client recevant une valeur plus élevée répondra avec 1730, et l'extrémité distante  
négociera vers le bas, comme d'habitude.


## Références

* [CALCULATION](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220)
* [ECIES](/docs/specs/ecies/#overhead)
* [STREAMING-OPTIONS](/docs/api/streaming/)
* [STREAMING-SPEC](/docs/specs/streaming/#flags-and-option-data-fields)
