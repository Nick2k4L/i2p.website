---
title: "Tạo Bản Sao Dịch Vụ của Bạn trên I2P"
description: "Hướng dẫn thân thiện cho người mới bắt đầu tạo các trang web, kho Git, API và nhiều thứ khác có sẵn trên mạng I2P — với hướng dẫn từng bước và sơ đồ minh họa"
slug: "mirroring-guide"
lastUpdated: "2025-02"
accurateFor: "2.10.0"
---

Bạn đã có một website trên internet thông thường. Giờ bạn muốn làm cho nó có thể truy cập được trên I2P - để mọi người có thể truy cập một cách riêng tư, mà không tiết lộ danh tính hay vị trí của họ. Đó chính là nội dung mà hướng dẫn này sẽ trình bày.

Mirroring không thay thế trang web hiện có của bạn. Nó thêm một lối vào thứ hai — một lối vào riêng tư — thông qua mạng I2P. Trang web clearnet của bạn vẫn tiếp tục hoạt động chính xác như trước.

![Cách thức hoạt động của mirroring I2P — máy chủ của bạn có thêm một lối vào thứ hai, riêng tư thông qua mạng I2P](/images/guides/mirroring/how-mirroring-works.svg)

## Tại sao Mirror đến I2P?

Có một số lý do thực tế để sao chép các dịch vụ của bạn:

**Quyền riêng tư cho người truy cập của bạn.** Mọi người có thể truy cập nội dung của bạn mà không cần tiết lộ địa chỉ IP của họ. Lưu lượng truy cập giữa họ và dịch vụ của bạn được mã hóa qua nhiều chặng — cả bạn và bất kỳ ai theo dõi mạng đều không thể xác định ai đang truy cập.

**Khả năng chống kiểm duyệt.** Nếu trang web của bạn bị chặn ở một số khu vực bằng cách lọc DNS, chặn IP, hoặc các phương thức khác, bản sao I2P vẫn có thể truy cập được. Nó không phụ thuộc vào DNS hoặc định tuyến IP thông thường.

**Khả năng phục hồi.** Một mirror I2P tăng thêm tính dự phòng. Nếu tên miền của bạn bị tịch thu hoặc CDN loại bỏ bạn, phiên bản I2P vẫn hoạt động miễn là máy chủ của bạn vẫn đang chạy.

**Hỗ trợ mạng lưới.** Mọi dịch vụ trên I2P đều làm cho mạng lưới trở nên hữu ích hơn và giúp phát triển hệ sinh thái.

## Những Gì Bạn Cần

Trước khi bắt đầu, hãy đảm bảo bạn có:

- **Một I2P router đang chạy** trên máy chủ của bạn (phiên bản Java). Nếu bạn chưa có, hãy làm theo [Hướng dẫn Cài đặt I2P](/downloads/) trước.
- **Website hoặc dịch vụ của bạn đã hoạt động** — nó phải đang phục vụ nội dung trên máy chủ của bạn.
- **Kiến thức cơ bản về dòng lệnh** — bạn sẽ cần chỉnh sửa file cấu hình và chạy một vài lệnh.
- **Khoảng 15–20 phút** — đó là tất cả thời gian cần thiết.

Router I2P của bạn cần ít nhất 512 MB RAM và hoạt động tốt nhất trên máy chủ có thời gian hoạt động 24/7. Nếu router của bạn mới khởi động lần đầu tiên, hãy chờ 10–15 phút để nó tích hợp với mạng trước khi tạo tunnel.

## Hiểu về Tunnel

Khái niệm cốt lõi đằng sau việc tạo mirror I2P là **server tunnel**. Ý tưởng như sau:

Khi ai đó trên I2P muốn truy cập trang web của bạn, yêu cầu của họ sẽ đi qua nhiều hop được mã hóa khác nhau trên mạng I2P cho đến khi nó đến router I2P của bạn. Router của bạn sau đó sẽ chuyển yêu cầu đến một **server tunnel**, tunnel này sẽ chuyển tiếp yêu cầu đến máy chủ web của bạn đang chạy trên localhost. Máy chủ web của bạn phản hồi, và câu trả lời sẽ đi theo đường ngược lại qua mạng được mã hóa.

Máy chủ web của bạn không bao giờ kết nối trực tiếp với internet công cộng cho các yêu cầu này — nó chỉ giao tiếp với localhost. I2P router xử lý mọi thứ liên quan đến mạng.

### Bạn Cần Loại Tunnel Nào?

I2P cung cấp nhiều loại tunnel khác nhau cho các tình huống khác nhau:

![So sánh các loại tunnel — HTTP Server là lựa chọn phù hợp nhất cho hầu hết các website](/images/guides/mirroring/tunnel-types.svg)

Để tạo bản sao của một website, bạn chắc chắn sẽ muốn sử dụng tunnel **HTTP Server**. Nó được thiết kế đặc biệt cho lưu lượng web và xử lý việc lọc header, nén dữ liệu, và giả mạo hostname một cách tự động. Các loại khác tồn tại cho những trường hợp sử dụng chuyên biệt như truy cập SSH, ứng dụng hai chiều, hoặc server IRC.

## Phần 1: Sao chép một Trang web

Đây là kịch bản phổ biến nhất — bạn có một trang web clearnet hiện tại và muốn làm cho nó có thể truy cập qua I2P. Dưới đây là quy trình tổng quan:

![Năm bước để mirror trang web của bạn trên I2P](/images/guides/mirroring/steps-overview.svg)

Hãy cùng đi qua từng bước.

### Bước 1: Thêm Localhost Listener vào Web Server của bạn

Trang web clearnet của bạn có thể đã đang chạy trên cổng 80 và 443, mở cho toàn thế giới. Đối với I2P, bạn sẽ tạo một *listener riêng biệt* trên localhost mà chỉ tunnel I2P mới có thể truy cập được. Điều này cho phép bạn kiểm soát hoàn toàn giao diện phiên bản I2P — bạn có thể loại bỏ header, chặn bảng điều khiển quản trị, và tinh chỉnh bộ nhớ đệm cho độ trễ cao hơn của I2P.

> **Phương án nhanh:** Nếu bạn không cần tùy chỉnh gì, bạn có thể bỏ qua bước này và trỏ I2P tunnel trực tiếp tới `127.0.0.1:80`. Nhưng cách tiếp cận listener chuyên dụng được khuyến nghị.

Chọn web server của bạn:

#### Nginx

Tạo cấu hình trang web mới:

```bash
sudo nano /etc/nginx/sites-available/i2p-mirror
```
Dán cấu hình này, thay thế `yoursite.i2p` và đường dẫn gốc bằng các giá trị của bạn:

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
Bật nó lên và tải lại:

```bash
sudo ln -s /etc/nginx/sites-available/i2p-mirror /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```
#### Apache

Tạo cấu hình site mới:

```bash
sudo nano /etc/apache2/sites-available/i2p-mirror.conf
```
Dán cấu hình này:

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
Sau đó thêm port, kích hoạt trang web, và tải lại:

```bash
echo "Listen 127.0.0.1:8080" | sudo tee -a /etc/apache2/ports.conf
sudo a2ensite i2p-mirror
sudo a2enmod headers
sudo a2dismod status info
sudo apachectl configtest
sudo systemctl reload apache2
```
#### Tại sao không có HSTS?

Bạn sẽ nhận thấy cả hai cấu hình đều tránh rõ ràng các header `Strict-Transport-Security`. Điều này rất quan trọng. HSTS yêu cầu trình duyệt chỉ sử dụng HTTPS, nhưng I2P không sử dụng TLS truyền thống — mã hóa được xử lý ở tầng mạng thay vào đó. Việc bao gồm HSTS sẽ khiến người dùng hoàn toàn không thể truy cập vào trang I2P của bạn.

### Bước 2: Tạo Server Tunnel

Mở I2P Router Console trong trình duyệt của bạn:

```
http://127.0.0.1:7657/i2ptunnel/
```
Nhấp vào **"Tunnel Wizard"** để bắt đầu tạo một tunnel mới.

![I2P Tunnel Wizard khởi động](/images/guides/mirroring/mirror_02.svg)

Chọn **"HTTP Server"** làm loại tunnel và nhấp **Next**.

### Bước 3: Cấu hình Tunnel

Điền vào các cài đặt tunnel:

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
![Cài đặt cấu hình tunnel](/images/guides/mirroring/mirror_03.png)

Nhấp **"Create"** để tạo tunnel của bạn. I2P sẽ tạo một khóa đích mã hóa duy nhất — đây sẽ trở thành địa chỉ vĩnh viễn của bạn trên mạng.

### Bước 4: Khởi động Tunnel và Chờ đợi

Tìm tunnel mới của bạn trong danh sách và nhấp **"Start"**. Bạn sẽ thấy:

- **Local Destination** — một địa chỉ base32 dài như `abc123...xyz.b32.i2p`
- **Status** — sẽ thay đổi thành "Running"

![Trạng thái hoạt động tunnel](/images/guides/mirroring/mirror_04.png)

> **Hãy kiên nhẫn!** Lần khởi động đầu tiên mất 2–5 phút trong khi tunnel của bạn được xây dựng và công bố các leaseSet của nó lên mạng. Điều này là bình thường.

### Bước 5: Kiểm tra Mirror của bạn

Khi tunnel hiển thị đang chạy, hãy mở trình duyệt đã cấu hình I2P của bạn và truy cập địa chỉ base32 của bạn. Lần tải trang đầu tiên có thể mất 5–30 giây — điều này bình thường đối với I2P.

Nếu trang web tải được, chúc mừng — trang web của bạn hiện đã hoạt động trên I2P!

### Bước 6: Đăng ký Địa chỉ .i2p Dễ đọc (Tùy chọn)

Trang web của bạn đã có thể truy cập qua địa chỉ base32, nhưng `abc123...xyz.b32.i2p` không thực sự dễ nhớ. Để có được tên miền `.i2p` dễ nhớ:

**Đối với addressbook của riêng bạn** — truy cập `http://127.0.0.1:7657/dns` và thêm tên máy chủ bạn chọn được ánh xạ tới destination key của bạn.

**Để được khám phá công khai** — đăng ký với sổ đăng ký địa chỉ I2P:

1. Truy cập `http://stats.i2p/i2p/addkey.html` (bên trong I2P)
2. Nhập tên miền mong muốn và khóa destination đầy đủ của bạn (chuỗi 500+ ký tự từ chi tiết tunnel, kết thúc bằng "AAAA")
3. Gửi để đăng ký

Sau khi đăng ký, bất kỳ ai có đăng ký sổ địa chỉ phù hợp sẽ có thể tìm thấy trang web của bạn theo tên.

## Phần 2: Tạo Mirror cho Ứng dụng Động

Nếu trang web của bạn chạy trên một framework backend (Node.js, Python, Ruby, PHP, v.v.) thay vì các file tĩnh, bạn cần Nginx hoặc Apache làm reverse proxy giữa I2P tunnel và ứng dụng của bạn.

### Cấu hình Reverse Proxy (Nginx)

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
Header `X-I2P-Request` cho phép ứng dụng của bạn phát hiện lưu lượng I2P nếu cần hoạt động khác biệt (ví dụ, vô hiệu hóa các tính năng yêu cầu truy cập clearnet).

### Viết Lại URL cho Clearnet Mirrors

Nếu ứng dụng của bạn tạo ra các URL trỏ đến tên miền clearnet của bạn, bạn sẽ muốn viết lại chúng cho những người truy cập I2P:

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
Sau đó tạo một HTTP Server tunnel trỏ đến `127.0.0.1:8080`, giống như trong Phần 1.

## Phần 3: Tạo Mirror cho Git Repository

### Gitea (Đầy đủ tính năng)

Gitea là một lựa chọn tuyệt vời để lưu trữ Git qua I2P. Nó có giao diện web, theo dõi vấn đề và pull request — tất cả đều hoạt động tốt trên mạng.

Cấu hình `/etc/gitea/app.ini`:

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
Các điểm chính: `OFFLINE_MODE = true` ngăn Gitea tải các tài nguyên bên ngoài (avatar, tài sản CDN). `COOKIE_SECURE = false` là cần thiết vì I2P không sử dụng HTTPS theo nghĩa truyền thống. Tắt email vì máy chủ I2P của bạn có thể chưa được cấu hình email gửi đi.

Tạo hai tunnel: 1. **HTTP Server tunnel** → `127.0.0.1:3000` (giao diện web) 2. **Standard Server tunnel** → `127.0.0.1:22` (truy cập SSH cho git push/pull — tùy chọn)

### cgit (Lựa chọn thay thế nhẹ)

Nếu bạn chỉ cần duyệt chỉ đọc và sao chép HTTP, cgit nhẹ hơn nhiều:

```ini
# /etc/cgitrc
virtual-root=/
clone-url=http://yourgit.i2p/$CGIT_REPO_URL
cache-root=/var/cache/cgit
cache-size=1000
scan-path=/srv/git
enable-http-clone=1
```
Tính năng cache tích cực của cgit làm cho nó đặc biệt phù hợp với độ trễ cao hơn của I2P.

### Thiết lập phía Client cho Git qua I2P

Bất kỳ ai clone từ Git mirror I2P của bạn cần định tuyến lưu lượng Git qua I2P HTTP proxy:

```bash
# Tell Git to use the I2P proxy for .i2p domains
git config --global http.http://yourgit.i2p.proxy http://127.0.0.1:4444
git config --global http.timeout 300

# Clone (allow for I2P latency)
GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=60 \
    git clone http://yourgit.i2p/repo
```
Đối với các repo lớn, shallow clone tiết kiệm rất nhiều thời gian qua I2P:

```bash
git clone --depth 1 http://yourgit.i2p/project
git fetch --unshallow   # grab full history later if needed
```
## Phần 4: Nhân Bản Dịch Vụ Lưu Trữ Tệp

### Nextcloud

Nextcloud hoạt động qua I2P với một số cấu hình. Chỉnh sửa `config/config.php`:

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
Những tính năng hoạt động tốt: tải file lên và xuống, duyệt thư mục, xác thực, chia sẻ liên kết công khai, và WebDAV. Những gì không hoạt động tốt: các ứng dụng đồng bộ trên máy tính cần cấu hình SOCKS proxy, các backend lưu trữ bên ngoài có thể làm rò rỉ địa chỉ IP, và việc kết nối với các máy chủ Nextcloud trên clearnet có thể làm tổn hại đến quyền riêng tư.

### Máy chủ tệp đơn giản

Để lưu trữ tệp tin đơn giản mà không cần sự phức tạp của Nextcloud, một máy chủ Python tối giản có thể đảm nhận công việc này:

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
Tạo một tunnel HTTP Server trỏ đến `127.0.0.1:8080`.

## Phần 5: API Nhân Bản

### Proxy API Cơ bản

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
### Hỗ trợ WebSocket

Nếu ứng dụng của bạn sử dụng WebSockets (ứng dụng chat, bảng điều khiển trực tiếp, v.v.):

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
Lưu ý rằng WebSockets qua I2P sẽ có độ trễ cao hơn đáng kể so với clearnet. Đối với các tính năng thời gian thực, hãy cân nhắc sử dụng khoảng thời gian polling dài hơn hoặc cập nhật UI lạc quan ở phía client.

## Các Thực Hành Bảo Mật Tốt Nhất

Việc thiết lập mirror hoạt động là phần dễ dàng. Việc giữ cho nó an toàn đòi hỏi chú ý đến một số chi tiết đặc biệt của việc hosting trên I2P.

![Danh sách kiểm tra bảo mật cho I2P mirrors](/images/guides/mirroring/security-checklist.svg)

### Các Quy Tắc Lớn

**Chỉ bind tới localhost.** Dịch vụ của bạn nên lắng nghe trên `127.0.0.1`, không bao giờ trên `0.0.0.0`. I2P router là thứ duy nhất có thể truy cập được dịch vụ của bạn.

**Loại bỏ các header nhận dạng.** Các web server thích thông báo phần mềm mà chúng đang chạy. Trên I2P, đây là thông tin mà bạn không muốn chia sẻ.

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
**Tự host mọi thứ.** Đừng tải font từ Google, script từ CDN, hoặc analytics từ bên thứ ba. Mỗi tài nguyên bên ngoài là một yêu cầu thoát khỏi mạng I2P, làm tăng độ trễ rất lớn và có thể rò rỉ thông tin. Hãy tải xuống các thư viện và font, đặt chúng trên máy chủ của bạn và phục vụ chúng cục bộ.

**Không bao giờ để lộ cơ sở dữ liệu.** Điều này là hiển nhiên, nhưng đừng tạo I2P tunnel tới các cổng cơ sở dữ liệu của bạn. Server tunnel chỉ nên trỏ tới web server hoặc application server.

## Điều chỉnh Hiệu suất

I2P thêm 2–10 giây độ trễ cho mỗi yêu cầu. Đó là cái giá phải trả cho mã hóa multi-hop. Nhưng với việc tinh chỉnh phù hợp, mirror I2P của bạn có thể cảm thấy nhanh một cách đáng ngạc nhiên.

### Cache Tích Cực

Các tài nguyên tĩnh nên có thời gian lưu cache dài. Nếu người dùng đã tải CSS và hình ảnh của bạn, họ không nên phải chờ tải lại chúng:

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|svg)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```
### Bật nén dữ liệu

Payload nhỏ hơn có nghĩa là truyền tải nhanh hơn trên băng thông hạn chế của I2P:

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript
           text/xml application/xml application/xml+rss;
```
### Điều chỉnh Số lượng Tunnel cho Lưu lượng

Nhiều tunnel hơn có nghĩa là nhiều kết nối đồng thời hơn. Mặc định là 3 tunnel thích hợp cho các trang web có lưu lượng thấp, nhưng nếu bạn gặp tình trạng tắc nghẽn:

```properties
tunnel.0.option.inbound.quantity=5
tunnel.0.option.outbound.quantity=5
tunnel.0.option.inbound.backupQuantity=2
tunnel.0.option.outbound.backupQuantity=2
```
### Độ dài Tunnel (Hops)

Mỗi hop thêm vào độ trễ nhưng cũng tăng tính ẩn danh. Hãy lựa chọn dựa trên mô hình mối đe dọa của bạn:

![Sự đánh đổi tunnel hops — nhiều hops hơn có nghĩa là riêng tư hơn nhưng độ trễ cao hơn](/images/guides/mirroring/tunnel-hops.svg)

Đối với một mirror công khai mà danh tính của server đã được biết (ví dụ như trang web của tổ chức bạn), việc giảm xuống còn 2 hop là một sự đánh đổi hợp lý:

```properties
tunnel.0.option.inbound.length=2
tunnel.0.option.outbound.length=2
```
### Các Mẹo Router Chung

- Chạy I2P router của bạn **24/7**. Càng chạy lâu, router càng được tích hợp tốt với mạng, và tunnel của bạn hoạt động càng nhanh.
- Đặt băng thông chia sẻ ít nhất **256 KB/giây**, nhưng giữ nó hơi thấp hơn tốc độ đường truyền thực tế của bạn.
- Hãy chuẩn bị tinh thần cho những kết nối đầu tiên sau khi khởi động lại sẽ chậm (30–90 giây). Điều này sẽ cải thiện nhanh chóng khi các tunnel được xây dựng.

## Nâng cao: Cấu hình Tunnel Thủ công

Trình hướng dẫn Router Console hoạt động rất tốt, nhưng nếu bạn thích chỉnh sửa trực tiếp các tệp cấu hình — hoặc cần tự động hóa việc triển khai — bạn có thể cấu hình tunnel trong `~/.i2p/i2ptunnel.config` (hoặc `/var/lib/i2p/i2p-config/i2ptunnel.config` cho các cài đặt hệ thống):

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
Khởi động lại I2P sau khi thay đổi:

```bash
sudo systemctl restart i2p
```
Từ I2P 0.9.42, bạn cũng có thể sử dụng các tệp cấu hình riêng lẻ trong `i2ptunnel.config.d/` để quản lý nhiều tunnel một cách gọn gàng hơn:

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
## Khắc phục sự cố

### "Tôi không thể truy cập trang web của mình"

Thực hiện theo danh sách kiểm tra này theo thứ tự:

**1. Web server có thực sự đang lắng nghe không?**

```bash
nc -zv 127.0.0.1 8080
```
Nếu điều này thất bại, cấu hình web server của bạn có vấn đề — hãy quay lại Bước 1.

**2. Tunnel có đang chạy không?** Truy cập `http://127.0.0.1:7657/i2ptunnel/` và kiểm tra trạng thái. Nếu nó hiển thị "Starting" trong hơn 5 phút, hãy kiểm tra tích hợp mạng của router.

**3. LeaseSet đã được công bố chưa?** Đảm bảo `i2cp.dontPublishLeaseSet` KHÔNG được thiết lập trong các tùy chọn tunnel của bạn. Nếu không có LeaseSet được công bố, không ai có thể tìm thấy tunnel của bạn.

**4. Đồng hồ của bạn có chính xác không?** I2P yêu cầu thời gian chính xác trong vòng 60 giây. Kiểm tra bằng:

```bash
timedatectl status
```
Nếu đồng hồ của bạn bị sai giờ, I2P sẽ gặp khó khăn trong việc xây dựng tunnel.

### Hiệu suất chậm sau khi khởi động lại

Điều này là bình thường. Sau khi khởi động lại I2P router của bạn, hãy đợi 10–15 phút để nó xây dựng lại tunnel pools và tái tích hợp với mạng lưới. Hiệu suất sẽ cải thiện khi có nhiều peer hơn biết về router của bạn.

Cũng hãy kiểm tra xem chuyển tiếp cổng đã được cấu hình cho cổng I2NP của bạn chưa (kiểm tra Router Console để biết số cổng cụ thể). Nếu không có nó, router của bạn sẽ hoạt động ở chế độ "firewalled", điều này sẽ hạn chế hiệu suất.

### Lỗi "Address not found" khi người khác truy cập

Khách truy cập cần có địa chỉ của bạn trong sổ địa chỉ của họ. Hãy đảm bảo bạn đã đăng ký với một sổ địa chỉ công khai, hoặc chia sẻ trực tiếp địa chỉ base32 đầy đủ của bạn. Họ cũng có thể thêm nhiều đăng ký hơn tại `http://127.0.0.1:7657/susidns/subscriptions`:

```
http://stats.i2p/cgi-bin/newhosts.txt
http://i2host.i2p/cgi-bin/i2hostetag
```
### Hết thời gian chờ khi kiểm tra

I2P có thời gian round-trip cao hơn do bản chất của nó. Khi kiểm tra từ command line, hãy sử dụng timeout mở rộng:

```bash
# curl
curl --connect-timeout 60 --max-time 300 http://yoursite.i2p/

# wget
wget --timeout=300 http://yoursite.i2p/
```
### Đọc các log

Nếu không có cách nào khác hiệu quả, hãy kiểm tra nhật ký I2P router để tìm lỗi:

```bash
# System service
sudo journalctl -u i2p -f

# Or directly
tail -f ~/.i2p/logs/log-router-0.txt
```
## Sao Lưu Khóa Của Bạn

Đây là điều duy nhất mà bạn tuyệt đối không được bỏ qua. Các tệp khóa riêng của tunnel (các tệp `.dat` trong thư mục cấu hình I2P của bạn) là thứ cung cấp cho dịch vụ của bạn một địa chỉ cố định trên mạng. Nếu bạn mất chúng, bạn sẽ mất địa chỉ I2P của mình — vĩnh viễn. Không có cách khôi phục, không có đặt lại, không có hỗ trợ kỹ thuật. Bạn sẽ phải bắt đầu lại từ đầu với một địa chỉ mới.

Sao lưu chúng ngay bây giờ:

```bash
# User installation
tar -czf tunnel-keys-backup.tar.gz ~/.i2p/*.dat

# System installation
sudo tar -czf tunnel-keys-backup.tar.gz /var/lib/i2p/i2p-config/*.dat
```
Lưu trữ bản sao lưu ở nơi an toàn và ngoài máy chủ.

## Bạn Đã Hoàn Thành

Vậy là xong. Dịch vụ của bạn giờ đây đã có sẵn trên cả internet thông thường và mạng I2P. Bạn đang mang lại cho mọi người một cách riêng tư để truy cập nội dung của bạn — nơi mà danh tính của họ vẫn thuộc về chính họ.

Nếu bạn gặp phải vấn đề hoặc muốn tham gia nhiều hơn, đây là nơi để tìm cộng đồng:

- **Diễn đàn:** [i2pforum.net](https://i2pforum.net)
- **IRC:** #i2p trên các mạng khác nhau
- **Phát triển:** [i2pgit.org](https://i2pgit.org)
- **StormyCloud:** [stormycloud.org](https://www.stormycloud.org)

---

*Hướng dẫn được tạo bởi [StormyCloud Inc](https://www.stormycloud.org) cho cộng đồng I2P.*
