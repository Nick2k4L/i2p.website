---
title: "Especificação de LeaseSet Criptografado"
description: "Ofuscação, criptografia e descriptografia de leasesets criptografados"
slug: "encryptedleaseset"
category: "Protocolos"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Visão Geral

Este documento especifica o mascaramento, criptografia e descriptografia de leasesets criptografados. Para a estrutura do leaseset criptografado, consulte a [especificação de estruturas comuns](/docs/specs/common-structures). Para informações sobre leasesets criptografados, consulte a [proposta 123](/proposals/123-new-netdb-entries). Para uso no netdb, consulte a documentação do netdb.

### Definições

Definimos as seguintes funções correspondentes aos blocos de construção criptográficos utilizados para LS2 criptografado:

**CSRNG(n)** : saída de n bytes de um gerador de números aleatórios criptograficamente seguro.

Além do requisito de que o CSRNG seja criptograficamente seguro (e, portanto, adequado para gerar material de chave), ele DEVE ser seguro para que uma saída de n bytes seja usada como material de chave quando as sequências de bytes imediatamente anteriores e posteriores forem expostas na rede (como em um salt ou preenchimento criptografado). Implementações que dependem de uma fonte potencialmente não confiável devem fazer hash de qualquer saída que será exposta na rede [PRNG-REFS](http://projectbullrun.org/dual-ec/ext-rand.html).

**H(p, d)** : função hash SHA-256 que recebe uma string de personalização p e dados d, e produz uma saída de 32 bytes de comprimento.

Use SHA-256 da seguinte forma:

```
H(p, d) := SHA-256(p || d)
```
**STREAM** : A cifra de fluxo ChaCha20 conforme especificado em [RFC-7539-S2.4](https://tools.ietf.org/html/rfc7539#section-2.4), com o contador inicial definido como 1. S_KEY_LEN = 32 e S_IV_LEN = 12.

- **ENCRYPT(k, iv, plaintext)** : Criptografa o texto simples usando a chave de cifra k, e o nonce iv que DEVE ser único para a chave k. Retorna um texto cifrado que tem o mesmo tamanho do texto simples. Todo o texto cifrado deve ser indistinguível de dados aleatórios se a chave for secreta.

- **DECRYPT(k, iv, ciphertext)** : Descriptografa o texto cifrado usando a chave de cifra k e o nonce iv. Retorna o texto simples.

**SIG** : O esquema de assinatura Red25519 (correspondente ao SigType 11) com key blinding. Possui as seguintes funções:

- **DERIVE_PUBLIC(privkey)** : Retorna a chave pública correspondente à chave privada fornecida.

- **SIGN(privkey, m)** : Retorna uma assinatura pela chave privada privkey sobre a mensagem dada m.

- **VERIFY(pubkey, m, sig)** : Verifica a assinatura sig contra a chave pública pubkey e mensagem m. Retorna verdadeiro se a assinatura for válida, falso caso contrário.

Também deve suportar as seguintes operações de ofuscação de chave:

- **GENERATE_ALPHA(data, secret)** : Gerar alpha para aqueles que conhecem os dados e um segredo opcional. O resultado deve ser distribuído de forma idêntica às chaves privadas.

- **BLIND_PRIVKEY(privkey, alpha)** : Oculta uma chave privada, usando um alpha secreto.

- **BLIND_PUBKEY(pubkey, alpha)** : Oculta uma chave pública, usando um alpha secreto. Para um determinado par de chaves (privkey, pubkey) a seguinte relação se mantém:

```
BLIND_PUBKEY(pubkey, alpha) ==
DERIVE_PUBLIC(BLIND_PRIVKEY(privkey, alpha))
```
**DH** : Sistema de acordo de chave pública X25519. Chaves privadas de 32 bytes, chaves públicas de 32 bytes, produz saídas de 32 bytes. Tem as seguintes funções:

- **GENERATE_PRIVATE()** : Gera uma nova chave privada.

- **DERIVE_PUBLIC(privkey)** : Retorna a chave pública correspondente à chave privada fornecida.

- **DH(privkey, pubkey)** : Gera um segredo compartilhado a partir das chaves privada e pública fornecidas.

**HKDF(salt, ikm, info, n)** : Uma função criptográfica de derivação de chaves que recebe algum material de chave de entrada ikm (que deve ter boa entropia, mas não precisa ser uma string uniformemente aleatória), um salt de 32 bytes de comprimento, e um valor 'info' específico do contexto, e produz uma saída de n bytes adequada para uso como material de chave.

Use HKDF conforme especificado em [RFC-5869](https://tools.ietf.org/html/rfc5869), usando a função hash HMAC SHA-256 conforme especificado em [RFC-2104](https://tools.ietf.org/html/rfc2104). Isso significa que SALT_LEN é de no máximo 32 bytes.

### Formato

O formato LS2 criptografado consiste em três camadas aninhadas:

- Uma camada externa contendo as informações de texto simples necessárias para armazenamento e recuperação.
- Uma camada intermediária que lida com a autenticação do cliente.
- Uma camada interna que contém os dados reais do LS2.

O formato geral é assim:

```
Layer 0 data + Enc(layer 1 data + Enc(layer 2 data)) + Signature
```
Note que o LS2 criptografado é blinded (ofuscado). O Destination não está no cabeçalho. A localização de armazenamento DHT é SHA-256(tipo de assinatura || chave pública blinded), e rotacionada diariamente.

NÃO usa o cabeçalho LS2 padrão especificado acima.

#### Camada 0 (externa)

**Tipo** : 1 byte

Na verdade não está no cabeçalho, mas faz parte dos dados cobertos pela assinatura. Obter do campo na Mensagem de Armazenamento de Base de Dados.

**Tipo de Assinatura da Chave Pública Cegada** : 2 bytes, big endian

Isto será sempre tipo 11, identificando uma chave cega Red25519.

**Chave Pública Cegada** : Comprimento conforme implícito pelo tipo de assinatura

**Timestamp de publicação** : 4 bytes, big endian

Segundos desde a época, reinicia em 2106

**Expires** : 2 bytes, big endian

Deslocamento do timestamp publicado em segundos, máximo de 18,2 horas

**Flags** : 2 bytes

Ordem dos bits: 15 14 ... 3 2 1 0

- Bit 0: Se 0, sem chaves offline; se 1, chaves offline
- Outros bits: definidos como 0 para compatibilidade com usos futuros

**Dados de chave transitória** : Presente se a flag indicar chaves offline

- **Timestamp de expiração** : 4 bytes, big endian. Segundos desde epoch, reinicia em 2106
- **Tipo de assinatura transiente** : 2 bytes, big endian
- **Chave pública de assinatura transiente** : Comprimento conforme implícito pelo tipo de assinatura
- **Assinatura** : Comprimento conforme implícito pelo tipo de assinatura da chave pública cegada. Sobre timestamp de expiração, tipo de assinatura transiente e chave pública transiente. Verificada com a chave pública cegada.

**lenOuterCiphertext** : 2 bytes, big endian

**outerCiphertext** : lenOuterCiphertext bytes

Dados criptografados da camada 1. Veja abaixo para algoritmos de derivação de chave e criptografia.

**Assinatura** : Comprimento conforme implícito pelo tipo de assinatura da chave de assinatura utilizada

A assinatura é de tudo acima. Se a flag indica chaves offline, a assinatura é verificada com a chave pública transitória. Caso contrário, a assinatura é verificada with a chave pública ofuscada.

#### Camada 1 (meio)

**Flags** : 1 byte

Ordem dos bits: 76543210

- Bit 0: 0 para todos, 1 para por-cliente, seção de autenticação a seguir
- Bits 3-1: Esquema de autenticação, apenas se o bit 0 estiver definido como 1 para por-cliente, caso contrário 000
  - 000: Autenticação de cliente DH (ou nenhuma autenticação por-cliente)
  - 001: Autenticação de cliente PSK
- Bits 7-4: Não utilizados, definir como 0 para compatibilidade futura

**Dados de autenticação de cliente DH** : Presente se o bit de flag 0 estiver definido como 1 e os bits de flag 3-1 estiverem definidos como 000.

- **ephemeralPublicKey** : 32 bytes
- **clients** : 2 bytes, big endian. Número de entradas authClient a seguir, 40 bytes cada
- **authClient** : Dados de autorização para um único cliente. Veja abaixo o algoritmo de autorização por cliente.
  - **clientID_i** : 8 bytes
  - **clientCookie_i** : 32 bytes

**Dados de autenticação do cliente PSK** : Presente se o bit de flag 0 estiver definido como 1 e os bits de flag 3-1 estiverem definidos como 001.

- **authSalt** : 32 bytes
- **clients** : 2 bytes, big endian. Número de entradas authClient a seguir, 40 bytes cada
- **authClient** : Dados de autorização para um único cliente. Veja abaixo o algoritmo de autorização por cliente.
  - **clientID_i** : 8 bytes
  - **clientCookie_i** : 32 bytes

**innerCiphertext** : Comprimento implícito por lenOuterCiphertext (quaisquer dados restantes)

Dados criptografados da camada 2. Veja abaixo os algoritmos de derivação de chave e criptografia.

#### Camada 2 (interna)

**Tipo** : 1 byte

Ou 3 (LS2) ou 7 (Meta LS2)

**Dados** : Dados do LeaseSet2 para o tipo fornecido.

Inclui o cabeçalho e a assinatura.

### Derivação de Chave de Ofuscamento

Utilizamos o seguinte esquema para ocultação de chaves, baseado no Ed25519 e ZCash RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf). As assinaturas Red25519 são sobre a curva Ed25519, usando SHA-512 para o hash.

Não utilizamos o apêndice A.2 do rend-spec-v3.txt do Tor [TOR-REND-SPEC-V3](https://spec.torproject.org/rend-spec-v3), que possui objetivos de design similares, porque suas chaves públicas cegas podem estar fora do subgrupo de ordem prima, com implicações de segurança desconhecidas.

#### Objetivos

- A chave pública de assinatura no destino não ofuscado deve ser Ed25519 (tipo de assinatura 7) ou Red25519 (tipo de assinatura 11); nenhum outro tipo de assinatura é suportado
- Se a chave pública de assinatura estiver offline, a chave pública de assinatura transitória também deve ser Ed25519
- A ofuscação é computacionalmente simples
- Usa primitivos criptográficos existentes
- Chaves públicas ofuscadas não podem ser desofuscadas
- Chaves públicas ofuscadas devem estar na curva Ed25519 e no subgrupo de ordem prima
- Deve conhecer a chave pública de assinatura do destino (destino completo não é necessário) para derivar a chave pública ofuscada
- Opcionalmente, fornecer um segredo adicional necessário para derivar a chave pública ofuscada

#### Segurança

A segurança de um esquema de blinding requer que a distribuição de alpha seja a mesma das chaves privadas não blindadas. No entanto, quando blindamos uma chave privada Ed25519 (sig type 7) para uma chave privada Red25519 (sig type 11), a distribuição é diferente. Para atender aos requisitos da seção 4.1.6.1 do zcash [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf), Red25519 (sig type 11) deveria ser usado para as chaves não blindadas também, para que "a combinação de uma chave pública re-randomizada e assinatura(s) sob essa chave não revele a chave da qual foi re-randomizada." Permitimos o type 7 para destinos existentes, mas recomendamos o type 11 para novos destinos que serão criptografados.

#### Definições

**B** : O ponto base (gerador) Ed25519 2^255 - 19 como em [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)

**L** : A ordem Ed25519 2^252 + 27742317777372353535851937790883648493 como em [ED25519-REFS](http://cr.yp.to/papers.html#ed25519)

**DERIVE_PUBLIC(a)** : Converter uma chave privada para pública, como em Ed25519 (multiplicar por G)

**alpha** : Um número aleatório de 32 bytes conhecido por aqueles que conhecem o destino.

**GENERATE_ALPHA(destination, date, secret)** : Gera alpha para a data atual, para aqueles que conhecem o destino e o segredo. O resultado deve ser distribuído de forma idêntica às chaves privadas Ed25519.

**a** : A chave privada de assinatura EdDSA ou RedDSA de 32 bytes não cegada usada para assinar o destino

**A** : A chave pública de assinatura EdDSA ou RedDSA não cegada de 32 bytes no destino, = DERIVE_PUBLIC(a), como em Ed25519

**a'** : A chave privada de assinatura EdDSA cegada de 32 bytes usada para assinar o leaseset criptografado. Esta é uma chave privada EdDSA válida.

**A'** : A chave pública de assinatura EdDSA cegada de 32 bytes no Destination, pode ser gerada com DERIVE_PUBLIC(a'), ou a partir de A e alpha. Esta é uma chave pública EdDSA válida, na curva e no subgrupo de ordem prima.

**LEOS2IP(x)** : Inverter a ordem dos bytes de entrada para little-endian

**H\*(x)** : 32 bytes = (LEOS2IP(SHA512(x))) mod B, o mesmo que no hash-and-reduce do Ed25519

#### Cálculos de Blinding

Um novo alfa secreto e chaves cegas devem ser geradas a cada dia (UTC).

O alpha secreto e as chaves cegas são calculados da seguinte forma:

GENERATE_ALPHA(destino, data, segredo), para todas as partes:

```
// secret is optional, else zero-length
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of blinded public key A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
datestring = 8 bytes ASCII YYYYMMDD from the current date UTC
secret = UTF-8 encoded string
seed = HKDF(H("I2PGenerateAlpha", keydata), datestring || secret, "i2pblinding1", 64)
// treat seed as a 64 byte little-endian value
alpha = seed mod L
```
BLIND_PRIVKEY(), para o proprietário publicando o leaseset:

```
alpha = GENERATE_ALPHA(destination, date, secret)
// If for a Ed25519 private key (type 7)
seed = destination's signing private key
a = left half of SHA512(seed) and clamped as usual for Ed25519
// else for a Red25519 private key (type 11)
a = destination's signing private key
// Addition using scalar arithmetic
blinded signing private key = a' = BLIND_PRIVKEY(a, alpha) = (a + alpha) mod L
blinded signing public key = A' = DERIVE_PUBLIC(a')
```
BLIND_PUBKEY(), para os clientes que recuperam o leaseset:

```
alpha = GENERATE_ALPHA(destination, date, secret)
A = destination's signing public key
// Addition using group elements (points on the curve)
blinded public key = A' = BLIND_PUBKEY(A, alpha) = A + DERIVE_PUBLIC(alpha)
```
Ambos os métodos de calcular A' produzem o mesmo resultado, conforme exigido.

#### Assinatura

O leaseSet não-cego é assinado pela chave privada de assinatura Ed25519 ou Red25519 não-cega e verificado com a chave pública de assinatura Ed25519 ou Red25519 não-cega (tipos de assinatura 7 ou 11) como de costume.

Se a chave pública de assinatura estiver offline, o leaseset não cegado é assinado pela chave privada de assinatura transitória Ed25519 ou Red25519 não cegada e verificado com a chave pública de assinatura transitória Ed25519 ou Red25519 não cegada (tipos de assinatura 7 ou 11) como de costume. Veja abaixo as notas adicionais sobre chaves offline para leasesets criptografados.

Para a assinatura do leaseset criptografado, usamos Red25519 baseado em RedDSA [ZCASH](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf) para assinar e verificar com chaves ofuscadas. As assinaturas Red25519 são sobre a curva Ed25519, usando SHA-512 para o hash.

Red25519 é semelhante ao Ed25519 padrão exceto conforme especificado abaixo.

#### Cálculos de Assinatura/Verificação

A parte externa do leaseset criptografado usa chaves e assinaturas Red25519.

Red25519 é semelhante ao Ed25519. Existem duas diferenças:

As chaves privadas Red25519 são geradas a partir de números aleatórios e então devem ser reduzidas mod L, onde L é definido acima. As chaves privadas Ed25519 são geradas a partir de números aleatórios e então "grampeadas" usando mascaramento bitwise nos bytes 0 e 31. Isso não é feito para Red25519. As funções GENERATE_ALPHA() e BLIND_PRIVKEY() definidas acima geram chaves privadas Red25519 adequadas usando mod L.

No Red25519, o cálculo de r para assinatura utiliza dados aleatórios adicionais e usa o valor da chave pública em vez do hash da chave privada. Devido aos dados aleatórios, cada assinatura Red25519 é diferente, mesmo ao assinar os mesmos dados com a mesma chave.

```
Signing:
  T = 80 random bytes
  r = H*(T || publickey || message)
  (rest is the same as in Ed25519)

Verification:
  Same as for Ed25519
```
### Criptografia e processamento

#### Derivação de subcredenciais

Como parte do processo de ocultação, precisamos garantir que um LS2 criptografado só possa ser descriptografado por alguém que conheça a chave pública de assinatura do Destination correspondente. O Destination completo não é necessário. Para conseguir isso, derivamos uma credencial da chave pública de assinatura:

```
A = destination's signing public key
stA = signature type of A, 2 bytes big endian (0x0007 or 0x000b)
stA' = signature type of A', 2 bytes big endian (0x000b)
keydata = A || stA || stA'
credential = H("credential", keydata)
```
A string de personalização garante que a credencial não colida com qualquer hash usado como chave de busca DHT, como o hash de Destination simples.

Para uma determinada chave ofuscada, podemos então derivar uma subcredencial:

```
subcredential = H("subcredential", credential || blindedPublicKey)
```
A subcredencial é incluída nos processos de derivação de chave abaixo, que vincula essas chaves ao conhecimento da chave pública de assinatura do Destination.

#### Criptografia da Camada 1

Primeiro, a entrada para o processo de derivação de chave é preparada:

```
outerInput = subcredential || publishedTimestamp
```
Em seguida, um salt aleatório é gerado:

```
outerSalt = CSRNG(32)
```
Em seguida, a chave usada para criptografar a camada 1 é derivada:

```
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Finalmente, o texto simples da camada 1 é criptografado e serializado:

```
outerCiphertext = outerSalt || ENCRYPT(outerKey, outerIV, outerPlaintext)
```
#### Descriptografia da Camada 1

O salt é analisado a partir do texto cifrado da camada 1:

```
outerSalt = outerCiphertext[0:31]
```
Então a chave usada para criptografar a camada 1 é derivada:

```
outerInput = subcredential || publishedTimestamp
keys = HKDF(outerSalt, outerInput, "ELS2_L1K", 44)
outerKey = keys[0:31]
outerIV = keys[32:43]
```
Finalmente, o texto cifrado da camada 1 é descriptografado:

```
outerPlaintext = DECRYPT(outerKey, outerIV, outerCiphertext[32:end])
```
#### Criptografia da Camada 2

Quando a autorização do cliente está habilitada, `authCookie` é calculado como descrito abaixo. Quando a autorização do cliente está desabilitada, `authCookie` é o array de bytes de comprimento zero.

A criptografia prossegue de forma similar à camada 1:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = CSRNG(32)
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerCiphertext = innerSalt || ENCRYPT(innerKey, innerIV, innerPlaintext)
```
#### Descriptografia da Camada 2

Quando a autorização de cliente está habilitada, `authCookie` é calculado conforme descrito abaixo. Quando a autorização de cliente está desabilitada, `authCookie` é o array de bytes de comprimento zero.

A descriptografia procede de forma semelhante à camada 1:

```
innerInput = authCookie || subcredential || publishedTimestamp
innerSalt = innerCiphertext[0:31]
keys = HKDF(innerSalt, innerInput, "ELS2_L2K", 44)
innerKey = keys[0:31]
innerIV = keys[32:43]
innerPlaintext = DECRYPT(innerKey, innerIV, innerCiphertext[32:end])
```
### Autorização por cliente

Quando a autorização de cliente está habilitada para um Destination, o servidor mantém uma lista de clientes que estão sendo autorizados a descriptografar os dados LS2 criptografados. Os dados armazenados por cliente dependem do mecanismo de autorização e incluem alguma forma de material de chave que cada cliente gera e envia ao servidor através de um mecanismo seguro fora da banda.

Existem duas alternativas para implementar autorização por cliente:

#### Autorização de cliente DH

Cada cliente gera um par de chaves DH `[csk_i, cpk_i]`, e envia a chave pública `cpk_i` para o servidor.

##### Processamento do servidor

O servidor gera um novo `authCookie` e um par de chaves DH efêmero:

```
authCookie = CSRNG(32)
esk = GENERATE_PRIVATE()
epk = DERIVE_PUBLIC(esk)
```
Em seguida, para cada cliente autorizado, o servidor criptografa `authCookie` para sua chave pública:

```
sharedSecret = DH(esk, cpk_i)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
O servidor coloca cada tupla `[clientID_i, clientCookie_i]` na camada 1 do LS2 criptografado, junto com `epk`.

##### Processamento do cliente

O cliente usa sua chave privada para derivar seu identificador de cliente esperado `clientID_i`, chave de criptografia `clientKey_i`, e IV de criptografia `clientIV_i`:

```
sharedSecret = DH(csk_i, epk)
authInput = sharedSecret || cpk_i || subcredential || publishedTimestamp
okm = HKDF(epk, authInput, "ELS2_XCA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Então o cliente busca nos dados de autorização da camada 1 por uma entrada que contenha `clientID_i`. Se uma entrada correspondente existir, o cliente a descriptografa para obter `authCookie`:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Autorização de cliente com chave pré-compartilhada

Cada cliente gera uma chave secreta de 32 bytes `psk_i`, e a envia para o servidor. Alternativamente, o servidor pode gerar a chave secreta e enviá-la para um ou mais clientes.

##### Processamento do servidor

O servidor gera um novo `authCookie` e salt:

```
authCookie = CSRNG(32)
authSalt = CSRNG(32)
```
Então, para cada cliente autorizado, o servidor criptografa `authCookie` para sua chave pré-compartilhada:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
clientCookie_i = ENCRYPT(clientKey_i, clientIV_i, authCookie)
```
O servidor coloca cada tupla `[clientID_i, clientCookie_i]` na camada 1 do LS2 criptografado, junto com `authSalt`.

##### Processamento do cliente

O cliente usa sua chave pré-compartilhada para derivar seu identificador de cliente esperado `clientID_i`, chave de criptografia `clientKey_i`, e IV de criptografia `clientIV_i`:

```
authInput = psk_i || subcredential || publishedTimestamp
okm = HKDF(authSalt, authInput, "ELS2PSKA", 52)
clientKey_i = okm[0:31]
clientIV_i = okm[32:43]
clientID_i = okm[44:51]
```
Em seguida, o cliente pesquisa os dados de autorização da camada 1 por uma entrada que contenha `clientID_i`. Se uma entrada correspondente existir, o cliente a descriptografa para obter `authCookie`:

```
authCookie = DECRYPT(clientKey_i, clientIV_i, clientCookie_i)
```
#### Considerações de segurança

Ambos os mecanismos de autorização de cliente acima fornecem privacidade para a associação de clientes. Uma entidade que conhece apenas o Destination pode ver quantos clientes estão inscritos a qualquer momento, mas não pode rastrear quais clientes estão sendo adicionados ou revogados.

Servidores DEVEM randomizar a ordem dos clientes cada vez que geram um LS2 criptografado, para impedir que os clientes descubram sua posição na lista e infiram quando outros clientes foram adicionados ou revogados.

Um servidor PODE escolher ocultar o número de clientes que estão subscritos inserindo entradas aleatórias na lista de dados de autorização.

##### Vantagens da autorização de cliente DH

- A segurança do esquema não depende exclusivamente da troca fora de banda do material de chave do cliente. A chave privada do cliente nunca precisa sair do seu dispositivo, e assim um adversário que conseguir interceptar a troca fora de banda, mas não conseguir quebrar o algoritmo DH, não pode descriptografar o LS2 criptografado, ou determinar por quanto tempo o cliente tem acesso concedido.

##### Desvantagens da autorização de cliente DH

- Requer N + 1 operações DH no lado do servidor para N clientes.
- Requer uma operação DH no lado do cliente.
- Requer que o cliente gere a chave secreta.

##### Vantagens da autorização de cliente PSK

- Não requer operações DH.
- Permite que o servidor gere a chave secreta.
- Permite que o servidor compartilhe a mesma chave com múltiplos clientes, se desejado.

##### Desvantagens da autorização de cliente PSK

- A segurança do esquema depende criticamente da troca fora de banda do material de chave do cliente. Um adversário que intercepte a troca para um cliente específico pode descriptografar qualquer LS2 criptografado subsequente para o qual esse cliente esteja autorizado, além de determinar quando o acesso do cliente é revogado.

### LS Criptografado com Endereços Base 32

Você não pode usar um endereço base 32 tradicional para um LS2 criptografado, pois ele contém apenas o hash do destino. Ele não fornece a chave pública não-ofuscada. Portanto, um endereço base 32 sozinho é insuficiente. O cliente precisa ou do destino completo (que contém a chave pública), ou da própria chave pública. Se o cliente tiver o destino completo em um catálogo de endereços, e o catálogo de endereços suportar busca reversa por hash, então a chave pública pode ser recuperada.

Então precisamos de um novo formato que coloque a chave pública em vez do hash em um endereço base32. Este formato também deve conter o tipo de assinatura da chave pública e o tipo de assinatura do esquema de ofuscação. Os requisitos totais são 32 + 3 = 35 bytes, necessitando 56 caracteres em base 32, ou mais para tipos de chave pública mais longos.

```
data = ((1 byte flags || 1 byte unblinded sigtype || 1 byte blinded sigtype) XOR checksum) || 32 byte pubkey
address = Base32Encode(data) || ".b32.i2p"
```
Usamos o mesmo sufixo ".b32.i2p" como para endereços base 32 tradicionais. Endereços para leaseSets criptografados são identificados pelos 56 caracteres codificados (35 bytes decodificados), comparado aos 52 caracteres (32 bytes) para endereços base 32 tradicionais. Os cinco bits não utilizados no final do b32 devem ser 0.

Você não pode usar um LS2 criptografado para bittorrent, devido às respostas de anúncio compactas que têm 32 bytes. Os 32 bytes contêm apenas o hash. Não há espaço para uma indicação de que o leaseset está criptografado, ou os tipos de assinatura.

Consulte a [especificação de nomenclatura](/docs/specs/naming) ou [proposta 149](/proposals/149-b32-encrypted-ls2) para mais informações sobre o novo formato.

### leaseSet Criptografado com Chaves Offline

Para leaseSets criptografados com chaves offline, as chaves privadas cegas também devem ser geradas offline, uma para cada dia.

Como o bloco de assinatura offline opcional está na parte de texto legível do leaseset criptografado, qualquer pessoa coletando dados dos floodfills poderia usar isso para rastrear o leaseset (mas não descriptografá-lo) ao longo de vários dias. Para prevenir isso, o proprietário das chaves também deveria gerar novas chaves transitórias para cada dia. Tanto as chaves transitórias quanto as chaves cegas podem ser geradas com antecedência e entregues ao router em lote.

Não há formato de arquivo definido para empacotar múltiplas chaves transitórias e cegas e fornecê-las ao cliente ou router. Não há melhoria do protocolo I2CP definida para suportar leaseSets criptografados com chaves offline.

### Notas

- Um serviço usando leasesets criptografados publicaria a versão criptografada para os floodfills. No entanto, para eficiência, enviaria leasesets não criptografados para clientes na mensagem garlic encapsulada, uma vez autenticados (via lista de permissões, por exemplo).
- Floodfills podem limitar o tamanho máximo a um valor razoável para prevenir abuso.
- Após a descriptografia, várias verificações devem ser feitas, incluindo que o timestamp interno e a expiração coincidam com aqueles no nível superior.
- ChaCha20 foi selecionado ao invés do AES. Embora as velocidades sejam similares se o suporte de hardware AES estiver disponível, ChaCha20 é 2,5-3x mais rápido quando o suporte de hardware AES não está disponível, como em dispositivos ARM de menor capacidade.

## Referências

- **[ED25519-REFS]** "High-speed high-security signatures" por Daniel J. Bernstein, Niels Duif, Tanja Lange, Peter Schwabe, e Bo-Yin Yang. [http://cr.yp.to/papers.html#ed25519](http://cr.yp.to/papers.html#ed25519)
- **[KEYBLIND-PROOF]** [https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html](https://lists.torproject.org/pipermail/tor-dev/2013-December/005943.html)
- **[KEYBLIND-REFS]** [https://trac.torproject.org/projects/tor/ticket/8106](https://trac.torproject.org/projects/tor/ticket/8106) e [https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html](https://lists.torproject.org/pipermail/tor-dev/2012-September/004026.html)
- **[PRNG-REFS]** [http://projectbullrun.org/dual-ec/ext-rand.html](http://projectbullrun.org/dual-ec/ext-rand.html) e [https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html](https://lists.torproject.org/pipermail/tor-dev/2015-November/009954.html)
- **[RFC-2104]** [https://tools.ietf.org/html/rfc2104](https://tools.ietf.org/html/rfc2104)
- **[RFC-4880-S5.1]** [https://tools.ietf.org/html/rfc4880#section-5.1](https://tools.ietf.org/html/rfc4880#section-5.1)
- **[RFC-5869]** [https://tools.ietf.org/html/rfc5869](https://tools.ietf.org/html/rfc5869)
- **[RFC-7539-S2.4]** [https://tools.ietf.org/html/rfc7539#section-2.4](https://tools.ietf.org/html/rfc7539#section-2.4)
- **[TOR-REND-SPEC-V3]** [https://spec.torproject.org/rend-spec-v3](https://spec.torproject.org/rend-spec-v3)
- **[ZCASH]** [https://github.com/zcash/zips/tree/master/protocol/protocol.pdf](https://github.com/zcash/zips/tree/master/protocol/protocol.pdf)
