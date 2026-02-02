---
title: "Verwaltete Clients"
description: "Wie router-verwaltete Anwendungen mit dem ClientAppManager und dem Port-Mapper integrieren"
slug: "managed-clients"
lastUpdated: "2014-02"
accurateFor: "0.9.11"
---

## Übersicht

Clients können direkt vom router gestartet werden, wenn sie in der [clients.config](/docs/specs/configuration/) Datei aufgelistet sind. Diese Clients können "verwaltet" oder "nicht verwaltet" sein. Dies wird vom ClientAppManager behandelt. Zusätzlich können verwaltete oder nicht verwaltete Clients sich beim ClientAppManager registrieren, damit andere Clients eine Referenz auf sie abrufen können. Es gibt auch eine einfache Port Mapper Funktion für Clients, um einen internen Port zu registrieren, den andere Clients nachschlagen können.

---

## Verwaltete Clients

Ab Release 0.9.4 unterstützt der router verwaltete Clients. Verwaltete Clients werden vom ClientAppManager instanziiert und gestartet. Der ClientAppManager behält eine Referenz auf den Client und erhält Aktualisierungen über den Zustand des Clients. Verwaltete Clients sind zu bevorzugen, da es viel einfacher ist, die Zustandsverfolgung zu implementieren und einen Client zu starten und zu stoppen. Es ist auch viel einfacher, statische Referenzen im Client-Code zu vermeiden, die zu übermäßigem Speicherverbrauch führen könnten, nachdem ein Client gestoppt wurde. Verwaltete Clients können vom Benutzer in der router-Konsole gestartet und gestoppt werden und werden beim Herunterfahren des routers gestoppt.

Verwaltete Clients implementieren entweder das net.i2p.app.ClientApp oder das net.i2p.router.app.RouterApp Interface. Clients, die das ClientApp Interface implementieren, müssen den folgenden Konstruktor bereitstellen:

```java
public MyClientApp(I2PAppContext context, ClientAppManager listener, String[] args)
```
Clients, die das RouterApp-Interface implementieren, müssen den folgenden Konstruktor bereitstellen:

```java
public MyClientApp(RouterContext context, ClientAppManager listener, String[] args)
```
Die bereitgestellten Argumente werden in der clients.config-Datei angegeben.

---

## Nicht verwaltete Clients

Wenn die in der clients.config-Datei angegebene Hauptklasse keine verwaltete Schnittstelle implementiert, wird sie mit main() mit den angegebenen Argumenten gestartet und mit main() mit den angegebenen Argumenten gestoppt. Der router behält keine Referenz, da alle Interaktionen über die statische main()-Methode erfolgen. Die Konsole kann dem Benutzer keine genauen Statusinformationen bereitstellen.

---

## Registrierte Clients

Clients, ob verwaltet oder unverwaltet, können sich beim ClientAppManager registrieren, damit andere Clients eine Referenz auf sie abrufen können. Die Registrierung erfolgt über den Namen. Bekannte registrierte Clients sind:

```
console, i2ptunnel, Jetty, outproxy, update
```
---

## Port Mapper

Der Router stellt auch einen einfachen Mechanismus für Clients bereit, um einen internen Socket-Dienst zu finden, wie z.B. den HTTP-Proxy. Dies wird durch den Port Mapper ermöglicht. Die Registrierung erfolgt über den Namen. Clients, die sich registrieren, stellen in der Regel einen internen emulierten Socket auf diesem Port bereit.
