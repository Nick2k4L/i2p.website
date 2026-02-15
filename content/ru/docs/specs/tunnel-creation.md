---
title: "Спецификация создания tunnel"
description: "Спецификация построения туннелей ElGamal для создания туннелей с использованием неинтерактивного телескопирования."
slug: "tunnel-creation"
aliases: 
category: "Дизайн"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
---

## Обзор

ПРИМЕЧАНИЕ: УСТАРЕЛО - Это спецификация создания туннелей ElGamal. См. [tunnel-creation-ecies](/docs/specs/tunnel-creation-ecies/) для спецификации создания туннелей X25519.

Этот документ определяет детали зашифрованных сообщений построения tunnel, используемых для создания tunnel с помощью метода "неинтерактивного телескопирования". См. документ по построению tunnel [TUNNEL-IMPL](/docs/specs/tunnel-implementation/) для обзора процесса, включая методы выбора и упорядочивания узлов.

Создание tunnel выполняется с помощью одного сообщения, передаваемого по пути узлов в tunnel, переписываемого на месте и отправляемого обратно создателю tunnel. Это единое сообщение tunnel состоит из переменного количества записей (до 8) - по одной для каждого потенциального узла в tunnel. Отдельные записи асимметрично шифруются (ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal)) для чтения только определенным узлом на пути, в то время как дополнительный симметричный уровень шифрования (AES [CRYPTO-AES](/docs/specs/cryptography/#aes)) добавляется на каждом переходе, чтобы раскрыть асимметрично зашифрованную запись только в подходящий момент.

### Количество записей

Не все записи должны содержать действительные данные. Сообщение построения для 3-хопового tunnel, например, может содержать больше записей для сокрытия фактической длины tunnel от участников. Существует два типа сообщений построения. Оригинальное Tunnel Build Message ([TBM](/docs/specs/i2np/#struct-TunnelBuild)) содержит 8 записей, что более чем достаточно для любой практической длины tunnel. Более новое Variable Tunnel Build Message ([VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild)) содержит от 1 до 8 записей. Инициатор может балансировать между размером сообщения и желаемой степенью маскировки длины tunnel.

В текущей сети большинство tunnel имеют длину 2 или 3 хопа. Текущая реализация использует 5-записный VTBM для построения tunnel длиной 4 хопа или меньше, и 8-записный TBM для более длинных tunnel. 5-записный VTBM (который при фрагментации помещается в три 1КБ tunnel сообщения) снижает сетевой трафик и увеличивает успешность построения, поскольку меньшие сообщения с меньшей вероятностью отбрасываются.

Ответное сообщение должно быть того же типа и длины, что и сообщение сборки.

### Спецификация записи запроса

Также указано в спецификации I2NP [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

Открытый текст записи, видимый только хопу, к которому обращаются:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-3</td><td style="border:1px solid var(--color-border); padding:0.6rem;">tunnel ID to receive messages as, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">4-35</td><td style="border:1px solid var(--color-border); padding:0.6rem;">local router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">36-39</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next tunnel ID, nonzero</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">40-71</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next router identity hash</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">72-103</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel layer key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">104-135</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 tunnel IV key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">136-167</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply key</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">168-183</td><td style="border:1px solid var(--color-border); padding:0.6rem;">AES-256 reply IV</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">184</td><td style="border:1px solid var(--color-border); padding:0.6rem;">flags</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">185-188</td><td style="border:1px solid var(--color-border); padding:0.6rem;">request time (in hours since the epoch, rounded down)</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">189-192</td><td style="border:1px solid var(--color-border); padding:0.6rem;">next message ID</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">193-221</td><td style="border:1px solid var(--color-border); padding:0.6rem;">uninterpreted / random padding</td></tr>
</tbody>
</table>
Поля ID следующего туннеля и хэша идентичности следующего router используются для указания следующего перехода в tunnel, хотя для конечной точки исходящего tunnel они указывают, куда должно быть отправлено переписанное сообщение ответа на создание tunnel. Кроме того, ID следующего сообщения указывает ID сообщения, который должно использовать сообщение (или ответ).

Ключ слоя tunnel, ключ IV tunnel, ключ ответа и IV ответа — это случайные 32-байтные значения, генерируемые создателем, для использования только в данной записи запроса построения.

Поле флагов содержит следующее (порядок битов: 76543210, бит 7 является старшим разрядом):

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bit</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Description</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">7</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages from anyone</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">6</td><td style="border:1px solid var(--color-border); padding:0.6rem;">if set, allow messages to anyone, and send the reply to the specified next hop in a Tunnel Build Reply Message</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">5-0</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Undefined, must set to 0 for compatibility with future options</td></tr>
</tbody>
</table>
Бит 7 указывает, что узел будет входящим шлюзом (IBGW). Бит 6 указывает, что узел будет исходящей конечной точкой (OBEP). Если ни один из битов не установлен, узел будет промежуточным участником. Оба бита не могут быть установлены одновременно.

#### Создание записи запроса

Каждый hop получает случайный Tunnel ID, отличный от нуля. Заполняются Tunnel ID текущего и следующего hop. Каждая запись получает случайный tunnel IV ключ, reply IV, layer ключ и reply ключ.

#### Шифрование записи запроса

Эта запись открытого текста шифруется ElGamal 2048 [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) с использованием публичного ключа шифрования узла и форматируется в 528-байтовую запись:

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-15</td><td style="border:1px solid var(--color-border); padding:0.6rem;">First 16 bytes of the SHA-256 of the current hop's router identity</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">16-527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">ElGamal-2048 encrypted request record</td></tr>
</tbody>
</table>
В 512-байтовой зашифрованной записи данные ElGamal содержат байты 1-256 и 258-513 из 514-байтового зашифрованного блока ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). Два байта заполнения из блока (нулевые байты в позициях 0 и 257) удаляются.

Поскольку открытый текст использует всё поле целиком, нет необходимости в дополнительном заполнении сверх `SHA256(cleartext) + cleartext`.

Каждая 528-байтовая запись затем итеративно шифруется (используя AES дешифрование с ключом ответа и IV ответа для каждого hop), так что идентичность router будет в открытом тексте только для соответствующего hop.

### Обработка и шифрование hop'ов

Когда узел получает TunnelBuildMessage, он просматривает содержащиеся в нем записи в поисках той, которая начинается с его собственного хеша идентификации (сокращенного до 16 байт). Затем он расшифровывает блок ElGamal из этой записи и извлекает защищенный открытый текст. На этом этапе он убеждается, что запрос tunnel не является дубликатом, подавая ключ ответа AES-256 в фильтр Блума. Дубликаты или недействительные запросы отбрасываются. Записи, которые не помечены текущим часом или предыдущим часом, если время незадолго после начала часа, должны быть отброшены. Например, возьмите час из временной метки, преобразуйте в полное время, затем если оно отстает более чем на 65 минут или опережает на 5 минут текущее время, оно недействительно. Фильтр Блума должен иметь продолжительность не менее одного часа (плюс несколько минут, чтобы учесть расхождение часов), чтобы дублированные записи в текущем часе, которые не отклоняются при проверке временной метки часа в записи, были отклонены фильтром.

После принятия решения о том, согласятся ли они участвовать в tunnel или нет, они заменяют запись, которая содержала запрос, зашифрованным блоком ответа. Все остальные записи шифруются AES-256 [CRYPTO-AES](/docs/specs/cryptography/#aes) с включенным ключом ответа и IV. Каждая запись шифруется AES/CBC отдельно с одним и тем же ключом ответа и IV ответа. Режим CBC не продолжается (не связывается) между записями.

Каждый hop знает только свой собственный ответ. Если он соглашается, он будет поддерживать tunnel до истечения срока действия, даже если он не будет использоваться, поскольку не может знать, согласились ли все остальные hop'ы.

#### Спецификация записи ответа

После того, как текущий узел прочитает свою запись, он заменяет её записью-ответом, указывающей, согласен ли он участвовать в tunnel или нет, а в случае несогласия — классифицирует причину отказа. Это просто значение размером 1 байт, где 0x0 означает согласие на участие в tunnel, а более высокие значения означают более высокие уровни отказа.

Определены следующие коды отклонения:

- TUNNEL_REJECT_PROBABALISTIC_REJECT = 10
- TUNNEL_REJECT_TRANSIENT_OVERLOAD = 20
- TUNNEL_REJECT_BANDWIDTH = 30
- TUNNEL_REJECT_CRIT = 50

Чтобы скрыть другие причины, такие как отключение router'а, от пиров, текущая реализация использует TUNNEL_REJECT_BANDWIDTH для почти всех отклонений.

Ответ зашифрован с помощью сессионного ключа AES, доставленного ему в зашифрованном блоке, дополнен 495 байтами случайных данных для достижения полного размера записи. Заполнение размещается перед байтом статуса:

`AES-256-CBC(SHA-256(padding+status) + padding + status, key, IV)`

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
<thead>
<tr>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Bytes</th>
<th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Contents</th>
</tr>
</thead>
<tbody>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">0-31</td><td style="border:1px solid var(--color-border); padding:0.6rem;">SHA-256 of bytes 32-527</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">32-526</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Random padding</td></tr>
<tr><td style="border:1px solid var(--color-border); padding:0.6rem;">527</td><td style="border:1px solid var(--color-border); padding:0.6rem;">Reply value</td></tr>
</tbody>
</table>
Это также описано в спецификации I2NP [BRR](/docs/specs/i2np/#struct-BuildRequestRecord).

### Подготовка сообщения построения tunnel

При создании нового сообщения Tunnel Build Message все записи Build Request Records должны быть сначала построены и асимметрично зашифрованы с использованием ElGamal [CRYPTO-ELG](/docs/specs/cryptography/#elgamal). Затем каждая запись упреждающе расшифровывается с помощью ключей ответа и IV узлов, находящихся ранее в пути, используя AES [CRYPTO-AES](/docs/specs/cryptography/#aes). Такое расшифрование должно выполняться в обратном порядке, чтобы асимметрично зашифрованные данные появились в открытом виде на правильном узле после того, как их предшественник их зашифрует.

Избыточные записи, не нужные для отдельных запросов, просто заполняются случайными данными создателем.

### Доставка сообщений построения tunnel

Для исходящих tunnel, доставка выполняется напрямую от создателя tunnel к первому узлу, упаковывая TunnelBuildMessage так, как если бы создатель был просто еще одним узлом в tunnel. Для входящих tunnel доставка выполняется через существующий исходящий tunnel. Исходящий tunnel обычно берется из того же пула, что и новый создаваемый tunnel. Если в этом пуле нет доступного исходящего tunnel, используется исходящий исследовательский tunnel. При запуске, когда исходящий исследовательский tunnel еще не существует, используется фальшивый исходящий tunnel с 0 узлов.

### Обработка конечной точки сообщения построения туннеля

Для создания исходящего tunnel, когда запрос достигает конечной точки исходящего tunnel (как определяется флагом 'разрешить сообщения всем'), хоп обрабатывается как обычно, шифруя ответ вместо записи и шифруя все остальные записи, но поскольку нет 'следующего хопа' для передачи TunnelBuildMessage, вместо этого он помещает зашифрованные записи ответа в TunnelBuildReplyMessage ([TBRM](/docs/specs/i2np/#struct-TunnelBuildReply)) или VariableTunnelBuildReplyMessage ([VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply)) (тип сообщения и количество записей должны соответствовать запросу) и доставляет его в tunnel ответа, указанный в записи запроса. Этот tunnel ответа пересылает Tunnel Build Reply Message обратно создателю tunnel, точно так же, как и для любого другого сообщения [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation). Создатель tunnel затем обрабатывает его, как описано ниже.

Reply tunnel был выбран создателем следующим образом: Обычно это входящий tunnel из того же пула, что и новый исходящий tunnel, который строится. Если во входящий tunnel недоступен в этом пуле, используется входящий исследовательский tunnel. При запуске, когда входящий исследовательский tunnel еще не существует, используется поддельный входящий tunnel с 0 переходов.

При создании входящего tunnel, когда запрос достигает входящей конечной точки (также известной как создатель tunnel), нет необходимости генерировать явное сообщение Tunnel Build Reply Message, и router обрабатывает каждый из ответов, как описано ниже.

### Обработка сообщения ответа на построение tunnel

Для обработки записей ответа создатель просто должен расшифровать каждую запись по отдельности с помощью AES, используя ключ ответа и IV каждого узла в tunnel после узла-получателя (в обратном порядке). Это затем раскрывает ответ, указывающий, согласны ли они участвовать в tunnel или почему они отказываются. Если все согласны, tunnel считается созданным и может использоваться немедленно, но если кто-то отказывается, tunnel отбрасывается.

Соглашения и отклонения отмечаются в профиле каждого узла [PEER-SELECTION](/docs/overview/tunnel-routing/), чтобы использоваться в будущих оценках пропускной способности tunnel узла.

## История и заметки

Эта стратегия возникла во время обсуждения в списке рассылки I2P между Майклом Роджерсом, Мэтью Тоузлендом (toad) и jrandom относительно атаки предшественника. См. TUNBUILD-SUMMARY, TUNBUILD-REASONING. Она была введена в релизе 0.6.1.10 от 2006-02-16, который стал последним разом, когда в I2P было внесено изменение, несовместимое с предыдущими версиями.

Примечания:

- Данная схема не предотвращает возможность двух враждебных peer'ов внутри tunnel'а пометить одну или несколько записей запроса или ответа для обнаружения того, что они находятся в одном tunnel'е, но это может быть обнаружено создателем tunnel'а при чтении ответа, что приведет к тому, что tunnel будет помечен как недействительный.
- Данная схема не включает в себя доказательство работы для асимметрично зашифрованной секции, хотя 16-байтовый хеш идентификатора можно было бы урезать вдвое, заменив последнюю часть функцией hashcash со стоимостью до 2^64.
- Данная схема сама по себе не предотвращает использование двумя враждебными peer'ами внутри tunnel'а временной информации для определения того, находятся ли они в одном tunnel'е. Могла бы помочь пакетная и синхронизированная доставка запросов (группировка запросов и отправка их в (синхронизированные по ntp) минуты). Однако это позволяет peer'ам "помечать" запросы, задерживая их и обнаруживая задержку позже в tunnel'е, хотя возможно отбрасывание запросов, не доставленных в небольшом временном окне, могло бы сработать (хотя для этого потребовалась бы высокая степень синхронизации часов). Альтернативно, возможно, отдельные переходы могли бы вносить случайную задержку перед пересылкой запроса?
- Существуют ли какие-либо не критичные методы пометки запроса?
- Временная метка с разрешением в один час используется для предотвращения повторных атак. Это ограничение не применялось до релиза 0.9.16.

## Будущая работа

- В текущей реализации инициатор оставляет одну запись пустой для себя. Таким образом, сообщение из n записей может построить только tunnel из n-1 переходов. Это кажется необходимым для входящих tunnel'ей (где предпоследний переход может видеть хеш-префикс для следующего перехода), но не для исходящих tunnel'ей. Это требует исследования и проверки. Если возможно использовать оставшуюся запись без ущерба для анонимности, мы должны это сделать.
- Дальнейший анализ возможных атак меткования и временных атак, описанных в приведенных выше заметках.
- Использовать только VTBM; не выбирать старые узлы, которые его не поддерживают.
- Запись Build Request Record не указывает время жизни tunnel'я или истечение; каждый переход завершает tunnel через 10 минут, что является жестко закодированной константой для всей сети. Мы могли бы использовать бит в поле флагов и взять 4 (или 8) байт из заполнения для указания времени жизни или истечения. Инициатор запроса указывал бы эту опцию только в том случае, если все участники ее поддерживают.

## Ссылки

- [BRR](/docs/specs/i2np/#struct-BuildRequestRecord) - спецификация BuildRequestRecord
- [CRYPTO-AES](/docs/specs/cryptography/#aes) - шифрование AES
- [CRYPTO-ELG](/docs/specs/cryptography/#elgamal) - шифрование ElGamal
- [HASHING-IT-OUT](http://www-users.cs.umn.edu/~hopper/hashing_it_out.pdf)
- [PEER-SELECTION](/docs/overview/tunnel-routing/)
- [PREDECESSOR](http://forensics.umass.edu/pubs/wright-tissec.pdf)
- [PREDECESSOR-2008](http://forensics.umass.edu/pubs/wright.tissec.2008.pdf)
- [TBM](/docs/specs/i2np/#struct-TunnelBuild) - TunnelBuildMessage
- [TBRM](/docs/specs/i2np/#struct-TunnelBuildReply) - TunnelBuildReplyMessage
- TUNBUILD-REASONING
- TUNBUILD-SUMMARY
- [TUNNEL-IMPL](/docs/specs/tunnel-implementation/)
- [TUNNEL-OP](/docs/specs/tunnel-implementation/#tunnel.operation)
- [VTBM](/docs/specs/i2np/#struct-VariableTunnelBuild) - VariableTunnelBuildMessage
- [VTBRM](/docs/specs/i2np/#struct-VariableTunnelBuildReply) - VariableTunnelBuildReplyMessage
