---
title: "Ortak yapılar Spesifikasyonu"
description: "Tüm I2P protokollerinde ortak olan veri türleri"
slug: "common-structures"
category: "Tasarım"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

Bu belge, [I2NP](/docs/specs/i2np/), [I2CP](/docs/specs/i2cp/), [SSU](/docs/legacy/ssu/) vb. gibi tüm I2P protokollerinde ortak olan bazı veri türlerini açıklar.

## Ortak tür belirtimi

### Tamsayı

#### Açıklama

Negatif olmayan bir tam sayıyı temsil eder.

#### İçindekiler

Network byte order'da (big endian) işaretsiz bir tamsayıyı temsil eden 1 ila 8 byte.

### Tarih

#### Açıklama

1 Ocak 1970 gece yarısından itibaren GMT saat diliminde geçen milisaniye sayısı. Sayı 0 ise, tarih tanımsız veya null'dur.

#### İçindekiler

8 bayt [Integer](#integer)

### Dize

#### Açıklama

UTF-8 kodlu bir dizeyi temsil eder.

#### İçindekiler

İlk byte'ın string'deki byte sayısını (karakter sayısını değil!) belirttiği ve kalan 0-255 byte'ın null ile sonlandırılmamış UTF-8 kodlamalı karakter dizisi olduğu 1 veya daha fazla byte. Uzunluk sınırı 255 byte'dır (karakter değil). Uzunluk 0 olabilir.

### PublicKey

#### Açıklama

Bu yapı ElGamal veya diğer asimetrik şifreleme yöntemlerinde kullanılır ve yalnızca üssü temsil eder, sabit olan ve kriptografi spesifikasyonunda [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy) tanımlanan asal sayıları değil. Diğer şifreleme şemaları tanımlanma sürecindedir, aşağıdaki tabloya bakın.

#### İçindekiler

Anahtar türü ve uzunluğu bağlamdan çıkarılır veya bir Destination ya da RouterInfo'nun Key Certificate'ında veya [LeaseSet2](#leaseset2) ya da diğer veri yapılarındaki alanlarda belirtilir. Varsayılan tür ElGamal'dır. 0.9.38 sürümünden itibaren, bağlama bağlı olarak diğer türler de desteklenebilir. Aksi belirtilmedikçe anahtarlar big-endian formatındadır.

X25519 anahtarları, 0.9.44 sürümünden itibaren Destinations ve LeaseSet2'de desteklenmektedir. X25519 anahtarları, 0.9.48 sürümünden itibaren RouterIdentities'de desteklenmektedir.

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

#### Açıklama

Bu yapı ElGamal veya diğer asimetrik şifre çözmede kullanılır ve yalnızca üssü temsil eder, kriptografi spesifikasyonunda [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy) sabit olarak tanımlanan asalları değil. Diğer şifreleme şemaları tanımlanma sürecindedir, aşağıdaki tabloya bakınız.

#### İçindekiler

Anahtar türü ve uzunluğu bağlamdan çıkarılır veya bir veri yapısında ya da özel anahtar dosyasında ayrı olarak saklanır. Varsayılan tür ElGamal'dır. 0.9.38 sürümü itibariyle, bağlama bağlı olarak diğer türler desteklenebilir. Aksi belirtilmedikçe anahtarlar big-endian formatındadır.

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

#### Açıklama

Bu yapı simetrik AES256 şifreleme ve şifre çözme için kullanılır.

#### İçindekiler

32 bayt

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionKey.html

### SigningPublicKey

#### Açıklama

Bu yapı imzaları doğrulamak için kullanılır.

#### İçindekiler

Anahtar türü ve uzunluğu bağlamdan çıkarılır veya bir Destination'ın Key Certificate'ında belirtilir. Varsayılan tür DSA_SHA1'dir. 0.9.12 sürümü itibariyle, bağlama bağlı olarak diğer türler de desteklenebilir.

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
#### Notlar

* Bir anahtar iki elemandan oluştuğunda (örneğin X,Y noktaları), gerekirse her elemanı önde sıfırlar eklenerek uzunluk/2'ye doldurularak serileştirilir.

* Tüm türler Big Endian formatındadır, EdDSA ve RedDSA hariç, bunlar Little Endian formatında saklanır ve iletilir.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPublicKey.html

### SigningPrivateKey

#### Açıklama

Bu yapı imza oluşturmak için kullanılır.

#### İçindekiler

Anahtar türü ve uzunluğu oluşturulurken belirtilir. Varsayılan tür DSA_SHA1'dir. 0.9.12 sürümü itibariyle, bağlama bağlı olarak diğer türler de desteklenebilir.

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
#### Notlar

* Bir anahtar iki elemandan oluştuğunda (örneğin X,Y noktaları), her eleman gerekirse başına sıfırlar eklenerek uzunluk/2'ye doldurularak serileştirilir.

* Tüm türler Big Endian formatındadır, EdDSA ve RedDSA hariç - bunlar Little Endian formatında saklanır ve iletilir.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPrivateKey.html

### İmza

#### Açıklama

Bu yapı, bazı verilerin imzasını temsil eder.

#### İçindekiler

İmza türü ve uzunluğu kullanılan anahtar türünden çıkarılır. Varsayılan tür DSA_SHA1'dir. 0.9.12 sürümünden itibaren, bağlama bağlı olarak diğer türler de desteklenebilir.

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
#### Notlar

* Bir imza iki elemandan oluştuğunda (örneğin R,S değerleri), gerekirse her eleman önde sıfırlarla uzunluk/2'ye tamamlanarak serileştirilir.

* Tüm türler Big Endian formatındadır, EdDSA ve RedDSA hariç; bunlar Little Endian formatında saklanır ve iletilir.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Signature.html

### Hash

#### Açıklama

Bazı verilerin SHA256 değerini temsil eder.

#### İçindekiler

32 bayt

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Hash.html

### Session Tag

Not: ECIES-X25519 hedefleri (ratchet) ve ECIES-X25519 router'ları için Session Tag'ları 8 bayttır. [ECIES](/docs/specs/ecies/) ve [ECIES-ROUTERS](/docs/specs/ecies-routers/) belgelerine bakınız.

#### Açıklama

Rastgele bir sayı

#### İçindekiler

32 bayt

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionTag.html

### TunnelId

#### Açıklama

Bir tunnel'daki her router için benzersiz olan bir tanımlayıcı belirler. Tunnel ID genellikle sıfırdan büyüktür; özel durumlar dışında sıfır değerini kullanmayın.

#### İçindekiler

4 byte [Integer](#integer)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/TunnelId.html

### Sertifika

#### Açıklama

Sertifika, I2P ağı genelinde kullanılan çeşitli makbuzlar veya iş kanıtları için bir kapsayıcıdır.

#### İçindekiler

Sertifika türünü belirten 1 byte [Integer](#integer), ardından sertifika yükünün boyutunu belirten 2 byte [Integer](#integer), sonra o kadar byte.

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
#### Notlar

* [Router Identities](#routeridentity) için, Certificate versiyon 0.9.15'e kadar her zaman NULL'dur. 0.9.16 sürümünden itibaren, anahtar türlerini belirtmek için bir Key Certificate kullanılır. 0.9.48 sürümünden itibaren, X25519 şifreleme public key türlerine izin verilir. Aşağıya bakınız.

* [Garlic Cloves](/docs/specs/i2np/#struct-garlicclove) için, Certificate her zaman NULL'dur, şu anda başka hiçbiri uygulanmamıştır.

* [Garlic Messages](/docs/specs/i2np/#msg-garlic) için, Sertifika her zaman NULL'dur, şu anda başka hiçbiri uygulanmamıştır.

* [Destinations](#destination) için, Sertifika non-NULL olabilir. 0.9.12 sürümü itibariyle, imzalama genel anahtarı türünü belirtmek için bir Anahtar Sertifikası kullanılabilir. Aşağıya bakınız.

* Uygulayıcılar, Sertifikalarda fazla veri bulunmasını yasaklamaları konusunda uyarılmaktadır.
  Her sertifika türü için uygun uzunluk zorunlu kılınmalıdır.

#### Sertifika Türleri

Aşağıdaki sertifika türleri tanımlanmıştır:

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
#### Anahtar Sertifikaları

Anahtar sertifikaları 0.9.12 sürümünde tanıtıldı. Bu sürümden önce, tüm PublicKey'ler 256 baytlık ElGamal anahtarları ve tüm SigningPublicKey'ler 128 baytlık DSA-SHA1 anahtarlarıydı. Bir anahtar sertifikası, Destination veya RouterIdentity içindeki PublicKey ve SigningPublicKey türünü belirtmek ve standart uzunlukları aşan herhangi bir anahtar verisini paketlemek için bir mekanizma sağlar.

Sertifikadan önce tam olarak 384 bayt tutarak ve fazla anahtar verilerini sertifikanın içine koyarak, Destination'ları ve Router Identity'leri ayrıştıran herhangi bir yazılımla uyumluluğu korumuş oluruz.

Anahtar sertifikası yükü şunları içerir:

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
Uyarı: Anahtar türü sırası beklediğinizin tersine olabilir; İmzalama Genel Anahtar Türü önce gelir.

Tanımlanan İmzalama Genel Anahtar türleri şunlardır:

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
Tanımlı Kripto Genel Anahtar türleri şunlardır:

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
Bir Key Certificate mevcut olmadığında, Destination veya RouterIdentity içindeki önceki 384 byte, 256-byte ElGamal PublicKey'i takip eden 128-byte DSA-SHA1 SigningPublicKey olarak tanımlanır. Bir Key Certificate mevcut olduğunda, önceki 384 byte aşağıdaki gibi yeniden tanımlanır:

* Crypto Public Key'in tamamı veya ilk bölümü

* İki anahtarın toplam uzunluğu 384 bayttan azsa rastgele doldurma

* İmzalama Genel Anahtarının tamamı veya ilk kısmı

Crypto Public Key başlangıçta hizalanır ve Signing Public Key sonunda hizalanır. Dolgu (varsa) ortada yer alır. Sertifikalardaki başlangıç anahtar verisi, dolgu ve fazla anahtar verisi bölümlerinin uzunlukları ve sınırları açık olarak belirtilmez, ancak belirtilen anahtar türlerinin uzunluklarından türetilir. Crypto ve Signing Public Key'lerin toplam uzunlukları 384 baytı aşarsa, kalan kısım Key Certificate içinde yer alacaktır. Crypto Public Key uzunluğu 256 bayt değilse, iki anahtar arasındaki sınırı belirleme yöntemi bu belgenin gelecekteki bir revizyonunda belirtilecektir.

Belirtilen ElGamal Crypto Public Key ve Signing Public Key türü kullanılarak örnek düzenler:

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

#### Notlar

* Uygulayıcılar Key Certificate'larda fazla veri bulunmasını yasaklama konusunda uyarılır.
  Her sertifika türü için uygun uzunluk zorlanmalıdır.

* Tip 0,0 (ElGamal,DSA_SHA1) olan bir KEY sertifikası izin verilir ancak önerilmez.
  İyi test edilmemiştir ve bazı uygulamalarda sorunlara neden olabilir.
  Bir (ElGamal,DSA_SHA1) Destination veya RouterIdentity'nin kanonik temsilinde
  NULL sertifika kullanın, bu KEY sertifikası kullanmaktan 4 bayt daha kısa olacaktır.

### Eşleme

#### Açıklama

Bir anahtar/değer eşlemeleri veya özellikler kümesi

#### İçindekiler

2-byte boyutunda bir Integer ve ardından bir dizi String=String; çifti.

UYARI: Mapping'in çoğu kullanımı imzalı yapılarda olup, burada Mapping girişleri anahtar değerine göre sıralanmış olmalıdır, böylece imza değişmez kalır. Anahtar değerine göre sıralama yapılmaması imza hatalarına neden olacaktır!

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
#### Notlar

* Kodlama optimal değil - ya '=' ve ';' karakterlerine ihtiyacımız var, ya da
  string uzunluklarına, ama ikisine birden değil

* Bazı belgeler, dizelerin '=' veya ';' içeremeyeceğini belirtir ancak bu kodlama bunları destekler

* String'ler UTF-8 olarak tanımlanır ancak mevcut implementasyonda, I2CP UTF-8 kullanır fakat I2NP kullanmaz. Örneğin, bir I2NP Database Store Message'ındaki RouterInfo seçenekleri eşlemesindeki UTF-8 string'ler bozulacaktır.

* Kodlama çift anahtarlara izin verir, ancak eşlemenin imzalandığı herhangi bir kullanımda, çiftler imza hatasına neden olabilir.

* I2NP mesajlarında bulunan eşlemeler (örneğin RouterAddress veya RouterInfo'da)
  imzanın değişmez olması için anahtara göre sıralanmış olmalıdır. Yinelenen anahtarlara
  izin verilmez.

* Bir [I2CP SessionConfig](/docs/specs/i2cp/#struct-sessionconfig) içinde bulunan eşlemeler, imzanın değişmez olması için anahtara göre sıralanmış olmalıdır. Yinelenen anahtarlara izin verilmez.

* Sıralama yöntemi, karakterlerin Unicode değerlerini kullanarak Java String.compareTo() metodunda olduğu gibi tanımlanır.

* Uygulamaya bağlı olsa da, anahtarlar ve değerler genellikle büyük-küçük harf duyarlıdır.

* Anahtar ve değer dizesi uzunluk sınırları her biri için 255 bayt (karakter değil) artı
  uzunluk baytıdır. Uzunluk baytı 0 olabilir.

* Toplam uzunluk sınırı 65535 bayttır, artı 2 bayt boyut alanı, toplamda 65537'dir.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/DataHelper.html

## Ortak yapı spesifikasyonu

### KeysAndCert

#### Açıklama

Bir RouterIdentity veya Destination olarak kullanılan şifreleme genel anahtarı, imzalama genel anahtarı ve sertifika.

#### İçindekiler

Bir [PublicKey](#publickey) ardından bir [SigningPublicKey](#signingpublickey) ve sonra bir [Certificate](#certificate).

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
#### Padding Üretim Yönergeleri

Bu yönergeler Öneri 161'de önerildi ve API sürüm 0.9.57'de uygulandı. Bu yönergeler 0.6 (2005) sürümünden itibaren tüm sürümlerle geriye dönük uyumludur. Arka plan ve daha fazla bilgi için Öneri 161'e bakın.

ElGamal + DSA-SHA1 dışında şu anda kullanılan herhangi bir anahtar türü kombinasyonu için dolgu mevcut olacaktır. Ayrıca, hedefler için 256 baytlık genel anahtar alanı 0.6 sürümünden (2005) beri kullanılmamaktadır.

Geliştiriciler, Destination public key'leri ile Destination ve Router Identity padding için rastgele veri üretirken, bu verilerin çeşitli I2P protokollerinde sıkıştırılabilir olmasını sağlamalı, aynı zamanda güvenli kalmalı ve Base 64 temsillerinin bozuk veya güvensiz görünmemesini garanti etmelidir. Bu yaklaşım, padding alanlarını kaldırmanın sağladığı faydaların çoğunu, herhangi bir yıkıcı protokol değişikliği olmadan sunar.

Kesin olarak konuşmak gerekirse, 32-baytlık imzalama açık anahtarının tek başına (hem Destination'larda hem de Router Identity'lerde) ve 32-baytlık şifreleme açik anahtarının (yalnızca Router Identity'lerde) bu yapıların SHA-256 hash'lerinin kriptografik olarak güçlü olması ve netDb DHT'sinde rastgele dağıtılması için gerekli tüm entropiyi sağlayan rastgele bir sayı olmasıdır.

Ancak, fazladan ihtiyatlı olmak adına, ElG public key alanında ve padding'de minimum 32 bayt rastgele veri kullanılmasını öneriyoruz. Ayrıca, alanların tümü sıfır olsaydı, Base 64 hedefler uzun AAAA karakter dizileri içerecekti, bu da kullanıcılarda endişe veya kafa karışıklığına neden olabilir.

32 baytlık rastgele veriyi, tam KeysAndCert yapısının I2NP Database Store Message, Streaming SYN, SSU2 handshake ve yanıtlanabilir Datagram'lar gibi I2P protokollerinde yüksek oranda sıkıştırılabilir olması için gerektiği kadar tekrarlayın.

Örnekler:

* X25519 şifreleme türü ve Ed25519 imza türüne sahip bir Router Identity, rastgele verinin 10 kopyasını (320 bayt) içerecek ve sıkıştırıldığında yaklaşık 288 bayt tasarruf sağlayacaktır.

* Ed25519 imza türüne sahip bir Destination
  rastgele verinin 11 kopyasını (352 bayt) içerecektir, sıkıştırıldığında yaklaşık 320 bayt tasarruf sağlar.

Uygulamalar, yapının SHA-256 hash'i tam içeriği kapsadığı için elbette tam 387+ bayt yapıyı saklamak zorundadır.

#### Notlar

* Bunların her zaman 387 bayt olduğunu varsaymayın! Bunlar 387 bayt artı 385-386 baytlarında belirtilen sertifika uzunluğudur ve bu sıfırdan farklı olabilir.

* 0.9.12 sürümünden itibaren, sertifika bir Key Certificate ise, anahtar alanlarının sınırları değişebilir. Ayrıntılar için yukarıdaki Key Certificate bölümüne bakın.

* Crypto Public Key başlangıçta hizalanır ve Signing Public Key sonunda hizalanır. Dolgu (varsa) ortadadır.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/KeysAndCert.html

### RouterIdentity

#### Açıklama

Belirli bir router'ı benzersiz şekilde tanımlamanın yolunu tanımlar

#### İçindekiler

KeysAndCert ile aynı.

Padding alanı için rastgele veri oluşturma yönergeleri için [KeysAndCert](#keysandcert) bölümüne bakın.

#### Notlar

* RouterIdentity için sertifika, 0.9.12 sürümüne kadar her zaman NULL idi.

* Bunların her zaman 387 bayt olduğunu varsaymayın! Bunlar 387 bayt artı 385-386 baytlarında belirtilen sertifika uzunluğudur ve bu sıfır olmayabilir.

* 0.9.12 sürümü itibariyle, sertifika bir Key Certificate ise, anahtar alanlarının sınırları değişebilir. Ayrıntılar için yukarıdaki Key Certificate bölümüne bakın.

* Crypto Public Key başlangıçta hizalanır ve Signing Public Key sonunda hizalanır. Dolgu (varsa) ortadadır.

* Anahtar sertifikası ve ECIES_X25519 public key içeren RouterIdentity'ler 0.9.48 sürümünden itibaren desteklenmektedir.
  Bundan önce, tüm RouterIdentity'ler ElGamal idi.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterIdentity.html

### Hedef

#### Açıklama

Bir Destination, mesajların güvenli teslimat için yönlendirilebileceği belirli bir uç noktayı tanımlar.

#### İçindekiler

[KeysAndCert](#keysandcert) ile aynıdır, ancak public key hiçbir zaman kullanılmaz ve geçerli bir ElGamal Public Key yerine rastgele veri içerebilir.

Public key ve padding alanları için rastgele veri üretme yönergeleri için [KeysAndCert](#keysandcert) bölümüne bakın.

#### Notlar

* Hedefin public key'i, 0.6 sürümünde (2005) devre dışı bırakılan eski i2cp-to-i2cp şifrelemesi için kullanılıyordu, şu anda kullanımdan kaldırılmış olan LeaseSet şifrelemesi için IV dışında kullanılmamaktadır. Bunun yerine LeaseSet'teki public key kullanılır.

* Bunların her zaman 387 bayt olduğunu varsaymayın! Bunlar 387 bayt artı 385-386 baytlarında belirtilen sertifika uzunluğudur ve bu sıfır olmayabilir.

* Sürüm 0.9.12 itibariyle, sertifika bir Key Certificate ise, anahtar alanlarının sınırları değişebilir. Ayrıntılar için yukarıdaki Key Certificate bölümüne bakın.

* Crypto Public Key başlangıçta hizalanır ve Signing Public Key sonunda hizalanır. Padding (varsa) ortadadır.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Destination.html

### Lease

#### Açıklama

Belirli bir tunnel'ın bir [Destination](#destination)'ı hedef alan mesajları alması için gereken yetkilendirmeyi tanımlar.

#### İçindekiler

Gateway router'ın [RouterIdentity](#routeridentity)'sinin SHA256 [Hash](#hash)'i, ardından [TunnelId](#tunnelid) ve son olarak bitiş [Date](#date)'i.

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
#### Notlar

* Toplam boyut: 44 bayt

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease.html

### LeaseSet

#### Açıklama

Belirli bir [Destination](#destination) için şu anda yetkili olan tüm [Lease](#lease)'leri, garlic mesajlarının şifrelenebileceği [PublicKey](#publickey)'i ve ardından bu yapının belirli sürümünü iptal etmek için kullanılabilecek [SigningPublicKey](#signingpublickey)'i içerir. LeaseSet, network database'de saklanan iki yapıdan biridir (diğeri [RouterInfo](#routerinfo)) ve içerdiği [Destination](#destination)'ın SHA256'sı altında anahtarlanır.

#### İçindekiler

[Destination](#destination), ardından şifreleme için bir [PublicKey](#publickey), sonra LeaseSet'in bu sürümünü iptal etmek için kullanılabilen bir [SigningPublicKey](#signingpublickey), daha sonra sette kaç [Lease](#lease) yapısı olduğunu belirten 1 byte'lık bir [Integer](#integer), ardından gerçek [Lease](#lease) yapıları ve son olarak [Destination](#destination)'ın [SigningPrivateKey](#signingprivatekey)'i ile imzalanmış önceki byte'ların bir [Signature](#signature)'ı.

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
#### Notlar

* Hedefin public key'i, 0.6 sürümünde devre dışı bırakılan eski I2CP-to-I2CP şifreleme için kullanılıyordu, şu anda kullanılmamaktadır.

* Şifreleme anahtarı, uçtan uca ElGamal/AES+SessionTag şifrelemesi 
  [ELGAMAL-AES](/docs/specs/elgamal-aes/) için kullanılır. Şu anda her router başlatılışında yeniden oluşturulur, 
  kalıcı değildir.

* İmza, hedefin imzalama açık anahtarı kullanılarak doğrulanabilir.

* Sıfır Lease içeren bir LeaseSet'e izin verilir ancak kullanılmaz.
  Bu, uygulanmamış olan LeaseSet iptali için tasarlanmıştı.
  Tüm LeaseSet2 varyantları en az bir Lease gerektirir.

* signing_key şu anda kullanılmamaktadır. LeaseSet iptal işlemi için tasarlanmıştı,
  ancak henüz uygulanmamıştır. Şu anda her router başlatılışında yeniden oluşturulur,
  kalıcı değildir. Signing key türü her zaman hedefin signing key türüyle aynıdır.

* Tüm Lease'lerin en erken sona erme tarihi, LeaseSet'in zaman damgası veya sürümü olarak kabul edilir. Router'lar genellikle mevcut olandan "daha yeni" olmadığı sürece bir LeaseSet'in saklanmasını kabul etmezler. En eski Lease'in önceki LeaseSet'teki en eski Lease ile aynı olduğu yeni bir LeaseSet yayınlarken dikkatli olun. Yayınlayan router, bu durumda genellikle en eski Lease'in sona erme süresini en az 1 ms artırmalıdır.

* 0.9.7 sürümünden önce, kaynak router tarafından gönderilen bir DatabaseStore Mesajına dahil edildiğinde, router yayınlanan tüm leaseların sona erme sürelerini aynı değere, yani en erken lease'in değerine ayarlardı. 0.9.7 sürümünden itibaren, router her lease için gerçek lease sona erme süresini yayınlar. Bu bir uygulama detayıdır ve yapılar spesifikasyonunun bir parçası değildir.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet.html

### Lease2

#### Açıklama

Belirli bir tunnel'ın bir [Destination](#destination)'ı hedefleyen mesajları alması için yetkilendirmeyi tanımlar. [Lease](#lease) ile aynıdır ancak 4-byte end_date ile. [LeaseSet2](#leaseset2) tarafından kullanılır. 0.9.38 sürümünden itibaren desteklenir; daha fazla bilgi için proposal 123'e bakınız.

#### İçindekiler

Gateway router'ın [RouterIdentity](#routeridentity)'sinin SHA256 [Hash](#hash)'i, ardından [TunnelId](#tunnelid) ve son olarak 4 baytlık bitiş tarihi.

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
#### Notlar

* Toplam boyut: 40 bayt

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease2.html

### OfflineSignature

#### Açıklama

Bu, [LeaseSet2Header](#leaseset2header)'ın isteğe bağlı bir parçasıdır. Ayrıca streaming ve I2CP'de de kullanılır. 0.9.38 sürümünden itibaren desteklenir; daha fazla bilgi için öneri 123'e bakın.

#### İçindekiler

Bir son kullanma tarihi, sigtype ve geçici [SigningPublicKey](#signingpublickey), ve bir [Signature](#signature) içerir.

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
#### Notlar

* Bu bölüm çevrimdışı olarak oluşturulabilir ve oluşturulmalıdır.

### LeaseSet2Header

#### Açıklama

Bu, [LeaseSet2](#leaseset2) ve [MetaLeaseSet](#metaleaseset)'in ortak kısmıdır. 0.9.38 sürümünden itibaren desteklenmektedir; daha fazla bilgi için 123 numaralı öneriyi inceleyin.

#### İçindekiler

[Destination](#destination), iki zaman damgası ve isteğe bağlı bir [OfflineSignature](#offlinesignature) içerir.

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
#### Notlar

* Toplam boyut: minimum 395 bayt

* Maksimum gerçek sona erme süresi [LeaseSet2](#leaseset2) için yaklaşık 660 (11 dakika) ve [MetaLeaseSet](#metaleaseset) için 65535 (tam 18,2 saat)'tir.

* [LeaseSet](#leaseset) (1) bir 'published' alanına sahip değildi, bu nedenle sürümleme
  en erken lease için arama gerektiriyordu. LeaseSet2, bir saniyelik çözünürlükle
  bir 'published' alanı ekler. Router'lar yeni leaseset'leri floodfill'lere gönderme
  hızını saniyede bir defadan çok daha yavaş bir hıza sınırlandırmalıdır (hedef başına).
  Bu uygulanmazsa, kod her yeni leaseset'in 'published' zamanının
  bir öncekinden en az bir saniye sonra olduğundan emin olmalıdır, aksi takdirde
  floodfill'ler yeni leaseset'i depolamaz veya yaymaz.

### LeaseSet2

#### Açıklama

Tip 3 I2NP DatabaseStore mesajında bulunur. 0.9.38 sürümünden itibaren desteklenir; daha fazla bilgi için öneri 123'e bakın.

Belirli bir [Destination](#destination) için şu anda yetkilendirilmiş tüm [Lease2](#lease2)'leri ve garlic mesajlarının şifrelenebileceği [PublicKey](#publickey)'i içerir. LeaseSet, ağ veritabanında saklanan iki yapıdan biridir (diğeri [RouterInfo](#routerinfo)'dur) ve içerdiği [Destination](#destination)'ın SHA256'sı altında anahtarlanır.

#### İçindekiler

[LeaseSet2Header](#leaseset2header), ardından seçenekler, sonra şifreleme için bir veya daha fazla [PublicKey](#publickey), küme içinde kaç [Lease2](#lease2) yapısı olduğunu belirten [Integer](#integer), ardından gerçek [Lease2](#lease2) yapıları ve son olarak [Destination](#destination)'ın [SigningPrivateKey](#signingprivatekey)'i veya geçici anahtar tarafından imzalanmış önceki baytların [Signature](#signature)'ı.

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
#### Şifreleme Anahtarı Tercihi

Yayınlanmış (sunucu) leaseSet'ler için, şifreleme anahtarları sunucu tercihine göre sıralanır, en çok tercih edilen önce gelir. İstemciler birden fazla şifreleme türünü destekliyorsa, sunucu tercihini dikkate almaları ve sunucuya bağlanmak için kullanılacak şifreleme yöntemi olarak desteklenen ilk türü seçmeleri önerilir. Genellikle, daha yeni (daha yüksek numaralı) anahtar türleri daha güvenli veya verimlidir ve tercih edilir, bu nedenle anahtarlar anahtar türünün ters sırasında listelenmelidir.

Ancak istemciler, uygulamaya bağlı olarak, bunun yerine kendi tercihlerine göre seçim yapabilir veya "birleştirilmiş" tercihi belirlemek için bir yöntem kullanabilir. Bu, bir yapılandırma seçeneği olarak veya hata ayıklama için yararlı olabilir.

Yayımlanmamış (istemci) leaseSet'lerdeki anahtar sırası etkin bir şekilde önemli değildir, çünkü yayımlanmamış istemcilere genellikle bağlantı girişimi yapılmaz. Yukarıda açıklandığı gibi, bu sıra birleşik bir tercih belirlemek için kullanılmadıkça.

#### Seçenekler

API 0.9.66 itibariyle, servis kayıt seçenekleri için standart bir format tanımlanmıştır. Ayrıntılar için 167 numaralı öneriye bakınız. Farklı format kullanan servis kayıtları dışındaki seçenekler gelecekte tanımlanabilir.

LS2 seçenekleri anahtar değerine göre sıralanmalıdır, böylece imza değişmez kalır.

Servis kayıt seçenekleri aşağıdaki gibi tanımlanır:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := İstenen servisin sembolik adı. Küçük harf olmalıdır. Örnek: "smtp".
  İzin verilen karakterler [a-z0-9-] ve '-' ile başlayamaz veya bitemez.
  [REGISTRY](http://www.dns-sd.org/ServiceTypes.html) veya Linux /etc/services dosyasında tanımlanmışsa standart tanımlayıcılar kullanılmalıdır.
- proto := İstenen servisin taşıma protokolü. Küçük harf olmalıdır, "tcp" veya "udp" olabilir.
  "tcp" akış (streaming) anlamına gelir ve "udp" yanıtlanabilir datagramlar anlamına gelir.
  Ham datagramlar ve datagram2 için protokol göstergeleri daha sonra tanımlanabilir.
  İzin verilen karakterler [a-z0-9-] ve '-' ile başlayamaz veya bitemez.
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := yaşam süresi (time to live), saniye cinsinden tamsayı. Pozitif tamsayı. Örnek: "86400".
  Aşağıdaki Öneriler bölümündeki ayrıntılar için minimum 86400 (bir gün) önerilir.
- priority := Hedef sunucunun önceliği, düşük değer daha çok tercih edilen anlamına gelir. Negatif olmayan tamsayı. Örnek: "0"
  Yalnızca birden fazla kayıt varsa yararlıdır, ancak tek kayıt olsa bile gereklidir.
- weight := Aynı önceliğe sahip kayıtlar için göreceli ağırlık. Yüksek değer seçilme şansının daha fazla olduğu anlamına gelir. Negatif olmayan tamsayı. Örnek: "0"
  Yalnızca birden fazla kayıt varsa yararlıdır, ancak tek kayıt olsa bile gereklidir.
- port := Servisin bulunacağı I2CP portu. Negatif olmayan tamsayı. Örnek: "25"
  Port 0 desteklenir ancak önerilmez.
- target := Servisi sağlayan hedefin hostname veya b32 adresi. [NAMING](/docs/overview/naming/) içindeki geçerli hostname. Küçük harf olmalıdır.
  Örnek: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" veya "example.i2p".
  Hostname "iyi bilinen" değilse, yani resmi veya varsayılan adres defterlerinde değilse b32 önerilir.
- appoptions := uygulamaya özgü keyfi metin, " " veya "," içeremez. Kodlama UTF-8'dir.

Örnekler:

LS2'de aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p için, bir SMTP sunucusunu işaret eden:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

LS2'de aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p için, iki SMTP sunucusuna işaret eden:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p için LS2'de, kendisini bir SMTP sunucusu olarak işaret ederken:

"_smtp._tcp" "0 999999 25"

#### Notlar

* Hedefin public anahtarı, 0.6 sürümünde devre dışı bırakılan eski I2CP-to-I2CP şifreleme için kullanılıyordu, şu anda kullanılmıyor.

* Şifreleme anahtarları uçtan uca ElGamal/AES+SessionTag şifrelemesi
  [ELGAMAL-AES](/docs/specs/elgamal-aes/) (tip 0) veya diğer uçtan uca şifreleme şemaları için kullanılır.
  [ECIES](/docs/specs/ecies/) ve 145 ile 156 numaralı önerilere bakın.
  Her router başlatımında yeniden oluşturulabilir
  veya kalıcı olabilirler.
  X25519 (tip 4, [ECIES](/docs/specs/ecies/) bakın) 0.9.44 sürümünden itibaren desteklenmektedir.

* İmza, yukarıdaki verinin ÖNCESİNE DatabaseStore türünü (3) içeren tek baytın EKLENMESİyle oluşan veri üzerindedir.

* İmza, hedefin imzalama genel anahtarı kullanılarak veya leaseset2 başlığında çevrimdışı bir imza bulunuyorsa geçici imzalama genel anahtarı kullanılarak doğrulanabilir.

* Her anahtar için anahtar uzunluğu sağlanır, böylece floodfill'ler ve istemciler tüm şifreleme türleri bilinmese veya desteklenmese bile yapıyı ayrıştırabilir.

* [LeaseSet2Header](#leaseset2header) bölümündeki 'published' alanı ile ilgili nota bakınız

* Seçenekler eşlemesi, boyutu birden büyükse, anahtar tarafından sıralanmış olmalıdır, böylece imza değişmez olur.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet2.html

### MetaLease

#### Açıklama

Belirli bir tunnel'ın bir [Destination](#destination)'ı hedefleyen mesajları alması için yetkilendirmeyi tanımlar. [Lease2](#lease2) ile aynıdır ancak tunnel id yerine bayraklar ve maliyet içerir. [MetaLeaseSet](#metaleaseset) tarafından kullanılır. Tip 7 I2NP DatabaseStore mesajında bulunur. 0.9.38 sürümünden itibaren desteklenir; daha fazla bilgi için 123 numaralı öneriye bakın.

#### İçindekiler

Gateway router'ının [RouterIdentity](#routeridentity)'sinin SHA256 [Hash](#hash)'i, ardından bayraklar ve maliyet, ve son olarak 4 baytlık bitiş tarihi.

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
#### Notlar

* Toplam boyut: 40 bayt

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLease.html

### MetaLeaseSet

#### Açıklama

Tip 7 I2NP DatabaseStore mesajında bulunur. 0.9.38 sürümünden itibaren tanımlanmıştır; 0.9.40 sürümünden itibaren çalışır duruma gelmesi planlanmıştır; daha fazla bilgi için 123 numaralı öneriyi görün.

Belirli bir [Destination](#destination) için şu anda yetkilendirilmiş tüm [MetaLease](#metalease)'leri ve garlic mesajlarının şifrelenebileceği [PublicKey](#publickey)'i içerir. LeaseSet, network veritabanında saklanan iki yapıdan biridir (diğeri [RouterInfo](#routerinfo)'dur) ve içerdiği [Destination](#destination)'ın SHA256'sı altında anahtarlanır.

#### İçindekiler

[LeaseSet2Header](#leaseset2header), ardından seçenekler, sette kaç tane [Lease2](#lease2) yapısı bulunduğunu belirten bir [Integer](#integer), ardından gerçek [Lease2](#lease2) yapıları ve son olarak önceki baytların [Destination](#destination)'ın [SigningPrivateKey](#signingprivatekey)'i veya geçici anahtar tarafından imzalandığı [Signature](#signature).

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
#### Notlar

* Destination'ın public key'i, 0.6 sürümünde devre dışı bırakılan eski I2CP-to-I2CP şifrelemesi için kullanılıyordu, şu anda kullanılmamaktadır.

* İmza, yukarıdaki verilerin üzerinde, DatabaseStore türünü (7) içeren tek baytın BAŞINA EKLENMESİ ile hesaplanır.

* İmza, hedefin imzalama genel anahtarı kullanılarak doğrulanabilir, ya da leaseset2 başlığında çevrimdışı bir imza bulunuyorsa geçici imzalama genel anahtarı kullanılabilir.

* [LeaseSet2Header](#leaseset2header) bölümündeki 'published' alanıyla ilgili nota bakın

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLeaseSet.html

### EncryptedLeaseSet

#### Açıklama

Tip 5'te bir I2NP DatabaseStore mesajında bulunur. 0.9.38 sürümünden itibaren tanımlanmıştır; 0.9.39 sürümünden itibaren çalışmaktadır; daha fazla bilgi için öneri 123'e bakınız.

Yalnızca körleştirilmiş anahtar ve son kullanma tarihi düz metin olarak görülebilir. Gerçek leaseSet şifrelenmiştir.

#### İçindekiler

İki baytlık bir imza türü, körleştirilmiş [SigningPrivateKey](#signingprivatekey), yayınlanma zamanı, son kullanma tarihi ve bayraklar. Ardından, iki baytlık uzunluk ve şifrelenmiş veri. Son olarak, körleştirilmiş [SigningPrivateKey](#signingprivatekey) veya geçici anahtar tarafından imzalanmış önceki baytların [Signature](#signature)'ı.

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
#### Notlar

* Hedefin public key'i, 0.6 sürümünde devre dışı bırakılan eski I2CP-to-I2CP
  şifrelemesi için kullanılıyordu, şu anda kullanılmamaktadır.

* İmza, yukarıdaki veriler üzerindedir ve DatabaseStore türünü (5) içeren tek bayt ile BAŞA EKLENMİŞTİR.

* İmza, hedefin imzalama public key'i kullanılarak doğrulanabilir veya eğer leaseset2 başlığında çevrimdışı bir imza bulunuyorsa, geçici imzalama public key'i kullanılarak doğrulanabilir.

* Gizleme ve şifreleme [EncryptedLeaseSet](/docs/specs/encryptedleaseset/) içinde belirtilmiştir

* Bu yapı [LeaseSet2Header](#leaseset2header) kullanmaz.

* Maksimum gerçek son kullanma süresi yaklaşık 660'tır (11 dakika), şifreli bir [MetaLeaseSet](#metaleaseset) olmadığı sürece.

* Şifrelenmiş leaseSet'ler ile çevrimdışı imzaların kullanımı hakkında notlar için öneri 123'e bakın.

* [LeaseSet2Header](#leaseset2header)'daki 'published' alanı hakkındaki nota bakın
  (aynı sorun, burada LeaseSet2Header formatını kullanmasak bile)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/EncryptedLeaseSet.html

### RouterAddress

#### Açıklama

Bu yapı, bir router ile taşıma protokolü aracılığıyla iletişim kurma yöntemlerini tanımlar.

#### İçindekiler

1 byte [Integer](#integer) adresin kullanım maliyetini tanımlayan değer, burada 0 ücretsiz ve 255 pahalı anlamına gelir, ardından adresin kullanılmaması gereken son kullanma [Date](#date) tarihi gelir, eğer null ise adresin süresi hiç dolmaz. Bundan sonra bu router adresinin kullandığı aktarım protokolünü tanımlayan bir [String](#string) gelir. Son olarak bağlantıyı kurmak için gerekli olan IP adresi, port numarası, e-posta adresi, URL vb. gibi aktarıma özgü tüm seçenekleri içeren bir [Mapping](#mapping) bulunur.

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
#### Notlar

* Maliyet genellikle SSU için 5 veya 6, NTCP için 10 veya 11'dir.

* Expiration şu anda kullanılmamaktadır, her zaman null'dur (tümü sıfır). 0.9.3 sürümü itibarıyla, expiration sıfır olarak varsayılır ve saklanmaz, bu nedenle sıfır olmayan herhangi bir expiration RouterInfo imza doğrulamasında başarısız olacaktır. Expiration'ı uygulamak (veya bu baytlar için başka bir kullanım) geriye dönük uyumsuz bir değişiklik olacaktır. Router'lar bu alanı tamamıyla sıfır olarak ayarlamalıdır. 0.9.12 sürümü itibarıyla, sıfır olmayan bir expiration alanı tekrar tanınmaktadır, ancak ağın büyük çoğunluğu bunu tanıyana kadar bu alanı kullanmak için birkaç sürüm beklememiz gerekir.

* Aşağıdaki seçenekler zorunlu olmamakla birlikte standarttır ve çoğu router adresinde bulunması beklenir: "host" (bir IPv4 veya IPv6 adresi ya da host adı) ve "port".

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterAddress.html

### RouterInfo

#### Açıklama

Bir router'ın ağın görmesi için yayınlamak istediği tüm verileri tanımlar. [RouterInfo](#routerinfo), ağ veritabanında depolanan iki yapıdan biridir (diğeri [LeaseSet](#leaseset)) ve içerdiği [RouterIdentity](#routeridentity)'nin SHA256'sı altında anahtarlanır.

#### İçindekiler

[RouterIdentity](#routeridentity) ve ardından girdinin yayınlandığı [Date](#date)

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
#### Notlar

* peer_size [Integer](#integer) değerini, o kadar router hash'inin listesi takip edebilir.
  Bu şu anda kullanılmamaktadır. Kısıtlı rotalar için bir form amaçlanmıştı,
  ancak henüz uygulanmamıştır.
  Bazı implementasyonlar, imzanın değişmez olması için listenin sıralanmasını gerektirebilir.
  Bu özelliği etkinleştirmeden önce araştırılması gerekmektedir.

* İmza, router_ident'in imzalama public key'i kullanılarak doğrulanabilir.

* Tüm router bilgilerinde bulunması beklenen standart seçenekler için network database sayfasındaki [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo) bölümüne bakın.

* Çok eski router'lar, imzanın değişmez olması için adreslerin verilerinin SHA256'sına göre sıralanmasını gerektiriyordu.
  Bu artık gerekli değildir ve geriye dönük uyumluluk için uygulanmaya değmez.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterInfo.html

### Teslimat Talimatları

Tunnel Mesaj Teslimat Talimatları, Tunnel Mesaj Spesifikasyonunda [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions) tanımlanmıştır.

Garlic Message Delivery Instructions, I2NP Mesaj Spesifikasyonunda [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions) tanımlanmıştır.

## Referanslar

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
