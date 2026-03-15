---
title: "Görünmez Çoklu Barındırma"
number: "140"
author: "str4d"
created: "2017-05-22"
lastupdated: "2017-07-04"
status: "Aç"
thread: "http://zzz.i2p/topics/2335"
toc: true
---
## Genel Bakış

Bu öneri, tek bir [Destination](/docs/specs/common-structures/#destination)’ı şeffaf bir şekilde barındıran birden fazla yönlendiriciyi yönetmek için bir I2P istemcisi, servisi veya harici bir dengeleyici sürecini mümkün kılan bir protokol tasarımı sunar.

Şu anki öneri, somut bir uygulamayı belirtmemektedir. [I2CP](/docs/specs/i2cp/)’ye bir uzantı olarak ya da yeni bir protokol olarak uygulanabilir.


## Motivasyon

Çoklu ev sahipliği (multihoming), aynı Destination’ı barındırmak için birden fazla yönlendiricinin kullanıldığı durumdur. I2P ile çoklu ev sahipliği yapmanın mevcut yolu, her yönlendiricide bağımsız olarak aynı Destination’ı çalıştırmaktır; istemciler tarafından belirli bir zamanda kullanılan yönlendirici, LeaseSet’i en son yayınlayan yönlendiricidir.

Bu bir geçici çözümdür ve büyük siteler için ölçeklenebilir bir şekilde çalışmayacağı varsayılır. Diyelim ki 100 yönlendiricimiz var ve her birinin 16 tüneli var. Bu, her 10 dakikada 1600 LeaseSet yayınlaması anlamına gelir, yani saniyede neredeyse 3 yayın. Floodfill'ler aşırı yüklenecek ve sınırlamalar devreye girecektir. Ve bu, arama trafiğinden bile bahsetmeden.

Öneri 123, 100 gerçek LeaseSet hash'ini listeleyen bir meta-LeaseSet ile bu sorunu çözer. Bir arama iki aşamalı bir işlem haline gelir: önce meta-LeaseSet aranır, sonra adlandırılmış LeaseSet'lerden biri. Bu, arama trafiği sorununa iyi bir çözümdür, ancak tek başına önemli bir gizlilik sızıntısı yaratır: Her gerçek LeaseSet tek bir yönlendiriciye karşılık geldiği için, yayınlanan meta-LeaseSet izlenerek hangi çoklu ev sahibi yönlendiricilerin çevrimiçi olduğu belirlenebilir.

I2P istemcisi veya servisinin, LeaseSet açısından tek bir yönlendirici kullanmakla ayırt edilemeyecek şekilde, tek bir Destination’ı birden fazla yönlendiriciye yayabilmesi için bir yol gereklidir.


## Tasarım

### Tanımlar

    Kullanıcı
        Destination'larını çoklu ev sahipliği yapmak isteyen kişi veya kuruluş. Genelliği kaybetmeden (WLOG) burada tek bir Destination ele alınır.

    İstemci
        Destination'ın arkasında çalışan uygulama veya servis. İstemci tarafında, sunucu tarafında veya eşten eşe uygulama olabilir; ona, I2P yönlendiricilerine bağlandığı anlamında bir istemci olarak atıfta bulunuruz.

        İstemci üç bölümden oluşur ve bu bölümler tek bir süreçte olabilir veya birden fazla süreç ya da makineye (çoklu istemci kurulumunda) dağılmış olabilir:

        Dengeleyici (Balancer)
            Eş seçimi ve tünel oluşturma işlemlerini yöneten istemcinin bölümü. Aynı anda tek bir dengeleyici vardır ve tüm I2P yönlendiricileriyle iletişim kurar. Yedek dengeleyiciler olabilir.

        Ön uç (Frontend)
            Paralel olarak çalıştırılabilen istemcinin bölümü. Her ön uç tek bir I2P yönlendiricisiyle iletişim kurar.

        Arka uç (Backend)
            Tüm ön uçlar arasında paylaşılan istemcinin bölümü. Herhangi bir I2P yönlendiricisiyle doğrudan iletişim kurmaz.

    Yönlendirici (Router)
        Kullanıcının I2P ağı ile kendi ağı arasındaki sınırda (kurumsal ağlardaki edge cihazına benzer şekilde) yer alan ve kullanıcı tarafından çalıştırılan bir I2P yönlendiricisidir. Bir dengeleyicinin komutuyla tüneller oluşturur ve bir istemci veya ön uca ait paketleri yönlendirir.

### Genel bakış

Aşağıdaki istenen yapılandırmayı hayal edin:

- Tek bir Destination'a sahip bir istemci uygulaması.
- Her biri üçer adet gelen tünel yöneten dört yönlendirici.
- On iki tünelin tamamı tek bir LeaseSet içinde yayınlanmalıdır.

### Tek istemci

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]-----
                 |-{ [Tunnel 3]===/               \
                 |                                 \
                 |-{ [Tunnel 4]===\                 \
  [Destination]  |-{ [Tunnel 5]====[Router 2]-----   \
    \            |-{ [Tunnel 6]===/               \   \
     [LeaseSet]--|                               [Client]
                 |-{ [Tunnel 7]===\               /   /
                 |-{ [Tunnel 8]====[Router 3]-----   /
                 |-{ [Tunnel 9]===/                 /
                 |                                 /
                 |-{ [Tunnel 10]==\               /
                 |-{ [Tunnel 11]===[Router 4]-----
                  -{ [Tunnel 12]==/
```

### Çoklu istemci

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]---------[Frontend 1]
                 |-{ [Tunnel 3]===/          \                    \
                 |                            \                    \
                 |-{ [Tunnel 4]===\            \                    \
  [Destination]  |-{ [Tunnel 5]====[Router 2]---\-----[Frontend 2]   \
    \            |-{ [Tunnel 6]===/          \   \                \   \
     [LeaseSet]--|                         [Balancer]            [Backend]
                 |-{ [Tunnel 7]===\          /   /                /   /
                 |-{ [Tunnel 8]====[Router 3]---/-----[Frontend 3]   /
                 |-{ [Tunnel 9]===/            /                    /
                 |                            /                    /
                 |-{ [Tunnel 10]==\          /                    /
                 |-{ [Tunnel 11]===[Router 4]---------[Frontend 4]
                  -{ [Tunnel 12]==/
```

### Genel istemci süreci

- Bir Destination yükleyin veya oluşturun.

- Her yönlendiriciyle, bu Destination'a bağlı bir oturum açın.

- Periyodik olarak (yaklaşık on dakikada bir, ancak tünel canlılığına göre daha fazla veya az olabilir):

  - Her yönlendiriciden hızlı katmanı (fast tier) alın.

  - Tünel oluşturmak için bu yönlendiricilerden gelen eşlerin süper kümesini kullanın.

    - Varsayılan olarak, belirli bir yönlendiriciye giden/gelen tüneller o yönlendiricinin hızlı katmanındaki eşleri kullanır, ancak bu protokol tarafından zorunlu tutulmaz.

  - Tüm aktif yönlendiricilerden gelen aktif gelen tünelleri toplayın ve bir LeaseSet oluşturun.

  - LeaseSet’i bir veya daha fazla yönlendirici aracılığıyla yayınlayın.

### I2CP’den farklar

Bu yapılandırmayı oluşturmak ve yönetmek için istemcinin [I2CP](/docs/specs/i2cp/)’de şu anda sağlananların ötesinde aşağıdaki yeni işlevlere ihtiyacı vardır:

- LeaseSet oluşturmadan bir yönlendiriciye tüneller oluşturmasını söylemek.
- Gelen havuzundaki mevcut tünellerin listesini almak.

Ayrıca, istemcinin tünellerini nasıl yönettiğine dair önemli esneklik sağlayacak aşağıdaki işlevsellikler de gereklidir:

- Yönlendiricinin hızlı katmanının içeriğini almak.
- Belirli bir eş listesini kullanarak bir yönlendiriciye gelen veya giden bir tünel oluşturmasını söylemek.

### Protokol taslağı

```
         Client                           Router

                    --------------------->  Create Session
   Session Status  <---------------------
                    --------------------->  Get Fast Tier
        Peer List  <---------------------
                    --------------------->  Create Tunnel
    Tunnel Status  <---------------------
                    --------------------->  Get Tunnel Pool
      Tunnel List  <---------------------
                    --------------------->  Publish LeaseSet
                    --------------------->  Send Packet
      Send Status  <---------------------
  Packet Received  <---------------------
```

### Mesajlar

**Create Session**
- Belirtilen Destination için bir oturum oluşturur.

**Session Status**
- Oturumun başarıyla kurulduğunu onaylar ve istemcinin artık tünel oluşturmaya başlayabileceğini belirtir.

**Get Fast Tier**
- Yönlendiricinin şu anda tünel oluşturmak için düşündüğü eşlerin listesini ister.

**Peer List**
- Yönlendirici tarafından bilinen eşlerin listesi.

**Create Tunnel**
- Yönlendiriciden, belirtilen eşler aracılığıyla yeni bir tünel oluşturmasını ister.

**Tunnel Status**
- Belirli bir tünel oluşturma işleminin sonucu, sonuç mevcut olduğunda gönderilir.

**Get Tunnel Pool**
- Destination için gelen veya giden havuzdaki mevcut tünellerin listesini ister.

**Tunnel List**
- İstenen havuz için tünel listesi.

**Publish LeaseSet**
- Yönlendiriciden, verilen LeaseSet’i Destination için giden tünellerden biri aracılığıyla yayınlamasını ister. Yanıt durumu gerekmez; yönlendirici LeaseSet’in yayınlandığından emin olana kadar yeniden denemeye devam etmelidir.

**Send Packet**
- İstemciden gelen bir çıkış paketi. İsteğe bağlı olarak paketin hangi giden tünel üzerinden gönderilmesi gerektiğini belirtir (zorunlu mu olmalı?).

**Send Status**
- Paketin gönderilmesinin başarılı olup olmadığını istemciye bildirir.

**Packet Received**
- İstemci için gelen bir paket. İsteğe bağlı olarak paketin hangi gelen tünel üzerinden alındığını belirtir(?)


## Güvenlik etkileri

Yönlendiriciler açısından bu tasarım, mevcut durumla işlevsel olarak eşdeğerdir. Yönlendirici hâlâ tüm tünelleri oluşturur, kendi eş profillerini korur ve yönlendirici ile istemci işlemleri arasında ayrımı sağlar. Varsayılan yapılandırmada tamamen aynıdır çünkü bu yönlendirici için tüneller kendi hızlı katmanından oluşturulur.

netDB açısından, bu protokol aracılığıyla oluşturulan tek bir LeaseSet, önceden var olan işlevselliği kullandığı için mevcut durumla aynıdır. Ancak, 16 Lease’e yaklaşan daha büyük LeaseSet’ler için, bir gözlemcinin LeaseSet’in çoklu ev sahipliği yapıldığını belirlemesi mümkün olabilir:

- Hızlı katmanın mevcut maksimum boyutu 75 eşten oluşur. Gelen ağ geçidi (IBGW, Lease’te yayınlanan düğüm), katmanın bir alt kümesinden seçilir (tünellerin havuzuna göre rastgele hash ile bölünür, sayıya göre değil):

      1 hop
          Tüm hızlı katman

      2 hops
          Hızlı katmanın yarısı
          (2014 ortasına kadar varsayılan)

      3+ hops
          Hızlı katmanın dörtte biri
          (3, mevcut varsayılan)

  Bu, ortalama olarak IBGW'lerin 20-30 eşten oluşan bir kümeden geleceği anlamına gelir.

- Tek ev sahipli bir yapılandırmada, tam 16 tünel içeren bir LeaseSet, en fazla (örneğin) 20 eşten oluşan bir kümeden rastgele seçilen 16 IBGW'ye sahip olur.

- Varsayılan yapılandırmayı kullanan 4 yönlendiricili çoklu ev sahipli bir yapılandırmada, tam 16 tünel içeren bir LeaseSet, en fazla 80 eşten oluşan bir kümeden rastgele seçilen 16 IBGW'ye sahip olur, ancak yönlendiriciler arasında ortak eşlerin bir kısmı muhtemeldir.

Bu nedenle varsayılan yapılandırmada, istatistiksel analiz ile bir LeaseSet’in bu protokol tarafından oluşturulduğu belirlenebilir. Ayrıca kaç yönlendirici olduğu da belirlenebilir, ancak hızlı katmanlardaki değişimin (churn) bu analizin etkinliğini azaltacağı muhtemeldir.

İstemci seçtiği eşlere tam kontrol sahibi olduğu için, IBGW'leri daraltılmış bir eş kümesinden seçerek bu bilgi sızıntısını azaltmak veya ortadan kaldırmak mümkündür.


## Uyumluluk

Bu tasarım, LeaseSet formatında herhangi bir değişiklik olmadığı için ağla tamamen geriye dönük uyumludur. Tüm yönlendiricilerin yeni protokolden haberdar olması gerekir, ancak hepsi aynı varlık tarafından kontrol edildiği için bu bir sorun değildir.


## Performans ve ölçeklenebilirlik notları

Bu öneri, LeaseSet başına 16 Lease üst sınırını değiştirmez. Daha fazla tünel gerektiren Destination’lar için iki olası ağ değişikliği vardır:

- LeaseSet boyutunun üst sınırını artırmak. Bu, uygulanması en kolay olan yöntemdir (ancak yaygın olarak kullanılmadan önce hâlâ yaygın ağ desteği gerektirir), ancak daha büyük paket boyutları nedeniyle aramaların yavaşlamasına neden olabilir. Maksimum uygulanabilir LeaseSet boyutu, altta yatan taşıma katmanlarının MTU'suyla belirlenir ve bu nedenle yaklaşık 16kB civarındadır.

- Katmanlı LeaseSet’ler için Öneri 123’ü uygulamak. Bu öneriyle birlikte, alt-LeaseSet’lerin Destination’ları birden fazla yönlendiriciye yayılabilir ve etkili bir şekilde clearnet servisleri için birden fazla IP adresi gibi davranabilir.


## Teşekkürler

Bu öneriye yol açan tartışmalar için psi'ye teşekkürler.


## Referanslar

* [Destination](/docs/specs/common-structures/#destination)
* [I2CP](/docs/specs/i2cp/)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [Prop123](/proposals/123-new-netdb-entries/)
