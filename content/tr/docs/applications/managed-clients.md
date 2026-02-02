---
title: "Yönetilen İstemciler"
description: "Router tarafından yönetilen uygulamaların ClientAppManager ve port mapper ile nasıl entegre olduğu"
slug: "managed-clients"
lastUpdated: "2014-02"
accurateFor: "0.9.11"
---

## Genel Bakış

İstemciler, [clients.config](/docs/specs/configuration/) dosyasında listelendiğinde router tarafından doğrudan başlatılabilir. Bu istemciler "yönetilen" veya "yönetilmeyen" olabilir. Bu durum ClientAppManager tarafından ele alınır. Ayrıca, yönetilen veya yönetilmeyen istemciler, diğer istemcilerin onlara referans alabilmesi için ClientAppManager'a kaydolabilir. İstemcilerin diğer istemcilerin arayabileceği dahili bir portu kaydetmeleri için basit bir Port Mapper olanağı da bulunmaktadır.

---

## Yönetilen İstemciler

0.9.4 sürümünden itibaren, router yönetilen istemcileri desteklemektedir. Yönetilen istemciler ClientAppManager tarafından başlatılır ve çalıştırılır. ClientAppManager istemciye bir referans tutar ve istemcinin durumu hakkında güncellemeler alır. Yönetilen istemciler tercih edilir, çünkü durum takibi yapmak ve bir istemciyi başlatıp durdurmak çok daha kolaydır. Ayrıca bir istemci durdurulduktan sonra aşırı bellek kullanımına yol açabilecek statik referansları istemci kodunda önlemek de çok daha kolaydır. Yönetilen istemciler kullanıcı tarafından router konsolunda başlatılıp durdurulabilir ve router kapatıldığında durdurulur.

Yönetilen istemciler net.i2p.app.ClientApp veya net.i2p.router.app.RouterApp arayüzünü uygular. ClientApp arayüzünü uygulayan istemciler aşağıdaki constructor'ı sağlamalıdır:

```java
public MyClientApp(I2PAppContext context, ClientAppManager listener, String[] args)
```
RouterApp arayüzünü uygulayan istemciler aşağıdaki yapıcıyı sağlamalıdır:

```java
public MyClientApp(RouterContext context, ClientAppManager listener, String[] args)
```
Sağlanan argümanlar clients.config dosyasında belirtilmiştir.

---

## Yönetilmeyen İstemciler

clients.config dosyasında belirtilen ana sınıf, yönetilen bir arayüzü (managed interface) uygulamıyorsa, belirtilen argümanlarla main() ile başlatılır ve belirtilen argümanlarla main() ile durdurulur. Router bir referans tutmaz çünkü tüm etkileşimler statik main() metodu aracılığıyla gerçekleşir. Konsol kullanıcıya doğru durum bilgisi sağlayamaz.

---

## Kayıtlı İstemciler

Yönetilen veya yönetilmeyen istemciler, diğer istemcilerin kendilerine referans alabilmesi için ClientAppManager'a kayıt olabilirler. Kayıt işlemi isim ile yapılır. Bilinen kayıtlı istemciler şunlardır:

```
console, i2ptunnel, Jetty, outproxy, update
```
---

## Port Eşleyici

Router ayrıca istemcilerin HTTP proxy gibi dahili soket hizmetlerini bulmalarını sağlayan basit bir mekanizma sunar. Bu, Port Mapper tarafından sağlanır. Kayıt işlemi isme göre yapılır. Kayıt olan istemciler genellikle o port üzerinde dahili emüle edilmiş bir soket sağlar.
