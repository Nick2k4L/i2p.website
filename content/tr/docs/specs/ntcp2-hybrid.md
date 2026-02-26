---
title: "PQ Hybrid NTCP2"
description: "ML-KEM kullanarak NTCP2 transport protokolünün post-quantum hibrit varyantı"
slug: "ntcp2-hybrid"
lastupdated: "2026-02"
category: "Taşıma Protokolleri"
accurateFor: "0.9.69"
---

### Durum

Beta Q1 2026, sürüm Q2 2026

## Genel Bakış

Bu, Öneri 169'da tasarlandığı şekliyle NTCP2 taşıma protokolünün hibrit post-kuantum varyantıdır. Ek bilgi için bu öneriye bakınız.

PQ Hybrid NTCP2 yalnızca standart NTCP2 ile aynı adres ve port üzerinde tanımlanır. Farklı bir port üzerinde çalışma veya standart NTCP2 desteği olmadan çalışma izin verilmez ve standart NTCP2'nin kullanımdan kaldırılacağı birkaç yıl boyunca da izin verilmeyecektir.

Bu spesifikasyon, yalnızca PQ Hybrid'i desteklemek için standart NTCP2'de gerekli olan değişiklikleri belgelemektedir. Temel uygulama ayrıntıları için NTCP2 spesifikasyonuna bakınız.

## Tasarım

NIST FIPS 203 ve 204 standartlarını destekliyoruz [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) bu standartlar CRYSTALS-Kyber ve CRYSTALS-Dilithium (sürüm 3.1, 3 ve daha eski) tabanlı olup ancak bunlarla uyumlu DEĞİLDİR.

### Anahtar Değişimi

PQ KEM yalnızca geçici anahtarlar sağlar ve Noise XK ve IK gibi statik anahtar el sıkışmalarını doğrudan desteklemez. Şifreleme türleri PQ Hybrid Ratchet'ta kullanılanlarla aynıdır ve [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)'te olduğu gibi ortak yapılar belgesinde [/docs/specs/common-structures/](/docs/specs/common-structures/) tanımlanmıştır. Hibrit türler yalnızca X25519 ile kombinasyon halinde tanımlanmıştır.

Şifreleme türleri şunlardır:

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Tür</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Kod</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">6</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">7</td>
</tr>
</table>### Yasal Kombinasyonlar

Yeni şifreleme türleri RouterAddresses içinde belirtilir. Anahtar sertifikasındaki şifreleme türü tip 4 olmaya devam edecektir.

## Şartname

### El Sıkışma Desenleri

El sıkışmalar [Noise Protocol](https://noiseprotocol.org/noise.html) el sıkışma desenlerini kullanır.

Aşağıdaki harf eşlemesi kullanılır:

- e = tek kullanımlık geçici anahtar
- s = statik anahtar
- p = mesaj yükü
- e1 = tek kullanımlık geçici PQ anahtarı, Alice'ten Bob'a gönderilir
- ekem1 = KEM şifreli metni, Bob'tan Alice'e gönderilir

Hibrit ileri gizlilik (hfs) için XK ve IK'ya aşağıdaki değişiklikler [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) bölüm 5'te belirtildiği gibidir:

```
XK:                       XKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, p               -> e, es, e1, p
  <- e, ee, p               <- e, ee, ekem1, p
  -> s, se                  -> s, se
  <- p                      <- p
  p ->                      p ->


  e1 and ekem1 are encrypted. See pattern definitions below.
  NOTE: e1 and ekem1 are different sizes (unlike X25519)
```
e1 deseni, [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) bölüm 4'te belirtildiği gibi aşağıdaki şekilde tanımlanmıştır:

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
ekem1 deseni, [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) bölüm 4'te belirtildiği gibi aşağıdaki şekilde tanımlanmıştır:

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
### Noise Handshake KDF

#### Genel Bakış

Hibrit handshake [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) belgesinde tanımlanmıştır. Alice'ten Bob'a gönderilen ilk mesaj, mesaj yükünden önce e1 olan kapsülleme anahtarını içerir. Bu, ek bir statik anahtar olarak ele alınır; (Alice olarak) EncryptAndHash() veya (Bob olarak) DecryptAndHash() çağırın. Ardından mesaj yükünü her zamanki gibi işleyin.

İkinci mesaj, Bob'dan Alice'e, mesaj yükünden önce ekem1, şifreli metni içerir. Bu, ek bir statik anahtar olarak ele alınır; (Bob olarak) EncryptAndHash() veya (Alice olarak) DecryptAndHash() çağırın. Ardından, kem_shared_key'i hesaplayın ve MixKey(kem_shared_key)'i çağırın. Sonra mesaj yükünü her zamanki gibi işleyin.

#### Tanımlanmış ML-KEM İşlemleri

[FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)'te tanımlandığı gibi kullanılan kriptografik yapı taşlarına karşılık gelen aşağıdaki fonksiyonları tanımlıyoruz.

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

Hem encap_key hem de ciphertext'in Noise handshake mesajları 1 ve 2'deki ChaCha/Poly blokları içinde şifrelendiğini unutmayın. Bunlar handshake işleminin bir parçası olarak çözülecektir.

kem_shared_key, MixHash() ile zincirleme anahtara karıştırılır. Ayrıntılar için aşağıya bakın.

#### Mesaj 1 için Alice KDF

'es' mesaj kalıbından sonra ve payload'dan önce, şunu ekleyin:

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
#### Mesaj 1 için Bob KDF

'es' mesaj kalıbından sonra ve yükten önce şunları ekleyin:

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
#### Mesaj 2 için Bob KDF

XK için: 'ee' mesaj deseni sonrasında ve payload öncesinde şunları ekleyin:

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
#### Mesaj 2 için Alice KDF

'ee' mesaj kalıbından sonra, şunu ekleyin:

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
#### Mesaj 3 için KDF (yalnızca XK)

değişmedi

#### split() için KDF

değişmemiş

### El Sıkışma Detayları

#### Noise tanımlayıcıları

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

Değişiklikler: Mevcut NTCP2 yalnızca ChaCha bölümündeki seçenekleri içerir. ML-KEM ile birlikte, ChaCha bölümü aynı zamanda şifrelenmiş PQ public key'i de içerecektir.

PQ ve PQ olmayan NTCP2'nin aynı router adresi ve portu üzerinde desteklenebilmesi için, X değerinin (X25519 geçici genel anahtarı) en anlamlı bitini PQ bağlantısı olduğunu işaretlemek için kullanıyoruz. Bu bit PQ olmayan bağlantılar için her zaman sıfırdır.

Alice için, mesaj Noise tarafından şifrelendikten sonra ancak X'in AES karartmasından önce, X[31] |= 0x7f olarak ayarla.

Bob için, X'in AES gizleme kaldırma işleminden sonra, X[31] & 0x80'i test edin. Bit ayarlıysa, X[31] &= 0x7f ile temizleyin ve PQ bağlantısı olarak Noise ile şifreyi çözün. Bit temizse, her zamanki gibi PQ olmayan bağlantı olarak Noise ile şifreyi çözün.

Farklı bir router adresi ve portu üzerinde duyurulan PQ NTCP2 için bu gerekli değildir.

Ek bilgi için aşağıdaki Yayınlanmış Adresler bölümüne bakın.

Ham içerikler:

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
Şifrelenmemiş veri (Poly1305 kimlik doğrulama etiketi gösterilmemiş):

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
Not: PQ bağlantıları için bile mesaj 1 seçenekler bloğundaki sürüm alanı 2 olarak ayarlanmalıdır.

Boyutlar:

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Tür</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Tür Kodu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">X uzunluğu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 1 uzunluğu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 1 Şif uzunluğu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 1 Çöz uzunluğu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">PQ anahtar uzunluğu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">seçenek uzunluğu</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">4</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">64+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">--</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">880+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">848</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">816</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">800</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">6</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1264+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1232</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1200</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1184</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">7</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1648+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1616</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1584</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1568</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
</table>Not: Tip kodları yalnızca dahili kullanım içindir. Router'lar tip 4 olarak kalacak ve destek router adreslerinde belirtilecektir.

#### 2) SessionCreated

Ham içerik:

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
Şifrelenmemiş veri (Poly1305 auth tag gösterilmedi):

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
Boyutlar:

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Tip</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Tip Kodu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Y uzunluğu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 2 uzunluğu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 2 Şif uzunluğu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Msg 2 Çöz uzunluğu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">PQ CT uzunluğu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">opt uzunluğu</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">4</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">64+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">--</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">848+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">816</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">784</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">768</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">6</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1136+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1104</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1104</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1088</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">7</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">32</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1616+pad</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1584</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1584</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1568</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">16</td>
</tr>
</table>Not: Tür kodları yalnızca dahili kullanım içindir. Router'lar tip 4 olarak kalacak ve destek router adreslerinde belirtilecektir.

#### 3) SessionConfirmed

Değiştirilmemiş

#### Anahtar Türetme Fonksiyonu (KDF) (veri fazı için)

Değişmedi

#### Yayınlanmış Adresler

Her durumda, NTCP2 transport adını her zamanki gibi kullanın.

PQ olmayan, güvenlik duvarı olmayan ile aynı adres/portu kullanın. Yalnızca bir PQ varyantı desteklenir. Router adresinde, v=2 (her zamanki gibi) ve MLKEM 512/768/1024'ü belirtmek için yeni parametre pq=[3|4|5]'i yayınlayın. Alice, bunun hibrit bir bağlantı olduğunu belirtmek için oturum isteğinde ephemeral key'in MSB'sini (key[31] & 0x80) ayarlar. Yukarıya bakın. Eski router'lar pq parametresini yok sayacak ve her zamanki gibi PQ olmayan şekilde bağlanacaktır.

Farklı adres/port ile PQ olmayan veya sadece PQ, güvenlik duvarı olmayan desteklenmez. Bu, PQ olmayan NTCP2 devre dışı bırakılana kadar, şu andan birkaç yıl sonrasına kadar uygulanmayacaktır. PQ olmayan devre dışı bırakıldığında, birden fazla PQ varyantı desteklenebilir, ancak adres başına yalnızca bir tanesi. Desteklendiğinde, router adresinde MLKEM 512/768/1024'ü belirtmek için v=[3|4|5] yayınlayın. Alice, ephemeral anahtarının MSB'sini ayarlamaz. Eski router'lar v parametresini kontrol edecek ve bu adresi desteklenmeyen olarak atlayacaktır.

Güvenlik duvarı arkasındaki adresler (yayınlanan IP yok): Router adresinde, v=2 yayınlayın (her zamanki gibi). Bir pq parametresi yayınlamaya gerek yoktur.

Alice, kendi router bilgilerinde pq desteğinin reklamını yapıp yapmadığına veya aynı varyantın reklamını yapıp yapmadığına bakılmaksızın, Bob'un yayınladığı PQ varyantını kullanarak PQ Bob'a bağlanabilir.

#### Maksimum Dolgu

Mevcut spesifikasyonda, mesaj 1 ve 2'nin "makul" miktarda dolgu içerecek şekilde tanımlandığı, 0-31 bayt aralığının önerildiği ve maksimum değerin belirtilmediği ifade edilmektedir.

API 0.9.68 (sürüm 2.11.0) aracılığıyla, Java I2P non-PQ bağlantıları için maksimum 256 bayt padding uyguladı, ancak bu daha önce belgelenmemişti. API 0.9.69 (sürüm 2.12.0) itibariyle, Java I2P non-PQ bağlantıları için MLKEM-512 ile aynı maksimum padding'i uygular. Aşağıdaki tabloya bakın.

Tanımlanan mesaj boyutunu maksimum dolgu olarak kullanın, yani maksimum dolgu PQ bağlantıları için mesaj boyutunu ikiye katlayacaktır, aşağıdaki gibi:

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Mesaj Maks Dolgu</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">non-PQ (0.9.68'e kadar)</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">non-PQ (0.9.69 itibariyle)</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">MLKEM-512</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">MLKEM-768</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">MLKEM-1024</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">Session Request</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">256</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">880</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">880</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1264</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1648</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">Session Created</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">256</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">848</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">848</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1136</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1616</td>
</tr>
</table>## Ek Yük Analizi

### Anahtar Değişimi

Boyut artışı (bayt):

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Tip</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Pubkey (Mesaj 1)</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Şifrelenmiş Metin (Mesaj 2)</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+816</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+784</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+1200</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+1104</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024_X25519</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+1584</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">+1584</td>
</tr>
</table>## Güvenlik Analizi

NIST güvenlik kategorileri [NIST sunumunun](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) 10. slaydında özetlenmiştir. Ön kriterler: Hibrit protokoller için minimum NIST güvenlik kategorimiz 2, PQ-only (yalnızca kuantum sonrası) için 3 olmalıdır.

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Kategori</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Güvenlik Düzeyi</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">1</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">AES128</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">2</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">SHA256</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">3</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">AES192</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">4</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">SHA384</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">AES256</td>
</tr>
</table>### El Sıkışmaları

Bunların hepsi hibrit protokollerdir. Uygulamalar MLKEM768'i tercih etmelidir; MLKEM512 yeterince güvenli değildir.

NIST güvenlik kategorileri [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf):

<table style="border: 1px solid var(--color-border); border-collapse: collapse;">
<tr style="background-color: var(--color-bg-secondary);">
<th style="border: 1px solid var(--color-border); padding: 8px;">Algoritma</th>
<th style="border: 1px solid var(--color-border); padding: 8px;">Güvenlik Kategorisi</th>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM512</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">1</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM768</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">3</td>
</tr>
<tr>
<td style="border: 1px solid var(--color-border); padding: 8px;">MLKEM1024</td>
<td style="border: 1px solid var(--color-border); padding: 8px;">5</td>
</tr>
</table>## Uygulama Notları

### Kütüphane Desteği

Bouncycastle, BoringSSL ve WolfSSL kütüphaneleri artık MLKEM ve MLDSA'yı destekliyor. OpenSSL desteği 8 Nisan 2025'teki 3.5 sürümünde olacak [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

### Gelen Trafik Tanımlama

Session request'te ephemeral key'in MSB'sini (key[31] & 0x80) ayarlayarak bunun bir hibrit bağlantı olduğunu belirtiriz. Bu, aynı port üzerinde hem standart NTCP hem de hibrit NTCP çalıştırmamızı sağlar. Gelen bağlantılar için yalnızca bir hibrit varyant desteklenir ve router adresinde duyurulur. Örneğin, pq=3 veya pq=4.

#### Gizleme

Alice olarak, bir PQ bağlantısı için, gizleme öncesinde X[31] |= 0x80 ayarlayın. Bu, X'i geçersiz bir X25519 public key yapar. Gizleme sonrasında, AES-CBC onu rastgele hale getirecektir. X'in MSB'si gizleme sonrasında rastgele olacaktır.

Bob olarak, gizleme kaldırma işleminden sonra (X[31] & 0x80) != 0 olup olmadığını test edin. Eğer öyleyse, bu bir PQ bağlantısıdır.

NTCP2-PQ için gereken minimum router sürümü henüz belirlenmemiştir.

Not: Tip kodları yalnızca dahili kullanım içindir. Router'lar tip 4 olarak kalacak ve destek router adreslerinde belirtilecektir.

## Router Uyumluluğu

### Taşıma İsimleri

Her durumda, NTCP2 transport adını her zamanki gibi kullanın. Eski router'lar pq parametresini yok sayacak ve her zamanki gibi standart NTCP2 ile bağlanacaktır.

## Referanslar

* [CABFORUM](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/)
* [Hash Seçimi](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3)
* [CLOUDFLARE](https://blog.cloudflare.com/pq-2024/)
* [ORTAK](/docs/specs/common-structures/)
* [COMPOSITE-SIGS](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)
* [ECIES](/docs/specs/ecies/)
* [FORUM](http://zzz.i2p/topics/3294)
* [FIPS202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
* [FIPS203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
* [FIPS204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
* [FIPS205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf)
* [MLDSA-OIDS](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/)
* [NIST-PQ](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)
* [NIST-PQ-GÜNCELLEME](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf)
* [NIST-PQ-SON](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf)
* [NIST-VEKTÖRLER](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values)
* [Noise](https://noiseprotocol.org/noise.html)
* [Noise-Hibrit](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf)
* [NSA-PQ](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF)
* [NTCP2](/docs/specs/ntcp2/)
* [OPENSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/)
* [Prop165](/docs/proposals/165/)
* [PQ-WIREGUARD](https://eprint.iacr.org/2020/379.pdf)
* [RFC-2104](https://tools.ietf.org/html/rfc2104)
* [Rosenpass](https://rosenpass.eu/)
* [Rosenpass-Beyaz-Kağıt](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf)
* [SSH-HİBRİT](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/)
* [SSU2](/docs/specs/ssu2/)
* [TLS-HİBRİT](https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/)
