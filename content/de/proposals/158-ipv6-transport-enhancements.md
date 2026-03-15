---
title: "IPv6 Transportverbesserungen"
aliases:
  - "/de/spec/proposals/158"
  - "/de/spec/proposals/158/"
number: "158"
author: "zzz, orignal"
created: "2021-03-19"
lastupdated: "2021-04-26"
status: "Closed"
thread: "http://zzz.i2p/topics/3060"
target: "0.9.50"
toc: true
---
## Hinweis
Netzwerk-Deployment und Tests sind im Gange.
Kleine Überarbeitungen vorbehalten.


## Übersicht

Dieser Vorschlag sieht Verbesserungen der SSU- und NTCP2-Transportschichten für IPv6 vor.


## Motivation

Da IPv6 weltweit zunehmend verbreitet ist und IPv6-only-Konfigurationen (insbesondere auf Mobilgeräten) immer häufiger werden,
müssen wir unsere IPv6-Unterstützung verbessern und die Annahme fallenlassen,
dass alle Router IPv4-fähig sind.



### Verbindungsprüfung

Beim Auswählen von Peers für Tunnel oder beim Auswählen von OBEP/IBGW-Pfaden zur Weiterleitung von Nachrichten
ist es hilfreich zu ermitteln, ob Router A eine Verbindung zu Router B herstellen kann.
Im Allgemeinen bedeutet dies, festzustellen, ob A über eine ausgehende Fähigkeit für einen Transport und Adresstyp (IPv4/v6) verfügt,
die zu einer der von B angekündigten eingehenden Adressen passt.

In vielen Fällen kennen wir jedoch A's Fähigkeiten nicht und müssen Annahmen treffen.
Wenn A versteckt oder hinter einer Firewall ist, werden die Adressen nicht veröffentlicht, und wir haben keine direkten Informationen –
daher nehmen wir an, dass A IPv4-fähig, aber nicht IPv6-fähig ist.
Die Lösung besteht darin, zwei neue „caps“ oder Fähigkeiten zum Router-Info hinzuzufügen, um ausgehende Fähigkeiten für IPv4 und IPv6 anzugeben.


### IPv6-Introducer

Unsere Spezifikationen für SSU enthalten Fehler und Inkonsistenzen bezüglich der Frage,
ob IPv6-Introducer für IPv4-Introductionen unterstützt werden.
In jedem Fall wurde dies bisher weder in Java I2P noch in i2pd implementiert.
Dies muss korrigiert werden.


### IPv6-Introductionen

Unsere Spezifikationen für SSU legen klar fest,
dass IPv6-Introductionen nicht unterstützt werden.
Dies basierte auf der Annahme, dass IPv6 niemals durch eine Firewall blockiert wird.
Dies ist eindeutig nicht zutreffend, und wir müssen die Unterstützung für hinter einer Firewall befindliche IPv6-Router verbessern.


### Einführungsdiagramme

Legende: ----- ist IPv4, ====== ist IPv6

**Aktuell nur IPv4:**

```
        Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**IPv4-Introduction, IPv6-Introducer:**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**IPv6-Introduction, IPv6-Introducer:**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```

**IPv6-Introduction, IPv4-Introducer:**

```
Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```


## Design

Es müssen drei Änderungen implementiert werden.

- Hinzufügen der Fähigkeiten „4“ und „6“ zu den Router-Adress-Fähigkeiten, um ausgehende IPv4- und IPv6-Unterstützung anzugeben
- Unterstützung für IPv4-Introductionen über IPv6-Introducer hinzufügen
- Unterstützung für IPv6-Introductionen über IPv4- und IPv6-Introducer hinzufügen



## Spezifikation

### 4/6-Fähigkeiten (Caps)

Diese wurde ursprünglich ohne formellen Vorschlag implementiert, ist aber erforderlich für
IPv6-Introductionen, daher wird sie hier aufgenommen.

Zwei neue Fähigkeiten „4“ und „6“ werden definiert.
Diese neuen Fähigkeiten werden der „caps“-Eigenschaft in der Router-Adresse hinzugefügt, nicht zu den Router-Info-Fähigkeiten.
Derzeit ist für NTCP2 keine „caps“-Eigenschaft definiert.
Eine SSU-Adresse mit Introducer ist per Definition aktuell immer ipv4. Wir unterstützen keine ipv6-Introduction.
Dieser Vorschlag ist jedoch kompatibel mit IPv6-Introductionen. Siehe unten.

Zusätzlich kann ein Router eine Verbindung über ein Overlay-Netzwerk wie I2P-over-Yggdrasil unterstützen,
möchte jedoch keine Adresse veröffentlichen, oder diese Adresse hat kein standardmäßiges IPv4- oder IPv6-Format.
Das neue Fähigkeitssystem sollte flexibel genug sein, um auch diese Netzwerke zu unterstützen.

Folgende Änderungen werden definiert:

NTCP2: „caps“-Eigenschaft hinzufügen

SSU: Unterstützung für eine Router-Adresse ohne Host oder Introducer hinzufügen, um ausgehende Unterstützung
für IPv4, IPv6 oder beides anzugeben.

Beide Transportschichten: Folgende caps-Werte definieren:

- „4“: IPv4-Unterstützung
- „6“: IPv6-Unterstützung

Mehrere Werte können in einer einzigen Adresse unterstützt werden. Siehe unten.
Mindestens einer dieser caps ist obligatorisch, wenn kein „host“-Wert in der Router-Adresse enthalten ist.
Höchstens einer dieser caps ist optional, wenn ein „host“-Wert in der Router-Adresse enthalten ist.
Zukünftig können zusätzliche Transport-Fähigkeiten definiert werden, um Unterstützung für Overlay-Netzwerke oder andere Verbindungen anzugeben.


#### Anwendungsfälle und Beispiele

SSU:

SSU mit Host: 4/6 optional, niemals mehr als einer.
Beispiel: SSU caps="4" host="1.2.3.4" key=... port="1234"

SSU nur ausgehend für eine, andere wird veröffentlicht: Nur caps, 4/6.
Beispiel: SSU caps="6"

SSU mit Introducer: niemals kombiniert. 4 oder 6 ist erforderlich.
Beispiel: SSU caps="4" iexp0=... ihost0=... iport0=... itag0=... key=...

SSU versteckt: Nur caps, 4, 6 oder 46. Mehrfach erlaubt.
Kein Bedarf an zwei Adressen, eine mit 4 und eine mit 6.
Beispiel: SSU caps="46"

NTCP2:

NTCP2 mit Host: 4/6 optional, niemals mehr als einer.
Beispiel: NTCP2 caps="4" host="1.2.3.4" i=... port="1234" s=... v="2"

NTCP2 nur ausgehend für eine, andere wird veröffentlicht: caps, s, v nur, 4/6/y, mehrfach erlaubt.
Beispiel: NTCP2 caps="6" i=... s=... v="2"

NTCP2 versteckt: caps, s, v nur 4/6, mehrfach erlaubt. Kein Bedarf an zwei Adressen, eine mit 4 und eine mit 6.
Beispiel: NTCP2 caps="46" i=... s=... v="2"



### IPv6-Introducer für IPv4

Die folgenden Änderungen sind erforderlich, um Fehler und Inkonsistenzen in den Spezifikationen zu korrigieren.
Wir haben dies auch als „Teil 1“ des Vorschlags bezeichnet.

#### Spezifikationsänderungen

Die SSU-Spezifikation sagt aktuell (IPv6-Anmerkungen):

IPv6 wird ab Version 0.9.8 unterstützt. Veröffentlichte Relay-Adressen können IPv4 oder IPv6 sein, und die Kommunikation zwischen Alice und Bob kann über IPv4 oder IPv6 erfolgen.

Folgendes hinzufügen:

Obwohl die Spezifikation ab Version 0.9.8 geändert wurde, wurde die Kommunikation zwischen Alice und Bob über IPv6 erst ab Version 0.9.50 tatsächlich unterstützt.
Ältere Versionen von Java-Routern veröffentlichten fälschlicherweise die 'C'-Fähigkeit für IPv6-Adressen,
obwohl sie nicht tatsächlich als Introducer über IPv6 fungierten.
Daher sollten Router die 'C'-Fähigkeit für eine IPv6-Adresse nur vertrauen, wenn die Router-Version 0.9.50 oder höher ist.



Die SSU-Spezifikation sagt aktuell (Relay Request):

Die IP-Adresse wird nur dann enthalten, wenn sie sich von der Quelladresse und dem Port des Pakets unterscheidet.
In der aktuellen Implementierung ist die IP-Länge immer 0 und der Port immer 0,
und der Empfänger sollte die Quelladresse und den Port des Pakets verwenden.
Diese Nachricht kann über IPv4 oder IPv6 gesendet werden. Bei IPv6 muss Alice ihre IPv4-Adresse und ihren Port angeben.

Folgendes hinzufügen:

Die IP-Adresse und der Port müssen enthalten sein, um eine IPv4-Adresse einzuführen, wenn diese Nachricht über IPv6 gesendet wird.
Dies wird ab Release 0.9.50 unterstützt.



### IPv6-Introductionen

Alle drei SSU-Relay-Nachrichten (RelayRequest, RelayResponse und RelayIntro) enthalten IP-Längenfelder,
um die Länge der (Alice, Bob oder Charlie) IP-Adresse anzugeben, die folgt.

Daher ist keine Änderung am Format der Nachrichten erforderlich.
Nur textuelle Änderungen an den Spezifikationen, die darauf hinweisen, dass 16-Byte-IP-Adressen erlaubt sind.

Die folgenden Änderungen sind an den Spezifikationen erforderlich.
Wir haben dies auch als „Teil 2“ des Vorschlags bezeichnet.


#### Spezifikationsänderungen

Die SSU-Spezifikation sagt aktuell (IPv6-Anmerkungen):

Die Kommunikation zwischen Bob und Charlie sowie zwischen Alice und Charlie erfolgt ausschließlich über IPv4.

Die SSU-Spezifikation sagt aktuell (Relay Request):

Es gibt keine Pläne, Relaying für IPv6 zu implementieren.

Ändern in:

Relaying für IPv6 wird ab Release 0.9.xx unterstützt.

Die SSU-Spezifikation sagt aktuell (Relay Response):

Die IP-Adresse von Charlie muss IPv4 sein, da dies die Adresse ist, an die Alice die SessionRequest nach dem Hole Punch sendet.
Es gibt keine Pläne, Relaying für IPv6 zu implementieren.

Ändern in:

Die IP-Adresse von Charlie kann IPv4 oder, ab Release 0.9.xx, IPv6 sein.
Das ist die Adresse, an die Alice die SessionRequest nach dem Hole Punch sendet.
Relaying für IPv6 wird ab Release 0.9.xx unterstützt.

Die SSU-Spezifikation sagt aktuell (Relay Intro):

Die IP-Adresse von Alice ist in der aktuellen Implementierung immer 4 Bytes lang, da Alice versucht, eine Verbindung zu Charlie über IPv4 herzustellen.
Diese Nachricht muss über eine etablierte IPv4-Verbindung gesendet werden,
da dies der einzige Weg ist, wie Bob Charlies IPv4-Adresse kennt, um sie Alice in der RelayResponse zurückzugeben.

Ändern in:

Für IPv4 ist die IP-Adresse von Alice immer 4 Bytes lang, da Alice versucht, eine Verbindung zu Charlie über IPv4 herzustellen.
Ab Release 0.9.xx wird IPv6 unterstützt, und die IP-Adresse von Alice kann 16 Bytes lang sein.

Für IPv4 muss diese Nachricht über eine etablierte IPv4-Verbindung gesendet werden,
da dies der einzige Weg ist, wie Bob Charlies IPv4-Adresse kennt, um sie Alice in der RelayResponse zurückzugeben.
Ab Release 0.9.xx wird IPv6 unterstützt, und diese Nachricht kann über eine etablierte IPv6-Verbindung gesendet werden.

Außerdem hinzufügen:

Ab Release 0.9.xx muss jede veröffentlichte SSU-Adresse mit Introducer „4“ oder „6“ in der „caps“-Option enthalten.


## Migration

Alle alten Router sollten die caps-Eigenschaft in NTCP2 sowie unbekannte Fähigkeitszeichen in der SSU-caps-Eigenschaft ignorieren.

Jede SSU-Adresse mit Introducer, die keine „4“- oder „6“-Fähigkeit enthält, wird als für IPv4-Introduction angenommen.


## Referenzen

* [CAPS](http://zzz.i2p/topics/3050)
* [NTCP2](/docs/specs/ntcp2/)
* [SSU](/docs/specs/ssu2/)
* [SSU-SPEC](/docs/legacy/ssu/)
