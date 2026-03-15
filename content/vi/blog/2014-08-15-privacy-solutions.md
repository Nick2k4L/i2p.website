---
title: "The birth of Privacy Solutions"
date: 2014-08-15
author: "Meeh"
description: "Organization launch"
categories: ["press"]
---
Xin chào tất cả mọi người!

Hôm nay chúng tôi xin thông báo về dự án Privacy Solutions, một tổ chức mới phát triển và duy trì phần mềm I2P. Privacy Solutions bao gồm một số nỗ lực phát triển mới nhằm tăng cường quyền riêng tư, bảo mật và ẩn danh cho người dùng, dựa trên các giao thức và công nghệ I2P.

Các nỗ lực này bao gồm:

1. Gói trình duyệt Abscond.
2. Dự án router i2pd bằng C++.
3. Dự án giám sát mạng I2P "BigBrother".
4. Dự án tiền mã hóa Anoncoin.
5. Dự án tiền mã hóa Monero.

Nguồn tài trợ ban đầu của Privacy Solutions đến từ những người ủng hộ các dự án Anoncoin và Monero. Privacy Solutions là một tổ chức phi lợi nhuận có trụ sở tại Na Uy, đã đăng ký trong hệ thống đăng ký chính phủ Na Uy. (Tương tự như loại hình 501(c)3 tại Mỹ.)

Privacy Solutions dự kiến sẽ xin tài trợ từ chính phủ Na Uy cho nghiên cứu mạng, vì dự án BigBrother (chúng tôi sẽ giải thích rõ hơn về điều này) và các đồng tiền mã hóa dự kiến sử dụng mạng độ trễ thấp làm lớp truyền tải chính. Nghiên cứu của chúng tôi sẽ hỗ trợ các bước tiến trong công nghệ phần mềm về ẩn danh, bảo mật và quyền riêng tư.

Trước tiên, xin nói đôi nét về Gói Trình Duyệt Abscond. Ban đầu đây là dự án một người do Meeh thực hiện, nhưng sau đó bạn bè bắt đầu gửi các bản vá, và dự án hiện đang cố gắng tạo ra trải nghiệm truy cập I2P dễ dàng như Tor với gói trình duyệt của họ. Bản phát hành đầu tiên của chúng tôi không còn xa, chỉ còn một vài tác vụ script gitian cần hoàn thành, bao gồm cả việc thiết lập chuỗi công cụ Apple. Tuy nhiên, chúng tôi sẽ thêm phần giám sát bằng PROCESS_INFORMATION (một cấu trúc C lưu trữ thông tin quan trọng về tiến trình) từ phiên bản Java để kiểm tra I2P trước khi công bố phiên bản ổn định. i2pd cũng sẽ thay thế phiên bản Java khi sẵn sàng, và sẽ không còn lý do gì để đóng gói JRE vào bộ cài nữa. Bạn có thể đọc thêm về Gói Trình Duyệt Abscond tại https://hideme.today/dev

Chúng tôi cũng muốn thông báo về tình trạng hiện tại của i2pd. i2pd hiện đã hỗ trợ streaming hai chiều, cho phép sử dụng không chỉ HTTP mà cả các kênh truyền thông lâu dài. Hỗ trợ IRC tức thì đã được thêm vào. Người dùng i2pd có thể sử dụng nó giống như I2P phiên bản Java để truy cập mạng IRC trên I2P. I2PTunnel là một trong những tính năng chính của mạng I2P, cho phép các ứng dụng không phải I2P giao tiếp một cách minh bạch. Vì vậy, đây là tính năng thiết yếu đối với i2pd và là một trong những mốc phát triển quan trọng.

Cuối cùng, nếu bạn đã quen thuộc với I2P, bạn có lẽ đã biết đến Bigbrother.i2p, một hệ thống đo lường do Meeh tạo ra cách đây hơn một năm. Gần đây chúng tôi nhận thấy rằng Meeh thực tế đã thu thập được 100Gb dữ liệu không trùng lặp từ các nút gửi báo cáo kể từ khi ra mắt ban đầu. Dữ liệu này cũng sẽ được chuyển sang Privacy Solutions và được viết lại với backend NSPOF. Cùng lúc đó, chúng tôi cũng sẽ bắt đầu sử dụng Graphite (http://graphite.wikidot.com/screen-shots). Điều này sẽ cung cấp cho chúng tôi cái nhìn tổng quan tuyệt vời về mạng mà không gây ảnh hưởng đến quyền riêng tư của người dùng cuối. Các client sẽ lọc mọi dữ liệu, chỉ giữ lại quốc gia, mã băm router và tỷ lệ thành công trong việc xây dựng tunnel. Tên dịch vụ này, như thường lệ, là một chút đùa vui từ Meeh.

Chúng tôi đã rút gọn một chút thông tin ở đây, nếu bạn muốn biết thêm chi tiết, vui lòng truy cập https://blog.privacysolutions.no/ Trang web hiện vẫn đang trong quá trình xây dựng và sẽ có thêm nhiều nội dung hơn!

Để biết thêm thông tin, vui lòng liên hệ: press@privacysolutions.no

Trân trọng,

Mikal "Meeh" Villa
