---
title: "Usando un git bundle para obtener el código fuente de I2P"
description: "Clonando repositorios grandes sobre I2P usando git bundles y BitTorrent"
slug: "git-bundle"
lastUpdated: "2020-09"
accurateFor: "0.9.47"
---

Clonar repositorios de software grandes a través de I2P puede ser difícil, y usar git a veces puede hacer esto más complicado. Afortunadamente, también puede a veces hacerlo más fácil. Git tiene un comando `git bundle` que se puede usar para convertir un repositorio git en un archivo del cual git puede luego clonar, obtener o importar desde una ubicación en tu disco local. Al combinar esta capacidad con descargas de bittorrent, podemos resolver nuestros problemas restantes con `git clone`.

---

## Antes de Comenzar

Si tienes la intención de generar un git bundle, **debes** poseer ya una copia completa del repositorio **git**, no del repositorio mtn. Puedes obtenerlo desde github o desde git.idk.i2p, pero un clon superficial (un clon hecho con --depth=1) *no funcionará*. Fallará silenciosamente, creando lo que parece un bundle, pero cuando trates de clonarlo fallará. Si solo estás recuperando un git bundle pre-generado, entonces esta sección no se aplica a ti.

---

## Descarga del código fuente de I2P vía Bittorrent

Alguien necesitará proporcionarte un archivo torrent o un enlace magnet correspondiente a un `git bundle` existente que ya hayan generado para ti. Un bundle reciente y correctamente generado del código fuente principal de i2p.i2p hasta el miércoles 18 de marzo de 2020, se puede encontrar dentro de I2P en mi pastebin paste.idk.i2p/f/4hq37i.

Una vez que tengas un bundle, necesitarás usar git para crear un repositorio de trabajo a partir de él. Si estás usando GNU/Linux e i2psnark, el git bundle debería estar ubicado en $HOME/.i2p/i2psnark o, como servicio en Debian, en /var/lib/i2p/i2p-config/i2psnark. Si estás usando BiglyBT en GNU/Linux, probablemente esté en "$HOME/BiglyBT Downloads/" en su lugar. Los ejemplos aquí asumen I2PSnark en GNU/Linux; si usas algo diferente, reemplaza la ruta al bundle con el directorio de descarga preferido por tu cliente y plataforma.

### Usando `git clone`

Clonar desde un git bundle es fácil, simplemente:

```
git clone $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
Si obtienes el siguiente error, intenta usar git init y git fetch manualmente en su lugar.

```
fatal: multiple updates for ref 'refs/remotes/origin/master' not allowed
```
### Usando `git init` y `git fetch`

Primero, crea un directorio i2p.i2p para convertirlo en un repositorio git.

```
mkdir i2p.i2p && cd i2p.i2p
```
A continuación, inicializa un repositorio git vacío para obtener los cambios de vuelta.

```
git init
```
Finalmente, obtén el repositorio desde el bundle.

```
git fetch $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
### Reemplaza el remoto bundle con el remoto upstream

Ahora que tienes un bundle, puedes mantenerte al día con los cambios configurando el remoto al repositorio fuente upstream.

```
git remote set-url origin git@127.0.0.1:I2P_Developers/i2p.i2p
```
---

## Generando un Bundle

Primero, sigue la [Guía de Git para Usuarios](/docs/applications/git/) hasta que tengas un clon exitosamente `--unshallow`ed del repositorio i2p.i2p. Si ya tienes un clon, asegúrate de ejecutar `git fetch --unshallow` antes de generar un paquete torrent.

Una vez que tengas eso, simplemente ejecuta el objetivo ant correspondiente:

```
ant git-bundle
```
y copia el paquete resultante en tu directorio de descargas de I2PSnark. Por ejemplo:

```
cp i2p.i2p.bundle* $HOME/.i2p/i2psnark/
```
En un minuto o dos, I2PSnark detectará el torrent. Haz clic en el botón "Start" para comenzar a compartir el torrent.
