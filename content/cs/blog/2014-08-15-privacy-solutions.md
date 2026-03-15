---
title: "The birth of Privacy Solutions"
date: 2014-08-15
author: "Meeh"
description: "Organization launch"
categories: ["press"]
---
Ahoj všichni!

Dnes oznámujeme projekt Privacy Solutions, novou organizaci, která vyvíjí a spravuje software I2P. Privacy Solutions zahrnuje několik nových vývojových úsilí zaměřených na zlepšení soukromí, bezpečnosti a anonymity uživatelů, založených na protokolech a technologii I2P.

Tato úsilí zahrnují:

1. Balíček prohlížeče Abscond.
2. Projekt směrovače i2pd v C++.
3. Projekt monitorování sítě I2P „BigBrother“.
4. Projekt kryptoměny Anoncoin.
5. Projekt kryptoměny Monero.

Počáteční financování Privacy Solutions zajistili příznivci projektů Anoncoin a Monero. Privacy Solutions je nezisková organizace založená v Norsku, registrovaná v norských státních rejstřících. (Něco jako americká 501(c)3.)

Privacy Solutions plánuje požádat o financování od norské vlády pro výzkum sítě, a to kvůli projektu BigBrother (o tom později) a kryptoměnám, které mají v plánu používat sítě s nízkou latencí jako hlavní transportní vrstvu. Náš výzkum bude podporovat pokroky v softwarových technologiích pro anonymitu, bezpečnost a soukromí.

Nejprve trochu informací o balíčku prohlížeče Abscond. Původně šlo o jednočlenný projekt Meeha, ale později začali přátelé posílat opravy. Projekt se nyní snaží vytvořit stejně snadný přístup k I2P jako má Tor se svým balíčkem prohlížeče. Naše první verze není daleko, zbývají jen některé úkoly v gitian skriptech, včetně nastavení Apple toolchainu. Přidáme však také monitorování pomocí PROCESS_INFORMATION (C struktura uchovávající klíčové informace o procesu) z instance Java, abychom mohli sledovat stav I2P, než ji označíme za stabilní. Jakmile bude připraveno, přepneme také na verzi i2pd místo Java verze, a nebude již dále nutné balit JRE do balíčku. Více o balíčku prohlížeče Abscond si můžete přečíst na https://hideme.today/dev

Rádi bychom vás informovali také o aktuálním stavu i2pd. I2pd nyní podporuje obousměrné proudování, což umožňuje používat nejen HTTP, ale i dlouhodobé komunikační kanály. Byla přidána podpora pro IRC. Uživatelé i2pd mohou IRC používat stejným způsobem jako u Java I2P pro přístup k I2P IRC síti. I2PTunnel je jednou z klíčových funkcí sítě I2P, umožňuje transparentní komunikaci i pro aplikace mimo I2P. Proto je to pro i2pd nezbytná funkce a jeden z hlavních milníků.

Nakonec, pokud znáte I2P, pravděpodobně jste slyšeli o Bigbrother.i2p, což je metrický systém, který Meeh vytvořil před více než rokem. Nedávno jsme si všimli, že Meeh ve skutečnosti shromáždil 100 GB neduplikovaných dat od uzlů od počátečního spuštění. Tato data budou také převedena pod Privacy Solutions a přepsána s NSPOF backendem. Začneme také používat Graphite (http://graphite.wikidot.com/screen-shots). To nám poskytne výborný přehled o síti bez ohrožení soukromí našich koncových uživatelů. Klienti filtrovají veškerá data kromě země, hashové hodnoty směrovače a úspěšnosti při vytváření tunelů. Název této služby je, jak už to Meeh má ve zvyku, trochu vtip.

Zde jsme zprávy trochu zkrátili. Pokud chcete více informací, navštivte prosím https://blog.privacysolutions.no/ Stále jsme ve výstavbě a další obsah bude následovat!

Pro další informace kontaktujte: press@privacysolutions.no

S pozdravem,

Mikal „Meeh“ Villa
