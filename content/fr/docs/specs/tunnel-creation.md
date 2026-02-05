---
title: "Spécification de création de tunnel"
description: "Spécification de construction de tunnel ElGamal pour créer des tunnels en utilisant le télescopage non interactif."
slug: "tunnel-creation"
aliases: 
category: "Conception"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Aperçu

NOTE : OBSOLÈTE - Ceci est la spécification de construction de tunnel ElGamal. Voir [tunnel-creation-ecies](/docs/specs/tunnel-creation-ecies/) pour la spécification de construction de tunnel X25519.

Ce document spécifie les détails des messages de construction de tunnel chiffrés utilisés pour créer des tunnels en utilisant une méthode de "télescopage non-interactif". Voir le document de construction de tunnel [TUNNEL-IMPL](/docs/specs/tunnel-implementation/) pour un aperçu du processus, incluant les méthodes de sélection et d'ordonnancement des pairs.

La création de tunnel est accomplie par un seul message transmis le long du chemin des pairs dans le tunnel, réécrit sur place, et retransmis au créateur du tunnel. Ce message de tunnel unique est composé d'un nombre variable d'enregistrements (jusqu'à 8) - un pour chaque pair potentiel dans le tunnel. Les enregistrements individuels sont chiffrés asymétriquement (ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)) pour être lus uniquement par un pair spécifique le long du chemin, tandis qu'une couche supplémentaire de chiffrement symétrique (AES [CRYPTO-AES](/docs/specs/cryptography/#aes)) est ajoutée à chaque saut afin d'exposer l'enregistrement chiffré asymétriquement uniquement au moment approprié.

### Nombre d'enregistrements

Tous les enregistrements ne doivent pas nécessairement contenir des données valides. Le message de construction pour un tunnel à 3 sauts, par exemple, peut contenir plus d'enregistrements pour masquer la longueur réelle du tunnel aux participants. Il existe deux types de messages de construction. Le message de construction de tunnel original ([TBM](/docs/specs/i2np/#struct-TunnelBuild)) contient 8 enregistrements, ce qui est largement suffisant pour toute longueur de tunnel pratique. Le nouveau message de construction de tunnel variable ([VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild)) contient de 1 à 8 enregistrements. L'initiateur peut faire un compromis entre la taille du message et le niveau d'obfuscation souhaité pour la longueur du tunnel.

Dans le réseau actuel, la plupart des tunnels font 2 ou 3 sauts de long. L'implémentation actuelle utilise un VTBM à 5 enregistrements pour construire des tunnels de 4 sauts ou moins, et le TBM à 8 enregistrements pour les tunnels plus longs. Le VTBM à 5 enregistrements (qui, une fois fragmenté, tient dans trois messages de tunnel de 1 Ko) réduit le trafic réseau et augmente le taux de réussite de construction, car les messages plus petits ont moins de chances d'être abandonnés.

Le message de réponse doit être du même type et de la même longueur que le message de construction.

### Spécification des enregistrements de requête

Également spécifié dans la spécification I2NP [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

Texte en clair de l'enregistrement, visible uniquement au hop interrogé :

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">tunnel ID to receive messages as, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4-35</td><td style="border:1px solid var(--color-border); padding:0.6rem;">local router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">36-39</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next tunnel ID, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">40-71</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">72-103</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel layer key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">104-135</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel IV key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">136-167</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">168-183</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply IV</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">184</td><td style="border:1px solid var(--color-border); padding:0.6rem;">flags</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">185-188</td><td style="border:1px solid var(--color-border); padding:0.6rem;">request time (in hours since the epoch, rounded down)</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">189-192</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next message ID</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">193-221</td><td style="border:1px solid var(--color-border); padding:0.6rem;">uninterpreted / random padding</td></tr>
</tbody>
</table>
Les champs ID du tunnel suivant et hachage d'identité du routeur suivant sont utilisés pour spécifier le saut suivant dans le tunnel, bien que pour un point de terminaison de tunnel sortant, ils spécifient où le message de réponse de création de tunnel réécrit doit être envoyé. De plus, l'ID du message suivant spécifie l'ID de message que le message (ou la réponse) doit utiliser.

La clé de couche tunnel, la clé IV de tunnel, la clé de réponse et l'IV de réponse sont chacune des valeurs aléatoires de 32 octets générées par le créateur, pour utilisation dans cet enregistrement de demande de construction uniquement.

Le champ flags contient ce qui suit (ordre des bits : 76543210, le bit 7 est le MSB) :

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages from anyone</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages to anyone, and send the reply to the specified next hop in a Tunnel Build Reply Message</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5-0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Undefined, must set to 0 for compatibility with future options</td></tr>
</tbody>
</table>
Le bit 7 indique que le saut sera une passerelle d'entrée (IBGW). Le bit 6 indique que le saut sera un point de sortie (OBEP). Si aucun bit n'est défini, le saut sera un participant intermédiaire. Les deux ne peuvent pas être définis en même temps.

#### Création d'enregistrement de requête

Chaque saut reçoit un Tunnel ID aléatoire, non nul. Les Tunnel IDs du saut actuel et du saut suivant sont remplis. Chaque enregistrement reçoit une clé IV de tunnel aléatoire, un IV de réponse, une clé de couche et une clé de réponse.

#### Chiffrement des enregistrements de requête

Cet enregistrement en texte clair est chiffré ElGamal 2048 [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) avec la clé publique de chiffrement du saut et formaté en un enregistrement de 528 octets :

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">First 16 bytes of the SHA-256 of the current hop's router identity</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">16-527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal-2048 encrypted request record</td></tr>
</tbody>
</table>
Dans l'enregistrement chiffré de 512 octets, les données ElGamal contiennent les octets 1-256 et 258-513 du bloc chiffré ElGamal de 514 octets [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). Les deux octets de remplissage du bloc (les octets zéro aux positions 0 et 257) sont supprimés.

Puisque le texte en clair utilise le champ complet, il n'y a pas besoin de remplissage supplémentaire au-delà de `SHA256(cleartext) + cleartext`.

Chaque enregistrement de 528 octets est alors chiffré de manière itérative (en utilisant le déchiffrement AES, avec la clé de réponse et l'IV de réponse pour chaque saut) de sorte que l'identité du router ne soit en texte clair que pour le saut en question.

### Traitement et chiffrement des sauts

Quand un saut reçoit un TunnelBuildMessage, il parcourt les enregistrements qu'il contient pour en trouver un commençant par son propre hash d'identité (tronqué à 16 octets). Il déchiffre alors le bloc ElGamal de cet enregistrement et récupère le texte clair protégé. À ce moment-là, il s'assure que la demande de tunnel n'est pas un duplicata en alimentant la clé de réponse AES-256 dans un filtre de Bloom. Les duplicatas ou les demandes invalides sont supprimés. Les enregistrements qui ne sont pas estampillés avec l'heure actuelle, ou l'heure précédente si peu après le début de l'heure, doivent être supprimés. Par exemple, prenez l'heure dans l'horodatage, convertissez-la en heure complète, puis si elle a plus de 65 minutes de retard ou 5 minutes d'avance sur l'heure actuelle, elle est invalide. Le filtre de Bloom doit avoir une durée d'au moins une heure (plus quelques minutes, pour permettre la dérive d'horloge), de sorte que les enregistrements dupliqués dans l'heure actuelle qui ne sont pas rejetés en vérifiant l'horodatage de l'heure dans l'enregistrement, seront rejetés par le filtre.

Après avoir décidé s'ils acceptent ou non de participer au tunnel, ils remplacent l'enregistrement qui contenait la demande par un bloc de réponse chiffré. Tous les autres enregistrements sont chiffrés en AES-256 [CRYPTO-AES](/docs/specs/cryptography/#aes) avec la clé de réponse et l'IV inclus. Chacun est chiffré séparément en AES/CBC avec la même clé de réponse et le même IV de réponse. Le mode CBC n'est pas continué (chaîné) entre les enregistrements.

Chaque hop ne connaît que sa propre réponse. S'il accepte, il maintiendra le tunnel jusqu'à expiration, même s'il ne sera pas utilisé, car il ne peut pas savoir si tous les autres hops ont accepté.

#### Spécification d'enregistrement de réponse

Après que le saut actuel a lu son enregistrement, il le remplace par un enregistrement de réponse indiquant s'il accepte ou non de participer au tunnel, et s'il refuse, il classe sa raison de rejet. Il s'agit simplement d'une valeur de 1 octet, où 0x0 signifie qu'il accepte de participer au tunnel, et les valeurs plus élevées signifient des niveaux de rejet plus élevés.

Les codes de rejet suivants sont définis :

- TUNNEL_REJECT_PROBABALISTIC_REJECT = 10
- TUNNEL_REJECT_TRANSIENT_OVERLOAD = 20
- TUNNEL_REJECT_BANDWIDTH = 30
- TUNNEL_REJECT_CRIT = 50

Pour dissimuler d'autres causes, telles que l'arrêt du router, aux pairs, l'implémentation actuelle utilise TUNNEL_REJECT_BANDWIDTH pour presque tous les rejets.

La réponse est chiffrée avec la clé de session AES qui lui a été fournie dans le bloc chiffré, complétée avec 495 octets de données aléatoires pour atteindre la taille d'enregistrement complète. Le remplissage est placé avant l'octet de statut :

`AES-256-CBC(SHA-256(padding+status) + padding + status, key, IV)`

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-31</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SHA-256 of bytes 32-527</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">32-526</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Random padding</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Reply value</td></tr>
</tbody>
</table>
Ceci est également décrit dans la spécification I2NP [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

### Préparation du Message de Construction de Tunnel

Lors de la construction d'un nouveau Tunnel Build Message, tous les Build Request Records doivent d'abord être construits et chiffrés de manière asymétrique en utilisant ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). Chaque enregistrement est ensuite déchiffré de manière préventive avec les clés de réponse et les IV des sauts précédents dans le chemin, en utilisant AES [CRYPTO-AES](/docs/specs/cryptography/#aes). Ce déchiffrement doit être exécuté dans l'ordre inverse afin que les données chiffrées asymétriquement apparaissent en clair au bon saut après que son prédécesseur les ait chiffrées.

Les enregistrements excédentaires non nécessaires pour les requêtes individuelles sont simplement remplis avec des données aléatoires par le créateur.

### Livraison de Message de Construction de Tunnel

Pour les tunnels sortants, la livraison se fait directement du créateur du tunnel au premier saut, en empaquetant le TunnelBuildMessage comme si le créateur était juste un autre saut dans le tunnel. Pour les tunnels entrants, la livraison se fait à travers un tunnel sortant existant. Le tunnel sortant provient généralement du même pool que le nouveau tunnel en cours de construction. Si aucun tunnel sortant n'est disponible dans ce pool, un tunnel exploratoire sortant est utilisé. Au démarrage, quand aucun tunnel exploratoire sortant n'existe encore, un faux tunnel sortant à 0-saut est utilisé.

### Gestion des Points de Terminaison des Messages de Construction de Tunnel

Pour la création d'un tunnel sortant, lorsque la requête atteint un point de terminaison sortant (tel que déterminé par le flag 'permettre les messages à n'importe qui'), le hop est traité comme d'habitude, chiffrant une réponse à la place de l'enregistrement et chiffrant tous les autres enregistrements, mais puisqu'il n'y a pas de 'hop suivant' vers lequel transmettre le TunnelBuildMessage, il place à la place les enregistrements de réponse chiffrés dans un TunnelBuildReplyMessage ([TBRM](/docs/specs/i2np/#struct-TunnelBuildReply)) ou VariableTunnelBuildReplyMessage ([VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply)) (le type de message et le nombre d'enregistrements doivent correspondre à ceux de la requête) et le livre au tunnel de réponse spécifié dans l'enregistrement de requête. Ce tunnel de réponse transmet le Tunnel Build Reply Message en retour vers le créateur du tunnel, exactement comme pour tout autre message [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation). Le créateur du tunnel le traite ensuite, comme décrit ci-dessous.

Le tunnel de réponse a été sélectionné par le créateur comme suit : En général, il s'agit d'un tunnel entrant du même groupe que le nouveau tunnel sortant en cours de construction. Si aucun tunnel entrant n'est disponible dans ce groupe, un tunnel exploratoire entrant est utilisé. Au démarrage, lorsqu'aucun tunnel exploratoire entrant n'existe encore, un faux tunnel entrant à 0 saut est utilisé.

Pour la création d'un tunnel entrant, lorsque la requête atteint le point de terminaison entrant (également connu sous le nom de créateur de tunnel), il n'est pas nécessaire de générer un message de réponse de construction de tunnel explicite, et le router traite chacune des réponses, comme ci-dessous.

### Traitement des messages de réponse de construction de tunnel

Pour traiter les enregistrements de réponse, le créateur doit simplement déchiffrer AES chaque enregistrement individuellement, en utilisant la clé de réponse et l'IV de chaque saut dans le tunnel après le pair (dans l'ordre inverse). Cela révèle alors la réponse spécifiant s'ils acceptent de participer au tunnel ou pourquoi ils refusent. S'ils acceptent tous, le tunnel est considéré comme créé et peut être utilisé immédiatement, mais si quelqu'un refuse, le tunnel est abandonné.

Les accords et rejets sont notés dans le profil de chaque pair [PEER-SELECTION](/docs/overview/tunnel-routing/), pour être utilisés dans les évaluations futures de la capacité de tunnel du pair.

## Historique et Notes

Cette stratégie a vu le jour lors d'une discussion sur la liste de diffusion I2P entre Michael Rogers, Matthew Toseland (toad), et jrandom concernant l'attaque du prédécesseur. Voir [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html), [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html). Elle a été introduite dans la version 0.6.1.10 le 16 février 2006, qui était la dernière fois qu'un changement non rétrocompatible a été effectué dans I2P.

Notes :

- Cette conception n'empêche pas deux pairs hostiles au sein d'un tunnel de marquer un ou plusieurs enregistrements de requête ou de réponse pour détecter qu'ils se trouvent dans le même tunnel, mais cela peut être détecté par le créateur du tunnel lors de la lecture de la réponse, ce qui entraîne le marquage du tunnel comme invalide.
- Cette conception n'inclut pas de preuve de travail sur la section chiffrée de manière asymétrique, bien que le hash d'identité de 16 octets pourrait être réduit de moitié avec la seconde moitié remplacée par une fonction hashcash d'un coût allant jusqu'à 2^64.
- Cette conception seule n'empêche pas deux pairs hostiles au sein d'un tunnel d'utiliser les informations de temporisation pour déterminer s'ils sont dans le même tunnel. L'utilisation de la livraison de requêtes groupées et synchronisées pourrait aider (regrouper les requêtes et les envoyer à la minute (synchronisée ntp)). Cependant, cela permet aux pairs de 'marquer' les requêtes en les retardant et en détectant le retard plus tard dans le tunnel, bien que peut-être abandonner les requêtes non livrées dans une petite fenêtre pourrait fonctionner (bien que cela nécessiterait un haut degré de synchronisation d'horloge). Alternativement, peut-être que les sauts individuels pourraient injecter un délai aléatoire avant de transmettre la requête ?
- Y a-t-il des méthodes non fatales de marquage de la requête ?
- L'horodatage avec une résolution d'une heure est utilisé pour la prévention de la relecture. Cette contrainte n'était pas appliquée jusqu'à la version 0.9.16.

## Travaux futurs

- Dans l'implémentation actuelle, l'initiateur laisse un enregistrement vide pour lui-même. Ainsi, un message de n enregistrements ne peut construire qu'un tunnel de n-1 sauts. Cela semble nécessaire pour les tunnels entrants (où l'avant-dernier saut peut voir le préfixe de hachage pour le saut suivant), mais pas pour les tunnels sortants. Ceci doit être recherché et vérifié. S'il est possible d'utiliser l'enregistrement restant sans compromettre l'anonymat, nous devrions le faire.
- Analyse plus approfondie des possibles attaques de marquage et de chronométrage décrites dans les notes ci-dessus.
- Utiliser uniquement VTBM ; ne pas sélectionner d'anciens pairs qui ne le supportent pas.
- L'enregistrement de demande de construction ne spécifie pas de durée de vie ou d'expiration du tunnel ; chaque saut fait expirer le tunnel après 10 minutes, ce qui est une constante codée en dur à l'échelle du réseau. Nous pourrions utiliser un bit dans le champ flag et prendre 4 (ou 8) octets du bourrage pour spécifier une durée de vie ou une expiration. Le demandeur ne spécifierait cette option que si tous les participants la supportaient.

## Références

- [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) - Spécification BuildRequestRecord
- [CRYPTO-AES](/docs/specs/cryptography/#aes) - Chiffrement AES
- [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) - Chiffrement ElGamal
- [HASHING-IT-OUT](http://www-users.cs.umn.edu/~hopper/hashing_it_out.pdf)
- [PEER-SELECTION](/docs/overview/tunnel-routing/)
- [PREDECESSOR](http://forensics.umass.edu/pubs/wright-tissec.pdf)
- [PREDECESSOR-2008](http://forensics.umass.edu/pubs/wright.tissec.2008.pdf)
- [TBM](/docs/specs/i2np/#struct-TunnelBuild) - TunnelBuildMessage
- [TBRM](/docs/specs/i2np/#struct-TunnelBuildReply) - TunnelBuildReplyMessage
- [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html)
- [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html)
- [TUNNEL-IMPL](/docs/specs/tunnel-implementation/)
- [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation)
- [VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild) - VariableTunnelBuildMessage
- [VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply) - VariableTunnelBuildReplyMessage
