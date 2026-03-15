---
title: "Neuer Verschlüsselungsvorschlags-Template"
aliases:
  - "/de/proposals/142-ecies-template"
  - "/de/proposals/142-ecies-template/"
number: "142"
author: "zzz"
created: "2018-01-11"
lastupdated: "2018-01-20"
status: "Meta"
thread: "http://zzz.i2p/topics/2499"
toc: true
---
## Übersicht

Dieses Dokument beschreibt wichtige Aspekte, die bei der Vorschlagstellung für einen Ersatz oder eine Ergänzung unserer ElGamal- asymmetrischen Verschlüsselung berücksichtigt werden müssen.

Dies ist ein informatives Dokument.


## Motivation

ElGamal ist veraltet und langsam, und es gibt bessere Alternativen.  
Es gibt jedoch mehrere Probleme, die gelöst werden müssen, bevor wir einen neuen Algorithmus hinzufügen oder wechseln können.  
Dieses Dokument hebt diese ungelösten Probleme hervor.


## Hintergrundrecherche

Jeder, der neue Kryptografie vorschlägt, muss zunächst mit den folgenden Dokumenten vertraut sein:

- [Vorschlag 111 NTCP2](/proposals/111-ntcp-2/)
- [Vorschlag 123 LS2](/proposals/123-new-netdb-entries/)
- [Vorschlag 136 experimentelle Sig-Typen](/proposals/136-experimental-sigtypes/)
- [Vorschlag 137 optionale Sig-Typen](/proposals/137-optional-sigtypes/)
- Diskussionsthreads hierzu für jeden der oben genannten Vorschläge, verlinkt innerhalb
- [2018 Vorschlagsprioritäten](http://zzz.i2p/topics/2494)
- [ECIES-Vorschlag](http://zzz.i2p/topics/2418)
- [Übersicht über neue asymmetrische Kryptografie](http://zzz.i2p/topics/1768)
- [Übersicht über Low-Level-Kryptografie](/docs/specs/common-structures/)


## Verwendung asymmetrischer Kryptografie

Zur Erinnerung: Wir verwenden ElGamal für:

1) Tunnel-Build-Nachrichten (Schlüssel ist im RouterIdentity)

2) Router-zu-Router-Verschlüsselung von netdb und anderen I2NP-Nachrichten (Schlüssel ist im RouterIdentity)

3) Client End-to-End ElGamal+AES/SessionTag (Schlüssel ist im LeaseSet, der Destination-Schlüssel wird nicht verwendet)

4) Ephemeres DH für NTCP und SSU


## Design

Jeder Vorschlag zum Ersetzen von ElGamal durch etwas anderes muss die folgenden Details enthalten.


## Spezifikation

Jeder Vorschlag für neue asymmetrische Kryptografie muss die folgenden Dinge vollständig spezifizieren.


### 1. Allgemein

Beantworten Sie die folgenden Fragen in Ihrem Vorschlag. Beachten Sie, dass dies möglicherweise ein separater Vorschlag zu den unten genannten Spezifika unter 2) sein muss, da es mit bestehenden Vorschlägen 111, 123, 136, 137 oder anderen kollidieren könnte.

- Für welche der oben genannten Fälle 1–4 schlagen Sie die Verwendung der neuen Kryptografie vor?
- Falls für 1) oder 2) (Router): Wo wird der öffentliche Schlüssel gespeichert, im RouterIdentity oder in den RouterInfo-Eigenschaften? Beabsichtigen Sie, den Kryptotyp im Schlüsselzertifikat zu verwenden? Spezifizieren Sie dies vollständig. Begründen Sie Ihre Entscheidung in jedem Fall.
- Falls für 3) (Client): Beabsichtigen Sie, den öffentlichen Schlüssel in der Destination zu speichern und den Kryptotyp im Schlüsselzertifikat zu verwenden (wie im ECIES-Vorschlag), oder ihn in LS2 zu speichern (wie im Vorschlag 123), oder etwas anderes? Spezifizieren Sie dies vollständig und begründen Sie Ihre Entscheidung.
- Wie wird die Unterstützung für alle Verwendungen angekündigt? Falls für 3): Wird dies in LS2 eingetragen oder an anderer Stelle? Falls für 1) und 2): Ist es ähnlich wie bei den Vorschlägen 136 und/oder 137? Spezifizieren Sie dies vollständig und begründen Sie Ihre Entscheidungen. Dafür wird wahrscheinlich ein separater Vorschlag benötigt.
- Spezifizieren Sie vollständig, wie und warum dies abwärtskompatibel ist, und legen Sie einen vollständigen Migrationsplan dar.
- Welche noch nicht implementierten Vorschläge sind Voraussetzungen für Ihren Vorschlag?


### 2. Spezifischer Kryptotyp

Beantworten Sie die folgenden Fragen in Ihrem Vorschlag:

- Allgemeine Kryptoinformationen, spezifische Kurven/Parameter, vollständige Begründung Ihrer Wahl. Stellen Sie Links zu Spezifikationen und weiteren Informationen bereit.
- Geschwindigkeitstestergebnisse im Vergleich zu ElG und anderen Alternativen, falls zutreffend. Einschließlich Verschlüsselung, Entschlüsselung und Schlüsselerzeugung.
- Verfügbarkeit der Bibliothek in C++ und Java (sowohl OpenJDK, BouncyCastle als auch Drittanbieter)  
  Für Drittanbieter oder Nicht-Java: Stellen Sie Links und Lizenzen bereit
- Vorgeschlagene Kryptotypnummer(n) (im experimentellen Bereich oder nicht)


## Anmerkungen
