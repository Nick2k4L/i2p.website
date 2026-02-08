---
title: "Cài đặt I2P trên macOS"
description: "Hướng dẫn từng bước để cài đặt thủ công I2P và các phụ thuộc của nó trên macOS"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

## Những Gì Bạn Cần

- Máy Mac chạy macOS 10.14 (Mojave) trở lên
- Quyền quản trị viên để cài đặt ứng dụng
- Khoảng 15-20 phút
- Kết nối Internet để tải xuống bộ cài đặt

## Tổng quan

Quá trình cài đặt này có bốn bước chính:

1. **Cài đặt Java** - Tải xuống và cài đặt Oracle Java Runtime Environment
2. **Cài đặt I2P** - Tải xuống và chạy trình cài đặt I2P
3. **Cấu hình Ứng dụng I2P** - Thiết lập trình khởi chạy và thêm vào dock của bạn
4. **Cấu hình Băng thông I2P** - Chạy trình hướng dẫn thiết lập để tối ưu hóa kết nối của bạn

## Phần Một: Cài đặt Java

I2P yêu cầu Java để chạy. Nếu bạn đã cài đặt Java 8 hoặc phiên bản mới hơn, bạn có thể [chuyển đến Phần Hai](#part-two-download-and-install-i2p).

### Bước 1: Tải xuống Java

Truy cập [trang tải xuống Oracle Java](https://www.oracle.com/java/technologies/downloads/) và tải xuống trình cài đặt macOS cho Java 8 hoặc phiên bản mới hơn.

![Tải xuống Oracle Java cho macOS](/images/guides/macos-install/0-jre.png)

### Bước 2: Chạy Trình Cài Đặt

Tìm tệp `.dmg` đã tải xuống trong thư mục Downloads của bạn và nhấp đúp để mở nó.

![Mở trình cài đặt Java](/images/guides/macos-install/1-jre.png)

### Bước 3: Cho phép Cài đặt

macOS có thể hiển thị thông báo bảo mật vì trình cài đặt đến từ một nhà phát triển đã được xác định. Nhấp vào **Mở** để tiếp tục.

![Cấp quyền cho trình cài đặt để tiếp tục](/images/guides/macos-install/2-jre.png)

### Bước 4: Cài đặt Java

Nhấp vào **Install** để bắt đầu quá trình cài đặt Java.

![Bắt đầu cài đặt Java](/images/guides/macos-install/3-jre.png)

### Bước 5: Chờ Cài Đặt

Trình cài đặt sẽ sao chép các tệp và cấu hình Java trên hệ thống của bạn. Quá trình này thường mất 1-2 phút.

![Đợi trình cài đặt hoàn thành](/images/guides/macos-install/4-jre.png)

### Bước 6: Hoàn tất cài đặt

Khi bạn thấy thông báo thành công, Java đã được cài đặt! Nhấp **Đóng** để hoàn tất.

![Cài đặt Java hoàn tất](/images/guides/macos-install/5-jre.png)

## Phần Hai: Tải xuống và Cài đặt I2P

Bây giờ Java đã được cài đặt, bạn có thể cài đặt I2P router.

### Bước 1: Tải xuống I2P

Truy cập [trang Tải xuống](/downloads/) và tải xuống bộ cài đặt **I2P for Unix/Linux/BSD/Solaris** (tệp `.jar`).

![Tải xuống trình cài đặt I2P](/images/guides/macos-install/0-i2p.png)

### Bước 2: Chạy Trình Cài Đặt

Nhấp đúp vào tệp `i2pinstall_X.X.X.jar` đã tải về. Trình cài đặt sẽ khởi chạy và yêu cầu bạn chọn ngôn ngữ ưa thích.

![Chọn ngôn ngữ của bạn](/images/guides/macos-install/1-i2p.png)

### Bước 3: Màn hình Chào mừng

Đọc thông báo chào mừng và nhấp **Next** để tiếp tục.

![Giới thiệu trình cài đặt](/images/guides/macos-install/2-i2p.png)

### Bước 4: Thông báo quan trọng

Trình cài đặt sẽ hiển thị thông báo quan trọng về cập nhật. Các bản cập nhật I2P được **ký số từ đầu đến cuối** và được xác minh, mặc dù bản thân trình cài đặt này không được ký số. Nhấp **Next**.

![Thông báo quan trọng về cập nhật](/images/guides/macos-install/3-i2p.png)

### Bước 5: Thỏa thuận Giấy phép

Đọc thỏa thuận cấp phép I2P (giấy phép kiểu BSD). Nhấp **Next** để chấp nhận.

![License agreement](/images/guides/macos-install/4-i2p.png)

### Bước 6: Chọn Thư mục Cài đặt

Chọn nơi cài đặt I2P. Vị trí mặc định (`/Applications/i2p`) được khuyến nghị. Nhấp **Next**.

![Chọn thư mục cài đặt](/images/guides/macos-install/5-i2p.png)

### Bước 7: Chọn Thành phần

Để tất cả các thành phần được chọn cho việc cài đặt hoàn chỉnh. Nhấp **Next**.

![Chọn các thành phần cần cài đặt](/images/guides/macos-install/6-i2p.png)

### Bước 8: Bắt đầu Cài đặt

Xem lại các lựa chọn của bạn và nhấp **Next** để bắt đầu cài đặt I2P.

![Bắt đầu cài đặt](/images/guides/macos-install/7-i2p.png)

### Bước 9: Cài đặt Files

Trình cài đặt sẽ sao chép các tệp I2P vào hệ thống của bạn. Quá trình này mất khoảng 1-2 phút.

![Đang cài đặt](/images/guides/macos-install/8-i2p.png)

### Bước 10: Tạo Scripts Khởi Chạy

Trình cài đặt tạo ra các script khởi chạy để bắt đầu I2P.

![Tạo scripts khởi chạy](/images/guides/macos-install/9-i2p.png)

### Bước 11: Phím Tắt Cài Đặt

Trình cài đặt sẽ đề xuất tạo các shortcut trên desktop và mục trong menu. Hãy lựa chọn và nhấp **Next**.

![Tạo shortcuts](/images/guides/macos-install/10-i2p.png)

### Bước 12: Hoàn tất cài đặt

Thành công! I2P đã được cài đặt. Nhấp **Done** để hoàn tất.

![Cài đặt hoàn tất](/images/guides/macos-install/11-i2p.png)

## Phần Ba: Cấu hình Ứng dụng I2P

Bây giờ hãy làm cho I2P dễ khởi chạy bằng cách thêm nó vào thư mục Applications và Dock của bạn.

### Bước 1: Mở thư mục Applications

Mở Finder và điều hướng đến thư mục **Applications** của bạn.

![Mở thư mục Applications](/images/guides/macos-install/0-conf.png)

### Bước 2: Tìm I2P Launcher

Tìm thư mục **I2P** hoặc ứng dụng **Start I2P Router** bên trong `/Applications/i2p/`.

![Tìm trình khởi chạy I2P](/images/guides/macos-install/1-conf.png)

### Bước 3: Thêm vào Dock

Kéo ứng dụng **Start I2P Router** vào Dock để truy cập dễ dàng. Bạn cũng có thể tạo một alias trên desktop.

![Thêm I2P vào Dock của bạn](/images/guides/macos-install/2-conf.png)

**Mẹo**: Nhấp chuột phải vào biểu tượng I2P trong Dock và chọn **Options → Keep in Dock** để giữ nó vĩnh viễn.

## Phần Bốn: Cấu hình Băng thông I2P

Khi bạn khởi chạy I2P lần đầu tiên, bạn sẽ được hướng dẫn qua trình thiết lập để cấu hình cài đặt băng thông. Điều này giúp tối ưu hóa hiệu suất của I2P cho kết nối của bạn.

### Bước 1: Khởi chạy I2P

Nhấp vào biểu tượng I2P trong Dock của bạn (hoặc nhấp đúp vào trình khởi chạy). Trình duyệt web mặc định của bạn sẽ mở ra trang I2P Router Console.

![Màn hình chào mừng I2P Router Console](/images/guides/macos-install/0-wiz.png)

### Bước 2: Trình hướng dẫn chào mừng

Trình hướng dẫn thiết lập sẽ chào bạn. Nhấp **Next** để bắt đầu cấu hình I2P.

![Giới thiệu trình hướng dẫn cài đặt](/images/guides/macos-install/1-wiz.png)

### Bước 3: Ngôn ngữ và Giao diện

Chọn **ngôn ngữ giao diện** ưa thích của bạn và chọn giữa chủ đề **sáng** hoặc **tối**. Nhấp **Tiếp theo**.

![Chọn ngôn ngữ và giao diện](/images/guides/macos-install/2-wiz.png)

### Bước 4: Thông tin Kiểm tra Băng thông

Trình hướng dẫn sẽ giải thích về bài kiểm tra băng thông. Bài kiểm tra này kết nối đến dịch vụ **M-Lab** để đo tốc độ internet của bạn. Nhấp **Tiếp theo** để tiếp tục.

![Giải thích kiểm tra băng thông](/images/guides/macos-install/3-wiz.png)

### Bước 5: Chạy Kiểm tra Băng thông

Nhấp **Chạy Kiểm Tra** để đo tốc độ tải lên và tải xuống của bạn. Kiểm tra mất khoảng 30-60 giây.

![Chạy kiểm tra băng thông](/images/guides/macos-install/4-wiz.png)

### Bước 6: Kết Quả Kiểm Tra

Xem lại kết quả kiểm tra của bạn. I2P sẽ đề xuất cài đặt băng thông dựa trên tốc độ kết nối của bạn.

![Kết quả kiểm tra băng thông](/images/guides/macos-install/5-wiz.png)

### Bước 7: Cấu hình Chia sẻ Băng thông

Chọn lượng băng thông bạn muốn chia sẻ với mạng I2P:

- **Tự động** (Khuyến nghị): I2P quản lý băng thông dựa trên việc sử dụng của bạn
- **Giới hạn**: Đặt giới hạn cụ thể cho tải lên/tải xuống
- **Không giới hạn**: Chia sẻ càng nhiều càng tốt (dành cho kết nối tốc độ cao)

Nhấp **Tiếp theo** để lưu cài đặt của bạn.

![Cấu hình chia sẻ băng thông](/images/guides/macos-install/6-wiz.png)

### Bước 8: Hoàn thành cấu hình

Router I2P của bạn hiện đã được cấu hình và đang chạy! Bảng điều khiển router sẽ hiển thị trạng thái kết nối của bạn và cho phép bạn duyệt các trang web I2P.

## Bắt đầu với I2P

Bây giờ khi I2P đã được cài đặt và cấu hình, bạn có thể:

1. **Duyệt các trang web I2P**: Truy cập [trang chủ I2P](http://127.0.0.1:7657/home) để xem các liên kết đến các dịch vụ I2P phổ biến
2. **Cấu hình trình duyệt của bạn**: Thiết lập một [hồ sơ trình duyệt](/docs/guides/browser-config) để truy cập các trang web `.i2p`
3. **Khám phá các dịch vụ**: Tìm hiểu email I2P, diễn đàn, chia sẻ tệp và nhiều hơn nữa
4. **Giám sát router của bạn**: [Console](http://127.0.0.1:7657/console) hiển thị trạng thái mạng và thống kê của bạn

### Liên kết hữu ích

- **Router Console**: [http://127.0.0.1:7657/](http://127.0.0.1:7657/)
- **Cấu hình**: [http://127.0.0.1:7657/config](http://127.0.0.1:7657/config)
- **Sổ địa chỉ**: [http://127.0.0.1:7657/susidns/addressbook](http://127.0.0.1:7657/susidns/addressbook)
- **Cài đặt băng thông**: [http://127.0.0.1:7657/config](http://127.0.0.1:7657/config)

## Chạy lại Trình hướng dẫn Thiết lập

Nếu bạn muốn thay đổi cài đặt băng thông hoặc cấu hình lại I2P sau này, bạn có thể chạy lại trình hướng dẫn chào mừng từ Router Console:

1. Truy cập [I2P Setup Wizard](http://127.0.0.1:7657/welcome)
2. Thực hiện lại các bước của wizard

## Xử lý sự cố

### I2P Không Khởi Động Được

- **Kiểm tra Java**: Đảm bảo Java đã được cài đặt bằng cách chạy `java -version` trong Terminal
- **Kiểm tra quyền truy cập**: Đảm bảo thư mục I2P có quyền truy cập chính xác
- **Kiểm tra logs**: Xem `~/.i2p/wrapper.log` để tìm thông báo lỗi

### Trình duyệt không thể truy cập các trang I2P

- Đảm bảo I2P đang chạy (kiểm tra Router Console)
- Cấu hình cài đặt proxy của trình duyệt để sử dụng HTTP proxy `127.0.0.1:4444`
- Đợi 5-10 phút sau khi khởi động để I2P tích hợp vào mạng lưới

### Hiệu suất chậm

- Chạy lại bài kiểm tra băng thông và điều chỉnh cài đặt của bạn
- Đảm bảo bạn đang chia sẻ một phần băng thông với mạng
- Kiểm tra trạng thái kết nối trong Router Console

## Gỡ cài đặt I2P

Để gỡ bỏ I2P khỏi Mac của bạn:

1. Thoát khỏi I2P router nếu nó đang chạy
2. Xóa thư mục `/Applications/i2p`
3. Xóa thư mục `~/.i2p` (cấu hình và dữ liệu I2P của bạn)
4. Gỡ bỏ biểu tượng I2P khỏi Dock của bạn

## Các Bước Tiếp Theo

- **Tham gia cộng đồng**: Truy cập [i2pforum.net](http://i2pforum.net) hoặc xem I2P trên Reddit
- **Tìm hiểu thêm**: Đọc [tài liệu I2P](/en/docs) để hiểu cách mạng lưới hoạt động
- **Tham gia đóng góp**: Cân nhắc [đóng góp cho I2P](/en/get-involved) trong việc phát triển hoặc vận hành hạ tầng

Chúc mừng! Bạn đã trở thành một phần của mạng I2P. Chào mừng đến với internet vô hình!

---
