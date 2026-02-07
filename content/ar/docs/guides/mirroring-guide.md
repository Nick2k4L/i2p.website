---
title: "نسخ خدماتك على I2P"
description: "دليل مبتدئ ودود لجعل مواقعك الإلكترونية ومستودعات Git وواجهات برمجة التطبيقات والمزيد متاحة على شبكة I2P — مع تعليمات خطوة بخطوة ومخططات"
slug: "mirroring-guide"
lastUpdated: "2025-02"
accurateFor: "2.10.0"
---

لديك موقع ويب على الإنترنت العادي. الآن تريد جعله متاحًا على I2P أيضًا — حتى يتمكن الأشخاص من زيارته بشكل خاص، دون الكشف عن هويتهم أو مكان قدومهم. هذا ما يتناوله هذا الدليل.

النسخ المتطابق لا يستبدل موقعك الحالي. بل يضيف مدخلاً ثانياً — مدخلاً خاصاً — عبر شبكة I2P. يستمر موقعك على الشبكة العادية في العمل تماماً كما كان من قبل.

![كيف يعمل النسخ المرآوي في I2P — يحصل خادمك على مدخل ثانٍ وخاص عبر شبكة I2P](/images/guides/mirroring/how-mirroring-works.svg)

## لماذا ننشئ مرآة على I2P؟

هناك عدة أسباب عملية لعمل نسخة مرآة لخدماتك:

**الخصوصية لزوارك.** يمكن للأشخاص الوصول إلى محتواك دون كشف عنوان IP الخاص بهم. حركة البيانات بينهم وبين خدمتك مشفرة عبر قفزات متعددة — لا يمكن لك ولا لأي شخص يراقب الشبكة تحديد هوية الزوار.

**مقاومة الرقابة.** إذا تم حجب موقعك في مناطق معينة عن طريق تصفية DNS أو حجب IP أو وسائل أخرى، فإن المرآة على I2P تبقى قابلة للوصول. لا تعتمد على DNS أو توجيه IP التقليدي.

**المرونة.** تضيف مرآة I2P التكرار. إذا تم حجز نطاقك أو تخلت عنك شبكة توصيل المحتوى، فإن إصدار I2P يبقى متاحاً طالما أن خادمك يعمل.

**دعم الشبكة.** كل خدمة على I2P تجعل الشبكة أكثر فائدة وتساعد في نمو النظام البيئي.

## ما ستحتاج إليه

قبل أن تبدأ، تأكد من أن لديك:

- **router I2P يعمل** على خادمك (التطبيق بلغة Java). إذا لم يكن لديك واحد بعد، اتبع [دليل تثبيت I2P](/downloads/) أولاً.
- **موقعك الإلكتروني أو خدمتك تعمل بالفعل** — يجب أن تكون تقدم المحتوى على خادمك.
- **راحة أساسية مع سطر الأوامر** — ستقوم بتحرير ملف إعدادات وتنفيذ بعض الأوامر.
- **حوالي 15-20 دقيقة** — هذا كل ما يتطلبه الأمر.

يحتاج router I2P الخاص بك إلى 512 ميجابايت من الذاكرة العشوائية على الأقل ويعمل بشكل أفضل على خادم يعمل على مدار الساعة. إذا كان router الخاص بك قد بدأ للمرة الأولى، امنحه 10-15 دقيقة للاندماج مع الشبكة قبل إنشاء tunnels.

## فهم الأنفاق (Tunnels)

المفهوم الأساسي وراء انعكاس I2P هو **server tunnel**. إليك الفكرة:

عندما يريد شخص ما على I2P زيارة موقعك، ينتقل طلبه عبر عدة قفزات مشفرة عبر شبكة I2P حتى يصل إلى I2P router الخاص بك. يقوم router الخاص بك بعد ذلك بتسليم الطلب إلى **server tunnel**، والذي يعيد توجيهه إلى خادم الويب الخاص بك الذي يعمل على localhost. يستجيب خادم الويب الخاص بك، وتأخذ الإجابة المسار العكسي للعودة عبر الشبكة المشفرة.

خادم الويب الخاص بك لا يتصل أبداً بالإنترنت العام لهذه الطلبات — إنه يتواصل فقط مع localhost. I2P router يتولى كل ما يتعلق بالشبكة.

### أي نوع من tunnel تحتاج؟

يقدم I2P عدة أنواع من الأنفاق (tunnels) لمختلف الحالات:

![مقارنة أنواع tunnel - خادم HTTP هو الخيار الصحيح لمعظم المواقع](/images/guides/mirroring/tunnel-types.svg)

لعكس موقع ويب، ستحتاج بالتأكيد تقريباً إلى نفق **خادم HTTP**. فهو مصمم خصيصاً لحركة الويب ويتعامل مع تصفية الرؤوس والضغط وانتحال اسم المضيف بشكل تلقائي. الأنواع الأخرى موجودة لحالات استخدام متخصصة مثل الوصول عبر SSH أو التطبيقات ثنائية الاتجاه أو خوادم IRC.

## الجزء الأول: إنشاء نسخة مرآة من الموقع

هذا هو السيناريو الأكثر شيوعاً — لديك موقع ويب clearnet موجود وتريد جعله متاحاً عبر I2P. إليك العملية باختصار:

![الخطوات الخمس لنسخ موقعك على I2P](/images/guides/mirroring/steps-overview.svg)

دعنا نمر عبر كل خطوة.

### الخطوة 1: إضافة مستمع localhost إلى خادم الويب الخاص بك

موقعك على الإنترنت العادي يعمل على الأرجح بالفعل على المنافذ 80 و 443، مفتوحاً للعالم. بالنسبة لـ I2P، ستقوم بإنشاء مستمع *منفصل* على localhost يمكن للـ I2P tunnel الوصول إليه فقط. هذا يمنحك تحكماً كاملاً في شكل إصدار I2P — يمكنك إزالة العناوين، وحظر لوحات الإدارة، وضبط التخزين المؤقت لزمن الاستجابة العالي في I2P.

> **بديل سريع:** إذا كنت لا تحتاج إلى أي تخصيص، يمكنك تخطي هذه الخطوة وتوجيه I2P tunnel مباشرة إلى `127.0.0.1:80`. لكن نهج المستمع المخصص مُوصى به.

اختر خادم الويب الخاص بك:

#### Nginx

إنشاء إعداد موقع جديد:

```bash
sudo nano /etc/nginx/sites-available/i2p-mirror
```
الصق هذا التكوين، مع استبدال `yoursite.i2p` ومسار الجذر بالقيم الخاصة بك:

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
قم بتفعيله وإعادة التحميل:

```bash
sudo ln -s /etc/nginx/sites-available/i2p-mirror /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```
#### Apache

إنشاء إعدادات موقع جديد:

```bash
sudo nano /etc/apache2/sites-available/i2p-mirror.conf
```
الصق هذا التكوين:

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
ثم أضف المنفذ، وفعّل الموقع، وأعد التحميل:

```bash
echo "Listen 127.0.0.1:8080" | sudo tee -a /etc/apache2/ports.conf
sudo a2ensite i2p-mirror
sudo a2enmod headers
sudo a2dismod status info
sudo apachectl configtest
sudo systemctl reload apache2
```
#### لماذا لا يوجد HSTS؟

ستلاحظ أن كلا التكوينين يتجنب صراحة رؤوس `Strict-Transport-Security`. هذا أمر بالغ الأهمية. HSTS يخبر المتصفحات باستخدام HTTPS فقط، لكن I2P لا يستخدم TLS التقليدي — بل يتم التعامل مع التشفير على مستوى الشبكة بدلاً من ذلك. تضمين HSTS سيؤدي إلى منع الزوار من الوصول إلى موقع I2P الخاص بك تماماً.

### الخطوة 2: إنشاء نفق الخادم

افتح وحدة تحكم I2P Router في متصفحك:

```
http://127.0.0.1:7657/i2ptunnel/
```
انقر على **"معالج الأنفاق"** لبدء إنشاء نفق جديد.

![بدء تشغيل معالج I2P Tunnel](/images/guides/mirroring/mirror_02.svg)

اختر **"HTTP Server"** كنوع tunnel وانقر على **التالي**.

### الخطوة 3: تكوين النفق (tunnel)

املأ إعدادات النفق:

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
![إعدادات تكوين النفق](/images/guides/mirroring/mirror_03.png)

انقر على **"إنشاء"** لتوليد النفق الخاص بك. سيقوم I2P بإنشاء مفتاح وجهة تشفيري فريد — وهذا يصبح عنوانك الدائم على الشبكة.

### الخطوة 4: تشغيل النفق والانتظار

اعثر على tunnel الجديد الخاص بك في القائمة وانقر على **"Start"**. ستشاهد:

- **الوجهة المحلية** — عنوان base32 طويل مثل `abc123...xyz.b32.i2p`
- **الحالة** — يجب أن تتغير إلى "قيد التشغيل"

![حالة تشغيل النفق](/images/guides/mirroring/mirror_04.png)

> **كن صبوراً!** يستغرق التشغيل الأول من 2-5 دقائق بينما يقوم الـ tunnel الخاص بك بالبناء ونشر الـ leasesets إلى الشبكة. هذا أمر طبيعي.

### الخطوة 5: اختبر المرآة الخاصة بك

بمجرد أن يظهر tunnel كقيد التشغيل، افتح متصفحك المُكوَّن لـ I2P وقم بزيارة عنوان base32 الخاص بك. قد يستغرق تحميل الصفحة الأولى من 5 إلى 30 ثانية — هذا أمر طبيعي في I2P.

إذا تم تحميل الصفحة، تهانينا — موقعك الآن مباشر على I2P!

### الخطوة 6: تسجيل عنوان .i2p قابل للقراءة البشرية (اختياري)

موقعك متاح بالفعل عبر عنوان base32، لكن `abc123...xyz.b32.i2p` ليس سهل التذكر تماماً. للحصول على نطاق `.i2p` واضح:

**لدفتر العناوين الخاص بك** — اذهب إلى `http://127.0.0.1:7657/dns` وأضف اسم المضيف المختار مربوطاً بمفتاح الوجهة الخاص بك.

**للاكتشاف العام** — قم بالتسجيل في سجل عناوين I2P:

1. زيارة `http://stats.i2p/i2p/addkey.html` (داخل I2P)
2. أدخل اسم المضيف المرغوب ومفتاح الوجهة الكامل (النص المكون من أكثر من 500 حرف من تفاصيل tunnel الخاص بك، والذي ينتهي بـ "AAAA")
3. إرسال للتسجيل

بمجرد التسجيل، سيتمكن أي شخص لديه اشتراكات دفتر العناوين المناسبة من العثور على موقعك بالاسم.

## الجزء 2: عكس التطبيقات الديناميكية

إذا كان موقعك يعمل على إطار عمل خلفي (Node.js، Python، Ruby، PHP، إلخ) بدلاً من الملفات الثابتة، فأنت بحاجة إلى Nginx أو Apache كوكيل عكسي بين I2P tunnel وتطبيقك.

### تكوين البروكسي العكسي (Nginx)

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
يتيح رأس `X-I2P-Request` لتطبيقك اكتشاف حركة مرور I2P إذا كان يحتاج للتصرف بشكل مختلف (على سبيل المثال، تعطيل الميزات التي تتطلب الوصول إلى الشبكة العادية).

### إعادة كتابة URL للمرايا على الشبكة العادية

إذا كان تطبيقك ينشئ عناوين URL تشير إلى نطاق clearnet الخاص بك، فستحتاج إلى إعادة كتابتها لزوار I2P:

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
ثم قم بإنشاء HTTP Server tunnel يشير إلى `127.0.0.1:8080`، تماماً كما في الجزء الأول.

## الجزء 3: نسخ مستودعات Git احتياطياً

### Gitea (مكتمل الميزات)

Gitea هو خيار ممتاز لاستضافة Git عبر I2P. يحتوي على واجهة ويب وتتبع المشاكل وطلبات السحب — وكلها تعمل بشكل جيد عبر الشبكة.

قم بتكوين `/etc/gitea/app.ini`:

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
النقاط الرئيسية: `OFFLINE_MODE = true` يمنع Gitea من تحميل الموارد الخارجية (الصور الرمزية، أصول CDN). `COOKIE_SECURE = false` مطلوب لأن I2P لا يستخدم HTTPS بالمعنى التقليدي. قم بتعطيل البريد الإلكتروني حيث أن خادم I2P الخاص بك قد لا يكون مُكوّناً لإرسال البريد الإلكتروني الصادر.

إنشاء tunnel اثنين: 1. **HTTP Server tunnel** → `127.0.0.1:3000` (واجهة الويب) 2. **Standard Server tunnel** → `127.0.0.1:22` (وصول SSH لعمليات git push/pull — اختياري)

### cgit (البديل الخفيف)

إذا كنت تحتاج فقط إلى التصفح للقراءة فقط و HTTP cloning، فإن cgit أخف بكثير:

```ini
# /etc/cgitrc
virtual-root=/
clone-url=http://yourgit.i2p/$CGIT_REPO_URL
cache-root=/var/cache/cgit
cache-size=1000
scan-path=/srv/git
enable-http-clone=1
```
التخزين المؤقت القوي لـ cgit يجعله مناسباً بشكل خاص لزمن الاستجابة الأعلى في I2P.

### إعداد العميل لـ Git عبر I2P

أي شخص يقوم بالاستنساخ من مرآة I2P Git الخاصة بك يحتاج إلى توجيه حركة مرور Git عبر بروكسي I2P HTTP:

```bash
# Tell Git to use the I2P proxy for .i2p domains
git config --global http.http://yourgit.i2p.proxy http://127.0.0.1:4444
git config --global http.timeout 300

# Clone (allow for I2P latency)
GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=60 \
    git clone http://yourgit.i2p/repo
```
بالنسبة للمستودعات الكبيرة، النسخ الضحلة توفر الكثير من الوقت عبر I2P:

```bash
git clone --depth 1 http://yourgit.i2p/project
git fetch --unshallow   # grab full history later if needed
```
## الجزء 4: استضافة الملفات المُرآة

### Nextcloud

يعمل Nextcloud عبر I2P مع بعض التكوين. قم بتحرير `config/config.php`:

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
ما يعمل بشكل جيد: رفع وتنزيل الملفات، تصفح المجلدات، المصادقة، مشاركة الروابط العامة، وWebDAV. ما لا يعمل: عملاء المزامنة المكتبية تحتاج إعداد SOCKS proxy، خلفيات التخزين الخارجية قد تسرب عناوين IP، والاتحاد مع مثيلات Nextcloud على الشبكة العادية يمكن أن يعرض الخصوصية للخطر.

### خادم الملفات البسيط

لاستضافة الملفات البسيطة دون التعقيدات الإضافية لـ Nextcloud، خادم Python بسيط يقوم بالمهمة:

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
أنشئ نفق خادم HTTP يشير إلى `127.0.0.1:8080`.

## الجزء الخامس: APIs النسخ المطابق

### وكيل API الأساسي

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
### دعم WebSocket

إذا كان تطبيقك يستخدم WebSockets (تطبيقات الدردشة، لوحات المراقبة المباشرة، إلخ):

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
لاحظ أن WebSockets عبر I2P ستواجه زمن استجابة أعلى بشكل ملحوظ من clearnet. للميزات الفورية، فكر في فترات polling أطول أو تحديثات UI متفائلة على جانب العميل.

## أفضل الممارسات الأمنية

تشغيل المرآة الخاصة بك هو الجزء السهل. الحفاظ على أمانها يتطلب الانتباه إلى بعض التفاصيل الفريدة لاستضافة I2P.

![قائمة التحقق الأمنية لمرايا I2P](/images/guides/mirroring/security-checklist.svg)

### القواعد الأساسية

**اربط بـ localhost فقط.** يجب أن تستمع خدمتك على `127.0.0.1`، وليس أبداً على `0.0.0.0`. I2P router هو الشيء الوحيد الذي يجب أن يكون قادراً على الوصول إلى خدمتك.

**إزالة الرؤوس المُعرِّفة.** خوادم الويب تحب الإعلان عن البرامج التي تشغلها. عبر I2P، هذه معلومات لا تريد مشاركتها.

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
**استضف كل شيء بنفسك.** لا تحمّل الخطوط من Google، أو النصوص البرمجية من CDNs، أو التحليلات من أطراف ثالثة. كل مورد خارجي هو طلب يخرج من شبكة I2P، مما يضيف زمن استجابة كبير ويحتمل تسريب المعلومات. قم بتنزيل المكتبات والخطوط، وضعها على خادمك، وقدمها محلياً.

**لا تعرض قواعد البيانات أبداً.** هذا أمر بديهي، ولكن لا تنشئ I2P tunnels لمنافذ قاعدة البيانات الخاصة بك. يجب أن تشير server tunnels فقط إلى خوادم الويب أو خوادم التطبيقات.

## ضبط الأداء

يضيف I2P زمن استجابة من 2-10 ثواني لكل طلب. هذا هو ثمن التشفير متعدد القفزات. ولكن مع الضبط المناسب، يمكن لمرآة I2P الخاصة بك أن تشعر بسرعة استجابة مفاجئة.

### التخزين المؤقت بقوة

يجب أن تحتوي الأصول الثابتة على فترات تخزين مؤقت طويلة. إذا كان الزائر قد حمّل ملفات CSS والصور الخاصة بك بالفعل، فلا يجب أن ينتظر لتحميلها مرة أخرى:

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```
### تمكين الضغط

الحمولات الأصغر تعني نقل أسرع عبر النطاق الترددي المحدود لـ I2P:

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript
           text/xml application/xml application/xml+rss;
```
### ضبط كمية الأنفاق للحركة المرورية

المزيد من tunnels يعني المزيد من الاتصالات المتزامنة. الافتراضي وهو 3 جيد للمواقع قليلة الحركة، لكن إذا كنت تواجه ازدحاماً:

```properties
tunnel.0.option.inbound.quantity=5
tunnel.0.option.outbound.quantity=5
tunnel.0.option.inbound.backupQuantity=2
tunnel.0.option.outbound.backupQuantity=2
```
### طول النفق (القفزات)

كل قفزة تضيف زمن استجابة ولكنها تضيف أيضاً إخفاء هوية. اختر بناءً على نموذج التهديد الخاص بك:

![مقايضة قفزات tunnel — المزيد من القفزات يعني خصوصية أكبر ولكن زمن استجابة أعلى](/images/guides/mirroring/tunnel-hops.svg)

بالنسبة لمرآة عامة حيث هوية الخادم معروفة بالفعل (موقع منظمتك الإلكتروني، على سبيل المثال)، فإن التقليل إلى 2 hops يُعتبر مقايضة معقولة:

```properties
tunnel.0.option.inbound.length=2
tunnel.0.option.outbound.length=2
```
### نصائح عامة للموجه (Router)

- شغّل router الـ I2P **24/7**. كلما طالت مدة تشغيله، كان أفضل اندماجاً مع الشبكة، وأسرع أداءً لـ tunnels الخاصة بك.
- اضبط مشاركة عرض النطاق الترددي على الأقل **256 KB/sec**، ولكن أبقها أقل قليلاً من سرعة خطك الفعلي.
- توقع أن تكون الاتصالات الأولى بعد إعادة التشغيل بطيئة (30-90 ثانية). هذا يتحسن بسرعة مع بناء tunnels.

## متقدم: تكوين tunnel يدوي

معالج وحدة تحكم الـ router يعمل بشكل رائع، ولكن إذا كنت تفضل تحرير ملفات التكوين مباشرة — أو تحتاج إلى أتمتة عمليات النشر — يمكنك تكوين الـ tunnels في `~/.i2p/i2ptunnel.config` (أو `/var/lib/i2p/i2p-config/i2ptunnel.config` لتثبيتات النظام):

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
أعد تشغيل I2P بعد التغييرات:

```bash
sudo systemctl restart i2p
```
اعتباراً من I2P 0.9.42، يمكنك أيضاً استخدام ملفات التكوين الفردية في `i2ptunnel.config.d/` لإدارة أنظف للأنفاق المتعددة:

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
## استكشاف الأخطاء وإصلاحها

### "لا أستطيع الوصول إلى موقعي"

اعمل من خلال قائمة التحقق هذه بالترتيب:

**1. هل خادم الويب يستمع فعلاً؟**

```bash
nc -zv 127.0.0.1 8080
```
إذا فشل هذا، فإن تكوين خادم الويب الخاص بك يواجه مشكلة — ارجع إلى الخطوة 1.

**2. هل يعمل النفق؟** قم بزيارة `http://127.0.0.1:7657/i2ptunnel/` وتحقق من الحالة. إذا كان يظهر "Starting" لأكثر من 5 دقائق، تحقق من تكامل الشبكة في الموجه الخاص بك.

**3. هل تم نشر LeaseSet؟** تأكد من أن `i2cp.dontPublishLeaseSet` غير مُعيّن في خيارات tunnel الخاص بك. بدون LeaseSet منشور، لن يتمكن أحد من العثور على tunnel الخاص بك.

**4. هل ساعتك دقيقة؟** يتطلب I2P دقة في الوقت ضمن 60 ثانية. تحقق من ذلك باستخدام:

```bash
timedatectl status
```
إذا كانت ساعتك غير مضبوطة، فسيواجه I2P مشكلة في بناء الأنفاق.

### أداء بطيء بعد إعادة التشغيل

هذا أمر طبيعي. بعد إعادة تشغيل I2P router الخاص بك، امنحه 10-15 دقيقة لإعادة بناء مجموعات tunnel الخاصة به وإعادة الاندماج مع الشبكة. يتحسن الأداء كلما تعلم المزيد من الأقران عن router الخاص بك.

تحقق أيضاً من أن إعادة توجيه المنافذ مُعدة لمنفذ I2NP الخاص بك (تحقق من وحدة تحكم الموجه للحصول على رقم المنفذ المحدد). بدونها، سيعمل الموجه في وضع "محمي بجدار الحماية"، مما يحد من الأداء.

### أخطاء "العنوان غير موجود" عندما يزور الآخرون

يحتاج الزوار إلى عنوانك في دفتر العناوين الخاص بهم. تأكد من أنك قمت بالتسجيل في دفتر عناوين عام، أو شارك عنوان base32 الكامل الخاص بك مباشرة. يمكنهم أيضاً إضافة المزيد من الاشتراكات على `http://127.0.0.1:7657/susidns/subscriptions`:

```
http://stats.i2p/cgi-bin/newhosts.txt
http://i2host.i2p/cgi-bin/i2hostetag
```
### انتهاء المهلة الزمنية عند الاختبار

I2P لديه بطبيعته أوقات استجابة ذهابًا وإيابًا أطول. عند الاختبار من سطر الأوامر، استخدم مهلات زمنية مطولة:

```bash
# curl
curl --connect-timeout 60 --max-time 300 http://yoursite.i2p/

# wget
wget --timeout=300 http://yoursite.i2p/
```
### قراءة السجلات

إذا لم تساعد أي من الحلول الأخرى، تحقق من سجلات I2P router للأخطاء:

```bash
# System service
sudo journalctl -u i2p -f

# Or directly
tail -f ~/.i2p/logs/log-router-0.txt
```
## احتفظ بنسخة احتياطية من مفاتيحك

هذا هو الشيء الوحيد الذي يجب عليك عدم تجاهله مطلقاً. ملفات المفاتيح الخاصة لـ tunnel الخاص بك (ملفات `.dat` في دليل إعدادات I2P) هي ما تمنح خدمتك عنوانها الدائم على الشبكة. إذا فقدتها، فستفقد عنوان I2P الخاص بك — إلى الأبد. لا يوجد استرداد، لا إعادة تعيين، لا تذكرة دعم. سيتعين عليك البدء من جديد بعنوان جديد.

قم بعمل نسخة احتياطية منها الآن:

```bash
# User installation
tar -czf tunnel-keys-backup.tar.gz ~/.i2p/*.dat

# System installation
sudo tar -czf tunnel-keys-backup.tar.gz /var/lib/i2p/i2p-config/*.dat
```
احفظ النسخة الاحتياطية في مكان آمن وخارج الخادم.

## انتهيت

هذا كل شيء. خدمتك متاحة الآن على كل من الإنترنت العادي وشبكة I2P. أنت تمنح الناس طريقة خاصة للوصول إلى محتواك — طريقة تحافظ على هويتهم الخاصة.

إذا واجهت مشاكل أو كنت تريد المشاركة أكثر، إليك أين تجد المجتمع:

- **المنتدى:** [i2pforum.net](https://i2pforum.net)
- **IRC:** #i2p على شبكات مختلفة
- **التطوير:** [i2pgit.org](https://i2pgit.org)
- **StormyCloud:** [stormycloud.org](https://www.stormycloud.org)

---

*دليل تم إنشاؤه من قِبل [StormyCloud Inc](https://www.stormycloud.org) لمجتمع I2P.*
