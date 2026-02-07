---
title: "Đặc tả tạo Tunnel"
description: "Đặc tả xây dựng tunnel ElGamal để tạo tunnel sử dụng telescoping không tương tác."
slug: "tunnel-creation"
aliases: 
category: "Thiết kế"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Tổng quan

LƯU Ý: ĐÃ LỖI THỜI - Đây là đặc tả xây dựng tunnel ElGamal. Xem [tunnel-creation-ecies](/docs/specs/tunnel-creation-ecies/) cho đặc tả xây dựng tunnel X25519.

Tài liệu này chỉ định các chi tiết của các thông điệp xây dựng tunnel được mã hóa được sử dụng để tạo tunnel bằng phương pháp "non-interactive telescoping". Xem tài liệu xây dựng tunnel [TUNNEL-IMPL](/docs/specs/tunnel-implementation/) để có cái nhìn tổng quan về quy trình, bao gồm các phương pháp lựa chọn và sắp xếp peer.

Việc tạo tunnel được thực hiện bằng một thông điệp duy nhất được truyền dọc theo đường đi của các peer trong tunnel, được viết lại tại chỗ, và truyền ngược lại cho người tạo tunnel. Thông điệp tunnel đơn lẻ này được tạo thành từ một số lượng bản ghi biến đổi (tối đa 8) - một cho mỗi peer tiềm năng trong tunnel. Các bản ghi riêng lẻ được mã hóa bất đối xứng (ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)) để chỉ có thể được đọc bởi một peer cụ thể dọc theo đường đi, trong khi một lớp mã hóa đối xứng bổ sung (AES [CRYPTO-AES](/docs/specs/cryptography/#aes)) được thêm vào tại mỗi hop để chỉ lộ ra bản ghi được mã hóa bất đối xứng vào đúng thời điểm thích hợp.

### Số lượng Bản ghi

Không phải tất cả các bản ghi đều phải chứa dữ liệu hợp lệ. Ví dụ, thông điệp xây dựng cho một tunnel 3-hop có thể chứa nhiều bản ghi hơn để ẩn độ dài thực tế của tunnel khỏi các thành viên tham gia. Có hai loại thông điệp xây dựng. Tunnel Build Message ([TBM](/docs/specs/i2np/#struct-TunnelBuild)) ban đầu chứa 8 bản ghi, đủ cho bất kỳ độ dài tunnel thực tế nào. Variable Tunnel Build Message ([VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild)) mới hơn chứa từ 1 đến 8 bản ghi. Người khởi tạo có thể đánh đổi kích thước thông điệp với mức độ che giấu độ dài tunnel mong muốn.

Trong mạng hiện tại, hầu hết các tunnel có độ dài 2 hoặc 3 hop. Triển khai hiện tại sử dụng VTBM 5 bản ghi để xây dựng các tunnel có 4 hop trở xuống, và TBM 8 bản ghi cho các tunnel dài hơn. VTBM 5 bản ghi (khi được phân mảnh, vừa vặn trong ba tunnel message 1KB) giảm lưu lượng mạng và tăng tỷ lệ thành công xây dựng, bởi vì các thông điệp nhỏ hơn ít có khả năng bị loại bỏ.

Thông điệp phản hồi phải cùng loại và độ dài với thông điệp xây dựng.

### Đặc tả Bản ghi Yêu cầu

Cũng được chỉ định trong Đặc tả I2NP [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

Văn bản rõ của bản ghi, chỉ hiển thị cho hop được yêu cầu:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">tunnel ID to receive messages as, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4-35</td><td style="border:1px solid var(--color-border); padding:0.6rem;">local router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">36-39</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next tunnel ID, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">40-71</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">72-103</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel layer key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">104-135</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel IV key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">136-167</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">168-183</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply IV</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">184</td><td style="border:1px solid var(--color-border); padding:0.6rem;">flags</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">185-188</td><td style="border:1px solid var(--color-border); padding:0.6rem;">request time (in hours since the epoch, rounded down)</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">189-192</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next message ID</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">193-221</td><td style="border:1px solid var(--color-border); padding:0.6rem;">uninterpreted / random padding</td></tr>
</tbody>
</table>
Các trường tunnel ID tiếp theo và hash danh tính router tiếp theo được sử dụng để xác định hop tiếp theo trong tunnel, tuy nhiên đối với điểm cuối tunnel outbound, chúng xác định nơi thông điệp phản hồi tạo tunnel đã được viết lại sẽ được gửi đến. Ngoài ra, message ID tiếp theo xác định message ID mà thông điệp (hoặc phản hồi) sẽ sử dụng.

Khóa lớp tunnel, khóa tunnel IV, khóa phản hồi, và IV phản hồi đều là các giá trị ngẫu nhiên 32-byte được tạo bởi người tạo, chỉ sử dụng trong bản ghi yêu cầu xây dựng này.

Trường flags chứa các thông tin sau (thứ tự bit: 76543210, bit 7 là MSB):

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages from anyone</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages to anyone, and send the reply to the specified next hop in a Tunnel Build Reply Message</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5-0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Undefined, must set to 0 for compatibility with future options</td></tr>
</tbody>
</table>
Bit 7 cho biết hop sẽ là một inbound gateway (IBGW). Bit 6 cho biết hop sẽ là một outbound endpoint (OBEP). Nếu không có bit nào được đặt, hop sẽ là một participant trung gian. Cả hai không thể được đặt cùng lúc.

#### Tạo Bản Ghi Yêu Cầu

Mỗi hop nhận một Tunnel ID ngẫu nhiên, khác không. Các Tunnel ID hiện tại và hop tiếp theo được điền vào. Mỗi bản ghi nhận một tunnel IV key ngẫu nhiên, reply IV, layer key, và reply key.

#### Mã hóa Bản ghi Yêu cầu

Bản ghi cleartext đó được mã hóa ElGamal 2048 [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) bằng khóa mã hóa công khai của hop và được định dạng thành bản ghi 528 byte:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">First 16 bytes of the SHA-256 of the current hop's router identity</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">16-527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal-2048 encrypted request record</td></tr>
</tbody>
</table>
Trong bản ghi mã hóa 512-byte, dữ liệu ElGamal chứa các byte từ 1-256 và 258-513 của khối mã hóa ElGamal 514-byte [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). Hai byte đệm từ khối (các byte zero tại vị trí 0 và 257) được loại bỏ.

Vì cleartext sử dụng toàn bộ trường, không cần thêm padding nào ngoài `SHA256(cleartext) + cleartext`.

Mỗi bản ghi 528-byte sau đó được mã hóa lặp lại (sử dụng giải mã AES, với reply key và reply IV cho từng hop) để danh tính router chỉ ở dạng cleartext cho hop được đề cập.

### Xử lý và Mã hóa Hop

Khi một hop nhận được TunnelBuildMessage, nó sẽ tìm kiếm qua các record được chứa bên trong để tìm một record bắt đầu bằng identity hash của chính mình (được cắt bớt xuống còn 16 byte). Sau đó nó giải mã khối ElGamal từ record đó và lấy ra cleartext được bảo vệ. Tại thời điểm này, chúng đảm bảo rằng yêu cầu tunnel không phải là bản trùng lặp bằng cách đưa AES-256 reply key vào Bloom filter. Các bản trùng lặp hoặc yêu cầu không hợp lệ sẽ bị loại bỏ. Các record không được đóng dấu với giờ hiện tại, hoặc giờ trước đó nếu ngay sau đầu giờ, phải được loại bỏ. Ví dụ, lấy giờ trong timestamp, chuyển đổi thành thời gian đầy đủ, sau đó nếu nó chậm hơn 65 phút hoặc nhanh hơn 5 phút so với thời gian hiện tại, thì nó không hợp lệ. Bloom filter phải có thời hạn ít nhất một giờ (cộng thêm vài phút, để cho phép sai lệch đồng hồ), để các record trùng lặp trong giờ hiện tại không bị từ chối bởi việc kiểm tra hour timestamp trong record, sẽ bị từ chối bởi bộ lọc.

Sau khi quyết định có đồng ý tham gia vào tunnel hay không, họ thay thế bản ghi đã chứa yêu cầu bằng một khối phản hồi được mã hóa. Tất cả các bản ghi khác được mã hóa AES-256 [CRYPTO-AES](/docs/specs/cryptography/#aes) với reply key và IV đi kèm. Mỗi bản ghi được mã hóa AES/CBC riêng biệt với cùng reply key và reply IV. Chế độ CBC không được tiếp tục (nối chuỗi) qua các bản ghi.

Mỗi hop chỉ biết phản hồi của chính nó. Nếu nó đồng ý, nó sẽ duy trì tunnel cho đến khi hết hạn, ngay cả khi nó sẽ không được sử dụng, vì nó không thể biết liệu tất cả các hop khác có đồng ý hay không.

#### Đặc tả Bản ghi Phản hồi

Sau khi hop hiện tại đọc bản ghi của họ, họ thay thế nó bằng một bản ghi phản hồi nêu rõ liệu họ có đồng ý tham gia vào tunnel hay không, và nếu không, họ phân loại lý do từ chối. Đây đơn giản là một giá trị 1 byte, với 0x0 có nghĩa là họ đồng ý tham gia vào tunnel, và các giá trị cao hơn có nghĩa là mức độ từ chối cao hơn.

Các mã từ chối sau được định nghĩa:

- TUNNEL_REJECT_PROBABALISTIC_REJECT = 10
- TUNNEL_REJECT_TRANSIENT_OVERLOAD = 20
- TUNNEL_REJECT_BANDWIDTH = 30
- TUNNEL_REJECT_CRIT = 50

Để ẩn các nguyên nhân khác, chẳng hạn như tắt router, khỏi các peer, triển khai hiện tại sử dụng TUNNEL_REJECT_BANDWIDTH cho hầu hết tất cả các từ chối.

Phản hồi được mã hóa bằng khóa phiên AES được gửi đến nó trong khối mã hóa, được đệm với 495 byte dữ liệu ngẫu nhiên để đạt kích thước bản ghi đầy đủ. Phần đệm được đặt trước byte trạng thái:

`AES-256-CBC(SHA-256(padding+status) + padding + status, key, IV)`

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-31</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SHA-256 of bytes 32-527</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">32-526</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Random padding</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Reply value</td></tr>
</tbody>
</table>
Điều này cũng được mô tả trong đặc tả I2NP [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

### Chuẩn Bị Thông Điệp Xây Dựng Tunnel

Khi xây dựng một Tunnel Build Message mới, tất cả các Build Request Records phải được xây dựng trước và mã hóa bất đối xứng bằng ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). Mỗi record sau đó được giải mã phòng ngừa với các reply keys và IVs của các hops trước đó trong đường dẫn, sử dụng AES [CRYPTO-AES](/docs/specs/cryptography/#aes). Việc giải mã đó nên được chạy theo thứ tự ngược lại để dữ liệu được mã hóa bất đối xứng sẽ hiển thị rõ ràng tại hop đúng sau khi hop tiền nhiệm của nó mã hóa dữ liệu.

Các bản ghi dư thừa không cần thiết cho các yêu cầu riêng lẻ được người tạo đơn giản là điền bằng dữ liệu ngẫu nhiên.

### Giao Nhận Thông Điệp Xây Dựng Tunnel

Đối với tunnel gửi đi, việc phân phối được thực hiện trực tiếp từ người tạo tunnel đến hop đầu tiên, đóng gói TunnelBuildMessage như thể người tạo chỉ là một hop khác trong tunnel. Đối với tunnel nhận vào, việc phân phối được thực hiện thông qua một tunnel gửi đi hiện có. Tunnel gửi đi thường từ cùng một pool với tunnel mới đang được xây dựng. Nếu không có tunnel gửi đi nào khả dụng trong pool đó, một tunnel khám phá gửi đi sẽ được sử dụng. Khi khởi động, khi chưa có tunnel khám phá gửi đi nào, một tunnel gửi đi giả 0-hop sẽ được sử dụng.

### Xử lý Endpoint Tin nhắn Xây dựng Tunnel

Đối với việc tạo một outbound tunnel, khi yêu cầu đến một outbound endpoint (được xác định bởi cờ 'allow messages to anyone'), hop được xử lý như bình thường, mã hóa một phản hồi thay cho bản ghi và mã hóa tất cả các bản ghi khác, nhưng vì không có 'next hop' để chuyển tiếp TunnelBuildMessage đến, thay vào đó nó đặt các bản ghi phản hồi đã mã hóa vào một TunnelBuildReplyMessage ([TBRM](/docs/specs/i2np/#struct-TunnelBuildReply)) hoặc VariableTunnelBuildReplyMessage ([VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply)) (loại thông điệp và số lượng bản ghi phải khớp với yêu cầu) và gửi nó đến reply tunnel được chỉ định trong bản ghi yêu cầu. Reply tunnel đó chuyển tiếp Tunnel Build Reply Message trở lại cho người tạo tunnel, giống như bất kỳ thông điệp nào khác [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation). Người tạo tunnel sau đó xử lý nó, như mô tả bên dưới.

Tunnel trả lời được người tạo lựa chọn như sau: Thông thường đó là một tunnel đến từ cùng pool với tunnel đi mới đang được xây dựng. Nếu không có tunnel đến nào khả dụng trong pool đó, một tunnel thám hiểm đến sẽ được sử dụng. Khi khởi động, khi chưa có tunnel thám hiểm đến nào tồn tại, một tunnel đến giả 0-hop sẽ được sử dụng.

Để tạo một inbound tunnel, khi yêu cầu đến inbound endpoint (còn được gọi là tunnel creator), không cần tạo một Tunnel Build Reply Message rõ ràng, và router sẽ xử lý từng phản hồi như sau.

### Xử lý Thông điệp Phản hồi Xây dựng Tunnel

Để xử lý các bản ghi phản hồi, người tạo chỉ cần giải mã AES từng bản ghi riêng lẻ, sử dụng reply key và IV của mỗi hop trong tunnel sau peer (theo thứ tự ngược lại). Điều này sẽ tiết lộ phản hồi xác định liệu họ có đồng ý tham gia vào tunnel hay tại sao họ từ chối. Nếu tất cả đều đồng ý, tunnel được coi là đã tạo thành công và có thể sử dụng ngay lập tức, nhưng nếu có ai từ chối, tunnel sẽ bị loại bỏ.

Các thỏa thuận và từ chối được ghi nhận trong hồ sơ của từng peer [PEER-SELECTION](/docs/overview/tunnel-routing/), để sử dụng trong các đánh giá tương lai về khả năng tunnel của peer.

## Lịch sử và Ghi chú

Chiến lược này được đưa ra trong một cuộc thảo luận trên danh sách gửi thư I2P giữa Michael Rogers, Matthew Toseland (toad), và jrandom về cuộc tấn công predecessor. Xem [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html), [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html). Nó được giới thiệu trong phiên bản 0.6.1.10 vào ngày 2006-02-16, đây là lần cuối cùng một thay đổi không tương thích ngược được thực hiện trong I2P.

Ghi chú:

- Thiết kế này không ngăn chặn hai peer thù địch trong một tunnel gắn thẻ một hoặc nhiều bản ghi yêu cầu hoặc phản hồi để phát hiện rằng chúng đang trong cùng một tunnel, nhưng việc làm như vậy có thể được phát hiện bởi người tạo tunnel khi đọc phản hồi, khiến tunnel bị đánh dấu là không hợp lệ.
- Thiết kế này không bao gồm một bằng chứng công việc trên phần mã hóa bất đối xứng, mặc dù hash nhận dạng 16 byte có thể được cắt làm đôi với phần sau được thay thế bằng một hàm hashcash với chi phí lên đến 2^64.
- Thiết kế này một mình không ngăn chặn hai peer thù địch trong một tunnel sử dụng thông tin thời gian để xác định xem chúng có trong cùng một tunnel hay không. Việc sử dụng phân phối yêu cầu theo lô và đồng bộ có thể giúp ích (nhóm các yêu cầu thành lô và gửi chúng vào phút (đồng bộ ntp)). Tuy nhiên, làm như vậy cho phép các peer 'gắn thẻ' các yêu cầu bằng cách trì hoãn chúng và phát hiện sự trì hoãn sau đó trong tunnel, mặc dù có lẽ việc loại bỏ các yêu cầu không được phân phối trong một cửa sổ nhỏ sẽ có hiệu quả (mặc dù làm như vậy sẽ yêu cầu mức độ đồng bộ đồng hồ cao). Hoặc có thể, các hop riêng lẻ có thể chèn một độ trễ ngẫu nhiên trước khi chuyển tiếp yêu cầu?
- Có phương pháp gắn thẻ yêu cầu nào không gây tử vong không?
- Dấu thời gian với độ phân giải một giờ được sử dụng để ngăn chặn replay. Ràng buộc này không được thực thi cho đến phiên bản 0.9.16.

## Công việc tương lai

- Trong triển khai hiện tại, bên khởi tạo để trống một bản ghi cho chính nó. Do đó một thông điệp có n bản ghi chỉ có thể xây dựng một tunnel có n-1 hops. Điều này có vẻ cần thiết cho các inbound tunnel (nơi hop áp chót có thể thấy hash prefix cho hop tiếp theo), nhưng không cần thiết cho các outbound tunnel. Điều này cần được nghiên cứu và xác minh. Nếu có thể sử dụng bản ghi còn lại mà không làm tổn hại tính ẩn danh, chúng ta nên làm như vậy.
- Phân tích sâu hơn về các cuộc tấn công tagging và timing có thể xảy ra được mô tả trong các ghi chú trên.
- Chỉ sử dụng VTBM; không chọn các peer cũ không hỗ trợ nó.
- Build Request Record không chỉ định thời gian sống hoặc thời điểm hết hạn của tunnel; mỗi hop sẽ làm hết hạn tunnel sau 10 phút, đây là một hằng số cố định trên toàn mạng. Chúng ta có thể sử dụng một bit trong trường flag và lấy 4 (hoặc 8) byte từ padding để chỉ định thời gian sống hoặc thời điểm hết hạn. Bên yêu cầu chỉ chỉ định tùy chọn này nếu tất cả các bên tham gia đều hỗ trợ nó.

## Tài liệu tham khảo

- [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) - Đặc tả BuildRequestRecord
- [CRYPTO-AES](/docs/specs/cryptography/#aes) - Mã hóa AES
- [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) - Mã hóa ElGamal
- [HASHING-IT-OUT](http://www-users.cs.umn.edu/~hopper/hashing_it_out.pdf)
- [PEER-SELECTION](/docs/overview/tunnel-routing/)
- [PREDECESSOR](http://forensics.umass.edu/pubs/wright-tissec.pdf)
- [PREDECESSOR-2008](http://forensics.umass.edu/pubs/wright.tissec.2008.pdf)
- [TBM](/docs/specs/i2np/#struct-TunnelBuild) - TunnelBuildMessage
- [TBRM](/docs/specs/i2np/#struct-TunnelBuildReply) - TunnelBuildReplyMessage
- [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html)
- [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html)
- [TUNNEL-IMPL](/docs/specs/tunnel-implementation/)
- [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation)
- [VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild) - VariableTunnelBuildMessage
- [VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply) - VariableTunnelBuildReplyMessage
