---
title: "PQ Hybrid NTCP2"
description: "Постквантовый гибридный вариант транспортного протокола NTCP2 с использованием ML-KEM"
slug: "ntcp2-hybrid"
lastupdated: "2026-02"
category: "Транспорты"
accurateFor: "0.9.69"
---

### Статус

Бета Q1 2026, релиз Q2 2026

## Обзор

Это гибридный постквантовый вариант транспортного протокола NTCP2, разработанный в Предложении 169. См. это предложение для дополнительной информации.

PQ Hybrid NTCP2 определён только для того же адреса и порта, что и стандартный NTCP2. Работа на другом порту или без поддержки стандартного NTCP2 не разрешена и не будет разрешена в течение нескольких лет, пока стандартный NTCP2 не будет признан устаревшим.

Данная спецификация документирует только изменения, необходимые для стандартного NTCP2 для поддержки PQ Hybrid. См. спецификацию NTCP2 для базовых деталей реализации.

## Дизайн

Мы поддерживаем стандарты NIST FIPS 203 и 204 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf), которые основаны на CRYSTALS-Kyber и CRYSTALS-Dilithium (версии 3.1, 3 и более старые), но НЕ совместимы с ними.

### Обмен ключами

PQ KEM предоставляет только эфемерные ключи и не поддерживает напрямую рукопожатия со статическими ключами, такие как Noise XK и IK. Типы шифрования те же, что используются в PQ Hybrid Ratchet, и определены в документе по общим структурам [/docs/specs/common-structures/](/docs/specs/common-structures/), как в [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf). Гибридные типы определены только в сочетании с X25519.

Типы шифрования:

| Тип | Код |
|------|------|
| MLKEM512_X25519 | 5 |
| MLKEM768_X25519 | 6 |
| MLKEM1024_X25519 | 7 |
### Допустимые комбинации

Новые типы шифрования указываются в RouterAddresses. Тип шифрования в сертификате ключа по-прежнему будет иметь тип 4.

## Спецификация

### Паттерны рукопожатия

Handshake используют шаблоны handshake [Noise Protocol](https://noiseprotocol.org/noise.html).

Используется следующее соответствие букв:

- e = одноразовый эфемерный ключ
- s = статический ключ
- p = полезная нагрузка сообщения
- e1 = одноразовый эфемерный PQ ключ, отправляемый от Alice к Bob
- ekem1 = шифртекст KEM, отправляемый от Bob к Alice

Следующие модификации XK и IK для гибридной прямой секретности (hfs) указаны в [спецификации Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) разделе 5:

```
XK:                       XKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, p               -> e, es, e1, p
  <- e, ee, p               <- e, ee, ekem1, p
  -> s, se                  -> s, se
  <- p                      <- p
  p ->                      p ->


  e1 and ekem1 are encrypted. See pattern definitions below.
  NOTE: e1 and ekem1 are different sizes (unlike X25519)
```
Паттерн e1 определяется следующим образом, как указано в [спецификации Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) разделе 4:

```
For Alice:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++
  MixHash(ciphertext)

  For Bob:

  // DecryptAndHash(ciphertext)
  encap_key = DECRYPT(k, n, ciphertext, ad)
  n++
  MixHash(ciphertext)
```
Шаблон ekem1 определяется следующим образом, как указано в разделе 4 [спецификации Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf):

```
For Bob:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  MixKey(kem_shared_key)


  For Alice:

  // DecryptAndHash(ciphertext)
  kem_ciphertext = DECRYPT(k, n, ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  MixKey(kem_shared_key)
```
### Noise Handshake KDF

#### Обзор

Гибридное рукопожатие определено в [спецификации Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf). Первое сообщение от Алисы к Бобу содержит e1, ключ инкапсуляции, перед полезной нагрузкой сообщения. Это рассматривается как дополнительный статический ключ; вызовите EncryptAndHash() на нем (как Алиса) или DecryptAndHash() (как Боб). Затем обработайте полезную нагрузку сообщения как обычно.

Второе сообщение от Боба к Алисе содержит ekem1, зашифрованный текст, перед полезной нагрузкой сообщения. Это рассматривается как дополнительный статический ключ; вызовите EncryptAndHash() для него (как Боб) или DecryptAndHash() (как Алиса). Затем вычислите kem_shared_key и вызовите MixKey(kem_shared_key). После этого обработайте полезную нагрузку сообщения как обычно.

#### Определенные операции ML-KEM

Мы определяем следующие функции, соответствующие криптографическим строительным блокам, используемым как определено в [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

(encap_key, decap_key) = PQ_KEYGEN()

    Alice creates the encapsulation and decapsulation keys
    The encapsulation key is sent in message 1.
    encap_key and decap_key sizes vary based on ML-KEM variant.

(ciphertext, kem_shared_key) = ENCAPS(encap_key)

    Bob calculates the ciphertext and shared key,
    using the ciphertext received in message 1.
    The ciphertext is sent in message 2.
    ciphertext size varies based on ML-KEM variant.
    The kem_shared_key is always 32 bytes.

kem_shared_key = DECAPS(ciphertext, decap_key)

    Alice calculates the shared key,
    using the ciphertext received in message 2.
    The kem_shared_key is always 32 bytes.

Обратите внимание, что и encap_key, и ciphertext зашифрованы внутри блоков ChaCha/Poly в сообщениях 1 и 2 рукопожатия Noise. Они будут расшифрованы как часть процесса рукопожатия.

kem_shared_key смешивается с chaining key с помощью MixHash(). Подробности см. ниже.

#### Alice KDF для сообщения 1

После шаблона сообщения 'es' и перед полезной нагрузкой добавьте:

```
This is the "e1" message pattern:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)


  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### Bob KDF для сообщения 1

После шаблона сообщения 'es' и перед полезной нагрузкой добавьте:

```
This is the "e1" message pattern:

  // DecryptAndHash(encap_key_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  encap_key = DECRYPT(k, n, encap_key_section, ad)
  n++

  // MixHash(encap_key_section)
  h = SHA256(h || encap_key_section)

  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### Bob KDF для сообщения 2

Для XK: После шаблона сообщения 'ee' и перед полезной нагрузкой добавить:

```
This is the "ekem1" message pattern:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  // MixKey(kem_shared_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### Alice KDF для сообщения 2

После паттерна сообщения 'ee' добавьте:

```
This is the "ekem1" message pattern:

  // DecryptAndHash(kem_ciphertext_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  kem_ciphertext = DECRYPT(k, n, kem_ciphertext_section, ad)

  // MixHash(kem_ciphertext_section)
  h = SHA256(h || kem_ciphertext_section)

  // MixKey(kem_shared_key)
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### KDF для сообщения 3 (только XK)

без изменений

#### KDF для split()

без изменений

### Детали рукопожатия

#### Идентификаторы Noise

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

Изменения: Текущий NTCP2 содержит только опции в секции ChaCha. С ML-KEM секция ChaCha также будет содержать зашифрованный PQ публичный ключ.

Чтобы PQ и не-PQ NTCP2 могли поддерживаться на одном и том же адресе и порту router'а, мы используем старший бит значения X (эфемерный публичный ключ X25519) для обозначения того, что это PQ соединение. Этот бит всегда сброшен для не-PQ соединений.

Для Алисы, после того как сообщение зашифровано с помощью Noise, но до AES-обфускации X, установите X[31] |= 0x7f.

Для Боба, после AES де-обфускации X, проверить X[31] & 0x80. Если бит установлен, очистить его с помощью X[31] &= 0x7f, и расшифровать через Noise как PQ соединение. Если бит не установлен, расшифровать через Noise как обычное не-PQ соединение как обычно.

Для PQ NTCP2, рекламируемого на другом адресе и порту router, это не требуется.

Для получения дополнительной информации см. раздел "Опубликованные адреса" ниже.

Исходное содержимое:

```
  +----+----+----+----+----+----+----+----+
  |        MS bit set to 1 and then       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted X         |
  +             (32 bytes)                +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +      (see table below for length)     +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  ~   n = 0                               ~
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaChaPoly frame (options)          |
  +         32 bytes                      +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  ~         padding (optional)            ~
  |     length defined in options block   |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
Незашифрованные данные (тег аутентификации Poly1305 не показан):

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
  |           ML-KEM encap_key            |
  +      (see table below for length)     +
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
```
Примечание: поле версии в блоке опций сообщения 1 должно быть установлено в значение 2, даже для PQ-соединений.

Размеры:

| Тип | Код типа | Длина X | Длина Msg 1 | Длина Msg 1 Enc | Длина Msg 1 Dec | Длина PQ ключа | Длина opt |
|------|-----------|---------|-------------|-----------------|-----------------|----------------|-----------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 880+pad | 848 | 816 | 800 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1264+pad | 1232 | 1200 | 1184 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1648+pad | 1616 | 1584 | 1568 | 16 |
Примечание: Коды типов предназначены только для внутреннего использования. Router останутся типа 4, а поддержка будет указана в адресах router.

#### 2) SessionCreated

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
  |   ChaChaPoly frame (MLKEM)            |
  +   Encrypted and authenticated data    +
  -      (see table below for length)     -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (options)          |
  +   Encrypted and authenticated data    +
  -           32 bytes                    -
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

  Same as current specification except add a second ChaChaPoly frame
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
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
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
```
Размеры:

| Тип | Код типа | Y len | Msg 2 len | Msg 2 Enc len | Msg 2 Dec len | PQ CT len | opt len |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 848+pad | 816 | 784 | 768 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1136+pad | 1104 | 1104 | 1088 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1616+pad | 1584 | 1584 | 1568 | 16 |
Примечание: Коды типов предназначены только для внутреннего использования. Router останутся типа 4, а поддержка будет указана в адресах router.

#### 3) SessionConfirmed

Без изменений

#### Функция формирования ключа (KDF) (для фазы данных)

Без изменений

#### Опубликованные адреса

Во всех случаях используйте название транспорта NTCP2 как обычно.

Используйте тот же адрес/порт, что и для не-PQ, не заблокированного фаерволом. Поддерживается только один вариант PQ. В адресе router публикуйте v=2 (как обычно) и новый параметр pq=[3|4|5] для указания MLKEM 512/768/1024. Alice устанавливает старший бит эфемерного ключа (key[31] & 0x80) в запросе сессии, чтобы указать, что это гибридное соединение. См. выше. Более старые router будут игнорировать параметр pq и подключаться не-PQ как обычно.

Разные адреса/порты для не-PQ или только PQ, без файрвола НЕ поддерживаются. Это не будет реализовано до тех пор, пока не-PQ NTCP2 не будет отключен, что произойдет через несколько лет. Когда не-PQ будет отключен, может поддерживаться несколько вариантов PQ, но только один на адрес. Когда это будет поддерживаться, в адресе router публикуйте v=[3|4|5] для указания MLKEM 512/768/1024. Alice не устанавливает MSB эфемерного ключа. Старые router будут проверять параметр v и пропускать этот адрес как неподдерживаемый.

Адреса за межсетевым экраном (IP не публикуется): В адресе router'а публикуйте v=2 (как обычно). Нет необходимости публиковать параметр pq.

Alice может подключиться к PQ Bob, используя PQ вариант, который публикует Bob, независимо от того, рекламирует ли Alice поддержку pq в информации своего router или рекламирует ли она тот же вариант.

#### Максимальное заполнение

В текущей спецификации сообщения 1 и 2 определены как имеющие "разумное" количество отступов, с рекомендуемым диапазоном 0-31 байт и без указанного максимума.

До API 0.9.68 (релиз 2.11.0) включительно, Java I2P реализовывал максимум 256 байт заполнения для не-PQ соединений, однако это ранее не было задокументировано. Начиная с API 0.9.69 (релиз 2.12.0), Java I2P реализует такое же максимальное заполнение для не-PQ соединений, как и для MLKEM-512. См. таблицу ниже.

Использовать определенный размер сообщения в качестве максимального заполнения, то есть максимальное заполнение удвоит размер сообщения для PQ-соединений следующим образом:

| Максимальный размер заполнения сообщения | не-PQ (до 0.9.68) | не-PQ (начиная с 0.9.69) | MLKEM-512 | MLKEM-768 | MLKEM-1024 |
|-------------------------------------------|-------------------|---------------------------|-----------|-----------|------------|
| Session Request  |   256   |   880   |    880   |     1264   |    1648  |
| Session Created  |   256   |   848   |    848   |     1136   |    1616  |
## Анализ накладных расходов

### Обмен ключами

Увеличение размера (байт):

| Тип | Pubkey (Сообщение 1) | Cipertext (Сообщение 2) |
|------|----------------|-------------------|
| MLKEM512_X25519 | +816 | +784 |
| MLKEM768_X25519 | +1200 | +1104 |
| MLKEM1024_X25519 | +1584 | +1584 |
## Анализ безопасности

Категории безопасности NIST кратко изложены в [презентации NIST](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) на слайде 10. Предварительные критерии: Наша минимальная категория безопасности NIST должна быть 2 для гибридных протоколов и 3 для протоколов только с постквантовой криптографией.

| Категория | Уровень безопасности как у |
|-----------|---------------------------|
| 1 | AES128 |
| 2 | SHA256 |
| 3 | AES192 |
| 4 | SHA384 |
| 5 | AES256 |
### Рукопожатия

Все это гибридные протоколы. Реализации должны отдавать предпочтение MLKEM768; MLKEM512 недостаточно безопасен.

Категории безопасности NIST [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf):

| Алгоритм | Категория безопасности |
|----------|------------------------|
| MLKEM512 | 1 |
| MLKEM768 | 3 |
| MLKEM1024 | 5 |
## Примечания по реализации

### Поддержка библиотек

Библиотеки Bouncycastle, BoringSSL и WolfSSL теперь поддерживают MLKEM и MLDSA. Поддержка OpenSSL будет в их релизе 3.5 от 8 апреля 2025 года [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

### Идентификация входящего трафика

Мы устанавливаем старший бит эфемерного ключа (key[31] & 0x80) в запросе сессии, чтобы указать, что это гибридное соединение. Это позволяет нам запускать как стандартный NTCP, так и гибридный NTCP на одном порту. Для входящих соединений поддерживается только один гибридный вариант, который рекламируется в адресе router. Например, pq=3 или pq=4.

#### Обфускация

Как Alice, для PQ соединения, перед обфускацией, установите X[31] |= 0x80. Это делает X недействительным открытым ключом X25519. После обфускации AES-CBC рандомизирует его. Старший бит X будет случайным после обфускации.

Как Bob, проверьте, что (X[31] & 0x80) != 0 после деобфускации. Если это так, то это PQ соединение.

Минимальная версия router, необходимая для NTCP2-PQ, пока не определена.

Примечание: Коды типов предназначены только для внутреннего использования. Роутеры останутся типа 4, а поддержка будет указана в адресах роутеров.

## Совместимость router'ов

### Названия транспортов

Во всех случаях используйте имя транспорта NTCP2 как обычно. Более старые router'ы будут игнорировать параметр pq и подключаться со стандартным NTCP2 как обычно.

## Ссылки

* [CABFORUM](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/)
* [Choosing-Hash](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3)
* [CLOUDFLARE](https://blog.cloudflare.com/pq-2024/)
* [COMMON](/docs/specs/common-structures/)
* [COMPOSITE-SIGS](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)
* [ECIES](/docs/specs/ecies/)
* [FORUM](http://zzz.i2p/topics/3294)
* [FIPS202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
* [FIPS203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
* [FIPS204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
* [FIPS205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf)
* [MLDSA-OIDS](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/)
* [NIST-PQ](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)
* [NIST-PQ-UPDATE](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf)
* [NIST-PQ-END](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf)
* [NIST-VECTORS](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values)
* [Noise](https://noiseprotocol.org/noise.html)
* [Noise-Hybrid](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf)
* [NSA-PQ](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF)
* [NTCP2](/docs/specs/ntcp2/)
* [OPENSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/)
* [Prop165](/docs/proposals/165/)
* [PQ-WIREGUARD](https://eprint.iacr.org/2020/379.pdf)
* [RFC-2104](https://tools.ietf.org/html/rfc2104)
* [Rosenpass](https://rosenpass.eu/)
* [Rosenpass-Whitepaper](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf)
* [SSH-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/)
* [SSU2](/docs/specs/ssu2/)
* [TLS-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/)
