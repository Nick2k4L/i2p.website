---
title: "B32 para Encrypted LeaseSet"
description: "Formato de dirección Base 32 para leasesets LS2 cifrados"
slug: "b32encrypted"
category: "Diseño"
lastUpdated: "2020-08"
accurateFor: "0.9.47"
---

## Descripción general

Las direcciones estándar Base 32 ("b32") contienen el hash del destino. Esto no funcionará para ls2 encriptado (propuesta 123).

No podemos usar una dirección base 32 tradicional para un LS2 cifrado (propuesta 123), ya que contiene solo el hash del destino. No proporciona la clave pública no ciega. Los clientes deben conocer la clave pública del destino, el tipo de firma, el tipo de firma ciega, y una clave secreta u opcional privada para obtener y descifrar el leaseset. Por lo tanto, una dirección base 32 por sí sola es insuficiente. El cliente necesita ya sea el destino completo (que contiene la clave pública), o la clave pública por sí misma. Si el cliente tiene el destino completo en una libreta de direcciones, y la libreta de direcciones soporta búsqueda inversa por hash, entonces la clave pública puede ser recuperada.

Este formato coloca la clave pública en lugar del hash en una dirección base32. Este formato también debe contener el tipo de firma de la clave pública y el tipo de firma del esquema de ocultamiento.

Este documento especifica un formato b32 para estas direcciones. Aunque hemos hecho referencia a este nuevo formato durante las discusiones como una dirección "b33", el nuevo formato real conserva el sufijo habitual ".b32.i2p".

## Diseño

- El nuevo formato contendrá la clave pública sin cegar, el tipo de firma sin cegar,
  y el tipo de firma cegada.
- Opcionalmente contendrá una clave secreta y/o privada, solo para enlaces privados
- Usar el sufijo ".b32.i2p" existente, pero con una longitud mayor.
- Añadir una suma de verificación.
- Las direcciones para leasesets cifrados se identifican por 56 o más
  caracteres codificados (35 o más bytes decodificados), comparado con 52 caracteres (32
  bytes) para las direcciones base 32 tradicionales.

## Especificación

### Creación y codificación

Construye un nombre de host de {56+ caracteres}.b32.i2p (35+ caracteres en binario) de la siguiente manera:

```
flag (1 byte)
    bit 0: 0 for one-byte sigtypes, 1 for two-byte sigtypes
    bit 1: 0 for no secret, 1 if secret is required
    bit 2: 0 for no per-client auth, 1 if client private key is required
    bits 7-3: Unused, set to 0

public key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

blinded key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

public key
    Number of bytes as implied by sigtype
```
Post-procesamiento y suma de verificación:

```
Construct the binary data as above.
Treat checksum as little-endian.
Calculate checksum = CRC-32(data[3:end])
data[0] ^= (byte) checksum
data[1] ^= (byte) (checksum >> 8)
data[2] ^= (byte) (checksum >> 16)

hostname = Base32.encode(data) || ".b32.i2p"
```
Cualquier bit no utilizado al final del b32 debe ser 0. No hay bits no utilizados para una dirección estándar de 56 caracteres (35 bytes).

### Decodificación y Verificación

```
strip the ".b32.i2p" from the hostname
data = Base32.decode(hostname)
Calculate checksum = CRC-32(data[3:end])
Treat checksum as little-endian.
flags = data[0] ^ (byte) checksum
if 1 byte sigtypes:
    pubkey sigtype = data[1] ^ (byte) (checksum >> 8)
    blinded sigtype = data[2] ^ (byte) (checksum >> 16)
else (2 byte sigtypes):
    pubkey sigtype = data[1] ^ ((byte) (checksum >> 8)) || data[2] ^ ((byte) (checksum >> 16))
    blinded sigtype = data[3] || data[4]
parse the remainder based on the flags to get the public key
```
### Bits de Clave Secreta y Privada

Los bits de clave secreta y privada se utilizan para indicar a los clientes, proxies u otro código del lado del cliente que se requerirá la clave secreta y/o privada para descifrar el leaseset. Las implementaciones particulares pueden solicitar al usuario que proporcione los datos requeridos, o rechazar los intentos de conexión si faltan los datos requeridos.

## Almacenamiento en caché

Aunque esté fuera del alcance de esta especificación, los routers y/o clientes deben recordar y almacenar en caché (probablemente de forma persistente) la correspondencia entre clave pública y destino, y viceversa.

## Notas

- Distinguir los tipos antiguos de los nuevos por longitud. Las direcciones b32 antiguas son
  siempre {52 caracteres}.b32.i2p. Las nuevas son {56+ caracteres}.b32.i2p
- Hilo de discusión de Tor:
  https://lists.torproject.org/pipermail/tor-dev/2017-January/011816.html
- No esperes que los sigtypes de 2 bytes lleguen a ocurrir, solo llegamos hasta 13. No es
  necesario implementar ahora.
- El nuevo formato puede usarse en enlaces de salto (y ser servido por servidores de salto) si
  se desea, igual que b32.

## Referencias

- [CRC-32](https://en.wikipedia.org/wiki/CRC-32) - ver también [RFC 3309](https://tools.ietf.org/html/rfc3309)
