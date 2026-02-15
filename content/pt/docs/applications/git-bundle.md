---
title: "Usando um git bundle para obter o código-fonte do I2P"
description: "Clonando repositórios grandes sobre I2P usando git bundles e BitTorrent"
slug: "git-bundle"
lastUpdated: "2020-09"
accurateFor: "0.9.47"
---

Clonar repositórios de software grandes através do I2P pode ser difícil, e usar git às vezes pode tornar isso mais complicado. Felizmente, também pode às vezes facilitar. O Git tem um comando `git bundle` que pode ser usado para transformar um repositório git em um arquivo do qual o git pode então clonar, buscar ou importar de um local no seu disco local. Ao combinar essa capacidade com downloads por bittorrent, podemos resolver nossos problemas restantes com `git clone`.

---

## Antes de Começar

Se você pretende gerar um bundle git, você **deve** já possuir uma cópia completa do repositório **git**, não do repositório mtn. Você pode obtê-lo do github ou do git.idk.i2p, mas um clone superficial (um clone feito com --depth=1) *não funcionará*. Ele falhará silenciosamente, criando o que parece ser um bundle, mas quando você tentar cloná-lo, falhará. Se você está apenas recuperando um bundle git pré-gerado, então esta seção não se aplica a você.

---

## Obtendo o Código Fonte do I2P via Bittorrent

Alguém precisará fornecer um arquivo torrent ou um link magnet correspondente a um `git bundle` existente que já foi gerado para você. Um bundle recente e corretamente gerado do código-fonte principal i2p.i2p de quarta-feira, 18 de março de 2020, pode ser encontrado dentro do I2P no meu pastebin paste.idk.i2p/f/4hq37i.

Uma vez que você tenha um bundle, precisará usar o git para criar um repositório de trabalho a partir dele. Se você estiver usando GNU/Linux e i2psnark, o git bundle deve estar localizado em $HOME/.i2p/i2psnark ou, como um serviço no Debian, em /var/lib/i2p/i2p-config/i2psnark. Se você estiver usando BiglyBT no GNU/Linux, provavelmente estará em "$HOME/BiglyBT Downloads/" em vez disso. Os exemplos aqui assumem I2PSnark no GNU/Linux, se você usar algo diferente, substitua o caminho para o bundle pelo diretório de download preferido pelo seu cliente e plataforma.

### Usando `git clone`

Clonar a partir de um git bundle é fácil, apenas:

```
git clone $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
Se você receber o seguinte erro, tente usar git init e git fetch manualmente.

```
fatal: multiple updates for ref 'refs/remotes/origin/master' not allowed
```
### Usando `git init` e `git fetch`

Primeiro, crie um diretório i2p.i2p para transformar em um repositório git.

```
mkdir i2p.i2p && cd i2p.i2p
```
Em seguida, inicialize um repositório git vazio para buscar as alterações de volta.

```
git init
```
Finalmente, busque o repositório do pacote.

```
git fetch $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
### Substitua o remote do bundle pelo remote upstream

Agora que você tem um bundle, pode acompanhar as mudanças configurando o remote para a fonte do repositório upstream.

```
git remote set-url origin git@127.0.0.1:I2P_Developers/i2p.i2p
```
---

## Gerando um Bundle

Primeiro, siga o [Guia Git para Usuários](/docs/applications/git/) até ter um clone com `--unshallow` bem-sucedido do repositório i2p.i2p. Se você já tem um clone, certifique-se de executar `git fetch --unshallow` antes de gerar um pacote torrent.

Uma vez que você tenha isso, simplesmente execute o target ant correspondente:

```
ant git-bundle
```
e copie o pacote resultante para o diretório de downloads do I2PSnark. Por exemplo:

```
cp i2p.i2p.bundle* $HOME/.i2p/i2psnark/
```
Em um ou dois minutos, o I2PSnark irá detectar o torrent. Clique no botão "Start" para começar a semear o torrent.
