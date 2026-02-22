---
title: "NTCP2 Transport"
description: "Router'dan router'a bağlantılar için Noise tabanlı TCP aktarım protokolü"
slug: "ntcp2"
category: "Taşıyıcılar"
lastUpdated: "2026-01"
accurateFor: "0.9.66"
---

## Genel Bakış

NTCP2, [NTCP](/docs/transport/ntcp)'nin çeşitli otomatik tanımlama ve saldırı türlerine karşı direncini artıran kimlik doğrulamalı anahtar anlaşması protokolüdür.

NTCP2, esneklik ve NTCP ile birlikte var olma için tasarlanmıştır. NTCP ile aynı port üzerinde veya farklı bir port üzerinde desteklenebilir ya da eşzamanlı NTCP desteği olmaksızın da çalışabilir. Ayrıntılar için aşağıdaki Yayınlanan Router Bilgisi bölümüne bakın.

Diğer I2P taşıma katmanlarında olduğu gibi, NTCP2 yalnızca I2NP mesajlarının noktadan noktaya (router'dan router'a) taşınması için tanımlanmıştır. Genel amaçlı bir veri borusu değildir.

NTCP2, 0.9.36 sürümünden itibaren desteklenmektedir. Orijinal teklif, arka plan tartışması ve ek bilgiler için [Prop111](/proposals/111-ntcp-2) sayfasına bakın.

## Noise Protocol Framework

NTCP2, Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (Revizyon 33, 2017-10-04) kullanır. Noise, [SSU](/docs/transport/ssu) protokolünün temelini oluşturan Station-To-Station protokolü [STS](#references) ile benzer özelliklere sahiptir. Noise terminolojisinde Alice başlatıcı (initiator), Bob ise yanıtlayıcıdır (responder).

NTCP2, Noise_XK_25519_ChaChaPoly_SHA256 Noise protokolüne dayanmaktadır. (İlk anahtar türetme fonksiyonu için gerçek tanımlayıcı, I2P uzantılarını belirtmek üzere "Noise_XKaesobfse+hs2+hs3_25519_ChaChaPoly_SHA256"'dır - aşağıdaki KDF 1 bölümüne bakın) Bu Noise protokolü aşağıdaki temel öğeleri kullanır:

- Handshake Pattern: XK Alice anahtarını Bob'a iletir (X) Alice Bob'un statik anahtarını zaten biliyor (K)
- DH Function: X25519 [RFC-7748](https://tools.ietf.org/html/rfc7748)'de belirtildiği gibi 32 byte anahtar uzunluğuna sahip X25519 DH.
- Cipher Function: ChaChaPoly [RFC-7539](https://tools.ietf.org/html/rfc7539) bölüm 2.8'de belirtildiği gibi AEAD_CHACHA20_POLY1305. İlk 4 byte sıfıra ayarlanmış 12 byte nonce.
- Hash Function: SHA256 I2P'de yaygın olarak kullanılan standart 32-byte hash.

## Framework'e Eklemeler

NTCP2, Noise_XK_25519_ChaChaPoly_SHA256'ya aşağıdaki geliştirmeleri tanımlar. Bunlar genellikle [NOISE](https://noiseprotocol.org/noise.html) bölüm 13'teki yönergeleri takip eder.

1) Açık metin geçici anahtarlar, bilinen bir anahtar ve IV kullanarak AES şifreleme ile gizlenir. 2) Mesaj 1 ve 2'ye rastgele açık metin dolgusu eklenir. Açık metin dolgusu handshake hash (MixHash) hesaplamasına dahil edilir. Mesaj 2 ve mesaj 3 bölüm 1 için aşağıdaki KDF bölümlerine bakın. Mesaj 3 ve veri aşaması mesajlarına rastgele AEAD dolgusu eklenir. 3) TCP üzerinde Noise için gerekli olduğu gibi ve obfs4'te olduğu gibi iki baytlık çerçeve uzunluğu alanı eklenir. Bu yalnızca veri aşaması mesajlarında kullanılır. Mesaj 1 ve 2 AEAD çerçeveleri sabit uzunluktadır. Mesaj 3 bölüm 1 AEAD çerçevesi sabit uzunluktadır. Mesaj 3 bölüm 2 AEAD çerçeve uzunluğu mesaj 1'de belirtilir. 4) İki baytlık çerçeve uzunluğu alanı, obfs4'te olduğu gibi SipHash-2-4 ile gizlenir. 5) Mesaj 1,2,3 ve veri aşaması için yük formatı tanımlanır. Tabii ki, bunlar çerçevede tanımlanmamıştır.

## Mesajlar

Tüm NTCP2 mesajları 65537 bayt veya daha kısa uzunluktadır. Mesaj formatı, çerçeveleme ve ayırt edilemezlik için değişiklikler yapılmış Noise mesajlarına dayanır. Standart Noise kütüphanelerini kullanan uygulamalar, alınan mesajları Noise mesaj formatına/formatından ön işleme tabi tutması gerekebilir. Tüm şifrelenmiş alanlar AEAD şifreli metinlerdir.

Kurulum sırası aşağıdaki gibidir:

```
Alice                           Bob

SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Noise terminolojisini kullanarak, kuruluş ve veri sırası şu şekildedir: (Payload Güvenlik Özellikleri [Noise](https://noiseprotocol.org/noise.html) kaynağından)

```
XK(s, rs):           Authentication   Confidentiality
  <- s
  ...
  -> e, es                  0                2
  <- e, ee                  2                1
  -> s, se                  2                5
  <-                        2                5
```
Bir oturum kurulduktan sonra, Alice ve Bob Veri mesajlarını değiş tokuş edebilirler.

Tüm mesaj türleri (SessionRequest, SessionCreated, SessionConfirmed, Data ve TimeSync) bu bölümde belirtilmiştir.

Bazı notasyonlar:

    - RH_A = Router Hash for Alice (32 bytes)
    - RH_B = Router Hash for Bob (32 bytes)

### Kimliği Doğrulanmış Şifreleme

Üç ayrı kimlik doğrulamalı şifreleme örneği (CipherState) bulunmaktadır. Biri handshake aşaması sırasında, ikisi (gönderme ve alma) veri aşaması için kullanılır. Her birinin KDF'den gelen kendi anahtarı vardır.

Şifrelenmiş/doğrulanmış veriler şu şekilde temsil edilecektir

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   Encrypted and authenticated data    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
```
#### ChaCha20/Poly1305

Şifrelenmiş ve doğrulanmış veri formatı.

Şifreleme/şifre çözme fonksiyonlarına girişler:

```
k :: 32 byte cipher key, as generated from KDF

nonce :: Counter-based nonce, 12 bytes.
         Starts at 0 and incremented for each message.
         First four bytes are always zero.
         Last eight bytes are the counter, little-endian encoded.
         Maximum value is 2**64 - 2.
         Connection must be dropped and restarted after
         it reaches that value.
         The value 2**64 - 1 must never be sent.

ad :: In handshake phase:
      Associated data, 32 bytes.
      The SHA256 hash of all preceding data.
      In data phase:
      Zero bytes

data :: Plaintext data, 0 or more bytes
```
Şifreleme fonksiyonunun çıktısı, şifre çözme fonksiyonunun girdisi:

```
+----+----+----+----+----+----+----+----+
|Obfs Len |                             |
+----+----+                             +
|       ChaCha20 encrypted data         |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|  Poly1305 Message Authentication Code |
+              (MAC)                    +
|             16 bytes                  |
+----+----+----+----+----+----+----+----+

Obfs Len :: Length of (encrypted data + MAC) to follow, 16 - 65535
            Obfuscation using SipHash (see below)
            Not used in message 1 or 2, or message 3 part 1, where the length is fixed
            Not used in message 3 part 1, as the length is specified in message 1

encrypted data :: Same size as plaintext data, 0 - 65519 bytes

MAC :: Poly1305 message authentication code, 16 bytes
```
ChaCha20 için burada açıklanan, TLS [RFC-7905](https://tools.ietf.org/html/rfc7905)'te benzer şekilde kullanılan [RFC-7539](https://tools.ietf.org/html/rfc7539)'a karşılık gelir.

#### Notlar

- ChaCha20 bir akış şifresi olduğundan, düz metinlerin doldurulması gerekmez. Ek keystream baytları atılır.
- Şifre için anahtar (256 bit) SHA256 KDF vasıtasıyla kararlaştırılır. Her mesaj için KDF'nin ayrıntıları aşağıdaki ayrı bölümlerde yer almaktadır.
- Mesaj 1, 2 ve mesaj 3'ün ilk bölümü için ChaChaPoly çerçeveleri bilinen boyuttadır. Mesaj 3'ün ikinci bölümünden başlayarak, çerçeveler değişken boyuttadır. Mesaj 3 bölüm 1 boyutu mesaj 1'de belirtilir. Veri aşamasından başlayarak, çerçeveler obfs4'teki gibi SipHash ile gizlenmiş iki baytlık uzunlukla başa eklenir.
- Doldurma, mesaj 1 ve 2 için kimlik doğrulamalı veri çerçevesinin dışındadır. Doldurma bir sonraki mesaj için KDF'de kullanılır, böylece kurcalama tespit edilir. Mesaj 3'ten başlayarak, doldurma kimlik doğrulamalı veri çerçevesinin içindedir.

#### AEAD Hata İşleme

- Mesaj 1, 2 ve mesaj 3'ün 1. ve 2. bölümlerinde, AEAD mesaj boyutu önceden bilinmektedir. Bir AEAD kimlik doğrulama hatasında, alıcı daha fazla mesaj işlemeyi durdurmalı ve yanıt vermeden bağlantıyı kapatmalıdır. Bu anormal bir kapanış olmalıdır (TCP RST).
- Yoklama direnci için, mesaj 1'de, bir AEAD hatasından sonra, Bob rastgele bir zaman aşımı ayarlamalı (aralık TBD) ve sonra soketi kapatmadan önce rastgele sayıda bayt okumalıdır (aralık TBD). Bob tekrarlanan hatalar olan IP'lerin kara listesini tutmalıdır.
- Veri aşamasında, AEAD mesaj boyutu SipHash ile "şifrelenmiştir" (gizlenmiştir). Bir şifre çözme oracle'ı oluşturmaktan kaçınmak için dikkat edilmelidir. Veri aşaması AEAD kimlik doğrulama hatasında, alıcı rastgele bir zaman aşımı ayarlamalı (aralık TBD) ve sonra rastgele sayıda bayt okumalıdır (aralık TBD). Okuma sonrasında veya okuma zaman aşımında, alıcı "AEAD hatası" neden kodu içeren bir sonlandırma bloğu ile yük göndermeli ve bağlantıyı kapatmalıdır.
- Veri aşamasındaki geçersiz uzunluk alanı değeri için aynı hata eylemini gerçekleştirin.

### Anahtar Türetme Fonksiyonu (KDF) (handshake mesajı 1 için)

KDF, DH sonucundan bir handshake aşaması şifreleme anahtarı k üretir ve [RFC-2104](https://tools.ietf.org/html/rfc2104)'te tanımlandığı şekilde HMAC-SHA256(key, data) kullanır. Bunlar InitializeSymmetric(), MixHash() ve MixKey() fonksiyonlarıdır ve tam olarak Noise spesifikasyonunda tanımlandığı gibidir.

```
This is the "e" message pattern:

// Define protocol_name.
Set protocol_name = "Noise_XKaesobfse+hs2+hs3_25519_ChaChaPoly_SHA256"
 (48 bytes, US-ASCII encoded, no NULL termination).

// Define Hash h = 32 bytes
h = SHA256(protocol_name);

Define ck = 32 byte chaining key. Copy the h data to ck.
Set ck = h

Define rs = Bob's 32-byte static key as published in the RouterInfo

// MixHash(null prologue)
h = SHA256(h);

// up until here, can all be precalculated by Alice for all outgoing connections

// Alice must validate that Bob's static key is a valid point on the curve here.

// Bob static key
// MixHash(rs)
// || below means append
h = SHA256(h || rs);

// up until here, can all be precalculated by Bob for all incoming connections

This is the "e" message pattern:

Alice generates her ephemeral DH key pair e.

// Alice ephemeral key X
// MixHash(e.pubkey)
// || below means append
h = SHA256(h || e.pubkey);

// h is used as the associated data for the AEAD in message 1
// Retain the Hash h for the message 2 KDF


End of "e" message pattern.

This is the "es" message pattern:

// DH(e, rs) == DH(s, re)
Define input_key_material = 32 byte DH result of Alice's ephemeral key and Bob's static key
Set input_key_material = X25519 DH result

// MixKey(DH())

Define temp_key = 32 bytes
Define HMAC-SHA256(key, data) as in [RFC-2104]_
// Generate a temp key from the chaining key and DH result
// ck is the chaining key, defined above
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

// retain the chaining key ck for message 2 KDF


End of "es" message pattern.
```
### 1) SessionRequest

Alice, Bob'a gönderir.

Noise içeriği: Alice'in geçici anahtarı X Noise yükü: 16 bayt seçenek bloğu Noise olmayan yük: Rastgele dolgu

(Payload Security Properties [Noise](https://noiseprotocol.org/noise.html) protokolünden)

```
XK(s, rs):           Authentication   Confidentiality
  -> e, es                  0                2

  Authentication: None (0).
  This payload may have been sent by any party, including an active attacker.

  Confidentiality: 2.
  Encryption to a known recipient, forward secrecy for sender compromise
  only, vulnerable to replay.  This payload is encrypted based only on DHs
  involving the recipient's static key pair.  If the recipient's static
  private key is compromised, even at a later date, this payload can be
  decrypted.  This message can also be replayed, since there's no ephemeral
  contribution from the recipient.

  "e": Alice generates a new ephemeral key pair and stores it in the e
       variable, writes the ephemeral public key as cleartext into the
       message buffer, and hashes the public key along with the old h to
       derive a new h.

  "es": A DH is performed between the Alice's ephemeral key pair and the
        Bob's static key pair.  The result is hashed along with the old ck to
        derive a new ck and k, and n is set to zero.
```
X değeri, DPI karşı önlemleri için gerekli olan yük ayırt edilemezliği ve benzersizliği sağlamak için şifrelenir. Bunu başarmak için elligator2 gibi daha karmaşık ve yavaş alternatiflerin yerine AES şifreleme kullanırız. Bob'un router genel anahtarına asimetrik şifreleme çok yavaş olurdu. AES şifreleme, anahtar olarak Bob'un router hash'ini ve netDb'de yayınlanan Bob'un IV'sini kullanır.

AES şifreleme yalnızca DPI direnci içindir. Bob'un router hash'ini ve ağ veritabanında yayınlanan IV'ü bilen herhangi bir taraf bu mesajdaki X değerini deşifre edebilir.

Dolgu Alice tarafından şifrelenmez. Zamanlama saldırılarını engellemek için Bob'un dolguyu şifrelemesi gerekli olabilir.

Ham içerikler:

```
+----+----+----+----+----+----+----+----+
|                                       |
+        obfuscated with RH_B           +
|       AES-CBC-256 encrypted X         |
+             (32 bytes)                +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaChaPoly frame                    |
+             (32 bytes)                +
|   k defined in KDF for message 1      |
+   n = 0                               +
|   see KDF for associated data         |
+----+----+----+----+----+----+----+----+
|     unencrypted authenticated         |
~         padding (optional)            ~
|     length defined in options block   |
+----+----+----+----+----+----+----+----+

X :: 32 bytes, AES-256-CBC encrypted X25519 ephemeral key, little endian
        key: RH_B
        iv: As published in Bobs network database entry

padding :: Random data, 0 or more bytes.
           Total message length must be 65535 bytes or less.
           Total message length must be 287 bytes or less if
           Bob is publishing his address as NTCP
           (see Version Detection section below).
           Alice and Bob will use the padding data in the KDF for message 2.
           It is authenticated so that any tampering will cause the
           next message to fail.
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

X :: 32 bytes, X25519 ephemeral key, little endian

options :: options block, 16 bytes, see below

padding :: Random data, 0 or more bytes.
           Total message length must be 65535 bytes or less.
           Total message length must be 287 bytes or less if
           Bob is publishing his address as "NTCP"
           (see Version Detection section below)
           Alice and Bob will use the padding data in the KDF for message 2.
           It is authenticated so that any tampering will cause the
           next message to fail.
```
Seçenekler bloğu: Not: Tüm alanlar big-endian formatındadır.

```
+----+----+----+----+----+----+----+----+
| id | ver|  padLen | m3p2len | Rsvd(0) |
+----+----+----+----+----+----+----+----+
|        tsA        |   Reserved (0)    |
+----+----+----+----+----+----+----+----+

id :: 1 byte, the network ID (currently 2, except for test networks)
      As of 0.9.42. See proposal 147.

ver :: 1 byte, protocol version (currently 2)

padLen :: 2 bytes, length of the padding, 0 or more
          Min/max guidelines TBD. Random size from 0 to 31 bytes minimum?
          (Distribution is implementation-dependent)

m3p2Len :: 2 bytes, length of the the second AEAD frame in SessionConfirmed
           (message 3 part 2) See notes below

Rsvd :: 2 bytes, set to 0 for compatibility with future options

tsA :: 4 bytes, Unix timestamp, unsigned seconds.
       Wraps around in 2106

Reserved :: 4 bytes, set to 0 for compatibility with future options
```
#### Notlar

- Yayınlanan adres "NTCP" olduğunda, Bob aynı port üzerinde hem NTCP hem de NTCP2'yi destekler. Uyumluluk için, "NTCP" olarak yayınlanan bir adrese bağlantı başlatırken, Alice bu mesajın padding dahil olmak üzere maksimum boyutunu 287 bayt veya daha az ile sınırlamalıdır. Bu, Bob tarafından otomatik protokol tanımlamasını kolaylaştırır. "NTCP2" olarak yayınlandığında, boyut kısıtlaması yoktur. Aşağıdaki Yayınlanan Adresler ve Sürüm Algılama bölümlerine bakın.

- İlk AES bloğundaki benzersiz X değeri, şifrelenmiş metnin her oturum için farklı olmasını sağlar.

- Bob, zaman damgası değeri mevcut zamandan çok uzak olan bağlantıları reddetmelidir. Maksimum delta zamanını "D" olarak adlandırın. Bob, replay saldırılarını önlemek için daha önce kullanılmış handshake değerlerinin yerel bir önbelleğini tutmalı ve duplikatları reddetmelidir. Önbellekteki değerlerin en az 2*D yaşam süresine sahip olması gerekir. Önbellek değerleri uygulama bağımlıdır, ancak 32-byte X değeri (veya şifrelenmiş eşdeğeri) kullanılabilir.

- Diffie-Hellman geçici anahtarları kriptografik saldırıları önlemek için asla yeniden kullanılmamalıdır ve yeniden kullanım bir tekrar saldırısı olarak reddedilecektir.

- "KE" ve "auth" seçenekleri uyumlu olmalıdır, yani paylaşılan gizli K uygun boyutta olmalıdır. Daha fazla "auth" seçeneği eklenirse, bu "KE" bayrağının anlamını farklı bir KDF veya farklı bir kesme boyutu kullanacak şekilde örtük olarak değiştirebilir.

- Bob, Alice'in geçici anahtarının burada eğri üzerinde geçerli bir nokta olduğunu doğrulamalıdır.

- Padding makul bir miktarla sınırlandırılmalıdır. Bob aşırı padding içeren bağlantıları reddedebilir. Bob padding seçeneklerini mesaj 2'de belirtecektir. Min/maks yönergeleri henüz belirlenmedi. 0'dan 31 bayta kadar rastgele boyut minimum? (Dağıtım implementasyona bağlıdır) Java implementasyonları şu anda padding'i maksimum 256 baytla sınırlandırıyor.

- AEAD, DH, zaman damgası, görünür tekrar oynatma veya anahtar doğrulama hatası dahil olmak üzere herhangi bir hata durumunda, Bob daha fazla mesaj işlemeyi durdurmalı ve yanıt vermeden bağlantıyı kapatmalıdır. Bu anormal bir kapanma (TCP RST) olmalıdır. Yoklama direnci için, bir AEAD hatasından sonra Bob rastgele bir zaman aşımı (aralık TBD) ayarlamalı ve ardından soket kapatmadan önce rastgele sayıda bayt (aralık TBD) okumalıdır.

- Bob, şifre çözme işlemini denemeden önce geçerli bir anahtar için hızlı bir MSB kontrolü yapabilir (X[31] & 0x80 == 0). Yüksek bit ayarlanmışsa, AEAD hatalarında olduğu gibi yoklama direnci uygulayın.

- DoS Hafifletme: DH nispeten pahalı bir işlemdir. Önceki NTCP protokolünde olduğu gibi, router'lar CPU veya bağlantı tükenmesini önlemek için gerekli tüm önlemleri almalıdır. Maksimum aktif bağlantılar ve devam eden maksimum bağlantı kurulumları için sınırlar koyun. Okuma zaman aşımlarını uygulayın (hem okuma başına hem de "slowloris" için toplam). Aynı kaynaktan tekrarlayan veya eşzamanlı bağlantıları sınırlayın. Tekrar tekrar başarısız olan kaynaklar için kara listeler tutun. AEAD başarısızlığına yanıt vermeyin.

- Hızlı versiyon tespiti ve el sıkışmayı kolaylaştırmak için, uygulamalar Alice'in ilk mesajın tüm içeriğini (dolgu dahil) önce tamponlamasını ve ardından bir kerede temizlemesini sağlamalıdır. Bu, verilerin tek bir TCP paketinde bulunma olasılığını artırır (işletim sistemi veya middlebox'lar tarafından bölünmedikçe) ve Bob tarafından aynı anda alınmasını sağlar. Ek olarak, uygulamalar Bob'un ikinci mesajın tüm içeriğini (dolgu dahil) önce tamponlamasını ve ardından bir kerede temizlemesini sağlamalıdır. ve Bob'un üçüncü mesajın tüm içeriğini önce tamponlamasını ve ardından bir kerede temizlemesini sağlamalıdır. Bu da verimlilik için ve rastgele dolgunun etkinliğini sağlamak içindir.

- "ver" alanı: Genel Noise protokolü, uzantılar ve yük belirtimleri dahil olmak üzere NTCP2'yi belirten NTCP protokolü. Bu alan gelecekteki değişiklikler için desteği belirtmek amacıyla kullanılabilir.

- Mesaj 3 bölüm 2 uzunluğu: Bu, SessionConfirmed mesajında gönderilecek olan Alice'in Router Info'sunu ve isteğe bağlı dolguyu içeren ikinci AEAD frame'inin boyutudur (16-baytlık MAC dahil). Router'lar periyodik olarak Router Info'larını yeniden oluşturup yeniden yayınladıkları için, mevcut Router Info'nun boyutu mesaj 3 gönderilmeden önce değişebilir. Implementasyonlar iki stratejiden birini seçmelidir:

a\) mesaj 3'te gönderilecek mevcut Router Info'yu kaydet, böylece boyut bilinir ve isteğe bağlı olarak dolgu için yer ekle;

b\) Router Info boyutunda olası artışa izin verecek kadar belirtilen boyutu artırın ve mesaj 3 gerçekten gönderildiğinde her zaman dolgu ekleyin. Her iki durumda da, mesaj 1'e dahil edilen "m3p2len" uzunluğu, mesaj 3'te gönderildiğinde o çerçevenin boyutuyla tam olarak aynı olmalıdır.

- Bob, mesaj 1'i doğruladıktan ve padding'i okuduktan sonra herhangi bir gelen veri kalırsa bağlantıyı başarısız kılmalıdır. Alice'ten fazladan veri olmamalıdır, çünkü Bob henüz mesaj 2 ile yanıt vermemiştir.

- Ağ kimliği alanı, çapraz ağ bağlantılarını hızlıca tanımlamak için kullanılır. Bu alan sıfır değilse ve Bob'un ağ kimliği ile eşleşmiyorsa, Bob bağlantıyı kesip gelecekteki bağlantıları engellemeli. Test ağlarından gelen herhangi bir bağlantı farklı bir kimliğe sahip olmalı ve testi geçemeyecek. 0.9.42 sürümü itibariyle. Daha fazla bilgi için öneri 147'ye bakın.

### Anahtar Türetme Fonksiyonu (KDF) (handshake mesajı 2 ve mesaj 3 bölüm 1 için)

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

Bob, Alice'e gönderir.

Noise içeriği: Bob'un geçici anahtarı Y Noise yükü: 16 bayt seçenek bloğu Noise olmayan yük: Rastgele dolgu

(Payload Security Properties [Noise](https://noiseprotocol.org/noise.html) protokolünden)

```
XK(s, rs):           Authentication   Confidentiality
  <- e, ee                  2                1

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 1.
  Encryption to an ephemeral recipient.
  This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee").
  However, the sender has not authenticated the recipient,
  so this payload might be sent to any party, including an active attacker.


  "e": Bob generates a new ephemeral key pair and stores it in the e variable,
  writes the ephemeral public key as cleartext into the message buffer,
  and hashes the public key along with the old h to derive a new h.

  "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair.
  The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Y değeri, gerekli DPI karşı önlemleri olan yük ayırt edilemezliği ve benzersizliği sağlamak için şifrelenir. Bunu başarmak için elligator2 gibi daha karmaşık ve yavaş alternatifler yerine AES şifreleme kullanırız. Alice'in router genel anahtarına asimetrik şifreleme çok yavaş olacaktır. AES şifreleme, anahtar olarak Bob'un router hash'ini ve mesaj 1'deki AES durumunu kullanır (bu, network database'de yayımlanan Bob'un IV'si ile başlatılmıştı).

AES şifreleme yalnızca DPI direnci içindir. Bob'un router hash'ini ve IV'sini (bunlar ağ veritabanında yayınlanır) bilen ve mesaj 1'in ilk 32 baytını yakalayan herhangi bir taraf, bu mesajdaki Y değerini şifreleyebilir.

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
|   ChaChaPoly frame                    |
+   Encrypted and authenticated data    +
|   32 bytes                            |
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

Y :: 32 bytes, AES-256-CBC encrypted X25519 ephemeral key, little endian
        key: RH_B
        iv: Using AES state from message 1
```
Şifrelenmemiş veri (Poly1305 doğrulama etiketi gösterilmedi):

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

Y :: 32 bytes, X25519 ephemeral key, little endian

options :: options block, 16 bytes, see below

padding :: Random data, 0 or more bytes.
           Total message length must be 65535 bytes or less.
           Alice and Bob will use the padding data in the KDF for message 3 part 1.
           It is authenticated so that any tampering will cause the
           next message to fail.
```
#### Notlar

- Alice, Bob'un geçici anahtarının burada eğri üzerinde geçerli bir nokta olduğunu doğrulamalıdır.
- Dolgu makul bir miktarla sınırlandırılmalıdır. Alice aşırı dolgulu bağlantıları reddedebilir. Alice dolgu seçeneklerini mesaj 3'te belirtecektir. Min/maks yönergeleri henüz belirlenmemiştir. Minimum 0 ila 31 bayt arasında rastgele boyut? (Dağılım uygulamaya bağlıdır)
- AEAD, DH, zaman damgası, görünür yeniden oynatma veya anahtar doğrulama hatası dahil herhangi bir hatada, Alice daha fazla mesaj işlemeyi durdurmalı ve yanıt vermeden bağlantıyı kapatmalıdır. Bu anormal bir kapanma olmalıdır (TCP RST).
- Hızlı el sıkışmayı kolaylaştırmak için, uygulamalar Bob'un ilk mesajın tüm içeriğini dolgu dahil olmak üzere arabelleğe alması ve ardından bir kerede temizlemesini sağlamalıdır. Bu, verilerin tek bir TCP paketinde bulunma (OS veya orta kutular tarafından bölümlenmedikçe) ve Alice tarafından bir kerede alınma olasılığını artırır. Bu aynı zamanda verimlilik için ve rastgele dolgunun etkinliğini sağlamak içindir.
- Alice, mesaj 2'yi doğruladıktan ve dolguyu okuduktan sonra herhangi bir gelen veri kalırsa bağlantıyı başarısız kılmalıdır. Bob'tan fazladan veri olmamalıdır, çünkü Alice henüz mesaj 3 ile yanıt vermemiştir.

Seçenekler bloğu: Not: Tüm alanlar big-endian formatındadır.

```
+----+----+----+----+----+----+----+----+
| Rsvd(0) | padLen  |   Reserved (0)    |
+----+----+----+----+----+----+----+----+
|        tsB        |   Reserved (0)    |
+----+----+----+----+----+----+----+----+

Reserved :: 10 bytes total, set to 0 for compatibility with future options

padLen :: 2 bytes, big endian, length of the padding, 0 or more
          Min/max guidelines TBD. Random size from 0 to 31 bytes minimum?
          (Distribution is implementation-dependent)

tsB :: 4 bytes, big endian, Unix timestamp, unsigned seconds.
       Wraps around in 2106
```
#### Notlar

- Alice, zaman damgası değeri mevcut zamandan çok uzak olan bağlantıları reddetmelidir. Maksimum delta zamanını "D" olarak adlandırın. Alice, tekrar saldırılarını önlemek için daha önce kullanılmış handshake değerlerinin yerel önbelleğini tutmalı ve kopyaları reddetmelidir. Önbellekteki değerler en az 2*D yaşam süresine sahip olmalıdır. Önbellek değerleri implementasyona bağımlıdır, ancak 32-byte Y değeri (veya şifrelenmiş eşdeğeri) kullanılabilir.

#### Sorunlar

- Min/maks dolgulama seçenekleri buraya dahil edilsin mi?

### Handshake mesajı 3 bölüm 1 için şifreleme, mesaj 2 KDF kullanarak)

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
### Anahtar Türetme Fonksiyonu (KDF) (handshake mesajı 3 bölüm 2 için)

```
This is the "se" message pattern:

// DH(s, re) == DH(e, rs)
Define input_key_material = 32 byte DH result of Alice's static key and Bob's ephemeral key
Set input_key_material = X25519 DH result
// overwrite Bob's ephemeral key in memory, no longer needed
// Alice:
re = (all zeros)
// Bob:
e(public and private) = (all zeros)

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

// h from message 3 part 1 is used as the associated data for the AEAD in message 3 part 2

// EncryptAndHash(payload)
// EncryptWithAd(h, payload)
// AEAD_ChaCha20_Poly1305(key, nonce, associatedData, data)
// n is 0
ciphertext = AEAD_ChaCha20_Poly1305(k, n++, h, payload)
// MixHash(ciphertext)
// || below means append
h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF
// retain the hash h for the data phase Additional Symmetric Key (SipHash) KDF

End of "se" message pattern.

// overwrite the temp_key in memory, no longer needed
temp_key = (all zeros)
```
### 3) SessionConfirmed

Alice, Bob'a gönderir.

Noise içeriği: Alice'in statik anahtarı Noise yükü: Alice'in RouterInfo'su ve rastgele dolgu Non-noise yükü: yok

(Yük Güvenlik Özellikleri [Noise](https://noiseprotocol.org/noise.html) protokolünden)

```
XK(s, rs):           Authentication   Confidentiality
  -> s, se                  2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).  The
  sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key
  pair.  Assuming the corresponding private keys are secure, this
  authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.  This payload is
  encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static
  DH with the recipient's static key pair.  Assuming the ephemeral private
  keys are secure, and the recipient is not being actively impersonated by an
  attacker that has stolen its static private key, this payload cannot be
  decrypted.

  "s": Alice writes her static public key from the s variable into the
  message buffer, encrypting it, and hashes the output along with the old h
  to derive a new h.

  "se": A DH is performed between the Alice's static key pair and the Bob's
  ephemeral key pair.  The result is hashed along with the old ck to derive a
  new ck and k, and n is set to zero.
```
Bu, iki ChaChaPoly çerçevesi içerir. İlki Alice'in şifrelenmiş statik public anahtarıdır. İkincisi Noise payload'ıdır: Alice'in şifrelenmiş RouterInfo'su, isteğe bağlı seçenekler ve isteğe bağlı padding. Bunlar farklı anahtarlar kullanır çünkü aralarında MixKey() fonksiyonu çağrılır.

Ham içerik:

```
+----+----+----+----+----+----+----+----+
|                                       |
+   ChaChaPoly frame (48 bytes)         +
|   Encrypted and authenticated         |
+   Alice static key S                  +
|      (32 bytes)                       |
+                                       +
|     k defined in KDF for message 2    |
+     n = 1                             +
|     see KDF for associated data       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+     Length specified in message 1     +
|                                       |
+   ChaChaPoly frame                    +
|   Encrypted and authenticated         |
+                                       +
|       Alice RouterInfo                |
+       using block format 2            +
|       Alice Options (optional)        |
+       using block format 1            +
|       Arbitrary padding               |
+       using block format 254          +
|                                       |
+                                       +
| k defined in KDF for message 3 part 2 |
+     n = 0                             +
|     see KDF for associated data       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, ChaChaPoly encrypted Alice's X25519 static key, little endian
     inside 48 byte ChaChaPoly frame
```
Şifrelenmemiş veri (Poly1305 kimlik doğrulama etiketleri gösterilmemiştir):

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|              S                        |
+       Alice static key                +
|          (32 bytes)                   |
+                                       +
|                                       |
+                                       +
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                                       |
+                                       +
|       Alice RouterInfo block          |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+       Optional Options block          +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+       Optional Padding block          +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, Alice's X25519 static key, little endian
```
#### Notlar

- Bob, olağan Router Info doğrulamasını gerçekleştirmeli. İmza türünün desteklendiğinden emin olun, imzayı doğrulayın, zaman damgasının sınırlar içinde olduğunu doğrulayın ve gerekli diğer kontrolleri yapın.

- Bob, ilk çerçevede aldığı Alice'in statik anahtarının Router Info'daki statik anahtarla eşleştiğini doğrulamalıdır. Bob önce Router Info'da eşleşen sürüm (v) seçeneği olan bir NTCP veya NTCP2 Router Address aramalıdır. Aşağıdaki Yayınlanmış Router Info ve Yayınlanmamış Router Info bölümlerine bakınız.

- Eğer Bob'un netdb'sinde Alice'in RouterInfo'sunun eski bir sürümü varsa, router info'daki statik anahtarın her ikisinde de aynı olduğunu doğrulayın (varsa), ve eski sürüm XXX'den daha az eskiyse (aşağıdaki anahtar döndürme zamanına bakın)

- Bob, Alice'in statik anahtarının burada eğri üzerinde geçerli bir nokta olduğunu doğrulamalıdır.

- Padding parametrelerini belirtmek için seçenekler dahil edilmelidir.

- AEAD, RI, DH, zaman damgası veya anahtar doğrulama hatası dahil herhangi bir hata durumunda, Bob daha fazla mesaj işlemini durdurmalı ve yanıt vermeden bağlantıyı kapatmalıdır. Bu anormal bir kapatma (TCP RST) olmalıdır.

- Hızlı el sıkışmayı kolaylaştırmak için, uygulamalar Alice'in üçüncü mesajın tüm içeriğini (her iki AEAD çerçevesini de dahil olmak üzere) bir kerede tamponlamasını ve ardından aktarmasını sağlamalıdır. Bu, verilerin (işletim sistemi veya ara kutular tarafından bölümlenmedikçe) tek bir TCP paketinde bulunma olasılığını artırır ve Bob tarafından aynı anda alınmasını sağlar. Bu aynı zamanda verimlilik için ve rastgele dolgunun etkinliğini sağlamak içindir.

- Mesaj 3 bölüm 2 çerçeve uzunluğu: Bu çerçevenin uzunluğu (MAC dahil) Alice tarafından mesaj 1'de gönderilir. Dolgu için yeterli alan bırakma konusundaki önemli notlar için o mesaja bakın.

- Mesaj 3 bölüm 2 çerçeve içeriği: Bu çerçevenin formatı veri fazı çerçevelerinin formatıyla aynıdır, ancak çerçevenin uzunluğu Alice tarafından mesaj 1'de gönderilir. Veri fazı çerçeve formatı için aşağıya bakın. Çerçeve aşağıdaki sırayla 1 ila 3 blok içermelidir:

1)  Alice'in Router Info bloğu (gerekli)   2)  Seçenekler bloğu (isteğe bağlı)

3\) Doldurma bloğu (isteğe bağlı) Bu çerçeve asla başka bir blok türü içermemelidir.

- Alice, mesaj 3'ün sonuna bir veri fazı çerçevesi (isteğe bağlı olarak padding içeren) ekleyip ikisini birden gönderirse, mesaj 3 bölüm 2 padding'i gerekli değildir, çünkü bir gözlemciye tek bir büyük bayt akışı gibi görünecektir. Alice genellikle (ama her zaman değil) Bob'a gönderilecek bir I2NP mesajına sahip olacağından (bu yüzden ona bağlandı), bu uygulama verimlilik açısından ve rastgele padding'in etkinliğini sağlamak için önerilir.

- Her iki Message 3 AEAD çerçevesinin (bölüm 1 ve 2) toplam uzunluğu 65535 bayttır; bölüm 1, 48 bayt olduğu için bölüm 2'nin maksimum çerçeve uzunluğu 65487'dir; bölüm 2'nin MAC hariç maksimum düz metin uzunluğu 65471'dir.

### Anahtar Türetme Fonksiyonu (KDF) (veri aşaması için)

Veri aşaması sıfır uzunlukta ilişkili veri girişi kullanır.

KDF, zincirleme anahtarı ck'dan iki şifre anahtarı k_ab ve k_ba üretir, [RFC-2104](https://tools.ietf.org/html/rfc2104)'te tanımlandığı gibi HMAC-SHA256(key, data) kullanarak. Bu, Noise spec'inde tam olarak tanımlandığı şekliyle Split() fonksiyonudur.

```
ck = from handshake phase

// k_ab, k_ba = HKDF(ck, zerolen)
// ask_master = HKDF(ck, zerolen, info="ask")

// zerolen is a zero-length byte array
temp_key = HMAC-SHA256(ck, zerolen)
// overwrite the chaining key in memory, no longer needed
ck = (all zeros)

// Output 1
// cipher key, for Alice transmits to Bob (Noise doesn't make clear which is which, but Java code does)
k_ab =   HMAC-SHA256(temp_key, byte(0x01)).

// Output 2
// cipher key, for Bob transmits to Alice (Noise doesn't make clear which is which, but Java code does)
k_ba =   HMAC-SHA256(temp_key, k_ab || byte(0x02)).


KDF for SipHash for length field:
Generate an Additional Symmetric Key (ask) for SipHash
SipHash uses two 8-byte keys (big endian) and 8 byte IV for first data.

// "ask" is 3 bytes, US-ASCII, no null termination
ask_master = HMAC-SHA256(temp_key, "ask" || byte(0x01))
// sip_master = HKDF(ask_master, h || "siphash")
// "siphash" is 7 bytes, US-ASCII, no null termination
// overwrite previous temp_key in memory
// h is from KDF for message 3 part 2
temp_key = HMAC-SHA256(ask_master, h || "siphash")
// overwrite ask_master in memory, no longer needed
ask_master = (all zeros)
sip_master = HMAC-SHA256(temp_key, byte(0x01))

Alice to Bob SipHash k1, k2, IV:
// sipkeys_ab, sipkeys_ba = HKDF(sip_master, zerolen)
// overwrite previous temp_key in memory
temp_key = HMAC-SHA256(sip_master, zerolen)
// overwrite sip_master in memory, no longer needed
sip_master = (all zeros)

sipkeys_ab = HMAC-SHA256(temp_key, byte(0x01)).
sipk1_ab = sipkeys_ab[0:7], little endian
sipk2_ab = sipkeys_ab[8:15], little endian
sipiv_ab = sipkeys_ab[16:23]

Bob to Alice SipHash k1, k2, IV:

sipkeys_ba = HMAC-SHA256(temp_key, sipkeys_ab || byte(0x02)).
sipk1_ba = sipkeys_ba[0:7], little endian
sipk2_ba = sipkeys_ba[8:15], little endian
sipiv_ba = sipkeys_ba[16:23]

// overwrite the temp_key in memory, no longer needed
temp_key = (all zeros)
```
### 4) Veri Aşaması

Noise payload: Aşağıda tanımlandığı gibi, rastgele dolgu dahil Non-noise payload: yok

Mesaj 3'ün 2. bölümünden başlayarak, tüm mesajlar önüne eklenmiş iki baytlık gizlenmiş uzunluğa sahip kimlik doğrulamalı ve şifrelenmiş ChaChaPoly "çerçevesi" içindedir. Tüm dolgu çerçeve içindedir. Çerçeve içinde sıfır veya daha fazla "blok" içeren standart bir format bulunur. Her blok bir baytlık tip ve iki baytlık uzunluğa sahiptir. Tipler arasında tarih/saat, I2NP mesajı, seçenekler, sonlandırma ve dolgu yer alır.

Not: Bob, veri aşamasında Alice'e gönderdiği ilk mesaj olarak RouterInfo'sunu gönderebilir, ancak bunu yapmak zorunda değildir.

(Yük Güvenlik Özellikleri [Noise](https://noiseprotocol.org/noise.html)'dan)

```
XK(s, rs):           Authentication   Confidentiality
  <-                        2                5
  ->                        2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.
  This payload is encrypted based on an ephemeral-ephemeral DH as well as
  an ephemeral-static DH with the recipient's static key pair.
  Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated
  by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### Notlar

- Verimlilik için ve uzunluk alanının tanımlanmasını en aza indirmek için, uygulamalar gönderenin veri mesajlarının tüm içeriğini (uzunluk alanı ve AEAD çerçevesi dahil) arabelleğe alıp sonra bir kerede temizlemesini sağlamalıdır. Bu, verinin tek bir TCP paketinde bulunma olasılığını artırır (işletim sistemi veya ara kutular tarafından bölümlenmediği sürece) ve karşı tarafın tümünü aynı anda almasını sağlar. Bu aynı zamanda verimlilik içindir ve rastgele dolgulamanın etkinliğini garanti etmek içindir.
- Router, AEAD hatası durumunda oturumu sonlandırmayı seçebilir veya iletişim kurmaya devam etmeye çalışabilir. Devam ederse, router tekrarlanan hatalardan sonra sonlandırmalıdır.

#### SipHash gizlenmiş uzunluk

Referans: [SipHash](https://www.131002.net/siphash/)

Her iki taraf da el sıkışmayı tamamladıktan sonra, ChaChaPoly "çerçeveleri" içinde şifrelenmiş ve doğrulanmış yükler aktarırlar.

Her frame, iki baytlık bir uzunluk değeri ile başlar (big endian). Bu uzunluk, MAC dahil olmak üzere takip eden şifrelenmiş frame baytlarının sayısını belirtir. Akışta tanımlanabilir uzunluk alanlarının iletilmesini önlemek için, frame uzunluğu, veri aşaması KDF'sinden başlatılan SipHash'ten türetilen bir mask ile XOR işlemine tabi tutularak gizlenir. İki yönün KDF'den benzersiz SipHash anahtarları ve IV'leri olduğunu unutmayın.

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
Alıcı aynı SipHash anahtarlarına ve IV'ye sahiptir. Uzunluğun çözülmesi, uzunluğu gizlemek için kullanılan maskeyi türeterek ve frame'in uzunluğunu elde etmek için kısaltılmış digest ile XOR işlemi yaparak gerçekleştirilir. Frame uzunluğu, MAC dahil olmak üzere şifrelenmiş frame'in toplam uzunluğudur.

#### Notlar

- Unsigned long integer döndüren bir SipHash kütüphane fonksiyonu kullanıyorsanız, en az anlamlı iki baytı Mask olarak kullanın. Long integer'ı sonraki IV'ye little endian olarak dönüştürün.

#### Ham içerikler

```
+----+----+----+----+----+----+----+----+
|obf size |                             |
+----+----+                             +
|                                       |
+   ChaChaPoly frame                    +
|   Encrypted and authenticated         |
+   key is k_ab for Alice to Bob        +
|   key is k_ba for Bob to Alice        |
+   as defined in KDF for data phase    +
|   n starts at 0 and increments        |
+   for each frame in that direction    +
|   no associated data                  |
+   16 bytes minimum                    +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

obf size :: 2 bytes length obfuscated with SipHash
            when de-obfuscated: 16 - 65535

Minimum size including length field is 18 bytes.
Maximum size including length field is 65537 bytes.
Obfuscated length is 2 bytes.
Maximum ChaChaPoly frame is 65535 bytes.
```
#### Notlar

- Alıcının MAC'i kontrol etmek için tüm çerçeveyi alması gerektiğinden, gönderenin çerçeve boyutunu maksimuma çıkarmak yerine çerçeveleri birkaç KB ile sınırlaması önerilir. Bu, alıcıdaki gecikmeyi en aza indirecektir.

#### Şifrelenmemiş veri

Şifrelenmiş çerçevede sıfır veya daha fazla blok bulunur. Her blok bir baytlık tanımlayıcı, iki baytlık uzunluk ve sıfır veya daha fazla bayt veri içerir.

Genişletilebilirlik için, alıcılar bilinmeyen tanımlayıcılara sahip blokları görmezden gelmeli ve bunları dolgu (padding) olarak işlemelidir.

Şifrelenmiş veri, 16 baytlık kimlik doğrulama başlığı dahil olmak üzere maksimum 65535 bayttır, dolayısıyla maksimum şifrelenmemiş veri 65519 bayttır.

(Poly1305 auth etiketi gösterilmemiş):

```
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
~               .   .   .               ~

blk :: 1 byte
       0 for datetime
       1 for options
       2 for RouterInfo
       3 for I2NP message
       4 for termination
       224-253 reserved for experimental features
       254 for padding
       255 reserved for future extension
size :: 2 bytes, big endian, size of data to follow, 0 - 65516
data :: the data

Maximum ChaChaPoly frame is 65535 bytes.
Poly1305 tag is 16 bytes
Maximum total block size is 65519 bytes
Maximum single block size is 65519 bytes
Block type is 1 byte
Block length is 2 bytes
Maximum single block data size is 65516 bytes.
```
#### Blok Sıralama Kuralları

Handshake mesajı 3 bölüm 2'de sıralama şu şekilde olmalıdır: RouterInfo, ardından varsa Options, ardından varsa Padding. Başka hiçbir bloğa izin verilmez.

Veri aşamasında sıralama belirtilmemiştir, ancak şu gereksinimler hariç: Padding (dolgulama), mevcutsa, son blok olmalıdır. Termination (sonlandırma), mevcutsa, Padding dışında son blok olmalıdır.

Tek bir çerçevede birden fazla I2NP bloğu bulunabilir. Tek bir çerçevede birden fazla Padding bloğuna izin verilmez. Diğer blok türlerinde muhtemelen tek bir çerçevede birden fazla blok olmayacaktır, ancak bu yasaklanmamıştır.

#### TarihSaat

Zaman senkronizasyonu için özel durum:

```
+----+----+----+----+----+----+----+
| 0  |    4    |     timestamp     |
+----+----+----+----+----+----+----+

blk :: 0
size :: 2 bytes, big endian, value = 4
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
```
NOT: Uygulamalar, ağda saat kayması oluşmaması için en yakın saniyeye yuvarlama yapmalıdır.

#### Seçenekler

Güncellenmiş seçenekleri geç. Seçenekler şunları içerir: Minimum ve maksimum padding.

Options bloğu değişken uzunlukta olacaktır.

```
+----+----+----+----+----+----+----+----+
| 1  |  size   |tmin|tmax|rmin|rmax|tdmy|
+----+----+----+----+----+----+----+----+
|tdmy|  rdmy   |  tdelay |  rdelay |    |
~----+----+----+----+----+----+----+    ~
|              more_options             |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 1
size :: 2 bytes, big endian, size of options to follow, 12 bytes minimum

tmin, tmax, rmin, rmax :: requested padding limits
    tmin and rmin are for desired resistance to traffic analysis.
    tmax and rmax are for bandwidth limits.
    tmin and tmax are the transmit limits for the router sending this options block.
    rmin and rmax are the receive limits for the router sending this options block.
    Each is a 4.4 fixed-point float representing 0 to 15.9375
    (or think of it as an unsigned 8-bit integer divided by 16.0).
    This is the ratio of padding to data. Examples:
    Value of 0x00 means no padding
    Value of 0x01 means add 6 percent padding
    Value of 0x10 means add 100 percent padding
    Value of 0x80 means add 800 percent (8x) padding
    Alice and Bob will negotiate the minimum and maximum in each direction.
    These are guidelines, there is no enforcement.
    Sender should honor receiver's maximum.
    Sender may or may not honor receiver's minimum, within bandwidth constraints.

tdmy: Max dummy traffic willing to send, 2 bytes big endian, bytes/sec average
rdmy: Requested dummy traffic, 2 bytes big endian, bytes/sec average
tdelay: Max intra-message delay willing to insert, 2 bytes big endian, msec average
rdelay: Requested intra-message delay, 2 bytes big endian, msec average

Padding distribution specified as additional parameters?
Random delay specified as additional parameters?

more_options :: Format TBD
```
#### Seçenek Sorunları

- Seçenekler biçimi henüz belirlenmemiştir.
- Seçenekler müzakeresi henüz belirlenmemiştir.

#### RouterInfo

Alice'in RouterInfo'sunu Bob'a ilet. Handshake mesajı 3 bölüm 2'de kullanılır. Alice'in RouterInfo'sunu Bob'a veya Bob'unkini Alice'e ilet. Veri aşamasında isteğe bağlı olarak kullanılır.

```
+----+----+----+----+----+----+----+----+
| 2  |  size   |flg |    RouterInfo     |
+----+----+----+----+                   +
| (Alice RI in handshake msg 3 part 2)  |
~ (Alice, Bob, or third-party           ~
|  RI in data phase)                    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 2
size :: 2 bytes, big endian, size of flag + router info to follow
flg :: 1 byte flags
       bit order: 76543210
       bit 0: 0 for local store, 1 for flood request
       bits 7-1: Unused, set to 0 for future compatibility
routerinfo :: Alice's or Bob's RouterInfo
```
#### Notlar

- Veri fazında kullanıldığında, alıcı (Alice veya Bob) bunun başlangıçta gönderilen (Alice için) veya gönderilen (Bob için) aynı Router Hash olduğunu doğrulamalıdır. Ardından, bunu yerel bir I2NP DatabaseStore Mesajı olarak ele alın. İmzayı doğrulayın, daha güncel zaman damgasını doğrulayın ve yerel netdb'de saklayın. Eğer bayrak bit 0'ı 1 ise ve alıcı taraf floodfill ise, bunu sıfır olmayan yanıt token'ı olan bir DatabaseStore Mesajı olarak ele alın ve en yakın floodfill'lere flood edin.
- Router Info gzip ile sıkıştırılmaz (DatabaseStore Mesajında olduğunun aksine, burada sıkıştırılır)
- RouterInfo'da yayınlanmış RouterAddress'ler olmadıkça flooding talep edilmemelidir. Alıcı router, RouterInfo'da yayınlanmış RouterAddress'ler olmadıkça RouterInfo'yu flood etmemelidir.
- Uygulayıcılar, bir blok okurken, bozuk veya kötü niyetli verilerin okumaların sonraki bloğa taşmasına neden olmayacağından emin olmalıdır.
- Bu protokol RouterInfo'nun alındığı, saklandığı veya flood edildiğine dair onay sağlamaz (ne handshake fazında ne de veri fazında). Eğer onay isteniyorsa ve alıcı floodfill ise, gönderici bunun yerine yanıt token'ı olan standart bir I2NP DatabaseStoreMessage göndermelidir.

#### Sorunlar

- Veri fazında, bir I2NP DatabaseStoreMessage yerine de kullanılabilir. Örneğin, Bob bunu veri fazını başlatmak için kullanabilir.
- Bunun, DatabaseStoreMessage'ların genel bir yedeği olarak, örneğin floodfill'ler tarafından taşırma için, gönderen dışındaki router'lar için RI içermesine izin verilir mi?

#### I2NP Mesajı

Değiştirilmiş başlığa sahip tek bir I2NP mesajı. I2NP mesajları bloklar arasında veya ChaChaPoly çerçeveleri arasında parçalanamaz.

Bu, standart NTCP I2NP başlığından ilk 9 baytı kullanır ve başlığın son 7 baytını şu şekilde kaldırır: son kullanma tarihini 8 bayttan 4 bayta kısaltır (milisaniye yerine saniye, SSU ile aynı), 2 baytlık uzunluğu kaldırır (blok boyutu - 9 kullanır) ve tek baytlık SHA256 sağlama toplamını kaldırır.

```
+----+----+----+----+----+----+----+----+
| 3  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |     message       |
+----+----+----+----+                   +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 3
size :: 2 bytes, big endian, size of type + msg id + exp + message to follow
        I2NP message body size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: I2NP message body
```
#### Notlar

- Uygulayıcılar, bir blok okunurken, hatalı biçimlendirilmiş veya kötü niyetli verilerin okumaların bir sonraki blok içine taşmasına neden olmamasını sağlamalıdır.

#### Sonlandırma

Noise açık bir sonlandırma mesajı önerir. Orijinal NTCP'de böyle bir mesaj yoktur. Bağlantıyı kesin. Bu, çerçevedeki son dolgu olmayan blok olmalıdır.

```
+----+----+----+----+----+----+----+----+
| 4  |  size   |    valid data frames   |
+----+----+----+----+----+----+----+----+
    received   | rsn|     addl data     |
+----+----+----+----+                   +
~               .   .   .               ~
+----+----+----+----+----+----+----+----+

blk :: 4
size :: 2 bytes, big endian, value = 9 or more
valid data frames received :: The number of valid AEAD data phase frames received
                              (current receive nonce value)
                              0 if error occurs in handshake phase
                              8 bytes, big endian
rsn :: reason, 1 byte:
       0: normal close or unspecified
       1: termination received
       2: idle timeout
       3: router shutdown
       4: data phase AEAD failure
       5: incompatible options
       6: incompatible signature type
       7: clock skew
       8: padding violation
       9: AEAD framing error
       10: payload format error
       11: message 1 error
       12: message 2 error
       13: message 3 error
       14: intra-frame read timeout
       15: RI signature verification fail
       16: s parameter missing, invalid, or mismatched in RouterInfo
       17: banned
addl data :: optional, 0 or more bytes, for future expansion, debugging,
             or reason text.
             Format unspecified and may vary based on reason code.
```
#### Notlar

Tüm nedenler gerçekte kullanılmayabilir, uygulama bağımlıdır. Handshake hataları genellikle TCP RST ile kapanmayla sonuçlanacaktır. Yukarıdaki handshake mesaj bölümlerindeki notlara bakın. Listelenen ek nedenler tutarlılık, günlükleme, hata ayıklama veya politika değişiklikleri içindir.

#### Dolgu

Bu AEAD çerçeveleri içindeki dolgu için kullanılır. Mesaj 1 ve 2 için dolgular AEAD çerçevelerinin dışındadır. Mesaj 3 ve veri aşaması için tüm dolgular AEAD çerçevelerinin içindedir.

AEAD içindeki padding kabaca müzakere edilen parametrelere uymalıdır. Bob, mesaj 2'de istenen tx/rx min/max parametrelerini gönderdi. Alice, mesaj 3'te istenen tx/rx min/max parametrelerini gönderdi. Güncellenmiş seçenekler veri aşamasında gönderilebilir. Yukarıdaki seçenekler bloğu bilgilerine bakınız.

Mevcut ise, bu çerçevedeki son blok olmalıdır.

```
+----+----+----+----+----+----+----+----+
|254 |  size   |      padding           |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 254
size :: 2 bytes, big endian, size of padding to follow
padding :: random data
```
#### Notlar

- Size = 0 kullanımına izin verilir.
- Padding stratejileri TBD.
- Minimum padding TBD.
- Yalnızca padding içeren frame'lere izin verilir.
- Padding varsayılanları TBD.
- Padding parametresi müzakeresi için seçenekler bloğuna bakın
- Min/max padding parametreleri için seçenekler bloğuna bakın
- Noise mesajları 64KB ile sınırlar. Daha fazla padding gerekiyorsa, birden fazla frame gönderin.
- Müzakere edilen padding ihlali durumunda router tepkisi uygulama-bağımlıdır.

#### Diğer blok türleri

Uygulamalar, ileri uyumluluk için bilinmeyen blok türlerini görmezden gelmeli, ancak mesaj 3 bölüm 2'de bilinmeyen bloklara izin verilmez.

#### Gelecekteki çalışmalar

- Dolgu uzunluğu ya mesaj bazında karar verilmeli ve uzunluk dağılımı tahminleri kullanılmalı, ya da rastgele gecikmeler eklenmelidir. Bu karşı önlemler DPI'ya (Derin Paket İnceleme) karşı direnç sağlamak için dahil edilmelidir, çünkü aksi takdirde mesaj boyutları taşıma protokolü tarafından I2P trafiğinin taşındığını ortaya çıkaracaktır. Kesin dolgu şeması gelecekteki çalışmaların bir alanıdır.

### 5) Sonlandırma

Bağlantılar normal veya anormal TCP soket kapatma yoluyla veya Noise'ın önerdiği gibi açık bir sonlandırma mesajı ile sonlandırılabilir. Açık sonlandırma mesajı yukarıdaki veri aşamasında tanımlanmıştır.

Herhangi bir normal veya anormal sonlandırma durumunda, router'lar bellekteki tüm geçici verileri sıfırlamalıdır; bunlara handshake geçici anahtarları, simetrik kripto anahtarları ve ilgili bilgiler dahildir.

## Yayınlanan Router Bilgisi

### Yetenekler

0.9.50 sürümünden itibaren, SSU'ya benzer şekilde NTCP2 adreslerinde "caps" seçeneği desteklenmektedir. "caps" seçeneğinde bir veya daha fazla yetenek yayınlanabilir. Yetenekler herhangi bir sırada olabilir, ancak uygulamalar arası tutarlılık için "46" sırası önerilir. Tanımlanmış iki yetenek bulunmaktadır:

4: Giden IPv4 yeteneğini belirtir. Host alanında bir IP yayınlanmışsa, bu yetenek gerekli değildir. Router gizliyse veya NTCP2 yalnızca giden bağlantılar için kullanılıyorsa, '4' ve '6' tek bir adreste birleştirilebilir.

6: Giden IPv6 yeteneğini belirtir. Host alanında bir IP yayınlanmışsa, bu yetenek gerekli değildir. Router gizliyse veya NTCP2 yalnızca giden bağlantı içinse, '4' ve '6' tek bir adreste birleştirilebilir.

### Yayınlanan Adresler

Yayınlanan RouterAddress (RouterInfo'nun bir parçası) "NTCP" veya "NTCP2" protokol tanımlayıcısına sahip olacaktır.

RouterAddress, mevcut NTCP protokolünde olduğu gibi "host" ve "port" seçeneklerini içermelidir.

RouterAddress, NTCP2 desteğini belirtmek için üç seçenek içermelidir:

- s=(Base64 anahtar) Bu RouterAddress için mevcut Noise statik public key (s). Standart I2P Base 64 alfabesi kullanılarak Base 64 kodlanmıştır. İkili formatta 32 bayt, Base 64 kodlanmış olarak 44 bayt, little-endian X25519 public key.
- i=(Base64 IV) Bu RouterAddress için mesaj 1'deki X değerini şifrelemek için mevcut IV. Standart I2P Base 64 alfabesi kullanılarak Base 64 kodlanmıştır. İkili formatta 16 bayt, Base 64 kodlanmış olarak 24 bayt, big-endian.
- v=2 Mevcut versiyon (2). "NTCP" olarak yayınlandığında, versiyon 1 için ek destek ima edilir. Gelecekteki versiyonlar için destek virgülle ayrılmış değerlerle olacaktır, örn. v=2,3 Uygulama, virgül mevcutsa birden fazla versiyon dahil olmak üzere uyumluluğu doğrulamalıdır. Virgülle ayrılmış versiyonlar sayısal sırada olmalıdır.

Alice, NTCP2 protokolünü kullanarak bağlanmadan önce her üç seçeneğin de mevcut ve geçerli olduğunu doğrulamalıdır.

"s", "i" ve "v" seçenekleriyle "NTCP" olarak yayınlandığında, router o host ve port üzerinde hem NTCP hem de NTCP2 protokolleri için gelen bağlantıları kabul etmeli ve protokol sürümünü otomatik olarak algılamalıdır.

"s", "i" ve "v" seçenekleri ile "NTCP2" olarak yayınlandığında, router o host ve port üzerinde sadece NTCP2 protokolü için gelen bağlantıları kabul eder.

Bir router hem NTCP1 hem de NTCP2 bağlantılarını destekliyorsa ancak gelen bağlantılar için otomatik sürüm algılaması uygulamıyorsa, hem "NTCP" hem de "NTCP2" adreslerini duyurmalı ve NTCP2 seçeneklerini yalnızca "NTCP2" adresine dahil etmelidir. Router, NTCP2'nin tercih edilmesi için "NTCP2" adresinde "NTCP" adresinden daha düşük bir maliyet değeri (daha yüksek öncelik) ayarlamalıdır.

Aynı RouterInfo içinde birden fazla NTCP2 RouterAddress ("NTCP" veya "NTCP2" olarak) yayınlanırsa (ek IP adresleri veya portlar için), aynı portu belirten tüm adresler özdeş NTCP2 seçenekleri ve değerleri içermelidir. Özellikle, hepsi aynı statik anahtar ve iv içermelidir.

### Yayınlanmamış NTCP2 Adresi

Eğer Alice gelen bağlantılar için NTCP2 adresini ("NTCP" veya "NTCP2" olarak) yayınlamazsa, Bob'un mesaj 3 bölüm 2'de Alice'in RouterInfo'sunu aldıktan sonra anahtarı doğrulayabilmesi için yalnızca statik anahtarını ve NTCP2 sürümünü içeren bir "NTCP2" router adresi yayınlamalıdır.

- s=(Base64 anahtar) Yayınlanan adresler için yukarıda tanımlandığı gibi.
- v=2 Yayınlanan adresler için yukarıda tanımlandığı gibi.

Bu router adresi "i", "host" veya "port" seçeneklerini içermeyecektir, çünkü bunlar giden NTCP2 bağlantıları için gerekli değildir. Bu adres için yayınlanan maliyet kesinlikle önemli değildir, çünkü sadece gelen bağlantılar içindir; ancak maliyet diğer adreslerden daha yüksek (daha düşük öncelik) ayarlanırsa diğer router'lar için yararlı olabilir. Önerilen değer 14'tür.

Alice ayrıca mevcut yayınlanmış bir "NTCP" adresine basitçe "s" ve "v" seçeneklerini ekleyebilir.

### Genel Anahtar ve IV Rotasyonu

RouterInfo'ların önbelleğe alınması nedeniyle, router'lar yayınlanmış bir adreste olsun veya olmasın, router çalışır durumdayken statik genel anahtarı veya IV'yi değiştirmemelidir. Router'lar bu anahtar ve IV'yi hemen yeniden başlatma sonrasında tekrar kullanmak üzere kalıcı olarak depolamalıdır, böylece gelen bağlantılar çalışmaya devam edecek ve yeniden başlatma süreleri açığa çıkmayacaktır. Router'lar son kapanma zamanını kalıcı olarak depolamalı veya başka bir şekilde belirlemelidir, böylece bir önceki çalışmama süresi başlangıçta hesaplanabilir.

Yeniden başlatma zamanlarını açığa çıkarma endişeleri göz önünde bulundurularak, router'lar daha önce bir süre (en az birkaç saat) kapalı kalmışlarsa başlangıçta bu anahtarı veya IV'yi değiştirebilirler.

Router'ın yayınlanmış herhangi bir NTCP2 RouterAddress'i varsa (NTCP veya NTCP2 olarak), yerel IP adresi değişmedikçe veya router "rekey" yapmadıkça, rotasyondan önceki minimum kesinti süresi çok daha uzun olmalıdır, örneğin bir ay.

Eğer router yayınlanmış SSU RouterAddresses'lere sahipse ancak NTCP2'ye (NTCP veya NTCP2 olarak) sahip değilse, rotasyon öncesi minimum kesinti süresi daha uzun olmalıdır, örneğin bir gün, yerel IP adresi değişmediği veya router "rekey" yapmadığı sürece. Bu, yayınlanmış SSU adresinin introducer'lara sahip olması durumunda bile geçerlidir.

Eğer router herhangi bir yayınlanmış RouterAddress'e (NTCP, NTCP2 veya SSU) sahip değilse, router "rekey" yapmadığı sürece, IP adresi değişse bile döndürme öncesi minimum kesinti süresi iki saat kadar kısa olabilir.

Router farklı bir Router Hash'e "rekey" yaparsa, yeni bir noise anahtarı ve IV de oluşturmalıdır.

Uygulamalar, statik genel anahtarı veya IV'yi değiştirmenin, eski bir RouterInfo önbelleğe almış router'lardan gelen NTCP2 bağlantılarını engelleyeceğinin farkında olmalıdır. RouterInfo yayınlama, tunnel eş seçimi (hem OBGW hem de IB en yakın hop dahil), sıfır-hop tunnel seçimi, transport seçimi ve diğer uygulama stratejileri bunu hesaba katmalıdır.

IV rotasyonu, anahtar rotasyonuyla aynı kurallara tabidir, ancak IV'ler yalnızca yayınlanmış RouterAddress'lerde bulunur, dolayısıyla gizli veya güvenlik duvarı arkasındaki router'lar için IV yoktur. Herhangi bir şey değişirse (sürüm, anahtar, seçenekler?) IV'nin de değişmesi önerilir.

Not: Yeniden anahtarlama öncesindeki minimum kesinti süresi, ağ sağlığını sağlamak ve orta düzeyde bir süre çevrimdışı olan bir router'ın yeniden tohumlama yapmasını önlemek için değiştirilebilir.

## Sürüm Tespiti

"NTCP" olarak yayınlandığında, router gelen bağlantılar için protokol sürümünü otomatik olarak algılamalıdır.

Bu tespit uygulama-bağımlıdır, ancak burada bazı genel rehberlik bulunmaktadır.

Gelen bir NTCP bağlantısının sürümünü tespit etmek için Bob şu adımları izler:

- En az 64 bayt bekle (minimum NTCP2 mesaj 1 boyutu)

- Eğer alınan ilk veri 288 veya daha fazla bayt ise, gelen bağlantı sürüm 1'dir.

- 288 bayttan azsa, ya

> - Daha fazla veri için kısa bir süre bekle (yaygın NTCP2 benimsenmesinden önceki iyi strateji) eğer en az 288 toplam alındıysa, bu NTCP 1'dir.   >   > - Sürüm 2 olarak kod çözmenin ilk aşamalarını dene, eğer başarısız olursa, daha fazla veri için kısa bir süre bekle (yaygın NTCP2 benimsenmesinden sonraki iyi strateji)   >   >   > - SessionRequest paketinin ilk 32 baytını (X anahtarı) RH_B anahtarıyla AES-256 kullanarak şifrele.   >   > - Eğri üzerinde geçerli bir nokta doğrula. Eğer başarısız olursa, NTCP 1 için daha fazla veri için kısa bir süre bekle   >   > - AEAD çerçevesini doğrula. Eğer başarısız olursa, NTCP 1 için daha fazla veri için kısa bir süre bekle

NTCP 1 üzerinde aktif TCP segmentasyon saldırıları tespit edersek değişiklikler veya ek stratejiler önerilmeyebilir.

Hızlı sürüm tespiti ve handshake işlemini kolaylaştırmak için, uygulamalar Alice'in ilk mesajın tüm içeriğini (padding dahil) arabelleğe almasını ve ardından tek seferde boşaltmasını sağlamalıdır. Bu, verilerin (işletim sistemi veya middlebox'lar tarafından parçalanmadığı sürece) tek bir TCP paketi içinde bulunması ve Bob tarafından tek seferde alınması olasılığını artırır. Bu aynı zamanda verimlilik için ve rastgele padding'in etkinliğini sağlamak içindir. Bu kural hem NTCP hem de NTCP2 handshake'leri için geçerlidir.

## Varyantlar, Yedek Seçenekler ve Genel Sorunlar

- Alice ve Bob'un ikisi de NTCP2'yi destekliyorsa, Alice NTCP2 ile bağlanmalıdır.
- Alice herhangi bir nedenle NTCP2 kullanarak Bob'a bağlanamayacak olursa, bağlantı başarısız olur. Alice NTCP 1 kullanarak yeniden deneyemez.

## Saat Kayması Yönergeleri

Peer zaman damgaları ilk iki handshake mesajında bulunur: Session Request ve Session Created. İki peer arasında +/- 60 saniyeden fazla bir saat sapması genellikle öldürücüdür. Bob yerel saatinin kötü olduğunu düşünüyorsa, hesaplanan sapma veya bazı dış kaynakları kullanarak saatini ayarlayabilir. Aksi takdirde, Bob maksimum sapma aşılsa bile bağlantıyı kapatmak yerine Session Created ile yanıt vermelidir. Bu Alice'in Bob'un zaman damgasını almasına ve sapmayı hesaplayıp gerekirse harekete geçmesine olanak tanır. Bob bu noktada Alice'in router kimliğine sahip değildir, ancak kaynakları korumak için Bob'un Alice'in IP'sinden gelen bağlantıları belirli bir süre boyunca yasaklaması veya aşırı sapma ile tekrarlanan bağlantı girişimlerinden sonra yasaklaması arzu edilebilir.

Alice, hesaplanan saat sapmasını RTT'nin yarısını çıkararak düzeltmelidir. Alice yerel saatinin kötü olduğunu düşünüyorsa, hesaplanan sapma veya harici bir kaynak kullanarak saatini ayarlayabilir. Alice, Bob'un saatinin kötü olduğunu düşünüyorsa, Bob'u belirli bir süre için yasaklayabilir. Her iki durumda da Alice bağlantıyı kapatmalıdır.

Eğer Alice Session Confirmed ile yanıt verirse (muhtemelen çarpıklık 60s sınırına çok yakın olduğu için ve RTT nedeniyle Alice ve Bob hesaplamaları tam olarak aynı olmadığı için), Bob hesaplanan saat çarpıklığını RTT'nin yarısını çıkararak ayarlamalıdır. Ayarlanan saat çarpıklığı maksimumu aşarsa, Bob daha sonra saat çarpıklığı sebep kodunu içeren bir Disconnect mesajı ile yanıt vermeli ve bağlantıyı kapatmalıdır. Bu noktada, Bob Alice'in router kimliğine sahiptir ve Alice'i belirli bir süre için yasaklayabilir.

## Referanslar

- [Ortak Yapılar](/docs/specs/common-structures)
- [I2NP](/docs/specs/i2np)
- [Network Database](/docs/overview/network-database)
- [NOISE - Noise Protocol Framework](https://noiseprotocol.org/noise.html)
- [NTCP](/docs/transport/ntcp)
- [Prop104](/proposals/104-tls-transport)
- [Prop109](/proposals/109-pt-transport)
- [Prop111](/proposals/111-ntcp-2)
- [RFC-2104 - HMAC](https://tools.ietf.org/html/rfc2104)
- [RFC-3526 - DH Groups](https://tools.ietf.org/html/rfc3526)
- [RFC-6151](https://tools.ietf.org/html/rfc6151)
- [RFC-7539 - ChaCha20-Poly1305](https://tools.ietf.org/html/rfc7539)
- [RFC-7748 - X25519](https://tools.ietf.org/html/rfc7748)
- [RFC-7905](https://tools.ietf.org/html/rfc7905)
- [SipHash](https://www.131002.net/siphash/)
- [SSU](/docs/transport/ssu)
- **[STS]** Diffie, W.; van Oorschot P. C.; Wiener M. J., Kimlik Doğrulama ve Kimlik Doğrulamalı Anahtar Değişimleri
