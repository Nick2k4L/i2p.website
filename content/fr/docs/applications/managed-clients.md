---
title: "Clients Gérés"
description: "Comment les applications gérées par le router s'intègrent avec ClientAppManager et le mappeur de ports"
slug: "managed-clients"
lastUpdated: "2014-02"
accurateFor: "0.9.11"
---

## Aperçu

Les clients peuvent être démarrés directement par le router lorsqu'ils sont listés dans le fichier [clients.config](/docs/specs/configuration/). Ces clients peuvent être "gérés" ou "non gérés". Ceci est géré par le ClientAppManager. De plus, les clients gérés ou non gérés peuvent s'enregistrer auprès du ClientAppManager afin que d'autres clients puissent récupérer une référence vers eux. Il existe également un système simple de Port Mapper permettant aux clients d'enregistrer un port interne que d'autres clients peuvent consulter.

---

## Clients gérés

À partir de la version 0.9.4, le router prend en charge les clients gérés. Les clients gérés sont instanciés et démarrés par le ClientAppManager. Le ClientAppManager maintient une référence vers le client et reçoit des mises à jour sur l'état du client. Les clients gérés sont préférés, car il est beaucoup plus facile d'implémenter le suivi d'état et de démarrer et arrêter un client. Il est également beaucoup plus facile d'éviter les références statiques dans le code client qui pourraient conduire à une utilisation excessive de la mémoire après l'arrêt d'un client. Les clients gérés peuvent être démarrés et arrêtés par l'utilisateur dans la console du router, et sont arrêtés lors de l'arrêt du router.

Les clients gérés implémentent soit l'interface net.i2p.app.ClientApp soit l'interface net.i2p.router.app.RouterApp. Les clients implémentant l'interface ClientApp doivent fournir le constructeur suivant :

```java
public MyClientApp(I2PAppContext context, ClientAppManager listener, String[] args)
```
Les clients implémentant l'interface RouterApp doivent fournir le constructeur suivant :

```java
public MyClientApp(RouterContext context, ClientAppManager listener, String[] args)
```
Les arguments fournis sont spécifiés dans le fichier clients.config.

---

## Clients non gérés

Si la classe principale spécifiée dans le fichier clients.config n'implémente pas une interface gérée, elle sera démarrée avec main() avec les arguments spécifiés, et arrêtée avec main() avec les arguments spécifiés. Le router ne maintient pas de référence, puisque toutes les interactions se font via la méthode statique main(). La console ne peut pas fournir d'informations d'état précises à l'utilisateur.

---

## Clients enregistrés

Les clients, qu'ils soient gérés ou non gérés, peuvent s'enregistrer auprès du ClientAppManager afin que d'autres clients puissent récupérer une référence vers eux. L'enregistrement se fait par nom. Les clients enregistrés connus sont :

```
console, i2ptunnel, Jetty, outproxy, update
```
---

## Mappeur de ports

Le router fournit également un mécanisme simple pour que les clients puissent trouver un service de socket interne, tel que le proxy HTTP. Ceci est fourni par le Port Mapper. L'enregistrement se fait par nom. Les clients qui s'enregistrent fournissent généralement un socket émulé interne sur ce port.
