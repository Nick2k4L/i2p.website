---
title: "Yeni Şifreleme Öneri Şablonu"
aliases:
  - "/tr/proposals/142-ecies-template"
  - "/tr/proposals/142-ecies-template/"
number: "142"
author: "zzz"
created: "2018-01-11"
lastupdated: "2018-01-20"
status: "Meta"
thread: "http://zzz.i2p/topics/2499"
toc: true
---
## Genel Bakış

Bu belge, ElGamal asimetrik şifrelememizin yerine geçecek veya buna eklenecek bir öneri sunarken dikkate alınması gereken önemli konuları açıklamaktadır.

Bu bir bilgilendirme belgesidir.


## Motivasyon

ElGamal eski ve yavaştır ve daha iyi alternatifler mevcuttur. Ancak yeni bir algoritma eklemek veya geçiş yapmak için çözülmesi gereken birkaç sorun vardır. Bu belge bu çözülmemiş sorunlara dikkat çekmektedir.


## Arka Plan Araştırması

Yeni kripto öneren herkesin öncelikle aşağıdaki belgelerle aşina olması gerekir:

- [Teklif 111 NTCP2](/proposals/111-ntcp-2/)
- [Teklif 123 LS2](/proposals/123-new-netdb-entries/)
- [Teklif 136 deneysel imza türleri](/proposals/136-experimental-sigtypes/)
- [Teklif 137 isteğe bağlı imza türleri](/proposals/137-optional-sigtypes/)
- Yukarıdaki her bir teklif için buradaki tartışma başlıkları, içlerinde bağlantı verilmiştir
- [2018 teklif öncelikleri](http://zzz.i2p/topics/2494)
- [ECIES teklifi](http://zzz.i2p/topics/2418)
- [Yeni asimetrik kripto genel bakış](http://zzz.i2p/topics/1768)
- [Düşük seviye kripto genel bakış](/docs/specs/common-structures/)


## Asimetrik Kripto Kullanımları

Gözden geçirme amaçlı, ElGamal'ı şu amaçlarla kullanıyoruz:

1) Tünel Oluşturma mesajları (anahtar RouterIdentity içinde yer alır)

2) Netdb ve diğer I2NP mesajlarının yönlendirici-yönlendirici şifrelenmesi (Anahtar RouterIdentity içinde yer alır)

3) İstemci uçtan uca ElGamal+AES/OturumEtiketi (anahtar LeaseSet içinde yer alır, Hedef anahtarı kullanılmaz)

4) NTCP ve SSU için geçici DH


## Tasarım

ElGamal'ı başka bir şeyle değiştirmeyi öneren herhangi bir teklifin aşağıdaki ayrıntıları sağlaması gerekir.



## Spesifikasyon

Yeni asimetrik kripto için herhangi bir teklif aşağıdaki unsurları tam olarak belirtmelidir.



### 1. Genel

Teklifinizde aşağıdaki soruları yanıtlayın. Aşağıdaki 2. maddedeki teknik detaylardan ayrı bir teklif olması gerekebileceğine dikkat edin, çünkü bu mevcut 111, 123, 136, 137 veya diğer tekliflerle çakışabilir.

- Yukarıdaki 1-4 durumlarının hangileri için yeni kriptonun kullanılmasını öneriyorsunuz?
- Eğer 1) veya 2) (yönlendirici) içinse, açık anahtar RouterIdentity içinde mi yoksa RouterInfo props içinde mi yer alacak? Anahtar sertifikasında kripto türünü kullanmayı mı planlıyorsunuz? Tam olarak belirtin. Her iki durumda da kararınızı gerekçelendirin.
- Eğer 3) (istemci) içinse, açık anahtarı hedeften mi saklamayı ve anahtar sertifikasında kripto türünü mi kullanmayı planlıyorsunuz (ECIES teklifinde olduğu gibi), yoksa LS2'de mi saklamayı düşünüyorsunuz (123. teklif gibi), ya da başka bir şey mi? Tam olarak belirtin ve kararınızı gerekçelendirin.
- Tüm kullanımlar için destek nasıl duyurulacak? Eğer 3) içinse, bu LS2'ye mi eklenecek yoksa başka bir yere mi? Eğer 1) ve 2) içinse, bu 136 ve/veya 137. tekliflere benzer mi olacak? Tam olarak belirtin ve kararlarınızı gerekçelendirin. Muhtemelen bunun için ayrı bir teklif gerekecektir.
- Bunun nasıl ve neden geriye dönük uyumlu olduğunu tam olarak belirtin ve geçiş planını eksiksiz şekilde tanımlayın.
- Teklifinizin ön koşulu olan henüz uygulanmamış teklifler hangileridir?


### 2. Spesifik kripto türü

Teklifinizde aşağıdaki soruları yanıtlayın:

- Genel kripto bilgisi, spesifik eğriler/parametreler, seçiminizi tam olarak gerekçelendirin. Spesifikasyonlara ve diğer bilgilere bağlantılar verin.
- ElG ve diğer alternatiflerle karşılaştırılmış hız testi sonuçları (uygulanabiliyorsa). Şifreleme, çözme ve anahtar oluşturma işlemlerini dahil edin.
- C++ ve Java'da (hem OpenJDK, hem BouncyCastle hem de üçüncü taraf) kütüphane uygunluğu
  Üçüncü taraf veya Java dışı için bağlantılar ve lisanslar verin
- Önerilen kripto türü numarası/ları (deneysel aralıkta mı değil mi)
