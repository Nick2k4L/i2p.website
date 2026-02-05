---
title: "Akış Protokolü Spesifikasyonu"
description: "TCP benzeri güvenilir aktarım sağlayan I2P streaming protokolü spesifikasyonu"
slug: "streaming"
category: "Protokoller"
lastUpdated: "2023-10"
accurateFor: "0.9.59"
---

## Genel Bakış

Streaming protokolüne genel bakış için [Streaming Library](/docs/api/streaming) bölümüne bakın.

## Protokol Sürümleri

Streaming protokolü bir sürüm alanı içermez. Aşağıda listelenen sürümler Java I2P içindir. Implementasyonlar ve gerçek kripto desteği değişiklik gösterebilir. Uzak ucun belirli bir sürümü veya özelliği destekleyip desteklemediğini belirlemenin bir yolu yoktur. Aşağıdaki tablo, çeşitli özelliklerin yayın tarihleri hakkında genel rehberlik sağlamak içindir.

Aşağıda listelenen özellikler protokolün kendisi içindir. Çeşitli yapılandırma seçenekleri, uygulandıkları Java I2P sürümü ile birlikte [Streaming Library](/docs/api/streaming) içinde belgelenmiştir.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Router Version</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Streaming Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Bob's hash in NACKs field of SYN packet</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE option</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">I2CP protocol number enforced</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED no longer required in RESET</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PINGs and PONGs may include a payload</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA Ed25519 sig type</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA P-256, P-384, and P-521 sig types</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Variable-length signatures</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.7.1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Protocol numbers defined in I2CP</td>
    </tr>
  </tbody>
</table>
## Protokol Spesifikasyonu

### Paket Formatı

Streaming protokolünde tek bir paketin formatı aşağıda gösterilmiştir. NACK'ler veya seçenek verileri olmadan minimum başlık boyutu 22 bayttır.

Streaming protokolünde uzunluk alanı bulunmamaktadır. Çerçeveleme alt katmanlar tarafından sağlanır - I2CP ve I2NP.

```
+----+----+----+----+----+----+----+----+
| send Stream ID    | rcv Stream ID     |
+----+----+----+----+----+----+----+----+
| sequence  Num     | ack Through       |
+----+----+----+----+----+----+----+----+
| nc |  nc*4 bytes of NACKs (optional)
+----+----+----+----+----+----+----+----+
     | rd |  flags  | opt size| opt data
+----+----+----+----+----+----+----+----+
   ...  (optional, see below)           |
+----+----+----+----+----+----+----+----+
|   payload ...
+----+----+----+-//
```
**sendStreamId** :: 4 byte [Integer](/docs/specs/common-structures#integer) : İlk SYN yanıt paketini göndermeden önce paket alıcısı tarafından seçilen rastgele sayı ve bağlantının ömrü boyunca sabit, sıfırdan büyük. Bağlantı başlatıcısı tarafından gönderilen SYN mesajında 0, ve sonraki mesajlarda karşı tarafın stream ID'sini içeren bir SYN yanıtı alınana kadar 0.

**receiveStreamId** :: 4 bayt [Integer](/docs/specs/common-structures#integer) : Paket göndereni tarafından ilk SYN paketi gönderilmeden önce seçilen ve bağlantının ömrü boyunca sabit olan, sıfırdan büyük rastgele sayı. Bilinmiyorsa, örneğin bir RESET paketinde olduğu gibi, 0 olabilir.

**sequenceNum** :: 4 bayt [Integer](/docs/specs/common-structures#integer) : Bu mesaj için sıra numarası, SYN mesajında 0'dan başlar ve düz ACK'ler ve yeniden gönderimler dışında her mesajda 1 artırılır. sequenceNum 0 ise ve SYN bayrağı ayarlanmamışsa, bu ACK'lenmemesi gereken düz bir ACK paketidir.

**ackThrough** :: 4 byte [Integer](/docs/specs/common-structures#integer) : receiveStreamId üzerinde alınan en yüksek paket sıra numarası. Bu alan, ilk bağlantı paketinde (receiveStreamId bilinmeyen id olduğunda) veya NO_ACK bayrağı ayarlanmışsa göz ardı edilir. Bu sıra numarasına kadar ve bu numara dahil olmak üzere tüm paketler ACK edilir, aşağıdaki NACK'lerde listelenenler HARİÇ.

**NACK sayısı** :: 1 byte [Integer](/docs/specs/common-structures#integer) : Sonraki alandaki 4-byte NACK'ların sayısı, veya 0.9.58 sürümü itibariyle tekrar oynatma önlenmesi için SYNCHRONIZE ile birlikte kullanıldığında 8; aşağıya bakın.

**NACKs** :: nc * 4 byte [Integer](/docs/specs/common-structures#integer) : ackThrough'dan küçük ancak henüz alınmamış sıra numaraları. Bir paketin iki NACK'ı, o paketin 'hızlı yeniden iletimi' için bir istektir. Ayrıca 0.9.58 sürümünden itibaren replay önleme için SYNCHRONIZE ile birlikte kullanılır; aşağıya bakın.

**resendDelay** :: 1 byte [Integer](/docs/specs/common-structures#integer) : Bu paketin yaratıcısı, paketi yeniden göndermeden önce ne kadar bekleyecek (eğer henüz ACK edilmediyse). Değer, paketin oluşturulmasından bu yana geçen saniyedir. Şu anda alımda göz ardı ediliyor.

**flags** :: 2 bayt değeri : Aşağıya bakın.

**option size** :: 2 bayt [Integer](/docs/specs/common-structures#integer) : Sonraki alandaki bayt sayısı

**seçenek verisi** :: 0 veya daha fazla bayt : Bayraklar tarafından belirtildiği gibi. Aşağıya bakın.

**payload** :: kalan paket boyutu

### Bayraklar ve Seçenek Veri Alanları

Yukarıdaki flags alanı, paket hakkında bazı metadata belirtir ve bu da belirli ek verilerin dahil edilmesini gerektirebilir. Flags'lar aşağıdaki gibidir. Belirtilen herhangi bir veri yapısı, options alanına verilen sırada eklenmelidir.

Bit sırası: 15....0 (15 MSB'dir)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Flag</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Order</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SYNCHRONIZE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP SYN. Set in the initial packet and in the first response. FROM_INCLUDED and SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">CLOSE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP FIN. If the response to a SYNCHRONIZE fits in a single message, the response will contain both SYNCHRONIZE and CLOSE. SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RESET</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Abnormal close. SIGNATURE_INCLUDED must also be set. Prior to release 0.9.20, due to a bug, FROM_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#signature">Signature</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, CLOSE, and RESET, where it is required, and with ECHO, where it is required for a ping. The signature uses the Destination's <a href="/docs/specs/common-structures#signingprivatekey">SigningPrivateKey</a> to sign the entire header and payload with the space in the option data field for the signature being set to all zeroes. Prior to release 0.9.11, the signature was always 40 bytes. As of release 0.9.11, the signature may be variable-length, see below for details.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused. Requests every packet in the other direction to have SIGNATURE_INCLUDED</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">387+ byte <a href="/docs/specs/common-structures#destination">Destination</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, where it is required, and with ECHO, where it is required for a ping. Prior to release 0.9.20, due to a bug, must also be sent with RESET.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DELAY_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Optional delay. How many milliseconds the sender of this packet wants the recipient to wait before sending any more data. A value greater than 60000 indicates choking. A value of 0 requests an immediate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MAX_PACKET_SIZE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum length of the payload. Send with SYNCHRONIZE.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PROFILE_INTERACTIVE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused or ignored; the interactive profile is unimplemented.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECHO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused except by ping programs. If set, most other options are ignored. See the <a href="/docs/api/streaming">streaming docs</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">NO_ACK</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">This flag simply tells the recipient to ignore the ackThrough field in the header. Currently set in the initial SYN packet, otherwise the ackThrough field is always valid. Note that this does not save any space, the ackThrough field is before the flags and is always present.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#offlinesignature">OfflineSig</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Contains the offline signature section from LS2. See proposal 123 and the common structures specification. FROM_INCLUDED must also be set. Contains an OfflineSig: 1) Expires timestamp (4 bytes, seconds since epoch, rolls over in 2106) 2) Transient sig type (2 bytes) 3) Transient <a href="/docs/specs/common-structures#signingpublickey">SigningPublicKey</a> (length as implied by sig type) 4) <a href="/docs/specs/common-structures#signature">Signature</a> of expires timestamp, transient sig type, and public key, by the destination public key. Length of sig as implied by the destination public key sig type.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12-15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">unused</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Set to zero for compatibility with future uses.</td>
    </tr>
  </tbody>
</table>
### Değişken Uzunluklu İmza Notları

0.9.11 sürümünden önce, seçenek alanındaki imza her zaman 40 bayt idi.

0.9.11 sürümünden itibaren, imza değişken uzunluktadır. İmza türü ve uzunluğu, FROM_INCLUDED seçeneğinde kullanılan anahtar türünden ve [İmza](/docs/specs/common-structures#signature) belgelerinden çıkarılır.

0.9.39 sürümü itibariyle, OFFLINE_SIGNATURE seçeneği desteklenmektedir. Bu seçenek mevcut ise, geçici [SigningPublicKey](/docs/specs/common-structures#signingpublickey) imzalanmış paketleri doğrulamak için kullanılır ve imza uzunluğu ile türü seçenekteki geçici SigningPublicKey'den çıkarılır.

- Bir paket hem FROM_INCLUDED hem de SIGNATURE_INCLUDED içerdiğinde (SYNCHRONIZE'da olduğu gibi), çıkarım doğrudan yapılabilir.

- Bir paket FROM_INCLUDED içermediğinde, çıkarım önceki bir SYNCHRONIZE paketinden yapılmalıdır.

- Bir paket FROM_INCLUDED içermediğinde ve önceki bir SYNCHRONIZE paketi bulunmadığında (örneğin başıboş bir CLOSE veya RESET paketi), çıkarım kalan seçeneklerin uzunluğundan yapılabilir (SIGNATURE_INCLUDED son seçenek olduğundan), ancak imzayı doğrulamak için kullanılabilir FROM bulunmadığından paket muhtemelen yine de atılacaktır. Gelecekte daha fazla seçenek alanı tanımlanırsa, bunlar da hesaba katılmalıdır.

### Tekrar Oynatma Önleme

Bob'un Alice'den aldığı geçerli bir imzalı SYNCHRONIZE paketini saklayarak daha sonra kurban Charlie'ye göndererek replay saldırısı yapmasını önlemek için, Alice'in SYNCHRONIZE paketine Bob'un destination hash'ini aşağıdaki gibi dahil etmesi gerekir:

```
Set NACK count field to 8
Set the NACKs field to Bob's 32-byte destination hash
```
Bir SYNCHRONIZE alındığında, NACK count alanı 8 ise, Bob NACK'ler alanını 32-byte'lık bir hedef hash'i olarak yorumlamalı ve bunun kendi hedef hash'i ile eşleştiğini doğrulamalıdır. Ayrıca, NACK count ve NACK'ler alanları dahil olmak üzere tüm paketi kapsadığı için, paketin imzasını her zamanki gibi doğrulamalıdır. Eğer NACK count 8 ise ve NACK'ler alanı eşleşmiyorsa, Bob paketi düşürmelidir.

Bu, 0.9.58 ve üzeri sürümler için gereklidir. Bu, eski sürümlerle geriye dönük uyumludur çünkü SYNCHRONIZE paketinde NACK'ler beklenmez. Destination'lar karşı tarafın hangi sürümü çalıştırdığını bilmez ve bilemez.

Bob'dan Alice'e gönderilen SYNCHRONIZE ACK paketi için herhangi bir değişiklik gerekli değildir; bu pakete NACK'ları dahil etmeyin.

## Kaynaklar

- **[Destination]** [Destination](/docs/specs/common-structures#destination)
- **[Integer]** [Integer](/docs/specs/common-structures#integer)
- **[OfflineSig]** [OfflineSignature](/docs/specs/common-structures#offlinesignature)
- **[Signature]** [Signature](/docs/specs/common-structures#signature)
- **[SigningPrivateKey]** [SigningPrivateKey](/docs/specs/common-structures#signingprivatekey)
- **[SigningPublicKey]** [SigningPublicKey](/docs/specs/common-structures#signingpublickey)
- **[STREAMING]** [Streaming Kütüphanesi](/docs/api/streaming)
