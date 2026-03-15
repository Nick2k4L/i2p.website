---
title: "Nouvelles entrées netDB"
number: "123"
author: "zzz, str4d, orignal"
created: "2016-01-16"
lastupdated: "2020-07-18"
status: "Ouvrir"
thread: "http://zzz.i2p/topics/2051"
supercedes: "110, 120, 121, 122"
toc: true
---
## Statut

Certaines parties de cette proposition sont terminées et implémentées dans les versions 0.9.38 et 0.9.39.  
Les spécifications des Structures Communes, I2CP, I2NP et autres  
ont maintenant été mises à jour pour refléter les changements actuellement pris en charge.

Les parties terminées restent sujettes à de légères révisions.  
D'autres parties de cette proposition sont encore en cours de développement  
et sujettes à des révisions importantes.

La recherche de service (types 9 et 11) est une priorité faible,  
non planifiée, et pourrait être séparée en une proposition distincte.


## Aperçu

Il s'agit d'une mise à jour et d'une agrégation des 4 propositions suivantes :

- 110 LS2
- 120 Meta LS2 pour multihébergement massif
- 121 LS2 Chiffré
- 122 Recherche de service non authentifiée (anycast)

Ces propositions sont principalement indépendantes, mais par souci de cohérence, nous définissons et utilisons un  
format commun pour plusieurs d'entre elles.

Les propositions suivantes sont partiellement liées :

- 140 Multihébergement Invisible (incompatible avec cette proposition)
- 142 Nouveau Modèle de Cryptographie (pour une nouvelle cryptographie symétrique)
- 144 ECIES-X25519-AEAD-Ratchet
- 145 ECIES-P256
- 146 Red25519
- 148 EdDSA-BLAKE2b-Ed25519
- 149 B32 pour LS2 Chiffré
- 150 Protocole Garlic Farm
- 151 ECDSA Blinding


## Proposition

Cette proposition définit 5 nouveaux types DatabaseEntry et le processus pour  
les stocker et les récupérer depuis la base de données du réseau,  
ainsi que la méthode pour les signer et vérifier ces signatures.

### Objectifs

- Compatibilité ascendante
- LS2 utilisable avec le multihébergement ancien style
- Aucune nouvelle cryptographie ou primitive requise pour le support
- Maintenir la découplage entre crypto et signature ; supporter toutes les versions actuelles et futures
- Permettre des clés de signature hors ligne optionnelles
- Réduire la précision des horodatages pour limiter le fingerprinting
- Permettre une nouvelle cryptographie pour les destinations
- Permettre un multihébergement massif
- Corriger plusieurs problèmes avec le LS chiffré existant
- Option de masquage (blinding) pour réduire la visibilité par les floodfills
- Le chiffré supporte à la fois une clé unique et des clés multiples révocables
- Recherche de service pour faciliter la recherche de outproxies, le bootstrap DHT d'application,  
  et autres usages
- Ne rien casser qui dépend des hachages binaires de destination de 32 octets, par exemple bittorrent
- Ajouter de la flexibilité aux leasesets via des propriétés, comme nous en avons dans les routerinfos.
- Placer l'horodatage de publication et l'expiration variable dans l'en-tête, pour que cela fonctionne même  
  si le contenu est chiffré (ne pas dériver l'horodatage à partir de la location la plus ancienne)
- Tous les nouveaux types vivent dans le même espace DHT et aux mêmes emplacements que les leasesets existants,  
  afin que les utilisateurs puissent migrer du vieux LS vers LS2,  
  ou changer entre LS2, Meta et Chiffré,  
  sans changer la Destination ou son hachage.
- Une Destination existante peut être convertie pour utiliser des clés hors ligne,  
  ou revenir à des clés en ligne, sans changer la Destination ou son hachage.


### Non-objectifs / Hors-scope

- Nouvel algorithme de rotation DHT ou génération de nombres aléatoires partagés
- Le type de chiffrement spécifique et le schéma de chiffrement de bout en bout  
  utilisant ce nouveau type seraient dans une proposition séparée.  
  Aucune nouvelle cryptographie n'est spécifiée ou discutée ici.
- Nouveau chiffrement pour les RIs ou la construction de tunnels.  
  Ce serait dans une proposition séparée.
- Méthodes de chiffrement, transmission et réception des messages I2NP DLM / DSM / DSRM.  
  Non modifiées.
- Comment générer et gérer Meta, y compris la communication inter-routeurs, gestion, basculement et coordination.  
  Le support pourrait être ajouté à I2CP, ou i2pcontrol, ou un nouveau protocole.  
  Cela pourrait ou non être standardisé.
- Comment implémenter et gérer réellement des tunnels à expiration prolongée, ou annuler des tunnels existants.  
  C'est extrêmement difficile, et sans cela, vous ne pouvez pas avoir un arrêt gracieux raisonnable.
- Changements du modèle de menace
- Format de stockage hors ligne, ou méthodes pour stocker/récupérer/partager les données.
- Les détails d'implémentation ne sont pas discutés ici et sont laissés à chaque projet.



### Justification

LS2 ajoute des champs pour changer le type de chiffrement et pour les futurs changements de protocole.

LS2 Chiffré corrige plusieurs problèmes de sécurité du LS chiffré existant en  
utilisant un chiffrement asymétrique de l'ensemble des locations.

Meta LS2 fournit un multihébergement flexible, efficace, performant et à grande échelle.

Les enregistrements et listes de service fournissent des services anycast tels que la recherche de noms  
et le bootstrap DHT.


### Types de données NetDB

Les numéros de type sont utilisés dans les messages I2NP Database Lookup/Store.

La colonne « end-to-end » indique si les requêtes/réponses sont envoyées à une Destination dans un message Garlic.


Types existants :

| NetDB Data | Lookup Type | Store Type |
|------------|-------------|------------|
| any        | 0           | any        |
| LS         | 1           | 1          |
| RI         | 2           | 0          |
| exploratory| 3           | DSRM       |

Nouveaux types :

| NetDB Data     | Lookup Type | Store Type | Std. LS2 Header? | Sent end-to-end? |
|----------------|-------------|------------|------------------|------------------|
| LS2            | 1           | 3          | yes              | yes              |
| Encrypted LS2  | 1           | 5          | no               | no               |
| Meta LS2       | 1           | 7          | yes              | no               |
| Service Record | n/a         | 9          | yes              | no               |
| Service List   | 4           | 11         | no               | no               |



### Notes

- Les types de recherche sont actuellement les bits 3-2 du message Database Lookup.  
  Tout type supplémentaire nécessiterait l'utilisation du bit 4.

- Tous les types de stockage sont impairs car les bits supérieurs du champ type dans le message Database Store  
  sont ignorés par les anciens routeurs.  
  Nous préférons que l'analyse échoue comme un LS plutôt que comme un RI compressé.

- Le type doit-il être explicite, implicite ou ni l'un ni l'autre dans les données couvertes par la signature ?



### Processus de recherche / stockage

Les types 3, 5 et 7 peuvent être retournés en réponse à une recherche standard de leaseset (type 1).  
Le type 9 n'est jamais retourné en réponse à une recherche.  
Le type 11 est retourné en réponse à un nouveau type de recherche de service (type 11).

Seul le type 3 peut être envoyé dans un message Garlic client-à-client.



### Format

Les types 3, 7 et 9 ont un format commun ::

  En-tête standard LS2
  - tel que défini ci-dessous

  Partie spécifique au type
  - tel que défini ci-dessous pour chaque partie

  Signature standard LS2 :
  - Longueur implicite par le type de signature de la clé de signature

Le type 5 (Chiffré) ne commence pas par une Destination et a un  
format différent. Voir ci-dessous.

Le type 11 (Service List) est une agrégation de plusieurs Service Records et a un  
format différent. Voir ci-dessous.


### Considérations de confidentialité/sécurité

TBD



## En-tête standard LS2

Les types 3, 7 et 9 utilisent l'en-tête standard LS2, spécifié ci-dessous :


### Format

```
En-tête standard LS2 :
  - Type (1 octet)
    Pas réellement dans l'en-tête, mais fait partie des données couvertes par la signature.
    À prendre depuis le champ du message Database Store.
  - Destination (387+ octets)
  - Horodatage de publication (4 octets, big endian, secondes depuis l'époque, dépassement en 2106)
  - Expiration (2 octets, big endian) (décalage depuis l'horodatage de publication en secondes, max 18,2 heures)
  - Flags (2 octets)
    Ordre des bits : 15 14 ... 3 2 1 0
    Bit 0 : Si 0, pas de clés hors ligne ; si 1, clés hors ligne
    Bit 1 : Si 0, un leaseset publié standard.
           Si 1, un leaseset non publié. Ne doit pas être diffusé, publié ou
           envoyé en réponse à une requête. Si ce leaseset expire, ne pas interroger le
           netdb pour un nouveau, sauf si le bit 2 est activé.
    Bit 2 : Si 0, un leaseset publié standard.
           Si 1, ce leaseset non chiffré sera masqué et chiffré lors de la publication.
           Si ce leaseset expire, interroger l'emplacement masqué dans le netdb pour un nouveau.
           Si ce bit est activé à 1, activer également le bit 1 à 1.
           À partir de la version 0.9.42.
    Bits 3-15 : à 0 pour compatibilité avec les usages futurs
  - Si le flag indique des clés hors ligne, la section de signature hors ligne :
    Horodatage d'expiration (4 octets, big endian, secondes depuis l'époque, dépassement en 2106)
    Type de signature temporaire (2 octets, big endian)
    Clé publique de signature temporaire (longueur implicite par le type de signature)
    Signature de l'horodatage d'expiration, du type de signature temporaire et de la clé publique,
    par la clé publique de destination,
    longueur implicite par le type de signature de la clé publique de destination.
    Cette section peut, et devrait, être générée hors ligne.
```

### Justification

- Non publié/publié : À utiliser lors de l'envoi d'un stockage de base de données de bout en bout,  
  le routeur émetteur peut souhaiter indiquer que ce leaseset ne doit pas être  
  envoyé à d'autres. Nous utilisons actuellement des heuristiques pour maintenir cet état.

- Publié : Remplace la logique complexe nécessaire pour déterminer la « version » du  
  leaseset. Actuellement, la version est l'expiration de la location expirant en dernier, et un routeur de publication doit incrémenter cette expiration d'au moins 1 ms lorsqu'il  
  publie un leaseset qui supprime uniquement une ancienne location.

- Expiration : Permet à l'expiration d'une entrée netdb d'être antérieure à celle de  
  sa location expirant en dernier. Peut ne pas être utile pour LS2, où les leasesets  
  sont censés rester avec une expiration maximale de 11 minutes, mais  
  pour d'autres nouveaux types, c'est nécessaire (voir Meta LS et Service Record ci-dessous).

- Les clés hors ligne sont optionnelles, pour réduire la complexité initiale/requise de l'implémentation.


### Problèmes

- Pourrait réduire encore plus la précision de l'horodatage (10 minutes ?) mais devrait ajouter  
  un numéro de version. Cela pourrait casser le multihébergement, sauf si nous avons un chiffrement préservant l'ordre ?  
  Probablement impossible sans horodatages du tout.

- Alternative : horodatage de 3 octets (époque / 10 minutes), version de 1 octet, expiration de 2 octets

- Le type est-il explicite ou implicite dans les données / signature ? Constantes « Domaine » pour la signature ?


### Notes

- Les routeurs ne devraient pas publier un LS plus d'une fois par seconde.  
  S'ils le font, ils doivent artificiellement incrémenter l'horodatage de publication de 1  
  par rapport au LS précédemment publié.

- Les implémentations de routeurs pourraient mettre en cache les clés temporaires et la signature pour  
  éviter la vérification à chaque fois. En particulier, les floodfills et les routeurs aux  
  deux extrémités de connexions longues pourraient bénéficier de cela.

- Les clés et signature hors ligne ne conviennent que pour les destinations à longue durée de vie,  
  c'est-à-dire les serveurs, pas les clients.



## Nouveaux types DatabaseEntry


### LeaseSet 2

Changements par rapport au LeaseSet existant :

- Ajout de l'horodatage de publication, de l'horodatage d'expiration, des flags et des propriétés
- Ajout du type de chiffrement
- Suppression de la clé de révocation

Recherche avec  
    Flag LS standard (1)  
Stockage avec  
    Type LS2 standard (3)  
Stockage à  
    Hachage de la destination  
    Ce hachage est ensuite utilisé pour générer la « clé de routage » quotidienne, comme dans LS1  
Expiration typique  
    10 minutes, comme dans un LS régulier.  
Publié par  
    Destination

### Format

```
En-tête standard LS2 tel que spécifié ci-dessus

  Partie spécifique au type LS2 standard
  - Propriétés (Mapping tel que spécifié dans la spécification des structures communes, 2 octets nuls si aucune)
  - Nombre de sections de clé à suivre (1 octet, max à déterminer)
  - Sections de clé :
    - Type de chiffrement (2 octets, big endian)
    - Longueur de la clé de chiffrement (2 octets, big endian)
      C'est explicite, afin que les floodfills puissent analyser LS2 avec des types de chiffrement inconnus.
    - Clé de chiffrement (nombre d'octets spécifié)
  - Nombre de lease2s (1 octet)
  - Lease2s (40 octets chacun)
    Ce sont des locations, mais avec une expiration de 4 octets au lieu de 8 octets,
    secondes depuis l'époque (dépassement en 2106)

  Signature standard LS2 :
  - Signature
    Si le flag indique des clés hors ligne, celle-ci est signée par la clé publique temporaire,
    sinon, par la clé publique de destination
    Longueur implicite par le type de signature de la clé de signature
    La signature couvre tout ce qui précède.
```


### Justification

- Propriétés : Extension et flexibilité futures.  
  Placées en premier au cas où nécessaires pour l'analyse des données restantes.

- Plusieurs paires type de chiffrement/clé publique sont  
  destinées à faciliter la transition vers de nouveaux types de chiffrement. L'autre façon de faire  
  est de publier plusieurs leasesets, éventuellement en utilisant les mêmes tunnels,  
  comme nous le faisons actuellement pour les destinations DSA et EdDSA.  
  L'identification du type de chiffrement entrant sur un tunnel  
  peut être faite avec le mécanisme existant de session tag,  
  et/ou par déchiffrement d'essai avec chaque clé. La longueur des messages entrants  
  peut également fournir un indice.

### Discussion

Cette proposition continue d'utiliser la clé publique dans le leaseset comme clé de chiffrement de bout en bout, et laisse le champ de clé publique dans la  
Destination inutilisé, comme actuellement. Le type de chiffrement n'est pas spécifié  
dans le certificat de clé de Destination, il restera 0.

Une alternative rejetée consiste à spécifier le type de chiffrement dans le certificat de clé de Destination,  
utiliser la clé publique dans la Destination, et ne pas utiliser la clé publique  
dans le leaseset. Nous n'avons pas l'intention de faire cela.

Avantages de LS2 :

- L'emplacement de la clé publique réelle ne change pas.
- Le type de chiffrement ou la clé publique peut changer sans changer la Destination.
- Supprime le champ de révocation inutilisé
- Compatibilité de base avec d'autres types DatabaseEntry dans cette proposition
- Permet plusieurs types de chiffrement

Inconvénients de LS2 :

- L'emplacement de la clé publique et du type de chiffrement diffère de RouterInfo
- Maintient la clé publique inutilisée dans le leaseset
- Nécessite une implémentation à travers le réseau ; dans l'alternative, des types de chiffrement expérimentaux peuvent être utilisés, si autorisés par les floodfills  
  (mais voir les propositions connexes 136 et 137 concernant le support des types de signature expérimentaux).  
  La proposition alternative pourrait être plus facile à implémenter et tester pour des types de chiffrement expérimentaux.


### Nouveaux problèmes de chiffrement

Certains points sont hors-scope pour cette proposition,  
mais nous mettons ici des notes car nous n'avons pas encore  
de proposition de chiffrement séparée.  
Voir aussi les propositions ECIES 144 et 145.

- Le type de chiffrement représente la combinaison  
  de courbe, longueur de clé et schéma de bout en bout,  
  incluant KDF et MAC, le cas échéant.

- Nous avons inclus un champ de longueur de clé, afin que le LS2 soit  
  analysable et vérifiable par le floodfill même pour des types de chiffrement inconnus.

- Le premier nouveau type de chiffrement proposé sera  
  probablement ECIES/X25519. Comment il est utilisé de bout en bout  
  (soit une version légèrement modifiée d'ElGamal/AES+SessionTag  
  soit quelque chose de complètement nouveau, par exemple ChaCha/Poly) sera spécifié  
  dans une ou plusieurs propositions séparées.  
  Voir aussi les propositions ECIES 144 et 145.


### Notes

- L'expiration de 8 octets dans les locations passe à 4 octets.

- Si nous implémentons jamais la révocation, nous pouvons le faire avec un champ d'expiration à zéro,  
  ou des locations nulles, ou les deux. Pas besoin d'une clé de révocation séparée.

- Les clés de chiffrement sont dans l'ordre de préférence du serveur, la plus préférée en premier.  
  Le comportement par défaut du client est de sélectionner la première clé avec  
  un type de chiffrement pris en charge. Les clients peuvent utiliser d'autres algorithmes de sélection  
  basés sur le support du chiffrement, les performances relatives et d'autres facteurs.


### LS2 Chiffré

Objectifs :

- Ajouter le masquage (blinding)
- Permettre plusieurs types de signature
- Ne pas nécessiter de nouvelles primitives cryptographiques
- Chiffrer éventuellement à chaque destinataire, révocable
- Supporter le chiffrement de LS2 standard et Meta LS2 uniquement

Le LS2 chiffré n'est jamais envoyé dans un message garlic de bout en bout.  
Utilisez le LS2 standard comme ci-dessus.

Changements par rapport au LeaseSet chiffré existant :

- Chiffrer l'ensemble pour la sécurité
- Chiffrer de manière sécurisée, pas seulement avec AES.
- Chiffrer à chaque destinataire

Recherche avec  
    Flag LS standard (1)  
Stockage avec  
    Type LS2 chiffré (5)  
Stockage à  
    Hachage du type de signature masquée et de la clé publique masquée  
    Type de signature sur 2 octets (big endian, par exemple 0x000b) || clé publique masquée  
    Ce hachage est ensuite utilisé pour générer la « clé de routage » quotidienne, comme dans LS1  
Expiration typique  
    10 minutes, comme dans un LS régulier, ou heures, comme dans un meta LS.  
Publié par  
    Destination


### Définitions

Nous définissons les fonctions suivantes correspondant aux blocs cryptographiques utilisés  
pour le LS2 chiffré :

CSRNG(n)  
    sortie de n octets d'un générateur de nombres aléatoires cryptographiquement sécurisé.

    En plus de l'exigence que CSRNG soit cryptographiquement sécurisé (et donc  
    adapté à la génération de matériel de clé), il DOIT être sûr  
    qu'une sortie de n octets puisse être utilisée comme matériel de clé lorsque les séquences d'octets immédiatement  
    précédentes et suivantes sont exposées sur le réseau (comme dans un sel, ou un remplissage chiffré). Les implémentations qui s'appuient sur une source potentiellement non fiable doivent hacher  
    toute sortie qui doit être exposée sur le réseau. Voir [PRNG references](http://projectbullrun.org/dual-ec/ext-rand.html) et [Tor dev discussion](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html).

H(p, d)  
    fonction de hachage SHA-256 prenant une chaîne de personnalisation p et des données d, et  
    produisant une sortie de 32 octets.

    Utiliser SHA-256 comme suit ::

        H(p, d) := SHA-256(p || d)

STREAM  
    le chiffrement en flux ChaCha20 tel que spécifié dans [RFC 7539 Section 2.4](https://tools.ietf.org/html/rfc7539#section-2.4), avec le compteur initial  
    défini à 1. S_KEY_LEN = 32 et S_IV_LEN = 12.

    ENCRYPT(k, iv, plaintext)  
        Chiffre le texte en clair en utilisant la clé de chiffrement k, et le nonce iv qui DOIT être unique pour  
        la clé k. Renvoie un texte chiffré de la même taille que le texte en clair.

        Le texte chiffré entier doit être indiscernable d'un aléatoire si la clé est secrète.

    DECRYPT(k, iv, ciphertext)  
        Déchiffre le texte chiffré en utilisant la clé de chiffrement k, et le nonce iv. Renvoie le texte en clair.


SIG  
    le schéma de signature RedDSA (correspondant au SigType 11) avec masquage de clé.  
    Il possède les fonctions suivantes :

    DERIVE_PUBLIC(privkey)  
        Renvoie la clé publique correspondant à la clé privée donnée.

    SIGN(privkey, m)  
        Renvoie une signature par la clé privée privkey sur le message donné m.

    VERIFY(pubkey, m, sig)  
        Vérifie la signature sig par rapport à la clé publique pubkey et au message m. Renvoie  
        vrai si la signature est valide, faux sinon.

    Il doit également supporter les opérations de masquage de clé suivantes :

    GENERATE_ALPHA(data, secret)  
        Génère alpha pour ceux qui connaissent les données et un secret optionnel.  
        Le résultat doit être identiquement distribué que les clés privées.

    BLIND_PRIVKEY(privkey, alpha)  
        Masque une clé privée, en utilisant un alpha secret.

    BLIND_PUBKEY(pubkey, alpha)  
        Masque une clé publique, en utilisant un alpha secret.  
        Pour une paire de clés donnée (privkey, pubkey), la relation suivante tient ::

            BLIND_PUBKEY(pubkey, alpha) ==
            DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))

DH  
    système d'accord de clé publique X25519. Clés privées de 32 octets, clés publiques de 32  
    octets, produit des sorties de 32 octets. Il possède les fonctions suivantes :

    GENERATE_PRIVATE()  
        Génère une nouvelle clé privée.

    DERIVE_PUBLIC(privkey)  
        Renvoie la clé publique correspondant à la clé privée donnée.

    DH(privkey, pubkey)  
        Génère un secret partagé à partir des clés privée et publique données.

HKDF(salt, ikm, info, n)  
    une fonction de dérivation de clé cryptographique qui prend un matériel de clé d'entrée ikm (qui  
    devrait avoir une bonne entropie mais n'est pas requis d'être une chaîne uniformément aléatoire), un sel  
    de longueur 32 octets, et une valeur 'info' spécifique au contexte, et produit une sortie  
    de n octets adaptée à une utilisation comme matériel de clé.

    Utiliser HKDF tel que spécifié dans [RFC 5869](https://tools.ietf.org/html/rfc5869), en utilisant la fonction de hachage HMAC SHA-256  
    tel que spécifié dans [RFC 2104](https://tools.ietf.org/html/rfc2104). Cela signifie que SALT_LEN est au maximum 32 octets.


### Format

Le format du LS2 chiffré consiste en trois couches imbriquées :

- Une couche externe contenant les informations en clair nécessaires pour le stockage et la récupération.
- Une couche intermédiaire qui gère l'authentification du client.
- Une couche interne qui contient les données LS2 réelles.

Le format global ressemble à ::

    Données couche 0 + Enc(données couche 1 + Enc(données couche 2)) + Signature

Notez que le LS2 chiffré est masqué. La Destination n'est pas dans l'en-tête.  
L'emplacement de stockage DHT est SHA-256(type de signature || clé publique masquée), et tourne quotidiennement.

N'utilise PAS l'en-tête LS2 standard spécifié ci-dessus.

#### Couche 0 (externe)
Type  
    1 octet

    Pas réellement dans l'en-tête, mais fait partie des données couvertes par la signature.  
    À prendre depuis le champ du message Database Store.

Type de signature de la clé publique masquée  
    2 octets, big endian  
    Ce sera toujours le type 11, identifiant une clé masquée Red25519.

Clé publique masquée  
    Longueur implicite par le type de signature

Horodatage de publication  
    4 octets, big endian

    Secondes depuis l'époque, dépassement en 2106

Expiration  
    2 octets, big endian

    Décalage depuis l'horodatage de publication en secondes, max 18,2 heures

Flags  
    2 octets

    Ordre des bits : 15 14 ... 3 2 1 0

    Bit 0 : Si 0, pas de clés hors ligne ; si 1, clés hors ligne

    Autres bits : à 0 pour compatibilité avec les usages futurs

Données de clé temporaire  
    Présentes si le flag indique des clés hors ligne

    Horodatage d'expiration  
        4 octets, big endian

        Secondes depuis l'époque, dépassement en 2106

    Type de signature temporaire  
        2 octets, big endian

    Clé publique de signature temporaire  
        Longueur implicite par le type de signature

    Signature  
        Longueur implicite par le type de signature de la clé publique masquée

        Sur l'horodatage d'expiration, le type de signature temporaire et la clé publique temporaire.

        Vérifiée avec la clé publique masquée.

lenOuterCiphertext  
    2 octets, big endian

outerCiphertext  
    lenOuterCiphertext octets

    Données couche 1 chiffrées. Voir ci-dessous pour les algorithmes de dérivation de clé et de chiffrement.

Signature  
    Longueur implicite par le type de signature de la clé de signature utilisée

    La signature couvre tout ce qui précède.

    Si le flag indique des clés hors ligne, la signature est vérifiée avec la clé publique temporaire.  
    Sinon, la signature est vérifiée avec la clé publique masquée.


#### Couche 1 (intermédiaire)
Flags  
    1 octet
    
    Ordre des bits : 76543210

    Bit 0 : 0 pour tout le monde, 1 pour par-client, section d'auth à suivre

    Bits 3-1 : Schéma d'authentification, seulement si le bit 0 est à 1 pour par-client, sinon 000  
              000 : authentification client DH (ou aucune authentification par-client)  
              001 : authentification client PSK

    Bits 7-4 : Inutilisés, à 0 pour compatibilité future

Données d'auth DH client  
    Présentes si le bit 0 du flag est à 1 et les bits 3-1 à 000.

    ephemeralPublicKey  
        32 octets

    clients  
        2 octets, big endian

        Nombre d'entrées authClient à suivre, 40 octets chacune

    authClient  
        Données d'autorisation pour un seul client.  
        Voir ci-dessous pour l'algorithme d'autorisation par-client.

        clientID_i  
            8 octets

        clientCookie_i  
            32 octets

Données d'auth PSK client  
    Présentes si le bit 0 du flag est à 1 et les bits 3-1 à 001.

    authSalt  
        32 octets

    clients  
        2 octets, big endian

        Nombre d'entrées authClient à suivre, 40 octets chacune

    authClient  
        Données d'autorisation pour un seul client.  
        Voir ci-dessous pour l'algorithme d'autorisation par-client.

        clientID_i  
            8 octets

        clientCookie_i  
            32 octets


innerCiphertext  
    Longueur implicite par lenOuterCiphertext (tout ce qui reste)

    Données couche 2 chiffrées. Voir ci-dessous pour les algorithmes de dérivation de clé et de chiffrement.


#### Couche 2 (interne)
Type  
    1 octet

    Soit 3 (LS2) soit 7 (Meta LS2)

Données  
    Données LeaseSet2 pour le type donné.

    Inclut l'en-tête et la signature.


### Dérivation de clé masquée

Nous utilisons le schéma suivant pour le masquage de clé,  
basé sur Ed25519 et [ZCash RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf).  
Les signatures Re25519 sont sur la courbe Ed25519, en utilisant SHA-512 pour le hachage.

Nous n'utilisons pas [Tor's rend-spec-v3.txt appendix A.2](https://spec.torproject.org/rend-spec-v3),  
qui a des objectifs de conception similaires, car ses clés publiques masquées  
peuvent être en dehors du sous-groupe d'ordre premier, avec des implications de sécurité inconnues.


#### Objectifs

- La clé publique de signature dans la destination non masquée doit être  
  Ed25519 (type de signature 7) ou Red25519 (type de signature 11) ;  
  aucun autre type de signature n'est supporté
- Si la clé publique de signature est hors ligne, la clé publique de signature temporaire doit aussi être Ed25519
- Le masquage est computationnellement simple
- Utiliser des primitives cryptographiques existantes
- Les clés publiques masquées ne peuvent pas être démascarquées
- Les clés publiques masquées doivent être sur la courbe Ed25519 et dans le sous-groupe d'ordre premier
- Doit connaître la clé publique de signature de la destination  
  (destination complète non requise) pour dériver la clé publique masquée
- Optionnellement fournir un secret supplémentaire requis pour dériver la clé publique masquée


#### Sécurité

La sécurité d'un schéma de masquage exige que la  
distribution d'alpha soit la même que celle des clés privées non masquées.  
Cependant, lorsque nous masquons une clé privée Ed25519 (type de signature 7)  
vers une clé privée Red25519 (type de signature 11), la distribution est différente.  
Pour répondre aux exigences de [zcash section 4.1.6.1](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf),  
Red25519 (type de signature 11) devrait être utilisé pour les clés non masquées également, afin que  
« la combinaison d'une clé publique ré-randomisée et de signature(s)  
sous cette clé ne révèle pas la clé à partir de laquelle elle a été ré-randomisée ».  
Nous autorisons le type 7 pour les destinations existantes, mais recommandons  
le type 11 pour les nouvelles destinations qui seront chiffrées.



#### Définitions

B  
    Le point de base Ed25519 (générateur) 2^255 - 19 tel que dans [Ed25519](http://cr.yp.to/papers.html#ed25519)

L  
    L'ordre Ed25519 2^252 + 27742317777372353535851937790883648493  
    tel que dans [Ed25519](http://cr.yp.to/papers.html#ed25519)

DERIVE_PUBLIC(a)  
    Convertir une clé privée en publique, comme dans Ed25519 (multiplier par G)

alpha  
    Un nombre aléatoire de 32 octets connu de ceux qui connaissent la destination.

GENERATE_ALPHA(destination, date, secret)  
    Génère alpha pour la date actuelle, pour ceux qui connaissent la destination et le secret.  
    Le résultat doit être identiquement distribué que les clés privées Ed25519.

a  
    La clé privée de signature EdDSA ou RedDSA non masquée de 32 octets utilisée pour signer la destination

A  
    La clé publique de signature EdDSA ou RedDSA non masquée de 32 octets dans la destination,  
    = DERIVE_PUBLIC(a), comme dans Ed25519

a'  
    La clé privée de signature EdDSA masquée de 32 octets utilisée pour signer le leaseset chiffré  
    C'est une clé privée EdDSA valide.

A'  
    La clé publique de signature EdDSA masquée de 32 octets dans la Destination,  
    peut être générée avec DERIVE_PUBLIC(a'), ou à partir de A et alpha.  
    C'est une clé publique EdDSA valide, sur la courbe et dans le sous-groupe d'ordre premier.

LEOS2IP(x)  
    Inverser l'ordre des octets d'entrée en little-endian

H*(x)  
    32 octets = (LEOS2IP(SHA512(x))) mod B, identique au hachage-et-réduction dans Ed25519


#### Calculs de masquage

Un nouveau secret alpha et des clés masquées doivent être générés chaque jour (UTC).  
Le secret alpha et les clés masquées sont calculés comme suit.

GENERATE_ALPHA(destination, date, secret), pour toutes les parties :

```text
// GENERATE_ALPHA(destination, date, secret)

  // secret est optionnel, sinon de longueur nulle
  A = clé publique de signature de la destination
  stA = type de signature de A, 2 octets big endian (0x0007 ou 0x000b)
  stA' = type de signature de la clé publique masquée A', 2 octets big endian (0x000b)
  keydata = A || stA || stA'
  datestring = 8 octets ASCII YYYYMMDD de la date actuelle UTC
  secret = chaîne encodée UTF-8
  seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || secret, "i2pblinding1", 64)
  // traiter seed comme une valeur little-endian de 64 octets
  alpha = seed mod L
```

BLIND_PRIVKEY(), pour le propriétaire publiant le leaseset :

```text
// BLIND_PRIVKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  // Si pour une clé privée Ed25519 (type 7)
  seed = clé privée de signature de la destination
  a = moitié gauche de SHA512(seed) et clampée comme d'habitude pour Ed25519
  // sinon, pour une clé privée Red25519 (type 11)
  a = clé privée de signature de la destination
  // Addition utilisant l'arithmétique scalaire
  clé privée de signature masquée = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
  clé publique de signature masquée = A' = DERIVE_PUBLIC(a')
```

BLIND_PUBKEY(), pour les clients récupérant le leaseset :

```text
// BLIND_PUBKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  A = clé publique de signature de la destination
  // Addition utilisant les éléments de groupe (points sur la courbe)
  clé publique masquée = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```

Les deux méthodes de calcul de A' donnent le même résultat, comme requis.



#### Signature

Le leaseset non masqué est signé par la clé privée de signature Ed25519 ou Red25519 non masquée  
et vérifié avec la clé publique de signature Ed25519 ou Red25519 non masquée (types de signature 7 ou 11) comme d'habitude.

Si la clé publique de signature est hors ligne,  
le leaseset non masqué est signé par la clé privée de signature temporaire Ed25519 ou Red25519 non masquée  
et vérifié avec la clé publique de signature temporaire Ed25519 ou Red25519 non masquée (types de signature 7 ou 11) comme d'habitude.  
Voir ci-dessous pour des notes supplémentaires sur les clés hors ligne pour les leasesets chiffrés.

Pour la signature du leaseset chiffré, nous utilisons Red25519, basé sur [RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)  
pour signer et vérifier avec des clés masquées.  
Les signatures Red25519 sont sur la courbe Ed25519, en utilisant SHA-512 pour le hachage.

Red25519 est identique à Ed25519 standard sauf spécifié ci-dessous.


#### Calculs de signature/vérification

La partie externe du leaseset chiffré utilise des clés et signatures Red25519.

Red25519 est presque identique à Ed25519. Deux différences :

Les clés privées Red25519 sont générées à partir de nombres aléatoires puis doivent être réduites mod L, où L est défini ci-dessus.  
Les clés privées Ed25519 sont générées à partir de nombres aléatoires puis « clampées » en utilisant  
un masquage bit à bit sur les octets 0 et 31. Cela n'est pas fait pour Red25519.  
Les fonctions GENERATE_ALPHA() et BLIND_PRIVKEY() définies ci-dessus génèrent des clés privées Red25519 correctes en utilisant mod L.

Dans Red25519, le calcul de r pour la signature utilise des données aléatoires supplémentaires,  
et utilise la valeur de la clé publique plutôt que le hachage de la clé privée.  
À cause des données aléatoires, chaque signature Red25519 est différente, même  
en signant les mêmes données avec la même clé.

Signature :

```text
T = 80 octets aléatoires
  r = H*(T || publickey || message)
  // le reste est identique à Ed25519
```

Vérification :

```text
// identique à Ed25519
```



### Chiffrement et traitement

#### Dérivation des sous-identifiants
Dans le cadre du processus de masquage, nous devons nous assurer qu'un LS2 chiffré ne peut être  
déchiffré que par quelqu'un qui connaît la clé publique de signature de la Destination correspondante.  
La Destination complète n'est pas requise.  
Pour y parvenir, nous dérivons un identifiant à partir de la clé publique de signature :

```text
A = clé publique de signature de la destination
  stA = type de signature de A, 2 octets big endian (0x0007 ou 0x000b)
  stA' = type de signature de A', 2 octets big endian (0x000b)
  keydata = A || stA || stA'
  credential = H("credential", keydata)
```

La chaîne de personnalisation garantit que l'identifiant ne collisionne avec aucun hachage utilisé  
comme clé de recherche DHT, comme le hachage de Destination brut.

Pour une clé masquée donnée, nous pouvons ensuite dériver un sous-identifiant :

```text
subcredential = H("subcredential", credential || blindedPublicKey)
```

Le sous-identifiant est inclus dans les processus de dérivation de clé ci-dessous, ce qui lie ces  
clés à la connaissance de la clé publique de signature de la Destination.

#### Chiffrement couche 1
D'abord, l'entrée pour le processus de dérivation de clé est préparée :

```text
outerInput = subcredential || publishedTimestamp
```

Ensuite, un sel aléatoire est généré :

```text
outerSalt = CSRNG(32)
```

Puis la clé utilisée pour chiffrer la couche 1 est dérivée :

```text
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
  outerKey = keys[0:31]
  outerIV = keys[32:43]
```

Enfin, le texte clair de la couche 1 est chiffré et sérialisé :

```text
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```

#### Déchiffrement couche 1
Le sel est analysé à partir du texte chiffré de la couche 1 :

```text
outerSalt = outerCiphertext[0:31]
```

Puis la clé utilisée pour chiffrer la couche 1 est dérivée :

```text
outerInput = subcredential || publishedTimestamp
  keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
  outerKey = keys[0:31]
  outerIV = keys[32:43]
```

Enfin, le texte chiffré de la couche 1 est déchiffré :

```text
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```

#### Chiffrement couche 2
Lorsque l'autorisation client est activée, ``authCookie`` est calculé comme décrit ci-dessous.  
Lorsque l'autorisation client est désactivée, ``authCookie`` est un tableau d'octets de longueur nulle.

Le chiffrement procède de manière similaire à la couche 1 :

```text
innerInput = authCookie || subcredential || publishedTimestamp
  innerSalt = CSRNG(32)
  keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
  innerKey = keys[0:31]
  innerIV = keys[32:43]
  innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```

#### Déchiffrement couche 2
Lorsque l'autorisation client est activée, ``authCookie`` est calculé comme décrit ci-dessous.  
Lorsque l'autorisation client est désactivée, ``authCookie`` est un tableau d'octets de longueur nulle.

Le déchiffrement procède de manière similaire à la couche 1 :

```text
innerInput = authCookie || subcredential || publishedTimestamp
  innerSalt = innerCiphertext[0:31]
  keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
  innerKey = keys[0:31]
  innerIV = keys[32:43]
  innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```


### Autorisation par-client

Lorsque l'autorisation client est activée pour une Destination, le serveur maintient une liste de  
clients qu'il autorise à déchiffrer les données du LS2 chiffré. Les données stockées par-client  
dépendent du mécanisme d'autorisation, et incluent une forme de matériel de clé que chaque  
client génère et envoie au serveur via un mécanisme sécurisé hors bande.

Il existe deux alternatives pour implémenter l'autorisation par-client :

#### Autorisation client DH
Chaque client génère une paire de clés DH ``[csk_i, cpk_i]``, et envoie la clé publique ``cpk_i``  
au serveur.

Traitement du serveur  
^^^^^^^^^^^^^^^^^
Le serveur génère un nouveau ``authCookie`` et une paire de clés DH éphémère :

```text
authCookie = CSRNG(32)
  esk = GENERATE_PRIVATE()
  epk = DERIVE_PUBLIC(esk)
```

Puis pour chaque client autorisé, le serveur chiffre ``authCookie`` à sa clé publique :

```text
sharedSecret = DH(esk, cpk_i)
  authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
  okm = HKDF(epk, authInput, "ELS2_XCA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
  clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```

Le serveur place chaque tuple ``[clientID_i, clientCookie_i]`` dans la couche 1 du  
LS2 chiffré, avec ``epk``.

Traitement du client  
^^^^^^^^^^^^^^^^^
Le client utilise sa clé privée pour dériver son identifiant client attendu ``clientID_i``,  
la clé de chiffrement ``clientKey_i``, et le vecteur d'initialisation ``clientIV_i`` :

```text
sharedSecret = DH(csk_i, epk)
  authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
  okm = HKDF(epk, authInput, "ELS2_XCA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
```

Puis le client recherche dans les données d'autorisation de la couche 1 une entrée contenant  
``clientID_i``. Si une entrée correspondante existe, le client la déchiffre pour obtenir  
``authCookie`` :

```text
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```

#### Autorisation client par clé pré-partagée (PSK)
Chaque client génère une clé secrète de 32 octets ``psk_i``, et l'envoie au serveur.  
Alternativement, le serveur peut générer la clé secrète, et l'envoyer à un ou plusieurs clients.


Traitement du serveur  
^^^^^^^^^^^^^^^^^
Le serveur génère un nouveau ``authCookie`` et un sel :

```text
authCookie = CSRNG(32)
  authSalt = CSRNG(32)
```

Puis pour chaque client autorisé, le serveur chiffre ``authCookie`` à sa clé pré-partagée :

```text
authInput = psk_i || subcredential || publishedTimestamp
  okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
  clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```

Le serveur place chaque tuple ``[clientID_i, clientCookie_i]`` dans la couche 1 du  
LS2 chiffré, avec ``authSalt``.

Traitement du client  
^^^^^^^^^^^^^^^^^
Le client utilise sa clé pré-partagée pour dériver son identifiant client attendu ``clientID_i``,  
la clé de chiffrement ``clientKey_i``, et le vecteur d'initialisation ``clientIV_i`` :

```text
authInput = psk_i || subcredential || publishedTimestamp
  okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
```

Puis le client recherche dans les données d'autorisation de la couche 1 une entrée contenant  
``clientID_i``. Si une entrée correspondante existe, le client la déchiffre pour obtenir  
``authCookie`` :

```text
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```

#### Considérations de sécurité
Les deux mécanismes d'autorisation client ci-dessus fournissent une confidentialité pour l'appartenance aux clients.  
Une entité qui connaît uniquement la Destination peut voir combien de clients sont abonnés à tout  
moment, mais ne peut pas suivre quels clients sont ajoutés ou révoqués.

Les serveurs DEVRAIENT randomiser l'ordre des clients chaque fois qu'ils génèrent un LS2 chiffré, pour  
empêcher les clients de connaître leur position dans la liste et d'inférer quand d'autres clients ont été ajoutés ou révoqués.

Un serveur PEUT choisir de cacher le nombre de clients abonnés en insérant des entrées aléatoires dans la liste des données d'autorisation.

Avantages de l'autorisation client DH  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- La sécurité du schéma ne dépend pas uniquement de l'échange hors bande du matériel de clé client.  
  La clé privée du client n'a jamais besoin de quitter son appareil, donc un  
  adversaire capable d'intercepter l'échange hors bande, mais incapable de casser l'algorithme DH,  
  ne peut pas déchiffrer le LS2 chiffré, ni déterminer combien de temps le client a accès.

Inconvénients de l'autorisation client DH  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Nécessite N + 1 opérations DH côté serveur pour N clients.
- Nécessite une opération DH côté client.
- Nécessite que le client génère la clé secrète.

Avantages de l'autorisation client PSK  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Ne nécessite aucune opération DH.
- Permet au serveur de générer la clé secrète.
- Permet au serveur de partager la même clé avec plusieurs clients, si souhaité.

Inconvénients de l'autorisation client PSK  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- La sécurité du schéma dépend critique de l'échange hors bande du matériel de clé client.  
  Un adversaire qui intercepte l'échange pour un client particulier peut déchiffrer  
  tout LS2 chiffré ultérieur pour lequel ce client est autorisé, ainsi que déterminer  
  quand l'accès du client est révoqué.


### LS chiffré avec adresses Base 32

Voir proposition 149.

Vous ne pouvez pas utiliser un LS2 chiffré pour bittorrent, à cause des réponses compactes d'annonce qui font 32 octets.  
Les 32 octets contiennent uniquement le hachage. Il n'y a pas de place pour indiquer que le  
leaseset est chiffré, ou les types de signature.



### LS chiffré avec clés hors ligne

Pour les leasesets chiffrés avec clés hors ligne, les clés privées masquées doivent également être générées hors ligne,  
une pour chaque jour.

Comme le bloc de signature hors ligne optionnel est dans la partie en clair du leaseset chiffré,  
n'importe qui scrapant les floodfills pourrait l'utiliser pour suivre le leaseset (mais pas le déchiffrer)  
sur plusieurs jours.  
Pour l'éviter, le propriétaire des clés devrait générer de nouvelles clés temporaires  
pour chaque jour également.  
Les clés temporaires et masquées peuvent être générées à l'avance, et livrées au routeur  
par lots.

Il n'y a pas de format de fichier défini dans cette proposition pour empaqueter plusieurs clés temporaires et  
masquées et les fournir au client ou au routeur.  
Il n'y a pas d'amélioration du protocole I2CP définie dans cette proposition pour supporter  
les leasesets chiffrés avec clés hors ligne.



### Notes

- Un service utilisant des leasesets chiffrés publierait la version chiffrée aux  
  floodfills. Cependant, par souci d'efficacité, il enverrait des leasesets non chiffrés aux  
  clients dans le message garlic encapsulé, une fois authentifié (via liste blanche, par  
  exemple).

- Les floodfills peuvent limiter la taille maximale à une valeur raisonnable pour éviter les abus.

- Après déchiffrement, plusieurs vérifications doivent être effectuées, notamment que  
  l'horodatage interne et l'expiration correspondent à ceux du niveau supérieur.

- ChaCha20 a été choisi plutôt qu'AES. Bien que les vitesses soient similaires si le  
  support matériel AES est disponible, ChaCha20 est 2,5 à 3 fois plus rapide lorsque  
  le support matériel AES n'est pas disponible, comme sur les appareils ARM bas de gamme.

- Nous ne nous soucions pas assez de la vitesse pour utiliser BLAKE2b avec clé. Il a une taille de sortie  
  suffisamment grande pour accommoder le plus grand n requis (ou nous pouvons l'appeler une fois par  
  clé souhaitée avec un argument compteur). BLAKE2b est beaucoup plus rapide que SHA-256, et  
  BLAKE2b avec clé réduirait le nombre total d'appels à la fonction de hachage.  
  Cependant, voir la proposition 148, où il est proposé que nous passions à BLAKE2b pour d'autres raisons.  
  Voir [Secure key derivation performance](https://www.lvh.io/posts/secure-key-derivation-performance.html).


### Meta LS2

Ceci est utilisé pour remplacer le multihébergement. Comme tout leaseset, ceci est signé par le  
créateur. C'est une liste authentifiée de hachages de destination.

Le Meta LS2 est le nœud supérieur, et éventuellement des nœuds intermédiaires,  
d'une structure en arbre.  
Il contient plusieurs entrées, chacune pointant vers un LS, LS2 ou un autre Meta LS2  
pour supporter un multihébergement massif.  
Un Meta LS2 peut contenir un mélange d'entrées LS, LS2 et Meta LS2.  
Les feuilles de l'arbre sont toujours un LS ou LS2.  
L'arbre est un DAG ; les boucles sont interdites ; les clients effectuant des recherches doivent détecter et  
refuser de suivre les boucles.

Un Meta LS2 peut avoir une expiration beaucoup plus longue qu'un LS ou LS2 standard.  
Le niveau supérieur peut avoir une expiration plusieurs heures après la date de publication.  
Le temps d'expiration maximal sera appliqué par les floodfills et clients, et est à déterminer.

L'utilisation de Meta LS2 est le multihébergement massif, mais sans plus  
de protection contre la corrélation des routeurs aux leasesets (au redémarrage du routeur) que  
celle fournie actuellement avec LS ou LS2.  
Ceci équivaut au cas d'usage « facebook », qui n'a probablement pas besoin  
de protection contre la corrélation. Ce cas d'usage a probablement besoin de clés hors ligne,  
qui sont fournies dans l'en-tête standard à chaque nœud de l'arbre.

Le protocole backend pour la coordination entre les routeurs feuilles, les signataires intermédiaires et principaux de Meta LS  
n'est pas spécifié ici. Les exigences sont extrêmement simples - juste vérifier que le pair est en ligne,  
et publier un nouveau LS toutes les quelques heures. La seule complexité est pour choisir de nouveaux  
éditeurs pour les Meta LS de niveau supérieur ou intermédiaire en cas de panne.

Le mélange de leasesets où des locations de plusieurs routeurs sont combinées, signées et publiées  
dans un seul leaseset est documenté dans la proposition 140, « multihébergement invisible ».  
Cette proposition est irréalisable telle quelle, car les connexions en streaming ne seraient pas  
« collantes » à un seul routeur, voir http://zzz.i2p/topics/2335 .

Le protocole backend, et l'interaction avec les composants internes du routeur et du client, serait  
très complexe pour le multihébergement invisible.

Pour éviter de surcharger le floodfill pour le Meta LS de niveau supérieur, l'expiration devrait  
être d'au moins plusieurs heures. Les clients doivent mettre en cache le Meta LS de niveau supérieur, et le conserver  
entre les redémarrages s'il n'est pas expiré.

Nous devons définir un algorithme pour que les clients parcourent l'arbre, y compris des solutions de secours,  
afin que l'utilisation soit dispersée. Une fonction de distance de hachage, coût et aléatoire.  
Si un nœud a à la fois LS ou LS2 et Meta LS, nous devons savoir quand il est autorisé  
d'utiliser ces leasesets, et quand continuer à parcourir l'arbre.




Recherche avec  
    Flag LS standard (1)  
Stockage avec  
    Type Meta LS2 (7)  
Stockage à  
    Hachage de la destination  
    Ce hachage est ensuite utilisé pour générer la « clé de routage » quotidienne, comme dans LS1  
Expiration typique  
    Heures. Max 18,2 heures (65535 secondes)  
Publié par  
    Destination « maître » ou coordinateur, ou coordinateurs intermédiaires

### Format

```
En-tête standard LS2 tel que spécifié ci-dessus

  Partie spécifique à Meta LS2
  - Propriétés (Mapping tel que spécifié dans la spécification des structures communes, 2 octets nuls si aucune)
  - Nombre d'entrées (1 octet) Maximum à déterminer
  - Entrées. Chaque entrée contient : (40 octets)
    - Hachage (32 octets)
    - Flags (2 octets)
      À déterminer. Mettre tous à zéro pour compatibilité avec les usages futurs.
    - Type (1 octet) Le type de LS auquel il fait référence ;  
      1 pour LS, 3 pour LS2, 5 pour chiffré, 7 pour meta, 0 pour inconnu.
    - Coût (priorité) (1 octet)
    - Expiration (4 octets) (4 octets, big endian, secondes depuis l'époque, dépassement en 2106)
  - Nombre de révocations (1 octet) Maximum à déterminer
  - Révocations : Chaque révocation contient : (32 octets)
    - Hachage (32 octets)

  Signature standard LS2 :
  - Signature (40+ octets)
    La signature couvre tout ce qui précède.
```

Flags et propriétés : pour usage futur


### Notes

- Un service distribué utilisant ceci aurait un ou plusieurs « maîtres » avec la  
  clé privée de la destination du service. Ils détermineraient (hors bande) la  
  liste actuelle des destinations actives et publieraient le Meta LS2. Pour  
  la redondance, plusieurs maîtres pourraient multihéberger (c'est-à-dire publier simultanément) le  
  Meta LS2.

- Un service distribué pourrait commencer avec une destination unique ou utiliser le  
  multihébergement ancien style, puis passer à un Meta LS2. Une recherche LS standard pourrait retourner  
  n'importe lequel parmi LS, LS2 ou Meta LS2.

- Lorsqu'un service utilise un Meta LS2, il n'a pas de tunnels (locations).


### Enregistrement de service

Ceci est un enregistrement individuel indiquant qu'une destination participe à un  
service. Il est envoyé du participant au floodfill. Il n'est jamais envoyé  
individuellement par un floodfill, mais seulement comme partie d'une liste de service. L'enregistrement de service est également utilisé pour révoquer la participation à un service, en fixant l'  
expiration à zéro.

Ce n'est pas un LS2 mais il utilise le format d'en-tête et de signature standard LS2.

Recherche avec  
    n/a, voir Liste de service  
Stockage avec  
    Type Enregistrement de service (9)  
Stockage à  
    Hachage du nom du service  
    Ce hachage est ensuite utilisé pour générer la « clé de routage » quotidienne, comme dans LS1  
Expiration typique  
    Heures. Max 18,2 heures (65535 secondes)  
Publié par  
    Destination

### Format

```
En-tête standard LS2 tel que spécifié ci-dessus

  Partie spécifique à l'Enregistrement de service
  - Port (2 octets, big endian) (0 si non spécifié)
  - Hachage du nom du service (32 octets)

  Signature standard LS2 :
  - Signature (40+ octets)
    La signature couvre tout ce qui précède.
```

### Notes

- Si l'expiration est à zéro, le floodfill devrait révoquer l'enregistrement et ne plus  
  l'inclure dans la liste de service.

- Stockage : Le floodfill peut strictement limiter le stockage de ces enregistrements et  
  limiter le nombre d'enregistrements stockés par hachage et leur expiration. Une liste blanche  
  de hachages peut également être utilisée.

- Tout autre type netdb au même hachage a priorité, donc un enregistrement de service ne peut jamais  
  écraser un LS/RI, mais un LS/RI écrasera tous les enregistrements de service à ce hachage.



### Liste de service

Ceci n'est rien comme un LS2 et utilise un format différent.

La liste de service est créée et signée par le floodfill. Elle est non authentifiée  
dans le sens où n'importe qui peut rejoindre un service en publiant un Enregistrement de service à un  
floodfill.

Une Liste de service contient des Enregistrements de service courts, pas des Enregistrements complets. Ceux-ci  
contiennent des signatures mais seulement des hachages, pas des destinations complètes, donc ils ne peuvent pas être  
vérifiés sans la destination complète.

La sécurité, s'il y en a une, et la désirabilité des listes de service sont à déterminer.  
Les floodfills pourraient limiter la publication et les recherches à une liste blanche de services,  
mais cette liste blanche peut varier selon l'implémentation ou les préférences de l'opérateur.  
Il peut ne pas être possible d'atteindre un consensus sur une liste blanche commune de base  
entre les implémentations.

Si le nom du service est inclus dans l'enregistrement de service ci-dessus,  
les opérateurs de floodfill peuvent s'y opposer ; si seul le hachage est inclus,  
il n'y a pas de vérification, et un enregistrement de service pourrait « entrer » avant  
tout autre type netdb et être stocké dans le floodfill.

Recherche avec  
    Type de recherche Liste de service (11)  
Stockage avec  
    Type Liste de service (11)  
Stockage à  
    Hachage du nom du service  
    Ce hachage est ensuite utilisé pour générer la « clé de routage » quotidienne, comme dans LS1  
Expiration typique  
    Heures, non spécifiée dans la liste elle-même, selon la politique locale  
Publié par  
    Personne, jamais envoyé au floodfill, jamais diffusé.

### Format

N'utilise PAS l'en-tête standard LS2 spécifié ci-dessus.

```
- Type (1 octet)
    Pas réellement dans l'en-tête, mais fait partie des données couvertes par la signature.
    À prendre depuis le champ du message Database Store.
  - Hachage du nom du service (implicite, dans le message Database Store)
  - Hachage du Créateur (floodfill) (32 octets)
  - Horodatage de publication (8 octets, big endian)

  - Nombre d'Enregistrements de service courts (1 octet)
  - Liste d'Enregistrements de service courts :
    Chaque Enregistrement de service court contient (90+ octets)
    - Hachage de destination (32 octets)
    - Horodatage de publication (8 octets, big endian)
    - Expiration (4 octets, big endian) (décalage depuis la publication en ms)
    - Flags (2 octets)
    - Port (2 octets, big endian)
    - Longueur de signature (2 octets, big endian)
    - Signature de
