---
title: "RI ve Hedef Doldurma"
number: "161"
author: "zzz"
created: "2022-09-28"
lastupdated: "2023-01-02"
status: "Açık"
thread: "http://zzz.i2p/topics/3279"
target: "0.9.57"
toc: true
---
## Durum

0.9.57 sürümünde uygulandı.  
"Gelecek Planlaması" bölümündeki fikirleri geliştirmek ve tartışmak için bu teklifi açık bırakıyoruz.


## Genel Bakış


### Özet

Destinations (Hedefler) içindeki ElGamal açık anahtarı, 0.6 sürümünden beri (2005) kullanılmamaktadır.  
Belirtimlerimizde bu alanın kullanılmadığı belirtilse de, uygulamaların ElGamal anahtar çifti üretmeyi atlayıp alanı rastgele veriyle doldurabileceğini **söylememektedir**.

Alanın görmezden gelindiğini ve uygulamaların alanın rastgele veriyle doldurabileceğini belirten şekilde belirtimleri değiştirmeyi öneriyoruz.  
Bu değişiklik geriye dönük uyumludur. ElGamal açık anahtarını doğrulayan bilinen bir uygulama yoktur.

Ek olarak, bu teklif, Hedefler ve Yönlendirici Kimlikleri için rastgele veri üretimi konusunda uygulayıcılara rehberlik eder. Bu veri, güvenli olmaya devam ederken sıkıştırılabilir olmalı ve Base64 temsilleri bozuk veya güvensiz görünmemelidir.  
Bu, protokolde herhangi bir bozucu değişiklik olmadan alanların kaldırılmasının avantajlarının çoğunu sağlar.  
Sıkıştırılabilir Hedefler, akışlı SYN ve yanıtlanabilir datagram boyutunu azaltır;  
sıkıştırılabilir Yönlendirici Kimlikleri ise Veritabanı Depolama Mesajlarını, SSU2 Oturum Onay mesajlarını ve yeniden kaynak su3 dosyalarını küçültür.

Son olarak, teklif, dolguyu tamamen ortadan kaldıracak yeni Hedef ve Yönlendirici Kimliği formatları üzerindeki olasılıkları tartışır. Ayrıca kuantum sonrası kripto (post-quantum crypto) konusuna ve bunun gelecek planlamasını nasıl etkileyebileceğine dair kısa bir tartışma da yer alır.



### Amaçlar

- Hedefler için ElGamal anahtar çifti üretme gereksinimini ortadan kaldırmak
- Hedeflerin ve Yönlendirici Kimliklerinin yüksek oranda sıkıştırılabilir olmasına rağmen Base64 temsillerinde bariz desenler göstermemesi için en iyi uygulama yöntemlerini önermek
- Tüm uygulamaların bu en iyi uygulamaları benimsemesini teşvik ederek alanların birbirinden ayırt edilemez hale gelmesini sağlamak
- Akışlı SYN boyutunu azaltmak
- Yanıtlanabilir datagram boyutunu azaltmak
- SSU2 RI blok boyutunu azaltmak
- SSU2 Oturum Onay mesajı boyutunu ve parçalanma sıklığını azaltmak
- Veritabanı Depolama Mesajı (RI ile birlikte) boyutunu azaltmak
- Yeniden kaynak dosyası boyutunu azaltmak
- Tüm protokollerde ve API'lerde uyumluluğu korumak
- Belirtimleri güncellemek
- Yeni Hedef ve Yönlendirici Kimliği formatları için alternatifleri tartışmak

ElGamal anahtarı üretme gereksinimini ortadan kaldırarak, uygulamalar diğer protokollerdeki geriye dönük uyumluluk hususlarına bağlı kalmak kaydıyla ElGamal kodunu tamamen kaldırabilecektir.



## Tasarım

Kesin anlamıyla, Hedeflerde ve Yönlendirici Kimliklerindeki 32 baytlık imza açık anahtarı ile yalnızca Yönlendirici Kimliklerde bulunan 32 baytlık şifreleme açık anahtarı, bu yapıların SHA-256 karmalarının kriptografik olarak güçlü ve ağ veritabanı DHT'sinde rastgele dağılmış olmasını sağlayan tüm entropiyi sağlayan rastgele bir sayıdır.

Ancak, aşırı dikkatli olmak adına, ElG açık anahtar alanı ve dolgu için en az 32 bayt rastgele veri kullanılmasını öneriyoruz. Ayrıca, alanlar sıfır olsaydı, Base64 Hedefler uzun AAAA karakter dizileri içerecekti ve bu kullanıcılar için alarma veya kafa karışıklığına neden olabilir.

Ed25519 imza türü ve X25519 şifreleme türü için:  
Hedefler, rastgele verinin 11 kopyasını (352 bayt) içerecektir.  
Yönlendirici Kimlikleri ise rastgele verinin 10 kopyasını (320 bayt) içerecektir.



### Tahmini Tasarruf

Hedefler, her akışlı SYN ve yanıtlanabilir datagramda yer alır.  
Yönlendirici Bilgileri (Yönlendirici Kimlikleri içerir) Veritabanı Depolama Mesajlarında ve NTCP2 ve SSU2'deki Oturum Onay mesajlarında yer alır.

NTCP2, Yönlendirici Bilgisini sıkıştırmaz.  
Veritabanı Depolama Mesajlarındaki ve SSU2 Oturum Onay mesajlarındaki Rİ'ler gzip ile sıkıştırılır.  
Yönlendirici Bilgileri, yeniden kaynak SU3 dosyalarında zip ile sıkıştırılır.

Veritabanı Depolama Mesajlarındaki Hedefler sıkıştırılmaz.  
Akışlı SYN mesajları I2CP katmanında gzip ile sıkıştırılır.

Ed25519 imza türü ve X25519 şifreleme türü için, tahmini tasarruf:

| Veri Türü | Toplam Boyut | Anahtarlar ve Sertifika | Sıkıştırılmamış Dolgu | Sıkıştırılmış Dolgu | Boyut | Tasarruf |
|-----------|------------|---------------|----------------------|--------------------|------|---------|
| Hedef | 391 | 39 | 352 | 32 | 71 | 320 bayt (%%82) |
| Yönlendirici Kimliği | 391 | 71 | 320 | 32 | 103 | 288 bayt (%%74) |
| Yönlendirici Bilgisi | 1000 tipik | 71 | 320 | 32 | 722 tipik | 288 bayt (%%29) |

Notlar: 7 baytlık sertifikanın sıkıştırılamaz olduğunu ve ek gzip ek yükünün olmadığını varsayar.  
İkisi de doğru değildir ama etkileri küçüktür.  
Yönlendirici Bilgisindeki diğer sıkıştırılabilir bölümleri görmezden gelir.



## Belirtim

Mevcut belirtimlerimize önerilen değişiklikler aşağıda belgelenmiştir.


### Ortak Yapılar
Ortak yapılar belirtimini, 256 baytlık Hedef açık anahtar alanının görmezden gelindiğini ve rastgele veri içerebileceğini belirtecek şekilde değiştirmek.

Ortak yapılar belirtimine, Hedef açık anahtar alanı ile Hedef ve Yönlendirici Kimliğindeki dolgu alanları için en iyi uygulama yöntemlerini öneren bir bölüm eklemek, şu şekilde:

Güçlü bir kriptografik sözde rastgele sayı üreticisini (PRNG) kullanarak 32 bayt rastgele veri üretin ve bu 32 baytlık veriyi açık anahtar alanını (Hedefler için) ve dolgu alanını (Hedefler ve Yönlendirici Kimlikleri için) doldurmak üzere gerektiği kadar tekrarlayın.

### Özel Anahtar Dosyası
Özel anahtar dosyası (eepPriv.dat) biçimi resmi bir belirtim parçası değildir ancak [Java I2P javadocs](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html) ve diğer uygulamalarda belgelenmiştir.  
Bu, özel anahtarların farklı uygulamalara taşınabilir olmasını sağlar.  
Bu javadoca, şifreleme açık anahtarının rastgele dolgu olabileceğine ve şifreleme özel anahtarının tümü sıfır veya rastgele veri olabileceğine dair bir not ekleyin.

### SAM
SAM belirtiminde, şifreleme özel anahtarının kullanılmadığını ve görmezden gelinebileceğini belirtin.  
İstemci tarafından herhangi bir rastgele veri döndürülebilir.  
SAM Köprüsü, Base64 temsili bozuk görünmesin diye tüm sıfır yerine rastgele veri döndürebilir (DEST GENERATE veya SESSION CREATE DESTINATION=TRANSIENT ile oluşturulurken).


### I2CP
I2CP'ye herhangi bir değişiklik gerekmez. Hedefteki şifreleme açık anahtarı için özel anahtar yönlendiriciye gönderilmez.


## Gelecek Planlaması


### Protokol Değişiklikleri

Protokol değişiklikleri maliyeti ve geriye dönük uyumsuzluk bedeliyle, Hedef, Yönlendirici Kimliği veya her ikisindeki dolgu alanını ortadan kaldırmak için protokollerimizi ve belirtimlerimizi değiştirebiliriz.

Bu teklif, yalnızca bir anahtar ve bir tür alanını içeren "b33" şifreli leaseset formatına benzerlik gösterir.

Kısmi uyumluluğu korumak için, belirli protokol katmanları diğer katmanlara sunmak üzere dolgu alanını sıfırlarla "genişletebilir".

Hedefler için, anahtar sertifikasındaki şifreleme türü alanını da iki bayt tasarrufu ile kaldırabiliriz.  
Alternatif olarak, Hedefler anahtar sertifikasında sıfır açık anahtar (ve dolgu) belirten yeni bir şifreleme türü alabilir.

Eski ve yeni formatlar arasında uyumluluk dönüşümü herhangi bir protokol katmanında sağlanmazsa, aşağıdaki belirtimler, API'ler, protokoller ve uygulamalar etkilenecektir:

- Ortak yapılar belirtimi
- I2NP
- I2CP
- NTCP2
- SSU2
- Ratchet
- Akış
- SAM
- Bittorrent
- Yeniden kaynaklama
- Özel Anahtar Dosyası
- Java çekirdek ve yönlendirici API'si
- i2pd API'si
- Üçüncü taraf SAM kütüphaneleri
- Paketlenmiş ve üçüncü taraf araçlar
- Birkaç Java eklentisi
- Kullanıcı arayüzleri
- P2P uygulamaları (örneğin MuWire, bitcoin, monero)
- hosts.txt, adres defteri ve abonelikler

Dönüşüm bazı katmanlarda belirtilirse, liste kısaltılabilir.

Bu değişikliklerin maliyetleri ve faydaları net değildir.

Özel teklifler belirlenecek:





### PQ Anahtarları

Herhangi bir öngörülen algoritma için Kuantum Sonrası (PQ) şifreleme açık anahtarları 256 bayttan büyüktür. Bu, Yönlendirici Kimlikleri için yukarıdaki önerilen değişikliklerden kaynaklanan herhangi bir dolguyu ve tasarrufu ortadan kaldırır.

SSL'ın yaptığı gibi bir "hibrit" PQ yaklaşımında, PQ anahtarları yalnızca geçici olur ve Yönlendirici Kimliğinde görünmez.

PQ imza anahtarları geçerli değildir ve Hedefler şifreleme açık anahtarı içermez.  
Ratchet için statik anahtarlar Hedefte değil, Lease Set'tedir.  
bu yüzden aşağıdaki tartışmadan Hedefleri çıkarabiliriz.

Dolayısıyla PQ yalnızca Yönlendirici Bilgilerini etkiler ve yalnızca PQ statik (geçici olmayan) anahtarları için, PQ hibriti için değil.  
Bu yeni bir şifreleme türü gerektirir ve NTCP2, SSU2 ve şifreli Veritabanı Arama Mesajları ile yanıtlarını etkiler.  
Tasarım, geliştirme ve devreye alma için tahmini zaman çerçevesi: ????????  
Ancak hibrit veya ratchet'ten sonra olur ????????????

Daha fazla tartışma için [bu konuya](http://zzz.i2p/topics/3294) bakın.




## Sorunlar

Yeni yönlendiriciler için örtme sağlamayı amaçlayarak ağı yavaş bir oranda yeniden anahtarlamak (rekeying) istenebilir.  
"Yeniden anahtarlamak", anahtarları gerçekten değiştirmekten ziyade yalnızca dolguyu değiştirmek anlamına gelebilir.

Mevcut Hedefleri yeniden anahtarlamak mümkün değildir.

Açık anahtar alanında dolgu bulunan Yönlendirici Kimlikleri, anahtar sertifikasında farklı bir şifreleme türü ile tanımlanmalı mıdır? Bu, uyumluluk sorunlarına neden olur.




## Geçiş

ElGamal anahtarını dolgu ile değiştirmek için geriye dönük uyumluluk sorunu yoktur.

Yeniden anahtarlamak uygulanırsa, üç önceki yönlendirici kimliği geçişiyle benzer olur:  
DSA-SHA1'den ECDSA imzalarına, ardından  
EdDSA imzalarına, ardından X25519 şifrelemeye.

Geriye dönük uyumluluk sorunlarına bağlı olarak ve SSU devre dışı bırakıldıktan sonra, uygulamalar ElGamal kodunu tamamen kaldırabilir.  
Ağdaki yönlendiricilerin yaklaşık %%14'ü ElGamal şifreleme türüdür ve bunlara birçok floodfill dahildir.

Java I2P için bir taslak birleştirme isteği [git.idk.i2p](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66) adresindedir.


## Kaynaklar

* [Ortak](/docs/specs/common-structures/)
* [Datagram](/docs/api/datagrams/)
* [I2CP](/docs/specs/i2cp/)
* [I2NP](/docs/specs/i2np/)
* [MR](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66)
* [NTCP2](/docs/specs/ntcp2/)
* [PKF](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html)
* [PQ](http://zzz.i2p/topics/3294)
* [SAM](/docs/api/samv3/)
* [SSU2](/docs/specs/ssu2/)
* [Akış](/docs/specs/streaming/)
