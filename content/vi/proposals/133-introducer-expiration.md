---
title: "Giới thiệu Hết hạn"
number: "133"
author: "zzz"
created: "2017-02-05"
lastupdated: "2017-08-09"
status: "Closed"
thread: "http://zzz.i2p/topics/2230"
target: "0.9.30"
implementedin: "0.9.30"
toc: true
---
## Tổng quan

Đề xuất này nhằm cải thiện tỷ lệ thành công cho các giới thiệu (introductions).


## Động lực

Các máy giới thiệu (introducers) sẽ hết hạn sau một khoảng thời gian nhất định, nhưng thông tin này không được công bố trong Router Info. Hiện tại, các router phải sử dụng các phương pháp ước lượng (heuristics) để dự đoán khi nào một máy giới thiệu không còn hiệu lực.


## Thiết kế

Trong một địa chỉ Router SSU chứa các máy giới thiệu, người xuất bản có thể tùy chọn thêm thời gian hết hạn cho từng máy giới thiệu.


## Đặc tả

```
iexp{X}={nnnnnnnnnn}

X :: Số thứ tự của máy giới thiệu (0-2)

nnnnnnnnnn :: Thời gian tính bằng giây (không phải mili giây) kể từ thời điểm epoch.
```

### Ghi chú

* Mỗi thời gian hết hạn phải lớn hơn thời điểm công bố của Router Info, và nhỏ hơn 6 giờ so với thời điểm công bố đó.

* Các router xuất bản và các máy giới thiệu nên cố gắng duy trì hiệu lực của máy giới thiệu cho đến khi hết hạn, tuy nhiên không có cách nào để đảm bảo điều này.

* Các router không nên sử dụng một máy giới thiệu đã hết hạn.

* Các thời gian hết hạn của máy giới thiệu nằm trong phần ánh xạ địa chỉ Router (Router Address mapping). Chúng không phải là trường hết hạn 8 byte (hiện chưa dùng) trong địa chỉ Router.

**Ví dụ:** `iexp0=1486309470`


## Di chuyển (Migration)

Không có vấn đề gì. Việc triển khai là tùy chọn.  
Tính tương thích ngược được đảm bảo, vì các router cũ sẽ bỏ qua các tham số không biết.


## Tài liệu tham khảo

* [RouterAddress](/docs/specs/common-structures/#routeraddress)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TRAC-TICKET](http://trac.i2p2.i2p/ticket/1352)
