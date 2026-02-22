---
title: "Verwendung eines Git-Bundles zum Abrufen des I2P-Quellcodes"
description: "Klonen großer Repositories über I2P mit Git-Bundles und BitTorrent"
slug: "git-bundle"
aliases:
  - "/de/docs/applications/git"
  - "/de/docs/applications/git/"
lastUpdated: "2020-09"
accurateFor: "0.9.47"
---

Das Klonen großer Software-Repositories über I2P kann schwierig sein, und die Verwendung von git kann dies manchmal noch schwieriger machen. Glücklicherweise kann es auch manchmal einfacher machen. Git verfügt über einen `git bundle`-Befehl, der verwendet werden kann, um ein git-Repository in eine Datei umzuwandeln, aus der git dann von einem Speicherort auf Ihrer lokalen Festplatte klonen, abrufen oder importieren kann. Durch die Kombination dieser Funktion mit BitTorrent-Downloads können wir unsere verbleibenden Probleme mit `git clone` lösen.

---

## Bevor Sie beginnen

Wenn Sie ein git bundle generieren möchten, **müssen** Sie bereits eine vollständige Kopie des **git** Repositorys besitzen, nicht das mtn Repository. Sie können es von github oder von git.idk.i2p erhalten, aber ein shallow clone (ein Klon mit --depth=1) *wird nicht funktionieren*. Es wird stillschweigend fehlschlagen und etwas erstellen, das wie ein Bundle aussieht, aber wenn Sie versuchen, es zu klonen, wird es fehlschlagen. Wenn Sie nur ein vorgeneriertes git bundle abrufen, dann gilt dieser Abschnitt nicht für Sie.

---

## I2P-Quellcode über Bittorrent herunterladen

Jemand muss Ihnen eine Torrent-Datei oder einen Magnet-Link zur Verfügung stellen, der einem bereits vorhandenen `git bundle` entspricht, das bereits für Sie erstellt wurde. Ein aktuelles, korrekt erstelltes Bundle des mainline i2p.i2p Quellcodes vom Mittwoch, 18. März 2020, finden Sie innerhalb von I2P in meinem pastebin [paste.idk.i2p/f/4hq37i](http://paste.idk.i2p/f/4h137i).

Sobald Sie ein Bundle haben, müssen Sie git verwenden, um ein funktionierendes Repository daraus zu erstellen. Wenn Sie GNU/Linux und i2psnark verwenden, sollte sich das git Bundle in $HOME/.i2p/i2psnark befinden oder, als Service unter Debian, in /var/lib/i2p/i2p-config/i2psnark. Wenn Sie BiglyBT unter GNU/Linux verwenden, befindet es sich wahrscheinlich stattdessen in "$HOME/BiglyBT Downloads/". Die Beispiele hier setzen I2PSnark unter GNU/Linux voraus. Wenn Sie etwas anderes verwenden, ersetzen Sie den Pfad zum Bundle durch das Download-Verzeichnis, das von Ihrem Client und Ihrer Plattform bevorzugt wird.

### Verwendung von `git clone`

Das Klonen aus einem Git-Bundle ist einfach, nur:

```
git clone $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
Falls Sie den folgenden Fehler erhalten, versuchen Sie stattdessen `git init` und `git fetch` manuell zu verwenden.

```
fatal: multiple updates for ref 'refs/remotes/origin/master' not allowed
```
### Verwendung von `git init` und `git fetch`

Erstellen Sie zunächst ein i2p.i2p-Verzeichnis, das in ein Git-Repository umgewandelt werden soll.

```
mkdir i2p.i2p && cd i2p.i2p
```
Als nächstes initialisieren Sie ein leeres Git-Repository, um Änderungen wieder hineinzuholen.

```
git init
```
Schließlich holen Sie das Repository aus dem Bundle.

```
git fetch $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
### Ersetze das Bundle-Remote mit dem Upstream-Remote

Nachdem Sie nun ein Bundle haben, können Sie mit Änderungen auf dem Laufenden bleiben, indem Sie das Remote auf die Quelle des Upstream-Repositorys setzen.

```
git remote set-url origin git@127.0.0.1:I2P_Developers/i2p.i2p
```
---

## Erstellen eines Bundles

Folgen Sie zunächst der [Git-Anleitung für Benutzer](/docs/applications/git/) bis Sie einen erfolgreich mit `--unshallow` geklonten i2p.i2p Repository haben. Falls Sie bereits einen Klon haben, stellen Sie sicher, dass Sie `git fetch --unshallow` ausführen bevor Sie ein Torrent-Bündel erstellen.

Sobald Sie das haben, führen Sie einfach das entsprechende ant-Target aus:

```
ant git-bundle
```
und kopieren Sie das resultierende Bundle in Ihr I2PSnark Downloads-Verzeichnis. Zum Beispiel:

```
cp i2p.i2p.bundle* $HOME/.i2p/i2psnark/
```
In ein oder zwei Minuten wird I2PSnark den Torrent erkennen. Klicken Sie auf die "Start"-Schaltfläche, um mit dem Seeden des Torrents zu beginnen.
