---
title: "Spécification du LeaseSet chiffré"
description: "Masquage, chiffrement et déchiffrement des leaseSets chiffrés"
slug: "encryptedleaseset"
category: "Protocoles"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Aperçu

Ce document spécifie l'aveuglement, le chiffrement et le déchiffrement des leasesets chiffrés. Pour la structure du leaseset chiffré, voir la [spécification des structures communes](/docs/specs/common-structures). Pour le contexte sur les leasesets chiffrés, voir la [proposition 123](/proposals/123-new-netdb-entries). Pour l'utilisation dans la netDb, voir la documentation netDb.

### Définitions

Nous définissons les fonctions suivantes correspondant aux blocs de construction cryptographiques utilisés pour les LS2 chiffrés :

**CSRNG(n)** : sortie de n octets d'un générateur de nombres aléatoires cryptographiquement sûr.

En plus de l'exigence que le CSRNG soit cryptographiquement sûr (et donc adapté pour générer du matériel de clé), il DOIT être sûr qu'une sortie de n octets soit utilisée pour du matériel de clé lorsque les séquences d'octets qui la précèdent et la suivent immédiatement sont exposées sur le réseau (comme dans un sel, ou un rembourrage chiffré). Les implémentations qui s'appuient sur une source potentiellement non fiable devraient hacher toute sortie qui doit être exposée sur le réseau [PRNG-REFS](http://projectbullrun.org/dual-ec/ext-rand.html).

**H(p, d)** : Fonction de hachage SHA-256 qui prend une chaîne de personnalisation p et des données d, et produit une sortie de longueur 32 octets.

Utilisez SHA-256 comme suit :

```
H(p, d) := SHA-256(p || d)
```
**STREAM** : Le chiffrement de flux ChaCha20 tel que spécifié dans [RFC-7539-S2.4](https://tools.ietf.org/html/rfc7539#section-2.4), avec le compteur initial défini à 1. S_KEY_LEN = 32 et S_IV_LEN = 12.

- **ENCRYPT(k, iv, plaintext)** : Chiffre le texte en clair en utilisant la clé de chiffrement k, et le nonce iv qui DOIT être unique pour la clé k. Retourne un texte chiffré de la même taille que le texte en clair. L'intégralité du texte chiffré doit être indiscernable de données aléatoires si la clé est secrète.

- **DECRYPT(k, iv, ciphertext)** : Déchiffre le texte chiffré en utilisant la clé de chiffrement k et le nonce iv. Retourne le texte en clair.

**SIG** : Le schéma de signature Red25519 (correspondant au SigType 11) avec masquage de clé. Il possède les fonctions suivantes :

- **DERIVE_PUBLIC(privkey)** : Retourne la clé publique correspondant à la clé privée donnée.

- **SIGN(privkey, m)** : Retourne une signature par la clé privée privkey sur le message donné m.

- **VERIFY(pubkey, m, sig)** : Vérifie la signature sig contre la clé publique pubkey et le message m. Retourne true si la signature est valide, false sinon.

Il doit également prendre en charge les opérations de masquage de clé suivantes :

- **GENERATE_ALPHA(data, secret)** : Générer alpha pour ceux qui connaissent les données et un secret optionnel. Le résultat doit être distribué de manière identique aux clés privées.

- **BLIND_PRIVKEY(privkey, alpha)** : Aveugle une clé privée, en utilisant un alpha secret.

- **BLIND_PUBKEY(pubkey, alpha)** : Aveugle une clé publique, en utilisant un alpha secret. Pour une paire de clés donnée (privkey, pubkey) la relation suivante s'applique :

```
BLIND_PUBKEY(pubkey, alpha) ==
DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))
```
**DH** : Système d'accord de clés publiques X25519. Clés privées de 32 octets, clés publiques de 32 octets, produit des sorties de 32 octets. Il possède les fonctions suivantes :

- **GENERATE_PRIVATE()** : Génère une nouvelle clé privée.

- **DERIVE_PUBLIC(privkey)** : Retourne la clé publique correspondant à la clé privée donnée.

- **DH(privkey, pubkey)** : Génère un secret partagé à partir des clés privée et publique données.

**HKDF(salt, ikm, info, n)** : Une fonction de dérivation de clé cryptographique qui prend un matériel de clé d'entrée ikm (qui devrait avoir une bonne entropie mais n'est pas requis d'être une chaîne uniformément aléatoire), un salt de longueur 32 octets, et une valeur 'info' spécifique au contexte, et produit une sortie de n octets appropriée pour être utilisée comme matériel de clé.

Utiliser HKDF tel que spécifié dans [RFC-5869](https://tools.ietf.org/html/rfc5869), en utilisant la fonction de hachage HMAC SHA-256 tel que spécifié dans [RFC-2104](https://tools.ietf.org/html/rfc2104). Cela signifie que SALT_LEN est de 32 octets maximum.

### Format

Le format LS2 chiffré se compose de trois couches imbriquées :

- Une couche externe contenant les informations en texte brut nécessaires pour le stockage et la récupération.
- Une couche intermédiaire qui gère l'authentification client.
- Une couche interne qui contient les données LS2 réelles.

Le format global ressemble à :

```
Layer 0 data + Enc(layer 1 data + Enc(layer 2 data)) + Signature
```
Notez que les LS2 chiffrés sont aveugles. La Destination n'est pas dans l'en-tête. L'emplacement de stockage DHT est SHA-256(type de sig || clé publique aveugle), et fait l'objet d'une rotation quotidienne.

N'utilise PAS l'en-tête LS2 standard spécifié ci-dessus.

#### Couche 0 (externe)

**Type** : 1 octet

Pas réellement dans l'en-tête, mais fait partie des données couvertes par la signature. Extraire du champ dans le Database Store Message.

**Type de signature de clé publique aveugle** : 2 octets, big endian

Ce sera toujours le type 11, identifiant une clé aveugle Red25519.

**Clé publique aveuglée** : Longueur selon le type de signature

**Horodatage de publication** : 4 octets, gros boutien

Secondes depuis l'époque, déborde en 2106

**Expires** : 2 octets, big endian

Décalage par rapport au timestamp publié en secondes, 18,2 heures maximum

**Flags** : 2 octets

Ordre des bits : 15 14 ... 3 2 1 0

- Bit 0 : Si 0, pas de clés hors ligne ; si 1, clés hors ligne
- Autres bits : définis à 0 pour la compatibilité avec les utilisations futures

**Données de clé transitoire** : Présent si le flag indique des clés hors ligne

- **Horodatage d'expiration** : 4 octets, big endian. Secondes depuis l'époque, reboucle en 2106
- **Type de signature transitoire** : 2 octets, big endian
- **Clé publique de signature transitoire** : Longueur comme impliquée par le type de signature
- **Signature** : Longueur comme impliquée par le type de signature de la clé publique aveuglée. Sur l'horodatage d'expiration, le type de signature transitoire, et la clé publique transitoire. Vérifiée avec la clé publique aveuglée.

**lenOuterCiphertext** : 2 octets, big endian

**outerCiphertext** : lenOuterCiphertext octets

Données de couche 1 chiffrées. Voir ci-dessous pour la dérivation de clé et les algorithmes de chiffrement.

**Signature** : Longueur telle qu'impliquée par le type de signature de la clé de signature utilisée

La signature porte sur tout ce qui précède. Si le drapeau indique des clés hors ligne, la signature est vérifiée avec la clé publique transitoire. Sinon, la signature est vérifiée avec la clé publique masquée.

#### Couche 1 (intermédiaire)

**Flags** : 1 octet

Ordre des bits : 76543210

- Bit 0 : 0 pour tout le monde, 1 pour par client, section d'authentification à suivre
- Bits 3-1 : Schéma d'authentification, seulement si le bit 0 est défini à 1 pour par client, sinon 000
  - 000 : Authentification client DH (ou pas d'authentification par client)
  - 001 : Authentification client PSK
- Bits 7-4 : Inutilisés, définir à 0 pour la compatibilité future

**Données d'authentification client DH** : Présentes si le bit de drapeau 0 est défini à 1 et les bits de drapeau 3-1 sont définis à 000.

- **ephemeralPublicKey** : 32 octets
- **clients** : 2 octets, big endian. Nombre d'entrées authClient à suivre, 40 octets chacune
- **authClient** : Données d'autorisation pour un client unique. Voir ci-dessous pour l'algorithme d'autorisation par client.
  - **clientID_i** : 8 octets
  - **clientCookie_i** : 32 octets

**Données d'authentification client PSK** : Présentes si le bit de flag 0 est défini à 1 et les bits de flag 3-1 sont définis à 001.

- **authSalt** : 32 octets
- **clients** : 2 octets, big endian. Nombre d'entrées authClient qui suivent, 40 octets chacune
- **authClient** : Données d'autorisation pour un client unique. Voir ci-dessous pour l'algorithme d'autorisation par client.
  - **clientID_i** : 8 octets
  - **clientCookie_i** : 32 octets

**innerCiphertext** : Longueur impliquée par lenOuterCiphertext (toutes les données restantes)

Données de couche 2 chiffrées. Voir ci-dessous pour la dérivation de clés et les algorithmes de chiffrement.

#### Couche 2 (interne)

**Type** : 1 octet

Soit 3 (LS2) ou 7 (Meta LS2)

**Données** : Données LeaseSet2 pour le type donné.

Inclut l'en-tête et la signature.

### Dérivation de Clé d'Aveuglement

Nous utilisons le schéma suivant pour l'aveuglement de clés, basé sur Ed25519 et ZCash RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf). Les signatures Red25519 sont sur la courbe Ed25519, utilisant SHA-512 pour le hachage.

Nous n'utilisons pas l'annexe A.2 du rend-spec-v3.txt de Tor [TOR-REND-SPEC-V3](https://spec.torproject.org/rend-spec-v3), qui a des objectifs de conception similaires, car ses clés publiques aveugles peuvent être en dehors du sous-groupe d'ordre premier, avec des implications de sécurité inconnues.

#### Objectifs

- La clé publique de signature dans la destination non aveuglée doit être Ed25519 (type de signature 7) ou Red25519 (type de signature 11) ; aucun autre type de signature n'est pris en charge
- Si la clé publique de signature est hors ligne, la clé publique de signature transitoire doit également être Ed25519
- L'aveuglement est computationnellement simple
- Utilise des primitives cryptographiques existantes
- Les clés publiques aveuglées ne peuvent pas être désaveuglées
- Les clés publiques aveuglées doivent être sur la courbe Ed25519 et le sous-groupe d'ordre premier
- Doit connaître la clé publique de signature de la destination (destination complète non requise) pour dériver la clé publique aveuglée
- Fournit optionnellement un secret supplémentaire requis pour dériver la clé publique aveuglée

#### Sécurité

La sécurité d'un schéma de masquage exige que la distribution d'alpha soit identique à celle des clés privées non masquées. Cependant, lorsque nous masquons une clé privée Ed25519 (type de signature 7) vers une clé privée Red25519 (type de signature 11), la distribution est différente. Pour répondre aux exigences de la section 4.1.6.1 de zcash [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf), Red25519 (type de signature 11) devrait également être utilisé pour les clés non masquées, afin que "la combinaison d'une clé publique re-randomisée et de signature(s) sous cette clé ne révèlent pas la clé à partir de laquelle elle a été re-randomisée." Nous autorisons le type 7 pour les destinations existantes, mais recommandons le type 11 pour les nouvelles destinations qui seront chiffrées.

#### Définitions

**B** : Le point de base Ed25519 (générateur) 2^255 - 19 comme dans [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)

**L** : L'ordre Ed25519 2^252 + 27742317777372353535851937790883648493 comme dans [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)

**DERIVE_PUBLIC(a)** : Convertir une clé privée en publique, comme dans Ed25519 (multiplier par G)

**alpha** : Un nombre aléatoire de 32 octets connu de ceux qui connaissent la destination.

**GENERATE_ALPHA(destination, date, secret)** : Génère alpha pour la date actuelle, pour ceux qui connaissent la destination et le secret. Le résultat doit être distribué de manière identique aux clés privées Ed25519.

**a** : La clé privée de signature EdDSA ou RedDSA non aveuglée de 32 octets utilisée pour signer la destination

**A** : La clé publique de signature EdDSA ou RedDSA de 32 octets non aveuglée dans la destination, = DERIVE_PUBLIC(a), comme dans Ed25519

**a'** : La clé privée de signature EdDSA aveuglée de 32 octets utilisée pour signer le leaseset chiffré. Il s'agit d'une clé privée EdDSA valide.

**A'** : La clé publique de signature EdDSA aveuglée de 32 octets dans la Destination, peut être générée avec DERIVE_PUBLIC(a'), ou à partir de A et alpha. Il s'agit d'une clé publique EdDSA valide, sur la courbe et sur le sous-groupe d'ordre premier.

**LEOS2IP(x)** : Inverser l'ordre des octets d'entrée vers little-endian

**H\*(x)** : 32 octets = (LEOS2IP(SHA512(x))) mod B, identique au hash-and-reduce d'Ed25519

#### Calculs d'aveuglement

Une nouvelle clé secrète alpha et une nouvelle clé aveuglée doivent être générées chaque jour (UTC).

Le secret alpha et les clés aveuglées sont calculés comme suit :

GENERATE_ALPHA(destination, date, secret), pour toutes les parties :

```
// secret is optional, else zero-length
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of blinded public key A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
datestring = 8 bytes ASCII YYYYMMDD from the current date UTC
secret = UTF-8 encoded string
seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || secret, "i2pblinding1", 64)
// treat seed as a 64 byte little-endian value
alpha = seed mod L
```
BLIND_PRIVKEY(), pour le propriétaire publiant le leaseSet :

```
alpha = GENERATE_ALPHA(destination, date, secret)
// If for a Ed25519 private key (type 7)
seed = destination's signing private key
a = left half of SHA512(seed) and clamped as usual for Ed25519
// else for a Red25519 private key (type 11)
a = destination's signing private key
// Addition using scalar arithmetic
blinded signing private key = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
blinded signing public key = A' = DERIVE_PUBLIC(a')
```
BLIND_PUBKEY(), pour les clients récupérant le leaseSet :

```
alpha = GENERATE_ALPHA(destination, date, secret)
A = destination's signing public key
// Addition using group elements (points on the curve)
blinded public key = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```
Les deux méthodes de calcul de A' donnent le même résultat, comme requis.

#### Signature

Le leaseSet non aveuglé est signé par la clé privée de signature Ed25519 ou Red25519 non aveuglée et vérifié avec la clé publique de signature Ed25519 ou Red25519 non aveuglée (types de signature 7 ou 11) comme d'habitude.

Si la clé publique de signature est hors ligne, le leaseSet non masqué est signé par la clé privée de signature transitoire Ed25519 ou Red25519 non masquée et vérifié avec la clé publique de signature transitoire Ed25519 ou Red25519 non masquée (types de signature 7 ou 11) comme d'habitude. Voir ci-dessous pour des notes supplémentaires sur les clés hors ligne pour les leasesets chiffrés.

Pour la signature du leaseSet chiffré, nous utilisons Red25519 basé sur RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) pour signer et vérifier avec des clés masquées. Les signatures Red25519 utilisent la courbe Ed25519, avec SHA-512 pour le hachage.

Red25519 est similaire à Ed25519 standard sauf comme spécifié ci-dessous.

#### Calculs de Signature/Vérification

La partie externe du leaseSet chiffré utilise des clés et signatures Red25519.

Red25519 est similaire à Ed25519. Il y a deux différences :

Les clés privées Red25519 sont générées à partir de nombres aléatoires puis doivent être réduites modulo L, où L est défini ci-dessus. Les clés privées Ed25519 sont générées à partir de nombres aléatoires puis "bridées" en utilisant un masquage bit à bit sur les octets 0 et 31. Ceci n'est pas fait pour Red25519. Les fonctions GENERATE_ALPHA() et BLIND_PRIVKEY() définies ci-dessus génèrent des clés privées Red25519 appropriées en utilisant mod L.

Dans Red25519, le calcul de r pour la signature utilise des données aléatoires supplémentaires, et utilise la valeur de la clé publique plutôt que le hachage de la clé privée. En raison des données aléatoires, chaque signature Red25519 est différente, même lors de la signature des mêmes données avec la même clé.

```
Signing:
  T = 80 random bytes
  r = H*(T || publickey || message)
  (rest is the same as in Ed25519)

Verification:
  Same as for Ed25519
```
### Chiffrement et traitement

#### Dérivation de sous-identifiants

Dans le cadre du processus de masquage, nous devons nous assurer qu'un LS2 chiffré ne peut être déchiffré que par quelqu'un qui connaît la clé publique de signature de la Destination correspondante. La Destination complète n'est pas requise. Pour y parvenir, nous dérivons un identifiant à partir de la clé publique de signature :

```
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
credential = H("credential", keydata)
```
La chaîne de personnalisation garantit que l'identifiant n'entre pas en collision avec tout hash utilisé comme clé de recherche DHT, tel que le hash de Destination simple.

Pour une clé aveuglée donnée, nous pouvons alors dériver un sous-identifiant :

```
subcredential = H("subcredential", credential || blindedPublicKey)
```
Le subcredential est inclus dans les processus de dérivation de clés ci-dessous, ce qui lie ces clés à la connaissance de la clé publique de signature de la Destination.

#### Chiffrement de couche 1

D'abord, l'entrée du processus de dérivation de clé est préparée :

```
outerInput = subcredential || publishedTimestamp
```
Ensuite, un sel aléatoire est généré :

```
outerSalt = CSRNG(32)
```
Ensuite, la clé utilisée pour chiffrer la couche 1 est dérivée :

```
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Enfin, le texte en clair de la couche 1 est chiffré et sérialisé :

```
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```
#### Déchiffrement de couche 1

Le salt est analysé à partir du texte chiffré de la couche 1 :

```
outerSalt = outerCiphertext[0:31]
```
Ensuite, la clé utilisée pour chiffrer la couche 1 est dérivée :

```
outerInput = subcredential || publishedTimestamp
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Enfin, le texte chiffré de la couche 1 est déchiffré :

```
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```
#### Chiffrement de couche 2

Lorsque l'autorisation client est activée, `authCookie` est calculé comme décrit ci-dessous. Lorsque l'autorisation client est désactivée, `authCookie` est le tableau d'octets de longueur nulle.

Le chiffrement procède de manière similaire à la couche 1 :

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = CSRNG(32)
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```
#### Déchiffrement de couche 2

Lorsque l'autorisation client est activée, `authCookie` est calculé comme décrit ci-dessous. Lorsque l'autorisation client est désactivée, `authCookie` est le tableau d'octets de longueur zéro.

Le déchiffrement procède de manière similaire à la couche 1 :

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = innerCiphertext[0:31]
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```
### Autorisation par client

Lorsque l'autorisation client est activée pour une Destination, le serveur maintient une liste des clients qu'il autorise à déchiffrer les données LS2 chiffrées. Les données stockées par client dépendent du mécanisme d'autorisation et incluent une forme de matériel cryptographique que chaque client génère et envoie au serveur via un mécanisme sécurisé hors bande.

Il existe deux alternatives pour implémenter l'autorisation par client :

#### Autorisation client DH

Chaque client génère une paire de clés DH `[csk_i, cpk_i]`, et envoie la clé publique `cpk_i` au serveur.

##### Traitement serveur

Le serveur génère un nouveau `authCookie` et une paire de clés DH éphémère :

```
authCookie = CSRNG(32)
esk = GENERATE_PRIVATE()
epk = DERIVE_PUBLIC(esk)
```
Ensuite, pour chaque client autorisé, le serveur chiffre `authCookie` avec sa clé publique :

```
sharedSecret = DH(esk, cpk_i)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
Le serveur place chaque tuple `[clientID_i, clientCookie_i]` dans la couche 1 du LS2 chiffré, avec `epk`.

##### Traitement client

Le client utilise sa clé privée pour dériver son identifiant client attendu `clientID_i`, sa clé de chiffrement `clientKey_i`, et son IV de chiffrement `clientIV_i` :

```
sharedSecret = DH(csk_i, epk)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Ensuite, le client recherche dans les données d'autorisation de la couche 1 une entrée qui contient `clientID_i`. Si une entrée correspondante existe, le client la déchiffre pour obtenir `authCookie` :

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Autorisation client par clé pré-partagée

Chaque client génère une clé secrète de 32 octets `psk_i`, et l'envoie au serveur. Alternativement, le serveur peut générer la clé secrète, et l'envoyer à un ou plusieurs clients.

##### Traitement serveur

Le serveur génère un nouveau `authCookie` et sel :

```
authCookie = CSRNG(32)
authSalt = CSRNG(32)
```
Ensuite, pour chaque client autorisé, le serveur chiffre `authCookie` avec sa clé pré-partagée :

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
Le serveur place chaque tuple `[clientID_i, clientCookie_i]` dans la couche 1 du LS2 chiffré, avec `authSalt`.

##### Traitement client

Le client utilise sa clé pré-partagée pour dériver son identifiant client attendu `clientID_i`, sa clé de chiffrement `clientKey_i`, et son IV de chiffrement `clientIV_i` :

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Ensuite, le client recherche dans les données d'autorisation de couche 1 une entrée qui contient `clientID_i`. Si une entrée correspondante existe, le client la déchiffre pour obtenir `authCookie` :

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Considérations de sécurité

Les deux mécanismes d'autorisation client ci-dessus offrent la confidentialité pour l'appartenance des clients. Une entité qui ne connaît que la Destination peut voir combien de clients sont abonnés à tout moment, mais ne peut pas suivre quels clients sont ajoutés ou révoqués.

Les serveurs DEVRAIENT randomiser l'ordre des clients chaque fois qu'ils génèrent un LS2 chiffré, pour empêcher les clients d'apprendre leur position dans la liste et de déduire quand d'autres clients ont été ajoutés ou révoqués.

Un serveur PEUT choisir de masquer le nombre de clients abonnés en insérant des entrées aléatoires dans la liste des données d'autorisation.

##### Avantages de l'autorisation client DH

- La sécurité du schéma ne dépend pas uniquement de l'échange hors-bande du matériel de clé client. La clé privée du client n'a jamais besoin de quitter son appareil, et donc un adversaire qui est capable d'intercepter l'échange hors-bande, mais ne peut pas casser l'algorithme DH, ne peut pas déchiffrer le LS2 chiffré, ou déterminer combien de temps le client se voit accorder l'accès.

##### Inconvénients de l'autorisation client DH

- Nécessite N + 1 opérations DH côté serveur pour N clients.
- Nécessite une opération DH côté client.
- Nécessite que le client génère la clé secrète.

##### Avantages de l'autorisation client PSK

- Ne nécessite aucune opération DH.
- Permet au serveur de générer la clé secrète.
- Permet au serveur de partager la même clé avec plusieurs clients, si souhaité.

##### Inconvénients de l'autorisation client PSK

- La sécurité du système dépend de manière critique de l'échange hors-bande du matériel de clé client. Un adversaire qui intercepte l'échange pour un client particulier peut déchiffrer tout LS2 chiffré ultérieur pour lequel ce client est autorisé, ainsi que déterminer quand l'accès du client est révoqué.

### LeaseSet chiffré avec adresses Base 32

Vous ne pouvez pas utiliser une adresse base 32 traditionnelle pour un LS2 chiffré, car elle ne contient que le hash de la destination. Elle ne fournit pas la clé publique non-aveuglée. Par conséquent, une adresse base 32 seule est insuffisante. Le client a besoin soit de la destination complète (qui contient la clé publique), soit de la clé publique elle-même. Si le client a la destination complète dans un carnet d'adresses, et que le carnet d'adresses prend en charge la recherche inverse par hash, alors la clé publique peut être récupérée.

Nous avons donc besoin d'un nouveau format qui place la clé publique au lieu du hachage dans une adresse base32. Ce format doit également contenir le type de signature de la clé publique et le type de signature du schéma d'aveuglage. Les exigences totales sont 32 + 3 = 35 octets, nécessitant 56 caractères en base 32, ou plus pour les types de clés publiques plus longs.

```
data = ((1 byte flags || 1 byte unblinded sigtype || 1 byte blinded sigtype) XOR checksum) || 32 byte pubkey
address = Base32Encode(data) || ".b32.i2p"
```
Nous utilisons le même suffixe ".b32.i2p" que pour les adresses base 32 traditionnelles. Les adresses pour les leasesets chiffrés sont identifiées par les 56 caractères encodés (35 octets décodés), comparé à 52 caractères (32 octets) pour les adresses base 32 traditionnelles. Les cinq bits inutilisés à la fin du b32 doivent être à 0.

Vous ne pouvez pas utiliser un LS2 chiffré pour bittorrent, à cause des réponses d'annonce compactes qui font 32 octets. Les 32 octets ne contiennent que le hash. Il n'y a pas de place pour une indication que le leaseSet est chiffré, ou les types de signature.

Voir la [spécification de nommage](/docs/specs/naming) ou la [proposition 149](/proposals/149-b32-encrypted-ls2) pour plus d'informations sur le nouveau format.

### LeaseSet chiffré avec clés hors ligne

Pour les leaseSets chiffrés avec des clés hors ligne, les clés privées masquées doivent également être générées hors ligne, une pour chaque jour.

Comme le bloc de signature hors ligne optionnel se trouve dans la partie en clair du leaseset chiffré, toute personne analysant les floodfills pourrait l'utiliser pour suivre le leaseset (mais pas le déchiffrer) pendant plusieurs jours. Pour éviter cela, le propriétaire des clés devrait également générer de nouvelles clés temporaires pour chaque jour. Les clés temporaires et masquées peuvent être générées à l'avance et livrées au router par lot.

Aucun format de fichier n'est défini pour regrouper plusieurs clés transitoires et aveugles et les fournir au client ou au router. Aucune amélioration du protocole I2CP n'est définie pour prendre en charge les leaseSets chiffrés avec des clés hors ligne.

### Notes

- Un service utilisant des leasesets chiffrés publierait la version chiffrée vers les floodfills. Cependant, pour des raisons d'efficacité, il enverrait des leasesets non chiffrés aux clients dans le message garlic encapsulé, une fois authentifié (via une liste blanche, par exemple).
- Les floodfills peuvent limiter la taille maximale à une valeur raisonnable pour empêcher les abus.
- Après déchiffrement, plusieurs vérifications doivent être effectuées, notamment que l'horodatage interne et l'expiration correspondent à ceux du niveau supérieur.
- ChaCha20 a été sélectionné plutôt qu'AES. Bien que les vitesses soient similaires si le support matériel AES est disponible, ChaCha20 est 2,5 à 3 fois plus rapide lorsque le support matériel AES n'est pas disponible, comme sur les appareils ARM de gamme inférieure.

## Références

- **[ED25519-REFS]** "Signatures haute vitesse haute sécurité" par Daniel J. Bernstein, Niels Duif, Tanja Lange, Peter Schwabe, et Bo-Yin Yang. [http://cr.yp.to/papers.html#ed25519](http://cr.yp.to/papers.html#ed25519)
- **[KEYBLIND-PROOF]** [https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html](https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html)
- **[KEYBLIND-REFS]** [https://trac.torproject.org/projects/tor/ticket/8106](https://trac.torproject.org/projects/tor/ticket/8106) et [https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html](https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html)
- **[PRNG-REFS]** [http://projectbullrun.org/dual-ec/ext-rand.html](http://projectbullrun.org/dual-ec/ext-rand.html) et [https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html)
- **[RFC-2104]** [https://tools.ietf.org/html/rfc2104](https://tools.ietf.org/html/rfc2104)
- **[RFC-4880-S5.1]** [https://tools.ietf.org/html/rfc4880#section-5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
- **[RFC-5869]** [https://tools.ietf.org/html/rfc5869](https://tools.ietf.org/html/rfc5869)
- **[RFC-7539-S2.4]** [https://tools.ietf.org/html/rfc7539#section-2.4](https://tools.ietf.org/html/rfc7539#section-2.4)
- **[TOR-REND-SPEC-V3]** [https://spec.torproject.org/rend-spec-v3](https://spec.torproject.org/rend-spec-v3)
- **[ZCASH]** [https://github.com/zcash/zips/tree/master/protocol/protocol.pdf](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)
