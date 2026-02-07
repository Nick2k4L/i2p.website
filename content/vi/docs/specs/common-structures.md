---
title: "Đặc tả cấu trúc chung"
description: "Các kiểu dữ liệu chung cho tất cả các giao thức I2P"
slug: "common-structures"
category: "Thiết kế"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

Tài liệu này mô tả một số kiểu dữ liệu chung cho tất cả các giao thức I2P, như [I2NP](/docs/specs/i2np/), [I2CP](/docs/specs/i2cp/), [SSU](/docs/legacy/ssu/), v.v.

## Đặc tả kiểu dữ liệu chung

### Số nguyên

#### Mô tả

Biểu thị một số nguyên không âm.

#### Nội dung

1 đến 8 byte theo thứ tự byte mạng (big endian) đại diện cho một số nguyên không dấu.

### Ngày

#### Mô tả

Số mili giây kể từ nửa đêm ngày 1 tháng 1 năm 1970 theo múi giờ GMT. Nếu số này là 0, ngày tháng sẽ không được xác định hoặc là null.

#### Nội dung

8 byte [Integer](#integer)

### Chuỗi

#### Mô tả

Biểu diễn một chuỗi được mã hóa UTF-8.

#### Nội dung

1 hoặc nhiều byte trong đó byte đầu tiên là số byte (không phải ký tự!) trong chuỗi và 0-255 byte còn lại là mảng ký tự được mã hóa UTF-8 không kết thúc bằng null. Giới hạn độ dài là 255 byte (không phải ký tự). Độ dài có thể là 0.

### PublicKey

#### Mô tả

Cấu trúc này được sử dụng trong ElGamal hoặc các phương pháp mã hóa bất đối xứng khác, chỉ biểu diễn số mũ, không phải số nguyên tố, vì chúng là hằng số và được định nghĩa trong đặc tả mật mã học [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy). Các sơ đồ mã hóa khác đang trong quá trình được định nghĩa, xem bảng bên dưới.

#### Nội dung

Loại khóa và độ dài được suy ra từ ngữ cảnh hoặc được chỉ định trong Key Certificate của một Destination hoặc RouterInfo, hoặc các trường trong [LeaseSet2](#leaseset2) hoặc cấu trúc dữ liệu khác. Loại mặc định là ElGamal. Kể từ phiên bản 0.9.38, các loại khác có thể được hỗ trợ, tùy thuộc vào ngữ cảnh. Các khóa sử dụng big-endian trừ khi có ghi chú khác.

Các khóa X25519 được hỗ trợ trong Destinations và LeaseSet2 kể từ phiên bản 0.9.44. Các khóa X25519 được hỗ trợ trong RouterIdentities kể từ phiên bản 0.9.48.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there; discouraged for leasesets</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Little-endian. See <a href="/docs/specs/ecies/">ECIES</a> and <a href="/docs/specs/ecies-routers/">ECIES-ROUTERS</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">800</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1184</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1568</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1088</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1568</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/PublicKey.html

### PrivateKey

#### Mô tả

Cấu trúc này được sử dụng trong ElGamal hoặc các phương pháp giải mã bất đối xứng khác, chỉ đại diện cho số mũ, không phải các số nguyên tố là hằng số và được định nghĩa trong đặc tả mật mã học [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy). Các lược đồ mã hóa khác đang trong quá trình được định nghĩa, xem bảng dưới đây.

#### Mục lục

Loại khóa và độ dài được suy ra từ ngữ cảnh hoặc được lưu trữ riêng biệt trong một cấu trúc dữ liệu hoặc tệp khóa riêng tư. Loại mặc định là ElGamal. Kể từ phiên bản 0.9.38, các loại khóa khác có thể được hỗ trợ, tùy thuộc vào ngữ cảnh. Các khóa sử dụng định dạng big-endian trừ khi có ghi chú khác.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there; discouraged for leasesets</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">48</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">66</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Little-endian. See <a href="/docs/specs/ecies/">ECIES</a> and <a href="/docs/specs/ecies-routers/">ECIES-ROUTERS</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1632</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2400</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3168</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/PrivateKey.html

### SessionKey

#### Mô tả

Cấu trúc này được sử dụng cho việc mã hóa và giải mã AES256 đối xứng.

#### Nội dung

32 byte

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionKey.html

### SigningPublicKey

#### Mô tả

Cấu trúc này được sử dụng để xác minh chữ ký.

#### Mục lục

Loại khóa và độ dài được suy ra từ ngữ cảnh hoặc được chỉ định trong Key Certificate của một Destination. Loại mặc định là DSA_SHA1. Kể từ phiên bản 0.9.12, các loại khác có thể được hỗ trợ, tùy thuộc vào ngữ cảnh.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### Ghi chú

* Khi một khóa được cấu thành từ hai phần tử (ví dụ các điểm X,Y), nó được tuần tự hóa bằng cách đệm mỗi phần tử đến độ dài/2 với các số không đứng đầu nếu cần thiết.

* Tất cả các loại đều là Big Endian, ngoại trừ EdDSA và RedDSA, được lưu trữ và truyền tải
  theo định dạng Little Endian.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPublicKey.html

### SigningPrivateKey

#### Mô tả

Cấu trúc này được sử dụng để tạo chữ ký.

#### Nội dung

Loại khóa và độ dài được chỉ định khi tạo. Loại mặc định là DSA_SHA1. Kể từ phiên bản 0.9.12, các loại khác có thể được hỗ trợ, tùy thuộc vào ngữ cảnh.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">48</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">66</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### Ghi chú

* Khi một key được tạo thành từ hai phần tử (ví dụ các điểm X,Y), nó được
  serialize bằng cách đệm mỗi phần tử đến độ dài/2 với các số 0 đứng đầu nếu
  cần thiết.

* Tất cả các kiểu dữ liệu đều là Big Endian, ngoại trừ EdDSA và RedDSA, được lưu trữ và truyền tải
  ở định dạng Little Endian.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPrivateKey.html

### Chữ ký

#### Mô tả

Cấu trúc này đại diện cho chữ ký của một số dữ liệu.

#### Mục lục

Loại và độ dài chữ ký được suy ra từ loại khóa được sử dụng. Loại mặc định là DSA_SHA1. Kể từ phiên bản 0.9.12, các loại khác có thể được hỗ trợ, tùy thuộc vào ngữ cảnh.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">40</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### Ghi chú

* Khi một chữ ký được tạo thành từ hai phần tử (ví dụ các giá trị R,S), nó được tuần tự hóa bằng cách đệm mỗi phần tử thành độ dài/2 với các số 0 đứng đầu nếu cần thiết.

* Tất cả các kiểu dữ liệu đều là Big Endian, ngoại trừ EdDSA và RedDSA, được lưu trữ và truyền tải theo định dạng Little Endian.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Signature.html

### Hash

#### Mô tả

Đại diện cho SHA256 của một số dữ liệu.

#### Mục lục

32 byte

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Hash.html

### Session Tag

Lưu ý: Session Tags cho các đích ECIES-X25519 (ratchet) và các router ECIES-X25519 có độ dài 8 byte. Xem [ECIES](/docs/specs/ecies/) và [ECIES-ROUTERS](/docs/specs/ecies-routers/).

#### Mô tả

Một số ngẫu nhiên

#### Mục lục

32 bytes

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionTag.html

### TunnelId

#### Mô tả

Định nghĩa một mã định danh duy nhất cho mỗi router trong một tunnel. Tunnel ID thường lớn hơn không; không sử dụng giá trị bằng không trừ trong các trường hợp đặc biệt.

#### Mục lục

4 byte [Integer](#integer)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/TunnelId.html

### Chứng chỉ

#### Mô tả

Certificate là một container chứa các biên lai hoặc bằng chứng công việc khác nhau được sử dụng trong toàn bộ mạng I2P.

#### Mục lục

1 byte [Integer](#integer) chỉ định loại chứng chỉ, tiếp theo là 2 byte [Integer](#integer) chỉ định kích thước của dữ liệu chứng chỉ, sau đó là số byte tương ứng.

```
+----+----+----+----+----+-/
|type| length  | payload
+----+----+----+----+----+-/

type :: `Integer`
        length -> 1 byte

        case 0 -> NULL
        case 1 -> HASHCASH
        case 2 -> HIDDEN
        case 3 -> SIGNED
        case 4 -> MULTIPLE
        case 5 -> KEY

length :: `Integer`
          length -> 2 bytes

payload :: data
           length -> $length bytes
```
#### Ghi chú

* Đối với [Router Identities](#routeridentity), Certificate luôn là NULL qua phiên bản
  0.9.15. Từ 0.9.16, một Key Certificate được sử dụng để chỉ định các
  kiểu khóa. Từ 0.9.48, các kiểu khóa công khai mã hóa X25519
  được cho phép. Xem bên dưới.

* Đối với [Garlic Cloves](/docs/specs/i2np/#struct-garlicclove), Certificate luôn là NULL, hiện tại không có loại nào khác được triển khai.

* Đối với [Garlic Messages](/docs/specs/i2np/#msg-garlic), Certificate luôn là NULL, hiện tại không có loại nào khác được triển khai.

* Đối với [Destinations](#destination), Certificate có thể khác NULL. Kể từ phiên bản 0.9.12, Key Certificate có thể được sử dụng để chỉ định loại khóa công khai ký. Xem bên dưới.

* Các nhà triển khai được khuyến cáo cấm dữ liệu thừa trong Certificates.
  Độ dài phù hợp cho mỗi loại certificate nên được thực thi.

#### Các Loại Chứng Chỉ

Các loại certificate sau đây được định nghĩa:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">HashCash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains an ASCII colon-separated hashcash string.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Hidden</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Hidden routers generally do not announce that they are hidden.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Signed</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">40 or 72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">43 or 75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains a 40-byte DSA signature, optionally followed by the 32-byte Hash of the signing Destination.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Multiple</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains multiple certificates.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4+</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7+</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Since 0.9.12. See below for details.</td>
    </tr>
  </tbody>
</table>
#### Chứng chỉ Khóa

Chứng chỉ khóa được giới thiệu trong phiên bản 0.9.12. Trước phiên bản đó, tất cả PublicKeys đều là khóa ElGamal 256-byte, và tất cả SigningPublicKeys đều là khóa DSA-SHA1 128-byte. Chứng chỉ khóa cung cấp cơ chế để chỉ định loại PublicKey và SigningPublicKey trong Destination hoặc RouterIdentity, và để đóng gói bất kỳ dữ liệu khóa nào vượt quá độ dài tiêu chuẩn.

Bằng cách duy trì chính xác 384 byte trước certificate, và đặt bất kỳ dữ liệu khóa dư thừa nào bên trong certificate, chúng tôi duy trì khả năng tương thích cho bất kỳ phần mềm nào phân tích Destinations và Router Identities.

Payload chứng chỉ khóa chứa:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Signing Public Key Type (<a href="#integer">Integer</a>)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Crypto Public Key Type (<a href="#integer">Integer</a>)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Excess Signing Public Key Data</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0+</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Excess Crypto Public Key Data</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0+</td>
    </tr>
  </tbody>
</table>
Cảnh báo: Thứ tự loại khóa ngược lại với những gì bạn có thể mong đợi; Loại Khóa Công Khai Ký được đặt trước.

Các loại Signing Public Key được định nghĩa là:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Public Key Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely if ever used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely if ever used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (GOST)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/134-gost/">Prop134</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (GOST)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/134-gost/">Prop134</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only; never used for Router Identities</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">13</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">14</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65280-65534</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for experimental use</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65535</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for future expansion</td>
    </tr>
  </tbody>
</table>
Các loại Crypto Public Key được định nghĩa là:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Public Key Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies/">ECIES</a> and proposal 156</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (NONE)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">255</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65280-65534</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for experimental use</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65535</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for future expansion</td>
    </tr>
  </tbody>
</table>
Khi Key Certificate không có mặt, 384 bytes phía trước trong Destination hoặc RouterIdentity được định nghĩa là 256-byte ElGamal PublicKey theo sau bởi 128-byte DSA-SHA1 SigningPublicKey. Khi Key Certificate có mặt, 384 bytes phía trước được định nghĩa lại như sau:

* Hoàn chỉnh hoặc phần đầu của Khóa Công khai Mật mã

* Padding ngẫu nhiên nếu tổng độ dài của hai khóa ít hơn 384 byte

* Hoàn chỉnh hoặc phần đầu của Signing Public Key

Crypto Public Key được căn chỉnh ở đầu và Signing Public Key được căn chỉnh ở cuối. Phần đệm (nếu có) nằm ở giữa. Độ dài và ranh giới của dữ liệu khóa ban đầu, phần đệm và phần dữ liệu khóa dư thừa trong các chứng chỉ không được chỉ định rõ ràng, mà được suy ra từ độ dài của các loại khóa đã chỉ định. Nếu tổng độ dài của Crypto và Signing Public Keys vượt quá 384 byte, phần còn lại sẽ được chứa trong Key Certificate. Nếu độ dài Crypto Public Key không phải là 256 byte, phương pháp xác định ranh giới giữa hai khóa sẽ được chỉ định trong phiên bản tương lai của tài liệu này.

Các bố cục ví dụ sử dụng ElGamal Crypto Public Key và loại Signing Public Key được chỉ định:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Signing Key Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Excess Signing Key Data in Cert</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Certificate.html

#### Ghi chú

* Những người triển khai được khuyến cáo nên cấm dữ liệu dư thừa trong Key Certificates.
  Độ dài phù hợp cho từng loại certificate nên được thực thi.

* Chứng chỉ KEY với loại 0,0 (ElGamal,DSA_SHA1) được cho phép nhưng không khuyến khích sử dụng.
  Nó chưa được kiểm tra kỹ lưỡng và có thể gây ra vấn đề trong một số triển khai.
  Sử dụng chứng chỉ NULL trong biểu diễn chuẩn của
  Destination hoặc RouterIdentity (ElGamal,DSA_SHA1), điều này sẽ ngắn hơn 4 byte
  so với việc sử dụng chứng chỉ KEY.

### Ánh xạ

#### Mô tả

Một tập hợp các ánh xạ key/value hoặc thuộc tính

#### Mục lục

Một Integer kích thước 2-byte theo sau bởi một chuỗi các cặp String=String;.

CẢNH BÁO: Hầu hết các cách sử dụng Mapping đều nằm trong các cấu trúc đã ký, nơi các mục Mapping phải được sắp xếp theo khóa, để chữ ký không thể thay đổi. Việc không sắp xếp theo khóa sẽ dẫn đến lỗi chữ ký!

```
+----+----+----+----+----+----+----+----+
|  size   | key_string (len + data)| =  |
+----+----+----+----+----+----+----+----+
| val_string (len + data)     | ;  | ...
+----+----+----+----+----+----+----+
size :: `Integer`
        length -> 2 bytes
        Total number of bytes that follow

key_string :: `String`
              A string (one byte length followed by UTF-8 encoded characters)

= :: A single byte containing '='

val_string :: `String`
              A string (one byte length followed by UTF-8 encoded characters)

; :: A single byte containing ';'
```
#### Ghi chú

* Việc mã hóa không tối ưu - chúng ta cần các ký tự '=' và ';', hoặc
  độ dài chuỗi, nhưng không cần cả hai

* Một số tài liệu nói rằng các chuỗi có thể không bao gồm '=' hoặc ';' nhưng mã hóa này hỗ trợ chúng

* Chuỗi được định nghĩa là UTF-8 nhưng trong implementation hiện tại, I2CP sử dụng UTF-8 còn I2NP thì không. Ví dụ, chuỗi UTF-8 trong ánh xạ tùy chọn RouterInfo trong I2NP Database Store Message sẽ bị hỏng.

* Mã hóa cho phép các khóa trùng lặp, tuy nhiên trong bất kỳ trường hợp sử dụng nào mà ánh xạ được ký, các khóa trùng lặp có thể gây ra lỗi chữ ký.

* Các ánh xạ chứa trong thông điệp I2NP (ví dụ trong RouterAddress hoặc RouterInfo)
  phải được sắp xếp theo khóa để chữ ký sẽ không thay đổi. Không được phép có
  khóa trùng lặp.

* Các ánh xạ được chứa trong một [I2CP SessionConfig](/docs/specs/i2cp/#struct-sessionconfig) phải được sắp xếp theo khóa để
  chữ ký sẽ không thay đổi. Các khóa trùng lặp không được phép.

* Phương thức sắp xếp được định nghĩa như trong Java String.compareTo(), sử dụng giá trị Unicode của các ký tự.

* Mặc dù phụ thuộc vào ứng dụng, các khóa và giá trị thường phân biệt chữ hoa chữ thường.

* Giới hạn độ dài chuỗi key và value là 255 byte (không phải ký tự) mỗi cái, cộng
  với byte độ dài. Byte độ dài có thể bằng 0.

* Giới hạn tổng độ dài là 65535 byte, cộng với trường kích thước 2 byte, hoặc tổng cộng 65537.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/DataHelper.html

## Đặc tả cấu trúc chung

### KeysAndCert

#### Mô tả

Một khóa công khai mã hóa, một khóa công khai ký số, và một chứng chỉ, được sử dụng như một RouterIdentity hoặc một Destination.

#### Nội dung

Một [PublicKey](#publickey) theo sau bởi một [SigningPublicKey](#signingpublickey) và sau đó là một [Certificate](#certificate).

```
+----+----+----+----+----+----+----+----+
| public_key                            |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| padding (optional)                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signing_key                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| certificate                           |
+----+----+----+-/

public_key :: `PublicKey` (partial or full)
              length -> 256 bytes or as specified in key certificate

padding :: random data
           length -> 0 bytes or as specified in key certificate
           public_key length + padding length + signing_key length == 384 bytes

signing__key :: `SigningPublicKey` (partial or full)
                length -> 128 bytes or as specified in key certificate

certificate :: `Certificate`
               length -> >= 3 bytes

total length: 387+ bytes
```
#### Hướng Dẫn Tạo Padding

Những hướng dẫn này đã được đề xuất trong Đề xuất 161 và được triển khai trong phiên bản API 0.9.57. Những hướng dẫn này tương thích ngược với tất cả các phiên bản từ 0.6 (2005). Xem Đề xuất 161 để biết thêm thông tin cơ bản và chi tiết.

Đối với bất kỳ kết hợp loại khóa nào hiện đang được sử dụng khác với ElGamal + DSA-SHA1, sẽ có padding. Ngoài ra, đối với các destination, trường public key 256-byte đã không được sử dụng kể từ phiên bản 0.6 (2005).

Các nhà phát triển nên tạo dữ liệu ngẫu nhiên cho khóa công khai Destination và phần đệm của Destination và Router Identity sao cho nó có thể được nén trong các giao thức I2P khác nhau trong khi vẫn đảm bảo bảo mật, và không làm cho các biểu diễn Base 64 có vẻ bị hỏng hoặc không an toàn. Điều này cung cấp hầu hết lợi ích của việc loại bỏ các trường đệm mà không cần thay đổi giao thức gây gián đoạn.

Nói một cách chính xác, chỉ riêng signing public key 32-byte (trong cả Destinations và Router Identities) và encryption public key 32-byte (chỉ trong Router Identities) là một số ngẫu nhiên cung cấp toàn bộ entropy cần thiết để các hash SHA-256 của những cấu trúc này có độ mạnh mật mã học và được phân phối ngẫu nhiên trong DHT của cơ sở dữ liệu mạng.

Tuy nhiên, để thận trọng tối đa, chúng tôi khuyến nghị sử dụng tối thiểu 32 byte dữ liệu ngẫu nhiên trong trường ElG public key và padding. Ngoài ra, nếu các trường đều là số không, các destination Base 64 sẽ chứa chuỗi dài các ký tự AAAA, điều này có thể gây lo ngại hoặc nhầm lẫn cho người dùng.

Lặp lại 32 byte dữ liệu ngẫu nhiên khi cần thiết để cấu trúc KeysAndCert đầy đủ có thể nén cao trong các giao thức I2P như I2NP Database Store Message, Streaming SYN, handshake SSU2, và Datagram có thể trả lời.

Ví dụ:

* Một Router Identity với loại mã hóa X25519 và loại chữ ký Ed25519
  sẽ chứa 10 bản sao (320 bytes) của dữ liệu ngẫu nhiên, tiết kiệm được khoảng 288 bytes khi nén.

* Một Destination với loại chữ ký Ed25519
  sẽ chứa 11 bản sao (352 bytes) của dữ liệu ngẫu nhiên, tiết kiệm được khoảng 320 bytes khi nén.

Các triển khai tất nhiên phải lưu trữ toàn bộ cấu trúc 387+ byte vì hash SHA-256 của cấu trúc bao phủ toàn bộ nội dung.

#### Ghi chú

* Đừng giả định rằng chúng luôn có 387 byte! Chúng có 387 byte cộng với độ dài certificate được chỉ định tại byte 385-386, có thể khác không.

* Kể từ phiên bản 0.9.12, nếu chứng chỉ là Key Certificate, ranh giới của các trường khóa có thể thay đổi. Xem phần Key Certificate ở trên để biết chi tiết.

* Crypto Public Key được căn chỉnh ở đầu và Signing Public Key được căn chỉnh ở cuối. Phần đệm (nếu có) nằm ở giữa.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/KeysAndCert.html

### RouterIdentity

#### Mô tả

Xác định cách để nhận dạng duy nhất một router cụ thể

#### Mục lục

Giống hệt với KeysAndCert.

Xem [KeysAndCert](#keysandcert) để biết hướng dẫn tạo dữ liệu ngẫu nhiên cho trường padding.

#### Ghi chú

* Chứng chỉ cho một RouterIdentity luôn là NULL cho đến phiên bản 0.9.12.

* Không giả định rằng chúng luôn là 387 byte! Chúng có độ dài 387 byte cộng với độ dài certificate được chỉ định tại byte 385-386, có thể khác không.

* Kể từ phiên bản 0.9.12, nếu certificate là Key Certificate, ranh giới của các trường khóa có thể thay đổi. Xem phần Key Certificate ở trên để biết chi tiết.

* Crypto Public Key được căn chỉnh ở đầu và Signing Public Key được
  căn chỉnh ở cuối. Phần đệm (nếu có) nằm ở giữa.

* RouterIdentities với key certificate và ECIES_X25519 public key
  được hỗ trợ từ phiên bản 0.9.48.
  Trước đó, tất cả RouterIdentities đều là ElGamal.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterIdentity.html

### Điểm đến

#### Mô tả

Một Destination định nghĩa một điểm cuối cụ thể mà các thông điệp có thể được định hướng để giao hàng an toàn.

#### Mục lục

Giống hệt với [KeysAndCert](#keysandcert), ngoại trừ việc public key không bao giờ được sử dụng và có thể chứa dữ liệu ngẫu nhiên thay vì một ElGamal Public Key hợp lệ.

Xem [KeysAndCert](#keysandcert) để biết hướng dẫn tạo dữ liệu ngẫu nhiên cho các trường public key và padding.

#### Ghi chú

* Khóa công khai của đích đã được sử dụng cho mã hóa i2cp-to-i2cp cũ
  đã bị vô hiệu hóa trong phiên bản 0.6 (2005), hiện tại không được sử dụng ngoại trừ
  làm IV cho mã hóa LeaseSet, điều này đã lỗi thời. Thay vào đó, khóa công khai trong
  LeaseSet được sử dụng.

* Đừng giả định rằng chúng luôn là 387 byte! Chúng là 387 byte cộng với độ dài certificate được chỉ định tại byte 385-386, có thể khác không.

* Kể từ phiên bản 0.9.12, nếu certificate là Key Certificate, ranh giới của các trường khóa có thể thay đổi. Xem phần Key Certificate ở trên để biết chi tiết.

* Khóa Công khai Mã hóa được căn chỉnh ở đầu và Khóa Công khai Ký được căn chỉnh ở cuối. Phần đệm (nếu có) nằm ở giữa.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Destination.html

### Lease

#### Mô tả

Định nghĩa quyền ủy quyền cho một tunnel cụ thể để nhận các thông điệp nhắm đến một [Destination](#destination).

#### Mục lục

SHA256 [Hash](#hash) của [RouterIdentity](#routeridentity) của gateway router, sau đó là [TunnelId](#tunnelid), và cuối cùng là [Date](#date) kết thúc.

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     tunnel_id     |      end_date
+----+----+----+----+----+----+----+----+
                    |
+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway
             length -> 32 bytes

tunnel_id :: `TunnelId`
             length -> 4 bytes

end_date :: `Date`
            length -> 8 bytes
```
#### Ghi chú

* Tổng kích thước: 44 bytes

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease.html

### LeaseSet

#### Mô tả

Chứa tất cả các [Lease](#lease) hiện được ủy quyền cho một [Destination](#destination) cụ thể, [PublicKey](#publickey) mà các thông điệp garlic có thể được mã hóa, và sau đó là [SigningPublicKey](#signingpublickey) có thể được sử dụng để thu hồi phiên bản cụ thể này của cấu trúc. LeaseSet là một trong hai cấu trúc được lưu trữ trong cơ sở dữ liệu mạng (cấu trúc còn lại là [RouterInfo](#routerinfo)), và được đánh khóa dưới SHA256 của [Destination](#destination) chứa bên trong.

#### Mục lục

[Destination](#destination), theo sau là một [PublicKey](#publickey) để mã hóa, sau đó là một [SigningPublicKey](#signingpublickey) có thể được sử dụng để thu hồi phiên bản này của LeaseSet, tiếp theo là một [Integer](#integer) 1 byte chỉ định có bao nhiều cấu trúc [Lease](#lease) trong tập hợp, theo sau là các cấu trúc [Lease](#lease) thực tế và cuối cùng là một [Signature](#signature) của các byte trước đó được ký bởi [SigningPrivateKey](#signingprivatekey) của [Destination](#destination).

```
+----+----+----+----+----+----+----+----+
| destination                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| encryption_key                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signing_key                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| Lease 0                          |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease 1                               |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease ($num-1)                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
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

destination :: `Destination`
               length -> >= 387+ bytes

encryption_key :: `PublicKey`
                  length -> 256 bytes

signing_key :: `SigningPublicKey`
               length -> 128 bytes or as specified in destination's key
                         certificate

num :: `Integer`
       length -> 1 byte
       Number of leases to follow
       value: 0 <= num <= 16

leases :: [`Lease`]
          length -> $num*44 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate
```
#### Ghi chú

* Khóa công khai của đích được sử dụng cho mã hóa I2CP-to-I2CP cũ đã bị vô hiệu hóa trong phiên bản 0.6, hiện tại nó không được sử dụng.

* Khóa mã hóa được sử dụng cho mã hóa ElGamal/AES+SessionTag đầu cuối đến đầu cuối
  [ELGAMAL-AES](/docs/specs/elgamal-aes/). Hiện tại nó được tạo mới mỗi khi router khởi động, nó
  không được lưu trữ lâu dài.

* Chữ ký có thể được xác minh bằng cách sử dụng khóa công khai ký của đích đến.

* Một LeaseSet với không có Lease nào được cho phép nhưng không được sử dụng.
  Nó được dự định cho việc thu hồi LeaseSet, tính năng chưa được triển khai.
  Tất cả các biến thể LeaseSet2 đều yêu cầu ít nhất một Lease.

* signing_key hiện tại chưa được sử dụng. Nó được dự định cho việc thu hồi LeaseSet, điều này chưa được triển khai. Hiện tại nó được tạo mới mỗi khi router khởi động, nó không bền vững. Loại signing key luôn giống với loại signing key của đích đến.

* Thời điểm hết hạn sớm nhất của tất cả các Lease được coi là timestamp hoặc
  phiên bản của LeaseSet. Các router thường sẽ không chấp nhận lưu trữ một
  LeaseSet trừ khi nó "mới hơn" so với LeaseSet hiện tại. Cần cẩn thận khi
  công bố một LeaseSet mới mà Lease cũ nhất giống với Lease cũ nhất trong
  LeaseSet trước đó. Router thực hiện công bố thường nên tăng thời gian hết hạn
  của Lease cũ nhất ít nhất 1 ms trong trường hợp đó.

* Trước phiên bản 0.9.7, khi được bao gồm trong một DatabaseStore Message được gửi bởi router gốc, router đã đặt tất cả thời hạn hết hạn của các lease đã xuất bản thành cùng một giá trị, tức là giá trị của lease sớm nhất. Từ phiên bản 0.9.7 trở đi, router xuất bản thời hạn hết hạn thực tế cho từng lease. Đây là chi tiết triển khai và không phải là một phần của đặc tả cấu trúc.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet.html

### Lease2

#### Mô tả

Định nghĩa quyền ủy quyền cho một tunnel cụ thể để nhận các thông điệp nhắm đến một [Destination](#destination). Giống như [Lease](#lease) nhưng với end_date 4-byte. Được sử dụng bởi [LeaseSet2](#leaseset2). Được hỗ trợ từ phiên bản 0.9.38; xem đề xuất 123 để biết thêm thông tin.

#### Mục lục

SHA256 [Hash](#hash) của [RouterIdentity](#routeridentity) của router gateway, sau đó là [TunnelId](#tunnelid), và cuối cùng là ngày kết thúc 4 byte.

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     tunnel_id     |      end_date     |
+----+----+----+----+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway
             length -> 32 bytes

tunnel_id :: `TunnelId`
             length -> 4 bytes

end_date :: 4 byte date
            length -> 4 bytes
            Seconds since the epoch, rolls over in 2106.

```
#### Ghi chú

* Tổng kích thước: 40 byte

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease2.html

### OfflineSignature

#### Mô tả

Đây là phần tùy chọn của [LeaseSet2Header](#leaseset2header). Cũng được sử dụng trong streaming và I2CP. Được hỗ trợ từ phiên bản 0.9.38; xem đề xuất 123 để biết thêm thông tin.

#### Nội dung

Chứa thời hạn hết hiệu lực, một sigtype và [SigningPublicKey](#signingpublickey) tạm thời, và một [Signature](#signature).

```
+----+----+----+----+----+----+----+----+
|     expires       | sigtype |         |
+----+----+----+----+----+----+         +
|       transient_public_key            |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|           signature                   |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

expires :: 4 byte date
           length -> 4 bytes
           Seconds since the epoch, rolls over in 2106.

sigtype :: 2 byte type of the transient_public_key
           length -> 2 bytes

transient_public_key :: `SigningPublicKey`
                        length -> As inferred from the sigtype

signature :: `Signature`
             length -> As inferred from the sigtype of the signing public key
                       in the `Destination` that preceded this offline signature.
             Signature of expires timestamp, transient sig type, and public key,
             by the destination public key.

```
#### Ghi chú

* Phần này có thể và nên được tạo ra offline.

### LeaseSet2Header

#### Mô tả

Đây là phần chung của [LeaseSet2](#leaseset2) và [MetaLeaseSet](#metaleaseset). Được hỗ trợ từ phiên bản 0.9.38; xem đề xuất 123 để biết thêm thông tin.

#### Mục lục

Chứa [Destination](#destination), hai timestamp và một [OfflineSignature](#offlinesignature) tùy chọn.

```
+----+----+----+----+----+----+----+----+
| destination                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|     published     | expires |  flags  |
+----+----+----+----+----+----+----+----+
| offline_signature (optional)          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

destination :: `Destination`
               length -> >= 387+ bytes

published :: 4 byte date
             length -> 4 bytes
             Seconds since the epoch, rolls over in 2106.

expires :: 2 byte time
           length -> 2 bytes
           Offset from published timestamp in seconds, 18.2 hours max

flags :: 2 bytes
  Bit order: 15 14 ... 3 2 1 0
  Bit 0: If 0, no offline keys; if 1, offline keys
  Bit 1: If 0, a standard published leaseset.
         If 1, an unpublished leaseset. Should not be flooded, published, or
         sent in response to a query. If this leaseset expires, do not query the
         netdb for a new one, unless bit 2 is set.
  Bit 2: If 0, a standard published leaseset.
         If 1, this unencrypted leaseset will be blinded and encrypted when published.
         If this leaseset expires, query the blinded location in the netdb for a new one.
         If this bit is set to 1, set bit 1 to 1 also.
         As of release 0.9.42.
  Bits 15-3: set to 0 for compatibility with future uses

offline_signature :: `OfflineSignature`
                     length -> varies
                     Optional, only present if bit 0 is set in the flags.

```
#### Ghi chú

* Tổng kích thước: tối thiểu 395 byte

* Thời gian hết hạn thực tế tối đa là khoảng 660 (11 phút) cho
  [LeaseSet2](#leaseset2) và 65535 (toàn bộ 18.2 giờ) cho [MetaLeaseSet](#metaleaseset).

* [LeaseSet](#leaseset) (1) không có trường 'published', do đó việc phân phiên bản yêu cầu
  tìm kiếm lease sớm nhất. LeaseSet2 thêm trường 'published'
  với độ phân giải một giây. Các router nên giới hạn tốc độ gửi
  leaseSet mới tới floodfill ở mức chậm hơn nhiều so với một lần một giây (mỗi đích đến).
  Nếu điều này không được triển khai, thì mã phải đảm bảo rằng mỗi leaseSet mới
  có thời gian 'published' ít nhất một giây sau thời gian trước đó, nếu không thì
  floodfill sẽ không lưu trữ hoặc flood leaseSet mới.

### LeaseSet2

#### Mô tả

Được chứa trong một thông điệp I2NP DatabaseStore loại 3. Được hỗ trợ từ phiên bản 0.9.38; xem đề xuất 123 để biết thêm thông tin.

Chứa tất cả các [Lease2](#lease2) hiện được ủy quyền cho một [Destination](#destination) cụ thể, và [PublicKey](#publickey) mà các thông điệp garlic có thể được mã hóa. LeaseSet là một trong hai cấu trúc được lưu trữ trong cơ sở dữ liệu mạng (cấu trúc còn lại là [RouterInfo](#routerinfo)), và được khóa dưới SHA256 của [Destination](#destination) chứa bên trong.

#### Mục lục

[LeaseSet2Header](#leaseset2header), theo sau là các tùy chọn, sau đó một hoặc nhiều [PublicKey](#publickey) để mã hóa, [Integer](#integer) chỉ định có bao nhiêu cấu trúc [Lease2](#lease2) trong tập hợp, theo sau là các cấu trúc [Lease2](#lease2) thực tế và cuối cùng là [Signature](#signature) của các byte trước đó được ký bởi [SigningPrivateKey](#signingprivatekey) của [Destination](#destination) hoặc khóa tạm thời.

```
+----+----+----+----+----+----+----+----+
|         ls2_header                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          options                      |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|numk| keytype0| keylen0 |              |
+----+----+----+----+----+              +
|          encryption_key_0             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| keytypen| keylenn |                   |
+----+----+----+----+                   +
|          encryption_key_n             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| Lease2 0                         |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease2($num-1)                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

ls2header :: `LeaseSet2Header`
             length -> varies

options :: `Mapping`
           length -> varies, 2 bytes minimum

numk :: `Integer`
        length -> 1 byte
        Number of key types, key lengths, and `PublicKey`s to follow
        value: 1 <= numk <= max TBD

keytype :: The encryption type of the `PublicKey` to follow.
           length -> 2 bytes

keylen :: The length of the `PublicKey` to follow.
          Must match the specified length of the encryption type.
          length -> 2 bytes

encryption_key :: `PublicKey`
                  length -> keylen bytes

num :: `Integer`
       length -> 1 byte
       Number of `Lease2`s to follow
       value: 0 <= num <= 16

leases :: [`Lease2`]
          length -> $num*40 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate, or by the sigtype of the transient public key,
                       if present in the header

```
#### Tùy chọn Khóa Mã hóa

Đối với các leaseSet đã được xuất bản (máy chủ), các khóa mã hóa được sắp xếp theo thứ tự ưu tiên của máy chủ, khóa được ưu tiên nhất sẽ đứng đầu. Nếu client hỗ trợ nhiều loại mã hóa, khuyến nghị là họ nên tôn trọng sự ưu tiên của máy chủ và chọn loại được hỗ trợ đầu tiên làm phương pháp mã hóa để sử dụng khi kết nối với máy chủ. Nhìn chung, các loại khóa mới hơn (có số thứ tự cao hơn) an toàn hoặc hiệu quả hơn và được ưu tiên, vì vậy các khóa nên được liệt kê theo thứ tự ngược lại của loại khóa.

Tuy nhiên, các client có thể, tùy thuộc vào cách triển khai, lựa chọn dựa trên sở thích của chúng thay vì vậy, hoặc sử dụng một số phương pháp để xác định sở thích "kết hợp". Điều này có thể hữu ích như một tùy chọn cấu hình, hoặc để gỡ lỗi.

Thứ tự khóa trong các leaseSet chưa công bố (client) thực tế không quan trọng, bởi vì các kết nối thường sẽ không được thực hiện đến các client chưa công bố. Trừ khi thứ tự này được sử dụng để xác định ưu tiên kết hợp, như đã mô tả ở trên.

#### Tùy chọn

Kể từ API 0.9.66, một định dạng chuẩn cho các tùy chọn service record đã được xác định. Xem đề xuất 167 để biết chi tiết. Các tùy chọn khác ngoài service record, sử dụng định dạng khác, có thể được định nghĩa trong tương lai.

Các tùy chọn LS2 PHẢI được sắp xếp theo khóa để chữ ký không thay đổi.

Các tùy chọn bản ghi dịch vụ được định nghĩa như sau:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := Tên biểu tượng của dịch vụ mong muốn. Phải viết thường. Ví dụ: "smtp".
  Các ký tự được phép là [a-z0-9-] và không được bắt đầu hoặc kết thúc bằng '-'.
  Phải sử dụng các định danh chuẩn từ [REGISTRY](http://www.dns-sd.org/ServiceTypes.html) hoặc Linux /etc/services nếu được định nghĩa ở đó.
- proto := Giao thức truyền tải của dịch vụ mong muốn. Phải viết thường, có thể là "tcp" hoặc "udp".
  "tcp" có nghĩa là streaming và "udp" có nghĩa là datagram có thể trả lời.
  Các chỉ báo giao thức cho raw datagram và datagram2 có thể được định nghĩa sau.
  Các ký tự được phép là [a-z0-9-] và không được bắt đầu hoặc kết thúc bằng '-'.
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := thời gian tồn tại, số giây nguyên. Số nguyên dương. Ví dụ: "86400".
  Khuyến nghị tối thiểu là 86400 (một ngày), xem phần Khuyến nghị bên dưới để biết chi tiết.
- priority := Độ ưu tiên của host đích, giá trị thấp hơn có nghĩa là được ưu tiên hơn. Số nguyên không âm. Ví dụ: "0"
  Chỉ hữu ích nếu có nhiều hơn một bản ghi, nhưng được yêu cầu ngay cả khi chỉ có một bản ghi.
- weight := Trọng số tương đối cho các bản ghi có cùng độ ưu tiên. Giá trị cao hơn có nghĩa là có nhiều cơ hội được chọn hơn. Số nguyên không âm. Ví dụ: "0"
  Chỉ hữu ích nếu có nhiều hơn một bản ghi, nhưng được yêu cầu ngay cả khi chỉ có một bản ghi.
- port := Cổng I2CP mà dịch vụ có thể được tìm thấy. Số nguyên không âm. Ví dụ: "25"
  Cổng 0 được hỗ trợ nhưng không được khuyến nghị.
- target := Hostname hoặc b32 của đích cung cấp dịch vụ. Một hostname hợp lệ như trong [NAMING](/docs/overview/naming/). Phải viết thường.
  Ví dụ: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" hoặc "example.i2p".
  b32 được khuyến nghị trừ khi hostname là "nổi tiếng", tức là trong sổ địa chỉ chính thức hoặc mặc định.
- appoptions := văn bản tùy ý dành riêng cho ứng dụng, không được chứa " " hoặc ",". Mã hóa là UTF-8.

Ví dụ:

Trong LS2 cho aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, trỏ đến một máy chủ SMTP:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Trong LS2 cho aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, trỏ đến hai máy chủ SMTP:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

Trong LS2 cho bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p, trỏ đến chính nó như một máy chủ SMTP:

"_smtp._tcp" "0 999999 25"

#### Ghi chú

* Khóa công khai của đích đã được sử dụng cho mã hóa I2CP-to-I2CP cũ đã bị vô hiệu hóa trong phiên bản 0.6, hiện tại không được sử dụng.

* Các khóa mã hóa được sử dụng cho mã hóa end-to-end ElGamal/AES+SessionTag
  [ELGAMAL-AES](/docs/specs/elgamal-aes/) (loại 0) hoặc các sơ đồ mã hóa end-to-end khác.
  Xem [ECIES](/docs/specs/ecies/) và đề xuất 145 và 156.
  Chúng có thể được tạo mới mỗi khi router khởi động
  hoặc có thể được duy trì lâu dài.
  X25519 (loại 4, xem [ECIES](/docs/specs/ecies/)) được hỗ trợ từ phiên bản 0.9.44.

* Chữ ký được tạo trên dữ liệu ở trên, được THÊM VÀO TRƯỚC với byte đơn
  chứa loại DatabaseStore (3).

* Chữ ký có thể được xác minh bằng khóa công khai ký của đích đến, hoặc khóa công khai ký tạm thời, nếu một chữ ký ngoại tuyến được bao gồm trong header của leaseset2.

* Độ dài khóa được cung cấp cho từng khóa, để các floodfill và client có thể phân tích cấu trúc ngay cả khi không phải tất cả các loại mã hóa đều được biết hoặc hỗ trợ.

* Xem ghi chú về trường 'published' trong [LeaseSet2Header](#leaseset2header)

* Ánh xạ các tùy chọn, nếu kích thước lớn hơn một, phải được sắp xếp theo khóa, để chữ ký không thay đổi.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet2.html

### MetaLease

#### Mô tả

Định nghĩa quyền ủy quyền cho một tunnel cụ thể để nhận các thông điệp nhắm đến một [Destination](#destination). Giống như [Lease2](#lease2) nhưng sử dụng flags và cost thay vì tunnel id. Được sử dụng bởi [MetaLeaseSet](#metaleaseset). Chứa trong thông điệp I2NP DatabaseStore loại 7. Được hỗ trợ từ phiên bản 0.9.38; xem đề xuất 123 để biết thêm thông tin.

#### Mục lục

SHA256 [Hash](#hash) của [RouterIdentity](#routeridentity) của gateway router, sau đó là các flags và cost, và cuối cùng là ngày kết thúc 4 byte.

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|    flags     |cost|      end_date     |
+----+----+----+----+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway,
             or the hash of another `MetaLeaseSet`.
             length -> 32 bytes

flags :: 3 bytes of flags
         Bit order: 23 22 ... 3 2 1 0
         Bits 3-0: Type of the entry.
         If 0, unknown.
         If 1, a `LeaseSet`.
         If 3, a `LeaseSet2`.
         If 5, a `MetaLeaseSet`.
         Bits 23-4: set to 0 for compatibility with future uses
         length -> 3 bytes

cost :: 1 byte, 0-255. Lower value is higher priority.
        length -> 1 byte

end_date :: 4 byte date
            length -> 4 bytes
            Seconds since the epoch, rolls over in 2106.

```
#### Ghi chú

* Tổng kích thước: 40 byte

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLease.html

### MetaLeaseSet

#### Mô tả

Chứa trong thông điệp I2NP DatabaseStore loại 7. Được định nghĩa từ phiên bản 0.9.38; dự kiến hoạt động từ phiên bản 0.9.40; xem đề xuất 123 để biết thêm thông tin.

Chứa tất cả các [MetaLease](#metalease) hiện được ủy quyền cho một [Destination](#destination) cụ thể, và [PublicKey](#publickey) mà các thông điệp garlic có thể được mã hóa. Một leaseSet là một trong hai cấu trúc được lưu trữ trong cơ sở dữ liệu mạng (cấu trúc kia là [RouterInfo](#routerinfo)), và được đánh khóa dưới SHA256 của [Destination](#destination) chứa trong đó.

#### Nội dung

[LeaseSet2Header](#leaseset2header), theo sau bởi các tùy chọn, [Integer](#integer) chỉ định có bao nhiêu cấu trúc [Lease2](#lease2) trong tập hợp, theo sau bởi các cấu trúc [Lease2](#lease2) thực tế và cuối cùng là một [Signature](#signature) của các byte trước đó được ký bởi [SigningPrivateKey](#signingprivatekey) của [Destination](#destination) hoặc khóa tạm thời.

```
+----+----+----+----+----+----+----+----+
|         ls2_header                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          options                      |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| MetaLease 0                      |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| MetaLease($num-1)                     |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|numr|                                  |
+----+                                  +
|          revocation_0                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          revocation_n                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

ls2header :: `LeaseSet2Header`
             length -> varies

options :: `Mapping`
           length -> varies, 2 bytes minimum

num :: `Integer`
        length -> 1 byte
        Number of `MetaLease`s to follow
        value: 1 <= num <= max TBD

leases :: `MetaLease`s
          length -> $numr*40 bytes

numr :: `Integer`
        length -> 1 byte
        Number of `Hash`es to follow
        value: 0 <= numr <= max TBD

revocations :: [`Hash`]
               length -> $numr*32 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate, or by the sigtype of the transient public key,
                       if present in the header

```
#### Ghi chú

* Khóa công khai của đích đến được sử dụng cho mã hóa I2CP-to-I2CP cũ đã bị vô hiệu hóa trong phiên bản 0.6, hiện tại nó không được sử dụng.

* Chữ ký được tạo trên dữ liệu ở trên, được THÊM VÀO TRƯỚC với một byte đơn
  chứa loại DatabaseStore (7).

* Chữ ký có thể được xác minh bằng khóa công khai ký của
  đích đến, hoặc khóa công khai ký tạm thời, nếu có chữ ký offline
  được bao gồm trong header của leaseset2.

* Xem ghi chú về trường 'published' trong [LeaseSet2Header](#leaseset2header)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLeaseSet.html

### EncryptedLeaseSet

#### Mô tả

Được chứa trong thông điệp I2NP DatabaseStore loại 5. Được định nghĩa từ phiên bản 0.9.38; hoạt động từ phiên bản 0.9.39; xem đề xuất 123 để biết thêm thông tin.

Chỉ có blinded key và thời gian hết hạn hiển thị dưới dạng văn bản thuần túy. LeaseSet thực tế được mã hóa.

#### Nội dung

Một loại chữ ký hai byte, [SigningPrivateKey](#signingprivatekey) được che mờ, thời gian xuất bản, thời gian hết hạn, và các cờ. Sau đó, một độ dài hai byte theo sau bởi dữ liệu được mã hóa. Cuối cùng, một [Signature](#signature) của các byte trước đó được ký bởi [SigningPrivateKey](#signingprivatekey) được che mờ hoặc khóa tạm thời.

```
+----+----+----+----+----+----+----+----+
| sigtype |                             |
+----+----+                             +
|        blinded_public_key             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|     published     | expires |  flags  |
+----+----+----+----+----+----+----+----+
| offline_signature (optional)          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  len    |                             |
+----+----+                             +
|         encrypted_data                |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

sigtype :: A two byte signature type of the public key to follow
           length -> 2 bytes

blinded_public_key :: `SigningPublicKey`
                      length -> As inferred from the sigtype

published :: 4 byte date
             length -> 4 bytes
             Seconds since the epoch, rolls over in 2106.

expires :: 2 byte time
           length -> 2 bytes
           Offset from published timestamp in seconds, 18.2 hours max

flags :: 2 bytes
  Bit order: 15 14 ... 3 2 1 0
  Bit 0: If 0, no offline keys; if 1, offline keys
  Bit 1: If 0, a standard published leaseset.
         If 1, an unpublished leaseset. Should not be flooded, published, or
         sent in response to a query. If this leaseset expires, do not query the
         netdb for a new one.
  Bits 15-2: set to 0 for compatibility with future uses

offline_signature :: `OfflineSignature`
                     length -> varies
                     Optional, only present if bit 0 is set in the flags.

len :: `Integer`
        length -> 2 bytes
        length of encrypted_data to follow
        value: 1 <= num <= max TBD

encrypted_data :: Data encrypted
                  length -> len bytes

signature :: `Signature`
             length -> As specified by the sigtype of the blinded pubic key,
                       or by the sigtype of the transient public key,
                       if present in the header

```
#### Ghi chú

* Khóa công khai của đích được sử dụng cho mã hóa I2CP-to-I2CP cũ đã bị vô hiệu hóa trong phiên bản 0.6, hiện tại không được sử dụng.

* Chữ ký được tạo trên dữ liệu ở trên, được BỔ SUNG TRƯỚC bởi một byte đơn
  chứa loại DatabaseStore (5).

* Chữ ký có thể được xác minh bằng khóa công khai ký của đích đến, hoặc khóa công khai ký tạm thời, nếu chữ ký offline được bao gồm trong header của leaseset2.

* Blinding và mã hóa được chỉ định trong [EncryptedLeaseSet](/docs/specs/encryptedleaseset/)

* Cấu trúc này không sử dụng [LeaseSet2Header](#leaseset2header).

* Thời gian hết hạn thực tế tối đa là khoảng 660 (11 phút), trừ khi
  đó là một [MetaLeaseSet](#metaleaseset) được mã hóa.

* Xem đề xuất 123 để biết ghi chú về việc sử dụng chữ ký ngoại tuyến
  với leaseSet được mã hóa.

* Xem ghi chú về trường 'published' trong [LeaseSet2Header](#leaseset2header)
  (cùng vấn đề, mặc dù chúng ta không sử dụng định dạng LeaseSet2Header ở đây)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/EncryptedLeaseSet.html

### RouterAddress

#### Mô tả

Cấu trúc này định nghĩa các phương thức để liên lạc với một router thông qua giao thức truyền tải.

#### Mục lục

1 byte [Integer](#integer) định nghĩa chi phí tương đối khi sử dụng địa chỉ, trong đó 0 là miễn phí và 255 là đắt đỏ, theo sau là [Date](#date) hết hạn sau đó địa chỉ không nên được sử dụng, hoặc nếu null, địa chỉ không bao giờ hết hạn. Sau đó là một [String](#string) định nghĩa giao thức vận chuyển mà địa chỉ router này sử dụng. Cuối cùng là một [Mapping](#mapping) chứa tất cả các tùy chọn cụ thể của phương thức vận chuyển cần thiết để thiết lập kết nối, chẳng hạn như địa chỉ IP, số cổng, địa chỉ email, URL, v.v.

```
+----+----+----+----+----+----+----+----+
|cost|           expiration
+----+----+----+----+----+----+----+----+
     |        transport_style           |
+----+----+----+----+-/-+----+----+----+
|                                       |
+                                       +
|               options                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

cost :: `Integer`
        length -> 1 byte

        case 0 -> free
        case 255 -> expensive

expiration :: `Date` (must be all zeros, see notes below)
              length -> 8 bytes

              case null -> never expires

transport_style :: `String`
                   length -> 1-256 bytes

options :: `Mapping`
```
#### Ghi chú

* Chi phí thường là 5 hoặc 6 cho SSU, và 10 hoặc 11 cho NTCP.

* Expiration hiện tại không được sử dụng, luôn null (toàn bộ số không). Kể từ phiên bản 0.9.3, expiration được giả định bằng không và không được lưu trữ, do đó bất kỳ expiration khác không nào sẽ thất bại trong quá trình xác minh chữ ký RouterInfo. Việc triển khai expiration (hoặc sử dụng khác cho các byte này) sẽ là một thay đổi không tương thích ngược. Các router PHẢI đặt trường này thành toàn bộ số không. Kể từ phiên bản 0.9.12, trường expiration khác không lại được nhận diện, tuy nhiên chúng ta phải đợi vài phiên bản nữa để sử dụng trường này, cho đến khi phần lớn mạng lưới nhận diện được nó.

* Các tùy chọn sau đây, mặc dù không bắt buộc, nhưng là tiêu chuẩn và được mong đợi có mặt trong hầu hết các địa chỉ router: "host" (một địa chỉ IPv4 hoặc IPv6 hoặc tên máy chủ) và "port".

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterAddress.html

### RouterInfo

#### Mô tả

Định nghĩa tất cả dữ liệu mà một router muốn công bố cho mạng lưới thấy. [RouterInfo](#routerinfo) là một trong hai cấu trúc được lưu trữ trong cơ sở dữ liệu mạng (cái còn lại là [LeaseSet](#leaseset)), và được đánh khóa dưới SHA256 của [RouterIdentity](#routeridentity) được chứa bên trong.

#### Nội dung

[RouterIdentity](#routeridentity) theo sau bởi [Date](#date), khi mục được xuất bản

```
+----+----+----+----+----+----+----+----+
| router_ident                          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| published                             |
+----+----+----+----+----+----+----+----+
|size| RouterAddress 0                  |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| RouterAddress 1                       |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| RouterAddress ($size-1)               |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+-/-+----+----+----+
|psiz| options                          |
+----+----+----+----+-/-+----+----+----+
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

router_ident :: `RouterIdentity`
                length -> >= 387+ bytes

published :: `Date`
             length -> 8 bytes

size :: `Integer`
        length -> 1 byte
        The number of `RouterAddress`es to follow, 0-255

addresses :: [`RouterAddress`]
             length -> varies

peer_size :: `Integer`
             length -> 1 byte
             The number of peer `Hash`es to follow, 0-255, unused, always zero
             value -> 0

options :: `Mapping`

signature :: `Signature`
             length -> 40 bytes or as specified in router_ident's key
                       certificate
```
#### Ghi chú

* Giá trị peer_size [Integer](#integer) có thể được theo sau bởi một danh sách chứa nhiều router hash tương ứng.
  Tính năng này hiện tại không được sử dụng. Nó được thiết kế cho một dạng restricted routes,
  nhưng chưa được triển khai.
  Một số implementation có thể yêu cầu danh sách phải được sắp xếp để chữ ký không thay đổi.
  Cần nghiên cứu thêm trước khi kích hoạt tính năng này.

* Chữ ký có thể được xác minh bằng cách sử dụng khóa công khai ký của
  router_ident.

* Xem trang cơ sở dữ liệu mạng [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo) để biết các tùy chọn tiêu chuẩn dự kiến có trong tất cả thông tin router.

* Các router rất cũ yêu cầu các địa chỉ phải được sắp xếp theo SHA256 của dữ liệu của chúng
  để chữ ký không thay đổi.
  Điều này không còn được yêu cầu nữa, và không đáng để triển khai cho khả năng tương thích ngược.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterInfo.html

### Hướng Dẫn Giao Hàng

Hướng dẫn Giao hàng Thông điệp Tunnel được định nghĩa trong Đặc tả Thông điệp Tunnel [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions).

Hướng dẫn Giao hàng Thông điệp Garlic được định nghĩa trong Đặc tả Thông điệp I2NP [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions).

## Tài liệu tham khảo

- [ECIES](/docs/specs/ecies/)
- [ECIES-HYBRID](/docs/specs/ecies-hybrid/)
- [ECIES-ROUTERS](/docs/specs/ecies-routers/)
- [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy)
- [ELGAMAL-AES](/docs/specs/elgamal-aes/)
- [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions)
- [I2CP](/docs/specs/i2cp/)
- [I2NP](/docs/specs/i2np/)
- [NAMING](/docs/overview/naming/)
- [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo)
- [Prop134](/proposals/134-gost/)
- [Prop169](/proposals/169-pq-crypto/)
- [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
- [SSU](/docs/legacy/ssu/)
- [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions)
