---
title: "O Processo de Proposta do I2P"
number: "001"
author: "str4d"
created: "2016-04-10"
lastupdated: "2017-04-07"
status: "Meta"
thread: "http://zzz.i2p/topics/1980"
toc: true
---
## Visão Geral

Este documento descreve como alterar as especificações do I2P, como funcionam as propostas do I2P e a relação entre as propostas do I2P e as especificações.

Este documento é adaptado do processo de proposta do Tor, e grande parte do conteúdo abaixo foi originalmente autorado por Nick Mathewson.

Este é um documento informativo.

## Motivação

Anteriormente, nosso processo para atualizar as especificações do I2P era relativamente informal: fazíamos uma proposta no fórum de desenvolvimento e discutíamos as alterações, então alcançávamos um consenso e modificávamos a especificação com alterações de rascunho (não necessariamente nessa ordem), e finalmente implementávamos as alterações.

Isso apresentou alguns problemas.

Em primeiro lugar, mesmo em sua forma mais eficiente, o antigo processo muitas vezes deixava a especificação desatualizada em relação ao código. Os piores casos eram aqueles em que a implementação era adiada: a especificação e o código podiam permanecer desatualizados por várias versões.

Em segundo lugar, era difícil participar da discussão, pois não estava sempre claro quais partes da thread de discussão faziam parte da proposta, ou quais alterações na especificação haviam sido implementadas. Os fóruns de desenvolvimento também são acessíveis apenas dentro do I2P, o que significa que as propostas só podiam ser visualizadas por pessoas que usam o I2P.

Em terceiro lugar, era muito fácil esquecer algumas propostas porque elas eram enterradas várias páginas atrás na lista de threads do fórum.

## Como alterar as especificações agora

Primeiramente, alguém escreve um documento de proposta. Ele deve descrever a alteração que deve ser feita em detalhes e dar alguma ideia de como implementá-la. Uma vez que esteja suficientemente desenvolvido, torna-se uma proposta.

Como um RFC, cada proposta recebe um número. Ao contrário dos RFCs, as propostas podem mudar ao longo do tempo e manter o mesmo número, até que sejam finalmente aceitas ou rejeitadas. O histórico de cada proposta será armazenado no repositório do site do I2P.

Uma vez que uma proposta esteja no repositório, devemos discuti-la na thread correspondente e aprimorá-la até que tenhamos alcançado um consenso de que é uma boa ideia e que está detalhada o suficiente para ser implementada. Quando isso acontece, implementamos a proposta e a incorporamos às especificações. Portanto, as especificações permanecem como a documentação canônica para o protocolo do I2P: nenhuma proposta é jamais a documentação canônica para um recurso implementado.

(Este processo é bastante semelhante ao Python Enhancement Process, com a principal exceção de que as propostas do I2P são reintegradas às especificações após a implementação, enquanto os PEPs *se tornam* a nova especificação.)

### Alterações pequenas

Ainda é aceitável fazer alterações pequenas diretamente na especificação se o código pode ser escrito mais ou menos imediatamente, ou alterações cosméticas se nenhuma alteração de código for necessária. Este documento reflete a intenção atual dos desenvolvedores, não uma promessa permanente de sempre usar este processo no futuro: reservamos o direito de nos entusiasmar e implementar algo em uma sessão de hacking noturna impulsionada por cafeína ou M&M's.

## Como novas propostas são adicionadas

Para submeter uma proposta, poste-a no fórum de desenvolvimento ou entre com um ticket com a proposta anexada.

Uma vez que uma ideia tenha sido proposta, um rascunho formatado corretamente (veja abaixo) existe, e um consenso bruto dentro da comunidade de desenvolvimento ativa existe de que essa ideia merece consideração, os editores de propostas oficialmente adicionam a proposta.

Os atuais editores de propostas são zzz e str4d.

## O que deve estar em uma proposta

Toda proposta deve ter um cabeçalho contendo os seguintes campos:

```
:author:
:created:
:thread:
:lastupdated:
:status:
```

- O campo `author` deve conter os nomes dos autores desta proposta.
- O campo `thread` deve ser um link para a thread do fórum de desenvolvimento onde esta proposta foi originalmente postada, ou para uma nova thread criada para discutir esta proposta.
- O campo `lastupdated` deve ser inicialmente igual ao campo `created` e deve ser atualizado sempre que a proposta for alterada.

Estes campos devem ser definidos quando necessário:

```
:supercedes:
:supercededby:
:editor:
```

- O campo `supercedes` é uma lista separada por vírgulas de todas as propostas que esta proposta substitui. Essas propostas devem ser Rejeitadas e ter seu campo `supercededby` definido para o número desta proposta.
- O campo `editor` deve ser definido se alterações significativas forem feitas nesta proposta que não alterem substancialmente seu conteúdo. Se o conteúdo estiver sendo substancialmente alterado, um autor adicional deve ser adicionado, ou uma nova proposta criada que substitua esta.

Estes campos são opcionais, mas recomendados:

```
:target:
:implementedin:
```

- O campo `target` deve descrever qual versão a proposta espera ser implementada (se estiver Aberta ou Aceita).
- O campo `implementedin` deve descrever qual versão a proposta foi implementada (se estiver Concluída ou Fechada).

O corpo da proposta deve começar com uma seção Visão Geral que explique sobre o que a proposta trata, o que ela faz e sobre qual estado ela está.

Após a Visão Geral, a proposta se torna mais livre. Dependendo de seu comprimento e complexidade, a proposta pode ser dividida em seções apropriadas, ou seguir um formato discursivo curto. Toda proposta deve conter pelo menos as seguintes informações antes de ser Aceita, embora as informações não precisem estar em seções com esses nomes.

**Motivação**
: Qual é o problema que a proposta está tentando resolver? Por que este problema é importante? Se várias abordagens forem possíveis, por que escolher esta?

**Design**
: Uma visão geral de alto nível das novas ou modificadas funcionalidades, de como as novas ou modificadas funcionalidades funcionam, de como elas interagem entre si e de como elas interagem com o restante do I2P. Este é o corpo principal da proposta. Algumas propostas começarão com apenas uma Motivação e um Design, e esperarão por uma especificação até que o Design pareça aproximadamente correto.

**Implicações de segurança**
: Quais efeitos as alterações propostas podem ter na anonimidade, quão bem compreendidos são esses efeitos e assim por diante.

**Especificação**
: Uma descrição detalhada de o que precisa ser adicionado às especificações do I2P para implementar a proposta. Isso deve estar em detalhes suficientes para que os programadores independentes possam escrever implementações mutuamente compatíveis da proposta com base em suas especificações.

**Compatibilidade**
: As versões do I2P que seguem a proposta serão compatíveis com as versões que não a seguem? Se sim, como a compatibilidade será alcançada? Geralmente, tentamos não perder a compatibilidade se possível; não fizemos uma alteração de "flag day" desde março de 2008, e não queremos fazer outra.

**Implementação**
: Se a proposta for difícil de implementar na arquitetura atual do I2P, o documento pode conter alguma discussão sobre como fazer com que funcione. Patches reais devem ser colocados em branches públicos de monotone, ou carregados no Trac.

**Notas de desempenho e escalabilidade**
: Se a funcionalidade tiver um efeito no desempenho (em RAM, CPU, largura de banda) ou escalabilidade, deve haver alguma análise sobre quão significativo será esse efeito, para que possamos evitar regressões de desempenho realmente caras e evitar gastar tempo com ganhos insignificantes.

**Referências**
: Se a proposta se referir a documentos externos, esses devem ser listados.

## Status da proposta

**Aberta**
: Uma proposta em discussão.

**Aceita**
: A proposta está completa, e pretendemos implementá-la. Após este ponto, alterações substantivas na proposta devem ser evitadas e consideradas como um sinal de que o processo falhou em algum lugar.

**Concluída**
: A proposta foi aceita e implementada. Após este ponto, a proposta não deve ser alterada.

**Fechada**
: A proposta foi aceita, implementada e mesclada nos documentos de especificação principais. A proposta não deve ser alterada após este ponto.

**Rejeitada**
: Não vamos implementar a funcionalidade como descrita aqui, embora possamos fazer alguma outra versão. Veja os comentários no documento para detalhes. A proposta não deve ser alterada após este ponto; para apresentar alguma outra versão da ideia, escreva uma nova proposta.

**Rascunho**
: Esta não é uma proposta completa ainda; há peças definitivamente faltantes. Por favor, não adicione novas propostas com este status; coloque-as no diretório "ideias" em vez disso.

**Precisa-revisão**
: A ideia para a proposta é boa, mas a proposta como está tem problemas sérios que a impedem de ser aceita. Veja os comentários no documento para detalhes.

**Morta**
: A proposta não foi tocada por um longo tempo, e não parece que alguém vai completá-la em breve. Ela pode se tornar "Aberta" novamente se obter um novo proponente.

**Precisa-pesquisa**
: Existem problemas de pesquisa que precisam ser resolvidos antes que fique claro se a proposta é uma boa ideia.

**Meta**
: Este não é uma proposta, mas um documento sobre propostas.

**Reserva**
: Esta proposta não é algo que estamos planejando implementar atualmente, mas podemos querer ressuscitá-la algum dia se decidirmos fazer algo semelhante ao que ela propõe.

**Informativa**
: Esta proposta é a última palavra sobre o que ela está fazendo. Ela não se tornará uma especificação a menos que alguém copie e cole ela em uma nova especificação para um novo subsistema.

Os editores mantêm o status correto das propostas, com base em consenso bruto e seu próprio discernimento.

## Numeração da proposta

Números 000-099 são reservados para propostas especiais e meta-propostas. 100 e acima são usados para propostas reais. Números não são reciclados.

## Referências

* [DEV-FORUM-PROPOSAL](http://zzz.i2p/topics/new?forum_id=7-big-topics-ideas-proposals-and-discussion)
* [TORSPEC-PROCESS](https://gitweb.torproject.org/torspec.git/tree/proposals/001-process.txt)
* [TRAC-PROPOSAL](http://trac.i2p2.i2p/newticket?summary=New%20proposal:%20&type=enhancement&milestone=n/a&component=www/i2p&keywords=review-needed)
