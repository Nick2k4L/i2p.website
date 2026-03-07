---
title: "SSU2 Spesifikasyonu"
description: "Güvenli Yarı-Güvenilir UDP Taşıma Protokolü Sürüm 2"
slug: "ssu2"
category: "Taşıyıcılar"
lastUpdated: "2026-03"
accurateFor: "0.9.69"
---

## Durum

Büyük ölçüde tamamlandı. Ek bilgi ve hedefler için [Prop159](/proposals/159-ssu2) bağlantısına bakın; bu bağlantı güvenlik analizi, tehdit modelleri, SSU 1 güvenlik incelemesi ve sorunları ile QUIC spesifikasyonlarından alıntıları içerir.

Dağıtım planı:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Feature</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Testing (not default)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Enabled by default</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Local test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-03</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test in-net</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze basic protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Basic Session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address Validation (Retry)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Fragmented RI in handshake</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze extended protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Enable for random 2%</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Validation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Connection Migration</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Immediate ACK flag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Key Rotation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2023-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (i2pd)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (Java I2P)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.61 2023-12</td></tr>
  </tbody>
</table>
Temel Oturum el sıkışma ve veri aşamasını içerir. Genişletilmiş protokol relay ve eş testi içerir.

## Genel Bakış

Bu spesifikasyon, [SSU](/docs/transport/ssu)'nun çeşitli otomatik tanımlama ve saldırı biçimlerine karşı direncini artırmak için kimlik doğrulamalı bir anahtar anlaşma protokolü tanımlar.

Diğer I2P taşıma protokolleri gibi, SSU2 de I2NP mesajlarının noktadan noktaya (router'dan router'a) taşınması için tanımlanmıştır. Genel amaçlı bir veri kanalı değildir. [SSU](/docs/transport/ssu) gibi, iki ek hizmet de sağlar: NAT geçişi için Relaying (röle) ve gelen bağlantı erişilebilirliğinin belirlenmesi için Peer Testing (eş testi). Ayrıca SSU'da bulunmayan üçüncü bir hizmet daha sağlar; bir eş IP veya port değiştirdiğinde bağlantı geçişi için.

## Tasarım Genel Bakış

### Özet

Hem I2P içindeki hem de dış standartlardaki mevcut birkaç protokole ilham, rehberlik ve kod yeniden kullanımı için güveniyoruz:

- Tehdit modelleri: NTCP2 [NTCP2](/docs/specs/ntcp2)'den, QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001) tarafından analiz edilen UDP taşıma katmanıyla ilgili önemli ek tehditlerle birlikte.
- Kriptografik seçimler: [NTCP2](/docs/specs/ntcp2)'den.
- El sıkışma: [NTCP2](/docs/specs/ntcp2) ve [NOISE](https://noiseprotocol.org/noise.html)'dan Noise XK. UDP tarafından sağlanan kapsülleme (doğal mesaj sınırları) nedeniyle NTCP2'de önemli basitleştirmeler mümkündür.
- El sıkışma geçici anahtar gizleme: [NTCP2](/docs/specs/ntcp2)'den uyarlanmış ancak AES yerine [ECIES](/docs/specs/ecies)'den ChaCha20 kullanarak.
- Paket başlıkları: WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) ve QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001)'den uyarlanmış.
- Paket başlığı gizleme: [NTCP2](/docs/specs/ntcp2)'den uyarlanmış ancak AES yerine [ECIES](/docs/specs/ecies)'den ChaCha20 kullanarak.
- Paket başlığı koruması: QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) ve [Nonces](https://eprint.iacr.org/2019/624.pdf)'dan uyarlanmış
- [ECIES](/docs/specs/ecies)'deki gibi AEAD ilişkili veri olarak kullanılan başlıklar.
- Paket numaralandırma: WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) ve QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001)'den uyarlanmış.
- Mesajlar: [SSU](/docs/transport/ssu)'dan uyarlanmış
- I2NP Parçalama: [SSU](/docs/transport/ssu)'dan uyarlanmış
- Röle ve Eş Testi: [SSU](/docs/transport/ssu)'dan uyarlanmış
- Röle ve Eş Test verilerinin İmzaları: Ortak yapılar spesifikasyonundan [Common](/docs/specs/common-structures)
- Blok formatı: [NTCP2](/docs/specs/ntcp2) ve [ECIES](/docs/specs/ecies)'den.
- Dolgu ve seçenekler: [NTCP2](/docs/specs/ntcp2) ve [ECIES](/docs/specs/ecies)'den.
- Onaylar, ret onayları: QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000)'den uyarlanmış.
- Akış kontrolü: Henüz belirlenmedi

I2P'de daha önce kullanılmamış yeni bir kriptografik temel işlem bulunmamaktadır.

### Teslimat Garantileri

Diğer I2P transport'ları NTCP, NTCP2 ve SSU 1'de olduğu gibi, bu transport da sıralı bayt akışının teslimi için genel amaçlı bir tesis değildir. I2NP mesajlarının transport'u için tasarlanmıştır. Herhangi bir "stream" soyutlaması sağlanmaz.

Bunlara ek olarak, SSU için olduğu gibi, eş-destekli NAT geçişi ve erişilebilirlik testi (gelen bağlantılar) için ek olanaklar içerir.

SSU 1 için, I2NP mesajlarının sıralı teslimatını SAĞLAMAZ. Ayrıca I2NP mesajlarının garantili teslimatını da sağlamaz. Verimlilik nedeniyle veya UDP datagramlarının sırasız teslimatı ya da bu datagramların kaybı yüzünden, I2NP mesajları karşı tarafa sırasız teslim edilebilir veya hiç teslim edilmeyebilir. Gerekirse bir I2NP mesajı birden çok kez yeniden iletilebilir, ancak tam bağlantının kesilmesine neden olmadan teslimat sonunda başarısız olabilir. Ayrıca, diğer I2NP mesajları için yeniden iletim (kayıp kurtarma) gerçekleşirken bile yeni I2NP mesajları gönderilmeye devam edebilir.

Bu protokol I2NP mesajlarının yinelenen teslimatını tamamen engellemez. Router, I2NP süre sonunu zorlamalı ve I2NP mesaj kimliğine dayanan bir Bloom filtresi veya başka bir mekanizma kullanmalıdır. Aşağıdaki I2NP Mesaj Çoğaltma bölümüne bakın.

### Noise Protocol Framework

Bu spesifikasyon, Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (Revizyon 33, 2017-10-04) temelinde gereksinimleri sağlar. Noise, [SSU](/docs/transport/ssu) protokolünün temelini oluşturan Station-To-Station protokolü [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol) ile benzer özelliklere sahiptir. Noise terminolojisinde Alice başlatıcı (initiator), Bob ise yanıtlayıcıdır (responder).

SSU2, Noise protokolü Noise_XK_25519_ChaChaPoly_SHA256'ya dayanmaktadır. (İlk anahtar türetme fonksiyonu için gerçek tanımlayıcı, I2P uzantılarını belirtmek üzere "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256"dır - aşağıdaki KDF 1 bölümüne bakın)

NOT: Bu tanımlayıcı NTCP2 için kullanılandan farklıdır, çünkü her üç handshake mesajı da başlığı ilişkili veri olarak kullanır.

Bu Noise protokolü aşağıdaki temel bileşenleri kullanır:

- Handshake Deseni: XK Alice anahtarını Bob'a iletir (X) Alice zaten Bob'un statik anahtarını bilir (K)
- DH Fonksiyonu: X25519 [RFC-7748](https://tools.ietf.org/html/rfc7748)'de belirtildiği gibi 32 bayt anahtar uzunluğuna sahip X25519 DH.
- Şifreleme Fonksiyonu: ChaChaPoly [RFC-7539](https://tools.ietf.org/html/rfc7539) bölüm 2.8'de belirtildiği gibi AEAD_CHACHA20_POLY1305. 12 bayt nonce, ilk 4 bayt sıfıra ayarlanmış.
- Hash Fonksiyonu: SHA256 I2P'de zaten yaygın olarak kullanılan standart 32 bayt hash.

### Framework'e Eklemeler

Bu spesifikasyon, Noise_XK_25519_ChaChaPoly_SHA256'ya aşağıdaki geliştirmeleri tanımlar. Bunlar genellikle [NOISE](https://noiseprotocol.org/noise.html) bölüm 13'teki yönergeleri takip eder.

1) Handshake mesajları (Session Request, Created, Confirmed) 16 veya 32 baytlık bir başlık içerir. 2) Handshake mesajlarının başlıkları (Session Request, Created, Confirmed) şifreleme/şifre çözme öncesinde başlıkları mesaja bağlamak için mixHash() fonksiyonuna girdi olarak kullanılır. 3) Başlıklar şifrelenir ve korunur. 4) Açık metin ephemeral anahtarlar bilinen bir anahtar ve IV kullanarak ChaCha20 şifrelemesi ile gizlenir. Bu elligator2'den daha hızlıdır. 5) Payload formatı mesaj 1, 2 ve veri aşaması için tanımlanmıştır. Tabii ki bu Noise'da tanımlanmamıştır.

Veri aşaması, Noise veri aşamasına benzer ancak onunla uyumlu olmayan şifreleme kullanır.

### Oturum Kurulumu

Kullanılan kriptografik yapı taşlarına karşılık gelen aşağıdaki fonksiyonları tanımlıyoruz.

#### Uzun Başlık

ZEROLEN

#### Kısa Başlık

:   sıfır uzunlukta bayt dizisi

#### Bağlantı ID Numaralandırması

H(p, d)

#### Paket Numaralandırma

:   Bir kişiselleştirme dizesi p ve veri d alan ve 32 bayt uzunluğunda çıktı üreten SHA-256 hash fonksiyonu. [NOISE](https://noiseprotocol.org/noise.html) içinde tanımlandığı şekilde. Aşağıdaki || ekleme anlamına gelir.

## Tanımlar

MixHash(d)

:   Önceki hash h ve yeni veri d'yi alan ve 32 byte uzunluğunda çıktı üreten SHA-256 hash fonksiyonu. Aşağıdaki || ekleme anlamına gelir.

STREAM

:   [RFC-7539](https://tools.ietf.org/html/rfc7539)'da belirtilen ChaCha20/Poly1305 AEAD. S_KEY_LEN = 32 ve S_IV_LEN = 12.

DH

    Use SHA-256 as follows:

        H(p, d) := SHA-256(p || d)

:   X25519 açık anahtar anlaşma sistemi. 32 baytlık özel anahtarlar, 32 baytlık açık anahtarlar, 32 baytlık çıktılar üretir. Aşağıdaki işlevlere sahiptir:

HKDF(salt, ikm, info, n)

    Use SHA-256 as follows:

        MixHash(d) := h = SHA-256(h || d)

:   Bir kriptografik anahtar türetme fonksiyonu; iyi entropi içermesi gereken ancak düzgün rastgele bir dize olması gerekmeyen giriş anahtar malzemesi ikm'yi, 32 bayt uzunluğunda bir tuz değerini ve bağlam-özel bir 'info' değerini alarak, anahtar malzemesi olarak kullanıma uygun n bayt çıktısı üretir.

MixKey(d)

    ENCRYPT(k, n, plaintext, ad)

    :   Encrypts plaintext using the cipher key k, and nonce n which MUST be unique for the key k. Associated data ad is optional. Returns a ciphertext that is the size of the plaintext + 16 bytes for the HMAC.

        The entire ciphertext must be indistinguishable from random if the key is secret.

    DECRYPT(k, n, ciphertext, ad)

    :   Decrypts ciphertext using the cipher key k, and nonce n. Associated data ad is optional. Returns the plaintext.

:   Önceki chainKey ve yeni veri d ile HKDF() kullanır, ve yeni chainKey ile k'yi ayarlar. [NOISE](https://noiseprotocol.org/noise.html)'da tanımlandığı gibi.

Her UDP datagramı tam olarak bir mesaj içerir. Datagramın uzunluğu (IP ve UDP başlıklarından sonra) mesajın uzunluğudur. Varsa dolgu, mesajın içindeki bir dolgu bloğunda bulunur. Bu belgede, "datagram" ve "paket" terimlerini çoğunlukla birbirinin yerine kullanıyoruz. Her datagram (veya paket) tek bir mesaj içerir (QUIC'den farklı olarak, burada bir datagram birden fazla QUIC paketi içerebilir). "Paket başlığı" IP/UDP başlığından sonraki kısımdır.

    GENERATE_PRIVATE()

    :   Generates a new private key.

    DERIVE_PUBLIC(privkey)

    :   Returns the public key corresponding to the given private key.

    DH(privkey, pubkey)

    :   Generates a shared secret from the given private and public keys.

İstisna: Session Confirmed mesajı, birden fazla paket arasında parçalanabileceği için benzersizdir. Daha fazla bilgi için aşağıdaki Session Confirmed Fragmentation bölümüne bakın.

Tüm SSU2 mesajları en az 40 bayt uzunluğundadır. 1-39 bayt uzunluğundaki herhangi bir mesaj geçersizdir. Tüm SSU2 mesajları 1472 (IPv4) veya 1452 (IPv6) bayttan küçük veya eşit uzunluktadır. Mesaj formatı Noise mesajlarına dayanır, çerçeveleme ve ayırt edilemezlik için değişikliklerle. Standart Noise kütüphanelerini kullanan uygulamalar, alınan mesajları standart Noise mesaj formatına önceden işlemelidir. Tüm şifreli alanlar AEAD şifre metinleridir.

    Use HKDF as specified in [RFC-5869](https://tools.ietf.org/html/rfc5869), using the HMAC hash function SHA-256 as specified in [RFC-2104](https://tools.ietf.org/html/rfc2104). This means that SALT_LEN is 32 bytes max.

Aşağıdaki mesajlar tanımlanmıştır:

Alice'in Bob'dan daha önce aldığı geçerli bir token'a sahip olduğu durumda standart kuruluş sırası şu şekildedir:

    Use HKDF as follows:

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]

## Mesajlar

Alice geçerli bir token'a sahip olmadığında, kurulum sırası şu şekildedir:

Alice geçerli bir token'a sahip olduğunu düşündüğünde, ancak Bob bunu reddettiğinde (belki Bob yeniden başlatıldığı için), kurulum sırası şu şekildedir:

Bob, bir neden kodu içeren Termination bloğu bulunan bir Retry mesajı ile yanıtlayarak Session veya Token Request'i reddedebilir. Neden koduna dayanarak, Alice belirli bir süre boyunca başka bir istek girişiminde bulunmamalıdır:

Noise terminolojisi kullanılarak, kurulum ve veri sırası şu şekildedir: (Payload Güvenlik Özellikleri)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Encr. Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionRequest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionCreated</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionConfirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">PeerTest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">HolePunch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
  </tbody>
</table>
### Paket Başlığı

Bir oturum kurulduktan sonra, Alice ve Bob Data mesajları alışverişinde bulunabilir.

```
Alice                           Bob

SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Tüm paketler gizlenmiş (şifrelenmiş) bir başlık ile başlar. Uzun ve kısa olmak üzere iki başlık türü vardır. İlk 13 baytın (Hedef Bağlantı Kimliği, paket numarası ve tür) tüm başlıklar için aynı olduğunu unutmayın.

```
Alice                           Bob

TokenRequest --------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Uzun başlık 32 bayttır. Bir oturum oluşturulmadan önce Token Request, SessionRequest, SessionCreated ve Retry için kullanılır. Ayrıca oturum-dışı Peer Test ve Hole Punch mesajları için de kullanılır.

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Header şifrelemesinden önce:

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry containing a Termination block

or

TokenRequest --------------------->
<---------------------------  Retry containing a Termination block
```
Kısa başlık 16 bayttır. Session Created ve Data mesajları için kullanılır. Session Request, Retry ve Peer Test gibi kimlik doğrulaması olmayan mesajlar her zaman uzun başlığı kullanacaktır.

```
XK(s, rs):           Authentication   Confidentiality
  <- s
  ...
  -> e, es                  0                2
  <- e, ee                  2                1
  -> s, se                  2                5
  <-                        2                5
```
16 bayt gereklidir, çünkü alıcının mesaj türünü elde etmek için ilk 16 baytı şifrelemesini çözmesi gerekir ve mesaj türünün belirttiği üzere gerçekten uzun bir başlık ise ek 16 bayt daha şifrelemesini çözmesi gerekir.

### Paket Bütünlüğü

Session Confirmed için, header şifrelenmesinden önce:

#### Header Bağlama

frag alanı hakkında daha fazla bilgi için aşağıdaki Session Confirmed Fragmentation bölümüne bakınız.

Veri mesajları için, başlık şifrelemesinden önce:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 0, 1, 7, 9, 10, or 11

ver :: The protocol version, equal to 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: 8 bytes, unsigned big endian integer

Token :: 8 bytes, unsigned big endian integer
```
#### Başlık Şifreleme

Connection ID'leri rastgele oluşturulmalıdır. Kaynak ve Hedef ID'leri aynı OLMAMALIDIR, böylece yol üzerindeki bir saldırgan geçerli görünen bir paketi yakalayıp gönderene geri gönderemez. Connection ID'leri oluşturmak için sayaç KULLANMAYIN, böylece yol üzerindeki bir saldırgan geçerli görünen bir paket oluşturamaz.

QUIC'ten farklı olarak, handshake sırasında veya sonrasında, hatta bir Retry mesajından sonra bile bağlantı ID'lerini değiştirmeyiz. ID'ler ilk mesajdan (Token Request veya Session Request) son mesaja (Termination ile Data) kadar sabit kalır. Ek olarak, bağlantı ID'leri path challenge veya bağlantı geçişi sırasında veya sonrasında değişmez.

Ayrıca QUIC'den farklı olarak, başlıklardaki bağlantı ID'leri her zaman başlık-şifrelidir. Aşağıya bakın.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, all zeros

type :: The message type = 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility
```
Handshake sırasında First Packet Number bloğu gönderilmezse, paketler tek bir oturum içinde, her yön için 0'dan başlayarak maksimum (2**32 -1) değerine kadar numaralandırılır. Maksimum paket sayısı gönderilmeden çok önce oturum sonlandırılmalı ve yeni bir oturum oluşturulmalıdır.

Eğer handshake sırasında bir İlk Paket Numarası bloğu gönderilirse, paketler tek bir oturum içinde, o yön için, o paket numarasından başlayarak numaralandırılır. Paket numarası oturum sırasında döngüye girebilir. 2**32 maksimum paket gönderildiğinde, paket numarası ilk paket numarasına geri dönerek, o oturum artık geçerli değildir. Maksimum paket sayısı gönderilmeden çok önce oturum sonlandırılmalı ve yeni bir oturum oluşturulmalıdır.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|flag|moreflags|
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 6

flag :: 1 byte flags:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-1: unused, set to 0 for future compatibility
       bits 0: when set to 1, immediate ack requested

moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### Header Şifreleme KDF'si

TODO anahtar rotasyonu, maksimum paket sayısını azalt?

Kayıp olduğu belirlenen handshake paketleri, paket numarası dahil olmak üzere özdeş başlık ile bütün olarak yeniden iletilir. Session Request, Session Created ve Session Confirmed handshake mesajları, aynı paket numarası ve özdeş şifreli içeriklerle yeniden iletilmelidir, böylece yanıtı şifrelemek için aynı zincirleme hash kullanılacaktır. Retry mesajı asla iletilmez.

Kaybolduğu belirlenen veri fazı paketleri hiçbir zaman bütün olarak yeniden iletilmez (sonlandırma hariç, aşağıya bakın). Aynı durum kayıp paketler içinde bulunan bloklar için de geçerlidir. Bunun yerine, bloklarda taşınabilecek bilgiler gerektiğinde yeni paketlerde tekrar gönderilir. Veri Paketleri hiçbir zaman aynı paket numarasıyla yeniden iletilmez. Paket içeriğinin herhangi bir yeniden iletimi (içerik aynı kalsa da kalmasada) bir sonraki kullanılmamış paket numarasını kullanmalıdır.

#### Başlık Doğrulama

Aynı paket numarasıyla değiştirilmemiş bir paketin olduğu gibi yeniden iletilmesi, çeşitli nedenlerle izin verilmez. Arka plan bilgisi için QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) bölüm 12.3'e bakın.

Yeni paketler, kaybolduğu belirlenen bilgileri taşımak için kullanılır. Genel olarak, bu bilgileri içeren bir paketin kaybolduğu belirlendiğinde bilgi tekrar gönderilir ve bu bilgileri içeren bir paket onaylandığında gönderim durdurulur.

İstisna: Bir Sonlandırma bloğu içeren veri fazı paketi, olduğu gibi bütünüyle yeniden iletilebilir, ancak bu zorunlu değildir. Aşağıdaki Oturum Sonlandırma bölümüne bakın.

Aşağıdaki paketler göz ardı edilen rastgele bir paket numarası içerir:

Alice için, giden paket numaralandırması Session Confirmed ile 0'dan başlar. Bob için, giden paket numaralandırması ilk Data paketi ile 0'dan başlar ve bu paket Session Confirmed'ın bir ACK'si olmalıdır. Örnek standart el sıkışmadaki paket numaraları şöyle olacaktır:

Herhangi bir handshake mesajının (SessionRequest, SessionCreated veya SessionConfirmed) yeniden iletimi, aynı paket numarası ile değiştirilmeden yeniden gönderilmelidir. Bu mesajları yeniden iletirken farklı geçici anahtarlar kullanmayın veya payload'ı değiştirmeyin.

- Yeniden iletim için paketleri saklamak verimsizdir
- Yeni bir paket verisi, yol üzerindeki bir gözlemci için farklı görünür, yeniden iletildiği anlaşılamaz
- Yeni bir paket, eski ack bloğu değil, güncellenmiş bir ack bloğu ile birlikte gönderilir
- Yalnızca gerekli olanı yeniden iletirsiniz. bazı parçalar zaten bir kez yeniden iletilmiş ve ack alınmış olabilir
- Daha fazlası bekliyorsa, yeniden iletilen her pakete ihtiyacınız kadar çok şey sığdırabilirsiniz
- Duplikatları tespit etmek amacıyla tüm bireysel paketleri izleyen endpoint'ler, aşırı durum biriktirme riski altındadır. Duplikatları tespit etmek için gereken veriler, altındaki tüm paketlerin hemen bırakıldığı minimum bir paket numarası tutarak sınırlandırılabilir.
- Bu şema çok daha esnektir

Başlık (gizleme ve koruma öncesi), AEAD fonksiyonu için ilişkili verilere her zaman dahil edilir ve başlığı verilere kriptografik olarak bağlamak için kullanılır.

Header şifrelemenin birkaç amacı vardır. Arka plan ve varsayımlar için yukarıdaki "Ek DPI Tartışması" bölümüne bakın.

Başlıklar, network database'de yayınlanan bilinen anahtarlar veya daha sonra hesaplanan anahtarlarla şifrelenir. Handshake aşamasında, bu yalnızca DPI direnci içindir, çünkü anahtar herkese açıktır ve anahtar ile nonce'ler yeniden kullanılır, bu nedenle etkili olarak sadece gizlemedir. Başlık şifrelemesinin aynı zamanda ephemeral anahtarları X'i (Session Request'te) ve Y'yi (Session Created'da) gizlemek için de kullanıldığını unutmayın.

- Oturum İsteği
- Oturum Oluşturuldu
- Token İsteği
- Yeniden Deneme
- Eş Testi
- Hole Punch

Ek rehberlik için aşağıdaki Gelen Paket İşleme bölümüne bakın.

```
Alice                           Bob

SessionRequest (r)    ------------>
<-------------   SessionCreated (r)
SessionConfirmed (0)  ------------>
<-------------             Data (0) (Ack-only)
Data (1)              ------------> (May be sent before Ack is received)
<-------------             Data (1)
Data (2)              ------------>
Data (3)              ------------>
Data (4)              ------------>
<-------------             Data (2)

r = random packet number (ignored)
Token Request, Retry, and Peer Test
also have random packet numbers.
```
Tüm başlıkların 0-15 baytları, QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) ve [Nonces](https://eprint.iacr.org/2019/624.pdf)'a benzer şekilde ChaCha20 kullanarak bilinen anahtarlardan hesaplanan verilerle XOR yapılarak bir başlık koruma şeması kullanılarak şifrelenir. Bu, şifrelenmiş kısa başlığın ve uzun başlığın ilk bölümünün rastgele görünmesini sağlar.

#### ChaCha20/Poly1305

Session Request ve Session Created için, uzun başlığın 16-31 baytları ve 32-baytlık Noise geçici anahtarı ChaCha20 kullanılarak şifrelenir. Şifrelenmemiş veri rastgeledir, bu nedenle şifrelenmiş veri rastgele görünecektir.

#### Notlar

Retry için, uzun başlığın 16-31 baytları ChaCha20 kullanılarak şifrelenir. Şifrelenmemiş veri rastgeledir, dolayısıyla şifrelenmiş veri de rastgele görünecektir.

- Çevrimiçi DPI'nin protokolü tanımlamasını engellemek
- Handshake yeniden iletimler hariç, aynı bağlantıdaki bir dizi mesajda kalıpları engellemek
- Farklı bağlantılardaki aynı türdeki mesajlarda kalıpları engellemek
- netDb'de bulunan introduction key bilgisi olmadan handshake başlıklarının şifresinin çözülmesini engellemek
- netDb'de bulunan introduction key bilgisi olmadan X25519 geçici anahtarlarının tanımlanmasını engellemek
- Herhangi bir çevrimiçi veya çevrimdışı saldırgan tarafından veri fazı paket numarası ve türünün şifresinin çözülmesini engellemek
- netDb'de bulunan introduction key bilgisi olmadan yol üzerindeki veya yol dışındaki gözlemci tarafından geçerli handshake paketlerinin enjekte edilmesini engellemek
- Yol üzerindeki veya yol dışındaki gözlemci tarafından geçerli veri paketlerinin enjekte edilmesini engellemek
- Gelen paketlerin hızlı ve verimli sınıflandırılmasına izin vermek
- Kötü bir Session Request'e yanıt verilmemesi veya Retry yanıtı varsa, netDb'de bulunan introduction key bilgisi olmadan yanıtın I2P olarak tanımlanamayacağı şekilde "probing" direncini sağlamak
- Destination Connection ID kritik veri değildir ve netDb'de bulunan introduction key bilgisine sahip bir gözlemci tarafından şifresi çözülebilirse sorun değil
- Veri fazı paketinin paket numarası bir AEAD nonce'ıdır ve kritik veridir. netDb'de bulunan introduction key bilgisine sahip olsa bile bir gözlemci tarafından şifresi çözülebilir olmamalıdır. Bkz. [Nonces](https://eprint.iacr.org/2019/624.pdf).

QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) başlık koruma şemasından farklı olarak, hedef ve kaynak bağlantı kimliklerini de içeren tüm başlıkların TÜM bölümleri şifrelenir. QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) ve [Nonces](https://eprint.iacr.org/2019/624.pdf) öncelikle başlığın "kritik" kısmını, yani paket numarasını (ChaCha20 nonce) şifrelemeye odaklanır. Oturum kimliğini şifrelemek gelen paket sınıflandırmasını biraz daha karmaşık hale getirse de, bazı saldırıları zorlaştırır. QUIC farklı aşamalar için ve yol zorlaması ile bağlantı geçişi için farklı bağlantı kimlikleri tanımlar. Burada şifreli oldukları için aynı bağlantı kimliklerini baştan sona kullanırız.

Yedi başlık koruma anahtarı fazı bulunmaktadır:

Header şifreleme, karmaşık buluşsal yöntemler veya geri dönüş mekanizmaları olmaksızın gelen paketlerin hızlı sınıflandırılmasına olanak tanımak için tasarlanmıştır. Bu, neredeyse tüm gelen mesajlar için aynı k_header_1 anahtarının kullanılmasıyla gerçekleştirilir. Gerçek bir IP değişikliği veya NAT davranışı nedeniyle bir bağlantının kaynak IP'si veya portu değişse bile, paket connection ID'nin tek bir aramasıyla hızla bir oturumla eşleştirilebilir.

Session Created ve Retry mesajlarının, Connection ID'yi şifresini çözmek için k_header_1 için fallback işleme gerektiren TEK mesajlar olduğunu unutmayın, çünkü bunlar gönderenin (Bob'un) intro key'ini kullanır. DİĞER TÜM mesajlar k_header_1 için alıcının intro key'ini kullanır. Fallback işleme yalnızca kaynak IP/port'a göre bekleyen outbound bağlantıları araması gerekir.

Kaynak IP/port ile yedek işleme bekleyen giden bağlantıyı bulamazsa, bunun birkaç nedeni olabilir:

Bekleyen giden bağlantıyı bulmaya çalışmak ve bu bağlantı için k_header_1 kullanarak bağlantı ID'sini şifresini çözmek için ek yedek işleme mümkün olsa da, muhtemelen gerekli değildir. Bob'un NAT veya paket yönlendirme konularında sorunları varsa, bağlantının başarısız olmasına izin vermek muhtemelen daha iyidir. Bu tasarım, uç noktaların handshake süresi boyunca kararlı bir adres tutmasına dayanır.

Ek yönergeler için aşağıdaki Gelen Paket İşleme bölümüne bakın.

- Oturum İsteği ve Token İsteği
- Oturum Oluşturuldu
- Yeniden Deneme
- Oturum Onaylandı
- Veri Aşaması
- Eş Testi
- Delik Delme

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_1</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_2</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Request KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Created KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice/Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See data phase KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 5,7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Hole Punch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
  </tbody>
</table>
Bu aşama için başlık şifreleme anahtarlarının türetilmesi için aşağıdaki bireysel KDF bölümlerine bakın.

Bu KDF, iki ChaCha20 işlemi için IV olarak paketin son 24 baytını kullanır. Tüm paketler 16 baytlık bir MAC ile bittiğinden, bu durum tüm paket yüklerinin minimum 8 bayt olmasını gerektirir. Bu gereklilik ayrıca aşağıdaki mesaj bölümlerinde de belgelenmiştir.

Başlığın ilk 8 baytını şifresini çözdükten sonra, alıcı Hedef Bağlantı Kimliği'ni bilecektir. Oradan itibaren alıcı, oturumun anahtar aşamasına dayalı olarak başlığın geri kalanı için hangi başlık şifreleme anahtarını kullanacağını bilir.

- SSU2 mesajı değil
- Bozuk bir SSU2 mesajı
- Yanıt bir saldırgan tarafından sahte veya değiştirilmiş
- Bob'un simetrik bir NAT'ı var
- Bob mesaj işleme sırasında IP veya port değiştirdi
- Bob yanıtı farklı bir arayüzden gönderdi

Header'ın sonraki 8 baytını şifrelemeden çıkarmak, mesaj türünü ortaya çıkaracak ve bunun kısa mı yoksa uzun bir header mı olduğunu belirlemeyi mümkün kılacaktır. Eğer uzun bir header ise, alıcı version ve netid alanlarını doğrulamalıdır. Version != 2 ise, veya netid != beklenen değer ise (genellikle 2, test ağları hariç), alıcı mesajı düşürmelidir.

Tüm mesajlar üç ya da dört bölümden oluşur:

Tüm durumlarda, başlık (ve varsa, ephemeral key) tüm mesajın bütünlüğünü sağlamak için kimlik doğrulama MAC'ine bağlanır.

#### AEAD Hata İşleme

```
// incoming encrypted packet
packet = incoming encrypted packet
len = packet.length

// take the next-to-last 12 bytes of the packet
iv = packet[len-24:len-13]
k_header_1 = header encryption key 1
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_1, iv, data)

// encrypt the first part of the header by XORing with the mask
packet[0:7] ^= mask[0:7]

// take the last 12 bytes of the packet
iv = packet[len-12:len-1]
k_header_2 = header encryption key 2
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_2, iv, data)

// encrypt the second part of the header by XORing with the mask
packet[8:15] ^= mask[0:7]


// For Session Request and Session Created only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header and the ephemeral key
packet[16:63] = ChaCha20.encrypt(k_header_2, iv, packet[16:63])


// For Retry, Token Request, Peer Test, and Hole Punch only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header
packet[16:31] = ChaCha20.encrypt(k_header_2, iv, packet[16:31])
```
Gelen paket işleyicileri, mesajı işlemeden önce her zaman ChaCha20 yükünü deşifre etmeli ve MAC'i doğrulamalıdır, tek bir istisna dışında: Geçersiz token içeren Session Request mesajları gibi görünen adres sahteciliği yapılmış paketlerden gelen DoS saldırılarını azaltmak için, bir işleyicinin tam mesajı deşifre etmeye ve doğrulamaya (ChaCha20/Poly1305 deşifrelemeye ek olarak pahalı bir DH işlemi gerektiren) çalışması gerekmez. İşleyici, Session Request mesajının başlığında bulunan değerleri kullanarak bir Retry mesajı ile yanıt verebilir.

#### İlk ChainKey için KDF

Üç ayrı kimlik doğrulamalı şifreleme örneği (CipherStates) bulunmaktadır. Biri handshake aşamasında, ikisi ise (gönderme ve alma) veri aşaması için kullanılır. Her birinin KDF'den gelen kendi anahtarı vardır.

Şifrelenmiş/doğrulanmış veriler şu şekilde temsil edilecektir:

### Kimlik Doğrulamalı Şifreleme

Şifrelenmiş ve doğrulanmış veri formatı.

- Mesaj başlığı
- Yalnızca Session Request ve Session Created için geçici bir anahtar
- ChaCha20-şifrelenmiş yük
- Bir Poly1305 MAC

Şifreleme/şifre çözme fonksiyonlarına girdi değerleri:

- Handshake mesajları Session Request, Session Created ve Session Confirmed için, mesaj başlığı Noise işleme aşamasından önce mixHash() edilir
- Geçici anahtar, eğer mevcutsa, standart bir Noise misHash() tarafından korunur
- Noise handshake dışındaki mesajlar için, başlık ChaCha20/Poly1305 şifrelemesi için Associated Data olarak kullanılır.

Şifreleme fonksiyonunun çıktısı, şifre çözme fonksiyonunun girdisi:

### Session Request için KDF

ChaCha20 için burada açıklanan, TLS [RFC-7905](https://tools.ietf.org/html/rfc7905)'te benzer şekilde kullanılan [RFC-7539](https://tools.ietf.org/html/rfc7539)'a karşılık gelir.

Anahtar Türetme Fonksiyonu (KDF), [RFC-2104](https://tools.ietf.org/html/rfc2104)'te tanımlandığı şekliyle HMAC-SHA256(key, data) kullanarak DH sonucundan bir handshake aşaması şifre anahtarı k oluşturur. Bunlar InitializeSymmetric(), MixHash() ve MixKey() fonksiyonlarıdır ve tam olarak Noise spesifikasyonunda tanımlandığı gibidir.

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   Encrypted and authenticated data    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
```
#### Oturum İsteği için KDF

Alice, Bob'a el sıkışma sürecindeki ilk mesaj olarak ya da bir Retry mesajına yanıt olarak gönderir. Bob bir Session Created mesajı ile yanıtlar. Boyut: 80 + payload boyutu. Minimum Boyut: 88

Alice geçerli bir token'a sahip değilse, Session Request oluştururken asimetrik şifreleme yükünden kaçınmak için Session Request yerine Token Request mesajı göndermelidir.

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
      The packet header, 16 bytes.

data :: Plaintext data, 0 or more bytes
```
Uzun başlık. Noise içeriği: Alice'in geçici anahtarı X Noise yükü: DateTime ve diğer bloklar Maksimum yük boyutu: MTU - 108 (IPv4) veya MTU - 128 (IPv6). 1280 MTU için: Maksimum yük 1172 (IPv4) veya 1152 (IPv6). 1500 MTU için: Maksimum yük 1392 (IPv4) veya 1372 (IPv6).

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|       ChaCha20 encrypted data         |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|  Poly1305 Message Authentication Code |
+              (MAC)                    +
|             16 bytes                  |
+----+----+----+----+----+----+----+----+

encrypted data :: Same size as plaintext data, 0 - 65519 bytes

MAC :: Poly1305 message authentication code, 16 bytes
```
Payload Güvenlik Özellikleri:

#### Yük

- ChaCha20 bir akış şifresi olduğu için, düz metinlerin doldurulması gerekmez. Ek anahtar akışı baytları atılır.
- Şifre için anahtar (256 bit), SHA256 KDF aracılığıyla üzerinde anlaşılır. Her mesaj için KDF'nin ayrıntıları aşağıdaki ayrı bölümlerdedir.

#### Notlar

- Tüm mesajlarda, AEAD mesaj boyutu önceden bilinir. Bir AEAD kimlik doğrulama hatasında, alıcı daha fazla mesaj işlemeyi durdurmalı ve mesajı atmalıdır.
- Bob, tekrarlanan hatalar olan IP'lerin kara listesini tutmalıdır.

### SessionRequest (Tip 0)

X değeri, gerekli DPI karşı önlemleri olan payload ayırt edilemezliği ve benzersizliği sağlamak için şifrelenir. Bunu başarmak için elligator2 gibi daha karmaşık ve yavaş alternatiflere kıyasla ChaCha20 şifrelemeyi kullanırız. Bob'un router genel anahtarına asimetrik şifreleme çok yavaş olacaktır. ChaCha20 şifreleme, network database'de yayınlandığı şekliyle Bob'un intro anahtarını kullanır.

#### Yük Verisi

```
// Define protocol_name.
Set protocol_name = "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256"
 (52 bytes, US-ASCII encoded, no NULL termination).

// Define Hash h = 32 bytes
h = SHA256(protocol_name);

Define ck = 32 byte chaining key. Copy the h data to ck.
Set ck = h

// MixHash(null prologue)
h = SHA256(h);

// up until here, can all be precalculated by Alice for all outgoing connections

// Bob's X25519 static keys
// bpk is published in routerinfo
bsk = GENERATE_PRIVATE()
bpk = DERIVE_PUBLIC(bsk)

// Bob static key
// MixHash(bpk)
// || below means append
h = SHA256(h || bpk);

// Bob introduction key
// bik is published in routerinfo
bik = RANDOM(32)

// up until here, can all be precalculated by Bob for all incoming connections
```
#### Notlar

```
// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Alice's X25519 ephemeral keys
aesk = GENERATE_PRIVATE()
aepk = DERIVE_PUBLIC(aesk)

// Alice ephemeral key X
// MixHash(aepk)
h = SHA256(h || aepk);

// h is used as the associated data for the AEAD in Session Request
// Retain the Hash h for the Session Created KDF


End of "e" message pattern.

This is the "es" message pattern:

// DH(e, rs) == DH(s, re)
sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
// ChaChaPoly parameters to encrypt/decrypt
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chainKey for Session Created KDF


End of "es" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2 = bik

// Header encryption keys for next message (Session Created)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessCreateHeader", 32)

// Header encryption keys for next message (Retry)
k_header_1 = bik
k_header_2 = bik
```
### Session Created ve Session Confirmed kısım 1 için KDF

ChaCha20 şifreleme yalnızca DPI direnci içindir. Ağ veritabanında yayınlanan Bob'un tanıtım anahtarını bilen herhangi bir taraf, bu mesajdaki başlığı ve X değerini şifresini çözebilir.

Ham içerikler:

Şifrelenmemiş veri (Poly1305 kimlik doğrulama etiketi gösterilmemiş):

Minimum payload boyutu 8 bayttır. DateTime bloğu yalnızca 7 bayt olduğundan, en az bir başka bloğun daha bulunması gerekir.

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
Bob, Alice'e Session Request mesajına yanıt olarak gönderir. Alice, Session Confirmed mesajıyla yanıtlar. Boyut: 80 + payload boyutu. Minimum Boyut: 88

Noise içeriği: Bob'un geçici anahtarı Y Noise yükü: DateTime, Address ve diğer bloklar Maksimum yük boyutu: MTU - 108 (IPv4) veya MTU - 128 (IPv6). 1280 MTU için: Maksimum yük 1172 (IPv4) veya 1152 (IPv6). 1500 MTU için: Maksimum yük 1392 (IPv4) veya 1372 (IPv6).

Payload Güvenlik Özellikleri:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|    See Header Encryption KDF          |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key n=0     +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+       X, ChaCha20 encrypted           +
|       with Bob intro key n=0          |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|  k defined in KDF for Session Request |
+  n = 0                                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

X :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted X)
```
Y değeri, gerekli DPI karşı önlemleri olan yük ayırt edilemezliğini ve benzersizliğini sağlamak için şifrelenir. Bunu başarmak için elligator2 gibi daha karmaşık ve yavaş alternatiflerin yerine ChaCha20 şifrelemesi kullanırız. Alice'ın router genel anahtarına asimetrik şifreleme çok yavaş olurdu. ChaCha20 şifrelemesi, network database'de yayınlandığı şekliyle Bob'un intro anahtarını kullanır.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                   X                   |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|     see below for allowed blocks      |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 0

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Alice, ignored

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: 0 if not previously received from Bob

X :: 32 bytes, X25519 ephemeral key, little endian
```
#### Sorunlar

- DateTime bloğu
- Seçenekler bloğu (isteğe bağlı)
- Relay Tag İsteği bloğu (isteğe bağlı)
- Dolgu bloğu (isteğe bağlı)

ChaCha20 şifreleme yalnızca DPI direnci içindir. Bob'un ağ veritabanında yayınlanan intro anahtarını bilen ve Session Request'in ilk 32 baytını yakalayan herhangi bir taraf, bu mesajdaki Y değerini çözebilir.

#### Yük

- İlk ChaCha20 bloğundaki benzersiz X değeri, şifreli metnin her oturum için farklı olmasını sağlar.
- Yoklama direnci sağlamak için Bob, Session Request mesajındaki mesaj türü, protokol sürümü ve network ID alanları geçerli olmadıkça Session Request mesajına yanıt olarak Retry mesajı göndermemelidir.
- Bob, zaman damgası değeri mevcut zamandan çok uzak olan bağlantıları reddetmelidir. Maksimum delta zamanını "D" olarak adlandırın. Bob, daha önce kullanılan handshake değerlerinin yerel önbelleğini tutmalı ve tekrar saldırılarını önlemek için kopyaları reddetmelidir. Önbellekteki değerlerin en az 2*D yaşam süresi olmalıdır. Önbellek değerleri uygulamaya bağlıdır, ancak 32-byte'lık X değeri (veya şifrelenmiş eşdeğeri) kullanılabilir. Sıfır token ve sonlandırma bloğu içeren Retry mesajı göndererek reddedin.
- Kriptografik saldırıları önlemek için Diffie-Hellman geçici anahtarları asla yeniden kullanılamaz ve yeniden kullanım tekrar saldırısı olarak reddedilir.
- "KE" ve "auth" seçenekleri uyumlu olmalıdır, yani paylaşılan gizli K uygun boyutta olmalıdır. Daha fazla "auth" seçeneği eklenirse, bu "KE" bayrağının anlamını farklı bir KDF veya farklı bir kesme boyutu kullanacak şekilde örtük olarak değiştirebilir.
- Bob, Alice'in geçici anahtarının burada eğri üzerinde geçerli bir nokta olduğunu doğrulamalıdır.
- Padding makul bir miktarla sınırlandırılmalıdır. Bob, aşırı padding'li bağlantıları reddedebilir. Bob, padding seçeneklerini Session Created'da belirtecektir. Min/max yönergeleri TBD. Minimum 0 ila 31 byte arası rastgele boyut? (Dağılım belirlenmeli, Ek A'ya bakın.)
- AEAD, DH, belirgin tekrar veya anahtar doğrulama hatası dahil çoğu hatada, Bob daha fazla mesaj işlemeyi durdurmalı ve yanıt vermeden mesajı bıraksıra melidir.
- Bob, DateTime bloğundaki zaman damgası çok fazla çarpıksa, sıfır token ve saat çarpıklığı neden kodu içeren Termination bloğu ile Retry mesajı GÖNDEREBİLİR.
- DoS Azaltımı: DH nispeten pahalı bir işlemdir. Önceki NTCP protokolünde olduğu gibi, router'lar CPU veya bağlantı tükenmesini önlemek için gerekli tüm önlemleri almalıdır. Maksimum aktif bağlantılar ve devam eden maksimum bağlantı kuruluşları için sınırlar koyun. Okuma zaman aşımlarını uygulayın (hem okuma başına hem de "slowloris" için toplam). Aynı kaynaktan tekrarlanan veya eşzamanlı bağlantıları sınırlayın. Tekrar tekrar başarısız olan kaynaklar için kara listeler tutun. AEAD hatasına yanıt vermeyin. Alternatif olarak, DH işlemi ve AEAD doğrulamasından önce Retry mesajı ile yanıt verin.
- "ver" alanı: SSU2'yi belirten SSU2 protokolü dahil olmak üzere genel Noise protokolü, uzantıları ve payload spesifikasyonları. Bu alan gelecekteki değişiklikler için desteği belirtmek üzere kullanılabilir.
- Network ID alanı, çapraz ağ bağlantılarını hızla tanımlamak için kullanılır. Bu alan Bob'un network ID'si ile eşleşmiyorsa, Bob bağlantıyı kesip gelecekteki bağlantıları bloklamalıdır.
- Source Connection ID, Destination Connection ID'ye eşitse Bob mesajı bırakmalıdır.

### SessionCreated (Tip 1)

```
// take h saved from Session Request KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Request)

// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Bob's X25519 ephemeral keys
besk = GENERATE_PRIVATE()
bepk = DERIVE_PUBLIC(besk)

// h is from KDF for Session Request
// Bob ephemeral key Y
// MixHash(bepk)
h = SHA256(h || bepk);

// h is used as the associated data for the AEAD in Session Created
// Retain the Hash h for the Session Confirmed KDF

End of "e" message pattern.

This is the "ee" message pattern:

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chaining key ck for Session Confirmed KDF

End of "ee" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Request KDF above

// Header protection keys for next message (Session Confirmed)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessionConfirmed", 32)
```
### Session Confirmed bölüm 1 için KDF, Session Created KDF kullanarak

Ham içerikler:

Şifrelenmemiş veri (Poly1305 doğrulama etiketi gösterilmiyor):

Minimum yük boyutu 8 bayttır. DateTime ve Address blokları toplamda bundan fazla olduğundan, yalnızca bu iki blok ile gereksinim karşılanır.

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
Alice, Session Created mesajına yanıt olarak Bob'a gönderir. Bob hemen ACK bloğu içeren bir Data mesajı ile yanıtlar. Boyut: 80 + payload boyutu. Minimum Boyut: Yaklaşık 500 (minimum router bilgi bloğu boyutu yaklaşık 420 bayttır)

Noise içeriği: Alice'in statik anahtarı Noise payload bölüm 1: Hiçbiri Noise payload bölüm 2: Alice'in RouterInfo'su ve diğer bloklar Maksimum payload boyutu: MTU - 108 (IPv4) veya MTU - 128 (IPv6). 1280 MTU için: Maksimum payload 1172 (IPv4) veya 1152 (IPv6). 1500 MTU için: Maksimum payload 1392 (IPv4) veya 1372 (IPv6).

Payload Güvenlik Özellikleri:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with derived key n=0       +
|  See Header Encryption KDF            |
+----+----+----+----+----+----+----+----+
|                                       |
+       Y, ChaCha20 encrypted           +
|       with derived key n=0            |
+              (32 bytes)               +
|       See Header Encryption KDF       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in KDF for Session Created +
|  n = 0; see KDF for associated data   |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

Y :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted Y)
```
Bu, iki ChaChaPoly çerçevesi içerir. İlki Alice'in şifrelenmiş statik genel anahtarıdır. İkincisi Noise yükü'dür: Alice'in şifrelenmiş RouterInfo'su, isteğe bağlı seçenekler ve isteğe bağlı dolgudur. Aralarında MixKey() fonksiyonu çağrıldığı için farklı anahtarlar kullanırlar.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                  Y                    |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|      see below for allowed blocks     |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: The Source Connection ID
                             received from Alice in Session Request

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 0

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Bob, ignored

Source Connection ID :: The Destination Connection ID
                        received from Alice in Session Request

Token :: 0 (unused)

Y :: 32 bytes, X25519 ephemeral key, little endian
```
#### Notlar

- DateTime bloğu
- Address bloğu
- Relay Tag bloğu (isteğe bağlı)
- New Token bloğu (önerilmez, nota bakın)
- First Packet Number bloğu (isteğe bağlı)
- Options bloğu (isteğe bağlı)
- Termination bloğu (önerilmez, bunun yerine yeniden deneme mesajında gönderin)
- Padding bloğu (isteğe bağlı)

Ham içerikler:

#### Session Onaylandı Parçalama

- Alice, Bob'un ephemeral anahtarının eğri üzerinde geçerli bir nokta olduğunu burada doğrulamalıdır.
- Padding makul bir miktarla sınırlandırılmalıdır. Alice, aşırı padding içeren bağlantıları reddedebilir. Alice, padding seçeneklerini Session Confirmed'da belirtecektir. Min/max yönergeleri henüz belirlenmedi. 0 ila 31 byte arasında minimum rastgele boyut? (Dağılım belirlenecek, Ek A'ya bakın.)
- AEAD, DH, zaman damgası, görünür tekrar saldırı veya anahtar doğrulama hatası dahil herhangi bir hatada, Alice daha fazla mesaj işlemeyi durdurmalı ve yanıt vermeden bağlantıyı kapatmalıdır.
- Alice, zaman damgası değerinin mevcut zamandan çok uzak olduğu bağlantıları reddetmelidir. Maksimum delta zamanını "D" olarak adlandırın. Alice, daha önce kullanılmış handshake değerlerinin yerel bir önbelleğini tutmalı ve tekrar saldırılarını önlemek için tekrarları reddetmelidir. Önbellekteki değerler en az 2*D yaşam süresine sahip olmalıdır. Önbellek değerleri uygulama bağımlıdır, ancak 32-byte Y değeri (veya şifreli eşdeğeri) kullanılabilir.
- Alice, kaynak IP ve port, Session Request'in hedef IP ve portu ile eşleşmiyorsa mesajı atmalıdır.
- Alice, Destination ve Source Connection ID'leri Session Request'in Source ve Destination Connection ID'leri ile eşleşmiyorsa mesajı atmalıdır.
- Bob, Alice tarafından Session Request'te istenirse bir relay tag bloğu gönderir.
- Session Created'da New Token bloğu önerilmez, çünkü Bob önce Session Confirmed'ın doğrulamasını yapmalıdır. Aşağıdaki Tokens bölümüne bakın.

#### Notlar

- Min/maks dolgu seçenekleri burada dahil edilsin mi?

### Session Confirmed bölüm 2 için KDF

```
// take h saved from Session Created KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Created)

// MixHash(header)
h = SHA256(h || header)
// h is used as the associated data for the AEAD in Session Confirmed part 1, below

This is the "s" message pattern:

// Alice's X25519 static keys
ask = GENERATE_PRIVATE()
apk = DERIVE_PUBLIC(ask)

// AEAD parameters
// k is from Session Request
n = 1
ad = h
ciphertext = ENCRYPT(k, n++, apk, ad)

// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// h is used as the associated data for the AEAD in Session Confirmed part 2

End of "s" message pattern.

// Header encryption keys for this message
See Session Confirmed part 2 below
```
### SessionConfirmed (Tip 2)

```
This is the "se" message pattern:

// DH(ask, bepk) == DH(besk, apk)
sharedSecret = DH(ask, bepk) = DH(besk, apk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// h from Session Confirmed part 1 is used as the associated data for the AEAD in Session Confirmed part 2
// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF
// retain the hash h for the data phase KDF

End of "se" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Created KDF above

// Header protection keys for data phase
See data phase KDF below
```
### Veri aşaması için KDF

Şifrelenmemiş veri (Poly1305 doğrulama etiketleri gösterilmez):

Minimum yük boyutu 8 bayttır. RouterInfo bloğu bundan çok daha fazla olacağından, gereksinim yalnızca bu blokla karşılanır.

1)  Alice'in Router Info bloğu (gerekli)   2)  Seçenekler bloğu (isteğe bağlı)   3)  I2NP blokları (isteğe bağlı)

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
4\) Dolgu bloku (isteğe bağlı) Bu çerçeve asla başka bir blok türü içermemelidir. TODO: relay ve peer test ne olacak?

Session Confirmed mesajı, Bob'un birkaç gerekli kontrolü gerçekleştirebilmesi için Alice'den gelen tam imzalı Router Info'yu içermelidir:

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|   ChaCha20 frame (32 bytes)           |
+   Encrypted and authenticated data    +
+   Alice static key S                  +
| k defined in KDF for Session Created  |
+     n = 1                             +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+ Length varies (remainder of packet)   +
|                                       |
+   ChaChaPoly frame                    +
|   Encrypted and authenticated         |
+   see below for allowed blocks        +
|                                       |
+     k defined in KDF for              +
|     Session Confirmed part 2          |
+     n = 0                             +
|     see KDF for associated data       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, ChaChaPoly encrypted Alice's X25519 static key, little endian
     inside 48 byte ChaChaPoly frame
```
Ne yazık ki Router Info, RI bloğunda gzip ile sıkıştırılsa bile MTU'yu aşabilir. Bu nedenle Session Confirmed iki veya daha fazla pakete bölünebilir. Bu, SSU2 protokolünde AEAD korumalı bir yükün iki veya daha fazla pakete bölündüğü TEK durumdur.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
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
|        Noise Payload                  |
+        (length varies)                +
|        see below for allowed blocks   |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As sent in Session Request,
                             or one received in Session Confirmed?

Packet Number :: 0 always, for all fragments, even if retransmitted

type :: 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility

S :: 32 bytes, Alice's X25519 static key, little endian
```
#### Notlar

- RouterInfo bloğu (ilk blok olmalıdır)
- Seçenekler bloğu (isteğe bağlı)
- Yeni Token bloğu (isteğe bağlı)
- Relay Request bloğu (isteğe bağlı)
- Peer Test bloğu (isteğe bağlı)
- İlk Paket Numarası bloğu (isteğe bağlı)
- I2NP, İlk Fragment veya Takip Fragment blokları (isteğe bağlı, ancak muhtemelen yer yok)
- Dolgu bloğu (isteğe bağlı)

Her paketin başlıkları şu şekilde oluşturulur:

#### Yük

- Bob, olağan Router Info doğrulamasını gerçekleştirmeli. İmza türünün desteklendiğinden emin olmalı, imzayı doğrulamalı, zaman damgasının sınırlar içinde olduğunu kontrol etmeli ve gerekli diğer kontrolleri yapmalı. Parçalanmış Router Info'ları işleme ile ilgili notlar için aşağıya bakın.

- Bob, ilk frame'de alınan Alice'in statik anahtarının Router Info'daki statik anahtarla eşleştiğini doğrulamalıdır. Bob önce Router Info'da eşleşen sürüm (v) seçeneğine sahip bir NTCP veya SSU2 Router Adresi aramalıdır. Aşağıdaki Yayınlanmış Router Info ve Yayınlanmamış Router Info bölümlerine bakın. Parçalanmış Router Info'ların işlenmesi ile ilgili notlar için aşağıya bakın.

- Eğer Bob'un netdb'sinde Alice'in RouterInfo'sunun eski bir sürümü varsa, router info'daki statik anahtarın her ikisinde de aynı olduğunu doğrulayın (eğer mevcutsa) ve eski sürüm XXX'den daha az eski ise (aşağıdaki anahtar döndürme zamanına bakın)

- Bob, Alice'in statik anahtarının burada eğri üzerinde geçerli bir nokta olduğunu doğrulamalıdır.

- Padding parametrelerini belirtmek için seçenekler dahil edilmelidir.

- AEAD, RI, DH, zaman damgası veya anahtar doğrulama hatası dahil olmak üzere herhangi bir hatada, Bob daha fazla mesaj işlemeyi durdurmalı ve yanıt vermeden bağlantıyı kapatmalıdır.

- Mesaj 3 bölüm 2 çerçeve içeriği: Bu çerçevenin formatı, çerçevenin uzunluğunun Alice tarafından Session Request'te gönderilmesi dışında veri fazı çerçevelerinin formatıyla aynıdır. Veri fazı çerçeve formatı için aşağıya bakın. Çerçeve aşağıdaki sırada 1 ila 4 blok içermelidir:

Paket serisini aşağıdaki gibi oluşturun:

Yeniden birleştirme işlemi:

- Mesaj 3 bölüm 2 doldurma bloğu önerilir.

- MTU ve Router Info boyutuna bağlı olarak, I2NP blokları için hiç alan bulunmayabilir veya yalnızca küçük miktarda alan mevcut olabilir. Router Info parçalanmışsa I2NP bloklarını DAHİL ETMEYİN. En basit uygulama, Session Confirmed mesajında hiçbir zaman I2NP blokları dahil etmemek ve tüm I2NP bloklarını sonraki Data mesajlarında göndermek olabilir. Maksimum blok boyutu için aşağıdaki Router Info blok bölümüne bakın.

#### Yük

Bob herhangi bir Session Confirmed mesajı aldığında, başlığın şifresini çözer, frag alanını inceler ve Session Confirmed'in parçalandığını belirler. Tüm parçalar alınıp yeniden birleştirilene kadar mesajın şifresini çözmez (ve çözemez).

- RI'daki statik anahtar "s", handshake'teki statik anahtarla eşleşir
- RI'daki tanıtım anahtarı "i" çıkarılmalı ve geçerli olmalı, veri fazında kullanılmak üzere
- RI imzası geçerlidir

Bob'un bireysel fragmanları onaylaması için herhangi bir mekanizma yoktur. Bob tüm fragmanları aldığında, yeniden birleştirip, şifresini çözdükten ve içeriği doğruladıktan sonra, her zamanki gibi split() işlemi yapar, veri aşamasına girer ve 0 numaralı paketin ACK'ını gönderir.

Alice paket numarası 0'ın ACK'sını almazsa, oturum onaylanmış tüm paketleri olduğu gibi yeniden iletmelidir.

- TÜM başlıklar aynı paket numarası 0 ile kısa başlıklardır
- TÜM başlıklar parça numarası ve toplam parça sayısını içeren bir "frag" alanı içerir
- Parça 0'ın şifrelenmemiş başlığı, "jumbo" mesajı için ilişkili veri (AD)'dir
- Her başlık, O paketteki verinin son 24 baytı kullanılarak şifrelenir

Örnekler:

- Tek bir RI bloğu oluşturun (RI blok frag alanında 1'in 0. fragmanı). RI blok parçalama kullanmıyoruz, bu aynı sorunu çözmenin alternatif bir yöntemi içindi.
- RI bloğu ve dahil edilecek diğer blokları içeren bir "jumbo" payload oluşturun
- Toplam veri boyutunu hesaplayın (header dahil değil), bu payload boyutu + statik anahtar ve iki MAC için 64 bayt
- Her pakette mevcut alanı hesaplayın, bu MTU eksi IP header'ı (20 veya 40), eksi UDP header'ı (8), eksi SSU2 kısa header'ı (16). Paket başına toplam overhead 44 (IPv4) veya 64 (IPv6).
- Paket sayısını hesaplayın.
- Son paketteki verinin boyutunu hesaplayın. Header şifrelemenin çalışması için 24 bayt veya daha büyük olmalıdır. Eğer çok küçükse, ya bir padding bloğu ekleyin, YA DA zaten mevcutsa padding bloğunun boyutunu artırın, YA DA diğer paketlerden birinin boyutunu azaltarak son paketin yeterince büyük olmasını sağlayın.
- İlk paket için şifrelenmemiş header oluşturun, frag alanında toplam fragman sayısı ile, ve "jumbo" payload'ı Noise ile şifreleyin, header'ı AD olarak kullanarak, her zamanki gibi.
- Şifrelenmiş jumbo paketi fragmanlara bölün
- Her 1-n fragmanı için şifrelenmemiş header ekleyin
- Her 0-n fragmanı için header'ı şifreleyin. Her header yukarıda Session Confirmed KDF'de tanımlanan AYNI k_header_1 ve k_header_2'yi kullanır.
- Tüm fragmanları iletin

IPv6 üzerinde 1500 MTU için, maksimum yük 1372'dir, RI blok ek yükü 5'tir, maksimum (gzip sıkıştırılmış) RI veri boyutu 1367'dir (başka blok olmadığı varsayılarak). İki paket ile, 2. paketin ek yükü 64'tür, bu nedenle 1436 bayt daha yük taşıyabilir. Dolayısıyla iki paket, 2803 bayta kadar sıkıştırılmış bir RI için yeterlidir.

Mevcut ağda görülen en büyük sıkıştırılmış RI yaklaşık 1400 bayttır; bu nedenle pratikte, minimum 1280 MTU ile bile iki parça yeterli olmalıdır. Protokol maksimum 15 parçaya izin verir.

- Fragment 0 için başlığı koruyun, Noise AD olarak kullanıldığı için
- Yeniden birleştirmeden önce diğer fragmentların başlıklarını atın
- Fragment 0'ın başlığını AD olarak kullanarak "jumbo" payload'ı yeniden birleştirin ve Noise ile şifreleyin
- RI bloğunu her zamanki gibi doğrulayın
- Veri aşamasına geçin ve her zamanki gibi ACK 0 gönderin

Güvenlik analizi:

Parçalanmış bir Session Confirmed'ın bütünlüğü ve güvenliği, parçalanmamış olanla aynıdır. Herhangi bir parçanın değiştirilmesi, yeniden birleştirme sonrasında Noise AEAD'in başarısız olmasına neden olur. Fragment 0'dan sonraki parçaların başlıkları yalnızca parçayı tanımlamak için kullanılır. Yolda bulunan bir saldırgan başlığı şifrelemek için kullanılan k_header_2 anahtarına sahip olsa bile (bu pek olası değil, handshake'den türetilir), bu durum saldırganın geçerli bir parçayı yerine koymasına izin vermez.

Veri aşaması, ilişkili veri için başlığı kullanır.

KDF, zincir anahtarı ck'dan iki şifre anahtarı k_ab ve k_ba üretir ve [RFC-2104](https://tools.ietf.org/html/rfc2104)'te tanımlandığı şekilde HMAC-SHA256(key, data) kullanır. Bu, Noise spesifikasyonunda tam olarak tanımlandığı şekilde split() fonksiyonudur.

Noise payload: Tüm blok türlerine izin verilir. Maksimum payload boyutu: MTU - 60 (IPv4) veya MTU - 80 (IPv6). 1500 MTU için: Maksimum payload 1440 (IPv4) veya 1420 (IPv6)'dır.

Session Confirmed'ın 2. kısmından başlayarak, tüm mesajlar kimlik doğrulamalı ve şifrelenmiş bir ChaChaPoly payload içindedir. Tüm dolgu mesajın içindedir. Payload içinde sıfır veya daha fazla "blok" içeren standart bir format bulunur. Her blok bir baytlık tür ve iki baytlık uzunluğa sahiptir. Türler arasında tarih/saat, I2NP mesajı, seçenekler, sonlandırma ve dolgu bulunur.

Not: Bob, veri aşamasında Alice'e gönderdiği ilk mesaj olarak RouterInfo'sunu gönderebilir, ancak bunu yapmak zorunda değildir.

### Veri Mesajı (Tip 6)

Yük Güvenlik Özellikleri:

Şifrelenmemiş veri (Poly1305 kimlik doğrulama etiketi gösterilmemiş):

```
// split()
// chainKey = from handshake phase
keydata = HKDF(chainKey, ZEROLEN, "", 64)
k_ab = keydata[0:31]
k_ba = keydata[32:63]

// key is k_ab for Alice to Bob
// key is k_ba for Bob to Alice

keydata = HKDF(key, ZEROLEN, "HKDFSSU2DataKeys", 64)
k_data = keydata[0:31]
k_header_2 = keydata[32:63]


// AEAD parameters
k = k_data
n = 4 byte packet number from header
ad = 16 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for data phase
// aik = Alice's intro key
// bik = Bob's intro key
k_header_1 = Receiver's intro key (aik or bik)
k_header_2: from above
```
### Peer Test için KDF

Charlie Alice'e gönderir ve Alice Charlie'ye gönderir, yalnızca Peer Test aşamaları 5-7 için. Peer Test aşamaları 1-4 mutlaka oturum içinde bir Data mesajında Peer Test bloğu kullanılarak gönderilmelidir. Daha fazla bilgi için aşağıdaki Peer Test Bloğu ve Peer Test Süreci bölümlerine bakın.

Boyut: 48 + yük boyutu.

Noise yükü: Aşağıya bakınız.

Ham içerik:

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

- Router, AEAD hatası olan bir mesajı düşürmek zorundadır.

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with intro key and         +
|  derived key, see Data Phase KDF      |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in Data Phase KDF          +
|  n = packet number from header        |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Şifrelenmemiş veri (Poly1305 kimlik doğrulama etiketi gösterilmedi):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: See below

Packet Number :: Random number generated by Charlie

type :: 11

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: See below

Token :: 8 byte unsigned integer, randomly generated by Charlie, nonzero.
```
#### Yük

- Minimum yük boyutu 8 bayttır. Bu gereksinim herhangi bir ACK, I2NP, İlk Parça veya Takip Eden Parça bloğu tarafından karşılanacaktır. Gereksinim karşılanmazsa, bir Dolgu bloğu dahil edilmelidir.
- Her paket numarası yalnızca bir kez kullanılabilir. I2NP mesajlarını veya parçaları yeniden iletirken, yeni bir paket numarası kullanılmalıdır.

### Eş Testi (Tip 7)

```
// AEAD parameters
// aik = Alice's intro key
k = aik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = aik
k_header_2 = aik
```
### Yeniden Deneme için KDF

Minimum payload boyutu 8 bayttır. Peer Test bloğu toplamda bundan fazla olduğundan, sadece bu blok ile gereksinim karşılanır.

5 ve 7 numaralı mesajlarda, Peer Test bloğu oturum içi 3 ve 4 numaralı mesajlardan gelen blokla aynı olabilir (Charlie tarafından imzalanmış anlaşmayı içeren) veya yeniden oluşturulabilir. İmza isteğe bağlıdır.

Mesaj 6'da, Peer Test bloğu, Alice tarafından imzalanmış isteği içeren oturum içi mesaj 1 ve 2'deki blokla aynı olabilir veya yeniden oluşturulabilir. İmza isteğe bağlıdır.

Connection ID'ler: İki connection ID test nonce'ından türetilir. Charlie'den Alice'e gönderilen 5 ve 7 numaralı mesajlar için, Destination Connection ID, 4 byte'lık big-endian test nonce'ının iki kopyasıdır, yani ((nonce << 32) | nonce). Source Connection ID, Destination Connection ID'nin tersidir, yani ~((nonce << 32) | nonce). Alice'den Charlie'ye gönderilen 6 numaralı mesaj için, iki connection ID'yi değiştirin.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Adres bloğu içeriği:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

Packet Number :: Random number generated by Alice

type :: 10

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: zero
```
#### Notlar

- DateTime bloğu
- Address bloğu (mesaj 6 ve 7 için gerekli, aşağıdaki nota bakın)
- Peer Test bloğu
- Padding bloğu (isteğe bağlı)

Retry mesajının gereksinimi, Bob'un bir Retry mesajı üretmek için Session Request mesajını şifresini çözmek zorunda olmamasıdır. Ayrıca, bu mesaj yalnızca simetrik şifreleme kullanarak hızlı bir şekilde üretilmelidir.

Bob, Session Request veya Token Request mesajına yanıt olarak Alice'e gönderir. Alice yeni bir Session Request ile yanıtlar. Boyut: 48 + payload boyutu.

Ayrıca bir Termination bloğu dahil edilirse Sonlandırma mesajı olarak da işlev görür (yani, "Yeniden Deneme").

Noise payload: Aşağıya bakın.

Ham içerikler:

- Mesaj 5'te: Gerekli değil.
- Mesaj 6'da: Charlie'nin RI'sinden seçilen Charlie'nin IP'si ve portu.
- Mesaj 7'de: Mesaj 6'nın alındığı Alice'in gerçek IP'si ve portu.

### Yeniden Dene (Tip 9)

Şifrelenmemiş veri (Poly1305 kimlik doğrulama etiketi gösterilmemiş):

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Token İsteği için KDF

Minimum yük boyutu 8 bayttır. DateTime ve Address blokları toplamda bundan fazla olduğu için, gereklilik sadece bu iki blokla karşılanır.

Bu mesaj sadece simetrik şifreleme kullanarak hızlı bir şekilde oluşturulmalıdır.

Alice, Bob'a gönderir. Bob bir Retry mesajı ile yanıt verir. Boyut: 48 + payload boyutu.

Alice geçerli bir token'a sahip değilse, Session Request oluşturmadaki asimetrik şifreleme yükünden kaçınmak için Session Request yerine bu mesajı göndermelidir.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Noise yükü: Aşağıya bakınız.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: The Source Connection ID
                             received from Alice in Token Request
                             or Session Request

Packet Number :: Random number generated by Bob

type :: 9

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: The Destination Connection ID
                        received from Alice in Token Request
                        or Session Request

Token :: 8 byte unsigned integer, randomly generated by Bob, nonzero,
         or zero if session is rejected and a termination block is included
```
#### Yük Verisi

- DateTime bloğu
- Address bloğu
- Options bloğu (isteğe bağlı)
- Termination bloğu (isteğe bağlı, oturum reddedilirse)
- Padding bloğu (isteğe bağlı)

Ham içerik:

#### TarihSaat

- Araştırma direnci sağlamak için, bir router yalnızca Request mesajındaki mesaj türü, protokol versiyonu ve ağ kimliği alanları geçerli olduğunda Session Request veya Token Request mesajına yanıt olarak Retry mesajı göndermelidir.
- Sahte kaynak adresleri kullanılarak yapılabilecek herhangi bir amplifikasyon saldırısının büyüklüğünü sınırlamak için, Retry mesajı büyük miktarda padding içermemelidir. Retry mesajının yanıt verdiği mesajın boyutundan üç kat daha büyük olmaması önerilir. Alternatif olarak, 1-64 bayt aralığında rastgele miktarda padding ekleme gibi basit bir yöntem kullanın.

### Token İsteği (Tip 10)

Şifrelenmemiş veri (Poly1305 kimlik doğrulama etiketi gösterilmemiştir):

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Hole Punch için KDF

Minimum payload boyutu 8 bayttır.

Bu mesaj yalnızca simetrik şifreleme kullanarak hızlı bir şekilde üretilmelidir.

Charlie, Bob'tan alınan bir Relay Intro'ya yanıt olarak Alice'e gönderir. Alice yeni bir Session Request ile yanıt verir. Boyut: 48 + payload boyutu.

Noise yükü: Aşağıya bakın.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Ham içerikler:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|    flags     |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As specified in session setup

Packet Number :: 4 byte big endian integer

type :: 6

flags :: 3 bytes, unused, set to 0 for future compatibility
```
#### Seçenekler

- DateTime bloğu
- Padding bloğu

Şifrelenmemiş veri (Poly1305 kimlik doğrulama etiketi gösterilmemiştir):

#### RouterInfo

- Araştırma direncini sağlamak için, bir router Token Request mesajındaki mesaj türü, protokol sürümü ve ağ ID alanları geçerli olmadıkça Token Request mesajına yanıt olarak Retry mesajı göndermemelidir.
- Bu standart bir Noise mesajı DEĞİLDIR ve handshake'in bir parçası değildir. Bağlantı ID'leri dışında Session Request mesajıyla bağlantılı değildir.
- AEAD dahil çoğu hata durumunda veya görünür replay saldırısında Bob daha fazla mesaj işlemeyi durdurmalı ve yanıt vermeden mesajı bırakmalıdır.
- Bob, zaman damgası değeri mevcut zamandan çok uzak olan bağlantıları reddetmelidir. Maksimum delta zamanını "D" olarak adlandırın. Bob, replay saldırılarını önlemek için önceden kullanılan handshake değerlerinin yerel bir önbelleğini tutmalı ve duplikatları reddetmelidir. Önbellekteki değerler en az 2*D yaşam süresine sahip olmalıdır. Önbellek değerleri implementasyona bağımlıdır, ancak 32-byte X değeri (veya şifrelenmiş eşdeğeri) kullanılabilir.
- Bob, DateTime bloğundaki zaman damgası çok fazla saptığında sıfır token ve saat sapması neden koduna sahip Termination bloğu içeren bir Retry mesajı GÖNDEREBİLİR.
- Minimum boyut: TBD, Session Created ile aynı kurallar?

### Hole Punch (Tip 11)

Minimum payload boyutu 8 bayttır. DateTime ve Address blokları toplamda bundan fazla olduğu için, gereklilik sadece bu iki blok ile karşılanmış olur.

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Yük Formatı

Bağlantı ID'leri: İki bağlantı ID'si relay nonce'dan türetilir. Hedef Bağlantı ID'si, 4 baytlık big-endian relay nonce'un iki kopyasıdır, yani ((nonce << 32) | nonce). Kaynak Bağlantı ID'si, Hedef Bağlantı ID'sinin tersidir, yani ~((nonce << 32) | nonce).

Alice, başlıktaki token'ı görmezden gelmelidir. Session Request'te kullanılacak token, Relay Response bloğundadır.

Her Noise yükü sıfır veya daha fazla "blok" içerir.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Bu, [NTCP2](/docs/specs/ntcp2) ve [ECIES](/docs/specs/ecies) spesifikasyonlarında tanımlananla aynı blok formatını kullanır. Bireysel blok türleri farklı şekilde tanımlanır. QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) standardındaki eşdeğer terim "frame"lerdir.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: See below

type :: 7

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random number generated by Alice or Charlie

Source Connection ID :: See below

Token :: Randomly generated by Alice or Charlie, ignored
```
#### I2NP Mesajı

- DateTime bloğu
- Address bloğu
- Relay Response bloğu
- Padding bloğu (isteğe bağlı)

Uygulayıcıları kod paylaşımına teşvik etmenin ayrıştırma sorunlarına yol açabileceği konusunda endişeler bulunmaktadır. Uygulayıcılar kod paylaşımının fayda ve risklerini dikkatli bir şekilde değerlendirmeli ve iki bağlam için sıralama ve geçerli blok kurallarının farklı olduğundan emin olmalıdır.

Şifrelenmiş yük içinde bir veya daha fazla blok bulunur. Bir blok, basit bir Tag-Length-Value (TLV) formatıdır. Her blok bir baytlık tanımlayıcı, iki baytlık uzunluk ve sıfır veya daha fazla veri baytı içerir. Bu format [NTCP2](/docs/specs/ntcp2) ve [ECIES](/docs/specs/ecies) ile aynıdır, ancak blok tanımları farklıdır.

Genişletilebilirlik için, alıcılar bilinmeyen tanımlayıcılara sahip blokları görmezden gelmeli ve bunları dolgu olarak değerlendirmelidir.

## Noise Payload

(Poly1305 auth etiketi gösterilmemiştir):

Header şifreleme, iki ChaCha20 işlemi için IV olarak paketin son 24 baytını kullanır. Tüm paketler 16 baytlık bir MAC ile bittiğinden, bu durum tüm paket yüklerinin minimum 8 bayt olmasını gerektirir. Bir yük aksi halde bu gereksinimi karşılamıyorsa, bir Padding bloğu dahil edilmelidir.

Maksimum ChaChaPoly yük boyutu, mesaj türü, MTU ve IPv4 veya IPv6 adres türüne bağlı olarak değişir. Maksimum yük boyutu IPv4 için MTU - 60, IPv6 için MTU - 80'dir. Maksimum yük verisi IPv4 için MTU - 63, IPv6 için MTU - 83'tür. Üst sınır IPv4, 1500 MTU, Data mesajı için yaklaşık 1440 bayttır. Maksimum toplam blok boyutu, maksimum yük boyutuna eşittir. Maksimum tek blok boyutu, maksimum toplam blok boyutuna eşittir. Blok türü 1 bayttır. Blok uzunluğu 2 bayttır. Maksimum tek blok veri boyutu, maksimum tek blok boyutundan 3 çıkarılmış halidir.

### Blok Sıralama Kuralları

Notlar:

Blok türleri:

Session Confirmed'da, Router Info ilk blok olmalıdır.

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

blk :: 1 byte, see below
size :: 2 bytes, big endian, size of data to follow, 0 - TBD
data :: the data
```
Diğer tüm mesajlarda sıra belirtilmemiştir, ancak şu gereksinimler hariçtir: Padding (dolgu) mevcutsa, son blok olmalıdır. Termination (sonlandırma) mevcutsa, Padding hariç son blok olmalıdır. Tek bir payload içinde birden fazla Padding bloğuna izin verilmez.

Zaman senkronizasyonu için:

Notlar:

- Uygulayıcılar, bir blok okunurken, hatalı biçimlendirilmiş veya kötü niyetli verilerin okumaların bir sonraki bloğa veya payload sınırının ötesine taşmasına neden olmayacağından emin olmalıdır.
- Uygulamalar, ileri uyumluluk için bilinmeyen blok türlerini görmezden gelmelidir.

Güncellenmiş seçenekleri geçin. Seçenekler şunları içerir: Minimum ve maksimum dolgu.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Block Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Number</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Block Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Options</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15+</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Router Info</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">I2NP Message</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Follow-on Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Termination</td><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 typ.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">8</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Intro</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Next Nonce</td><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">ACK</td><td style="border:1px solid var(--color-border); padding:0.6rem;">12</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 or 21</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;">--</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">17</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Challenge</td><td style="border:1px solid var(--color-border); padding:0.6rem;">18</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">19</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Packet Number</td><td style="border:1px solid var(--color-border); padding:0.6rem;">20</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Congestion</td><td style="border:1px solid var(--color-border); padding:0.6rem;">21</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for experimental features</td><td style="border:1px solid var(--color-border); padding:0.6rem;">224-253</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Padding</td><td style="border:1px solid var(--color-border); padding:0.6rem;">254</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for future extension</td><td style="border:1px solid var(--color-border); padding:0.6rem;">255</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>           
### Blok Özellikleri

Options bloğu değişken uzunlukta olacaktır.

Seçenek Sorunları:

### Oturum İsteği

#### İlk Parça

Alice'in RouterInfo'sunu Bob'a ilet. Yalnızca Session Confirmed bölüm 2 yükünde kullanılır. Veri aşamasında kullanılmamalıdır; bunun yerine bir I2NP DatabaseStore Mesajı kullanın.

```
+----+----+----+----+----+----+----+
| 0  |    4    |     timestamp     |
+----+----+----+----+----+----+----+

blk :: 0
size :: 2 bytes, big endian, value = 4
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
```
Minimum Boyut: Yaklaşık 420 bayt, router identity ve router info içindeki imza sıkıştırılabilir olmadıkça, ki bu olası değildir.

- SSU 1'den farklı olarak, SSU 2'de veri fazı için paket başlığında zaman damgası yoktur.
- Uygulamalar veri fazında periyodik olarak DateTime blokları göndermelidir.
- Uygulamalar ağda saat sapmasını önlemek için en yakın saniyeye yuvarlamalıdır.

#### Takip Eden Fragment

NOT: Router Info bloğu asla parçalanmaz. Frag alanı her zaman 0/1'dir. Daha fazla bilgi için yukarıdaki Session Confirmed Fragmentation bölümüne bakın.

Notlar:

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
Değiştirilmiş başlığa sahip tam bir I2NP mesajı.

- Seçenek müzakeresi henüz belirlenmemiştir.

#### Sonlandırma

Bu, [NTCP2](/docs/specs/ntcp2)'deki ile aynı 9 baytlık I2NP başlığını kullanır (tür, mesaj kimliği, kısa süre sonu).

Notlar:

Değiştirilmiş başlığa sahip bir I2NP mesajının ilk parçası (parça #0).

```
+----+----+----+----+----+----+----+----+
| 2  |  size   |flag|frag|              |
+----+----+----+----+----+              +
|                                       |
+       Router Info fragment            +
| (Alice RI in Session Confirmed)       |
+ (Alice, Bob, or third-party           +
|  RI in data phase)                    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 2
size :: 2 bytes, big endian, 2 + fragment size
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 0 for local store, 1 for flood request
       bit 1: 0 for uncompressed, 1 for gzip compressed
       bits 7-2: Unused, set to 0 for future compatibility
frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number, always 0
       bits 3-0: total fragments, always 1, big endian

routerinfo :: Alice's or Bob's RouterInfo
```
Bu, [NTCP2](/docs/specs/ntcp2)'deki ile aynı 9 baytlık I2NP başlığını kullanır (tür, mesaj kimliği, kısa süre sonu).

- Router Info isteğe bağlı olarak gzip ile sıkıştırılır, bu flag bit 1 ile belirtilir. Bu, hiçbir zaman sıkıştırılmadığı NTCP2'den ve her zaman sıkıştırıldığı DatabaseStore Message'dan farklıdır. Sıkıştırma isteğe bağlıdır çünkü genellikle sıkıştırılabilir içeriğin az olduğu küçük Router Info'lar için çok az fayda sağlar, ancak birkaç sıkıştırılabilir Router Address'e sahip büyük Router Info'lar için çok faydalıdır. Sıkıştırma, bir Router Info'nun parçalanma olmadan tek bir Session Confirmed paketi içine sığmasını sağlıyorsa önerilir.
- Session Confirmed mesajındaki ilk veya tek parçanın maksimum boyutu: IPv4 için MTU - 113 veya IPv6 için MTU - 133. 1500 bayt varsayılan MTU varsayarak ve mesajda başka blok olmadığını varsayarak, IPv4 için 1387 veya IPv6 için 1367. Mevcut router info'ların %97'si gzip'lenmeden 1367'den küçüktür. Mevcut router info'ların %99.9'u gzip'lendiğinde 1367'den küçüktür. 1280 bayt minimum MTU varsayarak ve mesajda başka blok olmadığını varsayarak, IPv4 için 1167 veya IPv6 için 1147. Mevcut router info'ların %94'ü gzip'lenmeden 1147'den küçüktür. Mevcut router info'ların %97'si gzip'lendiğinde 1147'den küçüktür.
- Frag baytı artık kullanılmaz, Router Info bloğu hiçbir zaman parçalanmaz. Frag baytı parça 0, toplam parça 1 olarak ayarlanmalıdır. Daha fazla bilgi için yukarıdaki Session Confirmed Fragmentation bölümüne bakınız.
- RouterInfo'da yayınlanmış RouterAddress'ler olmadıkça flooding talep edilmemelidir. Alıcı router, içinde yayınlanmış RouterAddress'ler olmadıkça RouterInfo'yu flood etmemelidir.
- Bu protokol RouterInfo'nun saklandığına veya flood edildiğine dair bir onay sağlamaz. Onay isteniyorsa ve alıcı floodfill ise, gönderen bunun yerine reply token ile standart bir I2NP DatabaseStoreMessage göndermelidir.

#### RelayRequest

Toplam fragment sayısı belirtilmemiş.

Notlar:

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
Bir I2NP mesajının ek parçası (sıfırdan büyük parça numarası).

- Bu, NTCP2'de kullanılan aynı 9-baytlık I2NP başlık formatıdır.
- Bu, İlk Fragment bloğuyla tamamen aynı formattır, ancak blok türü bunun tam bir mesaj olduğunu belirtir.
- 9-baytlık I2NP başlığı dahil maksimum boyut IPv4 için MTU - 63 ve IPv6 için MTU - 83'tür.

#### RelayResponse

Notlar:

Bağlantıyı kes. Bu, payload içindeki son padding olmayan blok olmalıdır.

Notlar:

```
+----+----+----+----+----+----+----+----+
| 4  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |                   |
+----+----+----+----+                   +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 4
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: Partial I2NP message body, bytes 0 - (size - 10)
```
Oturum içinde Alice'den Bob'a Data mesajında gönderilir. Aşağıdaki Relay Process bölümüne bakın.

- Bu, NTCP2'de kullanılan aynı 9-byte I2NP başlık formatıdır.
- Bu, I2NP Message bloğu ile tamamen aynı formattır, ancak blok türü bunun bir mesajın ilk parçası olduğunu gösterir.
- Kısmi mesaj uzunluğu sıfırdan büyük olmalıdır.
- SSU 1'de olduğu gibi, alıcının toplam parça sayısını bilmesi ve alma tamponu ayırmasını verimli şekilde yapabilmesi için son parçanın önce gönderilmesi önerilir.
- 9-byte I2NP başlığı dahil maksimum boyut, IPv4 için MTU - 63 ve IPv6 için MTU - 83'tür.

#### RelayIntro

Notlar:

```
+----+----+----+----+----+----+----+----+
| 5  |  size   |frag|    msg id         |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 5
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 5).
frag :: Fragment info:
        Bit order: 76543210 (bit 7 is MSB)
        bits 7-1: fragment number 1 - 127 (0 not allowed)
        bit 0: isLast (1 = true)
msg id :: 4 bytes, big endian, I2NP message ID
message :: Partial I2NP message body
```
İmza:

- Kısmi mesaj uzunluğu sıfırdan büyük olmalıdır.
- SSU 1'de olduğu gibi, alıcının toplam fragment sayısını bilmesi ve alma tamponlarını verimli bir şekilde tahsis edebilmesi için son fragmenti ilk göndermeniz önerilir.
- SSU 1'de olduğu gibi, maksimum fragment numarası 127'dir, ancak pratik limit 63 veya daha azdır. Uygulamalar, yaklaşık 64 KB'lık maksimum I2NP mesaj boyutu için pratik olanla sınırlandırabilir, bu da 1280 minimum MTU ile yaklaşık 55 fragmenttir. Aşağıdaki Maksimum I2NP Mesaj Boyutu bölümüne bakın.
- Maksimum kısmi mesaj boyutu (fragment ve mesaj kimliği dahil değil) IPv4 için MTU - 68 ve IPv6 için MTU - 88'dir.

#### PeerTest

Alice isteği imzalar ve bu bloka dahil eder; Bob bunu Relay Intro bloğunda Charlie'ye iletir. İmza algoritması: Aşağıdaki veriyi Alice'in router imzalama anahtarı ile imzala:

```
+----+----+----+----+----+----+----+----+
| 6  |  size   |    valid data packets  |
+----+----+----+----+----+----+----+----+
    received   | rsn|     addl data     |
+----+----+----+----+                   +
~               .   .   .               ~
+----+----+----+----+----+----+----+----+

blk :: 6
size :: 2 bytes, big endian, value = 9 or more
valid data packets received :: The number of valid packets received
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
       11: Session Request error
       12: Session Created error
       13: Session Confirmed error
       14: Timeout
       15: RI signature verification fail
       16: s parameter missing, invalid, or mismatched in RouterInfo
       17: banned
       18: bad token
       19: connection limits
       20: incompatible version
       21: wrong net ID
       22: replaced by new session
addl data :: optional, 0 or more bytes, for future expansion, debugging,
             or reason text.
             Format unspecified and may vary based on reason code.
```
Oturum içinde bir Veri mesajında Charlie'den Bob'a veya Bob'dan Alice'e GÖNDERİLİR VE Charlie'den Alice'e Hole Punch mesajında gönderilir. Aşağıdaki Relay İşlemi bölümüne bakın.

- Tüm nedenler gerçekte kullanılmayabilir, implementasyona bağlıdır. Çoğu hata genellikle mesajın düşürülmesi ile sonuçlanır, sonlandırma ile değil. Yukarıdaki handshake mesaj bölümlerindeki notlara bakın. Listelenen ek nedenler tutarlılık, günlükleme, hata ayıklama veya politika değişiklikleri içindir.
- Termination bloğu ile birlikte bir ACK bloğunun dahil edilmesi önerilir.
- Veri aşamasında, "termination received" dışındaki herhangi bir neden için, eş "termination received" nedeni ile bir termination bloğu ile yanıt vermelidir.

#### NextNonce

Notlar:

```
+----+----+----+----+----+----+----+----+
|  7 |  size   |flag|       nonce       |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 7
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility

The data below here is covered
by the signature, and Bob forwards it unmodified.

nonce :: 4 bytes, randomly generated by Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
Token, Alice tarafından Session Request'te hemen kullanılmalıdır.

- IP adresi her zaman dahil edilir (SSU 1'den farklı olarak) ve oturum için kullanılan IP'den farklı olabilir.

İmza:

Charlie kabul ederse (yanıt kodu 0) veya reddederse (yanıt kodu 64 veya daha yüksek), Charlie yanıtı imzalar ve bu bloğa dahil eder; Bob bunu Relay Response bloğunda Alice'e iletir. İmza algoritması: Aşağıdaki verileri Charlie'nin router imzalama anahtarı ile imzala:

- prologue: 16 bayt "RelayRequestData", null ile sonlandırılmamış (mesaja dahil değil)
- bhash: Bob'un 32 baytlık router hash'i (mesaja dahil değil)
- chash: Charlie'nin 32 baytlık router hash'i (mesaja dahil değil)
- nonce: 4 bayt nonce
- relay tag: 4 bayt relay tag
- timestamp: 4 bayt zaman damgası (saniye)
- ver: 1 bayt SSU sürümü
- asz: 1 bayt uç nokta (port + IP) boyutu (6 veya 18)
- AlicePort: 2 bayt Alice'nin port numarası
- Alice IP: (asz - 2) bayt Alice IP adresi

#### Onay

Bob reddederse (yanıt kodu 1-63), Bob yanıtı imzalar ve bu bloka dahil eder. İmza algoritması: Aşağıdaki veriyi Bob'un router imzalama anahtarı ile imzala:

```
+----+----+----+----+----+----+----+----+
|  8 |  size   |flag|code|    nonce
+----+----+----+----+----+----+----+----+
     |     timestamp     | ver| csz|Char
+----+----+----+----+----+----+----+----+
 Port|   Charlie IP addr |              |
+----+----+----+----+----+              +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

blk :: 8
size :: 2 bytes, 6
flag :: 1 byte flags, Unused, set to 0 for future compatibility
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, Charlie is banned
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, relay tag not found
       6: rejected by Bob, Alice RI not found
       7-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       71-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD

The data below is covered by the signature if the code is 0 (accept).
Bob forwards it unmodified.

nonce :: 4 bytes, as received from Bob or Alice

The data below is present only if the code is 0 (accept).

timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
csz :: 1 byte endpoint (port + IP) size (0 or 6 or 18)
       may be 0 for some rejection codes
CharliePort :: 2 byte Charlie's port number, big endian
               not present if csz is 0
Charlie IP :: (csz - 2) byte representation of Charlie's IP address,
              network byte order
              not present if csz is 0
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Charlie.
             Not present if rejected by Bob.
token :: Token generated by Charlie for Alice to use
         in the Session Request.
         Only present if code is 0 (accept)
```
Oturum içinde bir Data mesajında, Bob'dan Charlie'ye gönderilir. Aşağıdaki Relay İşlemi bölümüne bakın.

Öncesinde bir RouterInfo bloğu veya Alice'in Router Info'sunu içeren I2NP DatabaseStore mesaj bloğu (veya parçası) bulunmalıdır; bu bilgi aynı payload içinde (yer varsa) veya önceki bir mesajda yer alabilir.

Notlar:

İmza:

- prologue: 16 bayt "RelayAgreementOK", null ile sonlandırılmamış (mesajda dahil değil)
- bhash: Bob'un 32 baytlık router hash'i (mesajda dahil değil)
- nonce: 4 bayt nonce
- timestamp: 4 bayt zaman damgası (saniye)
- ver: 1 bayt SSU sürümü
- csz: 1 bayt endpoint (port + IP) boyutu (0 veya 6 veya 18)
- CharliePort: 2 bayt Charlie'nin port numarası (csz 0 ise mevcut değil)
- Charlie IP: (csz - 2) bayt Charlie IP adresi (csz 0 ise mevcut değil)

Alice isteği imzalar ve Bob bu blokta onu Charlie'ye iletir. Doğrulama algoritması: Aşağıdaki verileri Alice'in router imzalama anahtarı ile doğrulayın:

- prologue: 16 bayt "RelayAgreementOK", null ile sonlandırılmamış (mesaja dahil değil)
- bhash: Bob'un 32 baytlık router hash'i (mesaja dahil değil)
- nonce: 4 bayt nonce
- timestamp: 4 bayt zaman damgası (saniye)
- ver: 1 bayt SSU versiyonu
- csz: 1 bayt = 0

#### Adres

Oturum içinde bir Data mesajında ya da oturum dışında bir Peer Test mesajında gönderilir. Aşağıdaki Peer Test İşlemi bölümüne bakınız.

Mesaj 2 için, Alice'in Router Info'sunu içeren bir RouterInfo bloğu veya I2NP DatabaseStore mesaj bloğu (veya parçası) ile öncelenmeli, bu bilgi aynı payload içinde (yer varsa) veya önceki bir mesajda bulunmalıdır.

```
+----+----+----+----+----+----+----+----+
|  9 |  size   |flag|                   |
+----+----+----+----+                   +
|                                       |
+                                       +
|         Alice Router Hash             |
+             32 bytes                  +
|                                       |
+                   +----+----+----+----+
|                   |      nonce        |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 9
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's 32-byte router hash,

The data below here is covered
by the signature, as received from Alice in the Relay Request,
and Bob forwards it unmodified.

nonce :: 4 bytes, as received from Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
Mesaj 4 için, relay kabul edilirse (neden kodu 0), önce bir RouterInfo bloğu veya Charlie'nin Router Info'sunu içeren I2NP DatabaseStore mesaj bloğu (veya parçası) gelmelidir; bu ya aynı payload'da (yer varsa) ya da önceki bir mesajda olabilir.

- IPv4 için, Alice'in IP adresi her zaman 4 byte'tır, çünkü Alice IPv4 üzerinden Charlie'ye bağlanmaya çalışır. IPv6 desteklenir ve Alice'in IP adresi 16 byte olabilir.
- IPv4 için, bu mesaj kurulmuş bir IPv4 bağlantısı üzerinden gönderilmelidir, çünkü Bob'un Charlie'nin IPv4 adresini bilmesinin ve [RelayResponse](#relayresponse) içinde Alice'e geri döndürmesinin tek yolu budur. IPv6 desteklenir ve bu mesaj kurulmuş bir IPv6 bağlantısı üzerinden gönderilebilir.
- Introducer'lar ile yayınlanan herhangi bir SSU adresi "caps" seçeneğinde "4" veya "6" içermelidir.

Notlar:

Alice, test etmek istediği transport (IPv4 veya IPv6) üzerinden mevcut bir oturum kullanarak isteği Bob'a gönderir. Bob, Alice'den IPv4 üzerinden bir istek aldığında, Bob bir IPv4 adresi tanıtan bir Charlie seçmelidir. Bob, Alice'den IPv6 üzerinden bir istek aldığında, Bob bir IPv6 adresi tanıtan bir Charlie seçmelidir. Gerçek Bob-Charlie iletişimi IPv4 veya IPv6 üzerinden olabilir (yani Alice'in adres türünden bağımsız).

- prologue: 16 bayt "RelayRequestData", null ile sonlandırılmamış (mesaja dahil değil)
- bhash: Bob'un 32 baytlık router hash'i (mesaja dahil değil)
- chash: Charlie'nin 32 baytlık router hash'i (mesaja dahil değil)
- nonce: 4 bayt nonce
- relay tag: 4 bayt relay etiketi
- timestamp: 4 bayt zaman damgası (saniye)
- ver: 1 bayt SSU versiyonu
- asz: 1 bayt endpoint (port + IP) boyutu (6 veya 18)
- AlicePort: 2 bayt Alice'in port numarası
- Alice IP: (asz - 2) bayt Alice IP adresi

#### Relay Tag İsteği

İmzalar:

Alice isteği imzalar ve mesaj 1'e dahil eder; Bob bunu mesaj 2'de Charlie'ye iletir. Charlie yanıtı imzalar ve mesaj 3'e dahil eder; Bob bunu mesaj 4'te Alice'e iletir. İmza algoritması: Aşağıdaki veriyi Alice'in veya Charlie'nin imzalama anahtarı ile imzalayın veya doğrulayın:

TODO yalnızca anahtarları döndürürsek

```
+----+----+----+----+----+----+----+----+
| 10 |  size   | msg|code|flag|         |
+----+----+----+----+----+----+         +
| Alice router hash (message 2 only)    |
+             or                        +
| Charlie router hash (message 4 only)  |
+ or all zeros if rejected by Bob       +
| Not present in messages 1,3,5,6,7     |
+                             +----+----+
|                             | ver|
+----+----+----+----+----+----+----+----+
   nonce       |     timestamp     | asz|
+----+----+----+----+----+----+----+----+
|AlicePort|  Alice IP address |         |
+----+----+----+----+----+----+         +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 10
size :: 2 bytes, big endian, size of data to follow
msg :: 1 byte message number 1-7
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, no Charlie available
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, address unsupported
       6-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       70-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD
       reject codes only allowed in messages 3 and 4
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's or Charlie's 32-byte router hash,
        only present in messages 2 and 4.
        All zeros (fake hash) in message 4 if rejected by Bob.

For messages 1-4, the data below here is covered
by the signature, if present, and Bob forwards it unmodified.

ver :: 1 byte SSU version:
       1: SSU 1 (not supported)
       2: SSU 2 (required)
nonce :: 4 byte test nonce, big endian
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice or Charlie.
             Only present for messages 1-4.
             Optional in message 5-7.
```
4 baytlık ack through, ardından bir ack sayısı ve sıfır veya daha fazla nack/ack aralığı.

- SSU 1'den farklı olarak, mesaj 1 Alice'in IP adresini ve portunu içermek zorundadır.

- IPv6 adreslerinin test edilmesi desteklenir ve Bob ve Charlie yayınladıkları IPv6 adresinde 'B' kabiliyeti ile destek belirtirse, Alice-Bob ve Alice-Charlie iletişimi IPv6 üzerinden olabilir. Ayrıntılar için Proposal 126'ya bakın.

Bu tasarım QUIC'ten uyarlanmış ve basitleştirilmiştir. Tasarım hedefleri şunlardır:

- Mesaj 1-4, mevcut bir oturumdaki Data mesajında bulunmalıdır.

- Bob, mesaj 2'yi göndermeden önce Alice'in RI'sını Charlie'ye göndermelidir.

- Bob, kabul edilirse (neden kodu 0) mesaj 4'ü göndermeden önce Charlie'nin RI'sını Alice'e göndermelidir.

- Mesaj 5-7'nin oturum dışı bir Peer Test mesajında bulunması gerekir.

- Mesaj 5 ve 7, mesaj 3 ve 4'te gönderilen aynı imzalanmış verileri içerebilir veya yeni bir zaman damgasıyla yeniden oluşturulabilir. İmza isteğe bağlıdır.

- Mesaj 6, mesaj 1 ve 2'de gönderilen imzalı verilerle aynı içeriği içerebilir veya yeni bir zaman damgasıyla yeniden oluşturulabilir. İmza isteğe bağlıdır.

Aşağıda belirtilen kodlama, 1 olarak ayarlanmış en yüksek bitin numarasını, bundan daha düşük olan ve aynı zamanda 1 olarak ayarlanmış ek ardışık bitlerle birlikte göndererek bu tasarım hedeflerini gerçekleştirir. Bundan sonra, yer varsa, bundan daha düşük olan ardışık 0 bit ve ardışık 1 bit sayısını belirten bir veya daha fazla "aralık". Daha fazla bilgi için QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) bölüm 13.2.3'e bakın.

Örnekler:

- prologue: 16 bayt "PeerTestValidate", null ile sonlandırılmamış (mesajda dahil değil)
- bhash: Bob'un 32 baytlık router hash'i (mesajda dahil değil)
- ahash: Alice'in 32 baytlık router hash'i (Sadece 3. ve 4. mesajların imzasında kullanılır; 3. veya 4. mesajda dahil değil)
- ver: 1 bayt SSU sürümü
- nonce: 4 bayt test nonce
- timestamp: 4 bayt zaman damgası (saniye)
- asz: 1 bayt endpoint (port + IP) boyutu (6 veya 18)
- AlicePort: 2 bayt Alice'in port numarası
- Alice IP: (asz - 2) bayt Alice IP adresi

#### Relay Etiketi

Sadece paket 10'u ACK'lemek istiyoruz:

```
+----+----+----+----+----+----+----+----+
| 11 |  size   |      TBD               |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 11
size :: 2 bytes, big endian, size of data to follow
```
#### Yeni Token

Yalnızca 8-10 paketlerini ACK'lemek istiyoruz:

10 9 8 6 5 2 1 0'ı ACK'lemek ve 7 4 3'ü NACK'lemek istiyoruz. ACK Block'un kodlaması:

- Onaylanmış paketleri temsil eden bir bit dizisi olan "bitfield"ı verimli bir şekilde kodlamak istiyoruz.
- Bitfield çoğunlukla 1'lerden oluşur. Hem 1'ler hem de 0'lar genellikle ardışık "kümeler" halinde gelir.
- Pakette ack'ler için mevcut alan miktarı değişkendir.
- En önemli bit en yüksek numaralı olandır. Düşük numaralı olanlar daha az önemlidir. En yüksek bitten belirli bir mesafenin altında, en eski bitler "unutulacak" ve bir daha asla gönderilmeyecektir.

Notlar:

```
+----+----+----+----+----+----+----+----+
| 12 |  size   |    Ack Through    |acnt|
+----+----+----+----+----+----+----+----+
|  range  |  range  |     .   .   .     |
+----+----+----+----+                   +
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 12
size :: 2 bytes, big endian, size of data to follow,
        5 minimum
ack through :: highest packet number acked
acnt :: number of acks lower than ack through also acked,
        0-255
range :: If present,
         1 byte nack count followed by 1 byte ack count,
         0-255 each
```
2 bayt port ve 4 veya 16 bayt IP adresi. Alice'in adresi, Bob tarafından Alice'e gönderilen, veya Bob'un adresi, Alice tarafından Bob'a gönderilen.

Bu, Alice tarafından Session Request, Session Confirmed veya Data mesajında gönderilebilir. Session Created mesajında desteklenmez, çünkü Bob henüz Alice'in RI'sine sahip değildir ve Alice'in relay destekleyip desteklemediğini bilmez. Ayrıca, Bob gelen bir bağlantı alıyorsa, muhtemelen introducers'lara ihtiyacı yoktur (belki diğer tür ipv4/ipv6 için hariç).

- Ack Through: 10
- acnt: 0
- hiçbir aralık dahil edilmemiş

Session Request içinde gönderildiğinde, Bob Session Created mesajında bir Relay Tag ile yanıt verebilir veya Alice'in kimliğini doğrulamak için Session Confirmed içinde Alice'in RouterInfo'sunu almayı bekleyip Data mesajında yanıt vermeyi seçebilir. Bob Alice için relay yapmak istemiyorsa, Relay Tag bloğu göndermez.

- Ack Through: 10
- acnt: 2
- hiçbir aralık dahil edilmedi

Bu, Alice'in Relay Tag Request'ine yanıt olarak Bob tarafından bir Session Confirmed veya Data mesajında gönderilebilir.

- Ack Through: 10
- acnt: 2 (ack 9 8)
- range: 1 2 (nack 7, ack 6 5)
- range: 2 3 (nack 4 3, ack 2 1 0)

Relay Tag Request, Session Request içinde gönderildiğinde, Bob Session Created mesajında bir Relay Tag ile yanıt verebilir veya Alice'in kimliğini doğrulamak için Session Confirmed'da Alice'in RouterInfo'sunu almayı bekleyip bir Data mesajında yanıt vermeyi seçebilir. Bob, Alice için relay yapmak istemiyorsa, Relay Tag bloğu göndermez.

- Aralıklar mevcut olmayabilir. Maksimum aralık sayısı belirtilmemiştir, pakete sığacak kadar olabilir.
- 255'ten fazla ardışık paketi onaylıyorsa range nack sıfır olabilir.
- 255'ten fazla ardışık paketi reddetıyorsa range ack sıfır olabilir.
- Range nack ve ack'in ikisi birden sıfır olamaz.
- Son aralıktan sonra, paketler ne onaylanır ne de reddedilir. Ack bloğunun uzunluğu ve eski ack/nack'lerin nasıl işleneceği ack bloğunu gönderenin sorumluluğundadır. Tartışma için aşağıdaki ack bölümlerine bakınız.
- Ack through alınan en yüksek paket numarası olmalıdır ve daha yüksek paketler alınmamış olmalıdır. Ancak, sınırlı durumlarda, "bir boşluğu dolduran" tek bir paketi onaylamak veya alınan tüm paketlerin durumunu korumayan basitleştirilmiş bir uygulama gibi durumlarda daha düşük olabilir. Alınan en yüksek paketin üzerinde, paketler ne onaylanır ne de reddedilir, ancak birkaç ack bloğundan sonra hızlı yeniden gönderim moduna geçmek uygun olabilir.
- Bu format QUIC'teki formatın basitleştirilmiş bir versiyonudur. Çok sayıda ACK'i NACK patlamalarıyla birlikte verimli bir şekilde kodlamak için tasarlanmıştır.
- ACK blokları veri fazı paketlerini onaylamak için kullanılır. Bunlar yalnızca oturum içi veri fazı paketleri için dahil edilmelidir.

#### Yol Zorluğu

Sonraki bir bağlantı için. Genellikle Session Created ve Session Confirmed mesajlarında bulunur. Önceki token süresi dolarsa, uzun süreli bir oturumun Data mesajında da tekrar gönderilebilir.

```
+----+----+----+----+----+----+----+----+
| 13 | 6 or 18 |   Port  | IP Address    
+----+----+----+----+----+----+----+----+
     |
+----+

blk :: 13
size :: 2 bytes, big endian, 6 or 18
port :: 2 bytes, big endian
ip :: 4 byte IPv4 or 16 byte IPv6 address,
      big endian (network byte order)
```
#### Yol Yanıtı

Path Response içinde geri döndürülmek üzere rastgele veri içeren bir Ping, keep-alive olarak veya bir IP/Port değişikliğini doğrulamak için kullanılır.

Notlar:

```
+----+----+----+
| 15 |    0    |
+----+----+----+

blk :: 15
size :: 2 bytes, big endian, value = 0
```
#### İlk Paket Numarası

Path Challenge'da alınan verilerle birlikte bir Pong, Path Challenge'a yanıt olarak, keep-alive olarak veya bir IP/Port değişikliğini doğrulamak için kullanılır.

İsteğe bağlı olarak her yönde el sıkışmaya dahil edilir, gönderilecek ilk paket numarasını belirtmek için. Bu, TCP'ye benzer şekilde başlık şifrelemesi için daha fazla güvenlik sağlar.

```
+----+----+----+----+----+----+----+
| 16 |    4    |    relay tag      |
+----+----+----+----+----+----+----+

blk :: 16
size :: 2 bytes, big endian, value = 4
relay tag :: 4 bytes, big endian, nonzero
```
#### Tıkanıklık

Tam olarak belirtilmemiş, şu anda desteklenmiyor.

```
+----+----+----+----+----+----+----+----+
| 17 |   12    |     expires       |
+----+----+----+----+----+----+----+----+
                token              |
+----+----+----+----+----+----+----+

blk :: 17
size :: 2 bytes, big endian, value = 12
expires :: Unix timestamp, unsigned seconds.
           Wraps around in 2106
token :: 8 bytes, big endian
```
#### Doldurma

Bu blok, tıkanıklık kontrolü bilgilerini değiş tokuş etmek için genişletilebilir bir yöntem olarak tasarlanmıştır. Tıkanıklık kontrolü karmaşık olabilir ve protokolü canlı testlerde daha fazla deneyimlediğimizde veya tam dağıtımdan sonra gelişebilir.

```
+----+----+----+----+----+----+----+----+
| 18 |  size   |    Arbitrary Data      |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 18
size :: 2 bytes, big endian, size of data to follow
data :: Arbitrary data to be returned in a Path Response
        length as selected by sender
```
Bu, yoğun kullanılan I2NP, First Fragment, Followon Fragment ve ACK bloklarında herhangi bir tıkanıklık bilgisini dışarıda tutar, çünkü bu bloklarda flag'ler için ayrılmış alan yoktur. Data paket başlığında üç byte kullanılmayan flag alanı olsa da, bu da genişletilebilirlik için sınırlı alan sağlar ve daha zayıf şifreleme koruması sunar.

- Rastgele veri içeren minimum 8 bayt veri boyutu önerilir ancak zorunlu değildir.
- Maksimum boyut belirtilmemiştir, ancak yol doğrulama aşamasında PMTU 1280 olduğu için 1280'in oldukça altında olmalıdır.
- Büyük challenge boyutları, paket amplifikasyon saldırıları için bir vektör olabileceği için önerilmez.

#### Eş Adres Sahtekarlığı

İki bit bilgi için 4 baytlık bir blok kullanmak biraz israf olsa da, bunu ayrı bir blokta tutarak, mevcut pencere boyutları, ölçülen RTT veya diğer bayraklar gibi ek verilerle kolayca genişletebiliriz. Deneyim göstermiştir ki yalnızca bayrak bitleri, gelişmiş tıkanıklık kontrolü şemalarının uygulanması için genellikle yetersiz ve sakardır. Örneğin ACK bloğuna herhangi bir olası tıkanıklık kontrolü özelliği için destek eklemeye çalışmak, alan israfına neden olur ve o bloğun ayrıştırılmasına karmaşıklık katar.

```
+----+----+----+----+----+----+----+----+
| 19 |  size   |                        |
+----+----+----+                        +
|    Data received in Path Challenge    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 19
size :: 2 bytes, big endian, size of data to follow
data :: As received in a Path Challenge
```
#### Yol Üzerinde Adres Sahteciliği

Uygulamalar, bu spesifikasyonun gelecekteki bir sürümü tarafından uygulama gerekli kılınmadıkça, diğer router'ın burada yer alan herhangi bir özel bayrak bitini veya özelliği desteklediğini varsaymamalıdır.

Bu blok muhtemelen payload'daki son padding olmayan blok olmalıdır.

```
+----+----+----+----+----+----+----+
| 20 |  size   |  First pkt number |
+----+----+----+----+----+----+----+

blk :: 20
size :: 4
pkt num :: The first packet number to be sent in the data phase
```
#### Yol Dışı Paket Yönlendirme

Bu, AEAD yüklerinin içindeki dolgu için kullanılır. Tüm mesajlar için dolgu, AEAD yüklerinin içindedir.

Padding, müzakere edilen parametrelere kabaca uymalıdır. Bob, istenen tx/rx min/max parametrelerini Session Created içinde gönderdi. Alice, istenen tx/rx min/max parametrelerini Session Confirmed içinde gönderdi. Güncellenmiş seçenekler veri aşamasında gönderilebilir. Yukarıdaki options blok bilgilerine bakın.

Eğer mevcutsa, bu payload'daki son blok olmalıdır.

Notlar:

SSU2, bir saldırgan tarafından yeniden oynatılan mesajların etkisini en aza indirmek için tasarlanmıştır.

```
+----+----+----+----+
| 21 |  size   |flag|
+----+----+----+----+

blk :: 21
size :: 1 (or more if extended)
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 1 to request immediate ack
       bit 1: 1 for explicit congestion notification (ECN)
       bits 7-2: Unused, set to 0 for future compatibility
```
#### Gizlilik Etkileri

Token Request, Retry, Session Request, Session Created, Hole Punch ve oturum-dışı Peer Test mesajları DateTime blokları içermelidir.

Hem Alice hem de Bob, bu mesajların zamanının geçerli bir sapma içinde olduğunu doğrular (önerilen +/- 2 dakika). "Probing resistance" için Bob, sapma geçersizse Token Request veya Session Request mesajlarına yanıt vermemelidir, çünkü bu mesajlar bir tekrar saldırısı veya probing saldırısı olabilir.

Bob, geçerli bir skew olsa bile, Bloom filtresi veya başka bir mekanizma aracılığıyla yinelenen Token Request ve Retry mesajlarını reddetmeyi seçebilir. Ancak, bu mesajlara yanıt vermenin boyut ve CPU maliyeti düşüktür. En kötü durumda, tekrar oynatılan bir Token Request mesajı, daha önce gönderilmiş bir token'ı geçersiz kılabilir.

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
Token sistemi, tekrarlanan Session Request mesajlarının etkisini büyük ölçüde en aza indirir. Tokenlar yalnızca bir kez kullanılabildiğinden, tekrarlanan bir Session Request mesajı asla geçerli bir tokena sahip olamaz. Bob, sapma geçerli olsa bile, Bloom filter veya başka bir mekanizma aracılığıyla yinelenen Session Request mesajlarını reddetmeyi seçebilir. Ancak, bir Retry mesajıyla yanıt vermenin boyut ve CPU maliyeti düşüktür. En kötü durumda, bir Retry mesajı göndermek daha önce gönderilmiş bir tokenı geçersiz kılabilir.

- Boyut = 0 değerine izin verilir.
- Doldurma stratejileri henüz belirlenmemiştir.
- Minimum doldurma henüz belirlenmemiştir.
- Sadece doldurma içeren yükler (payload) izin verilir.
- Doldurma varsayılanları henüz belirlenmemiştir.
- Doldurma parametresi müzakeresi için seçenekler bloğuna bakın
- Min/maks doldurma parametreleri için seçenekler bloğuna bakın
- MTU'yu aşmayın. Daha fazla doldurma gerekiyorsa, birden çok mesaj gönderin.
- Router'ın müzakere edilen doldurma ihlali durumundaki tepkisi implementasyona bağlıdır.
- Doldurma uzunluğu ya mesaj bazında karar verilecek ve uzunluk dağılımının tahminleri yapılacak, ya da rastgele gecikmeler eklenecektir. Bu karşı önlemler DPI'ye (Derin Paket İncelemesi) karşı direnmek için dahil edilecektir, çünkü mesaj boyutları aksi takdirde taşıma protokolü tarafından I2P trafiğinin taşındığını ortaya çıkarır. Tam doldurma şeması gelecekteki çalışmaların alanıdır, [NTCP2](/docs/specs/ntcp2) Ek A bu konuda daha fazla bilgi sağlar.

## Yeniden Oynatma Önleme

Çoğaltılmış Session Created ve Session Confirmed mesajları doğrulanmayacaktır çünkü Noise handshake durumu onları şifrelemek için doğru durumda olmayacaktır. En kötü durumda, bir peer görünürde çoğaltılmış bir Session Created'a yanıt olarak bir Session Confirmed'ı yeniden iletebilir.

Yeniden oynatılan Hole Punch ve Peer Test mesajları çok az etkiye sahip olmalı veya hiç etkisi olmamalıdır.

Router'lar, yinelenen veri fazı mesajlarını tespit etmek ve atmak için veri mesajı paket numarasını kullanmalıdır. Her paket numarası yalnızca bir kez kullanılmalıdır. Yeniden oynatılan mesajlar göz ardı edilmelidir.

Alice tarafından Session Created veya Retry alınmazsa:

Aynı kaynak ve bağlantı ID'lerini, geçici anahtarı ve 0 paket numarasını koruyun. Ya da sadece aynı şifrelenmiş paketi tutun ve yeniden gönderin. Paket numarası artırılmamalıdır, çünkü bu Session Created mesajını şifrelemek için kullanılan zincirleme hash değerini değiştirir.

Önerilen yeniden iletim aralıkları: 1.25, 2.5 ve 5 saniye (ilk gönderimden sonra 1.25, 3.75 ve 8.75 saniye). Önerilen zaman aşımı: toplam 15 saniye

Eğer Bob tarafından Session Confirmed alınmazsa:

Aynı kaynak ve bağlantı ID'lerini, geçici anahtarı ve 0 paket numarasını koruyun. Ya da sadece şifrelenmiş paketi saklayın. Paket numarası artırılmamalıdır, çünkü bu Session Confirmed mesajını şifrelemek için kullanılan zincirleme hash değerini değiştirir.

## Handshake Yeniden İletimi

### Oturum Oluşturuldu

Önerilen yeniden iletim aralıkları: 1, 2 ve 4 saniye (ilk gönderimden sonra 1, 3 ve 7 saniye). Önerilen zaman aşımı: toplam 12 saniye

SSU 1'de Alice, Bob'tan ilk veri paketi alınana kadar veri aşamasına geçmez. Bu, SSU 1'i iki-gidiş-dönüş kurulum yapar.

SSU 2 için, Önerilen Session Confirmed yeniden iletim aralıkları: 1.25, 2.5 ve 5 saniye (ilk gönderimden sonra 1.25, 3.75 ve 8.75 saniye).

### Oturum Onaylandı

Birkaç alternatif vardır. Hepsi 1 RTT'dir:

1) Alice, Session Confirmed'in alındığını varsayar, veri mesajlarını hemen gönderir, Session Confirmed'i asla yeniden iletmez. Sıra dışı alınan veri paketleri (Session Confirmed'den önce) şifrelenemez durumda olacak, ancak yeniden iletilecektir. Session Confirmed kaybolursa, gönderilen tüm veri mesajları düşürülecektir. 2) 1'deki gibi, veri mesajlarını hemen gönder, ancak bir veri mesajı alınana kadar Session Confirmed'i de yeniden ilet. 3) XK yerine IK kullanabiliriz, çünkü handshake'te yalnızca iki mesaj var, ancak ekstra bir DH kullanır (3 yerine 4).

Önerilen uygulama seçenek 2)'dir. Alice, Session Confirmed mesajını yeniden iletmek için gerekli bilgileri saklamalıdır. Alice ayrıca Session Confirmed mesajı yeniden iletildikten sonra tüm Data mesajlarını da yeniden iletmelidir.

### Token İsteği

Session Confirmed yeniden iletilirken, aynı kaynak ve bağlantı ID'lerini, geçici anahtarı ve paket numarası 1'i koruyun. Ya da sadece şifrelenmiş paketi saklayın. Paket numarası artırılmamalıdır, çünkü bu split() fonksiyonu için girdi olan zincirleme hash değerini değiştirir.

Bob, Session Confirmed mesajından önce aldığı veri mesajlarını saklayabilir (kuyruğa alabilir). Session Confirmed mesajı alınmadan önce ne başlık koruma anahtarları ne de şifre çözme anahtarları mevcut olduğundan, Bob bunların veri mesajları olduğunu bilemez, ancak bu varsayılabilir. Session Confirmed mesajı alındıktan sonra, Bob kuyruktaki Veri mesajlarını şifreleyip işleyebilir. Bu çok karmaşıksa, Bob şifresi çözülemeyen Veri mesajlarını bırakabilir, çünkü Alice bunları yeniden iletecektir.

Not: Eğer oturum onaylandı paketleri kaybolursa, Bob oturum oluşturuldu paketini yeniden iletecektir. Oturum oluşturuldu başlığı Alice'in intro key'i ile şifrelemesi çözülemeyecektir, çünkü Bob'un intro key'i ile ayarlanmıştır (Bob'un intro key'i ile geri dönüş şifre çözme işlemi gerçekleştirilmedikçe). Bob, daha önce onaylanmamışsa oturum onaylandı paketlerini hemen yeniden iletebilir ve şifresi çözülemeyen bir paket alındığında da bu durumu gerçekleştirebilir.

Alice tarafından hiçbir Retry alınmazsa:

Aynı kaynak ve bağlantı ID'lerini koruyun. Bir uygulama yeni rastgele paket numarası oluşturabilir ve yeni bir paket şifreleyebilir; Ya da aynı paket numarasını yeniden kullanabilir veya sadece aynı şifreli paketi tutup yeniden iletebilir. Paket numarası artırılmamalıdır, çünkü bu Session Created mesajını şifrelemek için kullanılan zincirleme hash değerini değiştirecektir.

Önerilen yeniden gönderim aralıkları: 3 ve 6 saniye (ilk gönderimden sonra 3 ve 9 saniye). Önerilen zaman aşımı: toplam 15 saniye

Bob tarafından Session Confirmed alınmazsa:

Retry mesajı, sahte kaynak adreslerinin etkilerini azaltmak için zaman aşımında yeniden iletilmez.

### Yeniden Dene

Ancak, orijinal (geçersiz) token ile alınan tekrarlanan Session Request mesajına yanıt olarak veya tekrarlanan Token Request mesajına yanıt olarak bir Retry mesajı yeniden iletilebilir. Her iki durumda da bu, Retry mesajının kaybolduğunu gösterir.

Farklı ancak hala geçersiz bir token ile ikinci bir Session Request mesajı alınırsa, bekleyen oturumu bırakın ve yanıt vermeyin.

Retry mesajını yeniden gönderirken: Aynı kaynak ve bağlantı ID'lerini ve token'ı koruyun. Bir uygulama yeni bir rastgele paket numarası oluşturabilir ve yeni bir paket şifreleyebilir; Veya aynı paket numarasını yeniden kullanabilir ya da sadece aynı şifrelenmiş paketi koruyup yeniden iletebilir.

### Toplam Zaman Aşımı

Handshake için önerilen toplam zaman aşımı 20 saniyedir.

Üç Noise el sıkışma mesajının Session Request, Session Created ve Session Confirmed kopyaları, başlığın MixHash() işleminden önce tespit edilmelidir. Noise AEAD işleminin bundan sonra muhtemelen başarısız olacağı varsayılsa da, el sıkışma hash'i zaten bozulmuş olacaktır.

Üç mesajdan herhangi biri bozulur ve AEAD başarısız olursa, bozuk mesaj üzerinde MixHash() zaten çağrıldığı için handshake daha sonra yeniden iletimle bile kurtarılamaz.

Session Request başlığındaki Token, DoS saldırılarını azaltmak, kaynak adres sahtekarlığını önlemek ve tekrar oynatma saldırılarına karşı direnç sağlamak için kullanılır.

Eğer Bob, Session Request mesajındaki token'ı kabul etmezse, Bob mesajı decrypt etmez, çünkü bu pahalı bir DH işlemi gerektirir. Bob sadece yeni bir token ile bir Retry mesajı gönderir.

### Yinelemeler ve Hata İşleme

Daha sonra bu token ile bir Session Request mesajı alınırsa, Bob bu mesajı şifrelemesini çözer ve handshake ile devam eder.

### Paket Numaraları

Token, token üreticisi değerleri ve ilişkili IP ve port bilgilerini (bellekte veya kalıcı olarak) saklıyorsa, rastgele oluşturulmuş 8 byte'lık bir değer olmalıdır. Üretici, bellek içinde saklanması gerekmeyen tokenlar oluşturmak için IP, port ve mevcut saat veya gün bilgilerinin SipHash'ini (gizli seed K0, K1 ile) kullanarak opak bir değer oluşturamaz, çünkü bu yöntem yeniden kullanılan tokenları ve replay saldırılarını reddetmeyi zorlaştırır. Ancak, [WireGuard](https://www.wireguard.com/papers/wireguard.pdf)'ın yaptığı gibi sunucu sırrı ve IP adresinin 16-byte'lık HMAC'ini kullanarak böyle bir şemaya geçip geçemeyeceğimiz ileri çalışma konusudur.

Token'lar yalnızca bir kez kullanılabilir. Bob'dan Alice'e bir Retry mesajında gönderilen bir token hemen kullanılmalıdır ve birkaç saniye içinde süresi dolar. Kurulmuş bir oturumda New Token bloğunda gönderilen bir token sonraki bağlantıda kullanılabilir ve bu bloğunda belirtilen zamanda süresi dolar. Süre dolma zamanı gönderen tarafından belirtilir; önerilen değerler, saklanan token'ların istenen maksimum ek yüküne bağlı olarak minimum birkaç dakika, maksimum bir veya daha fazla saattir.

## Token'lar

Bir router'ın IP'si veya portu değişirse, eski IP veya port için kaydedilen tüm tokenları (hem gelen hem giden) silmesi gerekir, çünkü artık geçerli değillerdir. Tokenlar isteğe bağlı olarak router yeniden başlatmaları arasında saklanabilir, bu uygulama bağımlıdır. Süresi dolmamış bir token'ın kabul edilmesi garanti edilmez; eğer Bob kaydettiği tokenları unutmuş veya silmişse, Alice'e bir Retry gönderecektir. Bir router token depolamayı sınırlamayı seçebilir ve süresi dolmamış olsa bile en eski saklanan tokenları kaldırabilir.

Yeni Token blokları Alice'den Bob'a veya Bob'dan Alice'e gönderilebilir. Bunlar tipik olarak oturum kurulumu sırasında veya kısa süre sonrasında en az bir kez gönderilirler. Session Confirmed mesajındaki RouterInfo'nun doğrulama kontrollerinden dolayı, Bob, Session Created mesajında Yeni Token bloğu göndermemelidir; bu blok, Session Confirmed alındıktan ve doğrulandıktan sonra ACK 0 ve Router Info ile birlikte gönderilebilir.

Oturum yaşam süreleri genellikle token süresi dolma süresinden daha uzun olduğundan, token süresi dolmadan önce veya sonra yeni bir sona erme süresi ile yeniden gönderilmeli veya yeni bir token gönderilmelidir. Router'lar yalnızca alınan son token'ın geçerli olduğunu varsaymalıdır; aynı IP/port için birden fazla gelen veya giden token saklama zorunluluğu yoktur.

Bir token, kaynak IP/port ve hedef IP/port kombinasyonuna bağlıdır. IPv4 üzerinden alınan bir token IPv6 için kullanılamaz veya tam tersi geçerlidir.

Oturum sırasında herhangi bir peer yeni bir IP veya porta geçiş yaparsa (Connection Migration bölümüne bakınız), daha önce değiş tokuş edilen tüm token'lar geçersiz hale gelir ve yeni token'lar değiş tokuş edilmelidir.

Uygulamalar token'ları diske kaydedebilir ve yeniden başlatmada bunları yeniden yükleyebilir, ancak bu zorunlu değildir. Eğer kalıcı hale getirilirse, uygulama bunları yeniden yüklemeden önce kapatma işleminden bu yana IP ve port'un değişmediğinden emin olmalıdır.

SSU 1'den Farkları

Not: SSU 1'de olduğu gibi, ilk fragment toplam fragment sayısı veya toplam uzunluk hakkında bilgi içermez. Takip eden fragmentlar kendi ofset bilgilerini içermez. Bu, gönderene paketteki mevcut alana göre "anında" fragmentlama esnekliği sağlar. (Java I2P bunu yapmaz; ilk fragment gönderilmeden önce "ön-fragmentlama" yapar) Ancak bu, alıcıyı sıra dışı alınan fragmentları saklamak ve tüm fragmentlar alınana kadar yeniden birleştirmeyi geciktirmek zorunda bırakır.

SSU 1'de olduğu gibi, parçaların herhangi bir yeniden iletimi, parçanın önceki iletiminin uzunluğunu (ve örtük ofsetini) korumalıdır.

SSU 2, işleme verimliliğini artırmak için üç durumu (tam mesaj, ilk parça ve takip eden parça) üç farklı blok türüne ayırır.

Bu protokol I2NP mesajlarının yinelenen teslimatını tamamen engellemez. IP katmanı kopyaları veya tekrar saldırıları SSU2 katmanında tespit edilecektir, çünkü her paket numarası yalnızca bir kez kullanılabilir.

## I2NP Mesaj Parçalama

Ancak I2NP mesajları veya parçaları yeni paketlerde yeniden iletildiğinde, bu SSU2 katmanında tespit edilemez. Router, I2NP son kullanma tarihini (hem çok eski hem de gelecekte çok ileri tarihli) zorlamalı ve I2NP mesaj kimliğine dayalı olarak Bloom filtresi veya başka bir mekanizma kullanmalıdır.

Router tarafından veya SSU2 implementasyonunda, kopyaları tespit etmek için ek mekanizmalar kullanılabilir. Örneğin, SSU2 yakın zamanda alınan mesaj ID'lerinin bir önbelleğini tutabilir. Bu implementasyona bağlıdır.

Bu spesifikasyon, paket numaralandırma ve ACK blokları için protokolü belirtir. Bu, bir vericinin verimli ve duyarlı bir tıkanıklık kontrol algoritması uygulaması için yeterli gerçek zamanlı bilgi sağlarken, bu uygulamada esneklik ve yeniliğe izin verir. Bu bölüm uygulama hedeflerini tartışır ve öneriler sunar. Genel rehberlik [RFC-9002](https://tools.ietf.org/html/rfc9002)'de bulunabilir. Yeniden iletim zamanlayıcıları konusunda rehberlik için ayrıca [RFC-6298](https://tools.ietf.org/html/rfc6298)'e bakın.

Yalnızca ACK içeren veri paketleri, uçuştaki bayt veya paket sayımına dahil edilmemeli ve tıkanıklık kontrolüne tabi tutulmamalıdır. TCP'den farklı olarak, SSU2 bu paketlerin kaybını tespit edebilir ve bu bilgi tıkanıklık durumunu ayarlamak için kullanılabilir. Ancak, bu belge bunu yapmak için bir mekanizma belirtmemektedir.

## I2NP Mesaj Çoğaltma

İstenirse, başka veri olmayan blokları içeren paketler de tıkanıklık kontrolünden hariç tutulabilir, bu uygulama bağımlıdır. Örneğin:

Tıkanıklık kontrolünün, TCP RFC'leri ve QUIC [RFC-9002](https://tools.ietf.org/html/rfc9002) rehberliğini takip ederek paket sayısı değil bayt sayısı temelinde olması önerilir. Çekirdekte veya ara kutularda tampon taşmasını önlemek için ek bir paket sayısı sınırı da yararlı olabilir, bu uygulama bağımlıdır, ancak bu önemli karmaşıklık ekleyebilir. Oturum başına ve/veya toplam paket çıkışı bant genişliği ile sınırlandırılmış ve/veya hızlandırılmışsa, bu paket sayısı sınırlandırması ihtiyacını azaltabilir.

SSU 1'de, ACK'ler ve NACK'ler I2NP mesaj numaralarını ve parça bit maskelerini içeriyordu. Göndericiler, giden mesajların (ve bunların parçalarının) ACK durumunu takip ediyor ve gerektiğinde parçaları yeniden iletiyorlardı.

## Tıkanıklık Kontrolü

SSU 2'de ACK'lar ve NACK'lar paket numaralarını içerir. Gönderenler, paket numaralarını içeriklerine eşleyen bir veri yapısını korumak zorundadır. Bir paket ACK veya NACK alındığında, gönderen o pakette hangi I2NP mesajları ve parçalarının bulunduğunu belirlemeli ve neyi yeniden göndereceğine karar vermelidir.

Bob, 0 paketinin ACK'ını gönderir, bu da Session Confirmed mesajını onaylar ve Alice'in veri aşamasına geçmesine olanak tanır ve olası yeniden iletim için saklanan büyük Session Confirmed mesajını atmasını sağlar. Bu, SSU 1'de Bob tarafından gönderilen DeliveryStatusMessage'ın yerine geçer.

Bob, Session Confirmed mesajını aldıktan sonra mümkün olan en kısa sürede bir ACK göndermelidir. Küçük bir gecikme (50 ms'den fazla olmamak kaydıyla) kabul edilebilir, çünkü Session Confirmed mesajından hemen sonra en az bir Data mesajı gelmeli ve böylece ACK hem Session Confirmed hem de Data mesajını onaylayabilir. Bu, Bob'un Session Confirmed mesajını yeniden göndermek zorunda kalmasını önleyecektir.

- Eş Testi
- Röle isteği/tanıtım/yanıt
- Yol sınaması/yanıt

Tanım: Ack-eliciting paketler: Ack-eliciting bloklar içeren paketler, alıcıdan maksimum onay gecikmesi içinde bir ACK talep eder ve ack-eliciting paketler olarak adlandırılır.

### Oturum Onaylandı ACK

Router'lar aldıkları ve işledikleri tüm paketleri onaylar. Ancak, yalnızca ack-eliciting paketler maksimum ack gecikmesi içinde bir ACK bloğunun gönderilmesine neden olur. Ack-eliciting olmayan paketler yalnızca başka nedenlerle bir ACK bloğu gönderildiğinde onaylanır.

Herhangi bir nedenle paket gönderirken, bir endpoint yakın zamanda gönderilmemişse ACK bloğu dahil etmeye çalışmalıdır. Böyle yapmak, peer'da zamanında kayıp tespit etmeye yardımcı olur.

### ACK'ları Oluşturma

Genel olarak, alıcıdan gelen sık geri bildirim kayıp ve tıkanıklık yanıtını iyileştirir, ancak bu durum her ACK tetikleyici pakete yanıt olarak ACK bloğu gönderen alıcının oluşturduğu aşırı yüke karşı dengelenmelidir. Aşağıda sunulan rehberlik bu dengeyi kurmayı amaçlar.

Aşağıdakiler HARIÇ herhangi bir blok içeren oturum içi veri paketleri ack-eliciting (onay gerektiren) paketlerdir:

### Handshake ACK'ları

Oturum dışı paketler, handshake mesajları ve eş test mesajları 5-7 dahil olmak üzere, kendi onay mekanizmalarına sahiptir. Aşağıya bakın.

Bunlar özel durumlar:

ACK blokları, veri aşaması paketlerini onaylamak için kullanılır. Bunlar yalnızca oturum içi veri aşaması paketleri için dahil edilmelidir.

Her paket en az bir kez onaylanmalı ve onay-tetikleyici paketler maksimum gecikme süresi içinde en az bir kez onaylanmalıdır.

Bir uç nokta, aşağıdaki istisna dışında, tüm onay gerektiren el sıkışma paketlerini maksimum gecikme süresi içinde derhal onaylamalıdır. El sıkışma onayından önce, bir uç nokta paketleri alındığında şifrelemelerini çözmek için paket başlığı şifreleme anahtarlarına sahip olmayabilir. Bu nedenle bunları tamponlayabilir ve gerekli anahtarlar kullanılabilir hale geldiğinde onaylayabilir.

- ACK bloğu
- Adres bloğu
- DateTime bloğu
- Padding bloğu
- Sonlandırma bloğu
- Diğerleri?

Yalnızca ACK blokları içeren paketler tıkanıklık kontrolüne tabi olmadığından, bir uç nokta ack-eliciting (onay gerektiren) paket alımına yanıt olarak bu tür paketlerden birden fazla göndermemelidir.

### ACK Bloklarını Gönderme

Bir endpoint, alınan paketten önce gelen paket boşlukları olsa bile, ack gerektirmeyen bir pakete yanıt olarak ack gerektirmeyen bir paket göndermemelidir. Bu, bağlantının asla boşta kalmasını engelleyebilecek sonsuz bir onaylama geri bildirim döngüsünden kaçınır. Ack gerektirmeyen paketler, endpoint diğer olaylara yanıt olarak bir ACK bloğu gönderdiğinde sonunda onaylanır.

- Token Request, Retry tarafından dolaylı olarak onaylanır
- Session Request, Session Created veya Retry tarafından dolaylı olarak onaylanır
- Retry, Session Request tarafından dolaylı olarak onaylanır
- Session Created, Session Confirmed tarafından dolaylı olarak onaylanır
- Session Confirmed derhal onaylanmalıdır

### ACK Sıklığı

Yalnızca ACK blokları gönderen bir uç nokta, bu onaylar ack-eliciting bloklar içeren paketlere dahil edilmedikçe eş noktasından onay almayacaktır. Bir uç nokta, onaylanacak yeni ack-eliciting paketler olduğunda diğer bloklarla birlikte bir ACK bloğu göndermelidir. Yalnızca ack-eliciting olmayan paketlerin onaylanması gerektiğinde, bir uç nokta ack-eliciting bir paket alınana kadar giden bloklarla birlikte ACK bloğu göndermemeyi seçebilir.

Yalnızca ack-eliciting olmayan paketler gönderen bir uç nokta, bir onay aldığından emin olmak için bu paketlere zaman zaman bir ack-eliciting blok eklemeyi seçebilir. Bu durumda, sonsuz bir onay geri bildirim döngüsünden kaçınmak için, bir uç nokta aksi takdirde ack-eliciting olmayacak tüm paketlerde bir ack-eliciting blok göndermemelidir.

Göndericide kayıp tespitine yardımcı olmak için, bir uç nokta aşağıdaki durumlardan herhangi birinde ack-eliciting paket aldığında gecikme olmaksızın bir ACK bloğu oluşturmalı ve göndermelidir:

Algoritmaların, yukarıda sunulan rehberliği takip etmeyen alıcılara karşı dayanıklı olması beklenir. Ancak, bir uygulama bu gereksinimlerden yalnızca bir değişikliğin performans etkilerini - hem endpoint tarafından yapılan bağlantılar hem de ağın diğer kullanıcıları için - dikkatli bir şekilde değerlendirdikten sonra sapmalıdır.

Bir alıcı, onay gerektiren paketlere yanıt olarak ne sıklıkta onay göndereceğini belirler. Bu belirleme bir denge kurma işlemini içerir.

Uç noktalar kayıpları tespit etmek için zamanında onay almaya dayanır. Pencere tabanlı tıkanıklık denetleyicileri, tıkanıklık pencerelerini yönetmek için onayları kullanır. Her iki durumda da onayları geciktirmek performansı olumsuz etkileyebilir.

Öte yandan, sadece onaylamaları taşıyan paketlerin sıklığının azaltılması, her iki uç noktada da paket iletimi ve işleme maliyetini azaltır. Bu, ciddi şekilde asimetrik bağlantılarda bağlantı verim hızını iyileştirebilir ve dönüş yolu kapasitesini kullanan onaylama trafiği hacmini azaltabilir; bkz. [RFC-3449](https://tools.ietf.org/html/rfc3449)'un Bölüm 3'ü.

Bir alıcı, en az iki ACK gerektiren paket aldıktan sonra bir ACK bloğu göndermelidir. Bu öneri genel niteliktedir ve TCP uç nokta davranışı için önerilerle tutarlıdır [RFC-5681](https://tools.ietf.org/html/rfc5681). Ağ koşulları hakkındaki bilgi, eşin tıkanıklık denetleyicisi hakkındaki bilgi veya daha fazla araştırma ve deneyim, daha iyi performans özelliklerine sahip alternatif onaylama stratejileri önerebilir.

- Alınan paketin paket numarası, daha önce alınmış başka bir ack-eliciting paketin numarasından küçük olduğunda
- Paketin numarası, alınmış en yüksek numaralı ack-eliciting paketin numarasından büyük olduğunda ve o paket ile bu paket arasında eksik paketler bulunduğunda
- Paket başlığındaki ack-immediate bayrağı ayarlandığında

Bir alıcı, yanıt olarak bir ACK bloğu gönderip göndermeyeceğini belirlemeden önce birden fazla mevcut paketi işleyebilir. Genel olarak, alıcı bir ACK'yi RTT / 6'dan veya maksimum 150 ms'den daha fazla geciktirmemelidir.

### Anında ACK Bayrağı

Veri paketi başlığındaki ack-immediate bayrağı, alıcının paketi aldıktan kısa süre sonra, muhtemelen birkaç ms içinde bir onay göndermesi isteğidir. Genel olarak, alıcı anlık bir ACK'yi RTT / 16'dan veya maksimum 5 ms'den fazla geciktirmemelidir.

Alıcı, gönderenin gönderme pencere boyutunu bilmez ve bu nedenle ACK göndermeden önce ne kadar gecikme yapacağını bilemez. Veri paketi başlığındaki anında ACK bayrağı, etkili RTT'yi en aza indirerek maksimum verimliliği korumak için önemli bir yoldur. Anında ACK bayrağı, başlık bayt 13, bit 0'dır, yani (header[13] & 0x01). Ayarlandığında, anında ACK talep edilir. Ayrıntılar için yukarıdaki kısa başlık bölümüne bakınız.

Bir gönderenin immediate-ack bayrağını ne zaman ayarlayacağını belirlemek için kullanabileceği birkaç olası strateji vardır:

Anında ACK bayrakları yalnızca I2NP mesajları veya mesaj parçaları içeren veri paketlerinde gerekli olmalıdır.

Bir ACK bloğu gönderildiğinde, onaylanmış paketlerin bir veya daha fazla aralığı dahil edilir. Eski paketler için onaylamaların dahil edilmesi, daha büyük ACK blokları pahasına, daha önce gönderilen ACK bloklarının kaybolması nedeniyle oluşan sahte yeniden iletimlerin olasılığını azaltır.

ACK blokları her zaman en son alınan paketleri onaylamalıdır ve paketler ne kadar düzensizse, karşı tarafın bir paketi kayıp olarak ilan etmesini ve içerdiği blokları gereksiz yere yeniden iletmesini önlemek için güncellenmiş bir ACK bloğunu hızlıca göndermek o kadar önemlidir. Bir ACK bloğu tek bir paketin içine sığmalıdır. Eğer sığmıyorsa, eski aralıklar (en küçük paket numaralarına sahip olanlar) çıkarılır.

### ACK Blok Boyutu

Bir alıcı, hem ACK bloklarının boyutunu sınırlamak hem de kaynak tükenmesini önlemek için hatırladığı ve ACK bloklarında gönderdiği ACK aralıklarının sayısını sınırlar. Bir ACK bloğu için onaylar aldıktan sonra, alıcı bu onaylanmış ACK aralıklarını takip etmeyi bırakmalıdır. Gönderenler çoğu paket için onay bekleyebilir, ancak bu protokol alıcının işlediği her paket için onay alınacağını garanti etmez.

Çok sayıda ACK aralığının tutulması, bir ACK bloğunun çok büyük hale gelmesine neden olabilir. Bir alıcı, ACK blok boyutunu sınırlamak için onaylanmamış ACK Aralıklarını atabilir, ancak bu durumda gönderenden artan yeniden iletimlere katlanmak zorundadır. Eğer bir ACK bloğu bir pakete sığmayacak kadar büyükse bu gereklidir. Alıcılar ayrıca diğer bloklar için yer ayırmak veya onaylamaların tükettiği bant genişliğini sınırlamak amacıyla ACK blok boyutunu daha da sınırlandırabilir.

- Her N pakette bir kez ayarlanır, küçük bir N için
- Bir paket patlamasındaki son pakette ayarlanır
- Gönderme penceresi neredeyse dolduğunda ayarlanır, örneğin 2/3'ünden fazla dolu olduğunda
- Yeniden iletilen fragmanları olan tüm paketlerde ayarlanır

Bir alıcı, o aralıktaki numaralara sahip paketleri sonradan kabul etmeyeceğini garanti edemediği sürece bir ACK aralığını tutmak zorundadır. Aralıklar atıldıkça artan minimum paket numarasını korumak, bunu minimal durum ile başarmanın bir yoludur.

### ACK Bloklarını İzleyerek Aralıkları Sınırlama

Alıcılar tüm ACK aralıklarını atabilir, ancak başarıyla işlenmiş en büyük paket numarasını saklamalıdır, çünkü bu sonraki paketlerden paket numaralarını kurtarmak için kullanılır.

Aşağıdaki bölüm, her ACK bloğunda hangi paketlerin onaylanacağını belirlemek için örnek bir yaklaşımı açıklar. Bu algoritmanın amacı işlenen her paket için bir onay oluşturmak olsa da, onayların kaybolması hala mümkündür.

Bir ACK bloğu içeren paket gönderildiğinde, o bloktaki Ack Through alanı kaydedilebilir. Bir ACK bloğu içeren paket onaylandığında, alıcı gönderilen ACK bloğundaki Ack Through alanından küçük veya eşit paketleri onaylamayı durdurabilir.

Yalnızca ACK bloklarında olduğu gibi ack-eliciting olmayan paketler gönderen bir alıcı, uzun süre boyunca bir onay alamayabilir. Bu durum, alıcının çok sayıda ACK bloğu için uzun süre durum bilgisi tutmasına neden olabilir ve gönderdiği ACK blokları gereksiz yere büyük olabilir. Böyle bir durumda, alıcı karşı taraftan bir ACK elde etmek için ara sıra, örneğin her round trip'te bir kez olmak üzere, bir PING veya başka küçük ack-eliciting blok gönderebilir.

ACK blok kaybı olmayan durumlarda, bu algoritma minimum 1 RTT yeniden sıralamasına izin verir. ACK blok kaybı ve yeniden sıralama olan durumlarda, bu yaklaşım her onayın ACK bloğunda artık yer almadığı zamandan önce gönderici tarafından görüldüğünü garanti etmez. Paketler sıra dışında alınabilir ve bunları içeren sonraki tüm ACK blokları kaybolabilir. Bu durumda, kayıp kurtarma algoritması sahte yeniden iletimlere neden olabilir, ancak gönderici ilerlemeye devam edecektir.

I2P taşıma protokolleri I2NP mesajlarının sıralı teslimatını garanti etmez. Bu nedenle, bir veya daha fazla I2NP mesajı veya parçası içeren bir Data mesajının kaybolması diğer I2NP mesajlarının teslim edilmesini ENGELLEMEZ; hat başı engelleme yoktur. Uygulamalar, gönderim penceresi izin veriyorsa kayıp kurtarma aşamasında yeni mesajlar göndermeye devam etmelidir.

Bir gönderici, bir mesajın tam içeriğini aynı şekilde yeniden iletilmek üzere saklamamalıdır (handshake mesajları hariç, yukarıya bakın). Bir gönderici, her mesaj gönderdiğinde güncel bilgiler (ACK'ler, NACK'ler ve onaylanmamış veriler) içeren mesajları oluşturmalıdır. Bir gönderici, mesajlardan gelen bilgileri bir kez onaylandıktan sonra yeniden iletmekten kaçınmalıdır. Bu, kayıp olarak ilan edildikten sonra onaylanan mesajları da içerir, bu durum ağ yeniden sıralaması varlığında gerçekleşebilir.

### Tıkanıklık

TBD. Genel rehberlik [RFC-9002](https://tools.ietf.org/html/rfc9002)'de bulunabilir.

Bir peer'ın IP'si veya portu bir oturum yaşam döngüsü boyunca değişebilir. IP değişikliği IPv6 geçici adres rotasyonu, ISP kaynaklı periyodik IP değişikliği, WiFi ve hücresel IP'ler arasında geçiş yapan mobil istemci veya diğer yerel ağ değişiklikleri nedeniyle olabilir. Port değişikliği, önceki bağlantının zaman aşımına uğramasından sonra NAT yeniden bağlanması nedeniyle olabilir.

Bir peer'ın IP'si veya portu, paket değiştirme veya enjekte etme dahil olmak üzere çeşitli yol üzeri ve yol dışı saldırılar nedeniyle değişmiş gibi görünebilir.

### Yeniden İletim

Bağlantı geçişi, yeni bir kaynak uç noktasının (IP+port) doğrulandığı, aynı zamanda doğrulanmamış değişikliklerin önlendiği süreçtir. Bu süreç, QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000)'de tanımlanan sürümün basitleştirilmiş bir versiyonudur. Bu süreç yalnızca bir oturumun veri aşaması için tanımlanmıştır. Handshake sırasında geçişe izin verilmez. Tüm handshake paketleri, daha önce gönderilen ve alınan paketlerle aynı IP ve port'tan geldiği doğrulanmalıdır. Diğer bir deyişle, handshake sırasında bir peer'ın IP'si ve port'u sabit kalmalıdır.

### Pencere

(QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000)'den uyarlanmıştır)

### Tehdit Modeli

Bir eş, kaynak adresini taklit ederek bir uç noktanın isteksiz bir ana bilgisayara aşırı miktarda veri göndermesine neden olabilir. Uç nokta, taklit eden eşten önemli ölçüde daha fazla veri gönderiyorsa, bağlantı geçişi bir saldırganın bir kurbana yönelik üretebileceği veri hacmini artırmak için kullanılabilir.

## Bağlantı Geçişi

Yol üzerindeki bir saldırgan, sahte bir adresle paketleri kopyalayıp iletebilir ve bu paketin orijinal paketten önce ulaşmasını sağlayarak sahte bir bağlantı geçişine neden olabilir. Sahte adresli paket, geçiş yapan bir bağlantıdan geliyormuş gibi görünecek ve orijinal paket kopya olarak algılanıp atılacaktır. Sahte geçişten sonra kaynak adres doğrulaması başarısız olacaktır çünkü kaynak adresdeki varlık, kendisine gönderilen Path Challenge'ı okumak veya yanıtlamak için gerekli kriptografik anahtarlara sahip değildir, istese bile.

Paketleri gözlemleyebilen yol dışı bir saldırgan, gerçek paketlerin kopyalarını uç noktalara iletebilir. Kopyalanan paket gerçek paketten önce ulaşırsa, bu bir NAT yeniden bağlanması olarak görünür. Herhangi bir gerçek paket, kopya olarak atılır. Saldırgan paketleri iletmeye devam edebilirse, saldırgan üzerinden bir yola geçiş yapmaya neden olabilir. Bu, saldırganı yol üzerine yerleştirir ve ona sonraki tüm paketleri gözlemleme veya düşürme yetisi verir.

QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000), ağ yollarını değiştirirken bağlantı kimliklerinin de değiştirilmesini belirtir. Birden fazla ağ yolunda kararlı bir bağlantı kimliği kullanmak, pasif bir gözlemcinin bu yollar arasındaki aktiviteyi ilişkilendirmesine olanak tanır. Ağlar arasında geçiş yapan bir uç nokta, aktivitelerinin eş dışındaki herhangi bir varlık tarafından ilişkilendirilmesini istemeyebilir. Ancak, QUIC başlıktaki bağlantı kimliklerini şifrelemez. SSU2 bunu yapar, bu nedenle gizlilik sızıntısı, pasif gözlemcinin bağlantı kimliğini şifrelemek için gereken tanıtım anahtarını elde etmek üzere netDb'ye de erişmesini gerektirir. Tanıtım anahtarı ile bile bu güçlü bir saldırı değildir ve SSU2'de geçişten sonra bağlantı kimliklerini değiştirmiyoruz çünkü bu önemli bir karmaşıklık yaratacaktır.

### Yol Doğrulaması Başlatılıyor

Veri aşaması sırasında, eşler alınan her veri paketinin kaynak IP'sini ve portunu kontrol etmelidir. Eğer IP veya port daha önce alınandan farklıysa VE paket tekrar eden bir paket numarası değilse VE paket başarıyla şifre çözülüyorsa, oturum yol doğrulama aşamasına geçer.

#### Tanıtıcı Seçimi

Ek olarak, bir peer yeni IP ve port'un yerel doğrulama kurallarına göre geçerli olduğunu doğrulamalıdır (engellenmiş değil, yasadışı portlar değil, vb.). Peer'lar IPv4 ve IPv6 arasında geçişi desteklemek zorunda DEĞİLDİR ve diğer adres ailesindeki yeni bir IP'yi geçersiz olarak değerlendirebilir, çünkü bu beklenen bir davranış değildir ve önemli uygulama karmaşıklığı ekleyebilir. Geçersiz bir IP/port'tan paket aldığında, bir uygulama bunu basitçe düşürebilir veya eski IP/port ile yol doğrulaması başlatabilir.

#### Yanıt İşleme

Yol doğrulama aşamasına girildiğinde, aşağıdaki adımları izleyin:

#### Tanıtıcılar

Yol doğrulama aşamasında, oturum gelen paketleri işlemeye devam edebilir. İster eski ister yeni IP/port'tan gelsin. Oturum ayrıca veri paketleri göndermeye ve onaylamaya da devam edebilir. Ancak, sahte bir adrese büyük miktarda trafik göndererek hizmet reddi saldırıları için kullanılmasını önlemek amacıyla, yol doğrulama aşamasında tıkanıklık penceresi ve PMTU minimum değerlerde kalmalıdır.

#### Kimlik Gizleme

Bir uygulama, aynı anda birden fazla yolu doğrulamaya çalışabilir, ancak bunu yapmak zorunda değildir. Bu, muhtemelen karmaşıklığa değmez. Önceki bir IP/port'un zaten doğrulanmış olduğunu hatırlayabilir ve bir peer önceki IP/port'una geri dönerse yol doğrulamasını atlayabilir, ancak bunu yapmak zorunda değildir.

### Mesaj İçerikleri

Eğer Path Challenge'da gönderilen verilerle aynı verileri içeren bir Path Response alınırsa, Path Validation başarılı olmuştur. Path Response mesajının kaynak IP/port'unun, Path Challenge'ın gönderildiği adresle aynı olması gerekmez.

Path Response zamanlayıcısı dolmadan önce bir Path Response alınmazsa, başka bir Path Challenge gönder ve Path Response zamanlayıcısını ikiye katla.

Path Validation zamanlayıcısı sona ermeden önce bir Path Response alınmazsa, Path Validation başarısız olmuştur.

- Birkaç saniye veya mevcut RTO'nun birkaç katı kadar bir yol doğrulama zaman aşımı zamanlayıcısı başlat (TBD)
- Tıkanıklık penceresini minimuma düşür
- PMTU'yu minimuma düşür (1280)
- Path Challenge bloğu, Address bloğu (yeni IP/port içeren) ve tipik olarak bir ACK bloğu içeren bir veri paketi gönder, yeni IP ve port'a. Bu paket mevcut oturum ile aynı connection ID ve şifreleme anahtarlarını kullanır. Path Challenge blok verisi yeterli entropi içermeli (en az 8 bayt) böylece taklit edilemez.
- İsteğe bağlı olarak, farklı blok verisi ile eski IP/port'a da bir Path Challenge gönder. Aşağıya bakın.
- Mevcut RTO'ya dayalı bir Path Response zaman aşımı zamanlayıcısı başlat (tipik olarak RTT + RTTdev'in bir katı)

Data mesajları aşağıdaki blokları içermelidir. Padding'in son sırada olması dışında sıralama belirtilmemiştir:

Mesaja başka blokların (örneğin, I2NP) dahil edilmesi önerilmez.

Path Response içeren mesajda Path Challenge bloğu eklenmesine izin verilir, böylece diğer yönde doğrulama başlatılabilir.

Path Challenge ve Path Response blokları ACK-tetikleyicidir. Path Challenge, Path Response ve ACK bloklarını içeren bir Data mesajı ile ACK'lenecektir. Path Response, bir ACK bloğu içeren bir Data mesajı ile ACK'lenmelidir.

QUIC spesifikasyonu, path validation sırasında veri paketlerinin nereye gönderileceği konusunda net değil - eski mi yoksa yeni IP/port'a mı? IP/port değişikliklerine hızla yanıt vermek ile sahte adreslere trafik göndermemek arasında bir denge kurulması gerekiyor. Ayrıca, sahte paketlerin mevcut bir oturumu önemli ölçüde etkilemesine izin verilmemelidir. Yalnızca port değişiklikleri muhtemelen bir boşta kalma süresinden sonra NAT rebinding'inden kaynaklanır; IP değişiklikleri bir veya her iki yönde yoğun trafik aşamaları sırasında gerçekleşebilir.

### Path Validation Sırasında Yönlendirme

Stratejiler araştırma ve iyileştirmeye tabidir. Olasılıklar şunları içerir:

- Path Challenge veya Path Response bloğu. Path Challenge opak veri içerir, minimum 8 bayt önerilir. Path Response, Path Challenge'dan gelen veriyi içerir.
- Alıcının görünen IP'sini içeren Address bloğu
- DateTime bloğu
- ACK bloğu
- Padding bloğu

Bir Path Challenge alındığında, eş, Path Challenge'dan gelen veriyi içeren bir Path Response içerikli veri paketi ile yanıt vermelidir.

Path Response, Path Challenge'ın alındığı IP/port'a gönderilmelidir. Bu, peer için önceden kurulmuş olan IP/port ile MUTLAKA AYNI değildir. Bu, bir peer tarafından yapılan yol doğrulamasının yalnızca yol her iki yönde de işlevsel ise başarılı olmasını sağlar. Aşağıdaki Yerel Değişiklik Sonrası Doğrulama bölümüne bakın.

IP/port, peer için daha önce bilinen IP/port'tan farklı olmadığı sürece, Path Challenge'ı basit bir ping olarak kabul edin ve koşulsuz olarak Path Response ile yanıtlayın. Alıcı, alınan Path Challenge temelinde herhangi bir durum tutmaz veya değiştirmez. IP/port farklıysa, bir peer yeni IP ve port'un yerel doğrulama kurallarına göre geçerli olduğunu doğrulamalıdır (engellenmiş değil, yasak portlar değil, vb.). Peer'ların IPv4 ve IPv6 arasında çapraz adres ailesi yanıtlarını desteklemesi GEREKLİ DEĞİLDİR ve diğer adres ailesindeki yeni bir IP'yi geçersiz olarak kabul edebilir, çünkü bu beklenen bir davranış değildir.

### Path Challenge'a Yanıt Verme

Tıkanıklık kontrolü tarafından kısıtlanmadıkça, Path Response hemen gönderilmelidir. Uygulamalar gerekirse Path Response'ları veya kullanılan bant genişliğini hız sınırlamak için önlemler almalıdır.

Bir Path Challenge bloğu genellikle aynı mesajda bir Address bloğu ile birlikte gelir. Adres bloğu yeni bir IP/port içeriyorsa, bir eş o IP/port'u doğrulayabilir ve o yeni IP/port'un eş testini oturum eşi veya başka herhangi bir eş ile başlatabilir. Eş güvenlik duvarı arkasında olduğunu düşünüyorsa ve sadece port değiştiyse, bu değişiklik muhtemelen NAT yeniden bağlanması nedeniyledir ve daha fazla eş testi muhtemelen gerekli değildir.

- Doğrulanana kadar yeni IP/port'a veri paketleri gönderilmemesi
- Yeni IP/port doğrulanana kadar eski IP/port'a veri paketleri gönderilmeye devam edilmesi
- Eski IP/port'un aynı anda yeniden doğrulanması
- Eski veya yeni IP/port'tan biri doğrulanana kadar hiç veri gönderilmemesi
- Sadece port değişikliği için IP değişikliğinden farklı stratejiler
- Geçici adres rotasyonundan kaynaklanması muhtemel aynı /32 içindeki IPv6 değişikliği için farklı stratejiler

### Başarılı Yol Doğrulaması

Yol doğrulaması başarılı olduğunda, bağlantı tamamen yeni IP/port'a taşınır. Başarı durumunda:

Path validation (yol doğrulama) aşamasındayken, eski IP/port'tan alınan ve başarıyla şifrelenmiş olan geçerli, tekrar olmayan herhangi bir paket, Path Validation'ın iptal edilmesine neden olur. Sahte bir paket nedeniyle iptal edilen bir path validation'ın, geçerli bir oturumun sonlandırılmasına veya önemli ölçüde kesintiye uğramasına neden olmaması önemlidir.

İptal edilen yol doğrulamasında:

Sahte bir paket nedeniyle başarısız olan yol doğrulamasının, geçerli bir oturumun sonlandırılmasına veya önemli ölçüde kesintiye uğramasına neden olmaması önemlidir.

Başarısız yol doğrulamasında:

### Yol Doğrulamasını İptal Etme

Yukarıdaki süreç, değişmiş bir IP/port'tan paket alan peer'lar için tanımlanmıştır. Ancak, IP'sinin veya port'unun değiştiğini tespit eden bir peer tarafından diğer yönde de başlatılabilir. Bir peer yerel IP'sinin değiştiğini tespit edebilir; ancak NAT yeniden bağlanması nedeniyle port'unun değiştiğini tespit etmesi çok daha az olasıdır. Bu nedenle bu isteğe bağlıdır.

- Yol doğrulama aşamasından çık
- Tüm paketler yeni IP ve porta gönderilir.
- Tıkanıklık penceresi ve PMTU kısıtlamaları kaldırılır ve artmalarına izin verilir. Yeni yolun farklı özelliklere sahip olabileceği için bunları eski değerlere geri yüklemeyin.
- IP değiştiyse, hesaplanan RTT ve RTO'yu başlangıç değerlerine ayarlayın. Yalnızca port değişiklikleri genellikle NAT yeniden bağlama veya diğer ara kutu aktivitelerinin sonucu olduğu için, peer bu durumlarda başlangıç değerlerine geri dönmek yerine tıkanıklık kontrol durumunu ve gidiş-dönüş tahminini koruyabilir.
- Eski IP/port için gönderilen veya alınan tokenları sil (geçersiz kıl) (isteğe bağlı)
- Yeni IP/port için yeni bir token bloğu gönder (isteğe bağlı)

### Başarısız Yol Doğrulaması

IP'si veya portu değişmiş bir eşten path challenge aldığında, diğer eş karşı yönde bir path challenge başlatmalıdır.

Path Challenge ve Path Response blokları herhangi bir zamanda Ping/Pong paketleri olarak kullanılabilir. Path Challenge bloğunun alınması, farklı bir IP/port'tan alınmadığı sürece alıcıda herhangi bir durum değişikliğine neden olmaz.

- Yol doğrulama aşamasından çık
- Tüm paketler eski IP ve porta gönderilir.
- Tıkanıklık penceresi ve PMTU üzerindeki kısıtlamalar kaldırılır ve artışlarına izin verilir veya isteğe bağlı olarak önceki değerler geri yüklenir
- Daha önce yeni IP/porta gönderilen veri paketlerini eski IP/porta yeniden ilet.

### Yerel Değişiklik Sonrası Doğrulama

Peer'lar aynı peer ile, ister SSU 1 veya 2 olsun, ya da aynı veya farklı IP adresleriyle birden fazla oturum kurmamalıdır. Ancak bu durum, hatalar, önceki oturum sonlandırma mesajının kaybolması veya sonlandırma mesajının henüz gelmediği bir yarış durumu nedeniyle gerçekleşebilir.

Bob'un Alice ile mevcut bir oturumu varsa, Bob Alice'den Session Confirmed'i aldığında, el sıkışmayı tamamlayarak ve yeni bir oturum kurarak, Bob şunları yapmalıdır:

- Yol doğrulama aşamasından çık
- Tüm paketler eski IP ve porta gönderilir.
- Tıkanıklık penceresi ve PMTU üzerindeki kısıtlamalar kaldırılır ve artmalarına izin verilir.
- İsteğe bağlı olarak, eski IP ve port üzerinde yol doğrulama başlat. Başarısız olursa, oturumu sonlandır.
- Aksi takdirde, standart oturum zaman aşımı ve sonlandırma kurallarını takip et.
- Daha önce yeni IP/porta gönderilen tüm veri paketlerini eski IP/porta yeniden ilet.

### Ping/Pong olarak kullan

Handshake aşamasındaki oturumlar genellikle basitçe zaman aşımına uğrayarak veya daha fazla yanıt vermeyerek sonlandırılır. İsteğe bağlı olarak, yanıta bir Termination bloğu dahil edilerek sonlandırılabilirler, ancak çoğu hata kriptografik anahtarların eksikliği nedeniyle yanıtlanamaz. Bir termination bloğu içeren yanıt için anahtarlar mevcut olsa bile, genellikle yanıt için DH gerçekleştirmek CPU açısından değmez. Bir istisna, oluşturulması ucuz olan bir yeniden deneme mesajındaki Termination bloğu OLABİLİR.

Veri fazındaki oturumlar, bir Sonlandırma bloğu içeren veri mesajı gönderilerek sonlandırılır. Bu mesaj ayrıca bir ACK bloğu da içermelidir. Eğer oturum, daha önce gönderilen bir token'ın süresi dolmuş veya dolmak üzereyse yeterince uzun süredir açıksa, bir Yeni Token bloğu da içerebilir. Bu mesaj ack-eliciting (onay gerektiren) değildir. "Sonlandırma Alındı" dışında herhangi bir nedenle Sonlandırma bloğu alan eş, "Sonlandırma Alındı" nedeniyle bir Sonlandırma bloğu içeren veri mesajı ile yanıt verir.

### El sıkışma aşaması

Bir Termination bloğu gönderdikten veya aldıktan sonra, oturum belirli bir maksimum süre boyunca kapanma fazına girmelidir (süre henüz belirlenmemiştir). Kapanma durumu, Termination bloğunu içeren paketin kaybolmasına ve diğer yönde uçuş halindeki paketlere karşı koruma sağlamak için gereklidir. Kapanma fazındayken, alınan ek paketleri işleme zorunluluğu yoktur. Kapanma durumundaki bir oturum, oturuma atfettiği herhangi bir gelen pakete yanıt olarak Termination bloğu içeren bir paket gönderir. Bir oturum, kapanma durumunda ürettiği paket oranını sınırlamalıdır. Örneğin, bir oturum alınan paketlere yanıt vermeden önce giderek artan sayıda paket alınmasını veya belirli bir sürenin geçmesini bekleyebilir.

## Çoklu Oturumlar

Kapanan bir oturum için bir router'ın koruduğu durumu minimize etmek amacıyla, oturumlar alınan herhangi bir pakete yanıt olarak aynı paket numarasına sahip tamamen aynı paketi gönderebilir, ancak bunu yapmak zorunda değildir. Not: Bir sonlandırma paketinin yeniden iletilmesine izin verilmesi, her paket için yeni bir paket numarası kullanılması gerekliliğinin bir istisnasıdır. Yeni paket numaraları göndermenin birincil avantajı, kapalı bir bağlantı için gerekli olması beklenmeyen kayıp kurtarma ve tıkanıklık kontrolü içindir. Son paketi yeniden iletmek daha az durum gerektirir.

"Termination Received" nedeniyle bir Termination bloğu aldıktan sonra, oturum kapanma aşamasından çıkabilir.

- Eski oturumdan yeni oturuma gönderilmemiş veya onaylanmamış giden I2NP mesajlarını taşı
- Eski oturumda neden kodu 22 ile sonlandırma gönder
- Eski oturumu kaldır ve yerine yenisini koy

## Oturum Sonlandırma

### Veri aşaması

Herhangi bir normal veya anormal sonlandırma durumunda, router'lar bellekteki tüm geçici verileri sıfırlamalıdır; bu veriler arasında handshake geçici anahtarları, simetrik kripto anahtarları ve ilgili bilgiler bulunur.

### Temizlik

Gereksinimler, yayınlanan adresin SSU 1 ile paylaşılıp paylaşılmamasına bağlı olarak değişir. Mevcut SSU 1 IPv4 minimum değeri 620'dir ve bu kesinlikle çok küçüktür.

Minimum SSU2 MTU değeri hem IPv4 hem de IPv6 için 1280'dir, bu da [RFC-9000](https://tools.ietf.org/html/rfc9000)'de belirtilen değerle aynıdır. Aşağıya bakınız. Minimum MTU değerinin artırılmasıyla, 1 KB tunnel mesajları ve kısa tunnel yapı mesajları tek bir datagram'a sığacak ve tipik fragmantasyon miktarını büyük ölçüde azaltacaktır. Bu aynı zamanda maksimum I2NP mesaj boyutunda artışa da olanak sağlar. 1820-baytlık streaming mesajları iki datagram'a sığmalıdır.

Bir router, o adres için MTU en az 1280 olmadıkça SSU2'yi etkinleştirmemeli veya bir SSU2 adresi yayımlamamalıdır.

Router'lar her SSU veya SSU2 router adresinde varsayılan olmayan bir MTU yayınlamalıdır.

### SSU Adresi

SSU 1 ile paylaşılan adres, SSU 1 kurallarını takip etmelidir. IPv4: Varsayılan ve maksimum 1484'tür. Minimum 1292'dir. (IPv4 MTU + 4) 16'nın katı olmalıdır. IPv6: Yayınlanmalıdır, minimum 1280 ve maksimum 1488'dir. IPv6 MTU 16'nın katı olmalıdır.

## MTU

IPv4: Varsayılan ve maksimum 1500'dür. Minimum 1280'dir. IPv6: Varsayılan ve maksimum 1500'dür. Minimum 1280'dir. 16'nın katı kuralları yoktur, ancak muhtemelen en azından 2'nin katı olmalıdır.

SSU 1 için, mevcut Java I2P, PMTU keşfini küçük paketlerle başlayarak ve boyutu kademeli olarak artırarak veya alınan paket boyutuna göre artırarak gerçekleştirir. Bu yöntem kaba ve verimliliği büyük ölçüde azaltır. Bu özelliğin SSU 2'de devam ettirilmesi henüz belirlenmedi.

Son çalışmalar [PMTU](https://en.wikipedia.org/wiki/Path_MTU_Discovery), IPv4 için 1200 veya daha fazla minimum değerin bağlantıların %99'undan fazlası için çalışacağını öne sürüyor. QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) minimum 1280 bayt IP paket boyutu gerektirir.

[RFC-9000](https://tools.ietf.org/html/rfc9000) alıntısı:

### SSU2 Adresi

Maksimum datagram boyutu, tek bir UDP datagramı kullanarak bir ağ yolu üzerinden gönderilebilecek en büyük UDP yük boyutu olarak tanımlanır. Ağ yolu en az 1200 bayt maksimum datagram boyutunu destekleyemiyorsa QUIC KULLANILMAMALIDIR.

### PMTU Keşfi

QUIC, en az 1280 bayt IP paket boyutu varsayar. Bu IPv6 minimum boyutudur [IPv6] ve aynı zamanda çoğu modern IPv4 ağı tarafından da desteklenir. IPv6 için 40 bayt ve IPv4 için 20 bayt minimum IP başlık boyutu ve 8 bayt UDP başlık boyutu varsayıldığında, bu IPv6 için maksimum 1232 bayt ve IPv4 için 1252 bayt datagram boyutu ile sonuçlanır. Böylece, modern IPv4 ve tüm IPv6 ağ yollarının QUIC'i destekleyebilmesi beklenir.

### El Sıkışma Minimum Boyutu

Not: 1200 baytlık bir UDP yük alanını destekleme gerekliliği, yol yalnızca 1280 baytlık IPv6 minimum MTU'sunu destekliyorsa, IPv6 uzantı başlıkları için kullanılabilir alanı 32 bayt veya IPv4 seçenekleri için 52 bayt ile sınırlar. Bu durum İlk paketleri ve yol doğrulamasını etkiler.

alıntı sonu

QUIC, amplifikasyon saldırılarını önlemek ve PMTU'nun her iki yönde de bunu desteklediğinden emin olmak için her iki yönde de Initial datagramlarının en az 1200 bayt olmasını gerektirir.

Bunu Session Request ve Session Created için gerekli kılabiliriz, ancak bant genişliğinde önemli bir maliyet olur. Belki bunu yalnızca token'ımız yoksa veya Retry mesajı alındıktan sonra yapabiliriz. Henüz belirlenemedi

QUIC, Bob'un istemci adresi doğrulanana kadar alınan veri miktarının üç katından fazlasını göndermemesini gerektirir. SSU2 bu gereksinimi doğası gereği karşılar, çünkü Retry mesajı Token Request mesajı ile yaklaşık aynı boyuttadır ve Session Request mesajından daha küçüktür. Ayrıca, Retry mesajı yalnızca bir kez gönderilir.

QUIC, PATH_CHALLENGE veya PATH_RESPONSE blokları içeren mesajların amplifikasyon saldırılarını önlemek için en az 1200 bayt olmasını gerektirir ve PMTU'nun her iki yönde de bunu desteklediğinden emin olunmasını sağlar.

Bunu da gerekli kılabiliriz, ancak bant genişliğinde önemli bir maliyet getirir. Bununla birlikte, bu durumlar nadir olmalıdır. TBD

### Path Mesajı Min Boyutu

IPv4: IP parçalanması olmadığı varsayılır. IP + datagram başlığı 28 bayttır. Bu, IPv4 seçeneklerinin olmadığını varsayar. Maksimum mesaj boyutu MTU - 28'dir. Veri fazı başlığı 16 bayt ve MAC 16 bayttır, toplamda 32 bayt eder. Yük boyutu MTU - 60'tır. Maksimum veri fazı yükü, maksimum 1500 MTU için 1440'tır. Maksimum veri fazı yükü, minimum 1280 MTU için 1220'dir.

IPv6: IP parçalanmasına izin verilmez. IP + datagram başlığı 48 bayttır. Bu, IPv6 uzantı başlıklarının olmadığını varsayar. Maksimum mesaj boyutu MTU - 48'dir. Veri aşaması başlığı 16 bayt ve MAC 16 bayttır, toplamda 32 bayt. Yük boyutu MTU - 80'dir. Maksimum veri aşaması yükü, maksimum 1500 MTU için 1420'dir. Maksimum veri aşaması yükü, minimum 1280 MTU için 1200'dür.

SSU 1'de, yönergeler 64 maksimum fragment ve 620 minimum MTU'ya dayalı olarak bir I2NP mesajı için yaklaşık 32 KB'lık katı bir maksimum belirliyordu. Paketlenmiş LeaseSet'ler ve oturum anahtarları için ek yük nedeniyle, uygulama seviyesindeki pratik sınır yaklaşık 6KB daha düşüktü, yani yaklaşık 26KB. SSU 1 protokolü 128 fragment'a izin verir ancak mevcut implementasyonlar bunu 64 fragment ile sınırlar.

### Maksimum I2NP Mesaj Boyutu

Minimum MTU'yu 1280'e çıkararak, yaklaşık 1200'lük bir veri fazı yüküyle, 64 parçada yaklaşık 76 KB'lık ve 128 parçada 152 KB'lık bir SSU 2 mesajı mümkündür. Bu, maksimum 64 KB'ye kolayca izin verir.

Tunnel'lardaki parçalanma ve SSU 2'deki parçalanma nedeniyle, mesaj kaybı olasılığı mesaj boyutuyla birlikte katlanarak artar. I2NP datagram'ları için uygulama katmanında yaklaşık 10 KB'lık pratik bir sınır önermeye devam ediyoruz.

### Sürümler

SSU1 Peer Test analizi ve SSU2 Peer Test hedefleri için yukarıdaki Peer Test Güvenliği bölümüne bakınız.

Bob tarafından reddedildiğinde:

Charlie tarafından reddedildiğinde:

NOT: RI, I2NP blokları içinde I2NP Database Store mesajları olarak veya (yeterince küçükse) RI blokları olarak gönderilebilir. Bunlar, yeterince küçükse, peer test blokları ile aynı paketlerde bulunabilir.

Mesaj 1-4, Data mesajı içindeki Peer Test blokları kullanılarak oturum içinde gerçekleşir. Mesaj 5-7, Peer Test mesajı içindeki Peer Test blokları kullanılarak oturum dışında gerçekleşir.

## Peer Test Süreci

NOT: SSU 1'de olduğu gibi, 4 ve 5 numaralı mesajlar herhangi bir sırada gelebilir. Alice güvenlik duvarı arkasındaysa 5 ve/veya 7 numaralı mesajlar hiç alınmayabilir. 5 numaralı mesaj 4 numaralı mesajdan önce geldiğinde, Alice hemen 6 numaralı mesajı gönderemez çünkü henüz Charlie'nin başlığı şifrelemek için intro key'ine sahip değildir. 4 numaralı mesaj 5 numaralı mesajdan önce geldiğinde, Alice hemen 6 numaralı mesajı göndermemelidir çünkü 6 numaralı mesajla güvenlik duvarını açmadan önce 5 numaralı mesajın gelip gelmediğini beklemeli.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest
        <---------------- Charlie RI
4.      <------------------ PeerTest

5.      <----------------------------------------- PeerTest
6. PeerTest ----------------------------------------->
7.      <----------------------------------------- PeerTest
```
Sürümler arası peer testi desteklenmez. İzin verilen tek sürüm kombinasyonu, tüm peer'ların sürüm 2 olduğu durumdur.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
4.      <------------------ PeerTest (reject)
```
Mesajlar 1-4 oturum içindedir ve veri fazı ACK ve yeniden iletim süreçleri tarafından kapsanır. Peer Test blokları ack-tetikleyicidir.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest (reject)
                      (optional: Bob could try another Charlie here)
4.      <------------------ PeerTest (reject)
```
5-7 mesajları değiştirilmeden yeniden iletilebilir.

SSU 1'de olduğu gibi, IPv6 adreslerinin test edilmesi desteklenir ve Bob ve Charlie yayınladıkları IPv6 adresinde 'B' yeteneği ile destek belirtirlerse, Alice-Bob ve Alice-Charlie iletişimi IPv6 üzerinden olabilir. Ayrıntılar için Öneri 126'ya bakın.

0.9.50 öncesi SSU 1'deki gibi, Alice isteği Bob'a test etmek istediği taşıma katmanı (IPv4 veya IPv6) üzerinden mevcut bir oturum kullanarak gönderir. Bob, Alice'den IPv4 üzerinden bir istek aldığında, Bob bir IPv4 adresi tanıtan bir Charlie seçmelidir. Bob, Alice'den IPv6 üzerinden bir istek aldığında, Bob bir IPv6 adresi tanıtan bir Charlie seçmelidir. Gerçek Bob-Charlie iletişimi IPv4 veya IPv6 üzerinden olabilir (yani Alice'in adres türünden bağımsızdır). Bu, karışık IPv4/v6 isteklerine izin verilen 0.9.50 itibariyle SSU 1'in davranışı DEĞİLDİR.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Path</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Intro Key</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->C session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->A session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->C</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
  </tbody>
</table>
### Yeniden İletimler

SSU 1'den farklı olarak, Alice mesaj 1'de istenen test IP'sini ve portunu belirtir. Bob bu IP ve portu doğrulamalı ve geçersizse kod 5 ile reddetmelidir. Önerilen IP doğrulaması şudur: IPv4 için Alice'in IP'si ile eşleşmeli, IPv6 için ise IP'nin en az ilk 8 baytı eşleşmelidir. Port doğrulaması, ayrıcalıklı portları ve tanınmış protokoller için kullanılan portları reddetmelidir.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### IPv6 Notları

Burada Alice'in hangi mesajların alındığına bağlı olarak peer testinin sonuçlarını nasıl belirleyebileceğini belgeliyoruz. SSU2'nin geliştirmeleri, [SSU](/docs/transport/ssu)'daki ile karşılaştırıldığında peer test sonuç durum makinesini düzeltme, iyileştirme ve daha iyi belgeleme fırsatı sunuyor.

Test edilen her adres türü (IPv4 veya IPv6) için sonuç UNKNOWN, OK, FIREWALLED veya SYMNAT değerlerinden biri olabilir. Ek olarak, IP veya port değişikliğini ya da dahili porttan farklı bir harici portu tespit etmek için başka işlemler de yapılabilir.

### Bob tarafından işleme

Belgelenen SSU durum makinesi ile ilgili sorunlar:

Bu nedenle, SSU'nun aksine, mesaj 4'ü aldıktan sonra birkaç saniye beklemeyi, ardından mesaj 5 alınmamış olsa bile mesaj 6'yı göndermeyi öneriyoruz.

### Sonuçlar Durum Makinesi

Mesaj 4, 5 ve 7'nin alınıp alınmamasına (evet veya hayır) dayalı durum makinesi özeti aşağıdaki gibidir:

### Yeniden İletimler

IP/port'un mesaj 7'nin adres bloğunda alındığı kontrolleri içeren daha ayrıntılı bir durum makinesi aşağıdadır. Bir zorluk, simetrik NAT arkasında olanın siz (Alice) mi yoksa Charlie mi olduğunu belirlemektir.

Durum geçişlerini onaylamak için iki veya daha fazla peer testinde aynı sonuçları gerektiren son işleme veya ek mantık önerilir.

İki veya daha fazla test tarafından IP/port doğrulaması ve onayı alınması veya Session Created mesajlarında adres bloğu ile birlikte kullanılması da önerilir, ancak bu spesifikasyonun kapsamı dışındadır.

- Mesaj 5'i almadıkça asla mesaj 6'yı göndermeyiz, bu yüzden SYMNAT olup olmadığımızı asla bilemeyiz
- Mesaj 4 ve 7'yi aldıysak, nasıl olur da SYMNAT olabiliriz
- IP eşleşmedi ama port eşleştiyse, SYMNAT değiliz, sadece IP'mizi değiştirdik

SSU1 Relay analizi ve SSU2 Relay hedefleri için yukarıdaki Relay Güvenliği bölümüne bakın.

Bob tarafından reddedildiğinde:

```
4 5 7  Result             Notes
-----  ------             -----
n n n  UNKNOWN
y n n  FIREWALLED           (unless currently SYMNAT)
n y n  OK                   (unless currently SYMNAT, which is unlikely)
y y n  OK                   (unless currently SYMNAT, which is unlikely)
n n y  n/a                  (can't send msg 6)
y n y  FIREWALLED or SYMNAT (requires sending msg 6 w/o rcv msg 5)
n y y  n/a                  (can't send msg 6)
y y y  OK
```
Charlie tarafından reddedildiğinde:

NOT: RI, I2NP bloklarında I2NP Database Store mesajları olarak veya RI blokları olarak (yeterince küçükse) gönderilebilir. Bunlar, yeterince küçükse, relay blokları ile aynı paketlerde bulunabilir.

SSU 1'de, Charlie'nin router bilgisi her introducer için IP, port, intro key, relay tag ve son kullanma tarihini içerir.

```
If Alice does not get msg 5:
   If Alice does not get msg 4: -> UNKNOWN
   If Alice does not get msg 7: -> UNKNOWN
   If Alice gets msgs 4/7 and IP/port match: -> FIREWALLED
   If Alice gets msgs 4/7 and IP matches, port does not match:
      -> SYMNAT, but needs confirmation with 2nd test
   If Alice gets msgs 4/7 and IP does not match, port matches:
      -> FIREWALLED, address change?
   If Alice gets msgs 4/7 and both IP and port do not match:
      -> SYMNAT, address change?

If Alice gets msg 5:
   If Alice does not get msg 4: -> OK unless currently SYMNAT, else UNKNOWN
                                   (in SSU2 have to stop here)
   If Alice does not get msg 7: -> OK unless currently SYMNAT, else UNKNOWN
   If Alice gets msgs 4/5/7 and IP/port match: -> OK
   If Alice gets msgs 4/5/7 and IP matches, port does not match:
      -> OK, charlie is probably sym. natted
   If Alice gets msgs 4/5/7 and IP does not match, port matches:
      -> OK, address change?
   If Alice gets msgs 4/5/7 and both IP and port do not match:
      -> OK, address change?
```
## Relay Süreci

SSU 2'de, Charlie'nin router bilgisi her introducer için router hash'ini, relay etiketini ve son kullanma tarihini içerir.

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse

5.      <-------------------------------------------- HolePunch
6. SessionRequest -------------------------------------------->
7.      <-------------------------------------------- SessionCreated
8. SessionConfirmed ------------------------------------------>
```
Alice önce zaten bağlantı kurduğu bir introducer (Bob) seçerek gereken round trip sayısını azaltmalıdır. İkinci olarak, eğer böyle biri yoksa, zaten router bilgisine sahip olduğu bir introducer seçmelidir.

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
4.      <-------------- RelayResponse
```
Mümkünse sürümler arası relay de desteklenmelidir. Bu, SSU 1'den SSU 2'ye kademeli geçişi kolaylaştıracaktır. İzin verilen sürüm kombinasyonları şunlardır (TODO):

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse
```
Relay Request, Relay Intro ve Relay Response'un tümü oturum içindedir ve veri fazı ACK ve yeniden iletim süreçleri tarafından kapsanır. Relay Request, Relay Intro ve Relay Response blokları ACK gerektiren bloklardır.

Unutmayın ki genellikle Charlie, bir Relay Intro'ya hemen bir Relay Response ile yanıt verecektir ve bu yanıt bir ACK bloğu içermelidir. Bu durumda, ACK bloğu içeren ayrı bir mesaj gerekmez.

Hole punch, SSU 1'de olduğu gibi yeniden iletilebilir.

I2NP mesajlarının aksine, Relay mesajlarının benzersiz tanımlayıcıları yoktur, bu nedenle duplikatlar nonce kullanılarak relay durum makinesi tarafından tespit edilmelidir. Uygulamalar ayrıca yakın zamanda kullanılmış nonce'ların bir önbelleğini tutmaya ihtiyaç duyabilir, böylece o nonce için durum makinesi tamamlandıktan sonra bile alınan duplikatlar tespit edilebilir.

SSU 1 relay'in tüm özellikleri desteklenir, bu [Prop158](/proposals/158-ipv6-transport-enhancements) belgesinde açıklanan ve 0.9.50 sürümü itibarıyla desteklenen özellikler dahil. IPv4 ve IPv6 tanıtımları desteklenir. Bir Relay Request, IPv6 tanıtımı için IPv4 oturumu üzerinden gönderilebilir ve bir Relay Request, IPv4 tanıtımı için IPv6 oturumu üzerinden gönderilebilir.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/2/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### IPv4/v6

Aşağıda SSU 1'den farklılıklar ve SSU 2 uygulaması için öneriler yer almaktadır.

SSU 1'de, tanıtım nispeten ucuzdur ve Alice genellikle tüm tanıtıcılara Relay Request'ler gönderir. SSU 2'de, önce bir tanıtıcı ile bağlantı kurulması gerektiğinden tanıtım daha pahalıdır. Tanıtım gecikmesini ve ek yükünü en aza indirmek için önerilen işleme adımları şu şekildedir:

Hem SSU 1 hem de SSU 2'de, Relay Response ve Hole Punch herhangi bir sırada alınabilir veya hiç alınmayabilir.

SSU 1'de, Alice genellikle Hole Punch'tan (1 1/2 RTT) önce Relay Response'u (1 RTT) alır. Bu spesifikasyonlarda iyi belgelenmemiş olabilir, ancak Alice devam etmek için Bob'tan Relay Response'u almalı ve Charlie'nin IP'sini öğrenmelidir. Hole Punch önce alınırsa, Alice bunu tanımayacaktır çünkü veri içermez ve kaynak IP tanınmaz. Relay Response'u aldıktan sonra, Alice Charlie ile handshake başlatmadan önce Charlie'den Hole Punch almayı YA DA kısa bir gecikmeyi (önerilen 500 ms) beklemelidir.

### Alice tarafından işleniyor

SSU 2'de, Alice genellikle Hole Punch'ı (1 1/2 RTT) Relay Response'tan (2 RTT) önce alacaktır. SSU 2 Hole Punch'ı SSU 1'dekinden işlemesi daha kolaydır, çünkü tanımlanmış connection ID'leri (relay nonce'dan türetilmiş) ve Charlie'nin IP'si dahil olmak üzere içerikleri olan tam bir mesajdır. Relay Response (Data mesajı) ve Hole Punch mesajı aynı imzalı Relay Response bloğunu içerir. Bu nedenle, Alice, Charlie'den Hole Punch'ı aldıktan SONRA VEYA Bob'tan Relay Response'u aldıktan sonra Charlie ile handshake'i başlatabilir.

### Bob Tarafından Etiket İstekleri

Hole Punch'ın imza doğrulaması, tanıtıcının (Bob'un) router hash'ini içerir. Eğer Relay Request'ler birden fazla tanıtıcıya gönderilmişse, imzayı doğrulamak için birkaç seçenek vardır:

#### Özet

Eğer Charlie simetrik bir NAT'ın arkasındaysa, Relay Response ve Hole Punch'taki bildirdiği port doğru olmayabilir. Bu nedenle, Alice Hole Punch mesajının UDP kaynak portunu kontrol etmeli ve bildirilen porttan farklıysa onu kullanmalıdır.

- Adreste bulunan iexp değerine göre süresi dolmuş olan tüm introducer'ları yoksay
- Bir veya daha fazla introducer'a zaten kurulu bir SSU2 bağlantısı varsa, birini seç ve Relay Request'i sadece o introducer'a gönder.
- Aksi takdirde, bir veya daha fazla introducer için yerel olarak bir Router Info biliniyorsa, birini seç ve sadece o introducer'a bağlan.
- Aksi takdirde, tüm introducer'lar için Router Info'ları ara, Router Info'su ilk alınan introducer'a bağlan.

#### Detaylar

SSU 1'de, yalnızca Alice bir etiket talep edebilirdi, Session Request içinde. Bob asla bir etiket talep edemezdi ve Alice, Bob için relay yapamazdı.

SSU2'de Alice genellikle Session Request'te bir tag talep eder, ancak Alice veya Bob'un her ikisi de veri aşamasında tag talep edebilir. Bob genellikle gelen bir istek aldıktan sonra güvenlik duvarı arkasında değildir, ancak bir relay'den sonra olabilir veya Bob'un durumu değişebilir ya da diğer adres türü (IPv4/v6) için bir introducer talep edebilir. Bu nedenle SSU2'de Alice ve Bob'un aynı anda diğer taraf için relay olması mümkündür.

Aşağıdaki adres özellikleri, SSU 1'den değişmeden yayınlanabilir ve API 0.9.50 itibarıyla desteklenen [Prop158](/proposals/158-ipv6-transport-enhancements) değişiklikleri dahil olmak üzere:

Yayınlanan RouterAddress (RouterInfo'nun bir parçası) "SSU" veya "SSU2" protokol tanımlayıcısına sahip olacaktır.

- İstek gönderilen her hash'i dene
- Her introducer için farklı nonce'lar kullan ve bunları hangi introducer'ın bu Hole Punch'a yanıt verdiğini belirlemek için kullan
- Eğer içerik daha önce alınan Relay Response'dakiyle aynıysa imzayı yeniden doğrulama
- İmzayı hiç doğrulama

RouterAddress, SSU2 desteğini belirtmek için üç seçenek içermelidir:

### Adres Özellikleri

Alice, SSU2 protokolünü kullanarak bağlanmadan önce üç seçeneğin de mevcut ve geçerli olduğunu doğrulamalıdır.

"s", "i" ve "v" seçenekleri ile ve "host" ve "port" seçenekleri ile "SSU" olarak yayımlandığında, router hem SSU hem de SSU2 protokolleri için o host ve port üzerinden gelen bağlantıları kabul etmeli ve protokol sürümünü otomatik olarak algılamalıdır.

## Yayınlanmış Router Bilgisi

### Yayınlanmış Adresler

"s", "i" ve "v" seçenekleri ile ve "host" ve "port" seçenekleri ile "SSU2" olarak yayınlandığında, router yalnızca SSU2 protokolü için o host ve port üzerinden gelen bağlantıları kabul eder.

- caps: [B,C,4,6] yetenekleri
- host: IP (IPv4 veya IPv6). Kısaltılmış IPv6 adresi ("::") ile izin verilir. Güvenlik duvarı arkasındaysa mevcut olabilir veya olmayabilir. Host isimleri izin verilmez.
- iexp[0-2]: Bu introducer'ın sona erme zamanı. Epoch'tan bu yana saniye cinsinden ASCII rakamları. Sadece güvenlik duvarı arkasındaysa ve introducer'lar gerekiyorsa mevcut. İsteğe bağlı (bu introducer için diğer özellikler mevcut olsa bile).
- ihost[0-2]: Introducer'ın IP'si (IPv4 veya IPv6). Kısaltılmış IPv6 adresi ("::") ile izin verilir. Sadece güvenlik duvarı arkasındaysa ve introducer'lar gerekiyorsa mevcut. Host isimleri izin verilmez. Sadece SSU adresi.
- ikey[0-2]: Introducer'ın Base 64 tanıtım anahtarı. Sadece güvenlik duvarı arkasındaysa ve introducer'lar gerekiyorsa mevcut. Sadece SSU adresi.
- iport[0-2]: Introducer'ın portu 1024 - 65535. Sadece güvenlik duvarı arkasındaysa ve introducer'lar gerekiyorsa mevcut. Sadece SSU adresi.
- itag[0-2]: Introducer'ın etiketi 1 - (2**32 - 1) ASCII rakamları. Sadece güvenlik duvarı arkasındaysa ve introducer'lar gerekiyorsa mevcut.
- key: Base 64 tanıtım anahtarı.
- mtu: İsteğe bağlı. Yukarıdaki MTU bölümüne bakın.
- port: 1024 - 65535 Güvenlik duvarı arkasındaysa mevcut olabilir veya olmayabilir.

### Yayınlanmamış SSU2 Adresi

Bir router hem SSU1 hem de SSU2 bağlantılarını destekliyorsa ancak gelen bağlantılar için otomatik sürüm algılaması uygulamıyorsa, hem "SSU" hem de "SSU2" adreslerini tanıtmalı ve SSU2 seçeneklerini yalnızca "SSU2" adresine dahil etmelidir. Router, SSU2'nin tercih edilmesi için "SSU2" adresinde "SSU" adresinden daha düşük bir maliyet değeri (daha yüksek öncelik) ayarlamalıdır.

Aynı RouterInfo içinde birden fazla SSU2 RouterAddress ("SSU" veya "SSU2" olarak) yayınlanıyorsa (ek IP adresleri veya portlar için), aynı portu belirten tüm adresler özdeş SSU2 seçeneklerini ve değerlerini içermelidir. Özellikle, tümü aynı statik anahtar "s" ve tanıtım anahtarı "i" içermelidir.

- s=(Base64 anahtarı) Bu RouterAddress için mevcut Noise statik genel anahtarı (s). Standart I2P Base 64 alfabesi kullanılarak Base 64 kodlanmış. İkili formatta 32 bayt, Base 64 kodlu olarak 44 bayt, little-endian X25519 genel anahtarı.
- i=(Base64 anahtarı) Bu RouterAddress için başlıkları şifrelemek üzere mevcut tanıtım anahtarı. Standart I2P Base 64 alfabesi kullanılarak Base 64 kodlanmış. İkili formatta 32 bayt, Base 64 kodlu olarak 44 bayt, big-endian ChaCha20 anahtarı.
- v=2 Mevcut sürüm (2). "SSU" olarak yayınlandığında, sürüm 1 için ek destek ima edilir. Gelecek sürümler için destek virgülle ayrılmış değerlerle olacaktır, örn. v=2,3 Uygulama, virgül varsa birden fazla sürüm dahil olmak üzere uyumluluğu doğrulamalıdır. Virgülle ayrılmış sürümler sayısal sırada olmalıdır.

SSU veya SSU2 ile introducer'lar kullanılarak yayınlandığında, aşağıdaki seçenekler mevcuttur:

Aşağıdaki seçenekler yalnızca SSU içindir ve SSU2 için kullanılmaz. SSU2'de Alice bu bilgiyi Charlie'nin RI'sından alır.

Bir router, introducer yayınlarken adres içinde host veya port yayınlamamalıdır. Bir router, IPv4 ve/veya IPv6 desteğini belirtmek için introducer yayınlarken adres içinde 4 ve/veya 6 cap'lerini yayınlamalıdır. Bu, güncel SSU 1 adresleri için mevcut uygulamayla aynıdır.

Not: SSU olarak yayınlanırsa ve SSU 1 ile SSU2 introducer'ların karışımı varsa, eski router'larla uyumluluk için SSU 1 introducer'lar daha düşük indekslerde, SSU2 introducer'lar ise daha yüksek indekslerde olmalıdır.

Eğer Alice gelen bağlantılar için SSU2 adresini ("SSU" veya "SSU2" olarak) yayınlamazsa, sadece statik anahtarını ve SSU2 sürümünü içeren bir "SSU2" router adresi yayınlamalıdır, böylece Bob, Alice'in RouterInfo'sunu Session Confirmed bölüm 2'de aldıktan sonra anahtarı doğrulayabilir.

#### Hata İşleme

Bu router adresi "host" veya "port" seçeneklerini içermeyecektir, çünkü bunlar giden SSU2 bağlantıları için gerekli değildir. Bu adres için yayınlanan maliyet kesin olarak önemli değildir, çünkü sadece gelen bağlantılar içindir; ancak maliyet diğer adreslerden daha yüksek (daha düşük öncelik) olarak ayarlanırsa diğer router'lar için yararlı olabilir. Önerilen değer 14'tür.

- ih[0-2]=(Base64 hash) Bir introducer için router hash'i. Standart I2P Base 64 alfabesi kullanılarak Base 64 kodlanmış. Binary olarak 32 byte, Base 64 kodlanmış olarak 44 byte
- iexp[0-2]: Bu introducer'ın sona erme süresi. SSU 1'den değişmedi.
- itag[0-2]: Introducer'ın etiketi 1 - (2**32 - 1) SSU 1'den değişmedi.

Alice ayrıca mevcut yayınlanmış bir "SSU" adresine basitçe "i", "s" ve "v" seçeneklerini ekleyebilir.

- ihost[0-2]
- ikey[0-2]
- itag[0-2]

NTCP2 ve SSU2 için aynı statik anahtarları kullanmak mümkündür, ancak önerilmez.

RouterInfo'ların önbelleğe alınması nedeniyle, router'lar çalışır durumdayken statik genel anahtarı veya IV'yi döndürmemelidir, yayınlanmış bir adreste olsun ya da olmasın. Router'lar bu anahtarı ve IV'yi hemen yeniden başlatma sonrasında yeniden kullanım için kalıcı olarak saklamalıdır, böylece gelen bağlantılar çalışmaya devam eder ve yeniden başlatma süreleri açığa çıkmaz. Router'lar son kapanma zamanını kalıcı olarak saklamalı veya başka şekilde belirlemeli ki, başlangıçta önceki kesinti süresi hesaplanabilsin.

### Açık Anahtar ve IV Rotasyonu

Yeniden başlatma zamanlarının açığa çıkmasına ilişkin endişeler nedeniyle, router'lar daha önce bir süre (en az birkaç gün) kapalı kalmışsa başlangıçta bu anahtarı veya IV'yi döndürebilir.

- s=(Base64 anahtar) Yayınlanan adresler için yukarıda tanımlandığı gibi.
- i=(Base64 anahtar) Yayınlanan adresler için yukarıda tanımlandığı gibi.
- v=2 Yayınlanan adresler için yukarıda tanımlandığı gibi.

Router'ın yayınlanmış SSU2 RouterAddress'leri (SSU veya SSU2 olarak) varsa, yerel IP adresi değişmedikçe veya router "rekey" yapmadıkça, rotasyondan önceki minimum kesinti süresi çok daha uzun olmalıdır, örneğin bir ay.

Eğer router yayınlanmış SSU RouterAddress'lere sahipse, ancak SSU2'ye (SSU veya SSU2 olarak) sahip değilse, yerel IP adresi değişmediği veya router "rekey" yapmadığı sürece rotasyon öncesi minimum kesinti süresi daha uzun olmalıdır, örneğin bir gün. Bu durum, yayınlanan SSU adresinin introducer'lara sahip olması durumunda bile geçerlidir.

### Giden Paket Oluşturma

Router'ın yayınlanmış RouterAddress'leri (SSU, SSU2 veya SSU) yoksa, router "rekey" yapmadığı sürece, IP adresi değişse bile rotasyon öncesi minimum kesinti süresi iki saat kadar kısa olabilir.

Router farklı bir Router Hash'e "yeniden anahtar" oluşturursa, yeni bir noise anahtarı ve intro anahtarı da oluşturmalıdır.

Uygulamalar, statik genel anahtarı veya IV'yi değiştirmenin, eski bir RouterInfo'yu önbelleğe almış olan router'lardan gelen SSU2 bağlantılarını engelleyeceğinin farkında olmalıdır. RouterInfo yayınlama, tunnel eş seçimi (hem OBGW hem de IB en yakın hop dahil), sıfır-hop tunnel seçimi, taşıma seçimi ve diğer uygulama stratejileri bunu dikkate almalıdır.

Intro anahtar rotasyonu, anahtar rotasyonu ile aynı kurallara tabidir.

Not: Yeniden anahtarlama öncesindeki minimum kesinti süresi, ağ sağlığını sağlamak ve orta düzeyde bir süre çevrimdışı olan bir router'ın yeniden seed almasını önlemek için değiştirilebilir.

İnkar edilebilirlik bir hedef değildir. Yukarıdaki genel bakışa bakınız.

Her desenin, başlatıcının statik genel anahtarına ve yanıtlayıcının statik genel anahtarına sağlanan gizlilik düzeyini açıklayan özellikleri atanır. Temel varsayımlar, geçici özel anahtarların güvenli olduğu ve tarafların karşı taraftan güvenmedikleri bir statik genel anahtar almaları durumunda el sıkışmayı iptal ettikleridir.

Bu bölüm yalnızca handshake'lerdeki statik genel anahtar alanları aracılığıyla kimlik sızıntısını ele almaktadır. Tabii ki, Noise katılımcılarının kimlikleri payload alanları, trafik analizi veya IP adresleri gibi metadata dahil olmak üzere başka yollarla da açığa çıkabilir.

Alice: (8) Kimliği doğrulanmış bir tarafa ileri gizlilik ile şifrelenmiş.

Bob: (3) İletilmez, ancak pasif bir saldırgan yanıtlayanın özel anahtarı için adayları kontrol edebilir ve adayın doğru olup olmadığını belirleyebilir.

#### Kimlik Gizleme

Bob statik genel anahtarını netDb'de yayınlar. Alice yayınlamayabilir, ancak Bob'a gönderilen RI'ya dahil etmelidir.

Handshake mesajları (Session Request/Created/Confirmed, Retry) temel adımları, sırasıyla:

Veri fazı mesajlarının temel adımları, sırasıyla:

Tüm gelen mesajların ilk işlenmesi:

Handshake mesajları (Session Request/Created/Confirmed, Retry, Token Request) ve diğer oturum-dışı mesajların (Peer Test, Hole Punch) işlenmesi:

Veri aşaması mesaj işleme:

## Paket Yönergeleri

### Gelen Paket İşleme

SSU 1'de, gelen paket sınıflandırması zordur çünkü oturum numarasını belirten bir başlık yoktur. router'lar önce kaynak IP ve portu mevcut bir eş durumu ile eşleştirmeli, bulunamazsa uygun eş durumunu bulmak veya yeni bir tane başlatmak için farklı anahtarlarla birden fazla şifre çözme denemesi yapmalıdır. Mevcut bir oturum için kaynak IP veya port değişirse (muhtemelen NAT davranışından dolayı), router paketi mevcut bir oturumla eşleştirmeye ve içeriği kurtarmaya çalışmak için pahalı sezgisel yöntemler kullanabilir.

- 16 veya 32 bayt başlık oluştur
- Payload oluştur
- Başlığı mixHash() et (Retry hariç)
- Payload'ı Noise kullanarak şifrele (Retry hariç, başlığı AD olarak kullanarak ChaChaPoly kullan)
- Başlığı şifrele ve Session Request/Created için ephemeral key'i şifrele

SSU 2, DPI direncini ve diğer yol üzerindeki tehditleri korurken gelen paket sınıflandırma çabasını minimize edecek şekilde tasarlanmıştır. Connection ID numarası tüm mesaj türleri için başlıkta yer alır ve bilinen bir anahtar ve nonce kullanılarak ChaCha20 ile şifrelenir (gizlenir). Ek olarak, mesaj türü de başlıkta bulunur (bilinen bir anahtara başlık koruması ile şifrelenir ve ardından ChaCha20 ile gizlenir) ve ek sınıflandırma için kullanılabilir. Hiçbir durumda bir paketi sınıflandırmak için deneme DH veya diğer asimetrik kripto işlemleri gerekli değildir.

- 16-byte başlık oluştur
- Yük (payload) oluştur
- Başlığı AD olarak kullanarak ChaChaPoly ile yükü şifrele
- Başlığı şifrele

### Notlar

#### Özet

Tüm eşlerden gelen neredeyse tüm mesajlar için, Connection ID şifrelemesi için ChaCha20 anahtarı, netDb'de yayınlanan hedef router'ın tanıtım anahtarıdır.

- Başlığın ilk 8 baytını (Hedef Bağlantı ID'si) intro key ile çöz
- Hedef Bağlantı ID'sine göre bağlantıyı ara
- Bağlantı bulunursa ve veri fazındaysa, veri fazı bölümüne git
- Bağlantı bulunamazsa, handshake bölümüne git
- Not: Peer Test ve Hole Punch mesajları da test veya relay nonce'undan oluşturulan Hedef Bağlantı ID'si ile aranabilir.

Tek istisnalar Bob'un Alice'e gönderdiği ilk mesajlardır (Session Created veya Retry) burada Alice'in tanıtım anahtarı henüz Bob tarafından bilinmez. Bu durumlarda, Bob'un tanıtım anahtarı anahtar olarak kullanılır.

- Başlığın 8-15 baytlarını (paket türü, sürüm ve ağ kimliği) intro anahtarıyla çöz. Geçerli bir Session Request, Token Request, Peer Test veya Hole Punch ise devam et
- Geçerli bir mesaj değilse, paket kaynak IP/portu ile bekleyen giden bağlantıyı ara, paketi Session Created veya Retry olarak ele al. Başlığın ilk 8 baytını doğru anahtarla ve başlığın 8-15 baytlarını (paket türü, sürüm ve ağ kimliği) yeniden çöz. Geçerli bir Session Created veya Retry ise devam et
- Geçerli bir mesaj değilse, başarısız ol veya olası sıra dışı veri fazı paketi olarak kuyruğa al
- Session Request/Created, Retry, Token Request, Peer Test ve Hole Punch için başlığın 16-31 baytlarını çöz
- Session Request/Created için ephemeral anahtarını çöz
- Tüm başlık alanlarını doğrula, geçerli değilse dur
- Başlığı mixHash() yap
- Session Request/Created/Confirmed için payload'ı Noise kullanarak çöz
- Retry ve veri fazı için payload'ı ChaChaPoly kullanarak çöz
- Başlık ve payload'ı işle

Protokol, birden fazla geri dönüş adımında veya karmaşık buluşsal yöntemlerde ek şifreleme işlemleri gerektirebilecek paket sınıflandırma işlemlerini en aza indirmek üzere tasarlanmıştır. Ayrıca, alınan paketlerin büyük çoğunluğu kaynak IP/port'a göre (muhtemelen pahalı) geri dönüş araması ve ikinci bir başlık şifre çözme işlemi gerektirmeyecektir. Yalnızca Session Created ve Retry (ve muhtemelen henüz belirlenmemiş diğerleri) geri dönüş işlemi gerektirecektir. Bir uç nokta oturum oluşturulduktan sonra IP veya port'unu değiştirirse, oturumu aramak için bağlantı ID'si hâlâ kullanılır. Örneğin aynı IP'ye sahip ancak farklı port'a sahip farklı bir oturum arayarak oturumu bulmak için buluşsal yöntemler kullanmak asla gerekli değildir.

- Başlığın 8-15 baytlarını (paket türü, sürüm ve ağ kimliği) doğru anahtarla şifrele
- Başlığı AD olarak kullanarak ChaChaPoly ile yükü şifrele
- Başlık ve yükü işle

#### Ayrıntılar

Bu nedenle, alıcı döngü mantığında önerilen işleme adımları şunlardır:

1) Yerel tanıtım anahtarını kullanarak ChaCha20 ile ilk 8 baytı şifrele çözün ve Hedef Bağlantı ID'sini kurtarın. Bağlantı ID'si mevcut veya bekleyen bir gelen oturum ile eşleşiyorsa:

2) Bağlantı kimliği mevcut bir oturumla eşleşmiyorsa: 8-15 baytlarındaki düz metin başlığının geçerli olup olmadığını kontrol edin (herhangi bir başlık koruma işlemi yapmadan). Net kimliğinin ve protokol sürümünün geçerli olduğunu, mesaj türünün Session Request veya oturum dışında izin verilen diğer mesaj türleri (TBD) olduğunu doğrulayın.

3) Paketin kaynak IP/port'una göre bekleyen giden oturumu ara.

4)  Aynı port üzerinde SSU 1 çalışıyorsa, mesajı bir SSU 1 paketi olarak işlemeyi deneyin.

Genel olarak, bir oturum (handshake veya veri aşamasında) beklenmeyen bir mesaj türüne sahip bir paket aldıktan sonra asla yok edilmemelidir. Bu, paket enjeksiyon saldırılarını önler. Bu paketler ayrıca, başlık şifre çözme anahtarlarının artık geçerli olmadığı durumlarda, bir handshake paketinin yeniden iletiminden sonra da yaygın olarak alınacaktır.

Çoğu durumda, paketi basitçe düşürün. Bir uygulama, yanıt olarak daha önce gönderilen paketi (handshake mesajı veya ACK 0) yeniden iletebilir, ancak bunu yapmak zorunda değildir.

    a)  Using the appropriate key, decrypt the header bytes 8-15 to recover the version, net ID, and message type.
    b)  If the message type is Session Confirmed, it is a long header. Verify the net ID and protocol version are valid. Decrypt the bytes 15-31 of the header with ChaCha20 using the local intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise.
    c)  If the message type is valid but not Session Confirmed, it is a short header. Verify the net ID and protocol version are valid. decrypt the rest of the message with ChaCha20/Poly1305 using the session key, using the decrypted 16-byte header as the AD.
    d)  (optional) If connection ID is a pending inbound session awaiting a Session Confirmed message, but the net ID, protocol, or message type is not valid, it could be a Data message received out-of-order before the Session Confirmed, so the data phase header protection keys are not yet known, and the header bytes 8-15 were incorrectly decrypted. Queue the message, and attempt to decrypt it once the Session Confirmed message is received.
    e)  If b) or c) fails, drop the message.

Bob olarak Session Created gönderdikten sonra, beklenmeyen paketler genellikle Session Confirmed paketlerinin kaybolması veya sıra dışı gelmesi nedeniyle şifresi çözülemeyen Data paketleridir. Paketleri kuyruğa alın ve Session Confirmed paketlerini aldıktan sonra şifrelerini çözmeye çalışın.

    a)  If all is valid and the message type is Session Request, decrypt bytes 16-31 of the header and the 32-byte X value with ChaCha20 using the local intro key.

    - If the token at header bytes 24-31 is accepted, then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Created in response.
    - If the token is not accepted, send a Retry message to the source IP/port with a token. Do not attempt to decrypt the message with Noise to avoid DDoS attacks.

    b)  If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.
    c)  If a) or b) fails, go to step 3)

Bob olarak Session Confirmed aldıktan sonra, beklenmeyen paketler genellikle yeniden iletilen Session Confirmed paketleridir, çünkü Session Confirmed'ın ACK 0'ı kaybolmuştur. Beklenmeyen paketler düşürülebilir. Bir implementasyon, yanıt olarak bir ACK bloğu içeren bir Data paketi gönderebilir, ancak bu zorunlu değildir.

    a)  If found, re-decrypt the first 8 bytes with ChaCha20 using Bob's introduction key to recover the Destination Connection ID.
    b)  If the connection ID matches the pending session: Using the correct key, decrypt bytes 8-15 of the header to recover the version, net ID, and message type. Verify the net ID and protocol version are valid, and the message type is Session Created or Retry, or other message type allowed out-of-session (TBD).

    - If all is valid and the message type is Session Created, decrypt the next 16 bytes of the header and the 32-byte Y value with ChaCha20 using Bob's intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Confirmed in response.
    - If all is valid and the message type is Retry, decrypt bytes 16-31 of the header with ChaCha20 using Bob's intro key. Decrypt and validate the message using ChaCha20/Poly1305 using TBD as the key and TBD as the nonce and the decrypted 32-byte header as the AD. Resend a Session Request with the received token in response.
    - If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.

    > c)  If a pending outbound session is not found, or the connection ID does not match the pending session, drop the message, unless the port is shared with SSU 1.

Session Created ve Session Confirmed için, uygulamalar mixHash() fonksiyonunu başlık üzerinde çağırmadan ve Noise AEAD ile yükü şifresini çözmeye çalışmadan ÖNCE tüm şifresi çözülen başlık alanlarını (Connection ID'ler, paket numarası, paket türü, sürüm, id, frag ve flags) dikkatli bir şekilde doğrulamalıdır. Noise AEAD şifre çözme işlemi başarısız olursa, bir uygulama hash durumunu saklamıyor ve "geri almıyorsa", mixHash() handshake durumunu bozmuş olacağından dolayı daha fazla işlem yapılamaz.

#### Hata İşleme

Gelen paketlerin aynı gelen port üzerinde sürüm 1 veya 2 olup olmadığını verimli bir şekilde tespit etmek mümkün olmayabilir. Yukarıdaki adımlar, her iki protokol sürümünü kullanan deneme DH işlemlerini önlemek için SSU 1 işleminden önce yapılması mantıklı olabilir.

Gerekirse belirlenecek.

IPv4 varsayar, ek padding dahil değil, IP ve UDP başlık boyutları dahil değil. Padding yalnızca SSU 1 için mod-16 padding'dir.

**SSU 1**

### Sürüm Tespit

**SSU 2**

### Token'lar

Yukarıda belirttiğimiz gibi, token rastgele üretilmiş 8 baytlık bir değer olmalıdır; yeniden kullanım saldırıları nedeniyle sunucu sırrı ile IP, port'un hash'i veya HMAC'i gibi opak bir değer üretmemelidir. Ancak bu, teslim edilmiş token'ların geçici ve (isteğe bağlı olarak) kalıcı olarak saklanmasını gerektirir. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf), sunucu sırrı ve IP adresinin 16 baytlık HMAC'ini kullanır ve sunucu sırrı her iki dakikada bir döner. Daha uzun sunucu sırrı ömrü ile benzer bir şeyi araştırmalıyız. Token'a bir zaman damgası gömersek, bu bir çözüm olabilir, ancak 8 baytlık bir token bunun için yeterince büyük olmayabilir.

Gerekliyse belirlenecek.

## Önerilen Sabitler

- Giden handshake yeniden iletim zaman aşımı: 1.25 saniye, üstel geri çekilme ile (1.25, 3.75 ve 8.75 saniyede yeniden iletimler)
- Toplam giden handshake zaman aşımı: 15 saniye
- Gelen handshake yeniden iletim zaman aşımı: 1 saniye, üstel geri çekilme ile (1, 3 ve 7 saniyede yeniden iletimler)
- Toplam gelen handshake zaman aşımı: 12 saniye
- Yeniden deneme gönderildikten sonra zaman aşımı: 9 saniye
- ACK gecikmesi: max(10, min(rtt/6, 150)) ms
- Anında ACK gecikmesi: min(rtt/16, 5) ms
- Maksimum ACK aralıkları: 256?
- Maksimum ACK derinliği: 512?
- Padding dağılımı: 0-15 bayt veya daha fazla
- Veri aşaması minimum yeniden iletim zaman aşımı: 1 saniye, [RFC-6298](https://tools.ietf.org/html/rfc6298)'de olduğu gibi
- Veri aşaması için yeniden iletim zamanlayıcıları hakkında ek rehberlik için ayrıca [RFC-6298](https://tools.ietf.org/html/rfc6298)'e bakınız.

## Paket Ek Yükü Analizi

IPv4 varsayar, ekstra dolgu dahil değildir, IP ve UDP başlık boyutları dahil değildir. Dolgu yalnızca SSU 1 için mod-16 dolgusudur.

**SSU 1**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MAC</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">40</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">304</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. extended options</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">79</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">336</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 64 byte Ed25519 sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">462</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">512</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 391 byte ident and 64 byte sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (RI)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1014</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1051</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header, 1000 byte RI</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">51</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">2254</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>
**SSU 2**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MACs</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">87</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">96</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime, Address blocks</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1005</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1085</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1000 byte compressed RI block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">46</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1314</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>    
## Sorunlar ve Gelecek Çalışmalar

### Token'lar

Yukarıda, yeniden kullanım saldırılarına karşı önlem almak amacıyla, sunucu gizliliğinin ve IP'nin karmasını (hash) ya da HMAC'ini oluşturmak gibi şeffaf olmayan bir değer değil, rastgele üretilmiş 8 baytlık bir değerin belirteç olarak kullanılması gerektiğini belirttik. Ancak bu yöntem, teslim edilen belirteçlerin geçici ve (isteğe bağlı olarak) kalıcı olarak saklanmasını gerektirir. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf), bir sunucu gizliliği ve IP adresinin 16 baytlık bir HMAC'ini kullanır ve sunucu gizliliği her iki dakikada bir değiştirilir. Biz de benzer bir şeyi, ancak daha uzun bir sunucu gizliliği ömrüyle araştırmalıyız. Belirtece bir zaman damgası gömmeyi düşünürsek bu bir çözüm olabilir, ancak 8 baytlık bir belirteç bunun için yeterince büyük olmayabilir.

## Kaynaklar

- **[Common]** [Ortak Yapılar Spesifikasyonu](/docs/specs/common-structures)
- **[ECIES]** [ECIES-X25519-AEAD-Ratchet Spesifikasyonu](/docs/specs/ecies)
- **[NetDB]** [Ağ Veritabanı](/docs/overview/network-database)
- **[NOISE]** [Noise Protokol Çerçevesi](https://noiseprotocol.org/noise.html)
- **[Nonces]** [Nonce'leri Saymayan Düşmanlar](https://eprint.iacr.org/2019/624.pdf)
- **[NTCP]** [NTCP Transport](/docs/transport/ntcp)
- **[NTCP2]** [NTCP2 Spesifikasyonu](/docs/specs/ntcp2)
- **[PMTU]** [Yol MTU Keşfi](https://en.wikipedia.org/wiki/Path_MTU_Discovery)
- **[Prop104]** [Teklif 104: TLS Transport](/proposals/104-tls-transport)
- **[Prop109]** [Teklif 109: Takılabilir Transport](/proposals/109-pt-transport)
- **[Prop158]** [Teklif 158: IPv6 Transport Geliştirmeleri](/proposals/158-ipv6-transport-enhancements)
- **[Prop159]** [Teklif 159: SSU2](/proposals/159-ssu2)
- **[RFC-2104]** [RFC 2104: HMAC](https://tools.ietf.org/html/rfc2104)
- **[RFC-3449]** [RFC 3449: TCP Performans Etkileri](https://tools.ietf.org/html/rfc3449)
- **[RFC-3526]** [RFC 3526: MODP Grupları](https://tools.ietf.org/html/rfc3526)
- **[RFC-5681]** [RFC 5681: TCP Sıkışıklık Kontrolü](https://tools.ietf.org/html/rfc5681)
- **[RFC-5869]** [RFC 5869: HKDF](https://tools.ietf.org/html/rfc5869)
- **[RFC-6151]** [RFC 6151: MD5 Güvenlik Hususları](https://tools.ietf.org/html/rfc6151)
- **[RFC-6298]** [RFC 6298: TCP Yeniden İletim Zamanlayıcısı](https://tools.ietf.org/html/rfc6298)
- **[RFC-6437]** [RFC 6437: IPv6 Akış Etiketi](https://tools.ietf.org/html/rfc6437)
- **[RFC-7539]** [RFC 7539: ChaCha20/Poly1305](https://tools.ietf.org/html/rfc7539)
- **[RFC-7748]** [RFC 7748: Güvenlik için Eliptik Eğriler](https://tools.ietf.org/html/rfc7748)
- **[RFC-7905]** [RFC 7905: TLS için ChaCha20-Poly1305 Şifre Paketleri](https://tools.ietf.org/html/rfc7905)
- **[RFC-9000]** [RFC 9000: QUIC Transport Protokolü](https://datatracker.ietf.org/doc/html/rfc9000)
- **[RFC-9001]** [RFC 9001: QUIC'i Güvenceye Almak için TLS Kullanımı](https://datatracker.ietf.org/doc/html/rfc9001)
- **[RFC-9002]** [RFC 9002: QUIC Kayıp Tespiti ve Sıkışıklık Kontrolü](https://datatracker.ietf.org/doc/html/rfc9002)
- **[RouterAddress]** [RouterAddress Yapısı](/docs/specs/common-structures#struct-routeraddress)
- **[RouterIdentity]** [RouterIdentity Yapısı](/docs/specs/common-structures#struct-routeridentity)
- **[SigningPublicKey]** [SigningPublicKey Türü](/docs/specs/common-structures#type-signingpublickey)
- **[SSU]** [SSU Transport](/docs/transport/ssu)
- **[STS]** [İstasyondan İstasyona Protokolü](https://en.wikipedia.org/wiki/Station-to-Station_protocol)
- **[Ticket1112]** [I2P Bilet 1112](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1112)
- **[Ticket1849]** [I2P Bilet 1849](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1849)
- **[WireGuard]** [WireGuard Protokolü](https://www.wireguard.com/papers/wireguard.pdf)
