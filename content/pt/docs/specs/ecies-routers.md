---
title: "Mensagens de Router ECIES-X25519"
description: "Especificação para criptografia de mensagem garlic para routers ECIES usando X25519"
slug: "ecies-routers"
category: "Protocolos"
lastUpdated: "2025-03"
accurateFor: "0.9.65"
---

## Nota

Suportado a partir da versão 0.9.49. Implantação e testes na rede em andamento. Sujeito a pequenas revisões. Consulte [proposta 156](/proposals/156-ecies-routers).

## Visão Geral

Este documento especifica a criptografia de mensagem garlic para routers ECIES, usando primitivas criptográficas introduzidas pelo [ECIES-X25519](/docs/specs/ecies). É uma parte da [proposta 156](/proposals/156-ecies-routers) geral para converter routers de chaves ElGamal para ECIES-X25519. Esta especificação está implementada a partir da versão 0.9.49.

Para uma visão geral de todas as mudanças necessárias para routers ECIES, consulte a [proposta 156](/proposals/156-ecies-routers). Para Mensagens Garlic para destinos ECIES-X25519, consulte [ECIES-X25519](/docs/specs/ecies).

### Primitivos Criptográficos

As primitivas necessárias para implementar esta especificação são:

- AES-256-CBC como em [Criptografia](/docs/specs/cryptography)
- Funções STREAM ChaCha20/Poly1305: ENCRYPT(k, n, plaintext, ad) e DECRYPT(k, n, ciphertext, ad) - como em [NTCP2](/docs/specs/ntcp2), [ECIES-X25519](/docs/specs/ecies), e [RFC-7539](https://tools.ietf.org/html/rfc7539)
- Funções X25519 DH - como em [NTCP2](/docs/specs/ntcp2) e [ECIES-X25519](/docs/specs/ecies)
- HKDF(salt, ikm, info, n) - como em [NTCP2](/docs/specs/ntcp2) e [ECIES-X25519](/docs/specs/ecies)

Outras funções Noise definidas em outro lugar:

- MixHash(d) - como em [NTCP2](/docs/specs/ntcp2) e [ECIES-X25519](/docs/specs/ecies)
- MixKey(d) - como em [NTCP2](/docs/specs/ntcp2) e [ECIES-X25519](/docs/specs/ecies)

## Design

O ECIES Router SKM não precisa de um Ratchet SKM completo conforme especificado em [ECIES](/docs/specs/ecies) para Destinations. Não há requisito para mensagens não-anônimas usando o padrão IK. O modelo de ameaças não requer chaves efêmeras codificadas com Elligator2.

Portanto, o router SKM usará o padrão Noise "N", o mesmo especificado em [Prop152](/proposals/152-ecies-tunnels) para construção de tunnel. Ele usará o mesmo formato de payload especificado em [ECIES](/docs/specs/ecies) para Destinations. O modo de chave estática zero (sem vinculação ou sessão) do IK especificado em [ECIES](/docs/specs/ecies) não será usado.

As respostas às consultas serão criptografadas com uma ratchet tag se solicitado na consulta. Isso está documentado em [Prop154](/proposals/154-ecies-lookups), agora especificado em [I2NP](/docs/specs/i2np).

O design permite que o router tenha um único Gerenciador de Chaves de Sessão ECIES. Não há necessidade de executar Gerenciadores de Chaves de Sessão "chave dupla" como descrito em [ECIES](/docs/specs/ecies) para Destinos. Os routers têm apenas uma chave pública.

Um router ECIES não possui uma chave estática ElGamal. O router ainda precisa de uma implementação ElGamal para construir tunnels através de routers ElGamal e enviar mensagens criptografadas para routers ElGamal.

Um router ECIES PODE requerer um Gerenciador de Chave de Sessão ElGamal parcial para receber mensagens marcadas com ElGamal recebidas como respostas a consultas NetDB de roteadores floodfill pré-0.9.46, pois esses roteadores não têm uma implementação de respostas marcadas com ECIES conforme especificado em [Prop152](/proposals/152-ecies-tunnels). Caso contrário, um router ECIES pode não solicitar uma resposta criptografada de um router floodfill pré-0.9.46.

Isso é opcional. A decisão pode variar em diferentes implementações I2P e pode depender da quantidade da rede que foi atualizada para 0.9.46 ou superior. Nesta data, aproximadamente 85% da rede está na versão 0.9.46 ou superior.

### Framework de Protocolo Noise

Esta especificação fornece os requisitos baseados no [Noise Protocol Framework](https://noiseprotocol.org/noise.html) (Revisão 34, 2018-07-11). Na terminologia do Noise, Alice é o iniciador, e Bob é o respondedor.

É baseado no protocolo Noise Noise_N_25519_ChaChaPoly_SHA256. Este protocolo Noise usa as seguintes primitivas:

- **Padrão de Handshake Unidirecional: N** - Alice não transmite sua chave estática para Bob (N)
- **Função DH: X25519** - X25519 DH com um comprimento de chave de 32 bytes conforme especificado em [RFC-7748](https://tools.ietf.org/html/rfc7748).
- **Função de Cifra: ChaChaPoly** - AEAD_CHACHA20_POLY1305 conforme especificado em [RFC-7539](https://tools.ietf.org/html/rfc7539) seção 2.8. Nonce de 12 bytes, com os primeiros 4 bytes definidos como zero. Idêntico ao usado em [NTCP2](/docs/specs/ntcp2).
- **Função Hash: SHA256** - Hash padrão de 32 bytes, já usado extensivamente no I2P.

### Padrões de Handshake

Os handshakes usam padrões de handshake [Noise](https://noiseprotocol.org/noise.html).

O seguinte mapeamento de letras é usado:

- e = chave efêmera de uso único
- s = chave estática
- p = carga útil da mensagem

O pedido de construção é idêntico ao padrão Noise N. Isto também é idêntico à primeira mensagem (Pedido de Sessão) no padrão XK usado em [NTCP2](/docs/specs/ntcp2).

```
<- s
  ...
  e es p ->
```
### Criptografia de mensagens

As mensagens são criadas e criptografadas assimetricamente para o router de destino. Esta criptografia assimétrica das mensagens é atualmente ElGamal conforme definido em [Cryptography](/docs/specs/cryptography) e contém um checksum SHA-256. Este design não é forward-secret (não oferece sigilo futuro).

O design ECIES usa o padrão Noise unidirecional "N" com DH efêmero-estático ECIES-X25519, com um HKDF, e AEAD ChaCha20/Poly1305 para sigilo progressivo, integridade e autenticação. Alice é a remetente anônima da mensagem, um router ou destino. O router ECIES de destino é Bob.

### Criptografia de resposta

As respostas não fazem parte deste protocolo, pois Alice é anônima. As chaves de resposta, se houver, são agrupadas na mensagem de solicitação. Consulte a [especificação I2NP](/docs/specs/i2np) para Mensagens de Consulta de Banco de Dados.

As respostas às mensagens Database Lookup são mensagens Database Store ou Database Search Reply. Elas são criptografadas como mensagens Existing Session com a chave de resposta de 32 bytes e a tag de resposta de 8 bytes conforme especificado em [I2NP](/docs/specs/i2np) e [Prop154](/proposals/154-ecies-lookups).

Não há respostas explícitas para mensagens Database Store. O remetente pode agrupar sua própria resposta como uma Garlic Message para si mesmo, contendo uma mensagem Delivery Status.

## Especificação

X25519: Veja [ECIES](/docs/specs/ecies).

Identidade do Router e Certificado de Chave: Consulte [Estruturas Comuns](/docs/specs/common-structures).

### Criptografia de Solicitação

A criptografia da solicitação é a mesma especificada em [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) e [Prop152](/proposals/152-ecies-tunnels), usando o padrão Noise "N".

As respostas às consultas serão criptografadas com uma ratchet tag se solicitado na consulta. As mensagens de solicitação de Database Lookup contêm a chave de resposta de 32 bytes e a tag de resposta de 8 bytes conforme especificado em [I2NP](/docs/specs/i2np) e [Prop154](/proposals/154-ecies-lookups). A chave e a tag são usadas para criptografar a resposta.

Tag sets não são criados. O esquema de chave estática zero especificado em ECIES-X25519-AEAD-Ratchet [Prop144](/proposals/144-ecies-x25519-aead-ratchet) e [ECIES](/docs/specs/ecies) não será usado. Chaves efêmeras não serão codificadas com Elligator2.

Geralmente, essas serão mensagens New Session e serão enviadas com uma chave estática zero (sem vinculação ou sessão), pois o remetente da mensagem é anônimo.

#### KDF para ck e h iniciais

Este é o [Noise](https://noiseprotocol.org/noise.html) padrão para o padrão "N" com um nome de protocolo padrão. Este é o mesmo especificado em [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) e [Prop152](/proposals/152-ecies-tunnels) para mensagens de construção de tunnel.

```
This is the "e" message pattern:

  // Define protocol_name.
  Set protocol_name = "Noise_N_25519_ChaChaPoly_SHA256"
  (31 bytes, US-ASCII encoded, no NULL termination).

  // Define Hash h = 32 bytes
  // Pad to 32 bytes. Do NOT hash it, because it is not more than 32 bytes.
  h = protocol_name || 0

  Define ck = 32 byte chaining key. Copy the h data to ck.
  Set chainKey = h

  // MixHash(null prologue)
  h = SHA256(h);

  // up until here, can all be precalculated by all routers.
```
#### KDF para Mensagem

Os criadores de mensagens geram um par de chaves X25519 efêmero para cada mensagem. As chaves efêmeras devem ser únicas por mensagem. Isso é o mesmo especificado em [Tunnel-Creation-ECIES](/docs/specs/tunnel-creation-ecies) e [Prop152](/proposals/152-ecies-tunnels) para mensagens de construção de tunnel.

```
  // Target router's X25519 static keypair (hesk, hepk) from the Router Identity
  hesk = GENERATE_PRIVATE()
  hepk = DERIVE_PUBLIC(hesk)

  // MixHash(hepk)
  // || below means append
  h = SHA256(h || hepk);

  // up until here, can all be precalculated by each router
  // for all incoming messages

  // Sender generates an X25519 ephemeral keypair
  sesk = GENERATE_PRIVATE()
  sepk = DERIVE_PUBLIC(sesk)

  // MixHash(sepk)
  h = SHA256(h || sepk);

  End of "e" message pattern.

  This is the "es" message pattern:

  // Noise es
  // Sender performs an X25519 DH with receiver's static public key.
  // The target router
  // extracts the sender's ephemeral key preceding the encrypted record.
  sharedSecret = DH(sesk, hepk) = DH(hesk, sepk)

  // MixKey(DH())
  //[chainKey, k] = MixKey(sharedSecret)
  // ChaChaPoly parameters to encrypt/decrypt
  keydata = HKDF(chainKey, sharedSecret, "", 64)
  // Chain key is not used
  //chainKey = keydata[0:31]

  // AEAD parameters
  k = keydata[32:63]
  n = 0
  plaintext = 464 byte build request record
  ad = h
  ciphertext = ENCRYPT(k, n, plaintext, ad)

  End of "es" message pattern.

  // MixHash(ciphertext) is not required
  //h = SHA256(h || ciphertext)
```
#### Carga útil

O payload é o mesmo formato de bloco definido em [ECIES](/docs/specs/ecies) e [Prop144](/proposals/144-ecies-x25519-aead-ratchet). Todas as mensagens devem conter um bloco DateTime para prevenção de replay.

## Notas de Implementação

- Routers mais antigos não verificam o tipo de criptografia do router e enviarão mensagens criptografadas com ElGamal. Alguns routers recentes têm bugs e enviarão vários tipos de mensagens malformadas. Os implementadores devem detectar e rejeitar esses registros antes da operação DH, se possível, para reduzir o uso da CPU.

## Referências

- [Estruturas Comuns](/docs/specs/common-structures)
- [Criptografia](/docs/specs/cryptography)
- [ECIES](/docs/specs/ecies)
- [I2NP](/docs/specs/i2np)
- [Framework de Protocolo Noise](https://noiseprotocol.org/noise.html)
- [NTCP2](/docs/specs/ntcp2)
- [Prop144](/proposals/144-ecies-x25519-aead-ratchet)
- [Prop152](/proposals/152-ecies-tunnels)
- [Prop154](/proposals/154-ecies-lookups)
- [Prop156](/proposals/156-ecies-routers)
- [RFC-7539](https://tools.ietf.org/html/rfc7539)
- [RFC-7748](https://tools.ietf.org/html/rfc7748)
- [Criação de Tunnel-ECIES](/docs/specs/tunnel-creation-ecies)
