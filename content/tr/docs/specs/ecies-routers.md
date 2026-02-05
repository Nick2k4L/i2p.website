---
title: "ECIES-X25519 Router Mesajları"
description: "X25519 kullanan ECIES router'larına garlic message şifrelemesi için spesifikasyon"
slug: "ecies-routers"
category: "Protokoller"
lastUpdated: "2025-03"
accurateFor: "0.9.65"
---

## Not

0.9.49 sürümünden itibaren desteklenmektedir. Ağ dağıtımı ve testler devam etmektedir. Küçük revizyonlara tabi olabilir. Bkz. [öneri 156](/proposals/156-ecies-routers).

## Genel Bakış

Bu belge, [ECIES-X25519](/docs/specs/ecies) tarafından tanıtılan kripto primitiflerini kullanarak ECIES router'lara garlic mesaj şifrelemesini belirtir. Bu, router'ları ElGamal'dan ECIES-X25519 anahtarlarına dönüştürmek için genel [öneri 156](/proposals/156-ecies-routers)'nın bir parçasıdır. Bu spesifikasyon 0.9.49 sürümü itibariyle uygulanmıştır.

ECIES router'ları için gerekli tüm değişikliklerin genel görünümü için [proposal 156](/proposals/156-ecies-routers)'ya bakın. ECIES-X25519 hedeflerine Garlic Messages için [ECIES-X25519](/docs/specs/ecies)'e bakın.

### Kriptografik İlkeller

Bu spesifikasyonu uygulamak için gerekli temel öğeler şunlardır:

- [Cryptography](/docs/specs/cryptography) belgesindeki gibi AES-256-CBC
- STREAM ChaCha20/Poly1305 fonksiyonları: ENCRYPT(k, n, plaintext, ad) ve DECRYPT(k, n, ciphertext, ad) - [NTCP2](/docs/specs/ntcp2), [ECIES-X25519](/docs/specs/ecies), ve [RFC-7539](https://tools.ietf.org/html/rfc7539) belgeleirndeki gibi
- X25519 DH fonksiyonları - [NTCP2](/docs/specs/ntcp2) ve [ECIES-X25519](/docs/specs/ecies) belgelerindeki gibi
- HKDF(salt, ikm, info, n) - [NTCP2](/docs/specs/ntcp2) ve [ECIES-X25519](/docs/specs/ecies) belgelerindeki gibi

Başka yerlerde tanımlanan diğer Noise fonksiyonları:

- MixHash(d) - [NTCP2](/docs/specs/ntcp2) ve [ECIES-X25519](/docs/specs/ecies)'te olduğu gibi
- MixKey(d) - [NTCP2](/docs/specs/ntcp2) ve [ECIES-X25519](/docs/specs/ecies)'te olduğu gibi

## Tasarım

ECIES Router SKM, Destination'lar için [ECIES](/docs/specs/ecies)'te belirtilen tam bir Ratchet SKM'ye ihtiyaç duymaz. IK desenini kullanan anonim olmayan mesajlar için herhangi bir gereksinim yoktur. Tehdit modeli, Elligator2 ile kodlanmış geçici anahtarlar gerektirmez.

Bu nedenle, router SKM, tunnel oluşturma için [Prop152](/proposals/152-ecies-tunnels)'de belirtilen ile aynı olan Noise "N" desenini kullanacaktır. Hedefler için [ECIES](/docs/specs/ecies)'te belirtilen ile aynı payload formatını kullanacaktır. [ECIES](/docs/specs/ecies)'te belirtilen IK'nın sıfır statik anahtar (bağlama veya oturum yok) modu kullanılmayacaktır.

Arama isteklerindeki yanıtlar, arama sırasında talep edilirse bir ratchet tag ile şifrelenecektir. Bu, [Prop154](/proposals/154-ecies-lookups) belgesinde açıklandığı gibi olup, şimdi [I2NP](/docs/specs/i2np) içinde belirtilmiştir.

Bu tasarım, router'ın tek bir ECIES Session Key Manager'a sahip olmasını sağlar. Hedefler için [ECIES](/docs/specs/ecies) belgesinde açıklandığı gibi "ikili anahtar" Session Key Manager'ları çalıştırmaya gerek yoktur. Router'lar yalnızca bir genel anahtara sahiptir.

Bir ECIES router'ının ElGamal statik anahtarı yoktur. Router'ın hala ElGamal router'ları üzerinden tunnel'lar oluşturmak ve ElGamal router'larına şifrelenmiş mesajlar göndermek için bir ElGamal uygulamasına ihtiyacı vardır.

Bir ECIES router, 0.9.46 öncesi floodfill router'lardan NetDB sorguları yanıtı olarak alınan ElGamal-etiketli mesajları almak için kısmi bir ElGamal Session Key Manager gerektirebilir, çünkü bu router'lar [Prop152](/proposals/152-ecies-tunnels)'de belirtilen ECIES-etiketli yanıtların bir implementasyonuna sahip değildir. Aksi takdirde, bir ECIES router 0.9.46 öncesi bir floodfill router'dan şifrelenmiş yanıt talep etmeyebilir.

Bu isteğe bağlıdır. Karar, çeşitli I2P uygulamalarında değişiklik gösterebilir ve ağın 0.9.46 veya daha yüksek sürüme yükseltilmiş olan miktarına bağlı olabilir. Bu tarih itibariyle, ağın yaklaşık %85'i 0.9.46 veya daha yüksek sürümdedir.

### Noise Protocol Framework

Bu spesifikasyon, [Noise Protocol Framework](https://noiseprotocol.org/noise.html) (Revizyon 34, 2018-07-11) temel alınarak gereksinimleri sağlar. Noise terminolojisinde Alice başlatıcı, Bob ise yanıtlayıcıdır.

Noise_N_25519_ChaChaPoly_SHA256 Noise protokolüne dayanmaktadır. Bu Noise protokolü aşağıdaki temel bileşenleri kullanır:

- **Tek Yönlü El Sıkışma Deseni: N** - Alice statik anahtarını Bob'a iletmez (N)
- **DH Fonksiyonu: X25519** - [RFC-7748](https://tools.ietf.org/html/rfc7748)'de belirtildiği gibi 32 bayt anahtar uzunluğuna sahip X25519 DH.
- **Şifreleme Fonksiyonu: ChaChaPoly** - [RFC-7539](https://tools.ietf.org/html/rfc7539) bölüm 2.8'de belirtildiği gibi AEAD_CHACHA20_POLY1305. 12 bayt nonce, ilk 4 bayt sıfıra ayarlı. [NTCP2](/docs/specs/ntcp2)'dekiyle aynı.
- **Hash Fonksiyonu: SHA256** - Standart 32-bayt hash, I2P'de zaten yaygın olarak kullanılıyor.

### Handshake Kalıpları

El sıkışmalar [Noise](https://noiseprotocol.org/noise.html) el sıkışma modellerini kullanır.

Aşağıdaki harf eşlemesi kullanılır:

- e = tek kullanımlık geçici anahtar
- s = statik anahtar
- p = mesaj yükü

Build request, Noise N deseni ile aynıdır. Bu aynı zamanda [NTCP2](/docs/specs/ntcp2)'de kullanılan XK desenindeki ilk (Oturum İsteği) mesajı ile de aynıdır.

```
<- s
  ...
  e es p ->
```
### Mesaj şifreleme

Mesajlar oluşturulur ve hedef router'a asimetrik olarak şifrelenir. Mesajların bu asimetrik şifrelemesi şu anda [Cryptography](/docs/specs/cryptography) bölümünde tanımlandığı gibi ElGamal'dir ve SHA-256 sağlama toplamı içerir. Bu tasarım ileri gizlilik (forward-secret) sağlamaz.

ECIES tasarımı, ileri gizlilik, bütünlük ve kimlik doğrulama için ECIES-X25519 ephemeral-static DH, HKDF ve ChaCha20/Poly1305 AEAD ile tek yönlü Noise kalıbı "N"yi kullanır. Alice anonim mesaj gönderici, bir router veya hedef. Hedef ECIES router Bob'dur.

### Yanıt şifreleme

Yanıtlar bu protokolün parçası değildir, çünkü Alice anonimdir. Yanıt anahtarları, varsa, istek mesajında paketlenir. Database Lookup Messages için [I2NP spesifikasyonuna](/docs/specs/i2np) bakın.

Database Lookup mesajlarına verilen yanıtlar Database Store veya Database Search Reply mesajlarıdır. Bunlar, [I2NP](/docs/specs/i2np) ve [Prop154](/proposals/154-ecies-lookups)'te belirtildiği üzere 32-byte yanıt anahtarı ve 8-byte yanıt etiketi ile Existing Session mesajları olarak şifrelenir.

Database Store mesajlarına açık yanıtlar yoktur. Gönderen, kendisine yönelik bir Garlic Message içinde Delivery Status mesajı içeren kendi yanıtını paketleyebilir.

## Spesifikasyon

X25519: [ECIES](/docs/specs/ecies) bölümüne bakın.

Router Kimliği ve Anahtar Sertifikası: [Ortak Yapılar](/docs/specs/common-structures) bölümüne bakın.

### İstek Şifreleme

İstek şifrelemesi, Noise "N" desenini kullanarak [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) ve [Prop152](/proposals/152-ecies-tunnels) belgelerinde belirtilen ile aynıdır.

Aramalardan gelen yanıtlar, aramada talep edilirse ratchet etiketi ile şifrelenecektir. Database Lookup istek mesajları, [I2NP](/docs/specs/i2np) ve [Prop154](/proposals/154-ecies-lookups)'te belirtildiği şekilde 32-baytlık yanıt anahtarı ve 8-baytlık yanıt etiketini içerir. Anahtar ve etiket, yanıtı şifrelemek için kullanılır.

Tag setleri oluşturulmaz. ECIES-X25519-AEAD-Ratchet [Prop144](/proposals/144-ecies-x25519-aead-ratchet) ve [ECIES](/docs/specs/ecies) belgelerinde belirtilen sıfır statik anahtar şeması kullanılmayacaktır. Ephemeral (geçici) anahtarlar Elligator2 ile kodlanmayacaktır.

Genellikle bunlar New Session mesajları olacaktır ve sıfır statik anahtar ile gönderilecektir (bağlama veya oturum yok), çünkü mesajın göndereni anonimdir.

#### Başlangıç ck ve h için KDF

Bu, "N" deseni için standart [Noise](https://noiseprotocol.org/noise.html) protokolü ve standart protokol adıdır. Bu, tunnel oluşturma mesajları için [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) ve [Prop152](/proposals/152-ecies-tunnels) belgelerinde belirtilen ile aynıdır.

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
#### Mesaj için KDF

Mesaj oluşturucular her mesaj için geçici bir X25519 anahtar çifti oluşturur. Geçici anahtarlar mesaj başına benzersiz olmalıdır. Bu, tunnel yapım mesajları için [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) ve [Prop152](/proposals/152-ecies-tunnels) spesifikasyonlarında belirtilen ile aynıdır.

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
#### Yük Verisi

Payload, [ECIES](/docs/specs/ecies) ve [Prop144](/proposals/144-ecies-x25519-aead-ratchet) belgelerinde tanımlanan aynı blok formatındadır. Tüm mesajlar tekrar saldırısı önleme için bir DateTime bloğu içermelidir.

## Uygulama Notları

- Eski router'lar, router'ın şifreleme türünü kontrol etmez ve ElGamal-şifrelenmiş mesajlar gönderir. Bazı yeni router'lar hatalıdır ve çeşitli türlerde bozuk mesajlar gönderir. Uygulayıcılar, CPU kullanımını azaltmak için mümkünse bu kayıtları DH işleminden önce tespit etmeli ve reddetmelidir.

## Referanslar

- [Ortak Yapılar](/docs/specs/common-structures)
- [Kriptografi](/docs/specs/cryptography)
- [ECIES](/docs/specs/ecies)
- [I2NP](/docs/specs/i2np)
- [Noise Protocol Framework](https://noiseprotocol.org/noise.html)
- [NTCP2](/docs/specs/ntcp2)
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet)
- [Prop152](/proposals/152-ecies-tunnels)
- [Prop154](/proposals/154-ecies-lookups)
- [Prop156](/proposals/156-ecies-routers)
- [RFC-7539](https://tools.ietf.org/html/rfc7539)
- [RFC-7748](https://tools.ietf.org/html/rfc7748)
- [Tunnel Oluşturma-ECIES](/docs/specs/tunnel-creation-ecies)
