---
title: "Tunnel Oluşturma Spesifikasyonu"
description: "Etkileşimli olmayan teleskoplama kullanarak tunnel oluşturmak için ElGamal tunnel yapı spesifikasyonu."
slug: "tunnel-creation"
aliases: 
category: "Tasarım"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Genel Bakış

NOT: ESKİMİŞ - Bu ElGamal tunnel oluşturma spesifikasyonudur. X25519 tunnel oluşturma spesifikasyonu için [tunnel-creation-ecies](/docs/specs/tunnel-creation-ecies/) sayfasına bakın.

Bu belge, "etkileşimsiz teleskopik" yöntem kullanarak tunnel'lar oluşturmak için kullanılan şifrelenmiş tunnel yapım mesajlarının ayrıntılarını belirtir. Eş seçimi ve sıralama yöntemleri dahil olmak üzere sürecin genel bakışı için tunnel yapım belgesi [TUNNEL-IMPL](/docs/specs/tunnel-implementation/) bölümüne bakın.

Tunnel oluşturma işlemi, tunnel içindeki peer yolu boyunca iletilen, yerinde yeniden yazılan ve tunnel oluşturucusuna geri gönderilen tek bir mesaj ile gerçekleştirilir. Bu tek tunnel mesajı değişken sayıda kayıttan (8'e kadar) oluşur - tunnel içindeki her potansiyel peer için bir tane. Bireysel kayıtlar, yol boyunca sadece belirli bir peer tarafından okunabilmesi için asimetrik olarak (ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)) şifrelenir, aynı zamanda asimetrik olarak şifrelenmiş kaydı sadece uygun zamanda açığa çıkarmak için her hop'ta ek bir simetrik şifreleme katmanı (AES [CRYPTO-AES](/docs/specs/cryptography/#aes)) eklenir.

### Kayıt Sayısı

Tüm kayıtların geçerli veri içermesi zorunlu değildir. Örneğin, 3 atlamalı bir tunnel için build mesajı, tunnel'ın gerçek uzunluğunu katılımcılardan gizlemek için daha fazla kayıt içerebilir. İki build mesaj türü vardır. Orijinal Tunnel Build Message ([TBM](/docs/specs/i2np/#struct-TunnelBuild)) 8 kayıt içerir, bu da pratik herhangi bir tunnel uzunluğu için fazlasıyla yeterlidir. Daha yeni Variable Tunnel Build Message ([VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild)) 1 ile 8 arasında kayıt içerir. Başlatıcı, mesajın boyutunu istenen tunnel uzunluğu gizleme miktarıyla dengeleyebilir.

Mevcut ağda, çoğu tunnel 2 veya 3 hop uzunluğundadır. Mevcut uygulama, 4 hop veya daha az uzunluktaki tunnel'ları oluşturmak için 5 kayıtlı VTBM kullanır ve daha uzun tunnel'lar için 8 kayıtlı TBM kullanır. 5 kayıtlı VTBM (parçalandığında üç adet 1KB tunnel mesajına sığar) ağ trafiğini azaltır ve oluşturma başarı oranını artırır, çünkü daha küçük mesajların düşürülme olasılığı daha azdır.

Yanıt mesajı, yapılandırma mesajı ile aynı tip ve uzunlukta olmalıdır.

### Request Record Spesifikasyonu

Ayrıca I2NP Spesifikasyonunda belirtilmiştir [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

Kaydın düz metni, yalnızca sorulan hop tarafından görülebilir:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">tunnel ID to receive messages as, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4-35</td><td style="border:1px solid var(--color-border); padding:0.6rem;">local router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">36-39</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next tunnel ID, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">40-71</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">72-103</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel layer key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">104-135</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel IV key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">136-167</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">168-183</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply IV</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">184</td><td style="border:1px solid var(--color-border); padding:0.6rem;">flags</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">185-188</td><td style="border:1px solid var(--color-border); padding:0.6rem;">request time (in hours since the epoch, rounded down)</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">189-192</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next message ID</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">193-221</td><td style="border:1px solid var(--color-border); padding:0.6rem;">uninterpreted / random padding</td></tr>
</tbody>
</table>
Sonraki tunnel ID'si ve sonraki router kimlik hash alanları, tunnel'daki bir sonraki atlamayı belirtmek için kullanılır, ancak giden tunnel uç noktası için yeniden yazılan tunnel oluşturma yanıt mesajının nereye gönderilmesi gerektiğini belirtirler. Ayrıca, sonraki mesaj ID'si, mesajın (veya yanıtın) kullanması gereken mesaj ID'sini belirtir.

Tunnel katman anahtarı, tunnel IV anahtarı, yanıt anahtarı ve yanıt IV'ü, yalnızca bu yapı istek kaydında kullanılmak üzere yaratıcı tarafından oluşturulan rastgele 32-bayt değerlerdir.

Flags alanı aşağıdakileri içerir (bit sırası: 76543210, bit 7 MSB'dir):

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages from anyone</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages to anyone, and send the reply to the specified next hop in a Tunnel Build Reply Message</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5-0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Undefined, must set to 0 for compatibility with future options</td></tr>
</tbody>
</table>
Bit 7, hop'un bir gelen gateway (IBGW) olacağını belirtir. Bit 6, hop'un bir giden endpoint (OBEP) olacağını belirtir. Her iki bit de ayarlanmamışsa, hop bir ara katılımcı olacaktır. Her ikisi aynı anda ayarlanamaz.

#### İstek Kaydı Oluşturma

Her hop rastgele bir Tunnel ID alır, sıfır olmayan. Mevcut ve sonraki hop Tunnel ID'leri doldurulur. Her kayıt rastgele bir tunnel IV anahtarı, yanıt IV'si, katman anahtarı ve yanıt anahtarı alır.

#### Request Record Şifreleme

Bu açık metin kaydı, hop'un genel şifreleme anahtarı ile ElGamal 2048 şifreleme [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) kullanılarak şifrelenir ve 528 baytlık bir kayıt olarak biçimlendirilir:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">First 16 bytes of the SHA-256 of the current hop's router identity</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">16-527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal-2048 encrypted request record</td></tr>
</tbody>
</table>
512 baytlık şifrelenmiş kayıtta, ElGamal verisi 514 baytlık ElGamal şifrelenmiş bloğun 1-256 ve 258-513 baytlarını içerir [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). Bloktan gelen iki dolgu baytı (0 ve 257 konumlarındaki sıfır baytları) kaldırılır.

Cleartext alanın tamamını kullandığından, `SHA256(cleartext) + cleartext` dışında ek padding'e gerek yoktur.

Her 528 baytlık kayıt daha sonra yinelemeli olarak şifrelenir (her atlama için yanıt anahtarı ve yanıt IV'si kullanılarak AES şifre çözme ile) böylece router kimliği yalnızca söz konusu atlama için açık metin halinde olur.

### Hop İşleme ve Şifreleme

Bir hop TunnelBuildMessage aldığında, içindeki kayıtları kendi kimlik hash'i ile başlayanlar için inceler (16 bayta kırpılmış). Daha sonra o kayıttan ElGamal bloğunu çözer ve korumalı düz metni alır. Bu noktada, AES-256 yanıt anahtarını bir Bloom filtresine vererek tunnel isteğinin tekrar olmadığından emin olurlar. Tekrarlar veya geçersiz istekler atılır. Mevcut saat veya saatin başından kısa bir süre sonraysa bir önceki saat ile damgalanmamış kayıtlar atılmalıdır. Örneğin, zaman damgasındaki saati alın, tam zamana dönüştürün, sonra mevcut zamandan 65 dakikadan fazla geriyse veya 5 dakika ileriyse geçersizdir. Bloom filtresi en az bir saat sürmeli (artı birkaç dakika, saat farkına izin vermek için), böylece kayıttaki saat zaman damgasını kontrol ederek reddedilmeyen mevcut saatteki tekrar kayıtlar, filtre tarafından reddedilir.

Tunnel'a katılmayı kabul edip etmeyeceklerine karar verdikten sonra, isteği içeren kaydı şifrelenmiş bir yanıt bloğu ile değiştirirler. Diğer tüm kayıtlar, dahil edilen yanıt anahtarı ve IV ile AES-256 şifrelenmiş [CRYPTO-AES](/docs/specs/cryptography/#aes) olur. Her biri aynı yanıt anahtarı ve yanıt IV'si ile ayrı ayrı AES/CBC şifrelenmiştir. CBC modu kayıtlar arasında devam ettirilmez (zincirlenmiş).

Her hop yalnızca kendi yanıtını bilir. Eğer kabul ederse, kullanılmayacak olsa bile tunnel'i süre dolana kadar koruyacaktır, çünkü diğer tüm hop'ların kabul edip etmediğini bilemez.

#### Yanıt Kaydı Belirtimi

Mevcut hop kendi kaydını okuduktan sonra, tunnel'a katılmayı kabul edip etmediğini ve etmiyorsa reddedme nedenini sınıflandırdığını belirten bir yanıt kaydı ile değiştirir. Bu basitçe 1 bayt değeridir; 0x0 tunnel'a katılmayı kabul ettikleri anlamına gelir ve daha yüksek değerler daha yüksek reddedme seviyelerini ifade eder.

Aşağıdaki ret kodları tanımlanmıştır:

- TUNNEL_REJECT_PROBABALISTIC_REJECT = 10
- TUNNEL_REJECT_TRANSIENT_OVERLOAD = 20
- TUNNEL_REJECT_BANDWIDTH = 30
- TUNNEL_REJECT_CRIT = 50

Router kapanması gibi diğer nedenleri eşlerden gizlemek için, mevcut uygulama neredeyse tüm reddedilenler için TUNNEL_REJECT_BANDWIDTH kullanır.

Yanıt, şifrelenmiş blokta kendisine teslim edilen AES oturum anahtarıyla şifrelenir ve tam kayıt boyutuna ulaşmak için 495 bayt rastgele veriyle doldurulur. Dolgu, durum baytından önce yerleştirilir:

`AES-256-CBC(SHA-256(padding+status) + padding + status, key, IV)`

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-31</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SHA-256 of bytes 32-527</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">32-526</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Random padding</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Reply value</td></tr>
</tbody>
</table>
Bu aynı zamanda I2NP spesifikasyonunda [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) bölümünde açıklanmaktadır.

### Tunnel Oluşturma Mesajı Hazırlığı

Yeni bir Tunnel Build Message oluştururken, tüm Build Request Record'ları önce oluşturulmalı ve ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) kullanılarak asimetrik olarak şifrelenmelidir. Her kayıt daha sonra, AES [CRYPTO-AES](/docs/specs/cryptography/#aes) kullanılarak yoldaki önceki hop'ların yanıt anahtarları ve IV'leri ile önceden şifresi çözülür. Bu şifre çözme işlemi ters sırada çalıştırılmalıdır, böylece asimetrik olarak şifrelenmiş veriler, öncülleri şifreledikten sonra doğru hop'ta açık bir şekilde görünecektir.

Bireysel istekler için gerekli olmayan fazla kayıtlar, oluşturucu tarafından basitçe rastgele verilerle doldurulur.

### Tunnel İnşa Mesajı İletimi

Giden tunneller için, teslimat tunnel yaratıcısından ilk hop'a doğrudan yapılır ve TunnelBuildMessage, yaratıcı tunnel'daki başka bir hop'muş gibi paketlenir. Gelen tunneller için teslimat, mevcut bir giden tunnel üzerinden yapılır. Giden tunnel genellikle oluşturulmakta olan yeni tunnel ile aynı havuzdan gelir. O havuzda giden tunnel mevcut değilse, giden keşif tunnel'ı kullanılır. Başlangıçta, henüz giden keşif tunnel'ı mevcut olmadığında, sahte 0-hop giden tunnel kullanılır.

### Tunnel Build Message Endpoint İşleme

Giden tunnel oluşturumu için, istek bir giden uç noktaya ulaştığında ('herkese mesaj göndermeye izin ver' bayrağı ile belirlenen), hop her zamanki gibi işlenir, kayıt yerine bir yanıtı şifreler ve diğer tüm kayıtları şifreler, ancak TunnelBuildMessage'ın iletileceği 'sonraki hop' olmadığından, bunun yerine şifrelenmiş yanıt kayıtlarını bir TunnelBuildReplyMessage ([TBRM](/docs/specs/i2np/#struct-TunnelBuildReply)) veya VariableTunnelBuildReplyMessage ([VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply)) içine yerleştirir (mesaj türü ve kayıt sayısı isteğinkiyle eşleşmelidir) ve bunu istek kaydında belirtilen yanıt tunnel'ına teslim eder. Bu yanıt tunnel'ı, Tunnel Build Reply Message'ı diğer mesajlar gibi tunnel yaratıcısına geri iletir [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation). Tunnel yaratıcısı daha sonra bunu aşağıda açıklandığı gibi işler.

Yanıt tunnel'ı, oluşturucu tarafından şu şekilde seçildi: Genellikle, inşa edilen yeni giden tunnel ile aynı havuzdan gelen bir tunnel'dır. Bu havuzda mevcut gelen tunnel yoksa, gelen keşif tunnel'ı kullanılır. Başlangıçta, henüz gelen keşif tunnel'ı mevcut olmadığında, sahte 0-hop gelen tunnel kullanılır.

Bir inbound tunnel oluşturulması için, istek inbound endpoint'e (tunnel creator olarak da bilinir) ulaştığında, açık bir Tunnel Build Reply Message üretmeye gerek yoktur ve router her yanıtı aşağıdaki gibi işler.

### Tunnel Yapım Yanıt Mesajı İşleme

Yanıt kayıtlarını işlemek için, oluşturucu her kaydı ayrı ayrı AES ile şifrelemesini çözmek zorundadır. Bunun için eşten sonraki tunnel'daki her hop'un yanıt anahtarını ve IV'sini (ters sırada) kullanır. Bu işlem, tunnel'a katılmayı kabul edip etmediklerini veya neden reddettiklerini belirten yanıtı ortaya çıkarır. Hepsi kabul ederse tunnel oluşturulmuş sayılır ve hemen kullanılabilir, ancak herhangi biri reddederse tunnel iptal edilir.

Anlaşmalar ve reddedilmeler, gelecekteki peer tunnel kapasitesi değerlendirmelerinde kullanılmak üzere her peer'ın profilinde [PEER-SELECTION](/docs/overview/tunnel-routing/) kaydedilir.

## Geçmiş ve Notlar

Bu strateji, I2P posta listesinde Michael Rogers, Matthew Toseland (toad) ve jrandom arasında predecessor saldırısı hakkında yapılan bir tartışma sırasında ortaya çıkmıştır. Bkz. [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html), [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html). 2006-02-16 tarihinde 0.6.1.10 sürümünde tanıtılmıştır ve bu, I2P'de geriye dönük uyumluluğu olmayan bir değişikliğin yapıldığı son zamandır.

Notlar:

- Bu tasarım, tunnel içindeki iki düşman peer'in aynı tunnel içinde olduklarını tespit etmek için bir veya daha fazla istek veya yanıt kaydını etiketlemesini engellemez, ancak bunu yapmak yanıtı okurken tunnel yaratıcısı tarafından tespit edilebilir ve tunnel'ın geçersiz olarak işaretlenmesine neden olabilir.
- Bu tasarım, asimetrik olarak şifrelenmiş bölümde bir iş kanıtı içermez, ancak 16 baytlık kimlik hash'i yarıya kesilebilir ve ikincisi 2^64'e kadar maliyetli bir hashcash fonksiyonu ile değiştirilebilir.
- Bu tasarım tek başına, tunnel içindeki iki düşman peer'in aynı tunnel'da olup olmadıklarını belirlemek için zamanlama bilgilerini kullanmalarını engellemez. Toplu ve senkronize istek tesliminin kullanımı yardımcı olabilir (istekleri toplayıp (ntp-senkronize) dakika üzerinden göndermek). Ancak, bunu yapmak peer'lerin istekleri geciktirerek ve daha sonra tunnel'da gecikmeyi tespit ederek istekleri 'etiketlemesine' olanak tanır, belki de küçük bir pencerede teslim edilmeyen isteklerin düşürülmesi işe yarayabilir (ancak bunu yapmak yüksek derecede saat senkronizasyonu gerektirir). Alternatif olarak, belki de bireysel hop'lar isteği iletmeden önce rastgele bir gecikme ekleyebilir?
- İsteği etiketlemenin ölümcül olmayan yöntemleri var mı?
- Bir saatlik çözünürlüğe sahip zaman damgası tekrar oynatma önleme için kullanılır. Bu kısıtlama 0.9.16 sürümüne kadar uygulanmamıştır.

## Gelecekteki Çalışmalar

- Mevcut implementasyonda, başlatıcı kendisi için bir kaydı boş bırakır. Bu nedenle n kayıtlı bir mesaj yalnızca n-1 hop'luk bir tunnel oluşturabilir. Bu, inbound tunnel'lar için gerekli görünmektedir (burada sondan bir önceki hop, bir sonraki hop için hash önekini görebilir), ancak outbound tunnel'lar için gerekli değildir. Bu araştırılmalı ve doğrulanmalıdır. Kalan kaydı anonimliği tehlikeye atmadan kullanmak mümkünse, bunu yapmalıyız.
- Yukarıdaki notlarda açıklanan olası etiketleme ve zamanlama saldırılarının daha fazla analizi.
- Yalnızca VTBM kullanın; bunu desteklemeyen eski peer'ları seçmeyin.
- Build Request Record bir tunnel yaşam süresi veya süre dolumu belirtmez; her hop tunnel'ı 10 dakika sonra sonlandırır, bu ağ genelinde sabit kodlanmış bir sabittir. Flag alanında bir bit kullanabilir ve padding'den 4 (veya 8) byte alarak yaşam süresi veya süre dolumu belirtebiliriz. İstemci bu seçeneği yalnızca tüm katılımcılar desteklediğinde belirtir.

## Referanslar

- [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) - BuildRequestRecord spesifikasyonu
- [CRYPTO-AES](/docs/specs/cryptography/#aes) - AES şifreleme
- [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) - ElGamal şifreleme
- [HASHING-IT-OUT](http://www-users.cs.umn.edu/~hopper/hashing_it_out.pdf)
- [PEER-SELECTION](/docs/overview/tunnel-routing/)
- [PREDECESSOR](http://forensics.umass.edu/pubs/wright-tissec.pdf)
- [PREDECESSOR-2008](http://forensics.umass.edu/pubs/wright.tissec.2008.pdf)
- [TBM](/docs/specs/i2np/#struct-TunnelBuild) - TunnelBuildMessage
- [TBRM](/docs/specs/i2np/#struct-TunnelBuildReply) - TunnelBuildReplyMessage
- [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html)
- [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html)
- [TUNNEL-IMPL](/docs/specs/tunnel-implementation/)
- [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation)
- [VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild) - VariableTunnelBuildMessage
- [VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply) - VariableTunnelBuildReplyMessage
