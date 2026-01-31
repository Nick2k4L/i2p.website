---
title: "Protocole de streaming"
description: "Transport de type TCP utilisé par la plupart des applications I2P"
slug: "streaming"
lastUpdated: "2025-07"
accurateFor: "0.9.67"
---

## Aperçu {#overview}

La bibliothèque de streaming fait techniquement partie de la couche "application", car elle n'est pas une fonction principale du router. En pratique, cependant, elle fournit une fonction vitale pour presque toutes les applications I2P existantes, en proposant des flux similaires à TCP sur I2P, et en permettant aux applications existantes d'être facilement portées vers I2P. L'autre bibliothèque de transport de bout en bout pour la communication client est la [bibliothèque datagram](/docs/specs/datagrams).

La bibliothèque streaming est une couche au-dessus de l'[API I2CP](/docs/specs/i2cp) principale qui permet aux flux de messages fiables, ordonnés et authentifiés de fonctionner sur une couche de messages non fiable, non ordonnée et non authentifiée. Tout comme la relation entre TCP et IP, cette fonctionnalité de streaming dispose de toute une série de compromis et d'optimisations disponibles, mais plutôt que d'intégrer cette fonctionnalité dans le code I2P de base, elle a été séparée dans sa propre bibliothèque à la fois pour maintenir les complexités de type TCP séparées et pour permettre des implémentations alternatives optimisées.

En considération du coût relativement élevé des messages, le protocole de la bibliothèque de streaming pour la planification et la livraison de ces messages a été optimisé pour permettre aux messages individuels transmis de contenir autant d'informations que possible. Par exemple, une petite transaction HTTP proxifiée à travers la bibliothèque de streaming peut être complétée en un seul aller-retour - les premiers messages regroupent un SYN, FIN, et la petite charge utile de la requête HTTP, et la réponse regroupe le SYN, FIN, ACK, et la charge utile de la réponse HTTP. Bien qu'un ACK supplémentaire doive être transmis pour indiquer au serveur HTTP que le SYN/FIN/ACK a été reçu, le proxy HTTP local peut souvent livrer la réponse complète au navigateur immédiatement.

La bibliothèque de streaming ressemble beaucoup à une abstraction de TCP, avec ses fenêtres glissantes, ses algorithmes de contrôle de congestion (à la fois démarrage lent et évitement de congestion), et son comportement général des paquets (ACK, SYN, FIN, RST, calcul rto, etc).

La bibliothèque de streaming est une bibliothèque robuste optimisée pour fonctionner sur I2P. Elle dispose d'une configuration en une phase et contient une implémentation complète de fenêtrage.

## API {#api}

L'API de la bibliothèque de streaming fournit un paradigme de socket standard aux applications Java. L'API [I2CP](/docs/specs/i2cp) de niveau inférieur est complètement cachée, sauf que les applications peuvent transmettre des [paramètres I2CP](/docs/specs/i2cp#options) à travers la bibliothèque de streaming, pour être interprétés par I2CP.

L'interface standard de la bibliothèque de streaming consiste pour l'application à utiliser l'I2PSocketManagerFactory pour créer un I2PSocketManager. L'application demande ensuite au gestionnaire de socket une I2PSession, ce qui provoquera une connexion au routeur via [I2CP](/docs/specs/i2cp). L'application peut alors établir des connexions avec un I2PSocket ou recevoir des connexions avec un I2PServerSocket.

Pour un bon exemple d'utilisation, voir le code i2psnark.

### Options et valeurs par défaut {#options}

Les options et les valeurs par défaut actuelles sont listées ci-dessous. Les options sont sensibles à la casse et peuvent être définies pour l'ensemble du router, pour un client particulier, ou pour une socket individuelle sur une base par connexion. De nombreuses valeurs sont ajustées pour les performances HTTP dans des conditions I2P typiques. D'autres applications telles que les services pair-à-pair sont fortement encouragées à modifier selon les besoins, en définissant les options et en les passant via l'appel à I2PSocketManagerFactory.createManager(_i2cpHost, _i2cpPort, opts). Les valeurs de temps sont en ms.

Notez que les API de niveau supérieur, telles que [SAM](/docs/api/samv3), [BOB](/docs/legacy/bob), et [I2PTunnel](/docs/api/i2ptunnel), peuvent remplacer ces valeurs par défaut par leurs propres valeurs par défaut. Notez également que de nombreuses options ne s'appliquent qu'aux serveurs qui écoutent les connexions entrantes.

À partir de la version 0.9.1, la plupart des options, mais pas toutes, peuvent être modifiées sur un gestionnaire de socket ou une session actifs. Consultez la javadoc pour plus de détails.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Default</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.accessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes used for either access list or blacklist. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.destination.sigType</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The name or number of the signature type for a transient destination. As of release 0.9.12.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableAccessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a whitelist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableBlackList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a blacklist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.answerPings</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to respond to incoming pings</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.blacklist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes to be blacklisted for incoming connections to ALL destinations in the context. This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.3.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.bufferSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64K</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How much transmit data (in bytes) will be accepted that hasn't been written out yet.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.congestionAvoidanceGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in congestion avoidance, we grow the window size at the rate of <code>1/(windowSize*factor)</code>. In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to wait after instantiating a new con before actually attempting to connect. If this is &lt;= 0, connect immediately with no initial data. If greater than 0, wait until the output stream is flushed, the buffer fills, or that many milliseconds pass, and include any initial data with the SYN.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5*60*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on connect, in milliseconds. Negative means indefinitely. Default is 5 minutes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.disableRejectLogging</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to disable warnings in the logs when an incoming connection is rejected due to connection limits. As of release 0.9.4.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.dsalist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes or host names to be contacted using an alternate DSA destination. Only applies if multisession is enabled and the primary session is non-DSA (generally for shared clients only). This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.21.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.enforceProtocol</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to listen only for the streaming protocol. Setting to true will prohibit communication with Destinations earlier than release 0.7.1 (released March 2009). Set to true if running multiple protocols on this Destination. As of release 0.9.1. Default true as of release 0.9.36.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 (send)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0=noop, 1=disconnect) What to do on an inactivity timeout - do nothing, disconnect, or send a duplicate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">90*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Idle time before sending a keepalive</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialAckDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">750</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Delay before sending an ack</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialResendDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The initial value of the resend delay field in the packet header, times 1000. Not fully implemented; see below.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial timeout (if no <a href="#sharing">sharing data</a> available). As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial round trip time estimate (if no <a href="#sharing">sharing data</a> available). Disabled as of release 0.9.8; uses actual RTT.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(if no <a href="#sharing">sharing data</a> available) In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.limitAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reset</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">What action to take when an incoming connection exceeds limits. Valid values are: reset (reset the connection); drop (drop the connection); or http (send a hardcoded HTTP 429 response). Any other value is a custom response to be sent. backslash-r and backslash-n will be replaced with CR and LF. As of release 0.9.34.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConcurrentStreams</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0 or negative value means unlimited) This is a total limit for incoming and outgoing combined.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxMessageSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1730</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum size of the payload, i.e. the MTU in bytes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxResends</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Maximum number of retransmissions before failure.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (all peers; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.profile</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 (bulk)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1=bulk; 2=interactive; see important notes <a href="#profile">below</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.readTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on read, in milliseconds. Negative means indefinitely.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.slowStartGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in slow start, we grow the window size at the rate of 1/(factor). In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttdevDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.wdwDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.writeTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on write/flush, in milliseconds. Negative means indefinitely.</td>
    </tr>
  </tbody>
</table>
## Spécification du protocole {#spec}

[Voir la page de spécification de la bibliothèque Streaming.](/docs/specs/streaming)

## Détails d'implémentation {#implementation}

### Configuration {#setup}

L'initiateur envoie un paquet avec le flag SYNCHRONIZE activé. Ce paquet peut également contenir les données initiales. Le pair répond avec un paquet avec le flag SYNCHRONIZE activé. Ce paquet peut également contenir les données de réponse initiales.

L'initiateur peut envoyer des paquets de données supplémentaires, jusqu'à la taille de fenêtre initiale, avant de recevoir la réponse SYNCHRONIZE. Ces paquets auront également le champ send Stream ID défini à 0. Les destinataires doivent mettre en tampon les paquets reçus sur des flux inconnus pendant une courte période, car ils peuvent arriver dans le désordre, avant le paquet SYNCHRONIZE.

### Sélection et négociation de la MTU {#mtu}

La taille maximale des messages (aussi appelée MTU / MRU) est négociée à la valeur la plus faible supportée par les deux pairs. Comme les messages tunnel sont rembourrés à 1 Ko, une mauvaise sélection de MTU entraînera une grande quantité de surcharge. La MTU est spécifiée par l'option i2p.streaming.maxMessageSize. La MTU par défaut actuelle de 1730 a été choisie pour s'adapter précisément dans deux messages tunnel I2NP de 1 Ko, incluant la surcharge pour le cas typique.

Note : Il s'agit de la taille maximale de la charge utile uniquement, sans inclure l'en-tête.

Note : Pour les connexions ECIES, qui ont une surcharge réduite, le MTU recommandé est de 1812. Le MTU par défaut reste de 1730 pour toutes les connexions, quel que soit le type de clé utilisé. Les clients doivent utiliser le minimum entre le MTU envoyé et reçu, comme d'habitude. Voir la proposition 155.

Le premier message dans une connexion inclut une Destination de 387 octets (typique) ajoutée par la couche de streaming, et généralement un leaseSet de 898 octets (typique), ainsi que des clés de session, regroupés dans le message garlic par le router. (Le leaseSet et les clés de session ne seront pas regroupés si une session ElGamal a été établie précédemment). Par conséquent, l'objectif de faire tenir une requête HTTP complète dans un seul message I2NP de 1KB n'est pas toujours atteignable. Cependant, la sélection du MTU, ainsi qu'une implémentation soigneuse des stratégies de fragmentation et de regroupement par lots dans le processeur de passerelle tunnel, sont des facteurs importants pour la bande passante réseau, la latence, la fiabilité et l'efficacité, en particulier pour les connexions de longue durée.

### Intégrité des données {#integrity}

L'intégrité des données est assurée par la somme de contrôle gzip CRC-32 implémentée dans [la couche I2CP](/docs/specs/i2cp#format). Il n'y a pas de champ de somme de contrôle dans le protocole de streaming.

### Encapsulation des paquets {#encapsulation}

Chaque paquet est envoyé via I2P comme un message unique (ou comme un clove individuel dans un [Garlic Message](/docs/overview/garlic-routing)). L'encapsulation des messages est implémentée dans les couches sous-jacentes [I2CP](/docs/specs/i2cp), [I2NP](/docs/specs/i2np), et [tunnel message](/docs/specs/tunnel-message). Il n'y a pas de mécanisme de délimiteur de paquet ou de champ de longueur de charge utile dans le protocole de streaming.

### Délai optionnel {#delay}

Les paquets de données peuvent inclure un champ de délai optionnel spécifiant le délai demandé, en ms, avant que le récepteur ne doive accuser réception du paquet. Les valeurs valides sont de 0 à 60000 inclus. Une valeur de 0 demande un accusé de réception immédiat. Ceci est purement consultatif, et les récepteurs devraient retarder légèrement afin que des paquets supplémentaires puissent être accusés de réception avec un seul accusé. Certaines implémentations peuvent inclure une valeur consultative de (RTT mesuré / 2) dans ce champ. Pour les valeurs de délai optionnelles non nulles, les récepteurs devraient limiter le délai maximum avant d'envoyer un accusé de réception à quelques secondes au maximum. Les valeurs de délai optionnelles supérieures à 60000 indiquent un étranglement, voir ci-dessous.

### Fenêtres de Transmission/Réception et Limitation de Débit {#windows}

Les en-têtes TCP incluent la fenêtre de réception en octets ; cependant, le protocole de streaming ne fournit pas de moyen d'échanger la taille maximale de la fenêtre de réception, que ce soit en octets ou en paquets. Il n'y a qu'une simple indication d'étranglement/désétranglement indiquant que le tampon de réception est plein. Chaque point de terminaison doit maintenir sa propre estimation de la fenêtre de réception de l'extrémité distante, soit en octets soit en paquets. Notez qu'un tampon de réception peut déborder à n'importe quelle taille de fenêtre si l'application cliente est lente à vider le tampon.

La taille maximale par défaut de la fenêtre de transmission et de réception dans l'implémentation Java est de 128 paquets. Les implémentations définissant une taille maximale de fenêtre de transmission supérieure à 128 doivent considérer les problèmes suivants :

- Les réponses CHOKE des routeurs Java dues à un débordement de tampon de réception sont beaucoup plus probables.
- L'estimation de la taille du tampon du récepteur distant doit être implémentée pour atténuer les débordements répétés (voir ci-dessus)
- CHOKE doit être géré correctement (voir ci-dessous)
- Les tailles de fenêtre maximales supérieures à 256 sont encore plus sujettes aux erreurs, car la longueur du champ d'option de comptage nack est d'un octet, limitant le maximum de NACKs à 255. Cette spécification n'aborde pas ce qu'il faut faire s'il y a plus de 255 NACKs. Les tailles de fenêtre maximales supérieures à 256 ne sont pas recommandées.

La taille de tampon minimale recommandée pour les implémentations de récepteur est de 128 paquets ou 232 KB (approximativement 128 * 1812). En raison de la latence du réseau I2P, des pertes de paquets et du contrôle de congestion qui en résulte, un tampon de cette taille est rarement rempli. Un débordement est cependant beaucoup plus susceptible de se produire sur des connexions "local loopback" (même router) à haut débit ou lors de tests locaux.

Pour indiquer rapidement et récupérer en douceur des conditions de débordement, il existe un mécanisme simple de contre-pression dans le protocole de streaming. Si un paquet est reçu avec un champ de délai optionnel d'une valeur de 60001 ou plus, cela indique un "étranglement" ou une fenêtre de réception de zéro. Un paquet avec un champ de délai optionnel d'une valeur de 60000 ou moins indique un "dés-étranglement". Les paquets sans champ de délai optionnel n'affectent pas l'état d'étranglement/dés-étranglement.

Après avoir été bloqué, aucun paquet supplémentaire contenant des données ne devrait être envoyé jusqu'à ce que l'émetteur soit débloqué, à l'exception de paquets de données "sonde" occasionnels pour compenser d'éventuels paquets de déblocage perdus. Le point de terminaison bloqué devrait démarrer un "minuteur de persistance" pour contrôler le sondage, comme dans TCP. Le point de terminaison qui débloque devrait envoyer plusieurs paquets avec ce champ défini, ou continuer à les envoyer périodiquement jusqu'à ce que des paquets de données soient à nouveau reçus. Le temps maximum d'attente pour le déblocage dépend de l'implémentation. La taille de la fenêtre de l'émetteur et la stratégie de contrôle de congestion après déblocage dépendent de l'implémentation.

### Contrôle de congestion {#congestion}

La bibliothèque de streaming utilise les phases standard de démarrage lent (croissance exponentielle de la fenêtre) et d'évitement de congestion (croissance linéaire de la fenêtre), avec un backoff exponentiel. Le fenêtrage et les accusés de réception utilisent le nombre de paquets, pas le nombre d'octets.

### Fermer {#close}

Tout paquet, y compris un avec le flag SYNCHRONIZE défini, peut également avoir le flag CLOSE envoyé. La connexion n'est pas fermée tant que le pair ne répond pas avec le flag CLOSE. Les paquets CLOSE peuvent également contenir des données.

### Ping / Pong {#ping}

Il n'y a pas de fonction ping au niveau de la couche I2CP (équivalent à l'écho ICMP) ou dans les datagrammes. Cette fonction est fournie dans le streaming. Les pings et pongs ne peuvent pas être combinés avec un paquet de streaming standard ; si l'option ECHO est définie, alors la plupart des autres drapeaux, options, ackThrough, sequenceNum, NACKs, etc. sont ignorés.

Un paquet ping doit avoir les drapeaux ECHO, SIGNATURE_INCLUDED et FROM_INCLUDED définis. Le sendStreamId doit être supérieur à zéro, et le receiveStreamId est ignoré. Le sendStreamId peut ou non correspondre à une connexion existante.

Un paquet pong doit avoir le flag ECHO défini. Le sendStreamId doit être zéro, et le receiveStreamId est le sendStreamId du ping. Avant la version 0.9.18, le paquet pong n'inclut aucune charge utile qui était contenue dans le ping.

À partir de la version 0.9.18, les pings et pongs peuvent contenir une charge utile. La charge utile du ping, jusqu'à un maximum de 32 octets, est retournée dans le pong.

Le streaming peut être configuré pour désactiver l'envoi de pongs avec la configuration i2p.streaming.answerPings=false.

### Notes sur i2p.streaming.profile {#profile}

Cette option supporte deux valeurs ; 1=bulk et 2=interactive. L'option fournit une indication à la bibliothèque de streaming et/ou au router concernant le modèle de trafic attendu.

"Bulk" signifie optimiser pour une bande passante élevée, possiblement au détriment de la latence. C'est la valeur par défaut. "Interactive" signifie optimiser pour une faible latence, possiblement au détriment de la bande passante ou de l'efficacité. Les stratégies d'optimisation, le cas échéant, dépendent de l'implémentation et peuvent inclure des modifications en dehors du protocole de streaming.

Jusqu'à la version API 0.9.63, Java I2P retournait une erreur pour toute valeur autre que 1 (bulk) et le tunnel échouait au démarrage. À partir de l'API 0.9.64, Java I2P ignore la valeur. Jusqu'à la version API 0.9.63, i2pd ignorait cette option ; elle est implémentée dans i2pd à partir de l'API 0.9.64.

Bien que le protocole de streaming inclue un champ de flag pour transmettre le paramètre de profil à l'autre extrémité, ceci n'est implémenté dans aucun router connu.

### Partage de blocs de contrôle {#sharing}

La bibliothèque de streaming prend en charge le partage de "TCP" Control Block. Cela partage trois paramètres importants de la bibliothèque de streaming (taille de fenêtre, temps d'aller-retour, variance du temps d'aller-retour) entre les connexions vers le même pair distant. Ceci est utilisé pour le partage "temporel" au moment de l'ouverture/fermeture de connexion, pas pour le partage "d'ensemble" pendant une connexion (Voir [RFC 2140](http://www.ietf.org/rfc/rfc2140.txt)). Il y a un partage séparé par ConnectionManager (c'est-à-dire par Destination locale) afin qu'il n'y ait pas de fuite d'informations vers d'autres Destinations sur le même router. Les données de partage pour un pair donné expirent après quelques minutes. Les paramètres de partage Control Block suivants peuvent être définis par router :

- RTT_DAMPENING = 0.75
- RTTDEV_DAMPENING = 0.75
- WINDOW_DAMPENING = 0.75

### Autres paramètres {#other}

Les paramètres suivants sont les valeurs par défaut recommandées. Les valeurs par défaut peuvent varier selon l'implémentation :

- MIN_RESEND_DELAY = 100 ms (RTO minimum)
- MAX_RESEND_DELAY = 45 sec (RTO maximum)
- MIN_WINDOW_SIZE = 1
- MAX_WINDOW_SIZE = 128
- TREND_COUNT = 3
- MIN_MESSAGE_SIZE = 512 (MTU minimum)
- INBOUND_BUFFER_SIZE = maxMessageSize * (maxWindowSize + 2)
- INITIAL_TIMEOUT (valide uniquement avant l'échantillonnage du RTT) = 9 sec
- "alpha" (facteur d'amortissement RTT selon RFC 6298) = 0.125
- "beta" (facteur d'amortissement RTTDEV selon RFC 6298) = 0.25
- "K" (multiplicateur RTDEV selon RFC 6298) = 4
- PASSIVE_FLUSH_DELAY = 175 ms
- Estimation RTT maximale : 60 sec

### Historique {#history}

La bibliothèque de streaming a évolué de manière organique pour I2P - d'abord mihi a implémenté la "mini bibliothèque de streaming" dans le cadre d'I2PTunnel, qui était limitée à une taille de fenêtre d'1 message (nécessitant un ACK avant d'envoyer le suivant), puis elle a été refactorisée en une interface de streaming générique (imitant les sockets TCP) et l'implémentation complète de streaming a été déployée avec un protocole de fenêtre glissante et des optimisations pour tenir compte du produit bande passante x délai élevé. Les flux individuels peuvent ajuster la taille maximale des paquets et d'autres options. La taille de message par défaut est sélectionnée pour s'adapter précisément dans deux messages tunnel I2NP de 1K, et représente un compromis raisonnable entre les coûts de bande passante de la retransmission des messages perdus, et la latence et la surcharge de messages multiples.

## Travaux futurs {#future}

Le comportement de la bibliothèque de streaming a un impact profond sur les performances au niveau applicatif, et constitue donc un domaine important pour des analyses plus approfondies.

- Un réglage supplémentaire des paramètres de la bibliothèque streaming lib pourrait être nécessaire.
- Un autre domaine de recherche est l'interaction de la streaming lib avec les couches de transport NTCP et SSU. Voir [la page de discussion NTCP](/docs/historical/ntcp-discussion) pour plus de détails.
- L'interaction des algorithmes de routage avec la streaming lib affecte fortement les performances. En particulier, la distribution aléatoire des messages vers plusieurs tunnels dans un pool conduit à un degré élevé de livraison désordonnée qui résulte en des tailles de fenêtre plus petites que ce ne serait autrement le cas. Le router route actuellement les messages pour une paire de destination unique depuis/vers à travers un ensemble cohérent de tunnels, jusqu'à l'expiration du tunnel ou l'échec de livraison. Les algorithmes d'échec et de sélection de tunnel du router devraient être révisés pour d'éventuelles améliorations.
- Les données dans le premier paquet SYN peuvent dépasser le MTU du récepteur.
- Le champ DELAY_REQUESTED pourrait être utilisé davantage.
- Les paquets SYNCHRONIZE initiaux dupliqués sur les flux de courte durée peuvent ne pas être reconnus et supprimés.
- N'envoyez pas le MTU dans une retransmission.
- Les données sont envoyées à moins que la fenêtre sortante soit pleine. (c'est-à-dire no-Nagle ou TCP_NODELAY) Il devrait probablement y avoir une option de configuration pour cela.
- zzz a ajouté du code de débogage à la bibliothèque streaming library pour enregistrer les paquets dans un format compatible wireshark (pcap) ; Utilisez ceci pour analyser davantage les performances. Le format pourrait nécessiter une amélioration pour mapper plus de paramètres de streaming lib aux champs TCP.
- Il y a des propositions pour remplacer la streaming lib par du TCP standard (ou peut-être une couche null avec des sockets bruts). Cela serait malheureusement incompatible avec la streaming lib mais il serait bien de comparer les performances des deux.
