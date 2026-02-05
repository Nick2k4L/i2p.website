---
title: "Đặc tả Datagram"
description: "Đặc tả các định dạng thông điệp datagram của I2P bao gồm các loại thô, có thể trả lời và đã xác thực"
slug: "datagrams"
category: "Giao thức"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

## Tổng quan

Xem [tài liệu API Datagrams](/docs/api/datagrams/) để có cái nhìn tổng quan về API Datagrams.

Các loại sau đây được định nghĩa. Các số giao thức tiêu chuẩn được liệt kê, tuy nhiên có thể sử dụng bất kỳ số giao thức nào khác ngoài số giao thức streaming (6), tùy theo ứng dụng cụ thể.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Protocol</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Repliable?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Authenticated?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Replay Prevention?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">As Of</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Raw</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
  </tbody>
</table>
Hỗ trợ cho Datagram2 và Datagram3 trong các triển khai router và thư viện khác nhau vẫn chưa được xác định. Hãy kiểm tra tài liệu cho các triển khai đó.

### Nhận dạng loại Datagram

Bốn kiểu datagram không chia sẻ header chung với phiên bản giao thức ở cùng một vị trí. Các gói tin không thể được xác định theo kiểu dựa trên nội dung của chúng. Khi sử dụng nhiều kiểu trên cùng một phiên, hoặc một kiểu duy nhất cùng với streaming, các ứng dụng phải sử dụng số giao thức và/hoặc cổng I2CP/SAM để định tuyến các gói tin đến đến đúng nơi. Việc sử dụng các số giao thức tiêu chuẩn sẽ làm cho điều này dễ dàng hơn. Để trống số giao thức (0 hoặc PROTO_ANY), ngay cả đối với ứng dụng chỉ sử dụng datagram, không được khuyến khích vì nó làm tăng khả năng xảy ra lỗi định tuyến và khiến việc nâng cấp lên ứng dụng đa giao thức trở nên khó khăn hơn. Các trường version trong Datagram 2 và 3 chỉ được cung cấp như một kiểm tra bổ sung cho các lỗi định tuyến và những thay đổi trong tương lai.

### Thiết Kế Ứng Dụng

Tất cả việc sử dụng datagram đều phụ thuộc vào ứng dụng cụ thể.

Vì các datagram được xác thực mang theo overhead đáng kể, một ứng dụng điển hình sử dụng cả datagram được xác thực và không được xác thực. Một thiết kế điển hình là gửi một datagram được xác thực duy nhất chứa token từ client đến server. Server trả lời bằng một datagram không được xác thực chứa cùng token đó. Bất kỳ giao tiếp tiếp theo nào, trước khi token hết hạn, đều sử dụng raw datagram.

Các ứng dụng gửi và nhận datagram sử dụng số giao thức và cổng thông qua API [I2CP](/docs/specs/i2cp/) hoặc [SAMv3](/docs/api/samv3/).

Datagrams tất nhiên là không đáng tin cậy. Các ứng dụng phải thiết kế cho việc giao hàng không đáng tin cậy. Trong I2P, việc giao hàng là đáng tin cậy từ hop-to-hop nếu hop tiếp theo có thể tiếp cận được, vì các transport NTCP2 và SSU2 cung cấp độ tin cậy. Tuy nhiên, việc giao hàng end-to-end không đáng tin cậy, vì các tin nhắn I2NP có thể bị loại bỏ trong bất kỳ hop nào do giới hạn hàng đợi, hết hạn, timeout, giới hạn băng thông, hoặc các next-hops không thể tiếp cận.

### Kích thước Datagram

Giới hạn kích thước danh nghĩa cho các thông điệp I2NP, bao gồm cả datagram, là 64 KB. Chi phí overhead của garlic encryption và tunnel message làm giảm con số này một chút.

Tuy nhiên, tất cả các thông điệp I2NP phải được phân mảnh thành các thông điệp tunnel 1 KB. Xác suất drop của một thông điệp I2NP n KB là hàm mũ của xác suất drop của một thông điệp tunnel đơn lẻ, p ** n. Vì việc phân mảnh dẫn đến một loạt các thông điệp tunnel liên tiếp, xác suất drop thực tế cao hơn nhiều so với hàm mũ có thể gợi ý, do các giới hạn hàng đợi và quản lý hàng đợi chủ động (AQM, CoDel hoặc tương tự) trong các triển khai router.

Kích thước tối đa điển hình được khuyến nghị để đảm bảo giao hàng đáng tin cậy là vài KB, hoặc nhiều nhất là 10 KB. Với việc phân tích cẩn thận các kích thước overhead ở tất cả các lớp giao thức (trừ lớp transport), các nhà phát triển nên đặt kích thước payload tối đa sao cho phù hợp chính xác trong một, hai, hoặc ba tunnel message. Điều này sẽ tối đa hóa hiệu quả và độ tin cậy. Overhead ở các lớp khác nhau bao gồm gzip header, I2NP header, garlic message header, garlic encryption, tunnel message header, tunnel message fragmentation headers, và các thành phần khác. Xem tính toán MTU streaming trong [Proposal 144](/proposals/144-ecies-x25519-aead-ratchet/) và ConnectionOptions.java trong mã nguồn Java I2P để làm ví dụ.

### Cân nhắc về SAM

Các ứng dụng gửi và nhận datagram sử dụng số protocol và port thông qua I2CP API hoặc SAM. Việc chỉ định số protocol và port qua SAM yêu cầu SAM v3.2 trở lên. Sử dụng cả datagram và streaming (UDP và TCP) trên cùng một phiên SAM (tunnel) yêu cầu SAM v3.3 trở lên. Sử dụng nhiều loại datagram trên cùng một phiên SAM (tunnel) yêu cầu SAM v3.3 trở lên. SAM v3.3 hiện tại chỉ được hỗ trợ bởi Java I2P router.

Hỗ trợ SAM cho Datagram2 và Datagram3 trong các triển khai router và thư viện khác nhau vẫn chưa được xác định. Hãy kiểm tra tài liệu cho những triển khai đó.

Lưu ý rằng các kích thước vượt quá MTU mạng thông thường 1500 byte sẽ ngăn cản các ứng dụng SAM vận chuyển các gói tin không bị phân mảnh tới/từ máy chủ SAM, nếu ứng dụng và máy chủ ở trên các máy tính riêng biệt. Thông thường, điều này không xảy ra, cả hai đều ở trên localhost, nơi MTU là 65536 hoặc cao hơn. Nếu một ứng dụng SAM dự kiến sẽ được tách biệt trên một máy tính khác với máy chủ, tải trọng tối đa cho một datagram có thể trả lời là chỉ dưới 1 KB một chút.

### Cân nhắc về PQ

Nếu phần MLDSA của [Đề xuất 169 Post-Quantum](/proposals/169-pq-crypto/) được triển khai, overhead sẽ tăng đáng kể. Kích thước của một destination + chữ ký sẽ tăng từ 391 + 64 = 455 bytes lên tối thiểu 3739 cho MLDSA44 và tối đa 7226 cho MLDSA87. Tác động thực tế của điều này vẫn chưa được xác định. Datagram3, với xác thực được cung cấp bởi router, có thể là một giải pháp.

## Datagram Thô (Không Thể Trả Lời) {#raw}

Các datagram không thể trả lời không có địa chỉ 'from' và không được xác thực. Chúng cũng được gọi là datagram "thô" (raw). Nói một cách nghiêm ngặt, chúng hoàn toàn không phải là "datagram", chúng chỉ là dữ liệu thô. Chúng không được xử lý bởi datagram API. Tuy nhiên, SAM và các lớp I2PTunnel hỗ trợ "raw datagram".

Số giao thức I2CP tiêu chuẩn cho raw datagram là PROTO_DATAGRAM_RAW (18).

Định dạng không được chỉ định ở đây, nó được xác định bởi ứng dụng. Để đầy đủ thông tin, chúng tôi đưa vào một hình ảnh về định dạng bên dưới.

### Định dạng

```
+----+----+----+----+----//
| payload...
+----+----+----+----+----//

length: 0 - about 64 KB (see notes)
```
### Ghi chú

Độ dài thực tế bị giới hạn bởi cả overhead ở các lớp khác nhau và độ tin cậy.

## Datagram1 (Có thể trả lời) {#repliable}

Datagram có thể phản hồi chứa địa chỉ 'from' và chữ ký. Những thành phần này thêm ít nhất 427 byte overhead.

Số giao thức I2CP tiêu chuẩn cho datagram có thể phản hồi là PROTO_DATAGRAM (17).

### Định dạng

```
+----+----+----+----+----+----+----+----+
| from                                  |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+                                       +
|                                       |
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
| payload...
+----+----+----+----//

from :: a Destination
        length: 387+ bytes
        The originator and signer of the datagram

signature :: a Signature
             Signature type must match the signing public key type of $from
             length: 40+ bytes, as implied by the Signature type.
             For the default DSA_SHA1 key type:
                The DSA Signature of the SHA-256 hash of the payload.
             For other key types:
                The Signature of the payload.
             The signature may be verified by the signing public key of $from

payload :: The data
           Length: 0 to about 63 KB (see notes)

Total length: Payload length + 427+
```
### Ghi chú

- Độ dài thực tế bị giới hạn bởi cả overhead ở các tầng khác nhau và độ tin cậy.
- Xem các ghi chú quan trọng về độ tin cậy của datagram lớn trong [tài liệu API Datagrams](/docs/api/datagrams/). Để có kết quả tốt nhất, hãy giới hạn payload khoảng 10 KB hoặc ít hơn.
- Signature cho các loại khác DSA_SHA1 đã được định nghĩa lại trong phiên bản 0.9.14.
- Định dạng này không hỗ trợ bao gồm offline signature block cho LS2 (đề xuất 123). Một giao thức mới với các flag phải được định nghĩa cho việc đó.

## Datagram2 {#datagram2}

Định dạng Datagram2 được quy định theo [Proposal 163](/proposals/163-datagram2/). Số giao thức I2CP cho Datagram2 là 19.

Datagram2 được thiết kế để thay thế cho Datagram1. Nó bổ sung các tính năng sau vào Datagram1:

- Ngăn chặn tấn công replay
- Hỗ trợ chữ ký offline
- Các trường flags và options để mở rộng

Lưu ý rằng thuật toán tính toán chữ ký cho Datagram2 khác biệt đáng kể so với Datagram1.

### Định dạng

```
+----+----+----+----+----+----+----+----+
|                                       |
~            from                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~     offline_signature (optional)      ~
~   expires, sigtype, pubkey, offsig    ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            signature                  ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

from :: a Destination
        length: 387+ bytes
        The originator and (unless offline signed) signer of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x02 (0 0 1 0)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bit 5: If 0, no offline sig; if 1, offline signed
         Bits 15-6: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

offline_signature ::
             If flag indicates offline keys, the offline signature section,
             as specified in the Common Structures Specification,
             with the following 4 fields. Length: varies by online and offline
             sig types, typically 102 bytes for Ed25519
             This section can, and should, be generated offline.

  expires :: Expires timestamp
             (4 bytes, big endian, seconds since epoch, rolls over in 2106)

  sigtype :: Transient sig type (2 bytes, big endian)

  pubkey :: Transient signing public key (length as implied by sig type),
            typically 32 bytes for Ed25519 sig type.

  offsig :: a Signature
            Signature of expires timestamp, transient sig type,
            and public key, by the destination public key,
            length: 40+ bytes, as implied by the Signature type, typically
            64 bytes for Ed25519 sig type.

payload :: The data
           Length: 0 to about 61 KB (see notes)

signature :: a Signature
             Signature type must match the signing public key type of $from
             (if no offline signature) or the transient sigtype
             (if offline signed)
             length: 40+ bytes, as implied by the Signature type, typically
             64 bytes for Ed25519 sig type.
             The Signature of the payload and other fields as specified below.
             The signature is verified by the signing public key of $from
             (if no offline signature) or the transient pubkey
             (if offline signed)
```
Tổng độ dài: tối thiểu 433 + độ dài payload; độ dài điển hình cho người gửi X25519 và không có chữ ký offline: 457 + độ dài payload. Lưu ý rằng thông điệp thường sẽ được nén bằng gzip tại lớp I2CP, điều này sẽ mang lại sự tiết kiệm đáng kể nếu destination nguồn có thể nén được.

Lưu ý: Định dạng chữ ký offline giống như trong [Đặc tả Cấu trúc Chung](/docs/specs/common-structures/) và [Đặc tả Streaming](/docs/specs/streaming/).

### Chữ ký

Chữ ký được tạo trên các trường sau:

- Prelude: Hash 32-byte của đích đến mục tiêu (không được bao gồm trong datagram)
- flags
- options (nếu có)
- offline_signature (nếu có)
- payload

Trong repliable datagram, đối với loại khóa DSA_SHA1, chữ ký được tạo trên hash SHA-256 của payload chứ không phải chính payload đó; ở đây, chữ ký luôn được tạo trên các trường bên trên (KHÔNG phải hash), bất kể loại khóa nào.

### Xác minh ToHash

Các bên nhận phải xác minh chữ ký (sử dụng hash đích của họ) và loại bỏ datagram nếu thất bại, để ngăn chặn tấn công replay.

## Datagram3 {#datagram3}

Định dạng Datagram3 được chỉ định như trong [Đề xuất 163](/proposals/163-datagram2/). Số giao thức I2CP cho Datagram3 là 20.

Datagram3 được thiết kế như một phiên bản nâng cao của raw datagrams. Nó bổ sung các tính năng sau cho raw datagrams:

- Khả năng trả lời
- Các trường cờ và tùy chọn để mở rộng

Datagram3 KHÔNG được xác thực. Trong một đề xuất tương lai, việc xác thực có thể được cung cấp bởi lớp ratchet của router, và trạng thái xác thực sẽ được chuyển đến client.

### Định dạng

```
+----+----+----+----+----+----+----+----+
|                                       |
~            fromhash                   ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

fromhash :: a Hash
            length: 32 bytes
            The originator of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x03 (0 0 1 1)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bits 15-5: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

payload :: The data
           Length: 0 to about 61 KB (see notes)
```
Tổng độ dài: tối thiểu 34 + độ dài payload.

## Tài liệu tham khảo

- [Common](/docs/specs/common-structures/) - Đặc tả Cấu trúc Chung
- [DATAGRAMS](/docs/api/datagrams/) - Tổng quan API Datagrams
- [I2CP](/docs/specs/i2cp/) - Đặc tả I2CP
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet/) - Đề xuất ECIES-X25519-AEAD-Ratchet
- [Prop163](/proposals/163-datagram2/) - Đề xuất Datagram2 và Datagram3
- [Prop169](/proposals/169-pq-crypto/) - Đề xuất Mật mã học Hậu Lượng tử
- [SAMv3](/docs/api/samv3/) - Đặc tả SAM v3
- [Streaming](/docs/specs/streaming/) - Đặc tả Streaming
- [TRANSPORT](/docs/overview/transport/) - Tổng quan Transport
- [TUNMSG](/docs/specs/tunnel-message/#notes) - Đặc tả Thông điệp Tunnel
