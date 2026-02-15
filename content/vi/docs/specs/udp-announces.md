---
title: "UDP Trackers"
description: "Đặc tả giao thức cho các thông báo UDP BitTorrent trong I2P"
slug: "udp-announces"
aliases:
  - "/vi/docs/specs/udp-bittorrent-announces"
  - "/vi/docs/specs/udp-bittorrent-announces/"
category: "Các giao thức"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

## Tổng quan

Đặc tả này tài liệu hóa giao thức cho các thông báo UDP bittorrent trong I2P. Để xem đặc tả tổng thể về bittorrent trong I2P, hãy tham khảo [BitTorrent over I2P](/docs/applications/bittorrent). Để biết thêm thông tin nền tảng và bổ sung về việc phát triển đặc tả này, hãy xem [Proposal 160](/proposals/160-udp-trackers).

## Thiết kế

Đề xuất này sử dụng repliable datagram2, repliable datagram3, và raw datagrams, như được định nghĩa trong [Datagrams](/docs/specs/datagrams). Datagram2 và Datagram3 là các biến thể mới của repliable datagrams, được định nghĩa trong [Đề xuất 163](/proposals/163-datagram2-datagram3). Datagram2 bổ sung khả năng chống tái phát và hỗ trợ chữ ký ngoại tuyến. Datagram3 nhỏ hơn định dạng datagram cũ, nhưng không có xác thực.

### BEP 15

Để tham khảo, luồng thông điệp được định nghĩa trong [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) như sau:

```
Client                        Tracker
    Connect Req. ------------->
      <-------------- Connect Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
```
Giai đoạn kết nối là cần thiết để ngăn chặn việc giả mạo địa chỉ IP. Tracker trả về một connection ID mà client sử dụng trong các lần thông báo tiếp theo. Connection ID này sẽ hết hạn mặc định trong một phút ở phía client, và trong hai phút ở phía tracker.

I2P sẽ sử dụng cùng một luồng thông điệp như BEP 15, để dễ dàng áp dụng vào các codebase client hiện có hỗ trợ UDP: vì hiệu quả, và vì các lý do bảo mật được thảo luận bên dưới:

```
Client                        Tracker
    Connect Req. ------------->       (Repliable Datagram2)
      <-------------- Connect Resp.   (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
             ...
```
Điều này có thể mang lại tiết kiệm băng thông lớn so với các thông báo streaming (TCP). Trong khi Datagram2 có kích thước tương đương với streaming SYN, thì phản hồi raw nhỏ hơn nhiều so với streaming SYN ACK. Các yêu cầu tiếp theo sử dụng Datagram3, và các phản hồi tiếp theo là raw.

Các yêu cầu announce là Datagram3để tracker không cần duy trì một bảng ánh xạ lớn các connection ID tới đích announce hoặc hash. Thay vào đó, tracker có thể tạo ra các connection ID một cách mật mã học từ sender hash, timestamp hiện tại (dựa trên một khoảng thời gian nhất định), và một giá trị bí mật. Khi một yêu cầu announce được nhận, tracker xác thực connection ID, sau đó sử dụng Datagram3 sender hash làm mục tiêu gửi.

### Thời gian tồn tại kết nối

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html) quy định rằng connection ID hết hạn sau một phút ở client, và sau hai phút ở tracker. Điều này không thể cấu hình được. Điều đó hạn chế các lợi ích hiệu quả tiềm năng, trừ khi client gộp các thông báo lại để thực hiện tất cả trong khoảng thời gian một phút. i2psnark hiện tại không gộp các thông báo; nó phân tán chúng ra để tránh lưu lượng truy cập đột biến. Những người dùng chuyên nghiệp được báo cáo là đang chạy hàng nghìn torrent cùng lúc, và việc đẩy nhiều thông báo như vậy vào một phút là không thực tế.

Ở đây, chúng tôi đề xuất mở rộng phản hồi kết nối để thêm một trường thời gian sống kết nối tùy chọn. Mặc định, nếu không có, là một phút. Ngược lại, thời gian sống được chỉ định tính bằng giây, sẽ được client sử dụng, và tracker sẽ duy trì connection ID trong thời gian thêm một phút.

### Tương thích với BEP 15

Thiết kế này duy trì khả năng tương thích với [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) càng nhiều càng tốt để hạn chế các thay đổi cần thiết trong các client và tracker hiện có.

Thay đổi duy nhất bắt buộc là định dạng thông tin peer trong phản hồi announce. Việc thêm trường lifetime trong phản hồi connect không bắt buộc nhưng được khuyến nghị mạnh để tăng hiệu quả, như đã giải thích ở trên.

### Phân Tích Bảo Mật

Một mục tiêu quan trọng của giao thức thông báo UDP là ngăn chặn việc giả mạo địa chỉ. Client phải thực sự tồn tại và đóng gói một leaseset thực. Nó phải có các tunnel đầu vào để nhận Connect Response. Những tunnel này có thể là zero-hop và được xây dựng ngay lập tức, nhưng điều đó sẽ làm lộ người tạo ra chúng. Giao thức này đạt được mục tiêu đó.

### Vấn đề

- Giao thức này không hỗ trợ các điểm đến được làm mù (blinded destinations), nhưng có thể được mở rộng để làm như vậy. Xem bên dưới.

## Đặc tả kỹ thuật

### Giao thức và Cổng

Repliable Datagram2 sử dụng I2CP protocol 19; repliable Datagram3 sử dụng I2CP protocol 20; raw datagrams sử dụng I2CP protocol 18. Các yêu cầu có thể là Datagram2 hoặc Datagram3. Các phản hồi luôn là raw. Định dạng repliable datagram cũ hơn ("Datagram1") sử dụng I2CP protocol 17 KHÔNG ĐƯỢC sử dụng cho các yêu cầu hoặc phản hồi; chúng phải được loại bỏ nếu nhận được trên các cổng request/reply. Lưu ý rằng Datagram1 protocol 17 vẫn được sử dụng cho giao thức DHT.

Các yêu cầu sử dụng I2CP "to port" từ announce URL; xem bên dưới. "From port" của yêu cầu được chọn bởi client, nhưng nên khác không và khác với port được sử dụng bởi DHT, để các phản hồi có thể được phân loại dễ dàng. Các tracker nên từ chối các yêu cầu nhận được trên port sai.

Các phản hồi sử dụng "to port" của I2CP từ yêu cầu. "From port" của yêu cầu là "to port" từ yêu cầu.

### URL Thông báo

Định dạng URL announce không được chỉ định trong [BEP 15](http://www.bittorrent.org/beps/bep_0015.html), nhưng như trên clearnet, các URL announce UDP có dạng `udp://host:port/path`. Đường dẫn bị bỏ qua và có thể để trống, nhưng thường là `/announce` trên clearnet. Phần `:port` phải luôn có mặt, tuy nhiên, nếu phần `:port` bị bỏ qua, hãy sử dụng cổng I2CP mặc định là 6969, vì đây là cổng phổ biến trên clearnet. Cũng có thể có các tham số cgi `&a=b&c=d` được thêm vào, những tham số này có thể được xử lý và cung cấp trong yêu cầu announce, xem [BEP 41](http://www.bittorrent.org/beps/bep_0041.html). Nếu không có tham số hoặc đường dẫn, dấu `/` ở cuối cũng có thể được bỏ qua, như được ngụ ý trong [BEP 41](http://www.bittorrent.org/beps/bep_0041.html).

### Định dạng Datagram

Tất cả các giá trị được gửi theo thứ tự byte mạng (big endian). Không nên mong đợi các gói tin có kích thước chính xác nhất định. Các phần mở rộng trong tương lai có thể làm tăng kích thước của các gói tin.

#### Yêu cầu Kết nối

Client tới tracker. 16 bytes. Phải có thể trả lời được Datagram2. Giống như trong [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Không có thay đổi.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">protocol_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0x41727101980 // magic constant</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
#### Phản hồi Kết nối

Tracker đến client. 16 hoặc 18 bytes. Phải là raw. Giống như trong [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) ngoại trừ các điểm được ghi chú dưới đây.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">lifetime</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // Change from BEP 15</td>
    </tr>
  </tbody>
</table>
Phản hồi PHẢI được gửi đến I2CP "to port" mà đã được nhận như là "from port" của yêu cầu.

Trường lifetime là tùy chọn và chỉ ra thời gian tồn tại của connection_id client tính bằng giây. Mặc định là 60, và nếu được chỉ định thì tối thiểu là 60. Tối đa là 65535 hoặc khoảng 18 giờ. Tracker nên duy trì connection_id trong 60 giây nhiều hơn so với thời gian tồn tại của client.

#### Yêu cầu Thông báo

Client đến tracker. Tối thiểu 98 byte. Phải là Datagram3 có thể phản hồi. Giống như trong [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) ngoại trừ các điểm được ghi chú bên dưới.

connection_id là như đã nhận được trong phản hồi kết nối.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">info_hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">peer_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">56</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">downloaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">left</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">uploaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">80</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">event</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // 0: none; 1: completed; 2: started; 3: stopped</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">84</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">IP address</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // default, unused in I2P</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">88</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">92</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">num_want</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1 // default</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">port</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// must be same as I2CP from port</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">98</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">options</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // As specified in BEP 41</td>
    </tr>
  </tbody>
</table>
Thay đổi từ [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- key bị bỏ qua
- Địa chỉ IP không được sử dụng
- port có thể bị bỏ qua nhưng phải giống với port từ I2CP
- Phần options, nếu có, được định nghĩa theo [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)

Phản hồi PHẢI được gửi đến "to port" của I2CP đã nhận được như "from port" của yêu cầu. Không sử dụng port từ yêu cầu thông báo.

#### Phản hồi thông báo

Tracker tới client. Tối thiểu 20 byte. Phải là dữ liệu thô. Giống như trong [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) ngoại trừ những điểm được ghi chú bên dưới.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">interval</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">leechers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">seeders</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32 * n 32-byte hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">binary hashes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// Change from BEP 15</td>
    </tr>
  </tbody>
</table>
Thay đổi từ [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- Thay vì 6-byte IPv4+port hoặc 18-byte IPv6+port, chúng tôi trả về bội số của các "compact responses" 32-byte với các SHA-256 binary peer hashes. Giống như với TCP compact responses, chúng tôi không bao gồm port.

Phản hồi PHẢI được gửi đến "to port" của I2CP đã được nhận như là "from port" của yêu cầu. Không được sử dụng port từ yêu cầu thông báo.

Datagram I2P có kích thước tối đa rất lớn khoảng 64 KB; tuy nhiên, để đảm bảo giao hàng đáng tin cậy, nên tránh các datagram lớn hơn 4 KB. Để tối ưu băng thông, các tracker có lẽ nên giới hạn số peer tối đa khoảng 50, tương ứng với gói tin khoảng 1600 byte trước khi tính overhead ở các lớp khác nhau, và nên nằm trong giới hạn payload hai tunnel-message sau khi phân mảnh.

Như trong BEP 15, không có số lượng được bao gồm về số địa chỉ peer (IP/port cho BEP 15, hash ở đây) sẽ theo sau. Mặc dù không được dự kiến trong BEP 15, một dấu hiệu kết thúc peer bằng toàn số không có thể được định nghĩa để chỉ ra rằng thông tin peer đã hoàn chỉnh và một số dữ liệu mở rộng sẽ theo sau.

Để có thể mở rộng trong tương lai, các client nên bỏ qua hash 32-byte toàn số không và bất kỳ dữ liệu nào theo sau. Các tracker nên từ chối thông báo từ hash toàn số không, mặc dù hash đó đã bị cấm bởi các router Java.

#### Thu thập dữ liệu

Yêu cầu scrape/phản hồi từ [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) không được yêu cầu bởi thông số kỹ thuật này, nhưng có thể được triển khai nếu muốn, không cần thay đổi gì. Client phải lấy được connection ID trước. Yêu cầu scrape luôn là Datagram3 có thể trả lời. Phản hồi scrape luôn ở dạng raw.

#### Phản Hồi Lỗi

Tracker đến client. Tối thiểu 8 byte (nếu thông điệp trống). Phải ở dạng thô. Giống như trong [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Không có thay đổi.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3 // error</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">message</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
## Tiện ích mở rộng

Các bit mở rộng hoặc trường phiên bản không được bao gồm. Các client và tracker không nên giả định rằng các gói tin có kích thước nhất định. Bằng cách này, các trường bổ sung có thể được thêm vào mà không làm hỏng tính tương thích. Định dạng mở rộng được định nghĩa trong [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) được khuyến nghị nếu cần thiết.

Phản hồi kết nối được sửa đổi để thêm thời gian tồn tại ID kết nối tùy chọn.

Nếu cần hỗ trợ blinded destination, chúng ta có thể thêm địa chỉ blinded 35-byte vào cuối yêu cầu announce, hoặc yêu cầu blinded hash trong các phản hồi, sử dụng định dạng [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) (các tham số sẽ được xác định sau). Tập hợp các địa chỉ peer blinded 35-byte có thể được thêm vào cuối phản hồi announce, sau một hash 32-byte toàn số không.

## Hướng Dẫn Triển Khai

Xem phần thiết kế ở trên để thảo luận về những thách thức đối với các client và tracker không tích hợp, không sử dụng I2CP.

### Clients

Đối với một hostname tracker nhất định, client nên ưu tiên các URL UDP hơn HTTP, và không nên announce đến cả hai.

Các client đã hỗ trợ BEP 15 hiện tại sẽ chỉ cần những thay đổi nhỏ.

Nếu một client hỗ trợ DHT hoặc các giao thức datagram khác, có lẽ nó nên chọn một port khác làm "from port" của yêu cầu để các phản hồi trở về port đó và không bị trộn lẫn với các tin nhắn DHT. Client chỉ nhận các datagram thô làm phản hồi. Các tracker sẽ không bao giờ gửi datagram2 có thể trả lời đến client.

Các client có danh sách opentracker mặc định nên cập nhật danh sách để thêm các URL UDP sau khi các opentracker đã biết được xác nhận hỗ trợ UDP.

Các client có thể có hoặc không có cài đặt truyền lại các yêu cầu. Việc truyền lại, nếu được triển khai, nên sử dụng thời gian chờ ban đầu ít nhất 15 giây, và nhân đôi thời gian chờ cho mỗi lần truyền lại (exponential backoff).

Các client phải lùi lại sau khi nhận được phản hồi lỗi.

### Trackers

Các tracker đã hỗ trợ BEP 15 hiện tại chỉ cần những chỉnh sửa nhỏ. Đặc tả này khác với đề xuất năm 2014, ở chỗ tracker phải hỗ trợ việc nhận repliable datagram2 và datagram3 trên cùng một cổng.

Để giảm thiểu yêu cầu tài nguyên của tracker, giao thức này được thiết kế để loại bỏ mọi yêu cầu tracker phải lưu trữ ánh xạ hash của client với ID kết nối để xác thực sau này. Điều này có thể thực hiện được vì gói tin yêu cầu announce là một gói tin Datagram3 có thể trả lời, do đó nó chứa hash của người gửi.

Một triển khai được khuyến nghị là:

- Định nghĩa epoch hiện tại là thời gian hiện tại với độ phân giải của thời gian tồn tại kết nối, `epoch = now / lifetime`.
- Định nghĩa hàm băm mật mã `H(secret, clienthash, epoch)` tạo ra đầu ra 8 byte.
- Tạo hằng số ngẫu nhiên bí mật được sử dụng cho tất cả các kết nối.
- Đối với phản hồi kết nối, tạo `connection_id = H(secret, clienthash, epoch)`
- Đối với yêu cầu thông báo, xác thực ID kết nối nhận được trong epoch hiện tại bằng cách kiểm tra `connection_id == H(secret, clienthash, epoch) || connection_id == H(secret, clienthash, epoch - 1)`

## Tài liệu tham khảo

- **[BEP15]** [BEP 15 - Giao thức UDP Tracker](http://www.bittorrent.org/beps/bep_0015.html)
- **[BEP41]** [BEP 41 - Các mở rộng giao thức UDP Tracker](http://www.bittorrent.org/beps/bep_0041.html)
- **[DATAGRAMS]** [Đặc tả Datagrams](/docs/specs/datagrams)
- **[Prop160]** [Đề xuất 160 - UDP Trackers](/proposals/160-udp-trackers)
- **[Prop163]** [Đề xuất 163 - Datagram2/Datagram3](/proposals/163-datagram2-datagram3)
- **[SAMv3]** [API SAM v3](/docs/api/samv3)
- **[SPEC]** [BitTorrent trên I2P](/docs/applications/bittorrent)
