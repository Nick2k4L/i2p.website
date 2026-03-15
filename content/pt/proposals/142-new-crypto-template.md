---
title: "Novo Modelo de Proposta de Criptografia"
aliases:
  - "/pt/proposals/142-ecies-template"
  - "/pt/proposals/142-ecies-template/"
number: "142"
author: "zzz"
created: "2018-01-11"
lastupdated: "2018-01-20"
status: "Meta"
thread: "http://zzz.i2p/topics/2499"
toc: true
---
## Visão Geral

Este documento descreve questões importantes a serem consideradas ao propor
um substituto ou acréscimo à nossa criptografia assimétrica ElGamal.

Este é um documento informativo.


## Motivação

ElGamal é antigo e lento, e existem alternativas melhores.
No entanto, há várias questões que devem ser resolvidas antes que possamos adicionar ou mudar para qualquer novo algoritmo.
Este documento destaca essas questões não resolvidas.



## Pesquisa de Fundo

Qualquer pessoa que proponha nova criptografia deve primeiro estar familiarizada com os seguintes documentos:

- [Proposta 111 NTCP2](/proposals/111-ntcp-2/)
- [Proposta 123 LS2](/proposals/123-new-netdb-entries/)
- [Proposta 136 tipos de assinatura experimentais](/proposals/136-experimental-sigtypes/)
- [Proposta 137 tipos de assinatura opcionais](/proposals/137-optional-sigtypes/)
- Tópicos de discussão aqui para cada uma das propostas acima, vinculados internamente
- [Prioridades de proposta de 2018](http://zzz.i2p/topics/2494)
- [Proposta ECIES](http://zzz.i2p/topics/2418)
- [Visão geral de nova criptografia assimétrica](http://zzz.i2p/topics/1768)
- [Visão geral de criptografia de baixo nível](/docs/specs/common-structures/)


## Usos de Criptografia Assimétrica

Como revisão, usamos ElGamal para:

1) Mensagens de construção de túnel (a chave está em RouterIdentity)

2) Criptografia entre roteadores de netdb e outras mensagens I2NP (A chave está em RouterIdentity)

3) Cliente para cliente ElGamal+AES/SessionTag (a chave está em LeaseSet, a chave de Destino não é usada)

4) DH efêmero para NTCP e SSU


## Projeto

Qualquer proposta para substituir ElGamal por outra coisa deve fornecer os seguintes detalhes.



## Especificação

Qualquer proposta para nova criptografia assimétrica deve especificar completamente as seguintes coisas.



### 1. Geral

Responda às seguintes perguntas na sua proposta. Observe que isso pode precisar ser uma proposta separada das especificações no item 2) abaixo, pois pode entrar em conflito com as propostas existentes 111, 123, 136, 137 ou outras.

- Para quais dos casos acima de 1 a 4 você propõe usar a nova criptografia?
- Se para 1) ou 2) (roteador), onde a chave pública será colocada, na RouterIdentity ou nas propriedades do RouterInfo? Você pretende usar o tipo de criptografia no certificado da chave? Especifique completamente. Justifique sua decisão em qualquer caso.
- Se para 3) (cliente), você pretende armazenar a chave pública no destino e usar o tipo de criptografia no certificado da chave (como na proposta ECIES), ou armazená-la no LS2 (como na proposta 123), ou algo diferente? Especifique completamente e justifique sua decisão.
- Para todos os usos, como o suporte será anunciado? Se para 3), vai para o LS2, ou para outro lugar? Se para 1) e 2), é semelhante às propostas 136 e/ou 137? Especifique completamente e justifique suas decisões. Provavelmente será necessária uma proposta separada para isso.
- Especifique completamente como e por que isso é compatível com versões anteriores, e especifique totalmente um plano de migração.
- Quais propostas não implementadas são pré-requisitos para a sua proposta?


### 2. Tipo específico de criptografia

Responda às seguintes perguntas na sua proposta:

- Informações gerais de criptografia, curvas/parâmetros específicos, justifique completamente sua escolha. Forneça links para especificações e outras informações.
- Resultados de testes de velocidade comparados ao ElG e outras alternativas, se aplicável. Inclua criptografia, descriptografia e geração de chaves.
- Disponibilidade de bibliotecas em C++ e Java (tanto OpenJDK, BouncyCastle, quanto de terceiros)
  Para bibliotecas de terceiros ou não-Java, forneça links e licenças
- Número(s) proposto(s) do tipo de criptografia (na faixa experimental ou não)




## Notas
