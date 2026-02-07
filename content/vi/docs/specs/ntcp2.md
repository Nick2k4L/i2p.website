---
title: "NTCP2 Transport"
description: "Giao thức truyền tải TCP dựa trên Noise cho các liên kết router-to-router"
slug: "ntcp2"
category: "Transports"
lastUpdated: "2026-01"
accurateFor: "0.9.66"
---

## Tổng quan

NTCP2 là một giao thức thỏa thuận khóa được xác thực giúp cải thiện khả năng chống lại các hình thức nhận dạng tự động và tấn công khác nhau của [NTCP](/docs/transport/ntcp).

NTCP2 được thiết kế để linh hoạt và có thể tồn tại cùng với NTCP. Nó có thể được hỗ trợ trên cùng port với NTCP, hoặc một port khác, hoặc hoàn toàn không hỗ trợ NTCP đồng thời. Xem phần Published Router Info bên dưới để biết chi tiết.

Giống như các phương thức vận chuyển khác của I2P, NTCP2 được định nghĩa chỉ dành cho việc vận chuyển các thông điệp I2NP từ điểm-đến-điểm (router-to-router). Nó không phải là một đường ống dữ liệu đa mục đích.

NTCP2 được hỗ trợ từ phiên bản 0.9.36. Xem [Prop111](/proposals/111-ntcp-2) để biết đề xuất gốc, bao gồm thảo luận nền tảng và thông tin bổ sung.

## Noise Protocol Framework

NTCP2 sử dụng Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (Revision 33, 2017-10-04). Noise có các thuộc tính tương tự như giao thức Station-To-Station [STS](#references), đây là cơ sở cho giao thức [SSU](/docs/transport/ssu). Theo thuật ngữ của Noise, Alice là bên khởi tạo, và Bob là bên phản hồi.

NTCP2 dựa trên giao thức Noise Noise_XK_25519_ChaChaPoly_SHA256. (Mã định danh thực tế cho hàm rút gọn khóa ban đầu là "Noise_XKaesobfse+hs2+hs3_25519_ChaChaPoly_SHA256" để chỉ ra các mở rộng I2P - xem phần KDF 1 bên dưới) Giao thức Noise này sử dụng các nguyên hàm sau:

- Handshake Pattern: XK Alice truyền khóa của cô ấy cho Bob (X) Alice đã biết khóa tĩnh của Bob (K)
- DH Function: X25519 X25519 DH với độ dài khóa 32 byte như được quy định trong [RFC-7748](https://tools.ietf.org/html/rfc7748).
- Cipher Function: ChaChaPoly AEAD_CHACHA20_POLY1305 như được quy định trong [RFC-7539](https://tools.ietf.org/html/rfc7539) mục 2.8. 12 byte nonce, với 4 byte đầu được đặt thành zero.
- Hash Function: SHA256 Hash tiêu chuẩn 32-byte, đã được sử dụng rộng rãi trong I2P.

## Bổ sung vào Framework

NTCP2 định nghĩa các cải tiến sau đây cho Noise_XK_25519_ChaChaPoly_SHA256. Những cải tiến này nhìn chung tuân theo các hướng dẫn trong [NOISE](https://noiseprotocol.org/noise.html) mục 13.

1) Các khóa tạm thời dạng rõ được làm xáo trộn bằng mã hóa AES sử dụng khóa và IV đã biết. 2) Padding rõ ngẫu nhiên được thêm vào thông điệp 1 và 2. Padding rõ được bao gồm trong tính toán hash handshake (MixHash). Xem các phần KDF bên dưới cho thông điệp 2 và thông điệp 3 phần 1. Padding AEAD ngẫu nhiên được thêm vào thông điệp 3 và các thông điệp giai đoạn dữ liệu. 3) Một trường độ dài khung hai byte được thêm vào, như yêu cầu đối với Noise qua TCP, và như trong obfs4. Điều này chỉ được sử dụng trong các thông điệp giai đoạn dữ liệu. Các khung AEAD thông điệp 1 và 2 có độ dài cố định. Khung AEAD thông điệp 3 phần 1 có độ dài cố định. Độ dài khung AEAD thông điệp 3 phần 2 được chỉ định trong thông điệp 1. 4) Trường độ dài khung hai byte được làm xáo trộn với SipHash-2-4, như trong obfs4. 5) Định dạng payload được xác định cho các thông điệp 1, 2, 3, và giai đoạn dữ liệu. Tất nhiên, những điều này không được định nghĩa trong framework.

## Tin nhắn

Tất cả các thông điệp NTCP2 đều có độ dài nhỏ hơn hoặc bằng 65537 byte. Định dạng thông điệp dựa trên các thông điệp Noise, với những sửa đổi về khung và tính không thể phân biệt. Các triển khai sử dụng thư viện Noise tiêu chuẩn có thể cần xử lý trước các thông điệp nhận được sang/từ định dạng thông điệp Noise. Tất cả các trường được mã hóa đều là bản mã AEAD.

Trình tự thiết lập như sau:

```
Alice Bob

SessionRequest -------------------> <------------------- SessionCreated SessionConfirmed ----------------->
```
Sử dụng thuật ngữ Noise, trình tự thiết lập và dữ liệu như sau: (Thuộc tính Bảo mật Payload từ [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs): Authentication Confidentiality

<- s \... -> e, es 0 2 <- e, ee 2 1 -> s, se 2 5 <- 2 5
```
Sau khi một phiên kết nối đã được thiết lập, Alice và Bob có thể trao đổi các thông điệp Data.

Tất cả các loại thông điệp (SessionRequest, SessionCreated, SessionConfirmed, Data và TimeSync) được chỉ định trong phần này.

Một số ký hiệu:

    - RH_A = Router Hash for Alice (32 bytes)
    - RH_B = Router Hash for Bob (32 bytes)

### Mã hóa có xác thực

Có ba phiên bản mã hóa xác thực riêng biệt (CipherStates). Một phiên bản trong giai đoạn bắt tay, và hai phiên bản (truyền và nhận) cho giai đoạn dữ liệu. Mỗi phiên bản có khóa riêng từ một KDF.

Dữ liệu được mã hóa/xác thực sẽ được biểu diễn như

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | Encrypted and authenticated data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+
```
#### ChaCha20/Poly1305

Định dạng dữ liệu được mã hóa và xác thực.

Đầu vào cho các hàm mã hóa/giải mã:

```
k :: 32 byte cipher key, as generated from KDF



nonce :: Counter-based nonce, 12 bytes.

Starts at 0 and incremented for each message. First four bytes are always zero. Last eight bytes are the counter, little-endian encoded. Maximum value is 2**64 - 2. Connection must be dropped and restarted after it reaches that value. The value 2**64 - 1 must never be sent.

ad :: In handshake phase:

Associated data, 32 bytes. The SHA256 hash of all preceding data. In data phase: Zero bytes

data :: Plaintext data, 0 or more bytes
```
Đầu ra của hàm mã hóa, đầu vào của hàm giải mã:

```
+----+----+----+----+----+----+----+----+

[|Obfs Len |](##SUBST##|Obfs Len |) | +----+----+ + | ChaCha20 encrypted data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | Poly1305 Message Authentication Code | + (MAC) + | 16 bytes | +----+----+----+----+----+----+----+----+

    Obfs Len :: Length of (encrypted data + MAC) to follow, 16 - 65535

    :   Obfuscation using SipHash (see below) Not used in message 1 or 2, or message 3 part 1, where the length is fixed Not used in message 3 part 1, as the length is specified in message 1

    encrypted data :: Same size as plaintext data, 0 - 65519 bytes

    MAC :: Poly1305 message authentication code, 16 bytes
```
Đối với ChaCha20, những gì được mô tả ở đây tương ứng với [RFC-7539](https://tools.ietf.org/html/rfc7539), cũng được sử dụng tương tự trong TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).

#### Ghi chú

- Vì ChaCha20 là một stream cipher, các plaintext không cần được padding. Các byte keystream bổ sung sẽ bị loại bỏ.
- Key cho cipher (256 bit) được thống nhất thông qua SHA256 KDF. Chi tiết về KDF cho từng thông điệp được nêu trong các phần riêng biệt bên dưới.
- Các frame ChaChaPoly cho thông điệp 1, 2, và phần đầu của thông điệp 3, có kích thước đã biết. Bắt đầu từ phần thứ hai của thông điệp 3, các frame có kích thước thay đổi. Kích thước của thông điệp 3 phần 1 được chỉ định trong thông điệp 1. Bắt đầu từ giai đoạn dữ liệu, các frame được thêm phía trước với độ dài hai byte được làm mờ bằng SipHash như trong obfs4.
- Padding nằm bên ngoài frame dữ liệu đã xác thực cho thông điệp 1 và 2. Padding được sử dụng trong KDF cho thông điệp tiếp theo nên việc can thiệp sẽ được phát hiện. Bắt đầu từ thông điệp 3, padding nằm bên trong frame dữ liệu đã xác thực.

#### Xử lý lỗi AEAD

- Trong tin nhắn 1, 2, và tin nhắn 3 phần 1 và 2, kích thước tin nhắn AEAD được biết trước. Khi xác thực AEAD thất bại, người nhận phải dừng xử lý tin nhắn và đóng kết nối mà không phản hồi. Đây nên là một đóng kết nối bất thường (TCP RST).
- Để chống thăm dò, trong tin nhắn 1, sau khi AEAD thất bại, Bob nên đặt thời gian chờ ngẫu nhiên (phạm vi chưa xác định) và sau đó đọc một số byte ngẫu nhiên (phạm vi chưa xác định) trước khi đóng socket. Bob nên duy trì một danh sách đen các IP có lỗi lặp lại.
- Trong giai đoạn dữ liệu, kích thước tin nhắn AEAD được "mã hóa" (làm tối) bằng SipHash. Cần cẩn thận để tránh tạo ra một oracle giải mã. Khi xác thực AEAD giai đoạn dữ liệu thất bại, người nhận nên đặt thời gian chờ ngẫu nhiên (phạm vi chưa xác định) và sau đó đọc một số byte ngẫu nhiên (phạm vi chưa xác định). Sau khi đọc, hoặc khi hết thời gian chờ đọc, người nhận nên gửi một payload với khối kết thúc chứa mã lý do "AEAD failure" và đóng kết nối.
- Thực hiện cùng hành động lỗi cho giá trị trường độ dài không hợp lệ trong giai đoạn dữ liệu.

### Hàm Dẫn xuất Khóa (KDF) (cho thông điệp bắt tay 1)

KDF tạo ra một khóa cipher k cho giai đoạn handshake từ kết quả DH, sử dụng HMAC-SHA256(key, data) như được định nghĩa trong [RFC-2104](https://tools.ietf.org/html/rfc2104). Đây là các hàm InitializeSymmetric(), MixHash(), và MixKey(), chính xác như được định nghĩa trong đặc tả Noise.

```
This is the "e" message pattern:

// Define protocol_name. Set protocol_name = "Noise_XKaesobfse+hs2+hs3_25519_ChaChaPoly_SHA256" (48 bytes, US-ASCII encoded, no NULL termination).

// Define Hash h = 32 bytes h = SHA256(protocol_name);

Define ck = 32 byte chaining key. Copy the h data to ck. Set ck = h

Define rs = Bob's 32-byte static key as published in the RouterInfo

// MixHash(null prologue) h = SHA256(h);

// up until here, can all be precalculated by Alice for all outgoing connections

// Alice must validate that Bob's static key is a valid point on the curve here.

// Bob static key // MixHash(rs) // || below means append h = SHA256(h || rs);

// up until here, can all be precalculated by Bob for all incoming connections

This is the "e" message pattern:

Alice generates her ephemeral DH key pair e.

// Alice ephemeral key X // MixHash(e.pubkey) // || below means append h = SHA256(h || e.pubkey);

// h is used as the associated data for the AEAD in message 1 // Retain the Hash h for the message 2 KDF

End of "e" message pattern.

This is the "es" message pattern:

// DH(e, rs) == DH(s, re) Define input_key_material = 32 byte DH result of Alice's ephemeral key and Bob's static key Set input_key_material = X25519 DH result

// MixKey(DH())

Define temp_key = 32 bytes Define HMAC-SHA256(key, data) as in [RFC-2104](https://tools.ietf.org/html/rfc2104) // Generate a temp key from the chaining key and DH result // ck is the chaining key, defined above temp_key = HMAC-SHA256(ck, input_key_material) // overwrite the DH result in memory, no longer needed input_key_material = (all zeros)

// Output 1 // Set a new chaining key from the temp key // byte() below means a single byte ck = HMAC-SHA256(temp_key, byte(0x01)).

// Output 2 // Generate the cipher key k Define k = 32 bytes // || below means append // byte() below means a single byte k = HMAC-SHA256(temp_key, ck || byte(0x02)). // overwrite the temp_key in memory, no longer needed temp_key = (all zeros)

// retain the chaining key ck for message 2 KDF

End of "es" message pattern.
```
### 1) SessionRequest

Alice gửi cho Bob.

Noise content: Khóa tạm thời X của Alice Noise payload: Khối tùy chọn 16 byte Non-noise payload: Padding ngẫu nhiên

(Thuộc tính Bảo mật Payload từ [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs): Authentication Confidentiality

-> e, es 0 2

    Authentication: None (0). This payload may have been sent by any party, including an active attacker.

    Confidentiality: 2. Encryption to a known recipient, forward secrecy for sender compromise only, vulnerable to replay. This payload is encrypted based only on DHs involving the recipient's static key pair. If the recipient's static private key is compromised, even at a later date, this payload can be decrypted. This message can also be replayed, since there's no ephemeral contribution from the recipient.

    "e": Alice generates a new ephemeral key pair and stores it in the e

    :   variable, writes the ephemeral public key as cleartext into the message buffer, and hashes the public key along with the old h to derive a new h.

    "es": A DH is performed between the Alice's ephemeral key pair and the

    :   Bob's static key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Giá trị X được mã hóa để đảm bảo tính không thể phân biệt và duy nhất của payload, điều này cần thiết cho các biện pháp đối phó DPI. Chúng tôi sử dụng mã hóa AES để đạt được điều này, thay vì các phương án phức tạp và chậm hơn như elligator2. Mã hóa bất đối xứng với khóa công khai của router Bob sẽ quá chậm. Mã hóa AES sử dụng router hash của Bob làm khóa và IV của Bob như được công bố trong netDb.

Mã hóa AES chỉ dành để chống lại DPI (Deep Packet Inspection - kiểm tra gói tin sâu). Bất kỳ bên nào biết router hash của Bob và IV, được công bố trong cơ sở dữ liệu mạng, đều có thể giải mã giá trị X trong thông điệp này.

Phần đệm không được mã hóa bởi Alice. Bob có thể cần giải mã phần đệm để ngăn chặn các cuộc tấn công định thời.

Nội dung thô:

```
+----+----+----+----+----+----+----+----+

|                                       |

    + obfuscated with RH_B + | AES-CBC-256 encrypted X | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | | + + | ChaChaPoly frame | + (32 bytes) + | k defined in KDF for message 1 | + n = 0 + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | unencrypted authenticated | ~ padding (optional) ~ | length defined in options block | +----+----+----+----+----+----+----+----+

    X :: 32 bytes, AES-256-CBC encrypted X25519 ephemeral key, little endian

    :   key: RH_B iv: As published in Bobs network database entry

    padding :: Random data, 0 or more bytes.

    :   Total message length must be 65535 bytes or less. Total message length must be 287 bytes or less if Bob is publishing his address as NTCP (see Version Detection section below). Alice and Bob will use the padding data in the KDF for message 2. It is authenticated so that any tampering will cause the next message to fail.
```
Dữ liệu không mã hóa (không hiển thị thẻ xác thực Poly1305):

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | X | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | options | + (16 bytes) + | | +----+----+----+----+----+----+----+----+ | unencrypted authenticated | + padding (optional) + | length defined in options block | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    X :: 32 bytes, X25519 ephemeral key, little endian

    options :: options block, 16 bytes, see below

    padding :: Random data, 0 or more bytes.

    :   Total message length must be 65535 bytes or less. Total message length must be 287 bytes or less if Bob is publishing his address as "NTCP" (see Version Detection section below) Alice and Bob will use the padding data in the KDF for message 2. It is authenticated so that any tampering will cause the next message to fail.
```
Khối tùy chọn: Lưu ý: Tất cả các trường đều theo thứ tự big-endian.

```
+----+----+----+----+----+----+----+----+

| id | ver| padLen | m3p2len | Rsvd(0) |

    +-------------------------------+-------------------------------+
    | > tsA                         | > Reserved (0)                |
    +-------------------------------+-------------------------------+

    id :: 1 byte, the network ID (currently 2, except for test networks)

    :   As of 0.9.42. See proposal 147.

    ver :: 1 byte, protocol version (currently 2)

    padLen :: 2 bytes, length of the padding, 0 or more

    :   Min/max guidelines TBD. Random size from 0 to 31 bytes minimum? (Distribution is implementation-dependent)

    m3p2Len :: 2 bytes, length of the the second AEAD frame in SessionConfirmed

    :   (message 3 part 2) See notes below

    Rsvd :: 2 bytes, set to 0 for compatibility with future options

    tsA :: 4 bytes, Unix timestamp, unsigned seconds.

    :   Wraps around in 2106

    Reserved :: 4 bytes, set to 0 for compatibility with future options
```
#### Ghi chú

- Khi địa chỉ được công bố là "NTCP", Bob hỗ trợ cả NTCP và NTCP2 trên cùng một cổng. Để tương thích, khi khởi tạo kết nối đến địa chỉ được công bố là "NTCP", Alice phải giới hạn kích thước tối đa của thông điệp này, bao gồm padding, xuống 287 byte hoặc ít hơn. Điều này tạo điều kiện cho việc nhận dạng giao thức tự động bởi Bob. Khi được công bố là "NTCP2", không có giới hạn kích thước. Xem các phần Địa chỉ Được công bố và Phát hiện Phiên bản bên dưới.

- Giá trị X duy nhất trong khối AES ban đầu đảm bảo rằng bản mã hóa sẽ khác nhau cho mỗi phiên.

- Bob phải từ chối các kết nối có giá trị timestamp quá xa so với thời gian hiện tại. Gọi khoảng thời gian tối đa là "D". Bob phải duy trì một cache cục bộ của các giá trị handshake đã sử dụng trước đó và từ chối các giá trị trùng lặp, để ngăn chặn các cuộc tấn công replay. Các giá trị trong cache phải có thời gian tồn tại ít nhất là 2*D. Các giá trị cache phụ thuộc vào cách triển khai, tuy nhiên có thể sử dụng giá trị X 32-byte (hoặc tương đương đã mã hóa của nó).

- Khóa tạm thời Diffie-Hellman không bao giờ được sử dụng lại để ngăn chặn các cuộc tấn công mật mã, và việc sử dụng lại sẽ bị từ chối như một cuộc tấn công phát lại.

- Các tùy chọn "KE" và "auth" phải tương thích với nhau, tức là khóa bí mật chung K phải có kích thước phù hợp. Nếu thêm nhiều tùy chọn "auth" hơn, điều này có thể thay đổi ngầm định nghĩa của cờ "KE" để sử dụng một KDF khác hoặc kích thước cắt bớt khác.

- Bob phải xác thực rằng khóa tạm thời (ephemeral key) của Alice là một điểm hợp lệ trên đường cong ở đây.

- Padding nên được giới hạn ở mức hợp lý. Bob có thể từ chối các kết nối có padding quá mức. Bob sẽ chỉ định các tùy chọn padding của mình trong message 2. Hướng dẫn min/max sẽ được xác định sau. Kích thước ngẫu nhiên từ 0 đến tối thiểu 31 byte? (Phân phối phụ thuộc vào implementation) Các implementation Java hiện tại giới hạn padding tối đa 256 byte.

- Khi có bất kỳ lỗi nào, bao gồm AEAD, DH, timestamp, phát hiện replay rõ ràng, hoặc lỗi xác thực khóa, Bob phải dừng xử lý tin nhắn và đóng kết nối mà không phản hồi. Đây nên là một đóng kết nối bất thường (TCP RST). Để chống thăm dò, sau lỗi AEAD, Bob nên đặt timeout ngẫu nhiên (phạm vi TBD) và sau đó đọc một số byte ngẫu nhiên (phạm vi TBD), trước khi đóng socket.

- Bob có thể thực hiện kiểm tra MSB nhanh cho khóa hợp lệ (X[31] & 0x80 == 0) trước khi thử giải mã. Nếu bit cao được đặt, hãy triển khai khả năng chống thăm dò như với các lỗi AEAD.

- Giảm thiểu DoS: DH là một thao tác tương đối tốn kém. Như với giao thức NTCP trước đó, các router nên thực hiện tất cả các biện pháp cần thiết để ngăn chặn cạn kiệt CPU hoặc kết nối. Đặt giới hạn cho số kết nối hoạt động tối đa và số lượng thiết lập kết nối tối đa đang diễn ra. Áp dụng timeout đọc (cả trên mỗi lần đọc và tổng cộng cho "slowloris"). Giới hạn các kết nối lặp lại hoặc đồng thời từ cùng một nguồn. Duy trì danh sách đen cho các nguồn thường xuyên thất bại. Không phản hồi lại lỗi AEAD.

- Để tạo điều kiện thuận lợi cho việc phát hiện phiên bản nhanh chóng và bắt tay, các triển khai phải đảm bảo rằng Alice đệm và sau đó xả toàn bộ nội dung của tin nhắn đầu tiên cùng một lúc, bao gồm cả phần đệm. Điều này làm tăng khả năng dữ liệu sẽ được chứa trong một gói TCP duy nhất (trừ khi bị phân đoạn bởi hệ điều hành hoặc middlebox), và được Bob nhận tất cả cùng một lúc. Ngoài ra, các triển khai phải đảm bảo rằng Bob đệm và sau đó xả toàn bộ nội dung của tin nhắn thứ hai cùng một lúc, bao gồm cả phần đệm, và rằng Bob đệm và sau đó xả toàn bộ nội dung của tin nhắn thứ ba cùng một lúc. Điều này cũng nhằm mục đích hiệu quả và đảm bảo tính hiệu quả của việc đệm ngẫu nhiên.

- Trường "ver": Giao thức Noise tổng thể, các phần mở rộng, và giao thức NTCP bao gồm các đặc tả payload, cho biết NTCP2. Trường này có thể được sử dụng để chỉ ra hỗ trợ cho các thay đổi trong tương lai.

- Độ dài phần 2 của Thông điệp 3: Đây là kích thước của khung AEAD thứ hai (bao gồm MAC 16-byte) chứa Router Info của Alice và padding tùy chọn sẽ được gửi trong thông điệp SessionConfirmed. Vì các router định kỳ tạo lại và xuất bản lại Router Info của chúng, kích thước của Router Info hiện tại có thể thay đổi trước khi thông điệp 3 được gửi. Các triển khai phải chọn một trong hai chiến lược:

a\) lưu Router Info hiện tại để gửi trong thông điệp 3, để biết kích thước, và tùy chọn thêm chỗ cho padding;

b\) tăng kích thước đã chỉ định đủ để cho phép khả năng tăng kích thước Router Info, và luôn thêm padding khi message 3 thực sự được gửi. Trong cả hai trường hợp, độ dài "m3p2len" được bao gồm trong message 1 phải chính xác bằng kích thước của frame đó khi được gửi trong message 3.

- Bob phải thất bại kết nối nếu còn bất kỳ dữ liệu đến nào sau khi xác thực message 1 và đọc padding. Không nên có dữ liệu thừa từ Alice, vì Bob chưa phản hồi với message 2.

- Trường network ID được sử dụng để nhanh chóng xác định các kết nối xuyên mạng. Nếu trường này khác không và không khớp với network ID của Bob, Bob nên ngắt kết nối và chặn các kết nối trong tương lai. Bất kỳ kết nối nào từ các mạng thử nghiệm sẽ có ID khác và sẽ thất bại trong kiểm tra. Từ phiên bản 0.9.42. Xem đề xuất 147 để biết thêm thông tin.

### Hàm Tạo Khóa (KDF) (cho thông điệp bắt tay số 2 và phần 1 của thông điệp số 3)

```
// take h saved from message 1 KDF
// MixHash(ciphertext)
h = SHA256(h || 32 byte encrypted payload from message 1)

// MixHash(padding)
// Only if padding length is nonzero
h = SHA256(h || random padding from message 1)

This is the "e" message pattern:

Bob generates his ephemeral DH key pair e.

// h is from KDF for handshake message 1
// Bob ephemeral key Y
// MixHash(e.pubkey)
// || below means append
h = SHA256(h || e.pubkey);

// h is used as the associated data for the AEAD in message 2
// Retain the Hash h for the message 3 KDF

End of "e" message pattern.

This is the "ee" message pattern:

// DH(e, re)
Define input_key_material = 32 byte DH result of Alice's ephemeral key and Bob's ephemeral key
Set input_key_material = X25519 DH result
// overwrite Alice's ephemeral key in memory, no longer needed
// Alice:
e(public and private) = (all zeros)
// Bob:
re = (all zeros)

// MixKey(DH())

Define temp_key = 32 bytes
Define HMAC-SHA256(key, data) as in [RFC-2104]_
// Generate a temp key from the chaining key and DH result
// ck is the chaining key, from the KDF for handshake message 1
temp_key = HMAC-SHA256(ck, input_key_material)
// overwrite the DH result in memory, no longer needed
input_key_material = (all zeros)

// Output 1
// Set a new chaining key from the temp key
// byte() below means a single byte
ck =       HMAC-SHA256(temp_key, byte(0x01)).

// Output 2
// Generate the cipher key k
Define k = 32 bytes
// || below means append
// byte() below means a single byte
k =        HMAC-SHA256(temp_key, ck || byte(0x02)).
// overwrite the temp_key in memory, no longer needed
temp_key = (all zeros)

// retain the chaining key ck for message 3 KDF

End of "ee" message pattern.
```
### 2) SessionCreated

Bob gửi cho Alice.

Nội dung Noise: khóa tạm thời Y của Bob Payload Noise: khối tùy chọn 16 byte Payload không phải Noise: Padding ngẫu nhiên

(Thuộc tính Bảo mật Payload từ [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs): Authentication Confidentiality

<- e, ee 2 1

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 1. Encryption to an ephemeral recipient. This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee"). However, the sender has not authenticated the recipient, so this payload might be sent to any party, including an active attacker.

    "e": Bob generates a new ephemeral key pair and stores it in the e variable, writes the ephemeral public key as cleartext into the message buffer, and hashes the public key along with the old h to derive a new h.

    "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Giá trị Y được mã hóa để đảm bảo tính không thể phân biệt và tính duy nhất của payload, điều này là cần thiết cho các biện pháp chống DPI. Chúng tôi sử dụng mã hóa AES để đạt được điều này, thay vì các phương án phức tạp và chậm hơn như elligator2. Mã hóa bất đối xứng với khóa công khai của router Alice sẽ quá chậm. Mã hóa AES sử dụng hash của router Bob làm khóa và trạng thái AES từ message 1 (đã được khởi tạo với IV của Bob như được công bố trong netDb).

Mã hóa AES chỉ dành để chống DPI. Bất kỳ bên nào biết router hash và IV của Bob, được công bố trong cơ sở dữ liệu mạng, và chặn được 32 byte đầu tiên của thông điệp 1, đều có thể giải mã giá trị Y trong thông điệp này.

Nội dung thô:

```
+----+----+----+----+----+----+----+----+

|                                       |

    + obfuscated with RH_B + | AES-CBC-256 encrypted Y | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | ChaChaPoly frame | + Encrypted and authenticated data + | 32 bytes | + k defined in KDF for message 2 + | n = 0; see KDF for associated data | + + | | +----+----+----+----+----+----+----+----+ | unencrypted authenticated | + padding (optional) + | length defined in options block | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    Y :: 32 bytes, AES-256-CBC encrypted X25519 ephemeral key, little endian

    :   key: RH_B iv: Using AES state from message 1
```
Dữ liệu không được mã hóa (thẻ xác thực Poly1305 không được hiển thị):

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | Y | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | options | + (16 bytes) + | | +----+----+----+----+----+----+----+----+ | unencrypted authenticated | + padding (optional) + | length defined in options block | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    Y :: 32 bytes, X25519 ephemeral key, little endian

    options :: options block, 16 bytes, see below

    padding :: Random data, 0 or more bytes.

    :   Total message length must be 65535 bytes or less. Alice and Bob will use the padding data in the KDF for message 3 part 1. It is authenticated so that any tampering will cause the next message to fail.
```
#### Ghi chú

- Alice phải xác thực rằng khóa tạm thời của Bob là một điểm hợp lệ trên đường cong ở đây.
- Padding nên được giới hạn trong một lượng hợp lý. Alice có thể từ chối các kết nối có padding quá mức. Alice sẽ chỉ định các tùy chọn padding của mình trong thông điệp 3. Hướng dẫn min/max sẽ được xác định sau. Kích thước ngẫu nhiên từ 0 đến 31 byte tối thiểu? (Phân phối phụ thuộc vào việc triển khai)
- Khi có bất kỳ lỗi nào, bao gồm AEAD, DH, timestamp, replay có vẻ rõ ràng, hoặc lỗi xác thực khóa, Alice phải dừng xử lý thông điệp tiếp theo và đóng kết nối mà không phản hồi. Đây nên là một đóng kết nối bất thường (TCP RST).
- Để tạo điều kiện cho việc bắt tay nhanh chóng, các triển khai phải đảm bảo rằng Bob đệm và sau đó flush toàn bộ nội dung của thông điệp đầu tiên cùng một lúc, bao gồm cả padding. Điều này tăng khả năng dữ liệu sẽ được chứa trong một gói TCP duy nhất (trừ khi bị phân đoạn bởi OS hoặc middlebox), và được Alice nhận tất cả cùng một lúc. Điều này cũng nhằm mục đích hiệu quả và đảm bảo tính hiệu quả của padding ngẫu nhiên.
- Alice phải thất bại kết nối nếu bất kỳ dữ liệu đến nào còn lại sau khi xác thực thông điệp 2 và đọc padding. Không nên có dữ liệu bổ sung nào từ Bob, vì Alice chưa phản hồi với thông điệp 3.

Khối tùy chọn: Lưu ý: Tất cả các trường đều theo thứ tự big-endian.

```
+----+----+----+----+----+----+----+----+

| Rsvd(0) | padLen | Reserved (0) |

    +-------------------------------+-------------------------------+
    | > tsB                         | > Reserved (0)                |
    +-------------------------------+-------------------------------+

    Reserved :: 10 bytes total, set to 0 for compatibility with future options

    padLen :: 2 bytes, big endian, length of the padding, 0 or more

    :   Min/max guidelines TBD. Random size from 0 to 31 bytes minimum? (Distribution is implementation-dependent)

    tsB :: 4 bytes, big endian, Unix timestamp, unsigned seconds.

    :   Wraps around in 2106
```
#### Ghi chú

- Alice phải từ chối các kết nối có giá trị timestamp quá xa so với thời gian hiện tại. Gọi khoảng thời gian tối đa là "D". Alice phải duy trì một bộ nhớ đệm cục bộ các giá trị handshake đã sử dụng trước đó và từ chối các giá trị trùng lặp, để ngăn chặn các cuộc tấn công replay. Các giá trị trong bộ nhớ đệm phải có thời gian tồn tại ít nhất 2*D. Các giá trị bộ nhớ đệm phụ thuộc vào cách triển khai, tuy nhiên có thể sử dụng giá trị Y 32-byte (hoặc tương đương đã mã hóa của nó).

#### Vấn đề

- Bao gồm các tùy chọn padding tối thiểu/tối đa ở đây?

### Mã hóa cho phần 1 của thông điệp handshake 3, sử dụng KDF của thông điệp 2)

```
// take h saved from message 2 KDF
// MixHash(ciphertext)
h = SHA256(h || 24 byte encrypted payload from message 2)

// MixHash(padding)
// Only if padding length is nonzero
h = SHA256(h || random padding from message 2)
// h is used as the associated data for the AEAD in message 3 part 1, below

This is the "s" message pattern:

Define s = Alice's static public key, 32 bytes

// EncryptAndHash(s.publickey)
// EncryptWithAd(h, s.publickey)
// AEAD_ChaCha20_Poly1305(key, nonce, associatedData, data)
// k is from handshake message 1
// n is 1
ciphertext = AEAD_ChaCha20_Poly1305(k, n++, h, s.publickey)
// MixHash(ciphertext)
// || below means append
h = SHA256(h || ciphertext);

// h is used as the associated data for the AEAD in message 3 part 2

End of "s" message pattern.
```
### Hàm Tạo Khóa (KDF) (cho phần 2 của thông điệp bắt tay thứ 3)

```
This is the "se" message pattern:

// DH(s, re) == DH(e, rs) Define input_key_material = 32 byte DH result of Alice's static key and Bob's ephemeral key Set input_key_material = X25519 DH result // overwrite Bob's ephemeral key in memory, no longer needed // Alice: re = (all zeros) // Bob: e(public and private) = (all zeros)

// MixKey(DH())

Define temp_key = 32 bytes Define HMAC-SHA256(key, data) as in [RFC-2104](https://tools.ietf.org/html/rfc2104) // Generate a temp key from the chaining key and DH result // ck is the chaining key, from the KDF for handshake message 1 temp_key = HMAC-SHA256(ck, input_key_material) // overwrite the DH result in memory, no longer needed input_key_material = (all zeros)

// Output 1 // Set a new chaining key from the temp key // byte() below means a single byte ck = HMAC-SHA256(temp_key, byte(0x01)).

// Output 2 // Generate the cipher key k Define k = 32 bytes // || below means append // byte() below means a single byte k = HMAC-SHA256(temp_key, ck || byte(0x02)).

// h from message 3 part 1 is used as the associated data for the AEAD in message 3 part 2

// EncryptAndHash(payload) // EncryptWithAd(h, payload) // AEAD_ChaCha20_Poly1305(key, nonce, associatedData, data) // n is 0 ciphertext = AEAD_ChaCha20_Poly1305(k, n++, h, payload) // MixHash(ciphertext) // || below means append h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF // retain the hash h for the data phase Additional Symmetric Key (SipHash) KDF

End of "se" message pattern.

// overwrite the temp_key in memory, no longer needed temp_key = (all zeros)
```
### 3) SessionConfirmed

Alice gửi cho Bob.

Nội dung Noise: khóa tĩnh của Alice Tải trọng Noise: RouterInfo của Alice và padding ngẫu nhiên Tải trọng không phải Noise: không có

(Thuộc tính Bảo mật Payload từ [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs): Authentication Confidentiality

-> s, se 2 5

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 5. Encryption to a known recipient, strong forward secrecy. This payload is encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static DH with the recipient's static key pair. Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated by an attacker that has stolen its static private key, this payload cannot be decrypted.

    "s": Alice writes her static public key from the s variable into the message buffer, encrypting it, and hashes the output along with the old h to derive a new h.

    "se": A DH is performed between the Alice's static key pair and the Bob's ephemeral key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Điều này chứa hai ChaChaPoly frame. Frame đầu tiên là static public key được mã hóa của Alice. Frame thứ hai là Noise payload: RouterInfo được mã hóa của Alice, các tùy chọn tùy ý, và padding tùy ý. Chúng sử dụng các key khác nhau, vì hàm MixKey() được gọi ở giữa.

Nội dung thô:

```
+----+----+----+----+----+----+----+----+

|                                       |

    + ChaChaPoly frame (48 bytes) + | Encrypted and authenticated | + Alice static key S + | (32 bytes) | + + | k defined in KDF for message 2 | + n = 1 + | see KDF for associated data | + + | | +----+----+----+----+----+----+----+----+ | | + Length specified in message 1 + | | + ChaChaPoly frame + | Encrypted and authenticated | + + | Alice RouterInfo | + using block format 2 + | Alice Options (optional) | + using block format 1 + | Arbitrary padding | + using block format 254 + | | + + | k defined in KDF for message 3 part 2 | + n = 0 + | see KDF for associated data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    S :: 32 bytes, ChaChaPoly encrypted Alice's X25519 static key, little endian

    :   inside 48 byte ChaChaPoly frame
```
Dữ liệu không mã hóa (không hiển thị thẻ xác thực Poly1305):

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | S | + Alice static key + | (32 bytes) | + + | | + + +----+----+----+----+----+----+----+----+ | | + + | | + + | Alice RouterInfo block | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | | + Optional Options block + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | | + Optional Padding block + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    S :: 32 bytes, Alice's X25519 static key, little endian
```
#### Ghi chú

- Bob phải thực hiện xác thực Router Info thông thường. Đảm bảo loại chữ ký được hỗ trợ, xác minh chữ ký, xác minh timestamp nằm trong phạm vi cho phép, và bất kỳ kiểm tra nào khác cần thiết.

- Bob phải xác minh rằng khóa tĩnh của Alice nhận được trong frame đầu tiên khớp với khóa tĩnh trong Router Info. Bob trước tiên phải tìm kiếm trong Router Info một NTCP hoặc NTCP2 Router Address với tùy chọn phiên bản (v) khớp. Xem các phần Published Router Info và Unpublished Router Info bên dưới.

- Nếu Bob có phiên bản cũ hơn của RouterInfo của Alice trong netdb của mình, hãy xác minh rằng static key trong router info là giống nhau ở cả hai, nếu có, và nếu phiên bản cũ hơn ít hơn XXX tuổi (xem thời gian xoay key bên dưới)

- Bob phải xác thực rằng khóa tĩnh của Alice là một điểm hợp lệ trên đường cong tại đây.

- Các tùy chọn nên được bao gồm để xác định các tham số padding.

- Khi xảy ra bất kỳ lỗi nào, bao gồm lỗi AEAD, RI, DH, timestamp, hoặc lỗi xác thực khóa, Bob phải dừng xử lý tin nhắn và đóng kết nối mà không phản hồi. Đây phải là một lần đóng bất thường (TCP RST).

- Để tạo điều kiện thuận lợi cho quá trình bắt tay nhanh chóng, các triển khai phải đảm bảo rằng Alice đệm và sau đó xả toàn bộ nội dung của thông điệp thứ ba cùng một lúc, bao gồm cả hai khung AEAD. Điều này tăng khả năng dữ liệu sẽ được chứa trong một gói TCP duy nhất (trừ khi bị phân đoạn bởi hệ điều hành hoặc middlebox), và được Bob nhận tất cả cùng một lúc. Điều này cũng nhằm mục đích hiệu quả và đảm bảo tính hiệu quả của việc đệm ngẫu nhiên.

- Độ dài frame của Message 3 phần 2: Độ dài của frame này (bao gồm MAC) được Alice gửi trong message 1. Xem message đó để biết các lưu ý quan trọng về việc dành đủ chỗ cho padding.

- Nội dung frame phần 2 của Message 3: Định dạng của frame này giống với định dạng của các frame pha dữ liệu, ngoại trừ độ dài của frame được Alice gửi trong message 1. Xem bên dưới để biết định dạng frame pha dữ liệu. Frame phải chứa từ 1 đến 3 block theo thứ tự sau:

1)  Khối Router Info của Alice (bắt buộc)   2)  Khối Options (tùy chọn)

3\) Khối padding (tùy chọn) Frame này không bao giờ được chứa bất kỳ loại khối nào khác.

- Phần đệm của Message 3 part 2 không bắt buộc nếu Alice thêm một data phase frame (tùy chọn chứa đệm) vào cuối message 3 và gửi cả hai cùng một lúc, vì điều này sẽ xuất hiện như một luồng byte lớn đối với người quan sát. Vì Alice thường, nhưng không phải lúc nào cũng, có một I2NP message để gửi cho Bob (đó là lý do cô ấy kết nối với anh ấy), đây là cách triển khai được khuyến nghị, vì hiệu quả và để đảm bảo tính hiệu quả của phần đệm ngẫu nhiên.

- Tổng độ dài của cả hai khung AEAD Message 3 (phần 1 và phần 2) là 65535 byte; phần 1 là 48 byte nên độ dài khung tối đa của phần 2 là 65487; độ dài plaintext tối đa của phần 2 không bao gồm MAC là 65471.

### Hàm Tạo Khóa (KDF) (cho giai đoạn dữ liệu)

Giai đoạn dữ liệu sử dụng đầu vào dữ liệu liên kết có độ dài bằng không.

KDF tạo ra hai cipher key k_ab và k_ba từ chaining key ck, sử dụng HMAC-SHA256(key, data) như được định nghĩa trong [RFC-2104](https://tools.ietf.org/html/rfc2104). Đây là hàm Split(), được định nghĩa chính xác như trong đặc tả Noise.

```
ck = from handshake phase

// k_ab, k_ba = HKDF(ck, zerolen) // ask_master = HKDF(ck, zerolen, info="ask")

// zerolen is a zero-length byte array temp_key = HMAC-SHA256(ck, zerolen) // overwrite the chaining key in memory, no longer needed ck = (all zeros)

// Output 1 // cipher key, for Alice transmits to Bob (Noise doesn't make clear which is which, but Java code does) k_ab = HMAC-SHA256(temp_key, byte(0x01)).

// Output 2 // cipher key, for Bob transmits to Alice (Noise doesn't make clear which is which, but Java code does) k_ba = HMAC-SHA256(temp_key, k_ab || byte(0x02)).

KDF for SipHash for length field: Generate an Additional Symmetric Key (ask) for SipHash SipHash uses two 8-byte keys (big endian) and 8 byte IV for first data.

// "ask" is 3 bytes, US-ASCII, no null termination ask_master = HMAC-SHA256(temp_key, "ask" || byte(0x01)) // sip_master = HKDF(ask_master, h || "siphash") // "siphash" is 7 bytes, US-ASCII, no null termination // overwrite previous temp_key in memory // h is from KDF for message 3 part 2 temp_key = HMAC-SHA256(ask_master, h || "siphash") // overwrite ask_master in memory, no longer needed ask_master = (all zeros) sip_master = HMAC-SHA256(temp_key, byte(0x01))

Alice to Bob SipHash k1, k2, IV: // sipkeys_ab, sipkeys_ba = HKDF(sip_master, zerolen) // overwrite previous temp_key in memory temp_key = HMAC-SHA256(sip_master, zerolen) // overwrite sip_master in memory, no longer needed sip_master = (all zeros)

sipkeys_ab = HMAC-SHA256(temp_key, byte(0x01)). sipk1_ab = sipkeys_ab[0:7], little endian sipk2_ab = sipkeys_ab[8:15], little endian sipiv_ab = sipkeys_ab[16:23]

Bob to Alice SipHash k1, k2, IV:

sipkeys_ba = HMAC-SHA256(temp_key, sipkeys_ab || byte(0x02)). sipk1_ba = sipkeys_ba[0:7], little endian sipk2_ba = sipkeys_ba[8:15], little endian sipiv_ba = sipkeys_ba[16:23]

// overwrite the temp_key in memory, no longer needed temp_key = (all zeros)
```
### 4) Giai đoạn Dữ liệu

Noise payload: Như được định nghĩa bên dưới, bao gồm random padding Non-noise payload: không có

Bắt đầu từ phần thứ 2 của thông điệp 3, tất cả các thông điệp đều nằm bên trong một "khung" ChaChaPoly được xác thực và mã hóa với độ dài bị làm rối hai byte ở đầu. Tất cả padding đều nằm bên trong khung. Bên trong khung là một định dạng chuẩn với không hoặc nhiều "khối". Mỗi khối có một loại một byte và độ dài hai byte. Các loại bao gồm ngày/giờ, thông điệp I2NP, tùy chọn, kết thúc và padding.

Lưu ý: Bob có thể, nhưng không bắt buộc, gửi RouterInfo của mình cho Alice như tin nhắn đầu tiên gửi cho Alice trong giai đoạn dữ liệu.

(Thuộc tính Bảo mật Payload từ [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs): Authentication Confidentiality

<- 2 5 -> 2 5

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 5. Encryption to a known recipient, strong forward secrecy. This payload is encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static DH with the recipient's static key pair. Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### Ghi chú

- Để đảm bảo hiệu quả và giảm thiểu việc xác định trường độ dài, các implementation phải đảm bảo rằng bên gửi đệm và sau đó flush toàn bộ nội dung của thông điệp dữ liệu cùng một lúc, bao gồm trường độ dài và AEAD frame. Điều này tăng khả năng dữ liệu sẽ được chứa trong một TCP packet duy nhất (trừ khi bị phân đoạn bởi OS hoặc middleboxes), và được bên kia nhận tất cả cùng một lúc. Điều này cũng nhằm mục đích hiệu quả và đảm bảo tính hiệu quả của random padding.
- Router có thể chọn chấm dứt session khi có lỗi AEAD, hoặc có thể tiếp tục cố gắng liên lạc. Nếu tiếp tục, router nên chấm dứt sau các lỗi lặp lại.

#### SipHash độ dài được làm rối

Tham khảo: [SipHash](https://www.131002.net/siphash/)

Sau khi cả hai bên đã hoàn thành quá trình bắt tay, chúng truyền tải các payload sau đó được mã hóa và xác thực trong các "khung" ChaChaPoly.

Mỗi frame được đặt trước bởi độ dài hai byte, big endian. Độ dài này chỉ định số byte frame được mã hóa sẽ theo sau, bao gồm cả MAC. Để tránh truyền các trường độ dài có thể nhận dạng được trong stream, độ dài frame được làm mờ bằng cách XOR với một mask được tạo từ SipHash, như được khởi tạo từ KDF giai đoạn dữ liệu. Lưu ý rằng hai hướng có các khóa SipHash và IV riêng biệt từ KDF.

```
sipk1, sipk2 = The SipHash keys from the KDF.  (two 8-byte long integers)
    IV[0] = sipiv = The SipHash IV from the KDF. (8 bytes)
    length is big endian.
    For each frame:
      IV[n] = SipHash-2-4(sipk1, sipk2, IV[n-1])
      Mask[n] = First 2 bytes of IV[n]
      obfuscatedLength = length ^ Mask[n]

    The first length output will be XORed with with IV[1].
```
Bên nhận có các khóa SipHash và IV giống hệt nhau. Việc giải mã độ dài được thực hiện bằng cách dẫn xuất mask được sử dụng để che giấu độ dài và thực hiện phép XOR với digest đã cắt ngắn để thu được độ dài của frame. Độ dài frame là tổng độ dài của frame đã mã hóa bao gồm cả MAC.

#### Ghi chú

- Nếu bạn sử dụng một hàm thư viện SipHash trả về một số nguyên long không dấu, hãy sử dụng hai byte ít quan trọng nhất làm Mask. Chuyển đổi số nguyên long thành IV tiếp theo dưới dạng little endian.

#### Nội dung thô

```
+----+----+----+----+----+----+----+----+

[|obf size |](##SUBST##|obf size |) | +----+----+ + | | + ChaChaPoly frame + | Encrypted and authenticated | + key is k_ab for Alice to Bob + | key is k_ba for Bob to Alice | + as defined in KDF for data phase + | n starts at 0 and increments | + for each frame in that direction + | no associated data | + 16 bytes minimum + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    obf size :: 2 bytes length obfuscated with SipHash

    :   when de-obfuscated: 16 - 65535

    Minimum size including length field is 18 bytes. Maximum size including length field is 65537 bytes. Obfuscated length is 2 bytes. Maximum ChaChaPoly frame is 65535 bytes.
```
#### Ghi chú

- Vì bên nhận phải lấy toàn bộ frame để kiểm tra MAC, khuyến nghị bên gửi giới hạn frame ở vài KB thay vì tối đa hóa kích thước frame. Điều này sẽ giảm thiểu độ trễ tại bên nhận.

#### Dữ liệu chưa mã hóa

Có từ không đến nhiều block trong frame được mã hóa. Mỗi block chứa một định danh một byte, độ dài hai byte, và từ không đến nhiều byte dữ liệu.

Để đảm bảo khả năng mở rộng, bên nhận phải bỏ qua các block có định danh không xác định và xử lý chúng như padding.

Dữ liệu được mã hóa tối đa 65535 bytes, bao gồm header xác thực 16-byte, vì vậy dữ liệu chưa mã hóa tối đa là 65519 bytes.

(Thẻ xác thực Poly1305 không được hiển thị):

```
+----+----+----+----+----+----+----+----+

[|blk |](##SUBST##|blk |) size | data | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ [|blk |](##SUBST##|blk |) size | data | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ ~ . . . ~

    blk :: 1 byte

    :   0 for datetime 1 for options 2 for RouterInfo 3 for I2NP message 4 for termination 224-253 reserved for experimental features 254 for padding 255 reserved for future extension

    size :: 2 bytes, big endian, size of data to follow, 0 - 65516 data :: the data

    Maximum ChaChaPoly frame is 65535 bytes. Poly1305 tag is 16 bytes Maximum total block size is 65519 bytes Maximum single block size is 65519 bytes Block type is 1 byte Block length is 2 bytes Maximum single block data size is 65516 bytes.
```
#### Quy tắc sắp xếp khối

Trong phần 2 của thông điệp handshake 3, thứ tự phải là: RouterInfo, theo sau là Options nếu có, theo sau là Padding nếu có. Không được phép có các khối khác.

Trong giai đoạn dữ liệu, thứ tự không được xác định cụ thể, ngoại trừ các yêu cầu sau: Padding, nếu có, phải là khối cuối cùng. Termination, nếu có, phải là khối cuối cùng ngoại trừ Padding.

Có thể có nhiều khối I2NP trong một frame duy nhất. Không được phép có nhiều khối Padding trong một frame duy nhất. Các loại khối khác có thể sẽ không có nhiều khối trong một frame duy nhất, nhưng điều này không bị cấm.

#### Ngày giờ

Trường hợp đặc biệt cho đồng bộ hóa thời gian:

```
+----+----+----+----+----+----+----+

| 0 | 4 | timestamp |

    +----+----+----+----+----+----+----+

    blk :: 0 size :: 2 bytes, big endian, value = 4 timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106
```
LƯU Ý: Các triển khai phải làm tròn đến giây gần nhất để ngăn chặn độ lệch đồng hồ trong mạng.

#### Tùy chọn

Truyền các tùy chọn đã cập nhật. Các tùy chọn bao gồm: Padding tối thiểu và tối đa.

Khối tùy chọn sẽ có độ dài thay đổi.

```
+----+----+----+----+----+----+----+----+

| 1 | size [|tmin|](##SUBST##|tmin|)tmax[|rmin|](##SUBST##|rmin|)rmax[|tdmy|](##SUBST##|tdmy|)

    +----+----+----+----+----+----+----+----+ [|tdmy|](##SUBST##|tdmy|) rdmy | tdelay | rdelay | | ~----+----+----+----+----+----+----+ ~ | more_options | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 1 size :: 2 bytes, big endian, size of options to follow, 12 bytes minimum

    tmin, tmax, rmin, rmax :: requested padding limits

    :   tmin and rmin are for desired resistance to traffic analysis. tmax and rmax are for bandwidth limits. tmin and tmax are the transmit limits for the router sending this options block. rmin and rmax are the receive limits for the router sending this options block. Each is a 4.4 fixed-point float representing 0 to 15.9375 (or think of it as an unsigned 8-bit integer divided by 16.0). This is the ratio of padding to data. Examples: Value of 0x00 means no padding Value of 0x01 means add 6 percent padding Value of 0x10 means add 100 percent padding Value of 0x80 means add 800 percent (8x) padding Alice and Bob will negotiate the minimum and maximum in each direction. These are guidelines, there is no enforcement. Sender should honor receiver's maximum. Sender may or may not honor receiver's minimum, within bandwidth constraints.

    tdmy: Max dummy traffic willing to send, 2 bytes big endian, bytes/sec average rdmy: Requested dummy traffic, 2 bytes big endian, bytes/sec average tdelay: Max intra-message delay willing to insert, 2 bytes big endian, msec average rdelay: Requested intra-message delay, 2 bytes big endian, msec average

    Padding distribution specified as additional parameters? Random delay specified as additional parameters?

    more_options :: Format TBD
```
#### Vấn đề về Tùy chọn

- Định dạng tùy chọn đang được xác định.
- Đàm phán tùy chọn đang được xác định.

#### RouterInfo

Truyền RouterInfo của Alice cho Bob. Được sử dụng trong thông điệp bắt tay phần 3 mục 2. Truyền RouterInfo của Alice cho Bob, hoặc của Bob cho Alice. Được sử dụng tùy chọn trong giai đoạn dữ liệu.

```
+----+----+----+----+----+----+----+----+

| 2 | size [|flg |](##SUBST##|flg |) RouterInfo |

    +----+----+----+----+ + | (Alice RI in handshake msg 3 part 2) | ~ (Alice, Bob, or third-party ~ | RI in data phase) | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 2 size :: 2 bytes, big endian, size of flag + router info to follow flg :: 1 byte flags bit order: 76543210 bit 0: 0 for local store, 1 for flood request bits 7-1: Unused, set to 0 for future compatibility routerinfo :: Alice's or Bob's RouterInfo
```
#### Ghi chú

- Khi được sử dụng trong giai đoạn dữ liệu, bên nhận (Alice hoặc Bob) phải xác thực rằng đó là cùng một Router Hash như đã được gửi ban đầu (đối với Alice) hoặc được gửi tới (đối với Bob). Sau đó, xử lý nó như một I2NP DatabaseStore Message cục bộ. Xác thực chữ ký, xác thực timestamp gần đây hơn, và lưu trữ trong netDb cục bộ. Nếu bit cờ 0 là 1, và bên nhận là floodfill, xử lý nó như một DatabaseStore Message với reply token khác không, và flood nó đến các floodfill gần nhất.
- Router Info KHÔNG được nén với gzip (khác với trong DatabaseStore Message, nơi nó được nén)
- Flooding không được yêu cầu trừ khi có các RouterAddress được công bố trong RouterInfo. Router nhận không được flood RouterInfo trừ khi có các RouterAddress được công bố trong đó.
- Các nhà phát triển phải đảm bảo rằng khi đọc một block, dữ liệu bị hỏng hoặc độc hại sẽ không gây ra việc đọc tràn vào block tiếp theo.
- Giao thức này không cung cấp xác nhận rằng RouterInfo đã được nhận, lưu trữ, hoặc flood (cả trong giai đoạn handshake hoặc data). Nếu cần xác nhận, và bên nhận là floodfill, bên gửi nên gửi một I2NP DatabaseStoreMessage tiêu chuẩn với reply token thay thế.

#### Vấn đề

- Cũng có thể được sử dụng trong giai đoạn dữ liệu, thay vì I2NP DatabaseStoreMessage. Ví dụ, Bob có thể sử dụng nó để bắt đầu giai đoạn dữ liệu.
- Liệu có được phép chứa RI cho các router khác ngoài người khởi tạo không, như một sự thay thế chung cho DatabaseStoreMessages, ví dụ như để flooding bởi floodfills?

#### I2NP Message

Một thông điệp I2NP đơn lẻ với header đã được chỉnh sửa. Các thông điệp I2NP không được phân mảnh qua các khối hoặc qua các khung ChaChaPoly.

Cách này sử dụng 9 byte đầu tiên từ header I2NP NTCP tiêu chuẩn, và loại bỏ 7 byte cuối của header, như sau: rút ngắn thời gian hết hạn từ 8 xuống 4 byte (giây thay vì mili giây, giống như đối với SSU), loại bỏ độ dài 2 byte (sử dụng kích thước block - 9), và loại bỏ checksum SHA256 một byte.

```
+----+----+----+----+----+----+----+----+

| 3 | size [|type|](##SUBST##|type|) msg id |

    +-------------------------------+
    | > short exp                   |
    +-------------------------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 3 size :: 2 bytes, big endian, size of type + msg id + exp + message to follow I2NP message body size is (size - 9). type :: 1 byte, I2NP msg type, see I2NP spec msg id :: 4 bytes, big endian, I2NP message ID short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds. Wraps around in 2106 message :: I2NP message body
```
#### Ghi chú

- Người triển khai phải đảm bảo rằng khi đọc một khối, dữ liệu bị lỗi hoặc độc hại sẽ không gây ra việc đọc vượt quá giới hạn sang khối tiếp theo.

#### Kết thúc

Noise khuyến nghị sử dụng thông điệp kết thúc rõ ràng. NTCP gốc không có thông điệp này. Ngắt kết nối. Đây phải là khối không phải padding cuối cùng trong frame.

```
+----+----+----+----+----+----+----+----+

| 4 | size | valid data frames |

    +----+----+----+----+----+----+----+----+

    :   received | rsn| addl data |

    +----+----+----+----+ + ~ . . . ~ +----+----+----+----+----+----+----+----+

    blk :: 4 size :: 2 bytes, big endian, value = 9 or more valid data frames received :: The number of valid AEAD data phase frames received (current receive nonce value) 0 if error occurs in handshake phase 8 bytes, big endian rsn :: reason, 1 byte: 0: normal close or unspecified 1: termination received 2: idle timeout 3: router shutdown 4: data phase AEAD failure 5: incompatible options 6: incompatible signature type 7: clock skew 8: padding violation 9: AEAD framing error 10: payload format error 11: message 1 error 12: message 2 error 13: message 3 error 14: intra-frame read timeout 15: RI signature verification fail 16: s parameter missing, invalid, or mismatched in RouterInfo 17: banned addl data :: optional, 0 or more bytes, for future expansion, debugging, or reason text. Format unspecified and may vary based on reason code.
```
#### Ghi chú

Không phải tất cả các lý do đều thực sự được sử dụng, tùy thuộc vào cách triển khai. Các lỗi handshake thường sẽ dẫn đến việc đóng kết nối bằng TCP RST thay thế. Xem ghi chú trong các phần thông điệp handshake ở trên. Các lý do bổ sung được liệt kê là để đảm bảo tính nhất quán, ghi log, gỡ lỗi, hoặc nếu chính sách thay đổi.

#### Padding

Đây là để đệm bên trong các khung AEAD. Đệm cho thông điệp 1 và 2 nằm bên ngoài các khung AEAD. Tất cả đệm cho thông điệp 3 và giai đoạn dữ liệu đều nằm bên trong các khung AEAD.

Padding bên trong AEAD nên tuân thủ gần đúng các tham số đã được thỏa thuận. Bob đã gửi các tham số tx/rx min/max mà anh ấy yêu cầu trong thông điệp 2. Alice đã gửi các tham số tx/rx min/max mà cô ấy yêu cầu trong thông điệp 3. Các tùy chọn cập nhật có thể được gửi trong giai đoạn dữ liệu. Xem thông tin khối tùy chọn ở trên.

Nếu có, đây phải là khối cuối cùng trong frame.

```
+----+----+----+----+----+----+----+----+

[|254 |](##SUBST##|254 |) size | padding | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 254 size :: 2 bytes, big endian, size of padding to follow padding :: random data
```
#### Ghi chú

- Size = 0 được cho phép.
- Các chiến lược padding chưa được xác định.
- Padding tối thiểu chưa được xác định.
- Các frame chỉ có padding được cho phép.
- Padding mặc định chưa được xác định.
- Xem khối options để đàm phán tham số padding
- Xem khối options cho các tham số padding min/max
- Noise giới hạn tin nhắn ở 64KB. Nếu cần thêm padding, hãy gửi nhiều frame.
- Phản hồi của router khi vi phạm padding đã đàm phán tùy thuộc vào cách triển khai.

#### Các loại khối khác

Các implementation nên bỏ qua các loại block không xác định để đảm bảo tương thích với phiên bản mới, ngoại trừ trong message 3 part 2, nơi mà các block không xác định không được phép.

#### Công việc tương lai

- Độ dài padding sẽ được quyết định trên cơ sở từng thông điệp và ước tính phân bố độ dài, hoặc nên thêm độ trễ ngẫu nhiên. Những biện pháp đối phó này cần được bao gồm để chống lại DPI, vì kích thước thông điệp có thể tiết lộ rằng lưu lượng I2P đang được truyền tải bởi giao thức vận chuyển. Lược đồ padding chính xác là một lĩnh vực nghiên cứu trong tương lai.

### 5) Chấm dứt

Các kết nối có thể được chấm dứt thông qua đóng socket TCP bình thường hoặc bất thường, hoặc như Noise khuyến nghị, thông qua một thông điệp chấm dứt rõ ràng. Thông điệp chấm dứt rõ ràng được định nghĩa trong giai đoạn dữ liệu ở trên.

Khi có bất kỳ sự kết thúc bình thường hoặc bất thường nào, các router nên xóa sạch mọi dữ liệu tạm thời trong bộ nhớ, bao gồm các khóa tạm thời của handshake, khóa mã hóa đối xứng, và thông tin liên quan.

## Thông Tin Router Đã Xuất Bản

### Khả năng

Từ phiên bản 0.9.50, tùy chọn "caps" được hỗ trợ trong các địa chỉ NTCP2, tương tự như SSU. Một hoặc nhiều khả năng có thể được công bố trong tùy chọn "caps". Các khả năng có thể được sắp xếp theo bất kỳ thứ tự nào, nhưng "46" là thứ tự được khuyến nghị, để đảm bảo tính nhất quán giữa các triển khai. Có hai khả năng được định nghĩa:

4: Cho biết khả năng IPv4 outbound. Nếu một IP được công bố trong trường host, khả năng này không cần thiết. Nếu router bị ẩn, hoặc NTCP2 chỉ là outbound, '4' và '6' có thể được kết hợp trong một địa chỉ duy nhất.

6: Chỉ ra khả năng IPv6 outbound. Nếu một IP được công bố trong trường host, khả năng này không cần thiết. Nếu router ẩn, hoặc NTCP2chỉ outbound, '4' và '6' có thể được kết hợp trong một địa chỉ duy nhất.

### Địa chỉ đã công bố

RouterAddress được công bố (một phần của RouterInfo) sẽ có một định danh giao thức là "NTCP" hoặc "NTCP2".

RouterAddress phải chứa các tùy chọn "host" và "port", như trong giao thức NTCP hiện tại.

RouterAddress phải chứa ba tùy chọn để chỉ ra hỗ trợ NTCP2:

- s=(Base64 key) Khóa công khai tĩnh Noise hiện tại (s) cho RouterAddress này. Được mã hóa Base 64 sử dụng bảng chữ cái I2P Base 64 tiêu chuẩn. 32 byte ở dạng nhị phân, 44 byte khi được mã hóa Base 64, khóa công khai X25519 little-endian.
- i=(Base64 IV) IV hiện tại để mã hóa giá trị X trong tin nhắn 1 cho RouterAddress này. Được mã hóa Base 64 sử dụng bảng chữ cái I2P Base 64 tiêu chuẩn. 16 byte ở dạng nhị phân, 24 byte khi được mã hóa Base 64, big-endian.
- v=2 Phiên bản hiện tại (2). Khi được xuất bản dưới dạng "NTCP", việc hỗ trợ bổ sung cho phiên bản 1 được ngụ ý. Hỗ trợ cho các phiên bản tương lai sẽ có các giá trị phân tách bằng dấu phẩy, ví dụ v=2,3. Việc triển khai nên xác minh tính tương thích, bao gồm nhiều phiên bản nếu có dấu phẩy. Các phiên bản phân tách bằng dấu phẩy phải theo thứ tự số.

Alice phải xác minh rằng cả ba tùy chọn đều có mặt và hợp lệ trước khi kết nối bằng giao thức NTCP2.

Khi được công bố dưới dạng "NTCP" với các tùy chọn "s", "i", và "v", router phải chấp nhận các kết nối đến trên host và port đó cho cả giao thức NTCP và NTCP2, và tự động phát hiện phiên bản giao thức.

Khi được công bố dưới dạng "NTCP2" với các tùy chọn "s", "i", và "v", router sẽ chấp nhận các kết nối đến trên host và port đó chỉ cho giao thức NTCP2.

Nếu một router hỗ trợ cả kết nối NTCP1 và NTCP2 nhưng không triển khai tính năng phát hiện phiên bản tự động cho các kết nối đến, nó phải quảng bá cả địa chỉ "NTCP" và "NTCP2", và chỉ bao gồm các tùy chọn NTCP2 trong địa chỉ "NTCP2". Router nên đặt giá trị cost thấp hơn (ưu tiên cao hơn) trong địa chỉ "NTCP2" so với địa chỉ "NTCP", để NTCP2 được ưu tiên.

Nếu nhiều NTCP2 RouterAddress (dưới dạng "NTCP" hoặc "NTCP2") được công bố trong cùng một RouterInfo (cho các địa chỉ IP hoặc cổng bổ sung), tất cả các địa chỉ chỉ định cùng một cổng phải chứa các tùy chọn và giá trị NTCP2 giống hệt nhau. Đặc biệt, tất cả phải chứa cùng static key và iv.

### Địa chỉ NTCP2 chưa được công bố

Nếu Alice không công bố địa chỉ NTCP2 của mình (dưới dạng "NTCP" hoặc "NTCP2") cho các kết nối đến, cô ấy phải công bố địa chỉ router "NTCP2" chỉ chứa khóa tĩnh và phiên bản NTCP2 của mình, để Bob có thể xác thực khóa sau khi nhận được RouterInfo của Alice trong thông điệp 3 phần 2.

- s=(Base64 key) Như đã định nghĩa ở trên cho các địa chỉ được công bố.
- v=2 Như đã định nghĩa ở trên cho các địa chỉ được công bố.

Địa chỉ router này sẽ không chứa các tùy chọn "i", "host" hoặc "port", vì chúng không cần thiết cho các kết nối NTCP2 đi ra. Chi phí được công bố cho địa chỉ này không thực sự quan trọng, vì nó chỉ dành cho kết nối đến; tuy nhiên, có thể hữu ích cho các router khác nếu chi phí được đặt cao hơn (ưu tiên thấp hơn) so với các địa chỉ khác. Giá trị được đề xuất là 14.

Alice cũng có thể đơn giản thêm các tùy chọn "s" và "v" vào một địa chỉ "NTCP" đã được công bố hiện có.

### Luân chuyển Public Key và IV

Do việc lưu trữ cache các RouterInfo, các router không được xoay khóa công khai tĩnh hoặc IV khi router đang hoạt động, bất kể có trong địa chỉ được xuất bản hay không. Các router phải lưu trữ bền vững khóa và IV này để tái sử dụng sau khi khởi động lại ngay lập tức, để các kết nối đến sẽ tiếp tục hoạt động và thời gian khởi động lại không bị lộ. Các router phải lưu trữ bền vững hoặc xác định bằng cách khác thời gian tắt máy lần cuối, để có thể tính toán thời gian ngừng hoạt động trước đó khi khởi động.

Tùy thuộc vào mối lo ngại về việc tiết lộ thời gian khởi động lại, các router có thể xoay khóa hoặc IV này khi khởi động nếu router trước đó đã ngừng hoạt động trong một thời gian (ít nhất là vài giờ).

Nếu router có bất kỳ NTCP2 RouterAddresses nào được công bố (dưới dạng NTCP hoặc NTCP2), thời gian ngừng hoạt động tối thiểu trước khi luân chuyển nên dài hơn nhiều, ví dụ một tháng, trừ khi địa chỉ IP cục bộ đã thay đổi hoặc router "rekeys".

Nếu router có bất kỳ SSU RouterAddresses nào được xuất bản, nhưng không có NTCP2 (như NTCP hoặc NTCP2) thì thời gian ngừng hoạt động tối thiểu trước khi xoay vòng nên dài hơn, ví dụ như một ngày, trừ khi địa chỉ IP cục bộ đã thay đổi hoặc router "rekeys". Điều này áp dụng ngay cả khi địa chỉ SSU được xuất bản có introducers.

Nếu router không có bất kỳ RouterAddresses đã xuất bản nào (NTCP, NTCP2, hoặc SSU), thời gian downtime tối thiểu trước khi luân chuyển có thể ngắn chỉ hai giờ, ngay cả khi địa chỉ IP thay đổi, trừ khi router "rekeys".

Nếu router "rekeys" thành một Router Hash khác, nó cũng nên tạo một noise key và IV mới.

Các triển khai phải lưu ý rằng việc thay đổi khóa công khai tĩnh hoặc IV sẽ ngăn chặn các kết nối NTCP2 đến từ các router đã lưu cache RouterInfo cũ. Việc xuất bản RouterInfo, lựa chọn tunnel peer (bao gồm cả OBGW và IB closest hop), lựa chọn zero-hop tunnel, lựa chọn transport, và các chiến lược triển khai khác phải tính đến điều này.

Việc xoay vòng IV tuân theo các quy tắc giống hệt như xoay vòng khóa, ngoại trừ IV chỉ có mặt trong RouterAddresses đã được công bố, do đó không có IV cho các router ẩn hoặc bị firewall. Nếu có bất kỳ thay đổi nào (phiên bản, khóa, tùy chọn?) thì khuyến nghị IV cũng nên được thay đổi.

Lưu ý: Thời gian ngừng hoạt động tối thiểu trước khi tạo lại khóa có thể được điều chỉnh để đảm bảo sức khỏe mạng và ngăn chặn việc reseeding bởi một router ngừng hoạt động trong một khoảng thời gian vừa phải.

## Phát hiện phiên bản

Khi được xuất bản dưới dạng "NTCP", router phải tự động phát hiện phiên bản giao thức cho các kết nối đến.

Việc phát hiện này phụ thuộc vào cách triển khai, nhưng đây là một số hướng dẫn chung.

Để phát hiện phiên bản của một kết nối NTCP đến, Bob thực hiện như sau:

- Đợi ít nhất 64 byte (kích thước tối thiểu của NTCP2 message 1)

- Nếu dữ liệu ban đầu nhận được là 288 byte trở lên, kết nối đến là phiên bản 1.

- Nếu ít hơn 288 byte, thì

> - Đợi một thời gian ngắn để có thêm dữ liệu (chiến lược tốt trước khi NTCP2 được áp dụng rộng rãi) nếu tổng cộng nhận được ít nhất 288, đó là NTCP 1.   >   > - Thử các giai đoạn đầu của việc giải mã như phiên bản 2, nếu thất bại, đợi một thời gian ngắn để có thêm dữ liệu (chiến lược tốt sau khi NTCP2 được áp dụng rộng rãi)   >   >   > - Giải mã 32 byte đầu (khóa X) của gói SessionRequest sử dụng AES-256 với khóa RH_B.   >   > - Xác minh một điểm hợp lệ trên đường cong. Nếu thất bại, đợi một thời gian ngắn để có thêm dữ liệu cho NTCP 1   >   > - Xác minh khung AEAD. Nếu thất bại, đợi một thời gian ngắn để có thêm dữ liệu cho NTCP 1

Lưu ý rằng các thay đổi hoặc chiến lược bổ sung có thể được khuyến nghị nếu chúng tôi phát hiện các cuộc tấn công phân đoạn TCP đang hoạt động trên NTCP 1.

Để tạo thuận lợi cho việc phát hiện phiên bản nhanh chóng và thực hiện handshake, các triển khai phải đảm bảo rằng Alice lưu đệm và sau đó xóa toàn bộ nội dung của thông điệp đầu tiên cùng một lúc, bao gồm cả phần padding. Điều này tăng khả năng dữ liệu sẽ được chứa trong một gói TCP duy nhất (trừ khi bị phân đoạn bởi hệ điều hành hoặc middlebox), và được Bob nhận toàn bộ cùng một lúc. Việc này cũng nhằm mục đích tăng hiệu quả và đảm bảo tính hiệu quả của random padding. Điều này áp dụng cho cả handshake NTCP và NTCP2.

## Các biến thể, phương án dự phòng và vấn đề chung

- Nếu Alice và Bob đều hỗ trợ NTCP2, Alice nên kết nối bằng NTCP2.
- Nếu Alice không thể kết nối tới Bob bằng NTCP2 vì bất kỳ lý do gì, kết nối sẽ thất bại. Alice không được thử lại bằng NTCP 1.

## Hướng dẫn về độ lệch đồng hồ

Timestamp của peer được bao gồm trong hai thông điệp handshake đầu tiên, Session Request và Session Created. Độ lệch đồng hồ giữa hai peer lớn hơn +/- 60 giây thường sẽ gây lỗi nghiêm trọng. Nếu Bob nghĩ rằng đồng hồ cục bộ của mình có vấn đề, anh ta có thể điều chỉnh đồng hồ bằng cách sử dụng độ lệch đã tính toán, hoặc một nguồn bên ngoài. Nếu không, Bob nên phản hồi bằng Session Created ngay cả khi độ lệch tối đa bị vượt quá, thay vì chỉ đơn giản đóng kết nối. Điều này cho phép Alice lấy timestamp của Bob và tính toán độ lệch, và thực hiện hành động nếu cần thiết. Bob không có danh tính router của Alice tại thời điểm này, nhưng để tiết kiệm tài nguyên, có thể Bob muốn cấm các kết nối đến từ IP của Alice trong một khoảng thời gian, hoặc sau các lần thử kết nối lặp đi lặp lại với độ lệch quá mức.

Alice nên điều chỉnh độ lệch đồng hồ đã tính bằng cách trừ đi một nửa RTT. Nếu Alice nghĩ rằng đồng hồ cục bộ của cô ấy có vấn đề, cô ấy có thể điều chỉnh đồng hồ của mình bằng cách sử dụng độ lệch đã tính toán, hoặc một nguồn bên ngoài nào đó. Nếu Alice nghĩ rằng đồng hồ của Bob có vấn đề, cô ấy có thể cấm Bob trong một khoảng thời gian nhất định. Trong cả hai trường hợp, Alice nên đóng kết nối.

Nếu Alice trả lời với Session Confirmed (có thể vì độ lệch đồng hồ rất gần với giới hạn 60s, và các phép tính của Alice và Bob không hoàn toàn giống nhau do RTT), Bob nên điều chỉnh độ lệch đồng hồ đã tính bằng cách trừ đi một nửa RTT. Nếu độ lệch đồng hồ đã điều chỉnh vượt quá mức tối đa, Bob nên trả lời với thông điệp Disconnect chứa mã lý do độ lệch đồng hồ, và đóng kết nối. Tại thời điểm này, Bob có danh tính router của Alice, và có thể cấm Alice trong một khoảng thời gian.

## Tài liệu tham khảo

- [Cấu trúc Chung](/docs/specs/common-structures)
- [I2NP](/docs/specs/i2np)
- [Cơ sở Dữ liệu Mạng](/docs/overview/network-database)
- [NOISE - Khung Giao thức Noise](https://noiseprotocol.org/noise.html)
- [NTCP](/docs/transport/ntcp)
- [Prop104](/proposals/104-tls-transport)
- [Prop109](/proposals/109-pt-transport)
- [Prop111](/proposals/111-ntcp-2)
- [RFC-2104 - HMAC](https://tools.ietf.org/html/rfc2104)
- [RFC-3526 - Nhóm DH](https://tools.ietf.org/html/rfc3526)
- [RFC-6151](https://tools.ietf.org/html/rfc6151)
- [RFC-7539 - ChaCha20-Poly1305](https://tools.ietf.org/html/rfc7539)
- [RFC-7748 - X25519](https://tools.ietf.org/html/rfc7748)
- [RFC-7905](https://tools.ietf.org/html/rfc7905)
- [SipHash](https://www.131002.net/siphash/)
- [SSU](/docs/transport/ssu)
- **[STS]** Diffie, W.; van Oorschot P. C.; Wiener M. J., Xác thực và Trao đổi Khóa được Xác thực
