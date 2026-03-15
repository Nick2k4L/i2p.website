---
title: "Multihoming Vô Hình"
number: "140"
author: "str4d"
created: "2017-05-22"
lastupdated: "2017-07-04"
status: "Mở"
thread: "http://zzz.i2p/topics/2335"
toc: true
---
## Tổng quan

Đề xuất này trình bày một thiết kế giao thức cho phép một máy khách I2P, dịch vụ hoặc tiến trình cân bằng tải bên ngoài quản lý nhiều bộ định tuyến một cách minh bạch, cùng lưu trữ một [Destination](/docs/specs/common-structures/#destination) duy nhất.

Hiện tại, đề xuất này chưa chỉ định một triển khai cụ thể. Nó có thể được triển khai như một phần mở rộng của [I2CP](/docs/specs/i2cp/), hoặc như một giao thức mới.


## Động lực

Đa kết nối (multihoming) là việc sử dụng nhiều bộ định tuyến để lưu trữ cùng một Destination. Cách hiện tại để thực hiện đa kết nối với I2P là chạy cùng một Destination trên mỗi bộ định tuyến một cách độc lập; bộ định tuyến được máy khách sử dụng tại bất kỳ thời điểm nào là bộ định tuyến cuối cùng xuất bản LeaseSet.

Đây là một giải pháp tạm thời và rõ ràng sẽ không hoạt động hiệu quả ở quy mô lớn. Giả sử ta có 100 bộ định tuyến đa kết nối, mỗi bộ có 16 đường hầm. Điều đó đồng nghĩa với 1600 lần xuất bản LeaseSet mỗi 10 phút, hay gần 3 lần mỗi giây. Các nút floodfill sẽ bị quá tải và cơ chế giới hạn (throttles) sẽ được kích hoạt. Và điều này còn chưa tính đến lượng lưu lượng tìm kiếm (lookup traffic).

Đề xuất 123 giải quyết vấn đề này bằng một meta-LeaseSet, liệt kê 100 băm LeaseSet thực tế. Việc tìm kiếm trở thành một quá trình hai bước: trước tiên tra cứu meta-LeaseSet, sau đó tra cứu một trong các LeaseSet được đặt tên. Đây là một giải pháp tốt cho vấn đề lưu lượng tìm kiếm, nhưng riêng lẻ thì nó tạo ra một lỗ hổng bảo mật đáng kể: Có thể xác định được bộ định tuyến đa kết nối nào đang hoạt động bằng cách theo dõi meta-LeaseSet được xuất bản, vì mỗi LeaseSet thực tế tương ứng với một bộ định tuyến duy nhất.

Chúng ta cần một cách để một máy khách hoặc dịch vụ I2P có thể phân tán một Destination duy nhất qua nhiều bộ định tuyến, theo cách không thể phân biệt được với việc sử dụng một bộ định tuyến duy nhất (từ góc nhìn của chính LeaseSet).


## Thiết kế

### Định nghĩa

    User
        Người hoặc tổ chức muốn thực hiện đa kết nối cho Destination(s) của họ.
        Một Destination duy nhất được xem xét ở đây một cách tổng quát (WLOG).

    Client
        Ứng dụng hoặc dịch vụ chạy phía sau Destination. Nó có thể là ứng dụng
        phía máy khách, phía máy chủ, hoặc ngang hàng (peer-to-peer); ta gọi nó
        là máy khách theo nghĩa nó kết nối với các bộ định tuyến I2P.

        Máy khách bao gồm ba phần, có thể nằm trong cùng một tiến trình hoặc
        được chia tách qua nhiều tiến trình hoặc máy (trong cấu hình đa máy khách):

        Balancer
            Phần của máy khách quản lý việc chọn máy ngang hàng và xây dựng
            đường hầm. Tại một thời điểm chỉ có một balancer duy nhất, và nó
            giao tiếp với tất cả các bộ định tuyến I2P. Có thể có các balancer
            dự phòng.

        Frontend
            Phần của máy khách có thể hoạt động song song. Mỗi frontend giao
            tiếp với một bộ định tuyến I2P duy nhất.

        Backend
            Phần của máy khách được chia sẻ giữa tất cả các frontend. Nó không
            giao tiếp trực tiếp với bất kỳ bộ định tuyến I2P nào.

    Router
        Một bộ định tuyến I2P do người dùng vận hành, nằm ở ranh giới giữa mạng
        I2P và mạng của người dùng (tương tự như thiết bị biên trong mạng doanh
        nghiệp). Nó xây dựng các đường hầm theo lệnh từ balancer, và định tuyến
        các gói tin cho máy khách hoặc frontend.

### Tổng quan cấp cao

Hãy tưởng tượng cấu hình mong muốn như sau:

- Một ứng dụng máy khách với một Destination.
- Bốn bộ định tuyến, mỗi bộ quản lý ba đường hầm vào.
- Tất cả mười hai đường hầm nên được xuất bản trong một LeaseSet duy nhất.

### Đơn máy khách

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]-----
                 |-{ [Tunnel 3]===/               \
                 |                                 \
                 |-{ [Tunnel 4]===\                 \
  [Destination]  |-{ [Tunnel 5]====[Router 2]-----   \
    \            |-{ [Tunnel 6]===/               \   \
     [LeaseSet]--|                               [Client]
                 |-{ [Tunnel 7]===\               /   /
                 |-{ [Tunnel 8]====[Router 3]-----   /
                 |-{ [Tunnel 9]===/                 /
                 |                                 /
                 |-{ [Tunnel 10]==\               /
                 |-{ [Tunnel 11]===[Router 4]-----
                  -{ [Tunnel 12]==/
```

### Đa máy khách

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]---------[Frontend 1]
                 |-{ [Tunnel 3]===/          \                    \
                 |                            \                    \
                 |-{ [Tunnel 4]===\            \                    \
  [Destination]  |-{ [Tunnel 5]====[Router 2]---\-----[Frontend 2]   \
    \            |-{ [Tunnel 6]===/          \   \                \   \
     [LeaseSet]--|                         [Balancer]            [Backend]
                 |-{ [Tunnel 7]===\          /   /                /   /
                 |-{ [Tunnel 8]====[Router 3]---/-----[Frontend 3]   /
                 |-{ [Tunnel 9]===/            /                    /
                 |                            /                    /
                 |-{ [Tunnel 10]==\          /                    /
                 |-{ [Tunnel 11]===[Router 4]---------[Frontend 4]
                  -{ [Tunnel 12]==/
```

### Quy trình máy khách tổng quát

- Tải hoặc tạo một Destination.

- Mở một phiên với mỗi bộ định tuyến, liên kết với Destination.

- Định kỳ (khoảng mỗi mười phút, nhưng có thể nhiều hơn hoặc ít hơn tùy theo trạng thái sống của đường hầm):

  - Lấy danh sách tầng nhanh (fast tier) từ mỗi bộ định tuyến.

  - Sử dụng tập hợp con các máy ngang hàng để xây dựng các đường hầm đến/từ mỗi bộ định tuyến.

    - Theo mặc định, các đường hầm đến/từ một bộ định tuyến cụ thể sẽ sử dụng các máy ngang hàng từ tầng nhanh của bộ định tuyến đó, nhưng điều này không được giao thức bắt buộc.

  - Thu thập tập hợp các đường hầm vào đang hoạt động từ tất cả các bộ định tuyến đang hoạt động, và tạo một LeaseSet.

  - Xuất bản LeaseSet thông qua một hoặc nhiều bộ định tuyến.

### Khác biệt so với I2CP

Để tạo và quản lý cấu hình này, máy khách cần các chức năng mới sau đây vượt quá những gì hiện tại được cung cấp bởi [I2CP](/docs/specs/i2cp/):

- Yêu cầu bộ định tuyến xây dựng đường hầm, mà không tạo LeaseSet cho chúng.
- Lấy danh sách các đường hầm hiện tại trong nhóm đường hầm vào.

Ngoài ra, các chức năng sau đây sẽ cho phép sự linh hoạt đáng kể trong cách máy khách quản lý các đường hầm của nó:

- Lấy nội dung của tầng nhanh (fast tier) của một bộ định tuyến.
- Yêu cầu bộ định tuyến xây dựng một đường hầm vào hoặc ra bằng một danh sách máy ngang hàng đã cho.

### Khung giao thức

```
         Client                           Router

                    --------------------->  Create Session
   Session Status  <---------------------
                    --------------------->  Get Fast Tier
        Peer List  <---------------------
                    --------------------->  Create Tunnel
    Tunnel Status  <---------------------
                    --------------------->  Get Tunnel Pool
      Tunnel List  <---------------------
                    --------------------->  Publish LeaseSet
                    --------------------->  Send Packet
      Send Status  <---------------------
  Packet Received  <---------------------
```

### Các thông điệp

**Create Session**
- Tạo một phiên cho Destination đã cho.

**Session Status**
- Xác nhận rằng phiên đã được thiết lập, và máy khách hiện có thể bắt đầu xây dựng các đường hầm.

**Get Fast Tier**
- Yêu cầu danh sách các máy ngang hàng mà bộ định tuyến hiện tại sẽ xem xét để xây dựng đường hầm.

**Peer List**
- Danh sách các máy ngang hàng mà bộ định tuyến biết đến.

**Create Tunnel**
- Yêu cầu bộ định tuyến xây dựng một đường hầm mới qua các máy ngang hàng đã chỉ định.

**Tunnel Status**
- Kết quả của việc xây dựng một đường hầm cụ thể, khi đã có sẵn.

**Get Tunnel Pool**
- Yêu cầu danh sách các đường hầm hiện tại trong nhóm đường hầm vào hoặc ra cho Destination.

**Tunnel List**
- Danh sách các đường hầm cho nhóm đã yêu cầu.

**Publish LeaseSet**
- Yêu cầu bộ định tuyến xuất bản LeaseSet được cung cấp thông qua một trong các đường hầm ra cho Destination. Không cần trạng thái phản hồi; bộ định tuyến nên tiếp tục thử lại cho đến khi hài lòng rằng LeaseSet đã được xuất bản.

**Send Packet**
- Một gói tin đi ra từ máy khách. Có thể chỉ định một đường hầm ra mà gói tin phải (nên?) được gửi qua.

**Send Status**
- Thông báo cho máy khách về thành công hoặc thất bại khi gửi gói tin.

**Packet Received**
- Một gói tin đến cho máy khách. Có thể chỉ định đường hầm vào mà gói tin đã được nhận qua(?)


## Tác động đến bảo mật

Từ góc nhìn của các bộ định tuyến, thiết kế này về mặt chức năng tương đương với trạng thái hiện tại. Bộ định tuyến vẫn xây dựng tất cả các đường hầm, duy trì hồ sơ máy ngang hàng riêng, và thực thi sự tách biệt giữa các hoạt động của bộ định tuyến và máy khách. Trong cấu hình mặc định, nó hoàn toàn giống nhau, vì các đường hầm cho bộ định tuyến đó được xây dựng từ tầng nhanh của chính nó.

Từ góc nhìn của netDB, một LeaseSet duy nhất được tạo thông qua giao thức này giống hệt với trạng thái hiện tại, vì nó tận dụng chức năng đã tồn tại. Tuy nhiên, đối với các LeaseSet lớn hơn, tiến gần đến 16 Lease, có thể một quan sát viên có thể xác định được rằng LeaseSet đang được đa kết nối:

- Kích thước tối đa hiện tại của tầng nhanh là 75 máy ngang hàng. Cổng vào (IBGW, nút được công bố trong một Lease) được chọn từ một phần của tầng (được phân vùng ngẫu nhiên theo nhóm đường hầm theo băm, không theo số lượng):

      1 hop
          Toàn bộ tầng nhanh

      2 hops
          Một nửa tầng nhanh
          (mặc định cho đến giữa năm 2014)

      3+ hops
          Một phần tư tầng nhanh
          (3 là mặc định hiện tại)

  Điều đó có nghĩa là trung bình các IBGW sẽ đến từ một tập hợp khoảng 20-30 máy ngang hàng.

- Trong cấu hình đơn kết nối, một LeaseSet đầy đủ 16 đường hầm sẽ có 16 IBGW được chọn ngẫu nhiên từ một tập hợp tối đa (giả sử) 20 máy ngang hàng.

- Trong cấu hình đa kết nối 4 bộ định tuyến sử dụng cấu hình mặc định, một LeaseSet đầy đủ 16 đường hầm sẽ có 16 IBGW được chọn ngẫu nhiên từ một tập hợp tối đa 80 máy ngang hàng, mặc dù có thể có một phần các máy ngang hàng chung giữa các bộ định tuyến.

Do đó, với cấu hình mặc định, có thể thông qua phân tích thống kê để xác định rằng LeaseSet đang được tạo bởi giao thức này. Cũng có thể xác định được có bao nhiêu bộ định tuyến, mặc dù tác động của sự thay đổi (churn) trên các tầng nhanh sẽ làm giảm hiệu quả của phân tích này.

Vì máy khách có toàn quyền kiểm soát việc chọn máy ngang hàng nào, rò rỉ thông tin này có thể được giảm thiểu hoặc loại bỏ bằng cách chọn các IBGW từ một tập hợp máy ngang hàng bị thu hẹp.


## Tương thích

Thiết kế này hoàn toàn tương thích ngược với mạng, vì không có thay đổi nào đối với định dạng LeaseSet. Tất cả các bộ định tuyến sẽ cần nhận biết giao thức mới, nhưng điều này không phải là vấn đề vì chúng đều được kiểm soát bởi cùng một thực thể.


## Ghi chú về hiệu suất và khả năng mở rộng

Giới hạn trên 16 Lease mỗi LeaseSet không bị thay đổi bởi đề xuất này. Đối với các Destination yêu cầu nhiều đường hầm hơn, có hai khả năng sửa đổi mạng:

- Tăng giới hạn trên kích thước của LeaseSet. Đây sẽ là cách đơn giản nhất để triển khai (mặc dù vẫn cần hỗ trợ mạng rộng khắp trước khi có thể sử dụng phổ biến), nhưng có thể dẫn đến việc tìm kiếm chậm hơn do kích thước gói tin lớn hơn. Kích thước LeaseSet khả thi tối đa được xác định bởi MTU của các lớp truyền tải bên dưới, do đó khoảng 16kB.

- Triển khai Đề xuất 123 cho các LeaseSet phân tầng. Khi kết hợp với đề xuất này, các Destination cho các sub-LeaseSet có thể được phân tán qua nhiều bộ định tuyến, hiệu quả hoạt động như nhiều địa chỉ IP cho một dịch vụ clearnet.


## Ghi nhận

Cảm ơn psi vì cuộc thảo luận dẫn đến đề xuất này.


## Tài liệu tham khảo

* [Destination](/docs/specs/common-structures/#destination)
* [I2CP](/docs/specs/i2cp/)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [Prop123](/proposals/123-new-netdb-entries/)
