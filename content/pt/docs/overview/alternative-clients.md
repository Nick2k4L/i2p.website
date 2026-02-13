---
title: "Clientes I2P Alternativos"
description: "Implementações de clientes I2P mantidas pela comunidade (atualizado para 2025)"
slug: "alternative-clients"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

A implementação principal do cliente I2P usa **Java**. Se você não pode ou prefere não usar Java em um sistema específico, existem implementações alternativas de cliente I2P desenvolvidas e mantidas por membros da comunidade. Esses programas fornecem a mesma funcionalidade principal usando diferentes linguagens de programação ou abordagens.

---

## Tabela de Comparação

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Client</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Language</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Maturity</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Actively Maintained</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Suitable For</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Java I2P</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes (official)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">General users</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Standard full router; includes console, plugins, and tools</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>i2pd</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Low-resource systems, servers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Lightweight, fully compatible with Java I2P, includes web console</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Go-I2P</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Experimental</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">⚙️ In development</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Developers, testing</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Early-stage Go implementation; not yet production ready</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>Emissary</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Experimental</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">⚙️ In development</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Developers, embedded use</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Rust I2P implementation; embeddable router with eepsite, torrent, IRC and email support</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"><strong>I2P+</strong></td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Stable (fork)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">✅ Yes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Advanced users</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Enhanced Java I2P fork with UI and performance improvements</td>
    </tr>
  </tbody>
</table>
---

## i2pd (C++)

**Website:** [https://i2pd.website](https://i2pd.website)

**Descrição:** i2pd (o *I2P Daemon*) é um cliente I2P completo implementado em C++. Tem sido estável para uso em produção por muitos anos (desde cerca de 2016) e é mantido ativamente pela comunidade. O i2pd implementa completamente os protocolos de rede e APIs do I2P, tornando-o totalmente compatível com a rede Java I2P. Este router C++ é frequentemente usado como uma alternativa leve em sistemas onde o runtime Java não está disponível ou não é desejado. O i2pd inclui um console web integrado para configuração e monitoramento. É multiplataforma e disponível em muitos formatos de empacotamento — existe até mesmo uma versão Android do i2pd disponível (por exemplo, via F-Droid).

---

## Go-I2P (Go)

**Repositório:** [https://github.com/go-i2p/go-i2p](https://github.com/go-i2p/go-i2p)

**Descrição:** Go-I2P é um cliente I2P escrito na linguagem de programação Go. É uma implementação independente do router I2P, visando aproveitar a eficiência e portabilidade do Go. O projeto está em desenvolvimento ativo, mas ainda está em estágio inicial e não possui todas as funcionalidades completas. A partir de 2025, Go-I2P é considerado experimental — está sendo ativamente trabalhado por desenvolvedores da comunidade, mas não é recomendado para uso em produção até amadurecer mais. O objetivo do Go-I2P é fornecer um router I2P moderno e leve com compatibilidade total com a rede I2P uma vez que o desenvolvimento esteja completo.

---

## Emissary (Rust)

**Website:** [https://altonen.github.io/emissary/](https://altonen.github.io/emissary/)

**Descrição:** Emissary é uma implementação em Rust da pilha de protocolos I2P, projetada para funcionar como um router I2P incorporável. Pode ser integrado em outras aplicações ou executado de forma independente. O Emissary suporta hospedagem de eepsites, torrents, IRC e serviços de email. O projeto inclui documentação extensa cobrindo configuração rápida, incorporação para desenvolvedores e configuração detalhada. Como um projeto experimental, está em desenvolvimento ativo e ainda não é recomendado para uso em produção.

---

## I2P+ (fork Java)

**Website:** [https://i2pplus.github.io](https://i2pplus.github.io)

**Descrição:** I2P+ é um fork mantido pela comunidade do cliente Java I2P padrão. Não é uma reimplementação em uma nova linguagem, mas sim uma versão aprimorada do router Java com recursos e otimizações adicionais. O I2P+ foca em oferecer uma experiência do usuário melhorada e melhor desempenho, mantendo-se totalmente compatível com a rede I2P oficial. Ele introduz uma interface de console web renovada, opções de configuração mais amigáveis ao usuário e várias otimizações (por exemplo, desempenho aprimorado de torrent e melhor tratamento de peers de rede, especialmente para routers atrás de firewalls). O I2P+ requer um ambiente Java assim como o software I2P oficial, portanto não é uma solução para ambientes sem Java. No entanto, para usuários que possuem Java e desejam uma versão alternativa com capacidades extras, o I2P+ oferece uma opção atraente. Este fork é mantido atualizado com os lançamentos upstream do I2P (com sua numeração de versão adicionando um "+") e pode ser obtido no site do projeto.
