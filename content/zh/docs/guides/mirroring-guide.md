---
title: "在I2P上镜像您的服务"
description: "一个初学者友好的指南，教你如何在I2P网络上发布你的网站、Git仓库、API等服务——包含详细的步骤说明和图解"
slug: "mirroring-guide"
lastUpdated: "2025-02"
accurateFor: "2.10.0"
---

您在常规互联网上有一个网站。现在您想让它在I2P上也可以访问——这样人们就可以私密地访问它，而不会暴露他们是谁或来自哪里。这就是本指南要介绍的内容。

镜像不会替换您现有的网站。它只是通过I2P网络增加了第二个入口——一个私密的入口。您的明网站点会完全按照之前的方式继续运行。

![I2P 镜像工作原理 — 您的服务器通过 I2P 网络获得第二个私密入口](/images/guides/mirroring/how-mirroring-works.svg)

## 为什么要镜像到 I2P？

镜像您的服务有几个实际原因：

**保护访问者隐私。** 人们可以在不暴露其IP地址的情况下访问您的内容。他们与您的服务之间的流量通过多跳加密传输——无论是您还是网络监控者都无法识别访问者的身份。

**抗审查能力。** 如果你的网站在某些地区被DNS过滤、IP封锁或其他手段屏蔽，I2P镜像仍然可以访问。它不依赖DNS或传统的IP路由。

**韧性。** I2P 镜像增加了冗余性。如果您的域名被查封或您的 CDN 停止服务，只要您的服务器还在运行，I2P 版本就会保持可用。

**支持网络。** I2P上的每个服务都让网络变得更有用，并有助于生态系统的发展。

## 您需要准备的内容

开始之前，请确保您已具备：

- **在你的服务器上运行的 I2P router**（Java 实现版本）。如果你还没有安装，请先按照 [I2P 安装指南](/downloads/) 进行安装。
- **你的网站或服务已经正常工作** — 它应该已经在你的服务器上提供内容服务。
- **基本的命令行操作能力** — 你需要编辑配置文件并运行一些命令。
- **大约 15-20 分钟** — 这就是全部所需时间。

您的 I2P router 至少需要 512 MB 内存，在 24/7 全天候运行的服务器上效果最佳。如果您的 router 是首次启动，请给它 10-15 分钟的时间与网络集成，然后再创建 tunnel。

## 理解隧道

I2P 镜像背后的核心概念是 **server tunnel**。其思路如下：

当I2P网络上的某人想要访问您的网站时，他们的请求会通过I2P网络上的多个加密跳跃传输，直到到达您的I2P router。然后您的router将请求传递给**服务器tunnel**，服务器tunnel再将其转发到运行在localhost上的web服务器。您的web服务器响应后，回复会通过加密网络沿着相反的路径返回。

您的Web服务器在处理这些请求时永远不会接触公共互联网——它只与本地主机通信。I2P router处理所有面向网络的事务。

### 您需要哪种 Tunnel 类型？

I2P 为不同情况提供了几种 tunnel 类型：

![tunnel 类型比较 — HTTP 服务器是大多数网站的正确选择](/images/guides/mirroring/tunnel-types.svg)

对于镜像网站，你几乎肯定需要一个 **HTTP Server** tunnel。它专门为网络流量设计，开箱即用地处理头部过滤、压缩和主机名欺骗。其他类型存在是为了特殊用例，如SSH访问、双向应用程序或IRC服务器。

## 第一部分：镜像网站

这是最常见的场景——您有一个现有的明网网站，并希望通过 I2P 使其可访问。以下是整个过程的概览：

![在 I2P 上镜像您的网站的五个步骤](/images/guides/mirroring/steps-overview.svg)

让我们逐步了解每个步骤。

### 步骤 1：为您的 Web 服务器添加 Localhost 监听器

您的明网站点可能已经在端口80和443上运行，对全世界开放。对于I2P，您需要在localhost上创建一个*独立的*监听器，只有I2P tunnel能够访问。这让您可以完全控制I2P版本的外观——您可以删除请求头、屏蔽管理面板，并针对I2P较高的延迟调整缓存设置。

> **快速替代方案：** 如果你不需要任何自定义配置，可以跳过此步骤，直接将 I2P tunnel 指向 `127.0.0.1:80`。但建议使用专用监听器的方法。

选择你的 web 服务器：

#### Nginx

创建新的站点配置：

```bash
sudo nano /etc/nginx/sites-available/i2p-mirror
```
粘贴此配置，将 `yoursite.i2p` 和根路径替换为您自己的值：

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
启用它并重新加载：

```bash
sudo ln -s /etc/nginx/sites-available/i2p-mirror /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```
#### Apache

创建新的站点配置：

```bash
sudo nano /etc/apache2/sites-available/i2p-mirror.conf
```
粘贴此配置：

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
然后添加端口，启用站点，并重新加载：

```bash
echo "Listen 127.0.0.1:8080" | sudo tee -a /etc/apache2/ports.conf
sudo a2ensite i2p-mirror
sudo a2enmod headers
sudo a2dismod status info
sudo apachectl configtest
sudo systemctl reload apache2
```
#### 为什么没有 HSTS？

你会注意到两个配置都明确避免了 `Strict-Transport-Security` 头部。这很关键。HSTS 告诉浏览器只使用 HTTPS，但 I2P 不使用传统的 TLS —— 加密是在网络层处理的。包含 HSTS 会完全锁定访问者，使其无法访问你的 I2P 站点。

### 步骤 2：创建服务器 tunnel

在浏览器中打开 I2P Router Console：

```
`http://127.0.0.1:7657/i2ptunnel/`
```
点击 **"Tunnel Wizard"** 开始创建新的 tunnel。

![I2P Tunnel Wizard startup](/images/guides/mirroring/mirror_02.svg)

选择 **"HTTP Server"** 作为 tunnel 类型并点击 **Next**。

### 步骤 3：配置 Tunnel

填写隧道设置：

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
![Tunnel配置设置](/images/guides/mirroring/mirror_03.png)

点击**"创建"**来生成您的tunnel。I2P将创建一个唯一的加密destination密钥——这将成为您在网络上的永久地址。

### 第 4 步：启动 Tunnel 并等待

在列表中找到您的新 tunnel，然后点击 **"Start"**。您将看到：

- **本地目标地址** — 一个长的 base32 地址，如 `abc123...xyz.b32.i2p`
- **状态** — 应该变为"正在运行"

![Tunnel running status](/images/guides/mirroring/mirror_04.png)

> **请耐心等待！** 首次启动需要 2-5 分钟时间来构建您的 tunnel 并将其 leaseSet 发布到网络中。这是正常现象。

### 步骤 5：测试您的镜像

一旦tunnel显示为运行状态，打开你的I2P配置浏览器并访问你的base32地址。首次页面加载可能需要5-30秒——这对于I2P来说是正常的。

如果页面加载成功，恭喜您——您的网站现在已经在I2P上正式运行了！

### 步骤 6：注册一个人类可读的 .i2p 地址（可选）

你的网站已经可以通过 base32 地址访问，但是 `abc123...xyz.b32.i2p` 并不容易记住。要获得一个简洁的 `.i2p` 域名：

**对于您自己的地址簿** — 访问 `http://127.0.0.1:7657/dns` 并添加您选择的主机名映射到您的目标密钥。

**用于公开发现** — 在 I2P 地址注册表中注册：

1. 访问 `http://stats.i2p/i2p/addkey.html`（在 I2P 内部）
2. 输入您想要的主机名和完整的目标密钥（来自您的 tunnel 详情的 500+ 字符串，以 "AAAA" 结尾）
3. 提交注册

注册完成后，任何订阅了相应地址簿的人都能够通过名称找到您的网站。

## 第二部分：镜像动态应用程序

如果您的站点运行在后端框架（Node.js、Python、Ruby、PHP 等）上而不是静态文件，您需要 Nginx 或 Apache 作为 I2P tunnel 和您的应用程序之间的反向代理。

### 反向代理配置 (Nginx)

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
`X-I2P-Request` 头部让你的应用程序能够检测 I2P 流量，以便在需要时采取不同的行为（例如，禁用需要明网访问的功能）。

### 明网镜像的 URL 重写

如果您的应用程序生成指向明网域名的URL，您需要为I2P访问者重写这些URL：

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
然后创建一个指向 `127.0.0.1:8080` 的 HTTP Server tunnel，就像第一部分中所做的那样。

## 第三部分：镜像 Git 仓库

### Gitea（全功能版）

Gitea 是在 I2P 上托管 Git 的绝佳选择。它具有网络界面、问题跟踪和拉取请求功能——这些在网络上都运行良好。

配置 `/etc/gitea/app.ini`：

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
关键要点：`OFFLINE_MODE = true` 阻止 Gitea 加载外部资源（头像、CDN 资源）。`COOKIE_SECURE = false` 是必需的，因为 I2P 不会以传统方式使用 HTTPS。禁用电子邮件，因为您的 I2P 服务器可能没有配置出站电子邮件。

创建两个tunnel：1. **HTTP Server tunnel** → `127.0.0.1:3000`（Web界面）2. **Standard Server tunnel** → `127.0.0.1:22`（SSH访问用于git推送/拉取 — 可选）

### cgit（轻量级替代方案）

如果你只需要只读浏览和 HTTP 克隆功能，cgit 要轻量得多：

```ini
# /etc/cgitrc
virtual-root=/
clone-url=`http://yourgit.i2p/$CGIT_REPO_URL`
cache-root=/var/cache/cgit
cache-size=1000
scan-path=/srv/git
enable-http-clone=1
```
cgit的激进缓存机制使其特别适合I2P的高延迟环境。

### 通过 I2P 使用 Git 的客户端设置

任何从你的 I2P Git 镜像克隆的人都需要通过 I2P HTTP 代理路由 Git 流量：

```bash
# Tell Git to use the I2P proxy for .i2p domains
git config --global http.http://yourgit.i2p.proxy `http://127.0.0.1:4444`
git config --global http.timeout 300

# Clone (allow for I2P latency)
GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=60 \
    git clone `http://yourgit.i2p/repo`
```
对于大型仓库，浅层克隆在 I2P 上能节省大量时间：

```bash
git clone --depth 1 `http://yourgit.i2p/project`
git fetch --unshallow   # grab full history later if needed
```
## 第四部分：镜像文件托管

### Nextcloud

Nextcloud 可以通过一些配置在 I2P 上运行。编辑 `config/config.php`：

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
运行良好的功能：文件上传和下载、目录浏览、身份验证、公共链接分享和WebDAV。存在问题的功能：桌面同步客户端需要配置SOCKS代理，外部存储后端可能泄露IP地址，与明网Nextcloud实例的联合可能会危及隐私。

### 简单文件服务器

对于无需 Nextcloud 开销的简单文件托管，一个最小的 Python 服务器就能胜任：

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
创建一个指向 `127.0.0.1:8080` 的 HTTP 服务器 tunnel。

## 第五部分：镜像 APIs

### 基础 API 代理

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
### WebSocket 支持

如果您的应用程序使用 WebSockets（聊天应用、实时仪表板等）：

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
请注意，通过 I2P 的 WebSockets 延迟会明显高于明网。对于实时功能，请考虑使用更长的轮询间隔或在客户端进行乐观 UI 更新。

## 安全最佳实践

让你的镜像站点运行起来是简单的部分。保持其安全需要关注一些I2P托管特有的细节。

![I2P镜像站安全检查清单](/images/guides/mirroring/security-checklist.svg)

### 重要规则

**仅绑定到本地主机。** 您的服务应监听 `127.0.0.1`，绝不应监听 `0.0.0.0`。只有 I2P router 应该能够访问您的服务。

**移除身份识别标头。** Web服务器喜欢宣告它们正在运行的软件。在I2P网络上，这是你不想分享的信息。

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
**自托管一切。** 不要从 Google 加载字体，不要从 CDN 加载脚本，也不要从第三方加载分析工具。每个外部资源都是一个离开 I2P 网络的请求，会增加巨大的延迟并可能泄露信息。下载库文件和字体，将它们放在您的服务器上，并在本地提供服务。

**永远不要暴露数据库。** 这应该是不言而喻的，但不要创建指向数据库端口的I2P tunnel。Server tunnel应该只指向Web服务器或应用程序服务器。

## 性能调优

I2P 每个请求会增加 2-10 秒的延迟。这是多跳加密的代价。但通过适当的调优，您的 I2P 镜像站可以感觉出人意料地快速响应。

### 积极缓存

静态资源应该设置较长的缓存生命周期。如果访问者已经加载了您的CSS和图片，他们就不应该再次等待加载这些资源：

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```
### 启用压缩

较小的载荷意味着在I2P有限带宽上的传输更快：

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript
           text/xml application/xml application/xml+rss;
```
### 根据流量调整 Tunnel 数量

更多的 tunnel 意味着更多的并发连接。默认值3对于低流量站点来说是足够的，但如果您遇到拥堵：

```properties
tunnel.0.option.inbound.quantity=5
tunnel.0.option.outbound.quantity=5
tunnel.0.option.inbound.backupQuantity=2
tunnel.0.option.outbound.backupQuantity=2
```
### Tunnel 长度（跳数）

每一跳都会增加延迟，但同时也增加匿名性。请根据您的威胁模型进行选择：

![Tunnel 跳数权衡——更多跳数意味着更高的隐私性但延迟也更高](/images/guides/mirroring/tunnel-hops.svg)

对于服务器身份已知的公共镜像（例如您组织的网站），减少到2跳是一个合理的权衡：

```properties
tunnel.0.option.inbound.length=2
tunnel.0.option.outbound.length=2
```
### 通用 Router 配置建议

- **全天候24/7**运行您的I2P router。运行时间越长，与网络的集成度越好，tunnel性能也越快。
- 将带宽共享设置为至少**256 KB/秒**，但要保持略低于您的实际线路速度。
- 重启后的首次连接可能会很慢（30-90秒）。随着tunnel的建立，这种情况会迅速改善。

## 高级：手动 Tunnel 配置

Router Console 向导工作得很好，但如果你更喜欢直接编辑配置文件——或者需要自动化部署——你可以在 `~/.i2p/i2ptunnel.config`（对于系统安装则是 `/var/lib/i2p/i2p-config/i2ptunnel.config`）中配置 tunnel：

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
更改后重启 I2P：

```bash
sudo systemctl restart i2p
```
从 I2P 0.9.42 开始，您还可以在 `i2ptunnel.config.d/` 中使用单独的配置文件来更清晰地管理多个隧道：

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
## 故障排除

### "我无法访问我的网站"

按顺序完成此检查清单：

**1. Web 服务器是否真的在监听？**

```bash
nc -zv 127.0.0.1 8080
```
如果失败，说明你的网页服务器配置有问题——返回步骤1。

**2. tunnel 是否正在运行？** 访问 `http://127.0.0.1:7657/i2ptunnel/` 并检查状态。如果显示"Starting"超过5分钟，请检查你的 router 的网络集成。

**3. LeaseSet 是否已发布？** 确保在你的隧道选项中没有设置 `i2cp.dontPublishLeaseSet`。如果没有发布 LeaseSet，其他人就无法找到你的隧道。

**4. 你的时钟是否准确？** I2P 要求时间精度在 60 秒以内。检查方法：

```bash
timedatectl status
```
如果您的时钟不准确，I2P 将无法正常建立 tunnel。

### 重启后性能缓慢

这是正常的。重启你的 I2P router 后，给它 10-15 分钟时间重建 tunnel 池并重新整合到网络中。随着更多节点了解你的 router，性能会逐步改善。

同时检查是否为你的 I2NP 端口配置了端口转发（在 Router Console 中查看具体的端口号）。如果没有配置，你的 router 将以"防火墙模式"运行，这会限制性能。

### 其他人访问时出现"地址未找到"错误

访问者需要在他们的地址簿中添加您的地址。请确保您已在公共地址簿中注册，或直接分享您的完整 base32 地址。他们也可以在 `http://127.0.0.1:7657/susidns/subscriptions` 添加更多订阅：

```
`http://stats.i2p/cgi-bin/newhosts.txt`
`http://i2host.i2p/cgi-bin/i2hostetag`
```
### 测试时的超时

I2P 本身具有较高的往返时间。在命令行测试时，请使用扩展的超时设置：

```bash
# curl
curl --connect-timeout 60 --max-time 300 `http://yoursite.i2p/`

# wget
wget --timeout=300 `http://yoursite.i2p/`
```
### 读取日志

如果其他方法都无效，请检查 I2P router 日志中的错误信息：

```bash
# System service
sudo journalctl -u i2p -f

# Or directly
tail -f ~/.i2p/logs/log-router-0.txt
```
## 备份您的密钥

这是您绝对不能跳过的一件事。您的tunnel私钥文件（I2P配置目录中的`.dat`文件）决定了您的服务在网络上的永久地址。如果丢失了这些文件，您就永久丢失了您的I2P地址。没有恢复、重置或支持工单可以帮助您。您只能使用新地址重新开始。

现在备份它们：

```bash
# User installation
tar -czf tunnel-keys-backup.tar.gz ~/.i2p/*.dat

# System installation
sudo tar -czf tunnel-keys-backup.tar.gz /var/lib/i2p/i2p-config/*.dat
```
将备份存储在安全的地方，并且不要放在服务器上。

## 完成

就是这样。您的服务现在可以在普通互联网和I2P网络上同时使用。您为人们提供了一种私密访问您内容的方式——一种他们的身份保持私密的方式。

如果你遇到问题或想要更多参与，以下是寻找社区的地方：

- **论坛：** [i2pforum.net](https://i2pforum.net)
- **IRC：** 各种网络上的 #i2p
- **开发：** [i2pgit.org](https://i2pgit.org)
- **StormyCloud：** [stormycloud.org](https://www.stormycloud.org)

---

*本指南由 [StormyCloud Inc](https://www.stormycloud.org) 为 I2P 社区创建。*
