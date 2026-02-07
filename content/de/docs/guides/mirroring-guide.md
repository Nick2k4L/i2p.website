---
title: "Spiegeln Ihrer Dienste auf I2P"
description: "Ein anfängerfreundlicher Leitfaden, um Ihre Websites, Git-Repositories, APIs und mehr im I2P-Netzwerk verfügbar zu machen — mit Schritt-für-Schritt-Anleitungen und Diagrammen"
slug: "mirroring-guide"
lastUpdated: "2025-02"
accurateFor: "2.10.0"
---

Sie haben eine Website im regulären Internet. Jetzt möchten Sie sie auch über I2P verfügbar machen — damit Menschen sie privat besuchen können, ohne zu verraten, wer sie sind oder woher sie kommen. Darum geht es in diesem Leitfaden.

Mirroring ersetzt nicht Ihre bestehende Website. Es fügt einen zweiten Zugang hinzu — einen privaten — über das I2P-Netzwerk. Ihre Clearnet-Website läuft weiterhin genau wie zuvor.

![Wie I2P-Spiegelung funktioniert — Ihr Server erhält einen zweiten, privaten Zugang über das I2P-Netzwerk](/images/guides/mirroring/how-mirroring-works.svg)

## Warum auf I2P spiegeln?

Es gibt mehrere praktische Gründe, Ihre Dienste zu spiegeln:

**Privatsphäre für Ihre Besucher.** Menschen können auf Ihre Inhalte zugreifen, ohne ihre IP-Adresse preiszugeben. Der Datenverkehr zwischen ihnen and Ihrem Dienst wird über mehrere Sprungpunkte verschlüsselt – weder Sie noch jemand, der das Netzwerk überwacht, kann identifizieren, wer zu Besuch ist.

**Zensurresistenz.** Wenn Ihre Website in bestimmten Regionen durch DNS-Filterung, IP-Blockierung oder andere Mittel gesperrt ist, bleibt der I2P-Spiegel erreichbar. Er ist nicht auf DNS oder herkömmliches IP-Routing angewiesen.

**Ausfallsicherheit.** Ein I2P-Mirror fügt Redundanz hinzu. Wenn Ihre Domain beschlagnahmt wird oder Ihr CDN Sie fallen lässt, bleibt die I2P-Version online, solange Ihr Server läuft.

**Das Netzwerk unterstützen.** Jeder Dienst auf I2P macht das Netzwerk nützlicher und hilft beim Wachstum des Ökosystems.

## Was Sie benötigen

Bevor Sie beginnen, stellen Sie sicher, dass Sie haben:

- **Ein laufender I2P router** auf Ihrem Server (die Java-Implementierung). Falls Sie noch keinen haben, folgen Sie zuerst der [I2P Installationsanleitung](/downloads/).
- **Ihre Website oder Ihr Service funktioniert bereits** — sie sollte Inhalte auf Ihrem Server bereitstellen.
- **Grundlegende Befehlszeilen-Kenntnisse** — Sie werden eine Konfigurationsdatei bearbeiten und einige Befehle ausführen.
- **Etwa 15–20 Minuten** — das ist alles, was Sie brauchen.

Ihr I2P router benötigt mindestens 512 MB RAM und funktioniert am besten auf einem Server mit 24/7-Betriebszeit. Wenn Ihr router zum ersten Mal gestartet wurde, geben Sie ihm 10–15 Minuten Zeit, sich in das Netzwerk zu integrieren, bevor Sie tunnels erstellen.

## Tunnels verstehen

Das Grundkonzept hinter I2P-Spiegelung ist der **server tunnel**. Hier ist die Idee:

Wenn jemand im I2P-Netzwerk Ihre Website besuchen möchte, durchläuft seine Anfrage mehrere verschlüsselte Sprünge durch das I2P-Netzwerk, bis sie Ihren I2P-Router erreicht. Ihr Router übergibt die Anfrage dann an einen **server tunnel**, der sie an Ihren auf localhost laufenden Webserver weiterleitet. Ihr Webserver antwortet, und die Antwort nimmt den umgekehrten Weg zurück durch das verschlüsselte Netzwerk.

Ihr Webserver berührt niemals das öffentliche Internet für diese Anfragen — er kommuniziert nur mit localhost. Der I2P router übernimmt alles netzwerkseitige.

### Welchen Tunnel-Typ benötigen Sie?

I2P bietet mehrere tunnel-Typen für verschiedene Situationen:

![Tunnel-Typen Vergleich — HTTP Server ist die richtige Wahl für die meisten Websites](/images/guides/mirroring/tunnel-types.svg)

Für das Spiegeln einer Website möchten Sie fast sicher einen **HTTP Server** tunnel. Er ist speziell für Webverkehr konzipiert und behandelt Header-Filterung, Komprimierung und Hostname-Spoofing standardmäßig. Die anderen Typen existieren für spezialisierte Anwendungsfälle wie SSH-Zugriff, bidirektionale Anwendungen oder IRC-Server.

## Teil 1: Spiegeln einer Website

Dies ist das häufigste Szenario — Sie haben eine bestehende Clearnet-Website und möchten sie über I2P verfügbar machen. Hier ist der Prozess im Überblick:

![Die fünf Schritte zur Spiegelung Ihrer Website auf I2P](/images/guides/mirroring/steps-overview.svg)

Gehen wir jeden Schritt durch.

### Schritt 1: Fügen Sie einen Localhost-Listener zu Ihrem Webserver hinzu

Ihre clearnet-Website läuft wahrscheinlich bereits auf den Ports 80 und 443 und ist für die Welt zugänglich. Für I2P erstellen Sie einen *separaten* Listener auf localhost, den nur der I2P tunnel erreichen kann. Dies gibt Ihnen die volle Kontrolle darüber, wie die I2P-Version aussieht — Sie können Header entfernen, Admin-Panels blockieren und das Caching für die höhere Latenz von I2P optimieren.

> **Schnelle Alternative:** Wenn Sie keine Anpassungen benötigen, können Sie diesen Schritt überspringen und den I2P tunnel direkt auf `127.0.0.1:80` verweisen. Aber der Ansatz mit einem dedizierten Listener wird empfohlen.

Wählen Sie Ihren Webserver:

#### Nginx

Erstellen Sie eine neue Website-Konfiguration:

```bash
sudo nano /etc/nginx/sites-available/i2p-mirror
```
Fügen Sie diese Konfiguration ein und ersetzen Sie `yoursite.i2p` und den Root-Pfad durch Ihre eigenen Werte:

```nginx
server {
    # Only listen on localhost — the I2P tunnel connects here
    listen 127.0.0.1:8080;

    server_name yoursite.i2p yoursite.b32.i2p;

    # Point this to the same content as your clearnet site
    root /var/www/your-site;
    index index.html;

    # Don't reveal server software
    server_tokens off;

    # Security headers — note: NO HSTS (it breaks I2P access)
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header Referrer-Policy "same-origin" always;

    # Restrict resources to your own site only
    add_header Content-Security-Policy
        "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'"
        always;

    location / {
        try_files $uri $uri/ =404;

        # Aggressive caching reduces the impact of I2P latency
        expires 1d;
        add_header Cache-Control "public, immutable";
    }

    # Cache static assets even more aggressively
    location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Optional: block admin areas from I2P visitors
    location ~ ^/(admin|wp-admin|login) {
        return 403;
    }
}
```
Aktivieren Sie es und laden Sie neu:

```bash
sudo ln -s /etc/nginx/sites-available/i2p-mirror /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```
#### Apache

Erstelle eine neue Site-Konfiguration:

```bash
sudo nano /etc/apache2/sites-available/i2p-mirror.conf
```
Fügen Sie diese Konfiguration ein:

```apache
<VirtualHost 127.0.0.1:8080>
    ServerName yoursite.i2p
    ServerAlias yoursite.b32.i2p

    DocumentRoot /var/www/your-site

    # Hide server identification
    ServerSignature Off
    ServerTokens Prod
    TraceEnable Off

    <IfModule mod_headers.c>
        Header unset X-Powered-By
        Header unset Server
        # Never include HSTS — it breaks I2P
        Header unset Strict-Transport-Security

        Header always set X-Content-Type-Options "nosniff"
        Header always set X-Frame-Options "SAMEORIGIN"
        Header always set Referrer-Policy "same-origin"
        Header always set Content-Security-Policy "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'"

        # Aggressive caching for I2P latency
        Header set Cache-Control "public, max-age=86400, immutable"
    </IfModule>

    <Directory /var/www/your-site>
        Options -Indexes -FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>

    # Optional: block admin areas from I2P visitors
    <LocationMatch "^/(admin|wp-admin|login)">
        Require all denied
    </LocationMatch>
</VirtualHost>
```
Dann den Port hinzufügen, die Website aktivieren und neu laden:

```bash
echo "Listen 127.0.0.1:8080" | sudo tee -a /etc/apache2/ports.conf
sudo a2ensite i2p-mirror
sudo a2enmod headers
sudo a2dismod status info
sudo apachectl configtest
sudo systemctl reload apache2
```
#### Warum kein HSTS?

Sie werden bemerken, dass beide Konfigurationen explizit `Strict-Transport-Security`-Header vermeiden. Das ist entscheidend. HSTS weist Browser an, nur HTTPS zu verwenden, aber I2P verwendet kein herkömmliches TLS — die Verschlüsselung wird stattdessen auf der Netzwerkebene behandelt. Die Einbeziehung von HSTS würde Besucher vollständig von Ihrer I2P-Site aussperren.

### Schritt 2: Den Server Tunnel erstellen

Öffnen Sie die I2P Router Console in Ihrem Browser:

```
http://127.0.0.1:7657/i2ptunnel/
```
Klicken Sie auf **"Tunnel Wizard"**, um mit der Erstellung eines neuen Tunnels zu beginnen.

![I2P Tunnel Wizard startup](/images/guides/mirroring/mirror_02.svg)

Wählen Sie **"HTTP Server"** als tunnel-Typ und klicken Sie auf **Weiter**.

### Schritt 3: Den Tunnel konfigurieren

Füllen Sie die Tunnel-Einstellungen aus:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Setting</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Name</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">My Website Mirror</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Any descriptive name</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Description</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(optional)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Helps you remember what this tunnel is for</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Target Host</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>127.0.0.1</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Always localhost</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Target Port</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>8080</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Must match the port from Step 1</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Website Hostname</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>mysite.i2p</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The .i2p name you want (registered later)</td>
    </tr>
  </tbody>
</table>
![Tunnel-Konfigurationseinstellungen](/images/guides/mirroring/mirror_03.png)

Klicken Sie auf **"Erstellen"**, um Ihren tunnel zu generieren. I2P wird einen eindeutigen kryptografischen Zielschlüssel erstellen — dies wird Ihre permanente Adresse im Netzwerk.

### Schritt 4: Den Tunnel starten und warten

Finden Sie Ihren neuen tunnel in der Liste und klicken Sie auf **"Start"**. Sie werden sehen:

- **Lokales Ziel** — eine lange base32-Adresse wie `abc123...xyz.b32.i2p`
- **Status** — sollte sich zu "Running" ändern

![Tunnel running status](/images/guides/mirroring/mirror_04.png)

> **Seien Sie geduldig!** Der erste Start dauert 2–5 Minuten, während Ihr tunnel aufgebaut wird und seine leaseSets im Netzwerk veröffentlicht. Das ist normal.

### Schritt 5: Testen Sie Ihren Mirror

Sobald der tunnel als laufend angezeigt wird, öffnen Sie Ihren I2P-konfigurierten Browser und besuchen Sie Ihre base32-Adresse. Das erste Laden der Seite kann 5–30 Sekunden dauern — das ist typisch für I2P.

Wenn die Seite lädt, herzlichen Glückwunsch — Ihre Website ist jetzt live auf I2P!

### Schritt 6: Eine lesbare .i2p-Adresse registrieren (Optional)

Ihre Website ist bereits über die base32-Adresse erreichbar, aber `abc123...xyz.b32.i2p` ist nicht gerade einprägsam. Um eine saubere `.i2p`-Domain zu erhalten:

**Für Ihr eigenes Adressbuch** — gehen Sie zu `http://127.0.0.1:7657/dns` und fügen Sie Ihren gewählten Hostnamen hinzu, der Ihrem Zielschlüssel zugeordnet ist.

**Für öffentliche Auffindbarkeit** — registrieren Sie sich im I2P-Adressverzeichnis:

1. Besuchen Sie `http://stats.i2p/i2p/addkey.html` (innerhalb von I2P)
2. Geben Sie Ihren gewünschten Hostnamen und Ihren vollständigen destination key (die 500+ Zeichen lange Zeichenkette aus Ihren tunnel-Details, die mit "AAAA" endet) ein
3. Zur Registrierung absenden

Sobald registriert, kann jeder mit den entsprechenden Adressbuch-Abonnements Ihre Website über den Namen finden.

## Teil 2: Spiegelung dynamischer Anwendungen

Wenn Ihre Website auf einem Backend-Framework (Node.js, Python, Ruby, PHP, etc.) anstatt auf statischen Dateien läuft, benötigen Sie Nginx oder Apache als Reverse Proxy zwischen dem I2P tunnel und Ihrer Anwendung.

### Reverse Proxy-Konfiguration (Nginx)

```nginx
server {
    listen 127.0.0.1:8080;
    server_name yourapp.i2p;

    server_tokens off;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;

        proxy_set_header Host $host;
        proxy_set_header X-I2P-Request "true";

        # CRITICAL: never forward real IP headers
        proxy_set_header X-Forwarded-For "";
        proxy_set_header X-Real-IP "";

        # Strip headers that leak information
        proxy_hide_header Strict-Transport-Security;
        proxy_hide_header X-Powered-By;
        proxy_hide_header Server;

        # Extended timeouts — I2P is slower than clearnet
        proxy_connect_timeout 60s;
        proxy_read_timeout 120s;
        proxy_send_timeout 60s;
    }
}
```
Der `X-I2P-Request` Header ermöglicht es Ihrer Anwendung, I2P-Traffic zu erkennen, falls sie sich anders verhalten muss (zum Beispiel das Deaktivieren von Funktionen, die Clearnet-Zugang erfordern).

### URL-Umschreibung für Clearnet-Spiegel

Wenn Ihre Anwendung URLs generiert, die auf Ihre Clearnet-Domain verweisen, sollten Sie diese für I2P-Besucher umschreiben:

```nginx
location / {
    proxy_pass http://127.0.0.1:3000;

    sub_filter_once off;
    sub_filter_types text/html text/css application/javascript;

    # Rewrite your clearnet domain to the I2P domain
    sub_filter 'https://www.example.com' 'http://yoursite.i2p';
    sub_filter '//www.example.com' '//yoursite.i2p';
}
```
Erstellen Sie dann einen HTTP-Server-Tunnel, der auf `127.0.0.1:8080` zeigt, genau wie in Teil 1.

## Teil 3: Git-Repositories spiegeln

### Gitea (Vollständig ausgestattet)

Gitea ist eine großartige Wahl für das Hosting von Git über I2P. Es verfügt über eine Weboberfläche, Issue-Tracking und Pull-Requests — all das funktioniert gut über das Netzwerk.

Konfiguriere `/etc/gitea/app.ini`:

```ini
[server]
HTTP_ADDR     = 127.0.0.1
HTTP_PORT     = 3000
DOMAIN        = yourgit.i2p
ROOT_URL      = http://yourgit.i2p/
SSH_DOMAIN    = yourgit.i2p
PROTOCOL      = http
OFFLINE_MODE  = true

[service]
DISABLE_REGISTRATION    = false
REGISTER_MANUAL_CONFIRM = true
REGISTER_EMAIL_CONFIRM  = false

[mailer]
ENABLED = false

[session]
COOKIE_SECURE = false
```
Wichtige Punkte: `OFFLINE_MODE = true` verhindert, dass Gitea externe Ressourcen lädt (Avatare, CDN-Assets). `COOKIE_SECURE = false` ist erforderlich, da I2P HTTPS nicht im traditionellen Sinne verwendet. Deaktivieren Sie E-Mail, da Ihr I2P-Server möglicherweise keine ausgehende E-Mail konfiguriert hat.

Erstelle zwei tunnel: 1. **HTTP Server tunnel** → `127.0.0.1:3000` (Web-Interface) 2. **Standard Server tunnel** → `127.0.0.1:22` (SSH-Zugang für git push/pull — optional)

### cgit (Leichtgewichtige Alternative)

Wenn Sie nur schreibgeschütztes Browsing und HTTP-Klonen benötigen, ist cgit viel leichter:

```ini
# /etc/cgitrc
virtual-root=/
clone-url=http://yourgit.i2p/$CGIT_REPO_URL
cache-root=/var/cache/cgit
cache-size=1000
scan-path=/srv/git
enable-http-clone=1
```
Das aggressive Caching von cgit macht es besonders gut geeignet für die höhere Latenz von I2P.

### Client-seitige Einrichtung für Git über I2P

Jeder, der von deinem I2P Git-Mirror klont, muss den Git-Traffic durch den I2P HTTP-Proxy routen:

```bash
# Tell Git to use the I2P proxy for .i2p domains
git config --global http.http://yourgit.i2p.proxy http://127.0.0.1:4444
git config --global http.timeout 300

# Clone (allow for I2P latency)
GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=60 \
    git clone http://yourgit.i2p/repo
```
Für große Repositories sparen shallow clones viel Zeit über I2P:

```bash
git clone --depth 1 http://yourgit.i2p/project
git fetch --unshallow   # grab full history later if needed
```
## Teil 4: Spiegelung von Datei-Hosting

### Nextcloud

Nextcloud funktioniert über I2P mit einiger Konfiguration. Bearbeiten Sie `config/config.php`:

```php
$CONFIG = array(
    'trusted_domains' => array(
        0 => 'localhost',
        1 => 'yourbase32address.b32.i2p',
        2 => 'yoursite.i2p',
    ),
    'trusted_proxies'   => array('127.0.0.1'),
    'overwritehost'     => 'yoursite.i2p',
    'overwriteprotocol' => 'http',
    'overwrite.cli.url' => 'http://yoursite.i2p/',
);
```
Was gut funktioniert: Datei-Upload und -Download, Verzeichnis-Browsing, Authentifizierung, öffentliche Link-Freigabe und WebDAV. Was nicht funktioniert: Desktop-Synchronisations-Clients benötigen SOCKS-Proxy-Konfiguration, externe Speicher-Backends können IP-Adressen preisgeben, und die Verbindung mit Clearnet-Nextcloud-Instanzen kann die Privatsphäre gefährden.

### Einfacher Dateiserver

Für einfaches Datei-Hosting ohne den Overhead von Nextcloud reicht ein minimaler Python-Server aus:

```python
#!/usr/bin/env python3
import http.server
import socketserver

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    server_version = ""  # don't reveal server software
    sys_version = ""

with socketserver.TCPServer(("127.0.0.1", 8080), QuietHandler) as httpd:
    print("Serving on 127.0.0.1:8080")
    httpd.serve_forever()
```
Erstellen Sie einen HTTP-Server-tunnel, der auf `127.0.0.1:8080` zeigt.

## Teil 5: Mirroring APIs

### Einfacher API-Proxy

```nginx
server {
    listen 127.0.0.1:8080;
    server_name api.yoursite.i2p;

    server_tokens off;

    location / {
        proxy_pass http://127.0.0.1:3000;

        proxy_set_header Host $host;
        proxy_set_header Content-Type $content_type;

        # Strip identifying headers
        proxy_set_header X-Forwarded-For "";
        proxy_set_header X-Real-IP "";
        proxy_hide_header X-Powered-By;

        # I2P-appropriate timeouts
        proxy_connect_timeout 60s;
        proxy_read_timeout 120s;
    }
}
```
### WebSocket-Unterstützung

Wenn Ihre Anwendung WebSockets verwendet (Chat-Apps, Live-Dashboards, etc.):

```nginx
map $http_upgrade $connection_upgrade {
    default upgrade;
    ''      close;
}

server {
    listen 127.0.0.1:8080;

    location /ws {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;

        # Long timeout for persistent connections
        proxy_read_timeout 3600s;
        proxy_send_timeout 3600s;
        proxy_buffering off;
    }
}
```
Beachten Sie, dass WebSockets über I2P eine deutlich höhere Latenz als das Clearnet haben werden. Für Echtzeit-Funktionen sollten Sie längere Polling-Intervalle oder optimistische UI-Updates auf der Client-Seite in Betracht ziehen.

## Sicherheits-Best-Practices

Ihren Mirror zum Laufen zu bringen ist der einfache Teil. Ihn sicher zu halten erfordert Aufmerksamkeit für einige Details, die einzigartig für I2P-Hosting sind.

![Sicherheitscheckliste für I2P-Spiegel](/images/guides/mirroring/security-checklist.svg)

### Die wichtigsten Regeln

**Nur an localhost binden.** Ihr Dienst sollte auf `127.0.0.1` lauschen, niemals auf `0.0.0.0`. Der I2P router sollte das einzige sein, was Ihren Dienst erreichen kann.

**Identifizierende Header entfernen.** Webserver geben gerne bekannt, welche Software sie verwenden. Über I2P sind das Informationen, die Sie nicht teilen möchten.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">What It Leaks</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">How to Fix</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Server</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Web server software and version</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>server_tokens off;</code> (Nginx)</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>X-Powered-By</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Application framework</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>proxy_hide_header X-Powered-By;</code></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>X-Forwarded-For</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">IP addresses in proxy chain</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>proxy_set_header X-Forwarded-For "";</code></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>X-Real-IP</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Client IP address</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>proxy_set_header X-Real-IP "";</code></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>Strict-Transport-Security</code></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Breaks I2P access entirely</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><code>proxy_hide_header Strict-Transport-Security;</code></td>
    </tr>
  </tbody>
</table>
**Hoste alles selbst.** Lade keine Schriftarten von Google, Skripte von CDNs oder Analytics von Drittanbietern. Jede externe Ressource ist eine Anfrage, die das I2P-Netzwerk verlässt, was enorme Latenz hinzufügt und möglicherweise Informationen preisgibt. Lade Bibliotheken und Schriftarten herunter, platziere sie auf deinem Server und stelle sie lokal bereit.

**Niemals Datenbanken offenlegen.** Es sollte selbstverständlich sein, aber erstellen Sie keine I2P tunnel zu Ihren Datenbankports. Server tunnel sollten nur auf Webserver oder Anwendungsserver zeigen.

## Performance-Optimierung

I2P fügt 2–10 Sekunden Latenz pro Anfrage hinzu. Das ist der Preis für Multi-Hop-Verschlüsselung. Aber mit der richtigen Einstellung kann sich Ihr I2P-Mirror überraschend flink anfühlen.

### Cache aggressiv

Statische Assets sollten lange Cache-Laufzeiten haben. Wenn ein Besucher bereits Ihr CSS und Ihre Bilder geladen hat, sollte er nicht noch einmal darauf warten müssen:

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```
### Komprimierung aktivieren

Kleinere Datenmengen bedeuten schnellere Übertragungen über I2Ps begrenzte Bandbreite:

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript
           text/xml application/xml application/xml+rss;
```
### Tunnel-Anzahl für Traffic anpassen

Mehr tunnels bedeuten mehr gleichzeitige Verbindungen. Der Standardwert von 3 ist für Websites mit geringem Verkehr ausreichend, aber wenn Sie Überlastung feststellen:

```properties
tunnel.0.option.inbound.quantity=5
tunnel.0.option.outbound.quantity=5
tunnel.0.option.inbound.backupQuantity=2
tunnel.0.option.outbound.backupQuantity=2
```
### Tunnel-Länge (Hops)

Jeder Hop fügt Latenz hinzu, aber auch Anonymität. Wählen Sie basierend auf Ihrem Bedrohungsmodell:

![Tunnel-Hop-Kompromiss — mehr Hops bedeuten mehr Privatsphäre, aber höhere Latenz](/images/guides/mirroring/tunnel-hops.svg)

Für einen öffentlichen Mirror, bei dem die Identität des Servers bereits bekannt ist (zum Beispiel die Website Ihrer Organisation), ist eine Reduzierung auf 2 Hops ein vernünftiger Kompromiss:

```properties
tunnel.0.option.inbound.length=2
tunnel.0.option.outbound.length=2
```
### Allgemeine Router-Tipps

- Lassen Sie Ihren I2P router **24/7** laufen. Je länger er aktiv ist, desto besser ist er in das Netzwerk integriert und desto schneller arbeiten Ihre tunnels.
- Setzen Sie die Bandbreitenteilung auf mindestens **256 KB/s**, aber halten Sie sie etwas unter Ihrer tatsächlichen Leitungsgeschwindigkeit.
- Erwarten Sie, dass die ersten Verbindungen nach einem Neustart langsam sind (30–90 Sekunden). Das verbessert sich schnell, wenn sich tunnels aufbauen.

## Erweitert: Manuelle Tunnel-Konfiguration

Der Router Console-Assistent funktioniert großartig, aber wenn Sie es vorziehen, Konfigurationsdateien direkt zu bearbeiten — oder Deployments automatisieren müssen — können Sie tunnel in `~/.i2p/i2ptunnel.config` (oder `/var/lib/i2p/i2p-config/i2ptunnel.config` für Systeminstallationen) konfigurieren:

```properties
# HTTP Server Tunnel
tunnel.0.name=My Website
tunnel.0.description=I2P mirror of my clearnet site
tunnel.0.type=httpserver
tunnel.0.targetHost=127.0.0.1
tunnel.0.targetPort=8080
tunnel.0.privKeyFile=mysite-privKeys.dat
tunnel.0.spoofedHost=mysite.i2p
tunnel.0.startOnLoad=true
tunnel.0.sharedClient=false

# I2CP connection settings
tunnel.0.i2cpHost=127.0.0.1
tunnel.0.i2cpPort=7654

# Tunnel pool configuration
tunnel.0.option.inbound.length=3
tunnel.0.option.inbound.quantity=3
tunnel.0.option.inbound.backupQuantity=1
tunnel.0.option.outbound.length=3
tunnel.0.option.outbound.quantity=3
tunnel.0.option.outbound.backupQuantity=1
```
I2P nach Änderungen neu starten:

```bash
sudo systemctl restart i2p
```
Ab I2P 0.9.42 können Sie auch individuelle Konfigurationsdateien in `i2ptunnel.config.d/` für eine sauberere Verwaltung mehrerer tunnel verwenden:

```bash
mkdir -p ~/.i2p/i2ptunnel.config.d/

cat > ~/.i2p/i2ptunnel.config.d/mysite.config <<EOF
tunnel.0.name=My Website
tunnel.0.type=httpserver
tunnel.0.targetHost=127.0.0.1
tunnel.0.targetPort=8080
tunnel.0.privKeyFile=mysite-privKeys.dat
tunnel.0.startOnLoad=true
EOF
```
## Fehlerbehebung

### "Ich kann meine Seite nicht erreichen"

Arbeiten Sie diese Checkliste der Reihe nach ab:

**1. Lauscht der Webserver tatsächlich?**

```bash
nc -zv 127.0.0.1 8080
```
Wenn dies fehlschlägt, liegt ein Problem mit der Konfiguration Ihres Webservers vor — gehen Sie zurück zu Schritt 1.

**2. Läuft der tunnel?** Besuchen Sie `http://127.0.0.1:7657/i2ptunnel/` und überprüfen Sie den Status. Wenn dort länger als 5 Minuten "Starting" angezeigt wird, überprüfen Sie die Netzwerkintegration Ihres routers.

**3. Ist das LeaseSet veröffentlicht?** Stellen Sie sicher, dass `i2cp.dontPublishLeaseSet` NICHT in Ihren Tunnel-Optionen gesetzt ist. Ohne ein veröffentlichtes LeaseSet kann niemand Ihren Tunnel finden.

**4. Ist deine Uhr genau?** I2P erfordert eine Zeitgenauigkeit innerhalb von 60 Sekunden. Überprüfe mit:

```bash
timedatectl status
```
Wenn Ihre Uhr falsch geht, wird I2P Probleme beim Aufbau von tunnels haben.

### Langsame Leistung nach Neustart

Das ist normal. Geben Sie Ihrem I2P router nach einem Neustart 10–15 Minuten Zeit, um seine tunnel-Pools wieder aufzubauen und sich erneut in das Netzwerk zu integrieren. Die Leistung verbessert sich, wenn mehr Teilnehmer von Ihrem router erfahren.

Überprüfen Sie auch, dass die Portweiterleitung für Ihren I2NP-Port konfiguriert ist (prüfen Sie die Router-Konsole für die spezifische Portnummer). Ohne diese arbeitet Ihr Router im "Firewall-Modus", was die Leistung einschränkt.

### "Adresse nicht gefunden"-Fehler wenn andere zu Besuch kommen

Besucher benötigen Ihre Adresse in ihrem Adressbuch. Stellen Sie sicher, dass Sie sich bei einem öffentlichen Adressbuch registriert haben, oder teilen Sie Ihre vollständige base32-Adresse direkt. Sie können auch weitere Abonnements unter `http://127.0.0.1:7657/susidns/subscriptions` hinzufügen:

```
http://stats.i2p/cgi-bin/newhosts.txt
http://i2host.i2p/cgi-bin/i2hostetag
```
### Timeouts beim Testen

I2P hat von Natur aus höhere Umlaufzeiten. Beim Testen von der Kommandozeile aus verwenden Sie erweiterte Timeouts:

```bash
# curl
curl --connect-timeout 60 --max-time 300 http://yoursite.i2p/

# wget
wget --timeout=300 http://yoursite.i2p/
```
### Logs lesen

Wenn nichts anderes hilft, überprüfen Sie die I2P router-Logs auf Fehler:

```bash
# System service
sudo journalctl -u i2p -f

# Or directly
tail -f ~/.i2p/logs/log-router-0.txt
```
## Sichern Sie Ihre Schlüssel

Das ist das Eine, was Sie auf keinen Fall überspringen dürfen. Die privaten Schlüsseldateien Ihres tunnels (`.dat` Dateien in Ihrem I2P-Konfigurationsverzeichnis) sind das, was Ihrem Dienst seine permanente Adresse im Netzwerk verleiht. Wenn Sie diese verlieren, verlieren Sie Ihre I2P-Adresse — dauerhaft. Es gibt keine Wiederherstellung, keinen Reset, kein Support-Ticket. Sie müssten mit einer neuen Adresse von vorne anfangen.

Sichern Sie sie jetzt:

```bash
# User installation
tar -czf tunnel-keys-backup.tar.gz ~/.i2p/*.dat

# System installation
sudo tar -czf tunnel-keys-backup.tar.gz /var/lib/i2p/i2p-config/*.dat
```
Speichern Sie die Sicherung an einem sicheren Ort außerhalb des Servers.

## Sie sind fertig

Das war's. Ihr Service ist nun sowohl im regulären Internet als auch im I2P-Netzwerk verfügbar. Sie bieten den Menschen eine private Möglichkeit, auf Ihre Inhalte zuzugreifen — eine, bei der ihre Identität ihre eigene bleibt.

Wenn Sie auf Probleme stoßen oder sich stärker einbringen möchten, finden Sie hier die Community:

- **Forum:** [i2pforum.net](https://i2pforum.net)
- **IRC:** #i2p auf verschiedenen Netzwerken
- **Entwicklung:** [i2pgit.org](https://i2pgit.org)
- **StormyCloud:** [stormycloud.org](https://www.stormycloud.org)

---

*Leitfaden erstellt von [StormyCloud Inc](https://www.stormycloud.org) für die I2P-Community.*
