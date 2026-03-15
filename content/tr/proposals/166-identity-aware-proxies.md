---
title: "I2P önerisi #166: Kimlik/Host Farkındalığı Olan Tünel Türleri"
number: "166"
author: "eyedeekay"
created: "2024-05-27"
lastupdated: "2024-08-27"
status: "Open"
thread: "http://i2pforum.i2p/viewforum.php?f=13"
target: "0.9.65"
toc: true
---
### Sunucuya Duyarlı HTTP Proxy Tünel Türü Önerisi

Bu öneri, geleneksel HTTP-over-I2P kullanımında "Paylaşılan Kimlik Sorunu"nu çözmek amacıyla yeni bir HTTP proxy tünel türü sunar. Bu tünel türünün ek davranışları vardır ve potansiyel saldırgan gizli servis operatörlerinin, hedef alınan kullanıcı ajanlarına (tarayıcılara) ve I2P İstemci Uygulaması'na karşı yaptığı izlemeyi engellemeyi veya sınırlamayı amaçlar.

#### "Paylaşılan Kimlik" sorunu nedir?

"Paylaşılan Kimlik" sorunu, kriptografik adresli bir üst düzey ağda bulunan bir kullanıcı aracının başka bir kullanıcı aracısıyla kriptografik kimliği paylaştığında meydana gelir. Örneğin, bir Firefox ve GNU Wget'in aynı HTTP Proxy'yi kullanacak şekilde yapılandırılması durumunda bu gerçekleşir.

Bu senaryoda, sunucu etkinliğe yanıt vermek için kullanılan kriptografik adresi (Destination) toplayıp saklayabilir. Bu adresi, kökeni kriptografik olduğu için her zaman %100 benzersiz olan bir "parmak izi" olarak değerlendirebilir. Bu, Paylaşılan Kimlik sorununun gözlemlenen bağlantılılığını tam anlamıyla kusursuz hale getirir.

Ancak bu bir sorun mudur?
^^^^^^^^^^^^^^^^^^^^^^^^^

Paylaşılan kimlik sorunu, aynı protokolü kullanan kullanıcı ajanlarının bağlantısızlık istedikleri durumda bir sorundur. [Bu sorun, HTTP bağlamında ilk kez bu Reddit Tartışmasında](https://old.reddit.com/r/i2p/comments/579idi/warning_i2p_is_linkablefingerprintable/) bahsedilmiştir ve silinmiş yorumlara [pullpush.io](https://api.pullpush.io/reddit/search/comment/?link_id=579idi) sayesinde erişilebilir. *O dönemde* en aktif katılımcılardan biriydim ve *o dönemde* bu sorunun önemsiz olduğunu düşünüyordum. Geçtiğimiz 8 yıl içinde durum ve bu konudaki görüşüm değişti; artık kötü niyetli hedef korelasyonunun oluşturduğu tehdidin, daha fazla sitenin belirli kullanıcıları "profilleme" konumuna gelmesiyle önemli ölçüde arttığını düşünüyorum.

Bu saldırının giriş engeli çok düşüktür. Sadece bir gizli servis operatörünün birden fazla hizmet işletmesini gerektirir. Aynı anda yapılan ziyaretlere yönelik saldırılar için (aynı anda birden fazla siteye girilmesi) bu tek gerekliliktir. Zaman içinde olmayan bağlantılar için ise bu hizmetlerden birinin, takip edilmek istenen tek bir kullanıcıya ait "hesaplar" barındıran bir hizmet olması gerekir.

Şu anda, kullanıcı hesapları barındıran herhangi bir servis operatörü, Paylaşılan Kimlik sorununu istismar ederek, kontrol ettikleri herhangi bir sitedeki etkinliklerle bu hesapları ilişkilendirebilir. Mastodon, Gitlab veya basit forumlar bile birden fazla hizmet işletiyor ve bir kullanıcı için profil oluşturmak istiyorlarsa, bu saldırıları gerçekleştiren saldırganlar olabilirler. Bu gözetim, takip etme, maddi kazanç veya istihbarat amaçlı olabilir. Şu anda bu saldırıyı gerçekleştirebilecek ve anlamlı veriler elde edebilecek onlarca büyük operatör var. Şimdilik bunların bunu yapmayacaklarını varsayıyoruz, ancak bizim görüşlerimizle ilgilenmeyen aktörler kolayca ortaya çıkabilir.

Bu, açık ağda yapılan ve kuruluşların kendi sitelerindeki etkileşimleri kontrol ettikleri ağlardaki etkileşimlerle ilişkilendirdikleri temel bir profil oluşturma türüyle doğrudan ilişkilidir. I2P'de, kriptografik hedefin benzersiz olması nedeniyle bu teknik bazen coğrafi konumun ek gücü olmamasına rağmen daha güvenilir olabilir.

Paylaşılan Kimlik, yalnızca coğrafi konumu gizlemek için I2P kullanan bir kullanıcıya karşı etkisizdir. Ayrıca I2P yönlendirmesini kırmak için kullanılamaz. Sadece bağlamsal kimlik yönetimi sorunudur.

- Paylaşılan Kimlik sorunu, bir I2P kullanıcısının coğrafi konumunu belirlemek için kullanılamaz.
- Zaman içinde olmayan oturumları bağlamak için Paylaşılan Kimlik sorunu kullanılamaz.

Ancak, muhtemelen çok yaygın olan koşullarda bir I2P kullanıcısının anonimliğini zayıflatmak için kullanılması mümkündür. Bunların yaygın olmasının bir nedeni, "sekme" işlemi destekleyen Firefox gibi bir web tarayıcısının kullanımını teşvik etmemizdir.

- Paylaşılan Kimlik sorunundan, üçüncü taraf kaynakları isteyebilen *herhangi* bir web tarayıcısında *her zaman* bir parmak izi üretmek mümkündür.
- Javascript'in devre dışı bırakılması, Paylaşılan Kimlik sorununa karşı **hiçbir şey** ifade etmez.
- Geleneksel tarayıcı parmak izi gibi yöntemlerle zaman içinde olmayan oturumlar arasında bir bağlantı kurulabiliyorsa, Paylaşılan Kimlik geçişli olarak uygulanabilir ve zaman içinde olmayan bir bağlantı stratejisi mümkün hale gelebilir.
- Açık ağdaki bir etkinlik ile bir I2P kimliği arasında bir bağlantı kurulabiliyorsa, örneğin hedef, hem I2P hem de açık ağda varlığı olan bir sitede oturum açmışsa, Paylaşılan Kimlik geçişli olarak uygulanabilir ve tamamen anonimliğin kaldırılmasını sağlayabilir.

Paylaşılan Kimlik sorununun I2P HTTP proxy'sine uygulandığında ciddiyetini nasıl değerlendirdiğiniz, uygulama için bağlamsal kimliğin nerede olduğunu (veya daha doğrusu, potansiyel olarak bilgisiz beklentilere sahip bir "kullanıcı") düşündüğünüze bağlıdır. Birkaç olasılık vardır:

1. HTTP hem Uygulama hem de Bağlamsal Kimliktir - Şu anki çalışma şekli budur. Tüm HTTP Uygulamaları bir kimliği paylaşır.
2. Süreç hem Uygulama hem de Bağlamsal Kimliktir - Bu, bir uygulamanın SAMv3 veya I2CP gibi bir API kullandığı durumda geçerlidir; uygulama kimliğini oluşturur ve ömrünü kontrol eder.
3. HTTP Uygulamadır, ancak Sunucu Bağlamsal Kimliktir - Bu öneri tam olarak bunu amaçlar; her sunucuyu potansiyel bir "Web Uygulaması" olarak görür ve tehdit yüzeyini buna göre ele alır.

Çözülebilir mi?
^^^^^^^^^^^^^^

Proxy'nin operasyonunun bir uygulamanın anonimliğini zayıflatabileceği her olası duruma akıllıca yanıt vermesini sağlayan bir proxy oluşturmak muhtemelen mümkün değildir. Ancak, öngörülebilir şekilde davranan belirli bir uygulamaya akıllıca yanıt veren bir proxy oluşturmak mümkündür. Örneğin, modern web tarayıcılarda, kullanıcıların birden fazla sekmede birden fazla web sitesiyle etkileşime gireceği ve bu sitelerin ana bilgisayar adı ile ayrılacağı beklenir.

Bu, HTTP Proxy'nin her sunucuya kendi Destination'ını vererek kullanıcı aracısının davranışını yansıtarak HTTP Proxy'nin davranışını geliştirerek bu tür HTTP kullanıcı ajanları için iyileştirme yapmamızı sağlar. Bu değişiklik, iki farklı sunucunun artık dönüş kimliğini paylaşmayacağı için, iki sunucudaki istemci etkinliklerini ilişkilendirmek için kullanılan bir parmak izi çıkarmak amacıyla Paylaşılan Kimlik sorununun kullanılmasını imkansız hale getirir.

Açıklama:
^^^^^^^^^

Yeni bir HTTP Proxy'si oluşturulacak ve Gizli Servisler Yöneticisi'ne (I2PTunnel) eklenecektir. Yeni HTTP Proxy, I2PSocketManager'ların bir "çoklayıcısı" olarak çalışacaktır. Çoklayıcının kendisinin bir hedefi yoktur. Çoklayıcıya dahil olan her bireysel I2PSocketManager'ın kendi yerel hedefi ve kendi tünel havuzu vardır. I2PSocketManager'lar, çoklayıcı tarafından yeni bir sunucuya ilk ziyarette "talep" edildiğinde isteğe bağlı olarak oluşturulur. Çoklayıcıya eklenmeden önce bir veya daha fazlasını önceden oluşturup çoklayıcının dışında saklayarak I2PSocketManager'ların oluşturulmasını optimize etmek mümkündür. Bu performansı artırabilir.

Herhangi bir I2P Destination'ı *olmayan* siteler için (örneğin herhangi bir Açık Ağ sitesi) bir "Outproxy" taşıyıcısı olarak, kendi hedefine sahip ek bir I2PSocketManager kurulur. Bu, tüm Outproxy kullanımını tek bir Bağlamsal Kimlik haline getirir. Ancak, tünel için birden fazla Outproxy yapılandırılırsa, her outproxy'nin yalnızca tek bir site için istek alacağı normal "Sabit" outproxy döngüsüne neden olur. Bu, açık ağda HTTP-over-I2P proxy'lerini hedefe göre izole etmeye *neredeyse* eşdeğer bir davranıştır.

Kaynak Düşünceleri:
'''''''''''''''''''

Yeni HTTP proxy, mevcut HTTP proxy'ye kıyasla ek kaynaklar gerektirir. Bu:

- Potansiyel olarak daha fazla tünel ve I2PSocketManager oluşturur
- Tünelleri daha sık oluşturur

Bunların her biri şunları gerektirir:

- Yerel hesaplama kaynakları
- Eşlerden ağ kaynakları

Ayarlar:
''''''''

Artan kaynak kullanımının etkisini en aza indirmek için proxy mümkün olduğunca az kullanacak şekilde yapılandırılmalıdır. Çoklayıcıya ait olmayan (üst proxy olmayan) proxy'ler şu şekilde yapılandırılmalıdır:

- Çoklanmış I2PSocketManager'lar, tünel havuzlarında 1 tünel giriş, 1 tünel çıkış oluşturur
- Çoklanmış I2PSocketManager'lar varsayılan olarak 3 zıplama yapar.
- 10 dakika boyunca etkinlik olmazsa soketleri kapatır
- Çoklayıcı tarafından başlatılan I2PSocketManager'lar, çoklayıcının ömrünü paylaşır. Üst çoklayıcı yok edilene kadar çoklanmış tüneller "Yok Edilmez".

Şemalar:
^^^^^^^^

Aşağıdaki şema, "Bir sorun mu?" bölümündeki "Olasılık 1."e karşılık gelen mevcut HTTP proxy'nin çalışmasını temsil eder. Gördüğünüz gibi, HTTP proxy yalnızca bir hedef kullanarak doğrudan I2P siteleriyle etkileşime girer. Bu senaryoda, HTTP hem uygulama hem de bağlamsal kimliktir.

```text
**Mevcut Durum: HTTP Uygulamadır, HTTP Bağlamsal Kimliktir**
                                                      __-> Outproxy <-> i2pgit.org
                                                     /
Tarayıcı <-> HTTP Proxy (tek Hedef)<->I2PSocketManager <---> idk.i2p
                                                     \__-> translate.idk.i2p
                                                      \__-> git.idk.i2p
```

Aşağıdaki şema, "Bir sorun mu?" bölümündeki "Olasılık 3."e karşılık gelen sunucuya duyarlı HTTP proxy'nin çalışmasını temsil eder. Bu senaryoda, HTTP uygulamadır, ancak Sunucu bağlamsal kimliği tanımlar; burada her I2P sitesi, sunucu başına benzersiz bir hedefe sahip farklı bir HTTP proxy'siyle etkileşime girer. Bu, aynı kişinin işlettiği birden fazla siteyi ziyaret ettiğini ayırt edebilmelerini engeller.

```text
**Değişiklikten Sonra: HTTP Uygulamadır, Sunucu Bağlamsal Kimliktir**
                                                    __-> I2PSocketManager (Hedef A - Sadece Outproxy'ler) <--> i2pgit.org
                                                   /
Tarayıcı <-> HTTP Proxy Çoklayıcısı (Hedef Yok) <---> I2PSocketManager (Hedef B) <--> idk.i2p
                                                   \__-> I2PSocketManager (Hedef C) <--> translate.idk.i2p
                                                    \__-> I2PSocketManager (Hedef C) <--> git.idk.i2p
```

Durum:
^^^^^^

Sunucuya duyarlı proxy'nin, bu önerinin eski bir sürümüne uyan çalışan bir Java uygulaması, idk'nin çatalında i2p.i2p.2.6.0-browser-proxy-post-keepalive dalında mevcuttur. Alıntıdaki bağlantıya bakınız. Değişiklikleri daha küçük bölümlere ayırmak amacıyla yoğun bir şekilde gözden geçirilmektedir.

SAMv3 kütüphanesi kullanılarak Go dilinde çeşitli kapasitelerde uygulamalar yazılmıştır; bunlar diğer Go uygulamalarına gömülebilir veya go-i2p için yararlı olabilir ancak Java I2P için uygun değildir. Ayrıca, şifrelenmiş leaseSet'lerle etkileşimli çalışmak için iyi destek eksik.

Ek: ``i2psocks``
               

Yeni bir tünel türü uygulamadan veya mevcut I2P kodunu değiştirmeden diğer tür istemcileri izole etmek için basit bir uygulamaya yönelik yaklaşım mümkündür ve gizlilik topluluğunda zaten yaygın olarak mevcut ve test edilmiş I2PTunnel araçlarını birleştirir. Ancak bu yaklaşım, HTTP için geçerli olmayan ve birçok diğer potansiyel I2P istemcisi için de geçerli olmayan zor bir varsayım yapar.

Yaklaşık olarak, aşağıdaki betik bir uygulamaya duyarlı SOCKS5 proxy'si oluşturur ve temel komutu socksify eder:

```sh
#! /bin/sh
command_to_proxy="$@"
java -jar ~/i2p/lib/i2ptunnel.jar -wait -e 'sockstunnel 7695'
torsocks --port 7695 $command_to_proxy
```

Ek: ``saldırının örnek uygulaması``
                                  

[HTTP Kullanıcı Ajanları üzerinde Paylaşılan Kimlik saldırısının örnek bir uygulaması](https://github.com/eyedeekay/colluding_sites_attack/) birkaç yıldır mevcuttur. Ek bir örnek [idk’nin prop166 deposunun](https://git.idk.i2p/idk/i2p.host-aware-proxy) ``simple-colluder`` alt dizininde mevcuttur. Bu örnekler, saldırının işe yaradığını göstermek amacıyla kasıtlı olarak tasarlanmıştır ve gerçek bir saldırıya dönüştürülebilmesi için (küçük olmakla birlikte) değişiklik gerektirir.
