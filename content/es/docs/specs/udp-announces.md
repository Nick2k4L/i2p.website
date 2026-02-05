---
title: "Trackers UDP"
description: "Especificación de protocolo para anuncios UDP BitTorrent en I2P"
slug: "udp-announces"
category: "Protocolos"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

## Resumen

Esta especificación documenta el protocolo para anuncios UDP de bittorrent en I2P. Para la especificación general de bittorrent en I2P, consulte [BitTorrent over I2P](/docs/applications/bittorrent). Para antecedentes e información adicional sobre el desarrollo de esta especificación, consulte [Proposal 160](/proposals/160-udp-trackers).

## Diseño

Esta propuesta utiliza repliable datagram2, repliable datagram3, y raw datagrams, tal como se define en [Datagrams](/docs/specs/datagrams). Datagram2 y Datagram3 son nuevas variantes de repliable datagrams, definidas en [Proposal 163](/proposals/163-datagram2-datagram3). Datagram2 añade resistencia a la repetición y soporte para firma fuera de línea. Datagram3 es más pequeño que el formato de datagrama antiguo, pero sin autenticación.

### BEP 15

Para referencia, el flujo de mensajes definido en [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) es el siguiente:

```
Client                        Tracker
    Connect Req. ------------->
      <-------------- Connect Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
```
La fase de conexión es necesaria para prevenir la suplantación de direcciones IP. El tracker devuelve un ID de conexión que el cliente usa en anuncios posteriores. Este ID de conexión expira por defecto en un minuto en el cliente, y en dos minutos en el tracker.

I2P utilizará el mismo flujo de mensajes que BEP 15, para facilitar la adopción en bases de código de clientes existentes con capacidad UDP: por eficiencia, y por razones de seguridad discutidas a continuación:

```
Client                        Tracker
    Connect Req. ------------->       (Repliable Datagram2)
      <-------------- Connect Resp.   (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
             ...
```
Esto potencialmente proporciona un gran ahorro de ancho de banda sobre los anuncios de streaming (TCP). Mientras que el Datagram2 tiene aproximadamente el mismo tamaño que un SYN de streaming, la respuesta raw es mucho más pequeña que el SYN ACK de streaming. Las solicitudes posteriores usan Datagram3, y las respuestas posteriores son raw.

Las solicitudes de anuncio son Datagram3 para que el tracker no necesite mantener una gran tabla de mapeo de IDs de conexión a destino de anuncio o hash. En su lugar, el tracker puede generar IDs de conexión criptográficamente a partir del hash del remitente, la marca de tiempo actual (basada en algún intervalo), y un valor secreto. Cuando se recibe una solicitud de anuncio, el tracker valida el ID de conexión, y luego usa el hash del remitente Datagram3 como el objetivo de envío.

### Tiempo de Vida de la Conexión

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html) especifica que el ID de conexión expira en un minuto en el cliente, y en dos minutos en el tracker. No es configurable. Esto limita las posibles ganancias de eficiencia, a menos que los clientes agrupen los anuncios para hacerlos todos dentro de una ventana de un minuto. i2psnark actualmente no agrupa los anuncios; los distribuye, para evitar ráfagas de tráfico. Se reporta que los usuarios avanzados ejecutan miles de torrents a la vez, y enviar tantos anuncios en ráfagas en un minuto no es realista.

Aquí, proponemos extender la respuesta de conexión para agregar un campo opcional de tiempo de vida de conexión. El valor predeterminado, si no está presente, es de un minuto. De lo contrario, el tiempo de vida especificado en segundos deberá ser utilizado por el cliente, y el tracker mantendrá el ID de conexión durante un minuto adicional.

### Compatibilidad con BEP 15

Este diseño mantiene la compatibilidad con [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) tanto como sea posible para limitar los cambios requeridos en clientes y trackers existentes.

El único cambio requerido es el formato de la información del peer en la respuesta de announce. La adición del campo lifetime en la respuesta de connect no es requerida pero es fuertemente recomendada para eficiencia, como se explicó anteriormente.

### Análisis de Seguridad

Un objetivo importante de un protocolo de anuncio UDP es prevenir la suplantación de direcciones. El cliente debe existir realmente y agrupar un leaseSet real. Debe tener túneles de entrada para recibir la Respuesta de Conexión. Estos túneles podrían ser de cero saltos y construirse instantáneamente, pero eso expondría al creador. Este protocolo logra ese objetivo.

### Problemas

- Este protocolo no admite destinos ciegos, pero puede extenderse para hacerlo. Ver más abajo.

## Especificación

### Protocolos y Puertos

Repliable Datagram2 usa el protocolo I2CP 19; repliable Datagram3 usa el protocolo I2CP 20; los datagramas sin procesar usan el protocolo I2CP 18. Las solicitudes pueden ser Datagram2 o Datagram3. Las respuestas son siempre sin procesar. El formato de datagrama repliable más antiguo ("Datagram1") que usa el protocolo I2CP 17 NO debe ser utilizado para solicitudes o respuestas; estos deben descartarse si se reciben en los puertos de solicitud/respuesta. Tenga en cuenta que el protocolo Datagram1 17 todavía se usa para el protocolo DHT.

Las solicitudes utilizan el "puerto de destino" I2CP de la URL de anuncio; ver más abajo. El "puerto de origen" de la solicitud es elegido por el cliente, pero debe ser distinto de cero y un puerto diferente de los utilizados por DHT, para que las respuestas puedan clasificarse fácilmente. Los trackers deberían rechazar las solicitudes recibidas en el puerto incorrecto.

Las respuestas utilizan el "puerto destino" de I2CP de la solicitud. El "puerto origen" de la solicitud es el "puerto destino" de la solicitud.

### URL de anuncio

El formato de URL de announce no se especifica en [BEP 15](http://www.bittorrent.org/beps/bep_0015.html), pero como en clearnet, las URLs de announce UDP tienen la forma `udp://host:port/path`. La ruta se ignora y puede estar vacía, pero típicamente es `/announce` en clearnet. La parte `:port` siempre debería estar presente, sin embargo, si se omite la parte `:port`, usa un puerto I2CP predeterminado de 6969, ya que ese es el puerto común en clearnet. También puede haber parámetros cgi `&a=b&c=d` anexados, estos pueden ser procesados y proporcionados en la petición de announce, ver [BEP 41](http://www.bittorrent.org/beps/bep_0041.html). Si no hay parámetros o ruta, el `/` final también puede omitirse, como se implica en [BEP 41](http://www.bittorrent.org/beps/bep_0041.html).

### Formatos de Datagrama

Todos los valores se envían en orden de bytes de red (big endian). No esperes que los paquetes tengan exactamente un tamaño determinado. Las extensiones futuras podrían aumentar el tamaño de los paquetes.

#### Solicitud de Conexión

Cliente a rastreador. 16 bytes. Debe ser Datagram2 respondible. Igual que en [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Sin cambios.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">protocol_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0x41727101980 // magic constant</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
#### Respuesta de Conexión

Tracker a cliente. 16 o 18 bytes. Debe ser raw. Igual que en [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) excepto como se indica a continuación.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">lifetime</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // Change from BEP 15</td>
    </tr>
  </tbody>
</table>
La respuesta DEBE enviarse al "puerto de destino" I2CP que se recibió como "puerto de origen" de la solicitud.

El campo lifetime es opcional e indica la duración del connection_id del cliente en segundos. El valor predeterminado es 60, y el mínimo si se especifica es 60. El máximo es 65535 o aproximadamente 18 horas. El tracker debe mantener el connection_id durante 60 segundos más que la duración del cliente.

#### Solicitud de Anuncio

Cliente a tracker. 98 bytes mínimo. Debe ser un Datagram3 con capacidad de respuesta. Igual que en [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) excepto como se indica a continuación.

El connection_id es tal como se recibió en la respuesta de conexión.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">info_hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">peer_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">56</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">downloaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">left</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">uploaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">80</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">event</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // 0: none; 1: completed; 2: started; 3: stopped</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">84</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">IP address</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // default, unused in I2P</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">88</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">92</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">num_want</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1 // default</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">port</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// must be same as I2CP from port</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">98</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">options</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // As specified in BEP 41</td>
    </tr>
  </tbody>
</table>
Cambios desde [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- la clave se ignora
- la dirección IP no se utiliza
- el puerto probablemente se ignora pero debe ser el mismo que el puerto I2CP from
- La sección de opciones, si está presente, se define según [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)

La respuesta DEBE enviarse al "puerto de destino" I2CP que se recibió como "puerto de origen" de la solicitud. No utilices el puerto de la solicitud de anuncio.

#### Respuesta de Anuncio

Tracker a cliente. 20 bytes mínimo. Debe ser sin formato. Igual que en [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) excepto como se indica a continuación.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">interval</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">leechers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">seeders</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32 * n 32-byte hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">binary hashes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// Change from BEP 15</td>
    </tr>
  </tbody>
</table>
Cambios desde [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- En lugar de 6 bytes IPv4+puerto o 18 bytes IPv6+puerto, devolvemos un múltiplo de "respuestas compactas" de 32 bytes con los hashes SHA-256 binarios de los peers. Al igual que con las respuestas compactas TCP, no incluimos un puerto.

La respuesta DEBE ser enviada al "puerto de destino" I2CP que se recibió como "puerto de origen" de la solicitud. No uses el puerto de la solicitud de anuncio.

Los datagramas de I2P tienen un tamaño máximo muy grande de aproximadamente 64 KB; sin embargo, para una entrega confiable, se deben evitar los datagramas mayores de 4 KB. Para eficiencia de ancho de banda, los trackers probablemente deberían limitar el máximo de peers a aproximadamente 50, lo que corresponde a un paquete de aproximadamente 1600 bytes antes de la sobrecarga en varias capas, y debería estar dentro del límite de carga útil de dos mensajes de tunnel después de la fragmentación.

Como en BEP 15, no se incluye un conteo del número de direcciones de peers (IP/puerto para BEP 15, hashes aquí) que siguen. Aunque no se contempla en BEP 15, se podría definir un marcador de fin de peers con todos ceros para indicar que la información de peers está completa y que siguen algunos datos de extensión.

Para que sea posible esta extensión en el futuro, los clientes deberían ignorar un hash de 32 bytes completamente en ceros, y cualquier dato que le siga. Los trackers deberían rechazar anuncios de un hash completamente en ceros, aunque ese hash ya está prohibido por los routers Java.

#### Extraer

La solicitud/respuesta de scrape de [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) no es requerida por esta especificación, pero puede implementarse si se desea, no se requieren cambios. El cliente debe adquirir primero un ID de conexión. La solicitud de scrape es siempre un Datagram3 que puede responderse. La respuesta de scrape es siempre raw.

#### Respuesta de Error

Tracker a cliente. 8 bytes mínimo (si el mensaje está vacío). Debe ser sin procesar. Igual que en [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Sin cambios.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3 // error</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">message</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
## Extensiones

Los bits de extensión o un campo de versión no están incluidos. Los clientes y rastreadores no deben asumir que los paquetes tengan un tamaño determinado. De esta manera, se pueden agregar campos adicionales sin romper la compatibilidad. Se recomienda el formato de extensiones definido en [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) si es necesario.

La respuesta de conexión se modifica para agregar una duración opcional del ID de conexión.

Si se requiere soporte para destino ciego, podemos agregar la dirección ciega de 35 bytes al final de la solicitud de anuncio, o solicitar hashes ciegos en las respuestas, utilizando el formato [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) (parámetros por determinar). El conjunto de direcciones de pares ciegas de 35 bytes podría agregarse al final de la respuesta de anuncio, después de un hash de 32 bytes con todos ceros.

## Pautas de Implementación

Consulta la sección de diseño anterior para una discusión sobre los desafíos para clientes y trackers no integrados y que no usan I2CP.

### Clientes

Para un nombre de host de tracker determinado, un cliente debe preferir las URL UDP sobre HTTP, y no debe anunciar a ambos.

Los clientes con soporte BEP 15 existente deberían requerir solo modificaciones menores.

Si un cliente soporta DHT u otros protocolos de datagramas, probablemente debería seleccionar un puerto diferente como el "puerto origen" de la solicitud para que las respuestas regresen a ese puerto y no se mezclen con los mensajes DHT. El cliente solo recibe datagramas en bruto como respuestas. Los trackers nunca enviarán un datagram2 con capacidad de respuesta al cliente.

Los clientes con una lista predeterminada de opentrackers deberían actualizar la lista para agregar URLs UDP después de que se sepa que los opentrackers conocidos admiten UDP.

Los clientes pueden o no implementar la retransmisión de solicitudes. Las retransmisiones, si se implementan, deben usar un tiempo de espera inicial de al menos 15 segundos, y duplicar el tiempo de espera para cada retransmisión (retroceso exponencial).

Los clientes deben retroceder después de recibir una respuesta de error.

### Rastreadores

Los trackers con soporte BEP 15 existente deberían requerir solo pequeñas modificaciones. Esta especificación difiere de la propuesta de 2014, en que el tracker debe soportar la recepción de datagram2 y datagram3 con respuesta en el mismo puerto.

Para minimizar los requisitos de recursos del tracker, este protocolo está diseñado para eliminar cualquier requerimiento de que el tracker almacene mapeos de hashes de cliente a IDs de conexión para validación posterior. Esto es posible porque el paquete de solicitud de announce es un paquete Datagram3 con respuesta, por lo que contiene el hash del remitente.

Una implementación recomendada es:

- Definir la época actual como el tiempo actual con una resolución del tiempo de vida de la conexión, `epoch = now / lifetime`.
- Definir una función de hash criptográfica `H(secret, clienthash, epoch)` que genere una salida de 8 bytes.
- Generar el secreto constante aleatorio usado para todas las conexiones.
- Para respuestas de conexión, generar `connection_id = H(secret, clienthash, epoch)`
- Para solicitudes de anuncio, validar el ID de conexión recibido en la época actual verificando `connection_id == H(secret, clienthash, epoch) || connection_id == H(secret, clienthash, epoch - 1)`

## Referencias

- **[BEP15]** [BEP 15 - Protocolo de Tracker UDP](http://www.bittorrent.org/beps/bep_0015.html)
- **[BEP41]** [BEP 41 - Extensiones del Protocolo de Tracker UDP](http://www.bittorrent.org/beps/bep_0041.html)
- **[DATAGRAMS]** [Especificación de Datagramas](/docs/specs/datagrams)
- **[Prop160]** [Propuesta 160 - Trackers UDP](/proposals/160-udp-trackers)
- **[Prop163]** [Propuesta 163 - Datagram2/Datagram3](/proposals/163-datagram2-datagram3)
- **[SAMv3]** [API SAM v3](/docs/api/samv3)
- **[SPEC]** [BitTorrent sobre I2P](/docs/applications/bittorrent)
