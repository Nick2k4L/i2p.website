---
title: "Thông điệp Router ECIES-X25519"
description: "Đặc tả cho mã hóa garlic message đến các router ECIES sử dụng X25519"
slug: "ecies-routers"
category: "Giao thức"
lastUpdated: "2025-03"
accurateFor: "0.9.65"
---

## Ghi chú

Được hỗ trợ từ phiên bản 0.9.49. Việc triển khai và kiểm thử mạng đang trong quá trình thực hiện. Có thể có những sửa đổi nhỏ. Xem [đề xuất 156](/proposals/156-ecies-routers).

## Tổng quan

Tài liệu này quy định về mã hóa garlic message tới các ECIES router, sử dụng các nguyên hàm mật mã được giới thiệu bởi [ECIES-X25519](/docs/specs/ecies). Đây là một phần của [đề xuất 156](/proposals/156-ecies-routers) tổng thể để chuyển đổi các router từ khóa ElGamal sang khóa ECIES-X25519. Đặc tả này đã được triển khai từ phiên bản 0.9.49.

Để xem tổng quan về tất cả các thay đổi cần thiết cho router ECIES, hãy xem [đề xuất 156](/proposals/156-ecies-routers). Đối với Garlic Messages đến các đích ECIES-X25519, hãy xem [ECIES-X25519](/docs/specs/ecies).

### Các Thành Phần Mật Mã Cơ Bản

Các thành phần cơ bản cần thiết để triển khai đặc tả này là:

- AES-256-CBC như trong [Cryptography](/docs/specs/cryptography)
- Các hàm STREAM ChaCha20/Poly1305: ENCRYPT(k, n, plaintext, ad) và DECRYPT(k, n, ciphertext, ad) - như trong [NTCP2](/docs/specs/ntcp2), [ECIES-X25519](/docs/specs/ecies), và [RFC-7539](https://tools.ietf.org/html/rfc7539)
- Các hàm X25519 DH - như trong [NTCP2](/docs/specs/ntcp2) và [ECIES-X25519](/docs/specs/ecies)
- HKDF(salt, ikm, info, n) - như trong [NTCP2](/docs/specs/ntcp2) và [ECIES-X25519](/docs/specs/ecies)

Các hàm Noise khác được định nghĩa ở nơi khác:

- MixHash(d) - như trong [NTCP2](/docs/specs/ntcp2) và [ECIES-X25519](/docs/specs/ecies)
- MixKey(d) - như trong [NTCP2](/docs/specs/ntcp2) và [ECIES-X25519](/docs/specs/ecies)

## Thiết kế

ECIES Router SKM không cần một Ratchet SKM đầy đủ như được chỉ định trong [ECIES](/docs/specs/ecies) cho Destinations. Không có yêu cầu cho các thông điệp không ẩn danh sử dụng mẫu IK. Mô hình mối đe dọa không yêu cầu các khóa tạm thời được mã hóa Elligator2.

Do đó, router SKM sẽ sử dụng mẫu Noise "N", giống như được chỉ định trong [Prop152](/proposals/152-ecies-tunnels) để xây dựng tunnel. Nó sẽ sử dụng cùng định dạng payload như được chỉ định trong [ECIES](/docs/specs/ecies) cho các Destinations. Chế độ khóa tĩnh bằng không (không ràng buộc hoặc phiên) của IK được chỉ định trong [ECIES](/docs/specs/ecies) sẽ không được sử dụng.

Các phản hồi cho lookups sẽ được mã hóa bằng ratchet tag nếu được yêu cầu trong lookup. Điều này được ghi lại trong [Prop154](/proposals/154-ecies-lookups), hiện đã được chỉ định trong [I2NP](/docs/specs/i2np).

Thiết kế này cho phép router có một ECIES Session Key Manager duy nhất. Không cần chạy các Session Key Manager "khóa kép" như mô tả trong [ECIES](/docs/specs/ecies) cho các Destination. Các router chỉ có một khóa công khai.

Một router ECIES không có khóa tĩnh ElGamal. Router vẫn cần một triển khai ElGamal để xây dựng tunnel thông qua các router ElGamal và gửi tin nhắn được mã hóa đến các router ElGamal.

Một ECIES router CÓ THỂ yêu cầu một trình quản lý ElGamal Session Key một phần để nhận các thông điệp được gắn thẻ ElGamal nhận được dưới dạng phản hồi cho các tra cứu NetDB từ các floodfill router phiên bản trước 0.9.46, vì những router đó không có triển khai phản hồi được gắn thẻ ECIES như đã chỉ định trong [Prop152](/proposals/152-ecies-tunnels). Nếu không, một ECIES router có thể không yêu cầu phản hồi được mã hóa từ một floodfill router phiên bản trước 0.9.46.

Đây là tùy chọn. Quyết định có thể khác nhau trong các triển khai I2P khác nhau và có thể phụ thuộc vào lượng mạng đã nâng cấp lên phiên bản 0.9.46 trở lên. Tính đến ngày này, khoảng 85% mạng đang sử dụng phiên bản 0.9.46 trở lên.

### Khung Giao Thức Noise

Đặc tả này cung cấp các yêu cầu dựa trên [Noise Protocol Framework](https://noiseprotocol.org/noise.html) (Phiên bản 34, 2018-07-11). Theo thuật ngữ của Noise, Alice là bên khởi tạo và Bob là bên phản hồi.

Nó dựa trên giao thức Noise Noise_N_25519_ChaChaPoly_SHA256. Giao thức Noise này sử dụng các thành phần nguyên thủy sau:

- **Mẫu Bắt Tay Một Chiều: N** - Alice không truyền khóa tĩnh của cô ấy cho Bob (N)
- **Hàm DH: X25519** - X25519 DH với độ dài khóa 32 byte như được chỉ định trong [RFC-7748](https://tools.ietf.org/html/rfc7748).
- **Hàm Mã Hóa: ChaChaPoly** - AEAD_CHACHA20_POLY1305 như được chỉ định trong [RFC-7539](https://tools.ietf.org/html/rfc7539) mục 2.8. Nonce 12 byte, với 4 byte đầu được đặt bằng không. Giống hệt với [NTCP2](/docs/specs/ntcp2).
- **Hàm Hash: SHA256** - Hash tiêu chuẩn 32-byte, đã được sử dụng rộng rãi trong I2P.

### Các Mẫu Bắt Tay

Handshake sử dụng các mẫu handshake của [Noise](https://noiseprotocol.org/noise.html).

Ánh xạ chữ cái sau đây được sử dụng:

- e = khóa tạm thời một lần
- s = khóa tĩnh
- p = tải trọng thông điệp

Yêu cầu xây dựng giống hệt với mẫu Noise N. Điều này cũng giống hệt với thông điệp đầu tiên (Session Request) trong mẫu XK được sử dụng trong [NTCP2](/docs/specs/ntcp2).

```
<- s
  ...
  e es p ->
```
### Mã hóa tin nhắn

Các thông điệp được tạo ra và mã hóa bất đối xứng đến router đích. Việc mã hóa bất đối xứng các thông điệp này hiện tại sử dụng ElGamal như được định nghĩa trong [Cryptography](/docs/specs/cryptography) và chứa một checksum SHA-256. Thiết kế này không có tính bảo mật chuyển tiếp.

Thiết kế ECIES sử dụng mẫu Noise một chiều "N" với ECIES-X25519 ephemeral-static DH, với HKDF, và ChaCha20/Poly1305 AEAD để đảm bảo bảo mật chuyển tiếp, tính toàn vẹn và xác thực. Alice là người gửi tin nhắn ẩn danh, có thể là một router hoặc đích đến. Router ECIES đích là Bob.

### Mã hóa phản hồi

Các phản hồi không phải là một phần của giao thức này, vì Alice là ẩn danh. Các khóa phản hồi, nếu có, được đóng gói trong thông điệp yêu cầu. Xem [đặc tả I2NP](/docs/specs/i2np) cho các Database Lookup Messages.

Phản hồi cho các thông báo Database Lookup là các thông báo Database Store hoặc Database Search Reply. Chúng được mã hóa như các thông báo Existing Session với reply key 32-byte và reply tag 8-byte như được chỉ định trong [I2NP](/docs/specs/i2np) và [Prop154](/proposals/154-ecies-lookups).

Không có phản hồi rõ ràng nào cho các thông báo Database Store. Người gửi có thể gói phản hồi của chính mình như một Garlic Message gửi cho chính nó, chứa một thông báo Delivery Status.

## Đặc tả kỹ thuật

X25519: Xem [ECIES](/docs/specs/ecies).

Router Identity và Key Certificate: Xem [Common Structures](/docs/specs/common-structures).

### Mã hóa Yêu cầu

Mã hóa yêu cầu giống như được chỉ định trong [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) và [Prop152](/proposals/152-ecies-tunnels), sử dụng pattern "N" của Noise.

Các phản hồi cho việc tra cứu sẽ được mã hóa bằng ratchet tag nếu được yêu cầu trong tra cứu. Các thông điệp yêu cầu Database Lookup chứa reply key 32-byte và reply tag 8-byte như được chỉ định trong [I2NP](/docs/specs/i2np) và [Prop154](/proposals/154-ecies-lookups). Key và tag được sử dụng để mã hóa phản hồi.

Các bộ tag không được tạo. Sơ đồ khóa tĩnh bằng không được chỉ định trong ECIES-X25519-AEAD-Ratchet [Prop144](/proposals/144-ecies-x25519-aead-ratchet) và [ECIES](/docs/specs/ecies) sẽ không được sử dụng. Các khóa tạm thời sẽ không được mã hóa Elligator2.

Nói chung, đây sẽ là các thông điệp New Session và sẽ được gửi với khóa tĩnh bằng không (không có ràng buộc hoặc phiên), vì người gửi thông điệp là ẩn danh.

#### KDF cho ck và h ban đầu

Đây là [Noise](https://noiseprotocol.org/noise.html) tiêu chuẩn cho pattern "N" với tên giao thức tiêu chuẩn. Điều này giống như được chỉ định trong [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) và [Prop152](/proposals/152-ecies-tunnels) cho các thông điệp xây dựng tunnel.

```
This is the "e" message pattern:

  // Define protocol_name.
  Set protocol_name = "Noise_N_25519_ChaChaPoly_SHA256"
  (31 bytes, US-ASCII encoded, no NULL termination).

  // Define Hash h = 32 bytes
  // Pad to 32 bytes. Do NOT hash it, because it is not more than 32 bytes.
  h = protocol_name || 0

  Define ck = 32 byte chaining key. Copy the h data to ck.
  Set chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // up until here, can all be precalculated by all routers.
```
#### KDF cho Tin nhắn

Người tạo thông điệp tạo ra một cặp khóa X25519 tạm thời cho mỗi thông điệp. Các khóa tạm thời phải là duy nhất cho mỗi thông điệp. Điều này giống như được chỉ định trong [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) và [Prop152](/proposals/152-ecies-tunnels) cho các thông điệp xây dựng tunnel.

```
  // Target router's X25519 static keypair (hesk, hepk) from the Router Identity
  hesk = GENERATE_PRIVATE()
  hepk = DERIVE_PUBLIC(hesk)

  // MixHash(hepk)
  // || below means append
  h = SHA256(h || hepk);

  // up until here, can all be precalculated by each router
  // for all incoming messages

  // Sender generates an X25519 ephemeral keypair
  sesk = GENERATE_PRIVATE()
  sepk = DERIVE_PUBLIC(sesk)

  // MixHash(sepk)
  h = SHA256(h || sepk);

  End of "e" message pattern.

  This is the "es" message pattern:

  // Noise es
  // Sender performs an X25519 DH with receiver's static public key.
  // The target router
  // extracts the sender's ephemeral key preceding the encrypted record.
  sharedSecret = DH(sesk, hepk) = DH(hesk, sepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // ChaChaPoly parameters to encrypt/decrypt
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  // Chain key is not used
  //chainKey = keydata[0:31]

  // AEAD parameters
  k = keydata[32:63]
  n = 0
  plaintext = 464 byte build request record
  ad = h
  ciphertext = ENCRYPT(k, n, plaintext, ad)

  End of "es" message pattern.

  // MixHash(ciphertext) is not required
  //h = SHA256(h || ciphertext)
```
#### Tải trọng

Payload sử dụng cùng định dạng khối như được định nghĩa trong [ECIES](/docs/specs/ecies) và [Prop144](/proposals/144-ecies-x25519-aead-ratchet). Tất cả các thông điệp phải chứa một khối DateTime để ngăn chặn tấn công replay.

## Ghi Chú Triển Khai

- Các router cũ không kiểm tra loại mã hóa của router và sẽ gửi các thông điệp được mã hóa ElGamal. Một số router gần đây có lỗi và sẽ gửi các loại thông điệp không đúng định dạng khác nhau. Người triển khai nên phát hiện và từ chối các bản ghi này trước khi thực hiện thao tác DH nếu có thể, để giảm mức sử dụng CPU.

## Tài liệu tham khảo

- [Cấu trúc chung](/docs/specs/common-structures)
- [Mật mã học](/docs/specs/cryptography)
- [ECIES](/docs/specs/ecies)
- [I2NP](/docs/specs/i2np)
- [Khung giao thức Noise](https://noiseprotocol.org/noise.html)
- [NTCP2](/docs/specs/ntcp2)
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet)
- [Prop152](/proposals/152-ecies-tunnels)
- [Prop154](/proposals/154-ecies-lookups)
- [Prop156](/proposals/156-ecies-routers)
- [RFC-7539](https://tools.ietf.org/html/rfc7539)
- [RFC-7748](https://tools.ietf.org/html/rfc7748)
- [Tạo tunnel-ECIES](/docs/specs/tunnel-creation-ecies)
