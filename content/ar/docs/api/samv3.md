---
title: "SAM V3"
description: "بروتوكول المراسلة المجهولة البسيط لتطبيقات I2P غير الجافا"
slug: "samv3"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

SAM هو بروتوكول عميل بسيط للتفاعل مع I2P. SAM هو البروتوكول الموصى به للتطبيقات غير المطورة بـ Java للاتصال بشبكة I2P، وهو مدعوم من قبل عدة تطبيقات router. يجب على تطبيقات Java استخدام streaming أو I2CP APIs مباشرة.

تم تقديم SAMv3 في إصدار I2P 0.7.3 (مايو 2009) وهو واجهة مستقرة ومدعومة. الإصدار 3.1 مستقر أيضاً ويدعم خيار نوع التوقيع، والذي يُنصح به بشدة. الإصدارات الأحدث من 3.x تدعم ميزات متقدمة. لاحظ أن i2pd لا يدعم حالياً معظم ميزات الإصدارين 3.2 و 3.3.

البدائل: [SOCKS](/docs/api/socks)، [Streaming](/docs/api/streaming)، [I2CP](/docs/protocol/i2cp)، [BOB (مُهمل)](/docs/api/bob). الإصدارات المُهملة: [SAM V1](/docs/api/sam)، [SAM V2](/docs/api/samv2).

## مكتبات SAM المعروفة

تحذير: قد تكون بعض هذه قديمة جداً أو غير مدعومة. لم يتم اختبار أو مراجعة أو صيانة أي منها من قبل مشروع I2P إلا إذا تم ذكر ذلك أدناه. قم ببحثك الخاص.

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
      <td style="border:1px solid var(--color-border); padding:0.5rem;">notabug.org/villain/mooni2p</td>
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
      <td style="border:1px solid var(--color-border); padding:0.5rem;">github.com/eyedeekay/Jsam</td>
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
      <td style="border:1px solid var(--color-border); padding:0.5rem;">notabug.org/acetone/samty</td>
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
## البدء السريع

لتنفيذ تطبيق أساسي من نظير إلى نظير يعمل بـ TCP فقط، يجب على العميل دعم الأوامر التالية:

- `HELLO VERSION MIN=3.1 MAX=3.1` - مطلوب لجميع الأوامر المتبقية
- `DEST GENERATE SIGNATURE_TYPE=7` - لإنشاء مفتاحنا الخاص والوجهة
- `NAMING LOOKUP NAME=...` - لتحويل عناوين .i2p إلى وجهات
- `SESSION CREATE STYLE=STREAM ID=... DESTINATION=... i2cp.leaseSetEncType=4,0` - مطلوب لـ STREAM CONNECT و STREAM ACCEPT
- `STREAM CONNECT ID=... DESTINATION=...` - لإجراء اتصالات صادرة
- `STREAM ACCEPT ID=...` - لقبول الاتصالات الواردة

## إرشادات عامة للمطورين

### تصميم التطبيق

جلسات SAM (أو داخل I2P، مجمعات tunnel أو مجموعات من tunnels) مصممة لتكون طويلة المدى. معظم التطبيقات ستحتاج فقط إلى جلسة واحدة، يتم إنشاؤها عند بدء التشغيل وإغلاقها عند الخروج. I2P يختلف عن Tor، حيث يمكن إنشاء وإلغاء الدوائر بسرعة. فكر بعناية واستشر مطوري I2P قبل تصميم تطبيقك لاستخدام أكثر من جلسة أو جلستين متزامنتين، أو لإنشائها وإلغائها بسرعة. معظم نماذج التهديد لن تتطلب جلسة فريدة لكل اتصال.

أيضاً، يرجى التأكد من أن إعدادات تطبيقك (والإرشادات للمستخدمين حول إعدادات router، أو إعدادات router الافتراضية إذا كنت تُضمّن router) ستؤدي إلى مساهمة مستخدميك بموارد أكثر للشبكة مما يستهلكونه. I2P هي شبكة نظير إلى نظير، ولا يمكن للشبكة البقاء إذا كان تطبيق شائع يدفع الشبكة إلى ازدحام دائم.

### التوافق والاختبار

تطبيقات router الخاصة بـ Java I2P و i2pd مستقلة ولديها اختلافات طفيفة في السلوك ودعم الميزات والإعدادات الافتراضية. يرجى اختبار تطبيقك مع أحدث إصدار من كلا الـ router.

SAM في i2pd مُفعّل افتراضياً؛ أما SAM في Java I2P فليس كذلك. قدم تعليمات لمستخدميك حول كيفية تفعيل SAM في Java I2P (عبر /configclients في وحدة تحكم router)، و/أو قدم رسالة خطأ واضحة للمستخدم في حالة فشل الاتصال الأولي، مثل "تأكد من أن I2P يعمل وأن واجهة SAM مُفعّلة".

تحتوي routers الخاصة بـ Java I2P و i2pd على قيم افتراضية مختلفة لكميات tunnel. القيمة الافتراضية لـ Java هي 2 والقيمة الافتراضية لـ i2pd هي 5. بالنسبة لمعظم حالات استخدام النطاق الترددي المنخفض إلى المتوسط وأعداد الاتصالات المنخفضة إلى المتوسطة، يكفي 2 أو 3. يرجى تحديد كمية tunnel في رسالة SESSION CREATE للحصول على أداء متسق مع routers Java I2P و i2pd. انظر أدناه.

للحصول على مزيد من الإرشادات للمطورين حول ضمان استخدام تطبيقك للموارد التي يحتاجها فقط، يرجى مراجعة [دليلنا لحزم I2P مع تطبيقك](/docs/applications/embedding).

### أنواع التوقيع والتشفير

يدعم I2P أنواع متعددة من التوقيع والتشفير. من أجل التوافق مع الإصدارات السابقة، يستخدم SAM افتراضياً أنواع قديمة وغير فعالة، لذا يجب على جميع العملاء تحديد أنواع أحدث.

يتم تحديد نوع التوقيع في أوامر DEST GENERATE و SESSION CREATE (للمؤقت). يجب على جميع العملاء تعيين `SIGNATURE_TYPE=7` (Ed25519).

يتم تحديد نوع التشفير في أمر SESSION CREATE. يُسمح بأنواع تشفير متعددة. يجب على العملاء تعيين إما `i2cp.leaseSetEncType=4` (لـ ECIES-X25519 فقط) أو `i2cp.leaseSetEncType=4,0` (لـ ECIES-X25519 و ElGamal، إذا كانت التوافقية مطلوبة).

## تغييرات الإصدار 3

### تغييرات الإصدار 3.0

تم تقديم الإصدار 3.0 في إصدار I2P 0.7.3. وفر SAMv2 طريقة لإدارة عدة مقابس على نفس وجهة I2P *بالتوازي*، أي أن العميل لا يضطر إلى انتظار إرسال البيانات بنجاح على مقبس واحد قبل إرسال البيانات على مقبس آخر. لكن جميع البيانات مرت عبر نفس مقبس العميل إلى SAM، مما كان معقداً جداً للعميل في الإدارة.

يدير SAM v3 المقابس بطريقة مختلفة: كل *مقبس I2P* يطابق مقبس فريد من العميل إلى SAM، مما يجعل التعامل معه أبسط بكثير. هذا مشابه لـ [BOB](/docs/api/bob).

يوفر SAMv3 أيضًا منفذ UDP لإرسال الرسائل المجمعة (datagrams) عبر I2P، ويمكنه إعادة توجيه رسائل I2P المجمعة إلى خادم الرسائل المجمعة الخاص بالعميل.

### تغييرات الإصدار 3.1

تم تقديم الإصدار 3.1 في إصدار Java I2P 0.9.14 (يوليو 2014). SAMv3.1 هو الحد الأدنى الموصى به لتنفيذ SAM بسبب دعمه لأنواع توقيع أفضل من SAM 3.0. i2pd يدعم أيضاً معظم ميزات 3.1.

- DEST GENERATE و SESSION CREATE يدعمان الآن معامل SIGNATURE_TYPE.
- معاملا MIN و MAX في HELLO VERSION أصبحا اختياريين الآن.
- معاملا MIN و MAX في HELLO VERSION يدعمان الآن الإصدارات أحادية الرقم مثل "3".
- RAW SEND مدعوم الآن على bridge socket.

### تغييرات الإصدار 3.2

تم تقديم الإصدار 3.2 في إصدار Java I2P 0.9.24 (يناير 2016). لاحظ أن i2pd لا يدعم حاليًا معظم ميزات 3.2.

#### دعم منفذ وبروتوكول I2CP

- خيارات SESSION CREATE للـ FROM_PORT وTO_PORT
- خيار SESSION CREATE STYLE=RAW للـ PROTOCOL
- خيارات STREAM CONNECT وDATAGRAM SEND وRAW SEND للـ FROM_PORT وTO_PORT
- خيار RAW SEND للـ PROTOCOL
- DATAGRAM RECEIVED وRAW RECEIVED والتدفقات المُحوَّلة أو المُستلمة والـ datagrams القابلة للرد، تتضمن FROM_PORT وTO_PORT
- خيار RAW session الـ HEADER=true سيجعل الـ raw datagrams المُحوَّلة تُسبق بسطر يحتوي على PROTOCOL=nnn FROM_PORT=nnnn TO_PORT=nnnn
- السطر الأول من الـ datagrams المُرسلة عبر المنفذ 7655 يمكن أن يبدأ الآن بأي إصدار 3.x
- السطر الأول من الـ datagrams المُرسلة عبر المنفذ 7655 يمكن أن يحتوي على أي من الخيارات FROM_PORT أو TO_PORT أو PROTOCOL
- RAW RECEIVED يتضمن PROTOCOL=nnn

#### SSL والمصادقة

- USER/PASSWORD في معاملات HELLO للتفويض. انظر [أدناه](#authorization).
- تكوين التفويض الاختياري باستخدام أمر AUTH. انظر [أدناه](#authorization-configuration-sam-32-or-higher-optional-feature).
- دعم SSL/TLS الاختياري على مقبس التحكم. انظر [أدناه](#ssl).
- خيار STREAM FORWARD SSL=true

#### تعدد الخيوط

- مسموح بعمليات STREAM ACCEPT المعلقة المتزامنة على نفس معرف الجلسة.

#### تحليل سطر الأوامر والحفاظ على الاتصال

- الأوامر الاختيارية QUIT و STOP و EXIT لإغلاق الجلسة والمقبس. انظر [أدناه](#quitstopexitinvisible-sam-32-or-higher-optional-features).
- سيتعامل تحليل الأوامر بشكل صحيح مع UTF-8
- يتعامل تحليل الأوامر بشكل موثوق مع المسافات البيضاء داخل علامات الاقتباس
- قد يتم استخدام الشرطة المائلة العكسية '\\' لتجاهل علامات الاقتباس في سطر الأوامر
- يُوصى بأن يقوم الخادم بتحويل الأوامر إلى أحرف كبيرة، لسهولة الاختبار عبر telnet.
- قد يُسمح بقيم الخيارات الفارغة مثل PROTOCOL أو PROTOCOL=، حسب التنفيذ.
- PING/PONG للحفاظ على الاتصال نشطًا. انظر أدناه.
- قد تنفذ الخوادم مهلات زمنية لأمر HELLO أو الأوامر اللاحقة، حسب التنفيذ.

### تغييرات الإصدار 3.3

تم تقديم الإصدار 3.3 في إصدار Java I2P 0.9.25 (مارس 2016). لاحظ أن i2pd لا يدعم حاليًا معظم ميزات الإصدار 3.3.

- يمكن استخدام نفس الجلسة للتدفقات والرسائل المجمعة والخام في نفس الوقت. سيتم توجيه الحزم والتدفقات الواردة بناءً على بروتوكول I2P ومنفذ الوجهة. انظر [قسم PRIMARY أدناه](#sam-primary-sessions-v33-and-higher).
- يدعم DATAGRAM SEND و RAW SEND الآن الخيارات SEND_TAGS و TAG_THRESHOLD و EXPIRES و SEND_LEASESET. انظر [قسم إرسال الرسائل المجمعة أدناه](#sending-repliable-or-raw-datagrams).

## بروتوكول الإصدار 3

### نظرة عامة على مواصفات Simple Anonymous Messaging (SAM) الإصدار 3.3

تطبيق العميل يتواصل مع جسر SAM، الذي يتعامل مع جميع وظائف I2P (باستخدام [مكتبة التدفق](/docs/api/streaming) للتدفقات الافتراضية، أو [I2CP](/docs/protocol/i2cp) مباشرة للبيانات المجمعة).

بشكل افتراضي، الاتصال بين العميل وجسر SAM غير مشفر وغير مصادق عليه. قد يدعم جسر SAM اتصالات SSL/TLS؛ تفاصيل التكوين والتنفيذ خارج نطاق هذه المواصفة. اعتباراً من SAM 3.2، يتم دعم معاملات المصادقة الاختيارية للمستخدم/كلمة المرور في المصافحة الأولية وقد تكون مطلوبة من قِبل الجسر.

يمكن أن تتخذ اتصالات I2P عدة أشكال متميزة:

- [التدفقات الافتراضية](/docs/api/streaming)
- [البيانات المجمعة القابلة للرد والمصادق عليها](/docs/specs/datagrams#repliable) (الرسائل التي تحتوي على حقل FROM)
- [البيانات المجمعة المجهولة](/docs/specs/datagrams#raw) (الرسائل المجهولة الخام)
- [Datagram2](/docs/specs/datagrams#datagram2) (تنسيق جديد قابل للرد ومصادق عليه)
- [Datagram3](/docs/specs/datagrams#datagram3) (تنسيق جديد قابل للرد لكن غير مصادق عليه)

يتم دعم اتصالات I2P بواسطة جلسات I2P، وكل جلسة I2P مرتبطة بعنوان (يُسمى destination). ترتبط جلسة I2P بواحد من الأنواع الثلاثة المذكورة أعلاه، ولا يمكنها حمل اتصالات من نوع آخر، إلا عند استخدام [جلسات PRIMARY](#sam-primary-sessions-v33-and-higher).

### التشفير والإفلات

جميع رسائل SAM هذه يتم إرسالها على سطر واحد، وتنتهي بحرف السطر الجديد (\\n). قبل SAM 3.2، كان يتم دعم ASCII 7-bit فقط. اعتباراً من SAM 3.2، يجب أن يكون التشفير UTF-8. أي مفاتيح أو قيم مشفرة بـ UTF8 يجب أن تعمل.

التنسيق المعروض في هذه المواصفة أدناه هو فقط للقراءة، وبينما يجب أن تبقى الكلمتان الأوليان في كل رسالة في ترتيبهما المحدد، يمكن تغيير ترتيب أزواج key=value (مثل "ONE TWO A=B C=D" أو "ONE TWO C=D A=B" كلاهما تراكيب صحيحة تماماً). بالإضافة إلى ذلك، البروتوكول حساس لحالة الأحرف. فيما يلي، أمثلة الرسائل مسبوقة بـ "->" للرسائل المرسلة من العميل إلى جسر SAM، وبـ "<-" للرسائل المرسلة من جسر SAM إلى العميل.

يأخذ السطر الأساسي للأمر أو الاستجابة إحدى الأشكال التالية:

```
COMMAND SUBCOMMAND [key=value] [key=value] ...
COMMAND                                           # As of SAM 3.2
PING[ arbitrary text]                             # As of SAM 3.2
PONG[ arbitrary text]                             # As of SAM 3.2
```
الأمر COMMAND بدون SUBCOMMAND مدعوم لبعض الأوامر الجديدة في SAM 3.2 فقط.

يجب فصل أزواج Key=value بمسافة واحدة. (اعتبارًا من SAMv3.2، يُسمح بمسافات متعددة) يجب وضع القيم بين علامتي اقتباس مزدوجتين إذا كانت تحتوي على مسافات، مثل key="long value text". (قبل SAMv3.2، لم يكن هذا يعمل بشكل موثوق في بعض التطبيقات)

قبل SAMv3.2، لم تكن هناك آلية للهروب. اعتباراً من SAMv3.2، يمكن الهروب من علامات الاقتباس المزدوجة بخط مائل عكسي '\\' ويمكن تمثيل الخط المائل العكسي كخطين مائلين عكسيين '\\\\'.

### القيم الفارغة

اعتبارًا من SAMv3.2، قد يُسمح بقيم الخيارات الفارغة مثل KEY أو KEY= أو KEY=""، وذلك حسب التنفيذ.

### حساسية الأحرف الكبيرة والصغيرة

البروتوكول، كما هو محدد، حساس لحالة الأحرف. يُنصح ولكن ليس مطلوباً أن يقوم الخادم بتحويل الأوامر إلى أحرف كبيرة، لتسهيل الاختبار عبر telnet. هذا قد يسمح، على سبيل المثال، بعمل "hello version". هذا يعتمد على التنفيذ. لا تحول المفاتيح أو القيم إلى أحرف كبيرة، حيث أن هذا قد يفسد خيارات [I2CP](/docs/protocol/i2cp).

### مصافحة اتصال SAM

لا يمكن أن تحدث أي اتصالات SAM حتى يتفق العميل والجسر على إصدار البروتوكول، والذي يتم عن طريق إرسال العميل لرسالة HELLO وإرسال الجسر لرد HELLO REPLY:

```
->  HELLO VERSION
          [MIN=$min]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [MAX=$max]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [USER="xxx"]          # As of SAM 3.2, required if authentication is enabled, see below
          [PASSWORD="yyy"]      # As of SAM 3.2, required if authentication is enabled, see below
```
و

```
<-  HELLO REPLY RESULT=OK VERSION=3.1
```
اعتباراً من الإصدار 3.1 (I2P 0.9.14)، تُعتبر معاملات MIN و MAX اختيارية. سيقوم SAM دائماً بإرجاع أعلى إصدار ممكن ضمن قيود MIN و MAX، أو إصدار الخادم الحالي في حالة عدم تحديد أي قيود.

إذا لم يتمكن جسر SAM من العثور على إصدار مناسب، فإنه يرد بـ:

```
<- HELLO REPLY RESULT=NOVERSION
```
إذا حدث خطأ ما، مثل تنسيق طلب خاطئ، فإنه يرد بـ:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
#### SSL

قد يوفر مقبس التحكم الخاص بالخادم دعماً اختيارياً لـ SSL/TLS، حسب الإعداد على الخادم والعميل. قد توفر التنفيذات طبقات نقل أخرى أيضاً؛ وهذا خارج نطاق تعريف البروتوكول.

#### التفويض

للتخويل، يضيف العميل USER="xxx" PASSWORD="yyy" إلى معاملات HELLO. علامات الاقتباس المزدوجة لاسم المستخدم وكلمة المرور مُوصى بها لكنها غير مطلوبة. يجب تجاهل علامة الاقتباس المزدوجة داخل اسم المستخدم أو كلمة المرور بخط مائل عكسي. عند الفشل، سيرد الخادم بـ I2P_ERROR ورسالة. يُوصى بتمكين SSL على أي خوادم SAM التي تتطلب التخويل.

#### المهلة الزمنية

قد تقوم الخوادم بتطبيق مهلات زمنية لأمر HELLO أو الأوامر اللاحقة، حسب التنفيذ. يجب على العملاء إرسال HELLO والأمر التالي بسرعة بعد الاتصال.

إذا حدث انتهاء مهلة زمنية قبل استلام HELLO، يرد الجسر بـ:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
ثم ينقطع الاتصال.

إذا حدث انتهاء مهلة زمنية بعد استلام HELLO ولكن قبل الأمر التالي، يرد الجسر بـ:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
ثم ينقطع الاتصال.

### منافذ I2CP والبروتوكول

اعتبارًا من SAMv3.2، يمكن لمرسل عميل SAM تحديد منافذ وبروتوكول [I2CP](/docs/protocol/i2cp) ليتم تمريرها إلى [I2CP](/docs/protocol/i2cp)، وسيقوم جسر SAM بتمرير معلومات منفذ وبروتوكول [I2CP](/docs/protocol/i2cp) المستلمة إلى عميل SAM.

بالنسبة لـ FROM_PORT و TO_PORT، النطاق الصحيح هو 0-65535، والافتراضي هو 0.

بالنسبة لـ PROTOCOL، والذي قد يتم تحديده فقط لـ RAW، النطاق الصالح هو 0-255، والافتراضي هو 18.

بالنسبة لأوامر SESSION، فإن المنافذ والبروتوكول المحددة هي الافتراضية لتلك الجلسة. بالنسبة للتدفقات أو البيانات المجمعة الفردية، فإن المنافذ والبروتوكول المحددة تلغي افتراضيات الجلسة. بالنسبة للتدفقات أو البيانات المجمعة المستلمة، فإن المنافذ والبروتوكول المشار إليها هي كما تم استلامها من [I2CP](/docs/protocol/i2cp).

#### الاختلافات المهمة عن بروتوكول IP القياسي

منافذ I2CP مخصصة لمقابس I2P وحزم البيانات. وهي غير مرتبطة بمقابسك المحلية التي تتصل بـ SAM.

- المنفذ 0 صالح وله معنى خاص.
- المنافذ 1-1023 ليست خاصة أو مميزة.
- الخوادم تستمع على المنفذ 0 افتراضياً، مما يعني "جميع المنافذ".
- العملاء يرسلون إلى المنفذ 0 افتراضياً، مما يعني "أي منفذ".
- العملاء يرسلون من المنفذ 0 افتراضياً، مما يعني "غير محدد".
- قد تحتوي الخوادم على خدمة تستمع على المنفذ 0 وخدمات أخرى تستمع على منافذ أعلى. إذا كان الأمر كذلك، فإن خدمة المنفذ 0 هي الافتراضية، وسيتم الاتصال بها إذا لم يتطابق منفذ المقبس الوارد أو datagram مع خدمة أخرى.
- معظم وجهات I2P لديها خدمة واحدة فقط تعمل عليها، لذلك يمكنك استخدام الإعدادات الافتراضية، وتجاهل تكوين منافذ I2CP.
- SAM 3.2 أو 3.3 مطلوب لتحديد منافذ I2CP.
- إذا كنت لا تحتاج إلى منافذ I2CP، فأنت لا تحتاج إلى SAM 3.2 أو 3.3؛ 3.1 كافي.
- البروتوكول 0 صالح ويعني "أي بروتوكول". هذا غير مُوصى به، وربما لن يعمل.
- يتم تتبع مقابس I2P بواسطة معرف اتصال داخلي. لذلك، لا يوجد شرط أن تكون الخماسية dest:port:dest:port:protocol فريدة. على سبيل المثال، قد تكون هناك عدة مقابس بنفس المنافذ بين وجهتين. العملاء لا يحتاجون إلى اختيار "منفذ حر" للاتصال الصادر.

إذا كنت تصمم تطبيق SAM 3.3 مع عدة جلسات فرعية، فكر بعناية في كيفية استخدام المنافذ والبروتوكولات بشكل فعال. راجع مواصفات [I2CP](/docs/protocol/i2cp) للحصول على مزيد من المعلومات.

### جلسات SAM

يتم إنشاء جلسة SAMv3 عندما يفتح العميل مقبسًا إلى جسر SAM، ويقوم بعملية المصافحة، ويرسل رسالة SESSION CREATE، وتنتهي الجلسة عند قطع الاتصال بالمقبس.

كل I2P Destination مسجل يرتبط بشكل فريد مع معرف جلسة (أو اسم مستعار). معرفات الجلسات، بما في ذلك معرفات الجلسات الفرعية للجلسات الأساسية، يجب أن تكون فريدة عالمياً على خادم SAM. لمنع التضارب المحتمل في المعرفات مع العملاء الآخرين، أفضل الممارسات هي أن يقوم العميل بتوليد المعرفات بشكل عشوائي.

كل جلسة مرتبطة بشكل فريد مع:

- المقبس الذي ينشئ منه العميل الجلسة
- معرفه (أو اسمه المستعار)

#### طلب إنشاء جلسة

رسالة إنشاء الجلسة يمكنها استخدام شكل واحد فقط من هذه الأشكال (الرسائل المستلمة من خلال أشكال أخرى يتم الرد عليها برسالة خطأ):

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
DESTINATION يحدد أي وجهة يجب استخدامها لإرسال واستقبال الرسائل/التدفقات. إن $privkey هو الترميز base 64 لدمج [Destination](/docs/specs/common-structures#type_Destination) متبوعاً بـ [Private Key](/docs/specs/common-structures#type_PrivateKey) متبوعاً بـ [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey)، واختيارياً متبوعاً بـ [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature)، والذي يبلغ 663 بايت أو أكثر في النظام الثنائي و884 بايت أو أكثر في base 64، اعتماداً على نوع التوقيع. تم تحديد التنسيق الثنائي في Private Key File. انظر الملاحظات الإضافية حول [Private Key](/docs/specs/common-structures#type_PrivateKey) في قسم Destination Key Generation أدناه.

إذا كان مفتاح التوقيع الخاص كله أصفار، فإن قسم [التوقيع غير المتصل](/docs/specs/common-structures#struct_OfflineSignature) يتبع ذلك. التوقيعات غير المتصلة مدعومة فقط لجلسات STREAM و RAW. لا يمكن إنشاء التوقيعات غير المتصلة مع DESTINATION=TRANSIENT. تنسيق قسم التوقيع غير المتصل هو:

1. الطابع الزمني للانتهاء (4 بايت، big endian، ثواني منذ العصر، يعيد التدوير في 2106)
2. نوع التوقيع للمفتاح العام للتوقيع المؤقت (2 بايت، big endian)
3. المفتاح العام للتوقيع المؤقت (الطول كما هو محدد بنوع التوقيع المؤقت)
4. توقيع الحقول الثلاثة أعلاه بواسطة المفتاح غير المتصل (الطول كما هو محدد بنوع توقيع الوجهة)
5. المفتاح الخاص للتوقيع المؤقت (الطول كما هو محدد بنوع التوقيع المؤقت)

إذا تم تحديد الوجهة كـ TRANSIENT، فإن جسر SAM ينشئ وجهة جديدة. اعتباراً من الإصدار 3.1 (I2P 0.9.14)، إذا كانت الوجهة TRANSIENT، يتم دعم معامل اختياري SIGNATURE_TYPE. قيمة SIGNATURE_TYPE قد تكون أي اسم (مثل ECDSA_SHA256_P256، غير حساس لحالة الأحرف) أو رقم (مثل 1) مدعوم بواسطة [شهادات المفاتيح](/docs/specs/common-structures#type_Certificate). القيمة الافتراضية هي DSA_SHA1، والذي ليس ما تريده. لمعظم التطبيقات، يرجى تحديد SIGNATURE_TYPE=7.

$nickname هو اختيار العميل. لا يُسمح بالمسافات الفارغة.

الخيارات الإضافية المعطاة يتم تمريرها إلى تكوين جلسة I2P إذا لم يتم تفسيرها بواسطة جسر SAM (مثل outbound.length=0).

لدى router الـ Java I2P و router الـ i2pd قيم افتراضية مختلفة لكميات الـ tunnel. القيمة الافتراضية لـ Java هي 2 بينما القيمة الافتراضية لـ i2pd هي 5. بالنسبة لمعظم حالات النطاق الترددي المنخفض إلى المتوسط وعدد الاتصالات المنخفض إلى المتوسط، فإن 2 أو 3 يكفي. يرجى تحديد كميات الـ tunnel في رسالة SESSION CREATE للحصول على أداء متسق مع router الـ Java I2P و router الـ i2pd، باستخدام الخيارات مثل inbound.quantity=3 outbound.quantity=3. هذه الخيارات وخيارات أخرى [موثقة في الروابط أدناه](#tunnel-i2cp-and-streaming-options).

جسر SAM نفسه يجب أن يكون مُكوناً مسبقاً مع router الذي يجب أن يتصل من خلاله عبر I2P (رغم أنه قد تكون هناك طريقة لتوفير تجاوز إذا لزم الأمر، مثل i2cp.tcp.host=localhost و i2cp.tcp.port=7654).

#### استجابة إنشاء الجلسة

بعد استلام رسالة إنشاء الجلسة، ستقوم جسر SAM بالرد برسالة حالة الجلسة، كما يلي:

إذا تم الإنشاء بنجاح:

```
<-  SESSION STATUS RESULT=OK DESTINATION=$privkey
```
إن $privkey هو الـ base 64 لربط [Destination](/docs/specs/common-structures#type_Destination) متبوعاً بـ [Private Key](/docs/specs/common-structures#type_PrivateKey) متبوعاً بـ [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey)، واختيارياً متبوعاً بـ [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature)، والذي يبلغ 663 بايت أو أكثر في النظام الثنائي و884 بايت أو أكثر في base 64، اعتماداً على نوع التوقيع. التنسيق الثنائي محدد في ملف Private Key File.

إذا احتوى SESSION CREATE على مفتاح توقيع خاص يتكون من أصفار فقط وقسم [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature)، فإن رد SESSION STATUS سيتضمن نفس البيانات بنفس التنسيق. راجع قسم SESSION CREATE أعلاه للتفاصيل.

إذا كان الاسم المستعار مرتبطًا بالفعل بجلسة:

```
<-  SESSION STATUS RESULT=DUPLICATED_ID
```
إذا كانت الوجهة قيد الاستخدام بالفعل:

```
<-  SESSION STATUS RESULT=DUPLICATED_DEST
```
إذا لم يكن الوجهة مفتاح وجهة خاص صالح:

```
<-  SESSION STATUS RESULT=INVALID_KEY
```
إذا حدث خطأ آخر:

```
<-  SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
إذا لم تكن بخير، يجب أن تحتوي الرسالة MESSAGE على معلومات قابلة للقراءة البشرية حول سبب عدم إمكانية إنشاء الجلسة.

لاحظ أن الـ router يبني الأنفاق قبل الاستجابة بـ SESSION STATUS. قد يستغرق هذا عدة ثوان، أو، عند بدء تشغيل الـ router أو أثناء الازدحام الشديد في الشبكة، دقيقة أو أكثر. في حالة عدم النجاح، لن يستجيب الـ router برسالة فشل لعدة دقائق. لا تضع مهلة زمنية قصيرة في انتظار الاستجابة. لا تتخلى عن الجلسة بينما بناء النفق قيد التنفيذ وتعيد المحاولة.

جلسات SAM تعيش وتموت مع المقبس المرتبطة به. عندما يُغلق المقبس، تموت الجلسة، وتموت جميع الاتصالات التي تستخدم الجلسة في نفس الوقت. وبالعكس، عندما تموت الجلسة لأي سبب، يغلق جسر SAM المقبس.

### تدفقات SAM الافتراضية

التدفقات الافتراضية مضمونة الإرسال بشكل موثوق ومرتب، مع إشعارات الفشل والنجاح بمجرد توفرها.

التدفقات (Streams) هي مقابس اتصال ثنائية الاتجاه بين وجهتين I2P، ولكن يجب على إحداهما طلب فتحها. فيما بعد، يتم استخدام أوامر CONNECT من قبل عميل SAM لمثل هذا الطلب. يتم استخدام أوامر FORWARD / ACCEPT من قبل عميل SAM عندما يريد الاستماع للطلبات القادمة من وجهات I2P أخرى.

### SAM Virtual Streams: CONNECT

يطلب العميل الاتصال عن طريق:

- فتح socket جديد مع جسر SAM
- تمرير نفس مصافحة HELLO كما هو موضح أعلاه
- إرسال أمر STREAM CONNECT

#### طلب الاتصال

```
-> STREAM CONNECT
         ID=$nickname
         DESTINATION=$destination
         [SILENT={true,false}]                # default false
         [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
         [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
```
هذا ينشئ اتصالاً افتراضياً جديداً من الجلسة المحلية التي معرفها $nickname إلى النظير المحدد.

الهدف هو $destination، والذي يمثل base 64 للـ [Destination](/docs/specs/common-structures#type_Destination)، والذي يتكون من 516 أو أكثر من أحرف base 64 (387 أو أكثر من البايتات في النظام الثنائي)، حسب نوع التوقيع.

**ملاحظة:** منذ حوالي عام 2014 (SAM v3.1)، يدعم Java I2P أيضاً أسماء المضيفين وعناوين b32 لـ $destination، ولكن هذا لم يكن موثقاً سابقاً. أسماء المضيفين وعناوين b32 مدعومة رسمياً الآن من قبل Java I2P اعتباراً من الإصدار 0.9.48. router i2pd يدعم أسماء المضيفين وعناوين b32 اعتباراً من الإصدار 2.38.0 (0.9.50). بالنسبة لكلا الـ routers، دعم "b32" يتضمن دعم عناوين "b33" الموسعة للـ blinded destinations.

#### استجابة الاتصال

إذا تم تمرير SILENT=true، فلن يصدر جسر SAM أي رسالة أخرى على المقبس. في حالة فشل الاتصال، سيتم إغلاق المقبس. في حالة نجاح الاتصال، سيتم إعادة توجيه جميع البيانات المتبقية التي تمر عبر المقبس الحالي من وإلى وجهة I2P المتصلة.

إذا كان SILENT=false، وهي القيمة الافتراضية، فإن جسر SAM يرسل رسالة أخيرة إلى العميل الخاص به قبل إعادة التوجيه أو إغلاق المقبس:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
قد تكون قيمة RESULT واحدة من:

```
OK
CANT_REACH_PEER
I2P_ERROR
INVALID_KEY
INVALID_ID
TIMEOUT
```
إذا كانت النتيجة RESULT هي OK، فإن جميع البيانات المتبقية التي تمر عبر المقبس الحالي يتم توجيهها من وإلى نظير الوجهة I2P المتصل. إذا لم يكن الاتصال ممكناً (انتهاء المهلة الزمنية، إلخ)، فإن RESULT ستحتوي على قيمة الخطأ المناسبة (مصحوبة برسالة MESSAGE اختيارية قابلة للقراءة)، وجسر SAM يغلق المقبس.

مهلة اتصال تدفق router داخلياً هي دقيقة واحدة تقريباً، وتعتمد على التنفيذ. لا تقم بتعيين مهلة أقصر للانتظار للاستجابة.

### SAM Virtual Streams: ACCEPT

ينتظر العميل طلب اتصال وارد من خلال:

- فتح socket جديد مع جسر SAM
- تمرير نفس مصافحة HELLO المذكورة أعلاه
- إرسال أمر STREAM ACCEPT

#### قبول الطلب

```
-> STREAM ACCEPT
         ID=$nickname
         [SILENT={true,false}]                # default false
```
هذا يجعل الجلسة ${nickname} تستمع لطلب اتصال واردة واحدة من شبكة I2P. ACCEPT غير مسموح بينما يوجد FORWARD نشط على الجلسة.

اعتباراً من SAM 3.2، يُسمح بعدة عمليات STREAM ACCEPT معلقة ومتزامنة على نفس معرف الجلسة (حتى مع نفس المنفذ). قبل الإصدار 3.2، كانت عمليات القبول المتزامنة تفشل مع ALREADY_ACCEPTING. ملاحظة: Java I2P يدعم أيضاً عمليات ACCEPT المتزامنة على SAM 3.1، اعتباراً من الإصدار 0.9.24 (يناير 2016). i2pd يدعم أيضاً عمليات ACCEPT المتزامنة على SAM 3.1، اعتباراً من الإصدار 2.50.0 (ديسمبر 2023).

#### استجابة القبول

إذا تم تمرير SILENT=true، فلن يصدر جسر SAM أي رسالة أخرى على المقبس. إذا فشل القبول، سيتم إغلاق المقبس. إذا نجح القبول، فسيتم إعادة توجيه جميع البيانات المتبقية التي تمر عبر المقبس الحالي من وإلى وجهة I2P المتصلة. من أجل الموثوقية، ولتلقي الوجهة للاتصالات الواردة، يُنصح بـ SILENT=false.

إذا كان SILENT=false، وهو القيمة الافتراضية، فإن جسر SAM يجيب بـ:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
قد تكون قيمة RESULT إحدى القيم التالية:

```
OK
I2P_ERROR
INVALID_ID
```
إذا لم تكن النتيجة OK، يتم إغلاق الـ socket فوراً من قبل جسر SAM. إذا كانت النتيجة OK، يبدأ جسر SAM في انتظار طلب اتصال واردة من peer I2P آخر. عند وصول طلب، يقبله جسر SAM ويقوم بـ:

إذا تم تمرير SILENT=true، فإن جسر SAM لن يرسل أي رسالة أخرى على مقبس العميل. جميع البيانات المتبقية التي تمر عبر المقبس الحالي يتم توجيهها من وإلى وجهة I2P المتصلة.

إذا تم تمرير SILENT=false، وهي القيمة الافتراضية، فإن جسر SAM يرسل للعميل سطرًا بترميز ASCII يحتوي على مفتاح الوجهة العامة base64 للنظير الطالب، ومعلومات إضافية لـ SAM 3.2 فقط:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
بعد هذا السطر المنتهي بـ '\\n'، يتم توجيه جميع البيانات المتبقية التي تمر عبر المقبس الحالي من وإلى نظير الوجهة I2P المتصل، حتى يقوم أحد الأنظار بإغلاق المقبس.

#### أخطاء بعد OK

في حالات نادرة، قد يواجه جسر SAM خطأ بعد إرسال RESULT=OK، ولكن قبل وصول اتصال وإرسال سطر $destination إلى العميل. قد تشمل هذه الأخطاء إغلاق router، أو إعادة تشغيل router، أو إغلاق الجلسة. في هذه الحالات، عندما يكون SILENT=false، قد يرسل جسر SAM، ولكن ليس مطلوباً منه (يعتمد على التنفيذ)، السطر التالي:

```
<-  STREAM STATUS
         RESULT=I2P_ERROR
         [MESSAGE=...]
```
قبل إغلاق المقبس فوراً. هذا السطر ليس، بطبيعة الحال، قابلاً للفك كوجهة Base 64 صالحة.

### SAM Virtual Streams: FORWARD

يمكن للعميل استخدام خادم socket عادي وانتظار طلبات الاتصال القادمة من I2P. لهذا، يجب على العميل:

- افتح مقبس جديد مع جسر SAM
- مرر نفس مصافحة HELLO كما هو مذكور أعلاه
- أرسل أمر التوجيه

#### طلب إعادة التوجيه

```
-> STREAM FORWARD
         ID=$nickname
         PORT=$port
         [HOST=$host]
         [SILENT={true,false}]                # default false
         [SSL={true,false}]                   # SAM 3.2 or higher only, default false
```
هذا يجعل الجلسة ${nickname} تستمع لطلبات الاتصال الواردة من شبكة I2P. FORWARD غير مسموح بينما يوجد ACCEPT معلق على الجلسة.

#### إعادة توجيه الاستجابة

SILENT افتراضياً false. سواء كان SILENT true أو false، فإن جسر SAM يجيب دائماً برسالة STREAM STATUS. لاحظ أن هذا سلوك مختلف عن STREAM ACCEPT و STREAM CONNECT عندما SILENT=true. رسالة STREAM STATUS هي:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
قد تكون قيمة RESULT واحدة من:

```
OK
I2P_ERROR
INVALID_ID
```
$host هو اسم المضيف أو عنوان IP الخاص بخادم المقبس الذي سيقوم SAM بإعادة توجيه طلبات الاتصال إليه. إذا لم يتم تقديمه، فإن SAM يأخذ عنوان IP الخاص بالمقبس الذي أصدر أمر إعادة التوجيه.

$port هو رقم المنفذ لخادم المقبس الذي سيقوم SAM بإعادة توجيه طلبات الاتصال إليه. وهو إلزامي.

عندما يصل طلب اتصال من I2P، يفتح جسر SAM اتصال مقبس إلى $host:$port. إذا تم قبوله في أقل من 3 ثوانٍ، سيقبل SAM الاتصال من I2P، وبعدها:

إذا تم تمرير SILENT=true، فإن جميع البيانات التي تمر عبر الـ socket الحالي المحصول عليه يتم إعادة توجيهها من وإلى peer الوجهة المتصل في I2P.

إذا تم تمرير SILENT=false، وهي القيمة الافتراضية، يرسل جسر SAM على المقبس المحصل عليه سطرًا بصيغة ASCII يحتوي على مفتاح الوجهة العامة base64 للنظير الطالب، ومعلومات إضافية لـ SAM 3.2 فقط:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
بعد هذا السطر المنتهي بـ '\\n'، يتم توجيه جميع البيانات المتبقية التي تمر عبر المقبس من وإلى النظير المتصل في وجهة I2P، حتى يقوم أحد الطرفين بإغلاق المقبس.

اعتباراً من SAMv3.2، إذا تم تحديد SSL=true، فإن socket الإعادة التوجيه يكون عبر SSL/TLS.

سيتوقف router I2P عن الاستماع لطلبات الاتصال الواردة بمجرد إغلاق مقبس "forwarding".

### رسائل SAM البيانية

يوفر SAMv3 آليات لإرسال واستقبال الـ datagrams عبر مقابس الـ datagram المحلية. تدعم بعض تطبيقات SAMv3 أيضاً الطريقة الأقدم v1/v2 لإرسال/استقبال الـ datagrams عبر مقبس جسر SAM. كلا الطريقتين موثقتان أدناه.

يدعم I2P أربعة أنواع من الرسائل المجمعة (datagrams):

- الرسائل القابلة للرد والمصادق عليها تبدأ بوجهة المرسل، وتحتوي على توقيع المرسل، بحيث يمكن للمستقبل التحقق من أن وجهة المرسل لم تكن مزيفة، ويمكنه الرد على الرسالة. تنسيق Datagram2 الجديد أيضاً قابل للرد ومصادق عليه.
- تنسيق Datagram3 الجديد قابل للرد ولكن غير مصادق عليه. معلومات المرسل غير موثقة.
- الرسائل الخام لا تحتوي على وجهة المرسل أو التوقيع.

منافذ I2CP الافتراضية محددة لكل من الرسائل القابلة للرد والرسائل الخام. يمكن تغيير منفذ I2CP للرسائل الخام.

نمط تصميم البروتوكول الشائع هو إرسال البيانات القابلة للرد إلى الخوادم، مع تضمين معرف معين، وتقوم الخادم بالرد ببيانات خام تتضمن ذلك المعرف، بحيث يمكن ربط الرد بالطلب. هذا النمط التصميمي يلغي العبء الكبير للبيانات القابلة للرد في الردود. جميع خيارات بروتوكولات I2CP والمنافذ خاصة بالتطبيق، وينبغي للمصممين أخذ هذه القضايا في الاعتبار.

انظر أيضاً الملاحظات المهمة حول MTU للرسائل المجمعة في القسم أدناه.

#### إرسال الرسائل القابلة للرد أو الرسائل الخام

بينما لا يحتوي I2P بطبيعته على عنوان FROM، يتم توفير طبقة إضافية لسهولة الاستخدام كبيانات قابلة للرد - رسائل غير مرتبة وغير موثوقة يصل حجمها إلى 31744 بايت تتضمن عنوان FROM (تاركة ما يصل إلى 1KB لمواد الترويسة). يتم التحقق من صحة عنوان FROM هذا داخلياً بواسطة SAM (مستفيداً من مفتاح التوقيع الخاص بالوجهة للتحقق من المصدر) ويتضمن منع إعادة التشغيل.

الحد الأدنى للحجم هو 1. لأفضل موثوقية في التسليم، الحد الأقصى الموصى به للحجم هو حوالي 11 كيلوبايت. الموثوقية تتناسب عكسياً مع حجم الرسالة، وربما حتى بشكل أسي.

بعد إنشاء جلسة SAM مع STYLE=DATAGRAM أو STYLE=RAW، يمكن للعميل إرسال مخططات بيانات قابلة للرد أو خام من خلال منفذ UDP الخاص بـ SAM (7655 افتراضياً).

يجب أن يكون السطر الأول من datagram المرسل عبر هذا المنفذ بالتنسيق التالي. هذا كله على سطر واحد (مفصول بمسافات)، معروض على عدة أسطر للوضوح:

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
- 3.0 هو إصدار SAM. اعتباراً من SAM 3.2، أي إصدار 3.x مسموح.
- $nickname هو معرف جلسة DATAGRAM التي سيتم استخدامها
- الهدف هو $destination، وهو base 64 الخاص بـ [Destination](/docs/specs/common-structures#type_Destination)، والذي يتكون من 516 حرف base 64 أو أكثر (387 بايت أو أكثر في النظام الثنائي)، اعتماداً على نوع التوقيع. **ملاحظة:** منذ حوالي 2014 (SAM v3.1)، يدعم Java I2P أيضاً أسماء المضيفين وعناوين b32 لـ $destination، لكن هذا لم يكن موثقاً سابقاً. أسماء المضيفين وعناوين b32 مدعومة رسمياً الآن من قبل Java I2P اعتباراً من الإصدار 0.9.48. router i2pd لا يدعم حالياً أسماء المضيفين وعناوين b32؛ قد يتم إضافة الدعم في إصدار مستقبلي.
- جميع الخيارات هي إعدادات لكل datagram تتجاوز الافتراضيات المحددة في SESSION CREATE.
- خيارات الإصدار 3.3 وهي SEND_TAGS و TAG_THRESHOLD و EXPIRES و SEND_LEASESET سيتم تمريرها إلى [I2CP](/docs/protocol/i2cp) إذا كانت مدعومة. راجع [مواصفات I2CP](/docs/protocol/i2cp#msg_SendMessageExpire) للتفاصيل. الدعم من قبل خادم SAM اختياري، سيتجاهل هذه الخيارات إذا لم تكن مدعومة.
- هذا السطر منتهي بـ '\\n'.

سيتم تجاهل السطر الأول من قبل SAM قبل إرسال البيانات المتبقية من الرسالة إلى الوجهة المحددة.

للاطلاع على طريقة بديلة لإرسال الـ datagrams القابلة للرد والخام، راجع [DATAGRAM SEND و RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### SAM Repliable Datagrams: استقبال Datagram

يتم كتابة الـ datagrams المستلمة بواسطة SAMv3 على المنفذ الذي تم فتح جلسة الـ datagram منه، إذا لم يتم تحديد PORT للإعادة التوجيه في أمر SESSION CREATE. هذه هي الطريقة المتوافقة مع الإصدارين v1/v2 لاستقبال الـ datagrams.

عندما يصل datagram، يقوم الجسر بتسليمه إلى العميل عبر الرسالة:

```
<-  DATAGRAM RECEIVED
           DESTINATION=$destination           # See notes below for Datagram3 format
           SIZE=$numBytes
           FROM_PORT=nnn                      # SAM 3.2 or higher only
           TO_PORT=nnn                        # SAM 3.2 or higher only
           \n
       [$numBytes of data]
```
المصدر هو $destination، وهو ترميز base 64 لـ [Destination](/docs/specs/common-structures#type_Destination)، والذي يتكون من 516 حرف base 64 أو أكثر (387 بايت أو أكثر في النظام الثنائي)، اعتماداً على نوع التوقيع.

جسر SAM لا يعرض أبداً على العميل رؤوس المصادقة أو الحقول الأخرى، بل فقط البيانات التي قدمها المرسل. يستمر هذا حتى إغلاق الجلسة (عندما يقطع العميل الاتصال).

#### إعادة توجيه البيانات الخام أو القابلة للرد

عند إنشاء جلسة datagram، يمكن للعميل أن يطلب من SAM توجيه الرسائل الواردة إلى ip:port محدد. يتم ذلك عبر إصدار أمر CREATE مع خيارات PORT و HOST:

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
المتغير $privkey هو base 64 لدمج [Destination](/docs/specs/common-structures#type_Destination) متبوعاً بـ [Private Key](/docs/specs/common-structures#type_PrivateKey) متبوعاً بـ [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey)، واختيارياً متبوعاً بـ [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature)، والذي يحتوي على 884 حرف base 64 أو أكثر (663 بايت أو أكثر في النظام الثنائي)، اعتماداً على نوع التوقيع. التنسيق الثنائي محدد في Private Key File.

التوقيعات غير المتصلة مدعومة لـ RAW و DATAGRAM2 و DATAGRAM3 datagrams، ولكن ليس لـ DATAGRAM. راجع قسم SESSION CREATE أعلاه وقسم DATAGRAM2/3 أدناه للتفاصيل.

$host هو اسم المضيف أو عنوان IP الخاص بخادم datagram الذي سيقوم SAM بإعادة توجيه datagrams إليه. إذا لم يتم توفيره، فسيأخذ SAM عنوان IP الخاص بـ socket الذي أصدر أمر forward.

$port هو رقم المنفذ الخاص بخادم الرسائل المجمعة الذي سيقوم SAM بتوجيه الرسائل المجمعة إليه. إذا لم يتم تعيين $port، فلن يتم توجيه الرسائل المجمعة، بل سيتم استقبالها على مقبس التحكم، بالطريقة المتوافقة مع v1/v2.

يتم تمرير الخيارات الإضافية المعطاة إلى تكوين جلسة I2P إذا لم يتم تفسيرها بواسطة جسر SAM (مثل outbound.length=0). هذه الخيارات [موثقة أدناه](#tunnel-i2cp-and-streaming-options).

البيانات المُعاد توجيهها القابلة للرد تكون مسبوقة دائماً بوجهة base64، باستثناء Datagram3، انظر أدناه. عندما تصل بيانات قابلة للرد، يرسل الجسر إلى المضيف:المنفذ المحدد حزمة UDP تحتوي على البيانات التالية:

```
$destination                       # See notes below for Datagram3 format
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
$datagram_payload
```
يتم توجيه البيانات الخام المُرسلة كما هي إلى المضيف:المنفذ المحدد دون بادئة. تحتوي حزمة UDP على البيانات التالية:

```
$datagram_payload
```
اعتباراً من SAM 3.2، عندما يتم تحديد HEADER=true في SESSION CREATE، سيتم إضافة سطر رأس في بداية الـ datagram الخام المُعاد توجيهه كما يلي:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
الـ $destination هو الـ base 64 للـ [Destination](/docs/specs/common-structures#type_Destination)، والذي يتكون من 516 حرف base 64 أو أكثر (387 بايت أو أكثر في النظام الثنائي)، وذلك حسب نوع التوقيع.

#### SAM رسائل البيانات المجهولة (الخام)

لاستغلال أقصى استفادة من عرض النطاق الترددي لـ I2P، يسمح SAM للعملاء بإرسال واستقبال datagrams مجهولة الهوية، تاركاً معلومات المصادقة والرد للعميل نفسه. هذه الـ datagrams غير موثوقة وغير مرتبة، وقد تصل إلى 32768 بايت.

الحد الأدنى للحجم هو 1. لضمان أفضل موثوقية في التسليم، الحد الأقصى الموصى به للحجم هو حوالي 11 كيلوبايت.

بعد إنشاء جلسة SAM مع STYLE=RAW، يمكن للعميل إرسال رسائل البيانات المجهولة عبر جسر SAM بنفس الطريقة تماماً كما هو الحال في [إرسال رسائل البيانات القابلة للرد](#sending-repliable-or-raw-datagrams).

كلا الطريقتين لاستقبال البيانات المجمعة متاحتان أيضاً للبيانات المجمعة المجهولة.

يتم كتابة البيانات المستلمة بواسطة SAM على المقبس الذي تم فتح جلسة البيانات منه، إذا لم يتم تحديد PORT للإعادة التوجيه في أمر SESSION CREATE. هذه هي الطريقة المتوافقة مع الإصدارين v1/v2 لاستقبال البيانات.

```
<- RAW RECEIVED
          SIZE=$numBytes
          FROM_PORT=nnn                      # SAM 3.2 or higher only
          TO_PORT=nnn                        # SAM 3.2 or higher only
          PROTOCOL=nnn                       # SAM 3.2 or higher only
          \n
      [$numBytes of data]
```
عندما يتم توجيه البيانات المجهولة إلى مضيف:منفذ معين، يرسل الجسر إلى المضيف:المنفذ المحدد رسالة تحتوي على البيانات التالية:

```
$datagram_payload
```
اعتباراً من SAM 3.2، عندما يتم تحديد HEADER=true في SESSION CREATE، سيتم إضافة سطر رأس في بداية الرسالة المُعاد توجيهها كما يلي:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
للحصول على طريقة بديلة لإرسال البيانات المجهولة، راجع [RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### Datagram 2/3

تنسيقات Datagram 2/3 هي تنسيقات جديدة محددة في أوائل عام 2025. لا توجد تطبيقات معروفة حالياً. راجع وثائق التطبيق للاطلاع على الوضع الحالي. انظر [المواصفات](/docs/specs/datagrams) للمزيد من المعلومات.

لا توجد خطط حالية لزيادة إصدار SAM للإشارة إلى دعم Datagram 2/3. قد يكون هذا مشكلة حيث أن التطبيقات قد ترغب في دعم Datagram 2/3 ولكن ليس ميزات SAM v3.3. أي تغيير في الإصدار لم يتم تحديده بعد.

كل من Datagram2 و Datagram3 قابلان للرد عليهما. فقط Datagram2 مُصادق عليه.

Datagram2 مطابق تماماً للـ datagrams القابلة للرد من منظور SAMv3. كلاهما مُصادق عليه. فقط تنسيق I2CP والتوقيع مختلفان، لكن هذا غير مرئي لعملاء SAMv3. Datagram2 يدعم أيضاً التوقيعات غير المتصلة، لذا يمكن استخدامه بواسطة الوجهات الموقعة في وضع عدم الاتصال.

الهدف هو أن يحل Datagram2 محل Repliable datagrams للتطبيقات الجديدة التي لا تتطلب التوافق مع الإصدارات السابقة. يوفر Datagram2 حماية من إعادة التشغيل (replay protection) التي غير موجودة في Repliable datagrams. إذا كان التوافق مع الإصدارات السابقة مطلوباً، فيمكن للتطبيق دعم كل من Datagram2 و Repliable في نفس الجلسة مع جلسات SAM 3.3 PRIMARY.

Datagram3 قابل للرد عليه لكن غير مُصادق عليه. الحقل 'from' في صيغة I2CP هو hash وليس destination. الـ $destination كما يُرسل من خادم SAM إلى العميل سيكون hash بصيغة base64 بحجم 44 بايت. لتحويله إلى destination كامل للرد، قم بفك تشفير base64 إلى 32 بايت ثنائي، ثم قم بتشفيره بصيغة base32 إلى 52 حرف وأضف ".b32.i2p" لإجراء NAMING LOOKUP. كالمعتاد، يجب على العملاء الاحتفاظ بذاكرة التخزين المؤقت الخاصة بهم لتجنب تكرار NAMING LOOKUPs.

يجب على مصممي التطبيقات توخي الحذر الشديد والنظر في الآثار الأمنية للحزم البيانات غير المصادق عليها.

#### اعتبارات MTU لـ V3 Datagram

قد تكون I2P Datagrams أكبر من MTU الإنترنت النموذجي البالغ 1500. من المحتمل أن تتجاوز الـ datagrams المرسلة محلياً والـ datagrams القابلة للرد المُعاد توجيهها والمسبوقة بوجهة base64 بحجم 516+ بايت هذا الـ MTU. ومع ذلك، فإن MTUs المحلية على أنظمة Linux عادة ما تكون أكبر بكثير، على سبيل المثال 65536. ستختلف MTUs المحلية حسب نظام التشغيل. لن تكون I2P Datagrams أكبر من 65536 أبداً. يعتمد حجم الـ datagram على بروتوكول التطبيق.

إذا كان عميل SAM محلياً بالنسبة لخادم SAM ويدعم النظام وحدة نقل أكبر (MTU)، فلن يتم تجزئة الرسائل المرسلة محلياً. ومع ذلك، إذا كان عميل SAM بعيداً، فسيتم تجزئة رسائل IPv4 بينما ستفشل رسائل IPv6 (IPv6 لا يدعم تجزئة UDP).

يجب على مطوري مكتبات العملاء والتطبيقات أن يكونوا على دراية بهذه المشاكل وتوثيق التوصيات لتجنب التجزئة ومنع فقدان الحزم، خاصة في اتصالات SAM البعيدة بين العميل والخادم.

#### DATAGRAM SEND، RAW SEND (معالجة Datagram متوافقة مع V1/V2)

في SAMv3، الطريقة المفضلة لإرسال البيانات المجمعة (datagrams) هي عبر مقبس البيانات المجمعة على المنفذ 7655 كما هو موثق أعلاه. ومع ذلك، يمكن إرسال البيانات المجمعة القابلة للرد مباشرة عبر مقبس جسر SAM باستخدام أمر DATAGRAM SEND، كما هو موثق في [SAM V1](/docs/api/sam) و [SAM V2](/docs/api/samv2).

اعتباراً من الإصدار 0.9.14 (النسخة 3.1)، يمكن إرسال datagrams مجهولة المصدر مباشرة عبر مقبس جسر SAMv3 باستخدام أمر RAW SEND، كما هو موثق في [SAM V1](/docs/api/sam) و [SAM V2](/docs/api/samv2).

اعتباراً من الإصدار 0.9.24 (الإصدار 3.2)، قد تتضمن DATAGRAM SEND و RAW SEND المعاملات FROM_PORT=nnnn و/أو TO_PORT=nnnn لتجاوز المنافذ الافتراضية. اعتباراً من الإصدار 0.9.24 (الإصدار 3.2)، قد تتضمن RAW SEND المعامل PROTOCOL=nnn لتجاوز البروتوكول الافتراضي.

هذه الأوامر *لا* تدعم معامل ID. يتم إرسال البيانات إلى الجلسة المُنشأة مؤخراً من نوع DATAGRAM أو RAW، حسب الحاجة. قد يتم إضافة دعم لمعامل ID في إصدار مستقبلي.

تنسيقات DATAGRAM2 و DATAGRAM3 *غير* مدعومة بالطريقة المتوافقة مع V1/V2.

### جلسات SAM الأساسية (الإصدار 3.3 وما أعلى)

*تم تقديم الإصدار 3.3 في إصدار I2P 0.9.25.*

*في إصدار سابق من هذه المواصفة، كانت جلسات PRIMARY تُعرف باسم جلسات MASTER. في كل من `i2pd` و `I2P+`، لا تزال تُعرف فقط باسم جلسات MASTER.*

يضيف SAMv3.3 دعماً لتشغيل جلسات فرعية للبث المتدفق والبيانات المجمعة والخام على نفس الجلسة الأساسية، ولتشغيل عدة جلسات فرعية من نفس النوع. تستخدم جميع حركة البيانات للجلسات الفرعية وجهة واحدة، أو مجموعة من الـ tunnel. يعتمد توجيه حركة البيانات من I2P على خيارات المنفذ والبروتوكول للجلسات الفرعية.

لإنشاء subsessions متعددة الإرسال، يجب عليك إنشاء جلسة أساسية ثم إضافة subsessions إلى الجلسة الأساسية. كل subsession يجب أن يكون له معرف فريد وبروتوكول استماع ومنفذ فريد. يمكن أيضاً إزالة subsessions من الجلسة الأساسية.

باستخدام جلسة PRIMARY ومجموعة من الجلسات الفرعية، يمكن لعميل SAM دعم تطبيقات متعددة، أو تطبيق واحد متطور يستخدم مجموعة متنوعة من البروتوكولات، على مجموعة واحدة من tunnels. على سبيل المثال، يمكن لعميل bittorrent إعداد جلسة فرعية للبث (streaming subsession) لاتصالات الند للند، بالإضافة إلى جلسات فرعية للـ datagram والـ raw للتواصل مع DHT.

#### إنشاء جلسة PRIMARY

```
->  SESSION CREATE
          STYLE=PRIMARY                        # prior to 0.9.47, use STYLE=MASTER
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP and streaming options
```
سيرد جسر SAM بالنجاح أو الفشل كما في [الاستجابة لـ SESSION CREATE القياسي](#session-creation-response).

لا تقم بتعيين خيارات PORT أو HOST أو FROM_PORT أو TO_PORT أو PROTOCOL أو LISTEN_PORT أو LISTEN_PROTOCOL أو HEADER على جلسة أساسية. لا يجوز لك إرسال أي بيانات على معرف الجلسة الأساسية (PRIMARY session ID) أو على مقبس التحكم. جميع الأوامر مثل STREAM CONNECT أو DATAGRAM SEND وغيرها يجب أن تستخدم معرف الجلسة الفرعية على مقبس منفصل.

الجلسة الأساسية تتصل بـ router وتقوم ببناء tunnels. عندما يستجيب جسر SAM، تكون tunnels قد تم بناؤها والجلسة جاهزة لإضافة الجلسات الفرعية. جميع خيارات [I2CP](/docs/protocol/i2cp) المتعلقة بمعاملات tunnel مثل الطول والكمية والاسم المستعار يجب توفيرها في SESSION CREATE الخاص بالجلسة الأساسية.

جميع أوامر الأدوات المساعدة مدعومة في الجلسة الأساسية.

عندما يتم إغلاق الجلسة الأساسية، يتم إغلاق جميع الجلسات الفرعية أيضاً.

ملاحظة: قبل الإصدار 0.9.47، استخدم STYLE=MASTER. يتم دعم STYLE=PRIMARY اعتباراً من الإصدار 0.9.47. لا يزال MASTER مدعوماً للتوافق مع الإصدارات السابقة.

#### إنشاء جلسة فرعية

باستخدام نفس مقبس التحكم الذي تم إنشاء الجلسة الأساسية عليه:

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
سيستجيب جسر SAM بالنجاح أو الفشل كما في [الاستجابة لـ SESSION CREATE القياسي](#session-creation-response). نظراً لأن الأنفاق تم بناؤها بالفعل في SESSION CREATE الأساسي، يجب أن يستجيب جسر SAM فوراً.

لا تقم بتعيين خيار DESTINATION على SESSION ADD. ستستخدم الجلسة الفرعية الوجهة المحددة في الجلسة الأساسية. يجب إضافة جميع الجلسات الفرعية على مقبس التحكم، أي نفس الاتصال الذي أنشأت عليه الجلسة الأساسية.

يجب أن تحتوي subsessions المتعددة على خيارات فريدة بما فيه الكفاية بحيث يمكن توجيه البيانات الواردة بشكل صحيح. على وجه الخصوص، يجب أن تحتوي sessions المتعددة من نفس النوع على خيارات LISTEN_PORT مختلفة (و/أو LISTEN_PROTOCOL، لـ RAW فقط). إن استخدام SESSION ADD مع منفذ استماع وبروتوكول يكرر subsession موجود بالفعل سيؤدي إلى خطأ.

LISTEN_PORT هو منفذ I2P المحلي، أي منفذ الاستقبال (TO) للبيانات الواردة. إذا لم يتم تحديد LISTEN_PORT، فسيتم استخدام قيمة FROM_PORT. إذا لم يتم تحديد LISTEN_PORT و FROM_PORT، فسيعتمد التوجيه الوارد على STYLE و PROTOCOL فقط. بالنسبة لـ LISTEN_PORT و LISTEN_PROTOCOL، 0 يعني أي قيمة، أي رمز بديل. إذا كان كل من LISTEN_PORT و LISTEN_PROTOCOL يساوي 0، فستكون هذه الجلسة الفرعية هي الافتراضية لحركة المرور الواردة التي لا يتم توجيهها إلى جلسة فرعية أخرى. حركة المرور المتدفقة الواردة (protocol 6) لن يتم توجيهها أبداً إلى جلسة فرعية RAW، حتى لو كان LISTEN_PROTOCOL الخاص بها يساوي 0. جلسة فرعية RAW لا يمكنها تعيين LISTEN_PROTOCOL بقيمة 6. إذا لم يكن هناك افتراضي أو جلسة فرعية تطابق البروتوكول والمنفذ لحركة المرور الواردة، فسيتم إسقاط تلك البيانات.

استخدم معرف الجلسة الفرعية، وليس معرف الجلسة الأساسية، لإرسال واستقبال البيانات. جميع الأوامر مثل STREAM CONNECT، DATAGRAM SEND، إلخ يجب أن تستخدم معرف الجلسة الفرعية.

جميع أوامر الأدوات المساعدة مدعومة على الجلسة الأساسية أو الجلسات الفرعية. إرسال/استقبال datagram/raw من الإصدار v1/v2 غير مدعوم على الجلسة الأساسية أو على الجلسات الفرعية.

#### إيقاف جلسة فرعية

باستخدام نفس control socket التي تم إنشاء جلسة PRIMARY عليها:

```
->  SESSION REMOVE
          ID=$nickname
```
هذا يزيل جلسة فرعية من الجلسة الأساسية. لا تقم بتعيين أي خيارات أخرى على SESSION REMOVE. يجب إزالة الجلسات الفرعية على مقبس التحكم، أي نفس الاتصال الذي أنشأت عليه الجلسة الأساسية. بعد إزالة جلسة فرعية، يتم إغلاقها ولا يمكن استخدامها لإرسال أو استقبال البيانات.

سيستجيب جسر SAM بالنجاح أو الفشل كما هو موضح في [الاستجابة لإنشاء جلسة قياسية](#session-creation-response).

### أوامر أدوات SAM

بعض أوامر الأدوات المساعدة تتطلب جلسة موجودة مسبقاً وبعضها لا يتطلب ذلك. راجع التفاصيل أدناه.

#### البحث عن اسم المضيف

يمكن للعميل استخدام الرسالة التالية لاستعلام جسر SAM حول تحليل الأسماء:

```
NAMING LOOKUP
       NAME=$name
       [OPTIONS=true]     # Default false, as of router API 0.9.66
```
والذي يتم الرد عليه بواسطة

```
NAMING REPLY
       RESULT=$result
       NAME=$name
       [VALUE=$destination]
       [MESSAGE="$message"]
       [OPTION:optionkey="$optionvalue"]   # As of router API 0.9.66
```
قد تكون قيمة RESULT واحدة من:

```
OK
INVALID_KEY
KEY_NOT_FOUND
```
إذا كان NAME=ME، فإن الرد سيحتوي على الوجهة المستخدمة من قبل الجلسة الحالية (مفيد إذا كنت تستخدم واحدة TRANSIENT). إذا لم يكن $result هو OK، فقد تحمل MESSAGE رسالة وصفية، مثل "تنسيق سيء"، إلخ. INVALID_KEY يعني أن هناك خطأ ما في $name في الطلب، ربما أحرف غير صالحة.

الـ $destination هو base 64 الخاص بـ [Destination](/docs/specs/common-structures#type_Destination)، والذي يتكون من 516 أو أكثر من أحرف base 64 (387 أو أكثر من البايتات في النظام الثنائي)، وذلك حسب نوع التوقيع.

NAMING LOOKUP لا يتطلب إنشاء جلسة أولاً. ومع ذلك، في بعض التطبيقات، قد يفشل البحث عن .b32.i2p غير المخزن مؤقتاً والذي يتطلب استعلام شبكة، حيث لا تتوفر أنفاق عميل للبحث.

#### خيارات البحث عن الأسماء

تم توسيع NAMING LOOKUP اعتباراً من router API 0.9.66 لدعم عمليات البحث عن الخدمات. قد يختلف الدعم حسب التطبيق. راجع الاقتراح 167 للحصول على معلومات إضافية.

NAMING LOOKUP NAME=example.i2p OPTIONS=true يطلب تعيين الخيارات في الرد. يمكن أن يكون NAME وجهة base64 كاملة عندما OPTIONS=true.

إذا كان البحث عن الوجهة ناجحاً وكانت الخيارات موجودة في الـ leaseset، فإنه في الرد، بعد الوجهة، ستكون هناك خيار واحد أو أكثر في شكل OPTION:key=value. كل خيار سيكون له بادئة OPTION: منفصلة. جميع الخيارات من الـ leaseset ستُدرج، وليس فقط خيارات سجل الخدمة. على سبيل المثال، قد تكون موجودة خيارات للمعاملات المحددة في المستقبل. مثال:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

المفاتيح التي تحتوي على '='، والمفاتيح أو القيم التي تحتوي على سطر جديد، تُعتبر غير صالحة وسيتم إزالة زوج المفتاح/القيمة من الرد. إذا لم يتم العثور على خيارات في الـ leaseset، أو إذا كان الـ leaseset من الإصدار 1، فلن يتضمن الرد أي خيارات. إذا كان OPTIONS=true موجوداً في البحث، ولم يتم العثور على الـ leaseset، فسيتم إرجاع قيمة نتيجة جديدة LEASESET_NOT_FOUND.

#### توليد مفتاح الوجهة

يمكن إنشاء مفاتيح base64 العامة والخاصة باستخدام الرسالة التالية:

```
->  DEST GENERATE
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, default DSA_SHA1
```
والتي يتم الرد عليها بواسطة

```
DEST REPLY
     PUB=$destination
     PRIV=$privkey
```
اعتباراً من الإصدار 3.1 (I2P 0.9.14)، يتم دعم معامل اختياري SIGNATURE_TYPE. قيمة SIGNATURE_TYPE يمكن أن تكون أي اسم (مثل ECDSA_SHA256_P256، غير حساس لحالة الأحرف) أو رقم (مثل 1) مدعوم بواسطة [Key Certificates](/docs/specs/common-structures#type_Certificate). الافتراضي هو DSA_SHA1، وهو ليس ما تريده. لمعظم التطبيقات، يرجى تحديد SIGNATURE_TYPE=7.

إن $destination هو الترميز base 64 لـ [Destination](/docs/specs/common-structures#type_Destination)، والذي يتكون من 516 حرف base 64 أو أكثر (387 بايت أو أكثر في النظام الثنائي)، اعتماداً على نوع التوقيع.

إن $privkey هو base 64 لتسلسل [Destination](/docs/specs/common-structures#type_Destination) متبوعاً بـ [Private Key](/docs/specs/common-structures#type_PrivateKey) متبوعاً بـ [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey)، والذي يحتوي على 884 حرف base 64 أو أكثر (663 بايت أو أكثر في النظام الثنائي)، بناءً على نوع التوقيع. التنسيق الثنائي محدد في Private Key File.

ملاحظات حول [Private Key](/docs/specs/common-structures#type_PrivateKey) الثنائي 256 بايت: هذا الحقل لم يعد مستخدماً منذ الإصدار 0.6 (2005). قد ترسل تطبيقات SAM بيانات عشوائية أو كلها أصفار في هذا الحقل؛ لا تنزعج من سلسلة AAAA في base 64. معظم التطبيقات ستقوم ببساطة بتخزين سلسلة base 64 وإرجاعها كما هي في SESSION CREATE، أو فك التشفير إلى ثنائي للتخزين، ثم التشفير مرة أخرى لـ SESSION CREATE. قد تقوم التطبيقات، مع ذلك، بفك تشفير base 64، وتحليل الثنائي باتباع مواصفات PrivateKeyFile، وتجاهل جزء private key الـ 256 بايت، ثم استبداله بـ 256 بايت من البيانات العشوائية أو كلها أصفار عند إعادة التشفير لـ SESSION CREATE. يجب الحفاظ على جميع الحقول الأخرى في مواصفات PrivateKeyFile. هذا سيوفر 256 بايت من مساحة تخزين نظام الملفات ولكن ربما لا يستحق العناء لمعظم التطبيقات. راجع الاقتراح 161 للمعلومات الإضافية والخلفية.

DEST GENERATE لا يتطلب إنشاء جلسة أولاً.

لا يمكن استخدام DEST GENERATE لإنشاء وجهة بتوقيعات غير متصلة.

#### PING/PONG (SAM 3.2 أو أعلى)

يمكن للعميل أو الخادم إرسال:

```
PING[ arbitrary text]
```
على منفذ التحكم، مع الاستجابة:

```
PONG[ arbitrary text from the ping]
```
لاستخدامها للحفاظ على اتصال socket التحكم نشطاً. يمكن لأي من الطرفين إغلاق الجلسة و socket إذا لم يتم تلقي استجابة في وقت معقول، حسب التنفيذ المستخدم.

إذا حدث انتهاء مهلة زمنية أثناء انتظار PONG من العميل، قد يرسل الجسر:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
ثم قطع الاتصال.

إذا حدثت مهلة زمنية أثناء انتظار PONG من الجسر، فقد يقوم العميل بقطع الاتصال ببساطة.

PING/PONG لا تتطلب إنشاء جلسة مسبقاً.

#### QUIT/STOP/EXIT (SAM 3.2 أو أعلى، ميزات اختيارية)

الأوامر QUIT و STOP و EXIT ستغلق الجلسة والمقبس. التنفيذ اختياري، لتسهيل الاختبار عبر telnet. ما إذا كان هناك أي رد قبل إغلاق المقبس (على سبيل المثال، رسالة SESSION STATUS) فهو خاص بالتنفيذ وخارج نطاق هذه المواصفة.

QUIT/STOP/EXIT لا تتطلب إنشاء جلسة أولاً.

#### HELP (ميزة اختيارية)

قد تنفذ الخوادم أمر HELP. التنفيذ اختياري، لتسهيل الاختبار عبر telnet. تنسيق المخرجات وكشف نهاية المخرجات محدد حسب التنفيذ وخارج نطاق هذه المواصفة.

HELP لا يتطلب إنشاء جلسة أولاً.

#### إعداد التخويل (SAM 3.2 أو أعلى، ميزة اختيارية)

إعداد التفويض باستخدام أمر AUTH. قد يقوم خادم SAM بتنفيذ هذه الأوامر لتسهيل التخزين المستمر للبيانات الاعتماد. إعداد المصادقة بطرق أخرى غير هذه الأوامر خاص بالتنفيذ وخارج نطاق هذه المواصفة.

- AUTH ENABLE يُفعل التخويل على الاتصالات اللاحقة
- AUTH DISABLE يُعطل التخويل على الاتصالات اللاحقة
- AUTH ADD USER="foo" PASSWORD="bar" يُضيف مستخدم/كلمة مرور
- AUTH REMOVE USER="foo" يُزيل هذا المستخدم

يُنصح باستخدام علامات اقتباس مزدوجة لاسم المستخدم وكلمة المرور ولكنها ليست مطلوبة. يجب تجاهل علامة الاقتباس المزدوجة داخل اسم المستخدم أو كلمة المرور باستخدام شرطة مائلة عكسية. في حالة الفشل، سيرد الخادم برسالة I2P_ERROR ورسالة.

AUTH لا يتطلب إنشاء جلسة أولاً.

### قيم RESULT

هذه هي القيم التي يمكن أن يحملها حقل RESULT، مع معناها:

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
قد لا تكون التطبيقات المختلفة متسقة في أي RESULT يتم إرجاعها في السيناريوهات المختلفة.

معظم الاستجابات التي تحتوي على RESULT، بخلاف OK، ستتضمن أيضاً MESSAGE مع معلومات إضافية. سيكون MESSAGE مفيداً بشكل عام في تشخيص المشاكل. ومع ذلك، فإن نصوص MESSAGE تعتمد على التنفيذ، وقد تكون أو لا تكون مترجمة بواسطة خادم SAMv3 إلى اللغة المحلية الحالية، وقد تحتوي على معلومات داخلية خاصة بالتنفيذ مثل الاستثناءات، وهي عرضة للتغيير دون إشعار مسبق. في حين أن عملاء SAMv3 قد يختارون عرض نصوص MESSAGE للمستخدمين، فإنه لا ينبغي لهم اتخاذ قرارات برمجية بناءً على هذه النصوص، حيث أن ذلك سيكون هشاً.

### خيارات Tunnel وI2CP وStreaming

يمكن تمرير هذه الخيارات كأزواج name=value في سطر SAM SESSION CREATE.

جميع الجلسات قد تتضمن [خيارات I2CP مثل أطوال وكميات tunnel](/docs/protocol/i2cp#options). جلسات STREAM قد تتضمن [خيارات مكتبة Streaming](/docs/api/streaming#options).

راجع تلك المراجع لأسماء الخيارات والقيم الافتراضية. الوثائق المرجعية مخصصة لتنفيذ router في Java. القيم الافتراضية قابلة للتغيير. أسماء الخيارات والقيم حساسة لحالة الأحرف. تنفيذات router الأخرى قد لا تدعم جميع الخيارات وقد تحتوي على قيم افتراضية مختلفة؛ راجع وثائق router للحصول على التفاصيل.

### ملاحظات BASE 64

يجب أن يستخدم تشفير Base 64 الأبجدية المعيارية لـ I2P وهي "A-Z, a-z, 0-9, -, ~".

### إعداد SAM الافتراضي

المنفذ الافتراضي لـ SAM هو 7656. SAM غير مُفعّل افتراضياً في Java I2P Router؛ يجب تشغيله يدوياً، أو تكوينه للتشغيل التلقائي، في صفحة تكوين العملاء في وحدة تحكم router أو في ملف clients.config. منفذ SAM UDP الافتراضي هو 7655، يستمع على 127.0.0.1. يمكن تغيير هذه الإعدادات في Java router بإضافة المتغيرات sam.udp.port=nnnnn و/أو sam.udp.host=w.x.y.z إلى الاستدعاء، أو على سطر SESSION.

التكوين في routers أخرى خاص بالتنفيذ. راجع [دليل تكوين i2pd هنا](https://i2pd.readthedocs.io/en/latest/user-guide/configuration/).
