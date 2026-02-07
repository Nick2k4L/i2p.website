---
title: "Especificación de Datagrama"
description: "Especificación de los formatos de mensaje de datagramas I2P incluyendo tipos sin procesar, respondibles y autenticados"
slug: "datagrams"
category: "Protocolos"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

## Descripción General

Consulta la [documentación de la API Datagrams](/docs/api/datagrams/) para obtener una descripción general de la API Datagrams.

Se definen los siguientes tipos. Se listan los números de protocolo estándar, sin embargo pueden utilizarse cualquier otros números de protocolo distintos al número de protocolo de streaming (6), específicos de la aplicación.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Protocol</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Repliable?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Authenticated?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Replay Prevention?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">As Of</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Raw</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
  </tbody>
</table>
El soporte para Datagram2 y Datagram3 en varias implementaciones de router y bibliotecas está por determinar. Consulta la documentación de esas implementaciones.

### Identificación de Tipo de Datagrama

Los cuatro tipos de datagramas no comparten una cabecera común con la versión del protocolo en el mismo lugar. Los paquetes no pueden identificarse por tipo basándose en su contenido. Al usar múltiples tipos en la misma sesión, o un solo tipo junto con streaming, las aplicaciones deben usar números de protocolo y/o puertos I2CP/SAM para enrutar los paquetes entrantes al lugar correcto. Usar números de protocolo estándar facilitará esto. No se recomienda dejar el número de protocolo sin establecer (0 o PROTO_ANY), incluso para una aplicación solo de datagramas, ya que aumenta la posibilidad de errores de enrutamiento y hace más difíciles las actualizaciones a una aplicación multi-protocolo. Los campos de versión en Datagram 2 y 3 se proporcionan solo como una verificación adicional para errores de enrutamiento y cambios futuros.

### Diseño de Aplicaciones

Todos los usos de datagramas son específicos de la aplicación.

Como los datagramas autenticados conllevan una sobrecarga considerable, una aplicación típica utiliza tanto datagramas autenticados como no autenticados. Un diseño típico es enviar un único datagrama autenticado que contenga un token del cliente al servidor. El servidor responde con un datagrama no autenticado que contiene el mismo token. Cualquier comunicación posterior, antes del vencimiento del token, utiliza datagramas sin procesar.

Las aplicaciones envían y reciben datagramas usando números de protocolo y puerto a través de la API [I2CP](/docs/specs/i2cp/) o [SAMv3](/docs/api/samv3/).

Los datagramas son, por supuesto, no confiables. Las aplicaciones deben diseñarse para entrega no confiable. Dentro de I2P, la entrega es confiable salto-a-salto si el siguiente salto es alcanzable, ya que los transportes NTCP2 y SSU2 proporcionan confiabilidad. Sin embargo, la entrega extremo-a-extremo no es confiable, ya que los mensajes I2NP pueden descartarse dentro de cualquier salto debido a límites de cola, expiraciones, tiempos de espera, límites de ancho de banda, o siguientes saltos inalcanzables.

### Tamaño del Datagrama

El límite de tamaño nominal para mensajes I2NP, incluyendo datagramas, es de 64 KB. La sobrecarga de mensajes garlic encryption y tunnel reduce esto un poco.

Sin embargo, todos los mensajes I2NP deben fragmentarse en mensajes de túnel de 1 KB. La probabilidad de descarte de un mensaje I2NP de n KB es la función exponencial de la probabilidad de descarte de un solo mensaje de túnel, p ** n. Como la fragmentación resulta en una ráfaga de mensajes de túnel, la probabilidad real de descarte es mucho mayor de lo que implicaría la función exponencial, debido a los límites de cola y la gestión activa de colas (AQM, CoDel o similar) en las implementaciones de router.

El tamaño máximo típico recomendado para asegurar una entrega confiable es de unos pocos KB, o como máximo 10 KB. Con un análisis cuidadoso de los tamaños de overhead en todas las capas del protocolo (excepto transporte), los desarrolladores deberían establecer un tamaño máximo de payload que encaje precisamente en uno, dos o tres tunnel messages. Esto maximizará la eficiencia y confiabilidad. El overhead en varias capas incluye el header gzip, header I2NP, header del mensaje garlic, garlic encryption, header del tunnel message, headers de fragmentación del tunnel message, y otros. Consulta los cálculos de MTU de streaming en [Proposal 144](/proposals/144-ecies-x25519-aead-ratchet/) y ConnectionOptions.java en el código fuente de Java I2P para ver ejemplos.

### Consideraciones de SAM

Las aplicaciones envían y reciben datagramas usando números de protocolo y puerto a través de la API I2CP o SAM. Especificar números de protocolo y puerto a través de SAM requiere SAM v3.2 o superior. Usar tanto datagramas como streaming (UDP y TCP) en la misma sesión SAM (tunnels) requiere SAM v3.3 o superior. Usar múltiples tipos de datagramas en la misma sesión SAM (tunnels) requiere SAM v3.3 o superior. SAM v3.3 solo está soportado por el router I2P de Java en este momento.

El soporte de SAM para Datagram2 y Datagram3 en varias implementaciones de router y bibliotecas está por determinarse. Consulta la documentación de esas implementaciones.

Ten en cuenta que los tamaños superiores a la MTU típica de red de 1500 bytes impedirán que las aplicaciones SAM transporten paquetes no fragmentados hacia/desde el servidor SAM, si la aplicación y el servidor están en computadoras separadas. Típicamente, este no es el caso, ambos están en localhost, donde la MTU es de 65536 o superior. Si se espera que una aplicación SAM esté separada en una computadora diferente del servidor, la carga útil máxima para un datagrama respondible es ligeramente inferior a 1 KB.

### Consideraciones PQ

Si se implementa la parte MLDSA de la [Propuesta 169](/proposals/169-pq-crypto/) Post-Cuántica, la sobrecarga aumentará considerablemente. El tamaño de un destino + firma aumentará de 391 + 64 = 455 bytes a un mínimo de 3739 para MLDSA44 y un máximo de 7226 para MLDSA87. Los efectos prácticos de esto están por determinarse. Datagram3, con autenticación proporcionada por el router, puede ser una solución.

## Datagramas Raw (No Respondibles) {#raw}

Los datagramas no respondibles no tienen dirección 'from' y no están autenticados. También se les llama datagramas "raw" (crudos). Hablando estrictamente, no son "datagramas" en absoluto, son solo datos crudos. No son manejados por la API de datagramas. Sin embargo, SAM y las clases I2PTunnel soportan "datagramas raw".

El número de protocolo I2CP estándar para datagramas raw es PROTO_DATAGRAM_RAW (18).

El formato no se especifica aquí, está definido por la aplicación. Para completar la información, incluimos una imagen del formato a continuación.

### Formato

```
+----+----+----+----+----//
| payload...
+----+----+----+----+----//

length: 0 - about 64 KB (see notes)
```
### Notas

La longitud práctica está limitada tanto por la sobrecarga en varias capas como por la confiabilidad.

## Datagram1 (Con respuesta) {#repliable}

Los datagramas replicables contienen una dirección 'from' y una firma. Estos agregan al menos 427 bytes de sobrecarga.

El número de protocolo I2CP estándar para datagramas con respuesta es PROTO_DATAGRAM (17).

### Formato

```
+----+----+----+----+----+----+----+----+
| from                                  |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+                                       +
|                                       |
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
| payload...
+----+----+----+----//

from :: a Destination
        length: 387+ bytes
        The originator and signer of the datagram

signature :: a Signature
             Signature type must match the signing public key type of $from
             length: 40+ bytes, as implied by the Signature type.
             For the default DSA_SHA1 key type:
                The DSA Signature of the SHA-256 hash of the payload.
             For other key types:
                The Signature of the payload.
             The signature may be verified by the signing public key of $from

payload :: The data
           Length: 0 to about 63 KB (see notes)

Total length: Payload length + 427+
```
### Notas

- La longitud práctica está limitada tanto por la sobrecarga en varias capas como por la confiabilidad.
- Consulta las notas importantes sobre la confiabilidad de datagramas grandes en la [documentación de la API de Datagramas](/docs/api/datagrams/). Para obtener mejores resultados, limita la carga útil a aproximadamente 10 KB o menos.
- Las firmas para tipos distintos de DSA_SHA1 fueron redefinidas en la versión 0.9.14.
- El formato no admite la inclusión de un bloque de firma offline para LS2 (propuesta 123). Se debe definir un nuevo protocolo con flags para eso.

## Datagram2 {#datagram2}

El formato Datagram2 está especificado según la [Propuesta 163](/proposals/163-datagram2/). El número de protocolo I2CP para Datagram2 es 19.

Datagram2 está diseñado como un reemplazo para Datagram1. Añade las siguientes características a Datagram1:

- Prevención de reproducción
- Soporte para firmas sin conexión
- Campos de banderas y opciones para extensibilidad

Ten en cuenta que el algoritmo de cálculo de firma para Datagram2 es sustancialmente diferente al de Datagram1.

### Formato

```
+----+----+----+----+----+----+----+----+
|                                       |
~            from                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~     offline_signature (optional)      ~
~   expires, sigtype, pubkey, offsig    ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            signature                  ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

from :: a Destination
        length: 387+ bytes
        The originator and (unless offline signed) signer of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x02 (0 0 1 0)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bit 5: If 0, no offline sig; if 1, offline signed
         Bits 15-6: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

offline_signature ::
             If flag indicates offline keys, the offline signature section,
             as specified in the Common Structures Specification,
             with the following 4 fields. Length: varies by online and offline
             sig types, typically 102 bytes for Ed25519
             This section can, and should, be generated offline.

  expires :: Expires timestamp
             (4 bytes, big endian, seconds since epoch, rolls over in 2106)

  sigtype :: Transient sig type (2 bytes, big endian)

  pubkey :: Transient signing public key (length as implied by sig type),
            typically 32 bytes for Ed25519 sig type.

  offsig :: a Signature
            Signature of expires timestamp, transient sig type,
            and public key, by the destination public key,
            length: 40+ bytes, as implied by the Signature type, typically
            64 bytes for Ed25519 sig type.

payload :: The data
           Length: 0 to about 61 KB (see notes)

signature :: a Signature
             Signature type must match the signing public key type of $from
             (if no offline signature) or the transient sigtype
             (if offline signed)
             length: 40+ bytes, as implied by the Signature type, typically
             64 bytes for Ed25519 sig type.
             The Signature of the payload and other fields as specified below.
             The signature is verified by the signing public key of $from
             (if no offline signature) or the transient pubkey
             (if offline signed)
```
Longitud total: mínimo 433 + longitud de la carga útil; longitud típica para remitentes X25519 y sin firmas offline: 457 + longitud de la carga útil. Ten en cuenta que el mensaje será típicamente comprimido con gzip en la capa I2CP, lo que resultará en ahorros significativos si el destino de origen es compresible.

Nota: El formato de firma fuera de línea es el mismo que en la [Especificación de Estructuras Comunes](/docs/specs/common-structures/) y la [Especificación de Streaming](/docs/specs/streaming/).

### Firmas

La firma abarca los siguientes campos:

- Preámbulo: El hash de 32 bytes del destino objetivo (no incluido en el datagrama)
- flags
- options (si está presente)
- offline_signature (si está presente)
- payload

En el datagrama con respuesta, para el tipo de clave DSA_SHA1, la firma estaba sobre el hash SHA-256 de la carga útil, no sobre la carga útil en sí; aquí, la firma siempre está sobre los campos anteriores (NO el hash), independientemente del tipo de clave.

### Verificación de ToHash

Los receptores deben verificar la firma (usando el hash de su destino) y descartar el datagrama en caso de fallo, para prevenir ataques de repetición.

## Datagram3 {#datagram3}

El formato Datagram3 está especificado en [Propuesta 163](/proposals/163-datagram2/). El número de protocolo I2CP para Datagram3 es 20.

Datagram3 está diseñado como una versión mejorada de los datagramas en bruto. Añade las siguientes características a los datagramas en bruto:

- Replicabilidad
- Campos de banderas y opciones para extensibilidad

Datagram3 NO está autenticado. En una propuesta futura, la autenticación puede ser proporcionada por la capa ratchet del router, y el estado de autenticación sería pasado al cliente.

### Formato

```
+----+----+----+----+----+----+----+----+
|                                       |
~            fromhash                   ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

fromhash :: a Hash
            length: 32 bytes
            The originator of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x03 (0 0 1 1)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bits 15-5: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

payload :: The data
           Length: 0 to about 61 KB (see notes)
```
Longitud total: mínimo 34 + longitud de la carga útil.

## Referencias

- [Common](/docs/specs/common-structures/) - Especificación de Estructuras Comunes
- [DATAGRAMS](/docs/api/datagrams/) - Resumen de la API de Datagramas
- [I2CP](/docs/specs/i2cp/) - Especificación I2CP
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet/) - Propuesta ECIES-X25519-AEAD-Ratchet
- [Prop163](/proposals/163-datagram2/) - Propuesta Datagram2 y Datagram3
- [Prop169](/proposals/169-pq-crypto/) - Propuesta de Criptografía Post-Cuántica
- [SAMv3](/docs/api/samv3/) - Especificación SAM v3
- [Streaming](/docs/specs/streaming/) - Especificación de Streaming
- [TRANSPORT](/docs/overview/transport/) - Resumen de Transporte
- [TUNMSG](/docs/specs/tunnel-message/#notes) - Especificación de Mensajes de Túnel
