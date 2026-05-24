---
title: "Cờ I2CP cho việc chuyển đổi cổng ra"
number: "171"
author: "onon, eyedeekay"
created: "2026-05-19"
lastupdated: "2026-05-23"
status: "Bản nháp"
toc: true
---

## Tổng quan

Các kết nối client streaming có thể bị đình trệ khi các xác nhận giao hàng bị mất mà không báo hiệu. Bên gửi sẽ truyền lại cho đến khi nhận được xác nhận hoặc kết nối bị ngắt, nhưng không có cách đáng tin cậy nào để xác minh rằng các xác nhận đã đến đích. Đề xuất này thêm một bit cờ mới vào trường cờ của [SendMessageExpiresMessage](/docs/specs/i2cp/) để client có thể chỉ thị cho router chọn một tunnel gửi ra khác cho các tin nhắn tiếp theo đến cùng một đích. Giao thức streaming sử dụng bit này để khởi động việc chuyển tunnel khi phát hiện kết nối bị đình trệ.

## Các trình kích hoạt

Hai điều kiện NÊN khiến cho client thiết lập cờ trên tin nhắn gửi đi tiếp theo. Các điều kiện này được đo ở tầng streaming.

**Phía người gửi**

Chưa nhận được xác nhận nào trong khoảng thời gian chờ truyền lại hiện tại của máy khách.

**Phía bên nhận**

Bên nhận đã quan sát thấy bên từ xa đang truyền lại cùng một dữ liệu hơn một lần, cho thấy các xác nhận của nó không đến được bên từ xa. Bên nhận NÊN đặt cờ này trong tin nhắn I2CP gửi đi tiếp theo để các xác nhận có thể đến được bên từ xa thông qua một đường dẫn khác. Bên nhận PHẢI chờ cho đến khi: (1) đã nhận được một bản sao trùng lặp, (2) đã gửi ít nhất một xác nhận, và (3) bên từ xa đã truyền lại lần nữa trước khi đặt cờ.

Để hạn chế các cuộc tấn công tương quan thời gian, một máy khách KHÔNG ĐƯỢC đặt cờ quá một lần trong mỗi khoảng thời gian 10 giây trên mỗi kết nối. Máy khách NÊN trì hoãn việc đặt cờ bằng một khoảng trễ ngẫu nhiên được chọn đều trong khoảng `[0, min(T/4, 2000ms)]`, trong đó T là thời gian chờ truyền lại hiện tại của máy khách tính bằng mili giây, sau khi phát hiện điều kiện tắc nghẽn, nhằm giảm độ chính xác tương quan thời gian.

## Đặc tả

Trường flags của [SendMessageExpiresMessage](/docs/specs/i2cp/) chiếm 2 byte cao hơn sau trường Date (được định nghĩa lại kể từ phiên bản 0.8.4) và được truyền theo thứ tự big-endian. Bit 15 hiện tại chưa được sử dụng; đề xuất này sẽ định nghĩa nó.

Thứ tự bit: 15...0

| Bit | Tên | Mô tả |
|-----|------|-------------|
| 15 | SWITCH_OUTBOUND_TUNNEL | Nếu bằng 1, router NÊN chọn một tunnel gửi đi khác từ nhóm tunnel hiện có để gửi các tin nhắn tiếp theo đến đích này. Nếu không có tunnel thay thế nào khả dụng, cờ này sẽ bị bỏ qua một cách im lặng. Router KHÔNG ĐƯỢC đóng hoặc loại bỏ tunnel đã sử dụng trước đó chỉ vì cờ này được thiết lập. |
Cờ này mặc định là 0. Các bộ định tuyến không triển khai cờ này PHẢI bỏ qua mà không báo lỗi.

## Ghi chú triển khai

Khi `SWITCH_OUTBOUND_TUNNEL` được thiết lập, bộ định tuyến NÊN chọn một tunnel một cách ngẫu nhiên đều từ nhóm tunnel gửi đi, loại trừ:

- đường hầm đang được sử dụng cho phiên này, và
- đường hầm duy nhất mới nhất đã thất bại trong nhóm, nếu có.

Tất cả các chỉ số sức khỏe tunnel khác, thời gian xây dựng hoặc lịch sử lựa chọn KHÔNG ĐƯỢC ảnh hưởng đến việc lựa chọn, vì việc lựa chọn theo trọng số có thể ưu tiên cho các kẻ tấn công sybil. Nếu sau các loại trừ này, nhóm không còn tunnel nào đủ điều kiện thì cờ sẽ bị bỏ qua một cách im lặng.

Cờ này không làm phát sinh thêm tin nhắn đường hầm; việc chuyển đổi đường hầm có thể làm thay đổi độ trễ biểu kiến. Giới hạn tốc độ 10 giây cho mỗi kết nối (xem Kích hoạt) ngăn chặn việc chuyển đổi quá mức.

## Các cân nhắc về ẩn danh

Các cờ trong [SendMessageExpiresMessage](/docs/specs/i2cp/) được truyền qua I2CP, đây là một giao diện cục bộ giữa máy khách và bộ định tuyến của chính nó. Chúng không hiển thị với những người quan sát mạng.

Rủi ro về ẩn danh dựa trên mẫu lưu lượng: một đối thủ có khả năng quan sát xuyên suốt nhiều điểm cuối của đường hầm có thể theo dõi *thời điểm* việc sử dụng đường hầm thay đổi.

Việc chuyển đổi các tunnel xuất cảnh như một phản ứng trực tiếp đối với tình trạng đình trệ ở phía client sẽ tạo ra một mẫu hành vi có thể phát hiện được. Có hai hướng quan sát cụ thể:

**Tấn công Sybil vào các bước nhảy đầu tiên của tunnel gửi đi**

Chặng đầu tiên của mỗi đường hầm đi ra sẽ nhìn thấy toàn bộ lưu lượng truy cập đi vào đường hầm đó từ bộ định tuyến của người gửi. Một đối thủ kiểm soát chặng đầu tiên của nhiều hơn một đường hầm trong nhóm của người gửi có thể quan sát thấy lưu lượng ngừng trên một chặng đầu tiên và bắt đầu trên một chặng khác trong khoảng thời gian gần nhau, từ đó liên kết cả hai đường hầm với cùng một người gửi. Với một nhóm gồm N đường hầm, một đối thủ kiểm soát K chặng đầu tiên sẽ có xác suất K/N để quan sát được bất kỳ sự kiện chuyển đổi nào.

**Thời gian khoảng trống lưu lượng**

Trong thời gian tạm dừng, máy khách không gửi dữ liệu mới, do đó đường hầm gửi đi cũ trở nên im lặng. Khi việc chuyển đổi xảy ra, lưu lượng sẽ tiếp tục trên một tuyến đường khác. Một đối tượng tấn công có vị trí quan sát được bộ định tuyến của người gửi — ví dụ như nhà cung cấp mạng của người gửi hoặc chính nút bước đầu tiên — có thể nhận thấy mẫu im lặng rồi sau đó tiếp tục này. Thời lượng khoảng trống còn làm rò rỉ thêm một giá trị xấp xỉ thời gian chờ lại hiện tại của máy khách.

Các client PHẢI tuân thủ các yêu cầu về giới hạn tốc độ và độ trễ trong Triggers.

## Tài liệu tham khảo

- [Thông số kỹ thuật I2CP](/docs/specs/i2cp/)
