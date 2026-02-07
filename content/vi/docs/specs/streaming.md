---
title: "Đặc tả Giao thức Streaming"
description: "Đặc tả cho giao thức streaming I2P cung cấp vận chuyển đáng tin cậy giống TCP"
slug: "streaming"
category: "Giao thức"
lastUpdated: "2023-10"
accurateFor: "0.9.59"
---

## Tổng quan

Xem [Streaming Library](/docs/api/streaming) để có cái nhìn tổng quan về giao thức Streaming.

## Phiên bản Giao thức

Giao thức streaming không bao gồm trường phiên bản. Các phiên bản được liệt kê dưới đây dành cho Java I2P. Việc triển khai và hỗ trợ mã hóa thực tế có thể khác nhau. Không có cách nào để xác định liệu đầu xa có hỗ trợ phiên bản hoặc tính năng cụ thể nào hay không. Bảng dưới đây chỉ mang tính hướng dẫn chung về ngày phát hành của các tính năng khác nhau.

Các tính năng được liệt kê dưới đây dành cho chính giao thức. Nhiều tùy chọn cấu hình khác nhau được ghi lại trong [Streaming Library](/docs/api/streaming) cùng với phiên bản Java I2P mà chúng được triển khai.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Router Version</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Streaming Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Bob's hash in NACKs field of SYN packet</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE option</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">I2CP protocol number enforced</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED no longer required in RESET</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PINGs and PONGs may include a payload</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA Ed25519 sig type</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA P-256, P-384, and P-521 sig types</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Variable-length signatures</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.7.1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Protocol numbers defined in I2CP</td>
    </tr>
  </tbody>
</table>
## Đặc tả Giao thức

### Định Dạng Gói Tin

Định dạng của một gói tin đơn trong giao thức streaming được hiển thị bên dưới. Kích thước header tối thiểu, không có NACK hoặc dữ liệu tùy chọn, là 22 byte.

Không có trường độ dài trong giao thức streaming. Việc đóng khung được cung cấp bởi các lớp thấp hơn - I2CP và I2NP.

```
+----+----+----+----+----+----+----+----+
| send Stream ID    | rcv Stream ID     |
+----+----+----+----+----+----+----+----+
| sequence  Num     | ack Through       |
+----+----+----+----+----+----+----+----+
| nc |  nc*4 bytes of NACKs (optional)
+----+----+----+----+----+----+----+----+
     | rd |  flags  | opt size| opt data
+----+----+----+----+----+----+----+----+
   ...  (optional, see below)           |
+----+----+----+----+----+----+----+----+
|   payload ...
+----+----+----+-//
```
**sendStreamId** :: 4 byte [Integer](/docs/specs/common-structures#integer) : Số ngẫu nhiên được chọn bởi người nhận gói tin trước khi gửi gói tin SYN reply đầu tiên và không đổi trong suốt vòng đời của kết nối, lớn hơn 0. Giá trị 0 trong thông điệp SYN được gửi bởi bên khởi tạo kết nối, và trong các thông điệp tiếp theo, cho đến khi nhận được SYN reply chứa stream ID của peer.

**receiveStreamId** :: 4 byte [Integer](/docs/specs/common-structures#integer) : Số ngẫu nhiên được chọn bởi bên khởi tạo gói tin trước khi gửi gói SYN đầu tiên và không đổi trong suốt thời gian tồn tại của kết nối, lớn hơn không. Có thể là 0 nếu không biết, ví dụ trong gói RESET.

**sequenceNum** :: 4 byte [Integer](/docs/specs/common-structures#integer) : Số thứ tự cho thông báo này, bắt đầu từ 0 trong thông báo SYN, và tăng thêm 1 trong mỗi thông báo trừ các ACK đơn thuần và truyền lại. Nếu sequenceNum là 0 và cờ SYN không được đặt, đây là gói ACK đơn thuần không nên được ACK.

**ackThrough** :: 4 byte [Integer](/docs/specs/common-structures#integer) : Số thứ tự gói tin cao nhất đã được nhận trên receiveStreamId. Trường này được bỏ qua trong gói tin kết nối ban đầu (khi receiveStreamId là id không xác định) hoặc nếu cờ NO_ACK được thiết lập. Tất cả các gói tin đến và bao gồm số thứ tự này đều được ACK, NGOẠI TRỪ những gói tin được liệt kê trong NACKs bên dưới.

**Số lượng NACK** :: 1 byte [Integer](/docs/specs/common-structures#integer) : Số lượng NACK 4-byte trong trường tiếp theo, hoặc 8 khi được sử dụng cùng với SYNCHRONIZE để ngăn chặn replay từ phiên bản 0.9.58; xem bên dưới.

**NACKs** :: nc * 4 byte [Integer](/docs/specs/common-structures#integer)s : Các số thứ tự nhỏ hơn ackThrough mà chưa được nhận. Hai NACK của một gói tin là yêu cầu 'truyền lại nhanh' gói tin đó. Cũng được sử dụng cùng với SYNCHRONIZE để ngăn chặn replay tấn công kể từ phiên bản 0.9.58; xem bên dưới.

**resendDelay** :: 1 byte [Integer](/docs/specs/common-structures#integer) : Người tạo gói tin này sẽ đợi bao lâu trước khi gửi lại gói tin này (nếu chưa nhận được ACK). Giá trị tính bằng giây kể từ khi gói tin được tạo. Hiện tại bị bỏ qua khi nhận.

**flags** :: giá trị 2 byte : Xem bên dưới.

**option size** :: 2 byte [Integer](/docs/specs/common-structures#integer) : Số byte trong trường tiếp theo

**option data** :: 0 hoặc nhiều byte : Như được chỉ định bởi các flags. Xem bên dưới.

**payload** :: kích thước gói tin còn lại

### Các trường Flags và Option Data

Trường flags ở trên chỉ định một số metadata về gói tin, và do đó có thể yêu cầu một số dữ liệu bổ sung nhất định được bao gồm. Các flags như sau. Bất kỳ cấu trúc dữ liệu nào được chỉ định phải được thêm vào vùng options theo thứ tự đã cho.

Thứ tự bit: 15....0 (15 là MSB)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Flag</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Order</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SYNCHRONIZE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP SYN. Set in the initial packet and in the first response. FROM_INCLUDED and SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">CLOSE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP FIN. If the response to a SYNCHRONIZE fits in a single message, the response will contain both SYNCHRONIZE and CLOSE. SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RESET</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Abnormal close. SIGNATURE_INCLUDED must also be set. Prior to release 0.9.20, due to a bug, FROM_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#signature">Signature</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, CLOSE, and RESET, where it is required, and with ECHO, where it is required for a ping. The signature uses the Destination's <a href="/docs/specs/common-structures#signingprivatekey">SigningPrivateKey</a> to sign the entire header and payload with the space in the option data field for the signature being set to all zeroes. Prior to release 0.9.11, the signature was always 40 bytes. As of release 0.9.11, the signature may be variable-length, see below for details.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused. Requests every packet in the other direction to have SIGNATURE_INCLUDED</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">387+ byte <a href="/docs/specs/common-structures#destination">Destination</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, where it is required, and with ECHO, where it is required for a ping. Prior to release 0.9.20, due to a bug, must also be sent with RESET.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DELAY_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Optional delay. How many milliseconds the sender of this packet wants the recipient to wait before sending any more data. A value greater than 60000 indicates choking. A value of 0 requests an immediate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MAX_PACKET_SIZE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum length of the payload. Send with SYNCHRONIZE.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PROFILE_INTERACTIVE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused or ignored; the interactive profile is unimplemented.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECHO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused except by ping programs. If set, most other options are ignored. See the <a href="/docs/api/streaming">streaming docs</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">NO_ACK</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">This flag simply tells the recipient to ignore the ackThrough field in the header. Currently set in the initial SYN packet, otherwise the ackThrough field is always valid. Note that this does not save any space, the ackThrough field is before the flags and is always present.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#offlinesignature">OfflineSig</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Contains the offline signature section from LS2. See proposal 123 and the common structures specification. FROM_INCLUDED must also be set. Contains an OfflineSig: 1) Expires timestamp (4 bytes, seconds since epoch, rolls over in 2106) 2) Transient sig type (2 bytes) 3) Transient <a href="/docs/specs/common-structures#signingpublickey">SigningPublicKey</a> (length as implied by sig type) 4) <a href="/docs/specs/common-structures#signature">Signature</a> of expires timestamp, transient sig type, and public key, by the destination public key. Length of sig as implied by the destination public key sig type.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12-15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">unused</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Set to zero for compatibility with future uses.</td>
    </tr>
  </tbody>
</table>
### Ghi Chú Về Chữ Ký Độ Dài Biến Đổi

Trước phiên bản 0.9.11, chữ ký trong trường tùy chọn luôn có độ dài 40 byte.

Kể từ phiên bản 0.9.11, chữ ký có độ dài biến thiên. Loại và độ dài Signature được suy ra từ loại khóa được sử dụng trong tùy chọn FROM_INCLUDED và tài liệu [Signature](/docs/specs/common-structures#signature).

Kể từ phiên bản 0.9.39, tùy chọn OFFLINE_SIGNATURE đã được hỗ trợ. Nếu tùy chọn này có mặt, [SigningPublicKey](/docs/specs/common-structures#signingpublickey) tạm thời sẽ được sử dụng để xác minh bất kỳ gói tin đã ký nào, và độ dài cũng như loại chữ ký được suy ra từ SigningPublicKey tạm thời trong tùy chọn.

- Khi một gói tin chứa cả FROM_INCLUDED và SIGNATURE_INCLUDED (như trong SYNCHRONIZE), việc suy luận có thể được thực hiện trực tiếp.

- Khi một gói tin không chứa FROM_INCLUDED, việc suy luận phải được thực hiện từ một gói tin SYNCHRONIZE trước đó.

- Khi một gói tin không chứa FROM_INCLUDED, và không có gói tin SYNCHRONIZE trước đó (ví dụ như một gói tin CLOSE hoặc RESET lạc), có thể suy luận từ độ dài của các tùy chọn còn lại (vì SIGNATURE_INCLUDED là tùy chọn cuối cùng), nhưng gói tin có thể sẽ bị loại bỏ, vì không có FROM để xác thực chữ ký. Nếu có thêm các trường tùy chọn được định nghĩa trong tương lai, chúng phải được tính đến.

### Ngăn chặn Replay

Để ngăn Bob sử dụng tấn công replay bằng cách lưu trữ gói SYNCHRONIZE đã ký hợp lệ nhận được từ Alice và sau đó gửi nó đến nạn nhân Charlie, Alice phải bao gồm hash destination của Bob trong gói SYNCHRONIZE như sau:

```
Set NACK count field to 8
Set the NACKs field to Bob's 32-byte destination hash
```
Khi nhận được một SYNCHRONIZE, nếu trường NACK count là 8, Bob phải diễn giải trường NACKs như một destination hash 32-byte, và phải xác minh rằng nó khớp với destination hash của anh ta. Anh ta cũng phải xác minh chữ ký của gói tin như thường lệ, vì nó bao phủ toàn bộ gói tin bao gồm các trường NACK count và NACKs. Nếu NACK count là 8 và trường NACKs không khớp, Bob phải loại bỏ gói tin.

Điều này là bắt buộc cho các phiên bản 0.9.58 trở lên. Điều này tương thích ngược với các phiên bản cũ hơn, vì NACK không được mong đợi trong gói tin SYNCHRONIZE. Các destination không thể và không thể biết phiên bản nào mà đầu kia đang chạy.

Không cần thay đổi gì cho gói tin SYNCHRONIZE ACK được gửi từ Bob đến Alice; không bao gồm các NACK trong gói tin đó.

## Tài liệu tham khảo

- **[Destination]** [Destination](/docs/specs/common-structures#destination)
- **[Integer]** [Integer](/docs/specs/common-structures#integer)
- **[OfflineSig]** [OfflineSignature](/docs/specs/common-structures#offlinesignature)
- **[Signature]** [Signature](/docs/specs/common-structures#signature)
- **[SigningPrivateKey]** [SigningPrivateKey](/docs/specs/common-structures#signingprivatekey)
- **[SigningPublicKey]** [SigningPublicKey](/docs/specs/common-structures#signingpublickey)
- **[STREAMING]** [Thư viện Streaming](/docs/api/streaming)
