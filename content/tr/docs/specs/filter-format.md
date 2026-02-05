---
title: "Erişim Filtresi Biçimi"
description: "Tunnel erişim kontrolü filtre dosyaları söz dizimi"
slug: "filter-format"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
type: docs
---

## Genel Bakış

Bir filtrenin tanımı, String'lerden oluşan bir listedir. Boş satırlar ve `#` ile başlayan satırlar göz ardı edilir. Filtre tanımındaki değişiklikler tunnel'ın yeniden başlatılmasıyla geçerli olur.

Her satır şu öğelerden birini temsil edebilir:

- Bu dosyada veya referans verilen dosyalarda listelenmemiş herhangi bir uzak hedefe uygulanacak varsayılan eşik tanımı
- Belirli bir uzak hedefe uygulanacak eşik tanımı
- Bir dosyada listelenen uzak hedeflere uygulanacak eşik tanımı
- İhlal edildiğinde suçlu uzak hedefin belirtilen bir dosyaya kaydedilmesine neden olacak eşik tanımı

Tanımların sırası önemlidir. Belirli bir hedef için ilk eşik (açık olarak belirtilmiş veya bir dosyada listelenmiş olsun) aynı hedef için gelecekteki tüm eşikleri geçersiz kılar, ister açık olarak belirtilmiş ister bir dosyada listelenmiş olsun.

## Eşik Değerleri

Bir eşik, uzak bir hedefin belirli bir saniye sayısı içinde bir "ihlal" gerçekleşmeden önce gerçekleştirmesine izin verilen bağlantı denemesi sayısıyla tanımlanır. Örneğin, aşağıdaki eşik tanımı `15/5`, aynı uzak hedefin 5 saniyelik bir süre içinde 14 bağlantı denemesi yapmasına izin verildiği anlamına gelir. Aynı süre içinde bir deneme daha yaparsa, eşik ihlal edilmiş olacaktır.

Eşik formatı aşağıdakilerden biri olabilir:

- Saniye sayısına göre bağlantı sayısının **sayısal tanımı** - `15/5`, `30/60` vb. Bağlantı sayısının 1 olduğu durumda (örneğin `1/1`) ilk bağlantı denemesinin ihlal ile sonuçlanacağını unutmayın.
- **`allow`** kelimesi. Bu eşik hiçbir zaman ihlal edilmez, yani sınırsız sayıda bağlantı denemesine izin verilir.
- **`deny`** kelimesi. Bu eşik her zaman ihlal edilir, yani hiçbir bağlantı denemesine izin verilmez.

### Varsayılan Eşik

Varsayılan eşik, tanımda veya başvurulan dosyalarda açıkça listelenmemiş olan herhangi bir uzak hedef için geçerlidir. Varsayılan bir eşik belirlemek için `default` anahtar kelimesini kullanın. Aşağıdakiler varsayılan eşik örnekleridir:

```text
15/5 default
allow default
deny default
```
Her filtre için yalnızca bir varsayılan eşik tanımı olabilir. Eğer atlanırsa, filtre varsayılan olarak bilinmeyen bağlantılara izin verecektir.

### Açık Eşik Değerleri

Açık eşikler, tanımın kendisinde listelenen uzak bir hedefe uygulanır. Örnekler:

```text
15/5 explicit asdfasdfasdf.b32.i2p
allow explicit fdsafdsafdsa.b32.i2p
deny explicit qwerqwerqwer.b32.i2p
```
### Toplu Eşik Değerleri

Kolaylık için, destinasyonların listesini bir dosyada tutmak ve hepsi için toplu olarak bir eşik değeri tanımlamak mümkündür. Örnekler:

```text
15/5 file /path/throttled_destinations.txt
deny file /path/forbidden_destinations.txt
allow file /path/unlimited_destinations.txt
```
Bu dosyalar tunnel çalışırken elle düzenlenebilir. Bu dosyalardaki değişikliklerin etkili olması 10 saniyeye kadar sürebilir.

## Kayıtçılar

Recorder'lar uzak bir destination tarafından yapılan bağlantı denemelerini takip eder ve bu belirli bir eşiği aşarsa, o destination belirtilen dosyada kaydedilir. Örnekler:

```text
30/5 record /path/aggressive.txt
60/5 record /path/very_aggressive.txt
```
Agresif hedefleri belirtilen bir dosyaya kaydetmek için bir kaydedici kullanmak ve daha sonra bu dosyayı onları daraltmak için kullanmak mümkündür. Örneğin, aşağıdaki kod parçacığı başlangıçta tüm bağlantı denemelerine izin veren, ancak herhangi bir hedef 5 saniyede 30 denemeyi aşarsa onu 5 saniyede 15 denemeye düşüren bir filtre tanımlayacaktır:

```text
# by default there are no limits
allow default
# but record overly aggressive destinations
30/5 record /path/throttled.txt
# and any that end up in that file will get throttled in the future
15/5 file /path/throttled.txt
```
Bir tunnel'da başka bir tunnel'ı kısıtlayan bir dosyaya yazan bir kaydedici kullanmak mümkündür. Aynı dosyayı birden fazla tunnel'daki hedeflerle yeniden kullanmak mümkündür. Ve tabii ki, bu dosyaları elle düzenlemek de mümkündür.

İşte varsayılan olarak bazı kısıtlamalar uygulayan, `friends.txt` dosyasındaki destinationlar için kısıtlama yapmayan, `enemies.txt` dosyasındaki destinationlardan gelen bağlantıları yasaklayan ve herhangi bir saldırgan davranışı `suspicious.txt` adlı bir dosyaya kaydeden örnek bir filtre tanımı:

```text
15/5 default
allow file /path/friends.txt
deny file /path/enemies.txt
60/5 record /path/suspicious.txt
```