---
title: "Introducer-Verfall"
number: "133"
author: "zzz"
created: "2017-02-05"
lastupdated: "2017-08-09"
status: "Geschlossen"
thread: "http://zzz.i2p/topics/2230"
target: "0.9.30"
implementedin: "0.9.30"
toc: true
---
## Übersicht

Dieser Vorschlag zielt darauf ab, die Erfolgsrate bei Einführungen (Introductions) zu verbessern.


## Motivation

Einführer (Introducers) verfallen nach einer bestimmten Zeit, diese Information wird jedoch nicht in der Router-Info veröffentlicht. Derzeit müssen Router Heuristiken verwenden, um abzuschätzen, wann ein Einführer nicht mehr gültig ist.


## Design

In einer SSU-Router-Adresse, die Einführer enthält, kann der Herausgeber optional für jeden Einführer Ablaufzeiten angeben.


## Spezifikation

```
iexp{X}={nnnnnnnnnn}

X :: Die Nummer des Einführers (0-2)

nnnnnnnnnn :: Die Zeit in Sekunden (nicht ms) seit der Epoche.
```

### Hinweise

* Jede Ablaufzeit muss größer als das Veröffentlichungsdatum der Router-Info sein und weniger als 6 Stunden nach dem Veröffentlichungsdatum der Router-Info liegen.

* Herausgebende Router und Einführer sollten versuchen, den Einführer bis zum Ablauf gültig zu halten; es gibt jedoch keine Möglichkeit, dies zu garantieren.

* Router sollten einen veröffentlichten Einführer nach dessen Ablauf nicht mehr verwenden.

* Die Ablaufzeiten der Einführer befinden sich in der Router-Adresse-Zuordnung.  
  Es handelt sich nicht um das (derzeit ungenutzte) 8-Byte-Ablauf-Feld in der Router-Adresse.

**Beispiel:** `iexp0=1486309470`


## Migration

Keine Probleme. Die Implementierung ist optional.  
Die Abwärtskompatibilität ist sichergestellt, da ältere Router unbekannte Parameter ignorieren.


## Referenzen

* [RouterAddress](/docs/specs/common-structures/#routeraddress)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TRAC-TICKET](http://trac.i2p2.i2p/ticket/1352)
