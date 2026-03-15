---
title: "Mejoras en el Transporte IPv6"
aliases:
  - "/es/spec/proposals/158"
  - "/es/spec/proposals/158/"
number: "158"
author: "zzz, orignal"
created: "2021-03-19"
lastupdated: "2021-04-26"
status: "Closed"
thread: "http://zzz.i2p/topics/3060"
target: "0.9.50"
toc: true
---
## Nota
Despliegue y pruebas en la red en curso.
Sujeto a revisiones menores.


## Visión general

Esta propuesta tiene como objetivo implementar mejoras en los transportes SSU y NTCP2 para IPv6.


## Motivación

A medida que IPv6 crece en todo el mundo y las configuraciones exclusivas de IPv6 (especialmente en dispositivos móviles) se vuelven más comunes,
necesitamos mejorar nuestro soporte para IPv6 y eliminar el supuesto de que
todos los routers son compatibles con IPv4.



### Comprobación de conectividad

Al seleccionar pares para túneles, o al elegir rutas OBEP/IBGW para enrutar mensajes,
es útil calcular si el router A puede conectarse al router B.
En general, esto significa determinar si A tiene capacidad de salida para un transporte y tipo de dirección (IPv4/v6)
que coincida con una de las direcciones entrantes anunciadas por B.

Sin embargo, en muchos casos no conocemos las capacidades de A y debemos hacer suposiciones.
Si A está oculto o detrás de un cortafuegos, las direcciones no se publican y no tenemos conocimiento directo,
por lo que asumimos que es compatible con IPv4, pero no con IPv6.
La solución consiste en agregar dos nuevas "caps" o capacidades al Router Info para indicar la capacidad de salida para IPv4 y IPv6.


### Introducidos IPv6

Nuestras especificaciones para SSU contienen errores e inconsistencias sobre si
se admiten introducidos IPv6 para introducciones IPv4.
En cualquier caso, esto nunca se ha implementado ni en Java I2P ni en i2pd.
Esto debe corregirse.


### Introducciones IPv6

Nuestras especificaciones para SSU indican claramente que
las introducciones IPv6 no están soportadas.
Esto se basaba en la suposición de que IPv6 nunca está detrás de un cortafuegos.
Esto claramente no es cierto, y necesitamos mejorar el soporte para routers IPv6 detrás de cortafuegos.


### Diagramas de introducción

Leyenda: ----- es IPv4, ====== es IPv6

**Actual, solo IPv4:**

```
        Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**Introducción IPv4, introducido IPv6:**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ----------->
         <-------------------------------------------- HolePunch
    SessionRequest -------------------------------------------->
         <-------------------------------------------- SessionCreated
    SessionConfirmed ------------------------------------------>
    Data <--------------------------------------------------> Data
```

**Introducción IPv6, introducido IPv6:**

```
Alice                         Bob                  Charlie
    RelayRequest ======================>
         <============== RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```

**Introducción IPv6, introducido IPv4:**

```
Alice                         Bob                  Charlie
    RelayRequest ---------------------->
         <-------------- RelayResponse    RelayIntro ===========>
         <============================================ HolePunch
    SessionRequest ============================================>
         <============================================ SessionCreated
    SessionConfirmed ==========================================>
    Data <==================================================> Data
```

## Diseño

Se deben implementar tres cambios:

- Agregar capacidades "4" y "6" a las capacidades de dirección del router para indicar soporte de salida IPv4 e IPv6
- Agregar soporte para introducciones IPv4 a través de introducidos IPv6
- Agregar soporte para introducciones IPv6 a través de introducidos IPv4 e IPv6


## Especificación

### Caps 4/6

Esto se implementó originalmente sin una propuesta formal, pero es necesario para
las introducciones IPv6, por lo que lo incluimos aquí.

Se definen dos nuevas capacidades "4" y "6".
Estas nuevas capacidades se agregarán a la propiedad "caps" en la dirección del router, no en las caps del Router Info.
Actualmente no tenemos una propiedad "caps" definida para NTCP2.
Una dirección SSU con introducidos es, por definición, ipv4 en este momento. No soportamos introducción ipv6 en absoluto.
Sin embargo, esta propuesta es compatible con introducciones IPv6. Véase más abajo.

Además, un router puede admitir conectividad a través de una red superpuesta como I2P-over-Yggdrasil,
pero no desea publicar una dirección, o esa dirección no tiene un formato estándar IPv4 o IPv6.
Este nuevo sistema de capacidades debería ser lo suficientemente flexible como para admitir también estas redes.

Definimos los siguientes cambios:

NTCP2: Agregar propiedad "caps"

SSU: Agregar soporte para una dirección de router sin host ni introducidos, para indicar soporte de salida
para IPv4, IPv6, o ambos.

Ambos transportes: Definir los siguientes valores de caps:

- "4": Soporte IPv4
- "6": Soporte IPv6

Pueden admitirse múltiples valores en una sola dirección. Véase más abajo.
Al menos una de estas caps es obligatoria si no se incluye un valor "host" en la dirección del router.
Como máximo, una de estas caps es opcional si se incluye un valor "host" en la dirección del router.
En el futuro podrían definirse caps adicionales del transporte para indicar soporte para redes superpuestas u otra conectividad.


#### Casos de uso y ejemplos

SSU:

SSU con host: 4/6 opcional, nunca más de uno.
Ejemplo: SSU caps="4" host="1.2.3.4" key=... port="1234"

SSU solo salida para uno, el otro publicado: Solo caps, 4/6.
Ejemplo: SSU caps="6"

SSU con introducidos: nunca combinado. Se requiere 4 o 6.
Ejemplo: SSU caps="4" iexp0=... ihost0=... iport0=... itag0=... key=...

SSU oculto: Solo caps, 4, 6, o 46. Se permite múltiple.
No es necesario tener dos direcciones, una con 4 y otra con 6.
Ejemplo: SSU caps="46"

NTCP2:

NTCP2 con host: 4/6 opcional, nunca más de uno.
Ejemplo: NTCP2 caps="4" host="1.2.3.4" i=... port="1234" s=... v="2"

NTCP2 solo salida para uno, el otro publicado: Caps, s, v solo, 4/6/y, se permite múltiple.
Ejemplo: NTCP2 caps="6" i=... s=... v="2"

NTCP2 oculto: Caps, s, v solo 4/6, se permite múltiple. No es necesario tener dos direcciones, una con 4 y otra con 6.
Ejemplo: NTCP2 caps="46" i=... s=... v="2"



### Introducidos IPv6 para IPv4

Los siguientes cambios son necesarios para corregir errores e inconsistencias en las especificaciones.
También hemos descrito esto como "parte 1" de la propuesta.

#### Cambios en la especificación

La especificación SSU actual dice (notas IPv6):

IPv6 es compatible desde la versión 0.9.8. Las direcciones de retransmisión publicadas pueden ser IPv4 o IPv6, y la comunicación entre Alice y Bob puede ser mediante IPv4 o IPv6.

Agregar lo siguiente:

Aunque la especificación cambió a partir de la versión 0.9.8, la comunicación entre Alice y Bob mediante IPv6 no fue realmente compatible hasta la versión 0.9.50.
Versiones anteriores de routers Java publicaron erróneamente la capacidad 'C' para direcciones IPv6,
aunque en realidad no actuaban como introducidos mediante IPv6.
Por lo tanto, los routers deben confiar en la capacidad 'C' en una dirección IPv6 solo si la versión del router es 0.9.50 o superior.



La especificación SSU actual dice (Solicitud de retransmisión):

La dirección IP solo se incluye si es diferente a la dirección de origen y puerto del paquete.
En la implementación actual, la longitud de IP siempre es 0 y el puerto siempre es 0,
y el receptor debe usar la dirección de origen y puerto del paquete.
Este mensaje puede enviarse mediante IPv4 o IPv6. Si es IPv6, Alice debe incluir su dirección y puerto IPv4.

Agregar lo siguiente:

La IP y el puerto deben incluirse para introducir una dirección IPv4 al enviar este mensaje mediante IPv6.
Esto es compatible desde la versión 0.9.50.



### Introducciones IPv6

Los tres mensajes de retransmisión SSU (RelayRequest, RelayResponse y RelayIntro) contienen campos de longitud IP
para indicar la longitud de la dirección IP (de Alice, Bob o Charlie) que sigue.

Por lo tanto, no se requiere ningún cambio en el formato de los mensajes.
Solo se necesitan cambios textuales en las especificaciones, indicando que se permiten direcciones IP de 16 bytes.

Los siguientes cambios son necesarios en las especificaciones.
También hemos descrito esto como "parte 2" de la propuesta.


#### Cambios en la especificación

La especificación SSU actual dice (notas IPv6):

La comunicación Bob-Charlie y Alice-Charlie es solo mediante IPv4.

La especificación SSU actual dice (Solicitud de retransmisión):

No hay planes de implementar retransmisión para IPv6.

Cambiar a:

La retransmisión para IPv6 es compatible desde la versión 0.9.xx

La especificación SSU actual dice (Respuesta de retransmisión):

La dirección IP de Charlie debe ser IPv4, ya que es la dirección a la que Alice enviará el SessionRequest tras el Hole Punch.
No hay planes de implementar retransmisión para IPv6.

Cambiar a:

La dirección IP de Charlie puede ser IPv4 o, desde la versión 0.9.xx, IPv6.
Esa es la dirección a la que Alice enviará el SessionRequest tras el Hole Punch.
La retransmisión para IPv6 es compatible desde la versión 0.9.xx

La especificación SSU actual dice (Introducción de retransmisión):

La dirección IP de Alice siempre tiene 4 bytes en la implementación actual, porque Alice intenta conectarse a Charlie mediante IPv4.
Este mensaje debe enviarse mediante una conexión IPv4 establecida,
ya que es la única forma en que Bob conoce la dirección IPv4 de Charlie para devolvérsela a Alice en el RelayResponse.

Cambiar a:

Para IPv4, la dirección IP de Alice siempre tiene 4 bytes, porque Alice intenta conectarse a Charlie mediante IPv4.
Desde la versión 0.9.xx, se admite IPv6, y la dirección IP de Alice puede tener 16 bytes.

Para IPv4, este mensaje debe enviarse mediante una conexión IPv4 establecida,
ya que es la única forma en que Bob conoce la dirección IPv4 de Charlie para devolvérsela a Alice en el RelayResponse.
Desde la versión 0.9.xx, se admite IPv6, y este mensaje puede enviarse mediante una conexión IPv6 establecida.

Además, agregar:

Desde la versión 0.9.xx, cualquier dirección SSU publicada con introducidos debe contener "4" o "6" en la opción "caps".


## Migración

Todos los routers antiguos deberían ignorar la propiedad caps en NTCP2, y caracteres de capacidad desconocidos en la propiedad caps de SSU.

Cualquier dirección SSU con introducidos que no contenga una cap "4" o "6" se asume que es para introducción IPv4.


## Referencias

* [CAPS](http://zzz.i2p/topics/3050)
* [NTCP2](/docs/specs/ntcp2/)
* [SSU](/docs/specs/ssu2/)
* [SSU-SPEC](/docs/legacy/ssu/)
