---
title: "Cải tiến Giao thức Vận chuyển IPv6"
aliases:
  - "/vi/spec/proposals/158"
  - "/vi/spec/proposals/158/"
number: "158"
author: "zzz, orignal"
created: "2021-03-19"
lastupdated: "2021-04-26"
status: "Closed"
thread: "http://zzz.i2p/topics/3060"
target: "0.9.50"
toc: true
---
## Ghi chú
Triển khai mạng và kiểm thử đang được tiến hành.  
Có thể sửa đổi nhỏ.


## Tổng quan

Đề xuất này nhằm thực hiện các cải tiến cho các giao thức truyền tải SSU và NTCP2 đối với IPv6.


## Động lực

Khi IPv6 ngày càng phát triển trên toàn thế giới và các thiết lập chỉ dùng IPv6 (đặc biệt trên thiết bị di động) trở nên phổ biến hơn,
chúng ta cần cải thiện khả năng hỗ trợ IPv6 và loại bỏ các giả định rằng
tất cả các bộ định tuyến đều có khả năng IPv4.



### Kiểm tra kết nối

Khi chọn các điểm ngang hàng (peer) cho các đường hầm, hoặc chọn các đường dẫn OBEP/IBGW để định tuyến tin nhắn,
sẽ hữu ích nếu tính toán được liệu bộ định tuyến A có thể kết nối tới bộ định tuyến B hay không.
Nói chung, điều này có nghĩa là xác định xem A có khả năng gửi ra ngoài (outbound) cho một giao thức và loại địa chỉ (IPv4/v6)
phù hợp với một trong các địa chỉ nhận vào (inbound) được B công bố hay không.

Tuy nhiên, trong nhiều trường hợp, chúng ta không biết khả năng của A và phải đưa ra giả định.
Nếu A bị ẩn hoặc bị tường lửa, các địa chỉ sẽ không được công bố, và chúng ta không có thông tin trực tiếp —
do đó, chúng ta giả định rằng A có khả năng IPv4, nhưng không có khả năng IPv6.
Giải pháp là thêm hai "khả năng" (caps) mới vào Thông tin Bộ định tuyến (Router Info) để chỉ ra khả năng gửi ra ngoài cho IPv4 và IPv6.


### Người giới thiệu IPv6

Các đặc tả của chúng ta về SSU có những lỗi và không nhất quán về việc
có hỗ trợ người giới thiệu IPv6 cho các giới thiệu IPv4 hay không.
Dù sao đi nữa, điều này chưa từng được triển khai trong cả Java I2P lẫn i2pd.
Việc này cần được sửa chữa.


### Các giới thiệu IPv6

Các đặc tả của chúng ta về SSU nêu rõ rằng
các giới thiệu IPv6 không được hỗ trợ.
Điều này dựa trên giả định rằng IPv6 không bao giờ bị tường lửa.
Điều này rõ ràng là không đúng, và chúng ta cần cải thiện khả năng hỗ trợ các bộ định tuyến IPv6 bị tường lửa.


### Sơ đồ giới thiệu

Chú thích: ----- là IPv4, ====== là IPv6

**Chỉ dùng IPv4 hiện tại:**

```
        Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**Giới thiệu IPv4, người giới thiệu IPv6:**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**Giới thiệu IPv6, người giới thiệu IPv6:**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```

**Giới thiệu IPv6, người giới thiệu IPv4:**

```
Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```


## Thiết kế

Có ba thay đổi cần được triển khai.

- Thêm khả năng "4" và "6" vào các khả năng địa chỉ bộ định tuyến để chỉ ra hỗ trợ gửi ra ngoài IPv4 và IPv6
- Thêm hỗ trợ cho các giới thiệu IPv4 thông qua người giới thiệu IPv6
- Thêm hỗ trợ cho các giới thiệu IPv6 thông qua người giới thiệu IPv4 và IPv6



## Đặc tả

### Khả năng 4/6

Tính năng này ban đầu được triển khai mà không có đề xuất chính thức, nhưng nó là bắt buộc cho
các giới thiệu IPv6, vì vậy chúng tôi đưa nó vào đây.


Hai khả năng mới "4" và "6" được định nghĩa.
Các khả năng mới này sẽ được thêm vào thuộc tính "caps" trong Địa chỉ Bộ định tuyến (Router Address), chứ không phải trong các khả năng của Router Info.
Hiện tại, chúng ta chưa có thuộc tính "caps" được định nghĩa cho NTCP2.
Một địa chỉ SSU có người giới thiệu hiện tại, theo định nghĩa, là ipv4. Chúng ta hoàn toàn chưa hỗ trợ giới thiệu ipv6.
Tuy nhiên, đề xuất này tương thích với các giới thiệu IPv6. Xem bên dưới.

Ngoài ra, một bộ định tuyến có thể hỗ trợ kết nối thông qua một mạng overlay như I2P-over-Yggdrasil,
nhưng không muốn công bố địa chỉ, hoặc địa chỉ đó không có định dạng IPv4 hoặc IPv6 chuẩn.
Hệ thống khả năng mới này nên đủ linh hoạt để hỗ trợ các mạng này.

Chúng tôi định nghĩa các thay đổi sau:

NTCP2: Thêm thuộc tính "caps"

SSU: Thêm hỗ trợ cho một Địa chỉ Bộ định tuyến không có host hoặc người giới thiệu, để chỉ ra khả năng gửi ra ngoài
cho IPv4, IPv6, hoặc cả hai.

Cả hai giao thức: Định nghĩa các giá trị caps sau:

- "4": Hỗ trợ IPv4
- "6": Hỗ trợ IPv6

Nhiều giá trị có thể được hỗ trợ trong một địa chỉ duy nhất. Xem bên dưới.
Ít nhất một trong các khả năng này là bắt buộc nếu không có giá trị "host" nào được bao gồm trong Địa chỉ Bộ định tuyến.
Tối đa một trong các khả năng này là tùy chọn nếu có giá trị "host" trong Địa chỉ Bộ định tuyến.
Các khả năng giao thức bổ sung có thể được định nghĩa trong tương lai để chỉ ra hỗ trợ cho các mạng overlay hoặc các kết nối khác.


#### Các trường hợp sử dụng và ví dụ

SSU:

SSU có host: 4/6 tùy chọn, không bao giờ nhiều hơn một.
Ví dụ: SSU caps="4" host="1.2.3.4" key=... port="1234"

SSU chỉ gửi ra ngoài cho một loại, loại còn lại được công bố: Chỉ có caps, 4/6.
Ví dụ: SSU caps="6"

SSU có người giới thiệu: Không bao giờ kết hợp. Yêu cầu 4 hoặc 6.
Ví dụ: SSU caps="4" iexp0=... ihost0=... iport0=... itag0=... key=...

SSU ẩn: Chỉ có caps, 4, 6, hoặc 46. Cho phép nhiều giá trị.
Không cần hai địa chỉ, một với 4 và một với 6.
Ví dụ: SSU caps="46"

NTCP2:

NTCP2 có host: 4/6 tùy chọn, không bao giờ nhiều hơn một.
Ví dụ: NTCP2 caps="4" host="1.2.3.4" i=... port="1234" s=... v="2"

NTCP2 chỉ gửi ra ngoài cho một loại, loại còn lại được công bố: Chỉ có caps, s, v, 4/6/y, cho phép nhiều giá trị.
Ví dụ: NTCP2 caps="6" i=... s=... v="2"

NTCP2 ẩn: Chỉ có caps, s, v, 4/6, cho phép nhiều giá trị. Không cần hai địa chỉ, một với 4 và một với 6.
Ví dụ: NTCP2 caps="46" i=... s=... v="2"



### Người giới thiệu IPv6 cho IPv4

Các thay đổi sau đây là cần thiết để sửa lỗi và sự không nhất quán trong các đặc tả.
Chúng tôi cũng đã mô tả điều này như "phần 1" của đề xuất.

#### Thay đổi đặc tả

Đặc tả SSU hiện tại nói (ghi chú IPv6):

IPv6 được hỗ trợ kể từ phiên bản 0.9.8. Các địa chỉ chuyển tiếp được công bố có thể là IPv4 hoặc IPv6, và giao tiếp Alice-Bob có thể qua IPv4 hoặc IPv6.

Thêm vào:

Mặc dù đặc tả đã được thay đổi kể từ phiên bản 0.9.8, giao tiếp Alice-Bob qua IPv6 thực tế chưa được hỗ trợ cho đến phiên bản 0.9.50.
Các phiên bản cũ hơn của bộ định tuyến Java đã sai lầm khi công bố khả năng 'C' cho các địa chỉ IPv6,
dù thực tế chúng không hoạt động như một người giới thiệu qua IPv6.
Do đó, các bộ định tuyến chỉ nên tin tưởng khả năng 'C' trên một địa chỉ IPv6 nếu phiên bản bộ định tuyến là 0.9.50 trở lên.



Đặc tả SSU hiện tại nói (Yêu cầu Chuyển tiếp):

Địa chỉ IP chỉ được bao gồm nếu nó khác với địa chỉ nguồn và cổng của gói tin.
Trong triển khai hiện tại, độ dài IP luôn bằng 0 và cổng luôn bằng 0,
và người nhận nên sử dụng địa chỉ nguồn và cổng của gói tin.
Tin nhắn này có thể được gửi qua IPv4 hoặc IPv6. Nếu là IPv6, Alice phải bao gồm địa chỉ và cổng IPv4 của cô ấy.

Thêm vào:

IP và cổng phải được bao gồm để giới thiệu một địa chỉ IPv4 khi gửi tin nhắn này qua IPv6.
Tính năng này được hỗ trợ kể từ phiên bản 0.9.50.



### Các giới thiệu IPv6

Tất cả ba tin nhắn chuyển tiếp SSU (RelayRequest, RelayResponse và RelayIntro) đều chứa các trường độ dài IP
để chỉ ra độ dài của địa chỉ IP (Alice, Bob hoặc Charlie) theo sau.

Do đó, không cần thay đổi định dạng của các tin nhắn.
Chỉ cần thay đổi văn bản trong các đặc tả, nêu rõ rằng các địa chỉ IP 16 byte được cho phép.

Các thay đổi sau đây là cần thiết đối với các đặc tả.
Chúng tôi cũng đã mô tả điều này như "phần 2" của đề xuất.


#### Thay đổi đặc tả

Đặc tả SSU hiện tại nói (ghi chú IPv6):

Giao tiếp Bob-Charlie và Alice-Charlie chỉ qua IPv4.

Đặc tả SSU hiện tại nói (Yêu cầu Chuyển tiếp):

Hiện không có kế hoạch triển khai chuyển tiếp cho IPv6.

Thay đổi thành:

Chuyển tiếp cho IPv6 được hỗ trợ kể từ phiên bản 0.9.xx

Đặc tả SSU hiện tại nói (Phản hồi Chuyển tiếp):

Địa chỉ IP của Charlie phải là IPv4, vì đó là địa chỉ mà Alice sẽ gửi SessionRequest đến sau khi Hole Punch.
Hiện không có kế hoạch triển khai chuyển tiếp cho IPv6.

Thay đổi thành:

Địa chỉ IP của Charlie có thể là IPv4 hoặc, kể từ phiên bản 0.9.xx, là IPv6.
Đó là địa chỉ mà Alice sẽ gửi SessionRequest đến sau khi Hole Punch.
Chuyển tiếp cho IPv6 được hỗ trợ kể từ phiên bản 0.9.xx

Đặc tả SSU hiện tại nói (Giới thiệu Chuyển tiếp):

Địa chỉ IP của Alice luôn là 4 byte trong triển khai hiện tại, vì Alice đang cố kết nối với Charlie qua IPv4.
Tin nhắn này phải được gửi qua một kết nối IPv4 đã thiết lập,
vì đó là cách duy nhất để Bob biết địa chỉ IPv4 của Charlie để trả về cho Alice trong RelayResponse.

Thay đổi thành:

Đối với IPv4, địa chỉ IP của Alice luôn là 4 byte, vì Alice đang cố kết nối với Charlie qua IPv4.
Kể từ phiên bản 0.9.xx, IPv6 được hỗ trợ, và địa chỉ IP của Alice có thể là 16 byte.

Đối với IPv4, tin nhắn này phải được gửi qua một kết nối IPv4 đã thiết lập,
vì đó là cách duy nhất để Bob biết địa chỉ IPv4 của Charlie để trả về cho Alice trong RelayResponse.
Kể từ phiên bản 0.9.xx, IPv6 được hỗ trợ, và tin nhắn này có thể được gửi qua một kết nối IPv6 đã thiết lập.

Cũng thêm vào:

Kể từ phiên bản 0.9.xx, mọi địa chỉ SSU được công bố với người giới thiệu phải chứa "4" hoặc "6" trong tùy chọn "caps".


## Di chuyển

Tất cả các bộ định tuyến cũ nên bỏ qua thuộc tính caps trong NTCP2, và các ký tự khả năng không biết trong thuộc tính caps của SSU.

Bất kỳ địa chỉ SSU nào có người giới thiệu mà không chứa khả năng "4" hoặc "6" sẽ được coi là dùng để giới thiệu IPv4.


## Tài liệu tham khảo

* [CAPS](http://zzz.i2p/topics/3050)
* [NTCP2](/docs/specs/ntcp2/)
* [SSU](/docs/specs/ssu2/)
* [SSU-SPEC](/docs/legacy/ssu/)
