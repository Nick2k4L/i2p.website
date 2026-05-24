---
title: "Sinalizador I2CP para Troca de Túnel de Saída"
number: "171"
author: "onon, eyedeekay"
created: "2026-05-19"
lastupdated: "2026-05-23"
status: "Rascunho"
toc: true
---

## Visão Geral

As conexões de cliente de streaming podem ficar travadas quando os reconhecimentos de entrega são perdidos silenciosamente. O remetente retransmite até receber um reconhecimento ou até que a conexão seja encerrada, sem uma forma confiável de confirmar se os reconhecimentos estão chegando ao destino. Esta proposta adiciona um novo bit ao campo de flags do [SendMessageExpiresMessage](/docs/specs/i2cp/) para que um cliente possa instruir o roteador a selecionar um túnel de saída diferente para mensagens subsequentes ao mesmo destino. O protocolo de streaming usa esse bit para iniciar uma troca de túnel ao detectar uma conexão travada.

## Disparadores

Duas condições DEVEM levar o cliente a definir a flag na próxima mensagem de saída. Essas condições são medidas na camada de streaming.

**Lado do remetente**

Nenhum reconhecimento foi recebido dentro do período atual de tempo limite de retransmissão do cliente.

**Lado do receptor**

O receptor observou que o remoto está retransmitindo os mesmos dados mais de uma vez, indicando que seus reconhecimentos (acknowledgments) não estão alcançando o destino. O receptor DEVE definir essa flag em sua próxima mensagem de saída I2CP para que os reconhecimentos alcancem o remoto por um caminho diferente. O receptor DEVE aguardar até: (1) ter recebido um dado duplicado, (2) ter enviado pelo menos um reconhecimento, e (3) o remoto ter retransmitido novamente antes de definir a flag.

Para limitar ataques de correlação temporal, um cliente NÃO DEVE definir a flag mais de uma vez a cada janela de 10 segundos por conexão. O cliente TAMBÉM DEVE atrasar a definição da flag por um jitter extraído uniformemente do intervalo `[0, min(T/4, 2000ms)]`, onde T é o tempo limite atual de retransmissão do cliente em milissegundos, após detectar a condição de estagnação, para reduzir a precisão da correlação temporal.

## Especificação

O campo flags de [SendMessageExpiresMessage](/docs/specs/i2cp/) ocupa os 2 bytes superiores após o campo Date (redefinido a partir da versão 0.8.4) e é transmitido em ordem big-endian. O bit 15 está atualmente inutilizado; esta proposta o define.

Ordem dos bits: 15...0

| Bit | Nome | Descrição |
|-----|------|-------------|
| 15 | SWITCH_OUTBOUND_TUNNEL | Se 1, o roteador DEVE selecionar um túnel de saída diferente do seu pool para mensagens subsequentes a este destino. Se nenhum túnel alternativo estiver disponível, esta flag é silenciosamente ignorada. O roteador NÃO DEVE fechar ou desativar o túnel previamente usado apenas porque esta flag foi definida. |
Este sinalizador tem valor padrão 0. Roteadores que não o implementam DEVEM ignorá-lo sem erro.

## Notas de Implementação

Quando `SWITCH_OUTBOUND_TUNNEL` estiver definido, o roteador DEVE selecionar um túnel uniformemente ao acaso a partir do grupo de saída, excluindo:

- o túnel atualmente em uso para esta sessão, e
- o único túnel mais recentemente falhado no pool, se houver.

Todas as outras métricas de saúde de túnel, tempos de construção ou histórico de seleção NÃO DEVEM influenciar a escolha, pois a seleção ponderada poderia favorecer atacantes sybil. Se o grupo não contiver nenhum túnel elegível após essas exclusões, a flag é silenciosamente ignorada.

Esta opção não acarreta mensagens adicionais de túnel; alternar túneis pode alterar a latência aparente. O limite de taxa de 10 segundos por conexão (veja Disparadores) evita alternâncias excessivas.

## Considerações sobre Anonimato

As flags em [SendMessageExpiresMessage](/docs/specs/i2cp/) são transmitidas através do I2CP, que é uma interface local entre o cliente e seu próprio roteador. Elas não são visíveis para observadores da rede.

O risco à anonimidade é baseado no padrão de tráfego: um adversário com visibilidade em vários pontos finais de túnel pode observar *quando* o uso do túnel muda.

Alternar túneis de saída em resposta direta a uma interrupção no lado do cliente cria um padrão comportamental detectável. Existem dois vetores concretos de observação:

**Ataque Sybil nos primeiros saltos de túneis de saída**

O primeiro salto de cada túnel de saída vê todo o tráfego que entra nesse túnel a partir do roteador do remetente. Um adversário que controle o primeiro salto de mais de um túnel no conjunto do remetente observa o tráfego parando em um primeiro salto e começando em outro em proximidade temporal estreita, vinculando ambos os túneis ao mesmo remetente. Com um conjunto de N túneis, um adversário que controle K primeiros saltos tem uma probabilidade de K/N de observar qualquer evento de troca específico.

**Temporização de lacunas de tráfego**

Durante a interrupção, o cliente não está enviando novos dados, então o túnel de saída antigo fica inativo. Quando ocorre a troca, o tráfego retoma por um caminho diferente. Um adversário com uma posição privilegiada no roteador do remetente — como o provedor de rede do remetente ou o próprio nó do primeiro salto — pode observar o padrão de silêncio seguido de retomada. A duração da pausa também revela uma aproximação do valor atual de tempo limite de retransmissão do cliente.

Os clientes DEVEM cumprir os requisitos de limitação de taxa e jitter em Triggers.

## Referências

- [Especificação I2CP](/docs/specs/i2cp/)
