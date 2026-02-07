---
title: "Especificación de LeaseSet Cifrado"
description: "Ocultación, cifrado y descifrado de leaseSets cifrados"
slug: "encryptedleaseset"
category: "Protocolos"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Resumen

Este documento especifica el ocultamiento, cifrado y descifrado de leasesets cifrados. Para la estructura del leaseset cifrado, consulta la [especificación de estructuras comunes](/docs/specs/common-structures). Para información de contexto sobre leasesets cifrados, consulta la [propuesta 123](/proposals/123-new-netdb-entries). Para su uso en la netdb, consulta la documentación de netdb.

### Definiciones

Definimos las siguientes funciones correspondientes a los bloques de construcción criptográficos utilizados para LS2 cifrado:

**CSRNG(n)** : salida de n bytes de un generador de números aleatorios criptográficamente seguro.

Además del requisito de que el CSRNG sea criptográficamente seguro (y por lo tanto adecuado para generar material de clave), DEBE ser seguro que alguna salida de n-bytes se use para material de clave cuando las secuencias de bytes que la preceden y siguen inmediatamente estén expuestas en la red (como en un salt, o relleno cifrado). Las implementaciones que dependen de una fuente potencialmente no confiable deben hacer hash de cualquier salida que vaya a ser expuesta en la red [PRNG-REFS](http://projectbullrun.org/dual-ec/ext-rand.html).

**H(p, d)** : Función hash SHA-256 que toma una cadena de personalización p y datos d, y produce una salida de longitud 32 bytes.

Usa SHA-256 de la siguiente manera:

```
H(p, d) := SHA-256(p || d)
```
**STREAM** : El cifrado de flujo ChaCha20 como se especifica en [RFC-7539-S2.4](https://tools.ietf.org/html/rfc7539#section-2.4), con el contador inicial establecido en 1. S_KEY_LEN = 32 y S_IV_LEN = 12.

- **ENCRYPT(k, iv, plaintext)** : Cifra el texto plano usando la clave de cifrado k, y el nonce iv que DEBE ser único para la clave k. Devuelve un texto cifrado que tiene el mismo tamaño que el texto plano. Todo el texto cifrado debe ser indistinguible de datos aleatorios si la clave es secreta.

- **DECRYPT(k, iv, ciphertext)** : Descifra el texto cifrado usando la clave de cifrado k y el nonce iv. Devuelve el texto plano.

**SIG** : El esquema de firma Red25519 (correspondiente al SigType 11) con cegado de clave. Tiene las siguientes funciones:

- **DERIVE_PUBLIC(privkey)** : Devuelve la clave pública correspondiente a la clave privada dada.

- **SIGN(privkey, m)** : Devuelve una firma con la clave privada privkey sobre el mensaje dado m.

- **VERIFY(pubkey, m, sig)** : Verifica la firma sig contra la clave pública pubkey y el mensaje m. Devuelve true si la firma es válida, false en caso contrario.

También debe soportar las siguientes operaciones de enmascaramiento de claves:

- **GENERATE_ALPHA(data, secret)** : Generar alfa para aquellos que conocen los datos y un secreto opcional. El resultado debe estar distribuido de forma idéntica a las claves privadas.

- **BLIND_PRIVKEY(privkey, alpha)** : Ciega una clave privada, usando un secreto alpha.

- **BLIND_PUBKEY(pubkey, alpha)** : Ciega una clave pública, usando un alpha secreto. Para un par de claves dado (privkey, pubkey) se mantiene la siguiente relación:

```
BLIND_PUBKEY(pubkey, alpha) ==
DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))
```
**DH** : Sistema de acuerdo de claves públicas X25519. Claves privadas de 32 bytes, claves públicas de 32 bytes, produce salidas de 32 bytes. Tiene las siguientes funciones:

- **GENERATE_PRIVATE()** : Genera una nueva clave privada.

- **DERIVE_PUBLIC(privkey)** : Devuelve la clave pública correspondiente a la clave privada dada.

- **DH(privkey, pubkey)** : Genera un secreto compartido a partir de las claves privada y pública dadas.

**HKDF(salt, ikm, info, n)** : Una función criptográfica de derivación de claves que toma material de clave de entrada ikm (que debería tener buena entropía pero no se requiere que sea una cadena uniformemente aleatoria), un salt de longitud 32 bytes, y un valor 'info' específico del contexto, y produce una salida de n bytes adecuada para usar como material de clave.

Usa HKDF como se especifica en [RFC-5869](https://tools.ietf.org/html/rfc5869), utilizando la función hash HMAC SHA-256 como se especifica en [RFC-2104](https://tools.ietf.org/html/rfc2104). Esto significa que SALT_LEN es de 32 bytes máximo.

### Formato

El formato LS2 cifrado consiste en tres capas anidadas:

- Una capa externa que contiene la información en texto plano necesaria para almacenamiento y recuperación.
- Una capa intermedia que maneja la autenticación del cliente.
- Una capa interna que contiene los datos LS2 reales.

El formato general se ve así:

```
Layer 0 data + Enc(layer 1 data + Enc(layer 2 data)) + Signature
```
Ten en cuenta que el LS2 cifrado está ofuscado. El Destino no está en la cabecera. La ubicación de almacenamiento DHT es SHA-256(tipo de firma || clave pública ofuscada), y se rota diariamente.

NO utiliza el encabezado LS2 estándar especificado arriba.

#### Capa 0 (externa)

**Tipo** : 1 byte

No está realmente en el encabezado, sino que forma parte de los datos cubiertos por la firma. Tomar del campo en el Database Store Message.

**Tipo de Firma de Clave Pública Ciega** : 2 bytes, big endian

Este siempre será tipo 11, identificando una clave ciega Red25519.

**Clave Pública Ciega** : Longitud según lo implica el tipo de firma

**Marca de tiempo de publicación** : 4 bytes, big endian

Segundos desde el epoch, se reinicia en 2106

**Expires** : 2 bytes, big endian

Desplazamiento desde la marca de tiempo publicada en segundos, máximo 18,2 horas

**Flags** : 2 bytes

Orden de bits: 15 14 ... 3 2 1 0

- Bit 0: Si es 0, no hay claves offline; si es 1, hay claves offline
- Otros bits: establecer a 0 para compatibilidad con usos futuros

**Datos de clave transitoria** : Presente si la bandera indica claves offline

- **Marca de tiempo de expiración** : 4 bytes, big endian. Segundos desde epoch, reinicia en 2106
- **Tipo de firma transitoria** : 2 bytes, big endian
- **Clave pública de firma transitoria** : Longitud según implica el tipo de firma
- **Firma** : Longitud según implica el tipo de firma de la clave pública ciega. Sobre la marca de tiempo de expiración, tipo de firma transitoria y clave pública transitoria. Verificada con la clave pública ciega.

**lenOuterCiphertext** : 2 bytes, big endian

**outerCiphertext** : lenOuterCiphertext bytes

Datos cifrados de capa 1. Ver más abajo los algoritmos de derivación de claves y cifrado.

**Signature** : Longitud según el tipo de firma de la clave de firmado utilizada

La firma es de todo lo anterior. Si la bandera indica claves offline, la firma se verifica con la clave pública transitoria. De lo contrario, la firma se verifica con la clave pública ciega.

#### Capa 1 (intermedia)

**Flags** : 1 byte

Orden de bits: 76543210

- Bit 0: 0 para todos, 1 para por-cliente, sección de autenticación a continuación
- Bits 3-1: Esquema de autenticación, solo si el bit 0 está establecido en 1 para por-cliente, de lo contrario 000
  - 000: Autenticación de cliente DH (o sin autenticación por-cliente)
  - 001: Autenticación de cliente PSK
- Bits 7-4: Sin usar, establecer en 0 para compatibilidad futura

**Datos de autenticación de cliente DH** : Presente si el bit de bandera 0 está establecido en 1 y los bits de bandera 3-1 están establecidos en 000.

- **ephemeralPublicKey** : 32 bytes
- **clients** : 2 bytes, big endian. Número de entradas authClient a seguir, 40 bytes cada una
- **authClient** : Datos de autorización para un solo cliente. Ver más abajo el algoritmo de autorización por cliente.
  - **clientID_i** : 8 bytes
  - **clientCookie_i** : 32 bytes

**Datos de autenticación de cliente PSK** : Presente si el bit de bandera 0 está establecido en 1 y los bits de bandera 3-1 están establecidos en 001.

- **authSalt** : 32 bytes
- **clients** : 2 bytes, big endian. Número de entradas authClient a continuación, 40 bytes cada una
- **authClient** : Datos de autorización para un solo cliente. Ver más abajo para el algoritmo de autorización por cliente.
  - **clientID_i** : 8 bytes
  - **clientCookie_i** : 32 bytes

**innerCiphertext** : Longitud implícita por lenOuterCiphertext (cualquier dato que permanezca)

Datos cifrados de capa 2. Ver a continuación los algoritmos de derivación de claves y cifrado.

#### Capa 2 (interna)

**Tipo** : 1 byte

Ya sea 3 (LS2) o 7 (Meta LS2)

**Datos** : Datos del LeaseSet2 para el tipo dado.

Incluye el encabezado y la firma.

### Derivación de Clave de Ocultación

Utilizamos el siguiente esquema para el enmascaramiento de claves, basado en Ed25519 y ZCash RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf). Las firmas Red25519 están sobre la curva Ed25519, utilizando SHA-512 para el hash.

No utilizamos el apéndice A.2 del rend-spec-v3.txt de Tor [TOR-REND-SPEC-V3](https://spec.torproject.org/rend-spec-v3), que tiene objetivos de diseño similares, porque sus claves públicas ofuscadas pueden estar fuera del subgrupo de orden primo, con implicaciones de seguridad desconocidas.

#### Objetivos

- La clave pública de firma en el destino sin cegar debe ser Ed25519 (tipo de firma 7) o Red25519 (tipo de firma 11); no se admiten otros tipos de firma
- Si la clave pública de firma está offline, la clave pública de firma transitoria también debe ser Ed25519
- El cegado es computacionalmente simple
- Utiliza primitivas criptográficas existentes
- Las claves públicas cegadas no pueden ser descegadas
- Las claves públicas cegadas deben estar en la curva Ed25519 y el subgrupo de orden primo
- Debe conocer la clave pública de firma del destino (no se requiere el destino completo) para derivar la clave pública cegada
- Opcionalmente proporcionar un secreto adicional requerido para derivar la clave pública cegada

#### Seguridad

La seguridad de un esquema de cegado requiere que la distribución de alpha sea la misma que las claves privadas sin cegar. Sin embargo, cuando cegamos una clave privada Ed25519 (tipo de firma 7) a una clave privada Red25519 (tipo de firma 11), la distribución es diferente. Para cumplir con los requisitos de la sección 4.1.6.1 de zcash [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf), Red25519 (tipo de firma 11) debería usarse también para las claves sin cegar, para que "la combinación de una clave pública re-aleatorizada y firma(s) bajo esa clave no revelen la clave de la cual fue re-aleatorizada." Permitimos el tipo 7 para destinos existentes, pero recomendamos el tipo 11 para nuevos destinos que serán encriptados.

#### Definiciones

**B** : El punto base (generador) Ed25519 2^255 - 19 como en [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)

**L** : El orden Ed25519 2^252 + 27742317777372353535851937790883648493 como en [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)

**DERIVE_PUBLIC(a)** : Convertir una clave privada a pública, como en Ed25519 (multiplicar por G)

**alpha** : Un número aleatorio de 32 bytes conocido por aquellos que conocen el destino.

**GENERATE_ALPHA(destination, date, secret)** : Generar alpha para la fecha actual, para aquellos que conocen el destino y el secreto. El resultado debe estar distribuido de manera idéntica a las claves privadas Ed25519.

**a** : La clave privada de firma EdDSA o RedDSA de 32 bytes sin cegar utilizada para firmar el destino

**A** : La clave pública de firma EdDSA o RedDSA de 32 bytes sin cegar en el destino, = DERIVE_PUBLIC(a), como en Ed25519

**a'** : La clave privada de firma EdDSA de 32 bytes ofuscada utilizada para firmar el leaseset cifrado. Esta es una clave privada EdDSA válida.

**A'** : La clave pública de firma EdDSA ciega de 32 bytes en el Destination, puede ser generada con DERIVE_PUBLIC(a'), o desde A y alpha. Esta es una clave pública EdDSA válida, en la curva y en el subgrupo de orden primo.

**LEOS2IP(x)** : Invertir el orden de los bytes de entrada a little-endian

**H\*(x)** : 32 bytes = (LEOS2IP(SHA512(x))) mod B, igual que en el hash-and-reduce de Ed25519

#### Cálculos de Cegamiento

Se deben generar nuevos alpha secretos y claves ciegas cada día (UTC).

El alpha secreto y las claves cegadas se calculan de la siguiente manera:

GENERATE_ALPHA(destino, fecha, secreto), para todas las partes:

```
// secret is optional, else zero-length
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of blinded public key A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
datestring = 8 bytes ASCII YYYYMMDD from the current date UTC
secret = UTF-8 encoded string
seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || secret, "i2pblinding1", 64)
// treat seed as a 64 byte little-endian value
alpha = seed mod L
```
BLIND_PRIVKEY(), para el propietario que publica el leaseSet:

```
alpha = GENERATE_ALPHA(destination, date, secret)
// If for a Ed25519 private key (type 7)
seed = destination's signing private key
a = left half of SHA512(seed) and clamped as usual for Ed25519
// else for a Red25519 private key (type 11)
a = destination's signing private key
// Addition using scalar arithmetic
blinded signing private key = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
blinded signing public key = A' = DERIVE_PUBLIC(a')
```
BLIND_PUBKEY(), para los clientes que recuperan el leaseSet:

```
alpha = GENERATE_ALPHA(destination, date, secret)
A = destination's signing public key
// Addition using group elements (points on the curve)
blinded public key = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```
Ambos métodos de calcular A' producen el mismo resultado, como se requiere.

#### Firma

El leaseSet no cegado está firmado por la clave privada de firma Ed25519 o Red25519 no cegada y verificado con la clave pública de firma Ed25519 o Red25519 no cegada (tipos de firma 7 u 11) como es habitual.

Si la clave pública de firma está offline, el leaseSet no cegado es firmado por la clave privada de firma transitoria Ed25519 o Red25519 no cegada y verificado con la clave pública de firma transitoria Ed25519 o Red25519 no cegada (tipos de firma 7 u 11) como es habitual. Ver abajo para notas adicionales sobre claves offline para leasesets cifrados.

Para la firma del leaseSet cifrado, utilizamos Red25519 basado en RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) para firmar y verificar con claves ciegas. Las firmas Red25519 están sobre la curva Ed25519, utilizando SHA-512 para el hash.

Red25519 es similar al Ed25519 estándar excepto por lo especificado a continuación.

#### Cálculos de Firma/Verificación

La parte externa del leaseSet cifrado utiliza claves y firmas Red25519.

Red25519 es similar a Ed25519. Hay dos diferencias:

Las claves privadas Red25519 se generan a partir de números aleatorios y luego deben reducirse mod L, donde L se define arriba. Las claves privadas Ed25519 se generan a partir de números aleatorios y luego se "fijan" usando enmascaramiento bit a bit en los bytes 0 y 31. Esto no se hace para Red25519. Las funciones GENERATE_ALPHA() y BLIND_PRIVKEY() definidas arriba generan claves privadas Red25519 apropiadas usando mod L.

En Red25519, el cálculo de r para la firma utiliza datos aleatorios adicionales, y usa el valor de la clave pública en lugar del hash de la clave privada. Debido a los datos aleatorios, cada firma Red25519 es diferente, incluso cuando se firma los mismos datos con la misma clave.

```
Signing:
  T = 80 random bytes
  r = H*(T || publickey || message)
  (rest is the same as in Ed25519)

Verification:
  Same as for Ed25519
```
### Cifrado y procesamiento

#### Derivación de subcredenciales

Como parte del proceso de cegado, necesitamos asegurar que un LS2 cifrado solo pueda ser descifrado por alguien que conozca la clave pública de firma del Destination correspondiente. No se requiere el Destination completo. Para lograr esto, derivamos una credencial de la clave pública de firma:

```
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
credential = H("credential", keydata)
```
La cadena de personalización asegura que la credencial no colisione con ningún hash utilizado como clave de búsqueda DHT, como el hash de Destination plano.

Para una clave ciega dada, podemos entonces derivar una subcredencial:

```
subcredential = H("subcredential", credential || blindedPublicKey)
```
La subcredencial se incluye en los procesos de derivación de claves que se describen a continuación, lo que vincula esas claves al conocimiento de la clave pública de firma del Destination.

#### Cifrado de Capa 1

Primero, se prepara la entrada para el proceso de derivación de claves:

```
outerInput = subcredential || publishedTimestamp
```
A continuación, se genera un salt aleatorio:

```
outerSalt = CSRNG(32)
```
Entonces se deriva la clave utilizada para cifrar la capa 1:

```
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Finalmente, el texto plano de la capa 1 se cifra y serializa:

```
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```
#### Descifrado de capa 1

El salt se analiza desde el texto cifrado de la capa 1:

```
outerSalt = outerCiphertext[0:31]
```
Entonces se deriva la clave utilizada para cifrar la capa 1:

```
outerInput = subcredential || publishedTimestamp
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Finalmente, se descifra el texto cifrado de la capa 1:

```
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```
#### Cifrado de capa 2

Cuando la autorización de cliente está habilitada, `authCookie` se calcula como se describe a continuación. Cuando la autorización de cliente está deshabilitada, `authCookie` es el arreglo de bytes de longitud cero.

El cifrado procede de manera similar a la capa 1:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = CSRNG(32)
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```
#### Descifrado de Capa 2

Cuando la autorización de cliente está habilitada, `authCookie` se calcula como se describe a continuación. Cuando la autorización de cliente está deshabilitada, `authCookie` es el arreglo de bytes de longitud cero.

El descifrado procede de manera similar a la capa 1:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = innerCiphertext[0:31]
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```
### Autorización por cliente

Cuando la autorización de cliente está habilitada para un Destination, el servidor mantiene una lista de clientes a los que está autorizando para descifrar los datos cifrados del LS2. Los datos almacenados por cliente dependen del mecanismo de autorización, e incluyen algún tipo de material criptográfico que cada cliente genera y envía al servidor a través de un mecanismo seguro fuera de banda.

Hay dos alternativas para implementar autorización por cliente:

#### Autorización de cliente DH

Cada cliente genera un par de claves DH `[csk_i, cpk_i]`, y envía la clave pública `cpk_i` al servidor.

##### Procesamiento del servidor

El servidor genera un nuevo `authCookie` y un par de claves DH efímeras:

```
authCookie = CSRNG(32)
esk = GENERATE_PRIVATE()
epk = DERIVE_PUBLIC(esk)
```
Luego, para cada cliente autorizado, el servidor cifra `authCookie` con su clave pública:

```
sharedSecret = DH(esk, cpk_i)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
El servidor coloca cada tupla `[clientID_i, clientCookie_i]` en la capa 1 del LS2 cifrado, junto con `epk`.

##### Procesamiento del cliente

El cliente usa su clave privada para derivar su identificador de cliente esperado `clientID_i`, clave de cifrado `clientKey_i`, y IV de cifrado `clientIV_i`:

```
sharedSecret = DH(csk_i, epk)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Luego el cliente busca en los datos de autorización de capa 1 una entrada que contenga `clientID_i`. Si existe una entrada coincidente, el cliente la descifra para obtener `authCookie`:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Autorización de cliente con clave precompartida

Cada cliente genera una clave secreta de 32 bytes `psk_i`, y la envía al servidor. Alternativamente, el servidor puede generar la clave secreta y enviarla a uno o más clientes.

##### Procesamiento del servidor

El servidor genera un nuevo `authCookie` y salt:

```
authCookie = CSRNG(32)
authSalt = CSRNG(32)
```
Luego, para cada cliente autorizado, el servidor cifra `authCookie` con su clave precompartida:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
El servidor coloca cada tupla `[clientID_i, clientCookie_i]` en la capa 1 del LS2 cifrado, junto con `authSalt`.

##### Procesamiento del cliente

El cliente utiliza su clave precompartida para derivar su identificador de cliente esperado `clientID_i`, clave de cifrado `clientKey_i`, y IV de cifrado `clientIV_i`:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Luego el cliente busca en los datos de autorización de capa 1 una entrada que contenga `clientID_i`. Si existe una entrada coincidente, el cliente la descifra para obtener `authCookie`:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Consideraciones de seguridad

Ambos mecanismos de autorización de cliente descritos anteriormente proporcionan privacidad para la membresía de clientes. Una entidad que solo conoce el Destination puede ver cuántos clientes están suscritos en cualquier momento, pero no puede rastrear qué clientes están siendo agregados o revocados.

Los servidores DEBERÍAN aleatorizar el orden de los clientes cada vez que generen un LS2 cifrado, para evitar que los clientes conozcan su posición en la lista e infieran cuándo se han añadido o revocado otros clientes.

Un servidor PUEDE elegir ocultar el número de clientes que están suscritos insertando entradas aleatorias en la lista de datos de autorización.

##### Ventajas de la autorización de cliente DH

- La seguridad del esquema no depende únicamente del intercambio fuera de banda del material de claves del cliente. La clave privada del cliente nunca necesita salir de su dispositivo, por lo que un adversario que sea capaz de interceptar el intercambio fuera de banda, pero no pueda romper el algoritmo DH, no puede descifrar el LS2 cifrado, ni determinar por cuánto tiempo se le da acceso al cliente.

##### Desventajas de la autorización de cliente DH

- Requiere N + 1 operaciones DH en el lado del servidor para N clientes.
- Requiere una operación DH en el lado del cliente.
- Requiere que el cliente genere la clave secreta.

##### Ventajas de la autorización de cliente PSK

- No requiere operaciones DH.
- Permite al servidor generar la clave secreta.
- Permite al servidor compartir la misma clave con múltiples clientes, si se desea.

##### Desventajas de la autorización de cliente PSK

- La seguridad del esquema depende críticamente del intercambio fuera de banda del material de clave del cliente. Un adversario que intercepte el intercambio para un cliente particular puede descifrar cualquier LS2 cifrado posterior para el cual ese cliente esté autorizado, así como determinar cuándo se revoca el acceso del cliente.

### LS cifrado con direcciones Base 32

No puedes usar una dirección base 32 tradicional para un LS2 cifrado, ya que contiene solo el hash del destino. No proporciona la clave pública no ciega. Por lo tanto, una dirección base 32 por sí sola es insuficiente. El cliente necesita o bien el destino completo (que contiene la clave pública), o la clave pública por sí misma. Si el cliente tiene el destino completo en una libreta de direcciones, y la libreta de direcciones soporta búsqueda inversa por hash, entonces se puede recuperar la clave pública.

Por lo tanto, necesitamos un nuevo formato que coloque la clave pública en lugar del hash en una dirección base32. Este formato también debe contener el tipo de firma de la clave pública y el tipo de firma del esquema de ofuscación. Los requisitos totales son 32 + 3 = 35 bytes, requiriendo 56 caracteres en base 32, o más para tipos de clave pública más largos.

```
data = ((1 byte flags || 1 byte unblinded sigtype || 1 byte blinded sigtype) XOR checksum) || 32 byte pubkey
address = Base32Encode(data) || ".b32.i2p"
```
Utilizamos el mismo sufijo ".b32.i2p" que para las direcciones base 32 tradicionales. Las direcciones para leasesets cifrados se identifican por los 56 caracteres codificados (35 bytes decodificados), comparado con 52 caracteres (32 bytes) para las direcciones base 32 tradicionales. Los cinco bits no utilizados al final de b32 deben ser 0.

No puedes usar un LS2 cifrado para bittorrent, debido a las respuestas de anuncio compactas que son de 32 bytes. Los 32 bytes contienen solo el hash. No hay espacio para una indicación de que el leaseSet está cifrado, o los tipos de firma.

Consulta la [especificación de nombres](/docs/specs/naming) o la [propuesta 149](/proposals/149-b32-encrypted-ls2) para más información sobre el nuevo formato.

### LS Cifrado con Claves Fuera de Línea

Para leaseSets cifrados con claves offline, las claves privadas ofuscadas también deben generarse offline, una para cada día.

Como el bloque de firma opcional sin conexión está en la parte de texto claro del leaseset cifrado, cualquiera que rastree los floodfills podría usar esto para rastrear el leaseset (pero no descifrarlo) durante varios días. Para prevenir esto, el propietario de las claves debería generar también nuevas claves transitorias para cada día. Tanto las claves transitorias como las cegadas pueden generarse con anticipación y entregarse al router en lote.

No hay un formato de archivo definido para empaquetar múltiples claves transitorias y ciegas y proporcionarlas al cliente o router. No hay una mejora del protocolo I2CP definida para admitir leaseSets cifrados con claves offline.

### Notas

- Un servicio que use leasesets cifrados publicaría la versión cifrada en los floodfills. Sin embargo, por eficiencia, enviaría leasesets sin cifrar a los clientes en el mensaje garlic envuelto, una vez autenticado (mediante lista blanca, por ejemplo).
- Los floodfills pueden limitar el tamaño máximo a un valor razonable para prevenir abusos.
- Después del descifrado, se deben realizar varias verificaciones, incluyendo que la marca de tiempo interna y la expiración coincidan con las del nivel superior.
- ChaCha20 fue seleccionado sobre AES. Aunque las velocidades son similares si el soporte de hardware AES está disponible, ChaCha20 es 2.5-3x más rápido cuando el soporte de hardware AES no está disponible, como en dispositivos ARM de gama baja.

## Referencias

- **[ED25519-REFS]** "High-speed high-security signatures" por Daniel J. Bernstein, Niels Duif, Tanja Lange, Peter Schwabe, y Bo-Yin Yang. [http://cr.yp.to/papers.html#ed25519](http://cr.yp.to/papers.html#ed25519)
- **[KEYBLIND-PROOF]** [https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html](https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html)
- **[KEYBLIND-REFS]** [https://trac.torproject.org/projects/tor/ticket/8106](https://trac.torproject.org/projects/tor/ticket/8106) y [https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html](https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html)
- **[PRNG-REFS]** [http://projectbullrun.org/dual-ec/ext-rand.html](http://projectbullrun.org/dual-ec/ext-rand.html) y [https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html)
- **[RFC-2104]** [https://tools.ietf.org/html/rfc2104](https://tools.ietf.org/html/rfc2104)
- **[RFC-4880-S5.1]** [https://tools.ietf.org/html/rfc4880#section-5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
- **[RFC-5869]** [https://tools.ietf.org/html/rfc5869](https://tools.ietf.org/html/rfc5869)
- **[RFC-7539-S2.4]** [https://tools.ietf.org/html/rfc7539#section-2.4](https://tools.ietf.org/html/rfc7539#section-2.4)
- **[TOR-REND-SPEC-V3]** [https://spec.torproject.org/rend-spec-v3](https://spec.torproject.org/rend-spec-v3)
- **[ZCASH]** [https://github.com/zcash/zips/tree/master/protocol/protocol.pdf](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)
