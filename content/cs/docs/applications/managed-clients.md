---
title: "Spravovaní klienti"
description: "Jak aplikace spravované routerem integrují s ClientAppManager a mapovačem portů"
slug: "managed-clients"
lastUpdated: "2014-02"
accurateFor: "0.9.11"
---

## Přehled

Klienti mohou být spuštěni přímo routerem, když jsou uvedeni v souboru [clients.config](/docs/specs/configuration/). Tito klienti mohou být "spravovaní" nebo "nespravovaní". Toto je zpracováváno ClientAppManagerem. Kromě toho se spravovaní nebo nespravovaní klienti mohou registrovat u ClientAppManagera, aby ostatní klienti mohli získat odkaz na ně. Existuje také jednoduché zařízení Port Mapper, které klientům umožňuje zaregistrovat interní port, který si mohou ostatní klienti vyhledat.

---

## Spravovaní klienti

Od verze 0.9.4 router podporuje spravované klienty. Spravovaní klienti jsou vytvářeni a spouštěni pomocí ClientAppManager. ClientAppManager udržuje referenci na klienta a přijímá aktualizace o stavu klienta. Spravovaní klienti jsou preferováni, protože je mnohem jednodušší implementovat sledování stavu a spouštět a zastavovat klienta. Také je mnohem jednodušší vyhnout se statickým referencím v kódu klienta, které by mohly vést k nadměrnému využití paměti poté, co je klient zastaven. Spravovaní klienti mohou být spouštěni a zastavováni uživatelem v router konzoli a jsou zastaveni při vypnutí routeru.

Spravované klienty implementují buď rozhraní net.i2p.app.ClientApp nebo net.i2p.router.app.RouterApp. Klienty implementující rozhraní ClientApp musí poskytovat následující konstruktor:

```java
public MyClientApp(I2PAppContext context, ClientAppManager listener, String[] args)
```
Klienti implementující rozhraní RouterApp musí poskytovat následující konstruktor:

```java
public MyClientApp(RouterContext context, ClientAppManager listener, String[] args)
```
Argumenty jsou specifikovány v souboru clients.config.

---

## Nespravovaní klienti

Pokud hlavní třída specifikovaná v souboru clients.config neimplementuje managed rozhraní, bude spuštěna pomocí main() se specifikovanými argumenty a zastavena pomocí main() se specifikovanými argumenty. Router neudržuje referenci, protože všechny interakce probíhají přes statickou metodu main(). Konzole nemůže poskytnout uživateli přesné informace o stavu.

---

## Registrovaní klienti

Klienti, ať už spravovaní nebo nespravovaní, se mohou registrovat u ClientAppManager, aby k nim mohli ostatní klienti získat odkaz. Registrace probíhá podle jména. Známí registrovaní klienti jsou:

```
console, i2ptunnel, Jetty, outproxy, update
```
---

## Mapování portů

Router také poskytuje jednoduchý mechanismus pro klienty k nalezení interní socket služby, jako je HTTP proxy. Toto je zajištěno pomocí Port Mapperu. Registrace probíhá podle jména. Klienti, kteří se registrují, obecně poskytují interní emulovaný socket na daném portu.
