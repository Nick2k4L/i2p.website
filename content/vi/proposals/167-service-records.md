---
title: "Hồ Sơ Dịch Vụ trong LS2"
number: "167"
author: "zzz, hoặc là, eyedeekay"
created: "2024-06-22"
lastupdated: "2025-04-03"
status: "Đã Đóng"
thread: "http://zzz.i2p/topics/3641"
target: "0.9.66"
toc: true
---
## Trạng thái
Đã được phê duyệt trong lần xem xét thứ hai vào 2025-04-01; đặc tả đã được cập nhật; chưa triển khai.

## Tổng quan

I2P thiếu hệ thống DNS tập trung.
Tuy nhiên, sổ địa chỉ, cùng với hệ thống tên miền b32, cho phép
router tra cứu đích đầy đủ và lấy các tập thuê (lease set), trong đó chứa
danh sách các cổng và khóa để các máy khách có thể kết nối đến đích đó.

Do đó, leaseset tương tự như một bản ghi DNS. Tuy nhiên hiện tại không có cơ chế nào cho phép
xác định xem máy chủ đó có hỗ trợ dịch vụ nào hay không, dù là trên đích đó hay một đích khác,
theo cách tương tự như các bản ghi [SRV của DNS](https://en.wikipedia.org/wiki/SRV_record) được định nghĩa trong [RFC 2782](https://datatracker.ietf.org/doc/html/rfc2782).

Ứng dụng đầu tiên cho tính năng này có thể là email ngang hàng.
Các ứng dụng khả thi khác: DNS, GNS, máy chủ khóa, cơ quan chứng thực, máy chủ thời gian,
bittorrent, tiền mã hóa, các ứng dụng ngang hàng khác.

## Các đề xuất và phương án thay thế liên quan

### Danh sách dịch vụ

Đề xuất 123 [LS2](/proposals/123-new-netdb-entries/) định nghĩa các 'bản ghi dịch vụ' cho biết một đích
đang tham gia vào một dịch vụ toàn cục. Các máy chủ floodfill sẽ tập hợp các bản ghi này
thành các 'danh sách dịch vụ' toàn cục.
Tính năng này chưa bao giờ được triển khai do độ phức tạp, thiếu xác thực,
lo ngại về bảo mật và spam.

Đề xuất này khác biệt ở chỗ nó cung cấp cơ chế tra cứu dịch vụ cho một đích cụ thể,
không phải một nhóm các đích toàn cục cho một dịch vụ toàn cục.

### GNS

GNS đề xuất rằng mọi người đều chạy máy chủ DNS riêng của mình.
Đề xuất này bổ trợ, theo nghĩa chúng ta có thể dùng bản ghi dịch vụ để chỉ định
rằng GNS (hoặc DNS) được hỗ trợ, với tên dịch vụ tiêu chuẩn là "domain" trên cổng 53.

### Dot well-known

Đã có [đề xuất](http://i2pforum.i2p/viewtopic.php?p=3102) rằng các dịch vụ được tra cứu thông qua yêu cầu HTTP đến
/.well-known/i2pmail.key. Điều này yêu cầu mỗi dịch vụ phải có một trang web liên quan để lưu trữ khóa. Hầu hết người dùng không chạy trang web.

Một cách giải quyết tạm thời là chúng ta có thể giả định rằng một dịch vụ cho địa chỉ b32 thực sự
đang chạy trên chính địa chỉ b32 đó. Vì vậy, việc tìm kiếm dịch vụ cho example.i2p yêu cầu
lấy dữ liệu HTTP từ http://example.i2p/.well-known/i2pmail.key, nhưng
một dịch vụ cho aaa...aaa.b32.i2p thì không cần tra cứu này, mà có thể kết nối trực tiếp.

Tuy nhiên, điều này gây mơ hồ vì example.i2p cũng có thể được truy cập bằng b32 của nó.

### Bản ghi MX

Bản ghi SRV đơn giản là phiên bản tổng quát của bản ghi MX cho mọi dịch vụ.
"_smtp._tcp" là bản ghi "MX".
Không cần bản ghi MX nếu chúng ta có bản ghi SRV, và bản ghi MX
riêng lẻ không cung cấp bản ghi tổng quát cho mọi dịch vụ.

## Thiết kế

Các bản ghi dịch vụ được đặt trong phần tùy chọn của [LS2](/docs/specs/common-structures/).
Phần tùy chọn của LS2 hiện tại chưa được sử dụng.
Không hỗ trợ cho LS1.
Điều này tương tự như [đề xuất băng thông tunnel](/proposals/168-tunnel-bandwidth/),
định nghĩa các tùy chọn cho bản ghi xây dựng tunnel.

Để tra cứu địa chỉ dịch vụ cho một tên miền hoặc b32 cụ thể, router sẽ lấy
leaseset và tìm bản ghi dịch vụ trong các thuộc tính.

Dịch vụ có thể được lưu trữ trên cùng một đích với chính LS, hoặc có thể tham chiếu
đến một tên miền/b32 khác.

Nếu đích mục tiêu cho dịch vụ khác, thì LS đích cũng phải
bao gồm một bản ghi dịch vụ, trỏ đến chính nó, cho biết rằng nó hỗ trợ dịch vụ đó.

Thiết kế này không yêu cầu hỗ trợ đặc biệt, bộ nhớ đệm hay bất kỳ thay đổi nào ở các floodfill.
Chỉ có người xuất bản leaseset và máy khách tra cứu bản ghi dịch vụ
cần hỗ trợ các thay đổi này.

Được đề xuất mở rộng nhỏ I2CP và SAM để hỗ trợ việc truy xuất
bản ghi dịch vụ bởi các máy khách.

## Đặc tả

### Đặc tả tùy chọn LS2

Các tùy chọn LS2 PHẢI được sắp xếp theo khóa, để chữ ký là bất biến.

Được định nghĩa như sau:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := Tên biểu tượng của dịch vụ mong muốn. Phải viết thường. Ví dụ: "smtp".
  Các ký tự cho phép là [a-z0-9-] và không được bắt đầu hoặc kết thúc bằng '-'.
  Các định danh tiêu chuẩn từ [DNS-SD Service Types registry](http://www.dns-sd.org/ServiceTypes.html) hoặc /etc/services trên Linux phải được sử dụng nếu đã được định nghĩa ở đó.
- proto := Giao thức truyền tải của dịch vụ mong muốn. Phải viết thường, là "tcp" hoặc "udp".
  "tcp" nghĩa là streaming và "udp" nghĩa là datagram có thể trả lời.
  Các chỉ báo giao thức cho datagram thô và datagram2 có thể được định nghĩa sau.
  Các ký tự cho phép là [a-z0-9-] và không được bắt đầu hoặc kết thúc bằng '-'.
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := thời gian sống, đơn vị giây, số nguyên dương. Ví dụ: "86400".
  Khuyến nghị tối thiểu là 86400 (một ngày), xem phần Khuyến nghị bên dưới để biết chi tiết.
- priority := Độ ưu tiên của máy chủ đích, giá trị thấp hơn nghĩa là được ưu tiên hơn. Số nguyên không âm. Ví dụ: "0"
  Chỉ hữu ích nếu có nhiều hơn một bản ghi, nhưng bắt buộc ngay cả khi chỉ có một bản ghi.
- weight := Trọng số tương đối cho các bản ghi có cùng độ ưu tiên. Giá trị cao hơn nghĩa là khả năng được chọn cao hơn. Số nguyên không âm. Ví dụ: "0"
  Chỉ hữu ích nếu có nhiều hơn một bản ghi, nhưng bắt buộc ngay cả khi chỉ có một bản ghi.
- port := Cổng I2CP nơi dịch vụ được tìm thấy. Số nguyên không âm. Ví dụ: "25"
  Cổng 0 được hỗ trợ nhưng không được khuyến nghị.
- target := Tên miền hoặc b32 của đích cung cấp dịch vụ. Một [hostname](/docs/overview/naming/) hợp lệ. Phải viết thường.
  Ví dụ: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" hoặc "example.i2p".
  Nên dùng b32 trừ khi tên miền là "nổi tiếng", tức là nằm trong sổ địa chỉ chính thức hoặc mặc định.
- appoptions := văn bản tùy ý dành riêng cho ứng dụng, không được chứa " " hoặc ",". Mã hóa là UTF-8.

### Ví dụ

Trong LS2 cho aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, trỏ đến một máy chủ SMTP:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Trong LS2 cho aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, trỏ đến hai máy chủ SMTP:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

Trong LS2 cho bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p, trỏ đến chính nó như một máy chủ SMTP:

    "_smtp._tcp" "0 999999 25"

Định dạng khả thi để chuyển hướng email (xem bên dưới):

    "_smtp._tcp" "1 86400 0 0 25 smtp.postman.i2p example@mail.i2p"

### Giới hạn

Cấu trúc dữ liệu Mapping dùng cho tùy chọn LS2 giới hạn khóa và giá trị tối đa 255 byte (không phải ký tự).
Với đích b32, optionvalue dài khoảng 67 byte, nên chỉ chứa được khoảng 3 bản ghi.
Có thể chỉ một hoặc hai nếu trường appoptions dài, hoặc lên đến bốn hoặc năm nếu dùng tên miền ngắn.
Điều này là đủ; nhiều bản ghi nên là trường hợp hiếm.

### Khác biệt so với RFC 2782

- Không có dấu chấm ở cuối
- Không có tên sau proto
- Yêu cầu viết thường
- Dạng văn bản với các bản ghi phân tách bằng dấu phẩy, không phải định dạng DNS nhị phân
- Các chỉ báo loại bản ghi khác nhau
- Thêm trường appoptions

### Ghi chú

Không cho phép dùng ký tự đại diện như (dấu sao), (dấu sao)._tcp, hoặc _tcp.
Mỗi dịch vụ được hỗ trợ phải có bản ghi riêng.

### Registry tên dịch vụ

Các định danh không chuẩn chưa liệt kê trong [DNS-SD Service Types registry](http://www.dns-sd.org/ServiceTypes.html) hoặc /etc/services trên Linux
có thể được yêu cầu và thêm vào [đặc tả cấu trúc chung](/docs/specs/common-structures/).

Các định dạng appoptions riêng cho từng dịch vụ cũng có thể được thêm vào đó.

### Đặc tả I2CP

Giao thức [I2CP](/docs/specs/i2cp/) phải được mở rộng để hỗ trợ tra cứu dịch vụ.
Cần thêm các mã lỗi MessageStatusMessage và/hoặc HostReplyMessage liên quan đến tra cứu dịch vụ.
Để tính năng tra cứu mang tính tổng quát, không chỉ riêng bản ghi dịch vụ,
thiết kế là hỗ trợ truy xuất tất cả các tùy chọn LS2.

Triển khai: Mở rộng HostLookupMessage để thêm yêu cầu
tùy chọn LS2 cho hash, tên miền và đích (loại yêu cầu 2-4).
Mở rộng HostReplyMessage để thêm ánh xạ tùy chọn nếu được yêu cầu.
Mở rộng HostReplyMessage với các mã lỗi bổ sung.

Ánh xạ tùy chọn có thể được lưu tạm hoặc lưu tạm tiêu cực trong thời gian ngắn ở phía máy khách hoặc router,
phụ thuộc vào triển khai. Thời gian tối đa khuyến nghị là một giờ, trừ khi TTL của bản ghi dịch vụ ngắn hơn.
Bản ghi dịch vụ có thể được lưu tạm đến TTL do ứng dụng, máy khách hoặc router chỉ định.

Mở rộng đặc tả như sau:

#### Tùy chọn cấu hình

Thêm vào sau đây vào [các tùy chọn cấu hình I2CP](/docs/specs/i2cp/)

i2cp.leaseSetOption.nnn

Các tùy chọn để đặt vào leaseset. Chỉ khả dụng cho LS2.
nnn bắt đầu từ 0. Giá trị tùy chọn chứa "key=value".
(không bao gồm dấu ngoặc kép)

Ví dụ:
i2cp.leaseSetOption.0=_smtp._tcp=1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p

#### Tin nhắn HostLookup

- Loại tra cứu 2: Tra cứu Hash, yêu cầu ánh xạ tùy chọn
- Loại tra cứu 3: Tra cứu tên miền, yêu cầu ánh xạ tùy chọn
- Loại tra cứu 4: Tra cứu đích, yêu cầu ánh xạ tùy chọn

Đối với loại tra cứu 4, mục 5 là một Destination.

#### Tin nhắn HostReply

Đối với các loại tra cứu 2-4, router phải lấy leaseset,
ngay cả khi khóa tra cứu có trong sổ địa chỉ.

Nếu thành công, HostReply sẽ chứa ánh xạ tùy chọn
từ leaseset, và bao gồm nó như mục 5 sau Destination.
Nếu không có tùy chọn nào trong ánh xạ, hoặc leaseset là phiên bản 1,
nó vẫn sẽ được bao gồm như một ánh xạ rỗng (hai byte: 0 0).
Tất cả các tùy chọn từ leaseset sẽ được bao gồm, không chỉ riêng tùy chọn bản ghi dịch vụ.
Ví dụ, các tùy chọn cho các tham số được định nghĩa trong tương lai có thể hiện diện.

Khi việc tra cứu leaseset thất bại, phản hồi sẽ chứa mã lỗi mới 6 (Leaseset lookup failure)
và sẽ không bao gồm ánh xạ.
Khi mã lỗi 6 được trả về, trường Destination có thể có hoặc không.
Nó sẽ hiện diện nếu tra cứu tên miền trong sổ địa chỉ thành công,
hoặc nếu một lần tra cứu trước đó thành công và kết quả đã được lưu tạm,
hoặc nếu Destination hiện diện trong tin nhắn tra cứu (loại tra cứu 4).

Nếu loại tra cứu không được hỗ trợ,
phản hồi sẽ chứa mã lỗi mới 7 (lookup type unsupported).

### Đặc tả SAM

Giao thức [SAMv3](/docs/api/samv3/) phải được mở rộng để hỗ trợ tra cứu dịch vụ.

Mở rộng NAMING LOOKUP như sau:

NAMING LOOKUP NAME=example.i2p OPTIONS=true yêu cầu ánh xạ tùy chọn trong phản hồi.

NAME có thể là đích base64 đầy đủ khi OPTIONS=true.

Nếu việc tra cứu đích thành công và có tùy chọn trong leaseset,
thì trong phản hồi, sau Destination,
sẽ có một hoặc nhiều tùy chọn dưới dạng OPTION:key=value.
Mỗi tùy chọn sẽ có tiền tố OPTION: riêng biệt.
Tất cả các tùy chọn từ leaseset sẽ được bao gồm, không chỉ riêng tùy chọn bản ghi dịch vụ.
Ví dụ, các tùy chọn cho các tham số được định nghĩa trong tương lai có thể hiện diện.
Ví dụ:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Các khóa chứa '=', và các khóa hoặc giá trị chứa ký tự xuống dòng,
được coi là không hợp lệ và cặp khóa/giá trị sẽ bị loại khỏi phản hồi.

Nếu không tìm thấy tùy chọn nào trong leaseset, hoặc nếu leaseset là phiên bản 1,
phản hồi sẽ không bao gồm tùy chọn nào.

Nếu OPTIONS=true có trong yêu cầu tra cứu, và leaseset không tìm thấy, giá trị kết quả mới LEASESET_NOT_FOUND sẽ được trả về.

## Phương án thay thế tra cứu tên miền

Một thiết kế thay thế đã được xem xét, nhằm hỗ trợ tra cứu dịch vụ
dưới dạng tên miền đầy đủ, ví dụ _smtp._tcp.example.i2p,
bằng cách cập nhật [đặc tả tên miền](/docs/overview/naming/) để xử lý các tên miền bắt đầu bằng '_'.
Phương án này bị từ chối vì hai lý do:

- Vẫn cần thay đổi I2CP và SAM để truyền thông tin TTL và cổng đến máy khách.
- Nó sẽ không phải là một cơ sở tổng quát có thể dùng để truy xuất các tùy chọn LS2 khác
  có thể được định nghĩa trong tương lai.

## Khuyến nghị

Các máy chủ nên chỉ định TTL ít nhất là 86400, và cổng tiêu chuẩn cho ứng dụng.

## Tính năng nâng cao

### Tra cứu đệ quy

Có thể mong muốn hỗ trợ tra cứu đệ quy, nơi mỗi leaseset kế tiếp
được kiểm tra để tìm bản ghi dịch vụ trỏ đến một leaseset khác, theo kiểu DNS.
Điều này có lẽ không cần thiết, ít nhất là trong triển khai ban đầu.

TODO

### Trường riêng cho ứng dụng

Có thể mong muốn có dữ liệu riêng cho ứng dụng trong bản ghi dịch vụ.
Ví dụ, người vận hành example.i2p có thể muốn chỉ ra rằng email nên
được chuyển tiếp đến example@mail.i2p. Phần "example@" cần phải nằm trong một trường riêng
của bản ghi dịch vụ, hoặc bị loại bỏ khỏi đích.

Ngay cả khi người vận hành chạy dịch vụ email riêng, anh ta có thể muốn chỉ ra rằng
email nên được gửi đến example@example.i2p. Hầu hết các dịch vụ I2P được vận hành bởi một người.
Vì vậy, một trường riêng có thể hữu ích trong trường hợp này.

TODO cách thực hiện điều này một cách tổng quát

### Thay đổi cần thiết cho Email

Nằm ngoài phạm vi của đề xuất này. Xem [thảo luận trên i2pforum](http://i2pforum.i2p/viewtopic.php?p=3102) để biết thêm chi tiết.

## Ghi chú triển khai

Việc lưu tạm bản ghi dịch vụ đến TTL có thể được thực hiện bởi router hoặc ứng dụng,
phụ thuộc vào triển khai. Việc có nên lưu tạm lâu dài hay không cũng phụ thuộc vào triển khai.

Các yêu cầu tra cứu cũng phải tra cứu leaseset đích và xác minh rằng nó chứa bản ghi "self"
trước khi trả về đích cho máy khách.

## Phân tích bảo mật

Vì leaseset được ký, bất kỳ bản ghi dịch vụ nào bên trong đều được xác thực bởi khóa ký của đích.

Các bản ghi dịch vụ là công khai và hiển thị với các floodfill, trừ khi leaseset được mã hóa.
Bất kỳ router nào yêu cầu leaseset đều có thể xem các bản ghi dịch vụ.

Một bản ghi SRV khác "self" (tức là, trỏ đến một đích hostname/b32 khác)
không yêu cầu sự đồng ý của hostname/b32 đích.
Không rõ liệu việc chuyển hướng dịch vụ đến một đích tùy ý có thể tạo điều kiện cho một
cuộc tấn công nào đó hay không, hoặc mục đích của cuộc tấn công đó là gì.
Tuy nhiên, đề xuất này giảm thiểu cuộc tấn công bằng cách yêu cầu đích
cũng phải xuất bản bản ghi SRV "self". Người triển khai phải kiểm tra bản ghi "self"
trong leaseset của đích.

## Tương thích

LS2: Không có vấn đề. Tất cả các triển khai hiện tại đều bỏ qua trường tùy chọn trong LS2,
và bỏ qua đúng cách trường tùy chọn không rỗng.
Điều này đã được xác minh trong quá trình thử nghiệm bởi cả Java I2P và i2pd trong quá trình phát triển LS2.
LS2 được triển khai trong 0.9.38 vào năm 2016 và được tất cả các triển khai router hỗ trợ tốt.
Thiết kế không yêu cầu hỗ trợ đặc biệt, bộ nhớ đệm hay bất kỳ thay đổi nào ở các floodfill.

Tên miền: '_' không phải là ký tự hợp lệ trong tên miền i2p.

I2CP: Các loại tra cứu 2-4 không nên được gửi đến các router có phiên bản API thấp hơn
phiên bản tối thiểu mà nó được hỗ trợ (sẽ xác định sau).

SAM: Máy chủ SAM Java bỏ qua các khóa/giá trị bổ sung như OPTIONS=true.
i2pd cũng nên làm như vậy, cần xác minh.
Máy khách SAM sẽ không nhận được các giá trị bổ sung trong phản hồi trừ khi yêu cầu với OPTIONS=true.
Không cần nâng cấp phiên bản.

## Di chuyển

Các triển khai có thể thêm hỗ trợ bất kỳ lúc nào, không cần phối hợp,
ngoại trừ thỏa thuận về phiên bản API hiệu lực cho các thay đổi I2CP.
Các phiên bản tương thích SAM cho từng triển khai sẽ được ghi trong đặc tả SAM.

## Tài liệu tham khảo

* [DOTWELLKNOWN](http://i2pforum.i2p/viewtopic.php?p=3102)
* [I2CP](/docs/specs/i2cp/)
* [I2CP-OPTIONS](/docs/specs/i2cp/)
* [LS2](/docs/specs/common-structures/)
* [GNS](http://zzz.i2p/topcs/1545)
* [NAMING](/docs/overview/naming/)
* [Prop123](/proposals/123-new-netdb-entries/)
* [Prop168](/proposals/168-tunnel-bandwidth/)
* [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
* [RFC2782](https://datatracker.ietf.org/doc/html/rfc2782)
* [SAMv3](/docs/api/samv3/)
* [SRV](https://en.wikipedia.org/wiki/SRV_record)
