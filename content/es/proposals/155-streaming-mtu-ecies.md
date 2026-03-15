---
title: "MTU de Transmisión para Destinos ECIES"
number: "155"
author: "zzz"
created: "2020-05-06"
lastupdated: "2020-05-30"
status: "Cerrado"
thread: "http://zzz.i2p/topics/2886"
target: "0.9.47"
implementedin: "0.9.47"
toc: true
---
## Nota
Despliegue y pruebas en la red en curso.
Sujeto a revisiones menores.


## Visión general


### Resumen

ECIES reduce el sobrecoste de los mensajes de sesión existente (ES) en aproximadamente 90 bytes.
Por lo tanto, podemos aumentar el MTU en aproximadamente 90 bytes para conexiones ECIES.
Véase la [especificación ECIES](/docs/specs/ecies/#overhead), la [especificación de Streaming](/docs/specs/streaming/#flags-and-option-data-fields) y la [documentación de la API de Streaming](/docs/api/streaming/).

Sin aumentar el MTU, en muchos casos los ahorros de sobrecoste no se "ahorran" realmente,
ya que los mensajes serán rellenados para usar de todos modos dos mensajes de túnel completos.

Esta propuesta no requiere ningún cambio en las especificaciones.
Se publica únicamente como propuesta para facilitar la discusión y la construcción de consenso
sobre el valor recomendado y sobre los detalles de implementación.


### Objetivos

- Aumentar el MTU negociado
- Maximizar el uso de mensajes de túnel de 1 KB
- No cambiar el protocolo de streaming


## Diseño

Utilizar la opción existente MAX_PACKET_SIZE_INCLUDED y la negociación de MTU.
Streaming continúa usando el mínimo entre el MTU enviado y el recibido.
El valor predeterminado sigue siendo 1730 para todas las conexiones, sin importar qué claves se usen.

Se recomienda a las implementaciones incluir la opción MAX_PACKET_SIZE_INCLUDED en todos los paquetes SYN, en ambas direcciones,
aunque esto no es un requisito.

Si un destino es solo ECIES, usar el valor más alto (tanto como Alice como Bob).
Si un destino tiene claves duales, el comportamiento puede variar:

Si el cliente de clave dual está fuera del router (en una aplicación externa),
puede que no "sepa" qué clave está siendo usada en el extremo remoto, y Alice puede solicitar
un valor más alto en el SYN, mientras que el tamaño máximo de datos en el SYN sigue siendo 1730.

Si el cliente de clave dual está dentro del router, la información sobre qué clave
está siendo usada puede o no estar disponible para el cliente.
El leaseset puede no haber sido aún recuperado, o las interfaces de API internas
pueden no facilitar fácilmente esa información al cliente.
Si la información está disponible, Alice puede usar el valor más alto;
de lo contrario, Alice debe usar el valor estándar de 1730 hasta que se negocie.

Un cliente de clave dual actuando como Bob puede enviar el valor más alto en respuesta,
incluso si no se recibió valor alguno o se recibió un valor de 1730 desde Alice;
sin embargo, no existe provisión para negociar un aumento en streaming,
por lo que el MTU debe permanecer en 1730.


Como se indica en la [documentación de la API de Streaming](/docs/api/streaming/),
los datos en los paquetes SYN enviados desde Alice a Bob pueden exceder el MTU de Bob.
Esta es una debilidad en el protocolo de streaming.
Por lo tanto, los clientes de clave dual deben limitar los datos en los paquetes SYN enviados
a 1730 bytes, mientras envían una opción de MTU más alta.
Una vez que Alice reciba el MTU más alto desde Bob, puede aumentar el tamaño máximo real de carga útil enviada.


### Análisis

Como se describe en la [especificación ECIES](/docs/specs/ecies/#overhead), el sobrecoste ElGamal para mensajes de sesión existente es
de 151 bytes, y el sobrecoste del Ratchet es de 69 bytes.
Por lo tanto, podemos aumentar el MTU para conexiones Ratchet en (151 - 69) = 82 bytes,
de 1730 a 1812.



## Especificación

Añadir los siguientes cambios y aclaraciones a la sección Selección y Negociación de MTU de la [documentación de la API de Streaming](/docs/api/streaming/).
Sin cambios en la [especificación de Streaming](/docs/specs/streaming/).


El valor predeterminado de la opción i2p.streaming.maxMessageSize sigue siendo 1730 para todas las conexiones, sin importar qué claves se usen.
Los clientes deben usar el mínimo entre el MTU enviado y recibido, como es habitual.

Existen cuatro constantes y variables relacionadas con el MTU:

- DEFAULT_MTU: 1730, sin cambios, para todas las conexiones
- i2cp.streaming.maxMessageSize: predeterminado 1730 o 1812, puede modificarse mediante configuración
- ALICE_SYN_MAX_DATA: El tamaño máximo de datos que Alice puede incluir en un paquete SYN
- negotiated_mtu: El mínimo entre el MTU de Alice y el de Bob, que se usará como tamaño máximo de datos
  en el SYN ACK desde Bob a Alice, y en todos los paquetes posteriores enviados en ambas direcciones


Hay cinco casos a considerar:


### 1) Alice solo ElGamal
Sin cambios, MTU de 1730 en todos los paquetes.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize predeterminado: 1730
- Alice puede enviar MAX_PACKET_SIZE_INCLUDED en SYN, no requerido a menos que sea != 1730


### 2) Alice solo ECIES
MTU de 1812 en todos los paquetes.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize predeterminado: 1812
- Alice debe enviar MAX_PACKET_SIZE_INCLUDED en SYN



### 3) Alice de clave dual y sabe que Bob es ElGamal
MTU de 1730 en todos los paquetes.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize predeterminado: 1812
- Alice puede enviar MAX_PACKET_SIZE_INCLUDED en SYN, no requerido a menos que sea != 1730



### 4) Alice de clave dual y sabe que Bob es ECIES
MTU de 1812 en todos los paquetes.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize predeterminado: 1812
- Alice debe enviar MAX_PACKET_SIZE_INCLUDED en SYN



### 5) Alice de clave dual y clave de Bob desconocida
Enviar 1812 como MAX_PACKET_SIZE_INCLUDED en el paquete SYN pero limitar los datos del paquete SYN a 1730.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize predeterminado: 1812
- Alice debe enviar MAX_PACKET_SIZE_INCLUDED en SYN


### Para todos los casos

Alice y Bob calculan
negotiated_mtu, el mínimo entre el MTU de Alice y el de Bob, que se usará como tamaño máximo de datos
en el SYN ACK desde Bob a Alice, y en todos los paquetes posteriores enviados en ambas direcciones.




## Justificación

Véase el [código fuente de Java I2P](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220) para entender por qué el valor actual es 1730.
Véase la [especificación ECIES](/docs/specs/ecies/#overhead) para entender por qué el sobrecoste de ECIES es 82 bytes menor que el de ElGamal.



## Notas de implementación

Si streaming está creando mensajes de tamaño óptimo, es muy importante que
la capa ECIES-Ratchet no agregue relleno más allá de ese tamaño.

El tamaño óptimo de un mensaje Garlic para caber en dos mensajes de túnel,
incluyendo el encabezado I2NP de mensaje Garlic de 16 bytes, 4 bytes de longitud del mensaje Garlic,
8 bytes de etiqueta ES y 16 bytes de MAC, es de 1956 bytes.

Un algoritmo de relleno recomendado en ECIES es el siguiente:

- Si la longitud total del mensaje Garlic sería de 1954-1956 bytes,
  no agregar un bloque de relleno (no hay espacio)
- Si la longitud total del mensaje Garlic sería de 1938-1953 bytes,
  agregar un bloque de relleno para completar exactamente 1956 bytes.
- En otro caso, rellenar como de costumbre, por ejemplo con una cantidad aleatoria de 0-15 bytes.

Estrategias similares podrían usarse en los tamaños óptimos de un mensaje de túnel (964)
y tres mensajes de túnel (2952), aunque estos tamaños deberían ser raros en la práctica.



## Problemas

El valor 1812 es preliminar. Debe confirmarse y posiblemente ajustarse.




## Migración

Sin problemas de compatibilidad hacia atrás.
Esta es una opción existente y la negociación de MTU ya forma parte de la especificación.

Los destinos ECIES antiguos soportarán 1730.
Cualquier cliente que reciba un valor más alto responderá con 1730, y el extremo remoto
negociará hacia abajo, como es habitual.


## Referencias

* [CALCULATION](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220)
* [ECIES](/docs/specs/ecies/#overhead)
* [STREAMING-OPTIONS](/docs/api/streaming/)
* [STREAMING-SPEC](/docs/specs/streaming/#flags-and-option-data-fields)
