---
title: "Yeni netDB Girişleri"
number: "123"
author: "zzz, str4d, orignal"
created: "2016-01-16"
lastupdated: "2020-07-18"
status: "Aç"
thread: "http://zzz.i2p/topics/2051"
supercedes: "110, 120, 121, 122"
toc: true
---
## Durum

Bu teklifin bazı bölümleri tamamlanmış olup 0.9.38 ve 0.9.39 sürümlerinde uygulanmıştır.  
Ortak Yapılar, I2CP, I2NP ve diğer spesifikasyonlar  
şimdi desteklenen değişiklikleri yansıtacak şekilde güncellenmiştir.

Tamamlanan bölümler hâlâ küçük revizyonlara tabidir.  
Bu teklifin diğer bölümleri hâlâ geliştirme aşamasındadır  
ve önemli revizyonlara tabidir.

Hizmet Arama (tür 9 ve 11) düşük önceliklidir ve  
planlanmamıştır, ayrıca ayrı bir teklife ayrılabilir.


## Genel Bakış

Bu, aşağıdaki 4 teklifin bir güncellenmesi ve birleştirilmesidir:

- 110 LS2
- 120 Meta LS2 for massive multihoming
- 121 Encrypted LS2
- 122 Unauthenticated service lookup (anycasting)

Bu teklifler çoğunlukla bağımsızdır, ancak sağduyu açısından birkaç tanesi için  
ortak bir biçim tanımlıyoruz ve kullanıyoruz.

Aşağıdaki teklifler kısmen ilişkilidir:

- 140 Invisible Multihoming (bu teklifle uyumsuz)
- 142 New Crypto Template (yeni simetrik şifreleme için)
- 144 ECIES-X25519-AEAD-Ratchet
- 145 ECIES-P256
- 146 Red25519
- 148 EdDSA-BLAKE2b-Ed25519
- 149 B32 for Encrypted LS2
- 150 Garlic Farm Protocol
- 151 ECDSA Blinding


## Teklif

Bu teklif 5 yeni DatabaseEntry türü ve bunların  
ağ veritabanına nasıl kaydedileceğini ve oradan nasıl alınacağını tanımlar,  
ayrıca nasıl imzalanacaklarını ve bu imzaların nasıl doğrulanacağını da belirtir.

### Amaçlar

- Geriye dönük uyumlu
- LS2 eski tarz çoklu barındırmayla (multihoming) kullanılabilir
- Desteğin sağlanması için yeni şifreleme veya temel işlemler gerekmez
- Şifreleme ve imzalama arasındaki ayrımı koru; tüm mevcut ve gelecekteki sürümleri destekle
- İsteğe bağlı çevrimdışı imza anahtarlarını etkinleştir
- Parmak izini azaltmak için zaman damgalarının doğruluğunu azalt
- Hedefler için yeni şifreleme türlerini etkinleştir
- Büyük ölçekli çoklu barındırmayı (massive multihoming) etkinleştir
- Mevcut şifreli LS ile ilgili birçok sorunu düzelt
- Floodfill'ler tarafından görünürlüğü azaltmak için isteğe bağlı gizleme (blinding)
- Şifreleme, tek anahtarlı ve birden fazla iptal edilebilir anahtarlı modelleri destekler
- Çıkış vekilleri (outproxies), uygulama DHT önyüklemesi ve diğer kullanım alanları için hizmet arama
- 32 baytlık ikili hedef karmalarına (hash) dayanan hiçbir şeyi bozma, örneğin bittorrent
- Routerinfo'larda olduğu gibi, lease set'lere esneklik sağlamak için özellikler (properties) ekle
- Yayınlanan zaman damgasını ve değişken sona ermeyi başlığa koy, böylece içerik şifrelenmiş olsa bile çalışır (en erken lease'ten zaman damgası türetilmez)
- Tüm yeni türler mevcut lease set'lerle aynı DHT alanında ve aynı konumlarda yer alır, böylece kullanıcılar eski LS'den LS2'ye geçiş yapabilir veya LS2, Meta ve Şifreli arasında değişiklik yapabilir, hedefi veya karmayı değiştirmeden.
- Mevcut bir Hedef, hedefi veya karmayı değiştirmeden çevrimdışı anahtarlarla kullanılacak şekilde dönüştürülebilir veya çevrimiçi anahtarlara geri dönebilir.


### Amaçlar Dışı / Kapsam Dışı

- Yeni DHT döndürme algoritması veya paylaşılan rastgele sayı üretimi
- Yeni şifreleme türü ve bu yeni türü kullanan uçtan uca şifreleme şeması ayrı bir teklifte olur. Burada yeni bir şifreleme türü belirtilmez veya tartışmaz.
- Rİ'ler veya tünel oluşturma için yeni şifreleme. Bu ayrı bir teklifte olur.
- I2NP DLM / DSM / DSRM mesajlarının şifrelenmesi, iletilmesi ve alınması yöntemleri. Değişmiyor.
- Meta'nın nasıl üretileceği ve destekleneceği, dahil olmak üzere arka uç iç-router iletişimi, yönetimi, devreye alma ve koordinasyonu. Desteği I2CP'ye, i2pcontrol'e veya yeni bir protokole eklenebilir. Bu standartlaştırılmış olabilir veya olmayabilir.
- Daha uzun süreli tünellerin nasıl uygulanacağı ve yönetileceği veya mevcut tünellerin nasıl iptal edileceği. Bu son derece zordur ve bunu yapmadan makul bir şekilde kapatma mümkün değildir.
- Tehdit modeli değişiklikleri
- Çevrimdışı depolama biçimi veya verinin depolanması/alınması/paylaşılması yöntemleri.
- Uygulama ayrıntıları burada tartışılmaz ve her projeye bırakılır.



### Gerekçe

LS2, şifreleme türünü değiştirme ve gelecekteki protokol değişiklikleri için alanlar ekler.

Şifreli LS2, tüm lease'lerin asimetrik şifrelenmesini kullanarak mevcut şifreli LS ile ilgili birkaç güvenlik sorununu düzeltir.

Meta LS2, esnek, verimli, etkili ve büyük ölçekli çoklu barındırma sağlar.

Hizmet Kaydı ve Hizmet Listesi, ad arama ve DHT önyüklemesi gibi herhangi bir yere yayın (anycast) hizmetleri sağlar.


### NetDB Veri Türleri

Tür numaraları I2NP Veritabanı Arama/Depolama Mesajlarında kullanılır.

Uçtan uca sütunu, sorguların/yanıtların bir Hedefe Sarımsak Mesajında gönderilip gönderilmeyeceğini belirtir.


Mevcut türler:

| NetDB Veri | Arama Türü | Depolama Türü |
|------------|-------------|------------|
| herhangi | 0           | herhangi        |
| LS         | 1           | 1          |
| RI         | 2           | 0          |
| keşif | 3           | DSRM       |

Yeni türler:

| NetDB Veri     | Arama Türü | Depolama Türü | Standart LS2 Başlığı? | Uçtan uca gönderildi mi? |
|----------------|-------------|------------|------------------|------------------|
| LS2            | 1           | 3          | evet              | evet              |
| Şifreli LS2  | 1           | 5          | hayır               | hayır               |
| Meta LS2       | 1           | 7          | evet              | hayır               |
| Hizmet Kaydı | yok         | 9          | evet              | hayır               |
| Hizmet Listesi   | 4           | 11         | hayır               | hayır               |



### Notlar

- Arama türleri şu anda Veritabanı Arama Mesajında 3-2 bitleridir.  
  Ek türler 4. bitin kullanımını gerektirir.

- Eski yönlendiriciler tarafından Veritabanı Depolama Mesajı tür alanındaki üst bitlerin  
  dikkate alınmadığından, tüm depolama türleri tektir.  
  Bunu bir sıkıştırılmış RI yerine LS olarak ayrıştırılması başarısız olmasından ziyade LS olarak ayrıştırılmasını tercih ederiz.

- Tür, imza altındaki veride açık mı, örtük mü yoksa ikisi de değil mi olmalıdır?



### Arama/Depolama işlemi

Tür 3, 5 ve 7, standart lease set aramasına (tür 1) yanıt olarak döndürülebilir.  
Tür 9, bir arama sonucunda asla döndürülmez.  
Tür 11, yeni bir hizmet arama türüne (tür 11) yanıt olarak döndürülür.

Yalnızca tür 3, istemci-istemci Sarımsak mesajında gönderilebilir.



### Biçim

Tür 3, 7 ve 9 ortak bir biçime sahiptir::

  Standart LS2 Başlığı
  - aşağıda tanımlandığı gibi

  Tür Özel Bölüm
  - aşağıda her bölümde tanımlandığı gibi

  Standart LS2 İmzası:
  - İmza türüne göre dolaylı olarak belirlenen uzunlukta

Tür 5 (Şifreli), bir Hedefle başlamaz ve farklı bir biçimdedir. Aşağıya bakın.

Tür 11 (Hizmet Listesi), birkaç Hizmet Kaydının bir araya getirilmesidir ve farklı bir biçimdedir. Aşağıya bakın.


### Gizlilik/Güvenlik Hususları

TBD



## Standart LS2 Başlığı

Tür 3, 7 ve 9 standart LS2 başlığını kullanır, aşağıda belirtilmiştir:


### Biçim

```
Standart LS2 Başlığı:
  - Tür (1 bayt)
    Başlığın kendisinde değil, ancak imza altındaki verinin bir parçası. 
    Veritabanı Depolama Mesajındaki alandan alınır.
  - Hedef (387+ bayt)
  - Yayınlanan zaman damgası (4 bayt, büyük endian, epoch'tan bu yana saniye cinsinden, 2106'da döner)
  - Sona erer (2 bayt, büyük endian) (yayınlanan zaman damgasından saniye cinsinden ofset, maksimum 18.2 saat)
  - Bayraklar (2 bayt)
    Bit sırası: 15 14 ... 3 2 1 0
    Bit 0: 0 ise, çevrimdışı anahtar yok; 1 ise, çevrimdışı anahtar var
    Bit 1: 0 ise, standart yayınlanan lease set.
           1 ise, yayınlanmamış lease set. Başka yerlere gönderilmemeli, yayınlanmamalı veya
           bir sorguya yanıt olarak gönderilmemelidir. Bu lease set süresi dolarsa, netdb'de yeni bir tane için sorgu yapılmamalıdır,
           bit 2 ayarlanmamışsa.
    Bit 2: 0 ise, standart yayınlanan lease set.
           1 ise, bu şifrelenmemiş lease set yayınlandığında gizlenir ve şifrelenir.
           Bu lease set süresi dolarsa, netdb'de gizlenmiş konumda yeni bir tane için sorgu yapılır.
           Bu bit 1 olarak ayarlanırsa, bit 1 de 1 olarak ayarlanmalıdır.
           0.9.42 sürümünden itibaren.
    Bit 3-15: gelecekteki kullanımlarla uyumlu olması için 0 olarak ayarlanır
  - Bayrak çevrimdışı anahtarları gösteriyorsa, çevrimdışı imza bölümü:
    Sona erme zaman damgası (4 bayt, büyük endian, epoch'tan bu yana saniye cinsinden, 2106'da döner)
    Geçici imza türü (2 bayt, büyük endian)
    Geçici imza ortak anahtarı (imza türüne göre dolaylı uzunlukta)
    Sona erme zaman damgası, geçici imza türü ve ortak anahtarın,
    hedef ortak anahtarıyla imzalanması,
    hedef ortak anahtar imza türüne göre dolaylı uzunlukta.
    Bu bölüm çevrimdışı oluşturulabilir ve oluşturulmalıdır.
```

### Gerekçe

- Yayınlanmamış/yayınlanmış: Veritabanı deposunu uçtan uca gönderirken,
  gönderen yönlendirici bu lease set'in başkalarına gönderilmemesini isteyebilir. Şu anda bu durumu korumak için sezgisel yöntemler kullanıyoruz.

- Yayınlanmış: Lease set'in 'sürümünü' belirlemek için gereken karmaşık mantığı değiştirir. Şu anda sürüm, en geç süresi dolan lease'in sona erme zamanıdır ve bir yayınlayıcı, yalnızca eski bir lease'i kaldıran bir lease set'i yayınlarken bu sona erme süresini en az 1ms artırması gerekir.

- Sona erer: Bir netdb girdisinin sona erme süresinin, son süresi dolan lease set'inden daha erken olmasını sağlar. LS2 için faydalı olmayabilir, çünkü lease set'lerin 11 dakikalık maksimum sona erme süresiyle kalması beklenir, ancak diğer yeni türler için gereklidir (aşağıdaki Meta LS ve Hizmet Kaydı'na bakın).

- Çevrimdışı anahtarlar, başlangıç/uygulama karmaşıklığını azaltmak için isteğe bağlıdır.


### Sorunlar

- Zaman damgası doğruluğunu daha da azaltabiliriz (10 dakika?) ancak sürüm numarası eklememiz gerekir. Bu çoklu barındırmayı bozabilir, sıra koruyan şifreleme yapmazsak? Muhtemelen zaman damgaları olmadan yapamayız.

- Alternatif: 3 baytlık zaman damgası (epoch / 10 dakika), 1 baytlık sürüm, 2 baytlık sona erme

- Tür veri/imza içinde açık mı yoksa örtük müdür? İmza için "Alan" sabitleri?


### Notlar

- Yönlendiriciler bir LS'yi saniyede birden fazla kez yayınlamamalıdır.  
  Yaparlarsa, daha önce yayınlanan LS'den 1 saniye daha fazla yapay olarak  
  yayınlanan zaman damgasını artırmalıdırlar.

- Yönlendirici uygulamaları, her seferinde doğrulamayı önlemek için geçici anahtarları ve imzayı önbelleğe alabilir. Özellikle floodfill'ler ve uzun süreli bağlantıların her iki ucundaki yönlendiriciler bundan faydalanabilir.

- Çevrimdışı anahtarlar ve imza yalnızca uzun ömürlü hedefler için uygundur,  
  yani sunucular, istemciler değil.



## Yeni DatabaseEntry türleri


### LeaseSet 2

Mevcut LeaseSet'ten değişiklikler:

- Yayınlanan zaman damgası, sona erme zaman damgası, bayraklar ve özellikler ekle
- Şifreleme türünü ekle
- İptal anahtarını kaldır

Arama ile
    Standart LS bayrağı (1)
Depolama ile
    Standart LS2 türü (3)
Şurada depolama
    Hedefin karması
    Bu karma daha sonra LS1'de olduğu gibi günlük "yönlendirme anahtarı" oluşturmak için kullanılır
Tipik sona erme
    10 dakika, normal bir LS gibi.
Yayınlayan
    Hedef

### Biçim

```
Yukarıda belirtildiği gibi Standart LS2 Başlığı

  Standart LS2 Türüne Özel Bölüm
  - Özellikler (Ortak yapılar spesifikasyonunda belirtildiği gibi Haritalama, yoksa 2 sıfır bayt)
  - Takip edecek anahtar bölümlerinin sayısı (1 bayt, maksimum TBD)
  - Anahtar bölümleri:
    - Şifreleme türü (2 bayt, büyük endian)
    - Şifreleme anahtarı uzunluğu (2 bayt, büyük endian)
      Bu açıkça belirtilmiştir, böylece floodfill'ler bilinmeyen şifreleme türlerine sahip LS2'yi ayrıştırabilir.
    - Şifreleme anahtarı (belirtilen bayt sayısı)
  - lease2'lerin sayısı (1 bayt)
  - Lease2'ler (her biri 40 bayt)
    Bunlar lease'lerdir, ancak 8 baytlık yerine 4 baytlık sona erme,
    epoch'tan bu yana saniye cinsinden (2106'da döner)

  Standart LS2 İmzası:
  - İmza
    Bayrak çevrimdışı anahtarları gösteriyorsa, bu geçici ortak anahtarla imzalanır,
    aksi takdirde hedef ortak anahtarıyla imzalanır
    İmza türüne göre dolaylı uzunlukta
    İmza yukarıdakilerin tamamıdır.
```


### Gerekçe

- Özellikler: Gelecekteki genişleme ve esneklik.  
  Kalan verinin ayrıştırılması için gerekli olabileceği için ilk sırada yer alır.

- Birden fazla şifreleme türü/ortak anahtar çifti  
  yeni şifreleme türlerine geçişi kolaylaştırmak içindir. Diğer yol  
  birden fazla lease set yayınlamaktır, muhtemelen aynı tünelleri kullanarak,  
  şu an DSA ve EdDSA hedefleri için yaptığımız gibi.  
  Bir tüneldeki gelen şifreleme türünün tanımlanması  
  mevcut oturum etiketi mekanizmasıyla yapılabilir,  
  ve/veya her anahtarla deneme şifre çözme. Gelen  
  mesajların uzunluğu da bir ipucu sağlayabilir.

### Tartışma

Bu teklif, uçtan uca şifreleme anahtarı olarak lease set'teki ortak anahtarı kullanmaya devam eder ve  
ortak anahtar alanını hedefte kullanmaz, şu an olduğu gibi. Şifreleme türü  
hedef anahtar sertifikasında belirtilmez, 0 olarak kalır.

Reddedilen alternatif, şifreleme türünü hedef anahtar sertifikasında belirtmektir,  
hedefteki ortak anahtarı kullanmak ve lease set'teki ortak anahtarı  
kullanmamak. Bunu yapmayı planlamıyoruz.

LS2'nin faydaları:

- Gerçek ortak anahtarın konumu değişmez.
- Şifreleme türü veya ortak anahtar, Hedefi değiştirmeden değiştirilebilir.
- Kullanılmayan iptal alanını kaldırır
- Bu teklifteki diğer DatabaseEntry türleriyle temel uyumluluk
- Birden fazla şifreleme türünü destekler

LS2'nin dezavantajları:

- Ortak anahtarın ve şifreleme türünün konumu RouterInfo'dan farklıdır
- Lease set'te kullanılmayan ortak anahtarı korur
- Ağ genelinde uygulama gerektirir; alternatif olarak, deneysel  
  şifreleme türleri kullanılabilir, eğer floodfill'ler izin veriyorsa  
  (ancak deneysel imza türleri için destekle ilgili ilgili tekliflere 136 ve 137 bakın).  
  Alternatif teklif, deneysel şifreleme türleri için uygulamak ve test etmek daha kolay olabilir.


### Yeni Şifreleme Sorunları

Bunun bir kısmı bu teklifin kapsamı dışındadır,  
ancak henüz ayrı bir şifreleme teklifi olmadığından  
şimdilik buraya notlar ekliyoruz.  
Ayrıca ECIES tekliflerine 144 ve 145 bakın.

- Şifreleme türü, eğri, anahtar uzunluğu ve uçtan uca şemayı,  
  varsa KDF ve MAC'ı birlikte temsil eder.

- LS2'nin floodfill tarafından bilinmeyen şifreleme türleri için bile  
  ayrıştırılabilir ve doğrulanabilir olması için bir anahtar uzunluğu alanı ekledik.

- Önerilecek ilk yeni şifreleme türü  
  muhtemelen ECIES/X25519 olacaktır. Nasıl kullanılacağı uçtan uca  
  (ElGamal/AES+SessionTag'ın biraz değiştirilmiş bir versiyonu  
  veya tamamen yeni bir şey, örneğin ChaCha/Poly) bir veya daha fazla ayrı teklifte  
  belirtilecektir.  
  Ayrıca ECIES tekliflerine 144 ve 145 bakın.


### Notlar

- Lease'lerdeki 8 baytlık sona erme 4 bayta değiştirildi.

- Eğer iptal uygulamayı gerçekleştirirsek, bunu sıfır olan bir sona erme alanı veya sıfır lease'lerle yapabiliriz veya ikisiyle. Ayrı bir iptal anahtarı gerekmez.

- Şifreleme anahtarları, sunucunun tercihine göre sıraya dizilir, en çok tercih edilen ilk sırada. Varsayılan istemci davranışı, desteklenen bir şifreleme türüne sahip ilk anahtarı seçmektir. İstemciler şifreleme desteği, göreli performans ve diğer faktörlere dayalı olarak başka seçim algoritmaları kullanabilirler.


### Şifreli LS2

Amaçlar:

- Gizleme ekle
- Birden fazla imza türüne izin ver
- Yeni şifreleme temel işlemlerini gerektirme
- İsteğe bağlı olarak her alıcıya şifrele, iptal edilebilir
- Yalnızca Standart LS2 ve Meta LS2'nin şifrelenmesini destekle

Şifreli LS2, asla uçtan uca sarımsak mesajında gönderilmez.  
Yukarıdaki gibi standart LS2'yi kullanın.


Mevcut şifreli LeaseSet'ten değişiklikler:

- Güvenlik için her şeyi şifrele
- Sadece AES ile değil, güvenli şifrele
- Her alıcıya şifrele

Arama ile
    Standart LS bayrağı (1)
Depolama ile
    Şifreli LS2 türü (5)
Depolama konumu
    Gizlenmiş imza türü ve gizlenmiş ortak anahtarın karması  
    İki baytlık imza türü (büyük endian, örneğin 0x000b) || gizlenmiş ortak anahtar  
    Bu karma daha sonra LS1'de olduğu gibi günlük "yönlendirme anahtarı" oluşturmak için kullanılır
Tipik sona erme
    10 dakika, normal bir LS gibi veya saatlerce, bir meta LS gibi.
Yayınlayan
    Hedef


### Tanımlar

Şifreli LS2 için kullanılan kriptografik yapı taşlarına karşılık gelen aşağıdaki fonksiyonları tanımlıyoruz:

CSRNG(n)
    Kriptografik olarak güvenli rastgele sayı üretecinin n baytlık çıktısı.

    CSRNG'nin kriptografik olarak güvenli olması (ve bu nedenle anahtar malzemesi üretmek için uygun olması) gerekliliğine ek olarak, bazı n baytlık çıktının ağda (bir tuzda veya şifrelenmiş dolguda) açığa çıkan bayt dizileriyle birlikte anahtar malzemesi olarak kullanılmasının güvenli olması GEREKİR. Ağda açılacak herhangi bir çıktıyı hashlemelidir. [PRNG referansları](http://projectbullrun.org/dual-ec/ext-rand.html) ve [Tor geliştirici tartışması](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html) bölümüne bakın.

H(p, d)
    Kişiselleştirilmiş bir dize p ve veri d alan ve 32 baytlık bir çıktı üreten SHA-256 hash fonksiyonu.

    SHA-256'yı şu şekilde kullanın::

        H(p, d) := SHA-256(p || d)

STREAM
    [RFC 7539 Section 2.4](https://tools.ietf.org/html/rfc7539#section-2.4) bölümünde belirtildiği gibi ChaCha20 akış şifreleme, ilk sayaç 1 olarak ayarlanır. S_KEY_LEN = 32 ve S_IV_LEN = 12.

    ENCRYPT(k, iv, plaintext)
        Şifreleme anahtarı k ve benzersiz olmak zorunda olan nonce iv kullanarak plaintext'i şifreler. Plaintext ile aynı boyutta bir şifreli metin döndürür.

        Anahtar gizliyse, tüm şifreli metin rastgele olmaktan ayırt edilemez olmalıdır.

    DECRYPT(k, iv, ciphertext)
        Şifreleme anahtarı k ve nonce iv kullanarak ciphertext'i şifresini çözer. Plaintext'i döndürür.


SIG
    Anahtar gizleme (key blinding) ile RedDSA imza şeması (SigType 11'e karşılık gelir). Aşağıdaki fonksiyonlara sahiptir:

    DERIVE_PUBLIC(privkey)
        Verilen özel anahtara karşılık gelen ortak anahtarı döndürür.

    SIGN(privkey, m)
        Verilen mesaj m üzerinde özel anahtar privkey tarafından bir imza döndürür.

    VERIFY(pubkey, m, sig)
        İmza sig'ı ortak anahtar pubkey ve mesaj m ile doğrular. İmza geçerliyse true, aksi takdirde false döndürür.

    Ayrıca aşağıdaki anahtar gizleme işlemlerini desteklemelidir:

    GENERATE_ALPHA(data, secret)
        Veriyi ve isteğe bağlı bir sırrı bilenler için alpha üretir. Sonuç, özel anahtarlarla aynı şekilde dağıtılmış olmalıdır.

    BLIND_PRIVKEY(privkey, alpha)
        Gizli bir alpha kullanarak özel anahtarı gizler.

    BLIND_PUBKEY(pubkey, alpha)
        Gizli bir alpha kullanarak ortak anahtarı gizler.
        Verilen anahtar çifti (privkey, pubkey) için aşağıdaki ilişki geçerlidir::

            BLIND_PUBKEY(pubkey, alpha) ==
            DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))

DH
    X25519 ortak anahtar anlaşma sistemi. 32 baytlık özel anahtarlar, 32 baytlık ortak anahtarlar, 32 baytlık çıktılar üretir. Aşağıdaki fonksiyonlara sahiptir:

    GENERATE_PRIVATE()
        Yeni bir özel anahtar üretir.

    DERIVE_PUBLIC(privkey)
        Verilen özel anahtara karşılık gelen ortak anahtarı döndürür.

    DH(privkey, pubkey)
        Verilen özel ve ortak anahtarlardan paylaşılan bir gizli anahtar üretir.

HKDF(salt, ikm, info, n)
    Giriş anahtar malzemesi ikm'yi (iyi entropiye sahip olmalıdır ancak düzgün rastgele bir dize olmak zorunda değildir), 32 bayt uzunluğunda bir tuzu ve bağlama özgü bir 'info' değerini alan ve anahtar malzemesi olarak kullanılması için n baytlık bir çıktı üreten kriptografik bir anahtar türetme fonksiyonudur.

    [RFC 5869](https://tools.ietf.org/html/rfc5869) bölümünde belirtildiği gibi HKDF'yi kullanın, [RFC 2104](https://tools.ietf.org/html/rfc2104) bölümünde belirtildiği gibi HMAC hash fonksiyonu SHA-256'yı kullanarak. Bu, SALT_LEN'in maksimum 32 bayt olduğu anlamına gelir.


### Biçim

Şifreli LS2 biçimi üç iç içe katmandan oluşur:

- Depolama ve alım için gerekli düz metin bilgilerini içeren dış katman.
- İstemci kimlik doğrulamasını işleyen orta katman.
- Gerçek LS2 verisini içeren iç katman.

Genel biçim şöyle görünür::

    Katman 0 verisi + Enc(katman 1 verisi + Enc(katman 2 verisi)) + İmza

Şifreli LS2'nin gizlendiğini unutmayın. Hedef başlıkta değildir. DHT depolama konumu SHA-256(imza türü || gizlenmiş ortak anahtar)'dır ve günlük olarak döner.

Yukarıda belirtilen standart LS2 başlığını KULLANMAZ.

#### Katman 0 (dış)
Tür
    1 bayt

    Başlığın kendisinde değil, ancak imza altındaki verinin bir parçası.  
    Veritabanı Depolama Mesajındaki alandan alınır.

Gizlenmiş Ortak Anahtar İmza Türü
    2 bayt, büyük endian
    Bu her zaman tür 11 olacak, gizlenmiş bir Red25519 anahtarını tanımlar.

Gizlenmiş Ortak Anahtar
    İmza türüne göre dolaylı uzunlukta

Yayınlanan zaman damgası
    4 bayt, büyük endian

    Epoch'tan bu yana saniye cinsinden, 2106'da döner

Sona erer
    2 bayt, büyük endian

    Yayınlanan zaman damgasından saniye cinsinden ofset, maksimum 18.2 saat

Bayraklar
    2 bayt

    Bit sırası: 15 14 ... 3 2 1 0

    Bit 0: 0 ise, çevrimdışı anahtar yok; 1 ise, çevrimdışı anahtar var

    Diğer bitler: gelecekteki kullanımlarla uyumlu olması için 0 olarak ayarlanır

Geçici anahtar verisi
    Bayrak çevrimdışı anahtarları gösteriyorsa mevcuttur

    Sona erme zaman damgası
        4 bayt, büyük endian

        Epoch'tan bu yana saniye cinsinden, 2106'da döner

    Geçici imza türü
        2 bayt, büyük endian

    Geçici imza ortak anahtarı
        İmza türüne göre dolaylı uzunlukta

    İmza
        Gizlenmiş ortak anahtar imza türüne göre dolaylı uzunlukta

        Sona erme zaman damgası, geçici imza türü ve geçici ortak anahtar üzerinde.
        Gizlenmiş ortak anahtarla doğrulanır.

lenOuterCiphertext
    2 bayt, büyük endian

outerCiphertext
    lenOuterCiphertext bayt

    Şifreli katman 1 verisi. Anahtar türetme ve şifreleme algoritmaları için aşağıya bakın.

İmza
    Kullanılan imza anahtarının imza türüne göre dolaylı uzunlukta

    Yukarıdakilerin tamamının imzasıdır.

    Bayrak çevrimdışı anahtarları gösteriyorsa, imza geçici ortak anahtarla doğrulanır. Aksi takdirde, imza gizlenmiş ortak anahtarla doğrulanır.


#### Katman 1 (orta)
Bayraklar
    1 bayt
    
    Bit sırası: 76543210

    Bit 0: 0 herkes için, 1 istemci bazında, takip eden yetkilendirme bölümü

    Bit 3-1: Kimlik doğrulama şeması, bit 0 istemci bazında 1 olarak ayarlanırsa, aksi takdirde 000
              000: DH istemci kimlik doğrulaması (veya istemci bazında kimlik doğrulaması yok)
              001: PSK istemci kimlik doğrulaması

    Bit 7-4: Kullanılmıyor, gelecekteki uyumluluk için 0 olarak ayarlanır

DH istemci kimlik doğrulama verisi
    Bayrak biti 0 1 olarak ayarlanmışsa ve bayrak bitleri 3-1 000 olarak ayarlanmışsa mevcuttur.

    ephemeralPublicKey
        32 bayt

    clients
        2 bayt, büyük endian

        Takip edecek authClient girişlerinin sayısı, her biri 40 bayt

    authClient
        Tek bir istemci için yetkilendirme verisi.
        İstemci bazında yetkilendirme algoritması için aşağıya bakın.

        clientID_i
            8 bayt

        clientCookie_i
            32 bayt

PSK istemci kimlik doğrulama verisi
    Bayrak biti 0 1 olarak ayarlanmışsa ve bayrak bitleri 3-1 001 olarak ayarlanmışsa mevcuttur.

    authSalt
        32 bayt

    clients
        2 bayt, büyük endian

        Takip edecek authClient girişlerinin sayısı, her biri 40 bayt

    authClient
        Tek bir istemci için yetkilendirme verisi.
        İstemci bazında yetkilendirme algoritması için aşağıya bakın.

        clientID_i
            8 bayt

        clientCookie_i
            32 bayt


innerCiphertext
    lenOuterCiphertext'e göre dolaylı uzunlukta (kalan veri ne kadar ise)

    Şifreli katman 2 verisi. Anahtar türetme ve şifreleme algoritmaları için aşağıya bakın.


#### Katman 2 (iç)
Tür
    1 bayt

    3 (LS2) veya 7 (Meta LS2) olabilir

Veri
    Verilen tür için LeaseSet2 verisi.

    Başlığı ve imzasını içerir.


### Anahtar Gizleme Türetimi

Aşağıdaki şemayı anahtar gizleme için kullanıyoruz,  
Ed25519 ve [ZCash RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)'ya dayanır.  
Re25519 imzaları Ed25519 eğrisi üzerinde, hash için SHA-512 kullanılarak yapılır.

Benzer tasarım hedeflerine sahip olsa da [Tor'un rend-spec-v3.txt ek A.2](https://spec.torproject.org/rend-spec-v3)'sini kullanmıyoruz, çünkü gizlenmiş ortak anahtarları asal-sıra alt grubunun dışında olabilir ve güvenlik etkileri bilinmiyor.


#### Amaçlar

- Gizlenmemiş hedefteki imza ortak anahtarı  
  Ed25519 (imza türü 7) veya Red25519 (imza türü 11) olmalıdır;  
  başka imza türleri desteklenmez
- İmza ortak anahtarı çevrimdışıysa, geçici imza ortak anahtarı da Ed25519 olmalıdır
- Gizleme hesapsal olarak basit olmalıdır
- Mevcut kriptografik temel işlemleri kullan
- Gizlenmiş ortak anahtarlar geri gizlenemez olmalıdır
- Gizlenmiş ortak anahtarlar Ed25519 eğrisi üzerinde ve asal-sıra alt grubunda olmalıdır
- Gizlenmiş ortak anahtarı türetmek için hedefin imza ortak anahtarını bilmek gerekir  
  (tam hedef gerekli değildir)
- İsteğe bağlı olarak gizlenmiş ortak anahtarı türetmek için ek bir gizli anahtar sağla


#### Güvenlik

Bir gizleme şemasının güvenliği, alpha'nın dağılımının gizlenmemiş özel anahtarlarla aynı olması gerektiğini gerektirir. Ancak, bir Ed25519 özel anahtarını (imza türü 7) bir Red25519 özel anahtarına (imza türü 11) gizlerken dağılım farklıdır. [zcash bölüm 4.1.6.1](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) gereksinimlerini karşılamak için, "yeniden rastgeleleştirilmiş bir ortak anahtar ve bu anahtar altındaki imza(lar)ın, yeniden rastgeleleştirildiği anahtarı ortaya çıkarmaması" için Red25519 (imza türü 11) gizlenmemiş anahtarlar için de kullanılmalıdır. Mevcut hedefler için tür 7'yi kabul ediyoruz, ancak yeni şifrelenecek hedefler için tür 11 öneriyoruz.



#### Tanımlar

B
    Ed25519 taban noktası (üreteç) 2^255 - 19 [Ed25519](http://cr.yp.to/papers.html#ed25519) gibi

L
    Ed25519 sırası 2^252 + 27742317777372353535851937790883648493  
    [Ed25519](http://cr.yp.to/papers.html#ed25519) gibi

DERIVE_PUBLIC(a)
    Ed25519'daki gibi özel anahtarı ortak anahtara dönüştür (G ile çarp)

alpha
    Hedefi bilenlerin bildiği 32 baytlık rastgele sayı.

GENERATE_ALPHA(destination, date, secret)
    Hedefi ve sırrı bilenler için geçerli tarih için alpha üretir.  
    Sonuç Ed25519 özel anahtarları ile aynı şekilde dağıtılmış olmalıdır.

a
    Hedefi imzalamak için kullanılan gizlenmemiş 32 baytlık EdDSA veya RedDSA imza özel anahtarı

A
    Hedefteki gizlenmemiş 32 baytlık EdDSA veya RedDSA imza ortak anahtarı,  
    = DERIVE_PUBLIC(a), Ed25519'daki gibi

a'
    Şifreli lease set'i imzalamak için kullanılan gizlenmiş 32 baytlık EdDSA imza özel anahtarı  
    Bu, geçerli bir EdDSA özel anahtarıdır.

A'
    Hedefteki gizlenmiş 32 baytlık EdDSA imza ortak anahtarı,  
    DERIVE_PUBLIC(a') ile veya A ve alpha'dan üretilebilir.  
    Bu, eğri üzerinde ve asal-sıra alt grubunda geçerli bir EdDSA ortak anahtarıdır.

LEOS2IP(x)
    Giriş baytlarının sırasını little-endian yap

H*(x)
    32 bayt = (LEOS2IP(SHA512(x))) mod B, Ed25519 hash-and-reduce gibi aynı


#### Gizleme Hesaplamaları

Her gün (UTC) yeni bir gizli alpha ve gizlenmiş anahtarlar oluşturulmalıdır.  
Gizli alpha ve gizlenmiş anahtarlar aşağıdaki gibi hesaplanır.

GENERATE_ALPHA(destination, date, secret), tüm taraflar için:

```text
// GENERATE_ALPHA(destination, date, secret)

  // gizli isteğe bağlıdır, aksi takdirde sıfır uzunluklu
  A = hedefin imza ortak anahtarı
  stA = A'nın imza türü, 2 bayt büyük endian (0x0007 veya 0x000b)
  stA' = gizlenmiş ortak anahtar A'nın imza türü, 2 bayt büyük endian (0x000b)
  keydata = A || stA || stA'
  datestring = 8 bayt ASCII YYYYMMDD geçerli tarih UTC'den
  secret = UTF-8 kodlu dize
  seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || secret, "i2pblinding1", 64)
  // seed'i 64 baytlık little-endian değer olarak kabul et
  alpha = seed mod L
```

BLIND_PRIVKEY(), lease set'i yayınlayan sahip için:

```text
// BLIND_PRIVKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  // Eğer Ed25519 özel anahtarı (tür 7) için ise
  seed = hedefin imza özel anahtarı
  a = seed'in SHA512'inin sol yarısı ve Ed25519 için normal şekilde kısılır
  // aksi takdirde, Red25519 özel anahtarı (tür 11) için
  a = hedefin imza özel anahtarı
  // Skaler aritmetik kullanarak toplama
  gizlenmiş imza özel anahtarı = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
  gizlenmiş imza ortak anahtarı = A' = DERIVE_PUBLIC(a')
```

BLIND_PUBKEY(), lease set'i alan istemciler için:

```text
// BLIND_PUBKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  A = hedefin imza ortak anahtarı
  // Grup elemanlarını kullanarak toplama (eğri üzerindeki noktalar)
  gizlenmiş ortak anahtar = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```

A' hesaplamasının her iki yöntemi de aynı sonucu verir, gerektiği gibi.



#### İmzalama

Gizlenmemiş lease set, gizlenmemiş Ed25519 veya Red25519 imza özel anahtarıyla imzalanır ve gizlenmemiş Ed25519 veya Red25519 imza ortak anahtarıyla (imza türleri 7 veya 11) normal şekilde doğrulanır.

İmza ortak anahtarı çevrimdışıysa, gizlenmemiş lease set, gizlenmemiş geçici Ed25519 veya Red25519 imza özel anahtarıyla imzalanır ve gizlenmemiş Ed25519 veya Red25519 geçici imza ortak anahtarıyla (imza türleri 7 veya 11) normal şekilde doğrulanır. Şifreli lease set'ler için çevrimdışı anahtarlar hakkında ek notlar için aşağıya bakın.

Şifreli lease set'in imzalanması için, gizlenmiş anahtarlarla imzalama ve doğrulama yapmak üzere [RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)'ya dayanan Red25519 kullanıyoruz. Red25519 imzaları Ed25519 eğrisi üzerinde, hash için SHA-512 kullanılarak yapılır.

Red25519, aşağıda belirtilenler dışında standart Ed25519 ile aynıdır.


#### İmzalama/Doğrulama Hesaplamaları

Şifreli lease set'in dış kısmı Red25519 anahtarlarını ve imzalarını kullanır.

Red25519, neredeyse Ed25519 ile aynıdır. İki fark vardır:

Red25519 özel anahtarları rastgele sayıdan üretilir ve ardından yukarıda tanımlandığı gibi L modunda azaltılmalıdır. Ed25519 özel anahtarları rastgele sayıdan üretilir ve ardından bayt 0 ve 31 için bit maskesi kullanılarak "kısaltılır". Bu, Red25519 için yapılmaz. Yukarıda tanımlanan GENERATE_ALPHA() ve BLIND_PRIVKEY() fonksiyonları mod L kullanarak uygun Red25519 özel anahtarlarını üretir.

Red25519'de, imzalama için r'nin hesaplanması ek rastgele veri kullanır ve özel anahtarın hash'i yerine ortak anahtar değerini kullanır. Rastgele veri nedeniyle, her Red25519 imzası farklıdır, aynı veriyle aynı anahtarla imzalansa bile.

İmzalama:

```text
T = 80 rastgele bayt
  r = H*(T || publickey || message)
  // geri kalanı Ed25519'deki gibi
```

Doğrulama:

```text
// Ed25519'deki gibi aynı
```



### Şifreleme ve İşleme

#### Alt kimlik bilgilerinin türetilmesi
Gizleme sürecinin bir parçası olarak, şifreli bir LS2'nin yalnızca karşılık gelen Hedefin imza ortak anahtarını bilen biri tarafından şifresinin çözülebileceğinden emin olmamız gerekir. Tam Hedef gerekli değildir. Bunu başarmak için, imza ortak anahtarından bir kimlik bilgisi türetiriz:

```text
A = hedefin imza ortak anahtarı
  stA = A'nın imza türü, 2 bayt büyük endian (0x0007 veya 0x000b)
  stA' = A'nın imza türü, 2 bayt büyük endian (0x000b)
  keydata = A || stA || stA'
  credential = H("credential", keydata)
```

Kişiselleştirme dizesi, kimlik bilgisinin düz Hedef karması gibi bir DHT arama anahtarı olarak kullanılan herhangi bir hash ile çakışmadığından emin olur.

Verilen gizlenmiş anahtar için, ardından bir alt kimlik bilgisi türetebiliriz:

```text
subcredential = H("subcredential", credential || blindedPublicKey)
```

Alt kimlik bilgisi, aşağıdaki anahtar türetme süreçlerine dahil edilir, bu da bu anahtarları Hedefin imza ortak anahtarının bilinmesine bağlar.

#### Katman 1 şifreleme
İlk olarak, anahtar türetme sürecine girdi hazırlanır:

```text
outerInput = subcredential || publishedTimestamp
```

Ardından, rastgele bir tuz oluşturulur:

```text
outerSalt = CSRNG(32)
```

Ardından, katman 1'i şifrelemek için kullanılan anahtar türetilir:

```text
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
  outerKey = keys[0:31]
  outerIV = keys[32:43]
```

Son olarak, katman 1 düz metni şifrelenir ve serileştirilir:

```text
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```

#### Katman 1 şifre çözme
Tuz, katman 1 şifreli metninden ayrıştırılır:

```text
outerSalt = outerCiphertext[0:31]
```

Ardından, katman 1'i şifrelemek için kullanılan anahtar türetilir:

```text
outerInput = subcredential || publishedTimestamp
  keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
  outerKey = keys[0:31]
  outerIV = keys[32:43]
```

Son olarak, katman 1 şifreli metni şifresi çözülür:

```text
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```

#### Katman 2 şifreleme
İstemci yetkilendirmesi etkinleştirildiğinde, ``authCookie`` aşağıda açıklandığı gibi hesaplanır. İstemci yetkilendirmesi devre dışı bırakıldığında, ``authCookie`` sıfır uzunluklu bayt dizisidir.

Şifreleme, katman 1'e benzer şekilde devam eder:

```text
innerInput = authCookie || subcredential || publishedTimestamp
  innerSalt = CSRNG(32)
  keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
  innerKey = keys[0:31]
  innerIV = keys[32:43]
  innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```

#### Katman 2 şifre çözme
İstemci yetkilendirmesi etkinleştirildiğinde, ``authCookie`` aşağıda açıklandığı gibi hesaplanır. İstemci yetkilendirmesi devre dışı bırakıldığında, ``authCookie`` sıfır uzunluklu bayt dizisidir.

Şifre çözme, katman 1'e benzer şekilde devam eder:

```text
innerInput = authCookie || subcredential || publishedTimestamp
  innerSalt = innerCiphertext[0:31]
  keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
  innerKey = keys[0:31]
  innerIV = keys[32:43]
  innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```


### İstemci bazında yetkilendirme

Bir Hedef için istemci yetkilendirmesi etkinleştirildiğinde, sunucu şifreli LS2 verisinin şifresini çözmek için yetkilendirdiği istemcilerin bir listesini tutar. İstemci başına depolanan veri, yetkilendirme mekanizmasına bağlıdır ve her istemcinin güvenli bir dış bant mekanizmasıyla sunucuya gönderdiği bazı anahtar malzemesi biçimini içerir.

İstemci bazında yetkilendirme için iki alternatif vardır:

#### DH istemci yetkilendirmesi
Her istemci bir DH anahtar çifti ``[csk_i, cpk_i]`` üretir ve ortak anahtar ``cpk_i``'yi sunucuya gönderir.

Sunucu işleme
^^^^^^^^^^^^^^^^^
Sunucu yeni bir ``authCookie`` ve geçici bir DH anahtar çifti üretir:

```text
authCookie = CSRNG(32)
  esk = GENERATE_PRIVATE()
  epk = DERIVE_PUBLIC(esk)
```

Ardından her yetkili istemci için, sunucu ``authCookie``'yi ortak anahtarına şifreler:

```text
sharedSecret = DH(esk, cpk_i)
  authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
  okm = HKDF(epk, authInput, "ELS2_XCA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
  clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```

Sunucu her ``[clientID_i, clientCookie_i]`` ikilisini katman 1'e yerleştirir, ``epk`` ile birlikte.

İstemci işleme
^^^^^^^^^^^^^^^^^
İstemci özel anahtarını kullanarak beklenen istemci tanımlayıcısı ``clientID_i``, şifreleme anahtarı ``clientKey_i`` ve şifreleme IV'si ``clientIV_i``'yi türetir:

```text
sharedSecret = DH(csk_i, epk)
  authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
  okm = HKDF(epk, authInput, "ELS2_XCA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
```

Ardından istemci, ``clientID_i`` içeren bir giriş aramak için katman 1 yetkilendirme verisini tarar. Eşleşen bir giriş varsa, istemci şifresini çözerek ``authCookie``'yi elde eder:

```text
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```

#### Paylaşılan gizli anahtar istemci yetkilendirmesi
Her istemci 32 baytlık gizli bir anahtar ``psk_i`` üretir ve sunucuya gönderir. Alternatif olarak, sunucu gizli anahtarı üretebilir ve bir veya daha fazla istemciye gönderebilir.


Sunucu işleme
^^^^^^^^^^^^^^^^^
Sunucu yeni bir ``authCookie`` ve tuz üretir:

```text
authCookie = CSRNG(32)
  authSalt = CSRNG(32)
```

Ardından her yetkili istemci için, sunucu ``authCookie``'yi paylaşılan gizli anahtarına şifreler:

```text
authInput = psk_i || subcredential || publishedTimestamp
  okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
  clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```

Sunucu her ``[clientID_i, clientCookie_i]`` ikilisini katman 1'e yerleştirir, ``authSalt`` ile birlikte.

İstemci işleme
^^^^^^^^^^^^^^^^^
İstemci paylaşılan gizli anahtarını kullanarak beklenen istemci tanımlayıcısı ``clientID_i``, şifreleme anahtarı ``clientKey_i`` ve şifreleme IV'si ``clientIV_i``'yi türetir:

```text
authInput = psk_i || subcredential || publishedTimestamp
  okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
```

Ardından istemci, ``clientID_i`` içeren bir giriş aramak için katman 1 yetkilendirme verisini tarar. Eşleşen bir giriş varsa, istemci şifresini çözerek ``authCookie``'yi elde eder:

```text
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```

#### Güvenlik hususları
Yukarıdaki istemci yetkilendirme mekanizmalarının her ikisi de istemci üyeliği için gizlilik sağlar. Yalnızca Hedefi bilen bir varlık, herhangi bir anda kaç istemcinin abone olduğunu görebilir, ancak hangi istemcilerin eklendiğini veya iptal edildiğini izleyemez.

Sunucular, istemcilerin listedeki konumlarını öğrenmelerini ve diğer istemcilerin ne zaman eklendiğini veya iptal edildiğini çıkarsamalarını önlemek için her seferinde şifreli LS2 oluşturduklarında istemcilerin sırasını rastgeleleştirmelidir.

Bir sunucu, yetkilendirme verisi listesine rastgele girişler ekleyerek abone olan istemci sayısını gizlemeyi seçebilir.

DH istemci yetkilendirmesinin avantajları
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Şemanın güvenliği, istemci anahtar malzemesinin dış bant değiş tokuşuna tamamen bağlı değildir. İstemcinin özel anahtarı cihazından asla çıkmaz, bu nedenle dış bant değiş tokuşunu ele geçirebilen ancak DH algoritmasını kıramayan bir düşman, şifreli LS2'yi çözemeyecek veya istemcinin erişiminin ne kadar süreyle verildiğini belirleyemeyecektir.

DH istemci yetkilendirmesinin dezavantajları
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- N istemci için sunucu tarafında N + 1 DH işlemi gerektirir.
- İstemci tarafında bir DH işlemi gerektirir.
- İstemcinin gizli anahtarı üretmesini gerektirir.

PSK istemci yetkilendirmesinin avantajları
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- DH işlemi gerektirmez.
- Sunucunun gizli anahtarı üretmesine izin verir.
- İstendiği takdirde sunucunun aynı anahtarı birden fazla istemciyle paylaşmasına izin verir.

PSK istemci yetkilendirmesinin dezavantajları
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Şemanın güvenliği, istemci anahtar malzemesinin dış bant değiş tokuşuna kritik olarak bağlıdır. Belirli bir istemci için değiş tokuşu ele geçiren bir düşman, istemcinin yetkilendirildiği herhangi bir sonraki şifreli LS2'yi çözebilir ve ayrıca istemcinin erişiminin ne zaman iptal edildiğini belirleyebilir.


### Base 32 Adreslerle Şifreli LS

Teklif 149'a bakın.

Compact announce yanıtları 32 bayt olduğu için bittorrent için şifreli LS2 kullanamazsınız. 32 bayt sadece karmayı içerir. Lease set'in şifreli olduğunu veya imza türlerini belirten bir alan yoktur.



### Çevrimdışı Anahtarlarla Şifreli LS

Çevrimdışı anahtarlarla şifreli lease set'ler için, gizlenmiş özel anahtarlar da her gün için çevrimdışı oluşturulmalıdır.

İsteğe bağlı çevrimdışı imza bloğu şifreli lease set'in açık metin kısmında olduğundan, floodfill'eri tarayan herkes bu lease set'i (ancak şifresini çözmeden) birkaç gün boyunca izlemek için kullanabilir. Bunu önlemek için, anahtar sahibi her gün için yeni geçici anahtarlar üretmelidir. Hem geçici hem de gizlenmiş anahtarlar önceden üretilebilir ve toplu olarak yönlendiriciye teslim edilebilir.

Bu teklifte, birden fazla geçici ve gizlenmiş anahtarı paketlemek ve istemciye veya yönlendiriciye sağlamak için bir dosya biçimi tanımlanmamıştır. Çevrimdışı anahtarlarla şifreli lease set'leri desteklemek için bu teklifte bir I2CP protokolü geliştirilmesi tanımlanmamıştır.



### Notlar

- Şifreli lease set'ler kullanan bir hizmet, şifreli sürümü floodfill'lere yayınlar. Ancak verimlilik için, kimlik doğrulamasından sonra (örneğin beyaz liste ile) istemcilere sarılmış sarımsak mesajında şifrelenmemiş lease set'ler gönderir.

- Floodfill'ler, kötüye kullanımı önlemek için maksimum boyutu makul bir değere sınırlayabilir.

- Şifre çözmeden sonra, iç zaman damgasının ve sona ermenin üst düzeydekilerle eşleştiğinden emin olmak için birkaç kontrol yapılmalıdır.

- ChaCha20, AES yerine seçildi. AES donanım desteği mevcutsa hızlar benzer olsa da, düşük uç ARM cihazlarında olduğu gibi AES donanım desteği mevcut olmadığında ChaCha20 2.5-3 kat daha hızlıdır.

- Hız konusunda keyed BLAKE2b kullanmak kadar endişelenmiyoruz. En büyük n ihtiyacımızı karşılayacak kadar büyük bir çıktı boyutuna sahiptir (veya istenen anahtar başına bir kez çağrılabilir bir sayaç argümanı ile). BLAKE2b SHA-256'dan çok daha hızlıdır ve keyed-BLAKE2b toplam hash fonksiyonu çağrı sayısını azaltır. Ancak, diğer nedenlerle BLAKE2b'ye geçmeyi öneren teklif 148'e bakın. [Secure key derivation performance](https://www.lvh.io/posts/secure-key-derivation-performance.html) bölümüne bakın.


### Meta LS2

Bu, çoklu barındırmayı değiştirmek için kullanılır. Herhangi bir lease set gibi, bu da oluşturucusu tarafından imzalanır. Bu, hedef karmalarının kimliği doğrulanmış bir listesidir.

Meta LS2, bir ağaç yapısının en üstü ve olası ara düğümleridir. Bir LS, LS2 veya başka bir Meta LS2'ye işaret eden bir dizi girdi içerir ve büyük ölçekli çoklu barındırmayı destekler. Bir Meta LS2, LS, LS2 ve Meta LS2 girişlerinin karışımını içerebilir. Ağacın yaprakları her zaman bir LS veya LS2'dir. Ağaç bir DAG'dır; döngülere izin verilmez; aramalar yapan istemciler döngüleri tespit etmeli ve takip etmeyi reddetmelidir.

Meta LS2'nin standart bir LS veya LS2'den çok daha uzun bir sona erme süresi olabilir. En üst seviyenin yayın tarihinden birkaç saat sonra sona ermesi olabilir. Maksimum sona erme süresi floodfill'ler ve istemciler tarafından zorlanır ve TBD'dir.

Meta LS2'nin kullanım durumu büyük ölçekli çoklu barındırmadır, ancak LS veya LS2 ile şu anda sağlanandan daha fazla, yönlendiricilerin lease set'lerle korelasyonunu (yönlendirici yeniden başlatma zamanında) koruma sağlamaz. Bu, muhtemelen korelasyon korumasına ihtiyaç duymayan "facebook" kullanım durumuyla eşdeğerdir. Bu kullanım durumu muhtemelen çevrimdışı anahtarlara ihtiyaç duyar, bu anahtarlar ağaçtaki her düğümde standart başlıkta sağlanır.

Yaprak yönlendiriciler, ara ve ana Meta LS imzalayanlar arasındaki arka uç protokolü burada belirtilmemiştir. Gereksinimler son derece basittir - sadece eşin çalışır durumda olduğunu doğrulamak ve birkaç saatte bir yeni bir LS yayınlamak. Tek karmaşıklık, başarısızlık durumunda en üst seviye veya ara seviye Meta LS'ler için yeni yayıncılar seçmektir.

Birden fazla yönlendiriciden lease'lerin birleştirilip, imzalanıp, tek bir lease set'te yayınlandığı karışık lease set'ler, teklif 140, "görünmez çoklu barındırma"da belgelenmiştir. Bu teklif, akış bağlantılarının tek bir yönlendiriciye "sıkı" olmayacağı için yazılı olduğu gibi uygulanamaz, http://zzz.i2p/topics/2335 adresine bakın.

Görünmez çoklu barındırma için arka uç protokolü ve yönlendirici ile istemci iç yapısıyla etkileşim oldukça karmaşık olacaktır.

En üst seviye Meta LS için floodfill'in aşırı yüklenmesini önlemek için, sona erme süresi en az birkaç saat olmalıdır. İstemciler en üst seviye Meta LS'yi önbelleğe almalı ve süresi dolmamışsa yeniden başlatmalarda kalıcı hale getirmelidir.

Ağaçta dolaşmak için bazı algoritmalar tanımlamamız gerekiyor, dahil olmak üzere yedekleme, böylece kullanım dağıtılmış olur. Karma mesafesi, maliyeti ve rastgelelik fonksiyonu. Bir düğümde hem LS veya LS2 hem de Meta LS varsa, bu lease set'lerin ne zaman kullanılmasına izin verildiğini ve ne zaman ağaçta dolaşmaya devam edilmesi gerektiğini bilmemiz gerekir.




Arama ile
    Standart LS bayrağı (1)
Depolama ile
    Meta LS2 türü (7)
Depolama konumu
    Hedefin karması
    Bu karma daha sonra LS1'de olduğu gibi günlük "yönlendirme anahtarı" oluşturmak için kullanılır
Tipik sona erme
    Saatler. Maksimum 18.2 saat (65535 saniye)
Yayınlayan
    "ana" Hedef veya koordine edici, veya ara koordine ediciler

### Biçim

```
Yukarıda belirtildiği gibi Standart LS2 Başlığı

  Meta LS2 Türüne Özel Bölüm
  - Özellikler (Ortak yapılar spesifikasyonunda belirtildiği gibi Haritalama, yoksa 2 sıfır bayt)
  - Girişlerin sayısı (1 bayt) Maksimum TBD
  - Girişler. Her giriş şunları içerir: (40 bayt)
    - Karma (32 bayt)
    - Bayraklar (2 bayt)
      TBD. Gelecekteki kullanımlarla uyumlu olması için hepsini sıfıra ayarlayın.
    - Tür (1 bayt) Başvurduğu LS'nin türü;
      1 LS için, 3 LS2 için, 5 şifreli için, 7 meta için, 0 bilinmeyen için.
    - Maliyet (öncelik) (1 bayt)
    - Sona erer (4 bayt) (4 bayt, büyük endian, epoch'tan bu yana saniye cinsinden, 2106'da döner)
  - İptallerin sayısı (1 bayt) Maksimum TBD
  - İptaller: Her iptal şunları içerir: (32 bayt)
    - Karma (32 bayt)

  Standart LS2 İmzası:
  - İmza (40+ bay
