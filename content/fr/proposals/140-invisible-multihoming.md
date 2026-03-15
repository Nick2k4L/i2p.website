---
title: "Multihébergement invisible"
number: "140"
author: "str4d"
created: "2017-05-22"
lastupdated: "2017-07-04"
status: "Ouvrir"
thread: "http://zzz.i2p/topics/2335"
toc: true
---
## Aperçu

Cette proposition décrit une conception pour un protocole permettant à un client I2P, un service ou un processus équilibreur externe de gérer plusieurs routeurs hébergeant de manière transparente une seule [Destination](/docs/specs/common-structures/#destination).

La proposition ne spécifie actuellement aucune implémentation concrète. Elle pourrait être implémentée comme une extension de [I2CP](/docs/specs/i2cp/), ou comme un nouveau protocole.


## Motivation

Le multihébergement (multihoming) consiste à utiliser plusieurs routeurs pour héberger la même Destination. La méthode actuelle de multihébergement avec I2P consiste à exécuter la même Destination sur chaque routeur indépendamment ; le routeur utilisé par les clients à un moment donné est celui qui a publié en dernier un LeaseSet.

Ceci est un bidouillage et ne fonctionnera probablement pas à grande échelle pour les grands sites web. Imaginons que nous ayons 100 routeurs en multihébergement, chacun avec 16 tunnels. Cela représente 1600 publications de LeaseSet toutes les 10 minutes, soit presque 3 par seconde. Les nœuds floodfill seraient submergés et les limitations entreraient en jeu. Et cela sans même parler du trafic de recherche.

La proposition 123 résout ce problème avec un meta-LeaseSet, qui liste les 100 hachages réels de LeaseSet. Une recherche devient un processus en deux étapes : d'abord rechercher le meta-LeaseSet, puis l'un des LeaseSets nommés. C'est une bonne solution au problème du trafic de recherche, mais elle crée seule une fuite de confidentialité importante : il est possible de déterminer quels routeurs en multihébergement sont en ligne en surveillant le meta-LeaseSet publié, car chaque LeaseSet réel correspond à un seul routeur.

Nous avons besoin d'un moyen pour qu'un client ou un service I2P puisse répartir une seule Destination sur plusieurs routeurs, d'une manière indiscernable de l'utilisation d'un seul routeur (du point de vue du LeaseSet lui-même).


## Conception

### Définitions

    Utilisateur
        La personne ou l'organisation souhaitant mettre en œuvre le multihébergement pour sa(ou ses) Destination(s). Une seule Destination est considérée ici sans perte de généralité (WLOG).

    Client
        L'application ou le service fonctionnant derrière la Destination. Il peut s'agir d'une application côté client, côté serveur ou pair-à-pair ; nous l'appelons client au sens où il se connecte aux routeurs I2P.

        Le client se compose de trois parties, qui peuvent toutes être dans le même processus ou réparties sur plusieurs processus ou machines (dans une configuration multi-client) :

        Équilibreur (Balancer)
            La partie du client qui gère la sélection des pairs et la construction des tunnels. Il n'y a qu'un seul équilibreur à un instant donné, et il communique avec tous les routeurs I2P. Il peut y avoir des équilibreurs de secours.

        Interface (Frontend)
            La partie du client qui peut être exécutée en parallèle. Chaque interface communique avec un seul routeur I2P.

        Backend
            La partie du client partagée entre toutes les interfaces. Elle n'a aucune communication directe avec un routeur I2P.

    Routeur
        Un routeur I2P exploité par l'utilisateur qui se situe à la frontière entre le réseau I2P et le réseau de l'utilisateur (semblable à un dispositif périphérique dans les réseaux d'entreprise). Il construit des tunnels sous les ordres d'un équilibreur, et achemine les paquets pour un client ou une interface.

### Aperçu général

Imaginons la configuration souhaitée suivante :

- Une application cliente avec une Destination.
- Quatre routeurs, chacun gérant trois tunnels entrants.
- Les douze tunnels doivent être publiés dans un seul LeaseSet.

### Client unique

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

### Processus général du client

- Charger ou générer une Destination.

- Ouvrir une session avec chaque routeur, liée à la Destination.

- Périodiquement (environ toutes les dix minutes, mais plus ou moins selon la durée de vie des tunnels) :

  - Obtenir la couche rapide (fast tier) de chaque routeur.

  - Utiliser la superposition des pairs pour construire des tunnels vers/depuis chaque routeur.

    - Par défaut, les tunnels vers/depuis un routeur donné utiliseront des pairs de la couche rapide de ce routeur, mais cela n'est pas imposé par le protocole.

  - Rassembler l'ensemble des tunnels entrants actifs provenant de tous les routeurs actifs, et créer un LeaseSet.

  - Publier le LeaseSet via un ou plusieurs routeurs.

### Différences avec I2CP

Pour créer et gérer cette configuration, le client a besoin des nouvelles fonctionnalités suivantes, en plus de celles actuellement fournies par [I2CP](/docs/specs/i2cp/) :

- Demander à un routeur de construire des tunnels, sans créer de LeaseSet pour ceux-ci.
- Obtenir une liste des tunnels actuels dans le pool entrant.

De plus, les fonctionnalités suivantes permettraient une flexibilité significative dans la gestion des tunnels par le client :

- Obtenir le contenu de la couche rapide (fast tier) d'un routeur.
- Demander à un routeur de construire un tunnel entrant ou sortant en utilisant une liste donnée de pairs.

### Aperçu du protocole

```
         Client                           Router

                    --------------------->  Create Session
   Session Status  <---------------------
                    --------------------->  Get Fast Tier
        Peer List  <---------------------
                    --------------------->  Create Tunnel
    Tunnel Status  <---------------------
                    --------------------->  Get Tunnel Pool
      Tunnel List  <---------------------
                    --------------------->  Publish LeaseSet
                    --------------------->  Send Packet
      Send Status  <---------------------
  Packet Received  <---------------------
```

### Messages

**Create Session**
- Créer une session pour la Destination donnée.

**Session Status**
- Confirmation que la session a été configurée, et que le client peut maintenant commencer à construire des tunnels.

**Get Fast Tier**
- Demander une liste des pairs que le routeur envisagerait actuellement pour construire des tunnels.

**Peer List**
- Une liste de pairs connus du routeur.

**Create Tunnel**
- Demander au routeur de construire un nouveau tunnel via les pairs spécifiés.

**Tunnel Status**
- Résultat d'une construction particulière de tunnel, une fois disponible.

**Get Tunnel Pool**
- Demander une liste des tunnels actuels dans le pool entrant ou sortant pour la Destination.

**Tunnel List**
- Une liste de tunnels pour le pool demandé.

**Publish LeaseSet**
- Demander au routeur de publier le LeaseSet fourni via l'un des tunnels sortants de la Destination. Aucun statut de réponse n'est nécessaire ; le routeur doit continuer à réessayer jusqu'à ce qu'il soit satisfait que le LeaseSet ait été publié.

**Send Packet**
- Un paquet sortant du client. Spécifie éventuellement un tunnel sortant par lequel le paquet doit (devrait ?) être envoyé.

**Send Status**
- Informe le client du succès ou de l'échec de l'envoi d'un paquet.

**Packet Received**
- Un paquet entrant destiné au client. Spécifie éventuellement le tunnel entrant par lequel le paquet a été reçu(?)


## Implications de sécurité

Du point de vue des routeurs, cette conception est fonctionnellement équivalente à l'état actuel. Le routeur construit toujours tous les tunnels, maintient ses propres profils de pairs, et applique la séparation entre les opérations du routeur et du client. Dans la configuration par défaut, elle est complètement identique, car les tunnels pour ce routeur sont construits à partir de sa propre couche rapide.

Du point de vue du netDB, un seul LeaseSet créé via ce protocole est identique à l'état actuel, car il exploite des fonctionnalités déjà existantes. Cependant, pour des LeaseSets plus grands approchant 16 Leases, il pourrait être possible pour un observateur de déterminer que le LeaseSet est en multihébergement :

- La taille maximale actuelle de la couche rapide est de 75 pairs. La passerelle entrante (IBGW, le nœud publié dans un Lease) est sélectionnée à partir d'une fraction de cette couche (partitionnée aléatoirement par pool de tunnel selon le hachage, pas selon le nombre) :

      1 saut
          Toute la couche rapide

      2 sauts
          La moitié de la couche rapide
          (par défaut jusqu'au milieu de 2014)

      3+ sauts
          Un quart de la couche rapide
          (3 étant le paramètre par défaut actuel)

  Cela signifie qu'en moyenne, les IBGW seront choisis parmi un ensemble de 20 à 30 pairs.

- Dans une configuration mono-hébergée, un LeaseSet complet de 16 tunnels aurait 16 IBGW sélectionnés aléatoirement parmi un ensemble d'au plus (disons) 20 pairs.

- Dans une configuration en multihébergement à 4 routeurs utilisant la configuration par défaut, un LeaseSet complet de 16 tunnels aurait 16 IBGW sélectionnés aléatoirement parmi un ensemble d'au plus 80 pairs, bien qu'il y ait probablement une fraction de pairs communs entre les routeurs.

Ainsi, avec la configuration par défaut, il pourrait être possible, par analyse statistique, de déterminer qu'un LeaseSet est généré par ce protocole. Il pourrait aussi être possible de déterminer combien de routeurs sont utilisés, bien que l'effet du renouvellement (churn) sur les couches rapides réduise l'efficacité de cette analyse.

Étant donné que le client a un contrôle total sur les pairs qu'il sélectionne, cette fuite d'information pourrait être réduite ou éliminée en sélectionnant les IBGW parmi un ensemble restreint de pairs.


## Compatibilité

Cette conception est entièrement compatible avec le réseau, car il n'y a aucune modification du format du LeaseSet. Tous les routeurs devraient connaître le nouveau protocole, mais cela ne pose pas de problème car ils seraient tous contrôlés par la même entité.


## Remarques sur les performances et l'évolutivité

La limite supérieure de 16 Leases par LeaseSet n'est pas modifiée par cette proposition. Pour les Destinations nécessitant plus de tunnels, deux modifications réseau sont possibles :

- Augmenter la limite supérieure de la taille des LeaseSets. Ce serait la solution la plus simple à implémenter (bien qu'elle nécessiterait toujours un soutien généralisé du réseau avant d'être largement utilisée), mais pourrait entraîner des recherches plus lentes en raison de la taille accrue des paquets. La taille maximale réalisable d'un LeaseSet est définie par l'unité de transmission maximale (MTU) des transports sous-jacents, et est donc d'environ 16 ko.

- Implémenter la proposition 123 pour des LeaseSets hiérarchisés. En combinaison avec cette proposition, les Destinations des sous-LeaseSets pourraient être réparties sur plusieurs routeurs, agissant effectivement comme plusieurs adresses IP pour un service en clairnet.


## Remerciements

Merci à psi pour la discussion ayant conduit à cette proposition.


## Références

* [Destination](/docs/specs/common-structures/#destination)
* [I2CP](/docs/specs/i2cp/)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [Prop123](/proposals/123-new-netdb-entries/)
