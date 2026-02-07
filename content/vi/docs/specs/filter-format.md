---
title: "Định dạng Bộ lọc Truy cập"
description: "Cú pháp cho các tệp bộ lọc kiểm soát truy cập tunnel"
slug: "filter-format"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
type: docs
---

## Tổng quan

Định nghĩa của một bộ lọc là một danh sách các chuỗi String. Các dòng trống và các dòng bắt đầu bằng `#` sẽ được bỏ qua. Các thay đổi trong định nghĩa bộ lọc sẽ có hiệu lực khi khởi động lại tunnel.

Mỗi dòng có thể đại diện cho một trong những mục sau:

- Định nghĩa một ngưỡng mặc định để áp dụng cho bất kỳ điểm đích từ xa nào không được liệt kê trong tệp này hoặc bất kỳ tệp được tham chiếu nào
- Định nghĩa một ngưỡng để áp dụng cho một điểm đích từ xa cụ thể
- Định nghĩa một ngưỡng để áp dụng cho các điểm đích từ xa được liệt kê trong một tệp
- Định nghĩa một ngưỡng mà nếu bị vi phạm sẽ khiến điểm đích từ xa vi phạm được ghi lại trong một tệp được chỉ định

Thứ tự của các định nghĩa có ý nghĩa quan trọng. Ngưỡng đầu tiên cho một đích đến nhất định (dù được chỉ định rõ ràng hay được liệt kê trong một tệp) sẽ ghi đè bất kỳ ngưỡng nào sau đó cho cùng một đích đến, dù được chỉ định rõ ràng hay được liệt kê trong một tệp.

## Ngưỡng

Ngưỡng được định nghĩa bởi số lần thử kết nối mà một điểm đến từ xa được phép thực hiện trong một khoảng thời gian nhất định tính bằng giây trước khi xảy ra "vi phạm". Ví dụ, định nghĩa ngưỡng `15/5` có nghĩa là cùng một điểm đến từ xa được phép thực hiện 14 lần thử kết nối trong khoảng thời gian 5 giây. Nếu nó thực hiện thêm một lần thử nữa trong cùng khoảng thời gian đó, ngưỡng sẽ bị vi phạm.

Định dạng ngưỡng có thể là một trong những dạng sau:

- **Định nghĩa số** về số lượng kết nối trên số giây - `15/5`, `30/60`, v.v. Lưu ý rằng nếu số lượng kết nối là 1 (ví dụ như trong `1/1`) thì lần thử kết nối đầu tiên sẽ dẫn đến vi phạm ngưỡng.
- Từ **`allow`**. Ngưỡng này không bao giờ bị vi phạm, tức là cho phép số lượng lần thử kết nối vô hạn.
- Từ **`deny`**. Ngưỡng này luôn bị vi phạm, tức là không có lần thử kết nối nào được phép.

### Ngưỡng Mặc định

Ngưỡng mặc định áp dụng cho bất kỳ điểm đến từ xa nào không được liệt kê rõ ràng trong định nghĩa hoặc trong bất kỳ tệp được tham chiếu nào. Để đặt ngưỡng mặc định, sử dụng từ khóa `default`. Dưới đây là các ví dụ về ngưỡng mặc định:

```text
15/5 default
allow default
deny default
```
Chỉ có thể có một định nghĩa ngưỡng mặc định cho mỗi bộ lọc. Nếu bị bỏ qua, bộ lọc sẽ cho phép các kết nối không xác định theo mặc định.

### Ngưỡng Rõ Ràng

Ngưỡng rõ ràng được áp dụng cho một đích từ xa được liệt kê trong chính định nghĩa đó. Ví dụ:

```text
15/5 explicit asdfasdfasdf.b32.i2p
allow explicit fdsafdsafdsa.b32.i2p
deny explicit qwerqwerqwer.b32.i2p
```
### Ngưỡng Hàng Loạt

Để thuận tiện, có thể duy trì danh sách các đích đến trong một tệp và định nghĩa ngưỡng cho tất cả chúng theo lô. Ví dụ:

```text
15/5 file /path/throttled_destinations.txt
deny file /path/forbidden_destinations.txt
allow file /path/unlimited_destinations.txt
```
Những tệp này có thể được chỉnh sửa thủ công trong khi tunnel đang chạy. Các thay đổi đối với những tệp này có thể mất đến 10 giây để có hiệu lực.

## Bộ ghi âm

Recorder theo dõi các lần thử kết nối được thực hiện bởi một destination từ xa, và nếu điều đó vượt quá một ngưỡng nhất định, destination đó sẽ được ghi lại trong một file cho trước. Ví dụ:

```text
30/5 record /path/aggressive.txt
60/5 record /path/very_aggressive.txt
```
Có thể sử dụng một bộ ghi để ghi lại các đích đến tích cực vào một tệp cho trước, sau đó sử dụng cùng tệp đó để điều tiết chúng. Ví dụ, đoạn mã sau sẽ định nghĩa một bộ lọc ban đầu cho phép tất cả các nỗ lực kết nối, nhưng nếu bất kỳ destination đơn lẻ nào vượt quá 30 lần thử trong 5 giây thì nó sẽ bị điều tiết xuống còn 15 lần thử trong 5 giây:

```text
# by default there are no limits
allow default
# but record overly aggressive destinations
30/5 record /path/throttled.txt
# and any that end up in that file will get throttled in the future
15/5 file /path/throttled.txt
```
Có thể sử dụng một bộ ghi âm trong một tunnel để ghi vào một file mà điều chỉnh tốc độ cho một tunnel khác. Có thể tái sử dụng cùng một file với các đích đến trong nhiều tunnel. Và tất nhiên, có thể chỉnh sửa các file này bằng tay.

Đây là một ví dụ về định nghĩa bộ lọc áp dụng một số hạn chế theo mặc định, không hạn chế đối với các destination trong file `friends.txt`, cấm mọi kết nối từ các destination trong file `enemies.txt` và ghi lại bất kỳ hành vi hung hăng nào trong file có tên `suspicious.txt`:

```text
15/5 default
allow file /path/friends.txt
deny file /path/enemies.txt
60/5 record /path/suspicious.txt
```