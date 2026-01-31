---
title: "Akış Protokolü"
description: "Çoğu I2P uygulaması tarafından kullanılan TCP benzeri taşıma protokolü"
slug: "streaming"
lastUpdated: "2025-07"
accurateFor: "0.9.67"
---

## Genel Bakış {#overview}

Streaming kütüphanesi teknik olarak "uygulama" katmanının bir parçasıdır, çünkü temel router işlevi değildir. Ancak pratikte, I2P üzerinde TCP benzeri akışlar sağlayarak ve mevcut uygulamaların I2P'ye kolayca taşınmasına izin vererek, hemen hemen tüm mevcut I2P uygulamaları için hayati bir işlev sunar. İstemci iletişimi için diğer uçtan uca aktarım kütüphanesi [datagram kütüphanesidir](/docs/specs/datagrams).

Streaming kütüphanesi, güvenilir, sıralı ve kimlik doğrulamalı mesaj akışlarının güvenilmez, sırasız ve kimlik doğrulamasız mesaj katmanı üzerinde çalışmasına olanak tanıyan temel [I2CP API](/docs/specs/i2cp) üzerinde bir katmandır. Tıpkı TCP ile IP ilişkisi gibi, bu streaming işlevselliği bir dizi denge ve optimizasyon seçeneğine sahiptir, ancak bu işlevselliği temel I2P koduna gömek yerine, hem TCP benzeri karmaşıklıkları ayrı tutmak hem de alternatif optimize edilmiş implementasyonlara olanak sağlamak için kendi kütüphanesine ayrılmıştır.

Mesajların nispeten yüksek maliyeti göz önünde bulundurularak, streaming kütüphanesinin bu mesajları planlama ve iletme protokolü, geçirilen tek tek mesajların mevcut olan mümkün olduğunca fazla bilgiyi içerebilmesine olanak sağlayacak şekilde optimize edilmiştir. Örneğin, streaming kütüphanesi üzerinden proxy edilen küçük bir HTTP işlemi tek bir gidiş-dönüş ile tamamlanabilir - ilk mesajlar bir SYN, FIN ve küçük HTTP istek yükünü paketler, yanıt ise SYN, FIN, ACK ve HTTP yanıt yükünü paketler. HTTP sunucusuna SYN/FIN/ACK'ın alındığını bildirmek için ek bir ACK iletilmesi gerekse de, yerel HTTP proxy genellikle tam yanıtı tarayıcıya hemen iletebilir.

Streaming kütüphanesi, kayar pencereleri, tıkanıklık kontrol algoritmaları (hem yavaş başlangıç hem de tıkanıklık önleme) ve genel paket davranışları (ACK, SYN, FIN, RST, rto hesaplama vb.) ile TCP soyutlamasına büyük benzerlik gösterir.

Streaming kütüphanesi, I2P üzerinde çalışmak için optimize edilmiş sağlam bir kütüphanedir. Tek aşamalı kuruluma sahiptir ve tam bir pencere uygulaması içerir.

## API {#api}

Streaming kütüphanesi API'si, Java uygulamalarına standart bir soket paradigması sağlar. Alt seviye [I2CP](/docs/specs/i2cp) API'si tamamen gizlidir, ancak uygulamalar I2CP tarafından yorumlanmak üzere [I2CP parametrelerini](/docs/specs/i2cp#options) streaming kütüphanesi aracılığıyla geçirebilir.

Streaming kütüphanesinin standart arayüzü, uygulamanın bir I2PSocketManager oluşturmak için I2PSocketManagerFactory'yi kullanmasıdır. Uygulama daha sonra socket manager'dan bir I2PSession ister, bu da [I2CP](/docs/specs/i2cp) aracılığıyla router'a bağlantıya neden olur. Uygulama daha sonra bir I2PSocket ile bağlantıları kurabilir veya bir I2PServerSocket ile bağlantıları alabilir.

İyi bir kullanım örneği için i2psnark koduna bakın.

### Seçenekler ve Varsayılanlar {#options}

Seçenekler ve mevcut varsayılan değerler aşağıda listelenmiştir. Seçenekler büyük-küçük harf duyarlıdır ve tüm router için, belirli bir istemci için veya bağlantı başına tek bir soket için ayarlanabilir. Birçok değer, tipik I2P koşulları altında HTTP performansı için optimize edilmiştir. Peer-to-peer hizmetler gibi diğer uygulamaların, I2PSocketManagerFactory.createManager(_i2cpHost, _i2cpPort, opts) çağrısı aracılığıyla seçenekleri ayarlayarak ve ileterek gerektiği şekilde değiştirmeleri şiddetle önerilir. Zaman değerleri ms cinsindendir.

SAM, [BOB](/docs/legacy/bob) ve [I2PTunnel](/docs/api/i2ptunnel) gibi üst katman API'lerinin bu varsayılan ayarları kendi varsayılan değerleriyle geçersiz kılabileceğini unutmayın. Ayrıca birçok seçeneğin yalnızca gelen bağlantıları dinleyen sunucular için geçerli olduğunu da unutmayın.

0.9.1 sürümü itibariyle, aktif bir socket yöneticisi veya oturumda çoğu seçenek değiştirilebilir, ancak hepsi değil. Ayrıntılar için javadoc'lara bakın.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Default</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.accessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes used for either access list or blacklist. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.destination.sigType</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The name or number of the signature type for a transient destination. As of release 0.9.12.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableAccessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a whitelist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableBlackList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a blacklist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.answerPings</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to respond to incoming pings</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.blacklist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes to be blacklisted for incoming connections to ALL destinations in the context. This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.3.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.bufferSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64K</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How much transmit data (in bytes) will be accepted that hasn't been written out yet.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.congestionAvoidanceGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in congestion avoidance, we grow the window size at the rate of <code>1/(windowSize*factor)</code>. In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to wait after instantiating a new con before actually attempting to connect. If this is &lt;= 0, connect immediately with no initial data. If greater than 0, wait until the output stream is flushed, the buffer fills, or that many milliseconds pass, and include any initial data with the SYN.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5*60*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on connect, in milliseconds. Negative means indefinitely. Default is 5 minutes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.disableRejectLogging</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to disable warnings in the logs when an incoming connection is rejected due to connection limits. As of release 0.9.4.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.dsalist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes or host names to be contacted using an alternate DSA destination. Only applies if multisession is enabled and the primary session is non-DSA (generally for shared clients only). This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.21.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.enforceProtocol</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to listen only for the streaming protocol. Setting to true will prohibit communication with Destinations earlier than release 0.7.1 (released March 2009). Set to true if running multiple protocols on this Destination. As of release 0.9.1. Default true as of release 0.9.36.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 (send)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0=noop, 1=disconnect) What to do on an inactivity timeout - do nothing, disconnect, or send a duplicate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">90*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Idle time before sending a keepalive</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialAckDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">750</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Delay before sending an ack</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialResendDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The initial value of the resend delay field in the packet header, times 1000. Not fully implemented; see below.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial timeout (if no <a href="#sharing">sharing data</a> available). As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial round trip time estimate (if no <a href="#sharing">sharing data</a> available). Disabled as of release 0.9.8; uses actual RTT.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(if no <a href="#sharing">sharing data</a> available) In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.limitAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reset</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">What action to take when an incoming connection exceeds limits. Valid values are: reset (reset the connection); drop (drop the connection); or http (send a hardcoded HTTP 429 response). Any other value is a custom response to be sent. backslash-r and backslash-n will be replaced with CR and LF. As of release 0.9.34.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConcurrentStreams</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0 or negative value means unlimited) This is a total limit for incoming and outgoing combined.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxMessageSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1730</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum size of the payload, i.e. the MTU in bytes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxResends</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Maximum number of retransmissions before failure.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (all peers; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.profile</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 (bulk)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1=bulk; 2=interactive; see important notes <a href="#profile">below</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.readTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on read, in milliseconds. Negative means indefinitely.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.slowStartGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in slow start, we grow the window size at the rate of 1/(factor). In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttdevDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.wdwDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.writeTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on write/flush, in milliseconds. Negative means indefinitely.</td>
    </tr>
  </tbody>
</table>
## Protokol Belirtimi {#spec}

[Streaming Kütüphanesi Spesifikasyon sayfasına bakın.](/docs/specs/streaming)

## Uygulama Detayları {#implementation}

### Kurulum {#setup}

Başlatıcı SYNCHRONIZE bayrağı ayarlanmış bir paket gönderir. Bu paket aynı zamanda başlangıç verisini de içerebilir. Karşı taraf SYNCHRONIZE bayrağı ayarlanmış bir paketle yanıtlar. Bu paket aynı zamanda başlangıç yanıt verisini de içerebilir.

Başlatıcı, SYNCHRONIZE yanıtını almadan önce başlangıç pencere boyutuna kadar ek veri paketleri gönderebilir. Bu paketlerin de gönderme Stream ID alanı 0 olarak ayarlanacaktır. Alıcılar, bilinmeyen akışlarda alınan paketleri kısa bir süre boyunca arabelleğe almalıdır, çünkü bu paketler sıra dışı olarak, SYNCHRONIZE paketinden önce gelebilir.

### MTU Seçimi ve Müzakeresi {#mtu}

Maksimum mesaj boyutu (MTU / MRU olarak da adlandırılır) iki peer tarafından desteklenen daha düşük değere göre müzakere edilir. Tunnel mesajları 1KB'ye doldurulduğu için, kötü bir MTU seçimi büyük miktarda ek yüke yol açar. MTU, i2p.streaming.maxMessageSize seçeneği ile belirtilir. Mevcut varsayılan MTU değeri olan 1730, tipik durum için ek yük dahil olmak üzere tam olarak iki adet 1K I2NP tunnel mesajına sığacak şekilde seçilmiştir.

Not: Bu, yalnızca yük verilerinin maksimum boyutudur, başlık dahil değildir.

Not: Azaltılmış ek yüke sahip ECIES bağlantıları için önerilen MTU 1812'dir. Varsayılan MTU, hangi anahtar türü kullanılırsa kullanılsın tüm bağlantılar için 1730 olarak kalır. İstemciler her zamanki gibi gönderilen ve alınan MTU'nun minimum değerini kullanmalıdır. Öneri 155'e bakın.

Bir bağlantıdaki ilk mesaj, streaming katmanı tarafından eklenen 387 bayt (tipik) Destination ve genellikle 898 bayt (tipik) LeaseSet ile Session anahtarlarını içerir, bunlar router tarafından Garlic mesajında paketlenir. (Daha önce ElGamal Session kurulduysa LeaseSet ve Session Anahtarları paketlenmez). Bu nedenle, tam bir HTTP isteğini tek bir 1KB I2NP mesajına sığdırma hedefi her zaman ulaşılabilir değildir. Ancak, MTU seçimi ve tunnel gateway işlemcisinde fragmentation ve batching stratejilerinin dikkatli uygulanması, özellikle uzun süreli bağlantılarda ağ bant genişliği, gecikme, güvenilirlik ve verimlilik açısından önemli faktörlerdir.

### Veri Bütünlüğü {#integrity}

Veri bütünlüğü, [I2CP katmanında](/docs/specs/i2cp#format) uygulanan gzip CRC-32 sağlama toplamı ile garanti edilir. Streaming protokolünde sağlama toplamı alanı bulunmaz.

### Paket Kapsülleme {#encapsulation}

Her paket I2P üzerinden tek bir mesaj olarak (veya bir [Garlic Message](/docs/overview/garlic-routing) içinde bireysel bir clove olarak) gönderilir. Mesaj kapsülleme, alttaki [I2CP](/docs/specs/i2cp), [I2NP](/docs/specs/i2np) ve [tunnel message](/docs/specs/tunnel-message) katmanlarında uygulanır. Akış protokolünde paket ayırıcı mekanizması veya yük uzunluğu alanı yoktur.

### İsteğe Bağlı Gecikme {#delay}

Veri paketleri, alıcının paketi onaylamadan önce talep edilen gecikmeyi ms cinsinden belirten isteğe bağlı bir gecikme alanı içerebilir. Geçerli değerler 0 ile 60000 arasındadır (dahil). 0 değeri anında onay talep eder. Bu yalnızca tavsiye niteliğindedir ve alıcılar, ek paketlerin tek bir onay ile onaylanabilmesi için biraz gecikme yapmalıdır. Bazı uygulamalar bu alanda (ölçülen RTT / 2) tavsiye değerini içerebilir. Sıfır olmayan isteğe bağlı gecikme değerleri için alıcılar, onay göndermeden önceki maksimum gecikmeyi en fazla birkaç saniye ile sınırlamalıdır. 60000'den büyük isteğe bağlı gecikme değerleri tıkanmayı gösterir, aşağıya bakın.

### İletim/Alma Pencereleri ve Tıkanma {#windows}

TCP başlıkları alım penceresini bayt cinsinden içerir; ancak, streaming protokolü maksimum alım penceresi boyutunu bayt veya paket cinsinden değiştirmek için bir yol sağlamaz. Yalnızca alım arabelleğinin dolu olduğunu gösteren basit bir engelleme/engellemeyi kaldırma göstergesi vardır. Her endpoint, uzak uç alım penceresinin kendi tahminini bayt veya paket cinsinden tutmalıdır. İstemci uygulaması arabelleği boşaltmakta yavaşsa, herhangi bir pencere boyutunda alım arabelleğinin taşabileceğini unutmayın.

Java implementasyonunda varsayılan maksimum iletim ve alma pencere boyutu 128 pakettir. Maksimum iletim pencere boyutunu 128'den yüksek olarak ayarlayan implementasyonlar aşağıdaki konuları göz önünde bulundurmalıdır:

- Java router'larından gelen CHOKE yanıtları, alım buffer taşması nedeniyle çok daha olasıdır.
- Tekrarlanan taşmaları azaltmak için uzak uç alıcı buffer boyutu tahmini uygulanmalıdır (yukarıya bakınız)
- CHOKE doğru şekilde ele alınmalıdır (aşağıya bakınız)
- 256'dan büyük maksimum pencere boyutları daha da hata eğilimlidir, çünkü nack sayısı seçenek alanı uzunluğu bir bayttır ve maksimum NACK'leri 255 ile sınırlar. Bu spesifikasyon 255'den fazla NACK olması durumunda ne yapılacağını ele almaz. 256'dan büyük maksimum pencere boyutları önerilmez.

Alıcı uygulamaları için önerilen minimum tampon boyutu 128 paket veya 232 KB'dir (yaklaşık 128 * 1812). I2P ağ gecikmesi, paket kayıpları ve bunun sonucu olan tıkanıklık kontrolü nedeniyle, bu boyuttaki bir tampon nadiren dolar. Ancak taşma, yüksek bant genişlikli "yerel geri döngü" (aynı router) bağlantılarında veya yerel testlerde çok daha olası bir durumdur.

Taşma durumlarını hızlıca belirtmek ve sorunsuzca kurtulmak için, akış protokolünde pushback için basit bir mekanizma vardır. 60001 veya daha yüksek değerli isteğe bağlı gecikme alanı ile bir paket alınırsa, bu "tıkanma" veya sıfır alma penceresini gösterir. 60000 veya daha düşük değerli isteğe bağlı gecikme alanı olan bir paket "tıkanmayı kaldırmayı" gösterir. İsteğe bağlı gecikme alanı olmayan paketler choke/unchoke durumunu etkilemez.

Choke durumuna alındıktan sonra, kaybolmuş olabilecek unchoke paketlerini telafi etmek için ara sıra gönderilen "probe" veri paketleri haricinde, transmitter unchoke durumuna gelinceye kadar veri içeren başka paket gönderilmemelidir. Choke durumundaki endpoint, TCP'deki gibi probing'i kontrol etmek için bir "persist timer" başlatmalıdır. Unchoke yapan endpoint bu alanı ayarlanmış olarak birkaç paket göndermeli veya tekrar veri paketleri alınana kadar periyodik olarak göndermeye devam etmelidir. Unchoke için beklenecek maksimum süre implementasyona bağlıdır. Unchoke durumundan sonra transmitter pencere boyutu ve tıkanıklık kontrolü stratejisi implementasyona bağlıdır.

### Tıkanıklık Kontrolü {#congestion}

Streaming lib standart yavaş başlangıç (üstel pencere büyümesi) ve tıkanıklık önleme (doğrusal pencere büyümesi) fazlarını üstel geri çekilme ile kullanır. Pencereleme ve onaylamalar bayt sayısı değil, paket sayısı kullanır.

### Kapat {#close}

SYNCHRONIZE bayrağı ayarlanmış olanlar dahil herhangi bir paket, CLOSE bayrağının da gönderilmesini sağlayabilir. Bağlantı, eş CLOSE bayrağı ile yanıt verene kadar kapatılmaz. CLOSE paketleri de veri içerebilir.

### Ping / Pong {#ping}

I2CP katmanında (ICMP echo'ya eşdeğer) veya datagramlarda ping işlevi bulunmamaktadır. Bu işlev streaming'de sağlanmaktadır. Ping'ler ve pong'lar standart bir streaming paketi ile birleştirilemez; ECHO seçeneği ayarlanmışsa, diğer çoğu flag, seçenek, ackThrough, sequenceNum, NACK'ler vb. göz ardı edilir.

Bir ping paketi ECHO, SIGNATURE_INCLUDED ve FROM_INCLUDED bayraklarının ayarlanmış olması gerekir. sendStreamId sıfırdan büyük olmalıdır ve receiveStreamId göz ardı edilir. sendStreamId mevcut bir bağlantıya karşılık gelebilir veya gelmeyebilir.

Bir pong paketi ECHO bayrağının ayarlanmış olması gerekir. sendStreamId sıfır olmalıdır ve receiveStreamId, ping'den gelen sendStreamId'dir. 0.9.18 sürümünden önce, pong paketi ping'de bulunan herhangi bir payload içermez.

0.9.18 sürümünden itibaren, ping ve pong mesajları bir payload içerebilir. Ping içindeki payload, maksimum 32 bayt olmak üzere, pong ile geri döndürülür.

Streaming, i2p.streaming.answerPings=false yapılandırması ile pong gönderimini devre dışı bırakacak şekilde yapılandırılabilir.

### i2p.streaming.profile Notları {#profile}

Bu seçenek iki değeri destekler; 1=toplu ve 2=etkileşimli. Bu seçenek, beklenen trafik desenine dair streaming kütüphanesine ve/veya router'a bir ipucu sağlar.

"Bulk" yüksek bant genişliği için optimize etmek anlamına gelir, muhtemelen gecikme pahasına. Bu varsayılan ayardır. "Interactive" düşük gecikme için optimize etmek anlamına gelir, muhtemelen bant genişliği veya verimlilik pahasına. Optimizasyon stratejileri, varsa, uygulamaya bağımlıdır ve streaming protokolü dışındaki değişiklikleri içerebilir.

API sürüm 0.9.63'e kadar, Java I2P 1 (bulk) dışındaki herhangi bir değer için hata döndürür ve tunnel başlatılamaz. API 0.9.64'ten itibaren, Java I2P bu değeri görmezden gelir. API sürüm 0.9.63'e kadar, i2pd bu seçeneği görmezden gelirdi; API 0.9.64'ten itibaren i2pd'de uygulanmıştır.

Streaming protokolü, profil ayarını karşı tarafa iletmek için bir bayrak alanı içerse de, bu özellik bilinen hiçbir router'da uygulanmamıştır.

### Kontrol Bloğu Paylaşımı {#sharing}

Streaming kütüphanesi "TCP" Kontrol Bloğu paylaşımını destekler. Bu, aynı uzak eş ile yapılan bağlantılar arasında üç önemli streaming kütüphanesi parametresini (pencere boyutu, gidiş-dönüş süresi, gidiş-dönüş süresi varyansı) paylaşır. Bu, bir bağlantı sırasında "topluluk" paylaşımı için değil, bağlantı açma/kapama zamanında "zamansal" paylaşım için kullanılır ([RFC 2140](http://www.ietf.org/rfc/rfc2140.txt)'a bakın). Her ConnectionManager için (yani her yerel Destination için) ayrı bir paylaşım vardır, böylece aynı router üzerindeki diğer Destination'lara bilgi sızıntısı olmaz. Belirli bir eş için paylaşım verileri birkaç dakika sonra sona erer. Aşağıdaki Kontrol Bloğu Paylaşımı parametreleri router başına ayarlanabilir:

- RTT_DAMPENING = 0.75
- RTTDEV_DAMPENING = 0.75
- WINDOW_DAMPENING = 0.75

### Diğer Parametreler {#other}

Aşağıdaki parametreler önerilen varsayılan değerlerdir. Varsayılan değerler uygulamaya bağlı olarak değişebilir:

- MIN_RESEND_DELAY = 100 ms (minimum RTO)
- MAX_RESEND_DELAY = 45 saniye (maximum RTO)
- MIN_WINDOW_SIZE = 1
- MAX_WINDOW_SIZE = 128
- TREND_COUNT = 3
- MIN_MESSAGE_SIZE = 512 (minimum MTU)
- INBOUND_BUFFER_SIZE = maxMessageSize * (maxWindowSize + 2)
- INITIAL_TIMEOUT (yalnızca RTT örneklenmeden önce geçerli) = 9 saniye
- "alpha" ( RFC 6298'e göre RTT sönümleme faktörü ) = 0.125
- "beta" ( RFC 6298'e göre RTTDEV sönümleme faktörü ) = 0.25
- "K" ( RFC 6298'e göre RTDEV çarpanı ) = 4
- PASSIVE_FLUSH_DELAY = 175 ms
- Maksimum RTT tahmini: 60 saniye

### Geçmiş {#history}

Streaming kütüphanesi I2P için organik olarak büyümüştür - önce mihi, I2PTunnel'ın bir parçası olarak "mini streaming kütüphanesini" uygulamıştır, bu 1 mesaj pencere boyutuyla sınırlıydı (bir sonrakini göndermeden önce ACK gerektiriyordu), daha sonra bu generic streaming arayüzüne (TCP soketlerini yansıtan) dönüştürülmüş ve tam streaming uygulaması, yüksek bant genişliği x gecikme çarpımını hesaba katan kayan pencere protokolü ve optimizasyonlarla dağıtılmıştır. Bireysel stream'ler maksimum paket boyutunu ve diğer seçenekleri ayarlayabilir. Varsayılan mesaj boyutu, tam olarak iki adet 1K I2NP tunnel mesajına sığacak şekilde seçilmiştir ve kayıp mesajları yeniden iletmenin bant genişliği maliyetleri ile birden fazla mesajın gecikmesi ve ek yükü arasında makul bir dengedir.

## Gelecekteki Çalışmalar {#future}

Streaming kütüphanesinin davranışı, uygulama düzeyindeki performans üzerinde derin bir etkiye sahiptir ve bu nedenle daha ileri analiz için önemli bir alandır.

- Streaming lib parametrelerinin ek ayarlanması gerekli olabilir.
- Araştırma için başka bir alan da streaming lib'in NTCP ve SSU transport katmanları ile etkileşimidir. Ayrıntılar için [NTCP tartışma sayfasına](/docs/historical/ntcp-discussion) bakın.
- Routing algoritmalarının streaming lib ile etkileşimi performansı güçlü bir şekilde etkiler. Özellikle, mesajların bir havuzdaki birden fazla tunnel'a rastgele dağıtılması, yüksek derecede sıra dışı teslimat ile sonuçlanır ve bu da normalde olacağından daha küçük pencere boyutlarına yol açar. Router şu anda tek bir from/to hedef çifti için mesajları, tunnel'ın süresi dolana veya teslimat hatası oluşana kadar tutarlı bir tunnel seti aracılığıyla yönlendirir. Router'ın hata ve tunnel seçim algoritmaları olası iyileştirmeler için gözden geçirilmelidir.
- İlk SYN paketindeki veriler alıcının MTU'sunu aşabilir.
- DELAY_REQUESTED alanı daha fazla kullanılabilir.
- Kısa ömürlü akışlarda duplicate başlangıç SYNCHRONIZE paketleri tanınmayabilir ve kaldırılmayabilir.
- Yeniden iletimde MTU gönderme.
- Giden pencere dolu olmadığı sürece veriler gönderilir. (yani no-Nagle veya TCP_NODELAY) Muhtemelen bunun için bir yapılandırma seçeneği olmalı.
- zzz paketleri wireshark-uyumlu (pcap) formatta kaydetmek için streaming library'ye debug kodu eklemiştir; Performansı daha fazla analiz etmek için bunu kullanın. Format, daha fazla streaming lib parametresini TCP alanlarına eşlemek için geliştirme gerektirebilir.
- Streaming lib'i standart TCP (veya belki raw socketlerle birlikte null katman) ile değiştirme önerileri vardır. Bu ne yazık ki streaming lib ile uyumsuz olacaktır ancak ikisinin performansını karşılaştırmak iyi olacaktır.
