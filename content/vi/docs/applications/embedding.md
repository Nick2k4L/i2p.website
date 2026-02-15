---
title: "Nhúng I2P vào Ứng dụng của Bạn"
description: "Hướng dẫn tích hợp I2P router với ứng dụng của bạn"
slug: "embedding"
lastUpdated: "2023-01"
accurateFor: "2.1.0"
---

## Tổng quan

Trang này nói về việc đóng gói toàn bộ tệp nhị phân I2P router cùng với ứng dụng của bạn. Đây không phải là về việc viết một ứng dụng để hoạt động với I2P (dù là đóng gói hay bên ngoài). Tuy nhiên, nhiều hướng dẫn có thể hữu ích ngay cả khi không đóng gói router.

Nhiều dự án đang tích hợp hoặc đang bàn về việc tích hợp I2P. Điều này rất tuyệt vời nếu được thực hiện đúng cách. Nếu làm sai, nó có thể gây ra tác hại thực sự cho mạng lưới của chúng tôi. I2P router rất phức tạp và việc ẩn đi tất cả sự phức tạp khỏi người dùng có thể là một thách thức. Trang này thảo luận về một số hướng dẫn chung.

Hầu hết các hướng dẫn này áp dụng như nhau cho Java I2P hoặc i2pd. Tuy nhiên, một số hướng dẫn dành riêng cho Java I2P và được ghi chú bên dưới.

### Nói chuyện với chúng tôi

Bắt đầu một cuộc đối thoại. Chúng tôi ở đây để giúp đỡ. Các ứng dụng tích hợp I2P là cơ hội hứa hẹn nhất - và thú vị nhất - để chúng tôi phát triển mạng lưới và cải thiện tính ẩn danh cho mọi người.

### Chọn router của bạn một cách khôn ngoan

Nếu ứng dụng của bạn được viết bằng Java hoặc Scala, đây là lựa chọn dễ dàng - sử dụng Java router. Nếu viết bằng C/C++, chúng tôi khuyến nghị sử dụng i2pd. Việc phát triển i2pcpp đã dừng lại. Đối với các ứng dụng viết bằng ngôn ngữ khác, tốt nhất là sử dụng SAM hoặc BOB hoặc SOCKS và đóng gói Java router như một tiến trình riêng biệt. Một số thông tin sau đây chỉ áp dụng cho Java router.

### Cấp phép

Đảm bảo bạn đáp ứng các yêu cầu giấy phép của phần mềm mà bạn đang đóng gói.

---

## Cấu hình

### Xác minh cấu hình mặc định

Cấu hình mặc định chính xác là rất quan trọng. Hầu hết người dùng sẽ không thay đổi các cài đặt mặc định. Các cài đặt mặc định cho ứng dụng của bạn có thể cần khác với các cài đặt mặc định của router mà bạn đang tích hợp. Hãy ghi đè các cài đặt mặc định của router nếu cần thiết.

Một số cài đặt mặc định quan trọng cần xem xét: Băng thông tối đa, số lượng và độ dài tunnel, số tunnel tham gia tối đa. Phần lớn điều này phụ thuộc vào băng thông dự kiến và mô hình sử dụng của ứng dụng của bạn.

Cấu hình đủ băng thông và tunnel để cho phép người dùng của bạn đóng góp vào mạng lưới. Hãy xem xét việc tắt I2CP bên ngoài, vì có thể bạn không cần nó và nó có thể xung đột với bất kỳ phiên bản I2P nào khác đang chạy. Ngoài ra, hãy xem các cấu hình để tắt việc dừng JVM khi thoát chương trình, chẳng hạn.

### Những Cân nhắc về Lưu lượng Tham gia

Có thể bạn sẽ muốn vô hiệu hóa participating traffic (lưu lượng tham gia). Có một số cách để làm điều này (chế độ ẩn, đặt số tunnel tối đa về 0, đặt băng thông chia sẻ dưới 12 KBytes/giây). Nếu không có participating traffic, bạn không phải lo lắng về việc tắt máy một cách nhẹ nhàng, người dùng của bạn không thấy việc sử dụng băng thông không do họ tạo ra, v.v. Tuy nhiên, có rất nhiều lý do tại sao bạn nên cho phép participating tunnel.

Trước hết, router sẽ không hoạt động tốt nếu không có cơ hội "tích hợp" với mạng lưới, việc này được hỗ trợ rất nhiều bởi những người khác xây dựng tunnel thông qua bạn.

Thứ hai, hơn 90% router trong mạng hiện tại cho phép chuyển tiếp lưu lượng. Đây là cài đặt mặc định trong Java router. Nếu ứng dụng của bạn không định tuyến cho người khác và nó trở nên thực sự phổ biến, thì nó sẽ là một gánh nặng cho mạng, và phá vỡ sự cân bằng mà chúng ta có hiện tại. Nếu nó trở nên thực sự lớn, thì chúng ta sẽ trở thành Tor, và dành thời gian để cầu xin mọi người kích hoạt tính năng chuyển tiếp.

Thứ ba, lưu lượng tham gia là lưu lượng che giấu giúp bảo vệ tính ẩn danh của người dùng.

Chúng tôi khuyến cáo mạnh mẽ không nên tắt tính năng participating traffic theo mặc định. Nếu bạn làm điều này và ứng dụng của bạn trở nên rất phổ biến, nó có thể làm hỏng mạng lưới.

### Tính bền vững

Bạn phải lưu dữ liệu của router (netdb, cấu hình, v.v.) giữa các lần chạy router. I2P không hoạt động tốt nếu bạn phải reseed mỗi khi khởi động, và điều đó tạo ra tải lớn cho các máy chủ reseed của chúng tôi, đồng thời cũng không tốt cho tính ẩn danh. Ngay cả khi bạn đóng gói các router info, I2P cần dữ liệu profile đã lưu để có hiệu suất tốt nhất. Không có tính bền vững, người dùng của bạn sẽ có trải nghiệm khởi động kém.

Có hai khả năng nếu bạn không thể cung cấp tính năng lưu trữ lâu dài. Bất kỳ cách nào trong số này đều sẽ loại bỏ tải trọng của dự án bạn trên các máy chủ reseed của chúng tôi và sẽ cải thiện đáng kể thời gian khởi động.

1) Thiết lập server(s) reseed của riêng bạn để phục vụ nhiều router infos hơn số lượng thông thường trong reseed, ví dụ như vài trăm router infos. Cấu hình router để chỉ sử dụng các server của bạn.

2) Đóng gói từ một đến hai nghìn router info trong trình cài đặt của bạn.

Ngoài ra, hãy trì hoãn hoặc khởi động tunnel theo từng giai đoạn để cho router có cơ hội tích hợp trước khi xây dựng nhiều tunnel.

### Khả năng cấu hình

Cung cấp cho người dùng cách thay đổi cấu hình của các cài đặt quan trọng. Chúng tôi hiểu rằng bạn có thể muốn ẩn phần lớn độ phức tạp của I2P, nhưng điều quan trọng là hiển thị một số cài đặt cơ bản. Ngoài các giá trị mặc định ở trên, một số cài đặt mạng như UPnP, IP/port có thể hữu ích.

### Các Cân nhắc về Floodfill

Trên một thiết lập băng thông nhất định và đáp ứng các tiêu chí hoạt động khác, router của bạn sẽ trở thành floodfill, điều này có thể gây ra sự gia tăng lớn về số kết nối và việc sử dụng bộ nhớ (ít nhất với Java router). Hãy cân nhắc xem điều đó có ổn hay không. Bạn có thể vô hiệu hóa floodfill, nhưng khi đó những người dùng có tốc độ cao nhất sẽ không đóng góp những gì họ có thể. Điều này cũng phụ thuộc vào thời gian hoạt động điển hình của ứng dụng của bạn.

### Reseeding

Quyết định xem bạn có đóng gói router infos hay sử dụng reseed hosts của chúng tôi. Danh sách reseed host của Java nằm trong mã nguồn, vì vậy nếu bạn giữ mã nguồn cập nhật, danh sách host cũng sẽ được cập nhật. Hãy lưu ý về khả năng bị chặn bởi các chính phủ thù địch.

### Sử dụng Shared Clients

Java I2P i2ptunnel hỗ trợ shared clients (khách hàng chia sẻ), nơi các client có thể được cấu hình để sử dụng một pool duy nhất. Nếu bạn cần nhiều client và điều này phù hợp với mục tiêu bảo mật của bạn, hãy cấu hình các client để được chia sẻ.

### Giới Hạn Số Lượng Tunnel

Chỉ định số lượng tunnel một cách rõ ràng với các tùy chọn `inbound.quantity` và `outbound.quantity`. Giá trị mặc định trong Java I2P là 2; giá trị mặc định trong i2pd cao hơn. Chỉ định trong dòng SESSION CREATE sử dụng SAM để có cài đặt nhất quán với cả hai router. Hai tunnel cho mỗi chiều vào/ra là đủ cho hầu hết các ứng dụng băng thông thấp đến trung bình và fanout thấp đến trung bình. Các server và ứng dụng P2P fanout cao có thể cần nhiều hơn. Xem bài đăng diễn đàn này để được hướng dẫn tính toán yêu cầu cho các server và ứng dụng lưu lượng cao.

### Chỉ định SAM SIGNATURE_TYPE

SAM mặc định sử dụng DSA_SHA1 cho các destination, điều này không phải là những gì bạn muốn. Ed25519 (type 7) là lựa chọn đúng đắn. Thêm SIGNATURE_TYPE=7 vào lệnh DEST GENERATE, hoặc vào lệnh SESSION CREATE cho DESTINATION=TRANSIENT.

### Giới hạn phiên SAM

Hầu hết các ứng dụng chỉ cần một phiên SAM. SAM cung cấp khả năng nhanh chóng làm quá tải router cục bộ, hoặc thậm chí toàn bộ mạng, nếu tạo ra một số lượng lớn phiên. Nếu nhiều dịch vụ phụ có thể sử dụng một phiên duy nhất, hãy thiết lập chúng với một phiên PRIMARY và SUBSESSIONS (hiện tại chưa được hỗ trợ trên i2pd). Giới hạn hợp lý cho các phiên là tổng cộng 3 hoặc 4, hoặc có thể lên đến 10 trong những tình huống hiếm gặp. Nếu bạn có nhiều phiên, hãy chắc chắn chỉ định số lượng tunnel thấp cho mỗi phiên, xem phần trên.

Trong hầu như mọi tình huống, bạn không nên yêu cầu một session độc nhất cho mỗi kết nối. Nếu không thiết kế cẩn thận, điều này có thể nhanh chóng gây DDoS cho mạng lưới. Hãy cân nhắc kỹ lưỡng xem liệu các mục tiêu bảo mật của bạn có thực sự cần session độc nhất hay không. Vui lòng tham khảo ý kiến từ các nhà phát triển Java I2P hoặc i2pd trước khi triển khai session theo từng kết nối.

### Giảm Sử Dụng Tài Nguyên Mạng

Lưu ý rằng các tùy chọn này hiện tại không được hỗ trợ trên i2pd. Các tùy chọn này được hỗ trợ thông qua I2CP và SAM (trừ delay-open, chỉ có thể sử dụng qua i2ptunnel). Xem tài liệu I2CP (và đối với delay-open, xem tài liệu cấu hình i2ptunnel) để biết chi tiết.

Hãy xem xét cài đặt các tunnel ứng dụng của bạn để delay-open, reduce-on-idle và/hoặc close-on-idle. Điều này khá đơn giản nếu sử dụng i2ptunnel nhưng bạn sẽ phải tự triển khai một số phần nếu sử dụng I2CP trực tiếp. Xem i2psnark để có mã nguồn giúp giảm số lượng tunnel và sau đó đóng tunnel, ngay cả khi có một số hoạt động DHT chạy nền.

---

## Vòng đời

### Khả năng cập nhật

Có tính năng tự động cập nhật nếu có thể, hoặc ít nhất là thông báo tự động về phiên bản mới. Nỗi lo lớn nhất của chúng tôi là một số lượng lớn router ngoài kia không thể được cập nhật. Chúng tôi có khoảng 6-8 bản phát hành mỗi năm cho Java router, và việc này rất quan trọng đối với sức khỏe của mạng lưới để người dùng luôn cập nhật. Thông thường chúng tôi có hơn 80% mạng lưới sử dụng bản phát hành mới nhất trong vòng 6 tuần sau khi phát hành, và chúng tôi muốn duy trì điều này. Bạn không cần lo lắng về việc vô hiệu hóa chức năng tự động cập nhật tích hợp của router, vì mã đó nằm trong router console, mà có lẽ bạn không đóng gói.

### Triển khai

Hãy có kế hoạch triển khai từ từ. Đừng làm quá tải mạng lưới cùng một lúc. Hiện tại chúng tôi có khoảng 25K người dùng duy nhất mỗi ngày và 40K người dùng duy nhất mỗi tháng. Chúng tôi có thể xử lý tăng trưởng 2-3 lần mỗi năm mà không gặp quá nhiều vấn đề. Nếu bạn dự đoán tốc độ tăng trưởng nhanh hơn thế, HOẶC phân phối băng thông (hoặc phân phối thời gian hoạt động, hoặc bất kỳ đặc điểm quan trọng nào khác) của cơ sở người dùng của bạn khác biệt đáng kể so với cơ sở người dùng hiện tại của chúng tôi, chúng tôi thực sự cần phải thảo luận. Kế hoạch tăng trưởng của bạn càng lớn, thì tất cả những điều khác trong danh sách kiểm tra này càng quan trọng.

### Thiết kế và Khuyến khích Thời gian Hoạt động Lâu dài

Hãy cho người dùng biết rằng I2P hoạt động tốt nhất khi được duy trì chạy liên tục. Có thể mất vài phút sau khi khởi động để nó hoạt động tốt, và thậm chí lâu hơn sau lần cài đặt đầu tiên. Nếu thời gian hoạt động trung bình của bạn ít hơn một giờ, thì I2P có thể không phải là giải pháp phù hợp.

---

## Giao Diện Người Dùng

### Hiển thị Trạng thái

Cung cấp một số dấu hiệu cho người dùng biết rằng các tunnel ứng dụng đã sẵn sàng. Khuyến khích sự kiên nhẫn.

### Tắt Nhẹ Nhàng

Nếu có thể, hãy trì hoãn việc tắt máy cho đến khi các tunnel tham gia của bạn hết hạn. Đừng để người dùng của bạn dễ dàng phá vỡ các tunnel, hoặc ít nhất hãy yêu cầu họ xác nhận.

### Giáo dục và Quyên góp

Sẽ rất tuyệt nếu bạn cung cấp cho người dùng các liên kết để tìm hiểu thêm về I2P và để quyên góp.

### Tùy chọn Router Bên ngoài

Tùy thuộc vào cơ sở người dùng và ứng dụng của bạn, có thể hữu ích khi cung cấp một tùy chọn hoặc gói riêng biệt để sử dụng router bên ngoài.

---

## Các Chủ Đề Khác

### Sử dụng các Dịch vụ Phổ biến khác

Nếu bạn dự định sử dụng hoặc liên kết đến các dịch vụ I2P phổ biến khác (nguồn cấp tin tức, đăng ký hosts.txt, tracker, outproxy, v.v.), hãy đảm bảo rằng bạn không làm quá tải chúng và trao đổi với những người đang vận hành chúng để đảm bảo điều đó là được phép.

### Vấn đề về Thời gian / NTP

Lưu ý: Phần này đề cập đến Java I2P. i2pd không bao gồm SNTP client.

I2P bao gồm một SNTP client. I2P yêu cầu thời gian chính xác để hoạt động. Nó sẽ bù đắp cho đồng hồ hệ thống bị lệch nhưng điều này có thể làm chậm quá trình khởi động. Bạn có thể vô hiệu hóa các truy vấn SNTP của I2P, nhưng điều này không được khuyến khích trừ khi ứng dụng của bạn đảm bảo đồng hồ hệ thống là chính xác.

### Chọn Nội Dung và Cách Thức Đóng Gói

Lưu ý: Phần này chỉ áp dụng cho Java I2P.

Tối thiểu bạn sẽ cần i2p.jar, router.jar, streaming.jar, và mstreaming.jar. Bạn có thể bỏ qua hai jar streaming cho ứng dụng chỉ dùng datagram. Một số ứng dụng có thể cần thêm, ví dụ i2ptunnel.jar hoặc addressbook.jar. Đừng quên jbigi.jar, hoặc một phần của nó cho các nền tảng bạn hỗ trợ, để làm cho crypto nhanh hơn nhiều. Java 7 trở lên là bắt buộc để build. Nếu bạn đang build các gói Debian / Ubuntu, bạn nên yêu cầu gói I2P từ PPA của chúng tôi thay vì đóng gói nó. Bạn gần như chắc chắn không cần susimail, susidns, router console, và i2psnark, chẳng hạn.

Các tệp sau đây nên được bao gồm trong thư mục cài đặt I2P, được chỉ định bằng thuộc tính "i2p.dir.base". Đừng quên thư mục certificates/, cần thiết cho việc reseeding, và blocklist.txt để xác thực IP. Thư mục geoip là tùy chọn, nhưng được khuyến nghị để router có thể đưa ra quyết định dựa trên vị trí địa lý. Nếu bao gồm geoip, hãy đảm bảo đặt tệp GeoLite2-Country.mmdb trong thư mục đó (gunzip nó từ installer/resources/GeoLite2-Country.mmdb.gz). Tệp hosts.txt có thể cần thiết, bạn có thể sửa đổi nó để bao gồm bất kỳ hosts nào mà ứng dụng của bạn sử dụng. Bạn có thể thêm tệp router.config vào thư mục gốc để ghi đè các giá trị mặc định ban đầu. Xem xét và chỉnh sửa hoặc xóa các tệp clients.config và i2ptunnel.config.

Các yêu cầu giấy phép có thể đòi hỏi bạn phải bao gồm tệp LICENSES.txt và thư mục licenses.

- Bạn cũng có thể muốn đóng gói một file hosts.txt.
- Hãy đảm bảo chỉ định bootclasspath nếu bạn đang biên dịch Java I2P cho bản phát hành của mình, thay vì sử dụng các file nhị phân của chúng tôi.

### Các cân nhắc về Android

Lưu ý: Phần này chỉ áp dụng cho Java I2P.

Ứng dụng router Android của chúng tôi có thể được chia sẻ bởi nhiều client. Nếu nó chưa được cài đặt, người dùng sẽ được nhắc nhở khi anh ta khởi động một ứng dụng client.

Một số nhà phát triển đã bày tỏ lo ngại rằng đây là trải nghiệm người dùng kém, và họ muốn tích hợp router vào ứng dụng của mình. Chúng tôi có một thư viện dịch vụ router Android trong lộ trình của mình, có thể giúp việc tích hợp dễ dàng hơn. Cần thêm thông tin.

Nếu bạn cần hỗ trợ, vui lòng liên hệ với chúng tôi.

### Maven jars

Lưu ý: Phần này chỉ áp dụng cho Java I2P.

Chúng tôi có một số lượng hạn chế các jar trên [Maven Central](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22net.i2p%22). Có nhiều trac ticket mà chúng tôi cần giải quyết để cải thiện và mở rộng các jar được phát hành trên Maven Central.

Nếu bạn cần hỗ trợ, vui lòng liên hệ với chúng tôi.

### Các cân nhắc về Datagram (DHT)

Nếu ứng dụng của bạn đang sử dụng I2P datagrams, ví dụ như cho DHT, có rất nhiều tùy chọn nâng cao có sẵn để giảm overhead và tăng độ tin cậy. Điều này có thể mất một chút thời gian và thử nghiệm để hoạt động tốt. Hãy lưu ý về sự đánh đổi giữa kích thước/độ tin cậy. Hãy nói chuyện với chúng tôi để được trợ giúp. Có thể - và được khuyến nghị - sử dụng Datagrams và Streaming trên cùng một Destination. Đừng tạo các Destination riêng biệt cho việc này. Đừng cố gắng lưu trữ dữ liệu không liên quan của bạn trong các DHT mạng hiện có (iMule, bote, bittorrent, và router). Hãy xây dựng DHT của riêng bạn. Nếu bạn đang hardcode các seed nodes, chúng tôi khuyến nghị bạn nên có nhiều node.

### Outproxies

I2P outproxy đến clearnet là một tài nguyên có hạn. Chỉ sử dụng outproxy cho việc duyệt web do người dùng khởi tạo bình thường hoặc lưu lượng hạn chế khác. Đối với bất kỳ mục đích sử dụng nào khác, hãy tham khảo ý kiến và xin phép từ người vận hành outproxy.

### Đồng marketing

Hãy cùng nhau làm việc. Đừng chờ đến khi hoàn thành. Hãy cho chúng tôi biết tên Twitter của bạn và bắt đầu tweet về nó, chúng tôi sẽ đáp lại.

### Phần mềm độc hại

Vui lòng không sử dụng I2P cho mục đích xấu xa. Điều này có thể gây ra tổn hại lớn cho cả mạng lưới và danh tiếng của chúng tôi.

### Tham Gia Cùng Chúng Tôi

Điều này có thể hiển nhiên, nhưng hãy tham gia cộng đồng. Chạy I2P 24/7. Tạo một I2P Site về dự án của bạn. Tham gia IRC #i2p-dev. Đăng bài trên diễn đàn. Lan truyền thông tin. Chúng tôi có thể giúp bạn tìm được người dùng, người thử nghiệm, người dịch thuật, hoặc thậm chí là lập trình viên.

---

## Ví dụ

### Ví dụ Ứng dụng

Bạn có thể muốn cài đặt và thử nghiệm ứng dụng I2P Android, và xem xét mã nguồn của nó, để có ví dụ về một ứng dụng tích hợp sẵn router. Hãy xem những gì chúng tôi hiển thị cho người dùng và những gì chúng tôi ẩn đi. Hãy xem xét state machine mà chúng tôi sử dụng để khởi động và dừng router. Các ví dụ khác bao gồm: Vuze, ứng dụng Nightweb Android, iMule, TAILS, iCloak, và Monero.

### Ví dụ Mã nguồn

Lưu ý: Phần này chỉ áp dụng cho Java I2P.

Không có điều nào ở trên thực sự hướng dẫn bạn cách viết code để đóng gói Java router, vì vậy dưới đây là một ví dụ ngắn gọn.

```java
import java.util.Properties;
import net.i2p.router.Router;

	Properties p = new Properties();
        // add your configuration settings, directories, etc.
        // where to find the I2P installation files
	p.addProperty("i2p.dir.base", baseDir);
        // where to find the I2P data files
	p.addProperty("i2p.dir.config", configDir);
        // bandwidth limits in K bytes per second
	p.addProperty("i2np.inboundKBytesPerSecond", "50");
	p.addProperty("i2np.outboundKBytesPerSecond", "50");
	p.addProperty("router.sharePercentage", "80");
	p.addProperty("foo", "bar");
	Router r = new Router(p);
        // don't call exit() when the router stops
	r.setKillVMOnEnd(false);
	r.runRouter();

	...

	r.shutdownGracefully();
	// will shutdown in 11 minutes or less
```
Đoạn code này dành cho trường hợp ứng dụng của bạn khởi động router, như trong ứng dụng Android của chúng tôi. Bạn cũng có thể để router khởi động ứng dụng thông qua các file clients.config và i2ptunnel.config, cùng với Jetty webapps, như được thực hiện trong các gói Java của chúng tôi. Như thường lệ, quản lý trạng thái là phần khó khăn.

Xem thêm: javadocs của Router.
