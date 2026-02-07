---
title: "Especificación del Protocolo de Streaming"
description: "Especificación para el protocolo de streaming de I2P que proporciona transporte confiable similar a TCP"
slug: "streaming"
category: "Protocolos"
lastUpdated: "2023-10"
accurateFor: "0.9.59"
---

## Resumen

Consulta [Streaming Library](/docs/api/streaming) para obtener una descripción general del protocolo Streaming.

## Versiones de Protocolo

El protocolo de streaming no incluye un campo de versión. Las versiones listadas a continuación son para Java I2P. Las implementaciones y el soporte criptográfico real pueden variar. No hay forma de determinar si el extremo remoto soporta alguna versión o característica en particular. La tabla a continuación es para orientación general sobre las fechas de lanzamiento de varias características.

Las características listadas a continuación son para el protocolo en sí. Varias opciones de configuración están documentadas en la [Streaming Library](/docs/api/streaming) junto con la versión de Java I2P en la que fueron implementadas.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Router Version</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Streaming Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Bob's hash in NACKs field of SYN packet</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE option</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">I2CP protocol number enforced</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED no longer required in RESET</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PINGs and PONGs may include a payload</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA Ed25519 sig type</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA P-256, P-384, and P-521 sig types</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Variable-length signatures</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.7.1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Protocol numbers defined in I2CP</td>
    </tr>
  </tbody>
</table>
## Especificación del Protocolo

### Formato de Paquete

El formato de un solo paquete en el protocolo de streaming se muestra a continuación. El tamaño mínimo del encabezado, sin NACKs o datos de opciones, es de 22 bytes.

No hay un campo de longitud en el protocolo de streaming. El encuadre es proporcionado por las capas inferiores - I2CP e I2NP.

```
+----+----+----+----+----+----+----+----+
| send Stream ID    | rcv Stream ID     |
+----+----+----+----+----+----+----+----+
| sequence  Num     | ack Through       |
+----+----+----+----+----+----+----+----+
| nc |  nc*4 bytes of NACKs (optional)
+----+----+----+----+----+----+----+----+
     | rd |  flags  | opt size| opt data
+----+----+----+----+----+----+----+----+
   ...  (optional, see below)           |
+----+----+----+----+----+----+----+----+
|   payload ...
+----+----+----+-//
```
**sendStreamId** :: 4 byte [Integer](/docs/specs/common-structures#integer) : Número aleatorio seleccionado por el destinatario del paquete antes de enviar el primer paquete de respuesta SYN y constante durante la vida de la conexión, mayor que cero. 0 en el mensaje SYN enviado por el originador de la conexión, y en mensajes posteriores, hasta que se reciba una respuesta SYN, que contiene el ID de stream del peer.

**receiveStreamId** :: 4 bytes [Integer](/docs/specs/common-structures#integer) : Número aleatorio seleccionado por el originador del paquete antes de enviar el primer paquete SYN y constante durante toda la vida de la conexión, mayor que cero. Puede ser 0 si es desconocido, por ejemplo en un paquete RESET.

**sequenceNum** :: 4 bytes [Integer](/docs/specs/common-structures#integer) : La secuencia para este mensaje, comenzando en 0 en el mensaje SYN, e incrementándose en 1 en cada mensaje excepto para ACKs simples y retransmisiones. Si el sequenceNum es 0 y la bandera SYN no está establecida, este es un paquete ACK simple que no debería ser confirmado con ACK.

**ackThrough** :: 4 byte [Integer](/docs/specs/common-structures#integer) : El número de secuencia de paquete más alto que fue recibido en el receiveStreamId. Este campo se ignora en el paquete de conexión inicial (donde receiveStreamId es el id desconocido) o si está establecida la bandera NO_ACK. Todos los paquetes hasta e incluyendo este número de secuencia son confirmados (ACKed), EXCEPTO aquellos listados en los NACKs a continuación.

**Recuento de NACK** :: 1 byte [Integer](/docs/specs/common-structures#integer) : El número de NACKs de 4 bytes en el siguiente campo, u 8 cuando se usa junto con SYNCHRONIZE para prevención de repetición desde la versión 0.9.58; ver más abajo.

**NACKs** :: nc * 4 bytes [Integer](/docs/specs/common-structures#integer)s : Números de secuencia menores que ackThrough que aún no se han recibido. Dos NACKs de un paquete es una solicitud para una 'retransmisión rápida' de ese paquete. También se usa junto con SYNCHRONIZE para prevención de repetición desde la versión 0.9.58; ver más abajo.

**resendDelay** :: 1 byte [Integer](/docs/specs/common-structures#integer) : Cuánto tiempo va a esperar el creador de este paquete antes de reenviar este paquete (si aún no ha sido confirmado con ACK). El valor son segundos desde que se creó el paquete. Actualmente se ignora al recibir.

**flags** :: valor de 2 bytes : Ver más abajo.

**option size** :: [Integer](/docs/specs/common-structures#integer) de 2 bytes : El número de bytes en el siguiente campo

**datos de opción** :: 0 o más bytes : Según se especifica en las flags. Ver más abajo.

**payload** :: tamaño restante del paquete

### Campos de Banderas y Datos de Opciones

El campo de flags anterior especifica algunos metadatos sobre el paquete, y a su vez puede requerir que se incluyan ciertos datos adicionales. Los flags son los siguientes. Cualquier estructura de datos especificada debe agregarse al área de opciones en el orden dado.

Orden de bits: 15....0 (15 es MSB)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Flag</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Order</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SYNCHRONIZE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP SYN. Set in the initial packet and in the first response. FROM_INCLUDED and SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">CLOSE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP FIN. If the response to a SYNCHRONIZE fits in a single message, the response will contain both SYNCHRONIZE and CLOSE. SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RESET</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Abnormal close. SIGNATURE_INCLUDED must also be set. Prior to release 0.9.20, due to a bug, FROM_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#signature">Signature</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, CLOSE, and RESET, where it is required, and with ECHO, where it is required for a ping. The signature uses the Destination's <a href="/docs/specs/common-structures#signingprivatekey">SigningPrivateKey</a> to sign the entire header and payload with the space in the option data field for the signature being set to all zeroes. Prior to release 0.9.11, the signature was always 40 bytes. As of release 0.9.11, the signature may be variable-length, see below for details.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused. Requests every packet in the other direction to have SIGNATURE_INCLUDED</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">387+ byte <a href="/docs/specs/common-structures#destination">Destination</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, where it is required, and with ECHO, where it is required for a ping. Prior to release 0.9.20, due to a bug, must also be sent with RESET.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DELAY_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Optional delay. How many milliseconds the sender of this packet wants the recipient to wait before sending any more data. A value greater than 60000 indicates choking. A value of 0 requests an immediate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MAX_PACKET_SIZE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum length of the payload. Send with SYNCHRONIZE.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PROFILE_INTERACTIVE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused or ignored; the interactive profile is unimplemented.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECHO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused except by ping programs. If set, most other options are ignored. See the <a href="/docs/api/streaming">streaming docs</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">NO_ACK</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">This flag simply tells the recipient to ignore the ackThrough field in the header. Currently set in the initial SYN packet, otherwise the ackThrough field is always valid. Note that this does not save any space, the ackThrough field is before the flags and is always present.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#offlinesignature">OfflineSig</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Contains the offline signature section from LS2. See proposal 123 and the common structures specification. FROM_INCLUDED must also be set. Contains an OfflineSig: 1) Expires timestamp (4 bytes, seconds since epoch, rolls over in 2106) 2) Transient sig type (2 bytes) 3) Transient <a href="/docs/specs/common-structures#signingpublickey">SigningPublicKey</a> (length as implied by sig type) 4) <a href="/docs/specs/common-structures#signature">Signature</a> of expires timestamp, transient sig type, and public key, by the destination public key. Length of sig as implied by the destination public key sig type.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12-15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">unused</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Set to zero for compatibility with future uses.</td>
    </tr>
  </tbody>
</table>
### Notas sobre Firmas de Longitud Variable

Antes de la versión 0.9.11, la firma en el campo de opción siempre era de 40 bytes.

A partir de la versión 0.9.11, la signature tiene longitud variable. El tipo y longitud de la Signature se infieren del tipo de clave utilizada en la opción FROM_INCLUDED y la documentación de [Signature](/docs/specs/common-structures#signature).

A partir de la versión 0.9.39, se admite la opción OFFLINE_SIGNATURE. Si esta opción está presente, se utiliza la [SigningPublicKey](/docs/specs/common-structures#signingpublickey) transitoria para verificar cualquier paquete firmado, y la longitud y tipo de firma se infieren de la SigningPublicKey transitoria en la opción.

- Cuando un paquete contiene tanto FROM_INCLUDED como SIGNATURE_INCLUDED (como en SYNCHRONIZE), la inferencia puede hacerse directamente.

- Cuando un paquete no contiene FROM_INCLUDED, la inferencia debe hacerse a partir de un paquete SYNCHRONIZE anterior.

- Cuando un paquete no contiene FROM_INCLUDED, y no hubo un paquete SYNCHRONIZE anterior (por ejemplo, un paquete CLOSE o RESET perdido), la inferencia se puede hacer desde la longitud de las opciones restantes (ya que SIGNATURE_INCLUDED es la última opción), pero el paquete probablemente será descartado de todos modos, ya que no hay FROM disponible para validar la firma. Si se definen más campos de opción en el futuro, deben ser considerados.

### Prevención de Reproducción

Para evitar que Bob use un ataque de repetición almacenando un paquete SYNCHRONIZE firmado válido recibido de Alice y enviándolo posteriormente a una víctima Charlie, Alice debe incluir el hash de destino de Bob en el paquete SYNCHRONIZE de la siguiente manera:

```
Set NACK count field to 8
Set the NACKs field to Bob's 32-byte destination hash
```
Al recibir un SYNCHRONIZE, si el campo de conteo NACK es 8, Bob debe interpretar el campo NACKs como un hash de destino de 32 bytes, y debe verificar que coincida con su hash de destino. También debe verificar la firma del paquete como de costumbre, ya que esto cubre todo el paquete incluyendo los campos de conteo NACK y NACKs. Si el conteo NACK es 8 y el campo NACKs no coincide, Bob debe descartar el paquete.

Esto es requerido para las versiones 0.9.58 y superiores. Esto es compatible hacia atrás con versiones anteriores, porque los NACKs no se esperan en un paquete SYNCHRONIZE. Los destinos no saben y no pueden saber qué versión está ejecutando el otro extremo.

No es necesario realizar cambios en el paquete SYNCHRONIZE ACK enviado de Bob a Alice; no incluyas NACKs en ese paquete.

## Referencias

- **[Destination]** [Destination](/docs/specs/common-structures#destination)
- **[Integer]** [Integer](/docs/specs/common-structures#integer)
- **[OfflineSig]** [OfflineSignature](/docs/specs/common-structures#offlinesignature)
- **[Signature]** [Signature](/docs/specs/common-structures#signature)
- **[SigningPrivateKey]** [SigningPrivateKey](/docs/specs/common-structures#signingprivatekey)
- **[SigningPublicKey]** [SigningPublicKey](/docs/specs/common-structures#signingpublickey)
- **[STREAMING]** [Biblioteca de Streaming](/docs/api/streaming)
