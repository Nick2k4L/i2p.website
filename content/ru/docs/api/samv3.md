---
title: "SAM V3"
description: "Протокол простого анонимного обмена сообщениями для non-Java I2P приложений"
slug: "samv3"
aliases: 
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

SAM — это простой клиентский протокол для взаимодействия с I2P. SAM является рекомендуемым протоколом для приложений не на Java для подключения к сети I2P и поддерживается несколькими реализациями router. Java-приложения должны использовать streaming или I2CP API напрямую.

SAMv3 была представлена в релизе I2P 0.7.3 (май 2009) и является стабильным и поддерживаемым интерфейсом. Версия 3.1 также стабильна и поддерживает опцию типа подписи, что настоятельно рекомендуется. Более поздние версии 3.x поддерживают расширенные функции. Обратите внимание, что i2pd в настоящее время не поддерживает большинство функций версий 3.2 и 3.3.

Альтернативы: [SOCKS](/docs/api/socks), [Streaming](/docs/api/streaming), [I2CP](/docs/protocol/i2cp), [BOB (устаревший)](/docs/api/bob). Устаревшие версии: [SAM V1](/docs/api/sam), [SAM V2](/docs/api/samv2).

## Известные библиотеки SAM

Внимание: Некоторые из них могут быть очень старыми или неподдерживаемыми. Ни один из них не тестируется, не рецензируется и не поддерживается проектом I2P, если не указано иное ниже. Проводите собственные исследования.

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
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Typescript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/diva-exchange/i2p-sam">github.com/diva-exchange/i2p-sam</a></td>
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
## Быстрый старт

Для реализации базового TCP-приложения типа peer-to-peer клиент должен поддерживать следующие команды:

- `HELLO VERSION MIN=3.1 MAX=3.1` - Необходимо для всех остальных команд
- `DEST GENERATE SIGNATURE_TYPE=7` - Для генерации нашего приватного ключа и destination
- `NAMING LOOKUP NAME=...` - Для преобразования .i2p адресов в destinations
- `SESSION CREATE STYLE=STREAM ID=... DESTINATION=... i2cp.leaseSetEncType=4,0` - Необходимо для STREAM CONNECT и STREAM ACCEPT
- `STREAM CONNECT ID=... DESTINATION=...` - Для исходящих соединений
- `STREAM ACCEPT ID=...` - Для принятия входящих соединений

## Общее руководство для разработчиков

### Проектирование приложений

SAM сессии (или внутри I2P, tunnel pools или наборы туннелей) спроектированы как долгоживущие. Большинству приложений понадобится только одна сессия, создаваемая при запуске и закрываемая при выходе. I2P отличается от Tor, где цепочки могут быстро создаваться и отбрасываться. Подумайте внимательно и проконсультируйтесь с разработчиками I2P перед тем, как проектировать ваше приложение для использования более чем одной или двух одновременных сессий, или для их быстрого создания и отбрасывания. Большинство моделей угроз не потребуют уникальной сессии для каждого соединения.

Также, пожалуйста, убедитесь, что настройки вашего приложения (и рекомендации для пользователей по настройкам router или настройки router по умолчанию, если вы включаете router в комплект) приведут к тому, что ваши пользователи будут вносить в сеть больше ресурсов, чем потребляют. I2P — это одноранговая сеть, и сеть не сможет выжить, если популярное приложение приведет её к постоянной перегрузке.

### Совместимость и тестирование

Реализации Java I2P и i2pd router являются независимыми и имеют незначительные различия в поведении, поддержке функций и настройках по умолчанию. Пожалуйста, протестируйте ваше приложение с последними версиями обоих router'ов.

SAM в i2pd включен по умолчанию; SAM в Java I2P - нет. Предоставьте пользователям инструкции о том, как включить SAM в Java I2P (через /configclients в консоли router), и/или предоставьте понятное сообщение об ошибке пользователю, если первоначальное подключение не удается, например "убедитесь, что I2P запущен и интерфейс SAM включен".

Java I2P и i2pd router имеют разные значения по умолчанию для количества tunnel. Значение по умолчанию для Java равно 2, а для i2pd — 5. Для большинства случаев с низкой и средней пропускной способностью и низким и средним количеством соединений достаточно 2 или 3. Пожалуйста, укажите количество tunnel в сообщении SESSION CREATE, чтобы получить стабильную производительность с Java I2P и i2pd router. См. ниже.

Для получения дополнительных рекомендаций разработчикам о том, как обеспечить использование приложением только необходимых ресурсов, пожалуйста, ознакомьтесь с [нашим руководством по включению I2P в ваше приложение](/docs/applications/embedding).

### Типы подписей и шифрования

I2P поддерживает множество типов подписей и шифрования. Для обратной совместимости SAM по умолчанию использует старые и неэффективные типы, поэтому все клиенты должны указывать более новые типы.

Тип подписи указывается в командах DEST GENERATE и SESSION CREATE (для временных). Все клиенты должны устанавливать `SIGNATURE_TYPE=7` (Ed25519).

Тип шифрования указывается в команде SESSION CREATE. Допускается использование нескольких типов шифрования. Клиенты должны устанавливать либо `i2cp.leaseSetEncType=4` (только для ECIES-X25519), либо `i2cp.leaseSetEncType=4,0` (для ECIES-X25519 и ElGamal, если требуется совместимость).

## Изменения в версии 3

### Изменения версии 3.0

Версия 3.0 была представлена в релизе I2P 0.7.3. SAMv2 предоставила способ управления несколькими сокетами на одном I2P destination *параллельно*, то есть клиенту не нужно было ждать успешной отправки данных через один сокет перед отправкой данных через другой сокет. Но все данные передавались через один и тот же сокет клиент-SAM, что было довольно сложно для управления со стороны клиента.

SAM v3 управляет сокетами по-другому: каждый *I2P socket* соответствует уникальному сокету клиент-SAM, что гораздо проще в обработке. Это похоже на [BOB](/docs/api/bob).

SAMv3 также предоставляет UDP-порт для отправки датаграмм через I2P и может перенаправлять I2P-датаграммы обратно на сервер датаграмм клиента.

### Изменения версии 3.1

Версия 3.1 была введена в Java I2P релизе 0.9.14 (июль 2014). SAM 3.1 является рекомендуемой минимальной реализацией SAM из-за поддержки лучших типов подписей по сравнению с SAM 3.0. i2pd также поддерживает большинство функций 3.1.

- DEST GENERATE и SESSION CREATE теперь поддерживают параметр SIGNATURE_TYPE.
- Параметры MIN и MAX в HELLO VERSION теперь являются необязательными.
- Параметры MIN и MAX в HELLO VERSION теперь поддерживают однозначные версии, такие как "3".
- RAW SEND теперь поддерживается на bridge socket.

### Изменения в версии 3.2

Версия 3.2 была представлена в релизе Java I2P 0.9.24 (январь 2016). Обратите внимание, что i2pd в настоящее время не поддерживает большинство функций 3.2.

#### Поддержка порта и протокола I2CP

- Опции SESSION CREATE FROM_PORT и TO_PORT
- Опция SESSION CREATE STYLE=RAW PROTOCOL
- Опции STREAM CONNECT, DATAGRAM SEND и RAW SEND FROM_PORT и TO_PORT
- Опция RAW SEND PROTOCOL
- DATAGRAM RECEIVED, RAW RECEIVED и перенаправленные или полученные потоки и отвечаемые датаграммы включают FROM_PORT и TO_PORT
- Опция RAW сессии HEADER=true приведет к тому, что перенаправленные raw датаграммы будут дополнены строкой, содержащей PROTOCOL=nnn FROM_PORT=nnnn TO_PORT=nnnn
- Первая строка датаграмм, отправленных через порт 7655, теперь может начинаться с любой версии 3.x
- Первая строка датаграмм, отправленных через порт 7655, может содержать любые из опций FROM_PORT, TO_PORT, PROTOCOL
- RAW RECEIVED включает PROTOCOL=nnn

#### SSL и аутентификация

- USER/PASSWORD в параметрах HELLO для авторизации. См. [ниже](#authorization).
- Опциональная настройка авторизации с командой AUTH. См. [ниже](#authorization-configuration-sam-32-or-higher-optional-feature).
- Опциональная поддержка SSL/TLS для управляющего сокета. См. [ниже](#ssl).
- Опция STREAM FORWARD SSL=true

#### Многопоточность

- Одновременные ожидающие STREAM ACCEPT разрешены для одного и того же идентификатора сессии.

#### Парсинг командной строки и поддержание соединения

- Дополнительные команды QUIT, STOP и EXIT для закрытия сессии и сокета. См. [ниже](#quitstopexitinvisible-sam-32-или-выше-дополнительные-функции).
- Парсинг команд корректно обрабатывает UTF-8
- Парсинг команд надежно обрабатывает пробелы внутри кавычек
- Обратная косая черта '\\' может экранировать кавычки в командной строке
- Рекомендуется, чтобы сервер преобразовывал команды в верхний регистр для удобства тестирования через telnet.
- Пустые значения параметров, такие как PROTOCOL или PROTOCOL=, могут быть допустимы, зависит от реализации.
- PING/PONG для поддержания соединения. См. ниже.
- Серверы могут реализовывать таймауты для команды HELLO или последующих команд, зависит от реализации.

### Изменения версии 3.3

Версия 3.3 была введена в релизе Java I2P 0.9.25 (март 2016). Обратите внимание, что i2pd в настоящее время не поддерживает большинство функций версии 3.3.

- Одна и та же сессия может использоваться для streams, datagrams и raw одновременно. Входящие пакеты и потоки будут маршрутизироваться на основе протокола I2P и порта назначения. См. [раздел PRIMARY ниже](#sam-primary-sessions-v33-and-higher).
- DATAGRAM SEND и RAW SEND теперь поддерживают опции SEND_TAGS, TAG_THRESHOLD, EXPIRES и SEND_LEASESET. См. [раздел отправки datagram ниже](#sending-repliable-or-raw-datagrams).

## Протокол версии 3

### Обзор спецификации Simple Anonymous Messaging (SAM) версии 3.3

Клиентское приложение взаимодействует с мостом SAM, который обрабатывает всю функциональность I2P (используя [библиотеку streaming](/docs/api/streaming) для виртуальных потоков или [I2CP](/docs/protocol/i2cp) напрямую для датаграмм).

По умолчанию связь между клиентом и SAM bridge не шифруется и не аутентифицируется. SAM bridge может поддерживать SSL/TLS соединения; детали конфигурации и реализации выходят за рамки данной спецификации. Начиная с SAM 3.2 поддерживаются опциональные параметры аутентификации пользователя/пароля в начальном handshake и могут быть обязательными для bridge.

Коммуникации I2P могут принимать несколько различных форм:

- [Виртуальные потоки](/docs/api/streaming)
- [Отвечаемые и аутентифицированные датаграммы](/docs/specs/datagrams#repliable) (сообщения с полем FROM)
- [Анонимные датаграммы](/docs/specs/datagrams#raw) (необработанные анонимные сообщения)
- [Datagram2](/docs/specs/datagrams#datagram2) (новый отвечаемый и аутентифицированный формат)
- [Datagram3](/docs/specs/datagrams#datagram3) (новый отвечаемый, но неаутентифицированный формат)

Связь I2P поддерживается сессиями I2P, и каждая сессия I2P привязана к адресу (называемому destination). Сессия I2P связана с одним из трех типов, указанных выше, и не может обеспечивать связь другого типа, если не используются [PRIMARY сессии](#sam-primary-sessions-v33-and-higher).

### Кодирование и экранирование

Все эти SAM сообщения отправляются в одной строке, завершаемой символом новой строки (\\n). До SAM 3.2 поддерживался только 7-битный ASCII. Начиная с SAM 3.2, кодировка должна быть UTF-8. Любые ключи или значения в кодировке UTF8 должны работать.

Форматирование, показанное в данной спецификации ниже, предназначено исключительно для удобства чтения, и хотя первые два слова в каждом сообщении должны оставаться в своем определенном порядке, порядок пар ключ=значение может изменяться (например, "ONE TWO A=B C=D" или "ONE TWO C=D A=B" являются совершенно корректными конструкциями). Кроме того, протокол чувствителен к регистру. В следующих примерах сообщения, отправляемые клиентом в SAM bridge, предваряются символом "->", а сообщения, отправляемые SAM bridge клиенту, предваряются символом "<-".

Базовая командная строка или строка ответа имеет одну из следующих форм:

```
COMMAND SUBCOMMAND [key=value] [key=value] ...
COMMAND                                           # As of SAM 3.2
PING[ arbitrary text]                             # As of SAM 3.2
PONG[ arbitrary text]                             # As of SAM 3.2
```
COMMAND без SUBCOMMAND поддерживается только для некоторых новых команд в SAM 3.2.

Пары ключ=значение должны разделяться одним пробелом. (Начиная с SAMv3.2, допускается несколько пробелов) Значения должны заключаться в двойные кавычки, если содержат пробелы, например key="long value text". (До SAMv3.2 это работало ненадежно в некоторых реализациях)

До SAMv3.2 не было механизма экранирования. Начиная с SAMv3.2, двойные кавычки могут быть экранированы обратной косой чертой '\\', а обратная косая черта может быть представлена как две обратные косые черты '\\\\'.

### Пустые значения

Начиная с SAM 3.2, пустые значения опций, такие как KEY, KEY= или KEY="", могут быть разрешены в зависимости от реализации.

### Чувствительность к регистру

Протокол, как указано в спецификации, чувствителен к регистру. Рекомендуется, но не обязательно, чтобы сервер преобразовывал команды в верхний регистр для удобства тестирования через telnet. Это позволило бы, например, работать команде "hello version". Это зависит от реализации. Не преобразовывайте ключи или значения в верхний регистр, поскольку это повредит опции [I2CP](/docs/protocol/i2cp).

### Рукопожатие соединения SAM

Никакая SAM-коммуникация не может происходить до тех пор, пока клиент и мост не договорятся о версии протокола, что выполняется отправкой клиентом HELLO и отправкой мостом HELLO REPLY:

```
->  HELLO VERSION
          [MIN=$min]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [MAX=$max]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [USER="xxx"]          # As of SAM 3.2, required if authentication is enabled, see below
          [PASSWORD="yyy"]      # As of SAM 3.2, required if authentication is enabled, see below
```
и

```
<-  HELLO REPLY RESULT=OK VERSION=3.1
```
Начиная с версии 3.1 (I2P 0.9.14), параметры MIN и MAX являются необязательными. SAM всегда вернет максимально возможную версию с учетом ограничений MIN и MAX, или текущую версию сервера, если ограничения не заданы.

Если SAM bridge не может найти подходящую версию, он отвечает:

```
<- HELLO REPLY RESULT=NOVERSION
```
Если произошла какая-либо ошибка, например неверный формат запроса, он отвечает:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
#### SSL

Управляющий сокет сервера может дополнительно предлагать поддержку SSL/TLS, как настроено на сервере и клиенте. Реализации также могут предлагать другие транспортные уровни; это выходит за рамки определения протокола.

#### Авторизация

Для авторизации клиент добавляет USER="xxx" PASSWORD="yyy" к параметрам HELLO. Двойные кавычки для имени пользователя и пароля рекомендуются, но не обязательны. Двойная кавычка внутри имени пользователя или пароля должна быть экранирована обратной косой чертой. В случае неудачи сервер ответит I2P_ERROR с сообщением. Рекомендуется включить SSL на любых SAM серверах, где требуется авторизация.

#### Таймауты

Серверы могут реализовывать таймауты для команды HELLO или последующих команд, в зависимости от реализации. Клиенты должны незамедлительно отправлять HELLO и следующую команду после подключения.

Если происходит таймаут до получения HELLO, мост отвечает:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
а затем отключается.

Если тайм-аут происходит после получения HELLO, но до следующей команды, мост отвечает:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
а затем отключается.

### Порты и протокол I2CP

Начиная с SAM 3.2, порты и протокол [I2CP](/docs/protocol/i2cp) могут быть указаны клиентом-отправителем SAM для передачи через [I2CP](/docs/protocol/i2cp), и мост SAM будет передавать полученную информацию о порте и протоколе [I2CP](/docs/protocol/i2cp) клиенту SAM.

Для FROM_PORT и TO_PORT допустимый диапазон составляет 0-65535, по умолчанию используется 0.

Для PROTOCOL, который может быть указан только для RAW, допустимый диапазон составляет 0-255, значение по умолчанию — 18.

For SESSION commands, the specified ports and protocol are the defaults for that session. For individual streams or datagrams, the specified ports and protocol override the session defaults. For received streams or datagrams, the indicated ports and protocol are as received from [I2CP](/docs/protocol/i2cp).

#### Важные отличия от стандартного IP

Порты I2CP предназначены для сокетов и датаграмм I2P. Они не связаны с вашими локальными сокетами, подключающимися к SAM.

- Порт 0 является допустимым и имеет особое значение.
- Порты 1-1023 не являются особыми или привилегированными.
- Серверы по умолчанию слушают на порту 0, что означает "все порты".
- Клиенты по умолчанию отправляют на порт 0, что означает "любой порт".
- Клиенты по умолчанию отправляют с порта 0, что означает "не указан".
- Серверы могут иметь службу, слушающую на порту 0, и другие службы, слушающие на более высоких портах. В таком случае служба на порту 0 является службой по умолчанию и будет подключена, если входящий сокет или порт датаграммы не соответствует другой службе.
- Большинство I2P-пунктов назначения имеют только одну запущенную службу, поэтому вы можете использовать значения по умолчанию и игнорировать конфигурацию портов I2CP.
- SAM 3.2 или 3.3 требуется для указания портов I2CP.
- Если вам не нужны порты I2CP, вам не нужен SAM 3.2 или 3.3; достаточно 3.1.
- Протокол 0 является допустимым и означает "любой протокол". Это не рекомендуется и, вероятно, не будет работать.
- I2P-сокеты отслеживаются по внутреннему ID соединения. Поэтому нет требования, чтобы 5-кортеж dest:port:dest:port:protocol был уникальным. Например, может быть несколько сокетов с одинаковыми портами между двумя пунктами назначения. Клиентам не нужно выбирать "свободный порт" для исходящего соединения.

Если вы разрабатываете SAM 3.3 приложение с несколькими подсессиями, тщательно продумайте, как эффективно использовать порты и протоколы. См. спецификацию [I2CP](/docs/protocol/i2cp) для получения дополнительной информации.

### SAM-сессии

SAM сессия создается, когда клиент открывает сокет к SAM мосту, выполняет рукопожатие и отправляет сообщение SESSION CREATE, а сессия завершается при отключении сокета.

Каждый зарегистрированный I2P Destination уникально связан с идентификатором сессии (или псевдонимом). Идентификаторы сессий, включая идентификаторы подсессий для PRIMARY сессий, должны быть глобально уникальными на SAM сервере. Чтобы предотвратить возможные коллизии идентификаторов с другими клиентами, рекомендуется генерировать идентификаторы случайным образом.

Каждая сессия уникально связана с:

- сокет, из которого клиент создает сессию
- его ID (или псевдоним)

#### Запрос на создание сессии

Сообщение создания сессии может использовать только одну из этих форм (сообщения, полученные в других формах, получают в ответ сообщение об ошибке):

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
DESTINATION указывает, какой destination должен использоваться для отправки и получения сообщений/потоков. $privkey — это base 64 от конкатенации [Destination](/docs/specs/common-structures#type_Destination), за которым следует [Private Key](/docs/specs/common-structures#type_PrivateKey), затем [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), и опционально [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), что составляет 663 или более байт в двоичном формате и 884 или более байт в base 64, в зависимости от типа подписи. Двоичный формат указан в Private Key File. Смотрите дополнительные примечания о [Private Key](/docs/specs/common-structures#type_PrivateKey) в разделе Destination Key Generation ниже.

Если приватный ключ подписи состоит из одних нулей, следует секция [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature). Offline signatures поддерживаются только для сессий STREAM и RAW. Offline signatures не могут быть созданы с DESTINATION=TRANSIENT. Формат секции offline signature следующий:

1. Временная метка истечения (4 байта, big endian, секунды с начала эпохи, переполняется в 2106 году)
2. Тип подписи временного Signing Public Key (2 байта, big endian)
3. Временный Signing Public key (длина как указано типом временной подписи)
4. Подпись вышеуказанных трех полей офлайн-ключом (длина как указано типом подписи назначения)
5. Временный Signing Private key (длина как указано типом временной подписи)

Если destination указан как TRANSIENT, SAM мост создает новый destination. Начиная с версии 3.1 (I2P 0.9.14), если destination равен TRANSIENT, поддерживается дополнительный параметр SIGNATURE_TYPE. Значение SIGNATURE_TYPE может быть любым именем (например, ECDSA_SHA256_P256, регистр не важен) или номером (например, 1), поддерживаемым [Key Certificates](/docs/specs/common-structures#type_Certificate). По умолчанию используется DSA_SHA1, что НЕ то, что вам нужно. Для большинства приложений, пожалуйста, укажите SIGNATURE_TYPE=7.

$nickname выбирается клиентом. Пробелы не допускаются.

Дополнительные переданные параметры передаются в конфигурацию I2P сессии, если они не интерпретируются SAM мостом (например, outbound.length=0).

Java I2P и i2pd router имеют разные значения по умолчанию для количества tunnel. Значение по умолчанию для Java составляет 2, а для i2pd — 5. Для большинства случаев с низкой и средней пропускной способностью и низким и средним количеством соединений достаточно 2 или 3. Пожалуйста, укажите количество tunnel в сообщении SESSION CREATE, чтобы получить согласованную производительность с Java I2P и i2pd router, используя опции, например, inbound.quantity=3 outbound.quantity=3. Эти и другие опции [документированы по ссылкам ниже](#tunnel-i2cp-and-streaming-options).

SAM bridge сам по себе должен уже быть настроен с указанием того, какой router он должен использовать для связи через I2P (хотя при необходимости может быть способ переопределить это, например, i2cp.tcp.host=localhost и i2cp.tcp.port=7654).

#### Ответ на создание сессии

После получения сообщения создания сессии, SAM мост ответит сообщением о статусе сессии следующим образом:

Если создание прошло успешно:

```
<-  SESSION STATUS RESULT=OK DESTINATION=$privkey
```
$privkey представляет собой base 64 от конкатенации [Destination](/docs/specs/common-structures#type_Destination), за которым следует [Private Key](/docs/specs/common-structures#type_PrivateKey), затем [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), и опционально [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), что составляет 663 или более байт в бинарном формате и 884 или более байт в base 64, в зависимости от типа подписи. Бинарный формат определен в Private Key File.

Если SESSION CREATE содержал закрытый ключ подписи из всех нулей и секцию [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), ответ SESSION STATUS будет включать те же данные в том же формате. Подробности см. в разделе SESSION CREATE выше.

Если псевдоним уже связан с сессией:

```
<-  SESSION STATUS RESULT=DUPLICATED_ID
```
Если назначение уже используется:

```
<-  SESSION STATUS RESULT=DUPLICATED_DEST
```
Если назначение не является действительным ключом приватного назначения:

```
<-  SESSION STATUS RESULT=INVALID_KEY
```
Если произошла какая-либо другая ошибка:

```
<-  SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
Если это не OK, MESSAGE должно содержать понятную для человека информацию о том, почему сессия не может быть создана.

Обратите внимание, что router строит tunnel перед ответом SESSION STATUS. Это может занять несколько секунд или, при запуске router или во время серьезных сетевых перегрузок, минуту или более. В случае неудачи router не будет отвечать сообщением об ошибке в течение нескольких минут. Не устанавливайте короткий таймаут ожидания ответа. Не прерывайте сессию во время построения tunnel и не пытайтесь повторить попытку.

SAM сессии существуют и завершаются вместе с сокетом, с которым они связаны. Когда сокет закрывается, сессия завершается, и все коммуникации, использующие эту сессию, прекращаются одновременно. И наоборот, когда сессия завершается по любой причине, SAM мост закрывает сокет.

### Виртуальные потоки SAM

Виртуальные потоки гарантированно отправляются надежно и в правильном порядке, с уведомлениями об ошибках и успехе, как только они становятся доступными.

Streams — это двунаправленные коммуникационные сокеты между двумя I2P destinations, но их открытие должно быть запрошено одним из них. Далее команды CONNECT используются SAM-клиентом для такого запроса. Команды FORWARD / ACCEPT используются SAM-клиентом, когда он хочет прослушивать запросы, поступающие от других I2P destinations.

### SAM Virtual Streams: CONNECT

Клиент запрашивает соединение следующим образом:

- открытие нового сокета с мостом SAM
- передача того же рукопожатия HELLO, как указано выше
- отправка команды STREAM CONNECT

#### Запрос на подключение

```
-> STREAM CONNECT
         ID=$nickname
         DESTINATION=$destination
         [SILENT={true,false}]                # default false
         [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
         [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
```
Это устанавливает новое виртуальное соединение от локальной сессии с идентификатором $nickname к указанному узлу.

Цель — это $destination, которая представляет собой base 64 от [Destination](/docs/specs/common-structures#type_Destination), что составляет 516 или более символов base 64 (387 или более байт в двоичном формате), в зависимости от типа подписи.

**ПРИМЕЧАНИЕ:** Начиная примерно с 2014 года (SAM v3.1), Java I2P также поддерживает имена хостов и b32-адреса для $destination, но ранее это не было документировано. Имена хостов и b32-адреса теперь официально поддерживаются Java I2P начиная с релиза 0.9.48. Router i2pd поддерживает имена хостов и b32-адреса начиная с релиза 2.38.0 (0.9.50). Для обоих router'ов поддержка "b32" включает поддержку расширенных "b33"-адресов для скрытых назначений.

#### Ответ на подключение

Если передается SILENT=true, SAM bridge не будет отправлять никаких других сообщений в сокет. Если соединение не удается, сокет будет закрыт. Если соединение устанавливается успешно, все остальные данные, проходящие через текущий сокет, пересылаются от и к подключенному узлу назначения I2P.

Если SILENT=false, что является значением по умолчанию, SAM bridge отправляет последнее сообщение своему клиенту перед перенаправлением или закрытием сокета:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
Значение RESULT может быть одним из:

```
OK
CANT_REACH_PEER
I2P_ERROR
INVALID_KEY
INVALID_ID
TIMEOUT
```
Если RESULT равен OK, все остальные данные, проходящие через текущий сокет, пересылаются от и к подключенному I2P destination peer. Если подключение было невозможно (таймаут и т.д.), RESULT будет содержать соответствующее значение ошибки (сопровождаемое необязательным человеко-читаемым MESSAGE), и SAM bridge закрывает сокет.

Внутренний таймаут подключения потока router составляет приблизительно одну минуту и зависит от реализации. Не устанавливайте более короткий таймаут для ожидания ответа.

### SAM Virtual Streams: ACCEPT

Клиент ожидает входящий запрос подключения с помощью:

- открытие нового сокета с мостом SAM
- передача того же рукопожатия HELLO, как указано выше
- отправка команды STREAM ACCEPT

#### Принять запрос

```
-> STREAM ACCEPT
         ID=$nickname
         [SILENT={true,false}]                # default false
```
Это заставляет сессию ${nickname} ожидать один входящий запрос на подключение из сети I2P. ACCEPT не разрешен, пока в сессии активен FORWARD.

Начиная с SAM 3.2, разрешены множественные одновременные ожидающие STREAM ACCEPT на одном и том же ID сессии (даже с одинаковым портом). До версии 3.2 одновременные accept завершались с ошибкой ALREADY_ACCEPTING. Примечание: Java I2P также поддерживает одновременные ACCEPT в SAM 3.1, начиная с релиза 0.9.24 (2016-01). i2pd также поддерживает одновременные ACCEPT в SAM 3.1, начиная с релиза 2.50.0 (2023-12).

#### Ответ принятия

Если передается SILENT=true, мост SAM не будет выдавать никаких других сообщений на сокет. Если принятие соединения не удается, сокет будет закрыт. Если принятие соединения успешно, все оставшиеся данные, проходящие через текущий сокет, пересылаются от и к подключенному узлу назначения I2P. Для надежности и получения назначения для входящих соединений рекомендуется SILENT=false.

Если SILENT=false, что является значением по умолчанию, SAM мост отвечает:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
Значение RESULT может быть одним из:

```
OK
I2P_ERROR
INVALID_ID
```
Если результат не OK, сокет немедленно закрывается SAM-мостом. Если результат OK, SAM-мост начинает ожидать входящего запроса на соединение от другого I2P-узла. Когда запрос поступает, SAM-мост принимает его и:

Если был передан параметр SILENT=true, SAM мост не будет отправлять никаких других сообщений в клиентский сокет. Все остальные данные, проходящие через текущий сокет, пересылаются от и к подключенному узлу назначения I2P.

Если был передан SILENT=false, что является значением по умолчанию, SAM bridge отправляет клиенту ASCII строку, содержащую base64 публичный ключ destination запрашивающего узла, и дополнительную информацию только для SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
После этой строки, завершающейся '\\n', все остальные данные, проходящие через текущий сокет, пересылаются от и к подключенному I2P destination узлу, до тех пор пока один из узлов не закроет сокет.

#### Ошибки после OK

В редких случаях мост SAM может столкнуться с ошибкой после отправки RESULT=OK, но до поступления соединения и отправки строки $destination клиенту. Эти ошибки могут включать выключение роутера, перезапуск роутера и закрытие сессии. В таких случаях, когда SILENT=false, мост SAM может, но не обязан (зависит от реализации), отправить строку:

```
<-  STREAM STATUS
         RESULT=I2P_ERROR
         [MESSAGE=...]
```
перед немедленным закрытием сокета. Эта строка, конечно же, не может быть декодирована как валидный Base 64 destination.

### SAM Virtual Streams: FORWARD

Клиент может использовать обычный socket-сервер и ожидать запросы на соединение, поступающие из I2P. Для этого клиент должен:

- открыть новый сокет с мостом SAM
- выполнить то же рукопожатие HELLO, что и выше
- отправить команду forward

#### Запрос пересылки

```
-> STREAM FORWARD
         ID=$nickname
         PORT=$port
         [HOST=$host]
         [SILENT={true,false}]                # default false
         [SSL={true,false}]                   # SAM 3.2 or higher only, default false
```
Это заставляет сессию ${nickname} прослушивать входящие запросы на подключение из сети I2P. FORWARD не разрешен, пока в сессии есть ожидающий ACCEPT.

#### Ответ на пересылку

SILENT по умолчанию имеет значение false. Независимо от того, имеет ли SILENT значение true или false, SAM bridge всегда отвечает сообщением STREAM STATUS. Обратите внимание, что это отличается от поведения STREAM ACCEPT и STREAM CONNECT при SILENT=true. Сообщение STREAM STATUS имеет вид:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
Значение RESULT может быть одним из следующих:

```
OK
I2P_ERROR
INVALID_ID
```
$host — это имя хоста или IP-адрес серверного сокета, на который SAM будет перенаправлять запросы на подключение. Если не указан, SAM использует IP-адрес сокета, который выдал команду forward.

$port — это номер порта сокетного сервера, на который SAM будет перенаправлять запросы на подключение. Этот параметр обязателен.

Когда запрос на соединение поступает из I2P, мост SAM открывает socket-соединение к $host:$port. Если оно принимается менее чем за 3 секунды, SAM примет соединение из I2P, и затем:

Если был передан параметр SILENT=true, все данные, проходящие через полученный текущий сокет, пересылаются от и к подключенному узлу I2P destination.

Если был передан SILENT=false, что является значением по умолчанию, мост SAM отправляет в полученный сокет ASCII-строку, содержащую base64 публичный ключ назначения запрашивающего узла, а также дополнительную информацию только для SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
После этой строки, завершающейся '\\n', все оставшиеся данные, проходящие через сокет, пересылаются от и к подключенному I2P destination узлу, пока одна из сторон не закроет сокет.

Начиная с SAMv3.2, если указан параметр SSL=true, пересылающий сокет работает через SSL/TLS.

I2P router прекратит прослушивание входящих запросов на соединение, как только будет закрыт "forwarding" сокет.

### SAM датаграммы

SAMv3 предоставляет механизмы для отправки и получения датаграмм через локальные datagram сокеты. Некоторые реализации SAMv3 также поддерживают старый способ v1/v2 отправки/получения датаграмм через SAM bridge сокет. Оба способа документированы ниже.

I2P поддерживает четыре типа датаграмм:

- Датаграммы с возможностью ответа и аутентификацией имеют префикс с назначением отправителя и содержат подпись отправителя, поэтому получатель может убедиться, что назначение отправителя не было подделано, и может ответить на датаграмму. Новый формат Datagram2 также поддерживает ответы и аутентификацию.
- Новый формат Datagram3 поддерживает ответы, но не аутентификацию. Информация об отправителе не проверяется.
- Необработанные датаграммы не содержат назначения отправителя или подписи.

Порты I2CP по умолчанию определены как для отвечаемых, так и для необработанных датаграмм. Порт I2CP может быть изменен для необработанных датаграмм.

Распространенный шаблон проектирования протоколов заключается в отправке датаграмм с возможностью ответа на серверы с включенным идентификатором, и сервер отвечает обычной датаграммой, содержащей этот идентификатор, чтобы ответ можно было сопоставить с запросом. Этот шаблон проектирования устраняет значительные накладные расходы датаграмм с возможностью ответа в ответных сообщениях. Все выборы I2CP протоколов и портов являются специфичными для приложения, и разработчики должны учитывать эти вопросы.

См. также важные примечания о MTU датаграмм в разделе ниже.

#### Отправка датаграмм с возможностью ответа или необработанных датаграмм

Хотя I2P по своей природе не содержит адрес FROM, для удобства использования предоставляется дополнительный уровень в виде repliable datagrams - неупорядоченных и ненадежных сообщений размером до 31744 байт, которые включают адрес FROM (оставляя до 1КБ для заголовочного материала). Этот адрес FROM аутентифицируется внутренне SAM (используя ключ подписи назначения для проверки источника) и включает защиту от повторных атак.

Минимальный размер составляет 1. Для наилучшей надежности доставки рекомендуемый максимальный размер составляет приблизительно 11 КБ. Надежность обратно пропорциональна размеру сообщения, возможно, даже экспоненциально.

После установления SAM сессии с STYLE=DATAGRAM или STYLE=RAW, клиент может отправлять отвечаемые или сырые датаграммы через UDP порт SAM (7655 по умолчанию).

Первая строка датаграммы, отправленной через этот порт, должна иметь следующий формат. Всё это находится на одной строке (разделено пробелами), показано на нескольких строках для наглядности:

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
- 3.0 — это версия SAM. Начиная с SAM 3.2, разрешена любая версия 3.x.
- $nickname — это идентификатор DATAGRAM-сессии, которая будет использоваться
- Целью является $destination, которая представляет собой base 64 от [Destination](/docs/specs/common-structures#type_Destination), что составляет 516 или более символов base 64 (387 или более байт в двоичном виде), в зависимости от типа подписи. **ПРИМЕЧАНИЕ:** Примерно с 2014 года (SAM v3.1) Java I2P также поддерживает имена хостов и b32-адреса для $destination, но ранее это не было задокументировано. Имена хостов и b32-адреса теперь официально поддерживаются Java I2P начиная с релиза 0.9.48. router i2pd в настоящее время не поддерживает имена хостов и b32-адреса; поддержка может быть добавлена в будущем релизе.
- Все опции являются настройками для отдельных датаграмм, которые переопределяют значения по умолчанию, указанные в SESSION CREATE.
- Опции версии 3.3 SEND_TAGS, TAG_THRESHOLD, EXPIRES и SEND_LEASESET будут переданы в [I2CP](/docs/protocol/i2cp), если поддерживаются. Подробности см. в [спецификации I2CP](/docs/protocol/i2cp#msg_SendMessageExpire). Поддержка SAM-сервером необязательна, он будет игнорировать эти опции, если они не поддерживаются.
- эта строка завершается символом '\\n'.

Первая строка будет отброшена SAM перед отправкой оставшихся данных сообщения на указанное назначение.

Для альтернативного способа отправки датаграмм с возможностью ответа и необработанных датаграмм, см. [DATAGRAM SEND и RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### SAM Repliable Datagrams: Получение датаграммы

Полученные датаграммы записываются SAM в сокет, из которого была открыта сессия датаграмм, если переадресующий PORT не указан в команде SESSION CREATE. Это способ получения датаграмм, совместимый с v1/v2.

Когда прибывает датаграмма, мост доставляет её клиенту через сообщение:

```
<-  DATAGRAM RECEIVED
           DESTINATION=$destination           # See notes below for Datagram3 format
           SIZE=$numBytes
           FROM_PORT=nnn                      # SAM 3.2 or higher only
           TO_PORT=nnn                        # SAM 3.2 or higher only
           \n
       [$numBytes of data]
```
Источником является $destination, который представляет собой base 64 от [Destination](/docs/specs/common-structures#type_Destination), что составляет 516 или более символов base 64 (387 или более байт в двоичном формате), в зависимости от типа подписи.

Мост SAM никогда не предоставляет клиенту заголовки аутентификации или другие поля, а только данные, которые предоставил отправитель. Это продолжается до тех пор, пока сессия не будет закрыта (когда клиент разрывает соединение).

#### Пересылка сырых или отвечаемых датаграмм

При создании datagram сессии клиент может попросить SAM перенаправлять входящие сообщения на указанный ip:port. Это делается путем выполнения команды CREATE с опциями PORT и HOST:

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
$privkey представляет собой base 64 кодировку конкатенации [Destination](/docs/specs/common-structures#type_Destination), за которой следует [Private Key](/docs/specs/common-structures#type_PrivateKey), затем [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), и опционально [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), что составляет 884 или более символов base 64 (663 или более байт в двоичном формате), в зависимости от типа подписи. Двоичный формат описан в Private Key File.

Автономные подписи поддерживаются для датаграмм RAW, DATAGRAM2 и DATAGRAM3, но не для DATAGRAM. Подробности см. в разделе SESSION CREATE выше и в разделе DATAGRAM2/3 ниже.

$host — это имя хоста или IP-адрес сервера датаграмм, на который SAM будет перенаправлять датаграммы. Если не указано, SAM использует IP-адрес сокета, который отправил команду forward.

$port — это номер порта сервера датаграмм, на который SAM будет пересылать датаграммы. Если $port не задан, датаграммы НЕ будут пересылаться, они будут получены на управляющем сокете в режиме совместимости с v1/v2.

Дополнительные переданные опции передаются в конфигурацию I2P сессии, если они не интерпретируются мостом SAM (например, outbound.length=0). Эти опции [документированы ниже](#tunnel-i2cp-and-streaming-options).

Перенаправляемые датаграммы с возможностью ответа всегда имеют префикс с destination в формате base64, за исключением Datagram3, см. ниже. Когда приходит датаграмма с возможностью ответа, мост отправляет на указанный host:port UDP-пакет, содержащий следующие данные:

```
$destination                       # See notes below for Datagram3 format
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
$datagram_payload
```
Пересылаемые raw датаграммы пересылаются как есть на указанный host:port без префикса. UDP пакет содержит следующие данные:

```
$datagram_payload
```
Начиная с SAM 3.2, когда HEADER=true указан в SESSION CREATE, пересылаемая raw datagram будет дополнена заголовочной строкой следующим образом:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
$destination — это base 64 представление [Destination](/docs/specs/common-structures#type_Destination), которое составляет 516 или более символов base 64 (387 или более байт в двоичном формате), в зависимости от типа подписи.

#### SAM Анонимные (Raw) Датаграммы

Максимально эффективно используя пропускную способность I2P, SAM позволяет клиентам отправлять и получать анонимные датаграммы, оставляя аутентификацию и информацию об ответах на усмотрение самих клиентов. Эти датаграммы являются ненадежными и неупорядоченными, и могут достигать 32768 байт.

Минимальный размер — 1. Для наилучшей надежности доставки рекомендуемый максимальный размер составляет примерно 11 КБ.

После установления SAM-сессии с STYLE=RAW клиент может отправлять анонимные датаграммы через SAM-мост точно таким же способом, как [отправка датаграмм с возможностью ответа](#sending-repliable-or-raw-datagrams).

Оба способа получения датаграмм также доступны для анонимных датаграмм.

Полученные датаграммы записываются SAM в сокет, из которого была открыта сессия датаграмм, если в команде SESSION CREATE не указан PORT для перенаправления. Это способ получения датаграмм, совместимый с v1/v2.

```
<- RAW RECEIVED
          SIZE=$numBytes
          FROM_PORT=nnn                      # SAM 3.2 or higher only
          TO_PORT=nnn                        # SAM 3.2 or higher only
          PROTOCOL=nnn                       # SAM 3.2 or higher only
          \n
      [$numBytes of data]
```
Когда анонимные датаграммы должны быть переданы на определенный host:port, мост отправляет на указанный host:port сообщение, содержащее следующие данные:

```
$datagram_payload
```
Начиная с SAM 3.2, когда в SESSION CREATE указан параметр HEADER=true, переданная raw датаграмма будет предварена строкой заголовка следующим образом:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
Альтернативный способ отправки анонимных датаграмм см. в разделе [RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### Датаграмма 2/3

Datagram 2/3 - это новые форматы, указанные в начале 2025 года. В настоящее время не существует известных реализаций. Проверьте документацию реализации для получения текущего статуса. Смотрите [спецификацию](/docs/specs/datagrams) для получения дополнительной информации.

В настоящее время нет планов по увеличению версии SAM для указания поддержки Datagram 2/3. Это может быть проблематично, поскольку реализации могут захотеть поддерживать Datagram 2/3, но не функции SAM v3.3. Любое изменение версии пока не определено.

И Datagram2, и Datagram3 поддерживают ответы. Только Datagram2 является аутентифицированным.

Datagram2 идентичен repliable датаграммам с точки зрения SAM. Оба аутентифицированы. Отличаются только формат I2CP и подпись, но это не видно клиентам SAM. Datagram2 также поддерживает офлайн-подписи, поэтому может использоваться назначениями с офлайн-подписями.

Предполагается, что Datagram2 заменит Repliable datagram для новых приложений, которым не требуется обратная совместимость. Datagram2 обеспечивает защиту от повторных атак, которая отсутствует в Repliable datagram. Если требуется обратная совместимость, приложение может поддерживать как Datagram2, так и Repliable в рамках одной сессии с PRIMARY сессиями SAM 3.3.

Datagram3 поддерживает ответы, но не аутентифицирован. Поле 'from' в формате I2CP является хешем, а не destination. $destination, отправляемый от SAM сервера к клиенту, будет представлять собой 44-байтовый base64 хеш. Для преобразования его в полный destination для ответа нужно декодировать его из base64 в 32 байта бинарных данных, затем закодировать в base32 в 52 символа и добавить ".b32.i2p" для NAMING LOOKUP. Как обычно, клиенты должны поддерживать свой собственный кеш, чтобы избежать повторных NAMING LOOKUP.

Разработчики приложений должны проявлять крайнюю осторожность и учитывать последствия для безопасности при использовании неаутентифицированных датаграмм.

#### Соображения по MTU датаграмм V3

I2P датаграммы могут быть больше типичного интернет MTU в 1500 байт. Локально отправленные датаграммы и пересылаемые датаграммы с возможностью ответа, которым предшествует base64 назначение размером 516+ байт, вероятно, превысят этот MTU. Однако MTU localhost в системах Linux обычно намного больше, например 65536. MTU localhost будет различаться в зависимости от ОС. I2P датаграммы никогда не будут больше 65536 байт. Размер датаграммы зависит от протокола приложения.

Если SAM-клиент находится локально относительно SAM-сервера и система поддерживает больший MTU, то дейтаграммы не будут фрагментироваться локально. Однако, если SAM-клиент удаленный, то IPv4 дейтаграммы будут фрагментироваться, а IPv6 дейтаграммы не пройдут (IPv6 не поддерживает фрагментацию UDP).

Разработчики клиентских библиотек и приложений должны знать об этих проблемах и документировать рекомендации для предотвращения фрагментации и потери пакетов, особенно при удаленных соединениях SAM клиент-сервер.

#### DATAGRAM SEND, RAW SEND (Обработка датаграмм, совместимая с V1/V2)

В SAMv3 предпочтительным способом отправки датаграмм является использование сокета датаграмм на порту 7655, как описано выше. Однако датаграммы с возможностью ответа могут быть отправлены непосредственно через сокет моста SAM с использованием команды DATAGRAM SEND, как описано в [SAM V1](/docs/api/sam) и [SAM V2](/docs/api/samv2).

Начиная с релиза 0.9.14 (версия 3.1), анонимные датаграммы могут отправляться напрямую через сокет моста SAM с использованием команды RAW SEND, как описано в документации [SAM V1](/docs/api/sam) и [SAM V2](/docs/api/samv2).

Начиная с релиза 0.9.24 (версия 3.2), DATAGRAM SEND и RAW SEND могут включать параметры FROM_PORT=nnnn и/или TO_PORT=nnnn для переопределения портов по умолчанию. Начиная с релиза 0.9.24 (версия 3.2), RAW SEND может включать параметр PROTOCOL=nnn для переопределения протокола по умолчанию.

Эти команды *не* поддерживают параметр ID. Датаграммы отправляются в последнюю созданную сессию типа DATAGRAM или RAW, в зависимости от ситуации. Поддержка параметра ID может быть добавлена в будущих версиях.

Форматы DATAGRAM2 и DATAGRAM3 *не* поддерживаются в режиме совместимости с V1/V2.

### Первичные сессии SAM (V3.3 и выше)

*Версия 3.3 была введена в I2P релизе 0.9.25.*

*В более ранней версии данной спецификации сессии PRIMARY назывались сессиями MASTER. В `i2pd` и `I2P+` они по-прежнему известны только как сессии MASTER.*

SAM v3.3 добавляет поддержку для запуска потоковых, datagram и raw подсессий в рамках одной основной сессии, а также для запуска нескольких подсессий одного типа. Весь трафик подсессий использует одно назначение или набор туннелей. Маршрутизация трафика из I2P основана на параметрах порта и протокола для подсессий.

Чтобы создать мультиплексированные подсессии, вы должны создать основную сессию, а затем добавить подсессии к основной сессии. Каждая подсессия должна иметь уникальный идентификатор и уникальный протокол прослушивания и порт. Подсессии также могут быть удалены из основной сессии.

С помощью PRIMARY сессии и комбинации подсессий, SAM клиент может поддерживать несколько приложений, или одно сложное приложение, использующее различные протоколы, на едином наборе tunnel. Например, bittorrent клиент может настроить streaming подсессию для peer-to-peer соединений, вместе с datagram и raw подсессиями для DHT коммуникации.

#### Создание PRIMARY сессии

```
->  SESSION CREATE
          STYLE=PRIMARY                        # prior to 0.9.47, use STYLE=MASTER
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP and streaming options
```
Мост SAM ответит сообщением об успехе или неудаче, как в [ответе на стандартный SESSION CREATE](#session-creation-response).

Не устанавливайте опции PORT, HOST, FROM_PORT, TO_PORT, PROTOCOL, LISTEN_PORT, LISTEN_PROTOCOL или HEADER в первичной сессии. Вы не можете отправлять данные по ID первичной сессии или через управляющий сокет. Все команды, такие как STREAM CONNECT, DATAGRAM SEND и т.д., должны использовать ID подсессии через отдельный сокет.

PRIMARY сессия подключается к router и строит tunnel. Когда SAM мост отвечает, tunnel построены и сессия готова для добавления подсессий. Все опции [I2CP](/docs/protocol/i2cp), относящиеся к параметрам tunnel, таким как длина, количество и псевдоним, должны быть предоставлены в SESSION CREATE основной сессии.

Все служебные команды поддерживаются в основной сессии.

Когда основная сессия закрывается, все подсессии также закрываются.

ПРИМЕЧАНИЕ: До версии 0.9.47 используйте STYLE=MASTER. STYLE=PRIMARY поддерживается начиная с версии 0.9.47. MASTER по-прежнему поддерживается для обратной совместимости.

#### Создание подсессии

Используя тот же управляющий сокет, на котором была создана PRIMARY сессия:

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
SAM bridge ответит успехом или неудачей, как в [ответе на стандартный SESSION CREATE](#session-creation-response). Поскольку туннели уже были построены в основном SESSION CREATE, SAM bridge должен ответить немедленно.

Не устанавливайте опцию DESTINATION при SESSION ADD. Подсессия будет использовать destination, указанный в основной сессии. Все подсессии должны быть добавлены через управляющий сокет, то есть через то же соединение, на котором вы создали основную сессию.

Несколько подсессий должны иметь достаточно уникальные опции, чтобы входящие данные могли быть правильно маршrutизированы. В частности, несколько сессий одного и того же стиля должны иметь разные опции LISTEN_PORT (и/или LISTEN_PROTOCOL, только для RAW). SESSION ADD с портом прослушивания и протоколом, которые дублируют существующую подсессию, приведет к ошибке.

LISTEN_PORT — это локальный I2P порт, то есть порт получения (TO) для входящих данных. Если LISTEN_PORT не указан, будет использовано значение FROM_PORT. Если LISTEN_PORT и FROM_PORT не указаны, входящая маршрутизация будет основана только на STYLE и PROTOCOL. Для LISTEN_PORT и LISTEN_PROTOCOL значение 0 означает любое значение, то есть подстановочный знак. Если и LISTEN_PORT, и LISTEN_PROTOCOL равны 0, эта подсессия будет использоваться по умолчанию для входящего трафика, который не маршрутизируется в другую подсессию. Входящий потоковый трафик (протокол 6) никогда не будет маршрутизироваться в RAW подсессию, даже если её LISTEN_PROTOCOL равен 0. RAW подсессия не может устанавливать LISTEN_PROTOCOL равным 6. Если нет подсессии по умолчанию или подсессии, соответствующей протоколу и порту входящего трафика, эти данные будут отброшены.

Используйте ID подсессии, а не ID основной сессии, для отправки и получения данных. Все команды, такие как STREAM CONNECT, DATAGRAM SEND и т.д., должны использовать ID подсессии.

Все служебные команды поддерживаются в основной сессии или подсессии. Отправка/получение v1/v2 датаграмм/raw данных не поддерживается в основной сессии или в подсессиях.

#### Остановка подсессии

Используя тот же управляющий сокет, на котором была создана PRIMARY сессия:

```
->  SESSION REMOVE
          ID=$nickname
```
Это удаляет подсессию из основной сессии. Не устанавливайте никаких других опций для SESSION REMOVE. Подсессии должны удаляться через управляющий сокет, то есть через то же соединение, на котором вы создали основную сессию. После удаления подсессия закрывается и больше не может использоваться для отправки или получения данных.

SAM bridge ответит успехом или неудачей, как в [ответе на стандартную SESSION CREATE](#session-creation-response).

### Служебные команды SAM

Некоторые служебные команды требуют существующую сессию, а некоторые нет. См. подробности ниже.

#### Поиск имени хоста

Следующее сообщение может использоваться клиентом для запроса разрешения имён к мосту SAM:

```
NAMING LOOKUP
       NAME=$name
       [OPTIONS=true]     # Default false, as of router API 0.9.66
```
на что отвечает

```
NAMING REPLY
       RESULT=$result
       NAME=$name
       [VALUE=$destination]
       [MESSAGE="$message"]
       [OPTION:optionkey="$optionvalue"]   # As of router API 0.9.66
```
Значение RESULT может быть одним из:

```
OK
INVALID_KEY
KEY_NOT_FOUND
```
Если NAME=ME, то ответ будет содержать назначение, используемое текущей сессией (полезно, если вы используете TRANSIENT). Если $result не OK, MESSAGE может содержать описательное сообщение, например "bad format" и т.д. INVALID_KEY означает, что что-то не так с $name в запросе, возможно недопустимые символы.

$destination — это base 64 представление [Destination](/docs/specs/common-structures#type_Destination), которое содержит 516 или более символов base 64 (387 или более байт в двоичном формате), в зависимости от типа подписи.

NAMING LOOKUP не требует предварительного создания сессии. Однако в некоторых реализациях поиск .b32.i2p, который не кэширован и требует сетевого запроса, может завершиться неудачей, поскольку для поиска недоступны клиентские tunnel.

#### Опции поиска имён

NAMING LOOKUP расширен начиная с router API 0.9.66 для поддержки поиска сервисов. Поддержка может различаться в зависимости от реализации. Дополнительную информацию см. в предложении 167.

NAMING LOOKUP NAME=example.i2p OPTIONS=true запрашивает сопоставление параметров в ответе. NAME может быть полным base64 назначением, когда OPTIONS=true.

Если поиск назначения был успешным и в leaseset присутствовали опции, то в ответе, следующем за назначением, будет одна или более опций в форме OPTION:key=value. Каждая опция будет иметь отдельный префикс OPTION:. Будут включены все опции из leaseset, не только опции записей сервиса. Например, могут присутствовать опции для параметров, определённых в будущем. Пример:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Ключи, содержащие '=', и ключи или значения, содержащие символ новой строки, считаются недействительными, и пара ключ/значение будет удалена из ответа. Если в leaseset не найдено параметров, или если leaseset был версии 1, то ответ не будет включать никаких параметров. Если в запросе было указано OPTIONS=true, а leaseset не найден, будет возвращено новое значение результата LEASESET_NOT_FOUND.

#### Генерация ключей назначения

Публичные и приватные ключи в формате base64 могут быть сгенерированы с помощью следующего сообщения:

```
->  DEST GENERATE
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, default DSA_SHA1
```
на что отвечает

```
DEST REPLY
     PUB=$destination
     PRIV=$privkey
```
Начиная с версии 3.1 (I2P 0.9.14), поддерживается необязательный параметр SIGNATURE_TYPE. Значение SIGNATURE_TYPE может быть любым именем (например, ECDSA_SHA256_P256, регистр не учитывается) или числом (например, 1), которое поддерживается [Key Certificates](/docs/specs/common-structures#type_Certificate). По умолчанию используется DSA_SHA1, что НЕ то, что вам нужно. Для большинства приложений укажите SIGNATURE_TYPE=7.

$destination — это base 64 представление [Destination](/docs/specs/common-structures#type_Destination), которое содержит 516 или более символов base 64 (387 или более байт в двоичном формате), в зависимости от типа подписи.

$privkey — это base 64 представление конкатенации [Destination](/docs/specs/common-structures#type_Destination), за которым следует [Private Key](/docs/specs/common-structures#type_PrivateKey), за которым следует [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), что составляет 884 или более символов base 64 (663 или более байт в двоичном формате), в зависимости от типа подписи. Двоичный формат указан в Private Key File.

Примечания о 256-байтовом бинарном [Private Key](/docs/specs/common-structures#type_PrivateKey): Это поле не используется с версии 0.6 (2005). Реализации SAM могут отправлять случайные данные или все нули в этом поле; не беспокойтесь о строке AAAA в base 64. Большинство приложений просто сохранят строку base 64 и вернут её как есть в SESSION CREATE, или декодируют в бинарный формат для хранения, затем снова кодируют для SESSION CREATE. Приложения могут, однако, декодировать base 64, разобрать бинарные данные согласно спецификации PrivateKeyFile, отбросить 256-байтовую часть private key, а затем заменить её 256 байтами случайных данных или всех нулей при повторном кодировании для SESSION CREATE. ВСЕ остальные поля в спецификации PrivateKeyFile должны быть сохранены. Это сэкономит 256 байт хранилища файловой системы, но вероятно не стоит усилий для большинства приложений. См. предложение 161 для дополнительной информации и контекста.

DEST GENERATE не требует предварительного создания сессии.

DEST GENERATE нельзя использовать для создания назначения с автономными подписями.

#### PING/PONG (SAM 3.2 или выше)

Как клиент, так и сервер могут отправить:

```
PING[ arbitrary text]
```
на управляющем порту, с ответом:

```
PONG[ arbitrary text from the ping]
```
использоваться для поддержания активности управляющего сокета. Любая из сторон может закрыть сессию и сокет, если ответ не получен в разумное время, зависящее от реализации.

Если происходит таймаут при ожидании PONG от клиента, мост может отправить:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
а затем отключиться.

Если происходит таймаут при ожидании PONG от bridge, клиент может просто отключиться.

PING/PONG не требуют предварительного создания сессии.

#### QUIT/STOP/EXIT (SAM 3.2 или выше, дополнительные функции)

Команды QUIT, STOP и EXIT закроют сессию и сокет. Реализация необязательна, для удобства тестирования через telnet. Будет ли какой-либо ответ перед закрытием сокета (например, сообщение SESSION STATUS) зависит от конкретной реализации и выходит за рамки данной спецификации.

QUIT/STOP/EXIT не требуют предварительного создания сессии.

#### HELP (дополнительная функция)

Серверы могут реализовать команду HELP. Реализация является опциональной, для удобства тестирования через telnet. Формат вывода и определение конца вывода специфичны для реализации и не входят в область применения данной спецификации.

HELP не требует предварительного создания сессии.

#### Конфигурация авторизации (SAM 3.2 или выше, опциональная функция)

Конфигурация авторизации с использованием команды AUTH. SAM сервер может реализовать эти команды для обеспечения постоянного хранения учетных данных. Конфигурация аутентификации другими способами, помимо этих команд, зависит от конкретной реализации и выходит за рамки данной спецификации.

- AUTH ENABLE включает авторизацию для последующих соединений
- AUTH DISABLE отключает авторизацию для последующих соединений
- AUTH ADD USER="foo" PASSWORD="bar" добавляет пользователя/пароль
- AUTH REMOVE USER="foo" удаляет этого пользователя

Двойные кавычки для имени пользователя и пароля рекомендуются, но не обязательны. Двойная кавычка внутри имени пользователя или пароля должна быть экранирована обратной косой чертой. При неудаче сервер ответит с I2P_ERROR и сообщением.

AUTH не требует предварительного создания сессии.

### Значения RESULT

Это значения, которые может содержать поле RESULT, с их описанием:

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
Различные реализации могут быть непоследовательными в том, какой RESULT возвращается в различных сценариях.

Большинство ответов с RESULT, отличным от OK, также будут включать MESSAGE с дополнительной информацией. MESSAGE обычно будет полезным при отладке проблем. Однако строки MESSAGE зависят от реализации, могут переводиться или не переводиться SAM сервером на текущую локаль, могут содержать внутреннюю информацию, специфичную для реализации, такую как исключения, и могут изменяться без уведомления. Хотя SAM клиенты могут показывать строки MESSAGE пользователям, они не должны принимать программные решения на основе этих строк, поскольку это будет ненадежно.

### Параметры Tunnel, I2CP и Streaming

Эти параметры могут быть переданы как пары имя=значение в строке SAM SESSION CREATE.

Все сессии могут включать [опции I2CP, такие как длина и количество tunnel'ов](/docs/protocol/i2cp#options). STREAM сессии могут включать [опции библиотеки Streaming](/docs/api/streaming#options).

Смотрите эти справочные материалы для получения информации об именах опций и значениях по умолчанию. Указанная документация предназначена для Java-реализации router. Значения по умолчанию могут изменяться. Имена опций и их значения чувствительны к регистру. Другие реализации router могут поддерживать не все опции и иметь другие значения по умолчанию; подробности смотрите в документации router.

### Заметки о BASE 64

Кодирование Base 64 должно использовать стандартный алфавит I2P Base 64 "A-Z, a-z, 0-9, -, ~".

### Настройка SAM по умолчанию

Порт SAM по умолчанию — 7656. SAM не включен по умолчанию в Java I2P Router; он должен быть запущен вручную или настроен для автоматического запуска на странице настройки клиентов в консоли router или в файле clients.config. Порт SAM UDP по умолчанию — 7655, прослушивающий на 127.0.0.1. Эти настройки могут быть изменены в Java router путем добавления аргументов sam.udp.port=nnnnn и/или sam.udp.host=w.x.y.z к вызову или в строку SESSION.

Конфигурация в других router реализациях зависит от конкретной реализации. См. [руководство по настройке i2pd здесь](https://i2pd.readthedocs.io/en/latest/user-guide/configuration/).
