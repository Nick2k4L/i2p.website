---
title: "Intégrer I2P dans votre Application"
description: "Directives pour intégrer un router I2P avec votre application"
slug: "embedding"
lastUpdated: "2023-01"
accurateFor: "2.1.0"
---

## Aperçu

Cette page concerne l'intégration du binaire complet du router I2P avec votre application. Elle ne traite pas de l'écriture d'une application pour fonctionner avec I2P (qu'elle soit intégrée ou externe). Cependant, de nombreuses recommandations peuvent être utiles même si vous n'intégrez pas de router.

De nombreux projets intègrent, ou parlent d'intégrer, I2P. C'est formidable si c'est fait correctement. Si c'est mal fait, cela pourrait causer de réels dommages à notre réseau. Le router I2P est complexe, et il peut être difficile de masquer toute cette complexité à vos utilisateurs. Cette page présente quelques directives générales.

La plupart de ces directives s'appliquent également à Java I2P ou i2pd. Cependant, certaines directives sont spécifiques à Java I2P et sont indiquées ci-dessous.

### Contactez-nous

Entamez le dialogue. Nous sommes là pour vous aider. Les applications qui intègrent I2P représentent les opportunités les plus prometteuses - et passionnantes - pour nous permettre de développer le réseau et d'améliorer l'anonymat pour tous.

### Choisissez votre router avec soin

Si votre application est en Java ou Scala, le choix est facile - utilisez le router Java. Si elle est en C/C++, nous recommandons i2pd. Le développement d'i2pcpp s'est arrêté. Pour les applications dans d'autres langages, il est préférable d'utiliser SAM ou BOB ou SOCKS et d'intégrer le router Java comme processus séparé. Certains des éléments suivants ne s'appliquent qu'au router Java.

### Licences

Assurez-vous de respecter les exigences de licence du logiciel que vous intégrez.

---

## Configuration

### Vérifier la configuration par défaut

Une configuration par défaut correcte est cruciale. La plupart des utilisateurs ne modifieront pas les paramètres par défaut. Les valeurs par défaut de votre application peuvent nécessiter d'être différentes de celles du router que vous intégrez. Remplacez les paramètres par défaut du router si nécessaire.

Quelques paramètres par défaut importants à examiner : bande passante maximale, quantité et longueur des tunnels, nombre maximum de tunnels participants. Beaucoup de cela dépend de la bande passante attendue et des modèles d'utilisation de votre application.

Configurez suffisamment de bande passante et de tunnels pour permettre à vos utilisateurs de contribuer au réseau. Envisagez de désactiver I2CP externe, car vous n'en avez probablement pas besoin et cela pourrait entrer en conflit avec toute autre instance I2P en cours d'exécution. Examinez également les configurations pour désactiver l'arrêt de la JVM à la sortie, par exemple.

### Considérations sur le trafic de participation

Il peut être tentant pour vous de désactiver le trafic de participation. Il existe plusieurs façons de procéder (mode caché, définir le maximum de tunnels à 0, définir la bande passante partagée en dessous de 12 KBytes/sec). Sans le trafic de participation, vous n'avez pas à vous soucier de l'arrêt gracieux, vos utilisateurs ne voient pas l'utilisation de bande passante qui n'est pas générée par eux, etc. Cependant, il y a de nombreuses raisons pour lesquelles vous devriez autoriser les tunnels de participation.

Tout d'abord, le router ne fonctionne pas très bien s'il n'a pas la possibilité de s'« intégrer » au réseau, ce qui est grandement facilité par le fait que d'autres construisent des tunnels qui passent par vous.

Deuxièmement, plus de 90% des routers du réseau actuel permettent le trafic de participation. C'est le paramètre par défaut dans le router Java. Si votre application ne route pas pour les autres et qu'elle devient vraiment populaire, alors c'est un parasite sur le réseau, et cela perturbe l'équilibre que nous avons actuellement. Si elle devient vraiment importante, alors nous devenons Tor, et nous passons notre temps à supplier les gens d'activer le relais.

Troisièmement, le trafic participant constitue un trafic de couverture qui aide à l'anonymat de vos utilisateurs.

Nous vous déconseillons fortement de désactiver le trafic de participation par défaut. Si vous faites cela et que votre application devient extrêmement populaire, cela pourrait endommager le réseau.

### Persistance

Vous devez sauvegarder les données du router (netDb, configuration, etc.) entre les exécutions du router. I2P ne fonctionne pas bien si vous devez effectuer un reseed à chaque démarrage, ce qui représente une charge énorme sur nos serveurs de reseed et n'est pas très bon pour l'anonymat non plus. Même si vous incluez des router infos, I2P a besoin de données de profil sauvegardées pour de meilleures performances. Sans persistance, vos utilisateurs auront une mauvaise expérience de démarrage.

Il y a deux possibilités si vous ne pouvez pas fournir de persistance. L'une ou l'autre élimine la charge de votre projet sur nos serveurs de reseed et améliorera significativement le temps de démarrage.

1) Configurez votre propre serveur (ou vos propres serveurs) de reseed de projet qui servent beaucoup plus que le nombre habituel d'infos de router dans le reseed, disons, plusieurs centaines. Configurez le router pour utiliser uniquement vos serveurs.

2) Intégrez entre mille et deux mille informations de router dans votre programme d'installation.

De plus, retardez ou échelonnez le démarrage de vos tunnels, pour donner au router une chance de s'intégrer avant de construire beaucoup de tunnels.

### Configurabilité

Donnez à vos utilisateurs un moyen de modifier la configuration des paramètres importants. Nous comprenons que vous voudrez probablement masquer la plupart de la complexité d'I2P, mais il est important d'afficher quelques paramètres de base. En plus des valeurs par défaut ci-dessus, certains paramètres réseau tels qu'UPnP, IP/port peuvent être utiles.

### Considérations sur les floodfill

Au-dessus d'un certain paramètre de bande passante, et en respectant d'autres critères de santé, votre router deviendra floodfill, ce qui peut provoquer une forte augmentation des connexions et de l'utilisation mémoire (au moins avec le router Java). Réfléchissez si c'est acceptable. Vous pouvez désactiver floodfill, mais alors vos utilisateurs les plus rapides ne contribuent pas à leur plein potentiel. Cela dépend aussi du temps de fonctionnement typique de votre application.

### Reseeding

Décidez si vous regroupez les informations de router ou si vous utilisez nos hôtes de reseed. La liste des hôtes de reseed Java se trouve dans le code source, donc si vous maintenez votre code source à jour, la liste des hôtes le sera également. Soyez conscient d'un possible blocage par des gouvernements hostiles.

### Utiliser des clients partagés

Java I2P i2ptunnel prend en charge les clients partagés, où les clients peuvent être configurés pour utiliser un pool unique. Si vous avez besoin de plusieurs clients, et si cela est cohérent avec vos objectifs de sécurité, configurez les clients pour qu'ils soient partagés.

### Limiter la quantité de tunnels

Spécifiez la quantité de tunnels explicitement avec les options `inbound.quantity` et `outbound.quantity`. La valeur par défaut dans Java I2P est 2 ; la valeur par défaut dans i2pd est plus élevée. Spécifiez dans la ligne SESSION CREATE en utilisant SAM pour obtenir des paramètres cohérents avec les deux routeurs. Deux tunnels entrants et sortants suffisent pour la plupart des applications à bande passante faible à moyenne et à distribution faible à moyenne. Les serveurs et les applications P2P à haute distribution peuvent nécessiter davantage. Voir ce message du forum pour des conseils sur le calcul des exigences pour les serveurs et applications à fort trafic.

### Spécifier le SAM SIGNATURE_TYPE

SAM utilise par défaut DSA_SHA1 pour les destinations, ce qui n'est pas ce que vous voulez. Ed25519 (type 7) est le bon choix. Ajoutez SIGNATURE_TYPE=7 à la commande DEST GENERATE, ou à la commande SESSION CREATE pour DESTINATION=TRANSIENT.

### Limiter les sessions SAM

La plupart des applications n'auront besoin que d'une seule session SAM. SAM offre la capacité de submerger rapidement le router local, ou même le réseau plus large, si un grand nombre de sessions sont créées. Si plusieurs sous-services peuvent utiliser une seule session, configurez-les avec une session PRIMARY et des SUBSESSIONS (actuellement non supporté sur i2pd). Une limite raisonnable de sessions est de 3 ou 4 au total, ou peut-être jusqu'à 10 dans de rares situations. Si vous avez plusieurs sessions, assurez-vous de spécifier une faible quantité de tunnels pour chacune, voir ci-dessus.

Dans presque aucune situation vous ne devriez avoir besoin d'une session unique par connexion. Sans une conception soigneuse, cela pourrait rapidement mener à un DDoS du réseau. Réfléchissez bien si vos objectifs de sécurité nécessitent des sessions uniques. Veuillez consulter les développeurs Java I2P ou i2pd avant d'implémenter des sessions par connexion.

### Réduire l'utilisation des ressources réseau

Notez que ces options ne sont actuellement pas prises en charge sur i2pd. Ces options sont prises en charge via I2CP et SAM (sauf delay-open, qui n'est disponible que via i2ptunnel). Consultez la documentation I2CP (et, pour delay-open, la documentation de configuration i2ptunnel) pour plus de détails.

Envisagez de configurer vos tunnels d'application en delay-open, reduce-on-idle et/ou close-on-idle. C'est simple si vous utilisez i2ptunnel mais vous devrez implémenter une partie par vous-même si vous utilisez I2CP directement. Consultez i2psnark pour du code qui réduit le nombre de tunnels puis ferme le tunnel, même en présence d'une certaine activité DHT en arrière-plan.

---

## Cycle de vie

### Capacité de mise à jour

Ayez une fonctionnalité de mise à jour automatique si cela est possible, ou au moins une notification automatique d'une nouvelle version. Notre plus grande crainte est un nombre énorme de routers là-bas qui ne peuvent pas être mis à jour. Nous avons environ 6-8 versions par an du router Java, et il est essentiel pour la santé du réseau que les utilisateurs restent à jour. Nous avons généralement plus de 80% du réseau sur la dernière version dans les 6 semaines après la sortie, et nous aimerions que cela reste ainsi. Vous n'avez pas besoin de vous préoccuper de désactiver la fonction de mise à jour automatique intégrée du router, car ce code se trouve dans la console du router, que vous ne bundlez vraisemblablement pas.

### Déploiement

Ayez un plan de déploiement progressif. Ne surchargez pas le réseau d'un coup. Nous avons actuellement environ 25 000 utilisateurs uniques par jour et 40 000 uniques par mois. Nous sommes probablement capables de gérer une croissance de 2 à 3 fois par an sans trop de problèmes. Si vous anticipez une montée en charge plus rapide que cela, OU si la distribution de bande passante (ou la distribution de temps de fonctionnement, ou toute autre caractéristique significative) de votre base d'utilisateurs est significativement différente de notre base d'utilisateurs actuelle, nous devons vraiment avoir une discussion. Plus vos plans de croissance sont importants, plus tout le reste de cette liste de contrôle est important.

### Concevoir pour et Encourager de Longues Durées de Fonctionnement

Dites à vos utilisateurs qu'I2P fonctionne mieux s'il continue de tourner. Il peut s'écouler plusieurs minutes après le démarrage avant qu'il fonctionne bien, et encore plus après la première installation. Si votre temps de fonctionnement moyen est inférieur à une heure, I2P n'est probablement pas la bonne solution.

---

## Interface utilisateur

### Afficher le statut

Fournir une indication à l'utilisateur que les tunnels d'application sont prêts. Encourager la patience.

### Arrêt en douceur

Si possible, retardez l'arrêt jusqu'à ce que vos tunnels participants expirent. Ne laissez pas vos utilisateurs casser facilement les tunnels, ou au moins demandez-leur de confirmer.

### Éducation et Don

Il serait bien que vous donniez à vos utilisateurs des liens pour en apprendre davantage sur I2P et pour faire des dons.

### Option de Router Externe

Selon votre base d'utilisateurs et votre application, il peut être utile de fournir une option ou un package séparé pour utiliser un router externe.

---

## Autres Sujets

### Utilisation d'autres services communs

Si vous prévoyez d'utiliser ou de vous connecter à d'autres services I2P courants (flux d'actualités, abonnements hosts.txt, trackers, outproxies, etc.), assurez-vous de ne pas les surcharger et parlez aux personnes qui les gèrent pour vous assurer que c'est acceptable.

### Problèmes d'heure / NTP

Note : Cette section fait référence à Java I2P. i2pd n'inclut pas de client SNTP.

I2P inclut un client SNTP. I2P nécessite une heure correcte pour fonctionner. Il compensera une horloge système décalée mais cela peut retarder le démarrage. Vous pouvez désactiver les requêtes SNTP d'I2P, mais cela n'est pas conseillé sauf si votre application s'assure que l'horloge système est correcte.

### Choisissez Quoi et Comment Vous Regroupez

Note : Cette section ne concerne que Java I2P.

Au minimum, vous aurez besoin de i2p.jar, router.jar, streaming.jar et mstreaming.jar. Vous pouvez omettre les deux jars de streaming pour une application datagramme uniquement. Certaines applications peuvent nécessiter plus de fichiers, par exemple i2ptunnel.jar ou addressbook.jar. N'oubliez pas jbigi.jar, ou un sous-ensemble de celui-ci pour les plateformes que vous supportez, pour accélérer considérablement la cryptographie. Java 7 ou supérieur est requis pour la compilation. Si vous construisez des paquets Debian / Ubuntu, vous devriez exiger le paquet I2P de notre PPA au lieu de l'inclure. Vous n'avez presque certainement pas besoin de susimail, susidns, de la console du router et d'i2psnark, par exemple.

Les fichiers suivants doivent être inclus dans le répertoire d'installation I2P, spécifié avec la propriété "i2p.dir.base". N'oubliez pas le répertoire certificates/, qui est requis pour le reseeding, et blocklist.txt pour la validation des IP. Le répertoire geoip est optionnel, mais recommandé afin que le router puisse prendre des décisions basées sur la localisation. Si vous incluez geoip, assurez-vous de placer le fichier GeoLite2-Country.mmdb dans ce répertoire (décompressez-le depuis installer/resources/GeoLite2-Country.mmdb.gz). Le fichier hosts.txt peut être nécessaire, vous pouvez le modifier pour inclure tous les hôtes que votre application utilise. Vous pouvez ajouter un fichier router.config au répertoire de base pour remplacer les valeurs par défaut initiales. Examinez et modifiez ou supprimez les fichiers clients.config et i2ptunnel.config.

Les exigences de licence peuvent vous obliger à inclure le fichier LICENSES.txt et le répertoire des licences.

- Vous pouvez également souhaiter inclure un fichier hosts.txt.
- Assurez-vous de spécifier un bootclasspath si vous compilez Java I2P pour votre version, plutôt que d'utiliser nos binaires.

### Considérations pour Android

Note : Cette section se réfère uniquement à Java I2P.

Notre application router Android peut être partagée par plusieurs clients. Si elle n'est pas installée, l'utilisateur sera invité à le faire lorsqu'il démarre une application cliente.

Certains développeurs ont exprimé leur inquiétude que cela constitue une mauvaise expérience utilisateur, et ils souhaitent intégrer le router dans leur application. Nous avons effectivement une bibliothèque de service router Android dans notre feuille de route, qui pourrait faciliter l'intégration. Plus d'informations nécessaires.

Si vous avez besoin d'aide, veuillez nous contacter.

### JARs Maven

Note : Cette section fait référence à Java I2P uniquement.

Nous avons un nombre limité de nos jars sur [Maven Central](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22net.i2p%22). Il existe de nombreux tickets trac que nous devons traiter pour améliorer et étendre les jars publiés sur Maven Central.

Si vous avez besoin d'aide, veuillez nous contacter.

### Considérations sur les datagrammes (DHT)

Si votre application utilise des datagrammes I2P, par exemple pour une DHT, de nombreuses options avancées sont disponibles pour réduire la surcharge et augmenter la fiabilité. Cela peut prendre du temps et nécessiter de l'expérimentation pour bien fonctionner. Soyez conscient des compromis entre taille et fiabilité. Contactez-nous pour obtenir de l'aide. Il est possible - et recommandé - d'utiliser les datagrammes et le streaming sur la même destination. Ne créez pas de destinations séparées pour cela. N'essayez pas de stocker vos données non liées dans les DHT réseau existantes (iMule, bote, bittorrent, et router). Construisez la vôtre. Si vous codez en dur des nœuds d'amorçage, nous recommandons d'en avoir plusieurs.

### Outproxies

Les outproxies I2P vers le clearnet sont une ressource limitée. Utilisez les outproxies uniquement pour la navigation web normale initiée par l'utilisateur ou autre trafic limité. Pour tout autre usage, consultez et obtenez l'approbation de l'opérateur de l'outproxy.

### Co-marketing

Travaillons ensemble. N'attendez pas que ce soit terminé. Donnez-nous votre nom d'utilisateur Twitter et commencez à tweeter à ce sujet, nous vous rendrons la pareille.

### Logiciel malveillant

Veuillez ne pas utiliser I2P à des fins malveillantes. Cela pourrait causer un grand préjudice à notre réseau et à notre réputation.

### Rejoignez-nous

Cela peut paraître évident, mais rejoignez la communauté. Faites fonctionner I2P 24h/24 et 7j/7. Créez un site I2P sur votre projet. Traînez sur IRC #i2p-dev. Postez sur les forums. Faites passer le mot. Nous pouvons vous aider à trouver des utilisateurs, des testeurs, des traducteurs, ou même des développeurs.

---

## Exemples

### Exemples d'applications

Vous pourriez vouloir installer et expérimenter avec l'application I2P Android, et examiner son code, pour un exemple d'application qui intègre le router. Voyez ce que nous exposons à l'utilisateur et ce que nous cachons. Regardez la machine à états que nous utilisons pour démarrer et arrêter le router. D'autres exemples sont : Vuze, l'application Nightweb Android, iMule, TAILS, iCloak, et Monero.

### Exemple de Code

Remarque : Cette section ne concerne que Java I2P.

Rien de ce qui précède ne vous indique réellement comment écrire votre code pour intégrer le router Java, voici donc un bref exemple.

```java
import java.util.Properties;
import net.i2p.router.Router;

	Properties p = new Properties();
        // add your configuration settings, directories, etc.
        // where to find the I2P installation files
	p.addProperty("i2p.dir.base", baseDir);
        // where to find the I2P data files
	p.addProperty("i2p.dir.config", configDir);
        // bandwidth limits in K bytes per second
	p.addProperty("i2np.inboundKBytesPerSecond", "50");
	p.addProperty("i2np.outboundKBytesPerSecond", "50");
	p.addProperty("router.sharePercentage", "80");
	p.addProperty("foo", "bar");
	Router r = new Router(p);
        // don't call exit() when the router stops
	r.setKillVMOnEnd(false);
	r.runRouter();

	...

	r.shutdownGracefully();
	// will shutdown in 11 minutes or less
```
Ce code est pour le cas où votre application démarre le router, comme dans notre application Android. Vous pourriez également faire démarrer l'application par le router via les fichiers clients.config et i2ptunnel.config, conjointement avec les webapps Jetty, comme c'est fait dans nos paquets Java. Comme toujours, la gestion d'état est la partie difficile.

Voir aussi : la javadoc du Router.
