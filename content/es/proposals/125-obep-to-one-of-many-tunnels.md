---
title: "Entrega OBEP a Túneles 1-de-N o N-de-N"
number: "125"
author: "zzz, str4d"
created: "2016-03-10"
lastupdated: "2017-04-07"
status: "Open"
thread: "http://zzz.i2p/topics/2099"
toc: true
---
## Descripción general

Esta propuesta abarca dos mejoras para aumentar el rendimiento de la red:

- Delegar la selección del IBGW al OBEP proporcionándole una lista de
  alternativas en lugar de una única opción.

- Habilitar el enrutamiento de paquetes multicast en el OBEP.


## Motivación

En el caso de conexión directa, la idea es reducir la congestión de conexiones,
dando al OBEP flexibilidad en cómo se conecta a los IBGWs. La capacidad de
especificar múltiples túneles también nos permite implementar multicast en el
OBEP (entregando el mensaje a todos los túneles especificados).

Una alternativa a la parte de delegación de esta propuesta sería enviar a
través de un hash de LeaseSet, similar a la capacidad existente de especificar
un hash de
[RouterIdentity](/docs/specs/common-structures/#common-structure-specification). Esto resultaría en un mensaje más pequeño y un LeaseSet
potencialmente más reciente. Sin embargo:

1. Obligaría al OBEP a realizar una búsqueda.

2. El LeaseSet podría no estar publicado en un floodfill, por lo que la búsqueda fallaría.

3. El LeaseSet podría estar cifrado, por lo que el OBEP no podría obtener los leases.

4. Especificar un LeaseSet revelaría al OBEP el [Destination](/docs/specs/common-structures/#destination) del mensaje,
   que de otro modo solo podría descubrir escaneando todos los LeaseSets de la
   red y buscando una coincidencia de Lease.


## Diseño

El originador (OBGW) colocaría algunos (¿todos?) de los [Leases](/docs/specs/common-structures/#lease) objetivo en las
instrucciones de entrega [TUNNEL-DELIVERY](/docs/specs/i2np/#tunnel-message-delivery-instructions) en lugar de elegir solo uno.

El OBEP seleccionaría uno de ellos para entregar el mensaje. El OBEP elegiría,
si está disponible, uno al que ya esté conectado o del que ya tenga
conocimiento. Esto haría que la ruta OBEP-IBGW fuera más rápida y confiable, y
reduciría el número total de conexiones en la red.

Tenemos un tipo de entrega no utilizado (0x03) y dos bits restantes (0 y 1) en
los flags de TUNNEL-DELIVERY, que podemos aprovechar para implementar estas
características.


## Implicaciones de seguridad

Esta propuesta no cambia la cantidad de información filtrada sobre el
Destination objetivo del OBGW ni sobre su visión de la NetDB:

- Un adversario que controle el OBEP y esté escaneando LeaseSets desde la NetDB
  ya puede determinar si un mensaje está siendo enviado a un Destination
  particular, buscando el par TunnelId / RouterIdentity. En el peor de los
  casos, la presencia de múltiples Leases en el TMDI podría hacer más rápido
  encontrar una coincidencia en la base de datos del adversario.

- Un adversario que opere un Destination malicioso ya puede obtener información
  sobre la visión de la NetDB de una víctima conectada, publicando LeaseSets
  que contengan diferentes túneles entrantes en distintos floodfills y
  observando a través de qué túneles se conecta el OBGW. Desde su punto de
  vista, que el OBEP seleccione qué túnel usar es funcionalmente idéntico a que
  el OBGW haga la selección.

El flag de multicast revela al OBEP el hecho de que el OBGW está haciendo
multicast. Esto crea un compromiso entre rendimiento y privacidad que debe
considerarse al implementar protocolos de nivel superior. Al ser un flag
opcional, los usuarios pueden tomar la decisión adecuada para su aplicación.
Sin embargo, podría haber beneficios en que este sea el comportamiento por
defecto para aplicaciones compatibles, ya que su uso generalizado por diversas
aplicaciones reduciría la filtración de información sobre qué aplicación
específica envió un mensaje determinado.


## Especificación

Las instrucciones de entrega del primer fragmento se modificarían como sigue:

```
+----+----+----+----+----+----+----+----+
  |flag|  Tunnel ID (opt)  |              |
  +----+----+----+----+----+              +
  |                                       |
  +                                       +
  |         To Hash (optional)            |
  +                                       +
  |                                       |
  +                        +----+----+----+
  |                        |dly | Message
  +----+----+----+----+----+----+----+----+
   ID (opt) |extended opts (opt)|cnt | (o)
  +----+----+----+----+----+----+----+----+
   Tunnel ID N   |                        |
  +----+----+----+                        +
  |                                       |
  +                                       +
  |         To Hash N (optional)          |
  +                                       +
  |                                       |
  +              +----+----+----+----+----+
  |              | Tunnel ID N+1 (o) |    |
  +----+----+----+----+----+----+----+    +
  |                                       |
  +                                       +
  |         To Hash N+1 (optional)        |
  +                                       +
  |                                       |
  +                                  +----+
  |                                  | sz
  +----+----+----+----+----+----+----+----+
       |
  +----+

flag ::
       1 byte
       Orden de bits: 76543210
       bits 6-5: tipo de entrega
                 0x03 = TUNNELS
       bit 0: ¿multicast? Si es 0, entregar a uno de los túneles
                         Si es 1, entregar a todos los túneles
                         Establecer en 0 para compatibilidad con usos futuros si
                         el tipo de entrega no es TUNNELS

Count ::
       1 byte
       Opcional, presente si el tipo de entrega es TUNNELS
       2-255 - Número de pares id/hash que siguen

Tunnel ID :: TunnelId
To Hash ::
       36 bytes cada uno
       Opcional, presente si el tipo de entrega es TUNNELS
       pares id/hash

Longitud total: La longitud típica es:
       75 bytes para entrega TUNNELS con count 2 (mensaje de túnel sin fragmentar);
       79 bytes para entrega TUNNELS con count 2 (primer fragmento)

El resto de las instrucciones de entrega sin cambios
```


## Compatibilidad

Los únicos pares que necesitan entender la nueva especificación son los OBGWs
y los OBEPs. Por lo tanto, podemos hacer este cambio compatible con la red
existente haciendo que su uso dependa de la versión de I2P objetivo:

* Los OBGWs deben seleccionar OBEPs compatibles al construir túneles salientes,
  basándose en la versión de I2P anunciada en su [RouterInfo](/docs/specs/common-structures/#routerinfo).

* Los pares que anuncien la versión objetivo deben soportar el análisis de los
  nuevos flags y no deben rechazar las instrucciones como inválidas.


## Referencias

* [Destination](/docs/specs/common-structures/#destination)
* [Leases](/docs/specs/common-structures/#lease)
* [LeaseSet](/docs/specs/common-structures/#leaseset)
* [RouterIdentity](/docs/specs/common-structures/#routeridentity)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TUNNEL-DELIVERY](/docs/specs/common-structures/#tunnelmessagedeliveryinstructions)
* [TunnelId](/docs/specs/common-structures/#tunnelid)
* [VERSIONS](/docs/specs/i2np/#protocol-versions)
