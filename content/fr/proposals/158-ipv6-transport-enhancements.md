---
title: "Améliorations du Transport IPv6"
aliases:
  - "/fr/spec/proposals/158"
  - "/fr/spec/proposals/158/"
number: "158"
author: "zzz, original"
created: "2021-03-19"
lastupdated: "2021-04-26"
status: "Fermé"
thread: "http://zzz.i2p/topics/3060"
target: "0.9.50"
toc: true
---
## Note
Déploiement réseau et tests en cours.  
Sous réserve de révisions mineures.


## Aperçu

Cette proposition vise à implémenter des améliorations aux transports SSU et NTCP2 pour IPv6.


## Motivation

Alors que IPv6 se développe dans le monde entier et que les configurations IPv6-seulement (en particulier sur mobile) deviennent plus courantes,  
nous devons améliorer notre prise en charge d'IPv6 et supprimer les hypothèses selon lesquelles  
tous les routeurs sont compatibles IPv4.



### Vérification de connectivité

Lors de la sélection de pairs pour les tunnels, ou lors du choix des chemins OBEP/IBGW pour acheminer les messages,  
il est utile de déterminer si le routeur A peut se connecter au routeur B.  
En général, cela signifie déterminer si A dispose d'une capacité sortante pour un transport et un type d'adresse (IPv4/v6)  
qui correspond à l'une des adresses entrantes publiées par B.

Cependant, dans de nombreux cas, nous ne connaissons pas les capacités de A et devons faire des hypothèses.  
Si A est masqué ou derrière un pare-feu, les adresses ne sont pas publiées et nous n'avons pas de connaissance directe —  
nous supposons donc qu'il est compatible IPv4, mais pas IPv6.  
La solution consiste à ajouter deux nouvelles « caps » ou capacités au Router Info pour indiquer la capacité sortante IPv4 et IPv6.


### Introducers IPv6

Nos spécifications pour SSU contiennent des erreurs et incohérences quant à savoir si  
les introducers IPv6 sont pris en charge pour les introductions IPv4.  
Dans tous les cas, cela n'a jamais été implémenté ni dans Java I2P ni dans i2pd.  
Cela doit être corrigé.


### Introductions IPv6

Nos spécifications pour SSU indiquent clairement que  
les introductions IPv6 ne sont pas prises en charge.  
Cela reposait sur l'hypothèse que IPv6 n'est jamais derrière un pare-feu.  
Cela est manifestement faux, et nous devons améliorer la prise en charge des routeurs IPv6 derrière pare-feu.


### Diagrammes d'introduction

Légende : ----- est IPv4, ====== est IPv6

**Actuellement IPv4 uniquement :**

```
        Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**Introduction IPv4, introducer IPv6 :**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**Introduction IPv6, introducer IPv6 :**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```

**Introduction IPv6, introducer IPv4 :**

```
Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```


## Conception

Trois modifications doivent être mises en œuvre.

- Ajouter les capacités « 4 » et « 6 » aux capacités d'adresse de routeur pour indiquer la prise en charge sortante IPv4 et IPv6
- Ajouter la prise en charge des introductions IPv4 via des introducers IPv6
- Ajouter la prise en charge des introductions IPv6 via des introducers IPv4 et IPv6



## Spécification

### Caps 4/6

Cela a été initialement implémenté sans proposition formelle, mais c'est requis pour  
les introductions IPv6, donc nous l'incluons ici.

Deux nouvelles capacités « 4 » et « 6 » sont définies.  
Ces nouvelles capacités seront ajoutées à la propriété « caps » dans l'adresse de routeur, et non dans les caps du Router Info.  
Nous n'avons actuellement pas de propriété « caps » définie pour NTCP2.  
Une adresse SSU avec des introducers est, par définition, ipv4 pour l'instant. Nous ne prenons pas en charge l'introduction ipv6 du tout.  
Cependant, cette proposition est compatible avec les introductions IPv6. Voir ci-dessous.

De plus, un routeur peut prendre en charge la connectivité via un réseau superposé tel que I2P-over-Yggdrasil,  
mais ne souhaite pas publier d'adresse, ou cette adresse n'a pas un format IPv4 ou IPv6 standard.  
Ce nouveau système de capacités devrait être suffisamment flexible pour prendre en charge ces réseaux également.

Nous définissons les modifications suivantes :

NTCP2 : Ajouter la propriété « caps »

SSU : Ajouter la prise en charge d'une adresse de routeur sans hôte ni introducers, pour indiquer la prise en charge sortante  
pour IPv4, IPv6, ou les deux.

Les deux transports : Définir les valeurs de caps suivantes :

- « 4 » : prise en charge IPv4
- « 6 » : prise en charge IPv6

Plusieurs valeurs peuvent être prises en charge dans une seule adresse. Voir ci-dessous.  
Au moins l'une de ces caps est obligatoire si aucune valeur « host » n'est incluse dans l'adresse de routeur.  
Au plus une de ces caps est facultative si une valeur « host » est incluse dans l'adresse de routeur.  
Des caps de transport supplémentaires pourront être définis à l'avenir pour indiquer la prise en charge de réseaux superposés ou d'autres connectivités.


#### Cas d'utilisation et exemples

SSU :

SSU avec hôte : 4/6 facultatif, jamais plus d'un.  
Exemple : SSU caps="4" host="1.2.3.4" key=... port="1234"

SSU uniquement sortant pour un, l'autre est publié : Caps uniquement, 4/6.  
Exemple : SSU caps="6"

SSU avec introducers : jamais combiné. 4 ou 6 est requis.  
Exemple : SSU caps="4" iexp0=... ihost0=... iport0=... itag0=... key=...

SSU masqué : Caps uniquement, 4, 6, ou 46. Plusieurs autorisés.  
Pas besoin de deux adresses, une avec 4 et une avec 6.  
Exemple : SSU caps="46"

NTCP2 :

NTCP2 avec hôte : 4/6 facultatif, jamais plus d'un.  
Exemple : NTCP2 caps="4" host="1.2.3.4" i=... port="1234" s=... v="2"

NTCP2 uniquement sortant pour un, l'autre est publié : Caps, s, v uniquement, 4/6/y, plusieurs autorisés.  
Exemple : NTCP2 caps="6" i=... s=... v="2"

NTCP2 masqué : Caps, s, v uniquement 4/6, plusieurs autorisés. Pas besoin de deux adresses, une avec 4 et une avec 6.  
Exemple : NTCP2 caps="46" i=... s=... v="2"



### Introducers IPv6 pour IPv4

Les modifications suivantes sont nécessaires pour corriger les erreurs et incohérences dans les spécifications.  
Nous avons également décrit cela comme la « partie 1 » de la proposition.

#### Modifications de spécification

La spécification SSU dit actuellement (notes IPv6) :

IPv6 est pris en charge à partir de la version 0.9.8. Les adresses de relais publiées peuvent être IPv4 ou IPv6, et la communication Alice-Bob peut se faire via IPv4 ou IPv6.

Ajouter ce qui suit :

Bien que la spécification ait été modifiée à partir de la version 0.9.8, la communication Alice-Bob via IPv6 n'était pas réellement prise en charge avant la version 0.9.50.  
Les versions antérieures des routeurs Java ont publié de manière erronée la capacité 'C' pour les adresses IPv6,  
même s'ils n'agissaient pas réellement comme un introducer via IPv6.  
Par conséquent, les routeurs ne devraient faire confiance à la capacité 'C' sur une adresse IPv6 que si la version du routeur est 0.9.50 ou supérieure.



La spécification SSU dit actuellement (Relay Request) :

L'adresse IP n'est incluse que si elle est différente de l'adresse source et du port du paquet.  
Dans l'implémentation actuelle, la longueur IP est toujours 0 et le port est toujours 0,  
et le destinataire doit utiliser l'adresse source et le port du paquet.  
Ce message peut être envoyé via IPv4 ou IPv6. Si IPv6, Alice doit inclure son adresse et port IPv4.

Ajouter ce qui suit :

L'IP et le port doivent être inclus pour introduire une adresse IPv4 lors de l'envoi de ce message via IPv6.  
Cela est pris en charge à partir de la version 0.9.50.



### Introductions IPv6

Les trois messages de relais SSU (RelayRequest, RelayResponse et RelayIntro) contiennent des champs de longueur IP  
pour indiquer la longueur de l'adresse IP (Alice, Bob ou Charlie) à suivre.

Par conséquent, aucune modification du format des messages n'est requise.  
Seules des modifications textuelles aux spécifications, indiquant que les adresses IP de 16 octets sont autorisées.

Les modifications suivantes sont requises aux spécifications.  
Nous avons également décrit cela comme la « partie 2 » de la proposition.


#### Modifications de spécification

La spécification SSU dit actuellement (notes IPv6) :

La communication Bob-Charlie et Alice-Charlie se fait uniquement via IPv4.

La spécification SSU dit actuellement (Relay Request) :

Il n'est pas prévu d'implémenter le relais pour IPv6.

Modifier pour indiquer :

Le relais pour IPv6 est pris en charge à partir de la version 0.9.xx

La spécification SSU dit actuellement (Relay Response) :

L'adresse IP de Charlie doit être IPv4, car c'est l'adresse à laquelle Alice enverra le SessionRequest après le Hole Punch.  
Il n'est pas prévu d'implémenter le relais pour IPv6.

Modifier pour indiquer :

L'adresse IP de Charlie peut être IPv4 ou, à partir de la version 0.9.xx, IPv6.  
C'est l'adresse à laquelle Alice enverra le SessionRequest après le Hole Punch.  
Le relais pour IPv6 est pris en charge à partir de la version 0.9.xx

La spécification SSU dit actuellement (Relay Intro) :

L'adresse IP d'Alice fait toujours 4 octets dans l'implémentation actuelle, car Alice tente de se connecter à Charlie via IPv4.  
Ce message doit être envoyé via une connexion IPv4 établie,  
car c'est la seule façon dont Bob connaît l'adresse IPv4 de Charlie à renvoyer à Alice dans le RelayResponse.

Modifier pour indiquer :

Pour IPv4, l'adresse IP d'Alice fait toujours 4 octets, car Alice tente de se connecter à Charlie via IPv4.  
À partir de la version 0.9.xx, IPv6 est pris en charge, et l'adresse IP d'Alice peut faire 16 octets.

Pour IPv4, ce message doit être envoyé via une connexion IPv4 établie,  
car c'est la seule façon dont Bob connaît l'adresse IPv4 de Charlie à renvoyer à Alice dans le RelayResponse.  
À partir de la version 0.9.xx, IPv6 est pris en charge, et ce message peut être envoyé via une connexion IPv6 établie.

Ajouter également :

À partir de la version 0.9.xx, toute adresse SSU publiée avec des introducers doit contenir « 4 » ou « 6 » dans l'option « caps ».


## Migration

Tous les anciens routeurs devraient ignorer la propriété caps dans NTCP2, et les caractères de capacité inconnus dans la propriété caps SSU.

Toute adresse SSU avec des introducers qui ne contient pas une cap « 4 » ou « 6 » est supposée destinée à une introduction IPv4.


## Références

* [CAPS](http://zzz.i2p/topics/3050)
* [NTCP2](/docs/specs/ntcp2/)
* [SSU](/docs/specs/ssu2/)
* [SSU-SPEC](/docs/legacy/ssu/)
