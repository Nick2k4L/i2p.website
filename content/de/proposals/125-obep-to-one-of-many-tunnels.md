---
title: "OBEP-Lieferung an 1-von-N oder N-von-N-Tunnel"
number: "125"
author: "zzz, str4d"
created: "2016-03-10"
lastupdated: "2017-04-07"
status: "Offen"
thread: "http://zzz.i2p/topics/2099"
toc: true
---
## Übersicht

Dieser Vorschlag umfasst zwei Verbesserungen zur Steigerung der Netzwerkleistung:

- Die Übertragung der Auswahl des IBGW an das OBEP, indem diesem eine Liste von
  Alternativen statt einer einzelnen Option bereitgestellt wird.

- Die Aktivierung der Multicast-Paketweiterleitung am OBEP.


## Motivation

Im Fall einer direkten Verbindung soll die Verbindungskapazität entlastet werden, indem dem OBEP Flexibilität bei der Verbindungsherstellung zu IBGWs gegeben wird. Die Möglichkeit, mehrere Tunnel anzugeben, ermöglicht es uns zudem, Multicast am OBEP zu implementieren (indem die Nachricht an alle angegebenen Tunnel übermittelt wird).

Eine Alternative zum Delegierungsteil dieses Vorschlags wäre, einen LeaseSet-Hash zu übermitteln, ähnlich der bestehenden Möglichkeit, einen Ziel-[RouterIdentity](/docs/specs/common-structures/#common-structure-specification)-Hash anzugeben. Dies würde zu einer kleineren Nachricht und potenziell einem neueren LeaseSet führen. Allerdings:

1. Es würde das OBEP zwingen, eine Nachschlageoperation durchzuführen.

2. Der LeaseSet könnte nicht auf einem Floodfill veröffentlicht sein, sodass die Nachschlageoperation fehlschlägt.

3. Der LeaseSet könnte verschlüsselt sein, sodass das OBEP die Leases nicht extrahieren könnte.

4. Die Angabe eines LeaseSet offenbart dem OBEP das [Destination](/docs/specs/common-structures/#destination) der Nachricht,
   welches es andernfalls nur entdecken könnte, indem es alle LeaseSets im Netzwerk durchsucht und nach einer Lease-Übereinstimmung sucht.


## Design

Der Initiator (OBGW) würde einige (alle?) der Ziel-[Leases](/docs/specs/common-structures/#lease) in die Zustellanweisungen [TUNNEL-DELIVERY](/docs/specs/i2np/#tunnel-message-delivery-instructions) einfügen, anstatt nur einen auszuwählen.

Das OBEP würde dann einen dieser Leases zur Zustellung auswählen. Wenn verfügbar, würde das OBEP einen Lease auswählen, zu dem es bereits verbunden ist oder den es bereits kennt. Dies würde den OBEP-IBGW-Pfad schneller und zuverlässiger machen und die Gesamtanzahl der Netzwerkverbindungen reduzieren.

Wir haben einen ungenutzten Zustelltyp (0x03) und zwei verbleibende Bits (0 und 1) in den Flags für TUNNEL-DELIVERY, die wir nutzen können, um diese Funktionen zu implementieren.


## Sicherheitsimplikationen

Dieser Vorschlag verändert nicht die Menge an Informationen, die über das Ziel-Destination des OBGW oder dessen Sicht auf die NetDB preisgegeben wird:

- Ein Angreifer, der das OBEP kontrolliert und LeaseSets aus der NetDB extrahiert, kann bereits feststellen, ob eine Nachricht an ein bestimmtes Destination gesendet wird, indem er nach dem TunnelId-/RouterIdentity-Paar sucht. Im schlimmsten Fall könnte die Anwesenheit mehrerer Leases im TMDI die Suche nach einer Übereinstimmung in der Datenbank des Angreifers beschleunigen.

- Ein Angreifer, der ein bösartiges Destination betreibt, kann bereits Informationen über die Sicht des verbindenden Opfers auf die NetDB gewinnen, indem er LeaseSets mit verschiedenen eingehenden Tunneln auf unterschiedlichen Floodfills veröffentlicht und beobachtet, über welche Tunnel das OBGW sich verbindet. Aus ihrer Sicht ist die Auswahl des zu verwendenden Tunnels durch das OBEP funktional identisch mit der Auswahl durch das OBGW.

Das Multicast-Flag gibt preis, dass das OBGW eine Multicast-Übertragung durchführt, und zwar gegenüber den OBEPs. Dies schafft einen Kompromiss zwischen Leistung und Privatsphäre, der bei der Implementierung höherer Protokolle berücksichtigt werden sollte. Da es sich um ein optionales Flag handelt, können Benutzer die passende Entscheidung für ihre Anwendung treffen. Es könnte vorteilhaft sein, dieses Verhalten als Standard für kompatible Anwendungen festzulegen, da eine breite Nutzung durch verschiedene Anwendungen die Informationspreisgabe darüber verringern würde, von welcher spezifischen Anwendung eine Nachricht stammt.


## Spezifikation

Die First Fragment Delivery Instructions würden wie folgt modifiziert:

```
+----+----+----+----+----+----+----+----+
  |flag|  Tunnel ID (opt)  |              |
  +----+----+----+----+----+              +
  |                                       |
  +                                       +
  |         To Hash (optional)            |
  +                                       +
  |                                       |
  +                        +----+----+----+
  |                        |dly | Message
  +----+----+----+----+----+----+----+----+
   ID (opt) |extended opts (opt)|cnt | (o)
  +----+----+----+----+----+----+----+----+
   Tunnel ID N   |                        |
  +----+----+----+                        +
  |                                       |
  +                                       +
  |         To Hash N (optional)          |
  +                                       +
  |                                       |
  +              +----+----+----+----+----+
  |              | Tunnel ID N+1 (o) |    |
  +----+----+----+----+----+----+----+    +
  |                                       |
  +                                       +
  |         To Hash N+1 (optional)        |
  +                                       +
  |                                       |
  +                                  +----+
  |                                  | sz
  +----+----+----+----+----+----+----+----+
       |
  +----+

flag ::
       1 byte
       Bit-Reihenfolge: 76543210
       Bits 6-5: Zustelltyp
                 0x03 = TUNNELS
       Bit 0: Multicast? Wenn 0, Zustellung an einen der Tunnel
                         Wenn 1, Zustellung an alle Tunnel
                         Auf 0 setzen für Kompatibilität mit zukünftigen Verwendungen,
                         wenn der Zustelltyp nicht TUNNELS ist

Count ::
       1 byte
       Optional, vorhanden wenn Zustelltyp TUNNELS ist
       2-255 - Anzahl der folgenden ID/Hash-Paare

Tunnel ID :: TunnelId
To Hash ::
       jeweils 36 bytes
       Optional, vorhanden wenn Zustelltyp TUNNELS ist
       ID/Hash-Paare

Gesamtlänge: Typische Länge ist:
       75 bytes für Count 2 TUNNELS Zustellung (nicht fragmentierte Tunnelnachricht);
       79 bytes für Count 2 TUNNELS Zustellung (erstes Fragment)

Rest der Zustellanweisungen unverändert
```


## Kompatibilität

Die einzigen Peers, die die neue Spezifikation verstehen müssen, sind die OBGWs und die OBEPs. Wir können diese Änderung daher mit dem bestehenden Netzwerk kompatibel machen, indem wir ihre Nutzung vom Ziel-I2P-Version abhängig machen:

* Die OBGWs müssen beim Aufbau ausgehender Tunnel kompatible OBEPs auswählen, basierend auf der in deren [RouterInfo](/docs/specs/common-structures/#routerinfo) angegebenen I2P-Version.

* Peers, die die Zielversion angeben, müssen das Parsen der neuen Flags unterstützen und dürfen die Anweisungen nicht als ungültig ablehnen.


## Referenzen

* [Destination](/docs/specs/common-structures/#destination)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [RouterIdentity](/docs/specs/common-structures/#routeridentity)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TUNNEL-DELIVERY](/docs/specs/common-structures/#tunnelmessagedeliveryinstructions)
* [TunnelId](/docs/specs/common-structures/#tunnelid)
* [VERSIONS](/docs/specs/i2np/#protocol-versions)
