---
title: "Giden Tünel Değiştirme için I2CP Bayrağı"
number: "171"
author: "onon, eyedeekay"
created: "2026-05-19"
lastupdated: "2026-05-23"
status: "Taslak"
toc: true
---

## Genel Bakış

Teslim onayları sessizce kaybolduğunda, akış istemcisi bağlantıları askıya alınabilir. Gönderen, bir onay alana veya bağlantı koparılana kadar yeniden iletir ve karşı tarafa onayların ulaşması konusunda güvenilir bir şekilde doğrulama imkânı yoktur. Bu öneri, bir istemcinin, aynı hedefe yönelik sonraki mesajlar için yönlendiricinin farklı bir giden tünel seçmesini talimatlandırmasına olanak tanıyan, [SendMessageExpiresMessage](/docs/specs/i2cp/) bayraklar alanına yeni bir bayt biti ekler. Akış protokolü, bağlantı askıya alındığında tünelden geçişi başlatmak için bu biti kullanır.

## Tetikleyiciler

İstemcinin bir sonraki giden mesajda bayrağı ayarlamasını SAĞLAMASI gereken iki koşul vardır. Bu koşullar akış katmanında ölçülür.

**Gönderen taraf**

İstemcinin mevcut yeniden iletme zaman aşımı süresi içinde bir onay alınmadı.

**Alıcı taraf**

Alıcı, aynı verinin uzak uç tarafından birden fazla kez yeniden iletildiğini gözlemlemiştir ve bu durum, alıcının onaylarının (acknowledgments) uzak uca ulaşmadığını gösterir. Alıcı, onayların farklı bir yol üzerinden uzak uca ulaşmasını sağlamak için bir sonraki giden I2CP mesajında bu bayrağı ayarlamalıdır. Alıcı bayrağı ayarlamadan önce şu koşulların gerçekleşmesini beklemelidir: (1) bir çoğaltının alınmış olması, (2) en az bir onay gönderilmesi ve (3) uzak uç tarafından yeniden iletimin tekrar yapılması.

Zamanlama-korelasyon saldırılarını sınırlamak için bir istemci, her bağlantı başına 10 saniyelik süre içinde bayrağı bir kereden fazla ayarlamamalıdır. İstemci, durma koşulunu tespit ettikten sonra zamanlama-korelasyon hassasiyetini azaltmak için bayrağı, T istemcinin şu anki milisaniye cinsinden yeniden iletim zaman aşımı olmak üzere, `[0, min(T/4, 2000ms)]` aralığından eşit şekilde seçilen bir jiter kadar geciktirmelidir.

## Spesifikasyon

[SendMessageExpiresMessage](/docs/specs/i2cp/) mesajının bayraklar (flags) alanı, Tarih (Date) alanından sonraki üst 2 baytı işgal eder (0.8.4 sürümüyle yeniden tanımlanmıştır) ve büyük endian olarak iletilir. Bit 15 şu anda kullanılmamaktadır; bu teklif, bit 15'i tanımlamaktadır.

Bit sırası: 15...0

| Bit | Ad | Açıklama |
|-----|------|-------------|
| 15 | SWITCH_OUTBOUND_TUNNEL | 1 ise, yönlendirici bu hedefe gönderilecek sonraki mesajlar için havuzundan farklı bir giden tünel seçmelidir. Alternatif tünel mevcut değilse, bu bayrak sessizce yok sayılır. Yönlendirici yalnızca bu bayrağın ayarlanmış olmasından dolayı daha önce kullanılan tüneli kapatmamalı veya devre dışı bırakmamalıdır. |
Bu bayrak varsayılan olarak 0'dır. Bunu uygulamayan yönlendiriciler, hata vermeden bunu yoksaymalıdır.

## Uygulama Notları

`SWITCH_OUTBOUND_TUNNEL` ayarlandığında, yönlendirici giden havuzundan aşağıdaki hariç, tüneli rastgele eşit olasılıkla seçmelidir:

- bu oturum için şu anda kullanılan tünel, ve
- havuzdaki, varsa en son başarısız olan tek tünel.

Diğer tüm tünel sağlık ölçümleri, oluşturma süreleri veya seçim geçmişi, sybil saldırganlarını avantajlı duruma getirebileceği için seçimi ETKİLEMEMELİDİR. Havuzda bu dışlamalardan sonra uygun tünel kalmamışsa bayrak sessizce yok sayılır.

Bu bayrak ek tünel mesajları doğurmaz; tünel değiştirme görünür gecikmeyi değiştirebilir. Bağlantı başına 10 saniyelik oran sınırı (Tetikleyiciler'e bakın) aşırı değiştirme yapmayı engeller.

## Anonimlik Hususları

[SendMessageExpiresMessage](/docs/specs/i2cp/) içindeki bayraklar, istemci ile kendi yönlendiricisi arasındaki yerel bir arayüz olan I2CP üzerinden taşınır. Bu bayraklar ağ gözlemcileri tarafından görülemez.

Anonimlik riski trafik desenlerine dayalıdır: birden fazla tünel ucunu gözlemleyebilen bir düşman, tünel kullanımının *ne zaman* değiştiğini görebilir.

İstemci tarafında oluşan bir donmaya doğrudan yanıt olarak giden tünelleri değiştirmek, tespit edilebilir bir davranış deseni yaratır. İki somut gözlem vektörü vardır:

**Giden tünelin ilk sıçramalarına yapılan Sybil saldırısı**

Her giden tünelin ilk sıçraması, gönderen yönlendiriciden o tünele giren tüm trafiği görür. Göndericinin havuzundaki birden fazla tünelin ilk sıçramasını kontrol eden bir saldırgan, bir ilk sıçramadaki trafiğin durduğunu ve yakın zamanda başka birinde başladığını gözlemler ve bu şekilde her iki tüneli de aynı göndericiyle ilişkilendirir. N tünel içeren bir havuzda, K tane ilk sıçramayı kontrol eden bir saldırgan, verilen bir geçiş olayını K/N olasılıkla gözlemleyebilir.

**Trafik aralığı zamanlaması**

Tıkanma sırasında istemci yeni veri göndermez, bu nedenle eski giden tünel sessiz kalır. Değişim gerçekleştiğinde trafik farklı bir yolda yeniden başlar. Gönderenin yönlendiricisinde — örneğin gönderenin ağ sağlayıcısı veya ilk zıplama düğümü kendisi gibi — bir gözlem konumuna sahip olan bir saldırgan, sessizlik-sonra-tekrar-başlama desenini görebilir. Boşluk süresi ayrıca istemcinin mevcut yeniden iletme zaman aşımı değerinin bir tahminini de ortaya çıkarır.

İstemcilerin Tetikleyicilerde belirtilen hız sınırlama ve jitter gereksinimlerine uyması ZORUNLUDUR.

## Referanslar

- [I2CP Spesifikasyonu](/docs/specs/i2cp/)
