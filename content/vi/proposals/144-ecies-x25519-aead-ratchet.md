---
title: "ECIES-X25519-AEAD-Ratchet"
aliases:
  - "/vi/proposals/144-ecies-x25519"
  - "/vi/proposals/144-ecies-x25519/"
number: "144"
author: "zzz, chisana, orignal"
created: "2018-11-22"
lastupdated: "2025-03-05"
status: "Đã đóng"
thread: "http://zzz.i2p/topics/2639"
target: "0.9.46"
implementedin: "0.9.46"
toc: true
---
## Ghi chú
Triển khai mạng và kiểm thử đang được tiến hành.
Có thể sửa đổi nhỏ.
Xem [SPEC](/docs/specs/ecies/) để biết thông số kỹ thuật chính thức.

Các tính năng sau chưa được triển khai tính đến phiên bản 0.9.46:

- Các khối MessageNumbers, Options, và Termination
- Phản hồi ở tầng giao thức
- Khóa tĩnh bằng không
- Multicast


## Tổng quan

Đây là đề xuất cho loại mã hóa đầu cuối mới đầu tiên
kể từ khi I2P bắt đầu, nhằm thay thế ElGamal/AES+SessionTags [Elg-AES](/docs/specs/elgamal-aes/).

Nó dựa trên các công việc trước đây như sau:

- Thông số cấu trúc chung [Common Structures](/docs/specs/common-structures/)
- Thông số [I2NP](/docs/specs/i2np/) bao gồm LS2
- ElGamal/AES+Session Tags [Elg-AES](/docs/specs/elgamal-aes/)
- [http://zzz.i2p/topics/1768](http://zzz.i2p/topics/1768) tổng quan về mật mã bất đối xứng mới
- Tổng quan mật mã cấp thấp [CRYPTO-ELG](/docs/specs/cryptography/)
- ECIES [http://zzz.i2p/topics/2418](http://zzz.i2p/topics/2418)
- [NTCP2](/docs/specs/ntcp2/) [Đề xuất 111](/proposals/111-ntcp-2/)
- 123 Các mục netDB mới
- 142 Mẫu mã hóa mới
- [Noise](https://noiseprotocol.org/noise.html) giao thức
- [Signal](https://signal.org/docs/) thuật toán ratchet kép

Mục tiêu là hỗ trợ mã hóa mới cho giao tiếp
từ đầu đến cuối, từ đích đến đích.

Thiết kế sẽ sử dụng handshake Noise và giai đoạn dữ liệu kết hợp thuật toán ratchet kép của Signal.

Tất cả các tham chiếu đến Signal và Noise trong đề xuất này chỉ nhằm mục đích cung cấp thông tin nền.
Không cần phải hiểu các giao thức Signal và Noise để hiểu
hoặc triển khai đề xuất này.


### Các sử dụng hiện tại của ElGamal

Như một phần tổng kết,
các khóa công khai ElGamal 256 byte có thể được tìm thấy trong các cấu trúc dữ liệu sau.
Tham khảo thông số cấu trúc chung.

- Trong một Router Identity
  Đây là khóa mã hóa của router.

- Trong một Destination
  Khóa công khai của đích được dùng cho mã hóa i2cp-to-i2cp cũ
  đã bị tắt từ phiên bản 0.6, hiện tại không dùng ngoại trừ
  IV cho mã hóa LeaseSet, cái này đã lỗi thời.
  Khóa công khai trong LeaseSet được dùng thay thế.

- Trong một LeaseSet
  Đây là khóa mã hóa của đích.

- Trong một LS2
  Đây là khóa mã hóa của đích.



### EncTypes trong Key Certs

Như một phần tổng kết,
chúng tôi đã thêm hỗ trợ cho các loại mã hóa khi thêm hỗ trợ cho các loại chữ ký.
Trường loại mã hóa luôn bằng 0, cả trong Destinations và RouterIdentities.
Việc có nên thay đổi điều này hay không vẫn chưa được quyết định.
Tham khảo thông số cấu trúc chung [Common Structures](/docs/specs/common-structures/).




### Các sử dụng mật mã bất đối xứng

Như một phần tổng kết, chúng tôi dùng ElGamal cho:

1) Các tin nhắn Xây dựng Tunnel (khóa nằm trong RouterIdentity)
   Việc thay thế không được đề cập trong đề xuất này.
   Xem đề xuất 152 [Đề xuất 152](/proposals/152-ecies-tunnels).

2) Mã hóa router-to-router các tin nhắn netdb và I2NP khác (Khóa nằm trong RouterIdentity)
   Phụ thuộc vào đề xuất này.
   Yêu cầu một đề xuất cho 1) hoặc đặt khóa vào các tùy chọn RI.

3) Mã hóa đầu cuối ElGamal+AES/SessionTag của khách hàng (khóa nằm trong LeaseSet, khóa Destination không dùng)
   Việc thay thế ĐƯỢC đề cập trong đề xuất này.

4) DH tạm thời cho NTCP1 và SSU
   Việc thay thế không được đề cập trong đề xuất này.
   Xem đề xuất 111 cho NTCP2.
   Hiện chưa có đề xuất nào cho SSU2.


### Mục tiêu

- Tương thích ngược
- Yêu cầu và xây dựng trên LS2 (đề xuất 123)
- Tận dụng mật mã hoặc nguyên thủy mới được thêm vào cho NTCP2 (đề xuất 111)
- Không yêu cầu mật mã hoặc nguyên thủy mới để hỗ trợ
- Duy trì sự tách biệt giữa mật mã và chữ ký; hỗ trợ tất cả các phiên bản hiện tại và tương lai
- Cho phép mật mã mới cho các đích
- Cho phép mật mã mới cho các router, nhưng chỉ cho các tin nhắn tỏi - việc xây dựng tunnel sẽ
  là một đề xuất riêng
- Không làm hỏng bất cứ thứ gì phụ thuộc vào băm đích nhị phân 32 byte, ví dụ như bittorrent
- Duy trì việc giao tin nhắn 0-RTT bằng cách dùng DH tĩnh-tạm thời
- Không yêu cầu bộ đệm / hàng đợi tin nhắn ở tầng giao thức này;
  tiếp tục hỗ trợ việc giao tin nhắn vô hạn theo cả hai hướng mà không cần chờ phản hồi
- Nâng cấp lên DH tạm thời-tạm thời sau 1 RTT
- Duy trì xử lý tin nhắn không theo thứ tự
- Duy trì bảo mật 256-bit
- Thêm tính bí mật về phía trước
- Thêm xác thực (AEAD)
- Hiệu quả CPU hơn nhiều so với ElGamal
- Không phụ thuộc vào Java jbigi để làm cho DH hiệu quả
- Tối thiểu hóa các thao tác DH
- Hiệu quả băng thông hơn nhiều so với ElGamal (khối ElGamal 514 byte)
- Hỗ trợ mật mã mới và cũ trên cùng một tunnel nếu mong muốn
- Người nhận có thể phân biệt hiệu quả giữa mật mã mới và cũ đến từ
  cùng một tunnel
- Những người khác không thể phân biệt giữa mật mã mới, cũ hoặc tương lai
- Loại bỏ phân loại độ dài phiên mới so với hiện tại (hỗ trợ chèn đệm)
- Không yêu cầu tin nhắn I2NP mới
- Thay thế checksum SHA-256 trong tải AES bằng AEAD
- Hỗ trợ liên kết các phiên truyền và nhận để
  việc xác nhận có thể xảy ra trong giao thức, chứ không chỉ ngoài băng.
  Điều này cũng sẽ cho phép các phản hồi có tính bí mật về phía trước ngay lập tức.
- Cho phép mã hóa đầu cuối cho một số tin nhắn nhất định (lưu trữ RouterInfo)
  mà hiện tại chúng ta không thực hiện do chi phí CPU.
- Không thay đổi tin nhắn Tỏi I2NP
  hoặc định dạng Hướng dẫn Giao tin nhắn Tỏi.
- Loại bỏ các trường không dùng hoặc dư thừa trong định dạng Garlic Clove Set và Clove.

Loại bỏ một số vấn đề với session tags, bao gồm:

- Không thể dùng AES cho đến khi có phản hồi đầu tiên
- Không đáng tin cậy và bị đình trệ nếu giả định việc giao tag
- Không hiệu quả về băng thông, đặc biệt là khi giao lần đầu
- Không hiệu quả về không gian khổng lồ để lưu trữ các tag
- Chi phí băng thông khổng lồ để giao các tag
- Rất phức tạp, khó triển khai
- Khó điều chỉnh cho các trường hợp sử dụng khác nhau
  (streaming so với datagram, server so với client, băng thông cao so với thấp)
- Các lỗ hổng suy kiệt bộ nhớ do việc giao tag


### Mục tiêu không đạt được / Ngoài phạm vi

- Thay đổi định dạng LS2 (đề xuất 123 đã hoàn thành)
- Thuật toán quay DHT mới hoặc tạo số ngẫu nhiên chung
- Mã hóa mới cho việc xây dựng tunnel.
  Xem đề xuất 152 [Đề xuất 152](/proposals/152-ecies-tunnels).
- Mã hóa mới cho mã hóa tầng tunnel.
  Xem đề xuất 153 [Đề xuất 153](/proposals/153-chacha20-layer-encryption).
- Phương pháp mã hóa, truyền và nhận các tin nhắn I2NP DLM / DSM / DSRM.
  Không thay đổi.
- Không hỗ trợ giao tiếp từ LS1-to-LS2 hoặc từ ElGamal/AES sang đề xuất này.
  Đề xuất này là một giao thức hai chiều.
  Các đích có thể xử lý tương thích ngược bằng cách xuất bản hai leaseset
  sử dụng cùng các tunnel, hoặc đặt cả hai loại mã hóa vào LS2.
- Thay đổi mô hình mối đe dọa
- Chi tiết triển khai không được thảo luận ở đây và được để lại cho từng dự án.
- (Tối ưu) Thêm phần mở rộng hoặc móc nối để hỗ trợ multicast



### Lý do

ElGamal/AES+SessionTag đã là giao thức đầu cuối duy nhất của chúng ta trong khoảng 15 năm,
về cơ bản không có sửa đổi nào đối với giao thức.
Hiện nay có các nguyên thủy mật mã nhanh hơn.
Chúng ta cần nâng cao bảo mật của giao thức.
Chúng ta cũng đã phát triển các chiến lược và cách xử lý tạm thời để giảm thiểu
chi phí bộ nhớ và băng thông của giao thức, nhưng những chiến lược đó
rất mong manh, khó điều chỉnh và khiến giao thức dễ bị lỗi hơn,
gây ra việc mất phiên.

Trong khoảng thời gian tương tự, thông số kỹ thuật ElGamal/AES+SessionTag và các tài liệu liên quan
đã mô tả việc giao các session tag tốn băng thông như thế nào,
và đã đề xuất thay thế việc giao session tag bằng một "PRNG đồng bộ".
Một PRNG đồng bộ tạo ra các tag giống nhau ở cả hai đầu một cách xác định,
được suy ra từ một seed chung.
Một PRNG đồng bộ cũng có thể được gọi là một "ratchet".
Đề xuất này (cuối cùng) xác định cơ chế ratchet đó, và loại bỏ việc giao tag.

Bằng cách sử dụng một ratchet (một PRNG đồng bộ) để tạo ra các
session tag, chúng ta loại bỏ chi phí gửi session tag
trong tin nhắn New Session và các tin nhắn tiếp theo khi cần.
Đối với một bộ tag điển hình gồm 32 tag, điều này là 1KB.
Điều này cũng loại bỏ việc lưu trữ session tag ở phía gửi,
do đó giảm yêu cầu lưu trữ xuống một nửa.

Một handshake hai chiều đầy đủ, tương tự như mẫu Noise IK, là cần thiết để tránh các cuộc tấn công Mạo danh do Rò rỉ Khóa (KCI).
Xem bảng "Tính năng Bảo mật Payload" trong [NOISE](https://noiseprotocol.org/noise.html).
Để biết thêm thông tin về KCI, xem bài báo https://www.usenix.org/system/files/conference/woot15/woot15-paper-hlauschek.pdf



### Mô hình mối đe dọa

Mô hình mối đe dọa hơi khác so với NTCP2 (đề xuất 111).
Các nút MitM là OBEP và IBGW và được giả định có toàn quyền xem
cơ sở dữ liệu mạng toàn cầu hiện tại hoặc lịch sử, bằng cách thông đồng với các floodfill.

Mục tiêu là ngăn chặn các MitM này phân loại lưu lượng là
tin nhắn phiên mới và hiện tại, hoặc là mật mã mới so với cũ.



## Đề xuất chi tiết

Đề xuất này định nghĩa một giao thức đầu cuối mới để thay thế ElGamal/AES+SessionTags.
Thiết kế sẽ sử dụng handshake Noise và giai đoạn dữ liệu kết hợp ratchet kép của Signal.


### Tóm tắt thiết kế mật mã

Có năm phần của giao thức cần được thiết kế lại:


- 1) Các định dạng container phiên mới và hiện tại
  được thay thế bằng các định dạng mới.
- 2) ElGamal (khóa công khai 256 byte, khóa riêng 128 byte) sẽ được thay thế
  bằng ECIES-X25519 (khóa công khai và riêng 32 byte)
- 3) AES sẽ được thay thế bằng
  AEAD_ChaCha20_Poly1305 (viết tắt là ChaChaPoly bên dưới)
- 4) SessionTags sẽ được thay thế bằng ratchets,
  về cơ bản là một PRNG mật mã, đồng bộ.
- 5) Tải AES, như được định nghĩa trong thông số kỹ thuật ElGamal/AES+SessionTags,
  được thay thế bằng định dạng khối tương tự như trong NTCP2.

Mỗi thay đổi trong năm thay đổi trên đều có phần riêng bên dưới.


### Các nguyên thủy mật mã mới cho I2P

Các triển khai router I2P hiện tại sẽ yêu cầu triển khai các
nguyên thủy mật mã chuẩn sau,
không bắt buộc cho các giao thức I2P hiện tại:

- ECIES (nhưng về cơ bản là X25519)
- Elligator2

Các triển khai router I2P hiện tại chưa triển khai [NTCP2](/docs/specs/ntcp2/) ([Đề xuất 111](/proposals/111-ntcp-2/))
cũng sẽ yêu cầu triển khai cho:

- Tạo khóa và DH X25519
- AEAD_ChaCha20_Poly1305 (viết tắt là ChaChaPoly bên dưới)
- HKDF


### Loại mã hóa

Loại mã hóa (dùng trong LS2) là 4.
Điều này chỉ ra khóa công khai X25519 32 byte theo thứ tự nhỏ,
và giao thức đầu cuối được chỉ định ở đây.

Loại mã hóa 0 là ElGamal.
Các loại mã hóa 1-3 dành riêng cho ECIES-ECDH-AES-SessionTag, xem đề xuất 145 [Đề xuất 145](/proposals/145-ecies).


### Khung giao thức Noise

Đề xuất này cung cấp các yêu cầu dựa trên Khung giao thức Noise
[NOISE](https://noiseprotocol.org/noise.html) (Phiên bản 34, 2018-07-11).
Noise có các tính chất tương tự như giao thức Station-To-Station
[STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol), là cơ sở cho giao thức [SSU](/docs/legacy/ssu/). Trong thuật ngữ Noise, Alice
là người khởi tạo, và Bob là người phản hồi.

Đề xuất này dựa trên giao thức Noise Noise_IK_25519_ChaChaPoly_SHA256.
(Mã định danh thực tế cho hàm suy diễn khóa ban đầu
là "Noise_IKelg2_25519_ChaChaPoly_SHA256"
để chỉ ra các phần mở rộng I2P - xem phần KDF 1 bên dưới)
Giao thức Noise này sử dụng các nguyên thủy sau:

- Mẫu Handshake Tương tác: IK
  Alice ngay lập tức truyền khóa tĩnh của mình cho Bob (I)
  Alice đã biết khóa tĩnh của Bob (K)

- Mẫu Handshake Một chiều: N
  Alice không truyền khóa tĩnh của mình cho Bob (N)

- Hàm DH: X25519
  DH X25519 với độ dài khóa 32 byte như được chỉ định trong [RFC-7748](https://tools.ietf.org/html/rfc7748).

- Hàm Mã hóa: ChaChaPoly
  AEAD_CHACHA20_POLY1305 như được chỉ định trong [RFC-7539](https://tools.ietf.org/html/rfc7539) mục 2.8.
  Nonce 12 byte, với 4 byte đầu tiên đặt bằng 0.
  Giống hệt như trong [NTCP2](/docs/specs/ntcp2/).

- Hàm Băm: SHA256
  Băm tiêu chuẩn 32 byte, đã được sử dụng rộng rãi trong I2P.


### Các bổ sung cho khung

Đề xuất này định nghĩa các cải tiến sau cho
Noise_IK_25519_ChaChaPoly_SHA256. Những cải tiến này nói chung tuân theo các hướng dẫn trong
[NOISE](https://noiseprotocol.org/noise.html) mục 13.

1) Các khóa tạm thời rõ ràng được mã hóa bằng [Elligator2](https://elligator.cr.yp.to/).

2) Phản hồi được đặt tiền tố bằng một thẻ rõ ràng.

3) Định dạng tải được định nghĩa cho các tin nhắn 1, 2 và giai đoạn dữ liệu.
   Tất nhiên, điều này không được định nghĩa trong Noise.

Tất cả các tin nhắn đều bao gồm tiêu đề Tin nhắn Tỏi [I2NP](/docs/specs/i2np/).
Giai đoạn dữ liệu sử dụng mã hóa tương tự như, nhưng không tương thích với, giai đoạn dữ liệu Noise.


### Các mẫu Handshake

Các handshake sử dụng các mẫu handshake [Noise](https://noiseprotocol.org/noise.html).

Ánh xạ chữ cái sau được sử dụng:

- e = khóa tạm thời dùng một lần
- s = khóa tĩnh
- p = tải tin nhắn

Các phiên một lần và không ràng buộc tương tự như mẫu Noise N.

```

<- s
  ...
  e es p ->

```

Các phiên ràng buộc tương tự như mẫu Noise IK.

```

<- s
  ...
  e es s ss p ->
  <- tag e ee se
  <- p
  p ->

```


### Các phiên

Giao thức ElGamal/AES+SessionTag hiện tại là một chiều.
Ở tầng này, người nhận không biết tin nhắn đến từ đâu.
Các phiên gửi và nhận không được liên kết.
Các xác nhận nằm ngoài băng bằng cách sử dụng DeliveryStatusMessage
(được gói trong một GarlicMessage) trong nhánh tỏi.

Có sự kém hiệu quả đáng kể trong một giao thức một chiều.
Bất kỳ phản hồi nào cũng phải sử dụng tin nhắn 'New Session' tốn kém.
Điều này gây ra việc sử dụng băng thông, CPU và bộ nhớ cao hơn.

Cũng có những điểm yếu về bảo mật trong một giao thức một chiều.
Tất cả các phiên đều dựa trên DH tạm thời-tĩnh.
Không có đường hồi, Bob không thể "ratchet" khóa tĩnh của mình
thành khóa tạm thời.
Không biết tin nhắn đến từ đâu, không thể sử dụng
khóa tạm thời nhận được cho các tin nhắn gửi đi,
do đó phản hồi ban đầu cũng sử dụng DH tạm thời-tĩnh.

Đối với đề xuất này, chúng tôi định nghĩa hai cơ chế để tạo giao thức hai chiều -
"ghép nối" và "liên kết".
Các cơ chế này cung cấp hiệu quả và bảo mật cao hơn.


### Bối cảnh phiên

Giống như ElGamal/AES+SessionTags, tất cả các phiên gửi và nhận
phải nằm trong một bối cảnh nhất định, hoặc là bối cảnh của router hoặc
bối cảnh cho một đích cục bộ cụ thể.
Trong Java I2P, bối cảnh này được gọi là Session Key Manager.

Các phiên không được chia sẻ giữa các bối cảnh, vì điều đó sẽ
cho phép liên kết giữa các đích cục bộ khác nhau,
hoặc giữa một đích cục bộ và một router.

Khi một đích cụ thể hỗ trợ cả ElGamal/AES+SessionTags
và đề xuất này, cả hai loại phiên có thể chia sẻ một bối cảnh.
Xem phần 1c) bên dưới.



### Ghép nối các phiên gửi và nhận

Khi một phiên gửi được tạo tại người khởi tạo (Alice),
một phiên nhận mới được tạo và ghép nối với phiên gửi,
trừ khi không mong đợi phản hồi (ví dụ như datagram thô).

Một phiên nhận mới luôn được ghép nối với một phiên gửi mới,
trừ khi không yêu cầu phản hồi (ví dụ như datagram thô).

Nếu yêu cầu phản hồi và liên kết với một đích hoặc router ở xa,
phiên gửi mới đó sẽ được liên kết với đích hoặc router đó,
và thay thế bất kỳ phiên gửi nào trước đó đến đích hoặc router đó.

Việc ghép nối các phiên gửi và nhận cung cấp một giao thức hai chiều
với khả năng ratchet các khóa DH.



### Liên kết các phiên và đích

Chỉ có một phiên gửi đến một đích hoặc router nhất định.
Có thể có nhiều phiên nhận hiện tại từ một đích hoặc router nhất định.
Thông thường, khi một phiên nhận mới được tạo, và lưu lượng được nhận
trên phiên đó (điều này đóng vai trò là ACK), các phiên khác sẽ được đánh dấu
để hết hạn tương đối nhanh, trong khoảng một phút hoặc hơn.
Giá trị tin nhắn đã gửi trước (PN) được kiểm tra, và nếu không có
tin nhắn chưa nhận (trong kích thước cửa sổ) trong phiên nhận trước đó,
phiên trước đó có thể bị xóa ngay lập tức.


Khi một phiên gửi được tạo tại người khởi tạo (Alice),
nó được liên kết với đích ở xa (Bob),
và bất kỳ phiên nhận ghép nối nào cũng sẽ được liên kết với đích ở xa.
Khi các phiên ratchet, chúng tiếp tục được liên kết với đích ở xa.

Khi một phiên nhận được tạo tại người nhận (Bob),
nó có thể được liên kết với đích ở xa (Alice), theo lựa chọn của Alice.
Nếu Alice bao gồm thông tin liên kết (khóa tĩnh của cô ấy) trong tin nhắn New Session,
phiên sẽ được liên kết với đích đó,
và một phiên gửi sẽ được tạo và liên kết với cùng đích.
Khi các phiên ratchet, chúng tiếp tục được liên kết với đích ở xa.


### Lợi ích của việc Liên kết và Ghép nối

Đối với trường hợp phổ biến, streaming, chúng tôi mong đợi Alice và Bob sử dụng giao thức như sau:

- Alice ghép phiên gửi mới của cô ấy với một phiên nhận mới, cả hai đều liên kết với đích ở xa (Bob).
- Alice bao gồm thông tin liên kết và chữ ký, và yêu cầu phản hồi, trong
  tin nhắn New Session gửi đến Bob.
- Bob ghép phiên nhận mới của anh ấy với một phiên gửi mới, cả hai đều liên kết với đích ở xa (Alice).
- Bob gửi phản hồi (ack) cho Alice trong phiên ghép nối, với ratchet đến khóa DH mới.
- Alice ratchet đến phiên gửi mới với khóa mới của Bob, ghép nối với phiên nhận hiện tại.

Bằng cách liên kết một phiên nhận với một đích ở xa, và ghép nối phiên nhận
với một phiên gửi liên kết với cùng đích, chúng ta đạt được hai lợi ích lớn:

1) Phản hồi ban đầu từ Bob đến Alice sử dụng DH tạm thời-tạm thời

2) Sau khi Alice nhận được phản hồi của Bob và ratchet, tất cả các tin nhắn tiếp theo từ Alice đến Bob
sử dụng DH tạm thời-tạm thời.


### Xác nhận tin nhắn

Trong ElGamal/AES+SessionTags, khi một LeaseSet được gói như một nhánh tỏi,
hoặc các tag được giao, router gửi yêu cầu ACK.
Đây là một nhánh tỏi riêng biệt chứa DeliveryStatus Message.
Để tăng bảo mật, DeliveryStatus Message được gói trong một Tin nhắn Tỏi.
Cơ chế này nằm ngoài băng từ góc độ giao thức.

Trong giao thức mới, vì các phiên gửi và nhận được ghép nối,
chúng ta có thể có ACK trong băng. Không cần nhánh riêng biệt.

Một ACK rõ ràng đơn giản là một tin nhắn Existing Session không có khối I2NP.
Tuy nhiên, trong hầu hết các trường hợp, có thể tránh ACK rõ ràng, vì có lưu lượng ngược.
Có thể mong muốn các triển khai chờ một thời gian ngắn (có thể vài trăm ms)
trước khi gửi ACK rõ ràng, để cho tầng streaming hoặc ứng dụng có thời gian phản hồi.

Triển khai cũng cần trì hoãn việc gửi bất kỳ ACK nào cho đến sau khi
khối I2NP được xử lý, vì Tin nhắn Tỏi có thể chứa Database Store Message
với một lease set. Một lease set mới nhất sẽ cần thiết để định tuyến ACK,
và đích ở xa (chứa trong lease set) sẽ cần thiết để
xác minh khóa tĩnh liên kết.


### Hết hạn phiên

Các phiên gửi nên luôn hết hạn trước các phiên nhận.
Khi một phiên gửi hết hạn, và một phiên mới được tạo, một phiên nhận ghép nối mới
cũng sẽ được tạo. Nếu có một phiên nhận cũ,
nó sẽ được phép hết hạn.


### Multicast

TBD


### Định nghĩa
Chúng tôi định nghĩa các hàm sau tương ứng với các khối xây dựng mật mã được sử dụng.

ZEROLEN
    mảng byte độ dài bằng không

CSRNG(n)
    đầu ra n-byte từ một bộ tạo số ngẫu nhiên mật mã.

H(p, d)
    hàm băm SHA-256 nhận một chuỗi cá nhân hóa p và dữ liệu d, và
    tạo ra đầu ra độ dài 32 byte.
    Như được định nghĩa trong [NOISE](https://noiseprotocol.org/noise.html).
    || bên dưới có nghĩa là nối.

    Sử dụng SHA-256 như sau::

        H(p, d) := SHA-256(p || d)

MixHash(d)
    hàm băm SHA-256 nhận một băm trước đó h và dữ liệu mới d,
    và tạo ra đầu ra độ dài 32 byte.
    || bên dưới có nghĩa là nối.

    Sử dụng SHA-256 như sau::

        MixHash(d) := h = SHA-256(h || d)

STREAM
    AEAD ChaCha20/Poly1305 như được chỉ định trong [RFC-7539](https://tools.ietf.org/html/rfc7539).
    S_KEY_LEN = 32 và S_IV_LEN = 12.

    ENCRYPT(k, n, plaintext, ad)
        Mã hóa plaintext bằng khóa mã hóa k, và nonce n phải là duy nhất cho
        khóa k.
        Dữ liệu liên kết ad là tùy chọn.
        Trả về một bản mã có kích thước bằng plaintext + 16 byte cho HMAC.

        Bản mã hoàn chỉnh phải không thể phân biệt với dữ liệu ngẫu nhiên nếu khóa được giữ bí mật.

    DECRYPT(k, n, ciphertext, ad)
        Giải mã ciphertext bằng khóa mã hóa k, và nonce n.
        Dữ liệu liên kết ad là tùy chọn.
        Trả về plaintext.

DH
    Hệ thống thỏa thuận khóa công khai X25519. Khóa riêng 32 byte, khóa công khai 32
    byte, tạo ra đầu ra 32 byte. Nó có các
    hàm sau:

    GENERATE_PRIVATE()
        Tạo một khóa riêng mới.

    DERIVE_PUBLIC(privkey)
        Trả về khóa công khai tương ứng với khóa riêng đã cho.

    GENERATE_PRIVATE_ELG2()
        Tạo một khóa riêng mới ánh xạ đến một khóa công khai phù hợp để mã hóa Elligator2.
        Lưu ý rằng một nửa các khóa riêng được tạo ngẫu nhiên sẽ không phù hợp và phải bị loại bỏ.

    ENCODE_ELG2(pubkey)
        Trả về khóa công khai được mã hóa Elligator2 tương ứng với khóa công khai đã cho (ánh xạ ngược).
        Các khóa được mã hóa là theo thứ tự nhỏ.
        Khóa được mã hóa phải là 256 bit không thể phân biệt với dữ liệu ngẫu nhiên.
        Xem phần Elligator2 bên dưới để biết thông số kỹ thuật.

    DECODE_ELG2(pubkey)
        Trả về khóa công khai tương ứng với khóa công khai được mã hóa Elligator2 đã cho.
        Xem phần Elligator2 bên dưới để biết thông số kỹ thuật.

    DH(privkey, pubkey)
        Tạo một bí mật chung từ khóa riêng và khóa công khai đã cho.

HKDF(salt, ikm, info, n)
    Một hàm suy diễn khóa mật mã nhận một số liệu khóa đầu vào ikm (cái này
    nên có entropy tốt nhưng không yêu cầu phải là chuỗi ngẫu nhiên đều), một muối
    độ dài 32 byte, và một giá trị 'info' cụ thể theo ngữ cảnh, và tạo ra một đầu ra
    n byte phù hợp để dùng làm liệu khóa.

    Sử dụng HKDF như được chỉ định trong [RFC-5869](https://tools.ietf.org/html/rfc5869), sử dụng hàm băm HMAC SHA-256
    như được chỉ định trong [RFC-2104](https://tools.ietf.org/html/rfc2104). Điều này có nghĩa là SALT_LEN tối đa là 32 byte.

MixKey(d)
    Sử dụng HKDF() với một chainKey trước đó và dữ liệu mới d, và
    đặt chainKey mới và k.
    Như được định nghĩa trong [NOISE](https://noiseprotocol.org/noise.html).

    Sử dụng HKDF như sau::

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]



### 1) Định dạng tin nhắn


### Tổng kết định dạng tin nhắn hiện tại

Tin nhắn Tỏi như được chỉ định trong [I2NP](/docs/specs/i2np/) như sau.
Với mục tiêu thiết kế là các nút trung gian không thể phân biệt mật mã mới và cũ,
định dạng này không thể thay đổi, mặc dù trường độ dài là dư thừa.
Định dạng được hiển thị với tiêu đề đầy đủ 16 byte, mặc dù tiêu đề
thực tế có thể ở định dạng khác, tùy thuộc vào phương tiện truyền tải được sử dụng.

Khi được giải mã, dữ liệu chứa một chuỗi các Garlic Cloves và dữ liệu bổ sung,
còn được gọi là Clove Set.

Xem [I2NP](/docs/specs/i2np/) để biết chi tiết và thông số kỹ thuật đầy đủ.


```

+----+----+----+----+----+----+----+----+
  |type|      msg_id       |  expiration
  +----+----+----+----+----+----+----+----+
                           |  size   |chks|
  +----+----+----+----+----+----+----+----+
  |      length       |                   |
  +----+----+----+----+                   +
  |          encrypted data               |
  ~                                       ~
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

```


### Tổng kết định dạng dữ liệu được mã hóa

Định dạng tin nhắn hiện tại, được sử dụng hơn 15 năm,
là ElGamal/AES+SessionTags.
Trong ElGamal/AES+SessionTags, có hai định dạng tin nhắn:

1) Phiên mới:
- Khối ElGamal 514 byte
- Khối AES (tối thiểu 128 byte, bội số của 16)

2) Phiên hiện tại:
- Thẻ Session 32 byte
- Khối AES (tối thiểu 128 byte, bội số của 16)

Việc đệm tối thiểu đến 128 là như được triển khai trong Java I2P nhưng không được áp đặt khi nhận.

Các tin nhắn này được đóng gói trong một tin nhắn tỏi I2NP, chứa
trường độ dài, do đó độ dài được biết.

Lưu ý rằng không có việc đệm được định nghĩa đến độ dài không chia hết cho 16,
do đó phiên mới luôn (mod 16 == 2),
và một phiên hiện tại luôn (mod 16 == 0).
Chúng ta cần sửa điều này.

Người nhận trước tiên cố gắng tra cứu 32 byte đầu tiên như một Thẻ Session.
Nếu tìm thấy, anh ta giải mã khối AES.
Nếu không tìm thấy, và dữ liệu dài ít nhất (514+16), anh ta cố gắng giải mã khối ElGamal,
và nếu thành công, giải mã khối AES.


### Thẻ phiên mới và so sánh với Signal

Trong Signal Double Ratchet, tiêu đề chứa:

- DH: Khóa công khai ratchet hiện tại
- PN: Độ dài chuỗi tin nhắn trước đó
- N: Số tin nhắn

"chuỗi gửi" của Signal tương đương với bộ thẻ của chúng ta.
Bằng cách sử dụng một thẻ phiên, chúng ta có thể loại bỏ phần lớn điều đó.

Trong Phiên mới, chúng ta chỉ đặt khóa công khai vào tiêu đề không mã hóa.

Trong Phiên hiện tại, chúng ta sử dụng một thẻ phiên cho tiêu đề.
Thẻ phiên được liên kết với khóa công khai ratchet hiện tại,
và số tin nhắn.

Trong cả phiên mới và hiện tại, PN và N nằm trong phần được mã hóa.

Trong Signal, mọi thứ liên tục ratchet. Một khóa công khai DH mới yêu cầu
người nhận ratchet và gửi lại khóa công khai mới, điều này cũng phục vụ
như xác nhận cho khóa công khai đã nhận.
Điều này sẽ quá nhiều thao tác DH đối với chúng ta.
Vì vậy, chúng ta tách việc xác nhận khóa đã nhận và việc truyền khóa công khai mới.
Bất kỳ tin nhắn nào sử dụng thẻ phiên được tạo từ khóa DH mới đều cấu thành một ACK.
Chúng ta chỉ truyền khóa công khai mới khi muốn thay khóa.

Số lượng tin nhắn tối đa trước khi DH phải ratchet là 65535.

Khi giao một khóa phiên, chúng ta suy ra "Bộ thẻ" từ nó,
thay vì phải giao cả thẻ phiên.
Một Bộ thẻ có thể lên đến 65536 thẻ.
Tuy nhiên, người nhận nên triển khai chiến lược "nhìn trước",
thay vì tạo tất cả các thẻ có thể cùng một lúc.
Chỉ tạo tối đa N thẻ sau thẻ tốt cuối cùng đã nhận.
N có thể tối đa là 128, nhưng 32 hoặc ít hơn có thể là lựa chọn tốt hơn.



### 1a) Định dạng phiên mới

Thẻ công khai tạm thời phiên mới (32 byte)
Dữ liệu được mã hóa và MAC (các byte còn lại)

Tin nhắn Phiên mới có thể hoặc không chứa khóa công khai tĩnh của người gửi.
Nếu được bao gồm, phiên ngược lại được liên kết với khóa đó.
Khóa tĩnh nên được bao gồm nếu mong đợi phản hồi,
tức là cho streaming và datagram có thể phản hồi.
Nó không nên được bao gồm cho datagram thô.

Tin nhắn Phiên mới tương tự như mẫu Noise một chiều [NOISE](https://noiseprotocol.org/noise.html)
"N" (nếu khóa tĩnh không được gửi),
hoặc mẫu hai chiều "IK" (nếu khóa tĩnh được gửi).



### 1b) Định dạng phiên mới (có liên kết)

Độ dài là 96 + độ dài tải.
Định dạng được mã hóa:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   Khóa công khai tạm thời Phiên mới   |
  +             32 byte                   +
  |     Được mã hóa bằng Elligator2       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +         Khóa tĩnh                   +
  |       Dữ liệu được mã hóa ChaCha20    |
  +            32 byte                    +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Mã xác thực tin nhắn Poly1305        |
  +    (MAC) cho phần Khóa tĩnh         +
  |             16 byte                   |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Phần tải                 +
  |       Dữ liệu được mã hóa ChaCha20    |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Mã xác thực tin nhắn Poly1305        |
  +         (MAC) cho phần tải          +
  |             16 byte                   |
  +----+----+----+----+----+----+----+----+

  Khóa công khai :: 32 byte, theo thứ tự nhỏ, Elligator2, rõ ràng

  Dữ liệu được mã hóa Khóa tĩnh :: 32 byte

  Dữ liệu được mã hóa phần tải :: dữ liệu còn lại trừ 16 byte

  MAC :: mã xác thực tin nhắn Poly1305, 16 byte

```


### Khóa tạm thời phiên mới

Khóa tạm thời là 32 byte, được mã hóa bằng Elligator2.
Khóa này không bao giờ được sử dụng lại; một khóa mới được tạo với
mỗi tin nhắn, bao gồm cả việc truyền lại.

### Khóa tĩnh

Khi được giải mã, khóa tĩnh X25519 của Alice, 32 byte.


### Tải

Độ dài được mã hóa là phần còn lại của dữ liệu.
Độ dài được giải mã ít hơn 16 byte so với độ dài được mã hóa.
Tải phải chứa một khối DateTime và thường sẽ chứa một hoặc nhiều khối Garlic Clove.
Xem phần tải bên dưới để biết định dạng và các yêu cầu bổ sung.



### 1c) Định dạng phiên mới (không có liên kết)

Nếu không cần phản hồi, không gửi khóa tĩnh nào.


Độ dài là 96 + độ dài tải.
Định dạng được mã hóa:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   Khóa công khai tạm thời Phiên mới   |
  +             32 byte                   +
  |     Được mã hóa bằng Elligator2       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Phần cờ                   +
  |       Dữ liệu được mã hóa ChaCha20    |
  +            32 byte                    +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Mã xác thực tin nhắn Poly1305        |
  +         (MAC) cho phần trên         +
  |             16 byte                   |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Phần tải                 +
  |       Dữ liệu được mã hóa ChaCha20    |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Mã xác thực tin nhắn Poly1305        |
  +         (MAC) cho phần tải          +
  |             16 byte                   |
  +----+----+----+----+----+----+----+----+

  Khóa công khai :: 32 byte, theo thứ tự nhỏ, Elligator2, rõ ràng

  Dữ liệu được mã hóa phần cờ :: 32 byte

  Dữ liệu được mã hóa phần tải :: dữ liệu còn lại trừ 16 byte

  MAC :: mã xác thực tin nhắn Poly1305, 16 byte

```

### Khóa tạm thời phiên mới

Khóa tạm thời của Alice.
Khóa tạm thời là 32 byte, được mã hóa bằng Elligator2, theo thứ tự nhỏ.
Khóa này không bao giờ được sử dụng lại; một khóa mới được tạo với
mỗi tin nhắn, bao gồm cả việc truyền lại.


### Dữ liệu giải mã phần cờ

Phần cờ không chứa gì cả.
Nó luôn là 32 byte, vì nó phải có cùng độ dài
với khóa tĩnh cho các tin nhắn Phiên mới có liên kết.
Bob xác định liệu đó là khóa tĩnh hay phần cờ
bằng cách kiểm tra xem 32 byte có phải là toàn bộ số 0 hay không.

TODO có cần cờ nào ở đây không?

### Tải

Độ dài được mã hóa là phần còn lại của dữ liệu.
Độ dài được giải mã ít hơn 16 byte so với độ dài được mã hóa.
Tải phải chứa một khối DateTime và thường sẽ chứa một hoặc nhiều khối Garlic Clove.
Xem phần tải bên dưới để biết định dạng và các yêu cầu bổ sung.




### 1d) Định dạng một lần (không có liên kết hoặc phiên)

Nếu chỉ mong đợi gửi một tin nhắn duy nhất,
không cần thiết lập phiên hoặc khóa tĩnh.


Độ dài là 96 + độ dài tải.
Định dạng được mã hóa:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |       Khóa công khai tạm thời         |
  +             32 byte                   +
  |     Được mã hóa bằng Elligator2       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Phần cờ                   +
  |       Dữ liệu được mã hóa ChaCha20    |
  +            32 byte                    +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Mã xác thực tin nhắn Poly1305        |
  +         (MAC) cho phần trên         +
  |             16 byte                   |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Phần tải                 +
  |       Dữ liệu được mã hóa ChaCha20    |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Mã xác thực tin nhắn Poly1305        |
  +         (MAC) cho phần tải          +
  |             16 byte                   |
  +----+----+----+----+----+----+----+----+

  Khóa công khai :: 32 byte, theo thứ tự nhỏ, Elligator2, rõ ràng

  Dữ liệu được mã hóa phần cờ :: 32 byte

  Dữ liệu được mã hóa phần tải :: dữ liệu còn lại trừ 16 byte

  MAC :: mã xác thực tin nhắn Poly1305, 16 byte

```


### Khóa tạm thời một lần phiên mới

Khóa một lần là 32 byte, được mã hóa bằng Elligator2, theo thứ tự nhỏ.
Khóa này không bao giờ được sử dụng lại; một khóa mới được tạo với
mỗi tin nhắn, bao gồm cả việc truyền lại.


### Dữ liệu giải mã phần cờ

Phần cờ không chứa gì cả.
Nó luôn là 32 byte, vì nó phải có cùng độ dài
với khóa tĩnh cho các tin nhắn Phiên mới có liên kết.
Bob xác định liệu đó là khóa tĩnh hay phần cờ
bằng cách kiểm tra xem 32 byte có phải là toàn bộ số 0 hay không.

TODO có cần cờ nào ở đây không?

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                                       |
  +             Toàn bộ số 0              +
  |              32 byte                  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+

  zeros:: Toàn bộ số 0, 32 byte.

```


### Tải

Độ dài được mã hóa là phần còn lại của dữ liệu.
Độ dài được giải mã ít hơn 16 byte so với độ dài được mã hóa.
Tải phải chứa một khối DateTime và thường sẽ chứa một hoặc nhiều khối Garlic Clove.
Xem phần tải bên dưới để biết định dạng và các yêu cầu bổ sung.



### 1f) KDF cho tin nhắn Phiên mới

### KDF cho ChainKey ban đầu

Đây là [NOISE](https://noiseprotocol.org/noise.html) tiêu chuẩn cho IK với tên giao thức đã sửa đổi.
Lưu ý rằng chúng ta sử dụng cùng một bộ khởi tạo cho cả mẫu IK (phiên có liên kết)
và cho mẫu N (phiên không liên kết).

Tên giao thức được sửa đổi vì hai lý do.
Thứ nhất, để chỉ ra rằng các khóa tạm thời được mã hóa bằng Elligator2,
và thứ hai, để chỉ ra rằng MixHash() được gọi trước tin nhắn thứ hai
để trộn giá trị thẻ.

```

Đây là mẫu "e":

  // Định nghĩa protocol_name.
  Đặt protocol_name = "Noise_IKelg2+hs2_25519_ChaChaPoly_SHA256"
   (40 byte, mã hóa US-ASCII, không kết thúc NULL).

  // Định nghĩa Hash h = 32 byte
  h = SHA256(protocol_name);

  Định nghĩa ck = 32 byte chaining key. Sao chép dữ liệu h sang ck.
  Đặt chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // cho đến đây, tất cả đều có thể được tính trước bởi Alice cho tất cả các kết nối gửi đi

```


### KDF cho nội dung được mã hóa phần Cờ/Khóa tĩnh

```

Đây là mẫu "e":

  // Khóa tĩnh X25519 của Bob
  // bpk được công bố trong leaseset
  bsk = GENERATE_PRIVATE()
  bpk = DERIVE_PUBLIC(bsk)

  // Khóa công khai tĩnh của Bob
  // MixHash(bpk)
  // || bên dưới có nghĩa là nối
  h = SHA256(h || bpk);

  // cho đến đây, tất cả đều có thể được tính trước bởi Bob cho tất cả các kết nối nhận vào

  // Khóa tạm thời X25519 của Alice
  aesk = GENERATE_PRIVATE_ELG2()
  aepk = DERIVE_PUBLIC(aesk)

  // Khóa công khai tạm thời của Alice
  // MixHash(aepk)
  // || bên dưới có nghĩa là nối
  h = SHA256(h || aepk);

  // h được dùng làm dữ liệu liên kết cho AEAD trong tin nhắn Phiên mới
  // Giữ lại Hash h cho KDF Phản hồi Phiên mới
  // eapk được gửi rõ ràng ở đầu
  // của tin nhắn Phiên mới
  elg2_aepk = ENCODE_ELG2(aepk)
  // Như được giải mã bởi Bob
  aepk = DECODE_ELG2(elg2_aepk)

  Kết thúc mẫu "e".

  Đây là mẫu "es":

  // Noise es
  sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Tham số ChaChaPoly để mã hóa/giải mã
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Tham số AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, phần cờ/khóa tĩnh, ad)

  Kết thúc mẫu "es".

  Đây là mẫu "s":

  // MixHash(ciphertext)
  // Lưu cho KDF phần tải
  h = SHA256(h || ciphertext)

  // Khóa tĩnh X25519 của Alice
  ask = GENERATE_PRIVATE()
  apk = DERIVE_PUBLIC(ask)

  Kết thúc mẫu "s".


```



### KDF cho phần tải (với khóa tĩnh của Alice)

```

Đây là mẫu "ss":

  // Noise ss
  sharedSecret = DH(ask, bpk) = DH(bsk, apk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Tham số ChaChaPoly để mã hóa/giải mã
  // chainKey từ phần Khóa tĩnh
  Đặt sharedSecret = kết quả DH X25519
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Tham số AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, tải, ad)

  Kết thúc mẫu "ss".

  // MixHash(ciphertext)
  // Lưu cho KDF Phản hồi Phiên mới
  h = SHA256(h || ciphertext)

```


### KDF cho phần tải (không có khóa tĩnh của Alice)

Lưu ý rằng đây là mẫu Noise "N", nhưng chúng ta sử dụng cùng bộ khởi tạo "IK"
như cho các phiên có liên kết.

Các tin nhắn Phiên mới không thể được xác định là có chứa khóa tĩnh của Alice hay không
cho đến khi khóa tĩnh được giải mã và kiểm tra để xác định liệu nó có chứa toàn bộ số 0 hay không.
Do đó, người nhận phải sử dụng máy trạng thái "IK" cho tất cả
các tin nhắn Phiên mới.
Nếu khóa tĩnh là toàn bộ số 0, mẫu "ss" phải được bỏ qua.



```

chainKey = từ phần Cờ/Khóa tĩnh
  k = từ phần Cờ/Khóa tĩnh
  n = 1
  ad = h từ phần Cờ/Khóa tĩnh
  ciphertext = ENCRYPT(k, n, tải, ad)

```



### 1g) Định dạng Phản hồi Phiên mới

Một hoặc nhiều Phản hồi Phiên mới có thể được gửi để phản hồi một tin nhắn Phiên mới duy nhất.
Mỗi phản hồi được đặt tiền tố bằng một thẻ, được tạo từ một Bộ thẻ cho phiên.

Phản hồi Phiên mới gồm hai phần.
Phần đầu tiên là phần hoàn thành handshake Noise IK với thẻ tiền tố.
Độ dài phần đầu tiên là 56 byte.
Phần thứ hai là tải giai đoạn dữ liệu.
Độ dài phần thứ hai là 16 + độ dài tải.

Tổng độ dài là 72 + độ dài tải.
Định dạng được mã hóa:

```

+----+----+----+----+----+----+----+----+
  |       Thẻ phiên   8 byte              |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Khóa công khai tạm thời        +
  |                                       |
  +            32 byte                    +
  |     Được mã hóa bằng Elligator2       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Mã xác thực tin nhắn Poly1305        |
  +  (MAC) cho phần khóa (không có dữ liệu)      +
  |             16 byte                   |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Phần tải                 +
  |       Dữ liệu được mã hóa ChaCha20    |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Mã xác thực tin nhắn Poly1305        |
  +         (MAC) cho phần tải          +
  |             16 byte                   |
  +----+----+----+----+----+----+----+----+

  Thẻ :: 8 byte, rõ ràng

  Khóa công khai :: 32 byte, theo thứ tự nhỏ, Elligator2, rõ ràng

  MAC :: mã xác thực tin nhắn Poly1305, 16 byte
         Lưu ý: Dữ liệu rõ ChaCha20 là rỗng (ZEROLEN)

  Dữ liệu được mã hóa phần tải :: dữ liệu còn lại trừ 16 byte

  MAC :: mã xác thực tin nhắn Poly1305, 16 byte

```

### Thẻ phiên
Thẻ được tạo trong KDF Thẻ phiên, như được khởi tạo
trong KDF Khởi tạo DH bên dưới.
Điều này liên kết phản hồi với phiên.
Khóa Phiên từ Khởi tạo DH không được sử dụng.


### Khóa tạm thời Phản hồi Phiên mới

Khóa tạm thời của Bob.
Khóa tạm thời là 32 byte, được mã hóa bằng Elligator2, theo thứ tự nhỏ.
Khóa này không bao giờ được sử dụng lại; một khóa mới được tạo với
mỗi tin nhắn, bao gồm cả việc truyền lại.


### Tải
Độ dài được mã hóa là phần còn lại của dữ liệu.
Độ dài được giải mã ít hơn 16 byte so với độ dài được mã hóa.
Tải thường sẽ chứa một hoặc nhiều khối Garlic Clove.
Xem phần tải bên dưới để biết định dạng và các yêu cầu bổ sung.


### KDF cho Bộ thẻ Phản hồi

Một hoặc nhiều thẻ được tạo từ Bộ thẻ, được khởi tạo bằng cách sử dụng
KDF bên dưới, sử dụng chainKey từ tin nhắn Phiên mới.

```

// Tạo bộ thẻ
  tagsetKey = HKDF(chainKey, ZEROLEN, "SessionReplyTags", 32)
  tagset_nsr = DH_INITIALIZE(chainKey, tagsetKey)

```


### KDF cho nội dung được mã hóa phần khóa phản hồi

```

// Khóa từ tin nhắn Phiên mới
  // Khóa X25519 của Alice
  // apk và aepk được gửi trong tin nhắn Phiên mới gốc
  // ask = khóa tĩnh riêng của Alice
  // apk = khóa công khai tĩnh của Alice
  // aesk = khóa tạm thời riêng của Alice
  // aepk = khóa công khai tạm thời của Alice
  // Khóa tĩnh X25519 của Bob
  // bsk = khóa tĩnh riêng của Bob
  // bpk = khóa công khai tĩnh của Bob

  // Tạo thẻ
  tagsetEntry = tagset_nsr.GET_NEXT_ENTRY()
  tag = tagsetEntry.SESSION_TAG

  // MixHash(tag)
  h = SHA256(h || tag)

  Đây là mẫu "e":

  // Khóa tạm thời X25519 của Bob
  besk = GENERATE_PRIVATE_ELG2()
  bepk = DERIVE_PUBLIC(besk)

  // Khóa công khai tạm thời của Bob
  // MixHash(bepk)
  // || bên dưới có nghĩa là nối
  h = SHA256(h || bepk);

  // elg2_bepk được gửi rõ ràng ở đầu
  // của tin nhắn Phiên mới
  elg2_bepk = ENCODE_ELG2(bepk)
  // Như được giải mã bởi Bob
  bepk = DECODE_ELG2(elg2_bepk)

  Kết thúc mẫu "e".

  Đây là mẫu "ee":

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Tham số ChaChaPoly để mã hóa/giải mã
  // chainKey từ phần tải Phiên mới gốc
  sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
  keydata = HKDF(chainKey, sharedSecret, "", 32)
  chainKey = keydata[0:31]

  Kết thúc mẫu "ee".

  Đây là mẫu "se":

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  sharedSecret = DH(ask, bepk) = DH(besk, apk)
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Tham số AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, ZEROLEN, ad)

  Kết thúc mẫu "se".

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  chainKey được dùng trong ratchet bên dưới.

```


### KDF cho nội dung được mã hóa phần tải

Điều này giống như tin nhắn Phiên hiện tại đầu tiên,
sau khi chia, nhưng không có thẻ riêng biệt.
Ngoài ra, chúng ta sử dụng băm từ trên để liên kết
tải với tin nhắn NSR.


```

// split()
  keydata = HKDF(chainKey, ZEROLEN, "", 64)
  k_ab = keydata[0:31]
  k_ba = keydata[32:63]
  tagset_ab = DH_INITIALIZE(chainKey, k_ab)
  tagset_ba = DH_INITIALIZE(chainKey, k_ba)

  // Tham số AEAD cho tải Phản hồi Phiên mới
  k = HKDF(k_ba, ZEROLEN, "AttachPayloadKDF", 32)
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, tải, ad)
```


### Ghi chú

Nhiều tin nhắn NSR có thể được gửi để phản hồi, mỗi tin nhắn có khóa tạm thời riêng, tùy thuộc vào kích thước phản hồi.

Alice và Bob bắt buộc phải sử dụng khóa tạm thời mới cho mọi tin nhắn NS và NSR.

Alice phải nhận được một trong các tin nhắn NSR của Bob trước khi gửi tin nhắn Phiên hiện tại (ES),
và Bob phải nhận được tin nhắn ES từ Alice trước khi gửi tin nhắn ES.

``chainKey`` và ``k`` từ phần tải NSR của Bob được dùng
làm đầu vào cho các ratchet DH ES ban đầu (cả hai hướng, xem KDF Ratchet DH).

Bob chỉ được giữ các phiên hiện tại cho các tin nhắn ES nhận được từ Alice.
Bất kỳ phiên gửi và nhận nào khác được tạo (cho nhiều NSR) nên bị
hủy ngay lập tức sau khi nhận tin nhắn ES đầu tiên của Alice cho một phiên nhất định.



### 1h) Định dạng phiên hiện tại

Thẻ phiên (8 byte)
Dữ liệu được mã hóa và MAC (xem phần 3 bên dưới)


### Định dạng
Được mã hóa:

```

+----+----+----+----+----+----+----+----+
  |       Thẻ phiên                     |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Phần tải                 +
  |       Dữ liệu được mã hóa ChaCha20    |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Mã xác thực tin nhắn Poly1305        |
  +              (MAC)                    +
  |             16 byte                   |
  +----+----+----+----+----+----+----+----+

  Thẻ phiên :: 8 byte, rõ ràng

  Dữ liệu được mã hóa phần tải :: dữ liệu còn lại trừ 16 byte

  MAC :: mã xác thực tin nhắn Poly1305, 16 byte

```


### Tải
Độ dài được mã hóa là phần còn lại của dữ liệu.
Độ dài được giải mã ít hơn 16 byte so với độ dài được mã hóa.
Xem phần tải bên dưới để biết định dạng và yêu cầu.


KDF

```
Xem phần AEAD bên dưới.

  // Tham số AEAD cho tải Phiên hiện tại
  k = Khóa phiên 32 byte liên kết với thẻ phiên này
  n = Số tin nhắn N trong chuỗi hiện tại, như được truy xuất từ thẻ phiên liên kết.
  ad = Thẻ phiên, 8 byte
  ciphertext = ENCRYPT(k, n, tải, ad)
```



### 2) ECIES-X25519


Định dạng: khóa công khai và riêng 32 byte, theo thứ tự nhỏ.

Lý do: Được sử dụng trong [NTCP2](/docs/specs/ntcp2/).



### 2a) Elligator2

Trong các handshake Noise tiêu chuẩn, các tin nhắn handshake ban đầu theo mỗi hướng bắt đầu bằng
các khóa tạm thời được truyền rõ ràng.
Vì các khóa X25519 hợp lệ có thể phân biệt được với dữ liệu ngẫu nhiên, một kẻ trung gian có thể phân biệt
các tin nhắn này với các tin nhắn Phiên hiện tại bắt đầu bằng các thẻ phiên ngẫu nhiên.
Trong [NTCP2](/docs/specs/ntcp2/) ([Đề xuất 111](/proposals/111-ntcp-2/)), chúng tôi đã sử dụng một hàm XOR hiệu quả thấp sử dụng khóa tĩnh ngoài băng để che giấu
khóa. Tuy nhiên, mô hình mối đe dọa ở đây khác; chúng tôi không muốn cho phép bất kỳ MitM nào
sử dụng bất kỳ phương tiện nào để xác nhận đích của lưu lượng, hoặc để phân biệt
các tin nhắn handshake ban đầu với các tin nhắn Phiên hiện tại.

Do đó, [Elligator2](https://elligator.cr.yp.to/) được sử dụng để biến đổi các khóa tạm thời trong các tin nhắn Phiên mới và Phản hồi Phiên mới
sao cho chúng không thể phân biệt với các chuỗi ngẫu nhiên đều.



### Định dạng

32 byte khóa công khai và riêng.
Các khóa được mã hóa theo thứ tự nhỏ.

Như được định nghĩa trong [Elligator2](https://elligator.cr.yp.to/), các khóa được mã hóa không thể phân biệt với 254 bit ngẫu nhiên.
Chúng tôi yêu cầu 256 bit ngẫu nhiên (32 byte). Do đó, việc mã hóa và giải mã được
định nghĩa như sau:

Mã hóa:

```

Định nghĩa ENCODE_ELG2()

  // Mã hóa như được định nghĩa trong thông số kỹ thuật Elligator2
  encodedKey = encode(pubkey)
  // OR với 2 bit ngẫu nhiên vào MSB
  randomByte = CSRNG(1)
  encodedKey[31] |= (randomByte & 0xc0)
```


Giải mã:

```

Định nghĩa DECODE_ELG2()

  // Che 2 bit ngẫu nhiên từ MSB
  encodedKey[31] &= 0x3f
  // Giải mã như được định nghĩa trong thông số kỹ thuật Elligator2
  pubkey = decode(encodedKey)
```




### Lý do

Cần thiết để ngăn chặn OBEP và IBGW phân loại lưu lượng.


### Ghi chú

Elligator2 làm tăng gấp đôi thời gian trung bình để tạo khóa, vì một nửa các khóa riêng
dẫn đến các khóa công khai không phù hợp để mã hóa với Elligator2.
Ngoài ra, thời gian tạo khóa là không giới hạn với phân phối mũ,
vì bộ tạo phải tiếp tục thử cho đến khi tìm thấy một cặp khóa phù hợp.

Chi phí này có thể được quản lý bằng cách tạo khóa trước,
trong một luồng riêng biệt, để giữ một nhóm các khóa phù hợp.

Bộ tạo thực hiện hàm ENCODE_ELG2() để xác định tính phù hợp.
Do đó, bộ tạo nên lưu trữ kết quả của ENCODE_ELG2()
để không phải tính toán lại.

Ngoài ra, các khóa không phù hợp có thể được thêm vào nhóm các khóa
được sử dụng cho [NTCP2](/docs/specs/ntcp2/), nơi không sử dụng Elligator2.
Vấn đề bảo mật khi làm như vậy vẫn chưa được xác định.




### 3) AEAD (ChaChaPoly)

AEAD sử dụng ChaCha20 và Poly1305, giống như trong [NTCP2](/docs/specs/ntcp2/).
Điều này tương ứng với [RFC-7539](https://tools.ietf.org/html/rfc7539), cũng được
sử dụng tương tự trong TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).



### Đầu vào Phiên mới và Phản hồi Phiên mới

Đầu vào cho các hàm mã hóa/giải mã
cho một khối AEAD trong tin nhắn Phiên mới:

```

k :: khóa mã hóa 32 byte
       Xem KDF Phiên mới và Phản hồi Phiên mới ở trên.

  n :: nonce dựa trên bộ đếm, 12 byte.
       n = 0

  ad :: Dữ liệu liên kết, 32 byte.
        Băm SHA256 của dữ liệu trước đó, như đầu ra từ mixHash()

  data :: Dữ liệu rõ, 0 hoặc nhiều byte

```


### Đầu vào Phiên hiện tại

Đầu vào cho các hàm mã hóa/giải mã
cho một khối AEAD trong tin nhắn Phiên hiện tại:

```

k :: khóa phiên 32 byte
       Như tra cứu từ thẻ phiên đi kèm.

  n :: nonce dựa trên bộ đếm, 12 byte.
       Bắt đầu từ 0 và tăng lên cho mỗi tin nhắn khi truyền.
       Đối với người nhận, giá trị
       như tra cứu từ thẻ phiên đi kèm.
       Bốn byte đầu tiên luôn bằng 0.
       Tám byte cuối là số tin nhắn (n), được mã hóa theo thứ tự nhỏ.
       Giá trị tối đa là 65535.
       Phiên phải được ratchet khi N đạt đến giá trị đó.
       Không bao giờ được sử dụng các giá trị cao hơn.

  ad :: Dữ liệu liên kết
        Thẻ phiên

  data :: Dữ liệu rõ, 0 hoặc nhiều byte

```


### Định dạng được mã hóa

Đầu ra của hàm mã hóa, đầu vào của hàm giải mã:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |       Dữ liệu được mã hóa ChaCha20    |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Mã xác thực tin nhắn Poly1305        |
  +              (MAC)                    +
  |             16 byte                   |
  +----+----+----+----+----+----+----+----+

  dữ liệu được mã hóa :: Cùng kích thước với dữ liệu rõ, 0 - 65519 byte

  MAC :: mã xác thực tin nhắn Poly1305, 16 byte

```

### Ghi chú
- Vì ChaCha20 là một bộ mã hóa dòng, dữ liệu rõ không cần được đệm.
  Các byte dòng khóa bổ sung bị loại bỏ.

- Khóa cho bộ mã hóa (256 bit) được thỏa thuận bằng cách sử dụng KDF SHA256.
  Chi tiết về KDF cho mỗi tin nhắn nằm trong các phần riêng biệt bên dưới.

- Các khung ChaChaPoly có kích thước đã biết vì chúng được đóng gói trong tin nhắn dữ liệu I2NP.

- Đối với tất cả các tin nhắn,
  việc đệm nằm bên trong khung dữ liệu được xác thực.


### Xử lý lỗi AEAD

Tất cả dữ liệu nhận được mà thất bại trong xác minh AEAD phải bị loại bỏ.
Không trả lại phản hồi nào.


### Lý do

Được sử dụng trong [NTCP2](/docs/specs/ntcp2/).



### 4) Ratchets

Chúng tôi vẫn sử dụng session tags, như trước đây, nhưng chúng tôi sử dụng ratchets để tạo chúng.
Session tags cũng có một tùy chọn thay khóa mà chúng tôi chưa bao giờ triển khai.
Vì vậy, nó giống như một ratchet kép nhưng chúng tôi chưa bao giờ làm cái thứ hai.

Ở đây chúng tôi định nghĩa một cái gì đó tương tự như Ratchet Kép của Signal.
Các session tags được tạo một cách xác định và giống hệt nhau ở
cả hai phía người gửi và người nhận.

Bằng cách sử dụng một ratchet khóa/tag đối xứng, chúng tôi loại bỏ việc sử dụng bộ nhớ để lưu trữ session tags ở phía người gửi.
Chúng tôi cũng loại bỏ việc tiêu thụ băng thông khi gửi các bộ tag.
Việc sử dụng ở phía người nhận vẫn đáng kể, nhưng chúng tôi có thể giảm nó hơn nữa
vì chúng tôi sẽ thu nhỏ session tag từ 32 byte xuống 8 byte.

Chúng tôi không sử dụng mã hóa tiêu đề như được chỉ định (và tùy chọn) trong Signal,
chúng tôi sử dụng session tags thay thế.

Bằng cách sử dụng một ratchet DH, chúng tôi đạt được tính bí mật về phía trước, điều này chưa bao giờ được triển khai
trong ElGamal/AES+SessionTags.

Lưu ý: Khóa công khai tạm thời một lần cho Phiên mới không phải là một phần của ratchet, chức năng duy nhất của nó
là mã hóa khóa ratchet DH ban đầu của Alice.


### Số tin nhắn

Ratchet kép xử lý các tin nhắn bị mất hoặc không theo thứ tự bằng cách bao gồm trong mỗi tiêu đề tin nhắn
một thẻ. Người nhận tra cứu chỉ số của thẻ, đây là số tin nhắn N.
Nếu tin nhắn chứa một khối Số tin nhắn với giá trị PN,
người nhận có thể xóa bất kỳ thẻ nào cao hơn giá trị đó trong bộ thẻ trước đó,
trong khi vẫn giữ các thẻ bị bỏ qua
từ bộ thẻ trước đó phòng trường hợp các tin nhắn bị bỏ qua đến sau.


### Mẫu triển khai

Chúng tôi định nghĩa các cấu trúc dữ liệu và hàm sau để triển khai các ratchet này.

TAGSET_ENTRY
    Một mục duy nhất trong một TAGSET.

    INDEX
        Một chỉ số nguyên, bắt đầu từ 0

    SESSION_TAG
        Một định danh để gửi đi trên mạng, 8 byte

    SESSION_KEY
        Một khóa đối xứng, không bao giờ gửi đi trên mạng, 32 byte

TAGSET
    Một tập hợp các TAGSET_ENTRIES.

    CREATE(key, n)
        Tạo một TAGSET mới sử dụng liệu khóa mật mã ban đầu 32 byte.
        Định danh phiên liên kết được cung cấp.
        Số lượng thẻ ban đầu để tạo được chỉ định; điều này thường là 0 hoặc 1
        cho một phiên gửi đi.
        LAST_INDEX = -1
        Gọi EXTEND
