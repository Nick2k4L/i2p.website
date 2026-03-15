---
title: "Tanıtıcı Süresi Dolma"
number: "133"
author: "zzz"
created: "2017-02-05"
lastupdated: "2017-08-09"
status: "Kapalı"
thread: "http://zzz.i2p/topics/2230"
target: "0.9.30"
implementedin: "0.9.30"
toc: true
---
## Genel Bakış

Bu öneri, tanıtım başarı oranını artırmaya yöneliktir.


## Gerekçe

Tanıtıcılar belli bir süre sonra süresi dolmakla birlikte, bu bilgi Router Bilgisinde (Router Info) yayınlanmaz. Yönlendiricilerin şu anda geçerli olmayan bir tanıtıcıyı tahmin etmek için sezgisel yöntemler kullanması gerekir.


## Tasarım

SSU Yönlendirici Adresi tanıtıcılar içerdiğinde, yayımcı her bir tanıtıcı için isteğe bağlı olarak süre sonu zamanlarını ekleyebilir.


## Özellikler

```
iexp{X}={nnnnnnnnnn}

X :: Tanıtıcı numarası (0-2)

nnnnnnnnnn :: Epoch'tan bu yana geçen saniye cinsinden zaman (ms değil).
```

### Notlar

* Her bir süre sonu, Yönlendirici Bilgisinin yayın tarihinden daha büyük olmalı ve aynı zamanda yayın tarihinden 6 saat daha az olmalıdır.

* Yayınlama yapan yönlendiriciler ve tanıtıcılar, tanıtıcının süre sonuna kadar geçerli kalmasını sağlamaya çalışmalıdır; ancak bunu garanti etmenin bir yolu yoktur.

* Yönlendiriciler, bir tanıtıcının süresi dolduktan sonra onu kullanmamalıdır.

* Tanıtıcı süre sonları, Yönlendirici Adresi eşlemesinde yer alır.
  Şu anda kullanılmayan, Yönlendirici Adresindeki 8 baytlık süre sonu alanıyla karıştırılmamalıdır.

**Örnek:** `iexp0=1486309470`


## Geçiş

Herhangi bir sorun yok. Uygulama isteğe bağlıdır.
Eski yönlendiriciler bilinmeyen parametreleri yok sayacağından, geriye dönük uyumluluk garanti altındadır.


## Kaynaklar

* [RouterAddress](/docs/specs/common-structures/#routeraddress)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TRAC-TICKET](http://trac.i2p2.i2p/ticket/1352)
