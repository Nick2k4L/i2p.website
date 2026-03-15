---
title: "ECIES-X25519-AEAD-Ratchet"
aliases:
  - "/tr/proposals/144-ecies-x25519"
  - "/tr/proposals/144-ecies-x25519/"
number: "144"
author: "zzz, chisana, orignal"
created: "2018-11-22"
lastupdated: "2025-03-05"
status: "Kapatıldı"
thread: "http://zzz.i2p/topics/2639"
target: "0.9.46"
implementedin: "0.9.46"
toc: true
---
## Not
Ağ dağıtım ve testi devam etmektedir.
Küçük revizyonlara tabidir.
Resmi spesifikasyon için [SPEC](/docs/specs/ecies/) adresine bakın.

Aşağıdaki özellikler 0.9.46 itibarıyla uygulanmamıştır:

- MessageNumbers, Options ve Termination blokları
- Protokol katmanı yanıtları
- Sıfır statik anahtar
- Multicast


## Genel Bakış

Bu, I2P'nin başlangıcından bu yana ilk yeni uçtan uca şifreleme türüdür
ve ElGamal/AES+SessionTags [Elg-AES](/docs/specs/elgamal-aes/) yerine geçecektir.

Aşağıdaki önceki çalışmalara dayanmaktadır:

- Ortak yapılar spesifikasyonu [Common Structures](/docs/specs/common-structures/)
- LS2 dahil [I2NP](/docs/specs/i2np/) spesifikasyonu
- ElGamal/AES+Session Tags [Elg-AES](/docs/specs/elgamal-aes/)
- [http://zzz.i2p/topics/1768](http://zzz.i2p/topics/1768) yeni asimetrik kripto genel bakışı
- Düşük seviye kripto genel bakışı [CRYPTO-ELG](/docs/specs/cryptography/)
- ECIES [http://zzz.i2p/topics/2418](http://zzz.i2p/topics/2418)
- [NTCP2](/docs/specs/ntcp2/) [Proposal 111](/proposals/111-ntcp-2/)
- 123 Yeni netDB Girişleri
- 142 Yeni Şifreleme Şablonu
- [Noise](https://noiseprotocol.org/noise.html) protokolü
- [Signal](https://signal.org/docs/) çift ratchet algoritması

Amaç, uçtan uca,
hedef-hedef iletişim için yeni şifreleme desteği sağlamaktır.

Tasarım, Signal'ın çift ratchet'ini içeren bir Noise el sıkışma ve veri aşaması kullanacaktır.

Bu teklifte Signal ve Noise'a yapılan tüm atıflar yalnızca arka plan bilgisi içindir.
Bu teklifi anlamak veya uygulamak için Signal ve Noise protokollerini
bilmek gerekli değildir.


### Mevcut ElGamal Kullanımları

Gözden geçirme olarak,
256 baytlık ElGamal genel anahtarlar aşağıdaki veri yapılarında bulunabilir.
Ortak yapılar spesifikasyonuna bakın.

- Bir Yönlendirici Kimliğinde
  Bu, yönlendiricinin şifreleme anahtarıdır.

- Bir Hedeften
  Hedefin genel anahtarı, 0.6 sürümünde devre dışı bırakılan
  eski i2cp-to-i2cp şifrelemesi için kullanılmıştı, şu anda
  LeaseSet şifrelemesi için IV olarak kullanılır, bu da kullanım dışıdır.
  LeaseSet'teki genel anahtar bunun yerine kullanılır.

- Bir LeaseSet'te
  Bu, hedefin şifreleme anahtarıdır.

- Bir LS2'de
  Bu, hedefin şifreleme anahtarıdır.



### Anahtar Sertifikalarındaki Şifreleme Türleri

Gözden geçirme olarak,
imza türleri için destek eklerken şifreleme türleri için destek ekledik.
Şifreleme türü alanı hem Hedeflerde hem de Yönlendirici Kimliklerinde her zaman sıfırdır.
Bunu değiştirmenin gerekip gerekmediği belirsizdir.
Ortak yapılar spesifikasyonuna bakın [Common Structures](/docs/specs/common-structures/).




### Asimetrik Kripto Kullanımları

Gözden geçirme olarak, ElGamal'ı şu amaçlarla kullanıyoruz:

1) Tünel Oluşturma mesajları (anahtar Yönlendirici Kimliğinde)
   Bu teklif kapsamında değiştirilmez.
   Teklif 152'ye bakın [Proposal 152](/proposals/152-ecies-tunnels).

2) Yönlendirici-yönlendirici netdb ve diğer I2NP mesajlarının şifrelenmesi (Anahtar Yönlendirici Kimliğinde)
   Bu teklife bağlıdır.
   1) için bir teklif gerektirir veya anahtarı RI seçeneklerine koymak.

3) İstemci Uçtan Uca ElGamal+AES/SessionTag (anahtar LeaseSet'tedir, Hedef anahtarı kullanılmaz)
   Değiştirilmesi BU teklif kapsamındadır.

4) NTCP1 ve SSU için geçici DH
   Değiştirilmesi bu teklif kapsamında değildir.
   NTCP2 için teklif 111'e bakın.
   SSU2 için mevcut bir teklif yoktur.


### Amaçlar

- Geriye dönük uyumlu olmak
- LS2'yi (teklif 123) gerektirmek ve onun üzerine inşa etmek
- NTCP2 için eklenen yeni kripto veya primitiflerden yararlanmak (teklif 111)
- Desteği için yeni kripto veya primitifler gerekmemesi
- Şifreleme ve imzalama arasındaki ayrımı korumak; tüm mevcut ve gelecekteki sürümleri desteklemek
- Hedefler için yeni kripto etkinleştirmek
- Yönlendiriciler için yeni kripto etkinleştirmek, ancak yalnızca sarımsak mesajları için - tünel oluşturma
  ayrı bir teklif olur
- 32 baytlık ikili hedef karmalarına dayanan hiçbir şeyi bozmamak, örneğin bittorrent
- Geçici-statik DH kullanarak 0-RTT mesaj teslimini korumak
- Bu protokol katmanında mesajların arabelleğe alınmasını/kuyruğa alınmasını gerektirmemek;
  yanıt beklenmeden her iki yönde sınırsız mesaj teslimini sürdürmek
- 1 RTT sonra geçici-geçici DH'ye yükseltmek
- Sıra dışı mesajların işlenmesini korumak
- 256-bit güvenlik korumak
- İleri gizlilik eklemek
- Kimlik doğrulama (AEAD) eklemek
- ElGamal'dan çok daha CPU verimli olmak
- DH'yi verimli hale getirmek için Java jbigi'ye güvenmemek
- DH işlemlerini en aza indirmek
- ElGamal'dan (514 baytlık ElGamal bloğu) çok daha bant genişliği verimli olmak
- Aynı tünelde istenirse hem yeni hem de eski kriptoyu desteklemek
- Alıcı, aynı tünelde gelen yeni ve eski kriptoyu verimli bir şekilde ayırt edebilmelidir
- Diğerleri yeni ve eski veya gelecekteki kriptoyu birbirinden ayırt edemez
- Yeni ve Mevcut Oturum uzunluğu sınıflandırmasını ortadan kaldırmak (dolgu desteği)
- Yeni I2NP mesajları gerekmemesi
- AES yükünde SHA-256 kontrol toplamını AEAD ile değiştirmek
- İletim ve alma oturumlarını bağlamanın desteklenmesi, böylece
  onaylar yalnızca dış bantta değil, aynı zamanda protokol içinde gerçekleşebilir.
  Bu ayrıca yanıtların hemen ileri gizliliğe sahip olmasını sağlayacaktır.
- CPU yükü nedeniyle şu anda yapmadığımız bazı mesajların (RouterInfo depoları)
  uçtan uca şifrelenmesini etkinleştirmek.
- I2NP Sarımsak Mesajını veya
  Sarımsak Mesaj Teslim Talimatları biçimini değiştirmemek.
- Sarımsak Çıngırığı Seti ve Çıngırak biçimlerinde kullanılmayan veya gereksiz alanları ortadan kaldırmak.

Oturum etiketlerindeki birkaç sorunu ortadan kaldırın, bunlara dahildir:

- AES'i ilk yanıt gelene kadar kullanamama
- Etiket teslimi varsayıldığında güvenilmezlik ve durmalar
- Özellikle ilk teslimatta bant genişliği verimsizliği
- Etiketleri depolamak için devasa alan verimsizliği
- Etiketleri teslim etmek için devasa bant genişliği yükü
- Aşırı karmaşık, uygulanması zor
- Çeşitli kullanım senaryoları için (akış vs. veri birimleri, sunucu vs. istemci, yüksek vs. düşük bant genişliği) ayarlamak zor
- Etiket teslimi nedeniyle bellek tükenme açıkları


### Amaç Dışı / Kapsam Dışı

- LS2 biçim değişiklikleri (teklif 123 tamamlandı)
- Yeni DHT döndürme algoritması veya paylaşılan rastgele üretim
- Tünel oluşturma için yeni şifreleme.
  Teklif 152'ye bakın [Proposal 152](/proposals/152-ecies-tunnels).
- Tünel katmanı şifrelemesi için yeni şifreleme.
  Teklif 153'e bakın [Proposal 153](/proposals/153-chacha20-layer-encryption).
- I2NP DLM / DSM / DSRM mesajlarının şifrelenmesi, iletimi ve alımı yöntemleri.
  Değiştirilmiyor.
- LS1'den LS2'ye veya ElGamal/AES'ten bu teklife iletişim desteklenmiyor.
  Bu teklif çift yönlü bir protokoldür.
  Hedefler, aynı tünelleri kullanarak iki leaseset yayınlamak
  veya her iki şifreleme türünü LS2'ye koymak yoluyla geriye dönük uyumluluğu ele alabilir.
- Tehdit modeli değişiklikleri
- Uygulama ayrıntıları burada tartışılmamıştır ve her projeye bırakılmıştır.
- (İyimser) Multicast desteği için uzantılar veya bağlantı noktaları ekleme



### Gerekçe

ElGamal/AES+SessionTag yaklaşık 15 yıldır tek uçtan uca protokolumuz olmuştur,
temelde protokole herhangi bir değişiklik yapılmadan.
Şimdi daha hızlı olan kriptografik primitifler var.
Protokolün güvenliğini artırmamız gerekiyor.
Ayrıca, protokolün bellek ve bant genişliği yükünü en aza indirmek için
sezgisel stratejiler ve geçici çözümler geliştirdik, ancak bu stratejiler
kırılgan, ayarlaması zor ve protokolü daha da kırılgan hale getirerek
oturumun düşmesine neden oluyor.

Yaklaşık aynı süre boyunca, ElGamal/AES+SessionTag spesifikasyonu ve ilgili
belgeler, oturum etiketlerinin teslim edilmesinin ne kadar bant genişliği açısından maliyetli olduğunu
açıklamış ve oturum etiketi teslimini "senkronize PRNG" ile değiştirmeyi önermiştir.
Senkronize PRNG, ortak bir tohumdan türetilen her iki uçta da aynı etiketleri deterministik olarak üretir.
Senkronize PRNG, aynı zamanda "ratchet" olarak da adlandırılabilir.
Bu teklif (sonunda) bu ratchet mekanizmasını belirtir ve etiket teslimini ortadan kaldırır.

Oturum etiketlerini oluşturmak için bir ratchet (senkronize PRNG) kullanarak,
Yeni Oturum mesajında ve gerektiğinde sonraki mesajlarda oturum etiketlerinin
gönderilmesinin yükünü ortadan kaldırırız. Tipik 32 etiketlik bir etiket seti için bu 1KB'dır.
Bu aynı zamanda gönderen tarafın oturum etiketlerini depolamasını da ortadan kaldırır,
bu nedenle depolama gereksinimlerini yarıya indirir.

Anahtar Teslimi Sahtekarlığı (KCI) saldırılarını önlemek için, tam iki yönlü bir el sıkışma, Noise IK deseni gibi gerekir.
[NOISE](https://noiseprotocol.org/noise.html) adresindeki Noise "Payload Security Properties" tablosuna bakın.
KCI hakkında daha fazla bilgi için şu makaleye bakın https://www.usenix.org/system/files/conference/woot15/woot15-paper-hlauschek.pdf



### Tehdit Modeli

Tehdit modeli NTCP2 (teklif 111) içinkinden biraz farklıdır.
MitM düğümleri OBEP ve IBGW'dir ve floodfill'lerle işbirliği yaparak
mevcut veya tarihsel küresel NetDB'ye tam erişime sahip oldukları varsayılır.

Amaç, bu MitM'lerin trafiği
yeni ve Mevcut Oturum mesajları olarak veya yeni kripto ile eski kripto olarak sınıflandırmasını önlemektir.



## Ayrıntılı Teklif

Bu teklif, ElGamal/AES+SessionTags yerine geçecek yeni bir uçtan uca protokol tanımlar.
Tasarım, Signal'ın çift ratchet'ini içeren bir Noise el sıkışma ve veri aşaması kullanacaktır.


### Kriptografik Tasarım Özeti

Yeniden tasarlanacak protokolün beş bölümü vardır:


- 1) Yeni ve Mevcut Oturum konteyner biçimleri
  yeni biçimlerle değiştirilir.
- 2) ElGamal (256 bayt genel anahtarlar, 128 bayt özel anahtarlar) yerine
  ECIES-X25519 (32 bayt genel ve özel anahtarlar) kullanılır
- 3) AES yerine
  AEAD_ChaCha20_Poly1305 (aşağıda ChaChaPoly olarak kısaltılır)
- 4) SessionTags, ratchet'lerle değiştirilir,
  bu temelde kriptografik, senkronize PRNG'dir.
- 5) ElGamal/AES+SessionTags spesifikasyonunda tanımlanan AES yükü,
  NTCP2'dekine benzer bir blok biçimine değiştirilir.

Beş değişikliğin her birinin aşağıda kendi bölümü vardır.


### I2P için Yeni Kriptografik Primitifler

Mevcut I2P yönlendirici uygulamaları,
şu anda I2P protokolleri için gerekli olmayan
aşağıdaki standart kriptografik primitiflerin uygulamalarını gerektirir:

- ECIES (ancak bu temelde X25519'dir)
- Elligator2

Henüz [NTCP2](/docs/specs/ntcp2/) ([Proposal 111](/proposals/111-ntcp-2/)) uygulamamış olan
mevcut I2P yönlendirici uygulamaları ayrıca şunları gerektirir:

- X25519 anahtar üretimi ve DH
- AEAD_ChaCha20_Poly1305 (aşağıda ChaChaPoly olarak kısaltılır)
- HKDF


### Şifreleme Türü

(LS2'de kullanılan) şifreleme türü 4'tür.
Bu, little-endian 32 baytlık X25519 genel anahtarını
ve burada belirtilen uçtan uca protokolünü gösterir.

Şifreleme türü 0 ElGamal'dır.
Şifreleme türleri 1-3 ECIES-ECDH-AES-SessionTag için ayrılmıştır, teklif 145'e bakın [Proposal 145](/proposals/145-ecies).


### Noise Protokol Çerçevesi

Bu teklif, Noise Protokol Çerçevesi'ne dayalı gereksinimleri sağlar
[NOISE](https://noiseprotocol.org/noise.html) (Revizyon 34, 2018-07-11).
Noise, [SSU](/docs/legacy/ssu/) protokolünün temeli olan
İstasyon-İstasyon protokolüne [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol) benzer özelliklere sahiptir. Noise terminolojisinde, Alice
başlatıcıdır ve Bob yanıtlayıcıdır.

Bu teklif, Noise protokolü Noise_IK_25519_ChaChaPoly_SHA256 üzerine kuruludur.
(Gerçek tanımlayıcı başlangıç anahtar türetme işlevi için
"Noise_IKelg2_25519_ChaChaPoly_SHA256"
I2P uzantılarını belirtmek için - aşağıda KDF 1 bölümüne bakın)
Bu Noise protokolü aşağıdaki primitifleri kullanır:

- Etkileşimli El Sıkışma Deseni: IK
  Alice, statik anahtarını Bob'a hemen iletir (I)
  Alice, Bob'un statik anahtarını zaten bilir (K)

- Tek Yönlü El Sıkışma Deseni: N
  Alice, statik anahtarını Bob'a iletmez (N)

- DH İşlevi: X25519
  [RFC-7748](https://tools.ietf.org/html/rfc7748) belirtildiği gibi 32 bayt uzunluğunda anahtar ile X25519 DH.

- Şifreleme İşlevi: ChaChaPoly
  [RFC-7539](https://tools.ietf.org/html/rfc7539) bölüm 2.8'de belirtildiği gibi AEAD_CHACHA20_POLY1305.
  12 baytlık nonce, ilk 4 bayt sıfıra ayarlanır.
  [NTCP2](/docs/specs/ntcp2/) ile aynıdır.

- Hash İşlevi: SHA256
  I2P'de yaygın olarak kullanılan standart 32 baytlık hash.


### Çerçeveye Eklemeler

Bu teklif, Noise_IK_25519_ChaChaPoly_SHA256'a aşağıdaki geliştirmeleri tanımlar. Bunlar genellikle
[NOISE](https://noiseprotocol.org/noise.html) bölüm 13'teki kuralları takip eder.

1) Açık metin geçici anahtarlar [Elligator2](https://elligator.cr.yp.to/) ile kodlanır.

2) Yanıt, açık metin bir etiketle öncelenir.

3) Mesajlar 1, 2 ve veri aşaması için yük biçimi tanımlanır.
   Elbette, bu Noise'de tanımlanmamıştır.

Tüm mesajlar bir [I2NP](/docs/specs/i2np/) Sarımsak Mesaj başlığı içerir.
Veri aşaması, Noise veri aşamasına benzer ancak onunla uyumlu olmayan bir şifreleme kullanır.


### El Sıkışma Desenleri

El sıkışmalar [Noise](https://noiseprotocol.org/noise.html) el sıkışma desenlerini kullanır.

Aşağıdaki harf eşlemesi kullanılır:

- e = tek kullanımlık geçici anahtar
- s = statik anahtar
- p = mesaj yükü

Tek kullanımlık ve Sınırsız oturumlar Noise N desenine benzer.

```

<- s
  ...
  e es p ->

```

Bağlı oturumlar Noise IK desenine benzer.

```

<- s
  ...
  e es s ss p ->
  <- tag e ee se
  <- p
  p ->

```


### Oturumlar

Mevcut ElGamal/AES+SessionTag protokolü tek yönlüdür.
Bu katmanda, alıcı bir mesajın nereden geldiğini bilmez.
Giden ve gelen oturumlar ilişkilendirilmez.
Onaylar, bir DeliveryStatusMessage kullanılarak dış bantta yapılır
(bir GarlicMessage içinde sarılmış) çıngırakta.

Tek yönlü bir protokolde önemli verimsizlikler vardır.
Herhangi bir yanıt da pahalı bir 'Yeni Oturum' mesajı kullanmalıdır.
Bu, daha yüksek bant genişliği, CPU ve bellek kullanımına neden olur.

Tek yönlü bir protokolde ayrıca güvenlik zayıflıkları vardır.
Tüm oturumlar geçici-statik DH'ye dayanır.
Bir dönüş yolu olmadan, Bob'un statik anahtarını
geçici anahtara "ratchetlemesi" için bir yol yoktur.
Bir mesajın nereden geldiğini bilmeden, alınan geçici anahtarı
giden mesajlar için kullanmanın bir yolu yoktur,
bu nedenle ilk yanıt da geçici-statik DH kullanır.

Bu teklif için, çift yönlü bir protokol oluşturmak için iki mekanizma tanımlıyoruz -
"eşleştirme" ve "bağlama".
Bu mekanizmalar artan verimlilik ve güvenlik sağlar.


### Oturum Bağlamı

ElGamal/AES+SessionTags gibi, tüm gelen ve giden oturumlar
verilen bir bağlamda olmalıdır, ya yönlendiricinin bağlamı ya da
belirli bir yerel hedefin bağlamı.
Java I2P'de, bu bağlam Oturum Anahtar Yöneticisi olarak adlandırılır.

Oturumlar bağlamlar arasında paylaşılmamalıdır, çünkü bu
çeşitli yerel hedefler arasında veya bir yerel hedef ile bir yönlendirici arasında
korelasyona izin verir.

Belirli bir hedef hem ElGamal/AES+SessionTags hem de
bu teklifi desteklediğinde, her iki tür oturum da bir bağlamı paylaşabilir.
Aşağıdaki bölüm 1c)'ye bakın.



### Gelen ve Giden Oturumları Eşleştirme

Bir giden oturum başlatıcıda (Alice) oluşturulduğunda,
yeni bir gelen oturum oluşturulur ve giden oturumla eşleştirilir,
eğer yanıt beklenmiyorsa (örneğin ham veri birimleri).

Yeni bir giden oturum oluşturulduğunda her zaman yeni bir gelen oturumla eşleştirilir,
eğer yanıt istenmiyorsa (örneğin ham veri birimleri).

Yanıt isteniyorsa ve uzak uç hedefine veya yönlendiriciye bağlıysa,
bu yeni giden oturum bu hedefe veya yönlendiriciye bağlı olur
ve bu hedefe veya yönlendiriciye önceki giden oturumun yerini alır.

Gelen ve giden oturumları eşleştirmek, DH anahtarlarını ratchetleme
kapasitesine sahip çift yönlü bir protokol sağlar.



### Oturumları ve Hedefleri Bağlama

Verilen bir hedefe veya yönlendiriciye yalnızca bir giden oturum vardır.
Verilen bir hedeften veya yönlendiriciden birkaç mevcut gelen oturum olabilir.
Genellikle, yeni bir gelen oturum oluşturulduğunda ve bu oturumda trafik alındığında
(bu bir ACK görevi görür), diğerleri bir dakika veya civarında
hızla sona ermek üzere işaretlenir.
Önceki gönderilen (PN) değeri kontrol edilir ve önceki gelen oturumda
(eklenti boyutu içinde) alınmamış mesaj yoksa,
önceki oturum hemen silinebilir.


Bir giden oturum başlatıcıda (Alice) oluşturulduğunda,
uzak uç Hedefe (Bob) bağlıdır
ve eşleştirilmiş gelen oturum da uzak uç Hedefe bağlı olur.
Oturumlar ratchetlendiğinde, uzak uç Hedefe bağlı kalmaya devam ederler.

Bir gelen oturum alıcıda (Bob) oluşturulduğunda,
uzak uç Hedefe (Alice) Alice'in seçeneğine göre bağlı olabilir.
Eğer Alice, Yeni Oturum mesajında bağlama bilgilerini (statik anahtarını) içerirse,
oturum bu hedefe bağlı olur
ve bir giden oturum oluşturulur ve aynı Hedefe bağlı olur.
Oturumlar ratchetlendiğinde, uzak uç Hedefe bağlı kalmaya devam ederler.


### Bağlama ve Eşleştirmenin Faydaları

Yaygın, akış durumunda, Alice ve Bob'un protokolü şu şekilde kullanmasını bekleriz:

- Alice, yeni giden oturumunu uzak uç hedefe (Bob) bağlı yeni bir gelen oturumla eşleştirir.
- Alice, bağlama bilgilerini ve imzasını, ve bir yanıt isteğini
  Bob'a gönderilen Yeni Oturum mesajına ekler.
- Bob, yeni gelen oturumunu uzak uç hedefe (Alice) bağlı yeni bir giden oturumla eşleştirir.
- Bob, yeni bir DH anahtarıyla bir ratchet ile Alice'e bir yanıt (onay) gönderir.
- Alice, Bob'un yanıtını aldıktan ve ratchetledikten sonra, Bob'un yeni anahtarıyla yeni bir giden oturuma ratchetler, mevcut gelen oturuma bağlıdır.

Bir gelen oturumu uzak uç Hedefe bağlayarak ve gelen oturumu
aynı Hedefe bağlı giden oturumla eşleştirerek iki büyük fayda sağlarız:

1) Bob'dan Alice'e ilk yanıt geçici-geçici DH kullanır

2) Alice, Bob'un yanıtını aldıktan ve ratchetledikten sonra, Alice'ten Bob'a tüm sonraki mesajlar
geçici-geçici DH kullanır.


### Mesaj Onayları

ElGamal/AES+SessionTags'de, bir LeaseSet bir sarımsak çıngırak olarak paketlendiğinde
veya etiketler teslim edildiğinde, gönderen yönlendirici bir onay ister.
Bu, bir DeliveryStatus Mesajı içeren ayrı bir sarımsak çıngıraktır.
Ek güvenlik için, DeliveryStatus Mesajı bir Sarımsak Mesajı içinde sarılır.
Bu mekanizma protokol açısından dış banttadır.

Yeni protokolde, gelen ve giden oturumlar eşleştirildiğinden,
onayları iç bantta yapabiliriz. Ayrı bir çıngırak gerekmez.

Açık bir onay, yalnızca I2NP bloğu olmayan Mevcut Oturum mesajıdır.
Ancak, çoğu durumda açık bir onaydan kaçınılabilir, çünkü ters yönde trafik olur.
Uygulamaların, akış veya uygulama katmanının yanıt vermesi için zaman tanıması amacıyla
kısa bir süre (belki yüz ms) beklemesi istenebilir.

Uygulamalar ayrıca, I2NP bloğu işlendikten sonra herhangi bir onay göndermeyi ertelemelidir,
çünkü Sarımsak Mesajı bir lease set içeren bir Database Store Mesajı içerebilir.
Onayın yönlendirilmesi için güncel bir lease set gerekir
ve bağlama statik anahtarının doğrulanması için uzak uç hedef
(lease set içinde yer alır) gerekir.


### Oturum Zaman Aşımı

Giden oturumlar her zaman gelen oturumlardan önce sona ermelidir.
Bir giden oturum sona erdiğinde ve yeni bir tane oluşturulduğunda, yeni bir eşleştirilmiş gelen
oturum da oluşturulur. Eski bir gelen oturum varsa,
sona ermesine izin verilir.


### Multicast

Belirlenecek


### Tanımlar
Kullandığımız kriptografik yapı taşlarına karşılık gelen aşağıdaki işlevleri tanımlıyoruz.

ZEROLEN
    sıfır uzunluklu bayt dizisi

CSRNG(n)
    n baytlık, kriptografik olarak güvenli rastgele sayı üretecinin çıktısı.

H(p, d)
    kişiselleştirilmiş bir dize p ve veri d alan ve
    32 bayt uzunluğunda bir çıktı üreten SHA-256 hash işlevi.
    [NOISE](https://noiseprotocol.org/noise.html) adresinde tanımlandığı gibi.
    Aşağıda || ekleme anlamına gelir.

    SHA-256 şu şekilde kullanılır::

        H(p, d) := SHA-256(p || d)

MixHash(d)
    önceki bir hash h ve yeni veri d alan,
    32 bayt uzunluğunda bir çıktı üreten SHA-256 hash işlevi.
    Aşağıda || ekleme anlamına gelir.

    SHA-256 şu şekilde kullanılır::

        MixHash(d) := h = SHA-256(h || d)

STREAM
    [RFC-7539](https://tools.ietf.org/html/rfc7539) adresinde belirtildiği gibi ChaCha20/Poly1305 AEAD.
    S_KEY_LEN = 32 ve S_IV_LEN = 12.

    ENCRYPT(k, n, plaintext, ad)
        Şifreleme anahtarı k ve benzersiz olmak zorunda olan nonce n kullanarak plaintext'i şifreler.
        İlişkili veri ad isteğe bağlıdır.
        Plaintext boyutundan 16 bayt daha büyük olan bir şifreli metin döndürür (HMAC için).

        Anahtar gizliyse, şifreli metnin tamamı rastgele veriden ayırt edilemez olmalıdır.

    DECRYPT(k, n, ciphertext, ad)
        Şifreleme anahtarı k ve nonce n kullanarak ciphertext'i çözer.
        İlişkili veri ad isteğe bağlıdır.
        Plaintext'i döndürür.

DH
    32 bayt özel anahtarlar, 32 bayt genel anahtarlar, 32 bayt çıktı üreten X25519 genel anahtar anlaşma sistemi.
    Aşağıdaki işlevlere sahiptir:

    GENERATE_PRIVATE()
        Yeni bir özel anahtar üretir.

    DERIVE_PUBLIC(privkey)
        Verilen özel anahtara karşılık gelen genel anahtarı döndürür.

    GENERATE_PRIVATE_ELG2()
        Elligator2 kodlaması için uygun genel anahtara eşlenen yeni bir özel anahtar üretir.
        Rastgele oluşturulan özel anahtarların yarısının uygun olmayacağı ve atılması gerektiğini unutmayın.

    ENCODE_ELG2(pubkey)
        Verilen genel anahtara karşılık gelen Elligator2 kodlu genel anahtarı döndürür (ters eşleme).
        Kodlu anahtarlar little endian'dır.
        Kodlu anahtar, 256 bit rastgele veriden ayırt edilemez olmalıdır.
        Spesifikasyon için aşağıda Elligator2 bölümüne bakın.

    DECODE_ELG2(pubkey)
        Verilen Elligator2 kodlu genel anahtara karşılık gelen genel anahtarı döndürür.
        Spesifikasyon için aşağıda Elligator2 bölümüne bakın.

    DH(privkey, pubkey)
        Verilen özel ve genel anahtarlardan paylaşılan bir gizli anahtar üretir.

HKDF(salt, ikm, info, n)
    İyi entropiye sahip olması gereken (ancak düzgün rastgele bir dize olması gerekmez) bazı giriş anahtar malzemesi ikm, 32 bayt uzunluğunda bir tuz
    ve bağlama özgü bir 'info' değeri alan ve n bayt uzunluğunda, anahtar malzemesi olarak kullanılması uygun bir çıktı üreten
    kriptografik bir anahtar türetme işlevi.

    [RFC-5869](https://tools.ietf.org/html/rfc5869) adresinde belirtildiği gibi HKDF'yi kullanın, HMAC hash işlevi olarak [RFC-2104](https://tools.ietf.org/html/rfc2104) adresinde belirtildiği gibi SHA-256 kullanın.
    Bu, SALT_LEN'in maksimum 32 bayt olduğu anlamına gelir.

MixKey(d)
    Önceki chainKey ve yeni veri d ile HKDF() kullanır ve
    yeni chainKey ve k'yi ayarlar.
    [NOISE](https://noiseprotocol.org/noise.html) adresinde tanımlandığı gibi.

    HKDF şu şekilde kullanılır::

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]



### 1) Mesaj biçimi


### Mevcut Mesaj Biçiminin Gözden Geçirilmesi

[I2NP](/docs/specs/i2np/) adresinde belirtildiği gibi Sarımsak Mesaj şu şekildedir.
Ara atlamaların yeni ve eski kriptoyu birbirinden ayırt edememesi bir tasarım hedefidir,
bu nedenle bu biçim değişemez, hatta uzunluk alanı gereksiz olsa bile.
Biçim, tam 16 baytlık başlıkla gösterilmiştir, ancak
gerçek başlık farklı bir biçimde olabilir, kullanılan taşıma yöntemine bağlı olarak.

Şifresi çözüldüğünde veriler, bir dizi Sarımsak Çıngırak ve ek verilerden, ayrıca bir Çıngırak Seti olarak bilinir.

Ayrıntılar ve tam bir spesifikasyon için [I2NP](/docs/specs/i2np/) adresine bakın.


```

+----+----+----+----+----+----+----+----+
  |type|      msg_id       |  expiration
  +----+----+----+----+----+----+----+----+
                           |  size   |chks|
  +----+----+----+----+----+----+----+----+
  |      length       |                   |
  +----+----+----+----+                   +
  |          encrypted data               |
  ~                                       ~
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

```


### Şifreli Veri Biçiminin Gözden Geçirilmesi

15 yıldan fazla süredir kullanılan mevcut mesaj biçimi,
ElGamal/AES+SessionTags'tir.
ElGamal/AES+SessionTags'te, iki mesaj biçimi vardır:

1) Yeni oturum:
- 514 baytlık ElGamal bloğu
- AES bloğu (en az 128 bayt, 16'nın katı)

2) Mevcut oturum:
- 32 baytlık Oturum Etiketi
- AES bloğu (en az 128 bayt, 16'nın katı)

128'e kadar minimum dolgu, Java I2P'de uygulandığı gibi ancak alımda zorunlu tutulmaz.

Bu mesajlar, uzunluğun bilindiği bir I2NP sarımsak mesajında kapsüllenir.

Etiket olmayan uzunluğa dolgu tanımlanmadığına dikkat edin,
bu nedenle Yeni Oturum her zaman (mod 16 == 2),
ve Mevcut Oturum her zaman (mod 16 == 0) olur.
Bunu düzeltmemiz gerekiyor.

Alıcı önce ilk 32 baytı Oturum Etiketi olarak arar.
Bulunursa, AES bloğunu çözer.
Bulunamazsa ve veri en az (514+16) uzunluğundaysa, ElGamal bloğunu çözmeyi dener
ve başarılı olursa, AES bloğunu çözer.


### Yeni Oturum Etiketleri ve Signal ile Karşılaştırma

Signal Çift Ratchet'te, başlık şunları içerir:

- DH: Geçerli ratchet genel anahtarı
- PN: Önceki zincir mesaj uzunluğu
- N: Mesaj Numarası

Signal'ın "gönderme zincirleri" yaklaşık olarak bizim etiket setlerimize eşdeğerdir.
Bir oturum etiketi kullanarak bunların çoğunu ortadan kaldırabiliriz.

Yeni Oturum'da, açık metin başlığa yalnızca genel anahtarı koyarız.

Mevcut Oturum'da, başlık için bir oturum etiketi kullanırız.
Oturum etiketi, geçerli ratchet genel anahtarıyla
ve mesaj numarasıyla ilişkilidir.

Yeni ve Mevcut Oturum'da, PN ve N şifreli gövdededir.

Signal'de, her şey sürekli ratchetlenir. Yeni bir DH genel anahtarı alındığında,
alıcı ratchetlemeli ve yeni genel anahtarını geri göndermelidir, bu aynı zamanda
alınan genel anahtar için onay görevi görür.
Bu bizim için çok fazla DH işlemi olur.
Bu yüzden alınan anahtarın onayını ve yeni genel anahtarın iletimini ayırıyoruz.
Yeni DH genel anahtarıyla oluşturulan oturum etiketini kullanan herhangi bir mesaj bir onay oluşturur.
Yalnızca yeniden anahtarlamak istediğimizde yeni genel anahtar göndeririz.

DH'nin ratchetlenmesi gerekmeden önceki maksimum mesaj sayısı 65535'tir.

Bir oturum anahtarı teslim ederken, "Etiket Seti"ni ondan türetiriz,
böylece oturum etiketlerini ayrıca teslim etmek zorunda kalmayız.
Bir Etiket Seti en fazla 65536 etiket olabilir.
Ancak, alıcılar tüm olası etiketleri aynı anda üretmek yerine
"bak-ahead" stratejisi uygulamalıdır.
Son iyi alınan etiketten sonra en fazla N etiket üretin.
N en fazla 128 olabilir, ancak 32 veya daha az daha iyi bir seçim olabilir.



### 1a) Yeni oturum biçimi

Yeni Oturum Tek Kullanımlık Genel Anahtarı (32 bayt)
Şifreli veri ve MAC (kalan baytlar)

Yeni Oturum mesajı, gönderenin statik genel anahtarını içerebilir veya içermeyebilir.
Eğer dahil edilirse, ters oturum bu anahtara bağlı olur.
Yanıt bekleniyorsa, yani akış ve yanıtlanabilir veri birimleri için,
statik anahtar dahil edilmelidir.
Ham veri birimleri için dahil edilmemelidir.

Yeni Oturum mesajı, tek yönlü Noise [NOISE](https://noiseprotocol.org/noise.html) deseni
"N" (statik anahtar gönderilmemişse),
veya iki yönlü desen "IK" (statik anahtar gönderilmişse) gibidir.



### 1b) Yeni oturum biçimi (bağlama ile)

Uzunluk 96 + yük uzunluğudur.
Şifreli biçim:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   Yeni Oturum Geçici Genel Anahtarı    |
  +             32 bayt                  +
  |     Elligator2 ile kodlanmış           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +         Statik Anahtar                    +
  |       ChaCha20 şifreli veri         |
  +            32 bayt                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Mesaj Kimlik Doğrulama Kodu |
  +    (MAC) Statik Anahtar Bölümü için       +
  |             16 bayt                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Yük Bölümü            +
  |       ChaCha20 şifreli veri         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Mesaj Kimlik Doğrulama Kodu |
  +         (MAC) Yük Bölümü için     +
  |             16 bayt                  |
  +----+----+----+----+----+----+----+----+

  Genel Anahtar :: 32 bayt, little endian, Elligator2, açık metin

  Statik Anahtar şifreli veri :: 32 bayt

  Yük Bölümü şifreli veri :: kalan veri eksi 16 bayt

  MAC :: Poly1305 mesaj kimlik doğrulama kodu, 16 bayt

```


### Yeni Oturum Geçici Anahtarı

Geçici anahtar 32 bayttır, Elligator2 ile kodlanmıştır.
Bu anahtar yeniden kullanılmaz; her mesajla birlikte
yeni bir anahtar oluşturulur, yeniden iletimler dahil.

### Statik Anahtar

Çözüldüğünde, Alice'in X25519 statik anahtarı, 32 bayt.


### Yük

Şifreli uzunluk verinin geri kalanıdır.
Çözülmüş uzunluk şifreli uzunluktan 16 bayt daha azdır.
Yük bir DateTime bloğu içermelidir ve genellikle bir veya daha fazla Sarımsak Çıngırak bloğu içerir.
Biçim ve ek gereksinimler için aşağıda yük bölümüne bakın.



### 1c) Yeni oturum biçimi (bağlama olmadan)

Yanıt gerekmiyorsa, statik anahtar gönderilmez.


Uzunluk 96 + yük uzunluğudur.
Şifreli biçim:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   Yeni Oturum Geçici Genel Anahtarı    |
  +             32 bayt                  +
  |     Elligator2 ile kodlanmış           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Bayrak Bölümü               +
  |       ChaCha20 şifreli veri         |
  +            32 bayt                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Mesaj Kimlik Doğrulama Kodu |
  +         (MAC) yukarıdaki bölüm için       +
  |             16 bayt                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Yük Bölümü            +
  |       ChaCha20 şifreli veri         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Mesaj Kimlik Doğrulama Kodu |
  +         (MAC) Yük Bölümü için     +
  |             16 bayt                  |
  +----+----+----+----+----+----+----+----+

  Genel Anahtar :: 32 bayt, little endian, Elligator2, açık metin

  Bayrak Bölümü şifreli veri :: 32 bayt

  Yük Bölümü şifreli veri :: kalan veri eksi 16 bayt

  MAC :: Poly1305 mesaj kimlik doğrulama kodu, 16 bayt

```

### Yeni Oturum Geçici Anahtarı

Alice'in geçici anahtarı.
Geçici anahtar 32 bayttır, Elligator2 ile kodlanmış, little endian.
Bu anahtar yeniden kullanılmaz; her mesajla birlikte
yeni bir anahtar oluşturulur, yeniden iletimler dahil.


### Bayrak Bölümü Çözülmüş veri

Bayrak bölümü hiçbir şey içermiyor.
Her zaman 32 bayt uzunluğundadır, çünkü bağlama ile Yeni Oturum mesajlarındaki statik anahtarla
aynı uzunlukta olmalıdır. Bob, 32 baytın tümünün sıfır olup olmadığını test ederek
bunun bir statik anahtar mı yoksa bayrak bölümü mü olduğunu belirler.

TODO burada herhangi bir bayrak gerekli mi?

### Yük

Şifreli uzunluk verinin geri kalanıdır.
Çözülmüş uzunluk şifreli uzunluktan 16 bayt daha azdır.
Yük bir DateTime bloğu içermelidir ve genellikle bir veya daha fazla Sarımsak Çıngırak bloğu içerir.
Biçim ve ek gereksinimler için aşağıda yük bölümüne bakın.




### 1d) Tek kullanımlık biçim (bağlama veya oturum yok)

Yalnızca tek bir mesajın gönderileceği varsayılıyorsa,
oturum kurulumu veya statik anahtar gerekmez.


Uzunluk 96 + yük uzunluğudur.
Şifreli biçim:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |       Geçici Genel Anahtar            |
  +             32 bayt                  +
  |     Elligator2 ile kodlanmış           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Bayrak Bölümü               +
  |       ChaCha20 şifreli veri         |
  +            32 bayt                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Mesaj Kimlik Doğrulama Kodu |
  +         (MAC) yukarıdaki bölüm için       +
  |             16 bayt                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Yük Bölümü            +
  |       ChaCha20 şifreli veri         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Mesaj Kimlik Doğrulama Kodu |
  +         (MAC) Yük Bölümü için     +
  |             16 bayt                  |
  +----+----+----+----+----+----+----+----+

  Genel Anahtar :: 32 bayt, little endian, Elligator2, açık metin

  Bayrak Bölümü şifreli veri :: 32 bayt

  Yük Bölümü şifreli veri :: kalan veri eksi 16 bayt

  MAC :: Poly1305 mesaj kimlik doğrulama kodu, 16 bayt

```


### Yeni Oturum Tek Kullanımlık Anahtarı

Tek kullanımlık anahtar 32 bayttır, Elligator2 ile kodlanmış, little endian.
Bu anahtar yeniden kullanılmaz; her mesajla birlikte
yeni bir anahtar oluşturulur, yeniden iletimler dahil.


### Bayrak Bölümü Çözülmüş veri

Bayrak bölümü hiçbir şey içermiyor.
Her zaman 32 bayt uzunluğundadır, çünkü bağlama ile Yeni Oturum mesajlarındaki statik anahtarla
aynı uzunlukta olmalıdır. Bob, 32 baytın tümünün sıfır olup olmadığını test ederek
bunun bir statik anahtar mı yoksa bayrak bölümü mü olduğunu belirler.

TODO burada herhangi bir bayrak gerekli mi?

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                                       |
  +             Tüm sıfırlar                 +
  |              32 bayt                 |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+

  sıfırlar:: Tüm sıfırlar, 32 bayt.

```


### Yük

Şifreli uzunluk verinin geri kalanıdır.
Çözülmüş uzunluk şifreli uzunluktan 16 bayt daha azdır.
Yük bir DateTime bloğu içermelidir ve genellikle bir veya daha fazla Sarımsak Çıngırak bloğu içerir.
Biçim ve ek gereksinimler için aşağıda yük bölümüne bakın.



### 1f) Yeni Oturum Mesajı için KDF'ler

### Başlangıç Zincir Anahtarı için KDF

Bu, değiştirilmiş bir protokol adı ile IK için standart [NOISE](https://noiseprotocol.org/noise.html) 'dur.
Aynı başlatıcıyı hem IK deseni (bağlı oturumlar) hem de N deseni (bağlı olmayan oturumlar) için kullandığımıza dikkat edin.

Protokol adı iki nedenden dolayı değiştirilmiştir.
İlk olarak, geçici anahtarların Elligator2 ile kodlandığını belirtmek,
ikinci olarak, etiket değerini karıştırmak için ikinci mesajdan önce MixHash()'in çağrıldığını belirtmek.

```

Bu "e" mesaj desenidir:

  // Protokol adını tanımla.
  Protokol_adı = "Noise_IKelg2+hs2_25519_ChaChaPoly_SHA256"
   (40 bayt, US-ASCII kodlu, NULL sonlandırma yok).

  // 32 bayt Hash h tanımla
  h = SHA256(protokol_adı);

  32 baytlık zincirleme anahtarı tanımla ck. h verilerini ck'ye kopyala.
  ZincirAnahtarı = h

  // MixHash(null prologue)
  h = SHA256(h);

  // buraya kadar, Alice tarafından tüm giden bağlantılar için önceden hesaplanabilir

```


### Bayrak/Statik Anahtar Bölümü Şifreli İçerikleri için KDF

```

Bu "e" mesaj desenidir:

  // Bob'un X25519 statik anahtarları
  // bpk lease sette yayınlanır
  bsk = GENERATE_PRIVATE()
  bpk = DERIVE_PUBLIC(bsk)

  // Bob statik genel anahtarı
  // MixHash(bpk)
  // || aşağıda ekleme anlamına gelir
  h = SHA256(h || bpk);

  // buraya kadar, Bob tarafından tüm gelen bağlantılar için önceden hesaplanabilir

  // Alice'in X25519 geçici anahtarları
  aesk = GENERATE_PRIVATE_ELG2()
  aepk = DERIVE_PUBLIC(aesk)

  // Alice geçici genel anahtarı
  // MixHash(aepk)
  // || aşağıda ekleme anlamına gelir
  h = SHA256(h || aepk);

  // h, Yeni Oturum Mesajında AEAD için ilişkili veri olarak kullanılır
  // Yeni Oturum Yanıt KDF'si için Hash h'yi koru
  // eapk, Yeni Oturum mesajının
  // başında açık metin olarak gönderilir
  elg2_aepk = ENCODE_ELG2(aepk)
  // Bob tarafından çözüldüğünde
  aepk = DECODE_ELG2(elg2_aepk)

  "e" mesaj deseninin sonu.

  Bu "es" mesaj desenidir:

  // Noise es
  paylaşılanGizli = DH(aesk, bpk) = DH(bsk, aepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(paylaşılanGizli)
  // ChaChaPoly parametreleri şifrelemek/çözmek için
  anahtarverisi = HKDF(zincirAnahtarı, paylaşılanGizli, "", 64)
  zincirAnahtarı = anahtarverisi[0:31]

  // AEAD parametreleri
  k = anahtarverisi[32:63]
  n = 0
  ad = h
  şifreliMetin = ENCRYPT(k, n, bayrak/statik anahtar bölümü, ad)

  "es" mesaj deseninin sonu.

  Bu "s" mesaj desenidir:

  // MixHash(şifreliMetin)
  // Yük bölümü KDF'si için sakla
  h = SHA256(h || şifreliMetin)

  // Alice'in X25519 statik anahtarları
  ask = GENERATE_PRIVATE()
  apk = DERIVE_PUBLIC(ask)

  "s" mesaj deseninin sonu.


```



### Yük Bölümü için KDF (Alice statik anahtarı ile)

```

Bu "ss" mesaj desenidir:

  // Noise ss
  paylaşılanGizli = DH(ask, bpk) = DH(bsk, apk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(paylaşılanGizli)
  // ChaChaPoly parametreleri şifrelemek/çözmek için
  // Statik Anahtar Bölümünden zincirAnahtarı
  paylaşılanGizli = X25519 DH sonucu olarak ayarla
  anahtarverisi = HKDF(zincirAnahtarı, paylaşılanGizli, "", 64)
  zincirAnahtarı = anahtarverisi[0:31]

  // AEAD parametreleri
  k = anahtarverisi[32:63]
  n = 0
  ad = h
  şifreliMetin = ENCRYPT(k, n, yük, ad)

  "ss" mesaj deseninin sonu.

  // MixHash(şifreliMetin)
  // Yeni Oturum Yanıt KDF'si için sakla
  h = SHA256(h || şifreliMetin)

```


### Yük Bölümü için KDF (Alice statik anahtarı olmadan)

Bu bir Noise "N" desenidir, ancak bağlı oturumlar için olduğu gibi aynı "IK" başlatıcısını kullanırız.

Yeni Oturum mesajları, statik anahtar çözülüp incelenene kadar Alice'in statik anahtarını içerip içermediği
belirlenemez. Bu nedenle, alıcı tüm
Yeni Oturum mesajları için "IK" durum makinesini kullanmalıdır.
Statik anahtar tüm sıfırlarsa, "ss" mesaj deseni atlanmalıdır.



```

zincirAnahtarı = Bayrak/Statik anahtar bölümünden
  k = Bayrak/Statik anahtar bölümünden
  n = 1
  ad = Bayrak/Statik anahtar bölümünden h
  şifreliMetin = ENCRYPT(k, n, yük, ad)

```



### 1g) Yeni Oturum Yanıt biçimi

Tek bir Yeni Oturum mesajına yanıt olarak bir veya daha fazla Yeni Oturum Yanıtı gönderilebilir.
Her yanıt, oturum için bir EtiketSet'ten üretilen bir etiketle öncelenir.

Yeni Oturum Yanıtı iki kısımdan oluşur.
İlk kısım, öncelenmiş bir etiketle Noise IK el sıkışmasının tamamlanmasıdır.
İlk kısmın uzunluğu 56 bayttır.
İkinci kısım veri aşaması yüküdür.
İkinci kısmın uzunluğu 16 + yük uzunluğudur.

Toplam uzunluk 72 + yük uzunluğudur.
Şifreli biçim:

```

+----+----+----+----+----+----+----+----+
  |       Oturum Etiketi   8 bayt           |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Geçici Genel Anahtar           +
  |                                       |
  +            32 bayt                   +
  |     Elligator2 ile kodlanmış           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Mesaj Kimlik Doğrulama Kodu |
  +  (MAC) Anahtar Bölümü için (veri yok)      +
  |             16 bayt                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Yük Bölümü            +
  |       ChaCha20 şifreli veri         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Mesaj Kimlik Doğrulama Kodu |
  +         (MAC) Yük Bölümü için     +
  |             16 bayt                  |
  +----+----+----+----+----+----+----+----+

  Etiket :: 8 bayt, açık metin

  Genel Anahtar :: 32 bayt, little endian, Elligator2, açık metin

  MAC :: Poly1305 mesaj kimlik doğrulama kodu, 16 bayt
         Not: ChaCha20 açık metin verisi boştur (ZEROLEN)

  Yük Bölümü şifreli veri :: kalan veri eksi 16 bayt

  MAC :: Poly1305 mesaj kimlik doğrulama kodu, 16 bayt

```

### Oturum Etiketi
Etiket, aşağıda DH Başlatma KDF'sinde başlatıldığı gibi
Oturum Etiketleri KDF'sinde üretilir.
Bu, yanıtı oturumla ilişkilendirir.
DH Başlatma'daki Oturum Anahtarı kullanılmaz.


### Yeni Oturum Yanıt Geçici Anahtarı

Bob'un geçici anahtarı.
Geçici anahtar 32 bayttır, Elligator2 ile kodlanmış, little endian.
Bu anahtar yeniden kullanılmaz; her mesajla birlikte
yeni bir anahtar oluşturulur, yeniden iletimler dahil.


### Yük
Şifreli uzunluk verinin geri kalanıdır.
Çözülmüş uzunluk şifreli uzunluktan 16 bayt daha azdır.
Yük genellikle bir veya daha fazla Sarımsak Çıngırak bloğu içerir.
Biçim ve ek gereksinimler için aşağıda yük bölümüne bakın.


### Yanıt EtiketSeti için KDF

Bir veya daha fazla etiket, KDF'nin aşağıda tanımlandığı gibi
Yeni Oturum mesajındaki zincirAnahtarı kullanılarak başlatılan EtiketSet'ten oluşturulur.

```

// Etiketset oluştur
  etiketsetAnahtarı = HKDF(zincirAnahtarı, ZEROLEN, "SessionReplyTags", 32)
  etiketset_nsr = DH_INITIALIZE(zincirAnahtarı, etiketsetAnahtarı)

```


### Yanıt Anahtar Bölümü Şifreli İçerikleri için KDF

```

// Yeni Oturum mesajından anahtarlar
  // Alice'in X25519 anahtarları
  // apk ve aepk orijinal Yeni Oturum mesajında gönderilir
  // ask = Alice özel statik anahtarı
  // apk = Alice genel statik anahtarı
  // aesk = Alice geçici özel anahtarı
  // aepk = Alice geçici genel anahtarı
  // Bob'un X25519 statik anahtarları
  // bsk = Bob özel statik anahtarı
  // bpk = Bob genel statik anahtarı

  // Etiketi oluştur
  etiketsetGirişi = etiketset_nsr.GET_NEXT_ENTRY()
  etiket = etiketsetGirişi.SESSION_TAG

  // MixHash(etiket)
  h = SHA256(h || etiket)

  Bu "e" mesaj desenidir:

  // Bob'un X25519 geçici anahtarları
  besk = GENERATE_PRIVATE_ELG2()
  bepk = DERIVE_PUBLIC(besk)

  // Bob'un geçici genel anahtarı
  // MixHash(bepk)
  // || aşağıda ekleme anlamına gelir
  h = SHA256(h || bepk);

  // elg2_bepk, Yeni Oturum mesajının
  // başında açık metin olarak gönderilir
  elg2_bepk = ENCODE_ELG2(bepk)
  // Bob tarafından çözüldüğünde
  bepk = DECODE_ELG2(elg2_bepk)

  "e" mesaj deseninin sonu.

  Bu "ee" mesaj desenidir:

  // MixKey(DH())
  //[chainKey, k] = MixKey(paylaşılanGizli)
  // ChaChaPoly parametreleri şifrelemek/çözmek için
  // orijinal Yeni Oturum Yük Bölümünden zincirAnahtarı
  paylaşılanGizli = DH(aesk, bepk) = DH(besk, aepk)
  anahtarverisi = HKDF(zincirAnahtarı, paylaşılanGizli, "", 32)
  zincirAnahtarı = anahtarverisi[0:31]

  "ee" mesaj deseninin sonu.

  Bu "se" mesaj desenidir:

  // MixKey(DH())
  //[chainKey, k] = MixKey(paylaşılanGizli)
  paylaşılanGizli = DH(ask, bepk) = DH(besk, apk)
  anahtarverisi = HKDF(zincirAnahtarı, paylaşılanGizli, "", 64)
  zincirAnahtarı = anahtarverisi[0:31]

  // AEAD parametreleri
  k = anahtarverisi[32:63]
  n = 0
  ad = h
  şifreliMetin = ENCRYPT(k, n, ZEROLEN, ad)

  "se" mesaj deseninin sonu.

  // MixHash(şifreliMetin)
  h = SHA256(h || şifreliMetin)

  zincirAnahtarı, aşağıda ratchet için kullanılır.

```


### Yük Bölümü Şifreli İçerikleri için KDF

Bu, ilk Mevcut Oturum mesajına benzer,
bölünmeden sonra, ancak ayrı bir etiket olmadan. Ayrıca, yükü NSR mesajına bağlamak için
yukarıdaki hash'i kullanıyoruz.


```

// split()
  anahtarverisi = HKDF(zincirAnahtarı, ZEROLEN, "", 64)
  k_ab = anahtarverisi[0:31]
  k_ba = anahtarverisi[32:63]
  etiketset_ab = DH_INITIALIZE(zincirAnahtarı, k_ab)
  etiketset_ba = DH_INITIALIZE(zincirAnahtarı, k_ba)

  // Yeni Oturum Yanıt yükü için AEAD parametreleri
  k = HKDF(k_ba, ZEROLEN, "AttachPayloadKDF", 32)
  n = 0
  ad = h
  şifreliMetin = ENCRYPT(k, n, yük, ad)
```


### Notlar

Yanıtın boyutuna bağlı olarak, her biri benzersiz geçici anahtarlara sahip birden fazla NSR mesajı gönderilebilir.

Alice ve Bob, her NS ve NSR mesajı için yeni geçici anahtarlar kullanmak zorundadır.

Alice, Mevcut Oturum (ES) mesajları göndermeden önce Bob'un NSR mesajlarından birini almalıdır,
ve Bob, ES mesajları göndermeden önce Alice'den bir ES mesajı almalıdır.

Bob'un NSR Yük Bölümünden ``zincirAnahtarı`` ve ``k``,
ilk ES DH Ratcheti için giriş olarak kullanılır (her iki yönde, DH Ratchet KDF'ye bakın).

Bob, Alice'den alınan ES mesajları için Mevcut Oturumları saklamalıdır.
Belirli bir oturum için Alice'in ilk ES mesajını aldıktan sonra,
diğer tüm oluşturulan gelen ve giden oturumlar (birden fazla NSR için) hemen
yok edilmelidir.



### 1h) Mevcut oturum biçimi

Oturum etiketi (8 bayt)
Şifreli veri ve MAC (aşağıdaki bölüm 3'e bakın)


### Biçim
Şifreli:

```

+----+----+----+----+----+----+----+----+
  |       Oturum Etiketi                     |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Yük Bölümü            +
  |       ChaCha20 şifreli veri         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Mesaj Kimlik Doğrulama Kodu |
  +              (MAC)                    +
  |             16 bayt                  |
  +----+----+----+----+----+----+----+----+

  Oturum Etiketi :: 8 bayt, açık metin
