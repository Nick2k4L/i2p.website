---
title: "Спецификация SSU2"
description: "Протокол безопасного полунадежного UDP-транспорта версии 2"
slug: "ssu2"
category: "Транспорты"
lastUpdated: "2025-04"
accurateFor: "0.9.65"
---

## Статус

Практически завершено. См. [Prop159](/proposals/159-ssu2) для дополнительной информации и целей, включая анализ безопасности, модели угроз, обзор безопасности SSU 1 и проблем, а также выдержки из спецификаций QUIC.

План развертывания:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Feature</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Testing (not default)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Enabled by default</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Local test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-03</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test in-net</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze basic protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Basic Session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address Validation (Retry)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Fragmented RI in handshake</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze extended protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Enable for random 2%</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Validation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Connection Migration</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Immediate ACK flag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Key Rotation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2023-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (i2pd)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (Java I2P)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.61 2023-12</td></tr>
  </tbody>
</table>
Базовая сессия включает фазу handshake и фазу данных. Расширенный протокол включает relay и peer test.

## Обзор

Данная спецификация определяет протокол аутентифицированного согласования ключей для повышения устойчивости [SSU](/docs/transport/ssu) к различным формам автоматизированной идентификации и атак.

Как и другие транспорты I2P, SSU2 предназначен для точка-точка (router-to-router) передачи I2NP сообщений. Это не универсальный канал передачи данных. Как и [SSU](/docs/transport/ssu), он также предоставляет два дополнительных сервиса: Релеинг для преодоления NAT и Тестирование пиров для определения доступности входящих соединений. Он также предоставляет третий сервис, отсутствующий в SSU, для миграции соединений когда узел изменяет IP или порт.

## Обзор архитектуры

### Резюме

Мы опираемся на несколько существующих протоколов, как внутри I2P, так и внешних стандартов, для вдохновения, руководства и повторного использования кода:

- Модели угроз: Из NTCP2 [NTCP2](/docs/specs/ntcp2), со значительными дополнительными угрозами, относящимися к UDP транспорту, как проанализировано в QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Криптографические решения: Из [NTCP2](/docs/specs/ntcp2).
- Рукопожатие: Noise XK из [NTCP2](/docs/specs/ntcp2) и [NOISE](https://noiseprotocol.org/noise.html). Значительные упрощения NTCP2 возможны благодаря инкапсуляции (врожденным границам сообщений), предоставляемой UDP.
- Обфускация эфемерного ключа рукопожатия: Адаптировано из [NTCP2](/docs/specs/ntcp2), но используя ChaCha20 из [ECIES](/docs/specs/ecies) вместо AES.
- Заголовки пакетов: Адаптировано из WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) и QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Обфускация заголовков пакетов: Адаптировано из [NTCP2](/docs/specs/ntcp2), но используя ChaCha20 из [ECIES](/docs/specs/ecies) вместо AES.
- Защита заголовков пакетов: Адаптировано из QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) и [Nonces](https://eprint.iacr.org/2019/624.pdf)
- Заголовки используются как ассоциированные данные AEAD как в [ECIES](/docs/specs/ecies).
- Нумерация пакетов: Адаптировано из WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) и QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Сообщения: Адаптировано из [SSU](/docs/transport/ssu)
- Фрагментация I2NP: Адаптировано из [SSU](/docs/transport/ssu)
- Ретрансляция и тестирование узлов: Адаптировано из [SSU](/docs/transport/ssu)
- Подписи данных ретрансляции и тестирования узлов: Из спецификации общих структур [Common](/docs/specs/common-structures)
- Формат блока: Из [NTCP2](/docs/specs/ntcp2) и [ECIES](/docs/specs/ecies).
- Заполнение и опции: Из [NTCP2](/docs/specs/ntcp2) и [ECIES](/docs/specs/ecies).
- Подтверждения, отрицательные подтверждения: Адаптировано из QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000).
- Управление потоком: Будет определено позже

В I2P не используются новые криптографические примитивы, которые не применялись ранее.

### Гарантии доставки

Как и другие транспорты I2P NTCP, NTCP2 и SSU 1, этот транспорт не является универсальным средством для доставки упорядоченного потока байтов. Он предназначен для транспорта I2NP сообщений. Абстракция "потока" не предоставляется.

Кроме того, как и для SSU, он содержит дополнительные средства для обхода NAT с помощью узлов и тестирования доступности (входящих соединений).

Что касается SSU 1, он НЕ обеспечивает доставку I2NP сообщений в правильном порядке. Также он не гарантирует доставку I2NP сообщений. Из соображений эффективности, или из-за доставки UDP датаграмм не по порядку или потери этих датаграмм, I2NP сообщения могут доставляться на удаленный конец не по порядку или могут вообще не доставляться. I2NP сообщение может быть повторно передано несколько раз при необходимости, но доставка может в конечном итоге завершиться неудачей, не вызывая при этом полного разрыва соединения. Кроме того, новые I2NP сообщения могут продолжать отправляться даже во время повторной передачи (восстановления после потерь) других I2NP сообщений.

Этот протокол НЕ предотвращает полностью дублированную доставку I2NP сообщений. Роутер должен обеспечивать истечение срока действия I2NP и использовать фильтр Блума или другой механизм на основе идентификатора I2NP сообщения. См. раздел "Дублирование I2NP сообщений" ниже.

### Фреймворк протокола Noise

Данная спецификация определяет требования на основе Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (редакция 33, 2017-10-04). Noise обладает схожими свойствами с протоколом Station-To-Station [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol), который является основой для протокола [SSU](/docs/transport/ssu). В терминологии Noise Алиса является инициатором, а Боб — отвечающей стороной.

SSU2 основан на протоколе Noise Noise_XK_25519_ChaChaPoly_SHA256. (Фактический идентификатор для начальной функции деривации ключей - "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256", чтобы указать расширения I2P - см. раздел KDF 1 ниже)

ПРИМЕЧАНИЕ: Этот идентификатор отличается от используемого для NTCP2, поскольку все три сообщения handshake используют заголовок как связанные данные.

Этот протокол Noise использует следующие примитивы:

- Handshake Pattern: XK Алиса передает свой ключ Бобу (X) Алиса уже знает статический ключ Боба (K)
- DH Function: X25519 X25519 DH с длиной ключа 32 байта, как указано в [RFC-7748](https://tools.ietf.org/html/rfc7748).
- Cipher Function: ChaChaPoly AEAD_CHACHA20_POLY1305, как указано в [RFC-7539](https://tools.ietf.org/html/rfc7539) раздел 2.8. 12-байтовый nonce, при этом первые 4 байта устанавливаются в ноль.
- Hash Function: SHA256 Стандартный 32-байтовый хеш, уже широко используемый в I2P.

### Дополнения к фреймворку

Данная спецификация определяет следующие улучшения для Noise_XK_25519_ChaChaPoly_SHA256. Они в целом следуют рекомендациям из раздела 13 [NOISE](https://noiseprotocol.org/noise.html).

1) Сообщения рукопожатия (Session Request, Created, Confirmed) включают заголовок размером 16 или 32 байта. 2) Заголовки сообщений рукопожатия (Session Request, Created, Confirmed) используются как входные данные для mixHash() перед шифрованием/расшифровкой для привязки заголовков к сообщению. 3) Заголовки зашифрованы и защищены. 4) Открытые эфемерные ключи обфусцированы с помощью шифрования ChaCha20, используя известный ключ и IV. Это быстрее, чем elligator2. 5) Формат полезной нагрузки определен для сообщений 1, 2 и фазы данных. Конечно, это не определено в Noise.

Фаза данных использует шифрование, похожее на фазу данных Noise, но не совместимое с ней.

## Определения

Мы определяем следующие функции, соответствующие используемым криптографическим строительным блокам.

ZEROLEN

:   массив байтов нулевой длины

H(p, d)

:   Хеш-функция SHA-256, которая принимает строку персонализации p и данные d, и производит выходные данные длиной 32 байта. Как определено в [NOISE](https://noiseprotocol.org/noise.html). || ниже означает присоединение.

    Use SHA-256 as follows:

        H(p, d) := SHA-256(p || d)

MixHash(d)

:   Хеш-функция SHA-256, которая принимает предыдущий хеш h и новые данные d, и производит выходные данные длиной 32 байта. || ниже означает добавление.

    Use SHA-256 as follows:

        MixHash(d) := h = SHA-256(h || d)

STREAM

:   ChaCha20/Poly1305 AEAD как указано в [RFC-7539](https://tools.ietf.org/html/rfc7539). S_KEY_LEN = 32 и S_IV_LEN = 12.

    ENCRYPT(k, n, plaintext, ad)

    :   Encrypts plaintext using the cipher key k, and nonce n which MUST be unique for the key k. Associated data ad is optional. Returns a ciphertext that is the size of the plaintext + 16 bytes for the HMAC.

        The entire ciphertext must be indistinguishable from random if the key is secret.

    DECRYPT(k, n, ciphertext, ad)

    :   Decrypts ciphertext using the cipher key k, and nonce n. Associated data ad is optional. Returns the plaintext.

DH

:   Система согласования открытых ключей X25519. Приватные ключи 32 байта, открытые ключи 32 байта, выходные данные 32 байта. Имеет следующие функции:

    GENERATE_PRIVATE()

    :   Generates a new private key.

    DERIVE_PUBLIC(privkey)

    :   Returns the public key corresponding to the given private key.

    DH(privkey, pubkey)

    :   Generates a shared secret from the given private and public keys.

HKDF(salt, ikm, info, n)

:   Криптографическая функция выведения ключей, которая принимает исходный ключевой материал ikm (который должен иметь хорошую энтропию, но не обязан быть равномерно случайной строкой), соль длиной 32 байта и контекстно-специфичное значение 'info', и производит выходные данные длиной n байт, подходящие для использования в качестве ключевого материала.

    Use HKDF as specified in [RFC-5869](https://tools.ietf.org/html/rfc5869), using the HMAC hash function SHA-256 as specified in [RFC-2104](https://tools.ietf.org/html/rfc2104). This means that SALT_LEN is 32 bytes max.

MixKey(d)

:   Использует HKDF() с предыдущим chainKey и новыми данными d, и устанавливает новый chainKey и k. Как определено в [NOISE](https://noiseprotocol.org/noise.html).

    Use HKDF as follows:

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]

## Сообщения

Каждая UDP датаграмма содержит точно одно сообщение. Длина датаграммы (после заголовков IP и UDP) является длиной сообщения. Заполнение, если оно есть, содержится в блоке заполнения внутри сообщения. В этом документе мы используем термины "датаграмма" и "пакет" в основном взаимозаменяемо. Каждая датаграмма (или пакет) содержит одно сообщение (в отличие от QUIC, где датаграмма может содержать несколько QUIC пакетов). "Заголовок пакета" - это часть после заголовка IP/UDP.

Исключение: Сообщение Session Confirmed уникально тем, что может быть фрагментировано на несколько пакетов. Дополнительную информацию см. в разделе "Фрагментация Session Confirmed" ниже.

Все сообщения SSU2 имеют длину не менее 40 байт. Любое сообщение длиной 1-39 байт является недействительным. Все сообщения SSU2 имеют длину не более 1472 (IPv4) или 1452 (IPv6) байт. Формат сообщений основан на Noise сообщениях с модификациями для кадрирования и неразличимости. Реализации, использующие стандартные библиотеки Noise, должны предварительно обрабатывать полученные сообщения в стандартный формат сообщений Noise. Все зашифрованные поля являются AEAD шифротекстами.

Определены следующие сообщения:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Encr. Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionRequest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionCreated</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionConfirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">PeerTest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">HolePunch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
  </tbody>
</table>
### Установление сессии

Стандартная последовательность установления соединения, когда у Алисы есть действительный токен, ранее полученный от Боба, выглядит следующим образом:

```
Alice Bob

SessionRequest -------------------> <------------------- SessionCreated SessionConfirmed ----------------->
```
Когда у Alice нет действительного токена, последовательность установления соединения выглядит следующим образом:

```
Alice Bob

TokenRequest ---------------------> <--------------------------- Retry SessionRequest -------------------> <------------------- SessionCreated SessionConfirmed ----------------->
```
Когда Алиса считает, что у неё есть действительный токен, но Боб отклоняет его (возможно, потому что Боб перезапустился), последовательность установления соединения выглядит следующим образом:

```
Alice Bob

SessionRequest -------------------> <--------------------------- Retry SessionRequest -------------------> <------------------- SessionCreated SessionConfirmed ----------------->
```
Bob может отклонить запрос сессии или токена, ответив сообщением Retry, содержащим блок Termination с кодом причины. Основываясь на коде причины, Alice не должна предпринимать еще одну попытку запроса в течение некоторого периода времени:

```
Alice Bob

SessionRequest -------------------> <--------------------------- Retry containing a Termination block

or

TokenRequest ---------------------> <--------------------------- Retry containing a Termination block
```
Используя терминологию Noise, последовательность установления соединения и передачи данных выглядит следующим образом: (Свойства безопасности полезной нагрузки)

```
XK(s, rs): Authentication Confidentiality

<- s \... -> e, es 0 2 <- e, ee 2 1 -> s, se 2 5 <- 2 5
```
После установления сессии Алиса и Боб могут обмениваться сообщениями Data.

### Заголовок пакета

Все пакеты начинаются с обфускированного (зашифрованного) заголовка. Существует два типа заголовков: длинный и короткий. Обратите внимание, что первые 13 байт (Destination Connection ID, номер пакета и тип) одинаковы для всех заголовков.

#### Длинный заголовок

Длинный заголовок составляет 32 байта. Он используется до создания сессии для Token Request, SessionRequest, SessionCreated и Retry. Он также используется для сообщений Peer Test и Hole Punch вне сессии.

Перед шифрованием заголовка:

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-------------------------------------------+----------+----------+----------+----------+
    | > Packet Number                           | type     | ver      | id       | flag     |
    +-------------------------------------------+----------+----------+----------+----------+
    | > Source Connection ID                                                                |
    +---------------------------------------------------------------------------------------+
    | > Token                                                                               |
    +---------------------------------------------------------------------------------------+

    Destination Connection ID :: 8 bytes, unsigned big endian integer

    Packet Number :: 4 bytes, unsigned big endian integer

    type :: The message type = 0, 1, 7, 9, 10, or 11

    ver :: The protocol version, equal to 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Source Connection ID :: 8 bytes, unsigned big endian integer

    Token :: 8 bytes, unsigned big endian integer
```
#### Краткий заголовок

Короткий заголовок составляет 16 байт. Он используется для сообщений Session Created и Data. Неаутентифицированные сообщения, такие как Session Request, Retry и Peer Test, всегда используют длинный заголовок.

Требуется 16 байт, поскольку получатель должен расшифровать первые 16 байт, чтобы получить тип сообщения, а затем должен расшифровать дополнительные 16 байт, если это действительно длинный заголовок, как указано типом сообщения.

Для Session Confirmed, до шифрования заголовка:

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-----------------------------------+------+------+-------------+
    | > Packet Number                   | type | frag | > flags     |
    +-----------------------------------+------+------+-------------+

    Destination Connection ID :: 8 bytes, unsigned big endian integer

    Packet Number :: 4 bytes, all zeros

    type :: The message type = 2

    frag :: 1 byte fragment info:

    :   bit order: 76543210 (bit 7 is MSB) bits 7-4: fragment number 0-14, big endian bits 3-0: total fragments 1-15, big endian

    flags :: 2 bytes, unused, set to 0 for future compatibility
```
См. раздел "Session Confirmed Fragmentation" ниже для получения дополнительной информации о поле frag.

Для сообщений Data, перед шифрованием заголовка:

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-----------------------------------+------+------+---------------+
    | > Packet Number                   | type | flag | moreflags     |
    +-----------------------------------+------+------+---------------+

    Destination Connection ID :: 8 bytes, unsigned big endian integer

    Packet Number :: 4 bytes, unsigned big endian integer

    type :: The message type = 6

    flag :: 1 byte flags:

    :   bit order: 76543210 (bit 7 is MSB) bits 7-1: unused, set to 0 for future compatibility bits 0: when set to 1, immediate ack requested

    moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### Нумерация идентификаторов соединений

Идентификаторы соединений должны генерироваться случайным образом. Идентификаторы источника и назначения НЕ должны быть идентичными, чтобы атакующий на пути передачи не мог захватить и отправить пакет обратно отправителю, который выглядел бы валидным. НЕ используйте счетчик для генерации идентификаторов соединений, чтобы атакующий на пути передачи не мог сгенерировать пакет, который выглядел бы валидным.

В отличие от QUIC, мы не изменяем идентификаторы соединения во время или после рукопожатия, даже после сообщения Retry. Идентификаторы остаются постоянными от первого сообщения (Token Request или Session Request) до последнего сообщения (Data with Termination). Кроме того, идентификаторы соединения не изменяются во время или после проверки пути или миграции соединения.

Также отличием от QUIC является то, что идентификаторы соединений в заголовках всегда зашифрованы на уровне заголовков. См. ниже.

#### Нумерация пакетов

Если блок First Packet Number не отправляется в handshake, пакеты нумеруются в рамках одной сессии для каждого направления, начиная с 0, до максимума (2**32 -1). Сессия должна быть завершена, и создана новая сессия, задолго до отправки максимального количества пакетов.

Если блок First Packet Number отправляется в рукопожатии, пакеты нумеруются в рамках одной сессии для данного направления, начиная с этого номера пакета. Номер пакета может циклически повторяться во время сессии. Когда максимальное количество 2**32 пакетов было отправлено, происходит возврат номера пакета к первому номеру пакета, и эта сессия больше не является действительной. Сессия должна быть завершена, и должна быть создана новая сессия, задолго до того, как будет отправлено максимальное количество пакетов.

TODO ротация ключей, уменьшить максимальный номер пакета?

Пакеты handshake, которые определяются как потерянные, ретранслируются целиком с идентичным заголовком, включая номер пакета. Сообщения handshake Session Request, Session Created и Session Confirmed ДОЛЖНЫ быть ретранслированы с тем же номером пакета и идентичным зашифрованным содержимым, чтобы для шифрования ответа использовался тот же цепочечный хеш. Сообщение Retry никогда не передается.

Пакеты фазы данных, которые определяются как потерянные, никогда не передаются повторно целиком (за исключением завершения, см. ниже). То же самое применяется к блокам, содержащимся в потерянных пакетах. Вместо этого информация, которая может содержаться в блоках, отправляется снова в новых пакетах по мере необходимости. Пакеты данных никогда не передаются повторно с тем же номером пакета. Любая повторная передача содержимого пакета (независимо от того, остается ли содержимое прежним) должна использовать следующий неиспользованный номер пакета.

Повторная передача неизменённого целого пакета как есть, с тем же номером пакета, не разрешена по нескольким причинам. Для справки см. QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) раздел 12.3.

- Неэффективно хранить пакеты для повторной передачи
- Новый пакет данных выглядит по-другому для наблюдателя на пути, невозможно определить, что он повторно передан
- С новым пакетом отправляется обновленный блок подтверждений, а не старый блок подтверждений
- Вы повторно передаете только то, что необходимо. некоторые фрагменты могли уже быть переданы повторно один раз и получить подтверждение
- Вы можете поместить столько, сколько нужно, в каждый повторно передаваемый пакет, если ожидается больше данных
- Конечные точки, которые отслеживают все отдельные пакеты с целью обнаружения дубликатов, рискуют накопить избыточное состояние. Данные, необходимые для обнаружения дубликатов, можно ограничить, поддерживая минимальный номер пакета, ниже которого все пакеты немедленно отбрасываются.
- Эта схема гораздо более гибкая

Новые пакеты используются для передачи информации, которая была определена как потерянная. В общем случае информация отправляется повторно, когда пакет, содержащий эту информацию, определяется как потерянный, и отправка прекращается, когда пакет, содержащий эту информацию, получает подтверждение.

Исключение: Пакет фазы данных, содержащий блок завершения, может быть, но не обязан быть, ретранслирован целиком, как есть. См. раздел "Завершение сессии" ниже.

Следующие пакеты содержат случайный номер пакета, который игнорируется:

- Запрос сессии
- Сессия создана
- Запрос токена
- Повтор
- Тест пира
- Пробивание NAT

Для Alice нумерация исходящих пакетов начинается с 0 с пакета Session Confirmed. Для Bob нумерация исходящих пакетов начинается с 0 с первого пакета Data, который должен быть ACK пакета Session Confirmed. Номера пакетов в примере стандартного рукопожатия будут следующими:

```
Alice Bob

SessionRequest (r) ------------> <------------- SessionCreated (r) SessionConfirmed (0) ------------> <------------- Data (0) (Ack-only) Data (1) ------------> (May be sent before Ack is received) <------------- Data (1) Data (2) ------------> Data (3) ------------> Data (4) ------------> <------------- Data (2)

r = random packet number (ignored) Token Request, Retry, and Peer Test also have random packet numbers.
```
Любая повторная передача сообщений handshake (SessionRequest, SessionCreated или SessionConfirmed) должна быть отправлена без изменений, с тем же номером пакета. Не используйте разные эфемерные ключи и не изменяйте полезную нагрузку при повторной передаче этих сообщений.

#### Привязка заголовка

Заголовок (до обфускации и защиты) всегда включается в ассоциированные данные для функции AEAD, чтобы криптографически привязать заголовок к данным.

#### Шифрование заголовков

Шифрование заголовков преследует несколько целей. См. раздел "Дополнительное обсуждение DPI" выше для получения справочной информации и предположений.

- Предотвратить идентификацию протокола онлайн DPI
- Предотвратить закономерности в серии сообщений в одном соединении, за исключением повторных передач handshake
- Предотвратить закономерности в сообщениях одного типа в разных соединениях
- Предотвратить расшифровку заголовков handshake без знания introduction key, найденного в netDb
- Предотвратить идентификацию эфемерных ключей X25519 без знания introduction key, найденного в netDb
- Предотвратить расшифровку номера и типа пакета фазы данных любым онлайн или офлайн атакующим
- Предотвратить внедрение валидных пакетов handshake наблюдателем на пути или вне пути без знания introduction key, найденного в netDb
- Предотвратить внедрение валидных пакетов данных наблюдателем на пути или вне пути
- Обеспечить быструю и эффективную классификацию входящих пакетов
- Обеспечить устойчивость к "зондированию", чтобы не было ответа на неверный Session Request, или если есть ответ Retry, ответ не идентифицировался как I2P без знания introduction key, найденного в netDb
- Destination Connection ID не является критичными данными, и допустимо, если он может быть расшифрован наблюдателем со знанием introduction key, найденного в netDb
- Номер пакета в фазе данных является AEAD nonce и представляет критичные данные. Он не должен расшифровываться наблюдателем даже со знанием introduction key, найденного в netDb. См. [Nonces](https://eprint.iacr.org/2019/624.pdf).

Заголовки шифруются с использованием известных ключей, опубликованных в сетевой базе данных или вычисленных позже. На этапе установления соединения это служит только для сопротивления DPI, поскольку ключ является публичным, а ключ и nonce используются повторно, поэтому фактически это просто обфускация. Обратите внимание, что шифрование заголовков также используется для сокрытия эфемерных ключей X (в Session Request) и Y (в Session Created).

Смотрите раздел "Обработка входящих пакетов" ниже для получения дополнительных рекомендаций.

Байты 0-15 всех заголовков шифруются с использованием схемы защиты заголовков путем выполнения операции XOR с данными, вычисленными из известных ключей, используя ChaCha20, аналогично QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) и [Nonces](https://eprint.iacr.org/2019/624.pdf). Это гарантирует, что зашифрованный короткий заголовок и первая часть длинного заголовка будут выглядеть случайными.

For Session Request и Session Created байты 16-31 длинного заголовка и 32-байтовый эфемерный ключ Noise шифруются с использованием ChaCha20. Нешифрованные данные являются случайными, поэтому зашифрованные данные будут выглядеть случайными.

Для Retry байты 16-31 длинного заголовка шифруются с использованием ChaCha20. Нешифрованные данные являются случайными, поэтому зашифрованные данные будут выглядеть случайными.

В отличие от схемы защиты заголовков QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001), ВСЕ части всех заголовков, включая идентификаторы соединения назначения и источника, зашифрованы. QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) и [Nonces](https://eprint.iacr.org/2019/624.pdf) в первую очередь сосредоточены на шифровании "критической" части заголовка, т.е. номера пакета (nonce ChaCha20). Хотя шифрование идентификатора сессии делает классификацию входящих пакетов немного более сложной, это затрудняет некоторые атаки. QUIC определяет разные идентификаторы соединения для разных фаз, а также для проверки пути и миграции соединения. Здесь мы используем одни и те же идентификаторы соединения на протяжении всего процесса, поскольку они зашифрованы.

Существует семь фаз ключей защиты заголовка:

- Запрос сессии и запрос токена
- Сессия создана
- Повтор
- Сессия подтверждена
- Фаза данных
- Тест узла
- Пробивание отверстия

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_1</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_2</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Request KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Created KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice/Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See data phase KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 5,7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Hole Punch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
  </tbody>
</table>
Шифрование заголовков предназначено для быстрой классификации входящих пакетов без сложной эвристики или резервных методов. Это достигается использованием одного и того же ключа k_header_1 для почти всех входящих сообщений. Даже когда исходный IP или порт соединения изменяется из-за фактического изменения IP или поведения NAT, пакет может быть быстро сопоставлен с сессией с помощью единственного поиска по ID соединения.

Обратите внимание, что Session Created и Retry — это ЕДИНСТВЕННЫЕ сообщения, которые требуют резервной обработки для k_header_1 для расшифровки Connection ID, поскольку они используют intro key отправителя (Bob). ВСЕ остальные сообщения используют intro key получателя для k_header_1. Резервная обработка должна только искать ожидающие исходящие соединения по исходному IP/порту.

Если резервная обработка по исходному IP/порту не может найти ожидающее исходящее соединение, может быть несколько причин:

- Не SSU2 сообщение
- Поврежденное SSU2 сообщение
- Ответ подделан или изменен злоумышленником
- У Bob симметричный NAT
- Bob изменил IP или порт во время обработки сообщения
- Bob отправил ответ через другой интерфейс

Хотя возможна дополнительная резервная обработка для попытки найти ожидающее исходящее соединение и расшифровать идентификатор соединения с использованием k_header_1 для этого соединения, это, вероятно, не нужно. Если у Боба проблемы с NAT или маршрутизацией пакетов, вероятно, лучше позволить соединению завершиться неудачей. Данная схема полагается на то, что конечные точки сохраняют стабильный адрес в течение всего процесса установления соединения.

Смотрите раздел "Обработка входящих пакетов" ниже для дополнительных рекомендаций.

См. отдельные разделы KDF ниже для получения ключей шифрования заголовка для этой фазы.

#### KDF шифрования заголовка

```
// incoming encrypted packet

packet = incoming encrypted packet len = packet.length

    // take the next-to-last 12 bytes of the packet iv = packet[len-24:len-13] k_header_1 = header encryption key 1 data = {0, 0, 0, 0, 0, 0, 0, 0} mask = ChaCha20.encrypt(k_header_1, iv, data)

    // encrypt the first part of the header by XORing with the mask packet[0:7] \^= mask[0:7]

    // take the last 12 bytes of the packet iv = packet[len-12:len-1] k_header_2 = header encryption key 2 data = {0, 0, 0, 0, 0, 0, 0, 0} mask = ChaCha20.encrypt(k_header_2, iv, data)

    // encrypt the second part of the header by XORing with the mask packet[8:15] \^= mask[0:7]

    // For Session Request and Session Created only: iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

    // encrypt the third part of the header and the ephemeral key packet[16:63] = ChaCha20.encrypt(k_header_2, iv, packet[16:63])

    // For Retry, Token Request, Peer Test, and Hole Punch only: iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

    // encrypt the third part of the header packet[16:31] = ChaCha20.encrypt(k_header_2, iv, packet[16:31])
```
Данная KDF использует последние 24 байта пакета как IV для двух операций ChaCha20. Поскольку все пакеты заканчиваются 16-байтным MAC, это требует, чтобы все полезные нагрузки пакетов были минимум 8 байт. Это требование дополнительно документировано в разделах сообщений ниже.

#### Проверка заголовка

После расшифровки первых 8 байтов заголовка получатель узнает ID соединения назначения. Отсюда получатель знает, какой ключ шифрования заголовка использовать для остальной части заголовка, основываясь на фазе ключа сессии.

Расшифровка следующих 8 байт заголовка затем покажет тип сообщения и позволит определить, является ли заголовок коротким или длинным. Если это длинный заголовок, получатель должен проверить поля version и netid. Если version != 2, или netid != ожидаемому значению (обычно 2, за исключением тестовых сетей), получатель должен отбросить сообщение.

### Целостность пакетов

Все сообщения содержат три или четыре части:

- Заголовок сообщения
- Только для Session Request и Session Created, эфемерный ключ
- Полезная нагрузка, зашифрованная ChaCha20
- MAC Poly1305

Во всех случаях заголовок (и эфемерный ключ, если он присутствует) связывается с MAC аутентификации для обеспечения целостности всего сообщения.

- Для сообщений handshake Session Request, Session Created и Session Confirmed заголовок сообщения обрабатывается через mixHash() перед фазой обработки Noise
- Эфемерный ключ, если присутствует, покрывается стандартным Noise misHash()
- Для сообщений вне handshake Noise заголовок используется как Associated Data для шифрования ChaCha20/Poly1305.

Обработчики входящих пакетов должны всегда расшифровывать ChaCha20 payload и проверять MAC перед обработкой сообщения, за одним исключением: Для смягчения DoS-атак от пакетов с подделанными адресами, содержащих видимые сообщения Session Request с недействительным токеном, обработчику НЕ НУЖНО пытаться расшифровать и проверить полное сообщение (что требует дорогостоящей DH операции в дополнение к расшифровке ChaCha20/Poly1305). Обработчик может ответить сообщением Retry, используя значения, найденные в заголовке сообщения Session Request.

### Аутентифицированное шифрование

Существует три отдельных экземпляра аутентифицированного шифрования (CipherStates). Один во время фазы handshake, и два (передача и приём) для фазы данных. Каждый имеет свой собственный ключ из KDF.

Зашифрованные/аутентифицированные данные будут представлены как

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | Encrypted and authenticated data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+
```
#### ChaCha20/Poly1305

Формат зашифрованных и аутентифицированных данных.

Входные данные для функций шифрования/дешифрования:

```
k :: 32 byte cipher key, as generated from KDF


nonce :: Counter-based nonce, 12 bytes.

Starts at 0 and incremented for each message. First four bytes are always zero. Last eight bytes are the counter, little-endian encoded. Maximum value is 2**64 - 2. Connection must be dropped and restarted after it reaches that value. The value 2**64 - 1 must never be sent.

ad :: In handshake phase:

Associated data, 32 bytes. The SHA256 hash of all preceding data. In data phase: The packet header, 16 bytes.

data :: Plaintext data, 0 or more bytes
```
Выходные данные функции шифрования, входные данные функции расшифровки:

```
+----+----+----+----+----+----+----+----+

|                                       |

    + + | ChaCha20 encrypted data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | Poly1305 Message Authentication Code | + (MAC) + | 16 bytes | +----+----+----+----+----+----+----+----+

    encrypted data :: Same size as plaintext data, 0 - 65519 bytes

    MAC :: Poly1305 message authentication code, 16 bytes
```
Для ChaCha20 описанное здесь соответствует [RFC-7539](https://tools.ietf.org/html/rfc7539), который также аналогично используется в TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).

#### Примечания

- Поскольку ChaCha20 является потоковым шифром, открытые тексты не нуждаются в дополнении. Дополнительные байты потока ключей отбрасываются.
- Ключ для шифра (256 бит) согласовывается с помощью SHA256 KDF. Детали KDF для каждого сообщения приведены в отдельных разделах ниже.

#### Обработка ошибок AEAD

- Во всех сообщениях размер AEAD сообщения известен заранее. При сбое аутентификации AEAD получатель должен прекратить дальнейшую обработку сообщения и отбросить сообщение.
- Bob должен вести чёрный список IP-адресов с повторяющимися сбоями.

### KDF для Session Request

Функция выведения ключей (KDF) генерирует ключ шифра фазы handshake k из результата DH, используя HMAC-SHA256(key, data) как определено в [RFC-2104](https://tools.ietf.org/html/rfc2104). Это функции InitializeSymmetric(), MixHash() и MixKey(), точно как определено в спецификации Noise.

#### KDF для начального ChainKey

```
// Define protocol_name.


    Set protocol_name = "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256"

    :   (52 bytes, US-ASCII encoded, no NULL termination).

    // Define Hash h = 32 bytes h = SHA256(protocol_name);

    Define ck = 32 byte chaining key. Copy the h data to ck. Set ck = h

    // MixHash(null prologue) h = SHA256(h);

    // up until here, can all be precalculated by Alice for all outgoing connections

    // Bob's X25519 static keys // bpk is published in routerinfo bsk = GENERATE_PRIVATE() bpk = DERIVE_PUBLIC(bsk)

    // Bob static key // MixHash(bpk) // || below means append h = SHA256(h || bpk);

    // Bob introduction key // bik is published in routerinfo bik = RANDOM(32)

    // up until here, can all be precalculated by Bob for all incoming connections
```
#### KDF для запроса сессии

```
// MixHash(header)

h = SHA256(h || header)

    This is the "e" message pattern:

    // Alice's X25519 ephemeral keys aesk = GENERATE_PRIVATE() aepk = DERIVE_PUBLIC(aesk)

    // Alice ephemeral key X // MixHash(aepk) h = SHA256(h || aepk);

    // h is used as the associated data for the AEAD in Session Request // Retain the Hash h for the Session Created KDF

    End of "e" message pattern.

    This is the "es" message pattern:

    // DH(e, rs) == DH(s, re) sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

    // MixKey(DH()) //[chainKey, k] = MixKey(sharedSecret) // ChaChaPoly parameters to encrypt/decrypt keydata = HKDF(chainKey, sharedSecret, "", 64) chainKey = keydata[0:31]

    // AEAD parameters k = keydata[32:63] n = 0 ad = h ciphertext = ENCRYPT(k, n, payload, ad)

    // retain the chainKey for Session Created KDF

    End of "es" message pattern.

    // Header encryption keys for this message // bik = Bob's intro key k_header_1 = bik k_header_2 = bik

    // Header encryption keys for next message (Session Created) k_header_1 = bik k_header_2 = HKDF(chainKey, ZEROLEN, "SessCreateHeader", 32)

    // Header encryption keys for next message (Retry) k_header_1 = bik k_header_2 = bik
```
### SessionRequest (Тип 0)

Alice отправляет Bob, либо как первое сообщение в процессе установления соединения, либо в ответ на сообщение Retry. Bob отвечает сообщением Session Created. Размер: 80 + размер полезной нагрузки. Минимальный размер: 88

Если у Алисы нет действительного токена, Алиса должна отправить сообщение Token Request вместо Session Request, чтобы избежать накладных расходов асимметричного шифрования при генерации Session Request.

Длинный заголовок. Содержимое Noise: эфемерный ключ Алисы X Полезная нагрузка Noise: DateTime и другие блоки Максимальный размер полезной нагрузки: MTU - 108 (IPv4) или MTU - 128 (IPv6). Для MTU 1280: Максимальная полезная нагрузка составляет 1172 (IPv4) или 1152 (IPv6). Для MTU 1500: Максимальная полезная нагрузка составляет 1392 (IPv4) или 1372 (IPv6).

Свойства безопасности полезной нагрузки:

```
XK(s, rs): Authentication Confidentiality

-> e, es 0 2

    Authentication: None (0). This payload may have been sent by any party, including an active attacker.

    Confidentiality: 2. Encryption to a known recipient, forward secrecy for sender compromise only, vulnerable to replay. This payload is encrypted based only on DHs involving the recipient's static key pair. If the recipient's static private key is compromised, even at a later date, this payload can be decrypted. This message can also be replayed, since there's no ephemeral contribution from the recipient.

    "e": Alice generates a new ephemeral key pair and stores it in the e

    :   variable, writes the ephemeral public key as cleartext into the message buffer, and hashes the public key along with the old h to derive a new h.

    "es": A DH is performed between the Alice's ephemeral key pair and the

    :   Bob's static key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Значение X шифруется для обеспечения неразличимости и уникальности полезной нагрузки, что является необходимыми мерами противодействия DPI. Для этого мы используем шифрование ChaCha20, а не более сложные и медленные альтернативы, такие как elligator2. Асимметричное шифрование с использованием публичного ключа router'а Боба было бы слишком медленным. Шифрование ChaCha20 использует intro key Боба, опубликованный в netDb.

Шифрование ChaCha20 предназначено только для защиты от DPI. Любая сторона, знающая ключ представления Боба, который опубликован в сетевой базе данных, может расшифровать заголовок и значение X в этом сообщении.

Необработанное содержимое:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Bob intro key + | See Header Encryption KDF | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Bob intro key n=0 + | | +----+----+----+----+----+----+----+----+ | | + X, ChaCha20 encrypted + | with Bob intro key n=0 | + (32 bytes) + | | + + | | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | k defined in KDF for Session Request | + n = 0 + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+

    X :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian

    :   key: Bob's intro key n: 1 data: 48 bytes (bytes 16-31 of the header, followed by encrypted X)
```
Незашифрованные данные (тег аутентификации Poly1305 не показан):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-----------------------------------------------+-----------+-----------+-----------+-----------+
    | > Packet Number                               | type      | ver       | id        | flag      |
    +-----------------------------------------------+-----------+-----------+-----------+-----------+
    | > Source Connection ID                                                                        |
    +-----------------------------------------------------------------------------------------------+
    | > Token                                                                                       |
    +-----------------------------------------------------------------------------------------------+
    | > X (32 bytes)                                                                                |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    +-----------------------------------------------------------------------------------------------+
    | >                                                                                             |
    | >                                                                                             |
    | > Noise payload (block data)                                                                  |
    | >                                                                                             |
    | > :   (length varies)                                                                         |
    | >                                                                                             |
    | > see below for allowed blocks                                                                |
    |                                                                                               |
    |                                                                                               |
    +-----------------------------------------------------------------------------------------------+

    Destination Connection ID :: Randomly generated by Alice

    id :: 1 byte, the network ID (currently 2, except for test networks)

    ver :: 2

    type :: 0

    flag :: 1 byte, unused, set to 0 for future compatibility

    Packet Number :: Random 4 byte number generated by Alice, ignored

    Source Connection ID :: Randomly generated by Alice,

    :   must not be equal to Destination Connection ID

    Token :: 0 if not previously received from Bob

    X :: 32 bytes, X25519 ephemeral key, little endian
```
#### Полезная нагрузка

- Блок DateTime
- Блок Options (опциональный)
- Блок Relay Tag Request (опциональный)
- Блок Padding (опциональный)

Минимальный размер полезной нагрузки составляет 8 байт. Поскольку блок DateTime составляет всего 7 байт, должен присутствовать как минимум один другой блок.

#### Примечания

- Уникальное значение X в начальном блоке ChaCha20 гарантирует, что шифротекст будет разным для каждой сессии.
- Для обеспечения устойчивости к зондированию, Bob не должен отправлять сообщение Retry в ответ на сообщение Session Request, если только поля типа сообщения, версии протокола и network ID в сообщении Session Request не являются валидными.
- Bob должен отклонять соединения, где значение timestamp слишком сильно отклоняется от текущего времени. Назовем максимальную разность времени "D". Bob должен поддерживать локальный кэш ранее использованных значений handshake и отклонять дубликаты для предотвращения replay-атак. Значения в кэше должны иметь время жизни не менее 2*D. Значения кэша зависят от реализации, однако может использоваться 32-байтное значение X (или его зашифрованный эквивалент). Отклонять отправкой сообщения Retry, содержащего нулевой токен и блок завершения.
- Эфемерные ключи Diffie-Hellman никогда не должны использоваться повторно для предотвращения криптографических атак, и повторное использование будет отклонено как replay-атака.
- Опции "KE" и "auth" должны быть совместимы, т.е. общий секрет K должен иметь соответствующий размер. Если будут добавлены дополнительные опции "auth", это может неявно изменить значение флага "KE" для использования другой KDF или другого размера усечения.
- Bob должен проверить, что эфемерный ключ Alice является валидной точкой на кривой.
- Padding должен быть ограничен разумным объемом. Bob может отклонять соединения с избыточным padding. Bob укажет свои опции padding в Session Created. Рекомендации min/max TBD. Случайный размер от 0 до 31 байт минимум? (Распределение будет определено, см. Приложение A.)
- При большинстве ошибок, включая AEAD, DH, очевидный replay или сбой валидации ключа, Bob должен остановить дальнейшую обработку сообщения и отбросить сообщение без ответа.
- Bob МОЖЕТ отправить сообщение Retry, содержащее нулевой токен и блок Termination с кодом причины clock skew, если timestamp в блоке DateTime слишком сильно смещен.
- Предотвращение DoS: DH является относительно дорогой операцией. Как и с предыдущим протоколом NTCP, router должны принимать все необходимые меры для предотвращения истощения CPU или соединений. Устанавливать ограничения на максимальное количество активных соединений и максимальное количество настроек соединений в процессе. Применять таймауты чтения (как на операцию чтения, так и общий для "slowloris"). Ограничивать повторяющиеся или одновременные соединения от одного источника. Поддерживать черные списки для источников, которые постоянно терпят неудачу. Не отвечать на сбой AEAD. Альтернативно, отвечать сообщением Retry до операции DH и валидации AEAD.
- Поле "ver": Общий протокол Noise, расширения и протокол SSU2, включая спецификации полезной нагрузки, указывающие SSU2. Это поле может использоваться для указания поддержки будущих изменений.
- Поле network ID используется для быстрого выявления межсетевых соединений. Если это поле не соответствует network ID Bob, Bob должен отключиться и заблокировать будущие соединения.
- Bob должен отбросить сообщение, если Source Connection ID равен Destination Connection ID.

### KDF для Session Created и Session Confirmed часть 1

```
// take h saved from Session Request KDF

// MixHash(ciphertext) h = SHA256(h || encrypted Noise payload from Session Request)

    // MixHash(header) h = SHA256(h || header)

    This is the "e" message pattern:

    // Bob's X25519 ephemeral keys besk = GENERATE_PRIVATE() bepk = DERIVE_PUBLIC(besk)

    // h is from KDF for Session Request // Bob ephemeral key Y // MixHash(bepk) h = SHA256(h || bepk);

    // h is used as the associated data for the AEAD in Session Created // Retain the Hash h for the Session Confirmed KDF

    End of "e" message pattern.

    This is the "ee" message pattern:

    // MixKey(DH()) //[chainKey, k] = MixKey(sharedSecret) sharedSecret = DH(aesk, bepk) = DH(besk, aepk) keydata = HKDF(chainKey, sharedSecret, "", 64) chainKey = keydata[0:31]

    // AEAD parameters k = keydata[32:63] n = 0 ad = h ciphertext = ENCRYPT(k, n, payload, ad)

    // retain the chaining key ck for Session Confirmed KDF

    End of "ee" message pattern.

    // Header encryption keys for this message // bik = Bob's intro key k_header_1 = bik k_header_2: See Session Request KDF above

    // Header protection keys for next message (Session Confirmed) k_header_1 = bik k_header_2 = HKDF(chainKey, ZEROLEN, "SessionConfirmed", 32)
```
### SessionCreated (Тип 1)

Bob отправляет Alice в ответ на сообщение Session Request. Alice отвечает сообщением Session Confirmed. Размер: 80 + размер полезной нагрузки. Минимальный размер: 88

Содержимое Noise: эфемерный ключ Bob'а Y Полезная нагрузка Noise: DateTime, Address и другие блоки Максимальный размер полезной нагрузки: MTU - 108 (IPv4) или MTU - 128 (IPv6). Для MTU 1280: Максимальная полезная нагрузка составляет 1172 (IPv4) или 1152 (IPv6). Для MTU 1500: Максимальная полезная нагрузка составляет 1392 (IPv4) или 1372 (IPv6).

Свойства безопасности полезной нагрузки:

```
XK(s, rs): Authentication Confidentiality

<- e, ee 2 1

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 1. Encryption to an ephemeral recipient. This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee"). However, the sender has not authenticated the recipient, so this payload might be sent to any party, including an active attacker.

    "e": Bob generates a new ephemeral key pair and stores it in the e variable, writes the ephemeral public key as cleartext into the message buffer, and hashes the public key along with the old h to derive a new h.

    "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Значение Y зашифровано для обеспечения неразличимости и уникальности полезной нагрузки, что является необходимыми мерами противодействия DPI. Мы используем шифрование ChaCha20 для достижения этой цели, а не более сложные и медленные альтернативы, такие как elligator2. Асимметричное шифрование с использованием публичного ключа router Алисы было бы слишком медленным. Шифрование ChaCha20 использует intro ключ Боба, опубликованный в netDb.

Шифрование ChaCha20 предназначено только для противодействия DPI. Любая сторона, знающая ключ введения Боба, который публикуется в базе данных сети, и перехватившая первые 32 байта Session Request, может расшифровать значение Y в этом сообщении.

Исходное содержимое:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Bob intro key and + | derived key, see Header Encryption KDF| +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with derived key n=0 + | See Header Encryption KDF | +----+----+----+----+----+----+----+----+ | | + Y, ChaCha20 encrypted + | with derived key n=0 | + (32 bytes) + | See Header Encryption KDF | + + | | +----+----+----+----+----+----+----+----+ | ChaCha20 data | + Encrypted and authenticated data + | length varies | + k defined in KDF for Session Created + | n = 0; see KDF for associated data | + + | | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+

    Y :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian

    :   key: Bob's intro key n: 1 data: 48 bytes (bytes 16-31 of the header, followed by encrypted Y)
```
Незашифрованные данные (тег аутентификации Poly1305 не показан):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-------------------------------------------+----------+----------+----------+----------+
    | > Packet Number                           | type     | ver      | id       | flag     |
    +-------------------------------------------+----------+----------+----------+----------+
    | > Source Connection ID                                                                |
    +---------------------------------------------------------------------------------------+
    | > Token                                                                               |
    +---------------------------------------------------------------------------------------+
    | > Y (32 bytes)                                                                        |
    |                                                                                       |
    |                                                                                       |
    |                                                                                       |
    |                                                                                       |
    |                                                                                       |
    |                                                                                       |
    +---------------------------------------------------------------------------------------+
    | >                                                                                     |
    | >                                                                                     |
    | > Noise payload (block data)                                                          |
    | >                                                                                     |
    | > :   (length varies) see below for allowed blocks                                    |
    |                                                                                       |
    |                                                                                       |
    +---------------------------------------------------------------------------------------+

    Destination Connection ID :: The Source Connection ID

    :   received from Alice in Session Request

    id :: 1 byte, the network ID (currently 2, except for test networks)

    ver :: 2

    type :: 0

    flag :: 1 byte, unused, set to 0 for future compatibility

    Packet Number :: Random 4 byte number generated by Bob, ignored

    Source Connection ID :: The Destination Connection ID

    :   received from Alice in Session Request

    Token :: 0 (unused)

    Y :: 32 bytes, X25519 ephemeral key, little endian
```
#### Полезная нагрузка

- Блок DateTime
- Блок Address
- Блок Relay Tag (необязательный)
- Блок New Token (не рекомендуется, см. примечание)
- Блок First Packet Number (необязательный)
- Блок Options (необязательный)
- Блок Termination (не рекомендуется, отправляйте в retry сообщении)
- Блок Padding (необязательный)

Минимальный размер полезной нагрузки составляет 8 байт. Поскольку блоки DateTime и Address в сумме превышают это значение, требование выполняется только этими двумя блоками.

#### Примечания

- Алиса должна проверить, что эфемерный ключ Боба является действительной точкой на кривой.
- Дополнение должно быть ограничено разумным количеством. Алиса может отклонить соединения с избыточным дополнением. Алиса укажет свои параметры дополнения в Session Confirmed. Рекомендации по мин./макс. значениям будут определены позже. Случайный размер от 0 до 31 байта минимум? (Распределение будет определено, см. Приложение A.)
- При любой ошибке, включая AEAD, DH, метку времени, возможную повторную атаку или ошибку проверки ключа, Алиса должна прекратить дальнейшую обработку сообщений и закрыть соединение без ответа.
- Алиса должна отклонить соединения, где значение метки времени слишком сильно отличается от текущего времени. Назовем максимальную дельту времени "D". Алиса должна поддерживать локальный кэш ранее использованных значений handshake и отклонять дубликаты, чтобы предотвратить атаки повтора. Значения в кэше должны иметь время жизни не менее 2*D. Значения кэша зависят от реализации, однако может использоваться 32-байтовое значение Y (или его зашифрованный эквивалент).
- Алиса должна отбросить сообщение, если исходный IP и порт не совпадают с IP назначения и портом Session Request.
- Алиса должна отбросить сообщение, если ID соединения назначения и источника не совпадают с ID соединения источника и назначения Session Request.
- Боб отправляет блок relay tag, если это запрошено Алисой в Session Request.
- Блок New Token не рекомендуется в Session Created, поскольку Боб должен сначала выполнить проверку Session Confirmed. См. раздел Tokens ниже.

#### Проблемы

- Включить сюда опции минимального/максимального заполнения?

### KDF для Session Confirmed части 1, используя Session Created KDF

```
// take h saved from Session Created KDF

// MixHash(ciphertext) h = SHA256(h || encrypted Noise payload from Session Created)

    // MixHash(header) h = SHA256(h || header) // h is used as the associated data for the AEAD in Session Confirmed part 1, below

    This is the "s" message pattern:

    // Alice's X25519 static keys ask = GENERATE_PRIVATE() apk = DERIVE_PUBLIC(ask)

    // AEAD parameters // k is from Session Request n = 1 ad = h ciphertext = ENCRYPT(k, n++, apk, ad)

    // MixHash(ciphertext) h = SHA256(h || ciphertext);

    // h is used as the associated data for the AEAD in Session Confirmed part 2

    End of "s" message pattern.

    // Header encryption keys for this message See Session Confirmed part 2 below
```
### KDF для Session Confirmed часть 2

```
This is the "se" message pattern:

// DH(ask, bepk) == DH(besk, apk) sharedSecret = DH(ask, bepk) = DH(besk, apk)

// MixKey(DH()) //[chainKey, k] = MixKey(sharedSecret) keydata = HKDF(chainKey, sharedSecret, "", 64) chainKey = keydata[0:31]

// AEAD parameters k = keydata[32:63] n = 0 ad = h ciphertext = ENCRYPT(k, n, payload, ad)

// h from Session Confirmed part 1 is used as the associated data for the AEAD in Session Confirmed part 2 // MixHash(ciphertext) h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF // retain the hash h for the data phase KDF

End of "se" message pattern.

// Header encryption keys for this message // bik = Bob's intro key k_header_1 = bik k_header_2: See Session Created KDF above

// Header protection keys for data phase See data phase KDF below
```
### SessionConfirmed (Тип 2)

Alice отправляет Bob в ответ на сообщение Session Created. Bob немедленно отвечает сообщением Data, содержащим блок ACK. Размер: 80 + размер полезной нагрузки. Минимальный размер: Около 500 (минимальный размер блока router info составляет около 420 байт)

Содержимое Noise: статический ключ Alice Полезная нагрузка Noise часть 1: Нет Полезная нагрузка Noise часть 2: RouterInfo Alice и другие блоки Максимальный размер полезной нагрузки: MTU - 108 (IPv4) или MTU - 128 (IPv6). Для MTU 1280: Максимальная полезная нагрузка составляет 1172 (IPv4) или 1152 (IPv6). Для MTU 1500: Максимальная полезная нагрузка составляет 1392 (IPv4) или 1372 (IPv6).

Свойства безопасности полезной нагрузки:

```
XK(s, rs): Authentication Confidentiality

-> s, se 2 5

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 5. Encryption to a known recipient, strong forward secrecy. This payload is encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static DH with the recipient's static key pair. Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated by an attacker that has stolen its static private key, this payload cannot be decrypted.

    "s": Alice writes her static public key from the s variable into the message buffer, encrypting it, and hashes the output along with the old h to derive a new h.

    "se": A DH is performed between the Alice's static key pair and the Bob's ephemeral key pair. The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Это содержит два ChaChaPoly фрейма. Первый — это зашифрованный статический открытый ключ Alice. Второй — это Noise полезная нагрузка: зашифрованная RouterInfo Alice, опциональные параметры и опциональное заполнение. Они используют разные ключи, поскольку между ними вызывается функция MixKey().

Исходное содержимое:

```
+----+----+----+----+----+----+----+----+

|  Short Header 16 bytes, ChaCha20 |

    + encrypted with Bob intro key and + | derived key, see Header Encryption KDF| +----+----+----+----+----+----+----+----+ | ChaCha20 frame (32 bytes) | + Encrypted and authenticated data + + Alice static key S + | k defined in KDF for Session Created | + n = 1 + | | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+ | | + Length varies (remainder of packet) + | | + ChaChaPoly frame + | Encrypted and authenticated | + see below for allowed blocks + | | + k defined in KDF for + | Session Confirmed part 2 | + n = 0 + | see KDF for associated data | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+

    S :: 32 bytes, ChaChaPoly encrypted Alice's X25519 static key, little endian

    :   inside 48 byte ChaChaPoly frame
```
Незашифрованные данные (теги аутентификации Poly1305 не показаны):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+-------------------------+
    | > Packet Number                                   | type       | frag       | > flags                 |
    +---------------------------------------------------+------------+------------+-------------------------+
    | > S Alice static key (32 bytes)                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    Destination Connection ID :: As sent in Session Request,

    :   or one received in Session Confirmed?

    Packet Number :: 0 always, for all fragments, even if retransmitted

    type :: 2

    frag :: 1 byte fragment info:

    :   bit order: 76543210 (bit 7 is MSB) bits 7-4: fragment number 0-14, big endian bits 3-0: total fragments 1-15, big endian

    flags :: 2 bytes, unused, set to 0 for future compatibility

    S :: 32 bytes, Alice's X25519 static key, little endian
```
#### Полезная нагрузка

- Блок RouterInfo (должен быть первым блоком)
- Блок Options (опционально)
- Блок New Token (опционально)
- Блок Relay Request (опционально)
- Блок Peer Test (опционально)
- Блок First Packet Number (опционально)
- Блоки I2NP, First Fragment или Follow-on Fragment (опционально, но вероятно нет места)
- Блок Padding (опционально)

Минимальный размер полезной нагрузки составляет 8 байт. Поскольку блок RouterInfo будет значительно больше этого значения, требование выполняется только с этим блоком.

#### Заметки

- Боб должен выполнить обычную проверку Router Info. Убедиться, что тип подписи поддерживается, проверить подпись, проверить, что временная метка находится в допустимых пределах, и выполнить любые другие необходимые проверки. См. ниже примечания по обработке фрагментированных Router Info.

- Боб должен проверить, что статический ключ Алисы, полученный в первом кадре, соответствует статическому ключу в Router Info. Боб должен сначала найти в Router Info адрес NTCP или SSU2 router с совпадающей опцией версии (v). См. разделы "Опубликованная Router Info" и "Неопубликованная Router Info" ниже. См. ниже примечания по обработке фрагментированных Router Info.

- Если у Боба есть более старая версия RouterInfo Алисы в его netdb, проверить, что статический ключ в информации роутера одинаков в обеих версиях, если присутствует, и если более старая версия меньше чем XXX старая (см. время ротации ключей ниже)

- Боб должен проверить, что статический ключ Алисы является допустимой точкой на кривой здесь.

- Должны быть включены опции для указания параметров заполнения.

- При любой ошибке, включая сбой AEAD, RI, DH, временной метки или проверки ключа, Боб должен прекратить дальнейшую обработку сообщений и закрыть соединение без ответа.

- Содержимое фрейма части 2 сообщения 3: Формат этого фрейма такой же, как формат фреймов фазы данных, за исключением того, что длина фрейма отправляется Алисой в Session Request. См. ниже формат фрейма фазы данных. Фрейм должен содержать от 1 до 4 блоков в следующем порядке:

1)  Блок Router Info Алисы (обязательный)   2)  Блок опций (необязательный)   3)  Блоки I2NP (необязательные)

4\) Блок заполнения (необязательный) Этот фрейм никогда не должен содержать блоки других типов. TODO: что насчет relay и peer test?

- Рекомендуется блок заполнения для части 2 сообщения 3.

- Может не быть места или быть только небольшое количество места для блоков I2NP, в зависимости от MTU и размера Router Info. НЕ включайте блоки I2NP, если Router Info фрагментирован. Простейшая реализация может заключаться в том, чтобы никогда не включать блоки I2NP в сообщение Session Confirmed и отправлять все блоки I2NP в последующих сообщениях Data. См. раздел блока Router Info ниже для максимального размера блока.

#### Фрагментация подтвержденной сессии

Сообщение Session Confirmed должно содержать полную подписанную информацию Router Info от Алисы, чтобы Боб мог выполнить несколько необходимых проверок:

- Статический ключ "s" в RI соответствует статическому ключу в рукопожатии
- Ключ представления "i" в RI должен быть извлечен и действителен для использования в фазе данных
- Подпись RI действительна

К сожалению, Router Info, даже при сжатии gzip в блоке RI, может превышать MTU. Поэтому Session Confirmed может быть фрагментирована на два или более пакетов. Это ЕДИНСТВЕННЫЙ случай в протоколе SSU2, когда полезная нагрузка, защищенная AEAD, фрагментируется на два или более пакетов.

Заголовки для каждого пакета создаются следующим образом:

- ВСЕ заголовки являются короткими заголовками с одинаковым номером пакета 0
- ВСЕ заголовки содержат поле "frag" с номером фрагмента и общим количеством фрагментов
- Незашифрованный заголовок фрагмента 0 является ассоциированными данными (AD) для "jumbo" сообщения
- Каждый заголовок шифруется с использованием последних 24 байт данных в ЭТОМ пакете

Составьте серию пакетов следующим образом:

- Создать единый блок RI (фрагмент 0 из 1 в поле frag блока RI). Мы не используем фрагментацию блока RI, это было для альтернативного метода решения той же задачи.
- Создать "джамбо" полезную нагрузку с блоком RI и любыми другими блоками, которые должны быть включены
- Вычислить общий размер данных (не включая заголовок), который равен размеру полезной нагрузки + 64 байта для статического ключа и двух MAC
- Вычислить доступное пространство в каждом пакете, которое равно MTU минус заголовок IP (20 или 40), минус заголовок UDP (8), минус короткий заголовок SSU2 (16). Общие накладные расходы на пакет составляют 44 (IPv4) или 64 (IPv6).
- Вычислить количество пакетов.
- Вычислить размер данных в последнем пакете. Он должен быть больше или равен 24 байтам, чтобы шифрование заголовка работало. Если он слишком мал, либо добавить блок дополнения, ЛИБО увеличить размер блока дополнения, если он уже присутствует, ЛИБО уменьшить размер одного из других пакетов, чтобы последний пакет был достаточно большим.
- Создать незашифрованный заголовок для первого пакета с общим количеством фрагментов в поле frag и зашифровать "джамбо" полезную нагрузку с помощью Noise, используя заголовок как AD, как обычно.
- Разделить зашифрованный джамбо пакет на фрагменты
- Добавить незашифрованный заголовок для каждого фрагмента 1-n
- Зашифровать заголовок для каждого фрагмента 0-n. Каждый заголовок использует ТЕ ЖЕ k_header_1 и k_header_2, как определено выше в KDF Session Confirmed.
- Передать все фрагменты

Процесс пересборки:

Когда Боб получает любое сообщение Session Confirmed, он расшифровывает заголовок, проверяет поле frag и определяет, что Session Confirmed фрагментировано. Он не расшифровывает (и не может расшифровать) сообщение до тех пор, пока все фрагменты не будут получены и собраны заново.

- Сохранить заголовок для фрагмента 0, поскольку он используется как Noise AD
- Отбросить заголовки для других фрагментов перед повторной сборкой
- Собрать "jumbo" полезную нагрузку с заголовком для фрагмента 0 как AD и расшифровать с помощью Noise
- Проверить блок RI как обычно
- Перейти к фазе данных и отправить ACK 0, как обычно

У Bob нет механизма для подтверждения отдельных фрагментов. Когда Bob получает все фрагменты, собирает их, расшифровывает и проверяет содержимое, Bob выполняет split() как обычно, входит в фазу данных и отправляет ACK для пакета номер 0.

Если Алиса не получает ACK для пакета номер 0, она должна повторно передать все подтвержденные пакеты сессии как есть.

Примеры:

Для MTU 1500 по IPv6 максимальная полезная нагрузка составляет 1372, накладные расходы блока RI составляют 5, максимальный размер данных RI (сжатых gzip) составляет 1367 (при отсутствии других блоков). С двумя пакетами накладные расходы второго пакета составляют 64, поэтому он может содержать еще 1436 байт полезной нагрузки. Таким образом, двух пакетов достаточно для сжатого RI размером до 2803 байт.

Самый большой сжатый RI, наблюдаемый в текущей сети, составляет около 1400 байт; поэтому на практике двух фрагментов должно быть достаточно, даже при минимальном MTU 1280. Протокол позволяет максимум 15 фрагментов.

Анализ безопасности:

Целостность и безопасность фрагментированного Session Confirmed такая же, как у нефрагментированного. Любое изменение любого фрагмента приведет к сбою Noise AEAD после повторной сборки. Заголовки фрагментов после фрагмента 0 используются только для идентификации фрагмента. Даже если атакующий на пути передачи имел бы ключ k_header_2, используемый для шифрования заголовка (что маловероятно, поскольку он выводится из рукопожатия), это не позволило бы атакующему подставить действительный фрагмент.

### KDF для фазы данных

Фаза данных использует заголовок для связанных данных.

KDF генерирует два ключа шифрования k_ab и k_ba из цепочечного ключа ck, используя HMAC-SHA256(key, data), как определено в [RFC-2104](https://tools.ietf.org/html/rfc2104). Это функция split(), точно как определено в спецификации Noise.

```
// split()

// chainKey = from handshake phase keydata = HKDF(chainKey, ZEROLEN, "", 64) k_ab = keydata[0:31] k_ba = keydata[32:63]

    // key is k_ab for Alice to Bob // key is k_ba for Bob to Alice

    keydata = HKDF(key, ZEROLEN, "HKDFSSU2DataKeys", 64) k_data = keydata[0:31] k_header_2 = keydata[32:63]

    // AEAD parameters k = k_data n = 4 byte packet number from header ad = 16 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for data phase // aik = Alice's intro key // bik = Bob's intro key k_header_1 = Receiver's intro key (aik or bik) k_header_2: from above
```
### Сообщение с данными (Тип 6)

Noise payload: Все типы блоков разрешены Максимальный размер payload: MTU - 60 (IPv4) или MTU - 80 (IPv6). Для MTU 1500: Максимальный payload составляет 1440 (IPv4) или 1420 (IPv6).

Начиная со второй части Session Confirmed, все сообщения находятся внутри аутентифицированной и зашифрованной полезной нагрузки ChaChaPoly. Все заполнение находится внутри сообщения. Внутри полезной нагрузки используется стандартный формат с нулем или более "блоками". Каждый блок имеет однобайтовый тип и двухбайтовую длину. Типы включают дату/время, I2NP сообщение, опции, завершение и заполнение.

Примечание: Боб может, но не обязан, отправить свою RouterInfo Алисе в качестве первого сообщения на этапе передачи данных.

Свойства безопасности полезной нагрузки:

```
XK(s, rs): Authentication Confidentiality

<- 2 5 -> 2 5

    Authentication: 2. Sender authentication resistant to key-compromise impersonation (KCI). The sender authentication is based on an ephemeral-static DH ("es" or "se") between the sender's static key pair and the recipient's ephemeral key pair. Assuming the corresponding private keys are secure, this authentication cannot be forged.

    Confidentiality: 5. Encryption to a known recipient, strong forward secrecy. This payload is encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static DH with the recipient's static key pair. Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### Примечания

- Router должен отбросить сообщение с ошибкой AEAD.

```
+----+----+----+----+----+----+----+----+

|  Short Header 16 bytes, ChaCha20 |

    + encrypted with intro key and + | derived key, see Data Phase KDF | +----+----+----+----+----+----+----+----+ | ChaCha20 data | + Encrypted and authenticated data + | length varies | + k defined in Data Phase KDF + | n = packet number from header | + + | | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
Незашифрованные данные (тег аутентификации Poly1305 не показан):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +-------------------------------------------+----------+--------------------------------+
    | > Packet Number                           | type     | > flags                        |
    +-------------------------------------------+----------+--------------------------------+
    | >                                                                                     |
    | >                                                                                     |
    | > Noise payload (block data)                                                          |
    | >                                                                                     |
    | > :   (length varies)                                                                 |
    |                                                                                       |
    |                                                                                       |
    +---------------------------------------------------------------------------------------+

    Destination Connection ID :: As specified in session setup

    Packet Number :: 4 byte big endian integer

    type :: 6

    flags :: 3 bytes, unused, set to 0 for future compatibility
```
#### Примечания

- Минимальный размер полезной нагрузки составляет 8 байт. Это требование будет выполнено любым блоком ACK, I2NP, First Fragment или Follow-on Fragment. Если требование не выполняется, должен быть включен блок Padding.
- Каждый номер пакета может использоваться только один раз. При повторной передаче I2NP сообщений или фрагментов должен использоваться новый номер пакета.

### KDF для тестирования узлов

```
// AEAD parameters

// bik = Bob's intro key k = bik n = 4 byte packet number from header ad = 32 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for this message k_header_1 = bik k_header_2 = bik
```
### Тест пира (Тип 7)

Чарли отправляет Алисе, а Алиса отправляет Чарли, только для фаз 5-7 Peer Test. Фазы 1-4 Peer Test должны отправляться в рамках сессии с использованием блока Peer Test в сообщении Data. См. разделы "Блок Peer Test" и "Процесс Peer Test" ниже для получения дополнительной информации.

Размер: 48 + размер полезной нагрузки.

Полезная нагрузка Noise: См. ниже.

Необработанное содержимое:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Alice or Charlie + | intro key | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Alice or Charlie + | intro key | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | | + see KDF for key and n + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
Незашифрованные данные (тег аутентификации Poly1305 не показан):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+------------+------------+
    | > Packet Number                                   | type       | ver        | id         | flag       |
    +---------------------------------------------------+------------+------------+------------+------------+
    | > Source Connection ID                                                                                |
    +-------------------------------------------------------------------------------------------------------+
    | > Token                                                                                               |
    +-------------------------------------------------------------------------------------------------------+
    | >                                                                                                     |
    | >                                                                                                     |
    | > ChaCha20 payload (block data)                                                                       |
    | >                                                                                                     |
    | > :   (length varies)                                                                                 |
    | >                                                                                                     |
    | > see below for allowed blocks                                                                        |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    Destination Connection ID :: See below

    type :: 7

    ver :: 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Packet Number :: Random number generated by Alice or Charlie

    Source Connection ID :: See below

    Token :: Randomly generated by Alice or Charlie, ignored
```
#### Полезная нагрузка

- Блок DateTime
- Блок Address (обязателен для сообщений 6 и 7, см. примечание ниже)
- Блок Peer Test
- Блок Padding (необязательный)

Минимальный размер полезной нагрузки составляет 8 байт. Поскольку блок Peer Test в сумме превышает это значение, требование выполняется только с этим блоком.

В сообщениях 5 и 7 блок Peer Test может быть идентичен блоку из внутрисессионных сообщений 3 и 4, содержащему соглашение, подписанное Чарли, или может быть перегенерирован. Подпись необязательна.

В сообщении 6 блок Peer Test может быть идентичен блоку из внутрисессионных сообщений 1 и 2, содержащему запрос, подписанный Алисой, или может быть сгенерирован заново. Подпись необязательна.

Идентификаторы соединения: Два идентификатора соединения выводятся из тестового nonce. Для сообщений 5 и 7, отправляемых от Чарли к Алисе, идентификатор соединения назначения представляет собой две копии 4-байтного тестового nonce в формате big-endian, то есть ((nonce << 32) | nonce). Идентификатор соединения источника является инверсией идентификатора соединения назначения, то есть ~((nonce << 32) | nonce). Для сообщения 6, отправляемого от Алисы к Чарли, поменяйте местами два идентификатора соединения.

Содержимое блока адреса:

- В сообщении 5: Не требуется.
- В сообщении 6: IP и порт Чарли, выбранные из RI Чарли.
- В сообщении 7: Фактические IP и порт Алисы, с которых было получено сообщение 6.

### KDF для повторной попытки

Требование к сообщению Retry заключается в том, что Bob не обязан расшифровывать сообщение Session Request для генерации сообщения Retry в ответ. Также это сообщение должно быстро генерироваться, используя только симметричное шифрование.

```
// AEAD parameters

// bik = Bob's intro key k = bik n = 4 byte packet number from header ad = 32 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for this message k_header_1 = bik k_header_2 = bik
```
### Повтор (Тип 9)

Bob отправляет Alice в ответ на сообщение Session Request или Token Request. Alice отвечает новым Session Request. Размер: 48 + размер полезной нагрузки.

Также служит как сообщение завершения (т.е. "Не повторять"), если включен блок завершения.

Noise payload: См. ниже.

Необработанное содержимое:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Bob intro key + | | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Bob intro key + | | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | | + see KDF for key and n + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
Незашифрованные данные (тег аутентификации Poly1305 не показан):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+------------+------------+
    | > Packet Number                                   | type       | ver        | id         | flag       |
    +---------------------------------------------------+------------+------------+------------+------------+
    | > Source Connection ID                                                                                |
    +-------------------------------------------------------------------------------------------------------+
    | > Token                                                                                               |
    +-------------------------------------------------------------------------------------------------------+
    | >                                                                                                     |
    | >                                                                                                     |
    | > ChaCha20 payload (block data)                                                                       |
    | >                                                                                                     |
    | > :   (length varies)                                                                                 |
    | >                                                                                                     |
    | > see below for allowed blocks                                                                        |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    Destination Connection ID :: The Source Connection ID

    :   received from Alice in Token Request or Session Request

    Packet Number :: Random number generated by Bob

    type :: 9

    ver :: 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Source Connection ID :: The Destination Connection ID

    :   received from Alice in Token Request or Session Request

    Token :: 8 byte unsigned integer, randomly generated by Bob, nonzero,

    :   or zero if session is rejected and a termination block is included
```
#### Полезная нагрузка

- Блок DateTime
- Блок Address
- Блок Options (опциональный)
- Блок Termination (опциональный, если сессия отклонена)
- Блок Padding (опциональный)

Минимальный размер полезной нагрузки составляет 8 байт. Поскольку блоки DateTime и Address в сумме превышают это значение, требование выполняется только с этими двумя блоками.

#### Примечания

- Для обеспечения устойчивости к зондированию router не должен отправлять сообщение Retry в ответ на сообщение Session Request или Token Request, если поля типа сообщения, версии протокола и ID сети в сообщении Request недействительны.
- Чтобы ограничить масштаб любой атаки усиления, которая может быть осуществлена с использованием поддельных адресов отправителей, сообщение Retry не должно содержать большого количества заполнителей. Рекомендуется, чтобы сообщение Retry было не более чем в три раза больше размера сообщения, на которое оно отвечает. В качестве альтернативы используйте простой метод, такой как добавление случайного количества заполнителей в диапазоне 1-64 байта.

### KDF для запроса токена

Это сообщение должно генерироваться быстро, используя только симметричное шифрование.

```
// AEAD parameters

// bik = Bob's intro key k = bik n = 4 byte packet number from header ad = 32 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for this message k_header_1 = bik k_header_2 = bik
```
### Запрос токена (Тип 10)

Алиса отправляет Бобу. Боб отвечает сообщением Retry. Размер: 48 + размер полезной нагрузки.

Если у Алисы нет действительного токена, Алиса должна отправить это сообщение вместо Session Request, чтобы избежать накладных расходов асимметричного шифрования при генерации Session Request.

Noise payload: См. ниже.

Исходное содержимое:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Bob intro key + | | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Bob intro key + | | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | | + see KDF for key and n + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
Незашифрованные данные (тег аутентификации Poly1305 не показан):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+------------+------------+
    | > Packet Number                                   | type       | ver        | id         | flag       |
    +---------------------------------------------------+------------+------------+------------+------------+
    | > Source Connection ID                                                                                |
    +-------------------------------------------------------------------------------------------------------+
    | > Token                                                                                               |
    +-------------------------------------------------------------------------------------------------------+
    | >                                                                                                     |
    | >                                                                                                     |
    | > ChaCha20 payload (block data)                                                                       |
    | >                                                                                                     |
    | > :   (length varies)                                                                                 |
    | >                                                                                                     |
    | > see below for allowed blocks                                                                        |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    Destination Connection ID :: Randomly generated by Alice

    Packet Number :: Random number generated by Alice

    type :: 10

    ver :: 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Source Connection ID :: Randomly generated by Alice,

    :   must not be equal to Destination Connection ID

    Token :: zero
```
#### Полезная нагрузка

- Блок DateTime
- Блок заполнения

Минимальный размер полезной нагрузки составляет 8 байт.

#### Примечания

- Для обеспечения устойчивости к зондированию router не должен отправлять сообщение Retry в ответ на сообщение Token Request, если поля типа сообщения, версии протокола и ID сети в сообщении Token Request недействительны.
- Это НЕ стандартное Noise сообщение и не является частью handshake. Оно не связано с сообщением Session Request ничем, кроме ID соединения.
- При большинстве ошибок, включая AEAD или очевидную повторную передачу, Bob должен прекратить дальнейшую обработку сообщения и отбросить сообщение без ответа.
- Bob должен отклонять соединения, где значение временной метки слишком сильно отличается от текущего времени. Назовем максимальную дельту времени "D". Bob должен поддерживать локальный кэш ранее использованных значений handshake и отклонять дубликаты для предотвращения атак повторного воспроизведения. Значения в кэше должны иметь время жизни не менее 2*D. Значения кэша зависят от реализации, однако может использоваться 32-байтовое значение X (или его зашифрованный эквивалент).
- Bob МОЖЕТ отправить сообщение Retry, содержащее нулевой token и блок Termination с кодом причины расхождения часов, если временная метка в блоке DateTime слишком сильно расходится.
- Минимальный размер: TBD, те же правила, что и для Session Created?

### KDF для Hole Punch

Это сообщение должно быстро генерироваться, используя только симметричное шифрование.

```
// AEAD parameters

// aik = Alice's intro key k = aik n = 4 byte packet number from header ad = 32 byte header, before header encryption ciphertext = ENCRYPT(k, n, payload, ad)

    // Header encryption keys for this message k_header_1 = aik k_header_2 = aik
```
### Hole Punch (Тип 11)

Чарли отправляет Алисе в ответ на Relay Intro, полученное от Боба. Алиса отвечает новым Session Request. Размер: 48 + размер полезной нагрузки.

Noise payload: См. ниже.

Исходное содержимое:

```
+----+----+----+----+----+----+----+----+

|  Long Header bytes 0-15, ChaCha20 |

    + encrypted with Alice intro key + | | +----+----+----+----+----+----+----+----+ | Long Header bytes 16-31, ChaCha20 | + encrypted with Alice intro key + | | +----+----+----+----+----+----+----+----+ | | + + | ChaCha20 encrypted data | + (length varies) + | | + see KDF for key and n + | see KDF for associated data | +----+----+----+----+----+----+----+----+ | | + Poly1305 MAC (16 bytes) + | | +----+----+----+----+----+----+----+----+
```
Незашифрованные данные (тег аутентификации Poly1305 не показан):

```
+----+----+----+----+----+----+----+----+

|      Destination Connection ID |

    +---------------------------------------------------+------------+------------+------------+------------+
    | > Packet Number                                   | type       | ver        | id         | flag       |
    +---------------------------------------------------+------------+------------+------------+------------+
    | > Source Connection ID                                                                                |
    +-------------------------------------------------------------------------------------------------------+
    | > Token                                                                                               |
    +-------------------------------------------------------------------------------------------------------+
    | >                                                                                                     |
    | >                                                                                                     |
    | > ChaCha20 payload (block data)                                                                       |
    | >                                                                                                     |
    | > :   (length varies)                                                                                 |
    | >                                                                                                     |
    | > see below for allowed blocks                                                                        |
    |                                                                                                       |
    |                                                                                                       |
    +-------------------------------------------------------------------------------------------------------+

    Destination Connection ID :: See below

    Packet Number :: Random number generated by Charlie

    type :: 11

    ver :: 2

    id :: 1 byte, the network ID (currently 2, except for test networks)

    flag :: 1 byte, unused, set to 0 for future compatibility

    Source Connection ID :: See below

    Token :: 8 byte unsigned integer, randomly generated by Charlie, nonzero.
```
#### Полезная нагрузка

- Блок DateTime
- Блок Address
- Блок Relay Response
- Блок Padding (опционально)

Минимальный размер полезной нагрузки составляет 8 байт. Поскольку блоки DateTime и Address в сумме превышают это значение, требование выполняется только с этими двумя блоками.

Идентификаторы соединения: Два идентификатора соединения выводятся из nonce ретранслятора. Идентификатор соединения назначения представляет собой две копии 4-байтного nonce ретранслятора в формате big-endian, т.е. ((nonce << 32) | nonce). Идентификатор соединения источника является инверсией идентификатора соединения назначения, т.е. ~((nonce << 32) | nonce).

Alice должна игнорировать токен в заголовке. Токен, который должен использоваться в Session Request, находится в блоке Relay Response.

## Полезная нагрузка Noise

Каждая полезная нагрузка Noise содержит ноль или более "блоков".

Используется тот же формат блоков, что определен в спецификациях [NTCP2](/docs/specs/ntcp2) и [ECIES](/docs/specs/ecies). Отдельные типы блоков определяются по-разному. Эквивалентный термин в QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) — это "фреймы".

Существуют опасения, что поощрение разработчиков к совместному использованию кода может привести к проблемам с парсингом. Разработчики должны тщательно рассмотреть преимущества и риски совместного использования кода и убедиться, что правила упорядочивания и валидных блоков различаются для двух контекстов.

### Формат полезной нагрузки

В зашифрованной полезной нагрузке содержится один или несколько блоков. Блок имеет простой формат Tag-Length-Value (TLV). Каждый блок содержит однобайтовый идентификатор, двухбайтовую длину и ноль или более байтов данных. Этот формат идентичен тому, что используется в [NTCP2](/docs/specs/ntcp2) и [ECIES](/docs/specs/ecies), однако определения блоков различаются.

Для обеспечения расширяемости получатели должны игнорировать блоки с неизвестными идентификаторами и обрабатывать их как заполнение.

(Тег аутентификации Poly1305 не показан):

```
+----+----+----+----+----+----+----+----+

[|blk |](##SUBST##|blk |) size | data | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ [|blk |](##SUBST##|blk |) size | data | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+ ~ . . . ~

    blk :: 1 byte, see below size :: 2 bytes, big endian, size of data to follow, 0 - TBD data :: the data
```
Шифрование заголовка использует последние 24 байта пакета в качестве IV для двух операций ChaCha20. Поскольку все пакеты заканчиваются 16-байтовым MAC, это требует, чтобы все полезные нагрузки пакетов были минимум 8 байт. Если полезная нагрузка иначе не соответствует этому требованию, должен быть включён блок заполнения (Padding).

Максимальная полезная нагрузка ChaChaPoly варьируется в зависимости от типа сообщения, MTU и типа IPv4 или IPv6 адреса. Максимальная полезная нагрузка составляет MTU - 60 для IPv4 и MTU - 80 для IPv6. Максимальные данные полезной нагрузки составляют MTU - 63 для IPv4 и MTU - 83 для IPv6. Верхний предел составляет около 1440 байт для IPv4, MTU 1500, сообщение Data. Максимальный общий размер блока равен максимальному размеру полезной нагрузки. Максимальный размер одного блока равен максимальному общему размеру блока. Тип блока составляет 1 байт. Длина блока составляет 2 байта. Максимальный размер данных одного блока равен максимальному размеру одного блока минус 3.

Примечания:

- Разработчики должны обеспечить, что при чтении блока некорректные или вредоносные данные не приведут к выходу за границы следующего блока или за пределы полезной нагрузки.
- Реализации должны игнорировать неизвестные типы блоков для обеспечения обратной совместимости.

Типы блоков:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Block Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Number</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Block Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Options</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15+</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Router Info</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">I2NP Message</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Follow-on Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Termination</td><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 typ.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">8</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Intro</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Next Nonce</td><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">ACK</td><td style="border:1px solid var(--color-border); padding:0.6rem;">12</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 or 21</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;">--</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">17</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Challenge</td><td style="border:1px solid var(--color-border); padding:0.6rem;">18</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">19</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Packet Number</td><td style="border:1px solid var(--color-border); padding:0.6rem;">20</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Congestion</td><td style="border:1px solid var(--color-border); padding:0.6rem;">21</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for experimental features</td><td style="border:1px solid var(--color-border); padding:0.6rem;">224-253</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Padding</td><td style="border:1px solid var(--color-border); padding:0.6rem;">254</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for future extension</td><td style="border:1px solid var(--color-border); padding:0.6rem;">255</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>           
### Правила упорядочивания блоков

В Session Confirmed Router Info должен быть первым блоком.

Во всех остальных сообщениях порядок не определен, за исключением следующих требований: Padding (заполнение), если присутствует, должен быть последним блоком. Termination (завершение), если присутствует, должен быть последним блоком за исключением Padding. Множественные блоки Padding не допускаются в одной полезной нагрузке.

### Спецификации блоков

#### DateTime

Для синхронизации времени:

```
+----+----+----+----+----+----+----+

| 0 | 4 | timestamp |

    +----+----+----+----+----+----+----+

    blk :: 0 size :: 2 bytes, big endian, value = 4 timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106
```
Примечания:

- В отличие от SSU 1, в SSU 2 нет временной метки в заголовке пакета для фазы данных.
- Реализации должны периодически отправлять блоки DateTime в фазе данных.
- Реализации должны округлять до ближайшей секунды, чтобы предотвратить смещение часов в сети.

#### Опции

Передать обновленные параметры. Параметры включают: Минимальное и максимальное заполнение.

Блок опций будет иметь переменную длину.

```
+----+----+----+----+----+----+----+----+

| 1 | size [|tmin|](##SUBST##|tmin|)tmax[|rmin|](##SUBST##|rmin|)rmax[|tdmy|](##SUBST##|tdmy|)

    +----+----+----+----+----+----+----+----+ [|tdmy|](##SUBST##|tdmy|) rdmy | tdelay | rdelay | | ~----+----+----+----+----+----+----+ ~ | more_options | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 1 size :: 2 bytes, big endian, size of options to follow, 12 bytes minimum

    tmin, tmax, rmin, rmax :: requested padding limits

    :   tmin and rmin are for desired resistance to traffic analysis. tmax and rmax are for bandwidth limits. tmin and tmax are the transmit limits for the router sending this options block. rmin and rmax are the receive limits for the router sending this options block. Each is a 4.4 fixed-point float representing 0 to 15.9375 (or think of it as an unsigned 8-bit integer divided by 16.0). This is the ratio of padding to data. Examples: Value of 0x00 means no padding Value of 0x01 means add 6 percent padding Value of 0x10 means add 100 percent padding Value of 0x80 means add 800 percent (8x) padding Alice and Bob will negotiate the minimum and maximum in each direction. These are guidelines, there is no enforcement. Sender should honor receiver's maximum. Sender may or may not honor receiver's minimum, within bandwidth constraints.

    tdmy: Max dummy traffic willing to send, 2 bytes big endian, bytes/sec average rdmy: Requested dummy traffic, 2 bytes big endian, bytes/sec average tdelay: Max intra-message delay willing to insert, 2 bytes big endian, msec average rdelay: Requested intra-message delay, 2 bytes big endian, msec average

    Padding distribution specified as additional parameters? Random delay specified as additional parameters?

    more_options :: Format TBD
```
Проблемы с параметрами:

- Согласование параметров будет определено позже.

#### RouterInfo

Передать RouterInfo Алисы Бобу. Используется только в полезной нагрузке части 2 Session Confirmed. Не использовать в фазе данных; вместо этого используйте I2NP сообщение DatabaseStore.

Минимальный размер: Около 420 байт, если только идентификатор router и подпись в информации router не являются сжимаемыми, что маловероятно.

ПРИМЕЧАНИЕ: Блок Router Info никогда не фрагментируется. Поле frag всегда равно 0/1. См. раздел "Фрагментация Session Confirmed" выше для получения дополнительной информации.

```
+----+----+----+----+----+----+----+----+

| 2 | size [|flag|](##SUBST##|flag|)frag| |

    +----+----+----+----+----+ + | | + Router Info fragment + | (Alice RI in Session Confirmed) | + (Alice, Bob, or third-party + | RI in data phase) | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 2 size :: 2 bytes, big endian, 2 + fragment size flag :: 1 byte flags bit order: 76543210 (bit 7 is MSB) bit 0: 0 for local store, 1 for flood request bit 1: 0 for uncompressed, 1 for gzip compressed bits 7-2: Unused, set to 0 for future compatibility frag :: 1 byte fragment info: bit order: 76543210 (bit 7 is MSB) bits 7-4: fragment number, always 0 bits 3-0: total fragments, always 1, big endian

    routerinfo :: Alice's or Bob's RouterInfo
```
Примечания:

- Router Info опционально сжимается с помощью gzip, как указывает флаговый бит 1. Это отличается от NTCP2, где он никогда не сжимается, и от DatabaseStore Message, где он всегда сжимается. Сжатие опционально, потому что обычно оно приносит мало пользы для небольших Router Info, где мало сжимаемого содержимого, но очень полезно для больших Router Info с несколькими сжимаемыми Router Address. Сжатие рекомендуется, если оно позволяет Router Info поместиться в одном пакете Session Confirmed без фрагментации.
- Максимальный размер первого или единственного фрагмента в сообщении Session Confirmed: MTU - 113 для IPv4 или MTU - 133 для IPv6. Предполагая MTU по умолчанию 1500 байт и отсутствие других блоков в сообщении, 1387 для IPv4 или 1367 для IPv6. 97% текущих router info меньше 1367 без gzip-сжатия. 99.9% текущих router info меньше 1367 при сжатии gzip. Предполагая минимальный MTU 1280 байт и отсутствие других блоков в сообщении, 1167 для IPv4 или 1147 для IPv6. 94% текущих router info меньше 1147 без gzip-сжатия. 97% текущих router info меньше 1147 при сжатии gzip.
- Байт frag теперь не используется, блок Router Info никогда не фрагментируется. Байт frag должен быть установлен как фрагмент 0, общее количество фрагментов 1. Смотрите раздел Session Confirmed Fragmentation выше для получения дополнительной информации.
- Flooding не должен запрашиваться, если в RouterInfo нет опубликованных RouterAddress. Принимающий router не должен выполнять flood RouterInfo, если в нем нет опубликованных RouterAddress.
- Этот протокол не предоставляет подтверждения того, что RouterInfo был сохранен или передан через flood. Если требуется подтверждение, и получатель является floodfill, отправитель должен вместо этого отправить стандартное I2NP DatabaseStoreMessage с токеном ответа.

#### I2NP сообщение

Полное I2NP сообщение с модифицированным заголовком.

Это использует те же 9 байт для заголовка I2NP, что и в [NTCP2](/docs/specs/ntcp2) (тип, идентификатор сообщения, короткое время истечения).

```
+----+----+----+----+----+----+----+----+

| 3 | size [|type|](##SUBST##|type|) msg id |

    +-------------------------------+
    | > short exp                   |
    +-------------------------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 3 size :: 2 bytes, big endian, size of type + msg id + exp + message to follow I2NP message body size is (size - 9). type :: 1 byte, I2NP msg type, see I2NP spec msg id :: 4 bytes, big endian, I2NP message ID short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds. Wraps around in 2106 message :: I2NP message body
```
Примечания:

- Это тот же 9-байтный формат заголовка I2NP, который используется в NTCP2.
- Это точно такой же формат, как у блока First Fragment, но тип блока указывает, что это полное сообщение.
- Максимальный размер, включая 9-байтный заголовок I2NP, составляет MTU - 63 для IPv4 и MTU - 83 для IPv6.

#### Первый фрагмент

Первый фрагмент (фрагмент #0) I2NP сообщения с модифицированным заголовком.

Это использует те же 9 байт для заголовка I2NP, что и в [NTCP2](/docs/specs/ntcp2) (тип, идентификатор сообщения, короткий срок действия).

Общее количество фрагментов не указано.

```
+----+----+----+----+----+----+----+----+

| 4 | size [|type|](##SUBST##|type|) msg id |

    +-------------------------------+
    | > short exp                   |
    +-------------------------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 4 size :: 2 bytes, big endian, size of data to follow Fragment size is (size - 9). type :: 1 byte, I2NP msg type, see I2NP spec msg id :: 4 bytes, big endian, I2NP message ID short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds. Wraps around in 2106 message :: Partial I2NP message body, bytes 0 - (size - 10)
```
Примечания:

- Это тот же 9-байтный формат заголовка I2NP, используемый в NTCP2.
- Это точно такой же формат, как у блока I2NP Message, но тип блока указывает, что это первый фрагмент сообщения.
- Длина частичного сообщения должна быть больше нуля.
- Как и в SSU 1, рекомендуется сначала отправлять последний фрагмент, чтобы получатель знал общее количество фрагментов и мог эффективно выделить буферы приёма.
- Максимальный размер, включая 9-байтный заголовок I2NP, составляет MTU - 63 для IPv4 и MTU - 83 для IPv6.

#### Последующий фрагмент

Дополнительный фрагмент (номер фрагмента больше нуля) I2NP-сообщения.

```
+----+----+----+----+----+----+----+----+

| 5 | size [|frag|](##SUBST##|frag|) msg id |

    +----+----+----+----+----+----+----+----+ | | + + | partial message | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 5 size :: 2 bytes, big endian, size of data to follow Fragment size is (size - 5). frag :: Fragment info: Bit order: 76543210 (bit 7 is MSB) bits 7-1: fragment number 1 - 127 (0 not allowed) bit 0: isLast (1 = true) msg id :: 4 bytes, big endian, I2NP message ID message :: Partial I2NP message body
```
Примечания:

- Длина частичного сообщения должна быть больше нуля.
- Как и в SSU 1, рекомендуется отправлять последний фрагмент первым, чтобы получатель знал общее количество фрагментов и мог эффективно выделить буферы для приема.
- Как и в SSU 1, максимальный номер фрагмента равен 127, но практический лимит составляет 63 или меньше. Реализации могут ограничить максимум до практически применимого для максимального размера I2NP сообщения около 64 КБ, что составляет примерно 55 фрагментов с минимальным MTU 1280. См. раздел "Максимальный размер I2NP сообщения" ниже.
- Максимальный размер частичного сообщения (не включая frag и message id) составляет MTU - 68 для IPv4 и MTU - 88 для IPv6.

#### Завершение

Разорвать соединение. Это должен быть последний блок без заполнения в полезной нагрузке.

```
+----+----+----+----+----+----+----+----+

| 6 | size | valid data packets |

    +----+----+----+----+----+----+----+----+

    :   received | rsn| addl data |

    +----+----+----+----+ + ~ . . . ~ +----+----+----+----+----+----+----+----+

    blk :: 6 size :: 2 bytes, big endian, value = 9 or more valid data packets received :: The number of valid packets received (current receive nonce value) 0 if error occurs in handshake phase 8 bytes, big endian rsn :: reason, 1 byte: 0: normal close or unspecified 1: termination received 2: idle timeout 3: router shutdown 4: data phase AEAD failure 5: incompatible options 6: incompatible signature type 7: clock skew 8: padding violation 9: AEAD framing error 10: payload format error 11: Session Request error 12: Session Created error 13: Session Confirmed error 14: Timeout 15: RI signature verification fail 16: s parameter missing, invalid, or mismatched in RouterInfo 17: banned 18: bad token 19: connection limits 20: incompatible version 21: wrong net ID 22: replaced by new session addl data :: optional, 0 or more bytes, for future expansion, debugging, or reason text. Format unspecified and may vary based on reason code.
```
Примечания:

- Не все причины могут фактически использоваться, зависит от реализации. Большинство сбоев обычно приведет к отбрасыванию сообщения, а не к завершению соединения. См. примечания в разделах сообщений handshake выше. Дополнительные перечисленные причины предназначены для согласованности, логирования, отладки или в случае изменения политики.
- Рекомендуется включать блок ACK вместе с блоком Termination.
- В фазе данных, по любой причине, отличной от "получено завершение", peer должен ответить блоком termination с причиной "получено завершение".

#### RelayRequest

Отправляется в сообщении Data в рамках сессии, от Alice к Bob. См. раздел "Процесс ретрансляции" ниже.

```
+----+----+----+----+----+----+----+----+

|  7 | size [|flag|](##SUBST##|flag|) nonce |

    +-------+-------+---------------+-----------------------------------+
    | > relay tag                   | > timestamp                       |
    +-------+-------+---------------+-----------------------------------+
    | ver   | asz   | AlicePort     | > Alice IP address                |
    +-------+-------+---------------+-----------------------------------+

    ~ ~ | . . . | +----+----+----+----+----+----+----+----+

    blk :: 7 size :: 2 bytes, big endian, size of data to follow flag :: 1 byte flags, Unused, set to 0 for future compatibility

    The data below here is covered by the signature, and Bob forwards it unmodified.

    nonce :: 4 bytes, randomly generated by Alice relay tag :: 4 bytes, the itag from Charlie's RI timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106 ver :: 1 byte SSU version to be used for the introduction: 1: SSU 1 2: SSU 2 asz :: 1 byte endpoint (port + IP) size (6 or 18) AlicePort :: 2 byte Alice's port number, big endian Alice IP :: (asz - 2) byte representation of Alice's IP address, network byte order signature :: length varies, 64 bytes for Ed25519. Signature of prologue, Bob's hash, and signed data above, as signed by Alice.
```
Примечания:

- IP-адрес всегда включается (в отличие от SSU 1) и может отличаться от IP, используемого для сессии.

Подпись:

Алиса подписывает запрос и включает его в этот блок; Боб пересылает его в блоке Relay Intro к Чарли. Алгоритм подписи: Подписать следующие данные с помощью ключа подписи router'а Алисы:

- prologue: 16 байт "RelayRequestData", не завершается нулем (не включается в сообщение)
- bhash: 32-байтный hash router'а Bob (не включается в сообщение)
- chash: 32-байтный hash router'а Charlie (не включается в сообщение)
- nonce: 4-байтный nonce
- relay tag: 4-байтный relay tag
- timestamp: 4-байтная временная метка (секунды)
- ver: 1 байт версии SSU
- asz: 1 байт размера endpoint'а (порт + IP) (6 или 18)
- AlicePort: 2-байтный номер порта Alice
- Alice IP: (asz - 2) байт IP-адреса Alice

#### RelayResponse

Отправляется в сообщении Data в рамках сессии, от Charlie к Bob или от Bob к Alice, И в сообщении Hole Punch от Charlie к Alice. См. раздел "Процесс ретрансляции" ниже.

```
+----+----+----+----+----+----+----+----+

|  8 | size [|flag|](##SUBST##|flag|)code| nonce

    +----+----+----+----+----+----+----+----+

    :   |     timestamp | ver| csz|Char

    +----+----+----+----+----+----+----+----+

    :   Port| Charlie IP addr | |

    +----+----+----+----+----+ + | signature | + length varies + | 64 bytes for Ed25519 | ~ ~ | . . . | +----+----+----+----+----+----+----+----+ | Token | +----+----+----+----+----+----+----+----+

    blk :: 8 size :: 2 bytes, 6 flag :: 1 byte flags, Unused, set to 0 for future compatibility code :: 1 byte status code: 0: accept 1: rejected by Bob, reason unspecified 2: rejected by Bob, Charlie is banned 3: rejected by Bob, limit exceeded 4: rejected by Bob, signature failure 5: rejected by Bob, relay tag not found 6: rejected by Bob, Alice RI not found 7-63: other rejected by Bob codes TBD 64: rejected by Charlie, reason unspecified 65: rejected by Charlie, unsupported address 66: rejected by Charlie, limit exceeded 67: rejected by Charlie, signature failure 68: rejected by Charlie, Alice is already connected 69: rejected by Charlie, Alice is banned 70: rejected by Charlie, Alice is unknown 71-127: other rejected by Charlie codes TBD 128: reject, source and reason unspecified 129-255: other reject codes TBD

    The data below is covered by the signature if the code is 0 (accept). Bob forwards it unmodified.

    nonce :: 4 bytes, as received from Bob or Alice

    The data below is present only if the code is 0 (accept).

    timestamp :: Unix timestamp, unsigned seconds.

    :   Wraps around in 2106

    ver :: 1 byte SSU version to be used for the introduction:

    :   1: SSU 1 2: SSU 2

    csz :: 1 byte endpoint (port + IP) size (0 or 6 or 18)

    :   may be 0 for some rejection codes

    CharliePort :: 2 byte Charlie's port number, big endian

    :   not present if csz is 0

    Charlie IP :: (csz - 2) byte representation of Charlie's IP address,

    :   network byte order not present if csz is 0

    signature :: length varies, 64 bytes for Ed25519.

    :   Signature of prologue, Bob's hash, and signed data above, as signed by Charlie. Not present if rejected by Bob.

    token :: Token generated by Charlie for Alice to use

    :   in the Session Request. Only present if code is 0 (accept)
```
Примечания:

Токен должен быть немедленно использован Алисой в запросе сессии.

Подпись:

Если Чарли соглашается (код ответа 0) или отклоняет (код ответа 64 или выше), Чарли подписывает ответ и включает его в этот блок; Боб пересылает его в блоке Relay Response Алисе. Алгоритм подписи: Подписать следующие данные ключом подписи router'а Чарли:

- пролог: 16 байт "RelayAgreementOK", не завершается нулем (не включается в сообщение)
- bhash: 32-байтовый хеш router'а Bob'а (не включается в сообщение)
- nonce: 4-байтовый nonce
- timestamp: 4-байтовая метка времени (секунды)
- ver: 1 байт версии SSU
- csz: 1 байт размера конечной точки (порт + IP) (0 или 6 или 18)
- CharliePort: 2 байта номера порта Charlie (отсутствует, если csz равно 0)
- Charlie IP: (csz - 2) байт IP-адреса Charlie (отсутствует, если csz равно 0)

Если Bob отклоняет (код ответа 1-63), Bob подписывает ответ и включает его в этот блок. Алгоритм подписи: Подписать следующие данные ключом подписи router'а Bob'а:

- prologue: 16 байт "RelayAgreementOK", без завершающего нуля (не включается в сообщение)
- bhash: 32-байтовый хеш router Боба (не включается в сообщение)
- nonce: 4-байтовый nonce
- timestamp: 4-байтовая временная метка (секунды)
- ver: 1 байт версии SSU
- csz: 1 байт = 0

#### RelayIntro

Отправляется в сообщении Data внутри сессии, от Bob к Charlie. См. раздел Relay Process ниже.

Должен предшествовать блок RouterInfo или блок I2NP сообщения DatabaseStore (или фрагмент), содержащий Router Info Алисы, либо в той же полезной нагрузке (если есть место), либо в предыдущем сообщении.

```
+----+----+----+----+----+----+----+----+

|  9 | size [|flag|](##SUBST##|flag|) |

    +----+----+----+----+ + | | + + | Alice Router Hash | + 32 bytes + | | + +----+----+----+----+ | | nonce | +----+----+----+----+----+----+----+----+ | relay tag | timestamp | +----+----+----+----+----+----+----+----+ | ver| asz[|AlicePort|](##SUBST##|AlicePort|) Alice IP address | +----+----+----+----+----+----+----+----+ | signature | + length varies + | 64 bytes for Ed25519 | ~ ~ | . . . | +----+----+----+----+----+----+----+----+

    blk :: 9 size :: 2 bytes, big endian, size of data to follow flag :: 1 byte flags, Unused, set to 0 for future compatibility hash :: Alice's 32-byte router hash,

    The data below here is covered by the signature, as received from Alice in the Relay Request, and Bob forwards it unmodified.

    nonce :: 4 bytes, as received from Alice relay tag :: 4 bytes, the itag from Charlie's RI timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106 ver :: 1 byte SSU version to be used for the introduction: 1: SSU 1 2: SSU 2 asz :: 1 byte endpoint (port + IP) size (6 or 18) AlicePort :: 2 byte Alice's port number, big endian Alice IP :: (asz - 2) byte representation of Alice's IP address, network byte order signature :: length varies, 64 bytes for Ed25519. Signature of prologue, Bob's hash, and signed data above, as signed by Alice.
```
Примечания:

- Для IPv4 IP-адрес Alice всегда составляет 4 байта, поскольку Alice пытается подключиться к Charlie через IPv4. IPv6 поддерживается, и IP-адрес Alice может составлять 16 байт.
- Для IPv4 это сообщение должно быть отправлено через установленное IPv4-соединение, поскольку это единственный способ для Bob узнать IPv4-адрес Charlie, чтобы вернуть его Alice в [RelayResponse](#relayresponse). IPv6 поддерживается, и это сообщение может быть отправлено через установленное IPv6-соединение.
- Любой SSU-адрес, опубликованный с introducers, должен содержать "4" или "6" в опции "caps".

Подпись:

Алиса подписывает запрос, и Боб пересылает его в этом блоке Чарли. Алгоритм верификации: Проверить следующие данные с помощью ключа подписи router Алисы:

- пролог: 16 байт "RelayRequestData", не завершается нулем (не включается в сообщение)
- bhash: 32-байтный хеш router'а Bob (не включается в сообщение)
- chash: 32-байтный хеш router'а Charlie (не включается в сообщение)
- nonce: 4-байтный nonce
- relay tag: 4-байтный relay tag
- timestamp: 4-байтная временная метка (секунды)
- ver: 1-байтная версия SSU
- asz: 1-байтный размер конечной точки (порт + IP) (6 или 18)
- AlicePort: 2-байтный номер порта Alice
- Alice IP: (asz - 2) байт IP-адреса Alice

#### PeerTest

Отправляется либо в сообщении Data внутри сессии, либо в сообщении Peer Test вне сессии. См. раздел "Процесс тестирования пиров" ниже.

Для сообщения 2 должен предшествовать блок RouterInfo или блок I2NP DatabaseStore сообщения (или фрагмент), содержащий Router Info Алисы, либо в той же полезной нагрузке (если есть место), либо в предыдущем сообщении.

Для сообщения 4, если relay принимается (код причины 0), должно предшествовать блок RouterInfo или блок I2NP сообщения DatabaseStore (или фрагмент), содержащий Router Info Чарли, либо в той же полезной нагрузке (если есть место), либо в предыдущем сообщении.

```
+----+----+----+----+----+----+----+----+

| 10 | size | msg[|code|](##SUBST##|code|)flag| |

    +----+----+----+----+----+----+ + | Alice router hash (message 2 only) | + or + | Charlie router hash (message 4 only) | + or all zeros if rejected by Bob + | Not present in messages 1,3,5,6,7 | + +----+----+ | | ver| +----+----+----+----+----+----+----+----+ nonce | timestamp | asz| +----+----+----+----+----+----+----+----+ [|AlicePort|](##SUBST##|AlicePort|) Alice IP address | | +----+----+----+----+----+----+ + | signature | + length varies + | 64 bytes for Ed25519 | ~ ~ | . . . | +----+----+----+----+----+----+----+----+

    blk :: 10 size :: 2 bytes, big endian, size of data to follow msg :: 1 byte message number 1-7 code :: 1 byte status code: 0: accept 1: rejected by Bob, reason unspecified 2: rejected by Bob, no Charlie available 3: rejected by Bob, limit exceeded 4: rejected by Bob, signature failure 5: rejected by Bob, address unsupported 6-63: other rejected by Bob codes TBD 64: rejected by Charlie, reason unspecified 65: rejected by Charlie, unsupported address 66: rejected by Charlie, limit exceeded 67: rejected by Charlie, signature failure 68: rejected by Charlie, Alice is already connected 69: rejected by Charlie, Alice is banned 70: rejected by Charlie, Alice is unknown 70-127: other rejected by Charlie codes TBD 128: reject, source and reason unspecified 129-255: other reject codes TBD reject codes only allowed in messages 3 and 4 flag :: 1 byte flags, Unused, set to 0 for future compatibility hash :: Alice's or Charlie's 32-byte router hash, only present in messages 2 and 4. All zeros (fake hash) in message 4 if rejected by Bob.

    For messages 1-4, the data below here is covered by the signature, if present, and Bob forwards it unmodified.

    ver :: 1 byte SSU version:

    :   1: SSU 1 (not supported) 2: SSU 2 (required)

    nonce :: 4 byte test nonce, big endian timestamp :: Unix timestamp, unsigned seconds. Wraps around in 2106 asz :: 1 byte endpoint (port + IP) size (6 or 18) AlicePort :: 2 byte Alice's port number, big endian Alice IP :: (asz - 2) byte representation of Alice's IP address, network byte order signature :: length varies, 64 bytes for Ed25519. Signature of prologue, Bob's hash, and signed data above, as signed by Alice or Charlie. Only present for messages 1-4. Optional in message 5-7.
```
Примечания:

- В отличие от SSU 1, сообщение 1 должно включать IP-адрес и порт Алисы.

- Тестирование IPv6-адресов поддерживается, и связь между Alice-Bob и Alice-Charlie может осуществляться через IPv6, если Bob и Charlie указывают поддержку с помощью возможности 'B' в своём опубликованном IPv6-адресе. Подробности смотрите в Предложении 126.

Алиса отправляет запрос Бобу, используя существующую сессию через транспорт (IPv4 или IPv6), который она желает протестировать. Когда Боб получает запрос от Алисы через IPv4, Боб должен выбрать Чарли, который анонсирует IPv4 адрес. Когда Боб получает запрос от Алисы через IPv6, Боб должен выбрать Чарли, который анонсирует IPv6 адрес. Фактическая коммуникация Боб-Чарли может происходить через IPv4 или IPv6 (т.е., независимо от типа адреса Алисы).

- Сообщения 1-4 должны содержаться в сообщении Data в существующей сессии.

- Bob должен отправить RI Alice к Charlie перед отправкой сообщения 2.

- Bob должен отправить RI Чарли Алисе до отправки сообщения 4, если принято (код причины 0).

- Сообщения 5-7 должны содержаться в сообщении Peer Test вне сессии.

- Сообщения 5 и 7 могут содержать те же подписанные данные, что были отправлены в сообщениях 3 и 4, или они могут быть созданы заново с новой временной меткой. Подпись не обязательна.

- Сообщение 6 может содержать те же подписанные данные, что были отправлены в сообщениях 1 и 2, или они могут быть созданы заново с новой временной меткой. Подпись необязательна.

Подписи:

Алиса подписывает запрос и включает его в сообщение 1; Боб пересылает его в сообщении 2 Чарли. Чарли подписывает ответ и включает его в сообщение 3; Боб пересылает его в сообщении 4 Алисе. Алгоритм подписи: Подписать или проверить следующие данные с помощью ключа подписи Алисы или Чарли:

- prologue: 16 байт "PeerTestValidate", не завершается нулем (не включается в сообщение)
- bhash: 32-байтный хеш router'а Боба (не включается в сообщение)
- ahash: 32-байтный хеш router'а Алисы (используется только в подписи для сообщений 3 и 4; не включается в сообщения 3 или 4)
- ver: 1 байт версии SSU
- nonce: 4-байтный тестовый nonce
- timestamp: 4-байтная временная метка (секунды)
- asz: 1 байт размера endpoint'а (порт + IP) (6 или 18)
- AlicePort: 2-байтный номер порта Алисы
- Alice IP: (asz - 2) байт IP-адреса Алисы

#### NextNonce

TODO только если мы ротируем ключи

```
+----+----+----+----+----+----+----+----+

| 11 | size | TBD |

    +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 11 size :: 2 bytes, big endian, size of data to follow
```
#### Подтверждение

4-байтовое подтверждение прохождения, за которым следует счетчик подтверждений и ноль или более диапазонов nack/ack.

Этот дизайн адаптирован и упрощен из QUIC. Цели дизайна следующие:

- Мы хотим эффективно кодировать "битовое поле", которое представляет собой последовательность битов, обозначающих подтвержденные пакеты.
- Битовое поле состоит в основном из 1. И 1, и 0 обычно идут последовательными "группами".
- Количество места в пакете, доступное для подтверждений, варьируется.
- Наиболее важным является бит с наибольшим номером. Биты с меньшими номерами менее важны. На определенном расстоянии от старшего бита самые старые биты будут "забыты" и никогда больше не отправятся.

Кодирование, описанное ниже, достигает этих целей проектирования, отправляя номер самого старшего бита, установленного в 1, вместе с дополнительными последовательными битами ниже него, которые также установлены в 1. После этого, если есть место, один или несколько "диапазонов", указывающих количество последовательных 0 битов и последовательных 1 битов ниже них. См. QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) раздел 13.2.3 для дополнительной информации.

```
+----+----+----+----+----+----+----+----+

| 12 | size | Ack Through [|acnt|](##SUBST##|acnt|)

    +-------------+-------------+
    | > range     | > range     |
    +-------------+-------------+

    ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 12 size :: 2 bytes, big endian, size of data to follow, 5 minimum ack through :: highest packet number acked acnt :: number of acks lower than ack through also acked, 0-255 range :: If present, 1 byte nack count followed by 1 byte ack count, 0-255 each
```
Примеры:

Мы хотим подтвердить только пакет 10:

- Ack Through: 10
- acnt: 0
- диапазоны не включены

Мы хотим подтвердить только пакеты 8-10:

- Ack Through: 10
- acnt: 2
- диапазоны не включены

Мы хотим отправить ACK для 10 9 8 6 5 2 1 0 и NACK для 7 4 3. Кодирование ACK Block выглядит следующим образом:

- Ack Through: 10
- acnt: 2 (ack 9 8)
- range: 1 2 (nack 7, ack 6 5)
- range: 2 3 (nack 4 3, ack 2 1 0)

Примечания:

- Диапазоны могут отсутствовать. Максимальное количество диапазонов не указано, может быть столько, сколько поместится в пакет.
- Range nack может быть нулем при подтверждении более 255 последовательных пакетов.
- Range ack может быть нулем при отклонении более 255 последовательных пакетов.
- Range nack и ack не могут быть одновременно нулевыми.
- После последнего диапазона пакеты не подтверждаются и не отклоняются. Длина блока ack и обработка старых ack/nack зависит от отправителя блока ack. См. обсуждение в разделах ack ниже.
- Ack through должен быть наивысшим номером полученного пакета, а любые пакеты с большими номерами не были получены. Однако в ограниченных ситуациях он может быть ниже, например, при подтверждении одного пакета, который "заполняет дыру", или в упрощенной реализации, которая не поддерживает состояние всех полученных пакетов. Выше наивысшего полученного пакеты не подтверждаются и не отклоняются, но после нескольких блоков ack может быть уместно перейти в режим быстрой повторной передачи.
- Этот формат является упрощенной версией формата в QUIC. Он разработан для эффективного кодирования большого количества ACK вместе с пачками NACK.
- Блоки ACK используются для подтверждения пакетов фазы данных. Они должны включаться только для внутрисессионных пакетов фазы данных.

#### Адрес

2-байтовый порт и 4- или 16-байтовый IP-адрес. Адрес Алисы, отправленный Алисе Бобом, или адрес Боба, отправленный Бобу Алисой.

```
+----+----+----+----+----+----+----+----+

| 13 | 6 or 18 | Port | IP Address

    +----+----+----+----+----+----+----+----+

    :   | 

    +----+

    blk :: 13 size :: 2 bytes, big endian, 6 or 18 port :: 2 bytes, big endian ip :: 4 byte IPv4 or 16 byte IPv6 address, big endian (network byte order)
```
#### Запрос тега релея

Это может быть отправлено Alice в сообщении Session Request, Session Confirmed или Data. Не поддерживается в сообщении Session Created, поскольку Bob ещё не имеет RI Alice и не знает, поддерживает ли Alice relay. Также, если Bob получает входящее соединение, ему, вероятно, не нужны introducers (за исключением, возможно, другого типа ipv4/ipv6).

Когда отправлено в Session Request, Боб может ответить с Relay Tag в сообщении Session Created, или может выбрать подождать до получения RouterInfo Алисы в Session Confirmed для проверки личности Алисы перед ответом в сообщении Data. Если Боб не хочет выполнять ретрансляцию для Алисы, он не отправляет блок Relay Tag.

```
+----+----+----+

| 15 | 0 |

    +----+----+----+

    blk :: 15 size :: 2 bytes, big endian, value = 0
```
#### Тег ретрансляции

Это может быть отправлено Бобом в сообщении Session Confirmed или Data в ответ на Relay Tag Request от Алисы.

Когда Relay Tag Request отправляется в Session Request, Bob может ответить с Relay Tag в сообщении Session Created, или может выбрать подождать до получения RouterInfo Алисы в Session Confirmed, чтобы проверить личность Алисы перед ответом в Data сообщении. Если Bob не желает быть relay для Алисы, он не отправляет блок Relay Tag.

```
+----+----+----+----+----+----+----+

| 16 | 4 | relay tag |

    +----+----+----+----+----+----+----+

    blk :: 16 size :: 2 bytes, big endian, value = 4 relay tag :: 4 bytes, big endian, nonzero
```
#### Новый токен

Для последующего подключения. Обычно включается в сообщения Session Created и Session Confirmed. Также может быть отправлен повторно в сообщении Data долгоживущей сессии, если предыдущий токен истекает.

```
+----+----+----+----+----+----+----+----+

| 17 | 12 | expires |

    +----+----+----+----+----+----+----+----+

    :   token |

    +----+----+----+----+----+----+----+

    blk :: 17 size :: 2 bytes, big endian, value = 12 expires :: Unix timestamp, unsigned seconds. Wraps around in 2106 token :: 8 bytes, big endian
```
#### Проверка пути

Ping с произвольными данными, которые возвращаются в Path Response, используется как keep-alive или для проверки изменения IP/порта.

```
+----+----+----+----+----+----+----+----+

| 18 | size | Arbitrary Data |

    +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 18 size :: 2 bytes, big endian, size of data to follow data :: Arbitrary data to be returned in a Path Response length as selected by sender
```
Примечания:

- Рекомендуется минимальный размер данных 8 байт, содержащих случайные данные, но это не обязательно.
- Максимальный размер не указан, но он должен быть значительно меньше 1280, поскольку PMTU во время фазы проверки пути составляет 1280.
- Большие размеры вызовов не рекомендуются, поскольку они могут стать вектором для атак усиления пакетов.

#### Ответ пути

Pong с данными, полученными в Path Challenge, как ответ на Path Challenge, используется как keep-alive или для валидации изменения IP/Port.

```
+----+----+----+----+----+----+----+----+

| 19 | size | |

    +----+----+----+ + | Data received in Path Challenge | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 19 size :: 2 bytes, big endian, size of data to follow data :: As received in a Path Challenge
```
#### Номер первого пакета

Опционально включается в handshake в каждом направлении для указания номера первого пакета, который будет отправлен. Это обеспечивает большую безопасность для шифрования заголовков, аналогично TCP.

Не полностью определено, в настоящее время не поддерживается.

```
+----+----+----+----+----+----+----+

| 20 | size | First pkt number |

    +----+----+----+----+----+----+----+

    blk :: 20 size :: 4 pkt num :: The first packet number to be sent in the data phase
```
#### Перегрузка

Этот блок предназначен для обеспечения расширяемого метода обмена информацией о контроле перегрузки. Контроль перегрузки может быть сложным и может развиваться по мере накопления опыта работы с протоколом в живом тестировании или после полного развертывания.

Это позволяет исключить любую информацию о перегрузке из часто используемых блоков I2NP, First Fragment, Followon Fragment и ACK, где не выделено места для флагов. Хотя в заголовке пакета Data есть три байта неиспользуемых флагов, это также обеспечивает ограниченное пространство для расширяемости и более слабую защиту шифрования.

Хотя использование 4-байтного блока для двух битов информации является несколько расточительным, размещение этого в отдельном блоке позволяет нам легко расширить его дополнительными данными, такими как текущие размеры окон, измеренное RTT или другие флаги. Опыт показал, что одних только битов флагов часто недостаточно и неудобно для реализации продвинутых схем контроля перегрузок. Попытка добавить поддержку любой возможной функции контроля перегрузок в, например, блок ACK, привела бы к трате места и усложнению парсинга этого блока.

Реализации не должны предполагать, что другой router поддерживает какой-либо конкретный флаговый бит или функцию, включенную здесь, если только реализация не требуется будущей версией данной спецификации.

Этот блок вероятно должен быть последним блоком без заполнения в полезной нагрузке.

```
+----+----+----+----+

| 21 | size [|flag|](##SUBST##|flag|)

    +----+----+----+----+

    blk :: 21 size :: 1 (or more if extended) flag :: 1 byte flags bit order: 76543210 (bit 7 is MSB) bit 0: 1 to request immediate ack bit 1: 1 for explicit congestion notification (ECN) bits 7-2: Unused, set to 0 for future compatibility
```
#### Заполнение

Это предназначено для заполнения внутри AEAD полезных нагрузок. Заполнение для всех сообщений находится внутри AEAD полезных нагрузок.

Padding должен примерно соответствовать согласованным параметрам. Bob отправил свои запрошенные параметры tx/rx min/max в Session Created. Alice отправила свои запрошенные параметры tx/rx min/max в Session Confirmed. Обновленные опции могут быть отправлены во время фазы данных. См. информацию о блоке опций выше.

Если присутствует, это должен быть последний блок в полезной нагрузке.

```
+----+----+----+----+----+----+----+----+

[|254 |](##SUBST##|254 |) size | padding | +----+----+----+ + | | ~ . . . ~ | | +----+----+----+----+----+----+----+----+

    blk :: 254 size :: 2 bytes, big endian, size of padding to follow padding :: random data
```
Примечания:

- Размер = 0 разрешен.
- Стратегии заполнения TBD.
- Минимальное заполнение TBD.
- Полезные нагрузки только с заполнением разрешены.
- Значения заполнения по умолчанию TBD.
- См. блок опций для согласования параметров заполнения
- См. блок опций для параметров мин/макс заполнения
- Не превышайте MTU. Если необходимо больше заполнения, отправьте несколько сообщений.
- Ответ router'а на нарушение согласованного заполнения зависит от реализации.
- Длина заполнения должна определяться либо для каждого сообщения с учетом оценок распределения длины, либо должны добавляться случайные задержки. Эти контрмеры должны быть включены для противодействия DPI, поскольку размеры сообщений иначе выдавали бы, что I2P трафик передается транспортным протоколом. Точная схема заполнения - это область будущей работы, Приложение A [NTCP2](/docs/specs/ntcp2) предоставляет больше информации по этой теме.

## Предотвращение повторного воспроизведения

SSU2 спроектирован для минимизации воздействия сообщений, повторно воспроизведенных злоумышленником.

Сообщения Token Request, Retry, Session Request, Session Created, Hole Punch и внесессионные Peer Test должны содержать блоки DateTime.

И Алиса, и Боб проверяют, что время для этих сообщений находится в пределах допустимого отклонения (рекомендуется +/- 2 минуты). Для "защиты от зондирования" Боб не должен отвечать на сообщения Token Request или Session Request, если отклонение недопустимо, поскольку эти сообщения могут быть атакой с повторным воспроизведением или зондированием.

Bob может выбрать отклонение дублированных сообщений Token Request и Retry, даже если искажение действительно, через фильтр Блума или другой механизм. Однако размер и процессорная стоимость ответа на эти сообщения низкая. В худшем случае, повторно отправленное сообщение Token Request может аннулировать ранее отправленный токен.

Система токенов значительно минимизирует влияние повторно переданных сообщений Session Request. Поскольку токены могут использоваться только один раз, повторно переданное сообщение Session Request никогда не будет иметь действительный токен. Bob может выбрать отклонение дублированных сообщений Session Request, даже если отклонение времени действительно, с помощью фильтра Блума или другого механизма. Однако размер и стоимость процессорного времени для ответа сообщением Retry невелики. В худшем случае отправка сообщения Retry может аннулировать ранее отправленный токен.

Дублированные сообщения Session Created и Session Confirmed не пройдут валидацию, поскольку состояние handshake Noise не будет находиться в правильном состоянии для их расшифровки. В худшем случае узел может повторно передать Session Confirmed в ответ на явный дубликат Session Created.

Повторно переданные сообщения Hole Punch и Peer Test должны иметь минимальное влияние или не иметь его вовсе.

Router должны использовать номер пакета сообщения данных для обнаружения и отбрасывания дублирующихся сообщений фазы данных. Каждый номер пакета должен использоваться только один раз. Повторно переданные сообщения должны игнорироваться.

## Повторная передача рукопожатия

### Запрос сессии

Если Alice не получает Session Created или Retry:

Сохраняйте те же идентификаторы источника и соединения, эфемерный ключ и номер пакета 0. Или просто сохраните и повторно передайте тот же зашифрованный пакет. Номер пакета не должен увеличиваться, поскольку это изменит значение цепочечного хеша, используемого для шифрования сообщения Session Created.

Рекомендуемые интервалы повторной передачи: 1,25, 2,5 и 5 секунд (1,25, 3,75 и 8,75 секунд после первой отправки). Рекомендуемый таймаут: 15 секунд общего времени

### Сессия создана

Если Боб не получает Session Confirmed:

Сохраняйте те же идентификаторы источника и соединения, эфемерный ключ и номер пакета 0. Или просто сохраните зашифрованный пакет. Номер пакета не должен увеличиваться, поскольку это изменило бы значение цепочки хешей, используемое для шифрования сообщения Session Confirmed.

Рекомендуемые интервалы повторной передачи: 1, 2 и 4 секунды (1, 3 и 7 секунд после первой отправки). Рекомендуемый тайм-аут: 12 секунд общее время

### Сессия подтверждена

В SSU 1 Алиса не переходит к фазе данных до получения первого пакета данных от Боба. Это делает установку соединения в SSU 1 процессом с двумя круговыми обменами.

Для SSU 2, рекомендуемые интервалы повторной передачи Session Confirmed: 1,25, 2,5 и 5 секунд (1,25, 3,75 и 8,75 секунд после первой отправки).

Существует несколько альтернатив. Все они требуют 1 RTT:

1) Алиса предполагает, что Session Confirmed было получено, отправляет сообщения с данными немедленно, никогда не повторно передает Session Confirmed. Пакеты данных, полученные не по порядку (до Session Confirmed), будут недешифруемыми, но будут повторно переданы. Если Session Confirmed потеряно, все отправленные сообщения с данными будут отброшены. 2) Как в 1), отправлять сообщения с данными немедленно, но также повторно передавать Session Confirmed до получения сообщения с данными. 3) Мы могли бы использовать IK вместо XK, поскольку он имеет только два сообщения в рукопожатии, но он использует дополнительный DH (4 вместо 3).

Рекомендуемая реализация - это вариант 2). Алиса должна сохранять информацию, необходимую для повторной передачи сообщения Session Confirmed. Алиса также должна повторно передавать все сообщения Data после повторной передачи сообщения Session Confirmed.

При повторной передаче Session Confirmed сохраняйте те же идентификаторы источника и соединения, эфемерный ключ и номер пакета 1. Или просто сохраните зашифрованный пакет. Номер пакета не должен увеличиваться, поскольку это изменит значение цепочечного хеша, которое является входными данными для функции split().

Bob может сохранять (ставить в очередь) сообщения данных, полученные до сообщения Session Confirmed. Ни ключи защиты заголовков, ни ключи расшифровки недоступны до получения сообщения Session Confirmed, поэтому Bob не знает, что это сообщения данных, но это можно предположить. После получения сообщения Session Confirmed, Bob может расшифровать и обработать сообщения данных из очереди. Если это слишком сложно, Bob может просто отбросить нерасшифровываемые сообщения данных, поскольку Alice повторно передаст их.

Примечание: Если пакеты session confirmed потеряны, Bob повторно передаст session created. Заголовок session created не будет расшифровываться с помощью intro key Алисы, поскольку он установлен с intro key Боба (если только не выполняется резервная расшифровка с intro key Боба). Bob может немедленно повторно передать пакеты session confirmed, если они не были подтверждены ранее, и получен нерасшифровываемый пакет.

### Запрос токена

Если Алиса не получает Retry:

Сохраняйте те же идентификаторы источника и соединения. Реализация может сгенерировать новый случайный номер пакета и зашифровать новый пакет; или может повторно использовать тот же номер пакета или просто сохранить и повторно передать тот же зашифрованный пакет. Номер пакета не должен увеличиваться, поскольку это изменило бы значение цепного хеша, используемого для шифрования сообщения Session Created.

Рекомендуемые интервалы повторной передачи: 3 и 6 секунд (3 и 9 секунд после первой отправки). Рекомендуемый таймаут: 15 секунд общего времени

### Повторить

Если Bob не получает Session Confirmed:

Сообщение Retry не передается повторно при истечении времени ожидания, чтобы уменьшить влияние поддельных адресов источника.

Однако сообщение Retry может быть повторно передано в ответ на получение повторного сообщения Session Request с оригинальным (недействительным) токеном, или в ответ на повторное сообщение Token Request. В любом из этих случаев это указывает на то, что сообщение Retry было потеряно.

Если получено второе сообщение Session Request с другим, но все еще недействительным токеном, отбросить ожидающую сессию и не отвечать.

При повторной отправке сообщения Retry: сохраняйте те же идентификаторы источника и соединения, а также токен. Реализация может сгенерировать новый случайный номер пакета и зашифровать новый пакет; или может повторно использовать тот же номер пакета или просто сохранить и повторно передать тот же зашифрованный пакет.

### Общий тайм-аут

Рекомендуемое общее время ожидания для handshake составляет 20 секунд.

### Дубликаты и обработка ошибок

Дубликаты трех сообщений рукопожатия Noise Session Request, Session Created и Session Confirmed должны быть обнаружены до MixHash() заголовка. Хотя обработка Noise AEAD предположительно завершится ошибкой после этого, хеш рукопожатия уже будет поврежден.

Если любое из трех сообщений повреждено и не проходит AEAD, рукопожатие не может быть впоследствии восстановлено даже при повторной передаче, поскольку MixHash() уже был вызван для поврежденного сообщения.

## Токены

Токен в заголовке Session Request используется для предотвращения DoS-атак, защиты от подделки исходного адреса и противодействия атакам повтора.

Если Bob не принимает токен в сообщении Session Request, Bob НЕ расшифровывает сообщение, поскольку это требует дорогостоящей операции DH. Bob просто отправляет сообщение Retry с новым токеном.

Если затем получено последующее сообщение Session Request с этим токеном, Боб приступает к расшифровке этого сообщения и продолжает рукопожатие.

Токен должен быть случайно сгенерированным 8-байтным значением, если генератор токенов сохраняет значения и связанные IP-адреса и порты (в памяти или постоянно). Генератор не может создавать непрозрачные значения, например, используя SipHash (с секретным ключом K0, K1) от IP, порта и текущего часа или дня, для создания токенов, которые не нужно сохранять в памяти, поскольку этот метод затрудняет отклонение повторно используемых токенов и replay-атак. Однако это тема для дальнейшего изучения - можем ли мы перейти на такую схему, как делает [WireGuard](https://www.wireguard.com/papers/wireguard.pdf), используя 16-байтный HMAC от серверного секрета и IP-адреса.

Токены могут использоваться только один раз. Токен, отправленный от Bob к Alice в сообщении Retry, должен быть использован немедленно и истекает через несколько секунд. Токен, отправленный в блоке New Token в установленной сессии, может быть использован в последующем соединении и истекает в время, указанное в этом блоке. Время истечения указывается отправителем; рекомендуемые значения составляют минимум несколько минут, максимум один или более часов, в зависимости от желаемой максимальной нагрузки хранимых токенов.

Если IP-адрес или порт router'а изменяется, он должен удалить все сохранённые токены (как входящие, так и исходящие) для старого IP-адреса или порта, поскольку они больше не действительны. Токены могут опционально сохраняться между перезапусками router'а, в зависимости от реализации. Принятие неистёкшего токена не гарантируется; если Боб забыл или удалил свои сохранённые токены, он отправит Retry Алисе. Router может выбрать ограничение хранения токенов и удалять самые старые сохранённые токены, даже если их срок действия ещё не истёк.

Блоки New Token могут отправляться от Alice к Bob или от Bob к Alice. Обычно они отправляются как минимум один раз во время или вскоре после установления сессии. Из-за проверок валидации RouterInfo в сообщении Session Confirmed, Bob не должен отправлять блок New Token в сообщении Session Created, он может быть отправлен с ACK 0 и Router Info после получения и валидации Session Confirmed.

Поскольку время жизни сессии часто превышает время истечения токена, токен следует повторно отправить до или после истечения срока действия с новым временем истечения, или следует отправить новый токен. Router должны предполагать, что действителен только последний полученный токен; нет требования хранить несколько входящих или исходящих токенов для одного и того же IP/порта.

Токен привязан к комбинации исходного IP/порта и целевого IP/порта. Токен, полученный по IPv4, не может быть использован для IPv6 и наоборот.

Если любой из узлов мигрирует на новый IP или порт во время сессии (см. раздел "Connection Migration"), любые ранее обмененные токены становятся недействительными, и должны быть обменены новые токены.

Реализации могут, но не обязаны, сохранять токены на диск и перезагружать их при перезапуске. Если токены сохраняются, реализация должна убедиться, что IP и порт не изменились с момента завершения работы, прежде чем перезагружать их.

## Фрагментация I2NP сообщений

Отличия от SSU 1

Примечание: Как и в SSU 1, начальный фрагмент не содержит информации об общем количестве фрагментов или общей длине. Последующие фрагменты не содержат информации о своем смещении. Это предоставляет отправителю гибкость фрагментации "на лету" на основе доступного места в пакете. (Java I2P этого не делает; он выполняет "пре-фрагментацию" до отправки первого фрагмента) Однако это возлагает на получателя бремя хранения фрагментов, полученных не по порядку, и задержки сборки до получения всех фрагментов.

Как и в SSU 1, любая повторная передача фрагментов должна сохранять длину (и неявное смещение) предыдущей передачи фрагмента.

SSU 2 разделяет три случая (полное сообщение, начальный фрагмент и последующий фрагмент) на три различных типа блоков для повышения эффективности обработки.

## Дублирование I2NP сообщений

Данный протокол НЕ предотвращает полностью дублирование доставки I2NP сообщений. Дубликаты на IP-уровне или атаки повторного воспроизведения будут обнаружены на уровне SSU2, поскольку каждый номер пакета может использоваться только один раз.

Однако, когда I2NP сообщения или фрагменты повторно передаются в новых пакетах, это не обнаруживается на уровне SSU2. Маршрутизатор должен контролировать истечение срока действия I2NP (как слишком старые, так и слишком далёкие в будущем) и использовать фильтр Блума или другой механизм, основанный на идентификаторе I2NP сообщения.

Дополнительные механизмы могут использоваться router'ом или в реализации SSU2 для обнаружения дубликатов. Например, SSU2 может поддерживать кэш недавно полученных идентификаторов сообщений. Это зависит от реализации.

## Управление перегрузкой

Данная спецификация определяет протокол для нумерации пакетов и блоков ACK. Это обеспечивает достаточную информацию в реальном времени для передатчика, чтобы реализовать эффективный и отзывчивый алгоритм контроля перегрузки, при этом позволяя гибкость и инновации в этой реализации. Этот раздел обсуждает цели реализации и предоставляет предложения. Общие рекомендации можно найти в [RFC-9002](https://tools.ietf.org/html/rfc9002). См. также [RFC-6298](https://tools.ietf.org/html/rfc6298) для получения рекомендаций по таймерам повторной передачи.

Пакеты данных только с ACK не должны учитываться в байтах или пакетах в полёте и не подлежат контролю перегрузки. В отличие от TCP, SSU2 может обнаружить потерю таких пакетов, и эта информация может использоваться для корректировки состояния перегрузки. Однако данный документ не определяет механизм для этого.

Пакеты, содержащие некоторые другие блоки, не являющиеся данными, также могут быть исключены из управления перегрузкой при желании, в зависимости от реализации. Например:

- Тест узла
- Запрос/представление/ответ relay
- Вызов/ответ пути

Рекомендуется, чтобы управление перегрузкой основывалось на подсчете байтов, а не пакетов, следуя руководящим принципам в RFC для TCP и QUIC [RFC-9002](https://tools.ietf.org/html/rfc9002). Дополнительное ограничение по количеству пакетов также может быть полезным для предотвращения переполнения буфера в ядре или в промежуточных устройствах, в зависимости от реализации, хотя это может значительно усложнить систему. Если вывод пакетов на сеанс и/или общий вывод пакетов ограничен по пропускной способности и/или регулируется по времени, это может снизить потребность в ограничении количества пакетов.

### Номера пакетов

В SSU 1 подтверждения (ACK) и отрицательные подтверждения (NACK) содержали номера I2NP сообщений и битовые маски фрагментов. Передатчики отслеживали статус подтверждений исходящих сообщений (и их фрагментов) и повторно передавали фрагменты по мере необходимости.

В SSU 2 ACK и NACK содержат номера пакетов. Передатчики должны поддерживать структуру данных с отображением номеров пакетов на их содержимое. Когда пакет получает ACK или NACK, передатчик должен определить, какие I2NP сообщения и фрагменты находились в этом пакете, чтобы решить, что повторно передавать.

### Подтверждение установленной сессии

Bob отправляет ACK пакета 0, который подтверждает получение сообщения Session Confirmed и позволяет Alice перейти к фазе передачи данных, а также удалить большое сообщение Session Confirmed, сохраняемое для возможной повторной передачи. Это заменяет DeliveryStatusMessage, отправляемое Bob в SSU 1.

Bob должен отправить ACK как можно скорее после получения сообщения Session Confirmed. Небольшая задержка (не более 50 мс) допустима, поскольку как минимум одно сообщение Data должно прибыть почти сразу после сообщения Session Confirmed, чтобы ACK мог подтвердить как Session Confirmed, так и сообщение Data. Это предотвратит необходимость Bob повторно передавать сообщение Session Confirmed.

### Генерация подтверждений (ACK)

Определение: Пакеты, вызывающие подтверждение: Пакеты, содержащие блоки, вызывающие подтверждение, требуют ACK от получателя в течение максимальной задержки подтверждения и называются пакетами, вызывающими подтверждение.

Маршрутизаторы подтверждают все пакеты, которые они получают и обрабатывают. Однако только пакеты, требующие подтверждения, вызывают отправку блока ACK в течение максимальной задержки подтверждения. Пакеты, которые не требуют подтверждения, подтверждаются только тогда, когда блок ACK отправляется по другим причинам.

При отправке пакета по любой причине конечная точка должна попытаться включить блок ACK, если он не отправлялся недавно. Это помогает своевременному обнаружению потерь на стороне узла.

В общем, частая обратная связь от получателя улучшает реакцию на потери и перегрузки, но это необходимо сбалансировать с чрезмерной нагрузкой, создаваемой получателем, который отправляет блок ACK в ответ на каждый пакет, требующий подтверждения. Приведенные ниже рекомендации направлены на достижение этого баланса.

Пакеты данных в сессии, содержащие любой блок, ЗА ИСКЛЮЧЕНИЕМ следующих, требуют подтверждения:

- ACK блок
- Address блок
- DateTime блок
- Padding блок
- Termination блок
- Другие?

Пакеты вне сессии, включая сообщения рукопожатия и сообщения тестирования пиров 5-7, имеют свои собственные механизмы подтверждения. См. ниже.

### ACK подтверждения рукопожатия

Это особые случаи:

- Запрос токена неявно подтверждается сообщением Retry
- Запрос сессии неявно подтверждается сообщениями Session Created или Retry
- Retry неявно подтверждается сообщением Session Request
- Session Created неявно подтверждается сообщением Session Confirmed
- Session Confirmed должно быть подтверждено немедленно

### Отправка блоков ACK

Блоки ACK используются для подтверждения пакетов фазы данных. Они должны включаться только для пакетов фазы данных внутри сессии.

Каждый пакет должен быть подтвержден по крайней мере один раз, а пакеты, требующие подтверждения, должны быть подтверждены по крайней мере один раз в течение максимальной задержки.

Конечная точка должна немедленно подтверждать все пакеты handshake, требующие подтверждения, в пределах своей максимальной задержки, за следующим исключением. До подтверждения handshake конечная точка может не иметь ключей шифрования заголовка пакета для расшифровки пакетов при их получении. Поэтому она может буферизировать их и подтверждать, когда необходимые ключи станут доступными.

Поскольку пакеты, содержащие только ACK блоки, не подвергаются контролю перегрузки, конечная точка не должна отправлять более одного такого пакета в ответ на получение пакета, требующего подтверждения.

Конечная точка не должна отправлять пакет, не требующий подтверждения, в ответ на пакет, не требующий подтверждения, даже если есть пропуски в пакетах, предшествующих полученному пакету. Это позволяет избежать бесконечного цикла обратной связи подтверждений, который может помешать соединению когда-либо стать неактивным. Пакеты, не требующие подтверждения, в конечном итоге подтверждаются, когда конечная точка отправляет блок ACK в ответ на другие события.

Конечная точка, которая отправляет только блоки ACK, не будет получать подтверждения от своего узла-партнера, если только эти подтверждения не включены в пакеты с блоками, требующими подтверждения. Конечная точка должна отправлять блок ACK с другими блоками, когда есть новые пакеты, требующие подтверждения, которые нужно подтвердить. Когда нужно подтвердить только пакеты, не требующие подтверждения, конечная точка МОЖЕТ выбрать не отправлять блок ACK с исходящими блоками до тех пор, пока не будет получен пакет, требующий подтверждения.

Конечная точка, которая отправляет только пакеты, не требующие подтверждения, может периодически добавлять блок, требующий подтверждения, к таким пакетам, чтобы гарантировать получение подтверждения. В этом случае конечная точка НЕ ДОЛЖНА отправлять блок, требующий подтверждения, во всех пакетах, которые иначе не требовали бы подтверждения, чтобы избежать бесконечного цикла обратной связи подтверждений.

Чтобы помочь отправителю обнаружить потери, конечная точка должна генерировать и отправлять блок ACK без задержки при получении пакета, требующего подтверждения, в любом из следующих случаев:

- Когда полученный пакет имеет номер пакета меньше другого пакета, требующего подтверждения, который уже был получен
- Когда пакет имеет номер пакета больше самого высокого номера пакета, требующего подтверждения, который был получен, и есть отсутствующие пакеты между тем пакетом и этим пакетом
- Когда установлен флаг ack-immediate в заголовке пакета

Ожидается, что алгоритмы будут устойчивы к получателям, которые не следуют приведенным выше рекомендациям. Однако реализация должна отклоняться от этих требований только после тщательного рассмотрения влияния изменений на производительность — как для соединений, устанавливаемых конечной точкой, так и для других пользователей сети.

### Частота ACK

Получатель определяет, как часто отправлять подтверждения в ответ на пакеты, требующие подтверждения. Это решение включает в себя компромисс.

Конечные точки полагаются на своевременное подтверждение для обнаружения потерь. Контроллеры перегрузки, основанные на окне, полагаются на подтверждения для управления своим окном перегрузки. В обоих случаях задержка подтверждений может негативно повлиять на производительность.

С другой стороны, уменьшение частоты пакетов, которые содержат только подтверждения, снижает стоимость передачи и обработки пакетов на обеих конечных точках. Это может улучшить пропускную способность соединения на сильно асимметричных каналах и уменьшить объем трафика подтверждений, использующего пропускную способность обратного пути; см. Раздел 3 [RFC-3449](https://tools.ietf.org/html/rfc3449).

Получатель должен отправлять блок ACK после получения как минимум двух пакетов, требующих подтверждения. Эта рекомендация носит общий характер и согласуется с рекомендациями для поведения конечных точек TCP [RFC-5681](https://tools.ietf.org/html/rfc5681). Знание сетевых условий, знание контроллера перегрузки узла или дальнейшие исследования и эксперименты могут предложить альтернативные стратегии подтверждения с лучшими характеристиками производительности.

Получатель может обработать несколько доступных пакетов, прежде чем определить, следует ли отправлять блок ACK в ответ. В общем случае получатель не должен задерживать ACK более чем на RTT / 6 или максимум 150 мс.

Флаг ack-immediate в заголовке пакета данных является запросом получателю отправить подтверждение вскоре после получения, вероятно, в течение нескольких миллисекунд. В общем случае получатель не должен задерживать немедленное ACK более чем на RTT / 16, или максимум на 5 мс.

### Флаг немедленного ACK

Получатель не знает размер окна отправки отправителя и поэтому не знает, как долго задерживать отправку ACK. Флаг немедленного ACK в заголовке пакета данных является важным способом поддержания максимальной пропускной способности путем минимизации эффективного RTT. Флаг немедленного ACK находится в байте 13 заголовка, бит 0, то есть (header[13] & 0x01). Когда установлен, запрашивается немедленный ACK. Подробности см. в разделе о коротком заголовке выше.

Существует несколько возможных стратегий, которые отправитель может использовать для определения того, когда устанавливать флаг immediate-ack:

- Устанавливается один раз на каждые N пакетов, для некоторого небольшого N
- Устанавливается на последнем пакете в серии пакетов
- Устанавливается когда окно отправки почти заполнено, например заполнено более чем на 2/3
- Устанавливается на всех пакетах с повторно переданными фрагментами

Флаги немедленного ACK должны быть необходимы только для пакетов данных, содержащих I2NP сообщения или фрагменты сообщений.

### Размер блока ACK

Когда отправляется блок ACK, включается один или несколько диапазонов подтвержденных пакетов. Включение подтверждений для более старых пакетов снижает вероятность ложных повторных передач, вызванных потерей ранее отправленных блоков ACK, за счет увеличения размера блоков ACK.

Блоки ACK всегда должны подтверждать самые недавно полученные пакеты, и чем больше пакеты не по порядку, тем важнее быстро отправить обновленный блок ACK, чтобы предотвратить объявление узлом пакета потерянным и ложную повторную передачу содержащихся в нем блоков. Блок ACK должен помещаться в один пакет. Если это не так, то более старые диапазоны (те, что с наименьшими номерами пакетов) опускаются.

Получатель ограничивает количество диапазонов ACK, которые он запоминает и отправляет в блоках ACK, как для ограничения размера блоков ACK, так и для предотвращения истощения ресурсов. После получения подтверждений для блока ACK получатель должен прекратить отслеживание этих подтвержденных диапазонов ACK. Отправители могут ожидать подтверждений для большинства пакетов, но данный протокол не гарантирует получение подтверждения для каждого пакета, который обрабатывает получатель.

Возможно, что сохранение множества диапазонов ACK может привести к тому, что блок ACK станет слишком большим. Получатель может отбросить неподтвержденные диапазоны ACK для ограничения размера блока ACK, что приведет к увеличению повторных передач от отправителя. Это необходимо, если блок ACK будет слишком большим для размещения в пакете. Получатели также могут дополнительно ограничивать размер блока ACK для сохранения места для других блоков или для ограничения пропускной способности, потребляемой подтверждениями.

Получатель должен сохранять диапазон ACK, если он не может гарантировать, что впоследствии не будет принимать пакеты с номерами из этого диапазона. Поддержание минимального номера пакета, который увеличивается по мере отбрасывания диапазонов, является одним из способов достижения этого с минимальным состоянием.

Получатели могут отбросить все диапазоны ACK, но они должны сохранить наибольший номер пакета, который был успешно обработан, поскольку он используется для восстановления номеров пакетов из последующих пакетов.

Следующий раздел описывает примерный подход для определения того, какие пакеты подтверждать в каждом ACK блоке. Хотя цель этого алгоритма состоит в генерации подтверждения для каждого обработанного пакета, подтверждения все еще могут быть потеряны.

### Ограничение диапазонов путем отслеживания блоков ACK

Когда отправляется пакет, содержащий блок ACK, поле Ack Through в этом блоке может быть сохранено. Когда пакет, содержащий блок ACK, подтверждается, получатель может прекратить подтверждение пакетов, меньших или равных полю Ack Through в отправленном блоке ACK.

Получатель, который отправляет только пакеты, не требующие подтверждения, такие как блоки ACK, может не получать подтверждения в течение длительного времени. Это может привести к тому, что получатель будет поддерживать состояние для большого количества блоков ACK в течение длительного периода, и отправляемые им блоки ACK могут быть излишне большими. В таком случае получатель может периодически отправлять PING или другой небольшой блок, требующий подтверждения, например, один раз за цикл передачи, чтобы получить ACK от узла.

В случаях без потери блоков ACK этот алгоритм допускает минимум 1 RTT переупорядочивания. В случаях с потерей блоков ACK и переупорядочиванием этот подход не гарантирует, что каждое подтверждение будет увидено отправителем до того, как оно больше не будет включено в блок ACK. Пакеты могут быть получены в неправильном порядке, и все последующие блоки ACK, содержащие их, могут быть потеряны. В этом случае алгоритм восстановления после потерь может вызвать ложные повторные передачи, но отправитель продолжит продвигаться вперед.

### Перегрузка

Транспорты I2P не гарантируют доставку I2NP сообщений в порядке их отправки. Поэтому потеря Data сообщения, содержащего одно или несколько I2NP сообщений или фрагментов, НЕ препятствует доставке других I2NP сообщений; отсутствует блокировка головы очереди. Реализации должны продолжать отправку новых сообщений во время фазы восстановления после потерь, если окно отправки это позволяет.

### Повторная передача

Отправитель не должен сохранять полное содержимое сообщения для идентичной повторной передачи (за исключением сообщений handshake, см. выше). Отправитель должен собирать сообщения, содержащие актуальную информацию (ACK, NACK и неподтвержденные данные) каждый раз при отправке сообщения. Отправитель должен избегать повторной передачи информации из сообщений после их подтверждения. Это включает сообщения, которые подтверждаются после объявления потерянными, что может происходить при изменении порядка пакетов в сети.

### Окно

Подлежит определению. Общие рекомендации можно найти в [RFC-9002](https://tools.ietf.org/html/rfc9002).

## Миграция соединений

IP-адрес или порт узла могут измениться в течение жизненного цикла сессии. Изменение IP может быть вызвано ротацией временных адресов IPv6, периодическим изменением IP провайдером, переходом мобильного клиента между WiFi и сотовыми IP-адресами или другими изменениями в локальной сети. Изменение порта может быть вызвано повторной привязкой NAT после истечения времени предыдущей привязки.

IP-адрес или порт пира могут казаться изменившимися из-за различных атак на пути передачи данных и вне его, включая модификацию или внедрение пакетов.

Миграция соединения — это процесс, при котором проверяется новая исходная конечная точка (IP+порт), предотвращая изменения, которые не прошли проверку. Этот процесс представляет собой упрощенную версию процесса, определенного в QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000). Данный процесс определен только для фазы передачи данных сессии. Миграция не разрешена во время handshake (процедуры установления соединения). Все пакеты handshake должны быть проверены на то, что они отправлены с того же IP и порта, что и ранее отправленные и полученные пакеты. Другими словами, IP и порт узла должны оставаться постоянными во время handshake.

### Модель угроз

(Адаптировано из QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000))

#### Подмена адреса пира

Узел может подделать свой исходный адрес, чтобы заставить конечную точку отправлять чрезмерное количество данных нежелающему хосту. Если конечная точка отправляет значительно больше данных, чем подделывающий узел, миграция соединения может быть использована для усиления объема данных, который злоумышленник может генерировать в сторону жертвы.

#### Подмена адреса на маршруте

Атакующий, находящийся на пути передачи данных, может вызвать ложную миграцию соединения, скопировав и переправив пакет с подделанным адресом таким образом, чтобы он прибыл раньше оригинального пакета. Пакет с подделанным адресом будет восприниматься как исходящий от мигрирующего соединения, а оригинальный пакет будет рассматриваться как дубликат и отброшен. После ложной миграции проверка адреса источника завершится неудачей, поскольку объект по адресу источника не имеет необходимых криптографических ключей для чтения или ответа на Path Challenge, который ему отправляется, даже если бы он этого хотел.

#### Пересылка пакетов вне маршрута

Атакующий вне пути передачи данных, который может наблюдать пакеты, может пересылать копии подлинных пакетов конечным точкам. Если скопированный пакет прибудет раньше подлинного пакета, это будет выглядеть как NAT rebinding. Любой подлинный пакет будет отброшен как дубликат. Если атакующий сможет продолжать пересылку пакетов, он может вызвать миграцию на путь через атакующего. Это помещает атакующего на путь передачи данных, предоставляя ему возможность наблюдать или отбрасывать все последующие пакеты.

#### Последствия для приватности

QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) предписывает изменение идентификаторов соединения при смене сетевых путей. Использование стабильного идентификатора соединения на нескольких сетевых путях позволило бы пассивному наблюдателю коррелировать активность между этими путями. Конечная точка, перемещающаяся между сетями, может не желать, чтобы её активность коррелировалась каким-либо субъектом, кроме её узла-партнёра. Однако QUIC не шифрует идентификаторы соединения в заголовке. SSU2 это делает, поэтому утечка приватности потребует от пассивного наблюдателя также иметь доступ к базе данных сети для получения introduction key (ключа представления), необходимого для расшифровки идентификатора соединения. Даже имея introduction key, это не является сильной атакой, и мы не изменяем идентификаторы соединения после миграции в SSU2, поскольку это было бы значительным усложнением.

### Инициация валидации пути

Во время фазы данных узлы должны проверять исходный IP-адрес и порт каждого получаемого пакета данных. Если IP-адрес или порт отличается от ранее полученных, И пакет не является дубликатом по номеру, И пакет успешно расшифровывается, то сессия переходит в фазу валидации пути.

Кроме того, peer должен проверить, что новый IP и порт действительны согласно локальным правилам валидации (не заблокированы, не запрещенные порты и т.д.). Peer-ы НЕ обязаны поддерживать миграцию между IPv4 и IPv6, и могут считать новый IP из другого семейства адресов недействительным, поскольку это неожиданное поведение и может добавить значительную сложность реализации. При получении пакета с недействительного IP/порта, реализация может просто отбросить его, или может инициировать валидацию пути со старым IP/портом.

При входе в фазу валидации пути выполните следующие шаги:

- Запустить таймер тайм-аута валидации пути на несколько секунд или несколько значений текущего RTO (TBD)
- Уменьшить окно перегрузки до минимума
- Уменьшить PMTU до минимума (1280)
- Отправить пакет данных, содержащий блок Path Challenge, блок Address (содержащий новый IP/порт) и, как правило, блок ACK, на новый IP и порт. Этот пакет использует тот же connection ID и ключи шифрования, что и текущая сессия. Данные блока Path Challenge должны содержать достаточную энтропию (не менее 8 байт), чтобы их нельзя было подделать.
- Опционально также отправить Path Challenge на старый IP/порт с другими данными блока. См. ниже.
- Запустить таймер тайм-аута Path Response на основе текущего RTO (обычно RTT + кратное значение RTTdev)

Во время фазы валидации пути сессия может продолжать обрабатывать входящие пакеты. Как со старого, так и с нового IP/порта. Сессия также может продолжать отправлять и подтверждать пакеты данных. Однако окно перегрузки и PMTU должны оставаться на минимальных значениях во время фазы валидации пути, чтобы предотвратить использование для атак отказа в обслуживании путем отправки большого количества трафика на поддельный адрес.

Реализация может, но не обязана, пытаться одновременно валидировать несколько путей. Это, вероятно, не стоит усложнения. Она может, но не обязана, запоминать предыдущий IP/порт как уже проверенный и пропускать валидацию пути, если пир возвращается к своему предыдущему IP/порту.

Если получен Path Response, содержащий идентичные данные, отправленные в Path Challenge, то проверка пути прошла успешно. Исходный IP/порт сообщения Path Response не обязательно должен совпадать с тем, куда был отправлен Path Challenge.

Если Path Response не получен до истечения таймера Path Response, отправить другой Path Challenge и удвоить таймер Path Response.

Если Path Response не получен до истечения таймера Path Validation, проверка пути завершилась неудачей.

### Содержимое сообщения

Сообщения Data должны содержать следующие блоки. Порядок не определен, за исключением того, что Padding должен быть последним:

- Блок Path Challenge или Path Response. Path Challenge содержит непрозрачные данные, рекомендуется минимум 8 байт. Path Response содержит данные из Path Challenge.
- Блок Address, содержащий видимый IP получателя
- Блок DateTime
- Блок ACK
- Блок Padding

Не рекомендуется включать в сообщение какие-либо другие блоки (например, I2NP).

Разрешается включать блок Path Challenge в сообщение, содержащее Path Response, чтобы инициировать проверку в обратном направлении.

Блоки Path Challenge и Path Response вызывают подтверждение (ACK-eliciting). Path Challenge будет подтвержден сообщением Data, содержащим блоки Path Response и ACK. Path Response должен быть подтвержден сообщением Data, содержащим блок ACK.

### Маршрутизация во время валидации пути

Спецификация QUIC не ясно указывает, куда отправлять пакеты данных во время валидации пути - на старый или новый IP/порт? Необходимо найти баланс между быстрым реагированием на изменения IP/порта и недопущением отправки трафика на поддельные адреса. Также поддельные пакеты не должны существенно влиять на существующую сессию. Изменения только порта, вероятно, вызваны повторной привязкой NAT после периода простоя; изменения IP могут происходить во время фаз высокого трафика в одном или обоих направлениях.

Стратегии подлежат исследованию и доработке. Возможности включают:

- Не отправлять пакеты данных на новый IP/порт до валидации
- Продолжать отправку пакетов данных на старый IP/порт до валидации нового IP/порта
- Одновременно перевалидировать старый IP/порт
- Не отправлять никаких данных до валидации старого или нового IP/порта
- Различные стратегии для изменения только порта по сравнению с изменением IP
- Различные стратегии для изменения IPv6 в том же /32, вероятно вызванного ротацией временных адресов

### Ответ на Path Challenge

При получении Path Challenge узел должен ответить пакетом данных, содержащим Path Response, с данными из Path Challenge.

Path Response должен быть отправлен на IP/порт, с которого был получен Path Challenge. Это НЕ ОБЯЗАТЕЛЬНО тот IP/порт, который был ранее установлен для узла. Это гарантирует, что валидация пути узлом успешна только в том случае, если путь функционален в обоих направлениях. См. раздел "Валидация после локального изменения" ниже.

Если IP/порт отличается от ранее известного IP/порта для пира, обрабатывайте Path Challenge как простой пинг и просто отвечайте безусловно с помощью Path Response. Получатель не сохраняет и не изменяет какое-либо состояние на основе полученного Path Challenge. Если IP/порт отличается, пир должен проверить, что новый IP и порт являются действительными согласно локальным правилам валидации (не заблокированы, не являются запрещенными портами и т.д.). Пиры НЕ обязаны поддерживать ответы между адресными семействами IPv4 и IPv6, и могут рассматривать новый IP в другом адресном семействе как недействительный, поскольку такое поведение не ожидается.

Если это не ограничено контролем перегрузки, Path Response должен быть отправлен немедленно. Реализации должны принимать меры для ограничения скорости отправки Path Response или используемой пропускной способности при необходимости.

Блок Path Challenge обычно сопровождается блоком Address в том же сообщении. Если блок адреса содержит новый IP/порт, peer может проверить этот IP/порт и инициировать тестирование peer'а для этого нового IP/порта с сессионным peer'ом или любым другим peer'ом. Если peer считает, что он находится за firewall, и изменился только порт, это изменение, вероятно, вызвано NAT rebinding, и дальнейшее тестирование peer'а, скорее всего, не требуется.

### Успешная проверка пути

При успешной валидации пути соединение полностью мигрирует на новый IP/порт. В случае успеха:

- Выйти из фазы валидации пути
- Все пакеты отправляются на новый IP и порт.
- Ограничения на окно перегрузки и PMTU снимаются, и им разрешается увеличиваться. Не просто восстанавливайте их до старых значений, поскольку новый путь может иметь другие характеристики.
- Если IP изменился, установите рассчитанные RTT и RTO в начальные значения. Поскольку изменения только порта обычно являются результатом NAT rebinding или другой активности промежуточных устройств, узел может вместо этого сохранить своё состояние контроля перегрузки и оценку времени прохождения сигнала в таких случаях вместо возврата к начальным значениям.
- Удалить (аннулировать) любые токены, отправленные или полученные для старого IP/порта (необязательно)
- Отправить новый блок токенов для нового IP/порта (необязательно)

### Отмена валидации пути

Во время фазы валидации пути любые валидные, неповторяющиеся пакеты, полученные со старого IP/порта и успешно расшифрованные, приведут к отмене валидации пути. Важно, чтобы отмененная валидация пути, вызванная поддельным пакетом, не приводила к завершению или значительному нарушению работы валидной сессии.

При отменённой валидации пути:

- Выйти из фазы валидации пути
- Все пакеты отправляются на старый IP и порт.
- Ограничения на окно перегрузки и PMTU снимаются, и им разрешается увеличиваться, или, опционально, восстановить предыдущие значения
- Повторно передать любые пакеты данных, которые ранее были отправлены на новый IP/порт, на старый IP/порт.

### Ошибка проверки пути

Важно, чтобы неудачная проверка пути, вызванная поддельным пакетом, не приводила к завершению или существенному нарушению работы действительной сессии.

При неудачной проверке пути:

- Выйти из фазы валидации пути
- Все пакеты отправляются на старый IP и порт.
- Ограничения на окно перегрузки и PMTU снимаются, и им разрешается увеличиваться.
- Опционально, запустить валидацию пути на старом IP и порту. Если она не удается, завершить сессию.
- В противном случае, следовать стандартным правилам тайм-аута и завершения сессии.
- Повторно передать любые пакеты данных, которые ранее были отправлены на новый IP/порт, на старый IP/порт.

### Проверка после локального изменения

Описанный выше процесс определен для peer'ов, которые получают пакет с измененного IP/порта. Однако он также может быть инициирован в обратном направлении peer'ом, который обнаруживает, что его IP или порт изменились. Peer может определить, что его локальный IP изменился; однако гораздо менее вероятно, что он обнаружит изменение порта из-за переназначения NAT. Поэтому это необязательно.

При получении path challenge от узла, у которого изменился IP или порт, другой узел должен инициировать path challenge в обратном направлении.

### Использовать как Ping/Pong

Блоки Path Challenge и Path Response могут использоваться в любое время как пакеты Ping/Pong. Получение блока Path Challenge не изменяет никакого состояния у получателя, если только он не получен с другого IP/порта.

## Множественные сессии

Узлы не должны устанавливать несколько сессий с одним и тем же узлом, будь то SSU 1 или 2, или с одинаковыми или разными IP-адресами. Однако это может произойти либо из-за ошибок, либо из-за потери сообщения о завершении предыдущей сессии, либо в условиях гонки, когда сообщение о завершении еще не поступило.

Если у Боба есть существующая сессия с Алисой, когда Боб получает Session Confirmed от Алисы, завершая handshake и устанавливая новую сессию, Боб должен:

- Перенести все неотправленные или неподтвержденные исходящие I2NP сообщения со старой сессии на новую
- Отправить завершение с кодом причины 22 на старой сессии
- Удалить старую сессию и заменить её новой

## Завершение сессии

### Фаза установления соединения

Сессии в фазе handshake обычно завершаются просто по тайм-ауту или отсутствию дальнейшего ответа. По желанию они могут быть завершены путем включения блока Termination в ответ, но на большинство ошибок невозможно ответить из-за отсутствия криптографических ключей. Даже если ключи доступны для ответа, включающего блок termination, обычно не стоит тратить CPU на выполнение DH для ответа. Исключением МОЖЕТ быть блок Termination в сообщении повторной попытки, которое недорого генерировать.

### Фаза данных

Сессии в фазе данных завершаются отправкой сообщения данных, которое включает блок Termination. Это сообщение также должно включать блок ACK. Оно может, если сессия была активна достаточно долго, чтобы ранее отправленный токен истек или вот-вот истечет, включать блок New Token. Это сообщение не требует подтверждения. При получении блока Termination с любой причиной, кроме "Termination Received", узел отвечает сообщением данных, содержащим блок Termination с причиной "Termination Received".

После отправки или получения блока Termination сессия должна войти в фазу закрытия на некоторый максимальный период времени (TBD). Состояние закрытия необходимо для защиты от потери пакета, содержащего блок Termination, и пакетов в полёте в противоположном направлении. Находясь в фазе закрытия, не требуется обрабатывать любые дополнительные полученные пакеты. Сессия в состоянии закрытия отправляет пакет, содержащий блок Termination, в ответ на любой входящий пакет, который она относит к данной сессии. Сессия должна ограничивать скорость, с которой она генерирует пакеты в состоянии закрытия. Например, сессия может ждать прогрессивно увеличивающегося количества полученных пакетов или времени перед ответом на полученные пакеты.

Чтобы минимизировать состояние, которое router поддерживает для закрывающейся сессии, сессии могут, но не обязаны, отправлять точно такой же пакет с тем же номером пакета как есть в ответ на любой полученный пакет. Примечание: Разрешение повторной передачи пакета завершения является исключением из требования использовать новый номер пакета для каждого пакета. Отправка новых номеров пакетов в первую очередь выгодна для восстановления потерь и контроля перегрузки, которые не ожидаются как релевантные для закрытого соединения. Повторная передача финального пакета требует меньше состояния.

После получения блока Termination с причиной "Termination Received", сессия может выйти из фазы закрытия.

### Очистка

При любом нормальном или аварийном завершении работы router должен обнулить все временные данные в памяти, включая временные ключи handshake, симметричные криптографические ключи и связанную информацию.

## MTU

Требования варьируются в зависимости от того, используется ли опубликованный адрес совместно с SSU 1. Текущий минимум SSU 1 для IPv4 составляет 620, что определенно слишком мало.

Минимальный MTU SSU2 составляет 1280 для IPv4 и IPv6, что соответствует спецификации в [RFC-9000](https://tools.ietf.org/html/rfc9000). См. ниже. Увеличение минимального MTU позволяет поместить tunnel сообщения размером 1 КБ и короткие tunnel build сообщения в одну датаграмму, что значительно сокращает типичную фрагментацию. Это также позволяет увеличить максимальный размер I2NP сообщений. Потоковые сообщения размером 1820 байт должны помещаться в две датаграммы.

Router не должен включать SSU2 или публиковать SSU2-адрес, если MTU для этого адреса составляет менее 1280.

Роутеры должны публиковать нестандартный MTU в каждом SSU или SSU2 адресе роутера.

### SSU адрес

Общий адрес с SSU 1, должен следовать правилам SSU 1. IPv4: По умолчанию и максимум составляет 1484. Минимум — 1292. (IPv4 MTU + 4) должно быть кратно 16. IPv6: Должно быть опубликовано, минимум — 1280, максимум — 1488. IPv6 MTU должно быть кратно 16.

### SSU2 Адрес

IPv4: По умолчанию и максимум 1500. Минимум 1280. IPv6: По умолчанию и максимум 1500. Минимум 1280. Нет правил кратности 16, но должно быть кратным 2 как минимум.

### Обнаружение PMTU

Для SSU 1 текущая Java I2P выполняет обнаружение PMTU, начиная с небольших пакетов и постепенно увеличивая размер, или увеличивая на основе размера полученного пакета. Это грубый метод, который значительно снижает эффективность. Продолжение этой функции в SSU 2 пока не определено.

Недавние исследования [PMTU](https://en.wikipedia.org/wiki/Path_MTU_Discovery) показывают, что минимальный размер для IPv4 в 1200 или более байт будет работать для более чем 99% соединений. QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) требует минимальный размер IP-пакета в 1280 байт.

цитата [RFC-9000](https://tools.ietf.org/html/rfc9000):

Максимальный размер датаграммы определяется как наибольший размер полезной нагрузки UDP, который может быть отправлен по сетевому пути с помощью одной UDP датаграммы. QUIC НЕ ДОЛЖЕН использоваться, если сетевой путь не может поддерживать максимальный размер датаграммы не менее 1200 байт.

QUIC предполагает минимальный размер IP-пакета не менее 1280 байт. Это минимальный размер для IPv6 [IPv6], который также поддерживается большинством современных IPv4-сетей. Учитывая минимальный размер IP-заголовка 40 байт для IPv6 и 20 байт для IPv4 и размер UDP-заголовка 8 байт, это приводит к максимальному размеру датаграммы 1232 байта для IPv6 и 1252 байта для IPv4. Таким образом, ожидается, что современные IPv4 и все IPv6 сетевые пути смогут поддерживать QUIC.

Примечание: Это требование поддержки UDP полезной нагрузки размером 1200 байт ограничивает доступное пространство для заголовков расширения IPv6 до 32 байт или опций IPv4 до 52 байт, если путь поддерживает только минимальный MTU IPv6 в 1280 байт. Это влияет на Initial пакеты и валидацию пути.

конец цитаты

### Минимальный размер рукопожатия

QUIC требует, чтобы начальные дейтаграммы в обоих направлениях были не менее 1200 байт, чтобы предотвратить атаки усиления и гарантировать, что PMTU поддерживает это в обоих направлениях.

Мы могли бы требовать это для Session Request и Session Created за счёт значительного увеличения пропускной способности. Возможно, мы могли бы делать это только если у нас нет токена, или после получения сообщения Retry. Требует дальнейшего рассмотрения

QUIC требует, чтобы Боб отправлял не более чем в три раза больше данных, чем получено, пока адрес клиента не будет проверен. SSU2 изначально соответствует этому требованию, поскольку сообщение Retry примерно такого же размера, как сообщение Token Request, и меньше сообщения Session Request. Кроме того, сообщение Retry отправляется только один раз.

### Минимальный размер сообщения пути

QUIC требует, чтобы сообщения, содержащие блоки PATH_CHALLENGE или PATH_RESPONSE, были не менее 1200 байт, чтобы предотвратить атаки усиления и обеспечить поддержку PMTU в обоих направлениях.

Мы могли бы потребовать и это, но за счет существенного увеличения использования пропускной способности. Однако такие случаи должны быть редкими. TBD

### Максимальный размер I2NP сообщения

IPv4: Фрагментация IP не предполагается. Заголовок IP + датаграммы составляет 28 байт. Это предполагает отсутствие опций IPv4. Максимальный размер сообщения равен MTU - 28. Заголовок фазы данных составляет 16 байт, а MAC — 16 байт, всего 32 байта. Размер полезной нагрузки равен MTU - 60. Максимальная полезная нагрузка фазы данных составляет 1440 для максимального MTU 1500. Максимальная полезная нагрузка фазы данных составляет 1220 для минимального MTU 1280.

IPv6: Фрагментация IP не допускается. Заголовок IP + датаграммы составляет 48 байт. Это предполагает отсутствие расширенных заголовков IPv6. Максимальный размер сообщения равен MTU - 48. Заголовок фазы данных составляет 16 байт, а MAC - 16 байт, что в общей сложности составляет 32 байта. Размер полезной нагрузки равен MTU - 80. Максимальная полезная нагрузка фазы данных составляет 1420 для максимального MTU 1500. Максимальная полезная нагрузка фазы данных составляет 1200 для минимального MTU 1280.

В SSU 1 рекомендации устанавливали строгий максимум около 32 КБ для I2NP сообщения на основе 64 максимальных фрагментов и минимального MTU 620. Из-за накладных расходов на связанные leaseSet и ключи сессии практический лимит на уровне приложения был примерно на 6 КБ ниже, или около 26 КБ. Протокол SSU 1 позволяет использовать 128 фрагментов, но текущие реализации ограничивают это 64 фрагментами.

Повышая минимальный MTU до 1280, с полезной нагрузкой фазы данных около 1200, сообщение SSU 2 размером примерно 76 КБ возможно в 64 фрагментах и 152 КБ в 128 фрагментах. Это легко позволяет максимум 64 КБ.

Из-за фрагментации в tunnel и фрагментации в SSU 2, вероятность потери сообщений экспоненциально возрастает с увеличением размера сообщения. Мы по-прежнему рекомендуем практический лимит около 10 КБ на прикладном уровне для I2NP дейтаграмм.

## Процесс проверки пиров

См. раздел "Безопасность тестирования узлов" выше для анализа SSU1 Peer Test и целей SSU2 Peer Test.

```
Alice Bob Charlie

1.  

        PeerTest ------------------->

        :   Alice RI ------------------->

    2.  PeerTest ------------------->

    3\. <------------------ PeerTest

    :   <---------------- Charlie RI

    4.  <------------------ PeerTest
    5.  <----------------------------------------- PeerTest
    6.  PeerTest ----------------------------------------->
    7.  <----------------------------------------- PeerTest
```
Когда отклонено Бобом:

```
Alice Bob Charlie

1.  PeerTest ------------------->
    2.  <------------------ PeerTest (reject)
```
Когда отклонено Charlie:

```
Alice Bob Charlie

1.  

        PeerTest ------------------->

        :   Alice RI ------------------->

    2.  PeerTest ------------------->

    3\. <------------------ PeerTest (reject)

    :   (optional: Bob could try another Charlie here)

    4.  <------------------ PeerTest (reject)
```
ПРИМЕЧАНИЕ: RI может отправляться либо в сообщениях I2NP Database Store в блоках I2NP, либо как блоки RI (если достаточно маленькие). Они могут содержаться в тех же пакетах, что и блоки peer test, если достаточно маленькие.

Сообщения 1-4 находятся в рамках сессии и используют блоки Peer Test в сообщении Data. Сообщения 5-7 находятся вне сессии и используют блоки Peer Test в сообщении Peer Test.

ПРИМЕЧАНИЕ: Как и в SSU 1, сообщения 4 и 5 могут прибыть в любом порядке. Сообщение 5 и/или 7 могут вообще не быть получены, если Alice находится за firewall. Когда сообщение 5 прибывает раньше сообщения 4, Alice не может немедленно отправить сообщение 6, потому что у неё ещё нет intro key Чарли для шифрования заголовка. Когда сообщение 4 прибывает раньше сообщения 5, Alice не должна немедленно отправлять сообщение 6, потому что ей следует подождать и посмотреть, не прибудет ли сообщение 5 без открытия firewall с помощью сообщения 6.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Path</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Intro Key</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->C session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->A session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->C</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
  </tbody>
</table>
### Версии

Тестирование peer'ов между разными версиями не поддерживается. Единственно допустимая комбинация версий - когда все peer'ы используют версию 2.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### Повторные передачи

Сообщения 1-4 находятся в сессии и покрываются процессами подтверждения и повторной передачи фазы данных. Блоки Peer Test требуют подтверждения.

Сообщения 5-7 могут быть переданы повторно без изменений.

### Заметки по IPv6

Как и в SSU 1, поддерживается тестирование IPv6 адресов, и связь Alice-Bob и Alice-Charlie может осуществляться через IPv6, если Bob и Charlie указывают поддержку с помощью способности 'B' в своих опубликованных IPv6 адресах. Подробности см. в Предложении 126.

Как и в SSU 1 до версии 0.9.50, Алиса отправляет запрос Бобу, используя существующую сессию через транспорт (IPv4 или IPv6), который она хочет протестировать. Когда Боб получает запрос от Алисы через IPv4, Боб должен выбрать Чарли, который анонсирует IPv4-адрес. Когда Боб получает запрос от Алисы через IPv6, Боб должен выбрать Чарли, который анонсирует IPv6-адрес. Фактическое взаимодействие Боб-Чарли может происходить через IPv4 или IPv6 (т.е. независимо от типа адреса Алисы). Это НЕ поведение SSU 1 начиная с версии 0.9.50, где разрешены смешанные IPv4/v6 запросы.

### Обработка Bob'ом

В отличие от SSU 1, Алиса указывает запрашиваемый тестовый IP и порт в сообщении 1. Боб должен проверить этот IP и порт, и отклонить с кодом 5, если они недействительны. Рекомендуемая проверка IP заключается в том, что для IPv4 он должен совпадать с IP Алисы, а для IPv6 должны совпадать как минимум первые 8 байт IP. Проверка порта должна отклонять привилегированные порты и порты для хорошо известных протоколов.

### Конечный автомат результатов

Здесь мы документируем, как Алиса может определить результаты peer test на основе полученных сообщений. Улучшения SSU2 дают нам возможность исправить, улучшить и лучше задокументировать конечный автомат результатов peer test по сравнению с тем, что используется в [SSU](/docs/transport/ssu).

Для каждого тестируемого типа адреса (IPv4 или IPv6) результат может быть одним из UNKNOWN, OK, FIREWALLED или SYMNAT. Кроме того, может выполняться дополнительная обработка для обнаружения изменения IP или порта, или внешнего порта, отличающегося от внутреннего порта.

Проблемы с задокументированной машиной состояний SSU:

- Мы никогда не отправляем сообщение 6, если не получили сообщение 5, поэтому никогда не знаем, являемся ли мы SYMNAT
- Если мы ДЕЙСТВИТЕЛЬНО получили сообщения 4 и 7, как мы вообще можем быть SYMNAT
- Если IP не совпал, но порт совпал, мы не SYMNAT, мы просто сменили наш IP

Таким образом, в отличие от SSU, мы рекомендуем подождать несколько секунд после получения сообщения 4, затем отправить сообщение 6, даже если сообщение 5 не было получено.

Краткое описание конечного автомата, основанного на том, получены ли сообщения 4, 5 и 7 (да или нет), выглядит следующим образом:

```
4 5 7 Result Notes

----- ------ -----n n n UNKNOWN y n n FIREWALLED (unless currently SYMNAT) n y n OK (unless currently SYMNAT, which is unlikely) y y n OK (unless currently SYMNAT, which is unlikely) n n y n/a (can't send msg 6) y n y FIREWALLED or SYMNAT (requires sending msg 6 w/o rcv msg 5) n y y n/a (can't send msg 6) y y y OK
```
Более детальная машина состояний с проверками IP/порта, полученных в блоке адреса сообщения 7, представлена ниже. Одна из задач заключается в определении того, кто находится за симметричным NAT — вы (Alice) или Charlie.

Рекомендуется дополнительная обработка или дополнительная логика для подтверждения переходов состояния путем требования одинаковых результатов при двух или более тестах узлов.

Получение валидации IP/порта и подтверждения двумя или более тестами, или с блоком адреса в сообщениях Session Created, также рекомендуется, но находится за пределами данной спецификации.

```
If Alice does not get msg 5:

If Alice does not get msg 4: -> UNKNOWN If Alice does not get msg 7: -> UNKNOWN If Alice gets msgs 4/7 and IP/port match: -> FIREWALLED If Alice gets msgs 4/7 and IP matches, port does not match: -> SYMNAT, but needs confirmation with 2nd test If Alice gets msgs 4/7 and IP does not match, port matches: -> FIREWALLED, address change? If Alice gets msgs 4/7 and both IP and port do not match: -> SYMNAT, address change?

    If Alice gets msg 5: If Alice does not get msg 4: -> OK unless currently SYMNAT, else UNKNOWN (in SSU2 have to stop here) If Alice does not get msg 7: -> OK unless currently SYMNAT, else UNKNOWN If Alice gets msgs 4/5/7 and IP/port match: -> OK If Alice gets msgs 4/5/7 and IP matches, port does not match: -> OK, charlie is probably sym. natted If Alice gets msgs 4/5/7 and IP does not match, port matches: -> OK, address change? If Alice gets msgs 4/5/7 and both IP and port do not match: -> OK, address change?
```
## Процесс ретрансляции

См. раздел "Безопасность ретрансляции" выше для анализа SSU1 Relay и целей SSU2 Relay.

```
Alice Bob Charlie

lookup Bob RI

    SessionRequest -------------------->

    :   <------------ SessionCreated

    SessionConfirmed ----------------->

    1.  

        RelayRequest ---------------------->

        :   Alice RI ------------>

    2.  RelayIntro ----------->

    3.  <-------------- RelayResponse

    4.  <-------------- RelayResponse

    5.  <-------------------------------------------- HolePunch

    6.  SessionRequest -------------------------------------------->

    7.  <-------------------------------------------- SessionCreated

    8.  SessionConfirmed ------------------------------------------>
```
Когда отклонено Bob:

```
Alice Bob Charlie

lookup Bob RI

    SessionRequest -------------------->

    :   <------------ SessionCreated

    SessionConfirmed ----------------->

    1.  RelayRequest ---------------------->
    2.  <-------------- RelayResponse
```
Когда отклонено Charlie:

```
Alice Bob Charlie

lookup Bob RI

    SessionRequest -------------------->

    :   <------------ SessionCreated

    SessionConfirmed ----------------->

    1.  

        RelayRequest ---------------------->

        :   Alice RI ------------>

    2.  RelayIntro ----------->

    3.  <-------------- RelayResponse

    4.  <-------------- RelayResponse
```
ПРИМЕЧАНИЕ: RI может отправляться либо в сообщениях I2NP Database Store в блоках I2NP, либо как блоки RI (если достаточно малы). Они могут содержаться в тех же пакетах, что и блоки relay, если достаточно малы.

В SSU 1 информация о router Чарли содержит IP, порт, intro key, relay tag и срок истечения каждого introducer.

В SSU 2 информация о роутере Чарли содержит хеш роутера, тег ретранслятора и время истечения каждого introducer.

Алиса должна сократить количество необходимых циклов обмена данными, сначала выбрав introducer (Боба), к которому у неё уже есть соединение. Во-вторых, если такого нет, выбрать introducer, информацию о router которого она уже имеет.

Ретрансляция между версиями также должна поддерживаться, если это возможно. Это обеспечит постепенный переход с SSU 1 на SSU 2. Допустимые комбинации версий (TODO):

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/2/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### Повторные передачи

Relay Request, Relay Intro и Relay Response являются внутрисессионными и покрываются процессами ACK и повторной передачи фазы данных. Блоки Relay Request, Relay Intro и Relay Response требуют подтверждения.

Обратите внимание, что обычно Чарли немедленно отвечает на Relay Intro сообщением Relay Response, которое должно включать блок ACK. В этом случае отдельное сообщение с блоком ACK не требуется.

Hole punch может быть повторно передан, как в SSU 1.

В отличие от сообщений I2NP, сообщения Relay не имеют уникальных идентификаторов, поэтому дубликаты должны обнаруживаться машиной состояний relay с использованием nonce. Реализации также могут потребовать поддержания кэша недавно использованных nonce, чтобы полученные дубликаты могли быть обнаружены даже после завершения работы машины состояний для данного nonce.

### IPv4/v6

Все функции relay SSU 1 поддерживаются, включая те, что задокументированы в [Prop158](/proposals/158-ipv6-transport-enhancements) и поддерживаются начиная с версии 0.9.50. Поддерживаются представления IPv4 и IPv6. Запрос Relay может быть отправлен через IPv4-сессию для IPv6-представления, и запрос Relay может быть отправлен через IPv6-сессию для IPv4-представления.

### Обработка Алисой

Ниже приведены различия между SSU 1 и рекомендации по реализации SSU 2.

#### Выбор Introducer

В SSU 1 введение относительно недорогое, и Алиса обычно отправляет Relay Requests всем introducers. В SSU 2 введение более затратное, поскольку сначала необходимо установить соединение с introducer. Для минимизации задержки введения и накладных расходов рекомендуются следующие шаги обработки:

- Игнорировать любые introducers, которые истекли на основе значения iexp в адресе
- Если SSU2 соединение уже установлено с одним или несколькими introducers, выбрать один и отправить Relay Request только этому introducer.
- В противном случае, если Router Info локально известна для одного или нескольких introducers, выбрать один и подключиться только к этому introducer.
- В противном случае, найти Router Infos для всех introducers, подключиться к introducer, чья Router Info получена первой.

#### Обработка ответов

Как в SSU 1, так и в SSU 2, Relay Response и Hole Punch могут быть получены в любом порядке или могут не быть получены вообще.

В SSU 1 Алиса обычно получает Relay Response (1 RTT) до Hole Punch (1 1/2 RTT). Это может быть недостаточно хорошо документировано в этих спецификациях, но Алиса должна получить Relay Response от Боба перед продолжением, чтобы получить IP Чарли. Если Hole Punch получен первым, Алиса не распознает его, поскольку он не содержит данных и исходный IP не распознан. После получения Relay Response Алиса должна ждать ЛИБО получения Hole Punch от Чарли, ЛИБО короткой задержки (рекомендуется 500 мс) перед началом handshake с Чарли.

В SSU 2 Алиса обычно получит Hole Punch (1,5 RTT) раньше, чем Relay Response (2 RTT). SSU 2 Hole Punch проще обрабатывать, чем в SSU 1, поскольку это полное сообщение с определенными ID соединений (полученными из relay nonce) и содержимым, включающим IP Чарли. Relay Response (Data сообщение) и Hole Punch сообщение содержат идентичный подписанный блок Relay Response. Поэтому Алиса может инициировать handshake с Чарли после получения ЛИБО Hole Punch от Чарли, ЛИБО Relay Response от Боба.

Проверка подписи Hole Punch включает хеш router'а представителя (Bob). Если Relay Request'ы были отправлены более чем одному представителю, существует несколько вариантов проверки подписи:

- Попробовать каждый хеш, на который был отправлен запрос
- Использовать разные nonces для каждого introducer и использовать это для определения, от какого introducer пришел данный Hole Punch в ответ
- Не переподтверждать подпись, если содержимое идентично тому, что было в Relay Response, если оно уже получено
- Вообще не проверять подпись

Если Чарли находится за симметричным NAT, его указанный порт в Relay Response и Hole Punch может быть неточным. Поэтому Алиса должна проверить UDP порт источника сообщения Hole Punch и использовать его, если он отличается от указанного порта.

### Запросы тегов от Боба

В SSU 1 только Alice могла запросить тег в Session Request. Bob никогда не мог запросить тег, и Alice не могла выступать ретранслятором для Bob.

В SSU2 Алиса обычно запрашивает тег в Session Request, но как Алиса, так и Боб могут также запросить тег в фазе данных. Боб обычно не находится за файрволом после получения входящего запроса, но это может произойти после ретрансляции, или состояние Боба может измениться, или он может запросить introducer для другого типа адреса (IPv4/v6). Таким образом, в SSU2 возможно, чтобы и Алиса, и Боб одновременно были ретрансляторами для другой стороны.

## Опубликованная информация о router

### Свойства адреса

Следующие свойства адресов могут быть опубликованы, без изменений по сравнению с SSU 1, включая изменения в [Prop158](/proposals/158-ipv6-transport-enhancements), поддерживаемые начиная с API 0.9.50:

- caps: [B,C,4,6] возможности
- host: IP (IPv4 или IPv6). Сокращённый IPv6-адрес (с "::") разрешён. Может присутствовать или отсутствовать, если защищён брандмауэром. Имена хостов не разрешены.
- iexp[0-2]: Время истечения этого introducer. ASCII цифры, в секундах с начала эпохи. Присутствует только если защищён брандмауэром и требуются introducer. Необязательно (даже если присутствуют другие свойства для этого introducer).
- ihost[0-2]: IP introducer (IPv4 или IPv6). Сокращённый IPv6-адрес (с "::") разрешён. Присутствует только если защищён брандмауэром и требуются introducer. Имена хостов не разрешены. Только для SSU адресов.
- ikey[0-2]: Ключ введения introducer в Base 64. Присутствует только если защищён брандмауэром и требуются introducer. Только для SSU адресов.
- iport[0-2]: Порт introducer 1024 - 65535. Присутствует только если защищён брандмауэром и требуются introducer. Только для SSU адресов.
- itag[0-2]: Тег introducer 1 - (2**32 - 1) ASCII цифры. Присутствует только если защищён брандмауэром и требуются introducer.
- key: Ключ введения в Base 64.
- mtu: Необязательно. См. раздел MTU выше.
- port: 1024 - 65535 Может присутствовать или отсутствовать, если защищён брандмауэром.

### Опубликованные адреса

Опубликованный RouterAddress (часть RouterInfo) будет иметь идентификатор протокола "SSU" или "SSU2".

RouterAddress должен содержать три опции для указания поддержки SSU2:

- s=(Base64 ключ) Текущий открытый статический ключ Noise (s) для данного RouterAddress. Закодирован в Base 64 с использованием стандартного алфавита I2P Base 64. 32 байта в двоичном виде, 44 байта в кодировке Base 64, открытый ключ X25519 в формате little-endian.
- i=(Base64 ключ) Текущий ключ введения для шифрования заголовков данного RouterAddress. Закодирован в Base 64 с использованием стандартного алфавита I2P Base 64. 32 байта в двоичном виде, 44 байта в кодировке Base 64, ключ ChaCha20 в формате big-endian.
- v=2 Текущая версия (2). При публикации как "SSU" подразумевается дополнительная поддержка версии 1. Поддержка будущих версий будет осуществляться через значения, разделенные запятыми, например v=2,3. Реализация должна проверять совместимость, включая несколько версий, если присутствует запятая. Версии, разделенные запятыми, должны быть в числовом порядке.

Алиса должна убедиться, что все три опции присутствуют и действительны перед подключением с использованием протокола SSU2.

Когда опубликовано как "SSU" с опциями "s", "i" и "v", а также с опциями "host" и "port", router должен принимать входящие соединения на указанном хосте и порту для протоколов SSU и SSU2, и автоматически определять версию протокола.

Когда опубликовано как "SSU2" с опциями "s", "i" и "v", а также с опциями "host" и "port", router принимает входящие соединения на указанном хосте и порту только для протокола SSU2.

Если router поддерживает как SSU1, так и SSU2 соединения, но не реализует автоматическое определение версии для входящих соединений, он должен рекламировать как "SSU", так и "SSU2" адреса, и включать опции SSU2 только в "SSU2" адрес. Router должен устанавливать более низкое значение стоимости (более высокий приоритет) в "SSU2" адресе по сравнению с "SSU" адресом, чтобы SSU2 имел предпочтение.

Если несколько SSU2 RouterAddresses (как "SSU" или "SSU2") опубликованы в одном RouterInfo (для дополнительных IP-адресов или портов), все адреса, указывающие один и тот же порт, должны содержать идентичные SSU2 параметры и значения. В частности, все должны содержать одинаковый статический ключ "s" и ключ представления "i".

#### Introducers

При публикации как SSU или SSU2 с introducers присутствуют следующие опции:

- ih[0-2]=(Base64 hash) Хеш router'а для introducer'а. Кодируется в Base 64 с использованием стандартного алфавита I2P Base 64. 32 байта в двоичном формате, 44 байта в кодировке Base 64
- iexp[0-2]: Срок действия этого introducer'а. Не изменено по сравнению с SSU 1.
- itag[0-2]: Тег introducer'а 1 - (2**32 - 1) Не изменено по сравнению с SSU 1.

Следующие опции предназначены только для SSU и не используются для SSU2. В SSU2 Alice получает эту информацию из RI Charlie вместо этого.

- ihost[0-2]
- ikey[0-2]
- itag[0-2]

Router не должен публиковать хост или порт в адресе при публикации introducer'ов. Router должен публиковать флаги 4 и/или 6 в адресе при публикации introducer'ов для указания поддержки IPv4 и/или IPv6. Это соответствует текущей практике для современных SSU 1 адресов.

Примечание: Если публикуется как SSU, и есть смесь SSU 1 и SSU2 introducers, то SSU 1 introducers должны быть на младших индексах, а SSU2 introducers должны быть на старших индексах для совместимости со старыми router'ами.

### Неопубликованный SSU2 адрес

Если Alice не публикует свой SSU2 адрес (как "SSU" или "SSU2") для входящих соединений, она должна опубликовать router адрес "SSU2", содержащий только её статический ключ и версию SSU2, чтобы Bob мог проверить ключ после получения RouterInfo от Alice во второй части Session Confirmed.

- s=(Base64 key) Как определено выше для опубликованных адресов.
- i=(Base64 key) Как определено выше для опубликованных адресов.
- v=2 Как определено выше для опубликованных адресов.

Этот адрес router не будет содержать опции "host" или "port", поскольку они не требуются для исходящих SSU2 соединений. Опубликованная стоимость для этого адреса не имеет строгого значения, поскольку он предназначен только для входящих соединений; однако, это может быть полезно для других router, если стоимость установлена выше (более низкий приоритет), чем у других адресов. Рекомендуемое значение — 14.

Alice также может просто добавить опции "i", "s" и "v" к существующему опубликованному SSU-адресу.

### Ротация открытого ключа и IV

Использование одних и тех же статических ключей для NTCP2 и SSU2 разрешено, но не рекомендуется.

Из-за кэширования RouterInfo, router'ы не должны ротировать статический публичный ключ или IV пока router работает, независимо от того, находится ли он в опубликованном адресе или нет. Router'ы должны постоянно сохранять этот ключ и IV для повторного использования после немедленной перезагрузки, чтобы входящие соединения продолжали работать, а время перезапуска не раскрывалось. Router'ы должны постоянно сохранять или иным образом определять время последнего отключения, чтобы предыдущее время простоя могло быть рассчитано при запуске.

С учетом опасений по поводу раскрытия времени перезапуска, router'ы могут ротировать этот ключ или IV при запуске, если router ранее был недоступен в течение некоторого времени (по крайней мере несколько дней).

Если router имеет любые опубликованные SSU2 RouterAddresses (как SSU или SSU2), минимальное время простоя перед ротацией должно быть намного больше, например, один месяц, если только локальный IP-адрес не изменился или router не выполняет "rekeys".

Если router имеет какие-либо опубликованные SSU RouterAddresses, но не SSU2 (как SSU или SSU2), минимальное время простоя перед ротацией должно быть больше, например, один день, если только локальный IP-адрес не изменился или router не выполнил "rekeys". Это применяется, даже если опубликованный SSU адрес имеет introducers.

Если router не имеет опубликованных RouterAddresses (SSU, SSU2 или SSU), минимальное время простоя перед ротацией может составлять всего два часа, даже при изменении IP-адреса, если только router не выполняет "rekeys".

Если router "перегенерирует ключи" на другой Router Hash, он также должен сгенерировать новый noise key и intro key.

Реализации должны учитывать, что изменение статического публичного ключа или IV запретит входящие SSU2 соединения от router'ов, которые кэшировали более старую RouterInfo. Публикация RouterInfo, выбор узлов tunnel'а (включая как OBGW, так и ближайший переход IB), выбор нулевого tunnel'а, выбор транспорта и другие стратегии реализации должны это учитывать.

Ротация intro ключей подчиняется тем же правилам, что и ротация ключей.

Примечание: Минимальное время простоя перед повторным созданием ключей может быть изменено для обеспечения работоспособности сети и предотвращения повторного получения начальных данных router'ом, который был отключен в течение умеренного периода времени.

#### Скрытие личности

Отрицаемость не является целью. См. обзор выше.

Каждому паттерну присваиваются свойства, описывающие конфиденциальность, предоставляемую статическому открытому ключу инициатора и статическому открытому ключу отвечающей стороны. Базовые предположения состоят в том, что эфемерные приватные ключи являются безопасными, и что стороны прерывают рукопожатие, если получают от другой стороны статический открытый ключ, которому они не доверяют.

Данный раздел рассматривает только утечку идентичности через статические поля открытых ключей в процессе рукопожатия. Разумеется, идентичности участников Noise могут быть раскрыты и другими способами, включая поля полезной нагрузки, анализ трафика или метаданные, такие как IP-адреса.

Alice: (8) Зашифровано с прямой секретностью для аутентифицированной стороны.

Боб: (3) Не передается, но пассивный атакующий может проверить кандидатов на приватный ключ отвечающей стороны и определить, является ли кандидат правильным.

Боб публикует свой статический публичный ключ в netdb. Алиса может этого не делать, но должна включить его в RI, отправляемый Бобу.

## Руководящие принципы пакетов

### Создание исходящих пакетов

Сообщения рукопожатия (Session Request/Created/Confirmed, Retry) основные шаги, по порядку:

- Создать заголовок размером 16 или 32 байта
- Создать полезную нагрузку
- Выполнить mixHash() для заголовка (кроме Retry)
- Зашифровать полезную нагрузку с помощью Noise (кроме Retry, использовать ChaChaPoly с заголовком в качестве AD)
- Зашифровать заголовок, а для Session Request/Created — временный ключ

Основные шаги сообщений фазы данных, по порядку:

- Создать 16-байтовый заголовок
- Создать полезную нагрузку
- Зашифровать полезную нагрузку с использованием ChaChaPoly, используя заголовок как AD
- Зашифровать заголовок

### Обработка входящих пакетов

#### Сводка

Начальная обработка всех входящих сообщений:

- Расшифровать первые 8 байт заголовка (Destination Connection ID) с помощью intro key
- Найти соединение по Destination Connection ID
- Если соединение найдено и находится в фазе данных, перейти к разделу фазы данных
- Если соединение не найдено, перейти к разделу handshake
- Примечание: Сообщения Peer Test и Hole Punch также могут быть найдены по Destination Connection ID, созданному из test или relay nonce.

Обработка сообщений handshake (Session Request/Created/Confirmed, Retry, Token Request) и других внесессионных сообщений (Peer Test, Hole Punch):

- Расшифровать байты 8-15 заголовка (тип пакета, версию и net ID) с помощью intro key. Если это валидный Session Request, Token Request, Peer Test или Hole Punch, продолжить
- Если сообщение невалидно, найти ожидающее исходящее соединение по IP/порту источника пакета, обработать пакет как Session Created или Retry. Повторно расшифровать первые 8 байт заголовка с правильным ключом, и байты 8-15 заголовка (тип пакета, версию и net ID). Если это валидный Session Created или Retry, продолжить
- Если сообщение невалидно, завершить с ошибкой или поставить в очередь как возможный пакет фазы данных вне порядка
- Для Session Request/Created, Retry, Token Request, Peer Test и Hole Punch расшифровать байты 16-31 заголовка
- Для Session Request/Created расшифровать ephemeral key
- Валидировать все поля заголовка, остановиться если невалидны
- mixHash() заголовка
- Для Session Request/Created/Confirmed расшифровать полезную нагрузку используя Noise
- Для Retry и фазы данных расшифровать полезную нагрузку используя ChaChaPoly
- Обработать заголовок и полезную нагрузку

Обработка сообщений фазы данных:

- Расшифровать байты 8-15 заголовка (тип пакета, версия и net ID) с правильным ключом
- Расшифровать полезную нагрузку, используя ChaChaPoly с заголовком в качестве AD
- Обработать заголовок и полезную нагрузку

#### Подробности

В SSU 1 классификация входящих пакетов затруднена, поскольку нет заголовка для указания номера сессии. Роутеры должны сначала сопоставить исходный IP и порт с существующим состоянием пира, и если совпадение не найдено, попытаться выполнить множественные расшифровки с разными ключами, чтобы найти соответствующее состояние пира или начать новое. В случае изменения исходного IP или порта для существующей сессии, возможно из-за поведения NAT, роутер может использовать дорогостоящую эвристику для попытки сопоставить пакет с существующей сессией и восстановить содержимое.

SSU 2 разработан для минимизации усилий по классификации входящих пакетов при сохранении устойчивости к DPI и другим угрозам на пути передачи. Номер Connection ID включен в заголовок для всех типов сообщений и зашифрован (обфусцирован) с использованием ChaCha20 с известным ключом и nonce. Дополнительно, тип сообщения также включен в заголовок (зашифрован с защитой заголовка известным ключом, а затем обфусцирован с помощью ChaCha20) и может использоваться для дополнительной классификации. Ни в коем случае не требуется пробного DH или других операций асимметричной криптографии для классификации пакета.

Для практически всех сообщений от всех пиров ключ ChaCha20 для шифрования Connection ID является introduction key роутера назначения, опубликованным в netDb.

Единственными исключениями являются первые сообщения, отправляемые от Bob к Alice (Session Created или Retry), где introduction key Alice еще не известен Bob. В этих случаях в качестве ключа используется introduction key Bob.

Протокол разработан для минимизации обработки классификации пакетов, которая может потребовать дополнительных криптографических операций в нескольких резервных шагах или сложной эвристики. Кроме того, подавляющее большинство получаемых пакетов не будет требовать (возможно, дорогостоящего) резервного поиска по исходному IP/порту и второго расшифрования заголовка. Только Session Created и Retry (и возможно другие, которые будут определены позже) потребуют резервной обработки. Если конечная точка изменяет IP или порт после создания сессии, ID соединения по-прежнему используется для поиска сессии. Никогда не требуется использовать эвристику для поиска сессии, например, путем поиска другой сессии с тем же IP, но другим портом.

Таким образом, рекомендуемые шаги обработки в логике цикла получателя:

1) Расшифровать первые 8 байт с помощью ChaCha20, используя локальный ключ представления, чтобы восстановить Connection ID назначения. Если Connection ID соответствует текущей или ожидающей входящей сессии:

    a)  Using the appropriate key, decrypt the header bytes 8-15 to recover the version, net ID, and message type.
    b)  If the message type is Session Confirmed, it is a long header. Verify the net ID and protocol version are valid. Decrypt the bytes 15-31 of the header with ChaCha20 using the local intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise.
    c)  If the message type is valid but not Session Confirmed, it is a short header. Verify the net ID and protocol version are valid. decrypt the rest of the message with ChaCha20/Poly1305 using the session key, using the decrypted 16-byte header as the AD.
    d)  (optional) If connection ID is a pending inbound session awaiting a Session Confirmed message, but the net ID, protocol, or message type is not valid, it could be a Data message received out-of-order before the Session Confirmed, so the data phase header protection keys are not yet known, and the header bytes 8-15 were incorrectly decrypted. Queue the message, and attempt to decrypt it once the Session Confirmed message is received.
    e)  If b) or c) fails, drop the message.

2)  Если идентификатор соединения не соответствует текущей сессии: Проверить, что заголовок в открытом тексте в байтах 8-15 является действительным (без выполнения каких-либо операций защиты заголовка). Убедиться, что net ID и версия протокола действительны, а тип сообщения является Session Request или другим типом сообщения, разрешенным вне сессии (подлежит определению).

    a)  If all is valid and the message type is Session Request, decrypt bytes 16-31 of the header and the 32-byte X value with ChaCha20 using the local intro key.

    - If the token at header bytes 24-31 is accepted, then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Created in response.
    - If the token is not accepted, send a Retry message to the source IP/port with a token. Do not attempt to decrypt the message with Noise to avoid DDoS attacks.

    b)  If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.
    c)  If a) or b) fails, go to step 3)

3)  Найти ожидающую исходящую сессию по исходному IP/порту пакета.

    a)  If found, re-decrypt the first 8 bytes with ChaCha20 using Bob's introduction key to recover the Destination Connection ID.
    b)  If the connection ID matches the pending session: Using the correct key, decrypt bytes 8-15 of the header to recover the version, net ID, and message type. Verify the net ID and protocol version are valid, and the message type is Session Created or Retry, or other message type allowed out-of-session (TBD).

    - If all is valid and the message type is Session Created, decrypt the next 16 bytes of the header and the 32-byte Y value with ChaCha20 using Bob's intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Confirmed in response.
    - If all is valid and the message type is Retry, decrypt bytes 16-31 of the header with ChaCha20 using Bob's intro key. Decrypt and validate the message using ChaCha20/Poly1305 using TBD as the key and TBD as the nonce and the decrypted 32-byte header as the AD. Resend a Session Request with the received token in response.
    - If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.

    > c)  If a pending outbound session is not found, or the connection ID does not match the pending session, drop the message, unless the port is shared with SSU 1.

4)  Если SSU 1 работает на том же порту, попытаться обработать сообщение как SSU 1 пакет.

#### Обработка ошибок

В общем случае сессия (в фазе handshake или передачи данных) никогда не должна уничтожаться после получения пакета с неожиданным типом сообщения. Это предотвращает атаки внедрения пакетов. Такие пакеты также часто получаются после повторной передачи handshake-пакета, когда ключи расшифровки заголовка больше не действительны.

В большинстве случаев просто отбросить пакет. Реализация может, но не обязана, повторно передать ранее отправленный пакет (сообщение handshake или ACK 0) в ответ.

После отправки Session Created как Bob, неожиданные пакеты обычно являются пакетами Data, которые не могут быть расшифрованы, поскольку пакеты Session Confirmed были потеряны или получены не по порядку. Поставьте пакеты в очередь и попытайтесь расшифровать их после получения пакетов Session Confirmed.

После получения Session Confirmed в качестве Bob, неожиданные пакеты обычно представляют собой повторно переданные пакеты Session Confirmed, поскольку ACK 0 от Session Confirmed был утерян. Неожиданные пакеты могут быть отброшены. Реализация может, но не обязана, отправить пакет Data, содержащий блок ACK, в ответ.

### Примечания

Для Session Created и Session Confirmed реализации должны тщательно валидировать все расшифрованные поля заголовка (Connection IDs, номер пакета, тип пакета, версия, id, frag и флаги) ПЕРЕД вызовом mixHash() для заголовка и попыткой расшифровать полезную нагрузку с помощью Noise AEAD. Если расшифровка Noise AEAD не удается, дальнейшая обработка невозможна, поскольку mixHash() повредит состояние handshake, если только реализация не сохраняет и не "откатывает" состояние хеша.

### Определение версии

Возможно, будет невозможно эффективно определить, являются ли входящие пакеты версии 1 или 2 на одном и том же входящем порту. Описанные выше шаги может иметь смысл выполнить перед обработкой SSU 1, чтобы избежать попыток пробных операций DH с использованием обеих версий протокола.

Будет определено при необходимости.

## Рекомендуемые константы

- Таймаут повторной передачи исходящего handshake: 1,25 секунды с экспоненциальным увеличением (повторные передачи через 1,25, 3,75 и 8,75 секунд)
- Общий таймаут исходящего handshake: 15 секунд
- Таймаут повторной передачи входящего handshake: 1 секунда с экспоненциальным увеличением (повторные передачи через 1, 3 и 7 секунд)
- Общий таймаут входящего handshake: 12 секунд
- Таймаут после отправки retry: 9 секунд
- Задержка ACK: max(10, min(rtt/6, 150)) мс
- Немедленная задержка ACK: min(rtt/16, 5) мс
- Максимальные диапазоны ACK: 256?
- Максимальная глубина ACK: 512?
- Распределение padding: 0-15 байт или больше
- Минимальный таймаут повторной передачи фазы данных: 1 секунда, как указано в [RFC-6298](https://tools.ietf.org/html/rfc6298)
- См. также [RFC-6298](https://tools.ietf.org/html/rfc6298) для дополнительных рекомендаций по таймерам повторной передачи для фазы данных.

## Анализ накладных расходов пакета

Предполагается IPv4, не включая дополнительное выравнивание, не включая размеры заголовков IP и UDP. Выравнивание — это выравнивание по модулю 16 только для SSU 1.

**SSU 1**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MAC</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">40</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">304</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. extended options</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">79</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">336</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 64 byte Ed25519 sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">462</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">512</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 391 byte ident and 64 byte sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (RI)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1014</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1051</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header, 1000 byte RI</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">51</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">2254</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>
**SSU 2**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MACs</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">87</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">96</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime, Address blocks</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1005</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1085</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1000 byte compressed RI block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">46</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1314</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>    
## Проблемы и будущая работа

### Токены

Мы указываем выше, что токен должен быть случайно сгенерированным 8-байтовым значением, а не непрозрачным значением, таким как хеш или HMAC серверного секрета и IP, порта, из-за атак повторного использования. Однако это требует временного и (опционально) постоянного хранения доставленных токенов. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) использует 16-байтовый HMAC серверного секрета и IP-адреса, и серверный секрет обновляется каждые две минуты. Мы должны исследовать что-то похожее, с более длительным временем жизни серверного секрета. Если мы встроим временную метку в токен, это может быть решением, но 8-байтовый токен может быть недостаточно большим для этого.

## Ссылки

- **[Common]** [Спецификация общих структур](/docs/specs/common-structures)
- **[ECIES]** [Спецификация ECIES-X25519-AEAD-Ratchet](/docs/specs/ecies)
- **[NetDB]** [Сетевая база данных](/docs/overview/network-database)
- **[NOISE]** [Фреймворк протокола Noise](https://noiseprotocol.org/noise.html)
- **[Nonces]** [Противники, не учитывающие nonce](https://eprint.iacr.org/2019/624.pdf)
- **[NTCP]** [Транспорт NTCP](/docs/transport/ntcp)
- **[NTCP2]** [Спецификация NTCP2](/docs/specs/ntcp2)
- **[PMTU]** [Обнаружение MTU пути](https://en.wikipedia.org/wiki/Path_MTU_Discovery)
- **[Prop104]** [Предложение 104: TLS транспорт](/proposals/104-tls-transport)
- **[Prop109]** [Предложение 109: Подключаемый транспорт](/proposals/109-pt-transport)
- **[Prop158]** [Предложение 158: Улучшения IPv6 транспорта](/proposals/158-ipv6-transport-enhancements)
- **[Prop159]** [Предложение 159: SSU2](/proposals/159-ssu2)
- **[RFC-2104]** [RFC 2104: HMAC](https://tools.ietf.org/html/rfc2104)
- **[RFC-3449]** [RFC 3449: Влияние на производительность TCP](https://tools.ietf.org/html/rfc3449)
- **[RFC-3526]** [RFC 3526: MODP группы](https://tools.ietf.org/html/rfc3526)
- **[RFC-5681]** [RFC 5681: Управление перегрузкой TCP](https://tools.ietf.org/html/rfc5681)
- **[RFC-5869]** [RFC 5869: HKDF](https://tools.ietf.org/html/rfc5869)
- **[RFC-6151]** [RFC 6151: Соображения безопасности MD5](https://tools.ietf.org/html/rfc6151)
- **[RFC-6298]** [RFC 6298: Таймер повторной передачи TCP](https://tools.ietf.org/html/rfc6298)
- **[RFC-6437]** [RFC 6437: Метка потока IPv6](https://tools.ietf.org/html/rfc6437)
- **[RFC-7539]** [RFC 7539: ChaCha20/Poly1305](https://tools.ietf.org/html/rfc7539)
- **[RFC-7748]** [RFC 7748: Эллиптические кривые для безопасности](https://tools.ietf.org/html/rfc7748)
- **[RFC-7905]** [RFC 7905: Наборы шифров ChaCha20-Poly1305 для TLS](https://tools.ietf.org/html/rfc7905)
- **[RFC-9000]** [RFC 9000: Транспортный протокол QUIC](https://datatracker.ietf.org/doc/html/rfc9000)
- **[RFC-9001]** [RFC 9001: Использование TLS для защиты QUIC](https://datatracker.ietf.org/doc/html/rfc9001)
- **[RFC-9002]** [RFC 9002: Обнаружение потерь и управление перегрузкой QUIC](https://datatracker.ietf.org/doc/html/rfc9002)
- **[RouterAddress]** [Структура RouterAddress](/docs/specs/common-structures#struct-routeraddress)
- **[RouterIdentity]** [Структура RouterIdentity](/docs/specs/common-structures#struct-routeridentity)
- **[SigningPublicKey]** [Тип SigningPublicKey](/docs/specs/common-structures#type-signingpublickey)
- **[SSU]** [Транспорт SSU](/docs/transport/ssu)
- **[STS]** [Протокол станция-к-станции](https://en.wikipedia.org/wiki/Station-to-Station_protocol)
- **[Ticket1112]** Тикет I2P 1112
- **[Ticket1849]** Тикет I2P 1849
- **[WireGuard]** [Протокол WireGuard](https://www.wireguard.com/papers/wireguard.pdf)
