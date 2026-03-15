---
title: "Registros de Serviço em LS2"
number: "167"
author: "zzz, orignal, eyedeekay"
created: "2024-06-22"
lastupdated: "2025-04-03"
status: "Fechado"
thread: "http://zzz.i2p/topics/3641"
target: "0.9.66"
toc: true
---
## Status
Aprovado na segunda revisão em 2025-04-01; as especificações foram atualizadas; ainda não implementado.


## Visão Geral

O I2P não possui um sistema DNS centralizado.  
No entanto, a agenda de endereços, juntamente com o sistema de nomes de host b32, permite  
que o roteador pesquise destinos completos e busque conjuntos de locação (lease sets), que contêm  
uma lista de gateways e chaves para que os clientes possam se conectar a esse destino.

Assim, os conjuntos de locação são semelhantes a um registro DNS. Mas atualmente não há nenhum mecanismo para  
descobrir se esse host suporta quaisquer serviços, seja nesse destino ou em outro diferente,  
de maneira semelhante aos [registros SRV do DNS](https://en.wikipedia.org/wiki/SRV_record) definidos na [RFC 2782](https://datatracker.ietf.org/doc/html/rfc2782).

A primeira aplicação disso pode ser e-mail ponto a ponto.  
Outras aplicações possíveis: DNS, GNS, servidores de chaves, autoridades de certificação, servidores de tempo,  
bittorrent, criptomoedas, outras aplicações ponto a ponto.


## Propostas Relacionadas e Alternativas

### Listas de Serviço

A [Proposta 123](/proposals/123-new-netdb-entries/) do LS2 definiu 'registros de serviço' que indicavam um destino  
participando de um serviço global. Os floodfills agregariam esses registros  
em 'listas de serviço' globais.  
Isso nunca foi implementado devido à complexidade, falta de autenticação,  
preocupações com segurança e spam.

Esta proposta é diferente, pois fornece pesquisa de serviço para um destino específico,  
não um conjunto global de destinos para algum serviço global.

### GNS

O GNS propõe que todos executem seu próprio servidor DNS.  
Esta proposta é complementar, pois poderíamos usar registros de serviço para especificar  
que GNS (ou DNS) é suportado, com um nome de serviço padrão "domain" na porta 53.

### Dot well-known

Foi [proposto](http://i2pforum.i2p/viewtopic.php?p=3102) que serviços sejam pesquisados via requisição HTTP para  
/.well-known/i2pmail.key. Isso exige que todo serviço tenha um site relacionado para hospedar a chave. A maioria dos usuários não executa sites.

Uma solução alternativa é presumir que um serviço para um endereço b32 está realmente  
em execução nesse endereço b32. Assim, procurar o serviço para example.i2p exigiria  
a busca HTTP de http://example.i2p/.well-known/i2pmail.key, mas  
um serviço para aaa...aaa.b32.i2p não exigiria essa consulta, podendo conectar-se diretamente.

Mas há uma ambiguidade, pois example.i2p também pode ser endereçado pelo seu b32.

### Registros MX

Registros SRV são simplesmente uma versão genérica de registros MX para qualquer serviço.  
"_smtp._tcp" é o registro "MX".  
Não há necessidade de registros MX se tivermos registros SRV, e registros MX  
sozinhos não fornecem um registro genérico para qualquer serviço.


## Projeto

Registros de serviço são colocados na seção de opções no [LS2](/docs/specs/common-structures/).  
A seção de opções do LS2 atualmente não é utilizada.  
Não suportado para LS1.  
Isso é semelhante à [proposta de largura de banda de túnel](/proposals/168-tunnel-bandwidth/),  
que define opções para registros de construção de túnel.

Para pesquisar um endereço de serviço para um nome de host ou b32 específico, o roteador busca o  
conjunto de locação (leaseset) e procura o registro de serviço nas propriedades.

O serviço pode estar hospedado no mesmo destino do próprio LS, ou pode referenciar  
um nome de host/b32 diferente.

Se o destino alvo do serviço for diferente, o LS alvo também  
deve incluir um registro de serviço, apontando para si mesmo, indicando que suporta o serviço.

O projeto não exige suporte especial, cache ou quaisquer alterações nos floodfills.  
Apenas o publicador do conjunto de locação e o cliente que pesquisa um registro de serviço  
precisam suportar essas alterações.

São propostas extensões menores no I2CP e SAM para facilitar a recuperação de  
registros de serviço pelos clientes.



## Especificação

### Especificação de Opção LS2

As opções LS2 DEVEM ser ordenadas pela chave, para que a assinatura seja invariável.

Definidas da seguinte forma:

- serviceoption := optionkey optionvalue
- optionkey := _service._proto
- service := Nome simbólico do serviço desejado. Deve ser minúsculo. Exemplo: "smtp".  
  Caracteres permitidos são [a-z0-9-] e não devem começar ou terminar com "-".  
  Identificadores padrão do [registro de tipos de serviço DNS-SD](http://www.dns-sd.org/ServiceTypes.html) ou do /etc/services do Linux devem ser usados se definidos lá.
- proto := Protocolo de transporte do serviço desejado. Deve ser minúsculo, "tcp" ou "udp".  
  "tcp" significa streaming e "udp" significa datagramas com resposta.  
  Indicadores de protocolo para datagramas brutos e datagram2 podem ser definidos posteriormente.  
  Caracteres permitidos são [a-z0-9-] e não devem começar ou terminar com "-".
- optionvalue := self | srvrecord[,srvrecord]*
- self := "0" ttl port [appoptions]
- srvrecord := "1" ttl priority weight port target [appoptions]
- ttl := tempo de vida, em segundos inteiros. Inteiro positivo. Exemplo: "86400".  
  Recomenda-se um mínimo de 86400 (um dia), veja a seção Recomendações abaixo para detalhes.
- priority := Prioridade do host alvo, valor menor significa mais preferido. Inteiro não negativo. Exemplo: "0"  
  Útil apenas se houver mais de um registro, mas obrigatório mesmo com apenas um registro.
- weight := Peso relativo para registros com a mesma prioridade. Valor maior significa maior chance de ser escolhido. Inteiro não negativo. Exemplo: "0"  
  Útil apenas se houver mais de um registro, mas obrigatório mesmo com apenas um registro.
- port := Porta I2CP onde o serviço está localizado. Inteiro não negativo. Exemplo: "25"  
  A porta 0 é suportada, mas não recomendada.
- target := Nome de host ou b32 do destino que fornece o serviço. Um [nome de host](/docs/overview/naming/) válido. Deve ser minúsculo.  
  Exemplo: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p" ou "example.i2p".  
  Recomenda-se b32, a menos que o nome de host seja "bem conhecido", ou seja, nos endereços oficiais ou padrão.
- appoptions := texto arbitrário específico da aplicação, não deve conter " " ou ",". Codificação em UTF-8.

### Exemplos

No LS2 para aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, apontando para um servidor SMTP:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

No LS2 para aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.b32.i2p, apontando para dois servidores SMTP:

    "_smtp._tcp" "1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p,86400 1 0 25 cccccccccccccccccccccccccccccccccccccccccccc.b32.i2p"

No LS2 para bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p, apontando para si mesmo como servidor SMTP:

    "_smtp._tcp" "0 999999 25"

Formato possível para redirecionar e-mail (veja abaixo):

    "_smtp._tcp" "1 86400 0 0 25 smtp.postman.i2p example@mail.i2p"


### Limites

A estrutura de dados de mapeamento usada para opções LS2 limita chaves e valores a no máximo 255 bytes (não caracteres).  
Com um destino b32, o optionvalue tem cerca de 67 bytes, então caberiam apenas 3 registros.  
Talvez apenas um ou dois com um campo appoptions longo, ou até quatro ou cinco com um nome de host curto.  
Isso deve ser suficiente; múltiplos registros devem ser raros.


### Diferenças da RFC 2782

- Sem pontos finais
- Sem nome após o proto
- Minúsculas obrigatórias
- Em formato de texto com registros separados por vírgula, não em formato binário DNS
- Indicadores de tipo de registro diferentes
- Campo appoptions adicional


### Notas

Não é permitido curinga como (asterisco), (asterisco)._tcp ou _tcp.  
Cada serviço suportado deve ter seu próprio registro.



### Registro de Nomes de Serviço

Identificadores não padrão que não estão listados no [registro de tipos de serviço DNS-SD](http://www.dns-sd.org/ServiceTypes.html) ou no /etc/services do Linux  
podem ser solicitados e adicionados à [especificação de estruturas comuns](/docs/specs/common-structures/).

Formatos específicos de appoptions para serviços também podem ser adicionados lá.


### Especificação I2CP

O [protocolo I2CP](/docs/specs/i2cp/) deve ser estendido para suportar pesquisas de serviço.  
São necessários códigos de erro adicionais nas mensagens MessageStatusMessage e/ou HostReplyMessage relacionados à pesquisa de serviço.  
Para tornar a funcionalidade de pesquisa genérica, não apenas específica para registros de serviço,  
o projeto é suportar a recuperação de todas as opções LS2.

Implementação: Estender HostLookupMessage para adicionar solicitação de  
opções LS2 para hash, nome de host e destino (tipos de solicitação 2-4).  
Estender HostReplyMessage para adicionar o mapeamento de opções se solicitado.  
Estender HostReplyMessage com códigos de erro adicionais.

Os mapeamentos de opções podem ser armazenados em cache ou em cache negativo por um curto período no lado do cliente ou do roteador, dependendo da implementação.  
O tempo máximo recomendado é de uma hora, a menos que o TTL do registro de serviço seja menor.  
Registros de serviço podem ser armazenados em cache até o TTL especificado pela aplicação, cliente ou roteador.

Estender a especificação da seguinte forma:

#### Opções de configuração

Adicionar o seguinte às [opções de configuração I2CP](/docs/specs/i2cp/)

i2cp.leaseSetOption.nnn

Opções a serem colocadas no conjunto de locação. Disponível apenas para LS2.  
nnn começa em 0. O valor da opção contém "key=value".  
(não incluir aspas)

Exemplo:  
i2cp.leaseSetOption.0=_smtp._tcp=1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p


#### Mensagem HostLookup

- Tipo de pesquisa 2: Pesquisa por hash, solicita mapeamento de opções
- Tipo de pesquisa 3: Pesquisa por nome de host, solicita mapeamento de opções
- Tipo de pesquisa 4: Pesquisa por destino, solicita mapeamento de opções

Para o tipo de pesquisa 4, o item 5 é um Destino.



#### Mensagem HostReply

Para os tipos de pesquisa 2-4, o roteador deve buscar o conjunto de locação,  
mesmo se a chave de pesquisa estiver na agenda de endereços.

Se bem-sucedido, o HostReply conterá o mapeamento de opções  
do conjunto de locação e o incluirá como item 5 após o destino.  
Se não houver opções no mapeamento, ou se o conjunto de locação for da versão 1,  
ele ainda será incluído como um mapeamento vazio (dois bytes: 0 0).  
Todas as opções do conjunto de locação serão incluídas, não apenas opções de registro de serviço.  
Por exemplo, opções para parâmetros definidos no futuro podem estar presentes.

Em caso de falha na busca do conjunto de locação, a resposta conterá um novo código de erro 6 (falha na busca do conjunto de locação)  
e não incluirá um mapeamento.  
Quando o código de erro 6 for retornado, o campo Destino pode ou não estar presente.  
Ele estará presente se uma pesquisa por nome de host na agenda de endereços for bem-sucedida,  
ou se uma pesquisa anterior foi bem-sucedida e o resultado foi armazenado em cache,  
ou se o Destino estiver presente na mensagem de pesquisa (tipo de pesquisa 4).

Se um tipo de pesquisa não for suportado,  
a resposta conterá um novo código de erro 7 (tipo de pesquisa não suportado).



### Especificação SAM

O [protocolo SAMv3](/docs/api/samv3/) deve ser estendido para suportar pesquisas de serviço.

Estender NAMING LOOKUP da seguinte forma:

NAMING LOOKUP NAME=example.i2p OPTIONS=true solicita o mapeamento de opções na resposta.

NAME pode ser um destino base64 completo quando OPTIONS=true.

Se a pesquisa do destino for bem-sucedida e as opções estiverem presentes no conjunto de locação,  
então na resposta, após o destino,  
haverá uma ou mais opções no formato OPTION:key=value.  
Cada opção terá um prefixo OPTION: separado.  
Todas as opções do conjunto de locação serão incluídas, não apenas opções de registro de serviço.  
Por exemplo, opções para parâmetros definidos no futuro podem estar presentes.  
Exemplo:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Chaves contendo '=', e chaves ou valores contendo nova linha,  
são consideradas inválidas e o par chave/valor será removido da resposta.

Se nenhuma opção for encontrada no conjunto de locação, ou se o conjunto de locação for da versão 1,  
a resposta não incluirá nenhuma opção.

Se OPTIONS=true estiver na pesquisa e o conjunto de locação não for encontrado, um novo valor de resultado LEASESET_NOT_FOUND será retornado.


## Alternativa de Pesquisa de Nomes

Um projeto alternativo foi considerado, para suportar pesquisas de serviços  
como um nome de host completo, por exemplo _smtp._tcp.example.i2p,  
atualizando a [especificação de nomenclatura](/docs/overview/naming/) para especificar o tratamento de nomes de host que começam com '_'.  
Isso foi rejeitado por duas razões:

- As alterações no I2CP e SAM ainda seriam necessárias para repassar as informações de TTL e porta ao cliente.
- Não seria uma funcionalidade genérica que poderia ser usada para recuperar outras opções LS2  
  que poderiam ser definidas no futuro.


## Recomendações

Servidores devem especificar um TTL de pelo menos 86400 e a porta padrão para a aplicação.



## Recursos Avançados

### Pesquisas Recursivas

Pode ser desejável suportar pesquisas recursivas, onde cada conjunto de locação sucessivo  
é verificado por um registro de serviço apontando para outro conjunto de locação, estilo DNS.  
Isso provavelmente não é necessário, pelo menos em uma implementação inicial.

TODO



### Campos específicos da aplicação

Pode ser desejável ter dados específicos da aplicação no registro de serviço.  
Por exemplo, o operador de example.i2p pode desejar indicar que o e-mail deve  
ser encaminhado para example@mail.i2p. A parte "example@" precisaria estar em um campo separado  
do registro de serviço, ou ser removida do destino.

Mesmo que o operador execute seu próprio serviço de e-mail, ele pode desejar indicar que  
o e-mail deve ser enviado para example@example.i2p. A maioria dos serviços I2P é executada por uma única pessoa.  
Portanto, um campo separado pode ser útil aqui também.

TODO como fazer isso de forma genérica


### Alterações necessárias para E-mail

Fora do escopo desta proposta. Veja a [discussão no i2pforum](http://i2pforum.i2p/viewtopic.php?p=3102) para mais detalhes.


## Notas de Implementação

O armazenamento em cache de registros de serviço até o TTL pode ser feito pelo roteador ou pela aplicação, dependendo da implementação.  
Se o cache será persistente também depende da implementação.

As pesquisas devem também pesquisar o conjunto de locação alvo e verificar se ele contém um registro "self"  
antes de retornar o destino alvo ao cliente.


## Análise de Segurança

Como o conjunto de locação é assinado, quaisquer registros de serviço dentro dele são autenticados pela chave de assinatura do destino.

Os registros de serviço são públicos e visíveis aos floodfills, a menos que o conjunto de locação seja criptografado.  
Qualquer roteador que solicite o conjunto de locação poderá ver os registros de serviço.

Um registro SRV diferente de "self" (ou seja, que aponta para um destino hostname/b32 diferente)  
não exige o consentimento do hostname/b32 alvo.  
Não está claro se um redirecionamento de serviço para um destino arbitrário poderia facilitar algum  
tipo de ataque, ou qual seria o propósito de tal ataque.  
No entanto, esta proposta mitiga tal ataque exigindo que o alvo  
também publique um registro SRV "self". Os implementadores devem verificar a presença de um registro "self"  
no conjunto de locação do alvo.


## Compatibilidade

LS2: Sem problemas. Todas as implementações conhecidas atualmente ignoram o campo de opções no LS2,  
e pulam corretamente um campo de opções não vazio.  
Isso foi verificado em testes tanto pelo Java I2P quanto pelo i2pd durante o desenvolvimento do LS2.  
O LS2 foi implementado na versão 0.9.38 em 2016 e é bem suportado por todas as implementações de roteador.  
O projeto não exige suporte especial, cache ou quaisquer alterações nos floodfills.

Nomenclatura: '_' não é um caractere válido em nomes de host i2p.

I2CP: Os tipos de pesquisa 2-4 não devem ser enviados a roteadores com versão API inferior  
à mínima em que são suportados (a ser definida).

SAM: O servidor SAM Java ignora chaves/valores adicionais como OPTIONS=true.  
O i2pd também deveria, a ser verificado.  
Os clientes SAM não obterão os valores adicionais na resposta a menos que solicitados com OPTIONS=true.  
Nenhuma atualização de versão deve ser necessária.


## Migração

As implementações podem adicionar suporte a qualquer momento, sem necessidade de coordenação,  
exceto por um acordo sobre a versão API efetiva para as alterações no I2CP.  
As versões de compatibilidade SAM para cada implementação serão documentadas na especificação SAM.


## Referências

* [DOTWELLKNOWN](http://i2pforum.i2p/viewtopic.php?p=3102)
* [I2CP](/docs/specs/i2cp/)
* [I2CP-OPTIONS](/docs/specs/i2cp/)
* [LS2](/docs/specs/common-structures/)
* [GNS](http://zzz.i2p/topcs/1545)
* [NAMING](/docs/overview/naming/)
* [Prop123](/proposals/123-new-netdb-entries/)
* [Prop168](/proposals/168-tunnel-bandwidth/)
* [REGISTRY](http://www.dns-sd.org/ServiceTypes.html)
* [RFC2782](https://datatracker.ietf.org/doc/html/rfc2782)
* [SAMv3](/docs/api/samv3/)
* [SRV](https://en.wikipedia.org/wiki/SRV_record)
