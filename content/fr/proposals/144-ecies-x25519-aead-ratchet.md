---
title: "ECIES-X25519-AEAD-Ratchet"
aliases:
  - "/fr/proposals/144-ecies-x25519"
  - "/fr/proposals/144-ecies-x25519/"
number: "144"
author: "zzz, chisana, orignal"
created: "2018-11-22"
lastupdated: "2025-03-05"
status: "Fermé"
thread: "http://zzz.i2p/topics/2639"
target: "0.9.46"
implementedin: "0.9.46"
toc: true
---
## Note
Déploiement et tests réseau en cours.
Sous réserve de révisions mineures.
Voir [SPEC](/docs/specs/ecies/) pour la spécification officielle.

Les fonctionnalités suivantes ne sont pas implémentées à partir de la version 0.9.46 :

- Blocs MessageNumbers, Options et Termination
- Réponses au niveau du protocole
- Clé statique nulle
- Multidiffusion


## Aperçu

Il s'agit d'une proposition pour le premier nouveau type de chiffrement de bout en bout
depuis le début d'I2P, destiné à remplacer ElGamal/AES+SessionTags [Elg-AES](/docs/specs/elgamal-aes/).

Elle s'appuie sur des travaux antérieurs comme suit :

- Spécification des structures communes [Common Structures](/docs/specs/common-structures/)
- Spécification [I2NP](/docs/specs/i2np/) incluant LS2
- ElGamal/AES+Session Tags [Elg-AES](/docs/specs/elgamal-aes/)
- [http://zzz.i2p/topics/1768](http://zzz.i2p/topics/1768) aperçu de la nouvelle cryptographie asymétrique
- Aperçu de la cryptographie de bas niveau [CRYPTO-ELG](/docs/specs/cryptography/)
- ECIES [http://zzz.i2p/topics/2418](http://zzz.i2p/topics/2418)
- [NTCP2](/docs/specs/ntcp2/) [Proposal 111](/proposals/111-ntcp-2/)
- 123 Nouvelles entrées netDB
- 142 Nouveau modèle de cryptographie
- [Noise](https://noiseprotocol.org/noise.html) protocole
- [Signal](https://signal.org/docs/) algorithme double ratchet

L'objectif est de prendre en charge un nouveau chiffrement de bout en bout,
pour la communication destination-à-destination.

La conception utilisera un échange de clés Noise et une phase de données intégrant le double ratchet de Signal.

Toutes les références à Signal et Noise dans cette proposition sont uniquement destinées à fournir des informations contextuelles.
La connaissance des protocoles Signal et Noise n'est pas requise pour comprendre
ou implémenter cette proposition.


### Utilisations actuelles d'ElGamal

Pour rappel,
les clés publiques ElGamal de 256 octets peuvent être trouvées dans les structures de données suivantes.
Voir la spécification des structures communes.

- Dans une identité de routeur
  Il s'agit de la clé de chiffrement du routeur.

- Dans une destination
  La clé publique de la destination était utilisée pour l'ancien chiffrement i2cp-to-i2cp
  qui a été désactivé à la version 0.6 ; elle est actuellement inutilisée sauf pour
  l'IV du chiffrement du LeaseSet, qui est déprécié.
  La clé publique dans le LeaseSet est utilisée à la place.

- Dans un LeaseSet
  Il s'agit de la clé de chiffrement de la destination.

- Dans un LS2
  Il s'agit de la clé de chiffrement de la destination.



### Types de chiffrement dans les certificats de clé

Pour rappel,
nous avons ajouté le support des types de chiffrement en même temps que celui des types de signature.
Le champ type de chiffrement est toujours à zéro, tant dans les Destinations que dans les RouterIdentities.
Savoir s'il faudra un jour le modifier reste à déterminer.
Voir la spécification des structures communes [Common Structures](/docs/specs/common-structures/).




### Utilisations de la cryptographie asymétrique

Pour rappel, nous utilisons ElGamal pour :

1) Messages de construction de tunnel (la clé est dans RouterIdentity)
   Le remplacement n'est pas couvert par cette proposition.
   Voir la proposition 152 [Proposal 152](/proposals/152-ecies-tunnels).

2) Chiffrement routeur-à-routeur des messages netdb et autres messages I2NP (la clé est dans RouterIdentity)
   Dépend de cette proposition.
   Nécessite une proposition pour 1) également, ou placer la clé dans les options du RI.

3) Chiffrement client de bout en bout ElGamal+AES/SessionTag (la clé est dans LeaseSet, la clé de Destination est inutilisée)
   Le remplacement EST couvert par cette proposition.

4) DH éphémère pour NTCP1 et SSU
   Le remplacement n'est pas couvert par cette proposition.
   Voir la proposition 111 pour NTCP2.
   Aucune proposition actuelle pour SSU2.


### Objectifs

- Compatibilité ascendante
- Nécessite et s'appuie sur LS2 (proposition 123)
- Tirer parti de la nouvelle cryptographie ou des primitives ajoutées pour NTCP2 (proposition 111)
- Aucune nouvelle cryptographie ou primitive requise pour le support
- Maintenir la découplage entre cryptographie et signature ; prendre en charge toutes les versions actuelles et futures
- Activer la nouvelle cryptographie pour les destinations
- Activer la nouvelle cryptographie pour les routeurs, mais uniquement pour les messages garlic - la construction de tunnel ferait
  l'objet d'une proposition distincte
- Ne rien casser qui dépend des hachages binaires de destination de 32 octets, par exemple bittorrent
- Maintenir la livraison de messages en 0-RTT en utilisant DH éphémère-statique
- Ne pas nécessiter de mise en mémoire tampon / file d'attente des messages à ce niveau de protocole ;
  continuer à prendre en charge une livraison illimitée de messages dans les deux sens sans attendre de réponse
- Passer à DH éphémère-éphémère après 1 RTT
- Maintenir la gestion des messages hors ordre
- Maintenir une sécurité de 256 bits
- Ajouter la confidentialité persistante (forward secrecy)
- Ajouter l'authentification (AEAD)
- Beaucoup plus efficace en CPU que ElGamal
- Ne pas dépendre de Java jbigi pour rendre DH efficace
- Minimiser les opérations DH
- Beaucoup plus efficace en bande passante que ElGamal (bloc ElGamal de 514 octets)
- Prendre en charge à la fois l'ancienne et la nouvelle cryptographie sur le même tunnel si souhaité
- Le destinataire doit pouvoir distinguer efficacement la nouvelle cryptographie de l'ancienne arrivant par
  le même tunnel
- Les autres ne doivent pas pouvoir distinguer la nouvelle de l'ancienne ou d'une future cryptographie
- Éliminer la classification longueur de session nouvelle vs. existante (prendre en charge le remplissage)
- Aucun nouveau message I2NP requis
- Remplacer la somme de contrôle SHA-256 dans la charge utile AES par AEAD
- Prendre en charge la liaison des sessions d'émission et de réception afin que
  les accusés de réception puissent se produire dans le protocole, plutôt que uniquement hors bande.
  Cela permettra également aux réponses d'avoir immédiatement la confidentialité persistante.
- Permettre le chiffrement de bout en bout de certains messages (stockage de RouterInfo)
  que nous ne faisons actuellement pas en raison de la surcharge CPU.
- Ne pas modifier le message Garlic I2NP
  ou le format des instructions de livraison du message Garlic.
- Éliminer les champs inutilisés ou redondants dans les formats Garlic Clove Set et Clove.

Éliminer plusieurs problèmes liés aux session tags, notamment :

- Incapacité d'utiliser AES jusqu'à la première réponse
- Fiabilité médiocre et blocages si la livraison des tags est supposée
- Inefficacité en bande passante, surtout lors de la première livraison
- Énorme inefficacité spatiale pour stocker les tags
- Énorme surcharge en bande passante pour livrer les tags
- Très complexe, difficile à implémenter
- Difficile à ajuster pour divers cas d'utilisation
  (streaming vs. datagrammes, serveur vs. client, bande passante élevée vs. faible)
- Vulnérabilités d'épuisement de la mémoire dues à la livraison des tags


### Objectifs non visés / hors sujet

- Changements de format LS2 (la proposition 123 est terminée)
- Nouvel algorithme de rotation DHT ou génération de nombre aléatoire partagé
- Nouveau chiffrement pour la construction de tunnel.
  Voir la proposition 152 [Proposal 152](/proposals/152-ecies-tunnels).
- Nouveau chiffrement pour le chiffrement au niveau du tunnel.
  Voir la proposition 153 [Proposal 153](/proposals/153-chacha20-layer-encryption).
- Méthodes de chiffrement, de transmission et de réception des messages I2NP DLM / DSM / DSRM.
  Non modifiées.
- Aucune communication LS1-to-LS2 ou ElGamal/AES-to-this-proposal n'est prise en charge.
  Cette proposition est un protocole bidirectionnel.
  Les destinations peuvent gérer la compatibilité ascendante en publiant deux leasesets
  en utilisant les mêmes tunnels, ou en mettant les deux types de chiffrement dans le LS2.
- Changements du modèle de menace
- Les détails d'implémentation ne sont pas discutés ici et sont laissés à chaque projet.
- (Optimiste) Ajouter des extensions ou des crochets pour prendre en charge la multidiffusion



### Justification

ElGamal/AES+SessionTag a été notre unique protocole de bout en bout pendant environ 15 ans,
essentiellement sans modifications du protocole.
Il existe désormais des primitives cryptographiques plus rapides.
Nous devons améliorer la sécurité du protocole.
Nous avons également développé des stratégies heuristiques et des solutions de contournement pour minimiser la
surcharge mémoire et en bande passante du protocole, mais ces stratégies
sont fragiles, difficiles à ajuster et rendent le protocole encore plus sujet
aux pannes, entraînant la suppression de la session.

Depuis environ la même période, la spécification ElGamal/AES+SessionTag et la documentation associée
décrivent combien il est coûteux en bande passante de livrer les session tags,
et proposent de remplacer la livraison des session tags par un « PRNG synchronisé ».
Un PRNG synchronisé génère de manière déterministe les mêmes tags aux deux extrémités,
dérivés d'une graine commune.
Un PRNG synchronisé peut également être appelé un « ratchet ».
Cette proposition (enfin) spécifie ce mécanisme de ratchet, et élimine la livraison des tags.

En utilisant un ratchet (un PRNG synchronisé) pour générer les
session tags, nous éliminons la surcharge d'envoi des session tags
dans le message New Session et les messages suivants quand nécessaire.
Pour un ensemble typique de 32 tags, cela représente 1 Ko.
Cela élimine également le stockage des session tags côté émetteur,
réduisant ainsi les besoins de stockage de moitié.

Un échange complet bidirectionnel, similaire au modèle Noise IK, est nécessaire pour éviter les attaques d'impersonnalisation par compromission de clé (KCI).
Voir le tableau « Payload Security Properties » de Noise dans [NOISE](https://noiseprotocol.org/noise.html).
Pour plus d'informations sur KCI, voir l'article https://www.usenix.org/system/files/conference/woot15/woot15-paper-hlauschek.pdf



### Modèle de menace

Le modèle de menace est quelque peu différent de celui de NTCP2 (proposition 111).
Les nœuds MITM sont les OBEP et IBGW et sont supposés avoir une vue complète
de la netDB globale actuelle ou historique, en collusion avec les floodfills.

L'objectif est d'empêcher ces MITM de classer le trafic comme
messages de session nouvelle ou existante, ou comme crypto nouvelle vs. ancienne.



## Proposition détaillée

Cette proposition définit un nouveau protocole de bout en bout pour remplacer ElGamal/AES+SessionTags.
La conception utilisera un échange de clés Noise et une phase de données intégrant le double ratchet de Signal.


### Résumé de la conception cryptographique

Cinq parties du protocole doivent être redéfinies :

- 1) Les formats des conteneurs de session nouvelle et existante
  sont remplacés par de nouveaux formats.
- 2) ElGamal (clés publiques de 256 octets, clés privées de 128 octets) est remplacé
  par ECIES-X25519 (clés publiques et privées de 32 octets)
- 3) AES est remplacé par
  AEAD_ChaCha20_Poly1305 (abrégé ChaChaPoly ci-dessous)
- 4) Les SessionTags seront remplacés par des ratchets,
  qui est essentiellement un PRNG cryptographique synchronisé.
- 5) La charge utile AES, telle que définie dans la spécification ElGamal/AES+SessionTags,
  est remplacée par un format de bloc similaire à celui de NTCP2.

Chacun des cinq changements a sa propre section ci-dessous.


### Nouvelles primitives cryptographiques pour I2P

Les implémentations existantes du routeur I2P nécessiteront des implémentations des
primitives cryptographiques standard suivantes,
qui ne sont pas requises pour les protocoles I2P actuels :

- ECIES (mais c'est essentiellement X25519)
- Elligator2

Les implémentations existantes du routeur I2P qui n'ont pas encore implémenté [NTCP2](/docs/specs/ntcp2/) ([Proposal 111](/proposals/111-ntcp-2/))
auront également besoin d'implémentations pour :

- Génération de clés X25519 et DH
- AEAD_ChaCha20_Poly1305 (abrégé ChaChaPoly ci-dessous)
- HKDF


### Type de chiffrement

Le type de chiffrement (utilisé dans le LS2) est 4.
Cela indique une clé publique X25519 de 32 octets en little-endian,
et le protocole de bout en bout spécifié ici.

Le type de chiffrement 0 est ElGamal.
Les types de chiffrement 1-3 sont réservés pour ECIES-ECDH-AES-SessionTag, voir la proposition 145 [Proposal 145](/proposals/145-ecies).


### Cadre du protocole Noise

Cette proposition fournit les exigences basées sur le cadre du protocole Noise
[NOISE](https://noiseprotocol.org/noise.html) (Révision 34, 2018-07-11).
Noise a des propriétés similaires au protocole Station-To-Station
[STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol), qui est la base du protocole [SSU](/docs/legacy/ssu/). En termes Noise, Alice
est l'initiateur, et Bob est le répondant.

Cette proposition est basée sur le protocole Noise Noise_IK_25519_ChaChaPoly_SHA256.
(L'identifiant réel pour la fonction de dérivation de clé initiale
est « Noise_IKelg2_25519_ChaChaPoly_SHA256 »
pour indiquer les extensions I2P - voir la section KDF 1 ci-dessous)
Ce protocole Noise utilise les primitives suivantes :

- Modèle d'échange interactif : IK
  Alice transmet immédiatement sa clé statique à Bob (I)
  Alice connaît déjà la clé statique de Bob (K)

- Modèle d'échange unidirectionnel : N
  Alice ne transmet pas sa clé statique à Bob (N)

- Fonction DH : X25519
  DH X25519 avec une longueur de clé de 32 octets comme spécifié dans [RFC-7748](https://tools.ietf.org/html/rfc7748).

- Fonction de chiffrement : ChaChaPoly
  AEAD_CHACHA20_POLY1305 comme spécifié dans [RFC-7539](https://tools.ietf.org/html/rfc7539) section 2.8.
  Nonce de 12 octets, avec les 4 premiers octets à zéro.
  Identique à celle de [NTCP2](/docs/specs/ntcp2/).

- Fonction de hachage : SHA256
  Hachage standard de 32 octets, déjà largement utilisé dans I2P.


### Ajouts au cadre

Cette proposition définit les améliorations suivantes à
Noise_IK_25519_ChaChaPoly_SHA256. Ces éléments suivent généralement les directives de
[NOISE](https://noiseprotocol.org/noise.html) section 13.

1) Les clés éphémères en clair sont encodées avec [Elligator2](https://elligator.cr.yp.to/).

2) La réponse est préfixée par un tag en clair.

3) Le format de charge utile est défini pour les messages 1, 2, et la phase de données.
   Bien sûr, cela n'est pas défini dans Noise.

Tous les messages incluent un en-tête de message Garlic [I2NP](/docs/specs/i2np/).
La phase de données utilise un chiffrement similaire, mais non compatible, à la phase de données Noise.


### Modèles d'échange

Les échanges utilisent les modèles d'échange [Noise](https://noiseprotocol.org/noise.html).

La correspondance des lettres suivante est utilisée :

- e = clé éphémère ponctuelle
- s = clé statique
- p = charge utile du message

Les sessions ponctuelles et non liées sont similaires au modèle Noise N.

```

<- s
  ...
  e es p ->

```

Les sessions liées sont similaires au modèle Noise IK.

```

<- s
  ...
  e es s ss p ->
  <- tag e ee se
  <- p
  p ->

```


### Sessions

Le protocole actuel ElGamal/AES+SessionTag est unidirectionnel.
À ce niveau, le récepteur ne sait pas d'où vient un message.
Les sessions sortantes et entrantes ne sont pas associées.
Les accusés de réception sont hors bande en utilisant un DeliveryStatusMessage
(encapsulé dans un GarlicMessage) dans l'épice.

Il existe une inefficacité substantielle dans un protocole unidirectionnel.
Toute réponse doit également utiliser un message coûteux « New Session ».
Cela entraîne une utilisation plus élevée de la bande passante, du CPU et de la mémoire.

Il existe également des faiblesses de sécurité dans un protocole unidirectionnel.
Toutes les sessions sont basées sur DH éphémère-statique.
Sans chemin de retour, Bob ne peut pas « ratchet » sa clé statique
vers une clé éphémère.
Sans savoir d'où vient un message, il est impossible d'utiliser
la clé éphémère reçue pour les messages sortants,
donc la réponse initiale utilise également DH éphémère-statique.

Pour cette proposition, nous définissons deux mécanismes pour créer un protocole bidirectionnel -
« appariement » et « liaison ».
Ces mécanismes offrent une efficacité et une sécurité accrues.


### Contexte de session

Comme avec ElGamal/AES+SessionTags, toutes les sessions entrantes et sortantes
doivent être dans un contexte donné, soit le contexte du routeur, soit
le contexte pour une destination locale particulière.
Dans Java I2P, ce contexte est appelé Session Key Manager.

Les sessions ne doivent pas être partagées entre contextes, car cela permettrait
la corrélation entre les différentes destinations locales,
ou entre une destination locale et un routeur.

Lorsqu'une destination donnée prend en charge à la fois ElGamal/AES+SessionTags
et cette proposition, les deux types de sessions peuvent partager un contexte.
Voir la section 1c) ci-dessous.



### Appariement des sessions entrantes et sortantes

Lorsqu'une session sortante est créée à l'origine (Alice),
une nouvelle session entrante est créée et appariée à la session sortante,
sauf si aucune réponse n'est attendue (par exemple, datagrammes bruts).

Une nouvelle session entrante est toujours appariée à une nouvelle session sortante,
sauf si aucune réponse n'est demandée (par exemple, datagrammes bruts).

Si une réponse est demandée et liée à une destination ou un routeur distant,
cette nouvelle session sortante est liée à cette destination ou ce routeur,
et remplace toute session sortante précédente vers cette destination ou ce routeur.

L'appariement des sessions entrantes et sortantes fournit un protocole bidirectionnel
avec la capacité de ratchet les clés DH.



### Liaison des sessions et des destinations

Il n'y a qu'une seule session sortante vers une destination ou un routeur donné.
Il peut y avoir plusieurs sessions entrantes actuelles provenant d'une destination ou d'un routeur donné.
Généralement, lorsqu'une nouvelle session entrante est créée, et que du trafic est reçu
sur cette session (ce qui sert d'accusé de réception), les autres seront marquées
pour expirer relativement rapidement, en une minute environ.
La valeur des messages précédemment envoyés (PN) est vérifiée, et s'il n'y a pas
de messages non reçus (dans la fenêtre de taille) dans la session entrante précédente,
la session précédente peut être supprimée immédiatement.


Lorsqu'une session sortante est créée à l'origine (Alice),
elle est liée à la destination distante (Bob),
et toute session entrante appariée sera également liée à la destination distante.
Au fur et à mesure que les sessions ratchet, elles continuent d'être liées à la destination distante.

Lorsqu'une session entrante est créée au récepteur (Bob),
elle peut être liée à la destination distante (Alice), au choix d'Alice.
Si Alice inclut des informations de liaison (sa clé statique) dans le message New Session,
la session sera liée à cette destination,
et une session sortante sera créée et liée à la même destination.
Au fur et à mesure que les sessions ratchet, elles continuent d'être liées à la destination distante.


### Avantages de la liaison et de l'appariement

Pour le cas courant de streaming, nous nous attendons à ce qu'Alice et Bob utilisent le protocole comme suit :

- Alice apparie sa nouvelle session sortante à une nouvelle session entrante, les deux liées à la destination distante (Bob).
- Alice inclut les informations de liaison et la signature, et une demande de réponse, dans le
  message New Session envoyé à Bob.
- Bob apparie sa nouvelle session entrante à une nouvelle session sortante, les deux liées à la destination distante (Alice).
- Bob envoie une réponse (accusé de réception) à Alice dans la session appariée, avec un ratchet vers une nouvelle clé DH.
- Alice ratchet vers une nouvelle session sortante avec la nouvelle clé de Bob, appariée à la session entrante existante.

En liant une session entrante à une destination distante, et en appariant la session entrante
à une session sortante liée à la même destination, nous obtenons deux avantages majeurs :

1) La réponse initiale de Bob à Alice utilise DH éphémère-éphémère

2) Après qu'Alice a reçu la réponse de Bob et ratcheté, tous les messages suivants d'Alice à Bob
utilisent DH éphémère-éphémère.


### Accusés de réception de messages

Dans ElGamal/AES+SessionTags, lorsqu'un LeaseSet est inclus comme épice garlic,
ou que des tags sont livrés, le routeur émetteur demande un accusé de réception.
C'est une épice garlic séparée contenant un message DeliveryStatus.
Pour une sécurité supplémentaire, le message DeliveryStatus est encapsulé dans un message Garlic.
Ce mécanisme est hors bande du point de vue du protocole.

Dans le nouveau protocole, puisque les sessions entrantes et sortantes sont appariées,
nous pouvons avoir des accusés de réception en bande. Aucune épice séparée n'est requise.

Un accusé de réception explicite est simplement un message Existing Session sans bloc I2NP.
Cependant, dans la plupart des cas, un accusé de réception explicite peut être évité, car il y a du trafic inverse.
Il peut être souhaitable que les implémentations attendent un court instant (peut-être une centaine de ms)
avant d'envoyer un accusé de réception explicite, pour laisser le temps à la couche de streaming ou d'application de répondre.

Les implémentations devront également différer l'envoi de tout accusé de réception jusqu'à ce que le
bloc I2NP soit traité, car le message Garlic peut contenir un message Database Store
avec un lease set. Un lease set récent sera nécessaire pour router l'accusé de réception,
et la destination distante (contenue dans le lease set) sera nécessaire pour
vérifier la clé statique liée.


### Durées d'expiration des sessions

Les sessions sortantes doivent toujours expirer avant les sessions entrantes.
Une fois qu'une session sortante expire, et qu'une nouvelle est créée, une nouvelle session entrante appariée
sera également créée. Si une ancienne session entrante existait,
elle sera autorisée à expirer.


### Multidiffusion

À déterminer


### Définitions
Nous définissons les fonctions suivantes correspondant aux blocs de construction cryptographiques utilisés.

ZEROLEN
    tableau d'octets de longueur nulle

CSRNG(n)
    sortie de n octets d'un générateur de nombres aléatoires cryptographiquement sécurisé.

H(p, d)
    fonction de hachage SHA-256 qui prend une chaîne de personnalisation p et des données d, et
    produit une sortie de longueur 32 octets.
    Comme défini dans [NOISE](https://noiseprotocol.org/noise.html).
    || ci-dessous signifie concaténer.

    Utiliser SHA-256 comme suit::

        H(p, d) := SHA-256(p || d)

MixHash(d)
    fonction de hachage SHA-256 qui prend un hachage précédent h et de nouvelles données d,
    et produit une sortie de longueur 32 octets.
    || ci-dessous signifie concaténer.

    Utiliser SHA-256 comme suit::

        MixHash(d) := h = SHA-256(h || d)

STREAM
    Le chiffrement AEAD ChaCha20/Poly1305 tel que spécifié dans [RFC-7539](https://tools.ietf.org/html/rfc7539).
    S_KEY_LEN = 32 et S_IV_LEN = 12.

    ENCRYPT(k, n, plaintext, ad)
        Chiffre le texte en clair en utilisant la clé de chiffrement k, et le nonce n qui DOIT être unique pour
        la clé k.
        Les données associées ad sont facultatives.
        Renvoie un texte chiffré de la taille du texte en clair + 16 octets pour le HMAC.

        Le texte chiffré entier doit être indiscernable d'aléatoire si la clé est secrète.

    DECRYPT(k, n, ciphertext, ad)
        Déchiffre le texte chiffré en utilisant la clé de chiffrement k, et le nonce n.
        Les données associées ad sont facultatives.
        Renvoie le texte en clair.

DH
    Système d'accord de clé publique X25519. Clés privées de 32 octets, clés publiques de 32
    octets, produit des sorties de 32 octets. Il possède les fonctions suivantes :

    GENERATE_PRIVATE()
        Génère une nouvelle clé privée.

    DERIVE_PUBLIC(privkey)
        Renvoie la clé publique correspondant à la clé privée donnée.

    GENERATE_PRIVATE_ELG2()
        Génère une nouvelle clé privée qui correspond à une clé publique adaptée à l'encodage Elligator2.
        Notez que la moitié des clés privées générées aléatoirement ne seront pas adaptées et devront être rejetées.

    ENCODE_ELG2(pubkey)
        Renvoie la clé publique encodée avec Elligator2 correspondant à la clé publique donnée (carte inverse).
        Les clés encodées sont en little-endian.
        La clé encodée doit être de 256 bits indiscernables de données aléatoires.
        Voir la section Elligator2 ci-dessous pour la spécification.

    DECODE_ELG2(pubkey)
        Renvoie la clé publique correspondant à la clé publique encodée avec Elligator2 donnée.
        Voir la section Elligator2 ci-dessous pour la spécification.

    DH(privkey, pubkey)
        Génère un secret partagé à partir des clés privée et publique données.

HKDF(salt, ikm, info, n)
    Une fonction de dérivation de clé cryptographique qui prend du matériel de clé d'entrée ikm (qui
    devrait avoir une bonne entropie mais n'est pas requis d'être une chaîne uniformément aléatoire), un sel
    de longueur 32 octets, et une valeur 'info' spécifique au contexte, et produit une sortie
    de n octets adaptée à une utilisation comme matériel de clé.

    Utiliser HKDF tel que spécifié dans [RFC-5869](https://tools.ietf.org/html/rfc5869), en utilisant la fonction de hachage HMAC SHA-256
    tel que spécifié dans [RFC-2104](https://tools.ietf.org/html/rfc2104). Cela signifie que SALT_LEN est au maximum 32 octets.

MixKey(d)
    Utilise HKDF() avec une chainKey précédente et de nouvelles données d, et
    définit la nouvelle chainKey et k.
    Comme défini dans [NOISE](https://noiseprotocol.org/noise.html).

    Utiliser HKDF comme suit::

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]



### 1) Format du message


### Aperçu du format de message actuel

Le message Garlic tel que spécifié dans [I2NP](/docs/specs/i2np/) est le suivant.
Étant donné que l'objectif de conception est que les nœuds intermédiaires ne puissent pas distinguer la nouvelle de l'ancienne cryptographie,
ce format ne peut pas changer, même si le champ de longueur est redondant.
Le format est montré avec l'en-tête complet de 16 octets, bien que l'
en-tête réel puisse être dans un format différent, selon le transport utilisé.

Une fois déchiffré, les données contiennent une série d'épices Garlic et des données supplémentaires,
également appelées Clove Set.

Voir [I2NP](/docs/specs/i2np/) pour les détails et une spécification complète.


```

+----+----+----+----+----+----+----+----+
  |type|      msg_id       |  expiration
  +----+----+----+----+----+----+----+----+
                           |  size   |chks|
  +----+----+----+----+----+----+----+----+
  |      length       |                   |
  +----+----+----+----+                   +
  |          encrypted data               |
  ~                                       ~
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

```


### Aperçu du format des données chiffrées

Le format de message actuel, utilisé depuis plus de 15 ans,
est ElGamal/AES+SessionTags.
Dans ElGamal/AES+SessionTags, il existe deux formats de message :

1) Nouvelle session :
- Bloc ElGamal de 514 octets
- Bloc AES (minimum 128 octets, multiple de 16)

2) Session existante :
- Tag de session de 32 octets
- Bloc AES (minimum 128 octets, multiple de 16)

Le remplissage minimal à 128 est tel qu'implémenté dans Java I2P mais n'est pas appliqué à la réception.

Ces messages sont encapsulés dans un message garlic I2NP, qui contient
un champ de longueur, donc la longueur est connue.

Notez qu'aucun remplissage n'est défini pour une longueur non mod-16,
donc la Nouvelle Session est toujours (mod 16 == 2),
et une Session existante est toujours (mod 16 == 0).
Nous devons corriger cela.

Le récepteur tente d'abord de rechercher les 32 premiers octets comme Tag de session.
S'il est trouvé, il déchiffre le bloc AES.
S'il n'est pas trouvé, et que les données sont d'au moins (514+16) octets de long, il tente de déchiffrer le bloc ElGamal,
et s'il réussit, déchiffre le bloc AES.


### Nouveaux Session Tags et comparaison avec Signal

Dans le double ratchet de Signal, l'en-tête contient :

- DH : Clé publique actuelle du ratchet
- PN : Longueur du message de la chaîne précédente
- N : Numéro de message

Les « chaînes d'envoi » de Signal sont approximativement équivalentes à nos ensembles de tags.
En utilisant un session tag, nous pouvons éliminer la plupart de cela.

Dans New Session, nous mettons uniquement la clé publique dans l'en-tête non chiffré.

Dans Existing Session, nous utilisons un session tag pour l'en-tête.
Le session tag est associé à la clé publique actuelle du ratchet,
et au numéro de message.

Dans les deux cas, New et Existing Session, PN et N sont dans le corps chiffré.

Dans Signal, les choses ratchettent constamment. Une nouvelle clé publique DH nécessite que le
récepteur ratchet et envoie une nouvelle clé publique en retour, ce qui sert également
d'accusé de réception pour la clé publique reçue.
Cela représenterait trop d'opérations DH pour nous.
Nous séparons donc l'accusé de réception de la clé reçue et la transmission d'une nouvelle clé publique.
Tout message utilisant un session tag généré à partir de la nouvelle clé publique DH constitue un accusé de réception.
Nous ne transmettons une nouvelle clé publique que lorsque nous souhaitons réinitialiser la clé.

Le nombre maximum de messages avant que le DH doive ratchet est 65535.

Lors de la livraison d'une clé de session, nous dérivons l'« Ensemble de Tags » à partir de celle-ci,
plutôt que de devoir livrer également les session tags.
Un Ensemble de Tags peut contenir jusqu'à 65536 tags.
Cependant, les récepteurs devraient implémenter une stratégie de « prélecture »,
plutôt que de générer tous les tags possibles en même temps.
Générer au maximum N tags après le dernier bon tag reçu.
N pourrait être au maximum 128, mais 32 ou même moins pourrait être un meilleur choix.



### 1a) Format de nouvelle session

Clé publique éphémère de nouvelle session (32 octets)
Données chiffrées et MAC (octets restants)

Le message New Session peut ou non contenir la clé publique statique de l'émetteur.
S'il est inclus, la session inverse est liée à cette clé.
La clé statique devrait être incluse si des réponses sont attendues,
c'est-à-dire pour le streaming et les datagrammes répliables.
Elle ne devrait pas être incluse pour les datagrammes bruts.

Le message New Session est similaire au modèle unidirectionnel Noise [NOISE](https://noiseprotocol.org/noise.html)
« N » (si la clé statique n'est pas envoyée),
ou au modèle bidirectionnel « IK » (si la clé statique est envoyée).



### 1b) Format de nouvelle session (avec liaison)

Longueur est 96 + longueur de la charge utile.
Format chiffré :

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   Clé publique éphémère de nouvelle session    |
  +             32 octets                  +
  |     Encodée avec Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +         Clé statique                    +
  |       Données chiffrées ChaCha20         |
  +            32 octets                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Code d'authentification de message Poly1305 |
  +    (MAC) pour la section Clé statique       +
  |             16 octets                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Section charge utile            +
  |       Données chiffrées ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Code d'authentification de message Poly1305 |
  +         (MAC) pour la section charge utile     +
  |             16 octets                  |
  +----+----+----+----+----+----+----+----+

  Clé publique :: 32 octets, little-endian, Elligator2, en clair

  Données chiffrées de la clé statique :: 32 octets

  Données chiffrées de la section charge utile :: données restantes moins 16 octets

  MAC :: Code d'authentification de message Poly1305, 16 octets

```


### Clé éphémère de nouvelle session

La clé éphémère est de 32 octets, encodée avec Elligator2.
Cette clé n'est jamais réutilisée ; une nouvelle clé est générée avec
chaque message, y compris les retransmissions.

### Clé statique

Lorsqu'elle est déchiffrée, la clé statique X25519 d'Alice, 32 octets.


### Charge utile

La longueur chiffrée est le reste des données.
La longueur déchiffrée est 16 octets de moins que la longueur chiffrée.
La charge utile doit contenir un bloc DateTime et contiendra généralement un ou plusieurs blocs Garlic Clove.
Voir la section charge utile ci-dessous pour le format et les exigences supplémentaires.



### 1c) Format de nouvelle session (sans liaison)

S'il n'est pas nécessaire de répondre, aucune clé statique n'est envoyée.


Longueur est 96 + longueur de la charge utile.
Format chiffré :

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   Clé publique éphémère de nouvelle session    |
  +             32 octets                  +
  |     Encodée avec Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Section indicateurs               +
  |       Données chiffrées ChaCha20         |
  +            32 octets                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Code d'authentification de message Poly1305 |
  +         (MAC) pour la section ci-dessus       +
  |             16 octets                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Section charge utile            +
  |       Données chiffrées ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Code d'authentification de message Poly1305 |
  +         (MAC) pour la section charge utile     +
  |             16 octets                  |
  +----+----+----+----+----+----+----+----+

  Clé publique :: 32 octets, little-endian, Elligator2, en clair

  Données chiffrées de la section indicateurs :: 32 octets

  Données chiffrées de la section charge utile :: données restantes moins 16 octets

  MAC :: Code d'authentification de message Poly1305, 16 octets

```

### Clé éphémère de nouvelle session

Clé éphémère d'Alice.
La clé éphémère est de 32 octets, encodée avec Elligator2, little-endian.
Cette clé n'est jamais réutilisée ; une nouvelle clé est générée avec
chaque message, y compris les retransmissions.


### Données déchiffrées de la section indicateurs

La section indicateurs ne contient rien.
Elle fait toujours 32 octets, car elle doit avoir la même longueur
que la clé statique pour les messages New Session avec liaison.
Bob détermine s'il s'agit d'une clé statique ou d'une section indicateurs
en testant si les 32 octets sont tous des zéros.

TODO des indicateurs sont-ils nécessaires ici ?

### Charge utile

La longueur chiffrée est le reste des données.
La longueur déchiffrée est 16 octets de moins que la longueur chiffrée.
La charge utile doit contenir un bloc DateTime et contiendra généralement un ou plusieurs blocs Garlic Clove.
Voir la section charge utile ci-dessous pour le format et les exigences supplémentaires.




### 1d) Format ponctuel (sans liaison ni session)

S'il n'est attendu qu'un seul message,
aucune configuration de session ou clé statique n'est requise.


Longueur est 96 + longueur de la charge utile.
Format chiffré :

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |       Clé publique éphémère            |
  +             32 octets                  +
  |     Encodée avec Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Section indicateurs               +
  |       Données chiffrées ChaCha20         |
  +            32 octets                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Code d'authentification de message Poly1305 |
  +         (MAC) pour la section ci-dessus       +
  |             16 octets                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Section charge utile            +
  |       Données chiffrées ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Code d'authentification de message Poly1305 |
  +         (MAC) pour la section charge utile     +
  |             16 octets                  |
  +----+----+----+----+----+----+----+----+

  Clé publique :: 32 octets, little-endian, Elligator2, en clair

  Données chiffrées de la section indicateurs :: 32 octets

  Données chiffrées de la section charge utile :: données restantes moins 16 octets

  MAC :: Code d'authentification de message Poly1305, 16 octets

```


### Clé ponctuelle de nouvelle session

La clé ponctuelle est de 32 octets, encodée avec Elligator2, little-endian.
Cette clé n'est jamais réutilisée ; une nouvelle clé est générée avec
chaque message, y compris les retransmissions.


### Données déchiffrées de la section indicateurs

La section indicateurs ne contient rien.
Elle fait toujours 32 octets, car elle doit avoir la même longueur
que la clé statique pour les messages New Session avec liaison.
Bob détermine s'il s'agit d'une clé statique ou d'une section indicateurs
en testant si les 32 octets sont tous des zéros.

TODO des indicateurs sont-ils nécessaires ici ?

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                                       |
  +             Tous des zéros                 +
  |              32 octets                 |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+

  zéros:: Tous des zéros, 32 octets.

```


### Charge utile

La longueur chiffrée est le reste des données.
La longueur déchiffrée est 16 octets de moins que la longueur chiffrée.
La charge utile doit contenir un bloc DateTime et contiendra généralement un ou plusieurs blocs Garlic Clove.
Voir la section charge utile ci-dessous pour le format et les exigences supplémentaires.



### 1f) KDF pour le message New Session

### KDF pour la chainKey initiale

C'est le [NOISE](https://noiseprotocol.org/noise.html) standard pour IK avec un nom de protocole modifié.
Notez que nous utilisons le même initialiseur pour les deux modèles IK (sessions liées)
et pour le modèle N (sessions non liées).

Le nom du protocole est modifié pour deux raisons.
Premièrement, pour indiquer que les clés éphémères sont encodées avec Elligator2,
et deuxièmement, pour indiquer que MixHash() est appelé avant le deuxième message
pour mélanger la valeur du tag.

```

C'est le modèle de message « e » :

  // Définir protocol_name.
  Définir protocol_name = "Noise_IKelg2+hs2_25519_ChaChaPoly_SHA256"
   (40 octets, encodage US-ASCII, sans terminaison NULL).

  // Définir Hash h = 32 octets
  h = SHA256(protocol_name);

  Définir ck = 32 octets de clé de chaînage. Copier les données h dans ck.
  Définir chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // jusqu'ici, peut être précalculé par Alice pour toutes les connexions sortantes

```


### KDF pour le contenu chiffré de la section indicateurs/clé statique

```

C'est le modèle de message « e » :

  // Clés X25519 statiques de Bob
  // bpk est publiée dans le leaseset
  bsk = GENERATE_PRIVATE()
  bpk = DERIVE_PUBLIC(bsk)

  // Clé publique statique de Bob
  // MixHash(bpk)
  // || ci-dessous signifie concaténer
  h = SHA256(h || bpk);

  // jusqu'ici, peut être précalculé par Bob pour toutes les connexions entrantes

  // Clés X25519 éphémères d'Alice
  aesk = GENERATE_PRIVATE_ELG2()
  aepk = DERIVE_PUBLIC(aesk)

  // Clé publique éphémère d'Alice
  // MixHash(aepk)
  // || ci-dessous signifie concaténer
  h = SHA256(h || aepk);

  // h est utilisé comme données associées pour l'AEAD dans le message New Session
  // Conserver le Hash h pour le KDF de réponse New Session
  // eapk est envoyé en clair au
  // début du message New Session
  elg2_aepk = ENCODE_ELG2(aepk)
  // Comme décodé par Bob
  aepk = DECODE_ELG2(elg2_aepk)

  Fin du modèle de message « e ».

  C'est le modèle de message « es » :

  // Noise es
  sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Paramètres ChaChaPoly pour chiffrer/déchiffrer
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Paramètres AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, section indicateurs/clé statique, ad)

  Fin du modèle de message « es ».

  C'est le modèle de message « s » :

  // MixHash(ciphertext)
  // Sauvegarder pour le KDF de la section charge utile
  h = SHA256(h || ciphertext)

  // Clés X25519 statiques d'Alice
  ask = GENERATE_PRIVATE()
  apk = DERIVE_PUBLIC(ask)

  Fin du modèle de message « s ».


```



### KDF pour la section charge utile (avec clé statique d'Alice)

```

C'est le modèle de message « ss » :

  // Noise ss
  sharedSecret = DH(ask, bpk) = DH(bsk, apk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Paramètres ChaChaPoly pour chiffrer/déchiffrer
  // chainKey provenant de la section clé statique
  Définir sharedSecret = résultat DH X25519
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Paramètres AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, charge utile, ad)

  Fin du modèle de message « ss ».

  // MixHash(ciphertext)
  // Sauvegarder pour le KDF de réponse New Session
  h = SHA256(h || ciphertext)

```


### KDF pour la section charge utile (sans clé statique d'Alice)

Notez que c'est un modèle Noise « N », mais nous utilisons le même initialiseur « IK »
que pour les sessions liées.

Les messages New Session ne peuvent pas être identifiés comme contenant la clé statique d'Alice ou non
jusqu'à ce que la clé statique soit déchiffrée et inspectée pour déterminer si elle contient uniquement des zéros.
Par conséquent, le récepteur doit utiliser la machine d'état « IK » pour tous
les messages New Session.
Si la clé statique est entièrement nulle, le modèle de message « ss » doit être ignoré.



```

chainKey = provenant de la section clé statique/indicateurs
  k = provenant de la section clé statique/indicateurs
  n = 1
  ad = h provenant de la section clé statique/indicateurs
  ciphertext = ENCRYPT(k, n, charge utile, ad)

```



### 1g) Format de réponse New Session

Un ou plusieurs messages New Session Reply peuvent être envoyés en réponse à un seul message New Session.
Chaque réponse est préfixée par un tag, qui est généré à partir d'un TagSet pour la session.

La réponse New Session se compose de deux parties.
La première partie est la finalisation de l'échange de clés Noise IK avec un tag préfixé.
La longueur de la première partie est de 56 octets.
La deuxième partie est la charge utile de la phase de données.
La longueur de la deuxième partie est de 16 + longueur de la charge utile.

Longueur totale est 72 + longueur de la charge utile.
Format chiffré :

```

+----+----+----+----+----+----+----+----+
  |       Session Tag   8 octets           |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Clé publique éphémère           +
  |                                       |
  +            32 octets                   +
  |     Encodée avec Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Code d'authentification de message Poly1305 |
  +  (MAC) pour la section clé (pas de données)      +
  |             16 octets                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Section charge utile            +
  |       Données chiffrées ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Code d'authentification de message Poly1305 |
  +         (MAC) pour la section charge utile     +
  |             16 octets                  |
  +----+----+----+----+----+----+----+----+

  Tag :: 8 octets, en clair

  Clé publique :: 32 octets, little-endian, Elligator2, en clair

  MAC :: Code d'authentification de message Poly1305, 16 octets
         Remarque : Les données en clair ChaCha20 sont vides (ZEROLEN)

  Données chiffrées de la section charge utile :: données restantes moins 16 octets

  MAC :: Code d'authentification de message Poly1305, 16 octets

```

### Session Tag
Le tag est généré dans le KDF des Session Tags, tel qu'initialisé
dans le KDF d'initialisation DH ci-dessous.
Cela corrèle la réponse à la session.
La Session Key provenant de l'initialisation DH n'est pas utilisée.


### Clé éphémère de réponse New Session

Clé éphémère de Bob.
La clé éphémère est de 32 octets, encodée avec Elligator2, little-endian.
Cette clé n'est jamais réutilisée ; une nouvelle clé est générée avec
chaque message, y compris les retransmissions.


### Charge utile
La longueur chiffrée est le reste des données.
La longueur déchiffrée est 16 octets de moins que la longueur chiffrée.
La charge utile contiendra généralement un ou plusieurs blocs Garlic Clove.
Voir la section charge utile ci-dessous pour le format et les exigences supplémentaires.


### KDF pour le TagSet de réponse

Un ou plusieurs tags sont créés à partir du TagSet, qui est initialisé en utilisant
le KDF ci-dessous, en utilisant la chainKey du message New Session.

```

// Générer tagset
  tagsetKey = HKDF(chainKey, ZEROLEN, "SessionReplyTags", 32)
  tagset_nsr = DH_INITIALIZE(chainKey, tagsetKey)

```


### KDF pour le contenu chiffré de la section clé de réponse

```

// Clés du message New Session
  // Clés X25519 d'Alice
  // apk et aepk sont envoyées dans le message New Session original
  // ask = clé privée statique d'Alice
  // apk = clé publique statique d'Alice
  // aesk = clé privée éphémère d'Alice
  // aepk = clé publique éphémère d'Alice
  // Clés X25519 statiques de Bob
  // bsk = clé privée statique de Bob
  // bpk = clé publique statique de Bob

  // Générer le tag
  tagsetEntry = tagset_nsr.GET_NEXT_ENTRY()
  tag = tagsetEntry.SESSION_TAG

  // MixHash(tag)
  h = SHA256(h || tag)

  C'est le modèle de message « e » :

  // Clés X25519 éphémères de Bob
  besk = GENERATE_PRIVATE_ELG2()
  bepk = DERIVE_PUBLIC(besk)

  // Clé publique éphémère de Bob
  // MixHash(bepk)
  // || ci-dessous signifie concaténer
  h = SHA256(h || bepk);

  // elg2_bepk est envoyé en clair au
  // début du message New Session
  elg2_bepk = ENCODE_ELG2(bepk)
  // Comme décodé par Bob
  bepk = DECODE_ELG2(elg2_bepk)

  Fin du modèle de message « e ».

  C'est le modèle de message « ee » :

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Paramètres ChaChaPoly pour chiffrer/déchiffrer
  // chainKey provenant de la section charge utile du New Session original
  sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
  keydata = HKDF(chainKey, sharedSecret, "", 32)
  chainKey = keydata[0:31]

  Fin du modèle de message « ee ».

  C'est le modèle de message « se » :

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  sharedSecret = DH(ask, bepk) = DH(besk, apk)
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Paramètres AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, ZEROLEN, ad)

  Fin du modèle de message « se ».

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  chainKey est utilisé dans le ratchet ci-dessous.

```


### KDF pour le contenu chiffré de la section charge utile

C'est comme le premier message Existing Session,
post-split, mais sans tag séparé.
De plus, nous utilisons le hachage ci-dessus pour lier la
charge utile au message NSR.


```

// split()
  keydata = HKDF(chainKey, ZEROLEN, "", 64)
  k_ab = keydata[0:31]
  k_ba = keydata[32:63]
  tagset_ab = DH_INITIALIZE(chainKey, k_ab)
  tagset_ba = DH_INITIALIZE(chainKey, k_ba)

  // Paramètres AEAD pour la charge utile de réponse New Session
  k = HKDF(k_ba, ZEROLEN, "AttachPayloadKDF", 32)
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, charge utile, ad)
```


### Notes

Plusieurs messages NSR peuvent être envoyés en réponse, chacun avec des clés éphémères uniques, selon la taille de la réponse.

Alice et Bob doivent utiliser de nouvelles clés éphémères pour chaque message NS et NSR.

Alice doit recevoir l'un des messages NSR de Bob avant d'envoyer des messages Existing Session (ES),
et Bob doit recevoir un message ES d'Alice avant d'envoyer des messages ES.

La ``chainKey`` et ``k`` de la section charge utile du NSR de Bob sont utilisées
comme entrées pour les ratchets DH ES initiaux (dans les deux sens, voir KDF du ratchet DH).

Bob ne doit conserver que les sessions existantes pour les messages ES reçus d'Alice.
Toutes les autres sessions entrantes et sortantes créées (pour plusieurs NSR) doivent être
détruites immédiatement après avoir reçu le premier message ES d'Alice pour une session donnée.



### 1h) Format de session existante

Session tag (8 octets)
Données chiffrées et MAC (voir section 3 ci-dessous)


### Format
Chiffré :

```

+----+----+----+----+----+----+----+----+
  |       Session Tag                     |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Section charge utile            +
  |       Données chiffrées ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Code d'authentification de message Poly1305 |
  +              (MAC)                    +
  |             16 octets                  |
  +----+----+----+----+----+----+----+----+

  Session Tag :: 8 octets, en clair

  Données chiffrées de la section charge utile :: données restantes moins 16 octets

  MAC :: Code d'authentification de message Poly1305, 16 octets

```


### Charge utile
La longueur chiffrée est le reste des données.
La longueur déchiffrée est 16 octets de moins que la longueur chiffrée.
Voir la section charge utile ci-dessous pour le format et les exigences.


KDF

```
Voir la section AEAD ci-dessous.

  // Paramètres AEAD pour la charge utile Existing Session
  k = La clé de session de 32 octets associée à ce session tag
  n = Le numéro de message N dans la chaîne actuelle, tel que récupéré à partir du session tag associé.
  ad = Le session tag, 8 octets
  ciphertext = ENCRYPT(k, n, charge utile, ad)
```



### 2) ECIES-X25519


Format : clés publiques et privées de 32 octets, little-endian.

Justification : Utilisé dans [NTCP2](/docs/specs/ntcp2/).



### 2a) Elligator2

Dans les échanges Noise standards, les messages initiaux d'échange dans chaque direction commencent par
des clés éphémères transmises en clair.
Étant donné que les clés X25519 valides sont distinguables de données aléatoires, un homme du milieu peut distinguer
ces messages des messages Existing Session qui commencent par des tags de session aléatoires.
Dans [NTCP2](/docs/specs/ntcp2/) ([Proposal 111](/proposals/111-ntcp-2/)), nous avons utilisé une fonction XOR à faible surcharge utilisant la clé statique hors bande pour obscurcir
la clé. Cependant, le modèle de menace ici est différent ; nous ne voulons pas permettre à un MITM
d'utiliser un moyen quelconque pour confirmer la destination du trafic, ou pour distinguer
les messages d'échange initiaux des messages Existing Session.

Par conséquent, [Elligator2](https://elligator.cr.yp.to/) est utilisé pour transformer les clés éphémères dans les messages New Session et New Session Reply
afin qu'elles soient indiscernables de chaînes aléatoires uniformes.



### Format

Clés publiques et privées de 32 octets.
Les clés encodées sont en little-endian.

Tel que défini dans [Elligator2](https://elligator.cr.yp.to/), les clés encodées sont indiscernables de 254 bits aléatoires.
Nous exigeons 256 bits aléatoires (32 octets). Par conséquent, l'encodage et le décodage sont
définis comme suit :

Encodage :

```

Définition ENCODE_ELG2()

  // Encoder tel que défini dans la spécification Elligator2
  encodedKey = encode(pubkey)
  // OU binaire avec 2 bits aléatoires dans le MSB
  randomByte = CSRNG(1)
  encodedKey[31] |= (randomByte & 0xc0)
```


Décodage :

```

Définition DECODE_ELG2()

  // Masquer 2 bits aléatoires du MSB
  encodedKey[31] &= 0x3f
  // Décoder tel que défini dans la spécification Elligator2
  pubkey = decode(encodedKey)
```




### Justification

Requis pour empêcher les OBEP et IBGW de classifier le trafic.


### Notes

Elligator2 double en moyenne le temps de génération de clé, car la moitié des clés privées
donnent des clés publiques inadaptées à l'encodage avec Elligator2.
De plus, le temps de génération de clé est illimité avec une distribution exponentielle,
car le générateur doit continuer à réessayer jusqu'à ce qu'une paire de clés adaptée soit trouvée.

Ce surcoût peut être géré en générant les clés à l'avance,
dans un thread séparé, pour maintenir un pool de clés adaptées.

Le générateur effectue la fonction ENCODE_ELG2() pour déterminer l'adaptabilité.
Par conséquent, le générateur devrait stocker le résultat de ENCODE_ELG2()
afin qu'il n'ait pas à être recalculé.

De plus, les clés inadaptées peuvent être ajoutées au pool de clés
utilisées pour [NTCP2](/docs/specs/ntcp2/), où Elligator2 n'est pas utilisé.
Les problèmes de sécurité liés à cela sont à déterminer.




### 3) AEAD (ChaChaPoly)

AEAD utilisant ChaCha20 et Poly1305, identique à [NTCP2](/docs/specs/ntcp2/).
Cela correspond à [RFC-7539](https://tools.ietf.org/html/rfc7539), qui est également
utilisé de manière similaire dans TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).



### Entrées New Session et New Session Reply

Entrées aux fonctions de chiffrement/déchiffrement
pour un bloc AEAD dans un message New Session :

```

k :: clé de chiffrement de 32 octets
       Voir les KDF New Session et New Session Reply ci-dessus.

  n :: nonce basé sur compteur, 12 octets.
       n = 0

  ad :: données associées, 32 octets.
        Le hachage SHA256 des données précédentes, tel que produit par mixHash()

  data :: données en clair, 0 ou plus d'oct
