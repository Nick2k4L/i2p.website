---
title: "Summer Dev roundup: APIs"
date: 2016-07-02
author: "str4d"
description: "In the first month of Summer Dev, we have improved the usability of our APIs for Java, Android, and Python developers."
categories: ["summer-dev"]
---
Der Sommer-Entwicklungszeitraum läuft auf Hochtouren: Wir waren fleißig dabei, Räder zu schmieren, Kanten abzuschleifen und alles aufzuräumen. Nun ist es Zeit für unsere erste Zusammenfassung, in der wir euch über den Fortschritt informieren, den wir bisher erzielt haben!

## API-Monat

Unser Ziel für diesen Monat war es, uns „einzufügen“ – unsere APIs und Bibliotheken so zu gestalten, dass sie nahtlos in die bestehende Infrastruktur verschiedener Communities integriert werden können. Dadurch können Anwendungsentwickler effizienter mit I2P arbeiten, und Nutzer müssen sich nicht um technische Details kümmern.

### Java / Android

Die I2P-Client-Bibliotheken sind jetzt auf Maven Central verfügbar! Für Java-Entwickler wird es dadurch viel einfacher, I2P in ihren Anwendungen zu verwenden. Statt die Bibliotheken aus einer bestehenden Installation extrahieren zu müssen, können sie I2P nun einfach als Abhängigkeit hinzufügen. Auch das Aktualisieren auf neue Versionen wird dadurch deutlich erleichtert.

Die I2P-Android-Client-Bibliothek wurde ebenfalls aktualisiert, um die neuen I2P-Bibliotheken zu nutzen. Dadurch können plattformübergreifende Anwendungen nun nativ sowohl mit I2P für Android als auch mit dem Desktop-I2P arbeiten.

### Python

#### txi2p

Das Twisted-Plugin `txi2p` unterstützt nun I2P-Ports und funktioniert nahtlos über lokale, entfernte und portweitergeleitete SAM-APIs. Siehe die Dokumentation für Anleitungen zur Nutzung und melde Probleme auf GitHub.

#### i2psocket

Die erste (Beta-)Version von `i2psocket` wurde veröffentlicht! Dabei handelt es sich um einen direkten Ersatz für die Standard-Python-`socket`-Bibliothek, der diese um I2P-Unterstützung über die SAM-API erweitert. Siehe die GitHub-Seite für Nutzungsinformationen und um Probleme zu melden.

### Weitere Fortschritte

- zzz hat intensiv an Syndie gearbeitet und bereits einen Vorsprung für den Plugin-Monat erzielt
- psi hat ein I2P-Testnetzwerk mit i2pd eingerichtet und dabei mehrere i2pd-Bugs gefunden und behoben, wodurch die Kompatibilität mit Java-I2P verbessert wird

## Als Nächstes: App-Monat!

Wir freuen uns darauf, im Juli mit Tahoe-LAFS zusammenzuarbeiten! I2P beherbergt seit langem eines der größten öffentlichen Speichernetze, das eine angepasste Version von Tahoe-LAFS nutzt. Während des App-Monats werden wir sie bei ihren Bemühungen unterstützen, native Unterstützung für I2P und Tor hinzuzufügen, sodass I2P-Nutzer von allen Upstream-Verbesserungen profitieren können.

Es gibt noch mehrere andere Projekte, mit denen wir über deren Pläne zur I2P-Integration sprechen und bei der Gestaltung unterstützen werden. Bleibt dran!

## Mach mit beim Summer Dev!

Wir haben noch viele weitere Ideen, was wir in diesen Bereichen erreichen möchten. Wenn du Interesse daran hast, an Software für Privatsphäre und Anonymität zu programmieren, benutzerfreundliche Webseiten oder Schnittstellen zu entwerfen oder Anleitungen für Nutzer zu schreiben: Komm und chatte mit uns auf IRC oder Twitter! Wir begrüßen immer gerne neue Mitglieder in unserer Community.

Wir werden hier regelmäßig Berichte veröffentlichen, aber du kannst unseren Fortschritt auch über den Hashtag #I2PSummer auf Twitter verfolgen und deine eigenen Ideen und Projekte teilen. Auf in den Sommer!
