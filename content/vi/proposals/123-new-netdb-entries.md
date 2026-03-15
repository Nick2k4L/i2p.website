---
title: "Mục netDB Mới"
number: "123"
author: "zzz, str4d, orignal"
created: "2016-01-16"
lastupdated: "2020-07-18"
status: "Mở"
thread: "http://zzz.i2p/topics/2051"
supercedes: "110, 120, 121, 122"
toc: true
---
## Trạng thái

Một phần của đề xuất này đã hoàn thành và được triển khai trong 0.9.38 và 0.9.39.  
Các cấu trúc chung, I2CP, I2NP và các đặc tả khác  
hiện đã được cập nhật để phản ánh các thay đổi được hỗ trợ hiện nay.

Các phần đã hoàn thành vẫn có thể được sửa đổi nhỏ.  
Các phần khác của đề xuất này vẫn đang trong quá trình phát triển  
và có thể được sửa đổi đáng kể.

Tìm kiếm dịch vụ (loại 9 và 11) là ưu tiên thấp  
và chưa được lên lịch, có thể được tách thành một đề xuất riêng.

## Tổng quan

Đây là bản cập nhật và tổng hợp của 4 đề xuất sau:

- 110 LS2
- 120 Meta LS2 cho đa kết nối quy mô lớn
- 121 LS2 được mã hóa
- 122 Tìm kiếm dịch vụ không xác thực (anycasting)

Các đề xuất này phần lớn độc lập, nhưng vì lý do hợp lý, chúng tôi định nghĩa và sử dụng  
một định dạng chung cho một số trong số chúng.

Các đề xuất sau có liên quan một phần:

- 140 Đa kết nối vô hình (không tương thích với đề xuất này)
- 142 Mẫu mã hóa mới (cho mã hóa đối xứng mới)
- 144 ECIES-X25519-AEAD-Ratchet
- 145 ECIES-P256
- 146 Red25519
- 148 EdDSA-BLAKE2b-Ed25519
- 149 B32 cho LS2 được mã hóa
- 150 Giao thức Garlic Farm
- 151 ECDSA Blinding

## Đề xuất

Đề xuất này định nghĩa 5 loại DatabaseEntry mới và quy trình  
lưu trữ và truy xuất chúng từ cơ sở dữ liệu mạng,  
cũng như phương pháp ký và xác minh chữ ký.

### Mục tiêu

- Tương thích ngược
- LS2 có thể sử dụng với đa kết nối kiểu cũ
- Không yêu cầu mã hóa hoặc nguyên thủy mới để hỗ trợ
- Duy trì sự tách biệt giữa mã hóa và chữ ký; hỗ trợ tất cả các phiên bản hiện tại và tương lai
- Cho phép khóa ký ngoại tuyến tùy chọn
- Giảm độ chính xác của dấu thời gian để giảm khả năng định danh
- Cho phép mã hóa mới cho các điểm đến
- Cho phép đa kết nối quy mô lớn
- Sửa nhiều vấn đề với LS được mã hóa hiện tại
- Tùy chọn ẩn danh để giảm khả năng nhìn thấy bởi các floodfill
- Hỗ trợ cả khóa đơn và nhiều khóa có thể thu hồi
- Tìm kiếm dịch vụ để dễ dàng tìm kiếm outproxy, khởi động DHT ứng dụng,  
  và các mục đích sử dụng khác
- Không làm hỏng bất cứ thứ gì phụ thuộc vào băm điểm đến nhị phân 32 byte, ví dụ như bittorrent
- Thêm tính linh hoạt cho leaseset thông qua các thuộc tính, giống như chúng ta có trong routerinfos.
- Đặt dấu thời gian công bố và thời gian hết hạn thay đổi vào tiêu đề, để nó hoạt động ngay cả  
  khi nội dung được mã hóa (không suy ra dấu thời gian từ lease sớm nhất)
- Tất cả các loại mới nằm trong cùng không gian DHT và cùng vị trí như leaseset hiện tại,  
  để người dùng có thể di chuyển từ LS cũ sang LS2,  
  hoặc chuyển đổi giữa LS2, Meta và Encrypted,  
  mà không cần thay đổi Destination hoặc băm.
- Một Destination hiện tại có thể được chuyển sang sử dụng khóa ngoại tuyến,  
  hoặc trở lại khóa trực tuyến, mà không cần thay đổi Destination hoặc băm.

### Mục tiêu không đạt được / Ngoài phạm vi

- Thuật toán quay DHT mới hoặc tạo số ngẫu nhiên chung
- Loại mã hóa mới cụ thể và lược đồ mã hóa end-to-end  
  để sử dụng loại mới sẽ nằm trong một đề xuất riêng.  
  Không có mã hóa mới nào được chỉ định hoặc thảo luận ở đây.
- Mã hóa mới cho RIs hoặc xây dựng tunnel.  
  Sẽ nằm trong một đề xuất riêng.
- Phương pháp mã hóa, truyền và nhận tin nhắn I2NP DLM / DSM / DSRM.  
  Không thay đổi.
- Cách tạo và hỗ trợ Meta, bao gồm giao tiếp nội bộ giữa các router, quản lý, chuyển đổi và phối hợp.  
  Hỗ trợ có thể được thêm vào I2CP, hoặc i2pcontrol, hoặc một giao thức mới.  
  Điều này có thể hoặc không được chuẩn hóa.
- Cách thực hiện và quản lý các tunnel có thời gian hết hạn dài hơn, hoặc hủy các tunnel hiện tại.  
  Điều đó cực kỳ khó khăn, và nếu không có nó, bạn không thể có một quá trình tắt máy hợp lý.
- Thay đổi mô hình mối đe dọa
- Định dạng lưu trữ ngoại tuyến, hoặc phương pháp lưu trữ/truy xuất/chia sẻ dữ liệu.
- Chi tiết triển khai không được thảo luận ở đây và được để cho từng dự án.

### Cơ sở

LS2 thêm các trường để thay đổi loại mã hóa và cho các thay đổi giao thức trong tương lai.

LS2 được mã hóa sửa một số vấn đề bảo mật với LS được mã hóa hiện tại bằng cách  
sử dụng mã hóa bất đối xứng cho toàn bộ tập hợp các lease.

Meta LS2 cung cấp đa kết nối linh hoạt, hiệu quả, hiệu quả và quy mô lớn.

Bản ghi dịch vụ và Danh sách dịch vụ cung cấp các dịch vụ anycast như tra cứu tên  
và khởi động DHT.

### Các loại dữ liệu NetDB

Các số loại được sử dụng trong Tin nhắn Tìm kiếm/Lưu trữ Cơ sở dữ liệu I2NP.

Cột end-to-end đề cập đến việc truy vấn/phản hồi có được gửi đến một Destination trong một Tin nhắn Tỏi hay không.

Các loại hiện tại:

| NetDB Data | Loại Tìm kiếm | Loại Lưu trữ |
|------------|-------------|------------|
| bất kỳ        | 0           | bất kỳ        |
| LS         | 1           | 1          |
| RI         | 2           | 0          |
| khám phá| 3           | DSRM       |

Các loại mới:

| NetDB Data     | Loại Tìm kiếm | Loại Lưu trữ | Tiêu đề LS2 chuẩn? | Gửi end-to-end? |
|----------------|-------------|------------|------------------|------------------|
| LS2            | 1           | 3          | có              | có              |
| LS2 được mã hóa  | 1           | 5          | không               | không               |
| Meta LS2       | 1           | 7          | có              | không               |
| Bản ghi Dịch vụ | n/a         | 9          | có              | không               |
| Danh sách Dịch vụ   | 4           | 11         | không               | không               |

### Ghi chú

- Các loại tìm kiếm hiện đang là bit 3-2 trong Tin nhắn Tìm kiếm Cơ sở dữ liệu.  
  Bất kỳ loại bổ sung nào sẽ yêu cầu sử dụng bit 4.

- Tất cả các loại lưu trữ đều là số lẻ vì các bit trên trong trường loại của Tin nhắn Lưu trữ Cơ sở dữ liệu  
  bị các router cũ bỏ qua.  
  Chúng tôi thà để việc phân tích cú pháp thất bại như một LS hơn là như một RI được nén.

- Loại nên được chỉ định rõ ràng, ngầm định hay không rõ ràng trong dữ liệu được bao phủ bởi chữ ký?

### Quy trình Tìm kiếm/Lưu trữ

Các loại 3, 5 và 7 có thể được trả về như phản hồi cho một tìm kiếm leaseset tiêu chuẩn (loại 1).  
Loại 9 không bao giờ được trả về như phản hồi cho một tìm kiếm.  
Loại 11 được trả về như phản hồi cho một loại tìm kiếm dịch vụ mới (loại 11).

Chỉ loại 3 có thể được gửi trong một tin nhắn Tỏi từ client đến client.

### Định dạng

Các loại 3, 7 và 9 đều có định dạng chung::

  Tiêu đề LS2 chuẩn
  - như được định nghĩa bên dưới

  Phần riêng cho loại
  - như được định nghĩa bên dưới cho từng phần

  Chữ ký LS2 chuẩn:
  - Độ dài như được ngụ ý bởi loại chữ ký của khóa ký

Loại 5 (Được mã hóa) không bắt đầu bằng Destination và có định dạng khác. Xem bên dưới.

Loại 11 (Danh sách Dịch vụ) là tập hợp của nhiều Bản ghi Dịch vụ và có định dạng khác. Xem bên dưới.

### Xem xét về Quyền riêng tư/Bảo mật

TBD

## Tiêu đề LS2 chuẩn

Các loại 3, 7 và 9 sử dụng tiêu đề LS2 chuẩn, được chỉ định bên dưới:

### Định dạng

```
Tiêu đề LS2 chuẩn:
  - Loại (1 byte)
    Không thực sự nằm trong tiêu đề, nhưng là một phần của dữ liệu được bao phủ bởi chữ ký.
    Lấy từ trường trong Tin nhắn Lưu trữ Cơ sở dữ liệu.
  - Destination (387+ byte)
  - Dấu thời gian công bố (4 byte, big endian, giây kể từ epoch, quay vòng vào năm 2106)
  - Hết hạn (2 byte, big endian) (chênh lệch từ dấu thời gian công bố tính bằng giây, tối đa 18,2 giờ)
  - Cờ (2 byte)
    Thứ tự bit: 15 14 ... 3 2 1 0
    Bit 0: Nếu 0, không có khóa ngoại tuyến; nếu 1, có khóa ngoại tuyến
    Bit 1: Nếu 0, một leaseset được công bố chuẩn.
           Nếu 1, một leaseset chưa được công bố. Không nên được lan truyền, công bố hoặc
           gửi như phản hồi cho một truy vấn. Nếu leaseset này hết hạn, không truy vấn
           netdb để tìm cái mới, trừ khi bit 2 được đặt.
    Bit 2: Nếu 0, một leaseset được công bố chuẩn.
           Nếu 1, leaseset chưa được mã hóa này sẽ được ẩn danh và mã hóa khi công bố.
           Nếu leaseset này hết hạn, truy vấn vị trí ẩn danh trong netdb để tìm cái mới.
           Nếu bit này được đặt thành 1, đặt bit 1 thành 1 cũng vậy.
           Kể từ phiên bản 0.9.42.
    Bit 3-15: đặt thành 0 để tương thích với các mục đích sử dụng trong tương lai
  - Nếu cờ cho biết có khóa ngoại tuyến, phần chữ ký ngoại tuyến:
    Dấu thời gian hết hạn (4 byte, big endian, giây kể từ epoch, quay vòng vào năm 2106)
    Loại chữ ký tạm thời (2 byte, big endian)
    Khóa công khai ký tạm thời (độ dài như được ngụ ý bởi loại chữ ký)
    Chữ ký của dấu thời gian hết hạn, loại chữ ký tạm thời và khóa công khai,
    bởi khóa công khai destination,
    độ dài như được ngụ ý bởi loại chữ ký khóa công khai destination.
    Phần này có thể, và nên, được tạo ngoại tuyến.
```

### Cơ sở

- Chưa công bố/đã công bố: Để sử dụng khi gửi một lưu trữ cơ sở dữ liệu end-to-end,
  router gửi có thể muốn chỉ ra rằng leaseset này không nên được
  gửi cho người khác. Hiện tại chúng tôi sử dụng các phương pháp heuristic để duy trì trạng thái này.

- Đã công bố: Thay thế logic phức tạp cần thiết để xác định 'phiên bản' của
  leaseset. Hiện tại, phiên bản là thời gian hết hạn của lease có thời gian hết hạn lâu nhất,
  và một router công bố phải tăng thời gian hết hạn đó lên ít nhất 1ms khi
  công bố một leaseset chỉ loại bỏ một lease cũ hơn.

- Hết hạn: Cho phép thời gian hết hạn của một mục netdb sớm hơn thời gian hết hạn của
  lease có thời gian hết hạn lâu nhất. Có thể không hữu ích cho LS2, nơi mà các leaseset
  dự kiến sẽ duy trì với thời gian hết hạn tối đa 11 phút, nhưng
  cho các loại mới khác, điều này là cần thiết (xem Meta LS và Bản ghi Dịch vụ bên dưới).

- Khóa ngoại tuyến là tùy chọn, để giảm độ phức tạp triển khai ban đầu/yêu cầu.

### Vấn đề

- Có thể giảm độ chính xác của dấu thời gian nhiều hơn nữa (10 phút?) nhưng sẽ phải thêm
  số phiên bản. Điều này có thể làm hỏng đa kết nối, trừ khi chúng ta có mã hóa bảo toàn thứ tự?
  Có lẽ không thể làm mà không có dấu thời gian.

- Thay thế: 3 byte dấu thời gian (epoch / 10 phút), 1-byte phiên bản, 2-byte hết hạn

- Loại được chỉ định rõ ràng hay ngầm định trong dữ liệu / chữ ký? Hằng số "Domain" cho chữ ký?

### Ghi chú

- Các router không nên công bố một LS nhiều hơn một lần mỗi giây.
  Nếu họ làm vậy, họ phải tăng nhân tạo dấu thời gian công bố lên 1
  so với LS công bố trước đó.

- Các triển khai router có thể lưu trữ bộ nhớ đệm các khóa tạm thời và chữ ký để
  tránh xác minh mỗi lần. Đặc biệt, các floodfill, và các router ở
  cả hai đầu của các kết nối lâu dài, có thể hưởng lợi từ điều này.

- Khóa và chữ ký ngoại tuyến chỉ phù hợp với các điểm đến lâu dài,
  tức là máy chủ, không phải máy khách.

## Các loại DatabaseEntry mới

### LeaseSet 2

Thay đổi từ LeaseSet hiện tại:

- Thêm dấu thời gian công bố, dấu thời gian hết hạn, cờ và thuộc tính
- Thêm loại mã hóa
- Loại bỏ khóa thu hồi

Tìm kiếm với
    Cờ LS chuẩn (1)
Lưu trữ với
    Loại LS2 chuẩn (3)
Lưu trữ tại
    Băm của destination
    Băm này sau đó được sử dụng để tạo "khóa định tuyến" hàng ngày, như trong LS1
Thời gian hết hạn điển hình
    10 phút, như trong một LS thông thường.
Được công bố bởi
    Destination

### Định dạng

```
Tiêu đề LS2 chuẩn như được chỉ định ở trên

  Phần riêng cho loại LS2 chuẩn
  - Thuộc tính (Ánh xạ như được chỉ định trong đặc tả cấu trúc chung, 2 byte 0 nếu không có)
  - Số lượng phần khóa theo sau (1 byte, tối đa TBD)
  - Các phần khóa:
    - Loại mã hóa (2 byte, big endian)
    - Độ dài khóa mã hóa (2 byte, big endian)
      Đây là rõ ràng, để các floodfill có thể phân tích cú pháp LS2 với các loại mã hóa chưa biết.
    - Khóa mã hóa (số byte được chỉ định)
  - Số lượng lease2 (1 byte)
  - Lease2 (40 byte mỗi cái)
    Đây là các lease, nhưng với 4 byte thay vì 8 byte hết hạn,
    giây kể từ epoch (quay vòng vào năm 2106)

  Chữ ký LS2 chuẩn:
  - Chữ ký
    Nếu cờ cho biết có khóa ngoại tuyến, đây được ký bởi khóa công khai tạm thời,
    nếu không, bởi khóa công khai destination
    Độ dài như được ngụ ý bởi loại chữ ký của khóa ký
    Chữ ký của tất cả các nội dung ở trên.
```

### Cơ sở

- Thuộc tính: Mở rộng và linh hoạt trong tương lai.
  Được đặt đầu tiên trong trường hợp cần thiết để phân tích cú pháp dữ liệu còn lại.

- Nhiều cặp loại mã hóa/khóa công khai nhằm
  giúp chuyển đổi sang các loại mã hóa mới dễ dàng hơn. Cách khác để làm điều này
  là công bố nhiều leaseset, có thể sử dụng cùng các tunnel,
  như chúng ta đang làm hiện tại cho các destination DSA và EdDSA.
  Việc xác định loại mã hóa đầu vào trên một tunnel
  có thể được thực hiện bằng cơ chế thẻ phiên hiện tại,
  và/hoặc giải mã thử bằng từng khóa. Độ dài của các tin nhắn đầu vào
  cũng có thể cung cấp manh mối.

### Thảo luận

Đề xuất này tiếp tục sử dụng khóa công khai trong leaseset cho khóa mã hóa end-to-end, và để khóa công khai trong trường Destination không được sử dụng, như hiện nay. Loại mã hóa không được chỉ định trong chứng chỉ khóa Destination, nó sẽ vẫn là 0.

Một phương án thay thế bị từ chối là chỉ định loại mã hóa trong chứng chỉ khóa Destination, sử dụng khóa công khai trong Destination, và không sử dụng khóa công khai trong leaseset. Chúng tôi không có kế hoạch làm điều này.

Lợi ích của LS2:

- Vị trí của khóa công khai thực tế không thay đổi.
- Loại mã hóa hoặc khóa công khai có thể thay đổi mà không thay đổi Destination.
- Loại bỏ trường thu hồi không sử dụng
- Tương thích cơ bản với các loại DatabaseEntry khác trong đề xuất này
- Cho phép nhiều loại mã hóa

Nhược điểm của LS2:

- Vị trí của khóa công khai và loại mã hóa khác với RouterInfo
- Duy trì khóa công khai không sử dụng trong leaseset
- Yêu cầu triển khai trên toàn mạng; trong phương án thay thế, các loại mã hóa thử nghiệm có thể được sử dụng, nếu được các floodfill cho phép (nhưng xem các đề xuất liên quan 136 và 137 về hỗ trợ các loại chữ ký thử nghiệm). Đề xuất thay thế có thể dễ triển khai và thử nghiệm hơn cho các loại mã hóa thử nghiệm.

### Các vấn đề mã hóa mới

Một phần điều này nằm ngoài phạm vi của đề xuất này,  
nhưng ghi chú ở đây tạm thời vì chúng tôi chưa có  
một đề xuất mã hóa riêng biệt nào.  
Xem thêm các đề xuất ECIES 144 và 145.

- Loại mã hóa đại diện cho sự kết hợp  
  của đường cong, độ dài khóa và lược đồ end-to-end,  
  bao gồm KDF và MAC, nếu có.

- Chúng tôi đã bao gồm một trường độ dài khóa, để LS2 có thể  
  được phân tích cú pháp và xác minh bởi floodfill ngay cả với các loại mã hóa chưa biết.

- Loại mã hóa mới đầu tiên được đề xuất sẽ  
  có thể là ECIES/X25519. Cách nó được sử dụng end-to-end  
  (một phiên bản sửa đổi nhẹ của ElGamal/AES+SessionTag  
  hoặc một cái gì đó hoàn toàn mới, ví dụ ChaCha/Poly) sẽ được chỉ định  
  trong một hoặc nhiều đề xuất riêng biệt.  
  Xem thêm các đề xuất ECIES 144 và 145.

### Ghi chú

- 8-byte expiration trong leases thay đổi thành 4 byte.

- Nếu chúng ta từng triển khai thu hồi, chúng ta có thể làm điều đó với một trường hết hạn bằng không,  
  hoặc zero leases, hoặc cả hai. Không cần khóa thu hồi riêng biệt.

- Các khóa mã hóa được sắp xếp theo thứ tự ưu tiên của máy chủ, ưu tiên cao nhất đầu tiên.  
  Hành vi mặc định của client là chọn khóa đầu tiên có  
  loại mã hóa được hỗ trợ. Client có thể sử dụng các thuật toán chọn khác  
  dựa trên hỗ trợ mã hóa, hiệu suất tương đối và các yếu tố khác.

### LS2 được mã hóa

Mục tiêu:

- Thêm ẩn danh
- Cho phép nhiều loại chữ ký
- Không yêu cầu các nguyên thủy mã hóa mới
- Tùy chọn mã hóa cho từng người nhận, có thể thu hồi
- Hỗ trợ mã hóa LS2 chuẩn và Meta LS2 chỉ

LS2 được mã hóa không bao giờ được gửi trong một tin nhắn tỏi end-to-end.  
Sử dụng LS2 chuẩn như trên.

Thay đổi từ LeaseSet được mã hóa hiện tại:

- Mã hóa toàn bộ để đảm bảo an toàn
- Mã hóa an toàn, không chỉ bằng AES.
- Mã hóa cho từng người nhận

Tìm kiếm với
    Cờ LS chuẩn (1)
Lưu trữ với
    Loại LS2 được mã hóa (5)
Lưu trữ tại
    Băm của loại chữ ký ẩn danh và khóa công khai ẩn danh
    Hai byte loại chữ ký (big endian, ví dụ 0x000b) || khóa công khai ẩn danh
    Băm này sau đó được sử dụng để tạo "khóa định tuyến" hàng ngày, như trong LS1
Thời gian hết hạn điển hình
    10 phút, như trong một LS thông thường, hoặc hàng giờ, như trong một meta LS.
Được công bố bởi
    Destination

### Định nghĩa

Chúng tôi định nghĩa các hàm sau tương ứng với các khối xây dựng mật mã được sử dụng  
cho LS2 được mã hóa:

CSRNG(n)  
    đầu ra n-byte từ một bộ tạo số ngẫu nhiên an toàn về mặt mật mã.

    Ngoài yêu cầu CSRNG phải an toàn về mặt mật mã (và do đó  
    phù hợp để tạo vật liệu khóa), nó PHẢI an toàn  
    để một đầu ra n-byte được sử dụng cho vật liệu khóa khi các chuỗi byte ngay trước và sau nó  
    được phơi bày trên mạng (như trong một muối, hoặc đệm được mã hóa). Các triển khai dựa vào một nguồn đáng ngờ nên băm  
    bất kỳ đầu ra nào sẽ được phơi bày trên mạng. Xem [PRNG references](http://projectbullrun.org/dual-ec/ext-rand.html) và [Tor dev discussion](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html).

H(p, d)  
    hàm băm SHA-256 nhận một chuỗi cá nhân hóa p và dữ liệu d, và  
    tạo ra đầu ra có độ dài 32 byte.

    Sử dụng SHA-256 như sau::

        H(p, d) := SHA-256(p || d)

STREAM  
    mật mã dòng ChaCha20 như được chỉ định trong [RFC 7539 Section 2.4](https://tools.ietf.org/html/rfc7539#section-2.4), với bộ đếm ban đầu  
    được đặt thành 1. S_KEY_LEN = 32 và S_IV_LEN = 12.

    ENCRYPT(k, iv, plaintext)  
        Mã hóa plaintext bằng khóa mật mã k, và nonce iv mà PHẢI là duy nhất cho  
        khóa k. Trả về một bản mã có cùng kích thước với plaintext.

        Bản mã toàn bộ phải không thể phân biệt với dữ liệu ngẫu nhiên nếu khóa là bí mật.

    DECRYPT(k, iv, ciphertext)  
        Giải mã ciphertext bằng khóa mật mã k, và nonce iv. Trả về plaintext.

SIG  
    lược đồ chữ ký RedDSA (tương ứng với SigType 11) với ẩn danh khóa.  
    Nó có các hàm sau:

    DERIVE_PUBLIC(privkey)  
        Trả về khóa công khai tương ứng với khóa riêng tư đã cho.

    SIGN(privkey, m)  
        Trả về chữ ký bởi khóa riêng tư privkey trên thông điệp m đã cho.

    VERIFY(pubkey, m, sig)  
        Xác minh chữ ký sig đối với khóa công khai pubkey và thông điệp m. Trả về  
        true nếu chữ ký hợp lệ, false nếu không.

    Nó cũng phải hỗ trợ các thao tác ẩn danh khóa sau:

    GENERATE_ALPHA(data, secret)  
        Tạo alpha cho những người biết dữ liệu và một bí mật tùy chọn.  
        Kết quả phải được phân bố giống hệt như các khóa riêng tư.

    BLIND_PRIVKEY(privkey, alpha)  
        Ẩn danh một khóa riêng tư, sử dụng một bí mật alpha.

    BLIND_PUBKEY(pubkey, alpha)  
        Ẩn danh một khóa công khai, sử dụng một bí mật alpha.  
        Đối với một cặp khóa (privkey, pubkey) đã cho, mối quan hệ sau giữ::

            BLIND_PUBKEY(pubkey, alpha) ==
            DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))

DH  
    hệ thống thỏa thuận khóa công khai X25519. Khóa riêng 32 byte, khóa công khai 32  
    byte, tạo ra đầu ra 32 byte. Nó có các  
    hàm sau:

    GENERATE_PRIVATE()  
        Tạo một khóa riêng mới.

    DERIVE_PUBLIC(privkey)  
        Trả về khóa công khai tương ứng với khóa riêng đã cho.

    DH(privkey, pubkey)  
        Tạo một bí mật chung từ khóa riêng và khóa công khai đã cho.

HKDF(salt, ikm, info, n)  
    một hàm dẫn xuất khóa mật mã nhận một vật liệu khóa đầu vào ikm (mà  
    nên có entropy tốt nhưng không yêu cầu là một chuỗi ngẫu nhiên đều), một muối  
    độ dài 32 byte, và một giá trị 'info' cụ thể theo ngữ cảnh, và tạo ra một đầu ra  
    n byte phù hợp để sử dụng như vật liệu khóa.

    Sử dụng HKDF như được chỉ định trong [RFC 5869](https://tools.ietf.org/html/rfc5869), sử dụng hàm băm HMAC SHA-256  
    như được chỉ định trong [RFC 2104](https://tools.ietf.org/html/rfc2104). Điều này có nghĩa là SALT_LEN tối đa là 32 byte.

### Định dạng

Định dạng LS2 được mã hóa gồm ba lớp lồng nhau:

- Một lớp ngoài chứa thông tin văn bản thuần cần thiết để lưu trữ và truy xuất.
- Một lớp giữa xử lý xác thực khách hàng.
- Một lớp trong chứa dữ liệu LS2 thực tế.

Định dạng tổng thể trông như sau::

    Dữ liệu lớp 0 + Enc(dữ liệu lớp 1 + Enc(dữ liệu lớp 2)) + Chữ ký

Lưu ý rằng LS2 được mã hóa là ẩn danh. Destination không nằm trong tiêu đề.  
Vị trí lưu trữ DHT là SHA-256(loại chữ ký || khóa công khai ẩn danh), và được quay hàng ngày.

KHÔNG sử dụng tiêu đề LS2 chuẩn được chỉ định ở trên.

#### Lớp 0 (ngoài)
Loại  
    1 byte

    Không thực sự nằm trong tiêu đề, nhưng là một phần của dữ liệu được bao phủ bởi chữ ký.  
    Lấy từ trường trong Tin nhắn Lưu trữ Cơ sở dữ liệu.

Loại chữ ký khóa công khai ẩn danh  
    2 byte, big endian  
    Điều này sẽ luôn là loại 11, xác định một khóa ẩn danh Red25519.

Khóa công khai ẩn danh  
    Độ dài như được ngụ ý bởi loại chữ ký

Dấu thời gian công bố  
    4 byte, big endian

    Giây kể từ epoch, quay vòng vào năm 2106

Hết hạn  
    2 byte, big endian

    Chênh lệch từ dấu thời gian công bố tính bằng giây, tối đa 18,2 giờ

Cờ  
    2 byte

    Thứ tự bit: 15 14 ... 3 2 1 0

    Bit 0: Nếu 0, không có khóa ngoại tuyến; nếu 1, có khóa ngoại tuyến

    Các bit khác: đặt thành 0 để tương thích với các mục đích sử dụng trong tương lai

Dữ liệu khóa tạm thời  
    Có mặt nếu cờ cho biết có khóa ngoại tuyến

    Dấu thời gian hết hạn  
        4 byte, big endian

        Giây kể từ epoch, quay vòng vào năm 2106

    Loại chữ ký tạm thời  
        2 byte, big endian

    Khóa công khai ký tạm thời  
        Độ dài như được ngụ ý bởi loại chữ ký

    Chữ ký  
        Độ dài như được ngụ ý bởi loại chữ ký khóa công khai ẩn danh

        Trên dấu thời gian hết hạn, loại chữ ký tạm thời và khóa công khai tạm thời.

        Được xác minh bằng khóa công khai ẩn danh.

lenOuterCiphertext  
    2 byte, big endian

outerCiphertext  
    lenOuterCiphertext byte

    Dữ liệu lớp 1 đã mã hóa. Xem bên dưới về thuật toán dẫn xuất khóa và mã hóa.

Chữ ký  
    Độ dài như được ngụ ý bởi loại chữ ký của khóa ký được sử dụng

    Chữ ký của tất cả các nội dung ở trên.

    Nếu cờ cho biết có khóa ngoại tuyến, chữ ký được xác minh bằng khóa công khai tạm thời.  
    Nếu không, chữ ký được xác minh bằng khóa công khai ẩn danh.

#### Lớp 1 (giữa)
Cờ  
    1 byte
    
    Thứ tự bit: 76543210

    Bit 0: 0 cho mọi người, 1 cho từng khách hàng, phần xác thực theo sau

    Bit 3-1: Sơ đồ xác thực, chỉ nếu bit 0 được đặt thành 1 cho từng khách hàng, nếu không 000  
              000: Xác thực khách hàng DH (hoặc không có xác thực từng khách hàng)  
              001: Xác thực khách hàng PSK

    Bit 7-4: Không sử dụng, đặt thành 0 để tương thích trong tương lai

Dữ liệu xác thực khách hàng DH  
    Có mặt nếu bit cờ 0 được đặt thành 1 và bit cờ 3-1 được đặt thành 000.

    ephemeralPublicKey  
        32 byte

    clients  
        2 byte, big endian

        Số lượng mục authClient theo sau, 40 byte mỗi cái

    authClient  
        Dữ liệu ủy quyền cho một khách hàng duy nhất.  
        Xem bên dưới về thuật toán ủy quyền từng khách hàng.

        clientID_i  
            8 byte

        clientCookie_i  
            32 byte

Dữ liệu xác thực khách hàng PSK  
    Có mặt nếu bit cờ 0 được đặt thành 1 và bit cờ 3-1 được đặt thành 001.

    authSalt  
        32 byte

    clients  
        2 byte, big endian

        Số lượng mục authClient theo sau, 40 byte mỗi cái

    authClient  
        Dữ liệu ủy quyền cho một khách hàng duy nhất.  
        Xem bên dưới về thuật toán ủy quyền từng khách hàng.

        clientID_i  
            8 byte

        clientCookie_i  
            32 byte

innerCiphertext  
    Độ dài ngụ ý bởi lenOuterCiphertext (bất kỳ dữ liệu nào còn lại)

    Dữ liệu lớp 2 đã mã hóa. Xem bên dưới về thuật toán dẫn xuất khóa và mã hóa.

#### Lớp 2 (trong)
Loại  
    1 byte

    Hoặc 3 (LS2) hoặc 7 (Meta LS2)

Dữ liệu  
    Dữ liệu LeaseSet2 cho loại đã cho.

    Bao gồm tiêu đề và chữ ký.

### Dẫn xuất khóa ẩn danh

Chúng tôi sử dụng sơ đồ sau cho việc ẩn danh khóa,  
dựa trên Ed25519 và [ZCash RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf).  
Các chữ ký Re25519 là trên đường cong Ed25519, sử dụng SHA-512 cho hàm băm.

Chúng tôi không sử dụng [phụ lục A.2 của Tor's rend-spec-v3.txt](https://spec.torproject.org/rend-spec-v3),  
có mục tiêu thiết kế tương tự, vì các khóa công khai ẩn danh của nó  
có thể nằm ngoài nhóm con bậc nguyên tố, với các hệ quả bảo mật chưa biết.

#### Mục tiêu

- Khóa công khai ký trong destination chưa ẩn danh phải là  
  Ed25519 (loại chữ ký 7) hoặc Red25519 (loại chữ ký 11);  
  không hỗ trợ các loại chữ ký khác
- Nếu khóa công khai ký là ngoại tuyến, khóa công khai ký tạm thời cũng phải là Ed25519
- Việc ẩn danh khóa đơn giản về mặt tính toán
- Sử dụng các nguyên thủy mật mã hiện có
- Các khóa công khai ẩn danh không thể được gỡ ẩn danh
- Các khóa công khai ẩn danh phải nằm trên đường cong Ed25519 và nhóm con bậc nguyên tố
- Phải biết khóa công khai ký của destination  
  (không yêu cầu destination đầy đủ) để dẫn xuất khóa công khai ẩn danh
- Tùy chọn cung cấp một bí mật bổ sung cần thiết để dẫn xuất khóa công khai ẩn danh

#### Bảo mật

Bảo mật của một sơ đồ ẩn danh yêu cầu rằng  
phân bố của alpha giống hệt như các khóa riêng chưa ẩn danh.  
Tuy nhiên, khi chúng ta ẩn danh một khóa riêng Ed25519 (loại chữ ký 7)  
thành một khóa riêng Red25519 (loại chữ ký 11), phân bố là khác nhau.  
Để đáp ứng các yêu cầu của [zcash section 4.1.6.1](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf),  
Red25519 (loại chữ ký 11) nên được sử dụng cho cả các khóa chưa ẩn danh, để  
"tổ hợp của một khóa công khai được tạo ngẫu nhiên lại và chữ ký(s)  
dưới khóa đó không tiết lộ khóa mà nó được tạo ngẫu nhiên lại từ."  
Chúng tôi cho phép loại 7 cho các destination hiện tại, nhưng khuyến nghị  
loại 11 cho các destination mới sẽ được mã hóa.

#### Định nghĩa

B  
    Điểm cơ sở Ed25519 (generator) 2^255 - 19 như trong [Ed25519](http://cr.yp.to/papers.html#ed25519)

L  
    Bậc Ed25519 2^252 + 27742317777372353535851937790883648493  
    như trong [Ed25519](http://cr.yp.to/papers.html#ed25519)

DERIVE_PUBLIC(a)  
    Chuyển một khóa riêng thành công khai, như trong Ed25519 (nhân với G)

alpha  
    Một số ngẫu nhiên 32 byte được biết bởi những người biết destination.

GENERATE_ALPHA(destination, date, secret)  
    Tạo alpha cho ngày hiện tại, cho những người biết destination và bí mật.  
    Kết quả phải được phân bố giống hệt như các khóa riêng Ed25519.

a  
    Khóa riêng ký EdDSA hoặc RedDSA 32 byte chưa ẩn danh được sử dụng để ký destination

A  
    Khóa công khai ký EdDSA hoặc RedDSA 32 byte chưa ẩn danh trong destination,  
    = DERIVE_PUBLIC(a), như trong Ed25519

a'  
    Khóa riêng ký EdDSA 32 byte ẩn danh được sử dụng để ký leaseset được mã hóa  
    Đây là một khóa riêng EdDSA hợp lệ.

A'  
    Khóa công khai ký EdDSA 32 byte ẩn danh trong Destination,  
    có thể được tạo bằng DERIVE_PUBLIC(a'), hoặc từ A và alpha.  
    Đây là một khóa công khai EdDSA hợp lệ, trên đường cong và trên nhóm con bậc nguyên tố.

LEOS2IP(x)  
    Đảo ngược thứ tự các byte đầu vào thành little-endian

H*(x)  
    32 byte = (LEOS2IP(SHA512(x))) mod B, giống như trong hash-and-reduce của Ed25519

#### Tính toán ẩn danh

Một bí mật alpha mới và các khóa ẩn danh phải được tạo mỗi ngày (UTC).  
Bí mật alpha và các khóa ẩn danh được tính như sau.

GENERATE_ALPHA(destination, date, secret), cho tất cả các bên:

```text
// GENERATE_ALPHA(destination, date, secret)

  // bí mật là tùy chọn, nếu không thì độ dài bằng 0
  A = khóa công khai ký của destination
  stA = loại chữ ký của A, 2 byte big endian (0x0007 hoặc 0x000b)
  stA' = loại chữ ký của khóa công khai ẩn danh A', 2 byte big endian (0x000b)
  keydata = A || stA || stA'
  datestring = 8 byte ASCII YYYYMMDD từ ngày hiện tại UTC
  secret = chuỗi mã hóa UTF-8
  seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || secret, "i2pblinding1", 64)
  // coi seed là giá trị 64 byte little-endian
  alpha = seed mod L
```

BLIND_PRIVKEY(), cho chủ sở hữu công bố leaseset:

```text
// BLIND_PRIVKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  // Nếu cho một khóa riêng Ed25519 (loại 7)
  seed = khóa riêng ký của destination
  a = nửa trái của SHA512(seed) và được kẹp như thường lệ cho Ed25519
  // nếu không, cho một khóa riêng Red25519 (loại 11)
  a = khóa riêng ký của destination
  // Phép cộng sử dụng số học vô hướng
  khóa riêng ký ẩn danh = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
  khóa công khai ký ẩn danh = A' = DERIVE_PUBLIC(a')
```

BLIND_PUBKEY(), cho các client truy xuất leaseset:

```text
// BLIND_PUBKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  A = khóa công khai ký của destination
  // Phép cộng sử dụng phần tử nhóm (điểm trên đường cong)
  khóa công khai ẩn danh = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```

Cả hai phương pháp tính toán A' đều cho cùng kết quả, như yêu cầu.

#### Ký

Leaseset chưa ẩn danh được ký bởi khóa riêng ký Ed25519 hoặc Red25519 chưa ẩn danh  
và được xác minh bằng khóa công khai ký Ed25519 hoặc Red25519 chưa ẩn danh (loại chữ ký 7 hoặc 11) như thường lệ.

Nếu khóa công khai ký là ngoại tuyến,  
leaset chưa ẩn danh được ký bởi khóa riêng ký tạm thời Ed25519 hoặc Red25519 chưa ẩn danh  
và được xác minh bằng khóa công khai ký tạm thời Ed25519 hoặc Red25519 chưa ẩn danh (loại chữ ký 7 hoặc 11) như thường lệ.  
Xem bên dưới để biết thêm ghi chú về khóa ngoại tuyến cho leaseset được mã hóa.

Đối với việc ký leaseset được mã hóa, chúng tôi sử dụng Red25519, dựa trên [RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)  
để ký và xác minh với các khóa ẩn danh.  
Các chữ ký Red25519 là trên đường cong Ed25519, sử dụng SHA-512 cho hàm băm.

Red25519 giống hệt với Ed25519 chuẩn ngoại trừ như được chỉ định bên dưới.

#### Tính toán Ký/Xác minh

Phần ngoài của leaseset được mã hóa sử dụng các khóa và chữ ký Red25519.

Red25519 gần như giống hệt với Ed25519. Có hai điểm khác biệt:

Khóa riêng Red25519 được tạo từ các số ngẫu nhiên và sau đó phải được giảm mod L, trong đó L được định nghĩa ở trên.  
Khóa riêng Ed25519 được tạo từ các số ngẫu nhiên và sau đó được "kẹp" bằng  
mặt nạ bit cho byte 0 và 31. Điều này không được thực hiện cho Red25519.  
Các hàm GENERATE_ALPHA() và BLIND_PRIVKEY() được định nghĩa ở trên tạo ra các khóa riêng Red25519 đúng bằng cách sử dụng mod L.

Trong Red25519, phép tính r để ký sử dụng thêm dữ liệu ngẫu nhiên,  
và sử dụng giá trị khóa công khai thay vì băm của khóa riêng.  
Do dữ liệu ngẫu nhiên, mọi chữ ký Red25519 đều khác nhau, ngay cả khi  
ký cùng dữ liệu với cùng khóa.

Ký:

```text
T = 80 byte ngẫu nhiên
  r = H*(T || publickey || message)
  // phần còn lại giống như trong Ed25519
```

Xác minh:

```text
// giống như trong Ed25519
```

### Mã hóa và xử lý

#### Dẫn xuất các subcredentials
Là một phần của quá trình ẩn danh, chúng ta cần đảm bảo rằng một LS2 được mã hóa chỉ có thể được  
giải mã bởi ai đó biết khóa công khai ký tương ứng của Destination.  
Không yêu cầu Destination đầy đủ.  
Để đạt được điều này, chúng ta dẫn xuất một credential từ khóa công khai ký:

```text
A = khóa công khai ký của destination
  stA = loại chữ ký của A, 2 byte big endian (0x0007 hoặc 0x000b)
  stA' = loại chữ ký của A', 2 byte big endian (0x000b)
  keydata = A || stA || stA'
  credential = H("credential", keydata)
```

Chuỗi cá nhân hóa đảm bảo rằng credential không bị trùng với bất kỳ băm nào được sử dụng  
làm khóa tra cứu DHT, chẳng hạn như băm Destination thuần túy.

Đối với một khóa ẩn danh đã cho, chúng ta có thể dẫn xuất một subcredential:

```text
subcredential = H("subcredential", credential || blindedPublicKey)
```

Subcredential được bao gồm trong các quá trình dẫn xuất khóa bên dưới, điều này ràng buộc các khóa đó  
với việc biết khóa công khai ký của Destination.

#### Mã hóa lớp 1
Đầu tiên, đầu vào cho quá trình dẫn xuất khóa được chuẩn bị:

```text
outerInput = subcredential || publishedTimestamp
```

Tiếp theo, một muối ngẫu nhiên được tạo:

```text
outerSalt = CSRNG(32)
```

Sau đó, khóa được sử dụng để mã hóa lớp 1 được dẫn xuất:

```text
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
  outerKey = keys[0:31]
  outerIV = keys[32:43]
```

Cuối cùng, văn bản rõ lớp 1 được mã hóa và tuần tự hóa:

```text
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```

#### Giải mã lớp 1
Muối được phân tích từ văn bản mã lớp 1:

```text
outerSalt = outerCiphertext[0:31]
```

Sau đó, khóa được sử dụng để mã hóa lớp 1 được dẫn xuất:

```text
outerInput = subcredential || publishedTimestamp
  keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
  outerKey = keys[0:31]
  outerIV = keys[32:43]
```

Cuối cùng, văn bản mã lớp 1 được giải mã:

```text
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```

#### Mã hóa lớp 2
Khi xác thực khách hàng được bật, ``authCookie`` được tính như mô tả bên dưới.  
Khi xác thực khách hàng bị tắt, ``authCookie`` là mảng byte độ dài bằng 0.

Việc mã hóa tiến hành theo cách tương tự như lớp 1:

```text
innerInput = authCookie || subcredential || publishedTimestamp
  innerSalt = CSRNG(32)
  keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
  innerKey = keys[0:31]
  innerIV = keys[32:43]
  innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```

#### Giải mã lớp 2
Khi xác thực khách hàng được bật, ``authCookie`` được tính như mô tả bên dưới.  
Khi xác thực khách hàng bị tắt, ``authCookie`` là mảng byte độ dài bằng 0.

Việc giải mã tiến hành theo cách tương tự như lớp 1:

```text
innerInput = authCookie || subcredential || publishedTimestamp
  innerSalt = innerCiphertext[0:31]
  keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
  innerKey = keys[0:31]
  innerIV = keys[32:43]
  innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```

### Ủy quyền theo khách hàng

Khi xác thực khách hàng được bật cho một Destination, máy chủ duy trì một danh sách các  
khách hàng mà họ ủy quyền để giải mã dữ liệu LS2 được mã hóa. Dữ liệu được lưu trữ cho từng khách hàng  
phụ thuộc vào cơ chế ủy quyền, và bao gồm một số dạng vật liệu khóa mà mỗi  
khách hàng tạo và gửi đến máy chủ thông qua một cơ chế ngoài băng tần an toàn.

Có hai lựa chọn để triển khai ủy quyền theo khách hàng:

#### Xác thực khách hàng DH
Mỗi khách hàng tạo một cặp khóa DH ``[csk_i, cpk_i]``, và gửi khóa công khai ``cpk_i``  
đến máy chủ.

Xử lý máy chủ  
^^^^^^^^^^^^^^^^^
Máy chủ tạo một ``authCookie`` mới và một cặp khóa DH tạm thời:

```text
authCookie = CSRNG(32)
  esk = GENERATE_PRIVATE()
  epk = DERIVE_PUBLIC(esk)
```

Sau đó, đối với mỗi khách hàng được ủy quyền, máy chủ mã hóa ``authCookie`` bằng khóa công khai của nó:

```text
sharedSecret = DH(esk, cpk_i)
  authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
  okm = HKDF(epk, authInput, "ELS2_XCA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
  clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```

Máy chủ đặt mỗi bộ ``[clientID_i, clientCookie_i]`` vào lớp 1 của  
LS2 được mã hóa, cùng với ``epk``.

Xử lý khách hàng  
^^^^^^^^^^^^^^^^^
Khách hàng sử dụng khóa riêng của nó để dẫn xuất định danh khách hàng mong đợi ``clientID_i``,  
khóa mã hóa ``clientKey_i``, và IV mã hóa ``clientIV_i``:

```text
sharedSecret = DH(csk_i, epk)
  authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
  okm = HKDF(epk, authInput, "ELS2_XCA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
```

Sau đó, khách hàng tìm kiếm dữ liệu ủy quyền lớp 1 để tìm mục chứa  
``clientID_i``. Nếu tồn tại mục khớp, khách hàng giải mã nó để lấy  
``authCookie``:

```text
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```

#### Xác thực khách hàng khóa chia sẻ trước (PSK)
Mỗi khách hàng tạo một khóa bí mật 32 byte ``psk_i``, và gửi nó đến máy chủ.  
Ngoài ra, máy chủ có thể tạo khóa bí mật, và gửi nó đến một hoặc nhiều khách hàng.

Xử lý máy chủ  
^^^^^^^^^^^^^^^^^
Máy chủ tạo một ``authCookie`` mới và muối:

```text
authCookie = CSRNG(32)
  authSalt = CSRNG(32)
```

Sau đó, đối với mỗi khách hàng được ủy quyền, máy chủ mã hóa ``authCookie`` bằng khóa chia sẻ trước của nó:

```text
authInput = psk_i || subcredential || publishedTimestamp
  okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
  clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```

Máy chủ đặt mỗi bộ ``[clientID_i, clientCookie_i]`` vào lớp 1 của  
LS2 được mã hóa, cùng với ``authSalt``.

Xử lý khách hàng  
^^^^^^^^^^^^^^^^^
Khách hàng sử dụng khóa chia sẻ trước của nó để dẫn xuất định danh khách hàng mong đợi ``clientID_i``,  
khóa mã hóa ``clientKey_i``, và IV mã hóa ``clientIV_i``:

```text
authInput = psk_i || subcredential || publishedTimestamp
  okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
```

Sau đó, khách hàng tìm kiếm dữ liệu ủy quyền lớp 1 để tìm mục chứa  
``clientID_i``. Nếu tồn tại mục khớp, khách hàng giải mã nó để lấy  
``authCookie``:

```text
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```

#### Xem xét bảo mật
Cả hai cơ chế ủy quyền khách hàng trên đều cung cấp quyền riêng tư cho thành viên khách hàng.  
Một thực thể chỉ biết Destination có thể thấy có bao nhiêu khách hàng đang đăng ký tại bất kỳ  
thời điểm nào, nhưng không thể theo dõi khách hàng nào đang được thêm hoặc thu hồi.

Các máy chủ NÊN xáo trộn thứ tự các khách hàng mỗi khi họ tạo một LS2 được mã hóa, để  
ngăn khách hàng biết vị trí của họ trong danh sách và suy ra khi khách hàng khác được thêm hoặc thu hồi.

Một máy chủ CÓ THỂ chọn ẩn số lượng khách hàng đang đăng ký bằng cách chèn các mục ngẫu nhiên  
vào danh sách dữ liệu ủy quyền.

Ưu điểm của xác thực khách hàng DH  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Bảo mật của sơ đồ không hoàn toàn phụ thuộc vào việc trao đổi ngoài băng tần vật liệu khóa khách hàng.  
  Khóa riêng của khách hàng không cần rời khỏi thiết bị của họ, và do đó một  
  kẻ thù có thể chặn việc trao đổi ngoài băng tần, nhưng không thể phá vỡ thuật toán DH,  
  không thể giải mã LS2 được mã hóa, hoặc xác định thời gian khách hàng được cấp quyền truy cập.

Nhược điểm của xác thực khách hàng DH  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Yêu cầu N + 1 thao tác DH ở phía máy chủ cho N khách hàng.
- Yêu cầu một thao tác DH ở phía khách hàng.
- Yêu cầu khách hàng tạo khóa bí mật.

Ưu điểm của xác thực khách hàng PSK  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Không yêu cầu thao tác DH nào.
- Cho phép máy chủ tạo khóa bí mật.
- Cho phép máy chủ chia sẻ cùng một khóa với nhiều khách hàng, nếu muốn.

Nhược điểm của xác thực khách hàng PSK  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Bảo mật của sơ đồ phụ thuộc nghiêm trọng vào việc trao đổi ngoài băng tần vật liệu khóa khách hàng.  
  Một kẻ thù chặn được việc trao đổi cho một khách hàng cụ thể có thể giải mã  
  bất kỳ LS2 được mã hóa nào sau đó mà khách hàng đó được ủy quyền, cũng như xác định  
  khi quyền truy cập của khách hàng bị thu hồi.

### LS được mã hóa với địa chỉ Base 32

Xem đề xuất 149.

Bạn không thể sử dụng LS2 được mã hóa cho bittorrent, vì các phản hồi thông báo gọn gàng là 32 byte.  
32 byte chỉ chứa băm. Không có chỗ cho dấu hiệu rằng  
leaseset được mã hóa, hoặc các loại chữ ký.

### LS được mã hóa với khóa ngoại tuyến

Đối với leaseset được mã hóa có khóa ngoại tuyến, các khóa riêng ẩn danh cũng phải được tạo ngoại tuyến,  
một cho mỗi ngày.

Vì khối chữ ký ngoại tuyến tùy chọn nằm trong phần văn bản rõ của leaseset được mã hóa,  
bất kỳ ai quét các floodfill có thể sử dụng điều này để theo dõi leaseset (nhưng không giải mã nó)  
trong vài ngày.  
Để ngăn chặn điều này, chủ sở hữu khóa nên tạo các khóa tạm thời mới  
cho mỗi ngày cũng vậy.  
Cả khóa tạm thời và khóa ẩn danh đều có thể được tạo trước, và giao cho router  
theo lô.

Không có định dạng tệp nào được định nghĩa trong đề xuất này để đóng gói nhiều khóa tạm thời và  
khóa ẩn danh và cung cấp chúng cho client hoặc router.  
Không có cải tiến giao thức I2CP nào được định nghĩa trong đề xuất này để hỗ trợ  
leaseset được mã hóa với khóa ngoại tuyến.

### Ghi chú

- Một dịch vụ sử dụng leaseset được mã hóa sẽ công bố phiên bản được mã hóa đến các  
  floodfill. Tuy nhiên, để hiệu quả, nó sẽ gửi leaseset chưa được mã hóa đến  
  client trong tin nhắn tỏi được bao bọc, sau khi xác thực (qua danh sách trắng, ví dụ).

- Các floodfill có thể giới hạn kích thước tối đa ở mức hợp lý để ngăn lạm dụng.

- Sau khi giải mã, một số kiểm tra nên được thực hiện, bao gồm việc  
  dấu thời gian và hết hạn bên trong khớp với những cái ở cấp độ trên cùng.

- ChaCha20 được chọn thay vì AES. Mặc dù tốc độ tương tự nếu hỗ trợ phần cứng AES  
  có sẵn, ChaCha20 nhanh hơn 2,5-3 lần khi  
  hỗ trợ phần cứng AES không có, chẳng hạn như trên các thiết bị ARM cấp thấp.

- Chúng tôi không quan tâm đủ về tốc độ để sử dụng BLAKE2b có khóa. Nó có kích thước đầu ra  
  đủ lớn để chứa n lớn nhất chúng tôi yêu cầu (hoặc chúng tôi có thể gọi nó một lần cho mỗi  
  khóa mong muốn với một đối số bộ đếm). BLAKE2b nhanh hơn nhiều so với SHA-256, và  
  BLAKE2b có khóa sẽ giảm tổng số lần gọi hàm băm.  
  Tuy nhiên, xem đề xuất 148, nơi đề xuất rằng chúng tôi chuyển sang BLAKE2b vì các lý do khác.  
  Xem [Secure key derivation performance](https://www.lvh.io/posts/secure-key-derivation-performance.html).

### Meta LS2

Điều này được sử dụng để thay thế đa kết nối. Giống như bất kỳ leaseset nào, điều này được ký bởi người tạo. Đây là một danh sách được xác thực của các băm destination.

Meta LS2 là đỉnh, và có thể là các nút trung gian của,  
một cấu trúc cây.  
Nó chứa một số mục, mỗi mục trỏ đến một LS, LS2 hoặc một Meta LS2 khác  
để hỗ trợ đa kết nối quy mô lớn.  
Một Meta LS2 có thể chứa hỗn hợp các mục LS, LS2 và Meta LS2.  
Các lá của cây luôn là một LS hoặc LS2.  
Cây là một DAG; các vòng lặp bị cấm; các client thực hiện tra cứu phải phát hiện và  
từ chối theo các vòng lặp.

Một Meta LS2 có thể có thời gian hết hạn lâu hơn nhiều so với một LS hoặc LS2 chuẩn.  
Cấp độ trên cùng có thể có thời gian hết hạn vài giờ sau ngày công bố.  
Thời gian hết hạn tối đa sẽ được các floodfill và client thực thi, và đang được xác định.

Mục đích sử dụng cho Meta LS2 là đa kết nối quy mô lớn, nhưng không có thêm  
bảo vệ nào cho việc liên kết các router với leaseset (tại thời điểm khởi động lại router) hơn  
được cung cấp hiện tại với LS hoặc LS2.  
Điều này tương đương với trường hợp sử dụng "facebook", có lẽ không cần  
bảo vệ liên kết. Trường hợp sử dụng này có lẽ cần khóa ngoại tuyến,  
được cung cấp trong tiêu đề chuẩn tại mỗi nút của cây.

Giao thức back-end để phối hợp giữa các router lá, các chữ ký Meta LS trung gian và chính  
không được chỉ định ở đây. Các yêu cầu cực kỳ đơn giản - chỉ cần xác minh rằng peer đang hoạt động,  
và công bố một LS mới mỗi vài giờ. Độ phức tạp duy nhất là chọn  
các publisher mới cho các Meta LS cấp độ trên cùng hoặc cấp độ trung gian khi thất bại.

Leaseset kết hợp nơi các lease từ nhiều router được kết hợp, ký và công bố  
trong một leaseset duy nhất được ghi trong đề xuất 140, "đa kết nối vô hình".  
Đề xuất này không khả thi như đã viết, vì các kết nối streaming sẽ không  
"gắn bó" với một router duy nhất, xem http://zzz.i2p/topics/2335 .

Giao thức back-end, và tương tác với nội bộ router và client, sẽ  
rất phức tạp đối với đa kết nối vô hình.

Để tránh quá tải floodfill cho Meta LS cấp độ trên cùng, thời gian hết hạn nên  
ít nhất là vài giờ. Client phải lưu trữ bộ nhớ đệm Meta LS cấp độ trên cùng, và duy trì  
nó qua các lần khởi động lại nếu chưa hết hạn.

Chúng ta cần định nghĩa một số thuật toán để client duyệt cây, bao gồm các phương án dự phòng,  
để việc sử dụng được phân tán. Một số hàm của khoảng cách băm, chi phí và tính ngẫu nhiên.  
Nếu một nút có cả LS hoặc LS2 và Meta LS, chúng ta cần biết khi nào được phép  
sử dụng các leaseset đó, và khi nào nên tiếp tục duyệt cây.

Tìm kiếm với  
    Cờ LS chuẩn (1)  
Lưu trữ với  
    Loại Meta LS2 (7)  
Lưu trữ tại  
    Băm của destination  
    Băm này sau đó được sử dụng để tạo "khóa định tuyến" hàng ngày, như trong LS1  
Thời gian hết hạn điển hình  
    Hàng giờ. Tối đa 18,2 giờ (65535 giây)  
Được công bố bởi  
    Destination "chính" hoặc điều phối viên, hoặc các điều phối viên trung gian

### Định dạng

```
Tiêu đề LS2 chuẩn như được chỉ định ở trên

  Phần riêng cho loại Meta LS2
  - Thuộc tính (Ánh xạ như được chỉ định trong đặc tả cấu trúc chung, 2 byte 0 nếu không có)
  - Số lượng mục (1 byte) Tối đa TBD
  - Các mục. Mỗi mục chứa: (40 byte)
    - Băm (32 byte)
    - Cờ (2 byte)
      TBD. Đặt tất cả về 0 để tương thích với các mục đích sử dụng trong tương lai.
    - Loại (1 byte) Loại LS mà nó tham chiếu;
      1 cho LS, 3 cho LS2, 5 cho được mã hóa, 7 cho meta, 0 cho chưa biết.
    - Chi phí (ưu tiên) (1 byte)
    - Hết hạn (4 byte) (4 byte, big endian, giây kể từ epoch, quay vòng vào năm 2106)
  - Số lượng thu hồi (1 byte) Tối đa TBD
  - Thu hồi: Mỗi thu hồi chứa: (32 byte)
    - Băm (32 byte)

  Chữ ký LS2 chuẩn:
  - Chữ ký (40+ byte)
    Chữ ký của tất cả các nội dung ở trên.
```

Cờ và thuộc tính: để sử dụng trong tương lai

### Ghi chú

- Một dịch vụ phân tán sử dụng điều này sẽ có một hoặc nhiều "chính" với khóa riêng của destination dịch vụ. Họ sẽ (ngoài băng tần) xác định danh sách hiện tại các destination hoạt động và sẽ công bố Meta LS2. Để dự phòng, nhiều "chính" có thể đa kết nối (tức là công bố đồng thời) Meta LS2.

- Một dịch vụ phân tán có thể bắt đầu với một destination duy nhất hoặc sử dụng đa kết nối kiểu cũ, sau đó chuyển sang Meta LS2. Một tìm kiếm LS chuẩn có thể trả về bất kỳ một trong LS, LS2 hoặc Meta LS2.

- Khi một dịch vụ sử dụng Meta LS2, nó không có tunnel (lease).

### Bản ghi Dịch vụ

Đây là một bản ghi cá nhân nói rằng một destination đang tham gia vào một  
dịch vụ. Nó được gửi từ người tham gia đến floodfill. Nó không bao giờ được gửi  
riêng lẻ bởi một floodfill, mà chỉ như một phần của Danh sách Dịch vụ. Bản ghi Dịch vụ cũng được sử dụng để thu hồi sự tham gia vào một dịch vụ, bằng cách đặt  
thời gian hết hạn thành không.

Đây không phải là một LS2 nhưng nó sử dụng định dạng tiêu đề và chữ ký LS2 chuẩn.

Tìm kiếm với  
    n/a, xem Danh sách Dịch vụ  
Lưu trữ với  
    Loại Bản ghi Dịch vụ (9)  
Lưu trữ tại  
    Băm của tên dịch vụ  
    Băm này sau đó được sử dụng để tạo "khóa định tuyến" hàng ngày, như trong LS1  
Thời gian hết hạn điển hình  
    Hàng giờ. Tối đa 18,2 giờ (65535 giây)  
Được công bố bởi  
    Destination

### Định dạng

```
Tiêu đề LS2 chuẩn như được chỉ định ở trên

  Phần riêng cho loại Bản ghi Dịch vụ
  - Cổng (2 byte, big endian) (0 nếu không xác định)
  - Băm của tên dịch vụ (32 byte)

  Chữ ký LS2 chuẩn:
  - Chữ ký (40+ byte)
    Chữ ký của tất cả các nội dung ở trên.
```

### Ghi chú

- Nếu hết hạn là toàn bộ số 0, floodfill nên thu hồi bản ghi và không còn  
  bao gồm nó trong danh sách dịch vụ.

- Lưu trữ: Floodfill có thể giới hạn nghiêm ngặt việc lưu trữ các bản ghi này và  
  giới hạn số lượng bản ghi được lưu trữ cho mỗi băm và thời gian hết hạn của chúng. Một danh sách trắng  
  các băm cũng có thể được sử dụng.

- Bất kỳ loại netdb nào khác tại cùng băm có ưu tiên, vì vậy một bản ghi dịch vụ không bao giờ  
  có thể ghi đè LS/RI, nhưng một LS/RI sẽ ghi đè tất cả các bản ghi dịch vụ tại băm đó.

### Danh sách Dịch vụ

Điều này không giống gì với một LS2 và sử dụng định dạng khác.

Danh sách dịch vụ được tạo và ký bởi floodfill. Nó không được xác thực  
theo nghĩa bất kỳ ai cũng có thể tham gia một dịch vụ bằng cách công bố một Bản ghi Dịch vụ đến một  
floodfill.

Một Danh sách Dịch vụ chứa các Bản ghi Dịch vụ Ngắn, không phải Bản ghi Dịch vụ đầy đủ. Những bản ghi này  
chứa chữ ký nhưng chỉ băm, không phải destination đầy đủ, vì vậy chúng không thể được  
xác minh mà không có destination đầy đủ.

Bảo mật, nếu có, và tính mong muốn của danh sách dịch vụ đang được xác định.  
Các floodfill có thể giới hạn việc công bố và tra cứu, đến một danh sách trắng các dịch vụ,  
nhưng danh sách trắng đó có thể thay đổi tùy theo triển khai hoặc sở thích của người vận hành.  
Có thể không thể đạt được sự đồng thuận về một danh sách trắng cơ bản chung  
giữa các triển khai.

Nếu tên dịch vụ được bao gồm trong bản ghi dịch vụ ở trên,  
thì các người vận hành floodfill có thể phản đối; nếu chỉ băm được bao gồm,  
thì không có xác minh, và một bản ghi dịch vụ có thể "vào" trước  
bất kỳ loại netdb nào khác và được lưu trữ trong floodfill.

Tìm kiếm với  
    Loại tìm kiếm Danh sách Dịch vụ (11)  
Lưu trữ với  
    Loại Danh sách Dịch vụ (11)  
Lưu trữ tại  
    Băm của tên dịch vụ  
    Băm này sau đó được sử dụng để tạo "khóa định tuyến" hàng ngày, như trong LS1  
Thời gian hết hạn điển hình  
    Hàng giờ, không được chỉ định trong danh sách, tùy theo chính sách cục bộ  
Được công bố bởi  
    Không ai, không bao giờ gửi đến floodfill, không bao giờ được lan truyền.

### Định dạng

KHÔNG sử dụng tiêu đề LS2 chuẩn được chỉ định ở trên.

```
- Loại (1 byte)
    Không thực sự nằm trong tiêu đề, nhưng là một phần của dữ liệu được bao phủ bởi chữ ký.
    Lấy từ trường trong Tin nhắn Lưu trữ Cơ sở dữ liệu.
  - Băm của tên dịch vụ (ngầm, trong Tin nhắn Lưu trữ Cơ sở dữ liệu)
  - Băm của Người tạo (floodfill) (32 byte)
  - Dấu thời gian công bố (8 byte, big endian)

  - Số lượng Bản ghi Dịch vụ Ngắn (1 byte)
  - Danh sách các Bản ghi Dịch vụ Ngắn:
    Mỗi Bản ghi Dịch vụ Ngắn chứa (90+ byte)
    - Băm đích (32 byte)
    - Dấu thời gian công bố (8 byte, big endian)
    - Hết hạn (4 byte, big endian) (chênh lệch từ công bố tính bằng ms)
    - Cờ (2 byte)
    - Cổng (2 byte, big endian)
    - Độ dài chữ ký (2 byte, big endian)
    - Chữ ký của đích (40+ byte)

  - Số lượng Bản ghi Thu hồi (1 byte)
  - Danh sách các Bản ghi Thu hồi:
    Mỗi Bản ghi Thu hồi chứa (86+ byte)
    - Băm đích (32 byte)
    - Dấu thời gian công bố (8 byte, big endian)
    - Cờ (2 byte)
    - Cổng (2 byte, big endian)
    - Độ dài chữ ký (2 byte, big endian)
    - Chữ ký của đích (40+ byte)

  - Chữ ký của floodfill (40+ byte)
    Chữ ký của tất cả các nội dung ở trên.
```

Để xác minh chữ ký của Danh sách Dịch vụ:

- thêm vào đầu băm của tên dịch vụ
- loại bỏ băm của người tạo
- Kiểm tra chữ ký của nội dung đã sửa đổi

Để xác minh chữ ký của mỗi Bản ghi Dịch vụ Ngắn:

- lấy destination
- Kiểm tra chữ ký của (dấu thời gian công bố + hết hạn + cờ + cổng + Băm của  
  tên dịch vụ)

Để xác minh chữ ký của mỗi Bản ghi Thu hồi:

- lấy destination
- Kiểm tra chữ ký của (dấu thời gian công bố + 4 byte 0 + cờ + cổng + Băm  
  của tên dịch vụ)

### Ghi chú

- Chúng tôi sử dụng độ dài chữ ký thay vì loại chữ ký để hỗ trợ các loại chữ ký chưa biết.

- Không có thời gian hết hạn của danh sách dịch vụ, người nhận có thể tự quyết định  
  dựa trên chính sách hoặc thời gian hết hạn của các bản ghi riêng lẻ.

- Danh sách Dịch vụ không được lan truyền, chỉ các Bản ghi Dịch vụ riêng lẻ được. Mỗi  
  floodfill tạo, ký và lưu trữ bộ nhớ đệm một Danh sách Dịch vụ. Floodfill sử dụng  
  chính sách riêng của nó cho thời gian lưu trữ bộ nhớ đệm và số lượng tối đa các bản ghi dịch vụ và thu hồi.

## Các thay đổi cần thiết đối với Đặc tả Cấu trúc Chung

### Chứng chỉ khóa

Ngoài phạm vi của đề xuất này.  
Thêm vào các đề xuất ECIES 144 và 145.

### Các cấu trúc trung gian mới

Thêm các cấu trúc mới cho Lease2, MetaLease, LeaseSet2Header và OfflineSignature.  
Có hiệu lực kể từ phiên bản 0.9.38.

### Các loại NetDB mới

Thêm cấu trúc cho mỗi loại leaseset mới, được tích hợp từ trên.  
Đối với LeaseSet2, EncryptedLeaseSet và MetaLeaseSet,  
có hiệu lực kể từ phiên bản 0.9.38.  
Đối với Bản ghi Dịch vụ và Danh sách Dịch vụ,  
ban đầu và chưa lên lịch.

### Loại chữ ký mới

Thêm RedDSA_SHA512_Ed25519 Loại 11.  
Khóa công khai là 32 byte; khóa riêng là 32 byte; băm là 64 byte; chữ ký là 64 byte.

## Các thay đổi cần thiết đối với Đặc tả Mã hóa

Ngoài phạm vi của đề xuất này.  
Xem các đề xuất 144 và 145.

## Các thay đổi cần thiết đối với I2NP

Thêm ghi chú: LS2 chỉ có thể được công
