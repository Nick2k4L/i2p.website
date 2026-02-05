---
title: "Сообщения Router с ECIES-X25519"
description: "Спецификация для шифрования garlic сообщений для ECIES router'ов с использованием X25519"
slug: "ecies-routers"
category: "Протоколы"
lastUpdated: "2025-03"
accurateFor: "0.9.65"
---

## Примечание

Поддерживается начиная с версии 0.9.49. Развертывание в сети и тестирование в процессе. Возможны незначительные изменения. См. [предложение 156](/proposals/156-ecies-routers).

## Обзор

Этот документ определяет шифрование garlic-сообщений для ECIES router'ов, используя криптографические примитивы, представленные в [ECIES-X25519](/docs/specs/ecies). Это часть общего [предложения 156](/proposals/156-ecies-routers) по переводу router'ов с ключей ElGamal на ключи ECIES-X25519. Данная спецификация реализована начиная с релиза 0.9.49.

Для обзора всех изменений, необходимых для ECIES router'ов, см. [предложение 156](/proposals/156-ecies-routers). Для Garlic Messages к ECIES-X25519 получателям, см. [ECIES-X25519](/docs/specs/ecies).

### Криптографические примитивы

Примитивы, необходимые для реализации данной спецификации:

- AES-256-CBC как в [Cryptography](/docs/specs/cryptography)
- STREAM функции ChaCha20/Poly1305: ENCRYPT(k, n, plaintext, ad) и DECRYPT(k, n, ciphertext, ad) - как в [NTCP2](/docs/specs/ntcp2), [ECIES-X25519](/docs/specs/ecies), и [RFC-7539](https://tools.ietf.org/html/rfc7539)
- X25519 DH функции - как в [NTCP2](/docs/specs/ntcp2) и [ECIES-X25519](/docs/specs/ecies)
- HKDF(salt, ikm, info, n) - как в [NTCP2](/docs/specs/ntcp2) и [ECIES-X25519](/docs/specs/ecies)

Другие функции Noise, определенные в других местах:

- MixHash(d) - как в [NTCP2](/docs/specs/ntcp2) и [ECIES-X25519](/docs/specs/ecies)
- MixKey(d) - как в [NTCP2](/docs/specs/ntcp2) и [ECIES-X25519](/docs/specs/ecies)

## Дизайн

ECIES Router SKM не требует полного Ratchet SKM, как указано в [ECIES](/docs/specs/ecies) для Destinations. Нет требования для неанонимных сообщений, использующих паттерн IK. Модель угроз не требует эфемерных ключей, закодированных с помощью Elligator2.

Поэтому router SKM будет использовать паттерн Noise "N", такой же, как указано в [Prop152](/proposals/152-ecies-tunnels) для построения tunnel. Он будет использовать тот же формат полезной нагрузки, как указано в [ECIES](/docs/specs/ecies) для Destinations. Режим нулевого статического ключа (без привязки или сеанса) IK, указанный в [ECIES](/docs/specs/ecies), использоваться не будет.

Ответы на запросы будут зашифрованы с помощью ratchet tag, если это было запрошено в запросе. Это задокументировано в [Prop154](/proposals/154-ecies-lookups) и теперь специфицировано в [I2NP](/docs/specs/i2np).

Данная архитектура позволяет router использовать один ECIES Session Key Manager. Нет необходимости запускать "двойные ключи" Session Key Manager, как описано в [ECIES](/docs/specs/ecies) для Destinations. Router имеют только один публичный ключ.

ECIES router не имеет статического ключа ElGamal. Router по-прежнему нуждается в реализации ElGamal для построения tunnel через ElGamal router и отправки зашифрованных сообщений ElGamal router.

ECIES router МОЖЕТ потребовать частичный ElGamal Session Key Manager для получения ElGamal-помеченных сообщений, полученных в качестве ответов на NetDB запросы от floodfill router'ов версии до 0.9.46, поскольку эти router'ы не имеют реализации ECIES-помеченных ответов, как указано в [Prop152](/proposals/152-ecies-tunnels). В противном случае ECIES router может не запрашивать зашифрованный ответ от floodfill router'а версии до 0.9.46.

Это необязательно. Решение может различаться в разных реализациях I2P и может зависеть от количества узлов сети, которые обновились до версии 0.9.46 или выше. На данный момент приблизительно 85% сети использует версию 0.9.46 или выше.

### Noise Protocol Framework

Данная спецификация предоставляет требования, основанные на [Noise Protocol Framework](https://noiseprotocol.org/noise.html) (Редакция 34, 2018-07-11). В терминологии Noise, Алиса является инициатором, а Боб — отвечающей стороной.

Он основан на протоколе Noise Noise_N_25519_ChaChaPoly_SHA256. Этот протокол Noise использует следующие примитивы:

- **Односторонний шаблон рукопожатия: N** - Алиса не передает свой статический ключ Бобу (N)
- **Функция DH: X25519** - X25519 DH с длиной ключа 32 байта, как указано в [RFC-7748](https://tools.ietf.org/html/rfc7748).
- **Функция шифрования: ChaChaPoly** - AEAD_CHACHA20_POLY1305, как указано в [RFC-7539](https://tools.ietf.org/html/rfc7539) раздел 2.8. 12-байтовый nonce, с первыми 4 байтами, установленными в ноль. Идентично тому, что используется в [NTCP2](/docs/specs/ntcp2).
- **Хеш-функция: SHA256** - Стандартный 32-байтовый хеш, уже широко используемый в I2P.

### Паттерны рукопожатия

Для handshake используются шаблоны handshake протокола [Noise](https://noiseprotocol.org/noise.html).

Используется следующее соответствие букв:

- e = одноразовый эфемерный ключ
- s = статический ключ
- p = полезная нагрузка сообщения

Запрос на построение идентичен шаблону Noise N. Это также идентично первому сообщению (Запрос сессии) в шаблоне XK, используемом в [NTCP2](/docs/specs/ntcp2).

```
<- s
  ...
  e es p ->
```
### Шифрование сообщений

Сообщения создаются и асимметрично шифруются для целевого router. Это асимметричное шифрование сообщений в настоящее время использует ElGamal, как определено в [Cryptography](/docs/specs/cryptography), и содержит контрольную сумму SHA-256. Эта схема не обеспечивает прямую секретность.

Дизайн ECIES использует односторонний Noise паттерн "N" с ECIES-X25519 ephemeral-static DH, с HKDF и ChaCha20/Poly1305 AEAD для прямой секретности, целостности и аутентификации. Алиса — анонимный отправитель сообщения, router или назначение. Целевой ECIES router — Боб.

### Шифрование ответов

Ответы не являются частью этого протокола, поскольку Алиса анонимна. Ключи для ответов, если они есть, включаются в сообщение запроса. См. [спецификацию I2NP](/docs/specs/i2np) для Database Lookup Messages.

Ответы на сообщения Database Lookup являются сообщениями Database Store или Database Search Reply. Они шифруются как сообщения Existing Session с 32-байтовым ключом ответа и 8-байтовым тегом ответа, как указано в [I2NP](/docs/specs/i2np) и [Prop154](/proposals/154-ecies-lookups).

Явных ответов на сообщения Database Store не предусмотрено. Отправитель может включить свой собственный ответ в виде Garlic Message самому себе, содержащего сообщение Delivery Status.

## Спецификация

X25519: См. [ECIES](/docs/specs/ecies).

Идентификация router и сертификат ключа: См. [Общие структуры](/docs/specs/common-structures).

### Шифрование запросов

Шифрование запроса такое же, как указано в [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) и [Prop152](/proposals/152-ecies-tunnels), с использованием шаблона Noise "N".

Ответы на запросы поиска будут зашифрованы с помощью ratchet tag, если это запрошено в поиске. Сообщения запросов Database Lookup содержат 32-байтовый ключ ответа и 8-байтовый тег ответа, как указано в [I2NP](/docs/specs/i2np) и [Prop154](/proposals/154-ecies-lookups). Ключ и тег используются для шифрования ответа.

Наборы тегов не создаются. Схема с нулевым статическим ключом, указанная в ECIES-X25519-AEAD-Ratchet [Prop144](/proposals/144-ecies-x25519-aead-ratchet) и [ECIES](/docs/specs/ecies), использоваться не будет. Эфемерные ключи не будут закодированы с помощью Elligator2.

Обычно это будут сообщения New Session, которые отправляются с нулевым статическим ключом (без привязки или сессии), поскольку отправитель сообщения анонимен.

#### KDF для начальных ck и h

Это стандартный [Noise](https://noiseprotocol.org/noise.html) для паттерна "N" со стандартным именем протокола. Это то же самое, что указано в [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) и [Prop152](/proposals/152-ecies-tunnels) для сообщений построения tunnel.

```
This is the "e" message pattern:

  // Define protocol_name.
  Set protocol_name = "Noise_N_25519_ChaChaPoly_SHA256"
  (31 bytes, US-ASCII encoded, no NULL termination).

  // Define Hash h = 32 bytes
  // Pad to 32 bytes. Do NOT hash it, because it is not more than 32 bytes.
  h = protocol_name || 0

  Define ck = 32 byte chaining key. Copy the h data to ck.
  Set chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // up until here, can all be precalculated by all routers.
```
#### KDF для сообщения

Создатели сообщений генерируют эфемерную X25519 пару ключей для каждого сообщения. Эфемерные ключи должны быть уникальными для каждого сообщения. Это то же самое, что указано в [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) и [Prop152](/proposals/152-ecies-tunnels) для сообщений построения туннелей.

```
  // Target router's X25519 static keypair (hesk, hepk) from the Router Identity
  hesk = GENERATE_PRIVATE()
  hepk = DERIVE_PUBLIC(hesk)

  // MixHash(hepk)
  // || below means append
  h = SHA256(h || hepk);

  // up until here, can all be precalculated by each router
  // for all incoming messages

  // Sender generates an X25519 ephemeral keypair
  sesk = GENERATE_PRIVATE()
  sepk = DERIVE_PUBLIC(sesk)

  // MixHash(sepk)
  h = SHA256(h || sepk);

  End of "e" message pattern.

  This is the "es" message pattern:

  // Noise es
  // Sender performs an X25519 DH with receiver's static public key.
  // The target router
  // extracts the sender's ephemeral key preceding the encrypted record.
  sharedSecret = DH(sesk, hepk) = DH(hesk, sepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // ChaChaPoly parameters to encrypt/decrypt
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  // Chain key is not used
  //chainKey = keydata[0:31]

  // AEAD parameters
  k = keydata[32:63]
  n = 0
  plaintext = 464 byte build request record
  ad = h
  ciphertext = ENCRYPT(k, n, plaintext, ad)

  End of "es" message pattern.

  // MixHash(ciphertext) is not required
  //h = SHA256(h || ciphertext)
```
#### Полезная нагрузка

Полезная нагрузка имеет тот же формат блока, что определен в [ECIES](/docs/specs/ecies) и [Prop144](/proposals/144-ecies-x25519-aead-ratchet). Все сообщения должны содержать блок DateTime для предотвращения повторных атак.

## Примечания по реализации

- Старые router не проверяют тип шифрования router и будут отправлять сообщения, зашифрованные ElGamal. Некоторые недавние router содержат ошибки и будут отправлять различные типы некорректных сообщений. Разработчики должны обнаруживать и отклонять эти записи до операции DH, если это возможно, чтобы снизить загрузку процессора.

## Справочные материалы

- [Общие структуры](/docs/specs/common-structures)
- [Криптография](/docs/specs/cryptography)
- [ECIES](/docs/specs/ecies)
- [I2NP](/docs/specs/i2np)
- [Noise Protocol Framework](https://noiseprotocol.org/noise.html)
- [NTCP2](/docs/specs/ntcp2)
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet)
- [Prop152](/proposals/152-ecies-tunnels)
- [Prop154](/proposals/154-ecies-lookups)
- [Prop156](/proposals/156-ecies-routers)
- [RFC-7539](https://tools.ietf.org/html/rfc7539)
- [RFC-7748](https://tools.ietf.org/html/rfc7748)
- [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies)
