---
title: "Création d'un Eepsite I2P"
description: "Apprenez à créer et héberger votre propre site web sur le réseau I2P à l'aide du serveur web Jetty intégré"
lastUpdated: "2025-11"
toc: true
---

## Qu'est-ce qu'un Eepsite ?

Un **eepsite** est un site web qui réside exclusivement sur le réseau I2P. Contrairement aux sites web traditionnels accessibles via le clearnet (Internet public classique), les eepsites ne sont accessibles que via I2P, garantissant l’anonymat et la confidentialité tant pour l’opérateur du site que pour les visiteurs. Les eepsites utilisent le pseudo-domaine de premier niveau `.i2p` et sont accessibles via des adresses spéciales `.b32.i2p` ou des noms lisibles par des humains enregistrés dans le carnet d’adresses I2P.

Toutes les installations Java d’I2P sont fournies avec [Jetty](https://jetty.org/index.html), un serveur Web léger basé sur Java, préinstallé et préconfiguré. Cela permet de commencer à héberger votre propre eepsite (site web I2P) en quelques minutes - aucune installation logicielle supplémentaire n’est requise.

Ce guide vous expliquera pas à pas comment créer et configurer votre premier eepsite à l'aide des outils intégrés d'I2P.

---

## Étape 1 : Accéder au Gestionnaire des services cachés

Le Gestionnaire des services cachés (également appelé I2P Tunnel Manager) est l'endroit où vous configurez tous les tunnels serveur et client I2P, y compris les serveurs HTTP (eepsites).

1. Ouvrez votre `http://127.0.0.1:7657`
2. Accédez au `http://127.0.0.1:7657/i2ptunnelmgr`

Vous devriez voir l’interface du Gestionnaire des services cachés affichant : - **Messages d’état** - État actuel du tunnel et du client - **Contrôle global des tunnels** - Boutons pour gérer tous les tunnels en même temps - **Services cachés I2P** - Liste des tunnels serveur configurés

![Gestionnaire de services cachés](/images/guides/eepsite/hidden-services-manager.png)

Par défaut, vous verrez une entrée **serveur web I2P** existante, configurée mais non démarrée. Il s’agit du serveur web Jetty préconfiguré, prêt à l’emploi.

---

## Étape 2: Configurez les paramètres de votre serveur Eepsite

Cliquez sur l’entrée **I2P webserver** dans la liste des services cachés pour ouvrir la page de configuration du serveur. C’est ici que vous personnaliserez les paramètres de votre eepsite.

![Paramètres du serveur Eepsite](/images/guides/eepsite/webserver-settings.png)

### Options de configuration expliquées

**Nom** - Il s’agit d’un identifiant interne pour votre tunnel - Utile si vous exécutez plusieurs eepsites afin de savoir lequel est lequel - Par défaut : "I2P webserver"

**Description** - Une brève description de votre eepsite (site web sur I2P) pour votre propre référence - Visible uniquement pour vous dans le Gestionnaire des services cachés - Exemple : "Mon eepsite" ou "Blog personnel"

**Démarrage automatique du Tunnel** - **Important**: Cochez cette case pour démarrer automatiquement votre eepsite lorsque votre router I2P démarre - Garantit que votre site reste disponible sans intervention manuelle après les redémarrages du router - Recommandé: **Activé**

**Cible (Hôte et port)** - **Hôte** : L’adresse locale où votre serveur web s’exécute (par défaut : `127.0.0.1`) - **Port** : Le port sur lequel votre serveur web écoute (par défaut : `7658` pour Jetty) - Si vous utilisez le serveur web Jetty préinstallé, **laissez ces valeurs par défaut** - Ne modifiez ces paramètres que si vous exécutez un serveur web personnalisé sur un port différent

**Nom d’hôte du site Web** - Il s’agit du nom de domaine `.i2p` de votre eepsite, lisible par un humain - Valeur par défaut : `mysite.i2p` (texte indicatif) - Vous pouvez enregistrer un domaine personnalisé comme `stormycloud.i2p` ou `myblog.i2p` - Laissez vide si vous souhaitez uniquement utiliser l’adresse `.b32.i2p` générée automatiquement (pour les outproxies, mandataires sortants) - Voir [Enregistrer votre domaine I2P](#registering-your-i2p-domain) ci‑dessous pour savoir comment obtenir un nom d’hôte personnalisé

**Destination locale** - Il s'agit de l'identifiant cryptographique unique de votre eepsite (adresse de destination) - Généré automatiquement lors de la création initiale du tunnel - Considérez-le comme l'"adresse IP" permanente de votre site sur I2P - La longue chaîne alphanumérique est l'adresse `.b32.i2p` de votre site sous forme encodée

**Fichier de clé privée** - Emplacement où sont stockées les clés privées de votre eepsite (site web hébergé sur I2P) - Par défaut : `eepsite/eepPriv.dat` - **Conservez ce fichier en lieu sûr** - toute personne ayant accès à ce fichier peut se faire passer pour votre eepsite - Ne partagez ni ne supprimez jamais ce fichier

### Remarque importante

L'encadré d'avertissement jaune vous rappelle que, pour activer les fonctionnalités de génération de codes QR ou d'authentification à l'inscription, vous devez configurer un nom d'hôte de site Web avec le suffixe `.i2p` (par exemple, `mynewsite.i2p`).

---

## Étape 3 : Options réseau avancées (facultatif)

Si vous faites défiler vers le bas la page de configuration, vous trouverez des options réseau avancées. **Ces paramètres sont facultatifs** - les valeurs par défaut conviennent à la plupart des utilisateurs. Cependant, vous pouvez les ajuster en fonction de vos exigences en matière de sécurité et de vos besoins en performances.

### Options de longueur des tunnels

![Options de longueur et de quantité des tunnels](/images/guides/eepsite/tunnel-options.png)

**Longueur du tunnel** - **Par défaut** : tunnel à 3 sauts (anonymat élevé) - Contrôle le nombre de sauts de router qu’une requête effectue avant d’atteindre votre eepsite - **Plus de sauts = Anonymat plus élevé, mais des performances plus lentes** - **Moins de sauts = Performances plus rapides, mais anonymat réduit** - Les options vont de 0-3 sauts avec des paramètres de variance - **Recommandation** : Conserver 3 sauts sauf si vous avez des exigences de performances spécifiques

**Variance de tunnel** - **Par défaut**: variance de 0 saut (pas de randomisation, performances constantes) - Ajoute une randomisation à la longueur des tunnels pour une sécurité accrue - Exemple: "variance de 0-1 saut" signifie que les tunnels feront aléatoirement 3 ou 4 sauts - Augmente l'imprévisibilité mais peut entraîner des temps de chargement variables

### Options relatives au nombre de tunnels

**Nombre (Tunnels entrants/sortants)** - **Par défaut**: 2 tunnels entrants, 2 tunnels sortants (bande passante et fiabilité standard) - Contrôle le nombre de tunnels parallèles dédiés à votre eepsite - **Plus de tunnels = Meilleure disponibilité et gestion de la charge, mais utilisation des ressources plus élevée** - **Moins de tunnels = Utilisation des ressources plus faible, mais redondance réduite** - Recommandé pour la plupart des utilisateurs: 2/2 (par défaut) - Les sites à fort trafic peuvent bénéficier de 3/3 ou plus

**Nombre de tunnels de secours** - **Par défaut**: 0 tunnels de secours (aucune redondance, aucune consommation de ressources supplémentaire) - Tunnels de secours en attente qui s'activent si les tunnels principaux défaillent - Augmente la fiabilité mais consomme davantage de bande passante et de CPU - La plupart des eepsites personnels n'ont pas besoin de tunnels de secours

### Limites des requêtes POST

![Configuration des limites POST](/images/guides/eepsite/post-limits.png)

Si votre eepsite comprend des formulaires (formulaires de contact, sections de commentaires, téléversements de fichiers, etc.), vous pouvez configurer des limites pour les requêtes POST afin de prévenir les abus :

**Limites par client** - **Par période**: Nombre maximal de requêtes provenant d’un seul client (par défaut: 6 toutes les 5 minutes) - **Durée de bannissement**: Durée de blocage des clients abusifs (par défaut: 20 minutes)

**Limites totales** - **Total**: Nombre maximal de requêtes POST provenant de tous les clients réunis (par défaut : 20 toutes les 5 minutes) - **Durée du bannissement**: Durée pendant laquelle rejeter toutes les requêtes POST en cas de dépassement de la limite (par défaut : 10 minutes)

**Période de limitation des requêtes POST (méthode HTTP)** - Fenêtre temporelle pour mesurer la fréquence des requêtes (par défaut : 5 minutes)

Ces limites contribuent à protéger contre le spam, les attaques par déni de service et les abus liés à la soumission automatisée de formulaires.

### Quand ajuster les paramètres avancés

- **Site communautaire à fort trafic**: Augmenter le nombre de tunnels (3-4 entrants/sortants)
- **Application critique en termes de performances**: Réduire la longueur des tunnels à 2 sauts (compromis de confidentialité)
- **Anonymat maximal requis**: Conserver 3 sauts, ajouter 0-1 de variation
- **Formulaires avec une utilisation légitime élevée**: Augmenter en conséquence les limites de POST
- **Blog/portfolio personnel**: Utiliser tous les paramètres par défaut

---

## Étape 4 : Ajout de contenu à votre Eepsite

Maintenant que votre eepsite est configuré, vous devez ajouter les fichiers de votre site web (HTML, CSS, images, etc.) dans le répertoire racine du serveur web. L’emplacement varie selon votre système d’exploitation, le type d’installation et l’implémentation I2P.

### Trouver le répertoire racine de votre site

Le **répertoire racine du site** (souvent appelé `docroot`) est le répertoire où vous placez tous les fichiers de votre site web. Votre fichier `index.html` doit être placé directement dans ce répertoire.

#### Java I2P (distribution standard)

**Linux** - **Installation standard**: `~/.i2p/eepsite/docroot/` - **Installation via paquet (exécutée en tant que service)**: `/var/lib/i2p/i2p-config/eepsite/docroot/`

**Windows** - **Installation standard**: `%LOCALAPPDATA%\I2P\eepsite\docroot\`   - Chemin typique: `C:\Users\YourUsername\AppData\Local\I2P\eepsite\docroot\` - **Installation en tant que service Windows**: `%PROGRAMDATA%\I2P\eepsite\docroot\`   - Chemin typique: `C:\ProgramData\I2P\eepsite\docroot\`

**macOS** - **Installation par défaut**: `/Users/YourUsername/Library/Application Support/i2p/eepsite/docroot/`

#### I2P+ (Distribution I2P améliorée)

I2P+ utilise la même structure de répertoires que Java I2P. Suivez les chemins ci-dessus en fonction de votre système d’exploitation.

#### i2pd (Implémentation C++)

**Linux/Unix** - **Par défaut**: `/var/lib/i2pd/eepsite/` ou `~/.i2pd/eepsite/` - Vérifiez votre fichier de configuration `i2pd.conf` pour connaître la valeur effective de `root` dans la section de votre tunnel de serveur HTTP

**Windows** - Vérifiez `i2pd.conf` dans votre répertoire d'installation d'i2pd

**macOS** - Généralement : `~/Library/Application Support/i2pd/eepsite/`

### Ajout des fichiers de votre site web

1. **Accédez à la racine de votre site** à l'aide de votre gestionnaire de fichiers ou du terminal
2. **Créez ou copiez les fichiers de votre site web** dans le dossier `docroot`
   - Au minimum, créez un fichier `index.html` (c'est votre page d'accueil)
   - Ajoutez au besoin des fichiers CSS, JavaScript, des images et d'autres ressources
3. **Organisez les sous-répertoires** comme vous le feriez pour n'importe quel site web :
   ```
   docroot/
   ├── index.html
   ├── about.html
   ├── css/
   │   └── style.css
   ├── images/
   │   └── logo.png
   └── js/
       └── script.js
   ```

### Démarrage rapide : exemple HTML simple

Si vous commencez tout juste, créez un fichier `index.html` simple dans votre dossier `docroot` :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My I2P Eepsite</title>
</head>
<body>
    <h1>Welcome to My Eepsite!</h1>
    <p>This is my first website on the I2P network.</p>
    <p>Privacy-focused and decentralized!</p>
</body>
</html>
```
### Autorisations (Linux/Unix/macOS)

Si vous exécutez I2P en tant que service ou sous un autre utilisateur, assurez-vous que le processus I2P dispose d’un accès en lecture à vos fichiers :

```bash
# Set appropriate ownership (if running as i2p user)
sudo chown -R i2p:i2p /var/lib/i2p/i2p-config/eepsite/docroot/

# Or set readable permissions for all users
chmod -R 755 ~/.i2p/eepsite/docroot/
```
### Conseils

- **Contenu par défaut**: Lorsque vous installez I2P pour la première fois, du contenu d'exemple est déjà présent dans le dossier `docroot` - n'hésitez pas à le remplacer
- **Les sites statiques fonctionnent le mieux**: Bien que Jetty prenne en charge les servlets et JSP, les sites simples en HTML/CSS/JavaScript sont les plus faciles à maintenir
- **Serveurs web externes**: Les utilisateurs avancés peuvent exécuter des serveurs web personnalisés (Apache, Nginx, Node.js, etc.) sur différents ports et faire pointer le tunnel I2P vers eux

---

## Étape 5: Démarrer votre Eepsite

Maintenant que votre eepsite est configuré et comporte du contenu, il est temps de le démarrer et de le rendre accessible sur le réseau I2P.

### Démarrer le Tunnel

1. **Retournez au `http://127.0.0.1:7657/i2ptunnelmgr`**
2. Trouvez l’entrée de votre **serveur web I2P** dans la liste
3. Cliquez sur le bouton **Démarrer** dans la colonne Contrôle

![Eepsite en cours d'exécution](/images/guides/eepsite/eepsite-running.png)

### Attendre l’établissement du tunnel

Après avoir cliqué sur Démarrer, le tunnel de votre eepsite commencera à se mettre en place. Ce processus prend généralement **30 à 60 secondes**. Surveillez l'indicateur d'état:

- **Voyant rouge** = Tunnel en cours de démarrage/construction
- **Voyant jaune** = Tunnel partiellement établi
- **Voyant vert** = Tunnel pleinement opérationnel et prêt

Dès que vous voyez le **voyant vert**, votre eepsite est en ligne sur le réseau I2P !

### Accédez à votre Eepsite

Cliquez sur le bouton **Preview** à côté de votre eepsite en cours d’exécution (site web sur I2P). Cela ouvrira un nouvel onglet du navigateur avec l’adresse de votre eepsite.

Votre eepsite a deux types d'adresses :

1. **Adresse Base32 (.b32.i2p)**: Une longue adresse cryptographique qui ressemble à :
   ```
   `http://fcyianvr325tdgiiueyg4rsq4r5iuibzovl26msox5ryoselykpq.b32.i2p`
   ```
   - Il s’agit de l’adresse permanente de votre eepsite, dérivée cryptographiquement
   - Elle ne peut pas être modifiée et est liée à votre clé privée
   - Fonctionne toujours, même sans enregistrement de domaine

2. **Domaine lisible par l'humain (.i2p)**: Si vous définissez un nom d'hôte de site web (p. ex., `testwebsite.i2p`)
   - Ne fonctionne qu'après l'enregistrement du domaine (voir la section suivante)
   - Plus facile à mémoriser et à partager
   - Pointe vers votre adresse .b32.i2p

Le bouton **Copier le nom d’hôte** vous permet de copier rapidement votre adresse `.b32.i2p` complète pour la partager.

---

## ⚠️ Critique : sauvegardez votre clé privée

Avant d'aller plus loin, vous **devez impérativement sauvegarder** le fichier de clé privée de votre eepsite. C'est d'une importance cruciale pour plusieurs raisons :

### Pourquoi sauvegarder votre clé ?

**Votre clé privée (`eepPriv.dat`) est l'identité de votre eepsite.** Elle détermine votre adresse `.b32.i2p` et prouve que vous êtes le propriétaire de votre eepsite.

- **Clé = adresse .b32**: Votre clé privée génère mathématiquement votre adresse .b32.i2p unique
- **Ne peut pas être récupérée**: Si vous perdez votre clé, vous perdez définitivement l'adresse de votre eepsite
- **Ne peut pas être modifiée**: Si vous avez enregistré un domaine pointant vers une adresse .b32, **il n'y a aucun moyen de la mettre à jour** - l'enregistrement est permanent
- **Requise pour la migration**: Passer à un nouvel ordinateur ou réinstaller I2P nécessite cette clé pour conserver la même adresse
- **Prise en charge du multihoming (hébergement multi-emplacements)**: Héberger votre eepsite depuis plusieurs emplacements nécessite la même clé sur chaque serveur

### Où se trouve la clé privée ?

Par défaut, votre clé privée est stockée à l’emplacement suivant : - **Linux**: `~/.i2p/eepsite/eepPriv.dat` (ou `/var/lib/i2p/i2p-config/eepsite/eepPriv.dat` pour les installations en tant que service) - **Windows**: `%LOCALAPPDATA%\I2P\eepsite\eepPriv.dat` ou `%PROGRAMDATA%\I2P\eepsite\eepPriv.dat` - **macOS**: `/Users/YourUsername/Library/Application Support/i2p/eepsite/eepPriv.dat`

Vous pouvez également vérifier/modifier ce chemin dans la configuration de votre tunnel sous "Private Key File".

### Comment sauvegarder

1. **Arrêtez votre tunnel** (facultatif, mais plus sûr)
2. **Copiez `eepPriv.dat`** dans un emplacement sécurisé:
   - Disque USB externe
   - Disque de sauvegarde chiffré
   - Archive protégée par mot de passe
   - Stockage cloud sécurisé (chiffré)
3. **Conservez plusieurs sauvegardes** à des emplacements physiques différents
4. **Ne partagez jamais ce fichier** - quiconque le possède peut se faire passer pour votre eepsite

### Restaurer à partir d'une sauvegarde

Pour restaurer votre eepsite sur un nouveau système ou après une réinstallation :

1. Installez I2P et créez/configurez les paramètres de votre tunnel
2. **Arrêtez le tunnel** avant de copier la clé
3. Copiez votre `eepPriv.dat` sauvegardé à l’emplacement correct
4. Démarrez le tunnel - il utilisera votre adresse .b32 d’origine

---

## Si vous n'enregistrez pas de domaine

**Félicitations !** Si vous ne prévoyez pas d'enregistrer un nom de domaine `.i2p` personnalisé, votre eepsite est désormais complet et opérationnel.

Vous pouvez : - Partager votre adresse `.b32.i2p` avec d’autres - Accéder à votre site via le réseau I2P en utilisant n’importe quel navigateur compatible I2P - Mettre à jour les fichiers de votre site dans le dossier `docroot` à tout moment - Surveiller l’état de votre tunnel dans le Hidden Services Manager (gestionnaire des services cachés)

**Si vous souhaitez un nom de domaine lisible par un humain** (comme `mysite.i2p` plutôt qu'une longue adresse .b32), passez à la section suivante.

---

## Enregistrement de votre domaine I2P

Un domaine `.i2p` lisible par un humain (comme `testwebsite.i2p`) est bien plus facile à mémoriser et à partager qu’une longue adresse `.b32.i2p`. L’enregistrement d’un domaine est gratuit et associe le nom choisi à l’adresse cryptographique de votre eepsite.

### Prérequis

- Votre eepsite doit être en cours d’exécution avec un voyant vert
- Vous devez avoir défini un **Nom d’hôte du site Web** dans la configuration de votre tunnel (Étape 2)
- Exemple : `testwebsite.i2p` ou `myblog.i2p`

### Étape 1 : Générer la chaîne d'authentification

1. **Revenez à la configuration de votre tunnel** dans le Gestionnaire de services cachés
2. Cliquez sur l’entrée de votre **serveur web I2P** pour ouvrir les paramètres
3. Faites défiler vers le bas pour trouver le bouton **Authentification d’enregistrement**

![Authentification de l'inscription](/images/guides/eepsite/registration-authentication.png)

4. Cliquez sur **Authentification d’enregistrement**
5. **Copiez l’intégralité de la chaîne d’authentification** affichée pour « Authentication for adding host [yourdomainhere] »

La chaîne d’authentification ressemblera à :

```
testwebsite.i2p=I8WiuSx1TcYAutCrhLveZ6gghdqsIJ1v9noSGPb7ItYjxaK5LHVNxgC60KuEu95nqCCF2qwgnW~2ehIY9vsi1iPForksdU3GALrQq4S73meoIIXarCCdb~Z6Ehj2-yLWI8WiuSx1TcYAutCrhLveZ6gghdqsIJ1v9noSGPb7ItYjxaK5LHVNxgC60KuEu95nqCCF2qwgnW~2ehIY9vsi1iPForksdU3GALrQq4S73meoIIXarCCdb~Z6Ehj2-yLWI8WiuSx1TcYAutCrhLveZ6gghdqsIJ1v9noSGPb7ItYjxaK5LHVNxgC60KuEu95nqCCF2qwgnW~2ehIY9vsi1iPForksdU3GALrQq4S73meoIIXarCCdb~Z6Ehj2-yLWI8WiuSx1TcYAutCrhLveZ6gghdqsIJ1v9noSGPb7ItYjxaK5LHVNxgC60KuEu95nqCCF2qwgnW~2ehIY9vsi1uNxFZ0HN7tQbbVj1pmbahepQZNxEW0ufwnMYAoFo8opBQAEAAcAAA==#!date=1762104890#sig=9DjEfrcNRxsoSxiE0Mp0-7rH~ktYWtgwU8c4J0eSo0VHbGxDxdiO9D1Cvwcx8hkherMO07UWOC9BWf-1wRyUAw==
```
Cette chaîne contient : - Votre nom de domaine (`testwebsite.i2p`) - Votre adresse de destination (le long identifiant cryptographique) - Un horodatage - Une signature cryptographique prouvant que vous possédez la clé privée

**Conservez cette chaîne d’authentification** - vous en aurez besoin pour les deux services d’inscription.

### Étape 2 : S'inscrire sur stats.i2p

1. **Accédez à** stats.i2p Ajouter une clé (au sein d'I2P)

![Enregistrement du domaine stats.i2p](/images/guides/eepsite/stats-i2p-add.png)

2. **Collez la chaîne d'authentification** dans le champ "Authentication String"
3. **Ajoutez votre nom** (facultatif) - par défaut "Anonymous"
4. **Ajoutez une description** (recommandée) - décrivez brièvement l'objet de votre eepsite (site I2P)
   - Exemple : "Nouvel I2P Eepsite", "Blog personnel", "Service de partage de fichiers"
5. **Cochez "HTTP Service?"** s'il s'agit d'un site web (laissez coché pour la plupart des eepsites)
   - Décochez pour IRC, NNTP, serveurs proxy, XMPP, git, etc.
6. Cliquez sur **Submit**

Si tout s’est bien passé, vous verrez un message de confirmation indiquant que votre domaine a été ajouté au carnet d’adresses de stats.i2p.

### Étape 3 : S’inscrire sur reg.i2p

Pour garantir une disponibilité maximale, vous devriez également vous inscrire auprès du service reg.i2p :

1. **Accédez à** reg.i2p Ajouter un domaine (dans I2P)

![Enregistrement de domaine reg.i2p](/images/guides/eepsite/reg-i2p-add.png)

2. **Collez la même chaîne d'authentification** dans le champ "Auth string"
3. **Ajoutez une description** (facultatif mais recommandé)
   - Cela aide les autres utilisateurs I2P à comprendre ce que votre site propose
4. Cliquez sur **Submit**

Vous devriez recevoir une confirmation de l’enregistrement de votre domaine.

### Étape 4 : Attendre la propagation

Après avoir soumis votre demande aux deux services, votre enregistrement de domaine se propagera à travers le système de carnet d’adresses du réseau I2P.

**Chronologie de la propagation**: - **Enregistrement initial**: Immédiat sur les services d'enregistrement - **Propagation à l'échelle du réseau**: De plusieurs heures à 24+ heures - **Disponibilité complète**: Peut prendre jusqu'à 48 heures pour que tous les routers se mettent à jour

**C'est normal !** Le système de carnet d'adresses I2P se met à jour périodiquement, pas instantanément. Votre eepsite fonctionne - les autres utilisateurs doivent simplement recevoir le carnet d'adresses mis à jour.

### Vérifiez votre domaine

Après quelques heures, vous pouvez tester votre domaine :

1. **Ouvrez un nouvel onglet** dans votre navigateur I2P
2. Essayez d'accéder directement à votre domaine : `http://yourdomainname.i2p`
3. S'il se charge, votre domaine est enregistré et se propage !

Si cela ne fonctionne pas encore : - Patientez davantage (les carnets d’adresses se mettent à jour selon leur propre calendrier) - Le carnet d’adresses de votre router peut avoir besoin de temps pour se synchroniser - Essayez de redémarrer votre router I2P pour forcer une mise à jour du carnet d’adresses

### Remarques importantes

- **L’enregistrement est permanent**: Une fois enregistré et propagé, votre domaine pointe de façon permanente vers votre adresse `.b32.i2p`
- **Impossible de changer la destination**: Vous ne pouvez pas modifier l’adresse `.b32.i2p` vers laquelle pointe votre domaine - c’est pourquoi la sauvegarde de `eepPriv.dat` est cruciale
- **Propriété du domaine**: Seul le détenteur de la clé privée peut enregistrer ou mettre à jour le domaine
- **Service gratuit**: L’enregistrement de domaine sur I2P est gratuit, géré par la communauté et décentralisé
- **Plusieurs bureaux d’enregistrement**: L’enregistrement auprès de stats.i2p et de reg.i2p augmente la fiabilité et la vitesse de propagation

---

## Félicitations !

Votre eepsite I2P est désormais pleinement opérationnel avec un domaine enregistré !

**Prochaines étapes**: - Ajoutez davantage de contenu à votre dossier `docroot` - Partagez votre domaine avec la communauté I2P - Conservez la sauvegarde de votre `eepPriv.dat` en lieu sûr - Surveillez régulièrement l'état de votre tunnel - Envisagez de rejoindre les forums I2P ou IRC pour promouvoir votre site

Bienvenue sur le réseau I2P ! 🎉
