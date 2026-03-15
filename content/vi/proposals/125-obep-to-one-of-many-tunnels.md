---
title: "Giao nhận OBEP tới các kênh 1-of-N hoặc N-of-N"
number: "125"
author: "zzz, str4d"
created: "2016-03-10"
lastupdated: "2017-04-07"
status: "Open"
thread: "http://zzz.i2p/topics/2099"
toc: true
---
## Tổng quan

Đề xuất này bao gồm hai cải tiến nhằm nâng cao hiệu suất mạng:

- Ủy quyền việc chọn IBGW cho OBEP bằng cách cung cấp cho nó một danh sách các
  lựa chọn thay vì chỉ một tùy chọn duy nhất.

- Cho phép định tuyến gói tin multicast tại OBEP.


## Động lực

Trong trường hợp kết nối trực tiếp, mục tiêu là giảm tắc nghẽn kết nối bằng cách
tạo sự linh hoạt cho OBEP trong việc kết nối đến các IBGW. Khả năng chỉ định
nhiều tunnel cũng cho phép chúng ta triển khai multicast tại OBEP (bằng cách
gửi tin nhắn đến tất cả các tunnel được chỉ định).

Một phương án thay thế cho phần ủy quyền trong đề xuất này là gửi qua
một hash LeaseSet, tương tự như khả năng hiện tại để chỉ định một hash
[RouterIdentity](/docs/specs/common-structures/#common-structure-specification). Điều này sẽ tạo ra một tin nhắn nhỏ hơn và có thể có
LeaseSet mới hơn. Tuy nhiên:

1. Nó sẽ buộc OBEP phải thực hiện tra cứu.

2. LeaseSet có thể không được công bố lên floodfill, do đó việc tra cứu sẽ thất bại.

3. LeaseSet có thể được mã hóa, do đó OBEP không thể lấy được các lease.

4. Việc chỉ định một LeaseSet sẽ tiết lộ cho OBEP [Destination](/docs/specs/common-structures/#destination) của tin nhắn,
   điều mà họ không thể biết được nếu không quét toàn bộ các LeaseSet trong mạng
   và tìm kiếm sự trùng khớp lease.


## Thiết kế

Thành phần khởi tạo (OBGW) sẽ đặt một số (hoặc tất cả?) [Lease](/docs/specs/common-structures/#lease) đích vào
các chỉ dẫn giao hàng [TUNNEL-DELIVERY](/docs/specs/i2np/#tunnel-message-delivery-instructions) thay vì chỉ chọn một.

OBEP sẽ chọn một trong số đó để giao hàng. OBEP sẽ chọn, nếu có sẵn,
một tunnel mà nó đã kết nối hoặc đã biết trước. Điều này sẽ làm cho đường đi
OBEP-IBGW nhanh hơn và đáng tin cậy hơn, đồng thời giảm số lượng kết nối tổng thể
trong mạng.

Chúng ta có một loại giao hàng chưa dùng (0x03) và hai bit còn lại (0 và 1) trong
cờ của TUNNEL-DELIVERY, có thể tận dụng để triển khai các tính năng này.


## Tác động bảo mật

Đề xuất này không làm thay đổi lượng thông tin bị rò rỉ về
Destination đích của OBGW hay góc nhìn của họ về NetDB:

- Một kẻ tấn công kiểm soát OBEP và đang quét các LeaseSet từ NetDB
  đã có thể xác định được liệu một tin nhắn có đang được gửi đến một
  Destination cụ thể hay không, bằng cách tìm kiếm cặp TunnelId / RouterIdentity. Trong trường hợp xấu nhất, việc có nhiều Lease trong TMDI có thể giúp
  tìm thấy sự trùng khớp nhanh hơn trong cơ sở dữ liệu của kẻ tấn công.

- Một kẻ tấn công điều hành một Destination độc hại đã có thể thu thập thông tin
  về góc nhìn NetDB của nạn nhân đang kết nối, bằng cách công bố các LeaseSet
  chứa các tunnel nội tuyến khác nhau lên các floodfill khác nhau, và quan sát
  xem OBGW kết nối qua tunnel nào. Từ góc nhìn của chúng, việc OBEP chọn tunnel
  để sử dụng về cơ bản giống hệt như việc OBGW tự chọn.

Cờ multicast làm rò rỉ thông tin rằng OBGW đang thực hiện multicast đến các OBEP.
Điều này tạo ra sự đánh đổi giữa hiệu suất và quyền riêng tư, cần được cân nhắc
khi triển khai các giao thức cấp cao hơn. Vì là một cờ tùy chọn, người dùng có thể
tự đưa ra quyết định phù hợp cho ứng dụng của mình. Tuy nhiên, việc mặc định bật
tính năng này cho các ứng dụng tương thích có thể mang lại lợi ích, vì việc sử dụng
phổ biến từ nhiều ứng dụng khác nhau sẽ làm giảm lượng thông tin bị rò rỉ về việc
tin nhắn đến từ ứng dụng cụ thể nào.


## Đặc tả

Các chỉ dẫn giao hàng phân mảnh đầu tiên sẽ được sửa đổi như sau:

```
+----+----+----+----+----+----+----+----+
  |flag|  Tunnel ID (opt)  |              |
  +----+----+----+----+----+              +
  |                                       |
  +                                       +
  |         To Hash (optional)            |
  +                                       +
  |                                       |
  +                        +----+----+----+
  |                        |dly | Message
  +----+----+----+----+----+----+----+----+
   ID (opt) |extended opts (opt)|cnt | (o)
  +----+----+----+----+----+----+----+----+
   Tunnel ID N   |                        |
  +----+----+----+                        +
  |                                       |
  +                                       +
  |         To Hash N (optional)          |
  +                                       +
  |                                       |
  +              +----+----+----+----+----+
  |              | Tunnel ID N+1 (o) |    |
  +----+----+----+----+----+----+----+    +
  |                                       |
  +                                       +
  |         To Hash N+1 (optional)        |
  +                                       +
  |                                       |
  +                                  +----+
  |                                  | sz
  +----+----+----+----+----+----+----+----+
       |
  +----+

flag ::
       1 byte
       Thứ tự bit: 76543210
       bit 6-5: loại giao hàng
                 0x03 = TUNNELS
       bit 0: multicast? Nếu 0, giao đến một trong các tunnel
                         Nếu 1, giao đến tất cả các tunnel
                         Đặt về 0 để tương thích với các sử dụng trong tương lai nếu
                         loại giao hàng không phải là TUNNELS

Count ::
       1 byte
       Tùy chọn, hiện diện nếu loại giao hàng là TUNNELS
       2-255 - Số cặp id/hash theo sau

Tunnel ID :: TunnelId
To Hash ::
       36 byte mỗi cái
       Tùy chọn, hiện diện nếu loại giao hàng là TUNNELS
       các cặp id/hash

Độ dài tổng: Độ dài điển hình là:
       75 byte cho giao hàng TUNNELS với count = 2 (tin nhắn tunnel không phân mảnh);
       79 byte cho giao hàng TUNNELS với count = 2 (phân mảnh đầu tiên)

Phần còn lại của chỉ dẫn giao hàng không thay đổi
```


## Tương thích

Duy nhất các peer cần hiểu đặc tả mới là OBGW và OBEP. Do đó, chúng ta có thể
làm thay đổi này tương thích với mạng hiện tại bằng cách điều kiện hóa việc sử dụng
theo phiên bản I2P đích:

* OBGW phải chọn các OBEP tương thích khi xây dựng các tunnel đi ra, dựa trên
  phiên bản I2P được quảng cáo trong [RouterInfo](/docs/specs/common-structures/#routerinfo) của chúng.

* Các peer quảng cáo phiên bản đích phải hỗ trợ phân tích cú pháp các cờ mới,
  và không được từ chối các chỉ dẫn như là không hợp lệ.


## Tài liệu tham khảo

* [Destination](/docs/specs/common-structures/#destination)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [RouterIdentity](/docs/specs/common-structures/#routeridentity)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TUNNEL-DELIVERY](/docs/specs/common-structures/#tunnelmessagedeliveryinstructions)
* [TunnelId](/docs/specs/common-structures/#tunnelid)
* [VERSIONS](/docs/specs/i2np/#protocol-versions)
