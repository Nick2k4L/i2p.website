---
title: "Vencimiento del Presentador"
number: "133"
author: "zzz"
created: "2017-02-05"
lastupdated: "2017-08-09"
status: "Cerrado"
thread: "http://zzz.i2p/topics/2230"
target: "0.9.30"
implementedin: "0.9.30"
toc: true
---
## Descripción general

Esta propuesta trata sobre mejorar la tasa de éxito para las presentaciones.


## Motivación

Las presentadoras expiran después de un cierto tiempo, pero esa información no se publica en la información del enrutador (Router Info). Actualmente, los enrutadores deben usar heurísticas para estimar cuándo una presentadora ya no es válida.


## Diseño

En una dirección de enrutador SSU que contenga presentadoras, el editor puede incluir opcionalmente tiempos de expiración para cada presentadora.


## Especificación

```
iexp{X}={nnnnnnnnnn}

X :: El número de presentadora (0-2)

nnnnnnnnnn :: El tiempo en segundos (no milisegundos) desde la época.
```

### Notas

* Cada expiración debe ser mayor que la fecha de publicación de la información del enrutador (Router Info),
  y menor que 6 horas después de dicha fecha de publicación.

* Los enrutadores que publican y las presentadoras deberían intentar mantener la presentadora válida
  hasta su expiración, sin embargo no existe forma de garantizarlo.

* Los enrutadores no deberían usar una presentadora publicada después de su expiración.

* Las expiraciones de presentadoras están en el mapeo de Dirección del Enrutador.
  No son el campo de expiración de 8 bytes (actualmente no usado) en la Dirección del Enrutador.

**Ejemplo:** `iexp0=1486309470`


## Migración

No hay problemas. La implementación es opcional.
La compatibilidad hacia atrás está asegurada, ya que los enrutadores antiguos ignorarán los parámetros desconocidos.


## Referencias

* [RouterAddress](/docs/specs/common-structures/#routeraddress)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TRAC-TICKET](http://trac.i2p2.i2p/ticket/1352)
