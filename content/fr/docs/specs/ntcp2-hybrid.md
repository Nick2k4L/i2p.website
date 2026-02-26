---
title: "PQ Hybrid NTCP2"
description: "Variante hybride post-quantique du protocole de transport NTCP2 utilisant ML-KEM"
slug: "ntcp2-hybrid"
lastupdated: "2026-02"
category: "Transports"
accurateFor: "0.9.69"
---

### Statut

Beta T1 2026, sortie T2 2026

## Aperçu

Il s'agit de la variante post-quantique hybride du protocole de transport NTCP2, tel que conçu dans la Proposition 169. Voir cette proposition pour des informations contextuelles supplémentaires.

PQ Hybrid NTCP2 n'est défini que sur la même adresse et le même port que NTCP2 standard. Le fonctionnement sur un port différent, ou sans support NTCP2 standard, n'est pas autorisé, et ne le sera pas pendant plusieurs années, jusqu'à ce que NTCP2 standard soit déprécié.

Cette spécification documente uniquement les modifications requises au NTCP2 standard pour prendre en charge PQ Hybrid. Consultez la spécification NTCP2 pour les détails d'implémentation de base.

## Conception

Nous prenons en charge les standards NIST FIPS 203 et 204 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) qui sont basés sur, mais PAS compatibles avec, CRYSTALS-Kyber et CRYSTALS-Dilithium (versions 3.1, 3 et antérieures).

### Échange de Clés

PQ KEM fournit uniquement des clés éphémères et ne prend pas directement en charge les négociations à clé statique telles que Noise XK et IK. Les types de chiffrement sont les mêmes que ceux utilisés dans PQ Hybrid Ratchet et sont définis dans le document des structures communes [/docs/specs/common-structures/](/docs/specs/common-structures/), comme dans [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf), Les types hybrides ne sont définis qu'en combinaison avec X25519.

Les types de chiffrement sont :

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Type</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Code</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">6</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">7</td>
</tr>
</table>

### Combinaisons légales

Les nouveaux types de chiffrement sont indiqués dans les RouterAddresses. Le type de chiffrement dans le certificat de clé continuera d'être de type 4.

## Spécification

### Modèles de négociation

Les poignées de main utilisent les modèles de poignée de main du [Noise Protocol](https://noiseprotocol.org/noise.html).

Le mappage de lettres suivant est utilisé :

- e = clé éphémère à usage unique
- s = clé statique
- p = charge utile du message
- e1 = clé PQ éphémère à usage unique, envoyée d'Alice à Bob
- ekem1 = le texte chiffré KEM, envoyé de Bob à Alice

Les modifications suivantes à XK et IK pour la confidentialité prospective hybride (hfs) sont spécifiées dans la [spécification Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) section 5 :

```
XK:                       XKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, p               -> e, es, e1, p
  <- e, ee, p               <- e, ee, ekem1, p
  -> s, se                  -> s, se
  <- p                      <- p
  p ->                      p ->


  e1 and ekem1 are encrypted. See pattern definitions below.
  NOTE: e1 and ekem1 are different sizes (unlike X25519)
```
Le motif e1 est défini comme suit, tel que spécifié dans la section 4 de la [spécification Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) :

```
For Alice:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++
  MixHash(ciphertext)

  For Bob:

  // DecryptAndHash(ciphertext)
  encap_key = DECRYPT(k, n, ciphertext, ad)
  n++
  MixHash(ciphertext)
```
Le motif ekem1 est défini comme suit, tel que spécifié dans la section 4 de la [spécification Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) :

```
For Bob:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  MixKey(kem_shared_key)


  For Alice:

  // DecryptAndHash(ciphertext)
  kem_ciphertext = DECRYPT(k, n, ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  MixKey(kem_shared_key)
```
### KDF de handshake Noise

#### Aperçu

L'échange hybride est défini dans la [spécification Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf). Le premier message, d'Alice vers Bob, contient e1, la clé d'encapsulation, avant la charge utile du message. Ceci est traité comme une clé statique supplémentaire ; appelez EncryptAndHash() dessus (en tant qu'Alice) ou DecryptAndHash() (en tant que Bob). Ensuite, traitez la charge utile du message comme d'habitude.

Le deuxième message, de Bob vers Alice, contient ekem1, le texte chiffré, avant la charge utile du message. Ceci est traité comme une clé statique supplémentaire ; appelez EncryptAndHash() dessus (en tant que Bob) ou DecryptAndHash() (en tant qu'Alice). Ensuite, calculez la kem_shared_key et appelez MixKey(kem_shared_key). Puis traitez la charge utile du message comme d'habitude.

#### Opérations ML-KEM définies

Nous définissons les fonctions suivantes correspondant aux blocs de construction cryptographiques utilisés tels que définis dans [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

(encap_key, decap_key) = PQ_KEYGEN()

    Alice creates the encapsulation and decapsulation keys
    The encapsulation key is sent in message 1.
    encap_key and decap_key sizes vary based on ML-KEM variant.

(ciphertext, kem_shared_key) = ENCAPS(encap_key)

    Bob calculates the ciphertext and shared key,
    using the ciphertext received in message 1.
    The ciphertext is sent in message 2.
    ciphertext size varies based on ML-KEM variant.
    The kem_shared_key is always 32 bytes.

kem_shared_key = DECAPS(ciphertext, decap_key)

    Alice calculates the shared key,
    using the ciphertext received in message 2.
    The kem_shared_key is always 32 bytes.

Notez que la encap_key et le texte chiffré sont tous deux chiffrés à l'intérieur de blocs ChaCha/Poly dans les messages 1 et 2 de négociation Noise. Ils seront déchiffrés dans le cadre du processus de négociation.

La kem_shared_key est mélangée dans la clé de chaînage avec MixHash(). Voir ci-dessous pour les détails.

#### Alice KDF pour le Message 1

Après le modèle de message 'es' et avant la charge utile, ajouter :

```
This is the "e1" message pattern:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)


  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### KDF de Bob pour le Message 1

Après le motif de message 'es' et avant la charge utile, ajoutez :

```
This is the "e1" message pattern:

  // DecryptAndHash(encap_key_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  encap_key = DECRYPT(k, n, encap_key_section, ad)
  n++

  // MixHash(encap_key_section)
  h = SHA256(h || encap_key_section)

  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### KDF de Bob pour le Message 2

Pour XK : Après le motif de message 'ee' et avant la charge utile, ajouter :

```
This is the "ekem1" message pattern:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  // MixKey(kem_shared_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### KDF d'Alice pour le Message 2

Après le motif de message 'ee', ajoutez :

```
This is the "ekem1" message pattern:

  // DecryptAndHash(kem_ciphertext_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  kem_ciphertext = DECRYPT(k, n, kem_ciphertext_section, ad)

  // MixHash(kem_ciphertext_section)
  h = SHA256(h || kem_ciphertext_section)

  // MixKey(kem_shared_key)
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### KDF pour le Message 3 (XK uniquement)

inchangé

#### KDF pour split()

inchangé

### Détails de la poignée de main

#### Identifiants Noise

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

Modifications : Le NTCP2 actuel contient uniquement les options dans la section ChaCha. Avec ML-KEM, la section ChaCha contiendra également la clé publique PQ chiffrée.

Afin que les connexions NTCP2 PQ et non-PQ puissent être prises en charge sur la même adresse et le même port de routeur, nous utilisons le bit le plus significatif de la valeur X (clé publique éphémère X25519) pour marquer qu'il s'agit d'une connexion PQ. Ce bit est toujours désactivé pour les connexions non-PQ.

Pour Alice, après que le message soit chiffré par Noise, mais avant l'obfuscation AES de X, définir X[31] |= 0x7f.

Pour Bob, après la dé-obfuscation AES de X, tester X[31] & 0x80. Si le bit est défini, l'effacer avec X[31] &= 0x7f, et déchiffrer via Noise comme une connexion PQ. Si le bit est effacé, déchiffrer via Noise comme une connexion non-PQ comme d'habitude.

Pour PQ NTCP2 annoncé sur une adresse de routeur et un port différents, ceci n'est pas requis.

Pour des informations supplémentaires, voir la section Adresses Publiées ci-dessous.

Contenu brut :

```
  +----+----+----+----+----+----+----+----+
  |        MS bit set to 1 and then       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted X         |
  +             (32 bytes)                +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +      (see table below for length)     +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  ~   n = 0                               ~
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaChaPoly frame (options)          |
  +         32 bytes                      +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  ~         padding (optional)            ~
  |     length defined in options block   |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
Données non chiffrées (étiquette d'authentification Poly1305 non affichée) :

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                   X                   |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM encap_key            |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Note : le champ version dans le bloc d'options du message 1 doit être défini à 2, même pour les connexions PQ.

Tailles :

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Type</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Code Type</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">X len</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 1 len</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 1 Enc len</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 1 Dec len</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">PQ key len</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">opt len</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">4</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">64+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">--</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">880+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">848</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">816</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">800</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">6</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1264+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1232</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1200</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1184</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">7</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1648+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1616</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1584</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1568</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
</table>

Remarque : Les codes de type sont uniquement à usage interne. Les routeurs resteront de type 4, et la prise en charge sera indiquée dans les adresses de routeur.

#### 2) SessionCreated

Contenu brut :

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted Y         |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +   Encrypted and authenticated data    +
  -      (see table below for length)     -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (options)          |
  +   Encrypted and authenticated data    +
  -           32 bytes                    -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
Données non chiffrées (tag d'authentification Poly1305 non affiché) :

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                  Y                    |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Tailles :

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Type</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Code Type</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Longueur Y</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Longueur Msg 2</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Longueur Msg 2 Chiffré</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Longueur Msg 2 Déchiffré</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Longueur PQ CT</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">longueur opt</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">4</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">64+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">--</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">848+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">816</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">784</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">768</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">6</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1136+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1104</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1104</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1088</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">7</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1616+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1584</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1584</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1568</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
</table>

Note : Les codes de type sont uniquement à usage interne. Les routeurs resteront de type 4, et la prise en charge sera indiquée dans les adresses de routeur.

#### 3) SessionConfirmed

Inchangé

#### Fonction de dérivation de clé (KDF) (pour la phase de données)

Inchangé

#### Adresses Publiées

Dans tous les cas, utilisez le nom de transport NTCP2 comme d'habitude.

Utilisez la même adresse/port que non-PQ, non-pare-feu. Une seule variante PQ est prise en charge. Dans l'adresse du router, publiez v=2 (comme d'habitude) et le nouveau paramètre pq=[3|4|5] pour indiquer MLKEM 512/768/1024. Alice définit le MSB de la clé éphémère (key[31] & 0x80) dans la demande de session pour indiquer qu'il s'agit d'une connexion hybride. Voir ci-dessus. Les routers plus anciens ignoreront le paramètre pq et se connecteront en non-pq comme d'habitude.

Une adresse/port différente comme non-PQ, ou PQ uniquement, non-firewall n'est PAS prise en charge. Ceci ne sera pas implémenté tant que NTCP2 non-PQ ne sera pas désactivé, dans plusieurs années. Quand non-PQ sera désactivé, plusieurs variantes PQ pourront être prises en charge, mais seulement une par adresse. Quand ce sera pris en charge, dans l'adresse du router, publier v=[3|4|5] pour indiquer MLKEM 512/768/1024. Alice ne définit pas le MSB de la clé éphémère. Les anciens routers vérifieront le paramètre v et ignoreront cette adresse comme non prise en charge.

Adresses derrière un pare-feu (aucune IP publiée) : Dans l'adresse du router, publier v=2 (comme d'habitude). Il n'est pas nécessaire de publier un paramètre pq.

Alice peut se connecter à un Bob PQ en utilisant la variante PQ que Bob publie, que Alice annonce ou non le support pq dans ses informations de router, ou qu'elle annonce la même variante.

#### Remplissage Maximum

Dans la spécification actuelle, les messages 1 et 2 sont définis pour avoir une quantité "raisonnable" de remplissage, avec une plage de 0-31 octets recommandée, et aucun maximum spécifié.

Jusqu'à l'API 0.9.68 (version 2.11.0), Java I2P implémentait un maximum de 256 octets de remplissage pour les connexions non-PQ, cependant ceci n'était pas documenté précédemment. À partir de l'API 0.9.69 (version 2.12.0), Java I2P implémente le même remplissage maximum pour les connexions non-PQ que pour MLKEM-512. Voir le tableau ci-dessous.

Utilisez la taille de message définie comme le rembourrage maximum, c'est-à-dire que le rembourrage maximum doublera la taille du message pour les connexions PQ, comme suit :

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Bourrage Max du Message</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">non-PQ (jusqu'à 0.9.68)</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">non-PQ (à partir de 0.9.69)</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">MLKEM-512</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">MLKEM-768</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">MLKEM-1024</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">Session Request</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">256</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">880</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">880</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1264</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1648</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">Session Created</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">256</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">848</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">848</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1136</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1616</td>
</tr>
</table>

## Analyse des coûts généraux

### Échange de clés

Augmentation de taille (octets) :

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Type</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Pubkey (Msg 1)</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Cipertext (Msg 2)</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+816</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+784</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+1200</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+1104</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+1584</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+1584</td>
</tr>
</table>

## Analyse de sécurité

Les catégories de sécurité NIST sont résumées dans la [présentation NIST](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) diapositive 10. Critères préliminaires : Notre catégorie de sécurité NIST minimale devrait être 2 pour les protocoles hybrides et 3 pour les protocoles PQ uniquement.

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Catégorie</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Aussi sécurisé que</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">1</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">AES128</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">2</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">SHA256</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">3</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">AES192</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">4</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">SHA384</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">AES256</td>
</tr>
</table>

### Négociations de connexion

Ce sont tous des protocoles hybrides. Les implémentations devraient privilégier MLKEM768 ; MLKEM512 n'est pas suffisamment sécurisé.

Catégories de sécurité NIST [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) :

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Algorithme</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Catégorie de Sécurité</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">3</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
</tr>
</table>

## Notes d'implémentation

### Support de bibliothèque

Les bibliothèques Bouncycastle, BoringSSL et WolfSSL prennent désormais en charge MLKEM et MLDSA. Le support OpenSSL sera disponible dans leur version 3.5 le 8 avril 2025 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

### Identification du Trafic Entrant

Nous définissons le MSB de la clé éphémère (key[31] & 0x80) dans la demande de session pour indiquer qu'il s'agit d'une connexion hybride. Cela nous permet d'exécuter à la fois NTCP standard et NTCP hybride sur le même port. Une seule variante hybride est prise en charge pour les connexions entrantes, et annoncée dans l'adresse du router. Par exemple, pq=3 ou pq=4.

#### Obfuscation

En tant qu'Alice, pour une connexion PQ, avant l'obfuscation, définir X[31] |= 0x80. Cela rend X une clé publique X25519 invalide. Après l'obfuscation, AES-CBC la randomisera. Le MSB de X sera aléatoire après l'obfuscation.

En tant que Bob, testez si (X[31] & 0x80) != 0 après désobfuscation. Si c'est le cas, il s'agit d'une connexion PQ.

La version minimale du router requise pour NTCP2-PQ est à déterminer.

Note : Les codes de type sont uniquement à usage interne. Les routeurs resteront de type 4, et la prise en charge sera indiquée dans les adresses de routeur.

## Compatibilité des Routeurs

### Noms de Transport

Dans tous les cas, utilisez le nom de transport NTCP2 comme d'habitude. Les anciens routeurs ignoreront le paramètre pq et se connecteront avec NTCP2 standard comme d'habitude.

## Références

* [CABFORUM](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/)
* [Choosing-Hash](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3)
* [CLOUDFLARE](https://blog.cloudflare.com/pq-2024/)
* [COMMON](/docs/specs/common-structures/)
* [COMPOSITE-SIGS](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)
* [ECIES](/docs/specs/ecies/)
* [FORUM](http://zzz.i2p/topics/3294)
* [FIPS202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
* [FIPS203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
* [FIPS204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
* [FIPS205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf)
* [MLDSA-OIDS](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/)
* [NIST-PQ](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)
* [NIST-PQ-UPDATE](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf)
* [NIST-PQ-END](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf)
* [NIST-VECTORS](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values)
* [Noise](https://noiseprotocol.org/noise.html)
* [Noise-Hybrid](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf)
* [NSA-PQ](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF)
* [NTCP2](/docs/specs/ntcp2/)
* [OPENSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/)
* [Prop165](/docs/proposals/165/)
* [PQ-WIREGUARD](https://eprint.iacr.org/2020/379.pdf)
* [RFC-2104](https://tools.ietf.org/html/rfc2104)
* [Rosenpass](https://rosenpass.eu/)
* [Rosenpass-Whitepaper](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf)
* [SSH-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/)
* [SSU2](/docs/specs/ssu2/)
* [TLS-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/)
