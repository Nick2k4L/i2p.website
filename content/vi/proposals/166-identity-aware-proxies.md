---
title: "Đề xuất I2P #166: Các Loại Tunnel Nhận Biết Danh Tính/Host"
number: "166"
author: "eyedeekay"
created: "2024-05-27"
lastupdated: "2024-08-27"
status: "Mở"
thread: "http://i2pforum.i2p/viewforum.php?f=13"
target: "0.9.65"
toc: true
---
### Đề xuất về loại Túnel HTTP Proxy Nhận diện Máy chủ

Đây là một đề xuất nhằm giải quyết “Vấn đề Danh tính Chung” trong việc sử dụng HTTP-trên-I2P thông thường bằng cách giới thiệu một loại túnel HTTP proxy mới. Loại túnel này có hành vi bổ sung nhằm ngăn chặn hoặc hạn chế khả năng theo dõi do các máy chủ ẩn tiềm ẩn thù địch thực hiện đối với các user-agent (trình duyệt) mục tiêu và chính Ứng dụng Khách I2P.

#### "Vấn đề Danh tính Chung" là gì?

Vấn đề "Danh tính Chung" xảy ra khi một user-agent trên một mạng chồng (overlay network) có địa chỉ mã hóa lại chia sẻ danh tính mã hóa với một user-agent khác. Điều này xảy ra, ví dụ, khi cả Firefox và GNU Wget đều được cấu hình để sử dụng cùng một HTTP Proxy.

Trong trường hợp này, máy chủ có thể thu thập và lưu trữ địa chỉ mã hóa (Destination) được dùng để phản hồi hoạt động. Nó có thể coi đây là một “dấu vân tay” luôn 100% duy nhất, vì nó có nguồn gốc mã hóa. Điều này có nghĩa là khả năng liên kết quan sát được do Vấn đề Danh tính Chung là hoàn hảo.

Nhưng liệu có phải là một vấn đề?
^^^^^^^^^^^^^^^^^^^^

Vấn đề Danh tính Chung trở thành một vấn đề khi các user-agent sử dụng cùng giao thức lại mong muốn tính không liên kết. [Nó lần đầu tiên được đề cập trong bối cảnh HTTP tại chủ đề Reddit này](https://old.reddit.com/r/i2p/comments/579idi/warning_i2p_is_linkablefingerprintable/), với các bình luận đã bị xóa có thể truy cập thông qua [pullpush.io](https://api.pullpush.io/reddit/search/comment/?link_id=579idi). *Lúc đó*, tôi là một trong những người phản hồi tích cực nhất, và *lúc đó* tôi cho rằng vấn đề này nhỏ. Trong 8 năm qua, tình hình và quan điểm của tôi về nó đã thay đổi; tôi hiện tin rằng mối đe dọa từ việc các Destination ác ý liên kết dữ liệu ngày càng tăng đáng kể khi ngày càng có nhiều trang web ở vị trí “xây dựng hồ sơ” cho người dùng cụ thể.

Cuộc tấn công này có ngưỡng tham gia rất thấp. Nó chỉ yêu cầu một máy chủ ẩn vận hành nhiều dịch vụ. Đối với các cuộc tấn công vào các lượt truy cập hiện tại (truy cập nhiều trang cùng lúc), đây là yêu cầu duy nhất. Đối với việc liên kết không cùng thời điểm, một trong các dịch vụ đó phải là dịch vụ lưu trữ “tài khoản” thuộc về một người dùng đơn lẻ bị nhắm mục tiêu theo dõi.

Hiện tại, bất kỳ nhà điều hành dịch vụ nào lưu trữ tài khoản người dùng đều có thể liên kết chúng với hoạt động trên mọi trang web họ kiểm soát bằng cách khai thác Vấn đề Danh tính Chung. Mastodon, Gitlab, hay thậm chí các diễn đàn đơn giản cũng có thể là kẻ tấn công ngụy trang, miễn là họ vận hành nhiều hơn một dịch vụ và có động cơ xây dựng hồ sơ người dùng. Việc giám sát này có thể được thực hiện vì mục đích theo dõi, lợi ích tài chính hoặc vì lý do tình báo. Hiện tại có hàng chục nhà điều hành lớn có thể thực hiện cuộc tấn công này và thu thập dữ liệu có ý nghĩa từ đó. Chúng ta phần lớn tin tưởng họ sẽ không làm điều đó — ít nhất là hiện tại — nhưng những đối tượng không quan tâm đến quan điểm của chúng ta có thể dễ dàng xuất hiện.

Điều này liên quan trực tiếp đến một hình thức cơ bản của việc xây dựng hồ sơ trên mạng rõ (clear web), nơi các tổ chức có thể liên kết các tương tác trên trang web của họ với các tương tác trên các mạng mà họ kiểm soát. Trên I2P, do Destination mã hóa là duy nhất, kỹ thuật này đôi khi còn đáng tin cậy hơn, mặc dù không có thêm sức mạnh từ định vị địa lý.

Vấn đề Danh tính Chung không hữu ích chống lại người dùng chỉ sử dụng I2P để ngụy trang vị trí địa lý. Nó cũng không thể được dùng để phá vỡ định tuyến của I2P. Nó chỉ là một vấn đề quản lý danh tính theo ngữ cảnh.

-  Không thể sử dụng Vấn đề Danh tính Chung để định vị địa lý người dùng I2P.
-  Không thể sử dụng Vấn đề Danh tính Chung để liên kết các phiên I2P nếu chúng không cùng thời điểm.

Tuy nhiên, có thể sử dụng nó để làm suy giảm tính ẩn danh của người dùng I2P trong những hoàn cảnh có lẽ rất phổ biến. Một lý do khiến chúng phổ biến là vì chúng ta khuyến khích sử dụng Firefox, một trình duyệt web hỗ trợ chế độ “Tab”.

-  Luôn *có thể* tạo ra một dấu vân tay từ Vấn đề Danh tính Chung trong *bất kỳ* trình duyệt web nào hỗ trợ yêu cầu tài nguyên bên thứ ba.
-  Việc tắt Javascript **không làm gì cả** để chống lại Vấn đề Danh tính Chung.
-  Nếu có thể thiết lập liên kết giữa các phiên không cùng thời điểm, ví dụ bằng “dấu vân tay trình duyệt” truyền thống, thì Danh tính Chung có thể được áp dụng theo cách bắc cầu, từ đó có thể cho phép chiến lược liên kết không cùng thời điểm.
-  Nếu có thể thiết lập liên kết giữa hoạt động trên mạng rõ và danh tính I2P, ví dụ, nếu mục tiêu đã đăng nhập vào một trang với cả sự hiện diện I2P và mạng rõ ở cả hai phía, Danh tính Chung có thể được áp dụng theo cách bắc cầu, từ đó có thể dẫn đến việc loại bỏ ẩn danh hoàn toàn.

Cách bạn đánh giá mức độ nghiêm trọng của Vấn đề Danh tính Chung khi áp dụng cho HTTP proxy I2P phụ thuộc vào việc bạn (hay nói chính xác hơn, một “người dùng” với kỳ vọng có thể chưa được thông tin đầy đủ) nghĩ rằng “danh tính theo ngữ cảnh” cho ứng dụng nằm ở đâu. Có một vài khả năng:

1. HTTP vừa là Ứng dụng vừa là Danh tính Ngữ cảnh — Đây là cách hoạt động hiện tại. Tất cả các Ứng dụng HTTP đều chia sẻ một danh tính.
2. Tiến trình là Ứng dụng và là Danh tính Ngữ cảnh — Đây là cách hoạt động khi một ứng dụng sử dụng API như SAMv3 hoặc I2CP, nơi ứng dụng tự tạo danh tính và kiểm soát vòng đời của nó.
3. HTTP là Ứng dụng, nhưng Máy chủ (Host) là Danh tính Ngữ cảnh — Đây là mục tiêu của đề xuất này, coi mỗi Máy chủ như một “Ứng dụng Web” tiềm năng và xử lý bề mặt đe dọa tương ứng.

Liệu có thể giải quyết được không?
^^^^^^^^^^^^^^^

Có lẽ không thể tạo một proxy thông minh phản hồi mọi trường hợp có thể làm suy yếu tính ẩn danh của một ứng dụng. Tuy nhiên, có thể xây dựng một proxy thông minh phản hồi một ứng dụng cụ thể có hành vi dự đoán được. Ví dụ, trong các Trình duyệt Web hiện đại, người dùng được kỳ vọng sẽ mở nhiều tab, tương tác với nhiều trang web, được phân biệt bằng tên máy chủ (hostname).

Điều này cho phép chúng ta cải thiện hành vi của HTTP Proxy cho loại user-agent HTTP này bằng cách làm cho hành vi của proxy phù hợp với hành vi của user-agent, bằng cách cấp cho mỗi máy chủ một Destination riêng khi dùng với HTTP Proxy. Thay đổi này khiến việc sử dụng Vấn đề Danh tính Chung để tạo dấu vân tay nhằm liên kết hoạt động của client với 2 máy chủ trở nên không thể, vì 2 máy chủ sẽ không còn chia sẻ cùng một danh tính trả lời.

Mô tả:
^^^^^^^^^^^^

Một HTTP Proxy mới sẽ được tạo và thêm vào Trình quản lý Dịch vụ Ẩn (Hidden Services Manager - I2PTunnel). HTTP Proxy mới sẽ hoạt động như một “bộ đa hợp” (multiplexer) của các I2PSocketManager. Bản thân bộ đa hợp không có destination. Mỗi I2PSocketManager riêng lẻ trở thành một phần của bộ đa hợp sẽ có destination cục bộ riêng và nhóm túnel (tunnel pool) riêng. Các I2PSocketManager được tạo theo yêu cầu bởi bộ đa hợp, trong đó “yêu cầu” là lần truy cập đầu tiên vào một máy chủ mới. Có thể tối ưu hóa việc tạo I2PSocketManager trước khi đưa vào bộ đa hợp bằng cách tạo trước một hoặc nhiều cái và lưu trữ bên ngoài bộ đa hợp. Điều này có thể cải thiện hiệu suất.

Một I2PSocketManager bổ sung, với destination riêng, được thiết lập làm phương tiện cho “Outproxy” đối với bất kỳ trang nào *không* có Destination I2P, ví dụ như bất kỳ trang mạng rõ nào. Điều này về cơ bản khiến mọi việc sử dụng Outproxy trở thành một Danh tính Ngữ cảnh duy nhất, với lưu ý rằng việc cấu hình nhiều Outproxy cho túnel sẽ dẫn đến việc luân chuyển “Sticky” outproxy thông thường, nơi mỗi outproxy chỉ nhận yêu cầu từ một trang duy nhất. Đây *gần như* tương đương với việc tách biệt các proxy HTTP-trên-I2P theo destination trên mạng rõ.

Cân nhắc về tài nguyên:
''''''''''''''''''''''''

HTTP proxy mới yêu cầu tài nguyên bổ sung so với HTTP proxy hiện tại. Nó sẽ:

-  Có thể xây dựng nhiều túnel và I2PSocketManager hơn
-  Xây dựng túnel thường xuyên hơn

Mỗi điều này yêu cầu:

-  Tài nguyên tính toán cục bộ
-  Tài nguyên mạng từ các nút đồng đẳng (peers)

Cài đặt:
'''''''''

Để giảm thiểu tác động của việc sử dụng tài nguyên tăng lên, proxy nên được cấu hình để sử dụng càng ít càng tốt. Các proxy là một phần của bộ đa hợp (không phải proxy cha) nên được cấu hình để:

-  Các I2PSocketManager đa hợp xây dựng 1 túnel vào, 1 túnel ra trong nhóm túnel của chúng
-  Các I2PSocketManager đa hợp mặc định đi qua 3 nút (hops)
-  Đóng socket sau 10 phút không hoạt động
-  Các I2PSocketManager do Bộ đa hợp khởi tạo sẽ chia sẻ vòng đời với Bộ đa hợp. Các túnel đa hợp không bị “hủy bỏ” cho đến khi Bộ đa hợp cha bị hủy.

Sơ đồ:
^^^^^^^^^

Sơ đồ dưới đây biểu diễn hoạt động hiện tại của HTTP proxy, tương ứng với “Khả năng 1.” trong phần “Có phải là vấn đề không”. Như bạn thấy, HTTP proxy tương tác trực tiếp với các trang I2P chỉ bằng một destination. Trong tình huống này, HTTP vừa là ứng dụng vừa là danh tính ngữ cảnh.

```text
**Tình trạng hiện tại: HTTP là Ứng dụng, HTTP là Danh tính Ngữ cảnh**
                                                      __-> Outproxy <-> i2pgit.org
                                                     /
Trình duyệt <-> HTTP Proxy (một Destination)<->I2PSocketManager <---> idk.i2p
                                                     \__-> translate.idk.i2p
                                                      \__-> git.idk.i2p
```

Sơ đồ dưới đây biểu diễn hoạt động của một HTTP proxy nhận diện máy chủ (host-aware), tương ứng với “Khả năng 3.” trong phần “Có phải là vấn đề không”. Trong tình huống này, HTTP là ứng dụng, nhưng Máy chủ (Host) xác định danh tính ngữ cảnh, trong đó mỗi trang I2P tương tác với một HTTP proxy khác nhau, mỗi máy chủ có một destination riêng biệt. Điều này ngăn các nhà điều hành nhiều trang web phân biệt được khi cùng một người đang truy cập nhiều trang mà họ vận hành.

```text
**Sau khi thay đổi: HTTP là Ứng dụng, Máy chủ là Danh tính Ngữ cảnh**
                                                    __-> I2PSocketManager (Destination A - Chỉ dành cho Outproxy) <--> i2pgit.org
                                                   /
Trình duyệt <-> HTTP Proxy Multiplexer (Không có Destination) <---> I2PSocketManager (Destination B) <--> idk.i2p
                                                   \__-> I2PSocketManager (Destination C) <--> translate.idk.i2p
                                                    \__-> I2PSocketManager (Destination C) <--> git.idk.i2p
```

Tình trạng:
^^^^^^^

Một triển khai Java hoạt động của proxy nhận diện máy chủ phù hợp với phiên bản cũ hơn của đề xuất này có sẵn tại nhánh fork của idk: i2p.i2p.2.6.0-browser-proxy-post-keepalive. Liên kết trong phần trích dẫn. Nó đang được sửa đổi mạnh mẽ để chia nhỏ các thay đổi thành các phần nhỏ hơn.

Các triển khai với khả năng khác nhau đã được viết bằng Go sử dụng thư viện SAMv3, có thể hữu ích để nhúng vào các ứng dụng Go khác hoặc cho go-i2p nhưng không phù hợp với Java I2P. Ngoài ra, chúng thiếu hỗ trợ tốt để tương tác với các leaseSet được mã hóa.

Phụ lục: ``i2psocks``
                      

Một cách tiếp cận đơn giản theo hướng ứng dụng để tách biệt các loại client khác là có thể thực hiện mà không cần triển khai loại túnel mới hay thay đổi mã I2P hiện tại, bằng cách kết hợp các công cụ I2PTunnel đã có sẵn và được kiểm thử rộng rãi trong cộng đồng bảo mật. Tuy nhiên, cách tiếp cận này đặt ra một giả định khó khăn, không đúng với HTTP và cũng không đúng với nhiều loại client I2P tiềm năng khác.

Về cơ bản, kịch bản sau sẽ tạo ra một SOCKS5 proxy nhận diện ứng dụng và socksify lệnh nền:

```sh
#! /bin/sh
command_to_proxy="$@"
java -jar ~/i2p/lib/i2ptunnel.jar -wait -e 'sockstunnel 7695'
torsocks --port 7695 $command_to_proxy
```

Phụ lục: ``ví dụ triển khai cuộc tấn công``
                                                  

[Một ví dụ triển khai cuộc tấn công Danh tính Chung lên các HTTP User-Agent](https://github.com/eyedeekay/colluding_sites_attack/) đã tồn tại trong nhiều năm. Một ví dụ bổ sung có sẵn trong thư mục con ``simple-colluder`` của [kho lưu trữ prop166 của idk](https://git.idk.i2p/idk/i2p.host-aware-proxy). Các ví dụ này được thiết kế cố ý để minh họa rằng cuộc tấn công hoạt động và sẽ cần được sửa đổi (dù chỉ là nhỏ) để trở thành một cuộc tấn công thực sự.
