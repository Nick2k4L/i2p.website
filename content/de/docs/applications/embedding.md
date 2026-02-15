---
title: "I2P in Ihre Anwendung einbetten"
description: "Richtlinien für die Bündelung eines I2P routers mit Ihrer Anwendung"
slug: "embedding"
lastUpdated: "2023-01"
accurateFor: "2.1.0"
---

## Überblick

Diese Seite behandelt die Bündelung der gesamten I2P router-Binärdatei mit Ihrer Anwendung. Es geht nicht darum, eine Anwendung zu schreiben, die mit I2P funktioniert (weder gebündelt noch extern). Viele der Richtlinien können jedoch auch dann nützlich sein, wenn Sie keinen router bündeln.

Viele Projekte bündeln I2P oder sprechen darüber, I2P zu bündeln. Das ist großartig, wenn es richtig gemacht wird. Wenn es falsch gemacht wird, könnte es unserem Netzwerk echten Schaden zufügen. Der I2P router ist komplex, und es kann eine Herausforderung sein, die gesamte Komplexität vor Ihren Benutzern zu verbergen. Diese Seite behandelt einige allgemeine Richtlinien.

Die meisten dieser Richtlinien gelten gleichermaßen für Java I2P oder i2pd. Jedoch sind einige Richtlinien spezifisch für Java I2P und werden im Folgenden erwähnt.

### Sprechen Sie mit uns

Beginnen Sie einen Dialog. Wir sind hier, um zu helfen. Anwendungen, die I2P einbetten, sind die vielversprechendsten - und aufregendsten - Möglichkeiten für uns, das Netzwerk zu erweitern und die Anonymität für alle zu verbessern.

### Wählen Sie Ihren router mit Bedacht

Wenn Ihre Anwendung in Java oder Scala geschrieben ist, ist die Wahl einfach - verwenden Sie den Java router. Bei C/C++ empfehlen wir i2pd. Die Entwicklung von i2pcpp wurde eingestellt. Für Anwendungen in anderen Sprachen ist es am besten, SAM oder BOB oder SOCKS zu verwenden und den Java router als separaten Prozess zu bündeln. Einige der folgenden Punkte gelten nur für den Java router.

### Lizenzierung

Stellen Sie sicher, dass Sie die Lizenzanforderungen der Software erfüllen, die Sie bündeln.

---

## Konfiguration

### Standardkonfiguration überprüfen

Eine korrekte Standardkonfiguration ist entscheidend. Die meisten Benutzer werden die Standardeinstellungen nicht ändern. Die Standardwerte für Ihre Anwendung müssen möglicherweise von den Standardwerten für den router, den Sie bündeln, abweichen. Überschreiben Sie die router-Standardwerte bei Bedarf.

Einige wichtige Standardwerte zu überprüfen: Maximale Bandbreite, tunnel-Anzahl und -Länge, maximale teilnehmende tunnels. Vieles davon hängt von der erwarteten Bandbreite und den Nutzungsmustern Ihrer Anwendung ab.

Konfigurieren Sie ausreichend Bandbreite und Tunnel, um Ihren Benutzern zu ermöglichen, zum Netzwerk beizutragen. Erwägen Sie, externes I2CP zu deaktivieren, da Sie es wahrscheinlich nicht benötigen und es mit jeder anderen laufenden I2P-Instanz in Konflikt stehen würde. Schauen Sie sich auch die Konfigurationen an, um beispielsweise das Beenden der JVM beim Exit zu deaktivieren.

### Überlegungen zum teilnehmenden Datenverkehr

Es mag verlockend sein, den teilnehmenden Datenverkehr zu deaktivieren. Es gibt mehrere Möglichkeiten, dies zu tun (versteckter Modus, maximale tunnel auf 0 setzen, geteilte Bandbreite unter 12 KBytes/s setzen). Ohne teilnehmenden Datenverkehr müssen Sie sich keine Gedanken über ein ordnungsgemäßes Herunterfahren machen, Ihre Benutzer sehen keine Bandbreitennutzung, die nicht von ihnen generiert wurde, usw. Es gibt jedoch viele Gründe, warum Sie teilnehmende tunnel zulassen sollten.

Zunächst einmal funktioniert der router nicht besonders gut, wenn er keine Chance hat, sich in das Netzwerk zu "integrieren", was enorm dadurch unterstützt wird, dass andere tunnel durch Sie aufbauen.

Zweitens erlauben über 90% der router im aktuellen Netzwerk die Teilnahme am Datenverkehr. Das ist die Standardeinstellung im Java router. Wenn Ihre Anwendung nicht für andere weiterleitet und sehr beliebt wird, dann ist sie ein Schmarotzer im Netzwerk und stört das Gleichgewicht, das wir jetzt haben. Wenn sie wirklich groß wird, dann werden wir zu Tor und verbringen unsere Zeit damit, die Leute anzuflehen, das Weiterleiten zu aktivieren.

Drittens ist der teilnehmende Verkehr Tarndatenverkehr, der die Anonymität Ihrer Benutzer unterstützt.

Wir raten Ihnen dringend davon ab, den teilnehmenden Traffic standardmäßig zu deaktivieren. Wenn Sie dies tun und Ihre Anwendung sehr populär wird, könnte dies das Netzwerk zum Zusammenbruch bringen.

### Persistenz

Sie müssen die Daten des routers (netDb, Konfiguration, etc.) zwischen den Ausführungen des routers speichern. I2P funktioniert nicht gut, wenn Sie bei jedem Start neu seeden müssen, und das ist eine enorme Belastung für unsere Reseed-Server und auch nicht sehr gut für die Anonymität. Selbst wenn Sie router-Informationen bündeln, benötigt I2P gespeicherte Profildaten für die beste Leistung. Ohne Persistenz werden Ihre Benutzer eine schlechte Starterfahrung haben.

Es gibt zwei Möglichkeiten, wenn Sie keine Persistierung bereitstellen können. Beide eliminieren die Last Ihres Projekts auf unseren Reseed-Servern und verbessern die Startzeit erheblich.

1) Richten Sie Ihren eigenen Projekt-Reseed-Server (oder mehrere) ein, der deutlich mehr als die übliche Anzahl von Router-Infos beim Reseed bereitstellt, beispielsweise mehrere hundert. Konfigurieren Sie den Router so, dass er nur Ihre Server verwendet.

2) Bündeln Sie ein- bis zweitausend Router-Infos in Ihrem Installer.

Verzögern oder staffeln Sie außerdem den Start Ihrer Tunnel, um dem Router die Möglichkeit zu geben, sich zu integrieren, bevor viele Tunnel aufgebaut werden.

### Konfigurierbarkeit

Geben Sie Ihren Benutzern eine Möglichkeit, die Konfiguration der wichtigen Einstellungen zu ändern. Wir verstehen, dass Sie wahrscheinlich den Großteil der Komplexität von I2P verbergen möchten, aber es ist wichtig, einige grundlegende Einstellungen anzuzeigen. Zusätzlich zu den oben genannten Standardwerten können einige Netzwerkeinstellungen wie UPnP, IP/Port hilfreich sein.

### Floodfill-Überlegungen

Oberhalb einer bestimmten Bandbreiteneinstellung und beim Erfüllen anderer Gesundheitskriterien wird Ihr router zu einem floodfill, was zu einem erheblichen Anstieg der Verbindungen und des Speicherverbrauchs führen kann (zumindest beim Java-router). Überlegen Sie, ob das in Ordnung ist. Sie können floodfill deaktivieren, aber dann tragen Ihre schnellsten Benutzer nicht so viel bei, wie sie könnten. Es hängt auch von der typischen Betriebszeit Ihrer Anwendung ab.

### Reseeding

Entscheiden Sie, ob Sie router infos bündeln oder unsere reseed hosts verwenden. Die Java reseed host Liste befindet sich im Quellcode, wenn Sie also Ihren Quellcode aktuell halten, wird auch die Host-Liste aktuell sein. Seien Sie sich möglicher Blockierungen durch feindliche Regierungen bewusst.

### Geteilte Clients verwenden

Java I2P i2ptunnel unterstützt geteilte Clients, bei denen Clients so konfiguriert werden können, dass sie einen einzigen Pool verwenden. Wenn Sie mehrere Clients benötigen und dies mit Ihren Sicherheitszielen vereinbar ist, konfigurieren Sie die Clients als geteilt.

### Tunnel-Anzahl begrenzen

Geben Sie die tunnel-Anzahl explizit mit den Optionen `inbound.quantity` und `outbound.quantity` an. Der Standard in Java I2P ist 2; der Standard in i2pd ist höher. Geben Sie es in der SESSION CREATE-Zeile mit SAM an, um konsistente Einstellungen bei beiden routern zu erhalten. Zwei jeweils ein-/ausgehend ist ausreichend für die meisten Anwendungen mit geringer bis mittlerer Bandbreite und geringem bis mittlerem Fanout. Server und P2P-Anwendungen mit hohem Fanout benötigen möglicherweise mehr. Siehe diesen Forumsbeitrag für Anleitungen zur Berechnung der Anforderungen für Server und Anwendungen mit hohem Datenverkehr.

### SAM SIGNATURE_TYPE angeben

SAM verwendet standardmäßig DSA_SHA1 für Ziele, was nicht das ist, was Sie wollen. Ed25519 (Typ 7) ist die richtige Wahl. Fügen Sie SIGNATURE_TYPE=7 zum DEST GENERATE-Befehl hinzu, oder zum SESSION CREATE-Befehl für DESTINATION=TRANSIENT.

### SAM-Sitzungen begrenzen

Die meisten Anwendungen benötigen nur eine SAM-Session. SAM bietet die Möglichkeit, den lokalen Router oder sogar das breitere Netzwerk schnell zu überlasten, wenn eine große Anzahl von Sessions erstellt wird. Wenn mehrere Unterdienste eine einzige Session verwenden können, richten Sie diese mit einer PRIMARY-Session und SUBSESSIONS ein (derzeit nicht von i2pd unterstützt). Eine angemessene Begrenzung für Sessions liegt bei 3 oder 4 insgesamt, oder vielleicht bis zu 10 für seltene Situationen. Wenn Sie mehrere Sessions haben, stellen Sie sicher, dass Sie für jede eine niedrige Tunnel-Anzahl angeben, siehe oben.

In fast keiner Situation sollten Sie eine eindeutige Session pro Verbindung benötigen. Ohne sorgfältige Planung könnte dies schnell zu einem DDoS-Angriff auf das Netzwerk führen. Überlegen Sie sorgfältig, ob Ihre Sicherheitsziele eindeutige Sessions erfordern. Bitte konsultieren Sie die Java I2P oder i2pd Entwickler, bevor Sie Sessions pro Verbindung implementieren.

### Netzwerkressourcenverbrauch reduzieren

Beachten Sie, dass diese Optionen derzeit nicht von i2pd unterstützt werden. Diese Optionen werden über I2CP und SAM unterstützt (außer delay-open, das nur über i2ptunnel verfügbar ist). Siehe die I2CP-Dokumentation (und für delay-open die i2ptunnel-Konfigurationsdokumentation) für Details.

Erwägen Sie, Ihre Anwendungstunnel auf delay-open, reduce-on-idle und/oder close-on-idle zu setzen. Dies ist unkompliziert, wenn Sie i2ptunnel verwenden, aber Sie müssen einiges davon selbst implementieren, wenn Sie I2CP direkt verwenden. Siehe i2psnark für Code, der die tunnel-Anzahl reduziert und dann den tunnel schließt, auch bei einiger DHT-Hintergrundaktivität.

---

## Lebenszyklus

### Aktualisierbarkeit

Implementieren Sie nach Möglichkeit eine Auto-Update-Funktion oder zumindest eine automatische Benachrichtigung über neue Versionen. Unsere größte Sorge ist eine große Anzahl von routern, die nicht aktualisiert werden können. Wir haben etwa 6-8 Releases pro Jahr des Java-routers, und es ist entscheidend für die Gesundheit des Netzwerks, dass die Benutzer auf dem neuesten Stand bleiben. Normalerweise haben wir über 80% des Netzwerks innerhalb von 6 Wochen nach dem Release auf der neuesten Version, und wir möchten das so beibehalten. Sie müssen sich keine Gedanken über die Deaktivierung der eingebauten Auto-Update-Funktion des routers machen, da sich dieser Code in der router-Konsole befindet, die Sie vermutlich nicht mit einbündeln.

### Einführung

Haben Sie einen schrittweisen Rollout-Plan. Überlasten Sie das Netzwerk nicht auf einmal. Wir haben derzeit etwa 25.000 eindeutige Nutzer pro Tag und 40.000 eindeutige Nutzer pro Monat. Wir können wahrscheinlich ein Wachstum von 2-3x pro Jahr ohne größere Probleme bewältigen. Wenn Sie einen schnelleren Hochlauf als das erwarten, ODER die Bandbreitenverteilung (oder Uptime-Verteilung oder jede andere bedeutende Eigenschaft) Ihrer Nutzerbasis sich erheblich von unserer aktuellen Nutzerbasis unterscheidet, müssen wir wirklich ein Gespräch führen. Je größer Ihre Wachstumspläne sind, desto wichtiger wird alles andere in dieser Checkliste.

### Design für und Förderung langer Betriebszeiten

Teilen Sie Ihren Benutzern mit, dass I2P am besten funktioniert, wenn es kontinuierlich läuft. Es kann mehrere Minuten nach dem Start dauern, bis es gut funktioniert, und nach der ersten Installation sogar noch länger. Wenn Ihre durchschnittliche Betriebszeit weniger als eine Stunde beträgt, ist I2P wahrscheinlich die falsche Lösung.

---

## Benutzeroberfläche

### Status anzeigen

Geben Sie dem Benutzer einen Hinweis darauf, dass die Anwendungstunnel bereit sind. Ermutigen Sie zur Geduld.

### Ordnungsgemäßes Herunterfahren

Falls möglich, verzögern Sie das Herunterfahren, bis Ihre teilnehmenden tunnel ablaufen. Lassen Sie Ihre Benutzer nicht einfach tunnel unterbrechen, oder bitten Sie sie zumindest um Bestätigung.

### Bildung und Spenden

Es wäre schön, wenn Sie Ihren Benutzern Links zur Verfügung stellen würden, um mehr über I2P zu erfahren und zu spenden.

### Externe Router-Option

Je nach Ihrer Nutzerbasis und Anwendung kann es hilfreich sein, eine Option oder ein separates Paket zur Verwendung eines externen routers anzubieten.

---

## Weitere Themen

### Nutzung anderer gemeinsamer Dienste

Wenn Sie planen, andere gängige I2P-Dienste zu nutzen oder zu verlinken (News-Feeds, hosts.txt-Abonnements, Tracker, Outproxies usw.), stellen Sie sicher, dass Sie diese nicht überlasten, und sprechen Sie mit den Personen, die sie betreiben, um sicherzustellen, dass es in Ordnung ist.

### Zeit- / NTP-Probleme

Hinweis: Dieser Abschnitt bezieht sich auf Java I2P. i2pd enthält keinen SNTP-Client.

I2P enthält einen SNTP-Client. I2P benötigt die korrekte Zeit zum Betrieb. Es wird eine falsch gehende Systemuhr kompensieren, aber dies kann den Start verzögern. Sie können I2Ps SNTP-Abfragen deaktivieren, aber dies wird nicht empfohlen, es sei denn, Ihre Anwendung stellt sicher, dass die Systemuhr korrekt ist.

### Wählen Sie, was und wie Sie bündeln

Hinweis: Dieser Abschnitt bezieht sich nur auf Java I2P.

Mindestens benötigen Sie i2p.jar, router.jar, streaming.jar und mstreaming.jar. Sie können die beiden streaming-JARs für eine reine Datagramm-Anwendung weglassen. Einige Anwendungen benötigen möglicherweise mehr, z.B. i2ptunnel.jar oder addressbook.jar. Vergessen Sie nicht jbigi.jar oder eine Teilmenge davon für die von Ihnen unterstützten Plattformen, um die Kryptographie deutlich zu beschleunigen. Java 7 oder höher ist zum Kompilieren erforderlich. Wenn Sie Debian/Ubuntu-Pakete erstellen, sollten Sie das I2P-Paket aus unserem PPA voraussetzen, anstatt es mit zu bündeln. Sie benötigen mit ziemlicher Sicherheit beispielsweise nicht susimail, susidns, die Router-Konsole und i2psnark.

Die folgenden Dateien sollten im I2P-Installationsverzeichnis enthalten sein, das mit der Eigenschaft "i2p.dir.base" angegeben wird. Vergessen Sie nicht das certificates/ Verzeichnis, welches für das Reseeding erforderlich ist, und blocklist.txt für die IP-Validierung. Das geoip Verzeichnis ist optional, aber empfohlen, damit der router Entscheidungen basierend auf dem Standort treffen kann. Wenn Sie geoip einbeziehen, stellen Sie sicher, dass Sie die Datei GeoLite2-Country.mmdb in dieses Verzeichnis legen (entpacken Sie sie aus installer/resources/GeoLite2-Country.mmdb.gz). Die hosts.txt Datei könnte notwendig sein, Sie können sie modifizieren, um alle Hosts einzuschließen, die Ihre Anwendung verwendet. Sie können eine router.config Datei zum Basisverzeichnis hinzufügen, um anfängliche Standardwerte zu überschreiben. Überprüfen und bearbeiten oder entfernen Sie die clients.config und i2ptunnel.config Dateien.

Lizenzanforderungen können erfordern, dass Sie die Datei LICENSES.txt und das Lizenzverzeichnis mit einschließen.

- Sie möchten möglicherweise auch eine hosts.txt-Datei bündeln.
- Stellen Sie sicher, dass Sie einen bootclasspath angeben, wenn Sie Java I2P für Ihre Veröffentlichung kompilieren, anstatt unsere Binärdateien zu verwenden.

### Android-Überlegungen

Hinweis: Dieser Abschnitt bezieht sich nur auf Java I2P.

Unsere Android-Router-App kann von mehreren Clients gemeinsam genutzt werden. Falls sie nicht installiert ist, wird der Benutzer dazu aufgefordert, wenn er eine Client-App startet.

Einige Entwickler haben Bedenken geäußert, dass dies eine schlechte Benutzererfahrung darstellt, und sie möchten den router in ihre App einbetten. Wir haben eine Android router Service-Bibliothek auf unserer Roadmap, die das Einbetten erleichtern könnte. Weitere Informationen erforderlich.

Falls Sie Hilfe benötigen, kontaktieren Sie uns bitte.

### Maven-JAR-Dateien

Hinweis: Dieser Abschnitt bezieht sich nur auf Java I2P.

Wir haben eine begrenzte Anzahl unserer JAR-Dateien auf [Maven Central](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22net.i2p%22). Es gibt zahlreiche Trac-Tickets, die wir bearbeiten müssen, um die veröffentlichten JAR-Dateien auf Maven Central zu verbessern und zu erweitern.

Wenn Sie Hilfe benötigen, kontaktieren Sie uns bitte.

### Datagram (DHT) Überlegungen

Wenn Ihre Anwendung I2P-Datagramme verwendet, z.B. für eine DHT, stehen viele erweiterte Optionen zur Verfügung, um den Overhead zu reduzieren und die Zuverlässigkeit zu erhöhen. Dies kann einige Zeit und Experimente erfordern, um gut zu funktionieren. Beachten Sie die Kompromisse zwischen Größe und Zuverlässigkeit. Sprechen Sie uns für Hilfe an. Es ist möglich - und empfohlen - Datagramme und Streaming auf derselben Destination zu verwenden. Erstellen Sie dafür keine separaten Destinations. Versuchen Sie nicht, Ihre unabhängigen Daten in den bestehenden Netzwerk-DHTs (iMule, bote, bittorrent und router) zu speichern. Bauen Sie Ihre eigene auf. Wenn Sie Seed-Knoten fest einprogrammieren, empfehlen wir, dass Sie mehrere haben.

### Outproxies

I2P-Outproxies zum Clearnet sind eine begrenzte Ressource. Verwenden Sie Outproxies nur für normales benutzerinitiertes Web-Browsing oder anderen begrenzten Datenverkehr. Für jede andere Nutzung konsultieren Sie den Outproxy-Betreiber und holen Sie dessen Genehmigung ein.

### Comarketing

Lasst uns zusammenarbeiten. Wartet nicht, bis es fertig ist. Gebt uns euren Twitter-Handle und beginnt darüber zu twittern, wir werden uns revanchieren.

### Malware

Bitte verwenden Sie I2P nicht für böse Zwecke. Dies könnte sowohl unserem Netzwerk als auch unserem Ruf großen Schaden zufügen.

### Mach mit

Das mag offensichtlich sein, aber treten Sie der Gemeinschaft bei. Lassen Sie I2P rund um die Uhr laufen. Erstellen Sie eine I2P-Site über Ihr Projekt. Verbringen Sie Zeit im IRC #i2p-dev. Posten Sie in den Foren. Verbreiten Sie das Wort. Wir können Ihnen helfen, Benutzer, Tester, Übersetzer oder sogar Programmierer zu finden.

---

## Beispiele

### Anwendungsbeispiele

Sie können die I2P Android-App installieren und damit experimentieren und sich den Code ansehen, um ein Beispiel für eine Anwendung zu sehen, die den Router bündelt. Schauen Sie sich an, was wir dem Benutzer zeigen und was wir verbergen. Betrachten Sie die Zustandsmaschine, die wir zum Starten und Stoppen des Routers verwenden. Weitere Beispiele sind: Vuze, die Nightweb Android-App, iMule, TAILS, iCloak und Monero.

### Code-Beispiel

Hinweis: Dieser Abschnitt bezieht sich nur auf Java I2P.

Nichts davon erklärt Ihnen tatsächlich, wie Sie Ihren Code schreiben müssen, um den Java router zu bündeln, daher folgt ein kurzes Beispiel.

```java
import java.util.Properties;
import net.i2p.router.Router;

	Properties p = new Properties();
        // add your configuration settings, directories, etc.
        // where to find the I2P installation files
	p.addProperty("i2p.dir.base", baseDir);
        // where to find the I2P data files
	p.addProperty("i2p.dir.config", configDir);
        // bandwidth limits in K bytes per second
	p.addProperty("i2np.inboundKBytesPerSecond", "50");
	p.addProperty("i2np.outboundKBytesPerSecond", "50");
	p.addProperty("router.sharePercentage", "80");
	p.addProperty("foo", "bar");
	Router r = new Router(p);
        // don't call exit() when the router stops
	r.setKillVMOnEnd(false);
	r.runRouter();

	...

	r.shutdownGracefully();
	// will shutdown in 11 minutes or less
```
Dieser Code ist für den Fall gedacht, wo Ihre Anwendung den router startet, wie in unserer Android-App. Sie könnten auch den router die Anwendung über die clients.config und i2ptunnel.config Dateien starten lassen, zusammen mit Jetty-Webapps, wie es in unseren Java-Paketen gemacht wird. Wie immer ist die Zustandsverwaltung der schwierige Teil.

Siehe auch: die Router javadocs.
