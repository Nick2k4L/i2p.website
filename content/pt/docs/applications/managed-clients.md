---
title: "Clientes Gerenciados"
description: "Como aplicações gerenciadas pelo router se integram com ClientAppManager e o mapeador de portas"
slug: "managed-clients"
lastUpdated: "2014-02"
accurateFor: "0.9.11"
---

## Visão Geral

Os clientes podem ser iniciados diretamente pelo router quando estão listados no arquivo [clients.config](/docs/specs/configuration/). Estes clientes podem ser "gerenciados" ou "não gerenciados". Isto é tratado pelo ClientAppManager. Além disso, clientes gerenciados ou não gerenciados podem se registrar no ClientAppManager para que outros clientes possam recuperar uma referência a eles. Há também um recurso simples de Port Mapper para os clientes registrarem uma porta interna que outros clientes possam consultar.

---

## Clientes Gerenciados

A partir da versão 0.9.4, o router suporta clientes gerenciados. Os clientes gerenciados são instanciados e iniciados pelo ClientAppManager. O ClientAppManager mantém uma referência ao cliente e recebe atualizações sobre o estado do cliente. Os clientes gerenciados são preferenciais, pois é muito mais fácil implementar o rastreamento de estado e iniciar e parar um cliente. Também é muito mais fácil evitar referências estáticas no código do cliente que poderiam levar ao uso excessivo de memória após um cliente ser parado. Os clientes gerenciados podem ser iniciados e parados pelo usuário no console do router, e são parados durante o desligamento do router.

Clientes gerenciados implementam either a interface net.i2p.app.ClientApp ou net.i2p.router.app.RouterApp. Clientes que implementam a interface ClientApp devem fornecer o seguinte construtor:

```java
public MyClientApp(I2PAppContext context, ClientAppManager listener, String[] args)
```
Clientes que implementam a interface RouterApp devem fornecer o seguinte construtor:

```java
public MyClientApp(RouterContext context, ClientAppManager listener, String[] args)
```
Os argumentos fornecidos são especificados no arquivo clients.config.

---

## Clientes Não Gerenciados

Se a classe principal especificada no arquivo clients.config não implementar uma interface gerenciada, ela será iniciada com main() com os argumentos especificados, e interrompida com main() com os argumentos especificados. O router não mantém uma referência, já que todas as interações são via o método estático main(). O console não pode fornecer informações precisas de estado ao usuário.

---

## Clientes Registrados

Clientes, sejam gerenciados ou não gerenciados, podem se registrar no ClientAppManager para que outros clientes possam obter uma referência a eles. O registro é feito por nome. Os clientes registrados conhecidos são:

```
console, i2ptunnel, Jetty, outproxy, update
```
---

## Mapeador de Portas

O router também fornece um mecanismo simples para clientes encontrarem um serviço de socket interno, como o proxy HTTP. Isso é fornecido pelo Port Mapper. O registro é feito por nome. Clientes que se registram geralmente fornecem um socket emulado interno naquela porta.
