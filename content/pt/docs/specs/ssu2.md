---
title: "Especificação SSU2"
description: "Protocolo de Transporte UDP Semi-Confiável Seguro Versão 2"
slug: "ssu2"
category: "Transportes"
lastUpdated: "2026-03"
accurateFor: "0.9.69"
---

## Estado

Substancialmente completo. Veja [Prop159](/proposals/159-ssu2) para informações adicionais e objetivos, incluindo análise de segurança, modelos de ameaça, uma revisão da segurança e problemas do SSU 1, e trechos das especificações QUIC.

Plano de implementação:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Feature</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Testing (not default)</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Enabled by default</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Local test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test code</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2022-03</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Joint test in-net</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze basic protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.54 2022-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Basic Session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address Validation (Retry)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Fragmented RI in handshake</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Freeze extended protocol</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Enable for random 2%</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55 2022-08</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Validation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Connection Migration</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Immediate ACK flag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.55+ dev</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Key Rotation</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.57 2023-02</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (i2pd)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.56 2022-11</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Disable SSU 1 (Java I2P)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58 2023-05</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.61 2023-12</td></tr>
  </tbody>
</table>
A Sessão Básica inclui as fases de handshake e dados. O protocolo estendido inclui relay e teste de peer.

## Visão Geral

Esta especificação define um protocolo de acordo de chaves autenticado para melhorar a resistência do [SSU](/docs/transport/ssu) a várias formas de identificação automatizada e ataques.

Como com outros transportes I2P, o SSU2 é definido para transporte ponto-a-ponto (router para router) de mensagens I2NP. Não é um canal de dados de uso geral. Tal como o [SSU](/docs/transport/ssu), também fornece dois serviços adicionais: Retransmissão para travessia de NAT e Teste de Pares para determinação da acessibilidade de entrada. Também fornece um terceiro serviço, não presente no SSU, para migração de conexão quando um par altera o IP ou porta.

## Visão Geral do Design

### Resumo

Dependemos de vários protocolos existentes, tanto dentro do I2P quanto de padrões externos, para inspiração, orientação e reutilização de código:

- Modelos de ameaça: Do NTCP2 [NTCP2](/docs/specs/ntcp2), com ameaças adicionais significativas relevantes para transporte UDP conforme analisado pelo QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Escolhas criptográficas: Do [NTCP2](/docs/specs/ntcp2).
- Handshake: Noise XK do [NTCP2](/docs/specs/ntcp2) e [NOISE](https://noiseprotocol.org/noise.html). Simplificações significativas ao NTCP2 são possíveis devido ao encapsulamento (limites de mensagem inerentes) fornecido pelo UDP.
- Ofuscação de chave efêmera do handshake: Adaptado do [NTCP2](/docs/specs/ntcp2) mas usando ChaCha20 do [ECIES](/docs/specs/ecies) em vez de AES.
- Cabeçalhos de pacote: Adaptado do WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) e QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Ofuscação de cabeçalho de pacote: Adaptado do [NTCP2](/docs/specs/ntcp2) mas usando ChaCha20 do [ECIES](/docs/specs/ecies) em vez de AES.
- Proteção de cabeçalho de pacote: Adaptado do QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) e [Nonces](https://eprint.iacr.org/2019/624.pdf)
- Cabeçalhos usados como dados associados AEAD como no [ECIES](/docs/specs/ecies).
- Numeração de pacotes: Adaptado do WireGuard [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) e QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) [RFC-9001](https://tools.ietf.org/html/rfc9001).
- Mensagens: Adaptado do [SSU](/docs/transport/ssu)
- Fragmentação I2NP: Adaptado do [SSU](/docs/transport/ssu)
- Relay e Teste de Peers: Adaptado do [SSU](/docs/transport/ssu)
- Assinaturas de dados de Relay e Teste de Peers: Da especificação de estruturas comuns [Common](/docs/specs/common-structures)
- Formato de bloco: Do [NTCP2](/docs/specs/ntcp2) e [ECIES](/docs/specs/ecies).
- Padding e opções: Do [NTCP2](/docs/specs/ntcp2) e [ECIES](/docs/specs/ecies).
- Acks, nacks: Adaptado do QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000).
- Controle de fluxo: TBD

Não há primitivas criptográficas novas que não tenham sido usadas anteriormente no I2P.

### Garantias de Entrega

Assim como outros transportes I2P NTCP, NTCP2 e SSU 1, este transporte não é uma facilidade de uso geral para entrega de um fluxo ordenado de bytes. Ele foi projetado para o transporte de mensagens I2NP. Não há abstração de "fluxo" fornecida.

Além disso, assim como para SSU, contém facilidades adicionais para travessia de NAT facilitada por peers e teste de alcançabilidade (conexões de entrada).

Quanto ao SSU 1, ele NÃO fornece entrega em ordem das mensagens I2NP. Nem fornece entrega garantida das mensagens I2NP. Por eficiência, ou devido à entrega fora de ordem dos datagramas UDP ou perda desses datagramas, as mensagens I2NP podem ser entregues na extremidade remota fora de ordem, ou podem não ser entregues de forma alguma. Uma mensagem I2NP pode ser retransmitida várias vezes se necessário, mas a entrega pode eventualmente falhar sem causar a desconexão completa da conexão. Além disso, novas mensagens I2NP podem continuar a ser enviadas mesmo enquanto a retransmissão (recuperação de perda) está ocorrendo para outras mensagens I2NP.

Este protocolo NÃO previne completamente a entrega duplicada de mensagens I2NP. O router deve impor a expiração de I2NP e usar um filtro Bloom ou outro mecanismo baseado no ID da mensagem I2NP. Veja a seção Duplicação de Mensagens I2NP abaixo.

### Framework de Protocolo Noise

Esta especificação fornece os requisitos baseados no Noise Protocol Framework [NOISE](https://noiseprotocol.org/noise.html) (Revisão 33, 2017-10-04). O Noise possui propriedades similares ao protocolo Station-To-Station [STS](https://en.wikipedia.org/wiki/Station-to-Station_protocol), que é a base para o protocolo [SSU](/docs/transport/ssu). Na terminologia do Noise, Alice é o iniciador, e Bob é o respondedor.

SSU2 é baseado no protocolo Noise Noise_XK_25519_ChaChaPoly_SHA256. (O identificador real para a função inicial de derivação de chave é "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256" para indicar extensões I2P - veja a seção KDF 1 abaixo)

NOTA: Este identificador é diferente daquele usado para NTCP2, porque todas as três mensagens de handshake usam o cabeçalho como dados associados.

Este protocolo Noise usa os seguintes primitivos:

- Padrão de Handshake: XK Alice transmite sua chave para Bob (X) Alice já conhece a chave estática de Bob (K)
- Função DH: X25519 X25519 DH com comprimento de chave de 32 bytes conforme especificado na [RFC-7748](https://tools.ietf.org/html/rfc7748).
- Função de Cifra: ChaChaPoly AEAD_CHACHA20_POLY1305 conforme especificado na [RFC-7539](https://tools.ietf.org/html/rfc7539) seção 2.8. Nonce de 12 bytes, com os primeiros 4 bytes definidos como zero.
- Função de Hash: SHA256 Hash padrão de 32 bytes, já amplamente utilizado no I2P.

### Adições ao Framework

Esta especificação define as seguintes melhorias para Noise_XK_25519_ChaChaPoly_SHA256. Estas geralmente seguem as diretrizes da seção 13 do [NOISE](https://noiseprotocol.org/noise.html).

1) Mensagens de handshake (Session Request, Created, Confirmed) incluem um cabeçalho de 16 ou 32 bytes. 2) Os cabeçalhos para as mensagens de handshake (Session Request, Created, Confirmed) são usados como entrada para mixHash() antes da criptografia/descriptografia para vincular os cabeçalhos à mensagem. 3) Cabeçalhos são criptografados e protegidos. 4) Chaves efêmeras em texto claro são ofuscadas com criptografia ChaCha20 usando uma chave e IV conhecidos. Isso é mais rápido que elligator2. 5) O formato do payload é definido para mensagens 1, 2, e a fase de dados. É claro que isso não é definido no Noise.

A fase de dados usa criptografia similar, mas não compatível com a fase de dados do Noise.

### Estabelecimento de Sessão

Definimos as seguintes funções correspondentes aos blocos de construção criptográficos utilizados.

#### Cabeçalho Longo

ZEROLEN

#### Cabeçalho Curto

:   array de bytes de comprimento zero

#### Numeração de ID de Conexão

H(p, d)

#### Numeração de Pacotes

:   Função hash SHA-256 que recebe uma string de personalização p e dados d, e produz uma saída de 32 bytes de comprimento. Conforme definido em [NOISE](https://noiseprotocol.org/noise.html). || abaixo significa anexar.

## Definições

MixHash(d)

:   Função hash SHA-256 que recebe um hash anterior h e novos dados d, e produz uma saída de comprimento 32 bytes. || abaixo significa anexar.

STREAM

:   O AEAD ChaCha20/Poly1305 conforme especificado na [RFC-7539](https://tools.ietf.org/html/rfc7539). S_KEY_LEN = 32 e S_IV_LEN = 12.

DH

    Use SHA-256 as follows:

        H(p, d) := SHA-256(p || d)

:   Sistema de acordo de chaves públicas X25519. Chaves privadas de 32 bytes, chaves públicas de 32 bytes, produz saídas de 32 bytes. Possui as seguintes funções:

HKDF(salt, ikm, info, n)

    Use SHA-256 as follows:

        MixHash(d) := h = SHA-256(h || d)

:   Uma função de derivação de chave criptográfica que recebe algum material de chave de entrada ikm (que deve ter boa entropia mas não é necessário ser uma string uniformemente aleatória), um salt de 32 bytes de comprimento, e um valor 'info' específico do contexto, e produz uma saída de n bytes adequada para uso como material de chave.

MixKey(d)

    ENCRYPT(k, n, plaintext, ad)

    :   Encrypts plaintext using the cipher key k, and nonce n which MUST be unique for the key k. Associated data ad is optional. Returns a ciphertext that is the size of the plaintext + 16 bytes for the HMAC.

        The entire ciphertext must be indistinguishable from random if the key is secret.

    DECRYPT(k, n, ciphertext, ad)

    :   Decrypts ciphertext using the cipher key k, and nonce n. Associated data ad is optional. Returns the plaintext.

:   Usa HKDF() com uma chainKey anterior e novos dados d, e define a nova chainKey e k. Como definido em [NOISE](https://noiseprotocol.org/noise.html).

Cada datagrama UDP contém exatamente uma mensagem. O comprimento do datagrama (após os cabeçalhos IP e UDP) é o comprimento da mensagem. O preenchimento, se houver, está contido em um bloco de preenchimento dentro da mensagem. Neste documento, usamos os termos "datagrama" e "pacote" principalmente de forma intercambiável. Cada datagrama (ou pacote) contém uma única mensagem (ao contrário do QUIC, onde um datagrama pode conter múltiplos pacotes QUIC). O "cabeçalho do pacote" é a parte após o cabeçalho IP/UDP.

    GENERATE_PRIVATE()

    :   Generates a new private key.

    DERIVE_PUBLIC(privkey)

    :   Returns the public key corresponding to the given private key.

    DH(privkey, pubkey)

    :   Generates a shared secret from the given private and public keys.

Exceção: A mensagem Session Confirmed é única no sentido de que pode ser fragmentada em múltiplos pacotes. Veja a seção Session Confirmed Fragmentation abaixo para mais informações.

Todas as mensagens SSU2 têm pelo menos 40 bytes de comprimento. Qualquer mensagem com comprimento de 1-39 bytes é inválida. Todas as mensagens SSU2 têm no máximo 1472 (IPv4) ou 1452 (IPv6) bytes de comprimento. O formato da mensagem é baseado em mensagens Noise, com modificações para enquadramento e indistinguibilidade. Implementações que usam bibliotecas Noise padrão devem pré-processar as mensagens recebidas para o formato de mensagem Noise padrão. Todos os campos criptografados são textos cifrados AEAD.

    Use HKDF as specified in [RFC-5869](https://tools.ietf.org/html/rfc5869), using the HMAC hash function SHA-256 as specified in [RFC-2104](https://tools.ietf.org/html/rfc2104). This means that SALT_LEN is 32 bytes max.

As seguintes mensagens são definidas:

A sequência de estabelecimento padrão, quando Alice tem um token válido previamente recebido de Bob, é a seguinte:

    Use HKDF as follows:

        MixKey(d) := output = HKDF(chainKey, d, "", 64)
                     chainKey = output[0:31]
                     k = output[32:63]

## Mensagens

Quando Alice não possui um token válido, a sequência de estabelecimento é a seguinte:

Quando Alice pensa que tem um token válido, mas Bob o rejeita (talvez porque Bob reiniciou), a sequência de estabelecimento é a seguinte:

Bob pode rejeitar uma Solicitação de Sessão ou Token respondendo com uma mensagem de Retry contendo um bloco de Terminação com um código de motivo. Com base no código de motivo, Alice não deve tentar outra solicitação por algum período de tempo:

Usando a terminologia Noise, a sequência de estabelecimento e dados é a seguinte: (Propriedades de Segurança da Carga Útil)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Length</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header Encr. Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionRequest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionCreated</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">64</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SessionConfirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">PeerTest</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">HolePunch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td></tr>
  </tbody>
</table>
### Cabeçalho do Pacote

Uma vez que uma sessão tenha sido estabelecida, Alice e Bob podem trocar mensagens de Dados.

```
Alice                           Bob

SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Todos os pacotes começam com um cabeçalho ofuscado (criptografado). Existem dois tipos de cabeçalho, longo e curto. Note que os primeiros 13 bytes (Destination Connection ID, número do pacote e tipo) são os mesmos para todos os cabeçalhos.

```
Alice                           Bob

TokenRequest --------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
O cabeçalho longo tem 32 bytes. É usado antes de uma sessão ser criada, para Token Request, SessionRequest, SessionCreated e Retry. Também é usado para mensagens Peer Test e Hole Punch fora de sessão.

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry
SessionRequest ------------------->
<------------------- SessionCreated
SessionConfirmed ----------------->
```
Antes da criptografia do cabeçalho:

```
Alice                           Bob

SessionRequest ------------------->
<---------------------------  Retry containing a Termination block

or

TokenRequest --------------------->
<---------------------------  Retry containing a Termination block
```
O cabeçalho curto tem 16 bytes. É usado para mensagens Session Created e para mensagens de dados. Mensagens não autenticadas como Session Request, Retry e Peer Test sempre usarão o cabeçalho longo.

```
XK(s, rs):           Authentication   Confidentiality
  <- s
  ...
  -> e, es                  0                2
  <- e, ee                  2                1
  -> s, se                  2                5
  <-                        2                5
```
16 bytes são necessários, porque o receptor deve descriptografar os primeiros 16 bytes para obter o tipo de mensagem, e então deve descriptografar 16 bytes adicionais se for realmente um cabeçalho longo, conforme indicado pelo tipo de mensagem.

### Integridade de Pacotes

Para Session Confirmed, antes da criptografia do cabeçalho:

#### Vinculação de Cabeçalho

Consulte a seção Fragmentação de Sessão Confirmada abaixo para mais informações sobre o campo frag.

Para mensagens de Dados, antes da encriptação do cabeçalho:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 0, 1, 7, 9, 10, or 11

ver :: The protocol version, equal to 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: 8 bytes, unsigned big endian integer

Token :: 8 bytes, unsigned big endian integer
```
#### Criptografia do Cabeçalho

Os IDs de conexão devem ser gerados aleatoriamente. Os IDs de Origem e Destino NÃO devem ser idênticos, para que um atacante no caminho não possa capturar e enviar um pacote de volta ao originador que pareça válido. NÃO use um contador para gerar IDs de conexão, para que um atacante no caminho não possa gerar um pacote que pareça válido.

Ao contrário do QUIC, não alteramos os IDs de conexão durante ou após o handshake, mesmo depois de uma mensagem Retry. Os IDs permanecem constantes desde a primeira mensagem (Token Request ou Session Request) até a última mensagem (Data with Termination). Além disso, os IDs de conexão não mudam durante ou após path challenge ou migração de conexão.

Também diferente do QUIC é que os IDs de conexão nos cabeçalhos são sempre criptografados no cabeçalho. Veja abaixo.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, all zeros

type :: The message type = 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility
```
Se nenhum bloco First Packet Number for enviado no handshake, os pacotes são numerados dentro de uma única sessão, para cada direção, começando de 0, até um máximo de (2**32 -1). Uma sessão deve ser encerrada, e uma nova sessão criada, bem antes que o número máximo de pacotes seja enviado.

Se um bloco First Packet Number for enviado no handshake, os pacotes são numerados dentro de uma única sessão, para essa direção, começando a partir desse número de pacote. O número do pacote pode dar a volta durante a sessão. Quando um máximo de 2**32 pacotes tiverem sido enviados, fazendo o número do pacote voltar ao primeiro número de pacote, essa sessão não é mais válida. Uma sessão deve ser terminada, e uma nova sessão criada, bem antes do número máximo de pacotes ser enviado.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|flag|moreflags|
+----+----+----+----+----+----+----+----+

Destination Connection ID :: 8 bytes, unsigned big endian integer

Packet Number :: 4 bytes, unsigned big endian integer

type :: The message type = 6

flag :: 1 byte flags:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-1: unused, set to 0 for future compatibility
       bits 0: when set to 1, immediate ack requested

moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### KDF de Criptografia de Cabeçalho

TODO rotação de chaves, reduzir número máximo de pacotes?

Pacotes de handshake que são determinados como perdidos são retransmitidos inteiros, com o cabeçalho idêntico incluindo o número do pacote. As mensagens de handshake Session Request, Session Created e Session Confirmed DEVEM ser retransmitidas com o mesmo número de pacote e conteúdo criptografado idêntico, para que o mesmo hash encadeado seja usado para criptografar a resposta. A mensagem Retry nunca é transmitida.

Pacotes da fase de dados que são determinados como perdidos nunca são retransmitidos inteiros (exceto terminação, veja abaixo). O mesmo se aplica aos blocos que estão contidos dentro de pacotes perdidos. Em vez disso, as informações que podem ser transportadas em blocos são enviadas novamente em novos pacotes conforme necessário. Pacotes de Dados nunca são retransmitidos com o mesmo número de pacote. Qualquer retransmissão do conteúdo de pacotes (seja ou não o conteúdo permaneça o mesmo) deve usar o próximo número de pacote não utilizado.

#### Validação de Cabeçalho

Retransmitir um pacote inteiro inalterado como está, com o mesmo número de pacote, não é permitido por várias razões. Para contexto, consulte QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) seção 12.3.

Novos pacotes são usados para transportar informações que foram determinadas como perdidas. Em geral, as informações são enviadas novamente quando um pacote contendo essas informações é determinado como perdido, e o envio cessa quando um pacote contendo essas informações permanece o mesmo) é confirmado.

Exceção: Um pacote de fase de dados contendo um bloco de Terminação pode, mas não é obrigatório, ser retransmitido inteiro, como está. Veja a seção Terminação de Sessão abaixo.

Os seguintes pacotes contêm um número de pacote aleatório que é ignorado:

Para Alice, a numeração de pacotes de saída começa em 0 com Session Confirmed. Para Bob, a numeração de pacotes de saída começa em 0 com o primeiro pacote Data, que deve ser um ACK do Session Confirmed. Os números de pacotes em um exemplo de handshake padrão serão:

Qualquer retransmissão de mensagens de handshake (SessionRequest, SessionCreated, ou SessionConfirmed) deve ser reenviada inalterada, com o mesmo número de pacote. Não use chaves efêmeras diferentes ou altere o payload ao retransmitir essas mensagens.

- É ineficiente armazenar pacotes para retransmissão
- Um novo pacote de dados parece diferente para um observador no caminho, não consegue dizer que é retransmitido
- Um novo pacote recebe um bloco ack atualizado enviado junto com ele, não o bloco ack antigo
- Você só retransmite o que é necessário. alguns fragmentos podem ter sido já retransmitidos uma vez e confirmados
- Você pode encaixar tanto quanto precisar em cada pacote retransmitido se mais estiver pendente
- Endpoints que rastreiam todos os pacotes individuais para fins de detectar duplicatas correm o risco de acumular estado excessivo. Os dados necessários para detectar duplicatas podem ser limitados mantendo um número mínimo de pacote abaixo do qual todos os pacotes são imediatamente descartados.
- Este esquema é muito mais flexível

O cabeçalho (antes da ofuscação e proteção) é sempre incluído nos dados associados para a função AEAD, para vincular criptograficamente o cabeçalho aos dados.

A criptografia de cabeçalho tem vários objetivos. Consulte a seção "Discussão Adicional sobre DPI" acima para contexto e suposições.

Os cabeçalhos são criptografados com chaves conhecidas publicadas no netDb ou calculadas posteriormente. Na fase de handshake, isso serve apenas para resistência a DPI, pois a chave é pública e a chave e nonces são reutilizados, então é efetivamente apenas ofuscação. Note que a criptografia do cabeçalho também é usada para ofuscar as chaves efêmeras X (no Session Request) e Y (no Session Created).

- Solicitação de Sessão
- Sessão Criada
- Solicitação de Token
- Tentar Novamente
- Teste de Peer
- Hole Punch

Consulte a seção Tratamento de Pacotes de Entrada abaixo para orientações adicionais.

```
Alice                           Bob

SessionRequest (r)    ------------>
<-------------   SessionCreated (r)
SessionConfirmed (0)  ------------>
<-------------             Data (0) (Ack-only)
Data (1)              ------------> (May be sent before Ack is received)
<-------------             Data (1)
Data (2)              ------------>
Data (3)              ------------>
Data (4)              ------------>
<-------------             Data (2)

r = random packet number (ignored)
Token Request, Retry, and Peer Test
also have random packet numbers.
```
Os bytes 0-15 de todos os cabeçalhos são criptografados usando um esquema de proteção de cabeçalho através de XOR com dados calculados a partir de chaves conhecidas, utilizando ChaCha20, semelhante ao QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) e [Nonces](https://eprint.iacr.org/2019/624.pdf). Isso garante que o cabeçalho curto criptografado e a primeira parte do cabeçalho longo aparentem ser aleatórios.

#### ChaCha20/Poly1305

Para Session Request e Session Created, os bytes 16-31 do cabeçalho longo e a chave efêmera Noise de 32 bytes são criptografados usando ChaCha20. Os dados não criptografados são aleatórios, então os dados criptografados parecerão ser aleatórios.

#### Notas

Para Retry, os bytes 16-31 do cabeçalho longo são criptografados usando ChaCha20. Os dados não criptografados são aleatórios, então os dados criptografados parecerão ser aleatórios.

- Prevenir que DPI online identifique o protocolo
- Prevenir padrões numa série de mensagens na mesma conexão, exceto para retransmissões de handshake
- Prevenir padrões em mensagens do mesmo tipo em conexões diferentes
- Prevenir descriptografia de cabeçalhos de handshake sem conhecimento da chave de introdução encontrada no netDb
- Prevenir identificação de chaves efêmeras X25519 sem conhecimento da chave de introdução encontrada no netDb
- Prevenir descriptografia do número e tipo de pacote da fase de dados por qualquer atacante online ou offline
- Prevenir injeção de pacotes de handshake válidos por um observador no caminho ou fora do caminho sem conhecimento da chave de introdução encontrada no netDb
- Prevenir injeção de pacotes de dados válidos por um observador no caminho ou fora do caminho
- Permitir classificação rápida e eficiente de pacotes recebidos
- Fornecer resistência a "sondagem" para que não haja resposta a uma Session Request inválida, ou se houver uma resposta Retry, a resposta não seja identificável como I2P sem conhecimento da chave de introdução encontrada no netDb
- O Destination Connection ID não é dados críticos, e não há problema se puder ser descriptografado por um observador com conhecimento da chave de introdução encontrada no netDb
- O número do pacote de um pacote da fase de dados é um nonce AEAD e são dados críticos. Não deve ser descriptografável por um observador mesmo com conhecimento da chave de introdução encontrada no netDb. Veja [Nonces](https://eprint.iacr.org/2019/624.pdf).

Ao contrário do esquema de proteção de cabeçalho QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001), TODAS as partes de todos os cabeçalhos, incluindo IDs de conexão de destino e origem, são criptografadas. O QUIC [RFC-9001](https://tools.ietf.org/html/rfc9001) e [Nonces](https://eprint.iacr.org/2019/624.pdf) estão principalmente focados em criptografar a parte "crítica" do cabeçalho, ou seja, o número do pacote (nonce ChaCha20). Embora criptografar o ID da sessão torne a classificação de pacotes recebidos um pouco mais complexa, isso dificulta alguns ataques. O QUIC define diferentes IDs de conexão para diferentes fases, e para desafio de caminho e migração de conexão. Aqui utilizamos os mesmos IDs de conexão por toda a duração, já que eles são criptografados.

Existem sete fases de chaves de proteção de cabeçalho:

A encriptação de cabeçalho é projetada para permitir a classificação rápida de pacotes de entrada, sem heurísticas complexas ou mecanismos de fallback. Isso é alcançado usando a mesma chave k_header_1 para quase todas as mensagens de entrada. Mesmo quando o IP de origem ou porta de uma conexão muda devido a uma mudança real de IP ou comportamento de NAT, o pacote pode ser rapidamente mapeado para uma sessão com uma única consulta do ID da conexão.

Note que Session Created e Retry são as ÚNICAS mensagens que requerem processamento de fallback para k_header_1 para descriptografar o Connection ID, porque elas usam a chave de introdução do remetente (Bob). TODAS as outras mensagens usam a chave de introdução do receptor para k_header_1. O processamento de fallback precisa apenas procurar conexões de saída pendentes por IP/porta de origem.

Se o processamento de fallback por IP/porta de origem falhar em encontrar uma conexão de saída pendente, pode haver várias causas:

Embora seja possível realizar processamento de fallback adicional para tentar encontrar a conexão de saída pendente e descriptografar o ID da conexão usando o k_header_1 para essa conexão, provavelmente não é necessário. Se Bob tem problemas com seu NAT ou roteamento de pacotes, é provavelmente melhor deixar a conexão falhar. Este design depende dos endpoints manterem um endereço estável durante a duração do handshake.

Consulte a seção Manipulação de Pacotes de Entrada abaixo para diretrizes adicionais.

- Solicitação de Sessão e Solicitação de Token
- Sessão Criada
- Tentar Novamente
- Sessão Confirmada
- Fase de Dados
- Teste de Peer
- Perfuração de Buraco

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_1</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Key k_header_2</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Token Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Request KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See Session Created KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Retry</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Bob Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice/Bob Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">See data phase KDF</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 5,7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test 6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie Intro Key</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Hole Punch</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice Intro Key</td></tr>
  </tbody>
</table>
Consulte as seções individuais de KDF abaixo para a derivação das chaves de criptografia do cabeçalho para essa fase.

Este KDF usa os últimos 24 bytes do pacote como o IV para as duas operações ChaCha20. Como todos os pacotes terminam com um MAC de 16 bytes, isso exige que todas as cargas úteis de pacotes tenham um mínimo de 8 bytes. Este requisito é adicionalmente documentado nas seções de mensagem abaixo.

Após descriptografar os primeiros 8 bytes do cabeçalho, o receptor saberá o ID de Conexão de Destino. A partir daí, o receptor sabe qual chave de criptografia de cabeçalho usar para o restante do cabeçalho, com base na fase de chave da sessão.

- Não é uma mensagem SSU2
- Uma mensagem SSU2 corrompida
- A resposta foi falsificada ou modificada por um atacante
- Bob tem um NAT simétrico
- Bob mudou de IP ou porta durante o processamento da mensagem
- Bob enviou a resposta por uma interface diferente

Descriptografar os próximos 8 bytes do cabeçalho revelará então o tipo de mensagem e permitirá determinar se é um cabeçalho curto ou longo. Se for um cabeçalho longo, o receptor deve validar os campos de versão e netid. Se a versão for != 2, ou o netid for != o valor esperado (geralmente 2, exceto em redes de teste), o receptor deve descartar a mensagem.

Todas as mensagens contêm três ou quatro partes:

Em todos os casos, o cabeçalho (e se presente, a chave efêmera) está vinculado ao MAC de autenticação para garantir que toda a mensagem esteja íntegra.

#### Tratamento de Erros AEAD

```
// incoming encrypted packet
packet = incoming encrypted packet
len = packet.length

// take the next-to-last 12 bytes of the packet
iv = packet[len-24:len-13]
k_header_1 = header encryption key 1
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_1, iv, data)

// encrypt the first part of the header by XORing with the mask
packet[0:7] ^= mask[0:7]

// take the last 12 bytes of the packet
iv = packet[len-12:len-1]
k_header_2 = header encryption key 2
data = {0, 0, 0, 0, 0, 0, 0, 0}
mask = ChaCha20.encrypt(k_header_2, iv, data)

// encrypt the second part of the header by XORing with the mask
packet[8:15] ^= mask[0:7]


// For Session Request and Session Created only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header and the ephemeral key
packet[16:63] = ChaCha20.encrypt(k_header_2, iv, packet[16:63])


// For Retry, Token Request, Peer Test, and Hole Punch only:
iv = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

// encrypt the third part of the header
packet[16:31] = ChaCha20.encrypt(k_header_2, iv, packet[16:31])
```
Os manipuladores de pacotes de entrada devem sempre descriptografar o payload ChaCha20 e validar o MAC antes de processar a mensagem, com uma exceção: Para mitigar ataques DoS de pacotes com endereços falsificados contendo mensagens Session Request aparentes com um token inválido, um manipulador NÃO precisa tentar descriptografar e validar a mensagem completa (requerendo uma operação DH dispendiosa além da descriptografia ChaCha20/Poly1305). O manipulador pode responder com uma mensagem Retry usando os valores encontrados no cabeçalho da mensagem Session Request.

#### KDF para ChainKey Inicial

Existem três instâncias separadas de encriptação autenticada (CipherStates). Uma durante a fase de handshake, e duas (transmissão e recepção) para a fase de dados. Cada uma tem sua própria chave de um KDF.

Dados criptografados/autenticados serão representados como

### Criptografia Autenticada

Formato de dados criptografado e autenticado.

- O cabeçalho da mensagem
- Apenas para Session Request e Session Created, uma chave efêmera
- Um payload criptografado com ChaCha20
- Um MAC Poly1305

Entradas para as funções de criptografia/descriptografia:

- Para mensagens de handshake Session Request, Session Created e Session Confirmed, o cabeçalho da mensagem é mixHash()ed antes da fase de processamento Noise
- A chave efêmera, se presente, é coberta por um misHash() Noise padrão
- Para mensagens fora do handshake Noise, o cabeçalho é usado como Dados Associados para a criptografia ChaCha20/Poly1305.

Saída da função de criptografia, entrada da função de descriptografia:

### KDF para Solicitação de Sessão

Para ChaCha20, o que é descrito aqui corresponde ao [RFC-7539](https://tools.ietf.org/html/rfc7539), que também é usado de forma similar no TLS [RFC-7905](https://tools.ietf.org/html/rfc7905).

A Função de Derivação de Chave (KDF) gera uma chave de cifra da fase de handshake k a partir do resultado DH, usando HMAC-SHA256(key, data) conforme definido em [RFC-2104](https://tools.ietf.org/html/rfc2104). Estas são as funções InitializeSymmetric(), MixHash(), e MixKey(), exatamente como definidas na especificação Noise.

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   Encrypted and authenticated data    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
```
#### KDF para Solicitação de Sessão

Alice envia para Bob, seja como a primeira mensagem no handshake, ou em resposta a uma mensagem Retry. Bob responde com uma mensagem Session Created. Tamanho: 80 + tamanho do payload. Tamanho Mínimo: 88

Se Alice não tiver um token válido, Alice deve enviar uma mensagem Token Request em vez de uma Session Request, para evitar a sobrecarga de criptografia assimétrica na geração de uma Session Request.

```
k :: 32 byte cipher key, as generated from KDF

nonce :: Counter-based nonce, 12 bytes.
         Starts at 0 and incremented for each message.
         First four bytes are always zero.
         Last eight bytes are the counter, little-endian encoded.
         Maximum value is 2**64 - 2.
         Connection must be dropped and restarted after
         it reaches that value.
         The value 2**64 - 1 must never be sent.

ad :: In handshake phase:
      Associated data, 32 bytes.
      The SHA256 hash of all preceding data.
      In data phase:
      The packet header, 16 bytes.

data :: Plaintext data, 0 or more bytes
```
Cabeçalho longo. Conteúdo de ruído: chave efêmera X de Alice Carga útil de ruído: DateTime e outros blocos Tamanho máximo da carga útil: MTU - 108 (IPv4) ou MTU - 128 (IPv6). Para MTU 1280: Carga útil máxima é 1172 (IPv4) ou 1152 (IPv6). Para MTU 1500: Carga útil máxima é 1392 (IPv4) ou 1372 (IPv6).

```
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|       ChaCha20 encrypted data         |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|  Poly1305 Message Authentication Code |
+              (MAC)                    +
|             16 bytes                  |
+----+----+----+----+----+----+----+----+

encrypted data :: Same size as plaintext data, 0 - 65519 bytes

MAC :: Poly1305 message authentication code, 16 bytes
```
Propriedades de Segurança do Payload:

#### Carga útil

- Como ChaCha20 é um cipher de fluxo, os plaintexts não precisam ser preenchidos. Bytes adicionais do keystream são descartados.
- A chave para o cipher (256 bits) é acordada por meio do SHA256 KDF. Os detalhes do KDF para cada mensagem estão nas seções separadas abaixo.

#### Notas

- Em todas as mensagens, o tamanho da mensagem AEAD é conhecido antecipadamente. Em caso de falha de autenticação AEAD, o destinatário deve interromper o processamento adicional de mensagens e descartar a mensagem.
- Bob deve manter uma lista negra de IPs com falhas repetidas.

### SessionRequest (Tipo 0)

O valor X é criptografado para garantir a indistinguibilidade e unicidade do payload, que são contramedidas DPI necessárias. Usamos criptografia ChaCha20 para alcançar isso, em vez de alternativas mais complexas e lentas como elligator2. A criptografia assimétrica para a chave pública do router de Bob seria muito lenta. A criptografia ChaCha20 usa a chave de introdução de Bob conforme publicada no netDb.

#### Carga útil

```
// Define protocol_name.
Set protocol_name = "Noise_XKchaobfse+hs1+hs2+hs3_25519_ChaChaPoly_SHA256"
 (52 bytes, US-ASCII encoded, no NULL termination).

// Define Hash h = 32 bytes
h = SHA256(protocol_name);

Define ck = 32 byte chaining key. Copy the h data to ck.
Set ck = h

// MixHash(null prologue)
h = SHA256(h);

// up until here, can all be precalculated by Alice for all outgoing connections

// Bob's X25519 static keys
// bpk is published in routerinfo
bsk = GENERATE_PRIVATE()
bpk = DERIVE_PUBLIC(bsk)

// Bob static key
// MixHash(bpk)
// || below means append
h = SHA256(h || bpk);

// Bob introduction key
// bik is published in routerinfo
bik = RANDOM(32)

// up until here, can all be precalculated by Bob for all incoming connections
```
#### Notas

```
// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Alice's X25519 ephemeral keys
aesk = GENERATE_PRIVATE()
aepk = DERIVE_PUBLIC(aesk)

// Alice ephemeral key X
// MixHash(aepk)
h = SHA256(h || aepk);

// h is used as the associated data for the AEAD in Session Request
// Retain the Hash h for the Session Created KDF


End of "e" message pattern.

This is the "es" message pattern:

// DH(e, rs) == DH(s, re)
sharedSecret = DH(aesk, bpk) = DH(bsk, aepk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
// ChaChaPoly parameters to encrypt/decrypt
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chainKey for Session Created KDF


End of "es" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2 = bik

// Header encryption keys for next message (Session Created)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessCreateHeader", 32)

// Header encryption keys for next message (Retry)
k_header_1 = bik
k_header_2 = bik
```
### KDF para Session Created e Session Confirmed parte 1

A criptografia ChaCha20 é apenas para resistência a DPI. Qualquer parte que conheça a chave de introdução de Bob, que é publicada na base de dados da rede, pode descriptografar o cabeçalho e o valor X nesta mensagem.

Conteúdo bruto:

Dados não criptografados (tag de autenticação Poly1305 não mostrada):

O tamanho mínimo do payload é 8 bytes. Como o bloco DateTime tem apenas 7 bytes, pelo menos um outro bloco deve estar presente.

```
XK(s, rs):           Authentication   Confidentiality
  -> e, es                  0                2

  Authentication: None (0).
  This payload may have been sent by any party, including an active attacker.

  Confidentiality: 2.
  Encryption to a known recipient, forward secrecy for sender compromise
  only, vulnerable to replay.  This payload is encrypted based only on DHs
  involving the recipient's static key pair.  If the recipient's static
  private key is compromised, even at a later date, this payload can be
  decrypted.  This message can also be replayed, since there's no ephemeral
  contribution from the recipient.

  "e": Alice generates a new ephemeral key pair and stores it in the e
       variable, writes the ephemeral public key as cleartext into the
       message buffer, and hashes the public key along with the old h to
       derive a new h.

  "es": A DH is performed between the Alice's ephemeral key pair and the
        Bob's static key pair.  The result is hashed along with the old ck to
        derive a new ck and k, and n is set to zero.
```
Bob envia para Alice, em resposta a uma mensagem Session Request. Alice responde com uma mensagem Session Confirmed. Tamanho: 80 + tamanho do payload. Tamanho Mínimo: 88

Conteúdo Noise: chave efêmera Y de Bob Payload Noise: DateTime, Address e outros blocos Tamanho máximo do payload: MTU - 108 (IPv4) ou MTU - 128 (IPv6). Para MTU 1280: Payload máximo é 1172 (IPv4) ou 1152 (IPv6). Para MTU 1500: Payload máximo é 1392 (IPv4) ou 1372 (IPv6).

Propriedades de Segurança da Carga Útil:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|    See Header Encryption KDF          |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key n=0     +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+       X, ChaCha20 encrypted           +
|       with Bob intro key n=0          |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|  k defined in KDF for Session Request |
+  n = 0                                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

X :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted X)
```
O valor Y é criptografado para garantir indistinguibilidade e unicidade da carga útil, que são contramedidas DPI necessárias. Usamos criptografia ChaCha20 para alcançar isso, ao invés de alternativas mais complexas e lentas como elligator2. Criptografia assimétrica para a chave pública do router de Alice seria muito lenta. A criptografia ChaCha20 usa a chave de introdução de Bob, conforme publicada no network database.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                   X                   |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|     see below for allowed blocks      |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 0

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Alice, ignored

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: 0 if not previously received from Bob

X :: 32 bytes, X25519 ephemeral key, little endian
```
#### Problemas

- Bloco DateTime
- Bloco Options (opcional)
- Bloco Relay Tag Request (opcional)
- Bloco Padding (opcional)

A criptografia ChaCha20 é apenas para resistência ao DPI. Qualquer parte que conheça a chave de introdução de Bob, que é publicada na base de dados da rede, e capturar os primeiros 32 bytes da Solicitação de Sessão, pode descriptografar o valor Y nesta mensagem.

#### Carga útil

- O valor X único no bloco ChaCha20 inicial garante que o texto cifrado seja diferente para cada sessão.
- Para fornecer resistência a sondagem, Bob não deve enviar uma mensagem Retry em resposta a uma mensagem Session Request, a menos que os campos de tipo de mensagem, versão do protocolo e ID da rede na mensagem Session Request sejam válidos.
- Bob deve rejeitar conexões onde o valor do timestamp está muito distante do tempo atual. Chame o delta de tempo máximo de "D". Bob deve manter um cache local de valores de handshake previamente utilizados e rejeitar duplicatas, para prevenir ataques de replay. Valores no cache devem ter uma vida útil de pelo menos 2*D. Os valores do cache são dependentes da implementação, no entanto o valor X de 32 bytes (ou seu equivalente criptografado) pode ser usado. Rejeitar enviando uma mensagem Retry contendo um token zero e um bloco de terminação.
- Chaves efêmeras Diffie-Hellman nunca podem ser reutilizadas, para prevenir ataques criptográficos, e a reutilização será rejeitada como um ataque de replay.
- As opções "KE" e "auth" devem ser compatíveis, ou seja, o segredo compartilhado K deve ter o tamanho apropriado. Se mais opções "auth" forem adicionadas, isso pode implicitamente alterar o significado da flag "KE" para usar uma KDF diferente ou um tamanho de truncamento diferente.
- Bob deve validar que a chave efêmera da Alice é um ponto válido na curva aqui.
- O padding deve ser limitado a uma quantidade razoável. Bob pode rejeitar conexões com padding excessivo. Bob especificará suas opções de padding em Session Created. Diretrizes mín/máx a serem determinadas. Tamanho aleatório de 0 a 31 bytes no mínimo? (Distribuição a ser determinada, veja Apêndice A.)
- Na maioria dos erros, incluindo AEAD, DH, replay aparente ou falha de validação de chave, Bob deve interromper o processamento adicional da mensagem e descartar a mensagem sem responder.
- Bob PODE enviar uma mensagem Retry contendo um token zero e um bloco de Terminação com um código de razão de desalinhamento de relógio se o timestamp no bloco DateTime estiver muito desalinhado.
- Mitigação de DoS: DH é uma operação relativamente cara. Como com o protocolo NTCP anterior, os routers devem tomar todas as medidas necessárias para prevenir exaustão de CPU ou conexão. Impor limites no máximo de conexões ativas e máximo de configurações de conexão em progresso. Aplicar timeouts de leitura (tanto por leitura quanto total para "slowloris"). Limitar conexões repetidas ou simultâneas da mesma fonte. Manter listas negras para fontes que falharam repetidamente. Não responder a falha de AEAD. Alternativamente, responder com uma mensagem Retry antes da operação DH e validação AEAD.
- Campo "ver": O protocolo Noise geral, extensões e protocolo SSU2 incluindo especificações de payload, indicando SSU2. Este campo pode ser usado para indicar suporte para mudanças futuras.
- O campo de ID da rede é usado para identificar rapidamente conexões entre redes. Se este campo não corresponder ao ID da rede de Bob, Bob deve desconectar e bloquear conexões futuras.
- Bob deve descartar a mensagem se o Source Connection ID for igual ao Destination Connection ID.

### SessionCreated (Tipo 1)

```
// take h saved from Session Request KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Request)

// MixHash(header)
h = SHA256(h || header)

This is the "e" message pattern:

// Bob's X25519 ephemeral keys
besk = GENERATE_PRIVATE()
bepk = DERIVE_PUBLIC(besk)

// h is from KDF for Session Request
// Bob ephemeral key Y
// MixHash(bepk)
h = SHA256(h || bepk);

// h is used as the associated data for the AEAD in Session Created
// Retain the Hash h for the Session Confirmed KDF

End of "e" message pattern.

This is the "ee" message pattern:

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
sharedSecret = DH(aesk, bepk) = DH(besk, aepk)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// retain the chaining key ck for Session Confirmed KDF

End of "ee" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Request KDF above

// Header protection keys for next message (Session Confirmed)
k_header_1 = bik
k_header_2 = HKDF(chainKey, ZEROLEN, "SessionConfirmed", 32)
```
### KDF para a parte 1 do Session Confirmed, usando KDF do Session Created

Conteúdo bruto:

Dados não criptografados (tag de autenticação Poly1305 não mostrada):

O tamanho mínimo do payload é 8 bytes. Como os blocos DateTime e Address totalizam mais que isso, o requisito é atendido apenas com esses dois blocos.

```
XK(s, rs):           Authentication   Confidentiality
  <- e, ee                  2                1

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 1.
  Encryption to an ephemeral recipient.
  This payload has forward secrecy, since encryption involves an ephemeral-ephemeral DH ("ee").
  However, the sender has not authenticated the recipient,
  so this payload might be sent to any party, including an active attacker.


  "e": Bob generates a new ephemeral key pair and stores it in the e variable,
  writes the ephemeral public key as cleartext into the message buffer,
  and hashes the public key along with the old h to derive a new h.

  "ee": A DH is performed between the Bob's ephemeral key pair and the Alice's ephemeral key pair.
  The result is hashed along with the old ck to derive a new ck and k, and n is set to zero.
```
Alice envia para Bob, em resposta a uma mensagem Session Created. Bob responde imediatamente com uma mensagem Data contendo um bloco ACK. Tamanho: 80 + tamanho do payload. Tamanho Mínimo: Cerca de 500 (o tamanho mínimo do bloco router info é cerca de 420 bytes)

Conteúdo Noise: chave estática de Alice Parte 1 da carga útil Noise: Nenhuma Parte 2 da carga útil Noise: RouterInfo de Alice, e outros blocos Tamanho máximo da carga útil: MTU - 108 (IPv4) ou MTU - 128 (IPv6). Para MTU 1280: Carga útil máxima é 1172 (IPv4) ou 1152 (IPv6). Para MTU 1500: Carga útil máxima é 1392 (IPv4) ou 1372 (IPv6).

Propriedades de Segurança da Carga Útil:

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with derived key n=0       +
|  See Header Encryption KDF            |
+----+----+----+----+----+----+----+----+
|                                       |
+       Y, ChaCha20 encrypted           +
|       with derived key n=0            |
+              (32 bytes)               +
|       See Header Encryption KDF       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in KDF for Session Created +
|  n = 0; see KDF for associated data   |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

Y :: 32 bytes, ChaCha20 encrypted X25519 ephemeral key, little endian
        key: Bob's intro key
        n: 1
        data: 48 bytes (bytes 16-31 of the header, followed by encrypted Y)
```
Isto contém dois frames ChaChaPoly. O primeiro é a chave pública estática criptografada de Alice. O segundo é o payload Noise: o RouterInfo criptografado de Alice, opções opcionais e padding opcional. Eles usam chaves diferentes, porque a função MixKey() é chamada entre eles.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|                  Y                    |
+              (32 bytes)               +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|      see below for allowed blocks     |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: The Source Connection ID
                             received from Alice in Session Request

id :: 1 byte, the network ID (currently 2, except for test networks)

ver :: 2

type :: 1

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random 4 byte number generated by Bob, ignored

Source Connection ID :: The Destination Connection ID
                        received from Alice in Session Request

Token :: 0 (unused)

Y :: 32 bytes, X25519 ephemeral key, little endian
```
#### Notas

- Bloco DateTime
- Bloco Address
- Bloco Relay Tag (opcional)
- Bloco New Token (não recomendado, veja a nota)
- Bloco First Packet Number (opcional)
- Bloco Options (opcional)
- Bloco Termination (não recomendado, envie em uma mensagem retry em vez disso)
- Bloco Padding (opcional)

Conteúdo bruto:

#### Fragmentação de Sessão Confirmada

- Alice deve validar que a chave efêmera de Bob é um ponto válido na curva aqui.
- O padding deve ser limitado a uma quantidade razoável. Alice pode rejeitar conexões com padding excessivo. Alice especificará suas opções de padding em Session Confirmed. Diretrizes mín/máx a serem definidas. Tamanho aleatório de 0 a 31 bytes mínimo? (Distribuição a ser determinada, veja Apêndice A.)
- Em qualquer erro, incluindo AEAD, DH, timestamp, replay aparente, ou falha na validação de chave, Alice deve interromper o processamento adicional de mensagens e fechar a conexão sem responder.
- Alice deve rejeitar conexões onde o valor do timestamp está muito distante do tempo atual. Chame o tempo delta máximo de "D". Alice deve manter um cache local de valores de handshake previamente usados e rejeitar duplicatas, para prevenir ataques de replay. Valores no cache devem ter um tempo de vida de pelo menos 2*D. Os valores do cache são dependentes da implementação, porém o valor Y de 32 bytes (ou seu equivalente criptografado) pode ser usado.
- Alice deve descartar a mensagem se o IP e porta de origem não coincidirem com o IP e porta de destino do Session Request.
- Alice deve descartar a mensagem se os IDs de Conexão de Destino e Origem não coincidirem com os IDs de Conexão de Origem e Destino do Session Request.
- Bob envia um bloco de relay tag se solicitado por Alice no Session Request.
- O bloco New Token não é recomendado em Session Created, porque Bob deve fazer validação do Session Confirmed primeiro. Veja a seção Tokens abaixo.

#### Notas

- Incluir opções de preenchimento mín/máx aqui?

### KDF para Sessão Confirmada parte 2

```
// take h saved from Session Created KDF
// MixHash(ciphertext)
h = SHA256(h || encrypted Noise payload from Session Created)

// MixHash(header)
h = SHA256(h || header)
// h is used as the associated data for the AEAD in Session Confirmed part 1, below

This is the "s" message pattern:

// Alice's X25519 static keys
ask = GENERATE_PRIVATE()
apk = DERIVE_PUBLIC(ask)

// AEAD parameters
// k is from Session Request
n = 1
ad = h
ciphertext = ENCRYPT(k, n++, apk, ad)

// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// h is used as the associated data for the AEAD in Session Confirmed part 2

End of "s" message pattern.

// Header encryption keys for this message
See Session Confirmed part 2 below
```
### SessionConfirmed (Tipo 2)

```
This is the "se" message pattern:

// DH(ask, bepk) == DH(besk, apk)
sharedSecret = DH(ask, bepk) = DH(besk, apk)

// MixKey(DH())
//[chainKey, k] = MixKey(sharedSecret)
keydata = HKDF(chainKey, sharedSecret, "", 64)
chainKey = keydata[0:31]

// AEAD parameters
k = keydata[32:63]
n = 0
ad = h
ciphertext = ENCRYPT(k, n, payload, ad)

// h from Session Confirmed part 1 is used as the associated data for the AEAD in Session Confirmed part 2
// MixHash(ciphertext)
h = SHA256(h || ciphertext);

// retain the chaining key ck for the data phase KDF
// retain the hash h for the data phase KDF

End of "se" message pattern.

// Header encryption keys for this message
// bik = Bob's intro key
k_header_1 = bik
k_header_2: See Session Created KDF above

// Header protection keys for data phase
See data phase KDF below
```
### KDF para fase de dados

Dados não criptografados (tags de autenticação Poly1305 não mostradas):

O tamanho mínimo da carga útil é de 8 bytes. Como o bloco RouterInfo será bem maior que isso, o requisito é atendido apenas com esse bloco.

1)  Bloco de Informações do Router da Alice (obrigatório)   2)  Bloco de Opções (opcional)   3)  Blocos I2NP (opcional)

```
XK(s, rs):           Authentication   Confidentiality
  -> s, se                  2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).  The
  sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key
  pair.  Assuming the corresponding private keys are secure, this
  authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.  This payload is
  encrypted based on an ephemeral-ephemeral DH as well as an ephemeral-static
  DH with the recipient's static key pair.  Assuming the ephemeral private
  keys are secure, and the recipient is not being actively impersonated by an
  attacker that has stolen its static private key, this payload cannot be
  decrypted.

  "s": Alice writes her static public key from the s variable into the
  message buffer, encrypting it, and hashes the output along with the old h
  to derive a new h.

  "se": A DH is performed between the Alice's static key pair and the Bob's
  ephemeral key pair.  The result is hashed along with the old ck to derive a
  new ck and k, and n is set to zero.
```
4\) Bloco de preenchimento (opcional) Este frame nunca deve conter nenhum outro tipo de bloco. TODO: e quanto ao relay e teste de peer?

A mensagem Session Confirmed deve conter o Router Info completo assinado de Alice para que Bob possa realizar várias verificações obrigatórias:

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with Bob intro key and     +
| derived key, see Header Encryption KDF|
+----+----+----+----+----+----+----+----+
|   ChaCha20 encrypted data (32 bytes)  |
+   Encrypted and authenticated data    +
+   Alice static key S                  +
| k defined in KDF for Session Created  |
+     n = 1                             +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+ Length varies (remainder of packet)   +
|                                       |
+   ChaCha20 encrypted data             +
|   see below for allowed blocks        |
+     k defined in KDF for              +
|     Session Confirmed part 2          |
+     n = 0                             +
|     see KDF for associated data       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+

S :: 32 bytes, ChaCha20 encrypted Alice's X25519 static key, little endian
     inside 48 byte ChaChaPoly frame
```
Infelizmente, o Router Info, mesmo quando comprimido com gzip no bloco RI, pode exceder o MTU. Portanto, o Session Confirmed pode ser fragmentado em dois ou mais pacotes. Este é o ÚNICO caso no protocolo SSU2 onde uma carga útil protegida por AEAD é fragmentada em dois ou mais pacotes.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|frag|  flags  |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|              S                        |
+       Alice static key                +
|          (32 bytes)                   |
+                                       +
|                                       |
+                                       +
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|        Noise Payload                  |
+        (length varies)                +
|        see below for allowed blocks   |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As sent in Session Request,
                             or one received in Session Confirmed?

Packet Number :: 0 always, for all fragments, even if retransmitted

type :: 2

frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number 0-14, big endian
       bits 3-0: total fragments 1-15, big endian

flags :: 2 bytes, unused, set to 0 for future compatibility

S :: 32 bytes, Alice's X25519 static key, little endian
```
#### Notas

- Bloco RouterInfo (deve ser o primeiro bloco)
- Bloco de Opções (opcional)
- Bloco de Novo Token (opcional)
- Bloco de Solicitação de Relay (opcional)
- Bloco de Teste de Peer (opcional)
- Bloco de Primeiro Número de Pacote (opcional)
- Blocos I2NP, Primeiro Fragmento, ou Fragmentos Subsequentes (opcional, mas provavelmente sem espaço)
- Bloco de Padding (opcional)

Os cabeçalhos para cada pacote são construídos da seguinte forma:

#### Payload

- Bob deve realizar a validação usual do Router Info. Certificar-se de que o tipo de assinatura é suportado, verificar a assinatura, verificar se o timestamp está dentro dos limites, e quaisquer outras verificações necessárias. Veja abaixo as notas sobre o manuseio de Router Infos fragmentados.

- Bob deve verificar se a chave estática de Alice recebida no primeiro quadro corresponde à chave estática no Router Info. Bob deve primeiro procurar no Router Info por um Router Address NTCP ou SSU2 com uma opção de versão (v) correspondente. Veja as seções Published Router Info e Unpublished Router Info abaixo. Veja abaixo as notas sobre como lidar com Router Infos fragmentados.

- Se Bob tem uma versão mais antiga do RouterInfo de Alice em sua netdb, verifique se a chave estática no router info é a mesma em ambos, se presente, e se a versão mais antiga tem menos de XXX de idade (veja o tempo de rotação de chave abaixo)

- Bob deve validar que a chave estática de Alice é um ponto válido na curva aqui.

- Opções devem ser incluídas, para especificar parâmetros de preenchimento.

- Em qualquer erro, incluindo falha de validação AEAD, RI, DH, timestamp ou chave, Bob deve interromper o processamento adicional de mensagens e fechar a conexão sem responder.

- Conteúdo do quadro da parte 2 da Mensagem 3: O formato deste quadro é o mesmo do formato dos quadros da fase de dados, exceto que o comprimento do quadro é enviado por Alice na Solicitação de Sessão. Veja abaixo o formato do quadro da fase de dados. O quadro deve conter de 1 a 4 blocos na seguinte ordem:

Construa a série de pacotes da seguinte forma:

Processo de remontagem:

- Bloco de preenchimento da parte 2 da mensagem 3 é recomendado.

- Pode não haver espaço, ou apenas uma pequena quantidade de espaço, disponível para blocos I2NP, dependendo do MTU e do tamanho do Router Info. NÃO inclua blocos I2NP se o Router Info estiver fragmentado. A implementação mais simples pode ser nunca incluir blocos I2NP na mensagem Session Confirmed, e enviar todos os blocos I2NP em mensagens Data subsequentes. Veja a seção de bloco Router Info abaixo para o tamanho máximo do bloco.

#### Carga útil

Quando Bob recebe qualquer mensagem Session Confirmed, ele descriptografa o cabeçalho, inspeciona o campo frag e determina que o Session Confirmed está fragmentado. Ele não (e não pode) descriptografar a mensagem até que todos os fragmentos sejam recebidos e remontados.

- A chave estática "s" no RI corresponde à chave estática no handshake
- A chave de introdução "i" no RI deve ser extraída e válida, para ser usada na fase de dados
- A assinatura do RI é válida

Não há mecanismo para Bob confirmar fragmentos individuais. Quando Bob recebe todos os fragmentos, os remonta, descriptografa e valida o conteúdo, Bob faz um split() como de costume, entra na fase de dados e envia um ACK do pacote número 0.

Se Alice não receber um ACK do pacote número 0, ela deve retransmitir todos os pacotes confirmados de sessão como estão.

- TODOS os cabeçalhos são cabeçalhos curtos com o mesmo número de pacote 0
- TODOS os cabeçalhos contêm um campo "frag", com o número do fragmento e o número total de fragmentos
- O cabeçalho não criptografado do fragmento 0 é os dados associados (AD) para a mensagem "jumbo"
- Cada cabeçalho é criptografado usando os últimos 24 bytes de dados NESSE pacote

Exemplos:

- Criar um único bloco RI (fragmento 0 de 1 no campo frag do bloco RI). Não usamos fragmentação de bloco RI, isso era para um método alternativo de resolver o mesmo problema.
- Criar uma carga útil "jumbo" com o bloco RI e quaisquer outros blocos a serem incluídos
- Calcular o tamanho total dos dados (não incluindo o cabeçalho), que é o tamanho da carga útil + 64 bytes para a chave estática e dois MACs
- Calcular o espaço disponível em cada pacote, que é o MTU menos o cabeçalho IP (20 ou 40), menos o cabeçalho UDP (8), menos o cabeçalho curto SSU2 (16). O overhead total por pacote é 44 (IPv4) ou 64 (IPv6).
- Calcular o número de pacotes.
- Calcular o tamanho dos dados no último pacote. Deve ser maior ou igual a 24 bytes, para que a criptografia do cabeçalho funcione. Se for muito pequeno, adicionar um bloco de preenchimento, OU aumentar o tamanho do bloco de preenchimento se já estiver presente, OU reduzir o tamanho de um dos outros pacotes para que o último pacote seja grande o suficiente.
- Criar o cabeçalho não criptografado para o primeiro pacote, com o número total de fragmentos no campo frag, e criptografar a carga útil "jumbo" com Noise, usando o cabeçalho como AD, como de costume.
- Dividir o pacote jumbo criptografado em fragmentos
- Adicionar um cabeçalho não criptografado para cada fragmento 1-n
- Criptografar o cabeçalho para cada fragmento 0-n. Cada cabeçalho usa os MESMOS k_header_1 e k_header_2 conforme definido acima no KDF Session Confirmed.
- Transmitir todos os fragmentos

Para MTU de 1500 sobre IPv6, o payload máximo é 1372, a sobrecarga do bloco RI é 5, o tamanho máximo dos dados RI (comprimidos com gzip) é 1367 (assumindo nenhum outro bloco). Com dois pacotes, a sobrecarga do 2º pacote é 64, então ele pode conter outros 1436 bytes de payload. Portanto, dois pacotes são suficientes para um RI comprimido de até 2803 bytes.

O maior RI comprimido visto na rede atual tem cerca de 1400 bytes; portanto, na prática, dois fragmentos devem ser suficientes, mesmo com um MTU mínimo de 1280. O protocolo permite no máximo 15 fragmentos.

- Preservar o cabeçalho para o fragmento 0, pois é usado como AD do Noise
- Descartar os cabeçalhos para outros fragmentos antes da remontagem
- Remontar a carga útil "jumbo", com o cabeçalho para o fragmento 0 como AD, e descriptografar com Noise
- Validar o bloco RI como de costume
- Proceder para a fase de dados e enviar ACK 0, como de costume

Análise de segurança:

A integridade e segurança de uma Session Confirmed fragmentada é a mesma que a de uma não fragmentada. Qualquer alteração de qualquer fragmento fará com que o Noise AEAD falhe após a remontagem. Os cabeçalhos dos fragmentos após o fragmento 0 são usados apenas para identificar o fragmento. Mesmo se um atacante no caminho tivesse a chave k_header_2 usada para criptografar o cabeçalho (improvável, derivada do handshake), isso não permitiria ao atacante substituir um fragmento válido.

A fase de dados usa o cabeçalho para dados associados.

O KDF gera duas chaves de cifra k_ab e k_ba a partir da chaining key ck, usando HMAC-SHA256(key, data) conforme definido em [RFC-2104](https://tools.ietf.org/html/rfc2104). Esta é a função split(), exatamente como definido na especificação Noise.

Payload de ruído: Todos os tipos de bloco são permitidos Tamanho máximo do payload: MTU - 60 (IPv4) ou MTU - 80 (IPv6). Para MTU 1500: Payload máximo é 1440 (IPv4) ou 1420 (IPv6).

Começando com a 2ª parte do Session Confirmed, todas as mensagens estão dentro de um payload ChaChaPoly autenticado e criptografado. Todo o preenchimento está dentro da mensagem. Dentro do payload há um formato padrão com zero ou mais "blocos". Cada bloco tem um tipo de um byte e um comprimento de dois bytes. Os tipos incluem data/hora, mensagem I2NP, opções, terminação e preenchimento.

Nota: Bob pode, mas não é obrigatório, enviar suas RouterInfo para Alice como sua primeira mensagem para Alice na fase de dados.

### Mensagem de Dados (Tipo 6)

Propriedades de Segurança do Payload:

Dados não criptografados (tag de autenticação Poly1305 não mostrada):

```
// split()
// chainKey = from handshake phase
keydata = HKDF(chainKey, ZEROLEN, "", 64)
k_ab = keydata[0:31]
k_ba = keydata[32:63]

// key is k_ab for Alice to Bob
// key is k_ba for Bob to Alice

keydata = HKDF(key, ZEROLEN, "HKDFSSU2DataKeys", 64)
k_data = keydata[0:31]
k_header_2 = keydata[32:63]


// AEAD parameters
k = k_data
n = 4 byte packet number from header
ad = 16 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for data phase
// aik = Alice's intro key
// bik = Bob's intro key
k_header_1 = Receiver's intro key (aik or bik)
k_header_2: from above
```
### KDF para Teste de Pares

Charlie envia para Alice, e Alice envia para Charlie, apenas para as fases 5-7 do Peer Test. As fases 1-4 do Peer Test devem ser enviadas dentro da sessão usando um bloco Peer Test numa mensagem Data. Consulte as seções Bloco Peer Test e Processo Peer Test abaixo para mais informações.

Tamanho: 48 + tamanho da carga útil.

Payload do Noise: Veja abaixo.

Conteúdo bruto:

```
XK(s, rs):           Authentication   Confidentiality
  <-                        2                5
  ->                        2                5

  Authentication: 2.
  Sender authentication resistant to key-compromise impersonation (KCI).
  The sender authentication is based on an ephemeral-static DH ("es" or "se")
  between the sender's static key pair and the recipient's ephemeral key pair.
  Assuming the corresponding private keys are secure, this authentication cannot be forged.

  Confidentiality: 5.
  Encryption to a known recipient, strong forward secrecy.
  This payload is encrypted based on an ephemeral-ephemeral DH as well as
  an ephemeral-static DH with the recipient's static key pair.
  Assuming the ephemeral private keys are secure, and the recipient is not being actively impersonated
  by an attacker that has stolen its static private key, this payload cannot be decrypted.
```
#### Notas

- O router deve descartar uma mensagem com erro AEAD.

```
+----+----+----+----+----+----+----+----+
|  Short Header 16 bytes, ChaCha20      |
+  encrypted with intro key and         +
|  derived key, see Data Phase KDF      |
+----+----+----+----+----+----+----+----+
|   ChaCha20 data                       |
+   Encrypted and authenticated data    +
|  length varies                        |
+  k defined in Data Phase KDF          +
|  n = packet number from header        |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Dados não criptografados (tag de autenticação Poly1305 não mostrada):

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|flag|moreflags|
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|                                       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: As specified in session setup

Packet Number :: 4 byte big endian integer

type :: 6

flag :: 1 byte flags:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-1: unused, set to 0 for future compatibility
       bits 0: when set to 1, immediate ack requested

moreflags :: 2 bytes, unused, set to 0 for future compatibility
```
#### Carga útil

- O tamanho mínimo do payload é de 8 bytes. Este requisito será atendido por qualquer bloco ACK, I2NP, First Fragment ou Follow-on Fragment. Se o requisito não for atendido, um bloco Padding deve ser incluído.
- Cada número de pacote pode ser usado apenas uma vez. Ao retransmitir mensagens I2NP ou fragmentos, um novo número de pacote deve ser usado.

### Teste de Peer (Tipo 7)

```
// AEAD parameters
// aik = Alice's intro key
k = aik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = aik
k_header_2 = aik
```
### KDF para Retry

O tamanho mínimo da carga útil é de 8 bytes. Uma vez que o bloco Peer Test totaliza mais do que isso, o requisito é atendido apenas com este bloco.

Nas mensagens 5 e 7, o bloco Peer Test pode ser idêntico ao bloco das mensagens 3 e 4 da sessão, contendo o acordo assinado por Charlie, ou pode ser regenerado. A assinatura é opcional.

Na mensagem 6, o bloco Peer Test pode ser idêntico ao bloco das mensagens na sessão 1 e 2, contendo a solicitação assinada por Alice, ou pode ser regenerado. A assinatura é opcional.

Connection IDs: Os dois connection IDs são derivados do test nonce. Para as mensagens 5 e 7 enviadas do Charlie para a Alice, o Destination Connection ID são duas cópias do test nonce de 4 bytes em big-endian, ou seja, ((nonce << 32) | nonce). O Source Connection ID é o inverso do Destination Connection ID, ou seja, ~((nonce << 32) | nonce). Para a mensagem 6 enviada da Alice para o Charlie, trocar os dois connection IDs.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice intro key       +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Conteúdo do bloco de endereços:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: Randomly generated by Alice

Packet Number :: Random number generated by Alice

type :: 10

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: Randomly generated by Alice,
                        must not be equal to Destination Connection ID

Token :: zero
```
#### Notas

- Bloco DateTime
- Bloco Address (obrigatório para mensagens 6 e 7, veja nota abaixo)
- Bloco Peer Test
- Bloco Padding (opcional)

O requisito para a mensagem Retry é que Bob não é obrigatório a descriptografar a mensagem Session Request para gerar uma mensagem Retry em resposta. Além disso, esta mensagem deve ser rápida de gerar, usando apenas criptografia simétrica.

Bob envia para Alice, em resposta a uma mensagem Session Request ou Token Request. Alice responde com um novo Session Request. Tamanho: 48 + tamanho do payload.

Também serve como uma mensagem de Terminação (ou seja, "Não Tente Novamente") se um bloco de Terminação for incluído.

Payload do Noise: Veja abaixo.

Conteúdo bruto:

- Na mensagem 5: Não obrigatório.
- Na mensagem 6: IP e porta do Charlie conforme selecionados do RI do Charlie.
- Na mensagem 7: IP e porta reais da Alice de onde a mensagem 6 foi recebida.

### Repetir (Tipo 9)

Dados não criptografados (tag de autenticação Poly1305 não mostrada):

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### KDF para Solicitação de Token

O tamanho mínimo do payload é de 8 bytes. Uma vez que os blocos DateTime e Address totalizam mais que isso, o requisito é atendido apenas com esses dois blocos.

Esta mensagem deve ser rápida de gerar, usando apenas criptografia simétrica.

Alice envia para Bob. Bob responde com uma mensagem Retry. Tamanho: 48 + tamanho do payload.

Se Alice não possui um token válido, Alice deve enviar esta mensagem em vez de uma Session Request, para evitar a sobrecarga de criptografia assimétrica na geração de uma Session Request.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Payload do Noise: Veja abaixo.

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: The Source Connection ID
                             received from Alice in Token Request
                             or Session Request

Packet Number :: Random number generated by Bob

type :: 9

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Source Connection ID :: The Destination Connection ID
                        received from Alice in Token Request
                        or Session Request

Token :: 8 byte unsigned integer, randomly generated by Bob, nonzero,
         or zero if session is rejected and a termination block is included
```
#### Carga útil

- Bloco DateTime
- Bloco Address
- Bloco Options (opcional)
- Bloco Termination (opcional, se a sessão for rejeitada)
- Bloco Padding (opcional)

Conteúdo bruto:

#### DataHora

- Para fornecer resistência a sondagem, um router não deve enviar uma mensagem Retry em resposta a uma mensagem Session Request ou Token Request, a menos que os campos de tipo de mensagem, versão do protocolo e ID da rede na mensagem Request sejam válidos.
- Para limitar a magnitude de qualquer ataque de amplificação que possa ser montado usando endereços de origem falsificados, a mensagem Retry não deve conter grandes quantidades de preenchimento. É recomendado que a mensagem Retry não seja maior que três vezes o tamanho da mensagem à qual está respondendo. Alternativamente, use um método simples como adicionar uma quantidade aleatória de preenchimento no intervalo de 1-64 bytes.

### Solicitação de Token (Tipo 10)

Dados não criptografados (tag de autenticação Poly1305 não mostrada):

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### KDF para Hole Punch

O tamanho mínimo do payload é 8 bytes.

Esta mensagem deve ser rápida de gerar, usando apenas criptografia simétrica.

Charlie envia para Alice, em resposta a um Relay Intro recebido de Bob. Alice responde com uma nova Session Request. Tamanho: 48 + tamanho do payload.

Payload do Noise: Veja abaixo.

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Bob intro key         +
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Conteúdo bruto:

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type|    flags     |
+----+----+----+----+----+----+----+----+
|     Noise payload (block data)        |
+          (length varies)              +
|                                       |
+----+----+----+----+----+----+----+----+

Destination Connection ID :: As specified in session setup

Packet Number :: 4 byte big endian integer

type :: 6

flags :: 3 bytes, unused, set to 0 for future compatibility
```
#### Opções

- Bloco DateTime
- Bloco de preenchimento

Dados não criptografados (tag de autenticação Poly1305 não mostrada):

#### RouterInfo

- Para fornecer resistência a sondagem, um router não deve enviar uma mensagem Retry em resposta a uma mensagem Token Request, a menos que os campos de tipo de mensagem, versão do protocolo e ID da rede na mensagem Token Request sejam válidos.
- Esta NÃO é uma mensagem Noise padrão e não faz parte do handshake. Não está vinculada à mensagem Session Request além de pelos IDs de conexão.
- Na maioria dos erros, incluindo AEAD, ou replay aparente, Bob deve interromper o processamento adicional de mensagens e descartar a mensagem sem responder.
- Bob deve rejeitar conexões onde o valor do timestamp está muito distante do tempo atual. Chame o tempo delta máximo de "D". Bob deve manter um cache local de valores de handshake usados anteriormente e rejeitar duplicatas, para prevenir ataques de replay. Os valores no cache devem ter um tempo de vida de pelo menos 2*D. Os valores do cache são dependentes da implementação, no entanto o valor X de 32 bytes (ou seu equivalente encriptado) pode ser usado.
- Bob PODE enviar uma mensagem Retry contendo um token zero e um bloco Termination com um código de razão de clock skew se o timestamp no bloco DateTime estiver muito desalinhado.
- Tamanho mínimo: TBD, mesmas regras que para Session Created?

### Hole Punch (Tipo 11)

O tamanho mínimo da carga útil é de 8 bytes. Como os blocos DateTime e Address totalizam mais que isso, o requisito é atendido apenas com esses dois blocos.

```
// AEAD parameters
// bik = Bob's intro key
k = bik
n = 4 byte packet number from header
ad = 32 byte header, before header encryption
ciphertext = ENCRYPT(k, n, payload, ad)

// Header encryption keys for this message
k_header_1 = bik
k_header_2 = bik
```
### Formato da Carga Útil

IDs de Conexão: Os dois IDs de conexão são derivados do nonce de retransmissão. O ID de Conexão de Destino são duas cópias do nonce de retransmissão de 4 bytes em big-endian, ou seja, ((nonce << 32) | nonce). O ID de Conexão de Origem é o inverso do ID de Conexão de Destino, ou seja, ~((nonce << 32) | nonce).

Alice deve ignorar o token no cabeçalho. O token a ser usado na Solicitação de Sessão está no bloco de Resposta de Relay.

Cada payload Noise contém zero ou mais "blocos".

```
+----+----+----+----+----+----+----+----+
|  Long Header bytes 0-15, ChaCha20     |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|  Long Header bytes 16-31, ChaCha20    |
+  encrypted with Alice or Charlie      +
|  intro key                            |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|   ChaCha20 encrypted data             |
+          (length varies)              +
|                                       |
+  see KDF for key and n                +
|  see KDF for associated data          |
+----+----+----+----+----+----+----+----+
|                                       |
+        Poly1305 MAC (16 bytes)        +
|                                       |
+----+----+----+----+----+----+----+----+
```
Isso usa o mesmo formato de bloco definido nas especificações [NTCP2](/docs/specs/ntcp2) e [ECIES](/docs/specs/ecies). Os tipos de blocos individuais são definidos de forma diferente. O termo equivalente em QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) é "frames".

```
+----+----+----+----+----+----+----+----+
|      Destination Connection ID        |
+----+----+----+----+----+----+----+----+
|   Packet Number   |type| ver| id |flag|
+----+----+----+----+----+----+----+----+
|        Source Connection ID           |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+
|    ChaCha20 payload (block data)      |
+          (length varies)              +
|    see below for allowed blocks       |
+----+----+----+----+----+----+----+----+


Destination Connection ID :: See below

type :: 7

ver :: 2

id :: 1 byte, the network ID (currently 2, except for test networks)

flag :: 1 byte, unused, set to 0 for future compatibility

Packet Number :: Random number generated by Alice or Charlie

Source Connection ID :: See below

Token :: Randomly generated by Alice or Charlie, ignored
```
#### Mensagem I2NP

- Bloco DateTime
- Bloco Address
- Bloco Relay Response
- Bloco Padding (opcional)

Existem preocupações de que encorajar implementadores a compartilhar código possa levar a problemas de análise. Os implementadores devem considerar cuidadosamente os benefícios e riscos de compartilhar código, e garantir que as regras de ordenação e blocos válidos sejam diferentes para os dois contextos.

Há um ou mais blocos no payload criptografado. Um bloco é um formato Tag-Length-Value (TLV) simples. Cada bloco contém um identificador de um byte, um comprimento de dois bytes e zero ou mais bytes de dados. Este formato é idêntico ao usado em [NTCP2](/docs/specs/ntcp2) e [ECIES](/docs/specs/ecies), no entanto, as definições dos blocos são diferentes.

Para extensibilidade, os receptores devem ignorar blocos com identificadores desconhecidos e tratá-los como preenchimento.

## Payload de Ruído

(Tag de autenticação Poly1305 não mostrada):

A criptografia do cabeçalho usa os últimos 24 bytes do pacote como o IV para as duas operações ChaCha20. Como todos os pacotes terminam com um MAC de 16 bytes, isso exige que todas as cargas úteis dos pacotes tenham um mínimo de 8 bytes. Se uma carga útil não atenderia a esse requisito, um bloco de Padding deve ser incluído.

O payload máximo do ChaChaPoly varia com base no tipo de mensagem, MTU e tipo de endereço IPv4 ou IPv6. O payload máximo é MTU - 60 para IPv4 e MTU - 80 para IPv6. Os dados de payload máximos são MTU - 63 para IPv4 e MTU - 83 para IPv6. O limite superior é de cerca de 1440 bytes para IPv4, MTU 1500, mensagem de dados. O tamanho máximo total do bloco é o tamanho máximo do payload. O tamanho máximo de bloco único é o tamanho máximo total do bloco. O tipo de bloco é 1 byte. O comprimento do bloco é 2 bytes. O tamanho máximo de dados de bloco único é o tamanho máximo de bloco único menos 3.

### Regras de Ordenação de Blocos

Notas:

Tipos de bloco:

Na Session Confirmed, Router Info deve ser o primeiro bloco.

```
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
|blk |  size   |       data             |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+
~               .   .   .               ~

blk :: 1 byte, see below
size :: 2 bytes, big endian, size of data to follow, 0 - TBD
data :: the data
```
Em todas as outras mensagens, a ordem não é especificada, exceto pelos seguintes requisitos: Padding, se presente, deve ser o último bloco. Termination, se presente, deve ser o último bloco exceto pelo Padding. Múltiplos blocos Padding não são permitidos em uma única payload.

Para sincronização de horário:

Notas:

- Os implementadores devem garantir que ao ler um bloco, dados malformados ou maliciosos não causem leituras que ultrapassem o próximo bloco ou além do limite do payload.
- As implementações devem ignorar tipos de blocos desconhecidos para compatibilidade futura.

Passar opções atualizadas. As opções incluem: Preenchimento mínimo e máximo.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Payload Block Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type Number</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Block Length</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime</td><td style="border:1px solid var(--color-border); padding:0.6rem;">0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Options</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15+</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Router Info</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">I2NP Message</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Follow-on Fragment</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Termination</td><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 typ.</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">8</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Intro</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Peer Test</td><td style="border:1px solid var(--color-border); padding:0.6rem;">10</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Next Nonce</td><td style="border:1px solid var(--color-border); padding:0.6rem;">11</td><td style="border:1px solid var(--color-border); padding:0.6rem;">TBD</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">ACK</td><td style="border:1px solid var(--color-border); padding:0.6rem;">12</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Address</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">9 or 21</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved</td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;">--</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Relay Tag</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">New Token</td><td style="border:1px solid var(--color-border); padding:0.6rem;">17</td><td style="border:1px solid var(--color-border); padding:0.6rem;">15</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Challenge</td><td style="border:1px solid var(--color-border); padding:0.6rem;">18</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Path Response</td><td style="border:1px solid var(--color-border); padding:0.6rem;">19</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">First Packet Number</td><td style="border:1px solid var(--color-border); padding:0.6rem;">20</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Congestion</td><td style="border:1px solid var(--color-border); padding:0.6rem;">21</td><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for experimental features</td><td style="border:1px solid var(--color-border); padding:0.6rem;">224-253</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Padding</td><td style="border:1px solid var(--color-border); padding:0.6rem;">254</td><td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">reserved for future extension</td><td style="border:1px solid var(--color-border); padding:0.6rem;">255</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>           
### Especificações de Bloco

O bloco de opções terá comprimento variável.

Problemas de Opções:

### Solicitação de Sessão

#### Primeiro Fragmento

Passa o RouterInfo da Alice para o Bob. Usado apenas na parte 2 do payload de Session Confirmed. Não deve ser usado na fase de dados; use uma Mensagem I2NP DatabaseStore em vez disso.

```
+----+----+----+----+----+----+----+
| 0  |    4    |     timestamp     |
+----+----+----+----+----+----+----+

blk :: 0
size :: 2 bytes, big endian, value = 4
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
```
Tamanho Mínimo: Cerca de 420 bytes, a menos que a identidade do router e a assinatura nas informações do router sejam compressíveis, o que é improvável.

- Ao contrário do SSU 1, não há timestamp no cabeçalho do pacote para a fase de dados no SSU 2.
- As implementações devem enviar periodicamente blocos DateTime na fase de dados.
- As implementações devem arredondar para o segundo mais próximo para prevenir desvio de relógio na rede.

#### Fragmento de Continuação

NOTA: O bloco Router Info nunca é fragmentado. O campo frag é sempre 0/1. Consulte a seção Fragmentação de Sessão Confirmada acima para mais informações.

Notas:

```
+----+----+----+----+----+----+----+----+
| 1  |  size   |tmin|tmax|rmin|rmax|tdmy|
+----+----+----+----+----+----+----+----+
|tdmy|  rdmy   |  tdelay |  rdelay |    |
~----+----+----+----+----+----+----+    ~
|              more_options             |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 1
size :: 2 bytes, big endian, size of options to follow, 12 bytes minimum

tmin, tmax, rmin, rmax :: requested padding limits
    tmin and rmin are for desired resistance to traffic analysis.
    tmax and rmax are for bandwidth limits.
    tmin and tmax are the transmit limits for the router sending this options block.
    rmin and rmax are the receive limits for the router sending this options block.
    Each is a 4.4 fixed-point float representing 0 to 15.9375
    (or think of it as an unsigned 8-bit integer divided by 16.0).
    This is the ratio of padding to data. Examples:
    Value of 0x00 means no padding
    Value of 0x01 means add 6 percent padding
    Value of 0x10 means add 100 percent padding
    Value of 0x80 means add 800 percent (8x) padding
    Alice and Bob will negotiate the minimum and maximum in each direction.
    These are guidelines, there is no enforcement.
    Sender should honor receiver's maximum.
    Sender may or may not honor receiver's minimum, within bandwidth constraints.

tdmy: Max dummy traffic willing to send, 2 bytes big endian, bytes/sec average
rdmy: Requested dummy traffic, 2 bytes big endian, bytes/sec average
tdelay: Max intra-message delay willing to insert, 2 bytes big endian, msec average
rdelay: Requested intra-message delay, 2 bytes big endian, msec average

Padding distribution specified as additional parameters?
Random delay specified as additional parameters?

more_options :: Format TBD
```
Uma mensagem I2NP completa com um cabeçalho modificado.

- A negociação de opções está por definir (TBD).

#### Terminação

Isso usa os mesmos 9 bytes para o cabeçalho I2NP como em [NTCP2](/docs/specs/ntcp2) (tipo, id da mensagem, expiração curta).

Notas:

O primeiro fragmento (fragmento #0) de uma mensagem I2NP com um cabeçalho modificado.

```
+----+----+----+----+----+----+----+----+
| 2  |  size   |flag|frag|              |
+----+----+----+----+----+              +
|                                       |
+       Router Info fragment            +
| (Alice RI in Session Confirmed)       |
+ (Alice, Bob, or third-party           +
|  RI in data phase)                    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 2
size :: 2 bytes, big endian, 2 + fragment size
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 0 for local store, 1 for flood request
       bit 1: 0 for uncompressed, 1 for gzip compressed
       bits 7-2: Unused, set to 0 for future compatibility
frag :: 1 byte fragment info:
       bit order: 76543210 (bit 7 is MSB)
       bits 7-4: fragment number, always 0
       bits 3-0: total fragments, always 1, big endian

routerinfo :: Alice's or Bob's RouterInfo
```
Isto usa os mesmos 9 bytes para o cabeçalho I2NP como em [NTCP2](/docs/specs/ntcp2) (tipo, id da mensagem, expiração curta).

- A Router Info é opcionalmente comprimida com gzip, conforme indicado pelo bit 1 da flag. Isso é diferente do NTCP2, onde nunca é comprimida, e de uma DatabaseStore Message, onde sempre é comprimida. A compressão é opcional porque geralmente oferece pouco benefício para Router Infos pequenas, onde há pouco conteúdo comprimível, mas é muito benéfica para Router Infos grandes com vários Router Addresses comprimíveis. A compressão é recomendada se permitir que uma Router Info caiba em um único pacote Session Confirmed sem fragmentação.
- Tamanho máximo do primeiro ou único fragmento na mensagem Session Confirmed: MTU - 113 para IPv4 ou MTU - 133 para IPv6. Assumindo MTU padrão de 1500 bytes, e nenhum outro bloco na mensagem, 1387 para IPv4 ou 1367 para IPv6. 97% das router infos atuais são menores que 1367 sem compressão gzip. 99,9% das router infos atuais são menores que 1367 quando comprimidas com gzip. Assumindo MTU mínimo de 1280 bytes, e nenhum outro bloco na mensagem, 1167 para IPv4 ou 1147 para IPv6. 94% das router infos atuais são menores que 1147 sem compressão gzip. 97% das router infos atuais são menores que 1147 quando comprimidas com gzip.
- O byte frag agora está sem uso, o bloco Router Info nunca é fragmentado. O byte frag deve ser definido como fragmento 0, total de fragmentos 1. Veja a seção Fragmentação Session Confirmed acima para mais informações.
- O flooding não deve ser solicitado a menos que existam RouterAddresses publicados na RouterInfo. O router receptor não deve fazer flood da RouterInfo a menos que existam RouterAddresses publicados nela.
- Este protocolo não fornece uma confirmação de que a RouterInfo foi armazenada ou teve flood feito. Se for desejada confirmação, e o receptor for floodfill, o remetente deve em vez disso enviar uma I2NP DatabaseStoreMessage padrão com um token de resposta.

#### RelayRequest

O número total de fragmentos não está especificado.

Notas:

```
+----+----+----+----+----+----+----+----+
| 3  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |     message       |
+----+----+----+----+                   +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 3
size :: 2 bytes, big endian, size of type + msg id + exp + message to follow
        I2NP message body size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: I2NP message body
```
Um fragmento adicional (número do fragmento maior que zero) de uma mensagem I2NP.

- Este é o mesmo formato de cabeçalho I2NP de 9 bytes usado no NTCP2.
- Este é exatamente o mesmo formato do bloco First Fragment, mas o tipo de bloco indica que esta é uma mensagem completa.
- O tamanho máximo incluindo o cabeçalho I2NP de 9 bytes é MTU - 63 para IPv4 e MTU - 83 para IPv6.

#### RelayResponse

Notas:

Encerre a conexão. Este deve ser o último bloco não-padding no payload.

Notas:

```
+----+----+----+----+----+----+----+----+
| 4  |  size   |type|    msg id         |
+----+----+----+----+----+----+----+----+
|   short exp       |                   |
+----+----+----+----+                   +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 4
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 9).
type :: 1 byte, I2NP msg type, see I2NP spec
msg id :: 4 bytes, big endian, I2NP message ID
short exp :: 4 bytes, big endian, I2NP message expiration, Unix timestamp, unsigned seconds.
             Wraps around in 2106
message :: Partial I2NP message body, bytes 0 - (size - 10)
```
Enviado em uma mensagem Data dentro da sessão, de Alice para Bob. Veja a seção Processo de Relay abaixo.

- Este é o mesmo formato de cabeçalho I2NP de 9 bytes usado no NTCP2.
- Este é exatamente o mesmo formato que o bloco de Mensagem I2NP, mas o tipo de bloco indica que este é o primeiro fragmento de uma mensagem.
- O comprimento da mensagem parcial deve ser maior que zero.
- Como no SSU 1, é recomendado enviar o último fragmento primeiro, para que o receptor saiba o número total de fragmentos e possa alocar buffers de recepção de forma eficiente.
- O tamanho máximo incluindo o cabeçalho I2NP de 9 bytes é MTU - 63 para IPv4 e MTU - 83 para IPv6.

#### RelayIntro

Notas:

```
+----+----+----+----+----+----+----+----+
| 5  |  size   |frag|    msg id         |
+----+----+----+----+----+----+----+----+
|                                       |
+                                       +
|          partial message              |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 5
size :: 2 bytes, big endian, size of data to follow
        Fragment size is (size - 5).
frag :: Fragment info:
        Bit order: 76543210 (bit 7 is MSB)
        bits 7-1: fragment number 1 - 127 (0 not allowed)
        bit 0: isLast (1 = true)
msg id :: 4 bytes, big endian, I2NP message ID
message :: Partial I2NP message body
```
Assinatura:

- O comprimento da mensagem parcial deve ser maior que zero.
- Como no SSU 1, é recomendado enviar o último fragmento primeiro, para que o receptor saiba o número total de fragmentos e possa alocar eficientemente os buffers de recepção.
- Como no SSU 1, o número máximo de fragmentos é 127, mas o limite prático é 63 ou menos. As implementações podem limitar o máximo ao que é prático para um tamanho máximo de mensagem I2NP de cerca de 64 KB, que é cerca de 55 fragmentos com um MTU mínimo de 1280. Veja a seção Tamanho Máximo de Mensagem I2NP abaixo.
- O tamanho máximo da mensagem parcial (não incluindo frag e message id) é MTU - 68 para IPv4 e MTU - 88 para IPv6.

#### PeerTest

Alice assina a solicitação e a inclui neste bloco; Bob a encaminha no bloco Relay Intro para Charlie. Algoritmo de assinatura: Assine os seguintes dados com a chave de assinatura do router da Alice:

```
+----+----+----+----+----+----+----+----+
| 6  |  size   |    valid data packets  |
+----+----+----+----+----+----+----+----+
    received   | rsn|     addl data     |
+----+----+----+----+                   +
~               .   .   .               ~
+----+----+----+----+----+----+----+----+

blk :: 6
size :: 2 bytes, big endian, value = 9 or more
valid data packets received :: The number of valid packets received
                              (current receive nonce value)
                              0 if error occurs in handshake phase
                              8 bytes, big endian
rsn :: reason, 1 byte:
       0: normal close or unspecified
       1: termination received
       2: idle timeout
       3: router shutdown
       4: data phase AEAD failure
       5: incompatible options
       6: incompatible signature type
       7: clock skew
       8: padding violation
       9: AEAD framing error
       10: payload format error
       11: Session Request error
       12: Session Created error
       13: Session Confirmed error
       14: Timeout
       15: RI signature verification fail
       16: s parameter missing, invalid, or mismatched in RouterInfo
       17: banned
       18: bad token
       19: connection limits
       20: incompatible version
       21: wrong net ID
       22: replaced by new session
addl data :: optional, 0 or more bytes, for future expansion, debugging,
             or reason text.
             Format unspecified and may vary based on reason code.
```
Enviado em uma mensagem Data na sessão, de Charlie para Bob ou de Bob para Alice, E na mensagem Hole Punch de Charlie para Alice. Veja a seção Processo de Relay abaixo.

- Nem todas as razões podem ser realmente usadas, dependente da implementação. A maioria das falhas geralmente resultará na mensagem sendo descartada, não em uma terminação. Veja as notas nas seções de mensagem de handshake acima. Razões adicionais listadas são para consistência, registro, depuração, ou se as políticas mudarem.
- É recomendado que um bloco ACK seja incluído com o bloco de Terminação.
- Na fase de dados, para qualquer razão que não seja "termination received", o peer deve responder com um bloco de terminação com a razão "termination received".

#### NextNonce

Notas:

```
+----+----+----+----+----+----+----+----+
|  7 |  size   |flag|       nonce       |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 7
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility

The data below here is covered
by the signature, and Bob forwards it unmodified.

nonce :: 4 bytes, randomly generated by Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
O token deve ser usado imediatamente pela Alice na Solicitação de Sessão.

- O endereço IP está sempre incluído (ao contrário do SSU 1) e pode ser diferente do IP usado para a sessão.

Assinatura:

Se Charlie concordar (código de resposta 0) ou rejeitar (código de resposta 64 ou superior), Charlie assina a resposta e a inclui neste bloco; Bob a encaminha no bloco Relay Response para Alice. Algoritmo de assinatura: Assinar os seguintes dados com a chave de assinatura do router de Charlie:

- prólogo: 16 bytes "RelayRequestData", não terminado por null (não incluído na mensagem)
- bhash: hash do router de Bob de 32 bytes (não incluído na mensagem)
- chash: hash do router de Charlie de 32 bytes (não incluído na mensagem)
- nonce: nonce de 4 bytes
- relay tag: tag de relay de 4 bytes
- timestamp: timestamp de 4 bytes (segundos)
- ver: versão SSU de 1 byte
- asz: tamanho do endpoint (porta + IP) de 1 byte (6 ou 18)
- AlicePort: número da porta de Alice de 2 bytes
- Alice IP: endereço IP de Alice de (asz - 2) bytes

#### Confirmação

Se Bob rejeitar (código de resposta 1-63), Bob assina a resposta e a inclui neste bloco. Algoritmo de assinatura: Assinar os seguintes dados com a chave de assinatura do router do Bob:

```
+----+----+----+----+----+----+----+----+
|  8 |  size   |flag|code|    nonce
+----+----+----+----+----+----+----+----+
     |     timestamp     | ver| csz|Char
+----+----+----+----+----+----+----+----+
 Port|   Charlie IP addr |              |
+----+----+----+----+----+              +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+
|                 Token                 |
+----+----+----+----+----+----+----+----+

blk :: 8
size :: 2 bytes, 6
flag :: 1 byte flags, Unused, set to 0 for future compatibility
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, Charlie is banned
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, relay tag not found
       6: rejected by Bob, Alice RI not found
       7-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       71-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD

The data below is covered by the signature if the code is 0 (accept).
Bob forwards it unmodified.

nonce :: 4 bytes, as received from Bob or Alice

The data below is present only if the code is 0 (accept).

timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
csz :: 1 byte endpoint (port + IP) size (0 or 6 or 18)
       may be 0 for some rejection codes
CharliePort :: 2 byte Charlie's port number, big endian
               not present if csz is 0
Charlie IP :: (csz - 2) byte representation of Charlie's IP address,
              network byte order
              not present if csz is 0
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Charlie.
             Not present if rejected by Bob.
token :: Token generated by Charlie for Alice to use
         in the Session Request.
         Only present if code is 0 (accept)
```
Enviado numa mensagem Data dentro da sessão, de Bob para Charlie. Veja a seção Processo de Relay abaixo.

Deve ser precedido por um bloco RouterInfo, ou bloco de mensagem I2NP DatabaseStore (ou fragmento), contendo as Informações do Router da Alice, seja na mesma carga útil (se houver espaço), ou em uma mensagem anterior.

Notas:

Assinatura:

- prólogo: 16 bytes "RelayAgreementOK", não terminado em null (não incluído na mensagem)
- bhash: Hash do router de Bob de 32 bytes (não incluído na mensagem)
- nonce: nonce de 4 bytes
- timestamp: timestamp de 4 bytes (segundos)
- ver: versão SSU de 1 byte
- csz: tamanho do endpoint (porta + IP) de 1 byte (0 ou 6 ou 18)
- CharliePort: número da porta de Charlie de 2 bytes (não presente se csz for 0)
- Charlie IP: endereço IP de Charlie de (csz - 2) bytes (não presente se csz for 0)

Alice assina a solicitação e Bob a encaminha neste bloco para Charlie. Algoritmo de verificação: Verifique os seguintes dados com a chave de assinatura do router de Alice:

- prologue: 16 bytes "RelayAgreementOK", não terminado em null (não incluído na mensagem)
- bhash: Hash do router de 32 bytes do Bob (não incluído na mensagem)
- nonce: nonce de 4 bytes
- timestamp: timestamp de 4 bytes (segundos)
- ver: versão SSU de 1 byte
- csz: 1 byte = 0

#### Endereço

Enviado em uma mensagem Data durante a sessão, ou em uma mensagem Peer Test fora da sessão. Veja a seção Processo de Teste de Peer abaixo.

Para a mensagem 2, deve ser precedida por um bloco RouterInfo, ou bloco de mensagem I2NP DatabaseStore (ou fragmento), contendo as informações do router de Alice, seja no mesmo payload (se houver espaço), ou em uma mensagem anterior.

```
+----+----+----+----+----+----+----+----+
|  9 |  size   |flag|                   |
+----+----+----+----+                   +
|                                       |
+                                       +
|         Alice Router Hash             |
+             32 bytes                  +
|                                       |
+                   +----+----+----+----+
|                   |      nonce        |
+----+----+----+----+----+----+----+----+
|     relay tag     |     timestamp     |
+----+----+----+----+----+----+----+----+
| ver| asz|AlicePort|  Alice IP address |
+----+----+----+----+----+----+----+----+
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 9
size :: 2 bytes, big endian, size of data to follow
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's 32-byte router hash,

The data below here is covered
by the signature, as received from Alice in the Relay Request,
and Bob forwards it unmodified.

nonce :: 4 bytes, as received from Alice
relay tag :: 4 bytes, the itag from Charlie's RI
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
ver ::  1 byte SSU version to be used for the introduction:
       1: SSU 1
       2: SSU 2
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice.
```
Para a mensagem 4, se o relay for aceito (código de motivo 0), deve ser precedido por um bloco RouterInfo, ou bloco de mensagem I2NP DatabaseStore (ou fragmento), contendo as informações do Router do Charlie, seja no mesmo payload (se houver espaço), ou em uma mensagem anterior.

- Para IPv4, o endereço IP da Alice é sempre 4 bytes, porque Alice está tentando se conectar ao Charlie via IPv4. IPv6 é suportado, e o endereço IP da Alice pode ser 16 bytes.
- Para IPv4, esta mensagem deve ser enviada através de uma conexão IPv4 estabelecida, pois essa é a única forma que Bob conhece o endereço IPv4 do Charlie para retornar à Alice na [RelayResponse](#relayresponse). IPv6 é suportado, e esta mensagem pode ser enviada através de uma conexão IPv6 estabelecida.
- Qualquer endereço SSU publicado com introdutores deve conter "4" ou "6" na opção "caps".

Notas:

Alice envia a solicitação para Bob usando uma sessão existente sobre o transporte (IPv4 ou IPv6) que ela deseja testar. Quando Bob recebe uma solicitação de Alice via IPv4, Bob deve selecionar um Charlie que anuncia um endereço IPv4. Quando Bob recebe uma solicitação de Alice via IPv6, Bob deve selecionar um Charlie que anuncia um endereço IPv6. A comunicação real entre Bob-Charlie pode ser via IPv4 ou IPv6 (ou seja, independente do tipo de endereço de Alice).

- prólogo: 16 bytes "RelayRequestData", não terminado em null (não incluído na mensagem)
- bhash: hash do router de 32 bytes do Bob (não incluído na mensagem)
- chash: hash do router de 32 bytes do Charlie (não incluído na mensagem)
- nonce: nonce de 4 bytes
- relay tag: relay tag de 4 bytes
- timestamp: timestamp de 4 bytes (segundos)
- ver: versão SSU de 1 byte
- asz: tamanho do endpoint (porta + IP) de 1 byte (6 ou 18)
- AlicePort: número da porta da Alice de 2 bytes
- Alice IP: endereço IP da Alice de (asz - 2) bytes

#### Solicitação de Tag de Relay

Assinaturas:

Alice assina a solicitação e a inclui na mensagem 1; Bob a encaminha na mensagem 2 para Charlie. Charlie assina a resposta e a inclui na mensagem 3; Bob a encaminha na mensagem 4 para Alice. Algoritmo de assinatura: Assinar ou verificar os seguintes dados com a chave de assinatura de Alice ou Charlie:

TODO apenas se rotacionarmos as chaves

```
+----+----+----+----+----+----+----+----+
| 10 |  size   | msg|code|flag|         |
+----+----+----+----+----+----+         +
| Alice router hash (message 2 only)    |
+             or                        +
| Charlie router hash (message 4 only)  |
+ or all zeros if rejected by Bob       +
| Not present in messages 1,3,5,6,7     |
+                             +----+----+
|                             | ver|
+----+----+----+----+----+----+----+----+
   nonce       |     timestamp     | asz|
+----+----+----+----+----+----+----+----+
|AlicePort|  Alice IP address |         |
+----+----+----+----+----+----+         +
|              signature                |
+            length varies              +
|         64 bytes for Ed25519          |
~                                       ~
|                 . . .                 |
+----+----+----+----+----+----+----+----+

blk :: 10
size :: 2 bytes, big endian, size of data to follow
msg :: 1 byte message number 1-7
code :: 1 byte status code:
       0: accept
       1: rejected by Bob, reason unspecified
       2: rejected by Bob, no Charlie available
       3: rejected by Bob, limit exceeded
       4: rejected by Bob, signature failure
       5: rejected by Bob, address unsupported
       6-63: other rejected by Bob codes TBD
       64: rejected by Charlie, reason unspecified
       65: rejected by Charlie, unsupported address
       66: rejected by Charlie, limit exceeded
       67: rejected by Charlie, signature failure
       68: rejected by Charlie, Alice is already connected
       69: rejected by Charlie, Alice is banned
       70: rejected by Charlie, Alice is unknown
       70-127: other rejected by Charlie codes TBD
       128: reject, source and reason unspecified
       129-255: other reject codes TBD
       reject codes only allowed in messages 3 and 4
flag :: 1 byte flags, Unused, set to 0 for future compatibility
hash :: Alice's or Charlie's 32-byte router hash,
        only present in messages 2 and 4.
        All zeros (fake hash) in message 4 if rejected by Bob.

For messages 1-4, the data below here is covered
by the signature, if present, and Bob forwards it unmodified.

ver :: 1 byte SSU version:
       1: SSU 1 (not supported)
       2: SSU 2 (required)
nonce :: 4 byte test nonce, big endian
timestamp :: Unix timestamp, unsigned seconds.
             Wraps around in 2106
asz :: 1 byte endpoint (port + IP) size (6 or 18)
AlicePort :: 2 byte Alice's port number, big endian
Alice IP :: (asz - 2) byte representation of Alice's IP address,
            network byte order
signature :: length varies, 64 bytes for Ed25519.
             Signature of prologue, Bob's hash,
             and signed data above, as signed by
             Alice or Charlie.
             Only present for messages 1-4.
             Optional in message 5-7.
```
4 bytes de ack through, seguidos por uma contagem de ack e zero ou mais intervalos nack/ack.

- Ao contrário do SSU 1, a mensagem 1 deve incluir o endereço IP e porta da Alice.

- O teste de endereços IPv6 é suportado, e a comunicação Alice-Bob e Alice-Charlie pode ser via IPv6, se Bob e Charlie indicarem suporte com uma capacidade 'B' em seu endereço IPv6 publicado. Veja a Proposta 126 para detalhes.

Este design é adaptado e simplificado do QUIC. Os objetivos do design são os seguintes:

- As mensagens 1-4 devem estar contidas numa mensagem Data numa sessão existente.

- Bob deve enviar o RI de Alice para Charlie antes de enviar a mensagem 2.

- Bob deve enviar o RI do Charlie para Alice antes de enviar a mensagem 4, se aceito (código de razão 0).

- As mensagens 5-7 devem estar contidas numa mensagem Peer Test fora de sessão.

- As mensagens 5 e 7 podem conter os mesmos dados assinados enviados nas mensagens 3 e 4, ou podem ser regeneradas com um novo timestamp. A assinatura é opcional.

- A Mensagem 6 pode conter os mesmos dados assinados enviados nas mensagens 1 e 2, ou pode ser regenerada com um novo timestamp. A assinatura é opcional.

A codificação especificada abaixo alcança esses objetivos de design, enviando o número do bit mais alto que está definido como 1, juntamente com bits consecutivos adicionais menores que esse que também estão definidos como 1. Depois disso, se houver espaço, uma ou mais "faixas" especificando o número de bits consecutivos 0 e bits consecutivos 1 menores que esse. Consulte QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) seção 13.2.3 para mais informações.

Exemplos:

- prólogo: 16 bytes "PeerTestValidate", não terminado em null (não incluído na mensagem)
- bhash: hash do router de Bob de 32 bytes (não incluído na mensagem)
- ahash: hash do router de Alice de 32 bytes (Usado apenas na assinatura para mensagens 3 e 4; não incluído na mensagem 3 ou 4)
- ver: 1 byte da versão SSU
- nonce: 4 bytes do nonce de teste
- timestamp: 4 bytes do timestamp (segundos)
- asz: 1 byte do tamanho do endpoint (porta + IP) (6 ou 18)
- AlicePort: 2 bytes do número da porta de Alice
- Alice IP: (asz - 2) bytes do endereço IP de Alice

#### Tag de Relay

Queremos fazer ACK apenas do pacote 10:

```
+----+----+----+----+----+----+----+----+
| 11 |  size   |      TBD               |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 11
size :: 2 bytes, big endian, size of data to follow
```
#### Novo Token

Queremos fazer ACK apenas dos pacotes 8-10:

Queremos fazer ACK de 10 9 8 6 5 2 1 0, e NACK de 7 4 3. A codificação do Bloco ACK é:

- Queremos codificar eficientemente um "bitfield", que é uma sequência de bits representando pacotes confirmados.
- O bitfield é principalmente composto por 1's. Tanto os 1's quanto os 0's geralmente vêm em "grupos" sequenciais.
- A quantidade de espaço no pacote disponível para confirmações varia.
- O bit mais importante é o de número mais alto. Os de números menores são menos importantes. Abaixo de uma certa distância do bit mais alto, os bits mais antigos serão "esquecidos" e nunca mais enviados novamente.

Notas:

```
+----+----+----+----+----+----+----+----+
| 12 |  size   |    Ack Through    |acnt|
+----+----+----+----+----+----+----+----+
|  range  |  range  |     .   .   .     |
+----+----+----+----+                   +
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 12
size :: 2 bytes, big endian, size of data to follow,
        5 minimum
ack through :: highest packet number acked
acnt :: number of acks lower than ack through also acked,
        0-255
range :: If present,
         1 byte nack count followed by 1 byte ack count,
         0-255 each
```
Porta de 2 bytes e endereço IP de 4 ou 16 bytes. Endereço da Alice, enviado para Alice pelo Bob, ou endereço do Bob, enviado para Bob pela Alice.

Isso pode ser enviado por Alice em uma mensagem Session Request, Session Confirmed, ou Data. Não suportado na mensagem Session Created, pois Bob ainda não tem o RI da Alice e não sabe se Alice suporta relay. Além disso, se Bob está recebendo uma conexão de entrada, ele provavelmente não precisa de introducers (exceto talvez para o outro tipo ipv4/ipv6).

- Ack Through: 10
- acnt: 0
- nenhum intervalo está incluído

Quando enviado no Session Request, Bob pode responder com uma Relay Tag na mensagem Session Created, ou pode escolher aguardar até receber o RouterInfo de Alice no Session Confirmed para validar a identidade de Alice antes de responder em uma mensagem Data. Se Bob não deseja fazer relay para Alice, ele não envia um bloco Relay Tag.

- Ack Through: 10
- acnt: 2
- nenhum intervalo está incluído

Isso pode ser enviado pelo Bob em uma mensagem Session Confirmed ou Data, em resposta a um Relay Tag Request da Alice.

- Ack Through: 10
- acnt: 2 (ack 9 8)
- range: 1 2 (nack 7, ack 6 5)
- range: 2 3 (nack 4 3, ack 2 1 0)

Quando o Relay Tag Request é enviado na Session Request, Bob pode responder com um Relay Tag na mensagem Session Created, ou pode escolher aguardar até receber o RouterInfo de Alice na Session Confirmed para validar a identidade de Alice antes de responder numa mensagem Data. Se Bob não desejar fazer relay para Alice, ele não envia um bloco Relay Tag.

- Os intervalos podem não estar presentes. O número máximo de intervalos não é especificado, podendo ser tantos quantos couberem no pacote.
- Range nack pode ser zero se confirmando mais de 255 pacotes consecutivos.
- Range ack pode ser zero se rejeitando mais de 255 pacotes consecutivos.
- Range nack e ack não podem ser ambos zero.
- Após o último intervalo, os pacotes não são nem confirmados nem rejeitados. O comprimento do bloco ack e como acks/nacks antigos são tratados fica a cargo do remetente do bloco ack. Veja as seções de ack abaixo para discussão.
- O ack through deve ser o número mais alto de pacote recebido, e quaisquer pacotes mais altos não foram recebidos. No entanto, em situações limitadas, pode ser menor, como confirmar um único pacote que "preenche uma lacuna", ou uma implementação simplificada que não mantém o estado de todos os pacotes recebidos. Acima do mais alto recebido, os pacotes não são nem confirmados nem rejeitados, mas após vários blocos ack, pode ser apropriado entrar em modo de retransmissão rápida.
- Este formato é uma versão simplificada daquele no QUIC. É projetado para codificar eficientemente um grande número de ACKs, juntamente com rajadas de NACKs.
- Os blocos ACK são usados para confirmar pacotes da fase de dados. Devem ser incluídos apenas para pacotes da fase de dados em sessão.

#### Desafio de Caminho

Para uma conexão subsequente. Geralmente incluído nas mensagens Session Created e Session Confirmed. Também pode ser enviado novamente na mensagem Data de uma sessão de longa duração se o token anterior expirar.

```
+----+----+----+----+----+----+----+----+
| 13 | 6 or 18 |   Port  | IP Address    
+----+----+----+----+----+----+----+----+
     |
+----+

blk :: 13
size :: 2 bytes, big endian, 6 or 18
port :: 2 bytes, big endian
ip :: 4 byte IPv4 or 16 byte IPv6 address,
      big endian (network byte order)
```
#### Resposta do Caminho

Um Ping com dados arbitrários a serem retornados numa Path Response, usado como keep-alive ou para validar uma mudança de IP/Porta.

Notas:

```
+----+----+----+
| 15 |    0    |
+----+----+----+

blk :: 15
size :: 2 bytes, big endian, value = 0
```
#### Número do Primeiro Pacote

Um Pong com os dados recebidos no Path Challenge, como resposta ao Path Challenge, usado como keep-alive ou para validar uma mudança de IP/Porta.

Opcionalmente incluído no handshake em cada direção, para especificar o primeiro número de pacote que será enviado. Isso oferece mais segurança para a criptografia de cabeçalho, similar ao TCP.

```
+----+----+----+----+----+----+----+
| 16 |    4    |    relay tag      |
+----+----+----+----+----+----+----+

blk :: 16
size :: 2 bytes, big endian, value = 4
relay tag :: 4 bytes, big endian, nonzero
```
#### Congestionamento

Não totalmente especificado, atualmente não suportado.

```
+----+----+----+----+----+----+----+----+
| 17 |   12    |     expires       |
+----+----+----+----+----+----+----+----+
                token              |
+----+----+----+----+----+----+----+

blk :: 17
size :: 2 bytes, big endian, value = 12
expires :: Unix timestamp, unsigned seconds.
           Wraps around in 2106
token :: 8 bytes, big endian
```
#### Preenchimento

Este bloco é projetado para ser um método extensível para trocar informações de controle de congestionamento. O controle de congestionamento pode ser complexo e pode evoluir conforme ganhamos mais experiência com o protocolo em testes ao vivo, ou após a implementação completa.

```
+----+----+----+----+----+----+----+----+
| 18 |  size   |    Arbitrary Data      |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 18
size :: 2 bytes, big endian, size of data to follow
data :: Arbitrary data to be returned in a Path Response
        length as selected by sender
```
Isso mantém qualquer informação de congestionamento fora dos blocos I2NP, First Fragment, Followon Fragment e ACK de alto uso, onde não há espaço alocado para flags. Embora existam três bytes de flags não utilizadas no cabeçalho do pacote Data, isso também fornece espaço limitado para extensibilidade e proteção de criptografia mais fraca.

- Um tamanho mínimo de dados de 8 bytes, contendo dados aleatórios, é recomendado mas não obrigatório.
- O tamanho máximo não é especificado, mas deve estar bem abaixo de 1280, porque o PMTU durante a fase de validação do caminho é 1280.
- Tamanhos grandes de desafio não são recomendados porque podem ser um vetor para ataques de amplificação de pacotes.

#### Falsificação de Endereço de Peer

Embora seja um tanto desperdiçador usar um bloco de 4 bytes para dois bits de informação, ao colocar isso em um bloco separado, podemos facilmente estendê-lo com dados adicionais como tamanhos de janela atuais, RTT medido, ou outras flags. A experiência mostrou que apenas bits de flag muitas vezes é insuficiente e inadequado para implementação de esquemas avançados de controle de congestionamento. Tentar adicionar suporte para qualquer recurso possível de controle de congestionamento no, por exemplo, bloco ACK, desperdiçaria espaço e adicionaria complexidade à análise desse bloco.

```
+----+----+----+----+----+----+----+----+
| 19 |  size   |                        |
+----+----+----+                        +
|    Data received in Path Challenge    |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 19
size :: 2 bytes, big endian, size of data to follow
data :: As received in a Path Challenge
```
#### Falsificação de Endereço no Caminho

As implementações não devem assumir que o outro router suporta qualquer bit de flag ou funcionalidade específica incluída aqui, a menos que a implementação seja exigida por uma versão futura desta especificação.

Este bloco provavelmente deveria ser o último bloco sem preenchimento no payload.

```
+----+----+----+----+----+----+----+
| 20 |  size   |  First pkt number |
+----+----+----+----+----+----+----+

blk :: 20
size :: 4
pkt num :: The first packet number to be sent in the data phase
```
#### Encaminhamento de Pacotes Fora do Caminho

Isso é para preenchimento dentro de payloads AEAD. O preenchimento para todas as mensagens está dentro de payloads AEAD.

O padding deve aderir aproximadamente aos parâmetros negociados. Bob enviou seus parâmetros tx/rx mínimo/máximo solicitados no Session Created. Alice enviou seus parâmetros tx/rx mínimo/máximo solicitados no Session Confirmed. Opções atualizadas podem ser enviadas durante a fase de dados. Veja as informações do bloco de opções acima.

Se presente, este deve ser o último bloco no payload.

Notas:

SSU2 é projetado para minimizar o impacto de mensagens replicadas por um atacante.

```
+----+----+----+----+
| 21 |  size   |flag|
+----+----+----+----+

blk :: 21
size :: 1 (or more if extended)
flag :: 1 byte flags
       bit order: 76543210 (bit 7 is MSB)
       bit 0: 1 to request immediate ack
       bit 1: 1 for explicit congestion notification (ECN)
       bits 7-2: Unused, set to 0 for future compatibility
```
#### Implicações de Privacidade

As mensagens Token Request, Retry, Session Request, Session Created, Hole Punch e Peer Test fora de sessão devem conter blocos DateTime.

Tanto Alice quanto Bob validam que o tempo para essas mensagens está dentro de uma diferença válida (recomendado +/- 2 minutos). Para "resistência a sondagem", Bob não deve responder a mensagens Token Request ou Session Request se a diferença for inválida, pois essas mensagens podem ser um ataque de repetição ou sondagem.

Bob pode escolher rejeitar mensagens duplicadas de Token Request e Retry, mesmo se o skew for válido, através de um filtro Bloom ou outro mecanismo. No entanto, o tamanho e o custo de CPU para responder a essas mensagens é baixo. Na pior das hipóteses, uma mensagem Token Request reproduzida pode invalidar um token enviado anteriormente.

```
+----+----+----+----+----+----+----+----+
|254 |  size   |      padding           |
+----+----+----+                        +
|                                       |
~               .   .   .               ~
|                                       |
+----+----+----+----+----+----+----+----+

blk :: 254
size :: 2 bytes, big endian, size of padding to follow
padding :: random data
```
O sistema de tokens minimiza drasticamente o impacto de mensagens Session Request reproduzidas. Como os tokens só podem ser usados uma vez, uma mensagem Session Request reproduzida nunca terá um token válido. Bob pode escolher rejeitar mensagens Session Request duplicadas, mesmo se o desvio for válido, através de um filtro Bloom ou outro mecanismo. No entanto, o tamanho e o custo de CPU para responder com uma mensagem Retry é baixo. Na pior das hipóteses, enviar uma mensagem Retry pode invalidar um token enviado anteriormente.

- Tamanho = 0 é permitido.
- Estratégias de padding TBD.
- Padding mínimo TBD.
- Payloads apenas com padding são permitidos.
- Padrões de padding TBD.
- Veja o bloco de opções para negociação de parâmetros de padding
- Veja o bloco de opções para parâmetros de padding mín/máx
- Não exceda o MTU. Se mais padding for necessário, envie múltiplas mensagens.
- A resposta do router sobre violação de padding negociado depende da implementação.
- O comprimento do padding deve ser decidido por mensagem e estimativas da distribuição de comprimento, ou atrasos aleatórios devem ser adicionados. Essas contramedidas devem ser incluídas para resistir a DPI, pois os tamanhos das mensagens revelariam que tráfego I2P está sendo transportado pelo protocolo de transporte. O esquema exato de padding é uma área de trabalho futuro, o Apêndice A do [NTCP2](/docs/specs/ntcp2) fornece mais informações sobre o tópico.

## Prevenção de Replay

Mensagens duplicadas de Session Created e Session Confirmed não serão validadas porque o estado do handshake Noise não estará no estado correto para descriptografá-las. Na pior das hipóteses, um peer pode retransmitir um Session Confirmed em resposta a um aparente Session Created duplicado.

Mensagens de Hole Punch e Peer Test reproduzidas devem ter pouco ou nenhum impacto.

Os routers devem usar o número do pacote de mensagem de dados para detectar e descartar mensagens da fase de dados duplicadas. Cada número de pacote deve ser usado apenas uma vez. Mensagens repetidas devem ser ignoradas.

Se nenhum Session Created ou Retry for recebido pela Alice:

Manter os mesmos IDs de origem e conexão, chave efêmera e número de pacote 0. Ou, apenas reter e retransmitir o mesmo pacote criptografado. O número do pacote não deve ser incrementado, pois isso alteraria o valor de hash encadeado usado para criptografar a mensagem Session Created.

Intervalos de retransmissão recomendados: 1,25, 2,5 e 5 segundos (1,25, 3,75 e 8,75 segundos após o primeiro envio). Timeout recomendado: 15 segundos no total

Se nenhuma Session Confirmed for recebida por Bob:

Mantenha os mesmos IDs de origem e conexão, chave efêmera e número de pacote 0. Ou, simplesmente retenha o pacote criptografado. O número do pacote não deve ser incrementado, pois isso alteraria o valor do hash encadeado usado para criptografar a mensagem Session Confirmed.

## Retransmissão de Handshake

### Sessão Criada

Intervalos de retransmissão recomendados: 1, 2 e 4 segundos (1, 3 e 7 segundos após o primeiro envio). Timeout recomendado: 12 segundos no total

No SSU 1, Alice não muda para a fase de dados até que o primeiro pacote de dados seja recebido de Bob. Isso faz do SSU 1 uma configuração de duas viagens de ida e volta.

Para SSU 2, intervalos de retransmissão de Session Confirmed recomendados: 1,25, 2,5 e 5 segundos (1,25, 3,75 e 8,75 segundos após o primeiro envio).

### Sessão Confirmada

Existem várias alternativas. Todas são 1 RTT:

1) Alice assume que Session Confirmed foi recebido, envia mensagens de dados imediatamente, nunca retransmite Session Confirmed. Pacotes de dados recebidos fora de ordem (antes de Session Confirmed) serão indecifráveis, mas serão retransmitidos. Se Session Confirmed for perdido, todas as mensagens de dados enviadas serão descartadas. 2) Como em 1), envia mensagens de dados imediatamente, mas também retransmite Session Confirmed até que uma mensagem de dados seja recebida. 3) Poderíamos usar IK em vez de XK, pois tem apenas duas mensagens no handshake, mas usa um DH extra (4 em vez de 3).

A implementação recomendada é a opção 2). Alice deve reter as informações necessárias para retransmitir a mensagem Session Confirmed. Alice também deve retransmitir todas as mensagens Data após a mensagem Session Confirmed ser retransmitida.

### Solicitação de Token

Ao retransmitir Session Confirmed, mantenha os mesmos IDs de origem e conexão, chave efêmera e número de pacote 1. Ou, apenas retenha o pacote criptografado. O número do pacote não deve ser incrementado, porque isso mudaria o valor do hash encadeado que é uma entrada para a função split().

Bob pode reter (enfileirar) as mensagens de dados recebidas antes da mensagem Session Confirmed. Nem as chaves de proteção do cabeçalho nem as chaves de descriptografia estão disponíveis antes da mensagem Session Confirmed ser recebida, então Bob não sabe que são mensagens de dados, mas isso pode ser presumido. Após a mensagem Session Confirmed ser recebida, Bob consegue descriptografar e processar as mensagens de dados enfileiradas. Se isso for muito complexo, Bob pode simplesmente descartar as mensagens de dados não descriptografáveis, pois Alice irá retransmiti-las.

Nota: Se os pacotes de sessão confirmada forem perdidos, Bob retransmitirá a sessão criada. O cabeçalho da sessão criada não será decifrável com a chave de introdução de Alice, pois está configurado com a chave de introdução de Bob (a menos que a decodificação de fallback seja realizada com a chave de introdução de Bob). Bob pode retransmitir imediatamente os pacotes de sessão confirmada se não foram previamente confirmados, e um pacote não decifrável é recebido.

Se nenhum Retry for recebido por Alice:

Mantenha os mesmos IDs de origem e conexão. Uma implementação pode gerar um novo número de pacote aleatório e criptografar um novo pacote; ou pode reutilizar o mesmo número de pacote ou apenas manter e retransmitir o mesmo pacote criptografado. O número do pacote não deve ser incrementado, pois isso alteraria o valor de hash encadeado usado para criptografar a mensagem Session Created.

Intervalos de retransmissão recomendados: 3 e 6 segundos (3 e 9 segundos após o primeiro envio). Timeout recomendado: 15 segundos no total

Se nenhum Session Confirmed for recebido por Bob:

Uma mensagem Retry não é retransmitida em caso de timeout, para reduzir os impactos de endereços de origem falsificados.

### Tentar Novamente

No entanto, uma mensagem Retry pode ser retransmitida em resposta a uma mensagem Session Request repetida sendo recebida com o token original (inválido), ou em resposta a uma mensagem Token Request repetida. Em qualquer dos casos, isso indica que a mensagem Retry foi perdida.

Se uma segunda mensagem Session Request for recebida com um token diferente mas ainda inválido, descarte a sessão pendente e não responda.

Se reenviar a mensagem Retry: Manter os mesmos IDs de origem e conexão e token. Uma implementação pode gerar um novo número de pacote aleatório e criptografar um novo pacote; Ou pode reutilizar o mesmo número de pacote ou apenas reter e retransmitir o mesmo pacote criptografado.

### Timeout Total

O timeout total recomendado para o handshake é de 20 segundos.

Duplicatas das três mensagens de handshake Noise Session Request, Session Created e Session Confirmed devem ser detectadas antes do MixHash() do cabeçalho. Embora o processamento AEAD do Noise presumivelmente falhará após isso, o hash do handshake já estaria corrompido.

Se qualquer uma das três mensagens estiver corrompida e falhar no AEAD, o handshake não poderá ser recuperado subsequentemente mesmo com retransmissão, porque MixHash() já foi chamado na mensagem corrompida.

O Token no cabeçalho Session Request é usado para mitigação de DoS, para prevenir falsificação de endereço de origem e como resistência a ataques de replay.

Se Bob não aceitar o token na mensagem Session Request, Bob NÃO descriptografa a mensagem, pois isso requer uma operação DH custosa. Bob simplesmente envia uma mensagem Retry com um novo token.

### Duplicatas e Tratamento de Erros

Se uma mensagem de Solicitação de Sessão subsequente for recebida com esse token, Bob procede para descriptografar essa mensagem e continuar com o handshake.

### Números de Pacote

O token deve ser um valor de 8 bytes gerado aleatoriamente, se o gerador do token armazenar os valores e o IP e porta associados (em memória ou persistentemente). O gerador não pode gerar um valor opaco, por exemplo, usando o SipHash (com uma semente secreta K0, K1) do IP, porta e hora ou dia atual, para criar tokens que não precisam ser salvos em memória, porque este método torna difícil rejeitar tokens reutilizados e ataques de replay. No entanto, é um tópico para estudo futuro se podemos migrar para tal esquema, como o [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) faz, usando um HMAC de 16 bytes de um segredo do servidor e endereço IP.

Os tokens só podem ser usados uma vez. Um token enviado de Bob para Alice numa mensagem Retry deve ser usado imediatamente e expira em alguns segundos. Um token enviado num bloco New Token numa sessão estabelecida pode ser usado numa conexão subsequente, e expira no tempo especificado nesse bloco. A expiração é especificada pelo remetente; valores recomendados são vários minutos no mínimo, uma ou mais horas no máximo, dependendo da sobrecarga máxima desejada dos tokens armazenados.

## Tokens

Se o IP ou porta de um router mudar, ele deve excluir todos os tokens salvos (tanto de entrada quanto de saída) para o IP ou porta antigos, pois eles não são mais válidos. Os tokens podem opcionalmente ser persistidos através de reinicializações do router, dependendo da implementação. A aceitação de um token não expirado não é garantida; se Bob tiver esquecido ou excluído seus tokens salvos, ele enviará um Retry para Alice. Um router pode escolher limitar o armazenamento de tokens e remover os tokens armazenados mais antigos mesmo que não tenham expirado.

Novos blocos Token podem ser enviados de Alice para Bob ou de Bob para Alice. Eles normalmente seriam enviados pelo menos uma vez, durante ou logo após o estabelecimento da sessão. Devido às verificações de validação do RouterInfo na mensagem Session Confirmed, Bob não deve enviar um bloco New Token na mensagem Session Created, ele pode ser enviado com o ACK 0 e Router Info após a Session Confirmed ser recebida e validada.

Como os tempos de vida das sessões são frequentemente maiores que a expiração do token, o token deve ser reenviado antes ou após a expiração com um novo tempo de expiração, ou um novo token deve ser enviado. Os routers devem assumir que apenas o último token recebido é válido; não há exigência de armazenar múltiplos tokens de entrada ou saída para o mesmo IP/porta.

Um token está vinculado à combinação de IP/porta de origem e IP/porta de destino. Um token recebido no IPv4 não pode ser usado para IPv6 ou vice-versa.

Se qualquer peer migrar para um novo IP ou porta durante a sessão (veja a seção Migração de Conexão), quaisquer tokens previamente trocados são invalidados, e novos tokens devem ser trocados.

As implementações podem, mas não são obrigadas a, salvar tokens no disco e recarregá-los na reinicialização. Se persistidos, a implementação deve garantir que o IP e a porta não tenham mudado desde o desligamento antes de recarregá-los.

Diferenças do SSU 1

Nota: Assim como no SSU 1, o fragmento inicial não contém informações sobre o número total de fragmentos ou o comprimento total. Os fragmentos subsequentes não contêm informações sobre seu deslocamento. Isso fornece ao remetente a flexibilidade de fragmentar "em tempo real" com base no espaço disponível no pacote. (O Java I2P não faz isso; ele "pré-fragmenta" antes do primeiro fragmento ser enviado) No entanto, isso sobrecarrega o receptor ao armazenar fragmentos recebidos fora de ordem e atrasar a remontagem até que todos os fragmentos sejam recebidos.

Assim como no SSU 1, qualquer retransmissão de fragmentos deve preservar o comprimento (e o deslocamento implícito) da transmissão anterior do fragmento.

SSU 2 separa os três casos (mensagem completa, fragmento inicial e fragmento de continuação) em três tipos de bloco diferentes, para melhorar a eficiência de processamento.

Este protocolo NÃO previne completamente a entrega duplicada de mensagens I2NP. Duplicatas na camada IP ou ataques de replay serão detectados na camada SSU2, porque cada número de pacote só pode ser usado uma vez.

## Fragmentação de Mensagens I2NP

Quando mensagens ou fragmentos I2NP são retransmitidos em novos pacotes, no entanto, isso não é detectável na camada SSU2. O router deve aplicar a expiração I2NP (tanto muito antiga quanto muito distante no futuro) e usar um filtro Bloom ou outro mecanismo baseado no ID da mensagem I2NP.

Mecanismos adicionais podem ser utilizados pelo router, ou na implementação SSU2, para detectar duplicatas. Por exemplo, SSU2 poderia manter um cache de IDs de mensagens recebidas recentemente. Isto é dependente da implementação.

Esta especificação define o protocolo para numeração de pacotes e blocos ACK. Isso fornece informações em tempo real suficientes para que um transmissor implemente um algoritmo de controle de congestionamento eficiente e responsivo, permitindo flexibilidade e inovação nessa implementação. Esta seção discute objetivos de implementação e fornece sugestões. Orientações gerais podem ser encontradas na [RFC-9002](https://tools.ietf.org/html/rfc9002). Veja também [RFC-6298](https://tools.ietf.org/html/rfc6298) para orientações sobre temporizadores de retransmissão.

Pacotes de dados apenas com ACK não devem contar para bytes ou pacotes em trânsito e não são controlados por congestionamento. Ao contrário do TCP, o SSU2 pode detectar a perda desses pacotes e essa informação pode ser usada para ajustar o estado de congestionamento. No entanto, este documento não especifica um mecanismo para fazê-lo.

## Duplicação de Mensagens I2NP

Pacotes contendo alguns outros blocos não-dados também podem ser excluídos do controle de congestionamento se desejado, dependente da implementação. Por exemplo:

É recomendado que o controle de congestionamento seja baseado na contagem de bytes, não na contagem de pacotes, seguindo as orientações nos RFCs do TCP e QUIC [RFC-9002](https://tools.ietf.org/html/rfc9002). Um limite adicional de contagem de pacotes também pode ser útil para prevenir overflow de buffer no kernel ou em middleboxes, dependente da implementação, embora isso possa adicionar complexidade significativa. Se a saída de pacotes por sessão e/ou total for limitada por largura de banda e/ou ritmo controlado, isso pode mitigar a necessidade de limitação por contagem de pacotes.

No SSU 1, ACKs e NACKs continham números de mensagens I2NP e bitmasks de fragmentos. Os transmissores rastreavam o status de ACK das mensagens de saída (e seus fragmentos) e retransmitiam fragmentos conforme necessário.

## Controle de Congestionamento

No SSU 2, ACKs e NACKs contêm números de pacote. Os transmissores devem manter uma estrutura de dados com um mapeamento dos números de pacote para seus conteúdos. Quando um pacote recebe ACK ou NACK, o transmissor deve determinar quais mensagens I2NP e fragmentos estavam naquele pacote, para decidir o que retransmitir.

Bob envia um ACK do pacote 0, que confirma a mensagem Session Confirmed e permite que Alice prossiga para a fase de dados, e descarte a grande mensagem Session Confirmed que estava sendo salva para possível retransmissão. Isto substitui a DeliveryStatusMessage enviada por Bob no SSU 1.

Bob deve enviar um ACK o mais rápido possível após receber a mensagem Session Confirmed. Um pequeno atraso (não mais que 50 ms) é aceitável, uma vez que pelo menos uma mensagem Data deve chegar quase imediatamente após a mensagem Session Confirmed, para que o ACK possa confirmar tanto a Session Confirmed quanto a mensagem Data. Isso impedirá que Bob tenha que retransmitir a mensagem Session Confirmed.

- Teste de Par
- Solicitação/introdução/resposta de retransmissão
- Desafio/resposta de caminho

Definição: Pacotes que provocam ACK: Pacotes que contêm blocos que provocam ack geram um ACK do receptor dentro do atraso máximo de reconhecimento e são chamados de pacotes que provocam ack.

### ACK de Sessão Confirmada

Os routers reconhecem todos os pacotes que recebem e processam. No entanto, apenas pacotes que exigem confirmação fazem com que um bloco ACK seja enviado dentro do atraso máximo de confirmação. Pacotes que não exigem confirmação são apenas reconhecidos quando um bloco ACK é enviado por outras razões.

Ao enviar um pacote por qualquer motivo, um endpoint deve tentar incluir um bloco ACK se um não foi enviado recentemente. Fazer isso ajuda na detecção oportuna de perda no peer.

### Gerando ACKs

Em geral, feedback frequente de um receptor melhora a resposta à perda e ao congestionamento, mas isso deve ser equilibrado contra a carga excessiva gerada por um receptor que envia um bloco ACK em resposta a cada pacote que solicita confirmação. As orientações oferecidas abaixo buscam encontrar esse equilíbrio.

Pacotes de dados em sessão contendo qualquer bloco EXCETO os seguintes são elicitadores de ack:

### ACKs de Handshake

Pacotes fora de sessão, incluindo mensagens de handshake e mensagens de teste de pares 5-7, têm seus próprios mecanismos de confirmação. Veja abaixo.

Estes são casos especiais:

Blocos ACK são utilizados para confirmar pacotes da fase de dados. Eles devem ser incluídos apenas para pacotes da fase de dados dentro da sessão.

Cada pacote deve ser confirmado pelo menos uma vez, e pacotes que provocam confirmação devem ser confirmados pelo menos uma vez dentro de um atraso máximo.

Um endpoint deve reconhecer todos os pacotes de handshake que exigem confirmação imediatamente dentro de seu atraso máximo, com a seguinte exceção. Antes da confirmação do handshake, um endpoint pode não ter as chaves de criptografia do cabeçalho do pacote para descriptografar os pacotes quando eles são recebidos. Portanto, pode armazená-los em buffer e reconhecê-los quando as chaves necessárias ficarem disponíveis.

- Bloco ACK
- Bloco de endereço
- Bloco DateTime
- Bloco de preenchimento
- Bloco de terminação
- Outros?

Como pacotes contendo apenas blocos ACK não são controlados por congestionamento, um endpoint não deve enviar mais de um desses pacotes em resposta ao recebimento de um pacote que provoca ACK.

### Enviando Blocos ACK

Um endpoint não deve enviar um pacote que não elicita ACK em resposta a um pacote que não elicita ACK, mesmo se houver lacunas de pacotes que precedem o pacote recebido. Isso evita um loop infinito de reconhecimentos, que poderia impedir que a conexão se torne inativa. Pacotes que não elicitam ACK são eventualmente reconhecidos quando o endpoint envia um bloco ACK em resposta a outros eventos.

- Token Request é implicitamente confirmado por Retry
- Session Request é implicitamente confirmado por Session Created ou Retry
- Retry é implicitamente confirmado por Session Request
- Session Created é implicitamente confirmado por Session Confirmed
- Session Confirmed deve ser confirmado imediatamente

### Frequência de ACK

Um endpoint que está apenas enviando blocos ACK não receberá confirmações de seu par, a menos que essas confirmações estejam incluídas em pacotes com blocos que provocam confirmação. Um endpoint deve enviar um bloco ACK junto com outros blocos quando houver novos pacotes que provocam confirmação para serem reconhecidos. Quando apenas pacotes que não provocam confirmação precisam ser reconhecidos, um endpoint PODE escolher não enviar um bloco ACK com blocos de saída até que um pacote que provoca confirmação tenha sido recebido.

Um endpoint que está apenas enviando pacotes não-solicitadores-de-ack pode optar por ocasionalmente adicionar um bloco solicitador-de-ack a esses pacotes para garantir que receba uma confirmação. Nesse caso, um endpoint NÃO DEVE enviar um bloco solicitador-de-ack em todos os pacotes que de outra forma seriam não-solicitadores-de-ack, para evitar um loop infinito de feedback de confirmações.

Para auxiliar a detecção de perdas no remetente, um endpoint deve gerar e enviar um bloco ACK sem demora quando recebe um pacote que solicita confirmação em qualquer um destes casos:

Espera-se que os algoritmos sejam resistentes a receptores que não seguem a orientação oferecida acima. No entanto, uma implementação deve apenas desviar desses requisitos após consideração cuidadosa das implicações de desempenho de uma mudança, tanto para conexões feitas pelo endpoint quanto para outros usuários da rede.

Um receptor determina com que frequência enviar confirmações de recebimento em resposta a pacotes que exigem confirmação. Esta determinação envolve um equilíbrio.

Os endpoints dependem de reconhecimento oportuno para detectar perdas. Os controladores de congestionamento baseados em janela dependem de reconhecimentos para gerenciar sua janela de congestionamento. Em ambos os casos, atrasar reconhecimentos pode afetar adversamente o desempenho.

Por outro lado, reduzir a frequência de pacotes que carregam apenas confirmações reduz o custo de transmissão e processamento de pacotes em ambos os pontos finais. Isso pode melhorar o throughput da conexão em links severamente assimétricos e reduzir o volume de tráfego de confirmação usando a capacidade do caminho de retorno; veja a Seção 3 de [RFC-3449](https://tools.ietf.org/html/rfc3449).

Um receptor deve enviar um bloco ACK após receber pelo menos dois pacotes que exigem confirmação. Esta recomendação é de natureza geral e consistente com as recomendações para comportamento de endpoints TCP [RFC-5681](https://tools.ietf.org/html/rfc5681). O conhecimento das condições de rede, conhecimento do controlador de congestionamento do peer, ou pesquisas e experimentações adicionais podem sugerir estratégias de confirmação alternativas com melhores características de desempenho.

- Quando o pacote recebido tem um número de pacote menor que outro pacote que solicita confirmação que foi recebido
- Quando o pacote tem um número de pacote maior que o pacote que solicita confirmação com o número mais alto que foi recebido e há pacotes perdidos entre esse pacote e este pacote.
- Quando a flag ack-immediate no cabeçalho do pacote está definida

Um receptor pode processar múltiplos pacotes disponíveis antes de determinar se deve enviar um bloco ACK em resposta. Em geral, o receptor não deve atrasar um ACK por mais de RTT / 6, ou 150 ms no máximo.

### Flag de ACK Imediato

A flag ack-immediate no cabeçalho do pacote de dados é uma solicitação para que o receptor envie um ack logo após a recepção, provavelmente dentro de alguns ms. Em geral, o receptor não deve atrasar um ACK imediato por mais de RTT / 16, ou 5 ms no máximo.

O receptor não conhece o tamanho da janela de envio do remetente e, portanto, não sabe quanto tempo deve aguardar antes de enviar um ACK. A flag de ACK imediato no cabeçalho do pacote de dados é uma forma importante de manter o throughput máximo minimizando o RTT efetivo. A flag de ACK imediato está no byte 13 do cabeçalho, bit 0, ou seja, (header[13] & 0x01). Quando definida, um ACK imediato é solicitado. Consulte a seção do cabeçalho curto acima para detalhes.

Existem várias estratégias possíveis que um remetente pode usar para determinar quando definir a flag immediate-ack:

Flags de ACK imediato só devem ser necessárias em pacotes de dados que contenham mensagens I2NP ou fragmentos de mensagem.

Quando um bloco ACK é enviado, uma ou mais faixas de pacotes confirmados são incluídas. Incluir confirmações para pacotes mais antigos reduz a chance de retransmissões espúrias causadas pela perda de blocos ACK enviados anteriormente, ao custo de blocos ACK maiores.

Os blocos ACK devem sempre reconhecer os pacotes recebidos mais recentemente, e quanto mais fora de ordem estiverem os pacotes, mais importante é enviar um bloco ACK atualizado rapidamente, para evitar que o peer declare um pacote como perdido e retransmita desnecessariamente os blocos que ele contém. Um bloco ACK deve caber dentro de um único pacote. Se não couber, então os intervalos mais antigos (aqueles com os menores números de pacote) são omitidos.

### Tamanho do Bloco ACK

Um receptor limita o número de intervalos ACK que lembra e envia em blocos ACK, tanto para limitar o tamanho dos blocos ACK quanto para evitar o esgotamento de recursos. Após receber confirmações para um bloco ACK, o receptor deve parar de rastrear esses intervalos ACK confirmados. Os remetentes podem esperar confirmações para a maioria dos pacotes, mas este protocolo não garante o recebimento de uma confirmação para cada pacote que o receptor processa.

É possível que manter muitas faixas de ACK possa fazer com que um bloco de ACK se torne muito grande. Um receptor pode descartar faixas de ACK não reconhecidas para limitar o tamanho do bloco de ACK, ao custo de retransmissões aumentadas do remetente. Isso é necessário se um bloco de ACK for muito grande para caber em um pacote. Os receptores também podem limitar ainda mais o tamanho do bloco de ACK para preservar espaço para outros blocos ou para limitar a largura de banda que os reconhecimentos consomem.

- Definido uma vez a cada N pacotes, para algum N pequeno
- Definido no último pacote de uma rajada
- Definido sempre que a janela de envio estiver quase cheia, por exemplo mais de 2/3 cheia
- Definido em todos os pacotes com fragmentos retransmitidos

Um receptor deve manter um intervalo de ACK a menos que possa garantir que não aceitará subsequentemente pacotes com números nesse intervalo. Manter um número mínimo de pacote que aumenta conforme os intervalos são descartados é uma maneira de conseguir isso com estado mínimo.

### Limitando Intervalos Rastreando Blocos ACK

Os receptores podem descartar todos os intervalos ACK, mas devem reter o maior número de pacote que foi processado com sucesso, pois isso é usado para recuperar números de pacote de pacotes subsequentes.

A seção seguinte descreve uma abordagem exemplar para determinar quais pacotes reconhecer em cada bloco ACK. Embora o objetivo deste algoritmo seja gerar um reconhecimento para cada pacote que é processado, ainda é possível que os reconhecimentos sejam perdidos.

Quando um pacote contendo um bloco ACK é enviado, o campo Ack Through nesse bloco pode ser salvo. Quando um pacote contendo um bloco ACK é confirmado, o receptor pode parar de confirmar pacotes menores ou iguais ao campo Ack Through no bloco ACK enviado.

Um receptor que envia apenas pacotes que não solicitam ACK, como blocos ACK, pode não receber um reconhecimento por um longo período de tempo. Isso pode fazer com que o receptor mantenha estado para um grande número de blocos ACK por um longo período, e os blocos ACK que ele envia podem ser desnecessariamente grandes. Nesse caso, um receptor pode enviar um PING ou outro pequeno bloco que solicite ACK ocasionalmente, como uma vez por viagem de ida e volta, para provocar um ACK do par.

Em casos sem perda de bloco ACK, este algoritmo permite um mínimo de 1 RTT de reordenação. Em casos com perda de bloco ACK e reordenação, esta abordagem não garante que cada reconhecimento seja visto pelo remetente antes de não estar mais incluído no bloco ACK. Os pacotes podem ser recebidos fora de ordem, e todos os blocos ACK subsequentes que os contêm podem ser perdidos. Neste caso, o algoritmo de recuperação de perda pode causar retransmissões espúrias, mas o remetente continuará fazendo progresso.

Os transportes I2P não garantem a entrega em ordem das mensagens I2NP. Portanto, a perda de uma mensagem Data contendo uma ou mais mensagens ou fragmentos I2NP NÃO impede que outras mensagens I2NP sejam entregues; não há bloqueio de cabeça de fila. As implementações devem continuar a enviar novas mensagens durante a fase de recuperação de perda se a janela de envio permitir.

Um remetente não deve reter o conteúdo completo de uma mensagem, para ser retransmitida de forma idêntica (exceto para mensagens de handshake, veja acima). Um remetente deve montar mensagens contendo informações atualizadas (ACKs, NACKs e dados não confirmados) toda vez que enviar uma mensagem. Um remetente deve evitar retransmitir informações de mensagens uma vez que sejam confirmadas. Isso inclui mensagens que são confirmadas após serem declaradas perdidas, o que pode acontecer na presença de reordenamento de rede.

### Congestionamento

A definir. Orientações gerais podem ser encontradas na [RFC-9002](https://tools.ietf.org/html/rfc9002).

O IP ou porta de um peer pode mudar durante o tempo de vida de uma sessão. Uma mudança de IP pode ser causada por rotação de endereço temporário IPv6, mudança periódica de IP dirigida pelo ISP, um cliente móvel fazendo transição entre IPs WiFi e celular, ou outras mudanças de rede local. Uma mudança de porta pode ser causada por um rebinding de NAT após o binding anterior ter expirado.

O IP ou porta de um peer pode parecer mudar devido a vários ataques dentro e fora do caminho, incluindo modificação ou injeção de pacotes.

### Retransmissão

A migração de conexão é o processo pelo qual um novo endpoint de origem (IP+porta) é validado, ao mesmo tempo que previne mudanças que não são validadas. Este processo é uma versão simplificada daquela definida no QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000). Este processo é definido apenas para a fase de dados de uma sessão. A migração não é permitida durante o handshake. Todos os pacotes de handshake devem ser verificados para confirmar que são do mesmo IP e porta dos pacotes enviados e recebidos anteriormente. Em outras palavras, o IP e porta de um peer devem ser constantes durante o handshake.

### Janela

(Adaptado de QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000))

### Modelo de Ameaças

Um peer pode falsificar seu endereço de origem para fazer com que um endpoint envie quantidades excessivas de dados para um host não disposto. Se o endpoint enviar significativamente mais dados do que o peer falsificador, a migração de conexão pode ser usada para amplificar o volume de dados que um atacante pode gerar em direção a uma vítima.

## Migração de Conexão

Um atacante no caminho poderia causar uma migração de conexão espúria copiando e encaminhando um pacote com um endereço falsificado de modo que chegue antes do pacote original. O pacote com o endereço falsificado será visto como proveniente de uma conexão em migração, e o pacote original será visto como duplicado e descartado. Após uma migração espúria, a validação do endereço de origem falhará porque a entidade no endereço de origem não possui as chaves criptográficas necessárias para ler ou responder ao Path Challenge que é enviado para ela, mesmo que quisesse.

Um atacante fora do caminho que pode observar pacotes pode encaminhar cópias de pacotes genuínos para endpoints. Se o pacote copiado chegar antes do pacote genuíno, isso aparecerá como um rebinding de NAT. Qualquer pacote genuíno será descartado como duplicado. Se o atacante conseguir continuar encaminhando pacotes, pode ser capaz de causar migração para um caminho via o atacante. Isso coloca o atacante no caminho, dando-lhe a capacidade de observar ou descartar todos os pacotes subsequentes.

QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) especificou a alteração de IDs de conexão ao mudar caminhos de rede. Usar um ID de conexão estável em múltiplos caminhos de rede permitiria a um observador passivo correlacionar atividade entre esses caminhos. Um endpoint que se move entre redes pode não desejar ter sua atividade correlacionada por qualquer entidade além de seu peer. No entanto, QUIC não criptografa os IDs de conexão no cabeçalho. SSU2 faz isso, então o vazamento de privacidade exigiria que o observador passivo também tivesse acesso ao netDb para obter a chave de introdução necessária para descriptografar o ID de conexão. Mesmo com a chave de introdução, este não é um ataque forte, e não alteramos IDs de conexão após migração em SSU2, pois isso seria uma complicação significativa.

### Iniciando Validação de Caminho

Durante a fase de dados, os peers devem verificar o IP de origem e a porta de cada pacote de dados recebido. Se o IP ou a porta for diferente do recebido anteriormente, E o pacote não for um número de pacote duplicado, E o pacote descriptografar com sucesso, a sessão entra na fase de validação de caminho.

#### Seleção de Introdutor

Além disso, um peer deve verificar se o novo IP e porta são válidos de acordo com as regras de validação locais (não bloqueados, portas não ilegais, etc.). Peers NÃO são obrigados a suportar migração entre IPv4 e IPv6, e podem tratar um novo IP na outra família de endereços como inválido, já que este não é um comportamento esperado e pode adicionar complexidade significativa de implementação. Ao receber um pacote de um IP/porta inválido, uma implementação pode simplesmente descartá-lo, ou pode iniciar uma validação de caminho com o IP/porta antigo.

#### Tratamento de Resposta

Ao entrar na fase de validação do caminho, siga os seguintes passos:

#### Introdutores

Enquanto estiver na fase de validação de caminho, a sessão pode continuar a processar pacotes de entrada. Seja do IP/porta antigo ou novo. A sessão também pode continuar a enviar e reconhecer pacotes de dados. No entanto, a janela de congestionamento e PMTU devem permanecer nos valores mínimos durante a fase de validação de caminho, para evitar serem usados em ataques de negação de serviço ao enviar grandes quantidades de tráfego para um endereço falsificado.

#### Ocultação de Identidade

Uma implementação pode, mas não é obrigatório, tentar validar múltiplos caminhos simultaneamente. Isso provavelmente não vale a complexidade. Ela pode, mas não é obrigatório, lembrar de um IP/porta anterior como já validado, e pular a validação de caminho se um peer retornar ao seu IP/porta anterior.

### Conteúdo da Mensagem

Se uma Path Response for recebida, contendo os dados idênticos enviados no Path Challenge, a Validação de Caminho foi bem-sucedida. O IP/porta de origem da mensagem Path Response não precisa ser o mesmo para o qual o Path Challenge foi enviado.

Se uma Path Response não for recebida antes do timer de Path Response expirar, envie outro Path Challenge e dobre o timer de Path Response.

Se uma Path Response não for recebida antes que o timer de Path Validation expire, a Path Validation falhou.

- Iniciar um temporizador de timeout de validação de caminho de vários segundos, ou várias vezes o RTO atual (TBD)
- Reduzir a janela de congestionamento ao mínimo
- Reduzir o PMTU ao mínimo (1280)
- Enviar um pacote de dados contendo um bloco Path Challenge, um bloco Address (contendo o novo IP/porta), e, tipicamente, um bloco ACK, para o novo IP e porta. Este pacote usa o mesmo connection ID e chaves de criptografia da sessão atual. Os dados do bloco Path Challenge devem conter entropia suficiente (pelo menos 8 bytes) para que não possam ser falsificados.
- Opcionalmente, também enviar um Path Challenge para o antigo IP/porta, com dados de bloco diferentes. Veja abaixo.
- Iniciar um temporizador de timeout de Path Response baseado no RTO atual (tipicamente RTT + um múltiplo de RTTdev)

As mensagens Data devem conter os seguintes blocos. A ordem não é especificada, exceto que Padding deve ser o último:

Não é recomendado incluir quaisquer outros blocos (por exemplo, I2NP) na mensagem.

É permitido incluir um bloco Path Challenge na mensagem contendo o Path Response, para iniciar uma validação na outra direção.

Os blocos Path Challenge e Path Response geram ACK. O Path Challenge será confirmado por uma mensagem Data contendo os blocos Path Response e ACK. O Path Response deve ser confirmado por uma mensagem Data contendo um bloco ACK.

A especificação QUIC não é clara sobre onde enviar pacotes de dados durante a validação de caminho - para o IP/porta antigo ou novo? Há um equilíbrio a ser encontrado entre responder rapidamente a mudanças de IP/porta e não enviar tráfego para endereços falsificados. Além disso, pacotes falsificados não devem ter impacto substancial em uma sessão existente. Mudanças apenas de porta provavelmente são causadas por nova vinculação NAT após um período de inatividade; mudanças de IP podem acontecer durante fases de tráfego intenso em uma ou ambas as direções.

### Roteamento durante a Validação de Caminho

As estratégias estão sujeitas a pesquisa e refinamento. As possibilidades incluem:

- Bloco Path Challenge ou Path Response. Path Challenge contém dados opacos, recomendado 8 bytes mínimo. Path Response contém os dados do Path Challenge.
- Bloco de endereço contendo o IP aparente do destinatário
- Bloco DateTime
- Bloco ACK
- Bloco de preenchimento

Ao receber um Path Challenge, o peer deve responder com um pacote de dados contendo um Path Response, com os dados do Path Challenge.

A Path Response deve ser enviada para o IP/porta de onde a Path Challenge foi recebida. Isso NÃO É NECESSARIAMENTE o IP/porta que foi previamente estabelecido para o peer. Isso garante que a validação de caminho por um peer só seja bem-sucedida se o caminho for funcional em ambas as direções. Consulte a seção Validação após Mudança Local abaixo.

A menos que o IP/porta seja diferente do IP/porta conhecido anteriormente para o peer, trate um Path Challenge como um ping simples e responda incondicionalmente com um Path Response. O receptor não mantém ou altera nenhum estado baseado em um Path Challenge recebido. Se o IP/porta for diferente, um peer deve verificar que o novo IP e porta são válidos de acordo com as regras de validação locais (não bloqueados, portas não ilegais, etc.). Peers NÃO são obrigatórios a suportar respostas entre famílias de endereços cruzadas entre IPv4 e IPv6, e podem tratar um novo IP na outra família de endereços como inválido, já que este não é um comportamento esperado.

### Respondendo ao Desafio de Caminho

A menos que seja restringida pelo controle de congestionamento, a Path Response deve ser enviada imediatamente. As implementações devem tomar medidas para limitar a taxa de Path Responses ou a largura de banda utilizada, se necessário.

Um bloco Path Challenge geralmente é acompanhado por um bloco Address na mesma mensagem. Se o bloco de endereço contiver um novo IP/porta, um peer pode validar esse IP/porta e iniciar o teste de peer desse novo IP/porta, com o peer da sessão ou qualquer outro peer. Se o peer acha que está atrás de firewall, e apenas a porta mudou, essa mudança provavelmente é devido ao rebinding de NAT, e testes de peer adicionais provavelmente não são necessários.

- Não enviar pacotes de dados para o novo IP/porta até ser validado
- Continuar enviando pacotes de dados para o IP/porta antigo até que o novo IP/porta seja validado
- Simultaneamente revalidar o IP/porta antigo
- Não enviar nenhum dado até que o IP/porta antigo ou novo seja validado
- Estratégias diferentes para mudança apenas de porta do que para mudança de IP
- Estratégias diferentes para uma mudança de IPv6 no mesmo /32, provavelmente causada por rotação de endereço temporário

### Validação de Caminho Bem-sucedida

Na validação bem-sucedida do caminho, a conexão é totalmente migrada para o novo IP/porta. Em caso de sucesso:

Durante a fase de validação de caminho, quaisquer pacotes válidos e não duplicados que sejam recebidos do IP/porta antigo e sejam descriptografados com sucesso farão com que a Validação de Caminho seja cancelada. É importante que uma validação de caminho cancelada, causada por um pacote falsificado, não cause o encerramento ou interrupção significativa de uma sessão válida.

Na validação de caminho cancelada:

É importante que uma validação de caminho falhada, causada por um pacote falsificado, não cause o término ou interrupção significativa de uma sessão válida.

Em caso de falha na validação do caminho:

### Cancelando Validação de Caminho

O processo acima é definido para peers que recebem um pacote de um IP/porta alterado. No entanto, também pode ser iniciado na direção oposta, por um peer que detecta que seu IP ou porta foram alterados. Um peer pode ser capaz de detectar que seu IP local mudou; no entanto, é muito menos provável detectar que sua porta mudou devido a um rebinding de NAT. Portanto, isso é opcional.

- Sair da fase de validação de caminho
- Todos os pacotes são enviados para o novo IP e porta.
- As restrições na janela de congestionamento e PMTU são removidas, e elas têm permissão para aumentar. Não as restaure simplesmente aos valores antigos, pois o novo caminho pode ter características diferentes.
- Se o IP mudou, defina RTT calculado e RTO para valores iniciais. Como mudanças apenas de porta são comumente resultado de revinculação NAT ou outras atividades de middlebox, o peer pode em vez disso manter seu estado de controle de congestionamento e estimativa de round-trip nesses casos em vez de reverter aos valores iniciais.
- Excluir (invalidar) quaisquer tokens enviados ou recebidos para o IP/porta antigo (opcional)
- Enviar um novo bloco de token para o novo IP/porta (opcional)

### Falha na Validação do Caminho

Ao receber um path challenge de um peer cujo IP ou porta mudou, o outro peer deve iniciar um path challenge na direção oposta.

Os blocos Path Challenge e Path Response podem ser usados a qualquer momento como pacotes Ping/Pong. A recepção de um bloco Path Challenge não altera qualquer estado no receptor, a menos que seja recebido de um IP/porta diferente.

- Sair da fase de validação de caminho
- Todos os pacotes são enviados para o IP e porta antigos.
- As restrições na janela de congestionamento e PMTU são removidas, e eles são permitidos aumentar, ou, opcionalmente, restaurar os valores anteriores
- Retransmitir quaisquer pacotes de dados que foram previamente enviados para o novo IP/porta para o IP/porta antigo.

### Validação Após Mudança Local

Os peers não devem estabelecer múltiplas sessões com o mesmo peer, seja SSU 1 ou 2, ou com os mesmos ou diferentes endereços IP. No entanto, isso pode acontecer, seja devido a bugs, ou uma mensagem de terminação de sessão anterior ter sido perdida, ou em uma condição de corrida onde a mensagem de terminação ainda não chegou.

Se Bob tem uma sessão existente com Alice, quando Bob recebe o Session Confirmed de Alice, completando o handshake e estabelecendo uma nova sessão, Bob deve:

- Sair da fase de validação de caminho
- Todos os pacotes são enviados para o IP e porta antigos.
- As restrições na janela de congestionamento e PMTU são removidas, e eles têm permissão para aumentar.
- Opcionalmente, iniciar uma validação de caminho no IP e porta antigos. Se falhar, encerrar a sessão.
- Caso contrário, seguir as regras padrão de timeout e encerramento da sessão.
- Retransmitir quaisquer pacotes de dados que foram previamente enviados para o novo IP/porta para o IP/porta antigo.

### Usar como Ping/Pong

Sessões na fase de handshake são geralmente terminadas simplesmente por timeout, ou por não responder mais. Opcionalmente, elas podem ser terminadas incluindo um bloco de Terminação na resposta, mas a maioria dos erros não pode ser respondida devido à falta de chaves criptográficas. Mesmo se as chaves estiverem disponíveis para uma resposta incluindo um bloco de terminação, geralmente não vale a pena o CPU para realizar o DH para a resposta. Uma exceção PODE ser um bloco de Terminação em uma mensagem de retry, que é barato de gerar.

As sessões na fase de dados são terminadas enviando uma mensagem de dados que inclui um bloco de Terminação. Esta mensagem também deve incluir um bloco ACK. Pode, se a sessão esteve ativa por tempo suficiente para que um token enviado anteriormente tenha expirado ou esteja prestes a expirar, um bloco New Token. Esta mensagem não solicita acknowledgment. Ao receber um bloco de Terminação com qualquer motivo exceto "Terminação Recebida", o peer responde com uma mensagem de dados contendo um bloco de Terminação com o motivo "Terminação Recebida".

### Fase de handshake

Após enviar ou receber um bloco de Terminação, a sessão deve entrar na fase de encerramento por algum período máximo de tempo a ser definido. O estado de encerramento é necessário para proteger contra a perda do pacote que contém o bloco de Terminação e pacotes em trânsito na outra direção. Durante a fase de encerramento, não há requisito para processar quaisquer pacotes recebidos adicionais. Uma sessão no estado de encerramento envia um pacote contendo um bloco de Terminação em resposta a qualquer pacote recebido que ela atribua à sessão. Uma sessão deve limitar a taxa na qual gera pacotes no estado de encerramento. Por exemplo, uma sessão poderia aguardar por um número progressivamente crescente de pacotes recebidos ou quantidade de tempo antes de responder aos pacotes recebidos.

## Múltiplas Sessões

Para minimizar o estado que um router mantém para uma sessão em encerramento, as sessões podem, mas não são obrigadas a, enviar exatamente o mesmo pacote com o mesmo número de pacote como está em resposta a qualquer pacote recebido. Nota: Permitir a retransmissão de um pacote de terminação é uma exceção ao requisito de que um novo número de pacote seja usado para cada pacote. Enviar novos números de pacote é principalmente vantajoso para recuperação de perda e controle de congestionamento, que não se espera que sejam relevantes para uma conexão fechada. Retransmitir o pacote final requer menos estado.

Após receber um bloco de Terminação com a razão "Termination Received", a sessão pode sair da fase de fechamento.

- Migrar quaisquer mensagens I2NP de saída não enviadas ou não confirmadas da sessão antiga para a nova
- Enviar uma terminação com código de motivo 22 na sessão antiga
- Remover a sessão antiga e substituí-la pela nova

## Encerramento de Sessão

### Fase de dados

Após qualquer encerramento normal ou anormal, os routers devem zerar todos os dados efêmeros na memória, incluindo chaves efêmeras de handshake, chaves de criptografia simétricas e informações relacionadas.

### Limpeza

Os requisitos variam, baseados em se o endereço publicado é compartilhado com SSU 1. O mínimo atual de SSU 1 IPv4 é 620, que é definitivamente muito pequeno.

O MTU mínimo do SSU2 é 1280 para IPv4 e IPv6, que é o mesmo especificado na [RFC-9000](https://tools.ietf.org/html/rfc9000). Veja abaixo. Ao aumentar o MTU mínimo, mensagens de tunnel de 1 KB e mensagens curtas de construção de tunnel caberão em um datagrama, reduzindo drasticamente a quantidade típica de fragmentação. Isso também permite um aumento no tamanho máximo de mensagem I2NP. Mensagens de streaming de 1820 bytes devem caber em dois datagramas.

Um router não deve habilitar SSU2 ou publicar um endereço SSU2 a menos que o MTU para esse endereço seja de pelo menos 1280.

Os routers devem publicar um MTU não padrão em cada endereço de router SSU ou SSU2.

### Endereço SSU

Endereço compartilhado com SSU 1, deve seguir as regras do SSU 1. IPv4: Padrão e máximo é 1484. Mínimo é 1292. (IPv4 MTU + 4) deve ser múltiplo de 16. IPv6: Deve ser publicado, mínimo é 1280 e o máximo é 1488. IPv6 MTU deve ser múltiplo de 16.

## MTU

IPv4: Padrão e máximo é 1500. Mínimo é 1280. IPv6: Padrão e máximo é 1500. Mínimo é 1280. Não há regras de múltiplos de 16, mas provavelmente deveria ser um múltiplo de 2 no mínimo.

Para SSU 1, o I2P Java atual realiza descoberta de PMTU começando com pacotes pequenos e aumentando gradualmente o tamanho, ou aumentando baseado no tamanho do pacote recebido. Isso é rudimentar e reduz muito a eficiência. Continuar com esta funcionalidade no SSU 2 está a ser determinado.

Estudos recentes [PMTU](https://en.wikipedia.org/wiki/Path_MTU_Discovery) sugerem que um mínimo para IPv4 de 1200 ou mais funcionaria para mais de 99% das conexões. QUIC [RFC-9000](https://tools.ietf.org/html/rfc9000) requer um tamanho mínimo de pacote IP de 1280 bytes.

citação [RFC-9000](https://tools.ietf.org/html/rfc9000):

### Endereço SSU2

O tamanho máximo do datagrama é definido como o maior tamanho de carga útil UDP que pode ser enviado através de um caminho de rede usando um único datagrama UDP. QUIC NÃO DEVE ser usado se o caminho de rede não puder suportar um tamanho máximo de datagrama de pelo menos 1200 bytes.

### Descoberta de PMTU

QUIC assume um tamanho mínimo de pacote IP de pelo menos 1280 bytes. Este é o tamanho mínimo do IPv6 [IPv6] e também é suportado pela maioria das redes IPv4 modernas. Assumindo o tamanho mínimo do cabeçalho IP de 40 bytes para IPv6 e 20 bytes para IPv4 e um tamanho de cabeçalho UDP de 8 bytes, isso resulta em um tamanho máximo de datagrama de 1232 bytes para IPv6 e 1252 bytes para IPv4. Assim, espera-se que as redes IPv4 modernas e todos os caminhos de rede IPv6 sejam capazes de suportar QUIC.

### Tamanho Mínimo do Handshake

Nota: Este requisito de suportar um payload UDP de 1200 bytes limita o espaço disponível para cabeçalhos de extensão IPv6 a 32 bytes ou opções IPv4 a 52 bytes se o caminho suportar apenas o MTU mínimo IPv6 de 1280 bytes. Isso afeta os pacotes Initial e a validação de caminho.

fim da citação

QUIC exige que os datagramas Initial em ambas as direções tenham pelo menos 1200 bytes, para prevenir ataques de amplificação e garantir que o PMTU suporte isso em ambas as direções.

Poderíamos exigir isso para Session Request e Session Created, com um custo substancial em largura de banda. Talvez pudéssemos fazer isso apenas se não tivermos um token, ou após uma mensagem Retry ser recebida. A ser determinado

QUIC exige que Bob não envie mais de três vezes a quantidade de dados recebidos até que o endereço do cliente seja validado. SSU2 atende a esse requisito inerentemente, porque a mensagem Retry tem aproximadamente o mesmo tamanho da mensagem Token Request, e é menor que a mensagem Session Request. Além disso, a mensagem Retry é enviada apenas uma vez.

QUIC requer que mensagens contendo blocos PATH_CHALLENGE ou PATH_RESPONSE tenham pelo menos 1200 bytes, para prevenir ataques de amplificação e garantir que o PMTU suporte isso em ambas as direções.

Poderíamos exigir isso também, com um custo substancial em largura de banda. No entanto, esses casos devem ser raros. A definir

### Tamanho Mínimo da Mensagem de Caminho

IPv4: Não é assumida fragmentação de IP. O cabeçalho IP + datagrama é de 28 bytes. Isso assume que não há opções IPv4. O tamanho máximo da mensagem é MTU - 28. O cabeçalho da fase de dados é de 16 bytes e o MAC é de 16 bytes, totalizando 32 bytes. O tamanho do payload é MTU - 60. O payload máximo da fase de dados é 1440 para um MTU máximo de 1500. O payload máximo da fase de dados é 1220 para um MTU mínimo de 1280.

IPv6: Não é permitida fragmentação de IP. O cabeçalho IP + datagrama tem 48 bytes. Isto assume que não há cabeçalhos de extensão IPv6. O tamanho máximo da mensagem é MTU - 48. O cabeçalho da fase de dados tem 16 bytes e o MAC tem 16 bytes, totalizando 32 bytes. O tamanho do payload é MTU - 80. O payload máximo da fase de dados é 1420 para um MTU máximo de 1500. O payload máximo da fase de dados é 1200 para um MTU mínimo de 1280.

No SSU 1, as diretrizes eram um máximo rigoroso de cerca de 32 KB para uma mensagem I2NP baseado em 64 fragmentos máximos e um MTU mínimo de 620. Devido ao overhead para LeaseSets agrupados e chaves de sessão, o limite prático no nível da aplicação era cerca de 6KB menor, ou cerca de 26KB. O protocolo SSU 1 permite 128 fragmentos, mas as implementações atuais limitam a 64 fragmentos.

### Tamanho Máximo da Mensagem I2NP

Ao elevar o MTU mínimo para 1280, com uma carga útil de fase de dados de aproximadamente 1200, uma mensagem SSU 2 de cerca de 76 KB é possível em 64 fragmentos e 152 KB em 128 fragmentos. Isso facilmente permite um máximo de 64 KB.

Devido à fragmentação em tunnels e fragmentação no SSU 2, a probabilidade de perda de mensagens aumenta exponencialmente com o tamanho da mensagem. Continuamos a recomendar um limite prático de cerca de 10 KB na camada de aplicação para datagramas I2NP.

### Versões

Consulte a Segurança do Teste de Peer acima para uma análise do Teste de Peer SSU1 e os objetivos para o Teste de Peer SSU2.

Quando rejeitado por Bob:

Quando rejeitado por Charlie:

NOTA: RI pode ser enviado como mensagens I2NP Database Store em blocos I2NP, ou como blocos RI (se pequeno o suficiente). Estes podem estar contidos nos mesmos pacotes que os blocos de teste de peer, se pequenos o suficiente.

As mensagens 1-4 estão em sessão usando blocos Peer Test numa mensagem Data. As mensagens 5-7 estão fora de sessão usando blocos Peer Test numa mensagem Peer Test.

## Processo de Teste de Peer

NOTA: Como no SSU 1, as mensagens 4 e 5 podem chegar em qualquer ordem. A mensagem 5 e/ou 7 podem não ser recebidas se Alice estiver atrás de firewall. Quando a mensagem 5 chega antes da mensagem 4, Alice não pode enviar imediatamente a mensagem 6, porque ela ainda não possui a chave de introdução do Charlie para criptografar o cabeçalho. Quando a mensagem 4 chega antes da mensagem 5, Alice não deve enviar imediatamente a mensagem 6, porque ela deve aguardar para ver se a mensagem 5 chega sem abrir o firewall com a mensagem 6.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest
        <---------------- Charlie RI
4.      <------------------ PeerTest

5.      <----------------------------------------- PeerTest
6. PeerTest ----------------------------------------->
7.      <----------------------------------------- PeerTest
```
Testes de peers entre versões diferentes não são suportados. A única combinação de versão permitida é quando todos os peers são versão 2.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
4.      <------------------ PeerTest (reject)
```
As mensagens 1-4 estão em sessão e são cobertas pelos processos de ACK da fase de dados e retransmissão. Os blocos Peer Test provocam confirmação.

```
Alice                     Bob                  Charlie
1. PeerTest ------------------->
                            Alice RI ------------------->
2.                          PeerTest ------------------->
3.                             <------------------ PeerTest (reject)
                      (optional: Bob could try another Charlie here)
4.      <------------------ PeerTest (reject)
```
As mensagens 5-7 podem ser retransmitidas, inalteradas.

Como no SSU 1, o teste de endereços IPv6 é suportado, e a comunicação Alice-Bob e Alice-Charlie pode ser via IPv6, se Bob e Charlie indicarem suporte com uma capacidade 'B' em seu endereço IPv6 publicado. Consulte a Proposta 126 para detalhes.

Como no SSU 1 anterior à versão 0.9.50, Alice envia a solicitação para Bob usando uma sessão existente sobre o transporte (IPv4 ou IPv6) que ela deseja testar. Quando Bob recebe uma solicitação de Alice via IPv4, Bob deve selecionar um Charlie que anuncia um endereço IPv4. Quando Bob recebe uma solicitação de Alice via IPv6, Bob deve selecionar um Charlie que anuncia um endereço IPv6. A comunicação real Bob-Charlie pode ser via IPv4 ou IPv6 (ou seja, independente do tipo de endereço de Alice). Este NÃO é o comportamento do SSU 1 a partir da versão 0.9.50, onde solicitações mistas IPv4/v6 são permitidas.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Path</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Intro Key</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->C session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->B session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4</td><td style="border:1px solid var(--color-border); padding:0.6rem;">B->A session</td><td style="border:1px solid var(--color-border); padding:0.6rem;">in-session</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">A->C</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">C->A</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Alice</td></tr>
  </tbody>
</table>
### Retransmissões

Ao contrário do SSU 1, Alice especifica o IP e porta de teste solicitados na mensagem 1. Bob deve validar este IP e porta, e rejeitar com código 5 se inválidos. A validação de IP recomendada é que, para IPv4, corresponda ao IP de Alice, e para IPv6, pelo menos os primeiros 8 bytes do IP correspondam. A validação de porta deve rejeitar portas privilegiadas e portas para protocolos bem conhecidos.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 1 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, Bob must select a version 2 Charlie</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### Notas sobre IPv6

Aqui documentamos como Alice pode determinar os resultados de um teste de peer, baseado em quais mensagens são recebidas. As melhorias do SSU2 nos oferecem a oportunidade de corrigir, melhorar e documentar melhor a máquina de estados dos resultados do teste de peer comparado àquela em [SSU](/docs/transport/ssu).

Para cada tipo de endereço testado (IPv4 ou IPv6), o resultado pode ser UNKNOWN, OK, FIREWALLED, ou SYMNAT. Além disso, outros processamentos podem ser feitos para detectar mudança de IP ou porta, ou uma porta externa diferente da porta interna.

### Processamento por Bob

Problemas com a máquina de estados SSU documentada:

Então, em contraste com o SSU, recomendamos aguardar vários segundos após receber a mensagem 4, depois enviar a mensagem 6 mesmo que a mensagem 5 não seja recebida.

### Máquina de Estados dos Resultados

Um resumo da máquina de estados, baseado em se as mensagens 4, 5 e 7 são recebidas (sim ou não), é o seguinte:

### Retransmissões

Uma máquina de estados mais detalhada, com verificações do IP/porta recebidos no bloco de endereço da mensagem 7, está abaixo. Um desafio é determinar se você (Alice) é quem tem NAT simétrico, ou se é o Charlie.

Recomenda-se pós-processamento ou lógica adicional para confirmar transições de estado exigindo os mesmos resultados em dois ou mais testes de peer.

A validação e confirmação de IP/porta recebida por dois ou mais testes, ou com o bloco de endereço nas mensagens Session Created, também é recomendada, mas está fora do escopo desta especificação.

- Nunca enviamos a mensagem 6 a menos que tenhamos recebido a mensagem 5, então nunca sabemos se somos SYMNAT
- Se recebemos as mensagens 4 e 7, como poderíamos possivelmente ser SYMNAT
- Se o IP não correspondeu mas a porta correspondeu, não somos SYMNAT, apenas mudamos nosso IP

Veja Segurança do Relay acima para uma análise do SSU1 Relay e os objetivos para o SSU2 Relay.

Quando rejeitado por Bob:

```
4 5 7  Result             Notes
-----  ------             -----
n n n  UNKNOWN
y n n  FIREWALLED           (unless currently SYMNAT)
n y n  OK                   (unless currently SYMNAT, which is unlikely)
y y n  OK                   (unless currently SYMNAT, which is unlikely)
n n y  n/a                  (can't send msg 6)
y n y  FIREWALLED or SYMNAT (requires sending msg 6 w/o rcv msg 5)
n y y  n/a                  (can't send msg 6)
y y y  OK
```
Quando rejeitado por Charlie:

NOTA: RI pode ser enviado tanto como mensagens I2NP Database Store em blocos I2NP, ou como blocos RI (se pequenos o suficiente). Estes podem estar contidos nos mesmos pacotes que os blocos de retransmissão, se pequenos o suficiente.

No SSU 1, as informações do router de Charlie contêm o IP, porta, chave de introdução, tag de relay e expiração de cada introducer.

```
If Alice does not get msg 5:
   If Alice does not get msg 4: -> UNKNOWN
   If Alice does not get msg 7: -> UNKNOWN
   If Alice gets msgs 4/7 and IP/port match: -> FIREWALLED
   If Alice gets msgs 4/7 and IP matches, port does not match:
      -> SYMNAT, but needs confirmation with 2nd test
   If Alice gets msgs 4/7 and IP does not match, port matches:
      -> FIREWALLED, address change?
   If Alice gets msgs 4/7 and both IP and port do not match:
      -> SYMNAT, address change?

If Alice gets msg 5:
   If Alice does not get msg 4: -> OK unless currently SYMNAT, else UNKNOWN
                                   (in SSU2 have to stop here)
   If Alice does not get msg 7: -> OK unless currently SYMNAT, else UNKNOWN
   If Alice gets msgs 4/5/7 and IP/port match: -> OK
   If Alice gets msgs 4/5/7 and IP matches, port does not match:
      -> OK, charlie is probably sym. natted
   If Alice gets msgs 4/5/7 and IP does not match, port matches:
      -> OK, address change?
   If Alice gets msgs 4/5/7 and both IP and port do not match:
      -> OK, address change?
```
## Processo de Relay

No SSU 2, as informações do router de Charlie contêm o hash do router, relay tag e expiração de cada introducer.

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse

5.      <-------------------------------------------- HolePunch
6. SessionRequest -------------------------------------------->
7.      <-------------------------------------------- SessionCreated
8. SessionConfirmed ------------------------------------------>
```
Alice deve reduzir o número de viagens de ida e volta necessárias primeiro selecionando um introducer (Bob) ao qual ela já possui uma conexão. Em segundo lugar, se não houver nenhum, selecionar um introducer para o qual ela já possui as informações do router.

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
4.      <-------------- RelayResponse
```
O relaying entre versões também deve ser suportado se possível. Isso facilitará uma transição gradual do SSU 1 para o SSU 2. As combinações de versões permitidas são (TODO):

```
Alice                         Bob                  Charlie
   lookup Bob RI

   SessionRequest -------------------->
        <------------  SessionCreated
   SessionConfirmed  ----------------->

1. RelayRequest ---------------------->
                                         Alice RI  ------------>
2.                                       RelayIntro ----------->
3.                                  <-------------- RelayResponse
4.      <-------------- RelayResponse
```
Relay Request, Relay Intro e Relay Response são todos in-session e são cobertos pelos processos de ACK da fase de dados e retransmissão. Os blocos Relay Request, Relay Intro e Relay Response provocam ack.

Note que normalmente, Charlie responderá imediatamente a um Relay Intro com um Relay Response, que deve incluir um bloco ACK. Nesse caso, não é necessária uma mensagem separada com um bloco ACK.

O hole punch pode ser retransmitido, como no SSU 1.

Ao contrário das mensagens I2NP, as mensagens Relay não possuem identificadores únicos, portanto as duplicatas devem ser detectadas pela máquina de estado do relay, usando o nonce. As implementações também podem precisar manter um cache de nonces usados recentemente, para que duplicatas recebidas possam ser detectadas mesmo após a máquina de estado para aquele nonce ter sido concluída.

Todas as funcionalidades do relay SSU 1 são suportadas, incluindo aquelas documentadas na [Prop158](/proposals/158-ipv6-transport-enhancements) e suportadas a partir da versão 0.9.50. Introduções IPv4 e IPv6 são suportadas. Uma Solicitação de Relay pode ser enviada através de uma sessão IPv4 para uma introdução IPv6, e uma Solicitação de Relay pode ser enviada através de uma sessão IPv6 para uma introdução IPv4.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Bob</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bob/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Alice/Charlie</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SSU 1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/1/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 1/2/1</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes?</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">no, use 2/2/2</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">2</td><td style="border:1px solid var(--color-border); padding:0.6rem;">yes</td></tr>
  </tbody>
</table>
### IPv4/v6

A seguir estão as diferenças do SSU 1 e recomendações para implementação do SSU 2.

No SSU 1, a introdução é relativamente barata, e Alice geralmente envia Relay Requests para todos os introdutores. No SSU 2, a introdução é mais cara, pois uma conexão deve primeiro ser estabelecida com um introdutor. Para minimizar a latência e sobrecarga da introdução, os passos de processamento recomendados são os seguintes:

Em ambos SSU 1 e SSU 2, a Resposta de Retransmissão e o Hole Punch podem ser recebidos em qualquer ordem, ou podem não ser recebidos de forma alguma.

No SSU 1, Alice geralmente recebe a Relay Response (1 RTT) antes do Hole Punch (1 1/2 RTT). Pode não estar bem documentado nessas especificações, mas Alice deve receber a Relay Response de Bob antes de continuar, para receber o IP de Charlie. Se o Hole Punch for recebido primeiro, Alice não o reconhecerá, porque não contém dados e o IP de origem não é reconhecido. Após receber a Relay Response, Alice deve aguardar TANTO o recebimento do Hole Punch de Charlie, OU um pequeno atraso (recomendado 500 ms) antes de iniciar o handshake com Charlie.

### Processando por Alice

No SSU 2, Alice geralmente receberá o Hole Punch (1 1/2 RTT) antes da Relay Response (2 RTT). O Hole Punch do SSU 2 é mais fácil de processar do que no SSU 1, porque é uma mensagem completa com IDs de conexão definidos (derivados do nonce do relay) e conteúdo incluindo o IP do Charlie. A Relay Response (mensagem Data) e a mensagem Hole Punch contêm o bloco Relay Response assinado idêntico. Portanto, Alice pode iniciar o handshake com Charlie após OU receber o Hole Punch do Charlie, OU receber a Relay Response do Bob.

### Solicitações de Tag por Bob

A verificação de assinatura do Hole Punch inclui o hash do router do introdutor (Bob). Se Relay Requests foram enviados para mais de um introdutor, existem várias opções para validar a assinatura:

#### Resumo

Se Charlie estiver atrás de um NAT simétrico, sua porta reportada na Relay Response e Hole Punch pode não ser precisa. Portanto, Alice deve verificar a porta de origem UDP da mensagem Hole Punch e usar essa se for diferente da porta reportada.

- Ignore qualquer introducer que esteja expirado com base no valor iexp no endereço
- Se uma conexão SSU2 já estiver estabelecida com um ou mais introducers, escolha um e envie a Relay Request apenas para esse introducer.
- Caso contrário, se um Router Info for conhecido localmente para um ou mais introducers, escolha um e conecte apenas a esse introducer.
- Caso contrário, consulte os Router Infos para todos os introducers, conecte ao introducer cujo Router Info for recebido primeiro.

#### Detalhes

No SSU 1, apenas Alice poderia solicitar uma tag, na Solicitação de Sessão. Bob nunca poderia solicitar uma tag, e Alice não poderia retransmitir para Bob.

No SSU2, Alice geralmente solicita uma tag na Solicitação de Sessão, mas tanto Alice quanto Bob também podem solicitar uma tag na fase de dados. Bob geralmente não está atrás de firewall após receber uma solicitação de entrada, mas pode estar após um relay, ou o estado de Bob pode mudar, ou ele pode solicitar um introducer para o outro tipo de endereço (IPv4/v6). Portanto, no SSU2, é possível que tanto Alice quanto Bob sejam simultaneamente relays para a outra parte.

As seguintes propriedades de endereço podem ser publicadas, inalteradas do SSU 1, incluindo mudanças na [Prop158](/proposals/158-ipv6-transport-enhancements) suportadas a partir da API 0.9.50:

O RouterAddress publicado (parte do RouterInfo) terá um identificador de protocolo "SSU" ou "SSU2".

- Tente cada hash para o qual uma solicitação foi enviada
- Use nonces diferentes para cada introducer, e use isso para determinar qual introducer este Hole Punch foi em resposta a
- Não revalide a assinatura se o conteúdo for idêntico ao da Relay Response, se já recebido
- Não valide a assinatura de forma alguma

O RouterAddress deve conter três opções para indicar suporte SSU2:

### Propriedades do Endereço

Alice deve verificar se todas as três opções estão presentes e válidas antes de conectar usando o protocolo SSU2.

Quando publicado como "SSU" com as opções "s", "i" e "v", e com as opções "host" e "port", o router deve aceitar conexões de entrada nesse host e porta para ambos os protocolos SSU e SSU2, e detectar automaticamente a versão do protocolo.

## Informações do Router Publicadas

### Endereços Publicados

Quando publicado como "SSU2" com as opções "s", "i" e "v", e com as opções "host" e "port", o router aceita conexões de entrada nesse host e porta apenas para o protocolo SSU2.

- caps: capacidades [B,C,4,6]
- host: IP (IPv4 ou IPv6). Endereço IPv6 abreviado (com "::") é permitido. Pode ou não estar presente se estiver protegido por firewall. Nomes de host não são permitidos.
- iexp[0-2]: Expiração deste introducer. Dígitos ASCII, em segundos desde a época. Presente apenas se protegido por firewall, e introducers são necessários. Opcional (mesmo se outras propriedades para este introducer estiverem presentes).
- ihost[0-2]: IP do introducer (IPv4 ou IPv6). Endereço IPv6 abreviado (com "::") é permitido. Presente apenas se protegido por firewall, e introducers são necessários. Nomes de host não são permitidos. Apenas endereço SSU.
- ikey[0-2]: Chave de introdução Base 64 do introducer. Presente apenas se protegido por firewall, e introducers são necessários. Apenas endereço SSU.
- iport[0-2]: Porta do introducer 1024 - 65535. Presente apenas se protegido por firewall, e introducers são necessários. Apenas endereço SSU.
- itag[0-2]: Tag do introducer 1 - (2**32 - 1) dígitos ASCII. Presente apenas se protegido por firewall, e introducers são necessários.
- key: Chave de introdução Base 64.
- mtu: Opcional. Veja a seção MTU acima.
- port: 1024 - 65535 Pode ou não estar presente se estiver protegido por firewall.

### Endereço SSU2 Não Publicado

Se um router suporta tanto conexões SSU1 quanto SSU2 mas não implementa detecção automática de versão para conexões de entrada, ele deve anunciar tanto endereços "SSU" quanto "SSU2", e incluir as opções SSU2 apenas no endereço "SSU2". O router deve definir um valor de custo mais baixo (prioridade mais alta) no endereço "SSU2" do que no endereço "SSU", para que SSU2 seja preferido.

Se múltiplos RouterAddresses SSU2 (seja como "SSU" ou "SSU2") forem publicados no mesmo RouterInfo (para endereços IP ou portas adicionais), todos os endereços que especificam a mesma porta devem conter as opções e valores SSU2 idênticos. Em particular, todos devem conter a mesma chave estática "s" e chave de introdução "i".

- s=(Chave Base64) A chave pública estática Noise atual (s) para este RouterAddress. Codificada em Base 64 usando o alfabeto I2P Base 64 padrão. 32 bytes em binário, 44 bytes codificados em Base 64, chave pública X25519 little-endian.
- i=(Chave Base64) A chave de introdução atual para criptografar os cabeçalhos para este RouterAddress. Codificada em Base 64 usando o alfabeto I2P Base 64 padrão. 32 bytes em binário, 44 bytes codificados em Base 64, chave ChaCha20 big-endian.
- v=2 A versão atual (2). Quando publicado como "SSU", suporte adicional para versão 1 está implícito. Suporte para versões futuras será com valores separados por vírgula, ex: v=2,3. A implementação deve verificar compatibilidade, incluindo múltiplas versões se uma vírgula estiver presente. Versões separadas por vírgula devem estar em ordem numérica.

Quando publicado como SSU ou SSU2 com introdutores, as seguintes opções estão presentes:

As seguintes opções são apenas para SSU e não são usadas para SSU2. No SSU2, Alice obtém essa informação do RI do Charlie.

Um router não deve publicar host ou porta no endereço ao publicar introducers. Um router deve publicar caps 4 e/ou 6 no endereço ao publicar introducers para indicar suporte para IPv4 e/ou IPv6. Isso é o mesmo que a prática atual para endereços SSU 1 recentes.

Nota: Se publicado como SSU, e houver uma mistura de introducers SSU 1 e SSU2, os introducers SSU 1 devem estar nos índices mais baixos e os introducers SSU2 devem estar nos índices mais altos, para compatibilidade com routers mais antigos.

Se Alice não publicar seu endereço SSU2 (como "SSU" ou "SSU2") para conexões de entrada, ela deve publicar um endereço de router "SSU2" contendo apenas sua chave estática e versão SSU2, para que Bob possa validar a chave após receber o RouterInfo de Alice na parte 2 do Session Confirmed.

#### Tratamento de Erros

Este endereço do router não conterá opções "host" ou "port", pois estas não são necessárias para conexões SSU2 de saída. O custo publicado para este endereço não importa estritamente, pois é apenas de entrada; no entanto, pode ser útil para outros routers se o custo for definido mais alto (prioridade mais baixa) do que outros endereços. O valor sugerido é 14.

- ih[0-2]=(Base64 hash) Um hash de router para um introducer. Codificado em Base 64 usando o alfabeto I2P Base 64 padrão. 32 bytes em binário, 44 bytes como Base 64 codificado
- iexp[0-2]: Expiração deste introducer. Inalterado do SSU 1.
- itag[0-2]: Tag do introducer 1 - (2**32 - 1) Inalterado do SSU 1.

Alice também pode simplesmente adicionar as opções "i", "s" e "v" a um endereço "SSU" já publicado existente.

- ihost[0-2]
- ikey[0-2]
- itag[0-2]

Usar as mesmas chaves estáticas para NTCP2 e SSU2 é permitido, mas não recomendado.

Devido ao cache de RouterInfos, os routers não devem rotacionar a chave pública estática ou IV enquanto o router estiver ativo, seja em um endereço publicado ou não. Os routers devem armazenar persistentemente esta chave e IV para reutilização após uma reinicialização imediata, para que as conexões de entrada continuem funcionando e os tempos de reinicialização não sejam expostos. Os routers devem armazenar persistentemente, ou determinar de outra forma, o horário do último desligamento, para que o tempo de inatividade anterior possa ser calculado na inicialização.

### Rotação de Chave Pública e IV

Sujeito a preocupações sobre expor tempos de reinicialização, os routers podem rotacionar essa chave ou IV na inicialização se o router esteve previamente inativo por algum tempo (pelo menos vários dias).

- s=(chave Base64) Conforme definido acima para endereços publicados.
- i=(chave Base64) Conforme definido acima para endereços publicados.
- v=2 Conforme definido acima para endereços publicados.

Se o router tiver RouterAddresses SSU2 publicados (como SSU ou SSU2), o tempo mínimo de inatividade antes da rotação deve ser muito maior, por exemplo um mês, a menos que o endereço IP local tenha mudado ou o router faça "rekeys".

Se o router tem qualquer RouterAddresses SSU publicados, mas não SSU2 (como SSU ou SSU2), o tempo mínimo de inatividade antes da rotação deve ser maior, por exemplo um dia, a menos que o endereço IP local tenha mudado ou o router faça "rekeys". Isto aplica-se mesmo se o endereço SSU publicado tiver introducers.

### Criação de Pacotes de Saída

Se o router não possui RouterAddresses publicados (SSU, SSU2, ou SSU), o tempo mínimo de inatividade antes da rotação pode ser tão curto quanto duas horas, mesmo se o endereço IP mudar, a menos que o router faça "rekeys".

Se o router "rekeys" para um Router Hash diferente, ele deve gerar uma nova chave de ruído e chave de introdução também.

As implementações devem estar cientes de que alterar a chave pública estática ou o IV impedirá conexões SSU2 de entrada de routers que tenham em cache um RouterInfo mais antigo. A publicação do RouterInfo, seleção de pares de tunnel (incluindo tanto OBGW quanto o hop mais próximo IB), seleção de tunnel de zero-hop, seleção de transporte e outras estratégias de implementação devem levar isso em consideração.

A rotação de chaves de introdução está sujeita às mesmas regras da rotação de chaves.

Nota: O tempo mínimo de inatividade antes da regeneração de chaves pode ser modificado para garantir a saúde da rede e para prevenir o reseeding por um router que esteve inativo por um período moderado de tempo.

A negação plausível não é um objetivo. Veja a visão geral acima.

Cada padrão recebe propriedades que descrevem a confidencialidade fornecida à chave pública estática do iniciador e à chave pública estática do respondedor. As suposições subjacentes são que as chaves privadas efêmeras são seguras, e que as partes abortam o handshake se receberem uma chave pública estática da outra parte na qual não confiam.

Esta seção considera apenas o vazamento de identidade através de campos de chave pública estática em handshakes. É claro que as identidades dos participantes Noise podem ser expostas através de outros meios, incluindo campos de payload, análise de tráfego, ou metadados como endereços IP.

Alice: (8) Criptografado com forward secrecy para uma parte autenticada.

Bob: (3) Não transmitido, mas um atacante passivo pode verificar candidatos para a chave privada do respondente e determinar se o candidato está correto.

#### Ocultação de Identidade

Bob publica sua chave pública estática no netDb. Alice pode não fazê-lo, mas deve incluí-la no RI enviado para Bob.

Mensagens de handshake (Session Request/Created/Confirmed, Retry) passos básicos, em ordem:

Etapas básicas das mensagens da fase de dados, em ordem:

Processamento inicial de todas as mensagens de entrada:

Processamento de mensagens de handshake (Session Request/Created/Confirmed, Retry, Token Request) e outras mensagens fora de sessão (Peer Test, Hole Punch):

Processamento de mensagens da fase de dados:

## Diretrizes de Pacotes

### Tratamento de Pacotes de Entrada

No SSU 1, a classificação de pacotes de entrada é difícil, porque não há cabeçalho para indicar o número da sessão. Os routers devem primeiro corresponder o IP e porta de origem a um estado de peer existente, e se não for encontrado, tentar múltiplas descriptografias com diferentes chaves para encontrar o estado de peer apropriado ou iniciar um novo. No caso de o IP ou porta de origem para uma sessão existente mudar, possivelmente devido ao comportamento NAT, o router pode usar heurísticas custosas para tentar corresponder o pacote a uma sessão existente e recuperar o conteúdo.

- Criar cabeçalho de 16 ou 32 bytes
- Criar payload
- mixHash() o cabeçalho (exceto para Retry)
- Criptografar o payload usando Noise (exceto para Retry, usar ChaChaPoly com o cabeçalho como AD)
- Criptografar o cabeçalho e, para Session Request/Created, a chave efêmera

O SSU 2 foi projetado para minimizar o esforço de classificação de pacotes de entrada, mantendo a resistência a DPI e outras ameaças no caminho. O número do Connection ID está incluído no cabeçalho para todos os tipos de mensagem e criptografado (ofuscado) usando ChaCha20 com uma chave e nonce conhecidos. Além disso, o tipo de mensagem também está incluído no cabeçalho (criptografado com proteção de cabeçalho para uma chave conhecida e depois ofuscado com ChaCha20) e pode ser usado para classificação adicional. Em nenhum caso é necessária uma operação criptográfica assimétrica de teste DH ou outra para classificar um pacote.

- Criar cabeçalho de 16 bytes
- Criar payload
- Criptografar o payload usando ChaChaPoly usando o cabeçalho como AD
- Criptografar o cabeçalho

### Notas

#### Resumo

Para quase todas as mensagens de todos os peers, a chave ChaCha20 para a criptografia do Connection ID é a chave de introdução do router de destino conforme publicada no netDb.

- Descriptografar os primeiros 8 bytes do cabeçalho (o ID de Conexão de Destino) com a chave intro
- Procurar a conexão pelo ID de Conexão de Destino
- Se a conexão for encontrada e estiver na fase de dados, ir para a seção da fase de dados
- Se a conexão não for encontrada, ir para a seção de handshake
- Nota: Mensagens de Peer Test e Hole Punch também podem ser procuradas pelo ID de Conexão de Destino criado a partir do nonce de teste ou relay.

As únicas exceções são as primeiras mensagens enviadas de Bob para Alice (Session Created ou Retry) onde a chave de introdução de Alice ainda não é conhecida por Bob. Nestes casos, a chave de introdução de Bob é usada como a chave.

- Descriptografar bytes 8-15 do cabeçalho (o tipo de pacote, versão e ID da rede) com a chave de introdução. Se for um Session Request, Token Request, Peer Test ou Hole Punch válido, continuar
- Se não for uma mensagem válida, procurar uma conexão de saída pendente pelo IP/porta de origem do pacote, tratar o pacote como Session Created ou Retry. Re-descriptografar os primeiros 8 bytes do cabeçalho com a chave correta, e os bytes 8-15 do cabeçalho (o tipo de pacote, versão e ID da rede). Se for um Session Created ou Retry válido, continuar
- Se não for uma mensagem válida, falhar, ou colocar na fila como um possível pacote da fase de dados fora de ordem
- Para Session Request/Created, Retry, Token Request, Peer Test e Hole Punch, descriptografar bytes 16-31 do cabeçalho
- Para Session Request/Created, descriptografar a chave efêmera
- Validar todos os campos do cabeçalho, parar se não for válido
- mixHash() o cabeçalho
- Para Session Request/Created/Confirmed, descriptografar o payload usando Noise
- Para Retry e fase de dados, descriptografar o payload usando ChaChaPoly
- Processar o cabeçalho e payload

O protocolo foi projetado para minimizar o processamento de classificação de pacotes que poderia exigir operações criptográficas adicionais em múltiplas etapas de fallback ou heurísticas complexas. Além disso, a grande maioria dos pacotes recebidos não exigirá uma busca de fallback (possivelmente custosa) por IP/porta de origem e uma segunda descriptografia de cabeçalho. Apenas Session Created e Retry (e possivelmente outros a serem definidos) exigirão o processamento de fallback. Se um endpoint alterar IP ou porta após a criação da sessão, o ID de conexão ainda é usado para localizar a sessão. Nunca é necessário usar heurísticas para encontrar a sessão, por exemplo, procurando por uma sessão diferente com o mesmo IP, mas uma porta diferente.

- Descriptografar os bytes 8-15 do cabeçalho (o tipo de pacote, versão e ID da rede) com a chave correta
- Descriptografar a carga útil usando ChaChaPoly usando o cabeçalho como AD
- Processar o cabeçalho e a carga útil

#### Detalhes

Portanto, as etapas de processamento recomendadas na lógica do loop do receptor são:

1)  Descriptografar os primeiros 8 bytes com ChaCha20 usando a chave de introdução local, para recuperar o ID de Conexão de Destino. Se o ID de Conexão corresponder a uma sessão de entrada atual ou pendente:

2) Se o ID da conexão não corresponder a uma sessão atual: Verifique se o cabeçalho em texto simples nos bytes 8-15 são válidos (sem executar qualquer operação de proteção de cabeçalho). Verifique se o ID da rede e a versão do protocolo são válidos, e se o tipo de mensagem é Session Request, ou outro tipo de mensagem permitido fora de sessão (a ser determinado).

3)  Procurar uma sessão de saída pendente pelo IP/porta de origem do pacote.

4)  Se estiver executando SSU 1 na mesma porta, tente processar a mensagem como um pacote SSU 1.

Em geral, uma sessão (na fase de handshake ou de dados) nunca deve ser destruída após receber um pacote com um tipo de mensagem inesperado. Isso previne ataques de injeção de pacotes. Esses pacotes também serão comumente recebidos após a retransmissão de um pacote de handshake, quando as chaves de descriptografia do cabeçalho não são mais válidas.

Na maioria dos casos, simplesmente descarte o pacote. Uma implementação pode, mas não é obrigatória, retransmitir o pacote enviado anteriormente (mensagem de handshake ou ACK 0) em resposta.

    a)  Using the appropriate key, decrypt the header bytes 8-15 to recover the version, net ID, and message type.
    b)  If the message type is Session Confirmed, it is a long header. Verify the net ID and protocol version are valid. Decrypt the bytes 15-31 of the header with ChaCha20 using the local intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise.
    c)  If the message type is valid but not Session Confirmed, it is a short header. Verify the net ID and protocol version are valid. decrypt the rest of the message with ChaCha20/Poly1305 using the session key, using the decrypted 16-byte header as the AD.
    d)  (optional) If connection ID is a pending inbound session awaiting a Session Confirmed message, but the net ID, protocol, or message type is not valid, it could be a Data message received out-of-order before the Session Confirmed, so the data phase header protection keys are not yet known, and the header bytes 8-15 were incorrectly decrypted. Queue the message, and attempt to decrypt it once the Session Confirmed message is received.
    e)  If b) or c) fails, drop the message.

Após enviar Session Created como Bob, pacotes inesperados são comumente pacotes Data que não podem ser descriptografados porque os pacotes Session Confirmed foram perdidos ou estão fora de ordem. Enfileire os pacotes e tente descriptografá-los após receber os pacotes Session Confirmed.

    a)  If all is valid and the message type is Session Request, decrypt bytes 16-31 of the header and the 32-byte X value with ChaCha20 using the local intro key.

    - If the token at header bytes 24-31 is accepted, then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Created in response.
    - If the token is not accepted, send a Retry message to the source IP/port with a token. Do not attempt to decrypt the message with Noise to avoid DDoS attacks.

    b)  If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.
    c)  If a) or b) fails, go to step 3)

Após receber Session Confirmed como Bob, pacotes inesperados são comumente pacotes Session Confirmed retransmitidos, porque o ACK 0 do Session Confirmed foi perdido. Os pacotes inesperados podem ser descartados. Uma implementação pode, mas não é obrigatória, enviar um pacote Data contendo um bloco ACK em resposta.

    a)  If found, re-decrypt the first 8 bytes with ChaCha20 using Bob's introduction key to recover the Destination Connection ID.
    b)  If the connection ID matches the pending session: Using the correct key, decrypt bytes 8-15 of the header to recover the version, net ID, and message type. Verify the net ID and protocol version are valid, and the message type is Session Created or Retry, or other message type allowed out-of-session (TBD).

    - If all is valid and the message type is Session Created, decrypt the next 16 bytes of the header and the 32-byte Y value with ChaCha20 using Bob's intro key. Then MixHash() the decrypted 32 byte header and decrypt the message with Noise. Send a Session Confirmed in response.
    - If all is valid and the message type is Retry, decrypt bytes 16-31 of the header with ChaCha20 using Bob's intro key. Decrypt and validate the message using ChaCha20/Poly1305 using TBD as the key and TBD as the nonce and the decrypted 32-byte header as the AD. Resend a Session Request with the received token in response.
    - If the message type is some other message that is valid out-of-session, presumably with a short header, decrypt the rest of the message with ChaCha20/Poly1305 using the intro key, and using the decrypted 16-byte header as the AD. Process the message.

    > c)  If a pending outbound session is not found, or the connection ID does not match the pending session, drop the message, unless the port is shared with SSU 1.

Para Session Created e Session Confirmed, as implementações devem validar cuidadosamente todos os campos de cabeçalho descriptografados (Connection IDs, número do pacote, tipo do pacote, versão, id, frag e flags) ANTES de chamar mixHash() no cabeçalho e tentar descriptografar o payload com Noise AEAD. Se a descriptografia Noise AEAD falhar, nenhum processamento adicional pode ser feito, porque mixHash() terá corrompido o estado do handshake, a menos que uma implementação armazene e "reverta" o estado do hash.

#### Tratamento de Erros

Pode não ser possível detectar eficientemente se os pacotes recebidos são versão 1 ou 2 na mesma porta de entrada. Os passos acima podem fazer sentido antes do processamento SSU 1, para evitar tentar operações DH de teste usando ambas as versões do protocolo.

A ser definido se necessário.

Assume IPv4, não incluindo preenchimento extra, não incluindo tamanhos de cabeçalho IP e UDP. O preenchimento é mod-16 apenas para SSU 1.

**SSU 1**

### Detecção de Versão

**SSU 2**

### Tokens

Especificamos acima que o token deve ser um valor de 8 bytes gerado aleatoriamente, não gerar um valor opaco como um hash ou HMAC de um segredo do servidor e o IP, porta, devido a ataques de reutilização. No entanto, isso requer armazenamento temporário e (opcionalmente) persistente de tokens entregues. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) usa um HMAC de 16 bytes de um segredo do servidor e endereço IP, e o segredo do servidor rotaciona a cada dois minutos. Devemos investigar algo semelhante, com um tempo de vida do segredo do servidor mais longo. Se incorporarmos um timestamp no token, isso pode ser uma solução, mas um token de 8 bytes pode não ser grande o suficiente para isso.

A definir se necessário.

## Constantes Recomendadas

- Timeout de retransmissão de handshake de saída: 1,25 segundos, com backoff exponencial (retransmissões em 1,25, 3,75 e 8,75 segundos)
- Timeout total de handshake de saída: 15 segundos
- Timeout de retransmissão de handshake de entrada: 1 segundo, com backoff exponencial (retransmissões em 1, 3 e 7 segundos)
- Timeout total de handshake de entrada: 12 segundos
- Timeout após envio de retry: 9 segundos
- Atraso de ACK: max(10, min(rtt/6, 150)) ms
- Atraso de ACK imediato: min(rtt/16, 5) ms
- Máximo de intervalos ACK: 256?
- Profundidade máxima de ACK: 512?
- Distribuição de padding: 0-15 bytes, ou maior
- Timeout mínimo de retransmissão da fase de dados: 1 segundo, conforme [RFC-6298](https://tools.ietf.org/html/rfc6298)
- Veja também [RFC-6298](https://tools.ietf.org/html/rfc6298) para orientações adicionais sobre temporizadores de retransmissão para a fase de dados.

## Análise de Sobrecarga de Pacotes

Supõe IPv4, sem incluir preenchimento extra, sem incluir os tamanhos dos cabeçalhos IP e UDP. O preenchimento é um preenchimento mod-16 apenas para SSU 1.

**SSU 1**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MAC</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">40</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">5</td><td style="border:1px solid var(--color-border); padding:0.6rem;">3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">304</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. extended options</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;">256</td><td style="border:1px solid var(--color-border); padding:0.6rem;">79</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1</td><td style="border:1px solid var(--color-border); padding:0.6rem;">336</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 64 byte Ed25519 sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">462</td><td style="border:1px solid var(--color-border); padding:0.6rem;">13</td><td style="border:1px solid var(--color-border); padding:0.6rem;">512</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 391 byte ident and 64 byte sig</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (RI)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1014</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1051</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header, 1000 byte RI</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">37</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">51</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Incl. 5 byte I2NP header</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">2254</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>
**SSU 2**

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Message</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Header+MACs</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Keys</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Padding</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Total</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Request</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">87</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Created</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">16</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">96</td><td style="border:1px solid var(--color-border); padding:0.6rem;">DateTime, Address blocks</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Session Confirmed</td><td style="border:1px solid var(--color-border); padding:0.6rem;">48</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1005</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1085</td><td style="border:1px solid var(--color-border); padding:0.6rem;">1000 byte compressed RI block</td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Data (1 full msg)</td><td style="border:1px solid var(--color-border); padding:0.6rem;">32</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">14</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">46</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
    <tr><td style="border:1px solid var(--color-border); padding:0.6rem;">Total</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td><td style="border:1px solid var(--color-border); padding:0.6rem;">1314</td><td style="border:1px solid var(--color-border); padding:0.6rem;"></td></tr>
  </tbody>
</table>    
## Problemas e Trabalhos Futuros

### Tokens

Especificamos acima que o token deve ser um valor de 8 bytes gerado aleatoriamente, e não um valor opaco como um hash ou HMAC de um segredo do servidor com o IP e porta, devido a ataques de reutilização. No entanto, isso exige armazenamento temporário e (opcionalmente) persistente dos tokens entregues. [WireGuard](https://www.wireguard.com/papers/wireguard.pdf) utiliza um HMAC de 16 bytes de um segredo do servidor e do endereço IP, sendo que o segredo do servidor é rotacionado a cada dois minutos. Devemos investigar algo semelhante, com um tempo de vida maior para o segredo do servidor. Se incorporarmos um carimbo de tempo (timestamp) no token, isso pode ser uma solução, mas um token de 8 bytes pode não ser grande o suficiente para isso.

## Referências

- **[Common]** [Especificação de Estruturas Comuns](/docs/specs/common-structures)
- **[ECIES]** [Especificação ECIES-X25519-AEAD-Ratchet](/docs/specs/ecies)
- **[NetDB]** [Base de Dados da Rede](/docs/overview/network-database)
- **[NOISE]** [Framework do Protocolo Noise](https://noiseprotocol.org/noise.html)
- **[Nonces]** [Adversários que Desrespeitam Nonce](https://eprint.iacr.org/2019/624.pdf)
- **[NTCP]** [Transporte NTCP](/docs/transport/ntcp)
- **[NTCP2]** [Especificação NTCP2](/docs/specs/ntcp2)
- **[PMTU]** [Descoberta de MTU do Caminho](https://en.wikipedia.org/wiki/Path_MTU_Discovery)
- **[Prop104]** [Proposta 104: Transporte TLS](/proposals/104-tls-transport)
- **[Prop109]** [Proposta 109: Transporte Plugável](/proposals/109-pt-transport)
- **[Prop158]** [Proposta 158: Melhorias de Transporte IPv6](/proposals/158-ipv6-transport-enhancements)
- **[Prop159]** [Proposta 159: SSU2](/proposals/159-ssu2)
- **[RFC-2104]** [RFC 2104: HMAC](https://tools.ietf.org/html/rfc2104)
- **[RFC-3449]** [RFC 3449: Implicações de Performance TCP](https://tools.ietf.org/html/rfc3449)
- **[RFC-3526]** [RFC 3526: Grupos MODP](https://tools.ietf.org/html/rfc3526)
- **[RFC-5681]** [RFC 5681: Controle de Congestionamento TCP](https://tools.ietf.org/html/rfc5681)
- **[RFC-5869]** [RFC 5869: HKDF](https://tools.ietf.org/html/rfc5869)
- **[RFC-6151]** [RFC 6151: Considerações de Segurança MD5](https://tools.ietf.org/html/rfc6151)
- **[RFC-6298]** [RFC 6298: Timer de Retransmissão TCP](https://tools.ietf.org/html/rfc6298)
- **[RFC-6437]** [RFC 6437: Rótulo de Fluxo IPv6](https://tools.ietf.org/html/rfc6437)
- **[RFC-7539]** [RFC 7539: ChaCha20/Poly1305](https://tools.ietf.org/html/rfc7539)
- **[RFC-7748]** [RFC 7748: Curvas Elípticas para Segurança](https://tools.ietf.org/html/rfc7748)
- **[RFC-7905]** [RFC 7905: Suítes de Cifra ChaCha20-Poly1305 para TLS](https://tools.ietf.org/html/rfc7905)
- **[RFC-9000]** [RFC 9000: Protocolo de Transporte QUIC](https://datatracker.ietf.org/doc/html/rfc9000)
- **[RFC-9001]** [RFC 9001: Usando TLS para Proteger QUIC](https://datatracker.ietf.org/doc/html/rfc9001)
- **[RFC-9002]** [RFC 9002: Detecção de Perdas e Controle de Congestionamento QUIC](https://datatracker.ietf.org/doc/html/rfc9002)
- **[RouterAddress]** [Estrutura RouterAddress](/docs/specs/common-structures#struct-routeraddress)
- **[RouterIdentity]** [Estrutura RouterIdentity](/docs/specs/common-structures#struct-routeridentity)
- **[SigningPublicKey]** [Tipo SigningPublicKey](/docs/specs/common-structures#type-signingpublickey)
- **[SSU]** [Transporte SSU](/docs/transport/ssu)
- **[STS]** [Protocolo Station-to-Station](https://en.wikipedia.org/wiki/Station-to-Station_protocol)
- **[Ticket1112]** [Ticket I2P 1112](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1112)
- **[Ticket1849]** [Ticket I2P 1849](https://i2pgit.org/i2p-hackers/i2p.i2p/-/issues/1849)
- **[WireGuard]** [Protocolo WireGuard](https://www.wireguard.com/papers/wireguard.pdf)
