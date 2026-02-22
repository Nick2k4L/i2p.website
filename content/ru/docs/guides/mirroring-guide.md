---
title: "Зеркалирование ваших сервисов в I2P"
description: "Руководство для начинающих по размещению ваших веб-сайтов, Git-репозиториев, API и многого другого в сети I2P — с пошаговыми инструкциями и диаграммами"
slug: "mirroring-guide"
lastUpdated: "2025-02"
accurateFor: "2.10.0"
---

У вас есть веб-сайт в обычном интернете. Теперь вы хотите сделать его доступным и в I2P — чтобы люди могли посещать его приватно, не раскрывая, кто они и откуда приходят. Именно об этом данное руководство.

Зеркалирование не заменяет ваш существующий сайт. Оно добавляет второй вход — приватный — через сеть I2P. Ваш обычный сайт продолжает работать точно так же, как и раньше.

![Как работает зеркалирование I2P — ваш сервер получает второй, приватный вход через сеть I2P](/images/guides/mirroring/how-mirroring-works.svg)

## Зачем создавать зеркало в I2P?

Существует несколько практических причин для создания зеркал ваших сервисов:

**Приватность для ваших посетителей.** Люди могут получать доступ к вашему контенту, не раскрывая свой IP-адрес. Трафик между ними и вашим сервисом шифруется через несколько переходов — ни вы, ни кто-либо другой, наблюдающий за сетью, не сможет определить, кто посещает ваш сайт.

**Устойчивость к цензуре.** Если ваш сайт заблокирован в определенных регионах с помощью DNS-фильтрации, блокировки IP-адресов или другими способами, зеркало I2P остается доступным. Оно не зависит от DNS или обычной IP-маршрутизации.

**Устойчивость.** I2P зеркало добавляет избыточность. Если ваш домен конфискуют или ваш CDN откажется от вас, I2P версия останется работать до тех пор, пока работает ваш сервер.

**Поддержка сети.** Каждый сервис в I2P делает сеть более полезной и помогает развивать экосистему.

## Что вам понадобится

Перед началом убедитесь, что у вас есть:

- **Работающий I2P router** на вашем сервере (Java-реализация). Если у вас его ещё нет, сначала следуйте [Руководству по установке I2P](/downloads/).
- **Ваш веб-сайт или сервис уже работает** — он должен обслуживать контент на вашем сервере.
- **Базовые навыки работы с командной строкой** — вам нужно будет отредактировать конфигурационный файл и выполнить несколько команд.
- **Примерно 15–20 минут** — это всё, что потребуется.

Ваш I2P router нуждается как минимум в 512 МБ оперативной памяти и лучше всего работает на сервере с круглосуточной работой. Если ваш router только что запустился впервые, дайте ему 10–15 минут для интеграции с сетью перед созданием tunnel'ей.

## Понимание Tunnel'ов

Основная концепция зеркалирования I2P — это **server tunnel**. Вот идея:

Когда кто-то в I2P хочет посетить ваш сайт, его запрос проходит через несколько зашифрованных переходов по сети I2P, пока не достигнет вашего I2P router. Затем ваш router передает запрос **server tunnel** (серверному туннелю), который перенаправляет его на ваш веб-сервер, работающий на localhost. Ваш веб-сервер отвечает, и ответ идет обратным путем через зашифрованную сеть.

Ваш веб-сервер никогда не обращается к публичному интернету для этих запросов — он взаимодействует только с localhost. I2P router обрабатывает всё сетевое взаимодействие.

### Какой тип tunnel вам нужен?

I2P предлагает несколько типов tunnel для различных ситуаций:

![Сравнение типов tunnel — HTTP Server является правильным выбором для большинства веб-сайтов](/images/guides/mirroring/tunnel-types.svg)

Для зеркалирования веб-сайта вам почти наверняка понадобится туннель **HTTP Server**. Он специально разработан для веб-трафика и обрабатывает фильтрацию заголовков, сжатие и подмену имени хоста из коробки. Другие типы существуют для специализированных случаев использования, таких как SSH-доступ, двунаправленные приложения или IRC-серверы.

## Часть 1: Зеркалирование веб-сайта

Это наиболее распространенный сценарий — у вас есть существующий сайт в обычном интернете, и вы хотите сделать его доступным через I2P. Вот краткий обзор процесса:

![Пять шагов для создания зеркала вашего сайта на I2P](/images/guides/mirroring/steps-overview.svg)

Давайте пройдем через каждый шаг.

### Шаг 1: Добавьте localhost-слушатель к вашему веб-серверу

Ваш clearnet сайт вероятно уже работает на портах 80 и 443, открытых для всего мира. Для I2P вы создадите *отдельный* слушатель на localhost, к которому может подключиться только I2P tunnel. Это даёт вам полный контроль над тем, как выглядит I2P версия — вы можете удалять заголовки, блокировать админ-панели и настраивать кэширование для более высокой задержки I2P.

> **Быстрая альтернатива:** Если вам не нужна никакая настройка, вы можете пропустить этот шаг и направить I2P tunnel напрямую на `127.0.0.1:80`. Но рекомендуется использовать подход с выделенным слушателем.

Выберите свой веб-сервер:

#### Nginx

Создайте новую конфигурацию сайта:

```bash
sudo nano /etc/nginx/sites-available/i2p-mirror
```
Вставьте эту конфигурацию, заменив `yoursite.i2p` и корневой путь на свои значения:

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
Включите его и перезагрузите:

```bash
sudo ln -s /etc/nginx/sites-available/i2p-mirror /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```
#### Apache

Создайте новый конфиг сайта:

```bash
sudo nano /etc/apache2/sites-available/i2p-mirror.conf
```
Вставьте эту конфигурацию:

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
Затем добавьте порт, включите сайт и перезагрузите:

```bash
echo "Listen 127.0.0.1:8080" | sudo tee -a /etc/apache2/ports.conf
sudo a2ensite i2p-mirror
sudo a2enmod headers
sudo a2dismod status info
sudo apachectl configtest
sudo systemctl reload apache2
```
#### Почему нет HSTS?

Вы заметите, что обе конфигурации явно избегают заголовков `Strict-Transport-Security`. Это критически важно. HSTS указывает браузерам использовать только HTTPS, но I2P не использует традиционный TLS — шифрование обрабатывается на сетевом уровне. Включение HSTS полностью заблокирует доступ посетителей к вашему I2P сайту.

### Шаг 2: Создание серверного tunnel

Откройте консоль I2P router в вашем браузере:

```
http://127.0.0.1:7657/i2ptunnel/
```
Нажмите **"Tunnel Wizard"**, чтобы начать создание нового tunnel.

![I2P Tunnel Wizard startup](/images/guides/mirroring/mirror_02.svg)

Выберите **"HTTP Server"** в качестве типа туннеля и нажмите **Далее**.

### Шаг 3: Настройка tunnel

Заполните настройки tunnel:

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
![Настройки конфигурации tunnel'а](/images/guides/mirroring/mirror_03.png)

Нажмите **"Создать"**, чтобы сгенерировать ваш tunnel. I2P создаст уникальный криптографический ключ destination — он станет вашим постоянным адресом в сети.

### Шаг 4: Запустите tunnel и ждите

Найдите ваш новый tunnel в списке и нажмите **"Start"**. Вы увидите:

- **Local Destination** — длинный base32 адрес вида `abc123...xyz.b32.i2p`
- **Status** — должен измениться на "Running"

![Статус работы туннеля](/images/guides/mirroring/mirror_04.png)

> **Будьте терпеливы!** Первый запуск занимает 2–5 минут, пока ваш tunnel строится и публикует свои leaseSet в сети. Это нормально.

### Шаг 5: Протестируйте ваше зеркало

Как только tunnel покажет статус "запущен", откройте браузер с настроенным I2P и перейдите по вашему base32 адресу. Первая загрузка страницы может занять 5–30 секунд — это типично для I2P.

Если страница загружается, поздравляем — ваш сайт теперь работает в I2P!

### Шаг 6: Регистрация понятного адреса .i2p (Опционально)

Ваш сайт уже доступен по base32 адресу, но `abc123...xyz.b32.i2p` не очень запоминающийся. Чтобы получить чистый домен `.i2p`:

**Для вашей собственной адресной книги** — перейдите в `http://127.0.0.1:7657/dns` и добавьте выбранное вами имя хоста, сопоставленное с вашим ключом назначения.

**Для публичного обнаружения** — зарегистрируйтесь в реестре I2P адресов:

1. Перейдите на `http://stats.i2p/i2p/addkey.html` (внутри I2P)
2. Введите желаемое имя хоста и полный ключ назначения (строка из 500+ символов из деталей вашего tunnel, заканчивающаяся на "AAAA")
3. Отправьте для регистрации

После регистрации любой пользователь с соответствующими подписками на адресную книгу сможет найти ваш сайт по имени.

## Часть 2: Зеркалирование динамических приложений

Если ваш сайт работает на backend-фреймворке (Node.js, Python, Ruby, PHP и т.д.) вместо статических файлов, вам потребуется Nginx или Apache в качестве обратного прокси между I2P tunnel и вашим приложением.

### Настройка обратного прокси (Nginx)

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
Заголовок `X-I2P-Request` позволяет вашему приложению обнаруживать I2P трафик, если ему необходимо вести себя по-другому (например, отключать функции, которые требуют доступа к обычной сети).

### Перезапись URL для зеркал Clearnet

Если ваше приложение генерирует URL-адреса, указывающие на ваш clearnet домен, вам нужно будет переписать их для посетителей I2P:

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
Затем создайте HTTP Server tunnel, указывающий на `127.0.0.1:8080`, точно так же, как в Части 1.

## Часть 3: Зеркалирование Git-репозиториев

### Gitea (Полнофункциональный)

Gitea — отличный выбор для хостинга Git через I2P. У него есть веб-интерфейс, отслеживание задач и pull requests — все это хорошо работает в сети.

Настройте `/etc/gitea/app.ini`:

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
Ключевые моменты: `OFFLINE_MODE = true` предотвращает загрузку Gitea внешних ресурсов (аватары, CDN-ресурсы). `COOKIE_SECURE = false` необходимо, поскольку I2P не использует HTTPS в традиционном понимании. Отключите электронную почту, так как ваш I2P-сервер может не иметь настроенной исходящей почты.

Создайте два tunnel: 1. **HTTP Server tunnel** → `127.0.0.1:3000` (веб-интерфейс) 2. **Standard Server tunnel** → `127.0.0.1:22` (SSH доступ для git push/pull — опционально)

### cgit (Легковесная альтернатива)

Если вам нужен только просмотр в режиме чтения и HTTP-клонирование, cgit намного легче:

```ini
# /etc/cgitrc
virtual-root=/
clone-url=http://yourgit.i2p/$CGIT_REPO_URL
cache-root=/var/cache/cgit
cache-size=1000
scan-path=/srv/git
enable-http-clone=1
```
Агрессивное кэширование cgit делает его особенно подходящим для высокой задержки I2P.

### Настройка клиентской части для Git через I2P

Любому, кто клонирует из вашего Git зеркала I2P, необходимо направлять трафик Git через HTTP-прокси I2P:

```bash
# Tell Git to use the I2P proxy for .i2p domains
git config --global http.http://yourgit.i2p.proxy http://127.0.0.1:4444
git config --global http.timeout 300

# Clone (allow for I2P latency)
GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=60 \
    git clone http://yourgit.i2p/repo
```
Для больших репозиториев поверхностные клоны экономят много времени при работе через I2P:

```bash
git clone --depth 1 http://yourgit.i2p/project
git fetch --unshallow   # grab full history later if needed
```
## Часть 4: Зеркалирование файлового хостинга

### Nextcloud

Nextcloud работает через I2P с некоторыми настройками. Отредактируйте `config/config.php`:

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
Что работает хорошо: загрузка и скачивание файлов, просмотр директорий, аутентификация, публичное расшаривание ссылок и WebDAV. Что не работает: клиенты синхронизации для настольных систем требуют настройки SOCKS-прокси, внешние хранилища могут раскрывать IP-адреса, а федерация с clearnet-инстансами Nextcloud может скомпрометировать приватность.

### Простой файловый сервер

Для простого размещения файлов без накладных расходов Nextcloud подойдет минимальный Python-сервер:

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
Создайте HTTP Server tunnel, указывающий на `127.0.0.1:8080`.

## Часть 5: API для зеркалирования

### Базовый API прокси

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
### Поддержка WebSocket

Если ваше приложение использует WebSockets (чат-приложения, живые дашборды и т.д.):

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
Обратите внимание, что WebSockets поверх I2P будут иметь заметно большую задержку, чем в обычной сети. Для функций реального времени рассмотрите возможность увеличения интервалов опроса или оптимистичных обновлений интерфейса на стороне клиента.

## Лучшие практики безопасности

Запуск вашего зеркала — это простая часть. Обеспечение его безопасности требует внимания к нескольким деталям, которые уникальны для хостинга в I2P.

![Контрольный список безопасности для зеркал I2P](/images/guides/mirroring/security-checklist.svg)

### Основные правила

**Привязывайтесь только к localhost.** Ваш сервис должен слушать на `127.0.0.1`, никогда на `0.0.0.0`. Только I2P router должен иметь возможность достичь вашего сервиса.

**Удалите идентифицирующие заголовки.** Веб-серверы любят объявлять, какое программное обеспечение они используют. В сети I2P это информация, которой вы не хотите делиться.

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
**Размещайте всё самостоятельно.** Не загружайте шрифты с Google, скрипты с CDN или аналитику от третьих сторон. Каждый внешний ресурс — это запрос, который покидает сеть I2P, добавляя огромную задержку и потенциально утекающий информацию. Скачайте библиотеки и шрифты, разместите их на своём сервере и раздавайте локально.

**Никогда не выставляйте базы данных наружу.** Это должно быть само собой разумеющимся, но не создавайте I2P tunnel к портам ваших баз данных. Server tunnel должны указывать только на веб-серверы или серверы приложений.

## Настройка производительности

I2P добавляет 2–10 секунд задержки на каждый запрос. Это цена многоузловой маршрутизации с шифрованием. Но при правильной настройке ваше I2P-зеркало может работать удивительно быстро.

### Агрессивное кэширование

Статические ресурсы должны иметь длительное время кэширования. Если посетитель уже загрузил ваши CSS и изображения, ему не следует ждать их повторной загрузки:

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```
### Включить сжатие

Меньший размер полезной нагрузки означает более быстрые передачи при ограниченной пропускной способности I2P:

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript
           text/xml application/xml application/xml+rss;
```
### Настройка количества tunnel для трафика

Больше tunnel означает больше одновременных соединений. Значение по умолчанию 3 подходит для сайтов с низким трафиком, но если вы наблюдаете перегрузку:

```properties
tunnel.0.option.inbound.quantity=5
tunnel.0.option.outbound.quantity=5
tunnel.0.option.inbound.backupQuantity=2
tunnel.0.option.outbound.backupQuantity=2
```
### Длина туннеля (переходы)

Каждый hop добавляет задержку, но также повышает анонимность. Выбирайте на основе вашей модели угроз:

![Компромисс количества переходов tunnel — больше переходов означает большую приватность, но более высокую задержку](/images/guides/mirroring/tunnel-hops.svg)

Для публичного зеркала, где личность сервера уже известна (например, веб-сайт вашей организации), уменьшение до 2 переходов является разумным компромиссом:

```properties
tunnel.0.option.inbound.length=2
tunnel.0.option.outbound.length=2
```
### Общие советы по router'у

- Запускайте свой I2P router **24/7**. Чем дольше он работает, тем лучше он интегрирован в сеть и тем быстрее работают ваши tunnel.
- Установите совместное использование пропускной способности не менее **256 КБ/сек**, но держите её немного ниже вашей фактической скорости линии.
- Ожидайте, что первые подключения после перезапуска будут медленными (30–90 секунд). Это быстро улучшается по мере построения tunnel.

## Расширенные настройки: Ручная настройка tunnel

Мастер настройки Router Console работает отлично, но если вы предпочитаете редактировать конфигурационные файлы напрямую — или вам нужно автоматизировать развертывание — вы можете настроить tunnel в `~/.i2p/i2ptunnel.config` (или `/var/lib/i2p/i2p-config/i2ptunnel.config` для системных установок):

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
Перезапустите I2P после внесения изменений:

```bash
sudo systemctl restart i2p
```
Начиная с I2P 0.9.42, вы также можете использовать отдельные конфигурационные файлы в `i2ptunnel.config.d/` для более удобного управления несколькими tunnel:

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
## Устранение неполадок

### "Я не могу попасть на свой сайт"

Выполните этот контрольный список по порядку:

**1. Действительно ли веб-сервер прослушивает порт?**

```bash
nc -zv 127.0.0.1 8080
```
Если это не работает, значит проблема в конфигурации вашего веб-сервера — вернитесь к шагу 1.

**2. Работает ли tunnel?** Перейдите по адресу `http://127.0.0.1:7657/i2ptunnel/` и проверьте статус. Если он показывает "Starting" более 5 минут, проверьте сетевую интеграцию вашего router.

**3. Опубликован ли LeaseSet?** Убедитесь, что параметр `i2cp.dontPublishLeaseSet` НЕ установлен в настройках вашего туннеля. Без опубликованного LeaseSet никто не сможет найти ваш туннель.

**4. Точны ли ваши часы?** I2P требует точности времени в пределах 60 секунд. Проверьте с помощью:

```bash
timedatectl status
```
Если ваши часы идут неточно, I2P будет испытывать трудности при построении tunnel'ов.

### Низкая производительность после перезапуска

Это нормально. После перезапуска вашего I2P router дайте ему 10–15 минут на восстановление пулов tunnel и повторную интеграцию с сетью. Производительность улучшается по мере того, как больше узлов узнают о вашем router.

Также проверьте, что проброс портов настроен для вашего I2NP порта (проверьте конкретный номер порта в консоли роутера). Без этого ваш router работает в режиме "за брандмауэром", что ограничивает производительность.

### Ошибки "Адрес не найден" при посещении другими пользователями

Посетителям нужен ваш адрес в их адресной книге. Убедитесь, что вы зарегистрировались в публичной адресной книге, или поделитесь своим полным base32 адресом напрямую. Они также могут добавить больше подписок по адресу `http://127.0.0.1:7657/susidns/subscriptions`:

```
http://stats.i2p/cgi-bin/newhosts.txt
http://i2host.i2p/cgi-bin/i2hostetag
```
### Таймауты при тестировании

I2P имеет изначально более высокое время отклика. При тестировании из командной строки используйте увеличенные таймауты:

```bash
# curl
curl --connect-timeout 60 --max-time 300 http://yoursite.i2p/

# wget
wget --timeout=300 http://yoursite.i2p/
```
### Чтение логов

Если ничего другое не помогает, проверьте логи I2P router на наличие ошибок:

```bash
# System service
sudo journalctl -u i2p -f

# Or directly
tail -f ~/.i2p/logs/log-router-0.txt
```
## Создайте резервную копию ваших ключей

Это единственное, что вы абсолютно не должны пропускать. Файлы приватных ключей ваших tunnel (файлы `.dat` в директории конфигурации I2P) — это то, что даёт вашему сервису постоянный адрес в сети. Если вы их потеряете, вы потеряете свой I2P-адрес — навсегда. Нет никакого восстановления, никакого сброса, никакого обращения в поддержку. Вам придётся начинать заново с новым адресом.

Создайте их резервную копию прямо сейчас:

```bash
# User installation
tar -czf tunnel-keys-backup.tar.gz ~/.i2p/*.dat

# System installation
sudo tar -czf tunnel-keys-backup.tar.gz /var/lib/i2p/i2p-config/*.dat
```
Храните резервную копию в безопасном месте и вне сервера.

## Готово

Вот и всё. Теперь ваш сервис доступен как в обычном интернете, так и в сети I2P. Вы предоставляете людям приватный способ доступа к вашему контенту — такой, при котором их личность остается при них.

Если у вас возникли проблемы или вы хотите больше участвовать в проекте, вот где можно найти сообщество:

- **Форум:** [i2pforum.net](https://i2pforum.net)
- **IRC:** #i2p в различных сетях
- **Разработка:** [i2pgit.org](https://i2pgit.org)
- **StormyCloud:** [stormycloud.org](https://www.stormycloud.org)

---

*Руководство создано [StormyCloud Inc](https://www.stormycloud.org) для сообщества I2P.*
