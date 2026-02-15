---
title: "Spécification SAM V2"
description: "Protocole de messagerie anonyme simple hérité version 2 (obsolète)"
slug: "samv2"
aliases:
  - "/fr/docs/api/samv2"
  - "/fr/docs/api/samv2/"
lastUpdated: "2025-03"
accurateFor: "0.9.20"
---

## Avertissement - Obsolète - Non pris en charge - Utilisez [SAMv3](/docs/api/samv3)

Voici la version 2 d'un protocole client simple pour interagir avec I2P.

SAMv2 a été introduit dans la version 0.6.1.31 d'I2P. Les différences significatives par rapport à SAMv1 sont marquées par "\*\*\*". Alternatives : [SAMv1](/docs/api/sam), [SAMv3](/docs/api/samv3), [BOB](/docs/api/bob).

## Changements de la version 2

SAM V2 a été introduit dans la version 0.6.1.31 d'I2P. Comparé à la version 1, SAM v2 fournit un moyen de gérer plusieurs sockets sur la même destination I2P *en parallèle*, c'est-à-dire que le client n'a pas à attendre que les données soient envoyées avec succès sur un socket avant d'envoyer des données sur un autre socket. Toutes les données transitent par le même socket client\<--\>SAM. Pour les sockets multiples, voir [SAM V3](/docs/api/samv3).

### Modifications d'I2P 0.9.14

La version signalée reste "2.0".

- DEST GENERATE prend maintenant en charge un paramètre SIGNATURE_TYPE.
- Le paramètre MIN dans HELLO VERSION est maintenant optionnel.
- Les paramètres MIN et MAX dans HELLO VERSION prennent maintenant en charge les versions à un seul chiffre comme "3".

## Protocole Version 2

L'application cliente communique avec le pont SAMv3, qui gère toutes les fonctionnalités I2P (en utilisant la bibliothèque de streaming pour les flux virtuels, ou I2CP directement pour les messages asynchrones).

Toute communication client\<--\>pont SAM n'est ni chiffrée ni authentifiée sur une seule socket TCP. L'accès au pont SAM doit être protégé par des pare-feu ou d'autres moyens (peut-être que le pont peut avoir des ACL sur les adresses IP dont il accepte les connexions).

Tous ces messages SAM sont envoyés sur une seule ligne en ASCII brut, terminés par le caractère de nouvelle ligne (\\n). Le formatage présenté ci-dessous est uniquement pour la lisibilité, et bien que les deux premiers mots de chaque message doivent rester dans leur ordre spécifique, l'ordre des paires clé=valeur peut changer (par exemple, "ONE TWO A=B C=D" ou "ONE TWO C=D A=B" sont toutes deux des constructions parfaitement valides). De plus, le protocole est sensible à la casse.

Les messages SAM sont interprétés en UTF-8. Les paires clé=valeur doivent être séparées par un seul espace. Les valeurs peuvent être entourées de guillemets doubles si elles contiennent des espaces, par exemple clé="texte de valeur longue". Il n'y a pas de mécanisme d'échappement.

La communication peut prendre trois formes distinctes :

- [Flux virtuels](/docs/api/streaming)
- [Datagrammes avec réponse](/docs/specs/datagrams#repliable) (messages avec un champ FROM)
- [Datagrammes anonymes](/docs/specs/datagrams#raw) (messages anonymes bruts)

## Handshake de connexion SAM

Aucune communication SAM ne peut avoir lieu tant que le client et le bridge ne se sont pas mis d'accord sur une version de protocole, ce qui se fait par l'envoi d'un HELLO par le client et l'envoi d'une HELLO REPLY par le bridge :

```
HELLO VERSION MIN=$min MAX=$max
```
et

```
*** HELLO REPLY RESULT=$result VERSION=2.0
```
À partir d'I2P 0.9.14, le paramètre MIN est optionnel. Le paramètre MAX doit être fourni et être supérieur ou égal à "2" et inférieur à "3" pour utiliser la version 2.

La valeur RESULT peut être l'une des suivantes :

- `OK`
- `NOVERSION`

## Sessions SAM

Une session SAM est créée lorsqu'un client ouvre un socket vers le pont SAM, effectue une négociation, et envoie un message SESSION CREATE, et la session se termine lorsque le socket est déconnecté.

Chaque Destination I2P ne peut être utilisée que pour une seule session SAM à la fois, et ne peut utiliser qu'une seule de ces formes (les messages reçus par d'autres formes sont supprimés).

Le message SESSION CREATE envoyé par le client au pont est le suivant :

```
SESSION CREATE
        STYLE={STREAM,DATAGRAM,RAW}
        DESTINATION={$name,TRANSIENT}
        [DIRECTION={BOTH,RECEIVE,CREATE}]
        [option=value]*
```
DESTINATION spécifie quelle destination doit être utilisée pour envoyer et recevoir des messages/flux. Si un $name est donné, le pont SAM recherche dans son propre stockage local (le fichier sam.keys) une destination associée (et une clé privée). Si aucune association correspondant à ce nom n'existe, il en crée une nouvelle. Si la destination est spécifiée comme TRANSIENT, il en crée toujours une nouvelle.

Notez que DESTINATION est un identifiant, *pas* des données encodées en Base 64. Pour spécifier la Destination, vous devez utiliser [SAM V3](/docs/api/samv3).

La DIRECTION ne peut être spécifiée que pour les sessions STREAM, indiquant au pont que le client va soit créer ou recevoir des flux, ou les deux. Si cela n'est pas spécifié, BOTH sera supposé. Tenter de créer un flux sortant quand DIRECTION=RECEIVE devrait résulter en une erreur, et les flux entrants quand DIRECTION=CREATE seront ignorés.

Les options supplémentaires données doivent être transmises à la configuration de session I2P si elles ne sont pas interprétées par le pont SAM (par exemple "tunnels.depthInbound=0"). Ces options sont documentées ci-dessous.

Le pont SAM lui-même devrait déjà être configuré avec le router avec lequel il doit communiquer via I2P (bien que si nécessaire, il pourrait y avoir un moyen de fournir une substitution, par exemple i2cp.tcp.host=localhost et i2cp.tcp.port=7654).

Après avoir reçu le message de création de session, le pont SAM répondra avec un message de statut de session, comme suit :

```
SESSION STATUS
        RESULT=$result
        DESTINATION={$name,TRANSIENT}
        [MESSAGE=...]
```
La valeur RESULT peut être l'une des suivantes :

- `OK`
- `DUPLICATED_DEST`
- `I2P_ERROR`
- `INVALID_KEY`

Si ce n'est pas OK, le MESSAGE doit contenir des informations lisibles par l'homme expliquant pourquoi la session n'a pas pu être créée.

Notez qu'aucun avertissement n'est donné si le $name n'est pas trouvé et qu'une destination transitoire est créée à la place. Notez que la destination transitoire base 64 réelle n'est pas affichée dans la réponse ; c'est le $name ou TRANSIENT tel que fourni dans SESSION CREATE. Si vous avez besoin de ces fonctionnalités, vous devez utiliser [SAM V3](/docs/api/samv3).

## Flux virtuels SAM

Les flux virtuels sont garantis d'être envoyés de manière fiable et dans l'ordre, avec notification d'échec et de succès dès qu'elle est disponible.

Après avoir établi la session avec STYLE=STREAM, le client et le pont SAM peuvent envoyer de manière asynchrone divers messages dans les deux sens pour gérer les flux, comme énuméré ci-dessous :

```
STREAM CONNECT
       ID=$id
       DESTINATION=$destination
```
Ceci établit une nouvelle connexion virtuelle depuis la destination locale vers le pair spécifié, en la marquant avec l'ID unique limité à la session. L'ID unique est un entier ASCII en base 10 de 1 à (2^31-1).

La $destination est la base 64 de la [Destination](/docs/specs/common-structures#type_Destination), qui fait 516 caractères base 64 ou plus (387 octets ou plus en binaire), selon le type de signature.

Le pont SAM répond à cela avec un message de statut de flux :

```
STREAM STATUS
       RESULT=$result
       ID=$id
       [MESSAGE=...]
```
La valeur RESULT peut être l'une des suivantes :

- `OK`
- `CANT_REACH_PEER`
- `I2P_ERROR`
- `INVALID_KEY`
- `TIMEOUT`

Si le RESULT est OK, la destination spécifiée est active et a autorisé la connexion ; si la connexion n'était pas possible (timeout, etc), RESULT contiendra la valeur d'erreur appropriée (accompagnée d'un MESSAGE optionnel lisible par l'homme).

Du côté réception, le pont SAM notifie simplement le client comme suit :

```
STREAM CONNECTED
       DESTINATION=$destination
       ID=$id
```
Ceci indique au client que la destination donnée a créé une connexion virtuelle avec lui. Le flux de données suivant sera marqué avec l'ID unique donné, qui est un entier base 10 ASCII de -1 à -(2^31-1).

La $destination est le base 64 de la [Destination](/docs/specs/common-structures#type_Destination), qui fait 516 caractères base 64 ou plus (387 octets ou plus en binaire), selon le type de signature.

Lorsque le client souhaite envoyer des données sur la connexion virtuelle, il procède comme suit :

```
STREAM SEND
       ID=$id
       SIZE=$numBytes\n[$numBytes of data]
```
Ceci demande au pont SAM d'ajouter les données spécifiées au tampon envoyé au pair via la connexion virtuelle. La taille d'envoi $numBytes correspond au nombre d'octets 8 bits inclus après le saut de ligne, qui peut être de 1 à 32768 (32 Ko).

**\*\*\* Le bridge SAM répond immédiatement avec :**

```
*** STREAM SEND
***        ID=$id
***        RESULT=$result
***        STATE=$bufferState
```
**\*\*\*** où $bufferState peut être :

- `BUFFER_FULL` - Le buffer de SAM contient 32 Ko ou plus de données à envoyer, et les requêtes SEND suivantes échoueront
- `READY` - Le buffer de SAM n'est pas plein, et la prochaine requête SEND est garantie de réussir

**\*\*\*** et $result est l'un des suivants :

- `OK` - les données ont été mises en mémoire tampon avec succès
- `FAILED` - le tampon était plein, aucune donnée n'a été mise en mémoire tampon

**\*\*\*** Si le pont SAM a répondu avec BUFFER_FULL, il enverra un autre message dès que son tampon sera à nouveau disponible :

```
*** STREAM READY_TO_SEND ID=$id
```
**\*\*\*** Lorsque le résultat est OK, le pont SAM fera alors de son mieux pour livrer le message aussi rapidement et efficacement que possible, en regroupant peut-être plusieurs messages SEND ensemble. S'il y a une erreur lors de la livraison des données, ou si le côté distant ferme la connexion, le pont SAM informera le client :

```
STREAM CLOSED
       RESULT=$result
       ID=$id
       [MESSAGE=...]
```
La valeur RESULT peut être l'une des suivantes :

- `OK`
- `CANT_REACH_PEER`
- `I2P_ERROR`
- `PEER_NOT_FOUND`
- `TIMEOUT`

Si la connexion a été proprement fermée par l'autre pair, $result est défini sur OK. Si $result n'est pas OK, MESSAGE peut transmettre un message descriptif, tel que "peer unreachable", etc. Chaque fois qu'un client souhaite fermer la connexion, il envoie au pont SAM le message de fermeture :

```
STREAM CLOSE
       ID=$id
```
Le bridge nettoie ensuite ce dont il a besoin et rejette cet ID - aucun autre message ne peut être envoyé ou reçu sur celui-ci.

Pour l'autre côté de la communication, chaque fois que le pair a envoyé des données et qu'elles sont disponibles pour le client, le pont SAM les livrera immédiatement :

```
STREAM RECEIVED
       ID=$id
       SIZE=$numBytes\n[$numBytes of data]
```
**\*\*\*** Avec SAM version 2.0, cependant, le client doit d'abord indiquer au pont SAM quelle quantité de données entrantes est autorisée pour toute la session, en envoyant un message :

```
*** STREAM RECEIVE
***        ID=$id
***        LIMIT=$limit\n
```
**\*\*\*** où $limit peut être :

- `NONE` - le pont SAM continuera à écouter et délivrer les données entrantes (même comportement que dans la version 1.0)
- un entier (inférieur à 2^64) - le nombre d'octets reçus après lequel le pont SAM cessera d'écouter sur le flux entrant. Chaque fois que le client est prêt à accepter plus d'octets du flux, il doit envoyer à nouveau un tel message, avec une $limit plus grande.

**\*\*\*** Le client doit envoyer de tels messages STREAM RECEIVE après que la connexion au pair ait été établie, c'est-à-dire après que le client ait reçu un "STREAM CONNECTED" ou un "STREAM STATUS RESULT=OK" du pont SAM.

Tous les flux sont implicitement fermés lorsque la connexion entre le pont SAM et le client est interrompue.

## Datagrammes SAM avec réponse

Bien qu'I2P ne contienne pas intrinsèquement d'adresse FROM, pour faciliter l'utilisation, une couche supplémentaire est fournie sous forme de datagrammes avec réponse - des messages non ordonnés et non fiables allant jusqu'à 31744 octets qui incluent une adresse FROM (laissant jusqu'à 1 Ko pour le matériel d'en-tête). Cette adresse FROM est authentifiée en interne par SAM (en utilisant la clé de signature de la destination pour vérifier la source) et inclut une prévention contre la rejeu.

La taille minimale est de 1. Pour une fiabilité de livraison optimale, la taille maximale recommandée est d'environ 11 Ko.

Après avoir établi une session SAM avec STYLE=DATAGRAM, le client peut envoyer au bridge SAM :

```
DATAGRAM SEND
         DESTINATION=$destination
         SIZE=$numBytes\n[$numBytes of data]
```
Lorsqu'un datagramme arrive, le pont le livre au client via :

```
DATAGRAM RECEIVED
         DESTINATION=$destination
         SIZE=$numBytes\n[$numBytes of data]
```
La $destination est la base 64 de la [Destination](/docs/specs/common-structures#type_Destination), qui fait 516 caractères base 64 ou plus (387 octets ou plus en binaire), selon le type de signature.

Le bridge SAM n'expose jamais au client les en-têtes d'authentification ou autres champs, seulement les données que l'expéditeur a fournies. Ceci continue jusqu'à ce que la session soit fermée (par le client qui interrompt la connexion).

## Datagrammes anonymes SAM

Tirant le maximum de la bande passante d'I2P, SAM permet aux clients d'envoyer et de recevoir des datagrammes anonymes, laissant l'authentification et les informations de réponse à la charge du client lui-même. Ces datagrammes ne sont pas fiables et non ordonnés, et peuvent faire jusqu'à 32768 octets.

La taille minimale est de 1. Pour une fiabilité de livraison optimale, la taille maximale recommandée est d'environ 11 Ko.

Après avoir établi une session SAM avec STYLE=RAW, le client peut envoyer au pont SAM :

```
RAW SEND
    DESTINATION=$destination
    SIZE=$numBytes\n[$numBytes of data]
```
Le $destination est l'encodage base 64 de la [Destination](/docs/specs/common-structures#type_Destination), qui fait 516 caractères base 64 ou plus (387 octets ou plus en binaire), selon le type de signature.

Lorsqu'un datagramme brut arrive, le pont le livre au client via :

```
RAW RECEIVED
    SIZE=$numBytes\n[$numBytes of data]
```
## Fonctionnalité Utilitaire SAM

Le message suivant peut être utilisé par le client pour interroger le pont SAM concernant la résolution de noms :

```
NAMING LOOKUP
       NAME=$name
```
à laquelle il est répondu par

```
NAMING REPLY
       RESULT=$result
       NAME=$name
       [VALUE=$destination]
       [MESSAGE=$message]
```
La valeur RESULT peut être l'une des suivantes :

- `OK`
- `INVALID_KEY`
- `KEY_NOT_FOUND`

Si NAME=ME, alors la réponse contiendra la destination utilisée par la session courante (utile si vous utilisez une destination TRANSIENT). Si $result n'est pas OK, MESSAGE peut contenir un message descriptif, tel que "bad format", etc.

La $destination est l'encodage base 64 de la [Destination](/docs/specs/common-structures#type_Destination), qui fait 516 caractères base 64 ou plus (387 octets ou plus en binaire), selon le type de signature.

Les clés base64 publiques et privées peuvent être générées en utilisant le message suivant :

```
DEST GENERATE
```
qui reçoit pour réponse

```
DEST REPLY
     PUB=$destination
     PRIV=$privkey
```
À partir d'I2P 0.9.14, un paramètre optionnel SIGNATURE_TYPE est pris en charge. La valeur SIGNATURE_TYPE peut être n'importe quel nom (par exemple ECDSA_SHA256_P256, insensible à la casse) ou numéro (par exemple 1) qui est pris en charge par [Key Certificates](/docs/specs/common-structures#type_Certificate). La valeur par défaut est DSA_SHA1.

La $destination est la base 64 de la [Destination](/docs/specs/common-structures#type_Destination), qui fait 516 caractères base 64 ou plus (387 octets ou plus en binaire), selon le type de signature.

Le $privkey est la base 64 de la concaténation de la [Destination](/docs/specs/common-structures#type_Destination) suivie de la [Private Key](/docs/specs/common-structures#type_PrivateKey) suivie de la [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), ce qui représente 884 caractères base 64 ou plus (663 octets ou plus en binaire), selon le type de signature.

## Valeurs RESULT

Voici les valeurs que peut contenir le champ RESULT, avec leur signification :

| Valeur | Signification |
|--------|---------------|
| `OK` | Opération terminée avec succès |
| `CANT_REACH_PEER` | Le pair existe, mais ne peut pas être atteint |
| `DUPLICATED_DEST` | La Destination spécifiée est déjà utilisée |
| `I2P_ERROR` | Une erreur I2P générique (par ex. déconnexion I2CP, etc.) |
| `INVALID_KEY` | La clé spécifiée n'est pas valide (mauvais format, etc.) |
| `KEY_NOT_FOUND` | Le système de nommage ne peut pas résoudre le nom donné |
| `PEER_NOT_FOUND` | Le pair ne peut pas être trouvé sur le réseau |
| `TIMEOUT` | Délai d'attente dépassé en attendant un événement (par ex. réponse du pair) |
## Options de Tunnel, I2CP et Streaming

Ces options peuvent être passées sous forme de paires nom=valeur à la fin d'une ligne SAM SESSION CREATE.

Toutes les sessions peuvent inclure [des options I2CP telles que les longueurs de tunnel](/docs/protocol/i2cp#options). Les sessions STREAM peuvent inclure [des options de la bibliothèque Streaming](/docs/api/streaming#options). Consultez ces références pour les noms d'options et les valeurs par défaut.

## Notes sur Base 64

L'encodage Base 64 doit utiliser l'alphabet Base 64 standard I2P "A-Z, a-z, 0-9, -, ~".

## Implémentations de bibliothèques client

Des bibliothèques client sont disponibles pour C, C++, C#, Perl et Python. Elles se trouvent dans le répertoire apps/sam/ du package source I2P. Certaines peuvent être plus anciennes et n'ont pas été mises à jour pour le support SAMv2.

## Configuration SAM par défaut

Le port SAM par défaut est 7656. SAM n'est pas activé par défaut dans le routeur I2P ; il doit être démarré manuellement, ou configuré pour démarrer automatiquement, sur la page de configuration des clients dans la console du routeur, ou dans le fichier clients.config.
