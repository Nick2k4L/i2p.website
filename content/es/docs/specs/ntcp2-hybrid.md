---
title: "PQ Hybrid NTCP2"
description: "Variante híbrida post-cuántica del protocolo de transporte NTCP2 usando ML-KEM"
slug: "ntcp2-hybrid"
lastupdated: "2026-02"
category: "Transportes"
accurateFor: "0.9.69"
---

### Estado

Beta Q1 2026, lanzamiento Q2 2026

## Descripción general

Esta es la variante híbrida post-cuántica del protocolo de transporte NTCP2, según se diseñó en la Propuesta 169. Consulta esa propuesta para obtener información adicional.

PQ Hybrid NTCP2 solo está definido en la misma dirección y puerto que NTCP2 estándar. No se permite la operación en un puerto diferente, o sin soporte para NTCP2 estándar, y no será permitido durante varios años, cuando NTCP2 estándar sea descontinuado.

Esta especificación documenta únicamente los cambios requeridos al NTCP2 estándar para soportar PQ Hybrid. Consulte la especificación NTCP2 para los detalles de implementación base.

## Diseño

Soportamos los estándares NIST FIPS 203 y 204 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) que están basados en, pero NO son compatibles con, CRYSTALS-Kyber y CRYSTALS-Dilithium (versiones 3.1, 3 y anteriores).

### Intercambio de Claves

PQ KEM proporciona únicamente claves efímeras y no soporta directamente handshakes de clave estática como Noise XK e IK. Los tipos de cifrado son los mismos que se utilizan en PQ Hybrid Ratchet y están definidos en el documento de estructuras comunes [/docs/specs/common-structures/](/docs/specs/common-structures/), como en [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf). Los tipos híbridos solo están definidos en combinación con X25519.

Los tipos de cifrado son:

| Tipo | Código |
|------|--------|
| MLKEM512_X25519 | 5 |
| MLKEM768_X25519 | 6 |
| MLKEM1024_X25519 | 7 |
### Combinaciones Legales

Los nuevos tipos de cifrado se indican en las RouterAddresses. El tipo de cifrado en el certificado de clave seguirá siendo tipo 4.

## Especificación

### Patrones de Handshake

Los handshakes utilizan patrones de handshake del [Protocolo Noise](https://noiseprotocol.org/noise.html).

Se utiliza el siguiente mapeo de letras:

- e = clave efímera de un solo uso
- s = clave estática
- p = carga útil del mensaje
- e1 = clave PQ efímera de un solo uso, enviada de Alice a Bob
- ekem1 = el texto cifrado KEM, enviado de Bob a Alice

Las siguientes modificaciones a XK e IK para el secreto hacia adelante híbrido (hfs) están especificadas en la [especificación Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) sección 5:

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
El patrón e1 se define de la siguiente manera, como se especifica en la sección 4 de [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf):

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
El patrón ekem1 se define de la siguiente manera, como se especifica en la sección 4 de [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf):

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
### KDF de Handshake Noise

#### Descripción general

El handshake híbrido se define en la [especificación Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf). El primer mensaje, de Alice a Bob, contiene e1, la clave de encapsulación, antes de la carga útil del mensaje. Esto se trata como una clave estática adicional; llama a EncryptAndHash() en ella (como Alice) o DecryptAndHash() (como Bob). Luego procesa la carga útil del mensaje como de costumbre.

El segundo mensaje, de Bob a Alice, contiene ekem1, el texto cifrado, antes de la carga útil del mensaje. Este se trata como una clave estática adicional; llama a EncryptAndHash() en él (como Bob) o DecryptAndHash() (como Alice). Luego, calcula el kem_shared_key y llama a MixKey(kem_shared_key). Después procesa la carga útil del mensaje como de costumbre.

#### Operaciones ML-KEM Definidas

Definimos las siguientes funciones correspondientes a los bloques de construcción criptográficos utilizados según se define en [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

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

Ten en cuenta que tanto el encap_key como el texto cifrado están encriptados dentro de bloques ChaCha/Poly en los mensajes 1 y 2 del handshake Noise. Serán descifrados como parte del proceso de handshake.

La kem_shared_key se mezcla en la chaining key con MixHash(). Ver más abajo para detalles.

#### Alice KDF para Mensaje 1

Después del patrón de mensaje 'es' y antes de la carga útil, añadir:

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
#### Bob KDF para el Mensaje 1

Después del patrón de mensaje 'es' y antes de la carga útil, añadir:

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
#### Bob KDF para Mensaje 2

Para XK: Después del patrón de mensaje 'ee' y antes de la carga útil, añadir:

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
#### KDF de Alice para el Mensaje 2

Después del patrón de mensaje 'ee', agregar:

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
#### KDF para Mensaje 3 (solo XK)

sin cambios

#### KDF para split()

sin cambios

### Detalles del Handshake

#### Identificadores de ruido

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

Cambios: El NTCP2 actual contiene solo las opciones en la sección ChaCha. Con ML-KEM, la sección ChaCha también contendrá la clave pública PQ cifrada.

Para que PQ y non-PQ NTCP2 puedan ser soportados en la misma dirección de router y puerto, usamos el bit más significativo del valor X (clave pública efímera X25519) para marcar que es una conexión PQ. Este bit siempre está desactivado para conexiones non-PQ.

Para Alice, después de que el mensaje sea cifrado por Noise, pero antes de la ofuscación AES de X, establecer X[31] |= 0x7f.

Para Bob, después de la des-ofuscación AES de X, probar X[31] & 0x80. Si el bit está establecido, limpiarlo con X[31] &= 0x7f, y descifrar vía Noise como una conexión PQ. Si el bit está limpio, descifrar vía Noise como una conexión no-PQ como de costumbre.

Para PQ NTCP2 anunciado en una dirección de router y puerto diferentes, esto no es requerido.

Para obtener información adicional, consulte la sección de Direcciones Publicadas a continuación.

Contenido sin procesar:

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
Datos sin cifrar (etiqueta de autenticación Poly1305 no mostrada):

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
Nota: el campo de versión en el bloque de opciones del mensaje 1 debe establecerse en 2, incluso para conexiones PQ.

Tamaños:

| Tipo | Código de Tipo | X len | Msg 1 len | Msg 1 Enc len | Msg 1 Dec len | PQ key len | opt len |
|------|-----------|-------|-----------|---------------|---------------|------------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 880+pad | 848 | 816 | 800 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1264+pad | 1232 | 1200 | 1184 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1648+pad | 1616 | 1584 | 1568 | 16 |
Nota: Los códigos de tipo son solo para uso interno. Los routers permanecerán como tipo 4, y el soporte se indicará en las direcciones del router.

#### 2) SessionCreated

Contenido sin procesar:

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
Datos sin cifrar (etiqueta de autenticación Poly1305 no mostrada):

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
Tamaños:

| Tipo | Código de Tipo | Y len | Msg 2 len | Msg 2 Enc len | Msg 2 Dec len | PQ CT len | opt len |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 848+pad | 816 | 784 | 768 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1136+pad | 1104 | 1104 | 1088 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1616+pad | 1584 | 1584 | 1568 | 16 |
Nota: Los códigos de tipo son solo para uso interno. Los routers permanecerán como tipo 4, y el soporte será indicado en las direcciones del router.

#### 3) SessionConfirmed

Sin cambios

#### Función de Derivación de Claves (KDF) (para la fase de datos)

Sin cambios

#### Direcciones Publicadas

En todos los casos, utiliza el nombre de transporte NTCP2 como de costumbre.

Usa la misma dirección/puerto que non-PQ, non-firewalled. Solo se admite una variante PQ. En la dirección del router, publica v=2 (como es habitual) y el nuevo parámetro pq=[3|4|5] para indicar MLKEM 512/768/1024. Alice establece el MSB de la clave efímera (key[31] & 0x80) en la solicitud de sesión para indicar que esta es una conexión híbrida. Ver arriba. Los routers más antiguos ignorarán el parámetro pq y se conectarán non-pq como es habitual.

Dirección/puerto diferente como no-PQ, o solo-PQ, sin firewall NO está soportado. Esto no se implementará hasta que NTCP2 no-PQ se deshabilite, dentro de varios años. Cuando no-PQ se deshabilite, múltiples variantes PQ pueden ser soportadas, pero solo una por dirección. Cuando esté soportado, en la dirección del router, publica v=[3|4|5] para indicar MLKEM 512/768/1024. Alice no establece el MSB de la clave efímera. Los routers más antiguos verificarán el parámetro v y omitirán esta dirección como no soportada.

Direcciones con firewall (sin IP publicada): En la dirección del router, publicar v=2 (como es habitual). No es necesario publicar un parámetro pq.

Alice puede conectarse a un Bob PQ usando la variante PQ que Bob publica, sin importar si Alice anuncia soporte pq en su información de router, o si anuncia la misma variante.

#### Relleno Máximo

En la especificación actual, los mensajes 1 y 2 están definidos para tener una cantidad "razonable" de relleno, con un rango recomendado de 0-31 bytes y sin máximo especificado.

Hasta la API 0.9.68 (versión 2.11.0), Java I2P implementaba un máximo de 256 bytes de relleno para conexiones no-PQ, sin embargo esto no estaba documentado previamente. A partir de la API 0.9.69 (versión 2.12.0), Java I2P implementa el mismo relleno máximo para conexiones no-PQ que para MLKEM-512. Ver tabla a continuación.

Usar el tamaño de mensaje definido como el relleno máximo, es decir, el relleno máximo duplicará el tamaño del mensaje para conexiones PQ, como sigue:

| Relleno Máximo del Mensaje | no-PQ (hasta 0.9.68) | no-PQ (desde 0.9.69) | MLKEM-512 | MLKEM-768 | MLKEM-1024 |
|----------------------------|----------------------|----------------------|-----------|-----------|------------|
| Session Request  |   256   |   880   |    880   |     1264   |    1648  |
| Session Created  |   256   |   848   |    848   |     1136   |    1616  |
## Análisis de Sobrecarga

### Intercambio de Claves

Aumento de tamaño (bytes):

| Tipo | Pubkey (Msg 1) | Texto cifrado (Msg 2) |
|------|----------------|-------------------|
| MLKEM512_X25519 | +816 | +784 |
| MLKEM768_X25519 | +1200 | +1104 |
| MLKEM1024_X25519 | +1584 | +1584 |
## Análisis de Seguridad

Las categorías de seguridad NIST se resumen en la [presentación NIST](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) diapositiva 10. Criterios preliminares: Nuestra categoría mínima de seguridad NIST debería ser 2 para protocolos híbridos y 3 para solo PQ.

| Categoría | Tan Seguro Como |
|----------|--------------|
| 1 | AES128 |
| 2 | SHA256 |
| 3 | AES192 |
| 4 | SHA384 |
| 5 | AES256 |
### Handshakes

Todos estos son protocolos híbridos. Las implementaciones deberían preferir MLKEM768; MLKEM512 no es lo suficientemente seguro.

Categorías de seguridad NIST [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf):

| Algoritmo | Categoría de Seguridad |
|-----------|------------------------|
| MLKEM512 | 1 |
| MLKEM768 | 3 |
| MLKEM1024 | 5 |
## Notas de Implementación

### Soporte de Bibliotecas

Las bibliotecas Bouncycastle, BoringSSL y WolfSSL ahora soportan MLKEM y MLDSA. El soporte de OpenSSL estará en su versión 3.5 el 8 de abril de 2025 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

### Identificación de Tráfico Entrante

Establecemos el MSB de la clave efímera (key[31] & 0x80) en la solicitud de sesión para indicar que esta es una conexión híbrida. Esto nos permite ejecutar tanto NTCP estándar como NTCP híbrido en el mismo puerto. Solo se admite una variante híbrida para conexiones entrantes, y se anuncia en la dirección del router. Por ejemplo, pq=3 o pq=4.

#### Ofuscación

Como Alice, para una conexión PQ, antes de la ofuscación, establecer X[31] |= 0x80. Esto hace que X sea una clave pública X25519 inválida. Después de la ofuscación, AES-CBC la aleatorizará. El MSB de X será aleatorio después de la ofuscación.

Como Bob, verifica si (X[31] & 0x80) != 0 después de la des-ofuscación. Si es así, es una conexión PQ.

La versión mínima del router requerida para NTCP2-PQ está por determinar.

Nota: Los códigos de tipo son solo para uso interno. Los routers permanecerán como tipo 4, y el soporte se indicará en las direcciones del router.

## Compatibilidad del Router

### Nombres de Transporte

En todos los casos, usa el nombre de transporte NTCP2 como siempre. Los routers más antiguos ignorarán el parámetro pq y se conectarán con NTCP2 estándar como de costumbre.

## Referencias

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
