---
title: "MTU em Streaming para Destinos ECIES"
number: "155"
author: "zzz"
created: "2020-05-06"
lastupdated: "2020-05-30"
status: "Closed"
thread: "http://zzz.i2p/topics/2886"
target: "0.9.47"
implementedin: "0.9.47"
toc: true
---
## Nota
Implantação e testes na rede em andamento.
Sujeito a revisões menores.


## Visão geral


### Resumo

O ECIES reduz o overhead da mensagem de sessão existente (ES) em cerca de 90 bytes.
Portanto, podemos aumentar o MTU em cerca de 90 bytes para conexões ECIES.
Veja a [especificação ECIES](/docs/specs/ecies/#overhead), [especificação de Streaming](/docs/specs/streaming/#flags-and-option-data-fields) e a [documentação da API de Streaming](/docs/api/streaming/).

Sem aumentar o MTU, em muitos casos as economias de overhead não são realmente "economizadas",
já que as mensagens serão preenchidas para usar duas mensagens de túnel completas de qualquer forma.

Esta proposta não exige nenhuma alteração nas especificações.
Ela é publicada como proposta apenas para facilitar a discussão e a construção de consenso
sobre o valor recomendado e sobre os detalhes de implementação.


### Objetivos

- Aumentar o MTU negociado
- Maximizar o uso de mensagens de túnel de 1 KB
- Não alterar o protocolo de streaming


## Projeto

Utilize a opção existente MAX_PACKET_SIZE_INCLUDED e a negociação de MTU.
O streaming continua a usar o mínimo entre o MTU enviado e o recebido.
O valor padrão permanece 1730 para todas as conexões, independentemente das chaves utilizadas.

Recomenda-se que as implementações incluam a opção MAX_PACKET_SIZE_INCLUDED em todos os pacotes SYN, em ambas as direções,
embora isso não seja obrigatório.

Se um destino for apenas ECIES, use o valor maior (como Alice ou Bob).
Se um destino for de dupla chave, o comportamento pode variar:

Se o cliente de dupla chave estiver fora do roteador (em um aplicativo externo),
ele pode não "saber" qual chave está sendo usada no destino remoto, e Alice pode solicitar
um valor maior no SYN, enquanto o dado máximo no SYN permanece 1730.

Se o cliente de dupla chave estiver dentro do roteador, a informação sobre qual chave
está sendo usada pode ou não estar disponível para o cliente.
O leaseset pode ainda não ter sido buscado, ou as interfaces da API interna
podem não disponibilizar facilmente essa informação ao cliente.
Se a informação estiver disponível, Alice pode usar o valor maior;
caso contrário, Alice deve usar o valor padrão de 1730 até que seja negociado.

Um cliente de dupla chave como Bob pode enviar o valor maior em resposta,
mesmo que nenhum valor ou um valor de 1730 tenha sido recebido de Alice;
no entanto, não há previsão para negociação ascendente no streaming,
portanto o MTU deve permanecer em 1730.


Conforme observado na [documentação da API de Streaming](/docs/api/streaming/),
os dados nos pacotes SYN enviados de Alice para Bob podem exceder o MTU de Bob.
Esta é uma fraqueza no protocolo de streaming.
Portanto, clientes de dupla chave devem limitar os dados nos pacotes SYN enviados
a 1730 bytes, enquanto enviam uma opção de MTU maior.
Uma vez que o MTU maior seja recebido de Bob, Alice poderá aumentar o payload máximo real enviado.


### Análise

Conforme descrito na [especificação ECIES](/docs/specs/ecies/#overhead), o overhead ElGamal para mensagens de sessão existente é
de 151 bytes, e o overhead do Ratchet é de 69 bytes.
Portanto, podemos aumentar o MTU para conexões ratchet em (151 - 69) = 82 bytes,
de 1730 para 1812.



## Especificação

Adicione as seguintes alterações e esclarecimentos à seção Seleção e Negociação de MTU da [documentação da API de Streaming](/docs/api/streaming/).
Nenhuma alteração na [especificação de Streaming](/docs/specs/streaming/).


O valor padrão da opção i2p.streaming.maxMessageSize permanece 1730 para todas as conexões, independentemente das chaves utilizadas.
Os clientes devem usar o mínimo entre o MTU enviado e recebido, como de costume.

Existem quatro constantes e variáveis relacionadas ao MTU:

- DEFAULT_MTU: 1730, inalterado, para todas as conexões
- i2cp.streaming.maxMessageSize: padrão 1730 ou 1812, pode ser alterado pela configuração
- ALICE_SYN_MAX_DATA: O tamanho máximo de dados que Alice pode incluir em um pacote SYN
- negotiated_mtu: O mínimo entre o MTU de Alice e de Bob, a ser usado como tamanho máximo de dados
  no SYN ACK de Bob para Alice, e em todos os pacotes subsequentes enviados em ambas as direções


Existem cinco casos a considerar:


### 1) Alice apenas ElGamal
Sem alteração, MTU de 1730 em todos os pacotes.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize padrão: 1730
- Alice pode enviar MAX_PACKET_SIZE_INCLUDED no SYN, não obrigatório a menos que != 1730


### 2) Alice apenas ECIES
MTU de 1812 em todos os pacotes.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize padrão: 1812
- Alice deve enviar MAX_PACKET_SIZE_INCLUDED no SYN


### 3) Alice de dupla chave e sabe que Bob é ElGamal
MTU de 1730 em todos os pacotes.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize padrão: 1812
- Alice pode enviar MAX_PACKET_SIZE_INCLUDED no SYN, não obrigatório a menos que != 1730


### 4) Alice de dupla chave e sabe que Bob é ECIES
MTU de 1812 em todos os pacotes.

- ALICE_SYN_MAX_DATA = 1812
- i2cp.streaming.maxMessageSize padrão: 1812
- Alice deve enviar MAX_PACKET_SIZE_INCLUDED no SYN


### 5) Alice de dupla chave e chave de Bob desconhecida
Enviar 1812 como MAX_PACKET_SIZE_INCLUDED no pacote SYN, mas limitar os dados do pacote SYN a 1730.

- ALICE_SYN_MAX_DATA = 1730
- i2cp.streaming.maxMessageSize padrão: 1812
- Alice deve enviar MAX_PACKET_SIZE_INCLUDED no SYN


### Para todos os casos

Alice e Bob calculam
negotiated_mtu, o mínimo entre o MTU de Alice e de Bob, a ser usado como tamanho máximo de dados
no SYN ACK de Bob para Alice, e em todos os pacotes subsequentes enviados em ambas as direções.




## Justificativa

Veja o [código-fonte Java do I2P](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220) para entender por que o valor atual é 1730.
Veja a [especificação ECIES](/docs/specs/ecies/#overhead) para entender por que o overhead do ECIES é 82 bytes menor que o do ElGamal.



## Notas de Implementação

Se o streaming estiver criando mensagens de tamanho ideal, é muito importante que
a camada ECIES-Ratchet não faça padding além desse tamanho.

O tamanho ideal da mensagem Garlic para caber em duas mensagens de túnel,
incluindo o cabeçalho I2NP da mensagem Garlic de 16 bytes, 4 bytes de comprimento da mensagem Garlic,
8 bytes da tag ES e 16 bytes do MAC, é de 1956 bytes.

Um algoritmo de preenchimento recomendado no ECIES é o seguinte:

- Se o comprimento total da mensagem Garlic for de 1954-1956 bytes,
  não adicione um bloco de preenchimento (sem espaço)
- Se o comprimento total da mensagem Garlic for de 1938-1953 bytes,
  adicione um bloco de preenchimento para preencher exatamente até 1956 bytes.
- Caso contrário, faça padding normalmente, por exemplo com uma quantidade aleatória de 0-15 bytes.

Estratégias semelhantes poderiam ser usadas nos tamanhos ideais de uma mensagem de túnel (964)
e três mensagens de túnel (2952), embora esses tamanhos devam ser raros na prática.



## Problemas

O valor 1812 é preliminar. Deve ser confirmado e possivelmente ajustado.




## Migração

Sem problemas de compatibilidade com versões anteriores.
Esta é uma opção existente e a negociação de MTU já faz parte da especificação.

Destinos ECIES mais antigos suportarão 1730.
Qualquer cliente que receber um valor maior responderá com 1730, e o extremo remoto
negociará para baixo, como de costume.


## Referências

* [CALCULATION](https://github.com/i2p/i2p.i2p/blob/master/apps/streaming/java/src/net/i2p/client/streaming/impl/ConnectionOptions.java#L220)
* [ECIES](/docs/specs/ecies/#overhead)
* [STREAMING-OPTIONS](/docs/api/streaming/)
* [STREAMING-SPEC](/docs/specs/streaming/#flags-and-option-data-fields)
