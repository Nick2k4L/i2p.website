---
title: "Спецификация протокола потоковой передачи"
description: "Спецификация протокола потокового вещания I2P, обеспечивающего надежную передачу данных наподобие TCP"
slug: "streaming"
category: "Протоколы"
lastUpdated: "2023-10"
accurateFor: "0.9.59"
---

## Обзор

См. [Streaming Library](/docs/api/streaming) для обзора протокола Streaming.

## Версии протокола

Протокол потоковой передачи не включает поле версии. Версии, перечисленные ниже, предназначены для Java I2P. Реализации и фактическая поддержка криптографии могут различаться. Невозможно определить, поддерживает ли удаленная сторона какую-либо конкретную версию или функцию. Таблица ниже предназначена для общего ориентирования относительно дат выпуска различных функций.

Функции, перечисленные ниже, относятся к самому протоколу. Различные параметры конфигурации документированы в [Streaming Library](/docs/api/streaming) вместе с версией Java I2P, в которой они были реализованы.

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
## Спецификация протокола

### Формат пакета

Формат одного пакета в протоколе потокового вещания показан ниже. Минимальный размер заголовка без NACK или данных опций составляет 22 байта.

В протоколе потоковой передачи нет поля длины. Кадрирование обеспечивается нижними уровнями - I2CP и I2NP.

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
**sendStreamId** :: 4 байта [Integer](/docs/specs/common-structures#integer) : Случайное число, выбранное получателем пакета перед отправкой первого ответного пакета SYN и постоянное на протяжении жизни соединения, больше нуля. 0 в сообщении SYN, отправляемом инициатором соединения, и в последующих сообщениях, до получения ответа SYN, содержащего stream ID узла.

**receiveStreamId** :: 4 байта [Integer](/docs/specs/common-structures#integer) : Случайное число, выбранное отправителем пакета перед отправкой первого SYN пакета и постоянное в течение жизни соединения, больше нуля. Может быть 0, если неизвестно, например в RESET пакете.

**sequenceNum** :: 4 байта [Integer](/docs/specs/common-structures#integer) : Последовательный номер для данного сообщения, начинающийся с 0 в SYN-сообщении и увеличивающийся на 1 в каждом сообщении, за исключением простых ACK и повторных передач. Если sequenceNum равен 0 и флаг SYN не установлен, это простой ACK-пакет, который не должен подтверждаться.

**ackThrough** :: 4 байта [Integer](/docs/specs/common-structures#integer) : Наивысший порядковый номер пакета, который был получен на receiveStreamId. Это поле игнорируется в исходном пакете соединения (где receiveStreamId является неизвестным идентификатором) или если установлен флаг NO_ACK. Все пакеты до этого порядкового номера включительно считаются подтвержденными (ACK), ЗА ИСКЛЮЧЕНИЕМ тех, что перечислены в NACK ниже.

**Количество NACK** :: 1 байт [Integer](/docs/specs/common-structures#integer) : Количество 4-байтных NACK в следующем поле, или 8 при использовании совместно с SYNCHRONIZE для предотвращения повторов начиная с версии 0.9.58; см. ниже.

**NACKs** :: nc * 4 байта [Integer](/docs/specs/common-structures#integer) : Порядковые номера меньше ackThrough, которые ещё не были получены. Два NACK для пакета являются запросом на 'быструю повторную передачу' этого пакета. Также используется вместе с SYNCHRONIZE для предотвращения повторного воспроизведения начиная с версии 0.9.58; см. ниже.

**resendDelay** :: 1 байт [Integer](/docs/specs/common-structures#integer) : Как долго создатель этого пакета будет ждать перед повторной отправкой этого пакета (если он еще не был подтвержден ACK). Значение указано в секундах с момента создания пакета. В настоящее время игнорируется при получении.

**flags** :: 2-байтовое значение : См. ниже.

**размер опции** :: 2 байта [Integer](/docs/specs/common-structures#integer) : Количество байт в следующем поле

**данные опции** :: 0 или более байт : Как указано флагами. См. ниже.

**payload** :: оставшийся размер пакета

### Поля флагов и данных опций

Поле флагов выше указывает некоторые метаданные о пакете и, в свою очередь, может требовать включения определенных дополнительных данных. Флаги следующие. Любые указанные структуры данных должны быть добавлены в область опций в данном порядке.

Порядок битов: 15....0 (15 - старший разряд)

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
### Примечания к подписям переменной длины

До выпуска версии 0.9.11 подпись в поле опций всегда составляла 40 байт.

Начиная с релиза 0.9.11, подпись имеет переменную длину. Тип и длина подписи выводятся из типа ключа, используемого в опции FROM_INCLUDED, и документации по [Signature](/docs/specs/common-structures#signature).

Начиная с релиза 0.9.39, поддерживается опция OFFLINE_SIGNATURE. Если эта опция присутствует, временный [SigningPublicKey](/docs/specs/common-structures#signingpublickey) используется для проверки любых подписанных пакетов, а длина подписи и тип выводятся из временного SigningPublicKey в опции.

- Когда пакет содержит как FROM_INCLUDED, так и SIGNATURE_INCLUDED (как в SYNCHRONIZE), вывод может быть сделан напрямую.

- Когда пакет не содержит FROM_INCLUDED, вывод должен быть сделан из предыдущего пакета SYNCHRONIZE.

- Когда пакет не содержит FROM_INCLUDED, и не было предыдущего пакета SYNCHRONIZE (например, случайный пакет CLOSE или RESET), вывод может быть сделан из длины оставшихся опций (поскольку SIGNATURE_INCLUDED является последней опцией), но пакет, вероятно, будет отброшен в любом случае, поскольку нет доступного FROM для проверки подписи. Если в будущем будут определены дополнительные поля опций, их необходимо будет учесть.

### Предотвращение повторных атак

Чтобы предотвратить использование Бобом атаки повторного воспроизведения путем сохранения действительного подписанного пакета SYNCHRONIZE, полученного от Алисы, и последующей отправки его жертве Чарли, Алиса должна включить хеш назначения Боба в пакет SYNCHRONIZE следующим образом:

```
Set NACK count field to 8
Set the NACKs field to Bob's 32-byte destination hash
```
При получении SYNCHRONIZE, если поле счетчика NACK равно 8, Боб должен интерпретировать поле NACKs как 32-байтовый хеш назначения и должен проверить, что он соответствует его хешу назначения. Он также должен проверить подпись пакета как обычно, поскольку она покрывает весь пакет, включая поля счетчика NACK и NACKs. Если счетчик NACK равен 8, а поле NACKs не совпадает, Боб должен отбросить пакет.

Это требуется для версий 0.9.58 и выше. Это обратно совместимо со старыми версиями, поскольку NACK не ожидаются в пакете SYNCHRONIZE. Destinations не знают и не могут знать, какая версия запущена на другом конце.

Никаких изменений не требуется для пакета SYNCHRONIZE ACK, отправляемого от Bob к Alice; не включайте NACK в этот пакет.

## Справочники

- **[Destination]** [Destination](/docs/specs/common-structures#destination)
- **[Integer]** [Integer](/docs/specs/common-structures#integer)
- **[OfflineSig]** [OfflineSignature](/docs/specs/common-structures#offlinesignature)
- **[Signature]** [Signature](/docs/specs/common-structures#signature)
- **[SigningPrivateKey]** [SigningPrivateKey](/docs/specs/common-structures#signingprivatekey)
- **[SigningPublicKey]** [SigningPublicKey](/docs/specs/common-structures#signingpublickey)
- **[STREAMING]** [Библиотека Streaming](/docs/api/streaming)
