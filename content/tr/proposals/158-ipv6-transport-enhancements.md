---
title: "IPv6 Taşıma İyileştirmeleri"
aliases:
  - "/tr/spec/proposals/158"
  - "/tr/spec/proposals/158/"
number: "158"
author: "zzz, orijinal"
created: "2021-03-19"
lastupdated: "2021-04-26"
status: "Kapalı"
thread: "http://zzz.i2p/topics/3060"
target: "0.9.50"
toc: true
---
## Not

Ağ dağıtımı ve testi devam etmektedir.  
Küçük revizyonlara tabidir.


## Genel Bakış

Bu öneri, IPv6 için SSU ve NTCP2 aktarımlarına iyileştirmeler uygulamaktır.


## Gerekçe

IPv6 dünya çapında yaygınlaştıkça ve özellikle mobil cihazlarda IPv6-only yapılandırmalar daha yaygın hale geldikçe,  
IPv6 desteği konusunda iyileştirmeler yapmamız ve tüm yönlendiricilerin IPv4'ü desteklediği varsayımını  
kaldırmamız gerekmektedir.



### Bağlantı Kontrolü

Tüneller için eş seçerken veya mesaj yönlendirmesi için OBEP/IBGW yolları seçerken,  
A yönlendiricisinin B yönlendiricisine bağlanıp bağlanamayacağını hesaplamak faydalıdır.  
Genel olarak, bu, A'nın B'nin duyurduğu gelen adreslerinden biriyle eşleşen bir aktarım ve adres türüne (IPv4/v6)  
dışa dönük yeteneğe sahip olup olmadığını belirlemek anlamına gelir.

Ancak birçok durumda A'nın yeteneklerini bilmiyoruz ve varsayımlar yapmak zorunda kalıyoruz.  
Eğer A gizli veya duvar arkasındaysa, adresler yayınlanmaz ve doğrudan bilgimiz olmaz —  
bu yüzden IPv4 desteklediğini, ancak IPv6 desteklemediğini varsayıyoruz.  
Çözüm, dışa dönük IPv4 ve IPv6 yeteneğini belirtmek için Yönlendirici Bilgisine (Router Info)  
iki yeni "cap" (özellik) eklemektir.


### IPv6 Tanıtıcılar

SSU spesifikasyonlarımız, IPv6 tanıtıcıların IPv4 tanıtımında desteklenip desteklenmediği konusunda  
hatalar ve tutarsızlıklar içermektedir.  
Her halükarda, bu özellik ne Java I2P'de ne de i2pd'de hiçbir zaman uygulanmıştır.  
Bu düzeltilemelidir.


### IPv6 Tanıtımlar

SSU spesifikasyonlarımız, IPv6 tanıtımlarının desteklenmediğini açıkça belirtmektedir.  
Bu, IPv6'nın asla duvar arkasına alınmayacağı varsayımına dayanmaktadır.  
Bu açıkça doğru değildir ve duvar arkasındaki IPv6 yönlendiriciler için desteği geliştirmemiz gerekmektedir.


### Tanıtım Diyagramları

Açıklama: ----- IPv4, ====== IPv6 anlamındadır

**Şu anki sadece IPv4:**

```
        Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**IPv4 tanıtımı, IPv6 tanıtıcı:**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**IPv6 tanıtımı, IPv6 tanıtıcı:**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```

**IPv6 tanıtımı, IPv4 tanıtıcı:**

```
Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```


## Tasarım

Uygulanacak üç değişiklik vardır.

- Yönlendirici Adresi özelliklerine, dışa dönük IPv4 ve IPv6 desteğini belirtmek için "4" ve "6" özelliklerini ekle
- IPv6 tanıtıcılar aracılığıyla IPv4 tanıtımı desteğini ekle
- IPv4 ve IPv6 tanıtıcılar aracılığıyla IPv6 tanıtımı desteğini ekle



## Spesifikasyon

### 4/6 Özellikleri

Bu özellik resmi bir öneri olmadan önce uygulanmıştı ancak IPv6 tanıtımları için gerekli olduğundan  
burada dahil edilmiştir.

İki yeni özellik "4" ve "6" tanımlanmıştır.  
Bu yeni özellikler, Yönlendirici Bilgisi (Router Info) caps'leri yerine, Yönlendirici Adresi (Router Address)  
"caps" özelliğine eklenecektir. Şu anda NTCP2 için bir "caps" özelliği tanımlanmamıştır.  
Şu anda bir tanıtıcı içeren SSU adresi, tanım gereği ipv4'tür. IPv6 tanıtımı desteklenmez.  
Ancak bu öneri IPv6 tanıtımlarıyla uyumludur. Aşağıya bakın.

Ek olarak, bir yönlendirici I2P-over-Yggdrasil gibi bir üst düzey ağ (overlay network) üzerinden  
bağlantı sağlayabilir ancak bir adres yayınlamak istemeyebilir veya bu adres standart bir IPv4 veya IPv6  
formatına sahip olmayabilir. Bu yeni özellik sistemi, bu tür ağları destekleyecek kadar esnek olmalıdır.

Aşağıdaki değişiklikleri tanımlıyoruz:

NTCP2: "caps" özelliğini ekle

SSU: Bir ana bilgisayar (host) veya tanıtıcı (introducer) olmayan Yönlendirici Adresi desteği ekleyerek  
IPv4, IPv6 veya her ikisi için dışa dönük desteği belirt.

Her iki aktarım için aşağıdaki caps değerlerini tanımla:

- "4": IPv4 desteği
- "6": IPv6 desteği

Tek bir adreste birden fazla değer desteklenebilir. Aşağıya bakın.  
Yönlendirici Adresi "host" değeri içermiyorsa, bu caps'lerden en az biri zorunludur.  
Yönlendirici Adresi bir "host" değeri içeriyorsa, bu caps'lerden en fazla biri isteğe bağlıdır.  
Gelecekte, üst düzey ağlar veya diğer bağlantı türlerini belirtmek için ek aktarım caps'leri tanımlanabilir.


#### Kullanım senaryoları ve örnekler

SSU:

Ana bilgisayarı olan SSU: 4/6 isteğe bağlıdır, asla ikisi birden olmaz.  
Örnek: SSU caps="4" host="1.2.3.4" key=... port="1234"

Sadece biri için dışa dönük SSU, diğeri yayınlanmıştır: Sadece caps, 4/6.  
Örnek: SSU caps="6"

Tanıtıcı içeren SSU: asla birleştirilmez. 4 veya 6 zorunludur.  
Örnek: SSU caps="4" iexp0=... ihost0=... iport0=... itag0=... key=...

Gizli SSU: Sadece caps, 4, 6 veya 46. Birden fazla izin verilir.  
4 ve 6 için ayrı iki adres gerek yoktur.  
Örnek: SSU caps="46"

NTCP2:

Ana bilgisayarı olan NTCP2: 4/6 isteğe bağlıdır, asla ikisi birden olmaz.  
Örnek: NTCP2 caps="4" host="1.2.3.4" i=... port="1234" s=... v="2"

Sadece biri için dışa dönük NTCP2, diğeri yayınlanmıştır: caps, s, v sadece, 4/6/y, birden fazla izin verilir.  
Örnek: NTCP2 caps="6" i=... s=... v="2"

Gizli NTCP2: caps, s, v sadece 4/6, birden fazla izin verilir. 4 ve 6 için ayrı iki adres gerek yoktur.  
Örnek: NTCP2 caps="46" i=... s=... v="2"



### IPv4 için IPv6 Tanıtıcılar

Spesifikasyonlardaki hataları ve tutarsızlıkları düzeltmek için aşağıdaki değişiklikler gereklidir.  
Bunu ayrıca önerinin "1. kısmı" olarak da tanımladık.

#### Spesifikasyon Değişiklikleri

SSU spesifikasyonu şu anda şunu belirtmektedir (IPv6 notları):

IPv6, 0.9.8 sürümünden itibaren desteklenmektedir. Yayınlanan aktarıcı adresleri IPv4 veya IPv6 olabilir ve Alice-Bob iletişimi IPv4 veya IPv6 üzerinden olabilir.

Aşağıdakini ekle:

Spesifikasyon 0.9.8 sürümünden itibaren değiştirilse de, Alice-Bob iletişimi için IPv6 desteği aslında 0.9.50 sürümüne kadar desteklenmedi.  
Java yönlendiricilerinin önceki sürümleri, IPv6 adresleri için 'C' özelliğini yanlışlıkla yayınladılar,  
gerçekte IPv6 üzerinden tanıtıcı olarak davranmadıkları halde.  
Bu nedenle yönlendiriciler, yönlendirici sürümü 0.9.50 veya üzeri değilse, bir IPv6 adresindeki 'C' özelliğine güvenmemelidir.



SSU spesifikasyonu şu anda şunu belirtmektedir (Aktarıcı İsteği):

IP adresi, paketin kaynak adresi ve portundan farklıysa eklenir.  
Mevcut uygulamada, IP uzunluğu her zaman 0 ve port her zaman 0'dır,  
ve alıcı paketin kaynak adresini ve portunu kullanmalıdır.  
Bu mesaj IPv4 veya IPv6 üzerinden gönderilebilir. IPv6 kullanılıyorsa, Alice IPv4 adresini ve portunu eklemelidir.

Aşağıdakini ekle:

Bu mesaj IPv6 üzerinden gönderildiğinde IPv4 adresini tanıtmak için IP ve port eklenmelidir.  
Bu, 0.9.50 sürümünden itibaren desteklenmektedir.



### IPv6 Tanıtımlar

SSU aktarıcı mesajlarının üçü (RelayRequest, RelayResponse ve RelayIntro)  
(Alice, Bob veya Charlie) IP adresinin uzunluğunu belirtmek için IP uzunluğu alanlarını içerir.

Bu nedenle mesaj formatında herhangi bir değişiklik gerekmez.  
Sadece 16 baytlık IP adreslerine izin verildiğini belirten metinsel değişiklikler gereklidir.

Spesifikasyonlara aşağıdaki değişiklikler gereklidir.  
Bunu ayrıca önerinin "2. kısmı" olarak da tanımladık.


#### Spesifikasyon Değişiklikleri

SSU spesifikasyonu şu anda şunu belirtmektedir (IPv6 notları):

Bob-Charlie ve Alice-Charlie iletişimi sadece IPv4 üzerinden olur.

SSU spesifikasyonu şu anda şunu belirtmektedir (Aktarıcı İsteği):

IPv6 için aktarım uygulamak için herhangi bir plan yoktur.

Şöyle değiştir:

IPv6 için aktarım 0.9.xx sürümünden itibaren desteklenmektedir.

SSU spesifikasyonu şu anda şunu belirtmektedir (Aktarıcı Yanıtı):

Charlie'nin IP adresi IPv4 olmalıdır çünkü Alice, Delik Açmadan (Hole Punch) sonra Charlie'ye SessionRequest gönderir.  
IPv6 için aktarım uygulamak için herhangi bir plan yoktur.

Şöyle değiştir:

Charlie'nin IP adresi IPv4 olabilir veya 0.9.xx sürümünden itibaren IPv6 olabilir.  
Bu, Alice'in Delik Açmadan sonra Charlie'ye SessionRequest göndereceği adrestir.  
IPv6 için aktarım 0.9.xx sürümünden itibaren desteklenmektedir.

SSU spesifikasyonu şu anda şunu belirtmektedir (Aktarıcı Tanıtımı):

Mevcut uygulamada Alice'in IP adresi her zaman 4 bayttır çünkü Alice Charlie'ye IPv4 üzerinden bağlanmaya çalışır.  
Bu mesaj, Bob'un Charlie'nin IPv4 adresini RelayResponse'te Alice'e döndürebilmesi için yalnızca kurulmuş bir IPv4 bağlantısı üzerinden gönderilmelidir.

Şöyle değiştir:

IPv4 için, Alice'in IP adresi her zaman 4 bayttır çünkü Alice Charlie'ye IPv4 üzerinden bağlanmaya çalışır.  
0.9.xx sürümünden itibaren IPv6 desteklenir ve Alice'in IP adresi 16 bayt olabilir.

IPv4 için, bu mesaj kurulmuş bir IPv4 bağlantısı üzerinden gönderilmelidir,  
çünkü bu, Bob'un Charlie'nin IPv4 adresini RelayResponse'te Alice'e döndürebilmesi için tek yoldur.  
0.9.xx sürümünden itibaren IPv6 desteklenir ve bu mesaj kurulmuş bir IPv6 bağlantısı üzerinden gönderilebilir.

Ayrıca şunu ekle:

0.9.xx sürümünden itibaren, tanıtıcılarla yayınlanan herhangi bir SSU adresi "caps" seçeneğinde "4" veya "6" içermelidir.


## Geçiş

Eski tüm yönlendiriciler NTCP2'deki caps özelliğini ve SSU caps özelliğindeki bilinmeyen özellik karakterlerini yoksaymalıdır.

"4" veya "6" cap içermeyen herhangi bir SSU adresi, IPv4 tanıtımı için olduğu varsayılır.


## Kaynaklar

* [CAPS](http://zzz.i2p/topics/3050)
* [NTCP2](/docs/specs/ntcp2/)
* [SSU](/docs/specs/ssu2/)
* [SSU-SPEC](/docs/legacy/ssu/)
