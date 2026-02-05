---
title: "Đặc tả LeaseSet Mã hóa"
description: "Làm mờ, mã hóa và giải mã các leaseSet được mã hóa"
slug: "encryptedleaseset"
category: "Giao thức"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Tổng quan

Tài liệu này chỉ định việc làm mù (blinding), mã hóa và giải mã của encrypted leasesets. Để biết cấu trúc của encrypted leaseset, xem [đặc tả cấu trúc chung](/docs/specs/common-structures). Để hiểu về bối cảnh của encrypted leasesets, xem [đề xuất 123](/proposals/123-new-netdb-entries). Để biết cách sử dụng trong netDb, xem tài liệu netdb.

### Định nghĩa

Chúng tôi định nghĩa các hàm sau tương ứng với các khối xây dựng mật mã được sử dụng cho LS2 được mã hóa:

**CSRNG(n)** : đầu ra n-byte từ một bộ tạo số ngẫu nhiên an toàn mật mã học.

Ngoài yêu cầu CSRNG phải an toàn về mặt mật mã học (và do đó phù hợp để tạo key material), nó PHẢI an toàn khi một số đầu ra n-byte được sử dụng làm key material ngay cả khi các chuỗi byte đứng ngay trước và sau nó bị lộ trên mạng (chẳng hạn như trong salt, hoặc encrypted padding). Các triển khai dựa vào nguồn có thể không đáng tin cậy nên hash bất kỳ đầu ra nào sẽ bị lộ trên mạng [PRNG-REFS](http://projectbullrun.org/dual-ec/ext-rand.html).

**H(p, d)** : Hàm băm SHA-256 nhận vào một chuỗi cá nhân hóa p và dữ liệu d, và tạo ra đầu ra có độ dài 32 byte.

Sử dụng SHA-256 như sau:

```
H(p, d) := SHA-256(p || d)
```
**STREAM** : Mã hóa dòng ChaCha20 như được quy định trong [RFC-7539-S2.4](https://tools.ietf.org/html/rfc7539#section-2.4), với bộ đếm ban đầu được đặt thành 1. S_KEY_LEN = 32 và S_IV_LEN = 12.

- **ENCRYPT(k, iv, plaintext)** : Mã hóa plaintext bằng cipher key k, và nonce iv PHẢI là duy nhất cho key k. Trả về một ciphertext có cùng kích thước với plaintext. Toàn bộ ciphertext phải không thể phân biệt được với dữ liệu ngẫu nhiên nếu key được bảo mật.

- **DECRYPT(k, iv, ciphertext)** : Giải mã ciphertext bằng khóa mật mã k và nonce iv. Trả về plaintext.

**SIG** : Lược đồ chữ ký Red25519 (tương ứng với SigType 11) với key blinding. Nó có các chức năng sau:

- **DERIVE_PUBLIC(privkey)** : Trả về khóa công khai tương ứng với khóa riêng tư đã cho.

- **SIGN(privkey, m)** : Trả về một chữ ký bằng khóa riêng privkey trên thông điệp m đã cho.

- **VERIFY(pubkey, m, sig)** : Xác minh chữ ký sig với khóa công khai pubkey và thông điệp m. Trả về true nếu chữ ký hợp lệ, ngược lại trả về false.

Nó cũng phải hỗ trợ các thao tác làm mù khóa sau:

- **GENERATE_ALPHA(data, secret)** : Tạo alpha cho những ai biết dữ liệu và một secret tùy chọn. Kết quả phải được phân phối giống hệt như các private key.

- **BLIND_PRIVKEY(privkey, alpha)** : Làm mù một khóa riêng tư, sử dụng một bí mật alpha.

- **BLIND_PUBKEY(pubkey, alpha)** : Làm mù một khóa công khai, sử dụng một giá trị bí mật alpha. Với một cặp khóa cho trước (privkey, pubkey), mối quan hệ sau đây được duy trì:

```
BLIND_PUBKEY(pubkey, alpha) ==
DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))
```
**DH** : Hệ thống thỏa thuận khóa công khai X25519. Khóa riêng tư 32 byte, khóa công khai 32 byte, tạo ra đầu ra 32 byte. Nó có các chức năng sau:

- **GENERATE_PRIVATE()** : Tạo một private key mới.

- **DERIVE_PUBLIC(privkey)** : Trả về khóa công khai tương ứng với khóa riêng tư đã cho.

- **DH(privkey, pubkey)** : Tạo ra một bí mật chia sẻ từ khóa riêng và khóa công khai đã cho.

**HKDF(salt, ikm, info, n)** : Một hàm dẫn xuất khóa mật mã nhận đầu vào là tài liệu khóa ikm (cần có entropy tốt nhưng không bắt buộc phải là chuỗi ngẫu nhiên đồng đều), một salt có độ dài 32 byte, và một giá trị 'info' cụ thể theo ngữ cảnh, sau đó tạo ra đầu ra n byte phù hợp để sử dụng làm tài liệu khóa.

Sử dụng HKDF như được chỉ định trong [RFC-5869](https://tools.ietf.org/html/rfc5869), sử dụng hàm băm HMAC SHA-256 như được chỉ định trong [RFC-2104](https://tools.ietf.org/html/rfc2104). Điều này có nghĩa là SALT_LEN tối đa là 32 byte.

### Định dạng

Định dạng LS2 được mã hóa bao gồm ba lớp lồng nhau:

- Một lớp ngoài chứa thông tin văn bản thuần cần thiết để lưu trữ và truy xuất.
- Một lớp giữa xử lý việc xác thực client.
- Một lớp trong chứa dữ liệu LS2 thực tế.

Định dạng tổng thể trông như sau:

```
Layer 0 data + Enc(layer 1 data + Enc(layer 2 data)) + Signature
```
Lưu ý rằng LS2 được mã hóa là blinded. Destination không có trong header. Vị trí lưu trữ DHT là SHA-256(sig type || blinded public key), và được luân chuyển hàng ngày.

KHÔNG sử dụng header LS2 tiêu chuẩn được chỉ định ở trên.

#### Lớp 0 (ngoài)

**Type** : 1 byte

Không thực sự nằm trong header, nhưng là một phần của dữ liệu được bao phủ bởi chữ ký. Lấy từ trường trong Database Store Message.

**Blinded Public Key Sig Type** : 2 byte, big endian

Điều này sẽ luôn là loại 11, xác định một khóa bị che mờ Red25519.

**Blinded Public Key** : Độ dài như được ngụ ý bởi loại chữ ký

**Thời gian dấu xuất bản** : 4 byte, big endian

Số giây kể từ epoch, quay vòng vào năm 2106

**Expires** : 2 byte, big endian

Độ lệch từ timestamp đã công bố tính bằng giây, tối đa 18.2 giờ

**Flags** : 2 byte

Thứ tự bit: 15 14 ... 3 2 1 0

- Bit 0: Nếu 0, không có khóa ngoại tuyến; nếu 1, có khóa ngoại tuyến
- Các bit khác: đặt thành 0 để tương thích với các sử dụng trong tương lai

**Dữ liệu khóa tạm thời** : Có mặt nếu cờ chỉ ra khóa offline

- **Expires timestamp** : 4 bytes, big endian. Giây kể từ epoch, quay vòng vào năm 2106
- **Transient sig type** : 2 bytes, big endian
- **Transient signing public key** : Độ dài như được ngụ ý bởi sig type
- **Signature** : Độ dài như được ngụ ý bởi blinded public key sig type. Trên expires timestamp, transient sig type, và transient public key. Được xác minh bằng blinded public key.

**lenOuterCiphertext** : 2 byte, big endian

**outerCiphertext** : lenOuterCiphertext bytes

Dữ liệu lớp 1 được mã hóa. Xem bên dưới để biết thuật toán tạo khóa và mã hóa.

**Signature** : Độ dài được xác định bởi loại chữ ký của khóa ký được sử dụng

Chữ ký áp dụng cho tất cả nội dung phía trên. Nếu cờ hiệu chỉ ra khóa ngoại tuyến, chữ ký sẽ được xác minh bằng khóa công khai tạm thời. Ngược lại, chữ ký sẽ được xác minh bằng khóa công khai bị che khuất.

#### Lớp 1 (giữa)

**Flags** : 1 byte

Thứ tự bit: 76543210

- Bit 0: 0 cho mọi người, 1 cho từng client, phần auth theo sau
- Bits 3-1: Sơ đồ xác thực, chỉ khi bit 0 được đặt thành 1 cho từng client, nếu không thì 000
  - 000: Xác thực client DH (hoặc không có xác thực từng client)
  - 001: Xác thực client PSK
- Bits 7-4: Không sử dụng, đặt thành 0 để tương thích trong tương lai

**Dữ liệu xác thực client DH** : Có mặt nếu bit cờ 0 được đặt thành 1 và các bit cờ 3-1 được đặt thành 000.

- **ephemeralPublicKey** : 32 bytes
- **clients** : 2 bytes, big endian. Số lượng mục authClient theo sau, mỗi mục 40 bytes
- **authClient** : Dữ liệu ủy quyền cho một client duy nhất. Xem bên dưới thuật toán ủy quyền cho từng client.
  - **clientID_i** : 8 bytes
  - **clientCookie_i** : 32 bytes

**Dữ liệu xác thực client PSK** : Có mặt nếu bit cờ 0 được đặt thành 1 và các bit cờ 3-1 được đặt thành 001.

- **authSalt** : 32 bytes
- **clients** : 2 bytes, big endian. Số lượng mục authClient theo sau, mỗi mục 40 bytes
- **authClient** : Dữ liệu ủy quyền cho một client duy nhất. Xem bên dưới thuật toán ủy quyền cho mỗi client.
  - **clientID_i** : 8 bytes
  - **clientCookie_i** : 32 bytes

**innerCiphertext** : Độ dài được suy ra từ lenOuterCiphertext (bất kỳ dữ liệu nào còn lại)

Dữ liệu mã hóa tầng 2. Xem bên dưới để biết thuật toán tạo khóa và mã hóa.

#### Lớp 2 (trong)

**Loại** : 1 byte

3 (LS2) hoặc 7 (Meta LS2)

**Data** : Dữ liệu LeaseSet2 cho loại đã cho.

Bao gồm header và chữ ký.

### Tạo Khóa Che Mờ

Chúng tôi sử dụng sơ đồ sau để làm mờ khóa (key blinding), dựa trên Ed25519 và ZCash RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf). Các chữ ký Red25519 được thực hiện trên đường cong Ed25519, sử dụng SHA-512 cho hàm băm.

Chúng tôi không sử dụng phụ lục A.2 của rend-spec-v3.txt của Tor [TOR-REND-SPEC-V3](https://spec.torproject.org/rend-spec-v3), mặc dù có các mục tiêu thiết kế tương tự, bởi vì các khóa công khai được làm mù của nó có thể nằm ngoài nhóm con có bậc nguyên tố, với những tác động bảo mật chưa rõ.

#### Mục tiêu

- Khóa công khai ký trong destination không bị che mù phải là Ed25519 (loại chữ ký 7) hoặc Red25519 (loại chữ ký 11); không hỗ trợ các loại chữ ký khác
- Nếu khóa công khai ký đang offline, khóa công khai ký tạm thời cũng phải là Ed25519
- Blinding (che mù) tính toán đơn giản
- Sử dụng các nguyên hàm mật mã hiện có
- Khóa công khai bị che mù không thể được bỏ che mù
- Khóa công khai bị che mù phải nằm trên đường cong Ed25519 và nhóm con có bậc nguyên tố
- Phải biết khóa công khai ký của destination (không yêu cầu destination đầy đủ) để suy ra khóa công khai bị che mù
- Tùy chọn cung cấp thêm một bí mật cần thiết để suy ra khóa công khai bị che mù

#### Bảo mật

Tính bảo mật của một sơ đồ blinding yêu cầu rằng phân phối của alpha phải giống với các khóa riêng tư unblinded. Tuy nhiên, khi chúng ta blind một khóa riêng tư Ed25519 (sig type 7) thành một khóa riêng tư Red25519 (sig type 11), phân phối sẽ khác nhau. Để đáp ứng các yêu cầu của zcash phần 4.1.6.1 [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf), Red25519 (sig type 11) cũng nên được sử dụng cho các khóa unblinded, để "sự kết hợp của một khóa công khai được re-randomized và (các) chữ ký dưới khóa đó không tiết lộ khóa mà từ đó nó được re-randomized." Chúng tôi cho phép type 7 đối với các destination hiện có, nhưng khuyến nghị type 11 cho các destination mới sẽ được mã hóa.

#### Định nghĩa

**B** : Điểm cơ sở Ed25519 (bộ sinh) 2^255 - 19 như trong [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)

**L** : Bậc Ed25519 2^252 + 27742317777372353535851937790883648493 như trong [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)

**DERIVE_PUBLIC(a)** : Chuyển đổi khóa riêng tư thành khóa công khai, như trong Ed25519 (nhân với G)

**alpha** : Một số ngẫu nhiên 32-byte được biết bởi những ai biết địa chỉ đích.

**GENERATE_ALPHA(destination, date, secret)** : Tạo alpha cho ngày hiện tại, dành cho những ai biết destination và secret. Kết quả phải được phân phối đồng nhất như các private key Ed25519.

**a** : Khóa riêng ký 32-byte EdDSA hoặc RedDSA không bị làm mù được sử dụng để ký destination

**A** : Khóa công khai ký EdDSA hoặc RedDSA 32-byte không bị che mù trong đích đến, = DERIVE_PUBLIC(a), như trong Ed25519

**a'** : Khóa riêng tư ký EdDSA 32-byte bị che khuất được sử dụng để ký leaseSet được mã hóa. Đây là một khóa riêng tư EdDSA hợp lệ.

**A'** : Khóa công khai ký EdDSA 32-byte được che dấu trong Destination, có thể được tạo bằng DERIVE_PUBLIC(a'), hoặc từ A và alpha. Đây là một khóa công khai EdDSA hợp lệ, trên đường cong và trên nhóm con có bậc nguyên tố.

**LEOS2IP(x)** : Đảo ngược thứ tự các byte đầu vào thành little-endian

**H\*(x)** : 32 bytes = (LEOS2IP(SHA512(x))) mod B, giống như trong Ed25519 hash-and-reduce

#### Tính toán Blinding

Một secret alpha mới và các blinded keys phải được tạo ra mỗi ngày (UTC).

Khóa alpha bí mật và các khóa được làm mù được tính toán như sau:

GENERATE_ALPHA(destination, date, secret), cho tất cả các bên:

```
// secret is optional, else zero-length
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of blinded public key A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
datestring = 8 bytes ASCII YYYYMMDD from the current date UTC
secret = UTF-8 encoded string
seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || secret, "i2pblinding1", 64)
// treat seed as a 64 byte little-endian value
alpha = seed mod L
```
BLIND_PRIVKEY(), dành cho chủ sở hữu xuất bản leaseSet:

```
alpha = GENERATE_ALPHA(destination, date, secret)
// If for a Ed25519 private key (type 7)
seed = destination's signing private key
a = left half of SHA512(seed) and clamped as usual for Ed25519
// else for a Red25519 private key (type 11)
a = destination's signing private key
// Addition using scalar arithmetic
blinded signing private key = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
blinded signing public key = A' = DERIVE_PUBLIC(a')
```
BLIND_PUBKEY(), dành cho các client truy xuất leaseset:

```
alpha = GENERATE_ALPHA(destination, date, secret)
A = destination's signing public key
// Addition using group elements (points on the curve)
blinded public key = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```
Cả hai phương pháp tính A' đều cho kết quả giống nhau, như yêu cầu.

#### Ký số

LeaseSet không bị che mù được ký bởi khóa riêng tư ký Ed25519 hoặc Red25519 không bị che mù và được xác minh bằng khóa công khai ký Ed25519 hoặc Red25519 không bị che mù (loại chữ ký 7 hoặc 11) như thông thường.

Nếu khóa công khai ký không trực tuyến, leaseset không mù sẽ được ký bởi khóa riêng ký tạm thời Ed25519 hoặc Red25519 không mù và được xác minh bằng khóa công khai ký tạm thời Ed25519 hoặc Red25519 không mù (loại chữ ký 7 hoặc 11) như thường lệ. Xem thêm các ghi chú bổ sung về khóa ngoại tuyến cho encrypted leaseset ở phía dưới.

Để ký encrypted leaseset, chúng tôi sử dụng Red25519 dựa trên RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) để ký và xác minh với các khóa được che dấu. Chữ ký Red25519 hoạt động trên đường cong Ed25519, sử dụng SHA-512 cho hàm băm.

Red25519 tương tự như Ed25519 tiêu chuẩn ngoại trừ các điểm được chỉ định bên dưới.

#### Tính toán Ký/Xác minh

Phần bên ngoài của leaseset được mã hóa sử dụng khóa và chữ ký Red25519.

Red25519 tương tự như Ed25519. Có hai điểm khác biệt:

Các khóa riêng Red25519 được tạo từ các số ngẫu nhiên và sau đó phải được rút gọn theo mod L, trong đó L được định nghĩa ở trên. Các khóa riêng Ed25519 được tạo từ các số ngẫu nhiên và sau đó được "kẹp" bằng cách sử dụng mặt nạ bitwise cho các byte 0 và 31. Điều này không được thực hiện đối với Red25519. Các hàm GENERATE_ALPHA() và BLIND_PRIVKEY() được định nghĩa ở trên tạo ra các khóa riêng Red25519 phù hợp bằng cách sử dụng mod L.

Trong Red25519, việc tính toán r cho việc ký sử dụng dữ liệu ngẫu nhiên bổ sung, và sử dụng giá trị public key thay vì hash của private key. Do có dữ liệu ngẫu nhiên, mỗi chữ ký Red25519 đều khác nhau, ngay cả khi ký cùng một dữ liệu với cùng một key.

```
Signing:
  T = 80 random bytes
  r = H*(T || publickey || message)
  (rest is the same as in Ed25519)

Verification:
  Same as for Ed25519
```
### Mã hóa và xử lý

#### Phái sinh các subcredential

Như một phần của quá trình blinding (làm mù), chúng ta cần đảm bảo rằng một LS2 được mã hóa chỉ có thể được giải mã bởi ai đó biết signing public key tương ứng của Destination. Destination đầy đủ không bắt buộc. Để đạt được điều này, chúng ta tạo ra một credential từ signing public key:

```
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
credential = H("credential", keydata)
```
Chuỗi cá nhân hóa đảm bảo rằng thông tin xác thực không va chạm với bất kỳ hash nào được sử dụng làm khóa tra cứu DHT, chẳng hạn như hash Destination thông thường.

Với một khóa được che giấu cụ thể, chúng ta có thể suy ra một subcredential:

```
subcredential = H("subcredential", credential || blindedPublicKey)
```
Subcredential được bao gồm trong các quá trình dẫn xuất khóa bên dưới, điều này liên kết các khóa đó với kiến thức về khóa công khai ký của Destination.

#### Mã hóa tầng 1

Đầu tiên, đầu vào cho quá trình tạo khóa được chuẩn bị:

```
outerInput = subcredential || publishedTimestamp
```
Tiếp theo, một salt ngẫu nhiên được tạo ra:

```
outerSalt = CSRNG(32)
```
Sau đó khóa được sử dụng để mã hóa lớp 1 được tạo ra:

```
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Cuối cùng, plaintext lớp 1 được mã hóa và tuần tự hóa:

```
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```
#### Giải mã tầng 1

Salt được phân tích từ ciphertext lớp 1:

```
outerSalt = outerCiphertext[0:31]
```
Sau đó khóa được sử dụng để mã hóa lớp 1 được tạo ra:

```
outerInput = subcredential || publishedTimestamp
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Cuối cùng, bản mã hóa lớp 1 được giải mã:

```
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```
#### Mã hóa lớp 2

Khi xác thực client được kích hoạt, `authCookie` được tính toán như mô tả bên dưới. Khi xác thực client bị vô hiệu hóa, `authCookie` là mảng byte có độ dài bằng không.

Mã hóa tiến hành theo cách tương tự như lớp 1:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = CSRNG(32)
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```
#### Giải mã tầng 2

Khi client authorization được bật, `authCookie` được tính toán như mô tả bên dưới. Khi client authorization bị tắt, `authCookie` là mảng byte có độ dài bằng không.

Quá trình giải mã diễn ra theo cách tương tự như lớp 1:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = innerCiphertext[0:31]
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```
### Ủy quyền theo từng client

Khi client authorization được kích hoạt cho một Destination, máy chủ duy trì một danh sách các client mà họ ủy quyền để giải mã dữ liệu LS2 được mã hóa. Dữ liệu được lưu trữ cho mỗi client phụ thuộc vào cơ chế ủy quyền, và bao gồm một số dạng tài liệu khóa mà mỗi client tạo ra và gửi đến máy chủ thông qua một cơ chế bảo mật ngoài băng tần.

Có hai phương án để triển khai ủy quyền theo từng client:

#### Ủy quyền client DH

Mỗi client tạo ra một cặp khóa DH `[csk_i, cpk_i]`, và gửi khóa công khai `cpk_i` đến server.

##### Xử lý máy chủ

Server tạo ra một `authCookie` mới và một cặp khóa DH tạm thời:

```
authCookie = CSRNG(32)
esk = GENERATE_PRIVATE()
epk = DERIVE_PUBLIC(esk)
```
Sau đó, đối với mỗi client được ủy quyền, server sẽ mã hóa `authCookie` bằng khóa công khai của nó:

```
sharedSecret = DH(esk, cpk_i)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
Server đặt từng tuple `[clientID_i, clientCookie_i]` vào layer 1 của LS2 được mã hóa, cùng với `epk`.

##### Xử lý client

Client sử dụng private key của nó để tạo ra client identifier dự kiến `clientID_i`, encryption key `clientKey_i`, và encryption IV `clientIV_i`:

```
sharedSecret = DH(csk_i, epk)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Sau đó client tìm kiếm trong dữ liệu ủy quyền tầng 1 để tìm một mục chứa `clientID_i`. Nếu tồn tại một mục khớp, client sẽ giải mã nó để lấy được `authCookie`:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Xác thực client bằng khóa chia sẻ trước

Mỗi client tạo ra một khóa bí mật 32-byte `psk_i`, và gửi nó đến server. Ngoài ra, server có thể tạo ra khóa bí mật, và gửi nó đến một hoặc nhiều client.

##### Xử lý máy chủ

Máy chủ tạo ra một `authCookie` và salt mới:

```
authCookie = CSRNG(32)
authSalt = CSRNG(32)
```
Sau đó, đối với mỗi client được ủy quyền, server sẽ mã hóa `authCookie` bằng khóa chia sẻ trước của nó:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
Server đặt mỗi tuple `[clientID_i, clientCookie_i]` vào lớp 1 của LS2 được mã hóa, cùng với `authSalt`.

##### Xử lý client

Client sử dụng khóa chia sẻ trước của mình để tạo ra định danh client dự kiến `clientID_i`, khóa mã hóa `clientKey_i`, và IV mã hóa `clientIV_i`:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Sau đó client tìm kiếm trong dữ liệu ủy quyền layer 1 để tìm một mục chứa `clientID_i`. Nếu tìm thấy mục khớp, client sẽ giải mã nó để lấy `authCookie`:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Các cân nhắc về bảo mật

Cả hai cơ chế ủy quyền client ở trên đều cung cấp quyền riêng tư cho thành viên client. Một thực thể chỉ biết Destination có thể thấy có bao nhiêu client đang đăng ký tại bất kỳ thời điểm nào, nhưng không thể theo dõi client nào đang được thêm vào hoặc thu hồi.

Các server NÊN ngẫu nhiên hóa thứ tự của các client mỗi khi họ tạo ra một LS2 được mã hóa, để ngăn các client biết được vị trí của chúng trong danh sách và suy đoán khi nào các client khác đã được thêm vào hoặc thu hồi.

Máy chủ CÓ THỂ chọn ẩn số lượng client đã đăng ký bằng cách chèn các mục ngẫu nhiên vào danh sách dữ liệu ủy quyền.

##### Ưu điểm của phương thức xác thực client DH

- Tính bảo mật của lược đồ không phụ thuộc hoàn toàn vào việc trao đổi tài liệu khóa client ngoài băng tần. Khóa riêng của client không bao giờ cần rời khỏi thiết bị của họ, và do đó kẻ tấn công có thể chặn được việc trao đổi ngoài băng tần, nhưng không thể phá vỡ thuật toán DH, thì không thể giải mã LS2 được mã hóa, hoặc xác định thời gian client được cấp quyền truy cập.

##### Nhược điểm của việc xác thực client DH

- Yêu cầu N + 1 phép toán DH ở phía server cho N client.
- Yêu cầu một phép toán DH ở phía client.
- Yêu cầu client tạo ra khóa bí mật.

##### Ưu điểm của xác thực client PSK

- Không yêu cầu các thao tác DH.
- Cho phép server tạo khóa bí mật.
- Cho phép server chia sẻ cùng một khóa với nhiều client, nếu muốn.

##### Nhược điểm của việc ủy quyền client PSK

- Bảo mật của sơ đồ này phụ thuộc hoàn toàn vào việc trao đổi tài liệu khóa client qua kênh out-of-band. Kẻ tấn công chặn được quá trình trao đổi cho một client cụ thể có thể giải mã bất kỳ LS2 được mã hóa tiếp theo mà client đó được ủy quyền, cũng như xác định khi nào quyền truy cập của client bị thu hồi.

### Encrypted LS với Base 32 Addresses

Bạn không thể sử dụng địa chỉ base 32 truyền thống cho một LS2 được mã hóa, vì nó chỉ chứa hash của destination. Nó không cung cấp khóa công khai không bị che khuất. Do đó, chỉ riêng địa chỉ base 32 là không đủ. Client cần có hoặc là destination đầy đủ (chứa khóa công khai), hoặc chính khóa công khai. Nếu client có destination đầy đủ trong sổ địa chỉ, và sổ địa chỉ hỗ trợ tìm kiếm ngược theo hash, thì khóa công khai có thể được truy xuất.

Vì vậy chúng ta cần một định dạng mới để đặt khóa công khai thay vì hash vào địa chỉ base32. Định dạng này cũng phải chứa kiểu chữ ký của khóa công khai và kiểu chữ ký của sơ đồ làm mờ. Tổng yêu cầu là 32 + 3 = 35 byte, cần 56 ký tự trong base 32, hoặc nhiều hơn đối với các kiểu khóa công khai dài hơn.

```
data = ((1 byte flags || 1 byte unblinded sigtype || 1 byte blinded sigtype) XOR checksum) || 32 byte pubkey
address = Base32Encode(data) || ".b32.i2p"
```
Chúng tôi sử dụng cùng hậu tố ".b32.i2p" như đối với các địa chỉ base 32 truyền thống. Địa chỉ cho encrypted leasesets được xác định bởi 56 ký tự được mã hóa (35 byte sau giải mã), so với 52 ký tự (32 byte) cho các địa chỉ base 32 truyền thống. Năm bit không sử dụng ở cuối b32 phải là 0.

Bạn không thể sử dụng LS2 mã hóa cho bittorrent, vì các phản hồi announce compact chỉ có 32 byte. 32 byte này chỉ chứa hash. Không có chỗ để chỉ ra rằng leaseset đã được mã hóa, hoặc các loại chữ ký.

Xem [đặc tả đặt tên](/docs/specs/naming) hoặc [đề xuất 149](/proposals/149-b32-encrypted-ls2) để biết thêm thông tin về định dạng mới.

### LeaseSet Mã hóa với Khóa Ngoại tuyến

Đối với các leaseSet được mã hóa với khóa offline, các khóa riêng tư blinded cũng phải được tạo offline, một khóa cho mỗi ngày.

Vì khối chữ ký offline tùy chọn nằm trong phần văn bản rõ của leaseset được mã hóa, bất kỳ ai thu thập dữ liệu từ các floodfill đều có thể sử dụng điều này để theo dõi leaseset (nhưng không thể giải mã nó) trong vài ngày. Để ngăn chặn điều này, chủ sở hữu của các khóa cũng nên tạo ra các khóa tạm thời mới cho mỗi ngày. Cả khóa tạm thời và khóa làm mờ đều có thể được tạo trước và giao cho router theo lô.

Không có định dạng tệp nào được định nghĩa để đóng gói nhiều khóa tạm thời và khóa bị che mù và cung cấp chúng cho client hoặc router. Không có cải tiến giao thức I2CP nào được định nghĩa để hỗ trợ leaseSet được mã hóa với các khóa ngoại tuyến.

### Ghi chú

- Một dịch vụ sử dụng leaseSet được mã hóa sẽ xuất bản phiên bản được mã hóa lên các floodfill. Tuy nhiên, để tối ưu hiệu suất, nó sẽ gửi leaseSet không mã hóa cho các client trong thông điệp garlic được bọc, sau khi đã xác thực (ví dụ thông qua whitelist).
- Các floodfill có thể giới hạn kích thước tối đa ở một giá trị hợp lý để ngăn chặn lạm dụng.
- Sau khi giải mã, cần thực hiện một số kiểm tra, bao gồm việc kiểm tra timestamp bên trong và thời gian hết hạn khớp với những thông tin ở cấp cao nhất.
- ChaCha20 được chọn thay vì AES. Trong khi tốc độ tương tự nhau nếu có hỗ trợ phần cứng AES, ChaCha20 nhanh hơn 2.5-3 lần khi không có hỗ trợ phần cứng AES, chẳng hạn như trên các thiết bị ARM cấp thấp.

## Tài liệu tham khảo

- **[ED25519-REFS]** "Chữ ký tốc độ cao bảo mật cao" bởi Daniel J. Bernstein, Niels Duif, Tanja Lange, Peter Schwabe, và Bo-Yin Yang. [http://cr.yp.to/papers.html#ed25519](http://cr.yp.to/papers.html#ed25519)
- **[KEYBLIND-PROOF]** [https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html](https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html)
- **[KEYBLIND-REFS]** [https://trac.torproject.org/projects/tor/ticket/8106](https://trac.torproject.org/projects/tor/ticket/8106) và [https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html](https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html)
- **[PRNG-REFS]** [http://projectbullrun.org/dual-ec/ext-rand.html](http://projectbullrun.org/dual-ec/ext-rand.html) và [https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html)
- **[RFC-2104]** [https://tools.ietf.org/html/rfc2104](https://tools.ietf.org/html/rfc2104)
- **[RFC-4880-S5.1]** [https://tools.ietf.org/html/rfc4880#section-5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
- **[RFC-5869]** [https://tools.ietf.org/html/rfc5869](https://tools.ietf.org/html/rfc5869)
- **[RFC-7539-S2.4]** [https://tools.ietf.org/html/rfc7539#section-2.4](https://tools.ietf.org/html/rfc7539#section-2.4)
- **[TOR-REND-SPEC-V3]** [https://spec.torproject.org/rend-spec-v3](https://spec.torproject.org/rend-spec-v3)
- **[ZCASH]** [https://github.com/zcash/zips/tree/master/protocol/protocol.pdf](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)
