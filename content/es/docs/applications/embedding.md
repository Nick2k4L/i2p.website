---
title: "Integrando I2P en tu Aplicación"
description: "Directrices para incluir un router I2P con tu aplicación"
slug: "embedding"
lastUpdated: "2023-01"
accurateFor: "2.1.0"
---

## Descripción general

Esta página trata sobre incluir el binario completo del router I2P con tu aplicación. No se trata de escribir una aplicación para trabajar con I2P (ya sea incluido o externo). Sin embargo, muchas de las pautas pueden ser útiles incluso si no se incluye un router.

Muchos proyectos están integrando, o hablando de integrar, I2P. Eso es genial si se hace correctamente. Si se hace mal, podría causar daño real a nuestra red. El router I2P es complejo, y puede ser un desafío ocultar toda la complejidad a tus usuarios. Esta página discute algunas pautas generales.

La mayoría de estas pautas se aplican igualmente a Java I2P o i2pd. Sin embargo, algunas pautas son específicas para Java I2P y se indican a continuación.

### Habla con nosotros

Inicia un diálogo. Estamos aquí para ayudar. Las aplicaciones que integran I2P son las oportunidades más prometedoras - y emocionantes - para hacer crecer la red y mejorar el anonimato para todos.

### Elige tu router sabiamente

Si tu aplicación está en Java o Scala, es una elección fácil: usa el router de Java. Si está en C/C++, recomendamos i2pd. El desarrollo de i2pcpp se ha detenido. Para aplicaciones en otros lenguajes, es mejor usar SAM o BOB o SOCKS y agrupar el router de Java como un proceso separado. Algunas de las siguientes indicaciones solo se aplican al router de Java.

### Licencias

Asegúrate de cumplir con los requisitos de licencia del software que estás empaquetando.

---

## Configuración

### Verificar la configuración predeterminada

Una configuración predeterminada correcta es crucial. La mayoría de los usuarios no cambiarán los valores predeterminados. Los valores predeterminados para tu aplicación pueden necesitar ser diferentes a los predeterminados del router que estás incluyendo. Anula los valores predeterminados del router si es necesario.

Algunos valores predeterminados importantes a revisar: Ancho de banda máximo, cantidad y longitud de tunnel, máximo de tunnels participantes. Mucho de esto depende del ancho de banda esperado y los patrones de uso de tu aplicación.

Configura suficiente ancho de banda y túneles para permitir que tus usuarios contribuyan a la red. Considera deshabilitar I2CP externo, ya que probablemente no lo necesites y entraría en conflicto con cualquier otra instancia de I2P en ejecución. También revisa las configuraciones para deshabilitar la terminación de la JVM al salir, por ejemplo.

### Consideraciones del Tráfico Participante

Puede ser tentador deshabilitar el tráfico de participación. Hay varias formas de hacer esto (modo oculto, configurar tunnels máximos en 0, configurar el ancho de banda compartido por debajo de 12 KBytes/sec). Sin tráfico de participación, no tienes que preocuparte por el cierre elegante, tus usuarios no ven uso de ancho de banda que no fue generado por ellos, etc. Sin embargo, hay muchas razones por las que deberías permitir tunnels de participación.

En primer lugar, el router no funciona tan bien si no tiene la oportunidad de "integrarse" con la red, lo cual se ve enormemente facilitado cuando otros construyen túneles a través de ti.

En segundo lugar, más del 90% de los routers en la red actual permiten el tráfico de participación. Es la configuración predeterminada en el router Java. Si tu aplicación no enruta para otros y se vuelve realmente popular, entonces es una sanguijuela en la red, y altera el equilibrio que tenemos ahora. Si se vuelve realmente grande, entonces nos convertimos en Tor, y pasamos nuestro tiempo rogando a la gente que habilite el relaying (retransmisión).

En tercer lugar, el tráfico de participación es tráfico de cobertura que ayuda al anonimato de tus usuarios.

Desaconsejamos encarecidamente que desactives el tráfico participante por defecto. Si haces esto y tu aplicación se vuelve muy popular, podría romper la red.

### Persistencia

Debes guardar los datos del router (netDb, configuración, etc.) entre ejecuciones del router. I2P no funciona bien si debes resembrar en cada inicio, y eso supone una carga enorme en nuestros servidores de reseed, y tampoco es muy bueno para el anonimato. Incluso si incluyes router infos, I2P necesita datos de perfil guardados para un mejor rendimiento. Sin persistencia, tus usuarios tendrán una experiencia de inicio deficiente.

Hay dos posibilidades si no puedes proporcionar persistencia. Cualquiera de estas elimina la carga de tu proyecto en nuestros servidores reseed y mejorará significativamente el tiempo de inicio.

1) Configura tu(s) propio(s) servidor(es) de reseed del proyecto que sirvan mucho más que el número habitual de router infos en el reseed, digamos, varios cientos. Configura el router para usar solo tus servidores.

2) Incluye de mil a dos mil router infos en tu instalador.

Además, retrasa o escalona el inicio de tus túneles, para darle al router la oportunidad de integrarse antes de construir muchos túneles.

### Configurabilidad

Proporciona a tus usuarios una forma de cambiar la configuración de los ajustes importantes. Entendemos que probablemente querrás ocultar la mayor parte de la complejidad de I2P, pero es importante mostrar algunos ajustes básicos. Además de los valores predeterminados mencionados anteriormente, algunas configuraciones de red como UPnP, IP/puerto pueden ser útiles.

### Consideraciones sobre Floodfill

Por encima de cierta configuración de ancho de banda, y cumpliendo otros criterios de salud, tu router se convertirá en floodfill, lo que puede causar un gran aumento en las conexiones y el uso de memoria (al menos con el router Java). Piensa si eso está bien. Puedes deshabilitar floodfill, pero entonces tus usuarios más rápidos no estarán contribuyendo lo que podrían. También depende del tiempo de actividad típico de tu aplicación.

### Reseeding

Decide si vas a incluir router infos o usar nuestros hosts de reseed. La lista de hosts de reseed de Java está en el código fuente, así que si mantienes tu código fuente actualizado, la lista de hosts también lo estará. Ten en cuenta el posible bloqueo por parte de gobiernos hostiles.

### Usar Clientes Compartidos

Java I2P i2ptunnel admite clientes compartidos, donde los clientes pueden configurarse para usar un solo pool. Si necesitas múltiples clientes, y si es consistente con tus objetivos de seguridad, configura los clientes para que sean compartidos.

### Limitar Cantidad de Túneles

Especifica la cantidad de túneles explícitamente con las opciones `inbound.quantity` y `outbound.quantity`. El valor por defecto en Java I2P es 2; el valor por defecto en i2pd es mayor. Especifícalo en la línea SESSION CREATE usando SAM para obtener configuraciones consistentes con ambos routers. Dos de cada uno (entrada/salida) es suficiente para la mayoría de aplicaciones de ancho de banda bajo a medio y distribución baja a media. Los servidores y aplicaciones P2P de alta distribución pueden necesitar más. Consulta [esta publicación del foro](http://zzz.i2p/topics/1584) para obtener orientación sobre cómo calcular los requisitos para servidores y aplicaciones de alto tráfico.

### Especificar SAM SIGNATURE_TYPE

SAM por defecto usa DSA_SHA1 para los destinos, lo cual no es lo que quieres. Ed25519 (tipo 7) es la selección correcta. Añade SIGNATURE_TYPE=7 al comando DEST GENERATE, o al comando SESSION CREATE para DESTINATION=TRANSIENT.

### Limitar sesiones SAM

La mayoría de aplicaciones solo necesitarán una sesión SAM. SAM proporciona la capacidad de sobrecargar rápidamente el router local, o incluso la red más amplia, si se crea un gran número de sesiones. Si múltiples sub-servicios pueden usar una sola sesión, configúrelos con una sesión PRIMARY y SUBSESSIONS (actualmente no compatible con i2pd). Un límite razonable para las sesiones es de 3 o 4 en total, o tal vez hasta 10 para situaciones excepcionales. Si tienes múltiples sesiones, asegúrate de especificar una cantidad baja de tunnel para cada una, ver arriba.

En casi ninguna situación deberías requerir una sesión única por conexión. Sin un diseño cuidadoso, esto podría rápidamente hacer DDoS a la red. Considera cuidadosamente si tus objetivos de seguridad requieren sesiones únicas. Por favor consulta con los desarrolladores de Java I2P o i2pd antes de implementar sesiones por conexión.

### Reducir el Uso de Recursos de Red

Ten en cuenta que estas opciones no están actualmente soportadas en i2pd. Estas opciones están soportadas a través de I2CP y SAM (excepto delay-open, que es solo a través de i2ptunnel). Consulta la documentación de I2CP (y, para delay-open, la documentación de configuración de i2ptunnel) para más detalles.

Considera configurar tus túneles de aplicación como delay-open, reduce-on-idle y/o close-on-idle. Esto es sencillo si usas i2ptunnel, pero tendrás que implementar parte de esto por tu cuenta si usas I2CP directamente. Consulta i2psnark para ver código que reduce el número de túneles y luego cierra el túnel, incluso en presencia de alguna actividad DHT en segundo plano.

---

## Ciclo de Vida

### Capacidad de actualización

Tenga una función de actualización automática si es posible, o al menos notificación automática de una nueva versión. Nuestro mayor temor es una gran cantidad de routers que no puedan ser actualizados. Tenemos aproximadamente 6-8 lanzamientos al año del router Java, y es crítico para la salud de la red que los usuarios se mantengan actualizados. Usualmente tenemos más del 80% de la red en la última versión dentro de las 6 semanas posteriores al lanzamiento, y nos gustaría mantenerlo así. No necesita preocuparse por desactivar la función de actualización automática integrada del router, ya que ese código está en la consola del router, la cual presumiblemente no está incluyendo.

### Implementación

Ten un plan de implementación gradual. No satures la red de una vez. Actualmente tenemos aproximadamente 25K usuarios únicos por día y 40K únicos por mes. Probablemente podamos manejar un crecimiento de 2-3X por año sin demasiados problemas. Si anticipas un crecimiento más rápido que eso, O la distribución de ancho de banda (o distribución de tiempo de actividad, o cualquier otra característica significativa) de tu base de usuarios es significativamente diferente de nuestra base de usuarios actual, realmente necesitamos tener una discusión. Cuanto más grandes sean tus planes de crecimiento, más importante es todo lo demás en esta lista de verificación.

### Diseño para y Fomento de Tiempos de Actividad Prolongados

Informa a tus usuarios que I2P funciona mejor si se mantiene en ejecución. Pueden pasar varios minutos después del inicio antes de que funcione bien, e incluso más después de la primera instalación. Si tu tiempo de actividad promedio es menor a una hora, I2P probablemente no sea la solución adecuada.

---

## Interfaz de Usuario

### Mostrar Estado

Proporciona alguna indicación al usuario de que los túneles de la aplicación están listos. Fomenta la paciencia.

### Apagado Elegante

Si es posible, retrasa el apagado hasta que expiren tus tunnels participantes. No permitas que tus usuarios rompan los tunnels fácilmente, o al menos pídeles que confirmen.

### Educación y Donación

Sería bueno que les proporciones a tus usuarios enlaces para aprender más sobre I2P y para hacer donaciones.

### Opción de Router Externo

Dependiendo de tu base de usuarios y aplicación, puede ser útil proporcionar una opción o un paquete separado para usar un router externo.

---

## Otros Temas

### Uso de otros Servicios Comunes

Si planeas usar o enlazar a otros servicios comunes de I2P (fuentes de noticias, suscripciones a hosts.txt, trackers, outproxies, etc.), asegúrate de no sobrecargarlos, y habla con las personas que los administran para confirmar que está bien.

### Problemas de Hora / NTP

Nota: Esta sección se refiere a Java I2P. i2pd no incluye un cliente SNTP.

I2P incluye un cliente SNTP. I2P requiere la hora correcta para operar. Compensará un reloj del sistema desajustado, pero esto puede retrasar el arranque. Puedes desactivar las consultas SNTP de I2P, pero esto no se recomienda a menos que tu aplicación se asegure de que el reloj del sistema sea correcto.

### Elige Qué y Cómo Agrupar

Nota: Esta sección se refiere únicamente a Java I2P.

Como mínimo necesitarás i2p.jar, router.jar, streaming.jar, y mstreaming.jar. Puedes omitir los dos archivos jar de streaming para una aplicación que solo use datagramas. Algunas aplicaciones pueden necesitar más, por ejemplo i2ptunnel.jar o addressbook.jar. No olvides jbigi.jar, o un subconjunto del mismo para las plataformas que soportes, para hacer la criptografía mucho más rápida. Se requiere Java 7 o superior para compilar. Si estás compilando paquetes de Debian / Ubuntu, deberías requerir el paquete I2P de nuestro PPA en lugar de incluirlo. Casi con certeza no necesitas susimail, susidns, la consola del router, e i2psnark, por ejemplo.

Los siguientes archivos deben incluirse en el directorio de instalación de I2P, especificado con la propiedad "i2p.dir.base". No olvides el directorio certificates/, que es necesario para el reseeding, y blocklist.txt para la validación de IP. El directorio geoip es opcional, pero recomendado para que el router pueda tomar decisiones basadas en la ubicación. Si incluyes geoip, asegúrate de poner el archivo GeoLite2-Country.mmdb en ese directorio (descomprímelo desde installer/resources/GeoLite2-Country.mmdb.gz). El archivo hosts.txt puede ser necesario, puedes modificarlo para incluir cualquier host que use tu aplicación. Puedes agregar un archivo router.config al directorio base para anular los valores predeterminados iniciales. Revisa y edita o elimina los archivos clients.config e i2ptunnel.config.

Los requisitos de licencia pueden requerir que incluyas el archivo LICENSES.txt y el directorio de licencias.

- También podrías querer incluir un archivo hosts.txt.
- Asegúrate de especificar un bootclasspath si estás compilando Java I2P para tu lanzamiento, en lugar de tomar nuestros binarios.

### Consideraciones para Android

Nota: Esta sección se refiere solo a Java I2P.

Nuestra aplicación router de Android puede ser compartida por múltiples clientes. Si no está instalada, se le pedirá al usuario cuando inicie una aplicación cliente.

Algunos desarrolladores han expresado preocupación de que esta es una experiencia de usuario deficiente, y desean integrar el router en su aplicación. Tenemos en nuestra hoja de ruta una biblioteca de servicio de router para Android, que podría facilitar la integración. Se necesita más información.

Si necesita asistencia, por favor contáctenos.

### JARs de Maven

Nota: Esta sección se refiere únicamente a Java I2P.

Tenemos un número limitado de nuestros jars en [Maven Central](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22net.i2p%22). Hay numerosos tickets de trac que debemos abordar para mejorar y expandir los jars publicados en Maven Central.

Si necesita asistencia, por favor contáctenos.

### Consideraciones de datagramas (DHT)

Si tu aplicación está usando datagramas I2P, por ejemplo para una DHT, hay muchas opciones avanzadas disponibles para reducir la sobrecarga y aumentar la confiabilidad. Esto puede tomar algo de tiempo y experimentación para que funcione bien. Ten en cuenta los compromisos entre tamaño/confiabilidad. Habla con nosotros para obtener ayuda. Es posible - y recomendado - usar Datagrams y Streaming en el mismo Destination. No crees Destinations separados para esto. No trates de almacenar tus datos no relacionados en las DHTs de red existentes (iMule, bote, bittorrent, y router). Construye la tuya propia. Si estás codificando nodos semilla de forma fija, recomendamos que tengas varios.

### Outproxies

Los outproxies de I2P hacia la clearnet son un recurso limitado. Usa los outproxies solo para navegación web normal iniciada por el usuario u otro tráfico limitado. Para cualquier otro uso, consulta y obtén la aprobación del operador del outproxy.

### Comarketing

Trabajemos juntos. No esperes hasta que esté terminado. Danos tu usuario de Twitter y comienza a tuitear sobre esto, nosotros te devolveremos el favor.

### Malware

Por favor, no uses I2P para el mal. Podría causar un gran daño tanto a nuestra red como a nuestra reputación.

### Únete a nosotros

Esto puede ser obvio, pero únete a la comunidad. Ejecuta I2P 24/7. Crea un I2P Site sobre tu proyecto. Pasa tiempo en IRC #i2p-dev. Publica en los foros. Corre la voz. Podemos ayudarte a conseguir usuarios, probadores, traductores o incluso programadores.

---

## Ejemplos

### Ejemplos de Aplicaciones

Es posible que desees instalar y experimentar con la aplicación I2P para Android, y revisar su código, como ejemplo de una aplicación que incluye el router. Observa qué exponemos al usuario y qué ocultamos. Examina la máquina de estados que utilizamos para iniciar y detener el router. Otros ejemplos son: Vuze, la aplicación Nightweb para Android, iMule, TAILS, iCloak y Monero.

### Ejemplo de Código

Nota: Esta sección se refiere únicamente a Java I2P.

Nada de lo anterior te dice realmente cómo escribir tu código para empaquetar el router de Java, así que a continuación se presenta un breve ejemplo.

```java
import java.util.Properties;
import net.i2p.router.Router;

	Properties p = new Properties();
        // add your configuration settings, directories, etc.
        // where to find the I2P installation files
	p.addProperty("i2p.dir.base", baseDir);
        // where to find the I2P data files
	p.addProperty("i2p.dir.config", configDir);
        // bandwidth limits in K bytes per second
	p.addProperty("i2np.inboundKBytesPerSecond", "50");
	p.addProperty("i2np.outboundKBytesPerSecond", "50");
	p.addProperty("router.sharePercentage", "80");
	p.addProperty("foo", "bar");
	Router r = new Router(p);
        // don't call exit() when the router stops
	r.setKillVMOnEnd(false);
	r.runRouter();

	...

	r.shutdownGracefully();
	// will shutdown in 11 minutes or less
```
Este código es para el caso donde tu aplicación inicia el router, como en nuestra aplicación Android. También podrías hacer que el router inicie la aplicación a través de los archivos clients.config e i2ptunnel.config, junto con las webapps de Jetty, como se hace en nuestros paquetes Java. Como siempre, la gestión del estado es la parte difícil.

Véase también: [los javadocs del Router](http://idk.i2p/javadoc-i2p/net/i2p/router/Router.html).
