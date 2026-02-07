---
title: "Спецификация датаграмм"
description: "Спецификация форматов датаграмм I2P, включая обычные, с возможностью ответа и аутентифицированные типы"
slug: "datagrams"
category: "Протоколы"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

## Обзор

См. [документацию по API датаграмм](/docs/api/datagrams/) для обзора API датаграмм.

Определены следующие типы. Перечислены стандартные номера протоколов, однако могут использоваться любые другие номера протоколов, кроме номера протокола потоковой передачи (6), специфичного для приложения.

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
Поддержка Datagram2 и Datagram3 в различных реализациях router и библиотек пока не определена. Проверьте документацию для соответствующих реализаций.

### Идентификация типа датаграммы

Четыре типа датаграмм не имеют общего заголовка с версией протокола в одном месте. Пакеты нельзя идентифицировать по типу на основе их содержимого. При использовании нескольких типов в одной сессии или одного типа вместе со streaming, приложения должны использовать номера протоколов и/или порты I2CP/SAM для маршрутизации входящих пакетов в нужное место. Использование стандартных номеров протоколов упростит это. Оставлять номер протокола неустановленным (0 или PROTO_ANY), даже для приложения, использующего только датаграммы, не рекомендуется, поскольку это увеличивает вероятность ошибок маршрутизации и усложняет обновление до многопротокольного приложения. Поля версии в Datagram 2 и 3 предоставляются только как дополнительная проверка ошибок маршрутизации и будущих изменений.

### Проектирование приложений

Все варианты использования датаграмм зависят от конкретного приложения.

Поскольку аутентифицированные датаграммы несут значительные накладные расходы, типичное приложение использует как аутентифицированные, так и неаутентифицированные датаграммы. Типичный подход заключается в отправке одной аутентифицированной датаграммы, содержащей токен, от клиента к серверу. Сервер отвечает неаутентифицированной датаграммой, содержащей тот же токен. Любая последующая коммуникация до истечения времени действия токена использует обычные датаграммы.

Приложения отправляют и получают датаграммы, используя номера протоколов и портов через API [I2CP](/docs/specs/i2cp/) или [SAMv3](/docs/api/samv3/).

Датаграммы, конечно же, ненадёжны. Приложения должны быть спроектированы для ненадёжной доставки. В рамках I2P доставка надёжна между соседними узлами, если следующий узел достижим, поскольку транспорты NTCP2 и SSU2 обеспечивают надёжность. Однако сквозная доставка не является надёжной, поскольку сообщения I2NP могут быть отброшены на любом узле из-за ограничений очередей, истечения срока действия, таймаутов, ограничений пропускной способности или недостижимости следующих узлов.

### Размер датаграммы

Номинальное ограничение размера для I2NP сообщений, включая датаграммы, составляет 64 КБ. Накладные расходы garlic encryption и tunnel сообщений несколько уменьшают это значение.

Однако все I2NP сообщения должны быть фрагментированы на tunnel сообщения размером 1 КБ. Вероятность потери I2NP сообщения размером n КБ является экспоненциальной функцией от вероятности потери одного tunnel сообщения, p ** n. Поскольку фрагментация приводит к всплеску tunnel сообщений, фактическая вероятность потери намного выше, чем предполагает экспоненциальная функция, из-за ограничений очередей и активного управления очередями (AQM, CoDel или аналогичные) в реализациях router.

Рекомендуемый типичный максимальный размер для обеспечения надёжной доставки составляет несколько КБ или максимум 10 КБ. При тщательном анализе размеров накладных расходов на всех уровнях протокола (кроме транспортного), разработчики должны установить максимальный размер полезной нагрузки, который точно поместится в одно, два или три tunnel сообщения. Это максимизирует эффективность и надёжность. Накладные расходы на различных уровнях включают заголовок gzip, заголовок I2NP, заголовок garlic сообщения, garlic encryption, заголовок tunnel сообщения, заголовки фрагментации tunnel сообщений и другие. См. расчёты MTU для streaming в [Proposal 144](/proposals/144-ecies-x25519-aead-ratchet/) и ConnectionOptions.java в исходном коде Java I2P для примеров.

### Соображения по SAM

Приложения отправляют и получают датаграммы, используя номера протоколов и портов через I2CP API или SAM. Указание номеров протоколов и портов через SAM требует SAM v3.2 или выше. Использование как датаграмм, так и потоковой передачи (UDP и TCP) в одной SAM сессии (tunnel) требует SAM v3.3 или выше. Использование нескольких типов датаграмм в одной SAM сессии (tunnel) требует SAM v3.3 или выше. SAM v3.3 в настоящее время поддерживается только Java I2P router.

Поддержка SAM для Datagram2 и Datagram3 в различных реализациях router и библиотек пока не определена. Проверьте документацию для этих реализаций.

Обратите внимание, что размеры свыше типичного сетевого MTU в 1500 байт не позволят SAM-приложениям передавать нефрагментированные пакеты к/от SAM-сервера, если приложение и сервер находятся на разных компьютерах. Обычно это не так, они оба находятся на localhost, где MTU составляет 65536 или выше. Если предполагается, что SAM-приложение будет отделено на другом компьютере от сервера, максимальная полезная нагрузка для датаграммы с возможностью ответа составляет чуть менее 1 КБ.

### Соображения по постквантовой криптографии

Если будет реализована MLDSA часть пост-квантового [Предложения 169](/proposals/169-pq-crypto/), накладные расходы существенно увеличатся. Размер назначения + подпись увеличится с 391 + 64 = 455 байт до минимума 3739 для MLDSA44 и максимума 7226 для MLDSA87. Практические последствия этого предстоит определить. Datagram3 с аутентификацией, предоставляемой router'ом, может стать решением.

## Сырые (без возможности ответа) датаграммы {#raw}

Неотвечаемые датаграммы не имеют адреса отправителя ('from') и не проходят аутентификацию. Они также называются "сырыми" датаграммами. Строго говоря, это вообще не "датаграммы", а просто сырые данные. Они не обрабатываются API датаграмм. Однако SAM и классы I2PTunnel поддерживают "сырые датаграммы".

Стандартный номер протокола I2CP для сырых датаграмм — PROTO_DATAGRAM_RAW (18).

Формат здесь не указан, он определяется приложением. Для полноты мы включаем изображение формата ниже.

### Формат

```
+----+----+----+----+----//
| payload...
+----+----+----+----+----//

length: 0 - about 64 KB (see notes)
```
### Примечания

Практическая длина ограничена как накладными расходами на различных уровнях, так и надежностью.

## Datagram1 (С возможностью ответа) {#repliable}

Датаграммы с возможностью ответа содержат адрес отправителя ('from') и подпись. Это добавляет как минимум 427 байт служебной информации.

Стандартный номер протокола I2CP для датаграмм с возможностью ответа — PROTO_DATAGRAM (17).

### Формат

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
### Примечания

- Практическая длина ограничена как накладными расходами на различных уровнях, так и надежностью.
- См. важные замечания о надежности больших датаграмм в [документации API датаграмм](/docs/api/datagrams/). Для достижения наилучших результатов ограничьте полезную нагрузку примерно 10 КБ или меньше.
- Подписи для типов, отличных от DSA_SHA1, были переопределены в релизе 0.9.14.
- Формат не поддерживает включение блока автономной подписи для LS2 (предложение 123). Для этого должен быть определен новый протокол с флагами.

## Datagram2 {#datagram2}

Формат Datagram2 определен в [Предложении 163](/proposals/163-datagram2/). Номер протокола I2CP для Datagram2 — 19.

Datagram2 предназначен как замена для Datagram1. Он добавляет следующие функции к Datagram1:

- Предотвращение повторных атак
- Поддержка офлайн-подписи
- Поля флагов и опций для расширяемости

Обратите внимание, что алгоритм вычисления подписи для Datagram2 существенно отличается от алгоритма для Datagram1.

### Формат

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
Общая длина: минимум 433 + длина полезной нагрузки; типичная длина для отправителей X25519 и без офлайн-подписей: 457 + длина полезной нагрузки. Обратите внимание, что сообщение обычно будет сжато с помощью gzip на уровне I2CP, что приведет к значительной экономии, если назначение отправителя поддается сжатию.

Примечание: Формат автономной подписи такой же, как в [Спецификации общих структур](/docs/specs/common-structures/) и [Спецификации потоковой передачи](/docs/specs/streaming/).

### Подписи

Подпись вычисляется для следующих полей:

- Prelude: 32-байтовый хэш целевого назначения (не включается в датаграмму)
- flags
- options (если присутствует)
- offline_signature (если присутствует)
- payload

В отвечаемой датаграмме для типа ключа DSA_SHA1 подпись создавалась по SHA-256 хешу полезной нагрузки, а не по самой полезной нагрузке; здесь подпись всегда создается по полям выше (НЕ по хешу), независимо от типа ключа.

### Проверка ToHash

Получатели должны проверить подпись (используя хеш своего назначения) и отбросить датаграмму при неудаче, для предотвращения повторных атак.

## Datagram3 {#datagram3}

Формат Datagram3 определен в [Предложении 163](/proposals/163-datagram2/). Номер протокола I2CP для Datagram3 — 20.

Datagram3 предназначен как улучшенная версия raw datagram. Он добавляет следующие возможности к raw datagram:

- Воспроизводимость
- Поля флагов и опций для расширяемости

Datagram3 НЕ аутентифицирован. В будущем предложении аутентификация может быть обеспечена ratchet-слоем router'а, и статус аутентификации будет передаваться клиенту.

### Формат

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
Общая длина: минимум 34 + длина полезной нагрузки.

## Ссылки

- [Common](/docs/specs/common-structures/) - Спецификация общих структур
- [DATAGRAMS](/docs/api/datagrams/) - Обзор API датаграмм
- [I2CP](/docs/specs/i2cp/) - Спецификация I2CP
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet/) - Предложение ECIES-X25519-AEAD-Ratchet
- [Prop163](/proposals/163-datagram2/) - Предложение Datagram2 и Datagram3
- [Prop169](/proposals/169-pq-crypto/) - Предложение по постквантовой криптографии
- [SAMv3](/docs/api/samv3/) - Спецификация SAM v3
- [Streaming](/docs/specs/streaming/) - Спецификация потоковой передачи
- [TRANSPORT](/docs/overview/transport/) - Обзор транспорта
- [TUNMSG](/docs/specs/tunnel-message/#notes) - Спецификация сообщений tunnel
