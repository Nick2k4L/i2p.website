---
title: "LS2'de Servis Kayıtları"
number: "167"
author: "zzz, orjinal, eyedeekay"
created: "2024-06-22"
lastupdated: "2025-04-03"
status: "Kapalı"
thread: "http://zzz.i2p/topics/3641"
target: "0.9.66"
toc: true
---
## Durum
2. incelemede 2025-04-01 tarihinde onaylandı; teknik özellikler güncellendi; henüz uygulanmadı.


## Genel Bakış

I2P'nin merkezi bir DNS sistemi yoktur.
Ancak adres defteri ve b32 ana makine adı sistemi sayesinde,
yönlendirici tam hedefleri arayabilir ve kiralamaları (lease set) alabilir; bu kiralama setleri,
istemcilerin bu hedefe bağlanabilmesi için bir ağ geçidi ve anahtar listesi içerir.

Dolayısıyla kiralama setleri bir nevi DNS kaydı gibidir. Ancak şu anda, bir ana makinenin
o hedefte veya başka birinde herhangi bir hizmeti destekleyip desteklemediğini,
[RFC 2782](https://datatracker.ietf.org/doc/html/rfc2782)'de tanımlandığı gibi DNS [SRV kayıtlarına](https://en.wikipedia.org/wiki/SRV_record) benzer şekilde
belirleyebilmek için herhangi bir olanak mevcut değildir.

Bunun ilk uygulaması eşten eşe e-posta olabilir.
Diğer olası uygulamalar: DNS, GNS, anahtar sunucuları, sertifika yetkilileri, saat sunucuları,
bittorrent, kripto paralar, diğer eşten eşe uygulamalar.


## İlgili Öneriler ve Alternatifler

### Hizmet Listeleri

LS2 [Öneri 123](/proposals/123-new-netdb-entries/) bir hedefin küresel bir hizmete katıldığını belirten 'hizmet kayıtlarını' tanımladı.
Floodfill'ler bu kayıtları küresel 'hizmet listeleri'ne topluyordu.
Karmaşıklık, kimlik doğrulama eksikliği, güvenlik ve spamlama endişeleri nedeniyle bu asla uygulanmadı.

Bu öneri, bazı küresel hizmet için küresel bir hedef havuzu sağlamaktan ziyade,
belirli bir hedef için bir hizmet araması sağlaması açısından farklıdır.

### GNS

GNS, herkesin kendi DNS sunucusunu çalıştırmasını önerir.
Bu öneri tamamlayıcıdır; GNS (veya DNS) hizmetinin desteklendiğini belirtmek için hizmet kayıtlarını kullanabiliriz,
standart hizmet adı "domain" ve port 53 olabilir.

### Dot well-known

[Önerildiği gibi](http://i2pforum.i2p/viewtopic.php?p=3102), hizmetlerin
/.well-known/i2pmail.key adresine yapılan bir HTTP isteği ile aranması önerildi.
Bu, her hizmetin anahtarını barındırmak için ilgili bir web sitesi çalıştırmasını gerektirir.
Çoğu kullanıcı web sitesi çalıştırmaz.

Bir çözüm, bir b32 adresi için bir hizmetin aslında o b32 adresinde çalıştığını varsaymaktır.
Yani example.i2p için hizmet aramak, http://example.i2p/.well-known/i2pmail.key adresinden
HTTP alımını gerektirir; ancak aaa...aaa.b32.i2p için bir hizmet aramak bu aramayı gerektirmez,
doğrudan bağlanılabilir.

Ancak burada bir belirsizlik vardır çünkü example.i2p aynı zamanda b32 adresiyle de adreslenebilir.

### MX Kayıtları

SRV kayıtları herhangi bir hizmet için MX kayıtlarının genel bir versiyonudur.
"_smtp._tcp", "MX" kaydıdır.
SRV kayıtlarımız varsa MX kayıtlarına gerek yoktur ve MX kayıtları
tek başına herhangi bir hizmet için genel bir kayıt sağlamaz.


## Tasarım

Hizmet kayıtları [LS2](/docs/specs/common-structures/) içindeki seçenekler bölümüne yerleştirilir.
LS2 seçenekler bölümü şu anda kullanılmamaktadır.
LS1 için desteklenmez.
Bu, tünel oluşturma kayıtları için seçenekler tanımlayan [tünelden bant genişliği önerisi](/proposals/168-tunnel-bandwidth/) ile benzerdir.

Belirli bir ana makine adı veya b32 için bir hizmet adresi aramak üzere yönlendirici
kiralama setini alır ve özellikleri içinde hizmet kaydını arar.

Hizmet, LS'nin kendisiyle aynı hedefte barındırılabilir veya farklı bir ana makine adı/b32'yi gösterebilir.

Hizmetin hedef hedefi farklıysa, hedef LS'nin de kendisine işaret eden ve hizmeti desteklediğini belirten
bir hizmet kaydını içermesi gerekir.

Tasarım, floodfill'lerde özel destek, önbellekleme veya herhangi bir değişiklik gerektirmez.
Yalnızca kiralama setini yayınlayan ve hizmet kaydı arayan istemci bu değişiklikleri desteklemelidir.

İstemcilerin hizmet kayıtlarını almasını kolaylaştırmak için küçük I2CP ve SAM uzantıları önerilir.



## Özellikler

### LS2 Seçenek Özellikleri

LS2 seçenekleri imza değişken olmaması için anahtara göre sıralanmalıdır.

Aşağıdaki şekilde tanımlanır:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := İstenen hizmetin sembolik adı. Küçük harf olmalıdır. Örnek: "smtp".
  İzin verilen karakterler [a-z0-9-] olup '-' ile başlamamalı veya bitmemelidir.
  [DNS-SD Hizmet Türleri kayıt defteri](http://www.dns-sd.org/ServiceTypes.html) veya Linux /etc/services içinde tanımlanmışsa standart tanımlayıcılar kullanılmalıdır.
- proto := İstenen hizmetin taşıma protokolü. Küçük harf olmalı, "tcp" veya "udp" olmalıdır.
  "tcp", akışlı; "udp", yanıt verilebilir veri birimlerini ifade eder.
  Ham veri birimleri ve datagram2 için protokol göstergeleri ileride tanımlanabilir.
  İzin verilen karakterler [a-z0-9-] olup '-' ile başlamamalı veya bitmemelidir.
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := yaşam süresi, saniye cinsinden tamsayı. Pozitif tamsayı. Örnek: "86400".
  Aşağıdaki Öneriler bölümünde ayrıntılar verildiği gibi en az 86400 (bir gün) önerilir.
- priority := Hedef ana makinenin önceliği, daha düşük değer daha çok tercih edilir. Negatif olmayan tamsayı. Örnek: "0"
  Birden fazla kayıt varsa yararlıdır ancak tek kayıt varsa bile gereklidir.
- weight := Aynı önceliğe sahip kayıtlar için göreli ağırlık. Daha yüksek değer seçilme olasılığını artırır. Negatif olmayan tamsayı. Örnek: "0"
  Birden fazla kayıt varsa yararlıdır ancak tek kayıt varsa bile gereklidir.
- port := Hizmetin bulunduğu I2CP portu. Negatif olmayan tamsayı. Örnek: "25"
  Port 0 desteklenir ancak önerilmez.
- target := Hizmeti sağlayan hedefin ana makine adı veya b32'si. Geçerli bir [hostname](/docs/overview/naming/). Küçük harf olmalıdır.
  Örnek: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" veya "example.i2p".
  Ana makine adı "iyi bilinen" değilse (yani resmi veya varsayılan adres defterlerinde değilse) b32 önerilir.
- appoptions := Uygulamaya özgü rastgele metin, " " veya "," içermemelidir. Kodlama UTF-8'dir.

### Örnekler

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p için LS2'de bir SMTP sunucusuna işaret eder:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p için LS2'de iki SMTP sunucusuna işaret eder:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p için LS2'de kendisini bir SMTP sunucusu olarak gösterir:

    "_smtp._tcp" "0 999999 25"

E-postayı yönlendirmek için olası biçim (aşağıya bakın):

    "_smtp._tcp" "1 86400 0 0 25 smtp.postman.i2p example@mail.i2p"


### Sınırlar

LS2 seçenekleri için kullanılan Eşleme veri yapısı formatı anahtarları ve değerleri en fazla 255 bayt (karakter değil) ile sınırlar.
b32 hedef ile optionvalue yaklaşık 67 bayt olur, bu yüzden sadece 3 kayıt sığar.
Uzun bir appoptions alanı ile sadece bir veya iki, kısa bir ana makine adı ile dört veya beş kayıt sığabilir.
Bu yeterli olmalıdır; birden fazla kayıt nadir olmalıdır.


### RFC 2782'den Farklar

- Sonunda nokta yok
- Proto'dan sonra isim yok
- Küçük harf zorunlu
- İkili DNS formatı yerine virgülle ayrılmış metin formatında
- Farklı kayıt türü göstergeleri
- Ek appoptions alanı


### Notlar

(asterisk), (asterisk)._tcp veya _tcp gibi joker karakterlere izin verilmez.
Desteklenen her hizmetin kendi kaydına sahip olması gerekir.



### Hizmet Adı Kayıt Defteri

[DNS-SD Hizmet Türleri kayıt defteri](http://www.dns-sd.org/ServiceTypes.html) veya Linux /etc/services içinde listelenmeyen
standart olmayan tanımlayıcılar istenebilir ve [ortak yapılar spesifikasyonuna](/docs/specs/common-structures/) eklenebilir.

Hizmete özel appoptions biçimleri de oraya eklenebilir.


### I2CP Özellikleri

[I2CP protokolü](/docs/specs/i2cp/) hizmet aramalarını desteklemek için genişletilmelidir.
Hizmet aramasıyla ilgili ek MessageStatusMessage ve/veya HostReplyMessage hata kodları gereklidir.
Arama özelliğini yalnızca hizmet kaydı özel değil genel yapmak için,
tasarım tüm LS2 seçeneklerinin alınmasını desteklemeyi amaçlar.

Uygulama: HostLookupMessage'i, hash, ana makine adı ve hedef için LS2 seçenekleri isteği eklemek üzere genişletin (istek türleri 2-4).
İstenirse HostReplyMessage'i seçenekler eşlemesini eklemek üzere genişletin.
Hizmet aramasıyla ilgili ek hata kodlarıyla HostReplyMessage'i genişletin.

Eşleme seçenekleri istemci veya yönlendirici tarafında kısa bir süre önbelleğe alınabilir veya negatif önbelleğe alınabilir,
uygulamaya bağlıdır. Hizmet kaydı TTL'si daha kısa değilse önerilen maksimum süre bir saattir.
Hizmet kayıtları uygulama, istemci veya yönlendirici tarafından belirtilen TTL'ye kadar önbelleğe alınabilir.

Aşağıdaki şekilde spesifikasyonu genişletin:

#### Yapılandırma seçenekleri

[I2CP yapılandırma seçeneklerine](/docs/specs/i2cp/) aşağıdakileri ekleyin

i2cp.leaseSetOption.nnn

Kiralama setine konulacak seçenekler. Yalnızca LS2 için kullanılabilir.
nnn 0 ile başlar. Seçenek değeri "key=value" içerir.
(tırnakları dahil etmeyin)

Örnek:
i2cp.leaseSetOption.0=_smtp._tcp=1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p


#### HostLookup Mesajı

- Arama türü 2: Hash araması, seçenekler eşlemesi isteği
- Arama türü 3: Ana makine adı araması, seçenekler eşlemesi isteği
- Arama türü 4: Hedef araması, seçenekler eşlemesi isteği

4. arama türü için, 5. öğe bir Hedeftir (Destination).



#### HostReply Mesajı

2-4 arama türleri için yönlendirici, arama anahtarı adres defterinde olsa bile kiralama setini almalıdır.

Başarılı olursa, HostReply kiralama setinden gelen seçenekler Eşlemesini içerecek
ve hedeften sonra 5. öğe olarak dahil edilecektir. Eşlemede hiçbir seçenek yoksa veya kiralama seti sürüm 1'seydi,
yine de boş bir Eşleme olarak dahil edilecektir (iki bayt: 0 0).
Tüm kiralama seti seçenekleri dahil edilecektir, yalnızca hizmet kaydı seçenekleri değil.
Örneğin gelecekte tanımlanacak parametreler için seçenekler mevcut olabilir.

Kiralama seti araması başarısız olursa, yanıt yeni hata kodu 6'yı (Kiralama seti araması başarısız) içerecek
ve bir eşleme içermeyecektir.
Hata kodu 6 döndürüldüğünde, Hedef alanı mevcut olabilir veya olmayabilir.
Adres defterinde bir ana makine adı araması başarılı olursa,
veya önceki bir arama başarılı olup sonuç önbelleğe alınmışsa,
veya Hedef arama mesajında mevcutsa (arama türü 4) mevcut olacaktır.

Bir arama türü desteklenmiyorsa,
yanıt yeni hata kodu 7'yi (desteklenmeyen arama türü) içerecektir.



### SAM Özellikleri

[SAMv3 protokolü](/docs/api/samv3/) hizmet aramalarını desteklemek için genişletilmelidir.

NAMING LOOKUP'u aşağıdaki şekilde genişletin:

NAMING LOOKUP NAME=example.i2p OPTIONS=true, yanıtta seçenekler eşlemesini ister.

NAME, OPTIONS=true olduğunda tam bir base64 hedef olabilir.

Hedef araması başarılı olur ve kiralama setinde seçenekler mevcutsa,
yanıtta hedeften sonra bir veya daha fazla seçenek
OPTION:key=value biçiminde yer alır.
Her seçenek ayrı bir OPTION: öneki alır.
Tüm kiralama seti seçenekleri dahil edilir, yalnızca hizmet kaydı seçenekleri değil.
Örneğin gelecekte tanımlanacak parametreler için seçenekler mevcut olabilir.
Örnek:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

'=' içeren anahtarlar ve satır sonu içeren anahtarlar veya değerler
geçersiz kabul edilir ve anahtar/değer çifti yanıttan kaldırılır.

Kiralama setinde hiçbir seçenek bulunamazsa veya kiralama seti sürüm 1'seyse,
yanıt hiçbir seçeneği içermeyecektir.

Eğer aramada OPTIONS=true varsa ve kiralama seti bulunamazsa, yeni bir sonuç değeri LEASESET_NOT_FOUND döndürülecektir.


## Adlandırma Arama Alternatifi

Gelecekte tanımlanabilecek diğer LS2 seçeneklerini almak için kullanılabilecek genel bir olanak olmayacağından,
iki nedenle reddedildi:

- I2CP ve SAM değişiklikleri, TTL ve port bilgilerini istemciye iletmek için yine de gerekli olacaktır.
- Gelecekte tanımlanabilecek diğer LS2 seçeneklerini almak için kullanılabilecek genel bir olanak olmayacaktır.


## Öneriler

Sunucular, uygulama için en az 86400 TTL ve standart portu belirtmelidir.



## Gelişmiş Özellikler

### Yinelemeli Aramalar

Her bir sonraki kiralama setinin başka bir kiralama setine işaret eden bir hizmet kaydı olup olmadığını kontrol eden,
DNS tarzı yinelemeli aramaları desteklemek istenebilir.
Bu muhtemelen gerekli değildir, en azından ilk uygulamada.

TODO



### Uygulamaya Özel Alanlar

Hizmet kaydında uygulamaya özel verilerin olması istenebilir.
Örneğin, example.i2p operatörü e-postanın example@mail.i2p'ye iletilmesini isteyebilir.
"example@" kısmı hizmet kaydının ayrı bir alanına konulmalı veya hedeften çıkarılmalıdır.

Operatör kendi e-posta hizmetini çalıştırıyor olsa bile, e-postanın example@example.i2p'ye gönderilmesi gerektiğini belirtmek isteyebilir.
Çoğu I2P hizmeti tek bir kişi tarafından çalıştırılır.
Bu yüzden burada da ayrı bir alan faydalı olabilir.

TODO bunu genel bir şekilde nasıl yapacağımız


### E-posta için Gerekli Değişiklikler

Bu önerinin kapsamı dışında. Ayrıntılar için [i2pforum'daki tartışmaya](http://i2pforum.i2p/viewtopic.php?p=3102) bakın.


## Uygulama Notları

Hizmet kayıtlarının TTL'ye kadar önbelleğe alınması yönlendirici veya uygulama tarafından yapılabilir,
uygulamaya bağlıdır. Kalıcı olarak önbelleğe alınıp alınmayacağı da uygulamaya bağlıdır.

Aramalar ayrıca hedef kiralama setini aramalı ve hedef hedefi istemciye döndürmeden önce
kendisine işaret eden bir "self" kaydı içerdiğini doğrulamalıdır.


## Güvenlik Analizi

Kiralama seti imzalandığından, içindeki hizmet kayıtları hedefin imzalama anahtarıyla kimlik doğrulaması yapılır.

Hizmet kayıtları kamuya açıktır ve kiralama seti şifrelenmediği sürece floodfill'ler tarafından görülebilir.
Kiralama setini isteyen herhangi bir yönlendirici hizmet kayıtlarını görebilir.

"self" olmayan bir SRV kaydı (yani farklı bir ana makine adı/b32 hedefine işaret eden),
hedef ana makine adı/b32'nin onayını gerektirmez.
Bir hizmetin rastgele bir hedefe yönlendirilmesinin bir saldırıya olanak sağlayıp sağlamayacağı
veya böyle bir saldırının amacı ne olurdu net değildir.
Ancak bu öneri, hedefin de bir "self" SRV kaydı yayınlamasını zorunlu kılerek
böyle bir saldırıyı azaltır. Uygulayıcılar hedefin kiralama setinde "self" kaydının olup olmadığını kontrol etmelidir.


## Uyumluluk

LS2: Sorun yok. Bilinen tüm uygulamalar şu anda LS2'deki seçenek alanını yoksayar
ve boş olmayan bir seçenek alanının doğru şekilde atlanmasını sağlar.
Bu, LS2'nin geliştirilmesi sırasında hem Java I2P hem de i2pd tarafından test edilerek doğrulandı.
LS2, 2016'da 0.9.38'de uygulandı ve tüm yönlendirici uygulamaları tarafından iyi desteklenir.
Tasarım, floodfill'lerde özel destek, önbellekleme veya herhangi bir değişiklik gerektirmez.

Adlandırma: '_' i2p ana makine adlarında geçerli bir karakter değildir.

I2CP: 2-4 arama türleri, desteklendiği minimum API sürümünün altındaki yönlendiricilere gönderilmemelidir (TBD).

SAM: Java SAM sunucusu OPTIONS=true gibi ek anahtar/değerleri yoksayar.
i2pd de aynı şekilde yapmalıdır, doğrulanacak.
SAM istemcileri OPTIONS=true ile istenmedikçe ek değerleri yanıttan alamazlar.
Sürüm yükseltmesi gerekli olmamalıdır.


## Geçiş

Uygulamalar, I2CP değişiklikleri için etkili API sürümü konusunda bir anlaşma dışında
her zaman destek ekleyebilir, koordinasyon gerekmez.
Her uygulama için SAM uyumluluk sürümleri SAM spesifikasyonunda belgelenir.


## Referanslar

* [DOTWELLKNOWN](http://i2pforum.i2p/viewtopic.php?p=3102)
* [I2CP](/docs/specs/i2cp/)
* [I2CP-OPTIONS](/docs/specs/i2cp/)
* [LS2](/docs/specs/common-structures/)
* [GNS](http://zzz.i2p/topcs/1545)
* [NAMING](/docs/overview/naming/)
* [Prop123](/proposals/123-new-netdb-entries/)
* [Prop168](/proposals/168-tunnel-bandwidth/)
* [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
* [RFC2782](https://datatracker.ietf.org/doc/html/rfc2782)
* [SAMv3](/docs/api/samv3/)
* [SRV](https://en.wikipedia.org/wiki/SRV_record)
