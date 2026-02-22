---
title: "Đặc tả SSU2"
description: "Giao thức Truyền tải UDP Bán tin cậy Bảo mật Phiên bản 2"
slug: "ssu2"
category: "Giao thức vận chuyển"
lastUpdated: "2025-04"
accurateFor: "0.9.65"
---

## Trạng thái

Về cơ bản đã hoàn thành. Xem [Prop159](/proposals/159-ssu2) để biết thêm thông tin nền và mục tiêu, bao gồm phân tích bảo mật, mô hình mối đe dọa, đánh giá bảo mật và các vấn đề của SSU 1, cũng như các trích đoạn từ đặc tả QUIC.

Kế hoạch triển khai:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Feature</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Testing (not default)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Enabled by default</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Local test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-03</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test in-net</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze basic protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Basic Session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address Validation (Retry)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Fragmented RI in handshake</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze extended protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Enable for random 2%</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Validation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Connection Migration</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Immediate ACK flag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Key Rotation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2023-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (i2pd)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (Java I2P)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.61 2023-12</td></tr>
  </tbody>
</table>
Session cơ bản bao gồm giai đoạn bắt tay và truyền dữ liệu. Giao thức mở rộng bao gồm chuyển tiếp và kiểm tra peer.

## Tổng quan

Đặc tả này định nghĩa một giao thức thỏa thuận khóa được xác thực để cải thiện khả năng chống lại các hình thức nhận dạng tự động và tấn công khác nhau của [SSU](/docs/transport/ssu).

Giống như các phương thức vận chuyển khác của I2P, SSU2 được định nghĩa cho việc vận chuyển point-to-point (router-to-router) các thông điệp I2NP. Nó không phải là một đường ống dữ liệu đa mục đích. Giống như [SSU](/docs/transport/ssu), nó cũng cung cấp hai dịch vụ bổ sung: Relaying để vượt qua NAT, và Peer Testing để xác định khả năng tiếp cận đầu vào. Nó cũng cung cấp một dịch vụ thứ ba, không có trong SSU, cho việc chuyển đổi kết nối khi một peer thay đổi IP hoặc port.

## Tổng Quan Thiết Kế

### Tóm tắt

Chúng tôi dựa vào một số giao thức hiện có, cả trong I2P và các tiêu chuẩn bên ngoài, để lấy cảm hứng, hướng dẫn và tái sử dụng mã:

- Mô hình mối đe dọa: Từ NTCP2 [NTCP2](/docs/specs/ntcp2), với các mối đe dọa bổ sung đáng kể liên quan đến giao thức UDP như được phân tích bởi QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Lựa chọn mật mã: Từ [NTCP2](/docs/specs/ntcp2).
- Handshake: Noise XK từ [NTCP2](/docs/specs/ntcp2) và [NOISE](https://noiseprotocol.org/noise.html). Có thể đơn giản hóa đáng kể NTCP2 do việc đóng gói (ranh giới thông điệp vốn có) được cung cấp bởi UDP.
- Che giấu khóa tạm thời handshake: Được điều chỉnh từ [NTCP2](/docs/specs/ntcp2) nhưng sử dụng ChaCha20 từ [ECIES](/docs/specs/ecies) thay vì AES.
- Header gói tin: Được điều chỉnh từ WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) và QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Che giấu header gói tin: Được điều chỉnh từ [NTCP2](/docs/specs/ntcp2) nhưng sử dụng ChaCha20 từ [ECIES](/docs/specs/ecies) thay vì AES.
- Bảo vệ header gói tin: Được điều chỉnh từ QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) và [Nonces](https://eprint.iacr.org/2019/624.pdf)
- Header được sử dụng như dữ liệu liên kết AEAD như trong [ECIES](/docs/specs/ecies).
- Đánh số gói tin: Được điều chỉnh từ WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) và QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Thông điệp: Được điều chỉnh từ [SSU](/docs/transport/ssu)
- Phân mảnh I2NP: Được điều chỉnh từ [SSU](/docs/transport/ssu)
- Relay và Kiểm tra Peer: Được điều chỉnh từ [SSU](/docs/transport/ssu)
- Chữ ký của dữ liệu Relay và Peer Test: Từ đặc tả cấu trúc chung [Common](/docs/specs/common-structures)
- Định dạng khối: Từ [NTCP2](/docs/specs/ntcp2) và [ECIES](/docs/specs/ecies).
- Padding và tùy chọn: Từ [NTCP2](/docs/specs/ntcp2) và [ECIES](/docs/specs/ecies).
- Acks, nacks: Được điều chỉnh từ QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000).
- Điều khiển luồng: TBD

Không có các nguyên thủy mật mã mới nào chưa từng được sử dụng trong I2P trước đây.

### Đảm Bảo Phân Phối

Giống như các giao thức vận chuyển khác của I2P là NTCP, NTCP2, và SSU 1, giao thức vận chuyển này không phải là một phương tiện tổng quát để phân phối một luồng byte theo thứ tự. Nó được thiết kế để vận chuyển các thông điệp I2NP. Không có sự trừu tượng hóa "stream" nào được cung cấp.

Ngoài ra, đối với SSU, nó chứa các tiện ích bổ sung để NAT traversal được hỗ trợ bởi peer và kiểm tra khả năng tiếp cận (kết nối đến).

Đối với SSU 1, nó KHÔNG cung cấp khả năng giao hàng theo thứ tự các thông điệp I2NP. Nó cũng không đảm bảo việc giao hàng các thông điệp I2NP. Vì lý do hiệu quả, hoặc do việc giao hàng không theo thứ tự của các datagram UDP hoặc mất mát các datagram đó, các thông điệp I2NP có thể được giao đến đầu xa không theo thứ tự, hoặc có thể không được giao hàng chút nào. Một thông điệp I2NP có thể được truyền lại nhiều lần nếu cần thiết, nhưng việc giao hàng cuối cùng có thể thất bại mà không gây ra việc ngắt kết nối hoàn toàn. Ngoài ra, các thông điệp I2NP mới có thể tiếp tục được gửi ngay cả khi việc truyền lại (khôi phục mất mát) đang diễn ra cho các thông điệp I2NP khác.

Giao thức này KHÔNG ngăn chặn hoàn toàn việc gửi trùng lặp các tin nhắn I2NP. Router nên thực thi việc hết hạn I2NP và sử dụng bộ lọc Bloom hoặc cơ chế khác dựa trên ID tin nhắn I2NP. Xem phần I2NP Message Duplication bên dưới.

### Khung Giao Thức Noise

Đặc tả này cung cấp các yêu cầu dựa trên Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (Phiên bản 33, 2017-10-04). Noise có các thuộc tính tương tự như giao thức Station-To-Station [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol), là cơ sở cho giao thức [SSU](/docs/transport/ssu). Theo thuật ngữ của Noise, Alice là bên khởi tạo và Bob là bên phản hồi.

SSU2 dựa trên giao thức Noise Noise_XK_25519_ChaChaPoly_SHA256. (Định danh thực tế cho hàm dẫn xuất khóa ban đầu là "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256" để chỉ ra các mở rộng I2P - xem phần KDF 1 bên dưới)

LƯU Ý: Định danh này khác với định danh được sử dụng cho NTCP2, vì cả ba thông điệp handshake đều sử dụng header làm dữ liệu liên kết.

Giao thức Noise này sử dụng các thành phần cơ bản sau:

- Handshake Pattern: XK Alice truyền khóa của cô ấy cho Bob (X) Alice đã biết khóa tĩnh của Bob (K)
- DH Function: X25519 X25519 DH với độ dài khóa 32 byte như được chỉ định trong [RFC-7748](https://tools.ietf.org/html/rfc7748).
- Cipher Function: ChaChaPoly AEAD_CHACHA20_POLY1305 như được chỉ định trong [RFC-7539](https://tools.ietf.org/html/rfc7539) phần 2.8. 12 byte nonce, với 4 byte đầu tiên được đặt về không.
- Hash Function: SHA256 Hash tiêu chuẩn 32-byte, đã được sử dụng rộng rãi trong I2P.

### Bổ sung vào Framework

Đặc tả này định nghĩa các cải tiến sau cho Noise_XK_25519_ChaChaPoly_SHA256. Những cải tiến này thường tuân theo các hướng dẫn trong phần 13 của [NOISE](https://noiseprotocol.org/noise.html).

1) Các thông điệp bắt tay (Session Request, Created, Confirmed) bao gồm một header 16 hoặc 32 byte. 2) Các header cho các thông điệp bắt tay (Session Request, Created, Confirmed) được sử dụng làm đầu vào cho mixHash() trước khi mã hóa/giải mã để liên kết các header với thông điệp. 3) Các header được mã hóa và bảo vệ. 4) Các khóa tạm thời dạng cleartext được che giấu bằng mã hóa ChaCha20 sử dụng khóa và IV đã biết. Điều này nhanh hơn so với elligator2. 5) Định dạng payload được định nghĩa cho thông điệp 1, 2, và giai đoạn dữ liệu. Tất nhiên, điều này không được định nghĩa trong Noise.

Giai đoạn dữ liệu sử dụng mã hóa tương tự nhưng không tương thích với giai đoạn dữ liệu của Noise.

## Định nghĩa

Chúng tôi định nghĩa các hàm sau tương ứng với các khối xây dựng mật mã được sử dụng.

ZEROLEN

:   mảng byte có độ dài bằng không

H(p, d)

:   Hàm băm SHA-256 nhận một chuỗi cá nhân hóa p và dữ liệu d, và tạo ra đầu ra có độ dài 32 byte. Như được định nghĩa trong [NOISE](https://noiseprotocol.org/noise.html). || bên dưới có nghĩa là nối thêm.

    Use SHA-256 as follows:

        H(p, d) := SHA-256(p || d)

MixHash(d)

:   Hàm băm SHA-256 nhận vào một hash trước đó h và dữ liệu mới d, và tạo ra đầu ra có độ dài 32 byte. || bên dưới có nghĩa là nối thêm.

    Use SHA-256 as follows:

        MixHash(d) := h = SHA-256(h || d)

STREAM

:   ChaCha20/Poly1305 AEAD như được quy định trong [RFC-7539](https://tools.ietf.org/html/rfc7539). S_KEY_LEN = 32 và S_IV_LEN = 12.

    ENCRYPT(k, n, plaintext, ad)

    :   Encrypts plaintext using the cipher key k, and nonce n which MUST be unique for the key k. Associated data ad is optional. Returns a ciphertext that is the size of the plaintext + 16 bytes for the HMAC.

        The entire ciphertext must be indistinguishable from random if the key is secret.

    DECRYPT(k, n, ciphertext, ad)

    :   Decrypts ciphertext using the cipher key k, and nonce n. Associated data ad is optional. Returns the plaintext.

DH

:   Hệ thống thỏa thuận khóa công khai X25519. Khóa riêng tư 32 byte, khóa công khai 32 byte, tạo ra đầu ra 32 byte. Nó có các chức năng sau:

    GENERATE_PRIVATE()

    :   Generates a new private key.

    DERIVE_PUBLIC(privkey)

    :   Returns the public key corresponding to the given private key.

    DH(privkey, pubkey)

    :   Generates a shared secret from the given private and public keys.

HKDF(salt, ikm, info, n)

:   Một hàm dẫn xuất khóa mật mã nhận vào một số vật liệu khóa đầu vào ikm (nên có entropy tốt nhưng không bắt buộc phải là chuỗi ngẫu nhiên đồng đều), một salt có độ dài 32 byte, và một giá trị 'info' cụ thể theo ngữ cảnh, rồi tạo ra đầu ra n byte phù hợp để sử dụng làm vật liệu khóa.

    Use HKDF as specified in [RFC-5869](https://tools.ietf.org/html/rfc5869), using the HMAC hash function SHA-256 as specified in [RFC-2104](https://tools.ietf.org/html/rfc2104). This means that SALT_LEN is 32 bytes max.

MixKey(d)

:   Sử dụng HKDF() với chainKey trước đó và dữ liệu mới d, và đặt chainKey mới và k. Như được định nghĩa trong [NOISE](https://noiseprotocol.org/noise.html).

    Use HKDF as follows:

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]

## Tin nhắn

Mỗi datagram UDP chứa chính xác một thông điệp. Độ dài của datagram (sau các header IP và UDP) là độ dài của thông điệp. Padding, nếu có, được chứa trong một khối padding bên trong thông điệp. Trong tài liệu này, chúng tôi sử dụng các thuật ngữ "datagram" và "packet" hầu như có thể thay thế cho nhau. Mỗi datagram (hoặc packet) chứa một thông điệp duy nhất (khác với QUIC, trong đó một datagram có thể chứa nhiều QUIC packet). "Packet header" là phần sau header IP/UDP.

Ngoại lệ: Thông điệp Session Confirmed là duy nhất ở chỗ nó có thể được phân mảnh trên nhiều gói tin. Xem phần Session Confirmed Fragmentation bên dưới để biết thêm thông tin.

Tất cả thông điệp SSU2 có độ dài tối thiểu là 40 byte. Bất kỳ thông điệp nào có độ dài từ 1-39 byte đều không hợp lệ. Tất cả thông điệp SSU2 có độ dài nhỏ hơn hoặc bằng 1472 (IPv4) hoặc 1452 (IPv6) byte. Định dạng thông điệp dựa trên thông điệp Noise, với các sửa đổi cho việc đóng khung và tính không thể phân biệt. Các triển khai sử dụng thư viện Noise tiêu chuẩn phải tiền xử lý các thông điệp nhận được thành định dạng thông điệp Noise tiêu chuẩn. Tất cả các trường được mã hóa đều là ciphertext AEAD.

Các thông điệp sau đây được định nghĩa:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Encr. Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionRequest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionCreated</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionConfirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">PeerTest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">HolePunch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
  </tbody>
</table>
### Thiết Lập Phiên

Trình tự thiết lập tiêu chuẩn, khi Alice có một token hợp lệ đã nhận trước đó từ Bob, như sau:

```
Alice                           Bob

SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Khi Alice không có token hợp lệ, trình tự thiết lập như sau:

```
Alice                           Bob

TokenRequest --------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Khi Alice nghĩ rằng cô ấy có một token hợp lệ, nhưng Bob từ chối nó (có thể vì Bob đã khởi động lại), trình tự thiết lập như sau:

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Bob có thể từ chối một Session hoặc Token Request bằng cách trả lời với thông báo Retry chứa khối Termination với mã lý do. Dựa trên mã lý do, Alice không nên thử yêu cầu khác trong một khoảng thời gian:

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry containing a Termination block

or

TokenRequest --------------------->
<---------------------------  Retry containing a Termination block
```
Sử dụng thuật ngữ Noise, trình tự thiết lập và dữ liệu như sau: (Thuộc tính Bảo mật Payload)

```
XK(s, rs):           Authentication   Confidentiality
  <- s
  ...
  -> e, es                  0                2
  <- e, ee                  2                1
  -> s, se                  2                5
  <-                        2                5
```
Khi một phiên làm việc đã được thiết lập, Alice và Bob có thể trao đổi các thông điệp Data.

### Tiêu đề Gói tin

Tất cả các gói tin đều bắt đầu bằng một header được làm rối (mã hóa). Có hai loại header, dài và ngắn. Lưu ý rằng 13 byte đầu tiên (Destination Connection ID, packet number, và type) đều giống nhau cho tất cả các header.

#### Header Dài

Header dài có độ dài 32 byte. Nó được sử dụng trước khi một phiên được tạo, cho Token Request, SessionRequest, SessionCreated, và Retry. Nó cũng được sử dụng cho các thông điệp Peer Test và Hole Punch ngoài phiên.

Trước khi mã hóa header:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 0, 1, 7, 9, 10, or 11

ver :: The protocol version, equal to 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: 8 bytes, unsigned big endian integer

Token :: 8 bytes, unsigned big endian integer
```
#### Tiêu Đề Ngắn

Header ngắn có độ dài 16 byte. Nó được sử dụng cho các thông điệp Session Created và Data. Các thông điệp không được xác thực như Session Request, Retry, và Peer Test sẽ luôn sử dụng header dài.

16 byte là bắt buộc, vì bên nhận phải giải mã 16 byte đầu tiên để lấy loại thông điệp, và sau đó phải giải mã thêm 16 byte nữa nếu đó thực sự là header dài, như được chỉ ra bởi loại thông điệp.

Đối với Session Confirmed, trước khi mã hóa header:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, all zeros

type :: The message type = 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility
```
Xem phần Session Confirmed Fragmentation bên dưới để biết thêm thông tin về trường frag.

Đối với các thông điệp Data, trước khi mã hóa header:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|flag|moreflags|
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 6

flag :: 1 byte flags:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-1: unused, set to 0 for future compatibility
       bits 0: when set to 1, immediate ack requested

moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### Đánh Số ID Kết Nối

Connection ID phải được tạo ngẫu nhiên. Source ID và Destination ID KHÔNG được giống nhau, để một kẻ tấn công trên đường truyền không thể bắt và gửi lại packet cho người gửi ban đầu trông có vẻ hợp lệ. KHÔNG sử dụng bộ đếm để tạo connection ID, để một kẻ tấn công trên đường truyền không thể tạo ra packet trông có vẻ hợp lệ.

Không giống như trong QUIC, chúng tôi không thay đổi connection ID trong hoặc sau quá trình handshake, ngay cả sau thông điệp Retry. Các ID này vẫn không đổi từ thông điệp đầu tiên (Token Request hoặc Session Request) đến thông điệp cuối cùng (Data với Termination). Ngoài ra, connection ID không thay đổi trong hoặc sau path challenge hoặc connection migration.

Cũng khác với QUIC là các connection ID trong header luôn được mã hóa header. Xem bên dưới.

#### Đánh Số Gói Tin

Nếu không có khối First Packet Number nào được gửi trong quá trình handshake, các gói tin sẽ được đánh số trong một phiên duy nhất, cho mỗi hướng, bắt đầu từ 0, đến tối đa (2**32 -1). Một phiên phải được kết thúc và tạo phiên mới, trước khi số lượng gói tin tối đa được gửi đi.

Nếu một khối First Packet Number được gửi trong quá trình handshake, các gói tin sẽ được đánh số trong một phiên duy nhất, cho hướng đó, bắt đầu từ số gói tin đó. Số gói tin có thể quay vòng trong suốt phiên. Khi tối đa 2**32 gói tin đã được gửi, việc quay vòng số gói tin trở lại số gói tin đầu tiên, phiên đó không còn hợp lệ. Một phiên phải được kết thúc, và một phiên mới được tạo, trước khi số gói tin tối đa được gửi.

TODO xoay khóa, giảm số gói tối đa?

Các gói handshake được xác định là bị mất sẽ được truyền lại toàn bộ, với header giống hệt nhau bao gồm cả packet number. Các thông điệp handshake Session Request, Session Created, và Session Confirmed PHẢI được truyền lại với cùng packet number và nội dung mã hóa giống hệt nhau, để cùng một chained hash sẽ được sử dụng để mã hóa phản hồi. Thông điệp Retry không bao giờ được truyền.

Các gói tin pha dữ liệu được xác định là bị mất sẽ không bao giờ được truyền lại toàn bộ (ngoại trừ việc kết thúc, xem bên dưới). Điều này cũng áp dụng cho các khối được chứa trong các gói tin bị mất. Thay vào đó, thông tin có thể được mang trong các khối sẽ được gửi lại trong các gói tin mới khi cần thiết. Các Data Packet không bao giờ được truyền lại với cùng một số thứ tự gói tin. Bất kỳ việc truyền lại nội dung gói tin nào (cho dù nội dung có giữ nguyên hay không) đều phải sử dụng số thứ tự gói tin chưa sử dụng tiếp theo.

Việc truyền lại một gói tin nguyên vẹn không thay đổi như cũ, với cùng số hiệu gói tin, không được phép vì một số lý do. Để hiểu rõ hơn, xem QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) mục 12.3.

- Việc lưu trữ các gói tin để truyền lại là không hiệu quả
- Một gói tin mới trông khác đối với người quan sát trên đường truyền, không thể biết được đó là gói tin được truyền lại
- Một gói tin mới sẽ được gửi kèm với khối ack đã cập nhật, không phải khối ack cũ
- Bạn chỉ truyền lại những gì cần thiết. một số phân đoạn có thể đã được truyền lại một lần và đã được xác nhận
- Bạn có thể nhét vào mỗi gói tin được truyền lại nhiều như bạn cần nếu còn nhiều dữ liệu đang chờ
- Các endpoint theo dõi tất cả các gói tin riêng lẻ với mục đích phát hiện trùng lặp có nguy cơ tích lũy trạng thái quá mức. Dữ liệu cần thiết để phát hiện trùng lặp có thể được giới hạn bằng cách duy trì một số gói tin tối thiểu mà dưới đó tất cả các gói tin sẽ bị loại bỏ ngay lập tức.
- Phương án này linh hoạt hơn nhiều

Các gói tin mới được sử dụng để mang thông tin được xác định là đã bị mất. Nói chung, thông tin được gửi lại khi một gói tin chứa thông tin đó được xác định là đã bị mất, và việc gửi sẽ dừng lại khi một gói tin chứa thông tin đó được xác nhận.

Ngoại lệ: Một gói tin pha dữ liệu chứa khối Termination có thể, nhưng không bắt buộc, được truyền lại toàn bộ nguyên trạng. Xem phần Session Termination bên dưới.

Các gói tin sau đây chứa một số gói tin ngẫu nhiên sẽ được bỏ qua:

- Yêu cầu Phiên
- Phiên đã Tạo
- Yêu cầu Token
- Thử lại
- Kiểm tra Peer
- Hole Punch

Đối với Alice, việc đánh số packet gửi đi bắt đầu từ 0 với Session Confirmed. Đối với Bob, việc đánh số packet gửi đi bắt đầu từ 0 với packet Data đầu tiên, packet này sẽ là một ACK của Session Confirmed. Các số hiệu packet trong một ví dụ bắt tay chuẩn sẽ là:

```
Alice                           Bob

SessionRequest (r)    ------------>
<-------------   SessionCreated (r)
SessionConfirmed (0)  ------------>
<-------------             Data (0) (Ack-only)
Data (1)              ------------> (May be sent before Ack is received)
<-------------             Data (1)
Data (2)              ------------>
Data (3)              ------------>
Data (4)              ------------>
<-------------             Data (2)

r = random packet number (ignored)
Token Request, Retry, and Peer Test
also have random packet numbers.
```
Bất kỳ việc truyền lại nào của các thông điệp handshake (SessionRequest, SessionCreated, hoặc SessionConfirmed) phải được gửi lại không thay đổi, với cùng số thứ tự packet. Không sử dụng các ephemeral key khác nhau hoặc thay đổi payload khi truyền lại các thông điệp này.

#### Ràng buộc Header

Header (trước khi bị làm mờ và bảo vệ) luôn được bao gồm trong dữ liệu liên quan cho hàm AEAD, để liên kết mã hóa header với dữ liệu.

#### Mã hóa Header

Mã hóa header có một số mục tiêu. Xem phần "Thảo luận bổ sung về DPI" ở trên để hiểu về bối cảnh và các giả định.

- Ngăn chặn DPI trực tuyến xác định giao thức
- Ngăn chặn các mẫu trong một chuỗi thông điệp trong cùng một kết nối, ngoại trừ việc truyền lại handshake
- Ngăn chặn các mẫu trong thông điệp cùng loại trong các kết nối khác nhau
- Ngăn chặn giải mã header handshake mà không biết introduction key được tìm thấy trong netdb
- Ngăn chặn xác định khóa tạm thời X25519 mà không biết introduction key được tìm thấy trong netdb
- Ngăn chặn giải mã số thứ tự và loại gói tin pha dữ liệu bởi bất kỳ kẻ tấn công trực tuyến hoặc ngoại tuyến nào
- Ngăn chặn tiêm các gói handshake hợp lệ bởi người quan sát trên đường truyền hoặc ngoài đường truyền mà không biết introduction key được tìm thấy trong netdb
- Ngăn chặn tiêm các gói dữ liệu hợp lệ bởi người quan sát trên đường truyền hoặc ngoài đường truyền
- Cho phép phân loại nhanh chóng và hiệu quả các gói tin đến
- Cung cấp khả năng chống "thăm dò" để không có phản hồi nào cho Session Request không hợp lệ, hoặc nếu có phản hồi Retry, phản hồi đó không thể xác định được là I2P mà không biết introduction key được tìm thấy trong netdb
- Destination Connection ID không phải là dữ liệu quan trọng, và việc nó có thể được giải mã bởi người quan sát biết introduction key được tìm thấy trong netdb là chấp nhận được
- Số thứ tự gói tin của gói pha dữ liệu là một nonce AEAD và là dữ liệu quan trọng. Nó không được giải mã được bởi người quan sát ngay cả khi biết introduction key được tìm thấy trong netdb. Xem [Nonces](https://eprint.iacr.org/2019/624.pdf).

Các header được mã hóa bằng các khóa đã biết được xuất bản trong network database hoặc được tính toán sau đó. Trong giai đoạn handshake, điều này chỉ để chống DPI, vì khóa là công khai và khóa cùng nonces được sử dụng lại, nên về cơ bản đây chỉ là làm xáo trộn. Lưu ý rằng việc mã hóa header cũng được sử dụng để làm xáo trộn các khóa ephemeral X (trong Session Request) và Y (trong Session Created).

Xem phần Xử lý Gói tin Đến bên dưới để có thêm hướng dẫn.

Các byte 0-15 của tất cả header được mã hóa bằng cách sử dụng sơ đồ bảo vệ header thông qua phép XOR với dữ liệu được tính toán từ các khóa đã biết, sử dụng ChaCha20, tương tự như QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) và [Nonces](https://eprint.iacr.org/2019/624.pdf). Điều này đảm bảo rằng short header đã mã hóa và phần đầu của long header sẽ có vẻ ngẫu nhiên.

Đối với Session Request và Session Created, các byte 16-31 của long header và khóa ephemeral Noise 32-byte được mã hóa bằng ChaCha20. Dữ liệu chưa mã hóa là ngẫu nhiên, vì vậy dữ liệu đã mã hóa sẽ có vẻ ngẫu nhiên.

Đối với Retry, các byte 16-31 của long header được mã hóa bằng ChaCha20. Dữ liệu chưa mã hóa là ngẫu nhiên, vì vậy dữ liệu đã mã hóa sẽ có vẻ ngẫu nhiên.

Không giống như sơ đồ bảo vệ header của QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001), TẤT CẢ các phần của tất cả header, bao gồm cả connection ID đích và nguồn, đều được mã hóa. QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) và [Nonces](https://eprint.iacr.org/2019/624.pdf) chủ yếu tập trung vào việc mã hóa phần "quan trọng" của header, tức là số thứ tự packet (ChaCha20 nonce). Trong khi việc mã hóa session ID làm cho việc phân loại packet đến phức tạp hơn một chút, nó khiến một số cuộc tấn công trở nên khó khăn hơn. QUIC định nghĩa các connection ID khác nhau cho các giai đoạn khác nhau, và cho path challenge và connection migration. Ở đây chúng tôi sử dụng cùng một connection ID xuyên suốt, vì chúng được mã hóa.

Có bảy giai đoạn khóa bảo vệ header:

- Yêu cầu Phiên và Yêu cầu Token
- Phiên Đã Tạo
- Thử lại
- Phiên Đã Xác nhận
- Giai đoạn Dữ liệu
- Kiểm tra Peer
- Hole Punch

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_1</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_2</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Request KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Created KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice/Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See data phase KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 5,7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Hole Punch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
  </tbody>
</table>
Mã hóa header được thiết kế để cho phép phân loại nhanh chóng các gói tin đến, mà không cần các phương pháp phỏng đoán phức tạp hoặc các giải pháp dự phòng. Điều này được thực hiện bằng cách sử dụng cùng một khóa k_header_1 cho hầu hết tất cả các thông điệp đến. Ngay cả khi IP nguồn hoặc cổng của một kết nối thay đổi do thay đổi IP thực tế hoặc hành vi NAT, gói tin vẫn có thể được ánh xạ nhanh chóng đến một phiên với chỉ một lần tra cứu ID kết nối.

Lưu ý rằng Session Created và Retry là những thông điệp DUY NHẤT cần xử lý dự phòng cho k_header_1 để giải mã Connection ID, vì chúng sử dụng intro key của người gửi (Bob). TẤT CẢ các thông điệp khác đều sử dụng intro key của người nhận cho k_header_1. Việc xử lý dự phòng chỉ cần tra cứu các kết nối outbound đang chờ theo IP/port nguồn.

Nếu quá trình xử lý dự phòng theo IP/port nguồn không tìm thấy kết nối outbound đang chờ xử lý, có thể có một số nguyên nhân:

- Không phải là tin nhắn SSU2
- Tin nhắn SSU2 bị hỏng
- Phản hồi bị giả mạo hoặc sửa đổi bởi kẻ tấn công
- Bob có symmetric NAT
- Bob đã thay đổi IP hoặc port trong quá trình xử lý tin nhắn
- Bob đã gửi phản hồi qua một interface khác

Mặc dù có thể thực hiện xử lý dự phòng bổ sung để cố gắng tìm kết nối gửi đi đang chờ xử lý và giải mã connection ID bằng k_header_1 cho kết nối đó, nhưng điều này có lẽ không cần thiết. Nếu Bob gặp vấn đề với NAT hoặc định tuyến gói tin, có lẽ tốt hơn là để kết nối thất bại. Thiết kế này dựa vào việc các endpoint duy trì một địa chỉ ổn định trong suốt quá trình handshake.

Xem phần Xử lý Gói tin Đến bên dưới để biết thêm hướng dẫn.

Xem các phần KDF riêng lẻ bên dưới để biết cách tạo khóa mã hóa header cho giai đoạn đó.

#### KDF Mã hóa Header

```
// incoming encrypted packet
packet = incoming encrypted packet
len = packet.length

// take the next-to-last 12 bytes of the packet
iv = packet[len-24:len-13]
k_header_1 = header encryption key 1
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_1, iv, data)

// encrypt the first part of the header by XORing with the mask
packet[0:7] ^= mask[0:7]

// take the last 12 bytes of the packet
iv = packet[len-12:len-1]
k_header_2 = header encryption key 2
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_2, iv, data)

// encrypt the second part of the header by XORing with the mask
packet[8:15] ^= mask[0:7]


// For Session Request and Session Created only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header and the ephemeral key
packet[16:63] = ChaCha20.encrypt(k_header_2, iv, packet[16:63])


// For Retry, Token Request, Peer Test, and Hole Punch only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header
packet[16:31] = ChaCha20.encrypt(k_header_2, iv, packet[16:31])
```
KDF này sử dụng 24 byte cuối của gói tin làm IV cho hai thao tác ChaCha20. Vì tất cả các gói tin đều kết thúc bằng MAC 16 byte, điều này yêu cầu tất cả payload của gói tin phải có tối thiểu 8 byte. Yêu cầu này cũng được ghi chép thêm trong các phần thông điệp bên dưới.

#### Xác thực Header

Sau khi giải mã 8 byte đầu tiên của header, bên nhận sẽ biết được Destination Connection ID. Từ đó, bên nhận biết phải sử dụng khóa mã hóa header nào cho phần còn lại của header, dựa trên key phase của phiên làm việc.

Giải mã 8 byte tiếp theo của header sẽ tiết lộ loại thông điệp và có thể xác định đó là header ngắn hay dài. Nếu là header dài, bên nhận phải xác thực các trường version và netid. Nếu version != 2, hoặc netid != giá trị mong đợi (thường là 2, trừ trong các mạng thử nghiệm), bên nhận nên bỏ qua thông điệp đó.

### Tính toàn vẹn gói tin

Tất cả thông điệp đều chứa ba hoặc bốn phần:

- Header thông điệp
- Chỉ dành cho Session Request và Session Created, một khóa tạm thời
- Payload được mã hóa ChaCha20
- Một Poly1305 MAC

Trong tất cả các trường hợp, header (và nếu có, ephemeral key) được liên kết với authentication MAC để đảm bảo toàn bộ thông điệp còn nguyên vẹn.

- Đối với các thông điệp handshake Session Request, Session Created, và Session Confirmed, header thông điệp được mixHash() trước giai đoạn xử lý Noise
- Khóa ephemeral, nếu có, được bao phủ bởi một misHash() Noise tiêu chuẩn
- Đối với các thông điệp bên ngoài handshake Noise, header được sử dụng như Associated Data cho mã hóa ChaCha20/Poly1305.

Các bộ xử lý gói tin đến phải luôn giải mã payload ChaCha20 và xác thực MAC trước khi xử lý thông điệp, với một ngoại lệ: Để giảm thiểu các cuộc tấn công DoS từ các gói tin giả mạo địa chỉ chứa các thông điệp Session Request có vẻ hợp lệ nhưng với token không hợp lệ, bộ xử lý KHÔNG CẦN cố gắng giải mã và xác thực toàn bộ thông điệp (yêu cầu một phép toán DH tốn kém ngoài việc giải mã ChaCha20/Poly1305). Bộ xử lý có thể phản hồi bằng thông điệp Retry sử dụng các giá trị được tìm thấy trong header của thông điệp Session Request.

### Mã hóa có xác thực

Có ba phiên bản mã hóa xác thực riêng biệt (CipherStates). Một phiên bản trong giai đoạn handshake, và hai phiên bản (truyền và nhận) cho giai đoạn dữ liệu. Mỗi phiên bản có khóa riêng từ một KDF.

Dữ liệu được mã hóa/xác thực sẽ được biểu diễn dưới dạng

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   Encrypted and authenticated data    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
```
#### ChaCha20/Poly1305

Định dạng dữ liệu được mã hóa và xác thực.

Các đầu vào cho các hàm mã hóa/giải mã:

```
k :: 32 byte cipher key, as generated from KDF

nonce :: Counter-based nonce, 12 bytes.
         Starts at 0 and incremented for each message.
         First four bytes are always zero.
         Last eight bytes are the counter, little-endian encoded.
         Maximum value is 2**64 - 2.
         Connection must be dropped and restarted after
         it reaches that value.
         The value 2**64 - 1 must never be sent.

ad :: In handshake phase:
      Associated data, 32 bytes.
      The SHA256 hash of all preceding data.
      In data phase:
      The packet header, 16 bytes.

data :: Plaintext data, 0 or more bytes
```
Đầu ra của hàm mã hóa, đầu vào của hàm giải mã:

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|       ChaCha20 encrypted data         |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|  Poly1305 Message Authentication Code |
+              (MAC)                    +
|             16 bytes                  |
+----+----+----+----+----+----+----+----+

encrypted data :: Same size as plaintext data, 0 - 65519 bytes

MAC :: Poly1305 message authentication code, 16 bytes
```
Đối với ChaCha20, những gì được mô tả ở đây tương ứng với [RFC-7539](https://tools.ietf.org/html/rfc7539), cũng được sử dụng tương tự trong TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).

#### Ghi chú

- Vì ChaCha20 là một stream cipher, plaintext không cần được padding. Các byte keystream bổ sung sẽ bị loại bỏ.
- Khóa cho cipher (256 bit) được thỏa thuận thông qua SHA256 KDF. Chi tiết về KDF cho từng message được trình bày trong các phần riêng biệt bên dưới.

#### Xử lý Lỗi AEAD

- Trong tất cả các thông điệp, kích thước thông điệp AEAD được biết trước. Khi xác thực AEAD thất bại, người nhận phải dừng xử lý thông điệp tiếp theo và loại bỏ thông điệp.
- Bob nên duy trì một danh sách đen các IP có lỗi lặp lại.

### KDF cho Session Request

Key Derivation Function (KDF) tạo ra một cipher key k cho pha handshake từ kết quả DH, sử dụng HMAC-SHA256(key, data) như được định nghĩa trong [RFC-2104](https://tools.ietf.org/html/rfc2104). Đây là các hàm InitializeSymmetric(), MixHash(), và MixKey(), chính xác như được định nghĩa trong đặc tả Noise.

#### KDF cho ChainKey Ban đầu

```
// Define protocol_name.
Set protocol_name = "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256"
 (52 bytes, US-ASCII encoded, no NULL termination).

// Define Hash h = 32 bytes
h = SHA256(protocol_name);

Define ck = 32 byte chaining key. Copy the h data to ck.
Set ck = h

// MixHash(null prologue)
h = SHA256(h);

// up until here, can all be precalculated by Alice for all outgoing connections

// Bob's X25519 static keys
// bpk is published in routerinfo
bsk = GENERATE_PRIVATE()
bpk = DERIVE_PUBLIC(bsk)

// Bob static key
// MixHash(bpk)
// || below means append
h = SHA256(h || bpk);

// Bob introduction key
// bik is published in routerinfo
bik = RANDOM(32)

// up until here, can all be precalculated by Bob for all incoming connections
```
#### KDF cho Session Request

```
// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Alice's X25519 ephemeral keys
aesk = GENERATE_PRIVATE()
aepk = DERIVE_PUBLIC(aesk)

// Alice ephemeral key X
// MixHash(aepk)
h = SHA256(h || aepk);

// h is used as the associated data for the AEAD in Session Request
// Retain the Hash h for the Session Created KDF


End of "e" message pattern.

This is the "es" message pattern:

// DH(e, rs) == DH(s, re)
sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
// ChaChaPoly parameters to encrypt/decrypt
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chainKey for Session Created KDF


End of "es" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2 = bik

// Header encryption keys for next message (Session Created)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessCreateHeader", 32)

// Header encryption keys for next message (Retry)
k_header_1 = bik
k_header_2 = bik
```
### SessionRequest (Loại 0)

Alice gửi đến Bob, có thể là thông điệp đầu tiên trong quá trình handshake, hoặc để phản hồi một thông điệp Retry. Bob phản hồi bằng thông điệp Session Created. Kích thước: 80 + kích thước payload. Kích thước tối thiểu: 88

Nếu Alice không có token hợp lệ, Alice nên gửi thông điệp Token Request thay vì Session Request, để tránh chi phí mã hóa bất đối xứng khi tạo Session Request.

Header dài. Nội dung Noise: khóa tạm thời X của Alice Payload Noise: DateTime và các khối khác Kích thước payload tối đa: MTU - 108 (IPv4) hoặc MTU - 128 (IPv6). Với MTU 1280: Payload tối đa là 1172 (IPv4) hoặc 1152 (IPv6). Với MTU 1500: Payload tối đa là 1392 (IPv4) hoặc 1372 (IPv6).

Thuộc tính Bảo mật Payload:

```
XK(s, rs):           Authentication   Confidentiality
  -> e, es                  0                2

  Authentication: None (0).
  This payload may have been sent by any party, including an active attacker.

  Confidentiality: 2.
  Encryption to a known recipient, forward secrecy for sender compromise
  only, vulnerable to replay.  This payload is encrypted based only on DHs
  involving the recipient's static key pair.  If the recipient's static
  private key is compromised, even at a later date, this payload can be
  decrypted.  This message can also be replayed, since there's no ephemeral
  contribution from the recipient.

  "e": Alice generates a new ephemeral key pair and stores it in the e
       variable, writes the ephemeral public key as cleartext into the
       message buffer, and hashes the public key along with the old h to
       derive a new h.

  "es": A DH is performed between the Alice's ephemeral key pair and the
        Bob's static key pair.  The result is hashed along with the old ck to
        derive a new ck and k, and n is set to zero.
```
Giá trị X được mã hóa để đảm bảo tính không phân biệt được và tính duy nhất của payload, đây là những biện pháp đối phó DPI cần thiết. Chúng tôi sử dụng mã hóa ChaCha20 để đạt được điều này, thay vì những phương án phức tạp và chậm hơn như elligator2. Mã hóa bất đối xứng với khóa công khai router của Bob sẽ quá chậm. Mã hóa ChaCha20 sử dụng intro key của Bob như được công bố trong network database.

Mã hóa ChaCha20 chỉ dùng để chống DPI. Bất kỳ bên nào biết introduction key của Bob, được công bố trong network database, đều có thể giải mã header và giá trị X trong thông điệp này.

Nội dung thô:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|    See Header Encryption KDF          |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key n=0     +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+       X, ChaCha20 encrypted           +
|       with Bob intro key n=0          |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|  k defined in KDF for Session Request |
+  n = 0                                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

X :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted X)
```
Dữ liệu chưa mã hóa (không hiển thị thẻ xác thực Poly1305):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                   X                   |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|     see below for allowed blocks      |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 0

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Alice, ignored

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: 0 if not previously received from Bob

X :: 32 bytes, X25519 ephemeral key, little endian
```
#### Tải trọng

- Khối DateTime
- Khối Options (tùy chọn)
- Khối Relay Tag Request (tùy chọn)
- Khối Padding (tùy chọn)

Kích thước payload tối thiểu là 8 byte. Do khối DateTime chỉ có 7 byte, nên phải có ít nhất một khối khác.

#### Ghi chú

- Giá trị X duy nhất trong block ChaCha20 ban đầu đảm bảo rằng bản mã hóa sẽ khác nhau cho mỗi phiên.
- Để cung cấp khả năng chống thăm dò, Bob không nên gửi thông báo Retry để phản hồi thông báo Session Request trừ khi loại thông báo, phiên bản giao thức và các trường network ID trong thông báo Session Request là hợp lệ.
- Bob phải từ chối các kết nối có giá trị timestamp quá xa so với thời gian hiện tại. Gọi thời gian delta tối đa là "D". Bob phải duy trì bộ nhớ đệm cục bộ các giá trị handshake đã sử dụng trước đó và từ chối các giá trị trùng lặp, để ngăn chặn các cuộc tấn công replay. Các giá trị trong bộ nhớ đệm phải có thời gian tồn tại ít nhất 2*D. Các giá trị bộ nhớ đệm phụ thuộc vào việc triển khai, tuy nhiên có thể sử dụng giá trị X 32-byte (hoặc tương đương được mã hóa). Từ chối bằng cách gửi thông báo Retry chứa token zero và một termination block.
- Các khóa tạm thời Diffie-Hellman không bao giờ được sử dụng lại, để ngăn chặn các cuộc tấn công mã hóa, và việc sử dụng lại sẽ bị từ chối như một cuộc tấn công replay.
- Các tùy chọn "KE" và "auth" phải tương thích, tức là bí mật chia sẻ K phải có kích thước phù hợp. Nếu thêm nhiều tùy chọn "auth", điều này có thể thay đổi ngầm ý nghĩa của cờ "KE" để sử dụng KDF khác hoặc kích thước cắt ngắn khác.
- Bob phải xác thực rằng khóa tạm thời của Alice là một điểm hợp lệ trên đường cong tại đây.
- Padding nên được giới hạn ở mức hợp lý. Bob có thể từ chối các kết nối có padding quá mức. Bob sẽ chỉ định các tùy chọn padding của mình trong Session Created. Hướng dẫn tối thiểu/tối đa sẽ được xác định. Kích thước ngẫu nhiên từ 0 đến 31 byte tối thiểu? (Phân phối sẽ được xác định, xem Phụ lục A.)
- Đối với hầu hết các lỗi, bao gồm AEAD, DH, replay có vẻ rõ ràng, hoặc lỗi xác thực khóa, Bob nên dừng xử lý thông báo tiếp theo và loại bỏ thông báo mà không phản hồi.
- Bob CÓ THỂ gửi thông báo Retry chứa token zero và Termination block với mã lý do clock skew nếu timestamp trong DateTime block bị lệch quá xa.
- Giảm thiểu DoS: DH là một thao tác tương đối tốn kém. Giống như giao thức NTCP trước đó, các router nên thực hiện tất cả các biện pháp cần thiết để ngăn chặn việc cạn kiệt CPU hoặc kết nối. Đặt giới hạn về số kết nối hoạt động tối đa và số thiết lập kết nối tối đa đang thực hiện. Thực thi timeout đọc (cả cho mỗi lần đọc và tổng cho "slowloris"). Giới hạn các kết nối lặp lại hoặc đồng thời từ cùng nguồn. Duy trì danh sách đen cho các nguồn thường xuyên thất bại. Không phản hồi lỗi AEAD. Thay vào đó, phản hồi bằng thông báo Retry trước thao tác DH và xác thực AEAD.
- Trường "ver": Giao thức Noise tổng thể, các phần mở rộng và giao thức SSU2 bao gồm đặc tả payload, cho biết SSU2. Trường này có thể được sử dụng để cho biết hỗ trợ các thay đổi trong tương lai.
- Trường network ID được sử dụng để nhanh chóng xác định các kết nối cross-network. Nếu trường này không khớp với network ID của Bob, Bob nên ngắt kết nối và chặn các kết nối trong tương lai.
- Bob phải loại bỏ thông báo nếu Source Connection ID bằng Destination Connection ID.

### KDF cho Session Created và Session Confirmed phần 1

```
// take h saved from Session Request KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Request)

// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Bob's X25519 ephemeral keys
besk = GENERATE_PRIVATE()
bepk = DERIVE_PUBLIC(besk)

// h is from KDF for Session Request
// Bob ephemeral key Y
// MixHash(bepk)
h = SHA256(h || bepk);

// h is used as the associated data for the AEAD in Session Created
// Retain the Hash h for the Session Confirmed KDF

End of "e" message pattern.

This is the "ee" message pattern:

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chaining key ck for Session Confirmed KDF

End of "ee" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Request KDF above

// Header protection keys for next message (Session Confirmed)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessionConfirmed", 32)
```
### SessionCreated (Loại 1)

Bob gửi cho Alice để phản hồi thông báo Session Request. Alice phản hồi bằng thông báo Session Confirmed. Kích thước: 80 + kích thước payload. Kích thước tối thiểu: 88

Nội dung Noise: khóa tạm thời Y của Bob Payload Noise: DateTime, Address và các block khác Kích thước payload tối đa: MTU - 108 (IPv4) hoặc MTU - 128 (IPv6). Đối với MTU 1280: Payload tối đa là 1172 (IPv4) hoặc 1152 (IPv6). Đối với MTU 1500: Payload tối đa là 1392 (IPv4) hoặc 1372 (IPv6).

Thuộc tính Bảo mật Payload:

```
XK(s, rs):           Authentication   Confidentiality
  <- e, ee                  2                1

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 1.
  Encryption to an ephemeral recipient.
  This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee").
  However, the sender has not authenticated the recipient,
  so this payload might be sent to any party, including an active attacker.


  "e": Bob generates a new ephemeral key pair and stores it in the e variable,
  writes the ephemeral public key as cleartext into the message buffer,
  and hashes the public key along with the old h to derive a new h.

  "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair.
  The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Giá trị Y được mã hóa để đảm bảo tính không phân biệt được của payload và tính duy nhất, đây là những biện pháp đối phó DPI cần thiết. Chúng tôi sử dụng mã hóa ChaCha20 để đạt được điều này, thay vì các phương án phức tạp và chậm hơn như elligator2. Mã hóa bất đối xứng với khóa công khai của router Alice sẽ quá chậm. Mã hóa ChaCha20 sử dụng intro key của Bob, như được công bố trong network database.

Mã hóa ChaCha20 chỉ dùng để chống DPI. Bất kỳ bên nào biết intro key của Bob, được công bố trong cơ sở dữ liệu mạng, và bắt được 32 byte đầu tiên của Session Request, đều có thể giải mã giá trị Y trong thông điệp này.

Nội dung thô:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with derived key n=0       +
|  See Header Encryption KDF            |
+----+----+----+----+----+----+----+----+
|                                       |
+       Y, ChaCha20 encrypted           +
|       with derived key n=0            |
+              (32 bytes)               +
|       See Header Encryption KDF       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in KDF for Session Created +
|  n = 0; see KDF for associated data   |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

Y :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted Y)
```
Dữ liệu chưa mã hóa (thẻ xác thực Poly1305 không được hiển thị):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                  Y                    |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|      see below for allowed blocks     |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: The Source Connection ID
                             received from Alice in Session Request

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 0

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Bob, ignored

Source Connection ID :: The Destination Connection ID
                        received from Alice in Session Request

Token :: 0 (unused)

Y :: 32 bytes, X25519 ephemeral key, little endian
```
#### Tải trọng

- Khối DateTime
- Khối Address
- Khối Relay Tag (tùy chọn)
- Khối New Token (không khuyến nghị, xem ghi chú)
- Khối First Packet Number (tùy chọn)
- Khối Options (tùy chọn)
- Khối Termination (không khuyến nghị, nên gửi trong thông báo retry thay thế)
- Khối Padding (tùy chọn)

Kích thước payload tối thiểu là 8 byte. Vì các khối DateTime và Address có tổng kích thước lớn hơn con số đó, yêu cầu này đã được đáp ứng chỉ với hai khối này.

#### Ghi chú

- Alice phải xác thực rằng khóa tạm thời của Bob là một điểm hợp lệ trên đường cong tại đây.
- Padding nên được giới hạn ở một mức hợp lý. Alice có thể từ chối các kết nối có padding quá mức. Alice sẽ chỉ định các tùy chọn padding của mình trong Session Confirmed. Hướng dẫn tối thiểu/tối đa sẽ được xác định. Kích thước ngẫu nhiên từ 0 đến 31 byte tối thiểu? (Phân phối sẽ được xác định, xem Phụ lục A.)
- Khi có bất kỳ lỗi nào, bao gồm AEAD, DH, timestamp, replay rõ ràng, hoặc lỗi xác thực khóa, Alice phải dừng xử lý thông điệp tiếp theo và đóng kết nối mà không phản hồi.
- Alice phải từ chối các kết nối khi giá trị timestamp quá xa so với thời gian hiện tại. Gọi delta thời gian tối đa là "D". Alice phải duy trì bộ nhớ đệm cục bộ các giá trị handshake đã sử dụng trước đó và từ chối các bản trùng lặp, để ngăn chặn các cuộc tấn công replay. Các giá trị trong bộ nhớ đệm phải có thời gian tồn tại ít nhất 2*D. Các giá trị bộ nhớ đệm phụ thuộc vào implementation, tuy nhiên có thể sử dụng giá trị Y 32-byte (hoặc tương đương được mã hóa của nó).
- Alice phải loại bỏ thông điệp nếu IP nguồn và cổng không khớp với IP đích và cổng của Session Request.
- Alice phải loại bỏ thông điệp nếu Destination và Source Connection ID không khớp với Source và Destination Connection ID của Session Request.
- Bob gửi một relay tag block nếu được Alice yêu cầu trong Session Request.
- New Token block không được khuyến nghị trong Session Created, vì Bob nên thực hiện xác thực Session Confirmed trước. Xem phần Tokens bên dưới.

#### Vấn đề

- Bao gồm các tùy chọn padding tối thiểu/tối đa ở đây?

### KDF cho phần 1 của Session Confirmed, sử dụng KDF của Session Created

```
// take h saved from Session Created KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Created)

// MixHash(header)
h = SHA256(h || header)
// h is used as the associated data for the AEAD in Session Confirmed part 1, below

This is the "s" message pattern:

// Alice's X25519 static keys
ask = GENERATE_PRIVATE()
apk = DERIVE_PUBLIC(ask)

// AEAD parameters
// k is from Session Request
n = 1
ad = h
ciphertext = ENCRYPT(k, n++, apk, ad)

// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// h is used as the associated data for the AEAD in Session Confirmed part 2

End of "s" message pattern.

// Header encryption keys for this message
See Session Confirmed part 2 below
```
### KDF cho phần 2 của Session Confirmed

```
This is the "se" message pattern:

// DH(ask, bepk) == DH(besk, apk)
sharedSecret = DH(ask, bepk) = DH(besk, apk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// h from Session Confirmed part 1 is used as the associated data for the AEAD in Session Confirmed part 2
// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF
// retain the hash h for the data phase KDF

End of "se" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Created KDF above

// Header protection keys for data phase
See data phase KDF below
```
### SessionConfirmed (Loại 2)

Alice gửi cho Bob, để phản hồi tin nhắn Session Created. Bob phản hồi ngay lập tức với tin nhắn Data chứa khối ACK. Kích thước: 80 + kích thước payload. Kích thước tối thiểu: Khoảng 500 (kích thước khối router info tối thiểu là khoảng 420 byte)

Nội dung Noise: khóa tĩnh của Alice Phần tải trọng Noise 1: Không có Phần tải trọng Noise 2: RouterInfo của Alice và các khối khác Kích thước tải trọng tối đa: MTU - 108 (IPv4) hoặc MTU - 128 (IPv6). Đối với MTU 1280: Tải trọng tối đa là 1172 (IPv4) hoặc 1152 (IPv6). Đối với MTU 1500: Tải trọng tối đa là 1392 (IPv4) hoặc 1372 (IPv6).

Thuộc tính Bảo mật Payload:

```
XK(s, rs):           Authentication   Confidentiality
  -> s, se                  2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).  The
  sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key
  pair.  Assuming the corresponding private keys are secure, this
  authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.  This payload is
  encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static
  DH with the recipient's static key pair.  Assuming the ephemeral private
  keys are secure, and the recipient is not being actively impersonated by an
  attacker that has stolen its static private key, this payload cannot be
  decrypted.

  "s": Alice writes her static public key from the s variable into the
  message buffer, encrypting it, and hashes the output along with the old h
  to derive a new h.

  "se": A DH is performed between the Alice's static key pair and the Bob's
  ephemeral key pair.  The result is hashed along with the old ck to derive a
  new ck and k, and n is set to zero.
```
Điều này chứa hai ChaChaPoly frame. Frame đầu tiên là static public key được mã hóa của Alice. Frame thứ hai là Noise payload: RouterInfo được mã hóa của Alice, các tùy chọn tùy ý, và padding tùy ý. Chúng sử dụng các key khác nhau, vì hàm MixKey() được gọi ở giữa.

Nội dung thô:

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|   ChaCha20 frame (32 bytes)           |
+   Encrypted and authenticated data    +
+   Alice static key S                  +
| k defined in KDF for Session Created  |
+     n = 1                             +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+ Length varies (remainder of packet)   +
|                                       |
+   ChaChaPoly frame                    +
|   Encrypted and authenticated         |
+   see below for allowed blocks        +
|                                       |
+     k defined in KDF for              +
|     Session Confirmed part 2          |
+     n = 0                             +
|     see KDF for associated data       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, ChaChaPoly encrypted Alice's X25519 static key, little endian
     inside 48 byte ChaChaPoly frame
```
Dữ liệu không mã hóa (không hiển thị thẻ xác thực Poly1305):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|              S                        |
+       Alice static key                +
|          (32 bytes)                   |
+                                       +
|                                       |
+                                       +
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|        Noise Payload                  |
+        (length varies)                +
|        see below for allowed blocks   |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As sent in Session Request,
                             or one received in Session Confirmed?

Packet Number :: 0 always, for all fragments, even if retransmitted

type :: 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility

S :: 32 bytes, Alice's X25519 static key, little endian
```
#### Tải trọng

- Khối RouterInfo (phải là khối đầu tiên)
- Khối Options (tùy chọn)
- Khối New Token (tùy chọn)
- Khối Relay Request (tùy chọn)
- Khối Peer Test (tùy chọn)
- Khối First Packet Number (tùy chọn)
- Khối I2NP, First Fragment, hoặc Follow-on Fragment (tùy chọn, nhưng có thể không có chỗ)
- Khối Padding (tùy chọn)

Kích thước payload tối thiểu là 8 byte. Vì khối RouterInfo sẽ lớn hơn nhiều so với đó, yêu cầu này được đáp ứng chỉ với khối đó.

#### Ghi chú

- Bob phải thực hiện xác thực Router Info thông thường. Đảm bảo loại chữ ký được hỗ trợ, xác minh chữ ký, xác minh dấu thời gian nằm trong phạm vi cho phép, và bất kỳ kiểm tra cần thiết nào khác. Xem ghi chú bên dưới về cách xử lý Router Info bị phân mảnh.

- Bob phải xác minh rằng static key của Alice nhận được trong frame đầu tiên khớp với static key trong Router Info. Bob trước tiên phải tìm kiếm trong Router Info một NTCP hoặc SSU2 Router Address với tùy chọn phiên bản (v) khớp. Xem các phần Published Router Info và Unpublished Router Info bên dưới. Xem bên dưới để biết ghi chú về xử lý Router Infos bị phân mảnh.

- Nếu Bob có phiên bản cũ hơn của RouterInfo của Alice trong netdb của mình, hãy xác minh rằng khóa tĩnh trong router info là giống nhau ở cả hai, nếu có, và nếu phiên bản cũ hơn ít hơn XXX tuổi (xem thời gian xoay khóa bên dưới)

- Bob phải xác thực rằng khóa tĩnh của Alice là một điểm hợp lệ trên đường cong tại đây.

- Các tùy chọn nên được bao gồm để chỉ định các tham số đệm.

- Khi có bất kỳ lỗi nào, bao gồm lỗi xác thực AEAD, RI, DH, timestamp, hoặc key validation, Bob phải dừng xử lý tin nhắn và đóng kết nối mà không phản hồi.

- Nội dung khung phần 2 của Thông điệp 3: Định dạng của khung này giống như định dạng của các khung giai đoạn dữ liệu, ngoại trừ độ dài của khung được Alice gửi trong Session Request. Xem bên dưới để biết định dạng khung giai đoạn dữ liệu. Khung phải chứa từ 1 đến 4 khối theo thứ tự sau:

1)  Khối thông tin Router của Alice (bắt buộc)   2)  Khối tùy chọn (tùy chọn)   3)  Các khối I2NP (tùy chọn)

4\) Khối đệm (tùy chọn) Frame này không bao giờ được chứa bất kỳ loại khối nào khác. TODO: còn về relay và peer test thì sao?

- Khuyến nghị sử dụng khối đệm phần 2 của Message 3.

- Có thể không có không gian, hoặc chỉ có một lượng nhỏ không gian có sẵn cho các I2NP block, tùy thuộc vào MTU và kích thước Router Info. KHÔNG bao gồm các I2NP block nếu Router Info bị phân mảnh. Cách triển khai đơn giản nhất có thể là không bao giờ bao gồm các I2NP block trong thông điệp Session Confirmed, và gửi tất cả các I2NP block trong các thông điệp Data tiếp theo. Xem phần Router Info block bên dưới để biết kích thước block tối đa.

#### Phân mảnh Phiên Đã Xác nhận

Thông điệp Session Confirmed phải chứa Router Info đã ký đầy đủ từ Alice để Bob có thể thực hiện một số kiểm tra bắt buộc:

- Khóa tĩnh "s" trong RI khớp với khóa tĩnh trong quá trình handshake
- Khóa giới thiệu "i" trong RI phải được trích xuất và hợp lệ, để sử dụng trong giai đoạn dữ liệu
- Chữ ký RI hợp lệ

Thật không may, Router Info, ngay cả khi được nén gzip trong khối RI, có thể vượt quá MTU. Do đó, Session Confirmed có thể bị phân mảnh thành hai hoặc nhiều gói tin. Đây là trường hợp DUY NHẤT trong giao thức SSU2 mà một payload được bảo vệ AEAD bị phân mảnh thành hai hoặc nhiều gói tin.

Các header cho mỗi gói tin được xây dựng như sau:

- TẤT CẢ header đều là header ngắn với cùng packet number 0
- TẤT CẢ header đều chứa trường "frag", với số thứ tự fragment và tổng số fragment
- Header không mã hóa của fragment 0 là dữ liệu liên kết (AD) cho thông điệp "jumbo"
- Mỗi header được mã hóa bằng 24 byte cuối cùng của dữ liệu trong packet ĐÓ

Xây dựng chuỗi các gói tin như sau:

- Tạo một khối RI đơn (fragment 0 của 1 trong trường frag khối RI). Chúng ta không sử dụng phân mảnh khối RI, điều đó dành cho một phương pháp thay thế để giải quyết cùng một vấn đề.
- Tạo một payload "jumbo" với khối RI và bất kỳ khối nào khác cần được bao gồm
- Tính tổng kích thước dữ liệu (không bao gồm header), đó là kích thước payload + 64 byte cho static key và hai MAC
- Tính không gian có sẵn trong mỗi packet, đó là MTU trừ đi IP header (20 hoặc 40), trừ đi UDP header (8), trừ đi SSU2 short header (16). Tổng overhead mỗi packet là 44 (IPv4) hoặc 64 (IPv6).
- Tính số lượng packet.
- Tính kích thước dữ liệu trong packet cuối cùng. Nó phải lớn hơn hoặc bằng 24 byte, để mã hóa header có thể hoạt động. Nếu quá nhỏ, hãy thêm một padding block, HOẶC tăng kích thước của padding block nếu đã có sẵn, HOẶC giảm kích thước của một trong những packet khác để packet cuối cùng đủ lớn.
- Tạo header chưa mã hóa cho packet đầu tiên, với tổng số fragment trong trường frag, và mã hóa payload "jumbo" bằng Noise, sử dụng header làm AD, như thông thường.
- Chia nhỏ jumbo packet đã mã hóa thành các fragment
- Thêm header chưa mã hóa cho mỗi fragment 1-n
- Mã hóa header cho mỗi fragment 0-n. Mỗi header sử dụng CÙNG k_header_1 và k_header_2 như đã định nghĩa ở trên trong Session Confirmed KDF.
- Truyền tất cả fragment

Quá trình tái lắp ráp:

Khi Bob nhận được bất kỳ thông điệp Session Confirmed nào, anh ta giải mã header, kiểm tra trường frag, và xác định rằng Session Confirmed đã bị phân mảnh. Anh ta không (và không thể) giải mã thông điệp cho đến khi tất cả các mảnh được nhận và tái tạo lại.

- Giữ nguyên header cho fragment 0, vì nó được sử dụng làm Noise AD
- Loại bỏ các header cho các fragment khác trước khi tái lắp ráp
- Tái lắp ráp payload "jumbo", với header của fragment 0 làm AD, và giải mã bằng Noise
- Xác thực khối RI như thường lệ
- Tiến hành giai đoạn dữ liệu và gửi ACK 0, như thường lệ

Không có cơ chế để Bob xác nhận từng fragment riêng lẻ. Khi Bob nhận được tất cả các fragment, tái tập hợp, giải mã và xác thực nội dung, Bob thực hiện split() như thường lệ, vào giai đoạn dữ liệu và gửi ACK của packet số 0.

Nếu Alice không nhận được ACK của gói tin số 0, cô ấy phải truyền lại tất cả các gói tin đã xác nhận phiên như cũ.

Ví dụ:

Với MTU 1500 qua IPv6, tải trọng tối đa là 1372, chi phí khối RI là 5, kích thước dữ liệu RI tối đa (nén gzip) là 1367 (giả sử không có khối khác). Với hai gói tin, chi phí của gói tin thứ 2 là 64, vì vậy nó có thể chứa thêm 1436 byte tải trọng. Vậy hai gói tin là đủ cho một RI nén lên đến 2803 byte.

RI nén lớn nhất được thấy trong mạng hiện tại là khoảng 1400 byte; do đó, trong thực tế, hai fragment sẽ đủ, ngay cả với MTU tối thiểu 1280. Giao thức cho phép tối đa 15 fragment.

Phân tích bảo mật:

Tính toàn vẹn và bảo mật của một Session Confirmed bị phân mảnh là như nhau so với một Session Confirmed không bị phân mảnh. Bất kỳ sự thay đổi nào của bất kỳ mảnh nào sẽ khiến Noise AEAD thất bại sau khi tái tập hợp. Các header của các mảnh sau mảnh 0 chỉ được sử dụng để xác định mảnh. Ngay cả khi một kẻ tấn công trên đường truyền có khóa k_header_2 được sử dụng để mã hóa header (khó xảy ra, được tạo từ quá trình handshake), điều này sẽ không cho phép kẻ tấn công thay thế một mảnh hợp lệ.

### KDF cho giai đoạn dữ liệu

Giai đoạn dữ liệu sử dụng header cho dữ liệu liên kết.

KDF tạo ra hai cipher key k_ab và k_ba từ chaining key ck, sử dụng HMAC-SHA256(key, data) như được định nghĩa trong [RFC-2104](https://tools.ietf.org/html/rfc2104). Đây là hàm split(), được định nghĩa chính xác như trong đặc tả Noise.

```
// split()
// chainKey = from handshake phase
keydata = HKDF(chainKey, ZEROLEN, "", 64)
k_ab = keydata[0:31]
k_ba = keydata[32:63]

// key is k_ab for Alice to Bob
// key is k_ba for Bob to Alice

keydata = HKDF(key, ZEROLEN, "HKDFSSU2DataKeys", 64)
k_data = keydata[0:31]
k_header_2 = keydata[32:63]


// AEAD parameters
k = k_data
n = 4 byte packet number from header
ad = 16 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for data phase
// aik = Alice's intro key
// bik = Bob's intro key
k_header_1 = Receiver's intro key (aik or bik)
k_header_2: from above
```
### Thông điệp Dữ liệu (Loại 6)

Noise payload: Tất cả các loại block đều được cho phép. Kích thước payload tối đa: MTU - 60 (IPv4) hoặc MTU - 80 (IPv6). Với MTU 1500: Payload tối đa là 1440 (IPv4) hoặc 1420 (IPv6).

Bắt đầu từ phần thứ 2 của Session Confirmed, tất cả các thông điệp đều nằm trong một payload ChaChaPoly đã được xác thực và mã hóa. Tất cả padding đều nằm bên trong thông điệp. Bên trong payload là một định dạng tiêu chuẩn với không hoặc nhiều "block". Mỗi block có một byte kiểu và hai byte độ dài. Các kiểu bao gồm date/time, I2NP message, options, termination, và padding.

Lưu ý: Bob có thể, nhưng không bắt buộc, gửi RouterInfo của mình cho Alice như thông điệp đầu tiên trong giai đoạn dữ liệu.

Thuộc Tính Bảo Mật Payload:

```
XK(s, rs):           Authentication   Confidentiality
  <-                        2                5
  ->                        2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.
  This payload is encrypted based on an ephemeral-ephemeral DH as well as
  an ephemeral-static DH with the recipient's static key pair.
  Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated
  by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### Ghi chú

- Router phải loại bỏ thông điệp có lỗi AEAD.

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with intro key and         +
|  derived key, see Data Phase KDF      |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in Data Phase KDF          +
|  n = packet number from header        |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Dữ liệu không mã hóa (thẻ xác thực Poly1305 không hiển thị):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: See below

Packet Number :: Random number generated by Charlie

type :: 11

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: See below

Token :: 8 byte unsigned integer, randomly generated by Charlie, nonzero.
```
#### Ghi chú

- Kích thước payload tối thiểu là 8 byte. Yêu cầu này sẽ được đáp ứng bởi bất kỳ khối ACK, I2NP, First Fragment, hoặc Follow-on Fragment nào. Nếu yêu cầu không được đáp ứng, một khối Padding phải được bao gồm.
- Mỗi số gói chỉ có thể được sử dụng một lần. Khi truyền lại các thông điệp I2NP hoặc các mảnh, một số gói mới phải được sử dụng.

### KDF cho Peer Test

```
// AEAD parameters
// aik = Alice's intro key
k = aik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = aik
k_header_2 = aik
```
### Kiểm tra Peer (Loại 7)

Charlie gửi cho Alice, và Alice gửi cho Charlie, chỉ dành cho các giai đoạn Peer Test 5-7. Các giai đoạn Peer Test 1-4 phải được gửi trong phiên bằng cách sử dụng khối Peer Test trong thông điệp Data. Xem các phần Khối Peer Test và Quy trình Peer Test bên dưới để biết thêm thông tin.

Kích thước: 48 + kích thước payload.

Noise payload: Xem bên dưới.

Nội dung thô:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Dữ liệu không mã hóa (thẻ xác thực Poly1305 không được hiển thị):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

Packet Number :: Random number generated by Alice

type :: 10

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: zero
```
#### Tải trọng

- Khối DateTime
- Khối Address (bắt buộc cho thông điệp 6 và 7, xem ghi chú bên dưới)
- Khối Peer Test
- Khối Padding (tùy chọn)

Kích thước tải trọng tối thiểu là 8 byte. Vì khối Peer Test có tổng kích thước lớn hơn mức đó, yêu cầu được đáp ứng chỉ với khối này.

Trong thông điệp 5 và 7, khối Peer Test có thể giống hệt với khối từ thông điệp trong phiên 3 và 4, chứa thỏa thuận được ký bởi Charlie, hoặc có thể được tạo lại. Chữ ký là tùy chọn.

Trong thông điệp 6, khối Peer Test có thể giống hệt với khối từ các thông điệp trong phiên 1 và 2, chứa yêu cầu được ký bởi Alice, hoặc có thể được tạo lại. Chữ ký là tùy chọn.

Connection IDs: Hai connection IDs được tạo ra từ test nonce. Đối với các thông điệp 5 và 7 được gửi từ Charlie đến Alice, Destination Connection ID là hai bản sao của test nonce 4-byte big-endian, tức là ((nonce << 32) | nonce). Source Connection ID là nghịch đảo của Destination Connection ID, tức là ~((nonce << 32) | nonce). Đối với thông điệp 6 được gửi từ Alice đến Charlie, hoán đổi hai connection IDs.

Nội dung khối địa chỉ:

- Trong thông điệp 5: Không bắt buộc.
- Trong thông điệp 6: IP và port của Charlie được chọn từ RI của Charlie.
- Trong thông điệp 7: IP và port thực tế của Alice mà thông điệp 6 được nhận từ đó.

### KDF cho Thử lại

Yêu cầu đối với thông điệp Retry là Bob không bắt buộc phải giải mã thông điệp Session Request để tạo ra thông điệp Retry phản hồi. Ngoài ra, thông điệp này phải được tạo ra nhanh chóng, chỉ sử dụng mã hóa đối xứng.

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Thử lại (Loại 9)

Bob gửi cho Alice, để phản hồi thông điệp Session Request hoặc Token Request. Alice phản hồi bằng một Session Request mới. Kích thước: 48 + kích thước payload.

Cũng đóng vai trò như một thông báo Chấm dứt (tức là "Không Thử lại") nếu có bao gồm khối Chấm dứt.

Noise payload: Xem bên dưới.

Nội dung thô:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Dữ liệu chưa mã hóa (thẻ xác thực Poly1305 không được hiển thị):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: The Source Connection ID
                             received from Alice in Token Request
                             or Session Request

Packet Number :: Random number generated by Bob

type :: 9

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: The Destination Connection ID
                        received from Alice in Token Request
                        or Session Request

Token :: 8 byte unsigned integer, randomly generated by Bob, nonzero,
         or zero if session is rejected and a termination block is included
```
#### Tải trọng

- Khối DateTime
- Khối Address
- Khối Options (tùy chọn)
- Khối Termination (tùy chọn, nếu phiên bị từ chối)
- Khối Padding (tùy chọn)

Kích thước payload tối thiểu là 8 byte. Vì các khối DateTime và Address có tổng kích thước lớn hơn mức đó, yêu cầu được đáp ứng chỉ với hai khối này.

#### Ghi chú

- Để cung cấp khả năng chống thăm dò, một router không nên gửi thông báo Retry để phản hồi thông báo Session Request hoặc Token Request trừ khi loại thông báo, phiên bản giao thức và các trường network ID trong thông báo Request là hợp lệ.
- Để giới hạn mức độ của bất kỳ cuộc tấn công khuếch đại nào có thể được thực hiện bằng cách sử dụng địa chỉ nguồn giả mạo, thông báo Retry không được chứa lượng lớn padding. Khuyến nghị là thông báo Retry không nên lớn hơn ba lần kích thước của thông báo mà nó đang phản hồi. Hoặc, sử dụng một phương pháp đơn giản như thêm một lượng padding ngẫu nhiên trong khoảng 1-64 byte.

### KDF cho Token Request

Thông điệp này phải được tạo ra nhanh chóng, chỉ sử dụng mã hóa đối xứng.

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Yêu cầu Token (Loại 10)

Alice gửi đến Bob. Bob phản hồi với thông báo Retry. Kích thước: 48 + kích thước payload.

Nếu Alice không có token hợp lệ, Alice nên gửi thông điệp này thay vì Session Request, để tránh chi phí mã hóa bất đối xứng khi tạo ra Session Request.

Noise payload: Xem bên dưới.

Nội dung thô:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Dữ liệu chưa mã hóa (không hiển thị thẻ xác thực Poly1305):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|    flags     |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As specified in session setup

Packet Number :: 4 byte big endian integer

type :: 6

flags :: 3 bytes, unused, set to 0 for future compatibility
```
#### Tải trọng

- Khối DateTime
- Khối Padding

Kích thước payload tối thiểu là 8 byte.

#### Ghi chú

- Để cung cấp khả năng chống thăm dò, một router không nên gửi thông báo Retry để phản hồi thông báo Token Request trừ khi các trường loại thông báo, phiên bản giao thức và network ID trong thông báo Token Request là hợp lệ.
- Đây KHÔNG phải là thông báo Noise tiêu chuẩn và không phải là một phần của handshake. Nó không liên kết với thông báo Session Request ngoại trừ thông qua các connection ID.
- Đối với hầu hết các lỗi, bao gồm AEAD hoặc replay rõ ràng, Bob nên dừng xử lý thông báo tiếp theo và loại bỏ thông báo mà không phản hồi.
- Bob phải từ chối các kết nối có giá trị timestamp quá xa so với thời gian hiện tại. Gọi delta thời gian tối đa là "D". Bob phải duy trì một cache cục bộ của các giá trị handshake đã sử dụng trước đó và từ chối các bản sao để ngăn chặn các cuộc tấn công replay. Các giá trị trong cache phải có thời gian tồn tại ít nhất là 2*D. Các giá trị cache phụ thuộc vào việc triển khai, tuy nhiên có thể sử dụng giá trị X 32-byte (hoặc tương đương được mã hóa).
- Bob CÓ THỂ gửi thông báo Retry chứa token bằng không và khối Termination với mã lý do clock skew nếu timestamp trong khối DateTime bị lệch quá xa.
- Kích thước tối thiểu: TBD, cùng quy tắc như cho Session Created?

### KDF cho Hole Punch

Thông điệp này phải được tạo ra nhanh chóng, chỉ sử dụng mã hóa đối xứng.

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Hole Punch (Loại 11)

Charlie gửi cho Alice, để phản hồi một Relay Intro đã nhận từ Bob. Alice phản hồi với một Session Request mới. Kích thước: 48 + kích thước payload.

Noise payload: Xem bên dưới.

Nội dung thô:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Dữ liệu chưa mã hóa (thẻ xác thực Poly1305 không được hiển thị):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: See below

type :: 7

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random number generated by Alice or Charlie

Source Connection ID :: See below

Token :: Randomly generated by Alice or Charlie, ignored
```
#### Tải trọng

- Khối DateTime
- Khối Address
- Khối Relay Response
- Khối Padding (tùy chọn)

Kích thước payload tối thiểu là 8 byte. Vì các khối DateTime và Address có tổng kích thước lớn hơn giá trị đó, yêu cầu này đã được đáp ứng chỉ với hai khối này.

Connection ID: Hai connection ID được tạo ra từ relay nonce. Destination Connection ID là hai bản sao của relay nonce 4-byte big-endian, tức là ((nonce << 32) | nonce). Source Connection ID là nghịch đảo của Destination Connection ID, tức là ~((nonce << 32) | nonce).

Alice nên bỏ qua token trong header. Token được sử dụng trong Session Request nằm trong khối Relay Response.

## Noise Payload

Mỗi Noise payload chứa không hoặc nhiều "khối".

Điều này sử dụng cùng định dạng khối như được định nghĩa trong các đặc tả [NTCP2](/docs/specs/ntcp2) và [ECIES](/docs/specs/ecies). Các loại khối riêng lẻ được định nghĩa khác nhau. Thuật ngữ tương đương trong QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) là "frames".

Có những lo ngại rằng việc khuyến khích các nhà phát triển chia sẻ code có thể dẫn đến các vấn đề phân tích cú pháp. Các nhà phát triển nên cân nhắc cẩn thận lợi ích và rủi ro của việc chia sẻ code, đồng thời đảm bảo rằng thứ tự và quy tắc khối hợp lệ khác nhau cho hai ngữ cảnh.

### Định dạng Payload

Có một hoặc nhiều khối trong tải trọng được mã hóa. Một khối là định dạng Tag-Length-Value (TLV) đơn giản. Mỗi khối chứa một định danh một byte, một độ dài hai byte, và không hoặc nhiều byte dữ liệu. Định dạng này giống hệt với định dạng trong [NTCP2](/docs/specs/ntcp2) và [ECIES](/docs/specs/ecies), tuy nhiên các định nghĩa khối thì khác nhau.

Để có thể mở rộng, các receiver phải bỏ qua các block có định danh không xác định và coi chúng như là padding.

(Thẻ xác thực Poly1305 không được hiển thị):

```
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
~               .   .   .               ~

blk :: 1 byte, see below
size :: 2 bytes, big endian, size of data to follow, 0 - TBD
data :: the data
```
Mã hóa header sử dụng 24 byte cuối cùng của gói tin làm IV cho hai thao tác ChaCha20. Vì tất cả các gói tin đều kết thúc bằng MAC 16 byte, điều này yêu cầu tất cả payload của gói tin phải có tối thiểu 8 byte. Nếu payload không đáp ứng yêu cầu này, thì phải bao gồm một khối Padding.

Tải trọng ChaChaPoly tối đa thay đổi dựa trên loại thông điệp, MTU, và loại địa chỉ IPv4 hoặc IPv6. Tải trọng tối đa là MTU - 60 đối với IPv4 và MTU - 80 đối với IPv6. Dữ liệu tải trọng tối đa là MTU - 63 đối với IPv4 và MTU - 83 đối với IPv6. Giới hạn trên khoảng 1440 byte đối với IPv4, MTU 1500, thông điệp Data. Kích thước khối tổng tối đa là kích thước tải trọng tối đa. Kích thước khối đơn tối đa là kích thước khối tổng tối đa. Loại khối là 1 byte. Độ dài khối là 2 byte. Kích thước dữ liệu khối đơn tối đa là kích thước khối đơn tối đa trừ đi 3.

Ghi chú:

- Các nhà triển khai phải đảm bảo rằng khi đọc một khối, dữ liệu bị lỗi hoặc độc hại sẽ không khiến việc đọc tràn sang khối tiếp theo hoặc vượt ra ngoài ranh giới payload.
- Các triển khai nên bỏ qua các loại khối không xác định để tương thích với phiên bản tương lai.

Các loại khối:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Block Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Number</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Block Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Options</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15+</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Router Info</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">I2NP Message</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Follow-on Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Termination</td><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 typ.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">8</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Intro</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Next Nonce</td><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">ACK</td><td style="border:1px solid var(--color-border); padding:0.6rem;">12</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 or 21</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;">--</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">17</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Challenge</td><td style="border:1px solid var(--color-border); padding:0.6rem;">18</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">19</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Packet Number</td><td style="border:1px solid var(--color-border); padding:0.6rem;">20</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Congestion</td><td style="border:1px solid var(--color-border); padding:0.6rem;">21</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for experimental features</td><td style="border:1px solid var(--color-border); padding:0.6rem;">224-253</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Padding</td><td style="border:1px solid var(--color-border); padding:0.6rem;">254</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for future extension</td><td style="border:1px solid var(--color-border); padding:0.6rem;">255</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>           
### Quy tắc Sắp xếp Khối

Trong Session Confirmed, Router Info phải là block đầu tiên.

Trong tất cả các thông điệp khác, thứ tự không được chỉ định, trừ các yêu cầu sau: Padding, nếu có, phải là khối cuối cùng. Termination, nếu có, phải là khối cuối cùng trừ Padding. Không được phép có nhiều khối Padding trong một payload duy nhất.

### Thông số kỹ thuật Block

#### DateTime

Để đồng bộ hóa thời gian:

```
+----+----+----+----+----+----+----+
| 0  |    4    |     timestamp     |
+----+----+----+----+----+----+----+

blk :: 0
size :: 2 bytes, big endian, value = 4
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
```
Ghi chú:

- Khác với SSU 1, không có timestamp trong packet header cho data phase trong SSU 2.
- Các implementation nên định kỳ gửi các DateTime block trong data phase.
- Các implementation phải làm tròn đến giây gần nhất để ngăn chặn clock bias trong mạng.

#### Tùy chọn

Truyền các tùy chọn đã cập nhật. Các tùy chọn bao gồm: Padding tối thiểu và tối đa.

Khối tùy chọn sẽ có độ dài thay đổi.

```
+----+----+----+----+----+----+----+----+
| 1  |  size   |tmin|tmax|rmin|rmax|tdmy|
+----+----+----+----+----+----+----+----+
|tdmy|  rdmy   |  tdelay |  rdelay |    |
~----+----+----+----+----+----+----+    ~
|              more_options             |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 1
size :: 2 bytes, big endian, size of options to follow, 12 bytes minimum

tmin, tmax, rmin, rmax :: requested padding limits
    tmin and rmin are for desired resistance to traffic analysis.
    tmax and rmax are for bandwidth limits.
    tmin and tmax are the transmit limits for the router sending this options block.
    rmin and rmax are the receive limits for the router sending this options block.
    Each is a 4.4 fixed-point float representing 0 to 15.9375
    (or think of it as an unsigned 8-bit integer divided by 16.0).
    This is the ratio of padding to data. Examples:
    Value of 0x00 means no padding
    Value of 0x01 means add 6 percent padding
    Value of 0x10 means add 100 percent padding
    Value of 0x80 means add 800 percent (8x) padding
    Alice and Bob will negotiate the minimum and maximum in each direction.
    These are guidelines, there is no enforcement.
    Sender should honor receiver's maximum.
    Sender may or may not honor receiver's minimum, within bandwidth constraints.

tdmy: Max dummy traffic willing to send, 2 bytes big endian, bytes/sec average
rdmy: Requested dummy traffic, 2 bytes big endian, bytes/sec average
tdelay: Max intra-message delay willing to insert, 2 bytes big endian, msec average
rdelay: Requested intra-message delay, 2 bytes big endian, msec average

Padding distribution specified as additional parameters?
Random delay specified as additional parameters?

more_options :: Format TBD
```
Vấn đề về Tùy chọn:

- Việc đàm phán các tùy chọn sẽ được xác định sau (TBD).

#### RouterInfo

Truyền RouterInfo của Alice cho Bob. Chỉ được sử dụng trong phần payload của Session Confirmed part 2. Không được sử dụng trong giai đoạn dữ liệu; thay vào đó hãy sử dụng I2NP DatabaseStore Message.

Kích thước tối thiểu: Khoảng 420 byte, trừ khi danh tính router và chữ ký trong thông tin router có thể nén được, điều này không chắc chắn.

LƯU Ý: Khối Router Info không bao giờ bị phân mảnh. Trường frag luôn là 0/1. Xem phần Session Confirmed Fragmentation ở trên để biết thêm thông tin.

```
+----+----+----+----+----+----+----+----+
| 2  |  size   |flag|frag|              |
+----+----+----+----+----+              +
|                                       |
+       Router Info fragment            +
| (Alice RI in Session Confirmed)       |
+ (Alice, Bob, or third-party           +
|  RI in data phase)                    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 2
size :: 2 bytes, big endian, 2 + fragment size
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 0 for local store, 1 for flood request
       bit 1: 0 for uncompressed, 1 for gzip compressed
       bits 7-2: Unused, set to 0 for future compatibility
frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number, always 0
       bits 3-0: total fragments, always 1, big endian

routerinfo :: Alice's or Bob's RouterInfo
```
Ghi chú:

- Router Info tùy chọn được nén bằng gzip, như được chỉ ra bởi bit cờ 1. Điều này khác với NTCP2, nơi nó không bao giờ được nén, và khác với DatabaseStore Message, nơi nó luôn được nén. Nén là tùy chọn vì nó thường ít có lợi cho các Router Info nhỏ, nơi có ít nội dung có thể nén, nhưng rất có lợi cho các Router Info lớn với một số Router Address có thể nén. Nên sử dụng nén nếu nó cho phép Router Info vừa với một gói Session Confirmed duy nhất mà không cần phân mảnh.
- Kích thước tối đa của mảnh đầu tiên hoặc duy nhất trong thông điệp Session Confirmed: MTU - 113 cho IPv4 hoặc MTU - 133 cho IPv6. Giả sử MTU mặc định 1500 byte, và không có khối nào khác trong thông điệp, 1387 cho IPv4 hoặc 1367 cho IPv6. 97% router info hiện tại nhỏ hơn 1367 mà không cần gzip. 99.9% router info hiện tại nhỏ hơn 1367 khi đã gzip. Giả sử MTU tối thiểu 1280 byte, và không có khối nào khác trong thông điệp, 1167 cho IPv4 hoặc 1147 cho IPv6. 94% router info hiện tại nhỏ hơn 1147 mà không cần gzip. 97% router info hiện tại nhỏ hơn 1147 khi đã gzip.
- Byte frag hiện không được sử dụng, khối Router Info không bao giờ bị phân mảnh. Byte frag phải được đặt thành fragment 0, tổng số fragment 1. Xem phần Session Confirmed Fragmentation ở trên để biết thêm thông tin.
- Flooding không được yêu cầu trừ khi có RouterAddress được công bố trong RouterInfo. Router nhận không được flood RouterInfo trừ khi có RouterAddress được công bố trong đó.
- Giao thức này không cung cấp xác nhận rằng RouterInfo đã được lưu trữ hoặc flood. Nếu muốn có xác nhận, và người nhận là floodfill, người gửi nên gửi một I2NP DatabaseStoreMessage tiêu chuẩn với reply token thay thế.

#### I2NP Message

Một thông điệp I2NP hoàn chỉnh với header đã được chỉnh sửa.

Điều này sử dụng cùng 9 byte cho I2NP header như trong [NTCP2](/docs/specs/ntcp2) (loại, message id, thời gian hết hạn ngắn).

```
+----+----+----+----+----+----+----+----+
| 3  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |     message       |
+----+----+----+----+                   +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 3
size :: 2 bytes, big endian, size of type + msg id + exp + message to follow
        I2NP message body size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: I2NP message body
```
Ghi chú:

- Đây là cùng định dạng header I2NP 9-byte được sử dụng trong NTCP2.
- Đây chính xác là cùng định dạng như khối First Fragment, nhưng loại khối cho biết đây là một thông điệp hoàn chỉnh.
- Kích thước tối đa bao gồm header I2NP 9-byte là MTU - 63 cho IPv4 và MTU - 83 cho IPv6.

#### Fragment Đầu Tiên

Fragment đầu tiên (fragment #0) của một thông điệp I2NP với header đã được sửa đổi.

Điều này sử dụng cùng 9 byte cho header I2NP như trong [NTCP2](/docs/specs/ntcp2) (loại, ID thông điệp, thời hạn ngắn).

Tổng số fragment không được chỉ định.

```
+----+----+----+----+----+----+----+----+
| 4  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |                   |
+----+----+----+----+                   +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 4
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: Partial I2NP message body, bytes 0 - (size - 10)
```
Ghi chú:

- Đây là cùng định dạng header I2NP 9 byte được sử dụng trong NTCP2.
- Đây chính xác là cùng định dạng với khối I2NP Message, nhưng loại khối cho biết đây là fragment đầu tiên của một thông điệp.
- Độ dài thông điệp một phần phải lớn hơn không.
- Như trong SSU 1, khuyến nghị gửi fragment cuối cùng trước, để bên nhận biết tổng số fragment và có thể phân bổ buffer nhận một cách hiệu quả.
- Kích thước tối đa bao gồm header I2NP 9 byte là MTU - 63 cho IPv4 và MTU - 83 cho IPv6.

#### Fragment Tiếp Theo

Một fragment bổ sung (số fragment lớn hơn không) của một thông điệp I2NP.

```
+----+----+----+----+----+----+----+----+
| 5  |  size   |frag|    msg id         |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 5
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 5).
frag :: Fragment info:
        Bit order: 76543210 (bit 7 is MSB)
        bits 7-1: fragment number 1 - 127 (0 not allowed)
        bit 0: isLast (1 = true)
msg id :: 4 bytes, big endian, I2NP message ID
message :: Partial I2NP message body
```
Ghi chú:

- Độ dài tin nhắn một phần phải lớn hơn không.
- Như trong SSU 1, được khuyến nghị gửi phần cuối cùng trước, để bên nhận biết tổng số phần và có thể phân bổ bộ đệm nhận một cách hiệu quả.
- Như trong SSU 1, số phần tối đa là 127, nhưng giới hạn thực tế là 63 hoặc ít hơn. Các triển khai có thể giới hạn số tối đa thành mức thực tế cho kích thước tin nhắn I2NP tối đa khoảng 64 KB, tức là khoảng 55 phần với MTU tối thiểu 1280. Xem phần Max I2NP Message Size bên dưới.
- Kích thước tin nhắn một phần tối đa (không bao gồm frag và message id) là MTU - 68 đối với IPv4 và MTU - 88 đối với IPv6.

#### Chấm dứt

Ngắt kết nối. Đây phải là khối không đệm cuối cùng trong payload.

```
+----+----+----+----+----+----+----+----+
| 6  |  size   |    valid data packets  |
+----+----+----+----+----+----+----+----+
    received   | rsn|     addl data     |
+----+----+----+----+                   +
~               .   .   .               ~
+----+----+----+----+----+----+----+----+

blk :: 6
size :: 2 bytes, big endian, value = 9 or more
valid data packets received :: The number of valid packets received
                              (current receive nonce value)
                              0 if error occurs in handshake phase
                              8 bytes, big endian
rsn :: reason, 1 byte:
       0: normal close or unspecified
       1: termination received
       2: idle timeout
       3: router shutdown
       4: data phase AEAD failure
       5: incompatible options
       6: incompatible signature type
       7: clock skew
       8: padding violation
       9: AEAD framing error
       10: payload format error
       11: Session Request error
       12: Session Created error
       13: Session Confirmed error
       14: Timeout
       15: RI signature verification fail
       16: s parameter missing, invalid, or mismatched in RouterInfo
       17: banned
       18: bad token
       19: connection limits
       20: incompatible version
       21: wrong net ID
       22: replaced by new session
addl data :: optional, 0 or more bytes, for future expansion, debugging,
             or reason text.
             Format unspecified and may vary based on reason code.
```
Ghi chú:

- Không phải tất cả các lý do đều thực sự được sử dụng, phụ thuộc vào việc triển khai. Hầu hết các lỗi sẽ thường dẫn đến việc thông điệp bị loại bỏ, không phải chấm dứt. Xem ghi chú trong các phần thông điệp handshake ở trên. Các lý do bổ sung được liệt kê là để đảm bảo tính nhất quán, ghi log, gỡ lỗi, hoặc nếu chính sách thay đổi.
- Khuyến nghị nên bao gồm một khối ACK cùng với khối Termination.
- Trong giai đoạn dữ liệu, đối với bất kỳ lý do nào khác ngoài "termination received", peer nên phản hồi với một khối termination với lý do "termination received".

#### RelayRequest

Được gửi trong một thông điệp Data trong phiên, từ Alice đến Bob. Xem phần Quy trình Relay bên dưới.

```
+----+----+----+----+----+----+----+----+
|  7 |  size   |flag|       nonce       |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 7
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility

The data below here is covered
by the signature, and Bob forwards it unmodified.

nonce :: 4 bytes, randomly generated by Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
Ghi chú:

- Địa chỉ IP luôn được bao gồm (không giống như trong SSU 1) và có thể khác với IP được sử dụng cho phiên làm việc.

Chữ ký:

Alice ký yêu cầu và bao gồm nó trong khối này; Bob chuyển tiếp nó trong khối Relay Intro tới Charlie. Thuật toán chữ ký: Ký dữ liệu sau đây bằng khóa ký router của Alice:

- prologue: 16 bytes "RelayRequestData", không kết thúc bằng null (không được bao gồm trong thông điệp)
- bhash: 32-byte router hash của Bob (không được bao gồm trong thông điệp)
- chash: 32-byte router hash của Charlie (không được bao gồm trong thông điệp)
- nonce: 4 byte nonce
- relay tag: 4 byte relay tag
- timestamp: 4 byte timestamp (giây)
- ver: 1 byte phiên bản SSU
- asz: 1 byte kích thước endpoint (port + IP) (6 hoặc 18)
- AlicePort: 2 byte số port của Alice
- Alice IP: (asz - 2) byte địa chỉ IP của Alice

#### RelayResponse

Được gửi trong thông điệp Data trong phiên, từ Charlie đến Bob hoặc từ Bob đến Alice, VÀ trong thông điệp Hole Punch từ Charlie đến Alice. Xem phần Quy trình Relay bên dưới.

```
+----+----+----+----+----+----+----+----+
|  8 |  size   |flag|code|    nonce
+----+----+----+----+----+----+----+----+
     |     timestamp     | ver| csz|Char
+----+----+----+----+----+----+----+----+
 Port|   Charlie IP addr |              |
+----+----+----+----+----+              +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

blk :: 8
size :: 2 bytes, 6
flag :: 1 byte flags, Unused, set to 0 for future compatibility
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, Charlie is banned
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, relay tag not found
       6: rejected by Bob, Alice RI not found
       7-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       71-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD

The data below is covered by the signature if the code is 0 (accept).
Bob forwards it unmodified.

nonce :: 4 bytes, as received from Bob or Alice

The data below is present only if the code is 0 (accept).

timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
csz :: 1 byte endpoint (port + IP) size (0 or 6 or 18)
       may be 0 for some rejection codes
CharliePort :: 2 byte Charlie's port number, big endian
               not present if csz is 0
Charlie IP :: (csz - 2) byte representation of Charlie's IP address,
              network byte order
              not present if csz is 0
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Charlie.
             Not present if rejected by Bob.
token :: Token generated by Charlie for Alice to use
         in the Session Request.
         Only present if code is 0 (accept)
```
Ghi chú:

Token phải được Alice sử dụng ngay lập tức trong Session Request.

Chữ ký:

Nếu Charlie đồng ý (mã phản hồi 0) hoặc từ chối (mã phản hồi 64 trở lên), Charlie ký phản hồi và bao gồm nó trong khối này; Bob chuyển tiếp nó trong khối Relay Response tới Alice. Thuật toán chữ ký: Ký dữ liệu sau đây bằng khóa ký của router Charlie:

- prologue: 16 bytes "RelayAgreementOK", không kết thúc bằng null (không được bao gồm trong thông điệp)
- bhash: 32-byte router hash của Bob (không được bao gồm trong thông điệp)
- nonce: 4 byte nonce
- timestamp: 4 byte timestamp (giây)
- ver: 1 byte phiên bản SSU
- csz: 1 byte kích thước endpoint (port + IP) (0 hoặc 6 hoặc 18)
- CharliePort: 2 byte số port của Charlie (không có mặt nếu csz là 0)
- Charlie IP: (csz - 2) byte địa chỉ IP của Charlie (không có mặt nếu csz là 0)

Nếu Bob từ chối (mã phản hồi 1-63), Bob ký phản hồi và bao gồm nó trong khối này. Thuật toán chữ ký: Ký dữ liệu sau đây với khóa ký của router Bob:

- prologue: 16 byte "RelayAgreementOK", không kết thúc bằng null (không bao gồm trong thông điệp)
- bhash: 32-byte router hash của Bob (không bao gồm trong thông điệp)
- nonce: 4 byte nonce
- timestamp: 4 byte timestamp (giây)
- ver: 1 byte phiên bản SSU
- csz: 1 byte = 0

#### RelayIntro

Được gửi trong một thông điệp Data trong phiên, từ Bob đến Charlie. Xem phần Relay Process bên dưới.

Phải được đứng trước bởi một khối RouterInfo, hoặc khối I2NP DatabaseStore message (hoặc fragment), chứa Router Info của Alice, hoặc trong cùng một payload (nếu có đủ chỗ), hoặc trong một message trước đó.

```
+----+----+----+----+----+----+----+----+
|  9 |  size   |flag|                   |
+----+----+----+----+                   +
|                                       |
+                                       +
|         Alice Router Hash             |
+             32 bytes                  +
|                                       |
+                   +----+----+----+----+
|                   |      nonce        |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 9
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's 32-byte router hash,

The data below here is covered
by the signature, as received from Alice in the Relay Request,
and Bob forwards it unmodified.

nonce :: 4 bytes, as received from Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
Ghi chú:

- Đối với IPv4, địa chỉ IP của Alice luôn có 4 byte, vì Alice đang cố gắng kết nối đến Charlie thông qua IPv4. IPv6 được hỗ trợ, và địa chỉ IP của Alice có thể có 16 byte.
- Đối với IPv4, thông điệp này phải được gửi qua một kết nối IPv4 đã thiết lập, vì đây là cách duy nhất để Bob biết địa chỉ IPv4 của Charlie để trả về cho Alice trong [RelayResponse](#relayresponse). IPv6 được hỗ trợ, và thông điệp này có thể được gửi qua một kết nối IPv6 đã thiết lập.
- Bất kỳ địa chỉ SSU nào được xuất bản với introducers phải chứa "4" hoặc "6" trong tùy chọn "caps".

Chữ ký:

Alice ký yêu cầu và Bob chuyển tiếp nó trong khối này đến Charlie. Thuật toán xác minh: Xác minh dữ liệu sau với khóa ký của router Alice:

- prologue: 16 bytes "RelayRequestData", không kết thúc bằng null (không bao gồm trong thông điệp)
- bhash: 32-byte router hash của Bob (không bao gồm trong thông điệp)
- chash: 32-byte router hash của Charlie (không bao gồm trong thông điệp)
- nonce: 4 byte nonce
- relay tag: 4 byte relay tag
- timestamp: 4 byte timestamp (giây)
- ver: 1 byte phiên bản SSU
- asz: 1 byte kích thước endpoint (port + IP) (6 hoặc 18)
- AlicePort: 2 byte số port của Alice
- Alice IP: (asz - 2) byte địa chỉ IP của Alice

#### PeerTest

Được gửi trong một thông điệp Data trong phiên, hoặc trong một thông điệp Peer Test ngoài phiên. Xem phần Quy trình Peer Test bên dưới.

Đối với tin nhắn 2, phải được đi trước bởi một khối RouterInfo, hoặc khối tin nhắn I2NP DatabaseStore (hoặc đoạn), chứa Router Info của Alice, có thể trong cùng một payload (nếu có đủ chỗ), hoặc trong một tin nhắn trước đó.

Đối với thông điệp 4, nếu relay được chấp nhận (mã lý do 0), phải được đi trước bởi một khối RouterInfo, hoặc khối thông điệp I2NP DatabaseStore (hoặc đoạn), chứa Router Info của Charlie, hoặc trong cùng payload (nếu có chỗ), hoặc trong một thông điệp trước đó.

```
+----+----+----+----+----+----+----+----+
| 10 |  size   | msg|code|flag|         |
+----+----+----+----+----+----+         +
| Alice router hash (message 2 only)    |
+             or                        +
| Charlie router hash (message 4 only)  |
+ or all zeros if rejected by Bob       +
| Not present in messages 1,3,5,6,7     |
+                             +----+----+
|                             | ver|
+----+----+----+----+----+----+----+----+
   nonce       |     timestamp     | asz|
+----+----+----+----+----+----+----+----+
|AlicePort|  Alice IP address |         |
+----+----+----+----+----+----+         +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 10
size :: 2 bytes, big endian, size of data to follow
msg :: 1 byte message number 1-7
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, no Charlie available
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, address unsupported
       6-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       70-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD
       reject codes only allowed in messages 3 and 4
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's or Charlie's 32-byte router hash,
        only present in messages 2 and 4.
        All zeros (fake hash) in message 4 if rejected by Bob.

For messages 1-4, the data below here is covered
by the signature, if present, and Bob forwards it unmodified.

ver :: 1 byte SSU version:
       1: SSU 1 (not supported)
       2: SSU 2 (required)
nonce :: 4 byte test nonce, big endian
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice or Charlie.
             Only present for messages 1-4.
             Optional in message 5-7.
```
Ghi chú:

- Khác với SSU 1, thông điệp 1 phải bao gồm địa chỉ IP và cổng của Alice.

- Việc kiểm thử các địa chỉ IPv6 được hỗ trợ, và việc liên lạc Alice-Bob và Alice-Charlie có thể thông qua IPv6, nếu Bob và Charlie chỉ ra sự hỗ trợ với khả năng 'B' trong địa chỉ IPv6 đã xuất bản của họ. Xem Đề xuất 126 để biết chi tiết.

Alice gửi yêu cầu đến Bob sử dụng một phiên kết nối hiện có qua giao thức vận chuyển (IPv4 hoặc IPv6) mà cô ấy muốn kiểm tra. Khi Bob nhận được yêu cầu từ Alice qua IPv4, Bob phải chọn một Charlie có quảng cáo địa chỉ IPv4. Khi Bob nhận được yêu cầu từ Alice qua IPv6, Bob phải chọn một Charlie có quảng cáo địa chỉ IPv6. Việc liên lạc thực tế giữa Bob-Charlie có thể thông qua IPv4 hoặc IPv6 (tức là độc lập với loại địa chỉ của Alice).

- Các thông điệp 1-4 phải được chứa trong một thông điệp Data trong một phiên hiện có.

- Bob phải gửi RI của Alice cho Charlie trước khi gửi tin nhắn 2.

- Bob phải gửi RI của Charlie tới Alice trước khi gửi tin nhắn 4, nếu được chấp nhận (mã lý do 0).

- Các thông điệp 5-7 phải được chứa trong thông điệp Peer Test ngoài phiên.

- Thông điệp 5 và 7 có thể chứa cùng dữ liệu đã ký như đã gửi trong thông điệp 3 và 4, hoặc có thể được tạo lại với timestamp mới. Chữ ký là tùy chọn.

- Tin nhắn 6 có thể chứa cùng dữ liệu đã ký như đã gửi trong tin nhắn 1 và 2, hoặc có thể được tạo lại với timestamp mới. Chữ ký là tùy chọn.

Chữ ký:

Alice ký yêu cầu và đưa nó vào tin nhắn 1; Bob chuyển tiếp nó trong tin nhắn 2 đến Charlie. Charlie ký phản hồi và đưa nó vào tin nhắn 3; Bob chuyển tiếp nó trong tin nhắn 4 đến Alice. Thuật toán chữ ký: Ký hoặc xác minh dữ liệu sau đây bằng khóa ký của Alice hoặc Charlie:

- prologue: 16 bytes "PeerTestValidate", không kết thúc bằng null (không bao gồm trong thông điệp)
- bhash: 32-byte router hash của Bob (không bao gồm trong thông điệp)
- ahash: 32-byte router hash của Alice (Chỉ được sử dụng trong chữ ký cho thông điệp 3 và 4; không bao gồm trong thông điệp 3 hoặc 4)
- ver: 1 byte phiên bản SSU
- nonce: 4 byte test nonce
- timestamp: 4 byte timestamp (giây)
- asz: 1 byte kích thước endpoint (port + IP) (6 hoặc 18)
- AlicePort: 2 byte số port của Alice
- Alice IP: (asz - 2) byte địa chỉ IP của Alice

#### NextNonce

TODO chỉ khi chúng ta xoay khóa

```
+----+----+----+----+----+----+----+----+
| 11 |  size   |      TBD               |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 11
size :: 2 bytes, big endian, size of data to follow
```
#### Xác nhận

4 byte ack through, theo sau bởi một ack count và không hoặc nhiều nack/ack ranges.

Thiết kế này được điều chỉnh và đơn giản hóa từ QUIC. Các mục tiêu thiết kế như sau:

- Chúng ta muốn mã hóa hiệu quả một "bitfield", đây là một chuỗi bit đại diện cho các gói tin đã được xác nhận.
- Bitfield chủ yếu là các số 1. Cả số 1 và số 0 thường xuất hiện theo các "cụm" tuần tự.
- Lượng không gian có sẵn trong gói tin để chứa ack có thể thay đổi.
- Bit quan trọng nhất là bit có số thứ tự cao nhất. Các bit có số thứ tự thấp hơn ít quan trọng hơn. Dưới một khoảng cách nhất định từ bit cao nhất, các bit cũ nhất sẽ bị "quên" và không bao giờ được gửi lại.

Phương thức mã hóa được chỉ định dưới đây đạt được các mục tiêu thiết kế này, bằng cách gửi số của bit cao nhất được đặt thành 1, cùng với các bit liên tiếp bổ sung thấp hơn bit đó cũng được đặt thành 1. Sau đó, nếu còn chỗ, một hoặc nhiều "phạm vi" chỉ định số lượng bit 0 liên tiếp và bit 1 liên tiếp thấp hơn. Xem QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) phần 13.2.3 để biết thêm thông tin nền.

```
+----+----+----+----+----+----+----+----+
| 12 |  size   |    Ack Through    |acnt|
+----+----+----+----+----+----+----+----+
|  range  |  range  |     .   .   .     |
+----+----+----+----+                   +
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 12
size :: 2 bytes, big endian, size of data to follow,
        5 minimum
ack through :: highest packet number acked
acnt :: number of acks lower than ack through also acked,
        0-255
range :: If present,
         1 byte nack count followed by 1 byte ack count,
         0-255 each
```
Ví dụ:

Chúng ta chỉ muốn ACK packet 10:

- Ack Through: 10
- acnt: 0
- không có phạm vi nào được bao gồm

Chúng ta muốn ACK các gói tin 8-10 mà thôi:

- Ack Through: 10
- acnt: 2
- không có phạm vi nào được bao gồm

Chúng ta muốn ACK 10 9 8 6 5 2 1 0, và NACK 7 4 3. Mã hóa của ACK Block là:

- Ack Through: 10
- acnt: 2 (ack 9 8)
- range: 1 2 (nack 7, ack 6 5)
- range: 2 3 (nack 4 3, ack 2 1 0)

Ghi chú:

- Các range có thể không có mặt. Số lượng tối đa các range không được chỉ định, có thể có nhiều range miễn là vừa với gói tin.
- Range nack có thể bằng không nếu ack hơn 255 gói tin liên tiếp.
- Range ack có thể bằng không nếu nack hơn 255 gói tin liên tiếp.
- Range nack và ack không thể đồng thời bằng không.
- Sau range cuối cùng, các gói tin không được ack cũng không được nack. Độ dài của ack block và cách xử lý các ack/nack cũ phụ thuộc vào bên gửi ack block. Xem các phần ack bên dưới để thảo luận.
- Ack through nên là số gói tin cao nhất đã nhận được, và bất kỳ gói tin nào cao hơn đều chưa được nhận. Tuy nhiên, trong các tình huống hạn chế, nó có thể thấp hơn, chẳng hạn như ack một gói tin đơn lẻ "lấp đầy khoảng trống", hoặc một triển khai đơn giản không duy trì trạng thái của tất cả các gói tin đã nhận. Trên mức cao nhất đã nhận, các gói tin không được ack cũng không được nack, nhưng sau vài ack block, có thể thích hợp để chuyển sang chế độ truyền lại nhanh.
- Định dạng này là phiên bản đơn giản hóa của QUIC. Nó được thiết kế để mã hóa hiệu quả một số lượng lớn ACK, cùng với các đợt NACK.
- ACK block được sử dụng để xác nhận các gói tin giai đoạn dữ liệu. Chúng chỉ được bao gồm cho các gói tin giai đoạn dữ liệu trong phiên.

#### Địa chỉ

Cổng 2 byte và địa chỉ IP 4 hoặc 16 byte. Địa chỉ của Alice, được Bob gửi cho Alice, hoặc địa chỉ của Bob, được Alice gửi cho Bob.

```
+----+----+----+----+----+----+----+----+
| 13 | 6 or 18 |   Port  | IP Address    
+----+----+----+----+----+----+----+----+
     |
+----+

blk :: 13
size :: 2 bytes, big endian, 6 or 18
port :: 2 bytes, big endian
ip :: 4 byte IPv4 or 16 byte IPv6 address,
      big endian (network byte order)
```
#### Yêu cầu Relay Tag

Điều này có thể được gửi bởi Alice trong một thông điệp Session Request, Session Confirmed, hoặc Data. Không được hỗ trợ trong thông điệp Session Created, vì Bob chưa có RI của Alice, và không biết liệu Alice có hỗ trợ relay hay không. Ngoài ra, nếu Bob đang nhận một kết nối đến, anh ta có thể không cần introducers (ngoại trừ có thể cho loại khác ipv4/ipv6).

Khi được gửi trong Session Request, Bob có thể phản hồi bằng Relay Tag trong thông điệp Session Created, hoặc có thể chọn đợi cho đến khi nhận được RouterInfo của Alice trong Session Confirmed để xác thực danh tính của Alice trước khi phản hồi trong thông điệp Data. Nếu Bob không muốn relay cho Alice, anh ta sẽ không gửi khối Relay Tag.

```
+----+----+----+
| 15 |    0    |
+----+----+----+

blk :: 15
size :: 2 bytes, big endian, value = 0
```
#### Thẻ Relay

Điều này có thể được gửi bởi Bob trong một thông điệp Session Confirmed hoặc Data, để phản hồi lại một Relay Tag Request từ Alice.

Khi Relay Tag Request được gửi trong Session Request, Bob có thể phản hồi với một Relay Tag trong thông điệp Session Created, hoặc có thể chọn chờ đợi cho đến khi nhận được RouterInfo của Alice trong Session Confirmed để xác thực danh tính của Alice trước khi phản hồi trong thông điệp Data. Nếu Bob không muốn relay cho Alice, anh ta sẽ không gửi khối Relay Tag.

```
+----+----+----+----+----+----+----+
| 16 |    4    |    relay tag      |
+----+----+----+----+----+----+----+

blk :: 16
size :: 2 bytes, big endian, value = 4
relay tag :: 4 bytes, big endian, nonzero
```
#### Token Mới

Dành cho kết nối tiếp theo. Thường được bao gồm trong các thông điệp Session Created và Session Confirmed. Cũng có thể được gửi lại trong thông điệp Data của một phiên dài hạn nếu token trước đó hết hạn.

```
+----+----+----+----+----+----+----+----+
| 17 |   12    |     expires       |
+----+----+----+----+----+----+----+----+
                token              |
+----+----+----+----+----+----+----+

blk :: 17
size :: 2 bytes, big endian, value = 12
expires :: Unix timestamp, unsigned seconds.
           Wraps around in 2106
token :: 8 bytes, big endian
```
#### Thách thức Đường dẫn

Một Ping với dữ liệu tùy ý được trả về trong Path Response, được sử dụng như keep-alive hoặc để xác thực thay đổi IP/Port.

```
+----+----+----+----+----+----+----+----+
| 18 |  size   |    Arbitrary Data      |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 18
size :: 2 bytes, big endian, size of data to follow
data :: Arbitrary data to be returned in a Path Response
        length as selected by sender
```
Ghi chú:

- Khuyến nghị sử dụng kích thước dữ liệu tối thiểu là 8 byte, chứa dữ liệu ngẫu nhiên, nhưng không bắt buộc.
- Kích thước tối đa không được chỉ định, nhưng nên dưới 1280 vì PMTU trong giai đoạn xác thực đường dẫn là 1280.
- Không khuyến nghị sử dụng kích thước challenge lớn vì chúng có thể là vector cho các cuộc tấn công khuếch đại gói tin.

#### Phản Hồi Đường Dẫn

Một Pong với dữ liệu nhận được trong Path Challenge, như phản hồi cho Path Challenge, được sử dụng như keep-alive hoặc để xác thực thay đổi IP/Port.

```
+----+----+----+----+----+----+----+----+
| 19 |  size   |                        |
+----+----+----+                        +
|    Data received in Path Challenge    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 19
size :: 2 bytes, big endian, size of data to follow
data :: As received in a Path Challenge
```
#### Số Gói Tin Đầu Tiên

Tùy chọn được bao gồm trong quá trình bắt tay theo mỗi hướng, để chỉ định số gói tin đầu tiên sẽ được gửi. Điều này cung cấp thêm bảo mật cho việc mã hóa header, tương tự như TCP.

Chưa được xác định đầy đủ, hiện tại chưa được hỗ trợ.

```
+----+----+----+----+----+----+----+
| 20 |  size   |  First pkt number |
+----+----+----+----+----+----+----+

blk :: 20
size :: 4
pkt num :: The first packet number to be sent in the data phase
```
#### Tắc nghẽn

Khối này được thiết kế như một phương pháp có thể mở rộng để trao đổi thông tin kiểm soát tắc nghẽn. Kiểm soát tắc nghẽn có thể phức tạp và có thể phát triển khi chúng ta có thêm kinh nghiệm với giao thức trong thử nghiệm thực tế, hoặc sau khi triển khai đầy đủ.

Điều này giữ cho mọi thông tin tắc nghẽn tránh xa các khối I2NP, First Fragment, Followon Fragment và ACK sử dụng nhiều, nơi không có không gian được phân bổ cho các cờ. Mặc dù có ba byte cờ không sử dụng trong header của gói Data, điều đó cũng chỉ cung cấp không gian mở rộng hạn chế và bảo vệ mã hóa yếu hơn.

Mặc dù việc sử dụng một khối 4-byte cho hai bit thông tin có phần lãng phí, nhưng bằng cách đặt thông tin này trong một khối riêng biệt, chúng ta có thể dễ dàng mở rộng nó với dữ liệu bổ sung như kích thước cửa sổ hiện tại, RTT đo được, hoặc các cờ khác. Kinh nghiệm đã cho thấy rằng chỉ có các bit cờ thường là không đủ và khó khăn cho việc triển khai các lược đồ kiểm soát tắc nghẽn nâng cao. Việc cố gắng thêm hỗ trợ cho bất kỳ tính năng kiểm soát tắc nghẽn nào có thể có trong, ví dụ, khối ACK, sẽ lãng phí không gian và làm tăng độ phức tạp trong việc phân tích khối đó.

Các triển khai không nên giả định rằng router khác hỗ trợ bất kỳ bit cờ hoặc tính năng cụ thể nào được bao gồm ở đây, trừ khi việc triển khai được yêu cầu bởi một phiên bản tương lai của đặc tả này.

Block này có lẽ nên là block cuối cùng không phải padding trong payload.

```
+----+----+----+----+
| 21 |  size   |flag|
+----+----+----+----+

blk :: 21
size :: 1 (or more if extended)
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 1 to request immediate ack
       bit 1: 1 for explicit congestion notification (ECN)
       bits 7-2: Unused, set to 0 for future compatibility
```
#### Đệm

Đây là để đệm bên trong các payload AEAD. Đệm cho tất cả các thông điệp đều nằm bên trong payload AEAD.

Padding nên tuân thủ gần đúng các tham số đã thương lượng. Bob đã gửi các tham số tx/rx min/max được yêu cầu của mình trong Session Created. Alice đã gửi các tham số tx/rx min/max được yêu cầu của mình trong Session Confirmed. Các tùy chọn cập nhật có thể được gửi trong giai đoạn dữ liệu. Xem thông tin khối tùy chọn ở trên.

Nếu có, block này phải là block cuối cùng trong payload.

```
+----+----+----+----+----+----+----+----+
|254 |  size   |      padding           |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 254
size :: 2 bytes, big endian, size of padding to follow
padding :: random data
```
Ghi chú:

- Size = 0 được phép.
- Chiến lược padding TBD.
- Padding tối thiểu TBD.
- Payload chỉ có padding được phép.
- Padding mặc định TBD.
- Xem khối options để thương lượng tham số padding
- Xem khối options cho các tham số padding tối thiểu/tối đa
- Không vượt quá MTU. Nếu cần thêm padding, hãy gửi nhiều tin nhắn.
- Phản hồi của router khi vi phạm padding đã thương lượng phụ thuộc vào implementation.
- Độ dài padding có thể được quyết định trên cơ sở từng tin nhắn và ước tính phân phối độ dài, hoặc nên thêm độ trễ ngẫu nhiên. Các biện pháp đối phó này được bao gồm để chống DPI, vì kích thước tin nhắn có thể tiết lộ rằng lưu lượng I2P đang được truyền tải bởi giao thức transport. Sơ đồ padding chính xác là một lĩnh vực nghiên cứu trong tương lai, Phụ lục A của [NTCP2](/docs/specs/ntcp2) cung cấp thêm thông tin về chủ đề này.

## Ngăn chặn tấn công Replay

SSU2 được thiết kế để giảm thiểu tác động của các thông điệp bị kẻ tấn công phát lại.

Các thông điệp Token Request, Retry, Session Request, Session Created, Hole Punch và out-of-session Peer Test phải chứa các khối DateTime.

Cả Alice và Bob đều xác thực rằng thời gian của các thông điệp này nằm trong phạm vi sai lệch hợp lệ (khuyến nghị +/- 2 phút). Để "chống thăm dò", Bob không nên phản hồi các thông điệp Token Request hoặc Session Request nếu sai lệch thời gian không hợp lệ, vì các thông điệp này có thể là một cuộc tấn công phát lại hoặc thăm dò.

Bob có thể chọn từ chối các thông điệp Token Request và Retry trùng lặp, ngay cả khi độ lệch thời gian hợp lệ, thông qua bộ lọc Bloom hoặc cơ chế khác. Tuy nhiên, kích thước và chi phí CPU để phản hồi các thông điệp này là thấp. Trong trường hợp xấu nhất, một thông điệp Token Request được phát lại có thể làm vô hiệu hóa token đã được gửi trước đó.

Hệ thống token giảm thiểu đáng kể tác động của các thông điệp Session Request bị phát lại. Vì token chỉ có thể được sử dụng một lần, một thông điệp Session Request bị phát lại sẽ không bao giờ có token hợp lệ. Bob có thể chọn từ chối các thông điệp Session Request trùng lặp, ngay cả khi skew hợp lệ, thông qua Bloom filter hoặc cơ chế khác. Tuy nhiên, kích thước và chi phí CPU để trả lời bằng thông điệp Retry là thấp. Trong trường hợp xấu nhất, việc gửi thông điệp Retry có thể vô hiệu hóa một token đã được gửi trước đó.

Các thông điệp Session Created và Session Confirmed trùng lặp sẽ không được xác thực vì trạng thái handshake của Noise sẽ không ở trạng thái chính xác để giải mã chúng. Trong trường hợp xấu nhất, một peer có thể truyền lại Session Confirmed để phản hồi một Session Created trùng lặp rõ ràng.

Các thông điệp Hole Punch và Peer Test bị phát lại sẽ có ít hoặc không có tác động.

Các router phải sử dụng số gói tin của data message để phát hiện và loại bỏ các data phase message trùng lặp. Mỗi số gói tin chỉ nên được sử dụng một lần. Các tin nhắn phát lại phải được bỏ qua.

## Truyền lại bắt tay

### Yêu cầu Phiên

Nếu Alice không nhận được Session Created hoặc Retry:

Duy trì cùng ID nguồn và kết nối, khóa tạm thời, và số gói tin 0. Hoặc, chỉ cần giữ lại và truyền lại cùng gói tin đã mã hóa. Số gói tin không được tăng lên, vì điều đó sẽ thay đổi giá trị hash liên kết được sử dụng để mã hóa thông điệp Session Created.

Khoảng thời gian truyền lại được khuyến nghị: 1.25, 2.5, và 5 giây (1.25, 3.75, và 8.75 giây sau lần gửi đầu tiên). Thời gian chờ được khuyến nghị: tổng cộng 15 giây

### Phiên đã được tạo

Nếu Bob không nhận được Session Confirmed:

Duy trì cùng source và connection ID, ephemeral key, và packet number 0. Hoặc chỉ giữ lại encrypted packet. Packet number không được tăng, bởi vì điều đó sẽ thay đổi giá trị chained hash được sử dụng để mã hóa thông điệp Session Confirmed.

Khoảng thời gian truyền lại được khuyến nghị: 1, 2, và 4 giây (1, 3, và 7 giây sau lần gửi đầu tiên). Thời gian chờ được khuyến nghị: tổng cộng 12 giây

### Phiên Đã Được Xác Nhận

Trong SSU 1, Alice không chuyển sang giai đoạn dữ liệu cho đến khi nhận được gói dữ liệu đầu tiên từ Bob. Điều này làm cho SSU 1 có thiết lập hai vòng khứ hồi.

Đối với SSU 2, các khoảng thời gian truyền lại Session Confirmed được khuyến nghị: 1.25, 2.5, và 5 giây (1.25, 3.75, và 8.75 giây sau lần gửi đầu tiên).

Có một số lựa chọn thay thế. Tất cả đều là 1 RTT:

1) Alice giả định rằng Session Confirmed đã được nhận, gửi các thông điệp dữ liệu ngay lập tức, không bao giờ truyền lại Session Confirmed. Các gói dữ liệu nhận được không theo thứ tự (trước Session Confirmed) sẽ không thể giải mã được, nhưng sẽ được truyền lại. Nếu Session Confirmed bị mất, tất cả các thông điệp dữ liệu đã gửi sẽ bị loại bỏ. 2) Như trong 1), gửi các thông điệp dữ liệu ngay lập tức, nhưng cũng truyền lại Session Confirmed cho đến khi nhận được một thông điệp dữ liệu. 3) Chúng ta có thể sử dụng IK thay vì XK, vì nó chỉ có hai thông điệp trong quá trình bắt tay, nhưng nó sử dụng thêm một DH (4 thay vì 3).

Cách triển khai được khuyến nghị là tùy chọn 2). Alice phải giữ lại thông tin cần thiết để truyền lại thông điệp Session Confirmed. Alice cũng nên truyền lại tất cả các thông điệp Data sau khi thông điệp Session Confirmed được truyền lại.

Khi truyền lại Session Confirmed, giữ nguyên source ID và connection ID, ephemeral key, và packet number 1. Hoặc, chỉ cần giữ lại encrypted packet. Packet number không được tăng lên, vì điều đó sẽ thay đổi giá trị chained hash - đây là đầu vào cho hàm split().

Bob có thể giữ lại (xếp hàng) các thông điệp dữ liệu nhận được trước thông điệp Session Confirmed. Cả khóa bảo vệ header và khóa giải mã đều không có sẵn trước khi nhận được thông điệp Session Confirmed, vì vậy Bob không biết đó là các thông điệp dữ liệu, nhưng có thể giả định như vậy. Sau khi nhận được thông điệp Session Confirmed, Bob có thể giải mã và xử lý các thông điệp Data đã xếp hàng. Nếu điều này quá phức tạp, Bob có thể chỉ cần loại bỏ các thông điệp Data không thể giải mã được, vì Alice sẽ truyền lại chúng.

Lưu ý: Nếu các gói session confirmed bị mất, Bob sẽ truyền lại session created. Header của session created sẽ không thể giải mã được bằng intro key của Alice, vì nó được thiết lập bằng intro key của Bob (trừ khi thực hiện giải mã dự phòng bằng intro key của Bob). Bob có thể ngay lập tức truyền lại các gói session confirmed nếu chưa được ack trước đó, và một gói không thể giải mã được nhận.

### Yêu cầu Token

Nếu Alice không nhận được Retry:

Duy trì cùng ID nguồn và ID kết nối. Một triển khai có thể tạo một số gói ngẫu nhiên mới và mã hóa một gói mới; Hoặc có thể tái sử dụng cùng số gói hoặc chỉ giữ lại và truyền lại cùng gói đã mã hóa. Số gói không được tăng lên, vì điều đó sẽ thay đổi giá trị hash chuỗi được sử dụng để mã hóa thông điệp Session Created.

Khoảng thời gian retransmission được khuyến nghị: 3 và 6 giây (3 và 9 giây sau khi gửi lần đầu). Timeout được khuyến nghị: tổng cộng 15 giây

### Thử lại

Nếu Bob không nhận được Session Confirmed:

Một thông điệp Retry không được truyền lại khi hết thời gian chờ, để giảm tác động của các địa chỉ nguồn giả mạo.

Tuy nhiên, một thông điệp Retry có thể được truyền lại để phản hồi một thông điệp Session Request lặp lại được nhận với token gốc (không hợp lệ), hoặc để phản hồi một thông điệp Token Request lặp lại. Trong cả hai trường hợp, điều này cho thấy thông điệp Retry đã bị mất.

Nếu nhận được tin nhắn Session Request thứ hai với token khác nhưng vẫn không hợp lệ, hãy loại bỏ phiên đang chờ xử lý và không phản hồi.

Nếu gửi lại thông điệp Retry: Giữ nguyên source và connection ID cũng như token. Một implementation có thể tạo ra một packet number ngẫu nhiên mới và mã hóa một packet mới; Hoặc có thể tái sử dụng cùng một packet number hoặc chỉ giữ lại và truyền lại cùng một encrypted packet.

### Tổng Thời Gian Chờ

Thời gian timeout tổng được khuyến nghị cho handshake là 20 giây.

### Xử lý Trùng lặp và Lỗi

Các bản sao của ba thông điệp handshake Noise Session Request, Session Created, và Session Confirmed phải được phát hiện trước khi MixHash() của header. Trong khi quá trình xử lý Noise AEAD có thể sẽ thất bại sau đó, hash handshake đã bị hỏng từ trước.

Nếu bất kỳ một trong ba thông điệp nào bị hỏng và không vượt qua được AEAD, quá trình handshake không thể phục hồi được sau đó ngay cả khi truyền lại, vì MixHash() đã được gọi trên thông điệp bị hỏng.

## Token

Token trong header Session Request được sử dụng để giảm thiểu DoS, ngăn chặn giả mạo địa chỉ nguồn, và chống lại các cuộc tấn công replay.

Nếu Bob không chấp nhận token trong thông điệp Session Request, Bob KHÔNG giải mã thông điệp, vì nó yêu cầu một phép toán DH tốn kém. Bob chỉ đơn giản gửi một thông điệp Retry với một token mới.

Nếu sau đó nhận được thông điệp Session Request với token đó, Bob tiến hành giải mã thông điệp đó và tiếp tục với quá trình handshake.

Token phải là một giá trị 8 byte được tạo ngẫu nhiên, nếu bộ tạo token lưu trữ các giá trị và IP cùng port liên quan (trong bộ nhớ hoặc liên tục). Bộ tạo không được tạo một giá trị mờ đục, ví dụ, sử dụng SipHash (với seed bí mật K0, K1) của IP, port, và giờ hoặc ngày hiện tại, để tạo các token không cần được lưu trong bộ nhớ, bởi vì phương pháp này làm cho việc từ chối các token được sử dụng lại và các cuộc tấn công replay trở nên khó khăn. Tuy nhiên, đây là chủ đề để nghiên cứu thêm nếu chúng ta có thể chuyển sang một sơ đồ như vậy, như [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) thực hiện, sử dụng HMAC 16-byte của một server secret và địa chỉ IP.

Token chỉ có thể được sử dụng một lần. Một token được gửi từ Bob đến Alice trong thông điệp Retry phải được sử dụng ngay lập tức và sẽ hết hạn trong vài giây. Một token được gửi trong khối New Token trong một phiên đã thiết lập có thể được sử dụng trong kết nối tiếp theo, và nó sẽ hết hạn vào thời gian được chỉ định trong khối đó. Thời gian hết hạn được xác định bởi người gửi; các giá trị khuyến nghị là tối thiểu vài phút, tối đa một hoặc nhiều giờ, tùy thuộc vào mức độ overhead mong muốn tối đa của các token được lưu trữ.

Nếu IP hoặc port của router thay đổi, nó phải xóa tất cả các token đã lưu (cả inbound và outbound) cho IP hoặc port cũ, vì chúng không còn hợp lệ. Token có thể được lưu trữ qua các lần khởi động lại router, tùy thuộc vào cách triển khai. Việc chấp nhận token chưa hết hạn không được đảm bảo; nếu Bob đã quên hoặc xóa các token đã lưu, anh ta sẽ gửi Retry cho Alice. Router có thể chọn giới hạn việc lưu trữ token và xóa các token được lưu trữ lâu nhất ngay cả khi chúng chưa hết hạn.

Các khối New Token có thể được gửi từ Alice đến Bob hoặc từ Bob đến Alice. Chúng thường được gửi ít nhất một lần, trong hoặc ngay sau khi thiết lập phiên. Do các kiểm tra xác thực RouterInfo trong thông điệp Session Confirmed, Bob không nên gửi khối New Token trong thông điệp Session Created, nó có thể được gửi cùng với ACK 0 và Router Info sau khi Session Confirmed được nhận và xác thực.

Vì thời gian tồn tại của phiên thường dài hơn thời gian hết hạn của token, token nên được gửi lại trước hoặc sau khi hết hạn với thời gian hết hạn mới, hoặc một token mới nên được gửi. Các router nên giả định rằng chỉ có token cuối cùng nhận được là hợp lệ; không có yêu cầu phải lưu trữ nhiều token inbound hoặc outbound cho cùng một IP/port.

Một token được ràng buộc với sự kết hợp của IP/port nguồn và IP/port đích. Một token nhận được trên IPv4 không thể được sử dụng cho IPv6 hoặc ngược lại.

Nếu một trong hai peer di chuyển sang IP hoặc port mới trong suốt phiên kết nối (xem phần Connection Migration), bất kỳ token nào đã trao đổi trước đó sẽ bị vô hiệu hóa, và các token mới phải được trao đổi.

Các triển khai có thể, nhưng không bắt buộc phải, lưu các token trên đĩa và tải lại chúng khi khởi động lại. Nếu được lưu trữ lâu dài, triển khai phải đảm bảo rằng IP và port không thay đổi kể từ khi tắt máy trước khi tải lại chúng.

## Phân mảnh thông điệp I2NP

Sự khác biệt so với SSU 1

Lưu ý: Như trong SSU 1, fragment đầu tiên không chứa thông tin về tổng số fragment hoặc tổng độ dài. Các fragment tiếp theo không chứa thông tin về vị trí offset của chúng. Điều này cung cấp cho người gửi tính linh hoạt để phân mảnh "tức thì" dựa trên không gian có sẵn trong packet. (Java I2P không làm như vậy; nó "phân mảnh trước" trước khi fragment đầu tiên được gửi) Tuy nhiên, điều này tạo gánh nặng cho người nhận phải lưu trữ các fragment nhận được không theo thứ tự và trì hoãn việc tái lắp ráp cho đến khi tất cả fragment được nhận.

Như trong SSU 1, bất kỳ việc truyền lại nào của các fragment đều phải bảo toàn độ dài (và offset ngầm định) của lần truyền trước đó của fragment.

SSU 2 tách biệt ba trường hợp (thông điệp đầy đủ, fragment ban đầu, và fragment tiếp theo) thành ba loại block khác nhau, để cải thiện hiệu suất xử lý.

## Sao chép Thông điệp I2NP

Giao thức này KHÔNG ngăn chặn hoàn toàn việc gửi trùng lặp các tin nhắn I2NP. Các bản sao ở tầng IP hoặc các cuộc tấn công replay sẽ được phát hiện tại tầng SSU2, bởi vì mỗi số gói tin chỉ có thể được sử dụng một lần.

Tuy nhiên, khi các thông điệp I2NP hoặc các mảnh được truyền lại trong các gói tin mới, điều này không thể phát hiện được ở tầng SSU2. Router nên thực thi việc hết hạn I2NP (cả quá cũ và quá xa trong tương lai) và sử dụng bộ lọc Bloom hoặc cơ chế khác dựa trên ID thông điệp I2NP.

Các cơ chế bổ sung có thể được sử dụng bởi router, hoặc trong triển khai SSU2, để phát hiện các bản trùng lặp. Ví dụ, SSU2 có thể duy trì một bộ nhớ đệm các ID tin nhắn đã nhận gần đây. Điều này phụ thuộc vào cách triển khai.

## Kiểm Soát Tắc Nghẽn

Đặc tả này quy định giao thức cho việc đánh số gói tin và các khối ACK. Điều này cung cấp đủ thông tin thời gian thực để bộ truyền có thể triển khai một thuật toán kiểm soát tắc nghẽn hiệu quả và phản hồi nhanh, đồng thời cho phép tính linh hoạt và đổi mới trong việc triển khai đó. Phần này thảo luận về các mục tiêu triển khai và đưa ra các đề xuất. Hướng dẫn chung có thể được tìm thấy trong [RFC-9002](https://tools.ietf.org/html/rfc9002). Xem thêm [RFC-6298](https://tools.ietf.org/html/rfc6298) để được hướng dẫn về bộ đếm thời gian truyền lại.

Các gói dữ liệu chỉ chứa ACK không nên được tính vào số byte hoặc số gói đang truyền và không được kiểm soát tắc nghẽn. Khác với TCP, SSU2 có thể phát hiện sự mất mát của các gói này và thông tin đó có thể được sử dụng để điều chỉnh trạng thái tắc nghẽn. Tuy nhiên, tài liệu này không chỉ định cơ chế để thực hiện điều đó.

Các gói tin chứa một số khối không phải dữ liệu khác cũng có thể được loại trừ khỏi kiểm soát tắc nghẽn nếu muốn, tùy thuộc vào cách triển khai. Ví dụ:

- Peer Test
- Relay request/intro/response
- Path challenge/response

Khuyến nghị rằng việc kiểm soát tắc nghẽn nên dựa trên số byte, không phải số gói tin, theo hướng dẫn trong các TCP RFC và QUIC [RFC-9002](https://tools.ietf.org/html/rfc9002). Một giới hạn số gói tin bổ sung cũng có thể hữu ích để ngăn chặn tràn buffer trong kernel hoặc trong các middlebox, tùy thuộc vào triển khai, mặc dù điều này có thể làm tăng độ phức tạp đáng kể. Nếu đầu ra gói tin theo từng phiên và/hoặc tổng thể bị giới hạn băng thông và/hoặc được điều chỉnh tốc độ, điều này có thể giảm thiểu nhu cầu giới hạn số gói tin.

### Số Thứ Tự Gói Tin

Trong SSU 1, các ACK và NACK chứa số thứ tự I2NP message và bitmask của các fragment. Các transmitter theo dõi trạng thái ACK của các message gửi đi (và các fragment của chúng) và truyền lại các fragment khi cần thiết.

Trong SSU 2, ACK và NACK chứa số hiệu gói tin. Các bộ truyền phải duy trì cấu trúc dữ liệu với ánh xạ từ số hiệu gói tin đến nội dung của chúng. Khi một gói tin được ACK hoặc NACK, bộ truyền phải xác định những I2NP message và fragment nào có trong gói tin đó, để quyết định những gì cần truyền lại.

### Session Confirmed ACK

Bob gửi một ACK của gói tin 0, điều này xác nhận thông điệp Session Confirmed và cho phép Alice tiến hành đến giai đoạn dữ liệu, đồng thời loại bỏ thông điệp Session Confirmed lớn đang được lưu để có thể truyền lại. Điều này thay thế cho DeliveryStatusMessage được gửi bởi Bob trong SSU 1.

Bob nên gửi ACK càng sớm càng tốt sau khi nhận được thông báo Session Confirmed. Một độ trễ nhỏ (không quá 50 ms) là chấp nhận được, vì ít nhất một thông báo Data sẽ đến gần như ngay lập tức sau thông báo Session Confirmed, để ACK có thể xác nhận cả Session Confirmed và thông báo Data. Điều này sẽ ngăn Bob phải truyền lại thông báo Session Confirmed.

### Tạo ACK

Định nghĩa: Các gói tin gây ra ack: Các gói tin chứa các khối gây ra ack sẽ kích thích một ACK từ bên nhận trong thời gian trễ xác nhận tối đa và được gọi là các gói tin gây ra ack.

Các router xác nhận tất cả các gói tin mà chúng nhận và xử lý. Tuy nhiên, chỉ những gói tin yêu cầu xác nhận mới khiến một khối ACK được gửi trong thời gian trễ xác nhận tối đa. Những gói tin không yêu cầu xác nhận chỉ được xác nhận khi một khối ACK được gửi vì các lý do khác.

Khi gửi một gói tin vì bất kỳ lý do gì, một endpoint nên cố gắng bao gồm một khối ACK nếu một khối chưa được gửi gần đây. Việc làm này giúp phát hiện mất mát kịp thời tại peer.

Nhìn chung, phản hồi thường xuyên từ bên nhận sẽ cải thiện khả năng phản ứng với mất mát và tắc nghẽn, nhưng điều này phải được cân bằng với tải quá mức được tạo ra bởi bên nhận khi gửi một ACK block để phản hồi mỗi gói tin yêu cầu xác nhận. Hướng dẫn được đưa ra dưới đây nhằm tìm ra sự cân bằng này.

Các gói dữ liệu trong phiên chứa bất kỳ khối nào NGOẠI TRỪ những khối sau đây đều yêu cầu xác nhận:

- Khối ACK
- Khối địa chỉ
- Khối DateTime
- Khối đệm
- Khối kết thúc
- Khác?

Các gói tin ngoài phiên, bao gồm thông điệp bắt tay và thông điệp kiểm tra ngang hàng 5-7, có cơ chế xác nhận riêng của chúng. Xem bên dưới.

### ACK bắt tay

Đây là những trường hợp đặc biệt:

- Token Request được xác nhận ngầm định bởi Retry
- Session Request được xác nhận ngầm định bởi Session Created hoặc Retry
- Retry được xác nhận ngầm định bởi Session Request
- Session Created được xác nhận ngầm định bởi Session Confirmed
- Session Confirmed nên được xác nhận ngay lập tức

### Gửi các khối ACK

Các khối ACK được sử dụng để xác nhận các gói tin trong giai đoạn dữ liệu. Chúng chỉ được bao gồm cho các gói tin giai đoạn dữ liệu trong phiên.

Mỗi gói tin phải được xác nhận ít nhất một lần, và các gói tin yêu cầu xác nhận phải được xác nhận ít nhất một lần trong thời gian trễ tối đa.

Một endpoint phải xác nhận tất cả các gói handshake yêu cầu ack ngay lập tức trong thời gian trễ tối đa của nó, với ngoại lệ sau đây. Trước khi xác nhận handshake, một endpoint có thể không có các khóa mã hóa header của gói để giải mã các gói khi chúng được nhận. Do đó, nó có thể đệm chúng và xác nhận chúng khi các khóa cần thiết trở nên khả dụng.

Vì các gói tin chỉ chứa khối ACK không được kiểm soát tắc nghẽn, một endpoint không được gửi nhiều hơn một gói tin như vậy để phản hồi khi nhận được một gói tin yêu cầu xác nhận.

Một endpoint không được gửi gói tin non-ack-eliciting để phản hồi một gói tin non-ack-eliciting, ngay cả khi có những khoảng trống gói tin xuất hiện trước gói tin đã nhận. Điều này tránh vòng lặp phản hồi vô hạn của các xác nhận, có thể ngăn kết nối trở về trạng thái nhàn rỗi. Các gói tin non-ack-eliciting cuối cùng sẽ được xác nhận khi endpoint gửi khối ACK để phản hồi các sự kiện khác.

Một endpoint chỉ gửi các ACK block sẽ không nhận được acknowledgment từ peer của nó trừ khi những acknowledgment đó được bao gồm trong các packet có chứa ack-eliciting block. Một endpoint nên gửi một ACK block cùng với các block khác khi có các ack-eliciting packet mới cần được acknowledge. Khi chỉ có các non-ack-eliciting packet cần được acknowledged, một endpoint CÓ THỂ chọn không gửi ACK block cùng với các outgoing block cho đến khi một ack-eliciting packet đã được nhận.

Một endpoint chỉ gửi các gói non-ack-eliciting có thể chọn thỉnh thoảng thêm một khối ack-eliciting vào những gói đó để đảm bảo nhận được xác nhận. Trong trường hợp đó, endpoint KHÔNG ĐƯỢC gửi khối ack-eliciting trong tất cả các gói mà lẽ ra sẽ là non-ack-eliciting, để tránh vòng lặp phản hồi vô tận của các xác nhận.

Để hỗ trợ phát hiện mất gói tin tại bên gửi, một endpoint nên tạo và gửi một ACK block mà không chậm trễ khi nhận được một gói tin ack-eliciting trong bất kỳ trường hợp nào sau đây:

- Khi gói tin nhận được có số thứ tự gói tin nhỏ hơn một gói tin ack-eliciting khác đã được nhận
- Khi gói tin có số thứ tự gói tin lớn hơn gói tin ack-eliciting có số thứ tự cao nhất đã được nhận và có các gói tin bị thiếu giữa gói tin đó và gói tin này.
- Khi cờ ack-immediate trong header gói tin được thiết lập

Các thuật toán được kỳ vọng sẽ có khả năng phục hồi đối với những receiver không tuân theo hướng dẫn đã đưa ra ở trên. Tuy nhiên, một implementation chỉ nên khác biệt với những yêu cầu này sau khi cân nhắc cẩn thận về những tác động hiệu suất của sự thay đổi, đối với các kết nối được tạo bởi endpoint và đối với những người dùng khác của mạng.

### Tần suất ACK

Bên nhận xác định tần suất gửi thông báo xác nhận để phản hồi các gói tin yêu cầu xác nhận. Việc xác định này liên quan đến một sự cân bằng.

Các điểm cuối dựa vào việc xác nhận kịp thời để phát hiện mất mát. Các bộ điều khiển tắc nghẽn dựa trên cửa sổ dựa vào việc xác nhận để quản lý cửa sổ tắc nghẽn của chúng. Trong cả hai trường hợp, việc trì hoãn xác nhận có thể ảnh hưởng xấu đến hiệu suất.

Mặt khác, việc giảm tần suất các gói tin chỉ mang thông tin xác nhận sẽ giảm chi phí truyền và xử lý gói tin tại cả hai đầu cuối. Điều này có thể cải thiện thông lượng kết nối trên các liên kết bất đối xứng nghiêm trọng và giảm lượng lưu lượng xác nhận sử dụng dung lượng đường về; xem Mục 3 của [RFC-3449](https://tools.ietf.org/html/rfc3449).

Một receiver nên gửi một khối ACK sau khi nhận được ít nhất hai gói tin ack-eliciting. Khuyến nghị này mang tính chất tổng quát và phù hợp với các khuyến nghị về hành vi của TCP endpoint [RFC-5681](https://tools.ietf.org/html/rfc5681). Hiểu biết về điều kiện mạng, hiểu biết về bộ điều khiển tắc nghẽn của peer, hoặc nghiên cứu và thử nghiệm sâu hơn có thể đề xuất các chiến lược xác nhận thay thế với đặc tính hiệu suất tốt hơn.

Một bên nhận có thể xử lý nhiều gói tin có sẵn trước khi quyết định có gửi khối ACK để phản hồi hay không. Nói chung, bên nhận không nên trì hoãn việc gửi ACK quá RTT / 6, hoặc tối đa 150 ms.

Cờ ack-immediate trong header của gói dữ liệu là một yêu cầu để bên nhận gửi ack ngay sau khi nhận, có thể trong vòng vài ms. Nói chung, bên nhận không nên trì hoãn ACK ngay lập tức quá RTT / 16, hoặc tối đa 5 ms.

### Cờ ACK Ngay lập tức

Bên nhận không biết kích thước cửa sổ gửi của bên gửi, và do đó không biết cần trễ bao lâu trước khi gửi ACK. Cờ ACK ngay lập tức trong header gói dữ liệu là một cách quan trọng để duy trì thông lượng tối đa bằng cách giảm thiểu RTT hiệu quả. Cờ ACK ngay lập tức là byte 13 của header, bit 0, tức là (header[13] & 0x01). Khi được thiết lập, một ACK ngay lập tức được yêu cầu. Xem phần short header ở trên để biết chi tiết.

Có một số chiến lược có thể mà người gửi có thể sử dụng để xác định khi nào nên đặt cờ immediate-ack:

- Được đặt một lần sau mỗi N gói tin, với N là số nhỏ
- Được đặt trên gói tin cuối cùng trong một chuỗi gói tin
- Được đặt khi cửa sổ gửi gần đầy, ví dụ trên 2/3 dung lượng
- Được đặt trên tất cả các gói tin có các fragment được truyền lại

Cờ ACK ngay lập tức chỉ cần thiết trên các gói dữ liệu chứa thông điệp I2NP hoặc các phân đoạn thông điệp.

### Kích thước khối ACK

Khi một khối ACK được gửi, một hoặc nhiều phạm vi các gói tin đã được xác nhận sẽ được bao gồm. Việc bao gồm các xác nhận cho các gói tin cũ hơn sẽ giảm khả năng xảy ra các truyền lại giả do mất các khối ACK đã gửi trước đó, nhưng đổi lại là các khối ACK sẽ lớn hơn.

Các ACK block luôn phải xác nhận các gói tin được nhận gần đây nhất, và càng nhiều gói tin bị lộn xộn thứ tự thì càng quan trọng phải gửi ACK block cập nhật một cách nhanh chóng, để ngăn peer tuyên bố một gói tin bị mất và truyền lại một cách sai lầm các block mà nó chứa. Một ACK block phải vừa trong một gói tin duy nhất. Nếu không vừa, thì các dải cũ hơn (những dải có số packet nhỏ nhất) sẽ bị bỏ qua.

Một receiver giới hạn số lượng phạm vi ACK mà nó ghi nhớ và gửi trong các ACK block, vừa để giới hạn kích thước của ACK block vừa để tránh cạn kiệt tài nguyên. Sau khi nhận được acknowledgment cho một ACK block, receiver nên ngừng theo dõi những phạm vi ACK đã được acknowledge đó. Các sender có thể mong đợi acknowledgment cho hầu hết các packet, nhưng giao thức này không đảm bảo việc nhận được acknowledgment cho mọi packet mà receiver xử lý.

Có thể việc giữ lại nhiều phạm vi ACK có thể khiến khối ACK trở nên quá lớn. Một receiver có thể loại bỏ các phạm vi ACK chưa được xác nhận để giới hạn kích thước khối ACK, với cái giá phải trả là tăng số lần truyền lại từ sender. Điều này là cần thiết nếu một khối ACK quá lớn để có thể vừa trong một packet. Các receiver cũng có thể giới hạn kích thước khối ACK hơn nữa để bảo toàn không gian cho các khối khác hoặc để giới hạn băng thông mà các xác nhận tiêu thụ.

Một bên nhận phải giữ lại phạm vi ACK trừ khi nó có thể đảm bảo rằng sau đó sẽ không chấp nhận các gói tin có số trong phạm vi đó. Duy trì một số gói tin tối thiểu tăng lên khi các phạm vi bị loại bỏ là một cách để đạt được điều này với trạng thái tối thiểu.

Các bên nhận có thể loại bỏ tất cả các phạm vi ACK, nhưng chúng phải giữ lại số gói tin lớn nhất đã được xử lý thành công, vì số này được sử dụng để khôi phục số gói tin từ các gói tin tiếp theo.

Phần sau mô tả một cách tiếp cận mẫu để xác định những gói tin nào cần xác nhận trong mỗi khối ACK. Mặc dù mục tiêu của thuật toán này là tạo ra một xác nhận cho mỗi gói tin được xử lý, vẫn có thể xảy ra tình况 mất mát các xác nhận.

### Giới hạn Phạm vi bằng cách Theo dõi các Khối ACK

Khi một gói tin chứa khối ACK được gửi, trường Ack Through trong khối đó có thể được lưu lại. Khi một gói tin chứa khối ACK được xác nhận, bên nhận có thể ngừng xác nhận các gói tin nhỏ hơn hoặc bằng trường Ack Through trong khối ACK đã gửi.

Một receiver chỉ gửi các gói tin không yêu cầu xác nhận, chẳng hạn như các ACK block, có thể không nhận được xác nhận trong một khoảng thời gian dài. Điều này có thể khiến receiver phải duy trì trạng thái cho một số lượng lớn ACK block trong thời gian dài, và các ACK block mà nó gửi có thể có kích thước không cần thiết lớn. Trong trường hợp như vậy, receiver có thể gửi một PING hoặc block yêu cầu xác nhận nhỏ khác thỉnh thoảng, chẳng hạn như một lần mỗi vòng truyền, để yêu cầu ACK từ peer.

Trong các trường hợp không có mất mát ACK block, thuật toán này cho phép tối thiểu 1 RTT để sắp xếp lại. Trong các trường hợp có mất mát ACK block và sắp xếp lại, cách tiếp cận này không đảm bảo rằng mọi xác nhận đều được người gửi thấy trước khi nó không còn được bao gồm trong ACK block. Các gói có thể được nhận không theo thứ tự, và tất cả các ACK block tiếp theo chứa chúng có thể bị mất. Trong trường hợp này, thuật toán khôi phục mất mát có thể gây ra các lần truyền lại giả, nhưng người gửi sẽ tiếp tục tiến triển về phía trước.

### Tắc nghẽn

Các transport I2P không đảm bảo việc giao nhận có thứ tự của các thông điệp I2NP. Do đó, việc mất một thông điệp Data chứa một hoặc nhiều thông điệp I2NP hoặc các fragment KHÔNG ngăn cản các thông điệp I2NP khác được giao nhận; không có hiện tượng chặn đầu hàng đợi. Các triển khai nên tiếp tục gửi các thông điệp mới trong giai đoạn khôi phục mất mát nếu cửa sổ gửi cho phép.

### Truyền lại

Bên gửi không nên giữ lại toàn bộ nội dung của thông điệp để truyền lại một cách giống hệt (ngoại trừ các thông điệp bắt tay, xem phần trên). Bên gửi phải lắp ráp các thông điệp chứa thông tin cập nhật (ACK, NACK, và dữ liệu chưa được xác nhận) mỗi khi gửi thông điệp. Bên gửi nên tránh truyền lại thông tin từ các thông điệp một khi chúng đã được xác nhận. Điều này bao gồm các thông điệp được xác nhận sau khi bị tuyên bố mất, có thể xảy ra khi có sự sắp xếp lại thứ tự trong mạng.

### Cửa sổ

Chưa xác định. Hướng dẫn chung có thể được tìm thấy trong [RFC-9002](https://tools.ietf.org/html/rfc9002).

## Di chuyển Kết nối

IP hoặc cổng của một peer có thể thay đổi trong suốt thời gian tồn tại của phiên kết nối. Sự thay đổi IP có thể do luân chuyển địa chỉ tạm thời IPv6, thay đổi IP định kỳ do ISP thực hiện, client di động chuyển đổi giữa IP WiFi và cellular, hoặc các thay đổi mạng cục bộ khác. Sự thay đổi cổng có thể do NAT rebinding sau khi binding trước đó hết thời gian chờ.

IP hoặc cổng của một peer có thể xuất hiện thay đổi do các cuộc tấn công trên đường truyền và ngoài đường truyền khác nhau, bao gồm việc sửa đổi hoặc chèn gói tin.

Connection migration là quá trình mà một source endpoint mới (IP+port) được xác thực, đồng thời ngăn chặn các thay đổi chưa được xác thực. Quá trình này là phiên bản đơn giản hóa của quy trình được định nghĩa trong QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000). Quá trình này chỉ được định nghĩa cho giai đoạn truyền dữ liệu của một phiên. Migration không được phép trong quá trình handshake. Tất cả các gói handshake phải được xác minh là từ cùng một IP và port như các gói đã gửi và nhận trước đó. Nói cách khác, IP và port của một peer phải không đổi trong suốt quá trình handshake.

### Mô Hình Đe Dọa

(Chuyển thể từ QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000))

#### Giả mạo địa chỉ peer

Một peer có thể giả mạo địa chỉ nguồn của nó để khiến một endpoint gửi lượng dữ liệu quá mức đến một host không mong muốn. Nếu endpoint gửi nhiều dữ liệu hơn đáng kể so với peer giả mạo, việc di chuyển kết nối có thể được sử dụng để khuếch đại khối lượng dữ liệu mà kẻ tấn công có thể tạo ra nhắm vào nạn nhân.

#### Giả mạo địa chỉ trên đường truyền

Một kẻ tấn công trên đường truyền có thể gây ra việc di chuyển kết nối giả mạo bằng cách sao chép và chuyển tiếp một gói tin với địa chỉ giả mạo sao cho nó đến trước gói tin gốc. Gói tin với địa chỉ giả mạo sẽ được coi là đến từ một kết nối đang di chuyển, và gói tin gốc sẽ được coi là trùng lặp và bị loại bỏ. Sau một lần di chuyển giả mạo, việc xác thực địa chỉ nguồn sẽ thất bại vì thực thể tại địa chỉ nguồn không có các khóa mật mã cần thiết để đọc hoặc phản hồi Path Challenge được gửi đến nó ngay cả khi nó muốn.

#### Chuyển Tiếp Gói Tin Ngoài Đường Dẫn

Một kẻ tấn công off-path có thể quan sát các gói tin có thể chuyển tiếp bản sao của các gói tin thật đến các điểm cuối. Nếu gói tin được sao chép đến trước gói tin thật, điều này sẽ xuất hiện như một NAT rebinding. Bất kỳ gói tin thật nào sẽ bị loại bỏ như một bản sao. Nếu kẻ tấn công có thể tiếp tục chuyển tiếp các gói tin, nó có thể gây ra việc di chuyển đến một đường dẫn qua kẻ tấn công. Điều này đặt kẻ tấn công vào vị trí on-path, cho phép nó quan sát hoặc loại bỏ tất cả các gói tin tiếp theo.

#### Tác động đến Quyền riêng tư

QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) quy định thay đổi ID kết nối khi thay đổi đường dẫn mạng. Việc sử dụng ID kết nối ổn định trên nhiều đường dẫn mạng sẽ cho phép người quan sát thụ động tương quan hoạt động giữa các đường dẫn đó. Một endpoint di chuyển giữa các mạng có thể không muốn hoạt động của họ bị tương quan bởi bất kỳ thực thể nào khác ngoài đối tác của họ. Tuy nhiên, QUIC không mã hóa ID kết nối trong header. SSU2 có làm điều đó, vì vậy việc rò rỉ quyền riêng tư sẽ yêu cầu người quan sát thụ động cũng phải có quyền truy cập vào cơ sở dữ liệu mạng để lấy khóa giới thiệu cần thiết để giải mã ID kết nối. Ngay cả với khóa giới thiệu, đây không phải là một cuộc tấn công mạnh, và chúng tôi không thay đổi ID kết nối sau khi di chuyển trong SSU2, vì điều này sẽ là một biến chứng đáng kể.

### Khởi tạo Xác thực Đường dẫn

Trong giai đoạn dữ liệu, các peer phải kiểm tra IP nguồn và cổng của mỗi gói dữ liệu nhận được. Nếu IP hoặc cổng khác với những gì đã nhận trước đó, VÀ gói tin không phải là số gói trùng lặp, VÀ gói tin được giải mã thành công, thì phiên sẽ chuyển sang giai đoạn xác thực đường dẫn.

Ngoài ra, một peer phải xác minh rằng IP và port mới là hợp lệ theo các quy tắc xác thực cục bộ (không bị chặn, không phải port bất hợp pháp, v.v.). Các peer KHÔNG được yêu cầu hỗ trợ di chuyển giữa IPv4 và IPv6, và có thể coi IP mới trong họ địa chỉ khác là không hợp lệ, vì đây không phải là hành vi mong đợi và có thể làm tăng đáng kể độ phức tạp của việc triển khai. Khi nhận được gói tin từ IP/port không hợp lệ, một implementation có thể đơn giản bỏ qua nó, hoặc có thể khởi tạo xác thực đường dẫn với IP/port cũ.

Khi bước vào giai đoạn xác thực đường dẫn, hãy thực hiện các bước sau:

- Bắt đầu bộ đếm thời gian timeout xác thực đường dẫn trong vài giây, hoặc vài lần RTO hiện tại (TBD)
- Giảm congestion window xuống mức tối thiểu
- Giảm PMTU xuống mức tối thiểu (1280)
- Gửi một data packet chứa Path Challenge block, Address block (chứa IP/port mới), và thường là ACK block, đến IP và port mới. Packet này sử dụng cùng connection ID và encryption keys như session hiện tại. Dữ liệu Path Challenge block phải chứa đủ entropy (ít nhất 8 bytes) để không thể bị spoofed.
- Tùy chọn, cũng gửi Path Challenge đến IP/port cũ, với dữ liệu block khác. Xem bên dưới.
- Bắt đầu bộ đếm thời gian timeout Path Response dựa trên RTO hiện tại (thường là RTT + bội số của RTTdev)

Trong giai đoạn xác thực đường dẫn, phiên có thể tiếp tục xử lý các gói tin đến. Dù từ IP/cổng cũ hay mới. Phiên cũng có thể tiếp tục gửi và xác nhận các gói dữ liệu. Tuy nhiên, cửa sổ tắc nghẽn và PMTU phải duy trì ở giá trị tối thiểu trong giai đoạn xác thực đường dẫn, để ngăn chặn việc bị sử dụng cho các cuộc tấn công từ chối dịch vụ bằng cách gửi lưu lượng lớn đến địa chỉ giả mạo.

Một implementation có thể, nhưng không bắt buộc, cố gắng xác thực nhiều đường dẫn đồng thời. Điều này có lẽ không đáng để phức tạp hóa. Nó có thể, nhưng không bắt buộc, nhớ một IP/port trước đó đã được xác thực, và bỏ qua việc xác thực đường dẫn nếu một peer quay trở lại IP/port trước đó của nó.

Nếu nhận được Path Response chứa dữ liệu giống hệt như đã gửi trong Path Challenge, thì Path Validation đã thành công. IP/port nguồn của thông báo Path Response không bắt buộc phải giống với địa chỉ mà Path Challenge đã được gửi đến.

Nếu không nhận được Path Response trước khi bộ đếm thời gian Path Response hết hạn, hãy gửi một Path Challenge khác và nhân đôi bộ đếm thời gian Path Response.

Nếu không nhận được Path Response trước khi bộ đếm thời gian Path Validation hết hạn, thì Path Validation đã thất bại.

### Nội dung tin nhắn

Các thông điệp Data nên chứa các khối sau đây. Thứ tự không được chỉ định ngoại trừ Padding phải ở cuối cùng:

- Khối Path Challenge hoặc Path Response. Path Challenge chứa dữ liệu mờ (opaque), khuyến nghị tối thiểu 8 byte. Path Response chứa dữ liệu từ Path Challenge.
- Khối Address chứa IP có vẻ như của người nhận
- Khối DateTime
- Khối ACK
- Khối Padding

Không khuyến nghị bao gồm bất kỳ block nào khác (ví dụ như I2NP) trong thông điệp.

Được phép bao gồm một khối Path Challenge trong thông điệp chứa Path Response để khởi tạo việc xác thực theo hướng ngược lại.

Các khối Path Challenge và Path Response là ACK-eliciting. Path Challenge sẽ được ACK bởi một thông điệp Data chứa các khối Path Response và ACK. Path Response nên được ACK bởi một thông điệp Data chứa một khối ACK.

### Định tuyến trong quá trình Xác thực Đường dẫn

Đặc tả QUIC không rõ ràng về việc gửi các gói dữ liệu đến đâu trong quá trình xác thực đường dẫn - đến IP/port cũ hay mới? Cần có sự cân bằng giữa việc phản hồi nhanh chóng với các thay đổi IP/port và không gửi lưu lượng đến các địa chỉ giả mạo. Ngoài ra, các gói tin giả mạo không được phép tác động đáng kể đến một phiên kết nối hiện tại. Những thay đổi chỉ về port có thể xảy ra do NAT rebinding sau một thời gian không hoạt động; các thay đổi IP có thể xảy ra trong các giai đoạn lưu lượng cao ở một hoặc cả hai hướng.

Các chiến lược cần được nghiên cứu và cải tiến. Các khả năng bao gồm:

- Không gửi các gói dữ liệu đến IP/cổng mới cho đến khi được xác thực
- Tiếp tục gửi các gói dữ liệu đến IP/cổng cũ cho đến khi IP/cổng mới được xác thực
- Đồng thời xác thực lại IP/cổng cũ
- Không gửi bất kỳ dữ liệu nào cho đến khi IP/cổng cũ hoặc mới được xác thực
- Các chiến lược khác nhau cho việc thay đổi chỉ cổng so với việc thay đổi IP
- Các chiến lược khác nhau cho việc thay đổi IPv6 trong cùng /32, có thể do việc luân chuyển địa chỉ tạm thời

### Phản hồi Path Challenge

Khi nhận được Path Challenge, peer phải phản hồi bằng một gói dữ liệu chứa Path Response, với dữ liệu từ Path Challenge.

Path Response phải được gửi đến IP/port mà Path Challenge được nhận từ đó. Đây KHÔNG NHẤT THIẾT là IP/port đã được thiết lập trước đó cho peer. Điều này đảm bảo rằng việc xác thực đường dẫn bởi một peer chỉ thành công nếu đường dẫn hoạt động theo cả hai hướng. Xem phần Xác thực sau Thay đổi Cục bộ bên dưới.

Trừ khi IP/port khác với IP/port đã biết trước đó của peer, hãy xử lý Path Challenge như một ping đơn giản và chỉ cần phản hồi vô điều kiện bằng Path Response. Bên nhận không giữ hoặc thay đổi bất kỳ trạng thái nào dựa trên Path Challenge nhận được. Nếu IP/port khác biệt, một peer phải xác minh rằng IP và port mới hợp lệ theo các quy tắc xác thực cục bộ (không bị chặn, không phải port bất hợp pháp, v.v.). Các peer KHÔNG bắt buộc phải hỗ trợ phản hồi cross-address-family giữa IPv4 và IPv6, và có thể xử lý IP mới trong address family khác là không hợp lệ, vì đây không phải là hành vi mong đợi.

Trừ khi bị hạn chế bởi kiểm soát tắc nghẽn, Path Response nên được gửi ngay lập tức. Các triển khai nên thực hiện các biện pháp để giới hạn tốc độ Path Response hoặc băng thông được sử dụng nếu cần thiết.

Một khối Path Challenge thường được đi kèm với một khối Address trong cùng một thông điệp. Nếu khối address chứa một IP/cổng mới, một peer có thể xác thực IP/cổng đó và bắt đầu kiểm tra peer của IP/cổng mới đó, với session peer hoặc bất kỳ peer nào khác. Nếu peer cho rằng nó đang bị tường lửa chặn, và chỉ có cổng thay đổi, thì sự thay đổi này có thể là do NAT rebinding, và việc kiểm tra peer thêm có thể không cần thiết.

### Xác thực Đường dẫn Thành công

Khi xác thực đường dẫn thành công, kết nối sẽ được chuyển hoàn toàn sang IP/cổng mới. Khi thành công:

- Thoát khỏi giai đoạn xác thực đường dẫn
- Tất cả các gói tin được gửi đến IP và cổng mới.
- Các hạn chế về cửa sổ tắc nghẽn và PMTU được gỡ bỏ, và chúng được phép tăng lên. Không đơn giản khôi phục chúng về giá trị cũ, vì đường dẫn mới có thể có các đặc tính khác nhau.
- Nếu IP thay đổi, đặt RTT tính toán và RTO về giá trị ban đầu. Vì việc thay đổi chỉ cổng thường là kết quả của NAT rebinding hoặc hoạt động của middlebox khác, peer có thể thay vào đó giữ lại trạng thái kiểm soát tắc nghẽn và ước tính round-trip trong những trường hợp đó thay vì quay về giá trị ban đầu.
- Xóa (vô hiệu hóa) bất kỳ token nào đã gửi hoặc nhận cho IP/cổng cũ (tùy chọn)
- Gửi một token block mới cho IP/cổng mới (tùy chọn)

### Hủy bỏ Xác thực Đường dẫn

Trong giai đoạn xác thực đường truyền, bất kỳ gói tin hợp lệ, không trùng lặp nào được nhận từ IP/cổng cũ và được giải mã thành công sẽ khiến việc Xác thực Đường truyền bị hủy bỏ. Điều quan trọng là một quá trình xác thực đường truyền bị hủy bỏ do gói tin giả mạo không được gây ra việc chấm dứt hoặc gián đoạn nghiêm trọng một phiên kết nối hợp lệ.

Khi xác thực đường dẫn bị hủy:

- Thoát khỏi giai đoạn xác thực đường dẫn
- Tất cả các gói tin được gửi đến IP và cổng cũ.
- Các hạn chế về cửa sổ tắc nghẽn và PMTU được loại bỏ, và chúng được phép tăng, hoặc tùy chọn, khôi phục các giá trị trước đó
- Truyền lại bất kỳ gói dữ liệu nào đã được gửi trước đó đến IP/cổng mới sang IP/cổng cũ.

### Xác thực Đường dẫn Thất bại

Điều quan trọng là việc xác thực đường dẫn thất bại do gói tin giả mạo không được gây ra việc chấm dứt hoặc làm gián đoạn đáng kể một phiên hợp lệ.

Khi xác thực đường dẫn thất bại:

- Thoát khỏi giai đoạn xác thực đường dẫn
- Tất cả các gói tin được gửi đến IP và cổng cũ.
- Các hạn chế về congestion window và PMTU được loại bỏ, và chúng được phép tăng.
- Tùy chọn, bắt đầu xác thực đường dẫn trên IP và cổng cũ. Nếu thất bại, kết thúc phiên.
- Nếu không, tuân theo các quy tắc timeout và kết thúc phiên tiêu chuẩn.
- Truyền lại bất kỳ gói tin dữ liệu nào đã được gửi trước đó đến IP/cổng mới sang IP/cổng cũ.

### Xác thực sau Thay đổi Cục bộ

Quá trình trên được định nghĩa cho các peer nhận được một gói tin từ một IP/cổng đã thay đổi. Tuy nhiên, nó cũng có thể được khởi tạo theo hướng ngược lại, bởi một peer phát hiện ra rằng IP hoặc cổng của mình đã thay đổi. Một peer có thể phát hiện được rằng IP cục bộ của mình đã thay đổi; tuy nhiên, khả năng phát hiện cổng của mình thay đổi do NAT rebinding thì thấp hơn nhiều. Do đó, điều này là tùy chọn.

Khi nhận được path challenge từ một peer có IP hoặc port đã thay đổi, peer kia nên khởi tạo một path challenge theo hướng ngược lại.

### Sử dụng như Ping/Pong

Các khối Path Challenge và Path Response có thể được sử dụng bất cứ lúc nào như các gói tin Ping/Pong. Việc nhận được khối Path Challenge không thay đổi bất kỳ trạng thái nào tại bên nhận, trừ khi được nhận từ một IP/port khác.

## Nhiều Phiên

Các peer không nên thiết lập nhiều phiên kết nối với cùng một peer, dù là SSU 1 hay 2, hoặc với cùng hoặc khác địa chỉ IP. Tuy nhiên, điều này có thể xảy ra, do lỗi, hoặc tin nhắn chấm dứt phiên trước đó bị mất, hoặc trong trường hợp tranh chấp khi tin nhắn chấm dứt chưa đến.

Nếu Bob có một phiên hiện tại với Alice, khi Bob nhận được Session Confirmed từ Alice, hoàn thành quá trình bắt tay và thiết lập một phiên mới, Bob nên:

- Di chuyển bất kỳ tin nhắn I2NP gửi đi nào chưa được gửi hoặc chưa được xác nhận từ phiên cũ sang phiên mới
- Gửi lệnh kết thúc với mã lý do 22 trên phiên cũ
- Xóa phiên cũ và thay thế bằng phiên mới

## Kết thúc Phiên

### Giai đoạn bắt tay

Các session trong giai đoạn handshake thường được kết thúc đơn giản bằng cách hết thời gian chờ, hoặc không phản hồi thêm. Tùy chọn, chúng có thể được kết thúc bằng cách bao gồm một khối Termination trong phản hồi, nhưng hầu hết các lỗi không thể phản hồi được do thiếu khóa mã hóa. Ngay cả khi có sẵn khóa cho một phản hồi bao gồm khối termination, việc thực hiện DH cho phản hồi thường không đáng để tiêu tốn CPU. Một ngoại lệ CÓ THỂ là khối Termination trong tin nhắn retry, điều này ít tốn kém để tạo ra.

### Giai đoạn dữ liệu

Các phiên trong giai đoạn dữ liệu được chấm dứt bằng cách gửi một thông điệp dữ liệu bao gồm khối Termination. Thông điệp này cũng nên bao gồm một khối ACK. Nó có thể, nếu phiên đã hoạt động đủ lâu để một token đã gửi trước đó đã hết hạn hoặc sắp hết hạn, bao gồm một khối New Token. Thông điệp này không yêu cầu xác nhận. Khi nhận được một khối Termination với bất kỳ lý do nào ngoại trừ "Termination Received", peer sẽ phản hồi bằng một thông điệp dữ liệu chứa khối Termination với lý do "Termination Received".

Sau khi gửi hoặc nhận một khối Termination, phiên làm việc nên vào giai đoạn đóng trong một khoảng thời gian tối đa TBD. Trạng thái đóng là cần thiết để bảo vệ chống lại việc gói tin chứa khối Termination bị mất, và các gói tin đang truyền theo hướng ngược lại. Trong giai đoạn đóng, không có yêu cầu xử lý thêm bất kỳ gói tin nhận được nào. Một phiên làm việc trong trạng thái đóng sẽ gửi một gói tin chứa khối Termination để phản hồi bất kỳ gói tin đến nào mà nó quy cho phiên làm việc đó. Một phiên làm việc nên giới hạn tốc độ tạo ra các gói tin trong trạng thái đóng. Ví dụ, một phiên làm việc có thể chờ đợi một số lượng gói tin nhận được hoặc khoảng thời gian tăng dần trước khi phản hồi các gói tin nhận được.

Để giảm thiểu trạng thái mà router duy trì cho một phiên đóng, các phiên có thể, nhưng không bắt buộc, gửi chính xác cùng một gói với cùng số gói như hiện tại để phản hồi bất kỳ gói nhận được nào. Lưu ý: Cho phép truyền lại gói kết thúc là một ngoại lệ đối với yêu cầu phải sử dụng số gói mới cho mỗi gói. Việc gửi số gói mới chủ yếu có lợi cho khôi phục mất mát và kiểm soát tắc nghẽn, điều này không được kỳ vọng có liên quan đến kết nối đã đóng. Truyền lại gói cuối cùng yêu cầu ít trạng thái hơn.

Sau khi nhận được một khối Termination với lý do "Termination Received", session có thể thoát khỏi giai đoạn đóng.

### Dọn dẹp

Khi kết thúc bình thường hoặc bất thường, các router nên xóa sạch mọi dữ liệu tạm thời trong bộ nhớ, bao gồm các khóa tạm thời của handshake, khóa mã hóa đối xứng và thông tin liên quan.

## MTU

Các yêu cầu khác nhau, dựa trên việc địa chỉ được công bố có được chia sẻ với SSU 1 hay không. Mức tối thiểu hiện tại của SSU 1 IPv4 là 620, điều này chắc chắn là quá nhỏ.

MTU SSU2 tối thiểu là 1280 cho cả IPv4 và IPv6, giống như được chỉ định trong [RFC-9000](https://tools.ietf.org/html/rfc9000). Xem bên dưới. Bằng cách tăng MTU tối thiểu, các thông điệp tunnel 1 KB và các thông điệp xây dựng tunnel ngắn sẽ vừa trong một datagram, giảm đáng kể lượng phân mảnh thông thường. Điều này cũng cho phép tăng kích thước thông điệp I2NP tối đa. Các thông điệp streaming 1820 byte sẽ vừa trong hai datagram.

Một router không được phép bật SSU2 hoặc công bố địa chỉ SSU2 trừ khi MTU cho địa chỉ đó ít nhất là 1280.

Các router phải công bố MTU khác mặc định trong mỗi địa chỉ router SSU hoặc SSU2.

### Địa chỉ SSU

Địa chỉ chia sẻ với SSU 1, phải tuân theo các quy tắc SSU 1. IPv4: Mặc định và tối đa là 1484. Tối thiểu là 1292. (IPv4 MTU + 4) phải là bội số của 16. IPv6: Phải được công bố, tối thiểu là 1280 và tối đa là 1488. IPv6 MTU phải là bội số của 16.

### Địa chỉ SSU2

IPv4: Mặc định và tối đa là 1500. Tối thiểu là 1280. IPv6: Mặc định và tối đa là 1500. Tối thiểu là 1280. Không có quy tắc bội số của 16, nhưng có thể nên là bội số của 2 ít nhất.

### Khám phá PMTU

Đối với SSU 1, Java I2P hiện tại thực hiện khám phá PMTU bằng cách bắt đầu với các gói tin nhỏ và tăng dần kích thước, hoặc tăng dựa trên kích thước gói tin nhận được. Cách này thô sơ và làm giảm đáng kể hiệu quả. Việc tiếp tục tính năng này trong SSU 2 vẫn chưa được xác định.

Các nghiên cứu gần đây [PMTU](https://en.wikipedia.org/wiki/Path_MTU_Discovery) cho thấy rằng mức tối thiểu cho IPv4là 1200 hoặc hơn sẽ hoạt động cho hơn 99% kết nối. QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) yêu cầu kích thước gói IP tối thiểu là 1280 byte.

trích dẫn [RFC-9000](https://tools.ietf.org/html/rfc9000):

Kích thước datagram tối đa được định nghĩa là kích thước lớn nhất của UDP payload có thể được gửi qua một đường dẫn mạng bằng cách sử dụng một datagram UDP duy nhất. QUIC KHÔNG ĐƯỢC sử dụng nếu đường dẫn mạng không thể hỗ trợ kích thước datagram tối đa ít nhất 1200 byte.

QUIC giả định kích thước gói IP tối thiểu ít nhất 1280 byte. Đây là kích thước tối thiểu của IPv6 [IPv6] và cũng được hỗ trợ bởi hầu hết các mạng IPv4 hiện đại. Giả sử kích thước header IP tối thiểu là 40 byte cho IPv6 và 20 byte cho IPv4 và kích thước header UDP là 8 byte, điều này dẫn đến kích thước datagram tối đa là 1232 byte cho IPv6 và 1252 byte cho IPv4. Do đó, các đường dẫn mạng IPv4 hiện đại và tất cả IPv6 được kỳ vọng có thể hỗ trợ QUIC.

Lưu ý: Yêu cầu hỗ trợ payload UDP 1200 byte này giới hạn không gian có sẵn cho các extension header IPv6 xuống 32 byte hoặc các tùy chọn IPv4 xuống 52 byte nếu đường truyền chỉ hỗ trợ MTU tối thiểu của IPv6 là 1280 byte. Điều này ảnh hưởng đến các gói Initial và xác thực đường truyền.

kết thúc trích dẫn

### Kích Thước Tối Thiểu Bắt Tay

QUIC yêu cầu các datagram Initial theo cả hai hướng phải có ít nhất 1200 byte, để ngăn chặn các cuộc tấn công khuếch đại và đảm bảo PMTU hỗ trợ nó theo cả hai hướng.

Chúng ta có thể yêu cầu điều này cho Session Request và Session Created, với chi phí băng thông đáng kể. Có thể chúng ta chỉ làm điều này nếu chúng ta không có token, hoặc sau khi nhận được thông báo Retry. TBD

QUIC yêu cầu rằng Bob không gửi quá ba lần lượng dữ liệu đã nhận cho đến khi địa chỉ client được xác thực. SSU2 đáp ứng yêu cầu này một cách tự nhiên, bởi vì thông báo Retry có kích thước tương tự như thông báo Token Request, và nhỏ hơn thông báo Session Request. Ngoài ra, thông báo Retry chỉ được gửi một lần.

### Kích Thước Tối Thiểu Thông Điệp Đường Dẫn

QUIC yêu cầu các thông điệp chứa khối PATH_CHALLENGE hoặc PATH_RESPONSE phải có ít nhất 1200 byte, để ngăn chặn các cuộc tấn công khuếch đại và đảm bảo PMTU hỗ trợ nó theo cả hai hướng.

Chúng ta cũng có thể yêu cầu điều này, với chi phí đáng kể về băng thông. Tuy nhiên, những trường hợp này sẽ hiếm khi xảy ra. TBD

### Kích thước tối đa của thông điệp I2NP

IPv4: Không giả định phân mảnh IP. Header IP + datagram là 28 byte. Điều này giả định không có tùy chọn IPv4. Kích thước thông điệp tối đa là MTU - 28. Header pha dữ liệu là 16 byte và MAC là 16 byte, tổng cộng 32 byte. Kích thước payload là MTU - 60. Payload pha dữ liệu tối đa là 1440 cho MTU tối đa 1500. Payload pha dữ liệu tối đa là 1220 cho MTU tối thiểu 1280.

IPv6: Không cho phép phân mảnh IP. Header IP + datagram là 48 bytes. Điều này giả định không có extension header IPv6. Kích thước message tối đa là MTU - 48. Header data phase là 16 bytes và MAC là 16 bytes, tổng cộng 32 bytes. Kích thước payload là MTU - 80. Payload data phase tối đa là 1420 cho MTU tối đa 1500. Payload data phase tối đa là 1200 cho MTU tối thiểu 1280.

Trong SSU 1, các hướng dẫn đưa ra giới hạn tối đa nghiêm ngặt khoảng 32 KB cho một thông điệp I2NP dựa trên tối đa 64 phân đoạn và MTU tối thiểu 620. Do chi phí phụ trội cho LeaseSets gộp và session keys, giới hạn thực tế ở cấp ứng dụng thấp hơn khoảng 6KB, hay khoảng 26KB. Giao thức SSU 1 cho phép 128 phân đoạn nhưng các triển khai hiện tại giới hạn ở 64 phân đoạn.

Bằng cách tăng MTU tối thiểu lên 1280, với tải trọng giai đoạn dữ liệu khoảng 1200, một tin nhắn SSU 2 khoảng 76 KB có thể thực hiện được trong 64 phân đoạn và 152 KB trong 128 phân đoạn. Điều này dễ dàng cho phép tối đa 64 KB.

Do sự phân mảnh trong các tunnel và phân mảnh trong SSU 2, khả năng mất thông điệp tăng theo cấp số nhân với kích thước thông điệp. Chúng tôi tiếp tục khuyến nghị giới hạn thực tế khoảng 10 KB tại lớp ứng dụng cho các datagram I2NP.

## Quy trình Kiểm tra Peer

Xem phần Bảo mật Peer Test ở trên để có phân tích về SSU1 Peer Test và các mục tiêu của SSU2 Peer Test.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest
        <---------------- Charlie RI
4.      <------------------ PeerTest

5.      <----------------------------------------- PeerTest
6. PeerTest ----------------------------------------->
7.      <----------------------------------------- PeerTest
```
Khi bị Bob từ chối:

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
4.      <------------------ PeerTest (reject)
```
Khi bị Charlie từ chối:

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest (reject)
                      (optional: Bob could try another Charlie here)
4.      <------------------ PeerTest (reject)
```
LƯU Ý: RI có thể được gửi dưới dạng các thông điệp I2NP Database Store trong các khối I2NP, hoặc dưới dạng các khối RI (nếu đủ nhỏ). Những khối này có thể được chứa trong cùng các gói với các khối kiểm tra peer, nếu đủ nhỏ.

Các thông điệp 1-4 là trong phiên sử dụng các khối Peer Test trong thông điệp Data. Các thông điệp 5-7 là ngoài phiên sử dụng các khối Peer Test trong thông điệp Peer Test.

LƯU Ý: Như trong SSU 1, các thông báo 4 và 5 có thể đến theo thứ tự bất kỳ. Thông báo 5 và/hoặc 7 có thể không được nhận hoàn toàn nếu Alice bị chặn bởi tường lửa. Khi thông báo 5 đến trước thông báo 4, Alice không thể gửi ngay thông báo 6, vì cô ấy chưa có khóa giới thiệu của Charlie để mã hóa header. Khi thông báo 4 đến trước thông báo 5, Alice không nên gửi ngay thông báo 6, vì cô ấy nên chờ xem liệu thông báo 5 có đến mà không cần mở tường lửa bằng thông báo 6.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Path</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Intro Key</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->C session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->A session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->C</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
  </tbody>
</table>
### Phiên bản

Kiểm tra peer giữa các phiên bản khác nhau không được hỗ trợ. Kết hợp phiên bản duy nhất được phép là khi tất cả các peer đều là phiên bản 2.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### Truyền lại

Các thông điệp 1-4 nằm trong phiên và được bao phủ bởi các quy trình ACK và truyền lại của giai đoạn dữ liệu. Các khối Peer Test sẽ gây ra ACK.

Các thông điệp 5-7 có thể được truyền lại mà không thay đổi.

### Ghi chú về IPv6

Như trong SSU 1, việc kiểm tra các địa chỉ IPv6 được hỗ trợ, và giao tiếp Alice-Bob và Alice-Charlie có thể thông qua IPv6, nếu Bob và Charlie chỉ ra sự hỗ trợ với capability 'B' trong địa chỉ IPv6 được công bố của họ. Xem Proposal 126 để biết chi tiết.

Giống như trong SSU 1 trước phiên bản 0.9.50, Alice gửi yêu cầu đến Bob sử dụng một phiên kết nối hiện có qua transport (IPv4 hoặc IPv6) mà cô ấy muốn kiểm tra. Khi Bob nhận được yêu cầu từ Alice qua IPv4, Bob phải chọn một Charlie quảng cáo địa chỉ IPv4. Khi Bob nhận được yêu cầu từ Alice qua IPv6, Bob phải chọn một Charlie quảng cáo địa chỉ IPv6. Việc giao tiếp thực tế giữa Bob-Charlie có thể qua IPv4 hoặc IPv6 (tức là độc lập với loại địa chỉ của Alice). Đây KHÔNG phải là hành vi của SSU 1 kể từ phiên bản 0.9.50, nơi các yêu cầu IPv4/v6 hỗn hợp được cho phép.

### Xử lý bởi Bob

Khác với SSU 1, Alice chỉ định IP và port được yêu cầu kiểm tra trong thông điệp 1. Bob nên xác thực IP và port này, và từ chối với mã 5 nếu không hợp lệ. Xác thực IP được khuyến nghị là, đối với IPv4, nó phải khớp với IP của Alice, và đối với IPv6, ít nhất 8 byte đầu của IP phải khớp. Xác thực port nên từ chối các port đặc quyền và port cho các giao thức nổi tiếng.

### Máy Trạng Thái Kết Quả

Ở đây chúng tôi tài liệu hóa cách Alice có thể xác định kết quả của peer test, dựa trên các thông điệp được nhận. Các cải tiến của SSU2 cung cấp cho chúng ta cơ hội để sửa chữa, cải thiện và tài liệu hóa tốt hơn máy trạng thái kết quả peer test so với máy trong [SSU](/docs/transport/ssu).

Đối với mỗi loại địa chỉ được kiểm tra (IPv4 hoặc IPv6), kết quả có thể là một trong các trạng thái UNKNOWN, OK, FIREWALLED, hoặc SYMNAT. Ngoài ra, các quá trình xử lý khác có thể được thực hiện để phát hiện thay đổi IP hoặc port, hoặc một port bên ngoài khác với port bên trong.

Vấn đề với máy trạng thái SSU được tài liệu hóa:

- Chúng ta không bao giờ gửi thông điệp 6 trừ khi đã nhận được thông điệp 5, vì vậy chúng ta không bao giờ biết mình có phải SYMNAT hay không
- NẾU chúng ta ĐÃ nhận được thông điệp 4 và 7, làm sao chúng ta có thể là SYMNAT
- Nếu IP không khớp nhưng port khớp, chúng ta không phải SYMNAT, chúng ta chỉ thay đổi IP của mình

Vậy nên, trái ngược với SSU, chúng tôi khuyến nghị đợi vài giây sau khi nhận được message 4, sau đó gửi message 6 ngay cả khi message 5 không được nhận.

Tóm tắt về máy trạng thái, dựa trên việc có nhận được các thông điệp 4, 5 và 7 hay không (có hoặc không), như sau:

```
4 5 7  Result             Notes
-----  ------             -----
n n n  UNKNOWN
y n n  FIREWALLED           (unless currently SYMNAT)
n y n  OK                   (unless currently SYMNAT, which is unlikely)
y y n  OK                   (unless currently SYMNAT, which is unlikely)
n n y  n/a                  (can't send msg 6)
y n y  FIREWALLED or SYMNAT (requires sending msg 6 w/o rcv msg 5)
n y y  n/a                  (can't send msg 6)
y y y  OK
```
Một máy trạng thái chi tiết hơn, với việc kiểm tra IP/cổng nhận được trong khối địa chỉ của thông điệp 7, được mô tả bên dưới. Một thách thức là xác định xem bạn (Alice) có phải là người bị symmetric NAT hay Charlie mới là người bị symmetric NAT.

Việc xử lý hậu kỳ hoặc logic bổ sung để xác nhận các chuyển đổi trạng thái bằng cách yêu cầu cùng kết quả trên hai hoặc nhiều peer test được khuyến nghị.

Việc xác thực và xác nhận IP/port bằng hai hoặc nhiều thử nghiệm, hoặc với khối địa chỉ trong các thông điệp Session Created, cũng được khuyến nghị, nhưng nằm ngoài phạm vi của đặc tả này.

```
If Alice does not get msg 5:
   If Alice does not get msg 4: -> UNKNOWN
   If Alice does not get msg 7: -> UNKNOWN
   If Alice gets msgs 4/7 and IP/port match: -> FIREWALLED
   If Alice gets msgs 4/7 and IP matches, port does not match:
      -> SYMNAT, but needs confirmation with 2nd test
   If Alice gets msgs 4/7 and IP does not match, port matches:
      -> FIREWALLED, address change?
   If Alice gets msgs 4/7 and both IP and port do not match:
      -> SYMNAT, address change?

If Alice gets msg 5:
   If Alice does not get msg 4: -> OK unless currently SYMNAT, else UNKNOWN
                                   (in SSU2 have to stop here)
   If Alice does not get msg 7: -> OK unless currently SYMNAT, else UNKNOWN
   If Alice gets msgs 4/5/7 and IP/port match: -> OK
   If Alice gets msgs 4/5/7 and IP matches, port does not match:
      -> OK, charlie is probably sym. natted
   If Alice gets msgs 4/5/7 and IP does not match, port matches:
      -> OK, address change?
   If Alice gets msgs 4/5/7 and both IP and port do not match:
      -> OK, address change?
```
## Quá trình Chuyển tiếp

Xem phần Bảo mật Relay ở trên để có phân tích về SSU1 Relay và các mục tiêu cho SSU2 Relay.

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse

5.      <-------------------------------------------- HolePunch
6. SessionRequest -------------------------------------------->
7.      <-------------------------------------------- SessionCreated
8. SessionConfirmed ------------------------------------------>
```
Khi bị Bob từ chối:

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
4.      <-------------- RelayResponse
```
Khi bị Charlie từ chối:

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse
```
LƯU Ý: RI có thể được gửi dưới dạng các thông điệp I2NP Database Store trong các khối I2NP, hoặc dưới dạng các khối RI (nếu đủ nhỏ). Những khối này có thể được chứa trong cùng các gói với các khối relay, nếu đủ nhỏ.

Trong SSU 1, thông tin router của Charlie chứa IP, cổng, intro key, relay tag và thời gian hết hạn của mỗi introducer.

Trong SSU 2, thông tin router của Charlie chứa router hash, relay tag, và thời hạn hết hiệu lực của mỗi introducer.

Alice nên giảm số lượng round trip cần thiết bằng cách đầu tiên chọn một introducer (Bob) mà cô ấy đã có kết nối. Thứ hai, nếu không có, hãy chọn một introducer mà cô ấy đã có thông tin router.

Chuyển tiếp giữa các phiên bản khác nhau cũng nên được hỗ trợ nếu có thể. Điều này sẽ tạo điều kiện cho quá trình chuyển đổi dần dần từ SSU 1 sang SSU 2. Các kết hợp phiên bản được cho phép là (TODO):

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/2/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### Truyền lại

Relay Request, Relay Intro, và Relay Response đều nằm trong phiên kết nối và được bao phủ bởi các quy trình ACK và truyền lại của giai đoạn dữ liệu. Các khối Relay Request, Relay Intro, và Relay Response đều yêu cầu xác nhận (ack-eliciting).

Lưu ý rằng thông thường, Charlie sẽ phản hồi ngay lập tức cho một Relay Intro bằng một Relay Response, cái mà nên bao gồm một ACK block. Trong trường hợp đó, không cần thiết một thông điệp riêng biệt với ACK block.

Hole punch có thể được truyền lại, như trong SSU 1.

Không giống như các thông điệp I2NP, các thông điệp Relay không có định danh duy nhất, vì vậy các bản trùng lặp phải được phát hiện bởi máy trạng thái relay, sử dụng nonce. Các triển khai cũng có thể cần duy trì một bộ nhớ đệm của các nonce được sử dụng gần đây, để các bản trùng lặp nhận được có thể được phát hiện ngay cả sau khi máy trạng thái cho nonce đó đã hoàn thành.

### IPv4/v6

Tất cả các tính năng của SSU 1 relay đều được hỗ trợ, bao gồm những tính năng được ghi chép trong [Prop158](/proposals/158-ipv6-transport-enhancements) và được hỗ trợ từ phiên bản 0.9.50. Các introduction IPv4 và IPv6 đều được hỗ trợ. Một Relay Request có thể được gửi qua phiên IPv4 cho một introduction IPv6, và một Relay Request có thể được gửi qua phiên IPv6 cho một introduction IPv4.

### Xử lý bởi Alice

Sau đây là những điểm khác biệt so với SSU 1 và các khuyến nghị cho việc triển khai SSU 2.

#### Lựa chọn Introducer

Trong SSU 1, việc giới thiệu tương đối ít tốn kém, và Alice thường gửi Relay Requests đến tất cả các introducer. Trong SSU 2, việc giới thiệu tốn kém hơn, vì trước tiên phải thiết lập một kết nối với introducer. Để giảm thiểu độ trễ và chi phí giới thiệu, các bước xử lý được khuyến nghị như sau:

- Bỏ qua bất kỳ introducer nào đã hết hạn dựa trên giá trị iexp trong địa chỉ
- Nếu kết nối SSU2 đã được thiết lập với một hoặc nhiều introducer, chọn một và chỉ gửi Relay Request đến introducer đó.
- Nếu không, nếu Router Info được biết cục bộ cho một hoặc nhiều introducer, chọn một và chỉ kết nối đến introducer đó.
- Nếu không, tra cứu Router Info cho tất cả introducer, kết nối đến introducer có Router Info được nhận đầu tiên.

#### Xử lý Phản hồi

Trong cả SSU 1 và SSU 2, Relay Response và Hole Punch có thể được nhận theo thứ tự bất kỳ, hoặc có thể không được nhận chút nào.

Trong SSU 1, Alice thường nhận được Relay Response (1 RTT) trước Hole Punch (1 1/2 RTT). Có thể không được ghi chép đầy đủ trong các đặc tả đó, nhưng Alice phải nhận được Relay Response từ Bob trước khi tiếp tục, để nhận IP của Charlie. Nếu Hole Punch được nhận trước, Alice sẽ không nhận ra nó, vì nó không chứa dữ liệu và IP nguồn không được nhận diện. Sau khi nhận được Relay Response, Alice nên đợi HOẶC nhận Hole Punch từ Charlie, HOẶC một khoảng trễ ngắn (khuyến nghị 500 ms) trước khi bắt đầu handshake với Charlie.

Trong SSU 2, Alice thường sẽ nhận được Hole Punch (1 1/2 RTT) trước Relay Response (2 RTT). SSU 2 Hole Punch dễ xử lý hơn so với SSU 1, vì nó là một thông điệp đầy đủ với các connection ID được xác định (suy ra từ relay nonce) và nội dung bao gồm IP của Charlie. Relay Response (Data message) và Hole Punch message chứa cùng một khối Relay Response đã ký. Do đó, Alice có thể bắt đầu handshake với Charlie sau khi HOẶC nhận được Hole Punch từ Charlie, HOẶC nhận được Relay Response từ Bob.

Việc xác minh chữ ký của Hole Punch bao gồm router hash của người giới thiệu (Bob). Nếu các Relay Request đã được gửi đến nhiều hơn một người giới thiệu, có một số tùy chọn để xác thực chữ ký:

- Thử từng hash mà yêu cầu đã được gửi đến
- Sử dụng các nonce khác nhau cho mỗi introducer, và dùng điều đó để xác định introducer nào mà Hole Punch này đang phản hồi
- Không xác thực lại chữ ký nếu nội dung giống hệt với nội dung trong Relay Response, nếu đã nhận được
- Không xác thực chữ ký gì cả

Nếu Charlie đứng sau một symmetric NAT, cổng được báo cáo của anh ta trong Relay Response và Hole Punch có thể không chính xác. Do đó, Alice nên kiểm tra cổng nguồn UDP của thông điệp Hole Punch, và sử dụng cổng đó nếu nó khác với cổng được báo cáo.

### Yêu cầu Tag bởi Bob

Trong SSU 1, chỉ Alice mới có thể yêu cầu một tag trong Session Request. Bob không bao giờ có thể yêu cầu tag, và Alice không thể relay cho Bob.

Trong SSU2, Alice thường yêu cầu một tag trong Session Request, nhưng cả Alice hoặc Bob cũng có thể yêu cầu một tag trong giai đoạn dữ liệu. Bob thường không bị tường lửa chặn sau khi nhận được một yêu cầu đến, nhưng có thể bị chặn sau một relay, hoặc trạng thái của Bob có thể thay đổi, hoặc anh ta có thể yêu cầu một introducer cho loại địa chỉ khác (IPv4/v6). Vì vậy, trong SSU2, cả Alice và Bob có thể đồng thời làm relay cho bên kia.

## Thông Tin Router Đã Công Bố

### Thuộc Tính Địa Chỉ

Các thuộc tính địa chỉ sau đây có thể được xuất bản, không thay đổi từ SSU 1, bao gồm các thay đổi trong [Prop158](/proposals/158-ipv6-transport-enhancements) được hỗ trợ từ API 0.9.50:

- caps: khả năng [B,C,4,6]
- host: IP (IPv4 hoặc IPv6). Địa chỉ IPv6 rút gọn (với "::") được cho phép. Có thể có hoặc không có mặt nếu đằng sau tường lửa. Tên host không được phép.
- iexp[0-2]: Hết hạn của introducer này. Chữ số ASCII, tính bằng giây kể từ epoch. Chỉ có mặt nếu đằng sau tường lửa và cần introducer. Tùy chọn (ngay cả khi các thuộc tính khác cho introducer này có mặt).
- ihost[0-2]: IP của introducer (IPv4 hoặc IPv6). Địa chỉ IPv6 rút gọn (với "::") được cho phép. Chỉ có mặt nếu đằng sau tường lửa và cần introducer. Tên host không được phép. Chỉ dành cho địa chỉ SSU.
- ikey[0-2]: Khóa introduction Base 64 của introducer. Chỉ có mặt nếu đằng sau tường lửa và cần introducer. Chỉ dành cho địa chỉ SSU.
- iport[0-2]: Cổng của introducer 1024 - 65535. Chỉ có mặt nếu đằng sau tường lửa và cần introducer. Chỉ dành cho địa chỉ SSU.
- itag[0-2]: Thẻ của introducer 1 - (2**32 - 1) chữ số ASCII. Chỉ có mặt nếu đằng sau tường lửa và cần introducer.
- key: Khóa introduction Base 64.
- mtu: Tùy chọn. Xem phần MTU ở trên.
- port: 1024 - 65535 Có thể có hoặc không có mặt nếu đằng sau tường lửa.

### Địa chỉ đã xuất bản

RouterAddress được công bố (là một phần của RouterInfo) sẽ có một định danh giao thức là "SSU" hoặc "SSU2".

RouterAddress phải chứa ba tùy chọn để chỉ ra hỗ trợ SSU2:

- s=(Base64 key) Khóa công khai tĩnh Noise hiện tại (s) cho RouterAddress này. Được mã hóa Base 64 sử dụng bảng chữ cái Base 64 chuẩn của I2P. 32 byte ở dạng nhị phân, 44 byte khi được mã hóa Base 64, khóa công khai X25519 little-endian.
- i=(Base64 key) Khóa giới thiệu hiện tại để mã hóa các header cho RouterAddress này. Được mã hóa Base 64 sử dụng bảng chữ cái Base 64 chuẩn của I2P. 32 byte ở dạng nhị phân, 44 byte khi được mã hóa Base 64, khóa ChaCha20 big-endian.
- v=2 Phiên bản hiện tại (2). Khi được xuất bản dưới dạng "SSU", việc hỗ trợ bổ sung cho phiên bản 1 được ngầm hiểu. Việc hỗ trợ các phiên bản tương lai sẽ được thực hiện với các giá trị phân cách bằng dấu phẩy, ví dụ v=2,3. Việc triển khai nên xác minh tính tương thích, bao gồm nhiều phiên bản nếu có dấu phẩy. Các phiên bản phân cách bằng dấu phẩy phải theo thứ tự số.

Alice phải xác minh rằng cả ba tùy chọn đều có mặt và hợp lệ trước khi kết nối sử dụng giao thức SSU2.

Khi được xuất bản dưới dạng "SSU" với các tùy chọn "s", "i", và "v", và với các tùy chọn "host" và "port", router phải chấp nhận các kết nối đến trên host và port đó cho cả giao thức SSU và SSU2, và tự động phát hiện phiên bản giao thức.

Khi được xuất bản dưới dạng "SSU2" với các tùy chọn "s", "i", và "v", và với các tùy chọn "host" và "port", router sẽ chấp nhận các kết nối đến trên host và port đó chỉ dành cho giao thức SSU2.

Nếu một router hỗ trợ cả kết nối SSU1 và SSU2 nhưng không triển khai tự động phát hiện phiên bản cho các kết nối đến, nó phải quảng bá cả địa chỉ "SSU" và "SSU2", và chỉ bao gồm các tùy chọn SSU2 trong địa chỉ "SSU2". Router nên đặt giá trị chi phí thấp hơn (mức ưu tiên cao hơn) trong địa chỉ "SSU2" so với địa chỉ "SSU", để SSU2 được ưu tiên.

Nếu nhiều SSU2 RouterAddresses (dưới dạng "SSU" hoặc "SSU2") được công bố trong cùng một RouterInfo (cho các địa chỉ IP hoặc cổng bổ sung), tất cả các địa chỉ chỉ định cùng một cổng phải chứa các tùy chọn và giá trị SSU2 giống hệt nhau. Đặc biệt, tất cả phải chứa cùng một khóa tĩnh "s" và khóa giới thiệu "i".

#### Introducer

Khi được xuất bản dưới dạng SSU hoặc SSU2 với các introducer, các tùy chọn sau sẽ có mặt:

- ih[0-2]=(Base64 hash) Một router hash cho một introducer. Được mã hóa Base 64 sử dụng bảng chữ cái Base 64 chuẩn của I2P. 32 bytes ở dạng nhị phân, 44 bytes khi được mã hóa Base 64
- iexp[0-2]: Thời hạn hết hiệu lực của introducer này. Không thay đổi so với SSU 1.
- itag[0-2]: Tag của introducer từ 1 - (2**32 - 1) Không thay đổi so với SSU 1.

Các tùy chọn sau chỉ dành cho SSU và không được sử dụng cho SSU2. Trong SSU2, Alice lấy thông tin này từ RI của Charlie thay thế.

- ihost[0-2]
- ikey[0-2]
- itag[0-2]

Một router không được công bố host hoặc port trong địa chỉ khi công bố các introducer. Một router phải công bố cap 4 và/hoặc 6 trong địa chỉ khi công bố các introducer để chỉ ra việc hỗ trợ IPv4 và/hoặc IPv6. Điều này giống với thực hành hiện tại đối với các địa chỉ SSU 1 gần đây.

Lưu ý: Nếu được xuất bản như SSU, và có sự kết hợp giữa các introducer SSU 1 và SSU2, các introducer SSU 1 nên được đặt ở các chỉ mục thấp hơn và các introducer SSU2 nên được đặt ở các chỉ mục cao hơn, để tương thích với các router cũ hơn.

### Địa chỉ SSU2 chưa được công bố

Nếu Alice không công bố địa chỉ SSU2 của mình (dưới dạng "SSU" hoặc "SSU2") cho các kết nối đến, cô ấy phải công bố một địa chỉ router "SSU2" chỉ chứa khóa tĩnh và phiên bản SSU2 của mình, để Bob có thể xác thực khóa sau khi nhận RouterInfo của Alice trong Session Confirmed phần 2.

- s=(Base64 key) Như đã định nghĩa ở trên cho các địa chỉ đã công bố.
- i=(Base64 key) Như đã định nghĩa ở trên cho các địa chỉ đã công bố.
- v=2 Như đã định nghĩa ở trên cho các địa chỉ đã công bố.

Địa chỉ router này sẽ không chứa tùy chọn "host" hoặc "port", vì chúng không cần thiết cho các kết nối SSU2 đi ra. Chi phí được công bố cho địa chỉ này không quan trọng lắm, vì nó chỉ dành cho kết nối đến; tuy nhiên, có thể hữu ích cho các router khác nếu chi phí được đặt cao hơn (ưu tiên thấp hơn) so với các địa chỉ khác. Giá trị đề xuất là 14.

Alice cũng có thể đơn giản thêm các tùy chọn "i", "s" và "v" vào một địa chỉ "SSU" đã xuất bản hiện có.

### Xoay vòng Khóa Công khai và IV

Sử dụng cùng một static key cho NTCP2 và SSU2 được cho phép, nhưng không được khuyến khích.

Do việc lưu trữ tạm thời các RouterInfo, các router không được xoay khóa công khai tĩnh hoặc IV trong khi router đang hoạt động, bất kể có trong địa chỉ đã xuất bản hay không. Các router phải lưu trữ bền vững khóa và IV này để tái sử dụng sau khi khởi động lại ngay lập tức, để các kết nối đến sẽ tiếp tục hoạt động và thời gian khởi động lại không bị lộ. Các router phải lưu trữ bền vững hoặc xác định bằng cách khác thời gian tắt máy cuối cùng, để có thể tính toán thời gian ngừng hoạt động trước đó khi khởi động.

Tùy thuộc vào mối quan tâm về việc tiết lộ thời gian khởi động lại, các router có thể luân chuyển khóa này hoặc IV khi khởi động nếu router trước đó đã ngừng hoạt động trong một thời gian (ít nhất vài ngày).

Nếu router có bất kỳ SSU2 RouterAddresses nào được công bố (như SSU hoặc SSU2), thời gian ngừng hoạt động tối thiểu trước khi luân chuyển nên dài hơn nhiều, ví dụ một tháng, trừ khi địa chỉ IP cục bộ đã thay đổi hoặc router "rekeys".

Nếu router có bất kỳ SSU RouterAddresses nào được công bố, nhưng không có SSU2 (như SSU hoặc SSU2) thì thời gian ngừng hoạt động tối thiểu trước khi xoay vòng nên dài hơn, ví dụ một ngày, trừ khi địa chỉ IP cục bộ đã thay đổi hoặc router "rekeys". Điều này áp dụng ngay cả khi địa chỉ SSU được công bố có introducers.

Nếu router không có bất kỳ RouterAddresses đã công bố nào (SSU, SSU2, hoặc SSU), thời gian ngừng hoạt động tối thiểu trước khi xoay vòng có thể ngắn chỉ hai giờ, ngay cả khi địa chỉ IP thay đổi, trừ khi router thực hiện "rekeys".

Nếu router "rekey" sang một Router Hash khác, nó cũng nên tạo một noise key và intro key mới.

Các triển khai phải nhận thức rằng việc thay đổi static public key hoặc IV sẽ cấm các kết nối SSU2 đến từ các router đã lưu cache RouterInfo cũ hơn. Việc xuất bản RouterInfo, lựa chọn tunnel peer (bao gồm cả OBGW và IB closest hop), lựa chọn zero-hop tunnel, lựa chọn transport, và các chiến lược triển khai khác phải tính đến điều này.

Xoay khóa intro tuân theo các quy tắc giống hệt như xoay khóa.

Lưu ý: Thời gian ngừng hoạt động tối thiểu trước khi tạo lại khóa có thể được điều chỉnh để đảm bảo sức khỏe mạng và ngăn chặn việc reseed bởi một router bị ngưng trong khoảng thời gian vừa phải.

#### Ẩn Danh Tính

Khả năng chối bỏ không phải là mục tiêu. Xem tổng quan ở trên.

Mỗi pattern được gán các thuộc tính mô tả tính bảo mật được cung cấp cho static public key của bên khởi tạo và cho static public key của bên phản hồi. Các giả định cơ bản là ephemeral private keys được bảo mật, và các bên sẽ hủy bỏ handshake nếu họ nhận được một static public key từ bên kia mà họ không tin tưởng.

Phần này chỉ xem xét việc rò rỉ danh tính thông qua các trường khóa công khai tĩnh trong quá trình bắt tay. Tất nhiên, danh tính của các bên tham gia Noise có thể bị lộ thông qua các phương tiện khác, bao gồm các trường payload, phân tích lưu lượng, hoặc metadata như địa chỉ IP.

Alice: (8) Được mã hóa với tính bảo mật chuyển tiếp (forward secrecy) đến một bên đã được xác thực.

Bob: (3) Không được truyền, nhưng kẻ tấn công thụ động có thể kiểm tra các ứng viên cho khóa riêng của responder và xác định xem ứng viên đó có đúng không.

Bob công bố khóa công khai tĩnh của mình trong netDb. Alice có thể không làm vậy, nhưng phải bao gồm nó trong RI gửi cho Bob.

## Hướng Dẫn Gói Tin

### Tạo Gói Tin Đi Ra

Các bước cơ bản của thông điệp handshake (Session Request/Created/Confirmed, Retry), theo thứ tự:

- Tạo header 16 hoặc 32 byte
- Tạo payload
- mixHash() header (trừ Retry)
- Mã hóa payload sử dụng Noise (trừ Retry, sử dụng ChaChaPoly với header làm AD)
- Mã hóa header, và đối với Session Request/Created, mã hóa ephemeral key

Các bước cơ bản của thông điệp pha dữ liệu, theo thứ tự:

- Tạo header 16-byte
- Tạo payload
- Mã hóa payload bằng ChaChaPoly sử dụng header làm AD
- Mã hóa header

### Xử Lý Gói Tin Đến

#### Tóm tắt

Xử lý ban đầu của tất cả các tin nhắn đến:

- Giải mã 8 byte đầu tiên của header (Destination Connection ID) bằng intro key
- Tra cứu kết nối theo Destination Connection ID
- Nếu tìm thấy kết nối và đang ở giai đoạn data, chuyển đến phần giai đoạn data
- Nếu không tìm thấy kết nối, chuyển đến phần handshake
- Lưu ý: Các thông điệp Peer Test và Hole Punch cũng có thể được tra cứu bằng Destination Connection ID được tạo từ test hoặc relay nonce.

Xử lý các thông điệp handshake (Session Request/Created/Confirmed, Retry, Token Request) và các thông điệp ngoài phiên (Peer Test, Hole Punch):

- Giải mã byte 8-15 của header (loại gói tin, phiên bản, và net ID) với intro key. Nếu đó là Session Request, Token Request, Peer Test, hoặc Hole Punch hợp lệ, tiếp tục
- Nếu không phải thông điệp hợp lệ, tra cứu kết nối outbound đang chờ theo IP/port nguồn của gói tin, coi gói tin như Session Created hoặc Retry. Giải mã lại 8 byte đầu của header với key đúng, và byte 8-15 của header (loại gói tin, phiên bản, và net ID). Nếu đó là Session Created hoặc Retry hợp lệ, tiếp tục
- Nếu không phải thông điệp hợp lệ, thất bại, hoặc xếp hàng đợi như một gói tin data phase có thể bị lệch thứ tự
- Đối với Session Request/Created, Retry, Token Request, Peer Test, và Hole Punch, giải mã byte 16-31 của header
- Đối với Session Request/Created, giải mã ephemeral key
- Xác thực tất cả trường header, dừng nếu không hợp lệ
- mixHash() header
- Đối với Session Request/Created/Confirmed, giải mã payload sử dụng Noise
- Đối với Retry và data phase, giải mã payload sử dụng ChaChaPoly
- Xử lý header và payload

Xử lý thông điệp giai đoạn dữ liệu:

- Giải mã các byte 8-15 của header (loại gói tin, phiên bản và net ID) bằng khóa đúng
- Giải mã payload sử dụng ChaChaPoly với header làm AD
- Xử lý header và payload

#### Chi tiết

Trong SSU 1, việc phân loại gói tin đến rất khó khăn vì không có header để chỉ ra số phiên. Các router phải trước tiên khớp IP nguồn và cổng với trạng thái peer hiện có, và nếu không tìm thấy, thử nhiều lần giải mã với các khóa khác nhau để tìm trạng thái peer phù hợp hoặc bắt đầu một phiên mới. Trong trường hợp IP nguồn hoặc cổng cho một phiên hiện có thay đổi, có thể do hành vi NAT, router có thể sử dụng các phương pháp heuristic tốn kém để cố gắng khớp gói tin với phiên hiện có và khôi phục nội dung.

SSU 2 được thiết kế để giảm thiểu nỗ lực phân loại gói tin đến trong khi vẫn duy trì khả năng chống DPI và các mối đe dọa khác trên đường truyền. Số Connection ID được bao gồm trong header cho tất cả các loại message, và được mã hóa (làm rối) bằng ChaCha20 với một key và nonce đã biết. Ngoài ra, loại message cũng được bao gồm trong header (được mã hóa với header protection bằng một key đã biết và sau đó được làm rối bằng ChaCha20) và có thể được sử dụng để phân loại thêm. Trong mọi trường hợp, không cần thiết phải thực hiện thử nghiệm DH hoặc các phép toán mã hóa bất đối xứng khác để phân loại một gói tin.

Đối với hầu hết tất cả các tin nhắn từ tất cả các peer, khóa ChaCha20 cho việc mã hóa Connection ID là introduction key của router đích như được công bố trong netDb.

Các trường hợp ngoại lệ duy nhất là những thông điệp đầu tiên được gửi từ Bob đến Alice (Session Created hoặc Retry) khi Bob chưa biết introduction key của Alice. Trong những trường hợp này, introduction key của Bob được sử dụng làm key.

Giao thức được thiết kế để giảm thiểu việc xử lý phân loại gói tin có thể yêu cầu các thao tác mã hóa bổ sung trong nhiều bước dự phòng hoặc các phương pháp phát hiện phức tạp. Ngoài ra, phần lớn các gói tin nhận được sẽ không yêu cầu tra cứu dự phòng (có thể tốn kém) theo IP/port nguồn và giải mã header lần thứ hai. Chỉ có Session Created và Retry (và có thể các loại khác sẽ được xác định) sẽ yêu cầu xử lý dự phòng. Nếu một endpoint thay đổi IP hoặc port sau khi tạo session, connection ID vẫn được sử dụng để tra cứu session. Không bao giờ cần thiết phải sử dụng các phương pháp phát hiện để tìm session, ví dụ như tìm kiếm một session khác có cùng IP nhưng port khác.

Do đó, các bước xử lý được khuyến nghị trong logic vòng lặp receiver là:

1) Giải mã 8 byte đầu tiên bằng ChaCha20 sử dụng khóa introduction cục bộ, để khôi phục Destination Connection ID. Nếu Connection ID khớp với một phiên kết nối đang hoạt động hoặc đang chờ xử lý:

    a)  Using the appropriate key, decrypt the header bytes 8-15 to recover the version, net ID, and message type.
    b)  If the message type is Session Confirmed, it is a long header. Verify the net ID and protocol version are valid. Decrypt the bytes 15-31 of the header with ChaCha20 using the local intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise.
    c)  If the message type is valid but not Session Confirmed, it is a short header. Verify the net ID and protocol version are valid. decrypt the rest of the message with ChaCha20/Poly1305 using the session key, using the decrypted 16-byte header as the AD.
    d)  (optional) If connection ID is a pending inbound session awaiting a Session Confirmed message, but the net ID, protocol, or message type is not valid, it could be a Data message received out-of-order before the Session Confirmed, so the data phase header protection keys are not yet known, and the header bytes 8-15 were incorrectly decrypted. Queue the message, and attempt to decrypt it once the Session Confirmed message is received.
    e)  If b) or c) fails, drop the message.

2) Nếu ID kết nối không khớp với phiên hiện tại: Kiểm tra header plaintext tại các byte 8-15 có hợp lệ (mà không thực hiện bất kỳ thao tác bảo vệ header nào). Xác minh net ID và phiên bản giao thức hợp lệ, và loại thông điệp là Session Request, hoặc loại thông điệp khác được phép ngoài phiên (TBD).

    a)  If all is valid and the message type is Session Request, decrypt bytes 16-31 of the header and the 32-byte X value with ChaCha20 using the local intro key.

    - If the token at header bytes 24-31 is accepted, then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Created in response.
    - If the token is not accepted, send a Retry message to the source IP/port with a token. Do not attempt to decrypt the message with Noise to avoid DDoS attacks.

    b)  If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.
    c)  If a) or b) fails, go to step 3)

3) Tra cứu một phiên gửi đi đang chờ xử lý theo IP/cổng nguồn của gói tin.

    a)  If found, re-decrypt the first 8 bytes with ChaCha20 using Bob's introduction key to recover the Destination Connection ID.
    b)  If the connection ID matches the pending session: Using the correct key, decrypt bytes 8-15 of the header to recover the version, net ID, and message type. Verify the net ID and protocol version are valid, and the message type is Session Created or Retry, or other message type allowed out-of-session (TBD).

    - If all is valid and the message type is Session Created, decrypt the next 16 bytes of the header and the 32-byte Y value with ChaCha20 using Bob's intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Confirmed in response.
    - If all is valid and the message type is Retry, decrypt bytes 16-31 of the header with ChaCha20 using Bob's intro key. Decrypt and validate the message using ChaCha20/Poly1305 using TBD as the key and TBD as the nonce and the decrypted 32-byte header as the AD. Resend a Session Request with the received token in response.
    - If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.

    > c)  If a pending outbound session is not found, or the connection ID does not match the pending session, drop the message, unless the port is shared with SSU 1.

4)  Nếu đang chạy SSU 1 trên cùng cổng, hãy thử xử lý thông điệp như một gói SSU 1.

#### Xử lý Lỗi

Nói chung, một phiên (trong giai đoạn handshake hoặc dữ liệu) không bao giờ nên bị hủy sau khi nhận được một gói tin với loại thông điệp không mong đợi. Điều này ngăn chặn các cuộc tấn công tiêm gói tin. Những gói tin này cũng thường được nhận sau khi truyền lại gói tin handshake, khi các khóa giải mã header không còn hợp lệ.

Trong hầu hết các trường hợp, chỉ cần loại bỏ gói tin. Một triển khai có thể, nhưng không bắt buộc, truyền lại gói tin đã gửi trước đó (thông điệp handshake hoặc ACK 0) để phản hồi.

Sau khi gửi Session Created với vai trò Bob, các gói tin bất ngờ thường là các gói Data không thể giải mã được vì các gói Session Confirmed đã bị mất hoặc không đúng thứ tự. Xếp các gói tin này vào hàng đợi và thử giải mã chúng sau khi nhận được các gói Session Confirmed.

Sau khi nhận được Session Confirmed với vai trò Bob, các gói tin không mong muốn thường là các gói tin Session Confirmed được truyền lại, bởi vì ACK 0 của Session Confirmed đã bị mất. Các gói tin không mong muốn này có thể bị loại bỏ. Một implementation có thể, nhưng không bắt buộc, gửi một gói tin Data chứa khối ACK để phản hồi.

### Ghi chú

Đối với Session Created và Session Confirmed, các triển khai phải cẩn thận xác thực tất cả các trường header đã được giải mã (Connection IDs, packet number, packet type, version, id, frag, và flags) TRƯỚC KHI gọi mixHash() trên header và cố gắng giải mã payload bằng Noise AEAD. Nếu việc giải mã Noise AEAD thất bại, không được thực hiện xử lý tiếp theo nào nữa, vì mixHash() sẽ làm hỏng trạng thái handshake, trừ khi một triển khai lưu trữ và "khôi phục" trạng thái hash.

### Phát hiện Phiên bản

Có thể không hiệu quả khi phát hiện các gói tin đến là phiên bản 1 hay 2 trên cùng một cổng đầu vào. Các bước trên có thể hợp lý khi thực hiện trước khi xử lý SSU 1, để tránh thử các phép toán DH bằng cả hai phiên bản giao thức.

Sẽ được xác định nếu cần thiết.

## Các Hằng Số Được Khuyến Nghị

- Timeout truyền lại handshake đầu ra: 1.25 giây, với backoff theo cấp số nhân (truyền lại tại 1.25, 3.75, và 8.75 giây)
- Tổng timeout handshake đầu ra: 15 giây
- Timeout truyền lại handshake đầu vào: 1 giây, với backoff theo cấp số nhân (truyền lại tại 1, 3, và 7 giây)
- Tổng timeout handshake đầu vào: 12 giây
- Timeout sau khi gửi retry: 9 giây
- Độ trễ ACK: max(10, min(rtt/6, 150)) ms
- Độ trễ ACK tức thì: min(rtt/16, 5) ms
- Số lượng ACK ranges tối đa: 256?
- Độ sâu ACK tối đa: 512?
- Phân phối padding: 0-15 byte, hoặc lớn hơn
- Timeout truyền lại tối thiểu giai đoạn dữ liệu: 1 giây, như trong [RFC-6298](https://tools.ietf.org/html/rfc6298)
- Xem thêm [RFC-6298](https://tools.ietf.org/html/rfc6298) để có thêm hướng dẫn về bộ đếm thời gian truyền lại cho giai đoạn dữ liệu.

## Phân Tích Chi Phí Gói Tin

Giả sử IPv4, không bao gồm padding bổ sung, không bao gồm kích thước header IP và UDP. Padding là mod-16 padding chỉ dành cho SSU 1.

**SSU 1**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MAC</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">40</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">304</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. extended options</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">79</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">336</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 64 byte Ed25519 sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">462</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">512</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 391 byte ident and 64 byte sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (RI)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1014</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1051</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header, 1000 byte RI</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">51</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">2254</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>
**SSU 2**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MACs</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">87</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">96</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime, Address blocks</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1005</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1085</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1000 byte compressed RI block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">46</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1314</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>    
## Các Vấn Đề và Công Việc Tương Lai

### Token

Chúng tôi chỉ định ở trên rằng token phải là một giá trị 8 byte được tạo ngẫu nhiên, không được tạo một giá trị mờ đục như hash hoặc HMAC của một server secret và IP, port, do các cuộc tấn công tái sử dụng. Tuy nhiên, điều này yêu cầu lưu trữ tạm thời và (tùy chọn) lưu trữ liên tục các token đã gửi. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) sử dụng HMAC 16-byte của một server secret và địa chỉ IP, và server secret xoay vòng mỗi hai phút. Chúng ta nên điều tra một cái gì đó tương tự, với thời gian tồn tại server secret dài hơn. Nếu chúng ta nhúng một timestamp vào token, đó có thể là một giải pháp, nhưng một token 8-byte có thể không đủ lớn cho việc đó.

## Tài liệu tham khảo

- **[Common]** [Đặc tả Cấu trúc Chung](/docs/specs/common-structures)
- **[ECIES]** [Đặc tả ECIES-X25519-AEAD-Ratchet](/docs/specs/ecies)
- **[NetDB]** [Cơ sở Dữ liệu Mạng](/docs/overview/network-database)
- **[NOISE]** [Khung Giao thức Noise](https://noiseprotocol.org/noise.html)
- **[Nonces]** [Đối thủ Không tôn trọng Nonce](https://eprint.iacr.org/2019/624.pdf)
- **[NTCP]** [Giao thức Vận chuyển NTCP](/docs/transport/ntcp)
- **[NTCP2]** [Đặc tả NTCP2](/docs/specs/ntcp2)
- **[PMTU]** [Khám phá MTU Đường đi](https://en.wikipedia.org/wiki/Path_MTU_Discovery)
- **[Prop104]** [Đề xuất 104: Giao thức Vận chuyển TLS](/proposals/104-tls-transport)
- **[Prop109]** [Đề xuất 109: Giao thức Vận chuyển Cắm được](/proposals/109-pt-transport)
- **[Prop158]** [Đề xuất 158: Cải tiến Giao thức Vận chuyển IPv6](/proposals/158-ipv6-transport-enhancements)
- **[Prop159]** [Đề xuất 159: SSU2](/proposals/159-ssu2)
- **[RFC-2104]** [RFC 2104: HMAC](https://tools.ietf.org/html/rfc2104)
- **[RFC-3449]** [RFC 3449: Tác động Hiệu năng TCP](https://tools.ietf.org/html/rfc3449)
- **[RFC-3526]** [RFC 3526: Nhóm MODP](https://tools.ietf.org/html/rfc3526)
- **[RFC-5681]** [RFC 5681: Kiểm soát Tắc nghẽn TCP](https://tools.ietf.org/html/rfc5681)
- **[RFC-5869]** [RFC 5869: HKDF](https://tools.ietf.org/html/rfc5869)
- **[RFC-6151]** [RFC 6151: Cân nhắc Bảo mật MD5](https://tools.ietf.org/html/rfc6151)
- **[RFC-6298]** [RFC 6298: Bộ định thời Truyền lại TCP](https://tools.ietf.org/html/rfc6298)
- **[RFC-6437]** [RFC 6437: Nhãn Luồng IPv6](https://tools.ietf.org/html/rfc6437)
- **[RFC-7539]** [RFC 7539: ChaCha20/Poly1305](https://tools.ietf.org/html/rfc7539)
- **[RFC-7748]** [RFC 7748: Đường cong Elliptic cho Bảo mật](https://tools.ietf.org/html/rfc7748)
- **[RFC-7905]** [RFC 7905: Bộ mã hóa ChaCha20-Poly1305 cho TLS](https://tools.ietf.org/html/rfc7905)
- **[RFC-9000]** [RFC 9000: Giao thức Vận chuyển QUIC](https://datatracker.ietf.org/doc/html/rfc9000)
- **[RFC-9001]** [RFC 9001: Sử dụng TLS để Bảo mật QUIC](https://datatracker.ietf.org/doc/html/rfc9001)
- **[RFC-9002]** [RFC 9002: Phát hiện Mất mát và Kiểm soát Tắc nghẽn QUIC](https://datatracker.ietf.org/doc/html/rfc9002)
- **[RouterAddress]** [Cấu trúc RouterAddress](/docs/specs/common-structures#struct-routeraddress)
- **[RouterIdentity]** [Cấu trúc RouterIdentity](/docs/specs/common-structures#struct-routeridentity)
- **[SigningPublicKey]** [Kiểu SigningPublicKey](/docs/specs/common-structures#type-signingpublickey)
- **[SSU]** [Giao thức Vận chuyển SSU](/docs/transport/ssu)
- **[STS]** [Giao thức Station-to-Station](https://en.wikipedia.org/wiki/Station-to-Station_protocol)
- **[Ticket1112]** I2P Ticket 1112
- **[Ticket1849]** I2P Ticket 1849
- **[WireGuard]** [Giao thức WireGuard](https://www.wireguard.com/papers/wireguard.pdf)
