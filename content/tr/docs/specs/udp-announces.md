---
title: "UDP Tracker'lar"
description: "I2P'de UDP BitTorrent duyuruları için protokol spesifikasyonu"
slug: "udp-announces"
category: "Protokoller"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

## Genel Bakış

Bu spesifikasyon, I2P'de UDP bittorrent duyurularının protokolünü belgeler. I2P'de bittorrent'in genel spesifikasyonu için, [BitTorrent over I2P](/docs/applications/bittorrent) bölümüne bakın. Bu spesifikasyonun geliştirilmesine ilişkin arka plan ve ek bilgi için, [Proposal 160](/proposals/160-udp-trackers) bölümüne bakın.

## Tasarım

Bu teklif, [Datagrams](/docs/specs/datagrams) belgesinde tanımlandığı şekliyle repliable datagram2, repliable datagram3 ve ham datagramları kullanır. Datagram2 ve Datagram3, [Proposal 163](/proposals/163-datagram2-datagram3) belgesinde tanımlanan repliable datagramların yeni varyantlarıdır. Datagram2, tekrar saldırısı direnci ve çevrimdışı imza desteği ekler. Datagram3, eski datagram formatından daha küçüktür ancak kimlik doğrulama özelliği yoktur.

### BEP 15

Referans olarak, [BEP 15](http://www.bittorrent.org/beps/bep_0015.html)'te tanımlanan mesaj akışı aşağıdaki gibidir:

```
Client                        Tracker
    Connect Req. ------------->
      <-------------- Connect Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
```
Bağlantı aşaması, IP adresi sahtekarlığını önlemek için gereklidir. Tracker, istemcinin sonraki duyurularda kullandığı bir bağlantı kimliği döndürür. Bu bağlantı kimliği varsayılan olarak istemcide bir dakika, tracker'da ise iki dakika sonra sona erer.

I2P, mevcut UDP özellikli istemci kod tabanlarında benimsenme kolaylığı, verimlilik ve aşağıda tartışılan güvenlik nedenleri için BEP 15 ile aynı mesaj akışını kullanacaktır:

```
Client                        Tracker
    Connect Req. ------------->       (Repliable Datagram2)
      <-------------- Connect Resp.   (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
             ...
```
Bu, streaming (TCP) duyurularına göre potansiyel olarak büyük bir bant genişliği tasarrufu sağlar. Datagram2, streaming SYN ile yaklaşık aynı boyutta olsa da, ham yanıt streaming SYN ACK'dan çok daha küçüktür. Sonraki istekler Datagram3 kullanır ve sonraki yanıtlar hamdır.

Duyuru istekleri Datagram3 şeklindedir, böylece tracker'ın bağlantı ID'lerinden duyuru hedefine veya hash'e kadar büyük bir eşleme tablosunu sürdürmesi gerekmez. Bunun yerine, tracker bağlantı ID'lerini gönderen hash'inden, mevcut zaman damgasından (belirli bir aralığa dayalı) ve gizli bir değerden kriptografik olarak üretebilir. Bir duyuru isteği alındığında, tracker bağlantı ID'sini doğrular ve ardından Datagram3 gönderen hash'ini gönderim hedefi olarak kullanır.

### Bağlantı Ömrü

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html), bağlantı ID'sinin istemcide bir dakika, tracker'da iki dakika sonra sona erdiğini belirtir. Bu yapılandırılabilir değildir. Bu durum, istemciler tüm duyurularını bir dakikalık pencere içinde toplu olarak yapmadığı sürece potansiyel verimlilik kazançlarını sınırlar. i2psnark şu anda duyuruları toplu yapmıyor; trafik patlamalarını önlemek için bunları dağıtıyor. Güçlü kullanıcıların aynı anda binlerce torrent çalıştırdığı bildiriliyor ve bu kadar çok duyuruyu bir dakikaya sıkıştırmak gerçekçi değil.

Burada, bağlantı yanıtını isteğe bağlı bir bağlantı ömrü alanı eklemek için genişletmeyi öneriyoruz. Mevcut değilse varsayılan değer bir dakikadır. Aksi takdirde, saniye cinsinden belirtilen ömür istemci tarafından kullanılacak ve tracker, bağlantı ID'sini bir dakika daha fazla süreyle koruyacaktır.

### BEP 15 ile Uyumluluk

Bu tasarım, mevcut istemciler ve tracker'larda gerekli değişiklikleri sınırlamak için [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) ile mümkün olduğunca uyumluluk sağlar.

Tek gerekli değişiklik, announce yanıtındaki peer bilgilerinin formatıdır. Connect yanıtına lifetime alanının eklenmesi zorunlu değildir ancak yukarıda açıklandığı gibi verimlilik için şiddetle önerilir.

### Güvenlik Analizi

Bir UDP duyuru protokolünün önemli bir hedefi adres sahteciliğini önlemektir. İstemci gerçekten var olmalı ve gerçek bir leaseSet paketlemelidir. Connect Response'u almak için gelen tunnel'lara sahip olmalıdır. Bu tunnel'lar sıfır atlama olabilir ve anında oluşturulabilir, ancak bu yaratıcıyı açığa çıkarır. Bu protokol bu hedefi gerçekleştirir.

### Sorunlar

- Bu protokol blinded destinations'ı desteklemez, ancak desteklemek için genişletilebilir. Aşağıya bakınız.

## Spesifikasyon

### Protokoller ve Portlar

Repliable Datagram2, I2CP protokol 19'u kullanır; repliable Datagram3, I2CP protokol 20'yi kullanır; ham datagramlar I2CP protokol 18'i kullanır. İstekler Datagram2 veya Datagram3 olabilir. Yanıtlar her zaman hamdır. I2CP protokol 17 kullanan eski repliable datagram ("Datagram1") formatı istekler veya yanıtlar için kullanılmamalıdır; bunlar istek/yanıt portlarında alınırsa bırakılmalıdır. Datagram1 protokol 17'nin hala DHT protokolü için kullanıldığını unutmayın.

İstekler, duyuru URL'sinden I2CP "to port" kullanır; aşağıya bakın. İstek "from port" istemci tarafından seçilir, ancak sıfır olmayan ve DHT tarafından kullanılanlardan farklı bir port olmalıdır, böylece yanıtlar kolayca sınıflandırılabilir. Tracker'lar yanlış portta alınan istekleri reddetmelidir.

Yanıtlar, istekten gelen I2CP "to port" değerini kullanır. İsteğin "from port" değeri, istekten gelen "to port" değeridir.

### Duyuru URL'si

Announce URL formatı [BEP 15](http://www.bittorrent.org/beps/bep_0015.html)'te belirtilmemiştir, ancak clearnet'te olduğu gibi, UDP announce URL'leri `udp://host:port/path` formatındadır. Path yok sayılır ve boş olabilir, ancak clearnet'te tipik olarak `/announce`'dir. `:port` kısmı her zaman mevcut olmalıdır, ancak `:port` kısmı atlanırsa, varsayılan I2CP portu olan 6969'u kullanın, çünkü bu clearnet'te yaygın porttur. Ayrıca `&a=b&c=d` şeklinde cgi parametreleri eklenebilir, bunlar işlenebilir ve announce isteğinde sağlanabilir, bkz. [BEP 41](http://www.bittorrent.org/beps/bep_0041.html). Parametre veya path yoksa, sondaki `/` de atlanabilir, [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)'de ima edildiği gibi.

### Datagram Formatları

Tüm değerler ağ bayt sıralamasında (big endian) gönderilir. Paketlerin tam olarak belirli bir boyutta olmasını beklemeyin. Gelecekteki uzantılar paketlerin boyutunu artırabilir.

#### Bağlantı İsteği

İstemciden tracker'a. 16 bayt. Yanıtlanabilir Datagram2 olmalıdır. [BEP 15](http://www.bittorrent.org/beps/bep_0015.html)'teki ile aynı. Değişiklik yok.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">protocol_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0x41727101980 // magic constant</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
#### Bağlantı Yanıtı

Tracker'dan istemciye. 16 veya 18 bayt. Ham olmalı. Aşağıda belirtilenler dışında [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) ile aynı.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">lifetime</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // Change from BEP 15</td>
    </tr>
  </tbody>
</table>
Yanıt, istek "from port" olarak alınan I2CP "to port"una gönderilmek ZORUNDADIR.

Lifetime alanı isteğe bağlıdır ve connection_id istemci yaşam süresini saniye cinsinden belirtir. Varsayılan değer 60'tır ve belirtilirse minimum değer 60'tır. Maksimum değer 65535 veya yaklaşık 18 saattir. Tracker, connection_id'yi istemci yaşam süresinden 60 saniye daha fazla süreyle korumalıdır.

#### Duyuru İsteği

İstemciden tracker'a. Minimum 98 bayt. Yanıtlanabilir Datagram3 olmalı. Aşağıda belirtilen durumlar dışında [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) ile aynı.

connection_id, bağlantı yanıtında alınan değerdir.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">info_hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">peer_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">56</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">downloaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">left</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">uploaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">80</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">event</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // 0: none; 1: completed; 2: started; 3: stopped</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">84</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">IP address</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // default, unused in I2P</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">88</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">92</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">num_want</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1 // default</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">port</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// must be same as I2CP from port</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">98</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">options</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // As specified in BEP 41</td>
    </tr>
  </tbody>
</table>
[BEP 15](http://www.bittorrent.org/beps/bep_0015.html)'ten değişiklikler:

- key göz ardı edilir
- IP adresi kullanılmaz
- port muhtemelen göz ardı edilir ancak I2CP from port ile aynı olmalıdır
- Seçenekler bölümü, mevcutsa, [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)'de tanımlandığı gibidir

Yanıt, istek "from port" olarak alınan I2CP "to port"una gönderilmelidir. Duyuru isteğindeki portu kullanmayın.

#### Duyuru Yanıtı

Tracker'dan istemciye. Minimum 20 bayt. Ham veri olmalıdır. Aşağıda belirtilenler dışında [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) ile aynıdır.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">interval</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">leechers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">seeders</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32 * n 32-byte hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">binary hashes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// Change from BEP 15</td>
    </tr>
  </tbody>
</table>
[BEP 15](http://www.bittorrent.org/beps/bep_0015.html)'ten yapılan değişiklikler:

- 6-byte IPv4+port veya 18-byte IPv6+port yerine, SHA-256 ikili peer hash'leri ile 32-byte'ın katları şeklinde "kompakt yanıtlar" döndürürüz. TCP kompakt yanıtlarında olduğu gibi, bir port dahil etmeyiz.

Yanıt, istek "from port"u olarak alınan I2CP "to port"una gönderilmelidir. Duyuru isteğindeki portu kullanmayın.

I2P datagramları yaklaşık 64 KB'lık çok büyük bir maksimum boyuta sahiptir; ancak güvenilir teslimat için 4 KB'dan büyük datagramlardan kaçınılmalıdır. Bant genişliği verimliliği için, tracker'lar muhtemelen maksimum peer sayısını yaklaşık 50 ile sınırlamalıdır; bu da çeşitli katmanlardaki overhead öncesi yaklaşık 1600 baytlık bir pakete karşılık gelir ve parçalanma sonrası iki tunnel mesajı yük sınırı içinde olmalıdır.

BEP 15'te olduğu gibi, takip edecek peer adreslerinin (BEP 15 için IP/port, burada hash'ler) sayısını içeren bir sayım bulunmaz. BEP 15'te düşünülmemiş olsa da, peer bilgisinin tamamlandığını ve bazı ek verilerin takip ettiğini belirtmek için tamamı sıfırlardan oluşan bir peer-sonu işaretçisi tanımlanabilir.

Gelecekte genişletmenin mümkün olması için, istemciler 32-baytlık tamamı sıfır olan hash'i ve onu takip eden herhangi bir veriyi görmezden gelmelidir. Tracker'lar tamamı sıfır olan hash'den gelen duyuruları reddetmelidir, ancak bu hash zaten Java router'lar tarafından yasaklanmıştır.

#### Kazıma

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html)'ten scrape isteği/yanıtı bu spesifikasyon tarafından gerekli değildir, ancak istenirse uygulanabilir, herhangi bir değişiklik gerekmez. İstemci önce bir bağlantı kimliği edinmelidir. Scrape isteği her zaman yanıtlanabilir Datagram3'tür. Scrape yanıtı her zaman ham'dır.

#### Hata Yanıtı

Tracker'dan istemciye. Minimum 8 bayt (mesaj boşsa). Ham olmalıdır. [BEP 15](http://www.bittorrent.org/beps/bep_0015.html)'teki ile aynı. Değişiklik yok.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3 // error</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">message</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
## Uzantılar

Uzantı bitleri veya sürüm alanı dahil edilmez. İstemciler ve tracker'lar paketlerin belirli bir boyutta olduğunu varsaymamalıdır. Bu şekilde, uyumluluğu bozmadan ek alanlar eklenebilir. Gerekirse [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)'de tanımlanan uzantı formatı önerilir.

Bağlantı yanıtı, isteğe bağlı bir bağlantı kimliği ömrü eklemek için değiştirildi.

Blinded destination desteği gerekiyorsa, announce isteğinin sonuna blinded 35-byte adresini ekleyebiliriz veya [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) formatını kullanarak yanıtlarda blinded hash'leri isteyebiliriz (parametreler henüz belirlenmedi). Blinded 35-byte peer adreslerinin kümesi, tamamen sıfır olan 32-byte hash'ten sonra announce yanıtının sonuna eklenebilir.

## Uygulama Kılavuzları

Entegre olmayan, I2CP olmayan istemciler ve tracker'lar için zorlukların tartışılması için yukarıdaki tasarım bölümüne bakın.

### İstemciler

Belirli bir tracker hostname için, istemci HTTP URL'leri yerine UDP'yi tercih etmeli ve her ikisine birden announce yapmamalıdır.

Mevcut BEP 15 desteğine sahip istemciler yalnızca küçük değişiklikler gerektirecektir.

Bir istemci DHT veya diğer datagram protokollerini destekliyorsa, muhtemelen istek "kaynak portu" olarak farklı bir port seçmelidir, böylece yanıtlar o porta geri gelir ve DHT mesajları ile karışmaz. İstemci sadece yanıt olarak ham datagramlar alır. Tracker'lar istemciye asla yanıtlanabilir bir datagram2 göndermez.

Varsayılan opentracker listesine sahip istemciler, bilinen opentracker'ların UDP'yi desteklediği bilindiğinde UDP URL'lerini eklemek için listeyi güncellemelidir.

İstemciler isteklerin yeniden iletimini uygulayabilir veya uygulamayabilir. Yeniden iletimler, eğer uygulanırsa, en az 15 saniye başlangıç zaman aşımı kullanmalı ve her yeniden iletim için zaman aşımını ikiye katlamalıdır (üstel geri çekilme).

İstemciler bir hata yanıtı aldıktan sonra geri çekilmelidir.

### Takipçiler

Mevcut BEP 15 desteğine sahip tracker'lar yalnızca küçük değişiklikler gerektirecektir. Bu spesifikasyon 2014 önerisinden farklıdır, çünkü tracker aynı port üzerinde repliable datagram2 ve datagram3 alımını desteklemek zorundadır.

Tracker kaynak gereksinimlerini minimize etmek için, bu protokol tracker'ın daha sonra doğrulama için istemci hash'lerinin bağlantı kimliklerine eşlemelerini saklaması gerekliliğini ortadan kaldırmak üzere tasarlanmıştır. Bu mümkündür çünkü announce isteği paketi yanıtlanabilir bir Datagram3 paketidir, dolayısıyla gönderenin hash'ini içerir.

Önerilen bir uygulama şudur:

- Mevcut epoch'u bağlantı ömrü çözünürlüğü ile mevcut zaman olarak tanımla, `epoch = now / lifetime`.
- 8 byte çıktı üreten bir kriptografik hash fonksiyonu `H(secret, clienthash, epoch)` tanımla.
- Tüm bağlantılar için kullanılan rastgele sabit secret'ı üret.
- Connect yanıtları için, `connection_id = H(secret, clienthash, epoch)` üret
- Announce istekleri için, mevcut epoch'ta alınan connection ID'yi `connection_id == H(secret, clienthash, epoch) || connection_id == H(secret, clienthash, epoch - 1)` doğrulayarak geçerli kıl

## Referanslar

- **[BEP15]** [BEP 15 - UDP Tracker Protocol](http://www.bittorrent.org/beps/bep_0015.html)
- **[BEP41]** [BEP 41 - UDP Tracker Protocol Extensions](http://www.bittorrent.org/beps/bep_0041.html)
- **[DATAGRAMS]** [Datagrams Spesifikasyonu](/docs/specs/datagrams)
- **[Prop160]** [Öneri 160 - UDP Trackers](/proposals/160-udp-trackers)
- **[Prop163]** [Öneri 163 - Datagram2/Datagram3](/proposals/163-datagram2-datagram3)
- **[SAMv3]** [SAM v3 API](/docs/api/samv3)
- **[SPEC]** [I2P üzerinde BitTorrent](/docs/applications/bittorrent)
