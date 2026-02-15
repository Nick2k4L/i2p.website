---
title: "Zrcadlení vašich služeb na I2P"
description: "Průvodce pro začátečníky k zpřístupnění vašich webových stránek, Git repozitářů, API a dalšího na síti I2P — s postupnými instrukcemi a diagramy"
slug: "mirroring-guide"
lastUpdated: "2025-02"
accurateFor: "2.10.0"
---

Máte webovou stránku na běžném internetu. Teď ji chcete zpřístupnit i na I2P — aby ji lidé mohli navštívit soukromě, aniž by odhalili svou identitu nebo odkud přicházejí. O tom je tento návod.

Zrcadlení nenahrazuje vaši stávající stránku. Přidává druhý vstup — soukromý — prostřednictvím sítě I2P. Vaše clearnet stránka pokračuje v provozu přesně jako předtím.

![Jak funguje I2P zrcadlení — váš server získá druhý, soukromý vstup přes I2P síť](/images/guides/mirroring/how-mirroring-works.svg)

## Proč zrcadlit na I2P?

Existuje několik praktických důvodů pro zrcadlení vašich služeb:

**Soukromí pro vaše návštěvníky.** Lidé mohou přistupovat k vašemu obsahu, aniž by odhalili svou IP adresu. Provoz mezi nimi a vaší službou je šifrován přes několik přeskoků — ani vy, ani nikdo, kdo sleduje síť, nemůže identifikovat, kdo vás navštěvuje.

**Odolnost vůči cenzuře.** Pokud je váš web v určitých regionech blokován DNS filtrováním, blokováním IP adres nebo jinými způsoby, I2P zrcadlo zůstává dostupné. Nezávisí na DNS nebo konvenčním IP směrování.

**Odolnost.** I2P zrcadlo přidává redundanci. Pokud je vaše doména zabavena nebo vás CDN zruší, I2P verze zůstane funkční, dokud běží váš server.

**Podpora sítě.** Každá služba na I2P činí síť užitečnější a pomáhá růstu ekosystému.

## Co budete potřebovat

Než začnete, ujistěte se, že máte:

- **Běžící I2P router** na vašem serveru (Java implementace). Pokud jej ještě nemáte, nejdříve postupujte podle [Průvodce instalací I2P](/downloads/).
- **Vaše webová stránka nebo služba již funguje** — měla by poskytovat obsah na vašem serveru.
- **Základní znalost příkazové řádky** — budete editovat konfigurační soubor a spouštět několik příkazů.
- **Asi 15–20 minut** — to je vše, co potřebujete.

Váš I2P router potřebuje alespoň 512 MB RAM a funguje nejlépe na serveru s nepřetržitým provozem 24/7. Pokud se váš router spustil poprvé, dejte mu 10–15 minut na integraci se sítí před vytvářením tunnelů.

## Porozumění Tunnelům

Základní koncept za I2P zrcadlením je **server tunnel**. Zde je myšlenka:

Když někdo na I2P chce navštívit vaši stránku, jejich požadavek cestuje přes několik šifrovaných skoků napříč I2P sítí, dokud nedosáhne vašeho I2P routeru. Váš router pak předá požadavek **server tunnelu**, který jej přepošle vašemu webovému serveru běžícímu na localhost. Váš webový server odpoví a odpověď se vrátí zpět opačnou cestou přes šifrovanou síť.

Váš webový server se pro tyto požadavky nikdy nedostane do kontaktu s veřejným internetem — komunikuje pouze s localhost. I2P router se stará o veškerou síťovou komunikaci.

### Jaký typ tunelu potřebujete?

I2P nabízí několik typů tunelů pro různé situace:

![Porovnání typů tunelů — HTTP Server je správná volba pro většinu webových stránek](/images/guides/mirroring/tunnel-types.svg)

Pro zrcadlení webové stránky téměř jistě chcete **HTTP Server** tunnel. Je navržen speciálně pro webový provoz a zvládá filtrování hlaviček, kompresi a maskování hostname přímo v základní konfiguraci. Ostatní typy existují pro specializované případy použití jako SSH přístup, obousměrné aplikace nebo IRC servery.

## Část 1: Zrcadlení webové stránky

Toto je nejčastější scénář — máte existující clearnet webovou stránku a chcete ji zpřístupnit přes I2P. Zde je postup v kostce:

![Pět kroků pro zrcadlení vaší stránky na I2P](/images/guides/mirroring/steps-overview.svg)

Pojďme si projít každý krok.

### Krok 1: Přidejte localhost listener do vašeho webového serveru

Váš clearnet web pravděpodobně už běží na portech 80 a 443, otevřený světu. Pro I2P vytvoříte *samostatný* listener na localhost, ke kterému má přístup pouze I2P tunnel. To vám dává plnou kontrolu nad tím, jak vypadá I2P verze — můžete odstranit hlavičky, zablokovat administrátorské panely a vyladit cache pro vyšší latenci I2P.

> **Rychlá alternativa:** Pokud nepotřebujete žádné přizpůsobení, můžete tento krok přeskočit a nasměrovat I2P tunnel přímo na `127.0.0.1:80`. Ale přístup s dedikovaným naslouchačem je doporučený.

Vyberte svůj webový server:

#### Nginx

Vytvořte novou konfiguraci webu:

```bash
sudo nano /etc/nginx/sites-available/i2p-mirror
```
Vložte tuto konfiguraci a nahraďte `yoursite.i2p` a kořenovou cestu svými vlastními hodnotami:

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
Povolte jej a znovu načtěte:

```bash
sudo ln -s /etc/nginx/sites-available/i2p-mirror /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```
#### Apache

Vytvořte novou konfiguraci webu:

```bash
sudo nano /etc/apache2/sites-available/i2p-mirror.conf
```
Vložte tuto konfiguraci:

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
Poté přidejte port, povolte stránku a znovu načtěte:

```bash
echo "Listen 127.0.0.1:8080" | sudo tee -a /etc/apache2/ports.conf
sudo a2ensite i2p-mirror
sudo a2enmod headers
sudo a2dismod status info
sudo apachectl configtest
sudo systemctl reload apache2
```
#### Proč žádné HSTS?

Všimnete si, že obě konfigurace výslovně vyhýbají hlavičkám `Strict-Transport-Security`. To je klíčové. HSTS říká prohlížečům, aby používaly pouze HTTPS, ale I2P nepoužívá tradiční TLS — šifrování je místo toho zajištěno na síťové vrstvě. Zahrnutí HSTS by návštěvníky úplně vyloučilo z vaší I2P stránky.

### Krok 2: Vytvoření tunelu serveru

Otevřete I2P Router Console ve vašem prohlížeči:

```
`http://127.0.0.1:7657/i2ptunnel/`
```
Klikněte na **"Tunnel Wizard"** pro zahájení vytváření nového tunnelu.

![I2P Tunnel Wizard startup](/images/guides/mirroring/mirror_02.svg)

Vyberte **"HTTP Server"** jako typ tunelu a klikněte na **Další**.

### Krok 3: Nakonfigurujte tunnel

Vyplňte nastavení tunelu:

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
![Nastavení konfigurace tunelu](/images/guides/mirroring/mirror_03.png)

Klikněte na **"Vytvořit"** pro vygenerování vašeho tunelu. I2P vytvoří jedinečný kryptografický klíč destinace — ten se stane vaší trvalou adresou v síti.

### Krok 4: Spusťte tunnel a čekejte

Najděte svůj nový tunnel v seznamu a klikněte na **"Start"**. Uvidíte:

- **Místní Cíl** — dlouhá base32 adresa jako `abc123...xyz.b32.i2p`
- **Stav** — měl by se změnit na "Běží"

![Tunnel running status](/images/guides/mirroring/mirror_04.png)

> **Buďte trpěliví!** První spuštění trvá 2–5 minut, zatímco se váš tunnel vytváří a publikuje své leaseSety do sítě. To je normální.

### Krok 5: Otestujte své zrcadlo

Jakmile se tunnel zobrazí jako spuštěný, otevřete váš pro I2P nakonfigurovaný prohlížeč a navštivte vaši base32 adresu. První načtení stránky může trvat 5–30 sekund — to je pro I2P typické.

Pokud se stránka načte, gratulujeme — vaše stránka je nyní spuštěna na I2P!

### Krok 6: Registrace lidsky čitelné .i2p adresy (volitelné)

Vaše stránka je již přístupná přes base32 adresu, ale `abc123...xyz.b32.i2p` není zrovna zapamatovatelná. Pro získání čisté `.i2p` domény:

**Pro váš vlastní adresář** — přejděte na `http://127.0.0.1:7657/dns` a přidejte vámi zvolený hostname mapovaný na váš cílový klíč.

**Pro veřejné objevení** — zaregistrujte se v registru I2P adres:

1. Navštivte `http://stats.i2p/i2p/addkey.html` (uvnitř I2P)
2. Zadejte požadované hostname a váš úplný destination klíč (řetězec s 500+ znaky z detailů vašeho tunnel, končící na "AAAA")
3. Odešlete k registraci

Jakmile bude registrován, kdokoli s odpovídajícími předplatnými adresáře bude moci najít vaši stránku podle názvu.

## Část 2: Zrcadlení dynamických aplikací

Pokud váš web běží na backend frameworku (Node.js, Python, Ruby, PHP, atd.) namísto statických souborů, potřebujete Nginx nebo Apache jako reverse proxy mezi I2P tunnel a vaší aplikací.

### Konfigurace Reverse Proxy (Nginx)

```nginx
server {
    listen 127.0.0.1:8080;
    server_name yourapp.i2p;

    server_tokens off;

    location / {
        proxy_pass `http://127.0.0.1:3000;`
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
Hlavička `X-I2P-Request` umožňuje vaší aplikaci detekovat I2P provoz, pokud se potřebuje chovat odlišně (například zakázat funkce, které vyžadují přístup k clearnet).

### Přepisování URL pro clearnet zrcadla

Pokud vaše aplikace generuje URL adresy směřující na vaši clearnet doménu, budete je chtít přepsat pro I2P návštěvníky:

```nginx
location / {
    proxy_pass `http://127.0.0.1:3000;`

    sub_filter_once off;
    sub_filter_types text/html text/css application/javascript;

    # Rewrite your clearnet domain to the I2P domain
    sub_filter 'https://www.example.com' 'http://yoursite.i2p';
    sub_filter '//www.example.com' '//yoursite.i2p';
}
```
Poté vytvořte HTTP Server tunnel směřující na `127.0.0.1:8080`, stejně jako v části 1.

## Část 3: Zrcadlení Git repozitářů

### Gitea (Plně vybavené)

Gitea je skvělá volba pro hostování Git přes I2P. Má webové rozhraní, sledování problémů a pull requesty — vše funguje dobře přes síť.

Nakonfigurujte `/etc/gitea/app.ini`:

```ini
[server]
HTTP_ADDR     = 127.0.0.1
HTTP_PORT     = 3000
DOMAIN        = yourgit.i2p
ROOT_URL      = `http://yourgit.i2p/`
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
Klíčové body: `OFFLINE_MODE = true` zabraňuje Gitea načítat externí zdroje (avatary, CDN assety). `COOKIE_SECURE = false` je potřeba, protože I2P nepoužívá HTTPS v tradičním smyslu. Zakažte email, protože váš I2P server nemusí mít nakonfigurovaný odchozí email.

Vytvořte dva tunnely: 1. **HTTP Server tunnel** → `127.0.0.1:3000` (webové rozhraní) 2. **Standard Server tunnel** → `127.0.0.1:22` (SSH přístup pro git push/pull — volitelné)

### cgit (Lehká alternativa)

Pokud potřebujete pouze prohlížení jen pro čtení a HTTP klonování, cgit je mnohem lehčí:

```ini
# /etc/cgitrc
virtual-root=/
clone-url=`http://yourgit.i2p/$CGIT_REPO_URL`
cache-root=/var/cache/cgit
cache-size=1000
scan-path=/srv/git
enable-http-clone=1
```
Agresivní kešování cgit z něj dělá obzvláště vhodný nástroj pro vyšší latenci I2P.

### Nastavení na straně klienta pro Git přes I2P

Kdokoli, kdo klonuje z vašeho I2P Git mirror, musí směrovat Git provoz přes I2P HTTP proxy:

```bash
# Tell Git to use the I2P proxy for .i2p domains
git config --global http.http://yourgit.i2p.proxy `http://127.0.0.1:4444`
git config --global http.timeout 300

# Clone (allow for I2P latency)
GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=60 \
    git clone `http://yourgit.i2p/repo`
```
Pro velké repozitáře šetří mělké klony spoustu času přes I2P:

```bash
git clone --depth 1 `http://yourgit.i2p/project`
git fetch --unshallow   # grab full history later if needed
```
## Část 4: Zrcadlení hostování souborů

### Nextcloud

Nextcloud funguje přes I2P s určitým nastavením. Upravte `config/config.php`:

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
    'overwrite.cli.url' => '`http://yoursite.i2p/',`
);
```
Co funguje dobře: nahrávání a stahování souborů, procházení adresářů, autentizace, sdílení veřejných odkazů a WebDAV. Co nefunguje: desktopové synchronizační klienty potřebují konfiguraci SOCKS proxy, externí úložné backendy mohou prozradit IP adresy a federace s clearnet Nextcloud instancemi může ohrozit soukromí.

### Jednoduchý souborový server

Pro jednoduché hostování souborů bez režie Nextcloud postačí minimální Python server:

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
Vytvořte HTTP Server tunnel směřující na `127.0.0.1:8080`.

## Část 5: Zrcadlové API

### Základní API Proxy

```nginx
server {
    listen 127.0.0.1:8080;
    server_name api.yoursite.i2p;

    server_tokens off;

    location / {
        proxy_pass `http://127.0.0.1:3000;`

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
### Podpora WebSocket

Pokud vaše aplikace používá WebSockets (chatovací aplikace, živé dashboardy atd.):

```nginx
map $http_upgrade $connection_upgrade {
    default upgrade;
    ''      close;
}

server {
    listen 127.0.0.1:8080;

    location /ws {
        proxy_pass `http://127.0.0.1:3000;`
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
Upozorňujeme, že WebSockety přes I2P budou mít výrazně vyšší latenci než na clearnet. Pro funkce v reálném čase zvažte delší intervaly dotazování nebo optimistické aktualizace UI na straně klienta.

## Nejlepší bezpečnostní postupy

Zprovoznění vašeho zrcadla je ta snadná část. Udržet ho bezpečné vyžaduje pozornost k několika detailům, které jsou jedinečné pro hostování v I2P.

![Bezpečnostní kontrolní seznam pro I2P zrcadla](/images/guides/mirroring/security-checklist.svg)

### Hlavní pravidla

**Bind pouze na localhost.** Vaše služba by měla naslouchat na `127.0.0.1`, nikdy ne na `0.0.0.0`. I2P router je jediná věc, která by měla být schopna dosáhnout vaší služby.

**Odstraňte identifikační hlavičky.** Webové servery rády oznamují, jaký software používají. Přes I2P jsou to informace, které nechcete sdílet.

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
**Hostujte všechno sami.** Nenahrávejte písma z Google, skripty z CDN nebo analytické nástroje od třetích stran. Každý externí zdroj je požadavek, který opouští I2P síť, přidává obrovskou latenci a potenciálně prozrazuje informace. Stáhněte si knihovny a písma, umístěte je na svůj server a poskytujte je lokálně.

**Nikdy nevystavujte databáze.** Mělo by být samozřejmé, ale nevytvářejte I2P tunnely na porty vašich databází. Server tunnely by měly směřovat pouze na webové servery nebo aplikační servery.

## Ladění výkonu

I2P přidává 2–10 sekund latence na požadavek. To je cena za multi-hop šifrování. Ale s řádným nastavením může vaše I2P zrcadlo působit překvapivě svižně.

### Agresivní ukládání do cache

Statické soubory by měly mít dlouhou dobu života cache. Pokud návštěvník již načetl vaše CSS a obrázky, neměl by na ně čekat znovu:

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```
### Povolit kompresi

Menší datové pakety znamenají rychlejší přenosy přes omezenou šířku pásma I2P:

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript
           text/xml application/xml application/xml+rss;
```
### Nastavení množství tunnelů pro provoz

Více tunnelů znamená více současných připojení. Výchozí hodnota 3 je vhodná pro weby s nízkým provozem, ale pokud pozorujete přetížení:

```properties
tunnel.0.option.inbound.quantity=5
tunnel.0.option.outbound.quantity=5
tunnel.0.option.inbound.backupQuantity=2
tunnel.0.option.outbound.backupQuantity=2
```
### Délka tunelu (skoky)

Každý skok přidává latenci, ale také zvyšuje anonymitu. Vyberte podle vašeho modelu hrozeb:

![Kompromis počtu skoků tunnel — více skoků znamená více soukromí, ale vyšší latenci](/images/guides/mirroring/tunnel-hops.svg)

Pro veřejné zrcadlo, kde je identita serveru již známá (například webová stránka vaší organizace), snížení na 2 skoky je rozumný kompromis:

```properties
tunnel.0.option.inbound.length=2
tunnel.0.option.outbound.length=2
```
### Obecné tipy pro router

- Provozujte váš I2P router **24/7**. Čím déle běží, tím lépe je integrován do sítě a tím rychleji vaše tunnely fungují.
- Nastavte sdílení šířky pásma na nejméně **256 KB/sec**, ale udržujte ho mírně pod skutečnou rychlostí vašeho připojení.
- Očekávejte, že první připojení po restartu budou pomalá (30–90 sekund). To se rychle zlepší, jak se tunnely budují.

## Pokročilé: Ruční konfigurace tunnel

Průvodce Router Console funguje skvěle, ale pokud dáváte přednost přímé editaci konfiguračních souborů — nebo potřebujete automatizovat nasazení — můžete nakonfigurovat tunnely v `~/.i2p/i2ptunnel.config` (nebo `/var/lib/i2p/i2p-config/i2ptunnel.config` pro systémové instalace):

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
Restartujte I2P po změnách:

```bash
sudo systemctl restart i2p
```
Od verze I2P 0.9.42 můžete také používat jednotlivé konfigurační soubory v `i2ptunnel.config.d/` pro čistší správu více tunelů:

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
## Řešení problémů

### "Nemohu se dostat na svou stránku"

Projděte tento kontrolní seznam v daném pořadí:

**1. Naslouchá webový server skutečně?**

```bash
nc -zv 127.0.0.1 8080
```
Pokud se to nezdaří, je problém v konfiguraci vašeho webového serveru — vraťte se ke kroku 1.

**2. Běží tunnel?** Navštivte `http://127.0.0.1:7657/i2ptunnel/` a zkontrolujte stav. Pokud se zobrazuje "Starting" déle než 5 minut, zkontrolujte síťovou integraci vašeho routeru.

**3. Je LeaseSet publikován?** Ujistěte se, že `i2cp.dontPublishLeaseSet` NENÍ nastaveno ve vašich možnostech tunelu. Bez publikovaného LeaseSet nemůže nikdo váš tunel najít.

**4. Jsou vaše hodiny přesné?** I2P vyžaduje časovou přesnost do 60 sekund. Zkontrolujte pomocí:

```bash
timedatectl status
```
Pokud jsou vaše hodiny špatně nastavené, I2P bude mít problémy s vytvářením tunelů.

### Pomalý výkon po restartu

To je normální. Po restartování vašeho I2P routeru mu dejte 10–15 minut na obnovení tunnel poolů a opětovnou integraci se sítí. Výkon se zlepší, jakmile se více peerů dozví o vašem routeru.

Také zkontrolujte, že je nakonfigurováno přesměrování portů pro váš I2NP port (konkrétní číslo portu najdete v Router Console). Bez něj váš router funguje v "firewall" režimu, což omezuje výkon.

### Chyby "Adresa nebyla nalezena" při návštěvách ostatních

Návštěvníci potřebují vaši adresu ve svém adresáři. Ujistěte se, že jste se zaregistrovali ve veřejném adresáři, nebo sdílejte přímo svou plnou base32 adresu. Mohou také přidat další odběry na `http://127.0.0.1:7657/susidns/subscriptions`:

```
`http://stats.i2p/cgi-bin/newhosts.txt`
`http://i2host.i2p/cgi-bin/i2hostetag`
```
### Vypršení časových limitů při testování

I2P má ze své podstaty vyšší dobu odezvy. Při testování z příkazového řádku používejte prodloužené časové limity:

```bash
# curl
curl --connect-timeout 60 --max-time 300 `http://yoursite.i2p/`

# wget
wget --timeout=300 `http://yoursite.i2p/`
```
### Čtení logů

Pokud nic jiného nepomůže, zkontrolujte logy I2P routeru pro chyby:

```bash
# System service
sudo journalctl -u i2p -f

# Or directly
tail -f ~/.i2p/logs/log-router-0.txt
```
## Zálohujte si klíče

Toto je jedna věc, kterou rozhodně nesmíte přeskočit. Soubory s privátními klíči vašeho tunnelu (`.dat` soubory ve vašem I2P konfiguračním adresáři) jsou to, co vašemu servisu dává trvalou adresu v síti. Pokud je ztratíte, ztratíte svou I2P adresu — natrvalo. Neexistuje žádné obnovení, žádný reset, žádný servisní tiket. Museli byste začít znovu s novou adresou.

Zálohujte je nyní:

```bash
# User installation
tar -czf tunnel-keys-backup.tar.gz ~/.i2p/*.dat

# System installation
sudo tar -czf tunnel-keys-backup.tar.gz /var/lib/i2p/i2p-config/*.dat
```
Uložte zálohu na bezpečné místo mimo server.

## Hotovo

To je vše. Vaše služba je nyní dostupná jak na běžném internetu, tak na síti I2P. Poskytujete lidem soukromý způsob přístupu k vašemu obsahu — způsob, kde si jejich identita zůstává jejich vlastní.

Pokud narazíte na problémy nebo se chcete více zapojit, zde najdete komunitu:

- **Fórum:** [i2pforum.net](https://i2pforum.net)
- **IRC:** #i2p na různých sítích
- **Vývoj:** [i2pgit.org](https://i2pgit.org)
- **StormyCloud:** [stormycloud.org](https://www.stormycloud.org)

---

*Průvodce vytvořený společností [StormyCloud Inc](https://www.stormycloud.org) pro komunitu I2P.*
