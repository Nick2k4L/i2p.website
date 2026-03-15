---
title: "El Proceso de Propuestas de I2P"
number: "001"
author: "str4d"
created: "2016-04-10"
lastupdated: "2017-04-07"
status: "Meta"
thread: "http://zzz.i2p/topics/1980"
toc: true
---
## Resumen

Este documento describe cómo cambiar las especificaciones de I2P, cómo funcionan las propuestas de I2P y la relación entre las propuestas de I2P y las especificaciones.

Este documento se adapta del proceso de propuestas de Tor, y gran parte del contenido a continuación fue originalmente escrito por Nick Mathewson.

Este es un documento informativo.

## Motivación

Anteriormente, nuestro proceso para actualizar las especificaciones de I2P era relativamente informal: hacíamos una propuesta en el foro de desarrollo y discutíamos los cambios, luego llegábamos a un consenso y parcheábamos la especificación con cambios de borrador (no necesariamente en ese orden), y finalmente implementábamos los cambios.

Esto tenía algunos problemas.

Primero, incluso en su momento más eficiente, el antiguo proceso a menudo tenía la especificación fuera de sincronización con el código. Los peores casos eran aquellos en los que se posponía la implementación: la especificación y el código podían permanecer fuera de sincronización durante versiones.

Segundo, era difícil participar en la discusión, ya que no siempre era claro qué partes de la discusión eran parte de la propuesta, o qué cambios a la especificación se habían implementado. Los foros de desarrollo solo son accesibles dentro de I2P, lo que significa que las propuestas solo podían ser vistas por personas que usan I2P.

Tercero, era muy fácil olvidar algunas propuestas porque se enterraban varias páginas atrás en la lista de threads del foro.

## Cómo cambiar las especificaciones ahora

Primero, alguien escribe un documento de propuesta. Debe describir el cambio que debe hacerse en detalle y dar una idea de cómo implementarlo. Una vez que esté lo suficientemente desarrollado, se convierte en una propuesta.

Al igual que un RFC, cada propuesta obtiene un número. A diferencia de los RFC, las propuestas pueden cambiar con el tiempo y mantener el mismo número, hasta que sean finalmente aceptadas o rechazadas. La historia de cada propuesta se almacenará en el repositorio del sitio web de I2P.

Una vez que una propuesta esté en el repositorio, debemos discutirla en el thread correspondiente y mejorarla hasta que hayamos alcanzado un consenso de que es una buena idea, y que es lo suficientemente detallada como para implementarla. Cuando esto sucede, implementamos la propuesta e incorporamos la especificación. Así, las especificaciones siguen siendo la documentación canónica para el protocolo I2P: ninguna propuesta es nunca la documentación canónica para una característica implementada.

(Este proceso es bastante similar al Proceso de Mejora de Python, con la excepción principal de que las propuestas de I2P se reintegran en las especificaciones después de la implementación, mientras que los PEP se convierten en la nueva especificación.)

### Cambios pequeños

Todavía está bien hacer cambios pequeños directamente a la especificación si el código se puede escribir más o menos inmediatamente, o cambios cosméticos si no se requiere ningún cambio de código. Este documento refleja la intención actual de los desarrolladores, no una promesa permanente de siempre usar este proceso en el futuro: nos reservamos el derecho de entusiasmarnos y correr a implementar algo en una sesión de hacking de toda la noche impulsada por cafeína o M&M.

## Cómo se agregan nuevas propuestas

Para presentar una propuesta, publique en el foro de desarrollo o ingrese un ticket con la propuesta adjunta.

Una vez que se ha propuesto una idea, existe un borrador debidamente formateado (ver a continuación) y existe un consenso aproximado dentro de la comunidad de desarrollo activa de que esta idea merece consideración, los editores de propuestas agregarán oficialmente la propuesta.

Los actuales editores de propuestas son zzz y str4d.

## Qué debe ir en una propuesta

Cada propuesta debe tener un encabezado que contenga los siguientes campos:

```
:author:
:created:
:thread:
:lastupdated:
:status:
```

- El campo `author` debe contener los nombres de los autores de esta propuesta.
- El campo `thread` debe ser un enlace al thread del foro de desarrollo donde se publicó originalmente esta propuesta, o a un nuevo thread creado para discutir esta propuesta.
- El campo `lastupdated` debe ser inicialmente igual al campo `created` y debe actualizarse cada vez que se cambie la propuesta.

Estos campos deben establecerse cuando sea necesario:

```
:supercedes:
:supercededby:
:editor:
```

- El campo `supercedes` es una lista separada por comas de todas las propuestas que esta propuesta reemplaza. Esas propuestas deben ser rechazadas y deben tener su campo `supercededby` establecido en el número de esta propuesta.
- El campo `editor` debe establecerse si se realizan cambios significativos en esta propuesta que no alteren sustancialmente su contenido. Si el contenido se está alterando sustancialmente, debe agregarse un autor adicional o crearse una nueva propuesta que reemplace esta.

Estos campos son opcionales pero recomendados:

```
:target:
:implementedin:
```

- El campo `target` debe describir qué versión se espera implementar la propuesta (si está Abierta o Aceptada).
- El campo `implementedin` debe describir qué versión se implementó la propuesta (si está Terminada o Cerrada).

El cuerpo de la propuesta debe comenzar con una sección de Resumen que explique de qué se trata la propuesta, qué hace y en qué estado se encuentra.

Después del Resumen, la propuesta se vuelve más libre. Dependiendo de su longitud y complejidad, la propuesta puede dividirse en secciones según sea apropiado, o seguir un formato discursivo breve. Cada propuesta debe contener al menos la siguiente información antes de ser Aceptada, aunque la información no necesita estar en secciones con estos nombres.

**Motivación**
: ¿Qué problema intenta resolver la propuesta? ¿Por qué importa este problema? Si son posibles varios enfoques, ¿por qué se toma este?

**Diseño**
: Una visión de alto nivel de qué características nuevas o modificadas son, cómo funcionan las características nuevas o modificadas, cómo interactúan entre sí y cómo interactúan con el resto de I2P. Este es el cuerpo principal de la propuesta. Algunas propuestas comenzarán con solo una Motivación y un Diseño, y esperarán a una especificación hasta que el Diseño parezca aproximadamente correcto.

**Implicaciones de seguridad**
: Qué efectos pueden tener los cambios propuestos en la anonimidad, cuán bien entendidos están estos efectos y así sucesivamente.

**Especificación**
: Una descripción detallada de qué necesita agregarse a las especificaciones de I2P para implementar la propuesta. Debe estar en aproximadamente tanto detalle como las especificaciones contendrán eventualmente: debe ser posible para programadores independientes escribir implementaciones mutuamente compatibles de la propuesta basadas en sus especificaciones.

**Compatibilidad**
: ¿Serán compatibles las versiones de I2P que siguen la propuesta con las versiones que no lo hacen? Si es así, ¿cómo se logrará la compatibilidad? Generalmente, tratamos de no perder la compatibilidad si es posible; no hemos hecho un cambio de "día de la bandera" desde marzo de 2008, y no queremos hacer otro.

**Implementación**
: Si la propuesta será difícil de implementar en la arquitectura actual de I2P, el documento puede contener alguna discusión sobre cómo hacer que funcione. Los parches reales deben ir en ramas públicas de monotone, o subirse a Trac.

**Notas de rendimiento y escalabilidad**
: Si la característica tendrá un efecto en el rendimiento (en RAM, CPU, ancho de banda) o la escalabilidad, debe haber algún análisis sobre cuán significativo será este efecto, para que podamos evitar regresiones de rendimiento realmente costosas, y para que podamos evitar perder el tiempo en ganancias insignificantes.

**Referencias**
: Si la propuesta se refiere a documentos externos, estos deben enumerarse.

## Estado de la propuesta

**Abierta**
: Una propuesta bajo discusión.

**Aceptada**
: La propuesta es completa, y pretendemos implementarla. Después de este punto, los cambios sustantivos a la propuesta deben evitarse y considerarse como un signo de que el proceso ha fallado en algún lugar.

**Terminada**
: La propuesta ha sido aceptada e implementada. Después de este punto, la propuesta no debe cambiarse.

**Cerrada**
: La propuesta ha sido aceptada, implementada y fusionada con los documentos de especificación principales. La propuesta no debe cambiarse después de este punto.

**Rechazada**
: No implementaremos la característica como se describe aquí, aunque podríamos hacer alguna otra versión. Ver comentarios en el documento para detalles. La propuesta no debe cambiarse después de este punto; para presentar alguna otra versión de la idea, escriba una nueva propuesta.

**Borrador**
: Esta no es una propuesta completa todavía; hay piezas definitivamente faltantes. Por favor, no agregue nuevas propuestas con este estado; colóquelas en el subdirectorio "ideas" en su lugar.

**Necesita revisión**
: La idea para la propuesta es buena, pero la propuesta tal como está tiene problemas graves que la impiden ser aceptada. Ver comentarios en el documento para detalles.

**Muerta**
: La propuesta no ha sido tocada durante mucho tiempo, y no parece que alguien la complete pronto. Puede volver a estar "Abierta" si obtiene un nuevo proponente.

**Necesita investigación**
: Hay problemas de investigación que deben resolverse antes de que esté claro si la propuesta es una buena idea.

**Meta**
: Esto no es una propuesta, sino un documento sobre propuestas.

**Reserva**
: Esta propuesta no es algo que estemos planeando implementar actualmente, pero podríamos querer resucitarla algún día si decidimos hacer algo similar a lo que propone.

**Informativa**
: Esta propuesta es la última palabra sobre lo que está haciendo. No se convertirá en una especificación a menos que alguien copie y pegue en una nueva especificación para un nuevo subsistema.

Los editores mantienen el estado correcto de las propuestas, basado en un consenso aproximado y su propia discreción.

## Numeración de propuestas

Los números 000-099 están reservados para propuestas especiales y meta-propuestas. 100 y superior se utilizan para propuestas reales. Los números no se reciclan.

## Referencias

* [DEV-FORUM-PROPOSAL](http://zzz.i2p/topics/new?forum_id=7-big-topics-ideas-proposals-and-discussion)
* [TORSPEC-PROCESS](https://gitweb.torproject.org/torspec.git/tree/proposals/001-process.txt)
* [TRAC-PROPOSAL](http://trac.i2p2.i2p/newticket?summary=New%20proposal:%20&type=enhancement&milestone=n/a&component=www/i2p&keywords=review-needed)
