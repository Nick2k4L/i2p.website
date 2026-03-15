---
title: "ECIES-X25519-AEAD-Ratchet"
aliases:
  - "/pt/proposals/144-ecies-x25519"
  - "/pt/proposals/144-ecies-x25519/"
number: "144"
author: "zzz, chisana, orignal"
created: "2018-11-22"
lastupdated: "2025-03-05"
status: "Fechado"
thread: "http://zzz.i2p/topics/2639"
target: "0.9.46"
implementedin: "0.9.46"
toc: true
---
## Nota
Implantação e testes na rede em andamento.
Sujeito a revisões menores.
Consulte [SPEC](/docs/specs/ecies/) para a especificação oficial.

Os seguintes recursos não estão implementados na versão 0.9.46:

- Blocos MessageNumbers, Options e Termination
- Respostas na camada de protocolo
- Chave estática zero
- Multicast


## Visão Geral

Esta é uma proposta para o primeiro novo tipo de criptografia fim-a-fim
desde o início do I2P, para substituir ElGamal/AES+SessionTags [Elg-AES](/docs/specs/elgamal-aes/).

Baseia-se em trabalhos anteriores conforme a seguir:

- Especificação de estruturas comuns [Common Structures](/docs/specs/common-structures/)
- Especificação [I2NP](/docs/specs/i2np/) incluindo LS2
- ElGamal/AES+Session Tags [Elg-AES](/docs/specs/elgamal-aes/)
- [http://zzz.i2p/topics/1768](http://zzz.i2p/topics/1768) visão geral de nova criptografia assimétrica
- Visão geral de criptografia de baixo nível [CRYPTO-ELG](/docs/specs/cryptography/)
- ECIES [http://zzz.i2p/topics/2418](http://zzz.i2p/topics/2418)
- [NTCP2](/docs/specs/ntcp2/) [Proposal 111](/proposals/111-ntcp-2/)
- 123 Novas entradas no netDB
- 142 Novo modelo de criptografia
- [Noise](https://noiseprotocol.org/noise.html) protocol
- [Signal](https://signal.org/docs/) algoritmo double ratchet

O objetivo é suportar nova criptografia para comunicação fim-a-fim,
destino-a-destino.

O design usará um handshake Noise e fase de dados incorporando o double ratchet do Signal.

Todas as referências ao Signal e Noise nesta proposta são apenas para informação de fundo.
O conhecimento dos protocolos Signal e Noise não é necessário para entender
ou implementar esta proposta.


### Usos atuais do ElGamal

Como revisão,
chaves públicas ElGamal de 256 bytes podem ser encontradas nas seguintes estruturas de dados.
Consulte a especificação de estruturas comuns.

- Em uma Identidade de Roteador
  Esta é a chave de criptografia do roteador.

- Em um Destino
  A chave pública do destino foi usada para a antiga criptografia i2cp-to-i2cp
  que foi desativada na versão 0.6, atualmente está sem uso exceto por
  o IV para criptografia de LeaseSet, que está obsoleto.
  A chave pública no LeaseSet é usada em vez disso.

- Em um LeaseSet
  Esta é a chave de criptografia do destino.

- Em um LS2
  Esta é a chave de criptografia do destino.



### EncTypes em Certificados de Chave

Como revisão,
adicionamos suporte para tipos de criptografia quando adicionamos suporte para tipos de assinatura.
O campo de tipo de criptografia é sempre zero, tanto em Destinos quanto em RouterIdentities.
Se isso será alterado ou não é algo a ser definido.
Consulte a especificação de estruturas comuns [Common Structures](/docs/specs/common-structures/).




### Usos de Criptografia Assimétrica

Como revisão, usamos ElGamal para:

1) Mensagens de construção de túnel (a chave está no RouterIdentity)
   A substituição não está coberta nesta proposta.
   Consulte a proposta 152 [Proposal 152](/proposals/152-ecies-tunnels).

2) Criptografia roteador-a-roteador de netdb e outras mensagens I2NP (a chave está no RouterIdentity)
   Depende desta proposta.
   Requer uma proposta para 1) também, ou colocar a chave nas opções do RI.

3) Cliente fim-a-fim ElGamal+AES/SessionTag (a chave está no LeaseSet, a chave do Destino está sem uso)
   A substituição ESTÁ coberta nesta proposta.

4) DH efêmero para NTCP1 e SSU
   A substituição não está coberta nesta proposta.
   Consulte a proposta 111 para NTCP2.
   Nenhuma proposta atual para SSU2.


### Objetivos

- Compatibilidade com versões anteriores
- Requer e baseia-se no LS2 (proposta 123)
- Aproveitar nova criptografia ou primitivos adicionados para NTCP2 (proposta 111)
- Nenhuma nova criptografia ou primitivos necessários para suporte
- Manter o desacoplamento entre criptografia e assinatura; suportar todas as versões atuais e futuras
- Habilitar nova criptografia para destinos
- Habilitar nova criptografia para roteadores, mas apenas para mensagens garlic - a construção de túneis seria
  uma proposta separada
- Não quebrar nada que dependa de hashes binários de destino de 32 bytes, por exemplo, bittorrent
- Manter entrega de mensagens 0-RTT usando DH efêmero-estático
- Não exigir buffering / enfileiramento de mensagens nesta camada de protocolo;
  continuar a suportar entrega ilimitada de mensagens em ambas as direções sem esperar por uma resposta
- Atualizar para DH efêmero-efêmero após 1 RTT
- Manter o tratamento de mensagens fora de ordem
- Manter segurança de 256 bits
- Adicionar forward secrecy
- Adicionar autenticação (AEAD)
- Muito mais eficiente em CPU do que ElGamal
- Não depender do Java jbigi para tornar o DH eficiente
- Minimizar operações de DH
- Muito mais eficiente em largura de banda do que ElGamal (bloco ElGamal de 514 bytes)
- Suportar criptografia nova e antiga no mesmo túnel se desejado
- O destinatário é capaz de distinguir eficientemente criptografia nova da antiga vindo
  pelo mesmo túnel
- Outros não conseguem distinguir criptografia nova da antiga ou futura
- Eliminar a classificação de comprimento de sessão nova vs. existente (suportar padding)
- Nenhuma nova mensagem I2NP necessária
- Substituir o checksum SHA-256 no payload AES com AEAD
- Suportar o vínculo entre sessões de transmissão e recepção para que
  os reconhecimentos possam ocorrer dentro do protocolo, em vez de exclusivamente fora de banda.
  Isso também permitirá que respostas tenham forward secrecy imediatamente.
- Habilitar criptografia fim-a-fim de certas mensagens (armazenamentos de RouterInfo)
  que atualmente não fazemos devido à sobrecarga de CPU.
- Não alterar a Mensagem Garlic I2NP
  ou o formato de Instruções de Entrega de Mensagem Garlic.
- Eliminar campos não utilizados ou redundantes nos formatos Garlic Clove Set e Clove.

Eliminar vários problemas com session tags, incluindo:

- Incapacidade de usar AES até a primeira resposta
- Falhas e travamentos se a entrega da tag for assumida
- Ineficiência em largura de banda, especialmente na primeira entrega
- Grande ineficiência espacial para armazenar tags
- Grande sobrecarga de largura de banda para entregar tags
- Altamente complexo, difícil de implementar
- Difícil de ajustar para vários casos de uso
  (streaming vs. datagramas, servidor vs. cliente, alta vs. baixa largura de banda)
- Vulnerabilidades de esgotamento de memória devido à entrega de tags


### Não objetivos / Fora do escopo

- Alterações no formato LS2 (proposta 123 está concluída)
- Novo algoritmo de rotação DHT ou geração de número aleatório compartilhado
- Nova criptografia para construção de túneis.
  Consulte a proposta 152 [Proposal 152](/proposals/152-ecies-tunnels).
- Nova criptografia para criptografia na camada de túnel.
  Consulte a proposta 153 [Proposal 153](/proposals/153-chacha20-layer-encryption).
- Métodos de criptografia, transmissão e recepção de mensagens I2NP DLM / DSM / DSRM.
  Não está mudando.
- Não há suporte para comunicação LS1-to-LS2 ou ElGamal/AES-to-this-proposal.
  Esta proposta é um protocolo bidirecional.
  Destinos podem lidar com compatibilidade com versões anteriores publicando dois leasesets
  usando os mesmos túneis, ou colocando ambos os tipos de criptografia no LS2.
- Mudanças no modelo de ameaça
- Detalhes de implementação não são discutidos aqui e são deixados a cada projeto.
- (Otimista) Adicionar extensões ou ganchos para suportar multicast



### Justificativa

ElGamal/AES+SessionTag tem sido nosso único protocolo fim-a-fim por cerca de 15 anos,
essencialmente sem modificações no protocolo.
Agora existem primitivas criptográficas que são mais rápidas.
Precisamos aprimorar a segurança do protocolo.
Também desenvolvemos estratégias heurísticas e soluções alternativas para minimizar a
sobrecarga de memória e largura de banda do protocolo, mas essas estratégias
são frágeis, difíceis de ajustar e tornam o protocolo ainda mais propenso
a falhas, fazendo com que a sessão caia.

Por quase o mesmo período, a especificação ElGamal/AES+SessionTag e a documentação relacionada
descreveram como é caro em largura de banda entregar session tags,
e propuseram substituir a entrega de session tags por um "PRNG sincronizado".
Um PRNG sincronizado gera deterministicamente as mesmas tags nas duas extremidades,
derivadas de uma semente comum.
Um PRNG sincronizado também pode ser chamado de "ratchet".
Esta proposta (finalmente) especifica esse mecanismo de ratchet e elimina a entrega de tags.

Ao usar um ratchet (um PRNG sincronizado) para gerar as
session tags, eliminamos a sobrecarga de enviar session tags
na mensagem New Session e mensagens subsequentes quando necessário.
Para um conjunto típico de tags de 32, isso é 1KB.
Isso também elimina o armazenamento de session tags no lado do remetente,
reduzindo assim os requisitos de armazenamento pela metade.

Um handshake bidirecional completo, semelhante ao padrão Noise IK, é necessário para evitar ataques de Key Compromise Impersonation (KCI).
Consulte a tabela "Payload Security Properties" do Noise em [NOISE](https://noiseprotocol.org/noise.html).
Para mais informações sobre KCI, consulte o artigo https://www.usenix.org/system/files/conference/woot15/woot15-paper-hlauschek.pdf



### Modelo de Ameaça

O modelo de ameaça é um pouco diferente do NTCP2 (proposta 111).
Os nós MitM são o OBEP e IBGW e assumem-se ter visão completa do
netDB global atual ou histórico, por coludirem com floodfills.

O objetivo é impedir que esses MitMs classifiquem o tráfego como
mensagens de sessão nova e existente, ou como criptografia nova vs. antiga.



## Proposta Detalhada

Esta proposta define um novo protocolo fim-a-fim para substituir ElGamal/AES+SessionTags.
O design usará um handshake Noise e fase de dados incorporando o double ratchet do Signal.


### Resumo do Design Criptográfico

Há cinco partes do protocolo a serem redesenhadas:


- 1) Os formatos de contêiner de sessão nova e existente
  são substituídos por novos formatos.
- 2) ElGamal (chaves públicas de 256 bytes, chaves privadas de 128 bytes) será substituído
  por ECIES-X25519 (chaves públicas e privadas de 32 bytes)
- 3) AES será substituído por
  AEAD_ChaCha20_Poly1305 (abreviado como ChaChaPoly abaixo)
- 4) SessionTags serão substituídas por ratchets,
  que é essencialmente um PRNG criptográfico e sincronizado.
- 5) O payload AES, conforme definido na especificação ElGamal/AES+SessionTags,
  é substituído por um formato de bloco semelhante ao do NTCP2.

Cada uma das cinco mudanças tem sua própria seção abaixo.


### Novas Primitivas Criptográficas para I2P

Implementações existentes de roteadores I2P exigirão implementações para
as seguintes primitivas criptográficas padrão,
que não são necessárias para protocolos I2P atuais:

- ECIES (mas isso é essencialmente X25519)
- Elligator2

Implementações existentes de roteadores I2P que ainda não implementaram [NTCP2](/docs/specs/ntcp2/) ([Proposal 111](/proposals/111-ntcp-2/))
também exigirão implementações para:

- Geração de chaves X25519 e DH
- AEAD_ChaCha20_Poly1305 (abreviado como ChaChaPoly abaixo)
- HKDF


### Tipo de Criptografia

O tipo de criptografia (usado no LS2) é 4.
Isso indica uma chave pública X25519 de 32 bytes em ordem little-endian,
e o protocolo fim-a-fim especificado aqui.

O tipo de criptografia 0 é ElGamal.
Os tipos de criptografia 1-3 são reservados para ECIES-ECDH-AES-SessionTag, consulte a proposta 145 [Proposal 145](/proposals/145-ecies).


### Framework do Protocolo Noise

Esta proposta fornece os requisitos com base no Framework do Protocolo Noise
[NOISE](https://noiseprotocol.org/noise.html) (Revisão 34, 2018-07-11).
O Noise tem propriedades semelhantes ao protocolo Station-To-Station
[STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol), que é a base para o protocolo [SSU](/docs/legacy/ssu/). Em termos do Noise, Alice
é o iniciador, e Bob é o respondente.

Esta proposta baseia-se no protocolo Noise Noise_IK_25519_ChaChaPoly_SHA256.
(O identificador real para a função de derivação de chave inicial
é "Noise_IKelg2_25519_ChaChaPoly_SHA256"
para indicar extensões I2P - veja a seção KDF 1 abaixo)
Este protocolo Noise usa as seguintes primitivas:

- Padrão de Handshake Interativo: IK
  Alice transmite imediatamente sua chave estática para Bob (I)
  Alice já conhece a chave estática de Bob (K)

- Padrão de Handshake Unidirecional: N
  Alice não transmite sua chave estática para Bob (N)

- Função DH: X25519
  DH X25519 com comprimento de chave de 32 bytes conforme especificado em [RFC-7748](https://tools.ietf.org/html/rfc7748).

- Função de Cifra: ChaChaPoly
  AEAD_CHACHA20_POLY1305 conforme especificado na [RFC-7539](https://tools.ietf.org/html/rfc7539) seção 2.8.
  Nonce de 12 bytes, com os primeiros 4 bytes definidos como zero.
  Idêntico ao do [NTCP2](/docs/specs/ntcp2/).

- Função Hash: SHA256
  Hash padrão de 32 bytes, já amplamente usado no I2P.


### Adições ao Framework

Esta proposta define os seguintes aprimoramentos para
Noise_IK_25519_ChaChaPoly_SHA256. Geralmente seguem as diretrizes em
[NOISE](https://noiseprotocol.org/noise.html) seção 13.

1) Chaves efêmeras em texto claro são codificadas com [Elligator2](https://elligator.cr.yp.to/).

2) A resposta é prefixada com uma tag em texto claro.

3) O formato de payload é definido para as mensagens 1, 2 e a fase de dados.
   É claro que isso não é definido no Noise.

Todas as mensagens incluem um cabeçalho de Mensagem Garlic [I2NP](/docs/specs/i2np/).
A fase de dados usa criptografia semelhante, mas não compatível com, a fase de dados do Noise.


### Padrões de Handshake

Handshakes usam padrões de handshake [Noise](https://noiseprotocol.org/noise.html).

O seguinte mapeamento de letras é usado:

- e = chave efêmera única
- s = chave estática
- p = payload da mensagem

Sessões únicas e não vinculadas são semelhantes ao padrão Noise N.

```

<- s
  ...
  e es p ->

```

Sessões vinculadas são semelhantes ao padrão Noise IK.

```

<- s
  ...
  e es s ss p ->
  <- tag e ee se
  <- p
  p ->

```


### Sessões

O protocolo atual ElGamal/AES+SessionTag é unidirecional.
Nesta camada, o receptor não sabe de onde uma mensagem vem.
Sessões de saída e entrada não são associadas.
Reconhecimentos são fora de banda usando uma DeliveryStatusMessage
(envolvida em uma GarlicMessage) na clove.

Há uma ineficiência substancial em um protocolo unidirecional.
Qualquer resposta também deve usar uma cara mensagem 'New Session'.
Isso causa maior largura de banda, uso de CPU e memória.

Também há fraquezas de segurança em um protocolo unidirecional.
Todas as sessões são baseadas em DH efêmero-estático.
Sem um caminho de retorno, não há como Bob "ratchetar" sua chave estática
para uma chave efêmera.
Sem saber de onde uma mensagem vem, não há como usar
a chave efêmera recebida para mensagens de saída,
então a resposta inicial também usa DH efêmero-estático.

Para esta proposta, definimos dois mecanismos para criar um protocolo bidirecional -
"emparelhamento" e "vinculação".
Esses mecanismos fornecem maior eficiência e segurança.


### Contexto da Sessão

Como com ElGamal/AES+SessionTags, todas as sessões de entrada e saída
devem estar em um determinado contexto, seja o contexto do roteador ou
o contexto para um destino local específico.
No Java I2P, esse contexto é chamado de Session Key Manager.

As sessões não devem ser compartilhadas entre contextos, pois isso permitiria
a correlação entre os vários destinos locais,
ou entre um destino local e um roteador.

Quando um determinado destino suporta tanto ElGamal/AES+SessionTags
quanto esta proposta, ambos os tipos de sessões podem compartilhar um contexto.
Veja a seção 1c) abaixo.



### Emparelhamento de Sessões de Entrada e Saída

Quando uma sessão de saída é criada no originador (Alice),
uma nova sessão de entrada é criada e emparelhada com a sessão de saída,
a menos que nenhuma resposta seja esperada (por exemplo, datagramas brutos).

Uma nova sessão de entrada é sempre emparelhada com uma nova sessão de saída,
a menos que nenhuma resposta seja solicitada (por exemplo, datagramas brutos).

Se uma resposta for solicitada e vinculada a um destino ou roteador remoto,
essa nova sessão de saída será vinculada a esse destino ou roteador,
e substituirá qualquer sessão de saída anterior para esse destino ou roteador.

Emparelhar sessões de entrada e saída fornece um protocolo bidirecional
com a capacidade de ratchetar as chaves DH.



### Vinculação de Sessões e Destinos

Há apenas uma sessão de saída para um determinado destino ou roteador.
Pode haver várias sessões de entrada atuais de um determinado destino ou roteador.
Geralmente, quando uma nova sessão de entrada é criada e o tráfego é recebido
nessa sessão (o que serve como ACK), as outras serão marcadas
para expirar relativamente rápido, dentro de um minuto ou mais.
O valor de mensagens enviadas anteriormente (PN) é verificado, e se não houver
mensagens não recebidas (dentro do tamanho da janela) na sessão de entrada anterior,
a sessão anterior pode ser excluída imediatamente.


Quando uma sessão de saída é criada no originador (Alice),
ela é vinculada ao Destino remoto (Bob),
e qualquer sessão de entrada emparelhada também será vinculada ao Destino remoto.
À medida que as sessões ratchetam, continuam vinculadas ao Destino remoto.

Quando uma sessão de entrada é criada no receptor (Bob),
ela pode ser vinculada ao Destino remoto (Alice), à opção de Alice.
Se Alice incluir informações de vinculação (sua chave estática) na mensagem New Session,
a sessão será vinculada a esse destino,
e uma sessão de saída será criada e vinculada ao mesmo Destino.
À medida que as sessões ratchetam, continuam vinculadas ao Destino remoto.


### Benefícios da Vinculação e Emparelhamento

Para o caso comum de streaming, esperamos que Alice e Bob usem o protocolo da seguinte forma:

- Alice emparelha sua nova sessão de saída com uma nova sessão de entrada, ambas vinculadas ao destino remoto (Bob).
- Alice inclui as informações de vinculação e assinatura, e uma solicitação de resposta, na
  mensagem New Session enviada a Bob.
- Bob emparelha sua nova sessão de entrada com uma nova sessão de saída, ambas vinculadas ao destino remoto (Alice).
- Bob envia uma resposta (ack) a Alice na sessão emparelhada, com um ratchet para uma nova chave DH.
- Alice ratcheta para uma nova sessão de saída com a nova chave de Bob, emparelhada com a sessão de entrada existente.

Ao vincular uma sessão de entrada a um Destino remoto e emparelhar a sessão de entrada
a uma sessão de saída vinculada ao mesmo Destino, alcançamos dois grandes benefícios:

1) A resposta inicial de Bob para Alice usa DH efêmero-efêmero

2) Depois que Alice recebe a resposta de Bob e ratcheta, todas as mensagens subsequentes de Alice para Bob
usam DH efêmero-efêmero.


### ACKs de Mensagem

Em ElGamal/AES+SessionTags, quando um LeaseSet é agrupado como uma clove garlic,
ou tags são entregues, o roteador remetente solicita um ACK.
Isso é uma clove garlic separada contendo uma DeliveryStatus Message.
Para segurança adicional, a DeliveryStatus Message é envolvida em uma Garlic Message.
Esse mecanismo é fora de banda do ponto de vista do protocolo.

No novo protocolo, como as sessões de entrada e saída estão emparelhadas,
podemos ter ACKs dentro da banda. Nenhuma clove separada é necessária.

Um ACK explícito é simplesmente uma mensagem Existing Session sem bloco I2NP.
No entanto, na maioria dos casos, um ACK explícito pode ser evitado, pois há tráfego reverso.
Pode ser desejável que as implementações esperem um curto tempo (talvez algumas centenas de ms)
antes de enviar um ACK explícito, para dar tempo à camada de streaming ou aplicação de responder.

As implementações também precisarão adiar qualquer envio de ACK até depois que o
bloco I2NP seja processado, pois a Garlic Message pode conter uma Database Store Message
com um lease set. Um lease set recente será necessário para rotear o ACK,
e o destino remoto (contido no lease set) será necessário para
verificar a chave estática vinculada.


### Tempo Limite de Sessões

Sessões de saída devem sempre expirar antes das sessões de entrada.
Uma vez que uma sessão de saída expire e uma nova seja criada, uma nova sessão de entrada emparelhada
também será criada. Se houver uma sessão de entrada antiga,
ela será permitida expirar.


### Multicast

TBD


### Definições
Definimos as seguintes funções correspondentes aos blocos criptográficos usados.

ZEROLEN
    array de bytes de comprimento zero

CSRNG(n)
    saída de n bytes de um gerador de números aleatórios criptograficamente seguro.

H(p, d)
    função hash SHA-256 que recebe uma string de personalização p e dados d, e
    produz uma saída de comprimento 32 bytes.
    Conforme definido em [NOISE](https://noiseprotocol.org/noise.html).
    || abaixo significa concatenar.

    Use SHA-256 da seguinte forma::

        H(p, d) := SHA-256(p || d)

MixHash(d)
    função hash SHA-256 que recebe um hash anterior h e novos dados d,
    e produz uma saída de comprimento 32 bytes.
    || abaixo significa concatenar.

    Use SHA-256 da seguinte forma::

        MixHash(d) := h = SHA-256(h || d)

STREAM
    O AEAD ChaCha20/Poly1305 conforme especificado na [RFC-7539](https://tools.ietf.org/html/rfc7539).
    S_KEY_LEN = 32 e S_IV_LEN = 12.

    ENCRYPT(k, n, plaintext, ad)
        Criptografa plaintext usando a chave de cifra k e nonce n que DEVE ser único para
        a chave k.
        Dados associados ad são opcionais.
        Retorna um texto cifrado com o tamanho do plaintext + 16 bytes para o HMAC.

        Todo o texto cifrado deve ser indistinguível de aleatório se a chave for secreta.

    DECRYPT(k, n, ciphertext, ad)
        Descriptografa ciphertext usando a chave de cifra k e nonce n.
        Dados associados ad são opcionais.
        Retorna o plaintext.

DH
    Sistema de acordo de chave pública X25519. Chaves privadas de 32 bytes, chaves públicas de 32
    bytes, produz saídas de 32 bytes. Tem as seguintes
    funções:

    GENERATE_PRIVATE()
        Gera uma nova chave privada.

    DERIVE_PUBLIC(privkey)
        Retorna a chave pública correspondente à chave privada fornecida.

    GENERATE_PRIVATE_ELG2()
        Gera uma nova chave privada que mapeia para uma chave pública adequada para codificação Elligator2.
        Observe que metade das chaves privadas geradas aleatoriamente não será adequada e deve ser descartada.

    ENCODE_ELG2(pubkey)
        Retorna a chave pública codificada com Elligator2 correspondente à chave pública fornecida (mapeamento inverso).
        Chaves codificadas são little endian.
        Chave codificada deve ter 256 bits indistinguíveis de dados aleatórios.
        Consulte a seção Elligator2 abaixo para especificação.

    DECODE_ELG2(pubkey)
        Retorna a chave pública correspondente à chave pública codificada com Elligator2 fornecida.
        Consulte a seção Elligator2 abaixo para especificação.

    DH(privkey, pubkey)
        Gera um segredo compartilhado a partir das chaves privada e pública fornecidas.

HKDF(salt, ikm, info, n)
    Uma função de derivação de chave criptográfica que recebe algum material de chave de entrada ikm (que
    deve ter boa entropia mas não é necessário ser uma string uniformemente aleatória), um salt
    de comprimento 32 bytes, e um valor 'info' específico do contexto, e produz uma saída
    de n bytes adequada para uso como material de chave.

    Use HKDF conforme especificado na [RFC-5869](https://tools.ietf.org/html/rfc5869), usando a função hash HMAC SHA-256
    conforme especificado na [RFC-2104](https://tools.ietf.org/html/rfc2104). Isso significa que SALT_LEN é no máximo 32 bytes.

MixKey(d)
    Use HKDF() com um chainKey anterior e novos dados d, e
    define o novo chainKey e k.
    Conforme definido em [NOISE](https://noiseprotocol.org/noise.html).

    Use HKDF da seguinte forma::

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]



### 1) Formato da mensagem


### Revisão do Formato Atual da Mensagem

A Mensagem Garlic conforme especificado em [I2NP](/docs/specs/i2np/) é a seguinte.
Como objetivo de design é que os saltos intermediários não possam distinguir criptografia nova da antiga,
esse formato não pode mudar, mesmo que o campo de comprimento seja redundante.
O formato é mostrado com o cabeçalho completo de 16 bytes, embora o
cabeçalho real possa estar em um formato diferente, dependendo do transporte usado.

Quando descriptografados, os dados contêm uma série de Garlic Cloves e dados adicionais,
também conhecidos como Clove Set.

Consulte [I2NP](/docs/specs/i2np/) para detalhes e uma especificação completa.


```

+----+----+----+----+----+----+----+----+
  |type|      msg_id       |  expiration
  +----+----+----+----+----+----+----+----+
                           |  size   |chks|
  +----+----+----+----+----+----+----+----+
  |      length       |                   |
  +----+----+----+----+                   +
  |          encrypted data               |
  ~                                       ~
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

```


### Revisão do Formato de Dados Criptografados

O formato de mensagem atual, usado por mais de 15 anos,
é ElGamal/AES+SessionTags.
Em ElGamal/AES+SessionTags, há dois formatos de mensagem:

1) Nova sessão:
- Bloco ElGamal de 514 bytes
- Bloco AES (mínimo de 128 bytes, múltiplo de 16)

2) Sessão existente:
- Tag de sessão de 32 bytes
- Bloco AES (mínimo de 128 bytes, múltiplo de 16)

O preenchimento mínimo para 128 é conforme implementado no Java I2P, mas não é imposto na recepção.

Essas mensagens são encapsuladas em uma mensagem garlic I2NP, que contém
um campo de comprimento, portanto o comprimento é conhecido.

Observe que não há preenchimento definido para um comprimento não múltiplo de 16,
portanto, a Nova Sessão é sempre (mod 16 == 2),
e uma Sessão Existente é sempre (mod 16 == 0).
Precisamos corrigir isso.

O receptor primeiro tenta procurar os primeiros 32 bytes como uma Tag de Sessão.
Se encontrada, ele descriptografa o bloco AES.
Se não encontrada, e os dados tiverem pelo menos (514+16) de comprimento, ele tenta descriptografar o bloco ElGamal,
e se bem-sucedido, descriptografa o bloco AES.


### Novas Session Tags e Comparação com o Signal

No Signal Double Ratchet, o cabeçalho contém:

- DH: Chave pública atual do ratchet
- PN: Comprimento da cadeia de mensagens anterior
- N: Número da Mensagem

Os "sending chains" do Signal são aproximadamente equivalentes aos nossos conjuntos de tags.
Ao usar uma session tag, podemos eliminar a maior parte disso.

Em Nova Sessão, colocamos apenas a chave pública no cabeçalho não criptografado.

Em Sessão Existente, usamos uma session tag para o cabeçalho.
A session tag está associada à chave pública atual do ratchet,
e ao número da mensagem.

Tanto em nova quanto em Sessão Existente, PN e N estão no corpo criptografado.

No Signal, as coisas estão constantemente ratcheteando. Uma nova chave pública DH exige que o
receptor ratchet e envie uma nova chave pública de volta, o que também serve
como o ack para a chave pública recebida.
Isso seria um número muito alto de operações DH para nós.
Então separamos o ack da chave recebida e a transmissão de uma nova chave pública.
Qualquer mensagem usando uma session tag gerada a partir da nova chave pública DH constitui um ACK.
Só transmitimos uma nova chave pública quando desejamos rekey.

O número máximo de mensagens antes que o DH precise ratchetar é 65535.

Ao entregar uma chave de sessão, derivamos o "Conjunto de Tags" a partir dela,
em vez de ter que entregar session tags também.
Um Conjunto de Tags pode ter até 65536 tags.
No entanto, os receptores devem implementar uma estratégia de "look-ahead",
em vez de gerar todas as tags possíveis de uma vez.
Gere no máximo N tags além da última boa tag recebida.
N pode ser no máximo 128, mas 32 ou até menos pode ser uma escolha melhor.



### 1a) Formato de Nova Sessão

Chave Pública Efêmera de Nova Sessão (32 bytes)
Dados criptografados e MAC (bytes restantes)

A mensagem Nova Sessão pode ou não conter a chave pública estática do remetente.
Se incluída, a sessão reversa é vinculada a essa chave.
A chave estática deve ser incluída se respostas forem esperadas,
ou seja, para streaming e datagramas repliáveis.
Não deve ser incluída para datagramas brutos.

A mensagem Nova Sessão é semelhante ao padrão unidirecional Noise [NOISE](https://noiseprotocol.org/noise.html)
"N" (se a chave estática não for enviada),
ou ao padrão bidirecional "IK" (se a chave estática for enviada).



### 1b) Formato de Nova Sessão (com vinculação)

Comprimento é 96 + comprimento do payload.
Formato criptografado:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   Chave Pública Efêmera de Nova Sessão    |
  +             32 bytes                  +
  |     Codificada com Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +         Chave Estática                    +
  |       Dados criptografados ChaCha20         |
  +            32 bytes                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticação de Mensagem Poly1305 |
  +    (MAC) para seção de Chave Estática       +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Seção de Payload            +
  |       Dados criptografados ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticação de Mensagem Poly1305 |
  +         (MAC) para Seção de Payload     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Chave Pública :: 32 bytes, little endian, Elligator2, texto claro

  Dados criptografados de Chave Estática :: 32 bytes

  Dados criptografados da Seção de Payload :: dados restantes menos 16 bytes

  MAC :: código de autenticação de mensagem Poly1305, 16 bytes

```


### Chave Efêmera de Nova Sessão

A chave efêmera é de 32 bytes, codificada com Elligator2.
Essa chave nunca é reutilizada; uma nova chave é gerada com
cada mensagem, incluindo retransmissões.

### Chave Estática

Quando descriptografada, a chave estática X25519 de Alice, 32 bytes.


### Payload

O comprimento criptografado é o restante dos dados.
O comprimento descriptografado é 16 a menos que o comprimento criptografado.
O payload deve conter um bloco DateTime e geralmente conterá um ou mais blocos Garlic Clove.
Consulte a seção de payload abaixo para formato e requisitos adicionais.



### 1c) Formato de Nova Sessão (sem vinculação)

Se nenhuma resposta for necessária, nenhuma chave estática é enviada.


Comprimento é 96 + comprimento do payload.
Formato criptografado:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   Chave Pública Efêmera de Nova Sessão    |
  +             32 bytes                  +
  |     Codificada com Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Seção de Flags               +
  |       Dados criptografados ChaCha20         |
  +            32 bytes                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticação de Mensagem Poly1305 |
  +         (MAC) para seção acima       +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Seção de Payload            +
  |       Dados criptografados ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticação de Mensagem Poly1305 |
  +         (MAC) para Seção de Payload     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Chave Pública :: 32 bytes, little endian, Elligator2, texto claro

  Dados criptografados da Seção de Flags :: 32 bytes

  Dados criptografados da Seção de Payload :: dados restantes menos 16 bytes

  MAC :: código de autenticação de mensagem Poly1305, 16 bytes

```

### Chave Efêmera de Nova Sessão

Chave efêmera de Alice.
A chave efêmera é de 32 bytes, codificada com Elligator2, little endian.
Essa chave nunca é reutilizada; uma nova chave é gerada com
cada mensagem, incluindo retransmissões.


### Dados Descriptografados da Seção de Flags

A seção de Flags não contém nada.
É sempre de 32 bytes, porque deve ter o mesmo comprimento
da chave estática para mensagens Nova Sessão com vinculação.
Bob determina se é uma chave estática ou uma seção de flags
testando se os 32 bytes são todos zeros.

TODO alguma flag necessária aqui?

### Payload

O comprimento criptografado é o restante dos dados.
O comprimento descriptografado é 16 a menos que o comprimento criptografado.
O payload deve conter um bloco DateTime e geralmente conterá um ou mais blocos Garlic Clove.
Consulte a seção de payload abaixo para formato e requisitos adicionais.




### 1d) Formato Único (sem vinculação ou sessão)

Se apenas uma única mensagem for esperada para ser enviada,
não é necessário configuração de sessão ou chave estática.


Comprimento é 96 + comprimento do payload.
Formato criptografado:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |       Chave Pública Efêmera            |
  +             32 bytes                  +
  |     Codificada com Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           Seção de Flags               +
  |       Dados criptografados ChaCha20         |
  +            32 bytes                   +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticação de Mensagem Poly1305 |
  +         (MAC) para seção acima       +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Seção de Payload            +
  |       Dados criptografados ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticação de Mensagem Poly1305 |
  +         (MAC) para Seção de Payload     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Chave Pública :: 32 bytes, little endian, Elligator2, texto claro

  Dados criptografados da Seção de Flags :: 32 bytes

  Dados criptografados da Seção de Payload :: dados restantes menos 16 bytes

  MAC :: código de autenticação de mensagem Poly1305, 16 bytes

```


### Chave Única de Nova Sessão

A chave única é de 32 bytes, codificada com Elligator2, little endian.
Essa chave nunca é reutilizada; uma nova chave é gerada com
cada mensagem, incluindo retransmissões.


### Dados Descriptografados da Seção de Flags

A seção de Flags não contém nada.
É sempre de 32 bytes, porque deve ter o mesmo comprimento
da chave estática para mensagens Nova Sessão com vinculação.
Bob determina se é uma chave estática ou uma seção de flags
testando se os 32 bytes são todos zeros.

TODO alguma flag necessária aqui?

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                                       |
  +             Todos zeros                 +
  |              32 bytes                 |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+

  zeros:: Todos zeros, 32 bytes.

```


### Payload

O comprimento criptografado é o restante dos dados.
O comprimento descriptografado é 16 a menos que o comprimento criptografado.
O payload deve conter um bloco DateTime e geralmente conterá um ou mais blocos Garlic Clove.
Consulte a seção de payload abaixo para formato e requisitos adicionais.



### 1f) KDFs para Mensagem Nova Sessão

### KDF para ChainKey Inicial

Este é o [NOISE](https://noiseprotocol.org/noise.html) padrão para IK com um nome de protocolo modificado.
Observe que usamos o mesmo inicializador para o padrão IK (sessões vinculadas)
e para o padrão N (sessões não vinculadas).

O nome do protocolo é modificado por duas razões.
Primeiro, para indicar que as chaves efêmeras são codificadas com Elligator2,
e segundo, para indicar que MixHash() é chamado antes da segunda mensagem
para misturar o valor da tag.

```

Este é o padrão de mensagem "e":

  // Define protocol_name.
  Define protocol_name = "Noise_IKelg2+hs2_25519_ChaChaPoly_SHA256"
   (40 bytes, codificado em US-ASCII, sem terminação NULL).

  // Define Hash h = 32 bytes
  h = SHA256(protocol_name);

  Define ck = 32 byte chaining key. Copia os dados de h para ck.
  Define chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // até aqui, pode ser pré-calculado por Alice para todas as conexões de saída

```


### KDF para Conteúdo Criptografado da Seção de Flags/Chave Estática

```

Este é o padrão de mensagem "e":

  // Chaves X25519 estáticas de Bob
  // bpk é publicada no leaseset
  bsk = GENERATE_PRIVATE()
  bpk = DERIVE_PUBLIC(bsk)

  // Chave pública estática de Bob
  // MixHash(bpk)
  // || abaixo significa concatenar
  h = SHA256(h || bpk);

  // até aqui, pode ser pré-calculado por Bob para todas as conexões de entrada

  // Chaves X25519 efêmeras de Alice
  aesk = GENERATE_PRIVATE_ELG2()
  aepk = DERIVE_PUBLIC(aesk)

  // Chave pública efêmera de Alice
  // MixHash(aepk)
  // || abaixo significa concatenar
  h = SHA256(h || aepk);

  // h é usado como dados associados para o AEAD na Mensagem Nova Sessão
  // Mantenha o Hash h para o KDF de Resposta de Nova Sessão
  // eapk é enviada em texto claro no
  // início da mensagem Nova Sessão
  elg2_aepk = ENCODE_ELG2(aepk)
  // Como decodificado por Bob
  aepk = DECODE_ELG2(elg2_aepk)

  Fim do padrão de mensagem "e".

  Este é o padrão de mensagem "es":

  // Noise es
  sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Parâmetros ChaChaPoly para criptografar/descriptografar
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Parâmetros AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, seção de flags/chave estática, ad)

  Fim do padrão de mensagem "es".

  Este é o padrão de mensagem "s":

  // MixHash(ciphertext)
  // Salvar para KDF da Seção de Payload
  h = SHA256(h || ciphertext)

  // Chaves X25519 estáticas de Alice
  ask = GENERATE_PRIVATE()
  apk = DERIVE_PUBLIC(ask)

  Fim do padrão de mensagem "s".


```



### KDF para Seção de Payload (com chave estática de Alice)

```

Este é o padrão de mensagem "ss":

  // Noise ss
  sharedSecret = DH(ask, bpk) = DH(bsk, apk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Parâmetros ChaChaPoly para criptografar/descriptografar
  // chainKey da Seção de Chave Estática
  Define sharedSecret = resultado do DH X25519
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Parâmetros AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, payload, ad)

  Fim do padrão de mensagem "ss".

  // MixHash(ciphertext)
  // Salvar para KDF de Resposta de Nova Sessão
  h = SHA256(h || ciphertext)

```


### KDF para Seção de Payload (sem chave estática de Alice)

Observe que este é um padrão Noise "N", mas usamos o mesmo inicializador "IK"
como para sessões vinculadas.

Mensagens Nova Sessão não podem ser identificadas como contendo a chave estática de Alice ou não
até que a chave estática seja descriptografada e inspecionada para determinar se contém todos os zeros.
Portanto, o receptor deve usar a máquina de estados "IK" para todas
as mensagens Nova Sessão.
Se a chave estática for todos os zeros, o padrão de mensagem "ss" deve ser ignorado.



```

chainKey = da seção de Chave Estática/Flags
  k = da seção de Chave Estática/Flags
  n = 1
  ad = h da seção de Chave Estática/Flags
  ciphertext = ENCRYPT(k, n, payload, ad)

```



### 1g) Formato de Resposta de Nova Sessão

Uma ou mais Respostas de Nova Sessão podem ser enviadas em resposta a uma única mensagem Nova Sessão.
Cada resposta é prefixada com uma tag, que é gerada a partir de um TagSet para a sessão.

A Resposta de Nova Sessão tem duas partes.
A primeira parte é a conclusão do handshake Noise IK com uma tag prefixada.
O comprimento da primeira parte é de 56 bytes.
A segunda parte é o payload da fase de dados.
O comprimento da segunda parte é de 16 + comprimento do payload.

Comprimento total é de 72 + comprimento do payload.
Formato criptografado:

```

+----+----+----+----+----+----+----+----+
  |       Session Tag   8 bytes           |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Chave Pública Efêmera           +
  |                                       |
  +            32 bytes                   +
  |     Codificada com Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticação de Mensagem Poly1305 |
  +  (MAC) para Seção de Chave (sem dados)      +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Seção de Payload            +
  |       Dados criptografados ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticação de Mensagem Poly1305 |
  +         (MAC) para Seção de Payload     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Tag :: 8 bytes, texto claro

  Chave Pública :: 32 bytes, little endian, Elligator2, texto claro

  MAC :: código de autenticação de mensagem Poly1305, 16 bytes
         Nota: Os dados de texto claro ChaCha20 são vazios (ZEROLEN)

  Dados criptografados da Seção de Payload :: dados restantes menos 16 bytes

  MAC :: código de autenticação de mensagem Poly1305, 16 bytes

```

### Session Tag
A tag é gerada no KDF de Session Tags, conforme inicializado
no KDF de Inicialização DH abaixo.
Isso correlaciona a resposta à sessão.
A Session Key da Inicialização DH não é usada.


### Chave Efêmera de Resposta de Nova Sessão

Chave efêmera de Bob.
A chave efêmera é de 32 bytes, codificada com Elligator2, little endian.
Essa chave nunca é reutilizada; uma nova chave é gerada com
cada mensagem, incluindo retransmissões.


### Payload
O comprimento criptografado é o restante dos dados.
O comprimento descriptografado é 16 a menos que o comprimento criptografado.
O payload geralmente conterá um ou mais blocos Garlic Clove.
Consulte a seção de payload abaixo para formato e requisitos adicionais.


### KDF para TagSet de Resposta

Uma ou mais tags são criadas a partir do TagSet, que é inicializado usando
o KDF abaixo, usando o chainKey da mensagem Nova Sessão.

```

// Gera tagset
  tagsetKey = HKDF(chainKey, ZEROLEN, "SessionReplyTags", 32)
  tagset_nsr = DH_INITIALIZE(chainKey, tagsetKey)

```


### KDF para Conteúdo Criptografado da Seção de Chave de Resposta

```

// Chaves da mensagem Nova Sessão
  // Chaves X25519 de Alice
  // apk e aepk são enviadas na mensagem Nova Sessão original
  // ask = chave privada estática de Alice
  // apk = chave pública estática de Alice
  // aesk = chave privada efêmera de Alice
  // aepk = chave pública efêmera de Alice
  // Chaves X25519 estáticas de Bob
  // bsk = chave privada estática de Bob
  // bpk = chave pública estática de Bob

  // Gera a tag
  tagsetEntry = tagset_nsr.GET_NEXT_ENTRY()
  tag = tagsetEntry.SESSION_TAG

  // MixHash(tag)
  h = SHA256(h || tag)

  Este é o padrão de mensagem "e":

  // Chaves X25519 efêmeras de Bob
  besk = GENERATE_PRIVATE_ELG2()
  bepk = DERIVE_PUBLIC(besk)

  // Chave pública efêmera de Bob
  // MixHash(bepk)
  // || abaixo significa concatenar
  h = SHA256(h || bepk);

  // elg2_bepk é enviada em texto claro no
  // início da mensagem Nova Sessão
  elg2_bepk = ENCODE_ELG2(bepk)
  // Como decodificado por Bob
  bepk = DECODE_ELG2(elg2_bepk)

  Fim do padrão de mensagem "e".

  Este é o padrão de mensagem "ee":

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // Parâmetros ChaChaPoly para criptografar/descriptografar
  // chainKey da seção de Payload da Nova Sessão original
  sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
  keydata = HKDF(chainKey, sharedSecret, "", 32)
  chainKey = keydata[0:31]

  Fim do padrão de mensagem "ee".

  Este é o padrão de mensagem "se":

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  sharedSecret = DH(ask, bepk) = DH(besk, apk)
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  chainKey = keydata[0:31]

  // Parâmetros AEAD
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, ZEROLEN, ad)

  Fim do padrão de mensagem "se".

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  chainKey é usado no ratchet abaixo.

```


### KDF para Conteúdo Criptografado da Seção de Payload

Isto é semelhante à primeira mensagem Existing Session,
pós-divisão, mas sem uma tag separada.
Além disso, usamos o hash acima para vincular o
payload à mensagem NSR.


```

// split()
  keydata = HKDF(chainKey, ZEROLEN, "", 64)
  k_ab = keydata[0:31]
  k_ba = keydata[32:63]
  tagset_ab = DH_INITIALIZE(chainKey, k_ab)
  tagset_ba = DH_INITIALIZE(chainKey, k_ba)

  // Parâmetros AEAD para payload de Resposta de Nova Sessão
  k = HKDF(k_ba, ZEROLEN, "AttachPayloadKDF", 32)
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, payload, ad)
```


### Notas

Várias mensagens NSR podem ser enviadas como resposta, cada uma com chaves efêmeras únicas, dependendo do tamanho da resposta.

Alice e Bob são obrigados a usar novas chaves efêmeras para cada mensagem NS e NSR.

Alice deve receber uma das mensagens NSR de Bob antes de enviar mensagens Existing Session (ES),
e Bob deve receber uma mensagem ES de Alice antes de enviar mensagens ES.

O ``chainKey`` e ``k`` da seção de Payload NSR de Bob são usados
como entradas para os ratchets DH ES iniciais (ambas as direções, veja KDF do Ratchet DH).

Bob deve manter apenas sessões Existing para as mensagens ES recebidas de Alice.
Quaisquer outras sessões de entrada e saída criadas (para múltiplos NSRs) devem ser
destruídas imediatamente após receber a primeira mensagem ES de Alice para uma determinada sessão.



### 1h) Formato de Sessão Existente

Session tag (8 bytes)
Dados criptografados e MAC (veja seção 3 abaixo)


### Formato
Criptografado:

```

+----+----+----+----+----+----+----+----+
  |       Session Tag                     |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Seção de Payload            +
  |       Dados criptografados ChaCha20         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticação de Mensagem Poly1305 |
  +              (MAC)                    +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  Session Tag :: 8 bytes, texto claro

  Dados criptografados da Seção de Payload :: dados restantes menos 16 bytes

  MAC :: código de autenticação de mensagem Poly1305, 16 bytes

```


### Payload
O comprimento criptografado é o restante dos dados.
O comprimento descriptografado é 16 a menos que o comprimento criptografado.
Consulte a seção de payload abaixo para formato e requisitos.


KDF

```
Consulte seção AEAD abaixo.

  // Parâmetros AEAD para payload de Sessão Existente
  k = A chave de 32 bytes associada a esta session tag
  n = O número da mensagem N na cadeia atual, conforme recuperado da session tag associada.
  ad = A session tag, 8 bytes
  ciphertext = ENCRYPT(k, n, payload, ad)
```



### 2) ECIES-X25519


Formato: chaves públicas e privadas de 32 bytes, little-endian.

Justificativa: Usado em [NTCP2](/docs/specs/ntcp2/).



### 2a) Elligator2

Em handshakes Noise padrão, as mensagens iniciais de handshake em cada direção começam com
chaves efêmeras que são transmitidas em texto claro.
Como chaves X25519 válidas são distinguíveis de aleatórias, um homem no meio pode distinguir
essas mensagens de mensagens de Sessão Existente que começam com tags de sessão aleatórias.
Em [NTCP2](/docs/specs/ntcp2/) ([Proposal 111](/proposals/111-ntcp-2/)), usamos uma função XOR de baixa sobrecarga usando a chave estática fora de banda para ofuscar
a chave. No entanto, o modelo de ameaça aqui é diferente; não queremos permitir que nenhum MitM
use qualquer meio para confirmar o destino do tráfego, ou para distinguir
as mensagens iniciais de handshake de mensagens de Sessão Existente.

Portanto, [Elligator2](https://elligator.cr.yp.to/) é usado para transformar as chaves efêmeras nas mensagens Nova Sessão e Resposta de Nova Sessão
para que sejam indistinguíveis de strings aleatórias uniformes.



### Formato

Chaves públicas e privadas de 32 bytes.
Chaves codificadas são little endian.

Conforme definido em [Elligator2](https://elligator.cr.yp.to/), as chaves codificadas são indistinguíveis de 254 bits aleatórios.
Requerimos 256 bits aleatórios (32 bytes). Portanto, a codificação e decodificação são
definidas da seguinte forma:

Codificação:

```

Definição ENCODE_ELG2()

  // Codifica conforme definido na especificação Elligator2
  encodedKey = encode(pubkey)
  // OU bit a bit com 2 bits aleatórios no MSB
  randomByte = CSRNG(1)
  encodedKey[31] |= (randomByte & 0xc0)
```


Decodificação:

```

Definição DECODE_ELG2()

  // Mascara 2 bits aleatórios do MSB
  encodedKey[31] &= 0x3f
  // Decodifica conforme definido na especificação Elligator2
  pubkey = decode(encodedKey)
```




### Justificativa

Necessário para impedir que OBEP e IBGW classifiquem o tráfego.


### Notas

Elligator2 dobra em média o tempo de geração de chaves, pois metade das chaves privadas
resulta em chaves públicas inadequadas para codificação com Elligator2.
Além disso, o tempo de geração de chaves é ilimitado com uma distribuição exponencial,
pois o gerador deve continuar tentando até encontrar um par de chaves adequado.

Essa sobrecarga pode ser gerenciada gerando chaves com antecedência,
em uma thread separada, para manter um pool de chaves adequadas.

O gerador faz a função ENCODE_ELG2() para determinar adequação.
Portanto, o gerador deve armazenar o resultado de ENCODE_ELG2()
para que não precise ser calculado novamente.

Além disso, as chaves inadequadas podem ser adicionadas ao pool de chaves
usadas para [NTCP2](/docs/specs/ntcp2/), onde Elligator2 não é usado.
As questões de segurança de fazer isso são TBD.




### 3) AEAD (ChaChaPoly)

AEAD usando ChaCha20 e Poly1305, igual ao [NTCP2](/docs/specs/ntcp2/).
Isso corresponde à [RFC-7539](https://tools.ietf.org/html/rfc7539), que também é
usada de forma semelhante no TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).



### Entradas Nova Sessão e Resposta de Nova Sessão

Entradas para as funções de criptografia/descriptografia
para um bloco AEAD em uma mensagem Nova Sessão:

```

k :: chave de cifra de 32 bytes
       Veja KDFs de Nova Sessão e Resposta de Nova Sessão acima.

  n :: nonce baseado em contador, 12 bytes.
       n = 0

  ad :: dados associados, 32 bytes.
        O hash SHA256 dos dados anteriores, como saída de mixHash()

  data :: dados em texto claro, 0 ou mais bytes

```


### Entradas Sessão Existente

Entradas para as funções de criptografia/descriptografia
para um bloco AEAD em uma mensagem Sessão Existente:

```

k :: chave de sessão de 32 bytes
       Conforme procurado a partir da session tag acompanhante.

  n :: nonce baseado em contador, 12 bytes.
       Começa em 0 e é incrementado para cada mensagem ao transmitir.
       Para o receptor, o valor
       conforme procurado a partir da session tag acompanhante.
       Os primeiros quatro bytes são sempre zero.
       Os últimos oito bytes são o número da mensagem (n), codificados em little-endian.
       Valor máximo é 65535.
       A sessão deve ser ratchetada quando N atingir esse valor.
       Valores superiores nunca devem ser usados.

  ad :: dados associados
        A session tag

  data :: dados em texto claro, 0 ou mais bytes

```


### Formato Criptografado

Saída da função de criptografia, entrada para a função de descriptografia:

```

+----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |       Dados criptografados ChaCha20         |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Código de Autenticação de Mensagem Poly1305 |
  +              (MAC)                    +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+

  dados criptografados :: mesmo tamanho que os dados em texto claro, 0 - 65519 bytes

  MAC :: código de autenticação de mensagem Poly1305, 16 bytes

```

### Notas
- Como ChaCha20 é um cifrador de fluxo, textos claros não precisam ser preenchidos.
  Bytes adicionais de keystream são descartados.

- A chave para o cifrador (256 bits) é acordada por meio do KDF SHA256.
  Os detalhes do KDF para cada mensagem estão em seções separadas abaixo.

- Quadros ChaChaPoly têm tamanho conhecido, pois são encapsulados na mensagem de dados I2NP.

- Para todas as mensagens,
  o preenchimento está dentro do
  quadro de dados autenticados.


### Tratamento de Erros AEAD

Todos os dados recebidos que falharem na verificação AEAD devem ser descartados.
Nenhuma resposta é retornada.


### Justificativa

Usado em [NTCP2](/docs/specs/ntcp2/).



### 4) Ratchets

Ainda usamos session tags, como antes, mas usamos ratchets para gerá-las.
Session tags também tinham uma opção de rekey que nunca implementamos.
Então é como um double ratchet, mas nunca fizemos o segundo.

Aqui definimos algo semelhante ao Double Ratchet do Signal.
As session tags são geradas de forma determinística e idêntica nos
