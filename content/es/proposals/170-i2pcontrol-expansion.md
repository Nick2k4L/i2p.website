---
title: "i2pcontrol-expansion"
number: "170"
author: "Nick2k4"
created: "2026-05-20"
lastupdated: "2026-05-20"
status: "Abrir"
toc: true
---

Resumen ========

Esta propuesta expone nueva información a la API i2pcontrol, permitiendo una mayor flexibilidad. Esta información incluye: agregar, eliminar, recuperar y modificar libretas de direcciones y servicios ocultos. Esta propuesta también expone más información sobre tu router, como pares (peers), noticias, netDb, y más.

Motivación ==========

La razón de esta propuesta es permitir una mayor flexibilidad en la API de I2P para que las aplicaciones puedan implementar y gestionar una interfaz administrativa de I2P. Exponer dicha información a i2pcontrol permite a los usuarios crear aplicaciones más avanzadas y ofrecer un mejor soporte para la gestión remota.

Diseño ======

Cuando los usuarios interactúen con la API i2pcontrol, podrán acceder a nuevos puntos finales que proporcionan la información mencionada anteriormente. Por ejemplo, la API i2pcontrol expondrá nuevos métodos `TunnelManager` y `AddressBook` que permitirán a los usuarios ingresar parámetros para crear, eliminar, recuperar y modificar túneles y libretas de direcciones. Además, el método preexistente `RouterInfo` tendrá nuevos parámetros para exponer información sobre el router.

Implicaciones de seguridad =====================

No se esperan implicaciones de seguridad adicionales de esta propuesta, ya que la información que se expone ya es accesible mediante otros medios. Sin embargo, es importante asegurar que se implementen mecanismos adecuados de autenticación y autorización para acceder a la API i2pcontrol, a fin de evitar el acceso no autorizado a información sensible o al control del router.

Especificación y Métodos de la API ===========================

Todas las solicitudes siguen la estructura JSON-RPC 2.0:

```json
{
  "jsonrpc": "2.0",
  "method": "MethodName",
  "params": {
    // method-specific parameters
  },
  "id": 1
}
```
Método - RouterInfo -------------------

A continuación se incluyen los nuevos parámetros para el método `RouterInfo` y lo que devuelven:

- `i2p.router.news` - devuelve todas las entradas de noticias del router.
- `i2p.router.id` - devuelve el hash del router como una cadena Base64, o `null`.
- `i2p.router.clockskew` - devuelve la desviación promedio del reloj de los pares, o `null`.
- `i2p.router.info` - devuelve el RouterInfo serializado como una cadena Base64, o `null`.
- `i2p.router.logs` - devuelve los mensajes recientes del registro del router.
- `i2p.router.logs.clear` - limpia el búfer de registro del router y devuelve `"success"`.

- `i2p.router.net.total.received.bytes` - devuelve el total de bytes recibidos desde el inicio. *(adoptado de i2pd)*
- `i2p.router.net.total.sent.bytes` - devuelve el total de bytes enviados desde el inicio. *(adoptado de i2pd)*
- `i2p.router.net.total.transit.bytes` - devuelve el total de bytes en tránsito reenviados desde el inicio. *(adoptado de i2pd)*
- `i2p.router.net.bw.transit.15s` - devuelve el ancho de banda promedio de tránsito en los últimos 15 segundos (bytes/seg). *(adoptado de i2pd)*

- `i2p.router.net.tunnels.shareratio` - devuelve la proporción de compartición de túneles.
- `i2p.router.net.tunnels.participating.info` - devuelve información sobre los túneles participantes.
- `i2p.router.net.tunnels.i2ptunnel` - devuelve la información del controlador de I2PTunnel configurado (estadísticas rápidas de todos).
- `i2p.router.net.tunnels.exploratory.inbound` - devuelve el número de túneles entrantes exploratorios.
- `i2p.router.net.tunnels.exploratory.outbound` - devuelve el número de túneles salientes exploratorios.
- `i2p.router.net.tunnels.exploratory.info.list` - devuelve la lista de información de túneles exploratorios.
- `i2p.router.net.tunnels.client.inbound` - devuelve el número de túneles entrantes del cliente.
- `i2p.router.net.tunnels.client.outbound` - devuelve el número de túneles salientes del cliente.
- `i2p.router.net.tunnels.client.info.list` - devuelve la lista de información de túneles del cliente.

- `i2p.router.net.status.v6` - devuelve el código de estado de la red IPv6. *(adoptado de i2pd)*
- `i2p.router.net.error` - devuelve el código de error de la red IPv4. *(adoptado de i2pd)*
- `i2p.router.net.error.v6` - devuelve el código de error de la red IPv6. *(adoptado de i2pd)*
- `i2p.router.net.testing` - devuelve si la red IPv4 está en estado de prueba (0 o 1). *(adoptado de i2pd)*
- `i2p.router.net.testing.v6` - devuelve si la red IPv6 está en estado de prueba (0 o 1). *(adoptado de i2pd)*

- `i2p.router.net.tunnels.successrate` - devuelve la tasa reciente de éxito en la creación de túneles (%). *(adoptado de i2pd)*
- `i2p.router.net.tunnels.totalsuccessrate` - devuelve la tasa total de éxito en la creación de túneles desde el inicio (%). *(adoptado de i2pd)*
- `i2p.router.net.tunnels.queue` - devuelve el tamaño de la cola de solicitudes de creación de túneles. *(adoptado de i2pd)*
- `i2p.router.net.tunnels.tbmqueue` - devuelve el tamaño de la cola de mensajes de construcción de túneles (Tunnel Build Message). *(adoptado de i2pd)*

- `i2p.router.netdb.peers` - devuelve una lista de hashes de pares conocidos.
- `i2p.router.netdb.activepeers.info` - devuelve datos RouterInfo serializados para los pares activos.
- `i2p.router.netdb.ntcp.limit` - devuelve el límite de conexiones NTCP.
- `i2p.router.netdb.ssu.limit` - devuelve el límite de conexiones SSU.
- `i2p.router.netdb.bannedpeers` - devuelve los pares bloqueados con los detalles del bloqueo.
- `i2p.router.netdb.activepeers.list` - devuelve los hashes de los pares activos.
- `i2p.router.netdb.peers.list` - devuelve los hashes de los pares conocidos.
- `i2p.router.netdb.peers.info` - devuelve datos RouterInfo serializados para los pares conocidos.
- `i2p.router.netdb.activepeers.stats` - devuelve estadísticas de los pares activos.

- `i2p.router.addressbook.private.list` - devuelve las entradas del libro de direcciones privado.
- `i2p.router.addressbook.local.list` - devuelve las entradas del libro de direcciones local.
- `i2p.router.addressbook.router.list` - devuelve las entradas del libro de direcciones del router.
- `i2p.router.addressbook.published.list` - devuelve las entradas del libro de direcciones publicadas.
- `i2p.router.addressbook.subscriptions` - devuelve la ruta del archivo de suscripciones y sus entradas.
- `i2p.router.addressbook.config` - devuelve la ruta del archivo de configuración del libro de direcciones y sus entradas.

Ejemplo:

```json
{
    "jsonrpc": "2.0",
    "method": "RouterInfo",
    "params": {
        "i2p.router.id": "",
    },
    "id": 1
}
```
Devolver:

```json
{
    "jsonrpc": "2.0",
    "result": "{ data }",
    "id": 1
}
```
Método - Libreta de direcciones --------------------

Para el método `AddressBook`, se requieren tres parámetros/argumentos para eliminar y agregar entradas a la libreta de direcciones:

- `Type` - corresponde al tipo de libreta de direcciones:
  - `private`
  - `local`
  - `router`
  - `published`
- `Hostname` - corresponde al nombre de host o nombre de dominio asociado a la entrada en la libreta de direcciones.
- `Destination` - corresponde a la destino asociado a la entrada en la libreta de direcciones.
- `Delete` - este parámetro es opcional y se utiliza para eliminar una entrada de la libreta de direcciones. Si este parámetro no se proporciona, el método agregará una nueva entrada a la libreta de direcciones.

Ejemplo:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "Type": "private",
    "Hostname": "example.i2p",
    "Destination": "exampleDestinationString",
    "Delete": "" <--- this parameter is optional
  },
  "id": 1
}
```
Devolver:

```json
{
  "jsonrpc": "2.0",
  "success": true or false,        
  "message": "Deleted/Added (hostname) in (address book type) address book" OR "Failed to delete/add (hostname) to (address book type) address book",
  "id": 1
}
```
Para editar AddressBookSubscriptions:

- `SetSubscriptions` - este parámetro se utiliza para establecer las suscripciones de una entrada en la libreta de direcciones. Toma como argumento una lista de cadenas de texto.

Ejemplo:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetSubscriptions": ["notbob.i2p", "helloworld.i2p", ...]
  },
  "id": 1
}
```
Devolver:

```json
{
  "jsonrpc": "2.0",
  "success": true,
  "message": "Successfully modified: /path/to/subscriptions.txt"
}
```
Para editar AddressBookConfig:

- `SetConfig` - este parámetro se utiliza para establecer la configuración de una entrada en la libreta de direcciones.

Toma un objeto JSON como argumento, que contiene la configuración.

Parámetros de configuración disponibles/comunes:

- `subscriptions` - archivo que contiene la lista de URLs de suscripción.
- `update_delay` - intervalo de actualización en horas.
- `published_addressbook` - ruta al libro de direcciones publicado.
- `router_addressbook` - ruta al libro de direcciones del router.
- `local_addressbook` - ruta al libro de direcciones local.
- `private_addressbook` - ruta al libro de direcciones privado.
- `proxy_port` - puerto de eepProxy.
- `proxy_host` - nombre de host de eepProxy.
- `should_publish` - indica si se debe actualizar el libro de direcciones publicado.
- `etags` - archivo que contiene las etiquetas etag de las URLs de suscripción.
- `last_modified` - archivo que contiene las marcas de tiempo de última modificación de las URLs de suscripción.
- `log` - ruta del archivo de registro.
- `theme` - tema.

Ejemplo:

```json
{
  "jsonrpc": "2.0",
  "method": "AddressBook",
  "params": {
    "SetConfig": {
      "subscriptions": "subscriptions.txt",
      "update_delay": "12",
      "published_addressbook": "../eepsite/docroot/hosts.txt",
      "router_addressbook": "hosts.txt",
      "local_addressbook": "../userhosts.txt",
      "private_addressbook": "../privatehosts.txt",
      "proxy_port": "4444",
      "proxy_host": "127.0.0.1",
      "should_publish": "true",
      "etags": "etags.txt",
      "last_modified": "last_modified.txt",
      "log": "log.txt",
      "theme": "light"
    }
  },
  "id": 1
}
```
Devolver:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "success": true,
    "message": "Successfully modified: /path/to/config.txt"
  },
  "id": 1
}
```
Método - TunnelManager --------

El método `TunnelManager` se utiliza para crear, editar, obtener, iniciar, detener, reiniciar y eliminar controladores de I2PTunnel.

Parámetros requeridos:

- `Name` - nombre del túnel. Este es el identificador del túnel.
- `Action` - acción a realizar:
  - `create`.
  - `edit`
  - `get`
  - `start`
  - `stop`
  - `restart`
  - `delete`

Parámetros opcionales:

- `All` - booleano, indica si se debe aplicar la acción a todos los túneles. Esto solo es válido para las acciones `start`, `stop` y `restart`.

Tipos de túnel compatibles para `create`:

- `client`
- `httpclient`
- `ircclient`
- `socks`
- `socksirc`
- `connectclient`
- `streamrclient`

- `server`
- `httpserver`
- `httpbidirserver`
- `ircserver`
- `streamrserver`

Parámetros comunes para crear/editar túneles:

- `Type` - tipo de túnel. Requerido para `create`.
- `NewName` - nombre nuevo opcional al editar.
- `Port` - puerto local de escucha.
- `TargetHost` o `Host` - host destino para túneles servidor.
- `TargetPort` - puerto destino para túneles servidor.
- `TargetDestination` o `Destination` - destino para túneles cliente que lo requieran.
- `StartOnLoad` - booleano, indica si el túnel debe iniciarse al cargarse.
- `Description` - descripción del túnel.
- `ReachableBy` - interfaz/dirección en la que escucha el túnel.
- `Shared` - booleano, indica si el túnel cliente debe ser compartido.
- `UseSSL` - booleano, activa SSL donde esté soportado.
- `TunnelLength` - longitud del túnel, de `0` a `3`.
- `TunnelVariance` - variación de la longitud del túnel, de `-2` a `2`.
- `TunnelQuantity` - cantidad de túneles, de `1` a `6`.
- `TunnelBackupQuantity` - cantidad de túneles de respaldo, de `0` a `3`.
- `SigType` - tipo de clave de firma.
- `EncType` - tipo de cifrado.
- `CustomOptions` - opciones personalizadas del túnel.

Opciones de proxy del cliente:

- `ProxyList`
- `UseOutproxyPlugin`
- `ProxyAuth`
- `ProxyUsername`
- `ProxyPassword`
- `OutproxyAuth`
- `OutproxyUsername`
- `OutproxyPassword`
- `OutproxyType`
- `SSLProxies`
- `JumpList`

Opciones de gestión de clientes:

- `ConnectDelay`
- `Profile`
- `DelayOpen`
- `Reduce`
- `ReduceCount`
- `ReduceTime`
- `Close`
- `CloseTime`
- `NewDest`
- `PersistentClientKey`
- `PrivKeyFile`

Opciones de filtrado del cliente HTTP:

- `AllowUserAgent`
- `AllowReferer`
- `AllowAccept`
- `AllowInternalSSL`

Opciones del servidor:

- `WebsiteHostname` o `SpoofedHost`
- `BlockAccessInProxies`
- `BlockUserAgents`
- `UserAgents`
- `UniqueLocalAddressPerClient`
- `BlockReferers`
- `MultiHoming`
- `AccessOption`
- `AccessList`
- `FilterFilePath`
- `MaxConcurrentConns`
- `ClientPerMinute`
- `ClientPerHour`
- `ClientPerDay`
- `TotalInPerMinute`
- `TotalInPerHour`
- `TotalInPerDay`
- `PostLimit`
- `PostLimitTime`
- `PerClientPeriod`
- `TotalPeriod`
- `TotalBanTime`

Opciones de LeaseSet:

- `EncryptLeaseSet` - uno de:
  - `disable`
  - `encrypted (aes)`
  - `blinded`
  - `blinded with lookup password`
  - `encrypted (psk)`
  - `encrypted with lookup password (psk)`
  - `encrypted with per-user key (psk)`
  - `encrypted with lookup password and per-user key (psk)`
  - `encrypted with per-user key (dh)`
  - `encrypted with lookup password and per-user key (dh)`
- `OptionalLookup`
- `LeaseSetClientAuths`

Crear ejemplo:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "create",
    "Type": "client",
    "Port": 7656,
    "TargetDestination": "exampleDestinationString",
    "StartOnLoad": false,
    ....
  },
  "id": 1
}
```
Devolver:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - created tunnel example-client" OR "error - { error message }",
    "results": [ {/* information about where persistent keys are stored */} ]
  },
  "id": 1
}
```
Ejemplo de edición:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "edit",
    "NewName": "renamed-client",
    "Port": 7657,
    "TargetDestination": "newDestinationString",
    "StartOnLoad": true
  },
  "id": 1
}
```
Devolver:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - edited tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
Ejemplo de obtención:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "get"
  },
  "id": 1
}
```
Devolver:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - options for example-client" OR "error - { error message }",
    "info": {
      "client": true,
      "status": "running",
      "persistentClientKey": false,
      "offlineKeys": false,
      "targetDestination": "exampleDestinationString",
      "localDestination": "exampleBase64Destination",
      "destination": "exampleBase64Destination",
      "destinationB32": "example.b32.i2p",
      "rawConfig": {
        "name": "example-client",
        "type": "client"
      }
    }
  },
  "id": 1
}
```
Ejemplo de Iniciar, Detener, Reiniciar, Eliminar. Siguen la misma estructura, solo que con diferentes parámetros `Action`:

```json
{
  "jsonrpc": "2.0",
  "method": "TunnelManager",
  "params": {
    "Name": "example-client",
    "Action": "start"
  },
  "id": 1
}
```
Devolver:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "success - starting tunnel example-client" OR "error - { error message }"
  },
  "id": 1
}
```
Método - ClientServicesInfo *(adoptado de i2pd)* -------------------------------------------------

El método `ClientServicesInfo` devuelve información de estado sobre los servicios cliente que se ejecutan en el router. Incluya las claves de servicio deseadas (con cualquier valor) en `params` para solicitar el estado de cada servicio.

Parámetros soportados:

- `I2PTunnel` - devuelve un mapa de los nombres de túneles configurados a sus direcciones, dividido en subobjetos `client` y `server`.
- `HTTPProxy` - devuelve el estado de habilitación del proxy HTTP y su dirección.
- `SOCKS` - devuelve el estado de habilitación del proxy SOCKS y su dirección.
- `SAM` - devuelve el estado de habilitación del puente SAM y la información de sesiones activas.
- `BOB` - devuelve el estado de habilitación del puente BOB. (Obsoleto en Java I2P; siempre devuelve `false`.)
- `I2CP` - devuelve el estado de habilitación del servidor I2CP.

Ejemplo:

```json
{
  "jsonrpc": "2.0",
  "method": "ClientServicesInfo",
  "params": {
    "I2PTunnel": "",
    "SAM": ""
  },
  "id": 1
}
```
Devolver:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "I2PTunnel": {
      "client": {"my-client": {"address": "example.b32.i2p"}},
      "server": {"my-server": {"address": "example.b32.i2p", "port": 8080}}
    },
    "SAM": {
      "enabled": true,
      "sessions": {}
    }
  },
  "id": 1
}
```
Compatibilidad =============

Debe mantenerse la compatibilidad con la API i2pcontrol existente, ya que los nuevos métodos y parámetros se añaden de forma que no interfieren con la funcionalidad actual. Las aplicaciones existentes que utilicen la API i2pcontrol deben seguir funcionando sin modificaciones, mientras que las nuevas aplicaciones podrán aprovechar la información adicional y las capacidades proporcionadas por esta propuesta.

Implementación ==============

Java I2P --------

Esta propuesta aún no se ha implementado en Java I2P, aunque el código está disponible en el repositorio [i2p.plugins.i2pcontrol](https://github.com/i2p/i2p.plugins.i2pcontrol) bajo la solicitud de incorporación [#6](https://github.com/i2p/i2p.plugins.i2pcontrol/pull/6). Esto se hizo para permitir la prueba y el desarrollo de los nuevos métodos sin afectar el código existente. Una vez que el código esté listo para uso en producción, se actualizará en el repositorio principal de I2P dentro del directorio i2pcontrol.

i2pd ----

Los métodos y parámetros marcados como "(adoptados de i2pd)" están implementados en i2pd y no se modifican en esta propuesta. Las extensiones de i2pd no requerirán modificaciones como parte de esta propuesta. Las partes no marcadas de esta propuesta no están implementadas en i2pd.

go-i2p ------

go-i2p tiene la motivación de llevar a cabo esta propuesta con el fin de habilitar y mejorar su aplicación de consola del router. Adoptará e implementará la propuesta en el futuro.

emissary --------

La probabilidad de adopción en Emissary es desconocida en este momento, sin embargo, es probable que Emissary se beneficie de esta propuesta de las mismas formas que go-i2p.

Rendimiento ===========

No se espera impacto en el rendimiento.
