---
title: "Bandera I2CP para Cambio de Túnel Saliente"
number: "171"
author: "onon, eyedeekay"
created: "2026-05-19"
lastupdated: "2026-05-23"
status: "Borrador"
toc: true
---

## Descripción general

Las conexiones del cliente de streaming pueden quedarse bloqueadas cuando los acuses de recibo de entrega se pierden silenciosamente. El emisor retransmite hasta que recibe un acuse de recibo o se desconecta la conexión, sin tener una forma confiable de confirmar que los acuses de recibo están llegando al otro extremo. Esta propuesta añade un nuevo bit de bandera al campo de banderas de [SendMessageExpiresMessage](/docs/specs/i2cp/) para que un cliente pueda indicarle al router que seleccione un túnel saliente diferente para los mensajes posteriores hacia el mismo destino. El protocolo de streaming utiliza este bit para iniciar un cambio de túnel al detectar una conexión bloqueada.

## Disparadores

Dos condiciones DEBERÍAN hacer que el cliente active la bandera en el próximo mensaje saliente. Estas condiciones se miden en la capa de transmisión continua (streaming).

**Lado del remitente**

No se ha recibido ninguna confirmación dentro del período actual de tiempo de espera de retransmisión del cliente.

**Lado del receptor**

El receptor ha observado que el extremo remoto está retransmitiendo los mismos datos más de una vez, lo que indica que sus acuses de recibo no están llegando al remoto. El receptor DEBERÍA activar esta bandera en su próximo mensaje saliente I2CP para que los acuses de recibo lleguen al remoto a través de una ruta diferente. El receptor DEBE esperar hasta que: (1) haya recibido un duplicado, (2) haya enviado al menos un acuse de recibo, y (3) el remoto haya retransmitido nuevamente antes de activar la bandera.

Para limitar los ataques de correlación temporal, un cliente NO DEBE establecer la bandera más de una vez por cada ventana de 10 segundos por conexión. El cliente TAMBIÉN DEBERÍA retrasar la activación de la bandera mediante un valor de jitter extraído uniformemente del intervalo `[0, min(T/4, 2000ms)]`, donde T es el tiempo de espera actual de retransmisión del cliente en milisegundos, tras detectar la condición de bloqueo, para reducir la precisión de la correlación temporal.

## Especificación

El campo de flags (banderas) de [SendMessageExpiresMessage](/docs/specs/i2cp/) ocupa los 2 bytes superiores tras el campo Date (redefinido a partir de la versión 0.8.4) y se transmite en orden big-endian. El bit 15 actualmente no se utiliza; esta propuesta lo define.

Orden de bits: 15...0

| Bit | Nombre | Descripción |
|-----|--------|-------------|
| 15 | SWITCH_OUTBOUND_TUNNEL | Si es 1, el router DEBERÍA seleccionar un túnel saliente diferente de su grupo para mensajes posteriores a este destino. Si no hay disponible un túnel alternativo, esta bandera se ignora silenciosamente. El router NO DEBE cerrar ni retirar el túnel previamente utilizado únicamente porque esta bandera estuviera activa. |
Esta bandera tiene como valor predeterminado 0. Los routers que no la implementen DEBEN ignorarla sin generar errores.

## Notas de implementación

Cuando se establece `SWITCH_OUTBOUND_TUNNEL`, el router DEBERÍA seleccionar un túnel aleatoriamente y de forma uniforme del grupo de salida, excluyendo:

- el túnel que actualmente se está utilizando para esta sesión, y
- el único túnel más recientemente fallido en el grupo, si lo hubiera.

Ninguna otra métrica de salud del túnel, tiempos de creación ni historial de selección DEBE influir en la elección, ya que la selección ponderada podría favorecer a atacantes sybil. Si después de estas exclusiones el grupo no contiene ningún túnel elegible, la bandera se ignora silenciosamente.

Esta opción no genera mensajes adicionales en el túnel; cambiar de túnel puede modificar la latencia aparente. El límite de tasa de 10 segundos por conexión (ver Disparadores) evita cambios excesivos.

## Consideraciones sobre el anonimato

Las banderas en [SendMessageExpiresMessage](/docs/specs/i2cp/) se transmiten a través de I2CP, que es una interfaz local entre el cliente y su propio router. Estas no son visibles para los observadores de la red.

El riesgo para el anonimato se basa en los patrones de tráfico: un adversario con visibilidad en múltiples puntos finales de túneles puede observar *cuándo* cambia el uso del túnel.

Cambiar túneles salientes como respuesta directa a una interrupción del lado del cliente crea un patrón de comportamiento detectable. Existen dos vectores de observación concretos:

**Ataque Sybil en los primeros saltos de los túneles salientes**

El primer salto de cada túnel saliente ve todo el tráfico que entra en ese túnel desde el router del remitente. Un adversario que controle el primer salto de más de un túnel en el grupo del remitente observa cómo el tráfico se detiene en un primer salto y comienza en otro en un intervalo temporal cercano, vinculando ambos túneles al mismo remitente. Con un grupo de N túneles, un adversario que controle K primeros saltos tiene una probabilidad de K/N de observar cualquier evento de cambio dado.

**Temporización del intervalo de tráfico**

Durante la interrupción, el cliente no envía nuevos datos, por lo que el túnel saliente anterior queda inactivo. Cuando se produce el cambio, el tráfico se reanuda por una ruta diferente. Un adversario con una posición privilegiada en el router del remitente —como el proveedor de red del remitente o el propio nodo del primer salto— puede observar el patrón de silencio seguido de reanudación. La duración del intervalo además revela una aproximación del valor actual de tiempo de espera de retransmisión del cliente.

Los clientes DEBEN cumplir con los requisitos de limitación de velocidad y jitter en Triggers.

## Referencias

- [Especificación I2CP](/docs/specs/i2cp/)
