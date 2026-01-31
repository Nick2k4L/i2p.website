---
title: "SAM V3"
description: "Протокол простого анонимного обмена сообщениями для не-Java приложений I2P"
slug: "samv3"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

SAM — это простой клиентский протокол для взаимодействия с I2P. SAM является рекомендуемым протоколом для приложений, написанных не на Java, для подключения к сети I2P и поддерживается несколькими реализациями router. Приложения на Java должны использовать streaming или I2CP API напрямую.

SAMv3 был введен в релизе I2P 0.7.3 (май 2009 года) и является стабильным и поддерживаемым интерфейсом. 3.1 также стабилен и поддерживает опцию типа подписи, что настоятельно рекомендуется. Более поздние версии 3.x поддерживают расширенные возможности. Обратите внимание, что i2pd в настоящее время не поддерживает большинство функций 3.2 и 3.3.

Альтернативы: [SOCKS](/docs/api/socks), [Streaming](/docs/api/streaming), [I2CP](/docs/protocol/i2cp), [BOB (устаревший)](/docs/api/bob). Устаревшие версии: [SAM V1](/docs/api/sam), [SAM V2](/docs/api/samv2).

## Известные SAM библиотеки

Предупреждение: Некоторые из них могут быть очень старыми или неподдерживаемыми. Никто из них не тестируется, не проверяется и не поддерживается проектом I2P, если не указано ниже. Проводите собственные исследования.

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
## Быстрый старт

Для реализации базового TCP-приложения peer-to-peer клиент должен поддерживать следующие команды:

- `HELLO VERSION MIN=3.1 MAX=3.1` - Необходимо для всех остальных команд
- `DEST GENERATE SIGNATURE_TYPE=7` - Для генерации нашего приватного ключа и destination
- `NAMING LOOKUP NAME=...` - Для преобразования .i2p адресов в destinations
- `SESSION CREATE STYLE=STREAM ID=... DESTINATION=... i2cp.leaseSetEncType=4,0` - Необходимо для STREAM CONNECT и STREAM ACCEPT
- `STREAM CONNECT ID=... DESTINATION=...` - Для создания исходящих соединений
- `STREAM ACCEPT ID=...` - Для принятия входящих соединений

## Общее руководство для разработчиков

### Дизайн приложения

SAM сессии (или внутри I2P, пулы туннелей или наборы tunnel'ей) разработаны для длительного использования. Большинству приложений потребуется только одна сессия, созданная при запуске и закрытая при выходе. I2P отличается от Tor, где цепи могут быстро создаваться и отбрасываться. Тщательно обдумайте и проконсультируйтесь с разработчиками I2P, прежде чем проектировать ваше приложение для использования более одной или двух одновременных сессий, или для их быстрого создания и отбрасывания. Большинство моделей угроз не потребует уникальную сессию для каждого соединения.

Также, пожалуйста, убедитесь, что настройки вашего приложения (и рекомендации пользователям по настройкам router или настройки router по умолчанию, если вы включаете router в комплект) приведут к тому, что ваши пользователи будут предоставлять сети больше ресурсов, чем потребляют. I2P — это одноранговая сеть, и сеть не сможет выжить, если популярное приложение приведет к постоянной перегрузке сети.

### Совместимость и тестирование

Реализации router на Java I2P и i2pd являются независимыми и имеют незначительные различия в поведении, поддержке функций и настройках по умолчанию. Пожалуйста, протестируйте ваше приложение с последними версиями обоих router.

SAM в i2pd включен по умолчанию; SAM в Java I2P — нет. Предоставьте инструкции пользователям о том, как включить SAM в Java I2P (через /configclients в консоли router), и/или выводите понятное сообщение об ошибке пользователю, если первоначальное подключение не удалось, например: "убедитесь, что I2P запущен и интерфейс SAM включен".

Java I2P и i2pd router имеют разные значения по умолчанию для количества tunnel. По умолчанию в Java используется 2, а в i2pd — 5. Для большинства случаев с низкой и средней пропускной способностью и небольшим или средним количеством подключений достаточно 2 или 3. Пожалуйста, указывайте количество tunnel в сообщении SESSION CREATE, чтобы получить стабильную производительность с Java I2P и i2pd router. См. ниже.

Для получения дополнительных рекомендаций разработчикам по обеспечению использования вашим приложением только необходимых ресурсов, пожалуйста, ознакомьтесь с [нашим руководством по встраиванию I2P в ваше приложение](/docs/applications/embedding).

### Типы подписи и шифрования

I2P поддерживает несколько типов подписей и шифрования. Для обратной совместимости SAM по умолчанию использует старые и неэффективные типы, поэтому все клиенты должны указывать более новые типы.

Тип подписи указывается в командах DEST GENERATE и SESSION CREATE (для временных). Все клиенты должны устанавливать `SIGNATURE_TYPE=7` (Ed25519).

Тип шифрования указывается в команде SESSION CREATE. Разрешены множественные типы шифрования. Клиенты должны установить либо `i2cp.leaseSetEncType=4` (только для ECIES-X25519), либо `i2cp.leaseSetEncType=4,0` (для ECIES-X25519 и ElGamal, если требуется совместимость).

## Изменения в версии 3

### Изменения версии 3.0

Версия 3.0 была введена в релизе I2P 0.7.3. SAMv2 предоставил способ управлять несколькими сокетами на одном I2P destination *параллельно*, т.е. клиенту не нужно было ждать успешной отправки данных через один сокет перед отправкой данных через другой сокет. Но все данные передавались через один и тот же сокет клиент-SAM, что было довольно сложно для управления со стороны клиента.

SAM v3 управляет сокетами по-другому: каждый *I2P сокет* соответствует уникальному сокету клиент-SAM, что гораздо проще в обработке. Это похоже на [BOB](/docs/api/bob).

SAMv3 также предоставляет UDP-порт для отправки датаграмм через I2P и может перенаправлять I2P датаграммы обратно на датаграммный сервер клиента.

### Изменения версии 3.1

Версия 3.1 была введена в релизе Java I2P 0.9.14 (июль 2014). SAM 3.1 является рекомендуемой минимальной реализацией SAM из-за поддержки лучших типов подписей по сравнению с SAM 3.0. i2pd также поддерживает большинство функций 3.1.

- DEST GENERATE и SESSION CREATE теперь поддерживают параметр SIGNATURE_TYPE.
- Параметры MIN и MAX в HELLO VERSION теперь являются необязательными.
- Параметры MIN и MAX в HELLO VERSION теперь поддерживают однозначные версии, такие как "3".
- RAW SEND теперь поддерживается на bridge socket.

### Изменения версии 3.2

Версия 3.2 была представлена в релизе Java I2P 0.9.24 (январь 2016). Обратите внимание, что i2pd в настоящее время не поддерживает большинство функций версии 3.2.

#### Поддержка порта и протокола I2CP

- Опции SESSION CREATE FROM_PORT и TO_PORT
- Опция SESSION CREATE STYLE=RAW PROTOCOL
- Опции STREAM CONNECT, DATAGRAM SEND и RAW SEND FROM_PORT и TO_PORT
- Опция RAW SEND PROTOCOL
- DATAGRAM RECEIVED, RAW RECEIVED и переадресованные или полученные потоки и датаграммы с возможностью ответа включают FROM_PORT и TO_PORT
- Опция RAW session HEADER=true приведет к тому, что переадресованные raw датаграммы будут дополнены строкой, содержащей PROTOCOL=nnn FROM_PORT=nnnn TO_PORT=nnnn
- Первая строка датаграмм, отправленных через порт 7655, теперь может начинаться с любой версии 3.x
- Первая строка датаграмм, отправленных через порт 7655, может содержать любые из опций FROM_PORT, TO_PORT, PROTOCOL
- RAW RECEIVED включает PROTOCOL=nnn

#### SSL и аутентификация

- USER/PASSWORD в параметрах HELLO для авторизации. См. [ниже](#authorization).
- Опциональная конфигурация авторизации с помощью команды AUTH. См. [ниже](#authorization-configuration-sam-32-or-higher-optional-feature).
- Опциональная поддержка SSL/TLS на управляющем сокете. См. [ниже](#ssl).
- Опция STREAM FORWARD SSL=true

#### Многопоточность

- Одновременные ожидающие STREAM ACCEPT разрешены для одного и того же ID сессии.

#### Разбор командной строки и поддержание соединения

- Дополнительные команды QUIT, STOP и EXIT для закрытия сессии и сокета. См. [ниже](#quitstopexitinvisible-sam-32-or-higher-optional-features).
- Парсинг команд правильно обрабатывает UTF-8
- Парсинг команд надежно обрабатывает пробелы внутри кавычек
- Обратная косая черта '\\' может экранировать кавычки в командной строке
- Рекомендуется, чтобы сервер преобразовывал команды в верхний регистр для удобства тестирования через telnet.
- Пустые значения опций, такие как PROTOCOL или PROTOCOL=, могут быть разрешены, зависит от реализации.
- PING/PONG для поддержания соединения. См. ниже.
- Серверы могут реализовывать тайм-ауты для команды HELLO или последующих команд, зависит от реализации.

### Изменения в версии 3.3

Версия 3.3 была введена в релизе Java I2P 0.9.25 (март 2016). Обратите внимание, что i2pd в настоящее время не поддерживает большинство функций версии 3.3.

- Одна и та же сессия может использоваться для потоков, датаграмм и raw одновременно. Входящие пакеты и потоки будут маршrutизироваться на основе протокола I2P и порта назначения. См. [раздел PRIMARY ниже](#sam-primary-sessions-v33-and-higher).
- DATAGRAM SEND и RAW SEND теперь поддерживают опции SEND_TAGS, TAG_THRESHOLD, EXPIRES и SEND_LEASESET. См. [раздел отправки датаграмм ниже](#sending-repliable-or-raw-datagrams).

## Протокол версии 3

### Обзор спецификации Simple Anonymous Messaging (SAM) версии 3.3

Клиентское приложение взаимодействует с мостом SAM, который обрабатывает всю функциональность I2P (используя [библиотеку потоков](/docs/api/streaming) для виртуальных потоков или [I2CP](/docs/protocol/i2cp) напрямую для датаграмм).

По умолчанию связь между клиентом и мостом SAM не зашифрована и не аутентифицирована. Мост SAM может поддерживать SSL/TLS соединения; детали конфигурации и реализации выходят за рамки данной спецификации. Начиная с SAM 3.2, в начальном рукопожатии поддерживаются дополнительные параметры аутентификации имя пользователя/пароль, которые могут требоваться мостом.

Коммуникации I2P могут принимать несколько различных форм:

- [Виртуальные потоки](/docs/api/streaming)
- [Отвечаемые и аутентифицированные датаграммы](/docs/specs/datagrams#repliable) (сообщения с полем FROM)
- [Анонимные датаграммы](/docs/specs/datagrams#raw) (необработанные анонимные сообщения)
- [Datagram2](/docs/specs/datagrams#datagram2) (новый отвечаемый и аутентифицированный формат)
- [Datagram3](/docs/specs/datagrams#datagram3) (новый отвечаемый но неаутентифицированный формат)

Связь в I2P поддерживается сессиями I2P, и каждая сессия I2P привязана к адресу (называемому destination). Сессия I2P связана с одним из трех типов, указанных выше, и не может передавать сообщения другого типа, если не используются [PRIMARY сессии](#sam-primary-sessions-v33-and-higher).

### Кодирование и экранирование

Все эти SAM сообщения отправляются в одной строке, завершённой символом новой строки (\\n). До SAM 3.2 поддерживалась только 7-битная ASCII. Начиная с SAM 3.2, кодировка должна быть UTF-8. Любые ключи или значения в кодировке UTF8 должны работать.

Форматирование, показанное в данной спецификации ниже, предназначено исключительно для удобства чтения, и хотя первые два слова в каждом сообщении должны оставаться в своем определенном порядке, порядок пар ключ=значение может изменяться (например, "ONE TWO A=B C=D" или "ONE TWO C=D A=B" являются абсолютно корректными конструкциями). Кроме того, протокол чувствителен к регистру. Далее примеры сообщений предваряются символом "->" для сообщений, отправляемых клиентом SAM bridge, и символом "<-" для сообщений, отправляемых SAM bridge клиенту.

Базовая командная строка или строка ответа принимает одну из следующих форм:

```
COMMAND SUBCOMMAND [key=value] [key=value] ...
COMMAND                                           # As of SAM 3.2
PING[ arbitrary text]                             # As of SAM 3.2
PONG[ arbitrary text]                             # As of SAM 3.2
```
COMMAND без SUBCOMMAND поддерживается только для некоторых новых команд в SAM 3.2.

Пары ключ=значение должны быть разделены одним пробелом. (Начиная с SAMv3.2 допускаются множественные пробелы) Значения должны быть заключены в двойные кавычки, если они содержат пробелы, например key="long value text". (До SAMv3.2 это работало ненадежно в некоторых реализациях)

До SAMv3.2 не существовало механизма экранирования. Начиная с SAMv3.2, двойные кавычки могут быть экранированы обратной косой чертой '\\', а обратная косая черта может быть представлена как две обратные косые черты '\\\\'.

### Пустые значения

Начиная с SAMv3.2, пустые значения опций, такие как KEY, KEY= или KEY="", могут быть разрешены в зависимости от реализации.

### Чувствительность к регистру

Протокол, как указано в спецификации, чувствителен к регистру. Рекомендуется, но не обязательно, чтобы сервер преобразовывал команды в верхний регистр для упрощения тестирования через telnet. Это позволило бы, например, работать команде "hello version". Это зависит от реализации. Не преобразовывайте ключи или значения в верхний регистр, поскольку это повредит опции [I2CP](/docs/protocol/i2cp).

### Рукопожатие SAM-соединения

Никакая SAM коммуникация не может происходить до тех пор, пока клиент и мост не согласуют версию протокола, что выполняется посредством отправки клиентом HELLO и ответа моста HELLO REPLY:

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
Начиная с версии 3.1 (I2P 0.9.14), параметры MIN и MAX являются необязательными. SAM всегда возвращает максимально возможную версию с учетом ограничений MIN и MAX, или текущую версию сервера, если никаких ограничений не задано.

Если SAM bridge не может найти подходящую версию, он отвечает:

```
<- HELLO REPLY RESULT=NOVERSION
```
Если произошла какая-либо ошибка, например неверный формат запроса, он отвечает:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
#### SSL

Управляющий сокет сервера может дополнительно предлагать поддержку SSL/TLS в зависимости от конфигурации сервера и клиента. Реализации могут также предлагать другие транспортные уровни; это выходит за рамки определения протокола.

#### Авторизация

Для авторизации клиент добавляет USER="xxx" PASSWORD="yyy" к параметрам HELLO. Двойные кавычки для имени пользователя и пароля рекомендуются, но не являются обязательными. Двойная кавычка внутри имени пользователя или пароля должна быть экранирована обратной косой чертой. В случае неудачи сервер ответит I2P_ERROR с сообщением. Рекомендуется включить SSL на любых SAM серверах, где требуется авторизация.

#### Таймауты

Серверы могут реализовывать тайм-ауты для команды HELLO или последующих команд, в зависимости от реализации. Клиенты должны незамедлительно отправлять HELLO и следующую команду после подключения.

Если таймаут происходит до получения HELLO, мост отвечает:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
а затем отключается.

Если происходит тайм-аут после получения HELLO, но до следующей команды, мост отвечает:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
а затем отключается.

### Порты и протокол I2CP

Начиная с SAM 3.2, порты и протокол [I2CP](/docs/protocol/i2cp) могут быть указаны отправителем SAM клиента для передачи в [I2CP](/docs/protocol/i2cp), и SAM мост передаст полученную информацию о порте и протоколе [I2CP](/docs/protocol/i2cp) SAM клиенту.

For FROM_PORT and TO_PORT, допустимый диапазон — 0-65535, по умолчанию — 0.

Для PROTOCOL, который может быть указан только для RAW, допустимый диапазон составляет 0-255, а значение по умолчанию равно 18.

Для команд SESSION указанные порты и протокол являются значениями по умолчанию для этой сессии. Для отдельных потоков или датаграмм указанные порты и протокол переопределяют значения по умолчанию сессии. Для получаемых потоков или датаграмм указанные порты и протокол соответствуют тем, что получены от [I2CP](/docs/protocol/i2cp).

#### Важные отличия от стандартного IP

Порты I2CP предназначены для сокетов и датаграмм I2P. Они не связаны с вашими локальными сокетами, подключающимися к SAM.

- Порт 0 является допустимым и имеет специальное значение.
- Порты 1-1023 не являются специальными или привилегированными.
- Серверы по умолчанию слушают порт 0, что означает "все порты".
- Клиенты по умолчанию отправляют на порт 0, что означает "любой порт".
- Клиенты по умолчанию отправляют с порта 0, что означает "не указан".
- Серверы могут иметь службу, слушающую порт 0, и другие службы, слушающие более высокие порты. В этом случае служба на порту 0 является службой по умолчанию и будет использоваться для подключения, если входящий сокет или порт датаграммы не соответствует другой службе.
- Большинство I2P назначений имеют только одну запущенную службу, поэтому вы можете использовать настройки по умолчанию и игнорировать конфигурацию портов I2CP.
- Для указания портов I2CP требуется SAM 3.2 или 3.3.
- Если вам не нужны порты I2CP, вам не требуется SAM 3.2 или 3.3; достаточно версии 3.1.
- Протокол 0 является допустимым и означает "любой протокол". Это не рекомендуется и, вероятно, не будет работать.
- I2P сокеты отслеживаются по внутреннему идентификатору соединения. Поэтому нет требования к тому, чтобы кортеж из 5 элементов dest:port:dest:port:protocol был уникальным. Например, может существовать несколько сокетов с одинаковыми портами между двумя назначениями. Клиентам не нужно выбирать "свободный порт" для исходящего соединения.

Если вы разрабатываете приложение SAM 3.3 с несколькими подсессиями, тщательно продумайте, как эффективно использовать порты и протоколы. Дополнительную информацию смотрите в спецификации [I2CP](/docs/protocol/i2cp).

### SAM-сессии

SAM сессия создается клиентом, открывающим сокет к SAM мосту, выполняющим рукопожатие и отправляющим сообщение SESSION CREATE, и сессия завершается при отключении сокета.

Каждый зарегистрированный I2P Destination уникально связан с ID сессии (или псевдонимом). ID сессий, включая ID подсессий для PRIMARY сессий, должны быть глобально уникальными на SAM сервере. Во избежание возможных коллизий ID с другими клиентами, рекомендуется генерировать ID случайным образом.

Каждая сессия уникально связана с:

- сокет, из которого клиент создает сессию
- его ID (или псевдоним)

#### Запрос на создание сессии

Сообщение создания сессии может использовать только одну из этих форм (сообщения, полученные через другие формы, получают ответ с сообщением об ошибке):

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
DESTINATION указывает, какой пункт назначения должен использоваться для отправки и получения сообщений/потоков. $privkey — это base 64 от конкатенации [Destination](/docs/specs/common-structures#type_Destination), за которым следует [Private Key](/docs/specs/common-structures#type_PrivateKey), за которым следует [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), опционально за которым следует [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), что составляет 663 или более байт в двоичном формате и 884 или более байт в base 64, в зависимости от типа подписи. Двоичный формат указан в Private Key File. Смотрите дополнительные примечания о [Private Key](/docs/specs/common-structures#type_PrivateKey) в разделе Destination Key Generation ниже.

Если приватный ключ подписи состоит из одних нулей, следует секция [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature). Offline подписи поддерживаются только для STREAM и RAW сессий. Offline подписи не могут быть созданы с DESTINATION=TRANSIENT. Формат секции offline подписи следующий:

1. Метка времени истечения (4 байта, big endian, секунды с начала эпохи, переполняется в 2106 году)
2. Тип подписи временного открытого ключа подписи (2 байта, big endian)
3. Временный открытый ключ подписи (длина согласно типу временной подписи)
4. Подпись трех вышеперечисленных полей офлайн-ключом (длина согласно типу подписи назначения)
5. Временный закрытый ключ подписи (длина согласно типу временной подписи)

Если destination указан как TRANSIENT, SAM мост создает новый destination. Начиная с версии 3.1 (I2P 0.9.14), если destination является TRANSIENT, поддерживается дополнительный параметр SIGNATURE_TYPE. Значение SIGNATURE_TYPE может быть любым именем (например, ECDSA_SHA256_P256, регистр не учитывается) или номером (например, 1), поддерживаемым [Key Certificates](/docs/specs/common-structures#type_Certificate). По умолчанию используется DSA_SHA1, что НЕ является желаемым. Для большинства приложений укажите SIGNATURE_TYPE=7.

$nickname выбирается клиентом. Пробелы не допускаются.

Дополнительные переданные параметры передаются в конфигурацию I2P-сессии, если они не обрабатываются SAM-мостом (например, outbound.length=0).

Роутеры Java I2P и i2pd имеют разные значения по умолчанию для количества tunnel. Значение по умолчанию для Java составляет 2, а для i2pd — 5. Для большинства случаев с низкой и средней пропускной способностью и низким и средним количеством соединений достаточно 2 или 3. Пожалуйста, укажите количество tunnel в сообщении SESSION CREATE, чтобы получить стабильную производительность с роутерами Java I2P и i2pd, используя опции, например inbound.quantity=3 outbound.quantity=3. Эти и другие опции [задокументированы по ссылкам ниже](#tunnel-i2cp-and-streaming-options).

SAM мост сам по себе уже должен быть настроен с указанием того, какой router он должен использовать для связи через I2P (хотя при необходимости может быть способ переопределить это, например, i2cp.tcp.host=localhost и i2cp.tcp.port=7654).

#### Ответ на создание сессии

После получения сообщения создания сессии, мост SAM ответит сообщением о статусе сессии, как показано ниже:

Если создание прошло успешно:

```
<-  SESSION STATUS RESULT=OK DESTINATION=$privkey
```
$privkey представляет собой base 64 кодировку объединения [Destination](/docs/specs/common-structures#type_Destination), за которым следует [Private Key](/docs/specs/common-structures#type_PrivateKey), затем [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), и опционально [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), что составляет 663 или более байт в двоичном формате и 884 или более байт в base 64, в зависимости от типа подписи. Двоичный формат определён в Private Key File.

Если SESSION CREATE содержал приватный ключ подписи, состоящий из всех нулей, и секцию [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), то ответ SESSION STATUS будет включать те же данные в том же формате. См. раздел SESSION CREATE выше для подробностей.

Если псевдоним уже связан с сессией:

```
<-  SESSION STATUS RESULT=DUPLICATED_ID
```
Если пункт назначения уже используется:

```
<-  SESSION STATUS RESULT=DUPLICATED_DEST
```
Если destination не является действительным ключом приватного destination:

```
<-  SESSION STATUS RESULT=INVALID_KEY
```
Если произошла какая-либо другая ошибка:

```
<-  SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
Если это не OK, MESSAGE должно содержать информацию в человекочитаемом виде о том, почему сессия не может быть создана.

Обратите внимание, что router строит tunnels перед ответом SESSION STATUS. Это может занять несколько секунд или, при запуске router или во время серьезной перегрузки сети, минуту или больше. В случае неудачи router не ответит сообщением об ошибке в течение нескольких минут. Не устанавливайте короткий таймаут ожидания ответа. Не прерывайте сессию во время построения tunnel и не повторяйте попытку.

Сессии SAM существуют и завершаются вместе с сокетом, с которым они связаны. Когда сокет закрывается, сессия завершается, и все коммуникации, использующие эту сессию, прекращаются одновременно. И наоборот, когда сессия завершается по любой причине, мост SAM закрывает сокет.

### Виртуальные потоки SAM

Виртуальные потоки гарантированно отправляются надёжно и по порядку, с уведомлением о неудаче или успехе, как только оно становится доступным.

Потоки представляют собой двунаправленные коммуникационные сокеты между двумя I2P destinations, но их открытие должно быть запрошено одним из них. Далее команды CONNECT используются SAM клиентом для такого запроса. Команды FORWARD / ACCEPT используются SAM клиентом, когда он хочет прослушивать запросы, поступающие от других I2P destinations.

### SAM Virtual Streams: CONNECT

Клиент запрашивает соединение следующим способом:

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
Это устанавливает новое виртуальное соединение от локальной сессии с ID $nickname к указанному узлу.

Цель - это $destination, которая представляет собой base 64 от [Destination](/docs/specs/common-structures#type_Destination), что составляет 516 или более символов base 64 (387 или более байт в двоичном формате), в зависимости от типа подписи.

**ПРИМЕЧАНИЕ:** Примерно с 2014 года (SAM v3.1) Java I2P также поддерживает имена хостов и b32 адреса для $destination, но это ранее не было задокументировано. Имена хостов и b32 адреса теперь официально поддерживаются Java I2P начиная с релиза 0.9.48. Router i2pd поддерживает имена хостов и b32 адреса начиная с релиза 2.38.0 (0.9.50). Для обоих router'ов поддержка "b32" включает поддержку расширенных "b33" адресов для скрытых назначений.

#### Ответ на подключение

Если передан параметр SILENT=true, мост SAM не будет отправлять никаких других сообщений через сокет. Если соединение не удастся, сокет будет закрыт. Если соединение успешно, все оставшиеся данные, проходящие через текущий сокет, будут перенаправлены от и к подключенному узлу назначения I2P.

Если SILENT=false, что является значением по умолчанию, SAM bridge отправляет последнее сообщение своему клиенту перед переадресацией или закрытием сокета:

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
Если RESULT равен OK, все остальные данные, проходящие через текущий сокет, пересылаются от и к подключенному I2P destination узлу. Если соединение было невозможно (тайм-аут и т.д.), RESULT будет содержать соответствующее значение ошибки (сопровождаемое необязательным человекочитаемым MESSAGE), и SAM мост закрывает сокет.

Таймаут подключения потока router внутренне составляет примерно одну минуту, зависит от реализации. Не устанавливайте более короткий таймаут для ожидания ответа.

### SAM Виртуальные потоки: ACCEPT

Клиент ожидает входящий запрос соединения следующим образом:

- открытие нового сокета с мостом SAM
- передача того же рукопожатия HELLO, как указано выше
- отправка команды STREAM ACCEPT

#### Принять запрос

```
-> STREAM ACCEPT
         ID=$nickname
         [SILENT={true,false}]                # default false
```
Это заставляет сессию ${nickname} ожидать одного входящего запроса соединения из сети I2P. ACCEPT не разрешен, пока в сессии активен FORWARD.

Начиная с SAMv3.2, разрешены множественные одновременные ожидающие STREAM ACCEPT на одном и том же ID сессии (даже с одним и тем же портом). До версии 3.2 одновременные accept завершались ошибкой ALREADY_ACCEPTING. Примечание: Java I2P также поддерживает одновременные ACCEPT в SAMv3.1, начиная с релиза 0.9.24 (январь 2016). i2pd также поддерживает одновременные ACCEPT в SAMv3.1, начиная с релиза 2.50.0 (декабрь 2023).

#### Ответ принятия

Если передается SILENT=true, SAM bridge не будет отправлять никаких других сообщений в сокет. Если подключение не удается, сокет будет закрыт. Если подключение успешно, все оставшиеся данные, проходящие через текущий сокет, пересылаются от и к подключенному I2P peer назначения. Для надежности и получения назначения для входящих соединений рекомендуется использовать SILENT=false.

Если SILENT=false, что является значением по умолчанию, SAM bridge отвечает:

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
Если результат не OK, сокет немедленно закрывается SAM мостом. Если результат OK, SAM мост начинает ожидать входящий запрос на соединение от другого I2P узла. Когда запрос поступает, SAM мост принимает его и:

Если был передан параметр SILENT=true, SAM мост не будет отправлять никаких других сообщений на клиентский сокет. Все остальные данные, проходящие через текущий сокет, перенаправляются от и к подключенному I2P узлу назначения.

Если было передано SILENT=false, что является значением по умолчанию, SAM мост отправляет клиенту ASCII строку, содержащую base64 публичный ключ назначения запрашивающего узла, а также дополнительную информацию только для SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
После этой строки, завершающейся '\\n', все остальные данные, проходящие через текущий сокет, пересылаются от и к подключенному I2P destination узлу, пока один из узлов не закроет сокет.

#### Ошибки После OK

В редких случаях мост SAM может столкнуться с ошибкой после отправки RESULT=OK, но до установления соединения и отправки строки $destination клиенту. Эти ошибки могут включать выключение router, перезапуск router и закрытие сессии. В таких случаях, когда SILENT=false, мост SAM может, но не обязан (зависит от реализации), отправить строку:

```
<-  STREAM STATUS
         RESULT=I2P_ERROR
         [MESSAGE=...]
```
перед немедленным закрытием сокета. Эта строка, конечно же, не может быть декодирована как валидный Base 64 destination.

### SAM Virtual Streams: FORWARD

Клиент может использовать обычный socket-сервер и ожидать запросы на подключение, поступающие из I2P. Для этого клиент должен:

- открыть новый сокет с SAM мостом
- передать то же рукопожатие HELLO, что и выше
- отправить команду forward

#### Запрос переадресации

```
-> STREAM FORWARD
         ID=$nickname
         PORT=$port
         [HOST=$host]
         [SILENT={true,false}]                # default false
         [SSL={true,false}]                   # SAM 3.2 or higher only, default false
```
Это заставляет сессию ${nickname} прослушивать входящие запросы соединения из сети I2P. FORWARD не разрешен, пока на сессии есть ожидающий ACCEPT.

#### Ответ пересылки

SILENT по умолчанию равен false. Независимо от того, является ли SILENT true или false, SAM bridge всегда отвечает сообщением STREAM STATUS. Обратите внимание, что это отличается от поведения STREAM ACCEPT и STREAM CONNECT при SILENT=true. Сообщение STREAM STATUS имеет вид:

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
$host — это имя хоста или IP-адрес сокетного сервера, на который SAM будет перенаправлять запросы на подключение. Если не указан, SAM использует IP сокета, который выдал команду forward.

$port — это номер порта сокет-сервера, на который SAM будет перенаправлять запросы подключения. Это обязательный параметр.

Когда запрос на соединение поступает из I2P, мост SAM открывает сокет-соединение с $host:$port. Если оно принимается менее чем за 3 секунды, SAM примет соединение из I2P, а затем:

Если был передан параметр SILENT=true, все данные, проходящие через полученный текущий сокет, перенаправляются от и к подключенному узлу I2P destination.

Если был передан SILENT=false, что является значением по умолчанию, SAM мост отправляет на полученный сокет ASCII строку, содержащую base64 публичный ключ destination запрашивающего узла, и дополнительную информацию только для SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
После этой строки, завершаемой '\\n', все оставшиеся данные, проходящие через сокет, пересылаются от и к подключенному I2P destination узлу, пока одна из сторон не закроет сокет.

Начиная с SAM 3.2, если указано SSL=true, пересылающий сокет работает через SSL/TLS.

I2P router прекратит прослушивание входящих запросов на соединение, как только "пересылающий" сокет будет закрыт.

### SAM датаграммы

SAMv3 предоставляет механизмы для отправки и получения датаграмм через локальные datagram сокеты. Некоторые реализации SAMv3 также поддерживают более старый способ v1/v2 отправки/получения датаграмм через bridge сокет SAM. Оба способа задокументированы ниже.

I2P поддерживает четыре типа датаграмм:

- Датаграммы с возможностью ответа и аутентификацией имеют префикс с destination отправителя и содержат подпись отправителя, поэтому получатель может проверить, что destination отправителя не был подделан, и может ответить на датаграмму. Новый формат Datagram2 также поддерживает ответы и аутентификацию.
- Новый формат Datagram3 поддерживает ответы, но не аутентификацию. Информация об отправителе не проверяется.
- Необработанные датаграммы не содержат destination отправителя или подпись.

Порты I2CP по умолчанию определены как для отвечаемых, так и для необработанных датаграмм. Порт I2CP может быть изменен для необработанных датаграмм.

Распространённый шаблон проектирования протокола заключается в отправке датаграмм с возможностью ответа на серверы с включением некоторого идентификатора, и сервер отвечает обычной датаграммой, которая включает этот идентификатор, чтобы ответ можно было соотнести с запросом. Этот шаблон проектирования устраняет значительные накладные расходы датаграмм с возможностью ответа в ответах. Все выборы I2CP протоколов и портов специфичны для приложения, и разработчики должны учитывать эти вопросы.

См. также важные замечания о MTU датаграмм в разделе ниже.

#### Отправка датаграмм с возможностью ответа или сырых датаграмм

Хотя I2P изначально не содержит адрес FROM, для удобства использования предоставляется дополнительный уровень в виде repliable datagrams - неупорядоченных и ненадёжных сообщений размером до 31744 байт, которые включают адрес FROM (оставляя до 1КБ для заголовочного материала). Этот адрес FROM аутентифицируется внутренне SAM (используя ключ подписи destination для проверки источника) и включает защиту от повторных атак.

Минимальный размер составляет 1. Для обеспечения наилучшей надёжности доставки рекомендуемый максимальный размер составляет приблизительно 11 КБ. Надёжность обратно пропорциональна размеру сообщения, возможно даже экспоненциально.

После установления SAM-сессии с STYLE=DATAGRAM или STYLE=RAW, клиент может отправлять repliable или raw датаграммы через UDP-порт SAM (7655 по умолчанию).

Первая строка датаграммы, отправленной через этот порт, должна быть в следующем формате. Всё это располагается в одной строке (разделено пробелами), показано в нескольких строках для ясности:

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
- 3.0 — это версия SAM. Начиная с SAM 3.2, допускается любая версия 3.x.
- $nickname — это идентификатор DATAGRAM-сессии, которая будет использоваться
- Цель — это $destination, которая представляет собой base 64 от [Destination](/docs/specs/common-structures#type_Destination), что составляет 516 или более символов base 64 (387 или более байт в двоичном виде), в зависимости от типа подписи. **ПРИМЕЧАНИЕ:** Примерно с 2014 года (SAM v3.1) Java I2P также поддерживает имена хостов и b32-адреса для $destination, но это ранее не было задокументировано. Имена хостов и b32-адреса теперь официально поддерживаются Java I2P начиная с релиза 0.9.48. router i2pd в настоящее время не поддерживает имена хостов и b32-адреса; поддержка может быть добавлена в будущих версиях.
- Все опции являются настройками для отдельных датаграмм, которые переопределяют значения по умолчанию, указанные в SESSION CREATE.
- Опции версии 3.3 SEND_TAGS, TAG_THRESHOLD, EXPIRES и SEND_LEASESET будут переданы в [I2CP](/docs/protocol/i2cp), если поддерживается. См. [спецификацию I2CP](/docs/protocol/i2cp#msg_SendMessageExpire) для подробностей. Поддержка SAM-сервером является опциональной, он будет игнорировать эти опции, если они не поддерживаются.
- эта строка завершается '\\n'.

Первая строка будет отброшена SAM перед отправкой оставшихся данных сообщения на указанное назначение.

Для альтернативного способа отправки датаграмм с возможностью ответа и сырых датаграмм, см. [DATAGRAM SEND и RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### SAM Repliable Datagrams: Получение датаграммы

Полученные датаграммы записываются SAM в сокет, из которого была открыта сессия датаграмм, если переадресующий PORT не указан в команде SESSION CREATE. Это способ получения датаграмм, совместимый с v1/v2.

Когда приходит датаграмма, мост доставляет её клиенту через сообщение:

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

SAM-мост никогда не предоставляет клиенту заголовки аутентификации или другие поля, а только данные, которые предоставил отправитель. Это продолжается до закрытия сессии (когда клиент разрывает соединение).

#### Перенаправление необработанных или отвечаемых датаграмм

При создании сессии датаграммы клиент может попросить SAM перенаправлять входящие сообщения на указанный ip:порт. Это делается путем выполнения команды CREATE с опциями PORT и HOST:

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
$privkey представляет собой base 64 кодировку конкатенации [Destination](/docs/specs/common-structures#type_Destination), за которым следует [Private Key](/docs/specs/common-structures#type_PrivateKey), затем [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), и опционально [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), что составляет 884 или более символов base 64 (663 или более байт в двоичном формате), в зависимости от типа подписи. Двоичный формат определяется в файле Private Key File.

Автономные подписи поддерживаются для датаграмм RAW, DATAGRAM2 и DATAGRAM3, но не для DATAGRAM. См. раздел SESSION CREATE выше и раздел DATAGRAM2/3 ниже для получения подробной информации.

$host — это имя хоста или IP-адрес сервера датаграмм, на который SAM будет перенаправлять датаграммы. Если не указан, SAM использует IP сокета, который выдал команду forward.

$port - это номер порта сервера датаграмм, на который SAM будет пересылать датаграммы. Если $port не установлен, датаграммы НЕ будут пересылаться, они будут получены на управляющем сокете в режиме, совместимом с v1/v2.

Дополнительные переданные параметры передаются в конфигурацию I2P сессии, если они не интерпретируются SAM мостом (например, outbound.length=0). Эти параметры [документированы ниже](#tunnel-i2cp-and-streaming-options).

Переадресованные датаграммы с возможностью ответа всегда начинаются с base64 назначения, за исключением Datagram3, см. ниже. Когда приходит датаграмма с возможностью ответа, мост отправляет на указанные host:port UDP-пакет, содержащий следующие данные:

```
$destination                       # See notes below for Datagram3 format
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
$datagram_payload
```
Пересылаемые необработанные датаграммы пересылаются как есть на указанный host:port без префикса. UDP-пакет содержит следующие данные:

```
$datagram_payload
```
Начиная с SAM 3.2, когда в SESSION CREATE указано HEADER=true, пересылаемая raw datagram будет предваряться строкой заголовка следующим образом:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
$destination — это base 64 представление [Destination](/docs/specs/common-structures#type_Destination), которое составляет 516 или более символов base 64 (387 или более байт в двоичном виде), в зависимости от типа подписи.

#### SAM анонимные (raw) датаграммы

Выжимая максимум из пропускной способности I2P, SAM позволяет клиентам отправлять и получать анонимные датаграммы, оставляя аутентификацию и информацию об ответах на усмотрение самих клиентов. Эти датаграммы ненадежны и неупорядочены, и могут быть размером до 32768 байт.

Минимальный размер составляет 1. Для наилучшей надежности доставки рекомендуемый максимальный размер составляет приблизительно 11 КБ.

После установления SAM сессии с STYLE=RAW, клиент может отправлять анонимные датаграммы через SAM мост точно так же, как [отправка датаграмм с возможностью ответа](#sending-repliable-or-raw-datagrams).

Оба способа получения датаграмм также доступны для анонимных датаграмм.

Полученные датаграммы записываются SAM на сокет, с которого была открыта сессия датаграммы, если перенаправляющий PORT не указан в команде SESSION CREATE. Это способ получения датаграмм, совместимый с v1/v2.

```
<- RAW RECEIVED
          SIZE=$numBytes
          FROM_PORT=nnn                      # SAM 3.2 or higher only
          TO_PORT=nnn                        # SAM 3.2 or higher only
          PROTOCOL=nnn                       # SAM 3.2 or higher only
          \n
      [$numBytes of data]
```
Когда анонимные датаграммы должны быть переданы на некоторый host:port, мост отправляет на указанный host:port сообщение, содержащее следующие данные:

```
$datagram_payload
```
Начиная с SAM 3.2, когда в SESSION CREATE указан параметр HEADER=true, пересылаемая сырая датаграмма будет дополнена заголовочной строкой следующим образом:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
Для альтернативного способа отправки анонимных датаграмм см. [RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### Датаграмма 2/3

Datagram 2/3 — это новые форматы, определённые в начале 2025 года. На данный момент не существует известных реализаций. Проверьте документацию реализации для получения актуального статуса. См. [спецификацию](/docs/specs/datagrams) для получения дополнительной информации.

В настоящее время нет планов увеличить версию SAM для обозначения поддержки Datagram 2/3. Это может быть проблематично, поскольку реализации могут захотеть поддерживать Datagram 2/3, но не функции SAM v3.3. Любые изменения версии пока не определены.

И Datagram2, и Datagram3 поддерживают ответы. Только Datagram2 является аутентифицированным.

Datagram2 идентичен отвечаемым датаграммам с точки зрения SAM. Оба аутентифицированы. Отличаются только формат I2CP и подпись, но это не видно клиентам SAM. Datagram2 также поддерживает офлайн подписи, поэтому может использоваться назначениями с офлайн подписью.

Цель состоит в том, чтобы Datagram2 заменил Repliable датаграммы для новых приложений, которые не требуют обратной совместимости. Datagram2 обеспечивает защиту от повторов, которая отсутствует у Repliable датаграмм. Если требуется обратная совместимость, приложение может поддерживать как Datagram2, так и Repliable в одной сессии с SAM 3.3 PRIMARY сессиями.

Datagram3 поддерживает ответы, но не аутентифицирован. Поле 'from' в формате I2CP является хешем, а не destination. $destination, отправляемый с SAM сервера клиенту, будет 44-байтовым base64 хешем. Чтобы преобразовать его в полный destination для ответа, декодируйте его из base64 в 32 байта в бинарном виде, затем закодируйте в base32 до 52 символов и добавьте ".b32.i2p" для NAMING LOOKUP. Как обычно, клиенты должны поддерживать собственный кеш, чтобы избежать повторных NAMING LOOKUP.

Разработчики приложений должны проявлять крайнюю осторожность и учитывать последствия для безопасности при использовании неаутентифицированных датаграмм.

#### Соображения относительно MTU датаграмм V3

I2P датаграммы могут быть больше типичного интернет MTU в 1500 байт. Локально отправленные датаграммы и пересылаемые с возможностью ответа датаграммы с префиксом в виде base64 назначения размером 516+ байт, вероятно, превысят этот MTU. Однако MTU localhost в системах Linux обычно намного больше, например 65536. MTU localhost будет различаться в зависимости от ОС. I2P датаграммы никогда не будут больше 65536 байт. Размер датаграммы зависит от протокола приложения.

Если SAM клиент локален по отношению к SAM серверу и система поддерживает больший MTU, то датаграммы не будут фрагментированы локально. Однако, если SAM клиент удаленный, то IPv4 датаграммы будут фрагментированы, а IPv6 датаграммы завершатся неудачей (IPv6 не поддерживает UDP фрагментацию).

Разработчики клиентских библиотек и приложений должны знать об этих проблемах и документировать рекомендации по предотвращению фрагментации и потери пакетов, особенно при удаленных соединениях клиент-сервер SAM.

#### DATAGRAM SEND, RAW SEND (V1/V2 Совместимая обработка датаграмм)

В SAMv3 предпочтительным способом отправки датаграмм является использование datagram socket на порту 7655, как описано выше. Однако датаграммы с возможностью ответа могут быть отправлены напрямую через SAM bridge socket с помощью команды DATAGRAM SEND, как описано в [SAM V1](/docs/api/sam) и [SAM V2](/docs/api/samv2).

Начиная с релиза 0.9.14 (версия 3.1), анонимные датаграммы могут быть отправлены напрямую через сокет моста SAM с использованием команды RAW SEND, как документировано в [SAM V1](/docs/api/sam) и [SAM V2](/docs/api/samv2).

Начиная с релиза 0.9.24 (версия 3.2), DATAGRAM SEND и RAW SEND могут включать параметры FROM_PORT=nnnn и/или TO_PORT=nnnn для переопределения портов по умолчанию. Начиная с релиза 0.9.24 (версия 3.2), RAW SEND может включать параметр PROTOCOL=nnn для переопределения протокола по умолчанию.

Эти команды *не* поддерживают параметр ID. Датаграммы отправляются в последнюю созданную сессию типа DATAGRAM или RAW, в зависимости от ситуации. Поддержка параметра ID может быть добавлена в будущих версиях.

Форматы DATAGRAM2 и DATAGRAM3 *не* поддерживаются в режиме совместимости с V1/V2.

### SAM PRIMARY сессии (V3.3 и выше)

*Версия 3.3 была введена в релизе I2P 0.9.25.*

*В более ранней версии данной спецификации PRIMARY сессии назывались MASTER сессиями. В `i2pd` и `I2P+` они до сих пор известны только как MASTER сессии.*

SAM v3.3 добавляет поддержку запуска streaming, datagram и raw подсессий в рамках одной основной сессии, а также возможность запуска нескольких подсессий одного типа. Весь трафик подсессий использует одно назначение или набор tunnel. Маршрутизация трафика из I2P основана на параметрах порта и протокола для подсессий.

Для создания мультиплексированных подсессий необходимо создать основную сессию, а затем добавить подсессии к основной сессии. Каждая подсессия должна иметь уникальный идентификатор и уникальный протокол прослушивания и порт. Подсессии также могут быть удалены из основной сессии.

С помощью PRIMARY сессии и комбинации подсессий, SAM клиент может поддерживать несколько приложений или одно сложное приложение, использующее различные протоколы, на одном наборе туннелей. Например, bittorrent клиент может настроить потоковую подсессию для peer-to-peer соединений вместе с datagram и raw подсессиями для DHT коммуникации.

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
SAM bridge ответит успехом или неудачей, как в [ответе на стандартный SESSION CREATE](#session-creation-response).

Не устанавливайте параметры PORT, HOST, FROM_PORT, TO_PORT, PROTOCOL, LISTEN_PORT, LISTEN_PROTOCOL или HEADER для основной сессии. Вы не можете отправлять данные через PRIMARY session ID или через управляющий сокет. Все команды, такие как STREAM CONNECT, DATAGRAM SEND и т.д., должны использовать ID подсессии на отдельном сокете.

ПЕРВИЧНАЯ сессия подключается к router и строит tunnel'ы. Когда SAM мост отвечает, tunnel'ы уже построены и сессия готова для добавления подсессий. Все опции [I2CP](/docs/protocol/i2cp), относящиеся к параметрам tunnel'ов, таким как длина, количество и псевдоним, должны быть предоставлены в SESSION CREATE первичной сессии.

Все служебные команды поддерживаются в основной сессии.

Когда основная сессия закрывается, все подсессии также закрываются.

ПРИМЕЧАНИЕ: До версии 0.9.47 используйте STYLE=MASTER. STYLE=PRIMARY поддерживается начиная с версии 0.9.47. MASTER по-прежнему поддерживается для обратной совместимости.

#### Создание подсессии

Используя тот же контрольный сокет, на котором была создана PRIMARY сессия:

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
SAM мост ответит успехом или неудачей, как в [ответе на стандартный SESSION CREATE](#session-creation-response). Поскольку туннели уже были построены в основном SESSION CREATE, SAM мост должен ответить немедленно.

Не устанавливайте опцию DESTINATION для SESSION ADD. Подсессия будет использовать destination, указанный в основной сессии. Все подсессии должны быть добавлены через управляющий сокет, т.е. через то же соединение, на котором вы создали основную сессию.

Множественные подсессии должны иметь достаточно уникальные параметры, чтобы входящие данные могли маршрутизироваться корректно. В частности, множественные сессии одного типа должны иметь разные параметры LISTEN_PORT (и/или LISTEN_PROTOCOL только для RAW). Команда SESSION ADD с портом прослушивания и протоколом, дублирующими существующую подсессию, приведет к ошибке.

LISTEN_PORT - это локальный I2P порт, то есть принимающий (TO) порт для входящих данных. Если LISTEN_PORT не указан, будет использоваться значение FROM_PORT. Если LISTEN_PORT и FROM_PORT не указаны, маршрутизация входящих соединений будет основываться только на STYLE и PROTOCOL. Для LISTEN_PORT и LISTEN_PROTOCOL значение 0 означает любое значение, то есть является подстановочным знаком. Если и LISTEN_PORT, и LISTEN_PROTOCOL равны 0, эта подсессия будет использоваться по умолчанию для входящего трафика, который не маршрутизируется к другой подсессии. Входящий streaming трафик (протокол 6) никогда не будет маршрутизироваться к RAW подсессии, даже если её LISTEN_PROTOCOL равен 0. RAW подсессия не может установить LISTEN_PROTOCOL равным 6. Если нет подсессии по умолчанию или подсессии, соответствующей протоколу и порту входящего трафика, эти данные будут отброшены.

Используйте ID подсессии, а не ID основной сессии, для отправки и получения данных. Все команды, такие как STREAM CONNECT, DATAGRAM SEND и т.д., должны использовать ID подсессии.

Все служебные команды поддерживаются в основной сессии или подсессии. Отправка/получение датаграмм/raw данных v1/v2 не поддерживается в основной сессии или в подсессиях.

#### Остановка подсессии

Используя тот же управляющий сокет, на котором была создана PRIMARY сессия:

```
->  SESSION REMOVE
          ID=$nickname
```
Это удаляет подсессию из основной сессии. Не устанавливайте никаких других опций для SESSION REMOVE. Подсессии должны удаляться через управляющий сокет, то есть через то же соединение, на котором вы создали основную сессию. После удаления подсессии она закрывается и больше не может использоваться для отправки или получения данных.

SAM мост ответит сообщением об успехе или неудаче, как в [ответе на стандартную команду SESSION CREATE](#session-creation-response).

### Служебные команды SAM

Некоторые служебные команды требуют уже существующей сессии, а некоторые нет. Подробности смотрите ниже.

#### Поиск имени хоста

Следующее сообщение может использоваться клиентом для запроса разрешения имен у SAM bridge:

```
NAMING LOOKUP
       NAME=$name
       [OPTIONS=true]     # Default false, as of router API 0.9.66
```
на что отвечается

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
Если NAME=ME, то ответ будет содержать destination, используемый текущей сессией (полезно, если вы используете TRANSIENT). Если $result не OK, MESSAGE может содержать описательное сообщение, такое как "bad format" и т.д. INVALID_KEY означает, что что-то не так с $name в запросе, возможно недопустимые символы.

$destination — это base 64 представление [Destination](/docs/specs/common-structures#type_Destination), которое составляет 516 или более символов base 64 (387 или более байт в двоичном формате), в зависимости от типа подписи.

NAMING LOOKUP не требует предварительного создания сессии. Однако в некоторых реализациях поиск .b32.i2p, который не кэширован и требует сетевого запроса, может завершиться неудачей, поскольку для поиска недоступны клиентские tunnel.

#### Опции поиска имён

NAMING LOOKUP расширен с версии router API 0.9.66 для поддержки поиска сервисов. Поддержка может различаться в зависимости от реализации. См. предложение 167 для дополнительной информации.

NAMING LOOKUP NAME=example.i2p OPTIONS=true запрашивает сопоставление опций в ответе. NAME может быть полным base64 назначением, когда OPTIONS=true.

Если поиск назначения был успешным и в leaseset присутствовали опции, то в ответе после назначения будет одна или несколько опций в форме OPTION:key=value. Каждая опция будет иметь отдельный префикс OPTION:. Будут включены все опции из leaseset, а не только опции записей сервиса. Например, могут присутствовать опции для параметров, определенных в будущем. Пример:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Ключи, содержащие '=', и ключи или значения, содержащие символ новой строки, считаются недопустимыми, и пара ключ/значение будет удалена из ответа. Если в leaseset не найдены опции, или если leaseset был версии 1, то ответ не будет включать никаких опций. Если OPTIONS=true был в запросе, а leaseset не найден, будет возвращено новое значение результата LEASESET_NOT_FOUND.

#### Генерация ключа назначения

Публичные и приватные ключи в формате base64 можно сгенерировать с помощью следующего сообщения:

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
Начиная с версии 3.1 (I2P 0.9.14) поддерживается необязательный параметр SIGNATURE_TYPE. Значение SIGNATURE_TYPE может быть любым именем (например, ECDSA_SHA256_P256, регистр не учитывается) или номером (например, 1), которое поддерживается [Сертификатами ключей](/docs/specs/common-structures#type_Certificate). По умолчанию используется DSA_SHA1, что НЕ является желательным выбором. Для большинства приложений, пожалуйста, укажите SIGNATURE_TYPE=7.

$destination — это base 64 представление [Destination](/docs/specs/common-structures#type_Destination), которое содержит 516 или более символов base 64 (387 или более байт в двоичном виде), в зависимости от типа подписи.

$privkey представляет собой base 64 от конкатенации [Destination](/docs/specs/common-structures#type_Destination), за которым следует [Private Key](/docs/specs/common-structures#type_PrivateKey), за которым следует [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), что составляет 884 или более символов base 64 (663 или более байт в двоичном формате), в зависимости от типа подписи. Двоичный формат описан в Private Key File.

Примечания о 256-байтовом двоичном [Private Key](/docs/specs/common-structures#type_PrivateKey): Это поле не используется с версии 0.6 (2005). Реализации SAM могут отправлять случайные данные или все нули в этом поле; не стоит беспокоиться о строке из AAAA в base 64. Большинство приложений будет просто хранить строку base 64 и возвращать её как есть в SESSION CREATE, или декодировать в двоичный формат для хранения, а затем снова кодировать для SESSION CREATE. Приложения могут, однако, декодировать base 64, разобрать двоичные данные согласно спецификации PrivateKeyFile, отбросить 256-байтовую часть private key, а затем заменить её на 256 байт случайных данных или всех нулей при повторном кодировании для SESSION CREATE. ВСЕ остальные поля в спецификации PrivateKeyFile должны быть сохранены. Это сэкономило бы 256 байт дискового пространства, но вероятно не стоит усилий для большинства приложений. См. предложение 161 для дополнительной информации и контекста.

DEST GENERATE не требует предварительного создания сессии.

DEST GENERATE нельзя использовать для создания назначения с оффлайн подписями.

#### PING/PONG (SAM 3.2 или выше)

Клиент или сервер может отправить:

```
PING[ arbitrary text]
```
на управляющий порт, с ответом:

```
PONG[ arbitrary text from the ping]
```
для использования в качестве поддержания активности контрольного сокета. Любая сторона может закрыть сессию и сокет, если не получен ответ в разумное время, зависящее от реализации.

Если происходит таймаут при ожидании PONG от клиента, мост может отправить:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
а затем отключиться.

Если происходит таймаут при ожидании PONG от моста, клиент может просто отключиться.

PING/PONG не требуют предварительного создания сессии.

#### QUIT/STOP/EXIT (SAM 3.2 или выше, дополнительные функции)

Команды QUIT, STOP и EXIT закроют сессию и сокет. Реализация необязательна, для удобства тестирования через telnet. Будет ли какой-либо ответ перед закрытием сокета (например, сообщение SESSION STATUS) зависит от реализации и находится за пределами данной спецификации.

QUIT/STOP/EXIT не требуют предварительного создания сессии.

#### HELP (дополнительная функция)

Серверы могут реализовать команду HELP. Реализация является необязательной, для удобства тестирования через telnet. Формат вывода и определение конца вывода зависят от реализации и выходят за рамки данной спецификации.

HELP не требует предварительного создания сессии.

#### Конфигурация авторизации (SAM 3.2 или выше, дополнительная функция)

Конфигурация авторизации с использованием команды AUTH. SAM-сервер может реализовать эти команды для обеспечения постоянного хранения учетных данных. Конфигурация аутентификации другими способами, помимо этих команд, зависит от конкретной реализации и выходит за рамки данной спецификации.

- AUTH ENABLE включает авторизацию для последующих соединений
- AUTH DISABLE отключает авторизацию для последующих соединений
- AUTH ADD USER="foo" PASSWORD="bar" добавляет пользователя/пароль
- AUTH REMOVE USER="foo" удаляет этого пользователя

Двойные кавычки для имени пользователя и пароля рекомендуются, но не обязательны. Двойная кавычка внутри имени пользователя или пароля должна быть экранирована обратной косой чертой. В случае сбоя сервер ответит с I2P_ERROR и сообщением.

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

Большинство ответов с RESULT, отличных от OK, также будут включать MESSAGE с дополнительной информацией. MESSAGE обычно будет полезно при отладке проблем. Однако строки MESSAGE зависят от реализации, могут быть или не быть переведены SAM сервером на текущую локаль, могут содержать внутреннюю информацию, специфичную для реализации, такую как исключения, и могут изменяться без уведомления. Хотя SAM клиенты могут выбрать показ строк MESSAGE пользователям, они не должны принимать программные решения на основе этих строк, поскольку это будет неустойчиво.

### Опции Tunnel, I2CP и Streaming

Эти параметры могут быть переданы как пары имя=значение в строке SAM SESSION CREATE.

Все сессии могут включать [опции I2CP, такие как длины и количества туннелей](/docs/protocol/i2cp#options). STREAM сессии могут включать [опции библиотеки Streaming](/docs/api/streaming#options).

Обратитесь к этим источникам для получения информации о названиях опций и значениях по умолчанию. Указанная документация предназначена для реализации Java router. Значения по умолчанию могут изменяться. Названия опций и их значения чувствительны к регистру. Другие реализации router могут не поддерживать все опции и иметь другие значения по умолчанию; подробности смотрите в документации конкретного router.

### Заметки по BASE 64

Кодирование Base 64 должно использовать стандартный алфавит Base 64 для I2P "A-Z, a-z, 0-9, -, ~".

### Настройка SAM по умолчанию

Порт SAM по умолчанию — 7656. SAM не включен по умолчанию в Java I2P Router; он должен быть запущен вручную или настроен на автоматический запуск на странице настройки клиентов в консоли router или в файле clients.config. Порт SAM UDP по умолчанию — 7655, прослушивает на 127.0.0.1. Эти параметры могут быть изменены в Java router путем добавления аргументов sam.udp.port=nnnnn и/или sam.udp.host=w.x.y.z при вызове или в строке SESSION.

Конфигурация в других router реализациях зависит от конкретной реализации. См. [руководство по конфигурации i2pd здесь](https://i2pd.readthedocs.io/en/latest/user-guide/configuration/).
