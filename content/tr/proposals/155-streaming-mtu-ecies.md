---
title: "ECIES Hedefleri için Akış MTU'su"
number: "155"
author: "zzz"
created: "2020-05-06"
lastupdated: "2020-05-30"
status: "Kapalı"
thread: "http://zzz.i2p/topics/2886"
target: "0.9.47"
implementedin: "0.9.47"
toc: true
---
## Not

Ağda dağıtım ve test devam etmektedir.  
Küçük revizyonlara tabidir.


## Genel Bakış


### Özet

ECIES, mevcut oturum (ES) mesaj yükünü yaklaşık 90 bayt azaltır.  
Bu nedenle ECIES bağlantıları için MTU'yu yaklaşık 90 bayt artırabiliriz.  
Aşağıdaki belgelere bakın: [ECIES spesifikasyonu](/docs/specs/ecies/#overhead), [Streaming spesifikasyonu](/docs/specs/streaming/#flags-and-option-data-fields) ve [Streaming API belgeleri](/docs/api/streaming/).

MTU artırılmazsa, birçok durumda yük tasarrufu aslında "kazanılmaz",  
çünkü mesajlar zaten iki tam tünel mesajı kullanacak şekilde doldurulur.

Bu öneri, spesifikasyonlarda herhangi bir değişiklik gerektirmez.  
Sadece önerilen değer ve uygulama detayları üzerine tartışma ve fikir birliği sağlanması amacıyla yayınlanmıştır.


### Amaçlar

- Anlaşmaya varılan MTU'yu artırmak
- 1 KB'lık tünel mesajlarının kullanımını en üst düzeye çıkarmak
- Akış protokolünde değişiklik yapmamak


## Tasarım

Mevcut MAX_PACKET_SIZE_INCLUDED seçeneğini ve MTU anlaşmasını kullanın.  
Akış, gönderilen ve alınan MTU'nun minimumunu kullanmaya devam eder.  
Varsayılan değer tüm bağlantılar için 1730'dur, kullanılan anahtar ne olursa olsun.

Uygulamaların, her iki yönde de tüm SYN paketlerine MAX_PACKET_SIZE_INCLUDED seçeneğini eklemeleri teşvik edilir,  
ancak bu bir zorunluluk değildir.

Hedef yalnızca ECIES ise, daha yüksek değeri kullanın (Alice ya da Bob olarak).  
Hedef çift anahtarlıysa davranış değişebilir:

Eğer çift anahtarlı istemci yönlendiricinin dışında ise (dış bir uygulamada),  
uzaktaki uçtaki anahtarı "bilmeyebilir" ve Alice SYN'de daha yüksek bir değer isteyebilir,  
ancak SYN'deki maksimum veri 1730 olarak kalır.

Eğer çift anahtarlı istemci yönlendiricinin içindeyse, kullanılan anahtar  
istemci tarafından biliniyor olabilir ya da olmayabilir.  
Leaseset henüz alınmamış olabilir ya da iç API arayüzleri bu bilgiyi istemciye kolayca sağlayamıyor olabilir.  
Eğer bilgi mevcutsa, Alice daha yüksek değeri kullanabilir;  
aksi takdirde, anlaşma sağlanana kadar Alice 1730 standart değerini kullanmalıdır.

Bob olarak bir çift anahtarlı istemci, Alice'den hiçbir değer ya da 1730 değeri alınmış olsa bile,  
yanıtta daha yüksek bir değer gönderebilir;  
ancak akışta yukarı yönlü anlaşma için bir düzenleme yoktur,  
bu yüzden MTU 1730 olarak kalmalıdır.

[Streaming API belgelerinde](/docs/api/streaming/) belirtildiği gibi,  
Alice'den Bob'a gönderilen SYN paketlerindeki veri, Bob'un MTU'sunu aşabilir.  
Bu, akış protokolünün bir zayıflığıdır.  
Bu nedenle, çift anahtarlı istemciler gönderilen SYN paketlerindeki veriyi  
1730 baytla sınırlamalı, ancak daha yüksek bir MTU seçeneği göndermelidir.  
Bob'dan daha yüksek MTU alındıktan sonra, Alice gönderilen gerçek maksimum yükü artırabilir.


### Analiz

[ECIES spesifikasyonunda](/docs/specs/ecies/#overhead) açıklandığı gibi, mevcut oturum mesajları için ElGamal yükü  
151 bayt, Ratchet yükü ise 69 bayttır.  
Bu nedenle, ratchet bağlantıları için MTU'yu (151 - 69) = 82 bayt artırabiliriz,  
1730'dan 1812'ye.


## Spesifikasyon

[Streaming API belgelerinin](/docs/api/streaming/) MTU Seçimi ve Anlaşması bölümüne aşağıdaki değişiklikleri ve açıklamaları ekleyin.  
[Streaming spesifikasyonuna](/docs/specs/streaming/) değişiklik gerekmez.

i2p.streaming.maxMessageSize seçeneğinin varsayılan değeri, kullanılan anahtar ne olursa olsun tüm bağlantılar için 1730 olarak kalır.  
İstemciler, her zamanki gibi, gönderilen ve alınan MTU'nun minimumunu kullanmalıdır.

Dört ilgili MTU sabiti ve değişkeni vardır:

- DEFAULT_MTU: 1730, değişmeden, tüm bağlantılar için
- i2cp.streaming.maxMessageSize: varsayılan 1730 veya 1812, yapılandırmayla değiştirilebilir
- ALICE_SYN_MAX_DATA: Alice'in bir SYN paketine ekleyebileceği maksimum veri
- negotiated_mtu: Alice'in ve Bob'un MTU'larının minimumu, Bob'dan Alice'e gönderilen SYN ACK'de ve her iki yönde gönderilen tüm sonraki paketlerde kullanılacak maksimum veri boyutu olarak


Beş durum dikkate alınmalıdır:


### 1) Alice yalnızca ElGamal
Değişiklik yok, tüm paketlerde 1730 MTU.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize varsayılan: 1730
- Alice SYN'de MAX_PACKET_SIZE_INCLUDED gönderebilir, 1730'dan farklı olmadığı sürece zorunlu değil


### 2) Alice yalnızca ECIES
Tüm paketlerde 1812 MTU.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize varsayılan: 1812
- Alice SYN'de MAX_PACKET_SIZE_INCLUDED göndermelidir


### 3) Alice çift anahtarlı ve Bob'un ElGamal olduğunu biliyor
Tüm paketlerde 1730 MTU.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize varsayılan: 1812
- Alice SYN'de MAX_PACKET_SIZE_INCLUDED gönderebilir, 1730'dan farklı olmadığı sürece zorunlu değil


### 4) Alice çift anahtarlı ve Bob'un ECIES olduğunu biliyor
Tüm paketlerde 1812 MTU.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize varsayılan: 1812
- Alice SYN'de MAX_PACKET_SIZE_INCLUDED göndermelidir


### 5) Alice çift anahtarlı ve Bob anahtarı bilinmiyor
SYN paketine MAX_PACKET_SIZE_INCLUDED olarak 1812 gönderin ancak SYN paketi verisini 1730 ile sınırlayın.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize varsayılan: 1812
- Alice SYN'de MAX_PACKET_SIZE_INCLUDED göndermelidir


### Tüm durumlar için

Alice ve Bob, Bob'dan Alice'e gönderilen SYN ACK'de ve her iki yönde gönderilen tüm sonraki paketlerde kullanılacak maksimum veri boyutu olarak, Alice'in ve Bob'un MTU'larının minimumu olan negotiated_mtu'yu hesaplar.


## Gerekçe

Neden mevcut değer 1730 olduğunu görmek için [Java I2P kaynak koduna](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220) bakın.  
Neden ECIES yükü ElGamal'den 82 bayt daha az olduğunu görmek için [ECIES spesifikasyonuna](/docs/specs/ecies/#overhead) bakın.


## Uygulama Notları

Akış, en uygun boyutta mesajlar oluşturuyorsa, ECIES-Ratchet katmanının bu boyutun üzerine doldurma yapmaması çok önemlidir.

İki tünel mesajına sığması için en uygun Garlic Mesaj boyutu, 16 baytlık Garlic Mesaj I2NP başlığı, 4 baytlık Garlic Mesaj Uzunluğu, 8 baytlık ES etiketi ve 16 baytlık MAC dahil olmak üzere 1956 bayttır.

ECIES'de önerilen bir doldurma algoritması aşağıdaki gibidir:

- Garlic Mesaj toplam uzunluğu 1954-1956 bayt olacaksa, doldurma bloğu ekleme (yer yok)
- Garlic Mesaj toplam uzunluğu 1938-1953 bayt olacaksa, tam olarak 1956 bayta doldurmak için bir doldurma bloğu ekle
- Aksi takdirde, örneğin 0-15 bayt rastgele miktarda olacak şekilde normal şekilde doldur

Benzer stratejiler, en uygun tek tünel mesajı boyutu (964) ve üç tünel mesajı boyutu (2952) için de kullanılabilir, ancak bu boyutlar pratikte nadiren görülür.


## Sorunlar

1812 değeri ön karardır. Doğrulanacak ve muhtemelen ayarlanacaktır.


## Geçiş

Geriye dönük uyumluluk sorunu yoktur.  
Bu, mevcut bir seçenektir ve MTU anlaşması zaten spesifikasyonun bir parçasıdır.

Eski ECIES hedefleri 1730'u destekleyecektir.  
Daha yüksek bir değer alan herhangi bir istemci 1730 ile yanıt verecek ve uzak uç, normal şekilde aşağıya doğru anlaşmaya varacaktır.


## Referanslar

* [CALCULATION](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220)
* [ECIES](/docs/specs/ecies/#overhead)
* [STREAMING-OPTIONS](/docs/api/streaming/)
* [STREAMING-SPEC](/docs/specs/streaming/#flags-and-option-data-fields)
