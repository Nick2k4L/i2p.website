---
title: "Proposition I2P #166 : Types de Tunnels Sensibles à l'Identité/Hôte"
number: "166"
author: "eyedeekay"
created: "2024-05-27"
lastupdated: "2024-08-27"
status: "Ouvert"
thread: "http://i2pforum.i2p/viewforum.php?f=13"
target: "0.9.65"
toc: true
---
### Proposition pour un type de tunnel HTTP proxy prenant en compte l'hôte

Il s'agit d'une proposition visant à résoudre le « problème d'identité partagée » dans l'utilisation conventionnelle de HTTP-sur-I2P, en introduisant un nouveau type de tunnel HTTP proxy. Ce type de tunnel comporte un comportement supplémentaire destiné à empêcher ou limiter l'utilité du pistage mené par des opérateurs potentiellement malveillants de services cachés, contre des agents-utilisateurs ciblés (navigateurs) et l'application cliente I2P elle-même.

#### Qu'est-ce que le « problème d'identité partagée » ?

Le « problème d'identité partagée » survient lorsqu'un agent-utilisateur sur un réseau superposé à adressage cryptographique partage une identité cryptographique avec un autre agent-utilisateur. Cela se produit, par exemple, lorsqu'un Firefox et un GNU Wget sont tous deux configurés pour utiliser le même proxy HTTP.

Dans ce scénario, il est possible pour le serveur de collecter et stocker l'adresse cryptographique (Destination) utilisée pour répondre à l'activité. Il peut traiter cela comme un « fingerprint » qui est toujours 100 % unique, car il est d'origine cryptographique. Cela signifie que la traçabilité observée par le problème d'identité partagée est parfaite.

Mais est-ce un problème ?
^^^^^^^^^^^^^^^^^^^^^^^^^^

Le problème d'identité partagée est un problème lorsque des agents-utilisateurs parlant le même protocole souhaitent être non liés. [Il a été mentionné pour la première fois dans le contexte de HTTP dans ce fil Reddit](https://old.reddit.com/r/i2p/comments/579idi/warning_i2p_is_linkablefingerprintable/), les commentaires supprimés étant accessibles grâce à [pullpush.io](https://api.pullpush.io/reddit/search/comment/?link_id=579idi). *À l'époque*, j'étais l'un des répondants les plus actifs, et *à l'époque*, je pensais que le problème était mineur. Au cours des 8 dernières années, la situation et mon opinion à ce sujet ont changé ; je pense désormais que la menace posée par la corrélation malveillante de destinations augmente considérablement à mesure que davantage de sites sont en mesure de « profiler » des utilisateurs spécifiques.

Cette attaque a un seuil d'entrée très bas. Elle ne nécessite que l'exploitation de plusieurs services par un opérateur de service caché. Pour les attaques sur des visites contemporaines (visite de plusieurs sites simultanément), c'est la seule condition requise. Pour les liens non contemporains, l'un de ces services doit être un service hébergeant des « comptes » appartenant à un seul utilisateur ciblé pour le pistage.

Actuellement, tout opérateur de service hébergeant des comptes utilisateurs sera capable de les corréler avec l'activité sur tous les sites qu'il contrôle, en exploitant le problème d'identité partagée. Mastodon, Gitlab, ou même de simples forums pourraient être des attaquants déguisés, dès lors qu'ils exploitent plus d'un service et ont un intérêt à créer un profil utilisateur. Cette surveillance pourrait être menée pour du harcèlement, un gain financier ou des raisons liées au renseignement. Actuellement, des dizaines d'opérateurs majeurs pourraient mener cette attaque et en tirer des données significatives. Nous leur faisons principalement confiance pour ne pas le faire pour l'instant, mais des acteurs qui se moquent de nos opinions pourraient facilement apparaître.

Cela est directement lié à une forme assez basique de construction de profil sur le web clair, où des organisations peuvent corréler des interactions sur leur site avec des interactions sur des réseaux qu'elles contrôlent. Sur I2P, comme la destination cryptographique est unique, cette technique peut parfois être encore plus fiable, bien qu'elle ne dispose pas du pouvoir supplémentaire de la géolocalisation.

L'identité partagée n'est pas utile contre un utilisateur qui utilise I2P uniquement pour obscurcir sa géolocalisation. Elle ne peut pas non plus être utilisée pour compromettre le routage d'I2P. C'est uniquement un problème de gestion d'identité contextuelle.

-  Il est impossible d'utiliser le problème d'identité partagée pour géolocaliser un utilisateur I2P.
-  Il est impossible d'utiliser le problème d'identité partagée pour lier des sessions I2P si elles ne sont pas contemporaines.

Cependant, il est possible de l'utiliser pour dégrader l'anonymat d'un utilisateur I2P dans des circonstances qui sont probablement très fréquentes. Une raison de leur fréquence est que nous encourageons l'utilisation de Firefox, un navigateur web qui prend en charge le fonctionnement par « onglets ».

-  Il est *toujours* possible de produire un fingerprint à partir du problème d'identité partagée dans *n'importe quel* navigateur web prenant en charge la requête de ressources tierces.
-  Désactiver Javascript n'accomplit **rien** contre le problème d'identité partagée.
-  Si un lien peut être établi entre des sessions non contemporaines, par exemple via un fingerprinting « traditionnel » du navigateur, alors l'identité partagée peut être appliquée de manière transitive, permettant potentiellement une stratégie de liaison non contemporaine.
-  Si un lien peut être établi entre une activité sur le clearnet et une identité I2P, par exemple si la cible est connectée à un site avec une présence I2P et clearnet des deux côtés, l'identité partagée peut être appliquée de manière transitive, permettant potentiellement une dés-anonymisation complète.

La manière dont vous percevez la gravité du problème d'identité partagée en ce qui concerne le proxy HTTP I2P dépend de l'endroit où vous (ou plus précisément, un « utilisateur » avec des attentes potentiellement mal informées) situez l'« identité contextuelle » pour l'application. Plusieurs possibilités existent :

1. HTTP est à la fois l'Application et l'Identité Contextuelle — C'est ainsi que cela fonctionne actuellement. Toutes les applications HTTP partagent une identité.
2. Le Processus est l'Application et l'Identité Contextuelle — C'est ainsi que cela fonctionne lorsqu'une application utilise une API comme SAMv3 ou I2CP, où une application crée sa propre identité et en contrôle la durée de vie.
3. HTTP est l'Application, mais l'Hôte est l'Identité Contextuelle — C'est l'objet de cette proposition, qui traite chaque hôte comme une « application web » potentielle et considère la surface d'attaque comme telle.

Est-ce résoluble ?
^^^^^^^^^^^^^^^^^^

Il n'est probablement pas possible de créer un proxy qui réagisse intelligemment à chaque cas possible où son fonctionnement pourrait affaiblir l'anonymat d'une application. Cependant, il est possible de construire un proxy qui réagisse intelligemment à une application spécifique se comportant de manière prévisible. Par exemple, dans les navigateurs web modernes, on s'attend à ce que les utilisateurs aient plusieurs onglets ouverts, interagissant avec plusieurs sites web, distingués par leur nom d'hôte.

Cela nous permet d'améliorer le comportement du proxy HTTP pour ce type d'agent-utilisateur HTTP en faisant correspondre le comportement du proxy à celui de l'agent-utilisateur, en attribuant à chaque hôte sa propre Destination lorsqu'il est utilisé avec le proxy HTTP. Ce changement rend impossible l'utilisation du problème d'identité partagée pour dériver un fingerprint pouvant être utilisé pour corréler l'activité cliente avec 2 hôtes, car les 2 hôtes ne partageront plus d'identité de retour.

Description :
^^^^^^^^^^^^

Un nouveau proxy HTTP sera créé et ajouté au gestionnaire de services cachés (I2PTunnel). Le nouveau proxy HTTP fonctionnera comme un « multiplexeur » de I2PSocketManagers. Le multiplexeur lui-même n'a pas de destination. Chaque I2PSocketManager individuel faisant partie du multiplex possède sa propre destination locale et son propre pool de tunnels. Les I2PSocketManagers sont créés à la demande par le multiplexeur, la « demande » étant la première visite à un nouvel hôte. Il est possible d'optimiser la création des I2PSocketManagers avant de les insérer dans le multiplexeur en en créant un ou plusieurs à l'avance et en les stockant en dehors du multiplexeur. Cela pourrait améliorer les performances.

Un I2PSocketManager supplémentaire, avec sa propre destination, est configuré comme support d'un « Outproxy » pour tout site qui n'a *pas* de destination I2P, par exemple tout site du clearnet. Cela fait de toute utilisation d'Outproxy une seule identité contextuelle, avec la nuance que la configuration de plusieurs Outproxies pour le tunnel entraînera la rotation « collante » normale des outproxies, où chaque outproxy ne reçoit des requêtes que pour un seul site. C'est *presque* le comportement équivalent à l'isolation des proxys HTTP-sur-I2P par destination, sur internet clair.

Considérations relatives aux ressources :
''''''''''''''''''''''''''''''''''''''''

Le nouveau proxy HTTP nécessite des ressources supplémentaires par rapport au proxy HTTP existant. Il va :

-  Potentiellement construire plus de tunnels et de I2PSocketManagers
-  Construire des tunnels plus fréquemment

Chacun de ces éléments nécessite :

-  Des ressources informatiques locales
-  Des ressources réseau provenant des pairs

Paramètres :
'''''''''''

Afin de minimiser l'impact de l'utilisation accrue des ressources, le proxy devrait être configuré pour utiliser le moins possible. Les proxys faisant partie du multiplexeur (pas le proxy parent) devraient être configurés pour :

-  Les I2PSocketManagers multiplexés construisent 1 tunnel entrant, 1 tunnel sortant dans leurs pools de tunnels
-  Les I2PSocketManagers multiplexés utilisent 3 sauts par défaut.
-  Fermer les sockets après 10 minutes d'inactivité
-  Les I2PSocketManagers lancés par le Multiplexeur partagent la durée de vie du Multiplexeur. Les tunnels multiplexés ne sont pas « détruits » tant que le Multiplexeur parent ne l'est pas.

Diagrammes :
^^^^^^^^^^^

Le diagramme ci-dessous représente le fonctionnement actuel du proxy HTTP, qui correspond à la « Possibilité 1 » dans la section « Est-ce un problème ? ». Comme vous pouvez le voir, le proxy HTTP interagit directement avec les sites I2P en utilisant une seule destination. Dans ce scénario, HTTP est à la fois l'application et l'identité contextuelle.

```text
**Situation actuelle : HTTP est l'Application, HTTP est l'Identité Contextuelle**
                                                      __-> Outproxy <-> i2pgit.org
                                                     /
Browser <-> HTTP Proxy(une Destination)<->I2PSocketManager <---> idk.i2p
                                                     \__-> translate.idk.i2p
                                                      \__-> git.idk.i2p
```

Le diagramme ci-dessous représente le fonctionnement d'un proxy HTTP prenant en compte l'hôte, qui correspond à la « Possibilité 3 » dans la section « Est-ce un problème ? ». Dans ce scénario, HTTP est l'application, mais l'hôte définit l'identité contextuelle, chaque site I2P interagissant avec un proxy HTTP différent ayant une destination unique par hôte. Cela empêche les opérateurs de plusieurs sites de distinguer quand la même personne visite plusieurs sites qu'ils exploitent.

```text
**Après le changement : HTTP est l'Application, l'Hôte est l'Identité Contextuelle**
                                                    __-> I2PSocketManager(Destination A - uniquement pour les Outproxies) <--> i2pgit.org
                                                   /
Browser <-> HTTP Proxy Multiplexer(Pas de Destination) <---> I2PSocketManager(Destination B) <--> idk.i2p
                                                   \__-> I2PSocketManager(Destination C) <--> translate.idk.i2p
                                                    \__-> I2PSocketManager(Destination C) <--> git.idk.i2p
```

État :
^^^^^

Une implémentation Java fonctionnelle du proxy prenant en compte l'hôte, conforme à une version antérieure de cette proposition, est disponible sur le fork d'idk, dans la branche : i2p.i2p.2.6.0-browser-proxy-post-keepalive. Lien dans les citations. Elle est en cours de révision poussée, afin de décomposer les modifications en sections plus petites.

Des implémentations aux fonctionnalités variées ont été écrites en Go en utilisant la bibliothèque SAMv3. Elles peuvent être utiles pour intégration dans d'autres applications Go ou pour go-i2p, mais ne conviennent pas à Java I2P. De plus, elles manquent d'un bon support pour interagir de manière interactive avec des leaseSets chiffrés.

Annexe : ``i2psocks``
                     

Une approche simple orientée application pour isoler d'autres types de clients est possible sans implémenter un nouveau type de tunnel ni modifier le code I2P existant, en combinant les outils I2PTunnel déjà largement disponibles et testés dans la communauté de la confidentialité. Cependant, cette approche repose sur une hypothèse difficile qui n'est pas vraie pour HTTP et également fausse pour de nombreux autres types potentiels de clients I2P.

Grossièrement, le script suivant produira un proxy SOCKS5 conscient de l'application et socksifiera la commande sous-jacente :

```sh
#! /bin/sh
command_to_proxy="$@"
java -jar ~/i2p/lib/i2ptunnel.jar -wait -e 'sockstunnel 7695'
torsocks --port 7695 $command_to_proxy
```

Annexe : ``exemple d'implémentation de l'attaque``
                                                  

[Un exemple d'implémentation de l'attaque d'identité partagée sur les agents-utilisateurs HTTP](https://github.com/eyedeekay/colluding_sites_attack/) existe depuis plusieurs années. Un autre exemple est disponible dans le sous-répertoire ``simple-colluder`` du [dépôt prop166 d'idk](https://git.idk.i2p/idk/i2p.host-aware-proxy). Ces exemples sont délibérément conçus pour démontrer que l'attaque fonctionne et nécessiteraient une modification (bien que mineure) pour être transformés en une attaque réelle.
