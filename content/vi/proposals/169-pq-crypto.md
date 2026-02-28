---
title: "Các Giao Thức Mật Mã Hậu Lượng Tử"
aliases: 
number: "169"
author: "zzz, orignal, drzed, eyedeekay"
created: "2025-01-21"
lastupdated: "2026-02-28"
status: "Mở"
thread: "http://zzz.i2p/topics/3294"
target: "0.9.80"
toc: true
---

### Trạng thái

| Giao thức / Tính năng | Trạng thái |
|--------------------|--------|
| Ratchet | Hoàn thành trong Java I2P và i2pd |
| NTCP2 | Beta Q1 2026 |
| SSU2 | Bắt đầu triển khai sớm, Beta Q23 2026 |
| MLDSA SigTypes | Ưu tiên thấp, có thể 2027+ |
## Tổng quan

Trong khi nghiên cứu và cạnh tranh để tìm ra mật mã học hậu lượng tử (PQ) phù hợp đã tiến hành trong một thập kỷ, các lựa chọn vẫn chưa rõ ràng cho đến gần đây.

Chúng tôi bắt đầu xem xét các tác động của mật mã PQ vào năm 2022 [zzz.i2p](http://zzz.i2p/topics/3294).

Các tiêu chuẩn TLS đã bổ sung hỗ trợ mã hóa lai trong hai năm qua và hiện được sử dụng cho một phần đáng kể lưu lượng mã hóa trên internet do được hỗ trợ trong Chrome và Firefox [Cloudflare](https://blog.cloudflare.com/pq-2024/).

NIST gần đây đã hoàn thiện và công bố các thuật toán được khuyến nghị cho mật mã học hậu lượng tử [NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards). Một số thư viện mật mã phổ biến hiện đã hỗ trợ các tiêu chuẩn NIST hoặc sẽ phát hành hỗ trợ trong tương lai gần.

Cả [Cloudflare](https://blog.cloudflare.com/pq-2024/) và [NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) đều khuyến nghị việc di chuyển nên bắt đầu ngay lập tức. Xem thêm tài liệu FAQ PQ năm 2022 của NSA [NSA](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF). I2P nên là người dẫn đầu trong lĩnh vực bảo mật và mật mã học. Đây là thời điểm để triển khai các thuật toán được khuyến nghị. Sử dụng hệ thống linh hoạt về loại mật mã và loại chữ ký của chúng ta, chúng ta sẽ thêm các loại cho mật mã kết hợp, và cho PQ và chữ ký kết hợp.

## Mục tiêu

- Chọn các thuật toán kháng PQ
- Thêm các thuật toán chỉ-PQ và lai ghép vào các giao thức I2P khi thích hợp
- Định nghĩa nhiều biến thể
- Chọn các biến thể tốt nhất sau khi triển khai, thử nghiệm, phân tích và nghiên cứu
- Thêm hỗ trợ từng bước và với khả năng tương thích ngược

## Phi Mục Tiêu

- Không thay đổi các giao thức mã hóa một chiều (Noise N)
- Không chuyển sang khác SHA256, không bị đe dọa trong thời gian gần bởi PQ
- Không lựa chọn các biến thể ưa thích cuối cùng tại thời điểm này

## Mô hình Mối đe dọa

- Router tại OBEP hoặc IBGW, có thể đồng lõa,
  lưu trữ garlic message để giải mã sau này (bảo mật chuyển tiếp)
- Những kẻ quan sát mạng
  lưu trữ transport message để giải mã sau này (bảo mật chuyển tiếp)
- Những thành viên mạng giả mạo chữ ký cho RI, LS, streaming, datagram,
  hoặc các cấu trúc khác

## Các giao thức bị ảnh hưởng

Chúng tôi sẽ sửa đổi các giao thức sau đây, theo thứ tự phát triển gần đúng. Việc triển khai tổng thể có thể sẽ diễn ra từ cuối năm 2025 đến giữa năm 2027. Xem phần Ưu tiên và Triển khai bên dưới để biết chi tiết.

| Giao thức / Tính năng | Trạng thái |
|--------------------|--------|
| Hybrid MLKEM Ratchet và LS | Đã phê duyệt 2025-06; beta 2025-08; phát hành 2025-11 |
| Hybrid MLKEM NTCP2 | Đã thử nghiệm trên mạng thực, Đã phê duyệt 2026-02; mục tiêu beta 2026-05; mục tiêu phát hành 2026-08 |
| Hybrid MLKEM SSU2 | Đã phê duyệt 2026-02; mục tiêu beta 2026-08; mục tiêu phát hành 2026-11 |
| MLDSA SigTypes 12-14 | Đề xuất ổn định nhưng có thể không được hoàn thiện đến tận 2027 |
| MLDSA Dests | Đã thử nghiệm trên mạng thực, yêu cầu nâng cấp mạng để hỗ trợ floodfill |
| Hybrid SigTypes 15-17 | Sơ bộ |
| Hybrid Dests | |
## Thiết kế

Chúng tôi sẽ hỗ trợ các tiêu chuẩn NIST FIPS 203 và 204 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) được dựa trên, nhưng KHÔNG tương thích với, CRYSTALS-Kyber và CRYSTALS-Dilithium (phiên bản 3.1, 3, và các phiên bản cũ hơn).

### Trao đổi khóa

Chúng tôi sẽ hỗ trợ trao đổi khóa kết hợp trong các giao thức sau:

| Proto   | Loại Noise | Chỉ hỗ trợ PQ? | Hỗ trợ Hybrid? |
|---------|-------------|----------------|----------------|
| NTCP2   | XK          | không          | có             |
| SSU2    | XK          | không          | có             |
| Ratchet | IK          | không          | có             |
| TBM     | N           | không          | không          |
| NetDB   | N           | không          | không          |
PQ KEM chỉ cung cấp các khóa tạm thời và không hỗ trợ trực tiếp các handshake khóa tĩnh như Noise XK và IK.

Noise N không sử dụng trao đổi khóa hai chiều và do đó không phù hợp cho mã hóa lai.

Vì vậy chúng tôi sẽ chỉ hỗ trợ mã hóa lai, cho NTCP2, SSU2, và Ratchet. Chúng tôi sẽ định nghĩa ba biến thể ML-KEM như trong [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf), tổng cộng cho 3 loại mã hóa mới. Các loại lai sẽ chỉ được định nghĩa khi kết hợp với X25519.

Các loại mã hóa mới là:

| Loại | Mã |
|------|------|
| MLKEM512_X25519 | 5 |
| MLKEM768_X25519 | 6 |
| MLKEM1024_X25519 | 7 |
Chi phí overhead sẽ rất lớn. Kích thước điển hình của message 1 và 2 (cho XK và IK) hiện tại khoảng 100 byte (trước khi có bất kỳ payload bổ sung nào). Điều này sẽ tăng từ 8 đến 15 lần tùy thuộc vào thuật toán.

### Chữ ký

Chúng tôi sẽ hỗ trợ các chữ ký PQ và hybrid trong các cấu trúc sau:

| Loại | Hỗ trợ chỉ PQ? | Hỗ trợ Hybrid? |
|------|------------------|-----------------|
| RouterInfo | có | có |
| LeaseSet | có | có |
| Streaming SYN/SYNACK/Close | có | có |
| Repliable Datagrams | có | có |
| Datagram2 (prop. 163) | có | có |
| I2CP create session msg | có | có |
| SU3 files | có | có |
| X.509 certificates | có | có |
| Java keystores | có | có |
Vì vậy chúng tôi sẽ hỗ trợ cả chữ ký PQ-only và hybrid. Chúng tôi sẽ định nghĩa ba biến thể ML-DSA như trong [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf), ba biến thể hybrid với Ed25519, và ba biến thể PQ-only với prehash chỉ dành cho tập tin SU3, tổng cộng 9 loại chữ ký mới. Các loại hybrid sẽ chỉ được định nghĩa kết hợp với Ed25519. Chúng tôi sẽ sử dụng ML-DSA tiêu chuẩn, KHÔNG phải các biến thể pre-hash (HashML-DSA), trừ trường hợp tập tin SU3.

Chúng tôi sẽ sử dụng biến thể ký "hedged" hoặc ngẫu nhiên hóa, không phải biến thể "deterministic", như được định nghĩa trong [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) phần 3.4. Điều này đảm bảo rằng mỗi chữ ký đều khác nhau, ngay cả khi ký trên cùng một dữ liệu, và cung cấp thêm bảo vệ chống lại các cuộc tấn công kênh bên. Xem phần ghi chú triển khai bên dưới để biết thêm chi tiết về các lựa chọn thuật toán bao gồm mã hóa và ngữ cảnh.

Các loại chữ ký mới là:

| Loại | Mã |
|------|------|
| MLDSA44 | 12 |
| MLDSA65 | 13 |
| MLDSA87 | 14 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 |
| MLDSA44ph | 18 |
| MLDSA65ph | 19 |
| MLDSA87ph | 20 |
Chứng chỉ X.509 và các mã hóa DER khác sẽ sử dụng các cấu trúc tổng hợp và OID được định nghĩa trong [bản nháp IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/).

Chi phí overhead sẽ rất đáng kể. Kích thước điển hình của destination và router identity Ed25519 là 391 byte. Những kích thước này sẽ tăng từ 3.5x đến 6.8x tùy thuộc vào thuật toán. Chữ ký Ed25519 có kích thước 64 byte. Những chữ ký này sẽ tăng từ 38x đến 76x tùy thuộc vào thuật toán. RouterInfo đã ký, LeaseSet, datagram có thể trả lời, và streaming message đã ký thường có kích thước khoảng 1KB. Những thông tin này sẽ tăng từ 3x đến 8x tùy thuộc vào thuật toán.

Vì các loại danh tính destination và router mới sẽ không chứa padding, chúng sẽ không thể nén được. Kích thước của các destination và danh tính router được nén gzip khi truyền tải sẽ tăng từ 12x - 38x tùy thuộc vào thuật toán.

### Các Kết Hợp Hợp Lệ

Đối với Destinations, các loại chữ ký mới được hỗ trợ với tất cả các loại mã hóa trong leaseset. Đặt loại mã hóa trong key certificate thành NONE (255).

Đối với RouterIdentities, loại mã hóa ElGamal đã bị ngừng hỗ trợ. Các loại chữ ký mới chỉ được hỗ trợ với mã hóa X25519 (loại 4). Các loại mã hóa mới sẽ được chỉ định trong RouterAddresses. Loại mã hóa trong key certificate sẽ tiếp tục là loại 4.

### Cần Mã Hóa Mới

- ML-KEM (trước đây là CRYSTALS-Kyber) [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
- ML-DSA (trước đây là CRYSTALS-Dilithium) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
- SHA3-128 (trước đây là Keccak-256) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf) Chỉ được sử dụng cho SHAKE128
- SHA3-256 (trước đây là Keccak-512) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
- SHAKE128 và SHAKE256 (phần mở rộng XOF cho SHA3-128 và SHA3-256) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)

Các test vector cho SHA3-256, SHAKE128, và SHAKE256 có tại [NIST](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values).

Lưu ý rằng thư viện Java bouncycastle hỗ trợ tất cả các mục trên. Hỗ trợ thư viện C++ có trong OpenSSL 3.5 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

### Các lựa chọn thay thế

Chúng tôi sẽ không hỗ trợ [FIPS 205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf) (Sphincs+), vì nó chậm hơn và lớn hơn rất nhiều so với ML-DSA. Chúng tôi sẽ không hỗ trợ FIPS206 sắp tới (Falcon), vì nó chưa được chuẩn hóa. Chúng tôi sẽ không hỗ trợ NTRU hoặc các ứng cử viên PQ khác mà không được NIST chuẩn hóa.

### Rosenpass

Có một số nghiên cứu [paper](https://eprint.iacr.org/2020/379.pdf) về việc điều chỉnh Wireguard (IK) cho mã hóa PQ thuần túy, nhưng có một số câu hỏi mở trong bài nghiên cứu đó. Sau đó, cách tiếp cận này đã được triển khai dưới dạng Rosenpass [Rosenpass](https://rosenpass.eu/) [whitepaper](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf) cho PQ Wireguard.

Rosenpass sử dụng một bắt tay giống Noise KK với các khóa tĩnh Classic McEliece 460896 được chia sẻ trước (mỗi khóa 500 KB) và các khóa tạm thời Kyber-512 (về cơ bản là MLKEM-512). Vì các bản mã Classic McEliece chỉ có 188 byte, và các khóa công khai cùng bản mã Kyber-512 có kích thước hợp lý, cả hai thông điệp bắt tay đều vừa với MTU UDP tiêu chuẩn. Khóa chia sẻ đầu ra (osk) từ quá trình bắt tay PQ KK được sử dụng làm khóa chia sẻ trước đầu vào (psk) cho quá trình bắt tay Wireguard IK tiêu chuẩn. Vậy tổng cộng có hai quá trình bắt tay hoàn chỉnh, một quá trình PQ thuần túy và một quá trình X25519 thuần túy.

Chúng ta không thể làm bất kỳ điều gì trong số này để thay thế các handshake XK và IK của chúng ta vì:

- Chúng ta không thể thực hiện KK, Bob không có khóa tĩnh của Alice
- Khóa tĩnh 500KB là quá lớn
- Chúng ta không muốn có thêm một vòng trao đổi

Có rất nhiều thông tin hữu ích trong whitepaper, và chúng tôi sẽ xem xét nó để tìm ý tưởng và cảm hứng. TODO.

## Đặc tả kỹ thuật

### Cấu trúc chung

Cập nhật các phần và bảng trong tài liệu cấu trúc chung [/docs/specs/common-structures/](/docs/specs/common-structures/) như sau:

### PublicKey

Các loại Public Key mới là:

| Loại | Độ dài Public Key | Từ phiên bản | Cách sử dụng |
|------|-------------------|-------|-------|
| MLKEM512_X25519 | 32 | 0.9.xx | Xem đề xuất 169, chỉ dành cho Leasesets, không dành cho RIs hoặc Destinations |
| MLKEM768_X25519 | 32 | 0.9.xx | Xem đề xuất 169, chỉ dành cho Leasesets, không dành cho RIs hoặc Destinations |
| MLKEM1024_X25519 | 32 | 0.9.xx | Xem đề xuất 169, chỉ dành cho Leasesets, không dành cho RIs hoặc Destinations |
| MLKEM512 | 800 | 0.9.xx | Xem đề xuất 169, chỉ dành cho handshakes, không dành cho Leasesets, RIs hoặc Destinations |
| MLKEM768 | 1184 | 0.9.xx | Xem đề xuất 169, chỉ dành cho handshakes, không dành cho Leasesets, RIs hoặc Destinations |
| MLKEM1024 | 1568 | 0.9.xx | Xem đề xuất 169, chỉ dành cho handshakes, không dành cho Leasesets, RIs hoặc Destinations |
| MLKEM512_CT | 768 | 0.9.xx | Xem đề xuất 169, chỉ dành cho handshakes, không dành cho Leasesets, RIs hoặc Destinations |
| MLKEM768_CT | 1088 | 0.9.xx | Xem đề xuất 169, chỉ dành cho handshakes, không dành cho Leasesets, RIs hoặc Destinations |
| MLKEM1024_CT | 1568 | 0.9.xx | Xem đề xuất 169, chỉ dành cho handshakes, không dành cho Leasesets, RIs hoặc Destinations |
| NONE | 0 | 0.9.xx | Xem đề xuất 169, chỉ dành cho destinations với loại chữ ký PQ, không dành cho RIs hoặc Leasesets |
Khóa công khai lai (hybrid public keys) là khóa X25519. Khóa công khai KEM là khóa PQ tạm thời được gửi từ Alice đến Bob. Việc mã hóa và thứ tự byte được định nghĩa trong [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

Các khóa MLKEM*_CT không thực sự là khóa công khai, chúng là "bản mã" được gửi từ Bob đến Alice trong quá trình bắt tay Noise. Chúng được liệt kê ở đây cho đầy đủ thông tin.

### PrivateKey

Các loại Private Key mới là:

| Loại | Độ dài Private Key | Từ phiên bản | Cách sử dụng |
|------|---------------------|-------|-------|
| MLKEM512_X25519 | 32 | 0.9.xx | Xem đề xuất 169, chỉ dành cho Leasesets, không dành cho RIs hoặc Destinations |
| MLKEM768_X25519 | 32 | 0.9.xx | Xem đề xuất 169, chỉ dành cho Leasesets, không dành cho RIs hoặc Destinations |
| MLKEM1024_X25519 | 32 | 0.9.xx | Xem đề xuất 169, chỉ dành cho Leasesets, không dành cho RIs hoặc Destinations |
| MLKEM512 | 1632 | 0.9.xx | Xem đề xuất 169, chỉ dành cho handshakes, không dành cho Leasesets, RIs hoặc Destinations |
| MLKEM768 | 2400 | 0.9.xx | Xem đề xuất 169, chỉ dành cho handshakes, không dành cho Leasesets, RIs hoặc Destinations |
| MLKEM1024 | 3168 | 0.9.xx | Xem đề xuất 169, chỉ dành cho handshakes, không dành cho Leasesets, RIs hoặc Destinations |
Khóa riêng tư hybrid là các khóa X25519. Khóa riêng tư KEM chỉ dành cho Alice. Mã hóa KEM và thứ tự byte được định nghĩa trong [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

### SigningPublicKey

Các loại Signing Public Key mới là:

| Loại | Độ dài (bytes) | Từ phiên bản | Cách sử dụng |
|------|----------------|-------|-------|
| MLDSA44 | 1312 | 0.9.xx | Xem đề xuất 169 |
| MLDSA65 | 1952 | 0.9.xx | Xem đề xuất 169 |
| MLDSA87 | 2592 | 0.9.xx | Xem đề xuất 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 1344 | 0.9.xx | Xem đề xuất 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 1984 | 0.9.xx | Xem đề xuất 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 2624 | 0.9.xx | Xem đề xuất 169 |
| MLDSA44ph | 1344 | 0.9.xx | Chỉ dành cho tệp SU3, không dành cho cấu trúc netDb |
| MLDSA65ph | 1984 | 0.9.xx | Chỉ dành cho tệp SU3, không dành cho cấu trúc netDb |
| MLDSA87ph | 2624 | 0.9.xx | Chỉ dành cho tệp SU3, không dành cho cấu trúc netDb |
Hybrid signing public keys là Ed25519 key theo sau bởi PQ key, như trong [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/). Encoding và byte order được định nghĩa trong [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf).

### SigningPrivateKey

Các loại Signing Private Key mới là:

| Loại | Độ dài (bytes) | Từ phiên bản | Cách sử dụng |
|------|----------------|-------|-------|
| MLDSA44 | 2560 | 0.9.xx | Xem đề xuất 169 |
| MLDSA65 | 4032 | 0.9.xx | Xem đề xuất 169 |
| MLDSA87 | 4896 | 0.9.xx | Xem đề xuất 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 2592 | 0.9.xx | Xem đề xuất 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 4064 | 0.9.xx | Xem đề xuất 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 4928 | 0.9.xx | Xem đề xuất 169 |
| MLDSA44ph | 2592 | 0.9.xx | Chỉ dành cho tệp SU3, không dành cho cấu trúc netDb. Xem đề xuất 169 |
| MLDSA65ph | 4064 | 0.9.xx | Chỉ dành cho tệp SU3, không dành cho cấu trúc netDb. Xem đề xuất 169 |
| MLDSA87ph | 4928 | 0.9.xx | Chỉ dành cho tệp SU3, không dành cho cấu trúc netDb. Xem đề xuất 169 |
Khóa riêng tư ký lai (hybrid signing private keys) là khóa Ed25519 theo sau bởi khóa PQ, như trong [bản thảo IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/). Mã hóa và thứ tự byte được định nghĩa trong [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf).

### Chữ ký

Các loại Signature mới là:

| Loại | Độ dài (bytes) | Từ phiên bản | Sử dụng |
|------|----------------|-------|-------|
| MLDSA44 | 2420 | 0.9.xx | Xem đề xuất 169 |
| MLDSA65 | 3309 | 0.9.xx | Xem đề xuất 169 |
| MLDSA87 | 4627 | 0.9.xx | Xem đề xuất 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 2484 | 0.9.xx | Xem đề xuất 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 3373 | 0.9.xx | Xem đề xuất 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 4691 | 0.9.xx | Xem đề xuất 169 |
| MLDSA44ph | 2484 | 0.9.xx | Chỉ dành cho các tệp SU3, không dành cho cấu trúc netDb. Xem đề xuất 169 |
| MLDSA65ph | 3373 | 0.9.xx | Chỉ dành cho các tệp SU3, không dành cho cấu trúc netDb. Xem đề xuất 169 |
| MLDSA87ph | 4691 | 0.9.xx | Chỉ dành cho các tệp SU3, không dành cho cấu trúc netDb. Xem đề xuất 169 |
Chữ ký lai là chữ ký Ed25519 theo sau bởi chữ ký PQ, như trong [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/). Chữ ký lai được xác minh bằng cách xác minh cả hai chữ ký, và sẽ thất bại nếu một trong hai chữ ký thất bại. Mã hóa và thứ tự byte được định nghĩa trong [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf).

### Chứng chỉ khóa

Các loại Signing Public Key mới là:

| Loại | Mã Loại | Tổng Độ Dài Public Key | Từ Phiên Bản | Sử Dụng |
|------|-----------|-------------------------|-------|-------|
| MLDSA44 | 12 | 1312 | 0.9.xx | Xem đề xuất 169 |
| MLDSA65 | 13 | 1952 | 0.9.xx | Xem đề xuất 169 |
| MLDSA87 | 14 | 2592 | 0.9.xx | Xem đề xuất 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 0.9.xx | Xem đề xuất 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 0.9.xx | Xem đề xuất 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 0.9.xx | Xem đề xuất 169 |
| MLDSA44ph | 18 | n/a | 0.9.xx | Chỉ dành cho các tệp SU3 |
| MLDSA65ph | 19 | n/a | 0.9.xx | Chỉ dành cho các tệp SU3 |
| MLDSA87ph | 20 | n/a | 0.9.xx | Chỉ dành cho các tệp SU3 |
Các loại Crypto Public Key mới là:

| Loại | Mã Loại | Tổng Độ Dài Public Key | Từ Phiên Bản | Cách Sử Dụng |
|------|-----------|-------------------------|-------|-------|
| MLKEM512_X25519 | 5 | 32 | 0.9.xx | Xem đề xuất 169, chỉ dành cho Leasesets, không dành cho RIs hoặc Destinations |
| MLKEM768_X25519 | 6 | 32 | 0.9.xx | Xem đề xuất 169, chỉ dành cho Leasesets, không dành cho RIs hoặc Destinations |
| MLKEM1024_X25519 | 7 | 32 | 0.9.xx | Xem đề xuất 169, chỉ dành cho Leasesets, không dành cho RIs hoặc Destinations |
| NONE | 255 | 0 | 0.9.xx | Xem đề xuất 169 |
Các loại khóa hybrid KHÔNG BAO GIỜ được bao gồm trong chứng chỉ khóa; chỉ có trong leaseSet.

Đối với các đích có loại chữ ký Hybrid hoặc PQ, sử dụng NONE (loại 255) cho loại mã hóa, nhưng không có khóa mã hóa, và toàn bộ phần chính 384 byte là dành cho khóa ký.

### Kích thước Destination

Dưới đây là độ dài cho các loại Destination mới. Loại mã hóa cho tất cả đều là NONE (loại 255) và độ dài khóa mã hóa được coi như 0. Toàn bộ phần 384 byte được sử dụng cho phần đầu tiên của khóa công khai ký. LƯU Ý: Điều này khác với đặc tả cho các loại chữ ký ECDSA_SHA512_P521 và RSA, nơi chúng ta duy trì khóa ElGamal 256 byte trong destination mặc dù nó không được sử dụng.

Không có padding. Tổng chiều dài là 7 + tổng chiều dài key. Chiều dài key certificate là 4 + chiều dài key vượt quá.

Ví dụ luồng byte đích 1319-byte cho MLDSA44:

skey[0:383] 5 (932 >> 8) (932 & 0xff) 00 12 00 255 skey[384:1311]

| Loại | Mã Loại | Tổng Độ Dài Khóa Công Khai | Chính | Thừa | Tổng Độ Dài Dest |
|------|-----------|-------------------------|------|--------|-------------------|
| MLDSA44 | 12 | 1312 | 384 | 928 | 1319 |
| MLDSA65 | 13 | 1952 | 384 | 1568 | 1959 |
| MLDSA87 | 14 | 2592 | 384 | 2208 | 2599 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 384 | 960 | 1351 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 384 | 1600 | 1991 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 384 | 2240 | 2631 |
### Kích thước RouterIdent

Đây là độ dài cho các loại Destination mới. Loại mã hóa cho tất cả là X25519 (loại 4). Toàn bộ phần 352-byte sau khóa công khai X25519 được sử dụng cho phần đầu của khóa công khai ký. Không có padding. Tổng độ dài là 39 + tổng độ dài khóa. Độ dài chứng chỉ khóa là 4 + độ dài khóa dư thừa.

Ví dụ luồng byte nhận dạng router 1351-byte cho MLDSA44:

enckey[0:31] skey[0:351] 5 (960 >> 8) (960 & 0xff) 00 12 00 4 skey[352:1311]

| Loại | Mã Loại | Tổng Chiều Dài Public Key | Chính | Dư Thừa | Tổng Chiều Dài RouterIdent |
|------|-----------|-------------------------|------|--------|--------------------------|
| MLDSA44 | 12 | 1312 | 352 | 960 | 1351 |
| MLDSA65 | 13 | 1952 | 352 | 1600 | 1991 |
| MLDSA87 | 14 | 2592 | 352 | 2240 | 2631 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 352 | 992 | 1383 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 352 | 1632 | 2023 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 352 | 2272 | 2663 |
### Các Mẫu Handshake

Handshakes sử dụng các mẫu handshake của [Noise Protocol](https://noiseprotocol.org/noise.html).

Ánh xạ ký tự sau được sử dụng:

- e = khóa tạm thời một lần
- s = khóa tĩnh
- p = tải trọng thông điệp
- e1 = khóa PQ tạm thời một lần, được gửi từ Alice đến Bob
- ekem1 = bản mã KEM, được gửi từ Bob đến Alice

Các sửa đổi sau đây đối với XK và IK để có tính bảo mật tiến (hybrid forward secrecy - hfs) được chỉ định như trong [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) mục 5:

```
XK:                       XKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, p               -> e, es, e1, p
  <- e, ee, p               <- e, ee, ekem1, p
  -> s, se                  -> s, se
  <- p                      <- p
  p ->                      p ->


  IK:                       IKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, s, ss, p       -> e, es, e1, s, ss, p
  <- tag, e, ee, se, p     <- tag, e, ee, ekem1, se, p
  <- p                     <- p
  p ->                     p ->

  e1 and ekem1 are encrypted. See pattern definitions below.
  NOTE: e1 and ekem1 are different sizes (unlike X25519)
```
Mẫu e1 được định nghĩa như sau, theo quy định trong [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) phần 4:

```
For Alice:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++
  MixHash(ciphertext)

  For Bob:

  // DecryptAndHash(ciphertext)
  encap_key = DECRYPT(k, n, ciphertext, ad)
  n++
  MixHash(ciphertext)
```
Mẫu ekem1 được định nghĩa như sau, theo quy định trong [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) phần 4:

```
For Bob:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  MixKey(kem_shared_key)


  For Alice:

  // DecryptAndHash(ciphertext)
  kem_ciphertext = DECRYPT(k, n, ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  MixKey(kem_shared_key)
```
### KDF Bắt tay Noise

#### Vấn đề

- Chúng ta có nên thay đổi hàm hash handshake không? Xem [so sánh](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3).
  SHA256 không dễ bị tổn thương trước PQ, nhưng nếu chúng ta muốn nâng cấp
  hàm hash, thì bây giờ là lúc thích hợp, trong khi chúng ta đang thay đổi những thứ khác.
  Đề xuất SSH IETF hiện tại [bản thảo IETF](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/) là sử dụng MLKEM768
  với SHA256, và MLKEM1024 với SHA384. Đề xuất đó bao gồm
  thảo luận về các cân nhắc bảo mật.
- Chúng ta có nên ngừng gửi dữ liệu ratchet 0-RTT (ngoài LS) không?
- Chúng ta có nên chuyển ratchet từ IK sang XK nếu không gửi dữ liệu 0-RTT không?

#### Tổng quan

Phần này áp dụng cho cả giao thức IK và XK.

Handshake kết hợp được định nghĩa trong [đặc tả Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf). Thông điệp đầu tiên, từ Alice đến Bob, chứa e1, khóa đóng gói, trước payload của thông điệp. Điều này được xử lý như một khóa tĩnh bổ sung; gọi EncryptAndHash() trên nó (với tư cách Alice) hoặc DecryptAndHash() (với tư cách Bob). Sau đó xử lý payload thông điệp như bình thường.

Thông điệp thứ hai, từ Bob gửi cho Alice, chứa ekem1, bản mã hóa, trước payload của thông điệp. Điều này được xem như một khóa tĩnh bổ sung; gọi EncryptAndHash() trên nó (với tư cách là Bob) hoặc DecryptAndHash() (với tư cách là Alice). Sau đó, tính toán kem_shared_key và gọi MixKey(kem_shared_key). Rồi xử lý payload của thông điệp như bình thường.

#### Các Thao Tác ML-KEM Đã Định Nghĩa

Chúng tôi định nghĩa các hàm sau đây tương ứng với các khối xây dựng mật mã được sử dụng như đã định nghĩa trong [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

(encap_key, decap_key) = PQ_KEYGEN()

    Alice creates the encapsulation and decapsulation keys
    The encapsulation key is sent in message 1.
    encap_key and decap_key sizes vary based on ML-KEM variant.

(ciphertext, kem_shared_key) = ENCAPS(encap_key)

    Bob calculates the ciphertext and shared key,
    using the ciphertext received in message 1.
    The ciphertext is sent in message 2.
    ciphertext size varies based on ML-KEM variant.
    The kem_shared_key is always 32 bytes.

kem_shared_key = DECAPS(ciphertext, decap_key)

    Alice calculates the shared key,
    using the ciphertext received in message 2.
    The kem_shared_key is always 32 bytes.

Lưu ý rằng cả encap_key và ciphertext đều được mã hóa bên trong các khối ChaCha/Poly trong các thông điệp bắt tay Noise 1 và 2. Chúng sẽ được giải mã như một phần của quá trình bắt tay.

kem_shared_key được trộn vào chaining key với MixHash(). Xem chi tiết bên dưới.

#### Alice KDF cho Message 1

Đối với XK: Sau mẫu thông báo 'es' và trước payload, thêm:

HOẶC

Đối với IK: Sau mẫu thông điệp 'es' và trước mẫu thông điệp 's', thêm:

```
This is the "e1" message pattern:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)


  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### Bob KDF cho Message 1

Đối với XK: Sau mẫu thông điệp 'es' và trước payload, thêm:

HOẶC

Đối với IK: Sau mẫu tin nhắn 'es' và trước mẫu tin nhắn 's', thêm:

```
This is the "e1" message pattern:

  // DecryptAndHash(encap_key_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  encap_key = DECRYPT(k, n, encap_key_section, ad)
  n++

  // MixHash(encap_key_section)
  h = SHA256(h || encap_key_section)

  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### Bob KDF cho Message 2

Đối với XK: Sau mẫu thông điệp 'ee' và trước payload, thêm vào:

HOẶC

Đối với IK: Sau pattern tin nhắn 'ee' và trước pattern tin nhắn 'se', thêm vào:

```
This is the "ekem1" message pattern:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  // MixKey(kem_shared_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### Alice KDF cho Message 2

Sau mẫu thông điệp 'ee' (và trước mẫu thông điệp 'ss' cho IK), thêm:

```
This is the "ekem1" message pattern:

  // DecryptAndHash(kem_ciphertext_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  kem_ciphertext = DECRYPT(k, n, kem_ciphertext_section, ad)

  // MixHash(kem_ciphertext_section)
  h = SHA256(h || kem_ciphertext_section)

  // MixKey(kem_shared_key)
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### KDF cho Message 3 (chỉ XK)

không thay đổi

#### KDF cho split()

không thay đổi

### Ratchet

Cập nhật đặc tả ECIES-Ratchet [/docs/specs/ecies/](/docs/specs/ecies/) như sau:

#### Định danh Noise

- "Noise_IKhfselg2_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_IKhfselg2_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_IKhfselg2_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1b) Định dạng phiên mới (với ràng buộc)

Thay đổi: Ratchet hiện tại chứa static key trong phần ChaCha đầu tiên, và payload trong phần thứ hai. Với ML-KEM, giờ đây có ba phần. Phần đầu tiên chứa PQ public key được mã hóa. Phần thứ hai chứa static key. Phần thứ ba chứa payload.

Định dạng mã hóa:

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   New Session Ephemeral Public Key    |
  +             32 bytes                  +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           ML-KEM encap_key            +
  |       ChaCha20 encrypted data         |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +    (MAC) for encap_key Section        +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           X25519 Static Key           +
  |       ChaCha20 encrypted data         |
  +             32 bytes                  +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +    (MAC) for Static Key Section       +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
```
Định dạng đã giải mã:

```
Payload Part 1:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +       ML-KEM encap_key                +
  |                                       |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 2:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +       X25519 Static Key               +
  |                                       |
  +      (32 bytes)                       +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 3:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |                                       |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Kích thước:

| Loại | Mã Loại | Độ dài X | Độ dài Msg 1 | Độ dài Msg 1 Mã hóa | Độ dài Msg 1 Giải mã | Độ dài khóa PQ | Độ dài pl |
|------|-----------|-------|-----------|---------------|---------------|------------|--------|
| X25519 | 4 | 32 | 96+pl | 64+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 912+pl | 880+pl | 800+pl | 800 | pl |
| MLKEM768_X25519 | 6 | 32 | 1296+pl | 1360+pl | 1184+pl | 1184 | pl |
| MLKEM1024_X25519 | 7 | 32 | 1680+pl | 1648+pl | 1568+pl | 1568 | pl |
Lưu ý rằng payload phải chứa một khối DateTime, vì vậy kích thước payload tối thiểu là 7. Kích thước tối thiểu của message 1 có thể được tính toán tương ứng.

#### 1g) Định dạng New Session Reply

Thay đổi: Ratchet hiện tại có payload trống cho phần ChaCha đầu tiên, và payload ở phần thứ hai. Với ML-KEM, bây giờ có ba phần. Phần đầu tiên chứa PQ ciphertext được mã hóa. Phần thứ hai có payload trống. Phần thứ ba chứa payload.

Định dạng mã hóa:

```
  +----+----+----+----+----+----+----+----+
  |       Session Tag   8 bytes           |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Ephemeral Public Key           +
  |                                       |
  +            32 bytes                   +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  | ChaCha20 encrypted ML-KEM ciphertext  |
  +      (see table below for length)     +
  ~                                       ~
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +  (MAC) for ciphertext Section         +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +  (MAC) for key Section (no data)      +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
```
Định dạng đã giải mã:

```
Payload Part 1:


  +----+----+----+----+----+----+----+----+
  |                                       |
  +       ML-KEM ciphertext               +
  |                                       |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 2:

  empty

  Payload Part 3:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |                                       |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Kích thước:

| Loại | Mã Loại | Độ dài Y | Độ dài Msg 2 | Độ dài Msg 2 Mã hóa | Độ dài Msg 2 Giải mã | Độ dài PQ CT | Độ dài tùy chọn |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 72+pl | 32+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 856+pl | 816+pl | 768+pl | 768 | pl |
| MLKEM768_X25519 | 6 | 32 | 1176+pl | 1136+pl | 1088+pl | 1088 | pl |
| MLKEM1024_X25519 | 7 | 32 | 1656+pl | 1616+pl | 1568+pl | 1568 | pl |
Lưu ý rằng trong khi message 2 thường có payload khác không, đặc tả ratchet [/docs/specs/ecies/](/docs/specs/ecies/) không yêu cầu điều này, vì vậy kích thước payload tối thiểu là 0. Kích thước tối thiểu của message 2 có thể được tính toán tương ứng.

### NTCP2

Cập nhật đặc tả NTCP2 [/docs/specs/ntcp2/](/docs/specs/ntcp2/) như sau:

#### Định danh Noise

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

Thay đổi: NTCP2 hiện tại chỉ chứa các tùy chọn trong phần ChaCha. Với ML-KEM, phần ChaCha cũng sẽ chứa khóa công khai PQ được mã hóa.

Để PQ và NTCP2 non-PQ có thể được hỗ trợ trên cùng một địa chỉ và cổng router, chúng tôi sử dụng bit có ý nghĩa nhất của giá trị X (khóa công khai tạm thời X25519) để đánh dấu rằng đó là một kết nối PQ. Bit này luôn được tắt cho các kết nối non-PQ.

Đối với Alice, sau khi thông điệp được mã hóa bởi Noise, nhưng trước khi thực hiện làm xáo trộn AES của X, đặt X[31] |= 0x7f.

Đối với Bob, sau khi giải obfuscation AES của X, kiểm tra X[31] & 0x80. Nếu bit được thiết lập, xóa nó bằng X[31] &= 0x7f, và giải mã qua Noise như một kết nối PQ. Nếu bit không được thiết lập, giải mã qua Noise như một kết nối không-PQ như thường lệ.

Đối với PQ NTCP2 được quảng cáo trên địa chỉ router và cổng khác, điều này không bắt buộc.

Để biết thêm thông tin, xem phần Published Addresses bên dưới.

Nội dung thô:

```
  +----+----+----+----+----+----+----+----+
  |        MS bit set to 1 and then       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted X         |
  +             (32 bytes)                +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +      (see table below for length)     +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  ~   n = 0                               ~
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaChaPoly frame (options)          |
  +         32 bytes                      +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  ~         padding (optional)            ~
  |     length defined in options block   |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
Dữ liệu chưa mã hóa (thẻ xác thực Poly1305 không được hiển thị):

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                   X                   |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM encap_key            |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Lưu ý: trường version trong khối tùy chọn message 1 phải được đặt thành 2, ngay cả đối với các kết nối PQ.

Kích thước:

| Loại | Mã Loại | X len | Msg 1 len | Msg 1 Enc len | Msg 1 Dec len | PQ key len | opt len |
|------|-----------|-------|-----------|---------------|---------------|------------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 880+pad | 848 | 816 | 800 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1264+pad | 1232 | 1200 | 1184 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1648+pad | 1616 | 1584 | 1568 | 16 |
Lưu ý: Các mã loại chỉ dành cho sử dụng nội bộ. Router sẽ vẫn là loại 4, và hỗ trợ sẽ được chỉ ra trong các địa chỉ router.

#### 2) SessionCreated

Nội dung thô:

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted Y         |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +   Encrypted and authenticated data    +
  -      (see table below for length)     -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (options)          |
  +   Encrypted and authenticated data    +
  -           32 bytes                    -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
Dữ liệu không mã hóa (thẻ xác thực Poly1305 không hiển thị):

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                  Y                    |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Kích thước:

| Loại | Mã Loại | Độ dài Y | Độ dài Msg 2 | Độ dài Msg 2 Mã hóa | Độ dài Msg 2 Giải mã | Độ dài PQ CT | Độ dài tùy chọn |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 848+pad | 816 | 784 | 768 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1136+pad | 1104 | 1104 | 1088 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1616+pad | 1584 | 1584 | 1568 | 16 |
Lưu ý: Mã loại chỉ dành cho sử dụng nội bộ. Các router sẽ vẫn là loại 4, và hỗ trợ sẽ được chỉ ra trong địa chỉ router.

#### 3) SessionConfirmed

Không thay đổi

#### Hàm Dẫn xuất Khóa (KDF) (cho giai đoạn dữ liệu)

Không thay đổi

#### Địa chỉ đã xuất bản

Trong mọi trường hợp, sử dụng tên giao thức NTCP2 transport như thông thường.

Sử dụng cùng địa chỉ/cổng như non-PQ, non-firewalled. Chỉ hỗ trợ một biến thể PQ. Trong địa chỉ router, xuất bản v=2 (như thường lệ) và tham số mới pq=[3|4|5] để chỉ ra MLKEM 512/768/1024. Alice đặt MSB của khóa ephemeral (key[31] & 0x80) trong yêu cầu phiên để chỉ ra rằng đây là kết nối hybrid. Xem phần trên. Các router cũ sẽ bỏ qua tham số pq và kết nối non-pq như thường lệ.

Địa chỉ/cổng khác với non-PQ, hoặc chỉ PQ, không có tường lửa KHÔNG được hỗ trợ. Điều này sẽ không được triển khai cho đến khi NTCP2 non-PQ bị vô hiệu hóa, vài năm nữa. Khi non-PQ bị vô hiệu hóa, nhiều biến thể PQ có thể được hỗ trợ, nhưng chỉ một biến thể cho mỗi địa chỉ. Trong địa chỉ router, xuất bản v=[3|4|5] để chỉ ra MLKEM 512/768/1024. Alice không đặt MSB của ephemeral key. Các router cũ hơn sẽ kiểm tra tham số v và bỏ qua địa chỉ này vì không được hỗ trợ.

Địa chỉ bị chặn bởi tường lửa (không công bố IP): Trong địa chỉ router, công bố v=2 (như thường lệ). Không cần phải công bố tham số pq.

Alice có thể kết nối với PQ Bob sử dụng biến thể PQ mà Bob công bố, bất kể Alice có quảng cáo hỗ trợ pq trong thông tin router của mình hay không, hoặc liệu cô ấy có quảng cáo cùng biến thể đó.

#### Padding Tối đa

Trong đặc tả hiện tại, tin nhắn 1 và 2 được định nghĩa có một lượng padding "hợp lý", với phạm vi 0-31 byte được khuyến nghị và không chỉ định giá trị tối đa.

Từ API 0.9.68 (phiên bản 2.11.0), Java I2P đã triển khai tối đa 256 bytes padding cho các kết nối non-PQ, tuy nhiên điều này trước đây chưa được ghi lại. Từ API 0.9.69 (phiên bản 2.12.0), Java I2P triển khai cùng mức padding tối đa cho các kết nối non-PQ như đối với MLKEM-512. Xem bảng bên dưới.

Sử dụng kích thước thông điệp đã định nghĩa làm padding tối đa, nghĩa là padding tối đa sẽ tăng gấp đôi kích thước thông điệp cho các kết nối PQ, như sau:

| Message Max Padding | non-PQ (thru 0.9.68) | non-PQ (as of 0.9.69) | MLKEM-512 | MLKEM-768 | MLKEM-1024 |
|---------------------|----------------------|-----------------------|-----------|-----------|------------|
| Session Request  |   256   |   880   |    880   |     1264   |    1648  |
| Session Created  |   256   |   848   |    848   |     1136   |    1616  |
### SSU2

Cập nhật đặc tả SSU2 [/docs/specs/ssu2/](/docs/specs/ssu2/) như sau:

#### Định danh Noise

- "Noise_XKhfschaobfse+hs1+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfschaobfse+hs1+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"

Lưu ý rằng MLKEM-1024 KHÔNG được hỗ trợ cho SSU2, vì các khóa quá lớn để vừa trong một datagram tiêu chuẩn 1500 byte.

#### Tiêu đề dài

Header dài có kích thước 32 byte. Nó được sử dụng trước khi một phiên được tạo, cho Token Request, SessionRequest, SessionCreated và Retry. Nó cũng được sử dụng cho các thông điệp Peer Test và Hole Punch ngoài phiên.

Trong các thông điệp sau, đặt trường ver (version) trong long header thành 3 hoặc 4, để chỉ ra MLKEM-512 hoặc MLKEM-768.

- (0) Yêu cầu Phiên
- (1) Phiên Đã Tạo
- (9) Thử lại
- (10) Yêu cầu Token
- (11) Hole Punch

Trong các thông điệp sau, hãy đặt trường ver (version) trong long header thành 2 như thường lệ, ngay cả khi MLKEM-512 hoặc MLKEM-768 được hỗ trợ. Các triển khai cũng có thể đặt giá trị thành 3 hoặc 4 nếu đầu kia hỗ trợ, nhưng điều này không cần thiết. Các triển khai nên chấp nhận bất kỳ giá trị nào từ 2-4.

- (7) Kiểm tra Peer (tin nhắn ngoài phiên 5-7)

Thảo luận: Việc đặt trường version thành 3 hoặc 4 có thể không thực sự cần thiết đối với tất cả các loại message, nhưng việc làm này giúp phát hiện lỗi sớm hơn đối với các kết nối post-quantum không được hỗ trợ. Token Request và Retry (loại 9 và 10) nên có version 3/4 để đảm bảo tính nhất quán. Hole Punch messages (loại 11) có thể không yêu cầu cách xử lý này nhưng chúng ta sẽ tuân theo cùng một mẫu để đảm bảo tính đồng nhất. Peer Test messages (loại 7) là out-of-session và không chỉ ra ý định khởi tạo một session.

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

  ver :: The protocol version = 2, 3, or 4 for non-PQ, MLKEM512, MLKEM768

  id :: 1 byte, the network ID (currently 2, except for test networks)

  flag :: 1 byte, unused, set to 0 for future compatibility

  Source Connection ID :: 8 bytes, unsigned big endian integer

  Token :: 8 bytes, unsigned big endian integer

```
#### Tiêu đề ngắn

không thay đổi

#### SessionRequest (Loại 0)

Thay đổi: SSU2 hiện tại chỉ chứa dữ liệu khối trong phần ChaCha. Với ML-KEM, phần ChaCha cũng sẽ chứa khóa công khai PQ được mã hóa.

Thay đổi KDF cho Bảo vệ Chống Giả mạo: Để giải quyết các vấn đề được nêu ra trong Đề xuất 165 [Prop165]_, nhưng với một giải pháp khác, chúng tôi sửa đổi KDF cho Session Request. Điều này chỉ áp dụng cho các phiên PQ. KDF cho các phiên không phải PQ vẫn giữ nguyên.

```

// End of KDF for initial chain key (unchanged)
  // Bob static key
  // MixHash(bpk)
  h = SHA256(h || bpk);

  // Start of KDF for session request
  // NEW for PQ only
  // bhash = Bob router hash (32 bytes)
  // MixHash(bhash)
  h = SHA256(h || bhash);

  // Rest of KDF for session request, unchanged, as in SSU2 spec
  // MixHash(header)
  h = SHA256(h || header)

  ...

```
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
  |   ChaCha20 encrypted data (MLKEM)     |
  +          (length varies)              +
  |  k defined in KDF for Session Request |
  +  n = 0                                +
  |  see KDF for associated data          |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaCha20 encrypted data (payload)   |
  +          (length varies)              +
  |  k defined in KDF for Session Request |
  +  n = 0                                +
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
  |           ML-KEM encap_key            |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     Noise payload (block data)        |
  +          (length varies)              +
  |     see below for allowed blocks      |
  +----+----+----+----+----+----+----+----+
```
Kích thước, không bao gồm overhead IP:

| Loại | Mã Loại | Độ dài X | Độ dài Msg 1 | Độ dài Msg 1 Mã hóa | Độ dài Msg 1 Giải mã | Độ dài khóa PQ | Độ dài pl |
|------|-----------|-------|-----------|---------------|---------------|------------|--------|
| X25519 | 4 | 32 | 80+pl | 16+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 896+pl | 832+pl | 800+pl | 800 | pl |
| MLKEM768_X25519 | 6 | 32 | 1280+pl | 1216+pl | 1184+pl | 1184 | pl |
| MLKEM1024_X25519 | 7 | n/a | quá lớn | | | | |
Lưu ý: Mã loại chỉ dành cho sử dụng nội bộ. Các router sẽ vẫn là loại 4, và hỗ trợ sẽ được chỉ ra trong địa chỉ router.

MTU tối thiểu cho MLKEM768_X25519: 1318 cho IPv4 và 1338 cho IPv6. Xem bên dưới.

#### SessionCreated (Loại 1)

Thay đổi: SSU2 hiện tại chỉ chứa dữ liệu khối trong phần ChaCha. Với ML-KEM, phần ChaCha cũng sẽ chứa public key PQ được mã hóa.

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
  |   ChaCha20 data (MLKEM)               |
  +   Encrypted and authenticated data    +
  |  length varies                        |
  +  k defined in KDF for Session Created +
  |  n = 0; see KDF for associated data   |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaCha20 data (payload)             |
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


```
Dữ liệu không mã hóa (không hiển thị thẻ xác thực Poly1305):

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
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     Noise payload (block data)        |
  +          (length varies)              +
  |      see below for allowed blocks     |
  +----+----+----+----+----+----+----+----+
```
Kích thước, không bao gồm overhead IP:

| Loại | Mã Loại | Độ dài Y | Độ dài Msg 2 | Độ dài Msg 2 Mã hóa | Độ dài Msg 2 Giải mã | Độ dài PQ CT | Độ dài pl |
|------|-----------|-------|-----------|---------------|---------------|-----------|--------|
| X25519 | 4 | 32 | 80+pl | 16+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 864+pl | 800+pl | 768+pl | 768 | pl |
| MLKEM768_X25519 | 6 | 32 | 1184+pl | 1118+pl | 1088+pl | 1088 | pl |
| MLKEM1024_X25519 | 7 | n/a | quá lớn | | | | |
Lưu ý: Mã loại chỉ dành cho sử dụng nội bộ. Các router sẽ vẫn là loại 4, và hỗ trợ sẽ được chỉ ra trong các địa chỉ router.

MTU tối thiểu cho MLKEM768_X25519: 1318 cho IPv4 và 1338 cho IPv6. Xem bên dưới.

#### SessionConfirmed (Loại 2)

không thay đổi

#### KDF cho giai đoạn dữ liệu

không thay đổi

#### Relay và Kiểm Tra Peer

Các khối sau đây chứa các trường phiên bản. Chúng sẽ giữ nguyên phiên bản 2 (để tương thích với Bob không hỗ trợ PQ), và sẽ không thay đổi thành phiên bản 3/4 cho PQ.

- Relay Request
- Relay Response
- Relay Intro
- Peer Test

Chữ ký PQ: Các khối Relay, khối Peer Test và thông điệp Peer Test đều chứa chữ ký. Thật không may, chữ ký PQ lớn hơn MTU. Hiện tại không có cơ chế nào để phân mảnh các khối Relay hoặc Peer Test hoặc thông điệp qua nhiều gói UDP. Giao thức phải được mở rộng để hỗ trợ phân mảnh. Điều này sẽ được thực hiện trong một đề xuất riêng biệt sẽ được xác định sau. Cho đến khi hoàn thành, Relay và Peer Test sẽ không được hỗ trợ.

#### Địa chỉ đã xuất bản

Trong tất cả các trường hợp, sử dụng tên transport SSU2 như thông thường. MLKEM-1024 không được hỗ trợ.

Sử dụng cùng địa chỉ/cổng như non-PQ, non-firewalled. Một hoặc cả hai biến thể PQ đều được hỗ trợ. Trong địa chỉ router, xuất bản v=2 (như thường lệ) và tham số mới pq=[3|4|3,4|4,3] để chỉ ra MLKEM 512/768/cả hai. Các router có MTU nhỏ hơn mức tối thiểu được chỉ định bên dưới không được xuất bản tham số "pq" chứa "4". Xuất bản 4,3 để chỉ ra sự ưu tiên cho MLKEM-768 hoặc 3,4 để chỉ ra sự ưu tiên cho MLKEM-512. Phiên bản thực tế do người khởi tạo quyết định, và sự ưu tiên có thể không được tuân thủ. Các router có MTU nhỏ hơn mức tối thiểu được chỉ định bên dưới không được kết nối sử dụng MLKEM768. Các router cũ sẽ bỏ qua tham số pq và kết nối non-pq như thường lệ.

Địa chỉ/cổng khác với non-PQ, hoặc chỉ PQ, không bị tường lửa chặn KHÔNG được hỗ trợ. Điều này sẽ không được triển khai cho đến khi non-PQ SSU2 bị vô hiệu hóa, vài năm nữa. Khi non-PQ bị vô hiệu hóa, một hoặc cả hai biến thể PQ đều được hỗ trợ. Trong địa chỉ router, xuất bản v=[3|4|3,4|4,3] để chỉ ra MLKEM 512/768/cả hai. Các router cũ sẽ kiểm tra tham số v và bỏ qua địa chỉ này vì không được hỗ trợ.

Địa chỉ firewalled (không công bố IP): Trong địa chỉ router, công bố v=2 (như thường lệ). Tham số pq BẮT BUỘC phải được công bố trong các địa chỉ firewalled, để hỗ trợ relay.

Alice có thể kết nối đến một PQ Bob bằng cách sử dụng biến thể PQ mà Bob công bố, bất kể Alice có quảng cáo hỗ trợ pq trong router info của mình hay không, hoặc liệu cô ấy có quảng cáo cùng biến thể đó không.

#### MTU

Hãy thận trọng không vượt quá MTU với MLKEM768. MTU tối thiểu cho MLKEM768_X25519 là 1318 đối với IPv4 và 1338 đối với IPv6 (giả định payload tối thiểu 10 byte với một khối DateTime và Padding hoặc RelayTagRequest). MTU tối thiểu cho SSU2 nói chung là 1280, vì vậy không phải tất cả peer đều có thể sử dụng MLKEM768. Không được publish hoặc sử dụng MLKEM768 nếu MTU thực tế nhỏ hơn mức tối thiểu, dù là cục bộ hay như được quảng cáo bởi peer. Hãy cẩn thận không bao gồm kích thước padding sao cho message 1 hoặc 2 sẽ vượt quá MTU cục bộ hoặc từ xa.

#### Vấn đề

Chúng ta có thể sử dụng trường version nội bộ và dùng 3 cho MLKEM512 và 4 cho MLKEM768.

Đối với thông điệp 1 và 2, MLKEM768 sẽ làm tăng kích thước gói tin vượt quá MTU tối thiểu 1280. Có thể sẽ chỉ không hỗ trợ nó cho kết nối đó nếu MTU quá thấp.

Đối với tin nhắn 1 và 2, MLKEM1024 sẽ làm tăng kích thước gói tin vượt quá MTU tối đa 1500. Điều này sẽ yêu cầu phân mảnh tin nhắn 1 và 2, và đó sẽ là một phức tạp lớn. Có thể sẽ không làm điều này.

Relay và Peer Test: Xem phần trên

### Streaming

TODO: Có cách nào hiệu quả hơn để định nghĩa signing/verification nhằm tránh sao chép signature không?

### Tệp SU3

CẦN LÀM

[IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/) mục 8.1 không cho phép HashML-DSA trong chứng chỉ X.509 và không gán OID cho HashML-DSA, do độ phức tạp trong triển khai và bảo mật giảm.

Đối với chữ ký chỉ dùng PQ của các file SU3, hãy sử dụng các OID được định nghĩa trong [bản thảo IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/) của các biến thể non-prehash cho các chứng chỉ. Chúng tôi không định nghĩa chữ ký kết hợp của các file SU3, vì chúng tôi có thể phải hash các file hai lần (mặc dù HashML-DSA và X2559 sử dụng cùng hàm hash SHA512). Ngoài ra, việc nối hai khóa và chữ ký trong một chứng chỉ X.509 sẽ hoàn toàn không chuẩn.

Lưu ý rằng chúng tôi không cho phép ký Ed25519 đối với các tệp SU3, và mặc dù chúng tôi đã định nghĩa việc ký Ed25519ph, nhưng chúng tôi chưa bao giờ thống nhất về một OID cho nó, hoặc sử dụng nó.

Các loại chữ ký thông thường không được phép cho tệp SU3; sử dụng các biến thể ph (prehash).

### Các Thông Số Khác

Kích thước Destination tối đa mới sẽ là 2599 (3468 trong base 64).

Cập nhật các tài liệu khác đưa ra hướng dẫn về kích thước Destination, bao gồm:

- SAMv3
- Bittorrent
- Hướng dẫn cho nhà phát triển
- Đặt tên / sổ địa chỉ / jump server
- Tài liệu khác

## Phân Tích Chi Phí Bổ Sung

### Trao đổi khóa

Tăng kích thước (byte):

| Loại | Pubkey (Msg 1) | Cipertext (Msg 2) |
|------|----------------|-------------------|
| MLKEM512_X25519 | +816 | +784 |
| MLKEM768_X25519 | +1200 | +1104 |
| MLKEM1024_X25519 | +1584 | +1584 |
Tốc độ:

Tốc độ theo báo cáo của [Cloudflare](https://blog.cloudflare.com/pq-2024/):

| Loại | Tốc độ tương đối |
|------|----------------|
| X25519 DH/keygen | cơ sở |
| MLKEM512 | nhanh hơn 2.25x |
| MLKEM768 | nhanh hơn 1.5x |
| MLKEM1024 | 1x (như nhau) |
| XK | 4x DH (keygen + 3 DH) |
| MLKEM512_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 4.9x DH = chậm hơn 22% |
| MLKEM768_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 5.3x DH = chậm hơn 32% |
| MLKEM1024_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 6x DH = chậm hơn 50% |
Kết quả thử nghiệm sơ bộ trong Java:

| Loại | DH/encaps tương đối | DH/decaps | keygen |
|------|-------------------|-----------|--------|
| X25519 | cơ sở | cơ sở | cơ sở |
| MLKEM512 | nhanh hơn 29 lần | nhanh hơn 22 lần | nhanh hơn 17 lần |
| MLKEM768 | nhanh hơn 17 lần | nhanh hơn 14 lần | nhanh hơn 9 lần |
| MLKEM1024 | nhanh hơn 12 lần | nhanh hơn 10 lần | nhanh hơn 6 lần |
### Chữ ký

Kích thước:

Kích thước thông thường hoặc mức tăng kích thước của key, sig, RIdent, Dest (Ed25519 được bao gồm để tham khảo) giả định loại mã hóa X25519 cho RIs. Kích thước được thêm vào cho Router Info, LeaseSet, datagram có thể trả lời, và từng gói streaming (SYN và SYN ACK) được liệt kê. Destinations và Leasets hiện tại chứa padding lặp lại và có thể nén trong quá trình truyền. Các loại mới không chứa padding và sẽ không thể nén được, dẫn đến mức tăng kích thước cao hơn nhiều trong quá trình truyền. Xem phần thiết kế ở trên.

| Loại | Pubkey | Sig | Key+Sig | RIdent | Dest | RInfo | LS/Streaming/Datagram (mỗi msg) |
|------|--------|-----|---------|--------|------|-------|----------------------------------|
| EdDSA_SHA512_Ed25519 | 32 | 64 | 96 | 391 | 391 | baseline | baseline |
| MLDSA44 | 1312 | 2420 | 3732 | 1351 | 1319 | +3316 | +3284 |
| MLDSA65 | 1952 | 3309 | 5261 | 1991 | 1959 | +5668 | +5636 |
| MLDSA87 | 2592 | 4627 | 7219 | 2631 | 2599 | +7072 | +7040 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 1344 | 2484 | 3828 | 1383 | 1351 | +3412 | +3380 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 1984 | 3373 | 5357 | 2023 | 1991 | +5668 | +5636 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 2624 | 4691 | 7315 | 2663 | 2631 | +7488 | +7456 |
Tốc độ:

Tốc độ như được báo cáo bởi [Cloudflare](https://blog.cloudflare.com/pq-2024/):

| Loại | Dấu hiệu tốc độ tương đối | xác minh |
|------|---------------------|--------|
| EdDSA_SHA512_Ed25519 | cơ sở | cơ sở |
| MLDSA44 | chậm hơn 5 lần | nhanh hơn 2 lần |
| MLDSA65 | ??? | ??? |
| MLDSA87 | ??? | ??? |
Kết quả kiểm tra sơ bộ trong Java:

| Loại | Tốc độ tương đối ký | xác minh | tạo khóa |
|------|---------------------|--------|--------|
| EdDSA_SHA512_Ed25519 | cơ sở | cơ sở | cơ sở |
| MLDSA44 | chậm hơn 4.6x | nhanh hơn 1.7x | nhanh hơn 2.6x |
| MLDSA65 | chậm hơn 8.1x | tương đương | nhanh hơn 1.5x |
| MLDSA87 | chậm hơn 11.1x | chậm hơn 1.5x | tương đương |
## Phân tích Bảo mật

Các danh mục bảo mật NIST được tóm tắt trong [bài thuyết trình NIST](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) trang 10. Tiêu chí sơ bộ: Danh mục bảo mật NIST tối thiểu của chúng ta nên là 2 cho các giao thức hybrid và 3 cho PQ-only.

| Danh mục | Bảo mật tương đương |
|----------|--------------|
| 1 | AES128 |
| 2 | SHA256 |
| 3 | AES192 |
| 4 | SHA384 |
| 5 | AES256 |
### Bắt tay

Đây là tất cả các giao thức kết hợp. Các triển khai nên ưu tiên MLKEM768; MLKEM512 không đủ an toàn.

Các danh mục bảo mật NIST [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf):

| Thuật toán | Danh mục Bảo mật |
|------------|------------------|
| MLKEM512 | 1 |
| MLKEM768 | 3 |
| MLKEM1024 | 5 |
### Chữ ký

Đề xuất này định nghĩa cả loại chữ ký lai và chỉ PQ. MLDSA44 lai được ưa thích hơn MLDSA65 chỉ PQ. Kích thước khóa và chữ ký cho MLDSA65 và MLDSA87 có thể quá lớn đối với chúng ta, ít nhất là lúc đầu.

Các danh mục bảo mật NIST [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf):

| Thuật toán | Loại Bảo mật |
|-----------|--------------|
| MLDSA44 | 2 |
| MLKEM67 | 3 |
| MLKEM87 | 5 |
## Tùy chọn loại

Mặc dù chúng tôi sẽ định nghĩa và triển khai 3 loại crypto và 9 loại chữ ký, chúng tôi dự định đo lường hiệu suất trong quá trình phát triển và phân tích thêm về ảnh hưởng của việc tăng kích thước cấu trúc. Chúng tôi cũng sẽ tiếp tục nghiên cứu và theo dõi các phát triển trong các dự án và giao thức khác.

Sau một năm hoặc hơn phát triển, chúng tôi sẽ cố gắng quyết định một loại ưa thích hoặc mặc định cho mỗi trường hợp sử dụng. Việc lựa chọn sẽ yêu cầu đánh đổi giữa băng thông, CPU và mức độ bảo mật ước tính. Không phải tất cả các loại đều phù hợp hoặc được phép cho mọi trường hợp sử dụng.

Các tùy chọn sơ bộ như sau, có thể thay đổi:

Mã hóa: MLKEM768_X25519

Signatures: MLDSA44_EdDSA_SHA512_Ed25519

Các hạn chế sơ bộ như sau, có thể thay đổi:

Mã hóa: MLKEM1024_X25519 không được phép cho SSU2

Chữ ký: MLDSA87 và biến thể lai có thể quá lớn; MLDSA65 và biến thể lai có thể quá lớn

## Ghi chú triển khai

### Hỗ trợ Thư viện

Các thư viện Bouncycastle, BoringSSL và WolfSSL hiện đã hỗ trợ MLKEM và MLDSA. Hỗ trợ OpenSSL sẽ có trong bản phát hành 3.5 vào ngày 8 tháng 4 năm 2025 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

Thư viện Noise từ southernstorm.com được Java I2P điều chỉnh có chứa hỗ trợ sơ bộ cho hybrid handshakes, nhưng chúng tôi đã loại bỏ nó vì không sử dụng; chúng tôi sẽ phải thêm lại và cập nhật để phù hợp với [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf).

### Các Biến Thể Ký

Chúng tôi sẽ sử dụng biến thể ký "hedged" hoặc ngẫu nhiên hóa, không phải biến thể "deterministic", như được định nghĩa trong [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) phần 3.4. Điều này đảm bảo rằng mỗi chữ ký đều khác nhau, ngay cả khi ký trên cùng một dữ liệu, và cung cấp thêm bảo vệ chống lại các cuộc tấn công side-channel. Mặc dù [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) quy định rằng biến thể "hedged" là mặc định, điều này có thể đúng hoặc không đúng trong các thư viện khác nhau. Người triển khai phải đảm bảo rằng biến thể "hedged" được sử dụng để ký.

Chúng ta sử dụng quy trình ký bình thường (được gọi là Pure ML-DSA Signature Generation) mã hóa thông điệp nội bộ dưới dạng 0x00 || len(ctx) || ctx || message, trong đó ctx là một giá trị tùy chọn có kích thước 0x00..0xFF. Chúng ta không sử dụng bất kỳ ngữ cảnh tùy chọn nào. len(ctx) == 0. Quy trình này được định nghĩa trong [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) Thuật toán 2 bước 10 và Thuật toán 3 bước 5. Lưu ý rằng một số test vector đã công bố có thể yêu cầu thiết lập một chế độ mà thông điệp không được mã hóa.

### Độ tin cậy

Việc tăng kích thước sẽ dẫn đến phân mảnh tunnel nhiều hơn đáng kể cho các lưu trữ NetDB, bắt tay streaming và các thông điệp khác. Hãy kiểm tra những thay đổi về hiệu suất và độ tin cậy.

### Kích thước Cấu trúc

Tìm và kiểm tra bất kỳ mã nào giới hạn kích thước byte của router infos và leasesets.

### NetDB

Xem xét và có thể giảm số lượng LS/RI tối đa được lưu trữ trong RAM hoặc trên ổ đĩa, để hạn chế việc tăng dung lượng lưu trữ. Tăng yêu cầu băng thông tối thiểu cho floodfill?

### Ratchet

#### Tunnel Chia Sẻ

Việc tự động phân loại/phát hiện nhiều giao thức trên cùng một tunnel có thể thực hiện được dựa trên kiểm tra độ dài của message 1 (New Session Message). Sử dụng MLKEM512_X25519 làm ví dụ, độ dài message 1 lớn hơn 816 byte so với giao thức ratchet hiện tại, và kích thước tối thiểu của message 1 (chỉ bao gồm payload DateTime) là 919 byte. Hầu hết kích thước message 1 với ratchet hiện tại có payload nhỏ hơn 816 byte, vì vậy chúng có thể được phân loại là ratchet không lai. Các message lớn có thể là POSTs và tương đối hiếm.

Vậy chiến lược được khuyến nghị là:

- Nếu tin nhắn 1 nhỏ hơn 919 byte, đó là giao thức ratchet hiện tại.
- Nếu tin nhắn 1 lớn hơn hoặc bằng 919 byte, có thể là MLKEM512_X25519.
  Thử MLKEM512_X25519 trước, và nếu thất bại, hãy thử giao thức ratchet hiện tại.

Điều này sẽ cho phép chúng ta hỗ trợ hiệu quả cả ratchet tiêu chuẩn và hybrid ratchet trên cùng một destination, giống như trước đây chúng ta đã hỗ trợ ElGamal và ratchet trên cùng một destination. Do đó, chúng ta có thể di chuyển sang giao thức MLKEM hybrid nhanh hơn nhiều so với trường hợp không thể hỗ trợ dual-protocols cho cùng một destination, vì chúng ta có thể thêm hỗ trợ MLKEM vào các destination hiện có.

Các kết hợp được hỗ trợ bắt buộc là:

- X25519 + MLKEM512
- X25519 + MLKEM768
- X25519 + MLKEM1024

Các kết hợp sau đây có thể phức tạp và KHÔNG bắt buộc phải được hỗ trợ, nhưng có thể được hỗ trợ tùy thuộc vào cách triển khai:

- Nhiều hơn một MLKEM
- ElG + một hoặc nhiều MLKEM
- X25519 + một hoặc nhiều MLKEM
- ElG + X25519 + một hoặc nhiều MLKEM

Chúng ta có thể không cố gắng hỗ trợ nhiều thuật toán MLKEM (ví dụ, MLKEM512_X25519 và MLKEM_768_X25519) trên cùng một destination. Chỉ chọn một; tuy nhiên, điều đó phụ thuộc vào việc chúng ta chọn một biến thể MLKEM ưa thích, để các HTTP client tunnel có thể sử dụng. Phụ thuộc vào triển khai.

Chúng tôi CÓ THỂ cố gắng hỗ trợ ba thuật toán (ví dụ X25519, MLKEM512_X25519, và MLKEM769_X25519) trên cùng một destination. Việc phân loại và chiến lược thử lại có thể quá phức tạp. Cấu hình và giao diện người dùng cấu hình có thể quá phức tạp. Phụ thuộc vào implementation.

Chúng tôi có thể sẽ KHÔNG cố gắng hỗ trợ các thuật toán ElGamal và hybrid trên cùng một đích đến. ElGamal đã lỗi thời, và ElGamal + hybrid chỉ (không có X25519) không có nhiều ý nghĩa. Ngoài ra, cả ElGamal và Hybrid New Session Messages đều lớn, vì vậy các chiến lược phân loại thường phải thử cả hai quá trình giải mã, điều này sẽ không hiệu quả. Phụ thuộc vào việc triển khai.

Các client có thể sử dụng cùng một hoặc các khóa tĩnh X25519 khác nhau cho giao thức X25519 và giao thức hybrid trên cùng các tunnel, tùy thuộc vào cách triển khai.

#### Bảo mật tiến về phía trước

Đặc tả ECIES cho phép Garlic Messages trong payload New Session Message, điều này cho phép giao hàng 0-RTT của gói streaming ban đầu, thường là HTTP GET, cùng với leaseset của client. Tuy nhiên, payload New Session Message không có tính bảo mật chuyển tiếp. Vì đề xuất này nhấn mạnh việc tăng cường bảo mật chuyển tiếp cho ratchet, các triển khai có thể hoặc nên hoãn việc bao gồm payload streaming, hoặc toàn bộ thông điệp streaming, cho đến Existing Session Message đầu tiên. Điều này sẽ phải đánh đổi với việc giao hàng 0-RTT. Các chiến lược cũng có thể phụ thuộc vào loại traffic hoặc loại tunnel, hoặc phụ thuộc vào GET so với POST, chẳng hạn. Tùy thuộc vào triển khai.

#### Kích Thước Phiên Mới

MLKEM, MLDSA, hoặc cả hai trên cùng một đích đến, sẽ làm tăng đáng kể kích thước của New Session Message, như đã mô tả ở trên. Điều này có thể giảm đáng kể độ tin cậy của việc gửi New Session Message qua các tunnel, nơi chúng phải được phân mảnh thành nhiều tunnel message 1024 byte. Tỷ lệ gửi thành công tỷ lệ thuận với số mũ của số lượng mảnh. Các implementation có thể sử dụng nhiều chiến lược khác nhau để giới hạn kích thước của message, với cái giá là không thể gửi 0-RTT. Phụ thuộc vào implementation.

### NTCP2

Chúng tôi thiết lập MSB của ephemeral key (key[31] & 0x80) trong session request để chỉ ra rằng đây là một kết nối hybrid. Điều này cho phép chúng tôi chạy cả NTCP tiêu chuẩn và NTCP hybrid trên cùng một cổng. Chỉ một biến thể hybrid sẽ được hỗ trợ và được quảng cáo trong địa chỉ router. Ví dụ, v=2,3 hoặc v=2,4 hoặc v=2,5.

#### Che giấu

Với vai trò Alice, đối với kết nối PQ, trước khi obfuscation, đặt X[31] |= 0x80. Điều này làm cho X trở thành một public key X25519 không hợp lệ. Sau obfuscation, AES-CBC sẽ ngẫu nhiên hóa nó. MSB của X sẽ là ngẫu nhiên sau obfuscation.

Với vai trò Bob, kiểm tra xem (X[31] & 0x80) != 0 sau khi bỏ làm mờ. Nếu đúng, đó là kết nối PQ.

Phiên bản router tối thiểu yêu cầu cho NTCP2-PQ là TBD.

Lưu ý: Mã loại chỉ dành cho sử dụng nội bộ. Các router sẽ vẫn giữ loại 4, và hỗ trợ sẽ được chỉ ra trong địa chỉ router.

### SSU2

Chúng tôi sử dụng trường version trong long header và đặt nó thành 3 cho MLKEM512 và 4 cho MLKEM768. v=2,3,4 trong địa chỉ sẽ là đủ.

Kiểm tra và xác minh rằng SSU2 có thể xử lý RI được ký bằng MLDSA bị phân mảnh qua nhiều gói tin (6-8?).

Lưu ý: Các mã loại chỉ dành cho sử dụng nội bộ. Các router sẽ vẫn là loại 4, và việc hỗ trợ sẽ được chỉ ra trong các địa chỉ router.

## Tương thích Router

### Tên Transport

Trong tất cả các trường hợp, sử dụng tên giao thức truyền tải NTCP2 và SSU2 như thông thường.

### Các Loại Mã Hóa Router

Chúng ta có một số lựa chọn thay thế để xem xét:

#### Router Loại 5/6/7

Không được khuyến nghị. Chỉ sử dụng các transport mới được liệt kê ở trên phù hợp với loại router. Các router cũ không thể kết nối, xây dựng tunnel qua, hoặc gửi tin nhắn netDb tới. Sẽ cần vài chu kỳ phát hành để debug và đảm bảo hỗ trợ trước khi bật mặc định. Có thể kéo dài việc triển khai thêm một năm hoặc hơn so với các phương án thay thế bên dưới.

#### Router Loại 4

Được khuyến nghị. Vì PQ không ảnh hưởng đến khóa tĩnh X25519 hoặc các giao thức bắt tay N, chúng ta có thể để các router ở loại 4, và chỉ quảng bá các phương thức truyền tải mới. Các router cũ vẫn có thể kết nối, xây dựng tunnel qua, hoặc gửi tin nhắn netDb đến.

#### Khuyến nghị

MLKEM-768 được khuyến nghị cho Ratchet, NTCP2, và SSU2, là sự cân bằng tốt nhất giữa tính bảo mật và độ dài khóa.

### Các Loại Chữ Ký Router

#### Router Loại 12-17

Các router cũ hơn xác minh RIs và do đó không thể kết nối, xây dựng tunnel qua, hoặc gửi tin nhắn netDb tới. Sẽ cần nhiều chu kỳ phát hành để gỡ lỗi và đảm bảo hỗ trợ trước khi bật theo mặc định. Sẽ gặp các vấn đề tương tự như việc triển khai enc. type 5/6/7; có thể kéo dài việc triển khai thêm một năm hoặc hơn so với phương án thay thế triển khai enc. type 4 được liệt kê ở trên.

Không có lựa chọn thay thế.

### Các kiểu mã hóa LS

#### Khóa LS Loại 5-7

Những khóa này có thể có mặt trong LS với các khóa X25519 loại 4 cũ hơn. Các router cũ sẽ bỏ qua những khóa không xác định.

Các destination có thể hỗ trợ nhiều loại khóa, nhưng chỉ bằng cách thực hiện giải mã thử nghiệm message 1 với từng khóa. Chi phí overhead có thể được giảm thiểu bằng cách duy trì số lần đếm giải mã thành công cho mỗi khóa, và thử khóa được sử dụng nhiều nhất trước tiên. Java I2P sử dụng chiến lược này cho ElGamal+X25519 trên cùng một destination.

### Loại Chữ ký Đích

#### Type 12-17 Dests

Các router xác minh chữ ký leaseSet và do đó không thể kết nối, hoặc nhận leaseSet cho các đích loại 12-17. Sẽ mất vài chu kỳ phát hành để debug và đảm bảo hỗ trợ trước khi kích hoạt theo mặc định.

Không có lựa chọn thay thế.

## Ưu tiên và Triển khai

Dữ liệu có giá trị nhất là lưu lượng end-to-end, được mã hóa bằng ratchet. Đối với người quan sát bên ngoài giữa các hop của tunnel, dữ liệu này được mã hóa thêm hai lần nữa, với mã hóa tunnel và mã hóa transport. Đối với người quan sát bên ngoài giữa OBEP và IBGW, dữ liệu chỉ được mã hóa thêm một lần nữa, với mã hóa transport. Đối với người tham gia OBEP hoặc IBGW, ratchet là mã hóa duy nhất. Tuy nhiên, vì các tunnel là một chiều, việc bắt được cả hai thông điệp trong quá trình bắt tay ratchet sẽ đòi hỏi sự thông đồng giữa các router, trừ khi các tunnel được xây dựng với OBEP và IBGW trên cùng một router.

Mô hình đe dọa PQ đáng lo ngại nhất hiện tại là việc lưu trữ lưu lượng ngày hôm nay để giải mã sau nhiều năm nữa (bảo mật chuyển tiếp). Một phương pháp kết hợp sẽ bảo vệ điều đó.

Mô hình đe dọa PQ về việc phá vỡ các khóa xác thực trong một khoảng thời gian hợp lý (chẳng hạn vài tháng) và sau đó mạo danh xác thực hoặc giải mã gần như thời gian thực, còn xa hơn nhiều? Và đó là lúc chúng ta muốn chuyển sang các khóa tĩnh PQC.

Vậy, mô hình đe dọa PQ sớm nhất là OBEP/IBGW lưu trữ lưu lượng để giải mã sau này. Chúng ta nên triển khai hybrid ratchet trước.

Ratchet có độ ưu tiên cao nhất. Transports là tiếp theo. Signatures có độ ưu tiên thấp nhất.

Việc triển khai chữ ký cũng sẽ muộn hơn một năm hoặc hơn so với việc triển khai mã hóa, vì không thể có khả năng tương thích ngược. Ngoài ra, việc áp dụng MLDSA trong ngành sẽ được tiêu chuẩn hóa bởi CA/Browser Forum và các Certificate Authorities. Các CA cần hỗ trợ mô-đun bảo mật phần cứng (HSM) trước, điều này hiện tại chưa có sẵn [CA/Browser Forum](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/). Chúng tôi kỳ vọng CA/Browser Forum sẽ thúc đẩy các quyết định về lựa chọn tham số cụ thể, bao gồm việc có hỗ trợ hay yêu cầu composite signatures [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/).

| Cột mốc | Mục tiêu |
|---------|----------|
| Ratchet beta | Cuối 2025 |
| Chọn loại mã hóa tốt nhất | Đầu 2026 |
| NTCP2 beta | Đầu 2026 |
| SSU2 beta | Giữa 2026 |
| Ratchet production | Giữa 2026 |
| Ratchet mặc định | Cuối 2026 |
| Signature beta | Cuối 2026 |
| NTCP2 production | Cuối 2026 |
| SSU2 production | Đầu 2027 |
| Chọn loại chữ ký tốt nhất | Đầu 2027 |
| NTCP2 mặc định | Đầu 2027 |
| SSU2 mặc định | Giữa 2027 |
| Signature production | Giữa 2027 |
## Di chuyển

Nếu chúng ta không thể hỗ trợ cả giao thức ratchet cũ và mới trên cùng các tunnel, việc di chuyển sẽ khó khăn hơn nhiều.

Chúng ta có thể thử từng cái một lần lượt, như đã làm với X25519, để được chứng minh.

## Vấn đề

- Lựa chọn Noise Hash - tiếp tục với SHA256 hay nâng cấp?
  SHA256 sẽ còn tốt trong 20-30 năm nữa, không bị đe dọa bởi PQ,
  Xem [bài thuyết trình NIST](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf) và [bài thuyết trình NCCOE](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf).
  Nếu SHA256 bị phá vỡ thì chúng ta có vấn đề tồi tệ hơn (netDb).
- NTCP2 cổng riêng biệt, địa chỉ router riêng biệt
- SSU2 relay / peer test
- Trường phiên bản SSU2
- Phiên bản địa chỉ router SSU2

## Tài liệu tham khảo

* [CABFORUM](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/)
* [Choosing-Hash](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3)
* [CLOUDFLARE](https://blog.cloudflare.com/pq-2024/)
* [COMMON](/docs/specs/common-structures/)
* [COMPOSITE-SIGS](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)
* [ECIES](/docs/specs/ecies/)
* [FORUM](http://zzz.i2p/topics/3294)
* [FIPS202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
* [FIPS203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
* [FIPS204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
* [FIPS205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf)
* [MLDSA-OIDS](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/)
* [NIST-PQ](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)
* [NIST-PQ-UPDATE](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf)
* [NIST-PQ-END](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf)
* [NIST-VECTORS](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values)
* [Noise](https://noiseprotocol.org/noise.html)
* [Noise-Hybrid](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf)
* [NSA-PQ](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF)
* [NTCP2](/docs/specs/ntcp2/)
* [OPENSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/)
* [Prop165](/docs/proposals/165/)
* [PQ-WIREGUARD](https://eprint.iacr.org/2020/379.pdf)
* [RFC-2104](https://tools.ietf.org/html/rfc2104)
* [Rosenpass](https://rosenpass.eu/)
* [Rosenpass-Whitepaper](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf)
* [SSH-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/)
* [SSU2](/docs/specs/ssu2/)
* [TLS-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/)
