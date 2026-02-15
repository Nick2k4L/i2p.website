#!/usr/bin/env python3
"""Fix untranslated meta descriptions on release blog posts.

For non-English release posts where the description is identical to
the English version (i.e. not translated), replaces with a properly
translated description.
"""
import glob
import os
import re
import sys

CONTENT_DIR = "content"
TARGET_LANGS = ["ar", "cs", "de", "es", "fr", "hi", "pt", "vi"]

# ── Translations dictionary ──────────────────────────────────────────
# Maps (filename_stem, lang) -> translated description.
# filename_stem is without .md extension, e.g. "2010-01-22-0-7-10-release"

TRANSLATIONS = {
    # ── Spanish (es) - 17 files ──
    ("2007-10-07-0.6.1.30-release", "es"): "Anuncio del lanzamiento de I2P 0.6.1.30 con mejoras experimentales en el rendimiento de túneles, correcciones de eepget, gestión del backlog de red y mejoras en i2psnark",
    ("2008-02-10-0.6.1.31-release", "es"): "Lanzamiento de I2P 0.6.1.31 con proceso de publicación independiente y múltiples correcciones de errores",
    ("2008-03-09-0.6.1.32-release", "es"): "Lanzamiento de I2P 0.6.1.32 con nuevo algoritmo de construcción de túneles y mejoras de rendimiento",
    ("2008-04-26-0.6.1.33-release", "es"): "Lanzamiento de I2P 0.6.1.33 con correcciones de errores importantes y mejoras de rendimiento",
    ("2008-06-07-0.6.2-release", "es"): "Lanzamiento de I2P 0.6.2 con mejoras de rendimiento y anonimato",
    ("2008-08-26-0.6.3-release", "es"): "Lanzamiento de I2P 0.6.3 con correcciones de errores, optimizaciones y mejoras de seguridad",
    ("2008-10-06-0.6.4-release", "es"): "Lanzamiento de I2P 0.6.4 con mejoras de rendimiento y estabilidad",
    ("2008-12-01-0.6.5-release", "es"): "Lanzamiento de I2P 0.6.5 con el nuevo protocolo BOB y requisito de Java 1.5",
    ("2009-01-25-0.7-release", "es"): "Lanzamiento de I2P 0.7 con mejoras de estabilidad y sistema experimental de direcciones Base32",
    ("2009-03-29-0.7.1-release", "es"): "Lanzamiento de I2P 0.7.1 con optimizaciones de rendimiento, soporte de LeaseSets cifrados y nuevos tipos de túneles",
    ("2009-04-19-0.7.2-release", "es"): "Lanzamiento de I2P 0.7.2 con correcciones de errores, soporte de consola IPv6 e interfaz de escritorio experimental",
    ("2009-05-18-0.7.3-release", "es"): "Lanzamiento de I2P 0.7.3 con correcciones de errores, mejoras y protocolos SAM y BOB actualizados",
    ("2009-06-13-0.7.4-release", "es"): "Lanzamiento de I2P 0.7.4 con capacidad GeoIP, soporte UPnP y NTCP entrante automático",
    ("2009-06-29-0.7.5-release", "es"): "Lanzamiento de I2P 0.7.5 con correcciones de estabilidad de red y anuncio de la partida de Complication",
    ("2009-07-31-0.7.6-release", "es"): "Lanzamiento de I2P 0.7.6 con correcciones de estabilidad de red, nuevos temas de consola y optimizaciones de recursos",
    ("2009-10-12-0.7.7-release", "es"): "Lanzamiento de I2P 0.7.7 con mejoras de anonimato, reestructuración criptográfica y optimizaciones de memoria",
    ("2009-12-08-0.7.8-release", "es"): "Lanzamiento de I2P 0.7.8 con traducciones de la consola del router, mejoras de floodfill y puertos aleatorios",

    # ── German (de) - 35 files ──
    ("2010-01-12-0-7-9-release", "de"): "I2P Version 0.7.9 veröffentlicht mit Fehlerbehebungen für Nachrichtenbeschädigung und Leistungsverbesserungen",
    ("2010-01-22-0-7-10-release", "de"): "I2P Version 0.7.10 veröffentlicht mit Sicherheitskorrekturen für Floodfill-Kommunikationsschwachstellen",
    ("2010-02-15-0-7-11-release", "de"): "I2P Version 0.7.11 veröffentlicht mit uhrzeitbezogenen Korrekturen und Jetty-Sicherheitsupdate",
    ("2010-03-15-0-7-12-release", "de"): "I2P Version 0.7.12 veröffentlicht mit Plugin-Unterstützung und kleineren Tunnel-Build-Nachrichten",
    ("2010-04-27-0-7-13-release", "de"): "I2P Version 0.7.13 veröffentlicht mit Leistungsverbesserungen und aktivierten kleineren Tunnel-Build-Nachrichten",
    ("2010-06-07-0-7-14-release", "de"): "I2P Version 0.7.14 veröffentlicht mit Fehlerbehebungen, Leistungsanpassungen und i2psnark-Verbesserungen",
    ("2010-07-12-0-8-release", "de"): "I2P Version 0.8 veröffentlicht, Beginn der 0.8-Serie mit 18 Monaten an Verbesserungen",
    ("2010-11-15-0-8-1-release", "de"): "I2P Version 0.8.1 veröffentlicht mit Fehlerbehebungen, Leistungsanpassungen und neuem i2psnark-Theme",
    ("2010-12-22-0-8-2-release", "de"): "I2P Version 0.8.2 veröffentlicht mit Fehlerbehebungen, Theme-Updates und Proxy-Autorisierungsunterstützung",
    ("2011-01-24-0-8-3-release", "de"): "I2P Version 0.8.3 veröffentlicht mit SSL-Unterstützung, Leistungsverbesserungen und neuen Konfigurationsseiten",
    ("2011-03-02-release-0.8.4", "de"): "Das Release 0.8.4 enthält einige Leistungsverbesserungen und wichtige Fehlerbehebungen. Außerdem unterstützt i2psnark jetzt Magnet-Links.",
    ("2011-04-18-release-0.8.5", "de"): "Das Release 0.8.5 enthält einige Fehlerbehebungen und Leistungsverbesserungen sowie viele Übersetzungsaktualisierungen.",
    ("2011-05-16-release-0.8.6", "de"): "Das Release 0.8.6 enthält weitere Peer-Auswahl-Abwehrmaßnahmen gegen mächtige Angreifer und Anpassungen an das jüngste schnelle Netzwerkwachstum.",
    ("2011-06-27-release-0.8.7", "de"): "I2P Release 0.8.7 enthält mehrere Upgrades für lange vernachlässigte Komponenten, einschließlich der Naming Services, Graphen, nativen CPU-ID- und BigInteger-Bibliotheken, Krypto-Implementierungen und des Wrappers.",
    ("2011-08-23-release-0.8.8", "de"): "I2P Release 0.8.8 aktiviert die neue hosts.txt-Datenbank zur Beschleunigung von Hostnamen-Abfragen und Speicherung zusätzlicher Informationen zu Hostnamen-Einträgen.",
    ("2011-10-11-release-0.8.9", "de"): "Das Release 0.8.9 enthält mehrere Leistungsverbesserungen und viele Änderungen zur Bewältigung des anhaltend schnellen Netzwerkwachstums.",
    ("2011-10-20-release-0.8.10", "de"): "Release 0.8.10 enthält zwei Änderungen zur Reduzierung der Anzahl der Router-zu-Router-Verbindungen und damit zur Verbesserung der Tunnel-Build-Erfolgsraten und allgemeinen Zuverlässigkeit.",
    ("2011-11-08-release-0.8.11", "de"): "Release 0.8.11 enthält weitere Änderungen zur Reduzierung der Router-zu-Router-Verbindungen und zur Erhöhung der Verbindungs- und Tunnel-Build-Kapazität.",
    ("2012-01-06-release-0.8.12", "de"): "Das Release 0.8.12 behebt mehrere Nachrichtenbeschädigungsfehler, einige davon seit 2005 vorhanden. Es enthält auch eine Neugestaltung der Router-Überlastkontrolle und fortgesetzte Optimierung der CPU- und Speichernutzung.",
    ("2012-02-27-release-0.8.13", "de"): "Das Release 0.8.13 enthält mehrere Fehlerbehebungen und einige neue Funktionen. Wir freuen uns, dass das letzte Release die Leistung deutlich verbessert hat und das Netzwerk trotz anhaltend schnellem Wachstum gut läuft.",
    ("2012-05-02-release-0.9", "de"): "Das Release 0.9 schließt über anderthalb Jahre Arbeit an der 0.8.x-Serie ab, in der wir die Leistung und Sicherheit des Routers sowie die Skalierbarkeit des Netzwerks erheblich verbessert haben.",
    ("2012-07-30-release-0.9.1", "de"): "0.9.1 enthält zahlreiche Fehlerbehebungen in i2psnark, einige Verbesserungen der Streaming-Bibliothek, Änderungen der Startseite, neue Themes und Übersetzungsaktualisierungen.",
    ("2012-09-21-release-0.9.2", "de"): "0.9.2 enthält umfangreiche Low-Level-Änderungen zur Verbesserung der Leistung und Effizienz des Routers. Wir haben unsere UPnP-Bibliothek aktualisiert, damit UPnP bei mehr Nutzern funktioniert.",
    ("2012-10-27-0.9.3-release", "de"): "0.9.3 enthält umfangreiche Low-Level-Änderungen an der Nachrichtenwarteschlange des Routers. Wir implementieren den CoDel Active Queue Management (AQM) Algorithmus.",
    ("2012-12-17-0.9.4-release", "de"): "0.9.4 enthält eine Korrektur für einen Netzwerkkapazitätsfehler, der in 0.9.2 eingeführt wurde und die Netzwerkleistung und -zuverlässigkeit beeinträchtigte.",
    ("2013-03-08-0.9.5-release", "de"): "0.9.5 enthält Fehlerbehebungen und Abwehrmaßnahmen für einige Probleme und Schwachstellen, die von Forschern der UCSB untersucht werden.",
    ("2016-01-27-i2p-0-9-24-release", "de"): "0.9.24 enthält diverse Fehlerbehebungen und Leistungsverbesserungen",
    ("2016-03-22-i2p-0-9-25-release", "de"): "0.9.25 enthält SAM 3.3, QR-Codes und Fehlerbehebungen",
    ("2016-06-07-i2p-0-9-26-release", "de"): "0.9.26 enthält Krypto-Updates, Verbesserungen der Debian-Paketierung und Fehlerbehebungen",
    ("2016-10-17-i2p-0-9-27-release", "de"): "0.9.27 enthält Fehlerbehebungen",
    ("2016-12-12-i2p-0-9-28-release", "de"): "0.9.28 enthält Fehlerbehebungen",
    ("2017-02-27-i2p-0-9-29-release", "de"): "0.9.29 enthält Fehlerbehebungen",
    ("2017-05-03-i2p-0-9-30-release", "de"): "0.9.30 mit Jetty 9",
    ("2017-08-07-i2p-0-9-31-release", "de"): "0.9.31 mit Konsolenaktualisierungen",
    ("2017-11-07-i2p-0-9-32-release", "de"): "0.9.32 mit Konsolenaktualisierungen",

    # ── Arabic (ar) - 66 files ──
    ("2010-01-22-0-7-10-release", "ar"): "إصدار I2P 0.7.10 مع إصلاحات أمنية لثغرات اتصال floodfill",
    ("2010-02-15-0-7-11-release", "ar"): "إصدار I2P 0.7.11 مع إصلاحات متعلقة بالساعة وتحديث أمني لـ Jetty",
    ("2010-03-15-0-7-12-release", "ar"): "إصدار I2P 0.7.12 مع دعم الإضافات ورسائل بناء أنفاق أصغر",
    ("2010-04-27-0-7-13-release", "ar"): "إصدار I2P 0.7.13 مع تحسينات في الأداء وتفعيل رسائل بناء الأنفاق الأصغر",
    ("2010-06-07-0-7-14-release", "ar"): "إصدار I2P 0.7.14 مع إصلاحات أخطاء وتعديلات أداء وتحسينات i2psnark",
    ("2010-07-12-0-8-release", "ar"): "إصدار I2P 0.8 الذي يمثل بداية سلسلة 0.8 مع 18 شهرًا من التحسينات",
    ("2010-11-15-0-8-1-release", "ar"): "إصدار I2P 0.8.1 مع إصلاحات أخطاء وتعديلات أداء وسمة i2psnark جديدة",
    ("2010-12-22-0-8-2-release", "ar"): "إصدار I2P 0.8.2 مع إصلاحات أخطاء وتحديثات السمات ودعم تفويض البروكسي",
    ("2011-01-24-0-8-3-release", "ar"): "إصدار I2P 0.8.3 مع دعم SSL وتحسينات الأداء وصفحات تهيئة جديدة",
    ("2011-03-02-release-0.8.4", "ar"): "يحتوي الإصدار 0.8.4 على بعض تحسينات الأداء وإصلاحات أخطاء مهمة. كذلك أصبح i2psnark يدعم الآن روابط magnet.",
    ("2011-04-18-release-0.8.5", "ar"): "يحتوي الإصدار 0.8.5 على بعض إصلاحات الأخطاء وتحسينات الأداء والكثير من تحديثات الترجمة.",
    ("2011-05-16-release-0.8.6", "ar"): "يحتوي الإصدار 0.8.6 على المزيد من دفاعات اختيار الأقران لمقاومة المهاجمين الأقوياء وتعديلات للتكيف مع النمو السريع الأخير في الشبكة.",
    ("2011-06-27-release-0.8.7", "ar"): "يحتوي إصدار I2P 0.8.7 على عدة ترقيات لمكونات أُهملت طويلاً بما في ذلك خدمات التسمية والرسوم البيانية ومكتبات CPU ID الأصلية وBigInteger وتنفيذات التشفير والغلاف.",
    ("2011-08-23-release-0.8.8", "ar"): "يُفعّل إصدار I2P 0.8.8 قاعدة بيانات hosts.txt الجديدة لتسريع البحث عن أسماء المضيفين وتخزين معلومات إضافية عن إدخالات أسماء المضيفين.",
    ("2011-10-11-release-0.8.9", "ar"): "يحتوي الإصدار 0.8.9 على عدة تحسينات في الأداء والعديد من التغييرات للتعامل مع النمو السريع المستمر للشبكة.",
    ("2011-10-20-release-0.8.10", "ar"): "يتضمن الإصدار 0.8.10 تغييرين يهدفان إلى تقليل عدد الاتصالات بين الموجهات وبالتالي تحسين معدلات نجاح بناء الأنفاق والموثوقية العامة.",
    ("2011-11-08-release-0.8.11", "ar"): "يتضمن الإصدار 0.8.11 المزيد من التغييرات لتقليل الاتصالات بين الموجهات وزيادة سعة الاتصال وبناء الأنفاق.",
    ("2012-01-06-release-0.8.12", "ar"): "يصلح الإصدار 0.8.12 عدة أخطاء في تلف الرسائل بعضها موجود منذ 2005. كما يحتوي على إعادة تصميم التحكم في ازدحام الموجه واستمرار تحسين استخدام المعالج والذاكرة.",
    ("2012-02-27-release-0.8.13", "ar"): "يحتوي الإصدار 0.8.13 على عدة إصلاحات أخطاء وبعض الميزات الجديدة. يسرنا أن الإصدار الأخير حسّن الأداء بشكل ملحوظ والشبكة تعمل بشكل جيد رغم النمو السريع المستمر.",
    ("2012-05-02-release-0.9", "ar"): "يختتم الإصدار 0.9 أكثر من عام ونصف من العمل على سلسلة 0.8.x التي حسّنا فيها أداء وأمان الموجه وقابلية توسع الشبكة بشكل كبير.",
    ("2012-07-30-release-0.9.1", "ar"): "يتضمن 0.9.1 عددًا كبيرًا من إصلاحات الأخطاء في i2psnark وبعض تحسينات مكتبة البث وتغييرات الصفحة الرئيسية وسمات جديدة وتحديثات الترجمة.",
    ("2012-09-21-release-0.9.2", "ar"): "يتضمن 0.9.2 تغييرات واسعة على المستوى المنخفض لتحسين أداء وكفاءة الموجه. قمنا بتحديث مكتبة UPnP لنأمل أن يعمل UPnP لمزيد من المستخدمين.",
    ("2012-10-27-0.9.3-release", "ar"): "يتضمن 0.9.3 تغييرات واسعة على المستوى المنخفض في ترتيب الرسائل في الموجه. نُنفذ خوارزمية CoDel لإدارة قائمة الانتظار النشطة (AQM).",
    ("2012-12-17-0.9.4-release", "ar"): "يتضمن 0.9.4 إصلاحًا لخطأ في سعة الشبكة أُدخل في 0.9.2 كان يُقلل من أداء الشبكة وموثوقيتها.",
    ("2013-03-08-0.9.5-release", "ar"): "يتضمن 0.9.5 إصلاحات أخطاء ودفاعات لبعض المشكلات والثغرات التي يبحثها باحثون في UCSB.",
    ("2013-05-28-0.9.6-release", "ar"): "يتضمن 0.9.6 إصلاحات أخطاء وتحديثًا من Jetty 6.1.26 (2010-11-10) إلى Jetty 7.6.10 (2013-03-12).",
    ("2013-07-15-0.9.7-release", "ar"): "يتضمن 0.9.7 إصلاحات أخطاء وتحسينات مهمة.",
    ("2013-08-10-0.9.7.1-release", "ar"): "يُعطّل هذا الإصدار غير المجدول رسائل التحقق من RouterInfo التي استُخدمت في الهجوم المنشور في ورقة UCSB.",
    ("2013-09-30-0.9.8-release", "ar"): "يتضمن 0.9.8 الدعم المنتظر طويلاً لـ IPv6.",
    ("2013-10-02-0.9.8.1-release", "ar"): "يصلح 0.9.8.1 مشكلة في التحديث إلى 0.9.8 على Windows لدى بعض المستخدمين.",
    ("2013-12-07-0.9.9-release", "ar"): "يصلح 0.9.9 عددًا من الأخطاء في netdb وstreaming وi2ptunnel ويبدأ العمل على خطة سنوية لزيادة قوة خوارزميات التوقيع التشفيري.",
    ("2014-01-21-syndie-1.105b-release", "ar"): "تحديث إلى HSQLDB 2.3.1",
    ("2014-01-22-0.9.10-release", "ar"): "يغيّر 0.9.10 آلية البحث عن LeaseSet مما يجعل من الصعب على المهاجم ربط Destination بـ Router.",
    ("2014-02-08-0.9.11-release", "ar"): "يضيف 0.9.11 دعم إضافات outproxy ويحسّن أمان البحث عن lease set ويقلل استخدام الذاكرة.",
    ("2014-03-12-press-release-ddg-donation", "ar"): "محرك البحث DuckDuckGo يتبرع بـ 5000 دولار لمشروع الإنترنت الخفي (I2P) ضمن برنامج التبرعات مفتوحة المصدر.",
    ("2014-03-31-0.9.12-release", "ar"): "يضيف 0.9.12 دعم ECDSA والتحديث إلى Jetty 8",
    ("2014-05-22-0.9.13-release", "ar"): "0.9.13 مع تحسينات SusiMail وإصلاحات لأجهزة التوجيه خلف جدار الحماية",
    ("2014-07-26-0.9.14-release", "ar"): "يتضمن 0.9.14 إصلاحات أمنية حرجة",
    ("2014-08-09-0.9.14.1-release", "ar"): "يتضمن 0.9.14.1 إصلاحات i2psnark والوحدة",
    ("2014-09-20-0.9.15-release", "ar"): "يتضمن 0.9.15 تشفير Ed25519 والعديد من الإصلاحات",
    ("2014-11-01-0.9.16-release", "ar"): "يتضمن 0.9.16 نقل التشفير والعديد من الإصلاحات",
    ("2014-11-30-0.9.17-release", "ar"): "0.9.17 مع المزيد من نقل التشفير والعديد من الإصلاحات",
    ("2014-12-01-android-app-releases", "ar"): "تم إصدار I2P Android 0.9.17 وBote 0.3 على الموقع وGoogle Play وF-Droid.",
    ("2015-02-22-0.9.18-release", "ar"): "0.9.18 مع تحسينات الأداء وإصلاحات الأخطاء",
    ("2015-04-12-0.9.19-release", "ar"): "0.9.19 مع تحسينات الأداء وإصلاحات الأخطاء",
    ("2015-06-02-0.9.20-release", "ar"): "0.9.20 مع تحسينات الأداء وإصلاحات الأخطاء",
    ("2015-07-31-i2p-0-9-21-release", "ar"): "0.9.21 مع تحسينات الأداء وإصلاحات الأخطاء",
    ("2015-09-12-i2p-0-9-22-release", "ar"): "0.9.22 مع إصلاحات الأخطاء وبدء نقل Ed25519",
    ("2015-11-19-i2p-0-9-23-release", "ar"): "يحتوي 0.9.23 على مجموعة متنوعة من إصلاحات الأخطاء وبعض التحسينات الطفيفة في I2PSnark",
    ("2018-01-30-i2p-0-9-33-release", "ar"): "0.9.33 مع نقل التشفير",
    ("2018-04-10-i2p-0-9-34-release", "ar"): "0.9.34 مع إصلاحات الأخطاء",
    ("2018-06-26-i2p-0-9-35-release", "ar"): "0.9.35 مع توقيعات Ed25519",
    ("2018-08-23-i2p-0-9-36-release", "ar"): "0.9.36 مع NTCP2",
    ("2018-10-04-i2p-0-9-37-release", "ar"): "0.9.37 مع إصلاحات الأخطاء",
    ("2019-01-22-i2p-0-9-38-release", "ar"): "0.9.38 مع تفعيل NTCP2",
    ("2019-03-21-i2p-0-9-39-release", "ar"): "0.9.39 مع دعم LS2",
    ("2019-05-07-i2p-0-9-40-release", "ar"): "0.9.40 مع تعطيل NTCP1",
    ("2019-07-02-i2p-0-9-41-release", "ar"): "0.9.41 مع إصلاحات الأخطاء",
    ("2019-08-27-i2p-0-9-42-release", "ar"): "0.9.42 مع إصلاحات الأخطاء",
    ("2019-10-22-i2p-0-9-43-release", "ar"): "0.9.43 مع إصلاحات الأخطاء",
    ("2019-12-01-i2p-0-9-44-release", "ar"): "0.9.44 مع إصلاحات الأخطاء",
    ("2020-02-25-i2p-0-9-45-release", "ar"): "0.9.45 مع إصلاحات الأخطاء",
    ("2020-05-25-i2p-0-9-46-release", "ar"): "0.9.46 مع تشفير ECIES الجديد",
    ("2020-08-24-i2p-0-9-47-release", "ar"): "0.9.47 يُفعّل تشفير ECIES الجديد",
    ("2020-11-30-i2p-0-9-48-release", "ar"): "0.9.48 مع تحسينات الأداء",
    ("2024-08-06-i2p-2-6-1-release", "ar"): "إصدار 2.6.1 مع إصلاح واجهة I2PTunnel",

    # ── Czech (cs) - 29 files ──
    ("2011-05-16-release-0.8.6", "cs"): "Vydání 0.8.6 obsahuje další obrany při výběru peerů proti silným útočníkům a úpravy pro přizpůsobení nedávnému rychlému růstu sítě.",
    ("2013-03-08-0.9.5-release", "cs"): "0.9.5 obsahuje opravy chyb a obrany proti některým problémům a zranitelnostem, které zkoumají výzkumníci z UCSB.",
    ("2013-05-28-0.9.6-release", "cs"): "0.9.6 obsahuje opravy chyb a aktualizaci z Jetty 6.1.26 (2010-11-10) na Jetty 7.6.10 (2013-03-12).",
    ("2013-07-15-0.9.7-release", "cs"): "0.9.7 obsahuje významné opravy chyb a vylepšení.",
    ("2013-08-10-0.9.7.1-release", "cs"): "Toto neplánované vydání deaktivuje ověřovací zprávy RouterInfo, které byly použity v útoku publikovaném v článku UCSB.",
    ("2013-09-30-0.9.8-release", "cs"): "0.9.8 obsahuje dlouho očekávanou podporu IPv6.",
    ("2013-10-02-0.9.8.1-release", "cs"): "0.9.8.1 opravuje problém s aktualizací na 0.9.8 ve Windows u některých uživatelů.",
    ("2013-12-07-0.9.9-release", "cs"): "0.9.9 opravuje řadu chyb v netdb, streaming a i2ptunnel a zahajuje práci na ročním plánu zvýšení síly kryptografických podpisových algoritmů.",
    ("2014-01-21-syndie-1.105b-release", "cs"): "Aktualizace na HSQLDB 2.3.1",
    ("2014-01-22-0.9.10-release", "cs"): "0.9.10 mění mechanismus vyhledávání LeaseSet, čímž ztěžuje útočníkovi korelaci Destination s Routerem.",
    ("2014-02-08-0.9.11-release", "cs"): "0.9.11 přidává podporu pro outproxy pluginy, zlepšuje zabezpečení vyhledávání lease set a snižuje využití paměti.",
    ("2014-03-12-press-release-ddg-donation", "cs"): "Vyhledávač DuckDuckGo daruje 5000 dolarů projektu Invisible Internet Project (I2P) v rámci svého programu darů pro open source.",
    ("2014-03-31-0.9.12-release", "cs"): "0.9.12 přidává podporu ECDSA a aktualizaci na Jetty 8",
    ("2014-05-22-0.9.13-release", "cs"): "0.9.13 s vylepšeními SusiMail a opravami pro routery za firewallem",
    ("2014-07-26-0.9.14-release", "cs"): "0.9.14 obsahuje kritické bezpečnostní opravy",
    ("2014-08-09-0.9.14.1-release", "cs"): "0.9.14.1 obsahuje opravy i2psnark a konzole",
    ("2014-09-20-0.9.15-release", "cs"): "0.9.15 obsahuje kryptografii Ed25519 a mnoho oprav",
    ("2014-11-01-0.9.16-release", "cs"): "0.9.16 obsahuje migraci kryptografie a mnoho oprav",
    ("2014-11-30-0.9.17-release", "cs"): "0.9.17 s další migrací kryptografie a mnoha opravami",
    ("2014-12-01-android-app-releases", "cs"): "I2P Android 0.9.17 a Bote 0.3 byly vydány na webu, Google Play a F-Droid.",
    ("2015-02-22-0.9.18-release", "cs"): "0.9.18 s vylepšeními výkonu a opravami chyb",
    ("2015-04-12-0.9.19-release", "cs"): "0.9.19 s vylepšeními výkonu a opravami chyb",
    ("2015-06-02-0.9.20-release", "cs"): "0.9.20 s vylepšeními výkonu a opravami chyb",
    ("2015-07-31-i2p-0-9-21-release", "cs"): "0.9.21 s vylepšeními výkonu a opravami chyb",
    ("2015-09-12-i2p-0-9-22-release", "cs"): "0.9.22 s opravami chyb a zahájením migrace Ed25519",
    ("2015-11-19-i2p-0-9-23-release", "cs"): "0.9.23 obsahuje různé opravy chyb a drobná vylepšení v I2PSnark",
    ("2017-08-07-i2p-0-9-31-release", "cs"): "0.9.31 s aktualizacemi konzole",
    ("2023-01-09-i2p-2-1-0-release", "cs"): "2.1.0 s opravami SSU2 a zahlcení",
    ("2023-12-18-i2p-2-4-0-release", "cs"): "Vydání I2P 2.4.0 s vylepšeními zahlcení a zabezpečení NetDB",

    # ── Vietnamese (vi) - 26 files ──
    ("2013-03-08-0.9.5-release", "vi"): "0.9.5 bao gồm sửa lỗi và các biện pháp phòng thủ cho một số vấn đề và lỗ hổng đang được các nhà nghiên cứu tại UCSB điều tra.",
    ("2013-05-28-0.9.6-release", "vi"): "0.9.6 bao gồm sửa lỗi và cập nhật từ Jetty 6.1.26 (2010-11-10) lên Jetty 7.6.10 (2013-03-12).",
    ("2013-07-15-0.9.7-release", "vi"): "0.9.7 bao gồm các bản sửa lỗi và cải tiến đáng kể.",
    ("2013-08-10-0.9.7.1-release", "vi"): "Bản phát hành ngoài kế hoạch này vô hiệu hóa các tin nhắn xác minh RouterInfo đã được sử dụng trong cuộc tấn công công bố trong bài báo UCSB.",
    ("2013-09-30-0.9.8-release", "vi"): "0.9.8 bao gồm hỗ trợ IPv6 được chờ đợi từ lâu.",
    ("2013-10-02-0.9.8.1-release", "vi"): "0.9.8.1 sửa lỗi cập nhật lên 0.9.8 trên Windows cho một số người dùng.",
    ("2013-12-07-0.9.9-release", "vi"): "0.9.9 sửa nhiều lỗi trong netdb, streaming và i2ptunnel, đồng thời bắt đầu kế hoạch một năm để tăng cường độ mạnh của các thuật toán ký mật mã.",
    ("2014-01-21-syndie-1.105b-release", "vi"): "Cập nhật lên HSQLDB 2.3.1",
    ("2014-01-22-0.9.10-release", "vi"): "0.9.10 thay đổi cơ chế tra cứu LeaseSet, khiến kẻ tấn công khó liên kết Destination với Router hơn.",
    ("2014-02-08-0.9.11-release", "vi"): "0.9.11 thêm hỗ trợ plugin outproxy, cải thiện bảo mật tra cứu lease set và giảm sử dụng bộ nhớ.",
    ("2014-03-12-press-release-ddg-donation", "vi"): "Công cụ tìm kiếm DuckDuckGo quyên góp 5.000 đô la cho Dự án Internet Ẩn danh (I2P) trong chương trình quyên góp mã nguồn mở của họ.",
    ("2014-03-31-0.9.12-release", "vi"): "0.9.12 thêm hỗ trợ ECDSA và cập nhật lên Jetty 8",
    ("2014-05-22-0.9.13-release", "vi"): "0.9.13 với các cải tiến SusiMail và sửa lỗi cho các router bị tường lửa",
    ("2014-07-26-0.9.14-release", "vi"): "0.9.14 bao gồm các bản sửa lỗi bảo mật quan trọng",
    ("2014-08-09-0.9.14.1-release", "vi"): "0.9.14.1 bao gồm sửa lỗi i2psnark và bảng điều khiển",
    ("2014-09-20-0.9.15-release", "vi"): "0.9.15 bao gồm mật mã Ed25519 và nhiều bản sửa lỗi",
    ("2014-11-01-0.9.16-release", "vi"): "0.9.16 bao gồm di chuyển mật mã và nhiều bản sửa lỗi",
    ("2014-11-30-0.9.17-release", "vi"): "0.9.17 với thêm di chuyển mật mã và nhiều bản sửa lỗi",
    ("2014-12-01-android-app-releases", "vi"): "I2P Android 0.9.17 và Bote 0.3 đã được phát hành trên trang web, Google Play và F-Droid.",
    ("2015-02-22-0.9.18-release", "vi"): "0.9.18 với cải tiến hiệu năng và sửa lỗi",
    ("2015-04-12-0.9.19-release", "vi"): "0.9.19 với cải tiến hiệu năng và sửa lỗi",
    ("2015-06-02-0.9.20-release", "vi"): "0.9.20 với cải tiến hiệu năng và sửa lỗi",
    ("2015-07-31-i2p-0-9-21-release", "vi"): "0.9.21 với cải tiến hiệu năng và sửa lỗi",
    ("2015-09-12-i2p-0-9-22-release", "vi"): "0.9.22 với sửa lỗi và bắt đầu di chuyển Ed25519",
    ("2015-11-19-i2p-0-9-23-release", "vi"): "0.9.23 chứa nhiều bản sửa lỗi đa dạng và một số cải tiến nhỏ trong I2PSnark",
    ("2024-05-06-i2p-2-5-1-release", "vi"): "Phiên bản I2P 2.5.1",

    # ── French (fr) - 2 files ──
    ("2014-11-01-0.9.16-release", "fr"): "0.9.16 avec migration cryptographique et de nombreuses corrections",
    ("2016-01-27-i2p-0-9-24-release", "fr"): "0.9.24 contient diverses corrections de bogues et améliorations de performances",

    # ── Hindi (hi) - 3 files ──
    ("2014-07-26-0.9.14-release", "hi"): "0.9.14 में महत्वपूर्ण सुरक्षा सुधार शामिल हैं",
    ("2019-03-21-i2p-0-9-39-release", "hi"): "0.9.39 LS2 समर्थन के साथ",
    ("2022-11-21-i2p-2-0-0-release", "hi"): "2.0.0 SSU2 को सक्षम करता है",

    # ── Portuguese (pt) - 2 files ──
    ("2015-07-31-i2p-0-9-21-release", "pt"): "0.9.21 com melhorias de desempenho e correções de bugs",
    ("2023-01-09-i2p-2-1-0-release", "pt"): "2.1.0 com correções de SSU2 e congestionamento",
}


def main():
    dry_run = "--dry-run" in sys.argv

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.join(script_dir, "..", "..")
    content_dir = os.path.join(project_root, CONTENT_DIR)

    if dry_run:
        print("=== DRY RUN - no files will be modified ===\n")

    total_changed = 0
    missing = []

    for lang in TARGET_LANGS:
        lang_dir = os.path.join(content_dir, lang, "blog")
        en_dir = os.path.join(content_dir, "en", "blog")
        if not os.path.isdir(lang_dir):
            continue

        lang_changed = 0
        release_files = sorted(glob.glob(os.path.join(lang_dir, "*release*.md")))

        for filepath in release_files:
            basename = os.path.basename(filepath)
            en_file = os.path.join(en_dir, basename)

            if not os.path.isfile(en_file):
                continue

            # Read both files
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            with open(en_file, "r", encoding="utf-8") as f:
                en_content = f.read()

            # Extract descriptions
            fm = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
            en_fm = re.match(r"^---\n(.*?)\n---", en_content, re.DOTALL)
            if not fm or not en_fm:
                continue

            desc_match = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', fm.group(1), re.MULTILINE)
            en_desc_match = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', en_fm.group(1), re.MULTILINE)
            if not desc_match or not en_desc_match:
                continue

            desc = desc_match.group(1).strip()
            en_desc = en_desc_match.group(1).strip()

            # Only process if description matches English (untranslated)
            if desc != en_desc:
                continue

            # Look up translation
            stem = os.path.splitext(basename)[0]
            key = (stem, lang)
            if key not in TRANSLATIONS:
                missing.append(f"  ({stem!r}, {lang!r}): \"{en_desc}\",")
                continue

            new_desc = TRANSLATIONS[key]
            lang_changed += 1

            if dry_run:
                print(f"  [{lang}] {basename}")
                print(f"    OLD: {desc}")
                print(f"    NEW: {new_desc}")
            else:
                old_line = desc_match.group(0)
                new_line = f'description: "{new_desc}"'
                new_content = content.replace(old_line, new_line, 1)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)

        if lang_changed > 0:
            total_changed += lang_changed
            action = "would change" if dry_run else "changed"
            print(f"[{lang}] {action} {lang_changed} files")

    if missing:
        print(f"\nWARNING: {len(missing)} files missing translations:")
        for m in missing:
            print(m)

    print(f"\nTotal: {total_changed} files {'would be changed' if dry_run else 'changed'}")


if __name__ == "__main__":
    main()
