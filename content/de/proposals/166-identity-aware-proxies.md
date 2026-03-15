---
title: "I2P Vorschlag #166: Identitäts-/Hostbewusste Tunneltypen"
number: "166"
author: "eyedeekay"
created: "2024-05-27"
lastupdated: "2024-08-27"
status: "Offen"
thread: "http://i2pforum.i2p/viewforum.php?f=13"
target: "0.9.65"
toc: true
---
### Vorschlag für einen host-bewussten HTTP-Proxy-Tunneltyp

Dies ist ein Vorschlag zur Behebung des „Shared Identity Problems“ bei der herkömmlichen Verwendung von HTTP-over-I2P durch die Einführung eines neuen HTTP-Proxy-Tunneltyps. Dieser Tunneltyp verfügt über ergänzendes Verhalten, das darauf abzielt, die Nutzbarkeit von Tracking durch potenziell feindliche Hidden-Service-Betreiber gegenüber gezielten User-Agents (Browsern) und der I2P-Clientanwendung selbst zu verhindern oder einzuschränken.

#### Was ist das „Shared Identity“-Problem?

Das „Shared Identity“-Problem tritt auf, wenn ein User-Agent in einem kryptografisch adressierten Overlay-Netzwerk eine kryptografische Identität mit einem anderen User-Agent teilt. Dies geschieht beispielsweise, wenn Firefox und GNU Wget beide so konfiguriert sind, dass sie denselben HTTP-Proxy verwenden.

In diesem Szenario kann der Server die kryptografische Adresse (Destination), die zur Beantwortung der Aktivität verwendet wird, sammeln und speichern. Er kann diese als „Fingerprint“ behandeln, der immer zu 100 % eindeutig ist, da sie kryptografischen Ursprungs ist. Das bedeutet, dass die durch das Shared-Identity-Problem beobachtete Verknüpfbarkeit perfekt ist.

Aber ist es ein Problem?
^^^^^^^^^^^^^^^^^^^^

Das Shared-Identity-Problem ist ein Problem, wenn User-Agents, die dasselbe Protokoll verwenden, Unverknüpfbarkeit wünschen. [Es wurde erstmals im Kontext von HTTP in diesem Reddit-Thread erwähnt](https://old.reddit.com/r/i2p/comments/579idi/warning_i2p_is_linkablefingerprintable/), wobei die gelöschten Kommentare dank [pullpush.io](https://api.pullpush.io/reddit/search/comment/?link_id=579idi) zugänglich sind. *Zu dieser Zeit* war ich einer der aktivsten Antwortenden, und *zu dieser Zeit* glaubte ich, dass das Problem gering sei. In den letzten 8 Jahren hat sich die Situation und meine Einschätzung geändert. Ich glaube nun, dass die durch bösartige Destination-Korrelation verursachte Bedrohung erheblich wächst, je mehr Seiten in der Lage sind, bestimmte Nutzer zu „profilieren“.

Dieser Angriff hat eine sehr niedrige Einstiegshürde. Es erfordert lediglich, dass ein Hidden-Service-Betreiber mehrere Dienste betreibt. Für Angriffe auf zeitgleiche Besuche (mehrere Seiten gleichzeitig besuchen) ist dies die einzige Voraussetzung. Für nicht-zeitgleiche Verknüpfungen muss einer dieser Dienste ein Dienst sein, der „Accounts“ hostet, die einem einzelnen Nutzer gehören, der zum Tracking ausgewählt wurde.

Derzeit kann jeder Dienstbetreiber, der Benutzerkonten hostet, diese mit Aktivitäten über alle von ihm kontrollierten Seiten korrelieren, indem er das Shared-Identity-Problem ausnutzt. Mastodon, Gitlab oder sogar einfache Foren könnten Angreifer im Verborgenen sein, solange sie mehr als einen Dienst betreiben und daran interessiert sind, ein Profil für einen Nutzer zu erstellen. Diese Überwachung könnte aus Gründen der Stalking, finanziellen Gewinns oder Geheimdienstzwecken durchgeführt werden. Derzeit gibt es Dutzende großer Betreiber, die diesen Angriff durchführen und sinnvolle Daten daraus gewinnen könnten. Wir vertrauen ihnen derzeit größtenteils, dass sie es nicht tun, aber Akteure, denen unsere Meinung egal ist, könnten leicht auftauchen.

Dies hängt direkt mit einer ziemlich grundlegenden Form des Profilings im klaren Web zusammen, bei der Organisationen Interaktionen auf ihrer Website mit Interaktionen in von ihnen kontrollierten Netzwerken korrelieren können. Auf I2P ist diese Technik aufgrund der Eindeutigkeit der kryptografischen Destination manchmal sogar zuverlässiger, wenngleich ohne die zusätzliche Macht der Geolokalisierung.

Das Shared Identity ist nicht nützlich gegen einen Nutzer, der I2P ausschließlich zur Verschleierung der Geolokalisierung verwendet. Es kann auch nicht verwendet werden, um I2Ps Routing zu brechen. Es ist lediglich ein Problem des kontextuellen Identitätsmanagements.

-  Es ist unmöglich, das Shared-Identity-Problem zu verwenden, um einen I2P-Nutzer zu geolokalisieren.
-  Es ist unmöglich, das Shared-Identity-Problem zu verwenden, um I2P-Sitzungen zu verknüpfen, wenn sie nicht zeitgleich sind.

Es ist jedoch möglich, es in Situationen einzusetzen, in denen die Anonymität eines I2P-Nutzers beeinträchtigt wird, die vermutlich sehr häufig vorkommen. Ein Grund dafür ist, dass wir die Verwendung von Firefox fördern, einem Webbrowser, der „Tabbed“-Operation unterstützt.

-  Es ist *immer* möglich, einen Fingerprint aus dem Shared-Identity-Problem in *jedem* Webbrowser zu erzeugen, der das Abrufen von Ressourcen von Dritten unterstützt.
-  Das Deaktivieren von Javascript bewirkt **nichts** gegen das Shared-Identity-Problem.
-  Wenn eine Verbindung zwischen nicht-zeitgleichen Sitzungen hergestellt werden kann, beispielsweise durch „herkömmliches“ Browser-Fingerprinting, kann die Shared Identity transitiv angewendet werden, was möglicherweise eine nicht-zeitgleiche Verknüpfungsstrategie ermöglicht.
-  Wenn eine Verbindung zwischen einer Clearnet-Aktivität und einer I2P-Identität hergestellt werden kann, beispielsweise wenn das Ziel auf beiden Seiten – über I2P und Clearnet – auf einer Seite angemeldet ist, kann die Shared Identity transitiv angewendet werden, was möglicherweise eine vollständige De-Anonymisierung ermöglicht.

Wie Sie die Schwere des Shared-Identity-Problems im Zusammenhang mit dem I2P-HTTP-Proxy einschätzen, hängt davon ab, wo Sie (oder genauer gesagt, ein „Nutzer“ mit möglicherweise uninformierten Erwartungen) die „kontextuelle Identität“ für die Anwendung sehen. Es gibt mehrere Möglichkeiten:

1. HTTP ist sowohl die Anwendung als auch die kontextuelle Identität – so funktioniert es derzeit. Alle HTTP-Anwendungen teilen sich eine Identität.
2. Der Prozess ist die Anwendung und die kontextuelle Identität – so funktioniert es, wenn eine Anwendung eine API wie SAMv3 oder I2CP verwendet, wobei die Anwendung ihre Identität erstellt und deren Lebensdauer steuert.
3. HTTP ist die Anwendung, aber der Host ist die kontextuelle Identität – Dies ist der Gegenstand dieses Vorschlags, der jeden Host als potenzielle „Webanwendung“ behandelt und die Angriffsfläche entsprechend betrachtet.

Ist es lösbar?
^^^^^^^^^^^^^^^

Es ist wahrscheinlich nicht möglich, einen Proxy zu erstellen, der intelligent auf jeden möglichen Fall reagiert, in dem sein Betrieb die Anonymität einer Anwendung beeinträchtigen könnte. Es ist jedoch möglich, einen Proxy zu bauen, der intelligent auf eine spezifische Anwendung reagiert, die sich vorhersehbar verhält. Beispielsweise wird in modernen Webbrowsern erwartet, dass Nutzer mehrere Tabs geöffnet haben, in denen sie mit mehreren Websites interagieren, die durch ihren Hostnamen unterschieden werden.

Dies ermöglicht es uns, das Verhalten des HTTP-Proxys für diesen Typ von HTTP-User-Agent zu verbessern, indem wir das Verhalten des Proxys an das des User-Agents anpassen, indem wir jedem Host eine eigene Destination geben, wenn er mit dem HTTP-Proxy verwendet wird. Diese Änderung macht es unmöglich, das Shared-Identity-Problem zu nutzen, um einen Fingerprint zu erstellen, der verwendet werden kann, um Client-Aktivitäten mit zwei Hosts zu korrelieren, da die beiden Hosts einfach keine Rückgabe-Identität mehr teilen.

Beschreibung:
^^^^^^^^^^^^

Ein neuer HTTP-Proxy wird erstellt und dem Hidden Services Manager (I2PTunnel) hinzugefügt. Der neue HTTP-Proxy wird als „Multiplexer“ von I2PSocketManagern fungieren. Der Multiplexer selbst hat keine Destination. Jeder einzelne I2PSocketManager, der Teil des Multiplexers wird, hat seine eigene lokale Destination und seinen eigenen Tunnel-Pool. I2PSocketManager werden bei Bedarf vom Multiplexer erstellt, wobei der „Bedarf“ der erste Besuch einer neuen Host ist. Es ist möglich, die Erstellung der I2PSocketManager zu optimieren, bevor sie in den Multiplexer eingefügt werden, indem man einen oder mehrere im Voraus erstellt und außerhalb des Multiplexers speichert. Dies könnte die Leistung verbessern.

Ein zusätzlicher I2PSocketManager mit eigener Destination wird als Träger eines „Outproxys“ für jede Seite eingerichtet, die *keine* I2P-Destination hat, beispielsweise jede Clearnet-Seite. Dadurch wird die gesamte Outproxy-Nutzung zu einer einzigen kontextuellen Identität, mit der Einschränkung, dass die Konfiguration mehrerer Outproxys für den Tunnel die normale „Sticky“-Outproxy-Rotation verursacht, bei der jeder Outproxy nur Anfragen für eine einzelne Seite erhält. Dies ist *fast* das gleiche Verhalten wie die Isolierung von HTTP-over-I2P-Proxys nach Destination im klaren Internet.

Ressourcenüberlegungen:
''''''''''''''''''''''''

Der neue HTTP-Proxy benötigt im Vergleich zum bestehenden HTTP-Proxy zusätzliche Ressourcen. Er wird:

-  Potenziell mehr Tunnel und I2PSocketManager erstellen
-  Tunnel häufiger erstellen

Jedes dieser Elemente erfordert:

-  Lokale Rechenressourcen
-  Netzwerkressourcen von Peers

Einstellungen:
''''''''''''''

Um die Auswirkungen des erhöhten Ressourcenverbrauchs zu minimieren, sollte der Proxy so konfiguriert werden, dass er so wenig wie möglich verwendet. Proxys, die Teil des Multiplexers sind (nicht der übergeordnete Proxy), sollten so konfiguriert sein, dass:

-  Multiplexierte I2PSocketManager 1 Tunnel ein- und 1 Tunnel ausgehend in ihren Tunnel-Pools bauen
-  Multiplexierte I2PSocketManager standardmäßig 3 Hops verwenden
-  Sockets nach 10 Minuten Inaktivität geschlossen werden
-  I2PSocketManager, die vom Multiplexer gestartet werden, die Lebensdauer des Multiplexers teilen. Multiplexierte Tunnel werden nicht „zerstört“, bis der übergeordnete Multiplexer es wird.

Diagramme:
^^^^^^^^^

Das untenstehende Diagramm stellt den aktuellen Betrieb des HTTP-Proxys dar, was „Möglichkeit 1“ im Abschnitt „Ist es ein Problem?“ entspricht. Wie Sie sehen können, interagiert der HTTP-Proxy direkt mit I2P-Seiten, indem er nur eine Destination verwendet. In diesem Szenario ist HTTP sowohl die Anwendung als auch die kontextuelle Identität.

```text
**Aktuelle Situation: HTTP ist die Anwendung, HTTP ist die kontextuelle Identität**
                                                      __-> Outproxy <-> i2pgit.org
                                                     /
Browser <-> HTTP Proxy(eine Destination)<->I2PSocketManager <---> idk.i2p
                                                     \__-> translate.idk.i2p
                                                      \__-> git.idk.i2p
```

Das untenstehende Diagramm stellt den Betrieb eines host-bewussten HTTP-Proxys dar, was „Möglichkeit 3“ im Abschnitt „Ist es ein Problem?“ entspricht. In diesem Szenario ist HTTP die Anwendung, aber der Host definiert die kontextuelle Identität, wobei jede I2P-Seite mit einem anderen HTTP-Proxy interagiert, der eine eindeutige Destination pro Host hat. Dies verhindert, dass Betreiber mehrerer Seiten erkennen können, wenn dieselbe Person mehrere von ihnen betriebene Seiten besucht.

```text
**Nach der Änderung: HTTP ist die Anwendung, Host ist die kontextuelle Identität**
                                                    __-> I2PSocketManager(Destination A - Nur Outproxies) <--> i2pgit.org
                                                   /
Browser <-> HTTP Proxy Multiplexer(Keine Destination) <---> I2PSocketManager(Destination B) <--> idk.i2p
                                                   \__-> I2PSocketManager(Destination C) <--> translate.idk.i2p
                                                    \__-> I2PSocketManager(Destination C) <--> git.idk.i2p
```

Status:
^^^^^^^

Eine funktionierende Java-Implementierung des host-bewussten Proxys, die einer älteren Version dieses Vorschlags entspricht, ist in der Fork von idk unter dem Branch: i2p.i2p.2.6.0-browser-proxy-post-keepalive verfügbar (Link in den Zitaten). Sie wird derzeit stark überarbeitet, um die Änderungen in kleinere Abschnitte zu zerlegen.

Implementierungen mit unterschiedlichen Fähigkeiten wurden in Go unter Verwendung der SAMv3-Bibliothek geschrieben. Sie könnten nützlich sein, um sie in andere Go-Anwendungen einzubetten oder für go-i2p, sind aber für Java I2P ungeeignet. Außerdem fehlt ihnen eine gute Unterstützung für die interaktive Arbeit mit verschlüsselten LeaseSets.

Anhang: ``i2psocks``
                      

Ein einfacher, anwendungsorientierter Ansatz zur Isolierung anderer Clienttypen ist möglich, ohne einen neuen Tunneltyp einzuführen oder den bestehenden I2P-Code zu ändern, indem man I2PTunnel-Tools kombiniert, die bereits weit verbreitet und in der Datenschutzgemeinschaft getestet sind. Dieser Ansatz macht jedoch eine schwierige Annahme, die für HTTP nicht zutrifft und auch für viele andere potenzielle I2P-Clients nicht zutrifft.

Ungefähr das folgende Skript erzeugt einen anwendungsbezogenen SOCKS5-Proxy und socksifiziert den zugrundeliegenden Befehl:

```sh
#! /bin/sh
command_to_proxy="$@"
java -jar ~/i2p/lib/i2ptunnel.jar -wait -e 'sockstunnel 7695'
torsocks --port 7695 $command_to_proxy
```

Anhang: ``Beispiel-Implementierung des Angriffs``
                                                  

[Ein Beispiel für die Implementierung des Shared-Identity-Angriffs auf HTTP-User-Agents](https://github.com/eyedeekay/colluding_sites_attack/) existiert seit mehreren Jahren. Ein weiteres Beispiel ist im ``simple-colluder``-Unterverzeichnis des [idks prop166-Repositorys](https://git.idk.i2p/idk/i2p.host-aware-proxy) verfügbar. Diese Beispiele sind bewusst so gestaltet, dass sie demonstrieren, dass der Angriff funktioniert, und müssten (zwar nur geringfügig) modifiziert werden, um zu einem echten Angriff zu werden.
