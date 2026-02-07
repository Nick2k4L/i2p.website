---
title: "Spécification des datagrammes"
description: "Spécification des formats de messages datagramme I2P incluant les types bruts, avec réponse et authentifiés"
slug: "datagrams"
category: "Protocoles"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

## Aperçu

Consultez la [documentation de l'API Datagrams](/docs/api/datagrams/) pour un aperçu de l'API Datagrams.

Les types suivants sont définis. Les numéros de protocole standard sont listés, cependant tout autre numéro de protocole peut être utilisé à l'exception du numéro de protocole de streaming (6), spécifique à l'application.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Protocol</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Repliable?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Authenticated?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Replay Prevention?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">As Of</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Raw</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
  </tbody>
</table>
Le support pour Datagram2 et Datagram3 dans les diverses implémentations de router et de bibliothèques est à déterminer. Consultez la documentation de ces implémentations.

### Identification du Type de Datagramme

Les quatre types de datagrammes ne partagent pas d'en-tête commun avec la version du protocole au même endroit. Les paquets ne peuvent pas être identifiés par type selon leur contenu. Lors de l'utilisation de plusieurs types sur la même session, ou d'un seul type avec le streaming, les applications doivent utiliser des numéros de protocole et/ou des ports I2CP/SAM pour router les paquets entrants au bon endroit. L'utilisation de numéros de protocole standard facilitera cette tâche. Laisser le numéro de protocole non défini (0 ou PROTO_ANY), même pour une application utilisant uniquement des datagrammes, n'est pas recommandé car cela augmente le risque d'erreurs de routage et rend plus difficiles les mises à niveau vers une application multi-protocole. Les champs de version dans les Datagrammes 2 et 3 sont fournis uniquement comme vérification supplémentaire pour les erreurs de routage et les changements futurs.

### Conception d'Application

Toutes les utilisations de datagrammes sont spécifiques à l'application.

Comme les datagrammes authentifiés génèrent une surcharge importante, une application typique utilise à la fois des datagrammes authentifiés et non authentifiés. Une conception typique consiste à envoyer un seul datagramme authentifié contenant un jeton du client vers le serveur. Le serveur répond avec un datagramme non authentifié contenant le même jeton. Toute communication ultérieure, avant l'expiration du jeton, utilise des datagrammes bruts.

Les applications envoient et reçoivent des datagrammes en utilisant des numéros de protocole et de port via l'API [I2CP](/docs/specs/i2cp/) ou [SAMv3](/docs/api/samv3/).

Les datagrammes sont, bien sûr, non fiables. Les applications doivent être conçues pour une livraison non fiable. Dans I2P, la livraison est fiable de saut en saut si le saut suivant est accessible, car les transports NTCP2 et SSU2 fournissent la fiabilité. Cependant, la livraison de bout en bout n'est pas fiable, car les messages I2NP peuvent être supprimés dans n'importe quel saut en raison des limites de file d'attente, d'expirations, de délais d'attente, de limites de bande passante ou de sauts suivants inaccessibles.

### Taille du datagramme

La limite de taille nominale pour les messages I2NP, y compris les datagrammes, est de 64 Ko. Les surcharges des messages garlic et tunnel réduisent quelque peu cette limite.

Cependant, tous les messages I2NP doivent être fragmentés en messages de tunnel de 1 Ko. La probabilité de perte d'un message I2NP de n Ko est la fonction exponentielle de la probabilité de perte d'un seul message de tunnel, p ** n. Comme la fragmentation entraîne une rafale de messages de tunnel, la probabilité de perte réelle est beaucoup plus élevée que ce que la fonction exponentielle impliquerait, en raison des limites de file d'attente et de la gestion active des files d'attente (AQM, CoDel ou similaire) dans les implémentations de router.

La taille maximale typique recommandée pour assurer une livraison fiable est de quelques Ko, ou au maximum 10 Ko. Avec une analyse minutieuse des tailles de surcharge à toutes les couches de protocole (sauf transport), les développeurs doivent définir une taille de charge utile maximale qui s'adaptera précisément à un, deux ou trois messages de tunnel. Cela maximisera l'efficacité et la fiabilité. La surcharge aux différentes couches inclut l'en-tête gzip, l'en-tête I2NP, l'en-tête de message garlic, le chiffrement garlic, l'en-tête de message tunnel, les en-têtes de fragmentation de message tunnel, et d'autres. Voir les calculs de MTU de streaming dans [Proposal 144](/proposals/144-ecies-x25519-aead-ratchet/) et ConnectionOptions.java dans le code source Java I2P pour des exemples.

### Considérations SAM

Les applications envoient et reçoivent des datagrammes en utilisant des numéros de protocole et de port via l'API I2CP ou SAM. Spécifier des numéros de protocole et de port via SAM nécessite SAM v3.2 ou supérieur. Utiliser à la fois les datagrammes et le streaming (UDP et TCP) sur la même session SAM (tunnels) nécessite SAM v3.3 ou supérieur. Utiliser plusieurs types de datagrammes sur la même session SAM (tunnels) nécessite SAM v3.3 ou supérieur. SAM v3.3 n'est pris en charge que par le router I2P Java à l'heure actuelle.

Le support SAM pour Datagram2 et Datagram3 dans diverses implémentations de router et de bibliothèque est à déterminer. Consultez la documentation de ces implémentations.

Notez que les tailles supérieures à un MTU réseau typique de 1500 octets empêcheront les applications SAM de transporter des paquets non fragmentés vers/depuis le serveur SAM, si l'application et le serveur sont sur des ordinateurs séparés. Typiquement, ce n'est pas le cas, ils sont tous deux sur localhost, où le MTU est de 65536 ou plus. Si une application SAM est censée être séparée sur un ordinateur différent du serveur, la charge utile maximale pour un datagramme pouvant recevoir une réponse est légèrement inférieure à 1 Ko.

### Considérations PQ

Si la partie MLDSA de la [Proposition 169](/proposals/169-pq-crypto/) Post-Quantum est implémentée, la surcharge augmentera considérablement. La taille d'une destination + signature passera de 391 + 64 = 455 octets à un minimum de 3739 pour MLDSA44 et un maximum de 7226 pour MLDSA87. Les effets pratiques de ceci restent à déterminer. Datagram3, avec l'authentification fournie par le router, pourrait être une solution.

## Datagrammes bruts (non répondables) {#raw}

Les datagrammes non-répondables n'ont pas d'adresse « from » et ne sont pas authentifiés. Ils sont également appelés datagrammes « raw ». À strictement parler, ce ne sont pas des « datagrammes » du tout, ce sont juste des données brutes. Ils ne sont pas gérés par l'API datagram. Cependant, SAM et les classes I2PTunnel prennent en charge les « raw datagrams ».

Le numéro de protocole I2CP standard pour les datagrammes bruts est PROTO_DATAGRAM_RAW (18).

Le format n'est pas spécifié ici, il est défini par l'application. Par souci d'exhaustivité, nous incluons une image du format ci-dessous.

### Format

```
+----+----+----+----+----//
| payload...
+----+----+----+----+----//

length: 0 - about 64 KB (see notes)
```
### Notes

La longueur pratique est limitée à la fois par la surcharge à différentes couches et la fiabilité.

## Datagram1 (Avec réponse possible) {#repliable}

Les datagrammes répondables contiennent une adresse 'from' et une signature. Ceux-ci ajoutent au moins 427 octets de surcharge.

Le numéro de protocole I2CP standard pour les datagrammes avec réponse possible est PROTO_DATAGRAM (17).

### Format

```
+----+----+----+----+----+----+----+----+
| from                                  |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+                                       +
|                                       |
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
| payload...
+----+----+----+----//

from :: a Destination
        length: 387+ bytes
        The originator and signer of the datagram

signature :: a Signature
             Signature type must match the signing public key type of $from
             length: 40+ bytes, as implied by the Signature type.
             For the default DSA_SHA1 key type:
                The DSA Signature of the SHA-256 hash of the payload.
             For other key types:
                The Signature of the payload.
             The signature may be verified by the signing public key of $from

payload :: The data
           Length: 0 to about 63 KB (see notes)

Total length: Payload length + 427+
```
### Notes

- La longueur pratique est limitée à la fois par les frais généraux à différentes couches et la fiabilité.
- Voir les notes importantes concernant la fiabilité des gros datagrammes dans la [documentation de l'API Datagrams](/docs/api/datagrams/). Pour de meilleurs résultats, limitez la charge utile à environ 10 KB ou moins.
- Les signatures pour les types autres que DSA_SHA1 ont été redéfinies dans la version 0.9.14.
- Le format ne supporte pas l'inclusion d'un bloc de signature hors ligne pour LS2 (proposition 123). Un nouveau protocole avec des drapeaux doit être défini pour cela.

## Datagram2 {#datagram2}

Le format Datagram2 est tel que spécifié dans la [Proposition 163](/proposals/163-datagram2/). Le numéro de protocole I2CP pour Datagram2 est 19.

Datagram2 est conçu comme un remplacement de Datagram1. Il ajoute les fonctionnalités suivantes à Datagram1 :

- Prévention des attaques par rejeu
- Support des signatures hors ligne
- Champs d'indicateurs et d'options pour l'extensibilité

Notez que l'algorithme de calcul de signature pour Datagram2 est substantiellement différent de celui pour Datagram1.

### Format

```
+----+----+----+----+----+----+----+----+
|                                       |
~            from                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~     offline_signature (optional)      ~
~   expires, sigtype, pubkey, offsig    ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            signature                  ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

from :: a Destination
        length: 387+ bytes
        The originator and (unless offline signed) signer of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x02 (0 0 1 0)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bit 5: If 0, no offline sig; if 1, offline signed
         Bits 15-6: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

offline_signature ::
             If flag indicates offline keys, the offline signature section,
             as specified in the Common Structures Specification,
             with the following 4 fields. Length: varies by online and offline
             sig types, typically 102 bytes for Ed25519
             This section can, and should, be generated offline.

  expires :: Expires timestamp
             (4 bytes, big endian, seconds since epoch, rolls over in 2106)

  sigtype :: Transient sig type (2 bytes, big endian)

  pubkey :: Transient signing public key (length as implied by sig type),
            typically 32 bytes for Ed25519 sig type.

  offsig :: a Signature
            Signature of expires timestamp, transient sig type,
            and public key, by the destination public key,
            length: 40+ bytes, as implied by the Signature type, typically
            64 bytes for Ed25519 sig type.

payload :: The data
           Length: 0 to about 61 KB (see notes)

signature :: a Signature
             Signature type must match the signing public key type of $from
             (if no offline signature) or the transient sigtype
             (if offline signed)
             length: 40+ bytes, as implied by the Signature type, typically
             64 bytes for Ed25519 sig type.
             The Signature of the payload and other fields as specified below.
             The signature is verified by the signing public key of $from
             (if no offline signature) or the transient pubkey
             (if offline signed)
```
Longueur totale : minimum 433 + longueur de la charge utile ; longueur typique pour les expéditeurs X25519 et sans signatures hors ligne : 457 + longueur de la charge utile. Notez que le message sera typiquement compressé avec gzip au niveau de la couche I2CP, ce qui entraînera des économies significatives si la destination source est compressible.

Note : Le format de signature hors ligne est le même que dans la [Spécification des structures communes](/docs/specs/common-structures/) et la [Spécification de streaming](/docs/specs/streaming/).

### Signatures

La signature porte sur les champs suivants :

- Prélude : Le hash de 32 octets de la destination cible (non inclus dans le datagramme)
- flags
- options (si présentes)
- offline_signature (si présente)
- payload

Dans le datagramme répliquable, pour le type de clé DSA_SHA1, la signature portait sur le hachage SHA-256 de la charge utile, pas sur la charge utile elle-même ; ici, la signature porte toujours sur les champs ci-dessus (PAS le hachage), quel que soit le type de clé.

### Vérification ToHash

Les destinataires doivent vérifier la signature (en utilisant le hachage de leur destination) et rejeter le datagramme en cas d'échec, pour empêcher les attaques par rejeu.

## Datagram3 {#datagram3}

Le format Datagram3 est tel que spécifié dans la [Proposition 163](/proposals/163-datagram2/). Le numéro de protocole I2CP pour Datagram3 est 20.

Datagram3 est conçu comme une version améliorée des datagrammes bruts. Il ajoute les fonctionnalités suivantes aux datagrammes bruts :

- Réplicabilité
- Champs de drapeaux et d'options pour l'extensibilité

Datagram3 n'est PAS authentifié. Dans une proposition future, l'authentification pourrait être fournie par la couche ratchet du router, et le statut d'authentification serait transmis au client.

### Format

```
+----+----+----+----+----+----+----+----+
|                                       |
~            fromhash                   ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

fromhash :: a Hash
            length: 32 bytes
            The originator of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x03 (0 0 1 1)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bits 15-5: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

payload :: The data
           Length: 0 to about 61 KB (see notes)
```
Longueur totale : minimum 34 + longueur de la charge utile.

## Références

- [Common](/docs/specs/common-structures/) - Spécification des structures communes
- [DATAGRAMS](/docs/api/datagrams/) - Aperçu de l'API Datagrams
- [I2CP](/docs/specs/i2cp/) - Spécification I2CP
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet/) - Proposition ECIES-X25519-AEAD-Ratchet
- [Prop163](/proposals/163-datagram2/) - Proposition Datagram2 et Datagram3
- [Prop169](/proposals/169-pq-crypto/) - Proposition de cryptographie post-quantique
- [SAMv3](/docs/api/samv3/) - Spécification SAM v3
- [Streaming](/docs/specs/streaming/) - Spécification Streaming
- [TRANSPORT](/docs/overview/transport/) - Aperçu du transport
- [TUNMSG](/docs/specs/tunnel-message/#notes) - Spécification des messages de tunnel
