---
title: "Спецификация общих структур"
description: "Типы данных, общие для всех протоколов I2P"
slug: "common-structures"
category: "Дизайн"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

Этот документ описывает некоторые типы данных, общие для всех протоколов I2P, таких как [I2NP](/docs/specs/i2np/), [I2CP](/docs/specs/i2cp/), [SSU](/docs/legacy/ssu/) и др.

## Спецификация общего типа

### Целое число

#### Описание

Представляет неотрицательное целое число.

#### Содержание

От 1 до 8 байт в сетевом порядке байтов (big endian), представляющие беззнаковое целое число.

### Дата

#### Описание

Количество миллисекунд с полуночи 1 января 1970 года по времени GMT. Если число равно 0, дата не определена или null.

#### Содержание

8-байтное [Integer](#integer)

### Строка

#### Описание

Представляет строку в кодировке UTF-8.

#### Содержание

1 или более байт, где первый байт - это количество байт (не символов!) в строке, а остальные 0-255 байт представляют собой массив символов в кодировке UTF-8 без завершающего нулевого символа. Ограничение длины составляет 255 байт (не символов). Длина может быть равна 0.

### PublicKey

#### Описание

Эта структура используется в ElGamal или другом асимметричном шифровании, представляя только экспоненту, а не простые числа, которые являются константами и определены в спецификации криптографии [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy). Другие схемы шифрования находятся в процессе определения, см. таблицу ниже.

#### Содержание

Тип и длина ключа выводятся из контекста или указываются в сертификате ключа Destination или RouterInfo, или в полях [LeaseSet2](#leaseset2) или другой структуре данных. Тип по умолчанию — ElGamal. Начиная с версии 0.9.38 могут поддерживаться другие типы в зависимости от контекста. Ключи представлены в формате big-endian, если не указано иное.

Ключи X25519 поддерживаются в Destinations и LeaseSet2 начиная с версии 0.9.44. Ключи X25519 поддерживаются в RouterIdentities начиная с версии 0.9.48.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there; discouraged for leasesets</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Little-endian. See <a href="/docs/specs/ecies/">ECIES</a> and <a href="/docs/specs/ecies-routers/">ECIES-ROUTERS</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">800</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1184</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1568</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1088</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_CT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1568</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/PublicKey.html

### PrivateKey

#### Описание

Эта структура используется в ElGamal или других алгоритмах асимметричного расшифрования, представляя только экспоненту, а не простые числа, которые являются константами и определены в спецификации криптографии [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy). Другие схемы шифрования находятся в процессе определения, см. таблицу ниже.

#### Содержание

Тип и длина ключа выводятся из контекста или хранятся отдельно в структуре данных или файле приватного ключа. Тип по умолчанию — ElGamal. Начиная с версии 0.9.38 могут поддерживаться другие типы в зависимости от контекста. Ключи имеют порядок байтов big-endian, если не указано иное.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there; discouraged for leasesets</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">48</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">66</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Little-endian. See <a href="/docs/specs/ecies/">ECIES</a> and <a href="/docs/specs/ecies-routers/">ECIES-ROUTERS</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1632</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2400</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3168</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for handshakes only, not for Leasesets, RIs or Destinations</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/PrivateKey.html

### SessionKey

#### Описание

Эта структура используется для симметричного шифрования и дешифрования AES256.

#### Содержание

32 байта

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionKey.html

### SigningPublicKey

#### Описание

Эта структура используется для проверки подписей.

#### Содержание

Тип и длина ключа определяются из контекста или указываются в Key Certificate пункта назначения. Тип по умолчанию — DSA_SHA1. Начиная с версии 0.9.12, в зависимости от контекста могут поддерживаться другие типы.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### Примечания

* Когда ключ состоит из двух элементов (например, точки X,Y), он сериализуется путем дополнения каждого элемента до длины/2 ведущими нулями при необходимости.

* Все типы имеют порядок байтов Big Endian, за исключением EdDSA и RedDSA, которые хранятся и передаются в формате Little Endian.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPublicKey.html

### SigningPrivateKey

#### Описание

Эта структура используется для создания цифровых подписей.

#### Содержание

Тип и длина ключа указываются при создании. Тип по умолчанию — DSA_SHA1. Начиная с версии 0.9.12, другие типы могут поддерживаться в зависимости от контекста.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">48</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">66</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">768</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1024</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### Примечания

* Когда ключ состоит из двух элементов (например, точек X,Y), он
  сериализуется путем дополнения каждого элемента до длины/2 ведущими нулями при
  необходимости.

* Все типы используют порядок байтов Big Endian, за исключением EdDSA и RedDSA, которые хранятся и передаются в формате Little Endian.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SigningPrivateKey.html

### Подпись

#### Описание

Эта структура представляет подпись некоторых данных.

#### Содержание

Тип и длина подписи выводятся из типа используемого ключа. Тип по умолчанию — DSA_SHA1. Начиная с версии 0.9.12, могут поддерживаться другие типы в зависимости от контекста.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length (bytes)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">40</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 09.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline signing, never used for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only, never used for Router Identities</td>
    </tr>
  </tbody>
</table>
#### Примечания

* Когда подпись состоит из двух элементов (например, значений R,S), она сериализуется путем дополнения каждого элемента до длины/2 ведущими нулями при необходимости.

* Все типы используют порядок байтов Big Endian, за исключением EdDSA и RedDSA, которые хранятся и передаются в формате Little Endian.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Signature.html

### Хеш

#### Описание

Представляет SHA256 некоторых данных.

#### Содержание

32 байта

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Hash.html

### Тег сессии

Примечание: Session Tags для ECIES-X25519 назначений (ratchet) и ECIES-X25519 роутеров составляют 8 байт. См. [ECIES](/docs/specs/ecies/) и [ECIES-ROUTERS](/docs/specs/ecies-routers/).

#### Описание

Случайное число

#### Содержание

32 байта

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/SessionTag.html

### TunnelId

#### Описание

Определяет идентификатор, который является уникальным для каждого router в tunnel. Tunnel ID обычно больше нуля; не используйте значение ноль, за исключением особых случаев.

#### Содержание

4 байта [Integer](#integer)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/TunnelId.html

### Сертификат

#### Описание

Сертификат представляет собой контейнер для различных квитанций или подтверждений выполненной работы, используемых в сети I2P.

#### Содержание

1 байт [Integer](#integer), указывающий тип сертификата, за которым следует 2-байтный [Integer](#integer), указывающий размер полезной нагрузки сертификата, затем соответствующее количество байтов.

```
+----+----+----+----+----+-/
|type| length  | payload
+----+----+----+----+----+-/

type :: `Integer`
        length -> 1 byte

        case 0 -> NULL
        case 1 -> HASHCASH
        case 2 -> HIDDEN
        case 3 -> SIGNED
        case 4 -> MULTIPLE
        case 5 -> KEY

length :: `Integer`
          length -> 2 bytes

payload :: data
           length -> $length bytes
```
#### Примечания

* Для [Router Identities](#routeridentity) сертификат всегда равен NULL до версии
  0.9.15. Начиная с версии 0.9.16 используется Key Certificate для указания
  типов ключей. Начиная с версии 0.9.48 разрешены типы публичных ключей
  шифрования X25519. См. ниже.

* Для [Garlic Cloves](/docs/specs/i2np/#struct-garlicclove), сертификат всегда NULL, никаких других в настоящее время не реализовано.

* Для [Garlic Messages](/docs/specs/i2np/#msg-garlic), Certificate всегда равен NULL, другие в настоящее время не реализованы.

* Для [Destinations](#destination), Certificate может быть не-NULL. Начиная с версии 0.9.12, Key Certificate может использоваться для указания типа публичного ключа подписи. См. ниже.

* Разработчикам рекомендуется запретить избыточные данные в сертификатах.
  Для каждого типа сертификата должна соблюдаться соответствующая длина.

#### Типы сертификатов

Определены следующие типы сертификатов:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">HashCash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains an ASCII colon-separated hashcash string.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Hidden</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Hidden routers generally do not announce that they are hidden.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Signed</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">40 or 72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">43 or 75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains a 40-byte DSA signature, optionally followed by the 32-byte Hash of the signing Destination.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Multiple</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated, unused. Payload contains multiple certificates.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4+</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7+</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Since 0.9.12. See below for details.</td>
    </tr>
  </tbody>
</table>
#### Сертификаты ключей

Сертификаты ключей были введены в версии 0.9.12. До этой версии все PublicKeys были 256-байтными ключами ElGamal, а все SigningPublicKeys были 128-байтными ключами DSA-SHA1. Сертификат ключа предоставляет механизм для указания типа PublicKey и SigningPublicKey в Destination или RouterIdentity, а также для упаковки любых данных ключа, превышающих стандартные длины.

Поддерживая точно 384 байта перед сертификатом и помещая любые избыточные данные ключа внутрь сертификата, мы сохраняем совместимость с любым программным обеспечением, которое анализирует Destinations и Router Identities.

Полезная нагрузка ключевого сертификата содержит:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Signing Public Key Type (<a href="#integer">Integer</a>)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Crypto Public Key Type (<a href="#integer">Integer</a>)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Excess Signing Public Key Data</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0+</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Excess Crypto Public Key Data</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0+</td>
    </tr>
  </tbody>
</table>
Предупреждение: Порядок типов ключей противоположен тому, что вы можете ожидать; тип открытого ключа подписи идет первым.

Определенные типы открытых ключей подписи:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Public Key Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; discouraged for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Older Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely if ever used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Rarely if ever used for Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">512</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Recent Router Identities and Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.25</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Offline only; never used in Key Certificates for Router Identities or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (GOST)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/134-gost/">Prop134</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (GOST)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/134-gost/">Prop134</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RedDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">For Destinations and encrypted leasesets only; never used for Router Identities</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">13</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">14</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (MLDSA)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65280-65534</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for experimental use</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65535</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for future expansion</td>
    </tr>
  </tbody>
</table>
Определённые типы криптографических публичных ключей:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Code</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total Public Key Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Since</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Deprecated for Router Identities as of 0.9.58; use for Destinations, as the public key field is unused there</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">132</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see proposal 145</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.38</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies/">ECIES</a> and proposal 156</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM512_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM768_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MLKEM1024_X25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.67</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">See <a href="/docs/specs/ecies-hybrid/">ECIES-HYBRID</a>, for Leasesets only, not for RIs or Destinations</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved (NONE)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">255</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved, see <a href="/proposals/169-pq-crypto/">Prop169</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65280-65534</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for experimental use</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">65535</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Reserved for future expansion</td>
    </tr>
  </tbody>
</table>
Когда Key Certificate отсутствует, предыдущие 384 байта в Destination или RouterIdentity определяются как 256-байтный ElGamal PublicKey, за которым следует 128-байтный DSA-SHA1 SigningPublicKey. Когда Key Certificate присутствует, предыдущие 384 байта переопределяются следующим образом:

* Полный или первая часть криптографического открытого ключа

* Случайное заполнение, если общая длина двух ключей составляет менее 384 байт

* Полный или первая часть открытого ключа для подписи

Криптографический открытый ключ выравнивается по началу, а открытый ключ подписи выравнивается по концу. Отступы (если есть) располагаются в середине. Длины и границы исходных ключевых данных, отступов и избыточных ключевых данных в сертификатах не указываются явно, а выводятся из длин указанных типов ключей. Если общая длина криптографического и открытого ключей подписи превышает 384 байта, остаток будет содержаться в Key Certificate. Если длина криптографического открытого ключа не составляет 256 байт, метод определения границы между двумя ключами будет указан в будущей редакции этого документа.

Примеры схем с использованием криптографического открытого ключа ElGamal и указанного типа открытого ключа для подписи:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Signing Key Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Excess Signing Key Data in Cert</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA256_P256</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA384_P384</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA_SHA512_P521</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA256_2048</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA384_3072</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">256</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RSA_SHA512_4096</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">384</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA_SHA512_Ed25519ph</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
    </tr>
  </tbody>
</table>
JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Certificate.html

#### Примечания

* Разработчикам рекомендуется запретить избыточные данные в сертификатах ключей.
  Следует обеспечить соблюдение соответствующей длины для каждого типа сертификата.

* KEY сертификат с типами 0,0 (ElGamal,DSA_SHA1) разрешен, но не рекомендуется.
  Он недостаточно протестирован и может вызвать проблемы в некоторых реализациях.
  Используйте NULL сертификат в каноническом представлении
  (ElGamal,DSA_SHA1) Destination или RouterIdentity, который будет на 4 байта короче,
  чем при использовании KEY сертификата.

### Сопоставление

#### Описание

Набор сопоставлений ключ/значение или свойств

#### Содержание

2-байтовое целое число размера, за которым следует серия пар String=String;

ПРЕДУПРЕЖДЕНИЕ: Большинство случаев использования Mapping находятся в подписанных структурах, где записи Mapping должны быть отсортированы по ключу, чтобы подпись была неизменяемой. Несоблюдение сортировки по ключу приведет к ошибкам подписи!

```
+----+----+----+----+----+----+----+----+
|  size   | key_string (len + data)| =  |
+----+----+----+----+----+----+----+----+
| val_string (len + data)     | ;  | ...
+----+----+----+----+----+----+----+
size :: `Integer`
        length -> 2 bytes
        Total number of bytes that follow

key_string :: `String`
              A string (one byte length followed by UTF-8 encoded characters)

= :: A single byte containing '='

val_string :: `String`
              A string (one byte length followed by UTF-8 encoded characters)

; :: A single byte containing ';'
```
#### Примечания

* Кодирование не является оптимальным - нам нужны либо символы '=' и ';', либо
  длины строк, но не то и другое одновременно

* В некоторой документации говорится, что строки не могут содержать '=' или ';', но данная кодировка их поддерживает

* Строки определены как UTF-8, но в текущей реализации I2CP использует UTF-8, а I2NP - нет. Например, UTF-8 строки в маппинге опций RouterInfo в I2NP Database Store Message будут повреждены.

* Кодировка допускает дублирующиеся ключи, однако при любом использовании, где отображение подписано, дубликаты могут привести к сбою подписи.

* Сопоставления, содержащиеся в I2NP сообщениях (например, в RouterAddress или RouterInfo), должны быть отсортированы по ключу, чтобы подпись была инвариантной. Дублирование ключей не допускается.

* Сопоставления, содержащиеся в [I2CP SessionConfig](/docs/specs/i2cp/#struct-sessionconfig), должны быть отсортированы по ключу, чтобы подпись оставалась неизменной. Дублирующиеся ключи не допускаются.

* Метод сортировки определён как в Java String.compareTo(), используя Unicode значения символов.

* Хотя это зависит от приложения, ключи и значения обычно чувствительны к регистру.

* Ограничения длины строк ключа и значения составляют 255 байт (не символов) каждая, плюс
  байт длины. Байт длины может быть равен 0.

* Общее ограничение по длине составляет 65535 байт, плюс 2-байтовое поле размера, или всего 65537 байт.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/DataHelper.html

## Спецификация общей структуры

### KeysAndCert

#### Описание

Открытый ключ шифрования, открытый ключ подписи и сертификат, используемые как RouterIdentity или Destination.

#### Содержание

[PublicKey](#publickey), за которым следует [SigningPublicKey](#signingpublickey), а затем [Certificate](#certificate).

```
+----+----+----+----+----+----+----+----+
| public_key                            |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| padding (optional)                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signing_key                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| certificate                           |
+----+----+----+-/

public_key :: `PublicKey` (partial or full)
              length -> 256 bytes or as specified in key certificate

padding :: random data
           length -> 0 bytes or as specified in key certificate
           public_key length + padding length + signing_key length == 384 bytes

signing__key :: `SigningPublicKey` (partial or full)
                length -> 128 bytes or as specified in key certificate

certificate :: `Certificate`
               length -> >= 3 bytes

total length: 387+ bytes
```
#### Руководство по генерации отступов

Эти рекомендации были предложены в Предложении 161 и реализованы в версии API 0.9.57. Эти рекомендации обратно совместимы со всеми версиями начиная с 0.6 (2005). См. Предложение 161 для справочной информации и дополнительных сведений.

Для любой используемой в настоящее время комбинации типов ключей, отличной от ElGamal + DSA-SHA1, будет присутствовать заполнение. Кроме того, для назначений поле открытого ключа размером 256 байт не использовалось с версии 0.6 (2005).

Разработчики должны генерировать случайные данные для публичных ключей Destination и заполнения Destination и Router Identity таким образом, чтобы они были сжимаемыми в различных протоколах I2P, оставаясь при этом безопасными, и чтобы представления Base 64 не выглядели поврежденными или небезопасными. Это обеспечивает большинство преимуществ удаления полей заполнения без каких-либо разрушительных изменений протокола.

Строго говоря, только 32-байтовый открытый ключ подписи (как в Destinations, так и в Router Identities) и 32-байтовый открытый ключ шифрования (только в Router Identities) представляет собой случайное число, которое обеспечивает всю энтропию, необходимую для того, чтобы SHA-256 хеши этих структур были криптографически стойкими и случайно распределенными в DHT базы данных сети.

Однако из соображений повышенной осторожности мы рекомендуем использовать минимум 32 байта случайных данных в поле открытого ключа ElG и заполнении. Кроме того, если все поля были бы нулевыми, Base 64 адреса назначения содержали бы длинные последовательности символов AAAA, что может вызвать тревогу или путаницу у пользователей.

Повторяйте 32 байта случайных данных по необходимости, чтобы полная структура KeysAndCert была хорошо сжимаемой в протоколах I2P, таких как I2NP Database Store Message, Streaming SYN, SSU2 handshake и repliable Datagrams.

Примеры:

* Router Identity с типом шифрования X25519 и типом подписи Ed25519
  будет содержать 10 копий (320 байт) случайных данных, что даст экономию примерно 288 байт при сжатии.

* Destination с типом подписи Ed25519
  будет содержать 11 копий (352 байта) случайных данных, что даёт экономию примерно 320 байт при сжатии.

Реализации должны, конечно же, сохранять полную структуру размером 387+ байт, поскольку SHA-256 хеш структуры охватывает все содержимое.

#### Примечания

* Не предполагайте, что они всегда составляют 387 байт! Они составляют 387 байт плюс длина сертификата, указанная в байтах 385-386, которая может быть ненулевой.

* Начиная с релиза 0.9.12, если сертификат является Key Certificate, границы полей ключей могут варьироваться. См. раздел Key Certificate выше для получения подробной информации.

* Криптографический публичный ключ выровнен по началу, а публичный ключ для подписи выровнен по концу. Заполнение (если есть) находится посередине.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/KeysAndCert.html

### RouterIdentity

#### Описание

Определяет способ уникальной идентификации конкретного router

#### Содержание

Идентично KeysAndCert.

См. [KeysAndCert](#keysandcert) для рекомендаций по генерации случайных данных для поля заполнения.

#### Примечания

* Сертификат для RouterIdentity всегда был NULL до релиза 0.9.12.

* Не предполагайте, что они всегда составляют 387 байт! Они составляют 387 байт плюс длина сертификата, указанная в байтах 385-386, которая может быть ненулевой.

* Начиная с версии 0.9.12, если сертификат является Key Certificate, границы полей ключа могут варьироваться. Подробности см. в разделе Key Certificate выше.

* Криптографический публичный ключ выравнивается по началу, а публичный ключ подписи выравнивается по концу. Заполнение (если есть) находится посередине.

* RouterIdentities с сертификатом ключа и открытым ключом ECIES_X25519
  поддерживаются начиная с версии 0.9.48.
  До этого все RouterIdentities были ElGamal.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterIdentity.html

### Назначение

#### Описание

Destination определяет конкретную конечную точку, к которой могут быть направлены сообщения для безопасной доставки.

#### Содержание

Идентичен [KeysAndCert](#keysandcert), за исключением того, что публичный ключ никогда не используется и может содержать случайные данные вместо действительного публичного ключа ElGamal.

См. [KeysAndCert](#keysandcert) для руководства по генерации случайных данных для полей открытого ключа и заполнения.

#### Примечания

* Публичный ключ назначения использовался для старого i2cp-to-i2cp
  шифрования, которое было отключено в версии 0.6 (2005), в настоящее время он не используется, за исключением
  IV для шифрования LeaseSet, что является устаревшим. Вместо этого используется публичный ключ в
  LeaseSet.

* Не предполагайте, что они всегда имеют размер 387 байт! Они имеют размер 387 байт плюс длина сертификата, указанная в байтах 385-386, которая может быть ненулевой.

* Начиная с релиза 0.9.12, если сертификат является Key Certificate, границы полей ключей могут различаться. Подробности см. в разделе Key Certificate выше.

* Криптографический открытый ключ выравнивается по началу, а подписывающий открытый ключ выравнивается по концу. Заполнение (если есть) находится посередине.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Destination.html

### Lease

#### Описание

Определяет авторизацию для конкретного tunnel на получение сообщений, предназначенных для [Destination](#destination).

#### Содержание

SHA256 [Hash](#hash) от [RouterIdentity](#routeridentity) шлюзового router, затем [TunnelId](#tunnelid), и наконец конечная [Date](#date).

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     tunnel_id     |      end_date
+----+----+----+----+----+----+----+----+
                    |
+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway
             length -> 32 bytes

tunnel_id :: `TunnelId`
             length -> 4 bytes

end_date :: `Date`
            length -> 8 bytes
```
#### Заметки

* Общий размер: 44 байта

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease.html

### LeaseSet

#### Описание

Содержит все текущие авторизованные [Leases](#lease) для определённого [Destination](#destination), [PublicKey](#publickey), с помощью которого могут быть зашифрованы garlic-сообщения, а затем [SigningPublicKey](#signingpublickey), который может использоваться для отзыва данной конкретной версии структуры. LeaseSet является одной из двух структур, хранящихся в сетевой базе данных (другой является [RouterInfo](#routerinfo)), и индексируется по SHA256 от содержащегося [Destination](#destination).

#### Содержание

[Destination](#destination), за которым следует [PublicKey](#publickey) для шифрования, затем [SigningPublicKey](#signingpublickey), который может использоваться для отзыва данной версии LeaseSet, затем 1-байтовое [Integer](#integer), указывающее количество структур [Lease](#lease) в наборе, после чего идут фактические структуры [Lease](#lease) и, наконец, [Signature](#signature) предыдущих байтов, подписанная [SigningPrivateKey](#signingprivatekey) [Destination](#destination).

```
+----+----+----+----+----+----+----+----+
| destination                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| encryption_key                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signing_key                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| Lease 0                          |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease 1                               |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease ($num-1)                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
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

destination :: `Destination`
               length -> >= 387+ bytes

encryption_key :: `PublicKey`
                  length -> 256 bytes

signing_key :: `SigningPublicKey`
               length -> 128 bytes or as specified in destination's key
                         certificate

num :: `Integer`
       length -> 1 byte
       Number of leases to follow
       value: 0 <= num <= 16

leases :: [`Lease`]
          length -> $num*44 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate
```
#### Примечания

* Публичный ключ назначения использовался для старого шифрования I2CP-к-I2CP, которое было отключено в версии 0.6, в настоящее время он не используется.

* Ключ шифрования используется для сквозного шифрования ElGamal/AES+SessionTag
  [ELGAMAL-AES](/docs/specs/elgamal-aes/). В настоящее время он генерируется заново при каждом запуске router, он не является постоянным.

* Подпись может быть проверена с использованием открытого ключа подписи получателя.

* LeaseSet с нулевым количеством Lease разрешен, но не используется.
  Он предназначался для отзыва LeaseSet, что не реализовано.
  Все варианты LeaseSet2 требуют как минимум один Lease.

* signing_key в настоящее время не используется. Он предназначался для отзыва LeaseSet, что не реализовано. В настоящее время он генерируется заново при каждом запуске router'а и не является постоянным. Тип signing key всегда совпадает с типом signing key назначения.

* Самое раннее истечение срока действия всех Lease рассматривается как временная метка или версия LeaseSet. Router'ы обычно не принимают сохранение LeaseSet, если он не "новее" текущего. Будьте осторожны при публикации нового LeaseSet, где самый старый Lease совпадает с самым старым Lease в предыдущем LeaseSet. В таком случае публикующий router должен обычно увеличить срок истечения самого старого Lease как минимум на 1 мс.

* До релиза 0.9.7, когда включался в сообщение DatabaseStore, отправленное исходным router'ом, router устанавливал время истечения всех опубликованных lease'ов на одно и то же значение - значение самого раннего lease. Начиная с релиза 0.9.7, router публикует фактическое время истечения для каждого lease. Это деталь реализации, а не часть спецификации структур.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet.html

### Lease2

#### Описание

Определяет авторизацию для конкретного tunnel на получение сообщений, направленных к [Destination](#destination). То же самое, что и [Lease](#lease), но с 4-байтовым end_date. Используется [LeaseSet2](#leaseset2). Поддерживается начиная с версии 0.9.38; см. предложение 123 для получения дополнительной информации.

#### Содержание

SHA256 [Hash](#hash) от [RouterIdentity](#routeridentity) gateway router, затем [TunnelId](#tunnelid), и наконец 4-байтная дата окончания.

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     tunnel_id     |      end_date     |
+----+----+----+----+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway
             length -> 32 bytes

tunnel_id :: `TunnelId`
             length -> 4 bytes

end_date :: 4 byte date
            length -> 4 bytes
            Seconds since the epoch, rolls over in 2106.

```
#### Примечания

* Общий размер: 40 байт

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/Lease2.html

### OfflineSignature

#### Описание

Это необязательная часть [LeaseSet2Header](#leaseset2header). Также используется в streaming и I2CP. Поддерживается с версии 0.9.38; см. предложение 123 для получения дополнительной информации.

#### Содержание

Содержит срок действия, тип подписи и временный [SigningPublicKey](#signingpublickey), а также [Signature](#signature).

```
+----+----+----+----+----+----+----+----+
|     expires       | sigtype |         |
+----+----+----+----+----+----+         +
|       transient_public_key            |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|           signature                   |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

expires :: 4 byte date
           length -> 4 bytes
           Seconds since the epoch, rolls over in 2106.

sigtype :: 2 byte type of the transient_public_key
           length -> 2 bytes

transient_public_key :: `SigningPublicKey`
                        length -> As inferred from the sigtype

signature :: `Signature`
             length -> As inferred from the sigtype of the signing public key
                       in the `Destination` that preceded this offline signature.
             Signature of expires timestamp, transient sig type, and public key,
             by the destination public key.

```
#### Примечания

* Этот раздел может и должен быть сгенерирован в офлайн-режиме.

### LeaseSet2Header

#### Описание

Это общая часть [LeaseSet2](#leaseset2) и [MetaLeaseSet](#metaleaseset). Поддерживается начиная с версии 0.9.38; см. предложение 123 для получения дополнительной информации.

#### Содержание

Содержит [Destination](#destination), две временные метки и необязательную [OfflineSignature](#offlinesignature).

```
+----+----+----+----+----+----+----+----+
| destination                           |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|     published     | expires |  flags  |
+----+----+----+----+----+----+----+----+
| offline_signature (optional)          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

destination :: `Destination`
               length -> >= 387+ bytes

published :: 4 byte date
             length -> 4 bytes
             Seconds since the epoch, rolls over in 2106.

expires :: 2 byte time
           length -> 2 bytes
           Offset from published timestamp in seconds, 18.2 hours max

flags :: 2 bytes
  Bit order: 15 14 ... 3 2 1 0
  Bit 0: If 0, no offline keys; if 1, offline keys
  Bit 1: If 0, a standard published leaseset.
         If 1, an unpublished leaseset. Should not be flooded, published, or
         sent in response to a query. If this leaseset expires, do not query the
         netdb for a new one, unless bit 2 is set.
  Bit 2: If 0, a standard published leaseset.
         If 1, this unencrypted leaseset will be blinded and encrypted when published.
         If this leaseset expires, query the blinded location in the netdb for a new one.
         If this bit is set to 1, set bit 1 to 1 also.
         As of release 0.9.42.
  Bits 15-3: set to 0 for compatibility with future uses

offline_signature :: `OfflineSignature`
                     length -> varies
                     Optional, only present if bit 0 is set in the flags.

```
#### Примечания

* Общий размер: минимум 395 байт

* Максимальное фактическое время истечения составляет около 660 (11 минут) для
  [LeaseSet2](#leaseset2) и 65535 (полные 18,2 часа) для [MetaLeaseSet](#metaleaseset).

* [LeaseSet](#leaseset) (1) не имел поля 'published', поэтому для версионирования требовался
  поиск самого раннего lease. LeaseSet2 добавляет поле 'published'
  с разрешением в одну секунду. Router'ы должны ограничивать скорость отправки
  новых leasesets к floodfill'ам до частоты намного медленнее, чем раз в секунду (на пункт назначения).
  Если это не реализовано, то код должен обеспечить, что каждый новый leaseset
  имеет время 'published' как минимум на одну секунду позже предыдущего, иначе
  floodfill'ы не будут сохранять или распространять новый leaseset.

### LeaseSet2

#### Описание

Содержится в I2NP сообщении DatabaseStore типа 3. Поддерживается начиная с версии 0.9.38; см. предложение 123 для получения дополнительной информации.

Содержит все текущие авторизованные [Lease2](#lease2) для конкретного [Destination](#destination), и [PublicKey](#publickey), с помощью которого можно зашифровать garlic-сообщения. LeaseSet — это одна из двух структур, хранящихся в сетевой базе данных (другая — [RouterInfo](#routerinfo)), и она индексируется по SHA256 содержащегося [Destination](#destination).

#### Содержание

[LeaseSet2Header](#leaseset2header), за которым следуют опции, затем один или более [PublicKey](#publickey) для шифрования, [Integer](#integer), указывающий количество структур [Lease2](#lease2) в наборе, за которыми следуют фактические структуры [Lease2](#lease2) и, наконец, [Signature](#signature) предыдущих байтов, подписанная [SigningPrivateKey](#signingprivatekey) [Destination](#destination) или временным ключом.

```
+----+----+----+----+----+----+----+----+
|         ls2_header                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          options                      |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|numk| keytype0| keylen0 |              |
+----+----+----+----+----+              +
|          encryption_key_0             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| keytypen| keylenn |                   |
+----+----+----+----+                   +
|          encryption_key_n             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| Lease2 0                         |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| Lease2($num-1)                        |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

ls2header :: `LeaseSet2Header`
             length -> varies

options :: `Mapping`
           length -> varies, 2 bytes minimum

numk :: `Integer`
        length -> 1 byte
        Number of key types, key lengths, and `PublicKey`s to follow
        value: 1 <= numk <= max TBD

keytype :: The encryption type of the `PublicKey` to follow.
           length -> 2 bytes

keylen :: The length of the `PublicKey` to follow.
          Must match the specified length of the encryption type.
          length -> 2 bytes

encryption_key :: `PublicKey`
                  length -> keylen bytes

num :: `Integer`
       length -> 1 byte
       Number of `Lease2`s to follow
       value: 0 <= num <= 16

leases :: [`Lease2`]
          length -> $num*40 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate, or by the sigtype of the transient public key,
                       if present in the header

```
#### Предпочтения ключа шифрования

Для опубликованных (серверных) leaseSet ключи шифрования расположены в порядке предпочтения сервера, наиболее предпочтительные первые. Если клиенты поддерживают более одного типа шифрования, рекомендуется учитывать предпочтения сервера и выбирать первый поддерживаемый тип в качестве метода шифрования для подключения к серверу. Обычно новые (с большими номерами) типы ключей более безопасны или эффективны и являются предпочтительными, поэтому ключи должны быть перечислены в обратном порядке типа ключа.

Однако клиенты могут, в зависимости от реализации, выбирать на основе собственных предпочтений или использовать какой-либо метод для определения "комбинированных" предпочтений. Это может быть полезно как опция конфигурации или для отладки.

Порядок ключей в неопубликованных (клиентских) leaseSet фактически не имеет значения, поскольку соединения обычно не будут предприниматься к неопубликованным клиентам. Если только этот порядок не используется для определения комбинированного предпочтения, как описано выше.

#### Опции

Начиная с API 0.9.66, определен стандартный формат для опций записей сервиса. Подробности смотрите в предложении 167. В будущем могут быть определены опции, отличные от записей сервиса, использующие другой формат.

Опции LS2 ДОЛЖНЫ быть отсортированы по ключу, чтобы подпись была инвариантной.

Параметры записи сервиса определяются следующим образом:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := Символическое имя желаемого сервиса. Должно быть в нижнем регистре. Пример: "smtp".
  Разрешённые символы [a-z0-9-], не должно начинаться или заканчиваться на '-'.
  Должны использоваться стандартные идентификаторы из [REGISTRY](http://www.dns-sd.org/ServiceTypes.html) или Linux /etc/services, если они там определены.
- proto := Транспортный протокол желаемого сервиса. Должен быть в нижнем регистре, либо "tcp", либо "udp".
  "tcp" означает потоковый, а "udp" означает дейтаграммы с возможностью ответа.
  Индикаторы протокола для сырых дейтаграмм и datagram2 могут быть определены позже.
  Разрешённые символы [a-z0-9-], не должен начинаться или заканчиваться на '-'.
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := время жизни, целое число секунд. Положительное целое число. Пример: "86400".
  Рекомендуется минимум 86400 (один день), подробности см. в разделе Рекомендации ниже.
- priority := Приоритет целевого хоста, меньшее значение означает более предпочтительный. Неотрицательное целое число. Пример: "0"
  Полезно только при наличии более одной записи, но требуется даже при единственной записи.
- weight := Относительный вес для записей с одинаковым приоритетом. Большее значение означает больше шансов быть выбранным. Неотрицательное целое число. Пример: "0"
  Полезно только при наличии более одной записи, но требуется даже при единственной записи.
- port := I2CP порт, на котором можно найти сервис. Неотрицательное целое число. Пример: "25"
  Порт 0 поддерживается, но не рекомендуется.
- target := Имя хоста или b32 назначения, предоставляющего сервис. Действительное имя хоста как в [NAMING](/docs/overview/naming/). Должно быть в нижнем регистре.
  Пример: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" или "example.i2p".
  b32 рекомендуется, если только имя хоста не является "общеизвестным", т.е. находится в официальных или стандартных адресных книгах.
- appoptions := произвольный текст, специфичный для приложения, не должен содержать " " или ",". Кодировка UTF-8.

Примеры:

В LS2 для aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, указывающем на один SMTP-сервер:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

В LS2 для aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, указывающем на два SMTP сервера:

"_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

В LS2 для bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p, указывающем на себя как на SMTP-сервер:

"_smtp._tcp" "0 999999 25"

#### Примечания

* Публичный ключ назначения использовался для старого шифрования I2CP-to-I2CP, которое было отключено в версии 0.6, в настоящее время не используется.

* Ключи шифрования используются для сквозного шифрования ElGamal/AES+SessionTag
  [ELGAMAL-AES](/docs/specs/elgamal-aes/) (тип 0) или других схем сквозного шифрования.
  См. [ECIES](/docs/specs/ecies/) и предложения 145 и 156.
  Они могут генерироваться заново при каждом запуске router'а
  или могут быть постоянными.
  X25519 (тип 4, см. [ECIES](/docs/specs/ecies/)) поддерживается начиная с релиза 0.9.44.

* Подпись применяется к данным выше, ПРЕДВАРЯЕМЫМ одним байтом, содержащим тип DatabaseStore (3).

* Подпись может быть проверена с использованием публичного ключа подписи назначения или временного публичного ключа подписи, если автономная подпись включена в заголовок leaseset2.

* Длина ключа указывается для каждого ключа, чтобы floodfill и клиенты могли анализировать структуру, даже если не все типы шифрования известны или поддерживаются.

* См. примечание к полю 'published' в [LeaseSet2Header](#leaseset2header)

* Отображение опций, если размер больше единицы, должно быть отсортировано по ключу, чтобы подпись была инвариантной.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/LeaseSet2.html

### MetaLease

#### Описание

Определяет авторизацию для конкретного tunnel на получение сообщений, нацеленных на [Destination](#destination). То же самое, что и [Lease2](#lease2), но с флагами и стоимостью вместо tunnel id. Используется [MetaLeaseSet](#metaleaseset). Содержится в I2NP DatabaseStore сообщении типа 7. Поддерживается начиная с версии 0.9.38; смотрите proposal 123 для получения дополнительной информации.

#### Содержание

SHA256 [Hash](#hash) от [RouterIdentity](#routeridentity) шлюзового роутера, затем флаги и стоимость, и наконец 4-байтная дата окончания.

```
+----+----+----+----+----+----+----+----+
| tunnel_gw                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|    flags     |cost|      end_date     |
+----+----+----+----+----+----+----+----+

tunnel_gw :: Hash of the `RouterIdentity` of the tunnel gateway,
             or the hash of another `MetaLeaseSet`.
             length -> 32 bytes

flags :: 3 bytes of flags
         Bit order: 23 22 ... 3 2 1 0
         Bits 3-0: Type of the entry.
         If 0, unknown.
         If 1, a `LeaseSet`.
         If 3, a `LeaseSet2`.
         If 5, a `MetaLeaseSet`.
         Bits 23-4: set to 0 for compatibility with future uses
         length -> 3 bytes

cost :: 1 byte, 0-255. Lower value is higher priority.
        length -> 1 byte

end_date :: 4 byte date
            length -> 4 bytes
            Seconds since the epoch, rolls over in 2106.

```
#### Примечания

* Общий размер: 40 байт

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLease.html

### MetaLeaseSet

#### Описание

Содержится в I2NP DatabaseStore сообщении типа 7. Определено в версии 0.9.38; запланировано к работе в версии 0.9.40; смотрите предложение 123 для получения дополнительной информации.

Содержит все текущие авторизованные [MetaLease](#metalease) для конкретного [Destination](#destination), а также [PublicKey](#publickey), с помощью которого можно шифровать garlic-сообщения. LeaseSet является одной из двух структур, хранящихся в сетевой базе данных (другая - [RouterInfo](#routerinfo)), и индексируется по SHA256 содержащегося [Destination](#destination).

#### Содержание

[LeaseSet2Header](#leaseset2header), за которым следуют опции, [Integer](#integer), указывающий количество структур [Lease2](#lease2) в наборе, затем сами структуры [Lease2](#lease2) и, наконец, [Signature](#signature) предыдущих байтов, подписанная [SigningPrivateKey](#signingprivatekey) [Destination](#destination) или временным ключом.

```
+----+----+----+----+----+----+----+----+
|         ls2_header                    |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          options                      |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| num| MetaLease 0                      |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| MetaLease($num-1)                     |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|numr|                                  |
+----+                                  +
|          revocation_0                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|          revocation_n                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

ls2header :: `LeaseSet2Header`
             length -> varies

options :: `Mapping`
           length -> varies, 2 bytes minimum

num :: `Integer`
        length -> 1 byte
        Number of `MetaLease`s to follow
        value: 1 <= num <= max TBD

leases :: `MetaLease`s
          length -> $numr*40 bytes

numr :: `Integer`
        length -> 1 byte
        Number of `Hash`es to follow
        value: 0 <= numr <= max TBD

revocations :: [`Hash`]
               length -> $numr*32 bytes

signature :: `Signature`
             length -> 40 bytes or as specified in destination's key
                       certificate, or by the sigtype of the transient public key,
                       if present in the header

```
#### Примечания

* Публичный ключ назначения использовался для старого шифрования I2CP-to-I2CP, которое было отключено в версии 0.6, в настоящее время не используется.

* Подпись вычисляется над данными выше, ПРЕДВАРЕННЫМИ одним байтом,
  содержащим тип DatabaseStore (7).

* Подпись может быть проверена с использованием открытого ключа подписи назначения или временного открытого ключа подписи, если автономная подпись включена в заголовок leaseset2.

* См. примечание к полю 'published' в [LeaseSet2Header](#leaseset2header)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/MetaLeaseSet.html

### EncryptedLeaseSet

#### Описание

Содержится в I2NP сообщении DatabaseStore типа 5. Определено начиная с версии 0.9.38; работает начиная с версии 0.9.39; смотрите предложение 123 для получения дополнительной информации.

Только слепой ключ и время истечения видны в открытом тексте. Сам leaseSet зашифрован.

#### Содержание

Двухбайтовый тип подписи, слепой [SigningPrivateKey](#signingprivatekey), время публикации, срок действия и флаги. Затем двухбайтовая длина, за которой следуют зашифрованные данные. Наконец, [Signature](#signature) предыдущих байтов, подписанная слепым [SigningPrivateKey](#signingprivatekey) или временным ключом.

```
+----+----+----+----+----+----+----+----+
| sigtype |                             |
+----+----+                             +
|        blinded_public_key             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|     published     | expires |  flags  |
+----+----+----+----+----+----+----+----+
| offline_signature (optional)          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  len    |                             |
+----+----+                             +
|         encrypted_data                |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

sigtype :: A two byte signature type of the public key to follow
           length -> 2 bytes

blinded_public_key :: `SigningPublicKey`
                      length -> As inferred from the sigtype

published :: 4 byte date
             length -> 4 bytes
             Seconds since the epoch, rolls over in 2106.

expires :: 2 byte time
           length -> 2 bytes
           Offset from published timestamp in seconds, 18.2 hours max

flags :: 2 bytes
  Bit order: 15 14 ... 3 2 1 0
  Bit 0: If 0, no offline keys; if 1, offline keys
  Bit 1: If 0, a standard published leaseset.
         If 1, an unpublished leaseset. Should not be flooded, published, or
         sent in response to a query. If this leaseset expires, do not query the
         netdb for a new one.
  Bits 15-2: set to 0 for compatibility with future uses

offline_signature :: `OfflineSignature`
                     length -> varies
                     Optional, only present if bit 0 is set in the flags.

len :: `Integer`
        length -> 2 bytes
        length of encrypted_data to follow
        value: 1 <= num <= max TBD

encrypted_data :: Data encrypted
                  length -> len bytes

signature :: `Signature`
             length -> As specified by the sigtype of the blinded pubic key,
                       or by the sigtype of the transient public key,
                       if present in the header

```
#### Примечания

* Публичный ключ назначения использовался для старого шифрования I2CP-to-I2CP, которое было отключено в версии 0.6, в настоящее время не используется.

* Подпись применяется к данным выше, ПРЕДВАРЯЕМЫМ одним байтом, содержащим тип DatabaseStore (5).

* Подпись может быть проверена с использованием публичного ключа подписи
  destination, или временного публичного ключа подписи, если автономная подпись
  включена в заголовок leaseset2.

* Блайндинг и шифрование описаны в [EncryptedLeaseSet](/docs/specs/encryptedleaseset/)

* Эта структура не использует [LeaseSet2Header](#leaseset2header).

* Максимальное фактическое время истечения составляет около 660 (11 минут), если только это не зашифрованный [MetaLeaseSet](#metaleaseset).

* См. предложение 123 для заметок об использовании автономных подписей
  с зашифрованными leaseSet.

* См. примечание к полю 'published' в [LeaseSet2Header](#leaseset2header)
  (та же проблема, хотя мы не используем формат LeaseSet2Header здесь)

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/EncryptedLeaseSet.html

### RouterAddress

#### Описание

Эта структура определяет способы связи с router через транспортный протокол.

#### Содержание

1 байт [Integer](#integer), определяющий относительную стоимость использования адреса, где 0 означает бесплатно, а 255 — дорого, за которым следует дата истечения срока [Date](#date), после которой адрес не должен использоваться, или, если null, адрес никогда не истекает. После этого идет [String](#string), определяющая транспортный протокол, который использует данный router адрес. Наконец, есть [Mapping](#mapping), содержащее все специфичные для транспорта опции, необходимые для установления соединения, такие как IP-адрес, номер порта, адрес электронной почты, URL и т.д.

```
+----+----+----+----+----+----+----+----+
|cost|           expiration
+----+----+----+----+----+----+----+----+
     |        transport_style           |
+----+----+----+----+-/-+----+----+----+
|                                       |
+                                       +
|               options                 |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

cost :: `Integer`
        length -> 1 byte

        case 0 -> free
        case 255 -> expensive

expiration :: `Date` (must be all zeros, see notes below)
              length -> 8 bytes

              case null -> never expires

transport_style :: `String`
                   length -> 1-256 bytes

options :: `Mapping`
```
#### Заметки

* Стоимость обычно составляет 5 или 6 для SSU и 10 или 11 для NTCP.

* Срок действия в настоящее время не используется, всегда null (все нули). Начиная с релиза 0.9.3, срок действия считается равным нулю и не сохраняется, поэтому любой ненулевой срок действия приведет к сбою при проверке подписи RouterInfo. Реализация срока действия (или другое использование этих байтов) будет изменением, несовместимым с предыдущими версиями. Router-ы ДОЛЖНЫ устанавливать это поле в нули. Начиная с релиза 0.9.12, ненулевое поле срока действия снова распознается, однако мы должны подождать несколько релизов, чтобы использовать это поле, пока подавляющее большинство сети не будет его распознавать.

* Следующие опции, хотя и не являются обязательными, являются стандартными и ожидается, что они будут присутствовать в большинстве адресов router: "host" (IPv4 или IPv6 адрес или имя хоста) и "port".

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterAddress.html

### RouterInfo

#### Описание

Определяет все данные, которые router хочет опубликовать для просмотра сетью. [RouterInfo](#routerinfo) является одной из двух структур, хранящихся в базе данных сети (другая — [LeaseSet](#leaseset)), и индексируется по SHA256 от содержащегося [RouterIdentity](#routeridentity).

#### Содержание

[RouterIdentity](#routeridentity), за которым следует [Date](#date) — время публикации записи

```
+----+----+----+----+----+----+----+----+
| router_ident                          |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| published                             |
+----+----+----+----+----+----+----+----+
|size| RouterAddress 0                  |
+----+                                  +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| RouterAddress 1                       |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
| RouterAddress ($size-1)               |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+----+----+----+----+-/-+----+----+----+
|psiz| options                          |
+----+----+----+----+-/-+----+----+----+
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

router_ident :: `RouterIdentity`
                length -> >= 387+ bytes

published :: `Date`
             length -> 8 bytes

size :: `Integer`
        length -> 1 byte
        The number of `RouterAddress`es to follow, 0-255

addresses :: [`RouterAddress`]
             length -> varies

peer_size :: `Integer`
             length -> 1 byte
             The number of peer `Hash`es to follow, 0-255, unused, always zero
             value -> 0

options :: `Mapping`

signature :: `Signature`
             length -> 40 bytes or as specified in router_ident's key
                       certificate
```
#### Примечания

* Значение peer_size [Integer](#integer) может сопровождаться списком соответствующего количества хешей router.
  В настоящее время это не используется. Предназначалось для формы ограниченных маршрутов,
  которая не реализована.
  Некоторые реализации могут требовать отсортированный список, чтобы подпись была инвариантной.
  Необходимо исследовать перед включением этой функции.

* Подпись может быть проверена с использованием публичного ключа подписи из router_ident.

* См. страницу базы данных сети [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo) для стандартных опций, которые
  должны присутствовать во всех router info.

* Очень старые router требовали сортировки адресов по SHA256 их данных,
  чтобы подпись была инвариантной.
  Это больше не требуется и не стоит реализации для обратной совместимости.

JavaDoc: http://docs.i2p-projekt.de/javadoc/net/i2p/data/router/RouterInfo.html

### Инструкции по доставке

Инструкции доставки tunnel сообщений определены в спецификации Tunnel Message [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions).

Инструкции доставки Garlic Message определены в спецификации сообщений I2NP [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions).

## Ссылки

- [ECIES](/docs/specs/ecies/)
- [ECIES-HYBRID](/docs/specs/ecies-hybrid/)
- [ECIES-ROUTERS](/docs/specs/ecies-routers/)
- [ELGAMAL](/docs/specs/cryptography/#elgamal-legacy)
- [ELGAMAL-AES](/docs/specs/elgamal-aes/)
- [GARLIC-DELIVERY](/docs/specs/i2np/#garlic-clove-delivery-instructions)
- [I2CP](/docs/specs/i2cp/)
- [I2NP](/docs/specs/i2np/)
- [NAMING](/docs/overview/naming/)
- [NETDB-ROUTERINFO](/docs/overview/network-database/#routerinfo)
- [Prop134](/proposals/134-gost/)
- [Prop169](/proposals/169-pq-crypto/)
- [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
- [SSU](/docs/legacy/ssu/)
- [TUNNEL-DELIVERY](/docs/specs/tunnel-message/#struct-tunnelmessagedeliveryinstructions)
