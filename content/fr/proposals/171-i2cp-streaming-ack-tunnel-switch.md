---
title: "Indicateur I2CP pour le changement de tunnel sortant"
number: "171"
author: "onon, eyedeekay"
created: "2026-05-19"
lastupdated: "2026-05-23"
status: "Brouillon"
toc: true
---

## Aperçu

Les connexions client du protocole de streaming peuvent se bloquer lorsque les accusés de réception sont perdus silencieusement. L'expéditeur effectue des retransmissions jusqu'à réception d'un accusé de réception ou jusqu'à la fermeture de la connexion, sans moyen fiable de confirmer que les accusés de réception parviennent à l'autre extrémité. Cette proposition ajoute un nouveau bit indicateur au champ flags de [SendMessageExpiresMessage](/docs/specs/i2cp/), permettant ainsi à un client d'indiquer au routeur de sélectionner un tunnel sortant différent pour les messages ultérieurs adressés à la même destination. Le protocole de streaming utilise ce bit pour initier un changement de tunnel lorsqu'un blocage de connexion est détecté.

## Déclencheurs

Deux conditions DEVRAIENT inciter le client à activer le drapeau sur le prochain message sortant. Ces conditions sont mesurées au niveau de la couche de streaming.

**Côté expéditeur**

Aucun accusé de réception n'a été reçu dans le délai de retransmission actuel du client.

**Côté récepteur**

Le récepteur a observé que le correspondant retransmettait les mêmes données plus d'une fois, ce qui indique que ses accusés de réception n'atteignent pas le correspondant. Le récepteur DEVRAIT activer ce drapeau dans son prochain message sortant I2CP afin que les accusés de réception parviennent au correspondant via un chemin différent. Le récepteur DOIT attendre jusqu'à ce que : (1) il ait reçu un doublon, (2) il ait envoyé au moins un accusé de réception, et (3) le correspondant ait retransmis à nouveau avant d'activer le drapeau.

Pour limiter les attaques par corrélation temporelle, un client NE DOIT PAS définir le drapeau plus d'une fois par fenêtre de 10 secondes par connexion. Le client DEVRAIT également retarder le paramétrage du drapeau d'une gigue tirée uniformément depuis `[0, min(T/4, 2000ms)]`, où T est le délai de retransmission actuel du client en millisecondes, après avoir détecté la condition de blocage, afin de réduire la précision de la corrélation temporelle.

## Spécification

Le champ flags du [SendMessageExpiresMessage](/docs/specs/i2cp/) occupe les 2 octets supérieurs après le champ Date (redéfini à partir de la version 0.8.4) et est transmis en big-endian. Le bit 15 est actuellement inutilisé ; cette proposition le définit.

Ordre des bits : 15...0

| Bit | Nom | Description |
|-----|------|-------------|
| 15 | SWITCH_OUTBOUND_TUNNEL | Si ce bit vaut 1, le routeur DEVRAIT sélectionner un tunnel sortant différent parmi son pool pour les messages ultérieurs à destination de ce destinataire. Si aucun tunnel de remplacement n'est disponible, ce drapeau est ignoré silencieusement. Le routeur NE DOIT PAS fermer ou retirer le tunnel précédemment utilisé uniquement parce que ce drapeau a été activé. |
Ce drapeau a par défaut la valeur 0. Les routeurs qui ne l'implémentent pas DOIVENT l'ignorer sans erreur.

## Notes sur l'implémentation

Lorsque `SWITCH_OUTBOUND_TUNNEL` est activé, le routeur DOIT sélectionner un tunnel de manière uniforme et aléatoire dans le groupe de tunnels sortants, en excluant :

- le tunnel actuellement utilisé pour cette session, et
- le tunnel le plus récemment échoué dans le groupe, s'il y en a un.

Toutes les autres métriques de santé des tunnels, les temps de création ou l'historique de sélection NE DOIVENT PAS influencer le choix, car une sélection pondérée pourrait favoriser les attaquants sybil. Si le groupe ne contient aucun tunnel éligible après ces exclusions, le drapeau est silencieusement ignoré.

Ce drapeau n'entraîne aucun message de tunnel supplémentaire ; le changement de tunnel peut modifier la latence apparente. La limite de débit de 10 secondes par connexion (voir Déclencheurs) empêche les changements excessifs.

## Considérations sur l'anonymat

Les indicateurs dans [SendMessageExpiresMessage](/docs/specs/i2cp/) sont transmis via I2CP, une interface locale entre le client et son propre routeur. Ils ne sont pas visibles pour les observateurs du réseau.

Le risque d'anonymat est basé sur les motifs de trafic : un adversaire ayant une visibilité sur plusieurs extrémités de tunnel peut observer *quand* l'utilisation du tunnel change.

Changer les tunnels sortants en réponse directe à un blocage côté client crée un motif comportemental détectable. Il existe deux vecteurs d'observation concrets :

**Attaque Sybil sur les premiers sauts des tunnels sortants**

Le premier saut de chaque tunnel sortant voit tout le trafic entrant dans ce tunnel depuis le routeur de l'expéditeur. Un adversaire contrôlant le premier saut de plusieurs tunnels dans le groupe de l'expéditeur peut observer le trafic s'arrêter sur un premier saut et démarrer sur un autre dans un laps de temps très court, ce qui relie les deux tunnels au même expéditeur. Avec un groupe de N tunnels, un adversaire contrôlant K premiers sauts a une probabilité de K/N d'observer un événement de changement donné.

**Minutage des intervalles de trafic**

Pendant le blocage, le client n'envoie pas de nouvelles données, ce qui rend l'ancien tunnel sortant silencieux. Lorsque le changement a lieu, le trafic reprend sur un chemin différent. Un adversaire disposant d'un point d'observation sur le routeur de l'expéditeur — comme le fournisseur d'accès à Internet de l'expéditeur ou le nœud du premier saut lui-même — peut observer le motif de silence suivi d'une reprise. La durée de l'interruption révèle en outre une approximation de la valeur actuelle du délai de retransmission du client.

Les clients DOIVENT respecter les exigences de limitation de débit et de gigue décrites dans les déclencheurs.

## Références

- [Spécification I2CP](/docs/specs/i2cp/)
