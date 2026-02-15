---
title: "Uygulamanızda I2P'yi Gömme"
description: "Uygulamanızla bir I2P router paketleme yönergeleri"
slug: "embedding"
lastUpdated: "2023-01"
accurateFor: "2.1.0"
---

## Genel Bakış

Bu sayfa, tüm I2P router ikili dosyasını uygulamanızla paketleme hakkındadır. I2P ile çalışacak bir uygulama yazma (paketlenmiş veya harici) hakkında değildir. Ancak, bir router paketlemiyorsanız bile rehberlerin çoğu faydalı olabilir.

Birçok proje I2P'yi paketliyor veya paketleme hakkında konuşuyor. Doğru yapıldığında bu harika. Yanlış yapıldığında ağımıza gerçek zarar verebilir. I2P router karmaşıktır ve tüm bu karmaşıklığı kullanıcılarınızdan gizlemek zorlu olabilir. Bu sayfa bazı genel yönergeleri tartışmaktadır.

Bu yönergelerin çoğu Java I2P veya i2pd için eşit şekilde geçerlidir. Ancak, bazı yönergeler Java I2P'ye özgüdür ve aşağıda belirtilmiştir.

### Bizimle İletişime Geçin

Bir diyalog başlatın. Size yardım etmek için buradayız. I2P'yi entegre eden uygulamalar, ağı büyütmek ve herkes için anonimliği iyileştirmek açısından bizim için en umut verici - ve heyecan verici - fırsatlardır.

### Router'ınızı akıllıca seçin

Uygulamanız Java veya Scala dilindeyse, kolay bir seçim - Java router kullanın. C/C++ dilindeyse, i2pd'yi öneririz. i2pcpp'nin geliştirmesi durmuştur. Diğer dillerdeki uygulamalar için, SAM veya BOB veya SOCKS kullanmak ve Java router'ı ayrı bir süreç olarak paketlemek en iyisidir. Aşağıdakilerden bazıları yalnızca Java router için geçerlidir.

### Lisanslama

Paketlediğiniz yazılımın lisans gereksinimlerini karşıladığınızdan emin olun.

---

## Yapılandırma

### Varsayılan yapılandırmayı doğrula

Doğru bir varsayılan yapılandırma çok önemlidir. Çoğu kullanıcı varsayılanları değiştirmeyecektir. Uygulamanızın varsayılanları, paketlediğiniz router'ın varsayılanlarından farklı olması gerekebilir. Gerekirse router varsayılanlarını geçersiz kılın.

İncelenmesi gereken bazı önemli varsayılan ayarlar: Maksimum bant genişliği, tunnel miktarı ve uzunluğu, maksimum katılım tunnel'ları. Bunların çoğu uygulamanızın beklenen bant genişliği ve kullanım kalıplarına bağlıdır.

Kullanıcılarınızın ağa katkıda bulunmasına izin verecek kadar bant genişliği ve tunnel yapılandırın. Harici I2CP'yi devre dışı bırakmayı düşünün, çünkü muhtemelen buna ihtiyacınız yoktur ve çalışan diğer I2P örnekleriyle çakışabilir. Ayrıca örneğin, çıkışta JVM'nin sonlandırılmasını devre dışı bırakan yapılandırmalara da bakın.

### Katılımcı Trafik Değerlendirmeleri

Katılımcı trafiği devre dışı bırakmanız cazip gelebilir. Bunu yapmanın çeşitli yolları vardır (gizli mod, maksimum tunnel sayısını 0'a ayarlama, paylaşılan bant genişliğini 12 KBytes/sn'nin altına ayarlama). Katılımcı trafik olmadan, zarif kapatma konusunda endişelenmeniz gerekmez, kullanıcılarınız kendileri tarafından oluşturulmayan bant genişliği kullanımını görmezler, vb. Ancak, katılımcı tunnel'lara izin vermeniz için birçok neden vardır.

Her şeyden önce, router'ın ağla "bütünleşme" şansı yoksa o kadar iyi çalışmaz ve bu durum başkalarının sizin üzerinizden tunnel'lar oluşturmasıyla büyük ölçüde iyileşir.

İkinci olarak, mevcut ağdaki router'ların %90'ından fazlası katılımcı trafiğe izin veriyor. Bu, Java router'ında varsayılan ayardır. Eğer uygulamanız başkaları için routing yapmıyor ve gerçekten popüler hale geliyorsa, o zaman ağın üzerinde bir asalak haline gelir ve şu anda sahip olduğumuz dengeyi bozar. Eğer gerçekten büyük hale gelirse, o zaman Tor gibi oluruz ve zamanımızı insanları relaying'i etkinleştirmeleri için yalvarmaya harcarız.

Üçüncüsü, katılımcı trafik, kullanıcılarınızın anonimliğine yardımcı olan örtü trafiğidir.

Katılımcı trafiği varsayılan olarak devre dışı bırakmanızı kesinlikle önermiyoruz. Bunu yaparsanız ve uygulamanız çok popüler hale gelirse, ağı bozabilir.

### Kalıcılık

Router'ın verilerini (netDb, yapılandırma, vb.) router çalıştırmaları arasında kaydetmelisiniz. Her başlangıçta yeniden seed yapmanız gerekirse I2P iyi çalışmaz ve bu, reseed sunucularımız üzerinde büyük bir yük oluşturur ve anonimlik açısından da pek iyi değildir. Router bilgilerini paketleseniz bile, I2P en iyi performans için kaydedilmiş profil verilerine ihtiyaç duyar. Kalıcılık olmadan, kullanıcılarınız kötü bir başlangıç deneyimi yaşar.

Kalıcılık sağlayamıyorsanız iki seçeneğiniz vardır. Bu seçeneklerin herhangi biri, projenizin reseed sunucularımız üzerindeki yükünü ortadan kaldıracak ve başlangıç süresini önemli ölçüde iyileştirecektir.

1) Reseed'de normal sayıdan çok daha fazla router bilgisi sunan, örneğin birkaç yüz tane sunan kendi proje reseed sunucunuzu/sunucularınızı kurun. Router'ı sadece kendi sunucularınızı kullanacak şekilde yapılandırın.

2) Yükleyicinizde bir ila iki bin router bilgisini paketleyin.

Ayrıca, router'ın çok sayıda tunnel oluşturmadan önce entegre olması için tunnel başlatma işlemini geciktirin veya kademeli olarak yapın.

### Yapılandırılabilirlik

Kullanıcılarınıza önemli ayarların yapılandırmasını değiştirme imkanı sunun. Muhtemelen I2P'nin karmaşıklığının çoğunu gizlemek isteyeceğinizi anlıyoruz, ancak bazı temel ayarları göstermek önemlidir. Yukarıdaki varsayılan ayarlara ek olarak, UPnP, IP/port gibi bazı ağ ayarları da faydalı olabilir.

### Floodfill Hususları

Belirli bir bant genişliği ayarının üzerinde ve diğer sağlık kriterlerini karşıladığında, router'ınız floodfill olacaktır, bu da bağlantılarda ve bellek kullanımında büyük bir artışa neden olabilir (en azından Java router ile). Bunun uygun olup olmadığını düşünün. Floodfill'i devre dışı bırakabilirsiniz, ancak o zaman en hızlı kullanıcılarınız katkıda bulunabilecekleri kadarını sağlamıyor olurlar. Bu aynı zamanda uygulamanızın tipik çalışma süresine de bağlıdır.

### Yeniden Tohumlama

Router bilgilerini paketleyip paketlemeyeceğinize veya bizim reseed sunucularımızı kullanacağınıza karar verin. Java reseed sunucu listesi kaynak kodda bulunur, dolayısıyla kaynak kodunuzu güncel tutarsanız, sunucu listesi de güncel kalacaktır. Düşman hükümetler tarafından olası engellemelere dikkat edin.

### Paylaşılan İstemcileri Kullan

Java I2P i2ptunnel paylaşımlı istemcileri destekler; burada istemciler tek bir havuzu kullanacak şekilde yapılandırılabilir. Birden fazla istemciye ihtiyacınız varsa ve güvenlik hedeflerinizle uyumluysa, istemcileri paylaşımlı olacak şekilde yapılandırın.

### Tunnel Sayısını Sınırla

Tunnel miktarını `inbound.quantity` ve `outbound.quantity` seçenekleri ile açıkça belirtin. Java I2P'de varsayılan değer 2'dir; i2pd'de varsayılan değer daha yüksektir. Her iki router ile tutarlı ayarlar elde etmek için SAM kullanarak SESSION CREATE satırında belirtin. Gelen/giden için ikişer tunnel, düşük-orta bant genişliği ve düşük-orta fanout uygulamaları için yeterlidir. Sunucular ve yüksek-fanout P2P uygulamaları daha fazlaya ihtiyaç duyabilir. Yüksek trafikli sunucular ve uygulamalar için gereksinimlerin hesaplanması konusunda rehberlik için bu forum gönderisine bakın.

### SAM SIGNATURE_TYPE belirtin

SAM, hedefler için varsayılan olarak DSA_SHA1 kullanır, bu istediğiniz şey değildir. Ed25519 (tip 7) doğru seçimdir. DEST GENERATE komutuna SIGNATURE_TYPE=7 ekleyin veya DESTINATION=TRANSIENT için SESSION CREATE komutuna ekleyin.

### SAM Oturumlarını Sınırla

Çoğu uygulama yalnızca bir SAM oturumuna ihtiyaç duyacaktır. SAM, çok sayıda oturum oluşturulduğunda yerel router'ı veya hatta daha geniş ağı hızla bunaltma yeteneği sağlar. Birden fazla alt hizmet tek bir oturum kullanabiliyorsa, bunları bir PRIMARY oturum ve SUBSESSION'lar ile kurun (şu anda i2pd'de desteklenmiyor). Oturumlar için makul bir sınır toplam 3 veya 4'tür, nadiren 10'a kadar çıkabilir. Birden fazla oturumunuz varsa, her biri için düşük tunnel miktarı belirttiğinizden emin olun, yukarıya bakın.

Neredeyse hiçbir durumda bağlantı başına benzersiz bir oturum gerektirmemelisiniz. Dikkatli bir tasarım olmadan, bu hızlı bir şekilde ağa DDoS saldırısı yapabilir. Güvenlik hedeflerinizin benzersiz oturumlar gerektirip gerektirmediğini dikkatle düşünün. Bağlantı başına oturumlar uygulamadan önce lütfen Java I2P veya i2pd geliştiricileriyle görüşün.

### Ağ Kaynak Kullanımını Azaltma

Bu seçeneklerin şu anda i2pd'de desteklenmediğini unutmayın. Bu seçenekler I2CP ve SAM aracılığıyla desteklenir (delay-open hariç, bu sadece i2ptunnel aracılığıyla). Ayrıntılar için I2CP belgelerine (ve delay-open için i2ptunnel yapılandırma belgelerine) bakın.

Uygulama tunnel'larınızı delay-open, reduce-on-idle ve/veya close-on-idle olarak ayarlamayı düşünün. Bu, i2ptunnel kullanıyorsanız oldukça basittir ancak I2CP'yi doğrudan kullanıyorsanız bunun bir kısmını kendiniz uygulamanız gerekecektir. Bazı arka plan DHT etkinliği varlığında bile tunnel sayısını azaltan ve ardından tunnel'ı kapatan kod için i2psnark'a bakın.

---

## Yaşam Döngüsü

### Güncellenebilirlik

Mümkün olduğunca otomatik güncelleme özelliği veya en azından yeni sürüm için otomatik bildirim ekleyin. En büyük korkumuz, güncellenemeyen çok sayıda router'ın ağda bulunması. Java router için yılda yaklaşık 6-8 sürüm çıkarıyoruz ve kullanıcıların güncel kalması ağın sağlığı için kritik. Genellikle sürüm çıktıktan 6 hafta sonra ağın %80'inden fazlası en son sürümü kullanıyor ve bu durumu sürdürmek istiyoruz. Router'ın yerleşik otomatik güncelleme işlevini devre dışı bırakma konusunda endişelenmenize gerek yok, çünkü bu kod router console'da bulunuyor ve muhtemelen bunu paketlemiyorsunuz.

### Dağıtım

Aşamalı bir kullanıma sunma planınız olsun. Ağı bir anda bunaltmayın. Şu anda günde yaklaşık 25K benzersiz kullanıcımız ve ayda 40K benzersiz kullanıcımız var. Muhtemelen yılda 2-3 kat büyümeyi fazla sorun yaşamadan kaldırabiliriz. Bundan daha hızlı bir artış öngörüyorsanız, VEYA kullanıcı tabanınızın bant genişliği dağılımı (veya çalışma süresi dağılımı, veya diğer önemli özellikler) mevcut kullanıcı tabanımızdan önemli ölçüde farklıysa, gerçekten bir görüşme yapmamız gerekiyor. Büyüme planlarınız ne kadar büyükse, bu kontrol listesindeki diğer her şey o kadar önemli hale gelir.

### Uzun Çalışma Süreleri İçin Tasarla ve Teşvik Et

Kullanıcılarınıza I2P'nin sürekli çalıştırılması durumunda en iyi performansı gösterdiğini söyleyin. Başlangıçtan sonra iyi çalışmaya başlaması birkaç dakika sürebilir, ilk kurulumdan sonra ise daha da uzun sürebilir. Ortalama çalışma süreniz bir saatten azsa, I2P muhtemelen yanlış çözümdür.

---

## Kullanıcı Arayüzü

### Durumu Göster

Kullanıcıya uygulama tunnel'larının hazır olduğuna dair bir gösterge sağlayın. Sabırla beklemeyi teşvik edin.

### Düzgün Kapatma

Mümkünse, katıldığınız tunnel'lar sona erene kadar kapatmayı geciktirin. Kullanıcılarınızın tunnel'ları kolayca kırmasına izin vermeyin, ya da en azından onaylamalarını isteyin.

### Eğitim ve Bağış

Kullanıcılarınıza I2P hakkında daha fazla bilgi edinmeleri ve bağış yapmaları için bağlantılar verirseniz güzel olur.

### Harici Router Seçeneği

Kullanıcı tabanınıza ve uygulamanıza bağlı olarak, harici bir router kullanmak için bir seçenek veya ayrı bir paket sağlamak faydalı olabilir.

---

## Diğer Konular

### Diğer Yaygın Hizmetlerin Kullanımı

Diğer yaygın I2P hizmetlerini (haber beslemeleri, hosts.txt abonelikleri, tracker'lar, outproxy'ler vb.) kullanmayı veya bunlara bağlanmayı planlıyorsanız, bunları aşırı yüklemediğinizden emin olun ve sorun olmadığından emin olmak için bunları işleten kişilerle konuşun.

### Zaman / NTP Sorunları

Not: Bu bölüm Java I2P'yi ifade eder. i2pd bir SNTP istemcisi içermez.

I2P bir SNTP istemcisi içerir. I2P'nin düzgün çalışması için doğru zaman gereklidir. Sistem saatindeki sapmaları telafi edebilir ancak bu başlatmayı geciktirebilir. I2P'nin SNTP sorgularını devre dışı bırakabilirsiniz, ancak uygulamanız sistem saatinin doğru olduğundan emin olmadıkça bu tavsiye edilmez.

### Neyi ve Nasıl Paketleyeceğinizi Seçin

Not: Bu bölüm yalnızca Java I2P için geçerlidir.

En minimum olarak i2p.jar, router.jar, streaming.jar ve mstreaming.jar dosyalarına ihtiyacınız olacak. Yalnızca datagram kullanan bir uygulama için iki streaming jar dosyasını atlayabilirsiniz. Bazı uygulamalar daha fazlasına ihtiyaç duyabilir, örneğin i2ptunnel.jar veya addressbook.jar. Kripto işlemlerini çok daha hızlı hale getirmek için jbigi.jar dosyasını veya desteklediğiniz platformlar için bir alt kümesini eklemeyi unutmayın. Derleme için Java 7 veya daha yüksek bir sürüm gereklidir. Debian / Ubuntu paketleri oluşturuyorsanız, paketi dahil etmek yerine PPA'mızdaki I2P paketini gerektirmelisiniz. Örneğin susimail, susidns, router konsolu ve i2psnark'a neredeyse kesinlikle ihtiyacınız olmayacak.

Aşağıdaki dosyalar "i2p.dir.base" özelliği ile belirtilen I2P kurulum dizininde bulunmalıdır. Reseeding için gerekli olan certificates/ dizinini ve IP doğrulaması için blocklist.txt dosyasını unutmayın. geoip dizini isteğe bağlıdır, ancak router'ın konuma dayalı kararlar verebilmesi için önerilir. geoip dahil ediyorsanız, GeoLite2-Country.mmdb dosyasını o dizine koyduğunuzdan emin olun (installer/resources/GeoLite2-Country.mmdb.gz dosyasından gunzip ile çıkarın). hosts.txt dosyası gerekli olabilir, uygulamanızın kullandığı herhangi bir host'u dahil etmek için değiştirebilirsiniz. İlk varsayılanları geçersiz kılmak için temel dizine bir router.config dosyası ekleyebilirsiniz. clients.config ve i2ptunnel.config dosyalarını gözden geçirin ve düzenleyin veya kaldırın.

Lisans gereksinimleri, LICENSES.txt dosyasını ve licenses dizinini dahil etmenizi gerektirebilir.

- Ayrıca bir hosts.txt dosyası da paketlemek isteyebilirsiniz.
- Eğer sürümünüz için bizim binary dosyalarımızı almak yerine Java I2P'yi derliyorsanız, mutlaka bir bootclasspath belirttiğinizden emin olun.

### Android değerlendirmeleri

Not: Bu bölüm sadece Java I2P'yi kapsamaktadır.

Android router uygulamamız birden fazla istemci tarafından paylaşılabilir. Eğer yüklü değilse, kullanıcı bir istemci uygulaması başlattığında uyarılacaktır.

Bazı geliştiriciler bunun kötü bir kullanıcı deneyimi olduğuna dair endişelerini dile getirmiş ve router'ı kendi uygulamalarına gömmeyi istemişlerdir. Yol haritamızda, gömmeyi kolaylaştırabilecek bir Android router servis kütüphanesi bulunuyor. Daha fazla bilgiye ihtiyaç var.

Yardıma ihtiyacınız varsa, lütfen bizimle iletişime geçin.

### Maven jar dosyaları

Not: Bu bölüm yalnızca Java I2P'ye atıfta bulunmaktadır.

[Maven Central](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22net.i2p%22) üzerinde sınırlı sayıda jar dosyamız bulunmaktadır. Maven Central'daki yayınlanan jar dosyalarını geliştirmek ve genişletmek için ele almamız gereken çok sayıda trac ticket'ımız vardır.

Yardıma ihtiyacınız varsa, lütfen bizimle iletişime geçin.

### Datagram (DHT) değerlendirmeleri

Uygulamanız DHT gibi I2P datagram'ları kullanıyorsa, yükü azaltmak ve güvenilirliği artırmak için birçok gelişmiş seçenek mevcuttur. Bunun iyi çalışması için biraz zaman ve deneme gerekebilir. Boyut/güvenilirlik dengesinden haberdar olun. Yardım için bizimle iletişime geçin. Aynı Destination üzerinde Datagram'lar ve Streaming kullanmak mümkün - ve önerilir. Bunun için ayrı Destination'lar oluşturmayın. İlgisiz verilerinizi mevcut ağ DHT'lerinde (iMule, bote, bittorrent ve router) saklamaya çalışmayın. Kendinizinkini oluşturun. Seed node'ları sabit kod olarak yazıyorsanız, birkaç tane bulundurmanızı öneririz.

### Outproxy'ler

I2P outproxy'leri clearnet'e sınırlı bir kaynaktır. Outproxy'leri yalnızca normal kullanıcı tarafından başlatılan web tarama veya diğer sınırlı trafik için kullanın. Başka herhangi bir kullanım için outproxy operatörü ile görüşün ve onay alın.

### Ortak Pazarlama

Birlikte çalışalım. Bitene kadar beklemeyin. Bize Twitter hesabınızı verin ve bu konuda tweet atmaya başlayın, karşılığını vereceğiz.

### Kötü Amaçlı Yazılım

Lütfen I2P'yi kötü amaçlar için kullanmayın. Bu hem ağımıza hem de itibarımıza büyük zarar verebilir.

### Bize Katılın

Bu açık olabilir, ancak topluluğa katılın. I2P'yi 7/24 çalıştırın. Projeniz hakkında bir I2P Sitesi başlatın. IRC #i2p-dev kanalında takılın. Forumlarda yazı yazın. Haberi yayın. Size kullanıcı, test edici, çevirmen ve hatta kodlayıcı bulmada yardımcı olabiliriz.

---

## Örnekler

### Uygulama Örnekleri

I2P Android uygulamasını yükleyip deneyebilir ve kodunu inceleyerek router'ı paketleyen bir uygulama örneği görebilirsiniz. Kullanıcıya neyi gösterdiğimizi ve neyi sakladığımızı inceleyin. Router'ı başlatmak ve durdurmak için kullandığımız durum makinesine bakın. Diğer örnekler şunlardır: Vuze, Nightweb Android uygulaması, iMule, TAILS, iCloak ve Monero.

### Kod Örneği

Not: Bu bölüm yalnızca Java I2P'yi kapsamaktadır.

Yukarıdakilerin hiçbiri aslında Java router'ını paketlemek için kodunuzu nasıl yazacağınızı söylemiyor, bu yüzden aşağıda kısa bir örnek bulunmaktadır.

```java
import java.util.Properties;
import net.i2p.router.Router;

	Properties p = new Properties();
        // add your configuration settings, directories, etc.
        // where to find the I2P installation files
	p.addProperty("i2p.dir.base", baseDir);
        // where to find the I2P data files
	p.addProperty("i2p.dir.config", configDir);
        // bandwidth limits in K bytes per second
	p.addProperty("i2np.inboundKBytesPerSecond", "50");
	p.addProperty("i2np.outboundKBytesPerSecond", "50");
	p.addProperty("router.sharePercentage", "80");
	p.addProperty("foo", "bar");
	Router r = new Router(p);
        // don't call exit() when the router stops
	r.setKillVMOnEnd(false);
	r.runRouter();

	...

	r.shutdownGracefully();
	// will shutdown in 11 minutes or less
```
Bu kod, Android uygulamamızda olduğu gibi uygulamanızın router'ı başlattığı durum içindir. Java paketlerimizde yapıldığı gibi, Jetty webapps ile birlikte clients.config ve i2ptunnel.config dosyaları aracılığıyla router'ın uygulamayı başlatmasını da sağlayabilirsiniz. Her zaman olduğu gibi, durum yönetimi zor olan kısımdır.

Ayrıca bakınız: router javadocs.
