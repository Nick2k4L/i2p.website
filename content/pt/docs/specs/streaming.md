---
title: "Especificação do Protocolo de Streaming"
description: "Especificação para o protocolo de streaming I2P fornecendo transporte confiável similar ao TCP"
slug: "streaming"
category: "Protocolos"
lastUpdated: "2023-10"
accurateFor: "0.9.59"
---

## Visão Geral

Veja [Streaming Library](/docs/api/streaming) para uma visão geral do protocolo Streaming.

## Versões de Protocolo

O protocolo streaming não inclui um campo de versão. As versões listadas abaixo são para o Java I2P. As implementações e suporte real de criptografia podem variar. Não há maneira de determinar se a extremidade remota suporta qualquer versão ou funcionalidade específica. A tabela abaixo é para orientação geral quanto às datas de lançamento para várias funcionalidades.

Os recursos listados abaixo são para o protocolo em si. Várias opções de configuração estão documentadas na [Biblioteca de Streaming](/docs/api/streaming) juntamente com a versão Java I2P na qual foram implementadas.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Router Version</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Streaming Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.58</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Bob's hash in NACKs field of SYN packet</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.39</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE option</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">I2CP protocol number enforced</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED no longer required in RESET</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.18</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PINGs and PONGs may include a payload</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">EdDSA Ed25519 sig type</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECDSA P-256, P-384, and P-521 sig types</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.9.11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Variable-length signatures</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.7.1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Protocol numbers defined in I2CP</td>
    </tr>
  </tbody>
</table>
## Especificação do Protocolo

### Formato de Pacote

O formato de um único pacote no protocolo de streaming é mostrado abaixo. O tamanho mínimo do cabeçalho, sem NACKs ou dados de opção, é de 22 bytes.

Não há campo de comprimento no protocolo de streaming. O enquadramento é fornecido pelas camadas inferiores - I2CP e I2NP.

```
+----+----+----+----+----+----+----+----+
| send Stream ID    | rcv Stream ID     |
+----+----+----+----+----+----+----+----+
| sequence  Num     | ack Through       |
+----+----+----+----+----+----+----+----+
| nc |  nc*4 bytes of NACKs (optional)
+----+----+----+----+----+----+----+----+
     | rd |  flags  | opt size| opt data
+----+----+----+----+----+----+----+----+
   ...  (optional, see below)           |
+----+----+----+----+----+----+----+----+
|   payload ...
+----+----+----+-//
```
**sendStreamId** :: 4 byte [Integer](/docs/specs/common-structures#integer) : Número aleatório selecionado pelo destinatário do pacote antes de enviar o primeiro pacote de resposta SYN e constante durante toda a vida da conexão, maior que zero. 0 na mensagem SYN enviada pelo originador da conexão, e nas mensagens subsequentes, até que uma resposta SYN seja recebida, contendo o stream ID do peer.

**receiveStreamId** :: 4 bytes [Integer](/docs/specs/common-structures#integer) : Número aleatório selecionado pelo originador do pacote antes de enviar o primeiro pacote SYN e constante durante toda a vida da conexão, maior que zero. Pode ser 0 se desconhecido, por exemplo em um pacote RESET.

**sequenceNum** :: 4 byte [Integer](/docs/specs/common-structures#integer) : A sequência para esta mensagem, começando em 0 na mensagem SYN, e incrementada em 1 em cada mensagem exceto para ACKs simples e retransmissões. Se o sequenceNum for 0 e a flag SYN não estiver definida, este é um pacote ACK simples que não deve ser confirmado com ACK.

**ackThrough** :: 4 byte [Integer](/docs/specs/common-structures#integer) : O maior número de sequência de pacote que foi recebido no receiveStreamId. Este campo é ignorado no pacote de conexão inicial (onde receiveStreamId é o id desconhecido) ou se a flag NO_ACK estiver definida. Todos os pacotes até e incluindo este número de sequência são confirmados (ACKed), EXCETO aqueles listados em NACKs abaixo.

**Contagem NACK** :: 1 byte [Integer](/docs/specs/common-structures#integer) : O número de NACKs de 4 bytes no próximo campo, ou 8 quando usado junto com SYNCHRONIZE para prevenção de replay a partir da versão 0.9.58; veja abaixo.

**NACKs** :: nc * 4 byte [Integer](/docs/specs/common-structures#integer)s : Números de sequência menores que ackThrough que ainda não foram recebidos. Dois NACKs de um pacote é uma solicitação para uma 'retransmissão rápida' desse pacote. Também usado juntamente com SYNCHRONIZE para prevenção de replay a partir da versão 0.9.58; veja abaixo.

**resendDelay** :: 1 byte [Integer](/docs/specs/common-structures#integer) : Por quanto tempo o criador deste pacote vai aguardar antes de reenviar este pacote (se ainda não foi confirmado com ACK). O valor é em segundos desde que o pacote foi criado. Atualmente ignorado no recebimento.

**flags** :: valor de 2 bytes : Veja abaixo.

**option size** :: 2 byte [Integer](/docs/specs/common-structures#integer) : O número de bytes no próximo campo

**dados da opção** :: 0 ou mais bytes : Conforme especificado pelas flags. Veja abaixo.

**payload** :: tamanho restante do pacote

### Campos de Flags e Dados de Opção

O campo flags acima especifica alguns metadados sobre o pacote e, por sua vez, pode exigir que certos dados adicionais sejam incluídos. As flags são as seguintes. Quaisquer estruturas de dados especificadas devem ser adicionadas à área de opções na ordem fornecida.

Ordem dos bits: 15....0 (15 é MSB)

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Flag</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Order</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option Data</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SYNCHRONIZE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP SYN. Set in the initial packet and in the first response. FROM_INCLUDED and SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">CLOSE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Similar to TCP FIN. If the response to a SYNCHRONIZE fits in a single message, the response will contain both SYNCHRONIZE and CLOSE. SIGNATURE_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">RESET</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Abnormal close. SIGNATURE_INCLUDED must also be set. Prior to release 0.9.20, due to a bug, FROM_INCLUDED must also be set.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#signature">Signature</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, CLOSE, and RESET, where it is required, and with ECHO, where it is required for a ping. The signature uses the Destination's <a href="/docs/specs/common-structures#signingprivatekey">SigningPrivateKey</a> to sign the entire header and payload with the space in the option data field for the signature being set to all zeroes. Prior to release 0.9.11, the signature was always 40 bytes. As of release 0.9.11, the signature may be variable-length, see below for details.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">SIGNATURE_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused. Requests every packet in the other direction to have SIGNATURE_INCLUDED</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">FROM_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">387+ byte <a href="/docs/specs/common-structures#destination">Destination</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Currently sent only with SYNCHRONIZE, where it is required, and with ECHO, where it is required for a ping. Prior to release 0.9.20, due to a bug, must also be sent with RESET.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DELAY_REQUESTED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Optional delay. How many milliseconds the sender of this packet wants the recipient to wait before sending any more data. A value greater than 60000 indicates choking. A value of 0 requests an immediate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">7</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">MAX_PACKET_SIZE_INCLUDED</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 byte <a href="/docs/specs/common-structures#integer">Integer</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum length of the payload. Send with SYNCHRONIZE.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">PROFILE_INTERACTIVE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused or ignored; the interactive profile is unimplemented.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">ECHO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Unused except by ping programs. If set, most other options are ignored. See the <a href="/docs/api/streaming">streaming docs</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">10</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">NO_ACK</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">--</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">This flag simply tells the recipient to ignore the ackThrough field in the header. Currently set in the initial SYN packet, otherwise the ackThrough field is always valid. Note that this does not save any space, the ackThrough field is before the flags and is always present.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">11</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">OFFLINE_SIGNATURE</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">variable length <a href="/docs/specs/common-structures#offlinesignature">OfflineSig</a></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Contains the offline signature section from LS2. See proposal 123 and the common structures specification. FROM_INCLUDED must also be set. Contains an OfflineSig: 1) Expires timestamp (4 bytes, seconds since epoch, rolls over in 2106) 2) Transient sig type (2 bytes) 3) Transient <a href="/docs/specs/common-structures#signingpublickey">SigningPublicKey</a> (length as implied by sig type) 4) <a href="/docs/specs/common-structures#signature">Signature</a> of expires timestamp, transient sig type, and public key, by the destination public key. Length of sig as implied by the destination public key sig type.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12-15</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">unused</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Set to zero for compatibility with future uses.</td>
    </tr>
  </tbody>
</table>
### Notas sobre Assinatura de Comprimento Variável

Antes da versão 0.9.11, a assinatura no campo de opção sempre tinha 40 bytes.

A partir da versão 0.9.11, a assinatura tem comprimento variável. O tipo e comprimento da Signature são inferidos do tipo de chave usado na opção FROM_INCLUDED e da documentação da [Signature](/docs/specs/common-structures#signature).

A partir da versão 0.9.39, a opção OFFLINE_SIGNATURE é suportada. Se esta opção estiver presente, a [SigningPublicKey](/docs/specs/common-structures#signingpublickey) transitória é usada para verificar qualquer pacote assinado, e o comprimento e tipo da assinatura são inferidos da SigningPublicKey transitória na opção.

- Quando um pacote contém tanto FROM_INCLUDED quanto SIGNATURE_INCLUDED (como em SYNCHRONIZE), a inferência pode ser feita diretamente.

- Quando um pacote não contém FROM_INCLUDED, a inferência deve ser feita a partir de um pacote SYNCHRONIZE anterior.

- Quando um pacote não contém FROM_INCLUDED, e não houve pacote SYNCHRONIZE anterior (por exemplo, um pacote CLOSE ou RESET isolado), a inferência pode ser feita a partir do comprimento das opções restantes (já que SIGNATURE_INCLUDED é a última opção), mas o pacote provavelmente será descartado mesmo assim, pois não há FROM disponível para validar a assinatura. Se mais campos de opção forem definidos no futuro, eles devem ser considerados.

### Prevenção de Replay

Para impedir que Bob use um ataque de replay armazenando um pacote SYNCHRONIZE assinado válido recebido de Alice e posteriormente enviando-o para uma vítima Charlie, Alice deve incluir o hash de destino de Bob no pacote SYNCHRONIZE da seguinte forma:

```
Set NACK count field to 8
Set the NACKs field to Bob's 32-byte destination hash
```
Ao receber um SYNCHRONIZE, se o campo de contagem NACK for 8, Bob deve interpretar o campo NACKs como um hash de destino de 32 bytes e deve verificar se ele corresponde ao seu hash de destino. Ele também deve verificar a assinatura do pacote como de costume, pois ela cobre todo o pacote incluindo os campos de contagem NACK e NACKs. Se a contagem NACK for 8 e o campo NACKs não corresponder, Bob deve descartar o pacote.

Isso é obrigatório para as versões 0.9.58 e superiores. Isso é compatível com versões mais antigas, porque NACKs não são esperados em um pacote SYNCHRONIZE. Os destinations não sabem e não podem saber qual versão está sendo executada na outra extremidade.

Não é necessária nenhuma alteração para o pacote SYNCHRONIZE ACK enviado de Bob para Alice; não inclua NACKs nesse pacote.

## Referências

- **[Destination]** [Destination](/docs/specs/common-structures#destination)
- **[Integer]** [Integer](/docs/specs/common-structures#integer)
- **[OfflineSig]** [OfflineSignature](/docs/specs/common-structures#offlinesignature)
- **[Signature]** [Signature](/docs/specs/common-structures#signature)
- **[SigningPrivateKey]** [SigningPrivateKey](/docs/specs/common-structures#signingprivatekey)
- **[SigningPublicKey]** [SigningPublicKey](/docs/specs/common-structures#signingpublickey)
- **[STREAMING]** [Biblioteca de Streaming](/docs/api/streaming)
