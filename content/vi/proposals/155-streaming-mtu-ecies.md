---
title: "Truyền trực tuyến MTU cho Điểm đến ECIES"
number: "155"
author: "zzz"
created: "2020-05-06"
lastupdated: "2020-05-30"
status: "Đã đóng"
thread: "http://zzz.i2p/topics/2886"
target: "0.9.47"
implementedin: "0.9.47"
toc: true
---
## Ghi chú
Triển khai và kiểm thử mạng đang được tiến hành.  
Có thể điều chỉnh nhỏ.


## Tổng quan


### Tóm tắt

ECIES giảm khoảng 90 byte chi phí phát sinh từ tin nhắn phiên hiện tại (ES).  
Do đó, chúng ta có thể tăng MTU khoảng 90 byte cho các kết nối ECIES.  
Xem [đặc tả ECIES](/docs/specs/ecies/#overhead), [đặc tả Streaming](/docs/specs/streaming/#flags-and-option-data-fields), và [tài liệu API Streaming](/docs/api/streaming/).

Nếu không tăng MTU, trong nhiều trường hợp thì việc tiết kiệm chi phí này thực tế không được tận dụng,  
vì các tin nhắn vẫn sẽ được đệm để chiếm hai tin nhắn đường hầm đầy đủ.

Đề xuất này không yêu cầu thay đổi bất kỳ đặc tả nào.  
Nó được đăng dưới dạng đề xuất chỉ nhằm tạo điều kiện thảo luận và xây dựng sự đồng thuận  
về giá trị đề xuất và các chi tiết triển khai.


### Mục tiêu

- Tăng MTU đã thương lượng
- Tối đa hóa việc sử dụng tin nhắn đường hầm 1 KB
- Không thay đổi giao thức streaming


## Thiết kế

Sử dụng tùy chọn MAX_PACKET_SIZE_INCLUDED hiện có và cơ chế thương lượng MTU.  
Streaming tiếp tục sử dụng giá trị nhỏ nhất giữa MTU đã gửi và MTU đã nhận.  
Giá trị mặc định vẫn là 1730 cho mọi kết nối, bất kể loại khóa nào được dùng.

Khuyến khích các triển khai bao gồm tùy chọn MAX_PACKET_SIZE_INCLUDED trong mọi gói SYN, theo cả hai hướng,  
mặc dù đây không phải là yêu cầu bắt buộc.

Nếu đích chỉ dùng ECIES, hãy dùng giá trị cao hơn (dù là Alice hay Bob).  
Nếu đích dùng cả hai khóa, hành vi có thể khác nhau:

Nếu khách hàng dùng cả hai khóa nằm ngoài bộ định tuyến (trong ứng dụng bên ngoài),  
nó có thể "không biết" khóa nào đang được dùng ở đầu xa, và Alice có thể yêu cầu  
giá trị cao hơn trong gói SYN, trong khi dữ liệu tối đa trong gói SYN vẫn là 1730.

Nếu khách hàng dùng cả hai khóa nằm trong bộ định tuyến, thông tin về khóa đang dùng  
có thể có hoặc không có sẵn cho khách hàng.  
Leaseset có thể chưa được lấy về, hoặc các giao diện API nội bộ  
có thể không cung cấp dễ dàng thông tin đó cho khách hàng.  
Nếu thông tin có sẵn, Alice có thể dùng giá trị cao hơn;  
nếu không, Alice phải dùng giá trị chuẩn 1730 cho đến khi được thương lượng.

Một khách hàng dùng cả hai khóa với vai trò Bob có thể gửi giá trị cao hơn trong phản hồi,  
ngay cả khi không nhận được giá trị nào hoặc nhận được giá trị 1730 từ Alice;  
tuy nhiên, không có cơ chế thương lượng tăng MTU trong streaming,  
do đó MTU nên giữ nguyên ở mức 1730.


Như đã nêu trong [tài liệu API Streaming](/docs/api/streaming/),  
dữ liệu trong các gói SYN gửi từ Alice đến Bob có thể vượt quá MTU của Bob.  
Đây là điểm yếu trong giao thức streaming.  
Do đó, các khách hàng dùng cả hai khóa phải giới hạn dữ liệu trong gói SYN gửi đi  
ở mức 1730 byte, trong khi gửi tùy chọn MTU cao hơn.  
Sau khi nhận được MTU cao hơn từ Bob, Alice có thể tăng kích thước tải trọng thực tế gửi đi.


### Phân tích

Như mô tả trong [đặc tả ECIES](/docs/specs/ecies/#overhead), chi phí phát sinh ElGamal cho các tin nhắn phiên hiện tại là  
151 byte, và chi phí phát sinh Ratchet là 69 byte.  
Do đó, chúng ta có thể tăng MTU cho các kết nối ratchet thêm (151 - 69) = 82 byte,  
từ 1730 lên 1812.



## Đặc tả

Thêm các thay đổi và làm rõ sau vào phần MTU Selection and Negotiation của [tài liệu API Streaming](/docs/api/streaming/).  
Không có thay đổi nào đối với [đặc tả Streaming](/docs/specs/streaming/).


Giá trị mặc định của tùy chọn i2p.streaming.maxMessageSize vẫn là 1730 cho mọi kết nối, bất kể loại khóa nào được dùng.  
Các khách hàng phải dùng giá trị nhỏ nhất giữa MTU đã gửi và MTU đã nhận, như thông lệ.

Có bốn hằng số và biến MTU liên quan:

- DEFAULT_MTU: 1730, không đổi, cho mọi kết nối
- i2cp.streaming.maxMessageSize: mặc định 1730 hoặc 1812, có thể thay đổi bằng cấu hình
- ALICE_SYN_MAX_DATA: Kích thước dữ liệu tối đa mà Alice có thể đưa vào gói SYN
- negotiated_mtu: Giá trị nhỏ nhất giữa MTU của Alice và Bob, dùng làm kích thước dữ liệu tối đa  
  trong gói SYN ACK từ Bob sang Alice, và trong mọi gói tin tiếp theo được gửi theo cả hai hướng


Có năm trường hợp cần xem xét:


### 1) Alice chỉ dùng ElGamal
Không thay đổi, MTU 1730 trong mọi gói tin.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize mặc định: 1730
- Alice có thể gửi MAX_PACKET_SIZE_INCLUDED trong gói SYN, không bắt buộc trừ khi khác 1730


### 2) Alice chỉ dùng ECIES
MTU 1812 trong mọi gói tin.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize mặc định: 1812
- Alice phải gửi MAX_PACKET_SIZE_INCLUDED trong gói SYN



### 3) Alice dùng cả hai khóa và biết Bob dùng ElGamal
MTU 1730 trong mọi gói tin.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize mặc định: 1812
- Alice có thể gửi MAX_PACKET_SIZE_INCLUDED trong gói SYN, không bắt buộc trừ khi khác 1730



### 4) Alice dùng cả hai khóa và biết Bob dùng ECIES
MTU 1812 trong mọi gói tin.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize mặc định: 1812
- Alice phải gửi MAX_PACKET_SIZE_INCLUDED trong gói SYN



### 5) Alice dùng cả hai khóa và chưa biết khóa của Bob
Gửi 1812 làm MAX_PACKET_SIZE_INCLUDED trong gói SYN nhưng giới hạn dữ liệu gói SYN ở 1730.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize mặc định: 1812
- Alice phải gửi MAX_PACKET_SIZE_INCLUDED trong gói SYN


### Đối với mọi trường hợp

Alice và Bob tính toán  
negotiated_mtu, giá trị nhỏ nhất giữa MTU của Alice và Bob, dùng làm kích thước dữ liệu tối đa  
trong gói SYN ACK từ Bob sang Alice, và trong mọi gói tin tiếp theo được gửi theo cả hai hướng.




## Cơ sở lý luận

Xem [mã nguồn Java I2P](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220) để biết lý do giá trị hiện tại là 1730.  
Xem [đặc tả ECIES](/docs/specs/ecies/#overhead) để biết lý do chi phí phát sinh ECIES ít hơn ElGamal 82 byte.



## Ghi chú triển khai

Nếu streaming tạo ra các tin nhắn có kích thước tối ưu, điều rất quan trọng là  
lớp ECIES-Ratchet không được đệm vượt quá kích thước đó.

Kích thước tối ưu của tin nhắn Garlic để vừa vào hai tin nhắn đường hầm,  
bao gồm phần tiêu đề I2NP của tin nhắn Garlic 16 byte, độ dài tin nhắn Garlic 4 byte,  
thẻ ES 8 byte và MAC 16 byte, là 1956 byte.

Một thuật toán đệm đề xuất trong ECIES như sau:

- Nếu tổng độ dài của tin nhắn Garlic là 1954-1956 byte,  
  không thêm khối đệm (không còn chỗ)
- Nếu tổng độ dài của tin nhắn Garlic là 1938-1953 byte,  
  thêm một khối đệm để đệm chính xác đến 1956 byte.
- Trường hợp khác, đệm như thông lệ, ví dụ với lượng ngẫu nhiên 0-15 byte.

Các chiến lược tương tự có thể được áp dụng ở kích thước tối ưu một tin nhắn đường hầm (964)  
và ba tin nhắn đường hầm (2952), mặc dù các kích thước này trong thực tế hiếm khi xảy ra.



## Vấn đề

Giá trị 1812 là tạm thời. Cần xác nhận và có thể điều chỉnh.




## Di chuyển

Không có vấn đề tương thích ngược.  
Đây là một tùy chọn hiện có và việc thương lượng MTU đã là một phần của đặc tả.

Các đích ECIES cũ sẽ hỗ trợ 1730.  
Bất kỳ khách hàng nào nhận được giá trị cao hơn sẽ phản hồi bằng 1730, và đầu xa  
sẽ thương lượng xuống, như thông lệ.


## Tài liệu tham khảo

* [CALCULATION](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220)
* [ECIES](/docs/specs/ecies/#overhead)
* [STREAMING-OPTIONS](/docs/api/streaming/)
* [STREAMING-SPEC](/docs/specs/streaming/#flags-and-option-data-fields)
