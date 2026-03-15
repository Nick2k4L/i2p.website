---
title: "Giao Thức Garlic Farm"
number: "150"
author: "zzz"
created: "2019-05-02"
lastupdated: "2019-05-20"
status: "Open"
thread: "http://zzz.i2p/topics/2234"
toc: true
---
## Tổng quan

Đây là đặc tả cho giao thức truyền tải Garlic Farm,
dựa trên JRaft, mã "exts" của nó để triển khai qua TCP,
và ứng dụng mẫu "dmprinter" của nó [JRAFT](https://github.com/datatechnology/jraft).


Chúng tôi không thể tìm thấy bất kỳ triển khai nào có giao thức truyền tải được tài liệu hóa.
Tuy nhiên, triển khai JRaft đơn giản đến mức chúng tôi có thể
kiểm tra mã nguồn và sau đó tài liệu hóa giao thức của nó.
Đề xuất này là kết quả của nỗ lực đó.

Đây sẽ là phần nền tảng để điều phối các bộ định tuyến công bố
các mục trong một Meta LeaseSet. Xem đề xuất 123.


## Mục tiêu

- Kích thước mã nhỏ
- Dựa trên triển khai hiện có
- Không sử dụng các đối tượng Java được tuần tự hóa hoặc bất kỳ tính năng hoặc định dạng mã hóa đặc thù nào của Java
- Việc khởi tạo ban đầu nằm ngoài phạm vi. Giả định rằng ít nhất một máy chủ khác
  được ghi cứng hoặc cấu hình ngoài băng thông của giao thức này.
- Hỗ trợ cả các trường hợp sử dụng ngoài băng thông và trong I2P.


## Thiết kế

Giao thức Raft không phải là một giao thức cụ thể; nó chỉ định nghĩa một máy trạng thái.
Do đó, chúng tôi tài liệu hóa giao thức cụ thể của JRaft và xây dựng giao thức của mình dựa trên đó.
Không có thay đổi nào đối với giao thức JRaft ngoài việc thêm
một bước bắt tay xác thực.

Raft bầu chọn một Leader có nhiệm vụ công bố một nhật ký (log).
Nhật ký chứa dữ liệu Cấu hình Raft và dữ liệu Ứng dụng.
Dữ liệu Ứng dụng chứa trạng thái của bộ định tuyến trên mỗi Máy chủ và Địa điểm (Destination)
cho cụm Meta LS2.
Các máy chủ sử dụng một thuật toán chung để xác định người công bố và nội dung
của Meta LS2.
Người công bố Meta LS2 KHÔNG nhất thiết phải là Raft Leader.



## Đặc tả

Giao thức truyền tải được thực hiện qua cổng SSL hoặc cổng I2P không dùng SSL.
Các cổng I2P được chuyển tiếp qua HTTP Proxy.
Không hỗ trợ cổng rõ (clearnet) không dùng SSL.

### Bắt tay và xác thực

Không được JRaft định nghĩa.

Mục tiêu:

- Phương pháp xác thực người dùng/mật khẩu
- Định danh phiên bản
- Định danh cụm
- Có thể mở rộng
- Dễ dàng chuyển tiếp khi dùng cho cổng I2P
- Không tiết lộ không cần thiết máy chủ như một máy chủ Garlic Farm
- Giao thức đơn giản để không cần triển khai đầy đủ máy chủ web
- Tương thích với các tiêu chuẩn phổ biến, để các triển khai có thể sử dụng
  các thư viện chuẩn nếu muốn

Chúng tôi sẽ sử dụng một giao thức bắt tay giống websocket và
xác thực HTTP Digest [RFC 2617](https://tools.ietf.org/html/rfc2617).
Xác thực Cơ bản (Basic) theo RFC 2617 KHÔNG được hỗ trợ.
Khi chuyển tiếp qua HTTP proxy, giao tiếp với
proxy theo như được chỉ định trong [RFC 2616](https://tools.ietf.org/html/rfc2616).

#### Chứng thực

Việc tên người dùng và mật khẩu được áp dụng theo cụm hay
theo máy chủ là tùy thuộc vào triển khai.


#### Yêu cầu HTTP 1

Người khởi tạo sẽ gửi nội dung sau.

Tất cả các dòng đều kết thúc bằng CRLF như yêu cầu của HTTP.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: close
  (any other headers ignored)
  (blank line)

  CLUSTER là tên của cụm (mặc định là "farm")
  VERSION là phiên bản Garlic Farm (hiện tại là "1")

```


#### Phản hồi HTTP 1

Nếu đường dẫn không đúng, người nhận sẽ gửi phản hồi chuẩn "HTTP/1.1 404 Not Found",
như trong [RFC 2616](https://tools.ietf.org/html/rfc2616).

Nếu đường dẫn đúng, người nhận sẽ gửi phản hồi chuẩn "HTTP/1.1 401 Unauthorized",
bao gồm tiêu đề xác thực HTTP digest WWW-Authenticate,
như trong [RFC 2617](https://tools.ietf.org/html/rfc2617).

Cả hai bên sau đó sẽ đóng cổng kết nối.


#### Yêu cầu HTTP 2

Người khởi tạo sẽ gửi nội dung sau,
như trong [RFC 2617](https://tools.ietf.org/html/rfc2617).

Tất cả các dòng đều kết thúc bằng CRLF như yêu cầu của HTTP.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: keep-alive, Upgrade
  Upgrade: websocket
  (Sec-Websocket-* headers if proxied)
  Authorization: (HTTP digest authorization header as in RFC 2617)
  (any other headers ignored)
  (blank line)

  CLUSTER là tên của cụm (mặc định là "farm")
  VERSION là phiên bản Garlic Farm (hiện tại là "1")

```


#### Phản hồi HTTP 2

Nếu xác thực không đúng, người nhận sẽ gửi thêm một phản hồi chuẩn "HTTP/1.1 401 Unauthorized",
như trong [RFC 2617](https://tools.ietf.org/html/rfc2617).

Nếu xác thực đúng, người nhận sẽ gửi phản hồi sau,
như trong giao thức WebSocket.

Tất cả các dòng đều kết thúc bằng CRLF như yêu cầu của HTTP.

```text

HTTP/1.1 101 Switching Protocols
  Connection: Upgrade
  Upgrade: websocket
  (Sec-Websocket-* headers)
  (any other headers ignored)
  (blank line)

```

Sau khi nhận được điều này, cổng kết nối vẫn mở.
Giao thức Raft như được định nghĩa bên dưới bắt đầu, trên cùng một cổng kết nối.


#### Bộ nhớ đệm

Chứng thực phải được lưu vào bộ nhớ đệm ít nhất một giờ, để
các kết nối tiếp theo có thể nhảy trực tiếp đến
"Yêu cầu HTTP 2" ở trên.



### Các loại tin nhắn

Có hai loại tin nhắn: yêu cầu và phản hồi.
Yêu cầu có thể chứa các mục nhật ký (Log Entries), và có kích thước thay đổi;
phản hồi không chứa các mục nhật ký, và có kích thước cố định.

Các loại tin nhắn 1-4 là các tin nhắn RPC tiêu chuẩn do Raft định nghĩa.
Đây là phần cốt lõi của giao thức Raft.

Các loại tin nhắn 5-15 là các tin nhắn RPC mở rộng do
JRaft định nghĩa, để hỗ trợ khách hàng, thay đổi máy chủ động và
đồng bộ nhật ký hiệu quả.

Các loại tin nhắn 16-17 là các tin nhắn RPC nén nhật ký (Log Compaction) được định nghĩa
trong phần 7 của Raft.


| Tin nhắn | Số | Gửi bởi | Gửi đến | Ghi chú |
| :--- | :--- | :--- | :--- | :--- |
| RequestVoteRequest | 1 | Ứng cử viên (Candidate) | Người theo dõi (Follower) | RPC chuẩn của Raft; không được chứa mục nhật ký |
| RequestVoteResponse | 2 | Follower | Candidate | RPC chuẩn của Raft |
| AppendEntriesRequest | 3 | Leader | Follower | RPC chuẩn của Raft |
| AppendEntriesResponse | 4 | Follower | Leader / Client | RPC chuẩn của Raft |
| ClientRequest | 5 | Client | Leader / Follower | Phản hồi là AppendEntriesResponse; chỉ được chứa các mục nhật ký Ứng dụng |
| AddServerRequest | 6 | Client | Leader | Chỉ được chứa một mục nhật ký ClusterServer duy nhất |
| AddServerResponse | 7 | Leader | Client | Leader cũng sẽ gửi một JoinClusterRequest |
| RemoveServerRequest | 8 | Follower | Leader | Chỉ được chứa một mục nhật ký ClusterServer duy nhất |
| RemoveServerResponse | 9 | Leader | Follower | |
| SyncLogRequest | 10 | Leader | Follower | Chỉ được chứa một mục nhật ký LogPack duy nhất |
| SyncLogResponse | 11 | Follower | Leader | |
| JoinClusterRequest | 12 | Leader | Máy chủ mới | Lời mời tham gia; chỉ được chứa một mục nhật ký Cấu hình duy nhất |
| JoinClusterResponse | 13 | Máy chủ mới | Leader | |
| LeaveClusterRequest | 14 | Leader | Follower | Lệnh rời khỏi |
| LeaveClusterResponse | 15 | Follower | Leader | |
| InstallSnapshotRequest | 16 | Leader | Follower | Raft Mục 7; Chỉ được chứa một mục nhật ký SnapshotSyncRequest duy nhất |
| InstallSnapshotResponse | 17 | Follower | Leader | Raft Mục 7 |


### Thiết lập

Sau khi bắt tay HTTP, chuỗi thiết lập như sau:

```text

Máy chủ mới Alice              Người theo dõi ngẫu nhiên Bob

  ClientRequest   ------->
          <---------   AppendEntriesResponse

  Nếu Bob nói rằng nó là leader, tiếp tục như bên dưới.
  Nếu không, Alice phải ngắt kết nối với Bob và kết nối với leader.


  Máy chủ mới Alice              Leader Charlie

  ClientRequest   ------->
          <---------   AppendEntriesResponse
  AddServerRequest   ------->
          <---------   AddServerResponse
          <---------   JoinClusterRequest
  JoinClusterResponse  ------->
          <---------   SyncLogRequest
                       HOẶC InstallSnapshotRequest
  SyncLogResponse  ------->
  HOẶC InstallSnapshotResponse

```

Chuỗi ngắt kết nối:

```text

Follower Alice              Leader Charlie

  RemoveServerRequest   ------->
          <---------   RemoveServerResponse
          <---------   LeaveClusterRequest
  LeaveClusterResponse  ------->

```

Chuỗi bầu cử:

```text

Ứng cử viên Alice               Follower Bob

  RequestVoteRequest   ------->
          <---------   RequestVoteResponse

  nếu Alice thắng bầu cử:

  Leader Alice                Follower Bob

  AppendEntriesRequest   ------->
  (heartbeat)
          <---------   AppendEntriesResponse

```


### Định nghĩa

- Nguồn (Source): Xác định người khởi tạo tin nhắn
- Đích (Destination): Xác định người nhận tin nhắn
- Các kỳ hạn (Terms): Xem Raft. Được khởi tạo bằng 0, tăng đơn điệu
- Chỉ mục (Indexes): Xem Raft. Được khởi tạo bằng 0, tăng đơn điệu



### Yêu cầu

Yêu cầu chứa một tiêu đề và không hoặc nhiều mục nhật ký.
Yêu cầu chứa một tiêu đề kích thước cố định và các Mục nhật ký tùy chọn có kích thước thay đổi.


#### Tiêu đề yêu cầu

Tiêu đề yêu cầu dài 45 byte, như sau.
Tất cả các giá trị đều là số nguyên big-endian không dấu.

```text

Loại tin nhắn:      1 byte
  Nguồn:            ID, số nguyên 4 byte
  Đích:             ID, số nguyên 4 byte
  Kỳ hạn:           Kỳ hạn hiện tại (xem ghi chú), số nguyên 8 byte
  Kỳ hạn nhật ký cuối:     số nguyên 8 byte
  Chỉ mục nhật ký cuối:    số nguyên 8 byte
  Chỉ mục cam kết:      số nguyên 8 byte
  Kích thước mục nhật ký:  Tổng kích thước tính bằng byte, số nguyên 4 byte
  Mục nhật ký:       xem bên dưới, tổng độ dài như đã chỉ định

```


#### Ghi chú

Trong RequestVoteRequest, Term là kỳ hạn của ứng cử viên.
Trong các trường hợp khác, đó là kỳ hạn hiện tại của leader.

Trong AppendEntriesRequest, khi kích thước mục nhật ký bằng 0,
tin nhắn này là tin nhắn heartbeat (giữ kết nối).



#### Mục nhật ký

Nhật ký chứa không hoặc nhiều mục nhật ký.
Mỗi mục nhật ký như sau.
Tất cả các giá trị đều là số nguyên big-endian không dấu.

```text

Kỳ hạn:           số nguyên 8 byte
  Loại giá trị:     1 byte
  Kích thước mục:     Tính bằng byte, số nguyên 4 byte
  Mục:          độ dài như đã chỉ định

```


#### Nội dung nhật ký

Tất cả các giá trị đều là số nguyên big-endian không dấu.

| Loại giá trị nhật ký | Số |
| :--- | :--- |
| Ứng dụng | 1 |
| Cấu hình | 2 |
| ClusterServer | 3 |
| LogPack | 4 |
| SnapshotSyncRequest | 5 |


#### Ứng dụng

Nội dung Ứng dụng được mã hóa UTF-8 theo định dạng [JSON](https://www.json.org/).
Xem phần Lớp Ứng dụng bên dưới.


#### Cấu hình

Được dùng để leader tuần tự hóa một cấu hình cụm mới và sao chép tới các máy ngang hàng.
Chứa không hoặc nhiều cấu hình ClusterServer.


```text

Chỉ mục nhật ký:  số nguyên 8 byte
  Chỉ mục nhật ký cuối:  số nguyên 8 byte
  Dữ liệu ClusterServer cho mỗi máy chủ:
    ID:                số nguyên 4 byte
    Độ dài dữ liệu Endpoint: Tính bằng byte, số nguyên 4 byte
    Dữ liệu Endpoint:     chuỗi ASCII dạng "tcp://localhost:9001", độ dài như đã chỉ định

```


#### ClusterServer

Thông tin cấu hình cho một máy chủ trong cụm.
Chỉ được bao gồm trong tin nhắn AddServerRequest hoặc RemoveServerRequest.

Khi dùng trong tin nhắn AddServerRequest:

```text

ID:                số nguyên 4 byte
  Độ dài dữ liệu Endpoint: Tính bằng byte, số nguyên 4 byte
  Dữ liệu Endpoint:     chuỗi ASCII dạng "tcp://localhost:9001", độ dài như đã chỉ định

```


Khi dùng trong tin nhắn RemoveServerRequest:

```text

ID:                số nguyên 4 byte

```


#### LogPack

Chỉ được bao gồm trong tin nhắn SyncLogRequest.

Nội dung sau được nén bằng gz trước khi truyền:


```text

Độ dài dữ liệu chỉ mục: Tính bằng byte, số nguyên 4 byte
  Độ dài dữ liệu nhật ký:   Tính bằng byte, số nguyên 4 byte
  Dữ liệu chỉ mục:     8 byte cho mỗi chỉ mục, độ dài như đã chỉ định
  Dữ liệu nhật ký:       độ dài như đã chỉ định

```



#### SnapshotSyncRequest

Chỉ được bao gồm trong tin nhắn InstallSnapshotRequest.

```text

Chỉ mục nhật ký cuối:  số nguyên 8 byte
  Kỳ hạn nhật ký cuối:   số nguyên 8 byte
  Độ dài dữ liệu cấu hình: Tính bằng byte, số nguyên 4 byte
  Dữ liệu cấu hình:     độ dài như đã chỉ định
  Offset:          Vị trí dữ liệu trong cơ sở dữ liệu, tính bằng byte, số nguyên 8 byte
  Độ dài dữ liệu:        Tính bằng byte, số nguyên 4 byte
  Dữ liệu:            độ dài như đã chỉ định
  Hoàn tất:         1 nếu xong, 0 nếu chưa xong (1 byte)

```




### Phản hồi

Tất cả phản hồi đều dài 26 byte, như sau.
Tất cả các giá trị đều là số nguyên big-endian không dấu.

```text

Loại tin nhắn:   1 byte
  Nguồn:         ID, số nguyên 4 byte
  Đích:          Thường là ID đích thực (xem ghi chú), số nguyên 4 byte
  Kỳ hạn:           Kỳ hạn hiện tại, số nguyên 8 byte
  Chỉ mục tiếp theo:     Được khởi tạo bằng chỉ mục nhật ký cuối của leader + 1, số nguyên 8 byte
  Được chấp nhận:    1 nếu được chấp nhận, 0 nếu không (xem ghi chú), 1 byte

```


#### Ghi chú

ID Đích thường là ID đích thực cho tin nhắn này.
Tuy nhiên, đối với AppendEntriesResponse, AddServerResponse và RemoveServerResponse,
đó là ID của leader hiện tại.

Trong RequestVoteResponse, Is Accepted là 1 nếu bỏ phiếu cho ứng cử viên (người yêu cầu),
và 0 nếu không bỏ phiếu.


## Lớp Ứng dụng

Mỗi Máy chủ định kỳ đăng dữ liệu Ứng dụng vào nhật ký trong một ClientRequest.
Dữ liệu Ứng dụng chứa trạng thái của bộ định tuyến trên mỗi Máy chủ và Địa điểm (Destination)
cho cụm Meta LS2.
Các máy chủ sử dụng một thuật toán chung để xác định người công bố và nội dung
của Meta LS2.
Máy chủ có trạng thái "tốt nhất" gần đây nhất trong nhật ký là người công bố Meta LS2.
Người công bố Meta LS2 KHÔNG nhất thiết phải là Raft Leader.


### Nội dung dữ liệu Ứng dụng

Nội dung Ứng dụng được mã hóa UTF-8 theo định dạng [JSON](https://json.org/),
để đơn giản và có thể mở rộng.
Đặc tả đầy đủ sẽ được xác định sau.
Mục tiêu là cung cấp đủ dữ liệu để viết một thuật toán xác định bộ định tuyến "tốt nhất"
để công bố Meta LS2, và để người công bố có đủ thông tin để đánh trọng số các Địa điểm trong Meta LS2.
Dữ liệu sẽ chứa cả thống kê bộ định tuyến và Địa điểm.

Dữ liệu có thể tùy chọn chứa dữ liệu cảm biến từ xa về tình trạng sức khỏe của
các máy chủ khác, và khả năng truy xuất Meta LS.
Những dữ liệu này sẽ không được hỗ trợ trong phiên bản đầu tiên.

Dữ liệu có thể tùy chọn chứa thông tin cấu hình do
một khách hàng quản trị đăng.
Những dữ liệu này sẽ không được hỗ trợ trong phiên bản đầu tiên.

Nếu "name: value" được liệt kê, điều đó chỉ định khóa và giá trị bản đồ JSON.
Nếu không, đặc tả sẽ được xác định sau.


Dữ liệu cụm (cấp cao nhất):

- cluster: Tên cụm
- date: Ngày của dữ liệu này (dài, ms kể từ thời điểm gốc)
- id: ID Raft (số nguyên)

Dữ liệu cấu hình (config):

- Bất kỳ tham số cấu hình nào

Trạng thái công bố MetaLS (meta):

- destination: địa điểm metals, mã hóa base64
- lastPublishedLS: nếu có, mã hóa base64 của metals đã công bố gần nhất
- lastPublishedTime: tính bằng ms, hoặc 0 nếu chưa từng
- publishConfig: trạng thái cấu hình người công bố tắt/bật/tự động
- publishing: trạng thái boolean người công bố metals đúng/sai

Dữ liệu bộ định tuyến (router):

- lastPublishedRI: nếu có, mã hóa base64 của thông tin bộ định tuyến đã công bố gần nhất
- uptime: Thời gian hoạt động tính bằng ms
- Độ trễ công việc (Job lag)
- Các đường hầm thăm dò (Exploratory tunnels)
- Các đường hầm tham gia (Participating tunnels)
- Băng thông đã cấu hình
- Băng thông hiện tại

Các Địa điểm (destinations):
Danh sách

Dữ liệu Địa điểm:

- destination: địa điểm, mã hóa base64
- uptime: Thời gian hoạt động tính bằng ms
- Số lượng đường hầm đã cấu hình
- Số lượng đường hầm hiện tại
- Băng thông đã cấu hình
- Băng thông hiện tại
- Số lượng kết nối đã cấu hình
- Số lượng kết nối hiện tại
- Dữ liệu danh sách đen (Blacklist data)

Dữ liệu cảm biến bộ định tuyến từ xa:

- Phiên bản RI gần nhất đã thấy
- Thời gian truy xuất LS
- Dữ liệu kiểm tra kết nối
- Dữ liệu hồ sơ floodfill gần nhất
  cho các khoảng thời gian hôm qua, hôm nay và ngày mai

Dữ liệu cảm biến Địa điểm từ xa:

- Phiên bản LS gần nhất đã thấy
- Thời gian truy xuất LS
- Dữ liệu kiểm tra kết nối
- Dữ liệu hồ sơ floodfill gần nhất
  cho các khoảng thời gian hôm qua, hôm nay và ngày mai

Dữ liệu cảm biến Meta LS:

- Phiên bản gần nhất đã thấy
- Thời gian truy xuất
- Dữ liệu hồ sơ floodfill gần nhất
  cho các khoảng thời gian hôm qua, hôm nay và ngày mai


## Giao diện Quản trị

Sẽ được xác định sau, có thể là một đề xuất riêng.
Không yêu cầu cho phiên bản đầu tiên.

Yêu cầu của một giao diện quản trị:

- Hỗ trợ nhiều địa điểm chính, tức là nhiều cụm ảo (nông trại)
- Cung cấp cái nhìn toàn diện về trạng thái cụm chia sẻ - tất cả các thống kê do các thành viên công bố, ai là leader hiện tại, v.v.
- Khả năng buộc loại bỏ một thành viên hoặc leader khỏi cụm
- Khả năng buộc công bố metaLS (nếu nút hiện tại là người công bố)
- Khả năng loại trừ các băm khỏi metaLS (nếu nút hiện tại là người công bố)
- Chức năng nhập/xuất cấu hình cho triển khai hàng loạt



## Giao diện Bộ định tuyến

Sẽ được xác định sau, có thể là một đề xuất riêng.
i2pcontrol không bắt buộc cho phiên bản đầu tiên và các thay đổi chi tiết sẽ được đưa vào một đề xuất riêng.

Yêu cầu cho API Garlic Farm tới bộ định tuyến (trong-JVM java hoặc i2pcontrol)

- getLocalRouterStatus()
- getLocalLeafHash(Hash masterHash)
- getLocalLeafStatus(Hash leaf)
- getRemoteMeasuredStatus(Hash masterOrLeaf) // có thể không có trong MVP
- publishMetaLS(Hash masterHash, List<MetaLease> contents) // hoặc MetaLeaseSet đã ký? Ai ký?
- stopPublishingMetaLS(Hash masterHash)
- xác thực TBD?


## Cơ sở

Atomix quá lớn và sẽ không cho phép tùy chỉnh để chúng tôi định tuyến
giao thức qua I2P. Ngoài ra, định dạng truyền tải của nó chưa được tài liệu hóa và phụ thuộc
vào việc tuần tự hóa Java.


## Ghi chú



## Vấn đề

- Không có cách nào để một khách hàng biết và kết nối tới một leader chưa biết.
  Chỉ cần thay đổi nhỏ để một Follower gửi Cấu hình như một Mục nhật ký trong AppendEntriesResponse.



## Di chuyển

Không có vấn đề tương thích ngược.


## Tài liệu tham khảo

* [JRAFT](https://github.com/datatechnology/jraft)
* [JSON](https://json.org/)
* [RAFT](/docs/research/ongaro2014-raft.pdf)
* [RFC-2616](https://tools.ietf.org/html/rfc2616)
* [RFC-2617](https://tools.ietf.org/html/rfc2617)
* [WEBSOCKET](https://en.wikipedia.org/wiki/WebSocket)
