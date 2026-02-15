---
title: "Trackers UDP"
description: "Spécification du protocole pour les annonces UDP BitTorrent dans I2P"
slug: "udp-announces"
aliases:
  - "/fr/docs/specs/udp-bittorrent-announces"
  - "/fr/docs/specs/udp-bittorrent-announces/"
category: "Protocoles"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

## Aperçu

Cette spécification documente le protocole pour les annonces bittorrent UDP dans I2P. Pour la spécification globale de bittorrent dans I2P, voir [BitTorrent over I2P](/docs/applications/bittorrent). Pour le contexte et des informations supplémentaires sur le développement de cette spécification, voir [Proposal 160](/proposals/160-udp-trackers).

## Conception

Cette proposition utilise repliable datagram2, repliable datagram3, et raw datagrams, tels que définis dans [Datagrams](/docs/specs/datagrams). Datagram2 et Datagram3 sont de nouvelles variantes de repliable datagrams, définies dans la [Proposition 163](/proposals/163-datagram2-datagram3). Datagram2 ajoute une résistance aux attaques par rejeu et la prise en charge des signatures hors ligne. Datagram3 est plus petit que l'ancien format datagram, mais sans authentification.

### BEP 15

Pour référence, le flux de messages défini dans [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) est le suivant :

```
Client                        Tracker
    Connect Req. ------------->
      <-------------- Connect Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
```
La phase de connexion est nécessaire pour empêcher l'usurpation d'adresse IP. Le tracker renvoie un ID de connexion que le client utilise dans les annonces suivantes. Cet ID de connexion expire par défaut en une minute côté client, et en deux minutes côté tracker.

I2P utilisera le même flux de messages que BEP 15, pour faciliter l'adoption dans les bases de code client existantes compatibles UDP : pour des raisons d'efficacité et de sécurité discutées ci-dessous :

```
Client                        Tracker
    Connect Req. ------------->       (Repliable Datagram2)
      <-------------- Connect Resp.   (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
             ...
```
Cela offre potentiellement d'importantes économies de bande passante par rapport aux annonces en streaming (TCP). Bien que le Datagram2 soit à peu près de la même taille qu'un SYN de streaming, la réponse brute est beaucoup plus petite que le SYN ACK de streaming. Les requêtes suivantes utilisent Datagram3, et les réponses suivantes sont brutes.

Les requêtes d'annonce sont des Datagram3 de sorte que le tracker n'ait pas besoin de maintenir une grande table de correspondance des ID de connexion vers la destination d'annonce ou le hash. Au lieu de cela, le tracker peut générer des ID de connexion de manière cryptographique à partir du hash de l'expéditeur, de l'horodatage actuel (basé sur un certain intervalle), et d'une valeur secrète. Lorsqu'une requête d'annonce est reçue, le tracker valide l'ID de connexion, puis utilise le hash de l'expéditeur Datagram3 comme cible d'envoi.

### Durée de vie de la connexion

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html) spécifie que l'ID de connexion expire en une minute côté client, et en deux minutes côté tracker. Ce n'est pas configurable. Cela limite les gains d'efficacité potentiels, à moins que les clients ne regroupent les annonces pour toutes les faire dans une fenêtre d'une minute. i2psnark ne regroupe actuellement pas les annonces ; il les étale pour éviter les pics de trafic. Il est rapporté que les utilisateurs avancés font tourner des milliers de torrents à la fois, et faire un pic de tant d'annonces en une minute n'est pas réaliste.

Ici, nous proposons d'étendre la réponse de connexion pour ajouter un champ optionnel de durée de vie de connexion. La valeur par défaut, si elle n'est pas présente, est d'une minute. Sinon, la durée de vie spécifiée en secondes devra être utilisée par le client, et le tracker maintiendra l'ID de connexion pendant une minute supplémentaire.

### Compatibilité avec BEP 15

Cette conception maintient la compatibilité avec [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) autant que possible pour limiter les changements requis dans les clients et trackers existants.

Le seul changement requis est le format des informations de peer dans la réponse d'annonce. L'ajout du champ lifetime dans la réponse de connexion n'est pas obligatoire mais est fortement recommandé pour l'efficacité, comme expliqué ci-dessus.

### Analyse de Sécurité

Un objectif important d'un protocole d'annonce UDP est d'empêcher l'usurpation d'adresse. Le client doit réellement exister et regrouper un vrai leaseSet. Il doit avoir des tunnels entrants pour recevoir la réponse de connexion. Ces tunnels pourraient être à zéro saut et construits instantanément, mais cela exposerait le créateur. Ce protocole atteint cet objectif.

### Problèmes

- Ce protocole ne prend pas en charge les destinations masquées, mais peut être étendu pour le faire. Voir ci-dessous.

## Spécification

### Protocoles et Ports

Repliable Datagram2 utilise le protocole I2CP 19 ; repliable Datagram3 utilise le protocole I2CP 20 ; les datagrammes bruts utilisent le protocole I2CP 18. Les requêtes peuvent être Datagram2 ou Datagram3. Les réponses sont toujours brutes. L'ancien format de datagramme repliable ("Datagram1") utilisant le protocole I2CP 17 ne doit PAS être utilisé pour les requêtes ou les réponses ; ceux-ci doivent être abandonnés s'ils sont reçus sur les ports de requête/réponse. Notez que le protocole Datagram1 17 est toujours utilisé pour le protocole DHT.

Les requêtes utilisent le "to port" I2CP de l'URL d'annonce ; voir ci-dessous. Le "from port" de la requête est choisi par le client, mais doit être non-nul et différent des ports utilisés par DHT, afin que les réponses puissent être facilement classifiées. Les trackers doivent rejeter les requêtes reçues sur le mauvais port.

Les réponses utilisent le "to port" I2CP de la requête. Le "from port" de la requête est le "to port" de la requête.

### URL d'annonce

Le format d'URL d'annonce n'est pas spécifié dans [BEP 15](http://www.bittorrent.org/beps/bep_0015.html), mais comme sur le clearnet, les URL d'annonce UDP sont de la forme `udp://host:port/path`. Le chemin est ignoré et peut être vide, mais est typiquement `/announce` sur le clearnet. La partie `:port` devrait toujours être présente, cependant, si la partie `:port` est omise, utilisez un port I2CP par défaut de 6969, car c'est le port commun sur le clearnet. Il peut également y avoir des paramètres cgi `&a=b&c=d` ajoutés, ceux-ci peuvent être traités et fournis dans la requête d'annonce, voir [BEP 41](http://www.bittorrent.org/beps/bep_0041.html). S'il n'y a pas de paramètres ou de chemin, le `/` final peut également être omis, comme sous-entendu dans [BEP 41](http://www.bittorrent.org/beps/bep_0041.html).

### Formats de datagramme

Toutes les valeurs sont envoyées dans l'ordre des octets réseau (big endian). Ne vous attendez pas à ce que les paquets aient exactement une taille donnée. Les extensions futures pourraient augmenter la taille des paquets.

#### Demande de connexion

Client vers tracker. 16 octets. Doit être un Datagram2 avec réponse possible. Identique à [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Aucun changement.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">protocol_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0x41727101980 // magic constant</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
#### Réponse de Connexion

Tracker vers client. 16 ou 18 octets. Doit être brut. Identique à [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) sauf indication contraire ci-dessous.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">lifetime</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // Change from BEP 15</td>
    </tr>
  </tbody>
</table>
La réponse DOIT être envoyée vers le "port de destination" I2CP qui a été reçu comme "port source" de la requête.

Le champ lifetime est optionnel et indique la durée de vie du connection_id client en secondes. La valeur par défaut est 60, et le minimum s'il est spécifié est 60. Le maximum est 65535 ou environ 18 heures. Le tracker doit maintenir le connection_id pendant 60 secondes de plus que la durée de vie du client.

#### Demande d'annonce

Client vers tracker. 98 octets minimum. Doit être un Datagram3 auquel on peut répondre. Identique à [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) sauf indication contraire ci-dessous.

Le connection_id est tel que reçu dans la réponse de connexion.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">info_hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">peer_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">56</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">downloaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">left</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">uploaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">80</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">event</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // 0: none; 1: completed; 2: started; 3: stopped</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">84</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">IP address</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // default, unused in I2P</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">88</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">92</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">num_want</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1 // default</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">port</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// must be same as I2CP from port</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">98</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">options</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // As specified in BEP 41</td>
    </tr>
  </tbody>
</table>
Modifications par rapport à [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) :

- la clé est ignorée
- l'adresse IP n'est pas utilisée
- le port est probablement ignoré mais doit être identique au port I2CP from
- La section des options, si présente, est définie comme dans [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)

La réponse DOIT être envoyée au "port de destination" I2CP qui a été reçu comme "port source" de la requête. N'utilisez pas le port de la requête d'annonce.

#### Réponse d'annonce

Tracker vers client. 20 octets minimum. Doit être brut. Identique à [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) sauf mention contraire ci-dessous.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">interval</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">leechers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">seeders</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32 * n 32-byte hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">binary hashes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// Change from BEP 15</td>
    </tr>
  </tbody>
</table>
Modifications par rapport à [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) :

- Au lieu de 6 octets IPv4+port ou 18 octets IPv6+port, nous retournons un multiple de "réponses compactes" de 32 octets avec les hachages de pairs binaires SHA-256. Comme avec les réponses compactes TCP, nous n'incluons pas de port.

La réponse DOIT être envoyée au "port de destination" I2CP qui a été reçu comme "port source" de la requête. N'utilisez pas le port de la requête d'annonce.

Les datagrammes I2P ont une taille maximale très importante d'environ 64 Ko ; cependant, pour une livraison fiable, les datagrammes de plus de 4 Ko devraient être évités. Pour l'efficacité de la bande passante, les trackers devraient probablement limiter le nombre maximum de pairs à environ 50, ce qui correspond à un paquet d'environ 1600 octets avant les surcharges aux différentes couches, et devrait rester dans la limite de charge utile de deux messages de tunnel après fragmentation.

Comme dans BEP 15, il n'y a pas de compteur inclus du nombre d'adresses de pairs (IP/port pour BEP 15, hashes ici) à suivre. Bien que ce ne soit pas envisagé dans BEP 15, un marqueur de fin de pairs composé uniquement de zéros pourrait être défini pour indiquer que les informations de pairs sont complètes et que certaines données d'extension suivent.

Afin que cette extension soit possible à l'avenir, les clients doivent ignorer un hash de 32 octets composé uniquement de zéros, ainsi que toutes les données qui suivent. Les trackers doivent rejeter les annonces provenant d'un hash composé uniquement de zéros, bien que ce hash soit déjà banni par les routeurs Java.

#### Scrape

La requête/réponse scrape de [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) n'est pas requise par cette spécification, mais peut être implémentée si désirée, aucune modification requise. Le client doit d'abord acquérir un ID de connexion. La requête scrape est toujours un Datagram3 avec réponse possible. La réponse scrape est toujours brute.

#### Réponse d'erreur

Tracker vers client. 8 octets minimum (si le message est vide). Doit être brut. Identique à [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Aucun changement.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3 // error</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">message</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
## Extensions

Les bits d'extension ou un champ de version ne sont pas inclus. Les clients et trackers ne doivent pas supposer que les paquets ont une taille particulière. De cette façon, des champs supplémentaires peuvent être ajoutés sans casser la compatibilité. Le format d'extensions défini dans [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) est recommandé si nécessaire.

La réponse de connexion est modifiée pour ajouter une durée de vie optionnelle de l'ID de connexion.

Si la prise en charge des destinations aveugles est requise, nous pouvons soit ajouter l'adresse aveugle de 35 octets à la fin de la requête d'annonce, soit demander des hachages aveugles dans les réponses, en utilisant le format [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) (paramètres à déterminer). L'ensemble des adresses de pairs aveugles de 35 octets pourrait être ajouté à la fin de la réponse d'annonce, après un hachage de 32 octets composé uniquement de zéros.

## Directives d'implémentation

Voir la section conception ci-dessus pour une discussion des défis concernant les clients et trackers non-intégrés et non-I2CP.

### Clients

Pour un nom d'hôte de tracker donné, un client devrait privilégier les URLs UDP par rapport aux URLs HTTP, et ne devrait pas s'annoncer aux deux.

Les clients avec un support BEP 15 existant ne devraient nécessiter que de petites modifications.

Si un client prend en charge DHT ou d'autres protocoles de datagrammes, il devrait probablement sélectionner un port différent comme "port source" de la requête afin que les réponses reviennent sur ce port et ne soient pas mélangées avec les messages DHT. Le client ne reçoit que des datagrammes bruts comme réponses. Les trackers n'enverront jamais de datagramme2 avec possibilité de réponse au client.

Les clients avec une liste par défaut d'opentrackers devraient mettre à jour la liste pour ajouter des URLs UDP après que les opentrackers connus soient confirmés comme supportant UDP.

Les clients peuvent ou non implémenter la retransmission des requêtes. Les retransmissions, si elles sont implémentées, devraient utiliser un délai d'attente initial d'au moins 15 secondes, et doubler le délai d'attente pour chaque retransmission (backoff exponentiel).

Les clients doivent reculer après avoir reçu une réponse d'erreur.

### Trackers

Les trackers avec un support BEP 15 existant ne devraient nécessiter que de petites modifications. Cette spécification diffère de la proposition de 2014, en ce que le tracker doit prendre en charge la réception de datagram2 et datagram3 avec réponse sur le même port.

Pour minimiser les exigences de ressources du tracker, ce protocole est conçu pour éliminer toute exigence que le tracker stocke les correspondances entre les hachages des clients et les ID de connexion pour une validation ultérieure. Ceci est possible parce que le paquet de requête d'annonce est un paquet Datagram3 avec possibilité de réponse, il contient donc le hachage de l'expéditeur.

Une implémentation recommandée est :

- Définir l'époque actuelle comme le temps actuel avec une résolution de la durée de vie de la connexion, `epoch = now / lifetime`.
- Définir une fonction de hachage cryptographique `H(secret, clienthash, epoch)` qui génère une sortie de 8 octets.
- Générer la constante aléatoire secrète utilisée pour toutes les connexions.
- Pour les réponses de connexion, générer `connection_id = H(secret, clienthash, epoch)`
- Pour les requêtes d'annonce, valider l'ID de connexion reçu dans l'époque actuelle en vérifiant `connection_id == H(secret, clienthash, epoch) || connection_id == H(secret, clienthash, epoch - 1)`

## Références

- **[BEP15]** [BEP 15 - Protocole de Tracker UDP](http://www.bittorrent.org/beps/bep_0015.html)
- **[BEP41]** [BEP 41 - Extensions du Protocole de Tracker UDP](http://www.bittorrent.org/beps/bep_0041.html)
- **[DATAGRAMS]** [Spécification des Datagrammes](/docs/specs/datagrams)
- **[Prop160]** [Proposition 160 - Trackers UDP](/proposals/160-udp-trackers)
- **[Prop163]** [Proposition 163 - Datagram2/Datagram3](/proposals/163-datagram2-datagram3)
- **[SAMv3]** [API SAM v3](/docs/api/samv3)
- **[SPEC]** [BitTorrent sur I2P](/docs/applications/bittorrent)
