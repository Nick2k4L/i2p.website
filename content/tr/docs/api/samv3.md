---
title: "SAM V3"
description: "Java olmayan I2P uygulamaları için Basit Anonim Mesajlaşma protokolü"
slug: "samv3"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

SAM, I2P ile etkileşim kurmak için basit bir istemci protokolüdür. SAM, Java olmayan uygulamaların I2P ağına bağlanması için önerilen protokoldür ve birden fazla router uygulaması tarafından desteklenir. Java uygulamaları doğrudan streaming veya I2CP API'lerini kullanmalıdır.

SAMv3 sürümü I2P 0.7.3 sürümünde (Mayıs 2009) tanıtılmıştır ve kararlı ve desteklenen bir arayüzdür. 3.1 de kararlıdır ve kesinlikle önerilen imza türü seçeneğini destekler. Daha yeni 3.x sürümleri gelişmiş özellikleri destekler. i2pd'nin şu anda 3.2 ve 3.3 özelliklerinin çoğunu desteklemediğini unutmayın.

Alternatifler: [SOCKS](/docs/api/socks), [Streaming](/docs/api/streaming), [I2CP](/docs/protocol/i2cp), [BOB (kullanımdan kaldırıldı)](/docs/api/bob). Kullanımdan kaldırılmış sürümler: [SAM V1](/docs/api/sam), [SAM V2](/docs/api/samv2).

## Bilinen SAM Kütüphaneleri

Uyarı: Bunlardan bazıları çok eski veya desteklenmiyor olabilir. Aşağıda belirtilmedikçe hiçbiri I2P projesi tarafından test edilmemiş, incelenmemiş veya bakımı yapılmamıştır. Kendi araştırmanızı yapın.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Library Name</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Language</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">Version</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">STREAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">DGRAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">RAW</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Site</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2psam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++, C wrapper</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2psam">github.com/i2p/i2psam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">gosam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/goSam">github.com/eyedeekay/goSam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">sam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/sam3">github.com/eyedeekay/sam3</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">onramp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/onramp">github.com/eyedeekay/onramp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">txi2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/str4d/txi2p">github.com/str4d/txi2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.socket</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/majestrate/i2p.socket">github.com/majestrate/i2p.socket</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/l-n-s/i2plib">github.com/l-n-s/i2plib</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib-fork</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://codeberg.org/weko/i2plib-fork">codeberg.org/weko/i2plib-fork</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Py2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://i2pgit.org/robin/Py2p">i2pgit.org/robin/Py2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-rs</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2p-rs">github.com/i2p/i2p-rs</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">libsam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/libsam3">github.com/i2p/libsam3</a><br>(Maintained by the I2P project)</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">mooni2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Lua</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://notabug.org/villain/mooni2p">notabug.org/villain/mooni2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">haskell-network-anonymous-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Haskell</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/solatis/haskell-network-anonymous-i2p">github.com/solatis/haskell-network-anonymous-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-sam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Javascript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://codeberg.org/diva.exchange/i2p-sam">codeberg.org/diva.exchange/i2p-sam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">node-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Javascript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/redhog/node-i2p">github.com/redhog/node-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Jsam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/Jsam">github.com/eyedeekay/Jsam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">I2PSharp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/MohA39/I2PSharp">github.com/MohA39/I2PSharp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2pdotnet</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/SamuelFisher/i2pdotnet">github.com/SamuelFisher/i2pdotnet</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.rb</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Ruby</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/dryruby/i2p.rb">github.com/dryruby/i2p.rb</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">solitude</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/syvita/solitude">github.com/syvita/solitude</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Samty</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://notabug.org/acetone/samty">notabug.org/acetone/samty</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">bitcoin</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/bitcoin/bitcoin/blob/master/src/i2p.cpp">source (not a library, but good reference code)</a></td>
    </tr>
  </tbody>
</table>
## Hızlı Başlangıç

Temel bir yalnızca TCP, eşler arası uygulama geliştirmek için, istemci aşağıdaki komutları desteklemelidir:

- `HELLO VERSION MIN=3.1 MAX=3.1` - Kalan tüm komutlar için gerekli
- `DEST GENERATE SIGNATURE_TYPE=7` - Özel anahtarımızı ve destination'ımızı oluşturmak için
- `NAMING LOOKUP NAME=...` - .i2p adreslerini destination'lara dönüştürmek için
- `SESSION CREATE STYLE=STREAM ID=... DESTINATION=... i2cp.leaseSetEncType=4,0` - STREAM CONNECT ve STREAM ACCEPT için gerekli
- `STREAM CONNECT ID=... DESTINATION=...` - Giden bağlantılar yapmak için
- `STREAM ACCEPT ID=...` - Gelen bağlantıları kabul etmek için

## Geliştiriciler için Genel Rehberlik

### Uygulama Tasarımı

SAM oturumları (veya I2P içinde tunnel havuzları veya tunnel setleri) uzun ömürlü olacak şekilde tasarlanmıştır. Çoğu uygulama yalnızca bir oturuma ihtiyaç duyacaktır; bu oturum başlangıçta oluşturulur ve çıkışta kapatılır. I2P, devrelerin hızla oluşturulup atılabileceği Tor'dan farklıdır. Uygulamanızı birden fazla veya iki eş zamanlı oturum kullanacak şekilde veya bunları hızla oluşturup atacak şekilde tasarlamadan önce dikkatli düşünün ve I2P geliştiricileriyle görüşün. Çoğu tehdit modeli her bağlantı için benzersiz bir oturum gerektirmez.

Ayrıca, uygulama ayarlarınızın (ve kullanıcılara router ayarları hakkında verdiğiniz rehberliğin, ya da bir router paketliyorsanız router varsayılan ayarlarının) kullanıcılarınızın ağa tükettiklerinden daha fazla kaynak katkıda bulunmasını sağladığından emin olun. I2P eşler arası bir ağdır ve popüler bir uygulama ağı sürekli tıkanıklığa sürüklerse ağ hayatta kalamaz.

### Uyumluluk ve Test

Java I2P ve i2pd router implementasyonları bağımsızdır ve davranış, özellik desteği ve varsayılan ayınlarda küçük farklılıklar bulunmaktadır. Lütfen uygulamanızı her iki router'ın da en son sürümüyle test edin.

i2pd SAM varsayılan olarak etkindir; Java I2P SAM ise değildir. Kullanıcılarınıza Java I2P'de SAM'i nasıl etkinleştirecekleri konusunda talimatlar verin (router konsolunda /configclients aracılığıyla), ve/veya ilk bağlantı başarısız olursa kullanıcıya iyi bir hata mesajı sağlayın, örneğin "I2P'nin çalıştığından ve SAM arayüzünün etkinleştirildiğinden emin olun".

Java I2P ve i2pd router'ları tunnel miktarları için farklı varsayılan değerlere sahiptir. Java varsayılanı 2 ve i2pd varsayılanı 5'tir. Düşük-orta bant genişliği ve düşük-orta bağlantı sayıları için 2 veya 3 yeterlidir. Java I2P ve i2pd router'ları ile tutarlı performans elde etmek için lütfen SESSION CREATE mesajında tunnel miktarını belirtin. Aşağıya bakınız.

Uygulamanızın yalnızca ihtiyaç duyduğu kaynakları kullanmasını sağlama konusunda geliştiricilere daha fazla rehberlik için lütfen [I2P'yi uygulamanızla paketleme kılavuzumuza](/docs/applications/embedding) bakın.

### İmza ve Şifreleme Türleri

I2P birden fazla imza ve şifreleme türünü destekler. Geriye dönük uyumluluk için SAM, eski ve verimsiz türleri varsayılan olarak kullanır, bu nedenle tüm istemciler daha yeni türleri belirtmelidir.

İmza türü, DEST GENERATE ve SESSION CREATE (geçici için) komutlarında belirtilir. Tüm istemciler `SIGNATURE_TYPE=7` (Ed25519) ayarını yapmalıdır.

Şifreleme türü SESSION CREATE komutunda belirtilir. Birden fazla şifreleme türüne izin verilir. İstemciler ya `i2cp.leaseSetEncType=4` (yalnızca ECIES-X25519 için) ya da `i2cp.leaseSetEncType=4,0` (uyumluluk gerekiyorsa ECIES-X25519 ve ElGamal için) ayarlamalıdır.

## Sürüm 3 Değişiklikleri

### Sürüm 3.0 Değişiklikleri

Sürüm 3.0, I2P sürüm 0.7.3'te tanıtıldı. SAM v2, aynı I2P hedefinde birden fazla soketin *paralel* olarak yönetilmesi için bir yol sağlıyordu, yani istemcinin bir sokette veri göndermeyi başarıyla tamamlamasını beklemeden başka bir sokette veri gönderebiliyordu. Ancak tüm veriler aynı istemci-SAM soketi üzerinden geçiyordu, bu da istemci için yönetimi oldukça karmaşık hale getiriyordu.

SAM v3 soketleri farklı bir şekilde yönetir: her *I2P soketi* benzersiz bir istemci-SAM soketi ile eşleşir, bu da işlenmesi çok daha basittir. Bu [BOB](/docs/api/bob) ile benzerdir.

SAMv3 ayrıca I2P üzerinden datagram göndermek için bir UDP portu sunar ve I2P datagramlarını istemcinin datagram sunucusuna geri yönlendirebilir.

### Sürüm 3.1 Değişiklikleri

Versiyon 3.1, Java I2P sürüm 0.9.14'te (Temmuz 2014) tanıtıldı. SAM 3.1, SAM 3.0'dan daha iyi imza türlerini desteklemesi nedeniyle önerilen minimum SAM uygulamasıdır. i2pd de çoğu 3.1 özelliğini destekler.

- DEST GENERATE ve SESSION CREATE artık SIGNATURE_TYPE parametresini destekliyor.
- HELLO VERSION'daki MIN ve MAX parametreleri artık isteğe bağlı.
- HELLO VERSION'daki MIN ve MAX parametreleri artık "3" gibi tek haneli sürümleri destekliyor.
- RAW SEND artık bridge socket'inde destekleniyor.

### Sürüm 3.2 Değişiklikleri

Sürüm 3.2, Java I2P sürümü 0.9.24'te (Ocak 2016) tanıtıldı. i2pd'nin şu anda 3.2 özelliklerinin çoğunu desteklemediğini unutmayın.

#### I2CP Port ve Protokol Desteği

- SESSION CREATE seçenekleri FROM_PORT ve TO_PORT
- SESSION CREATE STYLE=RAW seçeneği PROTOCOL
- STREAM CONNECT, DATAGRAM SEND ve RAW SEND seçenekleri FROM_PORT ve TO_PORT
- RAW SEND seçeneği PROTOCOL
- DATAGRAM RECEIVED, RAW RECEIVED ve iletilen veya alınan akışlar ile yanıtlanabilir datagramlar, FROM_PORT ve TO_PORT içerir
- RAW oturum seçeneği HEADER=true, iletilen ham datagramların PROTOCOL=nnn FROM_PORT=nnnn TO_PORT=nnnn içeren bir satırla başlangıçta eklenmesine neden olur
- 7655 portu üzerinden gönderilen datagramların ilk satırı artık herhangi bir 3.x sürümüyle başlayabilir
- 7655 portu üzerinden gönderilen datagramların ilk satırı FROM_PORT, TO_PORT, PROTOCOL seçeneklerinden herhangi birini içerebilir
- RAW RECEIVED, PROTOCOL=nnn içerir

#### SSL ve Kimlik Doğrulama

- Yetkilendirme için HELLO parametrelerinde USER/PASSWORD. [Aşağıya](#authorization) bakınız.
- AUTH komutu ile isteğe bağlı yetkilendirme yapılandırması. [Aşağıya](#authorization-configuration-sam-32-or-higher-optional-feature) bakınız.
- Kontrol soketinde isteğe bağlı SSL/TLS desteği. [Aşağıya](#ssl) bakınız.
- STREAM FORWARD seçeneği SSL=true

#### Çoklu İş Parçacığı

- Aynı oturum kimliğinde eşzamanlı bekleyen STREAM ACCEPT'ler izin verilir.

#### Komut Satırı Ayrıştırma ve Canlı Tutma

- Oturumu ve soketi kapatmak için isteğe bağlı QUIT, STOP ve EXIT komutları. [Aşağıya](#quitstopexitinvisible-sam-32-or-higher-optional-features) bakınız.
- Komut ayrıştırma UTF-8'i düzgün şekilde işleyecektir
- Komut ayrıştırma tırnak işaretleri içindeki boşlukları güvenilir şekilde işler
- Ters eğik çizgi '\\' komut satırında tırnak işaretlerini kaçırabilir
- Sunucunun komutları büyük harfle eşlemesi önerilir, telnet ile test kolaylığı için.
- PROTOCOL veya PROTOCOL= gibi boş seçenek değerlerine izin verilebilir, implementasyona bağlıdır.
- Canlı tutmak için PING/PONG. Aşağıya bakınız.
- Sunucular HELLO veya sonraki komutlar için zaman aşımı implementasyonu uygulayabilir, implementasyona bağlıdır.

### Sürüm 3.3 Değişiklikleri

Versiyon 3.3, Java I2P sürümü 0.9.25 (Mart 2016) ile tanıtıldı. i2pd'nin şu anda 3.3 özelliklerinin çoğunu desteklemediğini unutmayın.

- Aynı oturum stream'ler, datagram'lar ve raw için eş zamanlı olarak kullanılabilir. Gelen paketler ve stream'ler I2P protokolü ve to-port temelinde yönlendirilecektir. [Aşağıdaki PRIMARY bölümüne bakın](#sam-primary-sessions-v33-and-higher).
- DATAGRAM SEND ve RAW SEND artık SEND_TAGS, TAG_THRESHOLD, EXPIRES ve SEND_LEASESET seçeneklerini desteklemektedir. [Aşağıdaki datagram gönderme bölümüne bakın](#sending-repliable-or-raw-datagrams).

## Sürüm 3 Protokolü

### Basit Anonim Mesajlaşma (SAM) Sürüm 3.3 Spesifikasyon Genel Bakışı

İstemci uygulaması, tüm I2P işlevlerini yöneten SAM köprüsüyle iletişim kurar (sanal akışlar için [streaming kütüphanesi](/docs/api/streaming) veya datagramlar için doğrudan [I2CP](/docs/protocol/i2cp) kullanarak).

Varsayılan olarak, istemci-SAM bridge iletişimi şifrelenmemiş ve kimlik doğrulamasızdır. SAM bridge SSL/TLS bağlantılarını destekleyebilir; yapılandırma ve uygulama detayları bu spesifikasyonun kapsamı dışındadır. SAM 3.2 itibariyle, ilk el sıkışmada isteğe bağlı kimlik doğrulama kullanıcı/şifre parametreleri desteklenir ve bridge tarafından gerekli olabilir.

I2P iletişimi birkaç farklı biçim alabilir:

- [Sanal akışlar](/docs/api/streaming)
- [Yanıtlanabilir ve kimlik doğrulamalı datagramlar](/docs/specs/datagrams#repliable) (FROM alanı olan mesajlar)
- [Anonim datagramlar](/docs/specs/datagrams#raw) (ham anonim mesajlar)
- [Datagram2](/docs/specs/datagrams#datagram2) (yeni yanıtlanabilir ve kimlik doğrulamalı format)
- [Datagram3](/docs/specs/datagrams#datagram3) (yeni yanıtlanabilir ancak kimlik doğrulamasız format)

I2P iletişimi I2P oturumları tarafından desteklenir ve her I2P oturumu bir adrese (destination olarak adlandırılır) bağlıdır. Bir I2P oturumu yukarıdaki üç türden biri ile ilişkilendirilir ve [PRIMARY oturumları](#sam-primary-sessions-v33-and-higher) kullanmadığı sürece başka türde iletişim taşıyamaz.

### Kodlama ve Kaçış Karakterleri

Tüm bu SAM mesajları tek bir satırda gönderilir ve yeni satır karakteri (\\n) ile sonlandırılır. SAM 3.2 öncesinde yalnızca 7-bit ASCII destekleniyordu. SAM 3.2 itibariyle, kodlama UTF-8 olmalıdır. UTF8 kodlamalı herhangi bir anahtar veya değer çalışmalıdır.

Bu spesifikasyonda aşağıda gösterilen biçimlendirme yalnızca okunabilirlik içindir ve her mesajdaki ilk iki kelimenin belirli sıralarında kalması gerekirken, key=value çiftlerinin sıralaması değişebilir (örn. "ONE TWO A=B C=D" veya "ONE TWO C=D A=B" her ikisi de tamamen geçerli yapılardır). Buna ek olarak, protokol büyük/küçük harf duyarlıdır. Aşağıda, mesaj örnekleri istemci tarafından SAM bridge'e gönderilen mesajlar için "->" ile ve SAM bridge tarafından istemciye gönderilen mesajlar için "<-" ile başlatılmıştır.

Temel komut veya yanıt satırı aşağıdaki formlardan birini alır:

```
COMMAND SUBCOMMAND [key=value] [key=value] ...
COMMAND                                           # As of SAM 3.2
PING[ arbitrary text]                             # As of SAM 3.2
PONG[ arbitrary text]                             # As of SAM 3.2
```
SUBCOMMAND olmadan COMMAND yalnızca SAMv3.2'deki bazı yeni komutlar için desteklenir.

Key=değer çiftleri tek boşlukla ayrılmalıdır. (SAM 3.2 itibariyle, birden fazla boşluğa izin verilir) Değerler boşluk içeriyorsa çift tırnak içine alınmalıdır, örneğin key="uzun değer metni". (SAM 3.2 öncesinde, bu bazı uygulamalarda güvenilir şekilde çalışmıyordu)

SAM 3.2'den önce herhangi bir kaçış mekanizması yoktu. SAM 3.2 itibariyle, çift tırnak işaretleri ters eğik çizgi '\\' ile kaçışlanabilir ve ters eğik çizgi iki ters eğik çizgi '\\\\' olarak temsil edilebilir.

### Boş Değerler

SAM 3.2 itibariyle, KEY, KEY=, veya KEY="" gibi boş seçenek değerlerine izin verilebilir, implementasyona bağlıdır.

### Büyük/Küçük Harf Duyarlılığı

Protokol, belirtildiği şekilde büyük-küçük harf duyarlıdır. Sunucunun, telnet üzerinden test kolaylığı için komutları büyük harfe dönüştürmesi önerilir ancak zorunlu değildir. Bu, örneğin "hello version" komutunun çalışmasını sağlar. Bu uygulama bağımlıdır. Anahtarları veya değerleri büyük harfe dönüştürmeyin, çünkü bu [I2CP](/docs/protocol/i2cp) seçeneklerini bozar.

### SAM Bağlantı El Sıkışması

İstemci ve köprü bir protokol sürümünde anlaşana kadar hiçbir SAM iletişimi gerçekleşemez; bu, istemcinin bir HELLO göndermesi ve köprünün bir HELLO REPLY göndermesi ile yapılır:

```
->  HELLO VERSION
          [MIN=$min]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [MAX=$max]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [USER="xxx"]          # As of SAM 3.2, required if authentication is enabled, see below
          [PASSWORD="yyy"]      # As of SAM 3.2, required if authentication is enabled, see below
```
ve

```
<-  HELLO REPLY RESULT=OK VERSION=3.1
```
Sürüm 3.1 (I2P 0.9.14) itibariyle, MIN ve MAX parametreleri isteğe bağlıdır. SAM her zaman MIN ve MAX kısıtlamaları göz önünde bulundurularak mümkün olan en yüksek sürümü döndürecektir, veya hiçbir kısıtlama verilmemişse mevcut sunucu sürümünü döndürecektir.

SAM bridge uygun bir sürüm bulamazsa, şu şekilde yanıtlar:

```
<- HELLO REPLY RESULT=NOVERSION
```
Kötü istek formatı gibi bir hata oluşursa, şu yanıtı verir:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
#### SSL

Sunucunun kontrol soketi, sunucu ve istemcide yapılandırıldığı şekilde isteğe bağlı olarak SSL/TLS desteği sunabilir. Uygulamalar başka aktarım katmanları da sunabilir; bu, protokol tanımının kapsamı dışındadır.

#### Yetkilendirme

Yetkilendirme için, istemci HELLO parametrelerine USER="xxx" PASSWORD="yyy" ekler. Kullanıcı ve şifre için çift tırnak önerilir ancak zorunlu değildir. Kullanıcı veya şifre içindeki çift tırnak ters eğik çizgi ile kaçırılmalıdır. Başarısızlık durumunda sunucu I2P_ERROR ve bir mesaj ile yanıt verecektir. Yetkilendirmenin gerekli olduğu SAM sunucularında SSL'in etkinleştirilmesi önerilir.

#### Zaman Aşımları

Sunucular, HELLO veya sonraki komutlar için zaman aşımları uygulayabilir, bu uygulama bağımlıdır. İstemciler bağlandıktan sonra derhal HELLO ve bir sonraki komutu göndermelidir.

HELLO alınmadan önce bir zaman aşımı meydana gelirse, bridge şu yanıtla cevap verir:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
ve ardından bağlantıyı keser.

Eğer HELLO alındıktan sonra ancak bir sonraki komuttan önce bir zaman aşımı meydana gelirse, köprü şu şekilde yanıtlar:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
ve ardından bağlantıyı keser.

### I2CP Portları ve Protokolü

SAM 3.2 itibariyle, [I2CP](/docs/protocol/i2cp) portları ve protokolü SAM istemci gönderici tarafından [I2CP](/docs/protocol/i2cp)'ye geçirilmek üzere belirtilebilir ve SAM köprüsü alınan [I2CP](/docs/protocol/i2cp) port ve protokol bilgilerini SAM istemcisine iletecektir.

FROM_PORT ve TO_PORT için geçerli aralık 0-65535'tir ve varsayılan değer 0'dır.

Yalnızca RAW için belirtilebilen PROTOCOL için, geçerli aralık 0-255'tir ve varsayılan değer 18'dir.

SESSION komutları için, belirtilen portlar ve protokol o oturum için varsayılan değerlerdir. Bireysel akışlar veya datagramlar için, belirtilen portlar ve protokol oturum varsayılanlarını geçersiz kılar. Alınan akışlar veya datagramlar için, belirtilen portlar ve protokol [I2CP](/docs/protocol/i2cp)'den alındığı gibidir.

#### Standart IP'den Önemli Farklar

I2CP portları I2P soketleri ve datagramları içindir. SAM'e bağlanan yerel soketlerinizle ilgili değildirler.

- Port 0 geçerlidir ve özel anlamı vardır.
- 1-1023 portları özel veya ayrıcalıklı değildir.
- Sunucular varsayılan olarak port 0'da dinler, bu "tüm portlar" anlamına gelir.
- İstemciler varsayılan olarak port 0'a gönderir, bu "herhangi bir port" anlamına gelir.
- İstemciler varsayılan olarak port 0'dan gönderir, bu "belirtilmemiş" anlamına gelir.
- Sunucular port 0'da bir hizmet ve daha yüksek portlarda başka hizmetler çalıştırabilir. Bu durumda, port 0 hizmeti varsayılan hizmettir ve gelen soket veya datagram portu başka bir hizmetle eşleşmezse buna bağlanılacaktır.
- Çoğu I2P hedefinde sadece bir hizmet çalıştığından, varsayılanları kullanabilir ve I2CP port yapılandırmasını görmezden gelebilirsiniz.
- I2CP portlarını belirtmek için SAM 3.2 veya 3.3 gereklidir.
- I2CP portlarına ihtiyacınız yoksa, SAM 3.2 veya 3.3'e ihtiyacınız yoktur; 3.1 yeterlidir.
- Protocol 0 geçerlidir ve "herhangi bir protokol" anlamına gelir. Bu önerilmez ve muhtemelen çalışmayacaktır.
- I2P soketleri dahili bir bağlantı ID'si ile takip edilir. Bu nedenle, dest:port:dest:port:protocol 5'li grubunun benzersiz olması gerekmez. Örneğin, iki hedef arasında aynı portlara sahip birden fazla soket olabilir. İstemcilerin giden bağlantı için "boş port" seçmesi gerekmez.

Birden fazla alt oturuma sahip bir SAM 3.3 uygulaması tasarlıyorsanız, port ve protokolleri nasıl etkili bir şekilde kullanacağınızı dikkatli bir şekilde düşünün. Daha fazla bilgi için [I2CP](/docs/protocol/i2cp) özelliklerine bakın.

### SAM Oturumları

Bir SAM oturumu, bir istemcinin SAM köprüsüne bir soket açması, bir el sıkışma işlemi gerçekleştirmesi ve bir SESSION CREATE mesajı göndermesiyle oluşturulur ve soket bağlantısı kesildiğinde oturum sonlanır.

Kayıtlı her I2P Destination benzersiz bir session ID (veya takma ad) ile ilişkilendirilir. PRIMARY session'lar için alt session ID'ler dahil olmak üzere session ID'ler, SAM sunucusunda global olarak benzersiz olmalıdır. Diğer istemcilerle olası ID çakışmalarını önlemek için, en iyi uygulama istemcinin ID'leri rastgele oluşturmasıdır.

Her oturum şununla benzersiz şekilde ilişkilendirilir:

- istemcinin oturumu oluşturduğu soket
- onun ID'si (veya takma adı)

#### Oturum Oluşturma İsteği

Oturum oluşturma mesajı yalnızca bu formlardan birini kullanabilir (diğer formlar aracılığıyla alınan mesajlara hata mesajı ile yanıt verilir):

```
->  SESSION CREATE
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, for DESTINATION=TRANSIENT only, default DSA_SHA1
          [PORT=$port]                         # Required for DATAGRAM* RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [HEADER={true,false}]                # SAM 3.2 or higher only, for STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
DESTINATION, mesaj/akış gönderme ve alma için hangi destinasyonun kullanılacağını belirtir. $privkey, [Destination](/docs/specs/common-structures#type_Destination)'ın ardından [Private Key](/docs/specs/common-structures#type_PrivateKey)'in ardından [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey)'in birleştirilmesinin base 64'üdür, isteğe bağlı olarak [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) takip eder. Bu, imza türüne bağlı olarak binary formatında 663 veya daha fazla byte, base 64'te ise 884 veya daha fazla byte'tır. Binary format Private Key File'da belirtilmiştir. Aşağıdaki Destination Key Generation bölümünde [Private Key](/docs/specs/common-structures#type_PrivateKey) hakkında ek notlara bakın.

İmzalama private key tamamen sıfırlardan oluşuyorsa, [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) bölümü takip eder. Offline imzalar yalnızca STREAM ve RAW oturumları için desteklenir. Offline imzalar DESTINATION=TRANSIENT ile oluşturulamaz. Offline imza bölümünün formatı şöyledir:

1. Sona erme zaman damgası (4 bayt, big endian, epoch'tan bu yana saniye, 2106'da döner)
2. Geçici Signing Public Key'in sig türü (2 bayt, big endian)
3. Geçici Signing Public key (geçici sig türü tarafından belirtilen uzunluk)
4. Yukarıdaki üç alanın çevrimdışı anahtar tarafından imzası (hedef sig türü tarafından belirtilen uzunluk)
5. Geçici Signing Private key (geçici sig türü tarafından belirtilen uzunluk)

Hedef TRANSIENT olarak belirtilirse, SAM bridge yeni bir hedef oluşturur. Sürüm 3.1 (I2P 0.9.14) itibariyle, hedef TRANSIENT ise, isteğe bağlı bir SIGNATURE_TYPE parametresi desteklenir. SIGNATURE_TYPE değeri, [Key Certificates](/docs/specs/common-structures#type_Certificate) tarafından desteklenen herhangi bir ad (örneğin ECDSA_SHA256_P256, büyük/küçük harf duyarsız) veya sayı (örneğin 1) olabilir. Varsayılan DSA_SHA1'dir ve bu istediğiniz şey DEĞİLDİR. Çoğu uygulama için lütfen SIGNATURE_TYPE=7 belirtin.

$nickname istemcinin seçimidir. Boşluk karakterine izin verilmez.

Verilen ek seçenekler, SAM köprüsü tarafından yorumlanmadığı takdirde I2P oturum yapılandırmasına aktarılır (örn. outbound.length=0).

Java I2P ve i2pd router'ları tunnel miktarları için farklı varsayılanlara sahiptir. Java varsayılanı 2'dir ve i2pd varsayılanı 5'tir. Çoğu düşük-orta bant genişliği ve düşük-orta bağlantı sayısı için 2 veya 3 yeterlidir. Java I2P ve i2pd router'ları ile tutarlı performans elde etmek için SESSION CREATE mesajında tunnel miktarlarını belirtin, örneğin inbound.quantity=3 outbound.quantity=3 seçeneklerini kullanarak. Bu ve diğer seçenekler [aşağıdaki bağlantılarda belgelenmiştir](#tunnel-i2cp-and-streaming-options).

SAM bridge'in kendisi zaten I2P üzerinden hangi router ile iletişim kurması gerektiği konusunda yapılandırılmış olmalıdır (gerekirse bir geçersiz kılma yöntemi olabilir, örneğin i2cp.tcp.host=localhost ve i2cp.tcp.port=7654).

#### Oturum Oluşturma Yanıtı

Session oluşturma mesajını aldıktan sonra, SAM bridge aşağıdaki gibi bir session durum mesajı ile yanıt verecektir:

Oluşturma başarılı olduysa:

```
<-  SESSION STATUS RESULT=OK DESTINATION=$privkey
```
$privkey, [Destination](/docs/specs/common-structures#type_Destination)'ı takiben [Private Key](/docs/specs/common-structures#type_PrivateKey)'i takiben [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey)'i ve isteğe bağlı olarak [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature)'ı takip eden birleştirmenin base 64'üdür. Bu, imza türüne bağlı olarak ikili formatta 663 veya daha fazla bayt ve base 64'te 884 veya daha fazla bayttır. İkili format Private Key File'da belirtilmiştir.

Eğer SESSION CREATE tamamı sıfırlardan oluşan bir imzalama özel anahtarı ve bir [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) bölümü içeriyorsa, SESSION STATUS yanıtı aynı verileri aynı formatta içerecektir. Ayrıntılar için yukarıdaki SESSION CREATE bölümüne bakın.

Takma ad zaten bir oturumla ilişkilendirilmişse:

```
<-  SESSION STATUS RESULT=DUPLICATED_ID
```
Hedef zaten kullanımdaysa:

```
<-  SESSION STATUS RESULT=DUPLICATED_DEST
```
Hedef geçerli bir özel hedef anahtarı değilse:

```
<-  SESSION STATUS RESULT=INVALID_KEY
```
Başka bir hata oluştuysa:

```
<-  SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
Eğer sorun varsa, MESSAGE oturum neden oluşturulamadığına dair insan tarafından okunabilir bilgiler içermelidir.

Router'ın SESSION STATUS ile yanıt vermeden önce tunnel'ları oluşturduğunu unutmayın. Bu işlem birkaç saniye sürebilir veya router başlangıcında ya da ciddi ağ tıkanıklığı sırasında bir dakika veya daha fazla zaman alabilir. Başarısız olursa, router birkaç dakika boyunca bir hata mesajı ile yanıt vermeyecektir. Yanıt beklerken kısa bir zaman aşımı ayarlamayın. Tunnel oluşturma işlemi devam ederken oturumu bırakıp tekrar denemeyin.

SAM oturumları, kendileriyle ilişkilendirildikleri soket ile birlikte yaşar ve ölür. Soket kapatıldığında oturum ölür ve oturumu kullanan tüm iletişimler aynı anda kesilir. Bunun tersi de geçerlidir; oturum herhangi bir nedenle öldüğünde, SAM köprüsü soketi kapatır.

### SAM Sanal Akışları

Sanal akışların güvenilir bir şekilde ve sırayla gönderilmesi garanti edilir, başarı ve başarısızlık bildirimleri mevcut olur olmaz iletilir.

Stream'ler iki I2P hedefi arasındaki çift yönlü iletişim soketleridir, ancak açılmaları bunlardan biri tarafından talep edilmelidir. Bundan sonra, CONNECT komutları SAM istemcisi tarafından böyle bir talep için kullanılır. FORWARD / ACCEPT komutları, SAM istemcisi diğer I2P hedeflerinden gelen talepleri dinlemek istediğinde kullanılır.

### SAM Sanal Akışları: CONNECT

Bir istemci şu şekilde bağlantı talep eder:

- SAM bridge ile yeni bir socket açmak
- yukarıdakiyle aynı HELLO handshake'ini geçirmek
- STREAM CONNECT komutunu göndermek

#### Bağlantı İsteği

```
-> STREAM CONNECT
         ID=$nickname
         DESTINATION=$destination
         [SILENT={true,false}]                # default false
         [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
         [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
```
Bu, ID'si $nickname olan yerel oturumdan belirtilen eşe yeni bir sanal bağlantı kurar.

Hedef $destination'dır, bu da [Destination](/docs/specs/common-structures#type_Destination)'ın base 64'üdür ve imza türüne bağlı olarak 516 veya daha fazla base 64 karakteri (binary'de 387 veya daha fazla bayt) içerir.

**NOT:** Yaklaşık 2014'ten beri (SAM v3.1), Java I2P ayrıca $destination için hostname'leri ve b32 adreslerini desteklemiştir, ancak bu daha önce belgelenmemişti. Hostname'ler ve b32 adresleri artık 0.9.48 sürümü itibariyle Java I2P tarafından resmi olarak desteklenmektedir. i2pd router, 2.38.0 (0.9.50) sürümü itibariyle hostname'leri ve b32 adreslerini desteklemektedir. Her iki router için de "b32" desteği, blinded destination'lar için genişletilmiş "b33" adreslerinin desteğini de içerir.

#### Bağlantı Yanıtı

SILENT=true parametresi geçirilirse, SAM bridge soket üzerinde başka hiçbir mesaj göndermez. Bağlantı başarısız olursa, soket kapatılır. Bağlantı başarılı olursa, mevcut soket üzerinden geçen tüm kalan veri, bağlı I2P hedef peer'dan ve peer'a iletilir.

SILENT=false ise, ki bu varsayılan değerdir, SAM bridge soketi yönlendirmeden veya kapatmadan önce istemcisine son bir mesaj gönderir:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
RESULT değeri şunlardan biri olabilir:

```
OK
CANT_REACH_PEER
I2P_ERROR
INVALID_KEY
INVALID_ID
TIMEOUT
```
RESULT OK ise, mevcut soket üzerinden geçen tüm kalan veri, bağlı I2P hedef eşinden ve eşine iletilir. Bağlantı mümkün değilse (zaman aşımı vb.), RESULT uygun hata değerini içerecektir (isteğe bağlı insan tarafından okunabilir MESSAGE ile birlikte) ve SAM köprüsü soketi kapatır.

Router akış bağlantısı zaman aşımı dahili olarak yaklaşık bir dakikadır ve uygulamaya bağlıdır. Yanıt beklerken daha kısa bir zaman aşımı ayarlamayın.

### SAM Sanal Akışları: ACCEPT

Bir istemci, gelen bağlantı isteğini şu şekilde bekler:

- SAM bridge ile yeni bir soket açma
- yukarıdaki ile aynı HELLO el sıkışmasını geçirme
- STREAM ACCEPT komutunu gönderme

#### İsteği Kabul Et

```
-> STREAM ACCEPT
         ID=$nickname
         [SILENT={true,false}]                # default false
```
Bu, ${nickname} oturumunun I2P ağından gelen bir bağlantı isteğini dinlemesini sağlar. Oturumda aktif bir FORWARD varken ACCEPT komutuna izin verilmez.

SAM 3.2 itibariyle, aynı oturum kimliğinde (hatta aynı port ile bile) birden fazla eşzamanlı bekleyen STREAM ACCEPT'e izin verilmektedir. 3.2 öncesinde, eşzamanlı accept'ler ALREADY_ACCEPTING ile başarısız olurdu. Not: Java I2P ayrıca 0.9.24 sürümünden itibaren (2016-01) SAM 3.1'de eşzamanlı ACCEPT'leri destekler. i2pd de 2.50.0 sürümünden itibaren (2023-12) SAM 3.1'de eşzamanlı ACCEPT'leri destekler.

#### Yanıt Kabul Et

SILENT=true geçilirse, SAM bridge socket üzerinde başka herhangi bir mesaj göndermez. Kabul başarısız olursa, socket kapatılır. Kabul başarılı olursa, mevcut socket üzerinden geçen tüm kalan veri, bağlı I2P destination peer'ına ve peer'ından iletilir. Güvenilirlik için ve gelen bağlantılar için destination bilgisini almak için SILENT=false önerilir.

SILENT=false ise, ki bu varsayılan değerdir, SAM bridge şu şekilde yanıtlar:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
RESULT değeri şunlardan biri olabilir:

```
OK
I2P_ERROR
INVALID_ID
```
Sonuç OK değilse, soket SAM köprüsü tarafından derhal kapatılır. Sonuç OK ise, SAM köprüsü başka bir I2P eşinden gelen bağlantı isteğini beklemeye başlar. Bir istek geldiğinde, SAM köprüsü onu kabul eder ve:

Eğer SILENT=true parametresi geçirildiyse, SAM köprüsü istemci soketinde başka hiçbir mesaj göndermez. Mevcut soketten geçen tüm kalan veriler, bağlı I2P hedef eşinden ve ona doğru iletilir.

Eğer varsayılan değer olan SILENT=false geçildiyse, SAM köprüsü istemciye talep eden eşin base64 genel hedef anahtarını içeren bir ASCII satırı ve yalnızca SAM 3.2 için ek bilgiler gönderir:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Bu '\\n' ile sonlandırılan satırdan sonra, mevcut soket üzerinden geçen tüm kalan veri, eşlerden biri soketi kapatana kadar bağlı I2P hedef eşinden ve eşine iletilir.

#### OK'dan Sonra Hatalar

Nadir durumlarda, SAM bridge RESULT=OK gönderdikten sonra ancak bir bağlantı gelmeden ve istemciye $destination satırı göndermeden önce bir hatayla karşılaşabilir. Bu hatalar router kapatma, router yeniden başlatma ve oturum kapatma durumlarını içerebilir. Bu durumlarda, SILENT=false olduğunda, SAM bridge aşağıdaki satırı gönderebilir (ancak göndermek zorunda değildir, uygulama bağımlıdır):

```
<-  STREAM STATUS
         RESULT=I2P_ERROR
         [MESSAGE=...]
```
socket'i hemen kapatmadan önce. Bu satır, tabii ki, geçerli bir Base 64 hedefi olarak çözümlenebilir değildir.

### SAM Sanal Akışları: FORWARD

Bir istemci düzenli bir socket sunucusu kullanabilir ve I2P'den gelen bağlantı isteklerini bekleyebilir. Bunun için istemci şunları yapmalıdır:

- SAM bridge ile yeni bir soket aç
- yukarıdaki ile aynı HELLO el sıkışmasını geçir
- forward komutunu gönder

#### İleri Yönlendirme İsteği

```
-> STREAM FORWARD
         ID=$nickname
         PORT=$port
         [HOST=$host]
         [SILENT={true,false}]                # default false
         [SSL={true,false}]                   # SAM 3.2 or higher only, default false
```
Bu, ${nickname} oturumunun I2P ağından gelen bağlantı isteklerini dinlemesini sağlar. Oturumda bekleyen bir ACCEPT varken FORWARD'a izin verilmez.

#### İleri Yanıt

SILENT varsayılan olarak false değerindedir. SILENT true veya false olsun, SAM bridge her zaman bir STREAM STATUS mesajı ile yanıt verir. Bunun SILENT=true olduğunda STREAM ACCEPT ve STREAM CONNECT'ten farklı bir davranış olduğunu unutmayın. STREAM STATUS mesajı şöyledir:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
RESULT değeri şunlardan biri olabilir:

```
OK
I2P_ERROR
INVALID_ID
```
$host, SAM'in bağlantı isteklerini ileteceği socket sunucusunun hostname veya IP adresidir. Verilmezse, SAM forward komutunu veren socket'in IP'sini alır.

$port, SAM'in bağlantı isteklerini ileteceği soket sunucusunun port numarasıdır. Zorunludur.

I2P'den bir bağlantı isteği geldiğinde, SAM bridge $host:$port adresine bir soket bağlantısı açar. Eğer 3 saniyeden kısa sürede kabul edilirse, SAM I2P'den gelen bağlantıyı kabul eder ve ardından:

Eğer SILENT=true geçirildiyse, elde edilen mevcut socket üzerinden geçen tüm veriler, bağlı I2P hedef eşinden gelen ve ona giden şekilde iletilir.

SILENT=false değeri geçirilmişse (ki bu varsayılan değerdir), SAM köprüsü elde edilen soket üzerinden, istekte bulunan eşin base64 genel hedef anahtarını içeren bir ASCII satırı ve yalnızca SAM 3.2 için ek bilgiler gönderir:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Bu '\\n' ile sonlandırılan satırdan sonra, soket üzerinden geçen kalan tüm veri, taraflardan biri soketi kapatana kadar bağlı I2P destination eşinden ve eşine iletilir.

SAM 3.2 itibariyle, SSL=true belirtilirse, yönlendirme soketi SSL/TLS üzerinden olur.

I2P router, "forwarding" soketi kapatılır kapatılmaz gelen bağlantı isteklerini dinlemeyi durduracaktır.

### SAM Datagramları

SAMv3, yerel datagram soketleri üzerinden datagram gönderme ve alma mekanizmaları sağlar. Bazı SAMv3 uygulamaları ayrıca SAM köprü soketi üzerinden datagram gönderme/alma işlemlerinin eski v1/v2 yöntemini de destekler. Her ikisi de aşağıda belgelenmiştir.

I2P dört türde datagram destekler:

- Yanıtlanabilir ve kimliği doğrulanmış datagramlar, gönderenin hedefi ile önek alır ve gönderenin imzasını içerir, böylece alıcı gönderenin hedefinin sahte olmadığını doğrulayabilir ve datagram'a yanıt verebilir. Yeni Datagram2 formatı da yanıtlanabilir ve kimliği doğrulanmıştır.
- Yeni Datagram3 formatı yanıtlanabilir ancak kimliği doğrulanmamıştır. Gönderen bilgisi doğrulanmamıştır.
- Ham datagramlar gönderenin hedefini veya imzasını içermez.

Hem yanıtlanabilir hem de ham datagramlar için varsayılan I2CP portları tanımlanmıştır. Ham datagramlar için I2CP portu değiştirilebilir.

Yaygın bir protokol tasarım deseni, tanımlayıcı içeren yanıtlanabilir datagramların sunuculara gönderilmesi ve sunucunun bu tanımlayıcıyı içeren ham bir datagram ile yanıt vermesidir, böylece yanıt talep ile ilişkilendirilebilir. Bu tasarım deseni, yanıtlardaki yanıtlanabilir datagramların önemli yükünü ortadan kaldırır. Tüm I2CP protokol ve port seçimleri uygulamaya özgüdür ve tasarımcılar bu konuları dikkate almalıdır.

Aşağıdaki bölümde datagram MTU ile ilgili önemli notlara da bakınız.

#### Yanıtlanabilir veya Ham Datagram Gönderme

I2P doğası gereği bir FROM adresi içermese de, kullanım kolaylığı için yanıtlanabilir datagramlar olarak ek bir katman sağlanır - FROM adresi içeren 31744 bayta kadar sırasız ve güvenilmez mesajlar (başlık materyali için 1KB'ye kadar yer bırakır). Bu FROM adresi SAM tarafından dahili olarak doğrulanır (kaynağı doğrulamak için destination'ın imzalama anahtarını kullanır) ve tekrar oynatma koruması içerir.

Minimum boyut 1'dir. En iyi teslimat güvenilirliği için önerilen maksimum boyut yaklaşık 11 KB'dir. Güvenilirlik mesaj boyutuyla ters orantılıdır, hatta muhtemelen üssel olarak.

STYLE=DATAGRAM veya STYLE=RAW ile bir SAM oturumu kurduktan sonra, istemci SAM'in UDP portu üzerinden (varsayılan olarak 7655) yanıtlanabilir veya ham datagramlar gönderebilir.

Bu port üzerinden gönderilen bir datagram'ın ilk satırı aşağıdaki formatta olmalıdır. Bu tek satırdır (boşlukla ayrılmış), netlik için birden fazla satırda gösterilmiştir:

```
3.0                                  # As of SAM 3.2, any "3.x" is allowed. Prior to that, "3.0" is required.
$nickname
$destination
[FROM_PORT=nnn]                      # SAM 3.2 or higher only, default from session options
[TO_PORT=nnn]                        # SAM 3.2 or higher only, default from session options
[PROTOCOL=nnn]                       # SAM 3.2 or higher only, only for RAW sessions, default from session options
[SEND_TAGS=nnn]                      # SAM 3.3 or higher only, number of session tags to send
                                     # Overrides crypto.tagsToSend I2CP session option
                                     # Default is router-dependent (40 for Java router)
[TAG_THRESHOLD=nnn]                  # SAM 3.3 or higher only, low session tag threshold
                                     # Overrides crypto.lowTagThreshold I2CP session option
                                     # Default is router-dependent (30 for Java router)
[EXPIRES=nnn]                        # SAM 3.3 or higher only, expiration from now in seconds
                                     # Overrides clientMessageTimeout I2CP session option (which is in ms)
                                     # Default is router-dependent (60 for Java router)
[SEND_LEASESET={true,false}]         # SAM 3.3 or higher only, whether to send our leaseset
                                     # Overrides shouldBundleReplyInfo I2CP session option
                                     # Default is true
\n
```
- 3.0, SAM'ın sürümüdür. SAM 3.2'den itibaren, herhangi bir 3.x sürümüne izin verilir.
- $nickname, kullanılacak DATAGRAM oturumunun kimliğidir
- Hedef $destination'dır, bu [Destination](/docs/specs/common-structures#type_Destination)'ın base 64 kodlamasıdır ve imza türüne bağlı olarak 516 veya daha fazla base 64 karakter (ikili formatta 387 veya daha fazla bayt) içerir. **NOT:** Yaklaşık 2014'ten beri (SAM v3.1), Java I2P ayrıca $destination için hostname'leri ve b32 adreslerini desteklemiştir, ancak bu daha önce belgelenmemişti. Hostname'ler ve b32 adresleri artık Java I2P tarafından 0.9.48 sürümü itibariyle resmi olarak desteklenmektedir. i2pd router şu anda hostname'leri ve b32 adreslerini desteklememektedir; destek gelecekteki bir sürümde eklenebilir.
- Tüm seçenekler, SESSION CREATE'de belirtilen varsayılan ayarları geçersiz kılan datagram başına ayarlardır.
- Sürüm 3.3 seçenekleri SEND_TAGS, TAG_THRESHOLD, EXPIRES ve SEND_LEASESET, destekleniyorsa [I2CP](/docs/protocol/i2cp)'ye aktarılacaktır. Ayrıntılar için [I2CP spesifikasyonuna](/docs/protocol/i2cp#msg_SendMessageExpire) bakın. SAM sunucusu tarafından destek isteğe bağlıdır, desteklenmiyorsa bu seçenekleri yok sayacaktır.
- bu satır '\\n' ile sonlandırılır.

İlk satır, mesajın kalan verilerini belirtilen hedefe göndermeden önce SAM tarafından atılacaktır.

Yanıtlanabilir ve ham datagram göndermenin alternatif bir yöntemi için, [DATAGRAM SEND ve RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling) bölümüne bakın.

#### SAM Yanıtlanabilir Datagramlar: Datagram Alma

Alınan datagramlar, SESSION CREATE komutunda bir yönlendirme PORT'u belirtilmemişse, datagram oturumunun açıldığı soket üzerinde SAM tarafından yazılır. Bu, datagram alma işleminin v1/v2-uyumlu yöntemidir.

Bir datagram geldiğinde, bridge bunu mesaj aracılığıyla istemciye teslim eder:

```
<-  DATAGRAM RECEIVED
           DESTINATION=$destination           # See notes below for Datagram3 format
           SIZE=$numBytes
           FROM_PORT=nnn                      # SAM 3.2 or higher only
           TO_PORT=nnn                        # SAM 3.2 or higher only
           \n
       [$numBytes of data]
```
Kaynak $destination'dır, bu da [Destination](/docs/specs/common-structures#type_Destination)'ın base 64'üdür ve imza türüne bağlı olarak 516 veya daha fazla base 64 karakter (binary olarak 387 veya daha fazla byte) içerir.

SAM köprüsü istemciye hiçbir zaman kimlik doğrulama başlıklarını veya diğer alanları göstermez, yalnızca gönderenin sağladığı veriyi sunar. Bu durum oturum kapanana kadar (istemcinin bağlantıyı kesmesiyle) devam eder.

#### Ham veya Yanıtlanabilir Datagram'ların Yönlendirilmesi

Bir datagram oturumu oluştururken, istemci SAM'den gelen mesajları belirli bir ip:port'a iletmesini isteyebilir. Bunu PORT ve HOST seçenekleri ile CREATE komutunu göndererek yapar:

```
-> SESSION CREATE
          STYLE={DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          PORT=$port
          [HOST=$host]
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP options
```
$privkey, [Destination](/docs/specs/common-structures#type_Destination)'ın ardından [Private Key](/docs/specs/common-structures#type_PrivateKey)'in ardından [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey)'in birleştirilmesinin base 64 kodlamasıdır ve isteğe bağlı olarak [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) ile takip edilir. Bu, imza türüne bağlı olarak 884 veya daha fazla base 64 karakter (ikili formatta 663 veya daha fazla bayt) içerir. İkili format Private Key File'da belirtilmiştir.

Çevrimdışı imzalar RAW, DATAGRAM2 ve DATAGRAM3 datagramları için desteklenir, ancak DATAGRAM için desteklenmez. Ayrıntılar için yukarıdaki SESSION CREATE bölümüne ve aşağıdaki DATAGRAM2/3 bölümüne bakın.

$host, SAM'in datagramları ileteceği datagram sunucusunun hostname veya IP adresidir. Verilmezse, SAM forward komutunu veren soketin IP adresini alır.

$port, SAM'in datagramları ileteceği datagram sunucusunun port numarasıdır. Eğer $port ayarlanmamışsa, datagramlar iletilmeyecek, bunun yerine v1/v2 uyumlu şekilde kontrol soketinde alınacaktır.

Verilen ek seçenekler, SAM köprüsü tarafından yorumlanmazsa I2P oturum yapılandırmasına aktarılır (örneğin outbound.length=0). Bu seçenekler [aşağıda belgelenmiştir](#tunnel-i2cp-and-streaming-options).

İletilen yanıtlanabilir datagramlar, aşağıda görülen Datagram3 hariç olmak üzere, her zaman base64 destination ile öneklenir. Yanıtlanabilir bir datagram geldiğinde, köprü belirtilen host:port adresine aşağıdaki verileri içeren bir UDP paketi gönderir:

```
$destination                       # See notes below for Datagram3 format
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
$datagram_payload
```
Yönlendirilen ham datagramlar, önek olmaksızın belirtilen host:port'a olduğu gibi yönlendirilir. UDP paketi aşağıdaki verileri içerir:

```
$datagram_payload
```
SAM 3.2 itibariyle, SESSION CREATE'de HEADER=true belirtildiğinde, iletilen ham datagram aşağıdaki gibi bir başlık satırı ile başlatılacaktır:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
$destination, [Destination](/docs/specs/common-structures#type_Destination)'ın base 64 kodlamasıdır ve imza türüne bağlı olarak 516 veya daha fazla base 64 karakter (ikili formatta 387 veya daha fazla bayt) içerir.

#### SAM Anonim (Ham) Datagramları

I2P'nin bant genişliğinden maksimum verim almak için SAM, istemcilerin anonim datagram gönderip almalarına izin verir ve kimlik doğrulama ile yanıt bilgilerini tamamen istemcilerin kendisine bırakır. Bu datagramlar güvenilir değildir ve sırasızdır, 32768 bayta kadar olabilir.

Minimum boyut 1'dir. En iyi teslimat güvenilirliği için önerilen maksimum boyut yaklaşık 11 KB'dir.

STYLE=RAW ile bir SAM oturumu kurduktan sonra, istemci SAM köprüsü üzerinden anonim datagramları tam olarak [yanıtlanabilir datagram gönderme](#sending-repliable-or-raw-datagrams) ile aynı şekilde gönderebilir.

Her iki datagram alma yöntemi anonim datagramlar için de kullanılabilir.

Alınan datagramlar, SESSION CREATE komutunda bir yönlendirme PORT'u belirtilmemişse, datagram oturumunun açıldığı soket üzerinden SAM tarafından yazılır. Bu, datagram alma işleminin v1/v2-uyumlu yöntemidir.

```
<- RAW RECEIVED
          SIZE=$numBytes
          FROM_PORT=nnn                      # SAM 3.2 or higher only
          TO_PORT=nnn                        # SAM 3.2 or higher only
          PROTOCOL=nnn                       # SAM 3.2 or higher only
          \n
      [$numBytes of data]
```
Anonim datagramlar belirli bir host:port'a iletilecek olduğunda, köprü belirtilen host:port'a aşağıdaki verileri içeren bir mesaj gönderir:

```
$datagram_payload
```
SAM 3.2 itibariyle, SESSION CREATE'de HEADER=true belirtildiğinde, iletilen ham datagram aşağıdaki gibi bir başlık satırı ile başlatılacaktır:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
Anonim datagram göndermenin alternatif bir yöntemi için, [RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling) bölümüne bakın.

#### Datagram 2/3

Datagram 2/3, 2025 yılının başlarında belirtilen yeni formatlardır. Şu anda bilinen hiçbir uygulama mevcut değildir. Güncel durum için uygulama belgelerini kontrol edin. Daha fazla bilgi için [spesifikasyona](/docs/specs/datagrams) bakın.

Datagram 2/3 desteğini belirtmek için SAM sürümünü artırma konusunda şu anda herhangi bir plan bulunmamaktadır. Bu durum, implementasyonların Datagram 2/3'ü desteklemek isteyebileceği ancak SAMv3.3 özelliklerini desteklemek istemeyebileceği için sorunlu olabilir. Herhangi bir sürüm değişikliği henüz belirlenmemiştir.

Hem Datagram2 hem de Datagram3 yanıtlanabilir. Yalnızca Datagram2 kimliği doğrulanmış.

Datagram2, SAM açısından yanıtlanabilir datagramlara benzerdir. Her ikisi de doğrulanmıştır. Yalnızca I2CP formatı ve imzası farklıdır, ancak bu SAM istemcileri tarafından görülmez. Datagram2 ayrıca çevrimdışı imzaları destekler, bu nedenle çevrimdışı imzalı hedefler tarafından kullanılabilir.

Datagram2'nin amacı, geriye dönük uyumluluk gerektirmeyen yeni uygulamalar için Repliable datagramları değiştirmektir. Datagram2, Repliable datagramlarda bulunmayan tekrar saldırısı koruması sağlar. Geriye dönük uyumluluk gerekiyorsa, bir uygulama SAM 3.3 PRIMARY oturumlarında aynı oturum üzerinde hem Datagram2 hem de Repliable'ı destekleyebilir.

Datagram3 yanıtlanabilir ancak kimlik doğrulaması yapılmaz. I2CP formatındaki 'from' alanı bir hash'tir, destination değil. SAM sunucusundan istemciye gönderilen $destination 44-byte base64 hash olacaktır. Bunu yanıt için tam destination'a dönüştürmek için, base64-decode ederek 32 byte binary haline getirin, sonra base32-encode ederek 52 karakter haline getirin ve NAMING LOOKUP için ".b32.i2p" ekleyin. Her zamanki gibi, istemciler tekrarlanan NAMING LOOKUP'ları önlemek için kendi önbelleklerini tutmalıdır.

Uygulama tasarımcıları aşırı dikkatli olmalı ve kimlik doğrulaması yapılmamış datagramların güvenlik etkilerini göz önünde bulundurmalıdır.

#### V3 Datagram MTU Değerlendirmeleri

I2P Datagramları, tipik internet MTU'su olan 1500'den daha büyük olabilir. Yerel olarak gönderilen datagramlar ve 516+ bayt base64 hedefi ile öneklenmiş iletilen yanıtlanabilir datagramlar muhtemelen bu MTU'yu aşacaktır. Ancak, Linux sistemlerinde localhost MTU'ları genellikle çok daha büyüktür, örneğin 65536. Localhost MTU'ları işletim sistemine göre değişiklik gösterecektir. I2P Datagramları asla 65536'dan büyük olmayacaktır. Datagram boyutu uygulama protokolüne bağlıdır.

SAM istemcisi SAM sunucusuna yerel ise ve sistem daha büyük bir MTU destekliyorsa, datagramlar yerel olarak parçalanmayacaktır. Ancak, SAM istemcisi uzak ise, IPv4 datagramları parçalanacak ve IPv6 datagramları başarısız olacaktır (IPv6, UDP parçalanmasını desteklemez).

İstemci kütüphanesi ve uygulama geliştiricileri bu sorunların farkında olmalı ve özellikle uzak SAM istemci-sunucu bağlantılarında parçalanmayı önlemek ve paket kaybını engellemek için önerileri belgelemelidir.

#### DATAGRAM SEND, RAW SEND (V1/V2 Uyumlu Datagram İşleme)

SAMv3'te, datagram göndermenin tercih edilen yolu yukarıda belgelendiği gibi 7655 portundaki datagram soketi üzerinden yapmaktır. Ancak, yanıtlanabilir datagramlar doğrudan SAM köprü soketi üzerinden DATAGRAM SEND komutu kullanılarak gönderilebilir, bu [SAM V1](/docs/api/sam) ve [SAM V2](/docs/api/samv2) belgelerinde açıklanmıştır.

0.9.14 sürümü (versiyon 3.1) itibariyle, anonim datagramlar [SAM V1](/docs/api/sam) ve [SAM V2](/docs/api/samv2) belgelerinde açıklandığı gibi RAW SEND komutu kullanılarak SAM bridge soketi üzerinden doğrudan gönderilebilir.

0.9.24 sürümünden itibaren (sürüm 3.2), DATAGRAM SEND ve RAW SEND varsayılan portları geçersiz kılmak için FROM_PORT=nnnn ve/veya TO_PORT=nnnn parametrelerini içerebilir. 0.9.24 sürümünden itibaren (sürüm 3.2), RAW SEND varsayılan protokolü geçersiz kılmak için PROTOCOL=nnn parametresini içerebilir.

Bu komutlar ID parametresini *desteklemez*. Datagramlar, uygun şekilde en son oluşturulan DATAGRAM- veya RAW-stil oturuma gönderilir. ID parametresi desteği gelecek bir sürümde eklenebilir.

DATAGRAM2 ve DATAGRAM3 formatları V1/V2 uyumlu şekilde *desteklenmez*.

### SAM PRIMARY Oturumları (V3.3 ve üzeri)

*Sürüm 3.3, I2P sürüm 0.9.25'te tanıtıldı.*

*Bu spesifikasyonun önceki bir sürümünde, PRIMARY oturumları MASTER oturumları olarak biliniyordu. Hem `i2pd` hem de `I2P+`'da hala yalnızca MASTER oturumları olarak bilinirler.*

SAM v3.3, aynı birincil oturum üzerinde streaming, datagram ve raw alt oturumları çalıştırma desteği ve aynı türde birden fazla alt oturum çalıştırma desteği ekler. Tüm alt oturum trafiği tek bir hedef veya tunnel seti kullanır. I2P'den gelen trafiğin yönlendirilmesi, alt oturumlar için port ve protokol seçeneklerine dayalıdır.

Çoğullanmış alt oturumlar oluşturmak için, önce birincil bir oturum oluşturmalı ve ardından bu birincil oturuma alt oturumlar eklemelisiniz. Her alt oturumun benzersiz bir kimliği ve benzersiz bir dinleme protokolü ile portu olmalıdır. Alt oturumlar ayrıca birincil oturumdan kaldırılabilir.

Bir PRIMARY oturum ve alt oturumların kombinasyonu ile, bir SAM istemcisi tek bir tunnel seti üzerinde birden fazla uygulamayı veya çeşitli protokoller kullanan tek bir gelişmiş uygulamayı destekleyebilir. Örneğin, bir bittorrent istemcisi eşler arası bağlantılar için streaming alt oturumu kurabilir ve DHT iletişimi için datagram ve raw alt oturumları ile birlikte kullanabilir.

#### PRIMARY Oturum Oluşturma

```
->  SESSION CREATE
          STYLE=PRIMARY                        # prior to 0.9.47, use STYLE=MASTER
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP and streaming options
```
SAM bridge, [standart SESSION CREATE yanıtındaki](#session-creation-response) gibi başarı veya başarısızlık ile yanıt verecektir.

Birincil oturumda PORT, HOST, FROM_PORT, TO_PORT, PROTOCOL, LISTEN_PORT, LISTEN_PROTOCOL veya HEADER seçeneklerini ayarlamayın. PRIMARY oturum kimliği veya kontrol soketi üzerinden herhangi bir veri gönderemezsiniz. STREAM CONNECT, DATAGRAM SEND vb. tüm komutlar ayrı bir soket üzerinde alt oturum kimliğini kullanmalıdır.

PRIMARY oturumu router'a bağlanır ve tunnel'ları oluşturur. SAM bridge yanıt verdiğinde, tunnel'lar oluşturulmuş ve oturum alt oturumların eklenmesi için hazır hale gelmiştir. Uzunluk, miktar ve takma ad gibi tunnel parametreleriyle ilgili tüm [I2CP](/docs/protocol/i2cp) seçenekleri primary'nin SESSION CREATE işleminde sağlanmalıdır.

Tüm yardımcı komutlar birincil oturumda desteklenir.

Birincil oturum kapatıldığında, tüm alt oturumlar da kapatılır.

NOT: 0.9.47 sürümünden önce STYLE=MASTER kullanın. STYLE=PRIMARY, 0.9.47 sürümünden itibaren desteklenmektedir. MASTER, geriye dönük uyumluluk için hala desteklenmektedir.

#### Bir Alt Oturum Oluşturma

PRIMARY oturumunun oluşturulduğu aynı kontrol socket'ini kullanarak:

```
->  SESSION ADD
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See above for DATAGRAM2/3
          ID=$nickname                         # must be unique
          [PORT=$port]                         # Required for DATAGRAM* and RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # For outbound traffic, default 0
          [TO_PORT=nnn]                        # For outbound traffic, default 0
          [PROTOCOL=nnn]                       # For outbound traffic for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [LISTEN_PORT=nnn]                    # For inbound traffic, default is the FROM_PORT value.
                                               # For STYLE=STREAM, only the FROM_PORT value or 0 is allowed.
          [LISTEN_PROTOCOL=nnn]                # For inbound traffic for STYLE=RAW only.
                                               # Default is the PROTOCOL value; 6 (streaming) is disallowed
          [HEADER={true,false}]                # For STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
SAM bridge, [standart SESSION CREATE yanıtında](#session-creation-response) olduğu gibi başarı veya başarısızlık ile yanıt verecektir. Tunnel'lar birincil SESSION CREATE'de zaten oluşturulduğundan, SAM bridge hemen yanıt vermelidir.

SESSION ADD'de DESTINATION seçeneğini ayarlamayın. Alt oturum, birincil oturumda belirtilen destination'ı kullanacaktır. Tüm alt oturumlar kontrol soketinde, yani birincil oturumu oluşturduğunuz aynı bağlantıda eklenmelidir.

Birden fazla alt oturum, gelen verilerin doğru şekilde yönlendirilebilmesi için yeterince benzersiz seçeneklere sahip olmalıdır. Özellikle, aynı türdeki birden fazla oturum farklı LISTEN_PORT seçeneklerine (ve/veya yalnızca RAW için LISTEN_PROTOCOL) sahip olmalıdır. Mevcut bir alt oturumu kopyalayan dinleme portu ve protokolü ile yapılan bir SESSION ADD komutu hatayla sonuçlanacaktır.

LISTEN_PORT yerel I2P portu, yani gelen veriler için alma (TO) portudur. LISTEN_PORT belirtilmezse, FROM_PORT değeri kullanılacaktır. LISTEN_PORT ve FROM_PORT belirtilmezse, gelen yönlendirme yalnızca STYLE ve PROTOCOL temel alınarak yapılacaktır. LISTEN_PORT ve LISTEN_PROTOCOL için 0 herhangi bir değer anlamına gelir, yani joker karakterdir. Hem LISTEN_PORT hem de LISTEN_PROTOCOL 0 ise, bu alt oturum başka bir alt oturuma yönlendirilmeyen gelen trafik için varsayılan olacaktır. Gelen streaming trafiği (protokol 6) LISTEN_PROTOCOL değeri 0 olsa bile asla RAW alt oturumuna yönlendirilmeyecektir. RAW alt oturumu LISTEN_PROTOCOL değerini 6 olarak ayarlayamaz. Gelen trafiğin protokolü ve portuyla eşleşen varsayılan veya alt oturum yoksa, bu veriler düşürülecektir.

Veri gönderme ve alma için birincil oturum ID'si değil, alt oturum ID'sini kullanın. STREAM CONNECT, DATAGRAM SEND vb. tüm komutlar alt oturum ID'sini kullanmalıdır.

Tüm yardımcı komutlar birincil oturumda veya alt oturumda desteklenir. v1/v2 datagram/raw gönderme/alma işlemleri birincil oturumda veya alt oturumlarda desteklenmez.

#### Bir Alt Oturumu Durdurma

PRIMARY oturumunun oluşturulduğu aynı kontrol soketini kullanarak:

```
->  SESSION REMOVE
          ID=$nickname
```
Bu, birincil oturumdan bir alt oturumu kaldırır. SESSION REMOVE üzerinde başka hiçbir seçenek ayarlamayın. Alt oturumlar kontrol socket'i üzerinden, yani birincil oturumu oluşturduğunuz aynı bağlantı üzerinden kaldırılmalıdır. Bir alt oturum kaldırıldıktan sonra kapatılır ve veri gönderme veya alma için kullanılamaz.

SAM bridge, [standart SESSION CREATE yanıtında](#session-creation-response) olduğu gibi başarı veya başarısızlık ile yanıt verecektir.

### SAM Yardımcı Komutları

Bazı yardımcı komutlar önceden var olan bir oturum gerektirir, bazıları gerektirmez. Aşağıdaki ayrıntılara bakın.

#### Host Adı Arama

Aşağıdaki mesaj, istemci tarafından SAM köprüsünden ad çözümlemesi sorgulamak için kullanılabilir:

```
NAMING LOOKUP
       NAME=$name
       [OPTIONS=true]     # Default false, as of router API 0.9.66
```
şu şekilde yanıtlanır

```
NAMING REPLY
       RESULT=$result
       NAME=$name
       [VALUE=$destination]
       [MESSAGE="$message"]
       [OPTION:optionkey="$optionvalue"]   # As of router API 0.9.66
```
RESULT değeri şunlardan biri olabilir:

```
OK
INVALID_KEY
KEY_NOT_FOUND
```
Eğer NAME=ME ise, yanıt mevcut oturum tarafından kullanılan hedefi içerecektir (TRANSIENT bir oturum kullanıyorsanız faydalıdır). Eğer $result OK değilse, MESSAGE "bad format" gibi açıklayıcı bir mesaj içerebilir. INVALID_KEY, istekteki $name ile ilgili bir sorun olduğunu, muhtemelen geçersiz karakterler bulunduğunu belirtir.

$destination, [Destination](/docs/specs/common-structures#type_Destination)'ın base 64 kodlamasıdır ve imza türüne bağlı olarak 516 veya daha fazla base 64 karakter (binary'de 387 veya daha fazla bayt) içerir.

NAMING LOOKUP, önce bir oturumun oluşturulmasını gerektirmez. Ancak bazı uygulamalarda, önbelleğe alınmamış ve ağ sorgusu gerektiren bir .b32.i2p araması başarısız olabilir, çünkü arama için istemci tunnel'ları mevcut değildir.

#### İsim Arama Seçenekleri

NAMING LOOKUP, router API 0.9.66 sürümünden itibaren servis aramalarını destekleyecek şekilde genişletilmiştir. Destek, uygulamaya göre değişiklik gösterebilir. Ek bilgi için proposal 167'ye bakınız.

NAMING LOOKUP NAME=example.i2p OPTIONS=true yanıtta seçenekler eşlemesini talep eder. OPTIONS=true olduğunda NAME tam bir base64 hedef olabilir.

Eğer hedef araması başarılı olduysa ve leaseset'te seçenekler mevcutsa, yanıtta hedefin ardından OPTION:anahtar=değer biçiminde bir veya daha fazla seçenek bulunacaktır. Her seçeneğin ayrı bir OPTION: öneki olacaktır. Leaseset'teki tüm seçenekler dahil edilecektir, sadece servis kayıt seçenekleri değil. Örneğin, gelecekte tanımlanacak parametreler için seçenekler de mevcut olabilir. Örnek:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

'=' içeren anahtarlar ve yeni satır içeren anahtar veya değerler geçersiz kabul edilir ve anahtar/değer çifti yanıttan kaldırılır. leaseSet'te hiçbir seçenek bulunamazsa veya leaseSet sürüm 1 ise, yanıt herhangi bir seçenek içermez. Aramada OPTIONS=true varsa ve leaseSet bulunamazsa, yeni bir sonuç değeri LEASESET_NOT_FOUND döndürülür.

#### Destination Anahtar Üretimi

Genel ve özel base64 anahtarları aşağıdaki mesaj kullanılarak oluşturulabilir:

```
->  DEST GENERATE
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, default DSA_SHA1
```
şu şekilde yanıtlanır

```
DEST REPLY
     PUB=$destination
     PRIV=$privkey
```
Sürüm 3.1 itibariyle (I2P 0.9.14), isteğe bağlı bir SIGNATURE_TYPE parametresi desteklenmektedir. SIGNATURE_TYPE değeri, [Anahtar Sertifikaları](/docs/specs/common-structures#type_Certificate) tarafından desteklenen herhangi bir isim (örneğin ECDSA_SHA256_P256, büyük/küçük harf duyarsız) veya sayı (örneğin 1) olabilir. Varsayılan değer DSA_SHA1'dir ve bu muhtemelen istediğiniz değer DEĞİLDİR. Çoğu uygulama için lütfen SIGNATURE_TYPE=7 belirtin.

$destination, [Destination](/docs/specs/common-structures#type_Destination)'ın base 64 halidir ve imza türüne bağlı olarak 516 veya daha fazla base 64 karakteri (ikili formatta 387 veya daha fazla bayt) içerir.

$privkey, [Destination](/docs/specs/common-structures#type_Destination) ardından [Private Key](/docs/specs/common-structures#type_PrivateKey) ardından [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey)'in birleştirilmesinin base 64 kodlamasıdır ve imza türüne bağlı olarak 884 veya daha fazla base 64 karakter (ikili formatta 663 veya daha fazla bayt) uzunluğundadır. İkili format Private Key File içinde belirtilmiştir.

256 byte'lık binary [Private Key](/docs/specs/common-structures#type_PrivateKey) hakkında notlar: Bu alan 0.6 sürümünden (2005) bu yana kullanılmamaktadır. SAM implementasyonları bu alana rastgele veri veya tamamı sıfır gönderebilir; base 64'te bir dizi AAAA görmekten endişelenmeyin. Çoğu uygulama sadece base 64 string'ini depolayacak ve SESSION CREATE'de olduğu gibi geri döndürecek, ya da depolama için binary'ye decode edip sonra SESSION CREATE için tekrar encode edecektir. Ancak uygulamalar, base 64'ü decode edebilir, binary'yi PrivateKeyFile spesifikasyonunu takip ederek parse edebilir, 256 byte'lık private key kısmını atabilir ve sonra SESSION CREATE için yeniden encode ederken onu 256 byte rastgele veri veya tamamı sıfır ile değiştirebilir. PrivateKeyFile spesifikasyonundaki DİĞER TÜM alanlar korunmalıdır. Bu, dosya sistemi depolamasından 256 byte tasarruf sağlayacaktır ancak çoğu uygulama için muhtemelen bu zahmet değmez. Ek bilgi ve geçmiş için proposal 161'e bakın.

DEST GENERATE komutu önce bir oturum oluşturulmasını gerektirmez.

DEST GENERATE, çevrimdışı imzalara sahip bir hedef oluşturmak için kullanılamaz.

#### PING/PONG (SAM 3.2 veya üstü)

İstemci veya sunucu gönderebilir:

```
PING[ arbitrary text]
```
kontrol portunda, şu yanıt ile:

```
PONG[ arbitrary text from the ping]
```
kontrol soket keepalive için kullanılacaktır. Makul bir süre içinde yanıt alınmazsa, her iki taraf da oturumu ve soketi kapatabilir, bu uygulama bağımlıdır.

İstemciden bir PONG beklenirken zaman aşımı oluşursa, köprü şunu gönderebilir:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
ve sonra bağlantıyı kes.

Bridge'den PONG bekleme sırasında zaman aşımı oluşursa, istemci basitçe bağlantıyı kesebilir.

PING/PONG işlemleri önce bir oturum oluşturulmasını gerektirmez.

#### QUIT/STOP/EXIT (SAM 3.2 veya üstü, isteğe bağlı özellikler)

QUIT, STOP ve EXIT komutları oturumu ve soketi kapatacaktır. Uygulama isteğe bağlıdır, telnet aracılığıyla test kolaylığı için vardır. Soket kapatılmadan önce herhangi bir yanıt olup olmayacağı (örneğin, bir SESSION STATUS mesajı) uygulamaya özgüdür ve bu spesifikasyonun kapsamı dışındadır.

QUIT/STOP/EXIT komutları önce bir oturum oluşturulmasını gerektirmez.

#### YARDIM (isteğe bağlı özellik)

Sunucular bir HELP komutu uygulayabilir. Uygulama isteğe bağlıdır ve telnet üzerinden test kolaylığı için mevcuttur. Çıktı formatı ve çıktının sonunun tespiti uygulamaya özgüdür ve bu spesifikasyonun kapsamı dışındadır.

HELP, önce bir oturum oluşturulmasını gerektirmez.

#### Yetkilendirme Yapılandırması (SAM 3.2 veya daha yüksek, isteğe bağlı özellik)

AUTH komutu kullanılarak yetkilendirme yapılandırması. Bir SAM sunucusu, kimlik bilgilerinin kalıcı depolanmasını kolaylaştırmak için bu komutları uygulayabilir. Bu komutlar dışında kimlik doğrulama yapılandırması, uygulamaya özel olup bu spesifikasyonun kapsamı dışındadır.

- AUTH ENABLE sonraki bağlantılarda yetkilendirmeyi etkinleştirir
- AUTH DISABLE sonraki bağlantılarda yetkilendirmeyi devre dışı bırakır
- AUTH ADD USER="foo" PASSWORD="bar" bir kullanıcı/şifre ekler
- AUTH REMOVE USER="foo" bu kullanıcıyı kaldırır

Kullanıcı adı ve parola için çift tırnak önerilir ancak zorunlu değildir. Kullanıcı adı veya parola içindeki çift tırnak ters eğik çizgi ile kaçış karakteri kullanılarak belirtilmelidir. Hata durumunda sunucu I2P_ERROR ve bir mesaj ile yanıt verecektir.

AUTH, önce bir oturum oluşturulmasını gerektirmez.

### RESULT Değerleri

Bunlar RESULT alanının taşıyabileceği değerler ve anlamlarıdır:

```
OK              Operation completed successfully
CANT_REACH_PEER The peer exists, but cannot be reached
DUPLICATED_DEST The specified Destination is already in use
I2P_ERROR       A generic I2P error (e.g. I2CP disconnection, etc.)
INVALID_KEY     The specified key is not valid (bad format, etc.)
KEY_NOT_FOUND   The naming system can't resolve the given name
PEER_NOT_FOUND  The peer cannot be found on the network
TIMEOUT         Timeout while waiting for an event (e.g. peer answer)
LEASESET_NOT_FOUND  See Name Lookup Options above. As of router API 0.9.66.
```
Farklı uygulamalar, çeşitli senaryolarda hangi RESULT'ın döndürüleceği konusunda tutarlı olmayabilir.

OK dışındaki RESULT içeren çoğu yanıt, ek bilgi içeren bir MESSAGE de içerecektir. MESSAGE genellikle sorunları gidermede yardımcı olacaktır. Ancak, MESSAGE dizeleri uygulama bağımlıdır, SAM sunucusu tarafından mevcut dil ayarına çevrilebilir veya çevrilmeyebilir, istisnalar gibi dahili uygulama özel bilgileri içerebilir ve önceden haber verilmeksizin değiştirilebilir. SAM istemcileri MESSAGE dizelerini kullanıcılara göstermeyi seçebilse de, bu kırılgan olacağından, bu dizelere dayalı programsal kararlar almamalıdırlar.

### Tunnel, I2CP ve Streaming Seçenekleri

Bu seçenekler SAM SESSION CREATE satırında isim=değer çiftleri olarak geçirilebilir.

Tüm oturumlar [tunnel uzunlukları ve miktarları gibi I2CP seçenekleri](/docs/protocol/i2cp#options) içerebilir. STREAM oturumları [Streaming kütüphanesi seçenekleri](/docs/api/streaming#options) içerebilir.

Seçenek adları ve varsayılan değerler için bu referanslara bakın. Referans verilen dokümantasyon Java router uygulaması içindir. Varsayılan değerler değişikliğe tabidir. Seçenek adları ve değerleri büyük/küçük harf duyarlıdır. Diğer router uygulamaları tüm seçenekleri desteklemeyebilir ve farklı varsayılan değerlere sahip olabilir; ayrıntılar için router dokümantasyonuna başvurun.

### BASE 64 Notları

Base 64 kodlaması I2P standart Base 64 alfabesi "A-Z, a-z, 0-9, -, ~" kullanmalıdır.

### Varsayılan SAM Kurulumu

Varsayılan SAM portu 7656'dır. SAM, Java I2P Router'da varsayılan olarak etkin değildir; router konsolundaki istemcileri yapılandır sayfasında veya clients.config dosyasında manuel olarak başlatılmalı veya otomatik olarak başlayacak şekilde yapılandırılmalıdır. Varsayılan SAM UDP portu 7655'tir ve 127.0.0.1'i dinler. Bunlar Java router'da çağrıya sam.udp.port=nnnnn ve/veya sam.udp.host=w.x.y.z argümanları eklenerek veya SESSION satırında değiştirilebilir.

Diğer router'larda konfigürasyon, uygulama-özeldir. [i2pd konfigürasyon kılavuzuna buradan bakın](https://i2pd.readthedocs.io/en/latest/user-guide/configuration/).
