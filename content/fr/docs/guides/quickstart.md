---
title: "Premiers pas avec I2P : un guide complet pour les débutants"
description: "Premiers pas avec I2P : un guide complet pour les débutants"
slug: "gettingstarted"
lastUpdated: "2026-03"
accurateFor: "2.11.0"
---

**I2P est un réseau anonyme, pair-à-pair et entièrement chiffré qui fonctionne « à l'intérieur » d'Internet**, et l'implémentation Java provenant de i2p.net reste la méthode principale pour l'utiliser. Contrairement à Tor, qui anonymise principalement l'accès au web classique, I2P crée un réseau entièrement autonome composé de services cachés, de sites web, de messagerie électronique, de chat et de partage de fichiers.

---

## Ce qui se passe au moment où vous démarrez I2P

Après l'installation, I2P lance une application web locale appelée la **console du routeur** à l'adresse `http://127.0.0.1:7657`. C'est votre centre de commande, qui fonctionne entièrement sur votre machine et est limité à localhost pour des raisons de sécurité. Lors du premier démarrage, un **assistant de configuration** vous guide à travers le choix de la langue, du thème (sombre ou clair), ainsi qu'un test de bande passante automatisé d'une durée d'environ une minute utilisant le service de mesure externe M-Lab. Vous définissez ensuite quel pourcentage de votre bande passante partager avec le réseau.

![Assistant de configuration d'I2P - Sélection de la langue](/images/guides/quickstart/wizard-language-selection.webp)

Une fois l'assistant terminé, le routeur commence le **bootstrapping**, un processus appelé « reseeding ». Votre routeur télécharge environ **100 enregistrements RouterInfo** depuis des serveurs de reseed en dur via HTTPS, obtenant ainsi une liste initiale de pairs. À partir de là, il commence à créer des **tunnels exploratoires** afin de découvrir davantage de pairs et peupler sa copie locale de la base de données du réseau (le « netDb »). Vous verrez apparaître un message « Rejecting tunnels: starting up » pendant ces premières minutes. C'est normal.

![Amorçage I2P - Recherche initiale](/images/guides/quickstart/reseed-bootstrapping.webp)

**Prévoyez d'attendre entre 3 et 10 minutes** avant que votre routeur ne devienne utilisable, et beaucoup plus longtemps — plusieurs jours de fonctionnement ininterrompu — avant d'atteindre ses performances maximales. La barre latérale de la console du routeur affiche votre nombre de pairs sous la forme « Actifs x/y », où x représente les pairs avec lesquels vous avez échangé récemment des messages, et y l'ensemble des pairs détectés. Dès que vous voyez **10 pairs actifs ou plus**, votre routeur est correctement connecté. La chose la plus importante qu'un nouvel utilisateur puisse faire est de **laisser le routeur fonctionner en continu**. Après une fermeture, les autres nœuds marquent votre routeur comme étant peu fiable pendant au moins 24 heures ; ainsi, redémarrer fréquemment dégrade fortement les performances.

![Tableau de bord de la console du routeur I2P](/images/guides/quickstart/router-console-dashboard.png)

---

## Configurer votre navigateur pour I2P

Contrairement au réseau Tor, I2P ne dispose pas de navigateur dédié. Pour accéder aux sites I2P (le pseudo-domaine de premier niveau `.i2p`), vous devez configurer les paramètres proxy de votre navigateur afin de router le trafic via le proxy HTTP d'I2P sur le port **4444**.

**Le chemin le plus simple pour les utilisateurs Windows** est le **bundle d'installation facile**, qui regroupe Java, le routeur et un profil Firefox pré-configuré avec l'extension « I2P in Private Browsing ». Il élimine toute configuration manuelle du proxy. Du téléchargement à la navigation sur les sites I2P, cela prend environ quatre minutes. Un bundle d'installation facile pour macOS (puce Apple Silicon) est également disponible en version bêta. Si vous utilisez le bundle d'installation facile, vous pouvez ignorer la configuration manuelle décrite ci-dessous.

### Firefox (Recommandé)

Firefox est fortement recommandé car il dispose de ses propres paramètres de proxy indépendants de votre système d'exploitation - Chrome et Edge utilisent des paramètres de proxy système qui affectent toutes les applications.

**Étape 1.** Ouvrez le menu de Firefox (icône hamburger) et cliquez sur **Paramètres**.

![Firefox - Ouvrir les paramètres](/images/guides/browser-config/accessi2p_3.png)

**Étape 2.** Recherchez **proxy** dans la barre de recherche des paramètres, puis cliquez sur **Paramètres...** à côté des paramètres réseau.

![Firefox - Rechercher un proxy](/images/guides/browser-config/accessi2p_4.png)

**Étape 3.** Sélectionnez **Configuration manuelle du proxy**, saisissez `127.0.0.1` pour le proxy HTTP et `4444` pour le port, puis cliquez sur **OK**.

![Firefox - Configuration manuelle du proxy](/images/guides/browser-config/accessi2p_5.png)

Après avoir configuré le proxy, plusieurs ajustements dans `about:config` sont recommandés :

- Définir `media.peerConnection.ice.proxy_only` à **true** (empêche les fuites WebRTC)
- Définir `keyword.enabled` à **false** (arrête les redirections vers les moteurs de recherche sur les adresses .i2p)
- Créer un booléen `browser.fixup.domainsuffixwhitelist.i2p` défini à **true** (indique à Firefox que `.i2p` est un suffixe de domaine valide)

Un piège fréquent pour les débutants : tapez toujours `http://` avant les adresses `.i2p`. La plupart des sites I2P n'utilisent pas HTTPS (I2P chiffre déjà tout le trafic de bout en bout), et sans ce préfixe, Firefox vous redirigera vers un moteur de recherche.

### Chrome / Edge (Windows)

Remarque : Chrome et Edge utilisent les paramètres de proxy de votre système d'exploitation, ce qui affecte **toutes** les applications de votre système.

**Étape 1.** Ouvrez le menu de Chrome et cliquez sur **Paramètres**.

![Chrome - Ouvrir les paramètres](/images/guides/browser-config/accessi2p_6.png)

**Étape 2.** Recherchez **proxy**, puis cliquez sur **Ouvrir les paramètres de proxy de votre ordinateur**.

![Chrome - Rechercher un proxy](/images/guides/browser-config/accessi2p_7.png)

**Étape 3.** Sous **Configuration manuelle du proxy**, cliquez sur **Configurer** à côté de « Utiliser un serveur proxy ».

![Windows - Paramètres du proxy](/images/guides/browser-config/accessi2p_8.png)

**Étape 4.** Activez **Utiliser un serveur proxy**, saisissez `127.0.0.1` comme adresse IP du proxy et `4444` comme port, puis cliquez sur **Enregistrer**.

![Windows - Modifier le serveur proxy](/images/guides/browser-config/accessi2p_9.png)

### Safari (macOS)

**Étape 1.** Allez dans **Safari → Paramètres → Avancé** puis cliquez sur **Modifier les paramètres...** à côté de Proxys.

![Safari - Paramètres avancés](/images/guides/browser-config/accessi2p_1.png)

**Étape 2.** Activez le **proxy Web (HTTP)**, saisissez `127.0.0.1` comme serveur et `4444` comme port, puis cliquez sur **OK**.

![macOS - Paramètres du proxy web](/images/guides/browser-config/accessi2p_2.png)

---

## Comprendre le tableau de bord de la console du routeur

La console du routeur à l'adresse `127.0.0.1:7657` affiche plusieurs indicateurs clés qui vous indiquent la performance de votre nœud. La **barre latérale** montre votre version d'I2P, le temps de fonctionnement, l'utilisation de la bande passante (entrée/sortie), le nombre de pairs actifs et l'état des tunnels. Lorsque « Clients partagés » devient vert, votre routeur est intégré et prêt à l'emploi.

![Console du routeur - Clients partagés en vert](/images/guides/quickstart/shared-clients-green.png)

Les **graphiques de bande passante** affichent le débit en temps réel. Les valeurs par défaut sont conservatrices : **96 Ko/s en réception et 40 Ko/s en émission**, avec seulement **48 Ko/s partagés**, et la documentation officielle recommande vivement de les augmenter. Rendez-vous sur `http://127.0.0.1:7657/config` (ou cliquez sur « Configurer la bande passante » dans la console) pour augmenter vos limites. Une bande passante partagée plus élevée améliore à la fois vos propres performances et la santé du réseau. Définir une bande passante partagée inférieure à **12 Ko/s** place effectivement votre routeur en « mode caché », vous empêchant de participer au trafic. À partir de **128 Ko/s ou plus**, votre routeur peut être promu au statut de *floodfill*, ce qui signifie qu’il contribue à la maintenance de la table de hachage distribuée.

![Configuration de la bande passante](/images/guides/quickstart/bandwidth-config.png)

La section **état du tunnel** affiche les tunnels participants — le trafic que vous relayez pour autrui. Plus de 90 % des routeurs I2P relaient par défaut du trafic participant. Cela constitue à la fois un trafic de couverture pour votre propre anonymat et votre contribution au réseau. Les tunnels expirent toutes les 10 minutes et sont reconstruits automatiquement.

![Gestionnaire I2PTunnel](/images/guides/quickstart/tunnel-manager.png)

Le gestionnaire **I2PTunnel** à l'adresse `http://127.0.0.1:7657/i2ptunnel/` affiche tous vos tunnels configurés — le proxy HTTP, IRC, le courrier électronique et le tunnel de votre serveur eepsite sont tous pré-configurés par défaut.

![Liste I2PTunnel](/images/guides/quickstart/i2ptunnel-list.png)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Console page</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">URL</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Home / Status</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/home</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Dashboard with peers, bandwidth, tunnels</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Bandwidth config</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/config</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Adjust speed limits and share percentage</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Network config</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/confignet</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Firewall, port, and reachability settings</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Tunnel manager</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/i2ptunnel/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Manage all I2P tunnels and hidden services</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">I2PSnark</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/i2psnark/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Built-in BitTorrent client</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">SusiMail</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/susimail/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Built-in email client</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Address book</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/dns</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Manage .i2p hostname mappings</td>
</tr>
</tbody>
</table>
---

## Cinq choses que vous pouvez faire une fois connecté

### Naviguer sur les sites web .i2p

L'utilisation la plus immédiate d'I2P est la navigation sur des sites web cachés. En configurant votre navigateur pour qu'il utilise le port 4444 en tant que proxy, rendez-vous sur n'importe quelle adresse `.i2p`. Plusieurs sites bien connus servent de bons points de départ : **`i2p-projekt.i2p`** est le site officiel du projet I2P miroiré à l'intérieur du réseau, **`i2pforum.i2p`** héberge le forum communautaire d'assistance, **`stats.i2p`** fournit des statistiques sur le réseau ainsi qu'un service d'enregistrement d'adresses, et **`notbob.i2p`** surveille le temps de fonctionnement des eepsites connus afin que vous puissiez voir ce qui est réellement en ligne. Lorsque vous rencontrez une adresse `.i2p` inconnue, le proxy proposera des liens de « service de saut » (jump service) permettant de résoudre le nom d'hôte — cliquez dessus pour ajouter de nouveaux sites à votre carnet d'adresses local.

I2P inclut également un **outproxy** par défaut (`exit.stormycloud.i2p`) qui vous permet d'accéder à Internet classique via I2P, mais ce n'est pas l'objectif principal du réseau et les performances seront lentes. I2P est conçu comme un darknet interne, et non comme un réseau de nœuds de sortie comme Tor.

### Partagez des fichiers Torrent anonymement avec I2PSnark

**I2PSnark** est un client BitTorrent entièrement fonctionnel intégré à chaque installation I2P, accessible à l'adresse `http://127.0.0.1:7657/i2psnark/`. Il fonctionne exclusivement au sein du réseau I2P : il ne peut pas se connecter à des torrents du clairnet, et les utilisateurs du clairnet ne peuvent pas voir les torrents I2P. L'interface web prend en charge les liens magnet, la DHT, le glisser-déposer, la recherche de torrents, les téléchargements séquentiels et les trackers UDP (ajoutés à partir de la version 2.10.0). La longueur par défaut des tunnels est de trois sauts. Il suffit d'ajouter des fichiers `.torrent` ou des liens magnet via l'interface.

![Interface I2PSnark](/images/guides/quickstart/i2psnark-interface.png)

Pour trouver des torrents, rendez-vous sur le **Postman Tracker** à l'adresse `http://tracker2.postman.i2p/` - un hub centralisé où les utilisateurs peuvent rechercher et télécharger des torrents publiés par d'autres membres du réseau I2P. Vous pouvez également y téléverser vos propres torrents pour les partager avec la communauté.

![Postman Tracker](/images/guides/quickstart/postman-tracker.png)

D'autres clients torrent compatibles avec I2P incluent BiglyBT et qBittorrent avec un greffon I2P.

### Envoyer des courriels chiffrés avec SusiMail

**SusiMail** à l'adresse `http://127.0.0.1:7657/susimail/` est un client de messagerie basé sur le web conçu pour éviter les fuites d'informations d'identification. Il se connecte au serveur de messagerie **`mail.i2p`** exploité par « postman ». Pour commencer, inscrivez-vous sur **`hq.postman.i2p`** (accessible via votre proxy I2P), puis connectez-vous avec ces identifiants dans SusiMail. Des entrées I2PTunnel préconfigurées acheminent SMTP via `localhost:7659` et POP3 via `localhost:7660`. Vous pouvez envoyer des courriels à d'autres utilisateurs `@mail.i2p` ainsi qu'à des adresses de messagerie Internet classiques (relayées via le serveur de messagerie en mode outproxy). SusiMail prend en charge le formatage markdown, les pièces jointes par glisser-déposer, et les courriels au format HTML.

![Boîte de réception SusiMail](/images/guides/quickstart/susimail-login.png)

![Rédiger un message SusiMail](/images/guides/quickstart/susimail-inbox.png)

### Discuter sur IRC via le réseau Irc2P

I2P est livré avec un **tunnel IRC préconfiguré** sur `localhost:6668`. Pointez n'importe quel client IRC vers cette adresse (avec SSL/TLS **désactivé** - I2P gère le chiffrement) et vous vous connecterez au réseau Irc2P, une fédération de serveurs incluant `irc.postman.i2p`, `irc.echelon.i2p` et `irc.dg.i2p`. Les principaux canaux sont **`#i2p`** pour les discussions générales, **`#i2p-dev`** pour le développement, et **`#i2p-help`** pour l'assistance. Le tunnel IRC supprime automatiquement les informations d'identification de votre connexion. Les clients recommandés incluent WeeChat, Pidgin et Thunderbird Chat.

### Hébergez votre propre site web anonyme

Chaque installation d’I2P inclut un **serveur web Jetty** déjà en cours d’exécution sur `localhost:7658`, avec un tunnel serveur I2P correspondant. Pour publier un site, il suffit de placer les fichiers HTML dans le répertoire racine : `~/.i2p/eepsite/docroot` sous Linux ou `%LOCALAPPDATA%\I2P\I2P Site\docroot` sous Windows. Votre site reçoit automatiquement une destination cryptographique au format Base64 et une adresse plus courte au format `xxxxx.b32.i2p`. Pour obtenir un nom lisible comme `mysite.i2p`, inscrivez-le auprès de services d’annuaire tels que `stats.i2p` ou `no.i2p`. Pour des configurations plus avancées, vous pouvez remplacer Jetty par Apache ou Nginx derrière le tunnel serveur I2PTunnel — pensez simplement à supprimer les en-têtes du serveur qui permettent l’identification. Pour un tutoriel détaillé, consultez notre guide [Créer un eepsite I2P](/docs/guides/creating-an-eepsite/).

---

## Pratiques de sécurité essentielles pour les nouveaux utilisateurs

**Ne naviguez jamais sur I2P et le clairnet avec le même profil de navigateur.** C'est la règle de sécurité la plus importante. Créez un profil Firefox dédié via `about:profiles` ou utilisez le profil préconfiguré fourni avec le bundle d'installation facile. La contamination croisée des cookies, de l'historique et des données mises en cache entre votre navigation anonyme et votre navigation identifiée constitue l'erreur la plus fréquente en matière de sécurité opérationnelle.

L'extension officielle **« I2P in Private Browsing »** pour Firefox (disponible sur le magasin d'add-ons de Mozilla) automatise en grande partie cette configuration en créant des onglets conteneurs isolés avec l'anti-empreinte numérique, l'isolation des premières parties et le letterboxing activés. Pour les utilisateurs de Chromium, lancez-le avec des indicateurs séparés : `--user-data-dir=$HOME/.config/chromium-i2p --proxy-server="http://127.0.0.1:4444"`.

---
