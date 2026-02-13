---
title: "Các ứng dụng I2P thay thế"
description: "Các triển khai I2P client được cộng đồng duy trì (cập nhật cho năm 2025)"
slug: "alternative-clients"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

Phiên bản I2P client chính sử dụng **Java**. Nếu bạn không thể hoặc không muốn sử dụng Java trên một hệ thống cụ thể, có các phiên bản I2P client thay thế được phát triển và duy trì bởi các thành viên cộng đồng. Những chương trình này cung cấp cùng chức năng cốt lõi bằng cách sử dụng các ngôn ngữ lập trình hoặc phương pháp khác nhau.

---

## Bảng So Sánh

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Client</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Language</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Maturity</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Actively Maintained</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Suitable For</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Java I2P</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes (official)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">General users</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Standard full router; includes console, plugins, and tools</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>i2pd</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Low-resource systems, servers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Lightweight, fully compatible with Java I2P, includes web console</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Go-I2P</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Experimental</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">⚙️ In development</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Developers, testing</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Early-stage Go implementation; not yet production ready</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Emissary</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Experimental</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">⚙️ In development</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Developers, embedded use</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Rust I2P implementation; embeddable router with eepsite, torrent, IRC and email support</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>I2P+</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable (fork)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Advanced users</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Enhanced Java I2P fork with UI and performance improvements</td>
    </tr>
  </tbody>
</table>
---

## i2pd (C++)

**Website:** [https://i2pd.website](https://i2pd.website)

**Mô tả:** i2pd (*I2P Daemon*) là một I2P client đầy đủ tính năng được triển khai bằng C++. Nó đã ổn định cho việc sử dụng trong môi trường sản xuất trong nhiều năm (từ khoảng 2016) và được cộng đồng duy trì tích cực. i2pd triển khai đầy đủ các giao thức mạng I2P và API, làm cho nó hoàn toàn tương thích với mạng Java I2P. Router C++ này thường được sử dụng như một giải pháp thay thế nhẹ trên các hệ thống nơi Java runtime không có sẵn hoặc không mong muốn. i2pd bao gồm một console web tích hợp cho việc cấu hình và giám sát. Nó đa nền tảng và có sẵn trong nhiều định dạng gói — thậm chí còn có phiên bản Android của i2pd (ví dụ, thông qua F-Droid).

---

## Go-I2P (Go)

**Kho mã nguồn:** [https://github.com/go-i2p/go-i2p](https://github.com/go-i2p/go-i2p)

**Mô tả:** Go-I2P là một I2P client được viết bằng ngôn ngữ lập trình Go. Đây là một triển khai độc lập của I2P router, nhằm tận dụng hiệu quả và tính di động của Go. Dự án đang được phát triển tích cực, nhưng vẫn ở giai đoạn đầu và chưa hoàn thiện đầy đủ tính năng. Tính đến năm 2025, Go-I2P được coi là thử nghiệm — đang được các nhà phát triển cộng đồng tích cực làm việc, nhưng không được khuyến nghị sử dụng trong môi trường sản xuất cho đến khi trưởng thành hơn. Mục tiêu của Go-I2P là cung cấp một I2P router hiện đại, nhẹ với khả năng tương thích đầy đủ với mạng I2P khi quá trình phát triển hoàn tất.

---

## Emissary (Rust)

**Trang web:** [https://altonen.github.io/emissary/](https://altonen.github.io/emissary/)

**Mô tả:** Emissary là một triển khai bằng Rust của ngăn xếp giao thức I2P, được thiết kế để hoạt động như một I2P router có thể nhúng. Nó có thể được tích hợp vào các ứng dụng khác hoặc chạy độc lập. Emissary hỗ trợ lưu trữ eepsite, torrent, IRC và dịch vụ email. Dự án bao gồm tài liệu mở rộng bao quát thiết lập khởi động nhanh, nhúng cho nhà phát triển, và cấu hình chi tiết. Là một dự án thực nghiệm, nó đang trong quá trình phát triển tích cực và chưa được khuyến nghị để sử dụng trong sản xuất.

---

## I2P+ (phiên bản Java fork)

**Website:** [https://i2pplus.github.io](https://i2pplus.github.io)

**Mô tả:** I2P+ là một nhánh được cộng đồng duy trì của client Java I2P tiêu chuẩn. Đây không phải là một triển khai lại bằng ngôn ngữ mới, mà là một phiên bản nâng cao của Java router với các tính năng và tối ưu hóa bổ sung. I2P+ tập trung vào việc cung cấp trải nghiệm người dùng được cải thiện và hiệu suất tốt hơn trong khi vẫn hoàn toàn tương thích với mạng I2P chính thức. Nó giới thiệu giao diện web console được làm mới, các tùy chọn cấu hình thân thiện với người dùng hơn, và nhiều tối ưu hóa khác nhau (ví dụ: hiệu suất torrent được cải thiện và xử lý tốt hơn các peer mạng, đặc biệt đối với các router đằng sau tường lửa). I2P+ yêu cầu môi trường Java giống như phần mềm I2P chính thức, vì vậy đây không phải là giải pháp cho các môi trường không có Java. Tuy nhiên, đối với những người dùng có Java và muốn một bản build thay thế với khả năng bổ sung, I2P+ cung cấp một lựa chọn hấp dẫn. Nhánh này được cập nhật thường xuyên với các bản phát hành I2P gốc (với cách đánh số phiên bản thêm dấu "+") và có thể được tải từ trang web của dự án.
