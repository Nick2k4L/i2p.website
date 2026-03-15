---
title: "1-of-N veya N-of-N Tünellere OBEP Teslimatı"
number: "125"
author: "zzz, str4d"
created: "2016-03-10"
lastupdated: "2017-04-07"
status: "Open"
thread: "http://zzz.i2p/topics/2099"
toc: true
---
## Genel Bakış

Bu öneri, ağ performansını artırmak için iki iyileştirmeyi kapsar:

- OBEP'ye tek bir seçenek yerine alternatiflerin bir listesini sağlayarak IBGW seçiminin OBEP'ye devredilmesi.

- OBEP'te çok noktaya yayın (multicast) paket yönlendirmesini etkinleştirme.


## Gerekçe

Doğrudan bağlantı durumunda, OBEP'nin IBGW'lara nasıl bağlandığı konusunda esneklik sağlayarak bağlantı yoğunluğunu azaltmak amaçlanmaktadır. Birden fazla tünel belirtebilme yeteneği, OBEP'te çok noktaya yayın özelliğini uygulamamızı da mümkün kılar (mesajı belirtilen tüm tünellere ileterek).

Bu önerinin devretme kısmına alternatif olarak, hedef [RouterIdentity](/docs/specs/common-structures/#common-structure-specification) hash'ini belirtme yeteneğine benzer şekilde bir LeaseSet hash'i göndermek düşünülebilir. Bu, daha küçük bir mesaj ve potansiyel olarak daha yeni bir LeaseSet anlamına gelir. Ancak:

1. OBEP'yi bir arama yapmaya zorlar.

2. LeaseSet, floodfill'e yayınlanmamış olabilir; bu nedenle arama başarısız olur.

3. LeaseSet şifrelenmiş olabilir; bu nedenle OBEP kiralıkları (leases) alamaz.

4. Bir LeaseSet belirtmek, OBEP'ye mesajın [Destination](/docs/specs/common-structures/#destination)'ını ifşa eder. Aksi takdirde OBEP, LeaseSet'leri ağdaki tüm LeaseSet'lerden taramak ve Lease eşleşmesi aramak suretiyle bu bilgiye ulaşabilir.


## Tasarım

Başlatıcı (OBGW), yalnızca bir tanesini seçmek yerine, hedef [Leases](/docs/specs/common-structures/#lease)'lerin bazılarını (tümünü?) teslim talimatları olan [TUNNEL-DELIVERY](/docs/specs/i2np/#tunnel-message-delivery-instructions) içine yerleştirir.

OBEP, bunlardan birini teslim için seçer. OBEP, mümkünse zaten bağlı olduğu veya zaten bildiği bir tanesini seçer. Bu, OBEP-IBGW yolunu daha hızlı ve güvenilir hale getirir ve genel ağ bağlantılarını azaltır.

TUNNEL-DELIVERY için bu özellikleri uygulamak amacıyla kullanılabilecek bir adet kullanılmayan teslim türü (0x03) ve bayraklarda (flags) iki adet bit (0 ve 1) mevcuttur.


## Güvenlik Etkileri

Bu öneri, OBGW'nun hedef Destination'ı veya NetDB görünümü hakkında sızan bilgi miktarını değiştirmez:

- OBEP'yi kontrol eden ve NetDB'den LeaseSet'leri tarayan bir saldırgan, zaten bir mesajın belirli bir Destination'a gönderilip gönderildiğini, TunnelId / RouterIdentity çiftini arayarak belirleyebilir. En kötü durumda, TMDI'deki birden fazla Lease'in varlığı, saldırganın veritabanında eşleşme bulmasını biraz daha hızlı hale getirebilir.

- Kötü niyetli bir Destination işleten bir saldırgan, farklı floodfill'lere farklı gelen tüneller içeren LeaseSet'ler yayınlayarak ve OBGW'nun hangi tüneller üzerinden bağlandığını gözlemleyerek, bağlanan kurbanın NetDB görünümü hakkında zaten bilgi edinebilir. Onların bakış açısından, OBEP'nin hangi tüneli kullanacağına karar vermesi, OBGW'nun bu seçimi yapmasıyla işlevsel olarak aynıdır.

Çok noktaya yayın bayrağı (multicast flag), OBGW'nun çok noktaya yayın yaptığının OBEP'lere ifşa edilmesine neden olur. Bu, üst düzey protokoller uygulanırken dikkate alınması gereken bir performans-karmaşıklık-özel yaşam dengesi oluşturur. Bu bayrak isteğe bağlı olduğu için kullanıcılar uygulamaları için uygun kararı verebilir. Ancak, çeşitli uygulamalar tarafından yaygın olarak kullanılması, bir mesajın hangi özel uygulamadan geldiğine dair bilgi sızıntısını azaltacağı için, uyumlu uygulamalar için varsayılan davranış olarak bu özelliğin etkinleştirilmesinin faydaları olabilir.


## Spesifikasyon

İlk Parça Teslim Talimatları aşağıdaki şekilde değiştirilir:

```
+----+----+----+----+----+----+----+----+
  |flag|  Tunnel ID (opt)  |              |
  +----+----+----+----+----+              +
  |                                       |
  +                                       +
  |         To Hash (optional)            |
  +                                       +
  |                                       |
  +                        +----+----+----+
  |                        |dly | Message
  +----+----+----+----+----+----+----+----+
   ID (opt) |extended opts (opt)|cnt | (o)
  +----+----+----+----+----+----+----+----+
   Tunnel ID N   |                        |
  +----+----+----+                        +
  |                                       |
  +                                       +
  |         To Hash N (optional)          |
  +                                       +
  |                                       |
  +              +----+----+----+----+----+
  |              | Tunnel ID N+1 (o) |    |
  +----+----+----+----+----+----+----+    +
  |                                       |
  +                                       +
  |         To Hash N+1 (optional)        |
  +                                       +
  |                                       |
  +                                  +----+
  |                                  | sz
  +----+----+----+----+----+----+----+----+
       |
  +----+

flag ::
       1 byte
       Bit sırası: 76543210
       bit 6-5: teslim türü
                 0x03 = TUNNELS
       bit 0: çok noktaya yayın mı? 0 ise, tünellerden birine teslim et
                                      1 ise, tüm tünellere teslim et
                                      Eğer teslim türü TUNNELS değilse,
                                      gelecekteki kullanımlarla uyum için 0 olarak ayarlanır

Count ::
       1 byte
       İsteğe bağlı, teslim türü TUNNELS ise mevcuttur
       2-255 - Takip eden id/hash çiftlerinin sayısı

Tunnel ID :: TunnelId
To Hash ::
       Her biri 36 byte
       İsteğe bağlı, teslim türü TUNNELS ise mevcuttur
       id/hash çiftleri

Toplam uzunluk: Tipik uzunluk:
       75 byte, sayım 2 olan TUNNELS teslimi için (parçalanmamış tünel mesajı);
       79 byte, sayım 2 olan TUNNELS teslimi için (ilk parça)

Diğer teslim talimatları değişmeden kalır
```


## Uyumluluk

Yeni spesifikasyonu anlaması gereken tek eşler OBGW'ler ve OBEP'lerdir. Bu nedenle, kullanımını hedef I2P sürümüne bağlı kılarsak bu değişikliği mevcut ağ ile uyumlu hale getirebiliriz:

* OBGW'ler, giden tünelleri oluştururken, [RouterInfo](/docs/specs/common-structures/#routerinfo)'lerinde duyurulan I2P sürümüne göre uyumlu OBEP'leri seçmelidir.

* Hedef sürümü duyuran eşler, yeni bayrakları ayrıştırabilmeli ve talimatları geçersiz olarak reddetmemelidir.


## Referanslar

* [Destination](/docs/specs/common-structures/#destination)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [RouterIdentity](/docs/specs/common-structures/#routeridentity)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TUNNEL-DELIVERY](/docs/specs/common-structures/#tunnelmessagedeliveryinstructions)
* [TunnelId](/docs/specs/common-structures/#tunnelid)
* [VERSIONS](/docs/specs/i2np/#protocol-versions)
