---
title: "Incorporando I2P na sua Aplicação"
description: "Diretrizes para incluir um router I2P com sua aplicação"
slug: "embedding"
lastUpdated: "2023-01"
accurateFor: "2.1.0"
---

## Visão Geral

Esta página é sobre incluir todo o binário do router I2P com sua aplicação. Não é sobre escrever uma aplicação para funcionar com I2P (seja incluída ou externa). No entanto, muitas das diretrizes podem ser úteis mesmo se não estiver incluindo um router.

Muitos projetos estão incluindo, ou falando sobre incluir, I2P. Isso é ótimo se feito corretamente. Se feito de forma errada, pode causar danos reais à nossa rede. O router I2P é complexo, e pode ser um desafio ocultar toda essa complexidade dos seus usuários. Esta página discute algumas diretrizes gerais.

A maioria destas diretrizes se aplica igualmente ao Java I2P ou i2pd. No entanto, algumas diretrizes são específicas do Java I2P e são observadas abaixo.

### Fale conosco

Inicie um diálogo. Estamos aqui para ajudar. Aplicações que incorporam I2P são as oportunidades mais promissoras - e empolgantes - para crescermos a rede e melhorarmos o anonimato para todos.

### Escolha seu router com sabedoria

Se sua aplicação é em Java ou Scala, é uma escolha fácil - use o router Java. Se em C/C++, recomendamos o i2pd. O desenvolvimento do i2pcpp foi interrompido. Para aplicações em outras linguagens, é melhor usar SAMv3 ou BOB ou SOCKS e incluir o router Java como um processo separado. Algumas das informações a seguir aplicam-se apenas ao router Java.

### Licenciamento

Certifique-se de atender aos requisitos de licença do software que está empacotando.

---

## Configuração

### Verificar configuração padrão

Uma configuração padrão correta é crucial. A maioria dos usuários não alterará os padrões. Os padrões para sua aplicação podem precisar ser diferentes dos padrões para o router que você está incluindo. Substitua os padrões do router se necessário.

Alguns padrões importantes para revisar: largura de banda máxima, quantidade e comprimento de tunnels, tunnels participantes máximos. Muito disso depende da largura de banda esperada e dos padrões de uso da sua aplicação.

Configure largura de banda e tunnels suficientes para permitir que seus usuários contribuam para a rede. Considere desabilitar o I2CP externo, pois você provavelmente não precisa dele e isso entraria em conflito com qualquer outra instância I2P em execução. Também verifique as configurações para desabilitar o encerramento da JVM na saída, por exemplo.

### Considerações sobre Tráfego de Participação

Pode ser tentador para você desabilitar o tráfego de participação. Existem várias maneiras de fazer isso (modo oculto, configurar max tunnels para 0, configurar largura de banda compartilhada abaixo de 12 KBytes/sec). Sem tráfego de participação, você não precisa se preocupar com desligamento gracioso, seus usuários não veem uso de largura de banda não gerado por eles, etc. No entanto, existem muitas razões pelas quais você deveria permitir tunnels de participação.

Em primeiro lugar, o router não funciona tão bem se não tiver a chance de se "integrar" com a rede, o que é tremendamente ajudado por outros construindo tunnels através de você.

Em segundo lugar, mais de 90% dos routers na rede atual permitem tráfego de participação. É o padrão no router Java. Se sua aplicação não roteia para outros e se torna realmente popular, então ela se torna uma sanguessuga na rede, e perturba o equilíbrio que temos agora. Se ficar realmente grande, então nos tornamos o Tor, e passamos nosso tempo implorando para as pessoas habilitarem o relay.

Em terceiro lugar, o tráfego participante é tráfego de cobertura que ajuda o anonimato dos seus utilizadores.

Desencorajamos fortemente que você desative o tráfego participante por padrão. Se você fizer isso e sua aplicação se tornar muito popular, isso pode quebrar a rede.

### Persistência

Você deve salvar os dados do router (netDb, configuração, etc.) entre execuções do router. O I2P não funciona bem se você precisar fazer reseed a cada inicialização, e isso gera uma carga enorme nos nossos servidores de reseed, além de não ser muito bom para o anonimato também. Mesmo se você incluir router infos, o I2P precisa de dados de perfil salvos para melhor desempenho. Sem persistência, seus usuários terão uma experiência de inicialização ruim.

Há duas possibilidades se você não conseguir fornecer persistência. Qualquer uma delas elimina a carga do seu projeto em nossos servidores de reseed e melhorará significativamente o tempo de inicialização.

1) Configure seus próprios servidores de reseed do projeto que sirvam muito mais do que o número usual de informações de router no reseed, digamos, várias centenas. Configure o router para usar apenas seus servidores.

2) Inclua mil a duas mil informações de router no seu instalador.

Além disso, atrase ou escalone a inicialização dos seus tunnels, para dar ao router uma chance de se integrar antes de construir muitos tunnels.

### Configurabilidade

Forneça aos seus usuários uma forma de alterar a configuração das definições importantes. Entendemos que você provavelmente quererá ocultar a maior parte da complexidade do I2P, mas é importante mostrar algumas configurações básicas. Além dos padrões acima, algumas configurações de rede como UPnP, IP/porta podem ser úteis.

### Considerações sobre Floodfill

Acima de uma determinada configuração de largura de banda, e atendendo a outros critérios de saúde, seu router se tornará floodfill, o que pode causar um grande aumento nas conexões e no uso de memória (pelo menos com o router Java). Considere se isso é aceitável. Você pode desativar o floodfill, mas então seus usuários mais rápidos não estarão contribuindo com o que poderiam. Também depende do tempo de atividade típico da sua aplicação.

### Reseeding

Decida se você está incluindo informações do router ou usando nossos hosts de reseed. A lista de hosts de reseed do Java está no código-fonte, então se você mantiver seu código-fonte atualizado, a lista de hosts também estará. Esteja ciente do possível bloqueio por governos hostis.

### Usar Clientes Compartilhados

O Java I2P i2ptunnel suporta clientes compartilhados, onde os clientes podem ser configurados para usar um único pool. Se você precisar de múltiplos clientes, e se for consistente com seus objetivos de segurança, configure os clientes para serem compartilhados.

### Limitar Quantidade de Tunnels

Especifique a quantidade de tunnels explicitamente com as opções `inbound.quantity` e `outbound.quantity`. O padrão no Java I2P é 2; o padrão no i2pd é maior. Especifique na linha SESSION CREATE usando SAM para obter configurações consistentes com ambos os routers. Dois para cada entrada/saída é suficiente para a maioria das aplicações de baixa a média largura de banda e baixa a média distribuição. Servidores e aplicações P2P de alta distribuição podem precisar de mais. Consulte [este post do fórum](http://zzz.i2p/topics/1584) para orientação sobre como calcular os requisitos para servidores e aplicações de alto tráfego.

### Especificar SAM SIGNATURE_TYPE

SAM usa como padrão DSA_SHA1 para destinos, o que não é o que você quer. Ed25519 (tipo 7) é a seleção correta. Adicione SIGNATURE_TYPE=7 ao comando DEST GENERATE, ou ao comando SESSION CREATE para DESTINATION=TRANSIENT.

### Limitar Sessões SAM

A maioria das aplicações precisará apenas de uma sessão SAM. O SAM oferece a capacidade de sobrecarregar rapidamente o router local, ou até mesmo a rede mais ampla, se um grande número de sessões for criado. Se múltiplos sub-serviços puderem usar uma única sessão, configure-os com uma sessão PRIMARY e SUBSESSIONS (atualmente não suportado no i2pd). Um limite razoável para sessões é de 3 ou 4 no total, ou talvez até 10 para situações raras. Se você tiver múltiplas sessões, certifique-se de especificar uma quantidade baixa de tunnels para cada uma, veja acima.

Em quase nenhuma situação você deveria necessitar de uma sessão única por conexão. Sem um design cuidadoso, isso poderia rapidamente causar DDoS na rede. Considere cuidadosamente se seus objetivos de segurança requerem sessões únicas. Por favor, consulte os desenvolvedores do Java I2P ou i2pd antes de implementar sessões por conexão.

### Reduzir o Uso de Recursos de Rede

Note que essas opções não são atualmente suportadas no i2pd. Essas opções são suportadas via I2CP e SAM (exceto delay-open, que é apenas via i2ptunnel). Consulte a documentação do I2CP (e, para delay-open, a documentação de configuração do i2ptunnel) para detalhes.

Considere configurar os tunnels da sua aplicação para delay-open, reduce-on-idle e/ou close-on-idle. Isso é simples se estiver usando i2ptunnel, mas você terá que implementar parte disso por conta própria se estiver usando I2CP diretamente. Veja o i2psnark para código que reduz a contagem de tunnels e depois fecha o tunnel, mesmo na presença de alguma atividade DHT em segundo plano.

---

## Ciclo de Vida

### Capacidade de Atualização

Tenha um recurso de atualização automática se possível, ou pelo menos notificação automática de uma nova versão. Nosso maior receio é um grande número de routers por aí que não podem ser atualizados. Temos cerca de 6-8 lançamentos por ano do router Java, e é fundamental para a saúde da rede que os usuários se mantenham atualizados. Geralmente temos mais de 80% da rede na versão mais recente dentro de 6 semanas após o lançamento, e gostaríamos de manter assim. Você não precisa se preocupar em desabilitar a função de atualização automática integrada do router, já que esse código está no console do router, que presumivelmente você não está incluindo no pacote.

### Implementação

Tenha um plano de implementação gradual. Não sobrecarregue a rede de uma só vez. Atualmente temos aproximadamente 25 mil usuários únicos por dia e 40 mil únicos por mês. Provavelmente conseguimos lidar com um crescimento de 2-3X por ano sem muito problema. Se você antecipa um crescimento mais rápido que isso, OU a distribuição de largura de banda (ou distribuição de tempo de atividade, ou qualquer outra característica significativa) da sua base de usuários é significativamente diferente da nossa base atual, realmente precisamos ter uma discussão. Quanto maiores seus planos de crescimento, mais importante é tudo o mais nesta lista de verificação.

### Projete para e Encoraje Longos Tempos de Atividade

Informe aos seus usuários que o I2P funciona melhor se continuar em execução. Podem ser necessários vários minutos após a inicialização antes de funcionar bem, e ainda mais tempo após a primeira instalação. Se o seu tempo médio de atividade for inferior a uma hora, o I2P provavelmente não é a solução adequada.

---

## Interface do Usuário

### Mostrar Status

Forneça alguma indicação ao usuário de que os tunnels da aplicação estão prontos. Incentive a paciência.

### Encerramento Gracioso

Se possível, atrase o desligamento até que seus tunnels participantes expirem. Não deixe seus usuários quebrarem tunnels facilmente, ou pelo menos peça para confirmarem.

### Educação e Doação

Seria bom se você fornecesse aos seus usuários links para aprender mais sobre o I2P e para fazer doações.

### Opção de Router Externo

Dependendo da sua base de usuários e aplicação, pode ser útil fornecer uma opção ou um pacote separado para usar um router externo.

---

## Outros Tópicos

### Uso de outros Serviços Comuns

Se você planeja usar ou conectar-se a outros serviços comuns do I2P (feeds de notícias, assinaturas de hosts.txt, trackers, outproxies, etc.), certifique-se de não sobrecarregá-los e converse com as pessoas que os administram para garantir que está tudo bem.

### Problemas de Tempo / NTP

Nota: Esta seção refere-se ao Java I2P. O i2pd não inclui um cliente SNTP.

O I2P inclui um cliente SNTP. O I2P requer horário correto para operar. Ele compensará um relógio de sistema desajustado, mas isso pode atrasar a inicialização. Você pode desabilitar as consultas SNTP do I2P, mas isso não é recomendado, a menos que sua aplicação garanta que o relógio do sistema esteja correto.

### Escolha O Que e Como Agrupar

Nota: Esta seção refere-se apenas ao I2P Java.

No mínimo você precisará dos arquivos i2p.jar, router.jar, streaming.jar e mstreaming.jar. Você pode omitir os dois jars de streaming para uma aplicação somente de datagramas. Algumas aplicações podem precisar de mais, por exemplo i2ptunnel.jar ou addressbook.jar. Não esqueça do jbigi.jar, ou um subconjunto dele para as plataformas que você suporta, para tornar a criptografia muito mais rápida. Java 7 ou superior é necessário para compilar. Se você está compilando pacotes Debian / Ubuntu, você deve exigir o pacote I2P do nosso PPA em vez de incluí-lo. Você quase certamente não precisa do susimail, susidns, do console do router e do i2psnark, por exemplo.

Os seguintes arquivos devem ser incluídos no diretório de instalação do I2P, especificado com a propriedade "i2p.dir.base". Não se esqueça do diretório certificates/, que é necessário para reseeding, e blocklist.txt para validação de IP. O diretório geoip é opcional, mas recomendado para que o router possa tomar decisões baseadas na localização. Se incluir geoip, certifique-se de colocar o arquivo GeoLite2-Country.mmdb nesse diretório (descomprima-o de installer/resources/GeoLite2-Country.mmdb.gz). O arquivo hosts.txt pode ser necessário, você pode modificá-lo para incluir quaisquer hosts que sua aplicação utilize. Você pode adicionar um arquivo router.config ao diretório base para sobrepor os padrões iniciais. Revise e edite ou remova os arquivos clients.config e i2ptunnel.config.

Os requisitos de licença podem exigir que você inclua o arquivo LICENSES.txt e o diretório de licenças.

- Você também pode desejar incluir um arquivo hosts.txt.
- Certifique-se de especificar um bootclasspath se estiver compilando Java I2P para sua versão, em vez de usar nossos binários.

### Considerações sobre Android

Nota: Esta seção refere-se apenas ao Java I2P.

Nosso aplicativo router Android pode ser compartilhado por múltiplos clientes. Se não estiver instalado, o usuário será solicitado quando iniciar um aplicativo cliente.

Alguns desenvolvedores expressaram preocupação de que esta é uma experiência de usuário ruim, e desejam incorporar o router em sua aplicação. Temos uma biblioteca de serviço de router Android em nosso roteiro, que poderia facilitar a incorporação. Mais informações necessárias.

Se precisar de assistência, por favor entre em contato conosco.

### JARs do Maven

Nota: Esta seção refere-se apenas ao Java I2P.

Temos um número limitado de nossos jars no [Maven Central](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22net.i2p%22). Existem vários tickets no trac para resolvermos que irão melhorar e expandir os jars lançados no Maven Central.

Se precisar de assistência, entre em contato conosco.

### Considerações sobre Datagram (DHT)

Se sua aplicação está usando datagramas I2P, por exemplo para uma DHT, há muitas opções avançadas disponíveis para reduzir overhead e aumentar confiabilidade. Isso pode levar algum tempo e experimentação para funcionar bem. Esteja ciente das compensações entre tamanho/confiabilidade. Converse conosco para obter ajuda. É possível - e recomendado - usar Datagramas e Streaming no mesmo Destination. Não crie Destinations separados para isso. Não tente armazenar seus dados não relacionados nas DHTs existentes da rede (iMule, bote, bittorrent, e router). Construa a sua própria. Se você está codificando nós seed fixos, recomendamos que tenha vários.

### Outproxies

Os outproxies do I2P para a clearnet são um recurso limitado. Use outproxies apenas para navegação web normal iniciada pelo usuário ou outro tráfego limitado. Para qualquer outro uso, consulte e obtenha aprovação do operador do outproxy.

### Comarketing

Vamos trabalhar juntos. Não espere até estar pronto. Nos forneça seu perfil do Twitter e comece a tweetar sobre isso, retribuiremos o favor.

### Malware

Por favor, não use o I2P para o mal. Isso poderia causar grandes danos tanto à nossa rede quanto à nossa reputação.

### Junte-se a Nós

Isso pode ser óbvio, mas junte-se à comunidade. Execute o I2P 24/7. Crie um I2P Site sobre seu projeto. Participe do IRC #i2p-dev. Poste nos fóruns. Espalhe a palavra. Podemos ajudar você a conseguir usuários, testadores, tradutores ou até mesmo programadores.

---

## Exemplos

### Exemplos de Aplicação

Você pode querer instalar e experimentar o aplicativo Android I2P, e examinar seu código, como exemplo de uma aplicação que integra o router. Veja o que expomos ao usuário e o que ocultamos. Observe a máquina de estados que usamos para iniciar e parar o router. Outros exemplos são: Vuze, o aplicativo Android Nightweb, iMule, TAILS, iCloak e Monero.

### Exemplo de Código

Nota: Esta seção se refere apenas ao Java I2P.

Nada do que foi mencionado acima realmente lhe diz como escrever seu código para agrupar o router Java, então a seguir está um breve exemplo.

```java
import java.util.Properties;
import net.i2p.router.Router;

	Properties p = new Properties();
        // add your configuration settings, directories, etc.
        // where to find the I2P installation files
	p.addProperty("i2p.dir.base", baseDir);
        // where to find the I2P data files
	p.addProperty("i2p.dir.config", configDir);
        // bandwidth limits in K bytes per second
	p.addProperty("i2np.inboundKBytesPerSecond", "50");
	p.addProperty("i2np.outboundKBytesPerSecond", "50");
	p.addProperty("router.sharePercentage", "80");
	p.addProperty("foo", "bar");
	Router r = new Router(p);
        // don't call exit() when the router stops
	r.setKillVMOnEnd(false);
	r.runRouter();

	...

	r.shutdownGracefully();
	// will shutdown in 11 minutes or less
```
Este código é para o caso onde sua aplicação inicia o router, como em nosso aplicativo Android. Você também poderia fazer o router iniciar a aplicação via arquivos clients.config e i2ptunnel.config, junto com webapps Jetty, como é feito em nossos pacotes Java. Como sempre, o gerenciamento de estado é a parte difícil.

Veja também: [os javadocs do Router](http://idk.i2p/javadoc-i2p/net/i2p/router/Router.html).
