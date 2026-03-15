---
title: "Expiração de Introduzer"
number: "133"
author: "zzz"
created: "2017-02-05"
lastupdated: "2017-08-09"
status: "Fechado"
thread: "http://zzz.i2p/topics/2230"
target: "0.9.30"
implementedin: "0.9.30"
toc: true
---
## Visão Geral

Esta proposta trata da melhoria da taxa de sucesso para introduções.


## Motivação

Os introduzores expiram após um determinado tempo, mas essa informação não é publicada no Router Info. Atualmente, os roteadores precisam usar heurísticas para estimar quando um introduzor já não é válido.


## Projeto

Em um Endereço de Roteador SSU contendo introduzores, o publicador pode opcionalmente incluir tempos de expiração para cada introduzor.


## Especificação

```
iexp{X}={nnnnnnnnnn}

X :: O número do introduzor (0-2)

nnnnnnnnnn :: O tempo em segundos (não milissegundos) desde a época.
```

### Notas

* Cada expiração deve ser maior que a data de publicação do Router Info e menor que 6 horas após a data de publicação do Router Info.

* Os roteadores publicadores e os introduzores devem tentar manter o introduzor válido até a expiração, entretanto não há como garantir isso.

* Os roteadores não devem usar um introduzor publicado após sua expiração.

* As expirações dos introduzores estão no mapeamento do Endereço de Roteador. Elas não são o campo de expiração de 8 bytes (atualmente não utilizado) no Endereço de Roteador.

**Exemplo:** `iexp0=1486309470`


## Migração

Sem problemas. A implementação é opcional.  
A compatibilidade com versões anteriores é garantida, já que roteadores mais antigos ignorarão parâmetros desconhecidos.


## Referências

* [RouterAddress](/docs/specs/common-structures/#routeraddress)
* [RouterInfo](/docs/specs/common-structures/#routerinfo)
* [TRAC-TICKET](http://trac.i2p2.i2p/ticket/1352)
