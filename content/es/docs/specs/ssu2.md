---
title: "Especificación SSU2"
description: "Protocolo de Transporte UDP Semi-Confiable Seguro Versión 2"
slug: "ssu2"
category: "Transportes"
lastUpdated: "2025-04"
accurateFor: "0.9.65"
---

## Estado

Sustancialmente completo. Consulte [Prop159](/proposals/159-ssu2) para obtener antecedentes y objetivos adicionales, incluyendo análisis de seguridad, modelos de amenazas, una revisión de la seguridad y problemas de SSU 1, y extractos de las especificaciones QUIC.

Plan de implementación:

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
La Sesión Básica incluye la fase de handshake y de datos. El protocolo extendido incluye relay y prueba de pares.

## Descripción general

Esta especificación define un protocolo de acuerdo de claves autenticado para mejorar la resistencia de [SSU](/docs/transport/ssu) a varias formas de identificación automatizada y ataques.

Al igual que con otros transportes de I2P, SSU2 está definido para el transporte punto a punto (router a router) de mensajes I2NP. No es una tubería de datos de propósito general. Como [SSU](/docs/transport/ssu), también proporciona dos servicios adicionales: Retransmisión para atravesar NAT, y Prueba de Pares para determinar la accesibilidad entrante. También proporciona un tercer servicio, que no está en SSU, para migración de conexión cuando un par cambia de IP o puerto.

## Resumen del Diseño

### Resumen

Nos basamos en varios protocolos existentes, tanto dentro de I2P como en estándares externos, para inspiración, orientación y reutilización de código:

- Modelos de amenaza: De NTCP2 [NTCP2](/docs/specs/ntcp2), con amenazas adicionales significativas relevantes para el transporte UDP según el análisis de QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Decisiones criptográficas: De [NTCP2](/docs/specs/ntcp2).
- Handshake: Noise XK de [NTCP2](/docs/specs/ntcp2) y [NOISE](https://noiseprotocol.org/noise.html). Son posibles simplificaciones significativas a NTCP2 debido a la encapsulación (límites de mensaje inherentes) proporcionada por UDP.
- Ofuscación de clave efímera del handshake: Adaptado de [NTCP2](/docs/specs/ntcp2) pero usando ChaCha20 de [ECIES](/docs/specs/ecies) en lugar de AES.
- Encabezados de paquete: Adaptado de WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) y QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Ofuscación de encabezados de paquete: Adaptado de [NTCP2](/docs/specs/ntcp2) pero usando ChaCha20 de [ECIES](/docs/specs/ecies) en lugar de AES.
- Protección de encabezados de paquete: Adaptado de QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) y [Nonces](https://eprint.iacr.org/2019/624.pdf)
- Encabezados utilizados como datos asociados AEAD como en [ECIES](/docs/specs/ecies).
- Numeración de paquetes: Adaptado de WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) y QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Mensajes: Adaptado de [SSU](/docs/transport/ssu)
- Fragmentación I2NP: Adaptado de [SSU](/docs/transport/ssu)
- Relay y Pruebas de Pares: Adaptado de [SSU](/docs/transport/ssu)
- Firmas de datos de Relay y Pruebas de Pares: De la especificación de estructuras comunes [Common](/docs/specs/common-structures)
- Formato de bloque: De [NTCP2](/docs/specs/ntcp2) y [ECIES](/docs/specs/ecies).
- Relleno y opciones: De [NTCP2](/docs/specs/ntcp2) y [ECIES](/docs/specs/ecies).
- Acks, nacks: Adaptado de QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000).
- Control de flujo: Por determinar

No hay primitivas criptográficas nuevas que no hayan sido utilizadas en I2P anteriormente.

### Garantías de Entrega

Al igual que con otros transportes I2P NTCP, NTCP2, y SSU 1, este transporte no es una facilidad de propósito general para la entrega de un flujo ordenado de bytes. Está diseñado para el transporte de mensajes I2NP. No se proporciona abstracción de "flujo".

Además, al igual que SSU, contiene facilidades adicionales para el atravesamiento de NAT facilitado por pares y pruebas de alcanzabilidad (conexiones entrantes).

En cuanto a SSU 1, NO proporciona entrega en orden de mensajes I2NP. Tampoco proporciona entrega garantizada de mensajes I2NP. Por eficiencia, o debido a la entrega fuera de orden de datagramas UDP o la pérdida de esos datagramas, los mensajes I2NP pueden ser entregados al extremo remoto fuera de orden, o pueden no ser entregados en absoluto. Un mensaje I2NP puede ser retransmitido múltiples veces si es necesario, pero la entrega puede eventualmente fallar sin causar que la conexión completa sea desconectada. Además, nuevos mensajes I2NP pueden continuar siendo enviados incluso mientras ocurre la retransmisión (recuperación de pérdidas) para otros mensajes I2NP.

Este protocolo NO previene completamente la entrega duplicada de mensajes I2NP. El router debe hacer cumplir la expiración de I2NP y usar un filtro Bloom u otro mecanismo basado en el ID del mensaje I2NP. Consulta la sección Duplicación de Mensajes I2NP a continuación.

### Marco de Protocolo Noise

Esta especificación proporciona los requisitos basados en el Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (Revisión 33, 2017-10-04). Noise tiene propiedades similares al protocolo Station-To-Station [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol), que es la base para el protocolo [SSU](/docs/transport/ssu). En la terminología de Noise, Alice es el iniciador y Bob es el respondedor.

SSU2 se basa en el protocolo Noise Noise_XK_25519_ChaChaPoly_SHA256. (El identificador real para la función de derivación de clave inicial es "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256" para indicar las extensiones de I2P - ver la sección KDF 1 más abajo)

NOTA: Este identificador es diferente al usado para NTCP2, porque los tres mensajes de handshake utilizan el encabezado como datos asociados.

Este protocolo Noise utiliza las siguientes primitivas:

- Patrón de Handshake: XK Alice transmite su clave a Bob (X) Alice ya conoce la clave estática de Bob (K)
- Función DH: X25519 X25519 DH con una longitud de clave de 32 bytes como se especifica en [RFC-7748](https://tools.ietf.org/html/rfc7748).
- Función de Cifrado: ChaChaPoly AEAD_CHACHA20_POLY1305 como se especifica en [RFC-7539](https://tools.ietf.org/html/rfc7539) sección 2.8. Nonce de 12 bytes, con los primeros 4 bytes establecidos en cero.
- Función Hash: SHA256 Hash estándar de 32 bytes, ya usado extensivamente en I2P.

### Adiciones al Framework

Esta especificación define las siguientes mejoras a Noise_XK_25519_ChaChaPoly_SHA256. Estas generalmente siguen las pautas de la sección 13 de [NOISE](https://noiseprotocol.org/noise.html).

1) Los mensajes de handshake (Session Request, Created, Confirmed) incluyen un encabezado de 16 o 32 bytes. 2) Los encabezados de los mensajes de handshake (Session Request, Created, Confirmed) se utilizan como entrada para mixHash() antes del cifrado/descifrado para vincular los encabezados al mensaje. 3) Los encabezados están cifrados y protegidos. 4) Las claves efímeras en texto plano están ofuscadas con cifrado ChaCha20 usando una clave e IV conocidos. Esto es más rápido que elligator2. 5) El formato de carga útil está definido para los mensajes 1, 2 y la fase de datos. Por supuesto, esto no está definido en Noise.

La fase de datos utiliza cifrado similar al de la fase de datos de Noise, pero no compatible con ella.

## Definiciones

Definimos las siguientes funciones correspondientes a los bloques de construcción criptográficos utilizados.

ZEROLEN

:   array de bytes de longitud cero

H(p, d)

:   Función hash SHA-256 que toma una cadena de personalización p y datos d, y produce una salida de 32 bytes de longitud. Como se define en [NOISE](https://noiseprotocol.org/noise.html). || a continuación significa concatenar.

    Use SHA-256 as follows:

        H(p, d) := SHA-256(p || d)

MixHash(d)

:   Función hash SHA-256 que toma un hash previo h y nuevos datos d, y produce una salida de 32 bytes de longitud. || a continuación significa agregar.

    Use SHA-256 as follows:

        MixHash(d) := h = SHA-256(h || d)

STREAM

:   El AEAD ChaCha20/Poly1305 como se especifica en [RFC-7539](https://tools.ietf.org/html/rfc7539). S_KEY_LEN = 32 y S_IV_LEN = 12.

    ENCRYPT(k, n, plaintext, ad)

    :   Encrypts plaintext using the cipher key k, and nonce n which MUST be unique for the key k. Associated data ad is optional. Returns a ciphertext that is the size of the plaintext + 16 bytes for the HMAC.

        The entire ciphertext must be indistinguishable from random if the key is secret.

    DECRYPT(k, n, ciphertext, ad)

    :   Decrypts ciphertext using the cipher key k, and nonce n. Associated data ad is optional. Returns the plaintext.

DH

:   Sistema de acuerdo de claves públicas X25519. Claves privadas de 32 bytes, claves públicas de 32 bytes, produce salidas de 32 bytes. Tiene las siguientes funciones:

    GENERATE_PRIVATE()

    :   Generates a new private key.

    DERIVE_PUBLIC(privkey)

    :   Returns the public key corresponding to the given private key.

    DH(privkey, pubkey)

    :   Generates a shared secret from the given private and public keys.

HKDF(salt, ikm, info, n)

:   Una función criptográfica de derivación de claves que toma material de clave de entrada ikm (que debe tener buena entropía pero no se requiere que sea una cadena uniformemente aleatoria), una sal de longitud de 32 bytes, y un valor 'info' específico del contexto, y produce una salida de n bytes adecuada para usar como material de clave.

    Use HKDF as specified in [RFC-5869](https://tools.ietf.org/html/rfc5869), using the HMAC hash function SHA-256 as specified in [RFC-2104](https://tools.ietf.org/html/rfc2104). This means that SALT_LEN is 32 bytes max.

MixKey(d)

:   Usa HKDF() con una chainKey anterior y nuevos datos d, y establece la nueva chainKey y k. Como se define en [NOISE](https://noiseprotocol.org/noise.html).

    Use HKDF as follows:

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]

## Mensajes

Cada datagrama UDP contiene exactamente un mensaje. La longitud del datagrama (después de los headers IP y UDP) es la longitud del mensaje. El relleno, si existe, se encuentra contenido en un bloque de relleno dentro del mensaje. En este documento, usamos los términos "datagrama" y "paquete" principalmente de forma intercambiable. Cada datagrama (o paquete) contiene un solo mensaje (a diferencia de QUIC, donde un datagrama puede contener múltiples paquetes QUIC). El "header del paquete" es la parte posterior al header IP/UDP.

Excepción: El mensaje Session Confirmed es único en el sentido de que puede fragmentarse a través de múltiples paquetes. Consulta la sección Fragmentación de Session Confirmed a continuación para más información.

Todos los mensajes SSU2 tienen al menos 40 bytes de longitud. Cualquier mensaje de longitud 1-39 bytes es inválido. Todos los mensajes SSU2 tienen una longitud menor o igual a 1472 (IPv4) o 1452 (IPv6) bytes. El formato del mensaje se basa en mensajes Noise, con modificaciones para el encuadre e indistinguibilidad. Las implementaciones que usan bibliotecas Noise estándar deben preprocesar los mensajes recibidos al formato de mensaje Noise estándar. Todos los campos cifrados son textos cifrados AEAD.

Los siguientes mensajes están definidos:

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
### Establecimiento de Sesión

La secuencia de establecimiento estándar, cuando Alice tiene un token válido previamente recibido de Bob, es la siguiente:

```
Alice                           Bob

SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Cuando Alice no tiene un token válido, la secuencia de establecimiento es la siguiente:

```
Alice                           Bob

TokenRequest --------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Cuando Alice piensa que tiene un token válido, pero Bob lo rechaza (tal vez porque Bob se reinició), la secuencia de establecimiento es la siguiente:

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Bob puede rechazar una Sesión o Solicitud de Token respondiendo con un mensaje Retry que contenga un bloque Termination con un código de razón. Basándose en el código de razón, Alice no debería intentar otra solicitud durante cierto período de tiempo:

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry containing a Termination block

or

TokenRequest --------------------->
<---------------------------  Retry containing a Termination block
```
Usando la terminología Noise, la secuencia de establecimiento y datos es la siguiente: (Propiedades de Seguridad del Payload)

```
XK(s, rs):           Authentication   Confidentiality
  <- s
  ...
  -> e, es                  0                2
  <- e, ee                  2                1
  -> s, se                  2                5
  <-                        2                5
```
Una vez que se ha establecido una sesión, Alice y Bob pueden intercambiar mensajes de datos.

### Cabecera del Paquete

Todos los paquetes comienzan con un encabezado ofuscado (encriptado). Hay dos tipos de encabezado, largo y corto. Nota que los primeros 13 bytes (ID de Conexión de Destino, número de paquete y tipo) son los mismos para todos los encabezados.

#### Encabezado Largo

El encabezado largo tiene 32 bytes. Se utiliza antes de que se cree una sesión, para Token Request, SessionRequest, SessionCreated y Retry. También se utiliza para mensajes Peer Test y Hole Punch fuera de sesión.

Antes del cifrado de cabecera:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 0, 1, 7, 9, 10, or 11

ver :: The protocol version, equal to 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: 8 bytes, unsigned big endian integer

Token :: 8 bytes, unsigned big endian integer
```
#### Encabezado Corto

El encabezado corto tiene 16 bytes. Se utiliza para los mensajes Session Created y Data. Los mensajes no autenticados como Session Request, Retry y Peer Test siempre utilizarán el encabezado largo.

Se requieren 16 bytes, porque el receptor debe descifrar los primeros 16 bytes para obtener el tipo de mensaje, y luego debe descifrar 16 bytes adicionales si en realidad es un encabezado largo, como lo indica el tipo de mensaje.

Para Session Confirmed, antes del cifrado de cabecera:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, all zeros

type :: The message type = 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility
```
Consulta la sección Fragmentación de Sesión Confirmada más abajo para obtener más información sobre el campo frag.

Para mensajes de datos, antes del cifrado del encabezado:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|flag|moreflags|
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 6

flag :: 1 byte flags:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-1: unused, set to 0 for future compatibility
       bits 0: when set to 1, immediate ack requested

moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### Numeración de ID de Conexión

Los IDs de conexión deben generarse de forma aleatoria. Los IDs de origen y destino NO deben ser idénticos, para que un atacante en la ruta no pueda capturar y enviar un paquete de vuelta al originador que parezca válido. NO uses un contador para generar IDs de conexión, para que un atacante en la ruta no pueda generar un paquete que parezca válido.

A diferencia de QUIC, no cambiamos los IDs de conexión durante o después del handshake, incluso después de un mensaje de Retry. Los IDs permanecen constantes desde el primer mensaje (Token Request o Session Request) hasta el último mensaje (Data con Termination). Además, los IDs de conexión no cambian durante o después del path challenge o la migración de conexión.

También diferente a QUIC es que los IDs de conexión en las cabeceras siempre están cifrados en la cabecera. Ver abajo.

#### Numeración de Paquetes

Si no se envía ningún bloque First Packet Number en el handshake, los paquetes se numeran dentro de una sola sesión, para cada dirección, comenzando desde 0, hasta un máximo de (2**32 -1). Una sesión debe terminarse, y debe crearse una nueva sesión, mucho antes de que se envíe el número máximo de paquetes.

Si se envía un bloque de Número de Primer Paquete en el handshake, los paquetes se numeran dentro de una sola sesión, para esa dirección, comenzando desde ese número de paquete. El número de paquete puede dar la vuelta durante la sesión. Cuando se han enviado un máximo de 2**32 paquetes, haciendo que el número de paquete vuelva al número del primer paquete, esa sesión ya no es válida. Una sesión debe terminarse, y crearse una nueva sesión, mucho antes de que se envíe el número máximo de paquetes.

TODO rotación de claves, ¿reducir número máximo de paquetes?

Los paquetes de handshake que se determinan como perdidos se retransmiten completos, con el encabezado idéntico incluyendo el número de paquete. Los mensajes de handshake Session Request, Session Created y Session Confirmed DEBEN retransmitirse con el mismo número de paquete y contenidos cifrados idénticos, de modo que se use el mismo hash encadenado para cifrar la respuesta. El mensaje Retry nunca se transmite.

Los paquetes de la fase de datos que se determina que están perdidos nunca se retransmiten completos (excepto la terminación, ver más abajo). Lo mismo se aplica a los bloques que están contenidos dentro de los paquetes perdidos. En su lugar, la información que podría ser transportada en bloques se envía nuevamente en nuevos paquetes según sea necesario. Los Data Packets nunca se retransmiten con el mismo número de paquete. Cualquier retransmisión del contenido de paquetes (independientemente de si el contenido permanece igual o no) debe usar el siguiente número de paquete no utilizado.

Retransmitir un paquete completo sin cambios tal como está, con el mismo número de paquete, no está permitido por varias razones. Para más contexto, consulte QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) sección 12.3.

- Es ineficiente almacenar paquetes para retransmisión
- Un nuevo paquete de datos se ve diferente para un observador en la ruta, no puede saber que es retransmitido
- Un nuevo paquete obtiene un bloque ack actualizado enviado con él, no el bloque ack antiguo
- Solo retransmites lo que es necesario. algunos fragmentos podrían haber sido ya retransmitidos una vez y confirmados
- Puedes ajustar tanto como necesites en cada paquete retransmitido si hay más pendiente
- Los endpoints que rastrean todos los paquetes individuales con el propósito de detectar duplicados están en riesgo de acumular estado excesivo. Los datos requeridos para detectar duplicados pueden ser limitados manteniendo un número mínimo de paquete por debajo del cual todos los paquetes son inmediatamente descartados.
- Este esquema es mucho más flexible

Los nuevos paquetes se utilizan para transportar información que se ha determinado que se perdió. En general, la información se envía nuevamente cuando se determina que un paquete que contiene esa información se ha perdido, y el envío cesa cuando un paquete que contiene esa información es reconocido.

Excepción: Un paquete de fase de datos que contenga un bloque de Terminación puede, pero no está obligado a ser, retransmitido completo, tal como está. Ver la sección de Terminación de Sesión a continuación.

Los siguientes paquetes contienen un número de paquete aleatorio que se ignora:

- Solicitud de Sesión
- Sesión Creada
- Solicitud de Token
- Reintentar
- Prueba de Par
- Perforación de Agujero

Para Alice, la numeración de paquetes salientes comienza en 0 con Session Confirmed. Para Bob, la numeración de paquetes salientes comienza en 0 con el primer paquete Data, que debería ser un ACK del Session Confirmed. Los números de paquete en un ejemplo de handshake estándar serán:

```
Alice                           Bob

SessionRequest (r)    ------------>
<-------------   SessionCreated (r)
SessionConfirmed (0)  ------------>
<-------------             Data (0) (Ack-only)
Data (1)              ------------> (May be sent before Ack is received)
<-------------             Data (1)
Data (2)              ------------>
Data (3)              ------------>
Data (4)              ------------>
<-------------             Data (2)

r = random packet number (ignored)
Token Request, Retry, and Peer Test
also have random packet numbers.
```
Cualquier retransmisión de mensajes de handshake (SessionRequest, SessionCreated, o SessionConfirmed) debe ser reenviada sin cambios, con el mismo número de paquete. No uses claves efímeras diferentes ni cambies la carga útil al retransmitir estos mensajes.

#### Vinculación de Encabezado

El encabezado (antes de la ofuscación y protección) siempre se incluye en los datos asociados para la función AEAD, para vincular criptográficamente el encabezado con los datos.

#### Cifrado de Encabezado

El cifrado de encabezados tiene varios objetivos. Consulta la sección "Discusión Adicional sobre DPI" anterior para contexto y suposiciones.

- Prevenir que la DPI en línea identifique el protocolo
- Prevenir patrones en una serie de mensajes en la misma conexión, excepto para retransmisiones de handshake
- Prevenir patrones en mensajes del mismo tipo en diferentes conexiones
- Prevenir el descifrado de cabeceras de handshake sin conocimiento de la clave de introducción encontrada en el netDb
- Prevenir la identificación de claves efímeras X25519 sin conocimiento de la clave de introducción encontrada en el netDb
- Prevenir el descifrado del número y tipo de paquete de la fase de datos por cualquier atacante en línea u offline
- Prevenir la inyección de paquetes de handshake válidos por un observador en ruta o fuera de ruta sin conocimiento de la clave de introducción encontrada en el netDb
- Prevenir la inyección de paquetes de datos válidos por un observador en ruta o fuera de ruta
- Permitir clasificación rápida y eficiente de paquetes entrantes
- Proporcionar resistencia al "probing" de modo que no haya respuesta a una Session Request incorrecta, o si hay una respuesta Retry, la respuesta no sea identificable como I2P sin conocimiento de la clave de introducción encontrada en el netDb
- El Destination Connection ID no es información crítica, y está bien si puede ser descifrado por un observador con conocimiento de la clave de introducción encontrada en el netDb
- El número de paquete de un paquete de fase de datos es un nonce AEAD y es información crítica. No debe ser descifrable por un observador incluso con conocimiento de la clave de introducción encontrada en el netDb. Ver [Nonces](https://eprint.iacr.org/2019/624.pdf).

Los encabezados se cifran con claves conocidas publicadas en la base de datos de red o calculadas posteriormente. En la fase de handshake, esto es solo para resistencia a DPI, ya que la clave es pública y tanto la clave como los nonces se reutilizan, por lo que efectivamente es solo ofuscación. Ten en cuenta que el cifrado de encabezados también se usa para ofuscar las claves efímeras X (en Session Request) e Y (en Session Created).

Consulte la sección de Manejo de Paquetes Entrantes a continuación para obtener orientación adicional.

Los bytes 0-15 de todos los encabezados están cifrados utilizando un esquema de protección de encabezados mediante XOR con datos calculados a partir de claves conocidas, usando ChaCha20, similar a QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) y [Nonces](https://eprint.iacr.org/2019/624.pdf). Esto asegura que el encabezado corto cifrado y la primera parte del encabezado largo aparenten ser aleatorios.

Para Session Request y Session Created, los bytes 16-31 del encabezado largo y la clave efímera Noise de 32 bytes se cifran usando ChaCha20. Los datos sin cifrar son aleatorios, por lo que los datos cifrados parecerán ser aleatorios.

Para Retry, los bytes 16-31 del encabezado largo se cifran usando ChaCha20. Los datos sin cifrar son aleatorios, por lo que los datos cifrados parecerán ser aleatorios.

A diferencia del esquema de protección de cabeceras QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001), TODAS las partes de todas las cabeceras, incluyendo los IDs de conexión de destino y origen, están cifradas. QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) y [Nonces](https://eprint.iacr.org/2019/624.pdf) se enfocan principalmente en cifrar la parte "crítica" de la cabecera, es decir, el número de paquete (nonce ChaCha20). Aunque cifrar el ID de sesión hace la clasificación de paquetes entrantes un poco más compleja, dificulta algunos ataques. QUIC define diferentes IDs de conexión para diferentes fases, y para el desafío de ruta y migración de conexión. Aquí usamos los mismos IDs de conexión durante todo el proceso, ya que están cifrados.

Hay siete fases de claves de protección de encabezado:

- Solicitud de Sesión y Solicitud de Token
- Sesión Creada
- Reintentar
- Sesión Confirmada
- Fase de Datos
- Prueba de Par
- Perforación de Agujero

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
El cifrado de cabecera está diseñado para permitir una clasificación rápida de los paquetes entrantes, sin heurísticas complejas o mecanismos de respaldo. Esto se logra utilizando la misma clave k_header_1 para casi todos los mensajes entrantes. Incluso cuando la IP de origen o el puerto de una conexión cambia debido a un cambio real de IP o comportamiento NAT, el paquete puede ser mapeado rápidamente a una sesión con una sola búsqueda del ID de conexión.

Ten en cuenta que Session Created y Retry son los ÚNICOS mensajes que requieren procesamiento de respaldo para k_header_1 para descifrar el Connection ID, porque usan la clave de introducción del remitente (Bob). TODOS los demás mensajes usan la clave de introducción del receptor para k_header_1. El procesamiento de respaldo solo necesita buscar conexiones salientes pendientes por IP/puerto de origen.

Si el procesamiento de respaldo por IP/puerto de origen no logra encontrar una conexión saliente pendiente, podría haber varias causas:

- No es un mensaje SSU2
- Un mensaje SSU2 corrupto
- La respuesta está falsificada o modificada por un atacante
- Bob tiene un NAT simétrico
- Bob cambió la IP o el puerto durante el procesamiento del mensaje
- Bob envió la respuesta por una interfaz diferente

Aunque es posible un procesamiento de respaldo adicional para intentar encontrar la conexión saliente pendiente y descifrar el ID de conexión usando el k_header_1 para esa conexión, probablemente no sea necesario. Si Bob tiene problemas con su NAT o enrutamiento de paquetes, probablemente sea mejor dejar que la conexión falle. Este diseño se basa en que los endpoints mantengan una dirección estable durante la duración del handshake.

Consulte la sección de Manejo de Paquetes Entrantes a continuación para pautas adicionales.

Consulta las secciones individuales de KDF a continuación para la derivación de las claves de cifrado de encabezado para esa fase.

#### KDF de Cifrado de Encabezado

```
// incoming encrypted packet
packet = incoming encrypted packet
len = packet.length

// take the next-to-last 12 bytes of the packet
iv = packet[len-24:len-13]
k_header_1 = header encryption key 1
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_1, iv, data)

// encrypt the first part of the header by XORing with the mask
packet[0:7] ^= mask[0:7]

// take the last 12 bytes of the packet
iv = packet[len-12:len-1]
k_header_2 = header encryption key 2
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_2, iv, data)

// encrypt the second part of the header by XORing with the mask
packet[8:15] ^= mask[0:7]


// For Session Request and Session Created only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header and the ephemeral key
packet[16:63] = ChaCha20.encrypt(k_header_2, iv, packet[16:63])


// For Retry, Token Request, Peer Test, and Hole Punch only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header
packet[16:31] = ChaCha20.encrypt(k_header_2, iv, packet[16:31])
```
Esta KDF utiliza los últimos 24 bytes del paquete como el IV para las dos operaciones ChaCha20. Como todos los paquetes terminan con un MAC de 16 bytes, esto requiere que todas las cargas útiles de paquetes tengan un mínimo de 8 bytes. Este requisito está documentado adicionalmente en las secciones de mensajes a continuación.

#### Validación de Encabezado

Después de descifrar los primeros 8 bytes del encabezado, el receptor conocerá el ID de Conexión de Destino. A partir de ahí, el receptor sabe qué clave de cifrado de encabezado usar para el resto del encabezado, basándose en la fase de clave de la sesión.

Desencriptar los siguientes 8 bytes del encabezado revelará entonces el tipo de mensaje y permitirá determinar si es un encabezado corto o largo. Si es un encabezado largo, el receptor debe validar los campos de versión y netid. Si la versión es != 2, o el netid es != el valor esperado (generalmente 2, excepto en redes de prueba), el receptor debe descartar el mensaje.

### Integridad de Paquetes

Todos los mensajes contienen tres o cuatro partes:

- El encabezado del mensaje
- Solo para Session Request y Session Created, una clave efímera
- Una carga útil cifrada con ChaCha20
- Un MAC Poly1305

En todos los casos, el encabezado (y si está presente, la clave efímera) está vinculado al MAC de autenticación para asegurar que todo el mensaje esté intacto.

- Para los mensajes de handshake Session Request, Session Created y Session Confirmed, el encabezado del mensaje se procesa con mixHash() antes de la fase de procesamiento Noise
- La clave efímera, si está presente, está cubierta por un misHash() estándar de Noise
- Para mensajes fuera del handshake Noise, el encabezado se utiliza como Datos Asociados para el cifrado ChaCha20/Poly1305.

Los manejadores de paquetes entrantes siempre deben descifrar la carga útil ChaCha20 y validar el MAC antes de procesar el mensaje, con una excepción: Para mitigar ataques DoS de paquetes con direcciones falsificadas que contienen mensajes de Session Request aparentes con un token inválido, un manejador NO necesita intentar descifrar y validar el mensaje completo (requiriendo una operación DH costosa además del descifrado ChaCha20/Poly1305). El manejador puede responder con un mensaje Retry usando los valores encontrados en el encabezado del mensaje Session Request.

### Cifrado Autenticado

Hay tres instancias separadas de cifrado autenticado (CipherStates). Una durante la fase de handshake, y dos (transmisión y recepción) para la fase de datos. Cada una tiene su propia clave de una KDF.

Los datos cifrados/autenticados se representarán como

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

Formato de datos encriptado y autenticado.

Entradas a las funciones de cifrado/descifrado:

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
      The packet header, 16 bytes.

data :: Plaintext data, 0 or more bytes
```
Salida de la función de cifrado, entrada a la función de descifrado:

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|       ChaCha20 encrypted data         |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|  Poly1305 Message Authentication Code |
+              (MAC)                    +
|             16 bytes                  |
+----+----+----+----+----+----+----+----+

encrypted data :: Same size as plaintext data, 0 - 65519 bytes

MAC :: Poly1305 message authentication code, 16 bytes
```
Para ChaCha20, lo que se describe aquí corresponde a [RFC-7539](https://tools.ietf.org/html/rfc7539), que también se utiliza de manera similar en TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).

#### Notas

- Dado que ChaCha20 es un cifrado de flujo, los textos planos no necesitan relleno. Los bytes adicionales del flujo de claves se descartan.
- La clave para el cifrado (256 bits) se acuerda mediante la KDF SHA256. Los detalles de la KDF para cada mensaje están en secciones separadas a continuación.

#### Manejo de Errores AEAD

- En todos los mensajes, el tamaño del mensaje AEAD se conoce de antemano. En caso de falla de autenticación AEAD, el receptor debe detener el procesamiento adicional del mensaje y descartarlo.
- Bob debe mantener una lista negra de IPs con fallas repetidas.

### KDF para Solicitud de Sesión

La Función de Derivación de Claves (KDF) genera una clave de cifrado k de la fase de handshake a partir del resultado DH, utilizando HMAC-SHA256(key, data) como se define en [RFC-2104](https://tools.ietf.org/html/rfc2104). Estas son las funciones InitializeSymmetric(), MixHash(), y MixKey(), exactamente como se definen en la especificación Noise.

#### KDF para ChainKey Inicial

```
// Define protocol_name.
Set protocol_name = "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256"
 (52 bytes, US-ASCII encoded, no NULL termination).

// Define Hash h = 32 bytes
h = SHA256(protocol_name);

Define ck = 32 byte chaining key. Copy the h data to ck.
Set ck = h

// MixHash(null prologue)
h = SHA256(h);

// up until here, can all be precalculated by Alice for all outgoing connections

// Bob's X25519 static keys
// bpk is published in routerinfo
bsk = GENERATE_PRIVATE()
bpk = DERIVE_PUBLIC(bsk)

// Bob static key
// MixHash(bpk)
// || below means append
h = SHA256(h || bpk);

// Bob introduction key
// bik is published in routerinfo
bik = RANDOM(32)

// up until here, can all be precalculated by Bob for all incoming connections
```
#### KDF para Solicitud de Sesión

```
// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Alice's X25519 ephemeral keys
aesk = GENERATE_PRIVATE()
aepk = DERIVE_PUBLIC(aesk)

// Alice ephemeral key X
// MixHash(aepk)
h = SHA256(h || aepk);

// h is used as the associated data for the AEAD in Session Request
// Retain the Hash h for the Session Created KDF


End of "e" message pattern.

This is the "es" message pattern:

// DH(e, rs) == DH(s, re)
sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
// ChaChaPoly parameters to encrypt/decrypt
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chainKey for Session Created KDF


End of "es" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2 = bik

// Header encryption keys for next message (Session Created)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessCreateHeader", 32)

// Header encryption keys for next message (Retry)
k_header_1 = bik
k_header_2 = bik
```
### SessionRequest (Tipo 0)

Alice envía a Bob, ya sea como el primer mensaje en el handshake, o en respuesta a un mensaje Retry. Bob responde con un mensaje Session Created. Tamaño: 80 + tamaño del payload. Tamaño mínimo: 88

Si Alice no tiene un token válido, Alice debería enviar un mensaje Token Request en lugar de un Session Request, para evitar la sobrecarga de cifrado asimétrico al generar un Session Request.

Encabezado largo. Contenido Noise: clave efímera X de Alice Carga útil Noise: DateTime y otros bloques Tamaño máximo de carga útil: MTU - 108 (IPv4) o MTU - 128 (IPv6). Para MTU 1280: La carga útil máxima es 1172 (IPv4) o 1152 (IPv6). Para MTU 1500: La carga útil máxima es 1392 (IPv4) o 1372 (IPv6).

Propiedades de Seguridad de la Carga Útil:

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
El valor X se cifra para garantizar la indistinguibilidad y unicidad de la carga útil, que son contramedidas DPI necesarias. Utilizamos cifrado ChaCha20 para lograr esto, en lugar de alternativas más complejas y lentas como elligator2. El cifrado asimétrico a la clave pública del router de Bob sería demasiado lento. El cifrado ChaCha20 utiliza la clave de introducción de Bob tal como se publica en el netDb.

El cifrado ChaCha20 es solo para resistencia a DPI. Cualquier parte que conozca la clave de introducción de Bob, que se publica en la base de datos de la red, puede descifrar el encabezado y el valor X en este mensaje.

Contenidos sin procesar:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|    See Header Encryption KDF          |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key n=0     +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+       X, ChaCha20 encrypted           +
|       with Bob intro key n=0          |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|  k defined in KDF for Session Request |
+  n = 0                                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

X :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted X)
```
Datos sin cifrar (etiqueta de autenticación Poly1305 no mostrada):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                   X                   |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|     see below for allowed blocks      |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 0

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Alice, ignored

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: 0 if not previously received from Bob

X :: 32 bytes, X25519 ephemeral key, little endian
```
#### Carga útil

- Bloque DateTime
- Bloque Options (opcional)
- Bloque Relay Tag Request (opcional)
- Bloque Padding (opcional)

El tamaño mínimo de la carga útil es de 8 bytes. Dado que el bloque DateTime es de solo 7 bytes, debe estar presente al menos otro bloque.

#### Notas

- El valor X único en el bloque inicial de ChaCha20 asegura que el texto cifrado sea diferente para cada sesión.
- Para proporcionar resistencia al sondeo, Bob no debería enviar un mensaje Retry en respuesta a un mensaje Session Request a menos que el tipo de mensaje, versión del protocolo y campos de ID de red en el mensaje Session Request sean válidos.
- Bob debe rechazar conexiones donde el valor de marca de tiempo está demasiado alejado del tiempo actual. Llama al tiempo delta máximo "D". Bob debe mantener una caché local de valores de handshake previamente usados y rechazar duplicados, para prevenir ataques de reproducción. Los valores en la caché deben tener un tiempo de vida de al menos 2*D. Los valores de la caché dependen de la implementación, sin embargo se puede usar el valor X de 32 bytes (o su equivalente cifrado). Rechazar enviando un mensaje Retry que contenga un token cero y un bloque de terminación.
- Las claves efímeras Diffie-Hellman nunca pueden ser reutilizadas, para prevenir ataques criptográficos, y la reutilización será rechazada como un ataque de reproducción.
- Las opciones "KE" y "auth" deben ser compatibles, es decir, el secreto compartido K debe ser del tamaño apropiado. Si se agregan más opciones "auth", esto podría cambiar implícitamente el significado de la bandera "KE" para usar una KDF diferente o un tamaño de truncamiento diferente.
- Bob debe validar que la clave efímera de Alice es un punto válido en la curva aquí.
- El relleno debería limitarse a una cantidad razonable. Bob puede rechazar conexiones con relleno excesivo. Bob especificará sus opciones de relleno en Session Created. Pautas mín/máx por determinar. ¿Tamaño aleatorio de 0 a 31 bytes mínimo? (Distribución por determinar, ver Apéndice A.)
- En la mayoría de errores, incluyendo AEAD, DH, aparente reproducción, o falla de validación de clave, Bob debería detener el procesamiento adicional de mensajes y descartar el mensaje sin responder.
- Bob PUEDE enviar un mensaje Retry que contenga un token cero y un bloque de Terminación con un código de razón de sesgo de reloj si la marca de tiempo en el bloque DateTime está demasiado sesgada.
- Mitigación DoS: DH es una operación relativamente costosa. Como con el protocolo NTCP anterior, los routers deberían tomar todas las medidas necesarias para prevenir el agotamiento de CPU o conexiones. Establecer límites en conexiones activas máximas y configuraciones de conexión máximas en progreso. Hacer cumplir timeouts de lectura (tanto por lectura como total para "slowloris"). Limitar conexiones repetidas o simultáneas desde la misma fuente. Mantener listas negras para fuentes que fallan repetidamente. No responder a falla AEAD. Alternativamente, responder con un mensaje Retry antes de la operación DH y validación AEAD.
- Campo "ver": El protocolo Noise general, extensiones y protocolo SSU2 incluyendo especificaciones de payload, indicando SSU2. Este campo puede usarse para indicar soporte para cambios futuros.
- El campo ID de red se usa para identificar rápidamente conexiones entre redes. Si este campo no coincide con el ID de red de Bob, Bob debería desconectar y bloquear conexiones futuras.
- Bob debe descartar el mensaje si el ID de Conexión de Origen es igual al ID de Conexión de Destino.

### KDF para Session Created y Session Confirmed parte 1

```
// take h saved from Session Request KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Request)

// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Bob's X25519 ephemeral keys
besk = GENERATE_PRIVATE()
bepk = DERIVE_PUBLIC(besk)

// h is from KDF for Session Request
// Bob ephemeral key Y
// MixHash(bepk)
h = SHA256(h || bepk);

// h is used as the associated data for the AEAD in Session Created
// Retain the Hash h for the Session Confirmed KDF

End of "e" message pattern.

This is the "ee" message pattern:

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chaining key ck for Session Confirmed KDF

End of "ee" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Request KDF above

// Header protection keys for next message (Session Confirmed)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessionConfirmed", 32)
```
### SessionCreated (Tipo 1)

Bob envía a Alice, en respuesta a un mensaje Session Request. Alice responde con un mensaje Session Confirmed. Tamaño: 80 + tamaño de la carga útil. Tamaño Mínimo: 88

Contenido Noise: clave efímera Y de Bob Carga útil Noise: DateTime, Address y otros bloques Tamaño máximo de carga útil: MTU - 108 (IPv4) o MTU - 128 (IPv6). Para MTU 1280: La carga útil máxima es 1172 (IPv4) o 1152 (IPv6). Para MTU 1500: La carga útil máxima es 1392 (IPv4) o 1372 (IPv6).

Propiedades de Seguridad del Payload:

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
El valor Y se cifra para garantizar la indistinguibilidad y unicidad de la carga útil, que son contramedidas DPI necesarias. Utilizamos el cifrado ChaCha20 para lograr esto, en lugar de alternativas más complejas y lentas como elligator2. El cifrado asimétrico a la clave pública del router de Alice sería demasiado lento. El cifrado ChaCha20 utiliza la clave de introducción de Bob, tal como se publica en la base de datos de red.

El cifrado ChaCha20 es solo para resistencia a DPI. Cualquier parte que conozca la clave de introducción de Bob, que está publicada en la base de datos de la red, y capture los primeros 32 bytes de Session Request, puede descifrar el valor Y en este mensaje.

Contenidos sin procesar:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with derived key n=0       +
|  See Header Encryption KDF            |
+----+----+----+----+----+----+----+----+
|                                       |
+       Y, ChaCha20 encrypted           +
|       with derived key n=0            |
+              (32 bytes)               +
|       See Header Encryption KDF       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in KDF for Session Created +
|  n = 0; see KDF for associated data   |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

Y :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted Y)
```
Datos sin cifrar (etiqueta de autenticación Poly1305 no mostrada):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                  Y                    |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|      see below for allowed blocks     |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: The Source Connection ID
                             received from Alice in Session Request

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 0

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Bob, ignored

Source Connection ID :: The Destination Connection ID
                        received from Alice in Session Request

Token :: 0 (unused)

Y :: 32 bytes, X25519 ephemeral key, little endian
```
#### Carga útil

- Bloque DateTime
- Bloque Address
- Bloque Relay Tag (opcional)
- Bloque New Token (no recomendado, ver nota)
- Bloque First Packet Number (opcional)
- Bloque Options (opcional)
- Bloque Termination (no recomendado, enviar en un mensaje de reintento en su lugar)
- Bloque Padding (opcional)

El tamaño mínimo del payload es de 8 bytes. Dado que los bloques DateTime y Address suman más que eso, el requisito se cumple con solo esos dos bloques.

#### Notas

- Alice debe validar que la clave efímera de Bob es un punto válido en la curva aquí.
- El relleno debe limitarse a una cantidad razonable. Alice puede rechazar conexiones con relleno excesivo. Alice especificará sus opciones de relleno en Session Confirmed. Pautas mín/máx por determinar. ¿Tamaño aleatorio de 0 a 31 bytes como mínimo? (Distribución por determinar, ver Apéndice A.)
- En cualquier error, incluyendo AEAD, DH, timestamp, aparente replay, o falla de validación de clave, Alice debe detener el procesamiento adicional de mensajes y cerrar la conexión sin responder.
- Alice debe rechazar conexiones donde el valor del timestamp esté demasiado alejado del tiempo actual. Llamar al delta máximo de tiempo "D". Alice debe mantener una caché local de valores de handshake previamente utilizados y rechazar duplicados, para prevenir ataques de replay. Los valores en la caché deben tener una vida útil de al menos 2*D. Los valores de la caché dependen de la implementación, sin embargo se puede usar el valor Y de 32 bytes (o su equivalente encriptado).
- Alice debe descartar el mensaje si la IP y puerto de origen no coinciden con la IP y puerto de destino del Session Request.
- Alice debe descartar el mensaje si los IDs de Conexión de Destino y Origen no coinciden con los IDs de Conexión de Origen y Destino del Session Request.
- Bob envía un bloque relay tag si es solicitado por Alice en el Session Request.
- El bloque New Token no se recomienda en Session Created, porque Bob debería hacer validación del Session Confirmed primero. Ver la sección Tokens más abajo.

#### Problemas

- ¿Incluir opciones de padding mínimo/máximo aquí?

### KDF para la parte 1 de Session Confirmed, usando KDF de Session Created

```
// take h saved from Session Created KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Created)

// MixHash(header)
h = SHA256(h || header)
// h is used as the associated data for the AEAD in Session Confirmed part 1, below

This is the "s" message pattern:

// Alice's X25519 static keys
ask = GENERATE_PRIVATE()
apk = DERIVE_PUBLIC(ask)

// AEAD parameters
// k is from Session Request
n = 1
ad = h
ciphertext = ENCRYPT(k, n++, apk, ad)

// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// h is used as the associated data for the AEAD in Session Confirmed part 2

End of "s" message pattern.

// Header encryption keys for this message
See Session Confirmed part 2 below
```
### KDF para la parte 2 de Session Confirmed

```
This is the "se" message pattern:

// DH(ask, bepk) == DH(besk, apk)
sharedSecret = DH(ask, bepk) = DH(besk, apk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// h from Session Confirmed part 1 is used as the associated data for the AEAD in Session Confirmed part 2
// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF
// retain the hash h for the data phase KDF

End of "se" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Created KDF above

// Header protection keys for data phase
See data phase KDF below
```
### SessionConfirmed (Tipo 2)

Alice envía a Bob, en respuesta a un mensaje Session Created. Bob responde inmediatamente con un mensaje Data que contiene un bloque ACK. Tamaño: 80 + tamaño de carga útil. Tamaño mínimo: Aproximadamente 500 (el tamaño mínimo del bloque de información del router es de aproximadamente 420 bytes)

Contenido Noise: clave estática de Alice Parte 1 del payload Noise: Ninguna Parte 2 del payload Noise: RouterInfo de Alice, y otros bloques Tamaño máximo del payload: MTU - 108 (IPv4) o MTU - 128 (IPv6). Para MTU 1280: El payload máximo es 1172 (IPv4) o 1152 (IPv6). Para MTU 1500: El payload máximo es 1392 (IPv4) o 1372 (IPv6).

Propiedades de Seguridad del Payload:

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
Esto contiene dos marcos ChaChaPoly. El primero es la clave pública estática cifrada de Alice. El segundo es la carga útil de Noise: el RouterInfo cifrado de Alice, opciones opcionales y relleno opcional. Utilizan claves diferentes, porque la función MixKey() se llama entre ellos.

Contenidos sin procesar:

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|   ChaCha20 frame (32 bytes)           |
+   Encrypted and authenticated data    +
+   Alice static key S                  +
| k defined in KDF for Session Created  |
+     n = 1                             +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+ Length varies (remainder of packet)   +
|                                       |
+   ChaChaPoly frame                    +
|   Encrypted and authenticated         |
+   see below for allowed blocks        +
|                                       |
+     k defined in KDF for              +
|     Session Confirmed part 2          |
+     n = 0                             +
|     see KDF for associated data       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, ChaChaPoly encrypted Alice's X25519 static key, little endian
     inside 48 byte ChaChaPoly frame
```
Datos no cifrados (etiquetas de autenticación Poly1305 no mostradas):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
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
|        Noise Payload                  |
+        (length varies)                +
|        see below for allowed blocks   |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As sent in Session Request,
                             or one received in Session Confirmed?

Packet Number :: 0 always, for all fragments, even if retransmitted

type :: 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility

S :: 32 bytes, Alice's X25519 static key, little endian
```
#### Carga útil

- Bloque RouterInfo (debe ser el primer bloque)
- Bloque Options (opcional)
- Bloque New Token (opcional)
- Bloque Relay Request (opcional)
- Bloque Peer Test (opcional)
- Bloque First Packet Number (opcional)
- Bloques I2NP, First Fragment o Follow-on Fragment (opcional, pero probablemente sin espacio)
- Bloque Padding (opcional)

El tamaño mínimo de la carga útil es de 8 bytes. Dado que el bloque RouterInfo será mucho más que eso, el requisito se cumple solo con ese bloque.

#### Notas

- Bob debe realizar la validación habitual de Router Info. Asegurarse de que el tipo de firma sea compatible, verificar la firma, verificar que la marca de tiempo esté dentro de los límites, y cualquier otra verificación necesaria. Ver a continuación las notas sobre el manejo de Router Infos fragmentados.

- Bob debe verificar que la clave estática de Alice recibida en el primer frame coincida con la clave estática en la Router Info. Bob debe primero buscar en la Router Info una Router Address de NTCP o SSU2 con una opción de versión (v) coincidente. Ver las secciones Router Info Publicada y Router Info No Publicada a continuación. Ver más abajo las notas sobre el manejo de Router Infos fragmentadas.

- Si Bob tiene una versión anterior de la RouterInfo de Alice en su netdb, verificar que la clave estática en la router info sea la misma en ambas, si está presente, y si la versión anterior tiene menos de XXX de antigüedad (ver tiempo de rotación de claves más abajo)

- Bob debe validar que la clave estática de Alice es un punto válido en la curva aquí.

- Se deben incluir opciones para especificar parámetros de relleno.

- En caso de cualquier error, incluyendo falla de AEAD, RI, DH, timestamp, o validación de clave, Bob debe detener el procesamiento adicional de mensajes y cerrar la conexión sin responder.

- Contenido del frame de la parte 2 del mensaje 3: El formato de este frame es el mismo que el formato de los frames de la fase de datos, excepto que la longitud del frame es enviada por Alice en la Solicitud de Sesión. Ver más abajo para el formato del frame de la fase de datos. El frame debe contener de 1 a 4 bloques en el siguiente orden:

1)  Bloque de información del router de Alice (requerido)   2)  Bloque de opciones (opcional)   3)  Bloques I2NP (opcional)

4\) Bloque de relleno (opcional) Este frame nunca debe contener ningún otro tipo de bloque. TODO: ¿qué pasa con relay y peer test?

- Se recomienda el bloque de relleno de la parte 2 del mensaje 3.

- Puede que no haya espacio, o solo una pequeña cantidad de espacio, disponible para bloques I2NP, dependiendo del MTU y el tamaño del Router Info. NO incluyas bloques I2NP si el Router Info está fragmentado. La implementación más simple puede ser nunca incluir bloques I2NP en el mensaje Session Confirmed, y enviar todos los bloques I2NP en mensajes Data posteriores. Ver la sección de bloques Router Info más abajo para el tamaño máximo de bloque.

#### Fragmentación de Sesión Confirmada

El mensaje Session Confirmed debe contener la Router Info firmada completa de Alice para que Bob pueda realizar varias verificaciones requeridas:

- La clave estática "s" en el RI coincide con la clave estática en el handshake
- La clave de introducción "i" en el RI debe ser extraída y válida, para ser utilizada en la fase de datos
- La firma del RI es válida

Desafortunadamente, el Router Info, incluso cuando está comprimido con gzip en el bloque RI, puede exceder el MTU. Por lo tanto, el Session Confirmed puede fragmentarse a través de dos o más paquetes. Este es el ÚNICO caso en el protocolo SSU2 donde una carga útil protegida por AEAD se fragmenta a través de dos o más paquetes.

Los encabezados de cada paquete se construyen de la siguiente manera:

- TODOS los headers son headers cortos con el mismo número de paquete 0
- TODOS los headers contienen un campo "frag", con el número de fragmento y el número total de fragmentos
- El header sin cifrar del fragmento 0 es el dato asociado (AD) para el mensaje "jumbo"
- Cada header se cifra usando los últimos 24 bytes de datos en ESE paquete

Construye la serie de paquetes de la siguiente manera:

- Crear un solo bloque RI (fragmento 0 de 1 en el campo frag del bloque RI). No usamos fragmentación de bloques RI, eso era para un método alternativo de resolver el mismo problema.
- Crear una carga útil "jumbo" con el bloque RI y cualquier otro bloque que se incluya
- Calcular el tamaño total de datos (sin incluir el encabezado), que es el tamaño de la carga útil + 64 bytes para la clave estática y dos MACs
- Calcular el espacio disponible en cada paquete, que es la MTU menos el encabezado IP (20 o 40), menos el encabezado UDP (8), menos el encabezado corto SSU2 (16). El overhead total por paquete es 44 (IPv4) o 64 (IPv6).
- Calcular el número de paquetes.
- Calcular el tamaño de los datos en el último paquete. Debe ser mayor o igual a 24 bytes, para que la encriptación del encabezado funcione. Si es muy pequeño, agregar un bloque de relleno, O aumentar el tamaño del bloque de relleno si ya está presente, O reducir el tamaño de uno de los otros paquetes para que el último paquete sea lo suficientemente grande.
- Crear el encabezado sin encriptar para el primer paquete, con el número total de fragmentos en el campo frag, y encriptar la carga útil "jumbo" con Noise, usando el encabezado como AD, como siempre.
- Dividir el paquete jumbo encriptado en fragmentos
- Agregar un encabezado sin encriptar para cada fragmento 1-n
- Encriptar el encabezado para cada fragmento 0-n. Cada encabezado usa las MISMAS k_header_1 y k_header_2 como se define arriba en el KDF de Session Confirmed.
- Transmitir todos los fragmentos

Proceso de reensamblaje:

Cuando Bob recibe cualquier mensaje Session Confirmed, descifra el encabezado, inspecciona el campo frag y determina que el Session Confirmed está fragmentado. No descifra (y no puede descifrar) el mensaje hasta que todos los fragmentos sean recibidos y reensamblados.

- Preservar el encabezado para el fragmento 0, ya que se usa como AD de Noise
- Descartar los encabezados de otros fragmentos antes del reensamblaje
- Reensamblar la carga útil "jumbo", con el encabezado del fragmento 0 como AD, y descifrar con Noise
- Validar el bloque RI como de costumbre
- Proceder a la fase de datos y enviar ACK 0, como de costumbre

No hay un mecanismo para que Bob confirme fragmentos individuales. Cuando Bob recibe todos los fragmentos, los reensambla, los descifra y valida el contenido, Bob hace un split() como de costumbre, entra en la fase de datos y envía un ACK del paquete número 0.

Si Alice no recibe un ACK del paquete número 0, debe retransmitir todos los paquetes de sesión confirmada tal como están.

Ejemplos:

Para MTU de 1500 sobre IPv6, la carga útil máxima es 1372, la sobrecarga del bloque RI es 5, el tamaño máximo de datos RI (comprimidos con gzip) es 1367 (asumiendo que no hay otros bloques). Con dos paquetes, la sobrecarga del segundo paquete es 64, por lo que puede contener otros 1436 bytes de carga útil. Así que dos paquetes son suficientes para un RI comprimido de hasta 2803 bytes.

El RI comprimido más grande visto en la red actual es de aproximadamente 1400 bytes; por lo tanto, en la práctica, dos fragmentos deberían ser suficientes, incluso con un MTU mínimo de 1280. El protocolo permite un máximo de 15 fragmentos.

Análisis de seguridad:

La integridad y seguridad de un Session Confirmed fragmentado es la misma que la de uno no fragmentado. Cualquier alteración de cualquier fragmento causará que el AEAD de Noise falle después del reensamblaje. Los encabezados de los fragmentos después del fragmento 0 solo se usan para identificar el fragmento. Incluso si un atacante en la ruta tuviera la clave k_header_2 utilizada para cifrar el encabezado (improbable, derivada del handshake), esto no permitiría al atacante sustituir un fragmento válido.

### KDF para la fase de datos

La fase de datos utiliza el encabezado para los datos asociados.

El KDF genera dos claves de cifrado k_ab y k_ba a partir de la clave de encadenamiento ck, utilizando HMAC-SHA256(key, data) como se define en [RFC-2104](https://tools.ietf.org/html/rfc2104). Esta es la función split(), exactamente como se define en la especificación Noise.

```
// split()
// chainKey = from handshake phase
keydata = HKDF(chainKey, ZEROLEN, "", 64)
k_ab = keydata[0:31]
k_ba = keydata[32:63]

// key is k_ab for Alice to Bob
// key is k_ba for Bob to Alice

keydata = HKDF(key, ZEROLEN, "HKDFSSU2DataKeys", 64)
k_data = keydata[0:31]
k_header_2 = keydata[32:63]


// AEAD parameters
k = k_data
n = 4 byte packet number from header
ad = 16 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for data phase
// aik = Alice's intro key
// bik = Bob's intro key
k_header_1 = Receiver's intro key (aik or bik)
k_header_2: from above
```
### Mensaje de Datos (Tipo 6)

Payload de Noise: Se permiten todos los tipos de bloques. Tamaño máximo de payload: MTU - 60 (IPv4) o MTU - 80 (IPv6). Para MTU de 1500: El payload máximo es 1440 (IPv4) o 1420 (IPv6).

A partir de la segunda parte de Session Confirmed, todos los mensajes están dentro de una carga útil ChaChaPoly autenticada y cifrada. Todo el relleno está dentro del mensaje. Dentro de la carga útil hay un formato estándar con cero o más "bloques". Cada bloque tiene un tipo de un byte y una longitud de dos bytes. Los tipos incluyen fecha/hora, mensaje I2NP, opciones, terminación y relleno.

Nota: Bob puede, pero no está obligado, a enviar su RouterInfo a Alice como su primer mensaje a Alice en la fase de datos.

Propiedades de Seguridad de la Carga Útil:

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
#### Notas

- El router debe descartar un mensaje con un error AEAD.

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with intro key and         +
|  derived key, see Data Phase KDF      |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in Data Phase KDF          +
|  n = packet number from header        |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Datos no cifrados (etiqueta de autenticación Poly1305 no mostrada):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: See below

Packet Number :: Random number generated by Charlie

type :: 11

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: See below

Token :: 8 byte unsigned integer, randomly generated by Charlie, nonzero.
```
#### Notas

- El tamaño mínimo de carga útil es de 8 bytes. Este requisito se cumplirá con cualquier bloque ACK, I2NP, First Fragment o Follow-on Fragment. Si no se cumple el requisito, debe incluirse un bloque Padding.
- Cada número de paquete solo puede usarse una vez. Al retransmitir mensajes I2NP o fragmentos, debe usarse un nuevo número de paquete.

### KDF para Prueba de Pares

```
// AEAD parameters
// aik = Alice's intro key
k = aik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = aik
k_header_2 = aik
```
### Prueba de Par (Tipo 7)

Charlie envía a Alice, y Alice envía a Charlie, solo para las fases 5-7 de Peer Test. Las fases 1-4 de Peer Test deben enviarse en sesión usando un bloque Peer Test en un mensaje Data. Consulta las secciones Bloque Peer Test y Proceso Peer Test a continuación para más información.

Tamaño: 48 + tamaño de payload.

Carga útil Noise: Ver más abajo.

Contenido sin procesar:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Datos no cifrados (etiqueta de autenticación Poly1305 no mostrada):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

Packet Number :: Random number generated by Alice

type :: 10

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: zero
```
#### Carga útil

- Bloque DateTime
- Bloque Address (requerido para mensajes 6 y 7, ver nota a continuación)
- Bloque Peer Test
- Bloque Padding (opcional)

El tamaño mínimo de carga útil es de 8 bytes. Dado que el bloque Peer Test totaliza más que eso, el requisito se cumple únicamente con este bloque.

En los mensajes 5 y 7, el bloque Peer Test puede ser idéntico al bloque de los mensajes 3 y 4 de la sesión, conteniendo el acuerdo firmado por Charlie, o puede ser regenerado. La firma es opcional.

En el mensaje 6, el bloque Peer Test puede ser idéntico al bloque de los mensajes 1 y 2 de la sesión, conteniendo la solicitud firmada por Alice, o puede ser regenerado. La firma es opcional.

IDs de Conexión: Los dos IDs de conexión se derivan del nonce de prueba. Para los mensajes 5 y 7 enviados de Charlie a Alice, el ID de Conexión de Destino son dos copias del nonce de prueba de 4 bytes en big-endian, es decir, ((nonce << 32) | nonce). El ID de Conexión de Origen es el inverso del ID de Conexión de Destino, es decir, ~((nonce << 32) | nonce). Para el mensaje 6 enviado de Alice a Charlie, intercambiar los dos IDs de conexión.

Contenidos del bloque de direcciones:

- En el mensaje 5: No requerido.
- En el mensaje 6: La IP y puerto de Charlie según se seleccionó del RI de Charlie.
- En el mensaje 7: La IP y puerto reales de Alice desde donde se recibió el mensaje 6.

### KDF para Reintentos

El requisito para el mensaje Retry es que Bob no está obligado a descifrar el mensaje Session Request para generar un mensaje Retry en respuesta. Además, este mensaje debe ser rápido de generar, usando únicamente cifrado simétrico.

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Reintentar (Tipo 9)

Bob envía a Alice, en respuesta a un mensaje Session Request o Token Request. Alice responde con un nuevo Session Request. Tamaño: 48 + tamaño del payload.

También sirve como mensaje de Terminación (es decir, "No Reintentar") si se incluye un bloque de Terminación.

Carga útil de Noise: Ver más abajo.

Contenidos sin procesar:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Datos no cifrados (etiqueta de autenticación Poly1305 no mostrada):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: The Source Connection ID
                             received from Alice in Token Request
                             or Session Request

Packet Number :: Random number generated by Bob

type :: 9

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: The Destination Connection ID
                        received from Alice in Token Request
                        or Session Request

Token :: 8 byte unsigned integer, randomly generated by Bob, nonzero,
         or zero if session is rejected and a termination block is included
```
#### Carga útil

- Bloque DateTime
- Bloque Address
- Bloque Options (opcional)
- Bloque Termination (opcional, si la sesión es rechazada)
- Bloque Padding (opcional)

El tamaño mínimo de la carga útil es de 8 bytes. Dado que los bloques DateTime y Address suman más que eso, el requisito se cumple con solo esos dos bloques.

#### Notas

- Para proporcionar resistencia al sondeo, un router no debe enviar un mensaje Retry en respuesta a un mensaje Session Request o Token Request a menos que los campos de tipo de mensaje, versión de protocolo e ID de red en el mensaje Request sean válidos.
- Para limitar la magnitud de cualquier ataque de amplificación que pueda llevarse a cabo usando direcciones de origen falsificadas, el mensaje Retry no debe contener grandes cantidades de relleno. Se recomienda que el mensaje Retry no sea más grande que tres veces el tamaño del mensaje al que está respondiendo. Alternativamente, usa un método simple como agregar una cantidad aleatoria de relleno en el rango de 1-64 bytes.

### KDF para Solicitud de Token

Este mensaje debe ser rápido de generar, usando únicamente cifrado simétrico.

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Solicitud de Token (Tipo 10)

Alice envía a Bob. Bob responde con un mensaje Retry. Tamaño: 48 + tamaño de payload.

Si Alice no tiene un token válido, Alice debería enviar este mensaje en lugar de una Solicitud de Sesión, para evitar la sobrecarga de cifrado asimétrico al generar una Solicitud de Sesión.

Carga útil de Noise: Ver más abajo.

Contenido sin procesar:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Datos no encriptados (etiqueta de autenticación Poly1305 no mostrada):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|    flags     |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As specified in session setup

Packet Number :: 4 byte big endian integer

type :: 6

flags :: 3 bytes, unused, set to 0 for future compatibility
```
#### Carga útil

- Bloque DateTime
- Bloque de relleno

El tamaño mínimo de la carga útil es de 8 bytes.

#### Notas

- Para proporcionar resistencia al sondeo, un router no debería enviar un mensaje Retry en respuesta a un mensaje Token Request a menos que el tipo de mensaje, la versión del protocolo y los campos de ID de red en el mensaje Token Request sean válidos.
- Este NO es un mensaje Noise estándar y no es parte del handshake. No está vinculado al mensaje Session Request más que por los IDs de conexión.
- En la mayoría de errores, incluyendo AEAD, o aparente replay, Bob debería detener el procesamiento posterior de mensajes y descartar el mensaje sin responder.
- Bob debe rechazar conexiones donde el valor del timestamp esté demasiado alejado del tiempo actual. Llamemos al delta de tiempo máximo "D". Bob debe mantener una caché local de valores de handshake previamente utilizados y rechazar duplicados, para prevenir ataques de replay. Los valores en la caché deben tener una vida útil de al menos 2*D. Los valores de caché dependen de la implementación, sin embargo puede usarse el valor X de 32 bytes (o su equivalente cifrado).
- Bob PUEDE enviar un mensaje Retry conteniendo un token cero y un bloque Termination con un código de razón de desajuste de reloj si el timestamp en el bloque DateTime está demasiado desajustado.
- Tamaño mínimo: TBD, ¿mismas reglas que para Session Created?

### KDF para Hole Punch

Este mensaje debe ser rápido de generar, usando solo cifrado simétrico.

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Hole Punch (Tipo 11)

Charlie envía a Alice, en respuesta a un Relay Intro recibido de Bob. Alice responde con una nueva Session Request. Tamaño: 48 + tamaño de payload.

Carga útil de Noise: Ver más abajo.

Contenidos sin procesar:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Datos no cifrados (etiqueta de autenticación Poly1305 no mostrada):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: See below

type :: 7

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random number generated by Alice or Charlie

Source Connection ID :: See below

Token :: Randomly generated by Alice or Charlie, ignored
```
#### Carga útil

- Bloque DateTime
- Bloque Address
- Bloque Relay Response
- Bloque Padding (opcional)

El tamaño mínimo de la carga útil es de 8 bytes. Dado que los bloques DateTime y Address suman más de esa cantidad, el requisito se cumple con solo esos dos bloques.

IDs de Conexión: Los dos IDs de conexión se derivan del nonce de relay. El ID de Conexión de Destino son dos copias del nonce de relay de 4 bytes en formato big-endian, es decir, ((nonce << 32) | nonce). El ID de Conexión de Origen es el inverso del ID de Conexión de Destino, es decir, ~((nonce << 32) | nonce).

Alice debe ignorar el token en el encabezado. El token que se debe usar en la Session Request está en el bloque Relay Response.

## Carga útil de Noise

Cada carga útil de Noise contiene cero o más "bloques".

Esto utiliza el mismo formato de bloque definido en las especificaciones [NTCP2](/docs/specs/ntcp2) y [ECIES](/docs/specs/ecies). Los tipos de bloques individuales se definen de manera diferente. El término equivalente en QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) es "frames".

Existen preocupaciones de que alentar a los implementadores a compartir código puede llevar a problemas de análisis. Los implementadores deben considerar cuidadosamente los beneficios y riesgos de compartir código, y asegurar que las reglas de ordenamiento y bloques válidos sean diferentes para los dos contextos.

### Formato de Carga Útil

Hay uno o más bloques en la carga útil cifrada. Un bloque es un formato simple Tag-Length-Value (TLV). Cada bloque contiene un identificador de un byte, una longitud de dos bytes y cero o más bytes de datos. Este formato es idéntico al de [NTCP2](/docs/specs/ntcp2) y [ECIES](/docs/specs/ecies), sin embargo las definiciones de bloques son diferentes.

Para la extensibilidad, los receptores deben ignorar los bloques con identificadores desconocidos y tratarlos como relleno.

(Etiqueta de autenticación Poly1305 no mostrada):

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

blk :: 1 byte, see below
size :: 2 bytes, big endian, size of data to follow, 0 - TBD
data :: the data
```
El cifrado del encabezado utiliza los últimos 24 bytes del paquete como IV para las dos operaciones ChaCha20. Como todos los paquetes terminan con un MAC de 16 bytes, esto requiere que todas las cargas útiles de los paquetes tengan un mínimo de 8 bytes. Si una carga útil no cumpliera de otra manera con este requisito, debe incluirse un bloque de Padding.

La carga útil máxima de ChaChaPoly varía según el tipo de mensaje, MTU y el tipo de dirección IPv4 o IPv6. La carga útil máxima es MTU - 60 para IPv4 y MTU - 80 para IPv6. Los datos de carga útil máxima son MTU - 63 para IPv4 y MTU - 83 para IPv6. El límite superior es de aproximadamente 1440 bytes para IPv4, MTU 1500, mensaje de datos. El tamaño máximo total del bloque es el tamaño máximo de carga útil. El tamaño máximo de un solo bloque es el tamaño máximo total del bloque. El tipo de bloque es 1 byte. La longitud del bloque es 2 bytes. El tamaño máximo de datos de un solo bloque es el tamaño máximo de un solo bloque menos 3.

Notas:

- Los implementadores deben asegurar que al leer un bloque, los datos malformados o maliciosos no causarán que las lecturas se desborden hacia el siguiente bloque o más allá del límite de la carga útil.
- Las implementaciones deberían ignorar los tipos de bloque desconocidos para compatibilidad hacia adelante.

Tipos de bloques:

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
### Reglas de Ordenamiento de Bloques

En la Sesión Confirmada, la Información del Router debe ser el primer bloque.

En todos los demás mensajes, el orden no está especificado, excepto por los siguientes requisitos: El relleno (Padding), si está presente, debe ser el último bloque. La terminación (Termination), si está presente, debe ser el último bloque excepto por el relleno (Padding). No se permiten múltiples bloques de relleno (Padding) en una sola carga útil.

### Especificaciones de Bloques

#### FechaHora

Para la sincronización de tiempo:

```
+----+----+----+----+----+----+----+
| 0  |    4    |     timestamp     |
+----+----+----+----+----+----+----+

blk :: 0
size :: 2 bytes, big endian, value = 4
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
```
Notas:

- A diferencia de SSU 1, no hay marca de tiempo en el encabezado del paquete para la fase de datos en SSU 2.
- Las implementaciones deberían enviar periódicamente bloques DateTime en la fase de datos.
- Las implementaciones deben redondear al segundo más cercano para prevenir sesgo de reloj en la red.

#### Opciones

Pasa opciones actualizadas. Las opciones incluyen: relleno mínimo y máximo.

El bloque de opciones tendrá longitud variable.

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
Problemas de Opciones:

- La negociación de opciones está por definir (TBD).

#### RouterInfo

Pasar el RouterInfo de Alice a Bob. Se usa únicamente en la carga útil de la parte 2 de Session Confirmed. No debe usarse en la fase de datos; usar en su lugar un mensaje I2NP DatabaseStore.

Tamaño Mínimo: Aproximadamente 420 bytes, a menos que la identidad del router y la firma en la información del router sean comprimibles, lo cual es improbable.

NOTA: El bloque Router Info nunca se fragmenta. El campo frag siempre es 0/1. Consulte la sección Fragmentación de Sesión Confirmada anterior para más información.

```
+----+----+----+----+----+----+----+----+
| 2  |  size   |flag|frag|              |
+----+----+----+----+----+              +
|                                       |
+       Router Info fragment            +
| (Alice RI in Session Confirmed)       |
+ (Alice, Bob, or third-party           +
|  RI in data phase)                    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 2
size :: 2 bytes, big endian, 2 + fragment size
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 0 for local store, 1 for flood request
       bit 1: 0 for uncompressed, 1 for gzip compressed
       bits 7-2: Unused, set to 0 for future compatibility
frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number, always 0
       bits 3-0: total fragments, always 1, big endian

routerinfo :: Alice's or Bob's RouterInfo
```
Notas:

- La Router Info está opcionalmente comprimida con gzip, como se indica por el bit de bandera 1. Esto es diferente de NTCP2, donde nunca se comprime, y de un DatabaseStore Message, donde siempre se comprime. La compresión es opcional porque usualmente es de poco beneficio para Router Infos pequeñas, donde hay poco contenido comprimible, pero es muy beneficiosa para Router Infos grandes con varias Router Addresses comprimibles. Se recomienda la compresión si permite que una Router Info quepa en un solo paquete Session Confirmed sin fragmentación.
- Tamaño máximo del primer o único fragmento en el mensaje Session Confirmed: MTU - 113 para IPv4 o MTU - 133 para IPv6. Asumiendo una MTU predeterminada de 1500 bytes, y sin otros bloques en el mensaje, 1387 para IPv4 o 1367 para IPv6. El 97% de las router infos actuales son menores que 1367 sin gzipping. El 99.9% de las router infos actuales son menores que 1367 cuando están gzipped. Asumiendo una MTU mínima de 1280 bytes, y sin otros bloques en el mensaje, 1167 para IPv4 o 1147 para IPv6. El 94% de las router infos actuales son menores que 1147 sin gzipping. El 97% de las router infos actuales son menores que 1147 cuando están gzipped.
- El byte frag ahora no se usa, el bloque Router Info nunca se fragmenta. El byte frag debe establecerse en fragmento 0, total de fragmentos 1. Consulta la sección Session Confirmed Fragmentation arriba para más información.
- No se debe solicitar flooding a menos que haya RouterAddresses publicadas en la RouterInfo. El router receptor no debe hacer flood de la RouterInfo a menos que tenga RouterAddresses publicadas en ella.
- Este protocolo no proporciona un reconocimiento de que la RouterInfo fue almacenada o flooded. Si se desea reconocimiento, y el receptor es floodfill, el emisor debería en su lugar enviar un DatabaseStoreMessage I2NP estándar con un token de respuesta.

#### Mensaje I2NP

Un mensaje I2NP completo con un encabezado modificado.

Esto utiliza los mismos 9 bytes para el encabezado I2NP como en [NTCP2](/docs/specs/ntcp2) (tipo, id del mensaje, expiración corta).

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
Notas:

- Este es el mismo formato de encabezado I2NP de 9 bytes utilizado en NTCP2.
- Este es exactamente el mismo formato que el bloque First Fragment, pero el tipo de bloque indica que este es un mensaje completo.
- El tamaño máximo incluyendo el encabezado I2NP de 9 bytes es MTU - 63 para IPv4 y MTU - 83 para IPv6.

#### Primer Fragmento

El primer fragmento (fragmento #0) de un mensaje I2NP con un encabezado modificado.

Esto usa los mismos 9 bytes para el encabezado I2NP como en [NTCP2](/docs/specs/ntcp2) (tipo, id del mensaje, expiración corta).

El número total de fragmentos no está especificado.

```
+----+----+----+----+----+----+----+----+
| 4  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |                   |
+----+----+----+----+                   +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 4
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: Partial I2NP message body, bytes 0 - (size - 10)
```
Notas:

- Este es el mismo formato de cabecera I2NP de 9 bytes utilizado en NTCP2.
- Este es exactamente el mismo formato que el bloque de Mensaje I2NP, pero el tipo de bloque indica que este es el primer fragmento de un mensaje.
- La longitud del mensaje parcial debe ser mayor que cero.
- Como en SSU 1, se recomienda enviar el último fragmento primero, para que el receptor conozca el número total de fragmentos y pueda asignar eficientemente los búferes de recepción.
- El tamaño máximo incluyendo la cabecera I2NP de 9 bytes es MTU - 63 para IPv4 y MTU - 83 para IPv6.

#### Fragmento de Continuación

Un fragmento adicional (número de fragmento mayor que cero) de un mensaje I2NP.

```
+----+----+----+----+----+----+----+----+
| 5  |  size   |frag|    msg id         |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 5
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 5).
frag :: Fragment info:
        Bit order: 76543210 (bit 7 is MSB)
        bits 7-1: fragment number 1 - 127 (0 not allowed)
        bit 0: isLast (1 = true)
msg id :: 4 bytes, big endian, I2NP message ID
message :: Partial I2NP message body
```
Notas:

- La longitud del mensaje parcial debe ser mayor que cero.
- Como en SSU 1, se recomienda enviar el último fragmento primero, para que el receptor conozca el número total de fragmentos y pueda asignar eficientemente los buffers de recepción.
- Como en SSU 1, el número máximo de fragmento es 127, pero el límite práctico es 63 o menos. Las implementaciones pueden limitar el máximo a lo que sea práctico para un tamaño máximo de mensaje I2NP de aproximadamente 64 KB, que son unos 55 fragmentos con una MTU mínima de 1280. Ver la sección Tamaño Máximo de Mensaje I2NP más abajo.
- El tamaño máximo del mensaje parcial (sin incluir frag y message id) es MTU - 68 para IPv4 y MTU - 88 para IPv6.

#### Terminación

Desconectar la conexión. Este debe ser el último bloque sin relleno en la carga útil.

```
+----+----+----+----+----+----+----+----+
| 6  |  size   |    valid data packets  |
+----+----+----+----+----+----+----+----+
    received   | rsn|     addl data     |
+----+----+----+----+                   +
~               .   .   .               ~
+----+----+----+----+----+----+----+----+

blk :: 6
size :: 2 bytes, big endian, value = 9 or more
valid data packets received :: The number of valid packets received
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
       11: Session Request error
       12: Session Created error
       13: Session Confirmed error
       14: Timeout
       15: RI signature verification fail
       16: s parameter missing, invalid, or mismatched in RouterInfo
       17: banned
       18: bad token
       19: connection limits
       20: incompatible version
       21: wrong net ID
       22: replaced by new session
addl data :: optional, 0 or more bytes, for future expansion, debugging,
             or reason text.
             Format unspecified and may vary based on reason code.
```
Notas:

- No todas las razones pueden ser utilizadas realmente, depende de la implementación. La mayoría de fallos generalmente resultarán en que el mensaje sea descartado, no en una terminación. Ver notas en las secciones de mensajes de handshake arriba. Las razones adicionales listadas son para consistencia, registro, depuración, o si cambian las políticas.
- Se recomienda que un bloque ACK sea incluido con el bloque de Terminación.
- En la fase de datos, por cualquier razón que no sea "terminación recibida", el peer debería responder con un bloque de terminación con la razón "terminación recibida".

#### RelayRequest

Enviado en un mensaje de datos dentro de la sesión, de Alice a Bob. Ver la sección Proceso de Relay más abajo.

```
+----+----+----+----+----+----+----+----+
|  7 |  size   |flag|       nonce       |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 7
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility

The data below here is covered
by the signature, and Bob forwards it unmodified.

nonce :: 4 bytes, randomly generated by Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
Notas:

- La dirección IP siempre se incluye (a diferencia de SSU 1) y puede ser diferente a la IP utilizada para la sesión.

Firma:

Alice firma la solicitud y la incluye en este bloque; Bob la reenvía en el bloque Relay Intro a Charlie. Algoritmo de firma: Firmar los siguientes datos con la clave de firma del router de Alice:

- prólogo: 16 bytes "RelayRequestData", sin terminación nula (no incluido en el mensaje)
- bhash: hash del router de Bob de 32 bytes (no incluido en el mensaje)
- chash: hash del router de Charlie de 32 bytes (no incluido en el mensaje)
- nonce: nonce de 4 bytes
- etiqueta de relay: etiqueta de relay de 4 bytes
- marca de tiempo: marca de tiempo de 4 bytes (segundos)
- ver: versión SSU de 1 byte
- asz: tamaño del endpoint (puerto + IP) de 1 byte (6 o 18)
- AlicePort: número de puerto de Alice de 2 bytes
- IP de Alice: dirección IP de Alice de (asz - 2) bytes

#### RelayResponse

Enviado en un mensaje de Datos dentro de la sesión, de Charlie a Bob o de Bob a Alice, Y en el mensaje Hole Punch de Charlie a Alice. Ver la sección Proceso de Retransmisión más abajo.

```
+----+----+----+----+----+----+----+----+
|  8 |  size   |flag|code|    nonce
+----+----+----+----+----+----+----+----+
     |     timestamp     | ver| csz|Char
+----+----+----+----+----+----+----+----+
 Port|   Charlie IP addr |              |
+----+----+----+----+----+              +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

blk :: 8
size :: 2 bytes, 6
flag :: 1 byte flags, Unused, set to 0 for future compatibility
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, Charlie is banned
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, relay tag not found
       6: rejected by Bob, Alice RI not found
       7-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       71-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD

The data below is covered by the signature if the code is 0 (accept).
Bob forwards it unmodified.

nonce :: 4 bytes, as received from Bob or Alice

The data below is present only if the code is 0 (accept).

timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
csz :: 1 byte endpoint (port + IP) size (0 or 6 or 18)
       may be 0 for some rejection codes
CharliePort :: 2 byte Charlie's port number, big endian
               not present if csz is 0
Charlie IP :: (csz - 2) byte representation of Charlie's IP address,
              network byte order
              not present if csz is 0
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Charlie.
             Not present if rejected by Bob.
token :: Token generated by Charlie for Alice to use
         in the Session Request.
         Only present if code is 0 (accept)
```
Notas:

El token debe ser usado inmediatamente por Alice en la Session Request.

Firma:

Si Charlie acepta (código de respuesta 0) o rechaza (código de respuesta 64 o superior), Charlie firma la respuesta y la incluye en este bloque; Bob la reenvía en el bloque Relay Response a Alice. Algoritmo de firma: Firmar los siguientes datos con la clave de firma del router de Charlie:

- prólogo: 16 bytes "RelayAgreementOK", no terminado en null (no incluido en el mensaje)
- bhash: Hash del router de Bob de 32 bytes (no incluido en el mensaje)
- nonce: nonce de 4 bytes
- timestamp: marca de tiempo de 4 bytes (segundos)
- ver: versión SSU de 1 byte
- csz: tamaño del endpoint (puerto + IP) de 1 byte (0 o 6 o 18)
- CharliePort: número de puerto de Charlie de 2 bytes (no presente si csz es 0)
- Charlie IP: dirección IP de Charlie de (csz - 2) bytes (no presente si csz es 0)

Si Bob rechaza (código de respuesta 1-63), Bob firma la respuesta y la incluye en este bloque. Algoritmo de firma: Firmar los siguientes datos con la clave de firma del router de Bob:

- prólogo: 16 bytes "RelayAgreementOK", sin terminación nula (no incluido en el mensaje)
- bhash: hash del router de Bob de 32 bytes (no incluido en el mensaje)
- nonce: nonce de 4 bytes
- timestamp: timestamp de 4 bytes (segundos)
- ver: versión SSU de 1 byte
- csz: 1 byte = 0

#### RelayIntro

Enviado en un mensaje Data dentro de la sesión, de Bob a Charlie. Ver la sección Proceso de Relay más abajo.

Debe estar precedido por un bloque RouterInfo, o un bloque de mensaje I2NP DatabaseStore (o fragmento), que contenga la información del router de Alice, ya sea en la misma carga útil (si hay espacio), o en un mensaje anterior.

```
+----+----+----+----+----+----+----+----+
|  9 |  size   |flag|                   |
+----+----+----+----+                   +
|                                       |
+                                       +
|         Alice Router Hash             |
+             32 bytes                  +
|                                       |
+                   +----+----+----+----+
|                   |      nonce        |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 9
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's 32-byte router hash,

The data below here is covered
by the signature, as received from Alice in the Relay Request,
and Bob forwards it unmodified.

nonce :: 4 bytes, as received from Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
Notas:

- Para IPv4, la dirección IP de Alice siempre tiene 4 bytes, porque Alice está tratando de conectarse a Charlie vía IPv4. IPv6 es compatible, y la dirección IP de Alice puede tener 16 bytes.
- Para IPv4, este mensaje debe ser enviado vía una conexión IPv4 establecida, ya que esa es la única forma en que Bob conoce la dirección IPv4 de Charlie para devolverla a Alice en el [RelayResponse](#relayresponse). IPv6 es compatible, y este mensaje puede ser enviado vía una conexión IPv6 establecida.
- Cualquier dirección SSU publicada con introducers debe contener "4" o "6" en la opción "caps".

Firma:

Alice firma la solicitud y Bob la reenvía en este bloque a Charlie. Algoritmo de verificación: Verificar los siguientes datos con la clave de firma del router de Alice:

- prólogo: 16 bytes "RelayRequestData", no terminado en null (no incluido en el mensaje)
- bhash: hash del router de Bob de 32 bytes (no incluido en el mensaje)
- chash: hash del router de Charlie de 32 bytes (no incluido en el mensaje)
- nonce: nonce de 4 bytes
- relay tag: etiqueta de relay de 4 bytes
- timestamp: marca de tiempo de 4 bytes (segundos)
- ver: versión SSU de 1 byte
- asz: tamaño del endpoint (puerto + IP) de 1 byte (6 o 18)
- AlicePort: número de puerto de Alice de 2 bytes
- Alice IP: dirección IP de Alice de (asz - 2) bytes

#### PeerTest

Enviado ya sea en un mensaje Data dentro de la sesión, o un mensaje Peer Test fuera de la sesión. Ver la sección Proceso de Peer Test a continuación.

Para el mensaje 2, debe estar precedido por un bloque RouterInfo, o un bloque de mensaje I2NP DatabaseStore (o fragmento), que contenga la información del router de Alice, ya sea en la misma carga útil (si hay espacio), o en un mensaje anterior.

Para el mensaje 4, si el relay es aceptado (código de razón 0), debe ir precedido por un bloque RouterInfo, o bloque de mensaje I2NP DatabaseStore (o fragmento), que contenga la Router Info de Charlie, ya sea en la misma carga útil (si hay espacio), o en un mensaje anterior.

```
+----+----+----+----+----+----+----+----+
| 10 |  size   | msg|code|flag|         |
+----+----+----+----+----+----+         +
| Alice router hash (message 2 only)    |
+             or                        +
| Charlie router hash (message 4 only)  |
+ or all zeros if rejected by Bob       +
| Not present in messages 1,3,5,6,7     |
+                             +----+----+
|                             | ver|
+----+----+----+----+----+----+----+----+
   nonce       |     timestamp     | asz|
+----+----+----+----+----+----+----+----+
|AlicePort|  Alice IP address |         |
+----+----+----+----+----+----+         +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 10
size :: 2 bytes, big endian, size of data to follow
msg :: 1 byte message number 1-7
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, no Charlie available
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, address unsupported
       6-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       70-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD
       reject codes only allowed in messages 3 and 4
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's or Charlie's 32-byte router hash,
        only present in messages 2 and 4.
        All zeros (fake hash) in message 4 if rejected by Bob.

For messages 1-4, the data below here is covered
by the signature, if present, and Bob forwards it unmodified.

ver :: 1 byte SSU version:
       1: SSU 1 (not supported)
       2: SSU 2 (required)
nonce :: 4 byte test nonce, big endian
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice or Charlie.
             Only present for messages 1-4.
             Optional in message 5-7.
```
Notas:

- A diferencia de SSU 1, el mensaje 1 debe incluir la dirección IP y el puerto de Alice.

- Se admite la prueba de direcciones IPv6, y la comunicación entre Alice-Bob y Alice-Charlie puede ser a través de IPv6, si Bob y Charlie indican soporte con una capacidad 'B' en su dirección IPv6 publicada. Consulta la Propuesta 126 para más detalles.

Alice envía la solicitud a Bob usando una sesión existente sobre el transporte (IPv4 o IPv6) que desea probar. Cuando Bob recibe una solicitud de Alice vía IPv4, Bob debe seleccionar un Charlie que anuncie una dirección IPv4. Cuando Bob recibe una solicitud de Alice vía IPv6, Bob debe seleccionar un Charlie que anuncie una dirección IPv6. La comunicación real entre Bob-Charlie puede ser vía IPv4 o IPv6 (es decir, independiente del tipo de dirección de Alice).

- Los mensajes 1-4 deben estar contenidos en un mensaje Data en una sesión existente.

- Bob debe enviar el RI de Alice a Charlie antes de enviar el mensaje 2.

- Bob debe enviar el RI de Charlie a Alice antes de enviar el mensaje 4, si es aceptado (código de razón 0).

- Los mensajes 5-7 deben estar contenidos en un mensaje Peer Test fuera de sesión.

- Los mensajes 5 y 7 pueden contener los mismos datos firmados que se enviaron en los mensajes 3 y 4, o pueden regenerarse con una nueva marca de tiempo. La firma es opcional.

- El Mensaje 6 puede contener los mismos datos firmados enviados en los mensajes 1 y 2, o puede ser regenerado con una nueva marca de tiempo. La firma es opcional.

Firmas:

Alice firma la solicitud y la incluye en el mensaje 1; Bob la reenvía en el mensaje 2 a Charlie. Charlie firma la respuesta y la incluye en el mensaje 3; Bob la reenvía en el mensaje 4 a Alice. Algoritmo de firma: Firmar o verificar los siguientes datos con la clave de firma de Alice o Charlie:

- prólogo: 16 bytes "PeerTestValidate", sin terminación nula (no incluido en el mensaje)
- bhash: hash del router de Bob de 32 bytes (no incluido en el mensaje)
- ahash: hash del router de Alice de 32 bytes (Solo usado en la firma para los mensajes 3 y 4; no incluido en el mensaje 3 o 4)
- ver: 1 byte versión SSU
- nonce: 4 bytes nonce de prueba
- timestamp: 4 bytes marca de tiempo (segundos)
- asz: 1 byte tamaño del endpoint (puerto + IP) (6 o 18)
- AlicePort: 2 bytes número de puerto de Alice
- Alice IP: (asz - 2) bytes dirección IP de Alice

#### NextNonce

TODO solo si rotamos las claves

```
+----+----+----+----+----+----+----+----+
| 11 |  size   |      TBD               |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 11
size :: 2 bytes, big endian, size of data to follow
```
#### Confirmación

4 bytes de ack through, seguidos de un conteo de ack y cero o más rangos nack/ack.

Este diseño está adaptado y simplificado de QUIC. Los objetivos de diseño son los siguientes:

- Queremos codificar eficientemente un "bitfield", que es una secuencia de bits que representa paquetes confirmados.
- El bitfield está compuesto principalmente de 1's. Tanto los 1's como los 0's generalmente vienen en "grupos" secuenciales.
- La cantidad de espacio disponible en el paquete para las confirmaciones varía.
- El bit más importante es el de mayor número. Los de menor número son menos importantes. Por debajo de cierta distancia del bit más alto, los bits más antiguos serán "olvidados" y nunca se enviarán de nuevo.

La codificación especificada a continuación logra estos objetivos de diseño, enviando el número del bit más alto que está establecido en 1, junto con bits consecutivos adicionales menores que ese que también están establecidos en 1. Después de eso, si hay espacio, uno o más "rangos" especificando el número de bits consecutivos 0 y bits consecutivos 1 menores que ese. Consulte QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) sección 13.2.3 para más información de contexto.

```
+----+----+----+----+----+----+----+----+
| 12 |  size   |    Ack Through    |acnt|
+----+----+----+----+----+----+----+----+
|  range  |  range  |     .   .   .     |
+----+----+----+----+                   +
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 12
size :: 2 bytes, big endian, size of data to follow,
        5 minimum
ack through :: highest packet number acked
acnt :: number of acks lower than ack through also acked,
        0-255
range :: If present,
         1 byte nack count followed by 1 byte ack count,
         0-255 each
```
Ejemplos:

Queremos hacer ACK solo del paquete 10:

- Ack Through: 10
- acnt: 0
- no se incluyen rangos

Queremos hacer ACK solo de los paquetes 8-10:

- Ack Through: 10
- acnt: 2
- no se incluyen rangos

Queremos hacer ACK a 10 9 8 6 5 2 1 0, y NACK a 7 4 3. La codificación del Bloque ACK es:

- Ack Through: 10
- acnt: 2 (ack 9 8)
- range: 1 2 (nack 7, ack 6 5)
- range: 2 3 (nack 4 3, ack 2 1 0)

Notas:

- Los rangos pueden no estar presentes. El número máximo de rangos no está especificado, pueden ser tantos como quepan en el paquete.
- El nack de rango puede ser cero si se están confirmando más de 255 paquetes consecutivos.
- El ack de rango puede ser cero si se están rechazando más de 255 paquetes consecutivos.
- El nack de rango y el ack no pueden ser ambos cero.
- Después del último rango, los paquetes no son ni confirmados ni rechazados. La longitud del bloque ack y cómo se manejan los acks/nacks antiguos depende del remitente del bloque ack. Ver las secciones de ack a continuación para discusión.
- El ack through debería ser el número de paquete más alto recibido, y cualquier paquete más alto no ha sido recibido. Sin embargo, en situaciones limitadas, podría ser más bajo, como confirmar un solo paquete que "llena un hueco", o una implementación simplificada que no mantiene el estado de todos los paquetes recibidos. Por encima del más alto recibido, los paquetes no son ni confirmados ni rechazados, pero después de varios bloques ack, puede ser apropiado entrar en modo de retransmisión rápida.
- Este formato es una versión simplificada del de QUIC. Está diseñado para codificar eficientemente un gran número de ACKs, junto con ráfagas de NACKs.
- Los bloques ACK se usan para confirmar paquetes de la fase de datos. Solo deben incluirse para paquetes de la fase de datos dentro de la sesión.

#### Dirección

Puerto de 2 bytes y dirección IP de 4 o 16 bytes. La dirección de Alice, enviada a Alice por Bob, o la dirección de Bob, enviada a Bob por Alice.

```
+----+----+----+----+----+----+----+----+
| 13 | 6 or 18 |   Port  | IP Address    
+----+----+----+----+----+----+----+----+
     |
+----+

blk :: 13
size :: 2 bytes, big endian, 6 or 18
port :: 2 bytes, big endian
ip :: 4 byte IPv4 or 16 byte IPv6 address,
      big endian (network byte order)
```
#### Solicitud de Etiqueta de Retransmisión

Esto puede ser enviado por Alice en un mensaje Session Request, Session Confirmed, o Data. No está soportado en el mensaje Session Created, ya que Bob aún no tiene el RI de Alice, y no sabe si Alice soporta relay. Además, si Bob está recibiendo una conexión entrante, probablemente no necesita introducers (excepto quizás para el otro tipo ipv4/ipv6).

Cuando se envía en la Solicitud de Sesión, Bob puede responder con una Etiqueta de Relé en el mensaje de Sesión Creada, o puede elegir esperar hasta recibir la RouterInfo de Alice en la Confirmación de Sesión para validar la identidad de Alice antes de responder en un mensaje de Datos. Si Bob no desea actuar como relé para Alice, no envía un bloque de Etiqueta de Relé.

```
+----+----+----+
| 15 |    0    |
+----+----+----+

blk :: 15
size :: 2 bytes, big endian, value = 0
```
#### Relay Tag

Esto puede ser enviado por Bob en un mensaje Session Confirmed o Data, en respuesta a una Relay Tag Request de Alice.

Cuando se envía la Solicitud de Etiqueta de Retransmisión en la Solicitud de Sesión, Bob puede responder con una Etiqueta de Retransmisión en el mensaje de Sesión Creada, o puede elegir esperar hasta recibir el RouterInfo de Alice en la Confirmación de Sesión para validar la identidad de Alice antes de responder en un mensaje de Datos. Si Bob no desea retransmitir para Alice, no envía un bloque de Etiqueta de Retransmisión.

```
+----+----+----+----+----+----+----+
| 16 |    4    |    relay tag      |
+----+----+----+----+----+----+----+

blk :: 16
size :: 2 bytes, big endian, value = 4
relay tag :: 4 bytes, big endian, nonzero
```
#### Nuevo Token

Para una conexión posterior. Generalmente incluido en los mensajes Session Created y Session Confirmed. También puede enviarse nuevamente en el mensaje Data de una sesión de larga duración si el token anterior expira.

```
+----+----+----+----+----+----+----+----+
| 17 |   12    |     expires       |
+----+----+----+----+----+----+----+----+
                token              |
+----+----+----+----+----+----+----+

blk :: 17
size :: 2 bytes, big endian, value = 12
expires :: Unix timestamp, unsigned seconds.
           Wraps around in 2106
token :: 8 bytes, big endian
```
#### Desafío de Ruta

Un Ping con datos arbitrarios que se devuelven en una Respuesta de Ruta, utilizado como keep-alive o para validar un cambio de IP/Puerto.

```
+----+----+----+----+----+----+----+----+
| 18 |  size   |    Arbitrary Data      |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 18
size :: 2 bytes, big endian, size of data to follow
data :: Arbitrary data to be returned in a Path Response
        length as selected by sender
```
Notas:

- Se recomienda un tamaño mínimo de datos de 8 bytes, que contenga datos aleatorios, pero no es obligatorio.
- El tamaño máximo no está especificado, pero debería estar muy por debajo de 1280, porque el PMTU durante la fase de validación de ruta es 1280.
- No se recomiendan tamaños de desafío grandes porque podrían ser un vector para ataques de amplificación de paquetes.

#### Respuesta de Ruta

Un Pong con los datos recibidos en el Path Challenge, como respuesta al Path Challenge, utilizado como keep-alive o para validar un cambio de IP/Puerto.

```
+----+----+----+----+----+----+----+----+
| 19 |  size   |                        |
+----+----+----+                        +
|    Data received in Path Challenge    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 19
size :: 2 bytes, big endian, size of data to follow
data :: As received in a Path Challenge
```
#### Número del Primer Paquete

Opcionalmente incluido en el handshake en cada dirección, para especificar el primer número de paquete que será enviado. Esto proporciona más seguridad para el cifrado de encabezados, similar a TCP.

No completamente especificado, no soportado actualmente.

```
+----+----+----+----+----+----+----+
| 20 |  size   |  First pkt number |
+----+----+----+----+----+----+----+

blk :: 20
size :: 4
pkt num :: The first packet number to be sent in the data phase
```
#### Congestión

Este bloque está diseñado para ser un método extensible para intercambiar información de control de congestión. El control de congestión puede ser complejo y puede evolucionar a medida que obtengamos más experiencia con el protocolo en pruebas en vivo, o después del despliegue completo.

Esto mantiene cualquier información de congestión fuera de los bloques I2NP de alto uso, First Fragment, Followon Fragment y ACK, donde no hay espacio asignado para flags. Aunque hay tres bytes de flags no utilizados en la cabecera del paquete Data, eso también proporciona espacio limitado para extensibilidad y una protección de cifrado más débil.

Aunque es algo derrochador usar un bloque de 4 bytes para dos bits de información, al poner esto en un bloque separado, podemos extenderlo fácilmente con datos adicionales como tamaños de ventana actuales, RTT medido, u otras banderas. La experiencia ha demostrado que solo los bits de bandera suelen ser insuficientes e incómodos para la implementación de esquemas avanzados de control de congestión. Tratar de añadir soporte para cualquier característica posible de control de congestión en, por ejemplo, el bloque ACK, desperdiciaría espacio y añadiría complejidad al análisis de ese bloque.

Las implementaciones no deben asumir que el otro router admite ningún bit de bandera o característica particular incluida aquí, a menos que la implementación sea requerida por una versión futura de esta especificación.

Este bloque probablemente debería ser el último bloque sin relleno en la carga útil.

```
+----+----+----+----+
| 21 |  size   |flag|
+----+----+----+----+

blk :: 21
size :: 1 (or more if extended)
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 1 to request immediate ack
       bit 1: 1 for explicit congestion notification (ECN)
       bits 7-2: Unused, set to 0 for future compatibility
```
#### Relleno

Esto es para el relleno dentro de las cargas útiles AEAD. El relleno para todos los mensajes está dentro de las cargas útiles AEAD.

El padding debe adherirse aproximadamente a los parámetros negociados. Bob envió sus parámetros mínimos/máximos de tx/rx solicitados en Session Created. Alice envió sus parámetros mínimos/máximos de tx/rx solicitados en Session Confirmed. Las opciones actualizadas pueden enviarse durante la fase de datos. Ver la información del bloque de opciones anterior.

Si está presente, este debe ser el último bloque en la carga útil.

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
Notas:

- Se permite Size = 0.
- Estrategias de padding por determinar.
- Padding mínimo por determinar.
- Se permiten payloads que solo contengan padding.
- Valores predeterminados de padding por determinar.
- Ver bloque de opciones para la negociación de parámetros de padding
- Ver bloque de opciones para parámetros de padding mín/máx
- No exceder la MTU. Si es necesario más padding, enviar múltiples mensajes.
- La respuesta del router ante la violación del padding negociado depende de la implementación.
- La longitud del padding debe decidirse por mensaje basándose en estimaciones de la distribución de longitudes, o deben añadirse retrasos aleatorios. Estas contramedidas deben incluirse para resistir DPI, ya que de lo contrario los tamaños de mensaje revelarían que el protocolo de transporte está transportando tráfico I2P. El esquema exacto de padding es un área de trabajo futuro, el Apéndice A de [NTCP2](/docs/specs/ntcp2) proporciona más información sobre el tema.

## Prevención de Repetición

SSU2 está diseñado para minimizar el impacto de los mensajes reproducidos por un atacante.

Los mensajes de Token Request, Retry, Session Request, Session Created, Hole Punch, y Peer Test fuera de sesión deben contener bloques DateTime.

Tanto Alice como Bob validan que el tiempo de estos mensajes esté dentro de un sesgo válido (recomendado +/- 2 minutos). Para "resistencia a sondeo", Bob no debería responder a mensajes de Token Request o Session Request si el sesgo es inválido, ya que estos mensajes pueden ser un ataque de repetición o sondeo.

Bob puede optar por rechazar mensajes duplicados de Token Request y Retry, incluso si el sesgo es válido, mediante un filtro Bloom u otro mecanismo. Sin embargo, el tamaño y el costo de CPU para responder a estos mensajes es bajo. En el peor de los casos, un mensaje Token Request repetido puede invalidar un token enviado previamente.

El sistema de tokens minimiza enormemente el impacto de los mensajes Session Request reproducidos. Dado que los tokens solo pueden usarse una vez, un mensaje Session Request reproducido nunca tendrá un token válido. Bob puede elegir rechazar mensajes Session Request duplicados, incluso si el desvío es válido, mediante un filtro Bloom u otro mecanismo. Sin embargo, el tamaño y costo de CPU de responder con un mensaje Retry es bajo. En el peor de los casos, enviar un mensaje Retry puede invalidar un token enviado previamente.

Los mensajes duplicados de Session Created y Session Confirmed no se validarán porque el estado del handshake Noise no estará en el estado correcto para descifrarlos. En el peor de los casos, un peer puede retransmitir un Session Confirmed en respuesta a un aparente Session Created duplicado.

Los mensajes de Hole Punch y Peer Test repetidos deberían tener poco o ningún impacto.

Los routers deben usar el número de paquete del mensaje de datos para detectar y descartar mensajes de fase de datos duplicados. Cada número de paquete debe usarse solo una vez. Los mensajes repetidos deben ser ignorados.

## Retransmisión de Handshake

### Solicitud de Sesión

Si Alice no recibe ningún Session Created o Retry:

Mantener los mismos IDs de origen y conexión, clave efímera y número de paquete 0. O simplemente retener y retransmitir el mismo paquete cifrado. El número de paquete no debe incrementarse, porque eso cambiaría el valor de hash encadenado usado para cifrar el mensaje Session Created.

Intervalos de retransmisión recomendados: 1,25, 2,5 y 5 segundos (1,25, 3,75 y 8,75 segundos después del primer envío). Tiempo de espera recomendado: 15 segundos en total

### Sesión Creada

Si Bob no recibe ningún Session Confirmed:

Mantener los mismos IDs de origen y conexión, clave efímera y número de paquete 0. O simplemente conservar el paquete encriptado. El número de paquete no debe incrementarse, porque eso cambiaría el valor hash encadenado usado para encriptar el mensaje Session Confirmed.

Intervalos de retransmisión recomendados: 1, 2 y 4 segundos (1, 3 y 7 segundos después del primer envío). Tiempo de espera recomendado: 12 segundos en total

### Sesión Confirmada

En SSU 1, Alice no cambia a la fase de datos hasta que se recibe el primer paquete de datos de Bob. Esto hace que SSU 1 sea una configuración de dos viajes de ida y vuelta.

Para SSU 2, intervalos de retransmisión de Session Confirmed recomendados: 1.25, 2.5, y 5 segundos (1.25, 3.75, y 8.75 segundos después del primer envío).

Hay varias alternativas. Todas son 1 RTT:

1) Alice asume que Session Confirmed fue recibido, envía mensajes de datos inmediatamente, nunca retransmite Session Confirmed. Los paquetes de datos recibidos fuera de orden (antes de Session Confirmed) serán indescifrables, pero serán retransmitidos. Si Session Confirmed se pierde, todos los mensajes de datos enviados serán descartados. 2) Como en 1), enviar mensajes de datos inmediatamente, pero también retransmitir Session Confirmed hasta que se reciba un mensaje de datos. 3) Podríamos usar IK en lugar de XK, ya que tiene solo dos mensajes en el handshake, pero usa un DH adicional (4 en lugar de 3).

La implementación recomendada es la opción 2). Alice debe conservar la información requerida para retransmitir el mensaje Session Confirmed. Alice también debería retransmitir todos los mensajes Data después de que se retransmita el mensaje Session Confirmed.

Al retransmitir Session Confirmed, mantén los mismos IDs de origen y conexión, clave efímera y número de paquete 1. O simplemente conserva el paquete cifrado. El número de paquete no debe incrementarse, porque eso cambiaría el valor del hash encadenado que es una entrada para la función split().

Bob puede retener (encolar) los mensajes de datos recibidos antes del mensaje Session Confirmed. Ni las claves de protección de encabezado ni las claves de descifrado están disponibles antes de que se reciba el mensaje Session Confirmed, por lo que Bob no sabe que son mensajes de datos, pero eso se puede presumir. Después de que se recibe el mensaje Session Confirmed, Bob es capaz de descifrar y procesar los mensajes de datos encolados. Si esto es demasiado complejo, Bob puede simplemente descartar los mensajes de datos no descifrables, ya que Alice los retransmitirá.

Nota: Si se pierden los paquetes de sesión confirmada, Bob retransmitirá la sesión creada. El encabezado de sesión creada no será descifrable con la clave de introducción de Alice, ya que está configurado con la clave de introducción de Bob (a menos que se realice el descifrado de respaldo con la clave de introducción de Bob). Bob puede retransmitir inmediatamente los paquetes de sesión confirmada si no han sido previamente confirmados, y se recibe un paquete no descifrable.

### Solicitud de Token

Si Alice no recibe ningún Retry:

Mantener los mismos IDs de origen y conexión. Una implementación puede generar un nuevo número de paquete aleatorio y cifrar un nuevo paquete; o puede reutilizar el mismo número de paquete o simplemente retener y retransmitir el mismo paquete cifrado. El número de paquete no debe incrementarse, porque eso cambiaría el valor hash encadenado utilizado para cifrar el mensaje Session Created.

Intervalos de retransmisión recomendados: 3 y 6 segundos (3 y 9 segundos después del primer envío). Tiempo de espera recomendado: 15 segundos en total

### Reintentar

Si Bob no recibe ningún Session Confirmed:

Un mensaje Retry no se retransmite al agotarse el tiempo de espera, para reducir los impactos de las direcciones de origen falsificadas.

Sin embargo, un mensaje Retry puede ser retransmitido en respuesta a un mensaje Session Request repetido que se reciba con el token original (inválido), o en respuesta a un mensaje Token Request repetido. En cualquier caso, esto indica que el mensaje Retry se perdió.

Si se recibe un segundo mensaje Session Request con un token diferente pero aún inválido, descartar la sesión pendiente y no responder.

Si se reenvía el mensaje Retry: Mantener los mismos IDs de origen y conexión y token. Una implementación puede generar un nuevo número de paquete aleatorio y cifrar un nuevo paquete; O puede reutilizar el mismo número de paquete o simplemente conservar y retransmitir el mismo paquete cifrado.

### Tiempo de Espera Total

El tiempo de espera total recomendado para el handshake es de 20 segundos.

### Duplicados y Manejo de Errores

Los duplicados de los tres mensajes de handshake de Noise Session Request, Session Created y Session Confirmed deben detectarse antes del MixHash() del encabezado. Aunque el procesamiento AEAD de Noise presumiblemente fallará después de eso, el hash del handshake ya estaría corrupto.

Si cualquiera de los tres mensajes se corrompe y falla AEAD, el handshake no puede recuperarse posteriormente incluso con retransmisión, porque MixHash() ya fue llamado en el mensaje corrupto.

## Tokens

El Token en el encabezado de Session Request se utiliza para mitigar DoS, prevenir la suplantación de direcciones de origen y como resistencia a ataques de repetición.

Si Bob no acepta el token en el mensaje Session Request, Bob NO descifra el mensaje, ya que requiere una operación DH costosa. Bob simplemente envía un mensaje Retry con un nuevo token.

Si posteriormente se recibe un mensaje Session Request con ese token, Bob procede a descifrar ese mensaje y continúa con el handshake.

El token debe ser un valor de 8 bytes generado aleatoriamente, si el generador del token almacena los valores y la IP y puerto asociados (en memoria o de forma persistente). El generador no puede generar un valor opaco, por ejemplo, usando el SipHash (con una semilla secreta K0, K1) de la IP, puerto y hora o día actual, para crear tokens que no necesiten guardarse en memoria, porque este método hace difícil rechazar tokens reutilizados y ataques de repetición. Sin embargo, es un tema para estudio posterior si podemos migrar a tal esquema, como hace [WireGuard](https://www.wireguard.com/papers/wireguard.pdf), usando un HMAC de 16 bytes de un secreto del servidor y dirección IP.

Los tokens solo pueden utilizarse una vez. Un token enviado de Bob a Alice en un mensaje Retry debe usarse inmediatamente y expira en unos segundos. Un token enviado en un bloque New Token en una sesión establecida puede utilizarse en una conexión posterior, y expira en el momento especificado en ese bloque. La expiración es especificada por el remitente; los valores recomendados son varios minutos como mínimo, una o más horas como máximo, dependiendo de la sobrecarga máxima deseada de tokens almacenados.

Si la IP o el puerto de un router cambia, debe eliminar todos los tokens guardados (tanto de entrada como de salida) para la IP o puerto anterior, ya que ya no son válidos. Los tokens pueden persistir opcionalmente a través de reinicios del router, dependiendo de la implementación. No se garantiza la aceptación de un token no expirado; si Bob ha olvidado o eliminado sus tokens guardados, enviará un Retry a Alice. Un router puede optar por limitar el almacenamiento de tokens, y eliminar los tokens almacenados más antiguos incluso si no han expirado.

Los bloques New Token pueden enviarse de Alice a Bob o de Bob a Alice. Típicamente se enviarían al menos una vez, durante o poco después del establecimiento de la sesión. Debido a las verificaciones de validación del RouterInfo en el mensaje Session Confirmed, Bob no debería enviar un bloque New Token en el mensaje Session Created, puede enviarse con el ACK 0 y Router Info después de que se reciba y valide el Session Confirmed.

Como las duraciones de sesión suelen ser más largas que la expiración del token, el token debe ser reenviado antes o después de la expiración con un nuevo tiempo de expiración, o se debe enviar un nuevo token. Los routers deben asumir que solo el último token recibido es válido; no hay requisito de almacenar múltiples tokens entrantes o salientes para la misma IP/puerto.

Un token está vinculado a la combinación de IP/puerto de origen e IP/puerto de destino. Un token recibido en IPv4 no puede usarse para IPv6 o viceversa.

Si cualquiera de los peers migra a una nueva IP o puerto durante la sesión (consulte la sección de Migración de Conexión), todos los tokens intercambiados previamente se invalidan y se deben intercambiar nuevos tokens.

Las implementaciones pueden, pero no están obligadas a, guardar tokens en disco y recargarlos al reiniciar. Si se persisten, la implementación debe asegurar que la IP y el puerto no hayan cambiado desde el apagado antes de recargarlos.

## Fragmentación de Mensajes I2NP

Diferencias con SSU 1

Nota: Como en SSU 1, el fragmento inicial no contiene información sobre el número total de fragmentos o la longitud total. Los fragmentos posteriores no contienen información sobre su desplazamiento. Esto proporciona al emisor la flexibilidad de fragmentar "sobre la marcha" basándose en el espacio disponible en el paquete. (Java I2P no hace esto; "pre-fragmenta" antes de que se envíe el primer fragmento) Sin embargo, esto carga al receptor con almacenar fragmentos recibidos fuera de orden y retrasar el reensamblaje hasta que se reciban todos los fragmentos.

Como en SSU 1, cualquier retransmisión de fragmentos debe preservar la longitud (y el offset implícito) de la transmisión previa del fragmento.

SSU 2 sí separa los tres casos (mensaje completo, fragmento inicial y fragmento de seguimiento) en tres tipos de bloques diferentes, para mejorar la eficiencia de procesamiento.

## Duplicación de Mensajes I2NP

Este protocolo NO previene completamente la entrega duplicada de mensajes I2NP. Los duplicados a nivel IP o los ataques de repetición serán detectados en la capa SSU2, porque cada número de paquete solo puede usarse una vez.

Cuando los mensajes o fragmentos I2NP se retransmiten en nuevos paquetes, sin embargo, esto no es detectable en la capa SSU2. El router debería hacer cumplir la expiración I2NP (tanto demasiado antigua como demasiado lejana en el futuro) y usar un filtro Bloom u otro mecanismo basado en el ID del mensaje I2NP.

El router, o en la implementación de SSU2, puede usar mecanismos adicionales para detectar duplicados. Por ejemplo, SSU2 podría mantener una caché de IDs de mensajes recibidos recientemente. Esto depende de la implementación.

## Control de Congestión

Esta especificación define el protocolo para la numeración de paquetes y bloques ACK. Esto proporciona información en tiempo real suficiente para que un transmisor implemente un algoritmo de control de congestión eficiente y receptivo, mientras permite flexibilidad e innovación en esa implementación. Esta sección discute los objetivos de implementación y proporciona sugerencias. Se puede encontrar orientación general en [RFC-9002](https://tools.ietf.org/html/rfc9002). Ver también [RFC-6298](https://tools.ietf.org/html/rfc6298) para orientación sobre temporizadores de retransmisión.

Los paquetes de datos de solo ACK no deberían contar para los bytes o paquetes en vuelo y no están controlados por congestión. A diferencia de TCP, SSU2 puede detectar la pérdida de estos paquetes y esa información puede usarse para ajustar el estado de congestión. Sin embargo, este documento no especifica un mecanismo para hacerlo.

Los paquetes que contengan algunos otros bloques que no sean de datos también pueden ser excluidos del control de congestión si se desea, dependiendo de la implementación. Por ejemplo:

- Prueba de Par
- Solicitud/introducción/respuesta de retransmisión
- Desafío/respuesta de ruta

Se recomienda que el control de congestión se base en el recuento de bytes, no en el recuento de paquetes, siguiendo la orientación en los RFCs de TCP y QUIC [RFC-9002](https://tools.ietf.org/html/rfc9002). Un límite adicional de recuento de paquetes también puede ser útil para prevenir el desbordamiento del búfer en el kernel o en middleboxes, dependiendo de la implementación, aunque esto puede agregar una complejidad significativa. Si la salida de paquetes por sesión y/o total está limitada por ancho de banda y/o regulada, esto puede mitigar la necesidad de limitar el recuento de paquetes.

### Números de Paquete

En SSU 1, los ACK y NACK contenían números de mensaje I2NP y máscaras de bits de fragmentos. Los transmisores rastreaban el estado de ACK de los mensajes salientes (y sus fragmentos) y retransmitían fragmentos según fuera necesario.

En SSU 2, los ACKs y NACKs contienen números de paquete. Los transmisores deben mantener una estructura de datos con un mapeo de números de paquete a sus contenidos. Cuando un paquete recibe un ACK o NACK, el transmisor debe determinar qué mensajes I2NP y fragmentos estaban en ese paquete, para decidir qué retransmitir.

### ACK de Sesión Confirmada

Bob envía un ACK del paquete 0, que confirma el mensaje Session Confirmed y permite a Alice proceder a la fase de datos, y descartar el mensaje Session Confirmed grande que se estaba guardando para una posible retransmisión. Esto reemplaza el DeliveryStatusMessage enviado por Bob en SSU 1.

Bob debería enviar un ACK tan pronto como sea posible después de recibir el mensaje Session Confirmed. Un pequeño retraso (no más de 50 ms) es aceptable, ya que al menos un mensaje Data debería llegar casi inmediatamente después del mensaje Session Confirmed, de modo que el ACK pueda confirmar tanto el Session Confirmed como el mensaje Data. Esto evitará que Bob tenga que retransmitir el mensaje Session Confirmed.

### Generando ACKs

Definición: Paquetes que provocan ACK: Los paquetes que contienen bloques que provocan ack obtienen un ACK del receptor dentro del retraso máximo de reconocimiento y se denominan paquetes que provocan ack.

Los routers confirman todos los paquetes que reciben y procesan. Sin embargo, solo los paquetes que provocan confirmación hacen que se envíe un bloque ACK dentro del retraso máximo de confirmación. Los paquetes que no provocan confirmación solo se confirman cuando se envía un bloque ACK por otras razones.

Al enviar un paquete por cualquier motivo, un endpoint debería intentar incluir un bloque ACK si no se ha enviado uno recientemente. Hacer esto ayuda con la detección oportuna de pérdidas en el peer.

En general, la retroalimentación frecuente de un receptor mejora la respuesta a pérdidas y congestión, pero esto debe equilibrarse contra la carga excesiva generada por un receptor que envía un bloque ACK en respuesta a cada paquete que solicita confirmación. La orientación que se ofrece a continuación busca lograr este equilibrio.

Los paquetes de datos dentro de la sesión que contengan cualquier bloque EXCEPTO los siguientes provocan confirmación de recepción (ack):

- Bloque ACK
- Bloque de dirección
- Bloque DateTime
- Bloque de relleno
- Bloque de terminación
- ¿Otros?

Los paquetes fuera de sesión, incluyendo mensajes de handshake y mensajes de peer test 5-7, tienen sus propios mecanismos de reconocimiento. Ver más abajo.

### ACKs de handshake

Estos son casos especiales:

- La Solicitud de Token se confirma implícitamente por Retry
- La Solicitud de Sesión se confirma implícitamente por Session Created o Retry
- Retry se confirma implícitamente por Session Request
- Session Created se confirma implícitamente por Session Confirmed
- Session Confirmed debe confirmarse inmediatamente

### Enviando Bloques ACK

Los bloques ACK se utilizan para confirmar la recepción de paquetes de la fase de datos. Solo deben incluirse para paquetes de la fase de datos dentro de la sesión.

Cada paquete debe ser confirmado al menos una vez, y los paquetes que requieren confirmación deben ser confirmados al menos una vez dentro de un retraso máximo.

Un endpoint debe confirmar inmediatamente todos los paquetes de handshake que requieren confirmación dentro de su retraso máximo, con la siguiente excepción. Antes de la confirmación del handshake, un endpoint podría no tener las claves de cifrado de encabezados de paquete para descifrar los paquetes cuando se reciben. Por lo tanto, podría almacenarlos en buffer y confirmarlos cuando las claves necesarias estén disponibles.

Dado que los paquetes que contienen solo bloques ACK no están controlados por congestión, un endpoint no debe enviar más de un paquete de este tipo en respuesta a recibir un paquete que solicite confirmación.

Un endpoint no debe enviar un paquete que no requiera confirmación en respuesta a un paquete que no requiera confirmación, incluso si hay espacios de paquetes que preceden al paquete recibido. Esto evita un bucle infinito de confirmaciones, que podría impedir que la conexión llegue a estar inactiva. Los paquetes que no requieren confirmación finalmente son confirmados cuando el endpoint envía un bloque ACK en respuesta a otros eventos.

Un endpoint que solo esté enviando bloques ACK no recibirá acknowledgments de su peer a menos que esos acknowledgments estén incluidos en paquetes con bloques que requieren confirmación (ack-eliciting). Un endpoint debería enviar un bloque ACK con otros bloques cuando haya nuevos paquetes que requieren confirmación para reconocer. Cuando solo necesiten ser reconocidos paquetes que no requieren confirmación (non-ack-eliciting), un endpoint PUEDE elegir no enviar un bloque ACK con bloques salientes hasta que se haya recibido un paquete que requiere confirmación.

Un endpoint que solo está enviando paquetes que no requieren confirmación podría elegir agregar ocasionalmente un bloque que requiera confirmación a esos paquetes para asegurar que recibe una confirmación. En ese caso, un endpoint NO DEBE enviar un bloque que requiera confirmación en todos los paquetes que de otra manera no requerirían confirmación, para evitar un bucle infinito de retroalimentación de confirmaciones.

Para ayudar en la detección de pérdidas en el remitente, un endpoint debería generar y enviar un bloque ACK sin demora cuando recibe un paquete que requiere confirmación en cualquiera de estos casos:

- Cuando el paquete recibido tiene un número de paquete menor que otro paquete que provoca acknowledgment que ha sido recibido
- Cuando el paquete tiene un número de paquete mayor que el paquete que provoca acknowledgment con el número más alto que ha sido recibido y hay paquetes perdidos entre ese paquete y este paquete.
- Cuando la bandera ack-immediate en el encabezado del paquete está establecida

Se espera que los algoritmos sean resistentes a receptores que no sigan las orientaciones ofrecidas anteriormente. Sin embargo, una implementación solo debe desviarse de estos requisitos después de una consideración cuidadosa de las implicaciones de rendimiento de un cambio, tanto para las conexiones realizadas por el punto final como para otros usuarios de la red.

### Frecuencia de ACK

Un receptor determina con qué frecuencia enviar confirmaciones en respuesta a paquetes que requieren confirmación. Esta determinación implica un equilibrio.

Los endpoints dependen de confirmaciones oportunas para detectar pérdidas. Los controladores de congestión basados en ventana dependen de las confirmaciones para gestionar su ventana de congestión. En ambos casos, retrasar las confirmaciones puede afectar negativamente el rendimiento.

Por otro lado, reducir la frecuencia de paquetes que solo llevan confirmaciones reduce el costo de transmisión y procesamiento de paquetes en ambos extremos. Puede mejorar el rendimiento de la conexión en enlaces severamente asimétricos y reducir el volumen de tráfico de confirmación utilizando la capacidad de la ruta de retorno; consulte la Sección 3 de [RFC-3449](https://tools.ietf.org/html/rfc3449).

Un receptor debería enviar un bloque ACK después de recibir al menos dos paquetes que requieren confirmación. Esta recomendación es de naturaleza general y es consistente con las recomendaciones para el comportamiento de endpoints TCP [RFC-5681](https://tools.ietf.org/html/rfc5681). El conocimiento de las condiciones de la red, el conocimiento del controlador de congestión del par, o investigación y experimentación adicional podrían sugerir estrategias de confirmación alternativas con mejores características de rendimiento.

Un receptor puede procesar múltiples paquetes disponibles antes de determinar si enviar un bloque ACK en respuesta. En general, el receptor no debería retrasar un ACK por más de RTT / 6, o 150 ms como máximo.

La bandera ack-immediate en la cabecera del paquete de datos es una solicitud para que el receptor envíe un ack poco después de la recepción, probablemente dentro de unos pocos ms. En general, el receptor no debería retrasar un ACK inmediato por más de RTT / 16, o 5 ms como máximo.

### Bandera de ACK Inmediato

El receptor no conoce el tamaño de la ventana de envío del remitente, por lo que no sabe cuánto tiempo debe esperar antes de enviar un ACK. La bandera de ACK inmediato en el encabezado del paquete de datos es una forma importante de mantener el rendimiento máximo minimizando el RTT efectivo. La bandera de ACK inmediato está en el byte 13 del encabezado, bit 0, es decir (header[13] & 0x01). Cuando está activada, se solicita un ACK inmediato. Consulta la sección de encabezado corto anterior para más detalles.

Existen varias estrategias posibles que un remitente puede usar para determinar cuándo establecer la bandera de immediate-ack:

- Establecido una vez cada N paquetes, para algún N pequeño
- Establecido en el último de una ráfaga de paquetes
- Establecido cuando la ventana de envío está casi llena, por ejemplo más de 2/3 llena
- Establecido en todos los paquetes con fragmentos retransmitidos

Las banderas de ACK inmediato solo deberían ser necesarias en paquetes de datos que contengan mensajes I2NP o fragmentos de mensajes.

### Tamaño del Bloque ACK

Cuando se envía un bloque ACK, se incluyen uno o más rangos de paquetes confirmados. Incluir confirmaciones para paquetes más antiguos reduce la probabilidad de retransmisiones falsas causadas por la pérdida de bloques ACK enviados previamente, a costa de bloques ACK más grandes.

Los bloques ACK siempre deben confirmar los paquetes recibidos más recientemente, y cuanto más desordenados estén los paquetes, más importante es enviar un bloque ACK actualizado rápidamente, para evitar que el par declare un paquete como perdido y retransmita erróneamente los bloques que contiene. Un bloque ACK debe caber dentro de un solo paquete. Si no es así, entonces se omiten los rangos más antiguos (aquellos con los números de paquete más pequeños).

Un receptor limita el número de rangos ACK que recuerda y envía en bloques ACK, tanto para limitar el tamaño de los bloques ACK como para evitar el agotamiento de recursos. Después de recibir confirmaciones para un bloque ACK, el receptor debería dejar de rastrear esos rangos ACK confirmados. Los emisores pueden esperar confirmaciones para la mayoría de los paquetes, pero este protocolo no garantiza la recepción de una confirmación para cada paquete que el receptor procesa.

Es posible que mantener muchos rangos ACK pueda causar que un bloque ACK se vuelva demasiado grande. Un receptor puede descartar rangos ACK no reconocidos para limitar el tamaño del bloque ACK, a costa de incrementar las retransmisiones del remitente. Esto es necesario si un bloque ACK sería demasiado grande para caber en un paquete. Los receptores también pueden limitar más el tamaño del bloque ACK para preservar espacio para otros bloques o para limitar el ancho de banda que consumen los reconocimientos.

Un receptor debe retener un rango de ACK a menos que pueda asegurar que no aceptará posteriormente paquetes con números en ese rango. Mantener un número mínimo de paquete que aumenta a medida que se descartan rangos es una forma de lograr esto con un estado mínimo.

Los receptores pueden descartar todos los rangos ACK, pero deben conservar el número de paquete más grande que haya sido procesado exitosamente, ya que se utiliza para recuperar números de paquete de paquetes posteriores.

La siguiente sección describe un enfoque ejemplar para determinar qué paquetes reconocer en cada bloque ACK. Aunque el objetivo de este algoritmo es generar un reconocimiento para cada paquete que se procesa, aún es posible que los reconocimientos se pierdan.

### Limitando Rangos mediante el Seguimiento de Bloques ACK

Cuando se envía un paquete que contiene un bloque ACK, el campo Ack Through en ese bloque puede guardarse. Cuando se reconoce un paquete que contiene un bloque ACK, el receptor puede dejar de reconocer paquetes menores o iguales al campo Ack Through en el bloque ACK enviado.

Un receptor que envía solo paquetes que no requieren confirmación de recibo, como bloques ACK, podría no recibir una confirmación durante un largo período de tiempo. Esto podría hacer que el receptor mantenga el estado para una gran cantidad de bloques ACK durante un período prolongado, y los bloques ACK que envía podrían ser innecesariamente grandes. En tal caso, un receptor podría enviar ocasionalmente un PING u otro bloque pequeño que requiera confirmación, como una vez por viaje de ida y vuelta, para solicitar un ACK del par.

En casos sin pérdida de bloques ACK, este algoritmo permite un mínimo de 1 RTT de reordenamiento. En casos con pérdida de bloques ACK y reordenamiento, este enfoque no garantiza que cada reconocimiento sea visto por el emisor antes de que ya no esté incluido en el bloque ACK. Los paquetes podrían recibirse fuera de orden, y todos los bloques ACK posteriores que los contengan podrían perderse. En este caso, el algoritmo de recuperación de pérdidas podría causar retransmisiones espurias, pero el emisor continuará progresando.

### Congestión

Los transportes I2P no garantizan la entrega en orden de los mensajes I2NP. Por lo tanto, la pérdida de un mensaje de datos que contenga uno o más mensajes I2NP o fragmentos NO impide que se entreguen otros mensajes I2NP; no hay bloqueo de cabecera de línea. Las implementaciones deben continuar enviando mensajes nuevos durante la fase de recuperación de pérdidas si la ventana de envío lo permite.

### Retransmisión

Un remitente no debe retener el contenido completo de un mensaje para retransmitirlo de forma idéntica (excepto para mensajes de handshake, ver arriba). Un remitente debe ensamblar mensajes que contengan información actualizada (ACKs, NACKs y datos no confirmados) cada vez que envía un mensaje. Un remitente debe evitar retransmitir información de mensajes una vez que son confirmados. Esto incluye mensajes que son confirmados después de ser declarados perdidos, lo cual puede ocurrir en presencia de reordenamiento de red.

### Ventana

Por determinar. Se puede encontrar orientación general en [RFC-9002](https://tools.ietf.org/html/rfc9002).

## Migración de Conexión

La IP o el puerto de un peer puede cambiar durante el tiempo de vida de una sesión. Un cambio de IP puede ser causado por la rotación de direcciones temporales IPv6, cambios periódicos de IP impulsados por el ISP, un cliente móvil que transiciona entre IPs de WiFi y celular, u otros cambios de red locales. Un cambio de puerto puede ser causado por un reenlace NAT después de que el enlace anterior haya expirado.

La IP o puerto de un peer puede parecer cambiar debido a varios ataques dentro y fuera de la ruta, incluyendo modificar o inyectar paquetes.

La migración de conexión es el proceso mediante el cual se valida un nuevo endpoint de origen (IP+puerto), mientras se previenen cambios que no están validados. Este proceso es una versión simplificada de la definida en QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000). Este proceso se define únicamente para la fase de datos de una sesión. La migración no está permitida durante el handshake. Todos los paquetes de handshake deben ser verificados para confirmar que provienen de la misma IP y puerto que los paquetes enviados y recibidos anteriormente. En otras palabras, la IP y puerto de un peer deben ser constantes durante el handshake.

### Modelo de Amenazas

(Adaptado de QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000))

#### Suplantación de Dirección de Peer

Un peer puede falsificar su dirección de origen para hacer que un endpoint envíe cantidades excesivas de datos a un host no dispuesto. Si el endpoint envía significativamente más datos que el peer que está falsificando, la migración de conexión podría usarse para amplificar el volumen de datos que un atacante puede generar hacia una víctima.

#### Suplantación de Direcciones en la Ruta

Un atacante en el camino podría causar una migración de conexión espuria copiando y reenviando un paquete con una dirección falsificada de tal manera que llegue antes que el paquete original. El paquete con la dirección falsificada será visto como proveniente de una conexión que está migrando, y el paquete original será visto como un duplicado y descartado. Después de una migración espuria, la validación de la dirección de origen fallará porque la entidad en la dirección de origen no tiene las claves criptográficas necesarias para leer o responder al Path Challenge que se le envía, incluso si quisiera hacerlo.

#### Reenvío de Paquetes Fuera de Ruta

Un atacante fuera de la ruta que pueda observar paquetes podría reenviar copias de paquetes genuinos a los endpoints. Si el paquete copiado llega antes que el paquete genuino, esto aparecerá como un reenlace NAT. Cualquier paquete genuino será descartado como duplicado. Si el atacante puede continuar reenviando paquetes, podría ser capaz de causar migración a una ruta a través del atacante. Esto coloca al atacante en la ruta, otorgándole la capacidad de observar o descartar todos los paquetes subsecuentes.

#### Implicaciones de Privacidad

QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) especifica cambiar los IDs de conexión al cambiar las rutas de red. Usar un ID de conexión estable en múltiples rutas de red permitiría a un observador pasivo correlacionar la actividad entre esas rutas. Un endpoint que se mueve entre redes podría no desear que su actividad sea correlacionada por ninguna entidad que no sea su par. Sin embargo, QUIC no cifra los IDs de conexión en el encabezado. SSU2 sí lo hace, por lo que la fuga de privacidad requeriría que el observador pasivo también tuviera acceso a la netDb para obtener la clave de introducción necesaria para descifrar el ID de conexión. Incluso con la clave de introducción, esto no es un ataque fuerte, y no cambiamos los IDs de conexión después de la migración en SSU2, ya que esto sería una complicación significativa.

### Iniciando Validación de Ruta

Durante la fase de datos, los peers deben verificar que la IP de origen y el puerto de cada paquete de datos recibido. Si la IP o el puerto es diferente a los recibidos previamente, Y el paquete no es un número de paquete duplicado, Y el paquete se descifra exitosamente, la sesión entra en la fase de validación de ruta.

Además, un peer debe verificar que la nueva IP y puerto sean válidos según las reglas de validación locales (no bloqueados, no puertos ilegales, etc.). Los peers NO están obligados a soportar migración entre IPv4 e IPv6, y pueden tratar una nueva IP en la otra familia de direcciones como inválida, ya que este no es un comportamiento esperado y puede añadir complejidad significativa de implementación. Al recibir un paquete desde una IP/puerto inválido, una implementación puede simplemente descartarlo, o puede iniciar una validación de ruta con la IP/puerto anterior.

Al entrar en la fase de validación de ruta, siga los siguientes pasos:

- Iniciar un temporizador de tiempo de espera de validación de ruta de varios segundos, o varias veces el RTO actual (por determinar)
- Reducir la ventana de congestión al mínimo
- Reducir el PMTU al mínimo (1280)
- Enviar un paquete de datos que contenga un bloque Path Challenge, un bloque Address (que contenga la nueva IP/puerto), y, típicamente, un bloque ACK, a la nueva IP y puerto. Este paquete utiliza el mismo ID de conexión y claves de cifrado que la sesión actual. Los datos del bloque Path Challenge deben contener suficiente entropía (al menos 8 bytes) para que no puedan ser falsificados.
- Opcionalmente, también enviar un Path Challenge a la antigua IP/puerto, con datos de bloque diferentes. Ver más abajo.
- Iniciar un temporizador de tiempo de espera de Path Response basado en el RTO actual (típicamente RTT + un múltiplo de RTTdev)

Mientras esté en la fase de validación de ruta, la sesión puede continuar procesando paquetes entrantes. Ya sea desde la IP/puerto antigua o nueva. La sesión también puede continuar enviando y confirmando paquetes de datos. Sin embargo, la ventana de congestión y PMTU deben permanecer en los valores mínimos durante la fase de validación de ruta, para evitar ser utilizadas en ataques de denegación de servicio mediante el envío de grandes cantidades de tráfico a una dirección falsificada.

Una implementación puede, pero no está obligada a, intentar validar múltiples rutas simultáneamente. Esto probablemente no vale la pena por la complejidad. Puede, pero no está obligada a, recordar una IP/puerto anterior como ya validada, y omitir la validación de ruta si un peer regresa a su IP/puerto anterior.

Si se recibe una Path Response, que contenga los datos idénticos enviados en el Path Challenge, la validación de ruta ha sido exitosa. La IP/puerto de origen del mensaje Path Response no tiene que ser la misma a la que se envió el Path Challenge.

Si no se recibe una Path Response antes de que expire el temporizador de Path Response, envía otro Path Challenge y duplica el temporizador de Path Response.

Si no se recibe una Path Response antes de que expire el temporizador de Path Validation, la Path Validation ha fallado.

### Contenido del Mensaje

Los mensajes Data deben contener los siguientes bloques. El orden no está especificado excepto que Padding debe ser el último:

- Bloque Path Challenge o Path Response. Path Challenge contiene datos opacos, se recomiendan 8 bytes mínimo. Path Response contiene los datos del Path Challenge.
- Bloque de dirección que contiene la IP aparente del destinatario
- Bloque DateTime
- Bloque ACK
- Bloque de relleno

No se recomienda incluir ningún otro bloque (por ejemplo, I2NP) en el mensaje.

Se permite incluir un bloque Path Challenge en el mensaje que contiene la Path Response, para iniciar una validación en la otra dirección.

Los bloques Path Challenge y Path Response provocan ACK. El Path Challenge será confirmado con ACK por un mensaje de datos que contenga los bloques Path Response y ACK. El Path Response debería ser confirmado con ACK por un mensaje de datos que contenga un bloque ACK.

### Enrutamiento durante la Validación de Ruta

La especificación QUIC no es clara sobre dónde enviar los paquetes de datos durante la validación de ruta - ¿a la IP/puerto antigua o nueva? Hay un equilibrio que debe lograrse entre responder rápidamente a los cambios de IP/puerto, y no enviar tráfico a direcciones falsificadas. Además, los paquetes falsificados no deben poder impactar sustancialmente una sesión existente. Los cambios solo de puerto probablemente sean causados por reenlace de NAT después de un período de inactividad; los cambios de IP podrían ocurrir durante fases de tráfico alto en una o ambas direcciones.

Las estrategias están sujetas a investigación y refinamiento. Las posibilidades incluyen:

- No enviar paquetes de datos a la nueva IP/puerto hasta que sea validada
- Continuar enviando paquetes de datos a la antigua IP/puerto hasta que la nueva IP/puerto sea validada
- Revalidar simultáneamente la antigua IP/puerto
- No enviar ningún dato hasta que la antigua o la nueva IP/puerto sea validada
- Estrategias diferentes para cambio solo de puerto que para cambio de IP
- Estrategias diferentes para un cambio IPv6 en la misma /32, probablemente causado por rotación de dirección temporal

### Respondiendo al Desafío de Ruta

Al recibir un Path Challenge, el peer debe responder con un paquete de datos que contenga un Path Response, con los datos del Path Challenge.

La Respuesta de Ruta debe enviarse a la IP/puerto desde el cual se recibió el Desafío de Ruta. Esto NO ES NECESARIAMENTE la IP/puerto que se estableció previamente para el peer. Esto asegura que la validación de ruta por un peer solo tenga éxito si la ruta es funcional en ambas direcciones. Ver la sección Validación después de Cambio Local más abajo.

A menos que la IP/puerto sea diferente de la IP/puerto previamente conocida para el peer, trata un Path Challenge como un simple ping, y simplemente responde incondicionalmente con un Path Response. El receptor no mantiene ni cambia ningún estado basado en un Path Challenge recibido. Si la IP/puerto es diferente, un peer debe verificar que la nueva IP y puerto son válidos según las reglas de validación locales (no bloqueados, no puertos ilegales, etc.). Los peers NO están obligados a soportar respuestas entre familias de direcciones diferentes entre IPv4 e IPv6, y pueden tratar una nueva IP en la otra familia de direcciones como inválida, ya que este no es un comportamiento esperado.

A menos que esté restringido por el control de congestión, la Respuesta de Ruta debe enviarse inmediatamente. Las implementaciones deben tomar medidas para limitar la velocidad de las Respuestas de Ruta o el ancho de banda utilizado si es necesario.

Un bloque Path Challenge generalmente va acompañado de un bloque Address en el mismo mensaje. Si el bloque de dirección contiene una nueva IP/puerto, un peer puede validar esa IP/puerto e iniciar pruebas de peer de esa nueva IP/puerto, con el peer de la sesión o cualquier otro peer. Si el peer cree que está detrás de un firewall, y solo cambió el puerto, este cambio probablemente se debe a reenlace NAT, y probablemente no se requieren más pruebas de peer.

### Validación de Ruta Exitosa

Al validar exitosamente la ruta, la conexión se migra completamente a la nueva IP/puerto. En caso de éxito:

- Salir de la fase de validación de ruta
- Todos los paquetes se envían a la nueva IP y puerto.
- Se eliminan las restricciones en la ventana de congestión y PMTU, y se les permite aumentar. No simplemente restaurarlas a los valores anteriores, ya que la nueva ruta puede tener características diferentes.
- Si la IP cambió, establecer el RTT calculado y RTO a valores iniciales. Debido a que los cambios solo de puerto son comúnmente el resultado de reenlace NAT u otra actividad de middlebox, el peer puede en su lugar retener su estado de control de congestión y estimación de tiempo de ida y vuelta en esos casos en lugar de revertir a valores iniciales.
- Eliminar (invalidar) cualquier token enviado o recibido para la IP/puerto antigua (opcional)
- Enviar un nuevo bloque de token para la nueva IP/puerto (opcional)

### Cancelando la Validación de Ruta

Durante la fase de validación de ruta, cualquier paquete válido y no duplicado que se reciba desde la IP/puerto anterior y que se descifre exitosamente causará que la Validación de Ruta sea cancelada. Es importante que una validación de ruta cancelada, causada por un paquete falsificado, no cause que una sesión válida sea terminada o significativamente interrumpida.

En validación de ruta cancelada:

- Salir de la fase de validación de ruta
- Todos los paquetes se envían a la IP y puerto antiguos.
- Se eliminan las restricciones en la ventana de congestión y PMTU, y se les permite aumentar, o, opcionalmente, restaurar los valores anteriores
- Retransmitir cualquier paquete de datos que fue enviado previamente a la nueva IP/puerto a la antigua IP/puerto.

### Validación de Ruta Fallida

Es importante que una validación de ruta fallida, causada por un paquete falsificado, no provoque que una sesión válida sea terminada o significativamente interrumpida.

En validación de ruta fallida:

- Salir de la fase de validación de ruta
- Todos los paquetes se envían a la IP y puerto antiguos.
- Se eliminan las restricciones en la ventana de congestión y PMTU, y se les permite aumentar.
- Opcionalmente, iniciar una validación de ruta en la IP y puerto antiguos. Si falla, terminar la sesión.
- De lo contrario, seguir las reglas estándar de tiempo de espera y terminación de sesión.
- Retransmitir cualquier paquete de datos que fue enviado previamente a la nueva IP/puerto hacia la IP/puerto antiguos.

### Validación Después del Cambio Local

El proceso anterior está definido para peers que reciben un paquete desde una IP/puerto cambiada. Sin embargo, también puede ser iniciado en la otra dirección, por un peer que detecta que su IP o puerto han cambiado. Un peer puede ser capaz de detectar que su IP local cambió; sin embargo, es mucho menos probable que detecte que su puerto cambió debido a una reasignación NAT. Por lo tanto, esto es opcional.

Al recibir un path challenge de un peer cuya IP o puerto ha cambiado, el otro peer debería iniciar un path challenge en la dirección opuesta.

### Usar como Ping/Pong

Los bloques Path Challenge y Path Response pueden utilizarse en cualquier momento como paquetes Ping/Pong. La recepción de un bloque Path Challenge no cambia ningún estado en el receptor, a menos que se reciba desde una IP/puerto diferente.

## Múltiples Sesiones

Los peers no deben establecer múltiples sesiones con el mismo peer, ya sea SSU 1 o 2, o con la misma o diferentes direcciones IP. Sin embargo, esto podría suceder, ya sea debido a errores, o que se haya perdido un mensaje de terminación de sesión anterior, o en una condición de carrera donde el mensaje de terminación aún no ha llegado.

Si Bob tiene una sesión existente con Alice, cuando Bob recibe el Session Confirmed de Alice, completando el handshake y estableciendo una nueva sesión, Bob debería:

- Migrar cualquier mensaje I2NP saliente no enviado o no confirmado de la sesión antigua a la nueva
- Enviar una terminación con código de razón 22 en la sesión antigua
- Eliminar la sesión antigua y reemplazarla con la nueva

## Terminación de Sesión

### Fase de handshake

Las sesiones en la fase de handshake generalmente se terminan simplemente por timeout, o al no responder más. Opcionalmente, pueden terminarse incluyendo un bloque de Termination en la respuesta, pero la mayoría de los errores no pueden ser respondidos debido a la falta de claves criptográficas. Incluso si las claves están disponibles para una respuesta que incluya un bloque de terminación, generalmente no vale la pena usar la CPU para realizar el DH para la respuesta. Una excepción PUEDE ser un bloque de Termination en un mensaje de reintento, que es económico de generar.

### Fase de datos

Las sesiones en la fase de datos se terminan enviando un mensaje de datos que incluye un bloque de Terminación. Este mensaje también debería incluir un bloque ACK. Puede, si la sesión ha estado activa el tiempo suficiente como para que un token enviado previamente haya expirado o esté a punto de expirar, incluir un bloque New Token. Este mensaje no solicita confirmación. Al recibir un bloque de Terminación con cualquier razón excepto "Terminación Recibida", el par responde con un mensaje de datos que contiene un bloque de Terminación con la razón "Terminación Recibida".

Después de enviar o recibir un bloque de Terminación, la sesión debería entrar en la fase de cierre durante algún período máximo de tiempo por determinar. El estado de cierre es necesario para protegerse contra la pérdida del paquete que contiene el bloque de Terminación, y los paquetes en vuelo en la otra dirección. Mientras está en la fase de cierre, no hay requisito de procesar ningún paquete recibido adicional. Una sesión en estado de cierre envía un paquete que contiene un bloque de Terminación en respuesta a cualquier paquete entrante que atribuye a la sesión. Una sesión debería limitar la velocidad a la que genera paquetes en el estado de cierre. Por ejemplo, una sesión podría esperar un número progresivamente creciente de paquetes recibidos o cantidad de tiempo antes de responder a los paquetes recibidos.

Para minimizar el estado que un router mantiene para una sesión que se está cerrando, las sesiones pueden, pero no están obligadas a, enviar exactamente el mismo paquete con el mismo número de paquete tal como está en respuesta a cualquier paquete recibido. Nota: Permitir la retransmisión de un paquete de terminación es una excepción al requisito de que se use un nuevo número de paquete para cada paquete. Enviar nuevos números de paquete es principalmente ventajoso para la recuperación de pérdidas y el control de congestión, que no se espera que sean relevantes para una conexión cerrada. Retransmitir el paquete final requiere menos estado.

Después de recibir un bloque de Terminación con la razón "Termination Received", la sesión puede salir de la fase de cierre.

### Limpieza

Al producirse cualquier terminación normal o anormal, los routers deben poner a cero cualquier dato efímero en memoria, incluyendo claves efímeras de handshake, claves de cifrado simétrico e información relacionada.

## MTU

Los requisitos varían, según si la dirección publicada se comparte con SSU 1. El mínimo actual de SSU 1 IPv4 es 620, que definitivamente es demasiado pequeño.

El MTU mínimo de SSU2 es 1280 tanto para IPv4 como para IPv6, que es el mismo especificado en [RFC-9000](https://tools.ietf.org/html/rfc9000). Ver más abajo. Al aumentar el MTU mínimo, los mensajes de tunnel de 1 KB y los mensajes cortos de construcción de tunnel cabrán en un datagrama, reduciendo considerablemente la cantidad típica de fragmentación. Esto también permite un aumento en el tamaño máximo de los mensajes I2NP. Los mensajes de streaming de 1820 bytes deberían caber en dos datagramas.

Un router no debe habilitar SSU2 o publicar una dirección SSU2 a menos que el MTU para esa dirección sea al menos 1280.

Los routers deben publicar un MTU no predeterminado en cada dirección de router SSU o SSU2.

### Dirección SSU

Dirección compartida con SSU 1, debe seguir las reglas de SSU 1. IPv4: Por defecto y máximo es 1484. Mínimo es 1292. (MTU IPv4 + 4) debe ser múltiplo de 16. IPv6: Debe ser publicado, mínimo es 1280 y máximo es 1488. MTU IPv6 debe ser múltiplo de 16.

### Dirección SSU2

IPv4: Por defecto y máximo es 1500. Mínimo es 1280. IPv6: Por defecto y máximo es 1500. Mínimo es 1280. No hay reglas de múltiplos de 16, pero probablemente debería ser un múltiplo de 2 como mínimo.

### Descubrimiento de PMTU

Para SSU 1, el Java I2P actual realiza el descubrimiento PMTU comenzando con paquetes pequeños y aumentando gradualmente el tamaño, o aumentando basándose en el tamaño del paquete recibido. Esto es rudimentario y reduce en gran medida la eficiencia. Continuar con esta funcionalidad en SSU 2 está por determinar.

Estudios recientes [PMTU](https://en.wikipedia.org/wiki/Path_MTU_Discovery) sugieren que un mínimo para IPv4 de 1200 o más funcionaría para más del 99% de las conexiones. QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) requiere un tamaño mínimo de paquete IP de 1280 bytes.

cita [RFC-9000](https://tools.ietf.org/html/rfc9000):

El tamaño máximo de datagrama se define como el tamaño más grande de carga útil UDP que puede enviarse a través de una ruta de red usando un solo datagrama UDP. QUIC NO DEBE usarse si la ruta de red no puede soportar un tamaño máximo de datagrama de al menos 1200 bytes.

QUIC asume un tamaño mínimo de paquete IP de al menos 1280 bytes. Este es el tamaño mínimo de IPv6 [IPv6] y también es compatible con la mayoría de las redes IPv4 modernas. Asumiendo el tamaño mínimo de cabecera IP de 40 bytes para IPv6 y 20 bytes para IPv4 y un tamaño de cabecera UDP de 8 bytes, esto resulta en un tamaño máximo de datagrama de 1232 bytes para IPv6 y 1252 bytes para IPv4. Por lo tanto, se espera que las redes IPv4 modernas y todas las rutas de red IPv6 puedan soportar QUIC.

Nota: Este requisito de soportar una carga útil UDP de 1200 bytes limita el espacio disponible para las cabeceras de extensión IPv6 a 32 bytes o las opciones IPv4 a 52 bytes si la ruta solo soporta el MTU mínimo de IPv6 de 1280 bytes. Esto afecta a los paquetes Initial y la validación de ruta.

fin de la cita

### Tamaño Mínimo de Handshake

QUIC requiere que los datagramas Initial en ambas direcciones tengan al menos 1200 bytes, para prevenir ataques de amplificación y asegurar que la PMTU lo soporte en ambas direcciones.

Podríamos requerir esto para Session Request y Session Created, a un costo considerable en ancho de banda. Quizás podríamos hacer esto solo si no tenemos un token, o después de recibir un mensaje Retry. Por determinar

QUIC requiere que Bob no envíe más de tres veces la cantidad de datos recibidos hasta que la dirección del cliente sea validada. SSU2 cumple este requisito de forma inherente, porque el mensaje Retry tiene aproximadamente el mismo tamaño que el mensaje Token Request, y es más pequeño que el mensaje Session Request. Además, el mensaje Retry solo se envía una vez.

### Tamaño Mínimo del Mensaje de Ruta

QUIC requiere que los mensajes que contengan bloques PATH_CHALLENGE o PATH_RESPONSE tengan al menos 1200 bytes, para prevenir ataques de amplificación y asegurar que el PMTU lo soporte en ambas direcciones.

También podríamos requerir esto, con un costo sustancial en ancho de banda. Sin embargo, estos casos deberían ser raros. TBD

### Tamaño Máximo de Mensaje I2NP

IPv4: No se asume fragmentación de IP. El encabezado IP + datagrama es de 28 bytes. Esto asume que no hay opciones IPv4. El tamaño máximo del mensaje es MTU - 28. El encabezado de la fase de datos es de 16 bytes y el MAC es de 16 bytes, totalizando 32 bytes. El tamaño de la carga útil es MTU - 60. La carga útil máxima de la fase de datos es 1440 para un MTU máximo de 1500. La carga útil máxima de la fase de datos es 1220 para un MTU mínimo de 1280.

IPv6: No se permite la fragmentación de IP. El encabezado IP + datagrama es de 48 bytes. Esto asume que no hay encabezados de extensión IPv6. El tamaño máximo del mensaje es MTU - 48. El encabezado de la fase de datos es de 16 bytes y el MAC es de 16 bytes, totalizando 32 bytes. El tamaño de la carga útil es MTU - 80. La carga útil máxima de la fase de datos es 1420 para una MTU máxima de 1500. La carga útil máxima de la fase de datos es 1200 para una MTU mínima de 1280.

En SSU 1, las directrices establecían un máximo estricto de aproximadamente 32 KB para un mensaje I2NP basado en 64 fragmentos máximos y un MTU mínimo de 620. Debido a la sobrecarga de los leaseSet agrupados y las claves de sesión, el límite práctico a nivel de aplicación era aproximadamente 6KB menor, es decir, alrededor de 26KB. El protocolo SSU 1 permite hasta 128 fragmentos, pero las implementaciones actuales lo limitan a 64 fragmentos.

Al aumentar la MTU mínima a 1280, con una carga útil de fase de datos de aproximadamente 1200, un mensaje SSU 2 de alrededor de 76 KB es posible en 64 fragmentos y 152 KB en 128 fragmentos. Esto permite fácilmente un máximo de 64 KB.

Debido a la fragmentación en túneles y la fragmentación en SSU 2, la probabilidad de pérdida de mensajes aumenta exponencialmente con el tamaño del mensaje. Continuamos recomendando un límite práctico de aproximadamente 10 KB en la capa de aplicación para datagramas I2NP.

## Proceso de Prueba de Pares

Consulta Seguridad de Peer Test arriba para un análisis del Peer Test de SSU1 y los objetivos del Peer Test de SSU2.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest
        <---------------- Charlie RI
4.      <------------------ PeerTest

5.      <----------------------------------------- PeerTest
6. PeerTest ----------------------------------------->
7.      <----------------------------------------- PeerTest
```
Cuando es rechazado por Bob:

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
4.      <------------------ PeerTest (reject)
```
Cuando es rechazado por Charlie:

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest (reject)
                      (optional: Bob could try another Charlie here)
4.      <------------------ PeerTest (reject)
```
NOTA: RI puede ser enviada como mensajes I2NP Database Store en bloques I2NP, o como bloques RI (si es lo suficientemente pequeña). Estos pueden estar contenidos en los mismos paquetes que los bloques de prueba de pares, si son lo suficientemente pequeños.

Los mensajes 1-4 están en sesión utilizando bloques Peer Test en un mensaje Data. Los mensajes 5-7 están fuera de sesión utilizando bloques Peer Test en un mensaje Peer Test.

NOTA: Como en SSU 1, los mensajes 4 y 5 pueden llegar en cualquier orden. Los mensajes 5 y/o 7 pueden no recibirse en absoluto si Alice está detrás de un firewall. Cuando el mensaje 5 llega antes que el mensaje 4, Alice no puede enviar inmediatamente el mensaje 6, porque aún no tiene la clave de introducción de Charlie para cifrar el encabezado. Cuando el mensaje 4 llega antes que el mensaje 5, Alice no debería enviar inmediatamente el mensaje 6, porque debería esperar a ver si llega el mensaje 5 sin abrir el firewall con el mensaje 6.

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
### Versiones

Las pruebas entre peers de diferentes versiones no están soportadas. La única combinación de versiones permitida es donde todos los peers son versión 2.

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
### Retransmisiones

Los mensajes 1-4 están en sesión y están cubiertos por los procesos de ACK de fase de datos y retransmisión. Los bloques de Peer Test requieren confirmación.

Los mensajes 5-7 pueden ser retransmitidos sin cambios.

### Notas sobre IPv6

Como en SSU 1, se admite la prueba de direcciones IPv6, y la comunicación Alice-Bob y Alice-Charlie puede ser a través de IPv6, si Bob y Charlie indican compatibilidad con una capacidad 'B' en su dirección IPv6 publicada. Ver la Propuesta 126 para más detalles.

Como en SSU 1 antes de la versión 0.9.50, Alice envía la solicitud a Bob usando una sesión existente sobre el transporte (IPv4 o IPv6) que desea probar. Cuando Bob recibe una solicitud de Alice vía IPv4, Bob debe seleccionar un Charlie que anuncie una dirección IPv4. Cuando Bob recibe una solicitud de Alice vía IPv6, Bob debe seleccionar un Charlie que anuncie una dirección IPv6. La comunicación real Bob-Charlie puede ser vía IPv4 o IPv6 (es decir, independiente del tipo de dirección de Alice). Este NO es el comportamiento de SSU 1 a partir de la versión 0.9.50, donde se permiten solicitudes mixtas IPv4/v6.

### Procesamiento por Bob

A diferencia de SSU 1, Alice especifica la IP y el puerto de prueba solicitados en el mensaje 1. Bob debería validar esta IP y puerto, y rechazar con código 5 si son inválidos. La validación de IP recomendada es que, para IPv4, coincida con la IP de Alice, y para IPv6, al menos los primeros 8 bytes de la IP coincidan. La validación del puerto debería rechazar puertos privilegiados y puertos para protocolos bien conocidos.

### Máquina de Estados de Resultados

Aquí documentamos cómo Alice puede determinar los resultados de una prueba de peer, basándose en qué mensajes se reciben. Las mejoras de SSU2 nos brindan la oportunidad de corregir, mejorar y documentar mejor la máquina de estados de resultados de prueba de peer en comparación con la de [SSU](/docs/transport/ssu).

Para cada tipo de dirección probada (IPv4 o IPv6), el resultado puede ser uno de UNKNOWN, OK, FIREWALLED, o SYMNAT. Adicionalmente, se puede realizar otro procesamiento para detectar cambios de IP o puerto, o un puerto externo diferente al puerto interno.

Problemas con la máquina de estados SSU documentada:

- Nunca enviamos el mensaje 6 a menos que hayamos recibido el mensaje 5, por lo que nunca sabemos si somos SYMNAT
- Si recibimos los mensajes 4 y 7, ¿cómo podríamos ser SYMNAT?
- Si la IP no coincidió pero el puerto sí, no somos SYMNAT, simplemente cambiamos nuestra IP

Por lo tanto, en contraste con SSU, recomendamos esperar varios segundos después de recibir el mensaje 4, luego enviar el mensaje 6 incluso si no se recibe el mensaje 5.

Un resumen de la máquina de estados, basado en si los mensajes 4, 5 y 7 son recibidos (sí o no), es el siguiente:

```
4 5 7  Result             Notes
-----  ------             -----
n n n  UNKNOWN
y n n  FIREWALLED           (unless currently SYMNAT)
n y n  OK                   (unless currently SYMNAT, which is unlikely)
y y n  OK                   (unless currently SYMNAT, which is unlikely)
n n y  n/a                  (can't send msg 6)
y n y  FIREWALLED or SYMNAT (requires sending msg 6 w/o rcv msg 5)
n y y  n/a                  (can't send msg 6)
y y y  OK
```
Una máquina de estados más detallada, con verificaciones de la IP/puerto recibida en el bloque de dirección del mensaje 7, se muestra a continuación. Un desafío es determinar si tú (Alice) eres quien tiene NAT simétrico, o si es Charlie.

Se recomienda el post-procesamiento o lógica adicional para confirmar las transiciones de estado requiriendo los mismos resultados en dos o más pruebas de peers.

Se recomienda también la validación y confirmación de IP/puerto recibida por dos o más pruebas, o con el bloque de dirección en los mensajes Session Created, pero esto está fuera del alcance de esta especificación.

```
If Alice does not get msg 5:
   If Alice does not get msg 4: -> UNKNOWN
   If Alice does not get msg 7: -> UNKNOWN
   If Alice gets msgs 4/7 and IP/port match: -> FIREWALLED
   If Alice gets msgs 4/7 and IP matches, port does not match:
      -> SYMNAT, but needs confirmation with 2nd test
   If Alice gets msgs 4/7 and IP does not match, port matches:
      -> FIREWALLED, address change?
   If Alice gets msgs 4/7 and both IP and port do not match:
      -> SYMNAT, address change?

If Alice gets msg 5:
   If Alice does not get msg 4: -> OK unless currently SYMNAT, else UNKNOWN
                                   (in SSU2 have to stop here)
   If Alice does not get msg 7: -> OK unless currently SYMNAT, else UNKNOWN
   If Alice gets msgs 4/5/7 and IP/port match: -> OK
   If Alice gets msgs 4/5/7 and IP matches, port does not match:
      -> OK, charlie is probably sym. natted
   If Alice gets msgs 4/5/7 and IP does not match, port matches:
      -> OK, address change?
   If Alice gets msgs 4/5/7 and both IP and port do not match:
      -> OK, address change?
```
## Proceso de Retransmisión

Ver Seguridad de Relay arriba para un análisis de SSU1 Relay y los objetivos para SSU2 Relay.

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse

5.      <-------------------------------------------- HolePunch
6. SessionRequest -------------------------------------------->
7.      <-------------------------------------------- SessionCreated
8. SessionConfirmed ------------------------------------------>
```
Cuando es rechazado por Bob:

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
4.      <-------------- RelayResponse
```
Cuando es rechazado por Charlie:

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse
```
NOTA: Los RI pueden enviarse ya sea como mensajes I2NP Database Store en bloques I2NP, o como bloques RI (si son lo suficientemente pequeños). Estos pueden contenerse en los mismos paquetes que los bloques de retransmisión, si son lo suficientemente pequeños.

En SSU 1, la información del router de Charlie contiene la IP, puerto, clave de introducción, etiqueta de retransmisión y expiración de cada introductor.

En SSU 2, la información del router de Charlie contiene el hash del router, la etiqueta de retransmisión y la expiración de cada introducer.

Alice debería reducir el número de viajes de ida y vuelta requeridos seleccionando primero un introductor (Bob) al que ya tenga una conexión. En segundo lugar, si no tiene ninguno, seleccionar un introductor para el cual ya tenga la información del router.

El relé entre versiones cruzadas también debería ser compatible si es posible. Esto facilitará una transición gradual de SSU 1 a SSU 2. Las combinaciones de versiones permitidas son (TODO):

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
### Retransmisiones

Relay Request, Relay Intro, y Relay Response están todos dentro de la sesión y están cubiertos por los procesos de ACK y retransmisión de la fase de datos. Los bloques Relay Request, Relay Intro, y Relay Response requieren confirmación de recepción.

Ten en cuenta que normalmente, Charlie responderá inmediatamente a un Relay Intro con un Relay Response, que debería incluir un bloque ACK. En ese caso, no se requiere un mensaje separado con un bloque ACK.

El hole punch puede ser retransmitido, como en SSU 1.

A diferencia de los mensajes I2NP, los mensajes Relay no tienen identificadores únicos, por lo que los duplicados deben ser detectados por la máquina de estados del relay, utilizando el nonce. Las implementaciones también pueden necesitar mantener un caché de nonces utilizados recientemente, para que los duplicados recibidos puedan ser detectados incluso después de que la máquina de estados para ese nonce haya completado.

### IPv4/v6

Todas las funciones del relay SSU 1 son compatibles, incluyendo aquellas documentadas en [Prop158](/proposals/158-ipv6-transport-enhancements) y compatibles desde la versión 0.9.50. Se admiten introducciones IPv4 e IPv6. Una Solicitud de Relay puede ser enviada a través de una sesión IPv4 para una introducción IPv6, y una Solicitud de Relay puede ser enviada a través de una sesión IPv6 para una introducción IPv4.

### Procesado por Alice

A continuación se presentan las diferencias con respecto a SSU 1 y recomendaciones para la implementación de SSU 2.

#### Selección de Introductor

En SSU 1, la introducción es relativamente económica, y Alice generalmente envía Relay Requests a todos los introductores. En SSU 2, la introducción es más costosa, ya que primero debe establecerse una conexión con un introductor. Para minimizar la latencia y la sobrecarga de introducción, los pasos de procesamiento recomendados son los siguientes:

- Ignorar cualquier introducer que haya expirado basándose en el valor iexp en la dirección
- Si ya se ha establecido una conexión SSU2 a uno o más introducers, elegir uno y enviar la Solicitud de Retransmisión solo a ese introducer.
- En caso contrario, si se conoce localmente un Router Info para uno o más introducers, elegir uno y conectarse solo a ese introducer.
- En caso contrario, buscar los Router Infos para todos los introducers, conectarse al introducer cuyo Router Info se reciba primero.

#### Manejo de Respuestas

En tanto SSU 1 como SSU 2, la Respuesta de Relé y el Hole Punch pueden recibirse en cualquier orden, o pueden no recibirse en absoluto.

En SSU 1, Alice generalmente recibe la Respuesta de Retransmisión (1 RTT) antes del Hole Punch (1 1/2 RTT). Puede que no esté bien documentado en esas especificaciones, pero Alice debe recibir la Respuesta de Retransmisión de Bob antes de continuar, para recibir la IP de Charlie. Si el Hole Punch se recibe primero, Alice no lo reconocerá, porque no contiene datos y la IP de origen no es reconocida. Después de recibir la Respuesta de Retransmisión, Alice debería esperar TANTO a recibir el Hole Punch de Charlie, COMO un breve retraso (recomendado 500 ms) antes de iniciar el handshake con Charlie.

En SSU 2, Alice normalmente recibirá el Hole Punch (1 1/2 RTT) antes que la Relay Response (2 RTT). El SSU 2 Hole Punch es más fácil de procesar que en SSU 1, porque es un mensaje completo con connection IDs definidos (derivados del relay nonce) y contenidos que incluyen la IP de Charlie. La Relay Response (mensaje Data) y el mensaje Hole Punch contienen el bloque Relay Response firmado idéntico. Por lo tanto, Alice puede iniciar el handshake con Charlie después de CUALQUIERA de estas opciones: recibir el Hole Punch de Charlie, O recibir la Relay Response de Bob.

La verificación de firma del Hole Punch incluye el hash del router del introductor (Bob). Si se han enviado Solicitudes de Retransmisión a más de un introductor, hay varias opciones para validar la firma:

- Intentar cada hash al que se envió una solicitud
- Usar diferentes nonces para cada introducer, y usar eso para determinar a qué introducer responde este Hole Punch
- No revalidar la firma si el contenido es idéntico al de la Relay Response, si ya se recibió
- No validar la firma en absoluto

Si Charlie está detrás de un NAT simétrico, su puerto reportado en la Respuesta de Retransmisión y el Hole Punch puede no ser preciso. Por lo tanto, Alice debería verificar el puerto de origen UDP del mensaje Hole Punch, y usar ese si es diferente al puerto reportado.

### Solicitudes de Etiquetas por Bob

En SSU 1, solo Alice podía solicitar una etiqueta, en la Solicitud de Sesión. Bob nunca podía solicitar una etiqueta, y Alice no podía retransmitir para Bob.

En SSU2, Alice generalmente solicita una etiqueta en la Solicitud de Sesión, pero tanto Alice como Bob también pueden solicitar una etiqueta en la fase de datos. Bob generalmente no está detrás de un firewall después de recibir una solicitud entrante, pero podría estarlo después de un relay, o el estado de Bob puede cambiar, o él puede solicitar un introductor para el otro tipo de dirección (IPv4/v6). Por lo tanto, en SSU2, es posible que tanto Alice como Bob sean simultáneamente relays para la otra parte.

## Información del Router Publicada

### Propiedades de Dirección

Las siguientes propiedades de dirección pueden ser publicadas, sin cambios respecto a SSU 1, incluyendo los cambios en [Prop158](/proposals/158-ipv6-transport-enhancements) soportados a partir de la API 0.9.50:

- caps: capacidades [B,C,4,6]
- host: IP (IPv4 o IPv6). Se permite dirección IPv6 acortada (con "::"). Puede estar presente o no si está detrás de firewall. No se permiten nombres de host.
- iexp[0-2]: Expiración de este introducer. Dígitos ASCII, en segundos desde la época. Solo presente si está detrás de firewall y se requieren introducers. Opcional (incluso si están presentes otras propiedades para este introducer).
- ihost[0-2]: IP del introducer (IPv4 o IPv6). Se permite dirección IPv6 acortada (con "::"). Solo presente si está detrás de firewall y se requieren introducers. No se permiten nombres de host. Solo dirección SSU.
- ikey[0-2]: Clave de introducción Base 64 del introducer. Solo presente si está detrás de firewall y se requieren introducers. Solo dirección SSU.
- iport[0-2]: Puerto del introducer 1024 - 65535. Solo presente si está detrás de firewall y se requieren introducers. Solo dirección SSU.
- itag[0-2]: Etiqueta del introducer 1 - (2**32 - 1) dígitos ASCII. Solo presente si está detrás de firewall y se requieren introducers.
- key: Clave de introducción Base 64.
- mtu: Opcional. Ver sección MTU arriba.
- port: 1024 - 65535 Puede estar presente o no si está detrás de firewall.

### Direcciones Publicadas

La RouterAddress publicada (parte del RouterInfo) tendrá un identificador de protocolo de "SSU" o "SSU2".

El RouterAddress debe contener tres opciones para indicar el soporte de SSU2:

- s=(Clave Base64) La clave pública estática Noise actual (s) para esta RouterAddress. Codificada en Base 64 usando el alfabeto Base 64 estándar de I2P. 32 bytes en binario, 44 bytes codificados en Base 64, clave X25519 little-endian.
- i=(Clave Base64) La clave de introducción actual para cifrar las cabeceras de esta RouterAddress. Codificada en Base 64 usando el alfabeto Base 64 estándar de I2P. 32 bytes en binario, 44 bytes codificados en Base 64, clave ChaCha20 big-endian.
- v=2 La versión actual (2). Cuando se publica como "SSU", se implica soporte adicional para la versión 1. El soporte para versiones futuras será con valores separados por comas, por ejemplo v=2,3. La implementación debe verificar la compatibilidad, incluyendo múltiples versiones si hay una coma presente. Las versiones separadas por comas deben estar en orden numérico.

Alice debe verificar que las tres opciones estén presentes y sean válidas antes de conectarse usando el protocolo SSU2.

Cuando se publica como "SSU" con las opciones "s", "i" y "v", y con las opciones "host" y "port", el router debe aceptar conexiones entrantes en ese host y puerto para ambos protocolos SSU y SSU2, y detectar automáticamente la versión del protocolo.

Cuando se publica como "SSU2" con las opciones "s", "i" y "v", y con las opciones "host" y "port", el router acepta conexiones entrantes en ese host y puerto solo para el protocolo SSU2.

Si un router soporta conexiones tanto SSU1 como SSU2 pero no implementa detección automática de versión para conexiones entrantes, debe anunciar direcciones tanto "SSU" como "SSU2", e incluir las opciones SSU2 únicamente en la dirección "SSU2". El router debería establecer un valor de costo más bajo (mayor prioridad) en la dirección "SSU2" que en la dirección "SSU", de modo que SSU2 sea preferido.

Si múltiples RouterAddresses SSU2 (ya sea como "SSU" o "SSU2") se publican en el mismo RouterInfo (para direcciones IP o puertos adicionales), todas las direcciones que especifiquen el mismo puerto deben contener opciones y valores SSU2 idénticos. En particular, todas deben contener la misma clave estática "s" y clave de introducción "i".

#### Introducers

Cuando se publica como SSU o SSU2 con introducers, están presentes las siguientes opciones:

- ih[0-2]=(hash Base64) Un hash de router para un introductor. Codificado en Base 64 usando el alfabeto estándar de I2P Base 64. 32 bytes en binario, 44 bytes codificado como Base 64
- iexp[0-2]: Expiración de este introductor. Sin cambios desde SSU 1.
- itag[0-2]: Etiqueta del introductor 1 - (2**32 - 1) Sin cambios desde SSU 1.

Las siguientes opciones son solo para SSU y no se utilizan para SSU2. En SSU2, Alice obtiene esta información del RI de Charlie en su lugar.

- ihost[0-2]
- ikey[0-2]
- itag[0-2]

Un router no debe publicar el host o puerto en la dirección al publicar introducers. Un router debe publicar capacidades 4 y/o 6 en la dirección al publicar introducers para indicar soporte para IPv4 y/o IPv6. Esto es lo mismo que la práctica actual para direcciones SSU 1 recientes.

Nota: Si se publica como SSU, y hay una mezcla de introducers SSU 1 y SSU2, los introducers SSU 1 deberían estar en los índices más bajos y los introducers SSU2 deberían estar en los índices más altos, para compatibilidad con routers más antiguos.

### Dirección SSU2 No Publicada

Si Alice no publica su dirección SSU2 (como "SSU" o "SSU2") para conexiones entrantes, debe publicar una dirección de router "SSU2" que contenga únicamente su clave estática y la versión SSU2, para que Bob pueda validar la clave después de recibir el RouterInfo de Alice en la parte 2 de Session Confirmed.

- s=(clave Base64) Como se define arriba para direcciones publicadas.
- i=(clave Base64) Como se define arriba para direcciones publicadas.
- v=2 Como se define arriba para direcciones publicadas.

Esta dirección de router no contendrá opciones "host" o "port", ya que no son necesarias para conexiones SSU2 salientes. El costo publicado para esta dirección no importa estrictamente, ya que es solo de entrada; sin embargo, puede ser útil para otros routers si el costo se establece más alto (menor prioridad) que otras direcciones. El valor sugerido es 14.

Alice también puede simplemente agregar las opciones "i", "s" y "v" a una dirección "SSU" publicada existente.

### Rotación de Clave Pública e IV

Usar las mismas claves estáticas para NTCP2 y SSU2 está permitido, pero no se recomienda.

Debido al almacenamiento en caché de las RouterInfos, los routers no deben rotar la clave pública estática o el IV mientras el router esté activo, ya sea en una dirección publicada o no. Los routers deben almacenar persistentemente esta clave e IV para reutilizarlos después de un reinicio inmediato, de modo que las conexiones entrantes continúen funcionando y los tiempos de reinicio no queden expuestos. Los routers deben almacenar persistentemente, o determinar de otra manera, la hora del último apagado, para que el tiempo de inactividad previo pueda calcularse al inicio.

Sujeto a preocupaciones sobre exponer los tiempos de reinicio, los routers pueden rotar esta clave o IV al arranque si el router estuvo previamente inactivo durante algún tiempo (varios días al menos).

Si el router tiene RouterAddresses SSU2 publicadas (como SSU o SSU2), el tiempo mínimo de inactividad antes de la rotación debería ser mucho más largo, por ejemplo un mes, a menos que la dirección IP local haya cambiado o el router "rekeys".

Si el router tiene alguna RouterAddress SSU publicada, pero no SSU2 (como SSU o SSU2), el tiempo de inactividad mínimo antes de la rotación debería ser más largo, por ejemplo un día, a menos que la dirección IP local haya cambiado o el router haga "rekeys". Esto se aplica incluso si la dirección SSU publicada tiene introducers.

Si el router no tiene ninguna RouterAddress publicada (SSU, SSU2, o SSU), el tiempo mínimo de inactividad antes de la rotación puede ser tan corto como dos horas, incluso si la dirección IP cambia, a menos que el router "rekeys".

Si el router "regenera claves" a un Router Hash diferente, también debería generar una nueva clave noise y clave intro.

Las implementaciones deben ser conscientes de que cambiar la clave pública estática o el IV impedirá las conexiones SSU2 entrantes de routers que hayan guardado en caché un RouterInfo más antiguo. La publicación de RouterInfo, la selección de pares de tunnel (incluyendo tanto OBGW como el salto más cercano IB), la selección de tunnel de salto cero, la selección de transporte y otras estrategias de implementación deben tener esto en cuenta.

La rotación de claves de introducción está sujeta a las mismas reglas que la rotación de claves.

Nota: El tiempo mínimo de inactividad antes del intercambio de claves puede modificarse para garantizar la salud de la red y prevenir la resiembra por parte de un router inactivo durante un período moderado de tiempo.

#### Ocultación de Identidad

La negación plausible no es un objetivo. Ver resumen anterior.

A cada patrón se le asignan propiedades que describen la confidencialidad proporcionada a la clave pública estática del iniciador, y a la clave pública estática del respondedor. Las suposiciones subyacentes son que las claves privadas efímeras son seguras, y que las partes abortan el handshake si reciben una clave pública estática de la otra parte en la que no confían.

Esta sección solo considera la filtración de identidad a través de campos de clave pública estática en los handshakes. Por supuesto, las identidades de los participantes de Noise podrían ser expuestas a través de otros medios, incluyendo campos de payload, análisis de tráfico, o metadatos como direcciones IP.

Alice: (8) Cifrado con forward secrecy hacia una parte autenticada.

Bob: (3) No se transmite, pero un atacante pasivo puede verificar candidatos para la clave privada del respondedor y determinar si el candidato es correcto.

Bob publica su clave pública estática en la netDb. Alice puede que no lo haga, pero debe incluirla en el RI enviado a Bob.

## Directrices de Paquetes

### Creación de Paquetes Salientes

Mensajes de handshake (Session Request/Created/Confirmed, Retry) pasos básicos, en orden:

- Crear encabezado de 16 o 32 bytes
- Crear carga útil
- mixHash() el encabezado (excepto para Retry)
- Cifrar la carga útil usando Noise (excepto para Retry, usar ChaChaPoly con el encabezado como AD)
- Cifrar el encabezado, y para Session Request/Created, la clave efímera

Pasos básicos de los mensajes de la fase de datos, en orden:

- Crear encabezado de 16 bytes
- Crear carga útil
- Cifrar la carga útil usando ChaChaPoly utilizando el encabezado como AD
- Cifrar el encabezado

### Manejo de Paquetes Entrantes

#### Resumen

Procesamiento inicial de todos los mensajes entrantes:

- Descifrar los primeros 8 bytes del encabezado (el ID de Conexión de Destino) con la clave de introducción
- Buscar la conexión por el ID de Conexión de Destino
- Si se encuentra la conexión y está en la fase de datos, ir a la sección de fase de datos
- Si no se encuentra la conexión, ir a la sección de handshake
- Nota: Los mensajes de Peer Test y Hole Punch también pueden buscarse por el ID de Conexión de Destino creado a partir del nonce de prueba o retransmisión.

Procesamiento de mensajes de handshake (Session Request/Created/Confirmed, Retry, Token Request) y otros mensajes fuera de sesión (Peer Test, Hole Punch):

- Descifrar los bytes 8-15 del encabezado (el tipo de paquete, versión y ID de red) con la intro key. Si es una Session Request, Token Request, Peer Test o Hole Punch válida, continuar
- Si no es un mensaje válido, buscar una conexión saliente pendiente por la IP/puerto de origen del paquete, tratar el paquete como una Session Created o Retry. Re-descifrar los primeros 8 bytes del encabezado con la clave correcta, y los bytes 8-15 del encabezado (el tipo de paquete, versión y ID de red). Si es una Session Created o Retry válida, continuar
- Si no es un mensaje válido, fallar, o poner en cola como un posible paquete de fase de datos fuera de orden
- Para Session Request/Created, Retry, Token Request, Peer Test y Hole Punch, descifrar los bytes 16-31 del encabezado
- Para Session Request/Created, descifrar la ephemeral key
- Validar todos los campos del encabezado, detenerse si no son válidos
- mixHash() el encabezado
- Para Session Request/Created/Confirmed, descifrar el payload usando Noise
- Para Retry y fase de datos, descifrar el payload usando ChaChaPoly
- Procesar el encabezado y el payload

Procesamiento de mensajes de la fase de datos:

- Descifrar los bytes 8-15 del encabezado (el tipo de paquete, versión e ID de red) con la clave correcta
- Descifrar la carga útil usando ChaChaPoly utilizando el encabezado como AD
- Procesar el encabezado y la carga útil

#### Detalles

En SSU 1, la clasificación de paquetes entrantes es difícil, porque no hay un encabezado para indicar el número de sesión. Los routers primero deben hacer coincidir la IP de origen y el puerto con un estado de peer existente, y si no se encuentra, intentar múltiples descifraciones con diferentes claves para encontrar el estado de peer apropiado o iniciar uno nuevo. En el caso de que la IP de origen o el puerto para una sesión existente cambie, posiblemente debido al comportamiento NAT, el router puede usar heurísticas costosas para intentar hacer coincidir el paquete con una sesión existente y recuperar el contenido.

SSU 2 está diseñado para minimizar el esfuerzo de clasificación de paquetes entrantes mientras mantiene la resistencia a DPI y otras amenazas en el camino. El número de Connection ID se incluye en el encabezado para todos los tipos de mensaje, y se cifra (ofusca) usando ChaCha20 con una clave y nonce conocidos. Además, el tipo de mensaje también se incluye en el encabezado (cifrado con protección de encabezado a una clave conocida y luego ofuscado con ChaCha20) y puede usarse para clasificación adicional. En ningún caso es necesaria una operación criptográfica asimétrica de DH de prueba u otra para clasificar un paquete.

Para casi todos los mensajes de todos los peers, la clave ChaCha20 para el cifrado del Connection ID es la clave de introducción del router de destino tal como se publica en la netDb.

Las únicas excepciones son los primeros mensajes enviados de Bob a Alice (Session Created o Retry) donde la clave de introducción de Alice aún no es conocida por Bob. En estos casos, se utiliza la clave de introducción de Bob como la clave.

El protocolo está diseñado para minimizar el procesamiento de clasificación de paquetes que podría requerir operaciones criptográficas adicionales en múltiples pasos de respaldo o heurísticas complejas. Además, la gran mayoría de los paquetes recibidos no requerirán una búsqueda de respaldo (posiblemente costosa) por IP/puerto de origen y un segundo descifrado de cabecera. Solo Session Created y Retry (y posiblemente otros por determinar) requerirán el procesamiento de respaldo. Si un endpoint cambia de IP o puerto después de la creación de la sesión, el ID de conexión aún se utiliza para buscar la sesión. Nunca es necesario usar heurísticas para encontrar la sesión, por ejemplo buscando una sesión diferente con la misma IP pero un puerto diferente.

Por lo tanto, los pasos de procesamiento recomendados en la lógica del bucle del receptor son:

1)  Descifrar los primeros 8 bytes con ChaCha20 usando la clave de introducción local, para recuperar el ID de Conexión de Destino. Si el ID de Conexión coincide con una sesión entrante actual o pendiente:

    a)  Using the appropriate key, decrypt the header bytes 8-15 to recover the version, net ID, and message type.
    b)  If the message type is Session Confirmed, it is a long header. Verify the net ID and protocol version are valid. Decrypt the bytes 15-31 of the header with ChaCha20 using the local intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise.
    c)  If the message type is valid but not Session Confirmed, it is a short header. Verify the net ID and protocol version are valid. decrypt the rest of the message with ChaCha20/Poly1305 using the session key, using the decrypted 16-byte header as the AD.
    d)  (optional) If connection ID is a pending inbound session awaiting a Session Confirmed message, but the net ID, protocol, or message type is not valid, it could be a Data message received out-of-order before the Session Confirmed, so the data phase header protection keys are not yet known, and the header bytes 8-15 were incorrectly decrypted. Queue the message, and attempt to decrypt it once the Session Confirmed message is received.
    e)  If b) or c) fails, drop the message.

2)  Si el ID de conexión no coincide con una sesión actual: Verificar que el encabezado de texto plano en los bytes 8-15 sea válido (sin realizar ninguna operación de protección de encabezado). Verificar que el ID de red y la versión del protocolo sean válidos, y que el tipo de mensaje sea Session Request, u otro tipo de mensaje permitido fuera de sesión (por determinar).

    a)  If all is valid and the message type is Session Request, decrypt bytes 16-31 of the header and the 32-byte X value with ChaCha20 using the local intro key.

    - If the token at header bytes 24-31 is accepted, then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Created in response.
    - If the token is not accepted, send a Retry message to the source IP/port with a token. Do not attempt to decrypt the message with Noise to avoid DDoS attacks.

    b)  If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.
    c)  If a) or b) fails, go to step 3)

3)  Buscar una sesión saliente pendiente por la IP/puerto de origen del paquete.

    a)  If found, re-decrypt the first 8 bytes with ChaCha20 using Bob's introduction key to recover the Destination Connection ID.
    b)  If the connection ID matches the pending session: Using the correct key, decrypt bytes 8-15 of the header to recover the version, net ID, and message type. Verify the net ID and protocol version are valid, and the message type is Session Created or Retry, or other message type allowed out-of-session (TBD).

    - If all is valid and the message type is Session Created, decrypt the next 16 bytes of the header and the 32-byte Y value with ChaCha20 using Bob's intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Confirmed in response.
    - If all is valid and the message type is Retry, decrypt bytes 16-31 of the header with ChaCha20 using Bob's intro key. Decrypt and validate the message using ChaCha20/Poly1305 using TBD as the key and TBD as the nonce and the decrypted 32-byte header as the AD. Resend a Session Request with the received token in response.
    - If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.

    > c)  If a pending outbound session is not found, or the connection ID does not match the pending session, drop the message, unless the port is shared with SSU 1.

4)  Si se está ejecutando SSU 1 en el mismo puerto, intentar procesar el mensaje como un paquete SSU 1.

#### Manejo de Errores

En general, una sesión (en la fase de handshake o de datos) nunca debe ser destruida después de recibir un paquete con un tipo de mensaje inesperado. Esto previene ataques de inyección de paquetes. Estos paquetes también serán comúnmente recibidos después de la retransmisión de un paquete de handshake, cuando las claves de descifrado del encabezado ya no son válidas.

En la mayoría de los casos, simplemente descartar el paquete. Una implementación puede, pero no está obligada a, retransmitir el paquete enviado previamente (mensaje de handshake o ACK 0) en respuesta.

Después de enviar Session Created como Bob, los paquetes inesperados son comúnmente paquetes de datos que no pueden descifrarse porque los paquetes Session Confirmed se perdieron o llegaron fuera de orden. Poner en cola los paquetes e intentar descifrarlos después de recibir los paquetes Session Confirmed.

Después de recibir Session Confirmed como Bob, los paquetes inesperados son comúnmente paquetes Session Confirmed retransmitidos, porque el ACK 0 del Session Confirmed se perdió. Los paquetes inesperados pueden descartarse. Una implementación puede, pero no está obligada a, enviar un paquete Data que contenga un bloque ACK como respuesta.

### Notas

Para Session Created y Session Confirmed, las implementaciones deben validar cuidadosamente todos los campos de encabezado descifrados (Connection IDs, número de paquete, tipo de paquete, versión, id, frag y flags) ANTES de llamar a mixHash() en el encabezado e intentar descifrar la carga útil con Noise AEAD. Si falla el descifrado de Noise AEAD, no se puede realizar ningún procesamiento adicional, porque mixHash() habrá corrompido el estado del handshake, a menos que una implementación almacene y "revierta" el estado del hash.

### Detección de Versión

Puede que no sea posible detectar eficientemente si los paquetes entrantes son versión 1 o 2 en el mismo puerto de entrada. Los pasos anteriores pueden tener sentido hacerlos antes del procesamiento de SSU 1, para evitar intentar operaciones DH de prueba usando ambas versiones del protocolo.

Por determinar si es necesario.

## Constantes Recomendadas

- Tiempo de espera para retransmisión de handshake saliente: 1.25 segundos, con backoff exponencial (retransmisiones en 1.25, 3.75, y 8.75 segundos)
- Tiempo de espera total para handshake saliente: 15 segundos
- Tiempo de espera para retransmisión de handshake entrante: 1 segundo, con backoff exponencial (retransmisiones en 1, 3, y 7 segundos)
- Tiempo de espera total para handshake entrante: 12 segundos
- Tiempo de espera después de enviar reintento: 9 segundos
- Retraso de ACK: max(10, min(rtt/6, 150)) ms
- Retraso de ACK inmediato: min(rtt/16, 5) ms
- Máximo de rangos ACK: ¿256?
- Profundidad máxima de ACK: ¿512?
- Distribución de padding: 0-15 bytes, o mayor
- Tiempo mínimo de espera para retransmisión en fase de datos: 1 segundo, como en [RFC-6298](https://tools.ietf.org/html/rfc6298)
- Ver también [RFC-6298](https://tools.ietf.org/html/rfc6298) para orientación adicional sobre temporizadores de retransmisión para la fase de datos.

## Análisis de Sobrecarga de Paquetes

Asume IPv4, sin incluir relleno adicional, sin incluir los tamaños de cabeceras IP y UDP. El relleno es relleno mod-16 solo para SSU 1.

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
## Problemas y Trabajo Futuro

### Tokens

Especificamos anteriormente que el token debe ser un valor de 8 bytes generado aleatoriamente, no generar un valor opaco como un hash o HMAC de un secreto del servidor y la IP, puerto, debido a ataques de reutilización. Sin embargo, esto requiere almacenamiento temporal y (opcionalmente) persistente de tokens entregados. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) usa un HMAC de 16 bytes de un secreto del servidor y dirección IP, y el secreto del servidor rota cada dos minutos. Deberíamos investigar algo similar, con un tiempo de vida del secreto del servidor más largo. Si incrustamos una marca de tiempo en el token, eso podría ser una solución, pero un token de 8 bytes podría no ser lo suficientemente grande para eso.

## Referencias

- **[Common]** [Especificación de Estructuras Comunes](/docs/specs/common-structures)
- **[ECIES]** [Especificación ECIES-X25519-AEAD-Ratchet](/docs/specs/ecies)
- **[NetDB]** [Base de Datos de Red](/docs/overview/network-database)
- **[NOISE]** [Marco de Protocolo Noise](https://noiseprotocol.org/noise.html)
- **[Nonces]** [Adversarios que No Respetan Nonces](https://eprint.iacr.org/2019/624.pdf)
- **[NTCP]** [Transporte NTCP](/docs/transport/ntcp)
- **[NTCP2]** [Especificación NTCP2](/docs/specs/ntcp2)
- **[PMTU]** [Descubrimiento de MTU de Ruta](https://en.wikipedia.org/wiki/Path_MTU_Discovery)
- **[Prop104]** [Propuesta 104: Transporte TLS](/proposals/104-tls-transport)
- **[Prop109]** [Propuesta 109: Transporte Conectable](/proposals/109-pt-transport)
- **[Prop158]** [Propuesta 158: Mejoras de Transporte IPv6](/proposals/158-ipv6-transport-enhancements)
- **[Prop159]** [Propuesta 159: SSU2](/proposals/159-ssu2)
- **[RFC-2104]** [RFC 2104: HMAC](https://tools.ietf.org/html/rfc2104)
- **[RFC-3449]** [RFC 3449: Implicaciones de Rendimiento TCP](https://tools.ietf.org/html/rfc3449)
- **[RFC-3526]** [RFC 3526: Grupos MODP](https://tools.ietf.org/html/rfc3526)
- **[RFC-5681]** [RFC 5681: Control de Congestión TCP](https://tools.ietf.org/html/rfc5681)
- **[RFC-5869]** [RFC 5869: HKDF](https://tools.ietf.org/html/rfc5869)
- **[RFC-6151]** [RFC 6151: Consideraciones de Seguridad MD5](https://tools.ietf.org/html/rfc6151)
- **[RFC-6298]** [RFC 6298: Temporizador de Retransmisión TCP](https://tools.ietf.org/html/rfc6298)
- **[RFC-6437]** [RFC 6437: Etiqueta de Flujo IPv6](https://tools.ietf.org/html/rfc6437)
- **[RFC-7539]** [RFC 7539: ChaCha20/Poly1305](https://tools.ietf.org/html/rfc7539)
- **[RFC-7748]** [RFC 7748: Curvas Elípticas para Seguridad](https://tools.ietf.org/html/rfc7748)
- **[RFC-7905]** [RFC 7905: Suites de Cifrado ChaCha20-Poly1305 para TLS](https://tools.ietf.org/html/rfc7905)
- **[RFC-9000]** [RFC 9000: Protocolo de Transporte QUIC](https://datatracker.ietf.org/doc/html/rfc9000)
- **[RFC-9001]** [RFC 9001: Uso de TLS para Asegurar QUIC](https://datatracker.ietf.org/doc/html/rfc9001)
- **[RFC-9002]** [RFC 9002: Detección de Pérdidas y Control de Congestión QUIC](https://datatracker.ietf.org/doc/html/rfc9002)
- **[RouterAddress]** [Estructura RouterAddress](/docs/specs/common-structures#struct-routeraddress)
- **[RouterIdentity]** [Estructura RouterIdentity](/docs/specs/common-structures#struct-routeridentity)
- **[SigningPublicKey]** [Tipo SigningPublicKey](/docs/specs/common-structures#type-signingpublickey)
- **[SSU]** [Transporte SSU](/docs/transport/ssu)
- **[STS]** [Protocolo Station-to-Station](https://en.wikipedia.org/wiki/Station-to-Station_protocol)
- **[Ticket1112]** [Ticket I2P 1112](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1112)
- **[Ticket1849]** [Ticket I2P 1849](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1849)
- **[WireGuard]** [Protocolo WireGuard](https://www.wireguard.com/papers/wireguard.pdf)
