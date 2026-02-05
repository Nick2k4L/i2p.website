---
title: "Şifrelenmiş LeaseSet Spesifikasyonu"
description: "Şifrelenmiş leaseSet'lerin köreltilmesi, şifrelenmesi ve şifre çözümü"
slug: "encryptedleaseset"
category: "Protokoller"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Genel Bakış

Bu belge, şifrelenmiş leaseset'lerin köreltme, şifreleme ve şifre çözme işlemlerini belirtir. Şifrelenmiş leaseset'in yapısı için, [ortak yapılar spesifikasyonuna](/docs/specs/common-structures) bakınız. Şifrelenmiş leaseset'ler hakkında genel bilgi için, [öneri 123'e](/proposals/123-new-netdb-entries) bakınız. netDb'de kullanımı için, netDb belgelerine bakınız.

### Tanımlar

Şifrelenmiş LS2 için kullanılan kriptografik yapı taşlarına karşılık gelen aşağıdaki fonksiyonları tanımlıyoruz:

**CSRNG(n)** : Kriptografik olarak güvenli rastgele sayı üreticisinden n-bayt çıktısı.

CSRNG'nin kriptografik olarak güvenli olması gereksiniminin yanı sıra (ve dolayısıyla anahtar malzemesi oluşturmak için uygun olması), n-bayt çıktısının, hemen öncesindeki ve sonrasındaki bayt dizileri ağda açığa çıktığında (tuz veya şifreli dolgu gibi) anahtar malzemesi için kullanılmasının güvenli olması GEREKİR. Potansiyel olarak güvenilmez bir kaynağa dayanan implementasyonlar, ağda açığa çıkacak herhangi bir çıktıyı hash'lemelidir [PRNG-REFS](http://projectbullrun.org/dual-ec/ext-rand.html).

**H(p, d)** : Bir kişiselleştirme dizesi p ve veri d alan ve 32 bayt uzunluğunda çıktı üreten SHA-256 hash fonksiyonu.

SHA-256'yı şu şekilde kullanın:

```
H(p, d) := SHA-256(p || d)
```
**STREAM** : [RFC-7539-S2.4](https://tools.ietf.org/html/rfc7539#section-2.4)'te belirtildiği gibi ChaCha20 stream cipher (akış şifresi), başlangıç sayacı 1 olarak ayarlanmış. S_KEY_LEN = 32 ve S_IV_LEN = 12.

- **ENCRYPT(k, iv, plaintext)** : Düz metni şifre anahtarı k ve k anahtarı için benzersiz OLMASI GEREKEN nonce iv kullanarak şifreler. Düz metin ile aynı boyutta bir şifreli metin döndürür. Anahtar gizli ise tüm şifreli metin rastgeleden ayırt edilemez olmalıdır.

- **DECRYPT(k, iv, ciphertext)** : Şifre anahtarı k ve nonce iv kullanarak ciphertext'i çözer. Düz metni döndürür.

**SIG** : Anahtar köreltme ile Red25519 imza şeması (SigType 11'e karşılık gelir). Aşağıdaki fonksiyonlara sahiptir:

- **DERIVE_PUBLIC(privkey)** : Verilen özel anahtara karşılık gelen açık anahtarı döndürür.

- **SIGN(privkey, m)** : Verilen mesaj m üzerinde özel anahtar privkey ile bir imza döndürür.

- **VERIFY(pubkey, m, sig)** : İmza sig'i genel anahtar pubkey ve mesaj m'ye karşı doğrular. İmza geçerliyse true, aksi takdirde false döndürür.

Ayrıca aşağıdaki anahtar köreltme işlemlerini de desteklemelidir:

- **GENERATE_ALPHA(data, secret)** : Veriyi ve isteğe bağlı bir gizli anahtarı bilenler için alpha üret. Sonuç, özel anahtarlarla aynı şekilde dağıtılmalıdır.

- **BLIND_PRIVKEY(privkey, alpha)** : Gizli bir alfa kullanarak özel anahtarı köreltir.

- **BLIND_PUBKEY(pubkey, alpha)** : Bir gizli alpha kullanarak bir açık anahtarı körletir. Verilen bir anahtar çifti (privkey, pubkey) için aşağıdaki ilişki geçerlidir:

```
BLIND_PUBKEY(pubkey, alpha) ==
DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))
```
**DH** : X25519 genel anahtar anlaşma sistemi. 32 baytlık özel anahtarlar, 32 baytlık genel anahtarlar, 32 baytlık çıktılar üretir. Aşağıdaki işlevlere sahiptir:

- **GENERATE_PRIVATE()** : Yeni bir özel anahtar oluşturur.

- **DERIVE_PUBLIC(privkey)** : Verilen özel anahtara karşılık gelen genel anahtarı döndürür.

- **DH(privkey, pubkey)** : Verilen özel ve genel anahtarlardan paylaşılan bir gizli anahtar üretir.

**HKDF(salt, ikm, info, n)** : Bazı girdi anahtar malzemesi ikm'yi (iyi entropiye sahip olması gereken ancak düzgün rastgele bir dize olması gerekmeyen), 32 bayt uzunluğunda bir salt değerini ve bağlama özgü bir 'info' değerini alarak anahtar malzemesi olarak kullanıma uygun n bayt çıktı üreten kriptografik anahtar türetme fonksiyonu.

[RFC-5869](https://tools.ietf.org/html/rfc5869)'da belirtildiği gibi HKDF kullanın, [RFC-2104](https://tools.ietf.org/html/rfc2104)'te belirtildiği gibi HMAC hash fonksiyonu SHA-256 kullanarak. Bu, SALT_LEN'in maksimum 32 bayt olduğu anlamına gelir.

### Format

Şifrelenmiş LS2 formatı üç iç içe geçmiş katmandan oluşur:

- Depolama ve erişim için gerekli düz metin bilgilerini içeren dış katman.
- İstemci kimlik doğrulamasını yöneten orta katman.
- Gerçek LS2 verilerini içeren iç katman.

Genel format şöyle görünür:

```
Layer 0 data + Enc(layer 1 data + Enc(layer 2 data)) + Signature
```
Şifreli LS2'nin blinded (körleştirilmiş) olduğunu unutmayın. Destination header'da bulunmaz. DHT depolama konumu SHA-256(sig type || blinded public key) şeklindedir ve günlük olarak döndürülür.

Yukarıda belirtilen standart LS2 header'ını KULLANMAZ.

#### Katman 0 (dış)

**Tür** : 1 bayt

Aslında başlıkta değil, ancak imza tarafından kapsanan verinin bir parçası. Database Store Message içindeki alandan al.

**Blinded Public Key Sig Type** : 2 bayt, big endian

Bu her zaman tip 11 olacaktır ve Red25519 blinded anahtarını tanımlar.

**Blinded Public Key** : Sig type tarafından belirtilen uzunluk

**Yayınlanma zaman damgası** : 4 bayt, big endian

Epoch'tan bu yana geçen saniye, 2106'da sıfırlanır

**Expires** : 2 bayt, big endian

Yayınlanan zaman damgasından saniye cinsinden ofset, maksimum 18.2 saat

**Bayraklar** : 2 bayt

Bit sırası: 15 14 ... 3 2 1 0

- Bit 0: 0 ise çevrimdışı anahtar yok; 1 ise çevrimdışı anahtarlar var
- Diğer bitler: gelecekteki kullanımlarla uyumluluk için 0'a ayarlanır

**Geçici anahtar verisi** : Bayrak çevrimdışı anahtarları belirtiyorsa mevcut

- **Expires timestamp** : 4 byte, big endian. Epoch'tan bu yana geçen saniye, 2106'da sıfırlanır
- **Transient sig type** : 2 byte, big endian
- **Transient signing public key** : Sig type tarafından belirtilen uzunluk
- **Signature** : Blinded public key sig type tarafından belirtilen uzunluk. Expires timestamp, transient sig type ve transient public key üzerinde. Blinded public key ile doğrulanır.

**lenOuterCiphertext** : 2 bayt, big endian

**outerCiphertext** : lenOuterCiphertext bayt

Şifrelenmiş katman 1 verisi. Anahtar türetme ve şifreleme algoritmaları için aşağıya bakın.

**İmza** : İmzalama anahtarının imza türü tarafından belirtilen uzunluk

İmza yukarıdaki her şeyin imzasıdır. Bayrak çevrimdışı anahtarları gösteriyorsa, imza geçici ortak anahtar ile doğrulanır. Aksi takdirde, imza köreltilmiş ortak anahtar ile doğrulanır.

#### Katman 1 (orta)

**Bayraklar** : 1 bayt

Bit sırası: 76543210

- Bit 0: herkes için 0, istemci başına için 1, auth bölümü takip eder
- Bit 3-1: Kimlik doğrulama şeması, yalnızca bit 0 istemci başına için 1'e ayarlıysa, aksi halde 000
  - 000: DH istemci kimlik doğrulaması (veya istemci başına kimlik doğrulama yok)
  - 001: PSK istemci kimlik doğrulaması
- Bit 7-4: Kullanılmayan, gelecekteki uyumluluk için 0'a ayarla

**DH istemci kimlik doğrulama verisi** : Bayrak bit 0'ı 1'e ayarlanmışsa ve bayrak bitleri 3-1 000'a ayarlanmışsa mevcut.

- **ephemeralPublicKey** : 32 bayt
- **clients** : 2 bayt, big endian. Takip eden authClient girişlerinin sayısı, her biri 40 bayt
- **authClient** : Tek bir istemci için yetkilendirme verisi. İstemci başına yetkilendirme algoritması için aşağıya bakın.
  - **clientID_i** : 8 bayt
  - **clientCookie_i** : 32 bayt

**PSK istemci kimlik doğrulama verisi** : Bayrak bit 0'ı 1'e ve bayrak bit 3-1'i 001'e ayarlanmışsa mevcuttur.

- **authSalt** : 32 bayt
- **clients** : 2 bayt, big endian. Takip edecek authClient girişlerinin sayısı, her biri 40 bayt
- **authClient** : Tek bir istemci için yetkilendirme verisi. İstemci başına yetkilendirme algoritması için aşağıya bakın.
  - **clientID_i** : 8 bayt
  - **clientCookie_i** : 32 bayt

**innerCiphertext** : Uzunluk lenOuterCiphertext tarafından belirtilir (kalan tüm veri)

Şifrelenmiş katman 2 verisi. Anahtar türetme ve şifreleme algoritmaları için aşağıya bakınız.

#### Katman 2 (iç)

**Tip** : 1 bayt

Ya 3 (LS2) ya da 7 (Meta LS2)

**Veri** : Verilen tür için LeaseSet2 verisi.

Başlık ve imzayı içerir.

### Blinding Key Türetme

Anahtar köreltme için Ed25519 ve ZCash RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) tabanlı aşağıdaki şemayı kullanıyoruz. Red25519 imzaları Ed25519 eğrisi üzerinde, hash için SHA-512 kullanarak yapılır.

Benzer tasarım hedefleri olan Tor'un rend-spec-v3.txt ek A.2 [TOR-REND-SPEC-V3](https://spec.torproject.org/rend-spec-v3) standardını kullanmıyoruz, çünkü onun köreltilmiş açık anahtarları asal-düzen alt grubunun dışında olabilir ve bu bilinmeyen güvenlik etkilerine sahiptir.

#### Hedefler

- Gizlenmemiş hedefdeki imzalama genel anahtarı Ed25519 (imza türü 7) veya Red25519 (imza türü 11) olmalıdır; başka imza türleri desteklenmez
- İmzalama genel anahtarı çevrimdışıysa, geçici imzalama genel anahtarı da Ed25519 olmalıdır
- Gizleme hesaplama açısından basittir
- Mevcut kriptografik ilkelleri kullanır
- Gizlenmiş genel anahtarlar gizlemesi kaldırılamaz
- Gizlenmiş genel anahtarlar Ed25519 eğrisi ve asal-sıralı alt grup üzerinde olmalıdır
- Gizlenmiş genel anahtarı türetmek için hedefin imzalama genel anahtarını bilmek gerekir (tam hedef gerekli değil)
- Gizlenmiş genel anahtarı türetmek için gereken ek bir gizli anahtar isteğe bağlı olarak sağlanabilir

#### Güvenlik

Bir kör etme şemasının güvenliği, alpha'nın dağılımının kör edilmemiş özel anahtarlarla aynı olmasını gerektirir. Ancak, bir Ed25519 özel anahtarını (imza türü 7) Red25519 özel anahtarına (imza türü 11) kör ettiğimizde, dağılım farklıdır. zcash bölüm 4.1.6.1 [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) gereksinimlerini karşılamak için, Red25519 (imza türü 11) kör edilmemiş anahtarlar için de kullanılmalıdır, böylece "yeniden rastgeleleştirilmiş bir genel anahtar ve o anahtar altındaki imza(lar) kombinasyonu, hangi anahtardan yeniden rastgeleleştirildiğini ortaya çıkarmaz." Mevcut hedefler için tür 7'ye izin veriyoruz, ancak şifrelenecek yeni hedefler için tür 11'i öneriyoruz.

#### Tanımlar

**B** : Ed25519 temel noktası (üreteci) 2^255 - 19, [ED25519-REFS](http://cr.yp.to/papers.html#ed25519) belgesinde belirtildiği gibi

**L** : [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)'te belirtildiği gibi Ed25519 sırası 2^252 + 27742317777372353535851937790883648493

**DERIVE_PUBLIC(a)** : Özel anahtarı Ed25519'da olduğu gibi herkese açık anahtara dönüştür (G ile çarp)

**alpha** : Hedefi bilenler tarafından bilinen 32-byte'lık rastgele bir sayı.

**GENERATE_ALPHA(destination, date, secret)** : Hedef ve gizli anahtarı bilen kişiler için mevcut tarih için alpha oluştur. Sonuç, Ed25519 özel anahtarları ile aynı şekilde dağıtılmalıdır.

**a** : Hedefi imzalamak için kullanılan kör edilmemiş 32-byte EdDSA veya RedDSA imzalama özel anahtarı

**A** : Hedefteki gizlenmemiş 32-byte EdDSA veya RedDSA imzalama genel anahtarı, = DERIVE_PUBLIC(a), Ed25519'da olduğu gibi

**a'** : Şifrelenmiş leaseset'i imzalamak için kullanılan körleştirilmiş 32-bayt EdDSA imzalama özel anahtarı. Bu geçerli bir EdDSA özel anahtarıdır.

**A'** : Destination içindeki körleştirilmiş 32-byte EdDSA imzalama genel anahtarı, DERIVE_PUBLIC(a') ile veya A ve alpha'dan üretilebilir. Bu, eğri üzerinde ve asal-mertebe alt grupta geçerli bir EdDSA genel anahtarıdır.

**LEOS2IP(x)** : Giriş baytlarının sırasını little-endian'a çevir

**H\*(x)** : 32 bayt = (LEOS2IP(SHA512(x))) mod B, Ed25519 hash-and-reduce ile aynı

#### Blinding Hesaplamaları

Her gün (UTC) yeni bir gizli alfa ve köreltilmiş anahtarlar oluşturulmalıdır.

Gizli alpha ve köreltilmiş anahtarlar şu şekilde hesaplanır:

GENERATE_ALPHA(hedef, tarih, gizli), tüm taraflar için:

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
BLIND_PRIVKEY(), leaseset yayınlayan sahip için:

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
BLIND_PUBKEY(), leaseSet'i alan istemciler için:

```
alpha = GENERATE_ALPHA(destination, date, secret)
A = destination's signing public key
// Addition using group elements (points on the curve)
blinded public key = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```
A' hesaplama yöntemlerinin her ikisi de gerektiği gibi aynı sonucu verir.

#### İmzalama

Kör edilmemiş leaseset, kör edilmemiş Ed25519 veya Red25519 imzalama özel anahtarı ile imzalanır ve her zamanki gibi kör edilmemiş Ed25519 veya Red25519 imzalama genel anahtarı (sig türleri 7 veya 11) ile doğrulanır.

Eğer imzalama public key çevrimdışıysa, unblinded leaseset, unblinded geçici Ed25519 veya Red25519 imzalama private key tarafından imzalanır ve her zamanki gibi unblinded Ed25519 veya Red25519 geçici imzalama public key (sig türleri 7 veya 11) ile doğrulanır. Şifrelenmiş leaseset'ler için çevrimdışı key'ler hakkında ek notlar için aşağıya bakınız.

Şifrelenmiş leaseSet'in imzalanması için, kör anahtarlarla imzalama ve doğrulama yapmak üzere RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) tabanlı Red25519 kullanırız. Red25519 imzaları Ed25519 eğrisi üzerinde, hash için SHA-512 kullanarak gerçekleştirilir.

Red25519, aşağıda belirtilen durumlar dışında standart Ed25519'a benzerdir.

#### İmzala/Doğrula Hesaplamaları

Şifrelenmiş leaseset'in dış kısmı Red25519 anahtarları ve imzaları kullanır.

Red25519, Ed25519'a benzerdir. İki fark vardır:

Red25519 özel anahtarları rastgele sayılardan oluşturulur ve ardından yukarıda tanımlanan L modülüne göre indirgenmesi gerekir. Ed25519 özel anahtarları rastgele sayılardan oluşturulur ve ardından 0 ve 31 baytlarına bit düzeyinde maskeleme kullanılarak "kısıtlanır". Bu Red25519 için yapılmaz. Yukarıda tanımlanan GENERATE_ALPHA() ve BLIND_PRIVKEY() fonksiyonları mod L kullanarak uygun Red25519 özel anahtarları oluşturur.

Red25519'da, imzalama için r hesaplaması ek rastgele veri kullanır ve özel anahtarın hash'i yerine genel anahtar değerini kullanır. Rastgele veri nedeniyle, aynı veriyi aynı anahtarla imzalarken bile her Red25519 imzası farklıdır.

```
Signing:
  T = 80 random bytes
  r = H*(T || publickey || message)
  (rest is the same as in Ed25519)

Verification:
  Same as for Ed25519
```
### Şifreleme ve işleme

#### Alt kimlik bilgilerinin türetilmesi

Blinding sürecinin bir parçası olarak, şifrelenmiş bir LS2'nin yalnızca karşılık gelen Destination'ın imzalama genel anahtarını bilen biri tarafından şifresinin çözülebileceğinden emin olmamız gerekir. Tam Destination gerekli değildir. Bunu başarmak için, imzalama genel anahtarından bir kimlik bilgisi türetiriz:

```
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
credential = H("credential", keydata)
```
Kişiselleştirme dizesi, kimlik bilgisinin düz Destination hash'i gibi DHT arama anahtarı olarak kullanılan herhangi bir hash ile çakışmamasını sağlar.

Belirli bir blinded key için, ardından bir subcredential türetebiliriz:

```
subcredential = H("subcredential", credential || blindedPublicKey)
```
Subcredential, aşağıdaki anahtar türetme işlemlerinde dahil edilir ve bu anahtarları Destination'ın imzalama genel anahtarının bilgisine bağlar.

#### Katman 1 şifreleme

İlk olarak, anahtar türetme işleminin girdi verisi hazırlanır:

```
outerInput = subcredential || publishedTimestamp
```
Sonra, rastgele bir salt oluşturulur:

```
outerSalt = CSRNG(32)
```
Daha sonra katman 1'i şifrelemek için kullanılan anahtar türetilir:

```
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Son olarak, katman 1 düz metni şifrelenir ve serileştirilir:

```
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```
#### Katman 1 şifre çözme

Salt, katman 1 şifrelenmiş metinden ayrıştırılır:

```
outerSalt = outerCiphertext[0:31]
```
Sonra katman 1'i şifrelemek için kullanılan anahtar türetilir:

```
outerInput = subcredential || publishedTimestamp
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Son olarak, katman 1 şifreli metni çözülür:

```
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```
#### Katman 2 şifreleme

İstemci yetkilendirmesi etkinleştirildiğinde, `authCookie` aşağıda açıklandığı gibi hesaplanır. İstemci yetkilendirmesi devre dışı bırakıldığında, `authCookie` sıfır uzunluklu bayt dizisidir.

Şifreleme 1. katmana benzer şekilde ilerler:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = CSRNG(32)
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```
#### Katman 2 şifre çözme

İstemci yetkilendirmesi etkinleştirildiğinde, `authCookie` aşağıda açıklandığı gibi hesaplanır. İstemci yetkilendirmesi devre dışı bırakıldığında, `authCookie` sıfır uzunluklu bayt dizisidir.

Şifre çözme işlemi katman 1'e benzer şekilde ilerler:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = innerCiphertext[0:31]
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```
### İstemci bazında yetkilendirme

Bir Destination için istemci yetkilendirmesi etkinleştirildiğinde, sunucu şifrelenmiş LS2 verilerinin şifresini çözmek için yetkilendirdiği istemcilerin bir listesini tutar. İstemci başına depolanan veriler yetkilendirme mekanizmasına bağlıdır ve her istemcinin oluşturup güvenli bir bant dışı mekanizma aracılığıyla sunucuya gönderdiği bir tür anahtar materyalini içerir.

İstemci başına yetkilendirme uygulaması için iki alternatif bulunmaktadır:

#### DH istemci yetkilendirmesi

Her istemci bir DH anahtar çifti `[csk_i, cpk_i]` oluşturur ve genel anahtar `cpk_i`'yi sunucuya gönderir.

##### Sunucu işleme

Sunucu yeni bir `authCookie` ve geçici bir DH anahtar çifti oluşturur:

```
authCookie = CSRNG(32)
esk = GENERATE_PRIVATE()
epk = DERIVE_PUBLIC(esk)
```
Daha sonra her yetkili istemci için, sunucu `authCookie`'yi o istemcinin public key'ine şifreler:

```
sharedSecret = DH(esk, cpk_i)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
Sunucu, her `[clientID_i, clientCookie_i]` çiftini `epk` ile birlikte şifrelenmiş LS2'nin 1. katmanına yerleştirir.

##### İstemci işleme

İstemci, beklenen istemci tanımlayıcısı `clientID_i`, şifreleme anahtarı `clientKey_i` ve şifreleme IV `clientIV_i` değerlerini türetmek için özel anahtarını kullanır:

```
sharedSecret = DH(csk_i, epk)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Ardından istemci, `clientID_i` içeren bir girdi için katman 1 yetkilendirme verilerini arar. Eşleşen bir girdi varsa, istemci `authCookie`'yi elde etmek için onu şifresini çözer:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Önceden paylaşılan anahtar istemci yetkilendirmesi

Her client (istemci) gizli 32-byte'lık bir `psk_i` anahtarı oluşturur ve bunu sunucuya gönderir. Alternatif olarak, sunucu gizli anahtarı oluşturabilir ve bunu bir veya daha fazla client'a gönderebilir.

##### Sunucu işleme

Sunucu yeni bir `authCookie` ve salt oluşturur:

```
authCookie = CSRNG(32)
authSalt = CSRNG(32)
```
Daha sonra her yetkili istemci için, sunucu `authCookie`'yi önceden paylaşılan anahtarına şifreler:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
Sunucu, her `[clientID_i, clientCookie_i]` tuple'ını `authSalt` ile birlikte şifrelenmiş LS2'nin 1. katmanına yerleştirir.

##### İstemci işleme

İstemci, beklenen istemci tanımlayıcısı `clientID_i`, şifreleme anahtarı `clientKey_i` ve şifreleme IV'si `clientIV_i`'yi türetmek için önceden paylaşılmış anahtarını kullanır:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Ardından istemci, `clientID_i` içeren bir giriş için katman 1 yetkilendirme verilerinde arama yapar. Eşleşen bir giriş varsa, istemci `authCookie` elde etmek için şifresini çözer:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Güvenlik hususları

Yukarıdaki her iki istemci yetkilendirme mekanizması da istemci üyeliği için gizlilik sağlar. Sadece Destination'ı bilen bir varlık, herhangi bir zamanda kaç istemcinin abone olduğunu görebilir, ancak hangi istemcilerin eklendiğini veya iptal edildiğini takip edemez.

Sunucular, şifrelenmiş bir LS2 oluşturdukları her seferde istemci sıralamasını rastgele hale getirmeli (SHOULD), böylece istemcilerin listedeki pozisyonlarını öğrenmelerini ve diğer istemcilerin ne zaman eklendiğini veya iptal edildiğini çıkarımlamalarını önlemelidir.

Bir sunucu, yetkilendirme verisi listesine rastgele girişler ekleyerek abone olan istemci sayısını gizlemeyi SEÇEBİLİR.

##### DH istemci yetkilendirmesinin avantajları

- Şemanın güvenliği yalnızca istemci anahtar materyalinin bant dışı değişimine bağlı değildir. İstemcinin özel anahtarının cihazından ayrılmasına hiçbir zaman gerek yoktur ve bu nedenle bant dışı değişimi yakalayabilen ancak DH algoritmasını kıramayan bir saldırgan, şifrelenmiş LS2'yi çözemez veya istemciye ne kadar süre erişim verildiğini belirleyemez.

##### DH istemci yetkilendirmesinin dezavantajları

- N istemci için sunucu tarafında N + 1 DH işlemi gerektirir.
- İstemci tarafında bir DH işlemi gerektirir.
- İstemcinin gizli anahtarı oluşturmasını gerektirir.

##### PSK istemci yetkilendirmesinin avantajları

- DH işlemleri gerektirmez.
- Sunucunun gizli anahtarı oluşturmasına izin verir.
- İstenirse sunucunun aynı anahtarı birden fazla istemciyle paylaşmasına izin verir.

##### PSK istemci yetkilendirmesinin dezavantajları

- Şemanın güvenliği, istemci anahtar materyalinin bant dışı değişimine kritik şekilde bağlıdır. Belirli bir istemci için değişimi engelleyen bir saldırgan, o istemcinin yetkilendirildiği sonraki şifrelenmiş LS2'leri çözebilir ve ayrıca istemcinin erişiminin ne zaman iptal edildiğini belirleyebilir.

### Base 32 Adresleri ile Şifrelenmiş LS

Şifrelenmiş bir LS2 için geleneksel bir base 32 adres kullanamazsınız, çünkü bu yalnızca hedefin hash'ini içerir. Köreltilmemiş (non-blinded) public key'i sağlamaz. Bu nedenle, tek başına bir base 32 adres yetersizdir. İstemci ya tam hedefi (public key içeren) ya da public key'in kendisini ihtiyaç duyar. İstemci adres defterinde tam hedefe sahipse ve adres defteri hash ile ters arama destekliyorsa, public key alınabilir.

Bu yüzden hash yerine public key'i base32 adresine koyan yeni bir formata ihtiyacımız var. Bu format aynı zamanda public key'in imza türünü ve blinding şemasının imza türünü de içermelidir. Toplam gereksinimler 32 + 3 = 35 bayttır, bu da base 32'de 56 karakter veya daha uzun public key türleri için daha fazla karakter gerektirir.

```
data = ((1 byte flags || 1 byte unblinded sigtype || 1 byte blinded sigtype) XOR checksum) || 32 byte pubkey
address = Base32Encode(data) || ".b32.i2p"
```
Geleneksel base 32 adreslerde olduğu gibi aynı ".b32.i2p" son ekini kullanırız. Şifrelenmiş leaseSet'ler için adresler 56 kodlanmış karakter (35 çözümlenmiş bayt) ile tanımlanır, geleneksel base 32 adresler için 52 karakter (32 bayt) ile karşılaştırıldığında. b32'nin sonundaki beş kullanılmayan bit 0 olmalıdır.

BitTorrent için şifreli bir LS2 kullanamazsınız, çünkü kompakt duyuru yanıtları 32 bayttır. Bu 32 bayt yalnızca hash'i içerir. LeaseSet'in şifreli olduğuna dair bir gösterge veya imza türleri için yer yoktur.

Yeni format hakkında daha fazla bilgi için [adlandırma spesifikasyonuna](/docs/specs/naming) veya [149 numaralı öneri](/proposals/149-b32-encrypted-ls2) belgesine bakın.

### Çevrimdışı Anahtarlar ile Şifrelenmiş LS

Çevrimdışı anahtarları olan şifrelenmiş leaseSets için, köreltilmiş özel anahtarlar da çevrimdışı olarak üretilmeli, her gün için bir tane.

İsteğe bağlı çevrimdışı imza bloğu, şifrelenmiş leaseset'in düz metin kısmında bulunduğundan, floodfill'leri tarayan herhangi biri bunu kullanarak leaseset'i (şifresini çözemese de) birkaç gün boyunca izleyebilir. Bunu önlemek için, anahtarların sahibi her gün için yeni geçici anahtarlar da üretmelidir. Hem geçici hem de körleştirilmiş anahtarlar önceden üretilebilir ve router'a toplu olarak teslim edilebilir.

Birden fazla geçici ve gizlenmiş anahtarı paketlemek ve bunları istemciye veya router'a sağlamak için tanımlanmış bir dosya formatı yoktur. Çevrimdışı anahtarlarla şifrelenmiş leaseSet'leri desteklemek için tanımlanmış bir I2CP protokol geliştirmesi yoktur.

### Notlar

- Şifreli leaseSet'ler kullanan bir hizmet, şifrelenmiş sürümü floodfill'lere yayınlayacaktır. Ancak verimlilik için, kimlik doğrulandıktan sonra (örneğin whitelist aracılığıyla) istemcilere garlic mesajı içinde şifrelenmemiş leaseSet'leri gönderecektir.
- Floodfill'ler kötüye kullanımı önlemek için maksimum boyutu makul bir değerle sınırlayabilir.
- Şifre çözme işleminden sonra, iç zaman damgası ve süre dolumunun üst seveldekilerle eşleştiği de dahil olmak üzere çeşitli kontroller yapılmalıdır.
- ChaCha20, AES yerine tercih edilmiştir. AES donanım desteği mevcut olduğunda hızlar benzer olsa da, düşük seviye ARM cihazlarında olduğu gibi AES donanım desteği olmadığında ChaCha20 2,5-3 kat daha hızlıdır.

## Kaynaklar

- **[ED25519-REFS]** Daniel J. Bernstein, Niels Duif, Tanja Lange, Peter Schwabe ve Bo-Yin Yang tarafından "High-speed high-security signatures". [http://cr.yp.to/papers.html#ed25519](http://cr.yp.to/papers.html#ed25519)
- **[KEYBLIND-PROOF]** [https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html](https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html)
- **[KEYBLIND-REFS]** [https://trac.torproject.org/projects/tor/ticket/8106](https://trac.torproject.org/projects/tor/ticket/8106) ve [https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html](https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html)
- **[PRNG-REFS]** [http://projectbullrun.org/dual-ec/ext-rand.html](http://projectbullrun.org/dual-ec/ext-rand.html) ve [https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html)
- **[RFC-2104]** [https://tools.ietf.org/html/rfc2104](https://tools.ietf.org/html/rfc2104)
- **[RFC-4880-S5.1]** [https://tools.ietf.org/html/rfc4880#section-5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
- **[RFC-5869]** [https://tools.ietf.org/html/rfc5869](https://tools.ietf.org/html/rfc5869)
- **[RFC-7539-S2.4]** [https://tools.ietf.org/html/rfc7539#section-2.4](https://tools.ietf.org/html/rfc7539#section-2.4)
- **[TOR-REND-SPEC-V3]** [https://spec.torproject.org/rend-spec-v3](https://spec.torproject.org/rend-spec-v3)
- **[ZCASH]** [https://github.com/zcash/zips/tree/master/protocol/protocol.pdf](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)
