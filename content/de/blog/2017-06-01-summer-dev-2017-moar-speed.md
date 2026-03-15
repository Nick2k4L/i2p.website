---
title: "I2P Summer Dev 2017: MOAR Speed!"
date: 2017-06-01
author: "str4d"
description: "This year's Summer Dev will be focused on metrics collection and performance improvements for the network."
categories: ["summer-dev"]
---
Es ist wieder soweit! Wir starten unser Sommerentwicklungsprogramm, bei dem wir einen bestimmten Aspekt von I2P in den Fokus rücken, um ihn voranzubringen. In den nächsten drei Monaten werden wir sowohl neue Mitwirkende als auch bestehende Community-Mitglieder ermutigen, eine Aufgabe auszuwählen und Spaß dabei zu haben!

Letztes Jahr konzentrierten wir uns darauf, Nutzern und Entwicklern zu helfen, I2P besser zu nutzen, indem wir die API-Werkzeuge verbesserten und Anwendungen, die über I2P laufen, besondere Aufmerksamkeit schenkten. Dieses Jahr möchten wir die Nutzererfahrung verbessern, indem wir an einem Aspekt arbeiten, der alle betrifft: der Performance.

Obwohl Onion-Routing-Netzwerke oft als „niedrig-latente“ Netzwerke bezeichnet werden, entsteht durch das Weiterleiten von Datenverkehr über zusätzliche Computer ein erheblicher Overhead. Durch das unidirektionale Tunnel-Design von I2P bedeutet ein Roundtrip zwischen zwei Destinations standardmäßig, dass zwölf Teilnehmer involviert sind! Die Verbesserung der Performance dieser Teilnehmer wird dazu beitragen, sowohl die Latenz von Ende-zu-Ende-Verbindungen zu verringern als auch die Qualität der Tunnel im gesamten Netzwerk zu erhöhen.

## MEHR Geschwindigkeit!

Unser Entwicklungsprogramm dieses Jahr besteht aus vier Komponenten:

### Messen

Ohne eine Basislinie können wir keine Verbesserungen feststellen! Wir werden ein Metriksystem erstellen, um Nutzungs- und Performance-Daten über I2P auf datenschutzfreundliche Weise zu sammeln, sowie verschiedene Benchmarking-Tools für den Betrieb über I2P anpassen (z. B. iperf3).

### Optimieren

Es gibt viel Potenzial, um die Performance unseres bestehenden Codes zu verbessern, z. B. um den Overhead an der Teilnahme an Tunneln zu reduzieren. Wir werden mögliche Verbesserungen bei kryptografischen Primitiven, Netzwerk-Transports (sowohl auf Link-Ebene als auch Ende-zu-Ende), Peer-Profilierung und Tunnel-Pfadselektion untersuchen.

### Vorantreiben

Wir haben mehrere offene Vorschläge zur Verbesserung der Skalierbarkeit des I2P-Netzwerks (z. B. Prop115, Prop123, Prop124, Prop125, Prop138, Prop140). Wir werden an diesen Vorschlägen arbeiten und mit der Implementierung der abgeschlossenen Vorschläge in den verschiedenen Netzwerk-Routern beginnen.

### Forschen

I2P ist ein paketvermitteltes Netzwerk, genau wie das Internet, auf dem es läuft. Das gibt uns große Flexibilität bei der Paketweiterleitung, sowohl für Performance als auch für Datenschutz. Der Großteil dieser Flexibilität ist bisher unerforscht! Wir möchten Forschung fördern, wie verschiedene Clearnet-Techniken zur Verbesserung der Bandbreite auf I2P angewendet werden können und wie sie die Privatsphäre der Netzwerkteilnehmer beeinflussen könnten.

## Mach mit beim Summer Dev!

Wir haben noch viele weitere Ideen, was wir in diesen Bereichen erreichen möchten. Wenn du Interesse daran hast, an Privatsphäre- und Anonymitätssoftware zu programmieren, Protokolle zu entwerfen (kryptografisch oder anders) oder zukünftige Ideen zu erforschen – komm und chatte mit uns auf IRC oder Twitter! Wir freuen uns immer, neue Mitglieder in unserer Community begrüßen zu dürfen. Außerdem versenden wir I2P-Aufkleber an alle neuen Mitwirkenden, die teilnehmen!

Wir werden hier regelmäßig Berichte veröffentlichen, aber du kannst unseren Fortschritt auch auf Twitter mit dem Hashtag #I2PSummer verfolgen und deine eigenen Ideen und Arbeiten teilen. Auf in den Sommer!
