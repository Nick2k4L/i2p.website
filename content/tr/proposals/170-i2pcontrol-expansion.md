---
title: "I2PControl Genişletmesi"
number: "170"
author: "Nick2k4"
created: "2026-05-20"
lastupdated: "2026-05-20"
status: "Aç"
toc: true
---

## Genel Bakış

Bu öneri, i2pcontrol API'sine yeni bilgiler sunarak daha fazla esneklik sağlar. Bu bilgiler, adres defterlerine ekleme, silme, geri alma ve değiştirme işlemlerinin yanı sıra gizli hizmetleri de içerir. Bu öneri aynı zamanda yönlendiriciniz hakkında eşler, haberler, netdb ve daha fazlası gibi daha fazla bilgiyi de ortaya çıkarır.

## Motivasyon

Bu teklifin kullanım senaryosu, standart i2p tünel takımıyla birlikte her yönlendirici uygulamasında paylaşılabilen birleştirilmiş ve sadeleştirilmiş bir yönlendirici konsolu oluşturmaktır. Temelde bu teklif, I2P ağındaki kullanıcılar için daha sezgisel ve kullanıcı dostu bir deneyim sağlar.

Bu öneri, uygulamaların bir I2P yönetim arayüzünü uygulaması ve yönetmesi için I2P API'sinde daha büyük esneklik sağlamayı da mümkün kılacaktır. i2pcontrol'e bu tür bilgilerin sunulması, kullanıcıların daha gelişmiş uygulamalar oluşturmasına ve uzaktan yönetim için daha iyi destek sağlamasına olanak tanır.

## Tasarım

Kullanıcılar i2pcontrol API'siyle etkileşime girdiğinde, yukarıda bahsedilen bilgileri sağlayan yeni uç noktalara erişebilecekler. Örneğin, i2pcontrol API'si, kullanıcıların tünel ve adres defterleri oluşturmak, silmek, almak ve değiştirmek için parametreler girebilecekleri yeni `TunnelManager` ve `AddressBook` metodlarını ortaya çıkaracak. Ayrıca, önceden var olan `RouterInfo` metodu, yönlendirici hakkında bilgi vermek için yeni parametrelere sahip olacaktır.

## Güvenlik etkileri

Bu öneriden kaynaklı beklenen ek güvenlik etkileri yoktur çünkü ortaya çıkarılan bilgi zaten diğer yollarla erişilebilirdir. Ancak hassas bilgilere erişimin veya yönlendirici üzerinde kontrolün yetkisiz erişime karşı korunabilmesi için i2pcontrol API'sine erişimde uygun kimlik doğrulama ve yetkilendirme mekanizmalarının yerinde olduğundan emin olmak önemlidir.

## API Spesifikasyonu ve Yöntemleri

Tüm istekler JSON-RPC 2.0 yapısını takip eder:

```json
{
  "jsonrpc": "2.0",
  "method": "MethodName",
  "params": {
    // method-specific parameters
  },
  "id": 1
}
```
### Yöntem - RouterInfo (ALICILAR)

Aşağıda, `RouterInfo` yöntemi için yeni parametreler ve bunların döndürdükleri yer alır:

- `i2p.router.news` - tüm yönlendirici haberlerini döndürür. Dönüş Türü - `String`
- `i2p.router.id` - yönlendirici karmasını Base64 dizesi olarak veya `null` döndürür. Dönüş Türü - `String`
- `i2p.router.clockskew` - ortalama eş saat sapmasını veya `null` döndürür. Dönüş Türü - `long`
- `i2p.router.info` - serileştirilmiş RouterInfo'yu Base64 dizesi olarak veya `null` döndürür. Dönüş Türü - `String`
- `i2p.router.logs` - son yönlendirici log mesajlarını döndürür. Dönüş Türü - `List<String>`
- `i2p.router.logs.clear` - yönlendirici log arabelleğini temizler ve `"success"` döndürür. Dönüş Türü - `String`

- `i2p.router.net.total.received.bytes` - başlangıçtan bu yana alınan toplam baytları döndürür. *(i2pd'den alınmıştır)* Dönüş Türü - `long`
- `i2p.router.net.total.sent.bytes` - başlangıçtan bu yana gönderilen toplam baytları döndürür. *(i2pd'den alınmıştır)* Dönüş Türü - `long`
- `i2p.router.net.total.transit.bytes` - başlangıçtan bu yana iletilen toplam transit baytlarını döndürür. *(i2pd'den alınmıştır)* Dönüş Türü - `long`
- `i2p.router.net.bw.transit.15s` - 15 saniyelik ortalama transit bant genişliğini döndürür (bayt/saniye). *(i2pd'den alınmıştır)* Dönüş Türü - `long`

- `i2p.router.net.tunnels.shareratio` - tünel paylaşım oranını döndürür. Dönüş Türü - `double`
- `i2p.router.net.tunnels.participating.info` - katılımcı tünel bilgisini döndürür. Dönüş Türü - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.i2ptunnel` - yapılandırılmış I2PTunnel denetleyici bilgisini döndürür (tümünün hızlı istatistikleri). Dönüş Türü - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.exploratory.inbound` - keşif amaçlı gelen tünel sayısını döndürür. Dönüş Türü - `int`
- `i2p.router.net.tunnels.exploratory.outbound` - keşif amaçlı giden tünel sayısını döndürür. Dönüş Türü - `int`
- `i2p.router.net.tunnels.exploratory.info.list` - keşif amaçlı tünellerin bilgi listesini döndürür. Dönüş Türü - `List<Map<String, Object>>`
- `i2p.router.net.tunnels.client.inbound` - istemciye ait gelen tünel sayısını döndürür. Dönüş Türü - `int`
- `i2p.router.net.tunnels.client.outbound` - istemciye ait giden tünel sayısını döndürür. Dönüş Türü - `int`
- `i2p.router.net.tunnels.client.info.list` - istemci tünellerinin bilgi listesini döndürür. Dönüş Türü - `List<Map<String, Object>>`

- `i2p.router.net.status.v6` - IPv6 ağ durumu kodunu döndürür. *(i2pd'den alınmıştır)* Dönüş Türü - `int`
- `i2p.router.net.error` - IPv4 ağ hata kodunu döndürür. *(i2pd'den alınmıştır)* Dönüş Türü - `int`
- `i2p.router.net.error.v6` - IPv6 ağ hata kodunu döndürür. *(i2pd'den alınmıştır)* Dönüş Türü - `int`
- `i2p.router.net.testing` - IPv4 ağının test durumunda olup olmadığını döndürür (0 veya 1). *(i2pd'den alınmıştır)* Dönüş Türü - `int`
- `i2p.router.net.testing.v6` - IPv6 ağının test durumunda olup olmadığını döndürür (0 veya 1). *(i2pd'den alınmıştır)* Dönüş Türü - `int`

- `i2p.router.net.tunnels.successrate` - Son tunel oluşturma başarı oranını (%) döndürür. *(i2pd'den alınmıştır)* Dönüş Türü - `double`
- `i2p.router.net.tunnels.totalsuccessrate` - Başlangıçtan beri toplam tunel oluşturma başarı oranını (%) döndürür. *(i2pd'den alınmıştır)* Dönüş Türü - `double`
- `i2p.router.net.tunnels.queue` - Tunel oluşturma istek kuyruğu boyutunu döndürür. *(i2pd'den alınmıştır)* Dönüş Türü - `int`
- `i2p.router.net.tunnels.tbmqueue` - Tunel Oluşturma Mesajı kuyruğu boyutunu döndürür. *(i2pd'den alınmıştır)* Dönüş Türü - `int`

- `i2p.router.netdb.peers` - bilinen eş hash'lerinin bir listesini döndürür. Dönüş Türü - `List<String>`
- `i2p.router.netdb.activepeers.info` - etkin eşler için serileştirilmiş RouterInfo verilerini döndürür. Dönüş Türü - `List<String>`
- `i2p.router.netdb.ntcp.limit` - NTCP bağlantı sınırını döndürür. Dönüş Türü - `int`
- `i2p.router.netdb.ssu.limit` - SSU bağlantı sınırını döndürür. Dönüş Türü - `int`
- `i2p.router.netdb.bannedpeers` - yasaklanmış eşleri ve yasaklama ayrıntılarını döndürür. Dönüş Türü - `Map<String, Map<String, Object>>`
- `i2p.router.netdb.activepeers.list` - etkin eş hash'lerini döndürür. Dönüş Türü - `List<String>`
- `i2p.router.netdb.peers.list` - bilinen eş hash'lerini döndürür. Dönüş Türü - `List<String>`
- `i2p.router.netdb.peers.info` - bilinen eşler için serileştirilmiş RouterInfo verilerini döndürür. Dönüş Türü - `List<String>`
- `i2p.router.netdb.activepeers.stats` - etkin eş istatistiklerini döndürür. Dönüş Türü - `List<Map<String, Object>>`

- `i2p.router.addressbook.private.list` - özel adres defteri girişlerini döndürür. Dönüş Türü - `List<Map<String, String>>`
- `i2p.router.addressbook.local.list` - yerel adres defteri girişlerini döndürür. Dönüş Türü - `List<Map<String, String>>`
- `i2p.router.addressbook.router.list` - yönlendirici adres defteri girişlerini döndürür. Dönüş Türü - `List<Map<String, String>>`
- `i2p.router.addressbook.published.list` - yayınlanan adres defteri girişlerini döndürür. Dönüş Türü - `List<Map<String, String>>`
- `i2p.router.addressbook.subscriptions` - abonelik dosya yolunu ve girişlerini döndürür. Dönüş Türü - `Map<String, Object>`
- `i2p.router.addressbook.config` - adres defteri yapılandırma yolunu ve girişlerini döndürür. Dönüş Türü - `Map<String, Object>`

Örnek:

```json
{
    "jsonrpc": "2.0",
    "method": "RouterInfo",
    "params": {
        "i2p.router.id": "",
    },
    "id": 1
}
```
Dönüş:

```json
{
    "jsonrpc": "2.0",
    "result": "{ data }",
    "id": 1
}
```
### Yöntem - Adres Defteri (AYARLAYICILAR)

`AddressBook` yöntemi için, adres defterine giriş eklemek ve silmek amacıyla üç parametre/bağımsız değişken gereklidir:

- `Type` - adres defteri türüne karşılık gelir:
  - `private`
  - `local`
  - `router`
  - `published`
- `Hostname` - adres defteri girdisiyle ilişkili ana bilgisayar adı veya etki alan adına karşılık gelir.
- `Destination` - adres defteri girdisiyle ilişkili hedefe karşılık gelir.
- `Delete` - bu parametre isteğe bağlıdır ve bir adres defteri girişini silmek için kullanılır. Bu parametre sağlanmazsa, yöntem adres defterine yeni bir giriş ekler.

Örnek:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "Type": "private",
    "Hostname": "example.i2p",
    "Destination": "exampleDestinationString",
    "Delete": "" <--- this parameter is optional
  },
  "id": 1
}
```
Dönüş:

```json
{
  "jsonrpc": "2.0",
  "success": true or false,        
  "message": "Deleted/Added (hostname) in (address book type) address book" OR "Failed to delete/add (hostname) to (address book type) address book",
  "id": 1
}
```
Adres Defteri Aboneliklerini düzenlemek için:

- `SetSubscriptions` - bu parametre, bir adres defteri girdisi için abonelikleri ayarlamak üzere kullanılır. Argüman olarak bir dize listesi alır.

Örnek:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetSubscriptions": ["notbob.i2p", "helloworld.i2p", ...]
  },
  "id": 1
}
```
Dönüş:

```json
{
  "jsonrpc": "2.0",
  "success": true,
  "message": "Successfully modified: /path/to/subscriptions.txt"
}
```
Adres Defteri Yapılandırması'nı düzenlemek için:

- `SetConfig` - bu parametre, bir adres defteri girdisi için yapılandırmayı ayarlamak amacıyla kullanılır.

Yapılandırma ayarlarını içeren bir JSON nesnesini bağımsız değişken olarak alır.

Mevcut/sık kullanılan yapılandırma parametreleri:

- `subscriptions` - abonelik URL'lerinin listesini içeren dosya.
- `update_delay` - saat cinsinden güncelleme aralığı.
- `published_addressbook` - yayımlanmış adres defterine giden yol.
- `router_addressbook` - yönlendirici adres defterine giden yol.
- `local_addressbook` - yerel adres defterine giden yol.
- `private_addressbook` - özel adres defterine giden yol.
- `proxy_port` - eepProxy portu.
- `proxy_host` - eepProxy ana bilgisayar adı.
- `should_publish` - yayımlanmış adres defterinin güncellenip güncellenmeyeceğini belirtir.
- `etags` - abonelik URL'lerinin etag'lerini içeren dosya.
- `last_modified` - abonelik URL'lerinin son değiştirilme zaman damgalarını içeren dosya.
- `log` - log dosyası yolu.
- `theme` - tema.

Örnek:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetConfig": {
      "subscriptions": "subscriptions.txt",
      "update_delay": "12",
      "published_addressbook": "../eepsite/docroot/hosts.txt",
      "router_addressbook": "hosts.txt",
      "local_addressbook": "../userhosts.txt",
      "private_addressbook": "../privatehosts.txt",
      "proxy_port": "4444",
      "proxy_host": "127.0.0.1",
      "should_publish": "true",
      "etags": "etags.txt",
      "last_modified": "last_modified.txt",
      "log": "log.txt",
      "theme": "light"
    }
  },
  "id": 1
}
```
Dönüş:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "success": true,
    "message": "Successfully modified: /path/to/config.txt"
  },
  "id": 1
}
```
### Yöntem - TunnelManager (1 İŞARETLİ ALICI, DİĞERLERİ AYARLAYICI)

`TunnelManager` yöntemi, I2PTunnel denetleyicilerini oluşturmak, düzenlemek, almak, başlatmak, durdurmak, yeniden başlatmak ve silmek için kullanılır.

Gerekli parametreler:

- `Name` - tünelin adı. Bu, tünelin tanımlayıcısıdır.
- `Action` - gerçekleştirilecek işlem:
  - `create`
  - `edit`
  - `get`
  - `start`
  - `stop`
  - `restart`
  - `delete`

İsteğe bağlı parametreler:

- `All` - boolean, eylemin tüm tünellerde uygulanıp uygulanmayacağını belirtir. Bu yalnızca `start`, `stop` ve `restart` eylemleri için geçerlidir.

`create` için desteklenen tünel türleri:

- `client` (istemci)
- `httpclient` (HTTP istemcisi)
- `ircclient` (IRC istemcisi)
- `socks` (SOCKS)
- `socksirc` (SOCKS IRC)
- `connectclient` (bağlantı istemcisi)
- `streamrclient` (akış istemcisi)

- `server`
- `httpserver`
- `httpbidirserver`
- `ircserver`
- `streamrserver`

Tünel oluşturmak/düzenlemek için ortak parametreler:

- `Type` - tünel türü. `create` için gereklidir.
- `NewName` - düzenleme sırasında isteğe bağlı yeni ad.
- `Port` - yerel dinleme portu.
- `TargetHost` veya `Host` - sunucu tünelleri için hedef makine.
- `TargetPort` - sunucu tünelleri için hedef port.
- `TargetDestination` veya `Destination` - bir hedef gerektiren istemci tünelleri için hedef.
- `StartOnLoad` - mantıksal değer, tünel yüklendiğinde başlamalı mı.
- `Description` - tünel açıklaması.
- `ReachableBy` - tünelin dinlediği arayüz/adres.
- `Shared` - mantıksal değer, istemci tüneli paylaşılmalı mı.
- `UseSSL` - mantıksal değer, desteklendiği yerlerde SSL etkinleştirilsin mi.
- `TunnelLength` - tünel uzunluğu, `0` ile `3` arasında.
- `TunnelVariance` - tünel varyansı, `-2` ile `2` arasında.
- `TunnelQuantity` - tünel miktarı, `1` ile `6` arasında.
- `TunnelBackupQuantity` - yedek tünel miktarı, `0` ile `3` arasında.
- `SigType` - imzalama anahtarı türü.
- `EncType` - şifreleme türü.
- `CustomOptions` - özel tünel seçenekleri.

İstemci vekil sunucu seçenekleri:

- `ProxyList`
- `UseOutproxyPlugin`
- `ProxyAuth`
- `ProxyUsername`
- `ProxyPassword`
- `OutproxyAuth`
- `OutproxyUsername`
- `OutproxyPassword`
- `OutproxyType`
- `SSLProxies`
- `JumpList`

İstemci yönetim seçenekleri:

- `ConnectDelay`
- `Profile`
- `DelayOpen`
- `Reduce`
- `ReduceCount`
- `ReduceTime`
- `Close`
- `CloseTime`
- `NewDest`
- `PersistentClientKey`
- `PrivKeyFile`

HTTP istemci filtreleme seçenekleri:

- `AllowUserAgent`
- `AllowReferer`
- `AllowAccept`
- `AllowInternalSSL`

Sunucu seçenekleri:

- `WebsiteHostname` veya `SpoofedHost`
- `BlockAccessInProxies`
- `BlockUserAgents`
- `UserAgents`
- `UniqueLocalAddressPerClient`
- `BlockReferers`
- `MultiHoming`
- `AccessOption`
- `AccessList`
- `FilterFilePath`
- `MaxConcurrentConns`
- `ClientPerMinute`
- `ClientPerHour`
- `ClientPerDay`
- `TotalInPerMinute`
- `TotalInPerHour`
- `TotalInPerDay`
- `PostLimit`
- `PostLimitTime`
- `PerClientPeriod`
- `TotalPeriod`
- `TotalBanTime`

LeaseSet seçenekleri:

- `EncryptLeaseSet` - aşağıdakilerden biri:
  - `disable`
  - `encrypted (aes)`
  - `blinded`
  - `blinded with lookup password`
  - `encrypted (psk)`
  - `encrypted with lookup password (psk)`
  - `encrypted with per-user key (psk)`
  - `encrypted with lookup password and per-user key (psk)`
  - `encrypted with per-user key (dh)`
  - `encrypted with lookup password and per-user key (dh)`
- `OptionalLookup`
- `LeaseSetClientAuths`

Örnek oluştur:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "create",
    "Type": "client",
    "Port": 7656,
    "TargetDestination": "exampleDestinationString",
    "StartOnLoad": false,
    ....
  },
  "id": 1
}
```
Dönüş:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - created tunnel example-client" OR "error - { error message }",
    "results": [ {/* information about where persistent keys are stored */} ]
  },
  "id": 1
}
```
Düzenleme örneği:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "edit",
    "NewName": "renamed-client",
    "Port": 7657,
    "TargetDestination": "newDestinationString",
    "StartOnLoad": true
  },
  "id": 1
}
```
Dönüş:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - edited tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
Örnek al (SADECE GETTER) Şunu döndürür - `Map<String, Object>` (bilgi) ve `String` (durum):

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "get"
  },
  "id": 1
}
```
Dönüş:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - options for example-client" OR "error - { error message }",
    "info": {
      "client": true,
      "status": "running",
      "persistentClientKey": false,
      "offlineKeys": false,
      "targetDestination": "exampleDestinationString",
      "localDestination": "exampleBase64Destination",
      "destination": "exampleBase64Destination",
      "destinationB32": "example.b32.i2p",
      "rawConfig": {
        "name": "example-client",
        "type": "client"
      }
    }
  },
  "id": 1
}
```
Başlat, Durdur, Yeniden Başlat, Örneği Sil. Aynı yapıya sahiptirler, sadece farklı `Action` parametreleri kullanılır:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "start"
  },
  "id": 1
}
```
Dönüş:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - starting tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
### Yöntem - ClientServicesInfo *(i2pd'den uyarlanmıştır)*

`ClientServicesInfo` yöntemi, yönlendirici üzerinde çalışan istemci hizmetleriyle ilgili durum bilgilerini döndürür. Her hizmetin durumunu istemek için, istenen hizmet anahtarlarını (herhangi bir değerle birlikte) `params` içine ekleyin.

Desteklenen parametreler:

- `I2PTunnel` - yapılandırılmış tünel adlarını adreslerine eşleyen bir harita döndürür ve bu harita `client` ve `server` alt nesnelerine ayrılır.
- `HTTPProxy` - HTTP vekilinin etkin durumunu ve adresini döndürür.
- `SOCKS` - SOCKS vekilinin etkin durumunu ve adresini döndürür.
- `SAM` - SAM köprüsünün etkin durumunu ve etkin oturum bilgilerini döndürür.
- `BOB` - BOB köprüsünün etkin durumunu döndürür. (Java I2P'de kullanım dışıdır; her zaman `false` döndürür.)
- `I2CP` - I2CP sunucusunun etkin durumunu döndürür.

Örnek:

```json
{
  "jsonrpc": "2.0",
  "method": "ClientServicesInfo",
  "params": {
    "I2PTunnel": "",
    "SAM": ""
  },
  "id": 1
}
```
Dönüş:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "I2PTunnel": {
      "client": {"my-client": {"address": "example.b32.i2p"}},
      "server": {"my-server": {"address": "example.b32.i2p", "port": 8080}}
    },
    "SAM": {
      "enabled": true,
      "sessions": {}
    }
  },
  "id": 1
}
```
## Uyumluluk

Yeni yöntemlerin ve parametrelerin mevcut işlevselliği etkilemeyecek şekilde eklenmesi nedeniyle, mevcut i2pcontrol API'si ile uyumluluk korunmalıdır. i2pcontrol API'sini kullanan mevcut uygulamalar değişiklik yapılmadan çalışmaya devam etmelidir, bu önerinin sağladığı ek bilgilerden ve yeteneklerden ise yeni uygulamalar yararlanabilir.

## Uygulama

### Java I2P

Bu öneri henüz Java I2P'de uygulanmadı, ancak kod [i2p.plugins.i2pcontrol](https://github.com/i2p/i2p.plugins.i2pcontrol) deposunda çekme isteği [#6](https://github.com/i2p/i2p.plugins.i2pcontrol/pull/6) altında mevcuttur. Mevcut kodu etkilemeden yeni yöntemlerin test edilmesi ve geliştirilmesi için bu şekilde yapılmıştır. Kod üretim kullanımı için hazır olduğunda ana I2P deposuna i2pcontrol dizini altında entegre edilecektir.

### i2pd

"(i2pd'den alınan)" olarak işaretlenen yöntemler ve parametreler i2pd içinde uygulanmış olup bu teklif kapsamında değiştirilmemiştir. i2pd'nin uzantıları bu teklif kapsamında herhangi bir değişiklik gerektirmeyecektir. Bu teklifte işaretsiz olarak kalan bölümler i2pd'de uygulanmamıştır.

### go-i2p

go-i2p, yönlendirici konsolu uygulamasını etkinleştirmek ve geliştirmek amacıyla bu öneriyi benimsemeye ve ileride uygulamaya isteklidir.

### emissary

Emissary'de benimsenme olasılığı şu anda bilinmiyor, ancak Emissary'nin bu tekliften go-i2p ile aynı şekillerde yararlanması muhtemeldir.

## Performans

Performans etkisi beklenmiyor.
