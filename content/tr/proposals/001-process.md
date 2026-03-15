---
title: "I2P Öneri Süreci"
number: "001"
author: "str4d"
created: "2016-04-10"
lastupdated: "2017-04-07"
status: "Meta"
thread: "http://zzz.i2p/topics/1980"
toc: true
---
## Genel Bakış

Bu belge, I2P spécifikasyonlarını nasıl değiştireceğinizi, I2P önerilerinin nasıl çalıştığını ve önerilerin spécifikasyonlarla ilişkisini açıklar.

Bu belge, Tor öneri sürecinden uyarlanmıştır ve aşağıdaki içeriğin büyük bir kısmı orijinal olarak Nick Mathewson tarafından yazılmıştır.

Bu, bir bilgilendirme belgesidir.

## Motivasyon

Önceden, I2P spécifikasyonlarını güncelleme sürecimiz oldukça gayriresmîydı: geliştirme forumunda bir öneri yapar ve değişiklikleri tartışır, ardından uzlaşıya varır ve spécifikasyonu taslak değişikliklerle güncellerdik (her zaman bu sırayla olmayabilirdi), ve sonunda değişiklikleri uygulardık.

Bu, birkaç problema neden oluyordu.

İlk olarak, eski süreç even en verimli haliyle bile, spécifikasyonun kodu ile senkron dışı kalmasına neden oluyordu. En kötü durumlar, ertelenen uygulamalardı: spécifikasyon ve kod, sürümler boyunca senkron dışı kalabiliyordu.

İkincisi, tartışmaya katıllemek zordu, çünkü tartışma thread'ının hangi kısımlarının önerinin bir parçası olduğu veya hangi spécifikasyon değişikliklerinin uygulandığı her zaman açık değildi. Geliştirme forumları yalnızca I2P içinde erişilebiliyordu, bu nedenle öneriler yalnızca I2P kullanan kişiler tarafından görülebiliyordu.

Üçüncüsü, bazı önerileri unutmak çok kolaydı, çünkü forum thread listesinde birkaç sayfa geriye gömülüyorlardı.

## Spécifikasyonları şimdi nasıl değiştirebiliriz

İlk olarak, birisi bir öneri belgesi yazar. Detaylı olarak yapılması gereken değişikliği açıklamalı ve nasıl uygulanacağını vermek için bir fikir vermelidir. Bir kez yeterli ölçüde ete kemiğe büründüğünde, bir öneri haline gelir.

Bir RFC gibi, her öneri bir numara alır. RFC'lerden farklı olarak, öneriler zamanla değişebilir ve aynı numara ile kabul edilene veya reddedilene kadar kalabilir. Her öneri için tarih, I2P web sitesi deposunda saklanır.

Bir kez depoda olan bir öneri, ilgili thread'de tartışılmalı ve uzlaşıya varana kadar geliştirilmelidir ki, iyi bir fikir olduğu ve uygulanmak için yeterli ayrıntı içerdiği konusunda uzlaşıya varılmalıdır. Bu gerçekleştiğinde, öneri uygulanır ve spécifikasyonlara entegre edilir. Böylece, spécifikasyonlar I2P protokolü için kanonik belgeler olarak kalır: hiçbir öneri, uygulanan bir özelliğin kanonik belgesi olmaz.

(Bu süreç, Python Enhancement Process'e oldukça benzer, ancak I2P önerilerinin, uygulanmadan sonra spécifikasyonlara yeniden entegre edildiği önemli bir fark vardır, oysa PEP'ler *yeni spécifikasyon* haline gelir.)

### Küçük değişiklikler

Spécifikasyona doğrudan küçük değişiklikler yapmak hala kabul edilebilir, eğer kod hemen yazılabilirse veya cosmetic değişiklikler gerektiriyorsa, kod değişikliği gerekmiyorsa. Bu belge, mevcut geliştiricilerin *niyetini* yansıtır, gelecekte her zaman bu süreci kullanma sözü vermez: gerçekten heyecanlanıp ve bir gece boyunca kod yazma seansında bir şeyler uygulamaya koyulma hakkını saklı tutar.

## Yeni önerilerin nasıl eklendiği

Bir öneri sunmak için, geliştirme forumunda yayınlayın veya bir ticket açın ve öneriyi ekleyin.

Bir fikir önerildikten sonra, uygun biçimde (aşağıya bakınız) bir taslak varsa ve aktif geliştirme topluluğu içinde rough consensus varsa, bu fikir dikkate alınmaya değer, öneri editörleri resmi olarak öneriyi ekler.

Şu anki öneri editörleri zzz ve str4d'dir.

## Bir öneride neler olmalı

Her öneri, aşağıdaki alanları içeren bir başlık içermelidir:

```
:author:
:created:
:thread:
:lastupdated:
:status:
```

- `author` alanı, bu önerinin yazarlarının adlarını içermelidir.
- `thread` alanı, bu önerinin orijinal olarak yayınlandığı geliştirme forumu thread'ına veya bu öneri için oluşturulan yeni bir thread'a bir bağlantı içermelidir.
- `lastupdated` alanı, başlangıçta `created` alanına eşit olmalıdır ve öneri değiştirildiğinde güncellenmelidir.

Aşağıdaki alanlar gerekli değildir, ancak ayarlanmalıdır:

```
:supercedes:
:supercededby:
:editor:
```

- `supercedes` alanı, bu önerinin yerini aldığı tüm önerilerin virgülle ayrılmış bir listesini içermelidir. Bu öneriler Reddedilmiş olmalıdır ve `supercededby` alanları, bu önerinin numarasına ayarlanmalıdır.
- `editor` alanı, öneriye önemli değişiklikler yapıldığında, ancak içeriği önemli ölçüde değiştirilmediğinde ayarlanmalıdır. İçerik önemli ölçüde değiştiriliyorsa, ya ek bir `author` eklenmeli veya bu öneriyi geçersiz kılan yeni bir öneri yaratılmalıdır.

Aşağıdaki alanlar isteğe bağlıdır, ancak önerilir:

```
:target:
:implementedin:
```

- `target` alanı, önerinin hangi sürümde uygulanmasını umduklarını açıklamalıdır (eğer Açık veya Kabul Edilmişse).
- `implementedin` alanı, önerinin hangi sürümde uygulandığını açıklamalıdır (eğer Tamamlandı veya Kapalıysa).

Önerinin gövdesi, önerinin ne hakkında olduğunu, ne yaptığını ve hangi durumda olduğunu açıklayan bir Genel Bakış bölümü ile başlamalıdır.

Genel Bakış'tan sonra, öneri daha serbest bir forma girer. Uzunluğu ve karmaşıklığına bağlı olarak, öneri uygun bölümlere ayrılabilir veya kısa bir tartışma formatını takip edebilir. Her öneri, Kabul Edilmeden önce aşağıdaki bilgileri içermelidir, ancak bu bilgiler aynı adlı bölümlerde olmak zorunda değildir.

**Motivasyon**
: Öneri hangi problemi çözmeye çalışıyor? Bu problem neden önemlidir? Birden fazla yaklaşım mümkün ise, neden bu yaklaşımı seçtik?

**Tasarım**
: Yeni veya değiştirilen özelliklerin yüksek düzeyde bir görünümü, nasıl çalıştıkları, birbirleriyle nasıl etkileşimde bulundukları ve I2P'nin geri kalanıyla nasıl etkileşimde bulundukları. Bu, önerinin ana gövdesidir. Bazı öneriler, yalnızca bir Motivasyon ve bir Tasarım ile başlayabilir ve spécifikasyon bekleyebilir, Tasarım yaklaşık olarak doğru görünene kadar.

**Güvenlik etkileri**
: Önerilen değişikliklerin anonimlik üzerindeki etkileri, bu etkilerin ne kadar iyi anlaşıldığı ve benzeri konular.

**Spécifikasyon**
: Öneriyi uygulamak için I2P spécifikasyonlarına neler eklenmesi gerektiğini ayrıntılı olarak açıklamalıdır: bağımsız programcılar, önerinin spécifikasyonlarına dayanarak互相 uyumlu uygulamalar yazabilmelidir.

**Uyumluluk**
: I2P'nin öneriyi izleyen sürümleri, öneriyi izlemeyen sürümlerle uyumlu olacak mı? Eğer öyleyse, uyumluluk nasıl sağlanacak? Genel olarak, uyumluluğu düşürmemeye çalışıyoruz; Mart 2008'den bu yana "flag day" değişikliği yapmadık ve başka bir tane yapmak istemiyoruz.

**Uygulama**
: Öneri, I2P'nin mevcut mimarisinde uygulanması zor olacaksa, belge, bunu nasıl çalıştırabileceğinize dair bazı tartışmaları içerebilir. Gerçek yamalar, kamu monotone dallarında veya Trac'e yüklenmelidir.

**Performans ve ölçeklenebilirlik notları**
: Özellik, performansı (RAM, CPU, bant genişliği) veya ölçeklenebilirliği etkileyecekse, bu etkinin ne kadar önemli olacağı konusunda bir analiz olmalıdır, böylece gerçekten pahalı performans gerilemelerinden kaçınabilelim ve önemsiz kazançlar için zaman kaybetmeyelim.

**Referanslar**
: Öneri, dış belgeleri referans alıyorsa, bunlar listelenmelidir.

## Öneri durumu

**Açık**
: Tartışma altında olan bir öneri.

**Kabul Edilmiş**
: Öneri tamamlanmıştır ve uygulamayı planlıyoruz. Bu noktadan sonra, önerideki önemli değişiklikler kaçınılmalıdır ve sürecin bir yerde başarısız olduğu bir işaret olarak görülmalıdır.

**Tamamlandı**
: Öneri kabul edilmiş ve uygulanmıştır. Bu noktadan sonra, öneri değiştirilmemelidir.

**Kapalı**
: Öneri kabul edilmiş, uygulanmış ve ana spécifikasyon belgelerine entegre edilmiştir. Öneri, bu noktadan sonra değiştirilmemelidir.

**Reddedilmiş**
: Önerilen özelliği, burada tanımlı olarak uygulamayacağız, ancak başka bir sürümünü yapabiliriz. Ayrıntılar için belgedeki yorumlara bakınız. Öneri, bu noktadan sonra değiştirilmemelidir; bu fikrin başka bir sürümünü getirmek için yeni bir öneri yazılmalıdır.

**Taslak**
: Bu henüz tamamlanmış bir öneri değildir; kesin olarak eksik parçalar vardır. Lütfen yeni öneriler eklemeyin; onları "ideas" alt dizinine koyun.

**Revizyon Gerektirir**
: Öneri fikri iyi bir fikirdir, ancak öneri olarak durduğu şekliyle ciddi sorunları vardır ve kabul edilmesini engeller. Ayrıntılar için belgedeki yorumlara bakınız.

**Ölü**
: Öneri uzun süredir dokunulmamıştır ve yakın zamanda tamamlanacağı görünmüyor. Yeni bir destekleyici bulursa tekrar "Açık" haline gelebilir.

**Araştırma Gerektirir**
: Önerinin iyi bir fikir olup olmadığından önce çözülmesi gereken araştırma sorunları vardır.

**Meta**
: Bu bir öneri değildir, ancak öneriler hakkında bir belgedir.

**Rezerv**
: Bu öneri, şu anda uygulamayı planladığımız bir şey değildir, ancak gelecekte benzer bir şey yapmak istersek yeniden canlandırabileceğimiz bir şeydir.

**Bilgilendirici**
: Bu öneri, yaptığının son sözüdür. Yeni bir alt sistem için yeni bir spécifikasyon oluşturmak için kopyala-yapıştır yapılmazsa, spécifikasyon haline gelmeyecektir.

Editörler, rough consensus ve kendi inisiyatiflerine dayanarak önerilerin doğru durumunu korur. 

## Öneri numaralandırma

000-099 numaraları, özel ve meta-öneriler için ayrılmıştır. 100 ve üzeri numaralar, gerçek öneriler için kullanılır. Numaralar geri dönüştürülmez.

## Referanslar

* [DEV-FORUM-PROPOSAL](http://zzz.i2p/topics/new?forum_id=7-big-topics-ideas-proposals-and-discussion)
* [TORSPEC-PROCESS](https://gitweb.torproject.org/torspec.git/tree/proposals/001-process.txt)
* [TRAC-PROPOSAL](http://trac.i2p2.i2p/newticket?summary=New%20proposal:%20&type=enhancement&milestone=n/a&component=www/i2p&keywords=review-needed)
