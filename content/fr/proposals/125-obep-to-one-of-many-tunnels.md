---
title: "Livraison OBEP vers 1-sur-N ou N-sur-N Tunnels"
number: "125"
author: "zzz, str4d"
created: "2016-03-10"
lastupdated: "2017-04-07"
status: "Open"
thread: "http://zzz.i2p/topics/2099"
toc: true
---
## Aperçu

Cette proposition couvre deux améliorations visant à améliorer les performances du réseau :

- Déléguer au OBEP le choix du IBGW en lui fournissant une liste d'alternatives au lieu d'une seule option.

- Permettre le routage de paquets multicast au niveau du OBEP.


## Motivation

Dans le cas d'une connexion directe, l'idée est de réduire la congestion du réseau en donnant au OBEP une certaine flexibilité dans la manière dont il se connecte aux IBGWs. La possibilité de spécifier plusieurs tunnels permet également d'implémenter le multicast au niveau du OBEP (en envoyant le message à tous les tunnels spécifiés).

Une alternative à la partie déléguée de cette proposition serait d'envoyer un hachage de LeaseSet, similaire à la capacité existante de spécifier un hachage d'identité de routeur cible [RouterIdentity](/docs/specs/common-structures/#common-structure-specification). Cela permettrait d'obtenir un message plus petit et potentiellement un LeaseSet plus récent. Cependant :

1. Cela obligerait le OBEP à effectuer une recherche.

2. Le LeaseSet pourrait ne pas être publié sur un nœud floodfill, donc la recherche échouerait.

3. Le LeaseSet pourrait être chiffré, donc le OBEP ne pourrait pas accéder aux leases.

4. Spécifier un LeaseSet révèle au OBEP la [Destination](/docs/specs/common-structures/#destination) du message, qu'il ne pourrait autrement découvrir qu'en analysant tous les LeaseSets du réseau à la recherche d'une correspondance de lease.


## Conception

L'expéditeur (OBGW) placerait certains (tous ?) des [Leases](/docs/specs/common-structures/#lease) cibles dans les instructions de livraison [TUNNEL-DELIVERY](/docs/specs/i2np/#tunnel-message-delivery-instructions) au lieu de n'en choisir qu'un seul.

Le OBEP sélectionnerait l'un de ces leases pour la livraison. Le OBEP choisirait, si disponible, un tunnel auquel il est déjà connecté ou qu'il connaît déjà. Cela rendrait le chemin OBEP-IBGW plus rapide et plus fiable, tout en réduisant le nombre total de connexions dans le réseau.

Nous disposons d'un type de livraison inutilisé (0x03) et de deux bits restants (0 et 1) dans les indicateurs (flags) de TUNNEL-DELIVERY, que nous pouvons exploiter pour implémenter ces fonctionnalités.


## Implications en matière de sécurité

Cette proposition ne modifie pas la quantité d'informations divulguées concernant la Destination cible du OBGW ni sa vision du NetDB :

- Un adversaire contrôlant le OBEP et analysant les LeaseSets depuis le NetDB peut déjà déterminer si un message est envoyé à une Destination particulière, en recherchant le couple TunnelId / RouterIdentity. Au pire, la présence de plusieurs Leases dans le TMDI pourrait accélérer la recherche d'une correspondance dans la base de données de l'adversaire.

- Un adversaire exploitant une Destination malveillante peut déjà obtenir des informations sur la vision du NetDB de la victime qui se connecte, en publiant des LeaseSets contenant différents tunnels entrants sur différents nœuds floodfill, puis en observant par quels tunnels le OBGW se connecte. Du point de vue de l'attaquant, le fait que le OBEP choisisse le tunnel à utiliser est fonctionnellement identique au fait que le OBGW fasse lui-même le choix.

Le drapeau multicast révèle au OBEP le fait que le OBGW effectue un envoi en multicast. Cela crée un compromis entre performance et confidentialité qui doit être pris en compte lors de l'implémentation de protocoles de niveau supérieur. Étant un drapeau optionnel, les utilisateurs peuvent prendre la décision adaptée à leur application. Il pourrait être bénéfique que ce comportement soit activé par défaut pour les applications compatibles, car une utilisation généralisée par diverses applications réduirait la fuite d'information sur l'application spécifique à l'origine du message.


## Spécification

Les instructions de livraison du premier fragment seraient modifiées comme suit :

```
+----+----+----+----+----+----+----+----+
  |flag|  Tunnel ID (opt)  |              |
  +----+----+----+----+----+              +
  |                                       |
  +                                       +
  |         To Hash (optional)            |
  +                                       +
  |                                       |
  +                        +----+----+----+
  |                        |dly | Message
  +----+----+----+----+----+----+----+----+
   ID (opt) |extended opts (opt)|cnt | (o)
  +----+----+----+----+----+----+----+----+
   Tunnel ID N   |                        |
  +----+----+----+                        +
  |                                       |
  +                                       +
  |         To Hash N (optional)          |
  +                                       +
  |                                       |
  +              +----+----+----+----+----+
  |              | Tunnel ID N+1 (o) |    |
  +----+----+----+----+----+----+----+    +
  |                                       |
  +                                       +
  |         To Hash N+1 (optional)        |
  +                                       +
  |                                       |
  +                                  +----+
  |                                  | sz
  +----+----+----+----+----+----+----+----+
       |
  +----+

flag ::
       1 octet
       Ordre des bits : 76543210
       bits 6-5 : type de livraison
                  0x03 = TUNNELS
       bit 0 : multicast ? Si 0, livrer à un seul des tunnels
                           Si 1, livrer à tous les tunnels
                           Doit être à 0 pour assurer la compatibilité avec les usages futurs
                           si le type de livraison n'est pas TUNNELS

Count ::
       1 octet
       Optionnel, présent si le type de livraison est TUNNELS
       2-255 - Nombre de paires id/hash suivantes

Tunnel ID :: TunnelId
To Hash ::
       36 octets chacun
       Optionnel, présent si le type de livraison est TUNNELS
       paires id/hash

Longueur totale : Longueur typique :
       75 octets pour une livraison TUNNELS avec count=2 (message de tunnel non fragmenté) ;
       79 octets pour une livraison TUNNELS avec count=2 (premier fragment)

Le reste des instructions de livraison reste inchangé
```


## Compatibilité

Les seuls pairs devant comprendre la nouvelle spécification sont les OBGWs et les OBEPs. Nous pouvons donc rendre ce changement compatible avec le réseau existant en conditionnant son utilisation à la version cible d'I2P :

* Les OBGWs doivent sélectionner des OBEPs compatibles lors de la construction des tunnels sortants, en fonction de la version d'I2P annoncée dans leur [RouterInfo](/docs/specs/common-structures/#routerinfo).

* Les pairs annonçant la version cible doivent supporter l'analyse des nouveaux indicateurs (flags) et ne doivent pas rejeter les instructions comme étant invalides.


## Références

* [Destination](/docs/specs/common-structures/#destination)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [RouterIdentity](/docs/specs/common-structures/#routeridentity)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TUNNEL-DELIVERY](/docs/specs/common-structures/#tunnelmessagedeliveryinstructions)
* [TunnelId](/docs/specs/common-structures/#tunnelid)
* [VERSIONS](/docs/specs/i2np/#protocol-versions)
