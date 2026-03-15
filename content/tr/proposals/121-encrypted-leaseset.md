---
title: "Şifreli LeaseSet"
number: "121"
author: "zzz"
created: "2016-01-11"
lastupdated: "2016-01-12"
status: "Reddedildi"
thread: "http://zzz.i2p/topics/2047"
supercededby: "123"
toc: true
---
## Genel Bakış

Bu öneri, LeaseSet'leri şifreleme mekanizmasını yeniden tasarlamaktadır.


## Motivasyon

Şu anki şifrelenmiş LS berbat ve güvensiz. Bunu söyleyebilirim, çünkü ben tasarladım ve uyguladım.

Nedenler:

- AES CBC şifreleme
- Herkes için tek bir AES anahtarı
- Kiralama süreleri hala açık
- Şifreleme pubkey hala açık


## Tasarım

### Hedefler

- Tüm şeyi opak hale getirmek
- Her alıcı için anahtarlar


### Strateji

GPG/OpenPGP gibi yapın. Her alıcı için simetrik bir anahtarı asimetrik olarak şifreleyin. Veriler bu asimetrik anahtar ile şifrelenir. Örnek olarak [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1) bölümüne bakın. Eğer küçük ve hızlı bir algoritma bulabilirsek.

Bulmaca, küçük ve hızlı bir asimetrik şifreleme bulmaktır. 514 byte'lık ElGamal burada biraz can sıkıcı. Daha iyisini yapabiliriz.

Örnek olarak http://security.stackexchange.com/questions/824... bölümüne bakın.

Bu, alıcıların (veya aslında anahtarların) küçük sayıları için çalışır; eğer isterseniz, anahtarları birden fazla kişiye dağıtabilirsiniz.


## Özellikler

- Hedef
- Yayınlanan zaman damgası
- Süre sonu
- Bayraklar
- Veri uzunluğu
- Şifrelenmiş veri
- İmza

Şifrelenmiş veri, bazı enctype belirteci ile öneklenmemiş olabilir.


## Referanslar

* [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
