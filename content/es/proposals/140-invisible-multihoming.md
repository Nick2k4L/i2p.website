---
title: "Multihoming Invisible"
number: "140"
author: "str4d"
created: "2017-05-22"
lastupdated: "2017-07-04"
status: "Abrir"
thread: "http://zzz.i2p/topics/2335"
toc: true
---
## Descripción general

Esta propuesta describe un diseño para un protocolo que permita a un cliente, servicio de I2P o proceso equilibrador externo gestionar múltiples routers que alojan de forma transparente un único [Destination](/docs/specs/common-structures/#destination).

La propuesta actualmente no especifica una implementación concreta. Podría implementarse como una extensión de [I2CP](/docs/specs/i2cp/), o como un nuevo protocolo.


## Motivación

El multihoming consiste en usar múltiples routers para alojar el mismo Destination. La forma actual de hacer multihoming con I2P es ejecutar el mismo Destination en cada router de forma independiente; el router que utilizan los clientes en un momento determinado es el último en publicar un LeaseSet.

Esto es un "hack" y presumiblemente no funcionará para sitios web grandes a escala. Supongamos que tenemos 100 routers con multihoming, cada uno con 16 túneles. Eso supone 1600 publicaciones de LeaseSet cada 10 minutos, o casi 3 por segundo. Los floodfills se verían abrumados y se activarían los límites. Y eso sin mencionar aún el tráfico de búsquedas.

La Propuesta 123 resuelve este problema con un meta-LeaseSet, que enumera los 100 hashes reales de LeaseSet. Una búsqueda se convierte en un proceso de dos etapas: primero buscar el meta-LeaseSet, y luego uno de los LeaseSets nombrados. Esta es una buena solución al problema del tráfico de búsquedas, pero por sí sola crea una fuga significativa de privacidad: es posible determinar qué routers con multihoming están en línea mediante el monitoreo del meta-LeaseSet publicado, porque cada LeaseSet real corresponde a un único router.

Necesitamos una forma de que un cliente o servicio de I2P pueda distribuir un único Destination a través de múltiples routers, de una manera indistinguible del uso de un solo router (desde la perspectiva del propio LeaseSet).


## Diseño

### Definiciones

    User
        La persona u organización que desea hacer multihoming de sus Destination(s). Aquí se considera un único Destination sin pérdida de generalidad (WLOG).

    Client
        La aplicación o servicio que se ejecuta detrás del Destination. Puede ser una aplicación cliente, servidor o peer-to-peer; nos referimos a ella como cliente en el sentido de que se conecta a los routers de I2P.

        El cliente consta de tres partes, que pueden estar todas en el mismo proceso o distribuidas entre procesos o máquinas (en una configuración multi-cliente):

        Balancer
            La parte del cliente que gestiona la selección de pares y la construcción de túneles. Hay un único balancer en cada momento, y se comunica con todos los routers de I2P. Puede haber balancers de respaldo.

        Frontend
            La parte del cliente que puede operarse en paralelo. Cada frontend se comunica con un único router de I2P.

        Backend
            La parte del cliente compartida entre todos los frontends. No tiene comunicación directa con ningún router de I2P.

    Router
        Un router de I2P ejecutado por el usuario que se sitúa en el límite entre la red I2P y la red del usuario (similar a un dispositivo perimetral en redes corporativas). Construye túneles bajo el comando de un balancer, y enruta paquetes para un cliente o frontend.

### Visión general de alto nivel

Imaginemos la siguiente configuración deseada:

- Una aplicación cliente con un Destination.
- Cuatro routers, cada uno gestionando tres túneles entrantes.
- Los doce túneles deben publicarse en un único LeaseSet.

### Cliente único

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]-----
                 |-{ [Tunnel 3]===/               \
                 |                                 \
                 |-{ [Tunnel 4]===\                 \
  [Destination]  |-{ [Tunnel 5]====[Router 2]-----   \
    \            |-{ [Tunnel 6]===/               \   \
     [LeaseSet]--|                               [Client]
                 |-{ [Tunnel 7]===\               /   /
                 |-{ [Tunnel 8]====[Router 3]-----   /
                 |-{ [Tunnel 9]===/                 /
                 |                                 /
                 |-{ [Tunnel 10]==\               /
                 |-{ [Tunnel 11]===[Router 4]-----
                  -{ [Tunnel 12]==/
```

### Cliente múltiple

```
                -{ [Tunnel 1]===\
                 |-{ [Tunnel 2]====[Router 1]---------[Frontend 1]
                 |-{ [Tunnel 3]===/          \                    \
                 |                            \                    \
                 |-{ [Tunnel 4]===\            \                    \
  [Destination]  |-{ [Tunnel 5]====[Router 2]---\-----[Frontend 2]   \
    \            |-{ [Tunnel 6]===/          \   \                \   \
     [LeaseSet]--|                         [Balancer]            [Backend]
                 |-{ [Tunnel 7]===\          /   /                /   /
                 |-{ [Tunnel 8]====[Router 3]---/-----[Frontend 3]   /
                 |-{ [Tunnel 9]===/            /                    /
                 |                            /                    /
                 |-{ [Tunnel 10]==\          /                    /
                 |-{ [Tunnel 11]===[Router 4]---------[Frontend 4]
                  -{ [Tunnel 12]==/
```

### Proceso general del cliente

- Cargar o generar un Destination.

- Abrir una sesión con cada router, asociada al Destination.

- Periódicamente (aproximadamente cada diez minutos, aunque puede variar según la vigencia de los túneles):

  - Obtener la capa rápida (fast tier) de cada router.

  - Usar el conjunto total de pares para construir túneles hacia y desde cada router.

    - Por defecto, los túneles hacia/desde un router determinado usarán pares de la capa rápida de ese router, pero esto no está impuesto por el protocolo.

  - Recopilar el conjunto de túneles entrantes activos de todos los routers activos, y crear un LeaseSet.

  - Publicar el LeaseSet a través de uno o más de los routers.

### Diferencias con I2CP

Para crear y gestionar esta configuración, el cliente necesita la siguiente funcionalidad nueva además de la proporcionada actualmente por [I2CP](/docs/specs/i2cp/):

- Indicar a un router que construya túneles sin crear un LeaseSet para ellos.
- Obtener una lista de los túneles actuales en el grupo entrante (inbound pool).

Adicionalmente, la siguiente funcionalidad permitiría una flexibilidad significativa en cómo el cliente gestiona sus túneles:

- Obtener el contenido de la capa rápida (fast tier) de un router.
- Indicar a un router que construya un túnel entrante o saliente usando una lista determinada de pares.

### Esquema del protocolo

```
         Client                           Router

                    --------------------->  Create Session
   Session Status  <---------------------
                    --------------------->  Get Fast Tier
        Peer List  <---------------------
                    --------------------->  Create Tunnel
    Tunnel Status  <---------------------
                    --------------------->  Get Tunnel Pool
      Tunnel List  <---------------------
                    --------------------->  Publish LeaseSet
                    --------------------->  Send Packet
      Send Status  <---------------------
  Packet Received  <---------------------
```

### Mensajes

**Create Session**
- Crear una sesión para el Destination dado.

**Session Status**
- Confirmación de que la sesión se ha configurado, y que el cliente puede comenzar a construir túneles.

**Get Fast Tier**
- Solicitar una lista de los pares que el router actualmente consideraría para construir túneles.

**Peer List**
- Una lista de pares conocidos por el router.

**Create Tunnel**
- Solicitar que el router construya un nuevo túnel a través de los pares especificados.

**Tunnel Status**
- El resultado de una construcción de túnel particular, una vez disponible.

**Get Tunnel Pool**
- Solicitar una lista de los túneles actuales en el grupo entrante o saliente para el Destination.

**Tunnel List**
- Una lista de túneles para el grupo solicitado.

**Publish LeaseSet**
- Solicitar que el router publique el LeaseSet proporcionado a través de uno de los túneles salientes para el Destination. No se requiere estado de respuesta; el router debe seguir intentándolo hasta que esté satisfecho de que el LeaseSet ha sido publicado.

**Send Packet**
- Un paquete saliente del cliente. Opcionalmente especifica un túnel saliente por el cual el paquete debe (¿debería?) enviarse.

**Send Status**
- Informa al cliente del éxito o fracaso al enviar un paquete.

**Packet Received**
- Un paquete entrante para el cliente. Opcionalmente especifica el túnel entrante por el cual se recibió el paquete(?)


## Implicaciones de seguridad

Desde la perspectiva de los routers, este diseño es funcionalmente equivalente al estado actual. El router sigue construyendo todos los túneles, mantiene sus propios perfiles de pares y aplica separación entre operaciones del router y del cliente. En la configuración predeterminada es completamente idéntico, porque los túneles para ese router se construyen a partir de su propia capa rápida.

Desde la perspectiva de la netDB, un único LeaseSet creado mediante este protocolo es idéntico al estado actual, porque aprovecha funcionalidad ya existente. Sin embargo, para LeaseSets más grandes que se acerquen a 16 Leases, podría ser posible para un observador determinar que el LeaseSet tiene multihoming:

- El tamaño máximo actual de la capa rápida es de 75 pares. La puerta de enlace entrante (IBGW, el nodo publicado en un Lease) se selecciona de una fracción de la capa (particionada aleatoriamente por grupo de túneles mediante hash, no por cantidad):

      1 salto
          Toda la capa rápida

      2 saltos
          La mitad de la capa rápida
          (el valor predeterminado hasta mediados de 2014)

      3+ saltos
          Un cuarto de la capa rápida
          (3 es el valor predeterminado actual)

  Esto significa que, en promedio, los IBGW estarán seleccionados de un conjunto de 20-30 pares.

- En una configuración con un solo router, un LeaseSet completo de 16 túneles tendría 16 IBGW seleccionados aleatoriamente de un conjunto de hasta (digamos) 20 pares.

- En una configuración de multihoming con 4 routers usando la configuración predeterminada, un LeaseSet completo de 16 túneles tendría 16 IBGW seleccionados aleatoriamente de un conjunto de hasta 80 pares, aunque probablemente haya una fracción de pares comunes entre routers.

Por tanto, con la configuración predeterminada, podría ser posible mediante análisis estadístico determinar que un LeaseSet está siendo generado por este protocolo. También podría ser posible determinar cuántos routers hay, aunque el efecto de la rotación (churn) en las capas rápidas reduciría la efectividad de este análisis.

Como el cliente tiene control total sobre qué pares selecciona, esta fuga de información podría reducirse o eliminarse seleccionando IBGWs de un conjunto reducido de pares.


## Compatibilidad

Este diseño es completamente compatible con versiones anteriores de la red, porque no hay cambios en el formato del LeaseSet. Todos los routers necesitarían conocer el nuevo protocolo, pero esto no es un problema ya que todos estarían controlados por la misma entidad.


## Notas sobre rendimiento y escalabilidad

El límite superior de 16 Leases por LeaseSet no se ve alterado por esta propuesta. Para Destinations que requieran más túneles, existen dos posibles modificaciones de red:

- Aumentar el límite superior del tamaño de los LeaseSets. Sería lo más sencillo de implementar (aunque aún requeriría soporte generalizado en la red antes de poder usarse ampliamente), pero podría resultar en búsquedas más lentas debido al mayor tamaño de los paquetes. El tamaño máximo factible de un LeaseSet está definido por la MTU de los transportes subyacentes, y por tanto es de aproximadamente 16kB.

- Implementar la Propuesta 123 para LeaseSets jerárquicos. En combinación con esta propuesta, los Destinations para los sub-LeaseSets podrían distribuirse entre múltiples routers, actuando efectivamente como múltiples direcciones IP para un servicio en claro.


## Agradecimientos

Gracias a psi por la discusión que condujo a esta propuesta.


## Referencias

* [Destination](/docs/specs/common-structures/#destination)
* [I2CP](/docs/specs/i2cp/)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [Prop123](/proposals/123-new-netdb-entries/)
