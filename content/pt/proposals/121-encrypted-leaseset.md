---
title: "LeaseSet Criptografado"
number: "121"
author: "zzz"
created: "2016-01-11"
lastupdated: "2016-01-12"
status: "Rejeitado"
thread: "http://zzz.i2p/topics/2047"
supercededby: "123"
toc: true
---
## Visão Geral

Esta proposta é sobre redesenhar o mecanismo para criptografar os LeaseSets.


## Motivação

O LS criptografado atual é horrível e inseguro. Posso dizer isso, pois o desenhei e
implementei.

Motivos:

- Criptografado com AES CBC
- Uma única chave AES para todos
- Expirações de Lease ainda expostas
- Chave pública de criptografia ainda exposta


## Design

### Objetivos

- Tornar a coisa toda opaca
- Chaves para cada destinatário


### Estratégia

Faça como o GPG/OpenPGP faz. Criptografe assimetricamente uma chave simétrica para cada
destinatário. Os dados são decifrados com essa chave assimétrica. Veja, por exemplo, [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
SE podemos encontrar um algoritmo que seja pequeno e rápido.

O truque é encontrar uma criptografia assimétrica que seja pequena e rápida. O ElGamal com 514
bytes é um pouco doloroso aqui. Podemos fazer melhor.

Veja, por exemplo, http://security.stackexchange.com/questions/824...

Isso funciona para pequenos números de destinatários (ou na verdade, chaves; você ainda
pode distribuir chaves para várias pessoas se quiser).


## Especificação

- Destino
- Carimbo de data e hora publicado
- Expiração
- Flags
- Comprimento dos dados
- Dados criptografados
- Assinatura

Os dados criptografados podem ser prefixados com algum especificador de tipo de criptografia, ou não.


## Referências

* [RFC-4880-S5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
