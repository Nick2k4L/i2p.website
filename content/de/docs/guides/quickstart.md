---
title: "Erste Schritte mit I2P: Eine komplette Anleitung für Anfänger"
description: "Erste Schritte mit I2P: Eine komplette Anleitung für Anfänger"
slug: "gettingstarted"
lastUpdated: "2026-03"
accurateFor: "2.11.0"
---

**I2P ist ein vollständig verschlüsseltes, peer-to-peer basiertes anonymes Netzwerk, das „innerhalb“ des Internets läuft**, und die Java-Implementierung von geti2p.net bleibt die führende Methode, um es zu nutzen. Im Gegensatz zu Tor, das hauptsächlich den Zugriff auf das reguläre Web anonymisiert, schafft I2P ein vollständig eigenständiges Netzwerk aus versteckten Diensten, Websites, E-Mail, Chat und Dateifreigabe.

---

## Was passiert in dem Moment, in dem du I2P startest

Nach der Installation startet I2P eine lokale Webanwendung namens **Router-Konsole** unter `http://127.0.0.1:7657`. Dies ist Ihr Kontrollzentrum, das vollständig auf Ihrem Gerät läuft und aus Sicherheitsgründen an localhost gebunden ist. Beim ersten Start führt ein **Einrichtungsassistent** Sie durch die Sprachauswahl, die Wahl des Farbthemas (dunkel oder hell) und einen automatisierten Bandbreitentest, der etwa eine Minute dauert und den externen Messdienst M-Lab verwendet. Anschließend legen Sie fest, wie viel Prozent Ihrer Bandbreite Sie mit dem Netzwerk teilen möchten.

![I2P-Einrichtungsassistent - Sprachauswahl](/images/guides/quickstart/wizard-language-selection.webp)

Sobald der Assistent abgeschlossen ist, beginnt der Router mit dem **Bootstrapping**, einem Prozess, der als „Neuseedierung“ („reseeding“) bezeichnet wird. Dein Router lädt über HTTPS etwa **100 RouterInfo-Datensätze** von hartkodierten Reseed-Servern herunter, wodurch er eine erste Liste von Peers erhält. Danach beginnt er damit, **explorative Tunnel** aufzubauen, um weitere Peers zu entdecken und seine lokale Kopie der Netzwerkdatenbank (die „netDb“) zu füllen. Während der ersten Minuten wird die Meldung „Tunnel werden abgelehnt: Startvorgang“ angezeigt. Dies ist normal.

![I2P-Neustart - Bootstrapping](/images/guides/quickstart/reseed-bootstrapping.webp)

**Rechnen Sie mit einer Wartezeit von 3–10 Minuten**, bis Ihr Router nutzbar wird, und deutlich länger – mehrere Tage durchgängiger Betrieb –, bis er die maximale Leistung erreicht. In der Seitenleiste der Router-Konsole wird Ihre Anzahl an Peers als „Aktiv x/y“ angezeigt, wobei x die Anzahl der Peers ist, mit denen Sie kürzlich Nachrichten ausgetauscht haben, und y die Gesamtanzahl der gesehenen Peers. Sobald Sie **10 oder mehr aktive Peers** sehen, ist Ihr Router gesund verbunden. Das Wichtigste, was ein neuer Nutzer tun kann, ist, den **Router kontinuierlich laufen zu lassen**. Nach einem Herunterfahren markieren andere Knoten Ihren Router mindestens 24 Stunden lang als unzuverlässig, weshalb häufige Neustarts die Leistung stark beeinträchtigen.

![I2P-Router-Konsole Dashboard](/images/guides/quickstart/router-console-dashboard.png)

---

## Konfigurieren Ihres Browsers für I2P

Im Gegensatz zum Tor-Netzwerk bietet I2P keinen dedizierten Browser. Um auf I2P-Seiten (die Pseudo-Top-Level-Domain `.i2p`) zuzugreifen, müssen Sie die Proxy-Einstellungen Ihres Browsers so konfigurieren, dass der Datenverkehr über den I2P-HTTP-Proxy auf Port **4444** geleitet wird.

**Der einfachste Weg für Windows-Nutzer** ist das **Easy Install Bundle**, das Java, den Router und ein vorab konfiguriertes Firefox-Profil mit der Erweiterung „I2P in Private Browsing“ enthält. Es eliminiert jegliche manuelle Proxy-Konfiguration. Vom Download bis zum Surfen auf I2P-Seiten dauert es etwa vier Minuten. Ein Easy Install Bundle für macOS (Apple Silicon) ist ebenfalls in der Beta-Phase verfügbar. Wenn Sie das Easy Install Bundle verwenden, können Sie die manuelle Einrichtung unten überspringen.

### Firefox (empfohlen)

Firefox wird dringend empfohlen, da er über eigene Proxy-Einstellungen verfügt, die unabhängig vom Betriebssystem sind – Chrome und Edge nutzen systemweite Proxy-Einstellungen, die alle Anwendungen betreffen.

**Schritt 1.** Öffnen Sie das Firefox-Menü (Hamburger-Symbol) und klicken Sie auf **Einstellungen**.

![Firefox – Einstellungen öffnen](/images/guides/browser-config/accessi2p_3.png)

**Schritt 2.** Suchen Sie nach **proxy** in der Suchleiste der Einstellungen und klicken Sie dann neben den Netzwerkeinstellungen auf **Einstellungen...**.

![Firefox - Suche nach Proxy](/images/guides/browser-config/accessi2p_4.png)

**Schritt 3.** Wählen Sie **Manuelle Proxy-Konfiguration**, geben Sie `127.0.0.1` als HTTP-Proxy und `4444` als Port ein, dann klicken Sie auf **OK**.

![Firefox - Manuelle Proxy-Konfiguration](/images/guides/browser-config/accessi2p_5.png)

Nach der Proxy-Einrichtung werden mehrere Anpassungen in `about:config` empfohlen:

- Setze `media.peerConnection.ice.proxy_only` auf **true** (verhindert WebRTC-Leaks)
- Setze `keyword.enabled` auf **false** (stoppt Suchmaschinen-Weiterleitungen bei .i2p-Adressen)
- Erstelle einen booleschen Wert `browser.fixup.domainsuffixwhitelist.i2p` und setze ihn auf **true** (teilt Firefox mit, dass `.i2p` ein gültiges Domain-Suffix ist)

Ein anhaltendes Problem für Anfänger: Geben Sie immer `http://` vor `.i2p`-Adressen ein. Die meisten I2P-Seiten verwenden kein HTTPS (I2P verschlüsselt bereits den gesamten Datenverkehr Ende-zu-Ende), und ohne das Präfix leitet Firefox Sie an eine Suchmaschine weiter.

### Chrome / Edge (Windows)

Hinweis: Chrome und Edge verwenden die Proxy-Einstellungen Ihres Betriebssystems, was **alle** Anwendungen auf Ihrem System betrifft.

**Schritt 1.** Öffnen Sie das Chrome-Menü und klicken Sie auf **Einstellungen**.

![Chrome - Einstellungen öffnen](/images/guides/browser-config/accessi2p_6.png)

**Schritt 2.** Suchen Sie nach **Proxy**, dann klicken Sie auf **Proxy-Einstellungen Ihres Computers öffnen**.

![Chrome - Suche nach Proxy](/images/guides/browser-config/accessi2p_7.png)

**Schritt 3.** Klicken Sie unter **Manuelle Proxy-Einrichtung** neben „Ein Proxy-Server verwenden“ auf **Einrichten**.

![Windows – Proxy-Einstellungen](/images/guides/browser-config/accessi2p_8.png)

**Schritt 4.** Schalten Sie **Verwenden Sie einen Proxy-Server** auf Ein, geben Sie `127.0.0.1` als Proxy-IP-Adresse und `4444` als Port ein, dann klicken Sie auf **Speichern**.

![Windows – Proxy-Server bearbeiten](/images/guides/browser-config/accessi2p_9.png)

### Safari (macOS)

**Schritt 1.** Navigieren Sie zu **Safari → Einstellungen → Erweitert** und klicken Sie neben Proxys auf **Einstellungen ändern...**.

![Safari – Erweiterte Einstellungen](/images/guides/browser-config/accessi2p_1.png)

**Schritt 2.** Aktivieren Sie **Webproxy (HTTP)**, geben Sie `127.0.0.1` als Server und `4444` als Port ein, dann klicken Sie auf **OK**.

![macOS - Web-Proxy-Einstellungen](/images/guides/browser-config/accessi2p_2.png)

---

## Verständnis des Router-Konsole-Dashboards

Die Router-Konsole unter `127.0.0.1:7657` zeigt mehrere wichtige Indikatoren an, die Aufschluss darüber geben, wie gut Ihr Knoten funktioniert. Die **Seitenleiste** zeigt Ihre I2P-Version, die Betriebszeit, die Bandbreitennutzung (Ein-/Ausgang), die Anzahl aktiver Peers sowie den Tunnelstatus an. Wenn „Shared Clients“ grün wird, ist Ihr Router integriert und einsatzbereit.

![Routerkonsole - Gemeinsam genutzte Clients Grün](/images/guides/quickstart/shared-clients-green.png)

**Bandbreitendiagramme** zeigen den Echtzeit-Durchsatz an. Die Standardeinstellungen sind konservativ – **96 KBps down und 40 KBps up**, wobei nur 48 KBps geteilt werden – und die offizielle Dokumentation empfiehlt nachdrücklich, diese Werte zu erhöhen. Rufen Sie `http://127.0.0.1:7657/config` auf (oder klicken Sie in der Konsole auf „Configure Bandwidth“), um Ihre Grenzwerte anzuheben. Höhere geteilte Bandbreite verbessert sowohl Ihre eigene Leistung als auch die Gesundheit des Netzwerks. Wenn die geteilte Bandbreite unter **12 KBps** liegt, wechselt Ihr Router praktisch in den „versteckten Modus“ und nimmt keinen Anteil am Netzwerkverkehr mehr. Ab **128 KBps oder mehr** kann Ihr Router zum Floodfill-Status befördert werden, wodurch er bei der Pflege der verteilten Hash-Tabelle (DHT) hilft.

![Bandbreiten-Konfiguration](/images/guides/quickstart/bandwidth-config.png)

Der Abschnitt **Tunnel-Status** zeigt die beteiligten Tunnel an – Datenverkehr, den Sie für andere weiterleiten. Über 90 % der I2P-Router leiten standardmäßig Teilnahmetraffic weiter. Dies dient gleichzeitig als Tarnverkehr für Ihre eigene Anonymität und ist Ihr Beitrag zum Netzwerk. Tunnel laufen alle 10 Minuten ab und werden automatisch neu aufgebaut.

![I2PTunnel Manager](/images/guides/quickstart/tunnel-manager.png)

Der **I2PTunnel-Manager** unter `http://127.0.0.1:7657/i2ptunnel/` zeigt alle konfigurierten Tunnel an – der HTTP-Proxy, IRC, E-Mail und der Eepsite-Server-Tunnel sind alle werkseitig vorab konfiguriert.

![I2PTunnel Liste](/images/guides/quickstart/i2ptunnel-list.png)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Console page</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">URL</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Home / Status</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/home</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Dashboard with peers, bandwidth, tunnels</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Bandwidth config</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/config</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Adjust speed limits and share percentage</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Network config</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/confignet</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Firewall, port, and reachability settings</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Tunnel manager</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/i2ptunnel/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Manage all I2P tunnels and hidden services</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">I2PSnark</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/i2psnark/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Built-in BitTorrent client</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">SusiMail</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/susimail/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Built-in email client</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Address book</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/dns</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Manage .i2p hostname mappings</td>
</tr>
</tbody>
</table>
---

## Fünf Dinge, die Sie nach der Verbindung durchführen können

### .i2p-Websites durchsuchen

Die unmittelbarste Verwendung von I2P ist das Surfen auf versteckten Websites. Wenn Ihr Browser über Port 4444 weitergeleitet wird, rufen Sie eine beliebige `.i2p`-Adresse auf. Mehrere bekannte Seiten eignen sich als guter Ausgangspunkt: **`i2p-projekt.i2p`** ist die offizielle I2P-Projektseite, die innerhalb des Netzwerks gespiegelt wird, **`i2pforum.i2p`** beherbergt das Community-Supportforum, **`stats.i2p`** stellt Netzwerkstatistiken und einen Adressregistrierungsdienst bereit, und **`notbob.i2p`** verfolgt die Betriebszeit bekannter Eepsites, sodass Sie sehen können, was tatsächlich online ist. Wenn Sie auf eine unbekannte `.i2p`-Adresse stoßen, bietet der Proxy „Jump-Service“-Links an, die den Hostnamen auflösen – klicken Sie darauf, um neue Seiten Ihrem lokalen Adressbuch hinzuzufügen.

I2P enthält auch einen voreingestellten **Outproxy** (`exit.stormycloud.i2p`), der es Ihnen ermöglicht, über I2P das reguläre Internet zu erreichen. Dies ist jedoch nicht der Hauptzweck des Netzwerks, und die Leistung wird langsam sein. I2P ist als internes Darknet konzipiert, nicht als Ausstiegsknoten-Netzwerk wie Tor.

### Teilen Sie Torrent-Dateien anonym über I2PSnark

**I2PSnark** ist ein voll funktionsfähiger BitTorrent-Client, der in jeder I2P-Installation integriert ist und unter `http://127.0.0.1:7657/i2psnark/` zugänglich ist. Er arbeitet vollständig innerhalb des I2P-Netzwerks – er kann keine Verbindung zu Clearnet-Torrents herstellen, und Clearnet-Nutzer können I2P-Torrents nicht sehen. Die Weboberfläche unterstützt Magnet-Links, DHT, Drag-and-Drop, Torrent-Suche, sequenzielle Downloads und UDP-Tracker (hinzugefügt in Version 2.10.0). Die Standard-Tunnel-Länge beträgt drei Stationen. Fügen Sie einfach `.torrent`-Dateien oder Magnet-Links über die Oberfläche hinzu.

![I2PSnark-Benutzeroberfläche](/images/guides/quickstart/i2psnark-interface.png)

Um Torrents zu finden, besuchen Sie den **Postman Tracker** unter `http://tracker2.postman.i2p/` – eine zentrale Plattform, auf der Nutzer nach Torrents suchen und diese herunterladen können, die von anderen innerhalb des I2P-Netzwerks hochgeladen wurden. Sie können auch eigene Torrents hochladen, um sie mit der Community zu teilen.

![Postman Tracker](/images/guides/quickstart/postman-tracker.png)

Weitere I2P-kompatible Torrent-Clients sind BiglyBT und qBittorrent mit einem I2P-Plugin.

### Verschlüsselte E-Mails mit SusiMail senden

**SusiMail** unter `http://127.0.0.1:7657/susimail/` ist ein webbasierter E-Mail-Client, der entwickelt wurde, um keine identifizierbaren Informationen preiszugeben. Er verbindet sich mit dem **`mail.i2p`**-Mailserver, der von „postman“ betrieben wird. Um loszulegen, registrieren Sie einen Account unter **`hq.postman.i2p`** (erreichbar über Ihren I2P-Proxy) und melden Sie sich danach mit diesen Anmeldedaten in SusiMail an. Vorab konfigurierte I2PTunnel-Einträge leiten SMTP über `localhost:7659` und POP3 über `localhost:7660` weiter. Sie können E-Mails sowohl an andere `@mail.i2p`-Nutzer als auch an reguläre Internet-E-Mail-Adressen senden (über den Outproxy des Mail-Servers weitergeleitet). SusiMail unterstützt Markdown-Formatierung, Drag-and-Drop-Anhänge und HTML-E-Mails.

![SusiMail Posteingang](/images/guides/quickstart/susimail-login.png)

![SusiMail verfassen](/images/guides/quickstart/susimail-inbox.png)

### Chat über IRC über das Irc2P-Netzwerk

I2P wird mit einem **vorab konfigurierten IRC-Tunnel** auf `localhost:6668` ausgeliefert. Richten Sie jeden IRC-Client auf diese Adresse (mit deaktiviertem SSL/TLS – I2P übernimmt die Verschlüsselung) und Sie verbinden sich mit dem Irc2P-Netzwerk, einer Verbundgemeinschaft von Servern, zu der auch `irc.postman.i2p`, `irc.echelon.i2p` und `irc.dg.i2p` gehören. Wichtige Kanäle sind **`#i2p`** für allgemeine Diskussionen, **`#i2p-dev`** für Entwicklungsfragen und **`#i2p-help`** für Support. Der IRC-Tunnel entfernt automatisch identifizierende Informationen aus Ihrer Verbindung. Empfohlene Clients sind WeeChat, Pidgin und Thunderbird Chat.

### Hosten Sie Ihre eigene anonyme Website

Jede I2P-Installation beinhaltet bereits einen laufenden **Jetty-Webserver** auf `localhost:7658` mit einem entsprechenden I2P-Server-Tunnel. Um eine Website zu veröffentlichen, legen Sie einfach HTML-Dateien im Dokument-Stammverzeichnis ab: `~/.i2p/eepsite/docroot` unter Linux oder `%LOCALAPPDATA%\I2P\I2P Site\docroot` unter Windows. Ihre Website erhält automatisch ein kryptographisches Base64-Ziel sowie eine kürzere Adresse der Form `xxxxx.b32.i2p`. Um einen menschenlesbaren Namen wie `mysite.i2p` zu erhalten, registrieren Sie diesen bei Adressbuchdiensten wie `stats.i2p` oder `no.i2p`. Für anspruchsvollere Konfigurationen können Sie Jetty durch Apache oder Nginx hinter dem I2PTunnel-Server-Tunnel ersetzen – achten Sie dabei jedoch darauf, identifizierende Server-Header zu entfernen. Eine ausführliche Anleitung finden Sie in unserem Leitfaden [Erstellen einer I2P-Eepsite](/docs/guides/creating-an-eepsite/).

---

## Wichtige Sicherheitspraktiken für neue Benutzer

**Browsen Sie niemals I2P und das Clearnet im selben Browserprofil.** Dies ist die wichtigste Sicherheitsregel. Erstellen Sie ein dediziertes Firefox-Profil über `about:profiles` oder verwenden Sie das vorkonfigurierte Profil aus dem Easy Install Bundle. Eine Vermischung von Cookies, Verlauf und zwischengespeicherten Daten zwischen anonymem und identifiziertem Surfen ist der häufigste Fehler in der operativen Sicherheit.

Die offizielle **"I2P in Private Browsing"**-Firefox-Erweiterung (erhältlich im Add-on-Speicher von Mozilla) automatisiert vieles davon, indem isolierte Container-Tabs mit aktivierter Anti-Fingerprinting-Funktion, Erstparteien-Isolation und Letterboxing erstellt werden. Für Chromium-Nutzer: mit separaten Flags starten: `--user-data-dir=$HOME/.config/chromium-i2p --proxy-server="http://127.0.0.1:4444"`.

---
