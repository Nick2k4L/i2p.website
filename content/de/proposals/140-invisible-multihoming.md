---
title: "Unsichtbares Multihoming"
number: "140"
author: "str4d"
created: "2017-05-22"
lastupdated: "2017-07-04"
status: "Öffnen"
thread: "http://zzz.i2p/topics/2335"
toc: true
---
## Übersicht

Dieser Vorschlag beschreibt ein Protokoll, das es einem I2P-Client, einer Diensteanwendung oder einem externen Lastverteilungsprozess ermöglicht, mehrere Router transparent zu verwalten, die gemeinsam eine einzelne [Destination](/docs/specs/common-structures/#destination) hosten.

Der Vorschlag legt derzeit keine konkrete Implementierung fest. Er könnte als Erweiterung von [I2CP](/docs/specs/i2cp/) oder als neues Protokoll realisiert werden.


## Motivation

Multihoming bedeutet, dass mehrere Router verwendet werden, um dieselbe Destination zu hosten. Die derzeitige Methode zum Multihoming mit I2P besteht darin, die gleiche Destination unabhängig auf jedem Router auszuführen; der Router, der zu einem bestimmten Zeitpunkt von Clients verwendet wird, ist der letzte, der einen LeaseSet veröffentlicht hat.

Dies ist ein Workaround und funktioniert vermutlich nicht für große Webseiten im großen Maßstab. Angenommen, wir hätten 100 Multihoming-Router, jeder mit 16 Tunneln. Das ergibt 1600 LeaseSet-Veröffentlichungen alle 10 Minuten, also fast 3 pro Sekunde. Die Floodfills würden überlastet und Drosselungen würden greifen. Und das, bevor wir überhaupt den Lookup-Verkehr erwähnen.

Vorschlag 123 löst dieses Problem mit einem Meta-LeaseSet, das die 100 echten LeaseSet-Hashes auflistet. Ein Lookup wird dadurch zu einem zweistufigen Prozess: Zuerst wird das Meta-LeaseSet nachgeschlagen, dann eines der benannten LeaseSets. Dies ist eine gute Lösung für das Problem des Lookup-Verkehrs, erzeugt aber allein betrachtet eine erhebliche Datenschutzlücke: Es ist möglich, festzustellen, welche Multihoming-Router online sind, indem man das veröffentlichte Meta-LeaseSet überwacht, da jedem echten LeaseSet genau ein Router zugeordnet ist.

Wir benötigen eine Möglichkeit, mit der ein I2P-Client oder eine Diensteanwendung eine einzelne Destination über mehrere Router verteilen kann, so dass dies aus Sicht des LeaseSets selbst nicht von der Nutzung eines einzelnen Routers zu unterscheiden ist.


## Design

### Definitionen

    User
        Die Person oder Organisation, die ihre Destination(s) mittels Multihoming betreiben möchte. Eine einzelne Destination wird hier ohne Beschränkung der Allgemeingültigkeit (WLOG) betrachtet.

    Client
        Die Anwendung oder Dienst, die hinter der Destination läuft. Es kann sich um eine Client-, Server- oder Peer-to-Peer-Anwendung handeln; wir bezeichnen sie als Client im Sinne der Verbindung zu den I2P-Routern.

        Der Client besteht aus drei Teilen, die alle im selben Prozess oder auf mehreren Prozessen oder Maschinen verteilt sein können (in einer Multi-Client-Konfiguration):

        Balancer
            Der Teil des Clients, der die Auswahl der Peers und den Aufbau der Tunnel verwaltet. Es gibt zu jedem Zeitpunkt genau einen Balancer, der mit allen I2P-Routern kommuniziert. Es können Failover-Balancer existieren.

        Frontend
            Der Teil des Clients, der parallel betrieben werden kann. Jedes Frontend kommuniziert mit genau einem I2P-Router.

        Backend
            Der Teil des Clients, der von allen Frontends gemeinsam genutzt wird. Er hat keine direkte Kommunikation mit irgendeinem I2P-Router.

    Router
        Ein von dem User betriebener I2P-Router, der an der Grenze zwischen dem I2P-Netzwerk und dem Netzwerk des Users sitzt (vergleichbar mit einem Edge-Gerät in Unternehmensnetzwerken). Er baut Tunnel auf Anweisung des Balancers auf und leitet Pakete für einen Client oder ein Frontend weiter.

### Hochstufige Übersicht

Stellen Sie sich die folgende gewünschte Konfiguration vor:

- Eine Client-Anwendung mit einer Destination.
- Vier Router, von denen jeder drei eingehende Tunnel verwaltet.
- Alle zwölf Tunnel sollen in einem einzigen LeaseSet veröffentlicht werden.

### Einzelner Client

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]-----
                 |-{ [Tunnel 3]===/               \
                 |                                 \
                 |-{ [Tunnel 4]===\                 \
  [Destination]  |-{ [Tunnel 5]====[Router 2]-----   \
    \            |-{ [Tunnel 6]===/               \   \
     [LeaseSet]--|                               [Client]
                 |-{ [Tunnel 7]===\               /   /
                 |-{ [Tunnel 8]====[Router 3]-----   /
                 |-{ [Tunnel 9]===/                 /
                 |                                 /
                 |-{ [Tunnel 10]==\               /
                 |-{ [Tunnel 11]===[Router 4]-----
                  -{ [Tunnel 12]==/
```

### Mehrere Clients

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]---------[Frontend 1]
                 |-{ [Tunnel 3]===/          \                    \
                 |                            \                    \
                 |-{ [Tunnel 4]===\            \                    \
  [Destination]  |-{ [Tunnel 5]====[Router 2]---\-----[Frontend 2]   \
    \            |-{ [Tunnel 6]===/          \   \                \   \
     [LeaseSet]--|                         [Balancer]            [Backend]
                 |-{ [Tunnel 7]===\          /   /                /   /
                 |-{ [Tunnel 8]====[Router 3]---/-----[Frontend 3]   /
                 |-{ [Tunnel 9]===/            /                    /
                 |                            /                    /
                 |-{ [Tunnel 10]==\          /                    /
                 |-{ [Tunnel 11]===[Router 4]---------[Frontend 4]
                  -{ [Tunnel 12]==/
```

### Allgemeiner Client-Prozess

- Laden oder Generieren einer Destination.

- Öffnen einer Sitzung mit jedem Router, gebunden an die Destination.

- In regelmäßigen Abständen (ca. alle zehn Minuten, abhängig von der Tunnel-Lebensdauer):

  - Abrufen der Fast-Tier-Liste von jedem Router.

  - Verwenden der Gesamtmenge der Peers, um Tunnel zu bzw. von jedem Router aufzubauen.

    - Standardmäßig werden Tunnel zu/von einem bestimmten Router Peers aus dessen Fast-Tier verwenden, dies wird jedoch nicht durch das Protokoll erzwungen.

  - Sammeln der Menge aktiver eingehender Tunnel von allen aktiven Routern und Erstellen eines LeaseSets.

  - Veröffentlichen des LeaseSets über einen oder mehrere der Router.

### Unterschiede zu I2CP

Um diese Konfiguration zu erstellen und zu verwalten, benötigt der Client folgende neue Funktionen, die über das derzeitige Angebot von [I2CP](/docs/specs/i2cp/) hinausgehen:

- Einen Router anweisen, Tunnel aufzubauen, ohne dafür ein LeaseSet zu erstellen.
- Abrufen einer Liste der aktuellen Tunnel im eingehenden Pool.

Zusätzlich würden die folgenden Funktionen eine erhebliche Flexibilität bei der Tunnelverwaltung durch den Client ermöglichen:

- Abrufen des Inhalts der Fast-Tier-Liste eines Routers.
- Einen Router anweisen, einen eingehenden oder ausgehenden Tunnel unter Verwendung einer gegebenen Liste von Peers aufzubauen.

### Protokoll-Übersicht

```
         Client                           Router

                    --------------------->  Create Session
   Session Status  <---------------------
                    --------------------->  Get Fast Tier
        Peer List  <---------------------
                    --------------------->  Create Tunnel
    Tunnel Status  <---------------------
                    --------------------->  Get Tunnel Pool
      Tunnel List  <---------------------
                    --------------------->  Publish LeaseSet
                    --------------------->  Send Packet
      Send Status  <---------------------
  Packet Received  <---------------------
```

### Nachrichten

**Create Session**
- Erstellt eine Sitzung für die angegebene Destination.

**Session Status**
- Bestätigung, dass die Sitzung eingerichtet wurde und der Client nun mit dem Aufbau von Tunneln beginnen kann.

**Get Fast Tier**
- Fordert eine Liste der Peers an, über die der Router derzeit Tunnel aufbauen würde.

**Peer List**
- Eine Liste der dem Router bekannten Peers.

**Create Tunnel**
- Fordert den Router auf, einen neuen Tunnel über die angegebenen Peers aufzubauen.

**Tunnel Status**
- Das Ergebnis eines bestimmten Tunnelaufbaus, sobald verfügbar.

**Get Tunnel Pool**
- Fordert eine Liste der aktuellen Tunnel im eingehenden oder ausgehenden Pool für die Destination an.

**Tunnel List**
- Eine Liste der Tunnel für den angeforderten Pool.

**Publish LeaseSet**
- Fordert den Router auf, das bereitgestellte LeaseSet über einen der ausgehenden Tunnel für die Destination zu veröffentlichen. Kein Antwortstatus ist erforderlich; der Router sollte es weiterhin versuchen, bis er überzeugt ist, dass das LeaseSet veröffentlicht wurde.

**Send Packet**
- Ein ausgehendes Paket vom Client. Kann optional einen ausgehenden Tunnel angeben, über den das Paket gesendet werden muss (sollte?).

**Send Status**
- Informiert den Client über den Erfolg oder Misserfolg beim Senden eines Pakets.

**Packet Received**
- Ein eingehendes Paket für den Client. Kann optional den eingehenden Tunnel angeben, über den das Paket empfangen wurde(?)


## Sicherheitsimplikationen

Aus Sicht der Router ist dieses Design funktional äquivalent zum Status quo. Der Router baut weiterhin alle Tunnel auf, verwaltet seine eigenen Peer-Profile und stellt die Trennung zwischen Router- und Client-Operationen sicher. In der Standardkonfiguration ist es vollständig identisch, da die Tunnel für diesen Router aus dessen eigenem Fast-Tier aufgebaut werden.

Aus Sicht der netDB ist ein einzelnes LeaseSet, das über dieses Protokoll erstellt wurde, identisch zum Status quo, da es auf bereits vorhandenen Funktionen aufbaut. Bei größeren LeaseSets, die nahe an 16 Leases liegen, könnte es jedoch für einen Beobachter möglich sein, festzustellen, dass das LeaseSet multihomed ist:

- Die aktuelle maximale Größe des Fast-Tiers beträgt 75 Peers. Der Inbound Gateway (IBGW, der im Lease veröffentlichte Knoten) wird aus einem Teil des Tiers ausgewählt (zufällig pro Tunnel-Pool nach Hash partitioniert, nicht nach Anzahl):

      1 Hop
          Das gesamte Fast-Tier

      2 Hops
          Die Hälfte des Fast-Tiers
          (Standard bis Mitte 2014)

      3+ Hops
          Ein Viertel des Fast-Tiers
          (3 ist derzeit der Standard)

  Das bedeutet, dass die IBGWs im Durchschnitt aus einer Menge von 20–30 Peers stammen.

- Bei einer Single-Homed-Konfiguration hätte ein vollständiges 16-Tunnel-LeaseSet 16 IBGWs, die zufällig aus einer Menge von bis zu (sagen wir) 20 Peers ausgewählt wurden.

- Bei einer 4-Router-Multihoming-Konfiguration mit Standardkonfiguration hätte ein vollständiges 16-Tunnel-LeaseSet 16 IBGWs, die zufällig aus einer Menge von maximal 80 Peers ausgewählt wurden, wobei wahrscheinlich einige gemeinsame Peers zwischen den Routern existieren.

Somit könnte es bei der Standardkonfiguration durch statistische Analyse möglich sein, festzustellen, dass ein LeaseSet mit diesem Protokoll generiert wurde. Es könnte auch möglich sein, die Anzahl der Router zu ermitteln, obwohl der Effekt von Churn auf den Fast-Tiers die Wirksamkeit dieser Analyse verringern würde.

Da der Client vollständige Kontrolle darüber hat, welche Peers er auswählt, könnte diese Informationsverluste reduziert oder eliminiert werden, indem IBGWs aus einer reduzierten Menge von Peers ausgewählt werden.


## Kompatibilität

Dieses Design ist vollständig rückwärtskompatibel mit dem Netzwerk, da sich das LeaseSet-Format nicht ändert. Alle Router müssten das neue Protokoll kennen, dies ist jedoch kein Problem, da sie alle von derselben Entität kontrolliert würden.


## Leistungs- und Skalierbarkeitshinweise

Die Obergrenze von 16 Leases pro LeaseSet bleibt durch diesen Vorschlag unverändert. Für Destinationen, die mehr Tunnel benötigen, gibt es zwei mögliche Netzwerkänderungen:

- Erhöhung der Obergrenze für die Größe von LeaseSets. Dies wäre die einfachste Implementierung (obwohl sie immer noch eine umfassende Netzwerkunterstützung erfordern würde, bevor sie weit verbreitet genutzt werden könnte), könnte aber zu langsameren Lookups aufgrund größerer Paketgrößen führen. Die maximal praktikable Größe eines LeaseSets wird durch die MTU der zugrundeliegenden Transporte definiert und beträgt daher etwa 16 kB.

- Implementierung von Vorschlag 123 für hierarchische LeaseSets. In Kombination mit diesem Vorschlag könnten die Destinationen der Unter-LeaseSets auf mehrere Router verteilt werden, was effektiv wie mehrere IP-Adressen für einen Clearnet-Dienst wirkt.


## Danksagungen

Vielen Dank an psi für die Diskussion, die zu diesem Vorschlag geführt hat.


## Referenzen

* [Destination](/docs/specs/common-structures/#destination)
* [I2CP](/docs/specs/i2cp/)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [Prop123](/proposals/123-new-netdb-entries/)
