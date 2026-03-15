---
title: "Le Processus de Proposition I2P"
number: "001"
author: "str4d"
created: "2016-04-10"
lastupdated: "2017-04-07"
status: "Meta"
thread: "http://zzz.i2p/topics/1980"
toc: true
---
## Vue d'ensemble

Ce document décrit comment modifier les spécifications I2P, comment fonctionnent les propositions I2P et la relation entre les propositions I2P et les spécifications.

Ce document est adapté du processus de proposition Tor, et une grande partie du contenu ci-dessous a été rédigée à l'origine par Nick Mathewson.

Il s'agit d'un document informatif.

## Motivation

Autrefois, notre processus de mise à jour des spécifications I2P était relativement informel : nous faisions une proposition sur le forum de développement et discutions des changements, puis nous arrivions à un consensus et patchions la spécification avec des changements de projet (pas nécessairement dans cet ordre), et enfin nous mettions en œuvre les changements.

Cela posait quelques problèmes.

Tout d'abord, même à son niveau le plus efficace, l'ancien processus faisait souvent que la spécification était désynchronisée avec le code. Les cas les plus graves étaient ceux où la mise en œuvre était différée : la spécification et le code pouvaient rester désynchronisés pendant des versions.

Deuxièmement, il était difficile de participer à la discussion, puisqu'il n'était pas toujours clair quelles parties du fil de discussion faisaient partie de la proposition, ou quels changements de la spécification avaient été mis en œuvre. Les forums de développement ne sont accessibles qu'à l'intérieur d'I2P, ce qui signifie que les propositions ne pouvaient être consultées que par les personnes qui utilisent I2P.

Troisièmement, il était très facile d'oublier certaines propositions parce qu'elles étaient noyées plusieurs pages plus loin dans la liste des threads du forum.

## Comment modifier les spécifications maintenant

Tout d'abord, quelqu'un rédige un document de proposition. Il devrait décrire le changement qui doit être apporté en détail et donner une idée de la façon de le mettre en œuvre. Une fois qu'il est suffisamment détaillé, il devient une proposition.

Comme un RFC, chaque proposition reçoit un numéro. Contrairement aux RFC, les propositions peuvent changer au fil du temps et conserver le même numéro, jusqu'à ce qu'elles soient finalement acceptées ou rejetées. L'historique de chaque proposition sera stocké dans le référentiel du site Web d'I2P.

Une fois qu'une proposition est dans le référentiel, nous devons la discuter sur le thread correspondant et l'améliorer jusqu'à ce que nous ayons atteint un consensus pour qu'elle soit une bonne idée, et qu'elle soit suffisamment détaillée pour être mise en œuvre. Lorsque cela se produit, nous mettons en œuvre la proposition et l'incorporons dans les spécifications. Ainsi, les spécifications restent la documentation canonique pour le protocole I2P : aucune proposition n'est jamais la documentation canonique pour une fonctionnalité mise en œuvre.

(Ce processus est assez similaire au processus d'amélioration de Python, avec la principale exception que les propositions I2P sont réintégrées dans les spécifications après la mise en œuvre, alors que les PEP *deviennent* la nouvelle spécification.)

### Petits changements

Il est toujours possible d'apporter de petits changements directement à la spécification si le code peut être écrit plus ou moins immédiatement, ou des changements cosmétiques si aucun changement de code n'est requis. Ce document reflète l'intention actuelle des développeurs, et non une promesse permanente d'utiliser toujours ce processus à l'avenir : nous nous reservons le droit de nous enthousiasmer et de mettre en œuvre quelque chose dans une session de programmation nocturne animée par du café ou des M&M's.

## Comment de nouvelles propositions sont ajoutées

Pour soumettre une proposition, publiez-la sur le forum de développement ou entrez un ticket avec la proposition attachée.

Une fois qu'une idée a été proposée, un projet de proposition correctement formaté (voir ci-dessous) existe, et un consensus approximatif au sein de la communauté de développement active existe pour que cette idée mérite d'être examinée, les éditeurs de proposition l'ajouteront officiellement.

Les éditeurs de proposition actuels sont zzz et str4d.

## Ce qui doit figurer dans une proposition

Chaque proposition doit avoir un en-tête contenant les champs suivants :

```
:author:
:created:
:thread:
:lastupdated:
:status:
```

- Le champ `author` doit contenir les noms des auteurs de cette proposition.
- Le champ `thread` doit être un lien vers le thread du forum de développement où cette proposition a été publiée à l'origine, ou vers un nouveau thread créé pour discuter de cette proposition.
- Le champ `lastupdated` doit être initialisé à la même valeur que le champ `created`, et doit être mis à jour chaque fois que la proposition est modifiée.

Ces champs doivent être définis lorsque cela est nécessaire :

```
:supercedes:
:supercededby:
:editor:
```

- Le champ `supercedes` est une liste séparée par des virgules de toutes les propositions que cette proposition remplace. Ces propositions doivent être rejetées et avoir leur champ `supercededby` défini sur le numéro de cette proposition.
- Le champ `editor` doit être défini si des changements importants sont apportés à cette proposition qui n'altèrent pas substantiellement son contenu. Si le contenu est substantiellement modifié, soit un autre `author` doit être ajouté, soit une nouvelle proposition doit être créée pour remplacer celle-ci.

Ces champs sont facultatifs mais recommandés :

```
:target:
:implementedin:
```

- Le champ `target` doit décrire quelle version de la proposition est espérée pour la mise en œuvre (si elle est ouverte ou acceptée).
- Le champ `implementedin` doit décrire quelle version de la proposition a été mise en œuvre (si elle est terminée ou close).

Le corps de la proposition doit commencer par une section Vue d'ensemble expliquant ce que propose la proposition, ce qu'elle fait et dans quel état elle se trouve.

Après la Vue d'ensemble, la proposition devient plus libre. Selon sa longueur et sa complexité, la proposition peut se diviser en sections comme il convient, ou suivre un format discursif court. Chaque proposition doit contenir au moins les informations suivantes avant d'être acceptée, bien que les informations n'aient pas besoin d'être dans des sections avec ces noms.

**Motivation**
: Quel est le problème que la proposition tente de résoudre ? Pourquoi ce problème est-il important ? Si plusieurs approches sont possibles, pourquoi choisir celle-ci ?

**Conception**
: Une vue d'ensemble de ce que sont les nouvelles fonctionnalités ou les fonctionnalités modifiées, de la façon dont elles fonctionnent, de la façon dont elles interagissent les unes avec les autres et de la façon dont elles interagissent avec le reste d'I2P. Il s'agit du corps principal de la proposition. Certaines propositions commenceront avec seulement une Motivation et une Conception, et attendront une spécification jusqu'à ce que la Conception semble approximativement correcte.

**Implications de sécurité**
: Quels effets les changements proposés pourraient avoir sur l'anonymat, à quel point ces effets sont bien compris, etc.

**Spécification**
: Une description détaillée de ce qui doit être ajouté aux spécifications I2P pour mettre en œuvre la proposition. Cela doit être dans autant de détails que les spécifications contiendront finalement : il doit être possible pour des programmeurs indépendants de rédiger des mises en œuvre compatibles entre elles de la proposition sur la base de ses spécifications.

**Compatibilité**
: Les versions d'I2P qui suivent la proposition seront-elles compatibles avec les versions qui ne le font pas ? Si oui, comment la compatibilité sera-t-elle assurée ? En général, nous essayons de ne pas abandonner la compatibilité si possible ; nous n'avons pas effectué de changement de "jour du drapeau" depuis mars 2008, et nous ne voulons pas en faire un autre.

**Mise en œuvre**
: Si la proposition sera difficile à mettre en œuvre dans l'architecture actuelle d'I2P, le document peut contenir une discussion sur la façon de la rendre fonctionnelle. Les patchs réels doivent être sur des branches monotone publiques, ou être téléchargés sur Trac.

**Notes sur les performances et la scalabilité**
: Si la fonctionnalité aura un effet sur les performances (en RAM, CPU, bande passante) ou la scalabilité, il doit y avoir une analyse de l'importance de cet effet, afin que nous puissions éviter des régressions de performances vraiment coûteuses, et que nous puissions éviter de perdre du temps sur des gains insignifiants.

**Références**
: Si la proposition fait référence à des documents externes, ceux-ci doivent être énumérés.

## État de la proposition

**Ouverte**
: Une proposition en discussion.

**Acceptée**
: La proposition est complète, et nous avons l'intention de la mettre en œuvre. Après ce point, les changements substantiels de la proposition doivent être évités et considérés comme un signe que le processus a échoué à un moment donné.

**Terminée**
: La proposition a été acceptée et mise en œuvre. Après ce point, la proposition ne doit pas être modifiée.

**Close**
: La proposition a été acceptée, mise en œuvre et fusionnée dans les documents de spécification principaux. La proposition ne doit pas être modifiée après ce point.

**Rejetée**
: Nous n'allons pas mettre en œuvre la fonctionnalité comme décrite ici, bien que nous puissions faire une autre version. Voir les commentaires dans le document pour plus de détails. La proposition ne doit pas être modifiée après ce point ; pour soulever une autre version de l'idée, rédigez une nouvelle proposition.

**Brouillon**
: Ce n'est pas encore une proposition complète ; il y a des pièces manquantes. S'il vous plaît, n'ajoutez pas de nouvelles propositions avec ce statut ; mettez-les dans le répertoire "idées" à la place.

**Nécessite une révision**
: L'idée de la proposition est bonne, mais la proposition telle qu'elle est a des problèmes graves qui l'empêchent d'être acceptée. Voir les commentaires dans le document pour plus de détails.

**Mort**
: La proposition n'a pas été touchée depuis longtemps, et il ne semble pas que quelqu'un soit sur le point de la compléter bientôt. Elle peut redevenir "Ouverte" si elle obtient un nouveau promoteur.

**Nécessite des recherches**
: Il y a des problèmes de recherche qui doivent être résolus avant qu'il ne soit clair que la proposition est une bonne idée.

**Meta**
: Ce n'est pas une proposition, mais un document sur les propositions.

**Réserve**
: Cette proposition n'est pas quelque chose que nous prévoyons actuellement de mettre en œuvre, mais nous pourrions vouloir la ressusciter un jour si nous décidons de faire quelque chose comme ce que propose la proposition.

**Informationnel**
: Cette proposition est le dernier mot sur ce qu'elle fait. Elle ne va pas se transformer en spécification à moins que quelqu'un ne la copie et la colle dans une nouvelle spécification pour un nouveau sous-système.

Les éditeurs maintiennent le statut correct des propositions, en fonction d'un consensus approximatif et de leur propre discrétion.

## Numérotation des propositions

Les numéros 000-099 sont réservés pour les propositions spéciales et métas. 100 et plus sont utilisés pour les propositions réelles. Les numéros ne sont pas recyclés.

## Références

* [DEV-FORUM-PROPOSAL](http://zzz.i2p/topics/new?forum_id=7-big-topics-ideas-proposals-and-discussion)
* [TORSPEC-PROCESS](https://gitweb.torproject.org/torspec.git/tree/proposals/001-process.txt)
* [TRAC-PROPOSAL](http://trac.i2p2.i2p/newticket?summary=New%20proposal:%20&type=enhancement&milestone=n/a&component=www/i2p&keywords=review-needed)
