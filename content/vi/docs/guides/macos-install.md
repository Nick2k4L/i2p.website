---
title: "Cài đặt I2P trên macOS"
description: "Hướng dẫn từng bước để cài đặt thủ công I2P và các phụ thuộc của nó trên macOS"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

## Những Gì Bạn Cần

- Máy Mac chạy macOS 10.14 (Mojave) hoặc mới hơn
- Quyền quản trị viên để cài đặt ứng dụng
- Khoảng 15-20 phút
- Kết nối internet để tải xuống các trình cài đặt

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

### Bước 2: Chạy trình cài đặt

Tìm tệp `.dmg` đã tải xuống trong thư mục Downloads và nhấp đúp để mở nó.

![Mở trình cài đặt Java](/images/guides/macos-install/1-jre.png)

### Bước 3: Cho phép cài đặt

macOS có thể hiển thị thông báo bảo mật vì trình cài đặt đến từ một nhà phát triển đã được xác định. Nhấp **Mở** để tiếp tục.

![Cấp quyền cho trình cài đặt để tiếp tục](/images/guides/macos-install/2-jre.png)

### Bước 4: Cài đặt Java

Nhấn **Install** để bắt đầu quá trình cài đặt Java.

![Bắt đầu cài đặt Java](/images/guides/macos-install/3-jre.png)

### Bước 5: Chờ Cài Đặt

Trình cài đặt sẽ sao chép các tệp và cấu hình Java trên hệ thống của bạn. Quá trình này thường mất 1-2 phút.

![Đợi quá trình cài đặt hoàn tất](/images/guides/macos-install/4-jre.png)

### Bước 6: Hoàn tất cài đặt

Khi bạn thấy thông báo thành công, Java đã được cài đặt! Nhấp **Đóng** để hoàn tất.

![Cài đặt Java hoàn tất](/images/guides/macos-install/5-jre.png)

## Phần Hai: Tải xuống và Cài đặt I2P

Bây giờ Java đã được cài đặt, bạn có thể cài đặt I2P router.

### Bước 1: Tải xuống I2P

Truy cập [trang Tải xuống](/downloads/) và tải về trình cài đặt **I2P for Unix/Linux/BSD/Solaris** (tệp `.jar`).

![Tải xuống trình cài đặt I2P](/images/guides/macos-install/0-i2p.png)

### Bước 2: Chạy Trình Cài Đặt

Nhấp đúp vào tệp `i2pinstall_X.X.X.jar` đã tải xuống. Trình cài đặt sẽ khởi động và yêu cầu bạn chọn ngôn ngữ ưa thích.

![Chọn ngôn ngữ của bạn](/images/guides/macos-install/1-i2p.png)

### Bước 3: Màn hình Chào mừng

Đọc thông điệp chào mừng và nhấp **Next** để tiếp tục.

![Installer introduction](/images/guides/macos-install/2-i2p.png)

### Bước 4: Thông Báo Quan Trọng

Trình cài đặt sẽ hiển thị một thông báo quan trọng về việc cập nhật. Các bản cập nhật I2P được **ký và xác minh end-to-end**, mặc dù chính trình cài đặt này không được ký. Nhấp **Next**.

![Important notice about updates](/images/guides/macos-install/3-i2p.png)

### Bước 5: Thỏa thuận Giấy phép

Đọc thỏa thuận giấy phép I2P (giấy phép kiểu BSD). Nhấp **Tiếp theo** để chấp nhận.

![Thỏa thuận cấp phép](/images/guides/macos-install/4-i2p.png)

### Bước 6: Chọn Thư mục Cài đặt

Chọn nơi cài đặt I2P. Vị trí mặc định (`/Applications/i2p`) được khuyến nghị. Nhấp **Next**.

![Chọn thư mục cài đặt](/images/guides/macos-install/5-i2p.png)

### Bước 7: Chọn Thành phần

Để tất cả các thành phần được chọn cho một cài đặt hoàn chỉnh. Nhấp **Next**.

![Chọn các thành phần để cài đặt](/images/guides/macos-install/6-i2p.png)

### Bước 8: Bắt đầu cài đặt

Xem lại các lựa chọn của bạn và nhấp **Next** để bắt đầu cài đặt I2P.

![Bắt đầu cài đặt](/images/guides/macos-install/7-i2p.png)

### Bước 9: Cài đặt Tệp

Trình cài đặt sẽ sao chép các tệp I2P vào hệ thống của bạn. Quá trình này mất khoảng 1-2 phút.

![Quá trình cài đặt](/images/guides/macos-install/8-i2p.png)

### Bước 10: Tạo Script Khởi Chạy

Trình cài đặt tạo ra các script khởi chạy để khởi động I2P.

![Tạo script khởi động](/images/guides/macos-install/9-i2p.png)

### Bước 11: Phím tắt cài đặt

Trình cài đặt đề xuất tạo các lối tắt trên desktop và mục trong menu. Hãy lựa chọn và nhấn **Next**.

![Tạo shortcuts](/images/guides/macos-install/10-i2p.png)

### Bước 12: Hoàn tất Cài đặt

Thành công! I2P đã được cài đặt. Nhấp **Hoàn tất** để kết thúc.

![Cài đặt hoàn tất](/images/guides/macos-install/11-i2p.png)

## Phần Ba: Cấu hình Ứng dụng I2P

Bây giờ hãy làm cho I2P dễ khởi động bằng cách thêm nó vào thư mục Applications và Dock của bạn.

### Bước 1: Mở thư mục Ứng dụng

Mở Finder và điều hướng đến thư mục **Applications** của bạn.

![Mở thư mục Applications](/images/guides/macos-install/0-conf.png)

### Bước 2: Tìm I2P Launcher

Tìm thư mục **I2P** hoặc ứng dụng **Start I2P Router** bên trong `/Applications/i2p/`.

![Tìm trình khởi động I2P](/images/guides/macos-install/1-conf.png)

### Bước 3: Thêm vào Dock

Kéo ứng dụng **Start I2P Router** vào Dock của bạn để dễ dàng truy cập. Bạn cũng có thể tạo một bí danh trên desktop.

![Thêm I2P vào Dock của bạn](/images/guides/macos-install/2-conf.png)

**Mẹo**: Nhấp chuột phải vào biểu tượng I2P trong Dock và chọn **Options → Keep in Dock** để giữ nó cố định.

## Phần Bốn: Cấu hình Băng thông I2P

Khi bạn khởi chạy I2P lần đầu tiên, bạn sẽ thực hiện qua một trình hướng dẫn thiết lập để cấu hình các cài đặt băng thông. Điều này giúp tối ưu hóa hiệu suất của I2P cho kết nối của bạn.

### Bước 1: Khởi động I2P

Nhấp vào biểu tượng I2P trong Dock của bạn (hoặc nhấp đúp vào trình khởi động). Trình duyệt web mặc định của bạn sẽ mở I2P Router Console.

![Màn hình chào mừng I2P Router Console](/images/guides/macos-install/0-wiz.png)

### Bước 2: Trình hướng dẫn chào mừng

Trình hướng dẫn thiết lập sẽ chào đón bạn. Nhấp **Tiếp theo** để bắt đầu cấu hình I2P.

![Giới thiệu trình hướng dẫn cài đặt](/images/guides/macos-install/1-wiz.png)

### Bước 3: Ngôn ngữ và Giao diện

Chọn **ngôn ngữ giao diện** ưa thích của bạn và chọn giữa chủ đề **sáng** hoặc **tối**. Nhấp **Next**.

![Chọn ngôn ngữ và chủ đề](/images/guides/macos-install/2-wiz.png)

### Bước 4: Thông Tin Kiểm Tra Băng Thông

Trình hướng dẫn sẽ giải thích về kiểm tra băng thông. Kiểm tra này kết nối đến dịch vụ **M-Lab** để đo tốc độ internet của bạn. Nhấp **Next** để tiếp tục.

![Bandwidth test explanation](/images/guides/macos-install/3-wiz.png)

### Bước 5: Chạy Kiểm Tra Băng Thông

Nhấp **Chạy Kiểm tra** để đo tốc độ tải lên và tải xuống của bạn. Kiểm tra mất khoảng 30-60 giây.

![Chạy kiểm tra băng thông](/images/guides/macos-install/4-wiz.png)

### Bước 6: Kết Quả Kiểm Tra

Xem lại kết quả kiểm tra của bạn. I2P sẽ đề xuất cài đặt băng thông dựa trên tốc độ kết nối của bạn.

![Kết quả kiểm tra băng thông](/images/guides/macos-install/5-wiz.png)

### Bước 7: Cấu hình Chia sẻ Băng thông

Chọn lượng băng thông bạn muốn chia sẻ với mạng I2P:

- **Tự động** (Khuyên dùng): I2P quản lý băng thông dựa trên mức sử dụng của bạn
- **Giới hạn**: Đặt giới hạn cụ thể cho tải lên/tải xuống
- **Không giới hạn**: Chia sẻ càng nhiều càng tốt (dành cho kết nối nhanh)

Nhấp **Tiếp theo** để lưu cài đặt của bạn.

![Cấu hình chia sẻ băng thông](/images/guides/macos-install/6-wiz.png)

### Bước 8: Hoàn tất Cấu hình

Router I2P của bạn hiện đã được cấu hình và đang chạy! Bảng điều khiển router sẽ hiển thị trạng thái kết nối của bạn và cho phép bạn duyệt các trang web I2P.

## Bắt đầu với I2P

Bây giờ I2P đã được cài đặt và cấu hình, bạn có thể:

1. **Duyệt các trang I2P**: Truy cập [trang chủ I2P](http://127.0.0.1:7657/home) để xem các liên kết đến các dịch vụ I2P phổ biến
2. **Cấu hình trình duyệt**: Thiết lập [hồ sơ trình duyệt](/docs/guides/browser-config) để truy cập các trang `.i2p`
3. **Khám phá dịch vụ**: Tìm hiểu email I2P, diễn đàn, chia sẻ tệp và nhiều hơn nữa
4. **Giám sát router**: [Console](http://127.0.0.1:7657/console) hiển thị trạng thái mạng và thống kê của bạn

### Liên kết hữu ích

- **Router Console**: [http://127.0.0.1:7657/](http://127.0.0.1:7657/)
- **Cấu hình**: [http://127.0.0.1:7657/config](http://127.0.0.1:7657/config)
- **Sổ địa chỉ**: [http://127.0.0.1:7657/susidns/addressbook](http://127.0.0.1:7657/susidns/addressbook)
- **Cài đặt băng thông**: [http://127.0.0.1:7657/config](http://127.0.0.1:7657/config)

## Chạy lại Trình hướng dẫn cài đặt

Nếu bạn muốn thay đổi cài đặt băng thông hoặc cấu hình lại I2P sau này, bạn có thể chạy lại trình hướng dẫn chào mừng từ Router Console:

1. Đi tới [I2P Setup Wizard](http://127.0.0.1:7657/welcome)
2. Thực hiện lại các bước của wizard

## Khắc phục sự cố

### I2P Không Khởi Động Được

- **Kiểm tra Java**: Đảm bảo Java đã được cài đặt bằng cách chạy `java -version` trong Terminal
- **Kiểm tra quyền truy cập**: Đảm bảo thư mục I2P có quyền truy cập chính xác
- **Kiểm tra logs**: Xem tại `~/.i2p/wrapper.log` để tìm thông báo lỗi

### Trình duyệt không thể truy cập các trang I2P

- Đảm bảo I2P đang chạy (kiểm tra Router Console)
- Cấu hình proxy của trình duyệt để sử dụng HTTP proxy `127.0.0.1:4444`
- Đợi 5-10 phút sau khi khởi động để I2P tích hợp vào mạng

### Hiệu suất chậm

- Chạy lại bài kiểm tra băng thông và điều chỉnh cài đặt của bạn
- Đảm bảo bạn đang chia sẻ một phần băng thông với mạng lưới
- Kiểm tra trạng thái kết nối trong Router Console

## Gỡ cài đặt I2P

Để gỡ bỏ I2P khỏi Mac của bạn:

1. Thoát router I2P nếu nó đang chạy
2. Xóa thư mục `/Applications/i2p`
3. Xóa thư mục `~/.i2p` (cấu hình và dữ liệu I2P của bạn)
4. Xóa biểu tượng I2P khỏi Dock

## Các Bước Tiếp Theo

- **Tham gia cộng đồng**: Ghé thăm [i2pforum.net](http://i2pforum.net) hoặc xem I2P trên Reddit
- **Tìm hiểu thêm**: Đọc [tài liệu I2P](/en/docs) để hiểu cách mạng hoạt động
- **Tham gia đóng góp**: Cân nhắc [đóng góp cho việc phát triển I2P](/en/get-involved) hoặc vận hành cơ sở hạ tầng

Chúc mừng! Bạn hiện đã là một phần của mạng I2P. Chào mừng đến với internet vô hình!

---
