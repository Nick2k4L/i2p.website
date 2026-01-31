---
title: "Protocolo de Streaming"
description: "Transporte similar a TCP utilizado por la mayoría de aplicaciones I2P"
slug: "streaming"
lastUpdated: "2025-07"
accurateFor: "0.9.67"
---

## Descripción general {#overview}

La biblioteca de streaming es técnicamente parte de la capa de "aplicación", ya que no es una función central del router. En la práctica, sin embargo, proporciona una función vital para casi todas las aplicaciones I2P existentes, al proveer flujos similares a TCP sobre I2P, y permitir que las aplicaciones existentes sean fácilmente portadas a I2P. La otra biblioteca de transporte extremo a extremo para comunicación de cliente es la [biblioteca de datagramas](/docs/specs/datagrams).

La biblioteca de streaming es una capa sobre la [API I2CP](/docs/specs/i2cp) principal que permite flujos confiables, ordenados y autenticados de mensajes para operar a través de una capa de mensajes no confiable, desordenada y no autenticada. Al igual que la relación TCP a IP, esta funcionalidad de streaming tiene toda una serie de compensaciones y optimizaciones disponibles, pero en lugar de integrar esa funcionalidad en el código base de I2P, se ha separado en su propia biblioteca tanto para mantener las complejidades similares a TCP separadas como para permitir implementaciones alternativas optimizadas.

Considerando el costo relativamente alto de los mensajes, el protocolo de la biblioteca de streaming para programar y entregar esos mensajes ha sido optimizado para permitir que los mensajes individuales transmitidos contengan tanta información como esté disponible. Por ejemplo, una pequeña transacción HTTP enviada a través de la biblioteca de streaming puede completarse en un solo viaje de ida y vuelta - los primeros mensajes agrupan un SYN, FIN y la pequeña carga útil de la solicitud HTTP, y la respuesta agrupa el SYN, FIN, ACK y la carga útil de la respuesta HTTP. Aunque debe transmitirse un ACK adicional para informar al servidor HTTP que el SYN/FIN/ACK ha sido recibido, el proxy HTTP local a menudo puede entregar la respuesta completa al navegador inmediatamente.

La biblioteca de streaming tiene mucho parecido a una abstracción de TCP, con sus ventanas deslizantes, algoritmos de control de congestión (tanto arranque lento como evitación de congestión), y comportamiento general de paquetes (ACK, SYN, FIN, RST, cálculo de rto, etc).

La biblioteca de streaming es una biblioteca robusta que está optimizada para operar sobre I2P. Tiene una configuración de una sola fase y contiene una implementación completa de ventanas.

## API {#api}

La API de la biblioteca de streaming proporciona un paradigma de socket estándar para aplicaciones Java. La API de nivel inferior [I2CP](/docs/specs/i2cp) está completamente oculta, excepto que las aplicaciones pueden pasar [parámetros I2CP](/docs/specs/i2cp#options) a través de la biblioteca de streaming, para ser interpretados por I2CP.

La interfaz estándar para la biblioteca de streaming es que la aplicación use el I2PSocketManagerFactory para crear un I2PSocketManager. La aplicación luego solicita al administrador de sockets un I2PSession, lo que causará una conexión al router a través de [I2CP](/docs/specs/i2cp). La aplicación puede entonces establecer conexiones con un I2PSocket o recibir conexiones con un I2PServerSocket.

Para ver un buen ejemplo de uso, consulta el código de i2psnark.

### Opciones y valores por defecto {#options}

Las opciones y valores predeterminados actuales se enumeran a continuación. Las opciones distinguen entre mayúsculas y minúsculas y pueden configurarse para todo el router, para un cliente en particular, o para un socket individual por conexión. Muchos valores están ajustados para el rendimiento HTTP bajo condiciones típicas de I2P. Otras aplicaciones como servicios peer-to-peer son fuertemente recomendadas a modificar según sea necesario, estableciendo las opciones y pasándolas a través de la llamada a I2PSocketManagerFactory.createManager(_i2cpHost, _i2cpPort, opts). Los valores de tiempo están en ms.

Ten en cuenta que las APIs de nivel superior, como [SAM](/docs/api/samv3), [BOB](/docs/legacy/bob) e [I2PTunnel](/docs/api/i2ptunnel), pueden anular estos valores predeterminados con sus propios valores por defecto. También ten en cuenta que muchas opciones solo se aplican a servidores que escuchan conexiones entrantes.

A partir de la versión 0.9.1, la mayoría de las opciones, pero no todas, pueden cambiarse en un gestor de socket o sesión activa. Consulta los javadocs para más detalles.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Default</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.accessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes used for either access list or blacklist. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.destination.sigType</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The name or number of the signature type for a transient destination. As of release 0.9.12.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableAccessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a whitelist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableBlackList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a blacklist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.answerPings</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to respond to incoming pings</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.blacklist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes to be blacklisted for incoming connections to ALL destinations in the context. This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.3.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.bufferSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64K</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How much transmit data (in bytes) will be accepted that hasn't been written out yet.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.congestionAvoidanceGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in congestion avoidance, we grow the window size at the rate of <code>1/(windowSize*factor)</code>. In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to wait after instantiating a new con before actually attempting to connect. If this is &lt;= 0, connect immediately with no initial data. If greater than 0, wait until the output stream is flushed, the buffer fills, or that many milliseconds pass, and include any initial data with the SYN.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5*60*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on connect, in milliseconds. Negative means indefinitely. Default is 5 minutes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.disableRejectLogging</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to disable warnings in the logs when an incoming connection is rejected due to connection limits. As of release 0.9.4.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.dsalist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes or host names to be contacted using an alternate DSA destination. Only applies if multisession is enabled and the primary session is non-DSA (generally for shared clients only). This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.21.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.enforceProtocol</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to listen only for the streaming protocol. Setting to true will prohibit communication with Destinations earlier than release 0.7.1 (released March 2009). Set to true if running multiple protocols on this Destination. As of release 0.9.1. Default true as of release 0.9.36.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 (send)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0=noop, 1=disconnect) What to do on an inactivity timeout - do nothing, disconnect, or send a duplicate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">90*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Idle time before sending a keepalive</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialAckDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">750</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Delay before sending an ack</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialResendDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The initial value of the resend delay field in the packet header, times 1000. Not fully implemented; see below.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial timeout (if no <a href="#sharing">sharing data</a> available). As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial round trip time estimate (if no <a href="#sharing">sharing data</a> available). Disabled as of release 0.9.8; uses actual RTT.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(if no <a href="#sharing">sharing data</a> available) In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.limitAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reset</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">What action to take when an incoming connection exceeds limits. Valid values are: reset (reset the connection); drop (drop the connection); or http (send a hardcoded HTTP 429 response). Any other value is a custom response to be sent. backslash-r and backslash-n will be replaced with CR and LF. As of release 0.9.34.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConcurrentStreams</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0 or negative value means unlimited) This is a total limit for incoming and outgoing combined.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxMessageSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1730</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum size of the payload, i.e. the MTU in bytes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxResends</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Maximum number of retransmissions before failure.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (all peers; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.profile</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 (bulk)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1=bulk; 2=interactive; see important notes <a href="#profile">below</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.readTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on read, in milliseconds. Negative means indefinitely.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.slowStartGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in slow start, we grow the window size at the rate of 1/(factor). In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttdevDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.wdwDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.writeTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on write/flush, in milliseconds. Negative means indefinitely.</td>
    </tr>
  </tbody>
</table>
## Especificación del Protocolo {#spec}

[Ver la página de Especificación de la Biblioteca de Streaming.](/docs/specs/streaming)

## Detalles de Implementación {#implementation}

### Configuración {#setup}

El iniciador envía un paquete con la bandera SYNCHRONIZE activada. Este paquete también puede contener los datos iniciales. El peer responde con un paquete con la bandera SYNCHRONIZE activada. Este paquete también puede contener los datos de respuesta iniciales.

El iniciador puede enviar paquetes de datos adicionales, hasta el tamaño de ventana inicial, antes de recibir la respuesta SYNCHRONIZE. Estos paquetes también tendrán el campo send Stream ID establecido en 0. Los destinatarios deben almacenar en buffer los paquetes recibidos en streams desconocidos durante un breve período de tiempo, ya que pueden llegar fuera de orden, antes del paquete SYNCHRONIZE.

### Selección y Negociación de MTU {#mtu}

El tamaño máximo de mensaje (también llamado MTU / MRU) se negocia al valor más bajo soportado por los dos peers. Como los mensajes de tunnel se rellenan a 1KB, una mala selección de MTU llevará a una gran cantidad de overhead. El MTU se especifica mediante la opción i2p.streaming.maxMessageSize. El MTU predeterminado actual de 1730 fue elegido para encajar precisamente en dos mensajes de tunnel I2NP de 1K, incluyendo el overhead para el caso típico.

Nota: Este es el tamaño máximo solo de la carga útil, sin incluir la cabecera.

Nota: Para conexiones ECIES, que tienen una sobrecarga reducida, el MTU recomendado es 1812. El MTU predeterminado permanece en 1730 para todas las conexiones, sin importar qué tipo de clave se use. Los clientes deben usar el mínimo del MTU enviado y recibido, como es habitual. Ver propuesta 155.

El primer mensaje en una conexión incluye un Destination de 387 bytes (típico) añadido por la capa de streaming, y usualmente un LeaseSet de 898 bytes (típico), y claves de sesión, empaquetados en el mensaje Garlic por el router. (El LeaseSet y las claves de sesión no serán empaquetados si una sesión ElGamal fue establecida previamente). Por lo tanto, el objetivo de ajustar una solicitud HTTP completa en un solo mensaje I2NP de 1KB no siempre es alcanzable. Sin embargo, la selección del MTU, junto con una implementación cuidadosa de las estrategias de fragmentación y agrupación en el procesador de gateway del tunnel, son factores importantes en el ancho de banda de la red, latencia, confiabilidad y eficiencia, especialmente para conexiones de larga duración.

### Integridad de Datos {#integrity}

La integridad de los datos está asegurada por la suma de verificación gzip CRC-32 implementada en [la capa I2CP](/docs/specs/i2cp#format). No hay campo de suma de verificación en el protocolo de streaming.

### Encapsulación de Paquetes {#encapsulation}

Cada paquete se envía a través de I2P como un mensaje único (o como un clove individual en un [Garlic Message](/docs/overview/garlic-routing)). La encapsulación de mensajes se implementa en las capas subyacentes de [I2CP](/docs/specs/i2cp), [I2NP](/docs/specs/i2np) y [tunnel message](/docs/specs/tunnel-message). No hay un mecanismo delimitador de paquetes o campo de longitud de carga útil en el protocolo de streaming.

### Retraso Opcional {#delay}

Los paquetes de datos pueden incluir un campo de retraso opcional que especifica el retraso solicitado, en ms, antes de que el receptor deba confirmar el paquete. Los valores válidos son de 0 a 60000 inclusive. Un valor de 0 solicita una confirmación inmediata. Esto es solo consultivo, y los receptores deberían retrasar ligeramente para que paquetes adicionales puedan ser confirmados con una sola confirmación. Algunas implementaciones pueden incluir un valor consultivo de (RTT medido / 2) en este campo. Para valores de retraso opcional distintos de cero, los receptores deberían limitar el retraso máximo antes de enviar una confirmación a unos pocos segundos como máximo. Los valores de retraso opcional mayores a 60000 indican ahogamiento, ver más abajo.

### Ventanas de Transmisión/Recepción y Ahogamiento {#windows}

Las cabeceras TCP incluyen la ventana de recepción en bytes; sin embargo, el protocolo de streaming no proporciona una forma de intercambiar el tamaño máximo de la ventana de recepción ni en bytes ni en paquetes. Solo hay una indicación simple de bloqueo/desbloqueo que indica que el búfer de recepción está lleno. Cada extremo debe mantener su propia estimación de la ventana de recepción del extremo remoto, ya sea en bytes o en paquetes. Ten en cuenta que un búfer de recepción puede desbordarse con cualquier tamaño de ventana si la aplicación cliente es lenta para vaciar el búfer.

El tamaño máximo predeterminado de ventana de transmisión y recepción en la implementación de Java es de 128 paquetes. Las implementaciones que establezcan un tamaño máximo de ventana de transmisión superior a 128 deben considerar los siguientes aspectos:

- Las respuestas CHOKE de routers Java debido a desbordamiento del búfer de recepción son mucho más probables.
- Se debe implementar la estimación del tamaño del búfer del receptor del extremo lejano para mitigar desbordamientos repetidos (ver arriba)
- CHOKE debe manejarse correctamente (ver abajo)
- Los tamaños máximos de ventana superiores a 256 son aún más propensos a errores, porque la longitud del campo de opción de conteo nack es de un byte, limitando los NACKs máximos a 255. Esta especificación no aborda qué hacer si hay más de 255 NACKs. No se recomiendan tamaños máximos de ventana superiores a 256.

El tamaño mínimo de búfer recomendado para implementaciones de receptor es 128 paquetes o 232 KB (aproximadamente 128 * 1812). Debido a la latencia de la red I2P, pérdidas de paquetes y el control de congestión resultante, rara vez se llena un búfer de este tamaño. Sin embargo, es mucho más probable que ocurra desbordamiento en conexiones de "bucle local" de alto ancho de banda (mismo router) o en pruebas locales.

Para indicar rápidamente y recuperarse suavemente de las condiciones de desbordamiento, existe un mecanismo simple para el retroceso en el protocolo de streaming. Si se recibe un paquete con un campo de retraso opcional con un valor de 60001 o superior, eso indica "ahogamiento" o una ventana de recepción de cero. Un paquete con un campo de retraso opcional con un valor de 60000 o menor indica "desahogamiento". Los paquetes sin un campo de retraso opcional no afectan el estado de ahogamiento/desahogamiento.

Después de ser bloqueado, no se deben enviar más paquetes con datos hasta que el transmisor sea desbloqueado, excepto por paquetes de datos de "sondeo" ocasionales para compensar por posibles paquetes de desbloqueo perdidos. El endpoint bloqueado debe iniciar un "temporizador de persistencia" para controlar el sondeo, como en TCP. El endpoint que desbloquea debe enviar varios paquetes con este campo configurado, o continuar enviándolos periódicamente hasta que se reciban paquetes de datos nuevamente. El tiempo máximo para esperar el desbloqueo depende de la implementación. El tamaño de ventana del transmisor y la estrategia de control de congestión después de ser desbloqueado depende de la implementación.

### Control de Congestión {#congestion}

La biblioteca de streaming utiliza slow-start estándar (crecimiento exponencial de ventana) y fases de evitación de congestión (crecimiento lineal de ventana), con backoff exponencial. El manejo de ventanas y confirmaciones utilizan conteo de paquetes, no conteo de bytes.

### Cerrar {#close}

Cualquier paquete, incluyendo uno con la bandera SYNCHRONIZE establecida, puede tener también la bandera CLOSE enviada. La conexión no se cierra hasta que el peer responde con la bandera CLOSE. Los paquetes CLOSE también pueden contener datos.

### Ping / Pong {#ping}

No hay función ping en la capa I2CP (equivalente a echo ICMP) o en datagramas. Esta función se proporciona en streaming. Los pings y pongs no pueden combinarse con un paquete de streaming estándar; si la opción ECHO está configurada, entonces la mayoría de las otras banderas, opciones, ackThrough, sequenceNum, NACKs, etc. son ignoradas.

Un paquete ping debe tener establecidas las banderas ECHO, SIGNATURE_INCLUDED y FROM_INCLUDED. El sendStreamId debe ser mayor que cero, y el receiveStreamId se ignora. El sendStreamId puede o no corresponder a una conexión existente.

Un paquete pong debe tener la bandera ECHO establecida. El sendStreamId debe ser cero, y el receiveStreamId es el sendStreamId del ping. Antes de la versión 0.9.18, el paquete pong no incluye ninguna carga útil que estuviera contenida en el ping.

A partir de la versión 0.9.18, los pings y pongs pueden contener una carga útil. La carga útil en el ping, hasta un máximo de 32 bytes, se devuelve en el pong.

El streaming puede configurarse para deshabilitar el envío de pongs con la configuración i2p.streaming.answerPings=false.

### Notas de i2p.streaming.profile {#profile}

Esta opción admite dos valores; 1=bulk y 2=interactive. La opción proporciona una pista a la biblioteca de streaming y/o al router sobre el patrón de tráfico que se espera.

"Bulk" significa optimizar para un alto ancho de banda, posiblemente a expensas de la latencia. Esta es la configuración predeterminada. "Interactive" significa optimizar para baja latencia, posiblemente a expensas del ancho de banda o la eficiencia. Las estrategias de optimización, si las hay, dependen de la implementación y pueden incluir cambios fuera del protocolo de streaming.

Hasta la versión 0.9.63 de la API, Java I2P devolvía un error para cualquier valor distinto de 1 (bulk) y el tunnel fallaría al iniciarse. A partir de la versión 0.9.64 de la API, Java I2P ignora el valor. Hasta la versión 0.9.63 de la API, i2pd ignoraba esta opción; está implementada en i2pd a partir de la versión 0.9.64 de la API.

Aunque el protocolo de streaming incluye un campo de bandera para pasar la configuración del perfil al otro extremo, esto no está implementado en ningún router conocido.

### Compartición de Bloques de Control {#sharing}

La biblioteca de streaming soporta el intercambio de Bloques de Control "TCP". Esto comparte tres parámetros importantes de la biblioteca de streaming (tamaño de ventana, tiempo de ida y vuelta, varianza del tiempo de ida y vuelta) entre conexiones al mismo peer remoto. Esto se utiliza para intercambio "temporal" en el momento de apertura/cierre de conexión, no para intercambio "conjunto" durante una conexión (Ver [RFC 2140](http://www.ietf.org/rfc/rfc2140.txt)). Hay un intercambio separado por ConnectionManager (es decir, por Destination local) para que no haya filtración de información a otros Destinations en el mismo router. Los datos de intercambio para un peer determinado expiran después de unos minutos. Los siguientes parámetros de Intercambio de Bloques de Control pueden configurarse por router:

- RTT_DAMPENING = 0.75
- RTTDEV_DAMPENING = 0.75
- WINDOW_DAMPENING = 0.75

### Otros Parámetros {#other}

Los siguientes parámetros son valores predeterminados recomendados. Los valores predeterminados pueden variar, dependiendo de la implementación:

- MIN_RESEND_DELAY = 100 ms (RTO mínimo)
- MAX_RESEND_DELAY = 45 seg (RTO máximo)
- MIN_WINDOW_SIZE = 1
- MAX_WINDOW_SIZE = 128
- TREND_COUNT = 3
- MIN_MESSAGE_SIZE = 512 (MTU mínimo)
- INBOUND_BUFFER_SIZE = maxMessageSize * (maxWindowSize + 2)
- INITIAL_TIMEOUT (válido solo antes de que se muestree el RTT) = 9 seg
- "alpha" (factor de amortiguación RTT según RFC 6298) = 0.125
- "beta" (factor de amortiguación RTTDEV según RFC 6298) = 0.25
- "K" (multiplicador RTDEV según RFC 6298) = 4
- PASSIVE_FLUSH_DELAY = 175 ms
- Estimación RTT máxima: 60 seg

### Historia {#history}

La biblioteca de streaming ha crecido orgánicamente para I2P - primero mihi implementó la "mini biblioteca de streaming" como parte de I2PTunnel, que estaba limitada a un tamaño de ventana de 1 mensaje (requiriendo un ACK antes de enviar el siguiente), y luego fue refactorizada hacia una interfaz de streaming genérica (imitando los sockets TCP) y la implementación completa de streaming fue desplegada con un protocolo de ventana deslizante y optimizaciones para tener en cuenta el alto producto de ancho de banda x retardo. Los streams individuales pueden ajustar el tamaño máximo de paquete y otras opciones. El tamaño de mensaje predeterminado se selecciona para encajar precisamente en dos mensajes de túnel I2NP de 1K, y es un compromiso razonable entre los costos de ancho de banda de retransmitir mensajes perdidos, y la latencia y overhead de múltiples mensajes.

## Trabajo Futuro {#future}

El comportamiento de la biblioteca de streaming tiene un impacto profundo en el rendimiento a nivel de aplicación, y como tal, es un área importante para análisis adicional.

- Puede ser necesario ajustar adicionalmente los parámetros de la librería de streaming.
- Otra área de investigación es la interacción de la librería de streaming con las capas de transporte NTCP y SSU. Consulta [la página de discusión de NTCP](/docs/historical/ntcp-discussion) para más detalles.
- La interacción de los algoritmos de enrutamiento con la librería de streaming afecta fuertemente el rendimiento. En particular, la distribución aleatoria de mensajes a múltiples tunnels en un pool conduce a un alto grado de entrega fuera de orden que resulta en tamaños de ventana más pequeños de lo que sería el caso de otra manera. El router actualmente enruta mensajes para un par de destino de/hacia único a través de un conjunto consistente de tunnels, hasta la expiración del tunnel o falla en la entrega. Los algoritmos de falla y selección de tunnel del router deberían ser revisados para posibles mejoras.
- Los datos en el primer paquete SYN pueden exceder el MTU del receptor.
- El campo DELAY_REQUESTED podría usarse más.
- Los paquetes SYNCHRONIZE iniciales duplicados en streams de corta duración pueden no ser reconocidos y removidos.
- No enviar el MTU en una retransmisión.
- Los datos se envían a menos que la ventana de salida esté llena. (es decir, no-Nagle o TCP_NODELAY) Probablemente debería tener una opción de configuración para esto.
- zzz ha agregado código de depuración a la librería de streaming para registrar paquetes en un formato compatible con wireshark (pcap); Úsalo para analizar más el rendimiento. El formato puede requerir mejoras para mapear más parámetros de la librería de streaming a campos TCP.
- Hay propuestas para reemplazar la librería de streaming con TCP estándar (o quizás una capa nula junto con sockets raw). Esto sería desafortunadamente incompatible con la librería de streaming pero sería bueno comparar el rendimiento de ambos.
