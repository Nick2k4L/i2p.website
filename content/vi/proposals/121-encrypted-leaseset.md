---
title: "LeaseSet Mã hóa"
number: "121"
author: "zzz"
created: "2016-01-11"
lastupdated: "2016-01-12"
status: "Bị từ chối"
thread: "http://zzz.i2p/topics/2047"
supercededby: "123"
toc: true
---
## Tổng quan

Đề xuất này liên quan đến việc thiết kế lại cơ chế mã hóa LeaseSets.


## Động lực

LeaseSet mã hóa hiện tại rất kém và không an toàn. Tôi có thể nói như vậy, vì tôi đã thiết kế và triển khai nó.

Lý do:

- Mã hóa AES CBC
- Một khóa AES duy nhất cho mọi người
- Thời gian hết hạn thuê vẫn暴露
- Khóa công khai mã hóa vẫn暴露


## Thiết kế

### Mục tiêu

- Làm cho toàn bộ quá trình trở nên không rõ ràng
- Khóa cho mỗi người nhận


### Chiến lược

Làm như GPG/OpenPGP. Mã hóa không đối xứng một khóa đối xứng cho mỗi người nhận. Dữ liệu được giải mã với khóa không đối xứng đó. Xem ví dụ [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
Nếu chúng ta có thể tìm thấy một thuật toán nhỏ và nhanh.

Điểm mấu chốt là tìm một mã hóa không đối xứng nhỏ và nhanh. ElGamal với 514 byte là một chút đau đầu ở đây. Chúng ta có thể làm tốt hơn.

Xem ví dụ http://security.stackexchange.com/questions/824...

Điều này hoạt động cho số lượng người nhận nhỏ (hoặc thực sự, khóa; bạn vẫn có thể phân phối khóa cho nhiều người nếu muốn).


## Đặc tả

- Điểm đến
- Thời gian đăng tải
- Thời gian hết hạn
- Flags
- Độ dài dữ liệu
- Dữ liệu mã hóa
- Chữ ký

Dữ liệu mã hóa có thể được đặt trước bằng một số loại mã hóa, hoặc không.


## Tài liệu tham khảo

* [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
