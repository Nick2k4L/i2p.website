---
title: "Especificación de Creación de Tunnel"
description: "Especificación de construcción de túneles ElGamal para crear túneles usando telescoping no interactivo."
slug: "tunnel-creation"
aliases: 
category: "Diseño"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Resumen

NOTA: OBSOLETO - Esta es la especificación de construcción de túneles ElGamal. Ver [tunnel-creation-ecies](/docs/specs/tunnel-creation-ecies/) para la especificación de construcción de túneles X25519.

Este documento especifica los detalles de los mensajes de construcción de tunnel cifrados utilizados para crear tunnels usando un método de "telescoping no interactivo". Consulte el documento de construcción de tunnel [TUNNEL-IMPL](/docs/specs/tunnel-implementation/) para obtener una descripción general del proceso, incluyendo métodos de selección y ordenamiento de peers.

La creación del tunnel se logra mediante un único mensaje que se pasa a lo largo de la ruta de peers en el tunnel, se reescribe en el lugar y se transmite de vuelta al creador del tunnel. Este único mensaje de tunnel está compuesto por un número variable de registros (hasta 8) - uno para cada peer potencial en el tunnel. Los registros individuales están encriptados asimétricamente (ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)) para ser leídos solo por un peer específico a lo largo de la ruta, mientras que se añade una capa adicional de encriptación simétrica (AES [CRYPTO-AES](/docs/specs/cryptography/#aes)) en cada salto para exponer el registro encriptado asimétricamente solo en el momento apropiado.

### Número de Registros

No todos los registros deben contener datos válidos. El mensaje de construcción para un tunnel de 3 saltos, por ejemplo, puede contener más registros para ocultar la longitud real del tunnel a los participantes. Existen dos tipos de mensajes de construcción. El Tunnel Build Message original ([TBM](/docs/specs/i2np/#struct-TunnelBuild)) contiene 8 registros, que es más que suficiente para cualquier longitud práctica de tunnel. El nuevo Variable Tunnel Build Message ([VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild)) contiene de 1 a 8 registros. El originador puede equilibrar el tamaño del mensaje con la cantidad deseada de ofuscación de la longitud del tunnel.

En la red actual, la mayoría de los tunnels tienen 2 o 3 saltos de longitud. La implementación actual utiliza un VTBM de 5 registros para construir tunnels de 4 saltos o menos, y el TBM de 8 registros para tunnels más largos. El VTBM de 5 registros (que, cuando se fragmenta, cabe en tres mensajes de tunnel de 1KB) reduce el tráfico de red y aumenta la tasa de éxito de construcción, porque los mensajes más pequeños tienen menos probabilidades de ser descartados.

El mensaje de respuesta debe ser del mismo tipo y longitud que el mensaje de construcción.

### Especificación de Registro de Solicitud

También especificado en la Especificación I2NP [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

Texto en claro del registro, visible solo para el salto que está siendo consultado:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">tunnel ID to receive messages as, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4-35</td><td style="border:1px solid var(--color-border); padding:0.6rem;">local router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">36-39</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next tunnel ID, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">40-71</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">72-103</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel layer key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">104-135</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel IV key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">136-167</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">168-183</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply IV</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">184</td><td style="border:1px solid var(--color-border); padding:0.6rem;">flags</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">185-188</td><td style="border:1px solid var(--color-border); padding:0.6rem;">request time (in hours since the epoch, rounded down)</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">189-192</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next message ID</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">193-221</td><td style="border:1px solid var(--color-border); padding:0.6rem;">uninterpreted / random padding</td></tr>
</tbody>
</table>
Los campos de ID del siguiente tunnel e hash de identidad del siguiente router se utilizan para especificar el siguiente salto en el tunnel, aunque para un punto final de tunnel saliente, especifican dónde debe enviarse el mensaje de respuesta de creación de tunnel reescrito. Además, el ID del siguiente mensaje especifica el ID de mensaje que el mensaje (o respuesta) debe usar.

La clave de capa de tunnel, la clave IV de tunnel, la clave de respuesta y el IV de respuesta son cada uno valores aleatorios de 32 bytes generados por el creador, para uso únicamente en este registro de solicitud de construcción.

El campo de flags contiene lo siguiente (orden de bits: 76543210, el bit 7 es MSB):

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages from anyone</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages to anyone, and send the reply to the specified next hop in a Tunnel Build Reply Message</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5-0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Undefined, must set to 0 for compatibility with future options</td></tr>
</tbody>
</table>
El bit 7 indica que el salto será un gateway de entrada (IBGW). El bit 6 indica que el salto será un endpoint de salida (OBEP). Si ninguno de los bits está establecido, el salto será un participante intermedio. Ambos no pueden estar establecidos al mismo tiempo.

#### Creación de Registro de Solicitud

Cada salto obtiene un Tunnel ID aleatorio, distinto de cero. Se completan los Tunnel IDs del salto actual y del siguiente. Cada registro obtiene una clave IV de tunnel aleatoria, IV de respuesta, clave de capa y clave de respuesta.

#### Cifrado de Registro de Solicitud

Ese registro en texto claro está cifrado con ElGamal 2048 [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) usando la clave pública de cifrado del salto y formateado en un registro de 528 bytes:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">First 16 bytes of the SHA-256 of the current hop's router identity</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">16-527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal-2048 encrypted request record</td></tr>
</tbody>
</table>
En el registro cifrado de 512 bytes, los datos ElGamal contienen los bytes 1-256 y 258-513 del bloque cifrado ElGamal de 514 bytes [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). Los dos bytes de relleno del bloque (los bytes cero en las ubicaciones 0 y 257) se eliminan.

Dado que el cleartext utiliza el campo completo, no hay necesidad de relleno adicional más allá de `SHA256(cleartext) + cleartext`.

Cada registro de 528 bytes se cifra luego de forma iterativa (usando descifrado AES, con la clave de respuesta y el IV de respuesta para cada salto) de modo que la identidad del router solo esté en texto plano para el salto en cuestión.

### Procesamiento y Cifrado de Saltos

Cuando un salto recibe un TunnelBuildMessage, busca entre los registros contenidos en él uno que comience con su propio hash de identidad (recortado a 16 bytes). Luego descifra el bloque ElGamal de ese registro y recupera el texto plano protegido. En ese punto, se aseguran de que la solicitud de tunnel no sea un duplicado alimentando la clave de respuesta AES-256 en un filtro Bloom. Los duplicados o solicitudes inválidas se descartan. Los registros que no estén marcados con la hora actual, o la hora anterior si es poco después del inicio de la hora, deben descartarse. Por ejemplo, toma la hora en la marca de tiempo, conviértela a un tiempo completo, luego si está más de 65 minutos atrasada o 5 minutos adelantada del tiempo actual, es inválida. El filtro Bloom debe tener una duración de al menos una hora (más unos pocos minutos, para permitir el desfase del reloj), de modo que los registros duplicados en la hora actual que no son rechazados al verificar la marca de tiempo de la hora en el registro, serán rechazados por el filtro.

Después de decidir si aceptarán participar en el tunnel o no, reemplazan el registro que contenía la solicitud con un bloque de respuesta cifrado. Todos los demás registros se cifran con AES-256 [CRYPTO-AES](/docs/specs/cryptography/#aes) usando la clave de respuesta e IV incluidos. Cada uno se cifra por separado con AES/CBC usando la misma clave de respuesta e IV de respuesta. El modo CBC no continúa (se encadena) entre registros.

Cada salto conoce solo su propia respuesta. Si está de acuerdo, mantendrá el tunnel hasta su expiración, incluso si no será utilizado, ya que no puede saber si todos los otros saltos estuvieron de acuerdo.

#### Especificación de Registro de Respuesta

Después de que el salto actual lee su registro, lo reemplaza con un registro de respuesta indicando si acepta o no participar en el tunnel, y si no lo hace, clasifica su razón de rechazo. Esto es simplemente un valor de 1 byte, donde 0x0 significa que acepta participar en el tunnel, y valores más altos significan niveles más altos de rechazo.

Los siguientes códigos de rechazo están definidos:

- TUNNEL_REJECT_PROBABALISTIC_REJECT = 10
- TUNNEL_REJECT_TRANSIENT_OVERLOAD = 20
- TUNNEL_REJECT_BANDWIDTH = 30
- TUNNEL_REJECT_CRIT = 50

Para ocultar otras causas, como el apagado del router, de los peers, la implementación actual usa TUNNEL_REJECT_BANDWIDTH para casi todos los rechazos.

La respuesta se cifra con la clave de sesión AES entregada en el bloque cifrado, rellenada con 495 bytes de datos aleatorios para alcanzar el tamaño completo del registro. El relleno se coloca antes del byte de estado:

`AES-256-CBC(SHA-256(padding+status) + padding + status, key, IV)`

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-31</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SHA-256 of bytes 32-527</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">32-526</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Random padding</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Reply value</td></tr>
</tbody>
</table>
Esto también se describe en la especificación I2NP [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

### Preparación del Mensaje de Construcción de Tunnel

Al construir un nuevo Tunnel Build Message, todos los Build Request Records deben primero construirse y cifrarse asimétricamente usando ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). Cada registro se descifra entonces preventivamente con las claves de respuesta e IVs de los saltos anteriores en la ruta, usando AES [CRYPTO-AES](/docs/specs/cryptography/#aes). Ese descifrado debe ejecutarse en orden inverso para que los datos cifrados asimétricamente aparezcan en claro en el salto correcto después de que su predecesor los cifre.

Los registros excedentes que no se necesitan para solicitudes individuales simplemente se llenan con datos aleatorios por parte del creador.

### Entrega de Mensajes de Construcción de Tunnel

Para túneles de salida, la entrega se realiza directamente desde el creador del túnel hasta el primer salto, empaquetando el TunnelBuildMessage como si el creador fuera simplemente otro salto en el túnel. Para túneles de entrada, la entrega se realiza a través de un túnel de salida existente. El túnel de salida generalmente proviene del mismo pool que el nuevo túnel que se está construyendo. Si no hay túneles de salida disponibles en ese pool, se utiliza un túnel exploratorio de salida. Al iniciar, cuando aún no existe un túnel exploratorio de salida, se utiliza un túnel de salida falso de 0 saltos.

### Manejo de Endpoint de Mensaje de Construcción de Tunnel

Para la creación de un túnel de salida, cuando la solicitud alcanza un punto final de salida (como se determina por la bandera 'permitir mensajes a cualquiera'), el salto se procesa como de costumbre, cifrando una respuesta en lugar del registro y cifrando todos los otros registros, pero como no hay un 'siguiente salto' al cual reenviar el TunnelBuildMessage, en su lugar coloca los registros de respuesta cifrados en un TunnelBuildReplyMessage ([TBRM](/docs/specs/i2np/#struct-TunnelBuildReply)) o VariableTunnelBuildReplyMessage ([VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply)) (el tipo de mensaje y el número de registros deben coincidir con los de la solicitud) y lo entrega al túnel de respuesta especificado dentro del registro de solicitud. Ese túnel de respuesta reenvía el Tunnel Build Reply Message de vuelta al creador del túnel, tal como lo hace para cualquier otro mensaje [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation). El creador del túnel luego lo procesa, como se describe a continuación.

El reply tunnel fue seleccionado por el creador de la siguiente manera: Generalmente es un tunnel de entrada del mismo pool que el nuevo tunnel de salida que se está construyendo. Si no hay ningún tunnel de entrada disponible en ese pool, se utiliza un tunnel exploratorio de entrada. Al inicio, cuando aún no existe ningún tunnel exploratorio de entrada, se utiliza un tunnel de entrada falso de 0 saltos.

Para la creación de un tunnel de entrada, cuando la solicitud llega al endpoint de entrada (también conocido como el creador del tunnel), no hay necesidad de generar un Mensaje de Respuesta de Construcción de Tunnel explícito, y el router procesa cada una de las respuestas, como se indica a continuación.

### Procesamiento de Mensajes de Respuesta de Construcción de Tunnel

Para procesar los registros de respuesta, el creador simplemente tiene que descifrar con AES cada registro individualmente, usando la clave de respuesta e IV de cada salto en el tunnel después del peer (en orden inverso). Esto entonces expone la respuesta especificando si están de acuerdo en participar en el tunnel o por qué se niegan. Si todos están de acuerdo, el tunnel se considera creado y puede usarse inmediatamente, pero si alguien se niega, el tunnel se descarta.

Los acuerdos y rechazos se registran en el perfil de cada peer [PEER-SELECTION](/docs/overview/tunnel-routing/), para ser utilizados en futuras evaluaciones de la capacidad de túnel del peer.

## Historia y Notas

Esta estrategia surgió durante una discusión en la lista de correo de I2P entre Michael Rogers, Matthew Toseland (toad), y jrandom sobre el ataque predecesor. Ver [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html), [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html). Fue introducida en la versión 0.6.1.10 el 2006-02-16, que fue la última vez que se realizó un cambio no compatible con versiones anteriores en I2P.

Notas:

- Este diseño no previene que dos peers hostiles dentro de un túnel marquen uno o más registros de solicitud o respuesta para detectar que están dentro del mismo túnel, pero hacerlo puede ser detectado por el creador del túnel al leer la respuesta, causando que el túnel sea marcado como inválido.
- Este diseño no incluye una prueba de trabajo en la sección encriptada asimétricamente, aunque el hash de identidad de 16 bytes podría reducirse a la mitad con la última parte reemplazada por una función hashcash de hasta 2^64 de costo.
- Este diseño por sí solo no previene que dos peers hostiles dentro de un túnel usen información de temporización para determinar si están en el mismo túnel. El uso de entrega de solicitudes sincronizada y por lotes podría ayudar (agrupando solicitudes y enviándolas en el minuto (sincronizado por ntp)). Sin embargo, hacerlo permite a los peers 'marcar' las solicitudes retrasándolas y detectando el retraso más adelante en el túnel, aunque quizás descartar solicitudes no entregadas en una pequeña ventana funcionaría (aunque hacerlo requeriría un alto grado de sincronización de reloj). Alternativamente, ¿quizás los saltos individuales podrían inyectar un retraso aleatorio antes de reenviar la solicitud?
- ¿Hay algún método no fatal para marcar la solicitud?
- La marca de tiempo con resolución de una hora se usa para prevención de repetición. La restricción no fue aplicada hasta la versión 0.9.16.

## Trabajo Futuro

- En la implementación actual, el originador deja un registro vacío para sí mismo. Por lo tanto, un mensaje de n registros solo puede construir un tunnel de n-1 saltos. Esto parece ser necesario para los tunnels de entrada (donde el penúltimo salto puede ver el prefijo hash para el siguiente salto), pero no para los tunnels de salida. Esto debe ser investigado y verificado. Si es posible usar el registro restante sin comprometer el anonimato, deberíamos hacerlo.
- Análisis adicional de posibles ataques de etiquetado y temporización descritos en las notas anteriores.
- Usar solo VTBM; no seleccionar peers antiguos que no lo soporten.
- El Build Request Record no especifica un tiempo de vida o expiración del tunnel; cada salto expira el tunnel después de 10 minutos, lo cual es una constante codificada fija en toda la red. Podríamos usar un bit en el campo de bandera y tomar 4 (u 8) bytes del relleno para especificar un tiempo de vida o expiración. El solicitante solo especificaría esta opción si todos los participantes la soportaran.

## Referencias

- [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) - Especificación de BuildRequestRecord
- [CRYPTO-AES](/docs/specs/cryptography/#aes) - Cifrado AES
- [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) - Cifrado ElGamal
- [HASHING-IT-OUT](http://www-users.cs.umn.edu/~hopper/hashing_it_out.pdf)
- [PEER-SELECTION](/docs/overview/tunnel-routing/)
- [PREDECESSOR](http://forensics.umass.edu/pubs/wright-tissec.pdf)
- [PREDECESSOR-2008](http://forensics.umass.edu/pubs/wright.tissec.2008.pdf)
- [TBM](/docs/specs/i2np/#struct-TunnelBuild) - TunnelBuildMessage
- [TBRM](/docs/specs/i2np/#struct-TunnelBuildReply) - TunnelBuildReplyMessage
- [TUNBUILD-REASONING](http://zzz.i2p/archive/2005-10/msg00129.html)
- [TUNBUILD-SUMMARY](http://zzz.i2p/archive/2005-10/msg00138.html)
- [TUNNEL-IMPL](/docs/specs/tunnel-implementation/)
- [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation)
- [VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild) - VariableTunnelBuildMessage
- [VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply) - VariableTunnelBuildReplyMessage
