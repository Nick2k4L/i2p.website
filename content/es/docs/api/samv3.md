---
title: "SAM V3"
description: "Protocolo de Mensajería Anónima Simple para aplicaciones I2P que no son de Java"
slug: "samv3"
aliases: 
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

SAM es un protocolo de cliente simple para interactuar con I2P. SAM es el protocolo recomendado para que aplicaciones no-Java se conecten a la red I2P, y es compatible con múltiples implementaciones de router. Las aplicaciones Java deberían usar las APIs de streaming o I2CP directamente.

SAMv3 fue introducida en la versión 0.7.3 de I2P (mayo de 2009) y es una interfaz estable y soportada. La versión 3.1 también es estable y soporta la opción de tipo de firma, que es altamente recomendada. Las versiones más recientes 3.x soportan características avanzadas. Ten en cuenta que i2pd actualmente no soporta la mayoría de las características de las versiones 3.2 y 3.3.

Alternativas: [SOCKS](/docs/api/socks), [Streaming](/docs/api/streaming), [I2CP](/docs/protocol/i2cp), [BOB (obsoleto)](/docs/api/bob). Versiones obsoletas: [SAM V1](/docs/api/sam), [SAM V2](/docs/api/samv2).

## Bibliotecas SAM Conocidas

Advertencia: Algunos de estos pueden ser muy antiguos o no estar soportados. Ninguno es probado, revisado o mantenido por el proyecto I2P a menos que se indique a continuación. Haz tu propia investigación.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Library Name</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Language</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">Version</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">STREAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">DGRAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">RAW</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Site</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2psam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++, C wrapper</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2psam">github.com/i2p/i2psam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">gosam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/goSam">github.com/eyedeekay/goSam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">sam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/sam3">github.com/eyedeekay/sam3</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">onramp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/onramp">github.com/eyedeekay/onramp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">txi2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/str4d/txi2p">github.com/str4d/txi2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.socket</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/majestrate/i2p.socket">github.com/majestrate/i2p.socket</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/l-n-s/i2plib">github.com/l-n-s/i2plib</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib-fork</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://codeberg.org/weko/i2plib-fork">codeberg.org/weko/i2plib-fork</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Py2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://i2pgit.org/robin/Py2p">i2pgit.org/robin/Py2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-rs</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2p-rs">github.com/i2p/i2p-rs</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">libsam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/libsam3">github.com/i2p/libsam3</a><br>(Maintained by the I2P project)</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">mooni2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Lua</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://notabug.org/villain/mooni2p">notabug.org/villain/mooni2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">haskell-network-anonymous-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Haskell</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/solatis/haskell-network-anonymous-i2p">github.com/solatis/haskell-network-anonymous-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-sam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Typescript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/diva-exchange/i2p-sam">github.com/diva-exchange/i2p-sam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">node-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Javascript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/redhog/node-i2p">github.com/redhog/node-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Jsam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/Jsam">github.com/eyedeekay/Jsam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">I2PSharp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/MohA39/I2PSharp">github.com/MohA39/I2PSharp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2pdotnet</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/SamuelFisher/i2pdotnet">github.com/SamuelFisher/i2pdotnet</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.rb</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Ruby</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/dryruby/i2p.rb">github.com/dryruby/i2p.rb</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">solitude</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/syvita/solitude">github.com/syvita/solitude</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Samty</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://notabug.org/acetone/samty">notabug.org/acetone/samty</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">bitcoin</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/bitcoin/bitcoin/blob/master/src/i2p.cpp">source (not a library, but good reference code)</a></td>
    </tr>
  </tbody>
</table>
## Inicio Rápido

Para implementar una aplicación básica punto a punto solo TCP, el cliente debe soportar los siguientes comandos:

- `HELLO VERSION MIN=3.1 MAX=3.1` - Necesario para todos los restantes
- `DEST GENERATE SIGNATURE_TYPE=7` - Para generar nuestra clave privada y destino
- `NAMING LOOKUP NAME=...` - Para convertir direcciones .i2p a destinos
- `SESSION CREATE STYLE=STREAM ID=... DESTINATION=... i2cp.leaseSetEncType=4,0` - Necesario para STREAM CONNECT y STREAM ACCEPT
- `STREAM CONNECT ID=... DESTINATION=...` - Para realizar conexiones salientes
- `STREAM ACCEPT ID=...` - Para aceptar conexiones entrantes

## Guía General para Desarrolladores

### Diseño de Aplicaciones

Las sesiones SAM (o dentro de I2P, pools de túneles o conjuntos de túneles) están diseñadas para ser de larga duración. La mayoría de las aplicaciones solo necesitarán una sesión, creada al iniciar y cerrada al salir. I2P es diferente de Tor, donde los circuitos pueden crearse y descartarse rápidamente. Piensa cuidadosamente y consulta con los desarrolladores de I2P antes de diseñar tu aplicación para usar más de una o dos sesiones simultáneas, o para crearlas y descartarlas rápidamente. La mayoría de los modelos de amenazas no requerirán una sesión única para cada conexión.

Además, asegúrese de que la configuración de su aplicación (y la orientación a los usuarios sobre la configuración del router, o los valores predeterminados del router si incluye uno) resulte en que sus usuarios contribuyan más recursos a la red de los que consumen. I2P es una red peer-to-peer, y la red no puede sobrevivir si una aplicación popular lleva la red a una congestión permanente.

### Compatibilidad y Pruebas

Las implementaciones de router Java I2P e i2pd son independientes y tienen diferencias menores en comportamiento, soporte de características y configuraciones predeterminadas. Por favor, prueba tu aplicación con la versión más reciente de ambos routers.

SAM de i2pd está habilitado por defecto; SAM de Java I2P no lo está. Proporciona instrucciones a tus usuarios sobre cómo habilitar SAM en Java I2P (a través de /configclients en la consola del router), y/o proporciona un buen mensaje de error al usuario si la conexión inicial falla, por ejemplo "asegúrate de que I2P esté ejecutándose y la interfaz SAM esté habilitada".

Los routers Java I2P e i2pd tienen diferentes valores predeterminados para las cantidades de tunnel. El predeterminado de Java es 2 y el predeterminado de i2pd es 5. Para la mayoría de casos con ancho de banda bajo a medio y conteos de conexión bajos a medios, 2 o 3 es suficiente. Por favor especifica la cantidad de tunnel en el mensaje SESSION CREATE para obtener rendimiento consistente con los routers Java I2P e i2pd. Ver más abajo.

Para más orientación a los desarrolladores sobre cómo asegurar que tu aplicación use solo los recursos que necesita, consulta [nuestra guía para incluir I2P con tu aplicación](/docs/applications/embedding).

### Tipos de Firma y Cifrado

I2P soporta múltiples tipos de firma y cifrado. Por compatibilidad hacia atrás, SAM usa por defecto tipos antiguos e ineficientes, por lo que todos los clientes deberían especificar tipos más nuevos.

El tipo de firma se especifica en los comandos DEST GENERATE y SESSION CREATE (para transitorios). Todos los clientes deben establecer `SIGNATURE_TYPE=7` (Ed25519).

El tipo de cifrado se especifica en el comando SESSION CREATE. Se permiten múltiples tipos de cifrado. Los clientes deben establecer ya sea `i2cp.leaseSetEncType=4` (solo para ECIES-X25519) o `i2cp.leaseSetEncType=4,0` (para ECIES-X25519 y ElGamal, si se requiere compatibilidad).

## Cambios de la Versión 3

### Cambios de la Versión 3.0

La versión 3.0 fue introducida en la versión 0.7.3 de I2P. SAMv2 proporcionaba una manera de gestionar varios sockets en el mismo destino de I2P *en paralelo*, es decir, el cliente no tenía que esperar a que los datos se enviaran exitosamente en un socket antes de enviar datos en otro socket. Pero todos los datos transitaban a través del mismo socket cliente-a-SAM, lo cual era bastante complicado de gestionar para el cliente.

SAM v3 gestiona los sockets de manera diferente: cada *socket I2P* coincide con un socket único cliente-a-SAM, lo cual es mucho más simple de manejar. Esto es similar a [BOB](/docs/api/bob).

SAMv3 también ofrece un puerto UDP para enviar datagramas a través de I2P, y puede reenviar datagramas I2P de vuelta al servidor de datagramas del cliente.

### Cambios de la Versión 3.1

La versión 3.1 fue introducida en el lanzamiento 0.9.14 de Java I2P (julio de 2014). SAMv3.1 es la implementación mínima recomendada de SAM debido a su soporte para mejores tipos de firma que SAMv3.0. i2pd también soporta la mayoría de las características de la versión 3.1.

- DEST GENERATE y SESSION CREATE ahora soportan un parámetro SIGNATURE_TYPE.
- Los parámetros MIN y MAX en HELLO VERSION ahora son opcionales.
- Los parámetros MIN y MAX en HELLO VERSION ahora soportan versiones de un solo dígito como "3".
- RAW SEND ahora es compatible en el socket bridge.

### Cambios de la Versión 3.2

La versión 3.2 fue introducida en el lanzamiento 0.9.24 de Java I2P (enero 2016). Ten en cuenta que i2pd actualmente no soporta la mayoría de las características de la versión 3.2.

#### Soporte de Puerto y Protocolo I2CP

- Opciones FROM_PORT y TO_PORT de SESSION CREATE
- Opción PROTOCOL de SESSION CREATE STYLE=RAW
- Opciones FROM_PORT y TO_PORT de STREAM CONNECT, DATAGRAM SEND y RAW SEND
- Opción PROTOCOL de RAW SEND
- DATAGRAM RECEIVED, RAW RECEIVED y streams reenviados o recibidos y datagramas respondibles, incluye FROM_PORT y TO_PORT
- La opción HEADER=true de sesión RAW hará que los datagramas raw reenviados sean precedidos por una línea que contenga PROTOCOL=nnn FROM_PORT=nnnn TO_PORT=nnnn
- La primera línea de datagramas enviados a través del puerto 7655 ahora puede comenzar con cualquier versión 3.x
- La primera línea de datagramas enviados a través del puerto 7655 puede contener cualquiera de las opciones FROM_PORT, TO_PORT, PROTOCOL
- RAW RECEIVED incluye PROTOCOL=nnn

#### SSL y Autenticación

- USER/PASSWORD en los parámetros HELLO para autorización. Ver [abajo](#authorization).
- Configuración de autorización opcional con el comando AUTH. Ver [abajo](#authorization-configuration-sam-32-or-higher-optional-feature).
- Soporte SSL/TLS opcional en el socket de control. Ver [abajo](#ssl).
- Opción STREAM FORWARD SSL=true

#### Multihilo

- Se permiten STREAM ACCEPTs pendientes concurrentes en la misma ID de sesión.

#### Análisis de Línea de Comandos y Keepalive

- Comandos opcionales QUIT, STOP y EXIT para cerrar la sesión y el socket. Ver [más abajo](#quitstopexitinvisible-sam-32-or-higher-optional-features).
- El análisis de comandos manejará correctamente UTF-8
- El análisis de comandos maneja de forma confiable los espacios en blanco dentro de comillas
- Una barra invertida '\\' puede escapar comillas en la línea de comandos
- Se recomienda que el servidor mapee los comandos a mayúsculas, para facilitar las pruebas a través de telnet.
- Valores de opción vacíos como PROTOCOL o PROTOCOL= pueden estar permitidos, dependiendo de la implementación.
- PING/PONG para mantener la conexión activa. Ver más abajo.
- Los servidores pueden implementar timeouts para el comando HELLO o comandos posteriores, dependiendo de la implementación.

### Cambios de la Versión 3.3

La versión 3.3 fue introducida en el lanzamiento 0.9.25 de Java I2P (marzo 2016). Ten en cuenta que i2pd actualmente no soporta la mayoría de las características de la versión 3.3.

- La misma sesión puede ser usada para streams, datagramas y raw simultáneamente. Los paquetes entrantes y streams serán enrutados basándose en el protocolo I2P y el puerto de destino. Ver [la sección PRIMARY más abajo](#sam-primary-sessions-v33-and-higher).
- DATAGRAM SEND y RAW SEND ahora soportan las opciones SEND_TAGS, TAG_THRESHOLD, EXPIRES y SEND_LEASESET. Ver [la sección de envío de datagramas más abajo](#sending-repliable-or-raw-datagrams).

## Protocolo Versión 3

### Descripción General de la Especificación de Simple Anonymous Messaging (SAM) Versión 3.3

La aplicación cliente se comunica con el puente SAM, que maneja toda la funcionalidad de I2P (usando la [biblioteca de streaming](/docs/api/streaming) para flujos virtuales, o [I2CP](/docs/protocol/i2cp) directamente para datagramas).

Por defecto, la comunicación entre el cliente y el puente SAM no está cifrada ni autenticada. El puente SAM puede soportar conexiones SSL/TLS; los detalles de configuración e implementación están fuera del alcance de esta especificación. A partir de SAM 3.2, se soportan parámetros opcionales de autenticación usuario/contraseña en el handshake inicial y pueden ser requeridos por el puente.

Las comunicaciones I2P pueden tomar varias formas distintas:

- [Flujos virtuales](/docs/api/streaming)
- [Datagramas replicables y autenticados](/docs/specs/datagrams#repliable) (mensajes con un campo FROM)
- [Datagramas anónimos](/docs/specs/datagrams#raw) (mensajes anónimos en bruto)
- [Datagram2](/docs/specs/datagrams#datagram2) (un nuevo formato replicable y autenticado)
- [Datagram3](/docs/specs/datagrams#datagram3) (un nuevo formato replicable pero no autenticado)

Las comunicaciones I2P son soportadas por sesiones I2P, y cada sesión I2P está vinculada a una dirección (llamada destination). Una sesión I2P está asociada con uno de los tres tipos anteriores, y no puede transportar comunicaciones de otro tipo, a menos que use [sesiones PRIMARY](#sam-primary-sessions-v33-and-higher).

### Codificación y Escapado

Todos estos mensajes SAM se envían en una sola línea, terminados por el carácter de nueva línea (\\n). Antes de SAM 3.2, solo se admitía ASCII de 7 bits. A partir de SAM 3.2, la codificación debe ser UTF-8. Cualquier clave o valor codificado en UTF8 debería funcionar.

El formato mostrado en esta especificación a continuación es únicamente para mejorar la legibilidad, y aunque las primeras dos palabras en cada mensaje deben mantener su orden específico, el ordenamiento de los pares clave=valor puede cambiar (por ejemplo, "ONE TWO A=B C=D" o "ONE TWO C=D A=B" son ambas construcciones perfectamente válidas). Además, el protocolo es sensible a mayúsculas y minúsculas. En lo que sigue, los ejemplos de mensajes van precedidos por "->" para mensajes enviados por el cliente al puente SAM, y por "<-" para mensajes enviados por el puente SAM al cliente.

La línea de comando o respuesta básica toma una de las siguientes formas:

```
COMMAND SUBCOMMAND [key=value] [key=value] ...
COMMAND                                           # As of SAM 3.2
PING[ arbitrary text]                             # As of SAM 3.2
PONG[ arbitrary text]                             # As of SAM 3.2
```
COMMAND sin un SUBCOMMAND es compatible solo con algunos comandos nuevos en SAM 3.2.

Los pares clave=valor deben estar separados por un solo espacio. (A partir de SAM 3.2, se permiten múltiples espacios) Los valores deben estar encerrados en comillas dobles si contienen espacios, por ejemplo key="long value text". (Antes de SAM 3.2, esto no funcionaba de manera confiable en algunas implementaciones)

Antes de SAMv3.2, no existía un mecanismo de escape. A partir de SAMv3.2, las comillas dobles pueden ser escapadas con una barra invertida '\\' y una barra invertida puede ser representada como dos barras invertidas '\\\\'.

### Valores Vacíos

A partir de SAM 3.2, los valores de opción vacíos como KEY, KEY=, o KEY="" pueden estar permitidos, dependiendo de la implementación.

### Sensibilidad a Mayúsculas y Minúsculas

El protocolo, según se especifica, distingue entre mayúsculas y minúsculas. Se recomienda pero no es obligatorio que el servidor mapee los comandos a mayúsculas, para facilitar las pruebas vía telnet. Esto permitiría, por ejemplo, que "hello version" funcione. Esto depende de la implementación. No mapees las claves o valores a mayúsculas, ya que esto corrompería las opciones de [I2CP](/docs/protocol/i2cp).

### Protocolo de conexión SAM

No puede ocurrir ninguna comunicación SAM hasta que el cliente y el puente hayan acordado una versión de protocolo, lo cual se hace cuando el cliente envía un HELLO y el puente envía un HELLO REPLY:

```
->  HELLO VERSION
          [MIN=$min]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [MAX=$max]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [USER="xxx"]          # As of SAM 3.2, required if authentication is enabled, see below
          [PASSWORD="yyy"]      # As of SAM 3.2, required if authentication is enabled, see below
```
y

```
<-  HELLO REPLY RESULT=OK VERSION=3.1
```
A partir de la versión 3.1 (I2P 0.9.14), los parámetros MIN y MAX son opcionales. SAM siempre devolverá la versión más alta posible dados los límites MIN y MAX, o la versión actual del servidor si no se proporcionan límites.

Si el puente SAM no puede encontrar una versión adecuada, responde con:

```
<- HELLO REPLY RESULT=NOVERSION
```
Si ocurre algún error, como un formato de solicitud incorrecto, responde con:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
#### SSL

El socket de control del servidor puede ofrecer opcionalmente soporte SSL/TLS, según se configure en el servidor y el cliente. Las implementaciones pueden ofrecer otras capas de transporte también; esto está fuera del alcance de la definición del protocolo.

#### Autorización

Para la autorización, el cliente agrega USER="xxx" PASSWORD="yyy" a los parámetros de HELLO. Se recomiendan las comillas dobles para el usuario y contraseña pero no son obligatorias. Una comilla doble dentro de un usuario o contraseña debe ser escapada con una barra invertida. En caso de fallo, el servidor responderá con un I2P_ERROR y un mensaje. Se recomienda que SSL esté habilitado en cualquier servidor SAM donde se requiera autorización.

#### Tiempos de espera

Los servidores pueden implementar timeouts para el comando HELLO o comandos posteriores, dependiendo de la implementación. Los clientes deben enviar rápidamente el HELLO y el siguiente comando después de conectarse.

Si ocurre un timeout antes de que se reciba el HELLO, el bridge responde con:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
y luego se desconecta.

Si ocurre un timeout después de recibir el HELLO pero antes del siguiente comando, el puente responde con:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
y luego se desconecta.

### Puertos y Protocolo I2CP

A partir de SAM 3.2, los puertos y protocolos [I2CP](/docs/protocol/i2cp) pueden ser especificados por el cliente SAM remitente para ser pasados a [I2CP](/docs/protocol/i2cp), y el puente SAM pasará la información de puerto y protocolo [I2CP](/docs/protocol/i2cp) recibida al cliente SAM.

Para FROM_PORT y TO_PORT, el rango válido es 0-65535, y el valor predeterminado es 0.

Para PROTOCOL, que solo puede especificarse para RAW, el rango válido es 0-255, y el valor predeterminado es 18.

Para los comandos SESSION, los puertos y protocolo especificados son los valores por defecto para esa sesión. Para streams o datagramas individuales, los puertos y protocolo especificados anulan los valores por defecto de la sesión. Para streams o datagramas recibidos, los puertos y protocolo indicados son tal como se recibieron desde [I2CP](/docs/protocol/i2cp).

#### Diferencias Importantes con el IP Estándar

Los puertos I2CP son para sockets y datagramas de I2P. No están relacionados con tus sockets locales que se conectan a SAM.

- El puerto 0 es válido y tiene un significado especial.
- Los puertos 1-1023 no son especiales ni privilegiados.
- Los servidores escuchan en el puerto 0 por defecto, lo que significa "todos los puertos".
- Los clientes envían al puerto 0 por defecto, lo que significa "cualquier puerto".
- Los clientes envían desde el puerto 0 por defecto, lo que significa "sin especificar".
- Los servidores pueden tener un servicio escuchando en el puerto 0 y otros servicios escuchando en puertos superiores. En ese caso, el servicio del puerto 0 es el predeterminado, y se conectará si el socket entrante o el puerto del datagrama no coincide con otro servicio.
- La mayoría de destinos I2P solo tienen un servicio ejecutándose en ellos, por lo que puedes usar los valores predeterminados e ignorar la configuración de puertos I2CP.
- Se requiere SAM 3.2 o 3.3 para especificar puertos I2CP.
- Si no necesitas puertos I2CP, no necesitas SAM 3.2 o 3.3; 3.1 es suficiente.
- El protocolo 0 es válido y significa "cualquier protocolo". Esto no se recomienda, y probablemente no funcionará.
- Los sockets I2P son rastreados por un ID de conexión interno. Por lo tanto, no hay requisito de que la tupla de 5 elementos destino:puerto:destino:puerto:protocolo sea única. Por ejemplo, puede haber múltiples sockets con los mismos puertos entre dos destinos. Los clientes no necesitan elegir un "puerto libre" para una conexión saliente.

Si estás diseñando una aplicación SAM 3.3 con múltiples subsesiones, piensa cuidadosamente en cómo usar puertos y protocolos de manera efectiva. Consulta la especificación [I2CP](/docs/protocol/i2cp) para más información.

### Sesiones SAM

Una sesión SAM se crea cuando un cliente abre un socket al puente SAM, realiza un handshake y envía un mensaje SESSION CREATE, y la sesión termina cuando el socket se desconecta.

Cada Destino I2P registrado está asociado únicamente con un ID de sesión (o apodo). Los IDs de sesión, incluyendo los IDs de subsesión para sesiones PRIMARY, deben ser globalmente únicos en el servidor SAM. Para prevenir posibles colisiones de ID con otros clientes, la mejor práctica es que el cliente genere los IDs de forma aleatoria.

Cada sesión está asociada de forma única con:

- el socket desde el cual el cliente crea la sesión
- su ID (o apodo)

#### Solicitud de Creación de Sesión

El mensaje de creación de sesión solo puede usar una de estas formas (los mensajes recibidos a través de otras formas se responden con un mensaje de error):

```
->  SESSION CREATE
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, for DESTINATION=TRANSIENT only, default DSA_SHA1
          [PORT=$port]                         # Required for DATAGRAM* RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [HEADER={true,false}]                # SAM 3.2 or higher only, for STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
DESTINATION especifica qué destino debe usarse para enviar y recibir mensajes/flujos. El $privkey es la base 64 de la concatenación del [Destination](/docs/specs/common-structures#type_Destination) seguido de la [Private Key](/docs/specs/common-structures#type_PrivateKey) seguida de la [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), opcionalmente seguida de la [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), que son 663 o más bytes en binario y 884 o más bytes en base 64, dependiendo del tipo de firma. El formato binario se especifica en Private Key File. Consulta las notas adicionales sobre la [Private Key](/docs/specs/common-structures#type_PrivateKey) en la sección Generación de Claves de Destino a continuación.

Si la clave privada de firma es todo ceros, sigue la sección [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature). Las firmas offline solo son compatibles con sesiones STREAM y RAW. Las firmas offline no pueden crearse con DESTINATION=TRANSIENT. El formato de la sección de firma offline es:

1. Marca de tiempo de expiración (4 bytes, big endian, segundos desde época, se reinicia en 2106)
2. Tipo de sig de la Clave Pública de Firma transitoria (2 bytes, big endian)
3. Clave Pública de Firma transitoria (longitud según especifica el tipo de sig transitoria)
4. Firma de los tres campos anteriores por clave offline (longitud según especifica el tipo de sig del destino)
5. Clave Privada de Firma transitoria (longitud según especifica el tipo de sig transitoria)

Si el destino se especifica como TRANSIENT, el puente SAM crea un nuevo destino. A partir de la versión 3.1 (I2P 0.9.14), si el destino es TRANSIENT, se admite un parámetro opcional SIGNATURE_TYPE. El valor de SIGNATURE_TYPE puede ser cualquier nombre (ej. ECDSA_SHA256_P256, sin distinción de mayúsculas y minúsculas) o número (ej. 1) compatible con [Key Certificates](/docs/specs/common-structures#type_Certificate). El valor por defecto es DSA_SHA1, que NO es lo que deseas. Para la mayoría de aplicaciones, por favor especifica SIGNATURE_TYPE=7.

$nickname es la elección del cliente. No se permiten espacios en blanco.

Las opciones adicionales proporcionadas se pasan a la configuración de la sesión I2P si no son interpretadas por el puente SAM (por ejemplo, outbound.length=0).

Los routers de Java I2P e i2pd tienen diferentes valores predeterminados para las cantidades de túneles. El valor predeterminado de Java es 2 y el de i2pd es 5. Para la mayoría de casos con ancho de banda bajo a medio y recuentos de conexiones bajos a medios, 2 o 3 es suficiente. Por favor, especifica las cantidades de túneles en el mensaje SESSION CREATE para obtener un rendimiento consistente con los routers de Java I2P e i2pd, usando las opciones como por ejemplo inbound.quantity=3 outbound.quantity=3. Estas y otras opciones [están documentadas en los enlaces a continuación](#tunnel-i2cp-and-streaming-options).

El puente SAM en sí ya debería estar configurado con el router con el que debe comunicarse a través de I2P (aunque si es necesario puede haber una forma de proporcionar una anulación, por ejemplo, i2cp.tcp.host=localhost e i2cp.tcp.port=7654).

#### Respuesta de Creación de Sesión

Después de recibir el mensaje de creación de sesión, el puente SAM responderá con un mensaje de estado de sesión, como sigue:

Si la creación fue exitosa:

```
<-  SESSION STATUS RESULT=OK DESTINATION=$privkey
```
El $privkey es la base 64 de la concatenación del [Destination](/docs/specs/common-structures#type_Destination) seguido de la [Private Key](/docs/specs/common-structures#type_PrivateKey) seguido de la [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), opcionalmente seguido de la [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), que son 663 o más bytes en binario y 884 o más bytes en base 64, dependiendo del tipo de firma. El formato binario se especifica en Private Key File.

Si el SESSION CREATE contenía una clave privada de firma de todos ceros y una sección [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), la respuesta SESSION STATUS incluirá los mismos datos en el mismo formato. Consulta la sección SESSION CREATE anterior para más detalles.

Si el apodo ya está asociado con una sesión:

```
<-  SESSION STATUS RESULT=DUPLICATED_ID
```
Si el destino ya está en uso:

```
<-  SESSION STATUS RESULT=DUPLICATED_DEST
```
Si el destino no es una clave de destino privada válida:

```
<-  SESSION STATUS RESULT=INVALID_KEY
```
Si ha ocurrido algún otro error:

```
<-  SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
Si no está bien, el MESSAGE debería contener información legible para humanos sobre por qué la sesión no pudo ser creada.

Ten en cuenta que el router construye túneles antes de responder con SESSION STATUS. Esto podría tomar varios segundos, o, al iniciar el router o durante congestión severa de la red, un minuto o más. Si no tiene éxito, el router no responderá con un mensaje de falla durante varios minutos. No establezcan un timeout corto esperando la respuesta. No abandones la sesión mientras la construcción del túnel está en progreso y reintentes.

Las sesiones SAM viven y mueren con el socket al que están asociadas. Cuando el socket se cierra, la sesión muere, y todas las comunicaciones que usan la sesión mueren al mismo tiempo. Y de la otra manera, cuando la sesión muere por cualquier razón, el puente SAM cierra el socket.

### Flujos Virtuales SAM

Los flujos virtuales están garantizados para ser enviados de manera confiable y en orden, con notificación de fallo y éxito tan pronto como esté disponible.

Los streams son sockets de comunicación bidireccional entre dos destinos I2P, pero su apertura debe ser solicitada por uno de ellos. En adelante, los comandos CONNECT son utilizados por el cliente SAM para realizar dicha solicitud. Los comandos FORWARD / ACCEPT son utilizados por el cliente SAM cuando quiere escuchar solicitudes provenientes de otros destinos I2P.

### SAM Virtual Streams: CONNECT

Un cliente solicita una conexión mediante:

- abrir un nuevo socket con el puente SAM
- pasar el mismo handshake HELLO como se muestra arriba
- enviar el comando STREAM CONNECT

#### Solicitud de Conexión

```
-> STREAM CONNECT
         ID=$nickname
         DESTINATION=$destination
         [SILENT={true,false}]                # default false
         [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
         [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
```
Esto establece una nueva conexión virtual desde la sesión local cuyo ID es $nickname al peer especificado.

El objetivo es $destination, que es la base 64 del [Destination](/docs/specs/common-structures#type_Destination), el cual tiene 516 o más caracteres en base 64 (387 o más bytes en binario), dependiendo del tipo de firma.

**NOTA:** Desde aproximadamente 2014 (SAM v3.1), Java I2P también ha soportado nombres de host y direcciones b32 para el $destination, pero esto no estaba documentado anteriormente. Los nombres de host y direcciones b32 ahora son oficialmente soportados por Java I2P a partir de la versión 0.9.48. El router i2pd soporta nombres de host y direcciones b32 a partir de la versión 2.38.0 (0.9.50). Para ambos routers, el soporte "b32" incluye soporte para direcciones "b33" extendidas para destinos ciegos.

#### Respuesta de Conexión

Si se pasa SILENT=true, el puente SAM no emitirá ningún otro mensaje en el socket. Si la conexión falla, el socket se cerrará. Si la conexión tiene éxito, todos los datos restantes que pasen a través del socket actual se reenviarán desde y hacia el peer de destino I2P conectado.

Si SILENT=false, que es el valor predeterminado, el puente SAM envía un último mensaje a su cliente antes de reenviar o cerrar el socket:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
El valor RESULT puede ser uno de:

```
OK
CANT_REACH_PEER
I2P_ERROR
INVALID_KEY
INVALID_ID
TIMEOUT
```
Si el RESULT es OK, todos los datos restantes que pasen por el socket actual se reenvían desde y hacia el peer de destino I2P conectado. Si la conexión no fue posible (timeout, etc), RESULT contendrá el valor de error apropiado (acompañado por un MESSAGE legible opcional), y el puente SAM cierra el socket.

El tiempo de espera de conexión del stream del router internamente es aproximadamente de un minuto, dependiente de la implementación. No establezcas un tiempo de espera más corto esperando la respuesta.

### Flujos Virtuales SAM: ACCEPT

Un cliente espera una solicitud de conexión entrante mediante:

- abriendo un nuevo socket con el puente SAM
- pasando el mismo saludo HELLO que arriba
- enviando el comando STREAM ACCEPT

#### Aceptar Solicitud

```
-> STREAM ACCEPT
         ID=$nickname
         [SILENT={true,false}]                # default false
```
Esto hace que la sesión ${nickname} escuche una solicitud de conexión entrante desde la red I2P. ACCEPT no está permitido mientras hay un FORWARD activo en la sesión.

A partir de SAM 3.2, se permiten múltiples STREAM ACCEPTs pendientes concurrentes en la misma ID de sesión (incluso con el mismo puerto). Antes de la versión 3.2, los accepts concurrentes fallarían con ALREADY_ACCEPTING. Nota: Java I2P también soporta ACCEPTs concurrentes en SAM 3.1, desde la versión 0.9.24 (2016-01). i2pd también soporta ACCEPTs concurrentes en SAM 3.1, desde la versión 2.50.0 (2023-12).

#### Respuesta de Aceptación

Si se pasa SILENT=true, el puente SAM no emitirá ningún otro mensaje en el socket. Si la aceptación falla, el socket se cerrará. Si la aceptación tiene éxito, todos los datos restantes que pasen por el socket actual se reenvían desde y hacia el destino I2P conectado. Para mayor confiabilidad, y para recibir el destino de las conexiones entrantes, se recomienda SILENT=false.

Si SILENT=false, que es el valor predeterminado, el puente SAM responde con:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
El valor RESULT puede ser uno de:

```
OK
I2P_ERROR
INVALID_ID
```
Si el resultado no es OK, el socket se cierra inmediatamente por el puente SAM. Si el resultado es OK, el puente SAM comienza a esperar una solicitud de conexión entrante de otro peer I2P. Cuando llega una solicitud, el puente SAM la acepta y:

Si se pasó SILENT=true, el puente SAM no emitirá ningún otro mensaje en el socket del cliente. Todos los datos restantes que pasen a través del socket actual se reenvían desde y hacia el peer de destino I2P conectado.

Si se pasó SILENT=false, que es el valor predeterminado, el puente SAM envía al cliente una línea ASCII que contiene la clave de destino público base64 del peer solicitante, e información adicional solo para SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Después de esta línea terminada en '\\n', todos los datos restantes que pasan a través del socket actual se reenvían desde y hacia el peer de destino I2P conectado, hasta que uno de los peers cierre el socket.

#### Errores Después de OK

En casos excepcionales, el puente SAM puede encontrar un error después de enviar RESULT=OK, pero antes de que llegue una conexión y se envíe la línea $destination al cliente. Estos errores pueden incluir apagado del router, reinicio del router y cierre de sesión. En estos casos, cuando SILENT=false, el puente SAM puede, pero no está obligado a (dependiente de la implementación), enviar la línea:

```
<-  STREAM STATUS
         RESULT=I2P_ERROR
         [MESSAGE=...]
```
antes de cerrar inmediatamente el socket. Esta línea no es, por supuesto, decodificable como un destino Base 64 válido.

### SAM Virtual Streams: FORWARD

Un cliente puede usar un servidor de socket regular y esperar solicitudes de conexión provenientes de I2P. Para eso, el cliente debe:

- abrir un nuevo socket con el puente SAM
- pasar el mismo handshake HELLO que arriba
- enviar el comando forward

#### Solicitud de Reenvío

```
-> STREAM FORWARD
         ID=$nickname
         PORT=$port
         [HOST=$host]
         [SILENT={true,false}]                # default false
         [SSL={true,false}]                   # SAM 3.2 or higher only, default false
```
Esto hace que la sesión ${nickname} escuche las solicitudes de conexión entrantes desde la red I2P. FORWARD no está permitido mientras haya un ACCEPT pendiente en la sesión.

#### Respuesta de Reenvío

SILENT tiene como valor predeterminado false. Ya sea que SILENT sea true o false, el puente SAM siempre responde con un mensaje STREAM STATUS. Tenga en cuenta que este es un comportamiento diferente de STREAM ACCEPT y STREAM CONNECT cuando SILENT=true. El mensaje STREAM STATUS es:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
El valor RESULT puede ser uno de:

```
OK
I2P_ERROR
INVALID_ID
```
$host es el nombre de host o dirección IP del servidor de socket al cual SAM reenviará las solicitudes de conexión. Si no se proporciona, SAM toma la IP del socket que emitió el comando forward.

$port es el número de puerto del servidor de socket al cual SAM reenviará las solicitudes de conexión. Es obligatorio.

Cuando llega una solicitud de conexión desde I2P, el puente SAM abre una conexión de socket a $host:$port. Si es aceptada en menos de 3 segundos, SAM aceptará la conexión desde I2P, y entonces:

Si se pasó SILENT=true, todos los datos que pasan a través del socket actual obtenido se reenvían desde y hacia el peer de destino I2P conectado.

Si se pasó SILENT=false, que es el valor predeterminado, el puente SAM envía en el socket obtenido una línea ASCII que contiene la clave de destino público base64 del peer solicitante, e información adicional solo para SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Después de esta línea terminada con '\\n', todos los datos restantes que pasan a través del socket son reenviados desde y hacia el peer de destino I2P conectado, hasta que uno de los lados cierre el socket.

A partir de SAM 3.2, si se especifica SSL=true, el socket de reenvío es sobre SSL/TLS.

El router I2P dejará de escuchar las solicitudes de conexión entrantes tan pronto como se cierre el socket de "reenvío".

### Datagramas SAM

SAMv3 proporciona mecanismos para enviar y recibir datagramas a través de sockets de datagrama locales. Algunas implementaciones de SAMv3 también admiten la forma más antigua v1/v2 de enviar/recibir datagramas a través del socket puente SAM. Ambas están documentadas a continuación.

I2P admite cuatro tipos de datagramas:

- Los datagramas replicables y autenticados tienen como prefijo el destino del remitente, y contienen la firma del remitente, para que el receptor pueda verificar que el destino del remitente no fue falsificado, y pueda responder al datagrama. El nuevo formato Datagram2 también es replicable y autenticado.
- El nuevo formato Datagram3 es replicable pero no autenticado. La información del remitente no está verificada.
- Los datagramas sin procesar no contienen el destino del remitente ni una firma.

Los puertos I2CP por defecto están definidos tanto para datagramas con respuesta como para datagramas sin procesar. El puerto I2CP puede cambiarse para datagramas sin procesar.

Un patrón de diseño de protocolo común es que los datagramas con respuesta se envíen a los servidores, con algún identificador incluido, y que el servidor responda with un datagrama raw que incluya ese identificador, para que la respuesta pueda correlacionarse con la solicitud. Este patrón de diseño elimina la sobrecarga sustancial de los datagramas con respuesta en las respuestas. Todas las opciones de protocolos y puertos I2CP son específicas de la aplicación, y los diseñadores deberían tomar estas cuestiones en consideración.

Consulta también las notas importantes sobre el MTU de datagramas en la sección a continuación.

#### Envío de Datagramas con Respuesta o Sin Procesar

Aunque I2P no contiene inherentemente una dirección FROM, para facilitar el uso se proporciona una capa adicional como datagramas respondibles - mensajes no ordenados y no confiables de hasta 31744 bytes que incluyen una dirección FROM (dejando hasta 1KB para material de cabecera). Esta dirección FROM es autenticada internamente por SAM (haciendo uso de la clave de firma del destino para verificar la fuente) e incluye prevención de reproducción.

El tamaño mínimo es 1. Para una mejor confiabilidad de entrega, el tamaño máximo recomendado es de aproximadamente 11 KB. La confiabilidad es inversamente proporcional al tamaño del mensaje, quizás incluso exponencialmente.

Después de establecer una sesión SAM con STYLE=DATAGRAM o STYLE=RAW, el cliente puede enviar datagramas respondibles o en bruto a través del puerto UDP de SAM (7655 por defecto).

La primera línea de un datagrama enviado a través de este puerto debe tener el siguiente formato. Todo esto va en una sola línea (separado por espacios), mostrado en múltiples líneas para mayor claridad:

```
3.0                                  # As of SAM 3.2, any "3.x" is allowed. Prior to that, "3.0" is required.
$nickname
$destination
[FROM_PORT=nnn]                      # SAM 3.2 or higher only, default from session options
[TO_PORT=nnn]                        # SAM 3.2 or higher only, default from session options
[PROTOCOL=nnn]                       # SAM 3.2 or higher only, only for RAW sessions, default from session options
[SEND_TAGS=nnn]                      # SAM 3.3 or higher only, number of session tags to send
                                     # Overrides crypto.tagsToSend I2CP session option
                                     # Default is router-dependent (40 for Java router)
[TAG_THRESHOLD=nnn]                  # SAM 3.3 or higher only, low session tag threshold
                                     # Overrides crypto.lowTagThreshold I2CP session option
                                     # Default is router-dependent (30 for Java router)
[EXPIRES=nnn]                        # SAM 3.3 or higher only, expiration from now in seconds
                                     # Overrides clientMessageTimeout I2CP session option (which is in ms)
                                     # Default is router-dependent (60 for Java router)
[SEND_LEASESET={true,false}]         # SAM 3.3 or higher only, whether to send our leaseset
                                     # Overrides shouldBundleReplyInfo I2CP session option
                                     # Default is true
\n
```
- 3.0 es la versión de SAM. A partir de SAM 3.2, cualquier versión 3.x está permitida.
- $nickname es el id de la sesión DATAGRAM que se utilizará
- El destino es $destination, que es la base 64 del [Destination](/docs/specs/common-structures#type_Destination), que son 516 o más caracteres en base 64 (387 o más bytes en binario), dependiendo del tipo de firma. **NOTA:** Desde aproximadamente 2014 (SAM v3.1), Java I2P también ha soportado nombres de host y direcciones b32 para $destination, pero esto no estaba documentado anteriormente. Los nombres de host y direcciones b32 ahora son oficialmente soportados por Java I2P a partir de la versión 0.9.48. El router i2pd actualmente no soporta nombres de host y direcciones b32; el soporte puede agregarse en una versión futura.
- Todas las opciones son configuraciones por datagrama que anulan los valores predeterminados especificados en SESSION CREATE.
- Las opciones de la versión 3.3 SEND_TAGS, TAG_THRESHOLD, EXPIRES y SEND_LEASESET se pasarán a [I2CP](/docs/protocol/i2cp) si son soportadas. Consulte [la especificación I2CP](/docs/protocol/i2cp#msg_SendMessageExpire) para más detalles. El soporte por parte del servidor SAM es opcional, ignorará estas opciones si no son soportadas.
- esta línea termina con '\\n'.

La primera línea será descartada por SAM antes de enviar los datos restantes del mensaje al destino especificado.

Para un método alternativo de envío de datagramas que admiten respuesta y datagramas sin procesar, consulte [DATAGRAM SEND y RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### SAM Repliable Datagrams: Recibir un Datagrama

Los datagramas recibidos son escritos por SAM en el socket desde el cual se abrió la sesión de datagramas, si no se especifica un PORT de reenvío en el comando SESSION CREATE. Esta es la forma compatible con v1/v2 de recibir datagramas.

Cuando llega un datagrama, el bridge lo entrega al cliente a través del mensaje:

```
<-  DATAGRAM RECEIVED
           DESTINATION=$destination           # See notes below for Datagram3 format
           SIZE=$numBytes
           FROM_PORT=nnn                      # SAM 3.2 or higher only
           TO_PORT=nnn                        # SAM 3.2 or higher only
           \n
       [$numBytes of data]
```
La fuente es $destination, que es la base 64 del [Destination](/docs/specs/common-structures#type_Destination), que son 516 o más caracteres en base 64 (387 o más bytes en binario), dependiendo del tipo de firma.

El puente SAM nunca expone al cliente las cabeceras de autenticación u otros campos, únicamente los datos que proporcionó el remitente. Esto continúa hasta que se cierra la sesión (cuando el cliente corta la conexión).

#### Reenviando Datagramas Raw o Respondibles

Al crear una sesión de datagram, el cliente puede solicitar a SAM que reenvíe los mensajes entrantes a una ip:puerto específica. Lo hace emitiendo el comando CREATE con las opciones PORT y HOST:

```
-> SESSION CREATE
          STYLE={DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          PORT=$port
          [HOST=$host]
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP options
```
El $privkey es la base 64 de la concatenación del [Destination](/docs/specs/common-structures#type_Destination) seguido de la [Private Key](/docs/specs/common-structures#type_PrivateKey) seguido de la [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), opcionalmente seguido de la [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), que son 884 o más caracteres en base 64 (663 o más bytes en binario), dependiendo del tipo de firma. El formato binario se especifica en Private Key File.

Las firmas sin conexión son compatibles con datagramas RAW, DATAGRAM2 y DATAGRAM3, pero no con DATAGRAM. Consulte la sección SESSION CREATE anterior y la sección DATAGRAM2/3 a continuación para más detalles.

$host es el nombre de host o dirección IP del servidor de datagramas al cual SAM reenviará los datagramas. Si no se proporciona, SAM toma la IP del socket que emitió el comando forward.

$port es el número de puerto del servidor de datagramas al cual SAM reenviará los datagramas. Si $port no está configurado, los datagramas NO serán reenviados, serán recibidos en el socket de control, de la manera compatible con v1/v2.

Las opciones adicionales proporcionadas se pasan a la configuración de sesión I2P si no son interpretadas por el puente SAM (por ejemplo, outbound.length=0). Estas opciones [están documentadas más abajo](#tunnel-i2cp-and-streaming-options).

Los datagramas reenviables enviados siempre tienen como prefijo el destino en base64, excepto para Datagram3, ver más abajo. Cuando llega un datagrama reenviable, el puente envía al host:puerto especificado un paquete UDP que contiene los siguientes datos:

```
$destination                       # See notes below for Datagram3 format
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
$datagram_payload
```
Los datagramas sin procesar reenviados se reenvían tal como están al host:puerto especificado sin un prefijo. El paquete UDP contiene los siguientes datos:

```
$datagram_payload
```
A partir de SAM 3.2, cuando se especifica HEADER=true en SESSION CREATE, el datagrama raw reenviado será precedido por una línea de encabezado de la siguiente manera:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
El $destination es la codificación base 64 del [Destination](/docs/specs/common-structures#type_Destination), que tiene 516 o más caracteres en base 64 (387 o más bytes en binario), dependiendo del tipo de firma.

#### Datagramas Anónimos (Raw) SAM

Aprovechando al máximo el ancho de banda de I2P, SAM permite a los clientes enviar y recibir datagramas anónimos, dejando la información de autenticación y respuesta en manos del propio cliente. Estos datagramas no son confiables ni están ordenados, y pueden tener hasta 32768 bytes.

El tamaño mínimo es 1. Para una mejor confiabilidad de entrega, el tamaño máximo recomendado es de aproximadamente 11 KB.

Después de establecer una sesión SAM con STYLE=RAW, el cliente puede enviar datagramas anónimos a través del puente SAM exactamente de la misma manera que [enviando datagramas con respuesta](#sending-repliable-or-raw-datagrams).

Ambas formas de recibir datagramas también están disponibles para datagramas anónimos.

Los datagramas recibidos son escritos por SAM en el socket desde el cual se abrió la sesión de datagramas, si no se especifica un PORT de reenvío en el comando SESSION CREATE. Esta es la forma compatible con v1/v2 de recibir datagramas.

```
<- RAW RECEIVED
          SIZE=$numBytes
          FROM_PORT=nnn                      # SAM 3.2 or higher only
          TO_PORT=nnn                        # SAM 3.2 or higher only
          PROTOCOL=nnn                       # SAM 3.2 or higher only
          \n
      [$numBytes of data]
```
Cuando los datagramas anónimos deben ser reenviados a algún host:puerto, el puente envía al host:puerto especificado un mensaje que contiene los siguientes datos:

```
$datagram_payload
```
A partir de SAM 3.2, cuando se especifica HEADER=true en SESSION CREATE, el datagrama sin procesar reenviado será precedido por una línea de encabezado como sigue:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
Para un método alternativo de envío de datagramas anónimos, consulta [RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### Datagrama 2/3

Datagram 2/3 son nuevos formatos especificados a principios de 2025. Actualmente no existen implementaciones conocidas. Consulte la documentación de implementación para conocer el estado actual. Vea [la especificación](/docs/specs/datagrams) para más información.

No hay planes actuales para incrementar la versión de SAM para indicar soporte de Datagram 2/3. Esto puede ser problemático ya que las implementaciones pueden querer soportar Datagram 2/3 pero no las características de SAM v3.3. Cualquier cambio de versión está por determinar.

Tanto Datagram2 como Datagram3 admiten respuesta. Solo Datagram2 está autenticado.

Datagram2 es idéntico a los datagramas respondibles desde la perspectiva de SAM. Ambos están autenticados. Solo el formato I2CP y la firma son diferentes, pero esto no es visible para los clientes SAM. Datagram2 también admite firmas sin conexión, por lo que puede ser usado por destinos firmados sin conexión.

La intención es que Datagram2 reemplace los datagramas Repliable para nuevas aplicaciones que no requieren compatibilidad hacia atrás. Datagram2 proporciona protección contra replay que no está presente en los datagramas Repliable. Si se requiere compatibilidad hacia atrás, una aplicación puede soportar tanto Datagram2 como Repliable en la misma sesión con sesiones SAM 3.3 PRIMARY.

Datagram3 es respondible pero no autenticado. El campo 'from' en el formato I2CP es un hash, no un destino. El $destination tal como se envía desde el servidor SAM al cliente será un hash base64 de 44 bytes. Para convertirlo a un destino completo para responder, decodifícalo en base64 a 32 bytes binarios, luego codifícalo en base32 a 52 caracteres y añade ".b32.i2p" para una NAMING LOOKUP. Como es habitual, los clientes deben mantener su propia caché para evitar NAMING LOOKUPs repetidas.

Los diseñadores de aplicaciones deben usar extrema precaución y considerar las implicaciones de seguridad de los datagramas no autenticados.

#### Consideraciones de MTU de Datagramas V3

Los datagramas I2P pueden ser más grandes que el MTU típico de internet de 1500. Los datagramas enviados localmente y los datagramas reenviables que se reenvían con el prefijo de destino base64 de 516+ bytes probablemente excedan ese MTU. Sin embargo, los MTU localhost en sistemas Linux son típicamente mucho más grandes, por ejemplo 65536. Los MTU localhost variarán según el sistema operativo. Los datagramas I2P nunca serán más grandes que 65536. El tamaño del datagrama depende del protocolo de aplicación.

Si el cliente SAM es local al servidor SAM y el sistema soporta una MTU más grande, entonces los datagramas no se fragmentarán localmente. Sin embargo, si el cliente SAM es remoto, entonces los datagramas IPv4 se fragmentarían y los datagramas IPv6 fallarían (IPv6 no soporta fragmentación UDP).

Los desarrolladores de bibliotecas de cliente y aplicaciones deben estar al tanto de estos problemas y documentar recomendaciones para evitar la fragmentación y prevenir la pérdida de paquetes, especialmente en conexiones remotas cliente-servidor SAM.

#### DATAGRAM SEND, RAW SEND (Manejo de Datagramas Compatible con V1/V2)

En SAMv3, la forma preferida de enviar datagramas es a través del socket de datagramas en el puerto 7655 como se documenta arriba. Sin embargo, los datagramas que admiten respuesta pueden enviarse directamente a través del socket puente SAM usando el comando DATAGRAM SEND, como se documenta en [SAM V1](/docs/api/sam) y [SAM V2](/docs/api/samv2).

A partir del lanzamiento 0.9.14 (versión 3.1), los datagramas anónimos pueden enviarse directamente a través del socket del puente SAM usando el comando RAW SEND, como se documenta en [SAM V1](/docs/api/sam) y [SAM V2](/docs/api/samv2).

A partir de la versión 0.9.24 (versión 3.2), DATAGRAM SEND y RAW SEND pueden incluir los parámetros FROM_PORT=nnnn y/o TO_PORT=nnnn para anular los puertos predeterminados. A partir de la versión 0.9.24 (versión 3.2), RAW SEND puede incluir el parámetro PROTOCOL=nnn para anular el protocolo predeterminado.

Estos comandos *no* admiten el parámetro ID. Los datagramas se envían a la sesión de estilo DATAGRAM o RAW creada más recientemente, según corresponda. El soporte para el parámetro ID puede añadirse en una versión futura.

Los formatos DATAGRAM2 y DATAGRAM3 *no* son compatibles de la manera V1/V2.

### Sesiones SAM PRIMARY (V3.3 y superior)

*La versión 3.3 fue introducida en la versión 0.9.25 de I2P.*

*En una versión anterior de esta especificación, las sesiones PRIMARY se conocían como sesiones MASTER. Tanto en `i2pd` como en `I2P+`, todavía se conocen únicamente como sesiones MASTER.*

SAM v3.3 añade soporte para ejecutar streaming, datagramas y subsesiones raw en la misma sesión primaria, y para ejecutar múltiples subsesiones del mismo estilo. Todo el tráfico de las subsesiones utiliza un único destino, o conjunto de tunnels. El enrutamiento del tráfico desde I2P se basa en las opciones de puerto y protocolo de las subsesiones.

Para crear subsesiones multiplexadas, debe crear una sesión principal y luego agregar subsesiones a la sesión principal. Cada subsesión debe tener un id único y un protocolo de escucha y puerto únicos. Las subsesiones también pueden eliminarse de la sesión principal.

Con una sesión PRIMARY y una combinación de subsesiones, un cliente SAM puede soportar múltiples aplicaciones, o una sola aplicación sofisticada que utilice una variedad de protocolos, en un único conjunto de tunnels. Por ejemplo, un cliente bittorrent podría configurar una subsesión de streaming para conexiones peer-to-peer, junto con subsesiones de datagram y raw para comunicación DHT.

#### Creando una Sesión PRIMARY

```
->  SESSION CREATE
          STYLE=PRIMARY                        # prior to 0.9.47, use STYLE=MASTER
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP and streaming options
```
El puente SAM responderá con éxito o falla como en [la respuesta a un SESSION CREATE estándar](#session-creation-response).

No establezca las opciones PORT, HOST, FROM_PORT, TO_PORT, PROTOCOL, LISTEN_PORT, LISTEN_PROTOCOL o HEADER en una sesión primaria. No puede enviar ningún dato en un ID de sesión PRIMARY o en el socket de control. Todos los comandos como STREAM CONNECT, DATAGRAM SEND, etc. deben usar el ID de subsesión en un socket separado.

La sesión PRIMARY se conecta al router y construye tunnels. Cuando el puente SAM responde, los tunnels han sido construidos y la sesión está lista para que se agreguen subsesiones. Todas las opciones de [I2CP](/docs/protocol/i2cp) relacionadas con parámetros de tunnel como longitud, cantidad y apodo deben proporcionarse en el SESSION CREATE de la primaria.

Todos los comandos de utilidad son compatibles con una sesión primaria.

Cuando la sesión principal se cierra, todas las subsesiones también se cierran.

NOTA: Antes de la versión 0.9.47, usa STYLE=MASTER. STYLE=PRIMARY es compatible desde la versión 0.9.47. MASTER aún es compatible por retrocompatibilidad.

#### Creando una Subsesión

Usando el mismo socket de control en el que se creó la sesión PRIMARY:

```
->  SESSION ADD
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See above for DATAGRAM2/3
          ID=$nickname                         # must be unique
          [PORT=$port]                         # Required for DATAGRAM* and RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # For outbound traffic, default 0
          [TO_PORT=nnn]                        # For outbound traffic, default 0
          [PROTOCOL=nnn]                       # For outbound traffic for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [LISTEN_PORT=nnn]                    # For inbound traffic, default is the FROM_PORT value.
                                               # For STYLE=STREAM, only the FROM_PORT value or 0 is allowed.
          [LISTEN_PROTOCOL=nnn]                # For inbound traffic for STYLE=RAW only.
                                               # Default is the PROTOCOL value; 6 (streaming) is disallowed
          [HEADER={true,false}]                # For STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
El bridge SAM responderá con éxito o fallo como en [la respuesta a un SESSION CREATE estándar](#session-creation-response). Como los tunnels ya fueron construidos en el SESSION CREATE primario, el bridge SAM debería responder inmediatamente.

No configure la opción DESTINATION en un SESSION ADD. La subsesión utilizará el destino especificado en la sesión principal. Todas las subsesiones deben agregarse en el socket de control, es decir, la misma conexión en la que creó la sesión principal.

Múltiples subsesiones deben tener opciones lo suficientemente únicas para que los datos entrantes puedan ser enrutados correctamente. En particular, múltiples sesiones del mismo estilo deben tener diferentes opciones LISTEN_PORT (y/o LISTEN_PROTOCOL, solo para RAW). Un SESSION ADD con puerto de escucha y protocolo que duplique una subsesión existente resultará en un error.

El LISTEN_PORT es el puerto I2P local, es decir, el puerto de recepción (TO) para datos entrantes. Si no se especifica el LISTEN_PORT, se utilizará el valor FROM_PORT. Si no se especifican ni LISTEN_PORT ni FROM_PORT, el enrutamiento entrante se basará únicamente en STYLE y PROTOCOL. Para LISTEN_PORT y LISTEN_PROTOCOL, 0 significa cualquier valor, es decir, un comodín. Si tanto LISTEN_PORT como LISTEN_PROTOCOL son 0, esta subsesión será la predeterminada para el tráfico entrante que no se enrute a otra subsesión. El tráfico de streaming entrante (protocolo 6) nunca se enrutará a una subsesión RAW, incluso si su LISTEN_PROTOCOL es 0. Una subsesión RAW no puede establecer un LISTEN_PROTOCOL de 6. Si no hay una subsesión predeterminada o que coincida con el protocolo y puerto del tráfico entrante, esos datos se descartarán.

Usa el ID de subsesión, no el ID de sesión principal, para enviar y recibir datos. Todos los comandos como STREAM CONNECT, DATAGRAM SEND, etc. deben usar el ID de subsesión.

Todos los comandos de utilidad están soportados en una sesión principal o subsesión. El envío/recepción de datagramas/datos en bruto v1/v2 no están soportados en una sesión principal o en subsesiones.

#### Detener una Subsesión

Usando el mismo socket de control en el que se creó la sesión PRIMARY:

```
->  SESSION REMOVE
          ID=$nickname
```
Esto elimina una subsesión de la sesión principal. No establezca ninguna otra opción en un SESSION REMOVE. Las subsesiones deben eliminarse en el socket de control, es decir, la misma conexión en la que creó la sesión principal. Después de que se elimine una subsesión, se cierra y no puede usarse para enviar o recibir datos.

El puente SAM responderá con éxito o fallo como en [la respuesta a un SESSION CREATE estándar](#session-creation-response).

### Comandos de Utilidad SAM

Algunos comandos de utilidad requieren una sesión preexistente y otros no. Ver detalles a continuación.

#### Búsqueda de Nombre de Host

El siguiente mensaje puede ser utilizado por el cliente para consultar al puente SAM para la resolución de nombres:

```
NAMING LOOKUP
       NAME=$name
       [OPTIONS=true]     # Default false, as of router API 0.9.66
```
que es respondido por

```
NAMING REPLY
       RESULT=$result
       NAME=$name
       [VALUE=$destination]
       [MESSAGE="$message"]
       [OPTION:optionkey="$optionvalue"]   # As of router API 0.9.66
```
El valor RESULT puede ser uno de:

```
OK
INVALID_KEY
KEY_NOT_FOUND
```
Si NAME=ME, entonces la respuesta contendrá el destino utilizado por la sesión actual (útil si estás usando uno TRANSIENT). Si $result no es OK, MESSAGE puede transmitir un mensaje descriptivo, como "bad format", etc. INVALID_KEY implica que algo está mal con $name en la solicitud, posiblemente caracteres inválidos.

El $destination es la base 64 del [Destination](/docs/specs/common-structures#type_Destination), que son 516 o más caracteres en base 64 (387 o más bytes en binario), dependiendo del tipo de firma.

NAMING LOOKUP no requiere que se haya creado una sesión primero. Sin embargo, en algunas implementaciones, una búsqueda .b32.i2p que no esté en caché y requiera una consulta de red puede fallar, ya que no hay túneles de cliente disponibles para la búsqueda.

#### Opciones de Búsqueda de Nombres

NAMING LOOKUP se ha extendido a partir de la API del router 0.9.66 para admitir búsquedas de servicios. El soporte puede variar según la implementación. Consulte la propuesta 167 para información adicional.

NAMING LOOKUP NAME=example.i2p OPTIONS=true solicita el mapeo de opciones en la respuesta. NAME puede ser un destino base64 completo cuando OPTIONS=true.

Si la búsqueda de destino fue exitosa y había opciones presentes en el leaseSet, entonces en la respuesta, después del destino, habrá una o más opciones en la forma de OPTION:clave=valor. Cada opción tendrá un prefijo OPTION: separado. Todas las opciones del leaseSet serán incluidas, no solo las opciones de registro de servicio. Por ejemplo, pueden estar presentes opciones para parámetros definidos en el futuro. Ejemplo:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Las claves que contengan '=', y las claves o valores que contengan un salto de línea, se consideran inválidas y el par clave/valor será eliminado de la respuesta. Si no se encuentran opciones en el leaseSet, o si el leaseSet era versión 1, entonces la respuesta no incluirá ninguna opción. Si OPTIONS=true estaba en la búsqueda, y el leaseSet no se encuentra, se devolverá un nuevo valor de resultado LEASESET_NOT_FOUND.

#### Generación de Claves de Destino

Las claves base64 públicas y privadas se pueden generar usando el siguiente mensaje:

```
->  DEST GENERATE
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, default DSA_SHA1
```
que es respondido por

```
DEST REPLY
     PUB=$destination
     PRIV=$privkey
```
A partir de la versión 3.1 (I2P 0.9.14), se admite un parámetro opcional SIGNATURE_TYPE. El valor de SIGNATURE_TYPE puede ser cualquier nombre (por ejemplo, ECDSA_SHA256_P256, sin distinción entre mayúsculas y minúsculas) o número (por ejemplo, 1) que sea compatible con [Key Certificates](/docs/specs/common-structures#type_Certificate). El valor predeterminado es DSA_SHA1, que NO es lo que deseas. Para la mayoría de aplicaciones, por favor especifica SIGNATURE_TYPE=7.

El $destination es la codificación base 64 del [Destination](/docs/specs/common-structures#type_Destination), que tiene 516 o más caracteres en base 64 (387 o más bytes en binario), dependiendo del tipo de firma.

El $privkey es el base 64 de la concatenación del [Destination](/docs/specs/common-structures#type_Destination) seguido de la [Private Key](/docs/specs/common-structures#type_PrivateKey) seguida de la [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), que tiene 884 o más caracteres en base 64 (663 o más bytes en binario), dependiendo del tipo de firma. El formato binario se especifica en Private Key File.

Notas sobre la Private Key binaria de 256 bytes: Este campo no se ha utilizado desde la versión 0.6 (2005). Las implementaciones SAM pueden enviar datos aleatorios o todos ceros en este campo; no te alarmes por una cadena de AAAA en base 64. La mayoría de aplicaciones simplemente almacenarán la cadena base 64 y la devolverán tal como está en el SESSION CREATE, o la decodificarán a binario para almacenamiento, luego la codificarán nuevamente para SESSION CREATE. Las aplicaciones pueden, sin embargo, decodificar el base 64, analizar el binario siguiendo la especificación PrivateKeyFile, descartar la porción de private key de 256 bytes, y luego reemplazarla con 256 bytes de datos aleatorios o todos ceros al re-codificarla para el SESSION CREATE. TODOS los demás campos en la especificación PrivateKeyFile deben preservarse. Esto ahorraría 256 bytes de almacenamiento del sistema de archivos pero probablemente no vale la pena el esfuerzo para la mayoría de aplicaciones. Ver propuesta 161 para información adicional y antecedentes.

DEST GENERATE no requiere que se haya creado una sesión primero.

DEST GENERATE no puede utilizarse para crear un destino con firmas offline.

#### PING/PONG (SAM 3.2 o superior)

Tanto el cliente como el servidor pueden enviar:

```
PING[ arbitrary text]
```
en el puerto de control, con la respuesta:

```
PONG[ arbitrary text from the ping]
```
para ser usado para el keepalive del socket de control. Cualquiera de los lados puede cerrar la sesión y el socket si no se recibe respuesta en un tiempo razonable, dependiendo de la implementación.

Si ocurre un timeout esperando un PONG del cliente, el bridge puede enviar:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
y luego desconectarse.

Si ocurre un timeout esperando un PONG del bridge, el cliente puede simplemente desconectarse.

PING/PONG no requieren que se haya creado una sesión primero.

#### QUIT/STOP/EXIT (SAM 3.2 o superior, características opcionales)

Los comandos QUIT, STOP y EXIT cerrarán la sesión y el socket. La implementación es opcional, para facilitar las pruebas a través de telnet. Si hay alguna respuesta antes de que se cierre el socket (por ejemplo, un mensaje SESSION STATUS) es específico de la implementación y está fuera del alcance de esta especificación.

QUIT/STOP/EXIT no requieren que se haya creado una sesión primero.

#### HELP (función opcional)

Los servidores pueden implementar un comando HELP. La implementación es opcional, para facilitar las pruebas a través de telnet. El formato de salida y la detección del final de la salida son específicos de la implementación y están fuera del alcance de esta especificación.

HELP no requiere que se haya creado una sesión primero.

#### Configuración de autorización (SAM 3.2 o superior, característica opcional)

Configuración de autorización usando el comando AUTH. Un servidor SAM puede implementar estos comandos para facilitar el almacenamiento persistente de credenciales. La configuración de autenticación distinta a estos comandos es específica de la implementación y está fuera del alcance de esta especificación.

- AUTH ENABLE habilita la autorización en conexiones posteriores
- AUTH DISABLE deshabilita la autorización en conexiones posteriores
- AUTH ADD USER="foo" PASSWORD="bar" añade un usuario/contraseña
- AUTH REMOVE USER="foo" elimina este usuario

Se recomiendan las comillas dobles para el usuario y la contraseña, pero no son obligatorias. Una comilla doble dentro de un usuario o contraseña debe escaparse con una barra invertida. En caso de fallo, el servidor responderá con un I2P_ERROR y un mensaje.

AUTH no requiere que se haya creado una sesión primero.

### Valores RESULT

Estos son los valores que puede llevar el campo RESULT, con su significado:

```
OK              Operation completed successfully
CANT_REACH_PEER The peer exists, but cannot be reached
DUPLICATED_DEST The specified Destination is already in use
I2P_ERROR       A generic I2P error (e.g. I2CP disconnection, etc.)
INVALID_KEY     The specified key is not valid (bad format, etc.)
KEY_NOT_FOUND   The naming system can't resolve the given name
PEER_NOT_FOUND  The peer cannot be found on the network
TIMEOUT         Timeout while waiting for an event (e.g. peer answer)
LEASESET_NOT_FOUND  See Name Lookup Options above. As of router API 0.9.66.
```
Diferentes implementaciones pueden no ser consistentes en cuál RESULT es devuelto en varios escenarios.

La mayoría de las respuestas con un RESULT, que no sean OK, también incluirán un MESSAGE con información adicional. El MESSAGE generalmente será útil para depurar problemas. Sin embargo, las cadenas MESSAGE dependen de la implementación, pueden o no ser traducidas por el servidor SAMv3 al idioma local actual, pueden contener información interna específica de la implementación como excepciones, y están sujetas a cambios sin previo aviso. Aunque los clientes SAMv3 pueden elegir exponer las cadenas MESSAGE a los usuarios, no deberían tomar decisiones programáticas basadas en esas cadenas, ya que eso sería frágil.

### Opciones de Tunnel, I2CP y Streaming

Estas opciones pueden pasarse como pares nombre=valor en la línea SAM SESSION CREATE.

Todas las sesiones pueden incluir [opciones de I2CP como longitudes y cantidades de túneles](/docs/protocol/i2cp#options). Las sesiones STREAM pueden incluir [opciones de la biblioteca Streaming](/docs/api/streaming#options).

Consulta esas referencias para los nombres de opciones y valores predeterminados. La documentación referenciada es para la implementación del router de Java. Los valores predeterminados están sujetos a cambios. Los nombres de opciones y valores distinguen entre mayúsculas y minúsculas. Otras implementaciones de router pueden no soportar todas las opciones y pueden tener diferentes valores predeterminados; consulta la documentación del router para más detalles.

### Notas de BASE 64

La codificación Base 64 debe usar el alfabeto Base 64 estándar de I2P "A-Z, a-z, 0-9, -, ~".

### Configuración SAM por Defecto

El puerto SAM predeterminado es 7656. SAM no está habilitado por defecto en el Java I2P Router; debe iniciarse manualmente o configurarse para iniciar automáticamente en la página de configuración de clientes en la consola del router, o en el archivo clients.config. El puerto UDP SAM predeterminado es 7655, escuchando en 127.0.0.1. Estos pueden cambiarse en el router Java agregando los argumentos sam.udp.port=nnnnn y/o sam.udp.host=w.x.y.z a la invocación, o en la línea SESSION.

La configuración en otros routers es específica de la implementación. Consulta [la guía de configuración de i2pd aquí](https://i2pd.readthedocs.io/en/latest/user-guide/configuration/).
