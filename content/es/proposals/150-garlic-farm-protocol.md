---
title: "Protocolo de la Granja de Ajo"
number: "150"
author: "zzz"
created: "2019-05-02"
lastupdated: "2019-05-20"
status: "Abierto"
thread: "http://zzz.i2p/topics/2234"
toc: true
---
## Descripción general

Esta es la especificación del protocolo de red Garlic Farm,
basado en JRaft, su código "exts" para implementación sobre TCP,
y su aplicación de ejemplo "dmprinter" [JRAFT](https://github.com/datatechnology/jraft).


No pudimos encontrar ninguna implementación con un protocolo de red documentado.
Sin embargo, la implementación de JRaft es lo suficientemente simple como para que pudiéramos
inspeccionar el código y luego documentar su protocolo.
Esta propuesta es el resultado de ese esfuerzo.

Esto será el backend para la coordinación de routers que publican
entradas en un Meta LeaseSet. Ver propuesta 123.


## Objetivos

- Pequeño tamaño de código
- Basado en una implementación existente
- Sin objetos Java serializados ni características o codificaciones específicas de Java
- Cualquier proceso de arranque queda fuera del alcance. Se asume que al menos otro servidor
  está codificado directamente o configurado fuera de banda respecto a este protocolo.
- Soportar casos de uso tanto fuera de banda como dentro de I2P.


## Diseño

El protocolo Raft no es un protocolo concreto; solo define una máquina de estados.
Por lo tanto, documentamos el protocolo concreto de JRaft y basamos nuestro protocolo en él.
No hay cambios en el protocolo JRaft más allá de la adición de
un handshake de autenticación.

Raft elige un Líder cuyo trabajo consiste en publicar un registro (log).
El registro contiene datos de configuración de Raft y datos de aplicación.
Los datos de aplicación contienen el estado de cada Router del Servidor y el Destino
para el clúster Meta LS2.
Los servidores usan un algoritmo común para determinar el publicador y el contenido
del Meta LS2.
El publicador del Meta LS2 NO es necesariamente el Líder de Raft.



## Especificación

El protocolo de red utiliza sockets SSL o sockets I2P sin SSL.
Los sockets I2P se transmiten a través del Proxy HTTP.
No hay soporte para sockets sin SSL en clearnet.

### Handshake y autenticación

No definido por JRaft.

Objetivos:

- Método de autenticación usuario/contraseña
- Identificador de versión
- Identificador de clúster
- Extensible
- Facilidad de proxy cuando se usa para sockets I2P
- No exponer innecesariamente al servidor como servidor Garlic Farm
- Protocolo simple para que no se requiera una implementación completa de servidor web
- Compatible con estándares comunes, para que las implementaciones puedan usar
  bibliotecas estándar si se desea

Usaremos un handshake similar al de websocket y
autenticación HTTP Digest [RFC 2617](https://tools.ietf.org/html/rfc2617).
No se admite la autenticación básica de RFC 2617.
Al transmitir a través del proxy HTTP, comuníquese con
el proxy según lo especificado en [RFC 2616](https://tools.ietf.org/html/rfc2616).

#### Credenciales

Si los nombres de usuario y contraseñas son por clúster o
por servidor, depende de la implementación.


#### Solicitud HTTP 1

El originador enviará lo siguiente.

Todas las líneas terminan con CRLF según requiere HTTP.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: close
  (cualquier otra cabecera ignorada)
  (línea en blanco)

  CLUSTER es el nombre del clúster (por defecto "farm")
  VERSION es la versión de Garlic Farm (actualmente "1")

```


#### Respuesta HTTP 1

Si la ruta no es correcta, el destinatario enviará una respuesta estándar "HTTP/1.1 404 Not Found",
como en [RFC 2616](https://tools.ietf.org/html/rfc2616).

Si la ruta es correcta, el destinatario enviará una respuesta estándar "HTTP/1.1 401 Unauthorized",
incluyendo la cabecera WWW-Authenticate de autenticación digest HTTP,
como en [RFC 2617](https://tools.ietf.org/html/rfc2617).

Ambas partes cerrarán entonces el socket.


#### Solicitud HTTP 2

El originador enviará lo siguiente,
como en [RFC 2617](https://tools.ietf.org/html/rfc2617).

Todas las líneas terminan con CRLF según requiere HTTP.

```text

GET /GarlicFarm/CLUSTER/VERSION/websocket HTTP/1.1
  Host: (ip):(port)
  Cache-Control: no-cache
  Connection: keep-alive, Upgrade
  Upgrade: websocket
  (cabeceras Sec-Websocket-* si está transmitido)
  Authorization: (cabecera de autorización digest HTTP como en RFC 2617)
  (cualquier otra cabecera ignorada)
  (línea en blanco)

  CLUSTER es el nombre del clúster (por defecto "farm")
  VERSION es la versión de Garlic Farm (actualmente "1")

```


#### Respuesta HTTP 2

Si la autenticación no es correcta, el destinatario enviará otra respuesta estándar "HTTP/1.1 401 Unauthorized",
como en [RFC 2617](https://tools.ietf.org/html/rfc2617).

Si la autenticación es correcta, el destinatario enviará la siguiente respuesta,
como en el protocolo WebSocket.

Todas las líneas terminan con CRLF según requiere HTTP.

```text

HTTP/1.1 101 Switching Protocols
  Connection: Upgrade
  Upgrade: websocket
  (cabeceras Sec-Websocket-*)
  (cualquier otra cabecera ignorada)
  (línea en blanco)

```

Después de recibir esto, el socket permanece abierto.
El protocolo Raft, definido a continuación, comienza en el mismo socket.


#### Caché

Las credenciales deben almacenarse en caché al menos una hora, para que
las conexiones posteriores puedan saltar directamente a
"Solicitud HTTP 2" anterior.



### Tipos de mensajes

Hay dos tipos de mensajes: solicitudes y respuestas.
Las solicitudes pueden contener entradas de registro (log entries) y son de tamaño variable;
las respuestas no contienen entradas de registro y son de tamaño fijo.

Los tipos de mensaje 1-4 son los mensajes RPC estándar definidos por Raft.
Este es el protocolo Raft principal.

Los tipos de mensaje 5-15 son los mensajes RPC extendidos definidos por
JRaft, para soportar clientes, cambios dinámicos de servidores y
sincronización eficiente del registro.

Los tipos de mensaje 16-17 son los mensajes RPC de compactación de registro definidos
en la sección 7 de Raft.


| Mensaje | Número | Enviado por | Enviado a | Notas |
| :--- | :--- | :--- | :--- | :--- |
| RequestVoteRequest | 1 | Candidato | Seguidor | RPC estándar de Raft; no debe contener entradas de registro |
| RequestVoteResponse | 2 | Seguidor | Candidato | RPC estándar de Raft |
| AppendEntriesRequest | 3 | Líder | Seguidor | RPC estándar de Raft |
| AppendEntriesResponse | 4 | Seguidor | Líder / Cliente | RPC estándar de Raft |
| ClientRequest | 5 | Cliente | Líder / Seguidor | La respuesta es AppendEntriesResponse; debe contener solo entradas de registro de aplicación |
| AddServerRequest | 6 | Cliente | Líder | Debe contener solo una entrada de registro ClusterServer |
| AddServerResponse | 7 | Líder | Cliente | El Líder también enviará un JoinClusterRequest |
| RemoveServerRequest | 8 | Seguidor | Líder | Debe contener solo una entrada de registro ClusterServer |
| RemoveServerResponse | 9 | Líder | Seguidor | |
| SyncLogRequest | 10 | Líder | Seguidor | Debe contener solo una entrada de registro LogPack |
| SyncLogResponse | 11 | Seguidor | Líder | |
| JoinClusterRequest | 12 | Líder | Nuevo Servidor | Invitación para unirse; debe contener solo una entrada de registro de Configuración |
| JoinClusterResponse | 13 | Nuevo Servidor | Líder | |
| LeaveClusterRequest | 14 | Líder | Seguidor | Comando para salir |
| LeaveClusterResponse | 15 | Seguidor | Líder | |
| InstallSnapshotRequest | 16 | Líder | Seguidor | Sección 7 de Raft; debe contener solo una entrada de registro SnapshotSyncRequest |
| InstallSnapshotResponse | 17 | Seguidor | Líder | Sección 7 de Raft |


### Establecimiento

Después del handshake HTTP, la secuencia de establecimiento es la siguiente:

```text

Nuevo Servidor Alice              Seguidor aleatorio Bob

  ClientRequest   ------->
          <---------   AppendEntriesResponse

  Si Bob dice que es el líder, continúe como abajo.
  De lo contrario, Alice debe desconectarse de Bob y conectarse al líder.


  Nuevo Servidor Alice              Líder Charlie

  ClientRequest   ------->
          <---------   AppendEntriesResponse
  AddServerRequest   ------->
          <---------   AddServerResponse
          <---------   JoinClusterRequest
  JoinClusterResponse  ------->
          <---------   SyncLogRequest
                       OR InstallSnapshotRequest
  SyncLogResponse  ------->
  OR InstallSnapshotResponse

```

Secuencia de desconexión:

```text

Seguidor Alice              Líder Charlie

  RemoveServerRequest   ------->
          <---------   RemoveServerResponse
          <---------   LeaveClusterRequest
  LeaveClusterResponse  ------->

```

Secuencia de elección:

```text

Candidato Alice               Seguidor Bob

  RequestVoteRequest   ------->
          <---------   RequestVoteResponse

  si Alice gana la elección:

  Líder Alice                Seguidor Bob

  AppendEntriesRequest   ------->
  (heartbeat)
          <---------   AppendEntriesResponse

```


### Definiciones

- Origen: Identifica al originador del mensaje
- Destino: Identifica al destinatario del mensaje
- Términos: Ver Raft. Inicializados a 0, aumentan monótonamente
- Índices: Ver Raft. Inicializados a 0, aumentan monótonamente



### Solicitudes

Las solicitudes contienen un encabezado y cero o más entradas de registro.
Las solicitudes contienen un encabezado de tamaño fijo y entradas de registro opcionales de tamaño variable.


#### Encabezado de solicitud

El encabezado de solicitud tiene 45 bytes, como sigue.
Todos los valores son enteros sin signo en orden big-endian.

```text

Tipo de mensaje:      1 byte
  Origen:               ID, entero de 4 bytes
  Destino:              ID, entero de 4 bytes
  Término:              Término actual (ver notas), entero de 8 bytes
  Último término de registro:     entero de 8 bytes
  Último índice de registro:    entero de 8 bytes
  Índice de confirmación:      entero de 8 bytes
  Tamaño de entradas de registro:  Tamaño total en bytes, entero de 4 bytes
  Entradas de registro:       ver abajo, longitud total según especificado

```


#### Notas

En RequestVoteRequest, Término es el término del candidato.
En otro caso, es el término actual del líder.

En AppendEntriesRequest, cuando el tamaño de las entradas de registro es cero,
este mensaje es un mensaje de latido (heartbeat o keepalive).



#### Entradas de registro

El registro contiene cero o más entradas de registro.
Cada entrada de registro es como sigue.
Todos los valores son enteros sin signo en orden big-endian.

```text

Término:           entero de 8 bytes
  Tipo de valor:     1 byte
  Tamaño de entrada: En bytes, entero de 4 bytes
  Entrada:          longitud según especificado

```


#### Contenido del registro

Todos los valores son enteros sin signo en orden big-endian.

| Tipo de valor de registro | Número |
| :--- | :--- |
| Aplicación | 1 |
| Configuración | 2 |
| ClusterServer | 3 |
| LogPack | 4 |
| SnapshotSyncRequest | 5 |


#### Aplicación

El contenido de la aplicación está codificado en UTF-8 [JSON](https://www.json.org/).
Ver la sección Capa de Aplicación más abajo.


#### Configuración

Se utiliza para que el líder serialice una nueva configuración de clúster y la replique a los pares.
Contiene cero o más configuraciones ClusterServer.


```text

Índice de registro:  entero de 8 bytes
  Último índice de registro:  entero de 8 bytes
  Datos ClusterServer para cada servidor:
    ID:                entero de 4 bytes
    Longitud de datos de punto final: En bytes, entero de 4 bytes
    Datos de punto final:     cadena ASCII de la forma "tcp://localhost:9001", longitud según especificado

```


#### ClusterServer

La información de configuración para un servidor en un clúster.
Esto se incluye solo en un mensaje AddServerRequest o RemoveServerRequest.

Cuando se usa en un mensaje AddServerRequest:

```text

ID:                entero de 4 bytes
  Longitud de datos de punto final: En bytes, entero de 4 bytes
  Datos de punto final:     cadena ASCII de la forma "tcp://localhost:9001", longitud según especificado

```


Cuando se usa en un mensaje RemoveServerRequest:

```text

ID:                entero de 4 bytes

```


#### LogPack

Esto se incluye solo en un mensaje SyncLogRequest.

Lo siguiente se comprime con gzip antes de la transmisión:


```text

Longitud de datos de índice: En bytes, entero de 4 bytes
  Longitud de datos de registro:   En bytes, entero de 4 bytes
  Datos de índice:     8 bytes para cada índice, longitud según especificado
  Datos de registro:       longitud según especificado

```



#### SnapshotSyncRequest

Esto se incluye solo en un mensaje InstallSnapshotRequest.

```text

Último índice de registro:  entero de 8 bytes
  Último término de registro:   entero de 8 bytes
  Longitud de datos de configuración: En bytes, entero de 4 bytes
  Datos de configuración:     longitud según especificado
  Desplazamiento:          El desplazamiento de los datos en la base de datos, en bytes, entero de 8 bytes
  Longitud de datos:        En bytes, entero de 4 bytes
  Datos:            longitud según especificado
  Está terminado:         1 si está terminado, 0 si no (1 byte)

```




### Respuestas

Todas las respuestas tienen 26 bytes, como sigue.
Todos los valores son enteros sin signo en orden big-endian.

```text

Tipo de mensaje:   1 byte
  Origen:         ID, entero de 4 bytes
  Destino:    Normalmente el ID del destinatario real (ver notas), entero de 4 bytes
  Término:           Término actual, entero de 8 bytes
  Siguiente índice:     Inicializado al último índice de registro del líder + 1, entero de 8 bytes
  Está aceptado:    1 si aceptado, 0 si no aceptado (ver notas), 1 byte

```


#### Notas

El ID de destino es normalmente el destinatario real de este mensaje.
Sin embargo, para AppendEntriesResponse, AddServerResponse y RemoveServerResponse,
es el ID del líder actual.

En RequestVoteResponse, Está aceptado es 1 si se vota por el candidato (solicitante),
y 0 si no se vota.


## Capa de Aplicación

Cada servidor publica periódicamente datos de Aplicación en el registro mediante una ClientRequest.
Los datos de Aplicación contienen el estado de cada Router del Servidor y el Destino
para el clúster Meta LS2.
Los servidores usan un algoritmo común para determinar el publicador y el contenido
del Meta LS2.
El servidor con el estado más "óptimo" reciente en el registro es el publicador del Meta LS2.
El publicador del Meta LS2 NO es necesariamente el Líder de Raft.


### Contenido de los datos de Aplicación

El contenido de la aplicación está codificado en UTF-8 [JSON](https://json.org/),
por simplicidad y extensibilidad.
La especificación completa está por determinar.
El objetivo es proporcionar suficientes datos para escribir un algoritmo que determine el
router "mejor" para publicar el Meta LS2, y para que el publicador tenga suficiente información
para ponderar los Destinos en el Meta LS2.
Los datos contendrán estadísticas tanto del router como de los Destinos.

Los datos pueden contener opcionalmente datos de detección remota sobre la salud de
otros servidores y la capacidad de obtener el Meta LS.
Estos datos no estarían soportados en la primera versión.

Los datos pueden contener opcionalmente información de configuración publicada
por un cliente administrador.
Estos datos no estarían soportados en la primera versión.

Si se lista "nombre: valor", eso especifica la clave y el valor del mapa JSON.
De lo contrario, la especificación está por determinar.


Datos del clúster (nivel superior):

- cluster: Nombre del clúster
- date: Fecha de estos datos (long, ms desde la época)
- id: ID de Raft (entero)

Datos de configuración (config):

- Cualquier parámetro de configuración

Estado de publicación de MetaLS (meta):

- destination: destino de metals, en base64
- lastPublishedLS: si está presente, codificación en base64 del último metals publicado
- lastPublishedTime: en ms, o 0 si nunca
- publishConfig: estado de configuración del publicador: off/on/auto
- publishing: estado booleano del publicador de metals: verdadero/falso

Datos del router (router):

- lastPublishedRI: si está presente, codificación en base64 de la última información del router publicada
- uptime: Tiempo de actividad en ms
- Retraso de tareas (Job lag)
- Túneles exploratorios
- Túneles participantes
- Ancho de banda configurado
- Ancho de banda actual

Destinos (destinations):
Lista

Datos del destino:

- destination: el destino, en base64
- uptime: Tiempo de actividad en ms
- Túneles configurados
- Túneles actuales
- Ancho de banda configurado
- Ancho de banda actual
- Conexiones configuradas
- Conexiones actuales
- Datos de lista negra

Datos de detección remota del router:

- Última versión de RI vista
- Tiempo de obtención de LS
- Datos de prueba de conexión
- Datos de perfil de floodfills más cercanos
  para los períodos de ayer, hoy y mañana

Datos de detección remota del destino:

- Última versión de LS vista
- Tiempo de obtención de LS
- Datos de prueba de conexión
- Datos de perfil de floodfills más cercanos
  para los períodos de ayer, hoy y mañana

Datos de detección de Meta LS:

- Última versión vista
- Tiempo de obtención
- Datos de perfil de floodfills más cercanos
  para los períodos de ayer, hoy y mañana


## Interfaz de administración

Por determinar, posiblemente una propuesta separada.
No requerida para la primera versión.

Requisitos de una interfaz de administración:

- Soporte para múltiples destinos maestros, es decir, múltiples clústeres virtuales (farms)
- Proporcionar una vista completa del estado compartido del clúster: todas las estadísticas publicadas por los miembros, quién es el líder actual, etc.
- Capacidad para forzar la eliminación de un participante o líder del clúster
- Capacidad para forzar la publicación de metaLS (si el nodo actual es el publicador)
- Capacidad para excluir hashes de metaLS (si el nodo actual es el publicador)
- Funcionalidad de importación/exportación de configuración para despliegues masivos



## Interfaz del router

Por determinar, posiblemente una propuesta separada.
i2pcontrol no es requerido para la primera versión y los cambios detallados se incluirán en una propuesta separada.

Requisitos para la API de Garlic Farm al router (java en-JVM o i2pcontrol)

- getLocalRouterStatus()
- getLocalLeafHash(Hash masterHash)
- getLocalLeafStatus(Hash leaf)
- getRemoteMeasuredStatus(Hash masterOrLeaf) // probablemente no en MVP
- publishMetaLS(Hash masterHash, List<MetaLease> contents) // o MetaLeaseSet firmado? ¿Quién firma?
- stopPublishingMetaLS(Hash masterHash)
- autenticación por determinar?


## Justificación

Atomix es demasiado grande y no permitirá la personalización necesaria para enrutar
el protocolo sobre I2P. Además, su formato de red no está documentado y depende
de la serialización de Java.


## Notas



## Problemas

- No hay forma de que un cliente descubra y se conecte a un líder desconocido.
  Sería un cambio menor que un Seguidor envíe la Configuración como una Entrada de Registro en AppendEntriesResponse.



## Migración

No hay problemas de compatibilidad hacia atrás.


## Referencias

* [JRAFT](https://github.com/datatechnology/jraft)
* [JSON](https://json.org/)
* [RAFT](/docs/research/ongaro2014-raft.pdf)
* [RFC-2616](https://tools.ietf.org/html/rfc2616)
* [RFC-2617](https://tools.ietf.org/html/rfc2617)
* [WEBSOCKET](https://en.wikipedia.org/wiki/WebSocket)
