---
title: "Protocolos Criptográficos Pós-Quânticos"
aliases: 
number: "169"
author: "zzz, orignal, drzed, eyedeekay"
created: "2025-01-21"
lastupdated: "2026-02-26"
status: "Abrir"
thread: "http://zzz.i2p/topics/3294"
target: "0.9.80"
toc: true
---

### Status

| Protocolo / Funcionalidade | Status |
|-----------------------------|--------|
| Ratchet | Completo no Java I2P e i2pd |
| NTCP2 | Beta Q1 2026 |
| SSU2 | Implementação começando em breve, Beta Q23 2026 |
| MLDSA SigTypes | Baixa prioridade, provavelmente 2027+ |
## Visão Geral

Embora a pesquisa e competição por criptografia pós-quântica (PQ) adequada tenham prosseguido por uma década, as escolhas não se tornaram claras até recentemente.

Começamos a analisar as implicações da criptografia PQ em 2022 [zzz.i2p](http://zzz.i2p/topics/3294).

Os padrões TLS adicionaram suporte à criptografia híbrida nos últimos dois anos e agora é usado para uma porção significativa do tráfego criptografado na internet devido ao suporte no Chrome e Firefox [Cloudflare](https://blog.cloudflare.com/pq-2024/).

O NIST recentemente finalizou e publicou os algoritmos recomendados para criptografia pós-quântica [NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards). Várias bibliotecas de criptografia comuns agora suportam os padrões NIST ou estarão lançando suporte em um futuro próximo.

Tanto a [Cloudflare](https://blog.cloudflare.com/pq-2024/) quanto o [NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) recomendam que a migração comece imediatamente. Veja também o FAQ PQ de 2022 da NSA [NSA](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF). O I2P deve ser líder em segurança e criptografia. Agora é o momento de implementar os algoritmos recomendados. Usando nosso sistema flexível de tipos de criptografia e tipos de assinatura, adicionaremos tipos para criptografia híbrida, e para assinaturas PQ e híbridas.

## Objetivos

- Selecionar algoritmos resistentes a PQ
- Adicionar algoritmos apenas PQ e híbridos aos protocolos I2P quando apropriado
- Definir múltiplas variantes
- Selecionar as melhores variantes após implementação, teste, análise e pesquisa
- Adicionar suporte incrementalmente e com compatibilidade retroativa

## Não-Objetivos

- Não altere protocolos de criptografia unidirecional (Noise N)
- Não abandone o SHA256, não está ameaçado a curto prazo pela computação quântica
- Não selecione as variantes preferidas finais neste momento

## Modelo de Ameaça

- Routers no OBEP ou IBGW, possivelmente em conluio,
  armazenando mensagens garlic para descriptografia posterior (forward secrecy)
- Observadores de rede
  armazenando mensagens de transporte para descriptografia posterior (forward secrecy)
- Participantes da rede falsificando assinaturas para RI, LS, streaming, datagramas,
  ou outras estruturas

## Protocolos Afetados

Iremos modificar os seguintes protocolos, aproximadamente na ordem de desenvolvimento. A implementação geral provavelmente ocorrerá do final de 2025 até meados de 2027. Consulte a seção Prioridades e Implementação abaixo para detalhes.

| Protocolo / Funcionalidade | Status |
|--------------------|--------|
| Hybrid MLKEM Ratchet e LS | Aprovado 2025-06; beta 2025-08; lançamento 2025-11 |
| Hybrid MLKEM NTCP2 | Testado na rede ativa, Aprovado 2026-02; meta beta 2026-05; meta de lançamento 2026-08 |
| Hybrid MLKEM SSU2 | Aprovado 2026-02; meta beta 2026-08; meta de lançamento 2026-11 |
| MLDSA SigTypes 12-14 | Proposta está estável mas pode não ser finalizada até 2027 |
| MLDSA Dests | Testado na rede ativa, requer atualização da rede para suporte floodfill |
| Hybrid SigTypes 15-17 | Preliminar |
| Hybrid Dests | |
## Design

Apoiaremos os padrões NIST FIPS 203 e 204 [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) que são baseados em, mas NÃO compatíveis com, CRYSTALS-Kyber e CRYSTALS-Dilithium (versões 3.1, 3 e anteriores).

### Troca de Chaves

Iremos suportar troca de chaves híbrida nos seguintes protocolos:

| Proto   | Tipo Noise | Suporta apenas PQ? | Suporta Híbrido? |
|---------|------------|-------------------|------------------|
| NTCP2   | XK         | não               | sim              |
| SSU2    | XK         | não               | sim              |
| Ratchet | IK         | não               | sim              |
| TBM     | N          | não               | não              |
| NetDB   | N          | não               | não              |
PQ KEM fornece apenas chaves efêmeras e não suporta diretamente handshakes de chave estática como Noise XK e IK.

O Noise N não usa uma troca de chaves bidirecional e, portanto, não é adequado para criptografia híbrida.

Então, daremos suporte apenas à criptografia híbrida, para NTCP2, SSU2 e Ratchet. Definiremos as três variantes ML-KEM conforme [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf), totalizando 3 novos tipos de criptografia. Os tipos híbridos serão definidos apenas em combinação com X25519.

Os novos tipos de criptografia são:

| Tipo | Código |
|------|--------|
| MLKEM512_X25519 | 5 |
| MLKEM768_X25519 | 6 |
| MLKEM1024_X25519 | 7 |
A sobrecarga será substancial. Os tamanhos típicos das mensagens 1 e 2 (para XK e IK) são atualmente cerca de 100 bytes (antes de qualquer payload adicional). Isso aumentará de 8x a 15x dependendo do algoritmo.

### Assinaturas

Ofereceremos suporte a assinaturas PQ e híbridas nas seguintes estruturas:

| Tipo | Suporta apenas PQ? | Suporta Híbrido? |
|------|-------------------|------------------|
| RouterInfo | sim | sim |
| LeaseSet | sim | sim |
| Streaming SYN/SYNACK/Close | sim | sim |
| Repliable Datagrams | sim | sim |
| Datagram2 (prop. 163) | sim | sim |
| I2CP create session msg | sim | sim |
| SU3 files | sim | sim |
| X.509 certificates | sim | sim |
| Java keystores | sim | sim |
Então iremos suportar tanto assinaturas apenas PQ quanto híbridas. Definiremos as três variantes ML-DSA como em [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf), três variantes híbridas com Ed25519, e três variantes apenas PQ com prehash apenas para arquivos SU3, totalizando 9 novos tipos de assinatura. Tipos híbridos só serão definidos em combinação com Ed25519. Usaremos o ML-DSA padrão, NÃO as variantes pre-hash (HashML-DSA), exceto para arquivos SU3.

Usaremos a variante de assinatura "hedged" ou randomizada, não a variante "determinística", conforme definido na seção 3.4 do [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf). Isso garante que cada assinatura seja diferente, mesmo quando sobre os mesmos dados, e fornece proteção adicional contra ataques de canal lateral. Consulte a seção de notas de implementação abaixo para detalhes adicionais sobre as escolhas de algoritmo, incluindo codificação e contexto.

Os novos tipos de assinatura são:

| Tipo | Código |
|------|--------|
| MLDSA44 | 12 |
| MLDSA65 | 13 |
| MLDSA87 | 14 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 |
| MLDSA44ph | 18 |
| MLDSA65ph | 19 |
| MLDSA87ph | 20 |
Certificados X.509 e outras codificações DER utilizarão as estruturas compostas e OIDs definidos no [rascunho do IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/).

O overhead será substancial. Os tamanhos típicos de destino Ed25519 e identidade de router são 391 bytes. Estes aumentarão de 3,5x a 6,8x dependendo do algoritmo. As assinaturas Ed25519 são 64 bytes. Estas aumentarão de 38x a 76x dependendo do algoritmo. RouterInfo assinados típicos, leaseSet, datagramas com resposta e mensagens de streaming assinadas são cerca de 1KB. Estes aumentarão de 3x a 8x dependendo do algoritmo.

Como os novos tipos de identidade de destino e router não conterão preenchimento, eles não serão comprimíveis. Os tamanhos de destinos e identidades de router que são comprimidos com gzip em trânsito aumentarão em 12x - 38x dependendo do algoritmo.

### Combinações Legais

Para Destinations, os novos tipos de assinatura são suportados com todos os tipos de criptografia no leaseSet. Defina o tipo de criptografia no certificado de chave como NONE (255).

Para RouterIdentities, o tipo de criptografia ElGamal está obsoleto. Os novos tipos de assinatura são suportados apenas com criptografia X25519 (tipo 4). Os novos tipos de criptografia serão indicados nos RouterAddresses. O tipo de criptografia no certificado de chave continuará sendo tipo 4.

### Nova Criptografia Necessária

- ML-KEM (anteriormente CRYSTALS-Kyber) [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
- ML-DSA (anteriormente CRYSTALS-Dilithium) [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
- SHA3-128 (anteriormente Keccak-256) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf) Usado apenas para SHAKE128
- SHA3-256 (anteriormente Keccak-512) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
- SHAKE128 e SHAKE256 (extensões XOF para SHA3-128 e SHA3-256) [FIPS 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)

Vetores de teste para SHA3-256, SHAKE128, e SHAKE256 estão disponíveis no [NIST](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values).

Note que a biblioteca Java bouncycastle suporta todos os itens acima. O suporte da biblioteca C++ está no OpenSSL 3.5 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

### Alternativas

Não daremos suporte ao [FIPS 205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf) (Sphincs+), ele é muito mais lento e maior que o ML-DSA. Não daremos suporte ao próximo FIPS206 (Falcon), ele ainda não foi padronizado. Não daremos suporte ao NTRU ou outros candidatos PQ que não foram padronizados pelo NIST.

### Rosenpass

Existe alguma [pesquisa](https://eprint.iacr.org/2020/379.pdf) sobre adaptar o Wireguard (IK) para criptografia PQ pura, mas há várias questões em aberto nesse artigo. Posteriormente, essa abordagem foi implementada como Rosenpass [Rosenpass](https://rosenpass.eu/) [whitepaper](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf) para PQ Wireguard.

O Rosenpass usa um handshake semelhante ao Noise KK com chaves estáticas pré-compartilhadas Classic McEliece 460896 (500 KB cada) e chaves efêmeras Kyber-512 (essencialmente MLKEM-512). Como os textos cifrados Classic McEliece têm apenas 188 bytes, e as chaves públicas e textos cifrados Kyber-512 são razoáveis, ambas as mensagens de handshake cabem em um MTU UDP padrão. A chave compartilhada de saída (osk) do handshake PQ KK é usada como a chave pré-compartilhada de entrada (psk) para o handshake IK padrão do Wireguard. Portanto, há dois handshakes completos no total, um puramente PQ e outro puramente X25519.

Não podemos fazer nada disso para substituir nossos handshakes XK e IK porque:

- Não podemos fazer KK, Bob não tem a chave estática da Alice
- Chaves estáticas de 500KB são grandes demais
- Não queremos uma viagem de ida e volta extra

Há muitas informações úteis no whitepaper, e vamos analisá-lo em busca de ideias e inspiração. TODO.

## Especificação

### Estruturas Comuns

Atualize as seções e tabelas no documento de estruturas comuns [/docs/specs/common-structures/](/docs/specs/common-structures/) da seguinte forma:

### PublicKey

Os novos tipos de Chave Pública são:

| Tipo | Comprimento da Chave Pública | Desde | Uso |
|------|-------------------------------|-------|-----|
| MLKEM512_X25519 | 32 | 0.9.xx | Ver proposta 169, apenas para Leasesets, não para RIs ou Destinations |
| MLKEM768_X25519 | 32 | 0.9.xx | Ver proposta 169, apenas para Leasesets, não para RIs ou Destinations |
| MLKEM1024_X25519 | 32 | 0.9.xx | Ver proposta 169, apenas para Leasesets, não para RIs ou Destinations |
| MLKEM512 | 800 | 0.9.xx | Ver proposta 169, apenas para handshakes, não para Leasesets, RIs ou Destinations |
| MLKEM768 | 1184 | 0.9.xx | Ver proposta 169, apenas para handshakes, não para Leasesets, RIs ou Destinations |
| MLKEM1024 | 1568 | 0.9.xx | Ver proposta 169, apenas para handshakes, não para Leasesets, RIs ou Destinations |
| MLKEM512_CT | 768 | 0.9.xx | Ver proposta 169, apenas para handshakes, não para Leasesets, RIs ou Destinations |
| MLKEM768_CT | 1088 | 0.9.xx | Ver proposta 169, apenas para handshakes, não para Leasesets, RIs ou Destinations |
| MLKEM1024_CT | 1568 | 0.9.xx | Ver proposta 169, apenas para handshakes, não para Leasesets, RIs ou Destinations |
| NONE | 0 | 0.9.xx | Ver proposta 169, apenas para destinations com tipos de assinatura PQ, não para RIs ou Leasesets |
As chaves públicas híbridas são a chave X25519. As chaves públicas KEM são a chave PQ efêmera enviada de Alice para Bob. A codificação e ordem de bytes são definidas em [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

As chaves MLKEM*_CT não são realmente chaves públicas, elas são o "texto cifrado" enviado de Bob para Alice no handshake Noise. Elas são listadas aqui para completude.

### PrivateKey

Os novos tipos de Chave Privada são:

| Tipo | Comprimento da Chave Privada | Desde | Uso |
|------|---------------------|-------|-------|
| MLKEM512_X25519 | 32 | 0.9.xx | Ver proposta 169, apenas para Leasesets, não para RIs ou Destinations |
| MLKEM768_X25519 | 32 | 0.9.xx | Ver proposta 169, apenas para Leasesets, não para RIs ou Destinations |
| MLKEM1024_X25519 | 32 | 0.9.xx | Ver proposta 169, apenas para Leasesets, não para RIs ou Destinations |
| MLKEM512 | 1632 | 0.9.xx | Ver proposta 169, apenas para handshakes, não para Leasesets, RIs ou Destinations |
| MLKEM768 | 2400 | 0.9.xx | Ver proposta 169, apenas para handshakes, não para Leasesets, RIs ou Destinations |
| MLKEM1024 | 3168 | 0.9.xx | Ver proposta 169, apenas para handshakes, não para Leasesets, RIs ou Destinations |
Chaves privadas híbridas são as chaves X25519. Chaves privadas KEM são apenas para Alice. A codificação KEM e a ordem de bytes são definidas em [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

### SigningPublicKey

Os novos tipos de Chave Pública de Assinatura são:

| Tipo | Comprimento (bytes) | Desde | Uso |
|------|---------------------|-------|-----|
| MLDSA44 | 1312 | 0.9.xx | Ver proposta 169 |
| MLDSA65 | 1952 | 0.9.xx | Ver proposta 169 |
| MLDSA87 | 2592 | 0.9.xx | Ver proposta 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 1344 | 0.9.xx | Ver proposta 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 1984 | 0.9.xx | Ver proposta 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 2624 | 0.9.xx | Ver proposta 169 |
| MLDSA44ph | 1344 | 0.9.xx | Apenas para arquivos SU3, não para estruturas netDb |
| MLDSA65ph | 1984 | 0.9.xx | Apenas para arquivos SU3, não para estruturas netDb |
| MLDSA87ph | 2624 | 0.9.xx | Apenas para arquivos SU3, não para estruturas netDb |
As chaves públicas de assinatura híbrida são a chave Ed25519 seguida pela chave PQ, como no [rascunho do IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/). A codificação e ordem de bytes são definidas no [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf).

### SigningPrivateKey

Os novos tipos de Chave Privada de Assinatura são:

| Tipo | Comprimento (bytes) | Desde | Uso |
|------|---------------------|-------|-----|
| MLDSA44 | 2560 | 0.9.xx | Ver proposta 169 |
| MLDSA65 | 4032 | 0.9.xx | Ver proposta 169 |
| MLDSA87 | 4896 | 0.9.xx | Ver proposta 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 2592 | 0.9.xx | Ver proposta 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 4064 | 0.9.xx | Ver proposta 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 4928 | 0.9.xx | Ver proposta 169 |
| MLDSA44ph | 2592 | 0.9.xx | Apenas para arquivos SU3, não para estruturas netDb. Ver proposta 169 |
| MLDSA65ph | 4064 | 0.9.xx | Apenas para arquivos SU3, não para estruturas netDb. Ver proposta 169 |
| MLDSA87ph | 4928 | 0.9.xx | Apenas para arquivos SU3, não para estruturas netDb. Ver proposta 169 |
Chaves privadas de assinatura híbridas são a chave Ed25519 seguida pela chave PQ, como no [rascunho IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/). A codificação e ordem de bytes são definidas no [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf).

### Assinatura

Os novos tipos de Signature são:

| Tipo | Comprimento (bytes) | Desde | Uso |
|------|---------------------|-------|-----|
| MLDSA44 | 2420 | 0.9.xx | Ver proposta 169 |
| MLDSA65 | 3309 | 0.9.xx | Ver proposta 169 |
| MLDSA87 | 4627 | 0.9.xx | Ver proposta 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 2484 | 0.9.xx | Ver proposta 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 3373 | 0.9.xx | Ver proposta 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 4691 | 0.9.xx | Ver proposta 169 |
| MLDSA44ph | 2484 | 0.9.xx | Apenas para arquivos SU3, não para estruturas netDb. Ver proposta 169 |
| MLDSA65ph | 3373 | 0.9.xx | Apenas para arquivos SU3, não para estruturas netDb. Ver proposta 169 |
| MLDSA87ph | 4691 | 0.9.xx | Apenas para arquivos SU3, não para estruturas netDb. Ver proposta 169 |
As assinaturas híbridas são a assinatura Ed25519 seguida pela assinatura PQ, como no [rascunho IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/). As assinaturas híbridas são verificadas verificando ambas as assinaturas, e falhando se qualquer uma falhar. A codificação e ordem de bytes são definidas no [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf).

### Certificados de Chave

Os novos tipos de Chave Pública de Assinatura são:

| Tipo | Código do Tipo | Comprimento Total da Chave Pública | Desde | Uso |
|------|----------------|-------------------------------------|-------|-----|
| MLDSA44 | 12 | 1312 | 0.9.xx | Ver proposta 169 |
| MLDSA65 | 13 | 1952 | 0.9.xx | Ver proposta 169 |
| MLDSA87 | 14 | 2592 | 0.9.xx | Ver proposta 169 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 0.9.xx | Ver proposta 169 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 0.9.xx | Ver proposta 169 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 0.9.xx | Ver proposta 169 |
| MLDSA44ph | 18 | n/a | 0.9.xx | Apenas para arquivos SU3 |
| MLDSA65ph | 19 | n/a | 0.9.xx | Apenas para arquivos SU3 |
| MLDSA87ph | 20 | n/a | 0.9.xx | Apenas para arquivos SU3 |
Os novos tipos de Chave Pública Criptográfica são:

| Tipo | Código do Tipo | Comprimento Total da Chave Pública | Desde | Uso |
|------|----------------|-------------------------------------|-------|-----|
| MLKEM512_X25519 | 5 | 32 | 0.9.xx | Ver proposta 169, apenas para Leasesets, não para RIs ou Destinations |
| MLKEM768_X25519 | 6 | 32 | 0.9.xx | Ver proposta 169, apenas para Leasesets, não para RIs ou Destinations |
| MLKEM1024_X25519 | 7 | 32 | 0.9.xx | Ver proposta 169, apenas para Leasesets, não para RIs ou Destinations |
| NONE | 255 | 0 | 0.9.xx | Ver proposta 169 |
Tipos de chave híbrida NUNCA são incluídos em certificados de chave; apenas em leaseSets.

Para destinos com tipos de assinatura Hybrid ou PQ, use NONE (tipo 255) para o tipo de criptografia, mas não há chave criptográfica, e toda a seção principal de 384 bytes é para a chave de assinatura.

### Tamanhos de destino

Aqui estão os comprimentos para os novos tipos de Destination. O tipo Enc para todos é NONE (tipo 255) e o comprimento da chave de encriptação é tratado como 0. Toda a seção de 384 bytes é usada para a primeira parte da chave pública de assinatura. NOTA: Isto é diferente da especificação para os tipos de assinatura ECDSA_SHA512_P521 e RSA, onde mantivemos a chave ElGamal de 256 bytes no destination mesmo que não fosse utilizada.

Sem preenchimento. O comprimento total é 7 + comprimento total da chave. O comprimento do certificado da chave é 4 + comprimento excedente da chave.

Exemplo de fluxo de bytes de destino de 1319 bytes para MLDSA44:

skey[0:383] 5 (932 >> 8) (932 & 0xff) 00 12 00 255 skey[384:1311]

| Tipo | Código do Tipo | Comprimento Total da Chave Pública | Principal | Excesso | Comprimento Total do Destino |
|------|-----------|-------------------------|------|--------|-------------------|
| MLDSA44 | 12 | 1312 | 384 | 928 | 1319 |
| MLDSA65 | 13 | 1952 | 384 | 1568 | 1959 |
| MLDSA87 | 14 | 2592 | 384 | 2208 | 2599 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 384 | 960 | 1351 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 384 | 1600 | 1991 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 384 | 2240 | 2631 |
### Tamanhos de RouterIdent

Aqui estão os comprimentos para os novos tipos de Destination. O tipo Enc para todos é X25519 (tipo 4). Toda a seção de 352 bytes após a chave pública X25519 é usada para a primeira parte da chave pública de assinatura. Sem preenchimento. O comprimento total é 39 + comprimento total da chave. O comprimento do certificado da chave é 4 + comprimento excedente da chave.

Exemplo de fluxo de bytes de identidade de router de 1351 bytes para MLDSA44:

enckey[0:31] skey[0:351] 5 (960 >> 8) (960 & 0xff) 00 12 00 4 skey[352:1311]

| Tipo | Código do Tipo | Comprimento Total da Chave Pública | Principal | Excesso | Comprimento Total do RouterIdent |
|------|-----------|-------------------------|------|--------|--------------------------|
| MLDSA44 | 12 | 1312 | 352 | 960 | 1351 |
| MLDSA65 | 13 | 1952 | 352 | 1600 | 1991 |
| MLDSA87 | 14 | 2592 | 352 | 2240 | 2631 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 15 | 1344 | 352 | 992 | 1383 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 16 | 1984 | 352 | 1632 | 2023 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 17 | 2624 | 352 | 2272 | 2663 |
### Padrões de Handshake

Handshakes usam padrões de handshake do [Noise Protocol](https://noiseprotocol.org/noise.html).

O seguinte mapeamento de letras é usado:

- e = chave efêmera de uso único
- s = chave estática
- p = carga útil da mensagem
- e1 = chave PQ efêmera de uso único, enviada de Alice para Bob
- ekem1 = o texto cifrado KEM, enviado de Bob para Alice

As seguintes modificações para XK e IK para sigilo futuro híbrido (hfs) são conforme especificado na [especificação Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf) seção 5:

```
XK:                       XKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, p               -> e, es, e1, p
  <- e, ee, p               <- e, ee, ekem1, p
  -> s, se                  -> s, se
  <- p                      <- p
  p ->                      p ->


  IK:                       IKhfs:
  <- s                      <- s
  ...                       ...
  -> e, es, s, ss, p       -> e, es, e1, s, ss, p
  <- tag, e, ee, se, p     <- tag, e, ee, ekem1, se, p
  <- p                     <- p
  p ->                     p ->

  e1 and ekem1 are encrypted. See pattern definitions below.
  NOTE: e1 and ekem1 are different sizes (unlike X25519)
```
O padrão e1 é definido da seguinte forma, conforme especificado na seção 4 da [especificação Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf):

```
For Alice:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++
  MixHash(ciphertext)

  For Bob:

  // DecryptAndHash(ciphertext)
  encap_key = DECRYPT(k, n, ciphertext, ad)
  n++
  MixHash(ciphertext)
```
O padrão ekem1 é definido da seguinte forma, conforme especificado na seção 4 do [Noise HFS spec](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf):

```
For Bob:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  MixKey(kem_shared_key)


  For Alice:

  // DecryptAndHash(ciphertext)
  kem_ciphertext = DECRYPT(k, n, ciphertext, ad)
  MixHash(ciphertext)

  // MixKey
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  MixKey(kem_shared_key)
```
### KDF do Handshake Noise

#### Problemas

- Devemos alterar a função hash do handshake? Veja a [comparação](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3).
  SHA256 não é vulnerável a PQ, mas se quisermos atualizar
  nossa função hash, agora é o momento, enquanto estamos mudando outras coisas.
  A proposta SSH IETF atual [rascunho IETF](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/) é usar MLKEM768
  com SHA256, e MLKEM1024 com SHA384. Essa proposta inclui
  uma discussão das considerações de segurança.
- Devemos parar de enviar dados ratchet 0-RTT (além do LS)?
- Devemos mudar o ratchet de IK para XK se não enviarmos dados 0-RTT?

#### Visão Geral

Esta seção se aplica aos protocolos IK e XK.

O handshake híbrido é definido na [especificação Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf). A primeira mensagem, de Alice para Bob, contém e1, a chave de encapsulamento, antes da carga útil da mensagem. Isso é tratado como uma chave estática adicional; chame EncryptAndHash() nela (como Alice) ou DecryptAndHash() (como Bob). Em seguida, processe a carga útil da mensagem normalmente.

A segunda mensagem, de Bob para Alice, contém ekem1, o texto cifrado, antes da carga útil da mensagem. Isto é tratado como uma chave estática adicional; chame EncryptAndHash() nela (como Bob) ou DecryptAndHash() (como Alice). Em seguida, calcule a kem_shared_key e chame MixKey(kem_shared_key). Depois processe a carga útil da mensagem como de costume.

#### Operações ML-KEM Definidas

Definimos as seguintes funções correspondentes aos blocos de construção criptográficos utilizados conforme definido em [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).

(encap_key, decap_key) = PQ_KEYGEN()

    Alice creates the encapsulation and decapsulation keys
    The encapsulation key is sent in message 1.
    encap_key and decap_key sizes vary based on ML-KEM variant.

(ciphertext, kem_shared_key) = ENCAPS(encap_key)

    Bob calculates the ciphertext and shared key,
    using the ciphertext received in message 1.
    The ciphertext is sent in message 2.
    ciphertext size varies based on ML-KEM variant.
    The kem_shared_key is always 32 bytes.

kem_shared_key = DECAPS(ciphertext, decap_key)

    Alice calculates the shared key,
    using the ciphertext received in message 2.
    The kem_shared_key is always 32 bytes.

Note que tanto o encap_key quanto o ciphertext são criptografados dentro de blocos ChaCha/Poly nas mensagens 1 e 2 do handshake Noise. Eles serão descriptografados como parte do processo de handshake.

A kem_shared_key é misturada na chaining key com MixHash(). Veja abaixo para detalhes.

#### KDF de Alice para Mensagem 1

Para XK: Após o padrão de mensagem 'es' e antes da carga útil, adicione:

OU

Para IK: Após o padrão de mensagem 'es' e antes do padrão de mensagem 's', adicione:

```
This is the "e1" message pattern:
  (encap_key, decap_key) = PQ_KEYGEN()

  // EncryptAndHash(encap_key)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, encap_key, ad)
  n++

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)


  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### Bob KDF para Mensagem 1

Para XK: Após o padrão de mensagem 'es' e antes da carga útil, adicione:

OU

Para IK: Após o padrão de mensagem 'es' e antes do padrão de mensagem 's', adicione:

```
This is the "e1" message pattern:

  // DecryptAndHash(encap_key_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  encap_key = DECRYPT(k, n, encap_key_section, ad)
  n++

  // MixHash(encap_key_section)
  h = SHA256(h || encap_key_section)

  End of "e1" message pattern.

  NOTE: For the next section (payload for XK or static key for IK),
  the keydata and chain key remain the same,
  and n now equals 1 (instead of 0 for non-hybrid).
```
#### Bob KDF para Mensagem 2

Para XK: Após o padrão de mensagem 'ee' e antes da carga útil, adicione:

OU

Para IK: Após o padrão de mensagem 'ee' e antes do padrão de mensagem 'se', adicione:

```
This is the "ekem1" message pattern:

  (kem_ciphertext, kem_shared_key) = ENCAPS(encap_key)

  // EncryptAndHash(kem_ciphertext)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  ciphertext = ENCRYPT(k, n, kem_ciphertext, ad)

  // MixHash(ciphertext)
  h = SHA256(h || ciphertext)

  // MixKey(kem_shared_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### Alice KDF para Mensagem 2

Após o padrão de mensagem 'ee' (e antes do padrão de mensagem 'ss' para IK), adicione:

```
This is the "ekem1" message pattern:

  // DecryptAndHash(kem_ciphertext_section)
  // AEAD parameters
  k = keydata[32:63]
  n = 0
  ad = h
  kem_ciphertext = DECRYPT(k, n, kem_ciphertext_section, ad)

  // MixHash(kem_ciphertext_section)
  h = SHA256(h || kem_ciphertext_section)

  // MixKey(kem_shared_key)
  kem_shared_key = DECAPS(kem_ciphertext, decap_key)
  keydata = HKDF(chainKey, kem_shared_key, "", 64)
  chainKey = keydata[0:31]

  End of "ekem1" message pattern.
```
#### KDF para Mensagem 3 (apenas XK)

inalterado

#### KDF para split()

inalterado

### Ratchet

Atualize a especificação ECIES-Ratchet [/docs/specs/ecies/](/docs/specs/ecies/) como segue:

#### Identificadores Noise

- "Noise_IKhfselg2_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_IKhfselg2_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_IKhfselg2_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1b) Novo formato de sessão (com vinculação)

Mudanças: O ratchet atual continha a chave estática na primeira seção ChaCha, e o payload na segunda seção. Com ML-KEM, agora há três seções. A primeira seção contém a chave pública PQ criptografada. A segunda seção contém a chave estática. A terceira seção contém o payload.

Formato criptografado:

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   New Session Ephemeral Public Key    |
  +             32 bytes                  +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           ML-KEM encap_key            +
  |       ChaCha20 encrypted data         |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +    (MAC) for encap_key Section        +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +           X25519 Static Key           +
  |       ChaCha20 encrypted data         |
  +             32 bytes                  +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +    (MAC) for Static Key Section       +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
```
Formato descriptografado:

```
Payload Part 1:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +       ML-KEM encap_key                +
  |                                       |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 2:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +       X25519 Static Key               +
  |                                       |
  +      (32 bytes)                       +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 3:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |                                       |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Tamanhos:

| Tipo | Código do Tipo | X len | Msg 1 len | Msg 1 Enc len | Msg 1 Dec len | PQ key len | pl len |
|------|-----------|-------|-----------|---------------|---------------|------------|--------|
| X25519 | 4 | 32 | 96+pl | 64+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 912+pl | 880+pl | 800+pl | 800 | pl |
| MLKEM768_X25519 | 6 | 32 | 1296+pl | 1360+pl | 1184+pl | 1184 | pl |
| MLKEM1024_X25519 | 7 | 32 | 1680+pl | 1648+pl | 1568+pl | 1568 | pl |
Note que a carga útil deve conter um bloco DateTime, então o tamanho mínimo da carga útil é 7. Os tamanhos mínimos da mensagem 1 podem ser calculados de acordo.

#### 1g) Formato de Resposta de Nova Sessão

Mudanças: O ratchet atual tem uma carga útil vazia para a primeira seção ChaCha, e a carga útil na segunda seção. Com ML-KEM, agora há três seções. A primeira seção contém o texto cifrado PQ encriptado. A segunda seção tem uma carga útil vazia. A terceira seção contém a carga útil.

Formato criptografado:

```
  +----+----+----+----+----+----+----+----+
  |       Session Tag   8 bytes           |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        Ephemeral Public Key           +
  |                                       |
  +            32 bytes                   +
  |     Encoded with Elligator2           |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  | ChaCha20 encrypted ML-KEM ciphertext  |
  +      (see table below for length)     +
  ~                                       ~
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +  (MAC) for ciphertext Section         +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +  (MAC) for key Section (no data)      +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |       ChaCha20 encrypted data         |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |  Poly1305 Message Authentication Code |
  +         (MAC) for Payload Section     +
  |             16 bytes                  |
  +----+----+----+----+----+----+----+----+
```
Formato descriptografado:

```
Payload Part 1:


  +----+----+----+----+----+----+----+----+
  |                                       |
  +       ML-KEM ciphertext               +
  |                                       |
  +      (see table below for length)     +
  |                                       |
  ~                                       ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Payload Part 2:

  empty

  Payload Part 3:

  +----+----+----+----+----+----+----+----+
  |                                       |
  +            Payload Section            +
  |                                       |
  ~                                       ~
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Tamanhos:

| Tipo | Código do Tipo | Y len | Msg 2 len | Msg 2 Enc len | Msg 2 Dec len | PQ CT len | opt len |
|------|-----------|-------|-----------|---------------|---------------|-----------|---------|
| X25519 | 4 | 32 | 72+pl | 32+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 856+pl | 816+pl | 768+pl | 768 | pl |
| MLKEM768_X25519 | 6 | 32 | 1176+pl | 1136+pl | 1088+pl | 1088 | pl |
| MLKEM1024_X25519 | 7 | 32 | 1656+pl | 1616+pl | 1568+pl | 1568 | pl |
Note que, embora a mensagem 2 normalmente tenha uma carga útil diferente de zero, a especificação do ratchet [/docs/specs/ecies/](/docs/specs/ecies/) não a exige, então o tamanho mínimo da carga útil é 0. Os tamanhos mínimos da mensagem 2 podem ser calculados adequadamente.

### NTCP2

Atualize a especificação NTCP2 [/docs/specs/ntcp2/](/docs/specs/ntcp2/) da seguinte forma:

#### Identificadores Noise

- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"
- "Noise_XKhfsaesobfse+hs2+hs3_25519+MLKEM1024_ChaChaPoly_SHA256"

#### 1) SessionRequest

Mudanças: O NTCP2 atual contém apenas as opções na seção ChaCha. Com ML-KEM, a seção ChaCha também conterá a chave pública PQ criptografada.

Para que PQ e NTCP2 não-PQ possam ser suportados no mesmo endereço e porta do router, usamos o bit mais significativo do valor X (chave pública efêmera X25519) para marcar que é uma conexão PQ. Este bit está sempre desmarcado para conexões não-PQ.

Para Alice, após a mensagem ser criptografada pelo Noise, mas antes da ofuscação AES de X, definir X[31] |= 0x7f.

Para Bob, após a des-ofuscação AES de X, teste X[31] & 0x80. Se o bit estiver definido, limpe-o com X[31] &= 0x7f, e descriptografe via Noise como uma conexão PQ. Se o bit estiver limpo, descriptografe via Noise como uma conexão não-PQ como de costume.

Para PQ NTCP2 anunciado em um endereço de router e porta diferentes, isso não é necessário.

Para informações adicionais, consulte a seção Endereços Publicados abaixo.

Conteúdos brutos:

```
  +----+----+----+----+----+----+----+----+
  |        MS bit set to 1 and then       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted X         |
  +             (32 bytes)                +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +      (see table below for length)     +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  ~   n = 0                               ~
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaChaPoly frame (options)          |
  +         32 bytes                      +
  |   k defined in KDF for message 1      |
  +   n = 0                               +
  |   see KDF for associated data         |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  ~         padding (optional)            ~
  |     length defined in options block   |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
Dados não criptografados (tag de autenticação Poly1305 não mostrada):

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                   X                   |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM encap_key            |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Nota: o campo de versão no bloco de opções da mensagem 1 deve ser definido como 2, mesmo para conexões PQ.

Tamanhos:

| Tipo | Código do Tipo | X len | Msg 1 len | Msg 1 Enc len | Msg 1 Dec len | PQ key len | opt len |
|------|-----------|-------|-----------|---------------|---------------|------------|---------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 880+pad | 848 | 816 | 800 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1264+pad | 1232 | 1200 | 1184 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1648+pad | 1616 | 1584 | 1568 | 16 |
Nota: Os códigos de tipo são apenas para uso interno. Os routers permanecerão como tipo 4, e o suporte será indicado nos endereços do router.

#### 2) SessionCreated

Conteúdo bruto:

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +        obfuscated with RH_B           +
  |       AES-CBC-256 encrypted Y         |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (MLKEM)            |
  +   Encrypted and authenticated data    +
  -      (see table below for length)     -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaChaPoly frame (options)          |
  +   Encrypted and authenticated data    +
  -           32 bytes                    -
  +   k defined in KDF for message 2      +
  |   n = 0; see KDF for associated data  |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+

  Same as current specification except add a second ChaChaPoly frame
```
Dados não criptografados (tag de autenticação Poly1305 não mostrada):

```
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |                  Y                    |
  +              (32 bytes)               +
  |                                       |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |               options                 |
  +              (16 bytes)               +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     unencrypted authenticated         |
  +         padding (optional)            +
  |     length defined in options block   |
  ~               .   .   .               ~
  |                                       |
  +----+----+----+----+----+----+----+----+
```
Tamanhos:

| Tipo | Código do Tipo | Comprimento Y | Comprimento Msg 2 | Comprimento Msg 2 Enc | Comprimento Msg 2 Dec | Comprimento PQ CT | Comprimento opt |
|------|----------------|---------------|-------------------|----------------------|----------------------|-------------------|-----------------|
| X25519 | 4 | 32 | 64+pad | 32 | 16 | -- | 16 |
| MLKEM512_X25519 | 5 | 32 | 848+pad | 816 | 784 | 768 | 16 |
| MLKEM768_X25519 | 6 | 32 | 1136+pad | 1104 | 1104 | 1088 | 16 |
| MLKEM1024_X25519 | 7 | 32 | 1616+pad | 1584 | 1584 | 1568 | 16 |
Nota: Os códigos de tipo são apenas para uso interno. Os routers permanecerão como tipo 4, e o suporte será indicado nos endereços do router.

#### 3) SessionConfirmed

Inalterado

#### Função de Derivação de Chave (KDF) (para fase de dados)

Inalterado

#### Endereços Publicados

Em todos os casos, use o nome de transporte NTCP2 como de costume.

Use o mesmo endereço/porta como não-PQ, não-firewalled. Apenas uma variante PQ é suportada. No endereço do router, publique v=2 (como usual) e o novo parâmetro pq=[3|4|5] para indicar MLKEM 512/768/1024. Alice define o MSB da chave efêmera (key[31] & 0x80) na solicitação de sessão para indicar que esta é uma conexão híbrida. Veja acima. Routers mais antigos irão ignorar o parâmetro pq e conectar não-pq como usual.

Endereço/porta diferente como não-PQ, ou somente PQ, não-firewalled NÃO é suportado. Isso não será implementado até que NTCP2 não-PQ seja desabilitado, daqui a vários anos. Quando não-PQ for desabilitado, múltiplas variantes PQ podem ser suportadas, mas apenas uma por endereço. No endereço do router, publique v=[3|4|5] para indicar MLKEM 512/768/1024. Alice não define o MSB da chave efêmera. Routers mais antigos verificarão o parâmetro v e pularão este endereço como não suportado.

Endereços com firewall (nenhum IP publicado): No endereço do router, publique v=2 (como de costume). Não há necessidade de publicar um parâmetro pq.

Alice pode conectar-se a um Bob PQ usando a variante PQ que Bob publica, independentemente de Alice anunciar suporte pq em suas informações de router, ou se ela anuncia a mesma variante.

#### Padding Máximo

Na especificação atual, as mensagens 1 e 2 são definidas para ter uma quantidade "razoável" de padding, com um intervalo de 0-31 bytes recomendado, e nenhum máximo especificado.

Até a API 0.9.68 (versão 2.11.0), o Java I2P implementava um máximo de 256 bytes de padding para conexões não-PQ, porém isso não estava documentado anteriormente. A partir da API 0.9.69 (versão 2.12.0), o Java I2P implementa o mesmo padding máximo para conexões não-PQ que para MLKEM-512. Veja a tabela abaixo.

Use o tamanho de mensagem definido como o padding máximo, ou seja, o padding máximo irá dobrar o tamanho da mensagem para conexões PQ, da seguinte forma:

| Preenchimento Máximo da Mensagem | não-PQ (até 0.9.68) | não-PQ (a partir de 0.9.69) | MLKEM-512 | MLKEM-768 | MLKEM-1024 |
|----------------------------------|----------------------|------------------------------|-----------|-----------|------------|
| Session Request  |   256   |   880   |    880   |     1264   |    1648  |
| Session Created  |   256   |   848   |    848   |     1136   |    1616  |
### SSU2

Atualize a especificação SSU2 [/docs/specs/ssu2/](/docs/specs/ssu2/) da seguinte forma:

#### Identificadores de Noise

- "Noise_XKhfschaobfse+hs1+hs2+hs3_25519+MLKEM512_ChaChaPoly_SHA256"
- "Noise_XKhfschaobfse+hs1+hs2+hs3_25519+MLKEM768_ChaChaPoly_SHA256"

Note que MLKEM-1024 NÃO é suportado para SSU2, pois as chaves são muito grandes para caber dentro de um datagrama padrão de 1500 bytes.

#### Cabeçalho Longo

O cabeçalho longo tem 32 bytes. É usado antes de uma sessão ser criada, para Token Request, SessionRequest, SessionCreated e Retry. Também é usado para mensagens Peer Test e Hole Punch fora de sessão.

Nas mensagens seguintes, defina o campo ver (versão) no cabeçalho longo para 3 ou 4, para indicar MLKEM-512 ou MLKEM-768.

- (0) Solicitação de Sessão
- (1) Sessão Criada
- (9) Tentar Novamente
- (10) Solicitação de Token
- (11) Perfuração de Buraco

Nas seguintes mensagens, defina o campo ver (versão) no cabeçalho longo como 2, como de costume, mesmo se MLKEM-512 ou MLKEM-768 for suportado. As implementações também podem definir o valor como 3 ou 4, se a outra extremidade suportar, mas isso não é necessário. As implementações devem aceitar qualquer valor 2-4.

- (7) Teste de Peer (mensagens fora de sessão 5-7)

Discussão: Definir o campo de versão como 3 ou 4 pode não ser estritamente necessário para todos os tipos de mensagem, mas fazê-lo auxilia na detecção precoce de falhas para conexões pós-quânticas não suportadas. Token Request e Retry (tipos 9 e 10) devem ter versões 3/4 para consistência. Mensagens Hole Punch (tipo 11) podem não exigir este tratamento, mas seguiremos o mesmo padrão para uniformidade. Mensagens Peer Test (tipo 7) são fora de sessão e não indicam intenção de iniciar uma sessão.

Antes da criptografia do cabeçalho:

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

  ver :: The protocol version = 2, 3, or 4 for non-PQ, MLKEM512, MLKEM768

  id :: 1 byte, the network ID (currently 2, except for test networks)

  flag :: 1 byte, unused, set to 0 for future compatibility

  Source Connection ID :: 8 bytes, unsigned big endian integer

  Token :: 8 bytes, unsigned big endian integer

```
#### Cabeçalho Curto

inalterado

#### SessionRequest (Tipo 0)

Alterações: O SSU2 atual contém apenas os dados do bloco na seção ChaCha. Com ML-KEM, a seção ChaCha também conterá a chave pública PQ criptografada.

Mudança de KDF para Proteção contra Spoofing: Para abordar as questões levantadas na Proposta 165 [Prop165]_, mas com uma solução diferente, modificamos o KDF para Session Request. Isto é apenas para sessões PQ. O KDF para sessões não-PQ permanece inalterado.

```

// End of KDF for initial chain key (unchanged)
  // Bob static key
  // MixHash(bpk)
  h = SHA256(h || bpk);

  // Start of KDF for session request
  // NEW for PQ only
  // bhash = Bob router hash (32 bytes)
  // MixHash(bhash)
  h = SHA256(h || bhash);

  // Rest of KDF for session request, unchanged, as in SSU2 spec
  // MixHash(header)
  h = SHA256(h || header)

  ...

```
Conteúdo bruto:

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
  |   ChaCha20 encrypted data (MLKEM)     |
  +          (length varies)              +
  |  k defined in KDF for Session Request |
  +  n = 0                                +
  |  see KDF for associated data          |
  +----+----+----+----+----+----+----+----+
  |                                       |
  +                                       +
  |   ChaCha20 encrypted data (payload)   |
  +          (length varies)              +
  |  k defined in KDF for Session Request |
  +  n = 0                                +
  |  see KDF for associated data          |
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
  |           ML-KEM encap_key            |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     Noise payload (block data)        |
  +          (length varies)              +
  |     see below for allowed blocks      |
  +----+----+----+----+----+----+----+----+
```
Tamanhos, não incluindo overhead do IP:

| Tipo | Código do Tipo | Tamanho X | Tamanho Msg 1 | Tamanho Msg 1 Enc | Tamanho Msg 1 Dec | Tamanho chave PQ | Tamanho pl |
|------|----------------|-----------|---------------|-------------------|-------------------|------------------|------------|
| X25519 | 4 | 32 | 80+pl | 16+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 896+pl | 832+pl | 800+pl | 800 | pl |
| MLKEM768_X25519 | 6 | 32 | 1280+pl | 1216+pl | 1184+pl | 1184 | pl |
| MLKEM1024_X25519 | 7 | n/a | muito grande | | | | |
Nota: Os códigos de tipo são apenas para uso interno. Os routers permanecerão como tipo 4, e o suporte será indicado nos endereços do router.

MTU mínimo para MLKEM768_X25519: Cerca de 1316 para IPv4 e 1336 para IPv6.

#### SessionCreated (Tipo 1)

Alterações: O SSU2 atual contém apenas os dados do bloco na seção ChaCha. Com ML-KEM, a seção ChaCha também conterá a chave pública PQ criptografada.

Conteúdo bruto:

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
  |   ChaCha20 data (MLKEM)               |
  +   Encrypted and authenticated data    +
  |  length varies                        |
  +  k defined in KDF for Session Created +
  |  n = 0; see KDF for associated data   |
  +                                       +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |   ChaCha20 data (payload)             |
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


```
Dados não criptografados (tag de autenticação Poly1305 não mostrada):

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
  |           ML-KEM Ciphertext           |
  +      (see table below for length)     +
  |                                       |
  +----+----+----+----+----+----+----+----+
  |     Noise payload (block data)        |
  +          (length varies)              +
  |      see below for allowed blocks     |
  +----+----+----+----+----+----+----+----+
```
Tamanhos, não incluindo a sobrecarga do IP:

| Tipo | Código do Tipo | Y len | Msg 2 len | Msg 2 Enc len | Msg 2 Dec len | PQ CT len | pl len |
|------|----------------|-------|-----------|---------------|---------------|-----------|--------|
| X25519 | 4 | 32 | 80+pl | 16+pl | pl | -- | pl |
| MLKEM512_X25519 | 5 | 32 | 864+pl | 800+pl | 768+pl | 768 | pl |
| MLKEM768_X25519 | 6 | 32 | 1184+pl | 1118+pl | 1088+pl | 1088 | pl |
| MLKEM1024_X25519 | 7 | n/a | muito grande | | | | |
Nota: Os códigos de tipo são apenas para uso interno. Os routers permanecerão como tipo 4, e o suporte será indicado nos endereços do router.

MTU mínimo para MLKEM768_X25519: Cerca de 1316 para IPv4 e 1336 para IPv6.

#### SessionConfirmed (Tipo 2)

inalterado

#### KDF para fase de dados

inalterado

#### Relay e Teste de Pares

Os seguintes blocos contêm campos de versão. Eles permanecerão na versão 2 (para compatibilidade com um Bob não-PQ), e não mudarão para a versão 3/4 para PQ.

- Solicitação de Retransmissão
- Resposta de Retransmissão
- Introdução de Retransmissão
- Teste de Par

Assinaturas PQ: Blocos de relay, blocos de teste de peer e mensagens de teste de peer contêm todas assinaturas. Infelizmente, as assinaturas PQ são maiores que o MTU. Não existe atualmente um mecanismo para fragmentar blocos de relay ou teste de peer ou mensagens através de múltiplos pacotes UDP. O protocolo deve ser estendido para suportar fragmentação. Isso será feito numa proposta separada a ser definida. Até que isso seja completado, relay e teste de peer não serão suportados.

#### Endereços Publicados

Em todos os casos, use o nome de transporte SSU2 como de costume. MLKEM-1024 não é suportado.

Use o mesmo endereço/porta como não-PQ, sem firewall. Uma ou ambas as variantes PQ são suportadas. No endereço do router, publique v=2 (como de costume) e o novo parâmetro pq=[3|4|3,4] para indicar MLKEM 512/768/ambos. Routers mais antigos irão ignorar o parâmetro pq e conectar não-pq como de costume.

Endereço/porta diferente como não-PQ, ou apenas PQ, sem firewall NÃO é suportado. Isso não será implementado até que SSU2 não-PQ seja desabilitado, daqui a vários anos. Quando não-PQ for desabilitado, uma ou ambas as variantes PQ são suportadas. No endereço do router, publique v=[3|4|3,4] para indicar MLKEM 512/768/ambos. Routers mais antigos verificarão o parâmetro v e pularão este endereço como não suportado.

Endereços com firewall (nenhum IP publicado): No endereço do router, publique v=2 (como de costume). O parâmetro pq DEVE ser publicado em endereços com firewall, para suportar relay.

Alice pode conectar-se a um Bob PQ usando a variante PQ que Bob publica, independentemente de Alice anunciar suporte pq em suas informações de router, ou se ela anuncia a mesma variante.

#### MTU

Tenha cuidado para não exceder o MTU com MLKEM768. O MTU mínimo para SSU2 é 1280, que é o tamanho da mensagem 1 sem preenchimento. Não inclua preenchimento na mensagem 1 se o MTU de Alice ou Bob for 1280.

#### Problemas

Poderíamos usar internamente o campo version e usar 3 para MLKEM512 e 4 para MLKEM768.

Para as mensagens 1 e 2, o MLKEM768 aumentaria o tamanho dos pacotes além do MTU mínimo de 1280. Provavelmente simplesmente não seria suportado para essa conexão se o MTU fosse muito baixo.

Para as mensagens 1 e 2, MLKEM1024 aumentaria os tamanhos dos pacotes além do MTU máximo de 1500. Isso exigiria fragmentar as mensagens 1 e 2, e seria uma grande complicação. Provavelmente não faremos isso.

Relay e Teste de Peer: Veja acima

### Streaming

TODO: Existe uma forma mais eficiente de definir assinatura/verificação para evitar copiar a assinatura?

### Arquivos SU3

TODO

A seção 8.1 do [rascunho IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/) não permite HashML-DSA em certificados X.509 e não atribui OIDs para HashML-DSA, devido às complexidades de implementação e segurança reduzida.

Para assinaturas apenas PQ de arquivos SU3, use os OIDs definidos no [rascunho IETF](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/) das variantes não-prehash para os certificados. Não definimos assinaturas híbridas de arquivos SU3, porque podemos ter que fazer o hash dos arquivos duas vezes (embora HashML-DSA e X2559 usem a mesma função hash SHA512). Além disso, concatenar duas chaves e assinaturas em um certificado X.509 seria completamente fora do padrão.

Note que não permitimos assinatura Ed25519 de arquivos SU3, e embora tenhamos definido assinatura Ed25519ph, nunca concordamos com um OID para ela, nem a utilizamos.

Os tipos de assinatura normais são proibidos para arquivos SU3; use as variantes ph (prehash).

### Outras Especificações

O novo tamanho máximo de Destination será 2599 (3468 em base 64).

Atualize outros documentos que fornecem orientação sobre tamanhos de Destination, incluindo:

- SAMv3
- Bittorrent
- Diretrizes para desenvolvedores
- Nomenclatura / livro de endereços / servidores de salto
- Outros documentos

## Análise de Sobrecarga

### Troca de Chaves

Aumento de tamanho (bytes):

| Tipo | Pubkey (Msg 1) | Cipertext (Msg 2) |
|------|----------------|-------------------|
| MLKEM512_X25519 | +816 | +784 |
| MLKEM768_X25519 | +1200 | +1104 |
| MLKEM1024_X25519 | +1584 | +1584 |
Velocidade:

Velocidades conforme relatado pela [Cloudflare](https://blog.cloudflare.com/pq-2024/):

| Tipo | Velocidade relativa |
|------|---------------------|
| X25519 DH/keygen | linha de base |
| MLKEM512 | 2.25x mais rápido |
| MLKEM768 | 1.5x mais rápido |
| MLKEM1024 | 1x (mesmo) |
| XK | 4x DH (keygen + 3 DH) |
| MLKEM512_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 4.9x DH = 22% mais lento |
| MLKEM768_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 5.3x DH = 32% mais lento |
| MLKEM1024_X25519 | 4x DH + 2x PQ (keygen + enc/dec) = 6x DH = 50% mais lento |
Resultados preliminares de teste em Java:

| Tipo | DH/encaps Relativo | DH/decaps | keygen |
|------|-------------------|-----------|--------|
| X25519 | baseline | baseline | baseline |
| MLKEM512 | 29x mais rápido | 22x mais rápido | 17x mais rápido |
| MLKEM768 | 17x mais rápido | 14x mais rápido | 9x mais rápido |
| MLKEM1024 | 12x mais rápido | 10x mais rápido | 6x mais rápido |
### Assinaturas

Tamanho:

Tamanhos típicos de chave, assinatura, RIdent, Dest ou aumentos de tamanho (Ed25519 incluído para referência) assumindo tipo de criptografia X25519 para RIs. Tamanho adicionado para um Router Info, LeaseSet, datagramas com resposta e cada um dos dois pacotes de streaming (SYN e SYN ACK) listados. Destinations e Leasesets atuais contêm preenchimento repetido e são compressíveis em trânsito. Novos tipos não contêm preenchimento e não serão compressíveis, resultando em um aumento de tamanho muito maior em trânsito. Veja a seção de design acima.

| Tipo | Pubkey | Sig | Key+Sig | RIdent | Dest | RInfo | LS/Streaming/Datagram (cada msg) |
|------|--------|-----|---------|--------|------|-------|----------------------------------|
| EdDSA_SHA512_Ed25519 | 32 | 64 | 96 | 391 | 391 | baseline | baseline |
| MLDSA44 | 1312 | 2420 | 3732 | 1351 | 1319 | +3316 | +3284 |
| MLDSA65 | 1952 | 3309 | 5261 | 1991 | 1959 | +5668 | +5636 |
| MLDSA87 | 2592 | 4627 | 7219 | 2631 | 2599 | +7072 | +7040 |
| MLDSA44_EdDSA_SHA512_Ed25519 | 1344 | 2484 | 3828 | 1383 | 1351 | +3412 | +3380 |
| MLDSA65_EdDSA_SHA512_Ed25519 | 1984 | 3373 | 5357 | 2023 | 1991 | +5668 | +5636 |
| MLDSA87_EdDSA_SHA512_Ed25519 | 2624 | 4691 | 7315 | 2663 | 2631 | +7488 | +7456 |
Velocidade:

Velocidades conforme relatado pela [Cloudflare](https://blog.cloudflare.com/pq-2024/):

| Tipo | Sinal de velocidade relativa | verificar |
|------|------------------------------|-----------|
| EdDSA_SHA512_Ed25519 | linha de base | linha de base |
| MLDSA44 | 5x mais lento | 2x mais rápido |
| MLDSA65 | ??? | ??? |
| MLDSA87 | ??? | ??? |
Resultados de teste preliminares em Java:

| Tipo | Sinal de velocidade relativa | verificar | geração de chave |
|------|------------------------------|-----------|-------------------|
| EdDSA_SHA512_Ed25519 | baseline | baseline | baseline |
| MLDSA44 | 4.6x mais lento | 1.7x mais rápido | 2.6x mais rápido |
| MLDSA65 | 8.1x mais lento | mesmo | 1.5x mais rápido |
| MLDSA87 | 11.1x mais lento | 1.5x mais lento | mesmo |
## Análise de Segurança

As categorias de segurança NIST são resumidas no [NIST presentation](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf) slide 10. Critérios preliminares: Nossa categoria mínima de segurança NIST deve ser 2 para protocolos híbridos e 3 para PQ apenas.

| Categoria | Tão Seguro Quanto |
|-----------|-------------------|
| 1 | AES128 |
| 2 | SHA256 |
| 3 | AES192 |
| 4 | SHA384 |
| 5 | AES256 |
### Handshakes

Estes são todos protocolos híbridos. As implementações devem preferir MLKEM768; MLKEM512 não é suficientemente seguro.

Categorias de segurança NIST [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf):

| Algoritmo | Categoria de Segurança |
|-----------|------------------------|
| MLKEM512 | 1 |
| MLKEM768 | 3 |
| MLKEM1024 | 5 |
### Assinaturas

Esta proposta define tanto tipos de assinatura híbrida quanto apenas PQ. MLDSA44 híbrida é preferível a MLDSA65 apenas-PQ. Os tamanhos de chaves e assinaturas para MLDSA65 e MLDSA87 são provavelmente muito grandes para nós, pelo menos inicialmente.

Categorias de segurança NIST [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf):

| Algoritmo | Categoria de Segurança |
|-----------|------------------------|
| MLDSA44 | 2 |
| MLKEM67 | 3 |
| MLKEM87 | 5 |
## Preferências de Tipo

Embora vamos definir e implementar 3 tipos de criptografia e 9 tipos de assinatura, planejamos medir o desempenho durante o desenvolvimento e analisar ainda mais os efeitos do aumento dos tamanhos das estruturas. Também continuaremos a pesquisar e monitorar desenvolvimentos em outros projetos e protocolos.

Após um ano ou mais de desenvolvimento, tentaremos definir um tipo preferido ou padrão para cada caso de uso. A seleção exigirá fazer compromissos entre largura de banda, CPU e nível de segurança estimado. Nem todos os tipos podem ser adequados ou permitidos para todos os casos de uso.

As preferências preliminares são as seguintes, sujeitas a alterações:

Criptografia: MLKEM768_X25519

Assinaturas: MLDSA44_EdDSA_SHA512_Ed25519

As restrições preliminares são as seguintes, sujeitas a alterações:

Criptografia: MLKEM1024_X25519 não permitido para SSU2

Assinaturas: MLDSA87 e variante híbrida provavelmente muito grandes; MLDSA65 e variante híbrida podem ser muito grandes

## Notas de Implementação

### Suporte de Biblioteca

As bibliotecas Bouncycastle, BoringSSL e WolfSSL agora suportam MLKEM e MLDSA. O suporte do OpenSSL estará na versão 3.5, lançada em 8 de abril de 2025 [OpenSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/).

A biblioteca Noise do southernstorm.com adaptada pelo Java I2P continha suporte preliminar para handshakes híbridos, mas removemos por não estar sendo usado; teremos que adicioná-lo de volta e atualizá-lo para corresponder à [especificação Noise HFS](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf).

### Variantes de Assinatura

Utilizaremos a variante de assinatura "hedged" ou randomizada, não a variante "determinística", conforme definido na [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) seção 3.4. Isso garante que cada assinatura seja diferente, mesmo quando sobre os mesmos dados, e fornece proteção adicional contra ataques de canal lateral. Embora a [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) especifique que a variante "hedged" é o padrão, isso pode ou não ser verdade em várias bibliotecas. Os implementadores devem garantir que a variante "hedged" seja usada para assinatura.

Utilizamos o processo normal de assinatura (chamado Pure ML-DSA Signature Generation) que codifica a mensagem internamente como 0x00 || len(ctx) || ctx || message, onde ctx é algum valor opcional de tamanho 0x00..0xFF. Não estamos usando nenhum contexto opcional. len(ctx) == 0. Este processo é definido no [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) Algoritmo 2 passo 10 e Algoritmo 3 passo 5. Note que alguns vetores de teste publicados podem exigir definir um modo onde a mensagem não é codificada.

### Confiabilidade

O aumento do tamanho resultará em muito mais fragmentação de tunnel para armazenamentos NetDB, handshakes de streaming e outras mensagens. Verifique mudanças de desempenho e confiabilidade.

### Tamanhos das Estruturas

Encontre e verifique qualquer código que limite o tamanho em bytes das informações do router e leasesets.

### NetDB

Revisar e possivelmente reduzir o máximo de LS/RI armazenados na RAM ou no disco, para limitar o aumento de armazenamento. Aumentar os requisitos mínimos de largura de banda para floodfills?

### Ratchet

#### Tunnels Compartilhados

A classificação/detecção automática de múltiplos protocolos nos mesmos tunnels deve ser possível baseada numa verificação de comprimento da mensagem 1 (New Session Message). Usando MLKEM512_X25519 como exemplo, o comprimento da mensagem 1 é 816 bytes maior que o protocolo ratchet atual, e o tamanho mínimo da mensagem 1 (com apenas um payload DateTime incluído) é 919 bytes. A maioria dos tamanhos de mensagem 1 com ratchet atual tem um payload inferior a 816 bytes, por isso podem ser classificadas como ratchet não-híbrido. Mensagens grandes são provavelmente POSTs que são raras.

Portanto, a estratégia recomendada é:

- Se a mensagem 1 for menor que 919 bytes, é o protocolo ratchet atual.
- Se a mensagem 1 for maior ou igual a 919 bytes, provavelmente é MLKEM512_X25519.
  Tente MLKEM512_X25519 primeiro, e se falhar, tente o protocolo ratchet atual.

Isso deve nos permitir suportar eficientemente o ratchet padrão e o ratchet híbrido no mesmo destino, assim como anteriormente suportávamos ElGamal e ratchet no mesmo destino. Portanto, podemos migrar para o protocolo híbrido MLKEM muito mais rapidamente do que se não pudéssemos suportar protocolos duplos para o mesmo destino, porque podemos adicionar suporte MLKEM a destinos existentes.

As combinações suportadas obrigatórias são:

- X25519 + MLKEM512
- X25519 + MLKEM768
- X25519 + MLKEM1024

As seguintes combinações podem ser complexas e NÃO são obrigatórias de serem suportadas, mas podem ser, dependendo da implementação:

- Mais de um MLKEM
- ElG + um ou mais MLKEM
- X25519 + um ou mais MLKEM
- ElG + X25519 + um ou mais MLKEM

Podemos não tentar suportar múltiplos algoritmos MLKEM (por exemplo, MLKEM512_X25519 e MLKEM_768_X25519) no mesmo destino. Escolha apenas um; no entanto, isso depende de selecionarmos uma variante MLKEM preferida, para que os túneis de cliente HTTP possam usar uma. Dependente da implementação.

Nós PODEMOS tentar suportar três algoritmos (por exemplo X25519, MLKEM512_X25519, e MLKEM769_X25519) no mesmo destino. A classificação e estratégia de repetição podem ser muito complexas. A configuração e interface de configuração podem ser muito complexas. Dependente da implementação.

Provavelmente NÃO tentaremos suportar algoritmos ElGamal e híbridos no mesmo destino. ElGamal está obsoleto, e ElGamal + híbrido apenas (sem X25519) não faz muito sentido. Além disso, as Mensagens de Nova Sessão ElGamal e Híbridas são ambas grandes, então as estratégias de classificação frequentemente teriam que tentar ambas as descriptografias, o que seria ineficiente. Dependente da implementação.

Os clientes podem usar as mesmas chaves estáticas X25519 ou chaves diferentes para os protocolos X25519 e híbrido nos mesmos tunnels, dependendo da implementação.

#### Sigilo Futuro

A especificação ECIES permite Garlic Messages no payload da New Session Message, o que possibilita a entrega 0-RTT do pacote de streaming inicial, geralmente um HTTP GET, juntamente com o leaseset do cliente. No entanto, o payload da New Session Message não possui sigilo futuro (forward secrecy). Como esta proposta enfatiza o sigilo futuro aprimorado para ratchet, as implementações podem ou devem adiar a inclusão do payload de streaming, ou da mensagem completa de streaming, até a primeira Existing Session Message. Isso seria às custas da entrega 0-RTT. As estratégias também podem depender do tipo de tráfego ou tipo de tunnel, ou entre GET vs. POST, por exemplo. Dependente da implementação.

#### Tamanho da Nova Sessão

MLKEM, MLDSA, ou ambos no mesmo destino, aumentarão drasticamente o tamanho da New Session Message, conforme descrito acima. Isso pode diminuir significativamente a confiabilidade da entrega da New Session Message através de túneis, onde elas devem ser fragmentadas em múltiplas mensagens de túnel de 1024 bytes. O sucesso da entrega é proporcional ao número exponencial de fragmentos. Implementações podem usar várias estratégias para limitar o tamanho da mensagem, às custas da entrega 0-RTT. Dependente da implementação.

### NTCP2

Definimos o MSB da chave efêmera (key[31] & 0x80) na solicitação de sessão para indicar que esta é uma conexão híbrida. Isso nos permite executar tanto NTCP padrão quanto NTCP híbrido na mesma porta. Apenas uma variante híbrida seria suportada e anunciada no endereço do router. Por exemplo, v=2,3 ou v=2,4 ou v=2,5.

#### Ofuscação

Como Alice, para uma conexão PQ, antes da ofuscação, defina X[31] |= 0x80. Isso torna X uma chave pública X25519 inválida. Após a ofuscação, AES-CBC irá randomizá-la. O MSB de X será aleatório após a ofuscação.

Como Bob, teste se (X[31] & 0x80) != 0 após a desobfuscação. Se for o caso, é uma conexão PQ.

A versão mínima do router necessária para NTCP2-PQ está por definir.

Nota: Os códigos de tipo são apenas para uso interno. Os routers permanecerão como tipo 4, e o suporte será indicado nos endereços do router.

### SSU2

Usamos o campo de versão no cabeçalho longo e o definimos como 3 para MLKEM512 e 4 para MLKEM768. v=2,3,4 no endereço seria suficiente.

Verificar e confirmar que o SSU2 pode lidar com RI assinado com MLDSA fragmentado em múltiplos pacotes (6-8?).

Nota: Os códigos de tipo são apenas para uso interno. Os routers permanecerão como tipo 4, e o suporte será indicado nos endereços do router.

## Compatibilidade do Router

### Nomes de Transporte

Em todos os casos, use os nomes de transporte NTCP2 e SSU2 como de costume.

### Tipos de Criptografia do Router

Temos várias alternativas a considerar:

#### Routers Tipo 5/6/7

Não recomendado. Use apenas os novos transportes listados acima que correspondem ao tipo de router. Routers mais antigos não conseguem conectar, construir tunnels através, ou enviar mensagens netDb para. Levaria vários ciclos de lançamento para depurar e garantir suporte antes de habilitar por padrão. Pode estender a implantação por um ano ou mais em relação às alternativas abaixo.

#### Routers Tipo 4

Recomendado. Como PQ não afeta a chave estática X25519 ou os protocolos de handshake N, poderíamos deixar os routers como tipo 4, e apenas anunciar novos transportes. Routers mais antigos ainda poderiam conectar, construir tunnels através deles, ou enviar mensagens netDb para eles.

#### Recomendações

MLKEM-768 é recomendado para Ratchet, NTCP2 e SSU2, como o melhor equilíbrio entre segurança e comprimento de chave.

### Tipos de Assinatura do Router

#### Routers Tipo 12-17

Routers mais antigos verificam RIs e, portanto, não podem se conectar, construir tunnels através deles ou enviar mensagens netDb para eles. Levaria vários ciclos de lançamento para depurar e garantir suporte antes de habilitar por padrão. Seriam os mesmos problemas do lançamento do tipo de enc. 5/6/7; poderia estender o lançamento por um ano ou mais em relação à alternativa de lançamento do tipo de enc. tipo 4 listada acima.

Nenhuma alternativa.

### Tipos de Criptografia LS

#### Chaves LS Tipo 5-7

Estes podem estar presentes no LS com chaves X25519 do tipo 4 mais antigas. Routers mais antigos irão ignorar chaves desconhecidas.

Os destinos podem suportar múltiplos tipos de chave, mas apenas fazendo tentativas de descriptografia da mensagem 1 com cada chave. A sobrecarga pode ser mitigada mantendo contagens de descriptografias bem-sucedidas para cada chave, e tentando primeiro a chave mais usada. O Java I2P usa esta estratégia para ElGamal+X25519 no mesmo destino.

### Tipos de Assinatura de Destino

#### Destinos Tipo 12-17

Os routers verificam assinaturas de leaseSet e portanto não conseguem conectar ou receber leaseSets para destinos do tipo 12-17. Levaria vários ciclos de lançamento para depurar e garantir suporte antes de habilitar por padrão.

Sem alternativas.

## Prioridades e Implementação

Os dados mais valiosos são o tráfego ponta a ponta, criptografados com ratchet. Como um observador externo entre saltos de tunnel, isso é criptografado duas vezes mais, com criptografia de tunnel e criptografia de transporte. Como um observador externo entre OBEP e IBGW, é criptografado apenas uma vez mais, com criptografia de transporte. Como um participante OBEP ou IBGW, ratchet é a única criptografia. No entanto, como tunnels são unidirecionais, capturar ambas as mensagens no handshake ratchet exigiria routers em conluio, a menos que tunnels fossem construídos com o OBEP e IBGW no mesmo router.

O modelo de ameaça PQ mais preocupante atualmente é armazenar tráfego hoje, para descriptografia muitos anos no futuro (sigilo direto). Uma abordagem híbrida protegeria contra isso.

O modelo de ameaça PQ de quebrar as chaves de autenticação em algum período razoável de tempo (digamos alguns meses) e depois se fazer passar pela autenticação ou descriptografar em tempo quase real, está muito mais distante? E é quando gostaríamos de migrar para chaves estáticas PQC.

Então, o modelo de ameaça PQ mais antigo é OBEP/IBGW armazenando tráfego para descriptografia posterior. Devemos implementar ratchet híbrido primeiro.

Ratchet é a prioridade mais alta. Transportes são os próximos. Assinaturas são a prioridade mais baixa.

O lançamento de assinaturas também será um ano ou mais após o lançamento de criptografia, porque não é possível compatibilidade com versões anteriores. Além disso, a adoção de MLDSA na indústria será padronizada pelo CA/Browser Forum e pelas Autoridades Certificadoras. As CAs precisam primeiro de suporte de módulo de segurança de hardware (HSM), que atualmente não está disponível [CA/Browser Forum](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/). Esperamos que o CA/Browser Forum conduza as decisões sobre escolhas específicas de parâmetros, incluindo se deve apoiar ou exigir assinaturas compostas [IETF draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/).

| Marco | Objetivo |
|-------|----------|
| Ratchet beta | Final de 2025 |
| Selecionar melhor tipo enc | Início de 2026 |
| NTCP2 beta | Início de 2026 |
| SSU2 beta | Meados de 2026 |
| Ratchet produção | Meados de 2026 |
| Ratchet padrão | Final de 2026 |
| Signature beta | Final de 2026 |
| NTCP2 produção | Final de 2026 |
| SSU2 produção | Início de 2027 |
| Selecionar melhor tipo sig | Início de 2027 |
| NTCP2 padrão | Início de 2027 |
| SSU2 padrão | Meados de 2027 |
| Signature produção | Meados de 2027 |
## Migração

Se não conseguirmos suportar os protocolos de ratchet antigo e novo nos mesmos túneis, a migração será muito mais difícil.

Devemos ser capazes de simplesmente tentar um-depois-o-outro, como fizemos com X25519, para ser comprovado.

## Problemas

- Seleção de Noise Hash - manter SHA256 ou atualizar?
  SHA256 deve ser bom por mais 20-30 anos, não ameaçado por PQ,
  Veja [apresentação NIST](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf) e [apresentação NCCOE](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf).
  Se SHA256 for quebrado temos problemas piores (netDb).
- NTCP2 porta separada, endereço de router separado
- SSU2 relay / teste de peer
- Campo de versão SSU2
- Versão de endereço de router SSU2

## Referências

* [CABFORUM](https://cabforum.org/2024/10/10/2024-10-10-minutes-of-the-code-signing-certificate-working-group/)
* [Choosing-Hash](https://kerkour.com/fast-secure-hash-function-sha256-sha512-sha3-blake3)
* [CLOUDFLARE](https://blog.cloudflare.com/pq-2024/)
* [COMMON](/docs/specs/common-structures/)
* [COMPOSITE-SIGS](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/)
* [ECIES](/docs/specs/ecies/)
* [FORUM](http://zzz.i2p/topics/3294)
* [FIPS202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
* [FIPS203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)
* [FIPS204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
* [FIPS205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf)
* [MLDSA-OIDS](https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/)
* [NIST-PQ](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)
* [NIST-PQ-UPDATE](https://csrc.nist.gov/csrc/media/Presentations/2022/update-on-post-quantum-encryption-and-cryptographi/Day%202%20-%20230pm%20Chen%20PQC%20ISPAB.pdf)
* [NIST-PQ-END](https://www.nccoe.nist.gov/sites/default/files/2023-08/pqc-light-at-the-end-of-the-tunnel-presentation.pdf)
* [NIST-VECTORS](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values)
* [Noise](https://noiseprotocol.org/noise.html)
* [Noise-Hybrid](https://github.com/noiseprotocol/noise_hfs_spec/blob/master/output/noise_hfs.pdf)
* [NSA-PQ](https://media.defense.gov/2022/Sep/07/2003071836/-1/-1/0/CSI_CNSA_2.0_FAQ_.PDF)
* [NTCP2](/docs/specs/ntcp2/)
* [OPENSSL](https://openssl-library.org/post/2025-02-04-release-announcement-3.5/)
* [Prop165](/docs/proposals/165/)
* [PQ-WIREGUARD](https://eprint.iacr.org/2020/379.pdf)
* [RFC-2104](https://tools.ietf.org/html/rfc2104)
* [Rosenpass](https://rosenpass.eu/)
* [Rosenpass-Whitepaper](https://raw.githubusercontent.com/rosenpass/rosenpass/papers-pdf/whitepaper.pdf)
* [SSH-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-sshm-mlkem-hybrid-kex/)
* [SSU2](/docs/specs/ssu2/)
* [TLS-HYBRID](https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/)
