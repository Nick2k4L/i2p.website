---
title: "UDP трекеры"
description: "Спецификация протокола для UDP BitTorrent анонсов в I2P"
slug: "udp-announces"
aliases:
  - "/ru/docs/specs/udp-bittorrent-announces"
  - "/ru/docs/specs/udp-bittorrent-announces/"
category: "Протоколы"
lastUpdated: "2025-06"
accurateFor: "0.9.67"
---

## Обзор

Данная спецификация документирует протокол для UDP объявлений bittorrent в I2P. Для общей спецификации bittorrent в I2P см. [BitTorrent over I2P](/docs/applications/bittorrent). Для справочной информации и дополнительных сведений о разработке данной спецификации см. [Proposal 160](/proposals/160-udp-trackers).

## Дизайн

Это предложение использует repliable datagram2, repliable datagram3 и raw datagrams, как определено в [Datagrams](/docs/specs/datagrams). Datagram2 и Datagram3 — это новые варианты repliable datagrams, определённые в [Предложении 163](/proposals/163-datagram2-datagram3). Datagram2 добавляет защиту от повторного воспроизведения и поддержку автономных подписей. Datagram3 меньше старого формата datagram, но без аутентификации.

### BEP 15

Для справки, поток сообщений, определенный в [BEP 15](http://www.bittorrent.org/beps/bep_0015.html), выглядит следующим образом:

```
Client                        Tracker
    Connect Req. ------------->
      <-------------- Connect Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
    Announce Req. ------------->
      <-------------- Announce Resp.
```
Фаза подключения необходима для предотвращения подмены IP-адресов. Трекер возвращает идентификатор соединения, который клиент использует в последующих анонсах. Этот идентификатор соединения истекает по умолчанию через одну минуту на клиенте и через две минуты на трекере.

I2P будет использовать тот же поток сообщений, что и BEP 15, для упрощения внедрения в существующие кодовые базы клиентов с поддержкой UDP: для эффективности и по соображениям безопасности, обсуждаемым ниже:

```
Client                        Tracker
    Connect Req. ------------->       (Repliable Datagram2)
      <-------------- Connect Resp.   (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
    Announce Req. ------------->      (Repliable Datagram3)
      <-------------- Announce Resp.  (Raw)
             ...
```
Это потенциально обеспечивает значительную экономию пропускной способности по сравнению с потоковыми (TCP) объявлениями. Хотя Datagram2 примерно того же размера, что и потоковый SYN, необработанный ответ намного меньше потокового SYN ACK. Последующие запросы используют Datagram3, а последующие ответы являются необработанными.

Запросы announce представляют собой Datagram3, поэтому tracker не нужно поддерживать большую таблицу соответствия ID соединений с назначениями announce или хешами. Вместо этого tracker может генерировать ID соединений криптографически на основе хеша отправителя, текущей временной метки (основанной на некотором интервале) и секретного значения. Когда получается запрос announce, tracker проверяет ID соединения, а затем использует хеш отправителя Datagram3 в качестве целевого адресата для отправки.

### Время жизни соединения

[BEP 15](http://www.bittorrent.org/beps/bep_0015.html) указывает, что ID соединения истекает через одну минуту на клиенте и через две минуты на трекере. Это не настраивается. Это ограничивает потенциальные выгоды в эффективности, если только клиенты не группируют анонсы, чтобы выполнить их все в течение одноминутного окна. i2psnark в настоящее время не группирует анонсы; он распределяет их во времени, чтобы избежать всплесков трафика. Сообщается, что опытные пользователи запускают тысячи торрентов одновременно, и сжатие такого количества анонсов в одну минуту нереалистично.

Здесь мы предлагаем расширить ответ на подключение, добавив необязательное поле времени жизни соединения. По умолчанию, если не указано, это одна минута. В противном случае время жизни, указанное в секундах, должно использоваться клиентом, и трекер будет поддерживать ID соединения еще одну минуту.

### Совместимость с BEP 15

Данная архитектура максимально сохраняет совместимость с [BEP 15](http://www.bittorrent.org/beps/bep_0015.html), чтобы минимизировать изменения, необходимые в существующих клиентах и трекерах.

Единственное обязательное изменение — это формат информации о пирах в ответе announce. Добавление поля lifetime в ответе connect не является обязательным, но настоятельно рекомендуется для эффективности, как объяснено выше.

### Анализ безопасности

Важной целью протокола UDP announce является предотвращение подмены адресов. Клиент должен реально существовать и содержать настоящий leaseset. У него должны быть входящие туннели для получения Connect Response. Эти туннели могут быть нулевой длины и созданы мгновенно, но это скомпрометирует создателя. Данный протокол достигает этой цели.

### Проблемы

- Этот протокол не поддерживает скрытые назначения, но может быть расширен для этого. См. ниже.

## Спецификация

### Протоколы и порты

Repliable Datagram2 использует I2CP протокол 19; repliable Datagram3 использует I2CP протокол 20; необработанные датаграммы используют I2CP протокол 18. Запросы могут быть Datagram2 или Datagram3. Ответы всегда необработанные. Старый формат repliable datagram ("Datagram1"), использующий I2CP протокол 17, НЕ ДОЛЖЕН использоваться для запросов или ответов; они должны быть отброшены при получении на портах запроса/ответа. Обратите внимание, что протокол Datagram1 17 по-прежнему используется для DHT протокола.

Запросы используют I2CP "to port" из announce URL; см. ниже. "From port" запроса выбирается клиентом, но должен быть ненулевым и отличаться от портов, используемых DHT, чтобы ответы могли быть легко классифицированы. Трекеры должны отклонять запросы, полученные на неправильном порту.

Ответы используют "to port" из I2CP из запроса. "From port" запроса является "to port" из запроса.

### URL для объявления

Формат URL для announce не указан в [BEP 15](http://www.bittorrent.org/beps/bep_0015.html), но как и в обычной сети, UDP announce URL имеют вид `udp://host:port/path`. Путь игнорируется и может быть пустым, но обычно это `/announce` в обычной сети. Часть `:port` должна всегда присутствовать, однако, если часть `:port` опущена, используйте порт I2CP по умолчанию 6969, так как это общепринятый порт в обычной сети. Также могут быть добавлены cgi параметры `&a=b&c=d`, которые могут быть обработаны и предоставлены в запросе announce, см. [BEP 41](http://www.bittorrent.org/beps/bep_0041.html). Если нет параметров или пути, завершающий `/` также может быть опущен, как подразумевается в [BEP 41](http://www.bittorrent.org/beps/bep_0041.html).

### Форматы датаграмм

Все значения передаются в сетевом порядке байтов (big endian). Не ожидайте, что пакеты будут точно определенного размера. Будущие расширения могут увеличить размер пакетов.

#### Запрос на подключение

Клиент к трекеру. 16 байт. Должен быть repliable Datagram2. То же самое, что и в [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Без изменений.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">protocol_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0x41727101980 // magic constant</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
#### Ответ подключения

Tracker к клиенту. 16 или 18 байт. Должен быть в сыром виде. То же самое, что в [BEP 15](http://www.bittorrent.org/beps/bep_0015.html), за исключением отмеченного ниже.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // connect</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">lifetime</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // Change from BEP 15</td>
    </tr>
  </tbody>
</table>
Ответ ДОЛЖЕН быть отправлен на I2CP "to port", который был получен как "from port" запроса.

Поле lifetime является необязательным и указывает время жизни connection_id клиента в секундах. По умолчанию 60, минимальное значение при указании также 60. Максимальное значение составляет 65535 или около 18 часов. Трекер должен поддерживать connection_id на 60 секунд дольше времени жизни клиента.

#### Запрос объявления

Клиент к трекеру. Минимум 98 байт. Должна быть отвечаемая Datagram3. То же, что и в [BEP 15](http://www.bittorrent.org/beps/bep_0015.html), за исключением отмеченного ниже.

connection_id — это значение, полученное в ответе на подключение.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">connection_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">info_hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">36</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20-byte string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">peer_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">56</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">downloaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">left</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">72</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">uploaded</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">80</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">event</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // 0: none; 1: completed; 2: started; 3: stopped</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">84</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">IP address</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0 // default, unused in I2P</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">88</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">key</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">92</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">num_want</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1 // default</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">96</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">port</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// must be same as I2CP from port</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">98</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">varies</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">options</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">optional // As specified in BEP 41</td>
    </tr>
  </tbody>
</table>
Изменения по сравнению с [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- ключ игнорируется
- IP-адрес не используется
- порт вероятно игнорируется, но должен совпадать с портом I2CP from
- Секция опций, если присутствует, определяется как в [BEP 41](http://www.bittorrent.org/beps/bep_0041.html)

Ответ ДОЛЖЕН быть отправлен на I2CP "to port", который был получен как "from port" запроса. Не используйте порт из запроса announce.

#### Ответ на объявление

Tracker к клиенту. Минимум 20 байт. Должно быть в raw формате. То же самое, что в [BEP 15](http://www.bittorrent.org/beps/bep_0015.html), за исключением отмеченного ниже.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 // announce</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">interval</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">12</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">leechers</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">16</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">seeders</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">20</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32 * n 32-byte hash</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">binary hashes</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">// Change from BEP 15</td>
    </tr>
  </tbody>
</table>
Изменения по сравнению с [BEP 15](http://www.bittorrent.org/beps/bep_0015.html):

- Вместо 6-байтового IPv4+порт или 18-байтового IPv6+порт, мы возвращаем кратное 32-байтовым "компактным ответам" с двоичными SHA-256 хешами узлов. Как и в случае с TCP компактными ответами, мы не включаем порт.

Ответ ДОЛЖЕН быть отправлен на I2CP "to port", который был получен как "from port" запроса. Не используйте порт из запроса объявления.

I2P датаграммы имеют очень большой максимальный размер около 64 КБ; однако для надежной доставки следует избегать датаграмм размером больше 4 КБ. Для эффективности пропускной способности трекеры должны вероятно ограничивать максимальное количество peers примерно до 50, что соответствует пакету размером около 1600 байт до накладных расходов на различных уровнях, и должно укладываться в лимит полезной нагрузки двух tunnel сообщений после фрагментации.

Как и в BEP 15, здесь не включается счетчик количества адресов пиров (IP/порт для BEP 15, хеши здесь), которые следуют далее. Хотя это не предусмотрено в BEP 15, можно определить маркер конца пиров из всех нулей, чтобы указать, что информация о пирах завершена и далее следуют некоторые данные расширения.

Чтобы расширение было возможно в будущем, клиенты должны игнорировать 32-байтовый хеш из всех нулей и любые данные, следующие за ним. Трекеры должны отклонять анонсы с хешем из всех нулей, хотя такой хеш уже заблокирован Java router'ами.

#### Парсинг

Запрос/ответ scrape из [BEP 15](http://www.bittorrent.org/beps/bep_0015.html) не требуется данной спецификацией, но может быть реализован при желании, изменения не требуются. Клиент должен сначала получить идентификатор соединения. Запрос scrape всегда является repliable Datagram3. Ответ scrape всегда в raw формате.

#### Ответ с ошибкой

Tracker к клиенту. Минимум 8 байт (если сообщение пустое). Должен быть необработанным. То же самое, что и в [BEP 15](http://www.bittorrent.org/beps/bep_0015.html). Без изменений.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Offset</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Size</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Name</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">action</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">3 // error</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">4</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">32-bit integer</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">transaction_id</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">string</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">message</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
  </tbody>
</table>
## Расширения

Биты расширения или поле версии не включены. Клиенты и трекеры не должны предполагать, что пакеты имеют определенный размер. Таким образом, дополнительные поля могут быть добавлены без нарушения совместимости. Если требуется, рекомендуется формат расширений, определенный в [BEP 41](http://www.bittorrent.org/beps/bep_0041.html).

Ответ подключения изменен для добавления необязательного времени жизни идентификатора соединения.

Если требуется поддержка blinded destination (скрытых назначений), мы можем либо добавить blinded 35-байтовый адрес в конец запроса announce, либо запросить blinded хеши в ответах, используя формат [BEP 41](http://www.bittorrent.org/beps/bep_0041.html) (параметры будут определены позже). Набор blinded 35-байтовых адресов узлов может быть добавлен в конец ответа announce после 32-байтового хеша из нулей.

## Руководство по реализации

Смотрите раздел о дизайне выше для обсуждения проблем неинтегрированных клиентов и трекеров, не использующих I2CP.

### Клиенты

Для данного имени хоста трекера клиент должен предпочитать UDP вместо HTTP URLs и не должен объявлять себя на обоих.

Клиенты с существующей поддержкой BEP 15 должны требовать только незначительных модификаций.

Если клиент поддерживает DHT или другие протоколы датаграмм, он должен вероятно выбрать другой порт в качестве "порта отправителя" запроса, чтобы ответы приходили на этот порт и не смешивались с сообщениями DHT. Клиент получает только необработанные датаграммы в качестве ответов. Трекеры никогда не отправят repliable datagram2 клиенту.

Клиенты со списком opentrackers по умолчанию должны обновить список, добавив UDP URL после того, как станет известно, что известные opentrackers поддерживают UDP.

Клиенты могут реализовывать или не реализовывать повторную передачу запросов. Повторные передачи, если они реализованы, должны использовать начальный таймаут не менее 15 секунд и удваивать таймаут для каждой повторной передачи (экспоненциальная задержка).

Клиенты должны делать откат после получения ответа с ошибкой.

### Трекеры

Tracker'ы с существующей поддержкой BEP 15 должны требовать лишь небольших модификаций. Данная спецификация отличается от предложения 2014 года тем, что tracker должен поддерживать прием repliable datagram2 и datagram3 на том же порту.

Чтобы минимизировать требования к ресурсам tracker'а, этот протокол разработан для исключения любых требований к tracker'у хранить сопоставления хешей клиентов с идентификаторами соединений для последующей проверки. Это возможно, поскольку пакет запроса announce является отвечаемым пакетом Datagram3, поэтому он содержит хеш отправителя.

Рекомендуемая реализация:

- Определить текущую эпоху как текущее время с разрешением времени жизни соединения, `epoch = now / lifetime`.
- Определить криптографическую хеш-функцию `H(secret, clienthash, epoch)`, которая генерирует 8-байтовый выход.
- Сгенерировать случайную константу secret, используемую для всех соединений.
- Для ответов на подключение генерировать `connection_id = H(secret, clienthash, epoch)`
- Для запросов announce валидировать полученный connection ID в текущей эпохе путем проверки `connection_id == H(secret, clienthash, epoch) || connection_id == H(secret, clienthash, epoch - 1)`

## Справочные материалы

- **[BEP15]** [BEP 15 - Протокол UDP Tracker](http://www.bittorrent.org/beps/bep_0015.html)
- **[BEP41]** [BEP 41 - Расширения протокола UDP Tracker](http://www.bittorrent.org/beps/bep_0041.html)
- **[DATAGRAMS]** [Спецификация датаграмм](/docs/specs/datagrams)
- **[Prop160]** [Предложение 160 - UDP Tracker'ы](/proposals/160-udp-trackers)
- **[Prop163]** [Предложение 163 - Datagram2/Datagram3](/proposals/163-datagram2-datagram3)
- **[SAMv3]** [SAM v3 API](/docs/api/samv3)
- **[SPEC]** [BitTorrent поверх I2P](/docs/applications/bittorrent)
