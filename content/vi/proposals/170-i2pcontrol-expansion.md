---
title: "i2pcontrol-expansion"
number: "170"
author: "Nick2k4"
created: "2026-05-20"
lastupdated: "2026-05-20"
status: "Mở"
toc: true
---

Tổng quan ========

Đề xuất này công bố thông tin mới cho API i2pcontrol, cho phép linh hoạt hơn. Thông tin này bao gồm: thêm, xóa, truy xuất và sửa đổi sổ địa chỉ và các dịch vụ ẩn. Đề xuất này cũng cung cấp thêm thông tin về router của bạn, chẳng hạn như các peer, tin tức, netdb, và nhiều hơn nữa.

Động lực ==========

Lý do cho đề xuất này là để mang lại sự linh hoạt cao hơn trong API của I2P, cho phép các ứng dụng triển khai và quản lý giao diện quản trị I2P. Việc cung cấp thông tin như vậy cho i2pcontrol cho phép người dùng tạo ra các ứng dụng nâng cao hơn và hỗ trợ tốt hơn cho việc quản lý từ xa.

Thiết kế ======

Khi người dùng tương tác với API i2pcontrol, họ sẽ có thể truy cập các endpoint mới cung cấp thông tin như đã nêu ở trên. Ví dụ, API i2pcontrol sẽ cung cấp các phương thức mới là `TunnelManager` và `AddressBook`, cho phép người dùng nhập các tham số để tạo, xóa, truy xuất và sửa đổi các tunnel và sổ địa chỉ. Ngoài ra, phương thức hiện có `RouterInfo` sẽ có các tham số mới để hiển thị thông tin về router.

Hệ quả về bảo mật =====================

Không có các hệ quả về an ninh bổ sung nào được dự kiến từ đề xuất này, vì thông tin được tiết lộ hiện đã có thể truy cập được thông qua các phương tiện khác. Tuy nhiên, điều quan trọng là phải đảm bảo các cơ chế xác thực và ủy quyền phù hợp được thiết lập để truy cập API i2pcontrol, nhằm ngăn chặn việc truy cập trái phép vào thông tin nhạy cảm hoặc kiểm soát bộ định tuyến.

Đặc tả API & Các phương thức ===========================

Tất cả các yêu cầu đều tuân theo cấu trúc JSON-RPC 2.0:

```json
{
  "jsonrpc": "2.0",
  "method": "MethodName",
  "params": {
    // method-specific parameters
  },
  "id": 1
}
```
Phương thức - RouterInfo -------------------

Bên dưới chứa các tham số mới cho phương thức `RouterInfo` và giá trị mà chúng trả về:

- `i2p.router.news` - trả về tất cả các mục tin tức của router.
- `i2p.router.id` - trả về mã băm của router dưới dạng chuỗi Base64, hoặc `null`.
- `i2p.router.clockskew` - trả về độ lệch trung bình của đồng hồ các peer, hoặc `null`.
- `i2p.router.info` - trả về RouterInfo được serial hóa dưới dạng chuỗi Base64, hoặc `null`.
- `i2p.router.logs` - trả về các thông báo nhật ký router gần đây.
- `i2p.router.logs.clear` - xóa bộ đệm nhật ký router và trả về `"success"`.

- `i2p.router.net.total.received.bytes` - trả về tổng số byte đã nhận kể từ khi khởi động. *(tham khảo từ i2pd)*
- `i2p.router.net.total.sent.bytes` - trả về tổng số byte đã gửi kể từ khi khởi động. *(tham khảo từ i2pd)*
- `i2p.router.net.total.transit.bytes` - trả về tổng số byte chuyển tiếp đã được chuyển tiếp kể từ khi khởi động. *(tham khảo từ i2pd)*
- `i2p.router.net.bw.transit.15s` - trả về băng thông trung bình chuyển tiếp trong 15 giây (byte/giây). *(tham khảo từ i2pd)*

- `i2p.router.net.tunnels.shareratio` - trả về tỷ lệ chia sẻ tunnel.
- `i2p.router.net.tunnels.participating.info` - trả về thông tin các tunnel đang tham gia.
- `i2p.router.net.tunnels.i2ptunnel` - trả về thông tin bộ điều khiển I2PTunnel đã cấu hình (thống kê nhanh của tất cả).
- `i2p.router.net.tunnels.exploratory.inbound` - trả về số lượng tunnel nội tuyến thăm dò.
- `i2p.router.net.tunnels.exploratory.outbound` - trả về số lượng tunnel ngoại tuyến thăm dò.
- `i2p.router.net.tunnels.exploratory.info.list` - trả về danh sách thông tin tunnel thăm dò.
- `i2p.router.net.tunnels.client.inbound` - trả về số lượng tunnel nội tuyến của khách hàng.
- `i2p.router.net.tunnels.client.outbound` - trả về số lượng tunnel ngoại tuyến của khách hàng.
- `i2p.router.net.tunnels.client.info.list` - trả về danh sách thông tin tunnel khách hàng.

- `i2p.router.net.status.v6` - trả về mã trạng thái mạng IPv6. *(tham khảo từ i2pd)*
- `i2p.router.net.error` - trả về mã lỗi mạng IPv4. *(tham khảo từ i2pd)*
- `i2p.router.net.error.v6` - trả về mã lỗi mạng IPv6. *(tham khảo từ i2pd)*
- `i2p.router.net.testing` - trả về giá trị cho biết mạng IPv4 có đang ở trạng thái kiểm thử hay không (0 hoặc 1). *(tham khảo từ i2pd)*
- `i2p.router.net.testing.v6` - trả về giá trị cho biết mạng IPv6 có đang ở trạng thái kiểm thử hay không (0 hoặc 1). *(tham khảo từ i2pd)*

- `i2p.router.net.tunnels.successrate` - trả về tỷ lệ thành công gần đây khi tạo tunnel (%). *(tham khảo từ i2pd)*
- `i2p.router.net.tunnels.totalsuccessrate` - trả về tỷ lệ thành công tổng thể khi tạo tunnel kể từ khi khởi động (%). *(tham khảo từ i2pd)*
- `i2p.router.net.tunnels.queue` - trả về kích thước hàng đợi yêu cầu tạo tunnel. *(tham khảo từ i2pd)*
- `i2p.router.net.tunnels.tbmqueue` - trả về kích thước hàng đợi Tin nhắn Tạo Tunnel (Tunnel Build Message). *(tham khảo từ i2pd)*

- `i2p.router.netdb.peers` - trả về danh sách các mã băm ngang hàng đã biết.
- `i2p.router.netdb.activepeers.info` - trả về dữ liệu RouterInfo đã được serial hóa cho các ngang hàng đang hoạt động.
- `i2p.router.netdb.ntcp.limit` - trả về giới hạn kết nối NTCP.
- `i2p.router.netdb.ssu.limit` - trả về giới hạn kết nối SSU.
- `i2p.router.netdb.bannedpeers` - trả về các ngang hàng bị cấm kèm thông tin cấm.
- `i2p.router.netdb.activepeers.list` - trả về danh sách mã băm ngang hàng đang hoạt động.
- `i2p.router.netdb.peers.list` - trả về danh sách mã băm ngang hàng đã biết.
- `i2p.router.netdb.peers.info` - trả về dữ liệu RouterInfo đã được serial hóa cho các ngang hàng đã biết.
- `i2p.router.netdb.activepeers.stats` - trả về thống kê các ngang hàng đang hoạt động.

- `i2p.router.addressbook.private.list` - trả về các mục trong sổ địa chỉ riêng tư.
- `i2p.router.addressbook.local.list` - trả về các mục trong sổ địa chỉ cục bộ.
- `i2p.router.addressbook.router.list` - trả về các mục trong sổ địa chỉ của router.
- `i2p.router.addressbook.published.list` - trả về các mục trong sổ địa chỉ đã được công bố.
- `i2p.router.addressbook.subscriptions` - trả về đường dẫn tệp đăng ký và các mục trong đó.
- `i2p.router.addressbook.config` - trả về đường dẫn tệp cấu hình sổ địa chỉ và các mục trong đó.

Ví dụ:

```json
{
    "jsonrpc": "2.0",
    "method": "RouterInfo",
    "params": {
        "i2p.router.id": "",
    },
    "id": 1
}
```
Trả về:

```json
{
    "jsonrpc": "2.0",
    "result": "{ data }",
    "id": 1
}
```
Phương thức - Sổ địa chỉ --------------------

Đối với phương thức `AddressBook`, ba tham số/đối số là bắt buộc để xóa và thêm mục vào sổ địa chỉ:

- `Type` - tương ứng với loại sổ địa chỉ:
  - `private`
  - `local`
  - `router`
  - `published`
- `Hostname` - tương ứng với tên máy hoặc tên miền gắn với mục nhập trong sổ địa chỉ.
- `Destination` - tương ứng với đích đến gắn với mục nhập trong sổ địa chỉ.
- `Delete` - tham số này là tùy chọn và được dùng để xóa một mục nhập trong sổ địa chỉ. Nếu tham số này không được cung cấp, phương thức sẽ thêm một mục nhập mới vào sổ địa chỉ.

Ví dụ:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "Type": "private",
    "Hostname": "example.i2p",
    "Destination": "exampleDestinationString",
    "Delete": "" <--- this parameter is optional
  },
  "id": 1
}
```
Trả về:

```json
{
  "jsonrpc": "2.0",
  "success": true or false,        
  "message": "Deleted/Added (hostname) in (address book type) address book" OR "Failed to delete/add (hostname) to (address book type) address book",
  "id": 1
}
```
Để chỉnh sửa AddressBookSubscriptions:

- `SetSubscriptions` - tham số này được dùng để thiết lập các đăng ký cho một mục trong sổ địa chỉ. Tham số này nhận một danh sách các chuỗi ký tự làm đối số.

Ví dụ:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetSubscriptions": ["notbob.i2p", "helloworld.i2p", ...]
  },
  "id": 1
}
```
Trả về:

```json
{
  "jsonrpc": "2.0",
  "success": true,
  "message": "Successfully modified: /path/to/subscriptions.txt"
}
```
Để chỉnh sửa AddressBookConfig:

- `SetConfig` - tham số này được dùng để thiết lập cấu hình cho một mục nhập trong sổ địa chỉ.

Nó nhận một đối tượng JSON làm đối số, trong đó chứa các thiết lập cấu hình.

Các tham số cấu hình có sẵn/thông dụng:

- `subscriptions` - tệp chứa danh sách các URL đăng ký.
- `update_delay` - khoảng thời gian cập nhật tính bằng giờ.
- `published_addressbook` - đường dẫn đến danh bạ đã công khai.
- `router_addressbook` - đường dẫn đến danh bạ của router.
- `local_addressbook` - đường dẫn đến danh bạ cục bộ.
- `private_addressbook` - đường dẫn đến danh bạ riêng tư.
- `proxy_port` - cổng eepProxy.
- `proxy_host` - tên máy chủ eepProxy.
- `should_publish` - xác định có cập nhật danh bạ đã công khai hay không.
- `etags` - tệp chứa các etag của URL đăng ký.
- `last_modified` - tệp chứa dấu thời gian lần sửa đổi cuối cùng của các URL đăng ký.
- `log` - đường dẫn tệp nhật ký.
- `theme` - chủ đề giao diện.

Ví dụ:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetConfig": {
      "subscriptions": "subscriptions.txt",
      "update_delay": "12",
      "published_addressbook": "../eepsite/docroot/hosts.txt",
      "router_addressbook": "hosts.txt",
      "local_addressbook": "../userhosts.txt",
      "private_addressbook": "../privatehosts.txt",
      "proxy_port": "4444",
      "proxy_host": "127.0.0.1",
      "should_publish": "true",
      "etags": "etags.txt",
      "last_modified": "last_modified.txt",
      "log": "log.txt",
      "theme": "light"
    }
  },
  "id": 1
}
```
Trả về:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "success": true,
    "message": "Successfully modified: /path/to/config.txt"
  },
  "id": 1
}
```
Phương thức - TunnelManager --------

Phương thức `TunnelManager` được sử dụng để tạo, chỉnh sửa, lấy, khởi động, dừng, khởi động lại và xóa các bộ điều khiển I2PTunnel.

Các tham số bắt buộc:

- `Name` - tên của tunnel. Đây là định danh của tunnel.
- `Action` - hành động cần thực hiện:
  - `create`.
  - `edit`
  - `get`
  - `start`
  - `stop`
  - `restart`
  - `delete`

Các tham số tùy chọn:

- `All` - boolean, cho biết có áp dụng hành động cho tất cả các tunnel hay không. Tùy chọn này chỉ có hiệu lực với các hành động `start`, `stop` và `restart`.

Các loại tunnel được hỗ trợ cho `create`:

- `client` (máy khách)
- `httpclient` (máy khách HTTP)
- `ircclient` (máy khách IRC)
- `socks` (máy khách SOCKS)
- `socksirc` (máy khách SOCKS-IRC)
- `connectclient` (máy khách kết nối)
- `streamrclient` (máy khách Streamr)

- `server`
- `httpserver`
- `httpbidirserver`
- `ircserver`
- `streamrserver`

Các tham số chung để tạo/sửa các đường hầm:

- `Type` - loại tunnel. Bắt buộc khi `create`.
- `NewName` - tên mới tùy chọn khi chỉnh sửa.
- `Port` - cổng lắng nghe cục bộ.
- `TargetHost` hoặc `Host` - máy chủ đích cho các tunnel máy chủ.
- `TargetPort` - cổng đích cho các tunnel máy chủ.
- `TargetDestination` hoặc `Destination` - đích đến cho các tunnel khách hàng cần chỉ định.
- `StartOnLoad` - giá trị boolean, cho biết tunnel có nên tự khởi động khi tải hay không.
- `Description` - mô tả tunnel.
- `ReachableBy` - giao diện/địa chỉ mà tunnel lắng nghe trên đó.
- `Shared` - giá trị boolean, cho biết tunnel khách hàng có nên được chia sẻ hay không.
- `UseSSL` - giá trị boolean, bật SSL ở những nơi được hỗ trợ.
- `TunnelLength` - độ dài tunnel, từ `0` đến `3`.
- `TunnelVariance` - độ biến thiên tunnel, từ `-2` đến `2`.
- `TunnelQuantity` - số lượng tunnel, từ `1` đến `6`.
- `TunnelBackupQuantity` - số lượng tunnel dự phòng, từ `0` đến `3`.
- `SigType` - loại khóa chữ ký.
- `EncType` - loại mã hóa.
- `CustomOptions` - các tùy chọn tunnel tùy chỉnh.

Tùy chọn proxy của client:

- `ProxyList`
- `UseOutproxyPlugin`
- `ProxyAuth`
- `ProxyUsername`
- `ProxyPassword`
- `OutproxyAuth`
- `OutproxyUsername`
- `OutproxyPassword`
- `OutproxyType`
- `SSLProxies`
- `JumpList`

Tùy chọn quản lý máy khách:

- `ConnectDelay`
- `Profile`
- `DelayOpen`
- `Reduce`
- `ReduceCount`
- `ReduceTime`
- `Close`
- `CloseTime`
- `NewDest`
- `PersistentClientKey`
- `PrivKeyFile`

Tùy chọn lọc client HTTP:

- `AllowUserAgent`
- `AllowReferer`
- `AllowAccept`
- `AllowInternalSSL`

Tùy chọn máy chủ:

- `WebsiteHostname` hoặc `SpoofedHost`
- `BlockAccessInProxies`
- `BlockUserAgents`
- `UserAgents`
- `UniqueLocalAddressPerClient`
- `BlockReferers`
- `MultiHoming`
- `AccessOption`
- `AccessList`
- `FilterFilePath`
- `MaxConcurrentConns`
- `ClientPerMinute`
- `ClientPerHour`
- `ClientPerDay`
- `TotalInPerMinute`
- `TotalInPerHour`
- `TotalInPerDay`
- `PostLimit`
- `PostLimitTime`
- `PerClientPeriod`
- `TotalPeriod`
- `TotalBanTime`

Tùy chọn LeaseSet:

- `EncryptLeaseSet` - một trong các tùy chọn:
  - `disable`
  - `encrypted (aes)`
  - `blinded`
  - `blinded with lookup password`
  - `encrypted (psk)`
  - `encrypted with lookup password (psk)`
  - `encrypted with per-user key (psk)`
  - `encrypted with lookup password and per-user key (psk)`
  - `encrypted with per-user key (dh)`
  - `encrypted with lookup password and per-user key (dh)`
- `OptionalLookup`
- `LeaseSetClientAuths`

Tạo ví dụ:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "create",
    "Type": "client",
    "Port": 7656,
    "TargetDestination": "exampleDestinationString",
    "StartOnLoad": false,
    ....
  },
  "id": 1
}
```
Trả về:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - created tunnel example-client" OR "error - { error message }",
    "results": [ {/* information about where persistent keys are stored */} ]
  },
  "id": 1
}
```
Ví dụ chỉnh sửa:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "edit",
    "NewName": "renamed-client",
    "Port": 7657,
    "TargetDestination": "newDestinationString",
    "StartOnLoad": true
  },
  "id": 1
}
```
Trả về:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - edited tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
Lấy ví dụ:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "get"
  },
  "id": 1
}
```
Trả về:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - options for example-client" OR "error - { error message }",
    "info": {
      "client": true,
      "status": "running",
      "persistentClientKey": false,
      "offlineKeys": false,
      "targetDestination": "exampleDestinationString",
      "localDestination": "exampleBase64Destination",
      "destination": "exampleBase64Destination",
      "destinationB32": "example.b32.i2p",
      "rawConfig": {
        "name": "example-client",
        "type": "client"
      }
    }
  },
  "id": 1
}
```
Ví dụ về Bắt đầu, Dừng, Khởi động lại, Xóa. Chúng có cùng cấu trúc, chỉ khác nhau ở tham số `Action`:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "start"
  },
  "id": 1
}
```
Trả về:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - starting tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
Phương thức - ClientServicesInfo *(được áp dụng từ i2pd)* -------------------------------------------------

Phương thức `ClientServicesInfo` trả về thông tin trạng thái về các dịch vụ khách đang chạy trên router. Hãy đưa các khóa dịch vụ mong muốn (kèm bất kỳ giá trị nào) vào `params` để yêu cầu trạng thái của từng dịch vụ.

Các tham số được hỗ trợ:

- `I2PTunnel` - trả về bản đồ các tên tunnel đã cấu hình cùng địa chỉ tương ứng, được chia thành các đối tượng con `client` và `server`.
- `HTTPProxy` - trả về trạng thái bật/tắt và địa chỉ của proxy HTTP.
- `SOCKS` - trả về trạng thái bật/tắt và địa chỉ của proxy SOCKS.
- `SAM` - trả về trạng thái bật/tắt của cầu nối SAM và thông tin các phiên đang hoạt động.
- `BOB` - trả về trạng thái bật/tắt của cầu nối BOB. (Đã bị loại bỏ trong Java I2P; luôn trả về `false`.)
- `I2CP` - trả về trạng thái bật/tắt của máy chủ I2CP.

Ví dụ:

```json
{
  "jsonrpc": "2.0",
  "method": "ClientServicesInfo",
  "params": {
    "I2PTunnel": "",
    "SAM": ""
  },
  "id": 1
}
```
Trả về:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "I2PTunnel": {
      "client": {"my-client": {"address": "example.b32.i2p"}},
      "server": {"my-server": {"address": "example.b32.i2p", "port": 8080}}
    },
    "SAM": {
      "enabled": true,
      "sessions": {}
    }
  },
  "id": 1
}
```
Tương thích =============

Việc tương thích với API i2pcontrol hiện có cần được duy trì, vì các phương thức và tham số mới được thêm vào theo cách không làm ảnh hưởng đến chức năng hiện tại. Các ứng dụng hiện có sử dụng API i2pcontrol vẫn phải tiếp tục hoạt động mà không cần thay đổi, trong khi các ứng dụng mới có thể tận dụng thông tin và khả năng bổ sung do đề xuất này cung cấp.

Triển khai ==============

Java I2P --------

Đề xuất này hiện chưa được triển khai trong Java I2P, tuy nhiên mã nguồn đã có sẵn trong kho lưu trữ [i2p.plugins.i2pcontrol](https://github.com/i2p/i2p.plugins.i2pcontrol) dưới dạng yêu cầu kéo [#6](https://github.com/i2p/i2p.plugins.i2pcontrol/pull/6). Việc này được thực hiện nhằm cho phép kiểm thử và phát triển các phương thức mới mà không ảnh hưởng đến mã nguồn hiện tại. Khi mã nguồn đã sẵn sàng để sử dụng trong môi trường sản xuất, nó sẽ được cập nhật vào kho I2P chính trong thư mục i2pcontrol.

i2pd ----

Các phương thức và tham số được đánh dấu là "(tham khảo từ i2pd)" đã được triển khai trong i2pd và không thay đổi trong đề xuất này. Các phần mở rộng của i2pd sẽ không cần sửa đổi như một phần của đề xuất này. Các phần không được đánh dấu trong đề xuất này chưa được triển khai trong i2pd.

go-i2p ------

go-i2p có động lực theo đuổi đề xuất này để có thể kích hoạt và cải thiện ứng dụng bảng điều khiển router của nó. Nó sẽ áp dụng và triển khai đề xuất này trong tương lai.

emissary --------

Khả năng áp dụng trong Emissary hiện tại chưa xác định, tuy nhiên Emissary có khả năng được hưởng lợi từ đề xuất này theo những cách tương tự như go-i2p.

Hiệu suất ===========

Không dự kiến ảnh hưởng đến hiệu suất.
