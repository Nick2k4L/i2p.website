---
title: "SAM V3"
description: "Protocolo de Mensagens Anônimas Simples para aplicações I2P não-Java"
slug: "samv3"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

SAM é um protocolo cliente simples para interagir com I2P. SAM é o protocolo recomendado para aplicações não-Java se conectarem à rede I2P, e é suportado por múltiplas implementações de router. Aplicações Java devem usar as APIs de streaming ou I2CP diretamente.

SAMv3 foi introduzido na versão 0.7.3 do I2P (maio de 2009) e é uma interface estável e suportada. A versão 3.1 também é estável e suporta a opção de tipo de assinatura, que é altamente recomendada. Versões 3.x mais recentes suportam recursos avançados. Note que o i2pd atualmente não suporta a maioria dos recursos das versões 3.2 e 3.3.

Alternativas: [SOCKS](/docs/api/socks), [Streaming](/docs/api/streaming), [I2CP](/docs/protocol/i2cp), [BOB (descontinuado)](/docs/api/bob). Versões descontinuadas: [SAM V1](/docs/api/sam), [SAM V2](/docs/api/samv2).

## Bibliotecas SAM Conhecidas

Aviso: Alguns destes podem ser muito antigos ou não suportados. Nenhum é testado, revisado ou mantido pelo projeto I2P, salvo indicação em contrário abaixo. Faça sua própria pesquisa.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Library Name</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Language</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">Version</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">STREAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">DGRAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">RAW</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Site</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2psam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++, C wrapper</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2psam">github.com/i2p/i2psam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">gosam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/goSam">github.com/eyedeekay/goSam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">sam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/sam3">github.com/eyedeekay/sam3</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">onramp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/onramp">github.com/eyedeekay/onramp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">txi2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/str4d/txi2p">github.com/str4d/txi2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.socket</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/majestrate/i2p.socket">github.com/majestrate/i2p.socket</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/l-n-s/i2plib">github.com/l-n-s/i2plib</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib-fork</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://codeberg.org/weko/i2plib-fork">codeberg.org/weko/i2plib-fork</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Py2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://i2pgit.org/robin/Py2p">i2pgit.org/robin/Py2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-rs</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2p-rs">github.com/i2p/i2p-rs</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">libsam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/libsam3">github.com/i2p/libsam3</a><br>(Maintained by the I2P project)</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">mooni2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Lua</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://notabug.org/villain/mooni2p">notabug.org/villain/mooni2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">haskell-network-anonymous-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Haskell</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/solatis/haskell-network-anonymous-i2p">github.com/solatis/haskell-network-anonymous-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-sam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Javascript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://codeberg.org/diva.exchange/i2p-sam">codeberg.org/diva.exchange/i2p-sam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">node-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Javascript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/redhog/node-i2p">github.com/redhog/node-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Jsam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/Jsam">github.com/eyedeekay/Jsam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">I2PSharp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/MohA39/I2PSharp">github.com/MohA39/I2PSharp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2pdotnet</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/SamuelFisher/i2pdotnet">github.com/SamuelFisher/i2pdotnet</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.rb</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Ruby</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/dryruby/i2p.rb">github.com/dryruby/i2p.rb</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">solitude</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/syvita/solitude">github.com/syvita/solitude</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Samty</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://notabug.org/acetone/samty">notabug.org/acetone/samty</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">bitcoin</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/bitcoin/bitcoin/blob/master/src/i2p.cpp">source (not a library, but good reference code)</a></td>
    </tr>
  </tbody>
</table>
## Início Rápido

Para implementar uma aplicação básica peer-to-peer apenas TCP, o cliente deve suportar os seguintes comandos:

- `HELLO VERSION MIN=3.1 MAX=3.1` - Necessário para todos os comandos restantes
- `DEST GENERATE SIGNATURE_TYPE=7` - Para gerar nossa chave privada e destination
- `NAMING LOOKUP NAME=...` - Para converter endereços .i2p em destinations
- `SESSION CREATE STYLE=STREAM ID=... DESTINATION=... i2cp.leaseSetEncType=4,0` - Necessário para STREAM CONNECT e STREAM ACCEPT
- `STREAM CONNECT ID=... DESTINATION=...` - Para fazer conexões de saída
- `STREAM ACCEPT ID=...` - Para aceitar conexões de entrada

## Orientações Gerais para Desenvolvedores

### Design de Aplicação

As sessões SAM (ou dentro do I2P, pools de tunnel ou conjuntos de tunnels) são projetadas para ter longa duração. A maioria das aplicações precisará apenas de uma sessão, criada na inicialização e fechada na saída. O I2P é diferente do Tor, onde os circuitos podem ser rapidamente criados e descartados. Pense cuidadosamente e consulte os desenvolvedores do I2P antes de projetar sua aplicação para usar mais de uma ou duas sessões simultâneas, ou para criá-las e descartá-las rapidamente. A maioria dos modelos de ameaça não exigirá uma sessão única para cada conexão.

Além disso, certifique-se de que as configurações da sua aplicação (e orientações aos usuários sobre configurações do router, ou padrões do router se você incluir um router) resultarão em seus usuários contribuindo mais recursos para a rede do que consomem. I2P é uma rede peer-to-peer, e a rede não pode sobreviver se uma aplicação popular levar a rede a um congestionamento permanente.

### Compatibilidade e Testes

As implementações de router Java I2P e i2pd são independentes e possuem pequenas diferenças no comportamento, suporte a recursos e configurações padrão. Por favor, teste sua aplicação com a versão mais recente de ambos os routers.

O SAM do i2pd está habilitado por padrão; o SAM do Java I2P não está. Forneça instruções aos seus usuários sobre como habilitar o SAM no Java I2P (via /configclients no console do router), e/ou forneça uma boa mensagem de erro ao usuário se a conexão inicial falhar, por exemplo "certifique-se de que o I2P está rodando e a interface SAM está habilitada".

Os routers Java I2P e i2pd têm padrões diferentes para quantidades de tunnel. O padrão do Java é 2 e o padrão do i2pd é 5. Para a maioria dos casos de baixa a média largura de banda e baixa a média quantidade de conexões, 2 ou 3 é suficiente. Por favor, especifique a quantidade de tunnel na mensagem SESSION CREATE para obter desempenho consistente com os routers Java I2P e i2pd. Veja abaixo.

Para obter mais orientação aos desenvolvedores sobre como garantir que sua aplicação use apenas os recursos necessários, consulte [nosso guia para incluir o I2P com sua aplicação](/docs/applications/embedding).

### Tipos de Assinatura e Criptografia

O I2P suporta múltiplos tipos de assinatura e criptografia. Para compatibilidade com versões anteriores, o SAM usa por padrão tipos antigos e ineficientes, então todos os clientes devem especificar tipos mais recentes.

O tipo de assinatura é especificado nos comandos DEST GENERATE e SESSION CREATE (para transiente). Todos os clientes devem definir `SIGNATURE_TYPE=7` (Ed25519).

O tipo de criptografia é especificado no comando SESSION CREATE. Múltiplos tipos de criptografia são permitidos. Os clientes devem definir `i2cp.leaseSetEncType=4` (apenas para ECIES-X25519) ou `i2cp.leaseSetEncType=4,0` (para ECIES-X25519 e ElGamal, se compatibilidade for necessária).

## Alterações da Versão 3

### Alterações da Versão 3.0

A versão 3.0 foi introduzida no lançamento 0.7.3 do I2P. O SAMv2 fornecia uma forma de gerenciar vários sockets no mesmo destino I2P *em paralelo*, ou seja, o cliente não precisava esperar que os dados fossem enviados com sucesso em um socket antes de enviar dados em outro socket. Mas todos os dados transitavam através do mesmo socket cliente-para-SAM, o que era bastante complicado de gerenciar para o cliente.

SAM v3 gerencia sockets de forma diferente: cada *socket I2P* corresponde a um único socket cliente-para-SAM, que é muito mais simples de lidar. Isso é similar ao [BOB](/docs/api/bob).

SAMv3 também oferece uma porta UDP para enviar datagramas através do I2P, e pode encaminhar datagramas I2P de volta para o servidor de datagramas do cliente.

### Mudanças da Versão 3.1

A versão 3.1 foi introduzida no lançamento Java I2P 0.9.14 (julho de 2014). SAMv3.1 é a implementação SAMv3 mínima recomendada devido ao seu suporte para tipos de assinatura melhores que o SAMv3.0. O i2pd também suporta a maioria dos recursos da versão 3.1.

- DEST GENERATE e SESSION CREATE agora suportam um parâmetro SIGNATURE_TYPE.
- Os parâmetros MIN e MAX em HELLO VERSION agora são opcionais.
- Os parâmetros MIN e MAX em HELLO VERSION agora suportam versões de um dígito como "3".
- RAW SEND agora é suportado no socket bridge.

### Alterações da Versão 3.2

A versão 3.2 foi introduzida no lançamento 0.9.24 do Java I2P (janeiro de 2016). Note que o i2pd atualmente não suporta a maioria dos recursos da versão 3.2.

#### Suporte de Porta e Protocolo I2CP

- Opções SESSION CREATE FROM_PORT e TO_PORT
- Opção SESSION CREATE STYLE=RAW PROTOCOL
- Opções STREAM CONNECT, DATAGRAM SEND e RAW SEND FROM_PORT e TO_PORT
- Opção RAW SEND PROTOCOL
- DATAGRAM RECEIVED, RAW RECEIVED e streams encaminhados ou recebidos e datagramas respondíveis, inclui FROM_PORT e TO_PORT
- A opção de sessão RAW HEADER=true fará com que os datagramas raw encaminhados sejam precedidos por uma linha contendo PROTOCOL=nnn FROM_PORT=nnnn TO_PORT=nnnn
- A primeira linha de datagramas enviados através da porta 7655 pode agora começar com qualquer versão 3.x
- A primeira linha de datagramas enviados através da porta 7655 pode conter qualquer uma das opções FROM_PORT, TO_PORT, PROTOCOL
- RAW RECEIVED inclui PROTOCOL=nnn

#### SSL e Autenticação

- USER/PASSWORD nos parâmetros HELLO para autorização. Veja [abaixo](#authorization).
- Configuração de autorização opcional com o comando AUTH. Veja [abaixo](#authorization-configuration-sam-32-or-higher-optional-feature).
- Suporte SSL/TLS opcional no socket de controle. Veja [abaixo](#ssl).
- Opção STREAM FORWARD SSL=true

#### Multithreading

- STREAM ACCEPTs pendentes simultâneos são permitidos no mesmo ID de sessão.

#### Análise de Linha de Comando e Keepalive

- Comandos opcionais QUIT, STOP e EXIT para fechar a sessão e socket. Veja [abaixo](#quitstopexitinvisible-sam-32-or-higher-optional-features).
- O parsing de comandos irá lidar adequadamente com UTF-8
- O parsing de comandos lida de forma confiável com espaços em branco dentro de aspas
- Uma barra invertida '\\' pode escapar aspas na linha de comando
- Recomendado que o servidor mapeie comandos para maiúsculas, para facilitar os testes via telnet.
- Valores de opção vazios como PROTOCOL ou PROTOCOL= podem ser permitidos, dependendo da implementação.
- PING/PONG para keepalive. Veja abaixo.
- Servidores podem implementar timeouts para o HELLO ou comandos subsequentes, dependendo da implementação.

### Mudanças da Versão 3.3

A versão 3.3 foi introduzida na versão 0.9.25 do Java I2P (março de 2016). Note que o i2pd atualmente não suporta a maioria dos recursos da versão 3.3.

- A mesma sessão pode ser usada para streams, datagramas e raw simultaneamente. Pacotes e streams recebidos serão roteados com base no protocolo I2P e na porta de destino. Veja [a seção PRIMARY abaixo](#sam-primary-sessions-v33-and-higher).
- DATAGRAM SEND e RAW SEND agora suportam as opções SEND_TAGS, TAG_THRESHOLD, EXPIRES e SEND_LEASESET. Veja [a seção de envio de datagramas abaixo](#sending-repliable-or-raw-datagrams).

## Protocolo Versão 3

### Visão Geral da Especificação Simple Anonymous Messaging (SAM) Versão 3.3

A aplicação cliente comunica com a ponte SAM, que lida com todas as funcionalidades do I2P (usando a [biblioteca de streaming](/docs/api/streaming) para streams virtuais, ou [I2CP](/docs/protocol/i2cp) diretamente para datagramas).

Por padrão, a comunicação entre cliente e ponte SAM não é criptografada nem autenticada. A ponte SAM pode suportar conexões SSL/TLS; detalhes de configuração e implementação estão fora do escopo desta especificação. A partir do SAM 3.2, parâmetros opcionais de autenticação usuário/senha são suportados no handshake inicial e podem ser exigidos pela ponte.

As comunicações I2P podem assumir várias formas distintas:

- [Streams virtuais](/docs/api/streaming)
- [Datagramas replicáveis e autenticados](/docs/specs/datagrams#repliable) (mensagens com campo FROM)
- [Datagramas anônimos](/docs/specs/datagrams#raw) (mensagens anônimas brutas)
- [Datagram2](/docs/specs/datagrams#datagram2) (um novo formato replicável e autenticado)
- [Datagram3](/docs/specs/datagrams#datagram3) (um novo formato replicável mas não autenticado)

As comunicações I2P são suportadas por sessões I2P, e cada sessão I2P está vinculada a um endereço (chamado destination). Uma sessão I2P está associada a um dos três tipos acima, e não pode transportar comunicações de outro tipo, a menos que use [sessões PRIMARY](#sam-primary-sessions-v33-and-higher).

### Codificação e Escapamento

Todas essas mensagens SAM são enviadas em uma única linha, terminadas pelo caractere de nova linha (\\n). Antes do SAM 3.2, apenas ASCII de 7 bits era suportado. A partir do SAM 3.2, a codificação deve ser UTF-8. Quaisquer chaves ou valores codificados em UTF8 devem funcionar.

A formatação mostrada nesta especificação abaixo é apenas para legibilidade, e embora as duas primeiras palavras em cada mensagem devam permanecer em sua ordem específica, a ordenação dos pares chave=valor pode mudar (por exemplo, "ONE TWO A=B C=D" ou "ONE TWO C=D A=B" são ambas construções perfeitamente válidas). Além disso, o protocolo é sensível a maiúsculas e minúsculas. A seguir, os exemplos de mensagens são precedidos por "->" para mensagens enviadas pelo cliente para a ponte SAM, e por "<-" para mensagens enviadas pela ponte SAM para o cliente.

A linha básica de comando ou resposta assume uma das seguintes formas:

```
COMMAND SUBCOMMAND [key=value] [key=value] ...
COMMAND                                           # As of SAM 3.2
PING[ arbitrary text]                             # As of SAM 3.2
PONG[ arbitrary text]                             # As of SAM 3.2
```
COMMAND sem um SUBCOMMAND é suportado apenas para alguns comandos novos no SAM 3.2.

Pares Chave=valor devem ser separados por um único espaço. (A partir do SAM 3.2, múltiplos espaços são permitidos) Valores devem estar entre aspas duplas se contiverem espaços, por exemplo, chave="texto de valor longo". (Antes do SAM 3.2, isso não funcionava de forma confiável em algumas implementações)

Antes do SAMv3.2, não havia mecanismo de escape. A partir do SAMv3.2, aspas duplas podem ser escapadas com uma barra invertida '\\' e uma barra invertida pode ser representada como duas barras invertidas '\\\\'.

### Valores Vazios

A partir do SAM 3.2, valores de opção vazios como KEY, KEY=, ou KEY="" podem ser permitidos, dependendo da implementação.

### Sensibilidade a Maiúsculas e Minúsculas

O protocolo, conforme especificado, é sensível a maiúsculas e minúsculas. É recomendado, mas não obrigatório, que o servidor mapeie comandos para maiúsculas, para facilitar testes via telnet. Isso permitiria, por exemplo, que "hello version" funcionasse. Isso depende da implementação. Não mapeie chaves ou valores para maiúsculas, pois isso corromperia as opções do [I2CP](/docs/protocol/i2cp).

### Handshake de Conexão SAM

Nenhuma comunicação SAM pode ocorrer até que o cliente e a ponte tenham concordado sobre uma versão de protocolo, o que é feito pelo cliente enviando um HELLO e a ponte enviando um HELLO REPLY:

```
->  HELLO VERSION
          [MIN=$min]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [MAX=$max]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [USER="xxx"]          # As of SAM 3.2, required if authentication is enabled, see below
          [PASSWORD="yyy"]      # As of SAM 3.2, required if authentication is enabled, see below
```
e

```
<-  HELLO REPLY RESULT=OK VERSION=3.1
```
A partir da versão 3.1 (I2P 0.9.14), os parâmetros MIN e MAX são opcionais. O SAM sempre retornará a versão mais alta possível dados os limites MIN e MAX, ou a versão atual do servidor se nenhum limite for fornecido.

Se a ponte SAM não conseguir encontrar uma versão adequada, ela responde com:

```
<- HELLO REPLY RESULT=NOVERSION
```
Se ocorreu algum erro, como um formato de solicitação inválido, ele responde com:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
#### SSL

O socket de controle do servidor pode opcionalmente oferecer suporte SSL/TLS, conforme configurado no servidor e cliente. As implementações podem oferecer outras camadas de transporte também; isso está fora do escopo da definição do protocolo.

#### Autorização

Para autorização, o cliente adiciona USER="xxx" PASSWORD="yyy" aos parâmetros HELLO. Aspas duplas para usuário e senha são recomendadas mas não obrigatórias. Uma aspa dupla dentro de um usuário ou senha deve ser escapada com uma barra invertida. Em caso de falha, o servidor responderá com um I2P_ERROR e uma mensagem. É recomendado que SSL seja habilitado em qualquer servidor SAM onde autorização seja necessária.

#### Timeouts

Os servidores podem implementar timeouts para o comando HELLO ou comandos subsequentes, dependendo da implementação. Os clientes devem enviar prontamente o HELLO e o próximo comando após se conectarem.

Se ocorrer um timeout antes de o HELLO ser recebido, a ponte responde com:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
e depois desconecta.

Se ocorrer um timeout após o HELLO ser recebido mas antes do próximo comando, a ponte responde com:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
e depois desconecta.

### Portas e Protocolo I2CP

A partir do SAM 3.2, as portas e protocolo [I2CP](/docs/protocol/i2cp) podem ser especificados pelo remetente cliente SAM para serem repassados ao [I2CP](/docs/protocol/i2cp), e a ponte SAM irá passar as informações de porta e protocolo [I2CP](/docs/protocol/i2cp) recebidas para o cliente SAM.

Para FROM_PORT e TO_PORT, o intervalo válido é 0-65535, e o padrão é 0.

Para PROTOCOL, que pode ser especificado apenas para RAW, o intervalo válido é 0-255, e o padrão é 18.

Para comandos SESSION, as portas e protocolo especificados são os padrões para essa sessão. Para fluxos ou datagramas individuais, as portas e protocolo especificados substituem os padrões da sessão. Para fluxos ou datagramas recebidos, as portas e protocolo indicados são como recebidos do [I2CP](/docs/protocol/i2cp).

#### Diferenças Importantes do IP Padrão

As portas I2CP são para sockets e datagramas I2P. Elas não estão relacionadas aos seus sockets locais que se conectam ao SAM.

- A porta 0 é válida e tem significado especial.
- As portas 1-1023 não são especiais nem privilegiadas.
- Os servidores escutam na porta 0 por padrão, o que significa "todas as portas".
- Os clientes enviam para a porta 0 por padrão, o que significa "qualquer porta".
- Os clientes enviam da porta 0 por padrão, o que significa "não especificada".
- Os servidores podem ter um serviço escutando na porta 0 e outros serviços escutando em portas superiores. Se for o caso, o serviço da porta 0 é o padrão e será conectado se a porta do socket ou datagrama de entrada não corresponder a outro serviço.
- A maioria dos destinos I2P tem apenas um serviço executando neles, então você pode usar os padrões e ignorar a configuração de portas I2CP.
- SAM 3.2 ou 3.3 é necessário para especificar portas I2CP.
- Se você não precisar de portas I2CP, não precisará do SAM 3.2 ou 3.3; 3.1 é suficiente.
- O protocolo 0 é válido e significa "qualquer protocolo". Isso não é recomendado e provavelmente não funcionará.
- Os sockets I2P são rastreados por um ID de conexão interno. Portanto, não há requisito de que a 5-tupla dest:porta:dest:porta:protocolo seja única. Por exemplo, pode haver múltiplos sockets com as mesmas portas entre dois destinos. Os clientes não precisam escolher uma "porta livre" para uma conexão de saída.

Se você está projetando uma aplicação SAM 3.3 com múltiplas subsessões, pense cuidadosamente sobre como usar portas e protocolos de forma eficaz. Consulte a especificação [I2CP](/docs/protocol/i2cp) para mais informações.

### Sessões SAM

Uma sessão SAM é criada por um cliente abrindo um socket para a ponte SAM, operando um handshake, e enviando uma mensagem SESSION CREATE, e a sessão termina quando o socket é desconectado.

Cada Destino I2P registrado está associado exclusivamente a um ID de sessão (ou apelido). Os IDs de sessão, incluindo IDs de subsessão para sessões PRIMARY, devem ser globalmente únicos no servidor SAM. Para prevenir possíveis colisões de ID com outros clientes, a melhor prática é que o cliente gere IDs aleatoriamente.

Cada sessão está associada exclusivamente com:

- o socket a partir do qual o cliente cria a sessão
- seu ID (ou apelido)

#### Solicitação de Criação de Sessão

A mensagem de criação de sessão pode usar apenas uma dessas formas (mensagens recebidas através de outras formas são respondidas com uma mensagem de erro):

```
->  SESSION CREATE
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, for DESTINATION=TRANSIENT only, default DSA_SHA1
          [PORT=$port]                         # Required for DATAGRAM* RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [HEADER={true,false}]                # SAM 3.2 or higher only, for STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
DESTINATION especifica qual destination deve ser usado para enviar e receber mensagens/streams. O $privkey é o base 64 da concatenação do [Destination](/docs/specs/common-structures#type_Destination) seguido pela [Private Key](/docs/specs/common-structures#type_PrivateKey) seguida pela [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), opcionalmente seguida pela [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), que tem 663 ou mais bytes em binário e 884 ou mais bytes em base 64, dependendo do tipo de assinatura. O formato binário é especificado em Private Key File. Veja notas adicionais sobre a [Private Key](/docs/specs/common-structures#type_PrivateKey) na seção Destination Key Generation abaixo.

Se a chave privada de assinatura for toda zeros, a seção [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) segue. Assinaturas offline são suportadas apenas para sessões STREAM e RAW. Assinaturas offline não podem ser criadas com DESTINATION=TRANSIENT. O formato da seção de assinatura offline é:

1. Timestamp de expiração (4 bytes, big endian, segundos desde epoch, reinicia em 2106)
2. Tipo de assinatura da Chave Pública de Assinatura transitória (2 bytes, big endian)
3. Chave pública de assinatura transitória (comprimento conforme especificado pelo tipo de assinatura transitória)
4. Assinatura dos três campos acima pela chave offline (comprimento conforme especificado pelo tipo de assinatura do destino)
5. Chave privada de assinatura transitória (comprimento conforme especificado pelo tipo de assinatura transitória)

Se o destino for especificado como TRANSIENT, a ponte SAM cria um novo destino. A partir da versão 3.1 (I2P 0.9.14), se o destino for TRANSIENT, um parâmetro opcional SIGNATURE_TYPE é suportado. O valor SIGNATURE_TYPE pode ser qualquer nome (por exemplo, ECDSA_SHA256_P256, não diferencia maiúsculas de minúsculas) ou número (por exemplo, 1) suportado pelos [Key Certificates](/docs/specs/common-structures#type_Certificate). O padrão é DSA_SHA1, que NÃO é o que você deseja. Para a maioria das aplicações, por favor especifique SIGNATURE_TYPE=7.

$nickname é a escolha do cliente. Não são permitidos espaços em branco.

Opções adicionais fornecidas são passadas para a configuração da sessão I2P se não forem interpretadas pela ponte SAM (por exemplo, outbound.length=0).

Os routers Java I2P e i2pd têm padrões diferentes para quantidades de tunnel. O padrão do Java é 2 e o padrão do i2pd é 5. Para a maioria dos casos de baixa a média largura de banda e baixa a média quantidade de conexões, 2 ou 3 é suficiente. Por favor, especifique as quantidades de tunnel na mensagem SESSION CREATE para obter desempenho consistente com os routers Java I2P e i2pd, usando as opções, por exemplo, inbound.quantity=3 outbound.quantity=3. Essas e outras opções [estão documentadas nos links abaixo](#tunnel-i2cp-and-streaming-options).

A própria bridge SAM já deve estar configurada com qual router deve comunicar através do I2P (embora, se necessário, pode haver uma forma de fornecer uma substituição, por exemplo, i2cp.tcp.host=localhost e i2cp.tcp.port=7654).

#### Resposta de Criação de Sessão

Após receber a mensagem de criação de sessão, a ponte SAM responderá com uma mensagem de status da sessão, conforme segue:

Se a criação foi bem-sucedida:

```
<-  SESSION STATUS RESULT=OK DESTINATION=$privkey
```
O $privkey é a base 64 da concatenação do [Destination](/docs/specs/common-structures#type_Destination) seguido pela [Private Key](/docs/specs/common-structures#type_PrivateKey) seguido pela [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), opcionalmente seguido pela [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), que tem 663 ou mais bytes em binário e 884 ou mais bytes em base 64, dependendo do tipo de assinatura. O formato binário é especificado no Private Key File.

Se o SESSION CREATE continha uma chave privada de assinatura com todos os zeros e uma seção [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), a resposta SESSION STATUS incluirá os mesmos dados no mesmo formato. Consulte a seção SESSION CREATE acima para detalhes.

Se o apelido já estiver associado a uma sessão:

```
<-  SESSION STATUS RESULT=DUPLICATED_ID
```
Se o destino já estiver em uso:

```
<-  SESSION STATUS RESULT=DUPLICATED_DEST
```
Se o destino não for uma chave de destino privada válida:

```
<-  SESSION STATUS RESULT=INVALID_KEY
```
Se ocorreu algum outro erro:

```
<-  SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
Se não estiver OK, a MESSAGE deve conter informações legíveis sobre por que a sessão não pôde ser criada.

Note que o router constrói tunnels antes de responder com SESSION STATUS. Isso pode levar vários segundos ou, na inicialização do router ou durante severo congestionamento da rede, um minuto ou mais. Se não for bem-sucedido, o router não responderá com uma mensagem de falha por vários minutos. Não defina um timeout curto esperando pela resposta. Não abandone a sessão enquanto a construção do tunnel estiver em progresso e tente novamente.

As sessões SAM vivem e morrem com o socket ao qual estão associadas. Quando o socket é fechado, a sessão morre, e todas as comunicações usando a sessão morrem ao mesmo tempo. E vice-versa, quando a sessão morre por qualquer motivo, a ponte SAM fecha o socket.

### Streams Virtuais SAM

Os streams virtuais são garantidos de serem enviados de forma confiável e em ordem, com notificação de falha e sucesso assim que estiver disponível.

Os streams são sockets de comunicação bidirecionais entre dois destinos I2P, mas sua abertura deve ser solicitada por um deles. Daqui em diante, comandos CONNECT são usados pelo cliente SAM para tal solicitação. Comandos FORWARD / ACCEPT são usados pelo cliente SAM quando ele deseja escutar solicitações vindas de outros destinos I2P.

### SAM Virtual Streams: CONNECT

Um cliente solicita uma conexão através de:

- abrindo um novo socket com a bridge SAM
- passando o mesmo handshake HELLO como acima
- enviando o comando STREAM CONNECT

#### Solicitação de Conexão

```
-> STREAM CONNECT
         ID=$nickname
         DESTINATION=$destination
         [SILENT={true,false}]                # default false
         [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
         [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
```
Isso estabelece uma nova conexão virtual da sessão local cujo ID é $nickname para o peer especificado.

O destino é $destination, que é a base 64 da [Destination](/docs/specs/common-structures#type_Destination), que tem 516 ou mais caracteres base 64 (387 ou mais bytes em binário), dependendo do tipo de assinatura.

**NOTA:** Desde cerca de 2014 (SAM v3.1), o Java I2P também suporta nomes de host e endereços b32 para o $destination, mas isso não estava documentado anteriormente. Nomes de host e endereços b32 agora são oficialmente suportados pelo Java I2P a partir da versão 0.9.48. O router i2pd suporta nomes de host e endereços b32 a partir da versão 2.38.0 (0.9.50). Para ambos os routers, o suporte "b32" inclui suporte a endereços "b33" estendidos para destinos cegos.

#### Resposta de Conexão

Se SILENT=true for passado, a bridge SAM não emitirá nenhuma outra mensagem no socket. Se a conexão falhar, o socket será fechado. Se a conexão for bem-sucedida, todos os dados restantes que passam pelo socket atual são encaminhados de e para o peer de destino I2P conectado.

Se SILENT=false, que é o valor padrão, a ponte SAM envia uma última mensagem para seu cliente antes de encaminhar ou fechar o socket:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
O valor RESULT pode ser um dos seguintes:

```
OK
CANT_REACH_PEER
I2P_ERROR
INVALID_KEY
INVALID_ID
TIMEOUT
```
Se o RESULT for OK, todos os dados restantes que passam pelo socket atual são encaminhados de e para o peer de destino I2P conectado. Se a conexão não foi possível (timeout, etc), RESULT conterá o valor de erro apropriado (acompanhado por uma MESSAGE legível opcional), e a ponte SAM fecha o socket.

O timeout de conexão do stream do router internamente é aproximadamente um minuto, dependente da implementação. Não defina um timeout mais curto aguardando a resposta.

### SAM Virtual Streams: ACCEPT

Um cliente aguarda uma solicitação de conexão de entrada por:

- abrindo um novo socket com a ponte SAM
- passando o mesmo handshake HELLO como acima
- enviando o comando STREAM ACCEPT

#### Aceitar Solicitação

```
-> STREAM ACCEPT
         ID=$nickname
         [SILENT={true,false}]                # default false
```
Isto faz com que a sessão ${nickname} escute por uma solicitação de conexão de entrada da rede I2P. ACCEPT não é permitido enquanto houver um FORWARD ativo na sessão.

A partir do SAM 3.2, múltiplos STREAM ACCEPTs pendentes simultâneos são permitidos no mesmo ID de sessão (mesmo com a mesma porta). Antes da versão 3.2, accepts simultâneos falhariam com ALREADY_ACCEPTING. Nota: Java I2P também suporta ACCEPTs simultâneos no SAM 3.1, a partir da versão 0.9.24 (2016-01). i2pd também suporta ACCEPTs simultâneos no SAM 3.1, a partir da versão 2.50.0 (2023-12).

#### Resposta de Aceitação

Se SILENT=true for passado, a ponte SAM não emitirá nenhuma outra mensagem no socket. Se a aceitação falhar, o socket será fechado. Se a aceitação for bem-sucedida, todos os dados restantes que passam pelo socket atual são encaminhados de e para o peer de destino I2P conectado. Para confiabilidade, e para receber o destino para conexões de entrada, recomenda-se SILENT=false.

Se SILENT=false, que é o valor padrão, a ponte SAM responde com:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
O valor RESULT pode ser um dos seguintes:

```
OK
I2P_ERROR
INVALID_ID
```
Se o resultado não for OK, o socket é fechado imediatamente pela ponte SAM. Se o resultado for OK, a ponte SAM começa a aguardar uma solicitação de conexão de entrada de outro peer I2P. Quando uma solicitação chega, a ponte SAM a aceita e:

Se SILENT=true foi passado, a ponte SAM não emitirá nenhuma outra mensagem no socket do cliente. Todos os dados restantes passando pelo socket atual são encaminhados de e para o peer de destino I2P conectado.

Se SILENT=false foi passado, que é o valor padrão, a ponte SAM envia ao cliente uma linha ASCII contendo a chave de destino público base64 do peer solicitante, e informações adicionais apenas para SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Após esta linha terminada com '\\n', todos os dados restantes que passam pelo socket atual são encaminhados de e para o peer de destino I2P conectado, até que um dos peers feche o socket.

#### Erros Após OK

Em casos raros, a ponte SAM pode encontrar um erro após enviar RESULT=OK, mas antes de uma conexão entrar e enviar a linha $destination para o cliente. Esses erros podem incluir desligamento do router, reinicialização do router e fechamento de sessão. Nesses casos, quando SILENT=false, a ponte SAM pode, mas não é obrigatório (dependente da implementação), enviar a linha:

```
<-  STREAM STATUS
         RESULT=I2P_ERROR
         [MESSAGE=...]
```
antes de fechar imediatamente o socket. Esta linha não é, obviamente, decodificável como um destino Base 64 válido.

### SAM Virtual Streams: FORWARD

Um cliente pode usar um servidor de socket regular e aguardar solicitações de conexão vindas do I2P. Para isso, o cliente deve:

- abrir um novo socket com a ponte SAM
- passar o mesmo handshake HELLO como acima
- enviar o comando forward

#### Solicitação de Encaminhamento

```
-> STREAM FORWARD
         ID=$nickname
         PORT=$port
         [HOST=$host]
         [SILENT={true,false}]                # default false
         [SSL={true,false}]                   # SAM 3.2 or higher only, default false
```
Isto faz com que a sessão ${nickname} escute por solicitações de conexão recebidas da rede I2P. FORWARD não é permitido enquanto houver um ACCEPT pendente na sessão.

#### Resposta de Encaminhamento

SILENT tem como padrão false. Seja SILENT verdadeiro ou falso, a ponte SAM sempre responde com uma mensagem STREAM STATUS. Note que este é um comportamento diferente de STREAM ACCEPT e STREAM CONNECT quando SILENT=true. A mensagem STREAM STATUS é:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
O valor RESULT pode ser um dos seguintes:

```
OK
I2P_ERROR
INVALID_ID
```
$host é o hostname ou endereço IP do servidor de socket para o qual o SAM irá encaminhar as solicitações de conexão. Se não fornecido, o SAM usa o IP do socket que emitiu o comando de encaminhamento.

$port é o número da porta do servidor de socket para o qual SAM irá encaminhar solicitações de conexão. É obrigatório.

Quando uma solicitação de conexão chega do I2P, a ponte SAM abre uma conexão socket para $host:$port. Se for aceita em menos de 3 segundos, o SAM aceitará a conexão do I2P, e então:

Se SILENT=true foi passado, todos os dados que passam pelo socket atual obtido são encaminhados de e para o peer de destino I2P conectado.

Se SILENT=false foi passado, que é o valor padrão, a ponte SAM envia no socket obtido uma linha ASCII contendo a chave de destino público em base64 do peer solicitante, e informações adicionais apenas para SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Após esta linha terminada em '\\n', todos os dados restantes que passam pelo socket são encaminhados de e para o peer de destino I2P conectado, até que um dos lados feche o socket.

A partir do SAM 3.2, se SSL=true for especificado, o socket de encaminhamento é sobre SSL/TLS.

O router I2P irá parar de escutar solicitações de conexão de entrada assim que o socket de "encaminhamento" for fechado.

### Datagramas SAM

SAMv3 fornece mecanismos para enviar e receber datagramas através de sockets de datagrama locais. Algumas implementações SAMv3 também suportam o método mais antigo v1/v2 de enviar/receber datagramas através do socket bridge SAM. Ambos estão documentados abaixo.

O I2P suporta quatro tipos de datagramas:

- Datagramas replicáveis e autenticados são prefixados com o destino do remetente, e contêm a assinatura do remetente, para que o receptor possa verificar que o destino do remetente não foi falsificado, e possa responder ao datagrama. O novo formato Datagram2 também é replicável e autenticado.
- O novo formato Datagram3 é replicável mas não autenticado. A informação do remetente não é verificada.
- Datagramas raw não contêm o destino do remetente ou uma assinatura.

As portas I2CP padrão são definidas tanto para datagramas respondíveis quanto para datagramas brutos. A porta I2CP pode ser alterada para datagramas brutos.

Um padrão comum de design de protocolo é enviar datagramas com resposta para servidores, incluindo algum identificador, e o servidor responder com um datagrama bruto que inclui esse identificador, para que a resposta possa ser correlacionada com a solicitação. Este padrão de design elimina a sobrecarga substancial de datagramas com resposta nas respostas. Todas as escolhas de protocolos I2CP e portas são específicas da aplicação, e os designers devem levar essas questões em consideração.

Veja também as notas importantes sobre MTU de datagrama na seção abaixo.

#### Enviando Datagramas Respondíveis ou Brutos

Embora o I2P não contenha inerentemente um endereço FROM, para facilidade de uso é fornecida uma camada adicional como datagramas com resposta - mensagens não ordenadas e não confiáveis de até 31744 bytes que incluem um endereço FROM (deixando até 1KB para material de cabeçalho). Este endereço FROM é autenticado internamente pelo SAM (fazendo uso da chave de assinatura do destino para verificar a origem) e inclui prevenção de replay.

O tamanho mínimo é 1. Para melhor confiabilidade de entrega, o tamanho máximo recomendado é de aproximadamente 11 KB. A confiabilidade é inversamente proporcional ao tamanho da mensagem, talvez até exponencialmente.

Após estabelecer uma sessão SAM com STYLE=DATAGRAM ou STYLE=RAW, o cliente pode enviar datagramas com resposta ou datagramas brutos através da porta UDP do SAM (7655 por padrão).

A primeira linha de um datagrama enviado através desta porta deve estar no seguinte formato. Isso está tudo em uma linha (separado por espaços), mostrado em múltiplas linhas para maior clareza:

```
3.0                                  # As of SAM 3.2, any "3.x" is allowed. Prior to that, "3.0" is required.
$nickname
$destination
[FROM_PORT=nnn]                      # SAM 3.2 or higher only, default from session options
[TO_PORT=nnn]                        # SAM 3.2 or higher only, default from session options
[PROTOCOL=nnn]                       # SAM 3.2 or higher only, only for RAW sessions, default from session options
[SEND_TAGS=nnn]                      # SAM 3.3 or higher only, number of session tags to send
                                     # Overrides crypto.tagsToSend I2CP session option
                                     # Default is router-dependent (40 for Java router)
[TAG_THRESHOLD=nnn]                  # SAM 3.3 or higher only, low session tag threshold
                                     # Overrides crypto.lowTagThreshold I2CP session option
                                     # Default is router-dependent (30 for Java router)
[EXPIRES=nnn]                        # SAM 3.3 or higher only, expiration from now in seconds
                                     # Overrides clientMessageTimeout I2CP session option (which is in ms)
                                     # Default is router-dependent (60 for Java router)
[SEND_LEASESET={true,false}]         # SAM 3.3 or higher only, whether to send our leaseset
                                     # Overrides shouldBundleReplyInfo I2CP session option
                                     # Default is true
\n
```
- 3.0 é a versão do SAM. A partir do SAM 3.2, qualquer versão 3.x é permitida.
- $nickname é o id da sessão DATAGRAM que será usada
- O alvo é $destination, que é a base 64 do [Destination](/docs/specs/common-structures#type_Destination), que são 516 ou mais caracteres em base 64 (387 ou mais bytes em binário), dependendo do tipo de assinatura. **NOTA:** Desde cerca de 2014 (SAM v3.1), o Java I2P também tem suportado nomes de host e endereços b32 para o $destination, mas isso não estava documentado anteriormente. Nomes de host e endereços b32 agora são oficialmente suportados pelo Java I2P a partir da versão 0.9.48. O roteador i2pd atualmente não suporta nomes de host e endereços b32; o suporte pode ser adicionado em uma versão futura.
- Todas as opções são configurações por datagrama que sobrescrevem os padrões especificados no SESSION CREATE.
- As opções da versão 3.3 SEND_TAGS, TAG_THRESHOLD, EXPIRES e SEND_LEASESET serão passadas para o [I2CP](/docs/protocol/i2cp) se suportadas. Veja [a especificação I2CP](/docs/protocol/i2cp#msg_SendMessageExpire) para detalhes. O suporte pelo servidor SAM é opcional, ele ignorará essas opções se não forem suportadas.
- esta linha é terminada por '\\n'.

A primeira linha será descartada pelo SAM antes de enviar os dados restantes da mensagem para o destino especificado.

Para um método alternativo de envio de datagramas com resposta e brutos, consulte [DATAGRAM SEND e RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### SAM Repliable Datagrams: Recebendo um Datagrama

Os datagramas recebidos são escritos pelo SAM no socket a partir do qual a sessão de datagrama foi aberta, se uma PORT de encaminhamento não for especificada no comando SESSION CREATE. Esta é a forma compatível com v1/v2 de receber datagramas.

Quando um datagrama chega, a ponte o entrega ao cliente através da mensagem:

```
<-  DATAGRAM RECEIVED
           DESTINATION=$destination           # See notes below for Datagram3 format
           SIZE=$numBytes
           FROM_PORT=nnn                      # SAM 3.2 or higher only
           TO_PORT=nnn                        # SAM 3.2 or higher only
           \n
       [$numBytes of data]
```
A origem é $destination, que é a base 64 do [Destination](/docs/specs/common-structures#type_Destination), que são 516 ou mais caracteres em base 64 (387 ou mais bytes em binário), dependendo do tipo de assinatura.

A ponte SAM nunca expõe ao cliente os cabeçalhos de autenticação ou outros campos, apenas os dados que o remetente forneceu. Isso continua até que a sessão seja fechada (pelo cliente que encerra a conexão).

#### Encaminhamento de Datagramas Brutos ou Respondíveis

Ao criar uma sessão de datagram, o cliente pode solicitar ao SAM para encaminhar mensagens recebidas para um ip:porta especificado. Isso é feito emitindo o comando CREATE com as opções PORT e HOST:

```
-> SESSION CREATE
          STYLE={DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          PORT=$port
          [HOST=$host]
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP options
```
O $privkey é a base 64 da concatenação do [Destination](/docs/specs/common-structures#type_Destination) seguido pela [Private Key](/docs/specs/common-structures#type_PrivateKey) seguido pela [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), opcionalmente seguido pela [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), que são 884 ou mais caracteres base 64 (663 ou mais bytes em binário), dependendo do tipo de assinatura. O formato binário é especificado em Private Key File.

Assinaturas offline são suportadas para datagramas RAW, DATAGRAM2 e DATAGRAM3, mas não para DATAGRAM. Consulte a seção SESSION CREATE acima e a seção DATAGRAM2/3 abaixo para detalhes.

$host é o hostname ou endereço IP do servidor de datagramas para o qual o SAM encaminhará os datagramas. Se não fornecido, o SAM usa o IP do socket que emitiu o comando forward.

$port é o número da porta do servidor de datagramas para o qual o SAM encaminhará datagramas. Se $port não estiver definido, os datagramas NÃO serão encaminhados, eles serão recebidos no socket de controle, de forma compatível com v1/v2.

Opções adicionais fornecidas são passadas para a configuração da sessão I2P se não forem interpretadas pela ponte SAM (ex: outbound.length=0). Essas opções [estão documentadas abaixo](#tunnel-i2cp-and-streaming-options).

Datagramas reencaminhados que podem ser respondidos são sempre prefixados com o destino em base64, exceto para Datagram3, veja abaixo. Quando um datagrama que pode ser respondido chega, a ponte envia para o host:porta especificado um pacote UDP contendo os seguintes dados:

```
$destination                       # See notes below for Datagram3 format
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
$datagram_payload
```
Datagramas brutos encaminhados são repassados tal como estão para o host:porta especificado sem um prefixo. O pacote UDP contém os seguintes dados:

```
$datagram_payload
```
A partir do SAM 3.2, quando HEADER=true é especificado em SESSION CREATE, o datagrama bruto encaminhado será precedido por uma linha de cabeçalho da seguinte forma:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
O $destination é a base 64 do [Destination](/docs/specs/common-structures#type_Destination), que tem 516 ou mais caracteres em base 64 (387 ou mais bytes em binário), dependendo do tipo de assinatura.

#### SAM Datagramas Anônimos (Raw)

Aproveitando ao máximo a largura de banda do I2P, o SAM permite que clientes enviem e recebam datagramas anônimos, deixando a autenticação e informações de resposta por conta dos próprios clientes. Esses datagramas são não confiáveis e desordenados, e podem ter até 32768 bytes.

O tamanho mínimo é 1. Para melhor confiabilidade de entrega, o tamanho máximo recomendado é aproximadamente 11 KB.

Após estabelecer uma sessão SAM com STYLE=RAW, o cliente pode enviar datagramas anônimos através da ponte SAM exatamente da mesma forma que [enviando datagramas com resposta](#sending-repliable-or-raw-datagrams).

Ambas as formas de receber datagramas também estão disponíveis para datagramas anônimos.

Os datagramas recebidos são escritos pelo SAM no socket a partir do qual a sessão de datagrama foi aberta, se uma PORTA de encaminhamento não for especificada no comando SESSION CREATE. Esta é a forma compatível com v1/v2 de receber datagramas.

```
<- RAW RECEIVED
          SIZE=$numBytes
          FROM_PORT=nnn                      # SAM 3.2 or higher only
          TO_PORT=nnn                        # SAM 3.2 or higher only
          PROTOCOL=nnn                       # SAM 3.2 or higher only
          \n
      [$numBytes of data]
```
Quando datagramas anônimos devem ser encaminhados para algum host:porta, a ponte envia para o host:porta especificado uma mensagem contendo os seguintes dados:

```
$datagram_payload
```
A partir do SAM 3.2, quando HEADER=true é especificado em SESSION CREATE, o datagrama bruto encaminhado será precedido por uma linha de cabeçalho da seguinte forma:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
Para um método alternativo de envio de datagramas anônimos, consulte [RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### Datagrama 2/3

Datagram 2/3 são novos formatos especificados no início de 2025. Atualmente não existem implementações conhecidas. Verifique a documentação da implementação para o status atual. Veja [a especificação](/docs/specs/datagrams) para mais informações.

Não há planos atuais para aumentar a versão SAM para indicar suporte a Datagram 2/3. Isso pode ser problemático, pois implementações podem desejar suportar Datagram 2/3 mas não os recursos do SAM v3.3. Qualquer mudança de versão está a ser determinada.

Tanto Datagram2 quanto Datagram3 podem receber resposta. Apenas Datagram2 é autenticado.

Datagram2 é idêntico aos datagramas replicáveis do ponto de vista do SAM. Ambos são autenticados. Apenas o formato I2CP e a assinatura são diferentes, mas isso não é visível para os clientes SAM. Datagram2 também suporta assinaturas offline, então pode ser usado por destinos com assinatura offline.

A intenção é que o Datagram2 substitua os datagramas Repliable para novas aplicações que não requerem compatibilidade com versões anteriores. O Datagram2 fornece proteção contra replay que não está presente nos datagramas Repliable. Se a compatibilidade com versões anteriores for necessária, uma aplicação pode suportar tanto Datagram2 quanto Repliable na mesma sessão com sessões SAM 3.3 PRIMARY.

Datagram3 é respondível mas não autenticado. O campo 'from' no formato I2CP é um hash, não um destino. O $destination enviado do servidor SAM para o cliente será um hash base64 de 44 bytes. Para convertê-lo em um destino completo para resposta, decodifique-o de base64 para 32 bytes binários, depois codifique-o em base32 para 52 caracteres e anexe ".b32.i2p" para uma NAMING LOOKUP. Como de costume, os clientes devem manter seu próprio cache para evitar NAMING LOOKUPs repetidos.

Os designers de aplicações devem usar extrema cautela e considerar as implicações de segurança dos datagramas não autenticados.

#### Considerações de MTU para Datagramas V3

I2P Datagrams podem ser maiores que o MTU típico da internet de 1500. Datagramas enviados localmente e datagramas replicáveis encaminhados prefixados com o destino base64 de 516+ bytes provavelmente excederão esse MTU. No entanto, MTUs localhost em sistemas Linux são tipicamente muito maiores, por exemplo 65536. MTUs localhost variam por sistema operacional. I2P Datagrams nunca serão maiores que 65536. O tamanho do datagrama depende do protocolo da aplicação.

Se o cliente SAM for local ao servidor SAM e o sistema suportar uma MTU maior, então os datagramas não serão fragmentados localmente. No entanto, se o cliente SAM for remoto, então os datagramas IPv4 seriam fragmentados e os datagramas IPv6 falhariam (IPv6 não suporta fragmentação UDP).

Desenvolvedores de bibliotecas cliente e aplicações devem estar cientes dessas questões e documentar recomendações para evitar fragmentação e prevenir perda de pacotes, especialmente em conexões remotas cliente-servidor SAM.

#### DATAGRAM SEND, RAW SEND (Manipulação de Datagram Compatível com V1/V2)

No SAMv3, a maneira preferida de enviar datagramas é através do socket de datagrama na porta 7655 como documentado acima. No entanto, datagramas que podem ser respondidos podem ser enviados diretamente através do socket bridge SAM usando o comando DATAGRAM SEND, como documentado em [SAM V1](/docs/api/sam) e [SAM V2](/docs/api/samv2).

A partir da versão 0.9.14 (versão 3.1), datagramas anônimos podem ser enviados diretamente através do socket da ponte SAM usando o comando RAW SEND, como documentado em [SAM V1](/docs/api/sam) e [SAM V2](/docs/api/samv2).

A partir da versão 0.9.24 (versão 3.2), DATAGRAM SEND e RAW SEND podem incluir os parâmetros FROM_PORT=nnnn e/ou TO_PORT=nnnn para substituir as portas padrão. A partir da versão 0.9.24 (versão 3.2), RAW SEND pode incluir o parâmetro PROTOCOL=nnn para substituir o protocolo padrão.

Estes comandos *não* suportam o parâmetro ID. Os datagramas são enviados para a sessão mais recentemente criada do estilo DATAGRAM ou RAW, conforme apropriado. O suporte para o parâmetro ID pode ser adicionado em uma versão futura.

Os formatos DATAGRAM2 e DATAGRAM3 *não* são suportados de forma compatível com V1/V2.

### Sessões PRIMARY do SAM (V3.3 e superior)

*A versão 3.3 foi introduzida no lançamento 0.9.25 do I2P.*

*Em uma versão anterior desta especificação, as sessões PRIMARY eram conhecidas como sessões MASTER. Tanto no `i2pd` quanto no `I2P+`, elas ainda são conhecidas apenas como sessões MASTER.*

SAM v3.3 adiciona suporte para executar streaming, datagramas e subsessões raw na mesma sessão primária, e para executar múltiplas subsessões do mesmo estilo. Todo o tráfego de subsessão usa um único destino, ou conjunto de túneis. O roteamento de tráfego do I2P é baseado nas opções de porta e protocolo para as subsessões.

Para criar subsessões multiplexadas, você deve criar uma sessão primária e então adicionar subsessões à sessão primária. Cada subsessão deve ter um id único e um protocolo de escuta e porta únicos. As subsessões também podem ser removidas da sessão primária.

Com uma sessão PRIMARY e uma combinação de subsessões, um cliente SAM pode suportar múltiplas aplicações, ou uma única aplicação sofisticada usando uma variedade de protocolos, em um único conjunto de tunnels. Por exemplo, um cliente bittorrent poderia configurar uma subsessão de streaming para conexões peer-to-peer, juntamente com subsessões datagram e raw para comunicação DHT.

#### Criando uma Sessão PRIMARY

```
->  SESSION CREATE
          STYLE=PRIMARY                        # prior to 0.9.47, use STYLE=MASTER
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP and streaming options
```
A bridge SAM responderá com sucesso ou falha como na [resposta a um SESSION CREATE padrão](#session-creation-response).

Não defina as opções PORT, HOST, FROM_PORT, TO_PORT, PROTOCOL, LISTEN_PORT, LISTEN_PROTOCOL ou HEADER em uma sessão primária. Você não pode enviar dados em um ID de sessão PRIMARY ou no socket de controle. Todos os comandos como STREAM CONNECT, DATAGRAM SEND, etc. devem usar o ID da subsessão em um socket separado.

A sessão PRIMÁRIA conecta-se ao router e constrói tunnels. Quando a ponte SAM responde, os tunnels foram construídos e a sessão está pronta para subsessões serem adicionadas. Todas as opções [I2CP](/docs/protocol/i2cp) relacionadas aos parâmetros do tunnel, como comprimento, quantidade e apelido, devem ser fornecidas no SESSION CREATE da primária.

Todos os comandos utilitários são suportados numa sessão primária.

Quando a sessão primária é fechada, todas as subsessões também são fechadas.

NOTA: Antes da versão 0.9.47, use STYLE=MASTER. STYLE=PRIMARY é suportado a partir da versão 0.9.47. MASTER ainda é suportado para compatibilidade com versões anteriores.

#### Criando uma Subsessão

Usando o mesmo socket de controle no qual a sessão PRIMARY foi criada:

```
->  SESSION ADD
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See above for DATAGRAM2/3
          ID=$nickname                         # must be unique
          [PORT=$port]                         # Required for DATAGRAM* and RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # For outbound traffic, default 0
          [TO_PORT=nnn]                        # For outbound traffic, default 0
          [PROTOCOL=nnn]                       # For outbound traffic for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [LISTEN_PORT=nnn]                    # For inbound traffic, default is the FROM_PORT value.
                                               # For STYLE=STREAM, only the FROM_PORT value or 0 is allowed.
          [LISTEN_PROTOCOL=nnn]                # For inbound traffic for STYLE=RAW only.
                                               # Default is the PROTOCOL value; 6 (streaming) is disallowed
          [HEADER={true,false}]                # For STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
A ponte SAM responderá com sucesso ou falha como na [resposta a um SESSION CREATE padrão](#session-creation-response). Como os tunnels já foram construídos no SESSION CREATE primário, a ponte SAM deve responder imediatamente.

Não defina a opção DESTINATION em um SESSION ADD. A subsessão usará o destino especificado na sessão primária. Todas as subsessões devem ser adicionadas no socket de controle, ou seja, na mesma conexão em que você criou a sessão primária.

Múltiplas subsessões devem ter opções suficientemente únicas para que os dados recebidos possam ser roteados corretamente. Em particular, múltiplas sessões do mesmo estilo devem ter opções LISTEN_PORT diferentes (e/ou LISTEN_PROTOCOL, apenas para RAW). Um SESSION ADD com porta de escuta e protocolo que duplica uma subsessão existente resultará em erro.

O LISTEN_PORT é a porta I2P local, ou seja, a porta de recebimento (TO) para dados de entrada. Se o LISTEN_PORT não for especificado, o valor FROM_PORT será usado. Se o LISTEN_PORT e FROM_PORT não forem especificados, o roteamento de entrada será baseado apenas em STYLE e PROTOCOL. Para LISTEN_PORT e LISTEN_PROTOCOL, 0 significa qualquer valor, isto é, um curinga. Se tanto LISTEN_PORT quanto LISTEN_PROTOCOL forem 0, esta subsessão será o padrão para tráfego de entrada que não seja roteado para outra subsessão. Tráfego de streaming de entrada (protocolo 6) nunca será roteado para uma subsessão RAW, mesmo se seu LISTEN_PROTOCOL for 0. Uma subsessão RAW não pode definir um LISTEN_PROTOCOL de 6. Se não houver padrão ou subsessão que corresponda ao protocolo e porta do tráfego de entrada, esses dados serão descartados.

Use o ID da subsessão, não o ID da sessão primária, para enviar e receber dados. Todos os comandos como STREAM CONNECT, DATAGRAM SEND, etc. devem usar o ID da subsessão.

Todos os comandos utilitários são suportados numa sessão primária ou subsessão. O envio/recebimento de datagramas/raw v1/v2 não é suportado numa sessão primária ou em subsessões.

#### Parando uma Subsessão

Usando o mesmo socket de controle no qual a sessão PRIMARY foi criada:

```
->  SESSION REMOVE
          ID=$nickname
```
Isto remove uma subsessão da sessão primária. Não defina outras opções em um SESSION REMOVE. As subsessões devem ser removidas no socket de controle, ou seja, na mesma conexão em que você criou a sessão primária. Após uma subsessão ser removida, ela é fechada e não pode ser usada para enviar ou receber dados.

A ponte SAM responderá com sucesso ou falha como na [resposta a um SESSION CREATE padrão](#session-creation-response).

### Comandos Utilitários SAM

Alguns comandos utilitários requerem uma sessão pré-existente e outros não. Veja os detalhes abaixo.

#### Busca de Nome de Host

A seguinte mensagem pode ser usada pelo cliente para consultar a ponte SAM para resolução de nomes:

```
NAMING LOOKUP
       NAME=$name
       [OPTIONS=true]     # Default false, as of router API 0.9.66
```
que é respondido por

```
NAMING REPLY
       RESULT=$result
       NAME=$name
       [VALUE=$destination]
       [MESSAGE="$message"]
       [OPTION:optionkey="$optionvalue"]   # As of router API 0.9.66
```
O valor RESULT pode ser um dos seguintes:

```
OK
INVALID_KEY
KEY_NOT_FOUND
```
Se NAME=ME, então a resposta conterá o destino usado pela sessão atual (útil se você estiver usando um TRANSIENT). Se $result não for OK, MESSAGE pode transmitir uma mensagem descritiva, como "bad format", etc. INVALID_KEY implica que algo está errado com $name na solicitação, possivelmente caracteres inválidos.

O $destination é o base 64 do [Destination](/docs/specs/common-structures#type_Destination), que são 516 ou mais caracteres base 64 (387 ou mais bytes em binário), dependendo do tipo de assinatura.

NAMING LOOKUP não exige que uma sessão tenha sido criada primeiro. No entanto, em algumas implementações, uma consulta .b32.i2p que não está em cache e requer uma consulta de rede pode falhar, pois não há client tunnels disponíveis para a consulta.

#### Opções de Busca de Nome

NAMING LOOKUP foi estendido a partir da API do router 0.9.66 para suportar pesquisas de serviços. O suporte pode variar conforme a implementação. Consulte a proposta 167 para informações adicionais.

NAMING LOOKUP NAME=example.i2p OPTIONS=true solicita o mapeamento de opções na resposta. NAME pode ser um destino base64 completo quando OPTIONS=true.

Se a busca de destino foi bem-sucedida e opções estavam presentes no leaseSet, então na resposta, seguindo o destino, haverá uma ou mais opções na forma de OPTION:key=value. Cada opção terá um prefixo OPTION: separado. Todas as opções do leaseSet serão incluídas, não apenas as opções de registro de serviço. Por exemplo, opções para parâmetros definidos no futuro podem estar presentes. Exemplo:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Chaves que contêm '=', e chaves ou valores que contêm uma quebra de linha, são consideradas inválidas e o par chave/valor será removido da resposta. Se não forem encontradas opções no leaseset, ou se o leaseset for versão 1, então a resposta não incluirá nenhuma opção. Se OPTIONS=true estava na consulta, e o leaseset não for encontrado, um novo valor de resultado LEASESET_NOT_FOUND será retornado.

#### Geração de Chave de Destino

Chaves base64 públicas e privadas podem ser geradas usando a seguinte mensagem:

```
->  DEST GENERATE
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, default DSA_SHA1
```
que é respondido por

```
DEST REPLY
     PUB=$destination
     PRIV=$privkey
```
A partir da versão 3.1 (I2P 0.9.14), um parâmetro opcional SIGNATURE_TYPE é suportado. O valor SIGNATURE_TYPE pode ser qualquer nome (por exemplo, ECDSA_SHA256_P256, insensível a maiúsculas e minúsculas) ou número (por exemplo, 1) que seja suportado por [Key Certificates](/docs/specs/common-structures#type_Certificate). O padrão é DSA_SHA1, que NÃO é o que você deseja. Para a maioria das aplicações, por favor especifique SIGNATURE_TYPE=7.

O $destination é a base 64 do [Destination](/docs/specs/common-structures#type_Destination), que possui 516 ou mais caracteres em base 64 (387 ou mais bytes em binário), dependendo do tipo de assinatura.

O $privkey é a base 64 da concatenação do [Destination](/docs/specs/common-structures#type_Destination) seguido da [Private Key](/docs/specs/common-structures#type_PrivateKey) seguido da [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), que são 884 ou mais caracteres base 64 (663 ou mais bytes em binário), dependendo do tipo de assinatura. O formato binário é especificado no Private Key File.

Notas sobre a [Private Key](/docs/specs/common-structures#type_PrivateKey) binária de 256 bytes: Este campo não é usado desde a versão 0.6 (2005). Implementações SAM podem enviar dados aleatórios ou todos zeros neste campo; não se preocupe com uma sequência de AAAA no base 64. A maioria das aplicações simplesmente armazenará a string base 64 e a retornará como está no SESSION CREATE, ou decodificará para binário para armazenamento, depois codificará novamente para SESSION CREATE. Aplicações podem, no entanto, decodificar o base 64, analisar o binário seguindo a especificação PrivateKeyFile, descartar a porção da private key de 256 bytes, e então substituí-la com 256 bytes de dados aleatórios ou todos zeros ao recodificá-la para o SESSION CREATE. TODOS os outros campos na especificação PrivateKeyFile devem ser preservados. Isso economizaria 256 bytes de armazenamento no sistema de arquivos, mas provavelmente não vale a pena o esforço para a maioria das aplicações. Veja a proposta 161 para informações adicionais e contexto.

DEST GENERATE não requer que uma sessão tenha sido criada primeiro.

DEST GENERATE não pode ser usado para criar um destino com assinaturas offline.

#### PING/PONG (SAM 3.2 ou superior)

O cliente ou o servidor podem enviar:

```
PING[ arbitrary text]
```
na porta de controle, com a resposta:

```
PONG[ arbitrary text from the ping]
```
para ser usado no keepalive do socket de controle. Qualquer lado pode fechar a sessão e o socket se nenhuma resposta for recebida em um tempo razoável, dependente da implementação.

Se ocorrer um timeout aguardando um PONG do cliente, a bridge pode enviar:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
e depois desconectar.

Se ocorrer um timeout aguardando um PONG da ponte, o cliente pode simplesmente desconectar.

PING/PONG não requerem que uma sessão tenha sido criada primeiro.

#### QUIT/STOP/EXIT (SAM 3.2 ou superior, recursos opcionais)

Os comandos QUIT, STOP e EXIT irão fechar a sessão e o socket. A implementação é opcional, para facilitar os testes via telnet. Se há alguma resposta antes do socket ser fechado (por exemplo, uma mensagem SESSION STATUS) é específico da implementação e está fora do escopo desta especificação.

QUIT/STOP/EXIT não exigem que uma sessão tenha sido criada primeiro.

#### HELP (recurso opcional)

Os servidores podem implementar um comando HELP. A implementação é opcional, para facilitar os testes via telnet. O formato de saída e a detecção do fim da saída são específicos da implementação e estão fora do escopo desta especificação.

HELP não requer que uma sessão tenha sido criada primeiro.

#### Configuração de Autorização (SAM 3.2 ou superior, recurso opcional)

Configuração de autorização usando o comando AUTH. Um servidor SAM pode implementar estes comandos para facilitar o armazenamento persistente de credenciais. A configuração de autenticação diferente destes comandos é específica da implementação e está fora do escopo desta especificação.

- AUTH ENABLE habilita a autorização em conexões subsequentes
- AUTH DISABLE desabilita a autorização em conexões subsequentes
- AUTH ADD USER="foo" PASSWORD="bar" adiciona um usuário/senha
- AUTH REMOVE USER="foo" remove este usuário

Aspas duplas para usuário e senha são recomendadas mas não obrigatórias. Uma aspa dupla dentro de um usuário ou senha deve ser escapada com uma barra invertida. Em caso de falha, o servidor responderá com um I2P_ERROR e uma mensagem.

AUTH não requer que uma sessão tenha sido criada primeiro.

### Valores RESULT

Estes são os valores que podem ser carregados pelo campo RESULT, com seus significados:

```
OK              Operation completed successfully
CANT_REACH_PEER The peer exists, but cannot be reached
DUPLICATED_DEST The specified Destination is already in use
I2P_ERROR       A generic I2P error (e.g. I2CP disconnection, etc.)
INVALID_KEY     The specified key is not valid (bad format, etc.)
KEY_NOT_FOUND   The naming system can't resolve the given name
PEER_NOT_FOUND  The peer cannot be found on the network
TIMEOUT         Timeout while waiting for an event (e.g. peer answer)
LEASESET_NOT_FOUND  See Name Lookup Options above. As of router API 0.9.66.
```
Diferentes implementações podem não ser consistentes em qual RESULT é retornado em vários cenários.

A maioria das respostas com um RESULT, além de OK, também incluirá uma MESSAGE com informações adicionais. A MESSAGE geralmente será útil para depurar problemas. No entanto, as strings MESSAGE são dependentes da implementação, podem ou não ser traduzidas pelo servidor SAM para a localidade atual, podem conter informações internas específicas da implementação como exceções, e estão sujeitas a mudanças sem aviso prévio. Embora os clientes SAM possam escolher expor strings MESSAGE aos usuários, eles não devem tomar decisões programáticas baseadas nessas strings, pois isso será frágil.

### Opções de Tunnel, I2CP e Streaming

Essas opções podem ser passadas como pares nome=valor na linha SAM SESSION CREATE.

Todas as sessões podem incluir [opções I2CP como comprimentos e quantidades de tunnel](/docs/protocol/i2cp#options). Sessões STREAM podem incluir [opções da biblioteca Streaming](/docs/api/streaming#options).

Consulte essas referências para nomes de opções e padrões. A documentação referenciada é para a implementação do router em Java. Os padrões estão sujeitos a alterações. Nomes de opções e valores são sensíveis a maiúsculas e minúsculas. Outras implementações de router podem não suportar todas as opções e podem ter padrões diferentes; consulte a documentação do router para detalhes.

### Notas sobre BASE 64

A codificação Base 64 deve usar o alfabeto Base 64 padrão do I2P "A-Z, a-z, 0-9, -, ~".

### Configuração Padrão do SAM

A porta SAM padrão é 7656. SAM não está habilitado por padrão no Java I2P Router; deve ser iniciado manualmente, ou configurado para iniciar automaticamente, na página de configuração de clientes no console do router, ou no arquivo clients.config. A porta SAM UDP padrão é 7655, escutando em 127.0.0.1. Essas podem ser alteradas no router Java adicionando os argumentos sam.udp.port=nnnnn e/ou sam.udp.host=w.x.y.z à invocação, ou na linha SESSION.

A configuração em outros routers é específica da implementação. Consulte [o guia de configuração do i2pd aqui](https://i2pd.readthedocs.io/en/latest/user-guide/configuration/).
