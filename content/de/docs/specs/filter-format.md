---
title: "Zugriffsfilterfurmat"
description: "Syntax für tunnel-Zugriffskontroll-Filterdateien"
slug: "filter-format"
lastUpdated: "2025-05"
accurateFor: "0.9.66"
type: docs
---

## Überblick

Die Definition eines Filters ist eine Liste von Strings. Leere Zeilen und Zeilen, die mit `#` beginnen, werden ignoriert. Änderungen in der Filterdefinition werden beim Neustart des tunnels wirksam.

Jede Zeile kann eines dieser Elemente repräsentieren:

- Definition eines Standard-Schwellenwerts, der auf alle entfernten Ziele angewendet wird, die nicht in dieser Datei oder einer der referenzierten Dateien aufgelistet sind
- Definition eines Schwellenwerts, der auf ein bestimmtes entferntes Ziel angewendet wird
- Definition eines Schwellenwerts, der auf entfernte Ziele angewendet wird, die in einer Datei aufgelistet sind
- Definition eines Schwellenwerts, bei dessen Überschreitung das verursachende entfernte Ziel in einer angegebenen Datei aufgezeichnet wird

Die Reihenfolge der Definitionen ist wichtig. Der erste Schwellenwert für ein bestimmtes Ziel (ob explizit oder in einer Datei aufgelistet) überschreibt alle zukünftigen Schwellenwerte für dasselbe Ziel, ob explizit oder in einer Datei aufgelistet.

## Schwellenwerte

Ein Schwellenwert wird durch die Anzahl der Verbindungsversuche definiert, die ein entferntes Ziel über eine bestimmte Anzahl von Sekunden durchführen darf, bevor eine "Verletzung" auftritt. Zum Beispiel bedeutet die folgende Schwellenwert-Definition `15/5`, dass dasselbe entfernte Ziel 14 Verbindungsversuche über einen Zeitraum von 5 Sekunden durchführen darf. Wenn es einen weiteren Versuch innerhalb desselben Zeitraums unternimmt, wird der Schwellenwert verletzt.

Das Schwellenwertformat kann eines der folgenden sein:

- **Numerische Definition** der Anzahl von Verbindungen über die Anzahl von Sekunden - `15/5`, `30/60`, und so weiter. Beachten Sie, dass wenn die Anzahl der Verbindungen 1 ist (wie zum Beispiel bei `1/1`) der erste Verbindungsversuch zu einer Überschreitung führt.
- Das Wort **`allow`**. Diese Schwelle wird niemals überschritten, d.h. eine unbegrenzte Anzahl von Verbindungsversuchen ist erlaubt.
- Das Wort **`deny`**. Diese Schwelle wird immer überschritten, d.h. keine Verbindungsversuche werden zugelassen.

### Standard-Schwellenwert

Der Standard-Schwellenwert gilt für alle entfernten Ziele, die nicht explizit in der Definition oder in einer der referenzierten Dateien aufgelistet sind. Um einen Standard-Schwellenwert zu setzen, verwenden Sie das Schlüsselwort `default`. Die folgenden sind Beispiele für Standard-Schwellenwerte:

```text
15/5 default
allow default
deny default
```
Es kann nur eine Definition eines Standard-Schwellenwerts pro Filter geben. Wird dieser weggelassen, erlaubt der Filter unbekannte Verbindungen standardmäßig.

### Explizite Schwellenwerte

Explizite Schwellenwerte werden auf ein entferntes Ziel angewendet, das in der Definition selbst aufgeführt ist. Beispiele:

```text
15/5 explicit asdfasdfasdf.b32.i2p
allow explicit fdsafdsafdsa.b32.i2p
deny explicit qwerqwerqwer.b32.i2p
```
### Bulk-Schwellenwerte

Der Einfachheit halber ist es möglich, eine Liste von Zielen in einer Datei zu führen und einen Schwellwert für alle gemeinsam zu definieren. Beispiele:

```text
15/5 file /path/throttled_destinations.txt
deny file /path/forbidden_destinations.txt
allow file /path/unlimited_destinations.txt
```
Diese Dateien können während des laufenden tunnel-Betriebs manuell bearbeitet werden. Änderungen an diesen Dateien können bis zu 10 Sekunden dauern, bis sie wirksam werden.

## Rekorder

Recorder verfolgen Verbindungsversuche, die von einem entfernten Ziel gemacht werden, und wenn dies einen bestimmten Schwellenwert überschreitet, wird dieses Ziel in einer bestimmten Datei aufgezeichnet. Beispiele:

```text
30/5 record /path/aggressive.txt
60/5 record /path/very_aggressive.txt
```
Es ist möglich, einen Recorder zu verwenden, um aggressive Ziele in eine bestimmte Datei aufzuzeichnen und diese Datei dann zu verwenden, um sie zu drosseln. Zum Beispiel definiert das folgende Code-Snippet einen Filter, der zunächst alle Verbindungsversuche erlaubt, aber wenn ein einzelnes Ziel 30 Versuche pro 5 Sekunden überschreitet, wird es auf 15 Versuche pro 5 Sekunden gedrosselt:

```text
# by default there are no limits
allow default
# but record overly aggressive destinations
30/5 record /path/throttled.txt
# and any that end up in that file will get throttled in the future
15/5 file /path/throttled.txt
```
Es ist möglich, einen Recorder in einem tunnel zu verwenden, der in eine Datei schreibt, die einen anderen tunnel drosselt. Es ist möglich, dieselbe Datei mit Zielen in mehreren tunnels wiederzuverwenden. Und natürlich ist es möglich, diese Dateien von Hand zu bearbeiten.

Hier ist ein Beispiel für eine Filterdefinition, die standardmäßig etwas Drosselung anwendet, keine Drosselung für Ziele in der Datei `friends.txt`, alle Verbindungen von Zielen in der Datei `enemies.txt` verbietet und jedes aggressive Verhalten in einer Datei namens `suspicious.txt` aufzeichnet:

```text
15/5 default
allow file /path/friends.txt
deny file /path/enemies.txt
60/5 record /path/suspicious.txt
```