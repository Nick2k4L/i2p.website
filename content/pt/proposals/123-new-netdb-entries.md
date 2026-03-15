---
title: "Novas Entradas netDB"
number: "123"
author: "zzz, str4d, orignal"
created: "2016-01-16"
lastupdated: "2020-07-18"
status: "Abrir"
thread: "http://zzz.i2p/topics/2051"
supercedes: "110, 120, 121, 122"
toc: true
---
## Status

Partes desta proposta estão completas e implementadas nas versões 0.9.38 e 0.9.39.  
As Estruturas Comuns, I2CP, I2NP e outras especificações  
agora estão atualizadas para refletir as mudanças que são suportadas atualmente.

As partes concluídas ainda estão sujeitas a revisões menores.  
Outras partes desta proposta ainda estão em desenvolvimento  
e sujeitas a revisões substanciais.

A Pesquisa de Serviço (tipos 9 e 11) tem baixa prioridade,  
não está agendada e pode ser separada em uma proposta distinta.


## Visão Geral

Esta é uma atualização e agregação das seguintes 4 propostas:

- 110 LS2
- 120 Meta LS2 para multihoming massivo
- 121 LS2 Criptografado
- 122 Pesquisa de serviço não autenticada (anycasting)

Essas propostas são principalmente independentes, mas, por coerência, definimos e usamos um  
formato comum para várias delas.

As seguintes propostas são parcialmente relacionadas:

- 140 Multihoming Invisível (incompatível com esta proposta)
- 142 Novo Modelo de Criptografia (para nova criptografia simétrica)
- 144 ECIES-X25519-AEAD-Ratchet
- 145 ECIES-P256
- 146 Red25519
- 148 EdDSA-BLAKE2b-Ed25519
- 149 B32 para LS2 Criptografado
- 150 Protocolo Garlic Farm
- 151 ECDSA Blinding


## Proposta

Esta proposta define 5 novos tipos de DatabaseEntry e o processo para  
armazená-los e recuperá-los do banco de dados da rede,  
bem como o método para assiná-los e verificar essas assinaturas.

### Objetivos

- Compatibilidade com versões anteriores
- LS2 utilizável com multihoming no estilo antigo
- Nenhuma nova criptografia ou primitivas necessárias para suporte
- Manter o desacoplamento entre criptografia e assinatura; suportar todas as versões atuais e futuras
- Habilitar chaves de assinatura offline opcionais
- Reduzir a precisão dos timestamps para reduzir fingerprinting
- Habilitar nova criptografia para destinos
- Habilitar multihoming massivo
- Corrigir múltiplos problemas com o LS criptografado existente
- Ofuscação opcional para reduzir a visibilidade pelos floodfills
- Criptografado suporta tanto chave única quanto múltiplas chaves revogáveis
- Pesquisa de serviço para facilitar a busca de outproxies, bootstrap de DHT de aplicação,  
  e outros usos
- Não quebrar nada que dependa de hashes binários de destino de 32 bytes, por exemplo, bittorrent
- Adicionar flexibilidade aos leasesets via propriedades, como temos em routerinfos.
- Colocar o timestamp de publicação e expiração variável no cabeçalho, para funcionar mesmo  
  se o conteúdo estiver criptografado (não derivar timestamp da lease mais antiga)
- Todos os novos tipos residem no mesmo espaço DHT e nas mesmas localizações dos leasesets existentes,  
  para que os usuários possam migrar do LS antigo para o LS2,  
  ou mudar entre LS2, Meta e Criptografado,  
  sem alterar o Destino ou o hash.
- Um Destino existente pode ser convertido para usar chaves offline,  
  ou voltar para chaves online, sem alterar o Destino ou o hash.


### Não-Objetivos / Fora do Escopo

- Novo algoritmo de rotação DHT ou geração de número aleatório compartilhado
- O tipo específico de nova criptografia e esquema de criptografia ponta a ponta  
  para usar esse novo tipo estaria em uma proposta separada.  
  Nenhuma nova criptografia é especificada ou discutida aqui.
- Nova criptografia para RIs ou construção de túneis.  
  Isso estaria em uma proposta separada.
- Métodos de criptografia, transmissão e recepção de mensagens I2NP DLM / DSM / DSRM.  
  Não será alterado.
- Como gerar e suportar Meta, incluindo comunicação inter-roteadores, gerenciamento, failover e coordenação.  
  O suporte pode ser adicionado ao I2CP, ou i2pcontrol, ou um novo protocolo.  
  Isso pode ou não ser padronizado.
- Como realmente implementar e gerenciar túneis com expiração mais longa, ou cancelar túneis existentes.  
  Isso é extremamente difícil, e sem isso, você não pode ter um desligamento gracioso razoável.
- Mudanças no modelo de ameaça
- Formato de armazenamento offline, ou métodos para armazenar/recuperar/compartilhar os dados.
- Detalhes de implementação não são discutidos aqui e são deixados a cada projeto.



### Justificativa

LS2 adiciona campos para alterar o tipo de criptografia e para futuras mudanças de protocolo.

LS2 Criptografado corrige vários problemas de segurança com o LS criptografado existente ao  
usar criptografia assimétrica de todo o conjunto de leases.

Meta LS2 fornece multihoming flexível, eficiente, eficaz e em larga escala.

Registro de Serviço e Lista de Serviço fornecem serviços anycast como pesquisa de nomes  
e bootstrap de DHT.


### Tipos de Dados NetDB

Os números de tipo são usados nas Mensagens I2NP de Pesquisa/Armazenamento no Banco de Dados.

A coluna ponta a ponta refere-se a se consultas/respostas são enviadas a um Destino em uma Mensagem de Alho.


Tipos existentes:

| NetDB Data | Tipo de Pesquisa | Tipo de Armazenamento |
|------------|------------------|-----------------------|
| any        | 0                | any                   |
| LS         | 1                | 1                     |
| RI         | 2                | 0                     |
| exploratory| 3                | DSRM                  |

Novos tipos:

| NetDB Data     | Tipo de Pesquisa | Tipo de Armazenamento | Cabeçalho LS2 Padrão? | Enviado ponta a ponta? |
|----------------|------------------|------------------------|------------------------|------------------------|
| LS2            | 1                | 3                      | sim                    | sim                    |
| LS2 Criptografado  | 1                | 5                      | não                    | não                    |
| Meta LS2       | 1                | 7                      | sim                    | não                    |
| Registro de Serviço | n/a         | 9                      | sim                    | não                    |
| Lista de Serviço   | 4                | 11                     | não                    | não                    |



### Notas

- Os tipos de pesquisa atualmente usam os bits 3-2 na Mensagem de Pesquisa no Banco de Dados.  
  Quaisquer tipos adicionais exigiriam o uso do bit 4.

- Todos os tipos de armazenamento são ímpares, pois os bits superiores no campo de tipo da Mensagem de Armazenamento no Banco de Dados  
  são ignorados por roteadores antigos.  
  Preferimos que a análise falhe como um LS do que como um RI comprimido.

- O tipo deve ser explícito, implícito ou nenhum nos dados cobertos pela assinatura?



### Processo de Pesquisa/Armazenamento

Os tipos 3, 5 e 7 podem ser retornados em resposta a uma pesquisa padrão de leaseset (tipo 1).  
O tipo 9 nunca é retornado em resposta a uma pesquisa.  
O tipo 11 é retornado em resposta a um novo tipo de pesquisa de serviço (tipo 11).

Apenas o tipo 3 pode ser enviado em uma mensagem de Alho cliente-cliente.



### Formato

Os tipos 3, 7 e 9 têm um formato comum::

  Cabeçalho Padrão LS2
  - conforme definido abaixo

  Parte Específica do Tipo
  - conforme definido abaixo em cada parte

  Assinatura Padrão LS2:
  - Comprimento conforme implicado pelo tipo de assinatura da chave de assinatura

O tipo 5 (Criptografado) não começa com um Destino e tem um  
formato diferente. Veja abaixo.

O tipo 11 (Lista de Serviço) é uma agregação de vários Registros de Serviço e tem um  
formato diferente. Veja abaixo.


### Considerações de Privacidade/Segurança

TBD



## Cabeçalho LS2 Padrão

Os tipos 3, 7 e 9 usam o cabeçalho LS2 padrão, especificado abaixo:


### Formato

```
Cabeçalho LS2 Padrão:
  - Tipo (1 byte)
    Não está realmente no cabeçalho, mas faz parte dos dados cobertos pela assinatura.
    Pegue do campo na Mensagem de Armazenamento no Banco de Dados.
  - Destino (387+ bytes)
  - Timestamp de publicação (4 bytes, big endian, segundos desde a época, rola em 2106)
  - Expira (2 bytes, big endian) (deslocamento do timestamp de publicação em segundos, máximo 18,2 horas)
  - Flags (2 bytes)
    Ordem dos bits: 15 14 ... 3 2 1 0
    Bit 0: Se 0, sem chaves offline; se 1, chaves offline
    Bit 1: Se 0, um leaseset publicado padrão.
           Se 1, um leaseset não publicado. Não deve ser inundado, publicado ou
           enviado em resposta a uma consulta. Se este leaseset expirar, não consulte o
           netdb para um novo, a menos que o bit 2 esteja definido.
    Bit 2: Se 0, um leaseset publicado padrão.
           Se 1, este leaseset não criptografado será ofuscado e criptografado ao ser publicado.
           Se este leaseset expirar, consulte a localização ofuscada no netdb para um novo.
           Se este bit for definido como 1, defina também o bit 1 como 1.
           A partir da versão 0.9.42.
    Bits 3-15: defina como 0 para compatibilidade com usos futuros
  - Se a flag indicar chaves offline, a seção de assinatura offline:
    Timestamp de expiração (4 bytes, big endian, segundos desde a época, rola em 2106)
    Tipo de assinatura transitória (2 bytes, big endian)
    Chave pública de assinatura transitória (comprimento conforme implicado pelo tipo de assinatura)
    Assinatura do timestamp de expiração, tipo de assinatura transitória e chave pública,
    pela chave pública do destino,
    comprimento conforme implicado pelo tipo de assinatura da chave pública do destino.
    Esta seção pode, e deve, ser gerada offline.
```

### Justificativa

- Não publicado/publicado: Para uso ao enviar um armazenamento de banco de dados ponta a ponta,  
  o roteador remetente pode desejar indicar que este leaseset não deve ser  
  enviado a outros. Atualmente usamos heurísticas para manter esse estado.

- Publicado: Substitui a lógica complexa necessária para determinar a 'versão' do  
  leaseset. Atualmente, a versão é a expiração da lease com expiração mais longa, e um roteador publicador deve incrementar essa expiração em pelo menos 1ms ao  
  publicar um leaseset que apenas remove uma lease mais antiga.

- Expira: Permite que a expiração de uma entrada netdb seja anterior à  
  de sua lease com expiração mais longa. Pode não ser útil para LS2, onde os leasesets  
  são esperados para permanecer com uma expiração máxima de 11 minutos, mas  
  para outros novos tipos, é necessário (veja Meta LS e Registro de Serviço abaixo).

- Chaves offline são opcionais, para reduzir a complexidade inicial/obrigatória de implementação.


### Problemas

- Poderia reduzir ainda mais a precisão do timestamp (10 minutos?) mas teria que adicionar  
  número de versão. Isso poderia quebrar multihoming, a menos que tivéssemos criptografia que preserva ordem?  
  Provavelmente não é possível sem timestamps.

- Alternativa: timestamp de 3 bytes (época / 10 minutos), versão de 1 byte, expiração de 2 bytes

- O tipo é explícito ou implícito nos dados/assinatura? Constantes "Domínio" para assinatura?


### Notas

- Roteadores não devem publicar um LS mais de uma vez por segundo.  
  Se fizerem, devem artificialmente incrementar o timestamp de publicação em 1  
  em relação ao LS publicado anteriormente.

- Implementações de roteadores poderiam armazenar em cache as chaves e assinatura transitórias para  
  evitar verificação toda vez. Em particular, floodfills e roteadores nas  
  extremidades de conexões de longa duração poderiam se beneficiar disso.

- Chaves e assinatura offline são apropriadas apenas para destinos de longa duração,  
  ou seja, servidores, não clientes.



## Novos tipos DatabaseEntry


### LeaseSet 2

Mudanças do LeaseSet existente:

- Adicionar timestamp de publicação, timestamp de expiração, flags e propriedades
- Adicionar tipo de criptografia
- Remover chave de revogação

Pesquisa com  
    Flag LS padrão (1)  
Armazenar com  
    Tipo LS2 padrão (3)  
Armazenar em  
    Hash do destino  
    Este hash é então usado para gerar a "chave de roteamento" diária, como em LS1  
Expiração típica  
    10 minutos, como em um LS regular.  
Publicado por  
    Destino

### Formato

```
Cabeçalho LS2 Padrão conforme especificado acima

  Parte Específica do Tipo LS2 Padrão
  - Propriedades (Mapeamento conforme especificado na especificação de estruturas comuns, 2 bytes zero se nenhuma)
  - Número de seções de chave a seguir (1 byte, máximo TBD)
  - Seções de chave:
    - Tipo de criptografia (2 bytes, big endian)
    - Comprimento da chave de criptografia (2 bytes, big endian)
      Isso é explícito, para que os floodfills possam analisar LS2 com tipos de criptografia desconhecidos.
    - Chave de criptografia (número de bytes especificado)
  - Número de lease2s (1 byte)
  - Lease2s (40 bytes cada)
    Estas são leases, mas com expiração de 4 bytes em vez de 8 bytes,
    segundos desde a época (rola em 2106)

  Assinatura LS2 Padrão:
  - Assinatura
    Se a flag indicar chaves offline, isso é assinado pela chave pública transitória,
    caso contrário, pela chave pública do destino
    Comprimento conforme implicado pelo tipo de assinatura da chave de assinatura
    A assinatura é de tudo acima.
```


### Justificativa

- Propriedades: Expansão futura e flexibilidade.  
  Colocadas primeiro caso sejam necessárias para análise dos dados restantes.

- Múltiplos pares tipo de criptografia/chave pública são  
  para facilitar a transição para novos tipos de criptografia. A outra maneira de fazer isso  
  é publicar múltiplos leasesets, possivelmente usando os mesmos túneis,  
  como fazemos agora para destinos DSA e EdDSA.  
  A identificação do tipo de criptografia de entrada em um túnel  
  pode ser feita com o mecanismo existente de tag de sessão,  
  e/ou descriptografia por tentativa usando cada chave. Os comprimentos das mensagens  
  de entrada também podem fornecer uma pista.

### Discussão

Esta proposta continua a usar a chave pública no leaseset para a  
chave de criptografia ponta a ponta, e deixa o campo de chave pública no  
Destino não utilizado, como está agora. O tipo de criptografia não é especificado  
no certificado de chave do Destino, permanecerá 0.

Uma alternativa rejeitada é especificar o tipo de criptografia no certificado de chave do Destino,  
usar a chave pública no Destino, e não usar a chave pública  
no leaseset. Não temos planos de fazer isso.

Benefícios do LS2:

- Localização da chave pública real não muda.
- Tipo de criptografia ou chave pública pode mudar sem alterar o Destino.
- Remove o campo de revogação não utilizado
- Compatibilidade básica com outros tipos DatabaseEntry nesta proposta
- Permite múltiplos tipos de criptografia

Desvantagens do LS2:

- Localização da chave pública e tipo de criptografia difere do RouterInfo
- Mantém a chave pública não utilizada no leaseset
- Requer implementação em toda a rede; na alternativa, tipos experimentais de criptografia podem ser usados, se permitidos pelos floodfills  
  (mas veja propostas relacionadas 136 e 137 sobre suporte para tipos de assinatura experimentais).  
  A proposta alternativa poderia ser mais fácil de implementar e testar para tipos experimentais de criptografia.


### Novos Problemas de Criptografia

Alguns pontos estão fora do escopo desta proposta,  
mas estamos colocando notas aqui por enquanto, pois ainda não temos  
uma proposta de criptografia separada.  
Veja também as propostas ECIES 144 e 145.

- O tipo de criptografia representa a combinação  
  de curva, comprimento da chave e esquema ponta a ponta,  
  incluindo KDF e MAC, se houver.

- Incluímos um campo de comprimento da chave, para que o LS2 seja  
  analisável e verificável pelo floodfill mesmo para tipos de criptografia desconhecidos.

- O primeiro novo tipo de criptografia a ser proposto provavelmente será  
  ECIES/X25519. Como ele é usado ponta a ponta  
  (ou uma versão ligeiramente modificada de ElGamal/AES+SessionTag  
  ou algo completamente novo, por exemplo, ChaCha/Poly) será especificado  
  em uma ou mais propostas separadas.  
  Veja também as propostas ECIES 144 e 145.


### Notas

- Expiração de 8 bytes nas leases mudada para 4 bytes.

- Se implementarmos revogação no futuro, podemos fazê-lo com um campo de expiração zero,  
  ou leases zero, ou ambos. Não há necessidade de uma chave de revogação separada.

- As chaves de criptografia estão em ordem de preferência do servidor, a mais preferida primeiro.  
  O comportamento padrão do cliente é selecionar a primeira chave com  
  um tipo de criptografia suportado. Os clientes podem usar outros algoritmos de seleção  
  com base no suporte à criptografia, desempenho relativo e outros fatores.


### LS2 Criptografado

Objetivos:

- Adicionar ofuscação
- Permitir múltiplos tipos de assinatura
- Não exigir nenhuma nova primitiva de criptografia
- Opcionalmente criptografar para cada destinatário, revogável
- Suportar criptografia apenas de LS2 Padrão e Meta LS2

LS2 Criptografado nunca é enviado em uma mensagem de alho ponta a ponta.  
Use o LS2 padrão conforme acima.


Mudanças do LeaseSet Criptografado existente:

- Criptografar tudo por segurança
- Criptografar com segurança, não apenas com AES.
- Criptografar para cada destinatário

Pesquisa com  
    Flag LS padrão (1)  
Armazenar com  
    Tipo LS2 Criptografado (5)  
Armazenar em  
    Hash do tipo de assinatura ofuscado e chave pública ofuscada  
    Tipo de assinatura de 2 bytes (big endian, por exemplo, 0x000b) || chave pública ofuscada  
    Este hash é então usado para gerar a "chave de roteamento" diária, como em LS1  
Expiração típica  
    10 minutos, como em um LS regular, ou horas, como em um meta LS.  
Publicado por  
    Destino


### Definições

Definimos as seguintes funções correspondentes aos blocos criptográficos usados  
para LS2 Criptografado:

CSRNG(n)  
    saída de n bytes de um gerador de números aleatórios criptograficamente seguro.

    Além do requisito de CSRNG ser criptograficamente seguro (e, portanto,  
    adequado para gerar material de chave), ele DEVE ser seguro  
    para que alguma saída de n bytes seja usada como material de chave quando as sequências de bytes imediatamente  
    anteriores e posteriores a ela forem expostas na rede (como em um sal, ou preenchimento criptografado). Implementações que dependem de uma fonte potencialmente não confiável devem hash  
    qualquer saída que será exposta na rede. Veja [referências PRNG](http://projectbullrun.org/dual-ec/ext-rand.html) e [discussão de desenvolvedores do Tor](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html).

H(p, d)  
    Função de hash SHA-256 que recebe uma string de personalização p e dados d, e  
    produz uma saída de 32 bytes.

    Use SHA-256 da seguinte forma::

        H(p, d) := SHA-256(p || d)

STREAM  
    O cifra de fluxo ChaCha20 conforme especificado em [RFC 7539 Seção 2.4](https://tools.ietf.org/html/rfc7539#section-2.4), com o contador inicial  
    definido como 1. S_KEY_LEN = 32 e S_IV_LEN = 12.

    ENCRYPT(k, iv, plaintext)  
        Criptografa plaintext usando a chave de cifra k e o nonce iv, que DEVE ser único para  
        a chave k. Retorna um texto cifrado do mesmo tamanho que o plaintext.

        Todo o texto cifrado deve ser indistinguível de aleatório se a chave for secreta.

    DECRYPT(k, iv, ciphertext)  
        Descriptografa ciphertext usando a chave de cifra k e o nonce iv. Retorna o plaintext.


SIG  
    O esquema de assinatura RedDSA (correspondente ao SigType 11) com ofuscação de chave.  
    Ele tem as seguintes funções:

    DERIVE_PUBLIC(privkey)  
        Retorna a chave pública correspondente à chave privada fornecida.

    SIGN(privkey, m)  
        Retorna uma assinatura pela chave privada privkey sobre a mensagem m fornecida.

    VERIFY(pubkey, m, sig)  
        Verifica a assinatura sig contra a chave pública pubkey e a mensagem m. Retorna  
        verdadeiro se a assinatura for válida, falso caso contrário.

    Ele também deve suportar as seguintes operações de ofuscação de chave:

    GENERATE_ALPHA(data, secret)  
        Gera alpha para quem conhece os dados e um segredo opcional.  
        O resultado deve ter distribuição idêntica às chaves privadas.

    BLIND_PRIVKEY(privkey, alpha)  
        Ofusca uma chave privada, usando um segredo alpha.

    BLIND_PUBKEY(pubkey, alpha)  
        Ofusca uma chave pública, usando um segredo alpha.  
        Para um par de chaves (privkey, pubkey) dado, a seguinte relação se mantém::

            BLIND_PUBKEY(pubkey, alpha) ==
            DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))

DH  
    Sistema de acordo de chave pública X25519. Chaves privadas de 32 bytes, chaves públicas de 32  
    bytes, produz saídas de 32 bytes. Ele tem as seguintes  
    funções:

    GENERATE_PRIVATE()  
        Gera uma nova chave privada.

    DERIVE_PUBLIC(privkey)  
        Retorna a chave pública correspondente à chave privada fornecida.

    DH(privkey, pubkey)  
        Gera um segredo compartilhado a partir das chaves privada e pública fornecidas.

HKDF(salt, ikm, info, n)  
    Uma função criptográfica de derivação de chave que recebe material de chave de entrada ikm (que  
    deve ter boa entropia, mas não é necessário ser uma string uniformemente aleatória), um sal  
    de 32 bytes, e um valor 'info' específico do contexto, e produz uma saída  
    de n bytes adequada para uso como material de chave.

    Use HKDF conforme especificado em [RFC 5869](https://tools.ietf.org/html/rfc5869), usando a função de hash HMAC SHA-256  
    conforme especificado em [RFC 2104](https://tools.ietf.org/html/rfc2104). Isso significa que SALT_LEN é no máximo 32 bytes.


### Formato

O formato LS2 criptografado consiste em três camadas aninhadas:

- Uma camada externa contendo as informações em texto claro necessárias para armazenamento e recuperação.
- Uma camada intermediária que lida com autenticação do cliente.
- Uma camada interna que contém os dados reais do LS2.

O formato geral é::

    Dados da camada 0 + Enc(dados da camada 1 + Enc(dados da camada 2)) + Assinatura

Observe que o LS2 criptografado é ofuscado. O Destino não está no cabeçalho.  
A localização de armazenamento DHT é SHA-256(tipo de assinatura || chave pública ofuscada), e rotacionada diariamente.

NÃO usa o cabeçalho LS2 padrão especificado acima.

#### Camada 0 (externa)
Tipo  
    1 byte

    Não está realmente no cabeçalho, mas faz parte dos dados cobertos pela assinatura.  
    Pegue do campo na Mensagem de Armazenamento no Banco de Dados.

Tipo de Assinatura da Chave Pública Ofuscada  
    2 bytes, big endian  
    Isso sempre será o tipo 11, identificando uma chave Red25519 ofuscada.

Chave Pública Ofuscada  
    Comprimento conforme implicado pelo tipo de assinatura

Timestamp de publicação  
    4 bytes, big endian

    Segundos desde a época, rola em 2106

Expira  
    2 bytes, big endian

    Deslocamento do timestamp de publicação em segundos, máximo 18,2 horas

Flags  
    2 bytes

    Ordem dos bits: 15 14 ... 3 2 1 0

    Bit 0: Se 0, sem chaves offline; se 1, chaves offline

    Outros bits: defina como 0 para compatibilidade com usos futuros

Dados da chave transitória  
    Presente se a flag indicar chaves offline

    Timestamp de expiração  
        4 bytes, big endian

        Segundos desde a época, rola em 2106

    Tipo de assinatura transitória  
        2 bytes, big endian

    Chave pública de assinatura transitória  
        Comprimento conforme implicado pelo tipo de assinatura

    Assinatura  
        Comprimento conforme implicado pelo tipo de assinatura da chave pública ofuscada

        Sobre o timestamp de expiração, tipo de assinatura transitória e chave pública transitória.

        Verificada com a chave pública ofuscada.

lenOuterCiphertext  
    2 bytes, big endian

outerCiphertext  
    lenOuterCiphertext bytes

    Dados da camada 1 criptografados. Veja abaixo para algoritmos de derivação de chave e criptografia.

Assinatura  
    Comprimento conforme implicado pelo tipo de assinatura da chave de assinatura usada

    A assinatura é de tudo acima.

    Se a flag indicar chaves offline, a assinatura é verificada com a chave pública transitória.  
    Caso contrário, a assinatura é verificada com a chave pública ofuscada.


#### Camada 1 (intermediária)
Flags  
    1 byte
    
    Ordem dos bits: 76543210

    Bit 0: 0 para todos, 1 para por cliente, seção de autenticação a seguir

    Bits 3-1: Esquema de autenticação, apenas se o bit 0 for definido como 1 para por cliente, caso contrário 000  
              000: Autenticação de cliente DH (ou sem autenticação por cliente)  
              001: Autenticação de cliente PSK

    Bits 7-4: Não utilizados, defina como 0 para compatibilidade futura

Dados de autenticação de cliente DH  
    Presente se o bit 0 da flag for definido como 1 e os bits 3-1 da flag forem definidos como 000.

    ephemeralPublicKey  
        32 bytes

    clients  
        2 bytes, big endian

        Número de entradas authClient a seguir, 40 bytes cada

    authClient  
        Dados de autorização para um único cliente.  
        Veja abaixo para o algoritmo de autorização por cliente.

        clientID_i  
            8 bytes

        clientCookie_i  
            32 bytes

Dados de autenticação de cliente PSK  
    Presente se o bit 0 da flag for definido como 1 e os bits 3-1 da flag forem definidos como 001.

    authSalt  
        32 bytes

    clients  
        2 bytes, big endian

        Número de entradas authClient a seguir, 40 bytes cada

    authClient  
        Dados de autorização para um único cliente.  
        Veja abaixo para o algoritmo de autorização por cliente.

        clientID_i  
            8 bytes

        clientCookie_i  
            32 bytes


innerCiphertext  
    Comprimento implícito por lenOuterCiphertext (quaisquer dados restantes)

    Dados da camada 2 criptografados. Veja abaixo para algoritmos de derivação de chave e criptografia.


#### Camada 2 (interna)
Tipo  
    1 byte

    Ou 3 (LS2) ou 7 (Meta LS2)

Dados  
    Dados LeaseSet2 para o tipo dado.

    Inclui o cabeçalho e a assinatura.


### Derivação de Chave Ofuscada

Usamos o seguinte esquema para ofuscação de chave,  
baseado em Ed25519 e [ZCash RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf).  
As assinaturas Re25519 são sobre a curva Ed25519, usando SHA-512 para o hash.

Não usamos [Tor's rend-spec-v3.txt appendix A.2](https://spec.torproject.org/rend-spec-v3),  
que tem objetivos de design semelhantes, porque suas chaves públicas ofuscadas  
podem estar fora do subgrupo de ordem prima, com implicações de segurança desconhecidas.


#### Objetivos

- A chave pública de assinatura no destino não ofuscado deve ser  
  Ed25519 (tipo de assinatura 7) ou Red25519 (tipo de assinatura 11);  
  nenhum outro tipo de assinatura é suportado  
- Se a chave pública de assinatura estiver offline, a chave pública de assinatura transitória também deve ser Ed25519  
- Ofuscação é computacionalmente simples  
- Usar primitivas criptográficas existentes  
- Chaves públicas ofuscadas não podem ser desofuscadas  
- Chaves públicas ofuscadas devem estar na curva Ed25519 e no subgrupo de ordem prima  
- Deve-se conhecer a chave pública de assinatura do destino  
  (destino completo não necessário) para derivar a chave pública ofuscada  
- Opcionalmente fornecer um segredo adicional necessário para derivar a chave pública ofuscada


#### Segurança

A segurança de um esquema de ofuscação requer que a  
distribuição de alpha seja a mesma das chaves privadas não ofuscadas.  
No entanto, quando ofuscamos uma chave privada Ed25519 (tipo de assinatura 7)  
para uma chave privada Red25519 (tipo de assinatura 11), a distribuição é diferente.  
Para atender aos requisitos da [zcash seção 4.1.6.1](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf),  
Red25519 (tipo de assinatura 11) deve ser usado também para as chaves não ofuscadas, para que  
"a combinação de uma chave pública re-randomizada e assinatura(s)  
sob essa chave não revele a chave da qual foi re-randomizada."  
Permitimos o tipo 7 para destinos existentes, mas recomendamos  
o tipo 11 para novos destinos que serão criptografados.



#### Definições

B  
    O ponto base Ed25519 (gerador) 2^255 - 19 conforme em [Ed25519](http://cr.yp.to/papers.html#ed25519)

L  
    A ordem Ed25519 2^252 + 27742317777372353535851937790883648493  
    conforme em [Ed25519](http://cr.yp.to/papers.html#ed25519)

DERIVE_PUBLIC(a)  
    Converte uma chave privada em pública, conforme em Ed25519 (multiplica por G)

alpha  
    Um número aleatório de 32 bytes conhecido por quem conhece o destino.

GENERATE_ALPHA(destination, date, secret)  
    Gera alpha para a data atual, para quem conhece o destino e o segredo.  
    O resultado deve ter distribuição idêntica às chaves privadas Ed25519.

a  
    A chave privada de assinatura EdDSA ou RedDSA de 32 bytes não ofuscada usada para assinar o destino

A  
    A chave pública de assinatura EdDSA ou RedDSA de 32 bytes não ofuscada no destino,  
    = DERIVE_PUBLIC(a), conforme em Ed25519

a'  
    A chave privada de assinatura EdDSA ofuscada de 32 bytes usada para assinar o leaseset criptografado  
    Esta é uma chave privada EdDSA válida.

A'  
    A chave pública de assinatura EdDSA ofuscada de 32 bytes no Destino,  
    pode ser gerada com DERIVE_PUBLIC(a'), ou a partir de A e alpha.  
    Esta é uma chave pública EdDSA válida, na curva e no subgrupo de ordem prima.

LEOS2IP(x)  
    Inverte a ordem dos bytes de entrada para little-endian

H*(x)  
    32 bytes = (LEOS2IP(SHA512(x))) mod B, igual ao hash-and-reduce em Ed25519


#### Cálculos de Ofuscação

Uma nova chave secreta alpha e chaves ofuscadas devem ser geradas a cada dia (UTC).  
A chave secreta alpha e as chaves ofuscadas são calculadas da seguinte forma.

GENERATE_ALPHA(destination, date, secret), para todas as partes:

```text
// GENERATE_ALPHA(destination, date, secret)

  // segredo é opcional, senão comprimento zero
  A = chave pública de assinatura do destino
  stA = tipo de assinatura de A, 2 bytes big endian (0x0007 ou 0x000b)
  stA' = tipo de assinatura da chave pública ofuscada A', 2 bytes big endian (0x000b)
  keydata = A || stA || stA'
  datestring = 8 bytes ASCII YYYYMMDD da data atual UTC
  segredo = string codificada em UTF-8
  seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || segredo, "i2pblinding1", 64)
  // trate seed como um valor little-endian de 64 bytes
  alpha = seed mod L
```

BLIND_PRIVKEY(), para o proprietário publicando o leaseset:

```text
// BLIND_PRIVKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  // Se para uma chave privada Ed25519 (tipo 7)
  seed = chave privada de assinatura do destino
  a = metade esquerda de SHA512(seed) e ajustada conforme o usual para Ed25519
  // senão, para uma chave privada Red25519 (tipo 11)
  a = chave privada de assinatura do destino
  // Adição usando aritmética escalar
  chave privada de assinatura ofuscada = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
  chave pública de assinatura ofuscada = A' = DERIVE_PUBLIC(a')
```

BLIND_PUBKEY(), para os clientes recuperando o leaseset:

```text
// BLIND_PUBKEY()

  alpha = GENERATE_ALPHA(destination, date, secret)
  A = chave pública de assinatura do destino
  // Adição usando elementos de grupo (pontos na curva)
  chave pública ofuscada = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```

Ambos os métodos de cálculo de A' produzem o mesmo resultado, conforme exigido.



#### Assinatura

O leaseset não ofuscado é assinado pela chave privada de assinatura Ed25519 ou Red25519 não ofuscada  
e verificado com a chave pública de assinatura Ed25519 ou Red25519 não ofuscada (tipos de assinatura 7 ou 11) conforme o usual.

Se a chave pública de assinatura estiver offline,  
o leaseset não ofuscado é assinado pela chave privada de assinatura transitória Ed25519 ou Red25519 não ofuscada  
e verificado com a chave pública de assinatura transitória Ed25519 ou Red25519 não ofuscada (tipos de assinatura 7 ou 11) conforme o usual.  
Veja abaixo para notas adicionais sobre chaves offline para leasesets criptografados.

Para assinatura do leaseset criptografado, usamos Red25519, baseado em [RedDSA](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)  
para assinar e verificar com chaves ofuscadas.  
As assinaturas Red25519 são sobre a curva Ed25519, usando SHA-512 para o hash.

Red25519 é idêntico ao Ed25519 padrão, exceto conforme especificado abaixo.


#### Cálculos de Assinatura/Verificação

A parte externa do leaseset criptografado usa chaves e assinaturas Red25519.

Red25519 é quase idêntico ao Ed25519. Existem duas diferenças:

Chaves privadas Red25519 são geradas a partir de números aleatórios e então devem ser reduzidas mod L, onde L é definido acima.  
Chaves privadas Ed25519 são geradas a partir de números aleatórios e então "ajustadas" usando  
máscara bit a bit para os bytes 0 e 31. Isso não é feito para Red25519.  
As funções GENERATE_ALPHA() e BLIND_PRIVKEY() definidas acima geram chaves privadas Red25519 adequadas usando mod L.

Em Red25519, o cálculo de r para assinatura usa dados aleatórios adicionais,  
e usa o valor da chave pública em vez do hash da chave privada.  
Por causa dos dados aleatórios, cada assinatura Red25519 é diferente, mesmo  
ao assinar os mesmos dados com a mesma chave.

Assinatura:

```text
T = 80 bytes aleatórios
  r = H*(T || publickey || message)
  // resto é o mesmo que em Ed25519
```

Verificação:

```text
// mesmo que em Ed25519
```



### Criptografia e processamento

#### Derivação de subcredenciais
Como parte do processo de ofuscação, precisamos garantir que um LS2 criptografado só possa ser  
descriptografado por alguém que conheça a chave pública de assinatura do Destino correspondente.  
O Destino completo não é necessário.  
Para alcançar isso, derivamos uma credencial a partir da chave pública de assinatura:

```text
A = chave pública de assinatura do destino
  stA = tipo de assinatura de A, 2 bytes big endian (0x0007 ou 0x000b)
  stA' = tipo de assinatura de A', 2 bytes big endian (0x000b)
  keydata = A || stA || stA'
  credential = H("credential", keydata)
```

A string de personalização garante que a credencial não colida com nenhum hash usado  
como chave de pesquisa DHT, como o hash simples do Destino.

Para uma chave ofuscada dada, podemos então derivar uma subcredencial:

```text
subcredential = H("subcredential", credential || blindedPublicKey)
```

A subcredencial é incluída nos processos de derivação de chave abaixo, o que vincula essas  
chaves ao conhecimento da chave pública de assinatura do Destino.

#### Criptografia da Camada 1
Primeiro, a entrada para o processo de derivação de chave é preparada:

```text
outerInput = subcredential || publishedTimestamp
```

Em seguida, um sal aleatório é gerado:

```text
outerSalt = CSRNG(32)
```

Então a chave usada para criptografar a camada 1 é derivada:

```text
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
  outerKey = keys[0:31]
  outerIV = keys[32:43]
```

Finalmente, o texto claro da camada 1 é criptografado e serializado:

```text
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```

#### Descriptografia da Camada 1
O sal é analisado a partir do texto cifrado da camada 1:

```text
outerSalt = outerCiphertext[0:31]
```

Então a chave usada para criptografar a camada 1 é derivada:

```text
outerInput = subcredential || publishedTimestamp
  keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
  outerKey = keys[0:31]
  outerIV = keys[32:43]
```

Finalmente, o texto cifrado da camada 1 é descriptografado:

```text
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```

#### Criptografia da Camada 2
Quando a autorização do cliente está habilitada, ``authCookie`` é calculado conforme descrito abaixo.  
Quando a autorização do cliente está desabilitada, ``authCookie`` é o array de bytes de comprimento zero.

A criptografia prossegue de forma semelhante à camada 1:

```text
innerInput = authCookie || subcredential || publishedTimestamp
  innerSalt = CSRNG(32)
  keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
  innerKey = keys[0:31]
  innerIV = keys[32:43]
  innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```

#### Descriptografia da Camada 2
Quando a autorização do cliente está habilitada, ``authCookie`` é calculado conforme descrito abaixo.  
Quando a autorização do cliente está desabilitada, ``authCookie`` é o array de bytes de comprimento zero.

A descriptografia prossegue de forma semelhante à camada 1:

```text
innerInput = authCookie || subcredential || publishedTimestamp
  innerSalt = innerCiphertext[0:31]
  keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
  innerKey = keys[0:31]
  innerIV = keys[32:43]
  innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```


### Autorização por cliente

Quando a autorização do cliente está habilitada para um Destino, o servidor mantém uma lista de  
clientes que estão autorizados a descriptografar os dados do LS2 criptografado. Os dados armazenados por cliente  
dependem do mecanismo de autorização e incluem alguma forma de material de chave que cada  
cliente gera e envia ao servidor por um mecanismo seguro fora da banda.

Existem duas alternativas para implementar a autorização por cliente:

#### Autorização de cliente DH
Cada cliente gera um par de chaves DH ``[csk_i, cpk_i]``, e envia a chave pública ``cpk_i``  
ao servidor.

Processamento do servidor  
^^^^^^^^^^^^^^^^^
O servidor gera um novo ``authCookie`` e um par de chaves DH efêmero:

```text
authCookie = CSRNG(32)
  esk = GENERATE_PRIVATE()
  epk = DERIVE_PUBLIC(esk)
```

Então, para cada cliente autorizado, o servidor criptografa ``authCookie`` para sua chave pública:

```text
sharedSecret = DH(esk, cpk_i)
  authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
  okm = HKDF(epk, authInput, "ELS2_XCA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
  clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```

O servidor coloca cada tupla ``[clientID_i, clientCookie_i]`` na  
camada 1 do LS2 criptografado, junto com ``epk``.

Processamento do cliente  
^^^^^^^^^^^^^^^^^
O cliente usa sua chave privada para derivar seu identificador de cliente esperado ``clientID_i``,  
chave de criptografia ``clientKey_i`` e IV de criptografia ``clientIV_i``:

```text
sharedSecret = DH(csk_i, epk)
  authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
  okm = HKDF(epk, authInput, "ELS2_XCA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
```

Então o cliente procura nos dados de autorização da camada 1 uma entrada que contenha  
``clientID_i``. Se uma entrada correspondente existir, o cliente a descriptografa para obter  
``authCookie``:

```text
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```

#### Autorização de cliente com chave pré-compartilhada
Cada cliente gera uma chave secreta de 32 bytes ``psk_i``, e a envia ao servidor.  
Alternativamente, o servidor pode gerar a chave secreta e enviá-la a um ou mais clientes.


Processamento do servidor  
^^^^^^^^^^^^^^^^^
O servidor gera um novo ``authCookie`` e sal:

```text
authCookie = CSRNG(32)
  authSalt = CSRNG(32)
```

Então, para cada cliente autorizado, o servidor criptografa ``authCookie`` para sua chave pré-compartilhada:

```text
authInput = psk_i || subcredential || publishedTimestamp
  okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
  clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```

O servidor coloca cada tupla ``[clientID_i, clientCookie_i]`` na  
camada 1 do LS2 criptografado, junto com ``authSalt``.

Processamento do cliente  
^^^^^^^^^^^^^^^^^
O cliente usa sua chave pré-compartilhada para derivar seu identificador de cliente esperado ``clientID_i``,  
chave de criptografia ``clientKey_i`` e IV de criptografia ``clientIV_i``:

```text
authInput = psk_i || subcredential || publishedTimestamp
  okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
  clientKey_i = okm[0:31]
  clientIV_i = okm[32:43]
  clientID_i = okm[44:51]
```

Então o cliente procura nos dados de autorização da camada 1 uma entrada que contenha  
``clientID_i``. Se uma entrada correspondente existir, o cliente a descriptografa para obter  
``authCookie``:

```text
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```

#### Considerações de segurança
Ambos os mecanismos de autorização de cliente acima fornecem privacidade para a associação de clientes.  
Uma entidade que conhece apenas o Destino pode ver quantos clientes estão inscritos em um determinado  
momento, mas não pode rastrear quais clientes estão sendo adicionados ou revogados.

Os servidores DEVEM embaralhar a ordem dos clientes cada vez que geram um LS2 criptografado, para  
impedir que os clientes descubram sua posição na lista e infiram quando outros clientes foram adicionados ou revogados.

Um servidor PODE optar por ocultar o número de clientes inscritos inserindo entradas aleatórias na  
lista de dados de autorização.

Vantagens da autorização de cliente DH  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- A segurança do esquema não depende exclusivamente da troca fora da banda do material de chave do cliente. A chave privada do cliente nunca precisa sair de seu dispositivo, e assim um  
  adversário que consiga interceptar a troca fora da banda, mas não consiga quebrar o algoritmo DH,  
  não poderá descriptografar o LS2 criptografado, nem determinar por quanto tempo o cliente tem acesso.

Desvantagens da autorização de cliente DH  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Requer N + 1 operações DH no lado do servidor para N clientes.
- Requer uma operação DH no lado do cliente.
- Requer que o cliente gere a chave secreta.

Vantagens da autorização de cliente PSK  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Não requer operações DH.
- Permite que o servidor gere a chave secreta.
- Permite que o servidor compartilhe a mesma chave com vários clientes, se desejado.

Desvantagens da autorização de cliente PSK  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- A segurança do esquema depende criticamente da troca fora da banda do material de chave do cliente. Um adversário que intercepte a troca para um cliente específico pode descriptografar  
  qualquer LS2 criptografado subsequente para o qual esse cliente esteja autorizado, bem como determinar  
  quando o acesso do cliente é revogado.


### LS Criptografado com Endereços Base 32

Veja a proposta 149.

Você não pode usar um LS2 criptografado para bittorrent, por causa das respostas compactas de anúncio que têm 32 bytes.  
Os 32 bytes contêm apenas o hash. Não há espaço para indicar que o  
leaseset está criptografado, ou os tipos de assinatura.



### LS Criptografado com Chaves Offline

Para leasesets criptografados com chaves offline, as chaves privadas ofuscadas também devem ser geradas offline,  
uma para cada dia.

Como o bloco opcional de assinatura offline está na parte em texto claro do leaseset criptografado,  
qualquer pessoa que colete dados dos floodfills poderia usar isso para rastrear o leaseset (mas não descriptografá-lo)  
por vários dias.  
Para evitar isso, o proprietário das chaves deve gerar novas chaves transitórias  
para cada dia também.  
Ambas as chaves transitórias e ofuscadas podem ser geradas com antecedência e entregues ao roteador  
em lote.

Não há formato de arquivo definido nesta proposta para empacotar múltiplas chaves transitórias e  
ofuscadas e fornecê-las ao cliente ou roteador.  
Não há melhoria no protocolo I2CP definida nesta proposta para suportar  
leasesets criptografados com chaves offline.



### Notas

- Um serviço usando leasesets criptografados publicaria a versão criptografada nos  
  floodfills. No entanto, por eficiência, enviaria leasesets não criptografados aos  
  clientes na mensagem de alho encapsulada, uma vez autenticado (via lista branca, por  
  exemplo).

- Floodfills podem limitar o tamanho máximo a um valor razoável para evitar abusos.

- Após a descriptografia, várias verificações devem ser feitas, incluindo que  
  o timestamp interno e a expiração correspondam aos do nível superior.

- ChaCha20 foi selecionado em vez de AES. Embora as velocidades sejam semelhantes se o  
  suporte de hardware AES estiver disponível, ChaCha20 é 2,5-3 vezes mais rápido quando  
  o suporte de hardware AES não está disponível, como em dispositivos ARM de baixo desempenho.

- Não nos preocupamos o suficiente com velocidade para usar BLAKE2b com chave. Ele tem um tamanho de saída  
  grande o suficiente para acomodar o maior n que exigimos (ou podemos chamá-lo uma vez por  
  chave desejada com um argumento contador). BLAKE2b é muito mais rápido que SHA-256, e  
  BLAKE2b com chave reduziria o número total de chamadas à função hash.  
  No entanto, veja a proposta 148, onde é proposto que mudemos para BLAKE2b por outros motivos.  
  Veja [Secure key derivation performance](https://www.lvh.io/posts/secure-key-derivation-performance.html).


### Meta LS2

Isso é usado para substituir multihoming. Como qualquer leaseset, isso é assinado pelo  
criador. É uma lista autenticada de hashes de destino.

O Meta LS2 é o topo de, e possivelmente nós intermediários de,  
uma estrutura em árvore.  
Contém vários registros, cada um apontando para um LS, LS2 ou outro Meta LS2  
para suportar multihoming massivo.  
Um Meta LS2 pode conter uma mistura de entradas LS, LS2 e Meta LS2.  
As folhas da árvore são sempre um LS ou LS2.  
A árvore é um DAG; loops são proibidos; clientes que fazem pesquisas devem detectar e  
recusar-se a seguir loops.

Um Meta LS2 pode ter uma expiração muito mais longa que um LS ou LS2 padrão.  
O nível superior pode ter uma expiração várias horas após a data de publicação.  
O tempo máximo de expiração será imposto por floodfills e clientes, e é TBD.

O caso de uso para Meta LS2 é multihoming massivo, mas sem mais  
proteção contra correlação de roteadores com leasesets (na reinicialização do roteador) do que  
é fornecida atualmente com LS ou LS2.  
Isso é equivalente ao caso de uso "facebook", que provavelmente não precisa  
de proteção contra correlação. Este caso de uso provavelmente precisa de chaves offline,  
que são fornecidas no cabeçalho padrão em cada nó da árvore.

O protocolo de back-end para coordenação entre os roteadores folha, signatários intermediários e mestres do Meta LS  
não é especificado aqui. Os requisitos são extremamente simples - apenas verificar se o peer está ativo,  
e publicar um novo LS a cada poucas horas. A única complexidade é para escolher novos  
publicadores para os Meta LS de nível superior ou intermediário em caso de falha.

Leasesets mistos onde leases de múltiplos roteadores são combinados, assinados e publicados  
em um único leaseset são documentados na proposta 140, "multihoming invisível".  
Esta proposta é inviável como escrita, porque conexões de streaming não seriam  
"aderentes" a um único roteador, veja http://zzz.i2p/topics/2335 .

O protocolo de back-end, e a interação com os componentes internos do roteador e cliente, seria  
muito complexo para multihoming invisível.

Para evitar sobrecarregar o floodfill para o Meta LS de nível superior, a expiração deve  
ser de várias horas no mínimo. Os clientes devem armazenar em cache o Meta LS de nível superior e mantê-lo  
entre reinicializações se não expirado.

Precisamos definir algum algoritmo para os clientes percorrerem a árvore, incluindo fallbacks,  
para que o uso seja disperso. Alguma função de distância de hash, custo e aleatoriedade.  
Se um nó tiver tanto LS ou LS2 quanto Meta LS, precisamos saber quando é permitido  
usar esses leasesets, e quando continuar percorrendo a árvore.




Pesquisa com  
    Flag LS padrão (1)  
Armazenar com  
    Tipo Meta LS2 (7)  
Armazenar em  
    Hash do destino  
    Este hash é então usado para gerar a "chave de roteamento" diária, como em LS1  
Expiração típica  
    Horas. Máximo 18,2 horas (65535 segundos)  
Publicado por  
    Destino "mestre" ou coordenador, ou coordenadores intermediários

### Formato

```
Cabeçalho LS2 Padrão conforme especificado acima

  Parte Específica do Tipo Meta LS2
  - Propriedades (Mapeamento conforme especificado na especificação de estruturas comuns, 2 bytes zero se nenhuma)
  - Número de entradas (1 byte) Máximo TBD
  - Entradas. Cada entrada contém: (40 bytes)
    - Hash (32 bytes)
    - Flags (2 bytes)
      TBD. Defina todos como zero para compatibilidade com usos futuros.
    - Tipo (1 byte) O tipo de LS ao qual está se referindo;  
      1 para LS, 3 para LS2, 5 para criptografado, 7 para meta, 0 para desconhecido.
    - Custo (prioridade) (1 byte)
    - Expira (4 bytes) (4 bytes, big endian, segundos desde a época, rola em 2106)
  - Número de revogações (1 byte) Máximo TBD
  - Revogações: Cada revogação contém: (32 bytes)
    - Hash (32 bytes)

  Assinatura LS2 Padrão:
  - Assinatura (40+ bytes)
    A assinatura é de tudo acima.
```

Flags e propriedades: para uso futuro


### Notas

- Um serviço distribuído usando isso teria um ou mais "mestres" com a  
  chave privada do destino do serviço. Eles (fora da banda) determinariam a  
  lista atual de destinos ativos e publicariam o Meta LS2. Para  
  redundância, múltiplos mestres poderiam multihoming (ou seja, publicar simultaneamente) o  
  Meta LS2.

- Um serviço distribuído poderia começar com um único destino ou usar multihoming no estilo antigo,  
  então migrar para um Meta LS2. Uma pesquisa LS padrão poderia retornar  
  qualquer um de LS, LS2 ou Meta LS2.

- Quando um serviço usa um Meta LS2, ele não tem túneis (leases).


### Registro de Serviço

Este é um registro individual dizendo que um destino está participando de um  
serviço. É enviado do participante para o floodfill. Nunca é enviado  
individualmente por um floodfill, mas apenas como parte de uma Lista de Serviço. O Registro de Serviço também é usado para revogar a participação em um serviço, definindo a  
expiração como zero.

Isso não é um LS2, mas usa o formato padrão de cabeçalho e assinatura LS2.

Pesquisa com  
    n/a, veja Lista de Serviço  
Armazenar com  
    Tipo Registro de Serviço (9)  
Armazenar em  
    Hash do nome do serviço  
    Este hash é então usado para gerar a "chave de roteamento" diária, como em LS1  
Expiração típica  
    Horas. Máximo 18,2 horas (65535 segundos)  
Publicado por  
    Destino

### Formato

```
Cabeçalho LS2 Padrão conforme especificado acima

  Parte Específica do Tipo Registro de Serviço
  - Porta (2 bytes, big endian) (0 se não especificada)
  - Hash do nome do serviço (32 bytes)

  Assinatura LS2 Padrão:
  - Assinatura (40+ bytes)
    A assinatura é de tudo acima.
```

### Notas

- Se expira for todo zero, o floodfill deve revogar o registro e não incluí-lo mais  
  na lista de serviço.

- Armazenamento: O floodfill pode limitar estritamente o armazenamento desses registros e  
  limitar o número de registros armazenados por hash e sua expiração. Uma lista branca  
  de hashes também pode ser usada.

- Qualquer outro tipo netdb no mesmo hash tem prioridade, então um registro de serviço nunca pode  
  sobrescrever um LS/RI, mas um LS/RI sobrescreverá todos os registros de serviço nesse hash.



### Lista de Serviço

Isso não é nada parecido com um LS2 e usa um formato diferente.

A lista de serviço é criada e assinada pelo floodfill. É não autenticada  
no sentido de que qualquer pessoa pode participar de um serviço publicando um Registro de Serviço para um  
floodfill.

Uma Lista de Serviço contém Registros de Serviço Curto, não Registros de Serviço completos. Estes  
contêm assinaturas, mas apenas hashes, não destinos completos, então não podem ser  
verificados sem o destino completo.

A segurança, se houver, e a desejabilidade das listas de serviço são TBD.  
Floodfills poderiam limitar publicação e pesquisas a uma lista branca de serviços,  
mas essa lista branca pode variar com base na implementação ou preferência do operador.  
Pode não ser possível alcançar consenso sobre uma lista branca comum e básica  
entre implementações.

Se o nome do serviço estiver incluído no registro de serviço acima,  
então operadores de floodfill podem objetar; se apenas o hash estiver incluído,  
não há verificação, e um registro de serviço poderia "entrar" antes de  
qualquer outro tipo netdb e ser armazenado no floodfill.

Pesquisa com  
    Tipo de pesquisa Lista de Serviço (11)  
Armazenar com  
    Tipo Lista de Serviço (11)  
Armazenar em  
    Hash do nome do serviço  
    Este hash é então usado para gerar a "chave de roteamento" diária, como em LS1  
Expiração típica  
    Horas, não especificada na lista em si, até a política local  
Publicado por  
    Ninguém, nunca enviado ao floodfill, nunca inundado.

### Formato

NÃO usa o cabeçalho LS2 padrão especificado acima.

```
- Tipo (1 byte)
    Não está realmente no cabeçalho, mas faz parte dos dados cobertos pela assinatura.
    Pegue do campo na Mensagem de Armazenamento no Banco de Dados.
  - Hash do nome do serviço (implícito, na Mensagem de Armazenamento no Banco de Dados)
  - Hash do Criador (floodfill) (32 bytes)
  - Timestamp de publicação (8 bytes, big endian)

  - Número de Registros de Serviço Curto (1 byte)
  - Lista de Registros de Serviço Curto:
    Cada Registro de Serviço Curto contém (90+ bytes)
    - Hash do destino (32 bytes)
    - Timestamp de publicação (8 bytes, big endian)
    - Expira (4 bytes, big endian) (deslocamento da publicação em ms)
    - Flags (2 bytes)
    - Porta (2 bytes, big endian)
    - Comprimento da assinatura (2 bytes, big endian)
    - Assinatura do destino (40+ bytes)

  - Número de Registros de Revogação (1 byte)
  - Lista de Registros de Revogação:
    Cada Registro de Revogação contém (86+ bytes)
    - Hash do destino (32 bytes)
    - Timestamp de publicação (8 bytes, big endian)
    - Flags (2 bytes)
    - Porta (2 bytes, big endian)
    - Comprimento da assinatura (2 bytes, big endian)
    - Assinatura do destino (40+ bytes)

  - Assinatura do floodfill (40+ bytes)
    A assinatura é de tudo acima.
```

Para verificar a assinatura da Lista de Serviço:

- pré-anexar o hash do nome do serviço
- remover o hash do criador
- Verificar assinatura do conteúdo modificado

Para verificar a assinatura de cada Registro de Serviço Curto:

- Buscar destino
- Verificar assinatura de (timestamp de publicação + expira + flags + porta + Hash do  
  nome do serviço)

Para verificar a assinatura de cada Registro de Revogação:

- Buscar destino
- Verificar assinatura de (timestamp de publicação + 4 bytes zero + flags + porta + Hash  
  do nome do serviço)

### Notas

- Usamos comprimento da assinatura em vez de tipo de assinatura para suportar tipos de assinatura desconhecidos.

- Não há expiração de uma lista de serviço, os destinatários podem tomar sua própria  
  decisão com base na política ou na expiração dos registros individuais.

- Listas de Serviço não são inundadas, apenas Registros de Serviço individuais são. Cada  
  floodfill cria, assina e armazena em cache uma Lista de Serviço. O floodfill usa sua  
  própria política para tempo de cache e número máximo de registros de serviço e revogação.



## Alterações Necessárias na Especificação de Estruturas Comuns


### Certificados de Chave
