---
title: "Installation d'I2P sur Windows"
description: "Choisissez votre méthode d'installation Windows : Easy Install Bundle ou Installation Standard"
lastUpdated: "2025-11"
toc: true
---

## Choisissez Votre Méthode d'Installation

Il existe deux façons d'installer I2P sur Windows. Choisissez la méthode qui correspond le mieux à vos besoins :

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin: 2rem 0;">

<div style="border: 2px solid #22c55e; border-radius: 8px; padding: 1.5rem; background: var(--background-secondary);">

IMPORTANT :  NE posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte est seulement un titre ou semble incomplet, traduisez-le tel quel.

### 🚀 Easy Install Bundle (Recommended)

**Idéal pour la plupart des utilisateurs**

✅ Programme d'installation tout-en-un ✅ Java inclus (aucune installation séparée) ✅ Profils Firefox inclus ✅ Configuration la plus rapide

**Choisissez ceci si :** - Vous souhaitez l'installation la plus simple - Vous n'avez pas Java installé - Vous débutez avec I2P

<a href="#easy-install-bundle" style="display: inline-block; background: #22c55e; color: white; padding: 0.75rem 1.5rem; border-radius: 4px; text-decoration: none; font-weight: bold; margin-top: 1rem;">Guide d'installation facile →</a>

</div>

<div style="border: 2px solid #1e40af; border-radius: 8px; padding: 1.5rem; background: var(--background-secondary);">

IMPORTANT :  NE posez PAS de questions, ne fournissez PAS d'explications, et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

### 🚀 Bundle d'Installation Facile (Recommandé)

**Pour les utilisateurs avancés**

📦 Programme d'installation JAR basé sur Java 🔧 Plus de contrôle sur l'installation 💾 Taille de téléchargement réduite

**Choisissez cette option si :** - Vous avez déjà Java installé - Vous souhaitez plus de contrôle - Vous préférez la méthode traditionnelle

<a href="#standard-installation" style="display: inline-block; background: #1e40af; color: white; padding: 0.75rem 1.5rem; border-radius: 4px; text-decoration: none; font-weight: bold; margin-top: 1rem;">Guide d'installation standard →</a>

</div>

</div>

---

## Easy Install Bundle

### ⚙️ Installation Standard

Le **I2P Easy Install Bundle** est la méthode d'installation recommandée pour les utilisateurs Windows. Ce programme d'installation tout-en-un inclut tout ce dont vous avez besoin pour commencer avec I2P :

- **I2P Router** - Le logiciel I2P principal
- **Embedded Java Runtime** - Aucune installation Java séparée requise
- **Profils et extensions Firefox** - Profils de navigateur et extensions optimisés pour I2P pour une navigation sécurisée
- **Installateur simple** - Aucune configuration manuelle requise
- **Mises à jour automatiques** - Maintenez votre logiciel I2P à jour

Cet installateur bêta simplifie le processus d'installation en incluant Java directement, vous n'avez donc pas besoin de télécharger ou configurer Java séparément.

---

**IMPORTANT :**  NE posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

## Step 1: Select Your Language

Après avoir lancé l'installateur Easy Install Bundle, vous serez accueilli par l'écran de sélection de la langue.

![Sélection de la langue](/images/guides/windows-install/language-selection.png)

1. **Choisissez votre langue préférée** dans le menu déroulant
   - Les langues disponibles incluent l'anglais, l'allemand, l'espagnol, le français et bien d'autres
2. Cliquez sur **OK** pour continuer

L'interface d'installation utilisera la langue que vous avez sélectionnée pour toutes les étapes suivantes.

# Options générales

## Bundle d'Installation Facile

Ensuite, les informations de licence d'I2P vous seront présentées. Le Bundle d'Installation Facile inclut des composants sous diverses licences libres et open source.

![Contrat de licence](/images/guides/windows-install/license-agreement.png)

**Pour continuer l'installation** : 1. Examinez les informations de licence (facultatif mais recommandé) 2. Cliquez sur **J'accepte** pour accepter les licences et continuer 3. Cliquez sur **Annuler** si vous ne souhaitez pas installer

---

IMPORTANT :  Ne posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

## Step 3: Choose Installation Folder

Vous allez maintenant sélectionner où installer I2P sur votre ordinateur.

![Sélection du dossier d'installation](/images/guides/windows-install/installation-folder.png)

**Options d'installation** :

1. **Utiliser l'emplacement par défaut** (recommandé)
   - Chemin par défaut : `C:\Users\[YourUsername]\AppData\Local\I2peasy\`
   - Cela installe I2P dans le répertoire de votre profil utilisateur
   - Aucun privilège administrateur requis pour les mises à jour

2. **Choisir un emplacement personnalisé**
   - Cliquez sur **Parcourir...** pour sélectionner un dossier différent
   - Utile si vous souhaitez installer sur un autre lecteur
   - Assurez-vous d'avoir les permissions d'écriture sur le dossier sélectionné

**Besoins en espace disque** : - L'installateur indique l'espace nécessaire (généralement moins de 1 Go) - Vérifiez que vous disposez de suffisamment d'espace libre sur le disque sélectionné

3. Cliquez sur **Install** pour commencer le processus d'installation

L'installateur va maintenant copier tous les fichiers nécessaires vers l'emplacement que vous avez choisi. Cela peut prendre quelques minutes.

---

## Étape 1 : Sélectionnez votre langue

Une fois l'installation terminée, vous verrez l'écran de finalisation.

![Installation terminée](/images/guides/windows-install/installation-complete.png)

L'assistant d'installation confirme que « I2P - i2peasy a été installé sur votre ordinateur. »

**Important** : Assurez-vous que la case **"Start I2P?"** est cochée (elle devrait être cochée par défaut).

- **Coché** (recommandé) : I2P démarrera automatiquement lorsque vous cliquerez sur Terminer
- **Décoché** : Vous devrez démarrer I2P manuellement plus tard depuis le menu Démarrer ou le raccourci du bureau

Cliquez sur **Terminer** pour finaliser l'installation et lancer I2P.

---

IMPORTANT :  NE posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

## Étape 2 : Accepter le contrat de licence

Après avoir cliqué sur Terminer avec « Démarrer I2P ? » coché :

1. **Le router I2P démarre** - Le router I2P commence à s'exécuter en arrière-plan
2. **L'icône de la barre système apparaît** - Recherchez l'icône I2P dans votre barre système Windows (coin inférieur droit)
3. **La console du router s'ouvre** - Votre navigateur web par défaut s'ouvrira automatiquement sur la console du router I2P (généralement à `http://127.0.0.1:7657`)
4. **Connexion initiale** - I2P commencera à se connecter au réseau et à construire des tunnels (cela peut prendre 5 à 10 minutes au premier lancement)

**Félicitations !** I2P est maintenant installé et fonctionne sur votre ordinateur Windows.

---

IMPORTANT :  NE posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

## Étape 3 : Choisir le dossier d'installation

Bien que ce ne soit pas strictement requis, **le transfert de port améliore considérablement votre expérience I2P** en permettant à votre routeur de communiquer plus efficacement avec les autres routeurs I2P. Sans le transfert de port, vous pourrez toujours utiliser I2P, mais avec des performances réduites et une contribution moindre au réseau.

### Why Forward a Port?

- **Meilleure connectivité** : Permet les connexions entrantes depuis d'autres routeurs I2P
- **Intégration plus rapide** : Vous aide à vous intégrer au réseau plus rapidement
- **Contribution au réseau** : Fait de vous un meilleur participant du réseau I2P
- **Performances améliorées** : Résulte généralement en une meilleure fiabilité et vitesse des tunnels

### Qu'est-ce que le Bundle d'Installation Facile ?

Tout d'abord, vous devez identifier quel port I2P utilise (il est attribué aléatoirement par défaut).

1. **Localisez l'icône I2P** dans la barre d'état système Windows (zone de notification) en bas à droite de votre écran

![Menu de la barre d'état système I2P](/images/guides/windows-install/system-tray-menu.png)

2. **Faites un clic droit sur l'icône I2P** pour ouvrir le menu contextuel
3. **Cliquez sur "Launch I2P Browser"** pour ouvrir la console du routeur I2P

Le menu affiche également des options utiles telles que : - **Network: Firewalled** - Affiche l'état actuel de votre réseau - **Configure I2P System Tray** - Personnaliser les paramètres de l'icône de la barre d'état système - **Stop I2P** / **Stop I2P Immediately** - Options d'arrêt

### Finding Your Port Numbers

Une fois que le navigateur I2P s'ouvre, vous devez vérifier quels ports I2P utilise :

1. **Accédez à la page de configuration réseau** :
   - Rendez-vous sur `http://127.0.0.1:7657/confignet` dans votre navigateur
   - Ou depuis la barre latérale de la console du router : **Configuration → Réseau**

2. **Faites défiler vers le bas** jusqu'à la section de configuration des ports

![Configuration des ports I2P](/images/guides/windows-install/port-configuration.png)

3. **Notez les numéros de port** affichés :

**Configuration UDP** :    - **Port UDP** : Le port affiché ici (exemple : `13697`)    - Par défaut, celui-ci est défini sur "Spécifier le port" avec un numéro attribué aléatoirement

**Configuration TCP** :    - **Port TCP accessible de l'extérieur** : Généralement configuré pour utiliser le même port qu'UDP    - Dans l'exemple ci-dessus : "Utiliser le même port configuré pour UDP (actuellement 13697)"

**Important** : Vous devez rediriger **à la fois UDP et TCP** sur le même numéro de port (dans cet exemple, le port `13697`) dans votre routeur/pare-feu.

### How to Forward Your Port

Comme chaque routeur et pare-feu est différent, nous ne pouvons pas fournir d'instructions universelles. Cependant, [portforward.com](https://portforward.com/) propose des guides détaillés pour des milliers de modèles de routeurs :

1. Visitez **[portforward.com](https://portforward.com/)**
2. Sélectionnez le fabricant et le modèle de votre routeur
3. Suivez le guide étape par étape pour rediriger votre port
4. Redirigez **les protocoles UDP et TCP** sur le numéro de port indiqué dans votre configuration I2P

**Étapes générales** (varie selon le routeur) : - Connectez-vous à l'interface d'administration de votre routeur (généralement à `192.168.1.1` ou `192.168.0.1`) - Trouvez la section "Redirection de ports" ou "Serveurs virtuels" - Créez une nouvelle règle de redirection de port pour votre numéro de port I2P - Configurez les protocoles UDP et TCP - Dirigez la règle vers l'adresse IP locale de votre ordinateur - Enregistrez la configuration

Après avoir transféré votre port, I2P devrait passer de « Réseau : Pare-feu » à « Réseau : OK » dans le menu de la barre système (cela peut prendre quelques minutes).

---

## Étape 4 : Terminer l'installation et démarrer I2P

- **Attendez l'intégration** : Accordez à I2P 5 à 10 minutes pour s'intégrer au réseau et construire les tunnels
- **Configurez votre navigateur** : Utilisez le profil Firefox inclus pour naviguer sur I2P
- **Transférez votre port** : Consultez [portforward.com](https://portforward.com/) pour des instructions spécifiques à votre routeur sur la façon de transférer le port utilisé par I2P
- **Explorez la console du router** : Découvrez les fonctionnalités, services et options de configuration d'I2P
- **Visitez des eepsites** : Essayez d'accéder à des sites web `.i2p` via le réseau I2P
- **Lisez la documentation** : Consultez la [documentation I2P](/docs/) pour plus d'informations

Bienvenue sur le réseau I2P ! 🎉

---

## Que se passe-t-il ensuite

### What is the Standard Installation?

L'**installation standard d'I2P** est la méthode traditionnelle d'installation d'I2P sur Windows. Contrairement au Easy Install Bundle, cette méthode nécessite que vous :

- **Installer Java séparément** - Téléchargez et installez l'environnement d'exécution Java (JRE) avant d'installer I2P
- **Exécuter l'installateur JAR** - Utilisez l'installateur graphique basé sur Java
- **Configurer manuellement** - Configurez vous-même les paramètres du navigateur (optionnel)

Cette méthode est recommandée pour : - Les utilisateurs qui ont déjà Java installé - Les utilisateurs avancés qui souhaitent plus de contrôle sur l'installation - Les utilisateurs qui préfèrent la méthode d'installation traditionnelle - Les systèmes où le bundle Easy Install n'est pas compatible

---

IMPORTANT :  NE posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

## Recommandé : Redirection de port (Optionnel mais Important)

Avant d'installer I2P, vous devez avoir Java installé sur votre système.

### Java Requirements

- **Version Java** : Java 8 (1.8) ou supérieur requis
- **Recommandé** : Java 11 ou ultérieur (version LTS)
- **Type** : Java Runtime Environment (JRE) ou Java Development Kit (JDK)

### Installing Java

Si vous n'avez pas encore Java installé, vous pouvez le télécharger depuis plusieurs sources :

**Option 1 : Oracle Java** - Source officielle : [java.com/download](https://www.java.com/download) - Distribution la plus largement utilisée

**Option 2 : OpenJDK** - Implémentation open-source : [openjdk.org](https://openjdk.org) - Gratuit et open-source

**Option 3 : Adoptium (Eclipse Temurin)** - Alternative recommandée : [adoptium.net](https://adoptium.net) - Versions LTS gratuites, open-source et bien maintenues

**Pour vérifier que Java est installé** : 1. Ouvrez l'Invite de commandes (appuyez sur `Windows + R`, tapez `cmd`, appuyez sur Entrée) 2. Tapez : `java -version` 3. Vous devriez voir s'afficher la version de Java installée

---

**IMPORTANT :**  NE posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

## Step 1: Install Java

Avant d'installer I2P, vous devez installer Java sur votre système.

1. **Choisissez une distribution Java** :
   - **Oracle Java** : [java.com/download](https://www.java.com/download)
   - **OpenJDK** : [openjdk.org](https://openjdk.org)
   - **Adoptium** : [adoptium.net](https://adoptium.net)

2. **Téléchargez le programme d'installation Windows** pour la distribution de votre choix

3. **Exécutez le programme d'installation** et suivez les instructions d'installation

4. **Vérifier l'installation** :
   - Ouvrir l'Invite de commandes
   - Taper `java -version` et appuyer sur Entrée
   - Confirmer que Java 8 ou version ultérieure est installé

Une fois Java installé, vous êtes prêt à installer I2P.

---

IMPORTANT :  NE posez PAS de questions, ne fournissez PAS d'explications, et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

## Step 2: Download and Launch the I2P Installer

1. **Télécharger le programme d'installation I2P** :
   - Visitez la [page de téléchargements I2P](/downloads/)
   - Téléchargez le **programme d'installation Windows** (fichier JAR) : `i2pinstall_X.X.X.jar`
   - Enregistrez-le dans un emplacement facilement accessible (par exemple, le dossier Téléchargements)

2. **Lancer l'installateur** :
   - Double-cliquez sur le fichier JAR téléchargé pour lancer l'installateur
   - Si le double-clic ne fonctionne pas, faites un clic droit sur le fichier et sélectionnez « Ouvrir avec → Java(TM) Platform SE binary »
   - Alternativement, ouvrez l'invite de commandes et exécutez : `java -jar i2pinstall_X.X.X.jar`

## Step 3: Select Your Language

Après avoir lancé l'installateur, vous verrez la boîte de dialogue de sélection de langue.

![Sélection de la langue](/images/guides/windows-standard-install/language-selection.png)

1. **Sélectionnez votre langue préférée** dans le menu déroulant
   - Les langues disponibles incluent l'anglais, l'allemand, l'espagnol, le français et bien d'autres
2. Cliquez sur **OK** pour continuer

L'installateur utilisera la langue que vous avez sélectionnée pour toutes les étapes suivantes.

---

IMPORTANT :  NE posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

## Step 4: Welcome to I2P Installation

![Écran de bienvenue](/images/guides/windows-standard-install/welcome-screen.png)

Ceci est l'**Étape 1 sur 8** du processus d'installation.

Cliquez sur **Next** pour continuer l'installation.

---

IMPORTANT :  NE posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

## Prochaines étapes

![Contrat de licence](/images/guides/windows-standard-install/license-agreement.png)

Il s'agit de l'**étape 2 sur 8** du processus d'installation.

Cliquez sur **Suivant** pour accepter la licence et continuer.

---

IMPORTANT :  NE posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte est simplement un titre ou semble incomplet, traduisez-le tel quel.

## Installation Standard

Choisissez l'emplacement où vous souhaitez installer I2P sur votre ordinateur.

![Chemin d'installation](/images/guides/windows-standard-install/installation-path.png)

**Chemin d'installation par défaut** : `C:\Program Files (x86)\i2p\`

Vous pouvez soit : - Utiliser l'emplacement par défaut (recommandé) - Cliquer sur **Parcourir...** pour sélectionner un dossier différent

Il s'agit de **l'étape 3 sur 8** du processus d'installation.

Cliquez sur **Suivant** pour continuer.

**Remarque** : Si c'est la première fois que vous installez I2P, une fenêtre contextuelle confirmera la création du répertoire :

![Popup de création de répertoire](/images/guides/windows-standard-install/directory-creation-popup.png)

Cliquez sur **OK** pour créer le répertoire d'installation.

---

IMPORTANT :  NE posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

## Step 7: Select Installation Packs

Choisissez les composants à installer.

![Sélectionner les packs](/images/guides/windows-standard-install/select-packs.png)

**Important** : Assurez-vous que les deux packs sont sélectionnés : - **Base** (requis) - Logiciel I2P principal (27,53 MB) - **Windows Service** (recommandé) - Démarrer automatiquement I2P au démarrage

L'option **Service Windows** garantit que I2P démarre automatiquement au démarrage de votre ordinateur, vous n'avez donc pas besoin de le lancer manuellement à chaque fois.

Il s'agit de l'**Étape 4 sur 8** du processus d'installation.

Cliquez sur **Suivant** pour continuer.

---


## Prérequis

L'installateur va maintenant copier les fichiers sur votre système.

![Progression de l'installation](/images/guides/windows-standard-install/installation-progress.png)

Vous verrez deux barres de progression : - **Progression de l'installation du pack** : Affiche le pack en cours d'installation - **Progression globale de l'installation** : Affiche la progression globale (par ex., « 2 / 2 »)

Il s'agit de l'**étape 5 sur 8** du processus d'installation.

Attendez que l'installation se termine, puis cliquez sur **Suivant**.

---

## Step 9: Setup Shortcuts

Configurez l'emplacement où vous souhaitez créer les raccourcis I2P.

![Configuration des raccourcis](/images/guides/windows-standard-install/setup-shortcuts.png)

**Options de raccourci** : - ✓ **Créer des raccourcis dans le menu Démarrer** (recommandé) - ✓ **Créer des raccourcis supplémentaires sur le bureau** (facultatif)

**Groupe de programmes** : Sélectionnez ou créez un nom de dossier pour les raccourcis - Par défaut : `I2P` - Vous pouvez choisir un groupe de programmes existant ou en créer un nouveau

**Créer un raccourci pour** : - **Utilisateur actuel** - Seul vous pouvez accéder aux raccourcis - **Tous les utilisateurs** - Tous les utilisateurs du système peuvent accéder aux raccourcis (nécessite des privilèges administrateur)

Ceci est l'**étape 6 sur 8** du processus d'installation.

Cliquez sur **Suivant** pour continuer.

---

IMPORTANT :  Ne posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

## Step 10: Installation Complete

L'installation est maintenant terminée !

![Installation Complete](/images/guides/windows-standard-install/installation-complete.png)

Vous verrez : - ✓ **L'installation s'est terminée avec succès** - **Un programme de désinstallation sera créé dans** : `C:\Program Files (x86)\i2p\Uninstaller`

Il s'agit de l'**étape 8 sur 8** - la dernière étape du processus d'installation.

Cliquez sur **Terminé** pour finaliser.

---

IMPORTANT :  NE posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

## Étape 1 : Installer Java

Après avoir cliqué sur Terminé :

1. **Le routeur I2P démarre** - Si vous avez installé le service Windows, I2P démarrera automatiquement
2. **La console du routeur s'ouvre** - Votre navigateur web par défaut ouvrira la console du routeur I2P à l'adresse `http://127.0.0.1:7657`
3. **Connexion initiale** - I2P commencera à se connecter au réseau et à construire des tunnels (cela peut prendre 5 à 10 minutes au premier lancement)

**Félicitations !** I2P est maintenant installé sur votre ordinateur Windows.

---

## Étape 2 : Télécharger et lancer l'installateur I2P

Si I2P ne démarre pas automatiquement, ou si vous devez le démarrer manuellement à l'avenir, vous avez deux options :

### Option 1: Start Menu

![Menu Démarrer Windows](/images/guides/windows-standard-install/start-menu.png)

1. Ouvrez le **Menu Démarrer de Windows**
2. Accédez au dossier **I2P**
3. Choisissez l'une des options de démarrage :
   - **I2P router console** - Ouvre la console du routeur dans votre navigateur
   - **Start I2P (no window)** - Démarre I2P silencieusement en arrière-plan
   - **Start I2P (restartable)** - Démarre I2P avec la capacité de redémarrage automatique

Vous pouvez également accéder au **Dossier de profil I2P ouvert (service)** pour consulter les fichiers de configuration d'I2P.

### Pourquoi transférer un port ?

![Windows Services](/images/guides/windows-standard-install/windows-services.png)

1. Appuyez sur **Windows + R** pour ouvrir la boîte de dialogue Exécuter
2. Tapez `services.msc` et appuyez sur Entrée
3. Faites défiler vers le bas pour trouver **I2P Service**
4. Cliquez avec le bouton droit sur **I2P Service** et sélectionnez :
   - **Démarrer** - Démarrer le service I2P
   - **Arrêter** - Arrêter le service I2P
   - **Redémarrer** - Redémarrer le service I2P
   - **Propriétés** - Configurer les paramètres du service (type de démarrage, etc.)

La méthode des Services Windows est utile pour gérer I2P en tant que service en arrière-plan, en particulier si vous l'avez installé en tant que Service Windows.

---

IMPORTANT :  NE posez PAS de questions, ne fournissez PAS d'explications et n'ajoutez AUCUN commentaire. Même si le texte n'est qu'un titre ou semble incomplet, traduisez-le tel quel.

## Étape 3 : Sélectionnez votre langue

- **Attendre l'intégration** : Laissez à I2P 5 à 10 minutes pour s'intégrer au réseau et construire des tunnels
- **Configurer la redirection de port** : Consultez le [guide de redirection de port](#recommended-port-forwarding-optional-but-important) pour les instructions
- **Configurer votre navigateur** : Paramétrez votre navigateur web pour utiliser le proxy HTTP d'I2P
- **Explorer la console du routeur** : Découvrez les fonctionnalités, services et options de configuration d'I2P
- **Visiter des eepsites** : Essayez d'accéder à des sites web `.i2p` via le réseau I2P
- **Lire la documentation** : Consultez la [documentation I2P](/docs/) pour plus d'informations

Bienvenue sur le réseau I2P ! 🎉
