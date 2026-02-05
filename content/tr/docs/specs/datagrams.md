---
title: "Datagram Spesifikasyonu"
description: "Ham, yanıtlanabilir ve kimlik doğrulamalı türler dahil olmak üzere I2P datagram mesaj formatlarının spesifikasyonu"
slug: "datagrams"
category: "Protokoller"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

## Genel Bakış

Datagrams API'sine genel bir bakış için [Datagrams API belgelerini](/docs/api/datagrams/) inceleyin.

Aşağıdaki türler tanımlanmıştır. Standart protokol numaraları listelenmiştir, ancak streaming protokol numarası (6) dışında, uygulamaya özel herhangi bir protokol numarası kullanılabilir.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Protocol</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Repliable?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Authenticated?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Replay Prevention?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">As Of</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Raw</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
  </tbody>
</table>
Çeşitli router ve kütüphane uygulamalarında Datagram2 ve Datagram3 desteği henüz belirlenmemiştir. Bu uygulamaların belgelerini kontrol edin.

### Datagram Tür Tanımlama

Dört datagram türü, protokol sürümünün aynı yerde bulunduğu ortak bir başlığı paylaşmaz. Paketler içeriklerine göre türe göre tanımlanamaz. Aynı oturumda birden fazla tür kullanırken veya streaming ile birlikte tek bir tür kullanırken, uygulamalar gelen paketleri doğru yere yönlendirmek için protokol numaralarını ve/veya I2CP/SAM portlarını kullanmalıdır. Standart protokol numaralarını kullanmak bunu kolaylaştıracaktır. Sadece datagram kullanan bir uygulama için bile protokol numarasını ayarlanmamış bırakmak (0 veya PROTO_ANY) önerilmez çünkü yönlendirme hatalarının olasılığını artırır ve çok protokollü bir uygulamaya yükseltmeleri zorlaştırır. Datagram 2 ve 3'teki sürüm alanları yalnızca yönlendirme hataları ve gelecekteki değişiklikler için ek bir kontrol olarak sağlanır.

### Uygulama Tasarımı

Datagramların tüm kullanımları uygulamaya özgüdır.

Kimlik doğrulamalı datagramlar önemli ek yük getirdiği için, tipik bir uygulama hem kimlik doğrulamalı hem de kimlik doğrulamasız datagramları kullanır. Tipik bir tasarım, istemciden sunucuya bir token içeren tek bir kimlik doğrulamalı datagram göndermektir. Sunucu aynı token'ı içeren kimlik doğrulamasız bir datagram ile yanıt verir. Token zaman aşımından önce gerçekleşen sonraki tüm iletişim, ham datagramları kullanır.

Uygulamalar, [I2CP](/docs/specs/i2cp/) API'si veya [SAMv3](/docs/api/samv3/) aracılığıyla protokol ve port numaralarını kullanarak datagram gönderip alır.

Datagramlar tabii ki güvenilir değildir. Uygulamalar güvenilmez teslimat için tasarlanmalıdır. I2P içinde, bir sonraki hop erişilebilir durumdaysa hop-to-hop teslimat güvenilirdir, çünkü NTCP2 ve SSU2 aktarım protokolleri güvenilirlik sağlar. Ancak, I2NP mesajları kuyruk limitleri, süre aşımları, zaman aşımları, bant genişliği limitleri veya erişilemeyen next-hop'lar nedeniyle herhangi bir hop içinde düşürülebileceğinden, uçtan uca teslimat güvenilir değildir.

### Datagram Boyutu

Datagramlar dahil olmak üzere I2NP mesajları için nominal boyut sınırı 64 KB'dir. Garlic encryption ve tunnel mesaj ek yükü bunu bir miktar azaltır.

Ancak, tüm I2NP mesajları 1 KB tunnel mesajlarına parçalanmalıdır. n KB'lık bir I2NP mesajının düşme olasılığı, tek bir tunnel mesajının düşme olasılığının üstel fonksiyonudur, p ** n. Parçalama tunnel mesajlarının patlamasına neden olduğundan, router uygulamalarındaki kuyruk sınırları ve aktif kuyruk yönetimi (AQM, CoDel veya benzeri) nedeniyle gerçek düşme olasılığı üstel fonksiyonun ima ettiğinden çok daha yüksektir.

Güvenilir teslimatı sağlamak için önerilen tipik maksimum boyut birkaç KB veya en fazla 10 KB'dir. Tüm protokol katmanlarındaki (taşıma hariç) ek yük boyutlarının dikkatli analizi ile geliştiriciler, tam olarak bir, iki veya üç tunnel mesajına sığacak bir maksimum yük boyutu belirlemelidir. Bu, verimliliği ve güvenilirliği maksimize edecektir. Çeşitli katmanlardaki ek yükler gzip başlığı, I2NP başlığı, garlic mesaj başlığı, garlic encryption, tunnel mesaj başlığı, tunnel mesaj parçalama başlıkları ve diğerlerini içerir. Örnekler için [Proposal 144](/proposals/144-ecies-x25519-aead-ratchet/)'teki streaming MTU hesaplamaları ve Java I2P kaynak kodundaki ConnectionOptions.java dosyasına bakın.

### SAM Değerlendirmeleri

Uygulamalar I2CP API veya SAM üzerinden protokol ve port numaraları kullanarak datagram gönderir ve alır. SAM üzerinden protokol ve port numaraları belirtmek SAM v3.2 veya daha yüksek sürüm gerektirir. Aynı SAM oturumunda (tunnel'lar) hem datagram hem de streaming (UDP ve TCP) kullanmak SAM v3.3 veya daha yüksek sürüm gerektirir. Aynı SAM oturumunda (tunnel'lar) birden fazla datagram türü kullanmak SAM v3.3 veya daha yüksek sürüm gerektirir. SAM v3.3 şu anda yalnızca Java I2P router tarafından desteklenmektedir.

Çeşitli router ve kütüphane uygulamalarında Datagram2 ve Datagram3 için SAM desteği henüz belirlenmemiştir. Bu uygulamaların belgelerini kontrol edin.

Tipik 1500 bayt ağ MTU'sundan büyük boyutların, uygulama ve sunucu ayrı bilgisayarlarda bulunuyorsa, SAM uygulamalarının SAM sunucusuna/sunucusundan fragmente edilmemiş paketler taşımasını engelleyeceğini unutmayın. Genellikle durum bu değildir, her ikisi de localhost'ta bulunur ve burada MTU 65536 veya daha yüksektir. Bir SAM uygulamasının sunucudan farklı bir bilgisayarda ayrılması bekleniyorsa, yanıtlanabilir bir datagram için maksimum yük 1 KB'nin biraz altındadır.

### PQ Değerlendirmeleri

Post-Quantum [Proposal 169](/proposals/169-pq-crypto/) önerisinin MLDSA kısmı uygulanırsa, ek yük önemli ölçüde artacaktır. Bir destination + imza boyutu 391 + 64 = 455 bayttan MLDSA44 için minimum 3739'a ve MLDSA87 için maksimum 7226'ya çıkacaktır. Bunun pratik etkileri henüz belirlenmemiştir. Router tarafından sağlanan kimlik doğrulama ile Datagram3, bir çözüm olabilir.

## Ham (Yanıtlanamaz) Datagramlar {#raw}

Yanıtlanamaz datagramlar 'from' adresine sahip değildir ve doğrulanmazlar. Bunlara "raw" datagramlar da denir. Kesin olarak konuşmak gerekirse, bunlar hiç "datagram" değildir, sadece ham veridir. Datagram API'si tarafından işlenmezler. Ancak, SAM ve I2PTunnel sınıfları "raw datagramları" destekler.

Ham datagramlar için standart I2CP protokol numarası PROTO_DATAGRAM_RAW (18)'dir.

Format burada belirtilmemiştir, uygulama tarafından tanımlanmaktadır. Eksiksizlik için aşağıda formatın bir resmini dahil ediyoruz.

### Format

```
+----+----+----+----+----//
| payload...
+----+----+----+----+----//

length: 0 - about 64 KB (see notes)
```
### Notlar

Pratik uzunluk, çeşitli katmanlardaki ek yük ve güvenilirlik ile sınırlıdır.

## Datagram1 (Yanıtlanabilir) {#repliable}

Yanıtlanabilir datagramlar bir 'kimden' adresi ve imza içerir. Bunlar en az 427 bayt ek yük ekler.

Yanıtlanabilir datagramlar için standart I2CP protokol numarası PROTO_DATAGRAM (17)'dir.

### Format

```
+----+----+----+----+----+----+----+----+
| from                                  |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+                                       +
|                                       |
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
| payload...
+----+----+----+----//

from :: a Destination
        length: 387+ bytes
        The originator and signer of the datagram

signature :: a Signature
             Signature type must match the signing public key type of $from
             length: 40+ bytes, as implied by the Signature type.
             For the default DSA_SHA1 key type:
                The DSA Signature of the SHA-256 hash of the payload.
             For other key types:
                The Signature of the payload.
             The signature may be verified by the signing public key of $from

payload :: The data
           Length: 0 to about 63 KB (see notes)

Total length: Payload length + 427+
```
### Notlar

- Pratik uzunluk, çeşitli katmanlardaki ek yük ve güvenilirlik ile sınırlıdır.
- Büyük datagramların güvenilirliği hakkında önemli notlar için [Datagrams API belgeleri](/docs/api/datagrams/) bölümüne bakın. En iyi sonuçlar için payload'u yaklaşık 10 KB veya daha az ile sınırlayın.
- DSA_SHA1 dışındaki türler için imzalar 0.9.14 sürümünde yeniden tanımlandı.
- Format, LS2 için çevrimdışı imza bloğu dahil edilmesini desteklemiyor (öneri 123). Bunun için flag'ler içeren yeni bir protokol tanımlanmalıdır.

## Datagram2 {#datagram2}

Datagram2 formatı [Proposal 163](/proposals/163-datagram2/) belgesinde belirtildiği gibidir. Datagram2 için I2CP protokol numarası 19'dur.

Datagram2, Datagram1'in yerini alması için tasarlanmıştır. Datagram1'e aşağıdaki özellikleri ekler:

- Tekrar saldırısı önleme
- Çevrimdışı imza desteği
- Genişletilebilirlik için bayrak ve seçenek alanları

Datagram2 için imza hesaplama algoritmasının Datagram1'den önemli ölçüde farklı olduğunu unutmayın.

### Format

```
+----+----+----+----+----+----+----+----+
|                                       |
~            from                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~     offline_signature (optional)      ~
~   expires, sigtype, pubkey, offsig    ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            signature                  ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

from :: a Destination
        length: 387+ bytes
        The originator and (unless offline signed) signer of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x02 (0 0 1 0)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bit 5: If 0, no offline sig; if 1, offline signed
         Bits 15-6: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

offline_signature ::
             If flag indicates offline keys, the offline signature section,
             as specified in the Common Structures Specification,
             with the following 4 fields. Length: varies by online and offline
             sig types, typically 102 bytes for Ed25519
             This section can, and should, be generated offline.

  expires :: Expires timestamp
             (4 bytes, big endian, seconds since epoch, rolls over in 2106)

  sigtype :: Transient sig type (2 bytes, big endian)

  pubkey :: Transient signing public key (length as implied by sig type),
            typically 32 bytes for Ed25519 sig type.

  offsig :: a Signature
            Signature of expires timestamp, transient sig type,
            and public key, by the destination public key,
            length: 40+ bytes, as implied by the Signature type, typically
            64 bytes for Ed25519 sig type.

payload :: The data
           Length: 0 to about 61 KB (see notes)

signature :: a Signature
             Signature type must match the signing public key type of $from
             (if no offline signature) or the transient sigtype
             (if offline signed)
             length: 40+ bytes, as implied by the Signature type, typically
             64 bytes for Ed25519 sig type.
             The Signature of the payload and other fields as specified below.
             The signature is verified by the signing public key of $from
             (if no offline signature) or the transient pubkey
             (if offline signed)
```
Toplam uzunluk: minimum 433 + payload uzunluğu; X25519 gönderenler ve çevrimdışı imzalar olmadan tipik uzunluk: 457 + payload uzunluğu. Mesajın genellikle I2CP katmanında gzip ile sıkıştırılacağını ve kaynak hedef sıkıştırılabilirse önemli tasarruf sağlayacağını unutmayın.

Not: Çevrimdışı imza formatı [Ortak Yapılar Belirtimi](/docs/specs/common-structures/) ve [Streaming Belirtimi](/docs/specs/streaming/)'ndeki ile aynıdır.

### İmzalar

İmza aşağıdaki alanları kapsar:

- Prelude: Hedef destinasyonun 32-byte hash değeri (datagram'a dahil değildir)
- flags
- options (varsa)
- offline_signature (varsa)
- payload

Yanıtlanabilir datagram'da, DSA_SHA1 anahtar türü için imza payload'ın kendisi üzerinde değil, payload'ın SHA-256 hash'i üzerindeydi; burada ise imza anahtar türüne bakılmaksızın her zaman yukarıdaki alanlar üzerindedir (hash üzerinde DEĞİL).

### ToHash Doğrulaması

Alıcılar, tekrar saldırılarını önlemek için imzayı (hedef hash'lerini kullanarak) doğrulamalı ve başarısızlık durumunda datagramı atmalıdır.

## Datagram3 {#datagram3}

Datagram3 formatı [Önerge 163](/proposals/163-datagram2/) içinde belirtildiği gibidir. Datagram3 için I2CP protokol numarası 20'dir.

Datagram3, ham datagramların gelişmiş bir sürümü olarak tasarlanmıştır. Ham datagramlara aşağıdaki özellikleri ekler:

- Tekrarlanabilirlik
- Genişletilebilirlik için bayraklar ve seçenekler alanları

Datagram3 kimlik doğrulaması yapılmaz. Gelecekteki bir öneride, kimlik doğrulama router'ın ratchet katmanı tarafından sağlanabilir ve kimlik doğrulama durumu istemciye aktarılabilir.

### Format

```
+----+----+----+----+----+----+----+----+
|                                       |
~            fromhash                   ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

fromhash :: a Hash
            length: 32 bytes
            The originator of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x03 (0 0 1 1)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bits 15-5: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

payload :: The data
           Length: 0 to about 61 KB (see notes)
```
Toplam uzunluk: minimum 34 + yük uzunluğu.

## Referanslar

- [Common](/docs/specs/common-structures/) - Ortak Yapılar Spesifikasyonu
- [DATAGRAMS](/docs/api/datagrams/) - Datagrams API Genel Bakış
- [I2CP](/docs/specs/i2cp/) - I2CP Spesifikasyonu
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet/) - ECIES-X25519-AEAD-Ratchet Önerisi
- [Prop163](/proposals/163-datagram2/) - Datagram2 ve Datagram3 Önerisi
- [Prop169](/proposals/169-pq-crypto/) - Kuantum Sonrası Kriptografi Önerisi
- [SAMv3](/docs/api/samv3/) - SAM v3 Spesifikasyonu
- [Streaming](/docs/specs/streaming/) - Streaming Spesifikasyonu
- [TRANSPORT](/docs/overview/transport/) - Transport Genel Bakış
- [TUNMSG](/docs/specs/tunnel-message/#notes) - tunnel Message Spesifikasyonu
