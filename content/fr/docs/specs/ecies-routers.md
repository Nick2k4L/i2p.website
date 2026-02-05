---
title: "Messages de router ECIES-X25519"
description: "Spécification pour le chiffrement des messages garlic vers les routeurs ECIES utilisant X25519"
slug: "ecies-routers"
category: "Protocoles"
lastUpdated: "2025-03"
accurateFor: "0.9.65"
---

## Note

Pris en charge depuis la version 0.9.49. Déploiement réseau et tests en cours. Sujet à des révisions mineures. Voir [proposition 156](/proposals/156-ecies-routers).

## Aperçu

Ce document spécifie le chiffrement des messages garlic vers les routeurs ECIES, en utilisant les primitives cryptographiques introduites par [ECIES-X25519](/docs/specs/ecies). Il fait partie de la [proposition 156](/proposals/156-ecies-routers) globale pour convertir les routeurs des clés ElGamal vers les clés ECIES-X25519. Cette spécification est implémentée depuis la version 0.9.49.

Pour un aperçu de tous les changements requis pour les routeurs ECIES, voir [proposition 156](/proposals/156-ecies-routers). Pour les messages garlic vers les destinations ECIES-X25519, voir [ECIES-X25519](/docs/specs/ecies).

### Primitives cryptographiques

Les primitives requises pour implémenter cette spécification sont :

- AES-256-CBC comme dans [Cryptography](/docs/specs/cryptography)
- Fonctions STREAM ChaCha20/Poly1305 : ENCRYPT(k, n, plaintext, ad) et DECRYPT(k, n, ciphertext, ad) - comme dans [NTCP2](/docs/specs/ntcp2), [ECIES-X25519](/docs/specs/ecies), et [RFC-7539](https://tools.ietf.org/html/rfc7539)
- Fonctions X25519 DH - comme dans [NTCP2](/docs/specs/ntcp2) et [ECIES-X25519](/docs/specs/ecies)
- HKDF(salt, ikm, info, n) - comme dans [NTCP2](/docs/specs/ntcp2) et [ECIES-X25519](/docs/specs/ecies)

Autres fonctions Noise définies ailleurs :

- MixHash(d) - comme dans [NTCP2](/docs/specs/ntcp2) et [ECIES-X25519](/docs/specs/ecies)
- MixKey(d) - comme dans [NTCP2](/docs/specs/ntcp2) et [ECIES-X25519](/docs/specs/ecies)

## Conception

Le SKM router ECIES n'a pas besoin d'un SKM Ratchet complet tel que spécifié dans [ECIES](/docs/specs/ecies) pour les Destinations. Il n'y a pas d'exigence pour les messages non-anonymes utilisant le modèle IK. Le modèle de menace n'exige pas de clés éphémères encodées en Elligator2.

Par conséquent, le router SKM utilisera le modèle Noise "N", tel que spécifié dans [Prop152](/proposals/152-ecies-tunnels) pour la construction de tunnel. Il utilisera le même format de charge utile que celui spécifié dans [ECIES](/docs/specs/ecies) pour les Destinations. Le mode de clé statique zéro (aucune liaison ou session) d'IK spécifié dans [ECIES](/docs/specs/ecies) ne sera pas utilisé.

Les réponses aux recherches seront chiffrées avec un ratchet tag si demandé dans la recherche. Ceci est documenté dans [Prop154](/proposals/154-ecies-lookups), maintenant spécifié dans [I2NP](/docs/specs/i2np).

La conception permet au router d'avoir un seul gestionnaire de clés de session ECIES. Il n'est pas nécessaire d'exécuter des gestionnaires de clés de session "double clé" comme décrit dans [ECIES](/docs/specs/ecies) pour les destinations. Les routers n'ont qu'une seule clé publique.

Un router ECIES n'a pas de clé statique ElGamal. Le router a encore besoin d'une implémentation d'ElGamal pour construire des tunnels à travers les routers ElGamal et envoyer des messages chiffrés aux routers ElGamal.

Un router ECIES PEUT nécessiter un gestionnaire de clé de session ElGamal partiel pour recevoir les messages étiquetés ElGamal reçus en réponse aux requêtes NetDB provenant de routers floodfill pré-0.9.46, car ces routers n'ont pas d'implémentation des réponses étiquetées ECIES comme spécifié dans [Prop152](/proposals/152-ecies-tunnels). Sinon, un router ECIES ne peut pas demander une réponse chiffrée à un router floodfill pré-0.9.46.

Ceci est optionnel. La décision peut varier selon les différentes implémentations I2P et peut dépendre de la proportion du réseau qui a été mise à niveau vers la version 0.9.46 ou supérieure. À cette date, environ 85% du réseau utilise la version 0.9.46 ou supérieure.

### Protocole Noise Framework

Cette spécification fournit les exigences basées sur le [Noise Protocol Framework](https://noiseprotocol.org/noise.html) (Révision 34, 2018-07-11). Dans la terminologie Noise, Alice est l'initiateur et Bob est le répondeur.

Il est basé sur le protocole Noise Noise_N_25519_ChaChaPoly_SHA256. Ce protocole Noise utilise les primitives suivantes :

- **Modèle de poignée de main unidirectionnelle : N** - Alice ne transmet pas sa clé statique à Bob (N)
- **Fonction DH : X25519** - X25519 DH avec une longueur de clé de 32 octets comme spécifié dans [RFC-7748](https://tools.ietf.org/html/rfc7748).
- **Fonction de chiffrement : ChaChaPoly** - AEAD_CHACHA20_POLY1305 comme spécifié dans [RFC-7539](https://tools.ietf.org/html/rfc7539) section 2.8. Nonce de 12 octets, avec les 4 premiers octets mis à zéro. Identique à celui dans [NTCP2](/docs/specs/ntcp2).
- **Fonction de hachage : SHA256** - Hachage standard de 32 octets, déjà largement utilisé dans I2P.

### Modèles de poignée de main

Les handshakes utilisent les modèles de handshake [Noise](https://noiseprotocol.org/noise.html).

La correspondance de lettres suivante est utilisée :

- e = clé éphémère à usage unique
- s = clé statique
- p = charge utile du message

La demande de construction est identique au modèle Noise N. Ceci est également identique au premier message (Session Request) dans le modèle XK utilisé dans [NTCP2](/docs/specs/ntcp2).

```
<- s
  ...
  e es p ->
```
### Chiffrement des messages

Les messages sont créés et chiffrés asymétriquement vers le router cible. Ce chiffrement asymétrique des messages utilise actuellement ElGamal tel que défini dans [Cryptography](/docs/specs/cryptography) et contient une somme de contrôle SHA-256. Cette conception n'offre pas la confidentialité persistante.

La conception ECIES utilise le motif Noise unidirectionnel "N" avec DH éphémère-statique ECIES-X25519, avec un HKDF, et ChaCha20/Poly1305 AEAD pour la confidentialité persistante, l'intégrité et l'authentification. Alice est l'expéditeur anonyme du message, un router ou une destination. Le router ECIES cible est Bob.

### Chiffrement des réponses

Les réponses ne font pas partie de ce protocole, car Alice est anonyme. Les clés de réponse, le cas échéant, sont regroupées dans le message de demande. Voir la [spécification I2NP](/docs/specs/i2np) pour les messages de recherche dans la base de données.

Les réponses aux messages Database Lookup sont des messages Database Store ou Database Search Reply. Ils sont chiffrés en tant que messages de session existante avec la clé de réponse de 32 octets et le tag de réponse de 8 octets comme spécifié dans [I2NP](/docs/specs/i2np) et [Prop154](/proposals/154-ecies-lookups).

Il n'y a pas de réponses explicites aux messages Database Store. L'expéditeur peut regrouper sa propre réponse sous forme de Garlic Message à lui-même, contenant un message Delivery Status.

## Spécification

X25519 : Voir [ECIES](/docs/specs/ecies).

Identité du router et certificat de clé : Voir [Structures communes](/docs/specs/common-structures).

### Chiffrement des requêtes

Le chiffrement de la requête est le même que celui spécifié dans [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) et [Prop152](/proposals/152-ecies-tunnels), utilisant le modèle Noise "N".

Les réponses aux recherches seront chiffrées avec un ratchet tag si demandé dans la recherche. Les messages de requête Database Lookup contiennent la clé de réponse de 32 octets et le tag de réponse de 8 octets comme spécifié dans [I2NP](/docs/specs/i2np) et [Prop154](/proposals/154-ecies-lookups). La clé et le tag sont utilisés pour chiffrer la réponse.

Les ensembles de tags ne sont pas créés. Le schéma de clé statique zéro spécifié dans ECIES-X25519-AEAD-Ratchet [Prop144](/proposals/144-ecies-x25519-aead-ratchet) et [ECIES](/docs/specs/ecies) ne sera pas utilisé. Les clés éphémères ne seront pas encodées en Elligator2.

En général, il s'agira de messages New Session et ils seront envoyés avec une clé statique zéro (pas de liaison ou de session), car l'expéditeur du message est anonyme.

#### KDF pour ck et h initiaux

Il s'agit du protocole [Noise](https://noiseprotocol.org/noise.html) standard pour le motif "N" avec un nom de protocole standard. C'est identique à ce qui est spécifié dans [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) et [Prop152](/proposals/152-ecies-tunnels) pour les messages de construction de tunnel.

```
This is the "e" message pattern:

  // Define protocol_name.
  Set protocol_name = "Noise_N_25519_ChaChaPoly_SHA256"
  (31 bytes, US-ASCII encoded, no NULL termination).

  // Define Hash h = 32 bytes
  // Pad to 32 bytes. Do NOT hash it, because it is not more than 32 bytes.
  h = protocol_name || 0

  Define ck = 32 byte chaining key. Copy the h data to ck.
  Set chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // up until here, can all be precalculated by all routers.
```
#### KDF pour Message

Les créateurs de messages génèrent une paire de clés X25519 éphémère pour chaque message. Les clés éphémères doivent être uniques par message. Ceci est identique à ce qui est spécifié dans [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) et [Prop152](/proposals/152-ecies-tunnels) pour les messages de construction de tunnel.

```
  // Target router's X25519 static keypair (hesk, hepk) from the Router Identity
  hesk = GENERATE_PRIVATE()
  hepk = DERIVE_PUBLIC(hesk)

  // MixHash(hepk)
  // || below means append
  h = SHA256(h || hepk);

  // up until here, can all be precalculated by each router
  // for all incoming messages

  // Sender generates an X25519 ephemeral keypair
  sesk = GENERATE_PRIVATE()
  sepk = DERIVE_PUBLIC(sesk)

  // MixHash(sepk)
  h = SHA256(h || sepk);

  End of "e" message pattern.

  This is the "es" message pattern:

  // Noise es
  // Sender performs an X25519 DH with receiver's static public key.
  // The target router
  // extracts the sender's ephemeral key preceding the encrypted record.
  sharedSecret = DH(sesk, hepk) = DH(hesk, sepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // ChaChaPoly parameters to encrypt/decrypt
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  // Chain key is not used
  //chainKey = keydata[0:31]

  // AEAD parameters
  k = keydata[32:63]
  n = 0
  plaintext = 464 byte build request record
  ad = h
  ciphertext = ENCRYPT(k, n, plaintext, ad)

  End of "es" message pattern.

  // MixHash(ciphertext) is not required
  //h = SHA256(h || ciphertext)
```
#### Charge utile

La charge utile utilise le même format de bloc que défini dans [ECIES](/docs/specs/ecies) et [Prop144](/proposals/144-ecies-x25519-aead-ratchet). Tous les messages doivent contenir un bloc DateTime pour la prévention des attaques par rejeu.

## Notes d'implémentation

- Les anciens routers ne vérifient pas le type de chiffrement du router et enverront des messages chiffrés ElGamal. Certains routers récents sont bogués et enverront différents types de messages mal formés. Les développeurs devraient détecter et rejeter ces enregistrements avant l'opération DH si possible, pour réduire l'utilisation du CPU.

## Références

- [Structures communes](/docs/specs/common-structures)
- [Cryptographie](/docs/specs/cryptography)
- [ECIES](/docs/specs/ecies)
- [I2NP](/docs/specs/i2np)
- [Framework du protocole Noise](https://noiseprotocol.org/noise.html)
- [NTCP2](/docs/specs/ntcp2)
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet)
- [Prop152](/proposals/152-ecies-tunnels)
- [Prop154](/proposals/154-ecies-lookups)
- [Prop156](/proposals/156-ecies-routers)
- [RFC-7539](https://tools.ietf.org/html/rfc7539)
- [RFC-7748](https://tools.ietf.org/html/rfc7748)
- [Création de tunnel-ECIES](/docs/specs/tunnel-creation-ecies)
