---
title: "B32 cho Encrypted Leasesets"
description: "Định dạng địa chỉ Base 32 cho leaseSet LS2 được mã hóa"
slug: "b32encrypted"
category: "Thiết kế"
lastUpdated: "2020-08"
accurateFor: "0.9.47"
---

## Tổng quan

Địa chỉ Base 32 tiêu chuẩn ("b32") chứa hash của đích đến. Điều này sẽ không hoạt động với encrypted ls2 (đề xuất 123).

Chúng ta không thể sử dụng địa chỉ base 32 truyền thống cho một LS2 mã hóa (đề xuất 123), vì nó chỉ chứa hash của destination. Nó không cung cấp public key không bị làm mờ. Clients phải biết public key của destination, loại sig, loại blinded sig, và một secret hoặc private key tùy chọn để tìm nạp và giải mã leaseset. Do đó, chỉ riêng địa chỉ base 32 là không đủ. Client cần có destination đầy đủ (chứa public key), hoặc chỉ riêng public key. Nếu client có destination đầy đủ trong address book, và address book hỗ trợ tra cứu ngược theo hash, thì public key có thể được truy xuất.

Định dạng này đặt public key thay vì hash vào một địa chỉ base32. Định dạng này cũng phải chứa loại chữ ký của public key và loại chữ ký của lược đồ blinding.

Tài liệu này quy định định dạng b32 cho các địa chỉ này. Mặc dù chúng tôi đã gọi định dạng mới này trong các cuộc thảo luận là địa chỉ "b33", định dạng mới thực tế vẫn giữ hậu tố ".b32.i2p" thông thường.

## Thiết kế

- Định dạng mới sẽ chứa public key không bị che mờ, loại chữ ký không bị che mờ,
  và loại chữ ký bị che mờ.
- Tùy chọn chứa secret và/hoặc private key, chỉ dành cho các liên kết riêng tư
- Sử dụng hậu tố ".b32.i2p" hiện có, nhưng với độ dài lớn hơn.
- Thêm checksum.
- Địa chỉ cho các leaseSet được mã hóa được xác định bởi 56 ký tự được mã hóa trở lên (35 byte được giải mã trở lên), so với 52 ký tự (32
  byte) cho các địa chỉ base 32 truyền thống.

## Đặc tả kỹ thuật

### Tạo và mã hóa

Xây dựng một hostname có dạng {56+ ký tự}.b32.i2p (35+ ký tự trong nhị phân) như sau:

```
flag (1 byte)
    bit 0: 0 for one-byte sigtypes, 1 for two-byte sigtypes
    bit 1: 0 for no secret, 1 if secret is required
    bit 2: 0 for no per-client auth, 1 if client private key is required
    bits 7-3: Unused, set to 0

public key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

blinded key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

public key
    Number of bytes as implied by sigtype
```
Xử lý hậu kỳ và checksum:

```
Construct the binary data as above.
Treat checksum as little-endian.
Calculate checksum = CRC-32(data[3:end])
data[0] ^= (byte) checksum
data[1] ^= (byte) (checksum >> 8)
data[2] ^= (byte) (checksum >> 16)

hostname = Base32.encode(data) || ".b32.i2p"
```
Bất kỳ bit không sử dụng nào ở cuối b32 phải bằng 0. Không có bit không sử dụng cho địa chỉ tiêu chuẩn 56 ký tự (35 byte).

### Giải mã và Xác minh

```
strip the ".b32.i2p" from the hostname
data = Base32.decode(hostname)
Calculate checksum = CRC-32(data[3:end])
Treat checksum as little-endian.
flags = data[0] ^ (byte) checksum
if 1 byte sigtypes:
    pubkey sigtype = data[1] ^ (byte) (checksum >> 8)
    blinded sigtype = data[2] ^ (byte) (checksum >> 16)
else (2 byte sigtypes):
    pubkey sigtype = data[1] ^ ((byte) (checksum >> 8)) || data[2] ^ ((byte) (checksum >> 16))
    blinded sigtype = data[3] || data[4]
parse the remainder based on the flags to get the public key
```
### Bit Khóa Bí Mật và Khóa Riêng Tư

Các bit secret và private key được sử dụng để báo hiệu cho client, proxy, hoặc các mã client-side khác rằng secret và/hoặc private key sẽ được yêu cầu để giải mã leaseset. Các triển khai cụ thể có thể nhắc người dùng cung cấp dữ liệu cần thiết, hoặc từ chối các nỗ lực kết nối nếu thiếu dữ liệu yêu cầu.

## Bộ nhớ đệm

Mặc dù nằm ngoài phạm vi của đặc tả này, các router và/hoặc client phải ghi nhớ và lưu cache (có thể là vĩnh viễn) ánh xạ từ khóa công khai đến đích đến, và ngược lại.

## Ghi chú

- Phân biệt các phiên bản cũ và mới theo độ dài. Địa chỉ b32 cũ luôn là
  {52 ký tự}.b32.i2p. Địa chỉ mới là {56+ ký tự}.b32.i2p
- Chủ đề thảo luận Tor:
  https://lists.torproject.org/pipermail/tor-dev/2017-January/011816.html
- Không mong đợi sigtypes 2 byte sẽ xuất hiện, chúng ta chỉ mới lên đến 13. Không
  cần triển khai ngay bây giờ.
- Định dạng mới có thể được sử dụng trong các liên kết jump (và được phục vụ bởi jump servers) nếu
  muốn, giống như b32.

## Tài liệu tham khảo

- [CRC-32](https://en.wikipedia.org/wiki/CRC-32) - xem thêm [RFC 3309](https://tools.ietf.org/html/rfc3309)
