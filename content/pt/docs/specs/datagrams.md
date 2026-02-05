---
title: "Especificação de Datagrama"
description: "Especificação dos formatos de mensagem de datagrama I2P incluindo tipos raw, repliable e authenticated"
slug: "datagrams"
category: "Protocolos"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

## Visão Geral

Veja a [documentação da API de Datagramas](/docs/api/datagrams/) para uma visão geral da API de Datagramas.

Os seguintes tipos são definidos. Os números de protocolo padrão são listados, no entanto quaisquer outros números de protocolo podem ser usados além do número de protocolo de streaming (6), específico da aplicação.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Type</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Protocol</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Repliable?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Authenticated?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:center; background:var(--color-bg-secondary);">Replay Prevention?</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">As Of</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Raw</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">17</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">19</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Datagram3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.66</td>
    </tr>
  </tbody>
</table>
O suporte para Datagram2 e Datagram3 em várias implementações de router e biblioteca está por definir. Consulte a documentação dessas implementações.

### Identificação de Tipo de Datagrama

Os quatro tipos de datagrama não compartilham um cabeçalho comum com a versão do protocolo no mesmo lugar. Os pacotes não podem ser identificados por tipo baseado em seu conteúdo. Ao usar múltiplos tipos na mesma sessão, ou um único tipo junto com streaming, as aplicações devem usar números de protocolo e/ou portas I2CP/SAM para rotear pacotes recebidos para o local correto. Usar números de protocolo padrão facilitará isso. Deixar o número de protocolo não definido (0 ou PROTO_ANY), mesmo para uma aplicação somente de datagrama, não é recomendado pois aumenta a chance de erros de roteamento e torna upgrades para uma aplicação multi-protocolo mais difíceis. Os campos de versão em Datagram 2 e 3 são fornecidos apenas como uma verificação adicional para erros de roteamento e mudanças futuras.

### Design de Aplicação

Todos os usos de datagramas são específicos da aplicação.

Como os datagramas autenticados carregam uma sobrecarga substancial, uma aplicação típica usa tanto datagramas autenticados quanto não autenticados. Um design típico é enviar um único datagrama autenticado contendo um token do cliente para o servidor. O servidor responde com um datagrama não autenticado contendo o mesmo token. Qualquer comunicação subsequente, antes do timeout do token, usa datagramas brutos.

As aplicações enviam e recebem datagramas usando números de protocolo e porta através da API [I2CP](/docs/specs/i2cp/) ou [SAMv3](/docs/api/samv3/).

Os datagramas são, obviamente, não confiáveis. As aplicações devem ser projetadas para entrega não confiável. Dentro do I2P, a entrega é confiável hop-a-hop se o próximo hop for alcançável, já que os transportes NTCP2 e SSU2 fornecem confiabilidade. No entanto, a entrega fim-a-fim não é confiável, pois as mensagens I2NP podem ser descartadas em qualquer hop devido a limites de fila, expirações, timeouts, limites de largura de banda ou próximos hops inacessíveis.

### Tamanho do Datagrama

O limite nominal de tamanho para mensagens I2NP, incluindo datagramas, é 64 KB. A sobrecarga de mensagens garlic e tunnel reduz isso um pouco.

No entanto, todas as mensagens I2NP devem ser fragmentadas em mensagens de tunnel de 1 KB. A probabilidade de descarte de uma mensagem I2NP de n KB é a função exponencial da probabilidade de descarte de uma única mensagem de tunnel, p ** n. Como a fragmentação resulta em uma rajada de mensagens de tunnel, a probabilidade real de descarte é muito maior do que a função exponencial sugeriria, devido aos limites de fila e ao gerenciamento ativo de filas (AQM, CoDel ou similar) nas implementações de router.

O tamanho máximo típico recomendado para garantir entrega confiável é de alguns KB, ou no máximo 10 KB. Com análise cuidadosa dos tamanhos de overhead em todas as camadas de protocolo (exceto transporte), os desenvolvedores devem definir um tamanho máximo de payload que se ajuste precisamente em uma, duas ou três mensagens de tunnel. Isso maximizará a eficiência e confiabilidade. O overhead em várias camadas inclui o cabeçalho gzip, cabeçalho I2NP, cabeçalho de mensagem garlic, garlic encryption, cabeçalho de mensagem de tunnel, cabeçalhos de fragmentação de mensagem de tunnel, e outros. Veja cálculos de MTU de streaming na [Proposta 144](/proposals/144-ecies-x25519-aead-ratchet/) e ConnectionOptions.java no código-fonte Java I2P para exemplos.

### Considerações sobre SAM

As aplicações enviam e recebem datagramas usando números de protocolo e porta através da API I2CP ou SAM. Especificar números de protocolo e porta via SAM requer SAM v3.2 ou superior. Usar tanto datagramas quanto streaming (UDP e TCP) na mesma sessão SAM (tunnels) requer SAM v3.3 ou superior. Usar múltiplos tipos de datagrama na mesma sessão SAM (tunnels) requer SAM v3.3 ou superior. SAM v3.3 é suportado apenas pelo router I2P Java neste momento.

O suporte SAM para Datagram2 e Datagram3 em várias implementações de router e biblioteca ainda está por ser definido. Consulte a documentação dessas implementações.

Note que tamanhos acima de um MTU de rede típico de 1500 bytes impedirão que aplicações SAM transportem pacotes não fragmentados de/para o servidor SAM, se a aplicação e o servidor estiverem em computadores separados. Tipicamente, este não é o caso, ambos estão no localhost, onde o MTU é 65536 ou superior. Se uma aplicação SAM for esperada estar separada em um computador diferente do servidor, a carga útil máxima para um datagrama respondível é ligeiramente inferior a 1 KB.

### Considerações PQ

Se a porção MLDSA da [Proposta 169](/proposals/169-pq-crypto/) Post-Quantum for implementada, a sobrecarga aumentará substancialmente. O tamanho de um destination + signature aumentará de 391 + 64 = 455 bytes para um mínimo de 3739 para MLDSA44 e um máximo de 7226 para MLDSA87. Os efeitos práticos disso devem ser determinados. Datagram3, com autenticação fornecida pelo router, pode ser uma solução.

## Datagramas Raw (Não Respondíveis) {#raw}

Datagramas não-respondíveis não têm endereço 'de' e não são autenticados. Também são chamados de datagramas "brutos". Estritamente falando, não são "datagramas" de forma alguma, são apenas dados brutos. Não são tratados pela API de datagramas. No entanto, o SAM e as classes I2PTunnel suportam "datagramas brutos".

O número de protocolo I2CP padrão para datagramas brutos é PROTO_DATAGRAM_RAW (18).

O formato não é especificado aqui, é definido pela aplicação. Para completude, incluímos uma imagem do formato abaixo.

### Formato

```
+----+----+----+----+----//
| payload...
+----+----+----+----+----//

length: 0 - about 64 KB (see notes)
```
### Notas

O comprimento prático é limitado tanto pela sobrecarga em várias camadas quanto pela confiabilidade.

## Datagram1 (Replicável) {#repliable}

Datagramas com resposta contêm um endereço 'from' e uma assinatura. Estes adicionam pelo menos 427 bytes de overhead.

O número de protocolo I2CP padrão para datagramas que podem ser respondidos é PROTO_DATAGRAM (17).

### Formato

```
+----+----+----+----+----+----+----+----+
| from                                  |
+                                       +
|                                       |
~                                       ~
~                                       ~
|                                       |
+                                       +
|                                       |
|                                       |
+----+----+----+----+----+----+----+----+
| signature                             |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+                                       +
|                                       |
+----+----+----+----+----+----+----+----+
| payload...
+----+----+----+----//

from :: a Destination
        length: 387+ bytes
        The originator and signer of the datagram

signature :: a Signature
             Signature type must match the signing public key type of $from
             length: 40+ bytes, as implied by the Signature type.
             For the default DSA_SHA1 key type:
                The DSA Signature of the SHA-256 hash of the payload.
             For other key types:
                The Signature of the payload.
             The signature may be verified by the signing public key of $from

payload :: The data
           Length: 0 to about 63 KB (see notes)

Total length: Payload length + 427+
```
### Notas

- O comprimento prático é limitado tanto pela sobrecarga em várias camadas quanto pela confiabilidade.
- Consulte as notas importantes sobre a confiabilidade de datagramas grandes na [documentação da API de Datagramas](/docs/api/datagrams/). Para melhores resultados, limite a carga útil a cerca de 10 KB ou menos.
- Assinaturas para tipos diferentes de DSA_SHA1 foram redefinidas na versão 0.9.14.
- O formato não suporta a inclusão de um bloco de assinatura offline para LS2 (proposta 123). Um novo protocolo com flags deve ser definido para isso.

## Datagram2 {#datagram2}

O formato Datagram2 é conforme especificado na [Proposta 163](/proposals/163-datagram2/). O número de protocolo I2CP para Datagram2 é 19.

Datagram2 é destinado como uma substituição para Datagram1. Ele adiciona as seguintes funcionalidades ao Datagram1:

- Prevenção de replay
- Suporte a assinatura offline
- Campos de flags e opções para extensibilidade

Note que o algoritmo de cálculo de assinatura para Datagram2 é substancialmente diferente do que para Datagram1.

### Formato

```
+----+----+----+----+----+----+----+----+
|                                       |
~            from                       ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~     offline_signature (optional)      ~
~   expires, sigtype, pubkey, offsig    ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|                                       |
~            signature                  ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

from :: a Destination
        length: 387+ bytes
        The originator and (unless offline signed) signer of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x02 (0 0 1 0)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bit 5: If 0, no offline sig; if 1, offline signed
         Bits 15-6: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

offline_signature ::
             If flag indicates offline keys, the offline signature section,
             as specified in the Common Structures Specification,
             with the following 4 fields. Length: varies by online and offline
             sig types, typically 102 bytes for Ed25519
             This section can, and should, be generated offline.

  expires :: Expires timestamp
             (4 bytes, big endian, seconds since epoch, rolls over in 2106)

  sigtype :: Transient sig type (2 bytes, big endian)

  pubkey :: Transient signing public key (length as implied by sig type),
            typically 32 bytes for Ed25519 sig type.

  offsig :: a Signature
            Signature of expires timestamp, transient sig type,
            and public key, by the destination public key,
            length: 40+ bytes, as implied by the Signature type, typically
            64 bytes for Ed25519 sig type.

payload :: The data
           Length: 0 to about 61 KB (see notes)

signature :: a Signature
             Signature type must match the signing public key type of $from
             (if no offline signature) or the transient sigtype
             (if offline signed)
             length: 40+ bytes, as implied by the Signature type, typically
             64 bytes for Ed25519 sig type.
             The Signature of the payload and other fields as specified below.
             The signature is verified by the signing public key of $from
             (if no offline signature) or the transient pubkey
             (if offline signed)
```
Comprimento total: mínimo 433 + comprimento da carga útil; comprimento típico para remetentes X25519 e sem assinaturas offline: 457 + comprimento da carga útil. Note que a mensagem será tipicamente comprimida com gzip na camada I2CP, o que resultará em economias significativas se o destino de origem for comprimível.

Nota: O formato de assinatura offline é o mesmo que na [Especificação de Estruturas Comuns](/docs/specs/common-structures/) e [Especificação de Streaming](/docs/specs/streaming/).

### Assinaturas

A assinatura abrange os seguintes campos:

- Preâmbulo: O hash de 32 bytes do destino alvo (não incluído no datagrama)
- flags
- opções (se presente)
- offline_signature (se presente)
- payload

No datagrama de resposta, para o tipo de chave DSA_SHA1, a assinatura era sobre o hash SHA-256 do payload, não sobre o payload em si; aqui, a assinatura é sempre sobre os campos acima (NÃO o hash), independentemente do tipo de chave.

### Verificação ToHash

Os receptores devem verificar a assinatura (usando seu hash de destino) e descartar o datagrama em caso de falha, para prevenção de replay.

## Datagram3 {#datagram3}

O formato Datagram3 é conforme especificado na [Proposta 163](/proposals/163-datagram2/). O número de protocolo I2CP para Datagram3 é 20.

Datagram3 é destinado como uma versão aprimorada dos datagramas brutos. Adiciona as seguintes funcionalidades aos datagramas brutos:

- Replicabilidade
- Campos de flags e opções para extensibilidade

Datagram3 NÃO é autenticado. Em uma proposta futura, a autenticação pode ser fornecida pela camada ratchet do router, e o status de autenticação seria passado para o cliente.

### Formato

```
+----+----+----+----+----+----+----+----+
|                                       |
~            fromhash                   ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+
|  flags  |     options (optional)      |
+----+----+                             +
~                                       ~
~                                       ~
+----+----+----+----+----+----+----+----+
|                                       |
~            payload                    ~
~                                       ~
|                                       |
+----+----+----+----+----+----+----+----+

fromhash :: a Hash
            length: 32 bytes
            The originator of the datagram

flags :: (2 bytes)
         Bit order: 15 14 ... 3 2 1 0
         Bits 3-0: Version: 0x03 (0 0 1 1)
         Bit 4: If 0, no options; if 1, options mapping is included
         Bits 15-5: unused, set to 0 for compatibility with future uses

options :: (2+ bytes if present)
         If flag indicates options are present, a Mapping
         containing arbitrary text options

payload :: The data
           Length: 0 to about 61 KB (see notes)
```
Comprimento total: mínimo 34 + comprimento da carga útil.

## Referências

- [Common](/docs/specs/common-structures/) - Especificação de Estruturas Comuns
- [DATAGRAMS](/docs/api/datagrams/) - Visão Geral da API de Datagramas
- [I2CP](/docs/specs/i2cp/) - Especificação I2CP
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet/) - Proposta ECIES-X25519-AEAD-Ratchet
- [Prop163](/proposals/163-datagram2/) - Proposta Datagram2 e Datagram3
- [Prop169](/proposals/169-pq-crypto/) - Proposta de Criptografia Pós-Quântica
- [SAMv3](/docs/api/samv3/) - Especificação SAM v3
- [Streaming](/docs/specs/streaming/) - Especificação de Streaming
- [TRANSPORT](/docs/overview/transport/) - Visão Geral de Transporte
- [TUNMSG](/docs/specs/tunnel-message/#notes) - Especificação de Mensagem de Tunnel
