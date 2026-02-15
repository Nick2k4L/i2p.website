---
title: "B32 para LeaseSet Criptografados"
description: "Formato de endereço Base 32 para leasesets LS2 criptografados"
slug: "b32encrypted"
aliases:
  - "/pt/docs/specs/b32-for-encrypted-leasesets"
  - "/pt/docs/specs/b32-for-encrypted-leasesets/"
category: "Design"
lastUpdated: "2020-08"
accurateFor: "0.9.47"
---

## Visão Geral

Endereços Base 32 padrão ("b32") contêm o hash do destino. Isso não funcionará para ls2 criptografado (proposta 123).

Não podemos usar um endereço base 32 tradicional para um LS2 criptografado (proposta 123), pois contém apenas o hash do destino. Não fornece a chave pública não-cega. Os clientes devem conhecer a chave pública do destino, o tipo de assinatura, o tipo de assinatura cega e uma chave secreta ou privada opcional para buscar e descriptografar o leaseset. Portanto, um endereço base 32 sozinho é insuficiente. O cliente precisa do destino completo (que contém a chave pública) ou da chave pública por si só. Se o cliente tiver o destino completo em um livro de endereços, e o livro de endereços suportar busca reversa por hash, então a chave pública pode ser recuperada.

Este formato coloca a chave pública em vez do hash em um endereço base32. Este formato também deve conter o tipo de assinatura da chave pública e o tipo de assinatura do esquema de ofuscação.

Este documento especifica um formato b32 para esses endereços. Embora tenhamos nos referido a este novo formato durante as discussões como um endereço "b33", o novo formato real mantém o sufixo usual ".b32.i2p".

## Design

- O novo formato conterá a chave pública não-cega, tipo de assinatura não-cega,
  e tipo de assinatura cega.
- Opcionalmente conter uma chave secreta e/ou privada, apenas para links privados
- Usar o sufixo ".b32.i2p" existente, mas com um comprimento maior.
- Adicionar um checksum.
- Endereços para leaseSets criptografados são identificados por 56 ou mais
  caracteres codificados (35 ou mais bytes decodificados), comparado a 52 caracteres (32
  bytes) para endereços base 32 tradicionais.

## Especificação

### Criação e codificação

Construa um nome de host de {56+ caracteres}.b32.i2p (35+ caracteres em binário) da seguinte forma:

```
flag (1 byte)
    bit 0: 0 for one-byte sigtypes, 1 for two-byte sigtypes
    bit 1: 0 for no secret, 1 if secret is required
    bit 2: 0 for no per-client auth, 1 if client private key is required
    bits 7-3: Unused, set to 0

public key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

blinded key sigtype (1 or 2 bytes as indicated in flags)
    If 1 byte, the upper byte is assumed zero

public key
    Number of bytes as implied by sigtype
```
Pós-processamento e checksum:

```
Construct the binary data as above.
Treat checksum as little-endian.
Calculate checksum = CRC-32(data[3:end])
data[0] ^= (byte) checksum
data[1] ^= (byte) (checksum >> 8)
data[2] ^= (byte) (checksum >> 16)

hostname = Base32.encode(data) || ".b32.i2p"
```
Quaisquer bits não utilizados no final do b32 devem ser 0. Não há bits não utilizados para um endereço padrão de 56 caracteres (35 bytes).

### Decodificação e Verificação

```
strip the ".b32.i2p" from the hostname
data = Base32.decode(hostname)
Calculate checksum = CRC-32(data[3:end])
Treat checksum as little-endian.
flags = data[0] ^ (byte) checksum
if 1 byte sigtypes:
    pubkey sigtype = data[1] ^ (byte) (checksum >> 8)
    blinded sigtype = data[2] ^ (byte) (checksum >> 16)
else (2 byte sigtypes):
    pubkey sigtype = data[1] ^ ((byte) (checksum >> 8)) || data[2] ^ ((byte) (checksum >> 16))
    blinded sigtype = data[3] || data[4]
parse the remainder based on the flags to get the public key
```
### Bits de Chave Secreta e Privada

Os bits de chave secreta e privada são usados para indicar aos clientes, proxies ou outros códigos do lado do cliente que a chave secreta e/ou privada será necessária para descriptografar o leaseset. Implementações específicas podem solicitar ao usuário que forneça os dados necessários, ou rejeitar tentativas de conexão se os dados necessários estiverem ausentes.

## Cache

Embora esteja fora do escopo desta especificação, os routers e/ou clientes devem lembrar e armazenar em cache (provavelmente de forma persistente) o mapeamento da chave pública para o destino, e vice-versa.

## Notas

- Distinguir versões antigas das novas pelo comprimento. Endereços b32 antigos são
  sempre {52 caracteres}.b32.i2p. Os novos são {56+ caracteres}.b32.i2p
- Thread de discussão do Tor:
  https://lists.torproject.org/pipermail/tor-dev/2017-January/011816.html
- Não espere que sigtypes de 2 bytes aconteçam, estamos apenas no 13. Não há
  necessidade de implementar agora.
- O novo formato pode ser usado em jump links (e servido por jump servers) se
  desejado, assim como o b32.

## Referências

- [CRC-32](https://en.wikipedia.org/wiki/CRC-32) - veja também [RFC 3309](https://tools.ietf.org/html/rfc3309)
