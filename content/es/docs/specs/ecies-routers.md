---
title: "Mensajes de Router ECIES-X25519"
description: "Especificación para el cifrado de mensajes garlic a routers ECIES usando X25519"
slug: "ecies-routers"
category: "Protocolos"
lastUpdated: "2025-03"
accurateFor: "0.9.65"
---

## Nota

Soportado desde la versión 0.9.49. Despliegue en red y pruebas en progreso. Sujeto a revisiones menores. Ver [propuesta 156](/proposals/156-ecies-routers).

## Resumen

Este documento especifica el cifrado de mensajes garlic encryption para routers ECIES, utilizando primitivas criptográficas introducidas por [ECIES-X25519](/docs/specs/ecies). Es una parte de la [propuesta 156](/proposals/156-ecies-routers) general para convertir routers de claves ElGamal a claves ECIES-X25519. Esta especificación está implementada desde la versión 0.9.49.

Para una descripción general de todos los cambios requeridos para routers ECIES, consulta la [propuesta 156](/proposals/156-ecies-routers). Para mensajes garlic a destinos ECIES-X25519, consulta [ECIES-X25519](/docs/specs/ecies).

### Primitivas Criptográficas

Las primitivas requeridas para implementar esta especificación son:

- AES-256-CBC como en [Criptografía](/docs/specs/cryptography)
- Funciones STREAM ChaCha20/Poly1305: ENCRYPT(k, n, plaintext, ad) y DECRYPT(k, n, ciphertext, ad) - como en [NTCP2](/docs/specs/ntcp2), [ECIES-X25519](/docs/specs/ecies), y [RFC-7539](https://tools.ietf.org/html/rfc7539)
- Funciones DH X25519 - como en [NTCP2](/docs/specs/ntcp2) y [ECIES-X25519](/docs/specs/ecies)
- HKDF(salt, ikm, info, n) - como en [NTCP2](/docs/specs/ntcp2) y [ECIES-X25519](/docs/specs/ecies)

Otras funciones Noise definidas en otro lugar:

- MixHash(d) - como en [NTCP2](/docs/specs/ntcp2) y [ECIES-X25519](/docs/specs/ecies)
- MixKey(d) - como en [NTCP2](/docs/specs/ntcp2) y [ECIES-X25519](/docs/specs/ecies)

## Diseño

El ECIES Router SKM no necesita un Ratchet SKM completo como se especifica en [ECIES](/docs/specs/ecies) para Destinations. No hay requisito para mensajes no anónimos usando el patrón IK. El modelo de amenazas no requiere claves efímeras codificadas con Elligator2.

Por lo tanto, el router SKM utilizará el patrón "N" de Noise, el mismo que se especifica en [Prop152](/proposals/152-ecies-tunnels) para la construcción de túneles. Utilizará el mismo formato de payload que se especifica en [ECIES](/docs/specs/ecies) para Destinations. No se utilizará el modo de clave estática cero (sin enlace o sesión) de IK especificado en [ECIES](/docs/specs/ecies).

Las respuestas a las consultas serán cifradas con una etiqueta ratchet si se solicita en la consulta. Esto está documentado en [Prop154](/proposals/154-ecies-lookups), ahora especificado en [I2NP](/docs/specs/i2np).

El diseño permite que el router tenga un único ECIES Session Key Manager. No hay necesidad de ejecutar Session Key Managers de "clave dual" como se describe en [ECIES](/docs/specs/ecies) para los Destinations. Los routers solo tienen una clave pública.

Un router ECIES no tiene una clave estática ElGamal. El router aún necesita una implementación de ElGamal para construir túneles a través de routers ElGamal y enviar mensajes cifrados a routers ElGamal.

Un router ECIES PUEDE requerir un Administrador de Claves de Sesión ElGamal parcial para recibir mensajes etiquetados con ElGamal recibidos como respuestas a búsquedas NetDB de routers floodfill anteriores a la versión 0.9.46, ya que esos routers no tienen una implementación de respuestas etiquetadas con ECIES como se especifica en [Prop152](/proposals/152-ecies-tunnels). Si no es así, un router ECIES puede no solicitar una respuesta cifrada de un router floodfill anterior a la versión 0.9.46.

Esto es opcional. La decisión puede variar en varias implementaciones de I2P y puede depender de la cantidad de la red que se haya actualizado a 0.9.46 o superior. A la fecha, aproximadamente el 85% de la red es 0.9.46 o superior.

### Marco de Protocolo Noise

Esta especificación proporciona los requisitos basados en el [Noise Protocol Framework](https://noiseprotocol.org/noise.html) (Revisión 34, 2018-07-11). En la terminología de Noise, Alice es la iniciadora y Bob es el respondedor.

Se basa en el protocolo Noise Noise_N_25519_ChaChaPoly_SHA256. Este protocolo Noise utiliza las siguientes primitivas:

- **Patrón de Handshake Unidireccional: N** - Alice no transmite su clave estática a Bob (N)
- **Función DH: X25519** - X25519 DH con una longitud de clave de 32 bytes según se especifica en [RFC-7748](https://tools.ietf.org/html/rfc7748).
- **Función de Cifrado: ChaChaPoly** - AEAD_CHACHA20_POLY1305 según se especifica en [RFC-7539](https://tools.ietf.org/html/rfc7539) sección 2.8. Nonce de 12 bytes, con los primeros 4 bytes establecidos en cero. Idéntico al usado en [NTCP2](/docs/specs/ntcp2).
- **Función Hash: SHA256** - Hash estándar de 32 bytes, ya usado extensivamente en I2P.

### Patrones de Handshake

Los handshakes utilizan patrones de handshake [Noise](https://noiseprotocol.org/noise.html).

Se utiliza la siguiente correspondencia de letras:

- e = clave efímera de un solo uso
- s = clave estática
- p = carga útil del mensaje

La solicitud de construcción es idéntica al patrón Noise N. Esto también es idéntico al primer mensaje (Solicitud de Sesión) en el patrón XK utilizado en [NTCP2](/docs/specs/ntcp2).

```
<- s
  ...
  e es p ->
```
### Cifrado de mensajes

Los mensajes se crean y se cifran asimétricamente hacia el router de destino. Este cifrado asimétrico de mensajes es actualmente ElGamal como se define en [Cryptography](/docs/specs/cryptography) y contiene una suma de verificación SHA-256. Este diseño no es forward-secret (sin secreto hacia adelante).

El diseño ECIES utiliza el patrón Noise unidireccional "N" con DH (intercambio de claves Diffie-Hellman) efímero-estático ECIES-X25519, con un HKDF, y AEAD ChaCha20/Poly1305 para secreto hacia adelante, integridad y autenticación. Alice es el remitente anónimo del mensaje, un router o destino. El router ECIES objetivo es Bob.

### Cifrado de respuesta

Las respuestas no son parte de este protocolo, ya que Alice es anónima. Las claves de respuesta, si las hay, se incluyen en el mensaje de solicitud. Consulta la [especificación I2NP](/docs/specs/i2np) para los Mensajes de Búsqueda en Base de Datos.

Las respuestas a los mensajes Database Lookup son mensajes Database Store o Database Search Reply. Se cifran como mensajes de Sesión Existente con la clave de respuesta de 32 bytes y la etiqueta de respuesta de 8 bytes como se especifica en [I2NP](/docs/specs/i2np) y [Prop154](/proposals/154-ecies-lookups).

No hay respuestas explícitas a los mensajes Database Store. El remitente puede agrupar su propia respuesta como un Garlic Message hacia sí mismo, conteniendo un mensaje Delivery Status.

## Especificación

X25519: Ver [ECIES](/docs/specs/ecies).

Identidad del Router y Certificado de Clave: Ver [Estructuras Comunes](/docs/specs/common-structures).

### Cifrado de Solicitudes

El cifrado de la solicitud es el mismo que el especificado en [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) y [Prop152](/proposals/152-ecies-tunnels), usando el patrón "N" de Noise.

Las respuestas a las búsquedas se cifrarán con una etiqueta ratchet si se solicita en la búsqueda. Los mensajes de solicitud de búsqueda en la base de datos contienen la clave de respuesta de 32 bytes y la etiqueta de respuesta de 8 bytes según se especifica en [I2NP](/docs/specs/i2np) y [Prop154](/proposals/154-ecies-lookups). La clave y la etiqueta se utilizan para cifrar la respuesta.

Los conjuntos de etiquetas no se crean. El esquema de clave estática cero especificado en ECIES-X25519-AEAD-Ratchet [Prop144](/proposals/144-ecies-x25519-aead-ratchet) y [ECIES](/docs/specs/ecies) no se utilizará. Las claves efímeras no se codificarán con Elligator2.

Generalmente, estos serán mensajes de Nueva Sesión y se enviarán con una clave estática cero (sin vinculación o sesión), ya que el remitente del mensaje es anónimo.

#### KDF para ck y h iniciales

Este es el protocolo [Noise](https://noiseprotocol.org/noise.html) estándar para el patrón "N" con un nombre de protocolo estándar. Es el mismo que se especifica en [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) y [Prop152](/proposals/152-ecies-tunnels) para los mensajes de construcción de tunnel.

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
#### KDF para Mensaje

Los creadores de mensajes generan un par de claves X25519 efímero para cada mensaje. Las claves efímeras deben ser únicas por mensaje. Esto es lo mismo que se especifica en [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) y [Prop152](/proposals/152-ecies-tunnels) para mensajes de construcción de tunnel.

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
#### Carga útil

La carga útil tiene el mismo formato de bloque definido en [ECIES](/docs/specs/ecies) y [Prop144](/proposals/144-ecies-x25519-aead-ratchet). Todos los mensajes deben contener un bloque DateTime para la prevención de repetición.

## Notas de Implementación

- Los routers más antiguos no verifican el tipo de cifrado del router y enviarán mensajes cifrados con ElGamal. Algunos routers recientes tienen errores y enviarán varios tipos de mensajes malformados. Los implementadores deberían detectar y rechazar estos registros antes de la operación DH si es posible, para reducir el uso de CPU.

## Referencias

- [Estructuras Comunes](/docs/specs/common-structures)
- [Criptografía](/docs/specs/cryptography)
- [ECIES](/docs/specs/ecies)
- [I2NP](/docs/specs/i2np)
- [Marco de Protocolo Noise](https://noiseprotocol.org/noise.html)
- [NTCP2](/docs/specs/ntcp2)
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet)
- [Prop152](/proposals/152-ecies-tunnels)
- [Prop154](/proposals/154-ecies-lookups)
- [Prop156](/proposals/156-ecies-routers)
- [RFC-7539](https://tools.ietf.org/html/rfc7539)
- [RFC-7748](https://tools.ietf.org/html/rfc7748)
- [Creación de Tunnel-ECIES](/docs/specs/tunnel-creation-ecies)
