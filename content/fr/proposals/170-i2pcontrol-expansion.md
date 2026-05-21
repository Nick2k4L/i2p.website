---
title: "i2pcontrol-expansion"
number: "170"
author: "Nick2k4"
created: "2026-05-20"
lastupdated: "2026-05-20"
status: "Ouvrir"
toc: true
---

Aperçu ========

Cette proposition expose de nouvelles informations à l'API i2pcontrol, permettant une plus grande flexibilité. Ces informations incluent : l'ajout, la suppression, la récupération et la modification des carnets d'adresses et des services cachés. Cette proposition expose également davantage d'informations sur votre routeur, telles que les pairs, les actualités, la netDb, et plus encore.

Motivation ==========

La raison de cette proposition est de permettre une plus grande flexibilité dans l'API I2P, afin que les applications puissent implémenter et gérer une interface administrative I2P. Exposer de telles informations à i2pcontrol permet aux utilisateurs de créer des applications plus avancées et d'offrir un meilleur support pour la gestion à distance.

Conception ======

Lorsque les utilisateurs interagiront avec l'API i2pcontrol, ils pourront accéder à de nouvelles extrémités (endpoints) fournissant les informations mentionnées ci-dessus. Par exemple, l'API i2pcontrol exposera de nouvelles méthodes `TunnelManager` et `AddressBook` qui permettront aux utilisateurs de saisir des paramètres pour créer, supprimer, récupérer et modifier des tunnels et des carnets d'adresses. De plus, la méthode préexistante `RouterInfo` disposera de nouveaux paramètres afin de rendre accessibles des informations concernant le routeur.

Implications en matière de sécurité =====================

Il n'y a pas de conséquences sur la sécurité attendues supplémentaires liées à cette proposition, car les informations exposées sont déjà accessibles par d'autres moyens. Toutefois, il est important de s'assurer que des mécanismes d'authentification et d'autorisation appropriés sont en place pour accéder à l'API i2pcontrol, afin d'empêcher un accès non autorisé à des informations sensibles ou un contrôle du routeur.

Spécification de l'API et méthodes ===========================

Toutes les requêtes suivent la structure JSON-RPC 2.0 :

```json
{
  "jsonrpc": "2.0",
  "method": "MethodName",
  "params": {
    // method-specific parameters
  },
  "id": 1
}
```
Méthode - RouterInfo -------------------

Ci-dessous figurent les nouveaux paramètres de la méthode `RouterInfo` et leurs valeurs de retour :

- `i2p.router.news` - renvoie toutes les entrées d'actualités du routeur.
- `i2p.router.id` - renvoie le hachage du routeur sous forme de chaîne Base64, ou `null`.
- `i2p.router.clockskew` - renvoie l'écart moyen d'horloge des pairs, ou `null`.
- `i2p.router.info` - renvoie le RouterInfo sérialisé sous forme de chaîne Base64, ou `null`.
- `i2p.router.logs` - renvoie les messages récents du journal du routeur.
- `i2p.router.logs.clear` - efface le tampon du journal du routeur et renvoie `"success"`.

- `i2p.router.net.total.received.bytes` - renvoie le nombre total d'octets reçus depuis le démarrage. *(adopté depuis i2pd)*
- `i2p.router.net.total.sent.bytes` - renvoie le nombre total d'octets envoyés depuis le démarrage. *(adopté depuis i2pd)*
- `i2p.router.net.total.transit.bytes` - renvoie le nombre total d'octets en transit transférés depuis le démarrage. *(adopté depuis i2pd)*
- `i2p.router.net.bw.transit.15s` - renvoie la bande passante moyenne de transit sur 15 secondes (octets/seconde). *(adopté depuis i2pd)*

- `i2p.router.net.tunnels.shareratio` - renvoie le ratio de partage des tunnels.
- `i2p.router.net.tunnels.participating.info` - renvoie les informations sur les tunnels participants.
- `i2p.router.net.tunnels.i2ptunnel` - renvoie les informations du contrôleur I2PTunnel configuré (statistiques rapides de tous).
- `i2p.router.net.tunnels.exploratory.inbound` - renvoie le nombre de tunnels entrants exploratoires.
- `i2p.router.net.tunnels.exploratory.outbound` - renvoie le nombre de tunnels sortants exploratoires.
- `i2p.router.net.tunnels.exploratory.info.list` - renvoie la liste des informations des tunnels exploratoires.
- `i2p.router.net.tunnels.client.inbound` - renvoie le nombre de tunnels entrants client.
- `i2p.router.net.tunnels.client.outbound` - renvoie le nombre de tunnels sortants client.
- `i2p.router.net.tunnels.client.info.list` - renvoie la liste des informations des tunnels client.

- `i2p.router.net.status.v6` - renvoie le code d'état du réseau IPv6. *(adopté depuis i2pd)*
- `i2p.router.net.error` - renvoie le code d'erreur du réseau IPv4. *(adopté depuis i2pd)*
- `i2p.router.net.error.v6` - renvoie le code d'erreur du réseau IPv6. *(adopté depuis i2pd)*
- `i2p.router.net.testing` - indique si le réseau IPv4 est en état de test (0 ou 1). *(adopté depuis i2pd)*
- `i2p.router.net.testing.v6` - indique si le réseau IPv6 est en état de test (0 ou 1). *(adopté depuis i2pd)*

- `i2p.router.net.tunnels.successrate` - renvoie le taux de réussite récent de création des tunnels (%). *(adopté depuis i2pd)*
- `i2p.router.net.tunnels.totalsuccessrate` - renvoie le taux de réussite total de création des tunnels depuis le démarrage (%). *(adopté depuis i2pd)*
- `i2p.router.net.tunnels.queue` - renvoie la taille de la file d'attente des demandes de création de tunnel. *(adopté depuis i2pd)*
- `i2p.router.net.tunnels.tbmqueue` - renvoie la taille de la file d'attente des messages de construction de tunnel (Tunnel Build Message). *(adopté depuis i2pd)*

- `i2p.router.netdb.peers` - renvoie une liste de hachages d'homologues connus.
- `i2p.router.netdb.activepeers.info` - renvoie les données RouterInfo sérialisées pour les homologues actifs.
- `i2p.router.netdb.ntcp.limit` - renvoie la limite de connexions NTCP.
- `i2p.router.netdb.ssu.limit` - renvoie la limite de connexions SSU.
- `i2p.router.netdb.bannedpeers` - renvoie les homologues bannis avec les détails du bannissement.
- `i2p.router.netdb.activepeers.list` - renvoie les hachages des homologues actifs.
- `i2p.router.netdb.peers.list` - renvoie les hachages des homologues connus.
- `i2p.router.netdb.peers.info` - renvoie les données RouterInfo sérialisées pour les homologues connus.
- `i2p.router.netdb.activepeers.stats` - renvoie les statistiques des homologues actifs.

- `i2p.router.addressbook.private.list` - renvoie les entrées du carnet d'adresses privé.
- `i2p.router.addressbook.local.list` - renvoie les entrées du carnet d'adresses local.
- `i2p.router.addressbook.router.list` - renvoie les entrées du carnet d'adresses du routeur.
- `i2p.router.addressbook.published.list` - renvoie les entrées du carnet d'adresses publiées.
- `i2p.router.addressbook.subscriptions` - renvoie le chemin du fichier d'abonnements et ses entrées.
- `i2p.router.addressbook.config` - renvoie le chemin du fichier de configuration du carnet d'adresses et ses entrées.

Exemple :

```json
{
    "jsonrpc": "2.0",
    "method": "RouterInfo",
    "params": {
        "i2p.router.id": "",
    },
    "id": 1
}
```
Retour :

```json
{
    "jsonrpc": "2.0",
    "result": "{ data }",
    "id": 1
}
```
Méthode - Carnet d'adresses --------------------

Pour la méthode `AddressBook`, trois paramètres/arguments sont requis pour supprimer et ajouter des entrées dans le carnet d'adresses :

- `Type` - correspond au type de carnet d'adresses :
  - `private`
  - `local`
  - `router`
  - `published`
- `Hostname` - correspond au nom d'hôte ou au nom de domaine associé à l'entrée du carnet d'adresses.
- `Destination` - correspond à la destination associée à l'entrée du carnet d'adresses.
- `Delete` - ce paramètre est facultatif et sert à supprimer une entrée du carnet d'adresses. Si ce paramètre n'est pas fourni, la méthode ajoutera une nouvelle entrée au carnet d'adresses.

Exemple :

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "Type": "private",
    "Hostname": "example.i2p",
    "Destination": "exampleDestinationString",
    "Delete": "" <--- this parameter is optional
  },
  "id": 1
}
```
Retour :

```json
{
  "jsonrpc": "2.0",
  "success": true or false,        
  "message": "Deleted/Added (hostname) in (address book type) address book" OR "Failed to delete/add (hostname) to (address book type) address book",
  "id": 1
}
```
Pour modifier les abonnements au carnet d'adresses :

- `SetSubscriptions` - ce paramètre est utilisé pour définir les abonnements d'une entrée du carnet d'adresses. Il prend une liste de chaînes de caractères comme argument.

Exemple :

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetSubscriptions": ["notbob.i2p", "helloworld.i2p", ...]
  },
  "id": 1
}
```
Retour :

```json
{
  "jsonrpc": "2.0",
  "success": true,
  "message": "Successfully modified: /path/to/subscriptions.txt"
}
```
Pour modifier AddressBookConfig :

- `SetConfig` - ce paramètre est utilisé pour définir la configuration d'une entrée du carnet d'adresses.

Il prend un objet JSON en argument, qui contient les paramètres de configuration.

Paramètres de configuration disponibles/courants :

- `subscriptions` - fichier contenant la liste des URL d'abonnement.
- `update_delay` - intervalle de mise à jour en heures.
- `published_addressbook` - chemin vers le carnet d'adresses publié.
- `router_addressbook` - chemin vers le carnet d'adresses du routeur.
- `local_addressbook` - chemin vers le carnet d'adresses local.
- `private_addressbook` - chemin vers le carnet d'adresses privé.
- `proxy_port` - port d'eepProxy.
- `proxy_host` - nom d'hôte d'eepProxy.
- `should_publish` - indique s'il faut mettre à jour le carnet d'adresses publié.
- `etags` - fichier contenant les etags des URL d'abonnement.
- `last_modified` - fichier contenant les horodatages de dernière modification des URL d'abonnement.
- `log` - chemin du fichier journal.
- `theme` - thème.

Exemple :

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetConfig": {
      "subscriptions": "subscriptions.txt",
      "update_delay": "12",
      "published_addressbook": "../eepsite/docroot/hosts.txt",
      "router_addressbook": "hosts.txt",
      "local_addressbook": "../userhosts.txt",
      "private_addressbook": "../privatehosts.txt",
      "proxy_port": "4444",
      "proxy_host": "127.0.0.1",
      "should_publish": "true",
      "etags": "etags.txt",
      "last_modified": "last_modified.txt",
      "log": "log.txt",
      "theme": "light"
    }
  },
  "id": 1
}
```
Retour :

```json
{
  "jsonrpc": "2.0",
  "result": {
    "success": true,
    "message": "Successfully modified: /path/to/config.txt"
  },
  "id": 1
}
```
Méthode - TunnelManager --------

La méthode `TunnelManager` est utilisée pour créer, modifier, obtenir, démarrer, arrêter, redémarrer et supprimer des contrôleurs I2PTunnel.

Paramètres requis :

- `Name` - nom du tunnel. C'est l'identifiant du tunnel.
- `Action` - action à effectuer :
  - `create`
  - `edit`
  - `get`
  - `start`
  - `stop`
  - `restart`
  - `delete`

Paramètres facultatifs :

- `All` - booléen, indique si l'action doit être appliquée à tous les tunnels. Ceci n'est valide que pour les actions `start`, `stop` et `restart`.

Types de tunnel pris en charge pour `create` :

- `client`
- `httpclient`
- `ircclient`
- `socks`
- `socksirc`
- `connectclient`
- `streamrclient`

- `server`
- `httpserver`
- `httpbidirserver`
- `ircserver`
- `streamrserver`

Paramètres courants pour la création/l'édition de tunnels :

- `Type` - type de tunnel. Requis pour `create`.
- `NewName` - nom facultatif lors de la modification.
- `Port` - port local d'écoute.
- `TargetHost` ou `Host` - hôte cible pour les tunnels serveur.
- `TargetPort` - port cible pour les tunnels serveur.
- `TargetDestination` ou `Destination` - destination pour les tunnels client qui en nécessitent une.
- `StartOnLoad` - booléen, indique si le tunnel doit démarrer au chargement.
- `Description` - description du tunnel.
- `ReachableBy` - interface/adresse sur laquelle le tunnel écoute.
- `Shared` - booléen, indique si le tunnel client doit être partagé.
- `UseSSL` - booléen, active le SSL là où il est pris en charge.
- `TunnelLength` - longueur du tunnel, de `0` à `3`.
- `TunnelVariance` - variance du tunnel, de `-2` à `2`.
- `TunnelQuantity` - nombre de tunnels, de `1` à `6`.
- `TunnelBackupQuantity` - nombre de tunnels de secours, de `0` à `3`.
- `SigType` - type de clé de signature.
- `EncType` - type de chiffrement.
- `CustomOptions` - options personnalisées du tunnel.

Options du proxy client :

- `ProxyList`
- `UseOutproxyPlugin`
- `ProxyAuth`
- `ProxyUsername`
- `ProxyPassword`
- `OutproxyAuth`
- `OutproxyUsername`
- `OutproxyPassword`
- `OutproxyType`
- `SSLProxies`
- `JumpList`

Options de gestion des clients :

- `ConnectDelay`
- `Profile`
- `DelayOpen`
- `Reduce`
- `ReduceCount`
- `ReduceTime`
- `Close`
- `CloseTime`
- `NewDest`
- `PersistentClientKey`
- `PrivKeyFile`

Options de filtrage du client HTTP :

- `AllowUserAgent`
- `AllowReferer`
- `AllowAccept`
- `AllowInternalSSL`

Options du serveur :

- `WebsiteHostname` ou `SpoofedHost`
- `BlockAccessInProxies`
- `BlockUserAgents`
- `UserAgents`
- `UniqueLocalAddressPerClient`
- `BlockReferers`
- `MultiHoming`
- `AccessOption`
- `AccessList`
- `FilterFilePath`
- `MaxConcurrentConns`
- `ClientPerMinute`
- `ClientPerHour`
- `ClientPerDay`
- `TotalInPerMinute`
- `TotalInPerHour`
- `TotalInPerDay`
- `PostLimit`
- `PostLimitTime`
- `PerClientPeriod`
- `TotalPeriod`
- `TotalBanTime`

Options du LeaseSet :

- `EncryptLeaseSet` - l'une des options suivantes :
  - `disable`
  - `encrypted (aes)`
  - `blinded`
  - `blinded with lookup password`
  - `encrypted (psk)`
  - `encrypted with lookup password (psk)`
  - `encrypted with per-user key (psk)`
  - `encrypted with lookup password and per-user key (psk)`
  - `encrypted with per-user key (dh)`
  - `encrypted with lookup password and per-user key (dh)`
- `OptionalLookup`
- `LeaseSetClientAuths`

Créer un exemple :

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "create",
    "Type": "client",
    "Port": 7656,
    "TargetDestination": "exampleDestinationString",
    "StartOnLoad": false,
    ....
  },
  "id": 1
}
```
Retour :

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - created tunnel example-client" OR "error - { error message }",
    "results": [ {/* information about where persistent keys are stored */} ]
  },
  "id": 1
}
```
Exemple de modification :

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "edit",
    "NewName": "renamed-client",
    "Port": 7657,
    "TargetDestination": "newDestinationString",
    "StartOnLoad": true
  },
  "id": 1
}
```
Retour :

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - edited tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
Exemple de récupération :

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "get"
  },
  "id": 1
}
```
Retour :

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - options for example-client" OR "error - { error message }",
    "info": {
      "client": true,
      "status": "running",
      "persistentClientKey": false,
      "offlineKeys": false,
      "targetDestination": "exampleDestinationString",
      "localDestination": "exampleBase64Destination",
      "destination": "exampleBase64Destination",
      "destinationB32": "example.b32.i2p",
      "rawConfig": {
        "name": "example-client",
        "type": "client"
      }
    }
  },
  "id": 1
}
```
Exemples de Démarrer, Arrêter, Redémarrer, Supprimer. Ils suivent la même structure, avec simplement différents paramètres `Action` :

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "start"
  },
  "id": 1
}
```
Retour :

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - starting tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
Méthode - ClientServicesInfo *(adopté depuis i2pd)* -------------------------------------------------

La méthode `ClientServicesInfo` renvoie des informations sur l'état des services clients en cours d'exécution sur le routeur. Incluez les clés de service souhaitées (avec n'importe quelle valeur) dans `params` pour demander l'état de chaque service.

Paramètres pris en charge :

- `I2PTunnel` - renvoie une carte des noms de tunnel configurés associés à leurs adresses, répartie en sous-objets `client` et `server`.
- `HTTPProxy` - renvoie l'état d'activation du proxy HTTP et son adresse.
- `SOCKS` - renvoie l'état d'activation du proxy SOCKS et son adresse.
- `SAM` - renvoie l'état d'activation du pont SAM et les informations des sessions actives.
- `BOB` - renvoie l'état d'activation du pont BOB. (Obsolète dans Java I2P ; renvoie toujours `false`.)
- `I2CP` - renvoie l'état d'activation du serveur I2CP.

Exemple :

```json
{
  "jsonrpc": "2.0",
  "method": "ClientServicesInfo",
  "params": {
    "I2PTunnel": "",
    "SAM": ""
  },
  "id": 1
}
```
Retour :

```json
{
  "jsonrpc": "2.0",
  "result": {
    "I2PTunnel": {
      "client": {"my-client": {"address": "example.b32.i2p"}},
      "server": {"my-server": {"address": "example.b32.i2p", "port": 8080}}
    },
    "SAM": {
      "enabled": true,
      "sessions": {}
    }
  },
  "id": 1
}
```
Compatibilité =============

La compatibilité avec l'API i2pcontrol existante doit être conservée, car les nouvelles méthodes et paramètres sont ajoutés d'une manière qui n'interfère pas avec les fonctionnalités existantes. Les applications existantes utilisant l'API i2pcontrol devraient continuer à fonctionner sans modification, tandis que les nouvelles applications pourront tirer parti des informations et fonctionnalités supplémentaires offertes par cette proposition.

Implémentation ==============

Java I2P --------

Cette proposition n'est pas encore implémentée dans Java I2P, mais le code est disponible dans le dépôt [i2p.plugins.i2pcontrol](https://github.com/i2p/i2p.plugins.i2pcontrol) sous la demande d'intégration [#6](https://github.com/i2p/i2p.plugins.i2pcontrol/pull/6). Cela a été fait afin de permettre les tests et le développement des nouvelles méthodes sans affecter le code existant. Cela sera intégré au dépôt principal d'I2P, dans le répertoire i2pcontrol, une fois que le code sera prêt pour un usage en production.

i2pd ----

Les méthodes et paramètres marqués comme « (adoptés de i2pd) » sont implémentés dans i2pd et inchangés dans cette proposition. Les extensions de i2pd ne nécessiteront aucune modification dans le cadre de cette proposition. Les parties non marquées de cette proposition ne sont pas implémentées dans i2pd.

go-i2p ------

go-i2p est motivé à suivre cette proposition afin de permettre et améliorer son application de console de routeur. Il adoptera et mettra en œuvre la proposition à l'avenir.

emissary --------

La probabilité d'adoption dans Emissary est inconnue à l'heure actuelle, mais Emissary devrait probablement bénéficier de cette proposition de la même manière que go-i2p.

Performance ===========

Aucun impact sur les performances n'est prévu.
