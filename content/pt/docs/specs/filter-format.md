---
title: "Formato do Filtro de Acesso"
description: "Sintaxe para arquivos de filtro de controle de acesso de tunnel"
slug: "filter-format"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
type: docs
---

## Visão Geral

A definição de um filtro é uma lista de Strings. Linhas em branco e linhas que começam com `#` são ignoradas. Mudanças na definição do filtro entram em vigor na reinicialização do tunnel.

Cada linha pode representar um destes itens:

- Definição de um limiar padrão a ser aplicado a quaisquer destinos remotos não listados neste arquivo ou em qualquer um dos arquivos referenciados
- Definição de um limiar a ser aplicado a um destino remoto específico
- Definição de um limiar a ser aplicado a destinos remotos listados em um arquivo
- Definição de um limiar que, se ultrapassado, fará com que o destino remoto infrator seja registrado em um arquivo especificado

A ordem das definições importa. O primeiro limite para um determinado destino (seja explícito ou listado em um arquivo) substitui quaisquer limites futuros para o mesmo destino, sejam explícitos ou listados em um arquivo.

## Limites

Um threshold é definido pelo número de tentativas de conexão que um destino remoto tem permissão para realizar durante um número especificado de segundos antes que uma "violação" ocorra. Por exemplo, a seguinte definição de threshold `15/5` significa que o mesmo destino remoto tem permissão para fazer 14 tentativas de conexão durante um período de 5 segundos. Se ele fizer mais uma tentativa dentro do mesmo período, o threshold será violado.

O formato do limite pode ser um dos seguintes:

- **Definição numérica** do número de conexões sobre número de segundos - `15/5`, `30/60`, e assim por diante. Note que se o número de conexões for 1 (como por exemplo em `1/1`) a primeira tentativa de conexão resultará numa violação.
- A palavra **`allow`**. Este limite nunca é violado, ou seja, número infinito de tentativas de conexão é permitido.
- A palavra **`deny`**. Este limite é sempre violado, ou seja, nenhuma tentativa de conexão será permitida.

### Limite Padrão

O limite padrão se aplica a qualquer destino remoto que não esteja explicitamente listado na definição ou em qualquer um dos arquivos referenciados. Para definir um limite padrão, use a palavra-chave `default`. A seguir estão exemplos de limites padrão:

```text
15/5 default
allow default
deny default
```
Pode haver apenas uma definição de limite padrão por filtro. Se for omitida, o filtro permitirá conexões desconhecidas por padrão.

### Limites Explícitos

Limites explícitos são aplicados a um destino remoto listado na própria definição. Exemplos:

```text
15/5 explicit asdfasdfasdf.b32.i2p
allow explicit fdsafdsafdsa.b32.i2p
deny explicit qwerqwerqwer.b32.i2p
```
### Limites de Volume

Por conveniência, é possível manter uma lista de destinos em um arquivo e definir um limite para todos eles em lote. Exemplos:

```text
15/5 file /path/throttled_destinations.txt
deny file /path/forbidden_destinations.txt
allow file /path/unlimited_destinations.txt
```
Estes arquivos podem ser editados manualmente enquanto o tunnel está em execução. Alterações nestes arquivos podem levar até 10 segundos para entrar em vigor.

## Gravadores

Recorders rastreiam tentativas de conexão feitas por um destino remoto, e se isso ultrapassar um certo limite, esse destino é registrado em um arquivo específico. Exemplos:

```text
30/5 record /path/aggressive.txt
60/5 record /path/very_aggressive.txt
```
É possível usar um gravador para registrar destinos agressivos em um arquivo específico, e então usar esse mesmo arquivo para limitá-los. Por exemplo, o trecho a seguir definirá um filtro que inicialmente permite todas as tentativas de conexão, mas se qualquer destino individual exceder 30 tentativas por 5 segundos, ele será limitado a 15 tentativas por 5 segundos:

```text
# by default there are no limits
allow default
# but record overly aggressive destinations
30/5 record /path/throttled.txt
# and any that end up in that file will get throttled in the future
15/5 file /path/throttled.txt
```
É possível usar um gravador em um tunnel que escreve em um arquivo que controla a velocidade de outro tunnel. É possível reutilizar o mesmo arquivo com destinos em múltiplos tunnels. E, claro, é possível editar esses arquivos manualmente.

Aqui está um exemplo de definição de filtro que aplica algum throttling por padrão, nenhum throttling para destinations no arquivo `friends.txt`, proíbe quaisquer conexões de destinations no arquivo `enemies.txt` e registra qualquer comportamento agressivo em um arquivo chamado `suspicious.txt`:

```text
15/5 default
allow file /path/friends.txt
deny file /path/enemies.txt
60/5 record /path/suspicious.txt
```