---
title: "RI e Preenchimento de Destino"
number: "161"
author: "zzz"
created: "2022-09-28"
lastupdated: "2023-01-02"
status: "Open"
thread: "http://zzz.i2p/topics/3279"
target: "0.9.57"
toc: true
---
## Status

Implementado na versão 0.9.57.
Mantendo esta proposta aberta para que possamos aprimorar e discutir as ideias na seção "Planejamento Futuro".


## Visão Geral


### Resumo

A chave pública ElGamal em Destinos não tem sido usada desde a versão 0.6 (2005).
Embora nossas especificações digam que ela é inutilizada, elas NÃO dizem que as implementações podem evitar
gerar um par de chaves ElGamal e simplesmente preencher o campo com dados aleatórios.

Propomos alterar as especificações para afirmar que
o campo é ignorado e que as implementações PODEM preenchê-lo com dados aleatórios.
Essa mudança é compatível com versões anteriores. Não há nenhuma implementação conhecida que valide
a chave pública ElGamal.

Além disso, esta proposta oferece orientações aos implementadores sobre como gerar os
dados aleatórios para o preenchimento (padding) do Destino e da Identidade do Roteador, de modo que sejam compactáveis, ainda que
seguros, e sem que suas representações em Base 64 pareçam corrompidas ou inseguras.
Isso fornece a maior parte dos benefícios da remoção dos campos de preenchimento, sem quaisquer
mudanças disruptivas no protocolo.
Destinos compactáveis reduzem o tamanho do SYN de streaming e de datagramas com resposta;
Identidades de Roteador compactáveis reduzem as Mensagens de Armazenamento no Banco de Dados, mensagens SSU2 Session Confirmed
e arquivos su3 de reseed.

Finalmente, a proposta discute possibilidades de novos formatos para Destino e Identidade do Roteador
que eliminariam completamente o preenchimento. Também há uma breve discussão sobre criptografia pós-quântica
e como isso pode afetar o planejamento futuro.



### Objetivos

- Eliminar a exigência de gerar par de chaves ElGamal para Destinos
- Recomendar boas práticas para que Destinos e Identidades de Roteador sejam altamente compactáveis,
  mas sem exibir padrões óbvios nas representações em Base 64.
- Incentivar a adoção dessas boas práticas por todas as implementações, de modo que
  os campos não sejam distinguíveis
- Reduzir o tamanho do SYN de streaming
- Reduzir o tamanho do datagrama com resposta
- Reduzir o tamanho do bloco RI no SSU2
- Reduzir o tamanho e a frequência de fragmentação da mensagem SSU2 Session Confirmed
- Reduzir o tamanho da Mensagem de Armazenamento no Banco de Dados (com RI)
- Reduzir o tamanho do arquivo de reseed
- Manter compatibilidade em todos os protocolos e APIs
- Atualizar especificações
- Discutir alternativas para novos formatos de Destino e Identidade do Roteador

Ao eliminar a exigência de gerar chaves ElGamal, as implementações poderão
remover completamente o código ElGamal, sujeito a considerações de compatibilidade com versões anteriores
em outros protocolos.



## Projeto

Estritamente falando, apenas a chave pública de assinatura de 32 bytes (tanto em Destinos quanto em Identidades de Roteador)
e a chave pública de criptografia de 32 bytes (apenas em Identidades de Roteador) é um número aleatório
que fornece toda a entropia necessária para que os hashes SHA-256 dessas estruturas
sejam criptograficamente fortes e distribuídos aleatoriamente no DHT do banco de dados da rede.

No entanto, por excesso de cautela, recomendamos que pelo menos 32 bytes de dados aleatórios
sejam usados no campo da chave pública ElGamal e no preenchimento. Além disso, se os campos fossem todos zeros,
os Destinos em Base 64 conteriam longas sequências de caracteres AAAA, o que poderia causar alarme
ou confusão aos usuários.

Para o tipo de assinatura Ed25519 e tipo de criptografia X25519:
Destinos conterão 11 cópias (352 bytes) dos dados aleatórios.
Identidades de Roteador conterão 10 cópias (320 bytes) dos dados aleatórios.



### Economia Estimada

Destinos são incluídos em todo SYN de streaming
e em datagramas com resposta.
Informações de Roteador (contendo Identidades de Roteador) são incluídas em Mensagens de Armazenamento no Banco de Dados
e nas mensagens Session Confirmed do NTCP2 e SSU2.

O NTCP2 não comprime a Informação de Roteador.
RIs em Mensagens de Armazenamento no Banco de Dados e mensagens SSU2 Session Confirmed são compactados com gzip.
Informações de Roteador são compactadas com zip em arquivos SU3 de reseed.

Destinos em Mensagens de Armazenamento no Banco de Dados não são compactados.
Mensagens SYN de streaming são compactadas com gzip na camada I2CP.

Para o tipo de assinatura Ed25519 e tipo de criptografia X25519,
economia estimada:

| Tipo de Dado | Tamanho Total | Chaves e Cert | Preenchimento Não Compactado | Preenchimento Compactado | Tamanho | Economia |
|--------------|---------------|---------------|-------------------------------|---------------------------|--------|---------|
| Destino | 391 | 39 | 352 | 32 | 71 | 320 bytes (82%) |
| Identidade do Roteador | 391 | 71 | 320 | 32 | 103 | 288 bytes (74%) |
| Informação do Roteador | 1000 tip. | 71 | 320 | 32 | 722 tip. | 288 bytes (29%) |

Notas: Assume que o certificado de 7 bytes não é compactável, sem sobrecarga adicional do gzip.
Nenhum dos dois é verdade, mas os efeitos serão pequenos.
Ignora outras partes compactáveis da Informação do Roteador.



## Especificação

As alterações propostas às nossas especificações atuais estão documentadas abaixo.


### Estruturas Comuns
Alterar a especificação de estruturas comuns
para indicar que o campo de 256 bytes da chave pública do Destino é ignorado e pode
conter dados aleatórios.

Adicionar uma seção à especificação de estruturas comuns
recomendando boas práticas para o campo da chave pública do Destino e os
campos de preenchimento no Destino e na Identidade do Roteador, da seguinte forma:

Gerar 32 bytes de dados aleatórios usando um gerador criptográfico forte de números pseudo-aleatórios (PRNG)
e repetir esses 32 bytes conforme necessário para preencher o campo da chave pública (para Destinos)
e o campo de preenchimento (para Destinos e Identidades de Roteador).

### Arquivo de Chave Privada
O formato do arquivo de chave privada (eepPriv.dat) não é uma parte oficial de nossas especificações,
mas está documentado nos [javadocs do Java I2P](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html)
e outras implementações o suportam.
Isso permite a portabilidade de chaves privadas entre diferentes implementações.
Adicionar uma nota nesse javadoc indicando que a chave pública de criptografia pode ser preenchimento aleatório
e a chave privada de criptografia pode ser todos zeros ou dados aleatórios.

### SAM
Observar na especificação SAM que a chave privada de criptografia é inutilizada e pode ser ignorada.
Qualquer dado aleatório pode ser retornado pelo cliente.
A Ponte SAM pode enviar dados aleatórios na criação (com DEST GENERATE ou SESSION CREATE DESTINATION=TRANSIENT)
em vez de todos os zeros, para que a representação em Base 64 não contenha uma sequência de caracteres AAAA
e pareça corrompida.


### I2CP
Nenhuma alteração necessária no I2CP. A chave privada para a chave pública de criptografia no Destino
não é enviada ao roteador.


## Planejamento Futuro


### Mudanças no Protocolo

Ao custo de mudanças no protocolo e perda de compatibilidade com versões anteriores, poderíamos
alterar nossos protocolos e especificações para eliminar o campo de preenchimento no
Destino, Identidade do Roteador, ou ambos.

Essa proposta tem alguma semelhança com o formato de leaseset criptografado "b33",
contendo apenas um campo de chave e um campo de tipo.

Para manter alguma compatibilidade, certas camadas de protocolo poderiam "expandir" o campo de preenchimento
com todos os zeros para apresentá-lo a outras camadas de protocolo.

Para Destinos, também poderíamos remover o campo de tipo de criptografia no certificado da chave,
com uma economia de dois bytes.
Alternativamente, Destinos poderiam receber um novo tipo de criptografia no certificado da chave,
indicando uma chave pública nula (e preenchimento).

Se a conversão de compatibilidade entre os formatos antigos e novos não for incluída em alguma camada de protocolo,
as seguintes especificações, APIs, protocolos e aplicações seriam afetadas:

- Especificação de estruturas comuns
- I2NP
- I2CP
- NTCP2
- SSU2
- Ratchet
- Streaming
- SAM
- Bittorrent
- Reseeding
- Arquivo de Chave Privada
- API do núcleo e roteador Java
- API do i2pd
- Bibliotecas SAM de terceiros
- Ferramentas embutidas e de terceiros
- Vários plugins Java
- Interfaces de usuário
- Aplicações P2P, por exemplo, MuWire, bitcoin, monero
- hosts.txt, catálogo de endereços e assinaturas

Se a conversão for especificada em alguma camada, a lista seria reduzida.

Os custos e benefícios dessas mudanças ainda não são claros.

Propostas específicas a serem definidas:





### Chaves PQ

Chaves públicas de criptografia Pós-Quântica (PQ), para qualquer algoritmo previsto,
são maiores que 256 bytes. Isso eliminaria qualquer preenchimento e qualquer economia das mudanças propostas acima,
para Identidades de Roteador.

Em uma abordagem "híbrida" PQ, como a usada pelo SSL, as chaves PQ seriam apenas efêmeras,
e não apareceriam na Identidade do Roteador.

Chaves de assinatura PQ não são viáveis,
e Destinos não contêm chaves públicas de criptografia.
Chaves estáticas para o ratchet estão no Lease Set, não no Destino.
portanto podemos excluir Destinos da seguinte discussão.

Assim, PQ afeta apenas Informações de Roteador, e apenas para chaves estáticas PQ (não efêmeras), não para PQ híbrido.
Isso seria para um novo tipo de criptografia e afetaria NTCP2, SSU2 e
Mensagens de Pesquisa no Banco de Dados criptografadas e suas respostas.
O prazo estimado para o projeto, desenvolvimento e implantação disso seria ????????
Mas seria após o híbrido ou ratchet ????????????

Para mais discussão, veja [este tópico](http://zzz.i2p/topics/3294).




## Problemas

Pode ser desejável redefinir as chaves da rede a uma taxa lenta, para fornecer cobertura a novos roteadores.
"Redefinir chaves" poderia significar simplesmente alterar o preenchimento, não mudar realmente as chaves.

Não é possível redefinir chaves em Destinos existentes.

Identidades de Roteador com preenchimento no campo da chave pública devem ser identificadas com um tipo
de criptografia diferente no certificado da chave? Isso causaria problemas de compatibilidade.




## Migração

Nenhum problema de compatibilidade com versões anteriores ao substituir a chave ElGamal por preenchimento.

A redefinição de chaves, se implementada, seria semelhante à realizada
em três transições anteriores de identidade de roteador:
De assinaturas DSA-SHA1 para ECDSA, depois para
assinaturas EdDSA, depois para criptografia X25519.

Sujeito a problemas de compatibilidade com versões anteriores, e após desativar o SSU,
as implementações podem remover completamente o código ElGamal.
Aproximadamente 14% dos roteadores na rede usam o tipo de criptografia ElGamal, incluindo muitos floodfill.

Uma solicitação de mesclagem em rascunho para o Java I2P está em [git.idk.i2p](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66).


## Referências

* [Common](/docs/specs/common-structures/)
* [Datagram](/docs/api/datagrams/)
* [I2CP](/docs/specs/i2cp/)
* [I2NP](/docs/specs/i2np/)
* [MR](http://git.idk.i2p/i2p-hackers/i2p.i2p/-/merge_requests/66)
* [NTCP2](/docs/specs/ntcp2/)
* [PKF](http://idk.i2p/javadoc-i2p/net/i2p/data/PrivateKeyFile.html)
* [PQ](http://zzz.i2p/topics/3294)
* [SAM](/docs/api/samv3/)
* [SSU2](/docs/specs/ssu2/)
* [Streaming](/docs/specs/streaming/)
