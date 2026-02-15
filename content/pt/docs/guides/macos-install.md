---
title: "Instalando o I2P no macOS"
description: "Guia passo a passo para instalar manualmente o I2P e suas dependências no macOS"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

## O Que Você Precisará

- Um Mac executando macOS 10.14 (Mojave) ou posterior
- Acesso de administrador para instalar aplicações
- Cerca de 15-20 minutos de tempo
- Conexão à internet para baixar os instaladores

## Visão Geral

Este processo de instalação tem quatro etapas principais:

1. **Instalar Java** - Baixe e instale o Oracle Java Runtime Environment
2. **Instalar I2P** - Baixe e execute o instalador do I2P
3. **Configurar Aplicação I2P** - Configure o lançador e adicione ao seu dock
4. **Configurar Largura de Banda I2P** - Execute o assistente de configuração para otimizar sua conexão

## Parte Um: Instalar Java

I2P requer Java para funcionar. Se você já tem Java 8 ou posterior instalado, pode [pular para a Parte Dois](#part-two-download-and-install-i2p).

### Passo 1: Baixar o Java

Visite a [página de download do Oracle Java](https://www.oracle.com/java/technologies/downloads/) e baixe o instalador para macOS do Java 8 ou posterior.

![Baixar Oracle Java para macOS](/images/guides/macos-install/0-jre.png)

### Passo 2: Execute o Instalador

Localize o arquivo `.dmg` baixado na sua pasta Downloads e clique duas vezes para abri-lo.

![Abrir o instalador do Java](/images/guides/macos-install/1-jre.png)

### Passo 3: Permitir Instalação

O macOS pode exibir um aviso de segurança porque o instalador é de um desenvolvedor identificado. Clique em **Abrir** para prosseguir.

![Conceder permissão ao instalador para prosseguir](/images/guides/macos-install/2-jre.png)

### Passo 4: Instalar Java

Clique em **Instalar** para iniciar o processo de instalação do Java.

![Start installing Java](/images/guides/macos-install/3-jre.png)

### Passo 5: Aguarde a Instalação

O instalador copiará arquivos e configurará o Java no seu sistema. Isso geralmente leva de 1 a 2 minutos.

![Aguarde a conclusão da instalação](/images/guides/macos-install/4-jre.png)

### Passo 6: Instalação Completa

Quando você vir a mensagem de sucesso, o Java está instalado! Clique em **Fechar** para finalizar.

![Instalação do Java concluída](/images/guides/macos-install/5-jre.png)

## Parte Dois: Baixar e Instalar I2P

Agora que o Java está instalado, você pode instalar o router I2P.

### Passo 1: Baixar I2P

Visite a [página de Downloads](/downloads/) e baixe o instalador **I2P para Unix/Linux/BSD/Solaris** (o arquivo `.jar`).

![Download I2P installer](/images/guides/macos-install/0-i2p.png)

### Passo 2: Executar o Instalador

Clique duas vezes no arquivo `i2pinstall_X.X.X.jar` baixado. O instalador será iniciado e solicitará que você selecione seu idioma preferido.

![Selecione seu idioma](/images/guides/macos-install/1-i2p.png)

### Passo 3: Tela de Boas-vindas

Leia a mensagem de boas-vindas e clique em **Próximo** para continuar.

![Installer introduction](/images/guides/macos-install/2-i2p.png)

### Passo 4: Aviso Importante

O instalador exibirá um aviso importante sobre atualizações. As atualizações do I2P são **assinadas ponta a ponta** e verificadas, mesmo que este instalador em si não seja assinado. Clique em **Avançar**.

![Aviso importante sobre atualizações](/images/guides/macos-install/3-i2p.png)

### Passo 5: Acordo de Licença

Leia o acordo de licença do I2P (licença estilo BSD). Clique em **Avançar** para aceitar.

![License agreement](/images/guides/macos-install/4-i2p.png)

### Passo 6: Selecionar Diretório de Instalação

Escolha onde instalar o I2P. A localização padrão (`/Applications/i2p`) é recomendada. Clique em **Próximo**.

![Selecionar diretório de instalação](/images/guides/macos-install/5-i2p.png)

### Passo 7: Selecionar Componentes

Deixe todos os componentes selecionados para uma instalação completa. Clique em **Próximo**.

![Selecionar componentes para instalar](/images/guides/macos-install/6-i2p.png)

### Passo 8: Iniciar Instalação

Revise suas escolhas e clique em **Próximo** para começar a instalação do I2P.

![Iniciar a instalação](/images/guides/macos-install/7-i2p.png)

### Passo 9: Instalando Arquivos

O instalador irá copiar os arquivos do I2P para o seu sistema. Isso leva cerca de 1-2 minutos.

![Instalação em progresso](/images/guides/macos-install/8-i2p.png)

### Passo 10: Gerar Scripts de Inicialização

O instalador cria scripts de inicialização para começar o I2P.

![Gerando scripts de inicialização](/images/guides/macos-install/9-i2p.png)

### Passo 11: Atalhos de Instalação

O instalador oferece a opção de criar atalhos na área de trabalho e entradas no menu. Faça suas seleções e clique em **Avançar**.

![Criar atalhos](/images/guides/macos-install/10-i2p.png)

### Passo 12: Instalação Concluída

Sucesso! O I2P está agora instalado. Clique em **Concluído** para finalizar.

![Instalação concluída](/images/guides/macos-install/11-i2p.png)

## Parte Três: Configurar Aplicação I2P

Agora vamos facilitar a execução do I2P adicionando-o à sua pasta Aplicações e ao Dock.

### Passo 1: Abrir Pasta de Aplicações

Abra o Finder e navegue até a pasta **Aplicações**.

![Abrir a pasta Aplicações](/images/guides/macos-install/0-conf.png)

### Passo 2: Encontre o Iniciador I2P

Procure pela pasta **I2P** ou pela aplicação **Start I2P Router** dentro de `/Applications/i2p/`.

![Encontre o lançador do I2P](/images/guides/macos-install/1-conf.png)

### Passo 3: Adicionar ao Dock

Arraste a aplicação **Start I2P Router** para o seu Dock para fácil acesso. Você também pode criar um alias na sua área de trabalho.

![Adicionar I2P ao seu Dock](/images/guides/macos-install/2-conf.png)

**Dica**: Clique com o botão direito no ícone I2P no Dock e selecione **Opções → Manter no Dock** para torná-lo permanente.

## Parte Quatro: Configurar Largura de Banda do I2P

Quando você iniciar o I2P pela primeira vez, passará por um assistente de configuração para definir suas configurações de largura de banda. Isso ajuda a otimizar o desempenho do I2P para sua conexão.

### Passo 1: Iniciar o I2P

Clique no ícone I2P no seu Dock (ou clique duas vezes no lançador). Seu navegador web padrão abrirá no I2P Router Console.

![Tela de boas-vindas do Console do Router I2P](/images/guides/macos-install/0-wiz.png)

### Passo 2: Assistente de Boas-vindas

O assistente de configuração irá cumprimentá-lo. Clique em **Avançar** para começar a configurar o I2P.

![Introdução do assistente de configuração](/images/guides/macos-install/1-wiz.png)

### Passo 3: Idioma e Tema

Selecione seu **idioma de interface** preferido e escolha entre o tema **claro** ou **escuro**. Clique em **Avançar**.

![Selecionar idioma e tema](/images/guides/macos-install/2-wiz.png)

### Passo 4: Informações do Teste de Largura de Banda

O assistente explicará o teste de largura de banda. Este teste conecta ao serviço **M-Lab** para medir a velocidade da sua internet. Clique em **Próximo** para prosseguir.

![Bandwidth test explanation](/images/guides/macos-install/3-wiz.png)

### Passo 5: Executar Teste de Largura de Banda

Clique em **Executar Teste** para medir suas velocidades de upload e download. O teste leva cerca de 30-60 segundos.

![Executando o teste de largura de banda](/images/guides/macos-install/4-wiz.png)

### Passo 6: Resultados dos Testes

Revise seus resultados de teste. O I2P recomendará configurações de largura de banda baseadas na velocidade da sua conexão.

![Resultados do teste de largura de banda](/images/guides/macos-install/5-wiz.png)

### Passo 7: Configurar Compartilhamento de Largura de Banda

Escolha quanta largura de banda você quer compartilhar com a rede I2P:

- **Automático** (Recomendado): O I2P gerencia a largura de banda baseado no seu uso
- **Limitado**: Define limites específicos de upload/download
- **Ilimitado**: Compartilha o máximo possível (para conexões rápidas)

Clique em **Próximo** para salvar suas configurações.

![Configure bandwidth sharing](/images/guides/macos-install/6-wiz.png)

### Passo 8: Configuração Concluída

Seu router I2P agora está configurado e funcionando! O console do router mostrará o status da sua conexão e permitirá navegar em sites I2P.

## Começando com I2P

Agora que o I2P está instalado e configurado, você pode:

1. **Navegar em sites I2P**: Visite a `http://127.0.0.1:7657/home` para ver links para serviços populares do I2P
2. **Configure seu navegador**: Configure um [perfil do navegador](/docs/guides/browser-config) para acessar sites `.i2p`
3. **Explore serviços**: Confira email I2P, fóruns, compartilhamento de arquivos e muito mais
4. **Monitore seu router**: O `http://127.0.0.1:7657/console` mostra o status da sua rede e estatísticas

### Links Úteis

- **Console do Router**: `http://127.0.0.1:7657/`
- **Configuração**: `http://127.0.0.1:7657/config`
- **Livro de Endereços**: `http://127.0.0.1:7657/susidns/addressbook`
- **Configurações de Largura de Banda**: `http://127.0.0.1:7657/config`

## Executando Novamente o Assistente de Configuração

Se você quiser alterar suas configurações de largura de banda ou reconfigurar o I2P mais tarde, pode executar novamente o assistente de boas-vindas a partir do Console do Router:

1. Vá para `http://127.0.0.1:7657/welcome`
2. Siga novamente os passos do assistente

## Solução de Problemas

### O I2P Não Inicia

- **Verificar Java**: Certifique-se de que o Java está instalado executando `java -version` no Terminal
- **Verificar permissões**: Garanta que a pasta do I2P tenha as permissões corretas
- **Verificar logs**: Examine `~/.i2p/wrapper.log` para mensagens de erro

### O Navegador Não Consegue Acessar Sites I2P

- Certifique-se de que o I2P está em execução (verifique o Router Console)
- Configure as definições de proxy do seu navegador para usar o proxy HTTP `127.0.0.1:4444`
- Aguarde 5-10 minutos após iniciar para que o I2P se integre na rede

### Desempenho Lento

- Execute o teste de largura de banda novamente e ajuste suas configurações
- Certifique-se de que está compartilhando alguma largura de banda com a rede
- Verifique o status da sua conexão no Router Console

## Desinstalando o I2P

Para remover o I2P do seu Mac:

1. Feche o router I2P se estiver em execução
2. Exclua a pasta `/Applications/i2p`
3. Exclua a pasta `~/.i2p` (sua configuração e dados do I2P)
4. Remova o ícone do I2P do seu Dock

## Próximos Passos

- **Junte-se à comunidade**: Visite [i2pforum.net](http://i2pforum.net) ou confira o I2P no Reddit
- **Saiba mais**: Leia a [documentação do I2P](/en/docs) para entender como a rede funciona
- **Envolva-se**: Considere [contribuir para o desenvolvimento do I2P](/en/get-involved) ou executar infraestrutura

Parabéns! Você agora faz parte da rede I2P. Bem-vindo à internet invisível!

---
