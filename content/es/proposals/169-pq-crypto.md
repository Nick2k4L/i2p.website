---
title: "Protocolos Criptográficos Post-Cuánticos"
aliases: 
number: "169"
author: "zzz, orignal, drzed, eyedeekay"
created: "2025-01-21"
lastupdated: "2026-02-28"
status: "Abrir"
thread: "http://zzz.i2p/topics/3294"
target: "0.9.80"
toc: true
---

### Estado

| Protocolo / Característica | Estado |
|--------------------|--------|
| Ratchet | Completo en Java I2P e i2pd |
| NTCP2 | Beta Q1 2026 |
| SSU2 | Implementación comenzando pronto, Beta Q23 2026 |
| MLDSA SigTypes | Baja prioridad, probablemente 2027+ |
## Resumen

Aunque la investigación y competencia por criptografía post-cuántica (PQ) adecuada ha estado en curso durante una década, las opciones no se han vuelto claras hasta hace poco.

Comenzamos a examinar las implicaciones de la criptografía PQ en 2022 [zzz.i2p](http://zzz.i2p/topics/3294).

Los estándares TLS agregaron soporte para cifrado híbrido en los últimos dos años y ahora se usa para una porción significativa del tráfico cifrado en internet debido al soporte en Chrome y Firefox [Cloudflare](https://blog.cloudflare.com/pq-2024/).

NIST recientemente finalizó y publicó los algoritmos recomendados para criptografía post-cuántica [NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards). Varias bibliotecas de criptografía comunes ahora soportan los estándares NIST o lanzarán soporte en el futuro cercano.

Tanto [Cloudflare](https://blog.cloudflare.com/pq-2024/) como [NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) recomiendan que la migración comience inmediatamente. Véase también las preguntas frecuentes sobre PQ de 2022 de la [NSA](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF). I2P debe ser líder en seguridad y criptografía. Ahora es el momento de implementar los algoritmos recomendados. Utilizando nuestro sistema flexible de tipos de criptografía y tipos de firma, añadiremos tipos para criptografía híbrida, y para firmas PQ e híbridas.

## Objetivos

- Seleccionar algoritmos resistentes a PQ
- Agregar algoritmos solo-PQ e híbridos a los protocolos I2P donde sea apropiado
- Definir múltiples variantes
- Seleccionar las mejores variantes después de la implementación, pruebas, análisis e investigación
- Agregar soporte de manera incremental y con compatibilidad hacia atrás

## No-Objetivos

- No cambiar los protocolos de cifrado unidireccional (Noise N)
- No alejarse de SHA256, no está amenazado a corto plazo por PQ
- No seleccionar las variantes preferidas finales en este momento

## Modelo de Amenazas

- Routers en el OBEP o IBGW, posiblemente en colusión,
  almacenando mensajes garlic para descifrado posterior (forward secrecy)
- Observadores de red
  almacenando mensajes de transporte para descifrado posterior (forward secrecy)
- Participantes de red falsificando firmas para RI, LS, streaming, datagramas,
  u otras estructuras

## Protocolos Afectados

Modificaremos los siguientes protocolos, aproximadamente en orden de desarrollo. El despliegue general probablemente será desde finales de 2025 hasta mediados de 2027. Consulta la sección de Prioridades y Despliegue a continuación para más detalles.

| Protocolo / Característica | Estado |
|--------------------|--------|
| Hybrid MLKEM Ratchet and LS | Aprobado 2025-06; beta 2025-08; lanzamiento 2025-11 |
| Hybrid MLKEM NTCP2 | Probado en red en vivo, Aprobado 2026-02; objetivo beta 2026-05; objetivo lanzamiento 2026-08 |
| Hybrid MLKEM SSU2 | Aprobado 2026-02; objetivo beta 2026-08; objetivo lanzamiento 2026-11 |
| MLDSA SigTypes 12-14 | La propuesta es estable pero puede no finalizarse hasta 2027 |
| MLDSA Dests | Probado en red en vivo, requiere actualización de red para soporte floodfill |
| Hybrid SigTypes 15-17 | Preliminar |
| Hybrid Dests | |
## Diseño

Soportaremos los estándares NIST FIPS 203 y 204 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) que están basados en, pero NO son compatibles con, CRYSTALS-Kyber y CRYSTALS-Dilithium (versiones 3.1, 3 y anteriores).

### Intercambio de Claves

Admitiremos el intercambio de claves híbrido en los siguientes protocolos:

| Proto   | Tipo de Noise | ¿Solo soporte PQ? | ¿Soporte híbrido? |
|---------|---------------|-------------------|-------------------|
| NTCP2   | XK            | no                | sí                |
| SSU2    | XK            | no                | sí                |
| Ratchet | IK            | no                | sí                |
| TBM     | N             | no                | no                |
| NetDB   | N             | no                | no                |
PQ KEM proporciona solo claves efímeras y no admite directamente handshakes de clave estática como Noise XK e IK.

Noise N no utiliza un intercambio de claves bidireccional y por lo tanto no es adecuado para el cifrado híbrido.

Por lo tanto, solo admitiremos cifrado híbrido, para NTCP2, SSU2 y Ratchet. Definiremos las tres variantes ML-KEM como en [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf), para un total de 3 nuevos tipos de cifrado. Los tipos híbridos solo se definirán en combinación con X25519.

Los nuevos tipos de cifrado son:

| Tipo | Código |
|------|--------|
| MLKEM512_X25519 | 5 |
| MLKEM768_X25519 | 6 |
| MLKEM1024_X25519 | 7 |
La sobrecarga será sustancial. Los tamaños típicos de mensaje 1 y 2 (para XK e IK) son actualmente de alrededor de 100 bytes (antes de cualquier carga útil adicional). Esto aumentará de 8x a 15x dependiendo del algoritmo.

### Firmas

Admitiremos firmas PQ e híbridas en las siguientes estructuras:

| Tipo | ¿Soporta solo PQ? | ¿Soporta Híbrido? |
|------|------------------|-------------------|
| RouterInfo | sí | sí |
| LeaseSet | sí | sí |
| Streaming SYN/SYNACK/Close | sí | sí |
| Repliable Datagrams | sí | sí |
| Datagram2 (prop. 163) | sí | sí |
| I2CP create session msg | sí | sí |
| Archivos SU3 | sí | sí |
| Certificados X.509 | sí | sí |
| Java keystores | sí | sí |
Por lo tanto, admitiremos tanto firmas solo PQ como híbridas. Definiremos las tres variantes ML-DSA como en [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf), tres variantes híbridas con Ed25519, y tres variantes solo PQ con prehash únicamente para archivos SU3, para un total de 9 nuevos tipos de firma. Los tipos híbridos solo se definirán en combinación con Ed25519. Utilizaremos el ML-DSA estándar, NO las variantes pre-hash (HashML-DSA), excepto para archivos SU3.

Utilizaremos la variante de firma "hedged" o aleatorizada, no la variante "determinística", como se define en [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) sección 3.4. Esto garantiza que cada firma sea diferente, incluso cuando se aplique sobre los mismos datos, y proporciona protección adicional contra ataques de canal lateral. Consulte la sección de notas de implementación más abajo para obtener detalles adicionales sobre las opciones de algoritmo, incluyendo la codificación y el contexto.

Los nuevos tipos de firma son:

| Tipo | Código |
|------|--------|
| MLDSA44 | 12 |
| MLDSA65 | 13 |
| MLDSA87 | 14 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 |
| MLDSA44ph | 18 |
| MLDSA65ph | 19 |
| MLDSA87ph | 20 |
Los certificados X.509 y otras codificaciones DER utilizarán las estructuras compuestas y OIDs definidos en [borrador IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/).

El overhead será sustancial. Los tamaños típicos de destino Ed25519 e identidad de router son de 391 bytes. Estos aumentarán de 3.5x a 6.8x dependiendo del algoritmo. Las firmas Ed25519 son de 64 bytes. Estas aumentarán de 38x a 76x dependiendo del algoritmo. Los RouterInfo firmados típicos, leaseSet, datagramas que pueden ser respondidos y mensajes de streaming firmados son de aproximadamente 1KB. Estos aumentarán de 3x a 8x dependiendo del algoritmo.

Como los nuevos tipos de identidad de destino y router no contendrán relleno, no serán comprimibles. Los tamaños de destinos e identidades de router que se comprimen con gzip en tránsito aumentarán entre 12x y 38x dependiendo del algoritmo.

### Combinaciones Legales

Para los Destinations, los nuevos tipos de firma son compatibles con todos los tipos de cifrado en el leaseset. Establece el tipo de cifrado en el certificado de clave como NONE (255).

Para RouterIdentities, el tipo de cifrado ElGamal está deprecado. Los nuevos tipos de firma solo son compatibles con cifrado X25519 (tipo 4). Los nuevos tipos de cifrado se indicarán en las RouterAddresses. El tipo de cifrado en el certificado de clave seguirá siendo tipo 4.

### Nuevo Crypto Requerido

- ML-KEM (anteriormente CRYSTALS-Kyber) [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
- ML-DSA (anteriormente CRYSTALS-Dilithium) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
- SHA3-128 (anteriormente Keccak-256) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf) Usado únicamente para SHAKE128
- SHA3-256 (anteriormente Keccak-512) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
- SHAKE128 y SHAKE256 (extensiones XOF a SHA3-128 y SHA3-256) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)

Los vectores de prueba para SHA3-256, SHAKE128 y SHAKE256 están disponibles en [NIST](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values).

Ten en cuenta que la biblioteca bouncycastle de Java soporta todo lo anterior. El soporte de la biblioteca C++ está en OpenSSL 3.5 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

### Alternativas

No daremos soporte a [FIPS 205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf) (Sphincs+), es mucho más lento y más grande que ML-DSA. No daremos soporte al próximo FIPS206 (Falcon), aún no está estandarizado. No daremos soporte a NTRU u otros candidatos PQ que no fueron estandarizados por NIST.

### Rosenpass

Existe un [artículo](https://eprint.iacr.org/2020/379.pdf) de investigación sobre la adaptación de Wireguard (IK) para criptografía PQ pura, pero hay varias preguntas abiertas en ese artículo. Posteriormente, este enfoque fue implementado como Rosenpass [Rosenpass](https://rosenpass.eu/) [documento técnico](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf) para PQ Wireguard.

Rosenpass utiliza un handshake similar a Noise KK con claves estáticas preshared de Classic McEliece 460896 (500 KB cada una) y claves efímeras Kyber-512 (esencialmente MLKEM-512). Como los textos cifrados de Classic McEliece son solo de 188 bytes, y las claves públicas y textos cifrados de Kyber-512 son razonables, ambos mensajes del handshake caben en un MTU UDP estándar. La clave compartida de salida (osk) del handshake PQ KK se usa como la clave preshared de entrada (psk) para el handshake IK estándar de Wireguard. Por lo tanto, hay dos handshakes completos en total, uno PQ puro y uno X25519 puro.

No podemos hacer nada de esto para reemplazar nuestros handshakes XK e IK porque:

- No podemos hacer KK, Bob no tiene la clave estática de Alice
- Las claves estáticas de 500KB son demasiado grandes
- No queremos un viaje de ida y vuelta adicional

Hay mucha información valiosa en el documento técnico, y lo revisaremos en busca de ideas e inspiración. PENDIENTE.

## Especificación

### Estructuras Comunes

Actualizar las secciones y tablas en el documento de estructuras comunes [/docs/specs/common-structures/](/docs/specs/common-structures/) de la siguiente manera:

### PublicKey

Los nuevos tipos de Clave Pública son:

| Tipo | Longitud de Clave Pública | Desde | Uso |
|------|---------------------------|-------|-----|
| MLKEM512_X25519 | 32 | 0.9.xx | Ver propuesta 169, solo para Leasesets, no para RIs o Destinations |
| MLKEM768_X25519 | 32 | 0.9.xx | Ver propuesta 169, solo para Leasesets, no para RIs o Destinations |
| MLKEM1024_X25519 | 32 | 0.9.xx | Ver propuesta 169, solo para Leasesets, no para RIs o Destinations |
| MLKEM512 | 800 | 0.9.xx | Ver propuesta 169, solo para handshakes, no para Leasesets, RIs o Destinations |
| MLKEM768 | 1184 | 0.9.xx | Ver propuesta 169, solo para handshakes, no para Leasesets, RIs o Destinations |
| MLKEM1024 | 1568 | 0.9.xx | Ver propuesta 169, solo para handshakes, no para Leasesets, RIs o Destinations |
| MLKEM512_CT | 768 | 0.9.xx | Ver propuesta 169, solo para handshakes, no para Leasesets, RIs o Destinations |
| MLKEM768_CT | 1088 | 0.9.xx | Ver propuesta 169, solo para handshakes, no para Leasesets, RIs o Destinations |
| MLKEM1024_CT | 1568 | 0.9.xx | Ver propuesta 169, solo para handshakes, no para Leasesets, RIs o Destinations |
| NONE | 0 | 0.9.xx | Ver propuesta 169, solo para destinations con tipos de firma PQ, no para RIs o Leasesets |
Las claves públicas híbridas son la clave X25519. Las claves públicas KEM son la clave PQ efímera enviada de Alice a Bob. La codificación y el orden de bytes están definidos en [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

Las claves MLKEM*_CT no son realmente claves públicas, son el "texto cifrado" enviado de Bob a Alice en el handshake de Noise. Se enumeran aquí por completitud.

### PrivateKey

Los nuevos tipos de Private Key son:

| Tipo | Longitud de Clave Privada | Desde | Uso |
|------|---------------------------|-------|-----|
| MLKEM512_X25519 | 32 | 0.9.xx | Ver propuesta 169, solo para Leasesets, no para RIs o Destinations |
| MLKEM768_X25519 | 32 | 0.9.xx | Ver propuesta 169, solo para Leasesets, no para RIs o Destinations |
| MLKEM1024_X25519 | 32 | 0.9.xx | Ver propuesta 169, solo para Leasesets, no para RIs o Destinations |
| MLKEM512 | 1632 | 0.9.xx | Ver propuesta 169, solo para handshakes, no para Leasesets, RIs o Destinations |
| MLKEM768 | 2400 | 0.9.xx | Ver propuesta 169, solo para handshakes, no para Leasesets, RIs o Destinations |
| MLKEM1024 | 3168 | 0.9.xx | Ver propuesta 169, solo para handshakes, no para Leasesets, RIs o Destinations |
Las claves privadas híbridas son las claves X25519. Las claves privadas KEM son solo para Alice. La codificación KEM y el orden de bytes están definidos en [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

### SigningPublicKey

Los nuevos tipos de Clave Pública de Firma son:

| Tipo | Longitud (bytes) | Desde | Uso |
|------|------------------|-------|-----|
| MLDSA44 | 1312 | 0.9.xx | Ver propuesta 169 |
| MLDSA65 | 1952 | 0.9.xx | Ver propuesta 169 |
| MLDSA87 | 2592 | 0.9.xx | Ver propuesta 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 1344 | 0.9.xx | Ver propuesta 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 1984 | 0.9.xx | Ver propuesta 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 2624 | 0.9.xx | Ver propuesta 169 |
| MLDSA44ph | 1344 | 0.9.xx | Solo para archivos SU3, no para estructuras netDb |
| MLDSA65ph | 1984 | 0.9.xx | Solo para archivos SU3, no para estructuras netDb |
| MLDSA87ph | 2624 | 0.9.xx | Solo para archivos SU3, no para estructuras netDb |
Las claves públicas de firma híbrida son la clave Ed25519 seguida de la clave PQ, como en el [borrador del IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/). La codificación y el orden de bytes se definen en [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf).

### SigningPrivateKey

Los nuevos tipos de Clave Privada de Firma son:

| Tipo | Longitud (bytes) | Desde | Uso |
|------|------------------|-------|-----|
| MLDSA44 | 2560 | 0.9.xx | Ver propuesta 169 |
| MLDSA65 | 4032 | 0.9.xx | Ver propuesta 169 |
| MLDSA87 | 4896 | 0.9.xx | Ver propuesta 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 2592 | 0.9.xx | Ver propuesta 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 4064 | 0.9.xx | Ver propuesta 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 4928 | 0.9.xx | Ver propuesta 169 |
| MLDSA44ph | 2592 | 0.9.xx | Solo para archivos SU3, no para estructuras netDb. Ver propuesta 169 |
| MLDSA65ph | 4064 | 0.9.xx | Solo para archivos SU3, no para estructuras netDb. Ver propuesta 169 |
| MLDSA87ph | 4928 | 0.9.xx | Solo para archivos SU3, no para estructuras netDb. Ver propuesta 169 |
Las claves privadas de firma híbrida son la clave Ed25519 seguida de la clave PQ, como en el [borrador IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/). La codificación y el orden de bytes se definen en [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf).

### Firma

Los nuevos tipos de Signature son:

| Tipo | Longitud (bytes) | Desde | Uso |
|------|------------------|-------|-----|
| MLDSA44 | 2420 | 0.9.xx | Ver propuesta 169 |
| MLDSA65 | 3309 | 0.9.xx | Ver propuesta 169 |
| MLDSA87 | 4627 | 0.9.xx | Ver propuesta 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 2484 | 0.9.xx | Ver propuesta 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 3373 | 0.9.xx | Ver propuesta 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 4691 | 0.9.xx | Ver propuesta 169 |
| MLDSA44ph | 2484 | 0.9.xx | Solo para archivos SU3, no para estructuras netDb. Ver propuesta 169 |
| MLDSA65ph | 3373 | 0.9.xx | Solo para archivos SU3, no para estructuras netDb. Ver propuesta 169 |
| MLDSA87ph | 4691 | 0.9.xx | Solo para archivos SU3, no para estructuras netDb. Ver propuesta 169 |
Las firmas híbridas son la firma Ed25519 seguida de la firma PQ, como en el [borrador IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/). Las firmas híbridas se verifican verificando ambas firmas, y fallan si cualquiera de las dos falla. La codificación y el orden de bytes se definen en [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf).

### Certificados de Clave

Los nuevos tipos de Signing Public Key son:

| Tipo | Código de Tipo | Longitud Total de Clave Pública | Desde | Uso |
|------|----------------|----------------------------------|-------|-----|
| MLDSA44 | 12 | 1312 | 0.9.xx | Ver propuesta 169 |
| MLDSA65 | 13 | 1952 | 0.9.xx | Ver propuesta 169 |
| MLDSA87 | 14 | 2592 | 0.9.xx | Ver propuesta 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 0.9.xx | Ver propuesta 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 0.9.xx | Ver propuesta 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 0.9.xx | Ver propuesta 169 |
| MLDSA44ph | 18 | n/a | 0.9.xx | Solo para archivos SU3 |
| MLDSA65ph | 19 | n/a | 0.9.xx | Solo para archivos SU3 |
| MLDSA87ph | 20 | n/a | 0.9.xx | Solo para archivos SU3 |
Los nuevos tipos de Clave Pública Criptográfica son:

| Tipo | Código de Tipo | Longitud Total de Clave Pública | Desde | Uso |
|------|----------------|----------------------------------|-------|-----|
| MLKEM512_X25519 | 5 | 32 | 0.9.xx | Ver propuesta 169, solo para Leasesets, no para RIs o Destinations |
| MLKEM768_X25519 | 6 | 32 | 0.9.xx | Ver propuesta 169, solo para Leasesets, no para RIs o Destinations |
| MLKEM1024_X25519 | 7 | 32 | 0.9.xx | Ver propuesta 169, solo para Leasesets, no para RIs o Destinations |
| NONE | 255 | 0 | 0.9.xx | Ver propuesta 169 |
Los tipos de clave híbridos NUNCA se incluyen en los certificados de clave; solo en los leaseSets.

Para destinos con tipos de firma Hybrid o PQ, usa NONE (tipo 255) para el tipo de cifrado, pero no hay clave criptográfica, y toda la sección principal de 384 bytes es para la clave de firma.

### Tamaños de destino

Aquí están las longitudes para los nuevos tipos de Destination. El tipo Enc para todos es NONE (tipo 255) y la longitud de la clave de cifrado se trata como 0. Toda la sección de 384 bytes se usa para la primera parte de la clave pública de firma. NOTA: Esto es diferente a la especificación para los tipos de firma ECDSA_SHA512_P521 y RSA, donde mantuvimos la clave ElGamal de 256 bytes en el destination aunque no se usara.

Sin relleno. La longitud total es 7 + longitud total de la clave. La longitud del certificado de clave es 4 + longitud excesiva de la clave.

Ejemplo de flujo de bytes de destino de 1319 bytes para MLDSA44:

skey[0:383] 5 (932 >> 8) (932 & 0xff) 00 12 00 255 skey[384:1311]

| Tipo | Código de Tipo | Longitud Total de Clave Pública | Principal | Exceso | Longitud Total de Destino |
|------|-----------|-------------------------|------|--------|-------------------|
| MLDSA44 | 12 | 1312 | 384 | 928 | 1319 |
| MLDSA65 | 13 | 1952 | 384 | 1568 | 1959 |
| MLDSA87 | 14 | 2592 | 384 | 2208 | 2599 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 384 | 960 | 1351 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 384 | 1600 | 1991 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 384 | 2240 | 2631 |
### Tamaños de RouterIdent

Aquí están las longitudes para los nuevos tipos de Destination. El tipo Enc para todos es X25519 (tipo 4). Toda la sección de 352 bytes después de la clave pública X28819 se usa para la primera parte de la clave pública de firma. Sin relleno. La longitud total es 39 + longitud total de clave. La longitud del certificado de clave es 4 + longitud excedente de clave.

Ejemplo de flujo de bytes de identidad de router de 1351 bytes para MLDSA44:

enckey[0:31] skey[0:351] 5 (960 >> 8) (960 & 0xff) 00 12 00 4 skey[352:1311]

| Tipo | Código de Tipo | Longitud Total de Clave Pública | Principal | Exceso | Longitud Total de RouterIdent |
|------|-----------|-------------------------|------|--------|--------------------------|
| MLDSA44 | 12 | 1312 | 352 | 960 | 1351 |
| MLDSA65 | 13 | 1952 | 352 | 1600 | 1991 |
| MLDSA87 | 14 | 2592 | 352 | 2240 | 2631 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 352 | 992 | 1383 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 352 | 1632 | 2023 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 352 | 2272 | 2663 |
### Patrones de Handshake

Los handshakes utilizan patrones de handshake del [Protocolo Noise](https://noiseprotocol.org/noise.html).

Se utiliza la siguiente correspondencia de letras:

- e = clave efímera de un solo uso
- s = clave estática
- p = carga útil del mensaje
- e1 = clave PQ efímera de un solo uso, enviada de Alice a Bob
- ekem1 = el texto cifrado KEM, enviado de Bob a Alice

Las siguientes modificaciones a XK e IK para el secreto hacia adelante híbrido (hfs) se especifican en la [especificación Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) sección 5:

```
XK:                       XKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, p               -> e, es, e1, p
  <- e, ee, p               <- e, ee, ekem1, p
  -> s, se                  -> s, se
  <- p                      <- p
  p ->                      p ->


  IK:                       IKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, s, ss, p       -> e, es, e1, s, ss, p
  <- tag, e, ee, se, p     <- tag, e, ee, ekem1, se, p
  <- p                     <- p
  p ->                     p ->

  e1 and ekem1 are encrypted. See pattern definitions below.
  NOTE: e1 and ekem1 are different sizes (unlike X25519)
```
El patrón e1 se define de la siguiente manera, según se especifica en la [especificación Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) sección 4:

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
El patrón ekem1 se define de la siguiente manera, según se especifica en la [especificación Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) sección 4:

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

#### Problemas

- ¿Deberíamos cambiar la función hash del handshake? Ver [comparación](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3).
  SHA256 no es vulnerable a PQ, pero si queremos actualizar
  nuestra función hash, ahora es el momento, mientras estamos cambiando otras cosas.
  La propuesta actual de SSH del IETF [borrador del IETF](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/) es usar MLKEM768
  con SHA256, y MLKEM1024 con SHA384. Esa propuesta incluye
  una discusión de las consideraciones de seguridad.
- ¿Deberíamos dejar de enviar datos de ratchet 0-RTT (aparte del LS)?
- ¿Deberíamos cambiar ratchet de IK a XK si no enviamos datos 0-RTT?

#### Descripción general

Esta sección se aplica tanto a los protocolos IK como XK.

El handshake híbrido está definido en la [especificación Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf). El primer mensaje, de Alice a Bob, contiene e1, la clave de encapsulación, antes de la carga útil del mensaje. Esto se trata como una clave estática adicional; llamar a EncryptAndHash() en ella (como Alice) o DecryptAndHash() (como Bob). Luego procesar la carga útil del mensaje como de costumbre.

El segundo mensaje, de Bob a Alice, contiene ekem1, el texto cifrado, antes de la carga útil del mensaje. Esto se trata como una clave estática adicional; llama EncryptAndHash() en ella (como Bob) o DecryptAndHash() (como Alice). Luego, calcula la kem_shared_key y llama MixKey(kem_shared_key). Después procesa la carga útil del mensaje como de costumbre.

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

Tenga en cuenta que tanto el encap_key como el texto cifrado están encriptados dentro de bloques ChaCha/Poly en los mensajes 1 y 2 del handshake Noise. Serán descifrados como parte del proceso de handshake.

El kem_shared_key se mezcla en la clave de encadenamiento con MixHash(). Ver más abajo para detalles.

#### KDF de Alice para el Mensaje 1

Para XK: Después del patrón de mensaje 'es' y antes de la carga útil, agregar:

O

Para IK: Después del patrón de mensaje 'es' y antes del patrón de mensaje 's', agregar:

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
#### Bob KDF para Mensaje 1

Para XK: Después del patrón de mensaje 'es' y antes de la carga útil, añadir:

O

Para IK: Después del patrón de mensaje 'es' y antes del patrón de mensaje 's', añadir:

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
#### KDF de Bob para el Mensaje 2

Para XK: Después del patrón de mensaje 'ee' y antes de la carga útil, agregar:

O

Para IK: Después del patrón de mensaje 'ee' y antes del patrón de mensaje 'se', agregar:

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

Después del patrón de mensaje 'ee' (y antes del patrón de mensaje 'ss' para IK), agregar:

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

### Ratchet

Actualiza la especificación ECIES-Ratchet [/docs/specs/ecies/](/docs/specs/ecies/) de la siguiente manera:

#### Identificadores de ruido

- "Noise_IKhfselg2_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_IKhfselg2_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_IKhfselg2_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1b) Nuevo formato de sesión (con vinculación)

Cambios: El ratchet actual contenía la clave estática en la primera sección ChaCha, y la carga útil en la segunda sección. Con ML-KEM, ahora hay tres secciones. La primera sección contiene la clave pública PQ cifrada. La segunda sección contiene la clave estática. La tercera sección contiene la carga útil.

Formato encriptado:

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   New Session Ephemeral Public Key    |
  +             32 bytes                  +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           ML-KEM encap_key            +
  |       ChaCha20 encrypted data         |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +    (MAC) for encap_key Section        +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           X25519 Static Key           +
  |       ChaCha20 encrypted data         |
  +             32 bytes                  +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +    (MAC) for Static Key Section       +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
```
Formato descifrado:

```
Payload Part 1:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +       ML-KEM encap_key                +
  |                                       |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 2:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +       X25519 Static Key               +
  |                                       |
  +      (32 bytes)                       +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 3:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |                                       |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Tamaños:

| Tipo | Código de Tipo | X len | Msg 1 len | Msg 1 Enc len | Msg 1 Dec len | PQ key len | pl len |
|------|-----------|-------|-----------|---------------|---------------|------------|--------|
| X25519 | 4 | 32 | 96+pl | 64+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 912+pl | 880+pl | 800+pl | 800 | pl |
| MLKEM768_X25519 | 6 | 32 | 1296+pl | 1360+pl | 1184+pl | 1184 | pl |
| MLKEM1024_X25519 | 7 | 32 | 1680+pl | 1648+pl | 1568+pl | 1568 | pl |
Ten en cuenta que la carga útil debe contener un bloque DateTime, por lo que el tamaño mínimo de la carga útil es 7. Los tamaños mínimos del mensaje 1 pueden calcularse en consecuencia.

#### 1g) Formato de respuesta de nueva sesión

Cambios: El ratchet actual tiene una carga útil vacía para la primera sección ChaCha, y la carga útil en la segunda sección. Con ML-KEM, ahora hay tres secciones. La primera sección contiene el texto cifrado PQ encriptado. La segunda sección tiene una carga útil vacía. La tercera sección contiene la carga útil.

Formato encriptado:

```
  +----+----+----+----+----+----+----+----+
  |       Session Tag   8 bytes           |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Ephemeral Public Key           +
  |                                       |
  +            32 bytes                   +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  | ChaCha20 encrypted ML-KEM ciphertext  |
  +      (see table below for length)     +
  ~                                       ~
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +  (MAC) for ciphertext Section         +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +  (MAC) for key Section (no data)      +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
```
Formato descifrado:

```
Payload Part 1:


  +----+----+----+----+----+----+----+----+
  |                                       |
  +       ML-KEM ciphertext               +
  |                                       |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 2:

  empty

  Payload Part 3:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |                                       |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Tamaños:

| Tipo | Código de Tipo | Y len | Msg 2 len | Msg 2 Enc len | Msg 2 Dec len | PQ CT len | opt len |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 72+pl | 32+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 856+pl | 816+pl | 768+pl | 768 | pl |
| MLKEM768_X25519 | 6 | 32 | 1176+pl | 1136+pl | 1088+pl | 1088 | pl |
| MLKEM1024_X25519 | 7 | 32 | 1656+pl | 1616+pl | 1568+pl | 1568 | pl |
Tenga en cuenta que aunque el mensaje 2 normalmente tendrá una carga útil distinta de cero, la especificación del ratchet [/docs/specs/ecies/](/docs/specs/ecies/) no lo requiere, por lo que el tamaño mínimo de carga útil es 0. Los tamaños mínimos del mensaje 2 pueden calcularse en consecuencia.

### NTCP2

Actualizar la especificación NTCP2 [/docs/specs/ntcp2/](/docs/specs/ntcp2/) de la siguiente manera:

#### Identificadores de Noise

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

Cambios: El NTCP2 actual contiene solo las opciones en la sección ChaCha. Con ML-KEM, la sección ChaCha también contendrá la clave pública PQ cifrada.

Para que PQ y NTCP2 no-PQ puedan ser soportados en la misma dirección y puerto del router, utilizamos el bit más significativo del valor X (clave pública efímera X25519) para marcar que es una conexión PQ. Este bit siempre está desactivado para conexiones no-PQ.

Para Alice, después de que el mensaje es encriptado por Noise, pero antes de la ofuscación AES de X, establecer X[31] |= 0x7f.

Para Bob, después de la des-ofuscación AES de X, probar X[31] & 0x80. Si el bit está establecido, limpiarlo con X[31] &= 0x7f, y descifrar vía Noise como una conexión PQ. Si el bit está limpio, descifrar vía Noise como una conexión no-PQ como de costumbre.

Para PQ NTCP2 anunciado en una dirección de router y puerto diferentes, esto no es necesario.

Para información adicional, consulte la sección Direcciones Publicadas a continuación.

Contenidos sin procesar:

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
Datos no cifrados (etiqueta de autenticación Poly1305 no mostrada):

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

Contenidos sin procesar:

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
Nota: Los códigos de tipo son solo para uso interno. Los routers permanecerán como tipo 4, y el soporte se indicará en las direcciones del router.

#### 3) SessionConfirmed

Sin cambios

#### Función de Derivación de Claves (KDF) (para la fase de datos)

Sin cambios

#### Direcciones Publicadas

En todos los casos, usa el nombre de transporte NTCP2 como es habitual.

Usar la misma dirección/puerto que el no-PQ, no cortafuegos. Solo se admite una variante PQ. En la dirección del router, publicar v=2 (como de costumbre) y el nuevo parámetro pq=[3|4|5] para indicar MLKEM 512/768/1024. Alice establece el MSB de la clave efímera (key[31] & 0x80) en la solicitud de sesión para indicar que esta es una conexión híbrida. Ver arriba. Los routers más antiguos ignorarán el parámetro pq y se conectarán no-pq como de costumbre.

No se admite una dirección/puerto diferente como no-PQ, o solo-PQ, sin firewall. Esto no se implementará hasta que NTCP2 no-PQ sea deshabilitado, dentro de varios años. Cuando no-PQ sea deshabilitado, se podrán admitir múltiples variantes PQ, pero solo una por dirección. En la dirección del router, publica v=[3|4|5] para indicar MLKEM 512/768/1024. Alice no establece el MSB de la clave efímera. Los routers más antiguos verificarán el parámetro v y omitirán esta dirección como no compatible.

Direcciones tras firewall (sin IP publicada): En la dirección del router, publique v=2 (como es habitual). No es necesario publicar un parámetro pq.

Alice puede conectarse a un Bob PQ utilizando la variante PQ que Bob publica, independientemente de si Alice anuncia soporte pq en su información de router, o si anuncia la misma variante.

#### Relleno Máximo

En la especificación actual, los mensajes 1 y 2 están definidos para tener una cantidad "razonable" de relleno, con un rango de 0-31 bytes recomendado, y sin máximo especificado.

Hasta la API 0.9.68 (versión 2.11.0), Java I2P implementaba un máximo de 256 bytes de relleno para conexiones que no son PQ, sin embargo esto no estaba documentado previamente. A partir de la API 0.9.69 (versión 2.12.0), Java I2P implementa el mismo relleno máximo para conexiones que no son PQ que para MLKEM-512. Ver tabla a continuación.

Usa el tamaño de mensaje definido como el relleno máximo, es decir, el relleno máximo duplicará el tamaño del mensaje para las conexiones PQ, de la siguiente manera:

| Relleno Máximo de Mensaje | no-PQ (hasta 0.9.68) | no-PQ (desde 0.9.69) | MLKEM-512 | MLKEM-768 | MLKEM-1024 |
|---------------------------|----------------------|----------------------|-----------|-----------|------------|
| Session Request  |   256   |   880   |    880   |     1264   |    1648  |
| Session Created  |   256   |   848   |    848   |     1136   |    1616  |
### SSU2

Actualiza la especificación SSU2 [/docs/specs/ssu2/](/docs/specs/ssu2/) de la siguiente manera:

#### Identificadores de ruido

- "Noise_XKhfschaobfse+hs1+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfschaobfse+hs1+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"

Tenga en cuenta que MLKEM-1024 NO es compatible con SSU2, ya que las claves son demasiado grandes para caber dentro de un datagrama estándar de 1500 bytes.

#### Cabecera Larga

El header largo tiene 32 bytes. Se utiliza antes de que se cree una sesión, para Token Request, SessionRequest, SessionCreated y Retry. También se usa para mensajes Peer Test y Hole Punch fuera de sesión.

En los siguientes mensajes, establece el campo ver (versión) en el encabezado largo a 3 o 4, para indicar MLKEM-512 o MLKEM-768.

- (0) Solicitud de Sesión
- (1) Sesión Creada
- (9) Reintentar
- (10) Solicitud de Token
- (11) Perforación de Agujero

En los siguientes mensajes, establece el campo ver (versión) en el encabezado largo a 2, como es habitual, incluso si MLKEM-512 o MLKEM-768 es compatible. Las implementaciones también pueden establecer el valor a 3 o 4, si el otro extremo lo soporta, pero esto no es necesario. Las implementaciones deben aceptar cualquier valor entre 2-4.

- (7) Prueba de Par (mensajes fuera de sesión 5-7)

Discusión: Establecer el campo de versión en 3 o 4 puede no ser estrictamente necesario para todos los tipos de mensajes, pero hacerlo ayuda a la detección temprana de fallos para conexiones post-cuánticas no compatibles. Token Request y Retry (tipos 9 y 10) deben tener versiones 3/4 por consistencia. Los mensajes Hole Punch (tipo 11) pueden no requerir este tratamiento pero seguiremos el mismo patrón por uniformidad. Los mensajes Peer Test (tipo 7) están fuera de sesión y no indican intención de iniciar una sesión.

Antes del cifrado del encabezado:

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

  ver :: The protocol version = 2, 3, or 4 for non-PQ, MLKEM512, MLKEM768

  id :: 1 byte, the network ID (currently 2, except for test networks)

  flag :: 1 byte, unused, set to 0 for future compatibility

  Source Connection ID :: 8 bytes, unsigned big endian integer

  Token :: 8 bytes, unsigned big endian integer

```
#### Encabezado Corto

sin cambios

#### SessionRequest (Tipo 0)

Cambios: El SSU2 actual contiene únicamente los datos del bloque en la sección ChaCha. Con ML-KEM, la sección ChaCha también contendrá la clave pública PQ cifrada.

Cambio de KDF para Protección contra Spoofing: Para abordar los problemas planteados en la Propuesta 165 [Prop165]_, pero con una solución diferente, modificamos el KDF para Session Request. Esto es solo para sesiones PQ. El KDF para sesiones no-PQ permanece sin cambios.

```

// End of KDF for initial chain key (unchanged)
  // Bob static key
  // MixHash(bpk)
  h = SHA256(h || bpk);

  // Start of KDF for session request
  // NEW for PQ only
  // bhash = Bob router hash (32 bytes)
  // MixHash(bhash)
  h = SHA256(h || bhash);

  // Rest of KDF for session request, unchanged, as in SSU2 spec
  // MixHash(header)
  h = SHA256(h || header)

  ...

```
Contenido sin procesar:

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
  |   ChaCha20 encrypted data (MLKEM)     |
  +          (length varies)              +
  |  k defined in KDF for Session Request |
  +  n = 0                                +
  |  see KDF for associated data          |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaCha20 encrypted data (payload)   |
  +          (length varies)              +
  |  k defined in KDF for Session Request |
  +  n = 0                                +
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
  |     Noise payload (block data)        |
  +          (length varies)              +
  |     see below for allowed blocks      |
  +----+----+----+----+----+----+----+----+
```
Tamaños, sin incluir la sobrecarga de IP:

| Tipo | Código de Tipo | X len | Msg 1 len | Msg 1 Enc len | Msg 1 Dec len | PQ key len | pl len |
|------|----------------|-------|-----------|---------------|---------------|------------|--------|
| X25519 | 4 | 32 | 80+pl | 16+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 896+pl | 832+pl | 800+pl | 800 | pl |
| MLKEM768_X25519 | 6 | 32 | 1280+pl | 1216+pl | 1184+pl | 1184 | pl |
| MLKEM1024_X25519 | 7 | n/a | demasiado grande | | | | |
Nota: Los códigos de tipo son solo para uso interno. Los routers permanecerán como tipo 4, y el soporte se indicará en las direcciones del router.

MTU mínimo para MLKEM768_X25519: 1318 para IPv4 y 1338 para IPv6. Ver abajo.

#### SessionCreated (Tipo 1)

Cambios: El SSU2 actual contiene solo los datos del bloque en la sección ChaCha. Con ML-KEM, la sección ChaCha también contendrá la clave pública PQ cifrada.

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
  |   ChaCha20 data (MLKEM)               |
  +   Encrypted and authenticated data    +
  |  length varies                        |
  +  k defined in KDF for Session Created +
  |  n = 0; see KDF for associated data   |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaCha20 data (payload)             |
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
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     Noise payload (block data)        |
  +          (length varies)              +
  |      see below for allowed blocks     |
  +----+----+----+----+----+----+----+----+
```
Tamaños, sin incluir la sobrecarga de IP:

| Tipo | Código de Tipo | Y len | Msg 2 len | Msg 2 Enc len | Msg 2 Dec len | PQ CT len | pl len |
|------|-----------|-------|-----------|---------------|---------------|-----------|--------|
| X25519 | 4 | 32 | 80+pl | 16+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 864+pl | 800+pl | 768+pl | 768 | pl |
| MLKEM768_X25519 | 6 | 32 | 1184+pl | 1118+pl | 1088+pl | 1088 | pl |
| MLKEM1024_X25519 | 7 | n/a | demasiado grande | | | | |
Nota: Los códigos de tipo son solo para uso interno. Los routers permanecerán como tipo 4, y el soporte se indicará en las direcciones del router.

MTU mínimo para MLKEM768_X25519: 1318 para IPv4 y 1338 para IPv6. Ver abajo.

#### SessionConfirmed (Tipo 2)

sin cambios

#### KDF para la fase de datos

sin cambios

#### Relay y Peer Test

Los siguientes bloques contienen campos de versión. Permanecerán en la versión 2 (para compatibilidad con un Bob no-PQ), y no cambiarán a la versión 3/4 para PQ.

- Solicitud de Relay
- Respuesta de Relay
- Introducción de Relay
- Prueba de Par

Firmas PQ: Los bloques Relay, bloques Peer Test y mensajes Peer Test contienen firmas. Desafortunadamente, las firmas PQ son más grandes que la MTU. No existe actualmente un mecanismo para fragmentar bloques Relay o Peer Test o mensajes a través de múltiples paquetes UDP. El protocolo debe extenderse para soportar fragmentación. Esto se hará en una propuesta separada por determinar. Hasta que eso se complete, Relay y Peer Test no serán soportados.

#### Direcciones Publicadas

En todos los casos, usa el nombre de transporte SSU2 como de costumbre. MLKEM-1024 no es compatible.

Usa la misma dirección/puerto que non-PQ, non-firewalled. Se admiten una o ambas variantes PQ. En la dirección del router, publica v=2 (como de costumbre) y el nuevo parámetro pq=[3|4|3,4|4,3] para indicar MLKEM 512/768/ambos. Los routers con una MTU menor que el mínimo especificado a continuación no deben publicar un parámetro "pq" que contenga "4". Publica 4,3 para indicar una preferencia por MLKEM-768 o 3,4 para indicar una preferencia por MLKEM-512. La versión real depende del iniciador, y la preferencia puede no ser respetada. Los routers con una MTU menor que el mínimo especificado a continuación no deben conectarse usando MLKEM768. Los routers más antiguos ignorarán el parámetro pq y se conectarán non-pq como de costumbre.

Dirección/puerto diferente como no-PQ, o solo-PQ, no-cortafuegos NO está soportado. Esto no se implementará hasta que SSU2 no-PQ sea deshabilitado, en varios años. Cuando no-PQ sea deshabilitado, una o ambas variantes PQ son soportadas. En la dirección del router, publicar v=[3|4|3,4|4,3] para indicar MLKEM 512/768/ambos. Los routers más antiguos verificarán el parámetro v y omitirán esta dirección como no soportada.

Direcciones con firewall (sin IP publicada): En la dirección del router, publicar v=2 (como es habitual). El parámetro pq DEBE ser publicado en direcciones con firewall, para soportar el relay.

Alice puede conectarse a un Bob PQ usando la variante PQ que Bob publica, independientemente de si Alice anuncia soporte pq en su información de router, o si anuncia la misma variante.

#### MTU

Ten cuidado de no exceder el MTU con MLKEM768. El MTU mínimo para MLKEM768_X25519 es 1318 para IPv4 y 1338 para IPv6 (asumiendo una carga útil mínima de 10 bytes con un bloque DateTime y un bloque Padding o RelayTagRequest). El MTU mínimo para SSU2 en general es 1280, por lo que no todos los peers pueden usar MLKEM768. No publiques ni uses MLKEM768 si el MTU real es menor que el mínimo, ya sea localmente o como lo anuncia el peer. Ten cuidado de no incluir un tamaño de padding tal que el mensaje 1 o 2 exceda el MTU local o remoto.

#### Problemas

Podríamos usar internamente el campo de versión y usar 3 para MLKEM512 y 4 para MLKEM768.

Para los mensajes 1 y 2, MLKEM768 aumentaría el tamaño de los paquetes más allá del MTU mínimo de 1280. Probablemente simplemente no lo soportaría para esa conexión si el MTU fuera demasiado bajo.

Para los mensajes 1 y 2, MLKEM1024 aumentaría el tamaño de los paquetes más allá del MTU máximo de 1500. Esto requeriría fragmentar los mensajes 1 y 2, y sería una gran complicación. Probablemente no lo haremos.

Relay y Peer Test: Ver arriba

### Streaming

TODO: ¿Hay una manera más eficiente de definir la firma/verificación para evitar copiar la firma?

### Archivos SU3

POR HACER

La sección 8.1 del [borrador IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/) prohíbe HashML-DSA en certificados X.509 y no asigna OIDs para HashML-DSA, debido a las complejidades de implementación y la seguridad reducida.

Para firmas únicamente PQ de archivos SU3, usa los OID definidos en el [borrador IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/) de las variantes sin pre-hash para los certificados. No definimos firmas híbridas de archivos SU3, porque podríamos tener que hacer hash de los archivos dos veces (aunque HashML-DSA y X2559 usan la misma función hash SHA512). Además, concatenar dos claves y firmas en un certificado X.509 sería completamente no estándar.

Ten en cuenta que no permitimos la firma Ed25519 de archivos SU3, y aunque hemos definido la firma Ed25519ph, nunca hemos acordado un OID para ella, ni la hemos usado.

Los tipos de firma normales no están permitidos para archivos SU3; usa las variantes ph (prehash).

### Otras Especificaciones

El nuevo tamaño máximo de Destination será de 2599 (3468 en base 64).

Actualizar otros documentos que ofrecen orientación sobre los tamaños de Destination, incluyendo:

- SAMv3
- Bittorrent
- Directrices para desarrolladores
- Nomenclatura / libreta de direcciones / servidores de salto
- Otros documentos

## Análisis de Sobrecarga

### Intercambio de Claves

Aumento de tamaño (bytes):

| Tipo | Pubkey (Msg 1) | Cipertext (Msg 2) |
|------|----------------|-------------------|
| MLKEM512_X25519 | +816 | +784 |
| MLKEM768_X25519 | +1200 | +1104 |
| MLKEM1024_X25519 | +1584 | +1584 |
Velocidad:

Velocidades según reporta [Cloudflare](https://blog.cloudflare.com/pq-2024/):

| Tipo | Velocidad relativa |
|------|-------------------|
| X25519 DH/keygen | línea base |
| MLKEM512 | 2.25x más rápido |
| MLKEM768 | 1.5x más rápido |
| MLKEM1024 | 1x (igual) |
| XK | 4x DH (keygen + 3 DH) |
| MLKEM512_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 4.9x DH = 22% más lento |
| MLKEM768_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 5.3x DH = 32% más lento |
| MLKEM1024_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 6x DH = 50% más lento |
Resultados preliminares de pruebas en Java:

| Tipo | DH/encaps relativo | DH/decaps | keygen |
|------|-------------------|-----------|--------|
| X25519 | línea base | línea base | línea base |
| MLKEM512 | 29x más rápido | 22x más rápido | 17x más rápido |
| MLKEM768 | 17x más rápido | 14x más rápido | 9x más rápido |
| MLKEM1024 | 12x más rápido | 10x más rápido | 6x más rápido |
### Firmas

Tamaño:

Tamaños típicos de clave, firma, RIdent, Dest o incrementos de tamaño (Ed25519 incluido como referencia) asumiendo tipo de cifrado X25519 para RIs. Tamaño agregado para un Router Info, LeaseSet, datagramas con respuesta, y cada uno de los dos paquetes de streaming (SYN y SYN ACK) listados. Los Destinations y Leasesets actuales contienen relleno repetido y son compresibles en tránsito. Los nuevos tipos no contienen relleno y no serán compresibles, resultando en un incremento de tamaño mucho mayor en tránsito. Ver sección de diseño arriba.

| Tipo | Pubkey | Sig | Key+Sig | RIdent | Dest | RInfo | LS/Streaming/Datagram (cada msg) |
|------|--------|-----|---------|--------|------|-------|----------------------------------|
| EdDSA_SHA512_Ed25519 | 32 | 64 | 96 | 391 | 391 | baseline | baseline |
| MLDSA44 | 1312 | 2420 | 3732 | 1351 | 1319 | +3316 | +3284 |
| MLDSA65 | 1952 | 3309 | 5261 | 1991 | 1959 | +5668 | +5636 |
| MLDSA87 | 2592 | 4627 | 7219 | 2631 | 2599 | +7072 | +7040 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 1344 | 2484 | 3828 | 1383 | 1351 | +3412 | +3380 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 1984 | 3373 | 5357 | 2023 | 1991 | +5668 | +5636 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 2624 | 4691 | 7315 | 2663 | 2631 | +7488 | +7456 |
Velocidad:

Velocidades según reporta [Cloudflare](https://blog.cloudflare.com/pq-2024/):

| Tipo | Signo de velocidad relativa | verificar |
|------|----------------------------|-----------|
| EdDSA_SHA512_Ed25519 | línea base | línea base |
| MLDSA44 | 5x más lento | 2x más rápido |
| MLDSA65 | ??? | ??? |
| MLDSA87 | ??? | ??? |
Resultados preliminares de pruebas en Java:

| Tipo | Signo de velocidad relativa | verificar | keygen |
|------|----------------------------|-----------|--------|
| EdDSA_SHA512_Ed25519 | línea base | línea base | línea base |
| MLDSA44 | 4.6x más lento | 1.7x más rápido | 2.6x más rápido |
| MLDSA65 | 8.1x más lento | igual | 1.5x más rápido |
| MLDSA87 | 11.1x más lento | 1.5x más lento | igual |
## Análisis de Seguridad

Las categorías de seguridad NIST se resumen en la [presentación NIST](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) diapositiva 10. Criterios preliminares: Nuestra categoría mínima de seguridad NIST debería ser 2 para protocolos híbridos y 3 para PQ únicamente.

| Categoría | Tan Seguro Como |
|----------|-----------------|
| 1 | AES128 |
| 2 | SHA256 |
| 3 | AES192 |
| 4 | SHA384 |
| 5 | AES256 |
### Protocolos de saludo

Todos estos son protocolos híbridos. Las implementaciones deberían preferir MLKEM768; MLKEM512 no es lo suficientemente seguro.

Categorías de seguridad NIST [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf):

| Algoritmo | Categoría de Seguridad |
|-----------|------------------------|
| MLKEM512 | 1 |
| MLKEM768 | 3 |
| MLKEM1024 | 5 |
### Firmas

Esta propuesta define tanto tipos de firma híbridos como solo PQ. El híbrido MLDSA44 es preferible al solo PQ MLDSA65. Los tamaños de claves y firmas para MLDSA65 y MLDSA87 probablemente son demasiado grandes para nosotros, al menos al principio.

Categorías de seguridad NIST [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf):

| Algoritmo | Categoría de Seguridad |
|-----------|------------------------|
| MLDSA44 | 2 |
| MLKEM67 | 3 |
| MLKEM87 | 5 |
## Preferencias de Tipo

Aunque definiremos e implementaremos 3 tipos de criptografía y 9 tipos de firma, planeamos medir el rendimiento durante el desarrollo y analizar más a fondo los efectos del aumento en el tamaño de las estructuras. También continuaremos investigando y monitoreando los desarrollos en otros proyectos y protocolos.

Después de un año o más de desarrollo intentaremos establecer un tipo preferido o predeterminado para cada caso de uso. La selección requerirá hacer compromisos entre ancho de banda, CPU y nivel de seguridad estimado. Es posible que no todos los tipos sean adecuados o estén permitidos para todos los casos de uso.

Las preferencias preliminares son las siguientes, sujetas a cambios:

Cifrado: MLKEM768_X25519

Firmas: MLDSA44_EdDSA_SHA512_Ed25519

Las restricciones preliminares son las siguientes, sujetas a cambios:

Cifrado: MLKEM1024_X25519 no permitido para SSU2

Firmas: MLDSA87 y variante híbrida probablemente demasiado grandes; MLDSA65 y variante híbrida pueden ser demasiado grandes

## Notas de Implementación

### Soporte de Bibliotecas

Las librerías Bouncycastle, BoringSSL y WolfSSL ahora soportan MLKEM y MLDSA. El soporte de OpenSSL estará en su versión 3.5 el 8 de abril de 2025 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

La biblioteca Noise de southernstorm.com adaptada por Java I2P contenía soporte preliminar para handshakes híbridos, pero lo eliminamos por no estar en uso; tendremos que agregarlo de vuelta y actualizarlo para que coincida con la [especificación Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf).

### Variantes de Firma

Utilizaremos la variante de firma "hedged" o aleatorizada, no la variante "determinística", como se define en [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) sección 3.4. Esto garantiza que cada firma sea diferente, incluso cuando se aplique sobre los mismos datos, y proporciona protección adicional contra ataques de canal lateral. Aunque [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) especifica que la variante "hedged" es la predeterminada, esto puede o no ser cierto en varias bibliotecas. Los implementadores deben asegurar que se use la variante "hedged" para la firma.

Utilizamos el proceso de firma normal (llamado Pure ML-DSA Signature Generation) que codifica el mensaje internamente como 0x00 || len(ctx) || ctx || message, donde ctx es algún valor opcional de tamaño 0x00..0xFF. No estamos utilizando ningún contexto opcional. len(ctx) == 0. Este proceso está definido en [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) Algoritmo 2 paso 10 y Algoritmo 3 paso 5. Ten en cuenta que algunos vectores de prueba publicados pueden requerir establecer un modo donde el mensaje no se codifica.

### Confiabilidad

El aumento de tamaño resultará en mucha más fragmentación de túnel para almacenes NetDB, intercambios de conexión de streaming y otros mensajes. Verifica los cambios en rendimiento y confiabilidad.

### Tamaños de Estructuras

Encuentra y verifica cualquier código que limite el tamaño en bytes de la información de router y leasesets.

### NetDB

Revisar y posiblemente reducir el máximo de LS/RI almacenados en RAM o en disco, para limitar el aumento de almacenamiento. ¿Aumentar los requisitos mínimos de ancho de banda para floodfills?

### Ratchet

#### Tunnels Compartidos

La clasificación/detección automática de múltiples protocolos en los mismos tunnels debería ser posible basándose en una verificación de longitud del mensaje 1 (New Session Message). Usando MLKEM512_X25519 como ejemplo, la longitud del mensaje 1 es 816 bytes mayor que el protocolo ratchet actual, y el tamaño mínimo del mensaje 1 (con solo una carga útil DateTime incluida) es de 919 bytes. La mayoría de los tamaños de mensaje 1 con ratchet actual tienen una carga útil menor a 816 bytes, por lo que pueden clasificarse como ratchet no híbrido. Los mensajes grandes probablemente son POSTs, que son raros.

Por lo tanto, la estrategia recomendada es:

- Si el mensaje 1 es menor de 919 bytes, es el protocolo ratchet actual.
- Si el mensaje 1 es mayor o igual a 919 bytes, probablemente es MLKEM512_X25519.
  Prueba MLKEM512_X25519 primero, y si falla, prueba el protocolo ratchet actual.

Esto debería permitirnos soportar eficientemente tanto el ratchet estándar como el ratchet híbrido en el mismo destino, tal como anteriormente soportábamos ElGamal y ratchet en el mismo destino. Por lo tanto, podemos migrar al protocolo híbrido MLKEM mucho más rápidamente que si no pudiéramos soportar protocolos duales para el mismo destino, porque podemos agregar soporte MLKEM a destinos existentes.

Las combinaciones compatibles requeridas son:

- X25519 + MLKEM512
- X25519 + MLKEM768
- X25519 + MLKEM1024

Las siguientes combinaciones pueden ser complejas y NO es necesario que sean compatibles, pero pueden serlo, dependiendo de la implementación:

- Más de un MLKEM
- ElG + uno o más MLKEM
- X25519 + uno o más MLKEM
- ElG + X25519 + uno o más MLKEM

Es posible que no intentemos soportar múltiples algoritmos MLKEM (por ejemplo, MLKEM512_X25519 y MLKEM_768_X25519) en el mismo destino. Elige solo uno; sin embargo, eso depende de que seleccionemos una variante MLKEM preferida, para que los túneles de cliente HTTP puedan usar una. Dependiente de la implementación.

PODEMOS intentar soportar tres algoritmos (por ejemplo X25519, MLKEM512_X25519, y MLKEM769_X25519) en el mismo destino. La clasificación y estrategia de reintento pueden ser demasiado complejas. La configuración y la interfaz de usuario de configuración pueden ser demasiado complejas. Dependiente de la implementación.

Probablemente NO intentaremos soportar algoritmos ElGamal e híbridos en el mismo destino. ElGamal está obsoleto, y ElGamal + híbrido únicamente (sin X25519) no tiene mucho sentido. Además, tanto los Mensajes de Nueva Sesión ElGamal como los Híbridos son grandes, por lo que las estrategias de clasificación a menudo tendrían que probar ambos descifrados, lo cual sería ineficiente. Dependiente de la implementación.

Los clientes pueden usar las mismas claves estáticas X25519 o claves diferentes para los protocolos X25519 e híbrido en los mismos túneles, dependiendo de la implementación.

#### Secreto Hacia Adelante

La especificación ECIES permite Garlic Messages en la carga útil del New Session Message, lo que permite la entrega 0-RTT del paquete de streaming inicial, usualmente un HTTP GET, junto con el leaseset del cliente. Sin embargo, la carga útil del New Session Message no tiene forward secrecy. Como esta propuesta enfatiza el forward secrecy mejorado para ratchet, las implementaciones pueden o deberían diferir la inclusión de la carga útil de streaming, o el mensaje de streaming completo, hasta el primer Existing Session Message. Esto sería a expensas de la entrega 0-RTT. Las estrategias también pueden depender del tipo de tráfico o tipo de tunnel, o en GET vs. POST, por ejemplo. Dependiente de la implementación.

#### Nuevo Tamaño de Sesión

MLKEM, MLDSA, o ambos en el mismo destino, aumentarán dramáticamente el tamaño del New Session Message, como se describe arriba. Esto puede disminuir significativamente la confiabilidad de la entrega del New Session Message a través de túneles, donde deben fragmentarse en múltiples mensajes de túnel de 1024 bytes. El éxito de la entrega es proporcional al número exponencial de fragmentos. Las implementaciones pueden usar varias estrategias para limitar el tamaño del mensaje, a expensas de la entrega 0-RTT. Dependiente de la implementación.

### NTCP2

Establecemos el MSB de la clave efímera (key[31] & 0x80) en la solicitud de sesión para indicar que esta es una conexión híbrida. Esto nos permite ejecutar tanto NTCP estándar como NTCP híbrido en el mismo puerto. Solo se soportaría una variante híbrida, y se anunciaría en la dirección del router. Por ejemplo, v=2,3 o v=2,4 o v=2,5.

#### Ofuscación

Como Alice, para una conexión PQ, antes de la ofuscación, establecer X[31] |= 0x80. Esto hace que X sea una clave pública X25519 inválida. Después de la ofuscación, AES-CBC la aleatorizará. El MSB de X será aleatorio después de la ofuscación.

Como Bob, prueba si (X[31] & 0x80) != 0 después de la des-ofuscación. Si es así, es una conexión PQ.

La versión mínima del router requerida para NTCP2-PQ está por determinar.

Nota: Los códigos de tipo son solo para uso interno. Los routers permanecerán como tipo 4, y el soporte se indicará en las direcciones del router.

### SSU2

Usamos el campo de versión en el encabezado largo y lo establecemos en 3 para MLKEM512 y 4 para MLKEM768. v=2,3,4 en la dirección sería suficiente.

Verificar y comprobar que SSU2 puede manejar RI firmado con MLDSA fragmentado a través de múltiples paquetes (¿6-8?).

Nota: Los códigos de tipo son solo para uso interno. Los routers permanecerán como tipo 4, y el soporte se indicará en las direcciones del router.

## Compatibilidad del Router

### Nombres de Transporte

En todos los casos, utiliza los nombres de transporte NTCP2 y SSU2 como de costumbre.

### Tipos de Cifrado del Router

Tenemos varias alternativas a considerar:

#### Routers Tipo 5/6/7

No recomendado. Usa únicamente los nuevos transportes listados arriba que coincidan con el tipo de router. Los routers más antiguos no pueden conectarse, construir túneles a través de, o enviar mensajes netDb hacia ellos. Tomaría varios ciclos de lanzamiento depurar y asegurar el soporte antes de habilitar por defecto. Podría extender el despliegue por un año o más sobre las alternativas de abajo.

#### Routers Tipo 4

Recomendado. Como PQ no afecta la clave estática X25519 o los protocolos de handshake N, podríamos dejar los routers como tipo 4, y simplemente anunciar nuevos transportes. Los routers más antiguos aún podrían conectarse, construir tunnels a través de ellos, o enviar mensajes netDb.

#### Recomendaciones

Se recomienda MLKEM-768 para Ratchet, NTCP2 y SSU2, como el mejor equilibrio entre seguridad y longitud de clave.

### Tipos de Firma del Router

#### Routers Tipo 12-17

Los routers más antiguos verifican los RIs y por lo tanto no pueden conectarse, construir túneles a través de ellos, o enviar mensajes netDb. Tomaría varios ciclos de lanzamiento depurar y asegurar el soporte antes de habilitarlo por defecto. Serían los mismos problemas que el despliegue de enc. type 5/6/7; podría extender el despliegue por un año o más sobre la alternativa de despliegue de enc. type 4 mencionada arriba.

No hay alternativas.

### Tipos de Cifrado LS

#### Claves LS Tipo 5-7

Estos pueden estar presentes en el LS con claves X25519 tipo 4 más antiguas. Los routers más antiguos ignorarán las claves desconocidas.

Los destinos pueden soportar múltiples tipos de claves, pero solo realizando desciframentos de prueba del mensaje 1 con cada clave. La sobrecarga puede mitigarse manteniendo conteos de desciframentos exitosos para cada clave, e intentando primero con la clave más utilizada. Java I2P utiliza esta estrategia para ElGamal+X25519 en el mismo destino.

### Tipos de Firma de Destino

#### Destinos Tipo 12-17

Los routers verifican las firmas de leaseSet y por lo tanto no pueden conectarse, o recibir leaseSets para destinos de tipo 12-17. Tomaría varios ciclos de lanzamiento depurar y garantizar el soporte antes de habilitarlo por defecto.

No hay alternativas.

## Prioridades y Despliegue

Los datos más valiosos son el tráfico extremo a extremo, cifrado con ratchet. Como observador externo entre saltos de túnel, está cifrado dos veces más, con cifrado de túnel y cifrado de transporte. Como observador externo entre OBEP e IBGW, está cifrado solo una vez más, con cifrado de transporte. Como participante OBEP o IBGW, ratchet es el único cifrado. Sin embargo, como los túneles son unidireccionales, capturar ambos mensajes en el handshake de ratchet requeriría routers que colaboren, a menos que los túneles se construyeran con el OBEP e IBGW en el mismo router.

El modelo de amenaza PQ más preocupante en este momento es el almacenamiento de tráfico hoy, para su descifrado dentro de muchos años (forward secrecy). Un enfoque híbrido protegería contra eso.

¿El modelo de amenaza PQ de romper las claves de autenticación en un período de tiempo razonable (digamos unos pocos meses) y luego suplantar la autenticación o descifrar en casi tiempo real, está mucho más lejos? Y ese es el momento en que querríamos migrar a claves estáticas PQC.

Por lo tanto, el modelo de amenaza PQ más temprano es que OBEP/IBGW almacenen tráfico para descifrado posterior. Deberíamos implementar el ratchet híbrido primero.

Ratchet tiene la prioridad más alta. Los transportes son los siguientes. Las firmas tienen la prioridad más baja.

El despliegue de firmas también será un año o más después que el despliegue de cifrado, porque no es posible la compatibilidad hacia atrás. Además, la adopción de MLDSA en la industria será estandarizada por el CA/Browser Forum y las Autoridades de Certificación. Las CA necesitan primero soporte de módulo de seguridad de hardware (HSM), que actualmente no está disponible [CA/Browser Forum](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/). Esperamos que el CA/Browser Forum impulse las decisiones sobre elecciones específicas de parámetros, incluyendo si soportar o requerir firmas compuestas [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/).

| Hito | Objetivo |
|-----------|--------|
| Ratchet beta | Finales de 2025 |
| Seleccionar mejor tipo de cifrado | Principios de 2026 |
| NTCP2 beta | Principios de 2026 |
| SSU2 beta | Mediados de 2026 |
| Ratchet producción | Mediados de 2026 |
| Ratchet por defecto | Finales de 2026 |
| Signature beta | Finales de 2026 |
| NTCP2 producción | Finales de 2026 |
| SSU2 producción | Principios de 2027 |
| Seleccionar mejor tipo de firma | Principios de 2027 |
| NTCP2 por defecto | Principios de 2027 |
| SSU2 por defecto | Mediados de 2027 |
| Signature producción | Mediados de 2027 |
## Migración

Si no podemos soportar tanto los protocolos de ratchet antiguos como los nuevos en los mismos tunnels, la migración será mucho más difícil.

Deberíamos poder simplemente probar uno-y-luego-el-otro, como hicimos con X25519, para ser probado.

## Problemas

- Selección de Hash Noise - ¿mantener SHA256 o actualizar?
  SHA256 debería ser bueno por otros 20-30 años, no está amenazado por PQ,
  Ver [presentación NIST](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf) y [presentación NCCOE](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf).
  Si SHA256 se rompe tenemos problemas peores (netdb).
- NTCP2 puerto separado, dirección de router separada
- SSU2 relay / prueba de par
- Campo de versión SSU2
- Versión de dirección de router SSU2

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
