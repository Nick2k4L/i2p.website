---
title: "Đề xuất Mẫu Mã hóa Mới"
aliases:
  - "/vi/proposals/142-ecies-template"
  - "/vi/proposals/142-ecies-template/"
number: "142"
author: "zzz"
created: "2018-01-11"
lastupdated: "2018-01-20"
status: "Meta"
thread: "http://zzz.i2p/topics/2499"
toc: true
---
## Tổng quan

Tài liệu này mô tả những vấn đề quan trọng cần xem xét khi đề xuất
thay thế hoặc bổ sung vào hệ mã hóa bất đối xứng ElGamal hiện tại của chúng ta.

Đây là một tài liệu mang tính thông tin.


## Động lực

ElGamal là thuật toán cũ và chậm, và hiện đã có những phương án thay thế tốt hơn.
Tuy nhiên, có một số vấn đề phải được giải quyết trước khi chúng ta có thể thêm hoặc chuyển sang bất kỳ thuật toán mới nào.
Tài liệu này nêu bật các vấn đề chưa được giải quyết này.



## Nghiên cứu nền tảng

Bất kỳ ai đề xuất mã hóa mới đều phải làm quen trước với các tài liệu sau:

- [Đề xuất 111 NTCP2](/proposals/111-ntcp-2/)
- [Đề xuất 123 LS2](/proposals/123-new-netdb-entries/)
- [Đề xuất 136 các kiểu chữ ký thử nghiệm](/proposals/136-experimental-sigtypes/)
- [Đề xuất 137 các kiểu chữ ký tùy chọn](/proposals/137-optional-sigtypes/)
- Các chuỗi thảo luận tại đây cho từng đề xuất nêu trên, được liên kết bên trong
- [Các ưu tiên đề xuất năm 2018](http://zzz.i2p/topics/2494)
- [Đề xuất ECIES](http://zzz.i2p/topics/2418)
- [Tổng quan về mã hóa bất đối xứng mới](http://zzz.i2p/topics/1768)
- [Tổng quan về mã hóa cấp thấp](/docs/specs/common-structures/)


## Các ứng dụng mã hóa bất đối xứng

Để nhắc lại, chúng ta sử dụng ElGamal cho:

1) Các thông điệp xây dựng tunnel (khóa nằm trong RouterIdentity)

2) Mã hóa giữa các router đối với netdb và các thông điệp I2NP khác (Khóa nằm trong RouterIdentity)

3) Mã hóa đầu cuối ElGamal+AES/SessionTag cho client (khóa nằm trong LeaseSet, khóa Destination không được sử dụng)

4) DH tạm thời cho NTCP và SSU


## Thiết kế

Bất kỳ đề xuất nào thay thế ElGamal bằng một phương pháp khác đều phải cung cấp các chi tiết sau.



## Đặc tả

Bất kỳ đề xuất nào về mã hóa bất đối xứng mới đều phải đặc tả đầy đủ những điều sau đây.



### 1. Tổng quát

Hãy trả lời các câu hỏi sau trong đề xuất của bạn. Lưu ý rằng điều này có thể cần một đề xuất riêng biệt so với các chi tiết ở mục 2) bên dưới, vì nó có thể xung đột với các đề xuất hiện tại 111, 123, 136, 137 hoặc các đề xuất khác.

- Bạn đề xuất sử dụng mã hóa mới cho các trường hợp nào trong số các trường hợp 1-4 ở trên?
- Nếu cho 1) hoặc 2) (router), khóa công khai sẽ được đặt ở đâu, trong RouterIdentity hay trong các thuộc tính RouterInfo? Bạn có định sử dụng loại mã hóa trong chứng chỉ khóa không? Hãy đặc tả hoàn toàn. Giải thích rõ ràng cho quyết định của bạn.
- Nếu cho 3) (client), bạn có định lưu khóa công khai trong Destination và sử dụng loại mã hóa trong chứng chỉ khóa (như trong đề xuất ECIES), hay lưu trong LS2 (như trong đề xuất 123), hay một phương án khác? Hãy đặc tả hoàn toàn và giải thích rõ ràng cho quyết định của bạn.
- Đối với mọi ứng dụng, việc hỗ trợ sẽ được công bố như thế nào? Nếu cho 3), liệu nó có nằm trong LS2 hay ở nơi khác? Nếu cho 1) và 2), liệu nó có tương tự như các đề xuất 136 và/hoặc 137 không? Hãy đặc tả hoàn toàn và giải thích rõ ràng cho các quyết định của bạn. Có thể cần một đề xuất riêng cho phần này.
- Hãy đặc tả hoàn toàn cách thức và lý do đảm bảo tính tương thích ngược, đồng thời đặc tả đầy đủ kế hoạch chuyển đổi.
- Những đề xuất nào chưa được triển khai là điều kiện tiên quyết cho đề xuất của bạn?


### 2. Loại mã hóa cụ thể

Hãy trả lời các câu hỏi sau trong đề xuất của bạn:

- Thông tin mã hóa tổng quát, các đường cong/thông số cụ thể, hoàn toàn giải thích rõ ràng cho lựa chọn của bạn. Cung cấp các liên kết đến đặc tả và thông tin khác.
- Kết quả kiểm tra tốc độ so sánh với ElG và các phương án thay thế khác nếu có thể. Bao gồm mã hóa, giải mã và tạo khóa.
- Khả năng sẵn có của thư viện trong C++ và Java (cả OpenJDK, BouncyCastle và bên thứ ba)
  Đối với thư viện bên thứ ba hoặc không phải Java, hãy cung cấp liên kết và giấy phép
- Số hiệu loại mã hóa đề xuất (trong phạm vi thử nghiệm hay không) 




## Ghi chú
