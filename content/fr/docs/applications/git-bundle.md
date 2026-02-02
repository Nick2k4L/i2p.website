---
title: "Utilisation d'un bundle git pour récupérer le code source I2P"
description: "Clonage de grands dépôts sur I2P en utilisant les bundles git et BitTorrent"
slug: "git-bundle"
lastUpdated: "2020-09"
accurateFor: "0.9.47"
---

Cloner de gros dépôts logiciels via I2P peut être difficile, et utiliser git peut parfois rendre cela plus compliqué. Heureusement, cela peut aussi parfois le rendre plus facile. Git dispose d'une commande `git bundle` qui peut être utilisée pour transformer un dépôt git en fichier depuis lequel git peut ensuite cloner, récupérer ou importer depuis un emplacement sur votre disque local. En combinant cette capacité avec les téléchargements bittorrent, nous pouvons résoudre nos problèmes restants avec `git clone`.

---

## Avant de commencer

Si vous avez l'intention de générer un bundle git, vous **devez** déjà posséder une copie complète du dépôt **git**, pas le dépôt mtn. Vous pouvez l'obtenir depuis github ou depuis git.idk.i2p, mais un clone superficiel (un clone fait avec --depth=1) *ne fonctionnera pas*. Il échouera silencieusement, créant ce qui ressemble à un bundle, mais quand vous essaierez de le cloner, cela échouera. Si vous récupérez simplement un bundle git pré-généré, alors cette section ne vous concerne pas.

---

## Récupération du code source I2P via Bittorrent

Quelqu'un devra vous fournir un fichier torrent ou un lien magnet correspondant à un `git bundle` existant qu'il a déjà généré pour vous. Un bundle récent et correctement généré du code source principal i2p.i2p en date du mercredi 18 mars 2020 peut être trouvé à l'intérieur d'I2P sur mon pastebin [paste.idk.i2p/f/4hq37i](http://paste.idk.i2p/f/4h137i).

Une fois que vous avez un bundle, vous devrez utiliser git pour créer un dépôt de travail à partir de celui-ci. Si vous utilisez GNU/Linux et i2psnark, le git bundle devrait se trouver dans $HOME/.i2p/i2psnark ou, en tant que service sur Debian, /var/lib/i2p/i2p-config/i2psnark. Si vous utilisez BiglyBT sur GNU/Linux, il se trouve probablement dans "$HOME/BiglyBT Downloads/" à la place. Les exemples ici supposent I2PSnark sur GNU/Linux, si vous utilisez autre chose, remplacez le chemin vers le bundle par le répertoire de téléchargement préféré par votre client et votre plateforme.

### Utilisation de `git clone`

Cloner à partir d'un bundle git est facile, il suffit de :

```
git clone $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
Si vous obtenez l'erreur suivante, essayez d'utiliser git init et git fetch manuellement à la place.

```
fatal: multiple updates for ref 'refs/remotes/origin/master' not allowed
```
### Utilisation de `git init` et `git fetch`

D'abord, créez un répertoire i2p.i2p pour le transformer en dépôt git.

```
mkdir i2p.i2p && cd i2p.i2p
```
Ensuite, initialisez un dépôt git vide pour récupérer les modifications.

```
git init
```
Enfin, récupérez le dépôt depuis le bundle.

```
git fetch $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
### Remplacer le remote bundle par le remote upstream

Maintenant que vous avez un bundle, vous pouvez suivre les modifications en définissant le remote vers la source du dépôt upstream.

```
git remote set-url origin git@127.0.0.1:I2P_Developers/i2p.i2p
```
---

## Génération d'un Bundle

D'abord, suivez le [Guide Git pour les utilisateurs](/docs/applications/git/) jusqu'à ce que vous ayez un clone `--unshallow` réussi du dépôt i2p.i2p. Si vous avez déjà un clone, assurez-vous d'exécuter `git fetch --unshallow` avant de générer un bundle torrent.

Une fois que vous avez cela, exécutez simplement la cible ant correspondante :

```
ant git-bundle
```
et copiez le bundle résultant dans votre répertoire de téléchargements I2PSnark. Par exemple :

```
cp i2p.i2p.bundle* $HOME/.i2p/i2psnark/
```
Dans une minute ou deux, I2PSnark détectera le torrent. Cliquez sur le bouton "Start" pour commencer à partager le torrent.
