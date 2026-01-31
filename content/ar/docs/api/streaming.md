---
title: "بروتوكول البث المباشر"
description: "نقل يشبه TCP يستخدم من قبل معظم تطبيقات I2P"
slug: "streaming"
lastUpdated: "2025-07"
accurateFor: "0.9.67"
---

## نظرة عامة {#overview}

مكتبة streaming هي تقنياً جزء من طبقة "التطبيق"، حيث أنها ليست وظيفة أساسية في router. ولكن في الممارسة العملية، تقدم وظيفة حيوية لجميع تطبيقات I2P الموجودة تقريباً، من خلال توفير تدفقات شبيهة بـ TCP عبر I2P، والسماح للتطبيقات الموجودة بأن يتم نقلها بسهولة إلى I2P. مكتبة النقل الأخرى من النهاية إلى النهاية لاتصال العميل هي [مكتبة datagram](/docs/specs/datagrams).

مكتبة streaming هي طبقة فوق [I2CP API](/docs/specs/i2cp) الأساسية التي تسمح بتدفقات موثوقة ومرتبة ومصادق عليها من الرسائل للعمل عبر طبقة رسائل غير موثوقة وغير مرتبة وغير مصادق عليها. تماماً مثل العلاقة بين TCP و IP، تحتوي هذه الوظيفة للـ streaming على سلسلة كاملة من المقايضات والتحسينات المتاحة، ولكن بدلاً من تضمين هذه الوظيفة في كود I2P الأساسي، تم فصلها إلى مكتبتها الخاصة سواء للحفاظ على تعقيدات TCP منفصلة أو للسماح بتطبيقات محسّنة بديلة.

نظراً للتكلفة المرتفعة نسبياً للرسائل، تم تحسين بروتوكول مكتبة streaming لجدولة وتسليم تلك الرسائل للسماح للرسائل الفردية المرسلة بأن تحتوي على أكبر قدر ممكن من المعلومات المتاحة. على سبيل المثال، يمكن إكمال معاملة HTTP صغيرة تم توصيلها عبر مكتبة streaming في رحلة واحدة فقط - الرسائل الأولى تجمع SYN و FIN وحمولة طلب HTTP الصغيرة، والرد يجمع SYN و FIN و ACK وحمولة استجابة HTTP. بينما يجب إرسال ACK إضافية لإخبار خادم HTTP أنه تم استلام SYN/FIN/ACK، يمكن لوكيل HTTP المحلي غالباً تسليم الاستجابة الكاملة إلى المتصفح فوراً.

تتشابه مكتبة streaming إلى حد كبير مع تجريد لبروتوكول TCP، مع نوافذها المنزلقة، وخوارزميات التحكم في الازدحام (كل من البدء البطيء وتجنب الازدحام)، والسلوك العام للحزم (ACK، SYN، FIN، RST، حساب rto، إلخ).

مكتبة streaming هي مكتبة قوية محسّنة للعمل عبر I2P. تحتوي على إعداد من مرحلة واحدة، وتتضمن تنفيذاً كاملاً للنوافذ.

## API {#api}

توفر واجهة برمجة التطبيقات لمكتبة التدفق نموذجاً قياسياً للمقابس لتطبيقات Java. واجهة برمجة التطبيقات [I2CP](/docs/specs/i2cp) منخفضة المستوى مخفية تماماً، باستثناء أن التطبيقات قد تمرر [معاملات I2CP](/docs/specs/i2cp#options) من خلال مكتبة التدفق، ليتم تفسيرها بواسطة I2CP.

الواجهة المعيارية لمكتبة streaming هي أن يستخدم التطبيق I2PSocketManagerFactory لإنشاء I2PSocketManager. يطلب التطبيق بعدها من مدير المقابس I2PSession، مما سيؤدي إلى الاتصال بالـ router عبر [I2CP](/docs/specs/i2cp). يمكن للتطبيق بعد ذلك إعداد الاتصالات باستخدام I2PSocket أو استقبال الاتصالات باستخدام I2PServerSocket.

للحصول على مثال جيد للاستخدام، راجع كود i2psnark.

### الخيارات والقيم الافتراضية {#options}

الخيارات والقيم الافتراضية الحالية مدرجة أدناه. الخيارات حساسة لحالة الأحرف ويمكن تعيينها للـ router بأكمله، أو لعميل معين، أو لـ socket فردي على أساس كل اتصال. العديد من القيم مضبوطة لأداء HTTP في ظروف I2P النموذجية. التطبيقات الأخرى مثل خدمات الند للند مشجعة بقوة على التعديل حسب الضرورة، عن طريق تعيين الخيارات وتمريرها عبر الاستدعاء إلى I2PSocketManagerFactory.createManager(_i2cpHost, _i2cpPort, opts). قيم الوقت بالميلي ثانية.

لاحظ أن واجهات برمجة التطبيقات عالية المستوى، مثل [SAM](/docs/api/samv3) و [BOB](/docs/legacy/bob) و [I2PTunnel](/docs/api/i2ptunnel)، قد تتجاوز هذه الإعدادات الافتراضية بإعداداتها الافتراضية الخاصة. لاحظ أيضاً أن العديد من الخيارات تنطبق فقط على الخوادم التي تستمع للاتصالات الواردة.

اعتبارًا من الإصدار 0.9.1، يمكن تغيير معظم الخيارات، ولكن ليس جميعها، على socket manager أو جلسة نشطة. راجع javadocs للحصول على التفاصيل.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Default</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.accessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes used for either access list or blacklist. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.destination.sigType</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The name or number of the signature type for a transient destination. As of release 0.9.12.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableAccessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a whitelist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableBlackList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a blacklist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.answerPings</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to respond to incoming pings</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.blacklist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes to be blacklisted for incoming connections to ALL destinations in the context. This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.3.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.bufferSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64K</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How much transmit data (in bytes) will be accepted that hasn't been written out yet.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.congestionAvoidanceGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in congestion avoidance, we grow the window size at the rate of <code>1/(windowSize*factor)</code>. In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to wait after instantiating a new con before actually attempting to connect. If this is &lt;= 0, connect immediately with no initial data. If greater than 0, wait until the output stream is flushed, the buffer fills, or that many milliseconds pass, and include any initial data with the SYN.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5*60*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on connect, in milliseconds. Negative means indefinitely. Default is 5 minutes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.disableRejectLogging</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to disable warnings in the logs when an incoming connection is rejected due to connection limits. As of release 0.9.4.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.dsalist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes or host names to be contacted using an alternate DSA destination. Only applies if multisession is enabled and the primary session is non-DSA (generally for shared clients only). This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.21.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.enforceProtocol</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to listen only for the streaming protocol. Setting to true will prohibit communication with Destinations earlier than release 0.7.1 (released March 2009). Set to true if running multiple protocols on this Destination. As of release 0.9.1. Default true as of release 0.9.36.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 (send)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0=noop, 1=disconnect) What to do on an inactivity timeout - do nothing, disconnect, or send a duplicate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">90*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Idle time before sending a keepalive</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialAckDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">750</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Delay before sending an ack</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialResendDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The initial value of the resend delay field in the packet header, times 1000. Not fully implemented; see below.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial timeout (if no <a href="#sharing">sharing data</a> available). As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial round trip time estimate (if no <a href="#sharing">sharing data</a> available). Disabled as of release 0.9.8; uses actual RTT.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(if no <a href="#sharing">sharing data</a> available) In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.limitAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reset</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">What action to take when an incoming connection exceeds limits. Valid values are: reset (reset the connection); drop (drop the connection); or http (send a hardcoded HTTP 429 response). Any other value is a custom response to be sent. backslash-r and backslash-n will be replaced with CR and LF. As of release 0.9.34.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConcurrentStreams</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0 or negative value means unlimited) This is a total limit for incoming and outgoing combined.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxMessageSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1730</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum size of the payload, i.e. the MTU in bytes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxResends</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Maximum number of retransmissions before failure.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (all peers; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.profile</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 (bulk)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1=bulk; 2=interactive; see important notes <a href="#profile">below</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.readTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on read, in milliseconds. Negative means indefinitely.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.slowStartGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in slow start, we grow the window size at the rate of 1/(factor). In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttdevDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.wdwDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.writeTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on write/flush, in milliseconds. Negative means indefinitely.</td>
    </tr>
  </tbody>
</table>
## مواصفات البروتوكول {#spec}

[انظر صفحة مواصفات مكتبة التدفق.](/docs/specs/streaming)

## تفاصيل التنفيذ {#implementation}

### الإعداد {#setup}

يرسل المُبادِر حزمة بيانات مع تعيين علامة SYNCHRONIZE. قد تحتوي هذه الحزمة على البيانات الأولية أيضاً. يرد النظير بحزمة بيانات مع تعيين علامة SYNCHRONIZE. قد تحتوي هذه الحزمة على بيانات الاستجابة الأولية أيضاً.

يمكن للمبادر إرسال حزم بيانات إضافية، حتى حجم النافذة الأولية، قبل تلقي استجابة SYNCHRONIZE. ستحتوي هذه الحزم أيضًا على حقل معرف Stream الإرسال مضبوط على 0. يجب على المستقبلين تخزين الحزم المستلمة مؤقتًا على streams غير معروفة لفترة قصيرة من الزمن، حيث قد تصل خارج الترتيب، قبل حزمة SYNCHRONIZE.

### اختيار وتفاوض MTU {#mtu}

يتم التفاوض على الحد الأقصى لحجم الرسالة (المسمى أيضاً MTU / MRU) إلى القيمة الأقل المدعومة من قبل النظيرين. نظراً لأن رسائل tunnel يتم حشوها إلى 1KB، فإن الاختيار السيء لـ MTU سيؤدي إلى كمية كبيرة من النفقات الإضافية. يتم تحديد MTU بواسطة الخيار i2p.streaming.maxMessageSize. تم اختيار MTU الافتراضي الحالي البالغ 1730 ليتناسب بدقة مع رسالتي I2NP tunnel بحجم 1K، بما في ذلك النفقات الإضافية للحالة النموذجية.

ملاحظة: هذا هو الحد الأقصى لحجم الحمولة فقط، لا يشمل الرأس.

ملاحظة: بالنسبة لاتصالات ECIES، والتي لديها overhead مخفض، فإن MTU الموصى به هو 1812. يبقى MTU الافتراضي 1730 لجميع الاتصالات، بغض النظر عن نوع المفتاح المستخدم. يجب على العملاء استخدام الحد الأدنى من MTU المُرسل والمُستقبل، كالمعتاد. انظر الاقتراح 155.

الرسالة الأولى في الاتصال تتضمن 387 بايت (نموذجية) Destination مضافة بواسطة طبقة التدفق، وعادة 898 بايت (نموذجية) LeaseSet، ومفاتيح الجلسة، مجمعة في رسالة Garlic بواسطة الموجه. (لن يتم تجميع LeaseSet ومفاتيح الجلسة إذا تم إنشاء جلسة ElGamal مسبقاً). لذلك، فإن هدف ملاءمة طلب HTTP كامل في رسالة I2NP واحدة بحجم 1KB ليس قابلاً للتحقيق دائماً. ومع ذلك، فإن اختيار MTU، جنباً إلى جنب مع التنفيذ الدقيق لاستراتيجيات التجزئة والتجميع في معالج بوابة tunnel، هي عوامل مهمة في عرض النطاق الترددي للشبكة، والكمون، والموثوقية، والكفاءة، خاصة للاتصالات طويلة المدى.

### سلامة البيانات {#integrity}

يتم ضمان تكامل البيانات من خلال مجموع التحقق gzip CRC-32 المطبق في [طبقة I2CP](/docs/specs/i2cp#format). لا يوجد حقل مجموع تحقق في بروتوكول التدفق.

### تغليف الحزم {#encapsulation}

يتم إرسال كل حزمة عبر I2P كرسالة واحدة (أو كفص منفرد في [رسالة Garlic](/docs/overview/garlic-routing)). يتم تنفيذ تغليف الرسائل في طبقات [I2CP](/docs/specs/i2cp) و [I2NP](/docs/specs/i2np) و [رسالة tunnel](/docs/specs/tunnel-message) الأساسية. لا توجد آلية فاصل حزم أو حقل طول البيانات النافعة في بروتوكول البث المتدفق.

### التأخير الاختياري {#delay}

قد تتضمن حزم البيانات حقل تأخير اختياري يحدد التأخير المطلوب، بالملي ثانية، قبل أن يقوم المستقبل بإرسال إقرار الاستلام للحزمة. القيم الصالحة هي من 0 إلى 60000 شاملة. قيمة 0 تطلب إقرار استلام فوري. هذا استشاري فقط، ويجب على المستقبلات التأخير قليلاً حتى يمكن إقرار حزم إضافية بإقرار استلام واحد. قد تتضمن بعض التطبيقات قيمة استشارية من (RTT المقاس / 2) في هذا الحقل. لقيم التأخير الاختياري غير الصفرية، يجب على المستقبلات تحديد الحد الأقصى للتأخير قبل إرسال إقرار الاستلام إلى بضع ثوانٍ كحد أقصى. قيم التأخير الاختياري الأكبر من 60000 تشير إلى الاختناق، انظر أدناه.

### نوافذ الإرسال/الاستقبال والاختناق {#windows}

تتضمن رؤوس TCP نافذة الاستقبال بالبايتات؛ ومع ذلك، فإن بروتوكول البث المباشر لا يوفر طريقة لتبادل الحد الأقصى لحجم نافذة الاستقبال سواء بالبايتات أو الحزم. يوجد فقط مؤشر بسيط للحجب/إلغاء الحجب يشير إلى أن مخزن الاستقبال ممتلئ. يجب على كل نقطة نهاية الحفاظ على تقديرها الخاص لنافذة استقبال الطرف البعيد، سواء بالبايتات أو الحزم. لاحظ أن مخزن الاستقبال قد يفيض عند أي حجم نافذة إذا كان تطبيق العميل بطيئاً في إفراغ المخزن.

الحد الأقصى الافتراضي لحجم نافذة الإرسال والاستقبال في تنفيذ Java هو 128 حزمة. التنفيذات التي تضع حداً أقصى لحجم نافذة الإرسال أعلى من 128 يجب أن تأخذ في الاعتبار القضايا التالية:

- استجابات CHOKE من Java routers بسبب فيض buffer الاستقبال أكثر احتمالاً بكثير.
- يجب تنفيذ تقدير حجم buffer المستقبِل البعيد لتخفيف الفيضانات المتكررة (انظر أعلاه)
- يجب التعامل مع CHOKE بشكل صحيح (انظر أدناه)
- أحجام النوافذ القصوى التي تزيد عن 256 أكثر عرضة للأخطاء، لأن طول حقل خيار عدد nack هو بايت واحد، مما يحد من الحد الأقصى لـ NACKs إلى 255. هذه المواصفة لا تتناول ما يجب فعله إذا كان هناك أكثر من 255 NACK. أحجام النوافذ القصوى التي تزيد عن 256 غير مُوصى بها.

الحد الأدنى المُوصى به لحجم المخزن المؤقت لتنفيذ المستقبل هو 128 حزمة أو 232 كيلوبايت (تقريباً 128 * 1812). بسبب زمن الاستجابة لشبكة I2P وفقدان الحزم والتحكم في الازدحام الناتج عن ذلك، نادراً ما يمتلئ مخزن مؤقت بهذا الحجم. ومع ذلك، فإن الفيض أكثر احتمالاً للحدوث في اتصالات "local loopback" عالية النطاق الترددي (نفس الـ router) أو في الاختبار المحلي.

للإشارة السريعة والتعافي السلس من حالات الفيض، هناك آلية بسيطة للضغط العكسي في بروتوكول البث. إذا تم استلام حزمة تحتوي على حقل تأخير اختياري بقيمة 60001 أو أعلى، فهذا يشير إلى "الخنق" أو نافذة استقبال بقيمة صفر. الحزمة التي تحتوي على حقل تأخير اختياري بقيمة 60000 أو أقل تشير إلى "إلغاء الخنق". الحزم التي لا تحتوي على حقل تأخير اختياري لا تؤثر على حالة الخنق/إلغاء الخنق.

بعد التعرض للخنق، لا ينبغي إرسال المزيد من الحزم التي تحتوي على بيانات حتى يتم إلغاء خنق المرسل، باستثناء حزم البيانات "الاستطلاعية" العرضية للتعويض عن حزم إلغاء الخنق المفقودة المحتملة. يجب على النقطة النهائية المخنوقة بدء "مؤقت الاستمرار" للتحكم في الاستطلاع، كما في TCP. يجب على النقطة النهائية التي تلغي الخنق إرسال عدة حزم مع تعيين هذا الحقل، أو الاستمرار في إرسالها بشكل دوري حتى يتم استقبال حزم البيانات مرة أخرى. الحد الأقصى لوقت الانتظار لإلغاء الخنق يعتمد على التطبيق. حجم نافذة المرسل واستراتيجية التحكم في الازدحام بعد إلغاء الخنق يعتمد على التطبيق.

### التحكم في الازدحام {#congestion}

تستخدم مكتبة التدفق مرحلتي البدء البطيء القياسي (النمو الأسي للنافذة) وتجنب الازدحام (النمو الخطي للنافذة)، مع التراجع الأسي. النوافذ والإقرارات تستخدم عدد الحزم وليس عدد البايتات.

### إغلاق {#close}

أي حزمة، بما في ذلك تلك التي تحتوي على علامة SYNCHRONIZE، قد تحتوي أيضاً على علامة CLOSE. لا يتم إغلاق الاتصال حتى يستجيب النظير بعلامة CLOSE. قد تحتوي حزم CLOSE على بيانات أيضاً.

### Ping / Pong {#ping}

لا توجد وظيفة ping في طبقة I2CP (المعادلة لـ ICMP echo) أو في datagrams. هذه الوظيفة متوفرة في streaming. لا يمكن دمج pings و pongs مع حزمة streaming عادية؛ إذا تم تعيين خيار ECHO، فسيتم تجاهل معظم العلامات والخيارات الأخرى مثل ackThrough و sequenceNum و NACKs وغيرها.

يجب أن تحتوي حزمة ping على العلامات ECHO و SIGNATURE_INCLUDED و FROM_INCLUDED مضبوطة. يجب أن يكون sendStreamId أكبر من الصفر، ويتم تجاهل receiveStreamId. قد يتطابق sendStreamId مع اتصال موجود أو لا يتطابق معه.

يجب أن تحتوي حزمة pong على تعيين علامة ECHO. يجب أن يكون sendStreamId صفراً، وreceiveStreamId هو sendStreamId من ping. قبل الإصدار 0.9.18، لا تتضمن حزمة pong أي حمولة كانت موجودة في ping.

اعتباراً من الإصدار 0.9.18، قد تحتوي رسائل ping و pong على حمولة بيانات. الحمولة في رسالة ping، حتى حد أقصى 32 بايت، يتم إرجاعها في رسالة pong.

يمكن تكوين Streaming لتعطيل إرسال pongs باستخدام التكوين i2p.streaming.answerPings=false.

### ملاحظات i2p.streaming.profile {#profile}

يدعم هذا الخيار قيمتين؛ 1=bulk و 2=interactive. يوفر الخيار تلميحاً لمكتبة التدفق و/أو الـ router حول نمط حركة البيانات المتوقع.

"Bulk" يعني التحسين لعرض النطاق الترددي العالي، ربما على حساب زمن الاستجابة. هذا هو الإعداد الافتراضي. "Interactive" يعني التحسين لزمن استجابة منخفض، ربما على حساب عرض النطاق الترددي أو الكفاءة. استراتيجيات التحسين، إن وجدت، تعتمد على التنفيذ، وقد تشمل تغييرات خارج بروتوكول التدفق.

حتى إصدار API 0.9.63، كان Java I2P يُرجع خطأ لأي قيمة غير 1 (bulk) وكان tunnel يفشل في البدء. اعتباراً من API 0.9.64، يتجاهل Java I2P القيمة. حتى إصدار API 0.9.63، كان i2pd يتجاهل هذا الخيار؛ تم تنفيذه في i2pd اعتباراً من API 0.9.64.

بينما يتضمن بروتوكول التدفق حقل علم لتمرير إعداد الملف الشخصي إلى الطرف الآخر، إلا أن هذا غير مُنفَّذ في أي router معروف.

### مشاركة كتلة التحكم {#sharing}

تدعم مكتبة التدفق مشاركة "TCP" Control Block. هذا يشارك ثلاثة معاملات مهمة لمكتبة التدفق (حجم النافذة، وقت الرحلة ذهاباً وإياباً، تباين وقت الرحلة ذهاباً وإياباً) عبر الاتصالات مع نفس النظير البعيد. يتم استخدام هذا للمشاركة "الزمنية" في وقت فتح/إغلاق الاتصال، وليس المشاركة "الجماعية" أثناء الاتصال (انظر [RFC 2140](http://www.ietf.org/rfc/rfc2140.txt)). هناك مشاركة منفصلة لكل ConnectionManager (أي لكل وجهة محلية) بحيث لا يحدث تسرب للمعلومات إلى وجهات أخرى على نفس router. تنتهي صلاحية بيانات المشاركة لنظير معين بعد بضع دقائق. يمكن تعيين معاملات مشاركة Control Block التالية لكل router:

- RTT_DAMPENING = 0.75
- RTTDEV_DAMPENING = 0.75
- WINDOW_DAMPENING = 0.75

### معاملات أخرى {#other}

المعاملات التالية هي القيم الافتراضية الموصى بها. قد تختلف القيم الافتراضية حسب التنفيذ:

- MIN_RESEND_DELAY = 100 ms (أدنى RTO)
- MAX_RESEND_DELAY = 45 sec (أقصى RTO)
- MIN_WINDOW_SIZE = 1
- MAX_WINDOW_SIZE = 128
- TREND_COUNT = 3
- MIN_MESSAGE_SIZE = 512 (أدنى MTU)
- INBOUND_BUFFER_SIZE = maxMessageSize * (maxWindowSize + 2)
- INITIAL_TIMEOUT (صالح فقط قبل أخذ عينة RTT) = 9 sec
- "alpha" (عامل التخميد RTT حسب RFC 6298) = 0.125
- "beta" (عامل التخميد RTTDEV حسب RFC 6298) = 0.25
- "K" (مضاعف RTDEV حسب RFC 6298) = 4
- PASSIVE_FLUSH_DELAY = 175 ms
- أقصى تقدير RTT: 60 sec

### التاريخ {#history}

نمت مكتبة streaming بشكل عضوي لـ I2P - أولاً قام mihi بتنفيذ "مكتبة streaming المصغرة" كجزء من I2PTunnel، والتي كانت محدودة بحجم نافذة من رسالة واحدة (تتطلب ACK قبل إرسال الرسالة التالية)، ثم تم إعادة هيكلتها إلى واجهة streaming عامة (تحاكي TCP sockets) وتم نشر تنفيذ streaming الكامل مع بروتوكول النافذة المنزلقة والتحسينات لأخذ منتج عرض النطاق الترددي العالي x التأخير في الاعتبار. يمكن للتدفقات الفردية تعديل الحد الأقصى لحجم الحزمة والخيارات الأخرى. يتم اختيار حجم الرسالة الافتراضي ليناسب بدقة رسالتين من رسائل I2NP tunnel بحجم 1K، وهو مقايضة معقولة بين تكاليف عرض النطاق الترددي لإعادة إرسال الرسائل المفقودة، وزمن الاستجابة والنفقات العامة للرسائل المتعددة.

## العمل المستقبلي {#future}

يؤثر سلوك مكتبة التدفق (streaming library) بشكل عميق على الأداء على مستوى التطبيق، وبالتالي فهي مجال مهم للتحليل الإضافي.

- قد يكون من الضروري إجراء ضبط إضافي لمعاملات مكتبة streaming lib.
- مجال آخر للبحث هو تفاعل مكتبة streaming lib مع طبقات النقل NTCP و SSU. راجع [صفحة مناقشة NTCP](/docs/historical/ntcp-discussion) للتفاصيل.
- تفاعل خوارزميات التوجيه مع مكتبة streaming lib يؤثر بقوة على الأداء. على وجه الخصوص، التوزيع العشوائي للرسائل إلى عدة tunnels في مجموعة واحدة يؤدي إلى درجة عالية من التسليم غير المرتب مما ينتج عنه أحجام نوافذ أصغر مما سيكون عليه الحال في غير ذلك. يقوم الـ router حالياً بتوجيه الرسائل لزوج وجهة واحد من/إلى عبر مجموعة ثابتة من tunnels، حتى انتهاء صلاحية tunnel أو فشل التسليم. يجب مراجعة خوارزميات فشل الـ router واختيار tunnel للتحسينات المحتملة.
- قد تتجاوز البيانات في أول حزمة SYN حجم MTU الخاص بالمستقبل.
- يمكن استخدام حقل DELAY_REQUESTED أكثر.
- حزم SYNCHRONIZE الأولية المكررة في streams قصيرة المدى قد لا يتم التعرف عليها وإزالتها.
- لا ترسل MTU في إعادة الإرسال.
- يتم إرسال البيانات إلا إذا كانت النافذة الصادرة ممتلئة. (أي no-Nagle أو TCP_NODELAY) ربما يجب أن يكون هناك خيار تكوين لهذا.
- أضاف zzz كود تصحيح أخطاء إلى مكتبة streaming لتسجيل الحزم بتنسيق متوافق مع wireshark (pcap)؛ استخدم هذا لتحليل الأداء أكثر. قد يتطلب التنسيق تحسيناً لربط المزيد من معاملات streaming lib بحقول TCP.
- هناك مقترحات لاستبدال مكتبة streaming lib بـ TCP قياسي (أو ربما طبقة فارغة مع raw sockets). هذا للأسف سيكون غير متوافق مع مكتبة streaming lib ولكن سيكون من الجيد مقارنة أداء الاثنين.
