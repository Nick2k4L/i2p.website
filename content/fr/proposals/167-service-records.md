---
title: "Enregistrements de service dans LS2"
number: "167"
author: "zzz, orignal, eyedeekay"
created: "2024-06-22"
lastupdated: "2025-04-03"
status: "Fermé"
thread: "http://zzz.i2p/topics/3641"
target: "0.9.66"
toc: true
---
## Statut
Approuvé lors de la deuxième relecture le 2025-04-01 ; les spécifications sont mises à jour ; pas encore implémenté.


## Aperçu

I2P ne dispose pas d'un système DNS centralisé.  
Cependant, le carnet d'adresses, combiné au système de noms d'hôte b32, permet  
au routeur de rechercher des destinations complètes et de récupérer les ensembles de baux (lease sets), qui contiennent  
une liste de passerelles et de clés afin que les clients puissent se connecter à cette destination.

Ainsi, les ensembles de baux (leasesets) ressemblent un peu à un enregistrement DNS. Mais il n'existe actuellement aucun mécanisme permettant  
de savoir si cet hôte prend en charge des services, que ce soit sur cette destination ou une autre,  
d'une manière similaire aux enregistrements [SRV DNS](https://en.wikipedia.org/wiki/SRV_record) définis dans [RFC 2782](https://datatracker.ietf.org/doc/html/rfc2782).

La première application possible serait le courrier électronique pair-à-pair.  
Autres applications possibles : DNS, GNS, serveurs de clés, autorités de certification, serveurs de temps,  
BitTorrent, cryptomonnaies, autres applications pair-à-pair.


## Propositions et alternatives associées

### Listes de services

La [Proposition 123](/proposals/123-new-netdb-entries/) LS2 définissait des « enregistrements de service » indiquant qu'une destination  
participait à un service global. Les floodfills regrouperaient ces enregistrements  
en « listes de services » globales.  
Cela n'a jamais été implémenté en raison de la complexité, du manque d'authentification,  
de préoccupations liées à la sécurité et au spam.

Cette proposition est différente en ce sens qu'elle fournit une recherche de service pour une destination spécifique,  
et non un ensemble global de destinations pour un service global.

### GNS

GNS propose que chacun exécute son propre serveur DNS.  
Cette proposition est complémentaire, car nous pourrions utiliser des enregistrements de service pour indiquer  
que GNS (ou DNS) est pris en charge, avec un nom de service standard « domain » sur le port 53.

### Dot well-known

Il a été [proposé](http://i2pforum.i2p/viewtopic.php?p=3102) que les services soient recherchés via une requête HTTP vers  
/.well-known/i2pmail.key. Cela nécessite que chaque service ait un site web associé pour héberger la clé. La plupart des utilisateurs n'exécutent pas de sites web.

Une solution de contournement serait de supposer qu'un service pour une adresse b32 s'exécute effectivement  
sur cette adresse b32. Ainsi, rechercher le service pour example.i2p nécessiterait  
la récupération HTTP depuis http://example.i2p/.well-known/i2pmail.key, mais  
un service pour aaa...aaa.b32.i2p ne nécessiterait pas cette recherche, on pourrait se connecter directement.

Mais cela crée une ambiguïté, car example.i2p peut aussi être adressé par son b32.

### Enregistrements MX

Les enregistrements SRV sont simplement une version générique des enregistrements MX pour n'importe quel service.  
« _smtp._tcp » est l'enregistrement « MX ».  
Il n'y a pas besoin d'enregistrements MX si nous avons des enregistrements SRV, et les enregistrements MX  
seuls ne fournissent pas un enregistrement générique pour n'importe quel service.


## Conception

Les enregistrements de service sont placés dans la section des options de [LS2](/docs/specs/common-structures/).  
La section d'options LS2 est actuellement inutilisée.  
Non pris en charge pour LS1.  
Cela est similaire à la [proposition sur la bande passante des tunnels](/proposals/168-tunnel-bandwidth/),  
qui définit des options pour les enregistrements de construction de tunnel.

Pour rechercher l'adresse d'un service pour un nom d'hôte ou un b32 spécifique, le routeur récupère l'  
ensemble de baux (leaseset) et recherche l'enregistrement de service dans les propriétés.

Le service peut être hébergé sur la même destination que l'ensemble de baux lui-même, ou peut faire référence  
à un autre nom d'hôte/b32.

Si la destination cible du service est différente, l'ensemble de baux cible doit également  
inclure un enregistrement de service, pointant vers lui-même, indiquant qu'il prend en charge le service.

La conception ne nécessite aucun support spécial, aucune mise en cache ni aucun changement dans les floodfills.  
Seul l'éditeur de l'ensemble de baux et le client recherchant un enregistrement de service  
doivent prendre en charge ces modifications.

De légères extensions d'I2CP et de SAM sont proposées pour faciliter la récupération des  
enregistrements de service par les clients.



## Spécification

### Spécification des options LS2

Les options LS2 DOIVENT être triées par clé, afin que la signature soit invariante.

Définies comme suit :

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := Nom symbolique du service souhaité. Doit être en minuscules. Exemple : « smtp ».  
  Les caractères autorisés sont [a-z0-9-] et ne doivent pas commencer ni finir par un « - ».  
  Les identifiants standard du [registre des types de service DNS-SD](http://www.dns-sd.org/ServiceTypes.html) ou du fichier /etc/services Linux doivent être utilisés s'ils sont définis.
- proto := Protocole de transport du service souhaité. Doit être en minuscules, soit « tcp » soit « udp ».  
  « tcp » signifie flux, « udp » signifie datagrammes avec réponse possible.  
  Des indicateurs de protocole pour les datagrammes bruts et datagram2 pourront être définis ultérieurement.  
  Les caractères autorisés sont [a-z0-9-] et ne doivent pas commencer ni finir par un « - ».
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := durée de vie, en secondes entières. Entier positif. Exemple : « 86400 ».  
  Un minimum de 86400 (un jour) est recommandé, voir la section Recommandations ci-dessous pour plus de détails.
- priority := Priorité de l'hôte cible, une valeur plus faible signifie plus préférée. Entier non négatif. Exemple : « 0 »  
  Utile uniquement s'il y a plusieurs enregistrements, mais requis même s'il n'y en a qu'un.
- weight := Poids relatif pour les enregistrements ayant la même priorité. Une valeur plus élevée signifie plus de chances d'être sélectionné. Entier non négatif. Exemple : « 0 »  
  Utile uniquement s'il y a plusieurs enregistrements, mais requis même s'il n'y en a qu'un.
- port := Port I2CP sur lequel le service est disponible. Entier non négatif. Exemple : « 25 »  
  Le port 0 est supporté mais non recommandé.
- target := Nom d'hôte ou b32 de la destination fournissant le service. Un [nom d'hôte](/docs/overview/naming/) valide. Doit être en minuscules.  
  Exemple : « aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p » ou « example.i2p ».  
  Le b32 est recommandé sauf si le nom d'hôte est « bien connu », c'est-à-dire présent dans les carnets d'adresses officiels ou par défaut.
- appoptions := texte arbitraire spécifique à l'application, ne doit pas contenir « » ou « , ». L'encodage est UTF-8.

### Exemples

Dans LS2 pour aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, pointant vers un serveur SMTP :

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Dans LS2 pour aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, pointant vers deux serveurs SMTP :

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

Dans LS2 pour bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p, pointant vers lui-même comme serveur SMTP :

    "_smtp._tcp" "0 999999 25"

Format possible pour rediriger les courriels (voir ci-dessous) :

    "_smtp._tcp" "1 86400 0 0 25 smtp.postman.i2p example@mail.i2p"


### Limites

La structure de données « Mapping » utilisée pour les options LS2 limite les clés et valeurs à 255 octets (pas caractères) maximum.  
Avec une cible b32, l'optionvalue fait environ 67 octets, donc seulement 3 enregistrements tiendraient.  
Peut-être un ou deux seulement avec un champ appoptions long, ou jusqu'à quatre ou cinq avec un nom d'hôte court.  
Cela devrait suffire ; plusieurs enregistrements devraient être rares.


### Différences avec RFC 2782

- Pas de points finaux
- Pas de nom après le proto
- Minuscules obligatoires
- Format texte avec enregistrements séparés par des virgules, pas format binaire DNS
- Indicateurs de type d'enregistrement différents
- Champ appoptions supplémentaire


### Notes

Aucun joker tel que (astérisque), (astérisque)._tcp ou _tcp n'est autorisé.  
Chaque service pris en charge doit avoir son propre enregistrement.



### Registre des noms de service

Des identifiants non standard non répertoriés dans le [registre des types de service DNS-SD](http://www.dns-sd.org/ServiceTypes.html) ou dans /etc/services Linux  
peuvent être demandés et ajoutés à la [spécification des structures communes](/docs/specs/common-structures/).

Les formats appoptions spécifiques aux services pourront également être ajoutés là-bas.


### Spécification I2CP

Le [protocole I2CP](/docs/specs/i2cp/) doit être étendu pour prendre en charge les recherches de service.  
Des codes d'erreur supplémentaires dans MessageStatusMessage et/ou HostReplyMessage liés à la recherche de service  
sont requis.  
Pour rendre la fonctionnalité de recherche générale, et pas seulement spécifique aux enregistrements de service,  
la conception vise à permettre la récupération de toutes les options LS2.

Implémentation : Étendre HostLookupMessage pour ajouter une demande  
d'options LS2 pour hash, nom d'hôte et destination (types de requête 2-4).  
Étendre HostReplyMessage pour ajouter le mapping d'options si demandé.  
Étendre HostReplyMessage avec des codes d'erreur supplémentaires.

Les mappings d'options peuvent être mis en cache ou en cache négatif pendant un court laps de temps côté client ou routeur,  
selon l'implémentation. Le temps maximum recommandé est d'une heure, sauf si le TTL de l'enregistrement de service est plus court.  
Les enregistrements de service peuvent être mis en cache jusqu'au TTL spécifié par l'application, le client ou le routeur.

Étendre la spécification comme suit :

#### Options de configuration

Ajouter ce qui suit aux [options de configuration I2CP](/docs/specs/i2cp/)

i2cp.leaseSetOption.nnn

Options à insérer dans l'ensemble de baux. Disponible uniquement pour LS2.  
nnn commence à 0. La valeur de l'option contient « key=value ».  
(ne pas inclure les guillemets)

Exemple :  
i2cp.leaseSetOption.0=_smtp._tcp=1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p


#### Message HostLookup

- Type de recherche 2 : Recherche par hash, demande du mapping d'options
- Type de recherche 3 : Recherche par nom d'hôte, demande du mapping d'options
- Type de recherche 4 : Recherche par destination, demande du mapping d'options

Pour le type de recherche 4, l'élément 5 est une Destination.



#### Message HostReply

Pour les types de recherche 2-4, le routeur doit récupérer l'ensemble de baux,  
même si la clé de recherche est dans le carnet d'adresses.

En cas de succès, HostReply contiendra le mapping d'options  
de l'ensemble de baux, et l'inclura comme élément 5 après la destination.  
S'il n'y a pas d'options dans le mapping, ou si l'ensemble de baux était en version 1,  
il sera quand même inclus comme mapping vide (deux octets : 0 0).  
Toutes les options de l'ensemble de baux seront incluses, pas seulement les options d'enregistrement de service.  
Par exemple, des options pour des paramètres définis à l'avenir pourraient être présentes.

En cas d'échec de la recherche de l'ensemble de baux, la réponse contiendra un nouveau code d'erreur 6 (échec de la recherche de l'ensemble de baux)  
et n'inclura pas de mapping.  
Lorsque le code d'erreur 6 est retourné, le champ Destination peut ou non être présent.  
Il sera présent si une recherche de nom d'hôte dans le carnet d'adresses a réussi,  
ou si une recherche précédente a réussi et que le résultat a été mis en cache,  
ou si la Destination était présente dans le message de recherche (type 4).

Si un type de recherche n'est pas pris en charge,  
la réponse contiendra un nouveau code d'erreur 7 (type de recherche non pris en charge).



### Spécification SAM

Le [protocole SAMv3](/docs/api/samv3/) doit être étendu pour prendre en charge les recherches de service.

Étendre NAMING LOOKUP comme suit :

NAMING LOOKUP NAME=example.i2p OPTIONS=true demande le mapping d'options dans la réponse.

NAME peut être une destination base64 complète lorsque OPTIONS=true.

Si la recherche de destination a réussi et que des options étaient présentes dans l'ensemble de baux,  
alors dans la réponse, après la destination,  
figurera un ou plusieurs options sous la forme OPTION:key=value.  
Chaque option aura un préfixe OPTION: séparé.  
Toutes les options de l'ensemble de baux seront incluses, pas seulement les options d'enregistrement de service.  
Par exemple, des options pour des paramètres définis à l'avenir pourraient être présentes.  
Exemple :

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Les clés contenant « = », et les clés ou valeurs contenant un saut de ligne,  
sont considérées comme invalides et la paire clé/valeur sera supprimée de la réponse.

S'il n'y a aucune option trouvée dans l'ensemble de baux, ou si l'ensemble de baux était en version 1,  
la réponse n'inclura aucune option.

Si OPTIONS=true était dans la recherche, et que l'ensemble de baux n'est pas trouvé, une nouvelle valeur de résultat LEASESET_NOT_FOUND sera retournée.


## Alternative de recherche par nom

Une conception alternative a été envisagée, pour prendre en charge les recherches de services  
sous forme de nom d'hôte complet, par exemple _smtp._tcp.example.i2p,  
en mettant à jour la [spécification de nommage](/docs/overview/naming/) pour spécifier le traitement des noms d'hôte commençant par « _ ».  
Cela a été rejeté pour deux raisons :

- Les modifications d'I2CP et de SAM seraient toujours nécessaires pour transmettre les informations TTL et port au client.
- Ce ne serait pas une fonctionnalité générale pouvant être utilisée pour récupérer d'autres options LS2  
  pouvant être définies à l'avenir.


## Recommandations

Les serveurs devraient spécifier un TTL d'au moins 86400, et le port standard pour l'application.



## Fonctionnalités avancées

### Recherches récursives

Il pourrait être souhaitable de prendre en charge des recherches récursives, où chaque ensemble de baux successif  
est vérifié pour un enregistrement de service pointant vers un autre ensemble de baux, à la manière DNS.  
Cela n'est probablement pas nécessaire, du moins dans une implémentation initiale.

TODO



### Champs spécifiques à l'application

Il pourrait être souhaitable d'avoir des données spécifiques à l'application dans l'enregistrement de service.  
Par exemple, l'opérateur de example.i2p pourrait vouloir indiquer que les courriels doivent  
être transférés vers example@mail.i2p. La partie « example@ » devrait être dans un champ séparé  
de l'enregistrement de service, ou extraite de la cible.

Même si l'opérateur exécute son propre service de courrier, il pourrait vouloir indiquer que  
les courriels doivent être envoyés à example@example.i2p. La plupart des services I2P sont gérés par une seule personne.  
Un champ séparé pourrait donc également être utile ici.

TODO comment faire cela de manière générique


### Modifications requises pour le courrier électronique

Hors du champ de cette proposition. Voir la [discussion sur i2pforum](http://i2pforum.i2p/viewtopic.php?p=3102) pour plus de détails.


## Notes d'implémentation

La mise en cache des enregistrements de service jusqu'au TTL peut être effectuée par le routeur ou l'application,  
selon l'implémentation. La mise en cache persistante est également dépendante de l'implémentation.

Les recherches doivent également rechercher l'ensemble de baux cible et vérifier qu'il contient un enregistrement « self »  
avant de retourner la destination cible au client.


## Analyse de sécurité

Étant donné que l'ensemble de baux est signé, tous les enregistrements de service qu'il contient sont authentifiés par la clé de signature de la destination.

Les enregistrements de service sont publics et visibles par les floodfills, sauf si l'ensemble de baux est chiffré.  
Tout routeur demandant l'ensemble de baux pourra voir les enregistrements de service.

Un enregistrement SRV autre que « self » (c'est-à-dire, pointant vers une cible nom d'hôte/b32 différente)  
ne nécessite pas le consentement du nom d'hôte/b32 cible.  
Il n'est pas clair si une redirection d'un service vers une destination arbitraire pourrait faciliter une  
quelconque attaque, ou quel en serait l'objectif.  
Cependant, cette proposition atténue une telle attaque en exigeant que la cible  
publie également un enregistrement SRV « self ». Les implémenteurs doivent vérifier la présence d'un enregistrement « self »  
dans l'ensemble de baux de la cible.


## Compatibilité

LS2 : Aucun problème. Toutes les implémentations connues ignorent actuellement le champ d'options dans LS2,  
et passent correctement outre un champ d'options non vide.  
Cela a été vérifié lors des tests par Java I2P et i2pd lors du développement de LS2.  
LS2 a été implémenté en 0.9.38 en 2016 et est bien pris en charge par toutes les implémentations de routeur.  
La conception ne nécessite aucun support spécial, aucune mise en cache ni aucun changement dans les floodfills.

Nommage : « _ » n'est pas un caractère valide dans les noms d'hôte I2P.

I2CP : Les types de recherche 2-4 ne doivent pas être envoyés aux routeurs dont la version API est inférieure à la version minimale  
à laquelle ils sont pris en charge (à déterminer).

SAM : Le serveur SAM Java ignore les clés/valeurs supplémentaires telles que OPTIONS=true.  
i2pd devrait en faire de même, à vérifier.  
Les clients SAM n'obtiendront pas les valeurs supplémentaires dans la réponse sauf si demandées avec OPTIONS=true.  
Aucun changement de version ne devrait être nécessaire.


## Migration

Les implémentations peuvent ajouter le support à tout moment, aucune coordination n'est nécessaire,  
sauf pour un accord sur la version API effective pour les modifications d'I2CP.  
Les versions de compatibilité SAM pour chaque implémentation seront documentées dans la spécification SAM.


## Références

* [DOTWELLKNOWN](http://i2pforum.i2p/viewtopic.php?p=3102)
* [I2CP](/docs/specs/i2cp/)
* [I2CP-OPTIONS](/docs/specs/i2cp/)
* [LS2](/docs/specs/common-structures/)
* [GNS](http://zzz.i2p/topcs/1545)
* [NAMING](/docs/overview/naming/)
* [Prop123](/proposals/123-new-netdb-entries/)
* [Prop168](/proposals/168-tunnel-bandwidth/)
* [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
* [RFC2782](https://datatracker.ietf.org/doc/html/rfc2782)
* [SAMv3](/docs/api/samv3/)
* [SRV](https://en.wikipedia.org/wiki/SRV_record)
