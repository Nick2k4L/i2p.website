---
title: "Sarımsak Çiftliği Protokolü"
number: "150"
author: "zzz"
created: "2019-05-02"
lastupdated: "2019-05-20"
status: "Açık"
thread: "http://zzz.i2p/topics/2234"
toc: true
---
## Genel Bakış

Bu, JRaft'a dayalı, TCP üzerinden uygulama için "exts" kodunu ve "dmprinter" örnek uygulamasını temel alan Garlic Farm iletişim kuralı (wire protocol) teknik belgesidir [JRAFT](https://github.com/datatechnology/jraft).

Belgelenmiş bir iletişim kuralına sahip herhangi bir uygulama bulamadık. Ancak, JRaft uygulaması yeterince basit olduğu için kodu inceleyip ardından iletişim kuralını belgeleyebildik. Bu öneri, bu çalışmanın sonucudur.

Bu, Meta LeaseSet'e giriş yayınlayan yönlendiricilerin koordinasyonu için arka uç olacak. Öneri 123'e bakın.


## Amaçlar

- Küçük kod boyutu
- Mevcut uygulamaya dayalı olmak
- Serileştirilmiş Java nesneleri veya herhangi bir Java'ya özgü özellik ya da kodlama içermemek
- Başlangıç (bootstrapping) işlemleri bu protokolün kapsamı dışındadır. En az bir sunucunun sabit kodlanmış ya da bu protokolün dışında yapılandırılmış olduğu varsayılır.
- Hem dış bant (out-of-band) hem de I2P içinde kullanım senaryolarını desteklemek.


## Tasarım

Raft protokolü somut bir protokol değildir; yalnızca bir durum makinesi tanımlar. Bu nedenle, JRaft'ın somut iletişim kuralını belgeleyip protokolumuzu buna dayandırıyoruz. JRaft protokolüne, kimlik doğrulama el sıkışmasının eklenmesi dışında herhangi bir değişiklik yapılmamıştır.

Raft, bir günlük yayınlamaktan sorumlu bir Lider seçer. Günlük, Raft Yapılandırma verilerini ve Uygulama verilerini içerir. Uygulama verileri, her Sunucunun Yönlendiricisinin durumunu ve Meta LS2 kümesi için Hedefi içerir. Sunucular, Meta LS2'nin yayıncısını ve içeriğini belirlemek için ortak bir algoritma kullanır. Meta LS2'nin yayıncısı, Raft Lideri olmak zorunda değildir.



## Spesifikasyon

İletişim kuralı, SSL soketleri veya SSL olmayan I2P soketleri üzerinden çalışır. I2P soketleri HTTP Proxy üzerinden yönlendirilir. Açık ağ (clearnet) için SSL olmayan soket desteği yoktur.

### El sıkışma ve kimlik doğrulama

JRaft tarafından tanımlanmamıştır.

Amaçlar:

- Kullanıcı/parola kimlik doğrulama yöntemi
- Sürüm tanımlayıcısı
- Küme tanımlayıcısı
- Genişletilebilirlik
- I2P soketleri için kullanıldığında proxy üzerinden iletimin kolay olması
- Sunucuyu gereksiz yere bir Garlic Farm sunucusu olarak ortaya çıkarmamak
- Tam bir web sunucusu uygulaması gerektirmeyen basit bir protokol
- Yaygın standartlarla uyumlu olmak, böylece uygulamalar istenirse standart kütüphaneleri kullanabilsin

WebSocket benzeri bir el sıkışma ve HTTP Digest kimlik doğrulaması [RFC 2617](https://tools.ietf.org/html/rfc2617) kullanılacaktır. RFC 2617 Temel (Basic) kimlik doğrulaması desteklenmez. HTTP proxy üzerinden yönlendirme yapılırken, [RFC 2616](https://tools.ietf.org/html/rfc2616)'ya göre proxy ile iletişim kurulur.

#### Kimlik Bilgileri

Kullanıcı adlarının ve parolaların küme bazında mı yoksa sunucu bazında mı olduğu, uygulamaya bağlıdır.


#### HTTP İsteği 1

Başlatıcı aşağıdaki isteği gönderir.

Tüm satırlar HTTP'nin gerektirdiği gibi CRLF ile sonlandırılır.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: close
  (diğer tüm başlıklar göz ardı edilir)
  (boş satır)

  CLUSTER, kümenin adıdır (varsayılan "farm")
  VERSION, Garlic Farm sürümüdür (şu an "1")

```


#### HTTP Yanıtı 1

Yol doğru değilse, alıcı [RFC 2616](https://tools.ietf.org/html/rfc2616)'ya göre standart "HTTP/1.1 404 Not Found" yanıtını gönderir.

Yol doğruysa, alıcı [RFC 2617](https://tools.ietf.org/html/rfc2617)'ye göre WWW-Authenticate HTTP digest kimlik doğrulama başlığını içeren standart "HTTP/1.1 401 Unauthorized" yanıtını gönderir.

İki taraf da ardından soketi kapatır.


#### HTTP İsteği 2

Başlatıcı aşağıdaki isteği gönderir,
[RFC 2617](https://tools.ietf.org/html/rfc2617)'ye göre.

Tüm satırlar HTTP'nin gerektirdiği gibi CRLF ile sonlandırılır.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: keep-alive, Upgrade
  Upgrade: websocket
  (proxy kullanılıyorsa Sec-Websocket-* başlıkları)
  Authorization: (RFC 2617'ye göre HTTP digest yetkilendirme başlığı)
  (diğer tüm başlıklar göz ardı edilir)
  (boş satır)

  CLUSTER, kümenin adıdır (varsayılan "farm")
  VERSION, Garlic Farm sürümüdür (şu an "1")

```


#### HTTP Yanıtı 2

Kimlik doğrulama doğru değilse, alıcı yine [RFC 2617](https://tools.ietf.org/html/rfc2617)'ye göre "HTTP/1.1 401 Unauthorized" yanıtını gönderir.

Kimlik doğrulama doğruysa, alıcı aşağıdaki yanıtı gönderir,
WebSocket protokolüne göre.

Tüm satırlar HTTP'nin gerektirdiği gibi CRLF ile sonlandırılır.

```text

HTTP/1.1 101 Switching Protocols
  Connection: Upgrade
  Upgrade: websocket
  (Sec-Websocket-* başlıkları)
  (diğer tüm başlıklar göz ardı edilir)
  (boş satır)

```

Bu alındıktan sonra soket açık kalır. Aşağıda tanımlanan Raft protokolü, aynı sokette başlar.


#### Önbelleğe Alma

Kimlik bilgileri en az bir saat önbelleğe alınmalıdır, böylece
sonraki bağlantılar doğrudan yukarıdaki
"HTTP İsteği 2" aşamasına atlayabilir.



### Mesaj Türleri

İki tür mesaj vardır: istekler ve yanıtlar. İstekler Günlük Girişleri içerebilir ve değişken boyutludur; yanıtlar Günlük Girişleri içermeyip sabit boyutludur.

1-4 arası mesaj türleri, Raft tarafından tanımlanan standart RPC mesajlarıdır. Bu, temel Raft protokolüdür.

5-15 arası mesaj türleri, JRaft tarafından tanımlanan, istemcileri, dinamik sunucu değişikliklerini ve verimli günlük eşitlemesini desteklemek için genişletilmiş RPC mesajlarıdır.

16-17 arası mesaj türleri, Raft Bölüm 7'de tanımlanan Günlük Sıkıştırma RPC mesajlarıdır.


| Mesaj | Numara | Gönderen | Alan | Notlar |
| :--- | :--- | :--- | :--- | :--- |
| RequestVoteRequest | 1 | Aday | Takipçi | Standart Raft RPC; günlük girişleri içermemelidir |
| RequestVoteResponse | 2 | Takipçi | Aday | Standart Raft RPC |
| AppendEntriesRequest | 3 | Lider | Takipçi | Standart Raft RPC |
| AppendEntriesResponse | 4 | Takipçi | Lider / İstemci | Standart Raft RPC |
| ClientRequest | 5 | İstemci | Lider / Takipçi | Yanıt AppendEntriesResponse'tir; yalnızca Uygulama günlük girişleri içermelidir |
| AddServerRequest | 6 | İstemci | Lider | Yalnızca tek bir ClusterServer günlük girişi içermelidir |
| AddServerResponse | 7 | Lider | İstemci | Lider ayrıca bir JoinClusterRequest gönderir |
| RemoveServerRequest | 8 | Takipçi | Lider | Yalnızca tek bir ClusterServer günlük girişi içermelidir |
| RemoveServerResponse | 9 | Lider | Takipçi | |
| SyncLogRequest | 10 | Lider | Takipçi | Yalnızca tek bir LogPack günlük girişi içermelidir |
| SyncLogResponse | 11 | Takipçi | Lider | |
| JoinClusterRequest | 12 | Lider | Yeni Sunucu | Katılma daveti; yalnızca tek bir Yapılandırma günlük girişi içermelidir |
| JoinClusterResponse | 13 | Yeni Sunucu | Lider | |
| LeaveClusterRequest | 14 | Lider | Takipçi | Ayrılma komutu |
| LeaveClusterResponse | 15 | Takipçi | Lider | |
| InstallSnapshotRequest | 16 | Lider | Takipçi | Raft Bölüm 7; yalnızca tek bir SnapshotSyncRequest günlük girişi içermelidir |
| InstallSnapshotResponse | 17 | Takipçi | Lider | Raft Bölüm 7 |


### Kurulum

HTTP el sıkışmasından sonra, kurulum sırası aşağıdaki gibidir:

```text

Yeni Sunucu Alice              Rastgele Takipçi Bob

  ClientRequest   ------->
          <---------   AppendEntriesResponse

  Eğer Bob lider olduğunu söylerse, aşağıda devam edilir.
  Aksi takdirde, Alice Bob'dan ayrılmalı ve liderle bağlantı kurmalıdır.


  Yeni Sunucu Alice              Lider Charlie

  ClientRequest   ------->
          <---------   AppendEntriesResponse
  AddServerRequest   ------->
          <---------   AddServerResponse
          <---------   JoinClusterRequest
  JoinClusterResponse  ------->
          <---------   SyncLogRequest
                       OR InstallSnapshotRequest
  SyncLogResponse  ------->
  OR InstallSnapshotResponse

```

Ayrılma Sırası:

```text

Takipçi Alice              Lider Charlie

  RemoveServerRequest   ------->
          <---------   RemoveServerResponse
          <---------   LeaveClusterRequest
  LeaveClusterResponse  ------->

```

Seçim Sırası:

```text

Aday Alice               Takipçi Bob

  RequestVoteRequest   ------->
          <---------   RequestVoteResponse

  eğer Alice seçimleri kazanırsa:

  Lider Alice                Takipçi Bob

  AppendEntriesRequest   ------->
  (kalp atışı)
          <---------   AppendEntriesResponse

```


### Tanımlar

- Kaynak: Mesajın başlatıcısını tanımlar
- Hedef: Mesajın alıcısını tanımlar
- Terimler: Raft'a bakın. 0'dan başlar, monoton artar
- İndeksler: Raft'a bakın. 0'dan başlar, monoton artar



### İstekler

İstekler bir başlık ve sıfır veya daha fazla günlük girişi içerir. İstekler sabit boyutlu bir başlık ve değişken boyutlu isteğe bağlı Günlük Girişleri içerir.


#### İstek Başlığı

İstek başlığı 45 bayttır ve aşağıdaki gibidir. Tüm değerler işaretsiz büyük endian'dır.

```text

Mesaj türü:      1 bayt
  Kaynak:            Kimlik, 4 baytlık tamsayı
  Hedef:             Kimlik, 4 baytlık tamsayı
  Terim:             Geçerli terim (notlara bakın), 8 baytlık tamsayı
  Son Günlük Terimi: 8 baytlık tamsayı
  Son Günlük İndeksi: 8 baytlık tamsayı
  Onay İndeksi:      8 baytlık tamsayı
  Günlük girişleri boyutu: Toplam bayt cinsinden boyut, 4 baytlık tamsayı
  Günlük girişleri:       aşağıya bakın, belirtilen toplam uzunluk

```


#### Notlar

RequestVoteRequest'te, Terim adayın terimidir. Aksi takdirde, liderin geçerli terimidir.

AppendEntriesRequest'te, günlük girişleri boyutu sıfırsa, bu mesaj bir kalp atışı (keepalive) mesajıdır.



#### Günlük Girişleri

Günlük, sıfır veya daha fazla günlük girişi içerir. Her günlük girişi aşağıdaki gibidir. Tüm değerler işaretsiz büyük endian'dır.

```text

Terim:           8 baytlık tamsayı
  Değer türü:     1 bayt
  Giriş boyutu:   Bayt cinsinden, 4 baytlık tamsayı
  Giriş:          belirtilen uzunlukta

```


#### Günlük İçeriği

Tüm değerler işaretsiz büyük endian'dır.

| Günlük Değer Türü | Numara |
| :--- | :--- |
| Uygulama | 1 |
| Yapılandırma | 2 |
| ClusterServer | 3 |
| LogPack | 4 |
| SnapshotSyncRequest | 5 |


#### Uygulama

Uygulama içeriği UTF-8 kodlamalı [JSON](https://www.json.org/)'dur. Aşağıdaki Uygulama Katmanı bölümüne bakın.


#### Yapılandırma

Liderin yeni bir küme yapılandırmasını serileştirip eşlere çoğaltması için kullanılır. Sıfır veya daha fazla ClusterServer yapılandırması içerir.


```text

Günlük İndeksi:  8 baytlık tamsayı
  Son Günlük İndeksi:  8 baytlık tamsayı
  Her sunucu için ClusterServer Verisi:
    Kimlik:                4 baytlık tamsayı
    Uç nokta veri uzunluğu: Bayt cinsinden, 4 baytlık tamsayı
    Uç nokta verisi:     "tcp://localhost:9001" biçiminde ASCII dizesi, belirtilen uzunlukta

```


#### ClusterServer

Bir kümedeki sunucunun yapılandırma bilgisi. Bu yalnızca AddServerRequest veya RemoveServerRequest mesajında yer alır.

AddServerRequest Mesajında kullanıldığında:

```text

Kimlik:                4 baytlık tamsayı
  Uç nokta veri uzunluğu: Bayt cinsinden, 4 baytlık tamsayı
  Uç nokta verisi:     "tcp://localhost:9001" biçiminde ASCII dizesi, belirtilen uzunlukta

```


RemoveServerRequest Mesajında kullanıldığında:

```text

Kimlik:                4 baytlık tamsayı

```


#### LogPack

Bu yalnızca SyncLogRequest mesajında yer alır.

İletimden önce gzip ile sıkıştırılır:


```text

İndeks veri uzunluğu: Bayt cinsinden, 4 baytlık tamsayı
  Günlük veri uzunluğu:   Bayt cinsinden, 4 baytlık tamsayı
  İndeks verisi:     Her indeks için 8 bayt, belirtilen uzunlukta
  Günlük verisi:       belirtilen uzunlukta

```



#### SnapshotSyncRequest

Bu yalnızca InstallSnapshotRequest mesajında yer alır.

```text

Son Günlük İndeksi:  8 baytlık tamsayı
  Son Günlük Terimi:   8 baytlık tamsayı
  Yapılandırma veri uzunluğu: Bayt cinsinden, 4 baytlık tamsayı
  Yapılandırma verisi:     belirtilen uzunlukta
  Offset:          Veritabanındaki verinin bayt cinsinden ofseti, 8 baytlık tamsayı
  Veri uzunluğu:        Bayt cinsinden, 4 baytlık tamsayı
  Veri:            belirtilen uzunlukta
  Bitti mi:         Bitti ise 1, değilse 0 (1 bayt)

```




### Yanıtlar

Tüm yanıtlar 26 bayttır ve aşağıdaki gibidir. Tüm değerler işaretsiz büyük endian'dır.

```text

Mesaj türü:   1 bayt
  Kaynak:         Kimlik, 4 baytlık tamsayı
  Hedef:          Genellikle gerçek hedef kimliği (notlara bakın), 4 baytlık tamsayı
  Terim:           Geçerli terim, 8 baytlık tamsayı
  Sonraki İndeks: Liderin son günlük indeksi + 1'den başlar, 8 baytlık tamsayı
  Kabul Edildi mi: Kabul edildiyse 1, edilmediyse 0 (notlara bakın), 1 bayt

```


#### Notlar

Hedef Kimliği genellikle bu mesajın gerçek alıcısıdır. Ancak, AppendEntriesResponse, AddServerResponse ve RemoveServerResponse için, mevcut liderin kimliğidir.

RequestVoteResponse'te, Kabul Edildi mi alanı, aday (istek sahibi) için oy verildiğinde 1, oy verilmediğinde 0'dır.


## Uygulama Katmanı

Her Sunucu, periyodik olarak bir ClientRequest içinde Uygulama verisini günlüğe yazar. Uygulama verisi, her Sunucunun Yönlendiricisinin durumunu ve Meta LS2 kümesi için Hedefi içerir. Sunucular, Meta LS2'nin yayıncısını ve içeriğini belirlemek için ortak bir algoritma kullanır. Günlükte "en iyi" son duruma sahip sunucu, Meta LS2 yayıncısıdır. Meta LS2'nin yayıncısı, Raft Lideri olmak zorunda değildir.


### Uygulama Verisi İçeriği

Basitlik ve genişletilebilirlik için uygulama içeriği UTF-8 kodlamalı [JSON](https://json.org/) biçimindedir. Tam spesifikasyonu henüz belirlenmedi. Amaç, Meta LS2'yi yayınlamak için "en iyi" yönlendiriciyi belirleyecek bir algoritma yazmak için yeterli veri sağlamak ve yayıncının Meta LS2'deki Hedefleri ağırlıklandırmak için yeterli bilgiye sahip olmaktır. Veri, hem yönlendirici hem de Hedef istatistiklerini içerecektir.

Veri, isteğe bağlı olarak diğer sunucuların sağlığına dair uzaktan algılama verilerini ve Meta LS'yi çekme yeteneğini içerebilir. Bu veriler ilk sürümde desteklenmeyecektir.

Veri, isteğe bağlı olarak bir yönetici istemcisi tarafından gönderilen yapılandırma bilgilerini içerebilir. Bu veriler ilk sürümde desteklenmeyecektir.

Eğer "ad: değer" listelenmişse, bu JSON harita anahtarını ve değerini belirtir. Aksi takdirde, spesifikasyon henüz belirlenmedi.


Küme verisi (üst düzey):

- cluster: Küme adı
- date: Bu verinin tarihi (uzun, epoch'tan bu yana ms)
- id: Raft Kimliği (tamsayı)

Yapılandırma verisi (config):

- Herhangi bir yapılandırma parametresi

MetaLS yayınlama durumu (meta):

- destination: metals hedefi, base64
- lastPublishedLS: varsa, son yayınlanan metals'in base64 kodlaması
- lastPublishedTime: ms cinsinden, hiç yayınlanmadıysa 0
- publishConfig: Yayıncı yapılandırma durumu açık/kapalı/otomatik
- publishing: metals yayıncı durumu boolean true/false

Yönlendirici verisi (router):

- lastPublishedRI: varsa, son yayınlanan yönlendirici bilgisinin base64 kodlaması
- uptime: Çalışma süresi ms cinsinden
- Job gecikmesi
- Keşif tüneli
- Katılımcı tünel
- Yapılandırılmış bant genişliği
- Geçerli bant genişliği

Hedefler (destinations):
Liste

Hedef verisi:

- destination: hedef, base64
- uptime: Çalışma süresi ms cinsinden
- Yapılandırılmış tünel
- Geçerli tünel
- Yapılandırılmış bant genişliği
- Geçerli bant genişliği
- Yapılandırılmış bağlantılar
- Geçerli bağlantılar
- Karaliste verisi

Uzaktan yönlendirici algılama verisi:

- Görülen son RI sürümü
- LS Çekme süresi
- Bağlantı testi verisi
- En yakın floodfill'lerin profil verisi
  dün, bugün ve yarın için zaman dilimleri

Uzaktan hedef algılama verisi:

- Görülen son LS sürümü
- LS Çekme süresi
- Bağlantı testi verisi
- En yakın floodfill'lerin profil verisi
  dün, bugün ve yarın için zaman dilimleri

Meta LS algılama verisi:

- Görülen son sürüm
- Çekme süresi
- En yakın floodfill'lerin profil verisi
  dün, bugün ve yarın için zaman dilimleri


## Yönetim Arayüzü

Henüz belirlenmedi, muhtemelen ayrı bir öneri. İlk sürüm için gerekli değildir.

Bir yönetici arayüzünün gereksinimleri:

- Birden fazla ana hedefi desteklemek, yani birden fazla sanal küme (çiftlik)
- Üyeler tarafından yayınlanan tüm istatistikler, mevcut lider kim, vb. gibi paylaşılan küme durumuna kapsamlı bir görünüm sağlamak
- Bir katılımcıyı veya lideri kümeden zorla çıkarma yeteneği
- MetaLS'yi zorla yayınlama yeteneği (mevcut düğüm yayıncıysa)
- MetaLS'den hash'leri hariç tutma yeteneği (mevcut düğüm yayıncıysa)
- Toplu dağıtımlar için yapılandırma içe/dışa aktarma işlevselliği



## Yönlendirici Arayüzü

Henüz belirlenmedi, muhtemelen ayrı bir öneri. İlk sürüm için i2pcontrol gerekli değildir ve ayrıntılı değişiklikler ayrı bir öneriye dahil edilecektir.

Garlic Farm'tan yönlendiriciye API gereksinimleri (in-JVM java veya i2pcontrol)

- getLocalRouterStatus()
- getLocalLeafHash(Hash masterHash)
- getLocalLeafStatus(Hash leaf)
- getRemoteMeasuredStatus(Hash masterOrLeaf) // muhtemelen MVP'de değil
- publishMetaLS(Hash masterHash, List<MetaLease> contents) // ya da imzalı MetaLeaseSet? Kim imzalar?
- stopPublishingMetaLS(Hash masterHash)
- kimlik doğrulama henüz belirlenmedi?


## Gerekçe

Atomix çok büyük ve protokolü I2P üzerinden yönlendirmemiz için özelleştirmemize izin vermez. Ayrıca, iletişim formatı belgelenmemiştir ve Java serileştirmeye bağlıdır.


## Notlar



## Sorunlar

- Bir istemcinin bilinmeyen bir lideri bulup ona bağlanmasının bir yolu yoktur.
  Bir Takipçinin AppendEntriesResponse'te Yapılandırmayı Günlük Girişi olarak göndermesi için küçük bir değişiklik yapılabilir.



## Geçiş

Geriye dönük uyumluluk sorunu yoktur.


## Kaynaklar

* [JRAFT](https://github.com/datatechnology/jraft)
* [JSON](https://json.org/)
* [RAFT](/docs/research/ongaro2014-raft.pdf)
* [RFC-2616](https://tools.ietf.org/html/rfc2616)
* [RFC-2617](https://tools.ietf.org/html/rfc2617)
* [WEBSOCKET](https://en.wikipedia.org/wiki/WebSocket)
