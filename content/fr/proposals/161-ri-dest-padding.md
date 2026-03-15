---
title: "RI et Remplissage de Destination"
number: "161"
author: "zzz"
created: "2022-09-28"
lastupdated: "2023-01-02"
status: "Open"
thread: "http://zzz.i2p/topics/3279"
target: "0.9.57"
toc: true
---
## Statut

Implémenté en 0.9.57.
Laisser cette proposition ouverte afin que nous puissions améliorer et discuter des idées dans la section « Planification future ».


## Aperçu


### Résumé

La clé publique ElGamal dans les Destinations n'est plus utilisée depuis la version 0.6 (2005).
Bien que nos spécifications indiquent qu'elle est inutilisée, elles ne précisent PAS que les implémentations peuvent éviter
de générer une paire de clés ElGamal et remplir simplement le champ avec des données aléatoires.

Nous proposons de modifier les spécifications pour indiquer que
le champ est ignoré et que les implémentations PEUVENT remplir le champ avec des données aléatoires.
Ce changement est compatible avec les versions antérieures. Aucune implémentation connue ne valide
la clé publique ElGamal.

De plus, cette proposition fournit des recommandations aux développeurs sur la manière de générer les
données aléatoires pour le remplissage des Destinations ET des Identités de routeur afin qu'elles soient compressibles tout en
restant sécurisées, et sans que leurs représentations en Base 64 ne semblent corrompues ou peu sûres.
Cela permet d'obtenir la plupart des avantages liés à la suppression des champs de remplissage sans nécessiter de
changements de protocole disruptifs.
Les Destinations compressibles réduisent la taille des SYN de streaming et des datagrammes avec accusé de réception ;
les Identités de routeur compressibles réduisent la taille des messages Database Store, des messages SSU2 Session Confirmed,
et des fichiers de reseed au format su3.

Enfin, la proposition examine les possibilités de nouveaux formats pour les Destinations et les Identités de routeur
qui supprimeraient complètement le remplissage. Une brève discussion sur la cryptographie post-quantique
et son impact potentiel sur la planification future est également incluse.



### Objectifs

- Supprimer l'obligation de générer une paire de clés ElGamal pour les Destinations
- Recommander des meilleures pratiques afin que les Destinations et les Identités de routeur soient fortement compressibles,
  tout en n'affichant pas de motifs évidents dans leurs représentations en Base 64.
- Encourager l'adoption de ces meilleures pratiques par toutes les implémentations afin que
  les champs ne soient pas distinguables
- Réduire la taille des SYN de streaming
- Réduire la taille des datagrammes avec accusé de réception
- Réduire la taille du bloc RI SSU2
- Réduire la taille des messages SSU2 Session Confirmed et la fréquence de fragmentation
- Réduire la taille des messages Database Store (avec RI)
- Réduire la taille des fichiers de reseed
- Maintenir la compatibilité dans tous les protocoles et API
- Mettre à jour les spécifications
- Discuter d'alternatives pour de nouveaux formats de Destination et d'Identité de routeur

En supprimant l'obligation de générer des clés ElGamal, les implémentations pourraient
pouvoir supprimer complètement le code ElGamal, sous réserve des considérations de compatibilité ascendante
dans d'autres protocoles.



## Conception

Strictement parlant, la seule clé publique de signature de 32 octets (dans les Destinations et les Identités de routeur)
et la clé publique de chiffrement de 32 octets (dans les Identités de routeur uniquement) constituent un nombre aléatoire
qui fournit toute l'entropie nécessaire pour que les hachages SHA-256 de ces structures
soient cryptographiquement solides et distribués aléatoirement dans la DHT de la base de données du réseau.

Cependant, par excès de prudence, nous recommandons d'utiliser au minimum 32 octets de données aléatoires
dans le champ de clé publique ElGamal et dans le remplissage. De plus, si les champs étaient tous à zéro,
les Destinations en Base 64 contiendraient de longues séquences de caractères AAAA, ce qui pourrait provoquer
de l'inquiétude ou de la confusion chez les utilisateurs.

Pour le type de signature Ed25519 et le type de chiffrement X25519 :
les Destinations contiendront 11 copies (352 octets) des données aléatoires.
Les Identités de routeur contiendront 10 copies (320 octets) des données aléatoires.



### Économies estimées

Les Destinations sont incluses dans chaque SYN de streaming
et chaque datagramme avec accusé de réception.
Les Router Infos (contenant les Identités de routeur) sont incluses dans les messages Database Store
et dans les messages Session Confirmed de NTCP2 et SSU2.

NTCP2 ne compresse pas le Router Info.
Les RIs dans les messages Database Store et les messages SSU2 Session Confirmed sont compressés avec gzip.
Les Router Infos sont compressés avec zip dans les fichiers de reseed SU3.

Les Destinations dans les messages Database Store ne sont pas compressées.
Les messages SYN de streaming sont compressés avec gzip au niveau de la couche I2CP.

Pour le type de signature Ed25519 et le type de chiffrement X25519,
économies estimées :

| Type de données | Taille totale | Clés et certificats | Remplissage non compressé | Remplissage compressé | Taille | Économie |
|-----------------|---------------|---------------------|--------------------------|------------------------|-------|---------|
| Destination | 391 | 39 | 352 | 32 | 71 | 320 octets (82 %) |
| Identité de routeur | 391 | 71 | 320 | 32 | 103 | 288 octets (74 %) |
| Router Info | 1000 typ. | 71 | 320 | 32 | 722 typ. | 288 octets (29 %) |

Notes : suppose qu'un certificat de 7 octets n'est pas compressible, sans surcharge gzip supplémentaire.
Aucune de ces hypothèses n'est strictement vraie, mais les effets seront minimes.
Ignore les autres parties compressibles du Router Info.



## Spécification

Les modifications proposées à nos spécifications actuelles sont documentées ci-dessous.


### Structures communes
Modifier la spécification des structures communes
pour indiquer que le champ de clé publique de 256 octets de la Destination est ignoré et peut
contenir des données aléatoires.

Ajouter une section à la spécification des structures communes
recommandant les meilleures pratiques pour le champ de clé publique de la Destination et les
champs de remplissage dans la Destination et l'Identité de routeur, comme suit :

Générer 32 octets de données aléatoires à l'aide d'un générateur de nombres pseudo-aléatoires cryptographiquement fort (PRNG)
et répéter ces 32 octets autant que nécessaire pour remplir le champ de clé publique (pour les Destinations)
et le champ de remplissage (pour les Destinations et les Identités de routeur).

### Fichier de clé privée
Le format du fichier de clé privée (eepPriv.dat) ne fait pas officiellement partie de nos spécifications,
mais il est documenté dans les [javadocs Java I2P](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html)
et d'autres implémentations le prennent en charge.
Cela permet la portabilité des clés privées entre différentes implémentations.
Ajouter une note dans ces javadocs indiquant que la clé publique de chiffrement peut être du remplissage aléatoire
et que la clé privée de chiffrement peut être composée uniquement de zéros ou de données aléatoires.

### SAM
Préciser dans la spécification SAM que la clé privée de chiffrement est inutilisée et peut être ignorée.
Des données aléatoires quelconques peuvent être retournées par le client.
Le pont SAM peut envoyer des données aléatoires lors de la création (avec DEST GENERATE ou SESSION CREATE DESTINATION=TRANSIENT)
plutôt que des zéros, afin que la représentation en Base 64 ne contienne pas de chaîne de caractères AAAA
et ne semble pas corrompue.


### I2CP
Aucun changement requis pour I2CP. La clé privée correspondant à la clé publique de chiffrement dans la Destination
n'est pas envoyée au routeur.


## Planification future


### Changements de protocole

Au prix de modifications de protocole et d'une perte de compatibilité ascendante, nous pourrions
modifier nos protocoles et spécifications pour supprimer le champ de remplissage dans
la Destination, l'Identité de routeur, ou les deux.

Cette proposition présente des similitudes avec le format de leaseset chiffré « b33 »,
contenant uniquement un champ de clé et un champ de type.

Pour maintenir une certaine compatibilité, certaines couches de protocole pourraient « étendre » le champ de remplissage
avec des zéros pour le présenter aux autres couches de protocole.

Pour les Destinations, nous pourrions également supprimer le champ de type de chiffrement dans le certificat de clé,
avec une économie de deux octets.
Alternativement, les Destinations pourraient obtenir un nouveau type de chiffrement dans le certificat,
indiquant une clé publique nulle (et un remplissage nul).

Si aucune conversion de compatibilité entre les anciens et nouveaux formats n'est incluse à une certaine couche de protocole,
les spécifications, API, protocoles et applications suivants seraient affectés :

- Spécification des structures communes
- I2NP
- I2CP
- NTCP2
- SSU2
- Ratchet
- Streaming
- SAM
- Bittorrent
- Reseeding
- Fichier de clé privée
- API du cœur Java et du routeur
- API i2pd
- Bibliothèques SAM tierces
- Outils intégrés et tiers
- Plusieurs plugins Java
- Interfaces utilisateur
- Applications P2P (ex. MuWire, bitcoin, monero)
- hosts.txt, carnet d'adresses et abonnements

Si une conversion est spécifiée à une certaine couche, la liste serait réduite.

Les coûts et avantages de ces changements ne sont pas clairs.

Propositions spécifiques à déterminer :





### Clés PQ

Les clés publiques de chiffrement post-quantique (PQ), pour tout algorithme anticipé,
sont plus grandes que 256 octets. Cela supprimerait tout remplissage et toute économie découlant des
modifications proposées ci-dessus, pour les Identités de routeur.

Dans une approche PQ « hybride », comme celle utilisée par SSL, les clés PQ seraient uniquement éphémères,
et n'apparaîtraient pas dans l'Identité de routeur.

Les clés de signature PQ ne sont pas viables,
et les Destinations ne contiennent pas de clés publiques de chiffrement.
Les clés statiques pour le ratchet sont dans le Lease Set, pas dans la Destination.
nous pouvons donc exclure les Destinations de la discussion suivante.

Ainsi, PQ n'affecte que les Router Infos, uniquement pour les clés PQ statiques (non éphémères), pas pour le mode hybride PQ.
Cela concernerait un nouveau type de chiffrement et affecterait NTCP2, SSU2, ainsi que
les messages chiffrés de recherche dans la base de données et leurs réponses.
Le délai estimé pour la conception, le développement et le déploiement serait ????????
Mais cela interviendrait après l'adoption du mode hybride ou du ratchet ????????????

Pour approfondir, voir [ce sujet](http://zzz.i2p/topics/3294).




## Problèmes

Il pourrait être souhaitable de réinitialiser progressivement les clés du réseau, afin de fournir une couverture aux nouveaux routeurs.
« Réinitialiser les clés » pourrait simplement signifier changer le remplissage, sans vraiment changer les clés.

Il n'est pas possible de réinitialiser les clés des Destinations existantes.

Les Identités de routeur avec du remplissage dans le champ de clé publique devraient-elles être identifiées avec un type
de chiffrement différent dans le certificat de clé ? Cela poserait des problèmes de compatibilité.




## Migration

Aucun problème de compatibilité ascendante lié au remplacement de la clé ElGamal par du remplissage.

La réinitialisation des clés, si elle est mise en œuvre, serait similaire à celles effectuées
lors des trois transitions précédentes d'identité de routeur :
du passage des signatures DSA-SHA1 aux signatures ECDSA, puis aux
signatures EdDSA, puis au chiffrement X25519.

Sous réserve des problèmes de compatibilité ascendante, et après désactivation de SSU,
les implémentations pourraient supprimer complètement le code ElGamal.
Environ 14 % des routeurs du réseau utilisent le type de chiffrement ElGamal, y compris de nombreux floodfills.

Une demande de fusion préliminaire pour Java I2P est disponible sur [git.idk.i2p](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66).


## Références

* [Common](/docs/specs/common-structures/)
* [Datagram](/docs/api/datagrams/)
* [I2CP](/docs/specs/i2cp/)
* [I2NP](/docs/specs/i2np/)
* [MR](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66)
* [NTCP2](/docs/specs/ntcp2/)
* [PKF](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html)
* [PQ](http://zzz.i2p/topics/3294)
* [SAM](/docs/api/samv3/)
* [SSU2](/docs/specs/ssu2/)
* [Streaming](/docs/specs/streaming/)
