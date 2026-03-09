---
title: "I2P'ye Başlarken: Tamamen Yeni Başlayanlar İçin Kapsamlı Rehber"
description: "I2P'ye Başlarken: Tamamen Yeni Başlayanlar İçin Kapsamlı Rehber"
slug: "gettingstarted"
lastUpdated: "2026-03"
accurateFor: "2.11.0"
---

**I2P, internet "içinde" çalışan, tamamen şifrelenmiş, eşten eşe anonim bir ağdır** ve geti2p.net adresinden sunulan Java uygulaması, bunu kullanmanın öncü yöntemi olarak kalmaktadır. Düzenli web'e erişimi anonimleştirmeye odaklanan Tor'un aksine, I2P tamamen kapalı bir yapıda gizli servisler, web siteleri, e-posta, sohbet ve dosya paylaşımı ağını oluşturur.

---

## I2P'yi başlattığınız anda ne olur?

Yüklemeden sonra, I2P `http://127.0.0.1:7657` adresinde **router console** adı verilen yerel bir web uygulamasını başlatır. Bu, tamamen makinenizde çalışan ve güvenlik nedeniyle yalnızca localhost'a bağlı olan komut merkezinizdir. İlk başlatmada, harici M-Lab ölçüm hizmetini kullanarak yaklaşık bir dakika süren dil seçimi, tema seçimi (koyu veya açık) ve otomatik bant genişliği testi gibi adımları size gösteren bir **setup wizard** çalışır. Ardından, ağ ile paylaşmak istediğiniz bant genişliğinizin yüzdesini belirlersiniz.

![I2P Kurulum Sihirbazı - Dil Seçimi](/images/guides/quickstart/wizard-language-selection.webp)

Sihirbaz tamamlandıktan sonra, yönlendirici "yeniden tohumlama" adı verilen bir işleme başlar. Yönlendiriciniz, HTTPS üzerinden sabit kodlanmış yeniden tohumlama sunucularından yaklaşık **100 RouterInfo kaydı** indirerek başlangıçtaki eş listesini elde eder. Bundan sonra, daha fazla eş bulmak ve yerel ağ veritabanı kopyasını (yani "netDb") doldurmak için **keşif tüneli** oluşturmaya başlar. Bu ilk dakikalar boyunca "Tünel reddediliyor: başlatılıyor" mesajını göreceksiniz. Bu durum normaldir.

![I2P Yeniden Başlatma - Başlangıç](/images/guides/quickstart/reseed-bootstrapping.webp)

**Routernizin kullanılır hale gelmesi 3–10 dakika sürebilir** ve en iyi performansa ulaşması için çok daha uzun — art arda günlerce açık kalma — bir süre gerekebilir. Router konsolunun yan çubuğunda eş sayınız "Etkin x/y" şeklinde gösterilir; burada x son zamanlarda mesaj alışverişi yaptığınız eşler, y ise toplam görünürlükte olan tüm eşlerdir. **10 veya daha fazla etkin eş** gördüğünüzde router'ınız sağlıklı bir şekilde bağlı demektir. Yeni bir kullanıcının yapabileceği en önemli şey **router'ı sürekli çalışır durumda bırakmaktır**. Bir kapatmadan sonra diğer düğümler router'ınızı en az 24 saat boyunca güvenilmez olarak işaretler; bu yüzden sık sık yeniden başlatmak performansı ciddi şekilde düşürür.

![I2P Yönlendirici Konsolu Kontrol Paneli](/images/guides/quickstart/router-console-dashboard.png)

---

## Tarayıcınızı I2P için yapılandırma

I2P, Tor Ağı'nın aksine özel bir tarayıcıyla gelmez. I2P sitelerine (`.i2p` sahte üst düzey alan adı) erişmek için trafiği **4444** numaralı bağlantı noktası üzerindeki I2P HTTP vekil sunucusu üzerinden yönlendirmek üzere tarayıcınızın vekil sunucu ayarlarını yapılandırmanız gerekir.

**Windows kullanıcıları için en kolay yol**, Java, yönlendirici ve "I2P in Private Browsing" eklentisiyle birlikte önceden yapılandırılmış bir Firefox profili içeren **Kolay Kurulum Paketi**dir. Bu paket, tüm elle vekil sunucu yapılandırmasını ortadan kaldırır. İndirmenizden itibaren I2P sitelerine göz atmanız yaklaşık dört dakika sürer. macOS için bir Kolay Kurulum paketi (Apple Silicon) de beta olarak mevcuttur. Kolay Kurulum Paketini kullanıyorsanız, aşağıdaki elle kurulumu atlayabilirsiniz.

### Firefox (Önerilen)

Firefox, işletim sisteminizden bağımsız kendi proxy ayarlarına sahip olduğu için kesinlikle önerilir - Chrome ve Edge, tüm uygulamaları etkileyen sistem genelindeki proxy ayarlarını kullanır.

**1. Adım.** Firefox menüsünü (hamburger simgesi) açın ve **Ayarlar**'a tıklayın.

![Firefox - Ayarları Aç](/images/guides/browser-config/accessi2p_3.png)

**Adım 2.** Ayarlar arama çubuğunda **proxy** kelimesini arayın, ardından Ağ Ayarları'nın yanındaki **Ayarlar...** seçeneğine tıklayın.

![Firefox - proxy için ara](/images/guides/browser-config/accessi2p_4.png)

**Adım 3.** **Manuel vekil sunucu yapılandırması** seçeneğini belirleyin, HTTP Vekil Sunucusu için `127.0.0.1` ve port için `4444` girin, ardından **Tamam**'a tıklayın.

![Firefox - Manuel vekil sunucu yapılandırması](/images/guides/browser-config/accessi2p_5.png)

Vekil ayarlandıktan sonra, birkaç `about:config` ayarı önerilir:

- `media.peerConnection.ice.proxy_only` değerini **true** olarak ayarlayın (WebRTC sızıntılarını önler)
- `keyword.enabled` değerini **false** olarak ayarlayın (.i2p adreslerinde arama motoru yönlendirmelerini durdurur)
- `browser.fixup.domainsuffixwhitelist.i2p` adında bir boolean oluşturun ve **true** olarak ayarlayın (Firefox'a `.i2p`'nin geçerli bir alan adı soneki olduğunu bildirir)

Yeni başlayanlar için sürekli bir tuzak: `.i2p` adreslerinden önce her zaman `http://` yazın. Çoğu I2P sitesi HTTPS kullanmaz (I2P zaten tüm trafiği uçtan uca şifreler) ve önek olmadan Firefox sizi bir arama motoruna yönlendirir.

### Chrome / Edge (Windows)

Not: Chrome ve Edge, sisteminizdeki tüm uygulamaları etkileyen **tüm** işletim sistemi proxy ayarlarınızı kullanır.

**Adım 1.** Chrome menüsünü açın ve **Ayarlar**'a tıklayın.

![Chrome - Ayarları Aç](/images/guides/browser-config/accessi2p_6.png)

**Adım 2.** **proxy** kelimesini arayın, ardından **Bilgisayarınızın proxy ayarlarını açın** seçeneğine tıklayın.

![Chrome - proxy için ara](/images/guides/browser-config/accessi2p_7.png)

**Adım 3.** **El ile vekil sunucu ayarı** bölümünde, "Bir vekil sunucu kullan" seçeneğinin yanındaki **Kurulumu** tıklayın.

![Windows - Proxy ayarları](/images/guides/browser-config/accessi2p_8.png)

**Adım 4.** **Bir vekil sunucu kullan** seçeneğini Aç konumuna getirin, Vekil sunucu IP adresi için `127.0.0.1` ve port için `4444` girin, ardından **Kaydet**'e tıklayın.

![Windows - Proxy sunucusunu düzenle](/images/guides/browser-config/accessi2p_9.png)

### Safari (macOS)

**Adım 1.** **Safari → Ayarlar → Gelişmiş** bölümüne gidin ve Vekillerin yanındaki **Ayarları Değiştir...** seçeneğine tıklayın.

![Safari - Gelişmiş ayarlar](/images/guides/browser-config/accessi2p_1.png)

**Adım 2.** **Web vekil sunucusu (HTTP)** seçeneğini etkinleştirin, sunucu için `127.0.0.1` ve port için `4444` girin, ardından **Tamam**'a tıklayın.

![macOS - Web proxy ayarları](/images/guides/browser-config/accessi2p_2.png)

---

## Yönlendirici konsolu panosını anlama

`127.0.0.1:7657` adresindeki yönlendirici konsolu, düğümünüzün ne kadar iyi performans gösterdiğini anlamanızı sağlayan birkaç önemli göstergeler sunar. **Yan çubuk**, I2P sürümünüzü, çalışma süresini, bant genişliği kullanımını (giriş/çıkış), aktif eş sayısı ve tünel durumunu gösterir. "Paylaşılan İstemciler" yeşile döndüğünde, yönlendiriciniz entegre edilmiş ve kullanıma hazırdır.

![Yönetici Konsolu - Paylaşılan İstemciler Yeşil](/images/guides/quickstart/shared-clients-green.png)

**Bant genişliği grafikleri**, gerçek zamanlı aktarım hızını gösterir. Varsayılan değerler tutumludur – **96 KBps indirme ve 40 KBps yükleme**, yalnızca 48 KBps paylaşımlı bant genişliği ile sınırlıdır. Resmi belgeler bu değerlerin artırılmasını kesinlikle önerir. Sınırlarınızı artırmak için `http://127.0.0.1:7657/config` adresine gidin (ya da konsolda "Bant Genişliğini Yapılandır" seçeneğine tıklayın). Daha yüksek paylaşımlı bant genişliği, hem kendi performansınızı hem de ağın sağlığını iyileştirir. Paylaşımlı bant genişliğinizi **12 KBps'in altına** düşürmek, yönlendiricinizi "gizli moda" sokar ve trafiğe katılmaktan etkisiz hale getirir. **128 KBps veya üzeri** bir değerde, yönlendiriciniz floodfill durumuna terfi edebilir; bu da, dağıtılmış hash tablosunu (DHT) sürdürmeye yardımcı olacağınız anlamına gelir.

![Bant Genişliği Yapılandırması](/images/guides/quickstart/bandwidth-config.png)

**Tünel durumu** bölümü, diğer kullanıcılar için yönlendirdiğiniz trafiği gösterir. I2P yönlendiricilerinin %90'ından fazlası varsayılan olarak bu tür trafiği iletir. Bu durum, aynı zamanda kendi anonimliğinize katkı sağlayan gizli trafiği oluşturur ve ağa yaptığınız bir katkıdır. Tüneller her 10 dakikada bir sona erer ve otomatik olarak yeniden oluşturulur.

![I2PTunnel Yöneticisi](/images/guides/quickstart/tunnel-manager.png)

`http://127.0.0.1:7657/i2ptunnel/` adresindeki **I2PTunnel yöneticisi**, yapılandırılmış tüm tünellerinizi gösterir - HTTP vekil sunucusu, IRC, e-posta ve eepsite sunucu tüneli, kutudan çıkınca önceden yapılandırılmış olarak gelir.

![I2PTunnel Listesi](/images/guides/quickstart/i2ptunnel-list.png)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Console page</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">URL</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Home / Status</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/home</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Dashboard with peers, bandwidth, tunnels</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Bandwidth config</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/config</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Adjust speed limits and share percentage</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Network config</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/confignet</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Firewall, port, and reachability settings</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Tunnel manager</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/i2ptunnel/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Manage all I2P tunnels and hidden services</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">I2PSnark</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/i2psnark/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Built-in BitTorrent client</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">SusiMail</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/susimail/</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Built-in email client</td>
</tr>
<tr>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Address book</td>
<td style="border:1px solid var(--color-border); padding:0.6rem;"><code>localhost:7657/dns</code></td>
<td style="border:1px solid var(--color-border); padding:0.6rem;">Manage .i2p hostname mappings</td>
</tr>
</tbody>
</table>
---

## Bağlandıktan sonra yapabileceğiniz beş şey

### .i2p sitelerine göz atın

I2P'nin en yaygın kullanımı, gizli web sitelerini ziyaret etmektir. Tarayıcınızı 4444 numaralı porta yönlendirerek herhangi bir `.i2p` adresine gidebilirsiniz. Başlamanız için iyi birkaç popüler site vardır: **`i2p-projekt.i2p`**, ağa yansıtılan resmi I2P proje sitesidir, **`i2pforum.i2p`** topluluk destek forumunu barındırır, **`stats.i2p`** ağ istatistikleri sağlar ve adres kayıt hizmeti sunar, **`notbob.i2p`** ise bilinen eepsitelerin çalışma sürelerini takip eder ve neyin gerçekten çevrimiçi olduğunu görmenizi sağlar. Bilinmeyen bir `.i2p` adresiyle karşılaştığınızda, vekil sunucu hostname'i çözümlemek için "jump service" (atlatma hizmeti) bağlantıları sunar. Yerel adres defterinize yeni siteler eklemek için bunlara tıklayın.

I2P ayrıca, I2P üzerinden normal internete erişmenizi sağlayan varsayılan bir **çıkış vekil sunucusu** (`exit.stormycloud.i2p`) içerir ancak bu ağın birincil amacı değildir ve performans yavaş olacaktır. I2P, Tor gibi bir çıkış düğümü ağı değil, dahili bir karanlık ağ (darknet) olarak tasarlanmıştır.

### I2PSnark ile torrent dosyalarını anonim olarak paylaşın

**I2PSnark**, her I2P kurulumuna entegre edilmiş, `http://127.0.0.1:7657/i2psnark/` adresinden erişilebilen, tam işlevsel bir BitTorrent istemcisidir. Tamamen I2P ağı içinde çalışır; açık internet (clearnet) torrentlerine bağlanamaz ve açık internet kullanıcıları I2P torrentlerini göremez. Web arayüzü magnet linkleri, DHT'yi, sürükle-bırak işlemini, torrent aramayı, sıralı indirmeyi ve UDP tracker'ları (sürüm 2.10.0'da eklenmiştir) destekler. Varsayılan tünel uzunluğu üç hopa kadardır. Yeter ki arayüz aracılığıyla `.torrent` dosyalarını veya magnet linkleri ekleyin.

![I2PSnark Arayüzü](/images/guides/quickstart/i2psnark-interface.png)

Torrent bulmak için `http://tracker2.postman.i2p/` adresindeki **Postman Tracker**'ı ziyaret edin - kullanıcıların I2P ağı içinde başkaları tarafından yüklenmiş torrent'leri arayıp indirdiği merkezileştirilmiş bir merkez. Ayrıca toplulukla paylaşmak için kendi torrent'lerinizi de yükleyebilirsiniz.

![Postman Takipçi](/images/guides/quickstart/postman-tracker.png)

I2P ile uyumlu diğer torrent istemcileri arasında BiglyBT ve I2P eklentisiyle qBittorrent bulunur.

### SusiMail ile şifreli e-posta gönderin

**SusiMail**, tanımlanabilir bilgi sızdırmaması için tasarlanmış `http://127.0.0.1:7657/susimail/` adresinde çalışan bir web tabanlı e-posta istemcisidir. "postman" tarafından işletilen **`mail.i2p`** posta sunucusuna bağlanır. Başlamak için, I2P proxy'niz aracılığıyla erişilebilen **`hq.postman.i2p`** adresinde bir hesap kaydedin, ardından bu kimlik bilgileriyle SusiMail'de oturum açın. Önceden yapılandırılmış I2PTunnel girişleri, SMTP trafiğini `localhost:7659` ve POP3 trafiğini `localhost:7660` üzerinden yönlendirir. E-postalarınızı diğer `@mail.i2p` kullanıcılarına ve normal internet e-posta adreslerine (posta sunucusunun outproxy'si aracılığıyla köprülenerek) gönderebilirsiniz. SusiMail, markdown biçimlendirmeyi, sürükleyip bırakma ile ek dosya ekleme özelliğini ve HTML e-postaları destekler.

![SusiMail Gelen Kutusu](/images/guides/quickstart/susimail-login.png)

![SusiMail Yeni Mesaj](/images/guides/quickstart/susimail-inbox.png)

### Irc2P ağı üzerinden IRC'de sohbet edin

I2P, `localhost:6668` üzerinde **önceden yapılandırılmış bir IRC tüneliyle** birlikte gelir. Herhangi bir IRC istemcisini bu adrese (SSL/TLS **devre dışı** olacak şekilde - şifrelemeyi I2P halleder) yönlendirerek `irc.postman.i2p`, `irc.echelon.i2p` ve `irc.dg.i2p` sunucularını içeren Irc2P ağına bağlanırsınız. Önemli kanallar, genel tartışmalar için **`#i2p`**, geliştirme için **`#i2p-dev`** ve destek için **`#i2p-help`** şeklindedir. IRC tüneli, bağlantınızdaki tanımlanabilir bilgileri otomatik olarak temizler. Önerilen istemciler arasında WeeChat, Pidgin ve Thunderbird Chat bulunur.

### Kendi anonim web sitenizi barındırın

Her I2P kurulumu, `localhost:7658` üzerinde çalışan ve buna karşılık gelen bir I2P sunucu tüneli olan bir **Jetty web sunucusu** içerir. Bir site yayınlamak için HTML dosyalarını belge kök dizinine yerleştirin: Linux'ta `~/.i2p/eepsite/docroot` veya Windows'ta `%LOCALAPPDATA%\I2P\I2P Site\docroot`. Siteniz otomatik olarak kriptografik bir Base64 hedefi ve daha kısa bir `xxxxx.b32.i2p` adresi alır. `mysite.i2p` gibi insan tarafından okunabilir bir isim almak için `stats.i2p` veya `no.i2p` gibi adres defteri servislerinde kaydolun. Daha gelişmiş kurulumlar için Jetty'yi I2PTunnel sunucu tünelinin arkasında Apache veya Nginx ile değiştirebilirsiniz — sadece tanımlanabilir sunucu başlıklarını kaldırmayı unutmayın. Detaylı bir kılavuz için [Bir I2P Eepsite Oluşturma](/docs/guides/creating-an-eepsite/) rehberimize bakın.

---

## Yeni kullanıcılar için temel güvenlik uygulamaları

**Asla I2P ve açık interneti aynı tarayıcı profiliyle kullanmayın.** Bu, en önemli güvenlik kuralıdır. `about:profiles` üzerinden özel bir Firefox profili oluşturun veya Kolay Kurulum Paketi'ndeki önceden yapılandırılmış profili kullanın. Anonim ve kimliğiniz belli olan tarama aktiviteleriniz arasında çerezlerin, geçmişin ve önbelleğe alınmış verilerin birbirine bulaşması, en yaygın operasyonel güvenlik hatasıdır.

Resmi **"I2P in Private Browsing"** Firefox eklentisi (Mozilla'nın eklenti mağazasından edinilebilir), parmak izi önleme, birinci taraf izolasyonu ve mektup kutusu (letterboxing) etkinleştirilmiş izole edilmiş konteyner sekmeleri oluşturarak bunun büyük bir kısmını otomatikleştirir. Chromium kullanıcıları için ayrı bayraklarla başlatın: `--user-data-dir=$HOME/.config/chromium-i2p --proxy-server="http://127.0.0.1:4444"`.

---
