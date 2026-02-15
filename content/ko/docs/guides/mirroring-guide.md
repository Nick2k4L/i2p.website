---
title: "I2P에서 서비스 미러링하기"
description: "웹사이트, Git 저장소, API 등을 I2P 네트워크에서 이용할 수 있도록 만드는 초보자 친화적인 가이드 — 단계별 설명과 다이어그램 포함"
slug: "mirroring-guide"
lastUpdated: "2025-02"
accurateFor: "2.10.0"
---

일반 인터넷에 웹사이트를 운영하고 계시군요. 이제 이를 I2P에서도 이용할 수 있도록 만들고 싶어하시는군요 — 사람들이 자신의 신원이나 접속 위치를 드러내지 않고 개인적으로 방문할 수 있도록 말이죠. 이 가이드가 바로 그것에 관한 내용입니다.

미러링은 기존 사이트를 대체하지 않습니다. I2P 네트워크를 통한 두 번째 입구, 즉 비공개 입구를 추가하는 것입니다. 클리어넷 사이트는 이전과 정확히 동일하게 계속 운영됩니다.

![I2P 미러링 작동 방식 — 당신의 서버가 I2P 네트워크를 통해 두 번째 비공개 입구를 얻습니다](/images/guides/mirroring/how-mirroring-works.svg)

## 왜 I2P로 미러링하나요?

서비스를 미러링해야 하는 몇 가지 실용적인 이유가 있습니다:

**방문자의 프라이버시 보호.** 사람들이 자신의 IP 주소를 노출하지 않고 콘텐츠에 접근할 수 있습니다. 방문자와 서비스 간의 트래픽은 여러 홉을 통해 암호화됩니다 — 당신도, 네트워크를 감시하는 누구도 방문자가 누구인지 식별할 수 없습니다.

**검열 저항성.** 귀하의 사이트가 특정 지역에서 DNS 필터링, IP 차단 또는 기타 수단에 의해 차단된 경우, I2P 미러는 여전히 접근 가능합니다. DNS나 기존의 IP 라우팅에 의존하지 않기 때문입니다.

**복원력.** I2P 미러는 중복성을 추가합니다. 도메인이 압수당하거나 CDN이 서비스를 중단하더라도, 서버가 실행되는 한 I2P 버전은 계속 작동합니다.

**네트워크 지원.** I2P의 모든 서비스는 네트워크를 더욱 유용하게 만들고 생태계 성장에 도움이 됩니다.

## 필요한 것들

시작하기 전에 다음 사항을 확인하세요:

- **서버에서 실행 중인 I2P router** (Java 구현). 아직 없다면 먼저 [I2P 설치 가이드](/downloads/)를 따라하세요.
- **이미 작동 중인 웹사이트나 서비스** — 서버에서 콘텐츠를 제공하고 있어야 합니다.
- **기본적인 명령줄 사용 능력** — 설정 파일을 편집하고 몇 가지 명령을 실행해야 합니다.
- **약 15-20분** — 필요한 시간은 이게 전부입니다.

I2P router는 최소 512MB의 RAM이 필요하며 24시간 가동되는 서버에서 최적으로 작동합니다. router를 처음 시작한 경우, tunnel을 생성하기 전에 네트워크와 통합되도록 10-15분 정도 기다려 주세요.

## tunnel 이해하기

I2P 미러링의 핵심 개념은 **server tunnel**입니다. 아이디어는 다음과 같습니다:

I2P에서 누군가가 당신의 사이트를 방문하고자 할 때, 그들의 요청은 I2P 네트워크를 통해 여러 개의 암호화된 홉을 거쳐 당신의 I2P router에 도달합니다. 그러면 당신의 router가 그 요청을 **server tunnel**에 전달하고, server tunnel은 이를 localhost에서 실행 중인 웹 서버로 전송합니다. 웹 서버가 응답하면, 답변은 암호화된 네트워크를 통해 역방향 경로로 되돌아갑니다.

이러한 요청에 대해 웹 서버는 공용 인터넷에 직접 연결되지 않으며, localhost와만 통신합니다. I2P router가 모든 네트워크 관련 처리를 담당합니다.

### 어떤 터널 유형이 필요한가요?

I2P는 다양한 상황에 맞는 여러 tunnel 유형을 제공합니다:

![터널 유형 비교 — HTTP Server가 대부분의 웹사이트에 적합한 선택입니다](/images/guides/mirroring/tunnel-types.svg)

웹사이트를 미러링하려면 거의 확실히 **HTTP Server** tunnel을 원할 것입니다. 이는 웹 트래픽을 위해 특별히 설계되었으며 헤더 필터링, 압축, 호스트명 스푸핑을 기본적으로 처리합니다. 다른 유형들은 SSH 접근, 양방향 애플리케이션, 또는 IRC 서버와 같은 특수한 사용 사례를 위해 존재합니다.

## 파트 1: 웹사이트 미러링

이것이 가장 일반적인 시나리오입니다 — 기존의 일반 웹사이트가 있고 이를 I2P를 통해 이용할 수 있게 만들고 싶은 경우입니다. 프로세스를 간략히 살펴보면 다음과 같습니다:

![I2P에서 사이트를 미러링하는 5단계](/images/guides/mirroring/steps-overview.svg)

각 단계를 차례로 살펴보겠습니다.

### 1단계: 웹 서버에 Localhost 리스너 추가

일반 인터넷 사이트는 이미 포트 80과 443에서 전 세계에 공개되어 실행되고 있을 것입니다. I2P의 경우, I2P tunnel만 접근할 수 있는 localhost에 *별도의* 리스너를 생성합니다. 이를 통해 I2P 버전이 어떻게 보일지 완전히 제어할 수 있습니다 — 헤더를 제거하고, 관리자 패널을 차단하며, I2P의 높은 지연시간에 맞게 캐싱을 조정할 수 있습니다.

> **빠른 대안:** 사용자 정의가 필요하지 않다면 이 단계를 건너뛰고 I2P tunnel을 `127.0.0.1:80`으로 직접 가리킬 수 있습니다. 하지만 전용 리스너 방식을 권장합니다.

웹 서버를 선택하세요:

#### Nginx

새 사이트 설정 생성:

```bash
sudo nano /etc/nginx/sites-available/i2p-mirror
```
`yoursite.i2p`와 루트 경로를 자신의 값으로 바꾸어 이 설정을 붙여넣으세요:

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
활성화하고 다시 로드하세요:

```bash
sudo ln -s /etc/nginx/sites-available/i2p-mirror /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```
#### Apache

새 사이트 설정을 생성하세요:

```bash
sudo nano /etc/apache2/sites-available/i2p-mirror.conf
```
다음 설정을 붙여넣으세요:

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
그런 다음 포트를 추가하고 사이트를 활성화한 후 다시 로드하세요:

```bash
echo "Listen 127.0.0.1:8080" | sudo tee -a /etc/apache2/ports.conf
sudo a2ensite i2p-mirror
sudo a2enmod headers
sudo a2dismod status info
sudo apachectl configtest
sudo systemctl reload apache2
```
#### 왜 HSTS가 없는가?

두 설정 모두 `Strict-Transport-Security` 헤더를 명시적으로 피하고 있음을 알 수 있습니다. 이는 매우 중요합니다. HSTS는 브라우저에게 HTTPS만 사용하라고 지시하지만, I2P는 기존의 TLS를 사용하지 않습니다 — 암호화는 대신 네트워크 계층에서 처리됩니다. HSTS를 포함하면 방문자들이 I2P 사이트에 완전히 접근할 수 없게 됩니다.

### 2단계: 서버 터널 생성

브라우저에서 I2P Router Console을 엽니다:

```
`http://127.0.0.1:7657/i2ptunnel/`
```
새 터널을 생성하려면 **"Tunnel Wizard"**를 클릭하세요.

![I2P Tunnel Wizard startup](/images/guides/mirroring/mirror_02.svg)

터널 유형으로 **"HTTP Server"**를 선택하고 **다음**을 클릭합니다.

### 3단계: Tunnel 구성

tunnel 설정을 입력하세요:

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
![터널 구성 설정](/images/guides/mirroring/mirror_03.png)

**"Create"**를 클릭하여 tunnel을 생성하세요. I2P가 고유한 암호화 destination 키를 생성합니다 — 이것이 네트워크에서 당신의 영구 주소가 됩니다.

### 4단계: Tunnel 시작하고 대기

목록에서 새로운 tunnel을 찾아 **"Start"**를 클릭하세요. 다음과 같이 표시됩니다:

- **Local Destination** — `abc123...xyz.b32.i2p`와 같은 긴 base32 주소
- **Status** — "Running"으로 변경되어야 함

![Tunnel 실행 상태](/images/guides/mirroring/mirror_04.png)

> **인내심을 가지세요!** 첫 번째 시작 시에는 tunnel이 구축되고 leaseSet을 네트워크에 게시하는 동안 2-5분이 소요됩니다. 이는 정상적인 현상입니다.

### 5단계: 미러 테스트하기

tunnel이 실행 중으로 표시되면, I2P로 설정된 브라우저를 열고 base32 주소를 방문하세요. 첫 페이지 로딩은 5-30초가 걸릴 수 있습니다 — 이는 I2P에서 일반적입니다.

페이지가 로드되면 축하합니다 — 이제 사이트가 I2P에서 운영되고 있습니다!

### 6단계: 사람이 읽을 수 있는 .i2p 주소 등록 (선택사항)

귀하의 사이트는 이미 base32 주소를 통해 접근 가능하지만, `abc123...xyz.b32.i2p`는 정확히 기억하기 쉽지 않습니다. 깔끔한 `.i2p` 도메인을 얻으려면:

**자신의 주소록을 위해** — `http://127.0.0.1:7657/dns`로 이동하여 선택한 호스트명을 목적지 키에 매핑하여 추가하세요.

**공개 검색을 위해** — I2P 주소 레지스트리에 등록하세요:

1. `http://stats.i2p/i2p/addkey.html` 방문 (I2P 내부)
2. 원하는 호스트명과 전체 destination 키 입력 (터널 세부정보에서 가져온 500자 이상의 문자열로 "AAAA"로 끝남)
3. 등록 제출

등록이 완료되면, 적절한 주소록 구독을 가진 누구나 이름으로 귀하의 사이트를 찾을 수 있게 됩니다.

## 파트 2: 동적 애플리케이션 미러링

사이트가 정적 파일 대신 백엔드 프레임워크(Node.js, Python, Ruby, PHP 등)에서 실행되는 경우, I2P tunnel과 애플리케이션 사이에 리버스 프록시로 Nginx 또는 Apache가 필요합니다.

### 리버스 프록시 설정 (Nginx)

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
`X-I2P-Request` 헤더는 애플리케이션이 I2P 트래픽을 감지할 수 있게 해주며, 다르게 동작해야 하는 경우(예: clearnet 접근이 필요한 기능 비활성화)에 사용할 수 있습니다.

### Clearnet 미러를 위한 URL 재작성

애플리케이션이 clearnet 도메인을 가리키는 URL을 생성하는 경우, I2P 방문자를 위해 이를 다시 작성해야 합니다:

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
그다음 1부에서와 같이 `127.0.0.1:8080`을 가리키는 HTTP Server tunnel을 생성합니다.

## 파트 3: Git 저장소 미러링

### Gitea (전체 기능)

Gitea는 I2P를 통해 Git을 호스팅하기에 훌륭한 선택입니다. 웹 인터페이스, 이슈 추적, 풀 리퀘스트 기능을 제공하며, 이 모든 기능이 네트워크상에서 잘 작동합니다.

`/etc/gitea/app.ini` 설정:

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
핵심 포인트: `OFFLINE_MODE = true`는 Gitea가 외부 리소스(아바타, CDN 자산)를 로드하는 것을 방지합니다. `COOKIE_SECURE = false`는 I2P가 전통적인 의미에서 HTTPS를 사용하지 않기 때문에 필요합니다. I2P 서버에 아웃바운드 이메일이 구성되어 있지 않을 수 있으므로 이메일을 비활성화하세요.

두 개의 tunnel을 생성하세요: 1. **HTTP Server tunnel** → `127.0.0.1:3000` (웹 인터페이스) 2. **Standard Server tunnel** → `127.0.0.1:22` (git push/pull을 위한 SSH 접근 — 선택사항)

### cgit (가벼운 대안)

읽기 전용 브라우징과 HTTP 클로닝만 필요하다면 cgit이 훨씬 가볍습니다:

```ini
# /etc/cgitrc
virtual-root=/
clone-url=`http://yourgit.i2p/$CGIT_REPO_URL`
cache-root=/var/cache/cgit
cache-size=1000
scan-path=/srv/git
enable-http-clone=1
```
cgit의 적극적인 캐싱은 I2P의 높은 지연 시간에 특히 적합합니다.

### I2P를 통한 Git 클라이언트 측 설정

당신의 I2P Git 미러에서 클론하는 사람은 누구든지 Git 트래픽을 I2P HTTP 프록시를 통해 라우팅해야 합니다:

```bash
# Tell Git to use the I2P proxy for .i2p domains
git config --global http.http://yourgit.i2p.proxy `http://127.0.0.1:4444`
git config --global http.timeout 300

# Clone (allow for I2P latency)
GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=60 \
    git clone `http://yourgit.i2p/repo`
```
대용량 저장소의 경우, shallow clone을 사용하면 I2P를 통해 많은 시간을 절약할 수 있습니다:

```bash
git clone --depth 1 `http://yourgit.i2p/project`
git fetch --unshallow   # grab full history later if needed
```
## 파트 4: 미러링 파일 호스팅

### Nextcloud

Nextcloud는 일부 설정을 통해 I2P에서 작동합니다. `config/config.php`를 편집하세요:

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
잘 작동하는 것들: 파일 업로드 및 다운로드, 디렉터리 탐색, 인증, 공개 링크 공유, WebDAV. 작동하지 않는 것들: 데스크톱 동기화 클라이언트는 SOCKS 프록시 설정이 필요하며, 외부 스토리지 백엔드가 IP 주소를 유출할 수 있고, clearnet Nextcloud 인스턴스와의 연합은 개인정보를 침해할 수 있습니다.

### 간단한 파일 서버

Nextcloud의 오버헤드 없이 간단한 파일 호스팅을 위해서는 최소한의 Python 서버로 충분합니다:

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
`127.0.0.1:8080`을 가리키는 HTTP Server tunnel을 생성하세요.

## 파트 5: 미러링 API

### 기본 API 프록시

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
### WebSocket 지원

애플리케이션에서 WebSocket을 사용하는 경우 (채팅 앱, 실시간 대시보드 등):

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
I2P를 통한 WebSocket은 일반 인터넷보다 눈에 띄게 높은 지연 시간을 가집니다. 실시간 기능의 경우 더 긴 폴링 간격이나 클라이언트 측에서 낙관적 UI 업데이트를 고려하세요.

## 보안 모범 사례

미러를 작동시키는 것은 쉬운 부분입니다. 보안을 유지하려면 I2P 호스팅에 고유한 몇 가지 세부사항에 주의를 기울여야 합니다.

![I2P 미러를 위한 보안 체크리스트](/images/guides/mirroring/security-checklist.svg)

### 큰 규칙들

**localhost에만 바인드하세요.** 서비스는 `127.0.0.1`에서 수신 대기해야 하며, `0.0.0.0`에서는 절대 안 됩니다. I2P router만이 서비스에 접근할 수 있어야 합니다.

**식별 헤더 제거.** 웹 서버는 자신이 실행 중인 소프트웨어를 알리기를 좋아합니다. I2P에서는 이러한 정보를 공유하고 싶지 않을 것입니다.

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
**모든 것을 자체 호스팅하세요.** Google에서 폰트를 로드하거나, CDN에서 스크립트를 가져오거나, 제3자로부터 분석 도구를 사용하지 마세요. 모든 외부 리소스는 I2P 네트워크를 벗어나는 요청으로, 큰 지연시간을 추가하고 잠재적으로 정보를 유출할 수 있습니다. 라이브러리와 폰트를 다운로드하여 서버에 저장하고 로컬에서 제공하세요.

**데이터베이스를 절대 노출하지 마세요.** 당연한 말이지만, 데이터베이스 포트에 I2P tunnel을 생성하지 마세요. Server tunnel은 웹 서버나 애플리케이션 서버만을 가리켜야 합니다.

## 성능 조정

I2P는 요청당 2-10초의 지연 시간을 추가합니다. 이는 다중 홉 암호화의 대가입니다. 하지만 적절한 튜닝을 통해 I2P 미러가 놀랍도록 빠르게 느껴질 수 있습니다.

### 적극적으로 캐시하기

정적 자산들은 긴 캐시 수명을 가져야 합니다. 방문자가 이미 CSS와 이미지를 로드했다면, 다시 기다릴 필요가 없어야 합니다:

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```
### 압축 사용

더 작은 페이로드는 I2P의 제한된 대역폭에서 더 빠른 전송을 의미합니다:

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript
           text/xml application/xml application/xml+rss;
```
### 트래픽에 맞춰 Tunnel 수량 조정

더 많은 tunnel은 더 많은 동시 연결을 의미합니다. 기본값인 3은 트래픽이 적은 사이트에는 충분하지만, 혼잡이 발생한다면:

```properties
tunnel.0.option.inbound.quantity=5
tunnel.0.option.outbound.quantity=5
tunnel.0.option.inbound.backupQuantity=2
tunnel.0.option.outbound.backupQuantity=2
```
### 터널 길이 (홉)

각 홉은 지연시간을 증가시키지만 동시에 익명성도 향상시킵니다. 위협 모델에 따라 선택하세요:

![터널 홉 트레이드오프 — 더 많은 홉은 더 높은 프라이버시를 의미하지만 지연 시간도 증가합니다](/images/guides/mirroring/tunnel-hops.svg)

서버의 신원이 이미 알려진 공개 미러의 경우 (예: 귀하 조직의 웹사이트), 2홉으로 줄이는 것은 합리적인 절충안입니다:

```properties
tunnel.0.option.inbound.length=2
tunnel.0.option.outbound.length=2
```
### 일반 Router 팁

- I2P router를 **24시간 연중무휴**로 실행하세요. 더 오래 실행할수록 네트워크와 더 잘 통합되고, tunnel의 성능이 빨라집니다.
- 대역폭 공유를 최소 **256 KB/초**로 설정하되, 실제 회선 속도보다 약간 낮게 유지하세요.
- 재시작 후 첫 연결은 느릴 것으로 예상하세요 (30~90초). tunnel이 구축되면서 빠르게 개선됩니다.

## 고급: 수동 tunnel 구성

Router Console 마법사는 훌륭하게 작동하지만, 설정 파일을 직접 편집하는 것을 선호하거나 배포를 자동화해야 하는 경우 `~/.i2p/i2ptunnel.config`(또는 시스템 설치의 경우 `/var/lib/i2p/i2p-config/i2ptunnel.config`)에서 tunnel을 구성할 수 있습니다:

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
변경 사항 후 I2P 재시작:

```bash
sudo systemctl restart i2p
```
I2P 0.9.42부터는 여러 터널을 더 깔끔하게 관리하기 위해 `i2ptunnel.config.d/`에서 개별 설정 파일을 사용할 수도 있습니다:

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
## 문제 해결

### "내 사이트에 접근할 수 없습니다"

이 체크리스트를 순서대로 진행하세요:

**1. 웹 서버가 실제로 수신 대기 중인가요?**

```bash
nc -zv 127.0.0.1 8080
```
이것이 실패하면 웹 서버 설정에 문제가 있는 것입니다 — 1단계로 돌아가세요.

**2. tunnel이 실행 중인가요?** `http://127.0.0.1:7657/i2ptunnel/`을 방문하여 상태를 확인하세요. 5분 이상 "Starting"으로 표시된다면, router의 네트워크 연결을 확인하세요.

**3. LeaseSet이 게시되었나요?** 터널 옵션에서 `i2cp.dontPublishLeaseSet`이 설정되지 **않았는지** 확인하세요. 게시된 LeaseSet이 없으면 아무도 당신의 터널을 찾을 수 없습니다.

**4. 시계가 정확한가요?** I2P는 60초 이내의 시간 정확도가 필요합니다. 다음으로 확인하세요:

```bash
timedatectl status
```
시계가 맞지 않으면 I2P가 tunnel을 구축하는 데 문제가 발생합니다.

### 재시작 후 성능 저하

이는 정상적인 현상입니다. I2P router를 재시작한 후에는 tunnel 풀을 재구성하고 네트워크와 다시 통합하는 데 10-15분 정도의 시간을 주세요. 더 많은 피어들이 당신의 router에 대해 알게 되면서 성능이 향상됩니다.

또한 I2NP 포트에 대해 포트 포워딩이 구성되어 있는지 확인하세요(구체적인 포트 번호는 Router Console에서 확인). 포트 포워딩이 없으면 router가 "방화벽" 모드로 작동하여 성능이 제한됩니다.

### 다른 사람들이 방문할 때 "주소를 찾을 수 없음" 오류

방문자들은 자신의 주소록에 당신의 주소가 필요합니다. 공개 주소록에 등록했는지 확인하거나, 전체 base32 주소를 직접 공유하세요. 또한 `http://127.0.0.1:7657/susidns/subscriptions`에서 더 많은 구독을 추가할 수도 있습니다:

```
`http://stats.i2p/cgi-bin/newhosts.txt`
`http://i2host.i2p/cgi-bin/i2hostetag`
```
### 테스트 시 타임아웃

I2P는 본질적으로 더 높은 왕복 시간을 가집니다. 명령줄에서 테스트할 때는 확장된 타임아웃을 사용하세요:

```bash
# curl
curl --connect-timeout 60 --max-time 300 `http://yoursite.i2p/`

# wget
wget --timeout=300 `http://yoursite.i2p/`
```
### 로그 읽기

다른 방법이 모두 실패할 경우, I2P router 로그에서 오류를 확인하세요:

```bash
# System service
sudo journalctl -u i2p -f

# Or directly
tail -f ~/.i2p/logs/log-router-0.txt
```
## 키 백업하기

이것은 절대로 건너뛰어서는 안 되는 한 가지입니다. tunnel의 개인 키 파일들(I2P 설정 디렉토리의 `.dat` 파일들)은 네트워크에서 서비스에 영구 주소를 부여하는 것입니다. 이 파일들을 잃어버리면 I2P 주소를 영구적으로 잃게 됩니다. 복구도, 재설정도, 지원 티켓도 없습니다. 새로운 주소로 다시 시작해야 합니다.

지금 백업하세요:

```bash
# User installation
tar -czf tunnel-keys-backup.tar.gz ~/.i2p/*.dat

# System installation
sudo tar -czf tunnel-keys-backup.tar.gz /var/lib/i2p/i2p-config/*.dat
```
백업을 안전한 곳과 서버 외부에 보관하세요.

## 완료했습니다

이제 끝났습니다. 여러분의 서비스가 일반 인터넷과 I2P 네트워크 모두에서 사용할 수 있게 되었습니다. 사람들에게 여러분의 콘텐츠에 접근할 수 있는 프라이빗한 방법을 제공하는 것입니다 — 그들의 신원이 그들 자신의 것으로 남아있는 방법 말이죠.

문제가 발생하거나 더 적극적으로 참여하고 싶다면, 커뮤니티를 찾을 수 있는 곳은 다음과 같습니다:

- **포럼:** [i2pforum.net](https://i2pforum.net)
- **IRC:** 다양한 네트워크의 #i2p
- **개발:** [i2pgit.org](https://i2pgit.org)
- **StormyCloud:** [stormycloud.org](https://www.stormycloud.org)

---

*[StormyCloud Inc](https://www.stormycloud.org)에서 I2P 커뮤니티를 위해 작성한 가이드입니다.*
