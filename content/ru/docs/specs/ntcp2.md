---
title: "NTCP2 транспорт"
description: "TCP-транспорт на основе Noise для соединений между router-ами"
slug: "ntcp2"
category: "Транспорты"
lastUpdated: "2026-01"
accurateFor: "0.9.66"
---

## Обзор

NTCP2 — это протокол аутентифицированного согласования ключей, который повышает устойчивость [NTCP](/docs/transport/ntcp) к различным формам автоматической идентификации и атакам.

NTCP2 разработан для гибкости и сосуществования с NTCP. Он может поддерживаться на том же порту, что и NTCP, или на другом порту, или вообще без одновременной поддержки NTCP. Подробности смотрите в разделе "Опубликованная информация router" ниже.

Как и другие транспорты I2P, NTCP2 предназначен исключительно для точка-точка (router-к-router) транспортировки сообщений I2NP. Это не универсальный канал передачи данных.

NTCP2 поддерживается начиная с версии 0.9.36. См. [Prop111](/proposals/111-ntcp-2) для ознакомления с оригинальным предложением, включая обсуждение предпосылок и дополнительную информацию.

## Фреймворк протокола Noise

NTCP2 использует Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (Редакция 33, 2017-10-04). Noise имеет схожие свойства с протоколом Station-To-Station [STS](#references), который является основой для протокола [SSU](/docs/transport/ssu). В терминологии Noise, Алиса является инициатором, а Боб — отвечающей стороной.

NTCP2 основан на протоколе Noise Noise_XK_25519_ChaChaPoly_SHA256. (Фактический идентификатор для начальной функции деривации ключей — "Noise_XKaesobfse+hs2+hs3_25519_ChaChaPoly_SHA256" для указания расширений I2P — см. раздел KDF 1 ниже) Этот протокол Noise использует следующие примитивы:

- Шаблон рукопожатия: XK Алиса передает свой ключ Бобу (X) Алиса уже знает статический ключ Боба (K)
- Функция DH: X25519 X25519 DH с длиной ключа 32 байта, как указано в [RFC-7748](https://tools.ietf.org/html/rfc7748).
- Функция шифрования: ChaChaPoly AEAD_CHACHA20_POLY1305, как указано в [RFC-7539](https://tools.ietf.org/html/rfc7539) раздел 2.8. 12-байтовый nonce, первые 4 байта установлены в ноль.
- Хэш-функция: SHA256 Стандартный 32-байтовый хэш, уже широко используемый в I2P.

## Дополнения к фреймворку

NTCP2 определяет следующие улучшения к Noise_XK_25519_ChaChaPoly_SHA256. Они в целом следуют рекомендациям в разделе 13 [NOISE](https://noiseprotocol.org/noise.html).

1) Открытые эфемерные ключи обфусцируются с помощью AES-шифрования, используя известный ключ и IV. 2) К сообщениям 1 и 2 добавляется случайное открытое заполнение. Открытое заполнение включается в вычисление хеша рукопожатия (MixHash). См. разделы KDF ниже для сообщения 2 и части 1 сообщения 3. Случайное AEAD-заполнение добавляется к сообщению 3 и сообщениям фазы данных. 3) Добавляется двухбайтовое поле длины фрейма, что требуется для Noise поверх TCP и как в obfs4. Это используется только в сообщениях фазы данных. AEAD-фреймы сообщений 1 и 2 имеют фиксированную длину. AEAD-фрейм части 1 сообщения 3 имеет фиксированную длину. Длина AEAD-фрейма части 2 сообщения 3 указывается в сообщении 1. 4) Двухбайтовое поле длины фрейма обфусцируется с помощью SipHash-2-4, как в obfs4. 5) Формат полезной нагрузки определен для сообщений 1, 2, 3 и фазы данных. Конечно, они не определены в фреймворке.

## Сообщения

Все NTCP2 сообщения имеют длину не более 65537 байт. Формат сообщений основан на Noise сообщениях, с модификациями для кадрирования и неразличимости. Реализации, использующие стандартные Noise библиотеки, могут потребовать предварительной обработки получаемых сообщений в/из формата Noise сообщений. Все зашифрованные поля являются AEAD шифротекстами.

Последовательность установления соединения выглядит следующим образом:

```
Alice                           Bob

SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Используя терминологию Noise, последовательность установления и передачи данных выглядит следующим образом: (Свойства безопасности полезной нагрузки из [Noise](https://noiseprotocol.org/noise.html))

```
XK(s, rs):           Authentication   Confidentiality
  <- s
  ...
  -> e, es                  0                2
  <- e, ee                  2                1
  -> s, se                  2                5
  <-                        2                5
```
После установки сессии Алиса и Боб могут обмениваться сообщениями Data.

Все типы сообщений (SessionRequest, SessionCreated, SessionConfirmed, Data и TimeSync) указаны в этом разделе.

Некоторые обозначения:

    - RH_A = Router Hash for Alice (32 bytes)
    - RH_B = Router Hash for Bob (32 bytes)

### Аутентифицированное шифрование

Существует три отдельных экземпляра аутентифицированного шифрования (CipherStates). Один во время фазы handshake, и два (передача и получение) для фазы данных. Каждый имеет свой собственный ключ из KDF.

Зашифрованные/аутентифицированные данные будут представлены как

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   Encrypted and authenticated data    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
```
#### ChaCha20/Poly1305

Зашифрованный и аутентифицированный формат данных.

Входные данные для функций шифрования/дешифрования:

```
k :: 32 byte cipher key, as generated from KDF

nonce :: Counter-based nonce, 12 bytes.
         Starts at 0 and incremented for each message.
         First four bytes are always zero.
         Last eight bytes are the counter, little-endian encoded.
         Maximum value is 2**64 - 2.
         Connection must be dropped and restarted after
         it reaches that value.
         The value 2**64 - 1 must never be sent.

ad :: In handshake phase:
      Associated data, 32 bytes.
      The SHA256 hash of all preceding data.
      In data phase:
      Zero bytes

data :: Plaintext data, 0 or more bytes
```
Вывод функции шифрования, ввод функции расшифровки:

```
+----+----+----+----+----+----+----+----+
|Obfs Len |                             |
+----+----+                             +
|       ChaCha20 encrypted data         |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|  Poly1305 Message Authentication Code |
+              (MAC)                    +
|             16 bytes                  |
+----+----+----+----+----+----+----+----+

Obfs Len :: Length of (encrypted data + MAC) to follow, 16 - 65535
            Obfuscation using SipHash (see below)
            Not used in message 1 or 2, or message 3 part 1, where the length is fixed
            Not used in message 3 part 1, as the length is specified in message 1

encrypted data :: Same size as plaintext data, 0 - 65519 bytes

MAC :: Poly1305 message authentication code, 16 bytes
```
Для ChaCha20 то, что описано здесь, соответствует [RFC-7539](https://tools.ietf.org/html/rfc7539), который также аналогично используется в TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).

#### Примечания

- Поскольку ChaCha20 является потоковым шифром, открытые тексты не нуждаются в дополнении. Дополнительные байты keystream отбрасываются.
- Ключ для шифра (256 бит) согласовывается с помощью SHA256 KDF. Детали KDF для каждого сообщения приведены в отдельных разделах ниже.
- Кадры ChaChaPoly для сообщений 1, 2 и первой части сообщения 3 имеют известный размер. Начиная со второй части сообщения 3, кадры имеют переменный размер. Размер части 1 сообщения 3 указывается в сообщении 1. Начиная с фазы данных, кадры предваряются двухбайтовой длиной, обфусцированной с помощью SipHash, как в obfs4.
- Дополнение находится вне аутентифицированного кадра данных для сообщений 1 и 2. Дополнение используется в KDF для следующего сообщения, поэтому подделка будет обнаружена. Начиная с сообщения 3, дополнение находится внутри аутентифицированного кадра данных.

#### Обработка ошибок AEAD

- В сообщениях 1, 2 и частях 1 и 2 сообщения 3 размер AEAD сообщения известен заранее. При сбое аутентификации AEAD получатель должен остановить дальнейшую обработку сообщений и закрыть соединение без ответа. Это должно быть аварийное закрытие (TCP RST).
- Для защиты от зондирования в сообщении 1, после сбоя AEAD, Bob должен установить случайный таймаут (диапазон TBD) и затем прочитать случайное количество байт (диапазон TBD) перед закрытием сокета. Bob должен вести черный список IP-адресов с повторяющимися сбоями.
- В фазе данных размер AEAD сообщения "зашифрован" (обфусцирован) с помощью SipHash. Необходимо проявлять осторожность, чтобы избежать создания оракула расшифровки. При сбое аутентификации AEAD в фазе данных получатель должен установить случайный таймаут (диапазон TBD) и затем прочитать случайное количество байт (диапазон TBD). После чтения или при истечении времени чтения получатель должен отправить полезную нагрузку с блоком завершения, содержащим код причины "сбой AEAD", и закрыть соединение.
- Выполнить то же действие при ошибке для недопустимого значения поля длины в фазе данных.

### Функция вывода ключа (KDF) (для сообщения рукопожатия 1)

KDF генерирует ключ шифра для фазы handshake k из результата DH, используя HMAC-SHA256(key, data) как определено в [RFC-2104](https://tools.ietf.org/html/rfc2104). Это функции InitializeSymmetric(), MixHash() и MixKey(), точно как определено в спецификации Noise.

```
This is the "e" message pattern:

// Define protocol_name.
Set protocol_name = "Noise_XKaesobfse+hs2+hs3_25519_ChaChaPoly_SHA256"
 (48 bytes, US-ASCII encoded, no NULL termination).

// Define Hash h = 32 bytes
h = SHA256(protocol_name);

Define ck = 32 byte chaining key. Copy the h data to ck.
Set ck = h

Define rs = Bob's 32-byte static key as published in the RouterInfo

// MixHash(null prologue)
h = SHA256(h);

// up until here, can all be precalculated by Alice for all outgoing connections

// Alice must validate that Bob's static key is a valid point on the curve here.

// Bob static key
// MixHash(rs)
// || below means append
h = SHA256(h || rs);

// up until here, can all be precalculated by Bob for all incoming connections

This is the "e" message pattern:

Alice generates her ephemeral DH key pair e.

// Alice ephemeral key X
// MixHash(e.pubkey)
// || below means append
h = SHA256(h || e.pubkey);

// h is used as the associated data for the AEAD in message 1
// Retain the Hash h for the message 2 KDF


End of "e" message pattern.

This is the "es" message pattern:

// DH(e, rs) == DH(s, re)
Define input_key_material = 32 byte DH result of Alice's ephemeral key and Bob's static key
Set input_key_material = X25519 DH result

// MixKey(DH())

Define temp_key = 32 bytes
Define HMAC-SHA256(key, data) as in [RFC-2104]_
// Generate a temp key from the chaining key and DH result
// ck is the chaining key, defined above
temp_key = HMAC-SHA256(ck, input_key_material)
// overwrite the DH result in memory, no longer needed
input_key_material = (all zeros)

// Output 1
// Set a new chaining key from the temp key
// byte() below means a single byte
ck =       HMAC-SHA256(temp_key, byte(0x01)).

// Output 2
// Generate the cipher key k
Define k = 32 bytes
// || below means append
// byte() below means a single byte
k =        HMAC-SHA256(temp_key, ck || byte(0x02)).
// overwrite the temp_key in memory, no longer needed
temp_key = (all zeros)

// retain the chaining key ck for message 2 KDF


End of "es" message pattern.
```
### 1) SessionRequest

Алиса отправляет Бобу.

Noise содержимое: эфемерный ключ Alice X Noise полезная нагрузка: 16-байтовый блок опций Не-noise полезная нагрузка: случайное заполнение

(Свойства безопасности полезной нагрузки из [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs):           Authentication   Confidentiality
  -> e, es                  0                2

  Authentication: None (0).
  This payload may have been sent by any party, including an active attacker.

  Confidentiality: 2.
  Encryption to a known recipient, forward secrecy for sender compromise
  only, vulnerable to replay.  This payload is encrypted based only on DHs
  involving the recipient's static key pair.  If the recipient's static
  private key is compromised, even at a later date, this payload can be
  decrypted.  This message can also be replayed, since there's no ephemeral
  contribution from the recipient.

  "e": Alice generates a new ephemeral key pair and stores it in the e
       variable, writes the ephemeral public key as cleartext into the
       message buffer, and hashes the public key along with the old h to
       derive a new h.

  "es": A DH is performed between the Alice's ephemeral key pair and the
        Bob's static key pair.  The result is hashed along with the old ck to
        derive a new ck and k, and n is set to zero.
```
Значение X шифруется для обеспечения неразличимости и уникальности полезной нагрузки, что необходимо для противодействия DPI. Мы используем шифрование AES для достижения этой цели, а не более сложные и медленные альтернативы, такие как elligator2. Асимметричное шифрование с использованием публичного ключа router'а Боба было бы слишком медленным. Шифрование AES использует хэш router'а Боба в качестве ключа и IV Боба, опубликованный в netDb.

Шифрование AES предназначено только для сопротивления DPI. Любая сторона, знающая хеш router'а Боба и IV, которые опубликованы в базе данных сети, может расшифровать значение X в этом сообщении.

Заполнение не шифруется Алисой. Бобу может потребоваться расшифровать заполнение, чтобы предотвратить атаки по времени.

Необработанное содержимое:

```
+----+----+----+----+----+----+----+----+
|                                       |
+        obfuscated with RH_B           +
|       AES-CBC-256 encrypted X         |
+             (32 bytes)                +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaChaPoly frame                    |
+             (32 bytes)                +
|   k defined in KDF for message 1      |
+   n = 0                               +
|   see KDF for associated data         |
+----+----+----+----+----+----+----+----+
|     unencrypted authenticated         |
~         padding (optional)            ~
|     length defined in options block   |
+----+----+----+----+----+----+----+----+

X :: 32 bytes, AES-256-CBC encrypted X25519 ephemeral key, little endian
        key: RH_B
        iv: As published in Bobs network database entry

padding :: Random data, 0 or more bytes.
           Total message length must be 65535 bytes or less.
           Total message length must be 287 bytes or less if
           Bob is publishing his address as NTCP
           (see Version Detection section below).
           Alice and Bob will use the padding data in the KDF for message 2.
           It is authenticated so that any tampering will cause the
           next message to fail.
```
Нешифрованные данные (тег аутентификации Poly1305 не показан):

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                   X                   |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|               options                 |
+              (16 bytes)               +
|                                       |
+----+----+----+----+----+----+----+----+
|     unencrypted authenticated         |
+         padding (optional)            +
|     length defined in options block   |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

X :: 32 bytes, X25519 ephemeral key, little endian

options :: options block, 16 bytes, see below

padding :: Random data, 0 or more bytes.
           Total message length must be 65535 bytes or less.
           Total message length must be 287 bytes or less if
           Bob is publishing his address as "NTCP"
           (see Version Detection section below)
           Alice and Bob will use the padding data in the KDF for message 2.
           It is authenticated so that any tampering will cause the
           next message to fail.
```
Блок опций: Примечание: Все поля имеют порядок байтов big-endian.

```
+----+----+----+----+----+----+----+----+
| id | ver|  padLen | m3p2len | Rsvd(0) |
+----+----+----+----+----+----+----+----+
|        tsA        |   Reserved (0)    |
+----+----+----+----+----+----+----+----+

id :: 1 byte, the network ID (currently 2, except for test networks)
      As of 0.9.42. See proposal 147.

ver :: 1 byte, protocol version (currently 2)

padLen :: 2 bytes, length of the padding, 0 or more
          Min/max guidelines TBD. Random size from 0 to 31 bytes minimum?
          (Distribution is implementation-dependent)

m3p2Len :: 2 bytes, length of the the second AEAD frame in SessionConfirmed
           (message 3 part 2) See notes below

Rsvd :: 2 bytes, set to 0 for compatibility with future options

tsA :: 4 bytes, Unix timestamp, unsigned seconds.
       Wraps around in 2106

Reserved :: 4 bytes, set to 0 for compatibility with future options
```
#### Заметки

- Когда опубликованный адрес имеет тип "NTCP", Bob поддерживает как NTCP, так и NTCP2 на одном и том же порту. Для совместимости при инициации соединения к адресу, опубликованному как "NTCP", Alice должна ограничить максимальный размер этого сообщения, включая padding, до 287 байт или меньше. Это облегчает автоматическую идентификацию протокола со стороны Bob. Когда адрес опубликован как "NTCP2", ограничений по размеру нет. См. разделы "Опубликованные адреса" и "Определение версии" ниже.

- Уникальное значение X в начальном блоке AES гарантирует, что шифротекст будет различным для каждой сессии.

- Bob должен отклонять соединения, где значение временной метки слишком сильно отличается от текущего времени. Назовем максимальную разность времени "D". Bob должен поддерживать локальный кэш ранее использованных значений handshake и отклонять дубликаты, чтобы предотвратить replay-атаки. Значения в кэше должны иметь время жизни не менее 2*D. Значения кэша зависят от реализации, однако может использоваться 32-байтовое значение X (или его зашифрованный эквивалент).

- Эфемерные ключи Diffie-Hellman никогда не должны использоваться повторно во избежание криптографических атак, и повторное использование будет отклонено как атака повторного воспроизведения.

- Опции "KE" и "auth" должны быть совместимы, то есть общий секретный ключ K должен иметь соответствующий размер. Если будут добавлены дополнительные опции "auth", это может неявно изменить значение флага "KE" для использования другой функции выведения ключей (KDF) или другого размера усечения.

- Боб должен проверить, что эфемерный ключ Алисы является действительной точкой на кривой здесь.

- Padding должен быть ограничен разумным количеством. Bob может отклонить соединения с избыточным padding. Bob укажет свои опции padding в сообщении 2. Минимальные/максимальные рекомендации еще предстоит определить. Случайный размер от 0 до 31 байта минимум? (Распределение зависит от реализации) Java реализации в настоящее время ограничивают padding максимум 256 байтами.

- При любой ошибке, включая AEAD, DH, метку времени, очевидный повтор или ошибку валидации ключа, Боб должен прекратить дальнейшую обработку сообщений и закрыть соединение без ответа. Это должно быть аварийное закрытие (TCP RST). Для сопротивления зондированию, после ошибки AEAD, Боб должен установить случайный таймаут (диапазон определяется) и затем прочитать случайное количество байт (диапазон определяется), прежде чем закрыть сокет.

- Боб может выполнить быструю проверку MSB для валидного ключа (X[31] & 0x80 == 0) перед попыткой расшифровки. Если старший бит установлен, реализовать сопротивление зондированию как для отказов AEAD.

- Защита от DoS: DH является относительно ресурсоемкой операцией. Как и в предыдущем протоколе NTCP, роутеры должны принимать все необходимые меры для предотвращения исчерпания CPU или соединений. Устанавливайте ограничения на максимальное количество активных соединений и максимальное количество настроек соединений в процессе. Применяйте таймауты чтения (как для каждого чтения, так и общий для "slowloris"). Ограничивайте повторные или одновременные соединения из одного источника. Ведите черные списки источников, которые постоянно терпят неудачу. Не отвечайте на сбой AEAD.

- Для облегчения быстрого определения версии и установления соединения, реализации должны обеспечить, чтобы Alice буферизовала, а затем отправляла всё содержимое первого сообщения целиком, включая заполнение. Это повышает вероятность того, что данные будут содержаться в одном TCP-пакете (если не сегментированы ОС или промежуточными устройствами) и получены Bobом полностью. Дополнительно, реализации должны обеспечить, чтобы Bob буферизовал, а затем отправлял всё содержимое второго сообщения целиком, включая заполнение, и чтобы Bob буферизовал, а затем отправлял всё содержимое третьего сообщения целиком. Это также для эффективности и обеспечения действенности случайного заполнения.

- Поле "ver": Общий протокол Noise, расширения и протокол NTCP, включая спецификации полезной нагрузки, указывающие на NTCP2. Это поле может использоваться для обозначения поддержки будущих изменений.

- Длина части 2 сообщения 3: Это размер второго AEAD-фрейма (включая 16-байтовый MAC), содержащего Router Info Алисы и дополнительное заполнение, которые будут отправлены в сообщении SessionConfirmed. Поскольку роутеры периодически перегенерируют и переопубликовывают свою Router Info, размер текущей Router Info может измениться до отправки сообщения 3. Реализации должны выбрать одну из двух стратегий:

a\) сохранить текущую Router Info для отправки в сообщении 3, чтобы размер был известен, и при необходимости добавить место для заполнения;

б) увеличить указанный размер достаточно, чтобы учесть возможное увеличение размера Router Info, и всегда добавлять заполнение при фактической отправке сообщения 3. В любом случае, длина "m3p2len", включенная в сообщение 1, должна точно соответствовать размеру этого фрейма при отправке в сообщении 3.

- Боб должен прервать соединение, если после валидации сообщения 1 и чтения заполнения остаются какие-либо входящие данные. Не должно быть никаких дополнительных данных от Алисы, поскольку Боб еще не ответил сообщением 2.

- Поле network ID используется для быстрой идентификации межсетевых подключений. Если это поле не равно нулю и не совпадает с network ID Боба, Боб должен отключиться и заблокировать будущие подключения. Любые подключения из тестовых сетей должны иметь другой ID и не пройдут проверку. Начиная с версии 0.9.42. См. предложение 147 для получения дополнительной информации.

### Функция вывода ключей (KDF) (для сообщения 2 и части 1 сообщения 3 handshake)

```
// take h saved from message 1 KDF
// MixHash(ciphertext)
h = SHA256(h || 32 byte encrypted payload from message 1)

// MixHash(padding)
// Only if padding length is nonzero
h = SHA256(h || random padding from message 1)

This is the "e" message pattern:

Bob generates his ephemeral DH key pair e.

// h is from KDF for handshake message 1
// Bob ephemeral key Y
// MixHash(e.pubkey)
// || below means append
h = SHA256(h || e.pubkey);

// h is used as the associated data for the AEAD in message 2
// Retain the Hash h for the message 3 KDF

End of "e" message pattern.

This is the "ee" message pattern:

// DH(e, re)
Define input_key_material = 32 byte DH result of Alice's ephemeral key and Bob's ephemeral key
Set input_key_material = X25519 DH result
// overwrite Alice's ephemeral key in memory, no longer needed
// Alice:
e(public and private) = (all zeros)
// Bob:
re = (all zeros)

// MixKey(DH())

Define temp_key = 32 bytes
Define HMAC-SHA256(key, data) as in [RFC-2104]_
// Generate a temp key from the chaining key and DH result
// ck is the chaining key, from the KDF for handshake message 1
temp_key = HMAC-SHA256(ck, input_key_material)
// overwrite the DH result in memory, no longer needed
input_key_material = (all zeros)

// Output 1
// Set a new chaining key from the temp key
// byte() below means a single byte
ck =       HMAC-SHA256(temp_key, byte(0x01)).

// Output 2
// Generate the cipher key k
Define k = 32 bytes
// || below means append
// byte() below means a single byte
k =        HMAC-SHA256(temp_key, ck || byte(0x02)).
// overwrite the temp_key in memory, no longer needed
temp_key = (all zeros)

// retain the chaining key ck for message 3 KDF

End of "ee" message pattern.
```
### 2) SessionCreated

Боб отправляет Алисе.

Содержимое Noise: эфемерный ключ Боба Y Полезная нагрузка Noise: блок опций 16 байт Не-noise полезная нагрузка: случайное заполнение

(Свойства безопасности полезной нагрузки из [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs):           Authentication   Confidentiality
  <- e, ee                  2                1

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 1.
  Encryption to an ephemeral recipient.
  This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee").
  However, the sender has not authenticated the recipient,
  so this payload might be sent to any party, including an active attacker.


  "e": Bob generates a new ephemeral key pair and stores it in the e variable,
  writes the ephemeral public key as cleartext into the message buffer,
  and hashes the public key along with the old h to derive a new h.

  "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair.
  The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Значение Y шифруется для обеспечения неразличимости и уникальности полезной нагрузки, что является необходимыми мерами противодействия DPI. Мы используем шифрование AES для достижения этой цели, а не более сложные и медленные альтернативы, такие как elligator2. Асимметричное шифрование с использованием публичного ключа router'а Alice было бы слишком медленным. Шифрование AES использует хеш router'а Bob в качестве ключа и состояние AES из сообщения 1 (которое было инициализировано с помощью IV Bob'а, как опубликовано в базе данных сети).

AES-шифрование предназначено только для противодействия DPI. Любая сторона, знающая хеш router'а Боба и IV, которые опубликованы в базе данных сети, и перехватившая первые 32 байта сообщения 1, может расшифровать значение Y в этом сообщении.

Исходное содержимое:

```
+----+----+----+----+----+----+----+----+
|                                       |
+        obfuscated with RH_B           +
|       AES-CBC-256 encrypted Y         |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|   ChaChaPoly frame                    |
+   Encrypted and authenticated data    +
|   32 bytes                            |
+   k defined in KDF for message 2      +
|   n = 0; see KDF for associated data  |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     unencrypted authenticated         |
+         padding (optional)            +
|     length defined in options block   |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

Y :: 32 bytes, AES-256-CBC encrypted X25519 ephemeral key, little endian
        key: RH_B
        iv: Using AES state from message 1
```
Незашифрованные данные (тег аутентификации Poly1305 не показан):

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                  Y                    |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|               options                 |
+              (16 bytes)               +
|                                       |
+----+----+----+----+----+----+----+----+
|     unencrypted authenticated         |
+         padding (optional)            +
|     length defined in options block   |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

Y :: 32 bytes, X25519 ephemeral key, little endian

options :: options block, 16 bytes, see below

padding :: Random data, 0 or more bytes.
           Total message length must be 65535 bytes or less.
           Alice and Bob will use the padding data in the KDF for message 3 part 1.
           It is authenticated so that any tampering will cause the
           next message to fail.
```
#### Примечания

- Alice должна проверить, что эфемерный ключ Bob является действительной точкой на кривой.
- Заполнение должно быть ограничено разумным объемом. Alice может отклонить соединения с чрезмерным заполнением. Alice укажет свои параметры заполнения в сообщении 3. Рекомендации по минимуму/максимуму будут определены позже. Случайный размер от 0 до 31 байта минимум? (Распределение зависит от реализации)
- При любой ошибке, включая AEAD, DH, временную метку, видимый повтор или сбой проверки ключа, Alice должна прекратить дальнейшую обработку сообщений и закрыть соединение без ответа. Это должно быть аварийное закрытие (TCP RST).
- Для облегчения быстрого установления соединения, реализации должны обеспечивать, чтобы Bob буферизовал, а затем отправлял всё содержимое первого сообщения сразу, включая заполнение. Это увеличивает вероятность того, что данные будут содержаться в одном TCP-пакете (если не сегментированы ОС или промежуточными устройствами) и получены Alice за один раз. Это также для эффективности и обеспечения эффективности случайного заполнения.
- Alice должна завершить соединение с ошибкой, если какие-либо входящие данные остаются после проверки сообщения 2 и чтения заполнения. Не должно быть никаких дополнительных данных от Bob, поскольку Alice еще не ответила сообщением 3.

Блок опций: Примечание: Все поля имеют порядок байтов big-endian.

```
+----+----+----+----+----+----+----+----+
| Rsvd(0) | padLen  |   Reserved (0)    |
+----+----+----+----+----+----+----+----+
|        tsB        |   Reserved (0)    |
+----+----+----+----+----+----+----+----+

Reserved :: 10 bytes total, set to 0 for compatibility with future options

padLen :: 2 bytes, big endian, length of the padding, 0 or more
          Min/max guidelines TBD. Random size from 0 to 31 bytes minimum?
          (Distribution is implementation-dependent)

tsB :: 4 bytes, big endian, Unix timestamp, unsigned seconds.
       Wraps around in 2106
```
#### Примечания

- Алиса должна отклонять соединения, где значение временной метки слишком сильно отличается от текущего времени. Назовем максимальную дельту времени "D". Алиса должна поддерживать локальный кэш ранее использованных значений рукопожатия и отклонять дубликаты, чтобы предотвратить атаки повторного воспроизведения. Значения в кэше должны иметь время жизни не менее 2*D. Значения кэша зависят от реализации, однако может использоваться 32-байтное значение Y (или его зашифрованный эквивалент).

#### Проблемы

- Включить здесь опции минимального/максимального заполнения?

### Шифрование для части 1 сообщения 3 handshake, используя KDF сообщения 2)

```
// take h saved from message 2 KDF
// MixHash(ciphertext)
h = SHA256(h || 24 byte encrypted payload from message 2)

// MixHash(padding)
// Only if padding length is nonzero
h = SHA256(h || random padding from message 2)
// h is used as the associated data for the AEAD in message 3 part 1, below

This is the "s" message pattern:

Define s = Alice's static public key, 32 bytes

// EncryptAndHash(s.publickey)
// EncryptWithAd(h, s.publickey)
// AEAD_ChaCha20_Poly1305(key, nonce, associatedData, data)
// k is from handshake message 1
// n is 1
ciphertext = AEAD_ChaCha20_Poly1305(k, n++, h, s.publickey)
// MixHash(ciphertext)
// || below means append
h = SHA256(h || ciphertext);

// h is used as the associated data for the AEAD in message 3 part 2

End of "s" message pattern.
```
### Функция выведения ключа (KDF) (для сообщения квитирования 3, часть 2)

```
This is the "se" message pattern:

// DH(s, re) == DH(e, rs)
Define input_key_material = 32 byte DH result of Alice's static key and Bob's ephemeral key
Set input_key_material = X25519 DH result
// overwrite Bob's ephemeral key in memory, no longer needed
// Alice:
re = (all zeros)
// Bob:
e(public and private) = (all zeros)

// MixKey(DH())

Define temp_key = 32 bytes
Define HMAC-SHA256(key, data) as in [RFC-2104]_
// Generate a temp key from the chaining key and DH result
// ck is the chaining key, from the KDF for handshake message 1
temp_key = HMAC-SHA256(ck, input_key_material)
// overwrite the DH result in memory, no longer needed
input_key_material = (all zeros)

// Output 1
// Set a new chaining key from the temp key
// byte() below means a single byte
ck =       HMAC-SHA256(temp_key, byte(0x01)).

// Output 2
// Generate the cipher key k
Define k = 32 bytes
// || below means append
// byte() below means a single byte
k =        HMAC-SHA256(temp_key, ck || byte(0x02)).

// h from message 3 part 1 is used as the associated data for the AEAD in message 3 part 2

// EncryptAndHash(payload)
// EncryptWithAd(h, payload)
// AEAD_ChaCha20_Poly1305(key, nonce, associatedData, data)
// n is 0
ciphertext = AEAD_ChaCha20_Poly1305(k, n++, h, payload)
// MixHash(ciphertext)
// || below means append
h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF
// retain the hash h for the data phase Additional Symmetric Key (SipHash) KDF

End of "se" message pattern.

// overwrite the temp_key in memory, no longer needed
temp_key = (all zeros)
```
### 3) SessionConfirmed

Алиса отправляет Бобу.

Содержимое Noise: статический ключ Alice Полезная нагрузка Noise: RouterInfo Alice и случайное заполнение Полезная нагрузка не-noise: отсутствует

(Свойства безопасности полезной нагрузки из [Noise](https://noiseprotocol.org/noise.html) )

```
XK(s, rs):           Authentication   Confidentiality
  -> s, se                  2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).  The
  sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key
  pair.  Assuming the corresponding private keys are secure, this
  authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.  This payload is
  encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static
  DH with the recipient's static key pair.  Assuming the ephemeral private
  keys are secure, and the recipient is not being actively impersonated by an
  attacker that has stolen its static private key, this payload cannot be
  decrypted.

  "s": Alice writes her static public key from the s variable into the
  message buffer, encrypting it, and hashes the output along with the old h
  to derive a new h.

  "se": A DH is performed between the Alice's static key pair and the Bob's
  ephemeral key pair.  The result is hashed along with the old ck to derive a
  new ck and k, and n is set to zero.
```
Это содержит два фрейма ChaChaPoly. Первый - зашифрованный статический публичный ключ Алисы. Второй - полезная нагрузка Noise: зашифрованная RouterInfo Алисы, дополнительные опции и дополнительное заполнение. Они используют разные ключи, поскольку функция MixKey() вызывается между ними.

Исходное содержимое:

```
+----+----+----+----+----+----+----+----+
|                                       |
+   ChaChaPoly frame (48 bytes)         +
|   Encrypted and authenticated         |
+   Alice static key S                  +
|      (32 bytes)                       |
+                                       +
|     k defined in KDF for message 2    |
+     n = 1                             +
|     see KDF for associated data       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+     Length specified in message 1     +
|                                       |
+   ChaChaPoly frame                    +
|   Encrypted and authenticated         |
+                                       +
|       Alice RouterInfo                |
+       using block format 2            +
|       Alice Options (optional)        |
+       using block format 1            +
|       Arbitrary padding               |
+       using block format 254          +
|                                       |
+                                       +
| k defined in KDF for message 3 part 2 |
+     n = 0                             +
|     see KDF for associated data       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, ChaChaPoly encrypted Alice's X25519 static key, little endian
     inside 48 byte ChaChaPoly frame
```
Незашифрованные данные (теги аутентификации Poly1305 не показаны):

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|              S                        |
+       Alice static key                +
|          (32 bytes)                   |
+                                       +
|                                       |
+                                       +
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                                       |
+                                       +
|       Alice RouterInfo block          |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+       Optional Options block          +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+       Optional Padding block          +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, Alice's X25519 static key, little endian
```
#### Примечания

- Боб должен выполнить обычную проверку Router Info. Убедиться, что тип подписи поддерживается, проверить подпись, проверить, что временная метка находится в допустимых пределах, и выполнить любые другие необходимые проверки.

- Боб должен проверить, что статический ключ Алисы, полученный в первом кадре, соответствует статическому ключу в Router Info. Боб должен сначала найти в Router Info адрес NTCP или NTCP2 router с соответствующей опцией версии (v). См. разделы Опубликованная Router Info и Неопубликованная Router Info ниже.

- Если у Bob есть более старая версия RouterInfo Alice в его netdb, проверить, что статический ключ в router info одинаковый в обеих версиях, если присутствует, и если более старая версия не старше XXX (см. время ротации ключа ниже)

- Боб должен проверить, что статический ключ Алисы является действительной точкой на кривой здесь.

- Должны быть включены параметры для указания параметров заполнения.

- При любой ошибке, включая сбой AEAD, RI, DH, временной метки или проверки ключей, Bob должен прекратить дальнейшую обработку сообщений и закрыть соединение без ответа. Это должно быть аварийное закрытие (TCP RST).

- Для обеспечения быстрого handshaking реализации должны гарантировать, что Alice буферизует и затем отправляет все содержимое третьего сообщения за раз, включая оба AEAD-фрейма. Это увеличивает вероятность того, что данные будут содержаться в одном TCP-пакете (если не сегментированы ОС или промежуточными устройствами) и получены Bob'ом одновременно. Это также делается для эффективности и обеспечения действенности случайного заполнения.

- Длина фрейма части 2 сообщения 3: Длина этого фрейма (включая MAC) отправляется Алисой в сообщении 1. См. это сообщение для важных замечаний о предоставлении достаточного места для заполнения.

- Содержимое фрейма части 2 сообщения 3: Формат этого фрейма такой же, как формат фреймов фазы данных, за исключением того, что длина фрейма отправляется Алисой в сообщении 1. См. ниже формат фрейма фазы данных. Фрейм должен содержать от 1 до 3 блоков в следующем порядке:

1)  Блок информации о Router Alice (обязательный)   2)  Блок опций (необязательный)

3\) Блок заполнения (необязательный) Этот фрейм никогда не должен содержать блоки других типов.

- Заполнение части 2 сообщения 3 не требуется, если Алиса добавляет фрейм фазы данных (опционально содержащий заполнение) в конец сообщения 3 и отправляет оба одновременно, поскольку для наблюдателя это будет выглядеть как один большой поток байтов. Поскольку у Алисы обычно, но не всегда, есть I2NP сообщение для отправки Бобу (именно поэтому она подключилась к нему), это рекомендуемая реализация для эффективности и обеспечения результативности случайного заполнения.

- Общая длина обеих AEAD-фреймов Сообщения 3 (части 1 и 2) составляет 65535 байт; часть 1 составляет 48 байт, поэтому максимальная длина фрейма части 2 составляет 65487; максимальная длина открытого текста части 2, исключая MAC, составляет 65471.

### Функция вывода ключей (KDF) (для фазы данных)

Фаза данных использует ввод связанных данных нулевой длины.

KDF генерирует два ключа шифрования k_ab и k_ba из chaining key ck, используя HMAC-SHA256(key, data) как определено в [RFC-2104](https://tools.ietf.org/html/rfc2104). Это функция Split(), точно как определено в спецификации Noise.

```
ck = from handshake phase

// k_ab, k_ba = HKDF(ck, zerolen)
// ask_master = HKDF(ck, zerolen, info="ask")

// zerolen is a zero-length byte array
temp_key = HMAC-SHA256(ck, zerolen)
// overwrite the chaining key in memory, no longer needed
ck = (all zeros)

// Output 1
// cipher key, for Alice transmits to Bob (Noise doesn't make clear which is which, but Java code does)
k_ab =   HMAC-SHA256(temp_key, byte(0x01)).

// Output 2
// cipher key, for Bob transmits to Alice (Noise doesn't make clear which is which, but Java code does)
k_ba =   HMAC-SHA256(temp_key, k_ab || byte(0x02)).


KDF for SipHash for length field:
Generate an Additional Symmetric Key (ask) for SipHash
SipHash uses two 8-byte keys (big endian) and 8 byte IV for first data.

// "ask" is 3 bytes, US-ASCII, no null termination
ask_master = HMAC-SHA256(temp_key, "ask" || byte(0x01))
// sip_master = HKDF(ask_master, h || "siphash")
// "siphash" is 7 bytes, US-ASCII, no null termination
// overwrite previous temp_key in memory
// h is from KDF for message 3 part 2
temp_key = HMAC-SHA256(ask_master, h || "siphash")
// overwrite ask_master in memory, no longer needed
ask_master = (all zeros)
sip_master = HMAC-SHA256(temp_key, byte(0x01))

Alice to Bob SipHash k1, k2, IV:
// sipkeys_ab, sipkeys_ba = HKDF(sip_master, zerolen)
// overwrite previous temp_key in memory
temp_key = HMAC-SHA256(sip_master, zerolen)
// overwrite sip_master in memory, no longer needed
sip_master = (all zeros)

sipkeys_ab = HMAC-SHA256(temp_key, byte(0x01)).
sipk1_ab = sipkeys_ab[0:7], little endian
sipk2_ab = sipkeys_ab[8:15], little endian
sipiv_ab = sipkeys_ab[16:23]

Bob to Alice SipHash k1, k2, IV:

sipkeys_ba = HMAC-SHA256(temp_key, sipkeys_ab || byte(0x02)).
sipk1_ba = sipkeys_ba[0:7], little endian
sipk2_ba = sipkeys_ba[8:15], little endian
sipiv_ba = sipkeys_ba[16:23]

// overwrite the temp_key in memory, no longer needed
temp_key = (all zeros)
```
### 4) Фаза данных

Noise полезная нагрузка: Как определено ниже, включая случайное заполнение Не-noise полезная нагрузка: отсутствует

Начиная со 2-й части сообщения 3, все сообщения находятся внутри аутентифицированного и зашифрованного ChaChaPoly "фрейма" с предваряющей двухбайтовой обфусцированной длиной. Все заполнение находится внутри фрейма. Внутри фрейма используется стандартный формат с нулем или более "блоков". Каждый блок имеет однобайтовый тип и двухбайтовую длину. Типы включают дату/время, I2NP сообщение, опции, завершение и заполнение.

Примечание: Боб может, но не обязан, отправить свою RouterInfo Алисе в качестве первого сообщения Алисе на этапе передачи данных.

(Свойства безопасности полезной нагрузки из [Noise](https://noiseprotocol.org/noise.html))

```
XK(s, rs):           Authentication   Confidentiality
  <-                        2                5
  ->                        2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.
  This payload is encrypted based on an ephemeral-ephemeral DH as well as
  an ephemeral-static DH with the recipient's static key pair.
  Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated
  by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### Примечания

- Для эффективности и минимизации идентификации поля длины, реализации должны обеспечивать, чтобы отправитель буферизовал и затем отправлял полное содержимое сообщений данных за один раз, включая поле длины и AEAD фрейм. Это повышает вероятность того, что данные будут содержаться в одном TCP пакете (если не сегментированы ОС или промежуточными устройствами) и получены другой стороной целиком. Это также делается для эффективности и обеспечения действенности случайного заполнения.
- Router может выбрать завершение сессии при ошибке AEAD или может продолжить попытки коммуникации. При продолжении router должен завершить сессию после повторных ошибок.

#### Запутанная длина SipHash

Справочная информация: [SipHash](https://www.131002.net/siphash/)

После того как обе стороны завершили handshake, они передают полезные нагрузки, которые затем шифруются и аутентифицируются в "фреймах" ChaChaPoly.

Каждый фрейм предваряется двухбайтовой длиной в формате big endian. Эта длина указывает количество зашифрованных байтов фрейма, которые следуют далее, включая MAC. Чтобы избежать передачи идентифицируемых полей длины в потоке, длина фрейма обфусцируется путем применения операции XOR с маской, полученной из SipHash, как инициализировано из KDF фазы данных. Обратите внимание, что два направления имеют уникальные ключи SipHash и IV из KDF.

```
    sipk1, sipk2 = The SipHash keys from the KDF.  (two 8-byte long integers)
    IV[0] = sipiv = The SipHash IV from the KDF. (8 bytes)
    length is big endian.
    For each frame:
      IV[n] = SipHash-2-4(sipk1, sipk2, IV[n-1])
      Mask[n] = First 2 bytes of IV[n]
      obfuscatedLength = length ^ Mask[n]

    The first length output will be XORed with with IV[1].
```
Получатель имеет идентичные ключи SipHash и IV. Декодирование длины выполняется путем получения маски, используемой для обфускации длины, и применения операции XOR к усеченному дайджесту для получения длины кадра. Длина кадра - это общая длина зашифрованного кадра, включая MAC.

#### Примечания

- Если вы используете функцию библиотеки SipHash, которая возвращает беззнаковое длинное целое число, используйте два младших значащих байта в качестве маски. Преобразуйте длинное целое число в следующий IV в формате little endian.

#### Исходное содержимое

```
+----+----+----+----+----+----+----+----+
|obf size |                             |
+----+----+                             +
|                                       |
+   ChaChaPoly frame                    +
|   Encrypted and authenticated         |
+   key is k_ab for Alice to Bob        +
|   key is k_ba for Bob to Alice        |
+   as defined in KDF for data phase    +
|   n starts at 0 and increments        |
+   for each frame in that direction    +
|   no associated data                  |
+   16 bytes minimum                    +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

obf size :: 2 bytes length obfuscated with SipHash
            when de-obfuscated: 16 - 65535

Minimum size including length field is 18 bytes.
Maximum size including length field is 65537 bytes.
Obfuscated length is 2 bytes.
Maximum ChaChaPoly frame is 65535 bytes.
```
#### Примечания

- Поскольку получатель должен получить весь фрейм для проверки MAC, рекомендуется, чтобы отправитель ограничивал размер фреймов несколькими КБ, а не максимизировал размер фрейма. Это минимизирует задержку у получателя.

#### Незашифрованные данные

В зашифрованном фрейме содержится ноль или более блоков. Каждый блок содержит однобайтовый идентификатор, двухбайтовую длину и ноль или более байт данных.

Для обеспечения расширяемости получатели должны игнорировать блоки с неизвестными идентификаторами и обрабатывать их как заполнение.

Зашифрованные данные имеют максимальный размер 65535 байт, включая 16-байтовый заголовок аутентификации, поэтому максимальный размер незашифрованных данных составляет 65519 байт.

(Тег аутентификации Poly1305 не показан):

```
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
~               .   .   .               ~

blk :: 1 byte
       0 for datetime
       1 for options
       2 for RouterInfo
       3 for I2NP message
       4 for termination
       224-253 reserved for experimental features
       254 for padding
       255 reserved for future extension
size :: 2 bytes, big endian, size of data to follow, 0 - 65516
data :: the data

Maximum ChaChaPoly frame is 65535 bytes.
Poly1305 tag is 16 bytes
Maximum total block size is 65519 bytes
Maximum single block size is 65519 bytes
Block type is 1 byte
Block length is 2 bytes
Maximum single block data size is 65516 bytes.
```
#### Правила упорядочивания блоков

В сообщении handshake 3 части 2 порядок должен быть следующим: RouterInfo, затем Options если присутствует, затем Padding если присутствует. Никакие другие блоки не допускаются.

В фазе данных порядок не определен, за исключением следующих требований: Заполнение (Padding), если присутствует, должно быть последним блоком. Завершение (Termination), если присутствует, должно быть последним блоком за исключением Заполнения (Padding).

В одном кадре может быть несколько блоков I2NP. Множественные блоки Padding не разрешены в одном кадре. Другие типы блоков, вероятно, не будут иметь несколько блоков в одном кадре, но это не запрещено.

#### DateTime

Особый случай для синхронизации времени:

```
+----+----+----+----+----+----+----+
| 0  |    4    |     timestamp     |
+----+----+----+----+----+----+----+

blk :: 0
size :: 2 bytes, big endian, value = 4
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
```
ПРИМЕЧАНИЕ: Реализации должны округлять до ближайшей секунды, чтобы предотвратить смещение часов в сети.

#### Опции

Передать обновленные параметры. Параметры включают: минимальное и максимальное заполнение.

Блок опций будет иметь переменную длину.

```
+----+----+----+----+----+----+----+----+
| 1  |  size   |tmin|tmax|rmin|rmax|tdmy|
+----+----+----+----+----+----+----+----+
|tdmy|  rdmy   |  tdelay |  rdelay |    |
~----+----+----+----+----+----+----+    ~
|              more_options             |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 1
size :: 2 bytes, big endian, size of options to follow, 12 bytes minimum

tmin, tmax, rmin, rmax :: requested padding limits
    tmin and rmin are for desired resistance to traffic analysis.
    tmax and rmax are for bandwidth limits.
    tmin and tmax are the transmit limits for the router sending this options block.
    rmin and rmax are the receive limits for the router sending this options block.
    Each is a 4.4 fixed-point float representing 0 to 15.9375
    (or think of it as an unsigned 8-bit integer divided by 16.0).
    This is the ratio of padding to data. Examples:
    Value of 0x00 means no padding
    Value of 0x01 means add 6 percent padding
    Value of 0x10 means add 100 percent padding
    Value of 0x80 means add 800 percent (8x) padding
    Alice and Bob will negotiate the minimum and maximum in each direction.
    These are guidelines, there is no enforcement.
    Sender should honor receiver's maximum.
    Sender may or may not honor receiver's minimum, within bandwidth constraints.

tdmy: Max dummy traffic willing to send, 2 bytes big endian, bytes/sec average
rdmy: Requested dummy traffic, 2 bytes big endian, bytes/sec average
tdelay: Max intra-message delay willing to insert, 2 bytes big endian, msec average
rdelay: Requested intra-message delay, 2 bytes big endian, msec average

Padding distribution specified as additional parameters?
Random delay specified as additional parameters?

more_options :: Format TBD
```
#### Проблемы с настройками

- Формат опций еще не определен.
- Согласование опций еще не определено.

#### RouterInfo

Передать RouterInfo Алисы Бобу. Используется в сообщении handshake 3, часть 2. Передать RouterInfo Алисы Бобу или RouterInfo Боба Алисе. Используется опционально в фазе данных.

```
+----+----+----+----+----+----+----+----+
| 2  |  size   |flg |    RouterInfo     |
+----+----+----+----+                   +
| (Alice RI in handshake msg 3 part 2)  |
~ (Alice, Bob, or third-party           ~
|  RI in data phase)                    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 2
size :: 2 bytes, big endian, size of flag + router info to follow
flg :: 1 byte flags
       bit order: 76543210
       bit 0: 0 for local store, 1 for flood request
       bits 7-1: Unused, set to 0 for future compatibility
routerinfo :: Alice's or Bob's RouterInfo
```
#### Примечания

- При использовании в фазе данных получатель (Alice или Bob) должен проверить, что это тот же Router Hash, который был изначально отправлен (для Alice) или отправлен к (для Bob). Затем обработать его как локальное I2NP DatabaseStore сообщение. Проверить подпись, проверить более позднюю временную метку и сохранить в локальной netDb. Если флаговый бит 0 равен 1, и принимающая сторона является floodfill, обработать его как DatabaseStore сообщение с ненулевым reply token и передать ближайшим floodfill.
- Router Info НЕ сжимается с помощью gzip (в отличие от DatabaseStore сообщения, где он сжимается)
- Флудинг не должен запрашиваться, если в RouterInfo нет опубликованных RouterAddresses. Принимающий router не должен делать флудинг RouterInfo, если в нём нет опубликованных RouterAddresses.
- Разработчики должны обеспечить, что при чтении блока искажённые или вредоносные данные не приведут к чтению за пределы следующего блока.
- Этот протокол не предоставляет подтверждения того, что RouterInfo была получена, сохранена или передана флудингом (ни в фазе рукопожатия, ни в фазе данных). Если требуется подтверждение, и получатель является floodfill, отправитель должен вместо этого отправить стандартное I2NP DatabaseStoreMessage с reply token.

#### Проблемы

- Также может использоваться в фазе данных вместо I2NP DatabaseStoreMessage. Например, Bob может использовать это для запуска фазы данных.
- Разрешено ли, чтобы это содержало RI для router'ов, отличных от отправителя, как общая замена для DatabaseStoreMessages, например, для флуда от floodfill'ов?

#### I2NP сообщение

Одиночное I2NP сообщение с модифицированным заголовком. I2NP сообщения не могут быть фрагментированы между блоками или между ChaChaPoly фреймами.

Используется первые 9 байт из стандартного NTCP I2NP заголовка, и удаляются последние 7 байт заголовка следующим образом: сокращается срок истечения с 8 до 4 байт (секунды вместо миллисекунд, как для SSU), удаляется 2-байтовая длина (используется размер блока - 9), и удаляется однобайтовая контрольная сумма SHA256.

```
+----+----+----+----+----+----+----+----+
| 3  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |     message       |
+----+----+----+----+                   +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 3
size :: 2 bytes, big endian, size of type + msg id + exp + message to follow
        I2NP message body size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: I2NP message body
```
#### Примечания

- Разработчики должны обеспечить, что при чтении блока некорректные или вредоносные данные не вызовут выход за границы блока при чтении.

#### Завершение

Noise рекомендует явное сообщение о завершении соединения. Оригинальный NTCP его не имеет. Разорвать соединение. Это должен быть последний блок без заполнения в кадре.

```
+----+----+----+----+----+----+----+----+
| 4  |  size   |    valid data frames   |
+----+----+----+----+----+----+----+----+
    received   | rsn|     addl data     |
+----+----+----+----+                   +
~               .   .   .               ~
+----+----+----+----+----+----+----+----+

blk :: 4
size :: 2 bytes, big endian, value = 9 or more
valid data frames received :: The number of valid AEAD data phase frames received
                              (current receive nonce value)
                              0 if error occurs in handshake phase
                              8 bytes, big endian
rsn :: reason, 1 byte:
       0: normal close or unspecified
       1: termination received
       2: idle timeout
       3: router shutdown
       4: data phase AEAD failure
       5: incompatible options
       6: incompatible signature type
       7: clock skew
       8: padding violation
       9: AEAD framing error
       10: payload format error
       11: message 1 error
       12: message 2 error
       13: message 3 error
       14: intra-frame read timeout
       15: RI signature verification fail
       16: s parameter missing, invalid, or mismatched in RouterInfo
       17: banned
addl data :: optional, 0 or more bytes, for future expansion, debugging,
             or reason text.
             Format unspecified and may vary based on reason code.
```
#### Примечания

Не все причины могут фактически использоваться, зависит от реализации. Сбои handshake обычно приводят к закрытию с TCP RST вместо этого. См. примечания в разделах сообщений handshake выше. Дополнительные перечисленные причины предназначены для согласованности, логирования, отладки или при изменении политики.

#### Дополнение

Это для заполнения внутри AEAD-фреймов. Заполнение для сообщений 1 и 2 находится вне AEAD-фреймов. Все заполнение для сообщения 3 и фазы данных находится внутри AEAD-фреймов.

Заполнение внутри AEAD должно примерно соответствовать согласованным параметрам. Bob отправил свои запрошенные параметры tx/rx min/max в сообщении 2. Alice отправила свои запрошенные параметры tx/rx min/max в сообщении 3. Обновленные опции могут быть отправлены во время фазы передачи данных. См. информацию о блоке опций выше.

Если присутствует, этот блок должен быть последним в кадре.

```
+----+----+----+----+----+----+----+----+
|254 |  size   |      padding           |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 254
size :: 2 bytes, big endian, size of padding to follow
padding :: random data
```
#### Примечания

- Размер = 0 разрешен.
- Стратегии заполнения требуют уточнения.
- Минимальное заполнение требует уточнения.
- Фреймы только с заполнением разрешены.
- Заполнение по умолчанию требует уточнения.
- См. блок опций для согласования параметров заполнения
- См. блок опций для параметров мин/макс заполнения
- Noise ограничивает сообщения до 64КБ. Если необходимо больше заполнения, отправляйте несколько фреймов.
- Реакция router на нарушение согласованного заполнения зависит от реализации.

#### Другие типы блоков

Реализации должны игнорировать неизвестные типы блоков для обеспечения прямой совместимости, за исключением сообщения 3 части 2, где неизвестные блоки не допускаются.

#### Будущая работа

- Длина заполнения должна определяться либо для каждого сообщения отдельно на основе оценок распределения длин, либо должны добавляться случайные задержки. Эти контрмеры необходимо включить для противодействия DPI, поскольку размеры сообщений иначе могли бы выдать, что транспортный протокол передает I2P трафик. Точная схема заполнения является областью будущей работы.

### 5) Прекращение

Соединения могут быть завершены через обычное или аварийное закрытие TCP сокета, или, как рекомендует Noise, через явное сообщение о завершении. Явное сообщение о завершении определено в фазе данных выше.

При любом нормальном или аварийном завершении работы router должны обнулить все временные данные в памяти, включая временные ключи рукопожатия, симметричные криптографические ключи и связанную информацию.

## Опубликованная информация о маршрутизаторе

### Возможности

Начиная с релиза 0.9.50, опция "caps" поддерживается в NTCP2 адресах, аналогично SSU. Одна или более возможностей могут быть опубликованы в опции "caps". Возможности могут быть в любом порядке, но "46" является рекомендуемым порядком для согласованности между реализациями. Определены две возможности:

4: Указывает на возможность исходящих IPv4 соединений. Если IP опубликован в поле host, эта возможность не требуется. Если router скрыт или NTCP2 работает только на исходящих соединениях, '4' и '6' могут быть объединены в одном адресе.

6: Указывает на возможность исходящих IPv6 соединений. Если IP-адрес опубликован в поле host, эта возможность не обязательна. Если router скрыт или NTCP2 работает только на исходящие соединения, '4' и '6' могут быть объединены в одном адресе.

### Опубликованные адреса

Опубликованный RouterAddress (часть RouterInfo) будет иметь идентификатор протокола либо "NTCP", либо "NTCP2".

RouterAddress должен содержать опции "host" и "port", как в текущем протоколе NTCP.

RouterAddress должен содержать три параметра для указания поддержки NTCP2:

- s=(Base64 ключ) Текущий статический открытый ключ Noise (s) для данного RouterAddress. Закодирован в Base 64 с использованием стандартного алфавита I2P Base 64. 32 байта в двоичном формате, 44 байта в кодировке Base 64, открытый ключ X25519 в формате little-endian.
- i=(Base64 IV) Текущий IV для шифрования значения X в сообщении 1 для данного RouterAddress. Закодирован в Base 64 с использованием стандартного алфавита I2P Base 64. 16 байт в двоичном формате, 24 байта в кодировке Base 64, формат big-endian.
- v=2 Текущая версия (2). При публикации как "NTCP" подразумевается дополнительная поддержка версии 1. Поддержка будущих версий будет осуществляться через значения, разделенные запятыми, например v=2,3. Реализация должна проверять совместимость, включая множественные версии при наличии запятой. Версии, разделенные запятыми, должны быть в числовом порядке.

Алиса должна убедиться, что все три опции присутствуют и действительны перед подключением с использованием протокола NTCP2.

Когда публикуется как "NTCP" с опциями "s", "i" и "v", router должен принимать входящие соединения на этом хосте и порту для обоих протоколов NTCP и NTCP2, и автоматически определять версию протокола.

При публикации как "NTCP2" с опциями "s", "i" и "v", router принимает входящие соединения на этом хосте и порту только для протокола NTCP2.

Если router поддерживает как NTCP1, так и NTCP2 соединения, но не реализует автоматическое определение версии для входящих соединений, он должен объявлять и "NTCP", и "NTCP2" адреса, и включать параметры NTCP2 только в "NTCP2" адрес. Router должен устанавливать более низкое значение стоимости (более высокий приоритет) в "NTCP2" адресе, чем в "NTCP" адресе, чтобы NTCP2 был предпочтительным.

Если несколько NTCP2 RouterAddresses (либо как "NTCP", либо как "NTCP2") публикуются в одном RouterInfo (для дополнительных IP-адресов или портов), все адреса, указывающие один и тот же порт, должны содержать идентичные опции и значения NTCP2. В частности, все должны содержать один и тот же статический ключ и iv.

### Неопубликованный NTCP2 адрес

Если Alice не публикует свой NTCP2 адрес (как "NTCP" или "NTCP2") для входящих соединений, она должна опубликовать router адрес "NTCP2", содержащий только её статический ключ и версию NTCP2, чтобы Bob мог проверить ключ после получения RouterInfo от Alice в сообщении 3, части 2.

- s=(Base64 ключ) Как определено выше для опубликованных адресов.
- v=2 Как определено выше для опубликованных адресов.

Этот адрес router не будет содержать опции "i", "host" или "port", поскольку они не требуются для исходящих NTCP2 соединений. Опубликованная стоимость для этого адреса не имеет строгого значения, поскольку он предназначен только для входящих соединений; однако, это может быть полезно для других router, если стоимость установлена выше (меньший приоритет), чем у других адресов. Рекомендуемое значение — 14.

Alice может также просто добавить опции "s" и "v" к существующему опубликованному адресу "NTCP".

### Ротация открытого ключа и вектора инициализации

Из-за кэширования RouterInfo, router'ы не должны ротировать статический публичный ключ или IV пока router работает, независимо от того, находится ли он в опубликованном адресе или нет. Router'ы должны постоянно хранить этот ключ и IV для повторного использования после немедленной перезагрузки, чтобы входящие соединения продолжали работать, и времена перезапуска не раскрывались. Router'ы должны постоянно хранить или иным образом определять время последнего выключения, чтобы предыдущий период простоя мог быть вычислен при запуске.

С учетом опасений по поводу раскрытия времени перезапуска, router'ы могут сменить этот ключ или IV при запуске, если router ранее был отключен в течение некоторого времени (как минимум пару часов).

Если router имеет опубликованные NTCP2 RouterAddresses (как NTCP или NTCP2), минимальное время простоя перед ротацией должно быть намного больше, например один месяц, если только не изменился локальный IP-адрес или router не выполнил "rekeys" (перегенерацию ключей).

Если router имеет любые опубликованные SSU RouterAddresses, но не NTCP2 (как NTCP или NTCP2), минимальное время простоя перед ротацией должно быть больше, например один день, если только локальный IP-адрес не изменился или router не выполнил "rekeys". Это применимо даже если опубликованный SSU адрес имеет introducers.

Если router не имеет опубликованных RouterAddresses (NTCP, NTCP2 или SSU), минимальное время простоя перед ротацией может составлять всего два часа, даже при изменении IP-адреса, если только router не выполнит "rekeys".

Если router "перегенерирует ключи" на другой Router Hash, он также должен сгенерировать новый ключ noise и IV.

Реализации должны учитывать, что изменение статического публичного ключа или IV запретит входящие NTCP2 соединения от router'ов, которые закешировали более старую RouterInfo. Публикация RouterInfo, выбор peer'ов для tunnel'ов (включая как OBGW, так и IB ближайший hop), выбор zero-hop tunnel'ов, выбор транспорта и другие стратегии реализации должны это учитывать.

Ротация IV подчиняется тем же правилам, что и ротация ключей, за исключением того, что IV присутствуют только в опубликованных RouterAddresses, поэтому для скрытых роутеров или роутеров за межсетевым экраном IV отсутствует. При любых изменениях (версия, ключ, опции?) рекомендуется также изменить IV.

Примечание: Минимальное время простоя перед повторной генерацией ключей может быть изменено для обеспечения здоровья сети и предотвращения повторного получения адресов router'ом, который был отключен в течение умеренного периода времени.

## Определение версии

Когда опубликовано как "NTCP", router должен автоматически определять версию протокола для входящих соединений.

Это обнаружение зависит от реализации, но вот общие рекомендации.

Для определения версии входящего NTCP соединения, Боб действует следующим образом:

- Дождитесь как минимум 64 байта (минимальный размер сообщения 1 NTCP2)

- Если изначально полученные данные составляют 288 или более байт, входящее соединение имеет версию 1.

- Если меньше 288 байт, то либо

> - Подождать короткое время для получения дополнительных данных (хорошая стратегия до широкого внедрения NTCP2), если получено как минимум 288 байт всего, это NTCP 1.   >   > - Попробовать первые этапы декодирования как версию 2, если это не удается, подождать короткое время для получения дополнительных данных (хорошая стратегия после широкого внедрения NTCP2)   >   >   > - Расшифровать первые 32 байта (ключ X) пакета SessionRequest с использованием AES-256 с ключом RH_B.   >   > - Проверить валидную точку на кривой. Если проверка не удается, подождать короткое время для получения дополнительных данных для NTCP 1   >   > - Проверить AEAD фрейм. Если проверка не удается, подождать короткое время для получения дополнительных данных для NTCP 1

Обратите внимание, что изменения или дополнительные стратегии могут быть рекомендованы, если мы обнаружим активные атаки TCP-сегментации на NTCP 1.

Для облегчения быстрого обнаружения версии и установления соединения, реализации должны обеспечивать, чтобы Алиса буферизировала, а затем отправляла полное содержимое первого сообщения за один раз, включая заполнение. Это повышает вероятность того, что данные будут содержаться в одном TCP-пакете (если только не сегментированы ОС или промежуточными устройствами) и получены Бобом сразу целиком. Это также делается для эффективности и обеспечения результативности случайного заполнения. Это относится как к NTCP, так и к NTCP2 handshake.

## Варианты, резервные решения и общие проблемы

- Если и Алиса, и Боб поддерживают NTCP2, Алиса должна подключаться через NTCP2.
- Если Алиса не сможет подключиться к Бобу используя NTCP2 по любой причине, подключение завершается неудачей. Алиса не может повторить попытку используя NTCP 1.

## Рекомендации по расхождению часов

Временные метки пиров включаются в первые два сообщения рукопожатия: Session Request и Session Created. Расхождение часов между двумя пирами более +/- 60 секунд обычно является фатальным. Если Bob считает, что его локальные часы неточны, он может скорректировать свои часы, используя вычисленное расхождение или какой-либо внешний источник. В противном случае Bob должен ответить сообщением Session Created даже при превышении максимального расхождения, а не просто закрывать соединение. Это позволяет Alice получить временную метку Bob и вычислить расхождение, а также принять необходимые меры при необходимости. У Bob на данном этапе нет идентификатора router Alice, но для экономии ресурсов может быть желательно для Bob заблокировать входящие соединения с IP-адреса Alice на некоторое время или после повторных попыток подключения с чрезмерным расхождением.

Alice должна скорректировать рассчитанное отклонение часов, вычтя половину RTT. Если Alice считает, что её локальные часы неточны, она может настроить свои часы, используя рассчитанное отклонение или какой-либо внешний источник. Если Alice считает, что часы Bob неточны, она может заблокировать Bob на некоторое время. В любом случае Alice должна закрыть соединение.

Если Алиса все же отвечает Session Confirmed (вероятно, потому что расхождение времени очень близко к пределу в 60 секунд, и вычисления Алисы и Боба не совпадают точно из-за RTT), Боб должен скорректировать вычисленное расхождение времени, вычтя половину RTT. Если скорректированное расхождение времени превышает максимум, Боб должен ответить сообщением Disconnect, содержащим код причины расхождения времени, и закрыть соединение. На этом этапе у Боба есть идентификатор router Алисы, и он может заблокировать Алису на некоторый период времени.

## Ссылки

- [Общие структуры](/docs/specs/common-structures)
- [I2NP](/docs/specs/i2np)
- [Сетевая база данных](/docs/overview/network-database)
- [NOISE - Фреймворк протокола Noise](https://noiseprotocol.org/noise.html)
- [NTCP](/docs/transport/ntcp)
- [Prop104](/proposals/104-tls-transport)
- [Prop109](/proposals/109-pt-transport)
- [Prop111](/proposals/111-ntcp-2)
- [RFC-2104 - HMAC](https://tools.ietf.org/html/rfc2104)
- [RFC-3526 - DH Groups](https://tools.ietf.org/html/rfc3526)
- [RFC-6151](https://tools.ietf.org/html/rfc6151)
- [RFC-7539 - ChaCha20-Poly1305](https://tools.ietf.org/html/rfc7539)
- [RFC-7748 - X25519](https://tools.ietf.org/html/rfc7748)
- [RFC-7905](https://tools.ietf.org/html/rfc7905)
- [SipHash](https://www.131002.net/siphash/)
- [SSU](/docs/transport/ssu)
- **[STS]** Diffie, W.; van Oorschot P. C.; Wiener M. J., Аутентификация и аутентифицированный обмен ключами
