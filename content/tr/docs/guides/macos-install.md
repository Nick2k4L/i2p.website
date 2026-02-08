---
title: "macOS'ta I2P Kurulumu"
description: "macOS'ta I2P ve bağımlılıklarını manuel olarak yükleme rehberi"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

## İhtiyacınız Olanlar

- macOS 10.14 (Mojave) veya daha yeni sürüm çalıştıran bir Mac
- Uygulama yüklemek için yönetici erişimi
- Yaklaşık 15-20 dakika süre
- Yükleyicileri indirmek için internet bağlantısı

## Genel Bakış

Bu kurulum süreci dört ana adımdan oluşur:

1. **Java'yı Kurun** - Oracle Java Runtime Environment'ı indirin ve kurun
2. **I2P'yi Kurun** - I2P kurulum dosyasını indirin ve çalıştırın
3. **I2P Uygulamasını Yapılandırın** - Başlatıcıyı ayarlayın ve dock'unuza ekleyin
4. **I2P Bant Genişliğini Yapılandırın** - Bağlantınızı optimize etmek için kurulum sihirbazını çalıştırın

## Birinci Bölüm: Java Kurulumu

I2P çalışmak için Java gerektirir. Eğer Java 8 veya daha yeni bir sürümü zaten yüklüyse, [İkinci Bölüme atlayabilirsiniz](#part-two-download-and-install-i2p).

### Adım 1: Java İndirin

[Oracle Java indirme sayfasını](https://www.oracle.com/java/technologies/downloads/) ziyaret edin ve Java 8 veya daha yeni sürüm için macOS yükleyicisini indirin.

![macOS için Oracle Java İndir](/images/guides/macos-install/0-jre.png)

### Adım 2: Yükleyiciyi Çalıştırın

İndirilen `.dmg` dosyasını İndirilenler klasörünüzde bulun ve açmak için çift tıklayın.

![Java yükleyicisini açın](/images/guides/macos-install/1-jre.png)

### Adım 3: Kuruluma İzin Ver

macOS, yükleyici tanımlı bir geliştirici tarafından sağlandığı için bir güvenlik uyarısı gösterebilir. Devam etmek için **Aç**'a tıklayın.

![Kurulum programına devam etme izni verin](/images/guides/macos-install/2-jre.png)

### Adım 4: Java Kurulumu

Java kurulum sürecini başlatmak için **Kur**'a tıklayın.

![Java kurulumunu başlat](/images/guides/macos-install/3-jre.png)

### Adım 5: Kurulumun Tamamlanmasını Bekleyin

Yükleyici dosyaları kopyalayacak ve sisteminizde Java'yı yapılandıracak. Bu işlem genellikle 1-2 dakika sürer.

![Yükleyicinin tamamlanmasını bekleyin](/images/guides/macos-install/4-jre.png)

### Adım 6: Kurulum Tamamlandı

Başarı mesajını gördüğünüzde, Java yüklenmiştir! Bitirmek için **Kapat**'a tıklayın.

![Java kurulumu tamamlandı](/images/guides/macos-install/5-jre.png)

## İkinci Bölüm: I2P'yi İndirin ve Kurun

Artık Java kurulu olduğuna göre, I2P router'ını kurabilirsiniz.

### Adım 1: I2P'yi İndirin

[İndirmeler sayfasını](/downloads/) ziyaret edin ve **Unix/Linux/BSD/Solaris için I2P** kurulum dosyasını (`.jar` dosyası) indirin.

![I2P kurulum programını indirin](/images/guides/macos-install/0-i2p.png)

### Adım 2: Kurulum Programını Çalıştırın

İndirilen `i2pinstall_X.X.X.jar` dosyasına çift tıklayın. Yükleyici başlatılacak ve tercih ettiğiniz dili seçmenizi isteyecektir.

![Select your language](/images/guides/macos-install/1-i2p.png)

### Adım 3: Karşılama Ekranı

Hoş geldin mesajını okuyun ve devam etmek için **İleri**'ye tıklayın.

![Installer introduction](/images/guides/macos-install/2-i2p.png)

### Adım 4: Önemli Uyarı

Yükleyici güncellemeler hakkında önemli bir uyarı gösterecektir. I2P güncellemeleri **uçtan uca imzalı** ve doğrulanmıştır, bu yükleyicinin kendisi imzasız olsa bile. **İleri**'ye tıklayın.

![Important notice about updates](/images/guides/macos-install/3-i2p.png)

### Adım 5: Lisans Sözleşmesi

I2P lisans anlaşmasını okuyun (BSD tarzı lisans). Kabul etmek için **İleri**'ye tıklayın.

![Lisans sözleşmesi](/images/guides/macos-install/4-i2p.png)

### Adım 6: Kurulum Dizinini Seçin

I2P'nin nereye kurulacağını seçin. Varsayılan konum (`/Applications/i2p`) önerilir. **İleri**'ye tıklayın.

![Kurulum dizinini seçin](/images/guides/macos-install/5-i2p.png)

### Adım 7: Bileşenleri Seçin

Tam kurulum için tüm bileşenleri seçili bırakın. **İleri**'ye tıklayın.

![Kurulacak bileşenleri seçin](/images/guides/macos-install/6-i2p.png)

### Adım 8: Kurulumu Başlat

Seçimlerinizi gözden geçirin ve I2P kurulumunu başlatmak için **İleri**'ye tıklayın.

![Kurulumu başlat](/images/guides/macos-install/7-i2p.png)

### Adım 9: Dosyaları Yükleme

Yükleyici I2P dosyalarını sisteminize kopyalayacak. Bu işlem yaklaşık 1-2 dakika sürer.

![Kurulum devam ediyor](/images/guides/macos-install/8-i2p.png)

### Adım 10: Başlatma Betiklerini Oluştur

Yükleyici, I2P'yi başlatmak için başlatma betikleri oluşturur.

![Başlatma komut dosyaları oluşturuluyor](/images/guides/macos-install/9-i2p.png)

### Adım 11: Kurulum Kısayolları

Yükleyici masaüstü kısayolları ve menü girişleri oluşturmayı önerir. Seçimlerinizi yapın ve **İleri**'ye tıklayın.

![Kısayollar oluştur](/images/guides/macos-install/10-i2p.png)

### Adım 12: Kurulum Tamamlandı

Başarılı! I2P şimdi yüklendi. Bitirmek için **Tamam**'a tıklayın.

![Kurulum tamamlandı](/images/guides/macos-install/11-i2p.png)

## Üçüncü Bölüm: I2P Uygulamasını Yapılandırma

Şimdi I2P'yi Uygulamalar klasörünüze ve Dock'unuza ekleyerek başlatmasını kolaylaştıralım.

### Adım 1: Uygulamalar Klasörünü Açın

Finder'ı açın ve **Uygulamalar** klasörünüze gidin.

![Uygulamalar klasörünü açın](/images/guides/macos-install/0-conf.png)

### Adım 2: I2P Başlatıcısını Bulun

`/Applications/i2p/` klasörü içinde **I2P** klasörünü veya **Start I2P Router** uygulamasını arayın.

![I2P başlatıcısını bulun](/images/guides/macos-install/1-conf.png)

### Adım 3: Dock'a Ekle

Kolay erişim için **Start I2P Router** uygulamasını Dock'unuza sürükleyin. Ayrıca masaüstünüzde bir takma ad oluşturabilirsiniz.

![I2P'yi Dock'unuza Ekleyin](/images/guides/macos-install/2-conf.png)

**İpucu**: Dock'taki I2P simgesine sağ tıklayın ve kalıcı hale getirmek için **Seçenekler → Dock'ta Tut**'u seçin.

## Dördüncü Bölüm: I2P Bant Genişliğini Yapılandırma

I2P'yi ilk kez başlattığınızda, bant genişliği ayarlarınızı yapılandırmak için bir kurulum sihirbazı çalıştırırsınız. Bu, I2P'nin performansını bağlantınız için optimize etmeye yardımcı olur.

### Adım 1: I2P'yi Başlatın

Dock'unuzdaki I2P simgesine tıklayın (veya başlatıcıya çift tıklayın). Varsayılan web tarayıcınız I2P Router Console'a açılacaktır.

![I2P Router Console karşılama ekranı](/images/guides/macos-install/0-wiz.png)

### Adım 2: Hoş Geldiniz Sihirbazı

Kurulum sihirbazı sizi karşılayacaktır. I2P'yi yapılandırmaya başlamak için **İleri**'ye tıklayın.

![Setup wizard introduction](/images/guides/macos-install/1-wiz.png)

### Adım 3: Dil ve Tema

Tercih ettiğiniz **arayüz dilini** seçin ve **açık** veya **koyu** tema arasından birini seçin. **İleri**'ye tıklayın.

![Dil ve tema seçin](/images/guides/macos-install/2-wiz.png)

### Adım 4: Bant Genişliği Test Bilgileri

Sihirbaz bant genişliği testini açıklayacaktır. Bu test internet hızınızı ölçmek için **M-Lab** servisine bağlanır. Devam etmek için **İleri**'ye tıklayın.

![Bandwidth test explanation](/images/guides/macos-install/3-wiz.png)

### Adım 5: Bant Genişliği Testi Çalıştırın

Yükleme ve indirme hızlarınızı ölçmek için **Testi Çalıştır**'a tıklayın. Test yaklaşık 30-60 saniye sürer.

![Bant genişliği testini çalıştırma](/images/guides/macos-install/4-wiz.png)

### Adım 6: Test Sonuçları

Test sonuçlarınızı inceleyin. I2P, bağlantı hızınıza göre bant genişliği ayarları önerecektir.

![Bant genişliği test sonuçları](/images/guides/macos-install/5-wiz.png)

### Adım 7: Bant Genişliği Paylaşımını Yapılandırın

I2P ağı ile ne kadar bant genişliği paylaşmak istediğinizi seçin:

- **Otomatik** (Önerilen): I2P bant genişliğini kullanımınıza göre yönetir
- **Sınırlı**: Belirli yükleme/indirme limitleri ayarlayın
- **Sınırsız**: Mümkün olduğunca çok paylaşın (hızlı bağlantılar için)

Ayarlarınızı kaydetmek için **İleri**'ye tıklayın.

![Bant genişliği paylaşımını yapılandır](/images/guides/macos-install/6-wiz.png)

### Adım 8: Yapılandırma Tamamlandı

I2P router'ınız artık yapılandırılmış ve çalışıyor! Router konsolu bağlantı durumunuzu gösterecek ve I2P sitelerine göz atmanızı sağlayacak.

## I2P ile Başlarken

I2P kurulup yapılandırıldığına göre, artık şunları yapabilirsiniz:

1. **I2P sitelerini gezin**: Popüler I2P hizmetlerinin bağlantılarını görmek için [I2P ana sayfasını](http://127.0.0.1:7657/home) ziyaret edin
2. **Tarayıcınızı yapılandırın**: `.i2p` sitelerine erişmek için bir [tarayıcı profili](/docs/guides/browser-config) oluşturun
3. **Hizmetleri keşfedin**: I2P e-posta, forum, dosya paylaşımı ve daha fazlasını inceleyin
4. **Router'ınızı izleyin**: [Konsol](http://127.0.0.1:7657/console) ağ durumunuzu ve istatistiklerinizi gösterir

### Faydalı Bağlantılar

- **Router Konsolu**: [http://127.0.0.1:7657/](http://127.0.0.1:7657/)
- **Yapılandırma**: [http://127.0.0.1:7657/config](http://127.0.0.1:7657/config)
- **Adres Defteri**: [http://127.0.0.1:7657/susidns/addressbook](http://127.0.0.1:7657/susidns/addressbook)
- **Bant Genişliği Ayarları**: [http://127.0.0.1:7657/config](http://127.0.0.1:7657/config)

## Kurulum Sihirbazını Yeniden Çalıştırma

Bant genişliği ayarlarınızı değiştirmek veya I2P'yi daha sonra yeniden yapılandırmak istiyorsanız, Router Console'dan hoş geldin sihirbazını yeniden çalıştırabilirsiniz:

1. [I2P Kurulum Sihirbazı](http://127.0.0.1:7657/welcome)'na gidin
2. Sihirbaz adımlarını tekrar takip edin

## Sorun Giderme

### I2P Başlamıyor

- **Java'yı kontrol edin**: Terminal'de `java -version` komutunu çalıştırarak Java'nın yüklü olduğundan emin olun
- **İzinleri kontrol edin**: I2P klasörünün doğru izinlere sahip olduğundan emin olun
- **Logları kontrol edin**: Hata mesajları için `~/.i2p/wrapper.log` dosyasına bakın

### Tarayıcı I2P Sitelerine Erişemiyor

- I2P'nin çalıştığından emin olun (Router Console'u kontrol edin)
- Tarayıcınızın proxy ayarlarını HTTP proxy `127.0.0.1:4444` kullanacak şekilde yapılandırın
- I2P'nin ağa entegre olması için başlattıktan sonra 5-10 dakika bekleyin

### Yavaş Performans

- Bant genişliği testini tekrar çalıştırın ve ayarlarınızı düzenleyin
- Ağ ile bir miktar bant genişliği paylaştığınızdan emin olun
- Router Console'da bağlantı durumunuzu kontrol edin

## I2P'yi Kaldırma

I2P'yi Mac'inizden kaldırmak için:

1. Çalışıyorsa I2P router'ı kapatın
2. `/Applications/i2p` klasörünü silin
3. `~/.i2p` klasörünü silin (I2P yapılandırmanız ve verileriniz)
4. I2P simgesini Dock'tan kaldırın

## Sonraki Adımlar

- **Topluluğa katılın**: [i2pforum.net](http://i2pforum.net) adresini ziyaret edin veya Reddit'te I2P'yi inceleyin
- **Daha fazla öğrenin**: Ağın nasıl çalıştığını anlamak için [I2P belgelerini](/en/docs) okuyun
- **Dahil olun**: [I2P'ye katkıda bulunmayı](/en/get-involved) düşünün - geliştirme veya altyapı işletimi konularında

Tebrikler! Artık I2P ağının bir parçasısınız. Görünmez internete hoş geldiniz!

---
