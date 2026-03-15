---
title: "Spécification SSU2"
description: "Protocole de Transport UDP Semi-Fiable Sécurisé Version 2"
slug: "ssu2"
category: "Transports"
lastUpdated: "2026-03"
accurateFor: "0.9.69"
---

## Statut

Substantiellement complet. Voir [Prop159](/proposals/159-ssu2) pour des informations supplémentaires et les objectifs, y compris l'analyse de sécurité, les modèles de menace, un examen de la sécurité et des problèmes de SSU 1, et des extraits des spécifications QUIC.

Plan de déploiement :

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Feature</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Testing (not default)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Enabled by default</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Local test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-03</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test in-net</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze basic protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Basic Session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address Validation (Retry)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Fragmented RI in handshake</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze extended protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Enable for random 2%</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Validation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Connection Migration</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Immediate ACK flag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Key Rotation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2023-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (i2pd)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (Java I2P)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.61 2023-12</td></tr>
  </tbody>
</table>
La session de base inclut la phase de négociation et la phase de données. Le protocole étendu inclut le relais et le test de pairs.

## Aperçu

Cette spécification définit un protocole d'accord de clés authentifié pour améliorer la résistance de [SSU](/docs/transport/ssu) à diverses formes d'identification automatisée et d'attaques.

Comme pour les autres transports I2P, SSU2 est défini pour le transport point-à-point (routeur-à-routeur) des messages I2NP. Ce n'est pas un canal de données généraliste. Comme [SSU](/docs/transport/ssu), il fournit également deux services supplémentaires : le relais pour la traversée NAT, et les tests de pairs pour déterminer l'accessibilité entrante. Il fournit aussi un troisième service, absent dans SSU, pour la migration de connexion lorsqu'un pair change d'IP ou de port.

## Aperçu de la conception

### Résumé

Nous nous appuyons sur plusieurs protocoles existants, à la fois au sein d'I2P et dans les standards externes, pour l'inspiration, les conseils et la réutilisation de code :

- Modèles de menace : De NTCP2 [NTCP2](/docs/specs/ntcp2), avec des menaces supplémentaires significatives pertinentes pour le transport UDP comme analysées par QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Choix cryptographiques : De [NTCP2](/docs/specs/ntcp2).
- Handshake : Noise XK de [NTCP2](/docs/specs/ntcp2) et [NOISE](https://noiseprotocol.org/noise.html). Des simplifications significatives de NTCP2 sont possibles grâce à l'encapsulation (limites de message inhérentes) fournie par UDP.
- Obfuscation des clés éphémères de handshake : Adapté de [NTCP2](/docs/specs/ntcp2) mais utilisant ChaCha20 de [ECIES](/docs/specs/ecies) au lieu d'AES.
- En-têtes de paquet : Adaptés de WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) et QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Obfuscation des en-têtes de paquet : Adapté de [NTCP2](/docs/specs/ntcp2) mais utilisant ChaCha20 de [ECIES](/docs/specs/ecies) au lieu d'AES.
- Protection des en-têtes de paquet : Adapté de QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) et [Nonces](https://eprint.iacr.org/2019/624.pdf)
- En-têtes utilisés comme données associées AEAD comme dans [ECIES](/docs/specs/ecies).
- Numérotation des paquets : Adaptée de WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) et QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Messages : Adaptés de [SSU](/docs/transport/ssu)
- Fragmentation I2NP : Adaptée de [SSU](/docs/transport/ssu)
- Relais et tests de pairs : Adaptés de [SSU](/docs/transport/ssu)
- Signatures des données de relais et de test de pair : De la spécification des structures communes [Common](/docs/specs/common-structures)
- Format de bloc : De [NTCP2](/docs/specs/ntcp2) et [ECIES](/docs/specs/ecies).
- Remplissage et options : De [NTCP2](/docs/specs/ntcp2) et [ECIES](/docs/specs/ecies).
- Acks, nacks : Adaptés de QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000).
- Contrôle de flux : À déterminer

Il n'y a pas de nouvelles primitives cryptographiques qui n'ont pas été utilisées dans I2P auparavant.

### Garanties de livraison

Comme avec les autres transports I2P NTCP, NTCP2, et SSU 1, ce transport n'est pas un mécanisme généraliste pour la livraison d'un flux ordonné d'octets. Il est conçu pour le transport de messages I2NP. Il n'y a pas d'abstraction de "flux" fournie.

De plus, comme pour SSU, il contient des fonctionnalités supplémentaires pour la traversée NAT facilitée par les pairs et les tests d'accessibilité (connexions entrantes).

Comme pour SSU 1, il ne fournit PAS de livraison ordonnée des messages I2NP. Il ne garantit pas non plus la livraison des messages I2NP. Pour des raisons d'efficacité, ou à cause de la livraison non ordonnée des datagrammes UDP ou de la perte de ces datagrammes, les messages I2NP peuvent être livrés à l'extrémité distante dans le désordre, ou peuvent ne pas être livrés du tout. Un message I2NP peut être retransmis plusieurs fois si nécessaire, mais la livraison peut finalement échouer sans provoquer la déconnexion complète de la connexion. De plus, de nouveaux messages I2NP peuvent continuer à être envoyés même pendant qu'une retransmission (récupération de perte) se produit pour d'autres messages I2NP.

Ce protocole ne prévient PAS complètement la livraison en double des messages I2NP. Le router devrait appliquer l'expiration I2NP et utiliser un filtre de Bloom ou un autre mécanisme basé sur l'ID du message I2NP. Voir la section Duplication des Messages I2NP ci-dessous.

### Protocole Noise Framework

Cette spécification fournit les exigences basées sur le Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (Révision 33, 2017-10-04). Noise a des propriétés similaires au protocole Station-To-Station [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol), qui est la base du protocole [SSU](/docs/transport/ssu). Dans le jargon de Noise, Alice est l'initiateur, et Bob est le répondeur.

SSU2 est basé sur le protocole Noise Noise_XK_25519_ChaChaPoly_SHA256. (L'identifiant réel pour la fonction de dérivation de clé initiale est "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256" pour indiquer les extensions I2P - voir la section KDF 1 ci-dessous)

NOTE : Cet identifiant est différent de celui utilisé pour NTCP2, car les trois messages de handshake utilisent l'en-tête comme données associées.

Ce protocole Noise utilise les primitives suivantes :

- Modèle de handshake : XK Alice transmet sa clé à Bob (X) Alice connaît déjà la clé statique de Bob (K)
- Fonction DH : X25519 X25519 DH avec une longueur de clé de 32 octets comme spécifié dans [RFC-7748](https://tools.ietf.org/html/rfc7748).
- Fonction de chiffrement : ChaChaPoly AEAD_CHACHA20_POLY1305 comme spécifié dans [RFC-7539](https://tools.ietf.org/html/rfc7539) section 2.8. Nonce de 12 octets, avec les 4 premiers octets mis à zéro.
- Fonction de hachage : SHA256 Hachage standard de 32 octets, déjà utilisé extensivement dans I2P.

### Ajouts au Framework

Cette spécification définit les améliorations suivantes à Noise_XK_25519_ChaChaPoly_SHA256. Celles-ci suivent généralement les directives de la section 13 de [NOISE](https://noiseprotocol.org/noise.html).

1) Les messages de handshake (Session Request, Created, Confirmed) incluent un en-tête de 16 ou 32 octets. 2) Les en-têtes pour les messages de handshake (Session Request, Created, Confirmed) sont utilisés comme entrée pour mixHash() avant le chiffrement/déchiffrement pour lier les en-têtes au message. 3) Les en-têtes sont chiffrés et protégés. 4) Les clés éphémères en texte clair sont obfusquées avec le chiffrement ChaCha20 en utilisant une clé et un IV connus. C'est plus rapide qu'elligator2. 5) Le format de charge utile est défini pour les messages 1, 2, et la phase de données. Bien sûr, ceci n'est pas défini dans Noise.

La phase de données utilise un chiffrement similaire à, mais non compatible avec, la phase de données Noise.

### Établissement de session

Nous définissons les fonctions suivantes correspondant aux blocs de construction cryptographiques utilisés.

#### En-tête Long

ZEROLEN

#### En-tête court

:   tableau d'octets de longueur zéro

#### Numérotation des ID de Connexion

H(p, d)

#### Numérotation des paquets

:   Fonction de hachage SHA-256 qui prend une chaîne de personnalisation p et des données d, et produit une sortie de 32 octets. Tel que défini dans [NOISE](https://noiseprotocol.org/noise.html). || ci-dessous signifie concaténer.

## Définitions

MixHash(d)

:   Fonction de hachage SHA-256 qui prend un hachage précédent h et de nouvelles données d, et produit une sortie de 32 octets de longueur. || ci-dessous signifie concaténer.

STREAM

:   Le ChaCha20/Poly1305 AEAD tel que spécifié dans [RFC-7539](https://tools.ietf.org/html/rfc7539). S_KEY_LEN = 32 et S_IV_LEN = 12.

DH

    Use SHA-256 as follows:

        H(p, d) := SHA-256(p || d)

:   Système d'accord de clés publiques X25519. Clés privées de 32 octets, clés publiques de 32 octets, produit des sorties de 32 octets. Il dispose des fonctions suivantes :

HKDF(salt, ikm, info, n)

    Use SHA-256 as follows:

        MixHash(d) := h = SHA-256(h || d)

:   Une fonction de dérivation de clé cryptographique qui prend un matériel de clé d'entrée ikm (qui devrait avoir une bonne entropie mais n'est pas requis d'être une chaîne uniformément aléatoire), un salt de longueur 32 octets, et une valeur 'info' spécifique au contexte, et produit une sortie de n octets appropriée pour une utilisation comme matériel de clé.

MixKey(d)

    ENCRYPT(k, n, plaintext, ad)

    :   Encrypts plaintext using the cipher key k, and nonce n which MUST be unique for the key k. Associated data ad is optional. Returns a ciphertext that is the size of the plaintext + 16 bytes for the HMAC.

        The entire ciphertext must be indistinguishable from random if the key is secret.

    DECRYPT(k, n, ciphertext, ad)

    :   Decrypts ciphertext using the cipher key k, and nonce n. Associated data ad is optional. Returns the plaintext.

:   Utilise HKDF() avec une chainKey précédente et de nouvelles données d, et définit la nouvelle chainKey et k. Comme défini dans [NOISE](https://noiseprotocol.org/noise.html).

Chaque datagramme UDP contient exactement un message. La longueur du datagramme (après les en-têtes IP et UDP) est la longueur du message. Le padding, s'il y en a un, est contenu dans un bloc de padding à l'intérieur du message. Dans ce document, nous utilisons les termes "datagramme" et "paquet" de manière largement interchangeable. Chaque datagramme (ou paquet) contient un seul message (contrairement à QUIC, où un datagramme peut contenir plusieurs paquets QUIC). L'"en-tête de paquet" est la partie après l'en-tête IP/UDP.

    GENERATE_PRIVATE()

    :   Generates a new private key.

    DERIVE_PUBLIC(privkey)

    :   Returns the public key corresponding to the given private key.

    DH(privkey, pubkey)

    :   Generates a shared secret from the given private and public keys.

Exception : Le message Session Confirmed est unique en ce qu'il peut être fragmenté sur plusieurs paquets. Voir la section Fragmentation Session Confirmed ci-dessous pour plus d'informations.

Tous les messages SSU2 ont une longueur d'au moins 40 octets. Tout message d'une longueur de 1 à 39 octets est invalide. Tous les messages SSU2 ont une longueur inférieure ou égale à 1472 (IPv4) ou 1452 (IPv6) octets. Le format de message est basé sur les messages Noise, avec des modifications pour l'encadrement et l'indistinguabilité. Les implémentations utilisant des bibliothèques Noise standard doivent pré-traiter les messages reçus au format de message Noise standard. Tous les champs chiffrés sont des textes chiffrés AEAD.

    Use HKDF as specified in [RFC-5869](https://tools.ietf.org/html/rfc5869), using the HMAC hash function SHA-256 as specified in [RFC-2104](https://tools.ietf.org/html/rfc2104). This means that SALT_LEN is 32 bytes max.

Les messages suivants sont définis :

La séquence d'établissement standard, quand Alice a un token valide précédemment reçu de Bob, est la suivante :

    Use HKDF as follows:

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]

## Messages

Lorsque Alice ne dispose pas d'un token valide, la séquence d'établissement est la suivante :

Quand Alice pense avoir un token valide, mais que Bob le rejette (peut-être parce que Bob a redémarré), la séquence d'établissement est la suivante :

Bob peut rejeter une demande de session ou de jeton en répondant avec un message Retry contenant un bloc Termination avec un code de raison. En fonction du code de raison, Alice ne devrait pas tenter une autre demande pendant une certaine période :

En utilisant la terminologie Noise, la séquence d'établissement et de données est la suivante : (Propriétés de sécurité de la charge utile)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Encr. Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionRequest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionCreated</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionConfirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">PeerTest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">HolePunch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
  </tbody>
</table>
### En-tête de paquet

Une fois qu'une session a été établie, Alice et Bob peuvent échanger des messages Data.

```
Alice                           Bob

SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Tous les paquets commencent par un en-tête obfusqué (chiffré). Il existe deux types d'en-têtes, longs et courts. Notez que les 13 premiers octets (ID de connexion de destination, numéro de paquet et type) sont identiques pour tous les en-têtes.

```
Alice                           Bob

TokenRequest --------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
L'en-tête long fait 32 octets. Il est utilisé avant qu'une session ne soit créée, pour Token Request, SessionRequest, SessionCreated, et Retry. Il est également utilisé pour les messages Peer Test et Hole Punch hors session.

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Avant le chiffrement de l'en-tête :

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry containing a Termination block

or

TokenRequest --------------------->
<---------------------------  Retry containing a Termination block
```
L'en-tête court fait 16 octets. Il est utilisé pour les messages Session Created et Data. Les messages non authentifiés tels que Session Request, Retry et Peer Test utiliseront toujours l'en-tête long.

```
XK(s, rs):           Authentication   Confidentiality
  <- s
  ...
  -> e, es                  0                2
  <- e, ee                  2                1
  -> s, se                  2                5
  <-                        2                5
```
16 octets sont requis, car le récepteur doit déchiffrer les 16 premiers octets pour obtenir le type de message, puis doit déchiffrer 16 octets supplémentaires si c'est effectivement un en-tête long, comme l'indique le type de message.

### Intégrité des paquets

Pour Session Confirmed, avant le chiffrement de l'en-tête :

#### Liaison d'en-tête

Voir la section Fragmentation de Session Confirmée ci-dessous pour plus d'informations sur le champ frag.

Pour les messages Data, avant le chiffrement de l'en-tête :

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 0, 1, 7, 9, 10, or 11

ver :: The protocol version, equal to 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: 8 bytes, unsigned big endian integer

Token :: 8 bytes, unsigned big endian integer
```
#### Chiffrement d'en-tête

Les ID de connexion doivent être générés de manière aléatoire. Les ID Source et Destination ne doivent PAS être identiques, afin qu'un attaquant situé sur le chemin ne puisse pas capturer et renvoyer un paquet à l'expéditeur qui paraisse valide. N'utilisez PAS un compteur pour générer les ID de connexion, afin qu'un attaquant situé sur le chemin ne puisse pas générer un paquet qui paraisse valide.

Contrairement à QUIC, nous ne changeons pas les ID de connexion pendant ou après la négociation, même après un message Retry. Les ID restent constants depuis le premier message (Token Request ou Session Request) jusqu'au dernier message (Data with Termination). De plus, les ID de connexion ne changent pas pendant ou après un défi de chemin ou une migration de connexion.

Une autre différence par rapport à QUIC est que les ID de connexion dans les en-têtes sont toujours chiffrés au niveau de l'en-tête. Voir ci-dessous.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, all zeros

type :: The message type = 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility
```
Si aucun bloc de Numéro de Premier Paquet n'est envoyé dans la négociation, les paquets sont numérotés au sein d'une session unique, pour chaque direction, en commençant par 0, jusqu'à un maximum de (2**32 -1). Une session doit être terminée, et une nouvelle session créée, bien avant que le nombre maximum de paquets ne soit envoyé.

Si un bloc First Packet Number est envoyé lors du handshake, les paquets sont numérotés au sein d'une seule session, pour cette direction, en commençant à partir de ce numéro de paquet. Le numéro de paquet peut revenir à zéro durant la session. Lorsqu'un maximum de 2**32 paquets ont été envoyés, ramenant le numéro de paquet au premier numéro de paquet, cette session n'est plus valide. Une session doit être terminée, et une nouvelle session créée, bien avant que le nombre maximum de paquets ne soit envoyé.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|flag|moreflags|
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 6

flag :: 1 byte flags:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-1: unused, set to 0 for future compatibility
       bits 0: when set to 1, immediate ack requested

moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### KDF de chiffrement d'en-tête

TODO rotation des clés, réduire le nombre maximum de paquets ?

Les paquets de handshake déterminés comme perdus sont retransmis en entier, avec l'en-tête identique incluant le numéro de paquet. Les messages de handshake Session Request, Session Created et Session Confirmed DOIVENT être retransmis avec le même numéro de paquet et un contenu chiffré identique, de sorte que le même hachage chaîné sera utilisé pour chiffrer la réponse. Le message Retry n'est jamais transmis.

Les paquets de phase de données qui sont déterminés comme perdus ne sont jamais retransmis dans leur intégralité (sauf pour la terminaison, voir ci-dessous). Il en va de même pour les blocs contenus dans les paquets perdus. Au lieu de cela, les informations qui pourraient être transportées dans les blocs sont renvoyées dans de nouveaux paquets selon les besoins. Les paquets de données ne sont jamais retransmis avec le même numéro de paquet. Toute retransmission du contenu d'un paquet (que le contenu reste identique ou non) doit utiliser le prochain numéro de paquet inutilisé.

#### Validation d'en-tête

Retransmettre un paquet entier inchangé tel quel, avec le même numéro de paquet, n'est pas autorisé pour plusieurs raisons. Pour le contexte, voir QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) section 12.3.

Les nouveaux paquets sont utilisés pour transporter des informations qui sont déterminées comme ayant été perdues. En général, les informations sont renvoyées lorsqu'un paquet contenant ces informations est déterminé comme perdu, et l'envoi cesse lorsqu'un paquet contenant ces informations est accusé de réception.

Exception : Un paquet de phase de données contenant un bloc de Terminaison peut, mais n'est pas tenu d'être, retransmis entièrement, tel quel. Voir la section Terminaison de Session ci-dessous.

Les paquets suivants contiennent un numéro de paquet aléatoire qui est ignoré :

Pour Alice, la numérotation des paquets sortants commence à 0 avec Session Confirmed. Pour Bob, la numérotation des paquets sortants commence à 0 avec le premier paquet Data, qui devrait être un ACK du Session Confirmed. Les numéros de paquets dans un exemple de handshake standard seront :

Toute retransmission de messages de handshake (SessionRequest, SessionCreated, ou SessionConfirmed) doit être renvoyée sans modification, avec le même numéro de paquet. N'utilisez pas de clés éphémères différentes ou ne modifiez pas la charge utile lors de la retransmission de ces messages.

- Il est inefficace de stocker les paquets pour la retransmission
- Un nouveau paquet de données semble différent à un observateur sur le chemin, impossible de dire qu'il est retransmis
- Un nouveau paquet reçoit un bloc d'accusé de réception mis à jour envoyé avec lui, pas l'ancien bloc d'accusé de réception
- Vous ne retransmettez que ce qui est nécessaire. certains fragments auraient pu être déjà retransmis une fois et avoir été acquittés
- Vous pouvez inclure autant que nécessaire dans chaque paquet retransmis si davantage est en attente
- Les points de terminaison qui suivent tous les paquets individuels dans le but de détecter les doublons risquent d'accumuler un état excessif. Les données requises pour détecter les doublons peuvent être limitées en maintenant un numéro de paquet minimum en dessous duquel tous les paquets sont immédiatement abandonnés.
- Ce schéma est beaucoup plus flexible

L'en-tête (avant obfuscation et protection) est toujours inclus dans les données associées pour la fonction AEAD, afin de lier cryptographiquement l'en-tête aux données.

Le chiffrement d'en-tête a plusieurs objectifs. Voir la section "Discussion supplémentaire sur la DPI" ci-dessus pour le contexte et les hypothèses.

Les en-têtes sont chiffrés avec des clés connues publiées dans la base de données réseau ou calculées ultérieurement. Dans la phase de handshake, cela sert uniquement à la résistance DPI, car la clé est publique et la clé et les nonces sont réutilisés, ce qui revient donc effectivement à une simple obfuscation. Notez que le chiffrement des en-têtes est également utilisé pour obscurcir les clés éphémères X (dans Session Request) et Y (dans Session Created).

- Demande de session
- Session créée
- Demande de jeton
- Nouvelle tentative
- Test de pair
- Perforation de pare-feu

Voir la section Gestion des paquets entrants ci-dessous pour des conseils supplémentaires.

```
Alice                           Bob

SessionRequest (r)    ------------>
<-------------   SessionCreated (r)
SessionConfirmed (0)  ------------>
<-------------             Data (0) (Ack-only)
Data (1)              ------------> (May be sent before Ack is received)
<-------------             Data (1)
Data (2)              ------------>
Data (3)              ------------>
Data (4)              ------------>
<-------------             Data (2)

r = random packet number (ignored)
Token Request, Retry, and Peer Test
also have random packet numbers.
```
Les octets 0-15 de tous les en-têtes sont chiffrés en utilisant un schéma de protection d'en-tête par XOR avec des données calculées à partir de clés connues, en utilisant ChaCha20, similaire à QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) et [Nonces](https://eprint.iacr.org/2019/624.pdf). Cela garantit que l'en-tête court chiffré et la première partie de l'en-tête long apparaîtront comme aléatoires.

#### ChaCha20/Poly1305

Pour Session Request et Session Created, les octets 16-31 de l'en-tête long et la clé éphémère Noise de 32 octets sont chiffrés en utilisant ChaCha20. Les données non chiffrées étant aléatoires, les données chiffrées apparaîtront également comme aléatoires.

#### Notes

Pour Retry, les octets 16-31 de l'en-tête long sont chiffrés en utilisant ChaCha20. Les données non chiffrées sont aléatoires, donc les données chiffrées apparaîtront comme étant aléatoires.

- Empêcher la DPI en ligne d'identifier le protocole
- Empêcher les motifs dans une série de messages dans la même connexion, sauf pour les retransmissions de handshake
- Empêcher les motifs dans les messages du même type dans différentes connexions
- Empêcher le déchiffrement des en-têtes de handshake sans connaissance de la clé d'introduction trouvée dans la netdb
- Empêcher l'identification des clés éphémères X25519 sans connaissance de la clé d'introduction trouvée dans la netdb
- Empêcher le déchiffrement du numéro et du type de paquet de la phase de données par tout attaquant en ligne ou hors ligne
- Empêcher l'injection de paquets de handshake valides par un observateur sur le chemin ou hors du chemin sans connaissance de la clé d'introduction trouvée dans la netdb
- Empêcher l'injection de paquets de données valides par un observateur sur le chemin ou hors du chemin
- Permettre une classification rapide et efficace des paquets entrants
- Fournir une résistance au "probing" afin qu'il n'y ait aucune réponse à une Session Request incorrecte, ou s'il y a une réponse Retry, la réponse n'est pas identifiable comme I2P sans connaissance de la clé d'introduction trouvée dans la netdb
- Le Destination Connection ID n'est pas une donnée critique, et c'est acceptable s'il peut être déchiffré par un observateur ayant connaissance de la clé d'introduction trouvée dans la netdb
- Le numéro de paquet d'un paquet de phase de données est un nonce AEAD et constitue une donnée critique. Il ne doit pas être déchiffrable par un observateur même avec la connaissance de la clé d'introduction trouvée dans la netdb. Voir [Nonces](https://eprint.iacr.org/2019/624.pdf).

Contrairement au schéma de protection des en-têtes QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001), TOUTES les parties de tous les en-têtes, y compris les ID de connexion de destination et source, sont chiffrées. QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) et [Nonces](https://eprint.iacr.org/2019/624.pdf) se concentrent principalement sur le chiffrement de la partie "critique" de l'en-tête, c'est-à-dire le numéro de paquet (nonce ChaCha20). Bien que le chiffrement de l'ID de session rende la classification des paquets entrants un peu plus complexe, cela rend certaines attaques plus difficiles. QUIC définit différents ID de connexion pour différentes phases, et pour le défi de chemin et la migration de connexion. Ici, nous utilisons les mêmes ID de connexion tout au long, car ils sont chiffrés.

Il y a sept phases de clés de protection d'en-tête :

Le chiffrement d'en-tête est conçu pour permettre une classification rapide des paquets entrants, sans heuristiques complexes ou mécanismes de repli. Ceci est accompli en utilisant la même clé k_header_1 pour presque tous les messages entrants. Même lorsque l'IP source ou le port d'une connexion change en raison d'un changement d'IP réel ou du comportement NAT, le paquet peut être rapidement associé à une session avec une seule recherche de l'ID de connexion.

Notez que Session Created et Retry sont les SEULS messages qui nécessitent un traitement de repli pour k_header_1 afin de déchiffrer le Connection ID, car ils utilisent la clé d'intro de l'expéditeur (Bob). TOUS les autres messages utilisent la clé d'intro du destinataire pour k_header_1. Le traitement de repli n'a besoin que de rechercher les connexions sortantes en attente par IP/port source.

Si le traitement de repli par IP/port source ne parvient pas à trouver une connexion sortante en attente, il pourrait y avoir plusieurs causes :

Bien qu'un traitement de secours supplémentaire soit possible pour tenter de trouver la connexion sortante en attente et déchiffrer l'ID de connexion en utilisant le k_header_1 pour cette connexion, ce n'est probablement pas nécessaire. Si Bob a des problèmes avec son NAT ou le routage des paquets, il est probablement préférable de laisser la connexion échouer. Cette conception repose sur le fait que les points de terminaison conservent une adresse stable pendant toute la durée de la négociation.

Voir la section Gestion des Paquets Entrants ci-dessous pour des directives supplémentaires.

- Demande de Session et Demande de Jeton
- Session Créée
- Nouvelle Tentative
- Session Confirmée
- Phase de Données
- Test de Pair
- Perforation de Trou

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_1</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_2</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Request KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Created KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice/Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See data phase KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 5,7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Hole Punch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
  </tbody>
</table>
Voir les sections KDF individuelles ci-dessous pour la dérivation des clés de chiffrement d'en-tête pour cette phase.

Cette KDF utilise les 24 derniers octets du paquet comme IV pour les deux opérations ChaCha20. Comme tous les paquets se terminent par un MAC de 16 octets, cela nécessite que toutes les charges utiles de paquet aient un minimum de 8 octets. Cette exigence est également documentée dans les sections de message ci-dessous.

Après avoir déchiffré les 8 premiers octets de l'en-tête, le récepteur connaîtra l'ID de Connexion de Destination. À partir de là, le récepteur sait quelle clé de chiffrement d'en-tête utiliser pour le reste de l'en-tête, en fonction de la phase de clé de la session.

- N'est pas un message SSU2
- Un message SSU2 corrompu
- La réponse est usurpée ou modifiée par un attaquant
- Bob a un NAT symétrique
- Bob a changé d'IP ou de port pendant le traitement du message
- Bob a envoyé la réponse par une interface différente

Le déchiffrement des 8 octets suivants de l'en-tête révélera alors le type de message et permettra de déterminer s'il s'agit d'un en-tête court ou long. S'il s'agit d'un en-tête long, le récepteur doit valider les champs version et netid. Si la version est != 2, ou si le netid est != la valeur attendue (généralement 2, sauf dans les réseaux de test), le récepteur doit abandonner le message.

Tous les messages contiennent soit trois soit quatre parties :

Dans tous les cas, l'en-tête (et si présente, la clé éphémère) est lié au MAC d'authentification pour garantir que l'ensemble du message est intact.

#### Gestion des erreurs AEAD

```
// incoming encrypted packet
packet = incoming encrypted packet
len = packet.length

// take the next-to-last 12 bytes of the packet
iv = packet[len-24:len-13]
k_header_1 = header encryption key 1
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_1, iv, data)

// encrypt the first part of the header by XORing with the mask
packet[0:7] ^= mask[0:7]

// take the last 12 bytes of the packet
iv = packet[len-12:len-1]
k_header_2 = header encryption key 2
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_2, iv, data)

// encrypt the second part of the header by XORing with the mask
packet[8:15] ^= mask[0:7]


// For Session Request and Session Created only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header and the ephemeral key
packet[16:63] = ChaCha20.encrypt(k_header_2, iv, packet[16:63])


// For Retry, Token Request, Peer Test, and Hole Punch only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header
packet[16:31] = ChaCha20.encrypt(k_header_2, iv, packet[16:31])
```
Les gestionnaires de paquets entrants doivent toujours déchiffrer la charge utile ChaCha20 et valider le MAC avant de traiter le message, avec une exception : Pour atténuer les attaques DoS provenant de paquets avec des adresses usurpées contenant des messages Session Request apparents avec un token invalide, un gestionnaire n'a PAS BESOIN de tenter de déchiffrer et valider le message complet (nécessitant une opération DH coûteuse en plus du déchiffrement ChaCha20/Poly1305). Le gestionnaire peut répondre avec un message Retry en utilisant les valeurs trouvées dans l'en-tête du message Session Request.

#### KDF pour ChainKey initial

Il y a trois instances de chiffrement authentifié distinctes (CipherStates). Une pendant la phase d'établissement de connexion, et deux (transmission et réception) pour la phase de données. Chacune a sa propre clé provenant d'un KDF.

Les données chiffrées/authentifiées seront représentées comme

### Chiffrement authentifié

Format de données chiffré et authentifié.

- L'en-tête du message
- Pour Session Request et Session Created uniquement, une clé éphémère
- Une charge utile chiffrée ChaCha20
- Un MAC Poly1305

Entrées pour les fonctions de chiffrement/déchiffrement :

- Pour les messages de handshake Session Request, Session Created et Session Confirmed, l'en-tête du message est traité par mixHash() avant la phase de traitement Noise
- La clé éphémère, si présente, est couverte par un misHash() Noise standard
- Pour les messages en dehors du handshake Noise, l'en-tête est utilisé comme données associées pour le chiffrement ChaCha20/Poly1305.

Sortie de la fonction de chiffrement, entrée de la fonction de déchiffrement :

### KDF pour Session Request

Pour ChaCha20, ce qui est décrit ici correspond à [RFC-7539](https://tools.ietf.org/html/rfc7539), qui est également utilisé de manière similaire dans TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).

La fonction de dérivation de clé (KDF) génère une clé de chiffrement k pour la phase de négociation à partir du résultat DH, en utilisant HMAC-SHA256(key, data) tel que défini dans [RFC-2104](https://tools.ietf.org/html/rfc2104). Il s'agit des fonctions InitializeSymmetric(), MixHash(), et MixKey(), exactement telles que définies dans la spécification Noise.

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   Encrypted and authenticated data    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
```
#### KDF pour la Requête de Session

Alice envoie à Bob, soit comme premier message dans la négociation, soit en réponse à un message Retry. Bob répond avec un message Session Created. Taille : 80 + taille de la charge utile. Taille minimale : 88

Si Alice n'a pas de jeton valide, Alice devrait envoyer un message Token Request au lieu d'un Session Request, pour éviter la surcharge de chiffrement asymétrique lors de la génération d'un Session Request.

```
k :: 32 byte cipher key, as generated from KDF

nonce :: Counter-based nonce, 12 bytes.
         Starts at 0 and incremented for each message.
         First four bytes are always zero.
         Last eight bytes are the counter, little-endian encoded.
         Maximum value is 2**64 - 2.
         Connection must be dropped and restarted after
         it reaches that value.
         The value 2**64 - 1 must never be sent.

ad :: In handshake phase:
      Associated data, 32 bytes.
      The SHA256 hash of all preceding data.
      In data phase:
      The packet header, 16 bytes.

data :: Plaintext data, 0 or more bytes
```
En-tête long. Contenu Noise : clé éphémère X d'Alice Charge utile Noise : DateTime et autres blocs Taille maximale de charge utile : MTU - 108 (IPv4) ou MTU - 128 (IPv6). Pour MTU 1280 : Charge utile maximale est 1172 (IPv4) ou 1152 (IPv6). Pour MTU 1500 : Charge utile maximale est 1392 (IPv4) ou 1372 (IPv6).

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|       ChaCha20 encrypted data         |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|  Poly1305 Message Authentication Code |
+              (MAC)                    +
|             16 bytes                  |
+----+----+----+----+----+----+----+----+

encrypted data :: Same size as plaintext data, 0 - 65519 bytes

MAC :: Poly1305 message authentication code, 16 bytes
```
Propriétés de sécurité de la charge utile :

#### Charge utile

- Puisque ChaCha20 est un chiffrement par flux, les textes en clair n'ont pas besoin d'être rembourrés. Les octets supplémentaires du flux de clés sont supprimés.
- La clé pour le chiffrement (256 bits) est convenue au moyen du SHA256 KDF. Les détails du KDF pour chaque message sont dans des sections séparées ci-dessous.

#### Notes

- Dans tous les messages, la taille du message AEAD est connue à l'avance. En cas d'échec d'authentification AEAD, le destinataire doit arrêter le traitement ultérieur du message et ignorer le message.
- Bob devrait maintenir une liste noire des adresses IP avec des échecs répétés.

### SessionRequest (Type 0)

La valeur X est chiffrée pour garantir l'indiscernabilité et l'unicité de la charge utile, qui sont des contre-mesures DPI nécessaires. Nous utilisons le chiffrement ChaCha20 pour y parvenir, plutôt que des alternatives plus complexes et plus lentes comme elligator2. Le chiffrement asymétrique avec la clé publique du router de Bob serait beaucoup trop lent. Le chiffrement ChaCha20 utilise la clé d'introduction de Bob telle que publiée dans la netDb.

#### Charge utile

```
// Define protocol_name.
Set protocol_name = "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256"
 (52 bytes, US-ASCII encoded, no NULL termination).

// Define Hash h = 32 bytes
h = SHA256(protocol_name);

Define ck = 32 byte chaining key. Copy the h data to ck.
Set ck = h

// MixHash(null prologue)
h = SHA256(h);

// up until here, can all be precalculated by Alice for all outgoing connections

// Bob's X25519 static keys
// bpk is published in routerinfo
bsk = GENERATE_PRIVATE()
bpk = DERIVE_PUBLIC(bsk)

// Bob static key
// MixHash(bpk)
// || below means append
h = SHA256(h || bpk);

// Bob introduction key
// bik is published in routerinfo
bik = RANDOM(32)

// up until here, can all be precalculated by Bob for all incoming connections
```
#### Notes

```
// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Alice's X25519 ephemeral keys
aesk = GENERATE_PRIVATE()
aepk = DERIVE_PUBLIC(aesk)

// Alice ephemeral key X
// MixHash(aepk)
h = SHA256(h || aepk);

// h is used as the associated data for the AEAD in Session Request
// Retain the Hash h for the Session Created KDF


End of "e" message pattern.

This is the "es" message pattern:

// DH(e, rs) == DH(s, re)
sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
// ChaChaPoly parameters to encrypt/decrypt
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chainKey for Session Created KDF


End of "es" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2 = bik

// Header encryption keys for next message (Session Created)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessCreateHeader", 32)

// Header encryption keys for next message (Retry)
k_header_1 = bik
k_header_2 = bik
```
### KDF pour Session Created et Session Confirmed partie 1

Le chiffrement ChaCha20 ne sert qu'à la résistance à l'inspection approfondie des paquets (DPI). Toute partie connaissant la clé d'introduction de Bob, qui est publiée dans la base de données réseau, peut déchiffrer l'en-tête et la valeur X de ce message.

Contenu brut :

Données non chiffrées (tag d'authentification Poly1305 non affiché) :

La taille minimale de la charge utile est de 8 octets. Puisque le bloc DateTime ne fait que 7 octets, au moins un autre bloc doit être présent.

```
XK(s, rs):           Authentication   Confidentiality
  -> e, es                  0                2

  Authentication: None (0).
  This payload may have been sent by any party, including an active attacker.

  Confidentiality: 2.
  Encryption to a known recipient, forward secrecy for sender compromise
  only, vulnerable to replay.  This payload is encrypted based only on DHs
  involving the recipient's static key pair.  If the recipient's static
  private key is compromised, even at a later date, this payload can be
  decrypted.  This message can also be replayed, since there's no ephemeral
  contribution from the recipient.

  "e": Alice generates a new ephemeral key pair and stores it in the e
       variable, writes the ephemeral public key as cleartext into the
       message buffer, and hashes the public key along with the old h to
       derive a new h.

  "es": A DH is performed between the Alice's ephemeral key pair and the
        Bob's static key pair.  The result is hashed along with the old ck to
        derive a new ck and k, and n is set to zero.
```
Bob envoie à Alice, en réponse à un message Session Request. Alice répond avec un message Session Confirmed. Taille : 80 + taille de la charge utile. Taille minimale : 88

Contenu Noise : clé éphémère Y de Bob Charge utile Noise : blocs DateTime, Address et autres Taille maximale de charge utile : MTU - 108 (IPv4) ou MTU - 128 (IPv6). Pour MTU 1280 : charge utile maximale est 1172 (IPv4) ou 1152 (IPv6). Pour MTU 1500 : charge utile maximale est 1392 (IPv4) ou 1372 (IPv6).

Propriétés de sécurité de la charge utile :

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|    See Header Encryption KDF          |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key n=0     +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+       X, ChaCha20 encrypted           +
|       with Bob intro key n=0          |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|  k defined in KDF for Session Request |
+  n = 0                                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

X :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted X)
```
La valeur Y est chiffrée pour garantir l'indiscernabilité et l'unicité de la charge utile, qui sont des contre-mesures DPI nécessaires. Nous utilisons le chiffrement ChaCha20 pour y parvenir, plutôt que des alternatives plus complexes et plus lentes telles qu'elligator2. Le chiffrement asymétrique avec la clé publique du router d'Alice serait bien trop lent. Le chiffrement ChaCha20 utilise la clé d'introduction de Bob, telle que publiée dans la base de données réseau.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                   X                   |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|     see below for allowed blocks      |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 0

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Alice, ignored

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: 0 if not previously received from Bob

X :: 32 bytes, X25519 ephemeral key, little endian
```
#### Problèmes

- Bloc DateTime
- Bloc Options (optionnel)
- Bloc Relay Tag Request (optionnel)
- Bloc Padding (optionnel)

Le chiffrement ChaCha20 n'est que pour la résistance à la DPI. Toute partie connaissant la clé d'intro de Bob, qui est publiée dans la base de données réseau, et ayant capturé les 32 premiers octets de la Session Request, peut déchiffrer la valeur Y dans ce message.

#### Charge utile

- La valeur X unique dans le bloc ChaCha20 initial garantit que le texte chiffré est différent pour chaque session.
- Pour fournir une résistance au sondage, Bob ne devrait pas envoyer un message Retry en réponse à un message Session Request à moins que le type de message, la version du protocole, et les champs d'ID réseau dans le message Session Request ne soient valides.
- Bob doit rejeter les connexions où la valeur d'horodatage est trop éloignée de l'heure actuelle. Appelons le delta de temps maximum "D". Bob doit maintenir un cache local des valeurs de handshake précédemment utilisées et rejeter les doublons, pour prévenir les attaques par rejeu. Les valeurs dans le cache doivent avoir une durée de vie d'au moins 2*D. Les valeurs du cache dépendent de l'implémentation, cependant la valeur X de 32 octets (ou son équivalent chiffré) peut être utilisée. Rejeter en envoyant un message Retry contenant un token zéro et un bloc de terminaison.
- Les clés éphémères Diffie-Hellman ne peuvent jamais être réutilisées, pour prévenir les attaques cryptographiques, et la réutilisation sera rejetée comme une attaque par rejeu.
- Les options "KE" et "auth" doivent être compatibles, c'est-à-dire que le secret partagé K doit être de la taille appropriée. Si davantage d'options "auth" sont ajoutées, cela pourrait implicitement changer la signification du flag "KE" pour utiliser un KDF différent ou une taille de troncature différente.
- Bob doit valider que la clé éphémère d'Alice est un point valide sur la courbe ici.
- Le padding devrait être limité à une quantité raisonnable. Bob peut rejeter les connexions avec un padding excessif. Bob spécifiera ses options de padding dans Session Created. Directives min/max à déterminer. Taille aléatoire de 0 à 31 octets minimum ? (Distribution à déterminer, voir Annexe A.)
- Sur la plupart des erreurs, incluant AEAD, DH, rejeu apparent, ou échec de validation de clé, Bob devrait arrêter le traitement ultérieur des messages et abandonner le message sans répondre.
- Bob PEUT envoyer un message Retry contenant un token zéro et un bloc Termination avec un code de raison de décalage d'horloge si l'horodatage dans le bloc DateTime est trop décalé.
- Atténuation DoS : DH est une opération relativement coûteuse. Comme avec le protocole NTCP précédent, les routeurs devraient prendre toutes les mesures nécessaires pour prévenir l'épuisement du CPU ou des connexions. Placer des limites sur les connexions actives maximales et les configurations de connexion maximales en cours. Appliquer des timeouts de lecture (à la fois par lecture et total pour "slowloris"). Limiter les connexions répétées ou simultanées de la même source. Maintenir des listes noires pour les sources qui échouent répétitivement. Ne pas répondre aux échecs AEAD. Alternativement, répondre avec un message Retry avant l'opération DH et la validation AEAD.
- Champ "ver" : Le protocole Noise global, les extensions, et le protocole SSU2 incluant les spécifications de payload, indiquant SSU2. Ce champ peut être utilisé pour indiquer le support de futurs changements.
- Le champ d'ID réseau est utilisé pour identifier rapidement les connexions inter-réseaux. Si ce champ ne correspond pas à l'ID réseau de Bob, Bob devrait se déconnecter et bloquer les futures connexions.
- Bob doit abandonner le message si l'ID de Connexion Source égale l'ID de Connexion de Destination.

### SessionCreated (Type 1)

```
// take h saved from Session Request KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Request)

// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Bob's X25519 ephemeral keys
besk = GENERATE_PRIVATE()
bepk = DERIVE_PUBLIC(besk)

// h is from KDF for Session Request
// Bob ephemeral key Y
// MixHash(bepk)
h = SHA256(h || bepk);

// h is used as the associated data for the AEAD in Session Created
// Retain the Hash h for the Session Confirmed KDF

End of "e" message pattern.

This is the "ee" message pattern:

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chaining key ck for Session Confirmed KDF

End of "ee" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Request KDF above

// Header protection keys for next message (Session Confirmed)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessionConfirmed", 32)
```
### KDF pour la partie 1 de Session Confirmed, utilisant le KDF de Session Created

Contenu brut :

Données non chiffrées (tag d'authentification Poly1305 non affiché) :

La taille minimale de la charge utile est de 8 octets. Puisque les blocs DateTime et Address totalisent plus que cela, l'exigence est satisfaite avec seulement ces deux blocs.

```
XK(s, rs):           Authentication   Confidentiality
  <- e, ee                  2                1

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 1.
  Encryption to an ephemeral recipient.
  This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee").
  However, the sender has not authenticated the recipient,
  so this payload might be sent to any party, including an active attacker.


  "e": Bob generates a new ephemeral key pair and stores it in the e variable,
  writes the ephemeral public key as cleartext into the message buffer,
  and hashes the public key along with the old h to derive a new h.

  "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair.
  The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Alice envoie à Bob, en réponse à un message Session Created. Bob répond immédiatement avec un message Data contenant un bloc ACK. Taille : 80 + taille de la charge utile. Taille minimale : Environ 500 (la taille minimale du bloc d'informations du routeur est d'environ 420 octets)

Contenu Noise : clé statique d'Alice Partie 1 de la charge utile Noise : Aucune Partie 2 de la charge utile Noise : RouterInfo d'Alice, et autres blocs Taille maximale de charge utile : MTU - 108 (IPv4) ou MTU - 128 (IPv6). Pour MTU 1280 : Charge utile maximale est 1172 (IPv4) ou 1152 (IPv6). Pour MTU 1500 : Charge utile maximale est 1392 (IPv4) ou 1372 (IPv6).

Propriétés de sécurité de la charge utile :

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with derived key n=0       +
|  See Header Encryption KDF            |
+----+----+----+----+----+----+----+----+
|                                       |
+       Y, ChaCha20 encrypted           +
|       with derived key n=0            |
+              (32 bytes)               +
|       See Header Encryption KDF       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in KDF for Session Created +
|  n = 0; see KDF for associated data   |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

Y :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted Y)
```
Cela contient deux trames ChaChaPoly. La première est la clé publique statique chiffrée d'Alice. La seconde est la charge utile Noise : la RouterInfo chiffrée d'Alice, les options facultatives et le remplissage facultatif. Elles utilisent des clés différentes, car la fonction MixKey() est appelée entre les deux.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                  Y                    |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|      see below for allowed blocks     |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: The Source Connection ID
                             received from Alice in Session Request

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 1

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Bob, ignored

Source Connection ID :: The Destination Connection ID
                        received from Alice in Session Request

Token :: 0 (unused)

Y :: 32 bytes, X25519 ephemeral key, little endian
```
#### Notes

- Bloc DateTime
- Bloc Address
- Bloc Relay Tag (optionnel)
- Bloc New Token (non recommandé, voir note)
- Bloc First Packet Number (optionnel)
- Bloc Options (optionnel)
- Bloc Termination (non recommandé, envoyer dans un message de nouvelle tentative à la place)
- Bloc Padding (optionnel)

Contenu brut :

#### Fragmentation de Session Confirmée

- Alice doit valider que la clé éphémère de Bob est un point valide sur la courbe ici.
- Le padding devrait être limité à une quantité raisonnable. Alice peut rejeter les connexions avec un padding excessif. Alice spécifiera ses options de padding dans Session Confirmed. Directives min/max à déterminer. Taille aléatoire de 0 à 31 octets minimum ? (Distribution à déterminer, voir Annexe A.)
- En cas d'erreur, y compris AEAD, DH, timestamp, rejeu apparent, ou échec de validation de clé, Alice doit arrêter tout traitement de message ultérieur et fermer la connexion sans répondre.
- Alice doit rejeter les connexions où la valeur timestamp est trop éloignée de l'heure actuelle. Appelons le delta temps maximum "D". Alice doit maintenir un cache local des valeurs de handshake précédemment utilisées et rejeter les doublons, pour prévenir les attaques par rejeu. Les valeurs dans le cache doivent avoir une durée de vie d'au moins 2*D. Les valeurs du cache dépendent de l'implémentation, cependant la valeur Y de 32 octets (ou son équivalent chiffré) peut être utilisée.
- Alice doit abandonner le message si l'IP et le port source ne correspondent pas à l'IP et au port de destination de la Session Request.
- Alice doit abandonner le message si les ID de Connexion Destination et Source ne correspondent pas aux ID de Connexion Source et Destination de la Session Request.
- Bob envoie un bloc relay tag s'il est demandé par Alice dans la Session Request.
- Le bloc New Token n'est pas recommandé dans Session Created, car Bob devrait d'abord faire la validation du Session Confirmed. Voir la section Tokens ci-dessous.

#### Notes

- Inclure les options de remplissage min/max ici ?

### KDF pour la partie 2 de Session Confirmed

```
// take h saved from Session Created KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Created)

// MixHash(header)
h = SHA256(h || header)
// h is used as the associated data for the AEAD in Session Confirmed part 1, below

This is the "s" message pattern:

// Alice's X25519 static keys
ask = GENERATE_PRIVATE()
apk = DERIVE_PUBLIC(ask)

// AEAD parameters
// k is from Session Request
n = 1
ad = h
ciphertext = ENCRYPT(k, n++, apk, ad)

// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// h is used as the associated data for the AEAD in Session Confirmed part 2

End of "s" message pattern.

// Header encryption keys for this message
See Session Confirmed part 2 below
```
### SessionConfirmed (Type 2)

```
This is the "se" message pattern:

// DH(ask, bepk) == DH(besk, apk)
sharedSecret = DH(ask, bepk) = DH(besk, apk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// h from Session Confirmed part 1 is used as the associated data for the AEAD in Session Confirmed part 2
// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF
// retain the hash h for the data phase KDF

End of "se" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Created KDF above

// Header protection keys for data phase
See data phase KDF below
```
### KDF pour la phase de données

Données non chiffrées (tags d'authentification Poly1305 non affichés) :

La taille minimale de la charge utile est de 8 octets. Étant donné que le bloc RouterInfo sera bien supérieur à cette taille, l'exigence est satisfaite avec seulement ce bloc.

1)  Bloc d'informations du router d'Alice (requis)   2)  Bloc d'options (facultatif)   3)  Blocs I2NP (facultatifs)

```
XK(s, rs):           Authentication   Confidentiality
  -> s, se                  2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).  The
  sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key
  pair.  Assuming the corresponding private keys are secure, this
  authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.  This payload is
  encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static
  DH with the recipient's static key pair.  Assuming the ephemeral private
  keys are secure, and the recipient is not being actively impersonated by an
  attacker that has stolen its static private key, this payload cannot be
  decrypted.

  "s": Alice writes her static public key from the s variable into the
  message buffer, encrypting it, and hashes the output along with the old h
  to derive a new h.

  "se": A DH is performed between the Alice's static key pair and the Bob's
  ephemeral key pair.  The result is hashed along with the old ck to derive a
  new ck and k, and n is set to zero.
```
4\) Bloc de remplissage (optionnel) Cette trame ne doit jamais contenir d'autre type de bloc. TODO : qu'en est-il du relais et du test de pair ?

Le message Session Confirmed doit contenir les informations complètes signées du router d'Alice afin que Bob puisse effectuer plusieurs vérifications requises :

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|   ChaCha20 encrypted data (32 bytes)  |
+   Encrypted and authenticated data    +
+   Alice static key S                  +
| k defined in KDF for Session Created  |
+     n = 1                             +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+ Length varies (remainder of packet)   +
|                                       |
+   ChaCha20 encrypted data             +
|   see below for allowed blocks        |
+     k defined in KDF for              +
|     Session Confirmed part 2          |
+     n = 0                             +
|     see KDF for associated data       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, ChaCha20 encrypted Alice's X25519 static key, little endian
     inside 48 byte ChaChaPoly frame
```
Malheureusement, les informations du Router Info, même lorsqu'elles sont compressées avec gzip dans le bloc RI, peuvent dépasser le MTU. Par conséquent, le Session Confirmed peut être fragmenté sur deux paquets ou plus. C'est le SEUL cas dans le protocole SSU2 où une charge utile protégée par AEAD est fragmentée sur deux paquets ou plus.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|              S                        |
+       Alice static key                +
|          (32 bytes)                   |
+                                       +
|                                       |
+                                       +
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|        Noise Payload                  |
+        (length varies)                +
|        see below for allowed blocks   |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As sent in Session Request,
                             or one received in Session Confirmed?

Packet Number :: 0 always, for all fragments, even if retransmitted

type :: 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility

S :: 32 bytes, Alice's X25519 static key, little endian
```
#### Notes

- Bloc RouterInfo (doit être le premier bloc)
- Bloc Options (optionnel)
- Bloc New Token (optionnel)
- Bloc Relay Request (optionnel)
- Bloc Peer Test (optionnel)
- Bloc First Packet Number (optionnel)
- Blocs I2NP, First Fragment, ou Follow-on Fragment (optionnels, mais probablement pas de place)
- Bloc Padding (optionnel)

Les en-têtes de chaque paquet sont construits comme suit :

#### Charge utile

- Bob doit effectuer la validation habituelle des Router Info. S'assurer que le type de signature est pris en charge, vérifier la signature, vérifier que l'horodatage est dans les limites acceptables, et toute autre vérification nécessaire. Voir ci-dessous les notes sur la gestion des Router Info fragmentées.

- Bob doit vérifier que la clé statique d'Alice reçue dans la première trame correspond à la clé statique dans le Router Info. Bob doit d'abord rechercher dans le Router Info une adresse de routeur NTCP ou SSU2 avec une option de version (v) correspondante. Voir les sections Router Info publié et Router Info non publié ci-dessous. Voir ci-dessous pour les notes sur la gestion des Router Infos fragmentés.

- Si Bob a une version plus ancienne du RouterInfo d'Alice dans sa netdb, vérifier que la clé statique dans les informations du router est la même dans les deux, si présente, et si la version plus ancienne a moins de XXX (voir le temps de rotation des clés ci-dessous)

- Bob doit valider que la clé statique d'Alice est un point valide sur la courbe ici.

- Les options doivent être incluses pour spécifier les paramètres de remplissage.

- En cas d'erreur, y compris l'échec de validation AEAD, RI, DH, horodatage, ou clé, Bob doit arrêter le traitement des messages et fermer la connexion sans répondre.

- Contenu de la trame partie 2 du message 3 : Le format de cette trame est identique au format des trames de la phase de données, sauf que la longueur de la trame est envoyée par Alice dans la Session Request. Voir ci-dessous pour le format des trames de la phase de données. La trame doit contenir 1 à 4 blocs dans l'ordre suivant :

Construisez la série de paquets comme suit :

Processus de réassemblage :

- Le bloc de remplissage de la partie 2 du message 3 est recommandé.

- Il peut n'y avoir aucun espace, ou seulement un petit espace disponible, pour les blocs I2NP, selon la MTU et la taille du Router Info. N'incluez PAS de blocs I2NP si le Router Info est fragmenté. L'implémentation la plus simple pourrait être de ne jamais inclure de blocs I2NP dans le message Session Confirmed, et d'envoyer tous les blocs I2NP dans les messages Data suivants. Voir la section bloc Router Info ci-dessous pour la taille maximale des blocs.

#### Charge utile

Lorsque Bob reçoit un message Session Confirmed, il déchiffre l'en-tête, inspecte le champ frag, et détermine que le Session Confirmed est fragmenté. Il ne déchiffre pas (et ne peut pas déchiffrer) le message tant que tous les fragments ne sont pas reçus et réassemblés.

- La clé statique "s" dans le RI correspond à la clé statique dans le handshake
- La clé d'introduction "i" dans le RI doit être extraite et valide, pour être utilisée dans la phase de données
- La signature RI est valide

Il n'y a aucun mécanisme pour que Bob acquitte des fragments individuels. Lorsque Bob reçoit tous les fragments, les réassemble, les déchiffre et valide le contenu, Bob effectue un split() comme d'habitude, entre dans la phase de données et envoie un ACK du paquet numéro 0.

Si Alice ne reçoit pas d'ACK du paquet numéro 0, elle doit retransmettre tous les paquets de session confirmée tels quels.

- Tous les en-têtes sont des en-têtes courts avec le même numéro de paquet 0
- Tous les en-têtes sont de type = 2 (session confirmée)
- Tous les en-têtes contiennent un champ « frag », indiquant le numéro de fragment et le nombre total de fragments
- L'en-tête non chiffré du fragment 0 constitue les données associées (AD) pour le message « jumbo »
- Chaque en-tête est chiffré à l'aide des 24 derniers octets de données de CE paquet

Exemples :

- Créer un seul bloc RI (fragment 0 de 1 dans le champ frag du bloc RI). Nous n'utilisons pas la fragmentation de bloc RI, c'était pour une méthode alternative de résoudre le même problème.
- Créer une charge utile "jumbo" avec le bloc RI et tous les autres blocs à inclure
- Calculer la taille totale des données (sans inclure l'en-tête), qui est la taille de la charge utile + 64 octets pour la clé statique et les deux MAC
- Calculer l'espace disponible dans chaque paquet, qui est le MTU moins l'en-tête IP (20 ou 40), moins l'en-tête UDP (8), moins l'en-tête court SSU2 (16). La surcharge totale par paquet est de 44 (IPv4) ou 64 (IPv6).
- Calculer le nombre de paquets.
- Calculer la taille des données dans le dernier paquet. Elle doit être supérieure ou égale à 24 octets, pour que le chiffrement d'en-tête fonctionne. Si elle est trop petite, soit ajouter un bloc de remplissage, OU augmenter la taille du bloc de remplissage s'il est déjà présent, OU réduire la taille de l'un des autres paquets pour que le dernier paquet soit assez grand.
- Créer l'en-tête non chiffré pour le premier paquet, avec le nombre total de fragments dans le champ frag, et chiffrer la charge utile "jumbo" avec Noise, en utilisant l'en-tête comme AD, comme d'habitude.
- Diviser le paquet jumbo chiffré en fragments
- Ajouter un en-tête non chiffré pour chaque fragment 1-n
- Chiffrer l'en-tête pour chaque fragment 0-n. Chaque en-tête utilise les MÊMES k_header_1 et k_header_2 tels que définis ci-dessus dans le KDF Session Confirmed.
- Transmettre tous les fragments

Pour un MTU de 1500 sur IPv6, la charge utile maximale est de 1372, la surcharge du bloc RI est de 5, la taille maximale des données RI (compressées gzip) est de 1367 (en supposant aucun autre bloc). Avec deux paquets, la surcharge du 2ème paquet est de 64, il peut donc contenir 1436 octets supplémentaires de charge utile. Ainsi, deux paquets suffisent pour un RI compressé jusqu'à 2803 octets.

Le plus grand RI compressé observé dans le réseau actuel fait environ 1400 octets ; par conséquent, en pratique, deux fragments devraient suffire, même avec un MTU minimum de 1280. Le protocole autorise un maximum de 15 fragments.

- Préserver l'en-tête du fragment 0, car il est utilisé comme Noise AD
- Rejeter les en-têtes des autres fragments avant le réassemblage
- Réassembler la charge utile "jumbo", avec l'en-tête du fragment 0 comme AD, et déchiffrer avec Noise
- Valider le bloc RI comme d'habitude
- Passer à la phase de données et envoyer ACK 0, comme d'habitude

Analyse de sécurité :

L'intégrité et la sécurité d'un Session Confirmed fragmenté sont identiques à celles d'un non fragmenté. Toute altération de n'importe quel fragment entraînera l'échec du Noise AEAD après le réassemblage. Les en-têtes des fragments après le fragment 0 ne sont utilisés que pour identifier le fragment. Même si un attaquant sur le chemin avait la clé k_header_2 utilisée pour chiffrer l'en-tête (peu probable, dérivée de la négociation), cela ne permettrait pas à l'attaquant de substituer un fragment valide.

La phase de données utilise l'en-tête pour les données associées.

Le KDF génère deux clés de chiffrement k_ab et k_ba à partir de la clé de chaînage ck, en utilisant HMAC-SHA256(key, data) tel que défini dans [RFC-2104](https://tools.ietf.org/html/rfc2104). Il s'agit de la fonction split(), exactement comme définie dans la spécification Noise.

Charge utile Noise : Tous les types de blocs sont autorisés Taille maximale de charge utile : MTU - 60 (IPv4) ou MTU - 80 (IPv6). Pour MTU 1500 : La charge utile maximale est 1440 (IPv4) ou 1420 (IPv6).

À partir de la 2ème partie de Session Confirmed, tous les messages sont à l'intérieur d'une charge utile ChaChaPoly authentifiée et chiffrée. Tout le rembourrage est à l'intérieur du message. À l'intérieur de la charge utile se trouve un format standard avec zéro ou plusieurs "blocs". Chaque bloc a un type d'un octet et une longueur de deux octets. Les types incluent date/heure, message I2NP, options, terminaison, et rembourrage.

Note : Bob peut, mais n'est pas obligé d'envoyer ses RouterInfo à Alice comme premier message à Alice dans la phase de données.

### Message de données (Type 6)

Propriétés de sécurité de la charge utile :

Données non chiffrées (tag d'authentification Poly1305 non affiché) :

```
// split()
// chainKey = from handshake phase
keydata = HKDF(chainKey, ZEROLEN, "", 64)
k_ab = keydata[0:31]
k_ba = keydata[32:63]

// key is k_ab for Alice to Bob
// key is k_ba for Bob to Alice

keydata = HKDF(key, ZEROLEN, "HKDFSSU2DataKeys", 64)
k_data = keydata[0:31]
k_header_2 = keydata[32:63]


// AEAD parameters
k = k_data
n = 4 byte packet number from header
ad = 16 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for data phase
// aik = Alice's intro key
// bik = Bob's intro key
k_header_1 = Receiver's intro key (aik or bik)
k_header_2: from above
```
### KDF pour le test de pair

Charlie envoie à Alice, et Alice envoie à Charlie, uniquement pour les phases 5-7 du Peer Test. Les phases 1-4 du Peer Test doivent être envoyées en session en utilisant un bloc Peer Test dans un message Data. Voir les sections Bloc Peer Test et Processus Peer Test ci-dessous pour plus d'informations.

Taille : 48 + taille de la charge utile.

Charge utile Noise : Voir ci-dessous.

Contenu brut :

```
XK(s, rs):           Authentication   Confidentiality
  <-                        2                5
  ->                        2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.
  This payload is encrypted based on an ephemeral-ephemeral DH as well as
  an ephemeral-static DH with the recipient's static key pair.
  Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated
  by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### Notes

- Le router doit abandonner un message avec une erreur AEAD.

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with intro key and         +
|  derived key, see Data Phase KDF      |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in Data Phase KDF          +
|  n = packet number from header        |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Données non chiffrées (étiquette d'authentification Poly1305 non affichée) :

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: See below

Packet Number :: Random number generated by Charlie

type :: 11

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: See below

Token :: 8 byte unsigned integer, randomly generated by Charlie, nonzero.
```
#### Charge utile

- La taille minimale de la charge utile est de 8 octets. Cette exigence sera satisfaite par tout bloc ACK, I2NP, Premier Fragment ou Fragment de Suite. Si l'exigence n'est pas satisfaite, un bloc de Remplissage doit être inclus.
- Chaque numéro de paquet ne peut être utilisé qu'une seule fois. Lors de la retransmission de messages I2NP ou de fragments, un nouveau numéro de paquet doit être utilisé.

### Test de pair (Type 7)

```
// AEAD parameters
// aik = Alice's intro key
k = aik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = aik
k_header_2 = aik
```
### KDF pour Retry

La taille minimale de la charge utile est de 8 octets. Puisque le bloc Peer Test totalise plus que cela, l'exigence est satisfaite avec seulement ce bloc.

Dans les messages 5 et 7, le bloc Peer Test peut être identique au bloc des messages de session 3 et 4, contenant l'accord signé par Charlie, ou il peut être régénéré. La signature est facultative.

Dans le message 6, le bloc Peer Test peut être identique au bloc des messages de session 1 et 2, contenant la demande signée par Alice, ou il peut être régénéré. La signature est optionnelle.

IDs de connexion : Les deux IDs de connexion sont dérivés du nonce de test. Pour les messages 5 et 7 envoyés de Charlie vers Alice, l'ID de connexion de destination est deux copies du nonce de test de 4 octets en big-endian, c'est-à-dire ((nonce << 32) | nonce). L'ID de connexion source est l'inverse de l'ID de connexion de destination, c'est-à-dire ~((nonce << 32) | nonce). Pour le message 6 envoyé d'Alice vers Charlie, échangez les deux IDs de connexion.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Contenu du bloc d'adresse :

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

Packet Number :: Random number generated by Alice

type :: 10

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: zero
```
#### Notes

- Bloc DateTime
- Bloc Address (requis pour les messages 6 et 7, voir note ci-dessous)
- Bloc Peer Test
- Bloc Padding (optionnel)

L'exigence pour le message Retry est que Bob n'est pas tenu de déchiffrer le message Session Request pour générer un message Retry en réponse. De plus, ce message doit être rapide à générer, en utilisant uniquement le chiffrement symétrique.

Bob envoie à Alice, en réponse à un message Session Request ou Token Request. Alice répond avec une nouvelle Session Request. Taille : 48 + taille de la charge utile.

Sert également de message de Terminaison (c'est-à-dire, "Ne pas réessayer") si un bloc de Terminaison est inclus.

Charge utile Noise : Voir ci-dessous.

Contenu brut :

- Dans le message 5 : Non requis.
- Dans le message 6 : L'IP et le port de Charlie tels que sélectionnés depuis le RI de Charlie.
- Dans le message 7 : L'IP et le port réels d'Alice depuis lesquels le message 6 a été reçu.

### Retry (Type 9)

Données non chiffrées (étiquette d'authentification Poly1305 non affichée) :

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### KDF pour la demande de jeton

La taille minimale de la charge utile est de 8 octets. Étant donné que les blocs DateTime et Address totalisent plus que cela, l'exigence est satisfaite avec seulement ces deux blocs.

Ce message doit être rapide à générer, en utilisant uniquement le chiffrement symétrique.

Alice envoie à Bob. Bob répond avec un message Retry. Taille : 48 + taille de la charge utile.

Si Alice n'a pas de jeton valide, Alice devrait envoyer ce message au lieu d'une Session Request, pour éviter la surcharge de chiffrement asymétrique lors de la génération d'une Session Request.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Charge utile Noise : Voir ci-dessous.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: The Source Connection ID
                             received from Alice in Token Request
                             or Session Request

Packet Number :: Random number generated by Bob

type :: 9

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: The Destination Connection ID
                        received from Alice in Token Request
                        or Session Request

Token :: 8 byte unsigned integer, randomly generated by Bob, nonzero,
         or zero if session is rejected and a termination block is included
```
#### Charge utile

- Bloc DateTime
- Bloc Address
- Bloc Options (optionnel)
- Bloc Termination (optionnel, si la session est rejetée)
- Bloc Padding (optionnel)

Contenu brut :

#### DateTime

- Pour fournir une résistance au sondage, un router ne devrait pas envoyer un message Retry en réponse à un message Session Request ou Token Request à moins que les champs type de message, version de protocole et ID réseau dans le message Request ne soient valides.
- Pour limiter l'ampleur de toute attaque par amplification qui peut être montée en utilisant des adresses sources usurpées, le message Retry ne doit pas contenir de grandes quantités de rembourrage. Il est recommandé que le message Retry ne soit pas plus grand que trois fois la taille du message auquel il répond. Alternativement, utilisez une méthode simple comme ajouter une quantité aléatoire de rembourrage dans la plage de 1 à 64 octets.

### Demande de jeton (Type 10)

Données non chiffrées (tag d'authentification Poly1305 non affiché) :

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### KDF pour Hole Punch

La taille minimale de la charge utile est de 8 octets.

Ce message doit être rapide à générer, en utilisant uniquement le chiffrement symétrique.

Charlie envoie à Alice, en réponse à un Relay Intro reçu de Bob. Alice répond avec une nouvelle Session Request. Taille : 48 + taille de la charge utile.

Charge utile Noise : Voir ci-dessous.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Contenu brut :

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|    flags     |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As specified in session setup

Packet Number :: 4 byte big endian integer

type :: 6

flags :: 3 bytes, unused, set to 0 for future compatibility
```
#### Options

- Bloc DateTime
- Bloc de remplissage

Données non chiffrées (tag d'authentification Poly1305 non affiché) :

#### RouterInfo

- Pour fournir une résistance au sondage, un router ne devrait pas envoyer un message Retry en réponse à un message Token Request à moins que les champs type de message, version du protocole et ID réseau dans le message Token Request ne soient valides.
- Ceci N'EST PAS un message Noise standard et ne fait pas partie de la négociation. Il n'est pas lié au message Session Request autrement que par les ID de connexion.
- Sur la plupart des erreurs, y compris AEAD, ou une apparente rejeu, Bob devrait arrêter le traitement ultérieur des messages et abandonner le message sans répondre.
- Bob doit rejeter les connexions où la valeur timestamp est trop éloignée de l'heure actuelle. Appelons le delta de temps maximum "D". Bob doit maintenir un cache local des valeurs de négociation précédemment utilisées et rejeter les doublons, pour empêcher les attaques par rejeu. Les valeurs dans le cache doivent avoir une durée de vie d'au moins 2*D. Les valeurs de cache dépendent de l'implémentation, cependant la valeur X de 32 octets (ou son équivalent chiffré) peut être utilisée.
- Bob PEUT envoyer un message Retry contenant un token zéro et un bloc Termination avec un code de raison de décalage d'horloge si le timestamp dans le bloc DateTime est trop décalé.
- Taille minimum : TBD, mêmes règles que pour Session Created ?

### Perforation (Type 11)

La taille minimale de la charge utile est de 8 octets. Étant donné que les blocs DateTime et Address totalisent plus que cela, l'exigence est remplie avec seulement ces deux blocs.

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Format de Charge Utile

ID de connexion : Les deux ID de connexion sont dérivés du nonce de relais. L'ID de connexion de destination est constitué de deux copies du nonce de relais de 4 octets en big-endian, c'est-à-dire ((nonce << 32) | nonce). L'ID de connexion source est l'inverse de l'ID de connexion de destination, c'est-à-dire ~((nonce << 32) | nonce).

Alice devrait ignorer le token dans l'en-tête. Le token à utiliser dans la demande de session se trouve dans le bloc de réponse de relais.

Chaque charge utile Noise contient zéro ou plusieurs "blocs".

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Cela utilise le même format de bloc que celui défini dans les spécifications [NTCP2](/docs/specs/ntcp2) et [ECIES](/docs/specs/ecies). Les types de blocs individuels sont définis différemment. Le terme équivalent dans QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) est "frames".

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: See below

type :: 7

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random number generated by Alice or Charlie

Source Connection ID :: See below

Token :: Randomly generated by Alice or Charlie, ignored
```
#### Message I2NP

- Bloc DateTime
- Bloc Address
- Bloc Relay Response
- Bloc Padding (optionnel)

Il existe des préoccupations selon lesquelles encourager les implémenteurs à partager du code pourrait conduire à des problèmes d'analyse syntaxique. Les implémenteurs devraient soigneusement considérer les avantages et les risques du partage de code, et s'assurer que les règles d'ordre et de blocs valides sont différentes pour les deux contextes.

Il y a un ou plusieurs blocs dans la charge utile chiffrée. Un bloc est un format simple Tag-Length-Value (TLV). Chaque bloc contient un identifiant d'un octet, une longueur de deux octets, et zéro ou plusieurs octets de données. Ce format est identique à celui de [NTCP2](/docs/specs/ntcp2) et [ECIES](/docs/specs/ecies), cependant les définitions de blocs sont différentes.

Pour des raisons d'extensibilité, les récepteurs doivent ignorer les blocs avec des identifiants inconnus et les traiter comme du remplissage.

## Charge utile Noise

(Tag d'authentification Poly1305 non affiché) :

Le chiffrement d'en-tête utilise les 24 derniers octets du paquet comme IV pour les deux opérations ChaCha20. Comme tous les paquets se terminent par un MAC de 16 octets, cela exige que toutes les charges utiles de paquets aient un minimum de 8 octets. Si une charge utile ne respecterait pas autrement cette exigence, un bloc de bourrage doit être inclus.

La charge utile ChaChaPoly maximale varie selon le type de message, la MTU, et le type d'adresse IPv4 ou IPv6. La charge utile maximale est MTU - 60 pour IPv4 et MTU - 80 pour IPv6. Les données de charge utile maximales sont MTU - 63 pour IPv4 et MTU - 83 pour IPv6. La limite supérieure est d'environ 1440 octets pour IPv4, MTU 1500, message Data. La taille maximale totale du bloc est la taille maximale de la charge utile. La taille maximale d'un bloc unique est la taille maximale totale du bloc. Le type de bloc fait 1 octet. La longueur du bloc fait 2 octets. La taille maximale des données d'un bloc unique est la taille maximale d'un bloc unique moins 3.

### Règles d'ordonnancement des blocs

Notes :

Types de blocs :

Dans la Session Confirmed, Router Info doit être le premier bloc.

```
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
~               .   .   .               ~

blk :: 1 byte, see below
size :: 2 bytes, big endian, size of data to follow, 0 - TBD
data :: the data
```
Dans tous les autres messages, l'ordre n'est pas spécifié, sauf pour les exigences suivantes : Le Padding, s'il est présent, doit être le dernier bloc. La Termination, si elle est présente, doit être le dernier bloc sauf pour le Padding. Plusieurs blocs Padding ne sont pas autorisés dans une seule charge utile.

Pour la synchronisation temporelle :

Notes :

- Les implémenteurs doivent s'assurer que lors de la lecture d'un bloc, des données malformées ou malveillantes ne causeront pas de débordements de lecture dans le bloc suivant ou au-delà des limites de la charge utile.
- Les implémentations devraient ignorer les types de blocs inconnus pour assurer la compatibilité future.

Transmettre les options mises à jour. Les options incluent : Remplissage minimum et maximum.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Block Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Number</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Block Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Options</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15+</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Router Info</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">I2NP Message</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Follow-on Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Termination</td><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 typ.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">8</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Intro</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Next Nonce</td><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">ACK</td><td style="border:1px solid var(--color-border); padding:0.6rem;">12</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 or 21</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;">--</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">17</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Challenge</td><td style="border:1px solid var(--color-border); padding:0.6rem;">18</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">19</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Packet Number</td><td style="border:1px solid var(--color-border); padding:0.6rem;">20</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Congestion</td><td style="border:1px solid var(--color-border); padding:0.6rem;">21</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for experimental features</td><td style="border:1px solid var(--color-border); padding:0.6rem;">224-253</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Padding</td><td style="border:1px solid var(--color-border); padding:0.6rem;">254</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for future extension</td><td style="border:1px solid var(--color-border); padding:0.6rem;">255</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>           
### Spécifications des blocs

Le bloc d'options aura une longueur variable.

Problèmes d'options :

### Demande de session

#### Premier Fragment

Transmettre les RouterInfo d'Alice à Bob. Utilisé uniquement dans la charge utile de la partie 2 de Session Confirmed. Ne doit pas être utilisé pendant la phase de données ; utilisez plutôt un message I2NP DatabaseStore.

```
+----+----+----+----+----+----+----+
| 0  |    4    |     timestamp     |
+----+----+----+----+----+----+----+

blk :: 0
size :: 2 bytes, big endian, value = 4
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
```
Taille minimale : Environ 420 octets, sauf si l'identité du router et la signature dans les informations du router sont compressibles, ce qui est peu probable.

- Contrairement à SSU 1, il n'y a pas d'horodatage dans l'en-tête de paquet pour la phase de données dans SSU 2.
- Les implémentations devraient envoyer périodiquement des blocs DateTime dans la phase de données.
- Les implémentations doivent arrondir à la seconde la plus proche pour éviter le biais d'horloge dans le réseau.

#### Fragment de suite

NOTE : Le bloc Router Info n'est jamais fragmenté. Le champ frag est toujours 0/1. Voir la section Fragmentation de Session Confirmée ci-dessus pour plus d'informations.

Notes :

```
+----+----+----+----+----+----+----+----+
| 1  |  size   |tmin|tmax|rmin|rmax|tdmy|
+----+----+----+----+----+----+----+----+
|tdmy|  rdmy   |  tdelay |  rdelay |    |
~----+----+----+----+----+----+----+    ~
|              more_options             |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 1
size :: 2 bytes, big endian, size of options to follow, 12 bytes minimum

tmin, tmax, rmin, rmax :: requested padding limits
    tmin and rmin are for desired resistance to traffic analysis.
    tmax and rmax are for bandwidth limits.
    tmin and tmax are the transmit limits for the router sending this options block.
    rmin and rmax are the receive limits for the router sending this options block.
    Each is a 4.4 fixed-point float representing 0 to 15.9375
    (or think of it as an unsigned 8-bit integer divided by 16.0).
    This is the ratio of padding to data. Examples:
    Value of 0x00 means no padding
    Value of 0x01 means add 6 percent padding
    Value of 0x10 means add 100 percent padding
    Value of 0x80 means add 800 percent (8x) padding
    Alice and Bob will negotiate the minimum and maximum in each direction.
    These are guidelines, there is no enforcement.
    Sender should honor receiver's maximum.
    Sender may or may not honor receiver's minimum, within bandwidth constraints.

tdmy: Max dummy traffic willing to send, 2 bytes big endian, bytes/sec average
rdmy: Requested dummy traffic, 2 bytes big endian, bytes/sec average
tdelay: Max intra-message delay willing to insert, 2 bytes big endian, msec average
rdelay: Requested intra-message delay, 2 bytes big endian, msec average

Padding distribution specified as additional parameters?
Random delay specified as additional parameters?

more_options :: Format TBD
```
Un message I2NP complet avec un en-tête modifié.

- La négociation des options est à définir.

#### Terminaison

Ceci utilise les mêmes 9 octets pour l'en-tête I2NP que dans [NTCP2](/docs/specs/ntcp2) (type, identifiant de message, expiration courte).

Notes :

Le premier fragment (fragment n°0) d'un message I2NP avec un en-tête modifié.

```
+----+----+----+----+----+----+----+----+
| 2  |  size   |flag|frag|              |
+----+----+----+----+----+              +
|                                       |
+       Router Info fragment            +
| (Alice RI in Session Confirmed)       |
+ (Alice, Bob, or third-party           +
|  RI in data phase)                    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 2
size :: 2 bytes, big endian, 2 + fragment size
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 0 for local store, 1 for flood request
       bit 1: 0 for uncompressed, 1 for gzip compressed
       bits 7-2: Unused, set to 0 for future compatibility
frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number, always 0
       bits 3-0: total fragments, always 1, big endian

routerinfo :: Alice's or Bob's RouterInfo
```
Ceci utilise les mêmes 9 octets pour l'en-tête I2NP que dans [NTCP2](/docs/specs/ntcp2) (type, identifiant de message, expiration courte).

- Le Router Info est optionnellement compressé avec gzip, comme indiqué par le bit de flag 1. Ceci diffère de NTCP2, où il n'est jamais compressé, et d'un message DatabaseStore, où il est toujours compressé. La compression est optionnelle car elle apporte généralement peu d'avantages pour les petits Router Infos, où il y a peu de contenu compressible, mais elle est très bénéfique pour les gros Router Infos avec plusieurs Router Addresses compressibles. La compression est recommandée si elle permet à un Router Info de tenir dans un seul paquet Session Confirmed sans fragmentation.
- Taille maximale du premier ou unique fragment dans le message Session Confirmed : MTU - 113 pour IPv4 ou MTU - 133 pour IPv6. En supposant une MTU par défaut de 1500 octets, et aucun autre bloc dans le message, 1387 pour IPv4 ou 1367 pour IPv6. 97% des router infos actuels sont plus petits que 1367 sans gzipping. 99,9% des router infos actuels sont plus petits que 1367 quand ils sont gzippés. En supposant une MTU minimale de 1280 octets, et aucun autre bloc dans le message, 1167 pour IPv4 ou 1147 pour IPv6. 94% des router infos actuels sont plus petits que 1147 sans gzipping. 97% des router infos actuels sont plus petits que 1147 quand ils sont gzippés.
- L'octet frag est maintenant inutilisé, le bloc Router Info n'est jamais fragmenté. L'octet frag doit être défini sur fragment 0, total fragments 1. Voir la section Fragmentation Session Confirmed ci-dessus pour plus d'informations.
- Le flooding ne doit pas être demandé sauf s'il y a des RouterAddresses publiées dans le RouterInfo. Le router récepteur ne doit pas faire le flood du RouterInfo sauf s'il contient des RouterAddresses publiées.
- Ce protocole ne fournit pas d'accusé de réception indiquant que le RouterInfo a été stocké ou diffusé. Si un accusé de réception est souhaité, et que le récepteur est floodfill, l'expéditeur devrait plutôt envoyer un DatabaseStoreMessage I2NP standard avec un token de réponse.

#### RelayRequest

Le nombre total de fragments n'est pas spécifié.

Notes :

```
+----+----+----+----+----+----+----+----+
| 3  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |     message       |
+----+----+----+----+                   +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 3
size :: 2 bytes, big endian, size of type + msg id + exp + message to follow
        I2NP message body size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: I2NP message body
```
Un fragment supplémentaire (numéro de fragment supérieur à zéro) d'un message I2NP.

- Il s'agit du même format d'en-tête I2NP de 9 octets utilisé dans NTCP2.
- Il s'agit exactement du même format que le bloc First Fragment, mais le type de bloc indique qu'il s'agit d'un message complet.
- La taille maximale incluant l'en-tête I2NP de 9 octets est MTU - 63 pour IPv4 et MTU - 83 pour IPv6.

#### RelayResponse

Notes :

Fermer la connexion. Ceci doit être le dernier bloc non-padding dans la charge utile.

Notes :

```
+----+----+----+----+----+----+----+----+
| 4  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |                   |
+----+----+----+----+                   +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 4
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: Partial I2NP message body, bytes 0 - (size - 10)
```
Envoyé dans un message Data en session, d'Alice à Bob. Voir la section Processus de relais ci-dessous.

- Il s'agit du même format d'en-tête I2NP de 9 octets utilisé dans NTCP2.
- Il s'agit exactement du même format que le bloc de message I2NP, mais le type de bloc indique qu'il s'agit du premier fragment d'un message.
- La longueur du message partiel doit être supérieure à zéro.
- Comme dans SSU 1, il est recommandé d'envoyer le dernier fragment en premier, afin que le récepteur connaisse le nombre total de fragments et puisse allouer efficacement les tampons de réception.
- La taille maximale incluant l'en-tête I2NP de 9 octets est MTU - 63 pour IPv4 et MTU - 83 pour IPv6.

#### RelayIntro

Notes :

```
+----+----+----+----+----+----+----+----+
| 5  |  size   |frag|    msg id         |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 5
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 5).
frag :: Fragment info:
        Bit order: 76543210 (bit 7 is MSB)
        bits 7-1: fragment number 1 - 127 (0 not allowed)
        bit 0: isLast (1 = true)
msg id :: 4 bytes, big endian, I2NP message ID
message :: Partial I2NP message body
```
Signature :

- La longueur du message partiel doit être supérieure à zéro.
- Comme dans SSU 1, il est recommandé d'envoyer le dernier fragment en premier, afin que le destinataire connaisse le nombre total de fragments et puisse allouer efficacement les tampons de réception.
- Comme dans SSU 1, le numéro de fragment maximum est 127, mais la limite pratique est de 63 ou moins. Les implémentations peuvent limiter le maximum à ce qui est pratique pour une taille de message I2NP maximale d'environ 64 Ko, ce qui représente environ 55 fragments avec un MTU minimum de 1280. Voir la section Taille maximale des messages I2NP ci-dessous.
- La taille maximale du message partiel (sans inclure l'identifiant de fragment et de message) est MTU - 68 pour IPv4 et MTU - 88 pour IPv6.

#### PeerTest

Alice signe la demande et l'inclut dans ce bloc ; Bob la transmet dans le bloc Relay Intro à Charlie. Algorithme de signature : Signer les données suivantes avec la clé de signature du router d'Alice :

```
+----+----+----+----+----+----+----+----+
| 6  |  size   |    valid data packets  |
+----+----+----+----+----+----+----+----+
    received   | rsn|     addl data     |
+----+----+----+----+                   +
~               .   .   .               ~
+----+----+----+----+----+----+----+----+

blk :: 6
size :: 2 bytes, big endian, value = 9 or more
valid data packets received :: The number of valid packets received
                              (current receive nonce value)
                              0 if error occurs in handshake phase
                              8 bytes, big endian
rsn :: reason, 1 byte:
       0: normal close or unspecified
       1: termination received
       2: idle timeout
       3: router shutdown
       4: data phase AEAD failure
       5: incompatible options
       6: incompatible signature type
       7: clock skew
       8: padding violation
       9: AEAD framing error
       10: payload format error
       11: Session Request error
       12: Session Created error
       13: Session Confirmed error
       14: Timeout
       15: RI signature verification fail
       16: s parameter missing, invalid, or mismatched in RouterInfo
       17: banned
       18: bad token
       19: connection limits
       20: incompatible version
       21: wrong net ID
       22: replaced by new session
addl data :: optional, 0 or more bytes, for future expansion, debugging,
             or reason text.
             Format unspecified and may vary based on reason code.
```
Envoyé dans un message Data en session, de Charlie vers Bob ou de Bob vers Alice, ET dans le message Hole Punch de Charlie vers Alice. Voir la section Processus de relais ci-dessous.

- Toutes les raisons ne sont pas nécessairement utilisées, cela dépend de l'implémentation. La plupart des échecs entraîneront généralement l'abandon du message, pas une terminaison. Voir les notes dans les sections de messages de handshake ci-dessus. Les raisons supplémentaires listées sont pour la cohérence, la journalisation, le débogage, ou en cas de changement de politique.
- Il est recommandé d'inclure un bloc ACK avec le bloc de Terminaison.
- Dans la phase de données, pour toute raison autre que "terminaison reçue", le pair devrait répondre avec un bloc de terminaison avec la raison "terminaison reçue".

#### NextNonce

Notes :

```
+----+----+----+----+----+----+----+----+
|  7 |  size   |flag|       nonce       |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 7
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility

The data below here is covered
by the signature, and Bob forwards it unmodified.

nonce :: 4 bytes, randomly generated by Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
Le jeton doit être utilisé immédiatement par Alice dans la demande de session.

- L'adresse IP est toujours incluse (contrairement à SSU 1) et peut être différente de l'IP utilisée pour la session.

Signature :

Si Charlie accepte (code de réponse 0) ou rejette (code de réponse 64 ou plus), Charlie signe la réponse et l'inclut dans ce bloc ; Bob la transmet dans le bloc Relay Response à Alice. Algorithme de signature : Signer les données suivantes avec la clé de signature du router de Charlie :

- prologue: 16 octets "RelayRequestData", non terminé par null (non inclus dans le message)
- bhash: hash de routeur de Bob de 32 octets (non inclus dans le message)
- chash: hash de routeur de Charlie de 32 octets (non inclus dans le message)
- nonce: nonce de 4 octets
- relay tag: étiquette de relais de 4 octets
- timestamp: horodatage de 4 octets (secondes)
- ver: version SSU de 1 octet
- asz: taille du point de terminaison (port + IP) de 1 octet (6 ou 18)
- AlicePort: numéro de port d'Alice de 2 octets
- Alice IP: adresse IP d'Alice de (asz - 2) octets

#### Accusé de réception

Si Bob rejette (code de réponse 1-63), Bob signe la réponse et l'inclut dans ce bloc. Algorithme de signature : Signer les données suivantes avec la clé de signature du router de Bob :

```
+----+----+----+----+----+----+----+----+
|  8 |  size   |flag|code|    nonce
+----+----+----+----+----+----+----+----+
     |     timestamp     | ver| csz|Char
+----+----+----+----+----+----+----+----+
 Port|   Charlie IP addr |              |
+----+----+----+----+----+              +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

blk :: 8
size :: 2 bytes, 6
flag :: 1 byte flags, Unused, set to 0 for future compatibility
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, Charlie is banned
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, relay tag not found
       6: rejected by Bob, Alice RI not found
       7-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       71-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD

The data below is covered by the signature if the code is 0 (accept).
Bob forwards it unmodified.

nonce :: 4 bytes, as received from Bob or Alice

The data below is present only if the code is 0 (accept).

timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
csz :: 1 byte endpoint (port + IP) size (0 or 6 or 18)
       may be 0 for some rejection codes
CharliePort :: 2 byte Charlie's port number, big endian
               not present if csz is 0
Charlie IP :: (csz - 2) byte representation of Charlie's IP address,
              network byte order
              not present if csz is 0
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Charlie.
             Not present if rejected by Bob.
token :: Token generated by Charlie for Alice to use
         in the Session Request.
         Only present if code is 0 (accept)
```
Envoyé dans un message Data en session, de Bob à Charlie. Voir la section Processus de relais ci-dessous.

Doit être précédé d'un bloc RouterInfo, ou d'un bloc de message I2NP DatabaseStore (ou fragment), contenant les informations du routeur d'Alice, soit dans la même charge utile (s'il y a de la place), soit dans un message précédent.

Notes :

Signature :

- prologue : 16 octets "RelayAgreementOK", non terminé par null (non inclus dans le message)
- bhash : hash de routeur de Bob de 32 octets (non inclus dans le message)
- nonce : nonce de 4 octets
- timestamp : timestamp de 4 octets (secondes)
- ver : version SSU de 1 octet
- csz : taille du point de terminaison (port + IP) de 1 octet (0 ou 6 ou 18)
- CharliePort : numéro de port de Charlie de 2 octets (absent si csz est 0)
- Charlie IP : adresse IP de Charlie de (csz - 2) octets (absente si csz est 0)

Alice signe la requête et Bob la transmet dans ce bloc à Charlie. Algorithme de vérification : Vérifier les données suivantes avec la clé de signature du router d'Alice :

- prologue : 16 octets "RelayAgreementOK", non terminé par null (non inclus dans le message)
- bhash : hachage de router de Bob sur 32 octets (non inclus dans le message)
- nonce : nonce sur 4 octets
- timestamp : horodatage sur 4 octets (secondes)
- ver : version SSU sur 1 octet
- csz : 1 octet = 0

#### Adresse

Envoyé soit dans un message Data en session, soit dans un message Peer Test hors session. Voir la section Processus de test de pairs ci-dessous.

Pour le message 2, doit être précédé d'un bloc RouterInfo, ou d'un bloc de message I2NP DatabaseStore (ou fragment), contenant les informations du router d'Alice, soit dans la même charge utile (s'il y a de la place), soit dans un message précédent.

```
+----+----+----+----+----+----+----+----+
|  9 |  size   |flag|                   |
+----+----+----+----+                   +
|                                       |
+                                       +
|         Alice Router Hash             |
+             32 bytes                  +
|                                       |
+                   +----+----+----+----+
|                   |      nonce        |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 9
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's 32-byte router hash,

The data below here is covered
by the signature, as received from Alice in the Relay Request,
and Bob forwards it unmodified.

nonce :: 4 bytes, as received from Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
Pour le message 4, si le relais est accepté (code de raison 0), il doit être précédé d'un bloc RouterInfo, ou d'un bloc de message I2NP DatabaseStore (ou fragment), contenant les informations du router de Charlie, soit dans la même charge utile (s'il y a de la place), soit dans un message précédent.

- Pour IPv4, l'adresse IP d'Alice fait toujours 4 octets, car Alice essaie de se connecter à Charlie via IPv4. IPv6 est pris en charge, et l'adresse IP d'Alice peut faire 16 octets.
- Pour IPv4, ce message doit être envoyé via une connexion IPv4 établie, car c'est la seule façon pour Bob de connaître l'adresse IPv4 de Charlie à retourner à Alice dans la [RelayResponse](#relayresponse). IPv6 est pris en charge, et ce message peut être envoyé via une connexion IPv6 établie.
- Toute adresse SSU publiée avec des introducers doit contenir "4" ou "6" dans l'option "caps".

Notes :

Alice envoie la requête à Bob en utilisant une session existante sur le transport (IPv4 ou IPv6) qu'elle souhaite tester. Lorsque Bob reçoit une requête d'Alice via IPv4, Bob doit sélectionner un Charlie qui annonce une adresse IPv4. Lorsque Bob reçoit une requête d'Alice via IPv6, Bob doit sélectionner un Charlie qui annonce une adresse IPv6. La communication réelle Bob-Charlie peut se faire via IPv4 ou IPv6 (c'est-à-dire, indépendamment du type d'adresse d'Alice).

- prologue : 16 octets "RelayRequestData", non terminé par null (non inclus dans le message)
- bhash : hachage de router de Bob sur 32 octets (non inclus dans le message)
- chash : hachage de router de Charlie sur 32 octets (non inclus dans le message)
- nonce : nonce sur 4 octets
- relay tag : tag de relais sur 4 octets
- timestamp : horodatage sur 4 octets (secondes)
- ver : version SSU sur 1 octet
- asz : taille du point de terminaison (port + IP) sur 1 octet (6 ou 18)
- AlicePort : numéro de port d'Alice sur 2 octets
- Alice IP : adresse IP d'Alice sur (asz - 2) octets

#### Demande de Relay Tag

Signatures :

Alice signe la requête et l'inclut dans le message 1 ; Bob la transmet dans le message 2 à Charlie. Charlie signe la réponse et l'inclut dans le message 3 ; Bob la transmet dans le message 4 à Alice. Algorithme de signature : Signer ou vérifier les données suivantes avec la clé de signature d'Alice ou de Charlie :

TODO seulement si nous effectuons une rotation des clés

```
+----+----+----+----+----+----+----+----+
| 10 |  size   | msg|code|flag|         |
+----+----+----+----+----+----+         +
| Alice router hash (message 2 only)    |
+             or                        +
| Charlie router hash (message 4 only)  |
+ or all zeros if rejected by Bob       +
| Not present in messages 1,3,5,6,7     |
+                             +----+----+
|                             | ver|
+----+----+----+----+----+----+----+----+
   nonce       |     timestamp     | asz|
+----+----+----+----+----+----+----+----+
|AlicePort|  Alice IP address |         |
+----+----+----+----+----+----+         +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 10
size :: 2 bytes, big endian, size of data to follow
msg :: 1 byte message number 1-7
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, no Charlie available
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, address unsupported
       6-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       70-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD
       reject codes only allowed in messages 3 and 4
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's or Charlie's 32-byte router hash,
        only present in messages 2 and 4.
        All zeros (fake hash) in message 4 if rejected by Bob.

For messages 1-4, the data below here is covered
by the signature, if present, and Bob forwards it unmodified.

ver :: 1 byte SSU version:
       1: SSU 1 (not supported)
       2: SSU 2 (required)
nonce :: 4 byte test nonce, big endian
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice or Charlie.
             Only present for messages 1-4.
             Optional in message 5-7.
```
4 octets d'acquittement passant, suivis d'un nombre d'acquittements et de zéro ou plusieurs plages nack/ack.

- Contrairement à SSU 1, le message 1 doit inclure l'adresse IP et le port d'Alice.

- Les tests d'adresses IPv6 sont pris en charge, et la communication Alice-Bob et Alice-Charlie peut se faire via IPv6, si Bob et Charlie indiquent leur support avec une capacité 'B' dans leur adresse IPv6 publiée. Voir la Proposition 126 pour plus de détails.

Cette conception est adaptée et simplifiée de QUIC. Les objectifs de conception sont les suivants :

- Les messages 1-4 doivent être contenus dans un message Data dans une session existante.

- Bob doit envoyer le RI d'Alice à Charlie avant d'envoyer le message 2.

- Bob doit envoyer le RI de Charlie à Alice avant d'envoyer le message 4, si accepté (code de raison 0).

- Les messages 5-7 doivent être contenus dans un message Peer Test hors session.

- Les messages 5 et 7 peuvent contenir les mêmes données signées que celles envoyées dans les messages 3 et 4, ou elles peuvent être régénérées avec un nouvel horodatage. La signature est optionnelle.

- Le message 6 peut contenir les mêmes données signées que celles envoyées dans les messages 1 et 2, ou il peut être régénéré avec un nouvel horodatage. La signature est optionnelle.

L'encodage spécifié ci-dessous accomplit ces objectifs de conception, en envoyant le numéro du bit le plus élevé qui est défini à 1, ainsi que des bits consécutifs supplémentaires inférieurs à celui-ci qui sont également définis à 1. Après cela, s'il y a de la place, une ou plusieurs "plages" spécifiant le nombre de bits consécutifs à 0 et de bits consécutifs à 1 inférieurs à cela. Voir QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) section 13.2.3 pour plus de contexte.

Exemples :

- prologue : 16 octets "PeerTestValidate", non terminé par null (non inclus dans le message)
- bhash : hash du router de Bob de 32 octets (non inclus dans le message)
- ahash : hash du router d'Alice de 32 octets (Utilisé uniquement dans la signature pour les messages 3 et 4 ; non inclus dans les messages 3 ou 4)
- ver : version SSU sur 1 octet
- nonce : nonce de test sur 4 octets
- timestamp : horodatage sur 4 octets (secondes)
- asz : taille du point de terminaison (port + IP) sur 1 octet (6 ou 18)
- AlicePort : numéro de port d'Alice sur 2 octets
- Alice IP : adresse IP d'Alice sur (asz - 2) octets

#### Étiquette de relais

Nous voulons ACK seulement le paquet 10 :

```
+----+----+----+----+----+----+----+----+
| 11 |  size   |      TBD               |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 11
size :: 2 bytes, big endian, size of data to follow
```
#### Nouveau Token

Nous voulons accuser réception des paquets 8-10 uniquement :

Nous voulons ACK 10 9 8 6 5 2 1 0, et NACK 7 4 3. L'encodage du bloc ACK est :

- Nous voulons encoder efficacement un "bitfield" (champ de bits), qui est une séquence de bits représentant les paquets acquittés.
- Le bitfield est principalement composé de 1. Les 1 et les 0 se présentent généralement en "groupes" séquentiels.
- L'espace disponible dans le paquet pour les acquittements varie.
- Le bit le plus important est celui avec le numéro le plus élevé. Ceux avec des numéros plus bas sont moins importants. En dessous d'une certaine distance par rapport au bit le plus élevé, les bits les plus anciens seront "oubliés" et ne seront plus jamais envoyés.

Notes :

```
+----+----+----+----+----+----+----+----+
| 12 |  size   |    Ack Through    |acnt|
+----+----+----+----+----+----+----+----+
|  range  |  range  |     .   .   .     |
+----+----+----+----+                   +
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 12
size :: 2 bytes, big endian, size of data to follow,
        5 minimum
ack through :: highest packet number acked
acnt :: number of acks lower than ack through also acked,
        0-255
range :: If present,
         1 byte nack count followed by 1 byte ack count,
         0-255 each
```
Port de 2 octets et adresse IP de 4 ou 16 octets. Adresse d'Alice, envoyée à Alice par Bob, ou adresse de Bob, envoyée à Bob par Alice.

Ceci peut être envoyé par Alice dans un message Session Request, Session Confirmed, ou Data. Non pris en charge dans le message Session Created, car Bob n'a pas encore le RI d'Alice et ne sait pas si Alice prend en charge le relais. De plus, si Bob reçoit une connexion entrante, il n'a probablement pas besoin d'introducers (sauf peut-être pour l'autre type ipv4/ipv6).

- Ack Through: 10
- acnt: 0
- aucune plage n'est incluse

Lorsqu'elle est envoyée dans la Session Request, Bob peut répondre avec un Relay Tag dans le message Session Created, ou peut choisir d'attendre de recevoir le RouterInfo d'Alice dans la Session Confirmed pour valider l'identité d'Alice avant de répondre dans un message Data. Si Bob ne souhaite pas faire de relais pour Alice, il n'envoie pas de bloc Relay Tag.

- Ack Through: 10
- acnt: 2
- aucune plage n'est incluse

Ceci peut être envoyé par Bob dans un message Session Confirmed ou Data, en réponse à une Relay Tag Request d'Alice.

- Ack Through: 10
- acnt: 2 (ack 9 8)
- range: 1 2 (nack 7, ack 6 5)
- range: 2 3 (nack 4 3, ack 2 1 0)

Lorsque la demande de Relay Tag est envoyée dans la Session Request, Bob peut répondre avec un Relay Tag dans le message Session Created, ou peut choisir d'attendre de recevoir les RouterInfo d'Alice dans la Session Confirmed pour valider l'identité d'Alice avant de répondre dans un message Data. Si Bob ne souhaite pas servir de relais pour Alice, il n'envoie pas de bloc Relay Tag.

- Les plages peuvent ne pas être présentes. Le nombre maximum de plages n'est pas spécifié, il peut y en avoir autant que le paquet peut en contenir.
- Range nack peut être zéro si on acquitte plus de 255 paquets consécutifs.
- Range ack peut être zéro si on rejette plus de 255 paquets consécutifs.
- Range nack et ack ne peuvent pas être tous les deux zéro.
- Après la dernière plage, les paquets ne sont ni acquittés ni rejetés. La longueur du bloc ack et la façon dont les anciens acks/nacks sont traités dépend de l'expéditeur du bloc ack. Voir les sections ack ci-dessous pour discussion.
- L'ack through devrait être le numéro de paquet le plus élevé reçu, et tous les paquets supérieurs n'ont pas été reçus. Cependant, dans des situations limitées, il pourrait être plus bas, comme acquitter un seul paquet qui "comble un trou", ou une implémentation simplifiée qui ne maintient pas l'état de tous les paquets reçus. Au-dessus du plus haut reçu, les paquets ne sont ni acquittés ni rejetés, mais après plusieurs blocs ack, il peut être approprié de passer en mode de retransmission rapide.
- Ce format est une version simplifiée de celui de QUIC. Il est conçu pour encoder efficacement un grand nombre d'ACKs, ainsi que des rafales de NACKs.
- Les blocs ACK sont utilisés pour acquitter les paquets de phase de données. Ils ne doivent être inclus que pour les paquets de phase de données en session.

#### Défi de Chemin

Pour une connexion ultérieure. Généralement inclus dans les messages Session Created et Session Confirmed. Peut également être envoyé à nouveau dans le message Data d'une session de longue durée si le jeton précédent expire.

```
+----+----+----+----+----+----+----+----+
| 13 | 6 or 18 |   Port  | IP Address    
+----+----+----+----+----+----+----+----+
     |
+----+

blk :: 13
size :: 2 bytes, big endian, 6 or 18
port :: 2 bytes, big endian
ip :: 4 byte IPv4 or 16 byte IPv6 address,
      big endian (network byte order)
```
#### Réponse du chemin

Un Ping avec des données arbitraires à retourner dans une Path Response, utilisé comme keep-alive ou pour valider un changement d'IP/Port.

Remarques :

```
+----+----+----+
| 15 |    0    |
+----+----+----+

blk :: 15
size :: 2 bytes, big endian, value = 0
```
#### Numéro du premier paquet

Un Pong avec les données reçues dans le Path Challenge, en réponse au Path Challenge, utilisé comme keep-alive ou pour valider un changement d'IP/Port.

Optionnellement inclus dans la négociation dans chaque direction, pour spécifier le premier numéro de paquet qui sera envoyé. Cela fournit plus de sécurité pour le chiffrement d'en-tête, similaire à TCP.

```
+----+----+----+----+----+----+----+
| 16 |    4    |    relay tag      |
+----+----+----+----+----+----+----+

blk :: 16
size :: 2 bytes, big endian, value = 4
relay tag :: 4 bytes, big endian, nonzero
```
#### Congestion

Pas entièrement spécifié, actuellement non pris en charge.

```
+----+----+----+----+----+----+----+----+
| 17 |   12    |     expires       |
+----+----+----+----+----+----+----+----+
                token              |
+----+----+----+----+----+----+----+

blk :: 17
size :: 2 bytes, big endian, value = 12
expires :: Unix timestamp, unsigned seconds.
           Wraps around in 2106
token :: 8 bytes, big endian
```
#### Remplissage

Ce bloc est conçu pour être une méthode extensible permettant d'échanger des informations de contrôle de congestion. Le contrôle de congestion peut être complexe et pourrait évoluer à mesure que nous acquérons plus d'expérience avec le protocole lors des tests en conditions réelles, ou après le déploiement complet.

```
+----+----+----+----+----+----+----+----+
| 18 |  size   |    Arbitrary Data      |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 18
size :: 2 bytes, big endian, size of data to follow
data :: Arbitrary data to be returned in a Path Response
        length as selected by sender
```
Cela maintient toute information de congestion en dehors des blocs I2NP, First Fragment, Followon Fragment et ACK à usage intensif, où aucun espace n'est alloué pour les drapeaux. Bien qu'il y ait trois octets de drapeaux inutilisés dans l'en-tête du paquet Data, cela fournit également un espace limité pour l'extensibilité et une protection de chiffrement plus faible.

- Une taille de données minimale de 8 octets, contenant des données aléatoires, est recommandée mais non requise.
- La taille maximale n'est pas spécifiée, mais elle devrait être bien en dessous de 1280, car la PMTU pendant la phase de validation du chemin est de 1280.
- Les grandes tailles de challenge ne sont pas recommandées car elles pourraient constituer un vecteur d'attaques par amplification de paquets.

#### Usurpation d'adresse de pair

Bien qu'il soit quelque peu inefficace d'utiliser un bloc de 4 octets pour deux bits d'information, en plaçant ceci dans un bloc séparé, nous pouvons facilement l'étendre avec des données supplémentaires telles que les tailles de fenêtre actuelles, le RTT mesuré, ou d'autres indicateurs. L'expérience a montré que les bits d'indicateurs seuls sont souvent insuffisants et maladroits pour l'implémentation de schémas avancés de contrôle de congestion. Essayer d'ajouter le support pour toute fonctionnalité possible de contrôle de congestion dans, par exemple, le bloc ACK, gaspillerait de l'espace et ajouterait de la complexité à l'analyse de ce bloc.

```
+----+----+----+----+----+----+----+----+
| 19 |  size   |                        |
+----+----+----+                        +
|    Data received in Path Challenge    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 19
size :: 2 bytes, big endian, size of data to follow
data :: As received in a Path Challenge
```
#### Usurpation d'adresse sur le chemin

Les implémentations ne doivent pas supposer que l'autre router prend en charge un bit de flag particulier ou une fonctionnalité incluse ici, sauf si l'implémentation est requise par une version future de cette spécification.

Ce bloc devrait probablement être le dernier bloc non-remplissage dans la charge utile.

```
+----+----+----+----+----+----+----+
| 20 |  size   |  First pkt number |
+----+----+----+----+----+----+----+

blk :: 20
size :: 4
pkt num :: The first packet number to be sent in the data phase
```
#### Transfert de paquets hors-chemin

Ceci est pour le remplissage à l'intérieur des charges utiles AEAD. Le remplissage pour tous les messages se trouve à l'intérieur des charges utiles AEAD.

Le padding devrait approximativement respecter les paramètres négociés. Bob a envoyé ses paramètres tx/rx min/max demandés dans Session Created. Alice a envoyé ses paramètres tx/rx min/max demandés dans Session Confirmed. Des options mises à jour peuvent être envoyées pendant la phase de données. Voir les informations sur le bloc d'options ci-dessus.

Si présent, ceci doit être le dernier bloc dans la charge utile.

Notes :

SSU2 est conçu pour minimiser l'impact des messages rejoués par un attaquant.

```
+----+----+----+----+
| 21 |  size   |flag|
+----+----+----+----+

blk :: 21
size :: 1 (or more if extended)
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 1 to request immediate ack
       bit 1: 1 for explicit congestion notification (ECN)
       bits 7-2: Unused, set to 0 for future compatibility
```
#### Implications en matière de confidentialité

Les messages Token Request, Retry, Session Request, Session Created, Hole Punch et Peer Test hors session doivent contenir des blocs DateTime.

Alice et Bob valident tous les deux que l'heure de ces messages se trouve dans une plage de décalage valide (recommandé +/- 2 minutes). Pour la "résistance au sondage", Bob ne devrait pas répondre aux messages Token Request ou Session Request si le décalage est invalide, car ces messages pourraient constituer une attaque par rejeu ou par sondage.

Bob peut choisir de rejeter les messages Token Request et Retry dupliqués, même si le décalage est valide, via un filtre de Bloom ou un autre mécanisme. Cependant, la taille et le coût CPU pour répondre à ces messages est faible. Au pire, un message Token Request rejoué peut invalider un token précédemment envoyé.

```
+----+----+----+----+----+----+----+----+
|254 |  size   |      padding           |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 254
size :: 2 bytes, big endian, size of padding to follow
padding :: random data
```
Le système de jetons réduit considérablement l'impact des messages Session Request rejoués. Étant donné que les jetons ne peuvent être utilisés qu'une seule fois, un message Session Request rejoué n'aura jamais un jeton valide. Bob peut choisir de rejeter les messages Session Request dupliqués, même si le décalage est valide, via un filtre de Bloom ou un autre mécanisme. Cependant, la taille et le coût CPU de répondre avec un message Retry sont faibles. Au pire, l'envoi d'un message Retry peut invalider un jeton précédemment envoyé.

- Taille = 0 est autorisée.
- Stratégies de remplissage à déterminer.
- Remplissage minimum à déterminer.
- Les charges utiles contenant uniquement du remplissage sont autorisées.
- Valeurs par défaut du remplissage à déterminer.
- Voir le bloc d'options pour la négociation des paramètres de remplissage
- Voir le bloc d'options pour les paramètres de remplissage min/max
- Ne pas dépasser le MTU. Si plus de remplissage est nécessaire, envoyer plusieurs messages.
- La réponse du router en cas de violation du remplissage négocié dépend de l'implémentation.
- La longueur du remplissage doit être décidée soit message par message avec des estimations de la distribution des longueurs, soit des délais aléatoires doivent être ajoutés. Ces contre-mesures doivent être incluses pour résister à la DPI (inspection approfondie de paquets), car les tailles de messages révéleraient sinon que du trafic I2P est transporté par le protocole de transport. Le schéma de remplissage exact fait l'objet de travaux futurs, l'Annexe A de [NTCP2](/docs/specs/ntcp2) fournit plus d'informations sur le sujet.

## Prévention de la rejeu

Les messages Session Created et Session Confirmed dupliqués ne seront pas validés car l'état de la négociation Noise ne sera pas dans l'état correct pour les déchiffrer. Au pire, un pair peut retransmettre un Session Confirmed en réponse à un Session Created apparemment dupliqué.

Les messages Hole Punch et Peer Test rejoués devraient avoir peu ou pas d'impact.

Les routers doivent utiliser le numéro de paquet du message de données pour détecter et supprimer les messages de phase de données dupliqués. Chaque numéro de paquet ne doit être utilisé qu'une seule fois. Les messages rejoués doivent être ignorés.

Si aucun Session Created ou Retry n'est reçu par Alice :

Maintenir les mêmes identifiants de source et de connexion, la clé éphémère, et le numéro de paquet 0. Ou, simplement conserver et retransmettre le même paquet chiffré. Le numéro de paquet ne doit pas être incrémenté, car cela changerait la valeur de hachage chaîné utilisée pour chiffrer le message Session Created.

Intervalles de retransmission recommandés : 1,25, 2,5 et 5 secondes (1,25, 3,75 et 8,75 secondes après le premier envoi). Délai d'expiration recommandé : 15 secondes au total

Si aucune Session Confirmed n'est reçue par Bob :

Conserver les mêmes ID de source et de connexion, la clé éphémère et le numéro de paquet 0. Ou simplement conserver le paquet chiffré. Le numéro de paquet ne doit pas être incrémenté, car cela changerait la valeur de hachage chaîné utilisée pour chiffrer le message Session Confirmed.

## Retransmission de handshake

### Session créée

Intervalles de retransmission recommandés : 1, 2 et 4 secondes (1, 3 et 7 secondes après le premier envoi). Délai d'expiration recommandé : 12 secondes au total

Dans SSU 1, Alice ne passe pas à la phase de données tant que le premier paquet de données n'est pas reçu de Bob. Cela fait de SSU 1 une configuration à deux allers-retours.

Pour SSU 2, intervalles de retransmission Session Confirmed recommandés : 1,25, 2,5 et 5 secondes (1,25, 3,75 et 8,75 secondes après le premier envoi).

### Session confirmée

Il existe plusieurs alternatives. Toutes sont 1 RTT :

1) Alice suppose que Session Confirmed a été reçu, envoie des messages de données immédiatement, ne retransmet jamais Session Confirmed. Les paquets de données reçus dans le désordre (avant Session Confirmed) seront indéchiffrables, mais seront retransmis. Si Session Confirmed est perdu, tous les messages de données envoyés seront supprimés. 2) Comme dans 1), envoyer des messages de données immédiatement, mais aussi retransmettre Session Confirmed jusqu'à ce qu'un message de données soit reçu. 3) Nous pourrions utiliser IK au lieu de XK, car il n'a que deux messages dans la négociation, mais il utilise un DH supplémentaire (4 au lieu de 3).

L'implémentation recommandée est l'option 2). Alice doit conserver les informations requises pour retransmettre le message Session Confirmed. Alice devrait également retransmettre tous les messages Data après que le message Session Confirmed ait été retransmis.

### Demande de jeton

Lors de la retransmission de Session Confirmed, maintenez les mêmes identifiants de source et de connexion, la clé éphémère et le numéro de paquet 1. Ou, conservez simplement le paquet chiffré. Le numéro de paquet ne doit pas être incrémenté, car cela modifierait la valeur de hachage chaîné qui est une entrée pour la fonction split().

Bob peut conserver (mettre en file d'attente) les messages de données reçus avant le message Session Confirmed. Ni les clés de protection d'en-tête ni les clés de déchiffrement ne sont disponibles avant la réception du message Session Confirmed, donc Bob ne sait pas qu'il s'agit de messages de données, mais cela peut être présumé. Après la réception du message Session Confirmed, Bob est capable de déchiffrer et traiter les messages de données mis en file d'attente. Si cela est trop complexe, Bob peut simplement abandonner les messages de données indéchiffrables, car Alice les retransmettra.

Note : Si les paquets de session confirmée sont perdus, Bob retransmettra la session créée. L'en-tête de session créée ne sera pas déchiffrable avec la clé d'intro d'Alice, car elle est définie avec la clé d'intro de Bob (sauf si un déchiffrement de secours est effectué avec la clé d'intro de Bob). Bob peut immédiatement retransmettre les paquets de session confirmée s'ils n'ont pas été précédemment acquittés, et qu'un paquet non déchiffrable est reçu.

Si aucun Retry n'est reçu par Alice :

Maintenir les mêmes identifiants de source et de connexion. Une implémentation peut générer un nouveau numéro de paquet aléatoire et chiffrer un nouveau paquet ; ou elle peut réutiliser le même numéro de paquet ou simplement conserver et retransmettre le même paquet chiffré. Le numéro de paquet ne doit pas être incrémenté, car cela modifierait la valeur de hachage chaîné utilisée pour chiffrer le message Session Created.

Intervalles de retransmission recommandés : 3 et 6 secondes (3 et 9 secondes après le premier envoi). Délai d'expiration recommandé : 15 secondes au total

Si aucun Session Confirmed n'est reçu par Bob :

Un message Retry n'est pas retransmis en cas de timeout, afin de réduire les impacts des adresses sources usurpées.

### Réessayer

Cependant, un message Retry peut être retransmis en réponse à un message Session Request répété reçu avec le token original (invalide), ou en réponse à un message Token Request répété. Dans les deux cas, cela indique que le message Retry a été perdu.

Si un second message de demande de session est reçu avec un token différent mais toujours invalide, abandonner la session en attente et ne pas répondre.

Si l'on renvoie le message Retry : Maintenir les mêmes ID source et de connexion ainsi que le token. Une implémentation peut générer un nouveau numéro de paquet aléatoire et chiffrer un nouveau paquet ; Ou elle peut réutiliser le même numéro de paquet ou simplement conserver et retransmettre le même paquet chiffré.

### Délai d'expiration total

Le délai d'expiration total recommandé pour la négociation est de 20 secondes.

Les duplicatas des trois messages de handshake Noise Session Request, Session Created et Session Confirmed doivent être détectés avant MixHash() de l'en-tête. Bien que le traitement AEAD de Noise échouera probablement après cela, le hash de handshake serait déjà corrompu.

Si l'un des trois messages est corrompu et échoue à l'AEAD, la négociation ne peut plus être récupérée par la suite même avec une retransmission, car MixHash() a déjà été appelé sur le message corrompu.

Le Token dans l'en-tête de Session Request est utilisé pour atténuer les attaques DoS, empêcher l'usurpation d'adresse source, et comme résistance aux attaques de rejeu.

Si Bob n'accepte pas le token dans le message Session Request, Bob ne décrypte PAS le message, car cela nécessite une opération DH coûteuse. Bob envoie simplement un message Retry avec un nouveau token.

### Doublons et Gestion d'Erreurs

Si un message Session Request ultérieur est alors reçu avec ce token, Bob procède au déchiffrement de ce message et continue avec la négociation.

### Numéros de Paquets

Le token doit être une valeur de 8 octets générée aléatoirement, si le générateur du token stocke les valeurs et l'IP et le port associés (en mémoire ou de manière persistante). Le générateur ne peut pas générer une valeur opaque, par exemple, en utilisant le SipHash (avec une graine secrète K0, K1) de l'IP, du port, et de l'heure ou du jour actuel, pour créer des tokens qui n'ont pas besoin d'être sauvegardés en mémoire, car cette méthode rend difficile le rejet des tokens réutilisés et les attaques par rejeu. Cependant, c'est un sujet d'étude ultérieure si nous pouvons migrer vers un tel schéma, comme le fait [WireGuard](https://www.wireguard.com/papers/wireguard.pdf), en utilisant un HMAC de 16 octets d'un secret serveur et d'une adresse IP.

Les tokens ne peuvent être utilisés qu'une seule fois. Un token envoyé de Bob à Alice dans un message Retry doit être utilisé immédiatement et expire en quelques secondes. Un token envoyé dans un bloc New Token dans une session établie peut être utilisé dans une connexion ultérieure, et il expire au moment spécifié dans ce bloc. L'expiration est spécifiée par l'expéditeur ; les valeurs recommandées sont de plusieurs minutes au minimum, une ou plusieurs heures au maximum, selon la surcharge maximale souhaitée des tokens stockés.

## Jetons

Si l'adresse IP ou le port d'un router change, il doit supprimer tous les jetons sauvegardés (entrants et sortants) pour l'ancienne adresse IP ou le port, car ils ne sont plus valides. Les jetons peuvent optionnellement être conservés lors des redémarrages du router, selon l'implémentation. L'acceptation d'un jeton non expiré n'est pas garantie ; si Bob a oublié ou supprimé ses jetons sauvegardés, il enverra un Retry à Alice. Un router peut choisir de limiter le stockage des jetons et supprimer les jetons les plus anciens même s'ils n'ont pas expiré.

Les blocs New Token peuvent être envoyés d'Alice vers Bob ou de Bob vers Alice. Ils seraient généralement envoyés au moins une fois, pendant ou peu après l'établissement de la session. En raison des vérifications de validation du RouterInfo dans le message Session Confirmed, Bob ne devrait pas envoyer un bloc New Token dans le message Session Created, il peut être envoyé avec l'ACK 0 et Router Info après que le Session Confirmed soit reçu and validé.

Comme les durées de vie des sessions sont souvent plus longues que l'expiration des jetons, le jeton devrait être renvoyé avant ou après expiration avec un nouveau délai d'expiration, ou un nouveau jeton devrait être envoyé. Les routeurs doivent supposer que seul le dernier jeton reçu est valide ; il n'y a aucune exigence de stocker plusieurs jetons entrants ou sortants pour la même IP/port.

Un jeton est lié à la combinaison d'IP/port source et d'IP/port de destination. Un jeton reçu sur IPv4 ne peut pas être utilisé pour IPv6 ou vice versa.

Si l'un des pairs migre vers une nouvelle IP ou un nouveau port pendant la session (voir la section Migration de Connexion), tous les jetons précédemment échangés sont invalidés, et de nouveaux jetons doivent être échangés.

Les implémentations peuvent, mais ne sont pas tenues de, sauvegarder les tokens sur disque et les recharger au redémarrage. Si ils sont persistés, l'implémentation doit s'assurer que l'adresse IP et le port n'ont pas changé depuis l'arrêt avant de les recharger.

Différences par rapport à SSU 1

Note : Comme dans SSU 1, le fragment initial ne contient pas d'informations sur le nombre total de fragments ou la longueur totale. Les fragments suivants ne contiennent pas d'informations sur leur décalage. Cela offre à l'expéditeur la flexibilité de fragmenter "à la volée" en fonction de l'espace disponible dans le paquet. (Java I2P ne fait pas cela ; il "pré-fragmente" avant que le premier fragment ne soit envoyé) Cependant, cela impose au récepteur de stocker les fragments reçus dans le désordre et de retarder le réassemblage jusqu'à ce que tous les fragments soient reçus.

Comme dans SSU 1, toute retransmission de fragments doit préserver la longueur (et le décalage implicite) de la transmission précédente du fragment.

SSU 2 sépare effectivement les trois cas (message complet, fragment initial et fragment de continuation) en trois types de blocs différents, afin d'améliorer l'efficacité de traitement.

Ce protocole ne prévient PAS complètement la livraison en double des messages I2NP. Les doublons au niveau de la couche IP ou les attaques par rejeu seront détectés au niveau de la couche SSU2, car chaque numéro de paquet ne peut être utilisé qu'une seule fois.

## Fragmentation des messages I2NP

Lorsque les messages I2NP ou les fragments sont retransmis dans de nouveaux paquets, cependant, ceci n'est pas détectable au niveau de la couche SSU2. Le router devrait appliquer l'expiration I2NP (à la fois trop ancien et trop loin dans le futur) et utiliser un filtre de Bloom ou un autre mécanisme basé sur l'ID du message I2NP.

Des mécanismes supplémentaires peuvent être utilisés par le router, ou dans l'implémentation SSU2, pour détecter les doublons. Par exemple, SSU2 pourrait maintenir un cache des identifiants de messages reçus récemment. Cela dépend de l'implémentation.

Cette spécification spécifie le protocole pour la numérotation des paquets et les blocs ACK. Ceci fournit suffisamment d'informations en temps réel pour qu'un transmetteur puisse implémenter un algorithme de contrôle de congestion efficace et réactif, tout en permettant de la flexibilité et de l'innovation dans cette implémentation. Cette section discute des objectifs d'implémentation et fournit des suggestions. Des conseils généraux peuvent être trouvés dans [RFC-9002](https://tools.ietf.org/html/rfc9002). Voir aussi [RFC-6298](https://tools.ietf.org/html/rfc6298) pour des conseils sur les minuteurs de retransmission.

Les paquets de données ACK uniquement ne doivent pas être comptabilisés dans les octets ou paquets en transit et ne sont pas soumis au contrôle de congestion. Contrairement à TCP, SSU2 peut détecter la perte de ces paquets et cette information peut être utilisée pour ajuster l'état de congestion. Cependant, ce document ne spécifie pas de mécanisme pour ce faire.

## Duplication des messages I2NP

Les paquets contenant d'autres blocs non-data peuvent également être exclus du contrôle de congestion si désiré, selon l'implémentation. Par exemple :

Il est recommandé que le contrôle de congestion soit basé sur le nombre d'octets, et non sur le nombre de paquets, en suivant les directives des RFC TCP et QUIC [RFC-9002](https://tools.ietf.org/html/rfc9002). Une limite supplémentaire du nombre de paquets peut également être utile pour éviter le débordement de tampon dans le noyau ou dans les middleboxes, selon l'implémentation, bien que cela puisse ajouter une complexité significative. Si la sortie de paquets par session et/ou totale est limitée en bande passante et/ou rythmée, cela peut atténuer le besoin de limiter le nombre de paquets.

Dans SSU 1, les ACK et NACK contenaient des numéros de messages I2NP et des masques de bits de fragments. Les transmetteurs suivaient le statut ACK des messages sortants (et leurs fragments) et retransmettaient les fragments selon les besoins.

## Contrôle de congestion

Dans SSU 2, les ACK et NACK contiennent des numéros de paquets. Les transmetteurs doivent maintenir une structure de données avec une correspondance entre les numéros de paquets et leur contenu. Quand un paquet reçoit un ACK ou un NACK, le transmetteur doit déterminer quels messages I2NP et fragments étaient dans ce paquet, pour décider quoi retransmettre.

Bob envoie un ACK du paquet 0, qui accuse réception du message Session Confirmed et permet à Alice de passer à la phase de données, et de supprimer le volumineux message Session Confirmed sauvegardé pour une éventuelle retransmission. Ceci remplace le DeliveryStatusMessage envoyé par Bob dans SSU 1.

Bob devrait envoyer un ACK dès que possible après avoir reçu le message Session Confirmed. Un petit délai (pas plus de 50 ms) est acceptable, car au moins un message Data devrait arriver presque immédiatement après le message Session Confirmed, de sorte que l'ACK puisse acquitter à la fois le Session Confirmed et le message Data. Cela empêchera Bob d'avoir à retransmettre le message Session Confirmed.

- Test de pair
- Demande/intro/réponse de relais
- Défi/réponse de chemin

Définition : Paquets provoquant un accusé de réception : Les paquets qui contiennent des blocs provoquant un accusé de réception déclenchent un ACK de la part du récepteur dans le délai maximum d'accusé de réception et sont appelés paquets provoquant un accusé de réception.

### ACK de Confirmation de Session

Les routeurs accusent réception de tous les paquets qu'ils reçoivent et traitent. Cependant, seuls les paquets nécessitant un accusé de réception provoquent l'envoi d'un bloc ACK dans le délai maximum d'accusé de réception. Les paquets qui ne nécessitent pas d'accusé de réception ne sont acquittés que lorsqu'un bloc ACK est envoyé pour d'autres raisons.

Lors de l'envoi d'un paquet pour quelque raison que ce soit, un endpoint devrait tenter d'inclure un bloc ACK si aucun n'a été envoyé récemment. Cela aide à la détection opportune des pertes chez le pair.

### Génération des ACK

En général, des commentaires fréquents d'un récepteur améliorent la réponse aux pertes et à la congestion, mais cela doit être équilibré contre la charge excessive générée par un récepteur qui envoie un bloc ACK en réponse à chaque paquet nécessitant un accusé de réception. Les conseils offerts ci-dessous cherchent à trouver cet équilibre.

Les paquets de données en session contenant n'importe quel bloc SAUF les suivants déclenchent un accusé de réception :

### ACKs de handshake

Les paquets hors session, y compris les messages d'établissement de liaison et les messages de test de pairs 5-7, ont leurs propres mécanismes d'accusé de réception. Voir ci-dessous.

Ce sont des cas particuliers :

Les blocs ACK sont utilisés pour accuser réception des paquets de phase de données. Ils ne doivent être inclus que pour les paquets de phase de données en session.

Chaque paquet doit être acquitté au moins une fois, et les paquets nécessitant un acquittement doivent être acquittés au moins une fois dans un délai maximum.

Un point de terminaison doit acquitter tous les paquets de poignée de main nécessitant un acquittement immédiatement dans son délai maximum, avec l'exception suivante. Avant la confirmation de la poignée de main, un point de terminaison pourrait ne pas avoir les clés de chiffrement d'en-tête de paquet pour déchiffrer les paquets lorsqu'ils sont reçus. Il pourrait donc les mettre en mémoire tampon et les acquitter lorsque les clés requises deviennent disponibles.

- Bloc ACK
- Bloc d'adresse
- Bloc DateTime
- Bloc de remplissage
- Bloc de terminaison
- Autres ?

Étant donné que les paquets contenant uniquement des blocs ACK ne sont pas soumis au contrôle de congestion, un point de terminaison ne doit pas envoyer plus d'un tel paquet en réponse à la réception d'un paquet sollicitant un accusé de réception.

### Envoi de blocs ACK

Un endpoint ne doit pas envoyer un paquet non-ack-eliciting en réponse à un paquet non-ack-eliciting, même s'il y a des lacunes de paquets qui précèdent le paquet reçu. Cela évite une boucle de rétroaction infinie d'accusés de réception, qui pourrait empêcher la connexion de devenir inactive. Les paquets non-ack-eliciting sont finalement acquittés lorsque l'endpoint envoie un bloc ACK en réponse à d'autres événements.

- La demande de Token est implicitement acquittée par Retry
- La demande de session est implicitement acquittée par Session Created ou Retry
- Retry est implicitement acquittée par Session Request
- Session Created est implicitement acquittée par Session Confirmed
- Session Confirmed doit être acquittée immédiatement

### Fréquence ACK

Un endpoint qui envoie uniquement des blocs ACK ne recevra pas d'accusés de réception de son pair à moins que ces accusés de réception ne soient inclus dans des paquets contenant des blocs déclenchant des accusés de réception. Un endpoint devrait envoyer un bloc ACK avec d'autres blocs lorsqu'il y a de nouveaux paquets déclenchant des accusés de réception à acquitter. Lorsque seuls des paquets ne déclenchant pas d'accusés de réception doivent être acquittés, un endpoint PEUT choisir de ne pas envoyer de bloc ACK avec les blocs sortants jusqu'à ce qu'un paquet déclenchant un accusé de réception ait été reçu.

Un endpoint qui n'envoie que des paquets non-ack-eliciting pourrait choisir d'ajouter occasionnellement un bloc ack-eliciting à ces paquets pour s'assurer qu'il reçoit un accusé de réception. Dans ce cas, un endpoint NE DOIT PAS envoyer un bloc ack-eliciting dans tous les paquets qui seraient autrement non-ack-eliciting, afin d'éviter une boucle de rétroaction infinie d'accusés de réception.

Pour aider à la détection de perte chez l'expéditeur, un point de terminaison devrait générer et envoyer un bloc ACK sans délai lorsqu'il reçoit un paquet sollicitant un accusé de réception dans l'un de ces cas :

Les algorithmes sont censés être résistants aux récepteurs qui ne suivent pas les conseils offerts ci-dessus. Cependant, une implémentation ne devrait dévier de ces exigences qu'après avoir soigneusement considéré les implications de performance d'un changement, pour les connexions établies par le point de terminaison et pour les autres utilisateurs du réseau.

Un récepteur détermine à quelle fréquence envoyer des accusés de réception en réponse aux paquets nécessitant un accusé de réception. Cette détermination implique un compromis.

Les endpoints s'appuient sur un accusé de réception en temps opportun pour détecter les pertes. Les contrôleurs de congestion basés sur une fenêtre s'appuient sur les accusés de réception pour gérer leur fenêtre de congestion. Dans les deux cas, retarder les accusés de réception peut affecter négativement les performances.

D'autre part, réduire la fréquence des paquets qui ne transportent que des accusés de réception réduit les coûts de transmission et de traitement des paquets aux deux extrémités. Cela peut améliorer le débit de connexion sur les liens gravement asymétriques et réduire le volume de trafic d'accusé de réception utilisant la capacité du chemin de retour ; voir la Section 3 de [RFC-3449](https://tools.ietf.org/html/rfc3449).

Un récepteur devrait envoyer un bloc ACK après avoir reçu au moins deux paquets nécessitant un acquittement. Cette recommandation est de nature générale et cohérente avec les recommandations pour le comportement des points de terminaison TCP [RFC-5681](https://tools.ietf.org/html/rfc5681). La connaissance des conditions réseau, la connaissance du contrôleur de congestion du pair, ou des recherches et expérimentations supplémentaires pourraient suggérer des stratégies d'acquittement alternatives avec de meilleures caractéristiques de performance.

- Quand le paquet reçu a un numéro de paquet inférieur à un autre paquet nécessitant un accusé de réception qui a été reçu
- Quand le paquet a un numéro de paquet supérieur au paquet nécessitant un accusé de réception avec le numéro le plus élevé qui a été reçu et qu'il manque des paquets entre ce paquet et ce paquet-ci.
- Quand le flag ack-immediate dans l'en-tête du paquet est défini

Un récepteur peut traiter plusieurs paquets disponibles avant de déterminer s'il doit envoyer un bloc ACK en réponse. En général, le récepteur ne devrait pas retarder un ACK de plus de RTT / 6, ou 150 ms maximum.

### Flag ACK Immédiat

Le drapeau ack-immediate dans l'en-tête du paquet de données est une demande pour que le récepteur envoie un accusé de réception peu après la réception, probablement dans quelques ms. En général, le récepteur ne devrait pas retarder un ACK immédiat de plus de RTT / 16, ou 5 ms maximum.

Le destinataire ne connaît pas la taille de la fenêtre d'envoi de l'expéditeur, et ne sait donc pas combien de temps attendre avant d'envoyer un ACK. Le flag d'ACK immédiat dans l'en-tête du paquet de données est un moyen important de maintenir un débit maximum en minimisant le RTT effectif. Le flag d'ACK immédiat est l'octet 13 de l'en-tête, bit 0, c'est-à-dire (header[13] & 0x01). Lorsqu'il est défini, un ACK immédiat est demandé. Voir la section sur l'en-tête court ci-dessus pour plus de détails.

Il existe plusieurs stratégies possibles qu'un expéditeur peut utiliser pour déterminer quand définir le flag immediate-ack :

Les drapeaux ACK immédiats ne devraient être nécessaires que sur les paquets de données contenant des messages I2NP ou des fragments de messages.

Quand un bloc ACK est envoyé, une ou plusieurs plages de paquets accusés réception sont incluses. Inclure des accusés de réception pour des paquets plus anciens réduit le risque de retransmissions parasites causées par la perte de blocs ACK précédemment envoyés, au coût de blocs ACK plus volumineux.

Les blocs ACK doivent toujours accuser réception des paquets reçus le plus récemment, et plus les paquets sont désordonnés, plus il est important d'envoyer rapidement un bloc ACK mis à jour, pour éviter que le pair déclare un paquet comme perdu et retransmette de manière erronée les blocs qu'il contient. Un bloc ACK doit tenir dans un seul paquet. Si ce n'est pas le cas, alors les plages plus anciennes (celles avec les plus petits numéros de paquet) sont omises.

### Taille du bloc ACK

Un récepteur limite le nombre de plages ACK qu'il mémorise et envoie dans les blocs ACK, à la fois pour limiter la taille des blocs ACK et pour éviter l'épuisement des ressources. Après avoir reçu des accusés de réception pour un bloc ACK, le récepteur devrait arrêter de suivre ces plages ACK acquittées. Les expéditeurs peuvent s'attendre à des accusés de réception pour la plupart des paquets, mais ce protocole ne garantit pas la réception d'un accusé de réception pour chaque paquet que le récepteur traite.

Il est possible que conserver de nombreuses plages d'ACK puisse faire qu'un bloc ACK devienne trop volumineux. Un récepteur peut écarter des plages d'ACK non acquittées pour limiter la taille du bloc ACK, au prix de retransmissions accrues de la part de l'expéditeur. Ceci est nécessaire si un bloc ACK serait trop volumineux pour tenir dans un paquet. Les récepteurs peuvent également limiter davantage la taille du bloc ACK pour préserver l'espace pour d'autres blocs ou pour limiter la bande passante que consomment les accusés de réception.

- Défini une fois tous les N paquets, pour un petit N
- Défini sur le dernier d'une rafale de paquets
- Défini chaque fois que la fenêtre d'envoi est presque pleine, par exemple plus de 2/3 pleine
- Défini sur tous les paquets avec des fragments retransmis

Un récepteur doit conserver une plage d'ACK à moins qu'il puisse s'assurer qu'il n'acceptera pas par la suite des paquets avec des numéros dans cette plage. Maintenir un numéro de paquet minimum qui augmente au fur et à mesure que les plages sont supprimées est une façon d'y parvenir avec un état minimal.

### Limitation des plages par suivi des blocs ACK

Les récepteurs peuvent ignorer toutes les plages ACK, mais ils doivent conserver le plus grand numéro de paquet qui a été traité avec succès, car celui-ci est utilisé pour récupérer les numéros de paquets des paquets suivants.

La section suivante décrit une approche exemplaire pour déterminer quels paquets accuser réception dans chaque bloc ACK. Bien que l'objectif de cet algorithme soit de générer un accusé de réception pour chaque paquet traité, il est toujours possible que les accusés de réception soient perdus.

Lorsqu'un paquet contenant un bloc ACK est envoyé, le champ Ack Through de ce bloc peut être sauvegardé. Lorsqu'un paquet contenant un bloc ACK est accusé de réception, le récepteur peut cesser d'accuser réception des paquets inférieurs ou égaux au champ Ack Through du bloc ACK envoyé.

Un récepteur qui n'envoie que des paquets ne nécessitant pas d'accusé de réception, tels que des blocs ACK, pourrait ne pas recevoir d'accusé de réception pendant une longue période. Cela pourrait amener le récepteur à maintenir l'état d'un grand nombre de blocs ACK pendant une longue période, et les blocs ACK qu'il envoie pourraient être inutilement volumineux. Dans un tel cas, un récepteur pourrait envoyer un PING ou un autre petit bloc nécessitant un accusé de réception de temps en temps, par exemple une fois par aller-retour, pour solliciter un ACK du pair.

Dans les cas sans perte de bloc ACK, cet algorithme permet un minimum de 1 RTT de réordonnancement. Dans les cas avec perte de bloc ACK et réordonnancement, cette approche ne garantit pas que chaque accusé de réception soit vu par l'expéditeur avant qu'il ne soit plus inclus dans le bloc ACK. Les paquets pourraient être reçus dans le désordre, et tous les blocs ACK suivants les contenant pourraient être perdus. Dans ce cas, l'algorithme de récupération de perte pourrait causer des retransmissions parasites, mais l'expéditeur continuera à progresser.

Les transports I2P ne garantissent pas la livraison dans l'ordre des messages I2NP. Par conséquent, la perte d'un message Data contenant un ou plusieurs messages ou fragments I2NP n'empêche PAS la livraison d'autres messages I2NP ; il n'y a pas de blocage en tête de ligne. Les implémentations devraient continuer à envoyer de nouveaux messages pendant la phase de récupération de perte si la fenêtre d'envoi le permet.

Un expéditeur ne devrait pas conserver le contenu intégral d'un message pour le retransmettre de manière identique (sauf pour les messages de handshake, voir ci-dessus). Un expéditeur doit assembler des messages contenant des informations à jour (ACKs, NACKs, et données non acquittées) à chaque fois qu'il envoie un message. Un expéditeur devrait éviter de retransmettre des informations provenant de messages une fois qu'ils sont acquittés. Cela inclut les messages qui sont acquittés après avoir été déclarés perdus, ce qui peut arriver en présence de réordonnancement réseau.

### Congestion

À déterminer. Des conseils généraux peuvent être trouvés dans [RFC-9002](https://tools.ietf.org/html/rfc9002).

L'IP ou le port d'un pair peut changer pendant la durée de vie d'une session. Un changement d'IP peut être causé par la rotation d'adresse temporaire IPv6, un changement d'IP périodique imposé par le FAI, un client mobile transitant entre les IP WiFi et cellulaires, ou d'autres changements de réseau local. Un changement de port peut être causé par une nouvelle liaison NAT après l'expiration de la liaison précédente.

L'IP ou le port d'un pair peut sembler changer en raison de diverses attaques sur le chemin de communication et hors chemin, incluant la modification ou l'injection de paquets.

### Retransmission

La migration de connexion est le processus par lequel un nouveau point de terminaison source (IP+port) est validé, tout en empêchant les changements qui ne sont pas validés. Ce processus est une version simplifiée de celui défini dans QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000). Ce processus n'est défini que pour la phase de données d'une session. La migration n'est pas autorisée pendant la poignée de main. Tous les paquets de poignée de main doivent être vérifiés comme provenant de la même IP et du même port que les paquets précédemment envoyés et reçus. En d'autres termes, l'IP et le port d'un pair doivent être constants pendant la poignée de main.

### Fenêtre

(Adapté de QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000))

### Modèle de menace

Un pair peut usurper son adresse source pour amener un endpoint à envoyer des quantités excessives de données vers un hôte non consentant. Si l'endpoint envoie significativement plus de données que le pair usurpateur, la migration de connexion pourrait être utilisée pour amplifier le volume de données qu'un attaquant peut générer vers une victime.

## Migration de Connexion

Un attaquant sur le chemin pourrait provoquer une migration de connexion fallacieuse en copiant et transférant un paquet avec une adresse usurpée de sorte qu'il arrive avant le paquet original. Le paquet avec l'adresse usurpée sera perçu comme provenant d'une connexion en migration, et le paquet original sera considéré comme un doublon et supprimé. Après une migration fallacieuse, la validation de l'adresse source échouera car l'entité à l'adresse source ne possède pas les clés cryptographiques nécessaires pour lire ou répondre au Path Challenge qui lui est envoyé, même si elle le souhaitait.

Un attaquant hors-chemin qui peut observer les paquets pourrait transmettre des copies de paquets authentiques vers les points de terminaison. Si le paquet copié arrive avant le paquet authentique, cela apparaîtra comme une re-liaison NAT. Tout paquet authentique sera rejeté comme un duplicata. Si l'attaquant est capable de continuer à transmettre des paquets, il pourrait être en mesure de provoquer une migration vers un chemin via l'attaquant. Cela place l'attaquant sur le chemin, lui donnant la capacité d'observer ou de supprimer tous les paquets suivants.

QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) spécifie de changer les ID de connexion lors du changement de chemins réseau. L'utilisation d'un ID de connexion stable sur plusieurs chemins réseau permettrait à un observateur passif de corréler l'activité entre ces chemins. Un endpoint qui se déplace entre les réseaux pourrait ne pas souhaiter que son activité soit corrélée par une entité autre que son pair. Cependant, QUIC ne chiffre pas les ID de connexion dans l'en-tête. SSU2 le fait, donc la fuite de confidentialité nécessiterait que l'observateur passif ait également accès à la base de données réseau pour obtenir la clé d'introduction requise pour déchiffrer l'ID de connexion. Même avec la clé d'introduction, ce n'est pas une attaque forte, et nous ne changeons pas les ID de connexion après migration dans SSU2, car cela constituerait une complication significative.

### Initiation de la validation du chemin

Pendant la phase de données, les pairs doivent vérifier que l'IP source et le port de chaque paquet de données reçu. Si l'IP ou le port est différent de celui reçu précédemment, ET que le paquet n'est pas un numéro de paquet dupliqué, ET que le paquet se décrypte avec succès, la session entre dans la phase de validation de chemin.

#### Sélection d'Introducer

De plus, un pair doit vérifier que la nouvelle IP et le nouveau port sont valides selon les règles de validation locales (non bloqués, ports non interdits, etc.). Les pairs ne sont PAS tenus de prendre en charge la migration entre IPv4 et IPv6, et peuvent traiter une nouvelle IP dans l'autre famille d'adresses comme invalide, car ce n'est pas un comportement attendu et cela peut ajouter une complexité d'implémentation significative. À la réception d'un paquet provenant d'une IP/port invalide, une implémentation peut simplement l'ignorer, ou peut initier une validation de chemin avec l'ancienne IP/port.

#### Gestion des réponses

En entrant dans la phase de validation du chemin, suivez les étapes suivantes :

#### Introducers

Pendant la phase de validation du chemin, la session peut continuer à traiter les paquets entrants. Qu'ils proviennent de l'ancienne ou de la nouvelle IP/port. La session peut également continuer à envoyer et accuser réception des paquets de données. Cependant, la fenêtre de congestion et le PMTU doivent rester aux valeurs minimales pendant la phase de validation du chemin, pour éviter d'être utilisés pour des attaques par déni de service en envoyant de grandes quantités de trafic vers une adresse usurpée.

#### Masquage d'identité

Une implémentation peut, mais n'est pas tenue, de tenter de valider plusieurs chemins simultanément. Cela ne vaut probablement pas la complexité. Elle peut, mais n'est pas tenue, de se souvenir qu'une IP/port précédente a déjà été validée, et d'ignorer la validation de chemin si un pair revient à son IP/port précédent.

### Contenu du message

Si une réponse de chemin (Path Response) est reçue, contenant les données identiques envoyées dans le défi de chemin (Path Challenge), la validation de chemin a réussi. L'IP/port source du message de réponse de chemin n'est pas obligé d'être le même que celui auquel le défi de chemin a été envoyé.

Si une Path Response n'est pas reçue avant l'expiration du minuteur Path Response, envoyer un autre Path Challenge et doubler le minuteur Path Response.

Si une Réponse de Chemin n'est pas reçue avant l'expiration du minuteur de Validation de Chemin, la Validation de Chemin a échoué.

- Démarrer un minuteur de timeout de validation de chemin de plusieurs secondes, ou plusieurs fois le RTO actuel (à déterminer)
- Réduire la fenêtre de congestion au minimum
- Réduire le PMTU au minimum (1280)
- Envoyer un paquet de données contenant un bloc Path Challenge, un bloc Address (contenant la nouvelle IP/port), et, typiquement, un bloc ACK, vers la nouvelle IP et le port. Ce paquet utilise le même ID de connexion et les mêmes clés de chiffrement que la session actuelle. Les données du bloc Path Challenge doivent contenir une entropie suffisante (au moins 8 octets) pour qu'elles ne puissent pas être usurpées.
- Optionnellement, envoyer aussi un Path Challenge vers l'ancienne IP/port, avec des données de bloc différentes. Voir ci-dessous.
- Démarrer un minuteur de timeout Path Response basé sur le RTO actuel (typiquement RTT + un multiple de RTTdev)

Les messages Data doivent contenir les blocs suivants. L'ordre n'est pas spécifié sauf que Padding doit être en dernier :

Il n'est pas recommandé d'inclure d'autres blocs (par exemple, I2NP) dans le message.

Il est autorisé d'inclure un bloc Path Challenge dans le message contenant la Path Response, pour initier une validation dans l'autre direction.

Les blocs Path Challenge et Path Response déclenchent des ACK. Le Path Challenge sera acquitté par un message Data contenant les blocs Path Response et ACK. Le Path Response devrait être acquitté par un message Data contenant un bloc ACK.

La spécification QUIC n'est pas claire sur l'endroit où envoyer les paquets de données pendant la validation de chemin - vers l'ancienne ou la nouvelle IP/port ? Il faut trouver un équilibre entre répondre rapidement aux changements d'IP/port, et ne pas envoyer de trafic vers des adresses usurpées. De plus, les paquets usurpés ne doivent pas être autorisés à impacter substantiellement une session existante. Les changements de port uniquement sont probablement causés par une re-liaison NAT après une période d'inactivité ; les changements d'IP pourraient survenir pendant des phases de trafic intense dans une ou les deux directions.

### Routage pendant la validation de chemin

Les stratégies font l'objet de recherches et d'améliorations. Les possibilités incluent :

- Bloc Path Challenge ou Path Response. Path Challenge contient des données opaques, 8 octets minimum recommandés. Path Response contient les données du Path Challenge.
- Bloc d'adresse contenant l'IP apparente du destinataire
- Bloc DateTime
- Bloc ACK
- Bloc de remplissage

À la réception d'un Path Challenge, le pair doit répondre avec un paquet de données contenant une Path Response, avec les données du Path Challenge.

La réponse de chemin (Path Response) doit être envoyée à l'IP/port depuis lequel le défi de chemin (Path Challenge) a été reçu. Ce n'est PAS NÉCESSAIREMENT l'IP/port qui avait été précédemment établi pour le pair. Cela garantit que la validation de chemin par un pair ne réussit que si le chemin est fonctionnel dans les deux directions. Voir la section Validation après changement local ci-dessous.

Sauf si l'IP/port est différent de l'IP/port précédemment connu pour le pair, traiter un Path Challenge comme un simple ping, et simplement répondre inconditionnellement avec un Path Response. Le récepteur ne conserve ni ne modifie aucun état basé sur un Path Challenge reçu. Si l'IP/port est différent, un pair doit vérifier que la nouvelle IP et le port sont valides selon les règles de validation locales (non bloqués, pas de ports illégaux, etc.). Les pairs ne sont PAS tenus de prendre en charge les réponses inter-familles d'adresses entre IPv4 et IPv6, et peuvent traiter une nouvelle IP dans l'autre famille d'adresses comme invalide, car ce n'est pas un comportement attendu.

### Réponse au défi de chemin

Sauf si elle est contrainte par le contrôle de congestion, la Path Response devrait être envoyée immédiatement. Les implémentations devraient prendre des mesures pour limiter le débit des Path Responses ou la bande passante utilisée si nécessaire.

Un bloc Path Challenge est généralement accompagné d'un bloc Address dans le même message. Si le bloc d'adresse contient une nouvelle IP/port, un pair peut valider cette IP/port et initier un test de pair de cette nouvelle IP/port, avec le pair de session ou tout autre pair. Si le pair pense qu'il est derrière un pare-feu, et que seul le port a changé, ce changement est probablement dû à une re-liaison NAT, et des tests de pair supplémentaires ne sont probablement pas nécessaires.

- Ne pas envoyer de paquets de données vers la nouvelle IP/port tant qu'elle n'est pas validée
- Continuer à envoyer des paquets de données vers l'ancienne IP/port jusqu'à ce que la nouvelle IP/port soit validée
- Revalider simultanément l'ancienne IP/port
- Ne pas envoyer de données tant que l'ancienne ou la nouvelle IP/port n'est pas validée
- Stratégies différentes pour un changement de port uniquement par rapport à un changement d'IP
- Stratégies différentes pour un changement IPv6 dans le même /32, probablement causé par une rotation d'adresse temporaire

### Validation de chemin réussie

Lors de la validation réussie du chemin, la connexion est entièrement migrée vers la nouvelle IP/port. En cas de succès :

Pendant la phase de validation de chemin, tous les paquets valides et non dupliqués qui sont reçus depuis l'ancienne IP/port et qui sont déchiffrés avec succès entraîneront l'annulation de la validation de chemin. Il est important qu'une validation de chemin annulée, causée par un paquet usurpé, n'entraîne pas la terminaison ou la perturbation significative d'une session valide.

En cas d'annulation de validation de chemin :

Il est important qu'une validation de chemin échouée, causée par un paquet usurpé, n'entraîne pas la terminaison ou la perturbation significative d'une session valide.

En cas d'échec de validation du chemin :

### Annulation de la validation du chemin

Le processus ci-dessus est défini pour les pairs qui reçoivent un paquet depuis une IP/port modifiée. Cependant, il peut également être initié dans l'autre direction, par un pair qui détecte que son IP ou son port ont changé. Un pair peut être capable de détecter que son IP locale a changé ; cependant, il est beaucoup moins probable qu'il détecte que son port a changé à cause d'une liaison NAT. Par conséquent, ceci est optionnel.

- Quitter la phase de validation du chemin
- Tous les paquets sont envoyés vers la nouvelle IP et le nouveau port.
- Les restrictions sur la fenêtre de congestion et PMTU sont supprimées, et elles sont autorisées à augmenter. Ne pas simplement les restaurer aux anciennes valeurs, car le nouveau chemin peut avoir des caractéristiques différentes.
- Si l'IP a changé, définir le RTT calculé et le RTO aux valeurs initiales. Étant donné que les changements de port uniquement sont généralement le résultat d'une re-liaison NAT ou d'une autre activité de middlebox, le pair peut à la place conserver son état de contrôle de congestion et son estimation de temps d'aller-retour dans ces cas au lieu de revenir aux valeurs initiales.
- Supprimer (invalider) tous les tokens envoyés ou reçus pour l'ancienne IP/port (optionnel)
- Envoyer un nouveau bloc de token pour la nouvelle IP/port (optionnel)

### Échec de la validation du chemin

À la réception d'un défi de chemin d'un pair dont l'IP ou le port a changé, l'autre pair devrait initier un défi de chemin dans l'autre direction.

Les blocs Path Challenge et Path Response peuvent être utilisés à tout moment comme paquets Ping/Pong. La réception d'un bloc Path Challenge ne modifie aucun état au niveau du récepteur, sauf s'il est reçu depuis une IP/port différente.

- Sortir de la phase de validation du chemin
- Tous les paquets sont envoyés vers l'ancienne IP et le port.
- Les restrictions sur la fenêtre de congestion et le PMTU sont supprimées, et ils sont autorisés à augmenter, ou, optionnellement, restaurer les valeurs précédentes
- Retransmettre tous les paquets de données qui ont été précédemment envoyés vers la nouvelle IP/port vers l'ancienne IP/port.

### Validation Après Modification Locale

Les pairs ne devraient pas établir plusieurs sessions avec le même pair, que ce soit SSU 1 ou 2, ou avec les mêmes adresses IP ou des adresses IP différentes. Cependant, cela pourrait arriver, soit à cause de bogues, soit parce qu'un message de fin de session précédent a été perdu, ou dans une situation de concurrence où le message de fin n'est pas encore arrivé.

Si Bob a une session existante avec Alice, lorsque Bob reçoit le Session Confirmed d'Alice, complétant la poignée de main et établissant une nouvelle session, Bob devrait :

- Quitter la phase de validation de chemin
- Tous les paquets sont envoyés vers l'ancienne IP et le port.
- Les restrictions sur la fenêtre de congestion et le PMTU sont supprimées, et ils sont autorisés à augmenter.
- Optionnellement, démarrer une validation de chemin sur l'ancienne IP et le port. Si elle échoue, terminer la session.
- Sinon, suivre les règles standard de timeout et de terminaison de session.
- Retransmettre tous les paquets de données qui ont été précédemment envoyés vers la nouvelle IP/port vers l'ancienne IP/port.

### Utiliser comme Ping/Pong

Les sessions en phase de handshake sont généralement terminées simplement par expiration de délai, ou en ne répondant plus. Optionnellement, elles peuvent être terminées en incluant un bloc de Termination dans la réponse, mais la plupart des erreurs ne peuvent pas recevoir de réponse en raison de l'absence de clés cryptographiques. Même si des clés sont disponibles pour une réponse incluant un bloc de termination, il n'est généralement pas rentable d'utiliser le CPU pour effectuer le DH pour la réponse. Une exception PEUT être un bloc de Termination dans un message de nouvelle tentative, qui est peu coûteux à générer.

Les sessions dans la phase de données sont terminées en envoyant un message de données qui inclut un bloc de Terminaison. Ce message devrait également inclure un bloc ACK. Il peut, si la session a été active assez longtemps pour qu'un token précédemment envoyé ait expiré ou soit sur le point d'expirer, inclure un bloc New Token. Ce message ne nécessite pas d'accusé de réception. Lors de la réception d'un bloc de Terminaison avec n'importe quelle raison excepté "Termination Received", le pair répond avec un message de données contenant un bloc de Terminaison avec la raison "Termination Received".

### Phase de handshake

Après avoir envoyé ou reçu un bloc de Terminaison, la session devrait entrer dans la phase de fermeture pour une période maximale de temps à déterminer. L'état de fermeture est nécessaire pour se protéger contre la perte du paquet contenant le bloc de Terminaison, et les paquets en transit dans l'autre direction. Pendant la phase de fermeture, il n'est pas nécessaire de traiter des paquets reçus supplémentaires. Une session dans l'état de fermeture envoie un paquet contenant un bloc de Terminaison en réponse à tout paquet entrant qu'elle attribue à la session. Une session devrait limiter le taux auquel elle génère des paquets dans l'état de fermeture. Par exemple, une session pourrait attendre un nombre progressivement croissant de paquets reçus ou une durée de temps avant de répondre aux paquets reçus.

## Sessions multiples

Pour minimiser l'état qu'un router maintient pour une session en cours de fermeture, les sessions peuvent, mais ne sont pas tenues de, envoyer exactement le même paquet avec le même numéro de paquet tel quel en réponse à tout paquet reçu. Note : Permettre la retransmission d'un paquet de terminaison est une exception à l'exigence qu'un nouveau numéro de paquet soit utilisé pour chaque paquet. L'envoi de nouveaux numéros de paquet présente principalement un avantage pour la récupération de perte et le contrôle de congestion, qui ne sont pas censés être pertinents pour une connexion fermée. Retransmettre le paquet final nécessite moins d'état.

Après avoir reçu un bloc Termination avec la raison "Termination Received", la session peut quitter la phase de fermeture.

- Migrer tous les messages I2NP sortants non envoyés ou non accusés de réception de l'ancienne session vers la nouvelle
- Envoyer une terminaison avec le code de raison 22 sur l'ancienne session
- Supprimer l'ancienne session et la remplacer par la nouvelle

## Arrêt de session

### Phase de données

Lors de toute terminaison normale ou anormale, les routers doivent effacer toutes les données éphémères en mémoire, y compris les clés éphémères de handshake, les clés cryptographiques symétriques et les informations associées.

### Nettoyage

Les exigences varient selon que l'adresse publiée est partagée avec SSU 1. Le minimum IPv4 actuel pour SSU 1 est de 620, ce qui est définitivement trop petit.

La MTU SSU2 minimale est de 1280 pour IPv4 et IPv6, ce qui est identique à ce qui est spécifié dans [RFC-9000](https://tools.ietf.org/html/rfc9000). Voir ci-dessous. En augmentant la MTU minimale, les messages de tunnel de 1 Ko et les messages courts de construction de tunnel tiendront dans un datagramme, réduisant considérablement la quantité typique de fragmentation. Cela permet également une augmentation de la taille maximale des messages I2NP. Les messages de streaming de 1820 octets devraient tenir dans deux datagrammes.

Un router ne doit pas activer SSU2 ou publier une adresse SSU2 à moins que le MTU pour cette adresse soit d'au moins 1280.

Les routers doivent publier une MTU non-par-défaut dans chaque adresse de router SSU ou SSU2.

### Adresse SSU

Adresse partagée avec SSU 1, doit suivre les règles SSU 1. IPv4 : Par défaut et maximum est 1484. Minimum est 1292. (MTU IPv4 + 4) doit être un multiple de 16. IPv6 : Doit être publié, minimum est 1280 et maximum est 1488. MTU IPv6 doit être un multiple de 16.

## MTU

IPv4 : Par défaut et maximum est 1500. Minimum est 1280. IPv6 : Par défaut et maximum est 1500. Minimum est 1280. Pas de règles de multiple de 16, mais devrait probablement être un multiple de 2 au moins.

Pour SSU 1, l'implémentation Java I2P actuelle effectue la découverte PMTU en commençant avec de petits paquets et en augmentant progressivement la taille, ou en augmentant basée sur la taille des paquets reçus. Cette méthode est rudimentaire et réduit considérablement l'efficacité. La continuation de cette fonctionnalité dans SSU 2 est à déterminer.

Des études récentes [PMTU](https://en.wikipedia.org/wiki/Path_MTU_Discovery) suggèrent qu'un minimum de 1200 octets ou plus pour IPv4 fonctionnerait pour plus de 99% des connexions. QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) exige une taille minimale de paquet IP de 1280 octets.

cite [RFC-9000](https://tools.ietf.org/html/rfc9000) :

### Adresse SSU2

La taille maximale de datagramme est définie comme la plus grande taille de charge utile UDP qui peut être envoyée à travers un chemin réseau en utilisant un seul datagramme UDP. QUIC NE DOIT PAS être utilisé si le chemin réseau ne peut pas prendre en charge une taille maximale de datagramme d'au moins 1200 octets.

### Découverte PMTU

QUIC assume une taille minimale de paquet IP d'au moins 1280 octets. Il s'agit de la taille minimale IPv6 [IPv6] et elle est également prise en charge par la plupart des réseaux IPv4 modernes. En supposant la taille minimale d'en-tête IP de 40 octets pour IPv6 et 20 octets pour IPv4 et une taille d'en-tête UDP de 8 octets, cela résulte en une taille maximale de datagramme de 1232 octets pour IPv6 et 1252 octets pour IPv4. Ainsi, les réseaux IPv4 modernes et tous les chemins réseau IPv6 sont censés pouvoir prendre en charge QUIC.

### Taille minimale du handshake

Note : Cette exigence de prendre en charge une charge utile UDP de 1200 octets limite l'espace disponible pour les en-têtes d'extension IPv6 à 32 octets ou les options IPv4 à 52 octets si le chemin ne prend en charge que le MTU minimum IPv6 de 1280 octets. Cela affecte les paquets Initial et la validation de chemin.

fin de citation

QUIC exige que les datagrammes Initial dans les deux directions fassent au moins 1200 octets, pour éviter les attaques d'amplification et s'assurer que le PMTU le prend en charge dans les deux directions.

Nous pourrions exiger ceci pour Session Request et Session Created, au prix d'un coût substantiel en bande passante. Peut-être pourrions-nous faire cela seulement si nous n'avons pas de jeton, ou après réception d'un message Retry. À déterminer

QUIC exige que Bob n'envoie pas plus de trois fois la quantité de données reçues jusqu'à ce que l'adresse du client soit validée. SSU2 répond intrinsèquement à cette exigence, car le message Retry fait à peu près la même taille que le message Token Request, et est plus petit que le message Session Request. De plus, le message Retry n'est envoyé qu'une seule fois.

QUIC exige que les messages contenant des blocs PATH_CHALLENGE ou PATH_RESPONSE fassent au moins 1200 octets, pour prévenir les attaques d'amplification et s'assurer que le PMTU le prend en charge dans les deux directions.

Nous pourrions également l'exiger, au prix d'un coût substantiel en bande passante. Cependant, ces cas devraient être rares. À déterminer

### Taille minimale du message de chemin

IPv4 : Aucune fragmentation IP n'est supposée. L'en-tête IP + datagramme fait 28 octets. Ceci suppose qu'il n'y a pas d'options IPv4. La taille maximale du message est MTU - 28. L'en-tête de la phase de données fait 16 octets et le MAC fait 16 octets, totalisant 32 octets. La taille de la charge utile est MTU - 60. La charge utile maximale de la phase de données est de 1440 pour un MTU maximum de 1500. La charge utile maximale de la phase de données est de 1220 pour un MTU minimum de 1280.

IPv6 : Aucune fragmentation IP n'est autorisée. L'en-tête IP + datagramme fait 48 octets. Ceci suppose qu'il n'y a pas d'en-têtes d'extension IPv6. La taille maximale du message est MTU - 48. L'en-tête de phase de données fait 16 octets et le MAC fait 16 octets, totalisant 32 octets. La taille de la charge utile est MTU - 80. La charge utile maximale de la phase de données est de 1420 pour un MTU maximum de 1500. La charge utile maximale de la phase de données est de 1200 pour un MTU minimum de 1280.

Dans SSU 1, les directives étaient un maximum strict d'environ 32 Ko pour un message I2NP basé sur 64 fragments maximum et un MTU minimum de 620. En raison de la surcharge pour les LeaseSets groupés et les clés de session, la limite pratique au niveau de l'application était d'environ 6 Ko de moins, soit environ 26 Ko. Le protocole SSU 1 permet 128 fragments mais les implémentations actuelles le limitent à 64 fragments.

### Taille maximale des messages I2NP

En augmentant le MTU minimum à 1280, avec une charge utile de phase de données d'environ 1200, un message SSU 2 d'environ 76 Ko est possible en 64 fragments et 152 Ko en 128 fragments. Cela permet facilement un maximum de 64 Ko.

En raison de la fragmentation dans les tunnels et de la fragmentation dans SSU 2, les chances de perte de messages augmentent de manière exponentielle avec la taille des messages. Nous continuons à recommander une limite pratique d'environ 10 KB au niveau de la couche application pour les datagrammes I2NP.

### Versions

Voir Sécurité des Tests de Pairs ci-dessus pour une analyse du Test de Pairs SSU1 et les objectifs du Test de Pairs SSU2.

Lorsque rejeté par Bob :

Lorsque rejeté par Charlie :

REMARQUE : Les RI peuvent être envoyés soit sous forme de messages I2NP Database Store dans des blocs I2NP, soit sous forme de blocs RI (s'ils sont suffisamment petits). Ils peuvent être contenus dans les mêmes paquets que les blocs de test de pairs, s'ils sont suffisamment petits.

Les messages 1-4 sont en session utilisant des blocs Peer Test dans un message Data. Les messages 5-7 sont hors session utilisant des blocs Peer Test dans un message Peer Test.

## Processus de test de pairs

NOTE : Comme dans SSU 1, les messages 4 et 5 peuvent arriver dans n'importe quel ordre. Les messages 5 et/ou 7 peuvent ne pas être reçus du tout si Alice est derrière un pare-feu. Lorsque le message 5 arrive avant le message 4, Alice ne peut pas envoyer immédiatement le message 6, car elle n'a pas encore la clé d'introduction de Charlie pour chiffrer l'en-tête. Lorsque le message 4 arrive avant le message 5, Alice ne devrait pas envoyer immédiatement le message 6, car elle devrait attendre de voir si le message 5 arrive sans ouvrir le pare-feu avec le message 6.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest
        <---------------- Charlie RI
4.      <------------------ PeerTest

5.      <----------------------------------------- PeerTest
6. PeerTest ----------------------------------------->
7.      <----------------------------------------- PeerTest
```
Les tests de pairs inter-versions ne sont pas pris en charge. La seule combinaison de versions autorisée est celle où tous les pairs sont en version 2.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
4.      <------------------ PeerTest (reject)
```
Les messages 1-4 sont en session et sont couverts par les processus d'ACK et de retransmission de la phase de données. Les blocs Peer Test déclenchent un accusé de réception.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest (reject)
                      (optional: Bob could try another Charlie here)
4.      <------------------ PeerTest (reject)
```
Les messages 5-7 peuvent être retransmis, sans modification.

Comme dans SSU 1, les tests d'adresses IPv6 sont pris en charge, et la communication Alice-Bob et Alice-Charlie peut se faire via IPv6, si Bob et Charlie indiquent leur support avec une capacité 'B' dans leur adresse IPv6 publiée. Voir la Proposition 126 pour plus de détails.

Comme dans SSU 1 avant la version 0.9.50, Alice envoie la demande à Bob en utilisant une session existante sur le transport (IPv4 ou IPv6) qu'elle souhaite tester. Lorsque Bob reçoit une demande d'Alice via IPv4, Bob doit sélectionner un Charlie qui annonce une adresse IPv4. Lorsque Bob reçoit une demande d'Alice via IPv6, Bob doit sélectionner un Charlie qui annonce une adresse IPv6. La communication réelle Bob-Charlie peut se faire via IPv4 ou IPv6 (c'est-à-dire, indépendamment du type d'adresse d'Alice). Ce n'est PAS le comportement de SSU 1 depuis la version 0.9.50, où les demandes mixtes IPv4/v6 sont autorisées.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Path</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Intro Key</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->C session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->A session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->C</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
  </tbody>
</table>
### Retransmissions

Contrairement à SSU 1, Alice spécifie l'IP et le port de test demandés dans le message 1. Bob devrait valider cette IP et ce port, et rejeter avec le code 5 s'ils sont invalides. La validation IP recommandée est que, pour IPv4, elle corresponde à l'IP d'Alice, et pour IPv6, au moins les 8 premiers octets de l'IP correspondent. La validation du port devrait rejeter les ports privilégiés et les ports pour les protocoles bien connus.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### Notes IPv6

Nous documentons ici comment Alice peut déterminer les résultats d'un test de pair, en fonction des messages reçus. Les améliorations de SSU2 nous offrent l'opportunité de corriger, améliorer et mieux documenter la machine d'état des résultats de test de pair par rapport à celle de [SSU](/docs/transport/ssu).

Pour chaque type d'adresse testé (IPv4 ou IPv6), le résultat peut être UNKNOWN, OK, FIREWALLED, ou SYMNAT. De plus, d'autres traitements peuvent être effectués pour détecter un changement d'IP ou de port, ou un port externe différent du port interne.

### Traitement par Bob

Problèmes avec la machine à états SSU documentée :

Ainsi, contrairement à SSU, nous recommandons d'attendre plusieurs secondes après avoir reçu le message 4, puis d'envoyer le message 6 même si le message 5 n'est pas reçu.

### Machine d'état des résultats

Un résumé de la machine d'état, basé sur la réception ou non des messages 4, 5 et 7 (oui ou non), est le suivant :

### Retransmissions

Une machine d'état plus détaillée, avec vérifications de l'IP/port reçus dans le bloc d'adresse du message 7, est présentée ci-dessous. Un défi consiste à déterminer si vous (Alice) êtes celui qui est derrière un NAT symétrique, ou si c'est Charlie.

Un post-traitement ou une logique supplémentaire pour confirmer les transitions d'état en exigeant les mêmes résultats sur deux tests de pairs ou plus est recommandé.

La validation et la confirmation de l'IP/port reçues par deux tests ou plus, ou avec le bloc d'adresse dans les messages Session Created, sont également recommandées, mais sortent du cadre de cette spécification.

- Nous n'envoyons jamais le message 6 à moins d'avoir reçu le message 5, donc nous ne savons jamais si nous sommes SYMNAT
- Si nous AVONS reçu les messages 4 et 7, comment pourrions-nous être SYMNAT
- Si l'IP ne correspondait pas mais que le port correspondait, nous ne sommes pas SYMNAT, nous avons juste changé notre IP

Voir la section Sécurité des relais ci-dessus pour une analyse du relais SSU1 et les objectifs du relais SSU2.

Quand rejeté par Bob :

```
4 5 7  Result             Notes
-----  ------             -----
n n n  UNKNOWN
y n n  FIREWALLED           (unless currently SYMNAT)
n y n  OK                   (unless currently SYMNAT, which is unlikely)
y y n  OK                   (unless currently SYMNAT, which is unlikely)
n n y  n/a                  (can't send msg 6)
y n y  FIREWALLED or SYMNAT (requires sending msg 6 w/o rcv msg 5)
n y y  n/a                  (can't send msg 6)
y y y  OK
```
Quand rejeté par Charlie :

NOTE : Les RI peuvent être envoyés soit dans des messages I2NP Database Store dans des blocs I2NP, soit sous forme de blocs RI (s'ils sont assez petits). Ceux-ci peuvent être contenus dans les mêmes paquets que les blocs de relais, s'ils sont assez petits.

Dans SSU 1, les informations du routeur de Charlie contiennent l'IP, le port, la clé d'introduction, le tag de relais et l'expiration de chaque introducer.

```
If Alice does not get msg 5:
   If Alice does not get msg 4: -> UNKNOWN
   If Alice does not get msg 7: -> UNKNOWN
   If Alice gets msgs 4/7 and IP/port match: -> FIREWALLED
   If Alice gets msgs 4/7 and IP matches, port does not match:
      -> SYMNAT, but needs confirmation with 2nd test
   If Alice gets msgs 4/7 and IP does not match, port matches:
      -> FIREWALLED, address change?
   If Alice gets msgs 4/7 and both IP and port do not match:
      -> SYMNAT, address change?

If Alice gets msg 5:
   If Alice does not get msg 4: -> OK unless currently SYMNAT, else UNKNOWN
                                   (in SSU2 have to stop here)
   If Alice does not get msg 7: -> OK unless currently SYMNAT, else UNKNOWN
   If Alice gets msgs 4/5/7 and IP/port match: -> OK
   If Alice gets msgs 4/5/7 and IP matches, port does not match:
      -> OK, charlie is probably sym. natted
   If Alice gets msgs 4/5/7 and IP does not match, port matches:
      -> OK, address change?
   If Alice gets msgs 4/5/7 and both IP and port do not match:
      -> OK, address change?
```
## Processus de relais

Dans SSU 2, les informations de routeur de Charlie contiennent le hash du routeur, l'étiquette de relais et l'expiration de chaque introducer.

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse

5.      <-------------------------------------------- HolePunch
6. SessionRequest -------------------------------------------->
7.      <-------------------------------------------- SessionCreated
8. SessionConfirmed ------------------------------------------>
```
Alice devrait réduire le nombre d'allers-retours requis en sélectionnant d'abord un introducer (Bob) auquel elle a déjà une connexion. Deuxièmement, si aucun n'est disponible, sélectionner un introducer pour lequel elle possède déjà les informations de router.

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
4.      <-------------- RelayResponse
```
Le relayage inter-versions devrait également être pris en charge si possible. Cela facilitera une transition progressive de SSU 1 vers SSU 2. Les combinaisons de versions autorisées sont (TODO) :

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse
```
Relay Request, Relay Intro et Relay Response sont tous en session et sont couverts par les processus d'ACK et de retransmission de la phase de données. Les blocs Relay Request, Relay Intro et Relay Response déclenchent un accusé de réception.

Notez qu'habituellement, Charlie répondra immédiatement à un Relay Intro avec une Relay Response, qui devrait inclure un bloc ACK. Dans ce cas, aucun message séparé avec un bloc ACK n'est requis.

Le hole punch peut être retransmis, comme dans SSU 1.

Contrairement aux messages I2NP, les messages Relay n'ont pas d'identifiants uniques, donc les doublons doivent être détectés par la machine à états du relais, en utilisant le nonce. Les implémentations peuvent également avoir besoin de maintenir un cache des nonces récemment utilisés, afin que les doublons reçus puissent être détectés même après que la machine à états pour ce nonce ait terminé.

Toutes les fonctionnalités du relais SSU 1 sont prises en charge, y compris celles documentées dans [Prop158](/proposals/158-ipv6-transport-enhancements) et supportées depuis la version 0.9.50. Les introductions IPv4 et IPv6 sont prises en charge. Une Demande de Relais peut être envoyée via une session IPv4 pour une introduction IPv6, et une Demande de Relais peut être envoyée via une session IPv6 pour une introduction IPv4.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/2/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### IPv4/v6

Voici les différences par rapport à SSU 1 et les recommandations pour l'implémentation de SSU 2.

Dans SSU 1, l'introduction est relativement peu coûteuse, et Alice envoie généralement des demandes de relais à tous les introducers. Dans SSU 2, l'introduction est plus coûteuse, car une connexion doit d'abord être établie avec un introducer. Pour minimiser la latence et les frais généraux d'introduction, les étapes de traitement recommandées sont les suivantes :

Dans SSU 1 et SSU 2, la Relay Response et le Hole Punch peuvent être reçus dans n'importe quel ordre, ou peuvent ne pas être reçus du tout.

Dans SSU 1, Alice reçoit généralement la Relay Response (1 RTT) avant le Hole Punch (1 1/2 RTT). Cela pourrait ne pas être bien documenté dans ces spécifications, mais Alice doit recevoir la Relay Response de Bob avant de continuer, pour recevoir l'IP de Charlie. Si le Hole Punch est reçu en premier, Alice ne le reconnaîtra pas, car il ne contient aucune donnée et l'IP source n'est pas reconnue. Après avoir reçu la Relay Response, Alice devrait attendre SOIT de recevoir le Hole Punch de Charlie, SOIT un court délai (500 ms recommandé) avant d'initier la négociation avec Charlie.

### Traitement par Alice

Dans SSU 2, Alice recevra généralement le Hole Punch (1 1/2 RTT) avant la Relay Response (2 RTT). Le Hole Punch SSU 2 est plus facile à traiter que dans SSU 1, car c'est un message complet avec des ID de connexion définis (dérivés du relay nonce) et un contenu incluant l'IP de Charlie. La Relay Response (message Data) et le message Hole Punch contiennent le bloc Relay Response signé identique. Par conséquent, Alice peut initier la négociation avec Charlie après SOIT avoir reçu le Hole Punch de Charlie, SOIT avoir reçu la Relay Response de Bob.

### Demandes de balises par Bob

La vérification de signature du Hole Punch inclut le hash du router de l'introducer (Bob). Si des requêtes de relais ont été envoyées à plus d'un introducer, il existe plusieurs options pour valider la signature :

#### Résumé

Si Charlie se trouve derrière un NAT symétrique, son port signalé dans la Relay Response et le Hole Punch peut ne pas être exact. Par conséquent, Alice devrait vérifier le port source UDP du message Hole Punch, et l'utiliser s'il diffère du port signalé.

- Ignorer tous les introducers qui ont expiré basé sur la valeur iexp dans l'adresse
- Si une connexion SSU2 est déjà établie vers un ou plusieurs introducers, en choisir un et envoyer la Relay Request uniquement à cet introducer.
- Sinon, si une Router Info est connue localement pour un ou plusieurs introducers, en choisir un et se connecter uniquement à cet introducer.
- Sinon, rechercher les Router Infos pour tous les introducers, se connecter à l'introducer dont la Router Info est reçue en premier.

#### Détails

Dans SSU 1, seule Alice pouvait demander un tag, dans la Session Request. Bob ne pouvait jamais demander un tag, et Alice ne pouvait pas relayer pour Bob.

Dans SSU2, Alice demande généralement une étiquette dans la Session Request, mais Alice ou Bob peuvent également demander une étiquette pendant la phase de données. Bob n'est généralement pas derrière un pare-feu après avoir reçu une requête entrante, mais il pourrait l'être après un relais, ou l'état de Bob peut changer, ou il peut demander un introducer pour l'autre type d'adresse (IPv4/v6). Ainsi, dans SSU2, il est possible qu'Alice et Bob soient simultanément des relais l'un pour l'autre.

Les propriétés d'adresse suivantes peuvent être publiées, inchangées par rapport à SSU 1, incluant les modifications de [Prop158](/proposals/158-ipv6-transport-enhancements) supportées à partir de l'API 0.9.50 :

La RouterAddress publiée (partie du RouterInfo) aura un identifiant de protocole soit "SSU" soit "SSU2".

- Essayer chaque hash auquel une requête a été envoyée
- Utiliser des nonces différents pour chaque introducer, et utiliser cela pour déterminer à quel introducer ce Hole Punch était en réponse
- Ne pas revalider la signature si le contenu est identique à celui de la Relay Response, si déjà reçue
- Ne pas valider la signature du tout

La RouterAddress doit contenir trois options pour indiquer la prise en charge de SSU2 :

### Propriétés d'adresse

Alice doit vérifier que les trois options sont présentes et valides avant de se connecter en utilisant le protocole SSU2.

Lorsqu'il est publié comme "SSU" avec les options "s", "i" et "v", et avec les options "host" et "port", le router doit accepter les connexions entrantes sur cet hôte et ce port pour les protocoles SSU et SSU2, et détecter automatiquement la version du protocole.

## Informations du Router Publiées

### Adresses Publiées

Lorsqu'il est publié comme "SSU2" avec les options "s", "i" et "v", et avec les options "host" et "port", le router accepte les connexions entrantes sur cet hôte et ce port pour le protocole SSU2 uniquement.

- caps: capacités [B,C,4,6]
- host: IP (IPv4 ou IPv6). Adresse IPv6 raccourcie (avec "::") autorisée. Peut être présente ou non si derrière un pare-feu. Les noms d'hôtes ne sont pas autorisés.
- iexp[0-2]: Expiration de cet introducer. Chiffres ASCII, en secondes depuis l'époque. Présent uniquement si derrière un pare-feu, et que les introducers sont requis. Optionnel (même si d'autres propriétés pour cet introducer sont présentes).
- ihost[0-2]: IP de l'introducer (IPv4 ou IPv6). Adresse IPv6 raccourcie (avec "::") autorisée. Présent uniquement si derrière un pare-feu, et que les introducers sont requis. Les noms d'hôtes ne sont pas autorisés. Adresse SSU uniquement.
- ikey[0-2]: Clé d'introduction Base 64 de l'introducer. Présent uniquement si derrière un pare-feu, et que les introducers sont requis. Adresse SSU uniquement.
- iport[0-2]: Port de l'introducer 1024 - 65535. Présent uniquement si derrière un pare-feu, et que les introducers sont requis. Adresse SSU uniquement.
- itag[0-2]: Tag de l'introducer 1 - (2**32 - 1) chiffres ASCII. Présent uniquement si derrière un pare-feu, et que les introducers sont requis.
- key: Clé d'introduction Base 64.
- mtu: Optionnel. Voir la section MTU ci-dessus.
- port: 1024 - 65535 Peut être présent ou non si derrière un pare-feu.

### Adresse SSU2 non publiée

Si un router prend en charge les connexions SSU1 et SSU2 mais n'implémente pas la détection automatique de version pour les connexions entrantes, il doit annoncer à la fois les adresses "SSU" et "SSU2", et inclure les options SSU2 uniquement dans l'adresse "SSU2". Le router devrait définir une valeur de coût plus faible (priorité plus élevée) dans l'adresse "SSU2" que dans l'adresse "SSU", afin que SSU2 soit privilégié.

Si plusieurs RouterAddresses SSU2 (soit comme "SSU" ou "SSU2") sont publiées dans la même RouterInfo (pour des adresses IP ou ports supplémentaires), toutes les adresses spécifiant le même port doivent contenir des options et valeurs SSU2 identiques. En particulier, toutes doivent contenir la même clé statique "s" et clé d'introduction "i".

- s=(Clé Base64) La clé publique statique Noise actuelle (s) pour cette RouterAddress. Encodée en Base 64 en utilisant l'alphabet Base 64 standard d'I2P. 32 octets en binaire, 44 octets encodés en Base 64, clé publique X25519 petit-boutiste.
- i=(Clé Base64) La clé d'introduction actuelle pour chiffrer les en-têtes de cette RouterAddress. Encodée en Base 64 en utilisant l'alphabet Base 64 standard d'I2P. 32 octets en binaire, 44 octets encodés en Base 64, clé ChaCha20 gros-boutiste.
- v=2 La version actuelle (2). Lorsque publié comme "SSU", le support additionnel pour la version 1 est implicite. Le support pour les versions futures se fera avec des valeurs séparées par des virgules, par exemple v=2,3. L'implémentation doit vérifier la compatibilité, incluant plusieurs versions si une virgule est présente. Les versions séparées par des virgules doivent être dans l'ordre numérique.

Lorsque publié en tant que SSU ou SSU2 avec des introducers, les options suivantes sont présentes :

Les options suivantes sont uniquement pour SSU et ne sont pas utilisées pour SSU2. Dans SSU2, Alice obtient ces informations depuis le RI de Charlie à la place.

Un router ne doit pas publier l'hôte ou le port dans l'adresse lors de la publication d'introducers. Un router doit publier les capacités 4 et/ou 6 dans l'adresse lors de la publication d'introducers pour indiquer la prise en charge d'IPv4 et/ou d'IPv6. Ceci est identique à la pratique actuelle pour les adresses SSU 1 récentes.

Note : Si publié en tant que SSU, et qu'il y a un mélange d'introducers SSU 1 et SSU2, les introducers SSU 1 devraient être aux index inférieurs et les introducers SSU2 devraient être aux index supérieurs, pour la compatibilité avec les anciens routers.

Si Alice ne publie pas son adresse SSU2 (comme "SSU" ou "SSU2") pour les connexions entrantes, elle doit publier une adresse router "SSU2" contenant uniquement sa clé statique et la version SSU2, afin que Bob puisse valider la clé après avoir reçu le RouterInfo d'Alice dans la partie 2 de Session Confirmed.

#### Gestion des erreurs

Cette adresse de routeur ne contiendra pas d'options "host" ou "port", car celles-ci ne sont pas requises pour les connexions SSU2 sortantes. Le coût publié pour cette adresse n'a pas d'importance stricte, car elle est uniquement entrante ; cependant, il peut être utile pour les autres routeurs si le coût est défini plus élevé (priorité plus faible) que les autres adresses. La valeur suggérée est 14.

- ih[0-2]=(Base64 hash) Un hash de router pour un introducer. Encodé en Base 64 en utilisant l'alphabet Base 64 standard d'I2P. 32 octets en binaire, 44 octets en Base 64 encodé
- iexp[0-2] : Expiration de cet introducer. Inchangé par rapport à SSU 1.
- itag[0-2] : Tag de l'introducer 1 - (2**32 - 1) Inchangé par rapport à SSU 1.

Alice peut également simplement ajouter les options "i", "s" et "v" à une adresse "SSU" publiée existante.

- ihost[0-2]
- ikey[0-2]
- itag[0-2]

L'utilisation des mêmes clés statiques pour NTCP2 et SSU2 est autorisée, mais non recommandée.

En raison de la mise en cache des RouterInfos, les routers ne doivent pas faire tourner la clé publique statique ou l'IV pendant que le router est actif, que ce soit dans une adresse publiée ou non. Les routers doivent stocker de manière persistante cette clé et cet IV pour les réutiliser après un redémarrage immédiat, afin que les connexions entrantes continuent de fonctionner et que les temps de redémarrage ne soient pas exposés. Les routers doivent stocker de manière persistante, ou déterminer autrement, l'heure du dernier arrêt, afin que la durée d'indisponibilité précédente puisse être calculée au démarrage.

### Rotation de la clé publique et du IV

Sous réserve des préoccupations concernant l'exposition des temps de redémarrage, les routers peuvent faire tourner cette clé ou IV au démarrage si le router était précédemment hors service pendant un certain temps (plusieurs jours au moins).

- s=(clé Base64) Comme défini ci-dessus pour les adresses publiées.
- i=(clé Base64) Comme défini ci-dessus pour les adresses publiées.
- v=2 Comme défini ci-dessus pour les adresses publiées.

Si le router a des RouterAddresses SSU2 publiées (en tant que SSU ou SSU2), le temps d'arrêt minimum avant rotation devrait être beaucoup plus long, par exemple un mois, à moins que l'adresse IP locale n'ait changé ou que le router "rekeys".

Si le router a des RouterAddresses SSU publiées, mais pas SSU2 (comme SSU ou SSU2), le temps d'arrêt minimum avant la rotation devrait être plus long, par exemple un jour, à moins que l'adresse IP locale n'ait changé ou que le router ne "rekey". Cela s'applique même si l'adresse SSU publiée a des introducers.

### Création de paquets sortants

Si le router n'a pas de RouterAddresses publiées (SSU, SSU2, ou SSU), le temps d'arrêt minimum avant rotation peut être aussi court que deux heures, même si l'adresse IP change, à moins que le router ne procède à un "rekeys".

Si le router "rekeys" vers un Router Hash différent, il devrait également générer une nouvelle clé noise et une nouvelle clé intro.

Les implémentations doivent être conscientes que modifier la clé publique statique ou l'IV empêchera les connexions SSU2 entrantes des routeurs qui ont mis en cache une RouterInfo plus ancienne. La publication des RouterInfo, la sélection des pairs de tunnel (incluant à la fois OBGW et le saut le plus proche IB), la sélection des tunnels zero-hop, la sélection du transport, et d'autres stratégies d'implémentation doivent prendre cela en compte.

La rotation des clés d'introduction est soumise aux mêmes règles que la rotation des clés.

Note : Le temps d'arrêt minimum avant la regénération des clés peut être modifié pour assurer la santé du réseau et empêcher la reséance par un router arrêté pendant une durée modérée.

La déniabilité n'est pas un objectif. Voir l'aperçu ci-dessus.

Chaque motif se voit attribuer des propriétés décrivant la confidentialité fournie à la clé publique statique de l'initiateur, et à la clé publique statique du répondeur. Les hypothèses sous-jacentes sont que les clés privées éphémères sont sécurisées, et que les parties abandonnent la négociation si elles reçoivent une clé publique statique de l'autre partie en laquelle elles n'ont pas confiance.

Cette section ne considère que la fuite d'identité par le biais des champs de clé publique statiques dans les handshakes. Bien entendu, les identités des participants Noise peuvent être exposées par d'autres moyens, notamment par les champs de charge utile, l'analyse de trafic, ou les métadonnées telles que les adresses IP.

Alice : (8) Chiffré avec confidentialité persistante vers une partie authentifiée.

Bob : (3) Non transmis, mais un attaquant passif peut vérifier les candidats pour la clé privée du répondeur et déterminer si le candidat est correct.

#### Dissimulation de l'identité

Bob publie sa clé publique statique dans la netDb. Alice peut ne pas le faire, mais doit l'inclure dans le RI envoyé à Bob.

Messages de handshake (Session Request/Created/Confirmed, Retry) étapes de base, dans l'ordre :

Étapes de base des messages de phase de données, dans l'ordre :

Traitement initial de tous les messages entrants :

Traitement des messages de handshake (Session Request/Created/Confirmed, Retry, Token Request) et autres messages hors session (Peer Test, Hole Punch) :

Traitement des messages de phase de données :

## Directives pour les paquets

### Gestion des Paquets Entrants

Dans SSU 1, la classification des paquets entrants est difficile, car il n'y a pas d'en-tête pour indiquer le numéro de session. Les routeurs doivent d'abord faire correspondre l'IP source et le port à un état de pair existant, et s'il n'est pas trouvé, tenter plusieurs déchiffrements avec différentes clés pour trouver l'état de pair approprié ou en démarrer un nouveau. Dans le cas où l'IP source ou le port d'une session existante change, possiblement en raison du comportement NAT, le router peut utiliser des heuristiques coûteuses pour tenter de faire correspondre le paquet à une session existante et récupérer le contenu.

- Créer un en-tête de 16 ou 32 octets
- Créer la charge utile
- mixHash() l'en-tête (sauf pour Retry)
- Chiffrer la charge utile en utilisant Noise (sauf pour Retry, utiliser ChaChaPoly avec l'en-tête comme AD)
- Chiffrer l'en-tête, et pour Session Request/Created, la clé éphémère

SSU 2 est conçu pour minimiser l'effort de classification des paquets entrants tout en maintenant la résistance DPI et autres menaces sur le chemin. Le numéro de Connection ID est inclus dans l'en-tête pour tous les types de messages, et chiffré (obfusqué) en utilisant ChaCha20 avec une clé et un nonce connus. De plus, le type de message est également inclus dans l'en-tête (chiffré avec une protection d'en-tête vers une clé connue puis obfusqué avec ChaCha20) et peut être utilisé pour une classification supplémentaire. En aucun cas une opération DH d'essai ou autre opération cryptographique asymétrique n'est nécessaire pour classifier un paquet.

- Créer un en-tête de 16 octets
- Créer la charge utile
- Chiffrer la charge utile en utilisant ChaChaPoly avec l'en-tête comme AD
- Chiffrer l'en-tête

### Notes

#### Résumé

Pour presque tous les messages de tous les pairs, la clé ChaCha20 pour le chiffrement de l'ID de connexion est la clé d'introduction du routeur de destination telle que publiée dans la netDb.

- Décrypter les 8 premiers octets de l'en-tête (l'ID de connexion de destination) avec la clé d'introduction
- Rechercher la connexion par l'ID de connexion de destination
- Si la connexion est trouvée et est dans la phase de données, aller à la section phase de données
- Si la connexion n'est pas trouvée, aller à la section handshake
- Note : Les messages Peer Test et Hole Punch peuvent également être recherchés par l'ID de connexion de destination créé à partir du nonce de test ou de relais.

Les seules exceptions sont les premiers messages envoyés de Bob vers Alice (Session Created ou Retry) où la clé d'introduction d'Alice n'est pas encore connue de Bob. Dans ces cas, la clé d'introduction de Bob est utilisée comme clé.

- Déchiffrer les octets 8-15 de l'en-tête (le type de paquet, la version et l'ID réseau) avec la clé d'introduction. Si c'est une Session Request, Token Request, Peer Test ou Hole Punch valide, continuer
- Si ce n'est pas un message valide, rechercher une connexion sortante en attente par l'IP/port source du paquet, traiter le paquet comme une Session Created ou Retry. Re-déchiffrer les 8 premiers octets de l'en-tête avec la bonne clé, et les octets 8-15 de l'en-tête (le type de paquet, la version et l'ID réseau). Si c'est une Session Created ou Retry valide, continuer
- Si ce n'est pas un message valide, échouer, ou mettre en file d'attente comme un possible paquet de phase de données hors séquence
- Pour Session Request/Created, Retry, Token Request, Peer Test et Hole Punch, déchiffrer les octets 16-31 de l'en-tête
- Pour Session Request/Created, déchiffrer la clé éphémère
- Valider tous les champs de l'en-tête, arrêter si non valide
- mixHash() l'en-tête
- Pour Session Request/Created/Confirmed, déchiffrer la charge utile en utilisant Noise
- Pour Retry et la phase de données, déchiffrer la charge utile en utilisant ChaChaPoly
- Traiter l'en-tête et la charge utile

Le protocole est conçu pour minimiser le traitement de classification des paquets qui pourrait nécessiter des opérations cryptographiques supplémentaires en plusieurs étapes de repli ou des heuristiques complexes. De plus, la grande majorité des paquets reçus ne nécessitera pas une recherche de repli (potentiellement coûteuse) par IP/port source et un second déchiffrement d'en-tête. Seuls Session Created et Retry (et possiblement d'autres à déterminer) nécessiteront le traitement de repli. Si un point de terminaison change d'IP ou de port après la création de session, l'ID de connexion est toujours utilisé pour rechercher la session. Il n'est jamais nécessaire d'utiliser des heuristiques pour trouver la session, par exemple en cherchant une session différente avec la même IP mais un port différent.

- Déchiffrer les octets 8-15 de l'en-tête (le type de paquet, la version et l'ID réseau) avec la clé correcte
- Déchiffrer la charge utile en utilisant ChaChaPoly avec l'en-tête comme AD
- Traiter l'en-tête et la charge utile

#### Détails

Par conséquent, les étapes de traitement recommandées dans la logique de la boucle du récepteur sont :

1)  Déchiffrer les 8 premiers octets avec ChaCha20 en utilisant la clé d'introduction locale, pour récupérer l'ID de connexion de destination. Si l'ID de connexion correspond à une session entrante actuelle ou en attente :

2) Si l'ID de connexion ne correspond à aucune session actuelle : Vérifier que l'en-tête en texte clair aux octets 8-15 est valide (sans effectuer d'opération de protection d'en-tête). Vérifier que l'ID réseau et la version du protocole sont valides, et que le type de message est Session Request, ou un autre type de message autorisé hors session (TBD).

3)  Rechercher une session sortante en attente par l'IP/port source du paquet.

4)  Si SSU 1 fonctionne sur le même port, tentez de traiter le message comme un paquet SSU 1.

En général, une session (dans la phase de négociation ou de données) ne devrait jamais être détruite après avoir reçu un paquet avec un type de message inattendu. Cela empêche les attaques par injection de paquets. Ces paquets seront aussi couramment reçus après la retransmission d'un paquet de négociation, lorsque les clés de déchiffrement d'en-tête ne sont plus valides.

Dans la plupart des cas, il suffit de supprimer le paquet. Une implémentation peut, mais n'est pas tenue de, retransmettre le paquet précédemment envoyé (message de handshake ou ACK 0) en réponse.

    a)  Using the appropriate key, decrypt the header bytes 8-15 to recover the version, net ID, and message type.
    b)  If the message type is Session Confirmed, it is a long header. Verify the net ID and protocol version are valid. Decrypt the bytes 15-31 of the header with ChaCha20 using the local intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise.
    c)  If the message type is valid but not Session Confirmed, it is a short header. Verify the net ID and protocol version are valid. decrypt the rest of the message with ChaCha20/Poly1305 using the session key, using the decrypted 16-byte header as the AD.
    d)  (optional) If connection ID is a pending inbound session awaiting a Session Confirmed message, but the net ID, protocol, or message type is not valid, it could be a Data message received out-of-order before the Session Confirmed, so the data phase header protection keys are not yet known, and the header bytes 8-15 were incorrectly decrypted. Queue the message, and attempt to decrypt it once the Session Confirmed message is received.
    e)  If b) or c) fails, drop the message.

Après avoir envoyé Session Created en tant que Bob, les paquets inattendus sont généralement des paquets Data qui ne peuvent pas être déchiffrés parce que les paquets Session Confirmed ont été perdus ou reçus dans le désordre. Mettre les paquets en file d'attente et tenter de les déchiffrer après avoir reçu les paquets Session Confirmed.

    a)  If all is valid and the message type is Session Request, decrypt bytes 16-31 of the header and the 32-byte X value with ChaCha20 using the local intro key.

    - If the token at header bytes 24-31 is accepted, then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Created in response.
    - If the token is not accepted, send a Retry message to the source IP/port with a token. Do not attempt to decrypt the message with Noise to avoid DDoS attacks.

    b)  If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.
    c)  If a) or b) fails, go to step 3)

Après avoir reçu Session Confirmed en tant que Bob, les paquets inattendus sont généralement des paquets Session Confirmed retransmis, car l'ACK 0 du Session Confirmed a été perdu. Les paquets inattendus peuvent être supprimés. Une implémentation peut, mais n'est pas tenue de, envoyer un paquet Data contenant un bloc ACK en réponse.

    a)  If found, re-decrypt the first 8 bytes with ChaCha20 using Bob's introduction key to recover the Destination Connection ID.
    b)  If the connection ID matches the pending session: Using the correct key, decrypt bytes 8-15 of the header to recover the version, net ID, and message type. Verify the net ID and protocol version are valid, and the message type is Session Created or Retry, or other message type allowed out-of-session (TBD).

    - If all is valid and the message type is Session Created, decrypt the next 16 bytes of the header and the 32-byte Y value with ChaCha20 using Bob's intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Confirmed in response.
    - If all is valid and the message type is Retry, decrypt bytes 16-31 of the header with ChaCha20 using Bob's intro key. Decrypt and validate the message using ChaCha20/Poly1305 using TBD as the key and TBD as the nonce and the decrypted 32-byte header as the AD. Resend a Session Request with the received token in response.
    - If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.

    > c)  If a pending outbound session is not found, or the connection ID does not match the pending session, drop the message, unless the port is shared with SSU 1.

Pour Session Created et Session Confirmed, les implémentations doivent soigneusement valider tous les champs d'en-tête déchiffrés (ID de connexion, numéro de paquet, type de paquet, version, id, frag et flags) AVANT d'appeler mixHash() sur l'en-tête et de tenter de déchiffrer la charge utile avec Noise AEAD. Si le déchiffrement Noise AEAD échoue, aucun traitement supplémentaire ne peut être effectué, car mixHash() aura corrompu l'état de la négociation, à moins qu'une implémentation ne stocke et "annule" l'état de hachage.

#### Gestion des erreurs

Il peut ne pas être possible de détecter efficacement si les paquets entrants sont de version 1 ou 2 sur le même port d'entrée. Les étapes ci-dessus peuvent être utiles à effectuer avant le traitement SSU 1, afin d'éviter de tenter des opérations DH d'essai en utilisant les deux versions de protocole.

À déterminer si nécessaire.

Suppose IPv4, sans inclure le rembourrage supplémentaire, sans inclure les tailles d'en-tête IP et UDP. Le rembourrage est un rembourrage mod-16 pour SSU 1 uniquement.

**SSU 1**

### Détection de version

**SSU 2**

### Jetons

Nous spécifions ci-dessus que le token doit être une valeur de 8 octets générée aléatoirement, et non générer une valeur opaque telle qu'un hash ou HMAC d'un secret serveur et de l'IP, port, en raison d'attaques de réutilisation. Cependant, cela nécessite un stockage temporaire et (optionnellement) persistant des tokens livrés. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) utilise un HMAC de 16 octets d'un secret serveur et d'une adresse IP, et le secret serveur effectue une rotation toutes les deux minutes. Nous devrions étudier quelque chose de similaire, avec une durée de vie du secret serveur plus longue. Si nous intégrons un horodatage dans le token, cela pourrait être une solution, mais un token de 8 octets pourrait ne pas être suffisamment grand pour cela.

À déterminer si nécessaire.

## Constantes recommandées

- Délai de retransmission du handshake sortant : 1,25 seconde, avec backoff exponentiel (retransmissions à 1,25, 3,75 et 8,75 secondes)
- Délai total du handshake sortant : 15 secondes
- Délai de retransmission du handshake entrant : 1 seconde, avec backoff exponentiel (retransmissions à 1, 3 et 7 secondes)
- Délai total du handshake entrant : 12 secondes
- Délai après envoi de retry : 9 secondes
- Délai ACK : max(10, min(rtt/6, 150)) ms
- Délai ACK immédiat : min(rtt/16, 5) ms
- Plages ACK max : 256 ?
- Profondeur ACK max : 512 ?
- Distribution du padding : 0-15 octets, ou plus
- Délai minimum de retransmission en phase de données : 1 seconde, comme dans [RFC-6298](https://tools.ietf.org/html/rfc6298)
- Voir aussi [RFC-6298](https://tools.ietf.org/html/rfc6298) pour des conseils supplémentaires sur les timers de retransmission pour la phase de données.

## Analyse de la surcharge des paquets

Suppose l'utilisation d'IPv4, sans inclure de remplissage supplémentaire, ni les tailles des en-têtes IP et UDP. Le remplissage est un remplissage modulo 16, uniquement pour SSU 1.

**SSU 1**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MAC</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">40</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">304</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. extended options</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">79</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">336</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 64 byte Ed25519 sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">462</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">512</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 391 byte ident and 64 byte sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (RI)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1014</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1051</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header, 1000 byte RI</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">51</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">2254</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>
**SSU 2**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MACs</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">87</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">96</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime, Address blocks</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1005</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1085</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1000 byte compressed RI block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">46</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1314</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>    
## Problèmes et Travaux Futurs

### Jetons

Nous précisons ci-dessus que le jeton doit être une valeur aléatoire de 8 octets, et non une valeur opaque telle qu'un hachage ou un HMAC basé sur un secret serveur et l'IP, le port, en raison des attaques par réutilisation. Toutefois, cela nécessite un stockage temporaire et (éventuellement) persistant des jetons délivrés. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) utilise un HMAC de 16 octets combinant un secret serveur et l'adresse IP, le secret serveur étant renouvelé toutes les deux minutes. Nous devrions étudier une approche similaire, avec une durée de vie plus longue pour le secret serveur. Si nous intégrons un horodatage dans le jeton, cela pourrait constituer une solution, mais un jeton de 8 octets pourrait ne pas être suffisamment grand pour cela.

## Références

- **[Common]** [Spécification des Structures Communes](/docs/specs/common-structures)
- **[ECIES]** [Spécification ECIES-X25519-AEAD-Ratchet](/docs/specs/ecies)
- **[NetDB]** [Base de Données Réseau](/docs/overview/network-database)
- **[NOISE]** [Cadre de Protocole Noise](https://noiseprotocol.org/noise.html)
- **[Nonces]** [Adversaires ne Respectant pas les Nonces](https://eprint.iacr.org/2019/624.pdf)
- **[NTCP]** [Transport NTCP](/docs/transport/ntcp)
- **[NTCP2]** [Spécification NTCP2](/docs/specs/ntcp2)
- **[PMTU]** [Découverte du MTU de Chemin](https://en.wikipedia.org/wiki/Path_MTU_Discovery)
- **[Prop104]** [Proposition 104 : Transport TLS](/proposals/104-tls-transport)
- **[Prop109]** [Proposition 109 : Transport Modulaire](/proposals/109-pt-transport)
- **[Prop158]** [Proposition 158 : Améliorations du Transport IPv6](/proposals/158-ipv6-transport-enhancements)
- **[Prop159]** [Proposition 159 : SSU2](/proposals/159-ssu2)
- **[RFC-2104]** [RFC 2104 : HMAC](https://tools.ietf.org/html/rfc2104)
- **[RFC-3449]** [RFC 3449 : Implications de Performance TCP](https://tools.ietf.org/html/rfc3449)
- **[RFC-3526]** [RFC 3526 : Groupes MODP](https://tools.ietf.org/html/rfc3526)
- **[RFC-5681]** [RFC 5681 : Contrôle de Congestion TCP](https://tools.ietf.org/html/rfc5681)
- **[RFC-5869]** [RFC 5869 : HKDF](https://tools.ietf.org/html/rfc5869)
- **[RFC-6151]** [RFC 6151 : Considérations de Sécurité MD5](https://tools.ietf.org/html/rfc6151)
- **[RFC-6298]** [RFC 6298 : Minuteur de Retransmission TCP](https://tools.ietf.org/html/rfc6298)
- **[RFC-6437]** [RFC 6437 : Étiquette de Flux IPv6](https://tools.ietf.org/html/rfc6437)
- **[RFC-7539]** [RFC 7539 : ChaCha20/Poly1305](https://tools.ietf.org/html/rfc7539)
- **[RFC-7748]** [RFC 7748 : Courbes Elliptiques pour la Sécurité](https://tools.ietf.org/html/rfc7748)
- **[RFC-7905]** [RFC 7905 : Suites de Chiffrement ChaCha20-Poly1305 pour TLS](https://tools.ietf.org/html/rfc7905)
- **[RFC-9000]** [RFC 9000 : Protocole de Transport QUIC](https://datatracker.ietf.org/doc/html/rfc9000)
- **[RFC-9001]** [RFC 9001 : Utilisation de TLS pour Sécuriser QUIC](https://datatracker.ietf.org/doc/html/rfc9001)
- **[RFC-9002]** [RFC 9002 : Détection de Perte et Contrôle de Congestion QUIC](https://datatracker.ietf.org/doc/html/rfc9002)
- **[RouterAddress]** [Structure RouterAddress](/docs/specs/common-structures#struct-routeraddress)
- **[RouterIdentity]** [Structure RouterIdentity](/docs/specs/common-structures#struct-routeridentity)
- **[SigningPublicKey]** [Type SigningPublicKey](/docs/specs/common-structures#type-signingpublickey)
- **[SSU]** [Transport SSU](/docs/transport/ssu)
- **[STS]** [Protocole Station-à-Station](https://en.wikipedia.org/wiki/Station-to-Station_protocol)
- **[Ticket1112]** [Ticket I2P 1112](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1112)
- **[Ticket1849]** [Ticket I2P 1849](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1849)
- **[WireGuard]** [Protocole WireGuard](https://www.wireguard.com/papers/wireguard.pdf)
