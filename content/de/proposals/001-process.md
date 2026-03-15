---
title: "Der I2P-Vorschlagsprozess"
number: "001"
author: "str4d"
created: "2016-04-10"
lastupdated: "2017-04-07"
status: "Meta"
thread: "http://zzz.i2p/topics/1980"
toc: true
---
## Überblick

Dieses Dokument beschreibt, wie die I2P-Spezifikationen geändert werden, wie I2P-Vorschläge funktionieren und die Beziehung zwischen I2P-Vorschlägen und den Spezifikationen.

Dieses Dokument ist an das Tor-Vorschlagsverfahren angelehnt, und viel von dem Inhalt unten wurde ursprünglich von Nick Mathewson verfasst.

Dies ist ein informatives Dokument.

## Motivation

Zuvor war unser Prozess für die Aktualisierung der I2P-Spezifikationen relativ informell: wir machten einen Vorschlag im Entwickler-Forum und diskutierten die Änderungen, dann erreichten wir einen Konsens und patchten die Spezifikation mit Entwurfsänderungen (nicht unbedingt in dieser Reihenfolge), und schließlich implementierten wir die Änderungen.

Dies hatte einige Probleme.

Zuerst war der alte Prozess selbst bei seiner effizientesten Ausprägung oft so, dass die Spezifikation nicht mit dem Code synchronisiert war. Die schlimmsten Fälle waren die, in denen die Implementierung verzögert wurde: die Spezifikation und der Code konnten über Versionen hinweg nicht synchronisiert werden.

Zweitens war es schwierig, an der Diskussion teilzunehmen, da es nicht immer klar war, welche Teile des Diskussionsthreads Teil des Vorschlags waren oder welche Änderungen an der Spezifikation implementiert worden waren. Die Entwickler-Foren sind auch nur innerhalb von I2P zugänglich, was bedeutet, dass Vorschläge nur von Personen angesehen werden konnten, die I2P verwenden.

Drittens war es sehr leicht, einige Vorschläge zu vergessen, weil sie in der Forum-Thread-Liste mehrere Seiten zurück verschüttet wurden.

## Wie die Spezifikationen jetzt geändert werden

Zuerst verfasst jemand ein Vorschlagdokument. Es sollte die Änderung, die vorgenommen werden soll, im Detail beschreiben und eine Vorstellung davon geben, wie sie implementiert werden kann. Sobald es ausreichend ausgearbeitet ist, wird es zu einem Vorschlag.

Wie ein RFC bekommt jeder Vorschlag eine Nummer. Anders als RFCs können Vorschläge jedoch über die Zeit hinweg geändert werden und behalten die gleiche Nummer, bis sie endgültig angenommen oder abgelehnt werden. Die Historie für jeden Vorschlag wird im I2P-Website-Repository gespeichert.

Sobald ein Vorschlag im Repository ist, sollten wir ihn im entsprechenden Thread diskutieren und verbessern, bis wir einen Konsens erreicht haben, dass es eine gute Idee ist und dass es ausreichend detailliert ist, um implementiert zu werden. Wenn dies der Fall ist, implementieren wir den Vorschlag und integrieren ihn in die Spezifikationen. Somit bleiben die Spezifikationen die kanonische Dokumentation für das I2P-Protokoll: kein Vorschlag ist jemals die kanonische Dokumentation für ein implementiertes Feature.

(Dieser Prozess ist ziemlich ähnlich dem Python-Enhancement-Prozess, mit der wesentlichen Ausnahme, dass I2P-Vorschläge nach der Implementierung wieder in die Spezifikationen integriert werden, während PEPs *zur neuen Spezifikation* werden.)

### Kleine Änderungen

Es ist immer noch okay, kleine Änderungen direkt an der Spezifikation vorzunehmen, wenn der Code mehr oder weniger sofort geschrieben werden kann oder kosmetische Änderungen, wenn keine Code-Änderung erforderlich ist. Dieses Dokument spiegelt die aktuelle *Absicht* der Entwickler wider, nicht ein ewiges Versprechen, immer diesen Prozess in der Zukunft zu verwenden: wir behalten uns das Recht vor, uns wirklich zu begeistern und in einer koffein- oder M&M-gesteuerten All-Night-Hacking-Session loszulegen.

## Wie neue Vorschläge hinzugefügt werden

Um einen Vorschlag einzureichen, posten Sie ihn im Entwickler-Forum oder erstellen Sie ein Ticket mit dem Vorschlag als Anhang.

Sobald eine Idee vorgeschlagen wurde, ein ordnungsgemäß formatierter (siehe unten) Entwurf existiert und ein ungefährer Konsens innerhalb der aktiven Entwicklergemeinschaft besteht, dass diese Idee eine Überlegung wert ist, werden die Vorschlagsherausgeber den Vorschlag offiziell hinzufügen.

Die aktuellen Vorschlagsherausgeber sind zzz und str4d.

## Was in einem Vorschlag enthalten sein sollte

Jeder Vorschlag sollte einen Header enthalten, der die folgenden Felder enthält:

```
:author:
:created:
:thread:
:lastupdated:
:status:
```

- Das `author`-Feld sollte die Namen der Autoren dieses Vorschlags enthalten.
- Das `thread`-Feld sollte ein Link zum Entwickler-Forum-Thread sein, in dem dieser Vorschlag ursprünglich gepostet wurde, oder zu einem neuen Thread, der für die Diskussion dieses Vorschlags erstellt wurde.
- Das `lastupdated`-Feld sollte zunächst dem `created`-Feld entsprechen und sollte aktualisiert werden, wenn der Vorschlag geändert wird.

Diese Felder sollten bei Bedarf gesetzt werden:

```
:supercedes:
:supercededby:
:editor:
```

- Das `supercedes`-Feld ist eine kommagetrennte Liste aller Vorschläge, die dieser Vorschlag ersetzt. Diese Vorschläge sollten abgelehnt und ihr `supercededby`-Feld auf die Nummer dieses Vorschlags gesetzt werden.
- Das `editor`-Feld sollte gesetzt werden, wenn bedeutende Änderungen an diesem Vorschlag vorgenommen werden, die seinen Inhalt nicht wesentlich ändern. Wenn der Inhalt wesentlich geändert wird, sollte entweder ein zusätzlicher `author` hinzugefügt oder ein neuer Vorschlag erstellt werden, der diesen ersetzt.

Diese Felder sind optional, aber empfehlenswert:

```
:target:
:implementedin:
```

- Das `target`-Feld sollte beschreiben, in welcher Version der Vorschlag implementiert werden soll (wenn er Open oder Accepted ist).
- Das `implementedin`-Feld sollte beschreiben, in welcher Version der Vorschlag implementiert wurde (wenn er Finished oder Closed ist).

Der Text des Vorschlags sollte mit einem Überblicksabschnitt beginnen, der beschreibt, worum es im Vorschlag geht, was er tut und in welchem Zustand er sich befindet.

Nach dem Überblick kann der Vorschlag freier gestaltet werden. Je nach Länge und Komplexität kann der Vorschlag in Abschnitte unterteilt werden oder einem kurzen diskursiven Format folgen. Jeder Vorschlag sollte jedoch mindestens die folgenden Informationen enthalten, bevor er angenommen wird, obwohl die Informationen nicht in Abschnitten mit diesen Namen enthalten sein müssen.

**Motivation**
: Welches Problem versucht der Vorschlag zu lösen? Warum ist dieses Problem wichtig? Wenn mehrere Ansätze möglich sind, warum wird dieser gewählt?

**Design**
: Eine hochrangige Ansicht der neuen oder geänderten Funktionen, wie die neuen oder geänderten Funktionen arbeiten, wie sie miteinander interagieren und wie sie mit dem Rest von I2P interagieren. Dies ist der Hauptteil des Vorschlags. Einige Vorschläge beginnen mit nur einer Motivation und einem Design und warten auf eine Spezifikation, bis das Design ungefähr richtig erscheint.

**Sicherheitsimplikationen**
: Welche Auswirkungen die vorgeschlagenen Änderungen auf die Anonymität haben könnten, wie gut diese Auswirkungen verstanden sind und so weiter.

**Spezifikation**
: Eine detaillierte Beschreibung dessen, was zur Implementierung des Vorschlags in die I2P-Spezifikationen hinzugefügt werden muss. Dies sollte in etwa dem gleichen Detailgrad wie die Spezifikationen enthalten, die schließlich entstehen werden: es sollte möglich sein, dass unabhängige Programmierer auf der Grundlage des Vorschlags kompatible Implementierungen schreiben.

**Kompatibilität**
: Werden Versionen von I2P, die den Vorschlag befolgen, mit Versionen kompatibel sein, die dies nicht tun? Wenn ja, wie wird die Kompatibilität erreicht? Im Allgemeinen versuchen wir, die Kompatibilität nicht aufzugeben, wenn dies möglich ist; wir haben seit März 2008 keine "Flag-Day"-Änderung mehr vorgenommen und möchten keine weitere durchführen.

**Implementierung**
: Wenn der Vorschlag schwierig in der aktuellen I2P-Architektur zu implementieren ist, kann das Dokument eine Diskussion darüber enthalten, wie es funktionieren kann. Tatsächliche Patches sollten auf öffentlichen Monotone-Branches oder auf Trac hochgeladen werden.

**Leistungs- und Skalierbarkeitsnotizen**
: Wenn die Funktion eine Auswirkung auf die Leistung (in RAM, CPU, Bandbreite) oder Skalierbarkeit haben wird, sollte es eine Analyse darüber geben, wie bedeutend diese Auswirkung sein wird, damit wir wirklich teure Leistungsregressions vermeiden können und nicht Zeit auf unbedeutende Gewinne verschwenden.

**Referenzen**
: Wenn der Vorschlag auf externe Dokumente verweist, sollten diese aufgelistet werden.

## Vorschlagsstatus

**Open**
: Ein Vorschlag, der diskutiert wird.

**Accepted**
: Der Vorschlag ist vollständig, und wir planen, ihn zu implementieren. Nach diesem Punkt sollten substantielle Änderungen am Vorschlag vermieden und als Zeichen dafür angesehen werden, dass der Prozess irgendwo fehlgeschlagen ist.

**Finished**
: Der Vorschlag wurde angenommen und implementiert. Nach diesem Punkt sollte der Vorschlag nicht geändert werden.

**Closed**
: Der Vorschlag wurde angenommen, implementiert und in die Haupt-Spezifikationsdokumente integriert. Der Vorschlag sollte nach diesem Punkt nicht geändert werden.

**Rejected**
: Wir werden das Feature nicht wie hier beschrieben implementieren, obwohl wir möglicherweise eine andere Version davon implementieren. Siehe Kommentare im Dokument für Details. Der Vorschlag sollte nach diesem Punkt nicht geändert werden; um eine andere Version der Idee vorzubringen, sollte ein neuer Vorschlag erstellt werden.

**Draft**
: Dies ist noch kein vollständiger Vorschlag; es gibt definitiv fehlende Teile. Bitte fügen Sie keine neuen Vorschläge mit diesem Status hinzu; stattdessen sollten sie im "Ideas"-Unterverzeichnis abgelegt werden.

**Needs-Revision**
: Die Idee für den Vorschlag ist gut, aber der Vorschlag wie er steht hat ernsthafte Probleme, die ihn davon abhalten, angenommen zu werden. Siehe Kommentare im Dokument für Details.

**Dead**
: Der Vorschlag wurde seit langem nicht mehr bearbeitet, und es sieht nicht so aus, als ob jemand ihn bald vervollständigen wird. Er kann wieder "Open" werden, wenn er einen neuen Befürworter findet.

**Needs-Research**
: Es gibt Forschungsprobleme, die gelöst werden müssen, bevor es klar ist, ob der Vorschlag eine gute Idee ist.

**Meta**
: Dies ist kein Vorschlag, sondern ein Dokument über Vorschläge.

**Reserve**
: Dieser Vorschlag ist nicht etwas, das wir derzeit planen zu implementieren, aber wir könnten ihn möglicherweise wiederbeleben, wenn wir beschließen, etwas zu tun, das dem entspricht, was er vorschlägt.

**Informational**
: Dieser Vorschlag ist das letzte Wort darüber, was er tut. Er wird nicht zu einer Spezifikation, es sei denn, jemand kopiert und fügt ihn in eine neue Spezifikation für ein neues Subsystem ein.

Die Herausgeber pflegen den korrekten Status der Vorschläge, basierend auf ungefährer Übereinstimmung und ihrem eigenen Ermessen.

## Vorschlagsnummern

Nummern 000-099 sind für spezielle und Meta-Vorschläge reserviert. 100 und höher werden für tatsächliche Vorschläge verwendet. Nummern werden nicht recycelt.

## Referenzen

* [DEV-FORUM-PROPOSAL](http://zzz.i2p/topics/new?forum_id=7-big-topics-ideas-proposals-and-discussion)
* [TORSPEC-PROCESS](https://gitweb.torproject.org/torspec.git/tree/proposals/001-process.txt)
* [TRAC-PROPOSAL](http://trac.i2p2.i2p/newticket?summary=New%20proposal:%20&type=enhancement&milestone=n/a&component=www/i2p&keywords=review-needed)
