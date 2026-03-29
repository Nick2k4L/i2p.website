---
title: "Bắt đầu với I2P: Hướng dẫn đầy đủ cho người mới bắt đầu"
description: "Bắt đầu với I2P: Hướng dẫn đầy đủ cho người mới bắt đầu"
slug: "gettingstarted"
lastUpdated: "2026-03"
accurateFor: "2.11.0"
---

**I2P là một mạng ngang hàng ẩn danh được mã hóa hoàn toàn, chạy "bên trong" internet**, và phiên bản triển khai bằng Java từ i2p.net vẫn là cách tiêu chuẩn để sử dụng nó. Không giống như Tor, vốn chủ yếu ẩn danh hóa việc truy cập vào web thông thường, I2P tạo ra một mạng lưới hoàn toàn độc lập gồm các dịch vụ ẩn, trang web, email, trò chuyện và chia sẻ tệp tin.

---

## Điều gì xảy ra ngay khi bạn khởi động I2P

Sau khi cài đặt, I2P sẽ khởi chạy một ứng dụng web cục bộ gọi là **bảng điều khiển bộ định tuyến** tại `http://127.0.0.1:7657`. Đây là trung tâm điều khiển của bạn, chạy hoàn toàn trên máy bạn và được liên kết với localhost để đảm bảo an toàn. Khi khởi động lần đầu, một **trình hướng dẫn thiết lập** sẽ hướng dẫn bạn qua việc chọn ngôn ngữ, chọn giao diện (tối hoặc sáng), và một bài kiểm tra băng thông tự động kéo dài khoảng một phút sử dụng dịch vụ đo lường bên ngoài M-Lab. Sau đó, bạn sẽ thiết lập tỷ lệ phần trăm băng thông muốn chia sẻ với mạng.

![Trình hướng dẫn thiết lập I2P - Chọn ngôn ngữ](/images/guides/quickstart/wizard-language-selection.webp)

Sau khi trình hướng dẫn hoàn tất, bộ định tuyến bắt đầu quá trình **khởi động ban đầu** được gọi là "reseeding" (tái cấp nguồn). Bộ định tuyến của bạn tải xuống khoảng **100 bản ghi RouterInfo** từ các máy chủ reseed được tích hợp sẵn thông qua HTTPS, qua đó có được danh sách ban đầu các nút ngang hàng. Từ đó, nó bắt đầu xây dựng các **tunnel thăm dò** để khám phá thêm các nút ngang hàng khác và cập nhật bản sao cục bộ của cơ sở dữ liệu mạng (gọi là "netDb"). Trong vài phút đầu tiên, bạn sẽ thấy thông báo "Rejecting tunnels: starting up" (Từ chối các tunnel: đang khởi động). Điều này là bình thường.

![I2P Reseeding - Bootstrapping](/images/guides/quickstart/reseed-bootstrapping.webp)

**Hãy chờ từ 3–10 phút** trước khi bộ định tuyến của bạn có thể sử dụng được, và thời gian lâu hơn đáng kể — vài ngày hoạt động liên tục — trước khi đạt hiệu suất tối đa. Thanh bên bảng điều khiển bộ định tuyến hiển thị số lượng nút ngang hàng của bạn dưới dạng "Đang hoạt động x/y", trong đó x là số nút bạn đã trao đổi tin nhắn gần đây và y là tổng số nút đã được phát hiện. Khi bạn thấy có **10 nút hoạt động trở lên**, bộ định tuyến của bạn đã kết nối ổn định. Việc quan trọng nhất mà người dùng mới có thể làm là **giữ bộ định tuyến hoạt động liên tục**. Sau mỗi lần tắt máy, các nút khác sẽ ghi nhận bộ định tuyến của bạn là không đáng tin cậy trong ít nhất 24 giờ, do đó việc khởi động lại thường xuyên sẽ làm giảm nghiêm trọng hiệu suất.

![Bảng điều khiển Router I2P](/images/guides/quickstart/router-console-dashboard.png)

---

## Cấu hình trình duyệt của bạn cho I2P

Không giống như Mạng Tor, I2P không đi kèm với trình duyệt chuyên dụng. Để truy cập các trang web I2P (miền giả cấp cao nhất `.i2p`), bạn cần cấu hình cài đặt proxy của trình duyệt để định tuyến lưu lượng qua proxy HTTP I2P trên cổng **4444**.

**Con đường dễ dàng nhất cho người dùng Windows** là **Gói Cài đặt Dễ dàng**, gói này bao gồm Java, bộ định tuyến và một hồ sơ Firefox đã được cấu hình sẵn cùng tiện ích mở rộng "I2P trong Chế độ Duyệt Riêng tư". Nó loại bỏ toàn bộ việc cấu hình proxy thủ công. Từ lúc tải về đến khi duyệt các trang web I2P chỉ mất khoảng bốn phút. Một gói Cài đặt Dễ dàng cho macOS (Apple Silicon) cũng đang có sẵn ở phiên bản beta. Nếu bạn đang sử dụng Gói Cài đặt Dễ dàng, bạn có thể bỏ qua các bước thiết lập thủ công bên dưới.

### Firefox (Được khuyến nghị)

Rất khuyến khích sử dụng Firefox vì nó có cài đặt proxy riêng biệt, độc lập với hệ điều hành của bạn - Chrome và Edge sử dụng cài đặt proxy toàn hệ thống, ảnh hưởng đến tất cả các ứng dụng.

**Bước 1.** Mở menu Firefox (biểu tượng hamburger) và nhấp vào **Cài đặt**.

![Firefox - Mở Cài đặt](/images/guides/browser-config/accessi2p_3.png)

**Bước 2.** Tìm kiếm **proxy** trong thanh tìm kiếm cài đặt, sau đó nhấp vào **Cài đặt...** bên cạnh Cài đặt Mạng.

![Firefox - Tìm kiếm proxy](/images/guides/browser-config/accessi2p_4.png)

**Bước 3.** Chọn **Cấu hình proxy thủ công**, nhập `127.0.0.1` vào ô HTTP Proxy và `4444` vào cổng, sau đó nhấn **OK**.

![Firefox - Cấu hình proxy thủ công](/images/guides/browser-config/accessi2p_5.png)

Sau khi thiết lập proxy, nên thực hiện một số điều chỉnh trong `about:config`:

- Đặt `media.peerConnection.ice.proxy_only` thành **true** (ngăn rò rỉ WebRTC)
- Đặt `keyword.enabled` thành **false** (ngăn chuyển hướng công cụ tìm kiếm trên các địa chỉ .i2p)
- Tạo một giá trị boolean `browser.fixup.domainsuffixwhitelist.i2p` và đặt thành **true** (thông báo cho Firefox rằng `.i2p` là một hậu tố tên miền hợp lệ)

Một lỗi phổ biến khiến người mới bắt đầu gặp khó khăn: luôn gõ `http://` trước các địa chỉ `.i2p`. Hầu hết các trang web I2P không sử dụng HTTPS (vì I2P đã mã hóa toàn bộ lưu lượng từ đầu đến cuối), và nếu thiếu phần tiền tố này, Firefox sẽ chuyển hướng bạn đến một công cụ tìm kiếm.

### Chrome / Edge (Windows)

Lưu ý: Chrome và Edge sử dụng cài đặt proxy của hệ điều hành bạn, điều này ảnh hưởng đến **tất cả** các ứng dụng trên hệ thống.

**Bước 1.** Mở menu Chrome và nhấp vào **Cài đặt**.

![Chrome - Mở Cài đặt](/images/guides/browser-config/accessi2p_6.png)

**Bước 2.** Tìm kiếm **proxy**, sau đó nhấp vào **Mở cài đặt proxy của máy tính**.

![Chrome - Tìm kiếm proxy](/images/guides/browser-config/accessi2p_7.png)

**Bước 3.** Trong phần **Thiết lập proxy thủ công**, nhấp vào **Thiết lập** kế bên mục "Sử dụng máy chủ proxy."

![Windows - Cài đặt Proxy](/images/guides/browser-config/accessi2p_8.png)

**Bước 4.** Bật tùy chọn **Sử dụng máy chủ proxy**, nhập `127.0.0.1` làm địa chỉ IP Proxy và `4444` làm cổng, sau đó nhấn **Lưu**.

![Windows - Chỉnh sửa máy chủ proxy](/images/guides/browser-config/accessi2p_9.png)

### Safari (macOS)

**Bước 1.** Truy cập **Safari → Cài đặt → Nâng cao** và nhấp vào **Thay đổi cài đặt...** bên cạnh phần Proxy.

![Safari - Cài đặt nâng cao](/images/guides/browser-config/accessi2p_1.png)

**Bước 2.** Bật **Web proxy (HTTP)**, nhập `127.0.0.1` làm máy chủ và `4444` làm cổng, sau đó nhấn **OK**.

![Cài đặt proxy web trên macOS](/images/guides/browser-config/accessi2p_2.png)

---

## Hiểu bảng điều khiển bảng điều khiển router

Bảng điều khiển router tại `127.0.0.1:7657` hiển thị một số chỉ báo chính cho biết hiệu suất hoạt động của nút I2P của bạn. **Thanh bên** cho thấy phiên bản I2P, thời gian hoạt động, mức sử dụng băng thông (vào/ra), số lượng peer đang hoạt động và trạng thái tunnel. Khi mục "Shared Clients" chuyển sang màu xanh lá, router của bạn đã được tích hợp và sẵn sàng hoạt động.

![Bảng điều khiển Router - Khách hàng chia sẻ màu xanh](/images/guides/quickstart/shared-clients-green.png)

**Biểu đồ băng thông** hiển thị tốc độ truyền dữ liệu theo thời gian thực. Giá trị mặc định khá tiết kiệm — **96 KBps tải xuống và 40 KBps tải lên**, chỉ chia sẻ 48 KBps — và tài liệu chính thức khuyến nghị mạnh mẽ việc tăng các giá trị này. Hãy truy cập `http://127.0.0.1:7657/config` (hoặc nhấp vào "Configure Bandwidth" trong bảng điều khiển) để tăng giới hạn của bạn. Việc tăng băng thông chia sẻ không chỉ cải thiện hiệu suất của chính bạn mà còn góp phần nâng cao sức khỏe của toàn bộ mạng. Nếu đặt băng thông chia sẻ dưới mức **12 KBps**, bộ định tuyến của bạn sẽ chuyển sang "chế độ ẩn", khiến bạn không thể tham gia vào lưu lượng chia sẻ. Khi đạt mức **128 KBps trở lên**, bộ định tuyến của bạn có thể được nâng cấp lên trạng thái floodfill, nghĩa là nó sẽ hỗ trợ duy trì bảng băm phân tán (distributed hash table).

![Cấu hình Băng thông](/images/guides/quickstart/bandwidth-config.png)

Phần **trạng thái tunnel** hiển thị các tunnel đang tham gia - lưu lượng bạn đang chuyển tiếp cho người khác. Trên 90% các router I2P mặc định chuyển tiếp lưu lượng tham gia này. Việc này vừa tạo ra lưu lượng che giấu để bảo vệ ẩn danh cho bạn, vừa là đóng góp của bạn cho mạng lưới. Các tunnel hết hạn sau mỗi 10 phút và được xây dựng lại tự động.

![Trình quản lý I2PTunnel](/images/guides/quickstart/tunnel-manager.png)

**Trình quản lý I2PTunnel** tại `http://127.0.0.1:7657/i2ptunnel/` hiển thị tất cả các tunnel đã được cấu hình của bạn — bộ proxy HTTP, IRC, email và tunnel máy chủ eepsite đều đã được cấu hình sẵn từ đầu.

![Danh sách I2PTunnel](/images/guides/quickstart/i2ptunnel-list.png)

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

## Năm điều bạn có thể làm sau khi kết nối

### Duyệt các trang web .i2p

Việc sử dụng I2P phổ biến nhất là duyệt các trang web ẩn. Khi trình duyệt của bạn được định tuyến qua cổng 4444, hãy truy cập bất kỳ địa chỉ nào có đuôi `.i2p`. Một số trang web nổi tiếng có thể làm điểm khởi đầu tốt: **`i2p-projekt.i2p`** là trang web chính thức của dự án I2P được sao chép trong mạng, **`i2pforum.i2p`** là diễn đàn hỗ trợ cộng đồng, **`stats.i2p`** cung cấp số liệu thống kê mạng và dịch vụ đăng ký địa chỉ, còn **`notbob.i2p`** theo dõi thời gian hoạt động của các eepsite đã biết để bạn có thể kiểm tra trang nào đang thực sự hoạt động. Khi gặp một địa chỉ `.i2p` chưa biết, proxy sẽ cung cấp các liên kết "dịch vụ nhảy" để phân giải tên máy chủ – hãy nhấp vào các liên kết này để thêm trang mới vào sổ địa chỉ cục bộ của bạn.

I2P cũng bao gồm một **outproxy** mặc định (`exit.stormycloud.i2p`) cho phép bạn truy cập internet thông thường thông qua I2P, nhưng đây không phải là mục đích chính của mạng và hiệu suất sẽ rất chậm. I2P được thiết kế như một mạng darknet nội bộ, chứ không phải là một mạng nút thoát (exit-node) như Tor.

### Chia sẻ file torrent ẩn danh bằng I2PSnark

**I2PSnark** là một máy khách BitTorrent hoạt động đầy đủ được tích hợp sẵn trong mọi bản cài đặt I2P, có thể truy cập tại `http://127.0.0.1:7657/i2psnark/`. Nó hoạt động hoàn toàn bên trong mạng I2P - không thể kết nối với các torrent trên mạng rõ (clearnet), và người dùng mạng rõ cũng không thể thấy các torrent của I2P. Giao diện web hỗ trợ liên kết magnet, DHT, kéo-thả, tìm kiếm torrent, tải xuống theo trình tự và máy theo dõi UDP (được thêm vào từ phiên bản 2.10.0). Độ dài mặc định của tunnel là ba bước nhảy. Bạn chỉ cần thêm các tệp `.torrent` hoặc liên kết magnet thông qua giao diện.

![Giao diện I2PSnark](/images/guides/quickstart/i2psnark-interface.png)

Để tìm các torrent, hãy truy cập **Postman Tracker** tại `http://tracker2.postman.i2p/` - một trung tâm tập trung nơi người dùng tìm kiếm và tải về các torrent đã được người khác tải lên trong mạng I2P. Bạn cũng có thể tải lên các torrent của riêng mình để chia sẻ với cộng đồng.

![Postman Tracker](/images/guides/quickstart/postman-tracker.png)

Các máy khách torrent tương thích với I2P khác bao gồm BiglyBT và qBittorrent với tiện ích bổ sung I2P.

### Gửi email được mã hóa bằng SusiMail

**SusiMail** tại `http://127.0.0.1:7657/susimail/` là một trình khách email dựa trên web được thiết kế để tránh rò rỉ thông tin nhận dạng. Nó kết nối tới máy chủ email **`mail.i2p`** do "postman" vận hành. Để bắt đầu, hãy đăng ký một tài khoản tại **`hq.postman.i2p`** (có thể truy cập thông qua proxy I2P của bạn), sau đó đăng nhập bằng thông tin đăng nhập đó vào SusiMail. Các mục I2PTunnel đã được cấu hình sẵn định tuyến SMTP qua `localhost:7659` và POP3 qua `localhost:7660`. Bạn có thể gửi email tới các người dùng `@mail.i2p` khác cũng như tới các địa chỉ email thông thường trên internet (được nối tiếp thông qua outproxy của máy chủ email). SusiMail hỗ trợ định dạng markdown, đính kèm tệp bằng thao tác kéo-thả, và email HTML.

![Hộp thư đến SusiMail](/images/guides/quickstart/susimail-login.png)

![Soạn SusiMail](/images/guides/quickstart/susimail-inbox.png)

### Trò chuyện trên IRC thông qua mạng Irc2P

I2P đi kèm với một **kênh IRC đã được cấu hình sẵn** tại `localhost:6668`. Hãy trỏ bất kỳ phần mềm IRC nào đến địa chỉ này (với SSL/TLS **tắt** - I2P tự xử lý mã hóa) và bạn sẽ kết nối được với mạng Irc2P, một liên minh các máy chủ bao gồm `irc.postman.i2p`, `irc.echelon.i2p`, và `irc.dg.i2p`. Các kênh chính gồm **`#i2p`** để thảo luận chung, **`#i2p-dev`** dành cho phát triển, và **`#i2p-help`** để được hỗ trợ. Kênh IRC tự động loại bỏ các thông tin nhận dạng khỏi kết nối của bạn. Các phần mềm được khuyến nghị bao gồm WeeChat, Pidgin và Thunderbird Chat.

### Tự lưu trữ trang web ẩn danh của bạn

Mỗi cài đặt I2P đều bao gồm một **máy chủ web Jetty** đã được chạy sẵn trên `localhost:7658` cùng với một cổng server I2P tương ứng. Để đăng một trang web, chỉ cần đặt các tệp HTML vào thư mục gốc: `~/.i2p/eepsite/docroot` trên Linux hoặc `%LOCALAPPDATA%\I2P\I2P Site\docroot` trên Windows. Trang web của bạn sẽ tự động nhận được một địa chỉ đích mã hóa dạng Base64 và một địa chỉ ngắn hơn là `xxxxx.b32.i2p`. Để có tên dễ nhớ như `mysite.i2p`, hãy đăng ký tên đó tại các dịch vụ sổ địa chỉ như `stats.i2p` hoặc `no.i2p`. Với các thiết lập nâng cao hơn, bạn có thể thay thế Jetty bằng Apache hoặc Nginx phía sau cổng server I2PTunnel — chỉ cần nhớ loại bỏ các tiêu đề máy chủ có thể nhận diện được. Để biết hướng dẫn chi tiết, hãy xem phần [Tạo một Eepsite I2P](/docs/guides/creating-an-eepsite/) của chúng tôi.

---

## Các biện pháp bảo mật thiết yếu dành cho người dùng mới

**Không bao giờ duyệt I2P và mạng rõ (clearnet) trong cùng một hồ sơ trình duyệt.** Đây là quy tắc bảo mật quan trọng nhất. Hãy tạo một hồ sơ Firefox riêng biệt thông qua `about:profiles` hoặc sử dụng hồ sơ đã được cấu hình sẵn trong Gói Cài đặt Dễ dàng (Easy Install Bundle). Việc nhiễm chéo dữ liệu như cookie, lịch sử và bộ nhớ đệm giữa phiên duyệt ẩn danh và phiên có danh tính là sai sót an toàn vận hành phổ biến nhất.

Tiện ích mở rộng Firefox chính thức **"I2P in Private Browsing"** (có sẵn từ cửa hàng tiện ích của Mozilla) tự động hóa phần lớn các thiết lập này bằng cách tạo các tab chứa riêng biệt với khả năng chống định danh, cách ly bên thứ nhất và bật chế độ letterboxing. Đối với người dùng Chromium, hãy khởi chạy với các cờ riêng biệt: `--user-data-dir=$HOME/.config/chromium-i2p --proxy-server="http://127.0.0.1:4444"`.

---
