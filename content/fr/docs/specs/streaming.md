---
title: "Spécification du Protocole de Streaming"
description: "Spécification du protocole de streaming I2P fournissant un transport fiable similaire à TCP"
slug: "streaming"
category: "Protocoles"
lastUpdated: "2023-10"
accurateFor: "0.9.59"
---

## Aperçu

Voir [Bibliothèque de Streaming](/docs/api/streaming) pour un aperçu du protocole Streaming.

## Versions du protocole

Le protocole de streaming n'inclut pas de champ de version. Les versions listées ci-dessous sont pour Java I2P. Les implémentations et le support cryptographique réel peuvent varier. Il n'y a aucun moyen de déterminer si l'extrémité distante prend en charge une version ou fonctionnalité particulière. Le tableau ci-dessous est fourni à titre d'orientation générale concernant les dates de sortie des diverses fonctionnalités.

Les fonctionnalités listées ci-dessous concernent le protocole lui-même. Diverses options de configuration sont documentées dans la [Bibliothèque de streaming](/docs/api/streaming) avec la version Java I2P dans laquelle elles ont été implémentées.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Router Version</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Streaming Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Bob's hash in NACKs field of SYN packet</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE option</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">I2CP protocol number enforced</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED no longer required in RESET</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PINGs and PONGs may include a payload</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA Ed25519 sig type</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA P-256, P-384, and P-521 sig types</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Variable-length signatures</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.7.1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Protocol numbers defined in I2CP</td>
    </tr>
  </tbody>
</table>
## Spécification du protocole

### Format de paquet

Le format d'un paquet unique dans le protocole de streaming est illustré ci-dessous. La taille minimale de l'en-tête, sans NACK ni données d'option, est de 22 octets.

Il n'y a pas de champ de longueur dans le protocole de streaming. L'encadrement est fourni par les couches inférieures - I2CP et I2NP.

```
+----+----+----+----+----+----+----+----+
| send Stream ID    | rcv Stream ID     |
+----+----+----+----+----+----+----+----+
| sequence  Num     | ack Through       |
+----+----+----+----+----+----+----+----+
| nc |  nc*4 bytes of NACKs (optional)
+----+----+----+----+----+----+----+----+
     | rd |  flags  | opt size| opt data
+----+----+----+----+----+----+----+----+
   ...  (optional, see below)           |
+----+----+----+----+----+----+----+----+
|   payload ...
+----+----+----+-//
```
**sendStreamId** :: 4 octets [Integer](/docs/specs/common-structures#integer) : Nombre aléatoire sélectionné par le destinataire du paquet avant d'envoyer le premier paquet de réponse SYN et constant pour la durée de vie de la connexion, supérieur à zéro. 0 dans le message SYN envoyé par l'initiateur de la connexion, et dans les messages suivants, jusqu'à ce qu'une réponse SYN soit reçue, contenant l'ID de flux du pair.

**receiveStreamId** :: 4 octets [Integer](/docs/specs/common-structures#integer) : Nombre aléatoire sélectionné par l'expéditeur du paquet avant d'envoyer le premier paquet SYN et constant pour toute la durée de la connexion, supérieur à zéro. Peut être 0 si inconnu, par exemple dans un paquet RESET.

**sequenceNum** :: 4 octets [Integer](/docs/specs/common-structures#integer) : Le numéro de séquence pour ce message, commençant à 0 dans le message SYN, et incrémenté de 1 dans chaque message sauf pour les ACK simples et les retransmissions. Si le sequenceNum est 0 et que le flag SYN n'est pas défini, il s'agit d'un paquet ACK simple qui ne doit pas être acquitté.

**ackThrough** :: 4 octets [Integer](/docs/specs/common-structures#integer) : Le numéro de séquence de paquet le plus élevé qui a été reçu sur le receiveStreamId. Ce champ est ignoré sur le paquet de connexion initial (où receiveStreamId est l'id inconnu) ou si le flag NO_ACK est défini. Tous les paquets jusqu'à et incluant ce numéro de séquence sont ACKés, SAUF ceux listés dans les NACKs ci-dessous.

**Nombre de NACK** :: 1 octet [Entier](/docs/specs/common-structures#integer) : Le nombre de NACK de 4 octets dans le champ suivant, ou 8 lorsqu'utilisé avec SYNCHRONIZE pour la prévention de rejeu à partir de la version 0.9.58 ; voir ci-dessous.

**NACKs** :: nc * 4 octets [Integer](/docs/specs/common-structures#integer)s : Numéros de séquence inférieurs à ackThrough qui ne sont pas encore reçus. Deux NACKs d'un paquet constituent une demande de « retransmission rapide » de ce paquet. Également utilisé conjointement avec SYNCHRONIZE pour la prévention de rejeu depuis la version 0.9.58 ; voir ci-dessous.

**resendDelay** :: 1 octet [Integer](/docs/specs/common-structures#integer) : Combien de temps le créateur de ce paquet va-t-il attendre avant de renvoyer ce paquet (s'il n'a pas encore été acquitté). La valeur est en secondes depuis la création du paquet. Actuellement ignoré à la réception.

**flags** :: valeur de 2 octets : Voir ci-dessous.

**option size** :: [Integer](/docs/specs/common-structures#integer) sur 2 octets : Le nombre d'octets dans le champ suivant

**données d'option** :: 0 ou plus d'octets : Comme spécifié par les flags. Voir ci-dessous.

**payload** :: taille restante du paquet

### Champs de drapeaux et de données d'options

Le champ flags ci-dessus spécifie certaines métadonnées sur le paquet, et peut à son tour nécessiter l'inclusion de certaines données supplémentaires. Les flags sont les suivants. Toute structure de données spécifiée doit être ajoutée à la zone d'options dans l'ordre donné.

Ordre des bits : 15....0 (15 est le MSB)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Flag</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Order</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SYNCHRONIZE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP SYN. Set in the initial packet and in the first response. FROM_INCLUDED and SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">CLOSE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP FIN. If the response to a SYNCHRONIZE fits in a single message, the response will contain both SYNCHRONIZE and CLOSE. SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RESET</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Abnormal close. SIGNATURE_INCLUDED must also be set. Prior to release 0.9.20, due to a bug, FROM_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#signature">Signature</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, CLOSE, and RESET, where it is required, and with ECHO, where it is required for a ping. The signature uses the Destination's <a href="/docs/specs/common-structures#signingprivatekey">SigningPrivateKey</a> to sign the entire header and payload with the space in the option data field for the signature being set to all zeroes. Prior to release 0.9.11, the signature was always 40 bytes. As of release 0.9.11, the signature may be variable-length, see below for details.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused. Requests every packet in the other direction to have SIGNATURE_INCLUDED</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">387+ byte <a href="/docs/specs/common-structures#destination">Destination</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, where it is required, and with ECHO, where it is required for a ping. Prior to release 0.9.20, due to a bug, must also be sent with RESET.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DELAY_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Optional delay. How many milliseconds the sender of this packet wants the recipient to wait before sending any more data. A value greater than 60000 indicates choking. A value of 0 requests an immediate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MAX_PACKET_SIZE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum length of the payload. Send with SYNCHRONIZE.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PROFILE_INTERACTIVE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused or ignored; the interactive profile is unimplemented.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECHO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused except by ping programs. If set, most other options are ignored. See the <a href="/docs/api/streaming">streaming docs</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">NO_ACK</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">This flag simply tells the recipient to ignore the ackThrough field in the header. Currently set in the initial SYN packet, otherwise the ackThrough field is always valid. Note that this does not save any space, the ackThrough field is before the flags and is always present.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#offlinesignature">OfflineSig</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Contains the offline signature section from LS2. See proposal 123 and the common structures specification. FROM_INCLUDED must also be set. Contains an OfflineSig: 1) Expires timestamp (4 bytes, seconds since epoch, rolls over in 2106) 2) Transient sig type (2 bytes) 3) Transient <a href="/docs/specs/common-structures#signingpublickey">SigningPublicKey</a> (length as implied by sig type) 4) <a href="/docs/specs/common-structures#signature">Signature</a> of expires timestamp, transient sig type, and public key, by the destination public key. Length of sig as implied by the destination public key sig type.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12-15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">unused</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Set to zero for compatibility with future uses.</td>
    </tr>
  </tbody>
</table>
### Notes sur les signatures de longueur variable

Avant la version 0.9.11, la signature dans le champ d'option faisait toujours 40 octets.

À partir de la version 0.9.11, la signature a une longueur variable. Le type et la longueur de la Signature sont déduits du type de clé utilisé dans l'option FROM_INCLUDED et de la documentation [Signature](/docs/specs/common-structures#signature).

À partir de la version 0.9.39, l'option OFFLINE_SIGNATURE est prise en charge. Si cette option est présente, la [SigningPublicKey](/docs/specs/common-structures#signingpublickey) transitoire est utilisée pour vérifier tous les paquets signés, et la longueur et le type de signature sont déduits de la SigningPublicKey transitoire dans l'option.

- Lorsqu'un paquet contient à la fois FROM_INCLUDED et SIGNATURE_INCLUDED (comme dans SYNCHRONIZE), l'inférence peut être faite directement.

- Lorsqu'un paquet ne contient pas FROM_INCLUDED, l'inférence doit être faite à partir d'un paquet SYNCHRONIZE précédent.

- Lorsqu'un paquet ne contient pas FROM_INCLUDED, et qu'il n'y a pas eu de paquet SYNCHRONIZE précédent (par exemple un paquet CLOSE ou RESET isolé), l'inférence peut être faite à partir de la longueur des options restantes (puisque SIGNATURE_INCLUDED est la dernière option), mais le paquet sera probablement rejeté de toute façon, car il n'y a pas de FROM disponible pour valider la signature. Si d'autres champs d'options sont définis à l'avenir, ils devront être pris en compte.

### Prévention des attaques par rejeu

Pour empêcher Bob d'utiliser une attaque par rejeu en stockant un paquet SYNCHRONIZE signé valide reçu d'Alice et en l'envoyant plus tard à une victime Charlie, Alice doit inclure le hash de destination de Bob dans le paquet SYNCHRONIZE comme suit :

```
Set NACK count field to 8
Set the NACKs field to Bob's 32-byte destination hash
```
À la réception d'un SYNCHRONIZE, si le champ de comptage NACK est 8, Bob doit interpréter le champ NACKs comme un hachage de destination de 32 octets, et doit vérifier qu'il correspond à son hachage de destination. Il doit également vérifier la signature du paquet comme d'habitude, car celle-ci couvre l'ensemble du paquet incluant les champs de comptage NACK et NACKs. Si le comptage NACK est 8 et que le champ NACKs ne correspond pas, Bob doit abandonner le paquet.

Ceci est requis pour les versions 0.9.58 et supérieures. Ceci est rétrocompatible avec les versions plus anciennes, car les NACK ne sont pas attendus dans un paquet SYNCHRONIZE. Les destinations ne savent pas et ne peuvent pas savoir quelle version fonctionne à l'autre extrémité.

Aucune modification n'est nécessaire pour le paquet SYNCHRONIZE ACK envoyé de Bob à Alice ; n'incluez pas de NACK dans ce paquet.

## Références

- **[Destination]** [Destination](/docs/specs/common-structures#destination)
- **[Integer]** [Integer](/docs/specs/common-structures#integer)
- **[OfflineSig]** [OfflineSignature](/docs/specs/common-structures#offlinesignature)
- **[Signature]** [Signature](/docs/specs/common-structures#signature)
- **[SigningPrivateKey]** [SigningPrivateKey](/docs/specs/common-structures#signingprivatekey)
- **[SigningPublicKey]** [SigningPublicKey](/docs/specs/common-structures#signingpublickey)
- **[STREAMING]** [Bibliothèque Streaming](/docs/api/streaming)
