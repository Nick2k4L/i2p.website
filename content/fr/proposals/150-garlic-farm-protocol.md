---
title: "Protocole de la ferme à l'ail"
number: "150"
author: "zzz"
created: "2019-05-02"
lastupdated: "2019-05-20"
status: "Ouvert"
thread: "http://zzz.i2p/topics/2234"
toc: true
---
## Aperçu

Il s'agit de la spécification du protocole réseau Garlic Farm,
basée sur JRaft, son code « exts » pour l'implémentation sur TCP,
et son exemple d'application « dmprinter » [JRAFT](https://github.com/datatechnology/jraft).


Nous n'avons pas pu trouver d'implémentation avec un protocole réseau documenté.
Cependant, l'implémentation JRaft est suffisamment simple pour que nous puissions
examiner le code puis documenter son protocole.
Cette proposition est le résultat de cet effort.

Cela servira de backend pour la coordination des routeurs publiant
des entrées dans un Meta LeaseSet. Voir la proposition 123.


## Objectifs

- Petite taille de code
- Basé sur une implémentation existante
- Pas d'objets Java sérialisés ni de fonctionnalités ou encodage spécifiques à Java
- Toute amorce (bootstrapping) est hors sujet. On suppose qu'au moins un autre serveur est
  codé en dur ou configuré en dehors de ce protocole.
- Prendre en charge les cas d'utilisation hors bande et dans I2P.


## Conception

Le protocole Raft n'est pas un protocole concret ; il définit uniquement une machine à états.
Par conséquent, nous documentons le protocole concret de JRaft et nous basons notre protocole dessus.
Aucun changement n'est apporté au protocole JRaft, hormis l'ajout
d'une poignée de main d'authentification.

Raft élit un Leader dont le rôle est de publier un journal (log).
Le journal contient des données de configuration Raft et des données applicatives.
Les données applicatives contiennent l'état du routeur de chaque serveur et la Destination
du cluster Meta LS2.
Les serveurs utilisent un algorithme commun pour déterminer l'éditeur et le contenu
du Meta LS2.
L'éditeur du Meta LS2 n'est PAS nécessairement le Leader Raft.



## Spécification

Le protocole réseau fonctionne sur des sockets SSL ou des sockets I2P non chiffrés.
Les sockets I2P sont relayés via le proxy HTTP.
Il n'y a aucun support pour les sockets claires non SSL.

### Poignée de main et authentification

Non défini par JRaft.

Objectifs :

- Méthode d'authentification utilisateur/mot de passe
- Identifiant de version
- Identifiant de cluster
- Extensible
- Facilité de relais lorsqu'utilisé pour les sockets I2P
- Ne pas exposer inutilement le serveur comme serveur Garlic Farm
- Protocole simple afin qu'une implémentation complète de serveur web ne soit pas requise
- Compatible avec les standards courants, afin que les implémentations puissent utiliser
  des bibliothèques standard si désiré

Nous utiliserons une poignée de main similaire à WebSocket et
l'authentification HTTP Digest [RFC 2617](https://tools.ietf.org/html/rfc2617).
L'authentification Basic de la RFC 2617 n'est PAS prise en charge.
Lors du relais via le proxy HTTP, communiquer avec
le proxy comme spécifié dans [RFC 2616](https://tools.ietf.org/html/rfc2616).

#### Identifiants

Le fait que les noms d'utilisateur et mots de passe soient par cluster ou
par serveur dépend de l'implémentation.


#### Requête HTTP 1

L'initiateur enverra ce qui suit.

Toutes les lignes se terminent par CRLF comme exigé par HTTP.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: close
  (tout autre en-tête ignoré)
  (ligne vide)

  CLUSTER est le nom du cluster (par défaut "farm")
  VERSION est la version Garlic Farm (actuellement "1")

```


#### Réponse HTTP 1

Si le chemin n'est pas correct, le destinataire enverra une réponse standard « HTTP/1.1 404 Not Found »,
comme dans [RFC 2616](https://tools.ietf.org/html/rfc2616).

Si le chemin est correct, le destinataire enverra une réponse standard « HTTP/1.1 401 Unauthorized »,
incluant l'en-tête WWW-Authenticate d'authentification Digest HTTP,
comme dans [RFC 2617](https://tools.ietf.org/html/rfc2617).

Les deux parties fermeront ensuite la socket.


#### Requête HTTP 2

L'initiateur enverra ce qui suit,
comme dans [RFC 2617](https://tools.ietf.org/html/rfc2617).

Toutes les lignes se terminent par CRLF comme exigé par HTTP.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: keep-alive, Upgrade
  Upgrade: websocket
  (en-têtes Sec-Websocket-* si relayé)
  Authorization: (en-tête d'autorisation Digest HTTP comme dans RFC 2617)
  (tout autre en-tête ignoré)
  (ligne vide)

  CLUSTER est le nom du cluster (par défaut "farm")
  VERSION est la version Garlic Farm (actuellement "1")

```


#### Réponse HTTP 2

Si l'authentification n'est pas correcte, le destinataire enverra une autre réponse standard « HTTP/1.1 401 Unauthorized »,
comme dans [RFC 2617](https://tools.ietf.org/html/rfc2617).

Si l'authentification est correcte, le destinataire enverra la réponse suivante,
comme dans le protocole WebSocket.

Toutes les lignes se terminent par CRLF comme exigé par HTTP.

```text

HTTP/1.1 101 Switching Protocols
  Connection: Upgrade
  Upgrade: websocket
  (en-têtes Sec-Websocket-*)
  (tout autre en-tête ignoré)
  (ligne vide)

```

Après réception de ceci, la socket reste ouverte.
Le protocole Raft tel que défini ci-dessous commence, sur la même socket.


#### Mise en cache

Les identifiants doivent être mis en cache pendant au moins une heure, afin que
les connexions ultérieures puissent passer directement à
« Requête HTTP 2 » ci-dessus.



### Types de messages

Il existe deux types de messages : requêtes et réponses.
Les requêtes peuvent contenir des entrées de journal (Log Entries) et sont de taille variable ;
les réponses ne contiennent pas d'entrées de journal et sont de taille fixe.

Les types de messages 1 à 4 sont les messages RPC standards définis par Raft.
Il s'agit du protocole Raft de base.

Les types de messages 5 à 15 sont les messages RPC étendus définis par
JRaft, pour prendre en charge les clients, les modifications dynamiques de serveurs et
la synchronisation efficace des journaux.

Les types de messages 16 à 17 sont les messages RPC de compactage du journal définis
dans la section 7 de Raft.


| Message | Numéro | Envoyé par | Envoyé à | Notes |
| :--- | :--- | :--- | :--- | :--- |
| RequestVoteRequest | 1 | Candidat | Suiveur | RPC standard Raft ; ne doit pas contenir d'entrées de journal |
| RequestVoteResponse | 2 | Suiveur | Candidat | RPC standard Raft |
| AppendEntriesRequest | 3 | Leader | Suiveur | RPC standard Raft |
| AppendEntriesResponse | 4 | Suiveur | Leader / Client | RPC standard Raft |
| ClientRequest | 5 | Client | Leader / Suiveur | Réponse est AppendEntriesResponse ; ne doit contenir que des entrées de journal applicatives |
| AddServerRequest | 6 | Client | Leader | Ne doit contenir qu'une seule entrée de journal ClusterServer |
| AddServerResponse | 7 | Leader | Client | Le leader enverra également une JoinClusterRequest |
| RemoveServerRequest | 8 | Suiveur | Leader | Ne doit contenir qu'une seule entrée de journal ClusterServer |
| RemoveServerResponse | 9 | Leader | Suiveur | |
| SyncLogRequest | 10 | Leader | Suiveur | Ne doit contenir qu'une seule entrée de journal LogPack |
| SyncLogResponse | 11 | Suiveur | Leader | |
| JoinClusterRequest | 12 | Leader | Nouveau serveur | Invitation à rejoindre ; ne doit contenir qu'une seule entrée de journal Configuration |
| JoinClusterResponse | 13 | Nouveau serveur | Leader | |
| LeaveClusterRequest | 14 | Leader | Suiveur | Commande pour quitter |
| LeaveClusterResponse | 15 | Suiveur | Leader | |
| InstallSnapshotRequest | 16 | Leader | Suiveur | Section 7 Raft ; ne doit contenir qu'une seule entrée de journal SnapshotSyncRequest |
| InstallSnapshotResponse | 17 | Suiveur | Leader | Section 7 Raft |


### Établissement

Après la poignée de main HTTP, la séquence d'établissement est la suivante :

```text

Nouveau serveur Alice              Suiveur aléatoire Bob

  ClientRequest   ------->
          <---------   AppendEntriesResponse

  Si Bob indique qu'il est le leader, continuer comme ci-dessous.
  Sinon, Alice doit se déconnecter de Bob et se connecter au leader.


  Nouveau serveur Alice              Leader Charlie

  ClientRequest   ------->
          <---------   AppendEntriesResponse
  AddServerRequest   ------->
          <---------   AddServerResponse
          <---------   JoinClusterRequest
  JoinClusterResponse  ------->
          <---------   SyncLogRequest
                       OU InstallSnapshotRequest
  SyncLogResponse  ------->
  OU InstallSnapshotResponse

```

Séquence de déconnexion :

```text

Suiveur Alice              Leader Charlie

  RemoveServerRequest   ------->
          <---------   RemoveServerResponse
          <---------   LeaveClusterRequest
  LeaveClusterResponse  ------->

```

Séquence d'élection :

```text

Candidat Alice               Suiveur Bob

  RequestVoteRequest   ------->
          <---------   RequestVoteResponse

  si Alice gagne l'élection :

  Leader Alice                Suiveur Bob

  AppendEntriesRequest   ------->
  (heartbeat)
          <---------   AppendEntriesResponse

```


### Définitions

- Source : Identifie l'origine du message
- Destination : Identifie le destinataire du message
- Termes : Voir Raft. Initialisés à 0, augmentent de façon monotone
- Index : Voir Raft. Initialisés à 0, augmentent de façon monotone



### Requêtes

Les requêtes contiennent un en-tête et zéro ou plusieurs entrées de journal.
Les requêtes contiennent un en-tête de taille fixe et des entrées de journal facultatives de taille variable.


#### En-tête de requête

L'en-tête de requête fait 45 octets, comme suit.
Toutes les valeurs sont non signées, big-endian.

```text

Type de message :      1 octet
  Source :            ID, entier sur 4 octets
  Destination :       ID, entier sur 4 octets
  Term :              Terme actuel (voir notes), entier sur 8 octets
  Last Log Term :     8 octets
  Last Log Index :    8 octets
  Commit Index :      8 octets
  Taille des entrées de journal :  Taille totale en octets, entier sur 4 octets
  Entrées de journal :       voir ci-dessous, longueur totale spécifiée

```


#### Notes

Dans RequestVoteRequest, Term est le terme du candidat.
Sinon, c'est le terme actuel du leader.

Dans AppendEntriesRequest, lorsque la taille des entrées de journal est nulle,
ce message est un message de heartbeat (keepalive).


#### Entrées de journal

Le journal contient zéro ou plusieurs entrées.
Chaque entrée de journal est comme suit.
Toutes les valeurs sont non signées, big-endian.

```text

Term :           8 octets
  Type de valeur :     1 octet
  Taille de l'entrée :     En octets, entier sur 4 octets
  Entrée :          longueur spécifiée

```


#### Contenu du journal

Toutes les valeurs sont non signées, big-endian.

| Type de valeur du journal | Numéro |
| :--- | :--- |
| Application | 1 |
| Configuration | 2 |
| ClusterServer | 3 |
| LogPack | 4 |
| SnapshotSyncRequest | 5 |


#### Application

Le contenu applicatif est encodé en UTF-8 [JSON](https://www.json.org/).
Voir la section Couche applicative ci-dessous.


#### Configuration

Utilisé par le leader pour sérialiser une nouvelle configuration de cluster et la répliquer aux pairs.
Contient zéro ou plusieurs configurations ClusterServer.


```text

Log Index :  8 octets
  Last Log Index :  8 octets
  Données ClusterServer pour chaque serveur :
    ID :                4 octets
    Longueur des données d'endpoint : En octets, 4 octets
    Données d'endpoint :     Chaîne ASCII de la forme "tcp://localhost:9001", longueur spécifiée

```


#### ClusterServer

Les informations de configuration d'un serveur dans un cluster.
Inclus uniquement dans un message AddServerRequest ou RemoveServerRequest.

Utilisé dans un message AddServerRequest :

```text

ID :                4 octets
  Longueur des données d'endpoint : En octets, 4 octets
  Données d'endpoint :     Chaîne ASCII de la forme "tcp://localhost:9001", longueur spécifiée

```


Utilisé dans un message RemoveServerRequest :

```text

ID :                4 octets

```


#### LogPack

Inclus uniquement dans un message SyncLogRequest.

Le suivant est compressé avec gzip avant transmission :


```text

Longueur des données d'index : En octets, 4 octets
  Longueur des données de journal :   En octets, 4 octets
  Données d'index :     8 octets pour chaque index, longueur spécifiée
  Données de journal :       longueur spécifiée

```



#### SnapshotSyncRequest

Inclus uniquement dans un message InstallSnapshotRequest.

```text

Last Log Index :  8 octets
  Last Log Term :   8 octets
  Longueur des données de configuration : En octets, 4 octets
  Données de configuration :     longueur spécifiée
  Offset :          L'offset des données dans la base, en octets, 8 octets
  Longueur des données :        En octets, 4 octets
  Données :            longueur spécifiée
  Is Done :         1 si terminé, 0 sinon (1 octet)

```




### Réponses

Toutes les réponses font 26 octets, comme suit.
Toutes les valeurs sont non signées, big-endian.

```text

Type de message :   1 octet
  Source :         ID, 4 octets
  Destination :    Habituellement l'ID du destinataire réel (voir notes), 4 octets
  Term :           Terme actuel, 8 octets
  Next Index :     Initialisé à dernier index de journal du leader + 1, 8 octets
  Is Accepted :    1 si accepté, 0 sinon (voir notes), 1 octet

```


#### Notes

L'ID de destination est habituellement l'ID du destinataire réel pour ce message.
Cependant, pour AppendEntriesResponse, AddServerResponse et RemoveServerResponse,
il s'agit de l'ID du leader actuel.

Dans RequestVoteResponse, Is Accepted vaut 1 pour un vote en faveur du candidat (demandeur),
et 0 pour aucun vote.


## Couche applicative

Chaque serveur poste périodiquement des données applicatives dans le journal via une ClientRequest.
Les données applicatives contiennent l'état du routeur de chaque serveur et la Destination
du cluster Meta LS2.
Les serveurs utilisent un algorithme commun pour déterminer l'éditeur et le contenu
du Meta LS2.
Le serveur ayant le statut « le meilleur » récent dans le journal est l'éditeur du Meta LS2.
L'éditeur du Meta LS2 n'est PAS nécessairement le Leader Raft.


### Contenu des données applicatives

Les données applicatives sont encodées en UTF-8 [JSON](https://json.org/),
pour plus de simplicité et d'extensibilité.
La spécification complète est à déterminer.
L'objectif est de fournir suffisamment de données pour écrire un algorithme déterminant le
meilleur routeur pour publier le Meta LS2, et pour que l'éditeur dispose d'informations suffisantes
pour pondérer les Destinations dans le Meta LS2.
Les données contiendront des statistiques sur le routeur et les Destinations.

Les données peuvent éventuellement contenir des données de détection à distance sur la santé des
autres serveurs et la capacité de récupérer le Meta LS.
Ces données ne seraient pas prises en charge dans la première version.

Les données peuvent éventuellement contenir des informations de configuration postées
par un client administrateur.
Ces données ne seraient pas prises en charge dans la première version.

Si « nom : valeur » est indiqué, cela spécifie la clé et la valeur de la carte JSON.
Sinon, la spécification est à déterminer.


Données de cluster (niveau supérieur) :

- cluster : Nom du cluster
- date : Date de ces données (long, ms depuis l'époque)
- id : ID Raft (entier)

Données de configuration (config) :

- Tous les paramètres de configuration

Statut de publication MetaLS (meta) :

- destination : destination metals, base64
- lastPublishedLS : si présent, encodage base64 du metals publié précédemment
- lastPublishedTime : en ms, ou 0 si jamais
- publishConfig : statut de configuration de l'éditeur : activé/désactivé/auto
- publishing : statut booléen de l'éditeur metals vrai/faux

Données du routeur (router) :

- lastPublishedRI : si présent, encodage base64 des dernières infos du routeur publiées
- uptime : Temps de fonctionnement en ms
- Délai des tâches (Job lag)
- Tunnels exploratoires
- Tunnels participant
- Bande passante configurée
- Bande passante actuelle

Destinations (destinations) :
Liste

Données de destination :

- destination : la destination, base64
- uptime : Temps de fonctionnement en ms
- Tunnels configurés
- Tunnels actuels
- Bande passante configurée
- Bande passante actuelle
- Connexions configurées
- Connexions actuelles
- Données de liste noire

Données de détection de routeur distant :

- Dernière version RI vue
- Temps de récupération LS
- Données de test de connexion
- Données de profil des floodfills les plus proches
  pour les périodes hier, aujourd'hui et demain

Données de détection de destination distante :

- Dernière version LS vue
- Temps de récupération LS
- Données de test de connexion
- Données de profil des floodfills les plus proches
  pour les périodes hier, aujourd'hui et demain

Données de détection Meta LS :

- Dernière version vue
- Temps de récupération
- Données de profil des floodfills les plus proches
  pour les périodes hier, aujourd'hui et demain


## Interface d'administration

À déterminer, éventuellement une proposition séparée.
Non requis pour la première version.

Exigences d'une interface d'administration :

- Support de plusieurs destinations maîtres, c'est-à-dire plusieurs clusters virtuels (farms)
- Fournir une vue complète de l'état partagé du cluster - toutes les statistiques publiées par les membres, qui est le leader actuel, etc.
- Capacité à forcer la suppression d'un participant ou du leader du cluster
- Capacité à forcer la publication du metaLS (si le nœud actuel est l'éditeur)
- Capacité à exclure des hachages du metaLS (si le nœud actuel est l'éditeur)
- Fonctionnalité d'import/export de configuration pour les déploiements en masse



## Interface du routeur

À déterminer, éventuellement une proposition séparée.
i2pcontrol n'est pas requis pour la première version et les modifications détaillées seront incluses dans une proposition séparée.

Exigences pour l'API Garlic Farm vers routeur (java in-JVM ou i2pcontrol)

- getLocalRouterStatus()
- getLocalLeafHash(Hash masterHash)
- getLocalLeafStatus(Hash leaf)
- getRemoteMeasuredStatus(Hash masterOrLeaf) // probablement pas dans MVP
- publishMetaLS(Hash masterHash, List<MetaLease> contents) // ou MetaLeaseSet signé ? Qui signe ?
- stopPublishingMetaLS(Hash masterHash)
- authentification à déterminer ?


## Justification

Atomix est trop volumineux et ne permet pas la personnalisation nécessaire pour acheminer
le protocole via I2P. De plus, son format réseau est non documenté et dépend
de la sérialisation Java.


## Notes



## Problèmes

- Il n'existe aucun moyen pour un client de découvrir et se connecter à un leader inconnu.
  Ce serait un changement mineur pour qu'un Suiveur envoie la Configuration comme entrée de journal dans AppendEntriesResponse.



## Migration

Aucun problème de compatibilité ascendante.


## Références

* [JRAFT](https://github.com/datatechnology/jraft)
* [JSON](https://json.org/)
* [RAFT](/docs/research/ongaro2014-raft.pdf)
* [RFC-2616](https://tools.ietf.org/html/rfc2616)
* [RFC-2617](https://tools.ietf.org/html/rfc2617)
* [WEBSOCKET](https://en.wikipedia.org/wiki/WebSocket)
