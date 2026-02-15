---
title: "I2P पर अपनी सेवाओं को मिरर करना"
description: "I2P network पर अपनी websites, Git repos, APIs, और अन्य चीजों को उपलब्ध कराने के लिए एक शुरुआती-अनुकूल गाइड — चरणबद्ध निर्देशों और diagrams के साथ"
slug: "mirroring-guide"
lastUpdated: "2025-02"
accurateFor: "2.10.0"
---

आपके पास नियमित इंटरनेट पर एक वेबसाइट है। अब आप इसे I2P पर भी उपलब्ध कराना चाहते हैं — ताकि लोग इसे निजी रूप से देख सकें, बिना यह बताए कि वे कौन हैं या कहाँ से आ रहे हैं। यह गाइड इसी के बारे में है।

मिररिंग आपकी मौजूदा साइट को बदलता नहीं है। यह एक दूसरा प्रवेश द्वार जोड़ता है — एक निजी — I2P नेटवर्क के माध्यम से। आपकी clearnet साइट पहले की तरह ही चलती रहती है।

![I2P mirroring कैसे काम करता है — आपके सर्वर को I2P network के माध्यम से एक दूसरा, निजी प्रवेश द्वार मिलता है](/images/guides/mirroring/how-mirroring-works.svg)

## I2P पर मिरर क्यों करें?

आपकी सेवाओं को मिरर करने के कई व्यावहारिक कारण हैं:

**आपके आगंतुकों के लिए गोपनीयता।** लोग अपना IP पता उजागर किए बिना आपकी सामग्री तक पहुँच सकते हैं। उनके और आपकी सेवा के बीच ट्रैफिक कई hops के माध्यम से एन्क्रिप्ट होता है — न तो आप और न ही नेटवर्क को देखने वाला कोई भी व्यक्ति यह पहचान सकता है कि कौन विज़िट कर रहा है।

**सेंसरशिप प्रतिरोध।** यदि आपकी साइट कुछ क्षेत्रों में DNS फ़िल्टरिंग, IP ब्लॉकिंग, या अन्य माध्यमों से अवरुद्ध है, तो I2P मिरर पहुंच योग्य रहता है। यह DNS या पारंपरिक IP रूटिंग पर निर्भर नहीं है।

**लचीलापन।** एक I2P mirror अतिरिक्त सुरक्षा जोड़ता है। यदि आपका डोमेन जब्त हो जाता है या आपका CDN आपको छोड़ देता है, तो I2P संस्करण तब तक चलता रहता है जब तक आपका सर्वर चल रहा है।

**नेटवर्क का समर्थन करना।** I2P पर प्रत्येक सेवा नेटवर्क को अधिक उपयोगी बनाती है और पारिस्थितिकी तंत्र को बढ़ाने में मदद करती है।

## आपको क्या चाहिए होगा

शुरू करने से पहले, सुनिश्चित करें कि आपके पास है:

- **आपके सर्वर पर एक चालू I2P router** (Java implementation)। यदि आपके पास अभी तक नहीं है, तो पहले [I2P Installation Guide](/downloads/) का पालन करें।
- **आपकी वेबसाइट या सेवा पहले से कार्य कर रही हो** — यह आपके सर्वर पर सामग्री परोस रही होनी चाहिए।
- **बुनियादी command-line की जानकारी** — आप एक config file संपादित करेंगे और कुछ commands चलाएंगे।
- **लगभग 15–20 मिनट** — बस इतना ही समय लगता है।

आपके I2P router को कम से कम 512 MB RAM की आवश्यकता होती है और यह 24/7 अपटाइम वाले सर्वर पर सबसे अच्छा काम करता है। यदि आपका router पहली बार शुरू हुआ है, तो tunnel बनाने से पहले इसे नेटवर्क के साथ एकीकृत होने के लिए 10-15 मिनट का समय दें।

## Tunnels को समझना

I2P mirroring के पीछे मुख्य अवधारणा **server tunnel** है। यहाँ विचार है:

जब I2P पर कोई व्यक्ति आपकी साइट पर जाना चाहता है, तो उनका अनुरोध I2P network में कई encrypted hops के माध्यम से यात्रा करता है जब तक कि यह आपके I2P router तक नहीं पहुंच जाता। आपका router फिर अनुरोध को एक **server tunnel** को सौंपता है, जो इसे localhost पर चल रहे आपके web server को forward कर देता है। आपका web server जवाब देता है, और उत्तर encrypted network के माध्यम से वापसी का रास्ता लेता है।

इन अनुरोधों के लिए आपका वेब सर्वर कभी भी सार्वजनिक इंटरनेट को स्पर्श नहीं करता — यह केवल localhost से बात करता है। I2P router सभी network-facing चीजों को संभालता है।

### आपको किस प्रकार के Tunnel की आवश्यकता है?

I2P विभिन्न स्थितियों के लिए कई tunnel प्रकार प्रदान करता है:

![Tunnel प्रकारों की तुलना — HTTP Server अधिकांश वेबसाइटों के लिए सही विकल्प है](/images/guides/mirroring/tunnel-types.svg)

वेबसाइट को मिरर करने के लिए, आप निश्चित रूप से एक **HTTP Server** tunnel चाहते हैं। यह विशेष रूप से वेब ट्रैफ़िक के लिए डिज़ाइन किया गया है और header filtering, compression, और hostname spoofing को तुरंत संभालता है। अन्य प्रकार विशेष उपयोग के मामलों के लिए मौजूद हैं जैसे SSH access, bidirectional applications, या IRC servers।

## भाग 1: एक वेबसाइट को मिरर करना

यह सबसे सामान्य स्थिति है — आपके पास पहले से एक clearnet वेबसाइट है और आप इसे I2P पर उपलब्ध कराना चाहते हैं। यहाँ इस प्रक्रिया का संक्षिप्त विवरण है:

![I2P पर अपनी साइट को मिरर करने के पांच चरण](/images/guides/mirroring/steps-overview.svg)

आइए प्रत्येक चरण को समझते हैं।

### चरण 1: अपने वेब सर्वर में एक Localhost Listener जोड़ें

आपकी clearnet साइट संभवतः पहले से ही पोर्ट 80 और 443 पर चल रही है, जो दुनिया के लिए खुली है। I2P के लिए, आप localhost पर एक *अलग* listener बनाएंगे जिसे केवल I2P tunnel ही पहुंच सकता है। यह आपको I2P संस्करण के दिखने के तरीके पर पूरा नियंत्रण देता है — आप headers को हटा सकते हैं, admin panels को ब्लॉक कर सकते हैं, और I2P की उच्च latency के लिए caching को ट्यून कर सकते हैं।

> **त्वरित विकल्प:** यदि आपको किसी अनुकूलन की आवश्यकता नहीं है, तो आप इस चरण को छोड़ सकते हैं और I2P tunnel को सीधे `127.0.0.1:80` पर निर्देशित कर सकते हैं। लेकिन समर्पित listener दृष्टिकोण की सिफारिश की जाती है।

अपना वेब सर्वर चुनें:

#### Nginx

एक नया साइट कॉन्फ़िग बनाएं:

```bash
sudo nano /etc/nginx/sites-available/i2p-mirror
```
इस कॉन्फ़िगरेशन को पेस्ट करें, `yoursite.i2p` और root path को अपनी वैल्यू से बदलें:

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
इसे सक्षम करें और पुनः लोड करें:

```bash
sudo ln -s /etc/nginx/sites-available/i2p-mirror /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```
#### Apache

एक नई साइट कॉन्फ़िग बनाएं:

```bash
sudo nano /etc/apache2/sites-available/i2p-mirror.conf
```
इस कॉन्फ़िगरेशन को पेस्ट करें:

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
फिर port जोड़ें, site को enable करें, और reload करें:

```bash
echo "Listen 127.0.0.1:8080" | sudo tee -a /etc/apache2/ports.conf
sudo a2ensite i2p-mirror
sudo a2enmod headers
sudo a2dismod status info
sudo apachectl configtest
sudo systemctl reload apache2
```
#### HSTS क्यों नहीं?

आप देखेंगे कि दोनों configs स्पष्ट रूप से `Strict-Transport-Security` headers से बचते हैं। यह महत्वपूर्ण है। HSTS browsers को केवल HTTPS उपयोग करने के लिए कहता है, लेकिन I2P पारंपरिक TLS का उपयोग नहीं करता — encryption को network layer पर handle किया जाता है। HSTS को शामिल करने से visitors आपकी I2P site से पूरी तरह बाहर हो जाएंगे।

### चरण 2: सर्वर टनल बनाएं

अपने browser में I2P Router Console खोलें:

```
`http://127.0.0.1:7657/i2ptunnel/`
```
नई tunnel बनाना शुरू करने के लिए **"Tunnel Wizard"** पर क्लिक करें।

![I2P Tunnel Wizard स्टार्टअप](/images/guides/mirroring/mirror_02.svg)

tunnel प्रकार के रूप में **"HTTP Server"** चुनें और **Next** पर क्लिक करें।

### चरण 3: Tunnel को कॉन्फ़िगर करें

tunnel सेटिंग्स भरें:

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
![Tunnel configuration settings](/images/guides/mirroring/mirror_03.png)

अपनी tunnel बनाने के लिए **"Create"** पर क्लिक करें। I2P एक अद्वितीय cryptographic destination key बनाएगा — यह नेटवर्क पर आपका स्थायी पता बन जाता है।

### चरण 4: Tunnel शुरू करें और प्रतीक्षा करें

अपनी नई tunnel को सूची में खोजें और **"Start"** पर क्लिक करें। आप देखेंगे:

- **Local Destination** — एक लंबा base32 पता जैसे `abc123...xyz.b32.i2p`
- **Status** — "Running" में बदल जाना चाहिए

![Tunnel running status](/images/guides/mirroring/mirror_04.png)

> **धैर्य रखें!** पहली बार शुरुआत में 2-5 मिनट लगते हैं जबकि आपकी tunnel बनती है और अपने leaseset को नेटवर्क पर प्रकाशित करती है। यह सामान्य है।

### चरण 5: अपने मिरर का परीक्षण करें

जब tunnel चालू दिखाई दे, तो अपना I2P-configured ब्राउज़र खोलें और अपने base32 address पर जाएं। पहली बार पेज लोड होने में 5–30 सेकंड लग सकते हैं — यह I2P के लिए सामान्य है।

यदि पेज लोड हो जाता है, बधाई हो — आपकी साइट अब I2P पर लाइव है!

### चरण 6: एक मानव-पठनीय .i2p पता पंजीकृत करें (वैकल्पिक)

आपकी साइट पहले से ही base32 एड्रेस के माध्यम से पहुंच योग्य है, लेकिन `abc123...xyz.b32.i2p` बिल्कुल यादगार नहीं है। एक साफ `.i2p` डोमेन प्राप्त करने के लिए:

**अपनी स्वयं की addressbook के लिए** — `http://127.0.0.1:7657/dns` पर जाएं और अपनी चुनी गई hostname को अपनी destination key के साथ mapped करके जोड़ें।

**सार्वजनिक खोज के लिए** — I2P पता रजिस्ट्री के साथ पंजीकरण करें:

1. `http://stats.i2p/i2p/addkey.html` पर जाएं (I2P के अंदर)
2. अपना वांछित hostname और अपनी पूर्ण destination key दर्ज करें (आपकी tunnel विवरण से 500+ अक्षरों की स्ट्रिंग, जो "AAAA" पर समाप्त होती है)
3. पंजीकरण के लिए सबमिट करें

एक बार पंजीकृत हो जाने पर, उपयुक्त address book subscriptions वाले कोई भी व्यक्ति आपकी साइट को नाम से खोज सकेंगे।

## भाग 2: गतिशील अनुप्रयोगों की मिररिंग

यदि आपकी साइट static files के बजाय backend framework (Node.js, Python, Ruby, PHP, आदि) पर चलती है, तो आपको I2P tunnel और आपकी application के बीच Nginx या Apache को reverse proxy के रूप में उपयोग करने की आवश्यकता होगी।

### रिवर्स प्रॉक्सी कॉन्फ़िगरेशन (Nginx)

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
`X-I2P-Request` हेडर आपकी एप्लिकेशन को I2P ट्रैफिक का पता लगाने की सुविधा देता है यदि इसे अलग तरीके से व्यवहार करना हो (उदाहरण के लिए, उन सुविधाओं को अक्षम करना जिनके लिए clearnet एक्सेस की आवश्यकता होती है)।

### Clearnet Mirrors के लिए URL Rewriting

यदि आपका एप्लिकेशन आपके clearnet डोमेन की ओर इशारा करने वाले URLs उत्पन्न करता है, तो आप I2P विज़िटर्स के लिए उन्हें फिर से लिखना चाहेंगे:

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
फिर एक HTTP Server tunnel बनाएं जो `127.0.0.1:8080` को point करे, बिल्कुल Part 1 की तरह।

## भाग 3: Git रिपॉजिटरी को मिरर करना

### Gitea (पूर्ण-सुविधा युक्त)

Gitea, I2P पर Git होस्ट करने के लिए एक बेहतरीन विकल्प है। इसमें एक वेब इंटरफ़ेस, issue tracking, और pull requests हैं — ये सभी नेटवर्क पर अच्छी तरह से काम करते हैं।

`/etc/gitea/app.ini` को कॉन्फ़िगर करें:

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
मुख्य बिंदु: `OFFLINE_MODE = true` Gitea को बाहरी संसाधन (अवतार, CDN एसेट्स) लोड करने से रोकता है। `COOKIE_SECURE = false` की आवश्यकता है क्योंकि I2P पारंपरिक अर्थों में HTTPS का उपयोग नहीं करता। ईमेल को अक्षम करें क्योंकि हो सकता है आपके I2P सर्वर में आउटबाउंड ईमेल कॉन्फ़िगर न हो।

दो tunnel बनाएं: 1. **HTTP Server tunnel** → `127.0.0.1:3000` (web interface) 2. **Standard Server tunnel** → `127.0.0.1:22` (SSH access git push/pull के लिए — वैकल्पिक)

### cgit (हल्का विकल्प)

यदि आपको केवल read-only browsing और HTTP cloning की आवश्यकता है, तो cgit बहुत हल्का है:

```ini
# /etc/cgitrc
virtual-root=/
clone-url=`http://yourgit.i2p/$CGIT_REPO_URL`
cache-root=/var/cache/cgit
cache-size=1000
scan-path=/srv/git
enable-http-clone=1
```
cgit की आक्रामक caching इसे I2P की उच्च latency के लिए विशेष रूप से उपयुक्त बनाती है।

### I2P पर Git के लिए क्लाइंट-साइड सेटअप

आपके I2P Git mirror से clone करने वाले किसी भी व्यक्ति को Git traffic को I2P HTTP proxy के माध्यम से route करना होगा:

```bash
# Tell Git to use the I2P proxy for .i2p domains
git config --global http.http://yourgit.i2p.proxy `http://127.0.0.1:4444`
git config --global http.timeout 300

# Clone (allow for I2P latency)
GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=60 \
    git clone `http://yourgit.i2p/repo`
```
बड़े repositories के लिए, shallow clones I2P पर काफी समय बचाते हैं:

```bash
git clone --depth 1 `http://yourgit.i2p/project`
git fetch --unshallow   # grab full history later if needed
```
## भाग 4: फ़ाइल होस्टिंग की मिररिंग

### Nextcloud

Nextcloud कुछ कॉन्फ़िगरेशन के साथ I2P पर काम करता है। `config/config.php` को संपादित करें:

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
क्या अच्छी तरह काम करता है: फ़ाइल अपलोड और डाउनलोड, डायरेक्टरी ब्राउज़िंग, प्रमाणीकरण, सार्वजनिक लिंक साझाकरण, और WebDAV। क्या नहीं करता: डेस्कटॉप sync clients को SOCKS proxy कॉन्फ़िगरेशन की आवश्यकता होती है, external storage backends IP addresses लीक कर सकते हैं, और clearnet Nextcloud instances के साथ federation गोपनीयता से समझौता कर सकता है।

### सरल फ़ाइल सर्वर

Nextcloud के overhead के बिना सीधी file hosting के लिए, एक minimal Python server काम आ जाता है:

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
`127.0.0.1:8080` की ओर इशारा करते हुए एक HTTP Server tunnel बनाएं।

## भाग 5: मिररिंग APIs

### बेसिक API प्रॉक्सी

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
### WebSocket समर्थन

यदि आपका एप्लिकेशन WebSockets का उपयोग करता है (चैट ऐप्स, लाइव डैशबोर्ड, आदि):

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
ध्यान दें कि I2P पर WebSockets में clearnet की तुलना में काफी अधिक latency होगी। real-time सुविधाओं के लिए, लंबे polling intervals या client side पर optimistic UI updates पर विचार करें।

## सुरक्षा सर्वोत्तम प्रथाएं

अपना mirror काम करवाना आसान हिस्सा है। इसे सुरक्षित रखने के लिए कुछ विवरणों पर ध्यान देना आवश्यक है जो I2P hosting के लिए विशिष्ट हैं।

![I2P mirrors के लिए सुरक्षा चेकलिस्ट](/images/guides/mirroring/security-checklist.svg)

### मुख्य नियम

**केवल localhost से bind करें।** आपकी सेवा को `127.0.0.1` पर सुनना चाहिए, कभी भी `0.0.0.0` पर नहीं। I2P router ही एकमात्र चीज़ होनी चाहिए जो आपकी सेवा तक पहुंच सके।

**पहचान करने वाले headers को हटाएं।** वेब सर्वर अपने चलने वाले सॉफ़्टवेयर की घोषणा करना पसंद करते हैं। I2P पर, यह ऐसी जानकारी है जिसे आप साझा नहीं करना चाहते।

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
**सब कुछ स्वयं होस्ट करें।** Google से फ़ॉन्ट, CDN से स्क्रिप्ट, या तृतीय पक्षों से analytics लोड न करें। हर बाहरी संसाधन एक अनुरोध है जो I2P नेटवर्क से बाहर निकलता है, जिससे बहुत अधिक विलंबता जुड़ती है और संभावित रूप से जानकारी लीक हो सकती है। लाइब्रेरी और फ़ॉन्ट डाउनलोड करें, उन्हें अपने सर्वर पर रखें, और उन्हें स्थानीय रूप से सर्व करें।

**कभी भी डेटाबेस को एक्सपोज़ न करें।** यह कहने की जरूरत नहीं होनी चाहिए, लेकिन अपने डेटाबेस पोर्ट्स के लिए I2P tunnels न बनाएं। Server tunnels केवल वेब सर्वर या एप्लिकेशन सर्वर को ही पॉइंट करना चाहिए।

## प्रदर्शन ट्यूनिंग

I2P प्रत्येक request में 2-10 सेकंड की latency जोड़ता है। यह multi-hop encryption की कीमत है। लेकिन उचित tuning के साथ, आपका I2P mirror आश्चर्यजनक रूप से तेज़ महसूस हो सकता है।

### आक्रामक रूप से Cache करें

Static assets का लंबा cache lifetime होना चाहिए। यदि किसी visitor ने आपके CSS और images को पहले से लोड कर लिया है, तो उन्हें दोबारा इनका इंतज़ार नहीं करना चाहिए:

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```
### कम्प्रेशन सक्षम करें

छोटे payloads का मतलब है I2P की सीमित bandwidth पर तेज transfers:

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript
           text/xml application/xml application/xml+rss;
```
### ट्रैफिक के लिए tunnel की मात्रा को समायोजित करें

अधिक tunnels का मतलब है अधिक समवर्ती कनेक्शन। कम-ट्रैफिक साइटों के लिए 3 का डिफ़ॉल्ट ठीक है, लेकिन यदि आप भीड़भाड़ देख रहे हैं:

```properties
tunnel.0.option.inbound.quantity=5
tunnel.0.option.outbound.quantity=5
tunnel.0.option.inbound.backupQuantity=2
tunnel.0.option.outbound.backupQuantity=2
```
### Tunnel की लंबाई (Hops)

प्रत्येक hop विलंबता (latency) जोड़ता है लेकिन गुमनामी भी बढ़ाता है। अपने खतरा मॉडल के आधार पर चुनें:

![Tunnel hops trade-off — अधिक hops का मतलब अधिक गोपनीयता लेकिन उच्च विलंबता है](/images/guides/mirroring/tunnel-hops.svg)

एक पब्लिक मिरर के लिए जहाँ सर्वर की पहचान पहले से ज्ञात है (उदाहरण के लिए, आपके संगठन की वेबसाइट), 2 hops तक कम करना एक उचित trade-off है:

```properties
tunnel.0.option.inbound.length=2
tunnel.0.option.outbound.length=2
```
### सामान्य Router सुझाव

- अपना I2P router **24/7** चलाएं। जितनी देर यह चालू रहता है, उतना बेहतर यह network के साथ एकीकृत होता है, और उतनी तेज़ी से आपकी tunnels काम करती हैं।
- bandwidth share कम से कम **256 KB/sec** सेट करें, लेकिन इसे अपनी वास्तविक line speed से थोड़ा कम रखें।
- restart के बाद पहले connections धीमे होने की अपेक्षा करें (30–90 सेकंड)। tunnels build होने के साथ यह जल्दी सुधर जाता है।

## उन्नत: मैनुअल tunnel कॉन्फ़िगरेशन

Router Console wizard बहुत अच्छा काम करता है, लेकिन यदि आप config फ़ाइलों को सीधे संपादित करना पसंद करते हैं — या deployments को automate करने की आवश्यकता है — तो आप `~/.i2p/i2ptunnel.config` में tunnels को configure कर सकते हैं (या system installs के लिए `/var/lib/i2p/i2p-config/i2ptunnel.config`):

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
परिवर्तनों के बाद I2P को पुनः आरंभ करें:

```bash
sudo systemctl restart i2p
```
I2P 0.9.42 के बाद से, आप कई tunnels के साफ प्रबंधन के लिए `i2ptunnel.config.d/` में व्यक्तिगत config फाइलों का भी उपयोग कर सकते हैं:

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
## समस्या निवारण

### "मैं अपनी साइट तक नहीं पहुंच सकता"

इस चेकलिस्ट को क्रमानुसार पूरा करें:

**1. क्या वेब सर्वर वास्तव में सुन रहा है?**

```bash
nc -zv 127.0.0.1 8080
```
यदि यह असफल हो जाता है, तो आपके web server config में कोई समस्या है — वापस Step 1 पर जाएं।

**2. क्या tunnel चल रहा है?** `http://127.0.0.1:7657/i2ptunnel/` पर जाएं और स्थिति की जांच करें। यदि यह 5 मिनट से अधिक समय तक "Starting" दिखाता है, तो अपने router के नेटवर्क integration की जांच करें।

**3. क्या LeaseSet प्रकाशित है?** सुनिश्चित करें कि आपके tunnel विकल्पों में `i2cp.dontPublishLeaseSet` सेट नहीं है। प्रकाशित LeaseSet के बिना, कोई भी आपका tunnel नहीं खोज सकता।

**4. क्या आपकी घड़ी सटीक है?** I2P को 60 सेकंड के भीतर समय की सटीकता की आवश्यकता होती है। इसे जांचें:

```bash
timedatectl status
```
यदि आपकी घड़ी गलत है, तो I2P को tunnels बनाने में परेशानी होगी।

### पुनः आरंभ के बाद धीमी कार्यप्रदर्शन

यह सामान्य है। अपने I2P router को restart करने के बाद, इसे अपने tunnel pools को rebuild करने और network के साथ फिर से integrate होने के लिए 10–15 मिनट का समय दें। जैसे-जैसे अधिक peers आपके router के बारे में जानते हैं, performance में सुधार होता है।

यह भी जांचें कि आपके I2NP port के लिए port forwarding कॉन्फ़िगर किया गया है (विशिष्ट port नंबर के लिए Router Console देखें)। इसके बिना, आपका router "firewalled" मोड में काम करता है, जो प्रदर्शन को सीमित करता है।

### दूसरों के द्वारा विज़िट करने पर "Address not found" त्रुटियां

आगंतुकों को अपनी address book में आपके पते की आवश्यकता होती है। सुनिश्चित करें कि आपने किसी सार्वजनिक address book के साथ पंजीकरण कराया है, या अपना पूरा base32 पता सीधे साझा करें। वे `http://127.0.0.1:7657/susidns/subscriptions` पर और भी subscriptions जोड़ सकते हैं:

```
`http://stats.i2p/cgi-bin/newhosts.txt`
`http://i2host.i2p/cgi-bin/i2hostetag`
```
### टेस्टिंग के दौरान टाइमआउट

I2P में स्वाभाविक रूप से अधिक round-trip समय होता है। command line से परीक्षण करते समय, विस्तारित timeouts का उपयोग करें:

```bash
# curl
curl --connect-timeout 60 --max-time 300 `http://yoursite.i2p/`

# wget
wget --timeout=300 `http://yoursite.i2p/`
```
### लॉग्स पढ़ना

यदि कुछ और मदद नहीं करता, तो त्रुटियों के लिए I2P router लॉग्स की जांच करें:

```bash
# System service
sudo journalctl -u i2p -f

# Or directly
tail -f ~/.i2p/logs/log-router-0.txt
```
## अपनी Keys का बैकअप लें

यह एक ऐसी चीज़ है जिसे आपको बिल्कुल भी छोड़ना नहीं चाहिए। आपकी tunnel की private key files (आपकी I2P config directory में `.dat` files) ही वे हैं जो आपकी service को network पर स्थायी पता प्रदान करती हैं। यदि आप इन्हें खो देते हैं, तो आप अपना I2P address खो देते हैं — स्थायी रूप से। कोई recovery नहीं, कोई reset नहीं, कोई support ticket नहीं। आपको नए address के साथ फिर से शुरुआत करनी होगी।

उन्हें अभी बैकअप करें:

```bash
# User installation
tar -czf tunnel-keys-backup.tar.gz ~/.i2p/*.dat

# System installation
sudo tar -czf tunnel-keys-backup.tar.gz /var/lib/i2p/i2p-config/*.dat
```
बैकअप को कहीं सुरक्षित स्थान पर और सर्वर के बाहर स्टोर करें।

## आपका काम हो गया

बस यही है। आपकी सेवा अब नियमित इंटरनेट और I2P network दोनों पर उपलब्ध है। आप लोगों को अपनी सामग्री तक पहुंचने का एक निजी तरीका दे रहे हैं — जहां उनकी पहचान उनकी अपनी बनी रहती है।

यदि आपको कोई समस्या आती है या आप और अधिक शामिल होना चाहते हैं, तो यहाँ आप समुदाय को पा सकते हैं:

- **फोरम:** [i2pforum.net](https://i2pforum.net)
- **IRC:** विभिन्न नेटवर्क पर #i2p
- **डेवलपमेंट:** [i2pgit.org](https://i2pgit.org)
- **StormyCloud:** [stormycloud.org](https://www.stormycloud.org)

---

*यह गाइड [StormyCloud Inc](https://www.stormycloud.org) द्वारा I2P समुदाय के लिए बनाया गया है।*
