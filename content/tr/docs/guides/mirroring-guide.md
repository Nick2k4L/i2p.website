---
title: "Hizmetlerinizi I2P'de Yansıtma"
description: "Web sitelerinizi, Git depolarınızı, API'lerinizi ve daha fazlasını I2P ağında erişilebilir hale getirmek için yeni başlayan dostu rehber — adım adım talimatlar ve diyagramlarla"
slug: "mirroring-guide"
lastUpdated: "2025-02"
accurateFor: "2.10.0"
---

Normal internette bir web siteniz var. Şimdi bunu I2P üzerinde de erişilebilir hale getirmek istiyorsunuz — böylece insanlar kim olduklarını veya nereden geldiklerini açığa çıkarmadan gizli bir şekilde ziyaret edebilsinler. Bu kılavuz tam da bununla ilgili.

Mirroring mevcut sitenizi değiştirmez. I2P ağı üzerinden ikinci bir giriş noktası — özel bir giriş — ekler. Clearnet siteniz daha önce olduğu gibi çalışmaya devam eder.

![I2P yansılamanın nasıl çalıştığı — sunucunuz I2P ağı üzerinden ikinci, özel bir giriş kapısı alır](/images/guides/mirroring/how-mirroring-works.svg)

## Neden I2P'ye Yansıtmalı?

Hizmetlerinizi yansılamanın birkaç pratik nedeni vardır:

**Ziyaretçileriniz için gizlilik.** İnsanlar IP adreslerini açığa çıkarmadan içeriğinize erişebilir. Onlarla hizmetiniz arasındaki trafik birden fazla atlama üzerinden şifrelenir — ne siz ne de ağı izleyen herhangi biri kimin ziyaret ettiğini belirleyemez.

**Sansür direnci.** Siteniz belirli bölgelerde DNS filtreleme, IP engelleme veya diğer yöntemlerle engelleniyorsa, I2P mirror erişilebilir kalır. DNS veya geleneksel IP yönlendirmesine bağımlı değildir.

**Dayanıklılık.** Bir I2P mirror yedeklilik sağlar. Alan adınız ele geçirilirse veya CDN'iniz sizi bırakırsa, sunucunuz çalıştığı sürece I2P sürümü ayakta kalır.

**Ağı destekleme.** I2P üzerindeki her hizmet, ağı daha kullanışlı hale getirir ve ekosistemin büyümesine yardımcı olur.

## İhtiyacınız Olanlar

Başlamadan önce, sahip olduğunuzdan emin olun:

- **Sunucunuzda çalışan bir I2P router** (Java uygulaması). Henüz yoksa, önce [I2P Kurulum Kılavuzu](/downloads/) takip edin.
- **Web siteniz veya hizmetiniz zaten çalışıyor olmalı** — sunucunuzda içerik sunuyor olması gerekir.
- **Temel komut satırı bilgisi** — bir yapılandırma dosyasını düzenleyecek ve birkaç komut çalıştıracaksınız.
- **Yaklaşık 15–20 dakika** — hepsi bu kadar sürer.

I2P router'ınızın en az 512 MB RAM'e ihtiyacı vardır ve 7/24 çalışma süresi olan bir sunucuda en iyi şekilde çalışır. Router'ınız ilk kez başlatıldıysa, tunnel oluşturmadan önce ağ ile entegre olması için 10-15 dakika bekleyin.

## Tunnel'ları Anlamak

I2P yansıtmanın arkasındaki temel kavram **server tunnel**'dır. İşte fikir şu:

I2P'deki birisi sitenizi ziyaret etmek istediğinde, istekleri I2P ağında birkaç şifreli atlama (hop) üzerinden geçerek I2P router'ınıza ulaşır. Router'ınız daha sonra isteği localhost'ta çalışan web sunucunuza ileten bir **server tunnel**'a aktarır. Web sunucunuz yanıt verir ve cevap şifreli ağ üzerinden ters yolu izleyerek geri döner.

Web sunucunuz bu istekler için hiçbir zaman genel internete dokunmaz — sadece localhost ile iletişim kurar. I2P router tüm ağ yönlü işlemleri halleder.

### Hangi Tunnel Türüne İhtiyacınız Var?

I2P farklı durumlar için çeşitli tunnel türleri sunar:

![Tunnel türleri karşılaştırması — HTTP Server çoğu web sitesi için doğru seçimdir](/images/guides/mirroring/tunnel-types.svg)

Bir web sitesini yansıtmak için, neredeyse kesinlikle bir **HTTP Server** tunnel isteyeceksiniz. Web trafiği için özel olarak tasarlanmıştır ve başlık filtreleme, sıkıştırma ve hostname spoofing işlemlerini hazır olarak yönetir. Diğer türler SSH erişimi, çift yönlü uygulamalar veya IRC sunucuları gibi özel kullanım durumları için mevcuttur.

## Bölüm 1: Bir Web Sitesini Yansıtma

Bu en yaygın senaryodur — mevcut bir clearnet web siteniz var ve bunu I2P üzerinden erişilebilir hale getirmek istiyorsunuz. İşte sürecin genel görünümü:

![Sitenizi I2P'de yansılamak için beş adım](/images/guides/mirroring/steps-overview.svg)

Her adımı tek tek inceleyelim.

### Adım 1: Web Sunucunuza Localhost Dinleyicisi Ekleyin

Clearnet siteniz muhtemelen zaten 80 ve 443 portlarında çalışıyor ve dünyaya açık durumda. I2P için, yalnızca I2P tunnel'ının erişebileceği localhost üzerinde *ayrı* bir dinleyici oluşturacaksınız. Bu size I2P versiyonunun nasıl görüneceği konusunda tam kontrol sağlar — başlıkları kaldırabilir, yönetici panellerini engelleyebilir ve I2P'nin daha yüksek gecikmesi için önbellekleme ayarlarını yapabilirsiniz.

> **Hızlı alternatif:** Herhangi bir özelleştirmeye ihtiyacınız yoksa, bu adımı atlayabilir ve I2P tunnel'ını doğrudan `127.0.0.1:80` adresine yönlendirebilirsiniz. Ancak özel dinleyici yaklaşımı önerilir.

Web sunucunuzu seçin:

#### Nginx

Yeni bir site yapılandırması oluşturun:

```bash
sudo nano /etc/nginx/sites-available/i2p-mirror
```
Bu yapılandırmayı yapıştırın, `yoursite.i2p` ve kök yolunu kendi değerlerinizle değiştirin:

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
Etkinleştirin ve yeniden yükleyin:

```bash
sudo ln -s /etc/nginx/sites-available/i2p-mirror /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```
#### Apache

Yeni bir site yapılandırması oluşturun:

```bash
sudo nano /etc/apache2/sites-available/i2p-mirror.conf
```
Bu yapılandırmayı yapıştırın:

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
Ardından portu ekleyin, siteyi etkinleştirin ve yeniden yükleyin:

```bash
echo "Listen 127.0.0.1:8080" | sudo tee -a /etc/apache2/ports.conf
sudo a2ensite i2p-mirror
sudo a2enmod headers
sudo a2dismod status info
sudo apachectl configtest
sudo systemctl reload apache2
```
#### Neden HSTS Yok?

Her iki yapılandırmanın da `Strict-Transport-Security` başlıklarından açıkça kaçındığını fark edeceksiniz. Bu kritik öneme sahiptir. HSTS tarayıcılara yalnızca HTTPS kullanmalarını söyler, ancak I2P geleneksel TLS kullanmaz — şifreleme bunun yerine ağ katmanında ele alınır. HSTS dahil etmek ziyaretçileri I2P sitenizden tamamen dışarıda bırakır.

### Adım 2: Sunucu Tunnel'ını Oluşturun

I2P Router Console'u tarayıcınızda açın:

```
`http://127.0.0.1:7657/i2ptunnel/`
```
Yeni bir tunnel oluşturmaya başlamak için **"Tunnel Wizard"**'a tıklayın.

![I2P Tunnel Wizard başlatma](/images/guides/mirroring/mirror_02.svg)

Tunnel türü olarak **"HTTP Server"** seçin ve **İleri**'ye tıklayın.

### Adım 3: Tunnel'ı Yapılandırın

Tunnel ayarlarını doldurun:

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
![Tunnel yapılandırma ayarları](/images/guides/mirroring/mirror_03.png)

Tunnel'ınızı oluşturmak için **"Create"** düğmesine tıklayın. I2P benzersiz bir kriptografik destination key oluşturacak — bu, ağdaki kalıcı adresiniz olur.

### Adım 4: Tunnel'ı Başlatın ve Bekleyin

Listede yeni tunnel'ınızı bulun ve **"Start"** butonuna tıklayın. Şunları göreceksiniz:

- **Yerel Hedef** — `abc123...xyz.b32.i2p` gibi uzun base32 adresi
- **Durum** — "Çalışıyor" olarak değişmeli

![Tunnel çalışma durumu](/images/guides/mirroring/mirror_04.png)

> **Sabırlı olun!** İlk başlatma, tunnel'ınız kurulup leaseSet'lerini ağa yayınlarken 2-5 dakika sürer. Bu normaldir.

### Adım 5: Mirror'unuzu Test Edin

Tunnel çalışır durumda göründükten sonra, I2P-yapılandırılmış tarayıcınızı açın ve base32 adresinizi ziyaret edin. İlk sayfa yüklemesi 5-30 saniye sürebilir — bu I2P için normaldir.

Sayfa yüklenirse, tebrikler — siteniz artık I2P'de yayında!

### Adım 6: İnsan Tarafından Okunabilir .i2p Adresi Kaydetme (İsteğe Bağlı)

Siteniz zaten base32 adresi üzerinden erişilebilir durumda, ancak `abc123...xyz.b32.i2p` pek akılda kalıcı değil. Temiz bir `.i2p` domaini almak için:

**Kendi adres defterin için** — `http://127.0.0.1:7657/dns` adresine git ve seçtiğin hostname'i destination anahtarınla eşleştirerek ekle.

**Genel keşif için** — I2P adres kayıt sistemine kayıt olun:

1. `http://stats.i2p/i2p/addkey.html` adresini ziyaret edin (I2P içinde)
2. İstediğiniz hostname'i ve tam destination key'inizi girin (tunnel detaylarınızdaki "AAAA" ile biten 500+ karakterlik string)
3. Kayıt için gönderin

Kayıt olduktan sonra, uygun adres defteri aboneliklerine sahip herkes sitenizi ismiyle bulabilecektir.

## Bölüm 2: Dinamik Uygulamaları Yansıtma

Siteniz statik dosyalar yerine bir backend framework (Node.js, Python, Ruby, PHP, vb.) üzerinde çalışıyorsa, I2P tunnel ile uygulamanız arasında reverse proxy olarak Nginx veya Apache'ye ihtiyacınız vardır.

### Ters Proxy Konfigürasyonu (Nginx)

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
`X-I2P-Request` başlığı, uygulamanızın farklı davranması gerektiğinde I2P trafiğini tespit etmesini sağlar (örneğin, clearnet erişimi gerektiren özellikleri devre dışı bırakma).

### Clearnet Aynalar için URL Yeniden Yazma

Uygulamanız clearnet etki alanınızı işaret eden URL'ler üretiyorsa, bunları I2P ziyaretçileri için yeniden yazmanız gerekir:

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
Ardından Bölüm 1'deki gibi `127.0.0.1:8080` adresine işaret eden bir HTTP Server tunnel'ı oluşturun.

## Bölüm 3: Git Depolarını Yansıtma

### Gitea (Tam Özellikli)

Gitea, Git'i I2P üzerinde barındırmak için harika bir seçimdir. Web arayüzü, sorun takibi ve pull request'ler içerir — bunların hepsi ağ üzerinde iyi çalışır.

`/etc/gitea/app.ini` dosyasını yapılandırın:

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
Önemli noktalar: `OFFLINE_MODE = true`, Gitea'nın harici kaynakları (avatarlar, CDN varlıkları) yüklemesini engeller. `COOKIE_SECURE = false` gereklidir çünkü I2P geleneksel anlamda HTTPS kullanmaz. E-postayı devre dışı bırakın çünkü I2P sunucunuzda giden e-posta yapılandırılmamış olabilir.

İki tunnel oluşturun: 1. **HTTP Server tunnel** → `127.0.0.1:3000` (web arayüzü) 2. **Standard Server tunnel** → `127.0.0.1:22` (git push/pull için SSH erişimi — isteğe bağlı)

### cgit (Hafif Alternatif)

Eğer sadece salt-okunur tarama ve HTTP klonlama ihtiyacınız varsa, cgit çok daha hafiftir:

```ini
# /etc/cgitrc
virtual-root=/
clone-url=`http://yourgit.i2p/$CGIT_REPO_URL`
cache-root=/var/cache/cgit
cache-size=1000
scan-path=/srv/git
enable-http-clone=1
```
cgit'in agresif önbellekleme özelliği, I2P'nin yüksek gecikme süresi için özellikle uygun hale getirir.

### I2P Üzerinden Git için İstemci Tarafı Kurulumu

I2P Git aynasından klonlama yapan herkesin Git trafiğini I2P HTTP proxy üzerinden yönlendirmesi gerekir:

```bash
# Tell Git to use the I2P proxy for .i2p domains
git config --global http.http://yourgit.i2p.proxy `http://127.0.0.1:4444`
git config --global http.timeout 300

# Clone (allow for I2P latency)
GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=60 \
    git clone `http://yourgit.i2p/repo`
```
Büyük depolar için, sığ klonlar I2P üzerinden çok fazla zaman tasarrufu sağlar:

```bash
git clone --depth 1 `http://yourgit.i2p/project`
git fetch --unshallow   # grab full history later if needed
```
## Bölüm 4: Dosya Barındırma Yansıtması

### Nextcloud

Nextcloud, bazı yapılandırmalarla I2P üzerinde çalışır. `config/config.php` dosyasını düzenleyin:

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
İyi çalışanlar: dosya yükleme ve indirme, dizin tarama, kimlik doğrulama, genel bağlantı paylaşımı ve WebDAV. Çalışmayanlar: masaüstü senkronizasyon istemcileri SOCKS proxy yapılandırmasına ihtiyaç duyar, harici depolama arka uçları IP adreslerini sızdırabilir ve clearnet Nextcloud örnekleri ile federasyon gizliliği tehlikeye atabilir.

### Basit Dosya Sunucusu

Nextcloud'un getirdiği ek yük olmadan basit dosya barındırma için, minimal bir Python sunucusu işinizi görür:

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
`127.0.0.1:8080` adresine işaret eden bir HTTP Server tunnel'ı oluşturun.

## Bölüm 5: Yansılama API'leri

### Temel API Proxy

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
### WebSocket Desteği

Uygulamanız WebSockets kullanıyorsa (sohbet uygulamaları, canlı kontrol panelleri vb.):

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
I2P üzerindeki WebSocket'lerin clearnet'e göre belirgin şekilde daha yüksek gecikme süresine sahip olacağını unutmayın. Gerçek zamanlı özellikler için, istemci tarafında daha uzun yoklama aralıkları veya iyimser UI güncellemeleri düşünün.

## Güvenlik En İyi Uygulamaları

Mirror'ınızı çalıştırmak kolay kısım. Güvenli tutmak ise I2P hosting'e özgü birkaç detaya dikkat etmeyi gerektirir.

![I2P ayna sunucuları için güvenlik kontrol listesi](/images/guides/mirroring/security-checklist.svg)

### Büyük Kurallar

**Yalnızca localhost'a bağlanın.** Hizmetiniz `127.0.0.1` üzerinde dinlemeli, asla `0.0.0.0` üzerinde değil. I2P router'ının hizmetinize ulaşabilmesi gereken tek şey olmalıdır.

**Tanımlayıcı başlıkları kaldır.** Web sunucuları hangi yazılımı çalıştırdıklarını duyurmayı severler. I2P üzerinden, bu paylaşmak istemeyeceğiniz bir bilgidir.

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
**Her şeyi kendi sunucunuzda barındırın.** Google'dan fontlar, CDN'lerden betikler veya üçüncü taraflardan analitik araçları yüklemeyin. Her harici kaynak I2P ağından çıkan bir istek olup büyük gecikme ekler ve potansiyel olarak bilgi sızıntısına neden olur. Kütüphaneleri ve fontları indirin, sunucunuza koyun ve yerel olarak sunun.

**Veritabanlarını asla dışarı açmayın.** Söylemeye gerek olmamalı, ancak veritabanı portlarınıza I2P tunnel'ları oluşturmayın. Server tunnel'ları yalnızca web sunucularına veya uygulama sunucularına işaret etmelidir.

## Performans Optimizasyonu

I2P her istek için 2-10 saniye gecikme ekler. Bu, çoklu atlama şifrelemesinin bedeli. Ancak uygun ayarlamalarla, I2P yansınız şaşırtıcı derecede hızlı hissedebilir.

### Agresif Önbellekleme

Statik varlıklar uzun önbellek yaşam sürelerine sahip olmalıdır. Bir ziyaretçi CSS ve resimlerinizi zaten yüklediyse, bunları tekrar beklemek zorunda kalmamalıdır:

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```
### Sıkıştırmayı Etkinleştir

Daha küçük veri yükleri, I2P'nin sınırlı bant genişliği üzerinden daha hızlı aktarım anlamına gelir:

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript
           text/xml application/xml application/xml+rss;
```
### Trafik İçin Tunnel Miktarını Ayarlama

Daha fazla tunnel daha fazla eşzamanlı bağlantı anlamına gelir. Varsayılan 3 değeri düşük trafikli siteler için yeterlidir, ancak tıkanıklık yaşıyorsanız:

```properties
tunnel.0.option.inbound.quantity=5
tunnel.0.option.outbound.quantity=5
tunnel.0.option.inbound.backupQuantity=2
tunnel.0.option.outbound.backupQuantity=2
```
### Tunnel Uzunluğu (Atlama)

Her atlama gecikme ekler ancak aynı zamanda anonimlik de ekler. Tehdit modelinize göre seçim yapın:

![Tunnel atlaması dengesi — daha fazla atlama daha fazla gizlilik demektir ancak daha yüksek gecikme ile sonuçlanır](/images/guides/mirroring/tunnel-hops.svg)

Sunucunun kimliğinin zaten bilindiği halka açık bir mirror için (örneğin, kuruluşunuzun web sitesi), 2 hop'a düşürmek makul bir takas olacaktır:

```properties
tunnel.0.option.inbound.length=2
tunnel.0.option.outbound.length=2
```
### Genel Router İpuçları

- I2P router'ınızı **7/24** çalıştırın. Ne kadar uzun süre açık kalırsa, ağ ile o kadar iyi entegre olur ve tunnel'larınız o kadar hızlı performans gösterir.
- Bant genişliği paylaşımını en az **256 KB/sn** olarak ayarlayın, ancak gerçek hat hızınızdan biraz düşük tutun.
- Yeniden başlatma sonrası ilk bağlantıların yavaş olmasını bekleyin (30-90 saniye). Tunnel'lar kuruldukça bu hızla iyileşir.

## Gelişmiş: Manuel Tunnel Yapılandırması

Router Console sihirbazı harika çalışır, ancak yapılandırma dosyalarını doğrudan düzenlemeyi tercih ediyorsanız — veya dağıtımları otomatikleştirmeniz gerekiyorsa — tunnel'ları `~/.i2p/i2ptunnel.config` dosyasında (veya sistem kurulumları için `/var/lib/i2p/i2p-config/i2ptunnel.config`) yapılandırabilirsiniz:

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
Değişikliklerden sonra I2P'yi yeniden başlatın:

```bash
sudo systemctl restart i2p
```
I2P 0.9.42 sürümünden itibaren, birden fazla tunnel'ın daha temiz yönetimi için `i2ptunnel.config.d/` içinde bireysel yapılandırma dosyaları da kullanabilirsiniz:

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
## Sorun Giderme

### "Siteme erişemiyorum"

Bu kontrol listesini sırasıyla çalışın:

**1. Web sunucusu gerçekten dinliyor mu?**

```bash
nc -zv 127.0.0.1 8080
```
Bu başarısız olursa, web sunucusu yapılandırmanızda bir sorun var — 1. Adım'a geri dönün.

**2. Tunnel çalışıyor mu?** `http://127.0.0.1:7657/i2ptunnel/` adresini ziyaret edin ve durumu kontrol edin. 5 dakikadan fazla "Starting" yazıyorsa, router'ınızın ağ entegrasyonunu kontrol edin.

**3. LeaseSet yayınlandı mı?** Tunnel seçeneklerinizde `i2cp.dontPublishLeaseSet` ayarının belirlenmediğinden emin olun. Yayınlanmış bir LeaseSet olmadan, kimse tunnel'ınızı bulamaz.

**4. Saatiniz doğru mu?** I2P, 60 saniye içinde zaman doğruluğu gerektirir. Şununla kontrol edin:

```bash
timedatectl status
```
Saatiniz yanlışsa, I2P tunnel oluştururken sorun yaşar.

### Yeniden başlatma sonrası yavaş performans

Bu normaldir. I2P router'ınızı yeniden başlattıktan sonra, tunnel havuzlarını yeniden oluşturması ve ağa yeniden entegre olması için 10-15 dakika bekleyin. Daha fazla eş router'ınız hakkında bilgi edindiğinde performans iyileşir.

Ayrıca I2NP portunuz için port yönlendirmesinin yapılandırıldığından emin olun (belirli port numarası için Router Console'u kontrol edin). Port yönlendirme olmadan, router'ınız performansı sınırlayan "firewalled" modunda çalışır.

### Başkaları ziyaret ettiğinde "Adres bulunamadı" hataları

Ziyaretçilerin adres defterlerinde sizin adresinizin bulunması gerekir. Halka açık bir adres defterine kayıt yaptırdığınızdan emin olun veya tam base32 adresinizi doğrudan paylaşın. Ayrıca `http://127.0.0.1:7657/susidns/subscriptions` adresinden daha fazla abonelik ekleyebilirler:

```
`http://stats.i2p/cgi-bin/newhosts.txt`
`http://i2host.i2p/cgi-bin/i2hostetag`
```
### Test sırasında zaman aşımları

I2P doğası gereği daha yüksek gidiş-dönüş sürelerine sahiptir. Komut satırından test ederken, uzatılmış zaman aşımı sürelerini kullanın:

```bash
# curl
curl --connect-timeout 60 --max-time 300 `http://yoursite.i2p/`

# wget
wget --timeout=300 `http://yoursite.i2p/`
```
### Logları okuma

Başka hiçbir şey yardım etmezse, I2P router günlüklerini hata mesajları için kontrol edin:

```bash
# System service
sudo journalctl -u i2p -f

# Or directly
tail -f ~/.i2p/logs/log-router-0.txt
```
## Anahtarlarınızı Yedekleyin

Bu kesinlikle atlamamanız gereken tek şeydir. Tunnel'ınızın özel anahtar dosyaları (I2P yapılandırma dizininizdeki `.dat` dosyaları), hizmetinize ağ üzerinde kalıcı adresini veren şeydir. Bunları kaybederseniz, I2P adresinizi kalıcı olarak kaybedersiniz. Kurtarma, sıfırlama veya destek talebi yoktur. Yeni bir adresle baştan başlamanız gerekir.

Şimdi yedekleyin:

```bash
# User installation
tar -czf tunnel-keys-backup.tar.gz ~/.i2p/*.dat

# System installation
sudo tar -czf tunnel-keys-backup.tar.gz /var/lib/i2p/i2p-config/*.dat
```
Yedeği güvenli bir yerde ve sunucu dışında saklayın.

## İşiniz Bitti

Bu kadar. Hizmetiniz artık hem normal internet hem de I2P network üzerinde kullanılabilir. İnsanlara içeriğinize erişmek için özel bir yol sunuyorsunuz — kimliklerinin kendilerine ait kaldığı bir yol.

Sorunlarla karşılaşırsanız veya daha fazla dahil olmak istiyorsanız, topluluğu burada bulabilirsiniz:

- **Forum:** [i2pforum.net](https://i2pforum.net)
- **IRC:** çeşitli ağlarda #i2p
- **Geliştirme:** [i2pgit.org](https://i2pgit.org)
- **StormyCloud:** [stormycloud.org](https://www.stormycloud.org)

---

*Bu rehber [StormyCloud Inc](https://www.stormycloud.org) tarafından I2P topluluğu için hazırlanmıştır.*
