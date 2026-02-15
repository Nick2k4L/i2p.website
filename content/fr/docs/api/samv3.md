---
title: "SAM V3"
description: "Protocole de messagerie anonyme simple pour les applications I2P non-Java"
slug: "samv3"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

SAM est un protocole client simple pour interagir avec I2P. SAM est le protocole recommandé pour que les applications non-Java se connectent au réseau I2P, et il est pris en charge par plusieurs implémentations de router. Les applications Java devraient utiliser directement les API streaming ou I2CP.

SAMv3 a été introduit dans la version 0.7.3 d'I2P (mai 2009) et constitue une interface stable et supportée. La version 3.1 est également stable et prend en charge l'option de type de signature, ce qui est fortement recommandé. Les versions 3.x plus récentes supportent des fonctionnalités avancées. Notez qu'i2pd ne supporte actuellement pas la plupart des fonctionnalités 3.2 et 3.3.

Alternatives : [SOCKS](/docs/api/socks), [Streaming](/docs/api/streaming), [I2CP](/docs/protocol/i2cp), [BOB (obsolète)](/docs/api/bob). Versions obsolètes : [SAM V1](/docs/api/sam), [SAM V2](/docs/api/samv2).

## Bibliothèques SAM connues

Avertissement : Certains d'entre eux peuvent être très anciens ou non pris en charge. Aucun n'est testé, examiné ou maintenu par le projet I2P sauf indication contraire ci-dessous. Faites vos propres recherches.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Library Name</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Language</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">Version</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">STREAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">DGRAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">RAW</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Site</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2psam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++, C wrapper</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2psam">github.com/i2p/i2psam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">gosam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/goSam">github.com/eyedeekay/goSam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">sam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/sam3">github.com/eyedeekay/sam3</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">onramp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/onramp">github.com/eyedeekay/onramp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">txi2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/str4d/txi2p">github.com/str4d/txi2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.socket</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/majestrate/i2p.socket">github.com/majestrate/i2p.socket</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/l-n-s/i2plib">github.com/l-n-s/i2plib</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib-fork</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://codeberg.org/weko/i2plib-fork">codeberg.org/weko/i2plib-fork</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Py2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://i2pgit.org/robin/Py2p">i2pgit.org/robin/Py2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-rs</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2p-rs">github.com/i2p/i2p-rs</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">libsam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/libsam3">github.com/i2p/libsam3</a><br>(Maintained by the I2P project)</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">mooni2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Lua</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">notabug.org/villain/mooni2p</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">haskell-network-anonymous-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Haskell</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/solatis/haskell-network-anonymous-i2p">github.com/solatis/haskell-network-anonymous-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-sam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Javascript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://codeberg.org/diva.exchange/i2p-sam">codeberg.org/diva.exchange/i2p-sam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">node-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Javascript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/redhog/node-i2p">github.com/redhog/node-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Jsam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">github.com/eyedeekay/Jsam</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">I2PSharp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/MohA39/I2PSharp">github.com/MohA39/I2PSharp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2pdotnet</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/SamuelFisher/i2pdotnet">github.com/SamuelFisher/i2pdotnet</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.rb</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Ruby</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/dryruby/i2p.rb">github.com/dryruby/i2p.rb</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">solitude</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/syvita/solitude">github.com/syvita/solitude</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Samty</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">notabug.org/acetone/samty</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">bitcoin</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/bitcoin/bitcoin/blob/master/src/i2p.cpp">source (not a library, but good reference code)</a></td>
    </tr>
  </tbody>
</table>
## Démarrage rapide

Pour implémenter une application peer-to-peer basique utilisant uniquement TCP, le client doit prendre en charge les commandes suivantes :

- `HELLO VERSION MIN=3.1 MAX=3.1` - Nécessaire pour toutes les commandes suivantes
- `DEST GENERATE SIGNATURE_TYPE=7` - Pour générer notre clé privée et destination
- `NAMING LOOKUP NAME=...` - Pour convertir les adresses .i2p en destinations
- `SESSION CREATE STYLE=STREAM ID=... DESTINATION=... i2cp.leaseSetEncType=4,0` - Nécessaire pour STREAM CONNECT et STREAM ACCEPT
- `STREAM CONNECT ID=... DESTINATION=...` - Pour établir des connexions sortantes
- `STREAM ACCEPT ID=...` - Pour accepter les connexions entrantes

## Guide général pour les développeurs

### Conception d'Application

Les sessions SAM (ou à l'intérieur d'I2P, les pools de tunnels ou ensembles de tunnels) sont conçues pour être durables. La plupart des applications n'auront besoin que d'une seule session, créée au démarrage et fermée à la sortie. I2P est différent de Tor, où les circuits peuvent être rapidement créés et supprimés. Réfléchissez bien et consultez les développeurs I2P avant de concevoir votre application pour utiliser plus d'une ou deux sessions simultanées, ou pour les créer et les supprimer rapidement. La plupart des modèles de menace ne nécessiteront pas une session unique pour chaque connexion.

De plus, veuillez vous assurer que les paramètres de votre application (et les conseils donnés aux utilisateurs concernant les paramètres du router, ou les valeurs par défaut du router si vous intégrez un router) permettront à vos utilisateurs de contribuer plus de ressources au réseau qu'ils n'en consomment. I2P est un réseau pair-à-pair, et le réseau ne peut survivre si une application populaire pousse le réseau vers une congestion permanente.

### Compatibilité et Tests

Les implémentations des routeurs Java I2P et i2pd sont indépendantes et présentent des différences mineures dans le comportement, la prise en charge des fonctionnalités et les paramètres par défaut. Veuillez tester votre application avec la dernière version des deux routeurs.

SAM d'i2pd est activé par défaut ; SAM de Java I2P ne l'est pas. Fournissez des instructions à vos utilisateurs sur comment activer SAM dans Java I2P (via /configclients dans la console du router), et/ou fournissez un bon message d'erreur à l'utilisateur si la connexion initiale échoue, par exemple "assurez-vous qu'I2P fonctionne et que l'interface SAM est activée".

Les routers Java I2P et i2pd ont des valeurs par défaut différentes pour les quantités de tunnel. La valeur par défaut Java est 2 et celle d'i2pd est 5. Pour la plupart des bandes passantes faibles à moyennes et des nombres de connexions faibles à moyens, 2 ou 3 est suffisant. Veuillez spécifier la quantité de tunnel dans le message SESSION CREATE pour obtenir des performances cohérentes avec les routers Java I2P et i2pd. Voir ci-dessous.

Pour plus de conseils aux développeurs sur la façon de s'assurer que votre application utilise uniquement les ressources dont elle a besoin, veuillez consulter [notre guide pour intégrer I2P dans votre application](/docs/applications/embedding).

### Types de signature et de chiffrement

I2P prend en charge plusieurs types de signature et de chiffrement. Pour la compatibilité descendante, SAM utilise par défaut des types anciens et inefficaces, donc tous les clients devraient spécifier des types plus récents.

Le type de signature est spécifié dans les commandes DEST GENERATE et SESSION CREATE (pour les sessions transitoires). Tous les clients doivent définir `SIGNATURE_TYPE=7` (Ed25519).

Le type de chiffrement est spécifié dans la commande SESSION CREATE. Plusieurs types de chiffrement sont autorisés. Les clients devraient définir soit `i2cp.leaseSetEncType=4` (pour ECIES-X25519 uniquement) ou `i2cp.leaseSetEncType=4,0` (pour ECIES-X25519 et ElGamal, si la compatibilité est requise).

## Changements de la version 3

### Changements de la version 3.0

La version 3.0 a été introduite dans la version 0.7.3 d'I2P. SAMv2 offrait un moyen de gérer plusieurs sockets sur la même destination I2P *en parallèle*, c'est-à-dire que le client n'avait pas à attendre que les données soient envoyées avec succès sur un socket avant d'envoyer des données sur un autre socket. Mais toutes les données transitaient par le même socket client-vers-SAM, ce qui était assez compliqué à gérer pour le client.

SAM v3 gère les sockets d'une manière différente : chaque *socket I2P* correspond à un socket client-vers-SAM unique, ce qui est beaucoup plus simple à gérer. Cela ressemble à [BOB](/docs/api/bob).

SAMv3 offre également un port UDP pour envoyer des datagrammes à travers I2P, et peut retransmettre les datagrammes I2P vers le serveur de datagrammes du client.

### Modifications de la version 3.1

La version 3.1 a été introduite dans la version Java I2P 0.9.14 (juillet 2014). SAM 3.1 est l'implémentation SAM minimale recommandée en raison de sa prise en charge de meilleurs types de signature que SAM 3.0. i2pd prend également en charge la plupart des fonctionnalités 3.1.

- DEST GENERATE et SESSION CREATE prennent désormais en charge un paramètre SIGNATURE_TYPE.
- Les paramètres MIN et MAX dans HELLO VERSION sont maintenant optionnels.
- Les paramètres MIN et MAX dans HELLO VERSION prennent maintenant en charge les versions à un chiffre telles que "3".
- RAW SEND est maintenant pris en charge sur le socket bridge.

### Changements de la version 3.2

La version 3.2 a été introduite dans la version 0.9.24 de Java I2P (janvier 2016). Notez qu'i2pd ne prend actuellement pas en charge la plupart des fonctionnalités 3.2.

#### Support du Port et Protocole I2CP

- Options SESSION CREATE FROM_PORT et TO_PORT
- Option SESSION CREATE STYLE=RAW PROTOCOL
- Options STREAM CONNECT, DATAGRAM SEND, et RAW SEND FROM_PORT et TO_PORT
- Option RAW SEND PROTOCOL
- DATAGRAM RECEIVED, RAW RECEIVED, et flux transférés ou reçus et datagrammes avec réponse possible, inclut FROM_PORT et TO_PORT
- L'option de session RAW HEADER=true fera que les datagrammes raw transférés seront précédés d'une ligne contenant PROTOCOL=nnn FROM_PORT=nnnn TO_PORT=nnnn
- La première ligne des datagrammes envoyés via le port 7655 peut maintenant commencer par n'importe quelle version 3.x
- La première ligne des datagrammes envoyés via le port 7655 peut contenir n'importe laquelle des options FROM_PORT, TO_PORT, PROTOCOL
- RAW RECEIVED inclut PROTOCOL=nnn

#### SSL et authentification

- USER/PASSWORD dans les paramètres HELLO pour l'autorisation. Voir [ci-dessous](#authorization).
- Configuration d'autorisation optionnelle avec la commande AUTH. Voir [ci-dessous](#authorization-configuration-sam-32-or-higher-optional-feature).
- Support SSL/TLS optionnel sur la socket de contrôle. Voir [ci-dessous](#ssl).
- Option STREAM FORWARD SSL=true

#### Multithreading

- Les STREAM ACCEPTs en attente simultanés sont autorisés sur le même ID de session.

#### Analyse de la ligne de commande et maintien en vie

- Commandes optionnelles QUIT, STOP et EXIT pour fermer la session et la socket. Voir [ci-dessous](#quitstopexitinvisible-sam-32-or-higher-optional-features).
- L'analyse des commandes gérera correctement l'UTF-8
- L'analyse des commandes gère de manière fiable les espaces à l'intérieur des guillemets
- Une barre oblique inverse '\\' peut échapper les guillemets sur la ligne de commande
- Il est recommandé que le serveur mappe les commandes en majuscules, pour faciliter les tests via telnet.
- Les valeurs d'option vides telles que PROTOCOL ou PROTOCOL= peuvent être autorisées, selon l'implémentation.
- PING/PONG pour le maintien en vie. Voir ci-dessous.
- Les serveurs peuvent implémenter des délais d'expiration pour HELLO ou les commandes suivantes, selon l'implémentation.

### Modifications de la version 3.3

La version 3.3 a été introduite dans la version 0.9.25 de Java I2P (mars 2016). Notez que i2pd ne prend actuellement pas en charge la plupart des fonctionnalités de la version 3.3.

- La même session peut être utilisée pour les streams, datagrammes et raw simultanément. Les paquets et streams entrants seront routés en fonction du protocole I2P et du to-port. Voir [la section PRIMARY ci-dessous](#sam-primary-sessions-v33-and-higher).
- DATAGRAM SEND et RAW SEND supportent maintenant les options SEND_TAGS, TAG_THRESHOLD, EXPIRES et SEND_LEASESET. Voir [la section d'envoi de datagrammes ci-dessous](#sending-repliable-or-raw-datagrams).

## Protocole Version 3

### Aperçu de la spécification Simple Anonymous Messaging (SAM) Version 3.3

L'application client communique avec le pont SAM, qui gère toutes les fonctionnalités I2P (en utilisant la [bibliothèque de streaming](/docs/api/streaming) pour les flux virtuels, ou [I2CP](/docs/protocol/i2cp) directement pour les datagrammes).

Par défaut, la communication entre le client et le pont SAM n'est ni chiffrée ni authentifiée. Le pont SAM peut prendre en charge les connexions SSL/TLS ; les détails de configuration et d'implémentation sont en dehors du cadre de cette spécification. À partir de SAM 3.2, des paramètres d'authentification optionnels utilisateur/mot de passe sont pris en charge lors de la négociation initiale et peuvent être requis par le pont.

Les communications I2P peuvent prendre plusieurs formes distinctes :

- [Flux virtuels](/docs/api/streaming)
- [Datagrammes répondables et authentifiés](/docs/specs/datagrams#repliable) (messages avec un champ FROM)
- [Datagrammes anonymes](/docs/specs/datagrams#raw) (messages anonymes bruts)
- [Datagram2](/docs/specs/datagrams#datagram2) (un nouveau format répondable et authentifié)
- [Datagram3](/docs/specs/datagrams#datagram3) (un nouveau format répondable mais non authentifié)

Les communications I2P sont prises en charge par les sessions I2P, et chaque session I2P est liée à une adresse (appelée destination). Une session I2P est associée à l'un des trois types ci-dessus, et ne peut pas transporter des communications d'un autre type, sauf en utilisant les [sessions PRIMARY](#sam-primary-sessions-v33-and-higher).

### Encodage et Échappement

Tous ces messages SAM sont envoyés sur une seule ligne, terminés par le caractère de nouvelle ligne (\\n). Avant SAM 3.2, seul l'ASCII 7 bits était pris en charge. À partir de SAM 3.2, l'encodage doit être UTF-8. Toutes les clés ou valeurs encodées en UTF-8 devraient fonctionner.

Le formatage présenté dans cette spécification ci-dessous est uniquement pour la lisibilité, et bien que les deux premiers mots de chaque message doivent conserver leur ordre spécifique, l'ordre des paires clé=valeur peut changer (par exemple, "ONE TWO A=B C=D" ou "ONE TWO C=D A=B" sont toutes deux des constructions parfaitement valides). De plus, le protocole est sensible à la casse. Dans ce qui suit, les exemples de messages sont précédés de "->" pour les messages envoyés par le client vers le pont SAM, et de "<-" pour les messages envoyés par le pont SAM vers le client.

La ligne de commande ou de réponse de base prend l'une des formes suivantes :

```
COMMAND SUBCOMMAND [key=value] [key=value] ...
COMMAND                                           # As of SAM 3.2
PING[ arbitrary text]                             # As of SAM 3.2
PONG[ arbitrary text]                             # As of SAM 3.2
```
COMMAND sans SUBCOMMAND est pris en charge uniquement pour certaines nouvelles commandes dans SAM 3.2.

Les paires Clé=valeur doivent être séparées par un seul espace. (À partir de SAMv3.2, plusieurs espaces sont autorisés) Les valeurs doivent être entourées de guillemets doubles si elles contiennent des espaces, par exemple key="long value text". (Avant SAMv3.2, cela ne fonctionnait pas de manière fiable dans certaines implémentations)

Avant SAM 3.2, il n'y avait aucun mécanisme d'échappement. À partir de SAM 3.2, les guillemets doubles peuvent être échappés avec une barre oblique inverse '\\' et une barre oblique inverse peut être représentée par deux barres obliques inverses '\\\\'.

### Valeurs vides

À partir de SAMv3.2, les valeurs d'option vides telles que KEY, KEY=, ou KEY="" peuvent être autorisées, selon l'implémentation.

### Sensibilité à la casse

Le protocole, tel que spécifié, est sensible à la casse. Il est recommandé mais non obligatoire que le serveur convertisse les commandes en majuscules, pour faciliter les tests via telnet. Cela permettrait, par exemple, à "hello version" de fonctionner. Ceci dépend de l'implémentation. Ne convertissez pas les clés ou valeurs en majuscules, car cela corromprait les options [I2CP](/docs/protocol/i2cp).

### Établissement de connexion SAM

Aucune communication SAM ne peut avoir lieu tant que le client et le bridge ne se sont pas mis d'accord sur une version de protocole, ce qui se fait par l'envoi d'un HELLO par le client et l'envoi d'un HELLO REPLY par le bridge :

```
->  HELLO VERSION
          [MIN=$min]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [MAX=$max]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [USER="xxx"]          # As of SAM 3.2, required if authentication is enabled, see below
          [PASSWORD="yyy"]      # As of SAM 3.2, required if authentication is enabled, see below
```
et

```
<-  HELLO REPLY RESULT=OK VERSION=3.1
```
À partir de la version 3.1 (I2P 0.9.14), les paramètres MIN et MAX sont optionnels. SAM retournera toujours la version la plus élevée possible selon les contraintes MIN et MAX, ou la version actuelle du serveur si aucune contrainte n'est donnée.

Si le pont SAM ne peut pas trouver une version appropriée, il répond avec :

```
<- HELLO REPLY RESULT=NOVERSION
```
Si une erreur s'est produite, comme un format de requête incorrect, il répond avec :

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
#### SSL

Le socket de contrôle du serveur peut optionnellement offrir un support SSL/TLS, tel que configuré sur le serveur et le client. Les implémentations peuvent également offrir d'autres couches de transport ; cela dépasse le cadre de la définition du protocole.

#### Autorisation

Pour l'autorisation, le client ajoute USER="xxx" PASSWORD="yyy" aux paramètres HELLO. Les guillemets doubles pour l'utilisateur et le mot de passe sont recommandés mais non obligatoires. Un guillemet double à l'intérieur d'un nom d'utilisateur ou d'un mot de passe doit être échappé avec une barre oblique inverse. En cas d'échec, le serveur répondra avec un I2P_ERROR et un message. Il est recommandé d'activer SSL sur tous les serveurs SAM où une autorisation est requise.

#### Délais d'expiration

Les serveurs peuvent implémenter des délais d'expiration pour la commande HELLO ou les commandes suivantes, selon l'implémentation. Les clients doivent envoyer rapidement la commande HELLO et la commande suivante après s'être connectés.

Si un délai d'expiration se produit avant que le HELLO soit reçu, le pont répond avec :

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
et se déconnecte ensuite.

Si un délai d'expiration se produit après la réception du HELLO mais avant la commande suivante, le bridge répond avec :

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
et se déconnecte ensuite.

### Ports et protocole I2CP

À partir de SAM 3.2, les ports et protocoles [I2CP](/docs/protocol/i2cp) peuvent être spécifiés par l'expéditeur client SAM pour être transmis à [I2CP](/docs/protocol/i2cp), et le pont SAM transmettra les informations de port et de protocole [I2CP](/docs/protocol/i2cp) reçues au client SAM.

Pour FROM_PORT et TO_PORT, la plage valide est 0-65535, et la valeur par défaut est 0.

Pour PROTOCOL, qui ne peut être spécifié que pour RAW, la plage valide est 0-255, et la valeur par défaut est 18.

Pour les commandes SESSION, les ports et le protocole spécifiés sont les valeurs par défaut pour cette session. Pour les flux ou datagrammes individuels, les ports et le protocole spécifiés remplacent les valeurs par défaut de la session. Pour les flux ou datagrammes reçus, les ports et le protocole indiqués sont tels que reçus depuis [I2CP](/docs/protocol/i2cp).

#### Différences importantes par rapport à l'IP standard

Les ports I2CP sont pour les sockets et datagrammes I2P. Ils ne sont pas liés à vos sockets locaux se connectant à SAM.

- Le port 0 est valide et a une signification spéciale.
- Les ports 1-1023 ne sont pas spéciaux ou privilégiés.
- Les serveurs écoutent sur le port 0 par défaut, ce qui signifie "tous les ports".
- Les clients envoient vers le port 0 par défaut, ce qui signifie "n'importe quel port".
- Les clients envoient depuis le port 0 par défaut, ce qui signifie "non spécifié".
- Les serveurs peuvent avoir un service écoutant sur le port 0 et d'autres services écoutant sur des ports plus élevés. Si c'est le cas, le service du port 0 est celui par défaut, et sera connecté si le port du socket entrant ou du datagramme ne correspond à aucun autre service.
- La plupart des destinations I2P n'ont qu'un seul service qui fonctionne sur elles, vous pouvez donc utiliser les valeurs par défaut et ignorer la configuration des ports I2CP.
- SAM 3.2 ou 3.3 est requis pour spécifier les ports I2CP.
- Si vous n'avez pas besoin des ports I2CP, vous n'avez pas besoin de SAM 3.2 ou 3.3 ; la version 3.1 est suffisante.
- Le protocole 0 est valide et signifie "n'importe quel protocole". Ceci n'est pas recommandé, et ne fonctionnera probablement pas.
- Les sockets I2P sont suivis par un ID de connexion interne. Par conséquent, il n'y a pas d'exigence que le 5-uplet dest:port:dest:port:protocol soit unique. Par exemple, il peut y avoir plusieurs sockets avec les mêmes ports entre deux destinations. Les clients n'ont pas besoin de choisir un "port libre" pour une connexion sortante.

Si vous concevez une application SAM 3.3 avec plusieurs sous-sessions, réfléchissez attentivement à la façon d'utiliser efficacement les ports et protocoles. Consultez la spécification [I2CP](/docs/protocol/i2cp) pour plus d'informations.

### Sessions SAM

Une session SAM est créée par un client qui ouvre un socket vers le pont SAM, effectue une négociation de connexion, et envoie un message SESSION CREATE, et la session se termine lorsque le socket est déconnecté.

Chaque Destination I2P enregistrée est uniquement associée à un ID de session (ou surnom). Les ID de session, y compris les ID de sous-session pour les sessions PRIMARY, doivent être globalement uniques sur le serveur SAM. Pour éviter d'éventuelles collisions d'ID avec d'autres clients, la meilleure pratique est que le client génère les ID de manière aléatoire.

Chaque session est uniquement associée à :

- le socket à partir duquel le client crée la session
- son ID (ou surnom)

#### Demande de Création de Session

Le message de création de session ne peut utiliser qu'une seule de ces formes (les messages reçus via d'autres formes reçoivent un message d'erreur en réponse) :

```
->  SESSION CREATE
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, for DESTINATION=TRANSIENT only, default DSA_SHA1
          [PORT=$port]                         # Required for DATAGRAM* RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [HEADER={true,false}]                # SAM 3.2 or higher only, for STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
DESTINATION spécifie quelle destination doit être utilisée pour envoyer et recevoir des messages/flux. Le $privkey est la base 64 de la concaténation de la [Destination](/docs/specs/common-structures#type_Destination) suivie de la [Private Key](/docs/specs/common-structures#type_PrivateKey) suivie de la [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), optionnellement suivie de la [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), qui fait 663 octets ou plus en binaire et 884 octets ou plus en base 64, selon le type de signature. Le format binaire est spécifié dans Private Key File. Voir les notes supplémentaires concernant la [Private Key](/docs/specs/common-structures#type_PrivateKey) dans la section Génération de Clé de Destination ci-dessous.

Si la clé privée de signature est composée uniquement de zéros, la section [Signature Hors-ligne](/docs/specs/common-structures#struct_OfflineSignature) suit. Les signatures hors-ligne ne sont prises en charge que pour les sessions STREAM et RAW. Les signatures hors-ligne ne peuvent pas être créées avec DESTINATION=TRANSIENT. Le format de la section de signature hors-ligne est :

1. Horodatage d'expiration (4 octets, big endian, secondes depuis l'époque, se réinitialise en 2106)
2. Type de signature de la clé publique de signature transitoire (2 octets, big endian)
3. Clé publique de signature transitoire (longueur selon le type de signature transitoire spécifié)
4. Signature des trois champs ci-dessus par la clé hors ligne (longueur selon le type de signature de destination spécifié)
5. Clé privée de signature transitoire (longueur selon le type de signature transitoire spécifié)

Si la destination est spécifiée comme TRANSIENT, le pont SAM crée une nouvelle destination. À partir de la version 3.1 (I2P 0.9.14), si la destination est TRANSIENT, un paramètre optionnel SIGNATURE_TYPE est pris en charge. La valeur SIGNATURE_TYPE peut être n'importe quel nom (par exemple ECDSA_SHA256_P256, insensible à la casse) ou numéro (par exemple 1) pris en charge par [Key Certificates](/docs/specs/common-structures#type_Certificate). La valeur par défaut est DSA_SHA1, ce qui n'est PAS ce que vous voulez. Pour la plupart des applications, veuillez spécifier SIGNATURE_TYPE=7.

$nickname est le choix du client. Aucun espace n'est autorisé.

Les options supplémentaires fournies sont transmises à la configuration de session I2P si elles ne sont pas interprétées par le pont SAM (par exemple outbound.length=0).

Les routers Java I2P et i2pd ont des valeurs par défaut différentes pour les quantités de tunnels. La valeur par défaut de Java est 2 et celle d'i2pd est 5. Pour la plupart des connexions à bande passante faible à moyenne et avec un nombre de connexions faible à moyen, 2 ou 3 sont suffisants. Veuillez spécifier les quantités de tunnels dans le message SESSION CREATE pour obtenir des performances cohérentes avec les routers Java I2P et i2pd, en utilisant les options par exemple inbound.quantity=3 outbound.quantity=3. Ces options et d'autres [sont documentées dans les liens ci-dessous](#tunnel-i2cp-and-streaming-options).

Le pont SAM lui-même devrait déjà être configuré avec le router avec lequel il doit communiquer via I2P (bien que si nécessaire, il pourrait y avoir un moyen de fournir une substitution, par exemple i2cp.tcp.host=localhost et i2cp.tcp.port=7654).

#### Réponse de création de session

Après avoir reçu le message de création de session, le pont SAM répondra avec un message de statut de session, comme suit :

Si la création a réussi :

```
<-  SESSION STATUS RESULT=OK DESTINATION=$privkey
```
Le $privkey est la base 64 de la concaténation de la [Destination](/docs/specs/common-structures#type_Destination) suivie de la [Private Key](/docs/specs/common-structures#type_PrivateKey) suivie de la [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), optionnellement suivie de la [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), qui fait 663 octets ou plus en binaire et 884 octets ou plus en base 64, selon le type de signature. Le format binaire est spécifié dans Private Key File.

Si le SESSION CREATE contenait une clé privée de signature composée uniquement de zéros et une section [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), la réponse SESSION STATUS inclura les mêmes données dans le même format. Voir la section SESSION CREATE ci-dessus pour plus de détails.

Si le pseudonyme est déjà associé à une session :

```
<-  SESSION STATUS RESULT=DUPLICATED_ID
```
Si la destination est déjà utilisée :

```
<-  SESSION STATUS RESULT=DUPLICATED_DEST
```
Si la destination n'est pas une clé de destination privée valide :

```
<-  SESSION STATUS RESULT=INVALID_KEY
```
Si une autre erreur s'est produite :

```
<-  SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
Si ce n'est pas correct, le MESSAGE devrait contenir des informations lisibles par l'utilisateur expliquant pourquoi la session n'a pas pu être créée.

Notez que le router construit les tunnels avant de répondre avec SESSION STATUS. Cela peut prendre plusieurs secondes, ou, au démarrage du router ou lors d'une congestion réseau sévère, une minute ou plus. En cas d'échec, le router ne répondra pas avec un message d'erreur pendant plusieurs minutes. Ne définissez pas un délai d'attente court pour attendre la réponse. N'abandonnez pas la session pendant que la construction du tunnel est en cours et ne réessayez pas.

Les sessions SAM vivent et meurent avec le socket auquel elles sont associées. Quand le socket est fermé, la session meurt, et toutes les communications utilisant la session meurent en même temps. Et inversement, quand la session meurt pour quelque raison que ce soit, le pont SAM ferme le socket.

### Flux virtuels SAM

Les flux virtuels sont garantis d'être envoyés de manière fiable et dans l'ordre, avec notification d'échec et de succès dès qu'elle est disponible.

Les streams sont des sockets de communication bidirectionnels entre deux destinations I2P, mais leur ouverture doit être demandée par l'une d'entre elles. Par la suite, les commandes CONNECT sont utilisées par le client SAM pour une telle demande. Les commandes FORWARD / ACCEPT sont utilisées par le client SAM quand il veut écouter les requêtes provenant d'autres destinations I2P.

### SAM Virtual Streams : CONNECT

Un client demande une connexion en :

- ouverture d'un nouveau socket avec le pont SAM
- transmission de la même négociation HELLO que ci-dessus
- envoi de la commande STREAM CONNECT

#### Demande de connexion

```
-> STREAM CONNECT
         ID=$nickname
         DESTINATION=$destination
         [SILENT={true,false}]                # default false
         [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
         [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
```
Ceci établit une nouvelle connexion virtuelle depuis la session locale dont l'ID est $nickname vers le pair spécifié.

La cible est $destination, qui est la base 64 de la [Destination](/docs/specs/common-structures#type_Destination), qui fait 516 caractères base 64 ou plus (387 octets ou plus en binaire), selon le type de signature.

**NOTE :** Depuis environ 2014 (SAM v3.1), Java I2P prend également en charge les noms d'hôte et les adresses b32 pour la $destination, mais cela n'était pas documenté auparavant. Les noms d'hôte et les adresses b32 sont maintenant officiellement pris en charge par Java I2P depuis la version 0.9.48. Le router i2pd prend en charge les noms d'hôte et les adresses b32 depuis la version 2.38.0 (0.9.50). Pour les deux routers, la prise en charge "b32" inclut la prise en charge des adresses "b33" étendues pour les destinations aveugles.

#### Réponse de connexion

Si SILENT=true est passé, le pont SAM n'émettra aucun autre message sur le socket. Si la connexion échoue, le socket sera fermé. Si la connexion réussit, toutes les données restantes passant par le socket actuel sont transmises depuis et vers le peer de destination I2P connecté.

Si SILENT=false, qui est la valeur par défaut, le pont SAM envoie un dernier message à son client avant de transférer ou de fermer le socket :

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
La valeur RESULT peut être l'une des suivantes :

```
OK
CANT_REACH_PEER
I2P_ERROR
INVALID_KEY
INVALID_ID
TIMEOUT
```
Si le RESULT est OK, toutes les données restantes transitant par le socket actuel sont transmises depuis et vers le pair de destination I2P connecté. Si la connexion n'était pas possible (timeout, etc), RESULT contiendra la valeur d'erreur appropriée (accompagnée d'un MESSAGE optionnel lisible par l'humain), et le bridge SAM ferme le socket.

Le délai d'attente de connexion du flux router en interne est d'environ une minute, selon l'implémentation. Ne définissez pas un délai d'attente plus court en attendant la réponse.

### SAM Virtual Streams : ACCEPT

Un client attend une demande de connexion entrante en :

- ouvrir un nouveau socket avec le bridge SAM
- passer la même négociation HELLO que ci-dessus
- envoyer la commande STREAM ACCEPT

#### Accepter la demande

```
-> STREAM ACCEPT
         ID=$nickname
         [SILENT={true,false}]                # default false
```
Cela fait que la session ${nickname} écoute une demande de connexion entrante depuis le réseau I2P. ACCEPT n'est pas autorisé tant qu'il y a un FORWARD actif sur la session.

À partir de SAM 3.2, plusieurs STREAM ACCEPTs en attente simultanés sont autorisés sur le même ID de session (même avec le même port). Avant la version 3.2, les accepts simultanés échouaient avec ALREADY_ACCEPTING. Note : Java I2P supporte également les ACCEPTs simultanés sur SAM 3.1, depuis la version 0.9.24 (2016-01). i2pd supporte également les ACCEPTs simultanés sur SAM 3.1, depuis la version 2.50.0 (2023-12).

#### Réponse d'acceptation

Si SILENT=true est passé, le pont SAM n'émettra aucun autre message sur la socket. Si l'acceptation échoue, la socket sera fermée. Si l'acceptation réussit, toutes les données restantes transitant par la socket actuelle sont transmises depuis et vers le pair de destination I2P connecté. Pour la fiabilité, et pour recevoir la destination des connexions entrantes, SILENT=false est recommandé.

Si SILENT=false, qui est la valeur par défaut, le pont SAM répond avec :

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
La valeur RESULT peut être l'une des suivantes :

```
OK
I2P_ERROR
INVALID_ID
```
Si le résultat n'est pas OK, la socket est fermée immédiatement par le pont SAM. Si le résultat est OK, le pont SAM commence à attendre une demande de connexion entrante d'un autre pair I2P. Quand une demande arrive, le pont SAM l'accepte et :

Si SILENT=true a été transmis, le pont SAM n'émettra aucun autre message sur la socket client. Toutes les données restantes transitant par la socket actuelle sont transmises depuis et vers le pair de destination I2P connecté.

Si SILENT=false a été passé, qui est la valeur par défaut, le pont SAM envoie au client une ligne ASCII contenant la clé de destination publique en base64 du pair demandeur, et des informations supplémentaires pour SAM 3.2 uniquement :

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Après cette ligne terminée par '\\n', toutes les données restantes passant par le socket actuel sont transmises depuis et vers le pair de destination I2P connecté, jusqu'à ce que l'un des pairs ferme le socket.

#### Erreurs après OK

Dans de rares cas, le pont SAM peut rencontrer une erreur après avoir envoyé RESULT=OK, mais avant qu'une connexion n'arrive et l'envoi de la ligne $destination au client. Ces erreurs peuvent inclure l'arrêt du router, le redémarrage du router, et la fermeture de session. Dans ces cas, lorsque SILENT=false, le pont SAM peut, mais n'est pas obligé de (dépendant de l'implémentation), envoyer la ligne :

```
<-  STREAM STATUS
         RESULT=I2P_ERROR
         [MESSAGE=...]
```
avant de fermer immédiatement le socket. Cette ligne n'est pas, bien sûr, décodable comme une destination Base 64 valide.

### Flux Virtuels SAM : FORWARD

Un client peut utiliser un serveur socket standard et attendre les demandes de connexion provenant d'I2P. Pour cela, le client doit :

- ouvrir une nouvelle socket avec le pont SAM
- passer la même négociation HELLO que ci-dessus
- envoyer la commande forward

#### Demande de transfert

```
-> STREAM FORWARD
         ID=$nickname
         PORT=$port
         [HOST=$host]
         [SILENT={true,false}]                # default false
         [SSL={true,false}]                   # SAM 3.2 or higher only, default false
```
Ceci fait que la session ${nickname} écoute les demandes de connexion entrantes du réseau I2P. FORWARD n'est pas autorisé tant qu'il y a un ACCEPT en attente sur la session.

#### Réponse de transfert

SILENT est par défaut à false. Que SILENT soit true ou false, le pont SAM répond toujours avec un message STREAM STATUS. Notez que c'est un comportement différent de STREAM ACCEPT et STREAM CONNECT quand SILENT=true. Le message STREAM STATUS est :

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
La valeur RESULT peut être l'une des suivantes :

```
OK
I2P_ERROR
INVALID_ID
```
$host est le nom d'hôte ou l'adresse IP du serveur socket vers lequel SAM transférera les demandes de connexion. Si non spécifié, SAM prend l'IP du socket qui a émis la commande de transfert.

$port est le numéro de port du serveur de socket vers lequel SAM transférera les demandes de connexion. Il est obligatoire.

Lorsqu'une demande de connexion arrive depuis I2P, le pont SAM ouvre une connexion socket vers $host:$port. Si elle est acceptée en moins de 3 secondes, SAM acceptera la connexion depuis I2P, et ensuite :

Si SILENT=true a été passé, toutes les données transitant par le socket actuel obtenu sont transmises depuis et vers le pair de destination I2P connecté.

Si SILENT=false a été passé, qui est la valeur par défaut, le pont SAM envoie sur le socket obtenu une ligne ASCII contenant la clé de destination publique en base64 du pair demandeur, et des informations supplémentaires pour SAM 3.2 uniquement :

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Après cette ligne terminée par '\\n', toutes les données restantes passant par le socket sont transmises depuis et vers le pair de destination I2P connecté, jusqu'à ce que l'un des côtés ferme le socket.

À partir de SAMv3.2, si SSL=true est spécifié, le socket de redirection utilise SSL/TLS.

Le router I2P cessera d'écouter les demandes de connexion entrantes dès que le socket de "transfert" sera fermé.

### Datagrammes SAM

SAMv3 fournit des mécanismes pour envoyer et recevoir des datagrammes via des sockets de datagrammes locaux. Certaines implémentations SAMv3 prennent également en charge l'ancienne méthode v1/v2 d'envoi/réception de datagrammes via le socket de pont SAM. Les deux sont documentées ci-dessous.

I2P prend en charge quatre types de datagrammes :

- Les datagrammes reproductibles et authentifiés sont préfixés avec la destination de l'expéditeur, et contiennent la signature de l'expéditeur, de sorte que le destinataire peut vérifier que la destination de l'expéditeur n'a pas été usurpée, et peut répondre au datagramme. Le nouveau format Datagram2 est également reproductible et authentifié.
- Le nouveau format Datagram3 est reproductible mais non authentifié. Les informations de l'expéditeur ne sont pas vérifiées.
- Les datagrammes bruts ne contiennent pas la destination de l'expéditeur ni de signature.

Les ports I2CP par défaut sont définis pour les datagrammes avec réponse et les datagrammes bruts. Le port I2CP peut être modifié pour les datagrammes bruts.

Un modèle de conception de protocole courant consiste à envoyer des datagrammes avec réponse possible vers des serveurs, avec un identifiant inclus, et le serveur répond avec un datagramme brut qui inclut cet identifiant, permettant ainsi de corréler la réponse avec la demande. Ce modèle de conception élimine la surcharge substantielle des datagrammes avec réponse possible dans les réponses. Tous les choix de protocoles et ports I2CP sont spécifiques à l'application, et les concepteurs devraient prendre ces questions en considération.

Voir aussi les notes importantes sur le MTU des datagrammes dans la section ci-dessous.

#### Envoi de datagrammes avec réponse ou bruts

Bien qu'I2P ne contienne pas intrinsèquement d'adresse FROM, pour faciliter l'utilisation, une couche supplémentaire est fournie sous forme de datagrammes avec réponse possible - des messages non ordonnés et non fiables allant jusqu'à 31744 octets qui incluent une adresse FROM (laissant jusqu'à 1 Ko pour le matériel d'en-tête). Cette adresse FROM est authentifiée en interne par SAM (en utilisant la clé de signature de la destination pour vérifier la source) et inclut une protection contre la rejeu.

La taille minimale est de 1. Pour une fiabilité de livraison optimale, la taille maximale recommandée est d'environ 11 Ko. La fiabilité est inversement proportionnelle à la taille du message, peut-être même de manière exponentielle.

Après avoir établi une session SAM avec STYLE=DATAGRAM ou STYLE=RAW, le client peut envoyer des datagrammes auxquels on peut répondre ou des datagrammes bruts via le port UDP de SAM (7655 par défaut).

La première ligne d'un datagramme envoyé via ce port doit être dans le format suivant. Tout ceci est sur une seule ligne (séparée par des espaces), affiché sur plusieurs lignes pour plus de clarté :

```
3.0                                  # As of SAM 3.2, any "3.x" is allowed. Prior to that, "3.0" is required.
$nickname
$destination
[FROM_PORT=nnn]                      # SAM 3.2 or higher only, default from session options
[TO_PORT=nnn]                        # SAM 3.2 or higher only, default from session options
[PROTOCOL=nnn]                       # SAM 3.2 or higher only, only for RAW sessions, default from session options
[SEND_TAGS=nnn]                      # SAM 3.3 or higher only, number of session tags to send
                                     # Overrides crypto.tagsToSend I2CP session option
                                     # Default is router-dependent (40 for Java router)
[TAG_THRESHOLD=nnn]                  # SAM 3.3 or higher only, low session tag threshold
                                     # Overrides crypto.lowTagThreshold I2CP session option
                                     # Default is router-dependent (30 for Java router)
[EXPIRES=nnn]                        # SAM 3.3 or higher only, expiration from now in seconds
                                     # Overrides clientMessageTimeout I2CP session option (which is in ms)
                                     # Default is router-dependent (60 for Java router)
[SEND_LEASESET={true,false}]         # SAM 3.3 or higher only, whether to send our leaseset
                                     # Overrides shouldBundleReplyInfo I2CP session option
                                     # Default is true
\n
```
- 3.0 est la version de SAM. Depuis SAM 3.2, toute version 3.x est autorisée.
- $nickname est l'identifiant de la session DATAGRAM qui sera utilisée
- La cible est $destination, qui est la base 64 de la [Destination](/docs/specs/common-structures#type_Destination), soit 516 caractères base 64 ou plus (387 octets ou plus en binaire), selon le type de signature. **NOTE :** Depuis environ 2014 (SAM v3.1), Java I2P prend également en charge les noms d'hôte et les adresses b32 pour $destination, mais cela n'était pas documenté auparavant. Les noms d'hôte et adresses b32 sont maintenant officiellement pris en charge par Java I2P depuis la version 0.9.48. Le router i2pd ne prend actuellement pas en charge les noms d'hôte et adresses b32 ; cette prise en charge pourrait être ajoutée dans une version future.
- Toutes les options sont des paramètres par datagramme qui remplacent les valeurs par défaut spécifiées dans SESSION CREATE.
- Les options de la version 3.3 SEND_TAGS, TAG_THRESHOLD, EXPIRES, et SEND_LEASESET seront transmises à [I2CP](/docs/protocol/i2cp) si pris en charge. Voir [la spécification I2CP](/docs/protocol/i2cp#msg_SendMessageExpire) pour les détails. La prise en charge par le serveur SAM est optionnelle, il ignorera ces options si elles ne sont pas prises en charge.
- cette ligne se termine par '\\n'.

La première ligne sera supprimée par SAM avant d'envoyer les données restantes du message vers la destination spécifiée.

Pour une méthode alternative d'envoi de datagrammes avec réponse possible et datagrammes bruts, voir [DATAGRAM SEND et RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### Datagrammes répondables SAM : Recevoir un datagramme

Les datagrammes reçus sont écrits par SAM sur le socket depuis lequel la session de datagrammes a été ouverte, si un PORT de transfert n'est pas spécifié dans la commande SESSION CREATE. C'est la méthode compatible v1/v2 pour recevoir les datagrammes.

Lorsqu'un datagramme arrive, le pont le livre au client via le message :

```
<-  DATAGRAM RECEIVED
           DESTINATION=$destination           # See notes below for Datagram3 format
           SIZE=$numBytes
           FROM_PORT=nnn                      # SAM 3.2 or higher only
           TO_PORT=nnn                        # SAM 3.2 or higher only
           \n
       [$numBytes of data]
```
La source est $destination, qui est le base 64 de la [Destination](/docs/specs/common-structures#type_Destination), soit 516 caractères base 64 ou plus (387 octets ou plus en binaire), selon le type de signature.

Le pont SAM n'expose jamais au client les en-têtes d'authentification ou autres champs, seulement les données que l'expéditeur a fournies. Cela continue jusqu'à ce que la session soit fermée (par le client qui interrompt la connexion).

#### Transmission de datagrammes bruts ou avec réponse possible

Lors de la création d'une session datagram, le client peut demander à SAM de transférer les messages entrants vers une adresse ip:port spécifiée. Il le fait en émettant la commande CREATE avec les options PORT et HOST :

```
-> SESSION CREATE
          STYLE={DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          PORT=$port
          [HOST=$host]
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP options
```
La $privkey est le base 64 de la concaténation de la [Destination](/docs/specs/common-structures#type_Destination) suivie de la [Private Key](/docs/specs/common-structures#type_PrivateKey) suivie de la [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), optionnellement suivie de l'[Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), ce qui représente 884 caractères base 64 ou plus (663 octets ou plus en binaire), selon le type de signature. Le format binaire est spécifié dans Private Key File.

Les signatures hors ligne sont prises en charge pour les datagrammes RAW, DATAGRAM2 et DATAGRAM3, mais pas pour DATAGRAM. Voir la section SESSION CREATE ci-dessus et la section DATAGRAM2/3 ci-dessous pour plus de détails.

$host est le nom d'hôte ou l'adresse IP du serveur de datagrammes vers lequel SAM transférera les datagrammes. S'il n'est pas fourni, SAM prend l'IP du socket qui a émis la commande de transfert.

$port est le numéro de port du serveur de datagrammes vers lequel SAM transmettra les datagrammes. Si $port n'est pas défini, les datagrammes ne seront PAS transmis, ils seront reçus sur le socket de contrôle, de manière compatible v1/v2.

Les options supplémentaires fournies sont transmises à la configuration de session I2P si elles ne sont pas interprétées par le pont SAM (par exemple outbound.length=0). Ces options [sont documentées ci-dessous](#tunnel-i2cp-and-streaming-options).

Les datagrammes transmissibles avec réponse sont toujours préfixés par la destination en base64, sauf pour Datagram3, voir ci-dessous. Lorsqu'un datagramme avec réponse arrive, le bridge envoie au host:port spécifié un paquet UDP contenant les données suivantes :

```
$destination                       # See notes below for Datagram3 format
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
$datagram_payload
```
Les datagrammes bruts transférés sont transmis tels quels vers l'hôte:port spécifié sans préfixe. Le paquet UDP contient les données suivantes :

```
$datagram_payload
```
À partir de SAM 3.2, lorsque HEADER=true est spécifié dans SESSION CREATE, le datagramme brut transféré sera préfixé avec une ligne d'en-tête comme suit :

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
La $destination est la base 64 de la [Destination](/docs/specs/common-structures#type_Destination), qui fait 516 caractères base 64 ou plus (387 octets ou plus en binaire), selon le type de signature.

#### Datagrammes Anonymes (Bruts) SAM

Exploitant au maximum la bande passante d'I2P, SAM permet aux clients d'envoyer et de recevoir des datagrammes anonymes, laissant les informations d'authentification et de réponse à la charge du client lui-même. Ces datagrammes ne sont pas fiables et non ordonnés, et peuvent faire jusqu'à 32768 octets.

La taille minimale est de 1. Pour une fiabilité de livraison optimale, la taille maximale recommandée est d'environ 11 Ko.

Après avoir établi une session SAM avec STYLE=RAW, le client peut envoyer des datagrammes anonymes à travers le pont SAM exactement de la même manière que [l'envoi de datagrammes avec réponse](#sending-repliable-or-raw-datagrams).

Les deux méthodes de réception de datagrammes sont également disponibles pour les datagrammes anonymes.

Les datagrammes reçus sont écrits par SAM sur le socket à partir duquel la session de datagramme a été ouverte, si un PORT de redirection n'est pas spécifié dans la commande SESSION CREATE. Il s'agit de la méthode compatible v1/v2 pour recevoir les datagrammes.

```
<- RAW RECEIVED
          SIZE=$numBytes
          FROM_PORT=nnn                      # SAM 3.2 or higher only
          TO_PORT=nnn                        # SAM 3.2 or higher only
          PROTOCOL=nnn                       # SAM 3.2 or higher only
          \n
      [$numBytes of data]
```
Lorsque des datagrammes anonymes doivent être transférés vers un host:port donné, le bridge envoie au host:port spécifié un message contenant les données suivantes :

```
$datagram_payload
```
À partir de SAM 3.2, lorsque HEADER=true est spécifié dans SESSION CREATE, le datagramme brut transféré sera précédé d'une ligne d'en-tête comme suit :

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
Pour une méthode alternative d'envoi de datagrammes anonymes, voir [RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### Datagram 2/3

Les formats Datagram 2/3 sont de nouveaux formats spécifiés au début de 2025. Aucune implémentation connue n'existe actuellement. Consultez la documentation d'implémentation pour connaître le statut actuel. Voir [la spécification](/docs/specs/datagrams) pour plus d'informations.

Il n'y a actuellement aucun plan pour augmenter la version SAM afin d'indiquer le support de Datagram 2/3. Cela peut être problématique car les implémentations pourraient souhaiter supporter Datagram 2/3 mais pas les fonctionnalités SAM v3.3. Tout changement de version reste à déterminer.

Datagram2 et Datagram3 sont tous deux répondables. Seul Datagram2 est authentifié.

Datagram2 est identique aux datagrammes avec réponse du point de vue de SAM. Les deux sont authentifiés. Seuls le format I2CP et la signature sont différents, mais ceci n'est pas visible pour les clients SAM. Datagram2 prend également en charge les signatures hors ligne, il peut donc être utilisé par des destinations signées hors ligne.

L'intention est que Datagram2 remplace les datagrammes Repliable pour les nouvelles applications qui ne nécessitent pas de compatibilité descendante. Datagram2 fournit une protection contre la réexécution qui n'est pas présente pour les datagrammes Repliable. Si la compatibilité descendante est requise, une application peut supporter à la fois Datagram2 et Repliable sur la même session avec les sessions SAM 3.3 PRIMARY.

Datagram3 permet les réponses mais n'est pas authentifié. Le champ 'from' au format I2CP est un hash, pas une destination. La $destination envoyée du serveur SAM au client sera un hash base64 de 44 octets. Pour le convertir en destination complète pour une réponse, décodez-le en base64 vers 32 octets binaires, puis encodez-le en base32 vers 52 caractères et ajoutez ".b32.i2p" pour une NAMING LOOKUP. Comme d'habitude, les clients devraient maintenir leur propre cache pour éviter les NAMING LOOKUPs répétées.

Les concepteurs d'applications doivent faire preuve d'une extrême prudence et considérer les implications de sécurité des datagrammes non authentifiés.

#### Considérations relatives au MTU des datagrammes V3

Les datagrammes I2P peuvent être plus volumineux que le MTU internet typique de 1500. Les datagrammes envoyés localement et les datagrammes transférables préfixés avec la destination base64 de 516+ octets sont susceptibles de dépasser ce MTU. Cependant, les MTU localhost sur les systèmes Linux sont typiquement beaucoup plus importants, par exemple 65536. Les MTU localhost varieront selon l'OS. Les datagrammes I2P ne dépasseront jamais 65536. La taille du datagramme dépend du protocole d'application.

Si le client SAM est local au serveur SAM et que le système prend en charge une MTU plus grande, alors les datagrammes ne seront pas fragmentés localement. Cependant, si le client SAM est distant, alors les datagrammes IPv4 seraient fragmentés et les datagrammes IPv6 échoueraient (IPv6 ne prend pas en charge la fragmentation UDP).

Les développeurs de bibliothèques client et d'applications doivent être conscients de ces problèmes et documenter les recommandations pour éviter la fragmentation et prévenir la perte de paquets, en particulier sur les connexions client-serveur SAM distantes.

#### DATAGRAM SEND, RAW SEND (Gestion des datagrammes compatible V1/V2)

Dans SAMv3, la méthode préférée pour envoyer des datagrammes est via le socket datagramme au port 7655 comme documenté ci-dessus. Cependant, les datagrammes avec réponse peuvent être envoyés directement via le socket bridge SAM en utilisant la commande DATAGRAM SEND, comme documenté dans [SAM V1](/docs/api/sam) et [SAM V2](/docs/api/samv2).

À partir de la version 0.9.14 (version 3.1), les datagrammes anonymes peuvent être envoyés directement via le socket de pont SAM en utilisant la commande RAW SEND, comme documenté dans [SAM V1](/docs/api/sam) et [SAM V2](/docs/api/samv2).

À partir de la version 0.9.24 (version 3.2), DATAGRAM SEND et RAW SEND peuvent inclure les paramètres FROM_PORT=nnnn et/ou TO_PORT=nnnn pour remplacer les ports par défaut. À partir de la version 0.9.24 (version 3.2), RAW SEND peut inclure le paramètre PROTOCOL=nnn pour remplacer le protocole par défaut.

Ces commandes ne prennent *pas* en charge le paramètre ID. Les datagrammes sont envoyés à la session de style DATAGRAM ou RAW créée le plus récemment, selon le cas. La prise en charge du paramètre ID pourra être ajoutée dans une version future.

Les formats DATAGRAM2 et DATAGRAM3 ne sont *pas* pris en charge de manière compatible avec V1/V2.

### Sessions SAM PRIMARY (V3.3 et supérieures)

*La version 3.3 a été introduite dans la version 0.9.25 d'I2P.*

*Dans une version antérieure de cette spécification, les sessions PRIMARY étaient connues sous le nom de sessions MASTER. Dans `i2pd` et `I2P+`, elles sont toujours connues uniquement sous le nom de sessions MASTER.*

SAM v3.3 ajoute la prise en charge de l'exécution de sous-sessions streaming, datagrams et raw sur la même session primaire, et pour l'exécution de plusieurs sous-sessions du même style. Tout le trafic des sous-sessions utilise une seule destination, ou un ensemble de tunnels. Le routage du trafic depuis I2P est basé sur les options de port et de protocole pour les sous-sessions.

Pour créer des sous-sessions multiplexées, vous devez créer une session primaire puis ajouter des sous-sessions à la session primaire. Chaque sous-session doit avoir un identifiant unique ainsi qu'un protocole d'écoute et un port uniques. Les sous-sessions peuvent également être supprimées de la session primaire.

Avec une session PRIMARY et une combinaison de sous-sessions, un client SAM peut prendre en charge plusieurs applications, ou une seule application sophistiquée utilisant une variété de protocoles, sur un seul ensemble de tunnels. Par exemple, un client bittorrent pourrait configurer une sous-session streaming pour les connexions pair-à-pair, ainsi que des sous-sessions datagram et raw pour la communication DHT.

#### Création d'une session PRIMARY

```
->  SESSION CREATE
          STYLE=PRIMARY                        # prior to 0.9.47, use STYLE=MASTER
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP and streaming options
```
Le pont SAM répondra avec un succès ou un échec comme dans [la réponse à un SESSION CREATE standard](#session-creation-response).

Ne définissez pas les options PORT, HOST, FROM_PORT, TO_PORT, PROTOCOL, LISTEN_PORT, LISTEN_PROTOCOL ou HEADER sur une session primaire. Vous ne pouvez envoyer aucune donnée sur un ID de session PRIMARY ou sur la socket de contrôle. Toutes les commandes telles que STREAM CONNECT, DATAGRAM SEND, etc. doivent utiliser l'ID de sous-session sur une socket séparée.

La session PRIMAIRE se connecte au router et construit des tunnels. Lorsque le pont SAM répond, les tunnels ont été construits et la session est prête pour que des sous-sessions soient ajoutées. Toutes les options [I2CP](/docs/protocol/i2cp) relatives aux paramètres de tunnel tels que la longueur, la quantité et le pseudonyme doivent être fournies dans le SESSION CREATE de la session primaire.

Toutes les commandes utilitaires sont prises en charge sur une session primaire.

Lorsque la session principale est fermée, toutes les sous-sessions sont également fermées.

NOTE : Avant la version 0.9.47, utilisez STYLE=MASTER. STYLE=PRIMARY est pris en charge à partir de la version 0.9.47. MASTER est toujours pris en charge pour la rétrocompatibilité.

#### Création d'une sous-session

En utilisant la même socket de contrôle sur laquelle la session PRIMARY a été créée :

```
->  SESSION ADD
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See above for DATAGRAM2/3
          ID=$nickname                         # must be unique
          [PORT=$port]                         # Required for DATAGRAM* and RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # For outbound traffic, default 0
          [TO_PORT=nnn]                        # For outbound traffic, default 0
          [PROTOCOL=nnn]                       # For outbound traffic for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [LISTEN_PORT=nnn]                    # For inbound traffic, default is the FROM_PORT value.
                                               # For STYLE=STREAM, only the FROM_PORT value or 0 is allowed.
          [LISTEN_PROTOCOL=nnn]                # For inbound traffic for STYLE=RAW only.
                                               # Default is the PROTOCOL value; 6 (streaming) is disallowed
          [HEADER={true,false}]                # For STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
Le pont SAM répondra avec un succès ou un échec comme dans [la réponse à une SESSION CREATE standard](#session-creation-response). Comme les tunnels ont déjà été construits lors de la SESSION CREATE primaire, le pont SAM devrait répondre immédiatement.

Ne définissez pas l'option DESTINATION sur un SESSION ADD. La sous-session utilisera la destination spécifiée dans la session principale. Toutes les sous-sessions doivent être ajoutées sur le socket de contrôle, c'est-à-dire la même connexion sur laquelle vous avez créé la session principale.

Les sous-sessions multiples doivent avoir des options suffisamment uniques pour que les données entrantes puissent être routées correctement. En particulier, les sessions multiples du même style doivent avoir des options LISTEN_PORT différentes (et/ou LISTEN_PROTOCOL, pour RAW uniquement). Un SESSION ADD avec un port d'écoute et un protocole qui duplique une sous-session existante entraînera une erreur.

Le LISTEN_PORT est le port I2P local, c'est-à-dire le port de réception (TO) pour les données entrantes. Si le LISTEN_PORT n'est pas spécifié, la valeur FROM_PORT sera utilisée. Si le LISTEN_PORT et FROM_PORT ne sont pas spécifiés, le routage entrant sera basé uniquement sur STYLE et PROTOCOL. Pour LISTEN_PORT et LISTEN_PROTOCOL, 0 signifie toute valeur, c'est-à-dire un caractère générique. Si LISTEN_PORT et LISTEN_PROTOCOL sont tous deux à 0, cette sous-session sera celle par défaut pour le trafic entrant qui n'est pas routé vers une autre sous-session. Le trafic de streaming entrant (protocole 6) ne sera jamais routé vers une sous-session RAW, même si son LISTEN_PROTOCOL est 0. Une sous-session RAW ne peut pas définir un LISTEN_PROTOCOL de 6. S'il n'y a pas de sous-session par défaut ou correspondant au protocole et au port du trafic entrant, ces données seront supprimées.

Utilisez l'ID de sous-session, et non l'ID de session principale, pour envoyer et recevoir des données. Toutes les commandes telles que STREAM CONNECT, DATAGRAM SEND, etc. doivent utiliser l'ID de sous-session.

Toutes les commandes utilitaires sont prises en charge sur une session principale ou sous-session. L'envoi/réception de datagrammes/raw v1/v2 ne sont pas pris en charge sur une session principale ou sur des sous-sessions.

#### Arrêter une sous-session

En utilisant le même socket de contrôle sur lequel la session PRIMARY a été créée :

```
->  SESSION REMOVE
          ID=$nickname
```
Ceci supprime une sous-session de la session principale. Ne définissez aucune autre option sur un SESSION REMOVE. Les sous-sessions doivent être supprimées sur le socket de contrôle, c'est-à-dire la même connexion sur laquelle vous avez créé la session principale. Après qu'une sous-session soit supprimée, elle est fermée et ne peut plus être utilisée pour envoyer ou recevoir des données.

Le pont SAM répondra avec succès ou échec comme dans [la réponse à une SESSION CREATE standard](#session-creation-response).

### Commandes utilitaires SAM

Certaines commandes utilitaires nécessitent une session préexistante et d'autres non. Voir les détails ci-dessous.

#### Recherche de nom d'hôte

Le message suivant peut être utilisé par le client pour interroger le pont SAM concernant la résolution de noms :

```
NAMING LOOKUP
       NAME=$name
       [OPTIONS=true]     # Default false, as of router API 0.9.66
```
qui reçoit comme réponse

```
NAMING REPLY
       RESULT=$result
       NAME=$name
       [VALUE=$destination]
       [MESSAGE="$message"]
       [OPTION:optionkey="$optionvalue"]   # As of router API 0.9.66
```
La valeur RESULT peut être l'une des suivantes :

```
OK
INVALID_KEY
KEY_NOT_FOUND
```
Si NAME=ME, alors la réponse contiendra la destination utilisée par la session actuelle (utile si vous utilisez une destination TRANSIENT). Si $result n'est pas OK, MESSAGE peut transmettre un message descriptif, tel que "bad format", etc. INVALID_KEY implique qu'il y a un problème avec $name dans la requête, possiblement des caractères invalides.

Le $destination est la base 64 de la [Destination](/docs/specs/common-structures#type_Destination), qui fait 516 caractères base 64 ou plus (387 octets ou plus en binaire), selon le type de signature.

NAMING LOOKUP ne nécessite pas qu'une session ait été créée au préalable. Cependant, dans certaines implémentations, une recherche .b32.i2p qui n'est pas en cache et nécessite une requête réseau peut échouer, car aucun tunnel client n'est disponible pour la recherche.

#### Options de recherche de nom

NAMING LOOKUP est étendu à partir de l'API router 0.9.66 pour prendre en charge les recherches de services. Le support peut varier selon l'implémentation. Voir la proposition 167 pour des informations supplémentaires.

NAMING LOOKUP NAME=example.i2p OPTIONS=true demande le mappage des options dans la réponse. NAME peut être une destination base64 complète lorsque OPTIONS=true.

Si la recherche de destination a réussi et que des options étaient présentes dans le leaseSet, alors dans la réponse, suivant la destination, il y aura une ou plusieurs options sous la forme OPTION:clé=valeur. Chaque option aura un préfixe OPTION: séparé. Toutes les options du leaseSet seront incluses, pas seulement les options d'enregistrement de service. Par exemple, des options pour des paramètres définis dans le futur peuvent être présentes. Exemple :

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Les clés contenant '=', et les clés ou valeurs contenant un saut de ligne, sont considérées comme invalides et la paire clé/valeur sera supprimée de la réponse. Si aucune option n'est trouvée dans le leaseSet, ou si le leaseSet était de version 1, alors la réponse n'inclura aucune option. Si OPTIONS=true était dans la recherche, et que le leaseSet n'est pas trouvé, une nouvelle valeur de résultat LEASESET_NOT_FOUND sera retournée.

#### Génération de clé de destination

Les clés base64 publiques et privées peuvent être générées en utilisant le message suivant :

```
->  DEST GENERATE
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, default DSA_SHA1
```
à laquelle il est répondu par

```
DEST REPLY
     PUB=$destination
     PRIV=$privkey
```
À partir de la version 3.1 (I2P 0.9.14), un paramètre optionnel SIGNATURE_TYPE est pris en charge. La valeur SIGNATURE_TYPE peut être n'importe quel nom (par exemple ECDSA_SHA256_P256, insensible à la casse) ou nombre (par exemple 1) qui est pris en charge par [Key Certificates](/docs/specs/common-structures#type_Certificate). La valeur par défaut est DSA_SHA1, ce qui n'est PAS ce que vous voulez. Pour la plupart des applications, veuillez spécifier SIGNATURE_TYPE=7.

Le $destination est la base 64 de la [Destination](/docs/specs/common-structures#type_Destination), qui fait 516 caractères base 64 ou plus (387 octets ou plus en binaire), selon le type de signature.

La $privkey est le base 64 de la concaténation de la [Destination](/docs/specs/common-structures#type_Destination) suivie de la [Private Key](/docs/specs/common-structures#type_PrivateKey) suivie de la [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), ce qui représente 884 caractères base 64 ou plus (663 octets ou plus en binaire), selon le type de signature. Le format binaire est spécifié dans Private Key File.

Notes sur la [Private Key](/docs/specs/common-structures#type_PrivateKey) binaire de 256 octets : Ce champ est inutilisé depuis la version 0.6 (2005). Les implémentations SAM peuvent envoyer des données aléatoires ou tous des zéros dans ce champ ; ne vous inquiétez pas d'une chaîne d'AAAA dans le base 64. La plupart des applications stockeront simplement la chaîne base 64 et la retourneront telle quelle dans SESSION CREATE, ou la décoderont en binaire pour le stockage, puis l'encoderont à nouveau pour SESSION CREATE. Les applications peuvent cependant décoder le base 64, analyser le binaire en suivant la spécification PrivateKeyFile, ignorer la portion de private key de 256 octets, puis la remplacer par 256 octets de données aléatoires ou tous des zéros lors du re-encodage pour SESSION CREATE. TOUS les autres champs de la spécification PrivateKeyFile doivent être préservés. Cela économiserait 256 octets de stockage sur le système de fichiers mais ne vaut probablement pas la peine pour la plupart des applications. Voir la proposition 161 pour des informations supplémentaires et le contexte.

DEST GENERATE ne nécessite pas qu'une session ait été créée au préalable.

DEST GENERATE ne peut pas être utilisé pour créer une destination avec des signatures hors ligne.

#### PING/PONG (SAM 3.2 ou supérieur)

Le client ou le serveur peut envoyer :

```
PING[ arbitrary text]
```
sur le port de contrôle, avec la réponse :

```
PONG[ arbitrary text from the ping]
```
à utiliser pour maintenir active la socket de contrôle. Chaque côté peut fermer la session et la socket si aucune réponse n'est reçue dans un délai raisonnable, selon l'implémentation.

Si un délai d'attente se produit en attendant un PONG du client, le pont peut envoyer :

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
et ensuite se déconnecter.

Si un délai d'expiration se produit en attendant un PONG du pont, le client peut simplement se déconnecter.

PING/PONG ne nécessitent pas qu'une session ait été créée au préalable.

#### QUIT/STOP/EXIT (SAM 3.2 ou supérieur, fonctionnalités optionnelles)

Les commandes QUIT, STOP et EXIT fermeront la session et le socket. L'implémentation est optionnelle, pour faciliter les tests via telnet. Qu'il y ait une réponse avant la fermeture du socket (par exemple, un message SESSION STATUS) dépend de l'implémentation et sort du cadre de cette spécification.

QUIT/STOP/EXIT ne nécessitent pas qu'une session ait été créée au préalable.

#### HELP (fonctionnalité optionnelle)

Les serveurs peuvent implémenter une commande HELP. L'implémentation est optionnelle, pour faciliter les tests via telnet. Le format de sortie et la détection de la fin de la sortie sont spécifiques à l'implémentation et en dehors du périmètre de cette spécification.

HELP ne nécessite pas qu'une session ait été créée au préalable.

#### Configuration d'autorisation (SAMv3.2 ou supérieur, fonctionnalité optionnelle)

Configuration d'autorisation utilisant la commande AUTH. Un serveur SAM peut implémenter ces commandes pour faciliter le stockage persistant des identifiants. La configuration d'authentification autre qu'avec ces commandes est spécifique à l'implémentation et en dehors de la portée de cette spécification.

- AUTH ENABLE active l'autorisation sur les connexions suivantes
- AUTH DISABLE désactive l'autorisation sur les connexions suivantes
- AUTH ADD USER="foo" PASSWORD="bar" ajoute un utilisateur/mot de passe
- AUTH REMOVE USER="foo" supprime cet utilisateur

Les guillemets doubles pour l'utilisateur et le mot de passe sont recommandés mais non obligatoires. Un guillemet double à l'intérieur d'un nom d'utilisateur ou d'un mot de passe doit être échappé avec une barre oblique inverse. En cas d'échec, le serveur répondra avec un I2P_ERROR et un message.

AUTH ne nécessite pas qu'une session ait été créée au préalable.

### Valeurs RESULT

Voici les valeurs que peut contenir le champ RESULT, avec leur signification :

```
OK              Operation completed successfully
CANT_REACH_PEER The peer exists, but cannot be reached
DUPLICATED_DEST The specified Destination is already in use
I2P_ERROR       A generic I2P error (e.g. I2CP disconnection, etc.)
INVALID_KEY     The specified key is not valid (bad format, etc.)
KEY_NOT_FOUND   The naming system can't resolve the given name
PEER_NOT_FOUND  The peer cannot be found on the network
TIMEOUT         Timeout while waiting for an event (e.g. peer answer)
LEASESET_NOT_FOUND  See Name Lookup Options above. As of router API 0.9.66.
```
Les différentes implémentations peuvent ne pas être cohérentes quant au RESULT retourné dans divers scénarios.

La plupart des réponses avec un RESULT, autre qu'OK, incluront également un MESSAGE avec des informations supplémentaires. Le MESSAGE sera généralement utile pour déboguer les problèmes. Cependant, les chaînes MESSAGE dépendent de l'implémentation, peuvent être traduites ou non par le serveur SAMv3 selon la locale actuelle, peuvent contenir des informations internes spécifiques à l'implémentation telles que des exceptions, et sont susceptibles d'être modifiées sans préavis. Bien que les clients SAMv3 puissent choisir d'exposer les chaînes MESSAGE aux utilisateurs, ils ne devraient pas prendre de décisions programmatiques basées sur ces chaînes, car cela serait fragile.

### Options de Tunnel, I2CP et Streaming

Ces options peuvent être passées comme paires nom=valeur dans la ligne SAM SESSION CREATE.

Toutes les sessions peuvent inclure [des options I2CP telles que les longueurs et quantités de tunnels](/docs/protocol/i2cp#options). Les sessions STREAM peuvent inclure [des options de la bibliothèque Streaming](/docs/api/streaming#options).

Consultez ces références pour les noms d'options et les valeurs par défaut. La documentation référencée concerne l'implémentation du router Java. Les valeurs par défaut sont susceptibles de changer. Les noms et valeurs d'options sont sensibles à la casse. D'autres implémentations de router peuvent ne pas prendre en charge toutes les options et peuvent avoir des valeurs par défaut différentes ; consultez la documentation du router pour plus de détails.

### Notes BASE 64

L'encodage Base 64 doit utiliser l'alphabet Base 64 standard I2P "A-Z, a-z, 0-9, -, ~".

### Configuration SAM par défaut

Le port SAM par défaut est 7656. SAM n'est pas activé par défaut dans le routeur I2P Java ; il doit être démarré manuellement, ou configuré pour démarrer automatiquement, sur la page de configuration des clients dans la console du routeur, ou dans le fichier clients.config. Le port UDP SAM par défaut est 7655, écoutant sur 127.0.0.1. Ces paramètres peuvent être modifiés dans le routeur Java en ajoutant les arguments sam.udp.port=nnnnn et/ou sam.udp.host=w.x.y.z à l'invocation, ou sur la ligne SESSION.

La configuration dans d'autres routeurs est spécifique à l'implémentation. Consultez [le guide de configuration i2pd ici](https://i2pd.readthedocs.io/en/latest/user-guide/configuration/).
