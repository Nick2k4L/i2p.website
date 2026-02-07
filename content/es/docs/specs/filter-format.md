---
title: "Formato de Filtro de Acceso"
description: "Sintaxis para archivos de filtro de control de acceso de tunnel"
slug: "filter-format"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
type: docs
---

## Descripción general

La definición de un filtro es una lista de cadenas de texto. Las líneas en blanco y las líneas que comienzan con `#` son ignoradas. Los cambios en la definición del filtro surten efecto al reiniciar el tunnel.

Cada línea puede representar uno de estos elementos:

- Definición de un umbral predeterminado para aplicar a cualquier destino remoto no listado en este archivo o en cualquiera de los archivos referenciados
- Definición de un umbral para aplicar a un destino remoto específico
- Definición de un umbral para aplicar a destinos remotos listados en un archivo
- Definición de un umbral que, si se supera, causará que el destino remoto infractor sea registrado en un archivo especificado

El orden de las definiciones importa. El primer umbral para un destino dado (ya sea explícito o listado en un archivo) anula cualquier umbral futuro para el mismo destino, ya sea explícito o listado en un archivo.

## Umbrales

Un umbral se define por el número de intentos de conexión que se permite realizar a un destino remoto durante un número específico de segundos antes de que ocurra una "violación". Por ejemplo, la siguiente definición de umbral `15/5` significa que al mismo destino remoto se le permite realizar 14 intentos de conexión durante un período de 5 segundos. Si realiza un intento más dentro del mismo período, se violará el umbral.

El formato de umbral puede ser uno de los siguientes:

- **Definición numérica** del número de conexiones sobre el número de segundos - `15/5`, `30/60`, y así sucesivamente. Nota que si el número de conexiones es 1 (como por ejemplo en `1/1`) el primer intento de conexión resultará en una violación.
- La palabra **`allow`**. Este umbral nunca se viola, es decir, se permite un número infinito de intentos de conexión.
- La palabra **`deny`**. Este umbral siempre se viola, es decir, no se permitirán intentos de conexión.

### Umbral Predeterminado

El umbral predeterminado se aplica a cualquier destino remoto que no esté listado explícitamente en la definición o en cualquiera de los archivos referenciados. Para establecer un umbral predeterminado usa la palabra clave `default`. Los siguientes son ejemplos de umbrales predeterminados:

```text
15/5 default
allow default
deny default
```
Solo puede haber una definición de umbral predeterminado por filtro. Si se omite, el filtro permitirá conexiones desconocidas por defecto.

### Umbrales Explícitos

Se aplican umbrales explícitos a un destino remoto listado en la propia definición. Ejemplos:

```text
15/5 explicit asdfasdfasdf.b32.i2p
allow explicit fdsafdsafdsa.b32.i2p
deny explicit qwerqwerqwer.b32.i2p
```
### Umbrales de Volumen

Por conveniencia es posible mantener una lista de destinos en un archivo y definir un umbral para todos ellos de forma masiva. Ejemplos:

```text
15/5 file /path/throttled_destinations.txt
deny file /path/forbidden_destinations.txt
allow file /path/unlimited_destinations.txt
```
Estos archivos pueden editarse manualmente mientras el tunnel está funcionando. Los cambios en estos archivos pueden tardar hasta 10 segundos en surtir efecto.

## Grabadoras

Los recorders llevan un registro de los intentos de conexión realizados por un destino remoto, y si esto supera un cierto umbral, ese destino se registra en un archivo determinado. Ejemplos:

```text
30/5 record /path/aggressive.txt
60/5 record /path/very_aggressive.txt
```
Es posible usar un grabador para registrar destinos agresivos en un archivo determinado, y luego usar ese mismo archivo para limitarlos. Por ejemplo, el siguiente fragmento definirá un filtro que inicialmente permite todos los intentos de conexión, pero si cualquier destino individual excede 30 intentos por 5 segundos, se limita a 15 intentos por 5 segundos:

```text
# by default there are no limits
allow default
# but record overly aggressive destinations
30/5 record /path/throttled.txt
# and any that end up in that file will get throttled in the future
15/5 file /path/throttled.txt
```
Es posible usar un grabador en un tunnel que escriba a un archivo que limite la velocidad de otro tunnel. Es posible reutilizar el mismo archivo con destinos en múltiples tunnels. Y por supuesto, es posible editar estos archivos a mano.

Aquí tienes un ejemplo de definición de filtro que aplica cierta limitación por defecto, sin limitación para destinos en el archivo `friends.txt`, prohíbe cualquier conexión de destinos en el archivo `enemies.txt` y registra cualquier comportamiento agresivo en un archivo llamado `suspicious.txt`:

```text
15/5 default
allow file /path/friends.txt
deny file /path/enemies.txt
60/5 record /path/suspicious.txt
```