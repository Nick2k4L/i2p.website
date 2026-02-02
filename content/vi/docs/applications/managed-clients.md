---
title: "Client được Quản lý"
description: "Cách các ứng dụng được quản lý bởi router tích hợp với ClientAppManager và bộ ánh xạ cổng"
slug: "managed-clients"
lastUpdated: "2014-02"
accurateFor: "0.9.11"
---

## Tổng quan

Các client có thể được khởi động trực tiếp bởi router khi chúng được liệt kê trong tệp [clients.config](/docs/specs/configuration/). Những client này có thể là "managed" (được quản lý) hoặc "unmanaged" (không được quản lý). Điều này được xử lý bởi ClientAppManager. Ngoài ra, các client được quản lý hoặc không được quản lý có thể đăng ký với ClientAppManager để các client khác có thể truy xuất tham chiếu đến chúng. Cũng có một công cụ Port Mapper đơn giản để các client đăng ký cổng nội bộ mà các client khác có thể tra cứu.

---

## Managed Clients

Kể từ phiên bản 0.9.4, router hỗ trợ các managed client (client được quản lý). Managed client được khởi tạo và bắt đầu bởi ClientAppManager. ClientAppManager duy trì một tham chiếu đến client và nhận các cập nhật về trạng thái của client. Managed client được ưa chuộng hơn, vì việc triển khai theo dõi trạng thái và khởi động cũng như dừng client dễ dàng hơn nhiều. Nó cũng giúp tránh các tham chiếu tĩnh trong mã client một cách dễ dàng hơn, điều có thể dẫn đến việc sử dụng bộ nhớ quá mức sau khi client được dừng. Managed client có thể được khởi động và dừng bởi người dùng trong router console, và sẽ được dừng khi router tắt.

Các client được quản lý triển khai giao diện net.i2p.app.ClientApp hoặc net.i2p.router.app.RouterApp. Các client triển khai giao diện ClientApp phải cung cấp constructor sau:

```java
public MyClientApp(I2PAppContext context, ClientAppManager listener, String[] args)
```
Các client triển khai giao diện RouterApp phải cung cấp constructor sau:

```java
public MyClientApp(RouterContext context, ClientAppManager listener, String[] args)
```
Các tham số được cung cấp được chỉ định trong tệp clients.config.

---

## Clients Không Được Quản Lý

Nếu lớp chính được chỉ định trong tệp clients.config không triển khai giao diện được quản lý, nó sẽ được khởi động bằng main() với các tham số được chỉ định, và dừng lại bằng main() với các tham số được chỉ định. Router không duy trì tham chiếu, vì tất cả các tương tác đều thông qua phương thức main() tĩnh. Console không thể cung cấp thông tin trạng thái chính xác cho người dùng.

---

## Clients Đã Đăng Ký

Các client, dù được quản lý hay không được quản lý, có thể đăng ký với ClientAppManager để các client khác có thể truy xuất tham chiếu đến chúng. Việc đăng ký được thực hiện theo tên. Các client đã đăng ký được biết đến là:

```
console, i2ptunnel, Jetty, outproxy, update
```
---

## Trình Ánh Xạ Cổng

Router cũng cung cấp một cơ chế đơn giản để các client tìm kiếm dịch vụ socket nội bộ, chẳng hạn như HTTP proxy. Điều này được cung cấp bởi Port Mapper. Việc đăng ký được thực hiện theo tên. Các client đăng ký thường cung cấp một socket mô phỏng nội bộ trên cổng đó.
