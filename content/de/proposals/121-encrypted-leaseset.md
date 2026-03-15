---
title: "Verschlüsselter LeaseSet"
number: "121"
author: "zzz"
created: "2016-01-11"
lastupdated: "2016-01-12"
status: "Abgelehnt"
thread: "http://zzz.i2p/topics/2047"
supercededby: "123"
toc: true
---
## Überblick

Dieses Vorschlag betrifft die Neugestaltung des Mechanismus für die Verschlüsselung von LeaseSets.


## Motivation

Die aktuelle verschlüsselte LS ist schrecklich und unsicher. Ich kann das sagen, ich habe sie entworfen und implementiert.

Gründe:

- AES CBC verschlüsselt
- Ein einzelner AES-Schlüssel für alle
- Lease-Abläufe sind immer noch offen gelegt
- Verschlüsselungs-Public-Key ist immer noch offen gelegt


## Design

### Ziele

- Das gesamte Ding undurchsichtig machen
- Schlüssel für jeden Empfänger


### Strategie

Machen wir es wie GPG/OpenPGP. Asymmetrisch verschlüsseln eines symmetrischen Schlüssels für jeden Empfänger. Daten werden mit diesem asymmetrischen Schlüssel entschlüsselt. Siehe z. B. [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
Wenn wir einen Algorithmus finden, der klein und schnell ist.

Das Problem ist, einen asymmetrischen Verschlüsselungsalgorithmus zu finden, der klein und schnell ist. ElGamal mit 514 Byte ist hier ein wenig schmerzhaft. Wir können es besser machen.

Siehe z. B. http://security.stackexchange.com/questions/824...

Dies funktioniert für kleine Empfängerzahlen (oder eigentlich, Schlüssel; Sie können Schlüssel immer noch an mehrere Personen verteilen, wenn Sie möchten).


## Spezifikation

- Ziel
- Veröffentlichte Zeitstempel
- Ablauf
- Flags
- Länge der Daten
- Verschlüsselte Daten
- Signatur

Die verschlüsselten Daten könnten mit einem enctype-Spezifizierer vorangestellt werden oder nicht.


## Referenzen

* [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
