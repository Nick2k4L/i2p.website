---
title: "Format de filtre d'accès"
description: "Syntaxe pour les fichiers de filtre de contrôle d'accès des tunnels"
slug: "filter-format"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
type: docs
---

## Aperçu

La définition d'un filtre est une liste de chaînes de caractères. Les lignes vides et les lignes commençant par `#` sont ignorées. Les modifications dans la définition du filtre prennent effet au redémarrage du tunnel.

Chaque ligne peut représenter l'un de ces éléments :

- Définition d'un seuil par défaut à appliquer à toutes les destinations distantes non listées dans ce fichier ou dans les fichiers référencés
- Définition d'un seuil à appliquer à une destination distante spécifique
- Définition d'un seuil à appliquer aux destinations distantes listées dans un fichier
- Définition d'un seuil qui, s'il est dépassé, entraînera l'enregistrement de la destination distante fautive dans un fichier spécifié

L'ordre des définitions importe. Le premier seuil pour une destination donnée (qu'il soit explicite ou listé dans un fichier) remplace tous les seuils futurs pour la même destination, qu'ils soient explicites ou listés dans un fichier.

## Seuils

Un seuil est défini par le nombre de tentatives de connexion qu'une destination distante est autorisée à effectuer sur une période spécifiée en secondes avant qu'une "violation" ne se produise. Par exemple, la définition de seuil suivante `15/5` signifie que la même destination distante est autorisée à effectuer 14 tentatives de connexion sur une période de 5 secondes. Si elle effectue une tentative supplémentaire dans la même période, le seuil sera violé.

Le format de seuil peut être l'un des suivants :

- **Définition numérique** du nombre de connexions sur le nombre de secondes - `15/5`, `30/60`, etc. Notez que si le nombre de connexions est 1 (comme par exemple dans `1/1`), la première tentative de connexion entraînera un dépassement.
- Le mot **`allow`**. Ce seuil n'est jamais dépassé, c'est-à-dire qu'un nombre infini de tentatives de connexion est autorisé.
- Le mot **`deny`**. Ce seuil est toujours dépassé, c'est-à-dire qu'aucune tentative de connexion ne sera autorisée.

### Seuil par défaut

Le seuil par défaut s'applique à toutes les destinations distantes qui ne sont pas explicitement listées dans la définition ou dans l'un des fichiers référencés. Pour définir un seuil par défaut, utilisez le mot-clé `default`. Voici des exemples de seuils par défaut :

```text
15/5 default
allow default
deny default
```
Il ne peut y avoir qu'une seule définition d'un seuil par défaut par filtre. S'il est omis, le filtre autorisera par défaut les connexions inconnues.

### Seuils explicites

Des seuils explicites sont appliqués à une destination distante listée dans la définition elle-même. Exemples :

```text
15/5 explicit asdfasdfasdf.b32.i2p
allow explicit fdsafdsafdsa.b32.i2p
deny explicit qwerqwerqwer.b32.i2p
```
### Seuils en lot

Pour plus de commodité, il est possible de maintenir une liste de destinations dans un fichier et de définir un seuil pour toutes en une seule fois. Exemples :

```text
15/5 file /path/throttled_destinations.txt
deny file /path/forbidden_destinations.txt
allow file /path/unlimited_destinations.txt
```
Ces fichiers peuvent être modifiés manuellement pendant que le tunnel fonctionne. Les modifications de ces fichiers peuvent prendre jusqu'à 10 secondes pour prendre effet.

## Enregistreurs

Les enregistreurs suivent les tentatives de connexion effectuées par une destination distante, et si cela dépasse un certain seuil, cette destination est enregistrée dans un fichier donné. Exemples :

```text
30/5 record /path/aggressive.txt
60/5 record /path/very_aggressive.txt
```
Il est possible d'utiliser un enregistreur pour consigner les destinations agressives dans un fichier donné, puis d'utiliser ce même fichier pour les limiter. Par exemple, l'extrait suivant définira un filtre qui autorise initialement toutes les tentatives de connexion, mais si une destination unique dépasse 30 tentatives par 5 secondes, elle sera limitée à 15 tentatives par 5 secondes :

```text
# by default there are no limits
allow default
# but record overly aggressive destinations
30/5 record /path/throttled.txt
# and any that end up in that file will get throttled in the future
15/5 file /path/throttled.txt
```
Il est possible d'utiliser un enregistreur dans un tunnel qui écrit dans un fichier qui régule un autre tunnel. Il est possible de réutiliser le même fichier avec des destinations dans plusieurs tunnels. Et bien sûr, il est possible d'éditer ces fichiers à la main.

Voici un exemple de définition de filtre qui applique une limitation par défaut, aucune limitation pour les destinations dans le fichier `friends.txt`, interdit toute connexion depuis les destinations dans le fichier `enemies.txt` et enregistre tout comportement agressif dans un fichier appelé `suspicious.txt` :

```text
15/5 default
allow file /path/friends.txt
deny file /path/enemies.txt
60/5 record /path/suspicious.txt
```