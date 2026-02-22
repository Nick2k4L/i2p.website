---
title: "Instalando I2P en macOS"
aliases:
  - "/es/docs/guides/installing-i2p-on-macos-the-long-way"
  - "/es/docs/guides/installing-i2p-on-macos-the-long-way/"
description: "Guía paso a paso para instalar manualmente I2P y sus dependencias en macOS"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

## Lo que necesitarás

- Una Mac ejecutando macOS 10.14 (Mojave) o posterior
- Acceso de administrador para instalar aplicaciones
- Aproximadamente 15-20 minutos de tiempo
- Conexión a Internet para descargar los instaladores

## Descripción general

Este proceso de instalación tiene cuatro pasos principales:

1. **Instalar Java** - Descargar e instalar Oracle Java Runtime Environment
2. **Instalar I2P** - Descargar y ejecutar el instalador de I2P
3. **Configurar la aplicación I2P** - Configurar el lanzador y agregar al dock
4. **Configurar el ancho de banda de I2P** - Ejecutar el asistente de configuración para optimizar tu conexión

## Parte Uno: Instalar Java

I2P requiere Java para ejecutarse. Si ya tienes Java 8 o posterior instalado, puedes [saltar a la Parte Dos](#part-two-download-and-install-i2p).

### Paso 1: Descargar Java

Visita la [página de descarga de Oracle Java](https://www.oracle.com/java/technologies/downloads/) y descarga el instalador de macOS para Java 8 o posterior.

![Descargar Oracle Java para macOS](/images/guides/macos-install/0-jre.png)

### Paso 2: Ejecutar el Instalador

Localiza el archivo `.dmg` descargado en tu carpeta de Descargas y haz doble clic para abrirlo.

![Abre el instalador de Java](/images/guides/macos-install/1-jre.png)

### Paso 3: Permitir la instalación

macOS puede mostrar una advertencia de seguridad porque el instalador proviene de un desarrollador identificado. Haz clic en **Abrir** para continuar.

![Otorga al instalador permiso para continuar](/images/guides/macos-install/2-jre.png)

### Paso 4: Instalar Java

Haz clic en **Instalar** para comenzar el proceso de instalación de Java.

![Comenzar instalación de Java](/images/guides/macos-install/3-jre.png)

### Paso 5: Esperar a que termine la instalación

El instalador copiará archivos y configurará Java en tu sistema. Esto generalmente toma de 1 a 2 minutos.

![Espera a que se complete el instalador](/images/guides/macos-install/4-jre.png)

### Paso 6: Instalación Completa

Cuando veas el mensaje de éxito, ¡Java está instalado! Haz clic en **Cerrar** para finalizar.

![Instalación de Java completada](/images/guides/macos-install/5-jre.png)

## Parte Dos: Descargar e Instalar I2P

Ahora que Java está instalado, puedes instalar el router I2P.

### Paso 1: Descargar I2P

Visita la [página de Descargas](/downloads/) y descarga el instalador **I2P para Unix/Linux/BSD/Solaris** (el archivo `.jar`).

![Descargar el instalador de I2P](/images/guides/macos-install/0-i2p.png)

### Paso 2: Ejecutar el Instalador

Haz doble clic en el archivo descargado `i2pinstall_X.X.X.jar`. El instalador se iniciará y te pedirá que selecciones tu idioma preferido.

![Selecciona tu idioma](/images/guides/macos-install/1-i2p.png)

### Paso 3: Pantalla de Bienvenida

Lee el mensaje de bienvenida y haz clic en **Siguiente** para continuar.

![Installer introduction](/images/guides/macos-install/2-i2p.png)

### Paso 4: Aviso Importante

El instalador mostrará un aviso importante sobre las actualizaciones. Las actualizaciones de I2P están **firmadas de extremo a extremo** y verificadas, aunque este instalador en sí mismo no esté firmado. Haz clic en **Siguiente**.

![Aviso importante sobre actualizaciones](/images/guides/macos-install/3-i2p.png)

### Paso 5: Acuerdo de Licencia

Lee el acuerdo de licencia de I2P (licencia estilo BSD). Haz clic en **Siguiente** para aceptar.

![Acuerdo de licencia](/images/guides/macos-install/4-i2p.png)

### Paso 6: Seleccionar Directorio de Instalación

Elige dónde instalar I2P. Se recomienda la ubicación predeterminada (`/Applications/i2p`). Haz clic en **Siguiente**.

![Seleccionar directorio de instalación](/images/guides/macos-install/5-i2p.png)

### Paso 7: Seleccionar Componentes

Deja todos los componentes seleccionados para una instalación completa. Haz clic en **Siguiente**.

![Seleccionar componentes a instalar](/images/guides/macos-install/6-i2p.png)

### Paso 8: Iniciar la Instalación

Revisa tus selecciones y haz clic en **Siguiente** para comenzar a instalar I2P.

![Iniciar la instalación](/images/guides/macos-install/7-i2p.png)

### Paso 9: Instalando Archivos

El instalador copiará los archivos de I2P a tu sistema. Esto toma aproximadamente 1-2 minutos.

![Instalación en progreso](/images/guides/macos-install/8-i2p.png)

### Paso 10: Generar Scripts de Lanzamiento

El instalador crea scripts de lanzamiento para iniciar I2P.

![Generando scripts de inicio](/images/guides/macos-install/9-i2p.png)

### Paso 11: Atajos de Instalación

El instalador ofrece crear accesos directos en el escritorio y entradas en el menú. Haz tus selecciones y haz clic en **Siguiente**.

![Crear accesos directos](/images/guides/macos-install/10-i2p.png)

### Paso 12: Instalación Completada

¡Éxito! I2P está ahora instalado. Haz clic en **Hecho** para finalizar.

![Instalación completa](/images/guides/macos-install/11-i2p.png)

## Parte Tres: Configurar la Aplicación I2P

Ahora hagamos que I2P sea fácil de ejecutar agregándolo a tu carpeta de Aplicaciones y al Dock.

### Paso 1: Abrir la carpeta Aplicaciones

Abre Finder y navega a tu carpeta **Aplicaciones**.

![Abrir la carpeta Aplicaciones](/images/guides/macos-install/0-conf.png)

### Paso 2: Buscar el Lanzador de I2P

Busca la carpeta **I2P** o la aplicación **Start I2P Router** dentro de `/Applications/i2p/`.

![Encuentra el lanzador de I2P](/images/guides/macos-install/1-conf.png)

### Paso 3: Agregar al Dock

Arrastra la aplicación **Start I2P Router** a tu Dock para un acceso fácil. También puedes crear un alias en tu escritorio.

![Agregar I2P a tu Dock](/images/guides/macos-install/2-conf.png)

**Consejo**: Haz clic derecho en el icono de I2P en el Dock y selecciona **Opciones → Mantener en el Dock** para hacerlo permanente.

## Parte Cuatro: Configurar el Ancho de Banda de I2P

Cuando inicies I2P por primera vez, ejecutarás un asistente de configuración para ajustar la configuración de ancho de banda. Esto ayuda a optimizar el rendimiento de I2P para tu conexión.

### Paso 1: Iniciar I2P

Haz clic en el icono de I2P en tu Dock (o haz doble clic en el lanzador). Tu navegador web predeterminado se abrirá en la Consola del Router I2P.

![Pantalla de bienvenida de la Consola del Router I2P](/images/guides/macos-install/0-wiz.png)

### Paso 2: Asistente de Bienvenida

El asistente de configuración te dará la bienvenida. Haz clic en **Siguiente** para comenzar a configurar I2P.

![Introducción del asistente de configuración](/images/guides/macos-install/1-wiz.png)

### Paso 3: Idioma y Tema

Selecciona tu **idioma de interfaz** preferido y elige entre el tema **claro** o **oscuro**. Haz clic en **Siguiente**.

![Seleccionar idioma y tema](/images/guides/macos-install/2-wiz.png)

### Paso 4: Información de Prueba de Ancho de Banda

El asistente explicará la prueba de ancho de banda. Esta prueba se conecta al servicio **M-Lab** para medir la velocidad de tu internet. Haz clic en **Siguiente** para continuar.

![Bandwidth test explanation](/images/guides/macos-install/3-wiz.png)

### Paso 5: Ejecutar Prueba de Ancho de Banda

Haz clic en **Ejecutar Prueba** para medir tus velocidades de subida y descarga. La prueba toma aproximadamente 30-60 segundos.

![Ejecutando la prueba de ancho de banda](/images/guides/macos-install/4-wiz.png)

### Paso 6: Resultados de las Pruebas

Revisa los resultados de tu prueba. I2P recomendará configuraciones de ancho de banda basadas en la velocidad de tu conexión.

![Resultados de la prueba de ancho de banda](/images/guides/macos-install/5-wiz.png)

### Paso 7: Configurar Compartición de Ancho de Banda

Elige cuánto ancho de banda quieres compartir con la red I2P:

- **Automático** (Recomendado): I2P gestiona el ancho de banda basado en tu uso
- **Limitado**: Establece límites específicos de subida/descarga
- **Ilimitado**: Comparte tanto como sea posible (para conexiones rápidas)

Haz clic en **Siguiente** para guardar tu configuración.

![Configurar compartición de ancho de banda](/images/guides/macos-install/6-wiz.png)

### Paso 8: Configuración Completa

¡Tu router I2P ahora está configurado y funcionando! La consola del router mostrará el estado de tu conexión y te permitirá navegar por sitios I2P.

## Comenzando con I2P

Ahora que I2P está instalado y configurado, puedes:

1. **Navegar sitios I2P**: Visita la [página principal de I2P](http://127.0.0.1:7657/home) para ver enlaces a servicios populares de I2P
2. **Configurar tu navegador**: Configura un [perfil de navegador](/docs/guides/browser-config) para acceder a sitios `.i2p`
3. **Explorar servicios**: Descubre el correo electrónico de I2P, foros, compartir archivos y más
4. **Monitorear tu router**: La [consola](http://127.0.0.1:7657/console) muestra el estado de tu red y estadísticas

### Enlaces Útiles

- **Consola del Router**: [http://127.0.0.1:7657/](http://127.0.0.1:7657/)
- **Configuración**: [http://127.0.0.1:7657/config](http://127.0.0.1:7657/config)
- **Libreta de Direcciones**: [http://127.0.0.1:7657/susidns/addressbook](http://127.0.0.1:7657/susidns/addressbook)
- **Configuración de Ancho de Banda**: [http://127.0.0.1:7657/config](http://127.0.0.1:7657/config)

## Volver a ejecutar el Asistente de configuración

Si quieres cambiar la configuración de ancho de banda o reconfigurar I2P más tarde, puedes ejecutar nuevamente el asistente de bienvenida desde la Consola del Router:

1. Ve al [Asistente de Configuración de I2P](http://127.0.0.1:7657/welcome)
2. Sigue los pasos del asistente nuevamente

## Solución de problemas

### I2P No Inicia

- **Verificar Java**: Asegúrate de que Java esté instalado ejecutando `java -version` en Terminal
- **Verificar permisos**: Asegúrate de que la carpeta de I2P tenga los permisos correctos
- **Verificar logs**: Revisa `~/.i2p/wrapper.log` para mensajes de error

### El navegador no puede acceder a sitios I2P

- Asegúrate de que I2P esté funcionando (verifica la Consola del Router)
- Configura los ajustes de proxy de tu navegador para usar el proxy HTTP `127.0.0.1:4444`
- Espera 5-10 minutos después del inicio para que I2P se integre en la red

### Rendimiento Lento

- Ejecuta la prueba de ancho de banda nuevamente y ajusta tu configuración
- Asegúrate de estar compartiendo algo de ancho de banda con la red
- Verifica el estado de tu conexión en la Consola del Router

## Desinstalando I2P

Para eliminar I2P de tu Mac:

1. Cierra el router I2P si está ejecutándose
2. Elimina la carpeta `/Applications/i2p`
3. Elimina la carpeta `~/.i2p` (tu configuración y datos de I2P)
4. Quita el icono de I2P de tu Dock

## Próximos Pasos

- **Únete a la comunidad**: Visita [i2pforum.net](http://i2pforum.net) o echa un vistazo a I2P en Reddit
- **Aprende más**: Lee la [documentación de I2P](/en/docs) para entender cómo funciona la red
- **Involúcrate**: Considera [contribuir al desarrollo de I2P](/en/get-involved) o ejecutar infraestructura

¡Felicidades! Ahora eres parte de la red I2P. ¡Bienvenido al internet invisible!

---
