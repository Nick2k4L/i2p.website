---
title: "Şifreli LeaseSet'ler için B32"
description: "Şifrelenmiş LS2 leaseSet'leri için Base 32 adres formatı"
slug: "b32encrypted"
aliases:
  - "/tr/docs/specs/b32-for-encrypted-leasesets"
  - "/tr/docs/specs/b32-for-encrypted-leasesets/"
category: "Tasarım"
lastUpdated: "2020-08"
accurateFor: "0.9.47"
---

## Genel Bakış

Standart Base 32 ("b32") adresleri hedefin hash değerini içerir. Bu, şifreli ls2 (öneri 123) için çalışmayacaktır.

Şifrelenmiş bir LS2 (öneri 123) için geleneksel bir base 32 adresi kullanamayız, çünkü bu sadece hedefin hash'ini içerir. Köreltilmemiş public key'i sağlamaz. İstemciler leaseset'i almak ve şifresini çözmek için hedefin public key'ini, imza tipini, köreltilmiş imza tipini ve isteğe bağlı bir gizli anahtar veya private key bilmelidir. Bu nedenle, tek başına bir base 32 adresi yetersizdir. İstemci ya tam hedefe (public key içeren) ya da tek başına public key'e ihtiyaç duyar. İstemci bir adres defterinde tam hedefe sahipse ve adres defteri hash ile ters arama destekliyorsa, o zaman public key alınabilir.

Bu format, hash yerine public key'i base32 adresine koyar. Bu format aynı zamanda public key'in imza türünü ve blinding şemasının imza türünü de içermelidir.

Bu belge, bu adresler için bir b32 formatı belirtir. Tartışmalar sırasında bu yeni formatı "b33" adresi olarak adlandırmış olsak da, gerçek yeni format olağan ".b32.i2p" son ekini korur.

## Tasarım

- Yeni format, unblinded public key, unblinded sig type ve blinded sig type içerecek.
- İsteğe bağlı olarak yalnızca özel bağlantılar için bir secret ve/veya private key içerebilir
- Mevcut ".b32.i2p" sonekini kullanır, ancak daha uzun bir uzunlukla.
- Bir checksum ekler.
- Şifrelenmiş leaseSet'ler için adresler, geleneksel base 32 adreslerinin 52 karakter (32 byte) olmasına kıyasla, 56 veya daha fazla kodlanmış karakter (35 veya daha fazla çözümlenmiş byte) ile tanımlanır.

## Şartname

### Oluşturma ve kodlama

{56+ karakter}.b32.i2p şeklinde bir hostname (35+ karakter ikili formatta) aşağıdaki şekilde oluşturun:

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
İşlem sonrası ve sağlama toplamı:

```
Construct the binary data as above.
Treat checksum as little-endian.
Calculate checksum = CRC-32(data[3:end])
data[0] ^= (byte) checksum
data[1] ^= (byte) (checksum >> 8)
data[2] ^= (byte) (checksum >> 16)

hostname = Base32.encode(data) || ".b32.i2p"
```
b32'nin sonundaki kullanılmayan bitler 0 olmalıdır. Standart 56 karakterlik (35 bayt) bir adres için kullanılmayan bit bulunmaz.

### Kod Çözme ve Doğrulama

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
### Gizli ve Özel Anahtar Bitleri

Secret ve private key bitleri, client'lara, proxy'lere veya diğer client tarafı kodlara leaseSet'in şifresinin çözülmesi için secret ve/veya private key'in gerekli olacağını belirtmek için kullanılır. Belirli implementasyonlar kullanıcıdan gerekli veriyi sağlamasını isteyebilir veya gerekli veri eksikse bağlantı girişimlerini reddedebilir.

## Önbellekleme

Bu spesifikasyonun kapsamı dışında olsa da, router'lar ve/veya istemciler public key'den hedef adrese ve bunun tersine olan eşlemeyi hatırlamak ve (muhtemelen kalıcı olarak) önbelleğe almak zorundadır.

## Notlar

- Eski ve yeni türleri uzunluğa göre ayırt edin. Eski b32 adresleri
  her zaman {52 karakter}.b32.i2p şeklindedir. Yenileri {56+ karakter}.b32.i2p
- Tor tartışma başlığı:
  https://lists.torproject.org/pipermail/tor-dev/2017-January/011816.html
- 2-byte sigtypes'ların hiç gerçekleşeceğini beklemeyin, daha sadece 13'e kadar çıktık. 
  Şimdi implement etmeye gerek yok.
- Yeni format, tıpkı b32 gibi, istenirse jump linklerinde kullanılabilir (ve jump serverlar tarafından sunulabilir).

## Referanslar

- [CRC-32](https://en.wikipedia.org/wiki/CRC-32) - ayrıca bkz. [RFC 3309](https://tools.ietf.org/html/rfc3309)
