---
title: "Đệm RI và Điểm đích"
number: "161"
author: "zzz"
created: "2022-09-28"
lastupdated: "2023-01-02"
status: "Open"
thread: "http://zzz.i2p/topics/3279"
target: "0.9.57"
toc: true
---
## Trạng thái

Đã triển khai trong phiên bản 0.9.57.  
Giữ đề xuất này mở để chúng ta có thể cải thiện và thảo luận các ý tưởng trong phần "Kế hoạch tương lai".


## Tổng quan


### Tóm tắt

Khóa công khai ElGamal trong Destinations đã không được sử dụng kể từ phiên bản 0.6 (2005).  
Mặc dù đặc tả của chúng ta nói rằng trường này không được dùng, nhưng đặc tả KHÔNG nói rằng các triển khai có thể tránh việc tạo cặp khóa ElGamal và đơn giản điền trường này bằng dữ liệu ngẫu nhiên.

Chúng tôi đề xuất thay đổi đặc tả để nói rằng  
trường này bị bỏ qua và các triển khai CÓ THỂ điền trường này bằng dữ liệu ngẫu nhiên.  
Thay đổi này tương thích ngược. Không có triển khai nào được biết đến đang xác thực khóa công khai ElGamal.

Ngoài ra, đề xuất này cung cấp hướng dẫn cho các nhà phát triển về cách tạo dữ liệu ngẫu nhiên cho phần đệm (padding) của Destination VÀ Router Identity sao cho dữ liệu này có thể nén tốt, vẫn đảm bảo an toàn, và không khiến biểu diễn Base 64 trông như bị hỏng hoặc không an toàn.  
Việc này mang lại hầu hết lợi ích của việc loại bỏ các trường đệm mà không cần thay đổi giao thức gây gián đoạn.  
Destination có thể nén được sẽ giảm kích thước gói SYN trong streaming và gói datagram có thể trả lời;  
Router Identity có thể nén được sẽ giảm kích thước Database Store Message, gói SSU2 Session Confirmed, và các tệp su3 dùng để reseed.

Cuối cùng, đề xuất này thảo luận về khả năng cho các định dạng mới của Destination và Router Identity  
sẽ loại bỏ hoàn toàn phần đệm. Cũng có một phần thảo luận ngắn về mật mã hậu lượng tử (post-quantum crypto) và cách điều đó có thể ảnh hưởng đến kế hoạch tương lai.



### Mục tiêu

- Loại bỏ yêu cầu tạo cặp khóa ElGamal cho Destinations  
- Đề xuất các phương pháp tốt nhất để Destination và Router Identity có thể nén hiệu quả,  
  nhưng không hiển thị các mẫu rõ ràng trong biểu diễn Base 64.  
- Khuyến khích việc áp dụng các phương pháp tốt nhất bởi mọi triển khai để  
  các trường này không thể phân biệt được  
- Giảm kích thước gói SYN trong streaming  
- Giảm kích thước gói datagram có thể trả lời  
- Giảm kích thước khối RI trong SSU2  
- Giảm kích thước và tần suất phân mảnh của gói SSU2 Session Confirmed  
- Giảm kích thước Database Store Message (có chứa RI)  
- Giảm kích thước tệp reseed  
- Duy trì tính tương thích trong mọi giao thức và API  
- Cập nhật đặc tả  
- Thảo luận các phương án thay thế cho định dạng mới của Destination và Router Identity  

Bằng cách loại bỏ yêu cầu tạo khóa ElGamal, các triển khai có thể  
có khả năng loại bỏ hoàn toàn mã nguồn ElGamal, tùy theo các cân nhắc về tương thích ngược  
trong các giao thức khác.



## Thiết kế

Về mặt kỹ thuật, riêng khóa công khai ký 32 byte (trong cả Destinations và Router Identities)  
và khóa công khai mã hóa 32 byte (chỉ trong Router Identities) là một số ngẫu nhiên  
cung cấp đủ entropy cần thiết để các giá trị băm SHA-256 của các cấu trúc này  
có độ mạnh mật mã cao và phân bố ngẫu nhiên trong DHT cơ sở dữ liệu mạng.

Tuy nhiên, vì cẩn trọng, chúng tôi khuyến nghị sử dụng ít nhất 32 byte dữ liệu ngẫu nhiên  
trong trường khóa công khai ElGamal và phần đệm. Ngoài ra, nếu các trường này toàn là số 0,  
các Destination dạng Base 64 sẽ chứa các chuỗi ký tự AAAA dài, có thể gây lo ngại  
hoặc nhầm lẫn cho người dùng.

Đối với loại chữ ký Ed25519 và loại mã hóa X25519:  
Destinations sẽ chứa 11 bản sao (352 byte) dữ liệu ngẫu nhiên.  
Router Identities sẽ chứa 10 bản sao (320 byte) dữ liệu ngẫu nhiên.



### Ước tính tiết kiệm

Destinations được bao gồm trong mọi gói SYN streaming  
và gói datagram có thể trả lời.  
Router Infos (chứa Router Identities) được bao gồm trong Database Store Messages  
và trong các gói Session Confirmed của NTCP2 và SSU2.

NTCP2 không nén Router Info.  
RIs trong Database Store Messages và SSU2 Session Confirmed được nén gzip.  
Router Infos được nén zip trong các tệp su3 reseed.

Destinations trong Database Store Messages không được nén.  
Các gói SYN streaming được nén gzip ở tầng I2CP.

Đối với loại chữ ký Ed25519 và loại mã hóa X25519,  
ước tính tiết kiệm như sau:

| Loại dữ liệu | Kích thước tổng | Khóa và chứng chỉ | Đệm chưa nén | Đệm đã nén | Kích thước | Tiết kiệm |
|-----------|------------|---------------|----------------------|--------------------|------|---------|
| Destination | 391 | 39 | 352 | 32 | 71 | 320 byte (82%) |
| Router Identity | 391 | 71 | 320 | 32 | 103 | 288 byte (74%) |
| Router Info | 1000 thông thường | 71 | 320 | 32 | 722 thông thường | 288 byte (29%) |

Ghi chú: Giả định chứng chỉ 7 byte không nén được, không có chi phí nén gzip bổ sung.  
Cả hai điều này đều không hoàn toàn đúng, nhưng ảnh hưởng sẽ nhỏ.  
Bỏ qua các phần khác có thể nén được trong Router Info.



## Đặc tả

Các thay đổi đề xuất đối với đặc tả hiện tại được ghi nhận dưới đây.


### Cấu trúc chung
Thay đổi đặc tả cấu trúc chung  
để quy định rằng trường khóa công khai 256 byte của Destination bị bỏ qua và có thể  
chứa dữ liệu ngẫu nhiên.

Thêm một mục vào đặc tả cấu trúc chung  
khuyến nghị phương pháp tốt nhất cho trường khóa công khai Destination và các  
trường đệm trong Destination và Router Identity, như sau:

Tạo 32 byte dữ liệu ngẫu nhiên bằng bộ tạo số ngẫu nhiên mật mã mạnh (PRNG)  
và lặp lại 32 byte đó khi cần để điền vào trường khóa công khai (đối với Destinations)  
và trường đệm (đối với Destinations và Router Identities).


### Tệp khóa riêng
Định dạng tệp khóa riêng (eepPriv.dat) không phải là phần chính thức của đặc tả  
nhưng được tài liệu hóa trong [Java I2P javadocs](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html)  
và các triển khai khác cũng hỗ trợ.  
Việc này cho phép di chuyển khóa riêng giữa các triển khai khác nhau.  
Thêm một ghi chú vào javadoc đó rằng khóa công khai mã hóa có thể là dữ liệu đệm ngẫu nhiên  
và khóa riêng mã hóa có thể là toàn bộ số 0 hoặc dữ liệu ngẫu nhiên.


### SAM
Ghi chú trong đặc tả SAM rằng khóa riêng mã hóa không được dùng và có thể bị bỏ qua.  
Dữ liệu ngẫu nhiên bất kỳ có thể được trả về bởi client.  
SAM Bridge có thể gửi dữ liệu ngẫu nhiên khi tạo (với DEST GENERATE hoặc SESSION CREATE DESTINATION=TRANSIENT)  
thay vì toàn bộ số 0, để biểu diễn Base 64 không chứa chuỗi ký tự AAAA  
và không trông như bị hỏng.


### I2CP
Không cần thay đổi I2CP. Khóa riêng tương ứng với khóa công khai mã hóa trong Destination  
không được gửi đến router.


## Kế hoạch tương lai


### Thay đổi giao thức

Với chi phí là thay đổi giao thức và mất tính tương thích ngược, chúng ta có thể  
thay đổi các giao thức và đặc tả để loại bỏ trường đệm trong  
Destination, Router Identity, hoặc cả hai.

Đề xuất này có một số điểm tương đồng với định dạng leaseset mã hóa "b33",  
chỉ chứa một trường khóa và một trường loại.

Để duy trì một mức độ tương thích, một số tầng giao thức có thể "mở rộng" trường đệm  
với toàn bộ số 0 để trình bày cho các tầng giao thức khác.

Đối với Destinations, chúng ta cũng có thể loại bỏ trường loại mã hóa trong chứng chỉ khóa,  
tiết kiệm được hai byte.  
Hoặc, Destinations có thể nhận một loại mã hóa mới trong chứng chỉ khóa,  
chỉ ra khóa công khai bằng 0 (và phần đệm).

Nếu không có chuyển đổi tương thích giữa định dạng cũ và mới ở một tầng giao thức nào đó,  
các đặc tả, API, giao thức và ứng dụng sau đây sẽ bị ảnh hưởng:

- Đặc tả cấu trúc chung  
- I2NP  
- I2CP  
- NTCP2  
- SSU2  
- Ratchet  
- Streaming  
- SAM  
- Bittorrent  
- Reseeding  
- Tệp khóa riêng  
- API lõi và router Java  
- API i2pd  
- Thư viện SAM của bên thứ ba  
- Công cụ tích hợp và của bên thứ ba  
- Một số plugin Java  
- Giao diện người dùng  
- Ứng dụng P2P ví dụ như MuWire, bitcoin, monero  
- hosts.txt, danh bạ, và đăng ký  

Nếu việc chuyển đổi được quy định ở một tầng nào đó, danh sách sẽ được rút ngắn.

Chi phí và lợi ích của các thay đổi này chưa rõ ràng.

Các đề xuất cụ thể sẽ được xác định sau:





### Khóa PQ

Khóa công khai mã hóa hậu lượng tử (PQ), với bất kỳ thuật toán nào dự kiến,  
lớn hơn 256 byte. Điều này sẽ loại bỏ hoàn toàn phần đệm và mọi lợi ích tiết kiệm từ các  
thay đổi đề xuất ở trên, đối với Router Identities.

Trong cách tiếp cận "lai" (hybrid) PQ, giống như SSL đang làm, các khóa PQ chỉ là tạm thời,  
và sẽ không xuất hiện trong Router Identity.

Khóa ký PQ hiện không khả thi,  
và Destinations không chứa khóa công khai mã hóa.  
Các khóa tĩnh cho ratchet nằm trong Lease Set, không nằm trong Destination.  
do đó chúng ta có thể loại bỏ Destinations khỏi phần thảo luận sau.

Vì vậy PQ chỉ ảnh hưởng đến Router Infos, và chỉ với khóa tĩnh PQ (không phải tạm thời), không ảnh hưởng đến PQ lai.  
Việc này sẽ yêu cầu một loại mã hóa mới và ảnh hưởng đến NTCP2, SSU2, và  
các tin nhắn tra cứu cơ sở dữ liệu mã hóa và phản hồi.  
Khung thời gian ước tính để thiết kế, phát triển và triển khai sẽ là ????????  
Nhưng sẽ diễn ra sau hybrid hoặc ratchet ????????????

Để thảo luận thêm, xem [chủ đề này](http://zzz.i2p/topics/3294).




## Vấn đề

Có thể mong muốn thay đổi khóa mạng từ từ, để che giấu cho các router mới.  
"Thay đổi khóa" (rekeying) có thể chỉ đơn giản là thay đổi phần đệm, không thực sự thay đổi khóa.

Không thể thay đổi khóa cho các Destinations hiện có.

Có nên xác định các Router Identity có phần đệm trong trường khóa công khai bằng một  
loại mã hóa khác trong chứng chỉ khóa không? Việc này sẽ gây ra các vấn đề tương thích.




## Di chuyển

Không có vấn đề tương thích ngược khi thay thế khóa ElGamal bằng phần đệm.

Việc thay đổi khóa (rekeying), nếu được triển khai, sẽ tương tự như những lần  
chuyển đổi danh tính router trước đó:  
Từ chữ ký DSA-SHA1 sang ECDSA, sau đó sang  
chữ ký EdDSA, rồi đến mã hóa X25519.

Tùy theo các vấn đề tương thích ngược, và sau khi tắt SSU,  
các triển khai có thể loại bỏ hoàn toàn mã nguồn ElGamal.  
Khoảng 14% router trong mạng đang dùng loại mã hóa ElGamal, bao gồm nhiều floodfill.

Một yêu cầu hợp nhất bản nháp cho Java I2P đang ở [git.idk.i2p](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66).


## Tài liệu tham khảo

* [Common](/docs/specs/common-structures/)
* [Datagram](/docs/api/datagrams/)
* [I2CP](/docs/specs/i2cp/)
* [I2NP](/docs/specs/i2np/)
* [MR](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66)
* [NTCP2](/docs/specs/ntcp2/)
* [PKF](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html)
* [PQ](http://zzz.i2p/topics/3294)
* [SAM](/docs/api/samv3/)
* [SSU2](/docs/specs/ssu2/)
* [Streaming](/docs/specs/streaming/)
